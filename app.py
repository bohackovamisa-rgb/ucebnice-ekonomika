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

# --- PAMĚŤ APLIKACE ---
# Uložíme si, která stránka je právě otevřená (na začátku je to Úvodní stránka)
if "current_page_id" not in st.session_state:
    st.session_state["current_page_id"] = MAIN_PAGE_ID

# Funkce pro načtení bloků z Notionu pro jakékoliv ID stránky
def fetch_notion_blocks(page_id):
    url = f"https://api.notion.com/v1/blocks/{page_id}/children"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("results", [])
    return []

# Načteme si hlavní stránku pro sestavení menu v bočním panelu
main_blocks = fetch_notion_blocks(MAIN_PAGE_ID)

# Najdeme všechny podstránky (kapitoly)
chapters = []
for b in main_blocks:
    if b.get("type") == "child_page":
        chapters.append({
            "id": b["id"],
            "title": b["child_page"]["title"]
        })

# --- BOČNÍ PANEL (NAVIGACE) ---
with st.sidebar:
    st.title("📚 Ekonomika")
    st.caption("Digitální učebnice")
    st.divider()
    
    # Tlačítko pro návrat na úvod
    if st.button("🏠 Úvodní stránka", use_container_width=True):
        st.session_state["current_page_id"] = MAIN_PAGE_ID
        st.rerun()
        
    st.divider()
    st.subheader("Kapitoly")
    
    # Dynamická tlačítka pro jednotlivé kapitoly
    for ch in chapters:
        if st.button(f"📖 {ch['title']}", key=ch["id"], use_container_width=True):
            st.session_state["current_page_id"] = ch["id"]
            st.rerun()

# --- HLAVNÍ OBSAH (Zobrazuje právě vybranou stránku) ---
active_blocks = fetch_notion_blocks(st.session_state["current_page_id"])

col1, main_col, col2 = st.columns([1, 4, 1])

with main_col:
    def render_block(block):
        b_type = block.get("type")
        
        def get_text(rich_text_list):
            return "".join([t.get("plain_text", "") for t in rich_text_list])

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
            st.info(get_text(block["callout"]["rich_text"]), icon="💡")
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
        elif b_type == "child_page":
            # Pokud se podstránka objeví přímo v textu, vykreslíme ji jako velkou proklikávací kartu
            title = block["child_page"]["title"]
            if st.button(f"📖 Otevřít kapitolu: {title}", key=f"main_{block['id']}", use_container_width=True):
                st.session_state["current_page_id"] = block["id"]
                st.rerun()

    with st.container(border=True):
        if active_blocks:
            for block in active_blocks:
                render_block(block)
        else:
            st.info("Tato kapitola zatím neobsahuje žádný text nebo se načítá...")
