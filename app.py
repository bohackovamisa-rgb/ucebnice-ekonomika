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

# Vlastní CSS
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

# Načtení klíčů
NOTION_TOKEN = st.secrets["NOTION_TOKEN"]
MAIN_PAGE_ID = st.secrets["PAGE_ID"]

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28"
}

if "current_page_id" not in st.session_state:
    st.session_state["current_page_id"] = MAIN_PAGE_ID

# --- POMOCNÉ FUNKCE PRO ZPRACOVÁNÍ ODKAZŮ A IKON ---
def get_internal_links(rich_text_list):
    """Získá všechna ID stránek z interních odkazů v Notionu."""
    internal_links = []
    if not rich_text_list: return internal_links
    
    for t in rich_text_list:
        page_id = None
        href = t.get("href", "")
        
        # 1. Detekce pomocí Mention (např. @Slovníček)
        if t.get("type") == "mention" and t.get("mention", {}).get("type") == "page":
            page_id = t["mention"]["page"]["id"]
        # 2. Detekce přes běžný odkaz (Ctrl+K)
        elif href and ("notion.so" in href or "notion.site" in href):
            match = re.search(r'([a-fA-F0-9]{32}|[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12})', href)
            if match:
                page_id = match.group(1).replace("-", "")
        
        if page_id:
            link_text = t.get("plain_text", "Odkaz").strip()
            # Zabránění duplikátům
            if not any(l["id"] == page_id for l in internal_links):
                internal_links.append({"text": link_text, "id": page_id})
                
    return internal_links

def get_callout_icon(block):
    """Extrahuje vlastní ikonu z Callout bloku (výchozí je 💡)."""
    icon_data = block.get("callout", {}).get("icon", {})
    if icon_data.get("type") == "emoji":
        return icon_data.get("emoji")
    return "💡"

def render_inline_buttons(links, block_id):
    """Vykreslí tlačítka pro odkazy vložené uvnitř dlouhých textů."""
    if not links: return
    for idx, link in enumerate(links):
        if st.button(f"🔗 Otevřít: {link['text']}", key=f"inline_{block_id}_{idx}"):
            st.session_state["current_page_id"] = link["id"]
            st.rerun()

# --- 1. PŘEKLADAČ FORMÁTOVÁNÍ ---
def rich_text_to_markdown(rich_text_list):
    if not rich_text_list:
        return ""
    md_text = ""
    for t in rich_text_list:
        text = t.get("plain_text", "")
        annotations = t.get("annotations", {})
        href = t.get("href")

        if annotations.get("bold"): text = f"**{text}**"
        if annotations.get("italic"): text = f"*{text}*"
        if annotations.get("strikethrough"): text = f"~~{text}~~"
        if annotations.get("code"): text = f"`{text}`"
        
        # Zabráníme prokliku ven u interních odkazů (jen je ztučníme)
        is_internal = False
        if href and ("notion.so" in href or "notion.site" in href): is_internal = True
        elif t.get("type") == "mention" and t.get("mention", {}).get("type") == "page": is_internal = True
            
        if is_internal:
            text = f"**{text}**"
        elif href:
            text = f"[{text}]({href})"
            
        md_text += text
    return md_text

# --- 2. NAČÍTÁNÍ BLOKŮ Z NOTIONU ---
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

# --- 3. DEDUPLIKACE A SEŘAZENÍ KAPITOL ---
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
                for col in cols:
                    scan_blocks(fetch_notion_blocks(col["id"]))

    scan_blocks(blocks)
    chapters_by_num = {}
    other_chapters = []

    for ch in raw_chapters:
        title = ch["title"].strip()
        num = extract_chapter_number(title)
        if num != 999:
            if num not in chapters_by_num:
                chapters_by_num[num] = ch
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

# --- 4. BOČNÍ PANEL ---
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

# --- 5. DETEKTOR INTERAKTIVNÍCH KARET A VYKRESLOVÁNÍ BLOKŮ ---
def is_completion_prompt(text):
    clean = re.sub(r"^[\*\_\#\s]+", "", text.strip()).lower()
    prompts = (
        "doplň", "úkol", "otázka", "název projektu", "jedna věta projektu", 
        "zákazník", "problém", "hodnota pro zákazníka", "řešení", 
        "konkurence", "cena", "jednorázové", "fixní", "variabilní", 
        "první test", "metrika úspěchu", "rizika", "právní forma", 
        "etické pravidlo", "rozhodnutí", "předpokládali jsme", 
        "ověřili jsme", "naměřili jsme", "zjistili jsme", "proto teď rozhodujeme"
    )
    if any(clean.startswith(p) for p in prompts): return True
    if (clean.endswith(("…", "...", "___")) or "…" in clean or "..." in clean) and len(clean) < 200: return True
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

def render_block(block):
    b_type = block.get("type")
    
    # 1. Extrakce interních odkazů z bloku
    rich_text_data = block.get(b_type, {}).get("rich_text", [])
    internal_links = get_internal_links(rich_text_data)
    block_plain_text = "".join([t.get("plain_text", "") for t in rich_text_data]).strip()

    # 2. Kontrola, zda blok neobsahuje POUZE odkaz (pak uděláme tlačítko)
    is_pure_link = False
    if len(internal_links) == 1 and internal_links[0]["text"] == block_plain_text and not is_completion_prompt(block_plain_text):
        is_pure_link = True

    if is_pure_link:
        icon = get_callout_icon(block) if b_type == "callout" else "🔗"
        if st.button(f"{icon} {internal_links[0]['text']}", key=f"pure_link_{block['id']}", use_container_width=True):
            st.session_state["current_page_id"] = internal_links[0]["id"]
            st.rerun()
        if block.get("has_children"): render_children(block["id"])
        return # Přeskočíme standardní textové vykreslování

    # 3. Standardní vykreslování bloku
    if b_type == "heading_1":
        text = rich_text_to_markdown(block["heading_1"]["rich_text"])
        if is_completion_prompt(text): render_text_or_input(text, block["id"])
        else: st.title(text)
        render_inline_buttons(internal_links, block["id"])
    elif b_type == "heading_2":
        text = rich_text_to_markdown(block["heading_2"]["rich_text"])
        if is_completion_prompt(text): render_text_or_input(text, block["id"])
        else: st.header(text)
        render_inline_buttons(internal_links, block["id"])
    elif b_type == "heading_3":
        text = rich_text_to_markdown(block["heading_3"]["rich_text"])
        if is_completion_prompt(text): render_text_or_input(text, block["id"])
        else: st.subheader(text)
        render_inline_buttons(internal_links, block["id"])
    elif b_type == "paragraph":
        text = rich_text_to_markdown(block["paragraph"]["rich_text"])
        if text: render_text_or_input(text, block["id"])
        render_inline_buttons(internal_links, block["id"])
    elif b_type == "bulleted_list_item":
        text = rich_text_to_markdown(block["bulleted_list_item"]["rich_text"])
        if is_completion_prompt(text): render_text_or_input(text, block["id"])
        else: st.markdown(f"* {text}")
        render_inline_buttons(internal_links, block["id"])
        if block.get("has_children"): render_children(block["id"])
    elif b_type == "numbered_list_item":
        text = rich_text_to_markdown(block["numbered_list_item"]["rich_text"])
        if is_completion_prompt(text): render_text_or_input(text, block["id"])
        else: st.markdown(f"1. {text}")
        render_inline_buttons(internal_links, block["id"])
        if block.get("has_children"): render_children(block["id"])
    elif b_type == "callout":
        text = rich_text_to_markdown(block["callout"]["rich_text"])
        icon = get_callout_icon(block)
        if is_completion_prompt(text):
            label_text = text.replace("**", "").replace("*", "").strip()
            with st.container(border=True):
                st.info(f"{icon} {label_text}")
                st.text_area("Vaše odpověď:", label_visibility="collapsed", placeholder="Zde se rozepište...", key=f"callout_input_{block['id']}", height=100)
        else: st.info(text, icon=icon)
        render_inline_buttons(internal_links, block["id"])
        if block.get("has_children"): render_children(block["id"])
    elif b_type == "toggle":
        title = rich_text_to_markdown(block["toggle"]["rich_text"])
        with st.expander(title or "Zobrazit detail"):
            render_children(block["id"])
    elif b_type == "to_do":
        checked = block["to_do"].get("checked", False)
        text = rich_text_to_markdown(block["to_do"]["rich_text"])
        st.checkbox(text, value=checked, key=f"todo_{block['id']}")
    elif b_type == "image":
        img_data = block["image"]
        img_url = img_data.get("file", {}).get("url") or img_data.get("external", {}).get("url")
        if img_url: st.image(img_url)
    elif b_type == "divider":
        st.divider()

    # --- PODPORA TABULEK ---
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

    # --- LAYOUT A ZANOŘENÍ ---
    elif b_type == "column_list":
        cols_blocks = fetch_notion_blocks(block["id"])
        if cols_blocks:
            cols = st.columns(len(cols_blocks))
            for idx, col_block in enumerate(cols_blocks):
                with cols[idx]: render_children(col_block["id"])
    elif b_type == "child_page":
        title = block["child_page"]["title"]
        if "řídící centrum" not in title.lower():
            if st.button(f"📖 Otevřít: {title}", key=f"page_{block['id']}", use_container_width=True):
                st.session_state["current_page_id"] = block["id"]
                st.rerun()
    elif b_type == "link_to_page":
        page_id = block.get("link_to_page", {}).get("page_id")
        if page_id:
            if st.button("🔗 Přejít na kapitolu", key=f"link_{block['id']}", use_container_width=True):
                st.session_state["current_page_id"] = page_id
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
