import streamlit as st
import requests

st.title("Moje digitální učebnice ekonomiky")

# Načtení tajných dat z bezpečného trezoru Streamlitu
NOTION_TOKEN = st.secrets["NOTION_TOKEN"]
PAGE_ID = st.secrets["PAGE_ID"]

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28"
}

st.write("Zkouším se připojit k Notionu...")

url = f"https://api.notion.com/v1/blocks/{PAGE_ID}/children"
response = requests.get(url, headers=headers)

if response.status_code == 200:
    st.success("Spojení s Notionem funguje! 🎉")
    st.write("Tady jsou surová data (kostky), které nám Notion poslal:")
    st.json(response.json())
else:
    st.error(f"Něco se pokazilo. Kód chyby: {response.status_code}")
    st.write(response.text)
