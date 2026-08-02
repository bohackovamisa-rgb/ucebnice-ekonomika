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
        st.error("⚠️ V nastavení Streamlit Secrets chybí proměnná APP_PASSWORD! Přidejte ji.")
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
    /* Schování podtržení u našich interních odkazů, aby vypadaly jako přirozený text */
    a { text-decoration: none; font-weight: bold; }
    a:hover { text-decoration: underline; }
    </style>
""", unsafe_allow_html=True)

NOTION_TOKEN = st.secrets["NOTION_TOKEN"]
MAIN_PAGE_ID = st.secrets["PAGE_ID"]

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28"
}

# --- UNIVERZÁLNÍ ZPRACOVÁNÍ ID STRÁNEK ---
def format_uuid(id_str):
    clean = id_str.replace("-", "")
    if len(clean) == 32:
        return f"{clean[:8]}-{clean[8:12]}-{clean[12:16]}-{clean[16:20]}-{clean[20:]}"
    return id_str

# Nativní Streamlit navigace přes URL parametry (Zaručuje 100% funkčnost odkazů)
if "page" in st.query_params:
    target_page = format_uuid(st.query_params["page"])
    if st.session_state.get("current_page_id") != target_page:
        st.session_state["current_page_id"] = target_page
elif "current_page_id" not in st.session_state:
    st.session_state["current_page_id"] = format_uuid(MAIN_PAGE_ID)

def extract_notion_id(href_or_text):
    if not href_or_text: return None
    clean_url = href_or_text.split('?')[0].split('#')[0]
    match = re.search(r'([a-fA-F0-9]{8}-?[a-fA-F0-9]{4}-?[a-fA-F0-9]{4}-?[a-fA-F0-9]{4}-?[a-fA-F0-9]{12}|[a-fA-F0-9]{32})', clean_url)
    if match: return format_uuid(match.group(1))
    return None

def is_notion_link(href):
    if not href: return False
    return "notion.so" in href or "notion.site" in href or extract_notion_id(href) is not None

# --- FORMÁTOVÁNÍ TEXTU A PŘEVOD ODKAZŮ ---
def rich_text_to_markdown(rich_text_list):
    """Místo ošklivých tlačítek udělá z Notionu přirozené klikací odkazy"""
    if not rich_text_list: return ""
    md_text = ""
    for t in rich_text_list:
        text = t.get("plain_text", "")
        annotations = t.get("annotations", {})
        href = t.get("href")
        
        is_internal = False
        page_id = None
        
        # Rozpoznání interních zmínek a odkazů
        if t.get("type") == "mention" and t.get("mention", {}).get("type") == "page":
            is_internal = True
            page_id = format_uuid(t["mention"]["page"]["id"])
        elif t.get("type") == "mention" and t.get("mention", {}).get("type") == "database":
            is_internal = True
            page_id = format_uuid(t["mention"]["database"]["id"])
        elif href and is_notion_link(href):
            is_internal = True
            page_id = extract_notion_id(href)
            
        # Zpracování tučnosti/kurzívy
        if annotations.get("bold"): text = f"**{text}**"
        if annotations.get("italic"): text = f"*{text}*"
        if annotations.get("strikethrough"): text = f"~~{text}~~"
        if annotations.get("code"): text = f"`{text}`"
        
        # Vytvoření klikacího odkazu přímo v textu
        if is_internal and page_id and text:
            text = f"[{text}](?page={page_id})"
        elif href and text:
            text = f"[{text}]({href})"
            
        md_text += text
    return md_text

# --- API NOTION ---
def fetch_notion_blocks(block_id):
    all_blocks = []
    url = f"https://api.notion.com/v1/blocks/{format_uuid(block_id)}/children?page_size=100"
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
    url = f"https://api.notion.com/v1/databases/{format_uuid(db_id)}/query"
    pages = []
    try:
        res = requests.post(url, headers=headers)
        if res.status_code == 200:
            for p in res.json().get("results", []):
                title = "Bez názvu"
                for key, val in p.get("properties", {}).items():
                    if val.get("type") == "title" and val.get("title"):
                        title = rich_text_to_markdown(val["title"])
                pages.append({"id": format_uuid(p["id"]), "title": title})
    except Exception: pass
    return pages

# --- BOČNÍ PANEL A KAPITOLY ---
def discover_chapters(blocks):
    raw_chapters = []
    def scan_blocks(block_list):
        for b in block_list:
            if b.get("type") == "child_page":
                title = b["child_page"]["title"].strip()
                if title and "řídící centrum" not in title.lower():
                    raw_chapters.append({"id": format_uuid(b["id"]), "title": title})
            elif b.get("type") == "child_database":
                raw_chapters.extend(fetch_database_pages(b["id"]))
            elif b.get("type") == "column_list":
                cols = fetch_notion_blocks(b["id"])
                for col in cols: scan_blocks(fetch_notion_blocks(col["id"]))
    scan_blocks(blocks)
    
    # Seřazení podle čísla kapitoly v názvu
    chapters_by_num, other_chapters = {}, []
    for ch in raw_chapters:
        match = re.search(r'(?:kapitola\s*|0)?(\d+)', ch["title"].lower())
        num = int(match.group(1)) if match else 999
        if num != 999: chapters_by_num[num] = ch
        elif not any(o["title"] == ch["title"] for o in other_chapters): other_chapters.append(ch)
    
    sorted_chapters = [chapters_by_num[k] for k in sorted(chapters_by_num.keys())] + other_chapters
    return sorted_chapters

chapters = discover_chapters(fetch_notion_blocks(MAIN_PAGE_ID))

with st.sidebar:
    st.title("📚 Učebnice Ekonomiky")
    st.divider()
    if st.button("🏠 Úvodní stránka", use_container_width=True):
        st.session_state["current_page_id"] = format_uuid(MAIN_PAGE_ID)
        if "page" in st.query_params: del st.query_params["page"]
        st.rerun()
        
    st.divider()
    st.subheader("Kapitoly")
    for ch in chapters:
        if st.button(f"📖 {ch['title']}", key=f"side_{ch['id']}", use_container_width=True):
            st.session_state["current_page_id"] = ch["id"]
            st.query_params["page"] = ch["id"]
            st.rerun()
            
    st.divider()
    if st.button("🔒 Odhlásit", use_container_width=True):
        st.session_state["password_correct"] = False
        st.rerun()

# --- DETEKTOR FORMULÁŘŮ (Zabraňuje chybným textovým polím) ---
def is_completion_prompt(text):
    clean = re.sub(r"^[\*\_\#\d\.\s\[\]\(\)\?]+", "", text.strip()).lower()
    explicit_prefixes = (
        "doplň:", "doplňte:", "úkol:", "otázka:", "odpověď:",
        "název projektu:", "jedna věta projektu:", "zákazník:", "problém:", 
        "hodnota pro zákazníka:", "řešení:", "konkurence:", "cena:", 
        "jednorázové náklady:", "fixní náklady:", "variabilní náklady:", 
        "první test:", "metrika úspěchu:", "rizika:", "právní forma:", 
        "etické pravidlo:", "rozhodnutí:"
    )
    if clean.startswith(explicit_prefixes): return True
    reflection_phrases = ("předpokládali jsme", "ověřili jsme", "naměřili jsme", "zjistili jsme", "proto teď rozhodujeme")
    if any(clean.startswith(p) for p in reflection_phrases): return True
    if (clean.endswith(("…", "...", "___")) or "…" in clean or "..." in clean) and len(clean) < 200: return True
    return False

def render_text_or_input(text, block_id):
    if is_completion_prompt(text):
        clean_lower = re.sub(r"^[\*\_\#\s]+", "", text.strip()).lower()
        label_text = text.replace("**", "").replace("*", "").strip()
        label_text = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", label_text) # Očištění od Markdown zbytků
        icon = "✏️"
        if "projekt" in clean_lower: icon = "🚀"
        elif "zákazník" in clean_lower: icon = "👥"
        elif "problém" in clean_lower: icon = "🚨"
        elif "řešení" in clean_lower or "hodnot" in clean_lower: icon = "💡"
        elif "cen" in clean_lower or "náklad" in clean_lower: icon = "💰"
        
        long_prompts = ("problém", "hodnota", "řešení", "konkurence", "rizika", "pravidlo", "věta", "předpokládali", "ověřili", "naměřili", "zjistili")
        is_long = any(p in clean_lower for p in long_prompts)
        
        with st.container(border=True):
            st.markdown(f"**{icon} {label_text}**")
            if is_long: st.text_area("Odpo", label_visibility="collapsed", placeholder="Zde se rozepište...", key=f"input_{block_id}", height=100)
            else: st.text_input("Odpo", label_visibility="collapsed", placeholder="Stručná odpověď...", key=f"input_{block_id}")
    else: 
        st.markdown(text)

# --- VYKRESLENÍ BLOKŮ ---
def render_block(block):
    b_type = block.get("type")
    rich_text_data = block.get(b_type, {}).get("rich_text", []) if b_type in block else []
    text = rich_text_to_markdown(rich_text_data)

    if b_type == "heading_1":
        if is_completion_prompt(text): render_text_or_input(text, block["id"])
        else: st.markdown(f"# {text}")
    elif b_type == "heading_2":
        if is_completion_prompt(text): render_text_or_input(text, block["id"])
        else: st.markdown(f"## {text}")
    elif b_type == "heading_3":
        if is_completion_prompt(text): render_text_or_input(text, block["id"])
        else: st.markdown(f"### {text}")
    elif b_type == "paragraph":
        if text:
            if is_completion_prompt(text): render_text_or_input(text, block["id"])
            else: st.markdown(text)
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
            label_text = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", label_text)
            with st.container(border=True):
                st.info(f"{icon} {label_text}")
                st.text_area("Vaše odpověď:", label_visibility="collapsed", placeholder="Zde se rozepište...", key=f"callout_input_{block['id']}", height=100)
        else:
            st.info(text if text else " ", icon=icon)
        if block.get("has_children"): render_children(block["id"])
    elif b_type == "toggle":
        with st.expander(text or "Zobrazit detail"):
            render_children(block["id"])
    elif b_type == "to_do":
        checked = block["to_do"].get("checked", False)
        st.checkbox(text, value=checked, key=f"todo_{block['id']}")
    elif b_type == "image":
        img_url = block["image"].get("file", {}).get("url") or block["image"].get("external", {}).get("url")
        if img_url: st.image(img_url)
    elif b_type == "divider":
        st.divider()
    elif b_type == "table":
        rows = fetch_notion_blocks(block["id"])
        if rows:
            has_header = block.get("table", {}).get("has_column_header", False)
            table_matrix = [[rich_text_to_markdown(c).replace("|", "\\|") for c in r["table_row"].get("cells", [])] for r in rows if r.get("type") == "table_row"]
            if table_matrix:
                num_cols = len(table_matrix[0])
                headers_row, data_rows = (table_matrix[0], table_matrix[1:]) if has_header and len(table_matrix) > 1 else ([""] * num_cols, table_matrix)
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
            st.markdown(f"### [📖 {title}](?page={format_uuid(block['id'])})")
    elif b_type == "link_to_page":
        page_id = block.get("link_to_page", {}).get("page_id")
        if page_id:
            st.markdown(f"[🔗 Přejít na připojenou stránku](?page={format_uuid(page_id)})")
    elif b_type == "synced_block":
        target_id = block.get("synced_block", {}).get("synced_from", {}).get("block_id") or block["id"]
        render_children(target_id)

def render_children(block_id):
    for child in fetch_notion_blocks(block_id): render_block(child)

# --- VYKRESLENÍ OBSAHU ---
active_blocks = fetch_notion_blocks(st.session_state["current_page_id"])
col1, main_col, col2 = st.columns([1, 4, 1])
with main_col:
    with st.container(border=True):
        if active_blocks:
            for block in active_blocks: render_block(block)
        else:
            st.warning("⚠️ Obsah se nepodařilo načíst (Ověřte sdílení stránky u integrace v Notionu).")
