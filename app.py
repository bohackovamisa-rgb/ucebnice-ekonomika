import streamlit as st
import requests

# 1. Konfigurace stránky
st.set_page_config(
    page_title="Ekonomika - Učebnice",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Načtení klíčů
NOTION_TOKEN = st.secrets["NOTION_TOKEN"]
MAIN_PAGE_ID = st.secrets["PAGE_ID"]

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28"
}

if "current_page_id" not in st.session_state:
    st.session_state["current_page_id"] = MAIN_PAGE_ID

# --- 1. PŘEKLADAČ FORMÁTOVÁNÍ (Zachová odkazy, bold, kurzívu) ---
def rich_text_to_markdown(rich_text_list):
    """Převede Notion rich_text na formátovaný Markdown včetně odkazů."""
    if not rich_text_list:
        return ""
    
    md_text = ""
    for t in rich_text_list:
        text = t.get("plain_text", "")
        annotations = t.get("annotations", {})
        href = t.get("href")

        # Aplikace stylů
        if annotations.get("bold"):
            text = f"**{text}**"
        if annotations.get("italic"):
            text = f"*{text}*"
        if annotations.get("strikethrough"):
            text = f"~~{text}~~"
        if annotations.get("code"):
            text = f"`{text}`"
        
        # Aplikace odkazu
        if href:
            text = f"[{text}]({href})"
            
        md_text += text
    return md_text

# --- 2. NAČÍTÁNÍ BLOKŮ A DATABÁZÍ ---
def fetch_notion_blocks(block_id):
    """Načte všechny bloky ze zadaného ID."""
    all_blocks = []
    url = f"https://api.notion.com/v1/blocks/{block_id}/children?page_size=100"
    has_more = True
    start_cursor = None
    
    while has_more:
        params_url = url + (f"&start_cursor={start_cursor}" if start_cursor else "")
        res = requests.get(params_url, headers=headers)
        if res.status_code == 200:
            data = res.json()
            all_blocks.extend(data.get("results", []))
            has_more = data.get("has_more", False)
            start_cursor = data.get("next_cursor")
        else:
            break
    return all_blocks

def fetch_database_pages(db_id):
    """Načte kapitoly, pokud jsou vložené v Notionu jako databáze/tabulka."""
    url = f"https://api.notion.com/v1/databases/{db_id}/query"
    res = requests.post(url, headers=headers)
    pages = []
    if res.status_code == 200:
        for p in res.json().get("results", []):
            title = "Bez názvu"
            props = p.get("properties", {})
            for key, val in props.items():
                if val.get("type") == "title" and val.get("title"):
                    title = rich_text_to_markdown(val["title"])
            pages.append({"id": p["id"], "title": title})
    return pages

# Vyhledání kapitol na hlavní stránce
def discover_chapters(blocks):
    chapters = []
    for b in blocks:
        b_type = b.get("type")
        if b_type == "child_page":
            title = b["child_page"]["title"]
            if "řídící centrum" not in title.lower():
                chapters.append({"id": b["id"], "title": title})
        elif b_type == "child_database":
            # Pokud máte kapitoly v tabulce/databázi
            db_pages = fetch_database_pages(b["id"])
            chapters.extend(db_pages)
    return chapters

main_blocks = fetch_notion_blocks(MAIN_PAGE_ID)
chapters = discover_chapters(main_blocks)

# --- 3. BOČNÍ PANEL ---
with st.sidebar:
    st.title("📚 Učebnice Ekonomiky")
    st.divider()
    
    if st.button("🏠 Úvodní stránka", use_container_width=True):
        st.session_state["current_page_id"] = MAIN_PAGE_ID
        st.rerun()
        
    st.divider()
    st.subheader("Kapitoly")
    for ch in chapters:
        if st.button(f"📖 {ch['title']}", key=ch["id"], use_container_width=True):
            st.session_state["current_page_id"] = ch["id"]
            st.rerun()

# --- 4. VYKRESLOVÁNÍ OBSAHU ---
def render_block(block):
    b_type = block.get("type")

    if b_type == "heading_1":
        st.title(rich_text_to_markdown(block["heading_1"]["rich_text"]))
    elif b_type == "heading_2":
        st.header(rich_text_to_markdown(block["heading_2"]["rich_text"]))
    elif b_type == "heading_3":
        st.subheader(rich_text_to_markdown(block["heading_3"]["rich_text"]))
    elif b_type == "paragraph":
        text = rich_text_to_markdown(block["paragraph"]["rich_text"])
        if text:
            st.markdown(text)
    elif b_type == "bulleted_list_item":
        st.markdown(f"* {rich_text_to_markdown(block['bulleted_list_item']['rich_text'])}")
    elif b_type == "numbered_list_item":
        st.markdown(f"1. {rich_text_to_markdown(block['numbered_list_item']['rich_text'])}")
    elif b_type == "callout":
        text = rich_text_to_markdown(block["callout"]["rich_text"])
        st.info(text, icon="💡")
        if block.get("has_children"):
            render_children(block["id"])
    elif b_type == "toggle":
        title = rich_text_to_markdown(block["toggle"]["rich_text"])
        with st.expander(title or "Zobrazit detail"):
            render_children(block["id"])
    elif b_type == "to_do":
        checked = block["to_do"].get("checked", False)
        text = rich_text_to_markdown(block["to_do"]["rich_text"])
        st.checkbox(text, value=checked, key=block["id"])
    elif b_type == "image":
        img_data = block["image"]
        img_url = img_data.get("file", {}).get("url") or img_data.get("external", {}).get("url")
        if img_url:
            st.image(img_url)
    elif b_type == "divider":
        st.divider()

def render_children(block_id):
    children = fetch_notion_blocks(block_id)
    for child in children:
        render_block(child)

# --- HLAVNÍ STRÁNKA ---
active_blocks = fetch_notion_blocks(st.session_state["current_page_id"])

col1, main_col, col2 = st.columns([1, 4, 1])

with main_col:
    with st.container(border=True):
        if active_blocks:
            for block in active_blocks:
                render_block(block)
        else:
            st.info("Obsah se načítá nebo je tato stránka prázdná...")
