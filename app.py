import streamlit as st
import requests

# 1. Konfigurace stránky
st.set_page_config(
    page_title="Ekonomika - Učebnice",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Vlastní CSS design (čistý a moderní)
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
    .stAlert {
        border-radius: 10px;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# Načtení klíčů z trezoru
NOTION_TOKEN = st.secrets["NOTION_TOKEN"]
PAGE_ID = st.secrets["PAGE_ID"]

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28"
}

# Načtení dat z Notionu
url = f"https://api.notion.com/v1/blocks/{PAGE_ID}/children"
response = requests.get(url, headers=headers)

blocks = []
chapters = []

if response.status_code == 200:
    data = response.json()
    all_results = data.get("results", [])
    
    # Rozdělíme obsah: co je běžný text a co jsou podstránky (kapitoly)
    for b in all_results:
        if b.get("type") == "child_page":
            chapters.append(b)
        else:
            blocks.append(b)

# --- BOČNÍ PANEL (ČISTÝ) ---
with st.sidebar:
    st.title("📚 Ekonomika")
    st.caption("Digitální učebnice")
    st.divider()
    
    st.subheader("Kapitoly v učebnici")
    if chapters:
        for ch in chapters:
            title = ch["child_page"]["title"]
            st.button(f"📖 {title}", key=ch["id"], use_container_width=True)
    else:
        st.write("Úvodní stránka")

# --- HLAVNÍ OBSAH ---
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

    if response.status_code == 200:
        with st.container(border=True):
            for block in blocks:
                render_block(block)
    else:
        st.error(f"Nepodařilo se načíst obsah. Kód chyby: {response.status_code}")
