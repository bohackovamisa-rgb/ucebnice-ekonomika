import streamlit as st
import requests

# Nastavení vzhledu stránky
st.set_page_config(page_title="Ekonomika - Učebnice", page_icon="📚", layout="centered")

# Načtení klíčů z trezoru
NOTION_TOKEN = st.secrets["NOTION_TOKEN"]
PAGE_ID = st.secrets["PAGE_ID"]

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28"
}

# Funkce, která převádí kódové kostky z Notionu na hezký text
def render_block(block):
    b_type = block.get("type")
    
    # Pomocná funkce pro získání čistého textu
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
        st.info(get_text(block["callout"]["rich_text"]))
    elif b_type == "quote":
        st.warning(get_text(block["quote"]["rich_text"]))

# Načtení dat z Notionu
url = f"https://api.notion.com/v1/blocks/{PAGE_ID}/children"
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    blocks = data.get("results", [])
    
    # Vykreslení jednotlivých bloků na stránku
    for block in blocks:
        render_block(block)
else:
    st.error(f"Nepodařilo se načíst obsah. Kód chyby: {response.status_code}")
