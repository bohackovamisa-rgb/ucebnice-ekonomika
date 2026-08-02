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

# Načtení klíčů z Secrets
NOTION_TOKEN = st.secrets["NOTION_TOKEN"]
MAIN_PAGE_ID = st.secrets["PAGE_ID"]

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28"
}

if "current_page_id" not in st.session_state:
    st.session_state["current_page_id"] = MAIN_PAGE_ID

# --- 1. PŘEKLADAČ FORMÁTOVÁNÍ ---
def rich_text_to_markdown(rich_text_list):
    """Převede Notion rich_text na formátovaný Markdown včetně odkazů."""
    if not rich_text_list:
        return ""
    
    md_text = ""
    for t in rich_text_list:
        text = t.get("plain_text", "")
        annotations = t.get("annotations", {})
        href = t.get("href")

        if annotations.get("bold"):
            text = f"**{text}**"
        if annotations.get("italic"):
            text = f"*{text}*"
        if annotations.get("strikethrough"):
            text = f"~~{text}~~"
        if annotations.get("code"):
            text = f"`{text}`"
        
        if href:
            text = f"[{text}]({href})"
            
        md_text += text
    return md_text

# --- 2. NAČÍTÁNÍ BLOKŮ Z NOTIONU ---
def fetch_notion_blocks(block_id):
    """Načte všechny bloky ze zadaného ID (řeší stránkování)."""
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
            else:
                break
        except Exception:
            break
    return all_blocks

def fetch_database_pages(db_id):
    """Načte stránky z databáze."""
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
    except Exception:
        pass
    return pages

# --- 3. DEDUPLIKACE A SEŘAZENÍ KAPITOL ---
def extract_chapter_number(title):
    match = re.search(r'(?:kapitola\s*|0)?(\d+)', title.lower())
    if match:
        return int(match.group(1))
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

# --- 5. CHYTRÉ VYKRESLOVÁNÍ TEXTU A INTERAKTIVNÍCH PRVKŮ ---
def render_text_or_input(text, block_id):
    """Rozpozná úkoly k doplňování a vytvoří pro ně interaktivní vstupní pole."""
    clean_text = text.strip()
    lower_text = clean_text.lower()
    
    # Detekce klíčových slov pro doplňování
    if lower_text.startswith(("doplň:", "doplňte:", "doplň ", "doplňte ", "úkol:", "otázka:")):
        st.text_input(
            label=clean_text,
            placeholder="Sem napište svou odpověď...",
            key=f"input_{block_id}"
        )
    else:
        st.markdown(text)

def render_block(block):
    b_type = block.get("type")

    # Textové prvky
    if b_type == "heading_1":
        st.title(rich_text_to_markdown(block["heading_1"]["rich_text"]))
    elif b_type == "heading_2":
        st.header(rich_text_to_markdown(block["heading_2"]["rich_text"]))
    elif b_type == "heading_3":
        st.subheader(rich_text_to_markdown(block["heading_3"]["rich_text"]))
    elif b_type == "paragraph":
        text = rich_text_to_markdown(block["paragraph"]["rich_text"])
        if text:
            render_text_or_input(text, block["id"])
    elif b_type == "bulleted_list_item":
        st.markdown(f"* {rich_text_to_markdown(block['bulleted_list_item']['rich_text'])}")
        if block.get("has_children"):
            render_children(block["id"])
    elif b_type == "numbered_list_item":
        st.markdown(f"1. {rich_text_to_markdown(block['numbered_list_item']['rich_text'])}")
        if block.get("has_children"):
            render_children(block["id"])
    elif b_type == "callout":
        text = rich_text_to_markdown(block["callout"]["rich_text"])
        
        # Pokud je v Calloutu úkol k doplňování
        if text.strip().lower().startswith(("doplň:", "doplňte:", "úkol:", "otázka:")):
            st.info("💡 " + text)
            st.text_input("Vaše odpověď:", placeholder="Napište odpověď...", key=f"callout_input_{block['id']}")
        else:
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
        st.checkbox(text, value=checked, key=f"todo_{block['id']}")
    elif b_type == "image":
        img_data = block["image"]
        img_url = img_data.get("file", {}).get("url") or img_data.get("external", {}).get("url")
        if img_url:
            st.image(img_url)
    elif b_type == "divider":
        st.divider()

    # --- LAYOUT A ZANOŘENÍ ---
    elif b_type == "column_list":
        cols_blocks = fetch_notion_blocks(block["id"])
        if cols_blocks:
            cols = st.columns(len(cols_blocks))
            for idx, col_block in enumerate(cols_blocks):
                with cols[idx]:
                    render_children(col_block["id"])

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
        # Prevence zpožděného nebo dvojitého vykreslení u zrcadlených bloků
        synced_from = block.get("synced_block", {}).get("synced_from")
        target_id = synced_from.get("block_id") if synced_from else block["id"]
        render_children(target_id)

def render_children(block_id):
    children = fetch_notion_blocks(block_id)
    for child in children:
        render_block(child)

# --- VYSVÍCENÍ OBSAHU ---
active_blocks = fetch_notion_blocks(st.session_state["current_page_id"])

col1, main_col, col2 = st.columns([1, 4, 1])

with main_col:
    with st.container(border=True):
        if active_blocks:
            for block in active_blocks:
                render_block(block)
        else:
            st.info("Obsah se načítá nebo je tato stránka prázdná...")
