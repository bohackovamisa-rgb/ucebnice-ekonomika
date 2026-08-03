import streamlit as st

# 1. Konfigurace stránky
st.set_page_config(
    page_title="Učebnice Ekonomiky",
    page_icon="📖",
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
    /* Import písma Montserrat */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Montserrat', sans-serif !important;
    }

    .stApp {
        background-color: #f8fafc;
        color: #0f172a;
    }

    /* Šířka a zarovnání hlavního obsahu */
    .main .block-container {
        max-width: 880px !important;
        padding-top: 2.5rem !important;
        padding-bottom: 5rem !important;
    }

    /* Karty a kontejnery */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #ffffff !important;
        border-radius: 12px !important;
        border: 1px solid #e2e8f0 !important;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.03) !important;
        padding: 1.75rem !important;
        margin-bottom: 1.25rem !important;
    }

    /* Typografie v Montserrat */
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

    /* Styling moderních ikon v textu */
    .icon-inline {
        display: inline-flex;
        align-items: center;
        margin-right: 6px;
        vertical-align: -2px;
    }

    /* Zvýrazněný Callout Box */
    .custom-callout {
        background-color: #f0f9ff;
        border-left: 3px solid #0284c7;
        border-radius: 0 8px 8px 0;
        padding: 1rem 1.25rem;
        margin: 1.25rem 0;
        color: #0369a1;
        font-size: 0.92rem;
    }

    /* Interaktivní pole (Inputy) */
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

    /* Tlačítka */
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

    /* Boční panel */
    section[data-testid="stSidebar"] {
        background-color: #ffffff !important;
        border-right: 1px solid #e2e8f0 !important;
    }

    /* Vzhled Tabs */
    button[data-baseweb="tab"] {
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 600 !important;
        font-size: 0.88rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- IAKONY SVG (LUCIDE STYLE) ---
SVG_BOOK = '<svg class="icon-inline" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#4f46e5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>'
SVG_EDIT = '<svg class="icon-inline" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#4f46e5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg>'
SVG_CHART = '<svg class="icon-inline" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#4f46e5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg>'
SVG_LIGHTBULB = '<svg class="icon-inline" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#0284c7" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1.3.5 2.6 1.5 3.5.7.7 1.3 1.5 1.5 2.5"></path><path d="M9 18h6"></path><path d="M10 22h4"></path></svg>'

# --- INICIALIZACE STAVU NAVIGACE ---
if "current_chapter" not in st.session_state:
    st.session_state["current_chapter"] = "Kapitola 1"

# --- BOČNÍ PANEL (NAVIGACE KAPITOL) ---
with st.sidebar:
    st.markdown("""
        <div style='padding: 0.5rem 0 1rem 0;'>
            <span style='font-size: 0.7rem; font-weight: 700; color: #6366f1; text-transform: uppercase; letter-spacing: 0.08em;'>E-Learning Portal</span>
            <h2 style='margin: 0; padding: 0; border: none; font-size: 1.25rem; color: #0f172a; font-weight: 800;'>Učebnice Ekonomiky</h2>
        </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    chapters = {
        "Kapitola 1": "1. Podnikavost a startupy",
        "Kapitola 2": "2. Finance a osobní management",
        "Kapitola 3": "3. Výroba, náklady a efektivita",
        "Kapitola 4": "4. Zaměstnanci a trh práce",
        "Kapitola 5": "5. Stát, daně a ekonomika",
        "Kapitola 6": "6. Management a marketing"
    }

    for key, title in chapters.items():
        is_active = st.session_state["current_chapter"] == key
        btn_type = "primary" if is_active else "secondary"
        if st.button(title, key=f"nav_{key}", use_container_width=True, type=btn_type):
            st.session_state["current_chapter"] = key
            st.rerun()

    st.divider()
    
    if st.button("🔒 Odhlásit se", use_container_width=True):
        st.session_state["password_correct"] = False
        st.rerun()

# --- HLAVNÍ PLOCHA A OBSAH KAPITOL ---
active_chap = st.session_state["current_chapter"]

if active_chap == "Kapitola 1":
    st.markdown("<span style='color: #6366f1; font-weight: 700; font-size: 0.8rem; letter-spacing: 0.08em;'>KAPITOLA 1</span>", unsafe_allow_html=True)
    st.title("Podnikavost a startupová kultura")
    st.markdown("<p style='font-size: 1rem; color: #64748b; margin-bottom: 2rem; font-weight: 400;'>Od nápadu k ověřenému projektu, výběru právní formy a etickému podnikání.</p>", unsafe_allow_html=True)

    # Vnitřní navigace kapitoly (Záložky s SVG ikonami)
    tab_text, tab_tasks, tab_canvas = st.tabs([
        "Výukový text", 
        "Praktický projekt", 
        "Lean Canvas & Reflexe"
    ])

    with tab_text:
        with st.container(border=True):
            st.header("1. Podnikatel a základní pojmy")
            st.write("""
            Podnikatelem je podle občanského zákoníku ten, kdo samostatně vykonává na vlastní účet a odpovědnost 
            výdělečnou činnost živnostenským nebo obdobným způsobem se záměrem činit tak soustavně za účelem dosažení zisku.
            """)
            
            st.markdown(f"""
            <div class='custom-callout'>
                <strong>{SVG_LIGHTBULB} Klíčové pravidlo:</strong> Podnikatelé nenesou odpovědnost pouze vůči svému zisku, ale také vůči zákazníkům, zaměstnancům a prostředí, ve kterém působí (CSR – Společenská odpovědnost firem).
            </div>
            """, unsafe_allow_html=True)

            st.header("2. OSVČ a druhy živností")
            st.write("Fyzická osoba nejčastěji podniká jako osoba samostatně výdělečně činná (OSVČ). Živnosti se dělí podle podmínek získání:")
            
            st.markdown("""
            - **Volné:** Stačí splnit všeobecné podmínky (věk 18 let, způsobilost, bezúhonnost). Není vyžadováno odborné vzdělání.
            - **Řemeslné:** Vyžadují odbornou způsobilost (výuční list, maturitu v oboru nebo praxi).
            - **Vázané:** Vyžadují specifickou odbornou způsobilost definovanou zákony (např. autoškola, účetnictví).
            - **Koncesované:** Vyžadují státní povolení – koncesi (např. taxislužba, prodej zbraní).
            """)

            st.header("3. Obchodní korporace")
            st.write("Pokud podnikatel zakládá právnickou osobu, nejčastěji volí mezi kapitálovými a osobními společnostmi:")
            
            st.markdown("""
            | Forma | Ručení | Minimální kapitál |
            | :--- | :--- | :--- |
            | **s.r.o.** (Společnost s r.o.) | Omezené (do výše nesplaceného vkladu) | 1 Kč |
            | **a.s.** (Akciová společnost) | Společnost ručí celým majetkem, akcionáři neručí | 2 000 000 Kč |
            | **OSVČ** | Neomezené (celým osobním majetkem) | 0 Kč |
            """)

    with tab_tasks:
        with st.container(border=True):
            st.header("Váš podnikatelský záměr")
            st.write("Vyplňte základní strukturu vašeho napadnutého projektu nebo nápadu.")
            
            st.text_input("1. Název projektu / nápadu:", placeholder="Napište název...", key="k1_nazev")
            st.text_area("2. Kdo je cílový zákazník?", placeholder="Popište skupinu lidí, pro které projekt stavíte...", height=90, key="k1_zakaznik")
            st.text_area("3. Jaký problém zákazníka řešíte?", placeholder="Popište hlavní bolest nebo potřebu...", height=90, key="k1_problem")
            st.text_area("4. Jaké je vaše navrhované řešení?", placeholder="Stručně popsání produktu nebo služby...", height=90, key="k1_reseni")

    with tab_canvas:
        with st.container(border=True):
            st.header("Lean Canvas šablona")
            st.write("Rychlý přehled biznis modelu vašeho nápadu.")
            
            c1, c2 = st.columns(2)
            with c1:
                st.text_area("Unikátní hodnota projektu:", placeholder="V čem jste jiní než konkurence?", height=100, key="lc_val")
                st.text_area("Struktura nákladů:", placeholder="Fixní a variabilní náklady...", height=100, key="lc_cost")
            with c2:
                st.text_area("První test (MVP):", placeholder="Jak nejrychleji a nejlevněji ověříte nápad?", height=100, key="lc_mvp")
                st.text_area("Zdroje příjmů:", placeholder="Za co přesně vám zákazník zaplatí?", height=100, key="lc_rev")
            
            st.divider()
            st.text_area("Reflexe a sebehodnocení na konci kapitoly:", placeholder="Co nového jste se v této kapitole naučili?", height=80, key="k1_reflexe")

else:
    # Zástupný modul pro ostatní kapitoly
    st.markdown(f"<span style='color: #6366f1; font-weight: 700; font-size: 0.8rem; letter-spacing: 0.08em;'>{active_chap.upper()}</span>", unsafe_allow_html=True)
    st.title(chapters[active_chap])
    with st.container(border=True):
        st.info("Tato kapitola je připravena pro vložení obsahu. Můžete mi poslat text a já ho hned zapracuji.")
