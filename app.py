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
            st.markdown("<p style='text-align: center; color: #64748b; font-size: 0.9rem; margin-bottom: 1.5rem;'>Zadejte přístupové heslo pro odemknutí kurzu.</p>", unsafe_allow_html=True)
            password = st.text_input("Heslo:", type="password", label_visibility="collapsed", placeholder="Přístupové heslo...")
            if st.button("Vstoupit do kurzu", use_container_width=True):
                if password == app_pwd:
                    st.session_state["password_correct"] = True
                    st.rerun()
                else:
                    st.error("❌ Nesprávné heslo")
    return False

if not check_password():
    st.stop()

# --- MINIMALISTICKÉ SOFISTIKOVANÉ CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }

    /* Pozadí celé aplikace */
    .stApp {
        background-color: #f8fafc;
        color: #0f172a;
    }

    /* Šířka a zarovnání hlavního obsahu */
    .main .block-container {
        max-width: 860px !important;
        padding-top: 3rem !important;
        padding-bottom: 5rem !important;
    }

    /* Karty a kontejnery */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #ffffff !important;
        border-radius: 12px !important;
        border: 1px solid #e2e8f0 !important;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.02), 0 1px 2px -1px rgba(0, 0, 0, 0.02) !important;
        padding: 1.75rem !important;
        margin-bottom: 1rem !important;
    }

    /* Typografie */
    h1 {
        color: #0f172a !important;
        font-weight: 800 !important;
        font-size: 2.25rem !important;
        letter-spacing: -0.03em !important;
        line-height: 1.25 !important;
        margin-bottom: 0.5rem !important;
    }

    h2 {
        color: #1e293b !important;
        font-weight: 700 !important;
        font-size: 1.4rem !important;
        letter-spacing: -0.02em !important;
        margin-top: 1.75rem !important;
        margin-bottom: 0.75rem !important;
        border-bottom: 1px solid #f1f5f9;
        padding-bottom: 0.5rem;
    }

    h3 {
        color: #334155 !important;
        font-weight: 600 !important;
        font-size: 1.15rem !important;
        margin-top: 1.25rem !important;
    }

    p, li {
        color: #334155;
        font-size: 1rem;
        line-height: 1.7;
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

# --- BOČNÍ PANEL (NAVIGACE) ---
with st.sidebar:
    st.markdown("""
        <div style='padding: 0.5rem 0 1rem 0;'>
            <span style='font-size: 0.75rem; font-weight: 700; color: #6366f1; text-transform: uppercase; letter-spacing: 0.05em;'>E-Learning Kurz</span>
            <h2 style='margin: 0; padding: 0; border: none; font-size: 1.3rem; color: #0f172a;'>Ekonomika & Startup</h2>
        </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    chapters = {
        "Kapitola 1": "1. Podnikavost a startupová kultura",
        "Kapitola 2": "2. Finance a osobní management",
        "Kapitola 3": "3. Výroba, náklady a efektivita",
        "Kapitola 4": "4. Zaměstnanci a trh práce",
        "Kapitola 5": "5. Stát, daně a globální souvislosti",
        "Kapitola 6": "6. Management a marketing"
    }

    for key, title in chapters.items():
        # Zvýraznění aktivní kapitoly
        is_active = st.session_state["current_chapter"] == key
        btn_type = "primary" if is_active else "secondary"
        if st.button(title, key=f"nav_{key}", use_container_width=True, type=btn_type):
            st.session_state["current_chapter"] = key
            st.rerun()

    st.divider()
    
    if st.button("🔒 Odhlásit se", use_container_width=True):
        st.session_state["password_correct"] = False
        st.rerun()

# --- HLAVNÍ OBSAHOVÁ PLOCHA ---

active_chap = st.session_state["current_chapter"]

if active_chap == "Kapitola 1":
    
    # Hlavička kapitoly
    st.markdown("<span style='color: #6366f1; font-weight: 600; font-size: 0.9rem;'>KAPITOLA 1</span>", unsafe_allow_html=True)
    st.title("Podnikavost a startupová kultura")
    st.markdown("<p style='font-size: 1.1rem; color: #64748b; margin-bottom: 2rem;'>Jak přetavit nápad v ověřitelný projekt, zvolit správnou právní formu a uvažovat v souvislostech.</p>", unsafe_allow_html=True)

    # Rychlé záložky / Rychlá navigace sekcemi
    tab1, tab2, tab3 = st.tabs(["📖 Výukový text", "✏️ Praktický úkol", "💡 Lean Canvas"])

    with tab1:
        with st.container(border=True):
            st.header("1. Podnikatel a jeho úloha")
            st.write("""
            Podnikatel je osoba, která samostatně vykonává na vlastní účet a odpovědnost živnostenskou 
            nebo obdobnou činnost se záměrem činit tak soustavně za účelem dosažení zisku.
            """)
            
            st.markdown("""
            <div class='custom-callout'>
                <strong>💡 Hlavní myšlenka:</strong> Podnikání není pouze o riziku, ale především o vyhledávání příležitostí a řešení problémů zákazníků.
            </div>
            """, unsafe_allow_html=True)

            st.header("2. OSVČ a živnosti")
            st.write("""
            Fyzická osoba může podnikat nejčastěji jako **OSVČ** (Osoba samostatně výdělečně činná). 
            Živnosti rozdělujeme do následujících kategorií:
            """)
            st.markdown("""
            * **Volná:** Není potřeba odborná způsobilost.
            * **Řemeslná:** Vyžaduje výuční list nebo praxi.
            * **Vázaná:** Vyžaduje specifické vzdělání či zkoušky.
            * **Koncesovaná:** Vyžaduje státní povolení (koncesi).
            """)

    with tab2:
        with st.container(border=True):
            st.header("Reflexe a příprava nápadu")
            st.write("Vyplňte následující pole pro váš projekt. Odpovědi se uchovávají v rámci vaší lekce.")
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.text_input("🚀 Název vašeho projektu:", placeholder="Např. Ekologické obaly z houbového mycelia...")
            st.text_area("👥 Kdo je váš cílový zákazník?", placeholder="Popište konkrétní skupinu lidí, kterým projekt řeší problém...", height=100)
            st.text_area("🚨 Jaký hlavní problém zákazníka řešíte?", placeholder="Stručně popište zákaznickou bolest...", height=100)

    with tab3:
        with st.container(border=True):
            st.header("Lean Canvas šablona")
            st.write("Stručný přehled obchodního modelu na jedné stránce.")
            
            col_a, col_b = st.columns(2)
            with col_a:
                st.text_area("💎 Hodnota pro zákazníka:", height=120)
                st.text_area("💰 Nákladová struktura:", height=120)
            with col_b:
                st.text_area("💡 Navrhované řešení:", height=120)
                st.text_area("🏷️ Zdroje příjmů:", height=120)

else:
    # Zástupný modul pro ostatní kapitoly
    st.markdown(f"<span style='color: #6366f1; font-weight: 600; font-size: 0.9rem;'>{active_chap.upper()}</span>", unsafe_allow_html=True)
    st.title(chapters[active_chap])
    
    with st.container(border=True):
        st.info("Obsah této kapitoly můžete snadno vložit jako čistý kód.")
