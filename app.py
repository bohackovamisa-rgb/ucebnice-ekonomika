import streamlit as st
import requests

# 1. Konfigurace stránky
st.set_page_config(
    page_title="Ekonomika - Učebnice",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Vlastní CSS design
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    h1 {
        color: #1e3a8a;
        font-weight: 700;
    }
    h2 {
        color: #2563eb;
        border-bottom: 2px solid #e5e7eb;
        padding-bottom: 0.3rem;
        margin-top: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Načtení klíčů z trezoru
NOTION_TOKEN = st.secrets["NOTION_TOKEN"]
MAIN_PAGE_ID = st.secrets["PAGE_ID"]

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28"
}

if "current_page_id" not in st.session_state:
    st.session_state["current_page_id"] = MAIN_PAGE_ID

# --- FUNKCE PRO NAČÍTÁNÍ S PODPOROU STRÁNKOVÁNÍ ---
def fetch_notion_blocks(block_id):
    """Načte VŠECHNY bloky dané stránky nebo kontejneru (řeší i stránkování)."""
    all_blocks = []
    url = f"https://api.notion.com/v1/blocks/{block_id}/children?page_size=100"
    has_more = True
    start_cursor = None
    
    while has_more:
        params_url = url
        if start_cursor:
            params_url += f"&start_cursor={start_cursor}"
        res = requests.get(params_url, headers=headers)
        if res.status_code == 200:
            data = res.json()
            all_blocks.extend(data.get("results", []))
            has_more = data.get("has_more", False)
            start_cursor = data.get("next_cursor")
        else:
            break
    return all_blocks

# Pomocná funkce pro vyhledání kapitol (prohledá i sloupce)
def find_all_chapters(blocks):
    chapters = []
    for b in blocks:
        b_type = b.get("type")
        if b_type == "child_page":
            # Vynecháme řídící centrum, chceme jen učební kapitoly
            title = b["child_page"]["title"]
            if "řídící centrum" not in title.lower() and "dashboard" not in title.lower():
                chapters.append({"id": b["id"], "title": title})
        elif b_type == "column_list":
            col_blocks = fetch_notion_blocks(b["id"])
            for col in col_blocks:
                child_in_col = fetch_notion_blocks(col["id"])
                chapters.extend(find_all_chapters(child_in_col))
    return chapters

# Načtení hlavních bloků z úvodní stránky
main_blocks = fetch_notion_blocks(MAIN_PAGE_ID)
chapters = find_all_chapters(main_blocks)

# --- BOČNÍ PANEL (NAVIGACE) ---
with st.sidebar:
    st.title("📚 Ekonomika")
    st.caption("Digitální učebnice")
    st.divider()
    
    if st.button("🏠 Úvodní stránka", use_container_width=True):
        st.session_state["current_page_id"] = MAIN_PAGE_ID
        st.rerun()
        
    st.divider()
    st.subheader("Kapitoly")
    
    if chapters:
        for ch in chapters:
            if st.button(f"📖 {ch['title']}", key=ch["id"], use_container_width=True):
                st.session_state["current_page_id"] = ch["id"]
                st.rerun()
    else:
        st.caption("Žádné kapitoly nenalezeny.")

# --- VYKERESLOVÁNÍ OBSAHU ---
def render_block(block):
    b_type = block.get("type")
    
    def get_text(rich_text_list):
        if not rich_text_list:
            return ""
        return "".join([t.get("plain_text", "") for t in rich_text_list])

    # Textové prvky
    if b_type == "heading_1":
        st.title(get_text(block["heading_1"]["rich_text"]))
    elif b_type == "heading_2":
        st.header(get_text(block["heading_2"]["rich_text"]))
    elif b_type == "heading_3":
        st.subheader(get_text(block["heading_3"]["rich_text"]))
    elif b_type == "paragraph":
        text = get_text(block["paragraph"]["rich_text"])
        if text:
            st.write(text)
    elif b_type == "bulleted_list_item":
        st.markdown(f"* {get_text(block['bulleted_list_item']['rich_text'])}")
    elif b_type == "numbered_list_item":
        st.markdown(f"1. {get_text(block['numbered_list_item']['rich_text'])}")
    elif b_type == "callout":
        text = get_text(block["callout"]["rich_text"])
        st.info(text, icon="💡")
        if block.get("has_children"):
            render_children(block["id"])
    elif b_type == "quote":
        st.warning(get_text(block["quote"]["rich_text"]), icon="💬")
    elif b_type == "divider":
        st.divider()
    elif b_type == "to_do":
        checked = block["to_do"].get("checked", False)
        text = get_text(block["to_do"]["rich_text"])
        st.checkbox(text, value=checked, key=block["id"])
    elif b_type == "image":
        img_data = block["image"]
        img_url = img_data.get("file", {}).get("url") or img_data.get("external", {}).get("url")
        if img_url:
            st.image(img_url)
    # SLOUPCE (Column List)
    elif b_type == "column_list":
        cols_blocks = fetch_notion_blocks(block["id"])
        if cols_blocks:
            cols = st.columns(len(cols_blocks))
            for idx, col_block in enumerate(cols_blocks):
                with cols[idx]:
                    render_children(col_block["id"])
    # ROZBALOVACÍ SEZNAM (Toggle)
    elif b_type == "toggle":
        title = get_text(block["toggle"]["rich_text"])
        with st.expander(title or "Zobrazit detail"):
            render_children(block["id"])
    elif b_type == "child_page":
        title = block["child_page"]["title"]
        if "řídící centrum" not in title.lower() and "dashboard" not in title.lower():
            if st.button(f"📖 Otevřít kapitolu: {title}", key=f"main_{block['id']}", use_container_width=True):
                st.session_state["current_page_id"] = block["id"]
                st.rerun()

def render_children(block_id):
    """Načte a vykreslí zanořený obsah uvnitř sloupců/boxů."""
    children = fetch_notion_blocks(block_id)
    for child in children:
        render_block(child)

# --- ZOBRAZENÍ HLAVNÍ STRÁNKY ---
active_blocks = fetch_notion_blocks(st.session_state["current_page_id"])

col1, main_col, col2 = st.columns([1, 4, 1])

with main_col:
    with st.container(border=True):
        if active_blocks:
            for block in active_blocks:
                render_block(block)
        else:
            st.info("Tato část neobsahuje žádný text.")
