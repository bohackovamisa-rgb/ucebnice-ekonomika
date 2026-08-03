import streamlit as st

# 1. Konfigurace stránky
st.set_page_config(
    page_title="Učebnice Ekonomiky",
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

    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("<h2 style='text-align: center; border: none; font-weight: 700; margin-bottom: 0;'>🔒 Soukromá učebnice</h2>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; color: #64748b; font-size: 0.85rem; margin-bottom: 1.5rem;'>Zadejte přístupové heslo pro odemknutí kurzu.</p>", unsafe_allow_html=True)
            password = st.text_input("Heslo:", type="password", label_visibility="collapsed", placeholder="Přístupové heslo...")
            if st.button("Vstoupit do učebnice", use_container_width=True):
                if password == app_pwd:
                    st.session_state["password_correct"] = True
                    st.rerun()
                else:
                    st.error("❌ Nesprávné heslo")
    return False

if not check_password():
    st.stop()

# --- STYLOVÁNÍ (MONTSERRAT + MODERNÍ MINIMALISMUS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Montserrat', sans-serif !important;
    }

    .stApp {
        background-color: #f8fafc;
        color: #0f172a;
    }

    .main .block-container {
        max-width: 880px !important;
        padding-top: 2.5rem !important;
        padding-bottom: 5rem !important;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #ffffff !important;
        border-radius: 12px !important;
        border: 1px solid #e2e8f0 !important;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.03) !important;
        padding: 1.75rem !important;
        margin-bottom: 1.25rem !important;
    }

    h1 {
        font-family: 'Montserrat', sans-serif !important;
        color: #0f172a !important;
        font-weight: 800 !important;
        font-size: 2.1rem !important;
        letter-spacing: -0.02em !important;
        line-height: 1.25 !important;
        margin-bottom: 0.5rem !important;
    }

    h2 {
        font-family: 'Montserrat', sans-serif !important;
        color: #1e293b !important;
        font-weight: 700 !important;
        font-size: 1.3rem !important;
        letter-spacing: -0.01em !important;
        margin-top: 1.5rem !important;
        margin-bottom: 0.75rem !important;
        border-bottom: 1px solid #f1f5f9;
        padding-bottom: 0.4rem;
    }

    h3 {
        font-family: 'Montserrat', sans-serif !important;
        color: #334155 !important;
        font-weight: 600 !important;
        font-size: 1.05rem !important;
        margin-top: 1.25rem !important;
    }

    p, li {
        font-family: 'Montserrat', sans-serif !important;
        color: #334155;
        font-size: 0.95rem;
        line-height: 1.7;
        font-weight: 400;
    }

    .icon-inline {
        display: inline-flex;
        align-items: center;
        margin-right: 6px;
        vertical-align: -2px;
    }

    .custom-callout {
        background-color: #f0f9ff;
        border-left: 3px solid #0284c7;
        border-radius: 0 8px 8px 0;
        padding: 1rem 1.25rem;
        margin: 1.25rem 0;
        color: #0369a1;
        font-size: 0.92rem;
    }

    .stTextInput input, .stTextArea textarea {
        font-family: 'Montserrat', sans-serif !important;
        border-radius: 8px !important;
        border: 1px solid #cbd5e1 !important;
        background-color: #ffffff !important;
        color: #0f172a !important;
        font-size: 0.9rem !important;
        padding: 0.6rem 0.8rem !important;
        transition: all 0.15s ease !important;
    }

    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #4f46e5 !important;
        box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1) !important;
    }

    .stButton > button {
        font-family: 'Montserrat', sans-serif !important;
        border-radius: 8px !important;
        border: 1px solid #cbd5e1 !important;
        background-color: #ffffff !important;
        color: #1e293b !important;
        font-weight: 600 !important;
        font-size: 0.85rem !important;
        padding: 0.5rem 1rem !important;
        box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.04) !important;
        transition: all 0.15s ease !important;
    }

    .stButton > button:hover {
        border-color: #4f46e5 !important;
        color: #4f46e5 !important;
        background-color: #f5f3ff !important;
    }

    section[data-testid="stSidebar"] {
        background-color: #ffffff !important;
        border-right: 1px solid #e2e8f0 !important;
    }

    .sidebar-section-title {
        font-size: 0.7rem;
        font-weight: 700;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-top: 1.2rem;
        margin-bottom: 0.4rem;
    }

    button[data-baseweb="tab"] {
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 600 !important;
        font-size: 0.88rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- SVG IKONY ---
SVG_LIGHTBULB = '<svg class="icon-inline" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#0284c7" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1.3.5 2.6 1.5 3.5.7.7 1.3 1.5 1.5 2.5"></path><path d="M9 18h6"></path><path d="M10 22h4"></path></svg>'

# --- NAVIGAČNÍ STAV ---
if "current_view" not in st.session_state:
    st.session_state["current_view"] = "Kapitola 1"

# --- BOČNÍ PANEL ---
with st.sidebar:
    st.markdown("""
        <div style='padding: 0.5rem 0 0.5rem 0;'>
            <span style='font-size: 0.7rem; font-weight: 700; color: #6366f1; text-transform: uppercase; letter-spacing: 0.08em;'>E-Learning Portal</span>
            <h2 style='margin: 0; padding: 0; border: none; font-size: 1.25rem; color: #0f172a; font-weight: 800;'>Učebnice Ekonomiky</h2>
        </div>
    """, unsafe_allow_html=True)
    
    st.divider()

    # --- KAPITOLY ---
    st.markdown("<div class='sidebar-section-title'>KAPITOLY KURZU</div>", unsafe_allow_html=True)
    chapters = {
        "Kapitola 1": "1. Podnikavost a startupy",
        "Kapitola 2": "2. Finance a osobní management",
        "Kapitola 3": "3. Výroba, náklady a efektivita",
        "Kapitola 4": "4. Zaměstnanci a trh práce",
        "Kapitola 5": "5. Stát, daně a ekonomika",
        "Kapitola 6": "6. Management a marketing"
    }

    for key, title in chapters.items():
        is_active = st.session_state["current_view"] == key
        btn_type = "primary" if is_active else "secondary"
        if st.button(title, key=f"nav_{key}", use_container_width=True, type=btn_type):
            st.session_state["current_view"] = key
            st.rerun()

    # --- OSOBNÍ A UČITELSKÁ ZÓNY ---
    st.markdown("<div class='sidebar-section-title'>STUDIUM A METODIKA</div>", unsafe_allow_html=True)
    
    # Tlačítko Moje pokroky
    is_pokroky = st.session_state["current_view"] == "Pokroky"
    if st.button("📈 Moje pokroky", key="nav_pokroky", use_container_width=True, type="primary" if is_pokroky else "secondary"):
        st.session_state["current_view"] = "Pokroky"
        st.rerun()

    # Tlačítko Učitelská základna
    is_ucitel = st.session_state["current_view"] == "Ucitel"
    if st.button("👩‍🏫 Učitelská základna", key="nav_ucitel", use_container_width=True, type="primary" if is_ucitel else "secondary"):
        st.session_state["current_view"] = "Ucitel"
        st.rerun()

    st.divider()
    
    if st.button("🔒 Odhlásit se", use_container_width=True):
        st.session_state["password_correct"] = False
        st.rerun()

# --- HLAVNÍ OBSAHOVÁ PLOCHA ---
view = st.session_state["current_view"]

if view == "Kapitola 1":
    st.markdown("<span style='color: #6366f1; font-weight: 700; font-size: 0.8rem; letter-spacing: 0.08em;'>KAPITOLA 1</span>", unsafe_allow_html=True)
    st.title("Podnikavost a startupová kultura")
    st.markdown("<p style='font-size: 1rem; color: #64748b; margin-bottom: 2rem;'>Od nápadu k ověřenému projektu, výběru právní formy a etickému podnikání.</p>", unsafe_allow_html=True)

    tab_text, tab_tasks, tab_canvas = st.tabs(["Výukový text", "Praktický projekt", "Lean Canvas & Reflexe"])

    with tab_text:
        with st.container(border=True):
            st.header("1. Podnikatel a základní pojmy")
            st.write("""
            Podnikatelem je podle občanského zákoníku ten, kdo samostatně vykonává na vlastní účet a odpovědnost 
            výdělečnou činnost živnostenským nebo obdobným způsobem se záměrem činit tak soustavně za účelem dosažení zisku.
            """)
            st.markdown(f"""
            <div class='custom-callout'>
                <strong>{SVG_LIGHTBULB} Klíčové pravidlo:</strong> Podnikatelé nenesou odpovědnost pouze vůči svému zisku, ale také vůči zákazníkům a prostředí (CSR).
            </div>
            """, unsafe_allow_html=True)

    with tab_tasks:
        with st.container(border=True):
            st.header("Váš podnikatelský záměr")
            st.text_input("1. Název projektu / nápadu:", placeholder="Napište název...", key="k1_nazev")
            st.text_area("2. Kdo je cílový zákazník?", placeholder="Popište skupinu...", height=90, key="k1_zakaznik")

    with tab_canvas:
        with st.container(border=True):
            st.header("Lean Canvas & Reflexe")
            st.text_area("Unikátní hodnota projektu:", placeholder="V čem jste jiní?", height=100, key="lc_val")

elif view == "Pokroky":
    st.markdown("<span style='color: #6366f1; font-weight: 700; font-size: 0.8rem; letter-spacing: 0.08em;'>STUDENTSKÁ ZÓNÁ</span>", unsafe_allow_html=True)
    st.title("📈 Moje pokroky")
    st.markdown("<p style='font-size: 1rem; color: #64748b; margin-bottom: 2rem;'>Přehled dokončených kapitol, uložených odpovědí a rozpracovaných projektů.</p>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        with st.container(border=True):
            st.metric(label="Dokončené kapitoly", value="1 / 6", delta="16 %")
    with c2:
        with st.container(border=True):
            st.metric(label="Vyplněné úkoly", value="4", delta="+2 dnes")
    with c3:
        with st.container(border=True):
            st.metric(label="Aktivní projekt", value="1", delta="Lean Canvas")

    with st.container(border=True):
        st.header("Moje uložené projekty")
        st.write("Zde uvidíte své uložené zápisky a Lean Canvas formuláře napříč všemi kapitolami.")
        st.info("Při dalším rozšíření sem můžeme přidat tlačítko **'Stáhnout mé podklady v PDF'** pro odevzdání učiteli!")

elif view == "Ucitel":
    st.markdown("<span style='color: #6366f1; font-weight: 700; font-size: 0.8rem; letter-spacing: 0.08em;'>METODICKÁ ZÓNÁ</span>", unsafe_allow_html=True)
    st.title("👩‍🏫 Učitelská základna & Řídící systém")
    st.markdown("<p style='font-size: 1rem; color: #64748b; margin-bottom: 2rem;'>Metodické pokyny, projektové scénáře do výuky a časové dotace pro lekce.</p>", unsafe_allow_html=True)

    with st.container(border=True):
        st.header("🎯 Projektové aktivity do hodin (Kapitola 1)")
        st.markdown("""
        **Aktivita: Startupový Pitch (45 min)**
        - **Cíl:** Žáci ve dvojicích formulují problém a řešení na základě Lean Canvas.
        - **Pomůcky:** Vyplněná záložka *Lean Canvas* v této učebnici.
        - **Postup:**
          1. 15 min – Individuální vyplnění políček v učebnici.
          2. 15 min – Vzájemná zpětná vazba ve dvojicích (Peer-review).
          3. 15 min – 60sekundový prezentace před třídou ("Elevator Pitch").
        """)

    with st.container(border=True):
        st.header("💡 Tipy pro hodnocení & reflexi")
        st.write("Doporučené otázky pro diskuzi na konci vyučovací hodiny:")
        st.markdown("""
        * *Co je největším rizikem při přechodu z OSVČ na s.r.o.?*
        * *Jak poznáme, že náš nápad řeší reálný problém a ne pouze naši představu?*
        """)

else:
    st.markdown("<span style='color: #6366f1; font-weight: 700; font-size: 0.8rem; letter-spacing: 0.08em;'>KAPITOLA</span>", unsafe_allow_html=True)
    st.title(chapters.get(view, view))
    with st.container(border=True):
        st.info("Tato kapitola čeká na vložení textu. Až budete připraveni, stačí mi poslat podklady.")
