import streamlit as st
import requests
import re

# 1. Konfigurace stránky
st.set_page_config(
    page_title="Ekonomika - Digitální Učebnice",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- PŘIHLAŠOVACÍ BRÁNA ---
def check_password():
    app_pwd = st.secrets.get("APP_PASSWORD")
    if not app_pwd:
        st.error("⚠️ V nastavení Streamlit Secrets chybí proměnná APP_PASSWORD!")
        return False
        
    if st.session_state.get("password_correct", False):
        return True

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("<h2 style='text-align: center; border: none;'>🔒 Soukromá učebnice</h2>", unsafe_allow_html=True)
            st.info("Tato aplikace je uzamčena. Zadejte přístupové heslo.")
            password = st.text_input("Heslo:", type="password")
            if st.button("Vstoupit do učebnice", use_container_width=True):
                if password == app_pwd:
                    st.session_state["password_correct"] = True
                    st.rerun()
                else:
                    st.error("❌ Nesprávné heslo!")
    return False

if not check_password():
    st.stop()

# --- ČISTÝ MODERNÍ DESIGN (CUSTOM CSS) ---
st.markdown("""
    <style>
    .stApp { background-color: #f8fafc; font-family: 'Inter', system-ui, -apple-system, sans-serif; }
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #ffffff !important; border-radius: 12px !important; border: 1px solid #e2e8f0 !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05) !important; padding: 1.25rem !important;
    }
    
    /* Elegantní odsazení kotvy od shora, aby nadpis nebyl nalepený pod lištou! */
    h1, h2, h3 { 
        scroll-margin-top: 80px; 
    }
    
    h1 { color: #0f172a !important; font-weight: 800 !important; font-size: 2.1rem !important; margin-top: 1rem; }
    h2 { color: #1e293b !important; font-weight: 700 !important; font-size: 1.5rem !important; border-bottom: 2px solid #f1f5f9; padding-bottom: 0.4rem; margin-top: 1.5rem; }
    h3 { color: #334155 !important; font-weight: 600 !important; font-size: 1.2rem !important; margin-top: 1rem; }
    
    .stTextInput input, .stTextArea textarea { border-radius: 10px !important; border: 1px solid #cbd5e1 !important; background-color: #f8fafc !important; color: #0f172a !important; }
    .stTextInput input:focus, .stTextArea textarea:focus { border-color: #3b82f6 !important; background-color: #ffffff !important; box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.15) !important; }
    .stButton > button { border-radius: 10px !important; border: 1px solid #e2e8f0 !important; background-color: #ffffff !important; color: #1e293b !important; font-weight: 600 !important; transition: all 0.2s ease-in-out !important; }
    .stButton > button:hover { border-color: #3b82f6 !important; color: #2563eb !important; background-color: #eff6ff !important; }
    
    /* Styly pro automatickou navigaci */
    .nav-link-box {
        display: block; padding: 0.75rem 1rem; background-color: #f1f5f9; 
        border-radius: 8px; text-align: center; text-decoration: none !important;
        color: #2563eb !important; font-weight: 600; margin-bottom: 0.5rem;
        transition: all 0.2s;
    }
    .nav-link-box:hover { background-color: #e2e8f0; transform: translateY(-2px); }
    p a, li a { color: #2563eb !important; text-decoration: none !important; font-weight: 600 !important; }
    p a:hover, li a:hover { text-decoration: underline !important; }
    </style>
""", unsafe_allow_html=True)

NOTION_TOKEN = st.secrets["NOTION_TOKEN"]
MAIN_PAGE_ID = st.secrets["PAGE_ID"]
headers = { "Authorization": f"Bearer {NOTION_TOKEN}", "Notion-Version": "2022-06-28" }

# --- POMOCNÉ FUNKCE ---
def format_uuid(id_str):
    clean = id_str.replace("-", "")
    if len(clean) == 32: return f"{clean[:8]}-{clean[8:12]}-{clean[12:16]}-{clean[16:20]}-{clean[20:]}"
    return id_str

if "page" in st.query_params:
    target_page = format_uuid(st.query_params["page"])
    if st.session_state.get("current_page_id") != target_page:
        st.session_state["current_page_id"] = target_page
elif "current_page_id" not in st.session_state:
    st.session_state["current_page_id"] = format_uuid(MAIN_PAGE_ID)

# --- PŘEKLADAČ TEXTU S NATIVNÍMI KOTVAMI ---
def rich_text_to_markdown(rich_text_list):
    if not rich_text_list: return ""
    md_text = ""
    for t in rich_text_list:
        text = t.get("plain_text", "").strip()
        annotations = t.get("annotations", {})
        href = t.get("href")
        
        is_internal = False
        target_id = None
        
        # Záchyt odkazů z Notionu a jejich přepsání na čisté lokální kotvy
        if href and ("notion.so" in href or "notion.site" in href):
            is_internal = True
            if "#" in href:
                # Odkaz na blok (vnitřní sekce)
                matched = re.search(r'([a-fA-F0-9]{32})', href.split("#")[1].replace("-", ""))
                if matched: target_id = format_uuid(matched.group(1))
            else:
                # Odkaz na stránku
                matched = re.search(r'([a-fA-F0-9]{32})', href.replace("-", ""))
                if matched: target_id = format_uuid(matched.group(1))
                
        elif t.get("type") == "mention":
            m_type = t.get("mention", {}).get("type")
            if m_type in ["page", "database"]:
                is_internal = True
                target_id = format_uuid(t["mention"][m_type]["id"])
                
        if is_internal and not text: text = "Odkaz"

        if text:
            # Aplikace standardního Markdownu
            if annotations.get("bold"): text = f"**{text}**"
            if annotations.get("italic"): text = f"*{text}*"
            if annotations.get("strikethrough"): text = f"~~{text}~~"
            if annotations.get("code"): text = f"`{text}`"
            
            # Tvorba lokálních odkazů (využívají čistý Markdown formát)
            if is_internal and target_id:
                text = f"[{text}](#{target_id})"
            elif href and not is_internal:
                text = f"[{text}]({href})"
                
            md_text += text + " "
    return md_text.strip()

# --- NAČÍTÁNÍ Z NOTIONU ---
def fetch_notion_blocks(block_id):
    all_blocks, has_more, start_cursor = [], True, None
    url = f"https://api.notion.com/v1/blocks/{format_uuid(block_id)}/children?page_size=100"
    while has_more:
        try:
            res = requests.get(url + (f"&start_cursor={start_cursor}" if start_cursor else ""), headers=headers)
            if res.status_code == 200:
                data = res.json()
                all_blocks.extend(data.get("results", []))
                has_more, start_cursor = data.get("has_more", False), data.get("next_cursor")
            else: break
        except Exception: break
    return all_blocks

def fetch_database_pages(db_id):
    pages = []
    try:
        res = requests.post(f"https://api.notion.com/v1/databases/{format_uuid(db_id)}/query", headers=headers)
        if res.status_code == 200:
            for p in res.json().get("results", []):
                title = "Bez názvu"
                for _, val in p.get("properties", {}).items():
                    if val.get("type") == "title" and val.get("title"): title = rich_text_to_markdown(val["title"])
                pages.append({"id": format_uuid(p["id"]), "title": title})
    except Exception: pass
    return pages

def discover_chapters(blocks):
    raw_chapters = []
    def scan_blocks(block_list):
        for b in block_list:
            if b.get("type") == "child_page":
                title = b["child_page"]["title"].strip()
                if title and "řídící centrum" not in title.lower(): raw_chapters.append({"id": format_uuid(b["id"]), "title": title})
            elif b.get("type") == "child_database": raw_chapters.extend(fetch_database_pages(b["id"]))
            elif b.get("type") == "column_list":
                for col in fetch_notion_blocks(b["id"]): scan_blocks(fetch_notion_blocks(col["id"]))
    scan_blocks(blocks)
    chapters_by_num, other_chapters = {}, []
    for ch in raw_chapters:
        match = re.search(r'(?:kapitola\s*|0)?(\d+)', ch["title"].lower())
        num = int(match.group(1)) if match else 999
        if num != 999: chapters_by_num[num] = ch
        elif not any(o["title"] == ch["title"] for o in other_chapters): other_chapters.append(ch)
    return [chapters_by_num[k] for k in sorted(chapters_by_num.keys())] + other_chapters

chapters = discover_chapters(fetch_notion_blocks(MAIN_PAGE_ID))

# --- BOČNÍ PANEL ---
with st.sidebar:
    st.markdown("<h2 style='margin-top:0;'>📚 Učebnice Ekonomiky</h2>", unsafe_allow_html=True)
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
    if st.button("🔒 Odhlásit se", use_container_width=True):
        st.session_state["password_correct"] = False
        st.rerun()

# --- DETEKTOR UŽIVATELSKÝCH VSTUPŮ ---
def is_completion_prompt(text):
    clean = re.sub(r"^[\*\_\#\d\.\s\[\]\(\)\?]+", "", text.strip()).lower()
    explicit_prefixes = (
        "doplň:", "doplňte:", "úkol:", "otázka:", "odpověď:", "název projektu:", 
        "jedna věta projektu:", "zákazník:", "problém:", "hodnota pro zákazníka:", 
        "řešení:", "konkurence:", "cena:", "jednorázové náklady:", "fixní náklady:", 
        "variabilní náklady:", "první test:", "metrika úspěchu:", "rizika:", 
        "právní forma:", "etické pravidlo:", "rozhodnutí:"
    )
    if clean.startswith(explicit_prefixes): return True
    if any(clean.startswith(p) for p in ("předpokládali jsme", "ověřili jsme", "naměřili jsme", "zjistili jsme", "proto teď rozhodujeme")): return True
    if (clean.endswith(("…", "...", "___")) or "…" in clean or "..." in clean) and len(clean) < 200: return True
    return False

def render_text_or_input(text, block_id):
    clean_lower = re.sub(r"^[\*\_\#\s]+", "", text.strip()).lower()
    label_text = text.replace("**", "").replace("*", "").strip()
    label_text = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", label_text)
    icon = "✏️"
    if "projekt" in clean_lower: icon = "🚀"
    elif "zákazník" in clean_lower: icon = "👥"
    elif "problém" in clean_lower: icon = "🚨"
    elif "řešení" in clean_lower or "hodnot" in clean_lower: icon = "💡"
    elif "cen" in clean_lower or "náklad" in clean_lower: icon = "💰"
    is_long = any(p in clean_lower for p in ("problém", "hodnota", "řešení", "konkurence", "rizika", "pravidlo", "věta", "předpokládali", "ověřili", "naměřili", "zjistili"))
    
    with st.container(border=True):
        st.markdown(f"**{icon} {label_text}**")
        if is_long: st.text_area("Odpo", label_visibility="collapsed", placeholder="Zde se rozepište...", key=f"input_{block_id}", height=100)
        else: st.text_input("Odpo", label_visibility="collapsed", placeholder="Stručná odpověď...", key=f"input_{block_id}")

# --- BEZPEČNÉ VYKRESLENÍ BLOKŮ S NATIVNÍMI KOTVAMI ---
def render_block(block):
    b_type = block.get("type")
    block_id = format_uuid(block["id"])
    
    rich_text_data = block.get(b_type, {}).get("rich_text", []) if b_type in block else []
    text = rich_text_to_markdown(rich_text_data)

    # Nyní používáme bezpečné nativní funkce st.title / st.header / st.subheader s parametrem anchor!
    if b_type == "heading_1":
        if is_completion_prompt(text): render_text_or_input(text, block_id)
        else: st.title(text, anchor=block_id)
    elif b_type == "heading_2":
        if is_completion_prompt(text): render_text_or_input(text, block_id)
        else: st.header(text, anchor=block_id)
    elif b_type == "heading_3":
        if is_completion_prompt(text): render_text_or_input(text, block_id)
        else: st.subheader(text, anchor=block_id)
    elif b_type == "paragraph":
        if text:
            if is_completion_prompt(text): render_text_or_input(text, block_id)
            else: st.markdown(text)
    elif b_type == "bulleted_list_item":
        if is_completion_prompt(text): render_text_or_input(text, block_id)
        else: st.markdown(f"* {text}")
        if block.get("has_children"): render_children(block_id)
    elif b_type == "numbered_list_item":
        if is_completion_prompt(text): render_text_or_input(text, block_id)
        else: st.markdown(f"1. {text}")
        if block.get("has_children"): render_children(block_id)
    elif b_type == "callout":
        icon_data = block.get("callout", {}).get("icon", {})
        icon = icon_data.get("emoji") if icon_data.get("type") == "emoji" else "💡"
        
        # Schováme nepotřebné bloky z Notionu (např. ručně tvořené navigace)
        if "Navigace" in text or "pořadové studio" in text:
            return

        if is_completion_prompt(text):
            render_text_or_input(text, block_id)
        else:
            st.info(text if text else " ", icon=icon)
        if block.get("has_children"): render_children(block_id)
    elif b_type == "toggle":
        with st.expander(text or "Zobrazit detail"): render_children(block_id)
    elif b_type == "to_do":
        st.checkbox(text, value=block["to_do"].get("checked", False), key=f"todo_{block_id}")
    elif b_type == "image":
        img_url = block["image"].get("file", {}).get("url") or block["image"].get("external", {}).get("url")
        if img_url: st.image(img_url)
    elif b_type == "divider":
        st.divider()
    elif b_type == "table":
        rows = fetch_notion_blocks(block_id)
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
        cols_blocks = fetch_notion_blocks(block_id)
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
        if page_id: st.markdown(f"[🔗 Přejít na připojenou stránku](?page={format_uuid(page_id)})")
    elif b_type == "synced_block":
        target_id = block.get("synced_block", {}).get("synced_from", {}).get("block_id") or block_id
        render_children(target_id)

def render_children(block_id):
    for child in fetch_notion_blocks(block_id): render_block(child)

# --- VYKRESLENÍ HLAVNÍHO OBSAHU A VLASTNÍ NAVIGACE ---
active_blocks = fetch_notion_blocks(st.session_state["current_page_id"])
col1, main_col, col2 = st.columns([0.5, 5, 0.5])

with main_col:
    with st.container(border=True):
        if active_blocks:
            
            # --- RYCHLÁ NAVIGACE ---
            headings = [b for b in active_blocks if b["type"] in ["heading_1", "heading_2", "heading_3"]]
            if len(headings) > 1:
                st.markdown("### 📍 Rychlá navigace kapitolou")
                cols_count = min(len(headings), 3) 
                nav_cols = st.columns(cols_count)
                
                for i, h in enumerate(headings):
                    h_text = h[h["type"]].get("rich_text", [])
                    if h_text:
                        raw_text = "".join([t.get("plain_text", "") for t in h_text]).strip()
                        clean_text = re.sub(r"^(Doplň|Úkol|Otázka).*?:", "", raw_text, flags=re.IGNORECASE).strip()
                        h_id = format_uuid(h["id"])
                        with nav_cols[i % cols_count]:
                            st.markdown(f"<a href='#{h_id}' class='nav-link-box'>{clean_text}</a>", unsafe_allow_html=True)
                st.divider()
            
            # --- ZBYTEK OBSAHU ---
            for block in active_blocks: 
                render_block(block)
        else:
            st.warning("⚠️ Obsah se nepodařilo načíst (Ověřte sdílení stránky u integrace v Notionu).")
