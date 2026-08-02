import streamlit as st
import requests
import re

# 1. Konfigurace stránky
st.set_page_config(
    page_title="Ekonomika - Učebnice",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- PŘIHLAŠOVACÍ BRÁNA ---
def check_password():
    app_pwd = st.secrets.get("APP_PASSWORD")
    if not app_pwd:
        st.error("⚠️ V nastavení Streamlit Secrets chybí proměnná APP_PASSWORD! Přidejte ji v nastavení aplikace.")
        return False
        
    if st.session_state.get("password_correct", False):
        return True

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        with st.container(border=True):
            st.title("🔒 Soukromá učebnice")
            st.info("Tato aplikace je uzamčena. Zadejte přístupové heslo.")
            password = st.text_input("Heslo:", type="password")
            if st.button("Vstoupit", use_container_width=True):
                if password == app_pwd:
                    st.session_state["password_correct"] = True
                    st.rerun()
                else:
                    st.error("❌ Nesprávné heslo!")
    return False

if not check_password():
    st.stop()

# --- VZHLED ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stTextInput input, .stTextArea textarea {
        border-radius: 8px !important;
        border: 1px solid #cbd5e1 !important;
        background-color: #ffffff !important;
    }
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #2563eb !important;
        box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.2) !important;
    }
    h1, h2, h3 { color: #1e293b; font-weight: 700; }
    </style>
""", unsafe_allow_html=True)

NOTION_TOKEN = st.secrets["NOTION_TOKEN"]
MAIN_PAGE_ID = st.secrets["PAGE_ID"]

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28"
}

if "current_page_id" not in st.session_state:
    st.session_state["current_page_id"] = MAIN_PAGE_ID

# --- ZPRACOVÁNÍ EXTERNÍCH A INTERNÍCH ODKAZŮ ---
def extract_notion_id(href_or_text):
    if not href_or_text: return None
    url_main = href_or_text.split('#')[0]
    match = re.search(r'([a-fA-F0-9]{32}|[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12})', url_main)
    if match: return match.group(1).replace("-", "")
    return None

def is_notion_link(href):
    if not href: return False
    return "notion.so" in href or "notion.site" in href or extract_notion_id(href) is not None

def get_internal_links(rich_text_list):
    internal_links = []
    if not rich_text_list: return internal_links
    for t in rich_text_list:
        page_id = None
        href = t.get("href", "")
        if t.get("type") == "mention":
            mention_data = t.get("mention", {})
            if mention_data.get("type") == "page":
                page_id = mention_data["page"]["id"].replace("-", "")
            elif mention_data.get("type") == "database":
                page_id = mention_data["database"]["id"].replace("-", "")
        elif href and is_notion_link(href):
            page_id = extract_notion_id(href)
            
        if page_id:
            link_text = t.get("plain_text", "Otevřít kapitolu").strip()
            if not any(l["id"] == page_id for l in internal_links):
                internal_links.append({"text": link_text, "id": page_id})
    return internal_links

# --- FORMÁTOVÁNÍ TEXTU ---
def rich_text_to_markdown(rich_text_list):
    if not rich_text_list: return ""
    md_text = ""
    for t in rich_text_list:
        text = t.get("plain_text", "")
        annotations = t.get("annotations", {})
        href = t.get("href")
        if annotations.get("bold"): text = f"**{text}**"
        if annotations.get("italic"): text = f"*{text}*"
        if annotations.get("strikethrough"): text = f"~~{text}~~"
        if annotations.get("code"): text = f"`{text}`"
        
        if is_notion_link(href) or (t.get("type") == "mention" and t.get("mention", {}).get("type") == "page"):
            text = f"**{text}**"
        elif href: text = f"[{text}]({href})"
        md_text += text
    return md_text

# --- API LEČENÍ ---
def fetch_notion_blocks(block_id):
    all_blocks = []
    url = f"https://api.notion.com/v1/blocks/{block_id}/children?page_size=100"
    has_more = True
    start_cursor = None
    while has_more:
        params_url = url + (f"&start_cursor={start_cursor}" if start_cursor else "")
        try:
            res = requests.get(params_url, headers=headers)
            if res.status_code == 200:
                data = res.json()
                all_blocks.extend(data.get("results", []))
                has_more = data.get("has_more", False)
                start_cursor = data.get("next_cursor")
            else: break
        except Exception: break
    return all_blocks

def fetch_database_pages(db_id):
    url = f"https://api.notion.com/v1/databases/{db_id}/query"
    pages = []
    try:
        res = requests.post(url, headers=headers)
        if res.status_code == 200:
            for p in res.json().get("results", []):
                title = "Bez názvu"
                props = p.get("properties", {})
                for key, val in props.items():
                    if val.get("type") == "title" and val.get("title"):
                        title = rich_text_to_markdown(val["title"])
                pages.append({"id": p["id"], "title": title})
    except Exception: pass
    return pages

# --- KAPITOLY A NAVIGATION ---
def extract_chapter_number(title):
    match = re.search(r'(?:kapitola\s*|0)?(\d+)', title.lower())
    if match: return int(match.group(1))
    return 999

def discover_chapters(blocks):
    raw_chapters = []
    def scan_blocks(block_list):
        for b in block_list:
            b_type = b.get("type")
            if b_type == "child_page":
                title = b["child_page"]["title"].strip()
                if title and "řídící centrum" not in title.lower() and "dashboard" not in title.lower():
                    raw_chapters.append({"id": b["id"], "title": title})
            elif b_type == "child_database":
                db_pages = fetch_database_pages(b["id"])
                raw_chapters.extend(db_pages)
            elif b_type == "column_list":
                cols = fetch_notion_blocks(b["id"])
                for col in cols: scan_blocks(fetch_notion_blocks(col["id"]))

    scan_blocks(blocks)
    chapters_by_num = {}
    other_chapters = []

    for ch in raw_chapters:
        title = ch["title"].strip()
        num = extract_chapter_number(title)
        if num != 999:
            if num not in chapters_by_num: chapters_by_num[num] = ch
            else:
                if "kapitola" in title.lower() and "kapitola" not in chapters_by_num[num]["title"].lower():
                    chapters_by_num[num] = ch
        else:
            if not any(o["title"] == title for o in other_chapters):
                other_chapters.append(ch)

    sorted_chapters = [chapters_by_num[k] for k in sorted(chapters_by_num.keys())]
    sorted_chapters.extend(other_chapters)
    return sorted_chapters

main_blocks = fetch_notion_blocks(MAIN_PAGE_ID)
chapters = discover_chapters(main_blocks)

# --- SIDEBAR ---
with st.sidebar:
    st.title("📚 Učebnice Ekonomiky")
    st.divider()
    if st.button("🏠 Úvodní stránka", use_container_width=True):
        st.session_state["current_page_id"] = MAIN_PAGE_ID
        st.rerun()
        
    st.divider()
    st.subheader("Kapitoly")
    for ch in chapters:
        if st.button(f"📖 {ch['title']}", key=f"side_{ch['id']}", use_container_width=True):
            st.session_state["current_page_id"] = ch["id"]
            st.rerun()
            
    st.divider()
    if st.button("🔒 Odhlásit", use_container_width=True):
        st.session_state["password_correct"] = False
        st.rerun()

# --- PŘÍSNÝ DETEKTOR INTERAKTIVNÍCH FORMULÁŘŮ ---
def is_completion_prompt(text):
    clean = re.sub(r"^[\*\_\#\d\.\s]+", "", text.strip()).lower()
    
    # Vyžadujeme dvojtečku u jednoslovných/klíčových slov
    explicit_prefixes = (
        "doplň:", "doplňte:", "úkol:", "otázka:", "odpověď:",
        "název projektu:", "jedna věta projektu:", "zákazník:", "problém:", 
        "hodnota pro zákazníka:", "řešení:", "konkurence:", "cena:", 
        "jednorázové náklady:", "fixní náklady:", "variabilní náklady:", 
        "první test:", "metrika úspěchu:", "rizika:", "právní forma:", 
        "etické pravidlo:", "rozhodnutí:"
    )
    if clean.startswith(explicit_prefixes): return True
        
    reflection_phrases = (
        "předpokládali jsme", "ověřili jsme", "naměřili jsme", 
        "zjistili jsme", "proto teď rozhodujeme"
    )
    if any(clean.startswith(p) for p in reflection_phrases): return True
        
    if (clean.endswith(("…", "...", "___")) or "…" in clean or "..." in clean) and len(clean) < 200:
        return True
        
    return False

def render_text_or_input(text, block_id):
    if is_completion_prompt(text):
        clean_lower = re.sub(r"^[\*\_\#\s]+", "", text.strip()).lower()
        label_text = text.replace("**", "").replace("*", "").strip()
        icon = "✏️"
        if "název projektu" in clean_lower: icon = "🚀"
        elif "jedna věta" in clean_lower: icon = "🎯"
        elif "zákazník" in clean_lower: icon = "👥"
        elif "problém" in clean_lower: icon = "🚨"
        elif "hodnota" in clean_lower: icon = "💎"
        elif "řešení" in clean_lower: icon = "💡"
        elif "konkurence" in clean_lower or "alternativy" in clean_lower: icon = "🥊"
        elif "cena" in clean_lower: icon = "🏷️"
        elif "náklad" in clean_lower: icon = "💰"
        elif "test" in clean_lower: icon = "🧪"
        elif "metrika" in clean_lower: icon = "📊"
        elif "rizik" in clean_lower: icon = "⚠️"
        elif "právní" in clean_lower or "etické" in clean_lower: icon = "⚖️"
        elif "rozhodnutí" in clean_lower: icon = "🧭"
        
        long_prompts = ("problém", "hodnota pro zákazníka", "řešení", "konkurence", "první test", "rizika", "etické pravidlo", "jedna věta projektu", "předpokládali jsme", "ověřili jsme", "naměřili jsme", "zjistili jsme")
        is_long = any(p in clean_lower for p in long_prompts)
        
        with st.container(border=True):
            st.markdown(f"**{icon} {label_text}**")
            if is_long: st.text_area(label=label_text, label_visibility="collapsed", placeholder="Zde se rozepište...", key=f"input_{block_id}", height=100)
            else: st.text_input(label=label_text, label_visibility="collapsed", placeholder="Stručná odpověď...", key=f"input_{block_id}")
    else: st.markdown(text)

# --- VYKRESLENÍ JEDNOTLIVÝCH BLOKŮ ---
def render_block(block):
    b_type = block.get("type")
    
    rich_text_data = block.get(b_type, {}).get("rich_text", []) if b_type in block else []
    internal_links = get_internal_links(rich_text_data)
    text = rich_text_to_markdown(rich_text_data)

    # 1. ČISTÁ NAVIGAČNÍ DLAŽDICE (Pokud blok obsahuje odkaz na jinou stránku)
    if internal_links and not is_completion_prompt(text):
        icon = "📖"
        if b_type == "callout":
            icon_data = block.get("callout", {}).get("icon", {})
            icon = icon_data.get("emoji") if icon_data.get("type") == "emoji" else "💡"
        
        for idx, link in enumerate(internal_links):
            btn_label = f"{icon} {link['text']}"
            if st.button(btn_label, key=f"nav_card_{block['id']}_{idx}", use_container_width=True):
                st.session_state["current_page_id"] = link["id"]
                st.rerun()
        if block.get("has_children"): render_children(block["id"])
        return

    # 2. STANDARDNÍ VYKRESLOVÁNÍ
    if b_type == "heading_1":
        if is_completion_prompt(text): render_text_or_input(text, block["id"])
        else: st.title(text)

    elif b_type == "heading_2":
        if is_completion_prompt(text): render_text_or_input(text, block["id"])
        else: st.header(text)

    elif b_type == "heading_3":
        if is_completion_prompt(text): render_text_or_input(text, block["id"])
        else: st.subheader(text)

    elif b_type == "paragraph":
        if text: render_text_or_input(text, block["id"])

    elif b_type == "bulleted_list_item":
        if is_completion_prompt(text): render_text_or_input(text, block["id"])
        else: st.markdown(f"* {text}")
        if block.get("has_children"): render_children(block["id"])

    elif b_type == "numbered_list_item":
        if is_completion_prompt(text): render_text_or_input(text, block["id"])
        else: st.markdown(f"1. {text}")
        if block.get("has_children"): render_children(block["id"])

    elif b_type == "callout":
        icon_data = block.get("callout", {}).get("icon", {})
        icon = icon_data.get("emoji") if icon_data.get("type") == "emoji" else "💡"
        
        if is_completion_prompt(text):
            label_text = text.replace("**", "").replace("*", "").strip()
            with st.container(border=True):
                st.info(f"{icon} {label_text}")
                st.text_area("Vaše odpověď:", label_visibility="collapsed", placeholder="Zde se rozepište...", key=f"callout_input_{block['id']}", height=100)
        else:
            st.info(text if text else "Informace", icon=icon)
            
        if block.get("has_children"): render_children(block["id"])

    elif b_type == "toggle":
        title = rich_text_to_markdown(rich_text_data)
        with st.expander(title or "Zobrazit detail"):
            render_children(block["id"])

    elif b_type == "to_do":
        checked = block["to_do"].get("checked", False)
        st.checkbox(text, value=checked, key=f"todo_{block['id']}")

    elif b_type == "image":
        img_data = block["image"]
        img_url = img_data.get("file", {}).get("url") or img_data.get("external", {}).get("url")
        if img_url: st.image(img_url)

    elif b_type == "divider":
        st.divider()

    elif b_type == "table":
        rows_blocks = fetch_notion_blocks(block["id"])
        if rows_blocks:
            has_header = block.get("table", {}).get("has_column_header", False)
            table_matrix = []
            for r in rows_blocks:
                if r.get("type") == "table_row":
                    cells = r["table_row"].get("cells", [])
                    table_matrix.append([rich_text_to_markdown(c).replace("|", "\\|") for c in cells])
            if table_matrix:
                num_cols = len(table_matrix[0])
                if has_header and len(table_matrix) > 1:
                    headers_row, data_rows = table_matrix[0], table_matrix[1:]
                else:
                    headers_row, data_rows = [""] * num_cols, table_matrix
                md_table = "| " + " | ".join(headers_row) + " |\n| " + " | ".join(["---"] * num_cols) + " |\n"
                for row in data_rows: md_table += "| " + " | ".join(row + [""] * (num_cols - len(row))) + " |\n"
                st.markdown(md_table)

    elif b_type == "column_list":
        cols_blocks = fetch_notion_blocks(block["id"])
        if cols_blocks:
            cols = st.columns(len(cols_blocks))
            for idx, col_block in enumerate(cols_blocks):
                with cols[idx]: render_children(col_block["id"])

    elif b_type == "child_page":
        title = block["child_page"]["title"]
        if "řídící centrum" not in title.lower():
            if st.button(f"📖 {title}", key=f"page_{block['id']}", use_container_width=True):
                st.session_state["current_page_id"] = block["id"].replace("-", "")
                st.rerun()

    elif b_type == "link_to_page":
        page_id = block.get("link_to_page", {}).get("page_id")
        if page_id:
            if st.button("🔗 Přejít na kapitolu", key=f"link_{block['id']}", use_container_width=True):
                st.session_state["current_page_id"] = page_id.replace("-", "")
                st.rerun()

    elif b_type == "synced_block":
        synced_from = block.get("synced_block", {}).get("synced_from")
        target_id = synced_from.get("block_id") if synced_from else block["id"]
        render_children(target_id)

def render_children(block_id):
    children = fetch_notion_blocks(block_id)
    for child in children: render_block(child)

# --- VYSVÍCENÍ OBSAHU ---
active_blocks = fetch_notion_blocks(st.session_state["current_page_id"])

col1, main_col, col2 = st.columns([1, 4, 1])

with main_col:
    with st.container(border=True):
        if active_blocks:
            for block in active_blocks: render_block(block)
        else:
            st.info("Obsah se načítá nebo je tato stránka prázdná...")
