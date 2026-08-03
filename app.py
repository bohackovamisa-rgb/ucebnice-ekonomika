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
            st.markdown("<p style='text-align: center; color: #64748b; font-size: 0.9rem; margin-bottom: 1.5rem;'>Zadejte přístupové heslo pro odemknutí kurzu.</p>", unsafe_allow_html=True)
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

# --- STYLOVÁNÍ (PURE SAAS / NOTION LOOK) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
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
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.02), 0 1px 2px -1px rgba(0, 0, 0, 0.02) !important;
        padding: 1.75rem !important;
        margin-bottom: 1.25rem !important;
    }

    /* Typografie */
    h1 {
        color: #0f172a !important;
        font-weight: 800 !important;
        font-size: 2.2rem !important;
        letter-spacing: -0.03em !important;
        line-height: 1.25 !important;
        margin-bottom: 0.5rem !important;
    }

    h2 {
        color: #1e293b !important;
        font-weight: 700 !important;
        font-size: 1.35rem !important;
        letter-spacing: -0.02em !important;
        margin-top: 1.5rem !important;
        margin-bottom: 0.75rem !important;
        border-bottom: 1px solid #f1f5f9;
        padding-bottom: 0.4rem;
    }

    h3 {
        color: #334155 !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        margin-top: 1.25rem !important;
    }

    p, li {
        color: #334155;
        font-size: 0.98rem;
        line-height: 1.75;
    }

    /* Zvýrazněný Callout Box */
    .custom-callout {
        background-color: #f0f9ff;
        border-left: 4px solid #0284c7;
        border-radius: 0 8px 8px 0;
        padding: 1rem 1.25rem;
        margin: 1.25rem 0;
        color: #0369a1;
        font-size: 0.95rem;
    }

    /* Interaktivní pole (Inputy) */
    .stTextInput input, .stTextArea textarea {
        border-radius: 8px !important;
        border: 1px solid #cbd5e1 !important;
        background-color: #ffffff !important;
        color: #0f172a !important;
        font-size: 0.95rem !important;
        padding: 0.6rem 0.8rem !important;
        transition: all 0.15s ease !important;
    }

    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #4f46e5 !important;
        box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1) !important;
    }

    /* Tlačítka */
    .stButton > button {
        border-radius: 8px !important;
        border: 1px solid #cbd5e1 !important;
        background-color: #ffffff !important;
        color: #1e293b !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
        padding: 0.5rem 1rem !important;
        box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05) !important;
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
    </style>
""", unsafe_allow_html=True)

# --- INICIALIZACE STAVU NAVIGACE ---
if "current_chapter" not in st.session_state:
    st.session_state["current_chapter"] = "Kapitola 1"

# --- BOČNÍ PANEL (NAVIGACE KAPITOL) ---
with st.sidebar:
    st.markdown("""
        <div style='padding: 0.5rem 0 1rem 0;'>
            <span style='font-size: 0.75rem; font-weight: 700; color: #6366f1; text-transform: uppercase; letter-spacing: 0.05em;'>E-Learning Portal</span>
            <h2 style='margin: 0; padding: 0; border: none; font-size: 1.3rem; color: #0f172a;'>Učebnice Ekonomiky</h2>
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
    st.markdown("<span style='color: #6366f1; font-weight: 600; font-size: 0.85rem; letter-spacing: 0.05em;'>KAPITOLA 1</span>", unsafe_allow_html=True)
    st.title("Podnikavost a startupová kultura")
    st.markdown("<p style='font-size: 1.05rem; color: #64748b; margin-bottom: 2rem;'>Od nápadu k ověřenému projektu, výběru právní formy a etickému podnikání.</p>", unsafe_allow_html=True)

    # Vnitřní navigace kapitoly (Záložky)
    tab_text, tab_tasks, tab_canvas = st.tabs(["📖 Výukový text", "✏️ Praktický projekt", "📊 Lean Canvas & Reflexe"])

    with tab_text:
        with st.container(border=True):
            st.header("1. Podnikatel a základní pojmy")
            st.write("""
            Podnikatelem je podle občanského zákoníku ten, kdo samostatně vykonává na vlastní účet a odpovědnost 
            výdělečnou činnost živnostenským nebo obdobným způsobem se záměrem činit tak soustavně za účelem dosažení zisku.
            """)
            
            st.markdown("""
            <div class='custom-callout'>
                <strong>💡 Klíčové pravidlo:</strong> Podnikatel nenesou odpovědnost pouze vůči svému zisku, ale také vůči zákazníkům, zaměstnancům a prostředí, ve kterém působí (CSR – Společenská odpovědnost firem).
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
            
            # Přehledná tabulka
            st.markdown("""
            | Forma | Ručení | Minimální kapitál |
            | :--- | :--- | :--- |
            | **s.r.o.** (Společnost s r.o.) | Omezené (do výše nesplaceného vkladu) | 1 Kč |
            | **a.s.** (Akciová společnost) | Společnost ručí celým majetkem, akcionáři neručí | 2 000 000 Kč |
            | **OSVČ** | Neomezené (celým osobním majetkem) | 0 Kč |
            """)

    with tab_tasks:
        with st.container(border=True):
            st.header("🚀 Váš podnikatelský záměr")
            st.write("Vyplňte základní strukturu vašeho napadnutého projektu nebo nápadu.")
            
            st.text_input("1. Název projektu / nápadu:", placeholder="Napište název...", key="k1_nazev")
            st.text_area("2. Kdo je cílový zákazník?", placeholder="Popište skupinu lidí, pro které projekt stavíte...", height=90, key="k1_zakaznik")
            st.text_area("3. Jaký problém zákazníka řešíte?", placeholder="Popište hlavní bolest nebo potřebu...", height=90, key="k1_problem")
            st.text_area("4. Jaké je vaše navrhované řešení?", placeholder="Stručně popsání produktu nebo služby...", height=90, key="k1_reseni")

    with tab_canvas:
        with st.container(border=True):
            st.header("📊 Lean Canvas šablona")
            st.write("Rychlý přehled biznis modelu vašeho nápadu.")
            
            c1, c2 = st.columns(2)
            with c1:
                st.text_area("Unikátní hodnota projektu:", placeholder="V čem jste jiní než konkurence?", height=100, key="lc_val")
                st.text_area("Struktura nákladů:", placeholder="Fixní a variabilní náklady...", height=100, key="lc_cost")
            with c2:
                st.text_area("První test (MVP):", placeholder="Jak nejrychleji a nejlevněji ověříte nápad?", height=100, key="lc_mvp")
                st.text_area("Zdroje příjmů:", placeholder="Za co přesně vám zákazník zaplatí?", height=100, key="lc_rev")
            
            st.divider()
            st.text_area("📝 Reflexe a sebehodnocení na konci kapitoly:", placeholder="Co nového jste se v této kapitole naučili?", height=80, key="k1_reflexe")

else:
    # Zástupný modul pro ostatní kapitoly
    st.markdown(f"<span style='color: #6366f1; font-weight: 600; font-size: 0.85rem;'>{active_chap.upper()}</span>", unsafe_allow_html=True)
    st.title(chapters[active_chap])
    with st.container(border=True):
        st.info("Tato kapitola je připravena pro vložení obsahu. Můžete mi poslat text a já ho hned zapracuji.")
