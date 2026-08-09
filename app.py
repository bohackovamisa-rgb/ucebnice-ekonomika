import math
import streamlit as st
from kapitoly import kapitola1, kapitola2, kapitola3, kapitola4, kapitola5, kapitola6

# --- 1. KONFIGURACE STRÁNKY ---
st.set_page_config(
    page_title="Učebnice ekonomiky", page_icon="📖", layout="wide"
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
            st.markdown(
                "<h2 style='text-align: center; border: none; font-weight: 800; color: #0F172A;"
                " margin-bottom: 0.5rem;'>Soukromá učebnice</h2>",
                unsafe_allow_html=True,
            )
            st.markdown(
                "<p style='text-align: center; color: #64748B; font-size:"
                " 0.95rem; margin-bottom: 1.5rem;'>Zadejte přístupové heslo pro"
                " odemknutí kurzu.</p>",
                unsafe_allow_html=True,
            )
            password = st.text_input(
                "Heslo:",
                type="password",
                label_visibility="collapsed",
                placeholder="Přístupové heslo...",
            )
            if st.button("Vstoupit do učebnice", use_container_width=True, type="primary"):
                if password == app_pwd:
                    st.session_state["password_correct"] = True
                    st.rerun()
                else:
                    st.error("Nesprávné heslo")
    return False

if not check_password():
    st.stop()

# --- STYLOVÁNÍ (VYLEPŠENÝ EDITORIAL STYL) ---
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&display=swap');

/* Skrytí výchozí navigace Streamlitu */
[data-testid="stSidebarNav"] { display: none !important; }

/* 1. ZÁKLADNÍ POZADÍ A PÍSMO (MONTSERRAT) */
html, body, [class*="css"], .stApp {
    font-family: 'Montserrat', -apple-system, sans-serif !important;
    background-color: #F8FAFC !important; /* Lehce čistší a modernější světlý odstín */
    color: #1E293B !important;
}

/* 2. ŠÍŘKA OBSAHU A ELEVACE KARET */
.main .block-container { 
    max-width: 920px !important; 
    padding-top: 2.5rem !important; 
    padding-bottom: 5rem !important; 
}

/* Skleněné a stínované karty s jemnou interakcí */
div[data-testid="stVerticalBlockBorderWrapper"] { 
    background-color: #FFFFFF !important; 
    border-radius: 16px !important; 
    border: 1px solid #E2E8F0 !important; 
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03) !important; 
    padding: 2rem !important; 
    margin-bottom: 1.5rem !important; 
    transition: transform 0.3s ease, box-shadow 0.3s ease !important;
}

div[data-testid="stVerticalBlockBorderWrapper"]:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -2px rgba(0, 0, 0, 0.04) !important;
}

/* 3. TYPOGRAFIE & NADPISY */
h1 { 
    font-family: 'Montserrat', sans-serif !important; 
    color: #0F172A !important; 
    font-weight: 800 !important; 
    font-size: 2.2rem !important; 
    letter-spacing: -0.03em !important; 
    line-height: 1.25 !important; 
    margin-bottom: 0.75rem !important; 
}

h2 { 
    font-family: 'Montserrat', sans-serif !important; 
    color: #1E293B !important; 
    font-weight: 700 !important; 
    font-size: 1.4rem !important; 
    letter-spacing: -0.02em !important; 
    margin-top: 1.5rem !important; 
    margin-bottom: 1rem !important; 
    border-bottom: 2px solid #F1F5F9; 
    padding-bottom: 0.5rem; 
}

h3 { 
    font-family: 'Montserrat', sans-serif !important; 
    color: #334155 !important; 
    font-weight: 600 !important; 
    font-size: 1.15rem !important; 
    margin-top: 1.25rem !important; 
}

p, li, td, th { 
    font-family: 'Montserrat', sans-serif !important; 
    color: #475569 !important; 
    font-size: 0.95rem !important; 
    line-height: 1.7 !important; 
    font-weight: 400 !important; 
}

/* 4. MODERNÍ TLAČÍTKA S HOVER EFEKTEM */
button[data-testid="baseButton-primary"], 
button[kind="primary"] { 
    font-family: 'Montserrat', sans-serif !important; 
    border-radius: 10px !important; 
    border: none !important; 
    background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%) !important; 
    color: #FFFFFF !important; 
    font-weight: 600 !important; 
    font-size: 0.9rem !important; 
    padding: 0.6rem 1.4rem !important; 
    box-shadow: 0 4px 6px rgba(15, 23, 42, 0.2) !important; 
    transition: all 0.2s ease !important;
}
button[data-testid="baseButton-primary"]:hover, 
button[kind="primary"]:hover {
    transform: translateY(-1px);
    box-shadow: 0 6px 12px rgba(15, 23, 42, 0.3) !important;
}

button[data-testid="baseButton-secondary"], 
button[kind="secondary"] {
    font-family: 'Montserrat', sans-serif !important; 
    border-radius: 10px !important; 
    background-color: #FFFFFF !important;
    color: #475569 !important;
    border: 1px solid #CBD5E1 !important;
    font-weight: 500 !important;
    font-size: 0.9rem !important;
    padding: 0.6rem 1.4rem !important;
    transition: all 0.2s ease !important;
}
button[data-testid="baseButton-secondary"]:hover, 
button[kind="secondary"]:hover {
    background-color: #F8FAFC !important;
    border-color: #94A3B8 !important;
    color: #0F172A !important;
}

/* 5. VSTUPNÍ POLA S FOCUS EFEKTEM */
.stTextInput input, .stTextArea textarea, div[data-baseweb="select"] > div { 
    font-family: 'Montserrat', sans-serif !important; 
    border-radius: 10px !important; 
    border: 1px solid #CBD5E1 !important; 
    background-color: #FFFFFF !important; 
    color: #0F172A !important; 
    font-size: 0.92rem !important; 
    padding: 0.65rem 0.9rem !important; 
    transition: all 0.2s ease !important;
}
.stTextInput input:focus, .stTextArea textarea:focus, div[data-baseweb="select"] > div:focus {
    border-color: #3B82F6 !important;
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.15) !important;
}

/* 6. BOČNÍ PANEL (SIDEBAR) */
section[data-testid="stSidebar"] { 
    background-color: #F8FAFC !important; 
    border-right: 1px solid #E2E8F0 !important; 
}
.sidebar-section-title { 
    font-size: 0.75rem; 
    font-weight: 700; 
    color: #94A3B8; 
    text-transform: uppercase; 
    letter-spacing: 0.08em; 
    margin-top: 1.6rem; 
    margin-bottom: 0.8rem; 
}

/* 7. JEMNÉ PASTELOVÉ BOXY (VYLADĚNÉ BARVY) */
.box-blue { 
    background-color: #EFF6FF !important; 
    border-left: 4px solid #3B82F6 !important; 
    padding: 1.2rem 1.4rem; 
    border-radius: 0 12px 12px 0; 
    margin: 1.2rem 0; 
    color: #1E3A8A !important; 
    font-size: 0.95rem; 
}
.box-yellow { 
    background-color: #FEFCE8 !important; 
    border-left: 4px solid #EAB308 !important; 
    padding: 1.2rem 1.4rem; 
    border-radius: 0 12px 12px 0; 
    margin: 1.2rem 0; 
    color: #713F12 !important; 
    font-size: 0.95rem; 
}
.box-purple { 
    background-color: #FAF5FF !important; 
    border-left: 4px solid #A855F7 !important; 
    padding: 1.2rem 1.4rem; 
    border-radius: 0 12px 12px 0; 
    margin: 1.2rem 0; 
    color: #581C87 !important; 
    font-size: 0.95rem; 
    word-wrap: break-word; 
}
.box-green { 
    background-color: #F0FDF4 !important; 
    border-left: 4px solid #22C55E !important; 
    padding: 1.2rem 1.4rem; 
    border-radius: 0 12px 12px 0; 
    margin: 1.2rem 0; 
    color: #14532D !important; 
    font-size: 0.95rem; 
}
.box-red { 
    background-color: #FEF2F2 !important; 
    border-left: 4px solid #EF4444 !important; 
    padding: 1.2rem 1.4rem; 
    border-radius: 0 12px 12px 0; 
    margin: 1.2rem 0; 
    color: #7F1D1D !important; 
    font-size: 0.95rem; 
}
.box-gray { 
    background-color: #F1F5F9 !important; 
    border-left: 4px solid #64748B !important; 
    padding: 1.2rem 1.4rem; 
    border-radius: 0 12px 12px 0; 
    margin: 1.2rem 0; 
    color: #334155 !important; 
    font-size: 0.95rem; 
}
</style>
""",
    unsafe_allow_html=True,
)

# --- NAVIGAČNÍ STAV ---
if "current_view" not in st.session_state:
    st.session_state["current_view"] = "Uvod"

# --- BOČNÍ PANEL ---
with st.sidebar:
    st.markdown(
        """
        <div style='padding: 0.5rem 0 0.5rem 0;'>
            <span style='font-size: 0.75rem; font-weight: 700; color: #64748B; text-transform: uppercase; letter-spacing: 0.1em;'>E-Learning Portal</span>
            <h2 style='margin: 0; padding: 0; border: none; font-size: 1.35rem; color: #0F172A; font-weight: 800;'>Učebnice Ekonomiky</h2>
        </div>
    """,
        unsafe_allow_html=True,
    )

    st.divider()

    # ÚVODNÍ STRÁNKA
    is_uvod = st.session_state["current_view"] == "Uvod"
    if st.button(
        "Úvodní stránka",
        key="nav_uvod",
        use_container_width=True,
        type="primary" if is_uvod else "secondary",
    ):
        st.session_state["current_view"] = "Uvod"
        st.rerun()

    # KAPITOLY KURZU
    st.markdown(
        "<div class='sidebar-section-title'>KAPITOLY KURZU</div>",
        unsafe_allow_html=True,
    )
    chapters = {
        "Kapitola 1": "1. Podnikavost a startupy",
        "Kapitola 2": "2. Finance a osobní management",
        "Kapitola 3": "3. Výroba, náklady a efektivita",
        "Kapitola 4": "4. Zaměstnanci a trh práce",
        "Kapitola 5": "5. Stát, daně a ekonomika",
        "Kapitola 6": "6. Management a marketing",
    }

    for key, title in chapters.items():
        is_active = st.session_state["current_view"] == key
        btn_type = "primary" if is_active else "secondary"
        if st.button(
            title, key=f"nav_{key}", use_container_width=True, type=btn_type
        ):
            st.session_state["current_view"] = key
            st.rerun()

    st.divider()

    if st.button("Odhlásit se", use_container_width=True):
        st.session_state["password_correct"] = False
        st.rerun()

# --- SMĚROVÁNÍ OBSAHU ---
if st.session_state["current_view"] == "Uvod":
    st.title("Ekonomika, která dává smysl")

    st.markdown(
        """
    <div class="box-gray">
        📚 <b>Moderní učebnice ekonomiky pro střední školy:</b> Podnikavost, finance & ekonomika v souvislostech.
    </div>
    <div class="box-green">
        🎯 <b>Cíl učebnice</b><br>
        Naučíš se propojit nápad, zákazníka, peníze, práci, stát, daně, marketing, rizika a odpovědnost do jednoho funkčního celku. Získáš dovednosti pro praktické rozhodování v reálném životě.
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown("### 📖 Jak s učebnicí pracovat")
    st.markdown("""
    1. **Otevři kapitolu z obsahu.** Nejprve si projdi úvod, rychlou orientaci a cíle kapitoly.
    2. **Čti po menších blocích.** Každá kapitola je členěná na výklad, příklady, tabulky, aktivity a reflexi.
    3. **Plň průběžné úkoly.** Žluté bloky slouží jako pracovní úkoly, otázky a aktivity.
    4. **Používej AI mentoring.** Fialové bloky obsahují prompty, které ti pomohou s vysvětlením, kontrolou nebo rozvojem tvého projektu.
    5. **Na konci kapitoly udělej reflexi.** Shrň, co už chápeš, co ještě potřebuješ dovysvětlit a jak bys téma použil/a v praxi.
    6. **Závěrečný projekt.** Na úplném konci propojíš všechno dohromady a vytvoříš návrh vlastního odpovědného projektu.
    """)

    st.divider()

    st.markdown("### 🧩 Legenda učebnice")
    st.markdown(
        """
    <div class="box-blue">📘 <b>Modrá:</b> Výklad, struktura, důležité vysvětlení</div>
    <div class="box-yellow">💡 <b>Žlutá:</b> Úkol, otázka, aktivita, procvičení</div>
    <div class="box-purple">🤖 <b>Fialová:</b> AI mentoring a práce s asistencí</div>
    <div class="box-green">✅ <b>Zelená:</b> Praxe, doporučení, dobrý postup</div>
    <div class="box-red">⚠️ <b>Červená / Oranžová:</b> Riziko, varování, právní nebo etický problém</div>
    <div class="box-gray">📄 <b>Šedá:</b> Zdroje, ověřování, učitelské poznámky</div>
    """,
        unsafe_allow_html=True,
    )

elif st.session_state["current_view"] == "Kapitola 1":
    if hasattr(kapitola1, "show"):
        kapitola1.show()
    elif hasattr(kapitola1, "render"):
        kapitola1.render()

elif st.session_state["current_view"] == "Kapitola 2":
    if hasattr(kapitola2, "show"):
        kapitola2.show()
    elif hasattr(kapitola2, "render"):
        kapitola2.render()

elif st.session_state["current_view"] == "Kapitola 3":
    if hasattr(kapitola3, "show"):
        kapitola3.show()
    elif hasattr(kapitola3, "render"):
        kapitola3.render()

elif st.session_state["current_view"] == "Kapitola 4":
    if hasattr(kapitola4, "show"):
        kapitola4.show()
    elif hasattr(kapitola4, "render"):
        kapitola4.render()

elif st.session_state["current_view"] == "Kapitola 5":
    if hasattr(kapitola5, "show"):
        kapitola5.show()
    elif hasattr(kapitola5, "render"):
        kapitola5.render()

elif st.session_state["current_view"] == "Kapitola 6":
    if hasattr(kapitola6, "show"):
        kapitola6.show()
    elif hasattr(kapitola6, "render"):
        kapitola6.render()
