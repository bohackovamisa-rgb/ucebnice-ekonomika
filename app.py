import streamlit as st
import requests

# 1. Konfigurace stránky
st.set_page_config(
    page_title="Ekonomika - Digitální učebnice",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Vlastní CSS design pro moderní vzhled
st.markdown("""
    <style>
    /* Hlavní pozadí a písmo */
    .main {
        background-color: #f8f9fa;
    }
    /* Styl pro hlavní karty s obsahem */
    div[data-testid="stVerticalBlock"] > div[style*="flex-direction: column;"] > div {
        background-color: white;
        border-radius: 12px;
        padding: 10px;
    }
    /* Úprava nadpisů */
    h1 {
        color: #1e3a8a;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    h2 {
        color: #2563eb;
        border-bottom: 2px solid #e5e7eb;
        padding-bottom: 0.3rem;
        margin-top: 1.5rem;
    }
    /* Stylování Callout boxů z Notionu */
    .stAlert {
        border-radius: 10px;
        border: none;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
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

# --- BOČNÍ PANEL (SIDEBAR) ---
with st.sidebar:
    st.image("https://img.icons8.com/illustrations/m_1.5x/education.png", width=150)
    st.title("📚 Ekonomika")
    st.caption("Interaktivní učebnice pro studenty")
    st.divider()
    
    st.subheader("Kapitoly")
    # Tady v budoucnu napojíme seznam všech kapitol
    st.radio("Vyberte téma:", ["Úvod do ekonomiky", "1. Trh a jeho mechamismy", "2. Ponuka a poptávka"], index=0)
    
    st.divider()
    st.progress(25, text="Celkový pokrok v předmětu: 25 %")

# --- HLAVNÍ OBSAH ---
# Zabalíme obsah do hezkého středového kontejneru
col1, main_col, col2 = st.columns([1, 4, 1])

with main_col:
    # Funkce pro převod bloků z Notionu
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

    # Načtení dat z Notionu
    url = f"https://api.notion.com/v1/blocks/{PAGE_ID}/children"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        blocks = data.get("results", [])
        
        # Vykreslení obsahu uvnitř bílé karty
        with st.container(border=True):
            for block in blocks:
                render_block(block)
                
            st.divider()
            
            # Tlačítko pro studenta na konci kapitoly
            if st.button("✅ Označit tuto kapitolu za dokončenou", type="primary", use_container_width=True):
                st.balloons()
                st.success("Skvělá práce! Kapitola byla označena jako splněná.")
    else:
        st.error(f"Nepodařilo se načíst obsah. Kód chyby: {response.status_code}")
