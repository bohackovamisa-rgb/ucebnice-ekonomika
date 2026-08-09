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
        st.error(
            "⚠️ V nastavení Streamlit Secrets chybí proměnná APP_PASSWORD!"
        )
        return False

    if st.session_state.get("password_correct", False):
        return True

    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown(
                "<h2 style='text-align: center; border: none; font-weight: 800; color: #0F172A;"
                " margin-bottom: 0.2rem; font-size: 1.8rem;'>Soukromá učebnice</h2>",
                unsafe_allow_html=True,
            )
            st.markdown(
                "<p style='text-align: center; color: #64748B; font-size:"
                " 0.9rem; margin-bottom: 1.5rem;'>Zadejte přístupové heslo pro"
                " odemknutí kurzu.</p>",
                unsafe_allow_html=True,
            )
            password = st.text_input(
                "Heslo:",
                type="password",
                label_visibility="collapsed",
                placeholder="Přístupové heslo...",
            )
            if st.button("Vstoupit do učebnice 🚀", use_container_width=True):
                if password == app_pwd:
                    st.session_state["password_correct"] = True
                    st.rerun()
                else:
                    st.error("Nesprávné heslo")
    return False


if not check_password():
    st.stop()

# --- PREMIOVÝ DESIGN & STYLOVÁNÍ (PREMIUM EDTECH SYSTEM) ---
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700;800&display=swap');

/* Skrytí výchozí navigace Streamlitu */
[data-testid="stSidebarNav"] { display: none !important; }

/* 1. GLOBÁLNÍ POZADÍ A PÍSMO (PLUS JAKARTA SANS & OUTFIT) */
html, body, [class*="css"], .stApp {
    font-family: 'Plus Jakarta Sans', -apple-system, sans-serif !important;
    background: radial-gradient(circle at 50% 0%, #F8FAFC 0%, #F1F5F9 100%) !important;
    color: #0F172A !important;
}

/* 2. HLAVNÍ KONTEJNER A SKLENĚNÉ KARTY */
.main .block-container { 
    max-width: 960px !important; 
    padding-top: 2.5rem !important; 
    padding-bottom: 6rem !important; 
}

/* Moderní karty s efektem stínu a mikronajetím */
div[data-testid="stVerticalBlockBorderWrapper"] { 
    background: rgba(255, 255, 255, 0.85) !important;
    backdrop-filter: blur(12px) !important;
    border-radius: 20px !important; 
    border: 1px solid rgba(226, 232, 240, 0.8) !important; 
    box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.04), 0 4px 6px -2px rgba(0, 0, 0, 0.02) !important; 
    padding: 2.2rem !important; 
    margin-bottom: 1.8rem !important; 
    transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.25s ease !important;
}

div[data-testid="stVerticalBlockBorderWrapper"]:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 20px 35px -5px rgba(0, 0, 0, 0.06), 0 8px 10px -4px rgba(0, 0, 0, 0.03) !important;
}

/* 3. SHARP EXPRESNÍ TYPOGRAFIE */
h1 { 
    font-family: 'Outfit', sans-serif !important; 
    color: #0F172A !important; 
    font-weight: 800 !important; 
    font-size: 2.5rem !important; 
    letter-spacing: -0.04em !important; 
    line-height: 1.2 !important; 
    margin-bottom: 0.85rem !important; 
}

h2 { 
    font-family: 'Outfit', sans-serif !important; 
    color: #1E293B !important; 
    font-weight: 700 !important; 
    font-size: 1.5rem !important; 
    letter-spacing: -0.03em !important; 
    margin-top: 1.8rem !important; 
    margin-bottom: 1rem !important; 
    border-bottom: 2px solid #E2E8F0; 
    padding-bottom: 0.6rem; 
}

h3 { 
    font-family: 'Outfit', sans-serif !important; 
    color: #334155 !important; 
    font-weight: 600 !important; 
    font-size: 1.2rem !important; 
    margin-top: 1.4rem !important; 
}

p, li, td, th { 
    font-family: 'Plus Jakarta Sans', sans-serif !important; 
    color: #334155 !important; 
    font-size: 0.98rem !important; 
    line-height: 1.75 !important; 
    font-weight: 400 !important; 
}

/* 4. MODERNÍ NEOMORFNÍ A DYNAMICKÁ TLAČÍTKA */
button[data-testid="baseButton-primary"], 
button[kind="primary"] { 
    font-family: 'Plus Jakarta Sans', sans-serif !important; 
    border-radius: 14px !important; 
    border: none !important; 
    background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%) !important; 
    color: #FFFFFF !important; 
    font-weight: 600 !important; 
    font-size: 0.9rem !important; 
    padding: 0.65rem 1.4rem !important; 
    box-shadow: 0 4px 12px rgba(15, 23, 42, 0.25) !important; 
    transition: all 0.2s ease !important;
}
button[data-testid="baseButton-primary"]:hover, 
button[kind="primary"]:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 16px rgba(15, 23, 42, 0.35) !important;
}

button[data-testid="baseButton-secondary"], 
button[kind="secondary"] {
    font-family: 'Plus Jakarta Sans', sans-serif !important; 
    border-radius: 14px !important; 
    background-color: #FFFFFF !important;
    color: #475569 !important;
    border: 1px solid #E2E8F0 !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    padding: 0.65rem 1.4rem !important;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.02) !important;
    transition: all 0.2s ease !important;
}

button[data-testid="baseButton-secondary"]:hover, 
button[kind="secondary"]:hover {
    background-color: #F8FAFC !important;
    border-color: #CBD5E1 !important;
    color: #0F172A !important;
    transform: translateY(-1px) !important;
}

/* 5. VSTUPNÍ POLA ZNAČKOVÉHO VZHLEDU */
.stTextInput input, .stTextArea textarea, div[data-baseweb="select"] > div { 
    font-family: 'Plus Jakarta Sans', sans-serif !important; 
    border-radius: 14px !important; 
    border: 1.5px solid #E2E8F0 !important; 
    background-color: #FFFFFF !important; 
    color: #0F172A !important; 
    font-size: 0.95rem !important; 
    padding: 0.7rem 1rem !important; 
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.01) !important;
    transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
}

.stTextInput input:focus, .stTextArea textarea:focus, div[data-baseweb="select"] > div:focus {
    border-color: #6366F1 !important;
    box-shadow: 0 0 0 4px rgba(99, 102, 241, 0.1) !important;
}

/* 6. SIDEBAR S ELEGANTNÍM TÓNEM */
section[data-testid="stSidebar"] { 
    background: #F8FAFC !important; 
    border-right: 1px solid #E2E8F0 !important; 
}
.sidebar-section-title { 
    font-size: 0.75rem; 
    font-weight: 800; 
    color: #94A3B8; 
    text-transform: uppercase; 
    letter-spacing: 0.1em; 
    margin-top: 1.6rem; 
    margin-bottom: 0.7rem; 
}

/* 7. VYLEPŠENÉ BAREVNÉ BOXY (DESIGN SYSTEM BOXES) */
.box-blue { 
    background: linear-gradient(135deg, #EFF6FF 0%, #E0F2FE 100%) !important; 
    border-left: 4px solid #0284C7 !important; 
    padding: 1.25rem 1.4rem; 
    border-radius: 0 16px 16px 0; 
    margin: 1.2rem 0; 
    color: #0C4A6E !important; 
    font-size: 0.96rem; 
    box-shadow: 0 4px 12px rgba(2, 132, 199, 0.05);
}
.box-yellow { 
    background: linear-gradient(135deg, #FEFCE8 0%, #FEF3C7 100%) !important; 
    border-left: 4px solid #D97706 !important; 
    padding: 1.25rem 1.4rem; 
    border-radius: 0 16px 16px 0; 
    margin: 1.2rem 0; 
    color: #78350F !important; 
    font-size: 0.96rem; 
    box-shadow: 0 4px 12px rgba(217, 119, 6, 0.05);
}
.box-purple { 
    background: linear-gradient(135deg, #FAF5FF 0%, #F3E8FF 100%) !important; 
    border-left: 4px solid #9333EA !important; 
    padding: 1.25rem 1.4rem; 
    border-radius: 0 16px 16px 0; 
    margin: 1.2rem 0; 
    color: #581C87 !important; 
    font-size: 0.96rem; 
    word-wrap: break-word; 
    box-shadow: 0 4px 12px rgba(147, 51, 234, 0.05);
}
.box-green { 
    background: linear-gradient(135deg, #F0FDF4 0%, #DCFCE7 100%) !important; 
    border-left: 4px solid #16A34A !important; 
    padding: 1.25rem 1.4rem; 
    border-radius: 0 16px 16px 0; 
    margin: 1.2rem 0; 
    color: #14532D !important; 
    font-size: 0.96rem; 
    box-shadow: 0 4px 12px rgba(22, 163, 74, 0.05);
}
.box-red { 
    background: linear-gradient(135deg, #FEF2F2 0%, #FEE2E2 100%) !important; 
    border-left: 4px solid #DC2626 !important; 
    padding: 1.25rem 1.4rem; 
    border-radius: 0 16px 16px 0; 
    margin: 1.2rem 0; 
    color: #7F1D1D !important; 
    font-size: 0.96rem; 
    box-shadow: 0 4px 12px rgba(220, 38, 38, 0.05);
}
.box-gray { 
    background: linear-gradient(135deg, #F8FAFC 0%, #F1F5F9 100%) !important; 
    border-left: 4px solid #64748B !important; 
    padding: 1.25rem 1.4rem; 
    border-radius: 0 16px 16px 0; 
    margin: 1.2rem 0; 
    color: #334155 !important; 
    font-size: 0.96rem; 
    box-shadow: 0 4px 12px rgba(100, 116, 139, 0.05);
}

/* ODZNÁČEK HERO / KAPITOLA */
.hero-badge {
    background: linear-gradient(135deg, #4F46E5 0%, #6366F1 100%);
    color: white !important;
    padding: 0.35rem 0.9rem;
    border-radius: 9999px;
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    display: inline-block;
    margin-bottom: 0.8rem;
    box-shadow: 0 4px 10px rgba(79, 70, 229, 0.3);
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
            <span style='font-size: 0.72rem; font-weight: 800; color: #6366F1; text-transform: uppercase; letter-spacing: 0.1em;'>E-Learning Portal</span>
            <h2 style='margin: 0; padding: 0; border: none; font-size: 1.35rem; color: #0F172A; font-weight: 800;'>Učebnice Ekonomiky</h2>
        </div>
    """,
        unsafe_allow_html=True,
    )

    st.divider()

    # ÚVODNÍ STRÁNKA
    is_uvod = st.session_state["current_view"] == "Uvod"
    if st.button(
        "🏠 Úvodní stránka",
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

    if st.button("🚪 Odhlásit se", use_container_width=True):
        st.session_state["password_correct"] = False
        st.rerun()

# --- SMĚROVÁNÍ OBSAHU ---
if st.session_state["current_view"] == "Uvod":
    st.markdown("<span class='hero-badge'>INTERAKTIVNÍ KURZ</span>", unsafe_allow_html=True)
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
