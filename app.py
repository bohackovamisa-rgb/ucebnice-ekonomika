import math
import streamlit as st
from supabase import create_client, Client
from kapitoly import kapitola1, kapitola2, kapitola3, kapitola4, kapitola5, kapitola6

# --- 1. KONFIGURACE STRÁNKY ---
st.set_page_config(
    page_title="Učebnice ekonomiky", page_icon="📖", layout="wide"
)

# --- 2. PROPOJENÍ S DATABÁZÍ SUPABASE ---
@st.cache_resource
def init_supabase() -> Client:
    url = st.secrets["connections"]["supabase"]["SUPABASE_URL"]
    key = st.secrets["connections"]["supabase"]["SUPABASE_KEY"]
    return create_client(url, key)

supabase = init_supabase()

# --- 3. STYLOVÁNÍ ---
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&display=swap');

[data-testid="stSidebarNav"] { display: none !important; }

html, body, [class*="css"], .stApp { font-family: 'Montserrat', -apple-system, sans-serif !important; background-color: #FAF8F5 !important; color: #1C1917 !important; }
.main .block-container { max-width: 920px !important; padding-top: 2.5rem !important; padding-bottom: 5rem !important; }

div[data-testid="stVerticalBlockBorderWrapper"] { background-color: #FFFFFF !important; border-radius: 18px !important; border: 1px solid #EAE7DC !important; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03) !important; padding: 2rem !important; margin-bottom: 1.5rem !important; transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s ease !important; }
div[data-testid="stVerticalBlockBorderWrapper"]:hover { transform: translateY(-2px); box-shadow: 0 12px 25px rgba(0, 0, 0, 0.05), 0 4px 10px rgba(0, 0, 0, 0.02) !important; }

h1 { font-family: 'Montserrat', sans-serif !important; color: #0F172A !important; font-weight: 800 !important; font-size: 2.2rem !important; letter-spacing: -0.03em !important; line-height: 1.25 !important; margin-bottom: 0.75rem !important; }
h2 { font-family: 'Montserrat', sans-serif !important; color: #1E293B !important; font-weight: 700 !important; font-size: 1.35rem !important; letter-spacing: -0.02em !important; margin-top: 1.5rem !important; margin-bottom: 0.85rem !important; border-bottom: 1px solid #F1F5F9; padding-bottom: 0.5rem; }
h3 { font-family: 'Montserrat', sans-serif !important; color: #334155 !important; font-weight: 600 !important; font-size: 1.1rem !important; margin-top: 1.25rem !important; }
p, li, td, th { font-family: 'Montserrat', sans-serif !important; color: #334155 !important; font-size: 0.95rem !important; line-height: 1.7 !important; font-weight: 400 !important; }

button[data-testid="baseButton-primary"], button[kind="primary"] { font-family: 'Montserrat', sans-serif !important; border-radius: 9999px !important; border: 1px solid #111111 !important; background-color: #111111 !important; color: #FFFFFF !important; font-weight: 600 !important; font-size: 0.88rem !important; padding: 0.6rem 1.4rem !important; box-shadow: 0 4px 10px rgba(17, 17, 17, 0.15) !important; transition: all 0.2s ease !important; }
button[data-testid="baseButton-primary"]:hover, button[kind="primary"]:hover { transform: translateY(-1px); box-shadow: 0 6px 14px rgba(17, 17, 17, 0.25) !important; }
button[data-testid="baseButton-primary"] *, button[kind="primary"] * { color: #FFFFFF !important; }

button[data-testid="baseButton-secondary"], button[kind="secondary"] { font-family: 'Montserrat', sans-serif !important; border-radius: 9999px !important; background-color: #F2EFE9 !important; color: #44403C !important; border: 1px solid #E2DEC6 !important; font-weight: 500 !important; font-size: 0.88rem !important; padding: 0.6rem 1.4rem !important; transition: all 0.2s ease !important; }
button[data-testid="baseButton-secondary"] *, button[kind="secondary"] * { color: #44403C !important; }
button[data-testid="baseButton-secondary"]:hover, button[kind="secondary"]:hover { background-color: #111111 !important; border-color: #111111 !important; color: #FFFFFF !important; transform: translateY(-1px); }
button[data-testid="baseButton-secondary"]:hover *, button[kind="secondary"]:hover * { color: #FFFFFF !important; }

.stTextInput input, .stTextArea textarea, div[data-baseweb="select"] > div { font-family: 'Montserrat', sans-serif !important; border-radius: 12px !important; border: 1px solid #E2DEC6 !important; background-color: #F2EFE9 !important; color: #0F172A !important; font-size: 0.92rem !important; padding: 0.65rem 0.9rem !important; transition: all 0.2s ease !important; }
.stTextInput input:focus, .stTextArea textarea:focus, div[data-baseweb="select"] > div:focus { border-color: #111111 !important; background-color: #FFFFFF !important; box-shadow: 0 0 0 3px rgba(17, 17, 17, 0.1) !important; }

section[data-testid="stSidebar"] { background-color: #FAF8F5 !important; border-right: 1px solid #E5E0D8 !important; }
.sidebar-section-title { font-size: 0.72rem; font-weight: 700; color: #78716C; text-transform: uppercase; letter-spacing: 0.08em; margin-top: 1.4rem; margin-bottom: 0.6rem; }

.box-blue { background-color: #F4F7F9 !important; border-left: 3px solid #8AA2B6 !important; padding: 1.1rem 1.3rem; border-radius: 0 12px 12px 0; margin: 1rem 0; color: #2C3E50 !important; font-size: 0.93rem; }
.box-yellow { background-color: #FAF7EE !important; border-left: 3px solid #D8C397 !important; padding: 1.1rem 1.3rem; border-radius: 0 12px 12px 0; margin: 1rem 0; color: #5C4E31 !important; font-size: 0.93rem; }
.box-purple { background-color: #F8F5F8 !important; border-left: 3px solid #B4A2B8 !important; padding: 1.1rem 1.3rem; border-radius: 0 12px 12px 0; margin: 1rem 0; color: #4A3B4E !important; font-size: 0.93rem; word-wrap: break-word; }
.box-green { background-color: #F3F6F3 !important; border-left: 3px solid #8DAE93 !important; padding: 1.1rem 1.3rem; border-radius: 0 12px 12px 0; margin: 1rem 0; color: #2A4231 !important; font-size: 0.93rem; }
.box-red { background-color: #FAF3F3 !important; border-left: 3px solid #C98A8A !important; padding: 1.1rem 1.3rem; border-radius: 0 12px 12px 0; margin: 1rem 0; color: #5C2E2E !important; font-size: 0.93rem; }
.box-gray { background-color: #F2EFE9 !important; border-left: 3px solid #A8A29E !important; padding: 1.1rem 1.3rem; border-radius: 0 12px 12px 0; margin: 1rem 0; color: #44403C !important; font-size: 0.93rem; }
</style>
""",
    unsafe_allow_html=True,
)

# --- 4. PŘIHLAŠOVACÍ BRÁNA (NAPOJENÍ NA SUPABASE) ---
def login_screen():
    if st.session_state.get("is_logged_in", False):
        return True

    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("<h2 style='text-align: center; border: none; font-weight: 700; margin-bottom: 0;'>Soukromá učebnice</h2>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; color: #78716c; font-size: 0.85rem; margin-bottom: 1.5rem;'>Zadejte jméno a heslo pro odemknutí kurzu.</p>", unsafe_allow_html=True)
            
            with st.form("login_form", border=False):
                username_input = st.text_input("Uživatelské jméno:", placeholder="Zadejte uživatelské jméno...")
                password_input = st.text_input("Heslo:", type="password", placeholder="Vaše heslo...")
                
                submit = st.form_submit_button("Vstoupit do učebnice", use_container_width=True)
                
                if submit:
                    try:
                        # Dotaz do Supabase
                        response = supabase.table("uzivatele").select("*").eq("username", username_input.strip().lower()).execute()
                        users = response.data

                        if users:
                            user = users[0]
                            if str(user.get("password")) == password_input:
                                st.session_state["is_logged_in"] = True
                                st.session_state["username"] = user.get("username")
                                st.session_state["user_role"] = user.get("role", "student")
                                st.session_state["user_name"] = user.get("jmeno", "Uživatel")
                                
                                if user.get("role") == "teacher":
                                    tridy_raw = user.get("trida", "")
                                    st.session_state["user_classes"] = [t.strip() for t in tridy_raw.split(",") if t.strip()]
                                else:
                                    st.session_state["user_class"] = user.get("trida", "")
                                    
                                st.rerun()
                            else:
                                st.error("Nesprávné heslo!")
                        else:
                            st.error("Uživatel s tímto jménem neexistuje!")
                    except Exception as e:
                        st.error(f"Chyba při připojení k databázi: {e}")
    return False

if not login_screen():
    st.stop()

# Spustíme přihlašování. Pokud se nevrátí True (uživatel není přihlášený), aplikace se zde zastaví.
if not login_screen():
    st.stop()


# --- NAVIGAČNÍ STAV ---
if "current_view" not in st.session_state:
    st.session_state["current_view"] = "Uvod"

# --- BOČNÍ PANEL S PROFILEM ---
with st.sidebar:
    st.markdown(
        """
        <div style='padding: 0.5rem 0 0.5rem 0;'>
            <span style='font-size: 0.7rem; font-weight: 700; color: #44403C; text-transform: uppercase; letter-spacing: 0.08em;'>E-Learning Portal</span>
            <h2 style='margin: 0; padding: 0; border: none; font-size: 1.25rem; color: #0F172A; font-weight: 800;'>Učebnice Ekonomiky</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Profilový rámeček s informací, kdo je přihlášený
    st.markdown(
        f"""
        <div style='background-color: #F2EFE9; padding: 1rem; border-radius: 12px; margin-bottom: 1.5rem; border: 1px solid #EAE7DC;'>
            <div style='font-size: 0.75rem; color: #78716C; font-weight: 600;'>PŘIHLÁŠEN(A):</div>
            <div style='font-size: 1.05rem; font-weight: 700; color: #1C1917;'>👤 {st.session_state['user_name']}</div>
            <div style='font-size: 0.85rem; color: #44403C; margin-top: 0.2rem;'>Role: {st.session_state['user_role'].capitalize()}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # UČITELSKÝ PANEL (Viditelný pouze pro učitele)
    if st.session_state["user_role"] == "teacher":
        st.markdown("<div class='sidebar-section-title'>👩‍🏫 UČITELSKÝ PANEL</div>", unsafe_allow_html=True)
        vybrana_trida = st.selectbox("Spravovat třídu:", st.session_state["user_classes"], label_visibility="collapsed")
        
        if st.button("📊 Přehled výsledků třídy", use_container_width=True, type="secondary"):
            st.session_state["current_view"] = "Ucitel_Panel"
            st.rerun()
        st.divider()

    # KAPITOLY KURZU
    st.markdown(
        "<div class='sidebar-section-title'>KAPITOLY KURZU</div>",
        unsafe_allow_html=True,
    )
    
    is_uvod = st.session_state["current_view"] == "Uvod"
    if st.button(
        "Úvodní stránka",
        key="nav_uvod",
        use_container_width=True,
        type="primary" if is_uvod else "secondary",
    ):
        st.session_state["current_view"] = "Uvod"
        st.rerun()

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
        st.session_state.clear()
        st.rerun()

# --- SMĚROVÁNÍ OBSAHU ---

if st.session_state["current_view"] == "Ucitel_Panel":
    st.title("📊 Přehled výsledků žáků")
    st.info("Zde jako učitel v budoucnu uvidíš výsledky kvízů, průchod učebnicí nebo odevzdané Projektové pasy od žáků z tvých tříd.")

elif st.session_state["current_view"] == "Uvod":
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
        

# --- STYLOVÁNÍ (PŮVODNÍ BARVY + VYLEPŠENÁ HLOUBKA A INTERAKCE) ---
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&display=swap');

/* Skrytí výchozí navigace Streamlitu */
[data-testid="stSidebarNav"] { display: none !important; }

/* 1. ZÁKLADNÍ POZADÍ A PÍSMO (MONTSERRAT) */
html, body, [class*="css"], .stApp {
    font-family: 'Montserrat', -apple-system, sans-serif !important;
    background-color: #FAF8F5 !important; /* TVOJE PŮVODNÍ POZADÍ */
    color: #1C1917 !important;
}

/* 2. ŠÍŘKA OBSAHU A ELEVACE KARET */
.main .block-container { 
    max-width: 920px !important; 
    padding-top: 2.5rem !important; 
    padding-bottom: 5rem !important; 
}

/* Vyladěné stínování a hover efekt pro kontejnery */
div[data-testid="stVerticalBlockBorderWrapper"] { 
    background-color: #FFFFFF !important; 
    border-radius: 18px !important; 
    border: 1px solid #EAE7DC !important; 
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03) !important; 
    padding: 2rem !important; 
    margin-bottom: 1.5rem !important; 
    transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s ease !important;
}

div[data-testid="stVerticalBlockBorderWrapper"]:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 25px rgba(0, 0, 0, 0.05), 0 4px 10px rgba(0, 0, 0, 0.02) !important;
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
    font-size: 1.35rem !important; 
    letter-spacing: -0.02em !important; 
    margin-top: 1.5rem !important; 
    margin-bottom: 0.85rem !important; 
    border-bottom: 1px solid #F1F5F9; 
    padding-bottom: 0.5rem; 
}

h3 { 
    font-family: 'Montserrat', sans-serif !important; 
    color: #334155 !important; 
    font-weight: 600 !important; 
    font-size: 1.1rem !important; 
    margin-top: 1.25rem !important; 
}

p, li, td, th { 
    font-family: 'Montserrat', sans-serif !important; 
    color: #334155 !important; 
    font-size: 0.95rem !important; 
    line-height: 1.7 !important; 
    font-weight: 400 !important; 
}

/* 4. TLAČÍTKA (PŮVODNÍ BARVY + LEPŠÍ HOVER) */
button[data-testid="baseButton-primary"], 
button[kind="primary"] { 
    font-family: 'Montserrat', sans-serif !important; 
    border-radius: 9999px !important; 
    border: 1px solid #111111 !important; 
    background-color: #111111 !important; 
    color: #FFFFFF !important; 
    font-weight: 600 !important; 
    font-size: 0.88rem !important; 
    padding: 0.6rem 1.4rem !important; 
    box-shadow: 0 4px 10px rgba(17, 17, 17, 0.15) !important; 
    transition: all 0.2s ease !important;
}
button[data-testid="baseButton-primary"]:hover, 
button[kind="primary"]:hover {
    transform: translateY(-1px);
    box-shadow: 0 6px 14px rgba(17, 17, 17, 0.25) !important;
}
button[data-testid="baseButton-primary"] *, 
button[kind="primary"] * {
    color: #FFFFFF !important;
}

button[data-testid="baseButton-secondary"], 
button[kind="secondary"] {
    font-family: 'Montserrat', sans-serif !important; 
    border-radius: 9999px !important; 
    background-color: #F2EFE9 !important;
    color: #44403C !important;
    border: 1px solid #E2DEC6 !important;
    font-weight: 500 !important;
    font-size: 0.88rem !important;
    padding: 0.6rem 1.4rem !important;
    transition: all 0.2s ease !important;
}
button[data-testid="baseButton-secondary"] *, 
button[kind="secondary"] * {
    color: #44403C !important;
}
button[data-testid="baseButton-secondary"]:hover, 
button[kind="secondary"]:hover {
    background-color: #111111 !important;
    border-color: #111111 !important;
    color: #FFFFFF !important;
    transform: translateY(-1px);
}
button[data-testid="baseButton-secondary"]:hover *, 
button[kind="secondary"]:hover * {
    color: #FFFFFF !important;
}

/* 5. VSTUPNÍ POLA (PŮVODNÍ BARVY + FOCUS EFEKT) */
.stTextInput input, .stTextArea textarea, div[data-baseweb="select"] > div { 
    font-family: 'Montserrat', sans-serif !important; 
    border-radius: 12px !important; 
    border: 1px solid #E2DEC6 !important; 
    background-color: #F2EFE9 !important; 
    color: #0F172A !important; 
    font-size: 0.92rem !important; 
    padding: 0.65rem 0.9rem !important; 
    transition: all 0.2s ease !important;
}
.stTextInput input:focus, .stTextArea textarea:focus, div[data-baseweb="select"] > div:focus {
    border-color: #111111 !important;
    background-color: #FFFFFF !important;
    box-shadow: 0 0 0 3px rgba(17, 17, 17, 0.1) !important;
}

/* 6. BOČNÍ PANEL (SIDEBAR) */
section[data-testid="stSidebar"] { 
    background-color: #F3F0E9 !important; 
    border-right: 1px solid #E5E0D8 !important; 
}
.sidebar-section-title { 
    font-size: 0.72rem; 
    font-weight: 700; 
    color: #78716C; 
    text-transform: uppercase; 
    letter-spacing: 0.08em; 
    margin-top: 1.4rem; 
    margin-bottom: 0.6rem; 
}

/* 7. TVOJE PŮVODNÍ BAREVNÉ BOXY */
.box-blue { 
    background-color: #F4F7F9 !important; 
    border-left: 3px solid #8AA2B6 !important; 
    padding: 1.1rem 1.3rem; 
    border-radius: 0 12px 12px 0; 
    margin: 1rem 0; 
    color: #2C3E50 !important; 
    font-size: 0.93rem; 
}
.box-yellow { 
    background-color: #FAF7EE !important; 
    border-left: 3px solid #D8C397 !important; 
    padding: 1.1rem 1.3rem; 
    border-radius: 0 12px 12px 0; 
    margin: 1rem 0; 
    color: #5C4E31 !important; 
    font-size: 0.93rem; 
}
.box-purple { 
    background-color: #F8F5F8 !important; 
    border-left: 3px solid #B4A2B8 !important; 
    padding: 1.1rem 1.3rem; 
    border-radius: 0 12px 12px 0; 
    margin: 1rem 0; 
    color: #4A3B4E !important; 
    font-size: 0.93rem; 
    word-wrap: break-word; 
}
.box-green { 
    background-color: #F3F6F3 !important; 
    border-left: 3px solid #8DAE93 !important; 
    padding: 1.1rem 1.3rem; 
    border-radius: 0 12px 12px 0; 
    margin: 1rem 0; 
    color: #2A4231 !important; 
    font-size: 0.93rem; 
}
.box-red { 
    background-color: #FAF3F3 !important; 
    border-left: 3px solid #C98A8A !important; 
    padding: 1.1rem 1.3rem; 
    border-radius: 0 12px 12px 0; 
    margin: 1rem 0; 
    color: #5C2E2E !important; 
    font-size: 0.93rem; 
}
.box-gray { 
    background-color: #F2EFE9 !important; 
    border-left: 3px solid #A8A29E !important; 
    padding: 1.1rem 1.3rem; 
    border-radius: 0 12px 12px 0; 
    margin: 1rem 0; 
    color: #44403C !important; 
    font-size: 0.93rem; 
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
            <span style='font-size: 0.7rem; font-weight: 700; color: #44403C; text-transform: uppercase; letter-spacing: 0.08em;'>E-Learning Portal</span>
            <h2 style='margin: 0; padding: 0; border: none; font-size: 1.25rem; color: #0F172A; font-weight: 800;'>Učebnice Ekonomiky</h2>
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
