import json
import math
import unicodedata
import gspread
from kapitoly import (
    kapitola1,
    kapitola2,
    kapitola3,
    kapitola4,
    kapitola5,
    kapitola6,
)
import pandas as pd
import requests
import streamlit as st
from supabase import Client, create_client
import yfinance as yf

# =========================================================================
# 1. KONFIGURACE STRÁNKY & INICIALIZACE STAVU
# =========================================================================
st.set_page_config(
    page_title="Učebnice ekonomiky", page_icon="📖", layout="wide"
)

# Inicializace výchozích proměnných v paměti relace
if "is_logged_in" not in st.session_state:
    st.session_state["is_logged_in"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""
if "user_name" not in st.session_state:
    st.session_state["user_name"] = "Uživatel"
if "user_role" not in st.session_state:
    st.session_state["user_role"] = "student"
if "user_class" not in st.session_state:
    st.session_state["user_class"] = ""
if "current_view" not in st.session_state:
    st.session_state["current_view"] = "Uvod"
if "dyslexic_mode" not in st.session_state:
    st.session_state["dyslexic_mode"] = False

# Výchozí metriky pro známkování učitele
if "hranice_1" not in st.session_state:
    st.session_state["hranice_1"] = 90
if "hranice_2" not in st.session_state:
    st.session_state["hranice_2"] = 75
if "hranice_3" not in st.session_state:
    st.session_state["hranice_3"] = 60
if "hranice_4" not in st.session_state:
    st.session_state["hranice_4"] = 45

# Konstanta pro počet úkolů v kapitolách
CELKEM_UKOLU = {
    "Kapitola 1": 15,
    "Kapitola 2": 11,
    "Kapitola 3": 12,
    "Kapitola 4": 15,
    "Kapitola 5": 14,
    "Kapitola 6": 21,
}

# =========================================================================
# 2. POMOCNÉ FUNKCE A DATABÁZE SUPABASE & GOOGLE SHEETS
# =========================================================================
def ocisti_username(text: str) -> str:
    """Odstraní diakritiku a převede text na malá písmena pro bezpečný dotaz do DB."""
    if not text:
        return ""
    text = unicodedata.normalize("NFD", text)
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    return text.strip().lower()


@st.cache_resource
def init_supabase() -> Client:
    url = st.secrets["connections"]["supabase"]["SUPABASE_URL"]
    key = st.secrets["connections"]["supabase"]["SUPABASE_KEY"]
    return create_client(url, key)

supabase = init_supabase()


@st.cache_resource(ttl=60)
def init_gspread():
    raw_creds = st.secrets["google_credentials"]
    tajemstvi = (
        json.loads(raw_creds) if isinstance(raw_creds, str) else dict(raw_creds)
    )
    if "private_key" in tajemstvi:
        tajemstvi["private_key"] = (
            tajemstvi["private_key"]
            .replace("\\n", "\n")
            .replace("\r", "")
            .strip()
        )
    return gspread.service_account_from_dict(tajemstvi)


def get_user_level(total_answers: int):
    """Vypočítá herní level a XP body studenta."""
    xp = total_answers * 100
    if xp < 400:
        return 1, "Nováček 🥉", xp, 400
    elif xp < 900:
        return 2, "Junior Analytik 🥈", xp, 900
    elif xp < 1500:
        return 3, "Manažer Projektu 🥇", xp, 1500
    elif xp < 2500:
        return 4, "Finanční Žralok 💎", xp, 2500
    else:
        return 5, "CEO & Investor 👑", xp, 3500


def ai_tutor_chat(otazka_zaka: str, aktualni_kapitola: str):
    """Zavolá OpenAI API pro plovoucího Eko-Parťáka s kontextem aktuální kapitoly."""
    try:
        api_key = st.secrets.get("OPENAI_API_KEY", "")
        if api_key:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"
            }
            system_prompt = (
                f"Jsi Eko-Parťák, přátelský, chytrý a vtipný AI tutor pro studenty středních škol. "
                f"Student se právě nachází v modulu: '{aktualni_kapitola}'. "
                "Odpovídej stručně (max 3-4 věty), polopaticky, srozumitelně s praktickými přirovnáními ze života teenagerů. "
                "Nikdy nepiš složité teoretické poučky, pokud je nevysvětlíš na příkladu z praxe."
            )
            payload = {
                "model": "gpt-4o-mini",
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": otazka_zaka}
                ],
                "temperature": 0.7,
                "max_tokens": 300
            }
            res = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload, timeout=8)
            if res.status_code == 200:
                return res.json()["choices"][0]["message"]["content"]
    except Exception:
        pass
    return "Skvělá otázka! Zkus se na to podívat přes selský rozum: každé rozhodnutí v ekonomice má své náklady a přínosy. Když si vybereš jednu možnost, vzdáváš se jiné (náklad příležitosti)."


def ai_analyza_tridy(nazev_tridy: str, data_odpovedi: list, celkem_ukolu_map: dict):
    """Generuje didaktickou AI diagnostiku pro učitele na základě anonymizovaných dat třídy."""
    try:
        api_key = st.secrets.get("OPENAI_API_KEY", "")
        if api_key:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"
            }
            souhrn_kapitol = {}
            for item in data_odpovedi:
                kap = item.get("kapitola", "Ostatní")
                souhrn_kapitol[kap] = souhrn_kapitol.get(kap, 0) + 1

            prompt_text = (
                f"Jsi expertní pedagogický metodik a AI asistent učitele ekonomiky na střední škole. "
                f"Zde jsou anonymizovaná souhrnná data o aktivitě třídy '{nazev_tridy}':\n"
                f"Počty splněných úkolů podle kapitol: {json.dumps(souhrn_kapitol, ensure_ascii=False)}\n"
                f"Celkové normy úkolů na kapitoly: {json.dumps(celkem_ukolu_map, ensure_ascii=False)}\n\n"
                "Vypracuj pro vyučujícího strukturovanou bleskovou pedagogickou diagnostiku třídy:\n"
                "1. 🎯 Shrnutí aktuálního zvládnutí učiva a celkové dynamiky třídy.\n"
                "2. ⚠️ Slabá místa a témata, která třída zatím zanedbává nebo kde hrozí nepochopení.\n"
                "3. 💡 2-3 konkrétní didaktická doporučení do příští vyučovací hodiny (aktivity, diskuze).\n"
                "4. 🧑‍🎓 Doporučení pro práci s pomalejšími a nadanými žáky.\n"
                "Piš věcně, profesionálně a didakticky podnětně."
            )
            payload = {
                "model": "gpt-4o-mini",
                "messages": [
                    {"role": "system", "content": "Jsi didaktický poradce pro výuku ekonomických předmětů."},
                    {"role": "user", "content": prompt_text}
                ],
                "temperature": 0.6,
                "max_tokens": 800
            }
            res = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload, timeout=12)
            if res.status_code == 200:
                return res.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Analýzu se nepodařilo vygenerovat: {e}"
    return "Analýza není momentálně dostupná. Zkontrolujte připojení k internetu a API klíč."

# --- 🔄 AUTO-LOGIN PO OBNOVENÍ STRÁNKY (F5) PŘES URL QUERY PARAMS ---
if not st.session_state.get("is_logged_in"):
    saved_user = st.query_params.get("user")
    if saved_user:
        ciste_jmeno = ocisti_username(saved_user)
        try:
            res_auto = (
                supabase.table("uzivatele")
                .select("*")
                .eq("username", ciste_jmeno)
                .execute()
            )
            if res_auto.data:
                user_auto = res_auto.data[0]
                st.session_state["is_logged_in"] = True
                st.session_state["username"] = user_auto.get("username")
                st.session_state["user_role"] = user_auto.get("role", "student")
                st.session_state["user_name"] = (
                    user_auto.get("jmeno")
                    or user_auto.get("username")
                    or "Uživatel"
                )
                st.session_state["user_class"] = user_auto.get("trida", "")

                saved_view = st.query_params.get("view")
                if saved_view:
                    st.session_state["current_view"] = saved_view
        except Exception:
            pass


# --- FUNKCE PRO VYKRESLENÍ A ZÁPIS OTÁZKY V KAPITOLÁCH ---
def vykresli_otazku(otazka_id, text_otazky, kapitola_id, ulozene_odpovedi):
    st.markdown(f"**{text_otazky}**")
    staved_text = ulozene_odpovedi.get(otazka_id, "")

    if staved_text:
        st.success("✅ **Tento úkol už máš splněný!** (Můžeš ho níže upravit)")
    else:
        st.info("💡 **Tento úkol zatím nemáš vyplněný.** (+100 XP)")

    odpoved_zaka = st.text_area(
        "Tvoje odpověď:", value=staved_text, key=f"in_{otazka_id}"
    )

    if st.button("Uložit odpověď 💾", key=f"btn_{otazka_id}"):
        if not odpoved_zaka.strip():
            st.warning("Před uložením nejprve napiš odpověď!")
            return

        nazev_kapitoly = (
            f"Kapitola {kapitola_id}"
            if not str(kapitola_id).startswith("Kapitola")
            else kapitola_id
        )

        try:
            supabase.table("odpovedi").upsert({
                "username": st.session_state.get("username", "demo.zak"),
                "kapitola": nazev_kapitoly,
                "otazka_id": otazka_id,
                "odpoved": odpoved_zaka,
            }).execute()

            if "ulozene_odpovedi" not in st.session_state:
                st.session_state["ulozene_odpovedi"] = {}
            st.session_state["ulozene_odpovedi"][otazka_id] = odpoved_zaka

            st.balloons()
            st.toast("Odpověď uložena! Získáváš +100 XP 🎯", icon="🎉")
            st.rerun()
        except Exception as e:
            st.error(f"Chyba při zápisu do databáze: {e}")


st.session_state["vykresli_otazku_fn"] = vykresli_otazku


def uloz_odpoved(kapitola: str, otazka_id: str, odpoved_text: str):
    username = st.session_state.get("username")
    if not username:
        return

    try:
        existing = (
            supabase.table("odpovedi")
            .select("username")
            .eq("username", username)
            .eq("kapitola", kapitola)
            .eq("otazka_id", otazka_id)
            .execute()
        )

        if existing.data:
            supabase.table("odpovedi").update({"odpoved": odpoved_text}).eq(
                "username", username
            ).eq("kapitola", kapitola).eq("otazka_id", otazka_id).execute()
        else:
            new_record = {
                "username": username,
                "kapitola": kapitola,
                "otazka_id": otazka_id,
                "odpoved": odpoved_text,
            }
            supabase.table("odpovedi").insert(new_record).execute()
            st.balloons()
        st.toast("✅ Odpověď byla uložena!", icon="💾")
    except Exception as e:
        st.error(f"Chyba při ukládání odpovědi: {e}")


st.session_state["uloz_odpoved_fn"] = uloz_odpoved


# =========================================================================
# 4. GLOBÁLNÍ DESIGN, ACCESSIBILITY & PLOVOUCÍ AI WIDGET
# =========================================================================
font_family = "'OpenDyslexic', sans-serif" if st.session_state.get("dyslexic_mode") else "'Montserrat', -apple-system, sans-serif"
letter_spacing = "0.08em" if st.session_state.get("dyslexic_mode") else "-0.01em"
line_height = "1.9" if st.session_state.get("dyslexic_mode") else "1.7"

dynamic_css = f"""
html, body, [class*="css"], .stApp {{ 
    font-family: {font_family} !important; 
    letter-spacing: {letter_spacing} !important;
}}
p, li, td, th, .stMarkdown p {{ 
    font-family: {font_family} !important; 
    line-height: {line_height} !important; 
}}
h1, h2, h3, h4, h5, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5 {{
    font-family: {font_family} !important; 
}}
"""

static_css = """
@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&display=swap');
@import url('https://fonts.cdnfonts.com/css/opendyslexic');

[data-testid="stSidebarNav"] { display: none !important; }

html, body, [class*="css"], .stApp { background-color: #FAF8F5 !important; color: #1C1917 !important; }

.main .block-container { max-width: 920px !important; padding-top: 2.5rem !important; padding-bottom: 5rem !important; }

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

h1, .stMarkdown h1 { color: #0F172A !important; font-weight: 800 !important; font-size: 2.2rem !important; letter-spacing: -0.03em !important; line-height: 1.25 !important; margin-bottom: 0.75rem !important; }
h2, .stMarkdown h2 { color: #0F172A !important; font-weight: 800 !important; font-size: 1.75rem !important; letter-spacing: -0.02em !important; margin-top: 2rem !important; margin-bottom: 0.75rem !important; border-bottom: 1px solid #E2E8F0 !important; padding-bottom: 0.4rem !important; }
h3, .stMarkdown h3 { color: #0F172A !important; font-weight: 700 !important; font-size: 1.4rem !important; margin-top: 1.5rem !important; margin-bottom: 0.5rem !important; }
h4, .stMarkdown h4 { color: #1E293B !important; font-weight: 600 !important; font-size: 1.15rem !important; margin-top: 1.2rem !important; margin-bottom: 0.4rem !important; }
h5, .stMarkdown h5 { color: #334155 !important; font-weight: 600 !important; font-size: 1.0rem !important; margin-top: 0.8rem !important; margin-bottom: 0.3rem !important; }
p, li, td, th, .stMarkdown p { color: #334155 !important; font-size: 0.95rem !important; font-weight: 400 !important; }

button[data-testid="baseButton-primary"], button[kind="primary"] { font-family: 'Montserrat', sans-serif !important; border-radius: 9999px !important; border: 1px solid #111111 !important; background-color: #111111 !important; color: #FFFFFF !important; font-weight: 600 !important; font-size: 0.88rem !important; padding: 0.6rem 1.4rem !important; box-shadow: 0 4px 10px rgba(17, 17, 17, 0.15) !important; transition: all 0.2s ease !important; }
button[data-testid="baseButton-primary"]:hover, button[kind="primary"]:hover { transform: translateY(-1px); box-shadow: 0 6px 14px rgba(17, 17, 17, 0.25) !important; }
button[data-testid="baseButton-primary"] *, button[kind="primary"] * { color: #FFFFFF !important; }

button[data-testid="baseButton-secondary"], button[kind="secondary"] { font-family: 'Montserrat', sans-serif !important; border-radius: 9999px !important; background-color: #F2EFE9 !important; color: #44403C !important; border: 1px solid #E2DEC6 !important; font-weight: 500 !important; font-size: 0.88rem !important; padding: 0.6rem 1.4rem !important; transition: all 0.2s ease !important; }
button[data-testid="baseButton-secondary"]:hover, button[kind="secondary"]:hover { background-color: #111111 !important; border-color: #111111 !important; color: #FFFFFF !important; transform: translateY(-1px); }
button[data-testid="baseButton-secondary"] *, button[kind="secondary"] * { color: #44403C !important; }
button[data-testid="baseButton-secondary"]:hover *, button[kind="secondary"]:hover * { color: #FFFFFF !important; }

.stTextInput input, .stTextArea textarea, div[data-baseweb="select"] > div { font-family: 'Montserrat', sans-serif !important; border-radius: 12px !important; border: 1px solid #E2DEC6 !important; background-color: #F2EFE9 !important; color: #0F172A !important; font-size: 0.92rem !important; padding: 0.65rem 0.9rem !important; transition: all 0.2s ease !important; }
.stTextInput input:focus, .stTextArea textarea:focus, div[data-baseweb="select"] > div:focus { border-color: #111111 !important; background-color: #FFFFFF !important; box-shadow: 0 0 0 3px rgba(17, 17, 17, 0.1) !important; }

section[data-testid="stSidebar"] { background-color: #FAF8F5 !important; border-right: 1px solid #E5E0D8 !important; }
.sidebar-section-title { font-size: 0.72rem; font-weight: 700; color: #78716C; text-transform: uppercase; letter-spacing: 0.08em; margin-top: 1.4rem; margin-bottom: 0.6rem; }

.box-blue { background-color: #F4F7F9 !important; border-left: 3px solid #8AA2B6 !important; padding: 1.1rem 1.3rem; border-radius: 0 12px 12px 0; margin: 1rem 0; color: #2C3E50 !important; font-size: 0.93rem; }
.box-yellow { background-color: #FAF7EE !important; border-left: 3px solid #D8C397 !important; padding: 1.1rem 1.3rem; border-radius: 0 12px 12px 0; margin: 1rem 0; color: #5C4E31 !important; font-size: 0.93rem; }
.box-purple { background-color: #F8F5F8 !important; border-left: 3px solid #B4A2B8 !important; padding: 1.1rem 1.3rem; border-radius: 0 12px 12px 0; color: #4A3B4E !important; font-size: 0.93rem; word-wrap: break-word; }
.box-green { background-color: #F3F6F3 !important; border-left: 3px solid #8DAE93 !important; padding: 1.1rem 1.3rem; border-radius: 0 12px 12px 0; margin: 1rem 0; color: #2A4231 !important; font-size: 0.93rem; }
.box-red { background-color: #FAF3F3 !important; border-left: 3px solid #C98A8A !important; padding: 1.1rem 1.3rem; border-radius: 0 12px 12px 0; margin: 1rem 0; color: #5C2E2E !important; font-size: 0.93rem; }
.box-gray { background-color: #F2EFE9 !important; border-left: 3px solid #A8A29E !important; padding: 1.1rem 1.3rem; border-radius: 0 12px 12px 0; margin: 1rem 0; color: #44403C !important; font-size: 0.93rem; }

/* 🌟 SKUTEČNĚ PLOVOUCÍ AI TUTOR V PRAVÉM DOLNÍM ROHU 🌟 */
div[data-testid="stPopover"] {
    position: fixed !important;
    bottom: 25px !important;
    right: 25px !important;
    z-index: 999999 !important;
}
div[data-testid="stPopover"] > button {
    background: linear-gradient(135deg, #4f46e5, #7c3aed) !important;
    color: #ffffff !important;
    border-radius: 16px !important;
    width: 65px !important;
    height: 65px !important;
    padding: 0 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    box-shadow: 0 8px 25px rgba(124, 58, 237, 0.4) !important;
    border: 2px solid #ffffff !important;
    font-size: 1.8rem !important;
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
}
div[data-testid="stPopover"] > button:hover {
    transform: scale(1.1) translateY(-4px) !important;
    box-shadow: 0 15px 35px rgba(124, 58, 237, 0.6) !important;
}
div[data-testid="stPopoverBody"] {
    width: 320px !important;
    padding: 1.5rem !important;
    border-radius: 16px !important;
    border: 1px solid #EAE7DC !important;
    box-shadow: 0 10px 40px rgba(0,0,0,0.1) !important;
}
"""

st.markdown(f"<style>{static_css} {dynamic_css}</style>", unsafe_allow_html=True)


# =========================================================================
# 5. PŘIHLAŠOVACÍ A REGISTRAČNÍ BRÁNA
# =========================================================================
def login_screen():
    if st.session_state.get("is_logged_in", False):
        return True

    col1, col2, col3 = st.columns([1, 1.8, 1])
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown(
                "<h2 style='text-align: center; border: none; font-weight: 800;"
                " margin-bottom: 0;'>Učebnice ekonomiky</h2>",
                unsafe_allow_html=True,
            )

            tab_login, tab_reg = st.tabs(["🔑 Přihlášení", "📝 Registrace žáka"])

            with tab_login:
                with st.form("login_form", border=False):
                    username_input = st.text_input("Uživatelské jméno:", placeholder="Zadejte uživatelské jméno...")
                    password_input = st.text_input("Heslo:", type="password", placeholder="Vaše heslo...")
                    submit = st.form_submit_button("Vstoupit do učebnice", use_container_width=True)

                    if submit:
                        try:
                            ciste_jmeno = ocisti_username(username_input)
                            res = supabase.table("uzivatele").select("*").eq("username", ciste_jmeno).execute()
                            if res.data:
                                user = res.data[0]
                                if str(user.get("password")) == password_input:
                                    st.session_state["is_logged_in"] = True
                                    st.session_state["username"] = user.get("username")
                                    st.session_state["user_role"] = user.get("role", "student")
                                    st.session_state["user_name"] = user.get("jmeno") or user.get("username") or "Uživatel"
                                    st.session_state["user_class"] = user.get("trida", "")

                                    st.query_params["user"] = user.get("username")
                                    st.query_params["view"] = st.session_state.get("current_view", "Uvod")
                                    st.rerun()
                                else:
                                    st.error("Nesprávné heslo!")
                            else:
                                st.error("Uživatel s tímto jménem neexistuje!")
                        except Exception as e:
                            st.error(f"Chyba při připojování: {e}")

            with tab_reg:
                with st.form("reg_form", border=False):
                    reg_jmeno = st.text_input("Jméno a příjmení:", placeholder="Jan Novák")
                    reg_username = st.text_input("Zvolte uživatelské jméno:", placeholder="jan.novak")
                    reg_password = st.text_input("Zvolte heslo:", type="password")
                    reg_code = st.text_input("Zvací kód třídy od učitele:", placeholder="např. EKO3A")
                    btn_reg = st.form_submit_button("Vytvořit žákovský účet 🚀", use_container_width=True)

                    if btn_reg:
                        if not (reg_jmeno and reg_username and reg_password and reg_code):
                            st.warning("Vyplňte prosím všechna pole!")
                        else:
                            try:
                                trida_res = supabase.table("tridy").select("*").eq("kod_tridy", reg_code.strip().upper()).execute()
                                if not trida_res.data:
                                    st.error("Zadaný kód třídy neexistuje! Požádejte učitele o správný kód.")
                                else:
                                    nazev_tridy = trida_res.data[0]["nazev_tridy"]
                                    ciste_reg_username = ocisti_username(reg_username)
                                    user_check = supabase.table("uzivatele").select("username").eq("username", ciste_reg_username).execute()

                                    if user_check.data:
                                        st.error("Toto uživatelské jméno je již zabrané. Zvolte jiné.")
                                    else:
                                        new_user = {
                                            "username": ciste_reg_username,
                                            "password": reg_password,
                                            "jmeno": reg_jmeno.strip(),
                                            "role": "student",
                                            "trida": nazev_tridy,
                                        }
                                        supabase.table("uzivatele").insert(new_user).execute()
                                        st.success("Účet byl úspěšně vytvořen! Nyní se můžete přihlásit.")
                            except Exception as e:
                                st.error(f"Chyba při registraci: {e}")
    return False

if not login_screen():
    st.stop()


# =========================================================================
# 6. BOČNÍ NAVIGAČNÍ PANEL (SIDEBAR)
# =========================================================================
with st.sidebar:
    st.markdown(
        f"""
        <div style='padding: 0.5rem 0;'>
            <span style='font-size: 0.72rem; font-weight: 800; color: #78716C; text-transform: uppercase;'>E-Learning Portal</span>
            <h2 style='margin: 0; padding: 0; border: none; font-size: 1.25rem; color: #0F172A; font-weight: 800;'>Učebnice Ekonomiky</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 🎮 WIDGET GAMIFIKACE PRO ŽÁKA
    if st.session_state.get("user_role") == "student":
        try:
            res_cnt = supabase.table("odpovedi").select("id", count="exact").eq("username", st.session_state["username"]).execute()
            pocet_odp = res_cnt.count if res_cnt.count is not None else 0
        except Exception:
            pocet_odp = 0

        lvl, titul, current_xp, next_xp = get_user_level(pocet_odp)
        prog = min(current_xp / next_xp, 1.0)

        st.markdown(
            f"""
            <div style='background: linear-gradient(135deg, #1e293b, #0f172a); padding: 1rem; border-radius: 14px; margin-bottom: 0.5rem; color: #ffffff;'>
                <div style='font-size: 0.72rem; color: #94a3b8; font-weight: 700; text-transform: uppercase;'>Tvůj herní status</div>
                <div style='font-size: 1.1rem; font-weight: 800; color: #38bdf8; margin: 2px 0;'>Level {lvl}: {titul}</div>
                <div style='font-size: 0.8rem; color: #cbd5e1;'>✨ <b>{current_xp} XP</b> / {next_xp} XP</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.progress(prog)
    else:
        st.markdown(
            f"""
            <div style='background-color: #F2EFE9; padding: 0.8rem; border-radius: 12px; margin-bottom: 0.5rem; border: 1px solid #EAE7DC;'>
                <div style='font-size: 0.75rem; color: #78716C; font-weight: 600;'>PŘIHLÁŠEN(A):</div>
                <div style='font-size: 0.95rem; font-weight: 700; color: #1C1917;'>👤 {st.session_state.get('user_name', 'Uživatel')}</div>
                <div style='font-size: 0.8rem; color: #44403C;'>Role: Učitel / Správce</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ♿ ACCESSIBILITY / DYSLEXICKÝ PŘEPÍNAČ
    dys_val = st.toggle("📖 Režim pro dyslektiky (SPU)", value=st.session_state.get("dyslexic_mode", False), help="Aktivuje speciální font OpenDyslexic a zvětšené řádkování.")
    if dys_val != st.session_state.get("dyslexic_mode", False):
        st.session_state["dyslexic_mode"] = dys_val
        st.rerun()

    # Učitelský panel jen pro učitele
    if st.session_state.get("user_role") == "teacher":
        st.markdown("<div class='sidebar-section-title'>👩‍🏫 UČITELSKÝ PANEL</div>", unsafe_allow_html=True)
        if st.button("📊 Správa tříd a odpovědí", use_container_width=True, type="primary" if st.session_state["current_view"] == "Ucitel_Panel" else "secondary"):
            st.session_state["current_view"] = "Ucitel_Panel"
            st.query_params["view"] = "Ucitel_Panel"
            st.rerun()
        if st.button("📂 Materiály a testy", use_container_width=True, type="primary" if st.session_state["current_view"] == "Ucitel_Materialy" else "secondary"):
            st.session_state["current_view"] = "Ucitel_Materialy"
            st.query_params["view"] = "Ucitel_Materialy"
            st.rerun()
        st.divider()

    st.markdown("<div class='sidebar-section-title'>PŘEHLED A ŽÁK</div>", unsafe_allow_html=True)

    if st.button("Úvodní stránka 🏠", use_container_width=True, type="primary" if st.session_state["current_view"] == "Uvod" else "secondary"):
        st.session_state["current_view"] = "Uvod"
        st.query_params["view"] = "Uvod"
        st.rerun()

    if st.button("Můj profil & Úkoly 📝", use_container_width=True, type="primary" if st.session_state["current_view"] == "Moje_Odpovedi" else "secondary"):
        st.session_state["current_view"] = "Moje_Odpovedi"
        st.query_params["view"] = "Moje_Odpovedi"
        st.rerun()

    st.markdown("<div class='sidebar-section-title'>KAPITOLY KURZU</div>", unsafe_allow_html=True)

    username_aktualni = st.session_state.get("username", "").lower()

    if "nakladatel" in username_aktualni or "demo" in username_aktualni:
        chapters = {
            "Kapitola 1": "1. Podnikavost a startupy",
            "Kapitola 2": "2. Finance a osobní management",
        }
    else:
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
        if st.button(title, key=f"nav_{key}", use_container_width=True, type="primary" if is_active else "secondary"):
            st.session_state["current_view"] = key
            st.query_params["view"] = key
            st.rerun()

    st.divider()
    if st.button("Odhlásit se 🚪", use_container_width=True):
        st.session_state.clear()
        st.query_params.clear()
        st.rerun()


# =========================================================================
# 7. ROUTING A STRÁNKY APLIKACE (MAIN VIEWS)
# =========================================================================

def zakovsky_panel():
    st.title("👨‍🎓 Můj žákovský profil")

    username = st.session_state.get("username")
    if not username:
        st.warning("Nejprve se prosím přihlaste.")
        return

    tab_ukoly, tab_gamifikace, tab_investice = st.tabs(
        ["📝 Moje úkoly z učebnice", "🏆 Herní odznaky a Level", "📈 Můj investiční profil"]
    )

    try:
        res = supabase.table("odpovedi").select("*").eq("username", username).execute()
        odpovedi_data = res.data if res.data else []
    except Exception:
        odpovedi_data = []

    lvl, titul, current_xp, next_xp = get_user_level(len(odpovedi_data))

    with tab_gamifikace:
        st.markdown(f"### 🎖️ Tvůj aktuální status: **Level {lvl} — {titul}**")
        st.write(f"Celkem máš **{current_xp} XP bodů**. Každý vyřešený úkol ti přináší **+100 XP**.")
        
        progress_xp = min(current_xp / next_xp, 1.0)
        st.progress(progress_xp, text=f"Postup do další úrovně: {current_xp} / {next_xp} XP")
        
        st.divider()
        st.markdown("#### 🏅 Odemčené odznaky úspěchu")
        
        c_bad1, c_bad2, c_bad3, c_bad4 = st.columns(4)
        has_k1 = any(o.get("kapitola") in ["Kapitola 1", "1"] for o in odpovedi_data)
        has_k2 = any(o.get("kapitola") in ["Kapitola 2", "2"] for o in odpovedi_data)
        has_k3 = any(o.get("kapitola") in ["Kapitola 3", "3"] for o in odpovedi_data)
        has_k4 = any(o.get("kapitola") in ["Kapitola 4", "4"] for o in odpovedi_data)

        if has_k1:
            c_bad1.success("🚀 **Zakladatel Startupů**\n\n(Aktivita v Kap. 1)")
        else:
            c_bad1.info("🔒 *Zamčeno*\n\n(Splň úkol v Kap. 1)")

        if has_k2:
            c_bad2.success("💰 **Finanční Guru**\n\n(Aktivita v Kap. 2)")
        else:
            c_bad2.info("🔒 *Zamčeno*\n\n(Splň úkol v Kap. 2)")

        if has_k3:
            c_bad3.success("⚙️ **Mistr Efektivity**\n\n(Aktivita v Kap. 3)")
        else:
            c_bad3.info("🔒 *Zamčeno*\n\n(Splň úkol v Kap. 3)")

        if has_k4:
            c_bad4.success("👔 **Vyjednavač Smluv**\n\n(Aktivita v Kap. 4)")
        else:
            c_bad4.info("🔒 *Zamčeno*\n\n(Splň úkol v Kap. 4)")

    with tab_ukoly:
        st.write("Zde vidíš všechny své uložené odpovědi napříč celou učebnicí. Můžeš sledovat svůj pokrok a odpovědi upravovat.")

        if not odpovedi_data:
            st.info("💡 **Zatím nemáš uložené žádné odpovědi.** Otevři kapitolu, vyplň úkol a klikni na *Uložit odpověď*.")
        else:
            kapitoly_dict = {}
            for row in odpovedi_data:
                kap = row.get("kapitola", "Ostatní")
                if kap not in kapitoly_dict:
                    kapitoly_dict[kap] = []
                kapitoly_dict[kap].append(row)

            col_m1, col_m2 = st.columns(2)
            col_m1.metric("Vyplněných úkolů celkem", f"{len(odpovedi_data)} ks")
            col_m2.metric("Rozpracovaných kapitol", len(kapitoly_dict))
            st.divider()

            for kap_nazev in sorted(kapitoly_dict.keys()):
                slozene_odpovedi = kapitoly_dict[kap_nazev]
                hotovo = len(slozene_odpovedi)
                celkem = CELKEM_UKOLU.get(kap_nazev, hotovo)
                procento_cislo = min((hotovo / celkem), 1.0) if celkem > 0 else 1.0
                procento_zobrazeni = int(procento_cislo * 100)

                with st.expander(f"📚 {kap_nazev} ({hotovo}/{celkem} úkolů) — {procento_zobrazeni} %", expanded=False):
                    st.progress(procento_cislo, text=f"Stav: {hotovo} z {celkem} hotovo ({procento_zobrazeni} %)")
                    st.markdown("<br>", unsafe_allow_html=True)
                    slozene_odpovedi = sorted(slozene_odpovedi, key=lambda x: str(x.get("otazka_id")))
                    
                    for row in slozene_odpovedi:
                        otazka_id = row.get("otazka_id", "Neuvedeno")
                        stare_text = row.get("odpoved", "")
                        st.markdown(f"**Úkol:** `{otazka_id}`")
                        nova_odpoved = st.text_area("Tvá odpověď:", value=stare_text, key=f"panel_in_{kap_nazev}_{otazka_id}")

                        if st.button("Uložit změnu 💾", key=f"panel_btn_{kap_nazev}_{otazka_id}"):
                            if nova_odpoved.strip():
                                try:
                                    supabase.table("odpovedi").upsert({
                                        "username": username,
                                        "kapitola": kap_nazev,
                                        "otazka_id": otazka_id,
                                        "odpoved": nova_odpoved,
                                    }).execute()
                                    if "ulozene_odpovedi" not in st.session_state:
                                        st.session_state["ulozene_odpovedi"] = {}
                                    st.session_state["ulozene_odpovedi"][otazka_id] = nova_odpoved
                                    st.toast("Odpověď byla upravena!", icon="✅")
                                    st.rerun()
                                except Exception as ex:
                                    st.error(f"Chyba při ukládání: {ex}")
                        st.markdown("---")

    with tab_investice:
        st.markdown("### 📈 Tvé investiční portfolio")
        st.write("Zde živě vidíš, jak si vedeš na burze. Pokud chceš nakupovat nebo prodávat další akcie, přejdi do obchodní aplikace.")

        muj_nick = username.strip().lower()
        url_sim = f"https://skolni-investice-jcu32nvp35ymaymjb9g2k5.streamlit.app/?user={muj_nick}&nick={muj_nick}"
        st.link_button("🚀 Přejít do investičního simulátoru (Koupit / Prodat)", url_sim, type="primary")

        st.divider()
        with st.spinner("Aktualizuji data z burzy... ⏳"):
            try:
                client = init_gspread()
                soubor = client.open("Skolni_Investice_DB")
                data_inv = soubor.sheet1.get_all_records(value_render_option="UNFORMATTED_VALUE")
                df_inv = pd.DataFrame(data_inv)
                df_zaka = df_inv[df_inv["Nick"].astype(str).str.strip().str.lower() == muj_nick]

                if not df_zaka.empty:
                    row = df_zaka.iloc[0]
                    zustatek = float(row.get("Zustatek", 0.0))

                    AKTIVA_MAP = {
                        "AAPL": ("Apple (AAPL)", "USD"), "TSLA": ("Tesla (TSLA)", "USD"),
                        "MSFT": ("Microsoft (MSFT)", "USD"), "GOOGL": ("Google (GOOGL)", "USD"),
                        "AMZN": ("Amazon (AMZN)", "USD"), "NVDA": ("Nvidia (NVDA)", "USD"),
                        "META": ("Meta (META)", "USD"), "CEZ": ("ČEZ", "CZK"),
                        "BTC": ("Bitcoin", "USD"), "ETH": ("Ethereum", "USD"),
                    }

                    try:
                        kurz_usd = yf.Ticker("CZK=X").history(period="1d")["Close"].iloc[-1]
                    except Exception:
                        kurz_usd = 23.5

                    hodnota_aktiv = 0.0
                    drzena_aktiva = {}

                    for db_col, (nazev, mena) in AKTIVA_MAP.items():
                        ks = float(row.get(db_col, 0.0))
                        if ks > 0:
                            try:
                                ticker_symbol = "CEZ.PR" if db_col == "CEZ" else ("BTC-USD" if db_col == "BTC" else ("ETH-USD" if db_col == "ETH" else db_col))
                                cena = yf.Ticker(ticker_symbol).history(period="1d")["Close"].iloc[-1]
                                cena_czk = cena * kurz_usd if mena == "USD" else cena
                            except Exception:
                                cena_czk = 0.0
                            hodnota_aktiv += ks * cena_czk
                            drzena_aktiva[nazev] = ks

                    celkovy_majetek = zustatek + hodnota_aktiv
                    zisk_ztrata = celkovy_majetek - 20000.0

                    col_met1, col_met2 = st.columns(2)
                    col_met1.metric("Celkový majetek", f"{celkovy_majetek:,.2f} Kč")
                    col_met2.metric("Čistý zisk / ztráta", f"{'+' if zisk_ztrata>0 else ''}{zisk_ztrata:,.2f} Kč")

                    col_inf1, col_inf2 = st.columns(2)
                    with col_inf1:
                        st.info(f"💵 **Volná hotovost:** `{zustatek:,.2f} Kč`")
                        st.info(f"📈 **Hodnota akcií:** `{hodnota_aktiv:,.2f} Kč`")
                    with col_inf2:
                        st.write("**Tvé aktuální portfolio:**")
                        if drzena_aktiva:
                            for aktivum, kusy in drzena_aktiva.items(): st.write(f"⚡ {aktivum}: `{kusy} ks`")
                        else:
                            st.write("Zatím nedržíš žádné akcie ani kryptoměny.")
                else:
                    st.info("Tvůj účet zatím v simulátoru nemá žádná data.")
            except Exception as e:
                st.error(f"Chyba při stahování dat z burzy: {e}")


# --- HLAVNÍ ROUTING (ZOBRAZENÍ STRÁNEK) ---

if st.session_state["current_view"] == "Uvod":
    st.title("Ekonomika, která dává smysl")

    st.markdown(
        """
    <div class="box-gray">
        📚 <b>Moderní učebnice ekonomiky pro střední školy:</b> Podnikavost, finance & ekonomika v souvislostech.
    </div>
    <div class="box-green">
        🎯 <b>Cíl učebnice & RVP</b><br>
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
    3. **Plň průběžné úkoly.** Žluté bloky slouží jako pracovní úkoly, otázky a aktivity. Každý úkol ti přináší **+100 XP bodů**!
    4. **Používej AI mentoring.** Fialové bloky obsahují prompty a v pravém dolním rohu máš kdykoliv po ruce **plovoucího Eko-Parťáka**.
    5. **Na konci kapitoly udělej reflexi.** Shrň, co už chápeš, a otestuj si znalosti v případových studiích.
    6. **Sbírej herní odznaky.** Postupuj v levelech z *Nováčka* až na *CEO & Investora*!
    """)

    st.divider()

    st.markdown("### 🧩 Legenda učebnice")
    st.markdown(
        """
    <div class="box-blue">📘 <b>Modrá:</b> Výklad, struktura, důležité vysvětlení</div>
    <div class="box-yellow">💡 <b>Žlutá:</b> Úkol, otázka, aktivita, procvičení (+100 XP)</div>
    <div class="box-purple">🤖 <b>Fialová:</b> AI mentoring a práce s asistencí</div>
    <div class="box-green">✅ <b>Zelená:</b> Praxe, doporučení, dobrý postup</div>
    <div class="box-red">⚠️ <b>Červená / Oranžová:</b> Riziko, varování, právní nebo etický problém</div>
    <div class="box-gray">📄 <b>Šedá:</b> Zdroje, ověřování, učitelské poznámky</div>
    """,
        unsafe_allow_html=True,
    )

elif st.session_state["current_view"] == "Moje_Odpovedi":
    zakovsky_panel()

elif st.session_state["current_view"] == "Ucitel_Panel":
    st.title("👩‍🏫 Učitelský panel")

    tab_tridy, tab_vysledky, tab_investice, tab_msmt = st.tabs([
        "➕ Správa a tvorba tříd",
        "📊 Odpovědi a Klasifikace",
        "📈 Výsledky ze simulátoru",
        "🏛️ MŠMT, RVP a GDPR standardy"
    ])

    with tab_tridy:
        st.markdown("### Vytvořit novou třídu")
        with st.form("nova_trida_form"):
            novy_nazev = st.text_input("Název třídy (např. 4.B - Ekonomika):")
            novy_kod = st.text_input("Zvolte Zvací kód pro žáky (např. EKO4B):")
            if st.form_submit_button("Vytvořit třídu 🚀"):
                if novy_nazev and novy_kod:
                    try:
                        kod_clean = novy_kod.strip().upper()
                        check = supabase.table("tridy").select("kod_tridy").eq("kod_tridy", kod_clean).execute()
                        if check.data:
                            st.error("Tento Zvací kód již existuje, zvolte jiný.")
                        else:
                            new_trida = {"kod_tridy": kod_clean, "nazev_tridy": novy_nazev.strip(), "ucitel_username": st.session_state["username"]}
                            supabase.table("tridy").insert(new_trida).execute()
                            st.success(f"Třída '{novy_nazev}' vytvořena! Kód pro žáky: **{kod_clean}**")
                    except Exception as e:
                        st.error(f"Chyba při vytváření třídy: {e}")
                else:
                    st.warning("Vyplňte název i kód třídy!")

        st.divider()
        st.markdown("### Vaše existující třídy")
        try:
            moje_tridy = supabase.table("tridy").select("*").eq("ucitel_username", st.session_state["username"]).execute()
            if moje_tridy.data:
                for t in moje_tridy.data:
                    st.info(f"📍 **{t['nazev_tridy']}** | Zvací kód pro žáky: `{t['kod_tridy']}`")
            else:
                st.write("Zatím jste nevytvořil(a) žádnou třídu.")
        except Exception as e:
            st.error(f"Chyba při načítání tříd: {e}")

    with tab_vysledky:
        st.markdown("### Přehled odevzdaných prací a klasifikace")

        try:
            t_res = supabase.table("tridy").select("nazev_tridy").eq("ucitel_username", st.session_state["username"]).execute()
            list_trid = [x["nazev_tridy"] for x in t_res.data] if t_res.data else []

            if list_trid:
                vybrana_t = st.selectbox("Vyberte třídu:", list_trid, key="sel_trida_uc")
                zaci_res = supabase.table("uzivatele").select("username, jmeno").eq("trida", vybrana_t).execute()

                if zaci_res.data:
                    zaci_dict = {z["jmeno"]: z["username"] for z in zaci_res.data}
                    st.markdown(f"#### 📊 Klasifikace a pokrok třídy **{vybrana_t}**")
                    
                    with st.expander("⚙️ Nastavení průběžné klasifikace (Metrika známkování)", expanded=False):
                        st.write("Nastavte procentuální hranice pro výpočet orientační průběžné známky na základě splněných úkolů z učebnice.")
                        col_z1, col_z2, col_z3, col_z4 = st.columns(4)
                        hranice_1 = col_z1.number_input("Jednička (1) od %:", value=st.session_state.get("hranice_1", 90), step=1)
                        hranice_2 = col_z2.number_input("Dvojka (2) od %:", value=st.session_state.get("hranice_2", 75), step=1)
                        hranice_3 = col_z3.number_input("Trojka (3) od %:", value=st.session_state.get("hranice_3", 60), step=1)
                        hranice_4 = col_z4.number_input("Čtyřka (4) od %:", value=st.session_state.get("hranice_4", 45), step=1)
                        if st.button("Uložit metriku známkování"):
                            st.session_state["hranice_1"] = hranice_1
                            st.session_state["hranice_2"] = hranice_2
                            st.session_state["hranice_3"] = hranice_3
                            st.session_state["hranice_4"] = hranice_4
                            st.success("Metrika uložena!")
                            st.rerun()

                    h1 = st.session_state.get("hranice_1", 90)
                    h2 = st.session_state.get("hranice_2", 75)
                    h3 = st.session_state.get("hranice_3", 60)
                    h4 = st.session_state.get("hranice_4", 45)

                    hodnocena_cast = st.selectbox(
                        "Vyberte, co chcete hodnotit a známkovat:",
                        ["Všechny kapitoly (Celoroční průměr)"] + list(CELKEM_UKOLU.keys())
                    )

                    usernames_tridy = list(zaci_dict.values())
                    vsechny_odp_res = supabase.table("odpovedi").select("username, kapitola").in_("username", usernames_tridy).execute()

                    if vsechny_odp_res.data:
                        pokrok_data = []
                        for jmeno, uname in zaci_dict.items():
                            odp_zaka = [o for o in vsechny_odp_res.data if o["username"] == uname]
                            zak_stats = {"Žák": jmeno}
                            
                            if hodnocena_cast == "Všechny kapitoly (Celoroční průměr)":
                                celkem_hotovo_zaka = 0
                                celkem_vsech_ukolu = sum(CELKEM_UKOLU.values())
                                for kap, celkem_kap in CELKEM_UKOLU.items():
                                    hotovo_kap = len([o for o in odp_zaka if o["kapitola"] == kap])
                                    celkem_hotovo_zaka += hotovo_kap
                                    zak_stats[kap] = f"{hotovo_kap} / {celkem_kap}"
                                    
                                pct = int((celkem_hotovo_zaka / celkem_vsech_ukolu) * 100) if celkem_vsech_ukolu > 0 else 0
                                zak_stats["✅ Celkem hotovo"] = f"{celkem_hotovo_zaka} úkolů"
                                zak_stats["📈 Úspěšnost"] = f"{pct} %"
                            else:
                                celkem_kap = CELKEM_UKOLU[hodnocena_cast]
                                hotovo_kap = len([o for o in odp_zaka if o["kapitola"] == hodnocena_cast])
                                pct = int((hotovo_kap / celkem_kap) * 100) if celkem_kap > 0 else 0
                                zak_stats[f"✅ Úkoly ({hodnocena_cast})"] = f"{hotovo_kap} z {celkem_kap}"
                                zak_stats["📈 Úspěšnost"] = f"{pct} %"
                            
                            if pct >= h1: znamka = "1"
                            elif pct >= h2: znamka = "2"
                            elif pct >= h3: znamka = "3"
                            elif pct >= h4: znamka = "4"
                            else: znamka = "5"
                            zak_stats["🎓 Navrhovaná známka"] = znamka
                            pokrok_data.append(zak_stats)

                        df_pokrok = pd.DataFrame(pokrok_data)
                        st.dataframe(df_pokrok, use_container_width=True, hide_index=True)

                        # EXPORT A AI ANALÝZA TŘÍDY
                        col_exp1, col_exp2 = st.columns(2)
                        df_bakalari = df_pokrok[["Žák", "📈 Úspěšnost", "🎓 Navrhovaná známka"]].copy()
                        csv_bakalari = df_bakalari.to_csv(index=False, sep=";").encode("utf-8-sig")
                        col_exp1.download_button("📥 Stáhnout známky pro Bakaláře / Škola OnLine (CSV)", data=csv_bakalari, file_name=f"klasifikace_{vybrana_t}_{hodnocena_cast}.csv", mime="text/csv", use_container_width=True)

                        if col_exp2.button("🤖 Spustit AI pedagogickou analýzu třídy", use_container_width=True, type="primary"):
                            with st.spinner("AI didaktický asistent analyzuje odpovědi a dynamiku třídy..."):
                                analyza_txt = ai_analyza_tridy(vybrana_t, vsechny_odp_res.data, CELKEM_UKOLU)
                                st.markdown("### 🧠 AI Didaktická diagnóza třídy")
                                st.info(analyza_txt)
                    else:
                        st.info("Zatím žádný žák v této třídě neodevzdal odpověď.")

                    st.divider()
                    st.markdown("#### 🔍 Detailní odpovědi konkrétního žáka")
                    vybrany_zak_jmeno = st.selectbox("Vyberte žáka pro zobrazení textů:", list(zaci_dict.keys()), key="sel_zak_uc")
                    vybrany_zak_user = zaci_dict[vybrany_zak_jmeno]

                    odpovedi_res = supabase.table("odpovedi").select("*").eq("username", vybrany_zak_user).execute()
                    if odpovedi_res.data:
                        df_export = pd.DataFrame(odpovedi_res.data)
                        povolene_sloupce = [c for c in ["username", "kapitola", "otazka_id", "odpoved"] if c in df_export.columns]
                        df_export = df_export[povolene_sloupce].rename(columns={"username": "Žák", "kapitola": "Kapitola", "otazka_id": "Úkol", "odpoved": "Odpověď"})
                        csv_data = df_export.to_csv(index=False, sep=";").encode("utf-8-sig")
                        st.download_button(label=f"📥 Stáhnout odpovědi žáka {vybrany_zak_jmeno} v CSV", data=csv_data, file_name=f"odpovedi_{vybrany_zak_user}.csv", mime="text/csv")
                        st.write("")

                        kapitoly_zaka_dict = {}
                        for o in odpovedi_res.data:
                            k = o.get("kapitola", "Ostatní")
                            if k not in kapitoly_zaka_dict: kapitoly_zaka_dict[k] = []
                            kapitoly_zaka_dict[k].append(o)

                        for kap_nazev in sorted(kapitoly_zaka_dict.keys()):
                            odp_v_kapitole = kapitoly_zaka_dict[kap_nazev]
                            hotovo = len(odp_v_kapitole)
                            celkem = CELKEM_UKOLU.get(kap_nazev, hotovo)
                            pct_cislo = min((hotovo / celkem), 1.0) if celkem > 0 else 1.0

                            with st.expander(f"📘 {kap_nazev} — splněno {hotovo}/{celkem} ({int(pct_cislo*100)} %)", expanded=False):
                                st.progress(pct_cislo)
                                st.write("")
                                for o in sorted(odp_v_kapitole, key=lambda x: str(x.get("otazka_id"))):
                                    st.markdown(f"**Úkol:** `{o['otazka_id']}`")
                                    st.info(o["odpoved"])
                                    st.write("")
                    else:
                        st.write("Tento žák zatím neodevzdal žádné odpovědi ke kontrole.")
                else:
                    st.write("V této třídě zatím nejsou zaregistrovaní žádní žáci.")
            else:
                st.write("Nejprve vytvořte třídu v záložce 'Správa a tvorba tříd'.")
        except Exception as e:
            st.error(f"Chyba při načítání výsledků: {e}")

    with tab_investice:
        st.markdown("### 🏆 Živý žebříček investic a historie obchodů")
        with st.spinner("Stahuji aktuální ceny z burzy a data ze simulátoru... ⏳"):
            try:
                t_res = supabase.table("tridy").select("nazev_tridy").eq("ucitel_username", st.session_state["username"]).execute()
                moje_tridy_seznam = [x["nazev_tridy"] for x in t_res.data] if t_res.data else []

                moje_usernames = []
                if moje_tridy_seznam:
                    zaci_res = supabase.table("uzivatele").select("username").in_("trida", moje_tridy_seznam).execute()
                    if zaci_res.data:
                        moje_usernames = [z["username"].strip().lower() for z in zaci_res.data]

                if not moje_usernames:
                    st.info("Zatím nemáte ve svých třídách žádné žáky.")
                else:
                    client = init_gspread()
                    soubor = client.open("Skolni_Investice_DB")
                    df_zaci = pd.DataFrame(soubor.sheet1.get_all_records(value_render_option="UNFORMATTED_VALUE"))
                    df_transakce = pd.DataFrame(soubor.worksheet("Transakce").get_all_records(value_render_option="UNFORMATTED_VALUE"))

                    if not df_zaci.empty:
                        df_zaci["Nick_lower"] = df_zaci["Nick"].astype(str).str.strip().str.lower()
                        df_zaci = df_zaci[df_zaci["Nick_lower"].isin(moje_usernames)]

                    if not df_zaci.empty:
                        AKTIVA_MAP = {
                            "AAPL": ("Apple", "USD"), "TSLA": ("Tesla", "USD"), "MSFT": ("Microsoft", "USD"),
                            "GOOGL": ("Google", "USD"), "AMZN": ("Amazon", "USD"), "NVDA": ("Nvidia", "USD"),
                            "META": ("Meta", "USD"), "CEZ": ("ČEZ", "CZK"), "BTC": ("Bitcoin", "USD"), "ETH": ("Ethereum", "USD"),
                        }
                        try:
                            kurz_usd = yf.Ticker("CZK=X").history(period="1d")["Close"].iloc[-1]
                        except Exception:
                            kurz_usd = 23.5

                        zive_ceny = {}
                        for db_col, (nazev, mena) in AKTIVA_MAP.items():
                            try:
                                ticker_symbol = "CEZ.PR" if db_col == "CEZ" else ("BTC-USD" if db_col == "BTC" else ("ETH-USD" if db_col == "ETH" else db_col))
                                cena = yf.Ticker(ticker_symbol).history(period="1d")["Close"].iloc[-1]
                                zive_ceny[db_col] = cena * kurz_usd if mena == "USD" else cena
                            except Exception:
                                zive_ceny[db_col] = 0.0

                        zaci_list = []
                        for index, row in df_zaci.iterrows():
                            zustatek = float(row.get("Zustatek", 0.0))
                            hodnota_aktiv = 0.0
                            drzena_aktiva = {}
                            for db_col, (nazev, mena) in AKTIVA_MAP.items():
                                ks = float(row.get(db_col, 0.0))
                                if ks > 0:
                                    hodnota_aktiv += ks * zive_ceny.get(db_col, 0.0)
                                    drzena_aktiva[nazev] = ks
                            celkovy_majetek = zustatek + hodnota_aktiv
                            zaci_list.append({
                                "Nick": str(row.get("Nick", "")),
                                "Jmeno": str(row.get("Jmeno", row.get("Nick", ""))),
                                "Zustatek": zustatek, "HodnotaAktiv": hodnota_aktiv,
                                "CelkovyMajetek": celkovy_majetek, "Zisk": celkovy_majetek - 20000.0,
                                "Portfolio": drzena_aktiva,
                            })

                        zaci_list = sorted(zaci_list, key=lambda x: x["CelkovyMajetek"], reverse=True)
                        st.markdown("#### 🥇 Žebříček mých studentů")

                        for i, zak in enumerate(zaci_list):
                            poradi = i + 1
                            medaile = "🥇" if poradi == 1 else ("🥈" if poradi == 2 else "🥉" if poradi == 3 else f"{poradi}.")
                            zisk_str = f"+{zak['Zisk']:,.2f} Kč" if zak["Zisk"] > 0 else f"{zak['Zisk']:,.2f} Kč"
                            with st.expander(f"{medaile} {zak['Jmeno']} — Majetek: {zak['CelkovyMajetek']:,.2f} Kč | Zisk: {zisk_str}"):
                                c1, c2 = st.columns(2)
                                with c1:
                                    st.info(f"💵 Volná hotovost: `{zak['Zustatek']:,.2f} Kč`\n\n📈 Hodnota akcií: `{zak['HodnotaAktiv']:,.2f} Kč`")
                                with c2:
                                    if zak["Portfolio"]:
                                        for aktivum, kusy in zak["Portfolio"].items(): st.write(f"⚡ {aktivum}: `{kusy} ks`")
                                    else:
                                        st.write("Žádné akcie.")
                                st.write("**📜 Historie obchodů:**")
                                if not df_transakce.empty:
                                    df_trans_zak = df_transakce[df_transakce["Nick"].astype(str).str.strip().str.lower() == zak["Nick"].strip().lower()]
                                    if not df_trans_zak.empty:
                                        sloupce_k_zobrazeni = [c for c in df_trans_zak.columns if c not in ["Nick", "Jmeno"]]
                                        st.dataframe(df_trans_zak[sloupce_k_zobrazeni].iloc[::-1], use_container_width=True, hide_index=True)
                    else:
                        st.info("Vaši žáci zatím nemají založené účty v simulátoru.")
            except Exception as e:
                st.error(f"Chyba při stahování dat z burzy: {e}")

    with tab_msmt:
        st.markdown("### 🏛️ Soulad s RVP, MŠMT a GDPR ochrana")
        st.markdown("""
        Tato interaktivní e-učebnice je koncipována plně v souladu s **Rámcovým vzdělávacím programem (RVP)** pro střední odborné vzdělávání a gymnázia (průřezová témata *Člověk a svět práce*, *Občan v demokratické společnosti*, *Finanční a ekonomická gramotnost*).
        """)
        
        c_rvp1, c_rvp2 = st.columns(2)
        with c_rvp1:
            st.markdown("#### 🎯 Rozvíjené klíčové kompetence (RVP)")
            st.markdown("""
            * **Kompetence k podnikavosti:** Reálné sestavování rozpočtů, kalkulace nákladů, launch merche a vyhodnocení bodu zvratu.
            * **Kompetence k řešení problémů:** Krizové trenažéry (řešení nelegálního švarcsystému, neférové výpovědi a reklamací nekvality).
            * **Digitální a AI kompetence:** Využití generativní AI k přípravě na pohovory, promptování a práce s burzovními API.
            * **Finanční gramotnost:** Pochopení čisté vs. hrubé mzdy, investiční portfolio na reálných datech a daně.
            """)
        
        with c_rvp2:
            st.markdown("#### 🛡️ GDPR & Bezpečnost AI (MŠMT Standard)")
            st.markdown("""
            * **Anonymizace dat:** AI moduly (OpenAI API) nezpracovávají žádná rodná čísla, adresy ani plná jména studentů.
            * **Minimální stopa:** Všechny dotazy pro Eko-Parťáka jsou zpracovávány bez trénování modelů na datech žáků.
            * **Inkluze a přístupnost:** Splňuje standardy přístupnosti díky integrovanému **OpenDyslexic režimu** a kontrastním prvkům.
            """)

elif st.session_state["current_view"] == "Ucitel_Materialy":
    st.title("📂 Materiály k výuce a testy")
    st.markdown(
        """
    <div class="box-gray">
        Tato sekce je viditelná <b>pouze pro přihlášené učitele</b>. 
        Najdete zde metodické podklady, prezentace, pracovní listy a testy ke všem kapitolám.
    </div>
    """,
        unsafe_allow_html=True,
    )

    tab_metodika, tab_testy = st.tabs(
        ["📄 Metodické balíčky ke kapitolám", "📝 Písemné práce a testy"]
    )

    with tab_metodika:
        vybrana_kap = st.selectbox(
            "Vyberte kapitolu učebnice:",
            [
                "Kapitola 1: Podnikavost a startupy",
                "Kapitola 2: Finance a osobní management",
                "Kapitola 3: Výroba, náklady a efektivita",
                "Kapitola 4: Zaměstnanci a trh práce",
                "Kapitola 5: Stát, daně a ekonomika",
                "Kapitola 6: Management a marketing",
            ],
        )

        st.divider()

        if vybrana_kap == "Kapitola 1: Podnikavost a startupy":
            st.markdown("### 📘 Materiály ke Kapitole 1")
            with st.container(border=True):
                st.markdown("#### 📦 Výukový modul: Influencer jako firma")
                st.markdown("""
                **Popis materiálu:**  
                Komplexní výukový balíček zaměřený na téma podnikání v digitální době. Obsahuje metodickou příručku pro vyučujícího, prezentaci pro výklad v hodině, pracovní listy a případové studie.
                """)
                try:
                    with open("Influencer - podnikání.zip", "rb") as file:
                        st.download_button("📥 Stáhnout balíček: Influencer jako firma (ZIP)", data=file, file_name="Influencer_podnikani.zip", mime="application/zip", type="primary")
                except FileNotFoundError:
                    st.warning("Soubor 'Influencer - podnikání.zip' nebyl nalezen.")
        else:
            st.info(f"Pro **{vybrana_kap}** zatím nebyly nahrány žádné metodické balíčky.")

    with tab_testy:
        st.markdown("### 📝 Návrhy písemných prací a testů")
        st.info("Testy ke stažení se připravují.")

else:
    kapitoly_map = {
        "Kapitola 1": (kapitola1, "1"),
        "Kapitola 2": (kapitola2, "2"),
        "Kapitola 3": (kapitola3, "3"),
        "Kapitola 4": (kapitola4, "4"),
        "Kapitola 5": (kapitola5, "5"),
        "Kapitola 6": (kapitola6, "6"),
    }

    if st.session_state["current_view"] in kapitoly_map:
        modul, kap_num = kapitoly_map[st.session_state["current_view"]]

        st.session_state["ulozene_odpovedi"] = {}
        if st.session_state.get("username"):
            kap_nazev = f"Kapitola {kap_num}" if not str(kap_num).startswith("Kapitola") else kap_num
            res = supabase.table("odpovedi").select("otazka_id, odpoved").eq("username", st.session_state["username"]).in_("kapitola", [kap_nazev, str(kap_num)]).execute()
            if res.data:
                st.session_state["ulozene_odpovedi"] = {row["otazka_id"]: row["odpoved"] for row in res.data}

        if hasattr(modul, "render"):
            modul.render()
        elif hasattr(modul, "show"):
            modul.show()

# =========================================================================
# 8. 💬 SKUTEČNĚ PLOVOUCÍ AI TUTOR (EKO-PARŤÁK) V PRAVÉM DOLNÍM ROHU
# =========================================================================
curr_view_name = st.session_state.get("current_view", "Obecná ekonomika")
with st.popover("💬", help="Zeptat se Eko-Parťáka"):
    st.markdown("#### 💬 Eko-Parťák")
    st.caption(f"📍 Kontext: **{curr_view_name}**")
    ai_q = st.text_input("Něco není jasné? Zeptej se:", placeholder="např. Co je to bod zvratu?", key="floating_ai_q")
    if st.button("Vysvětlit 💡", key="btn_floating_ai", use_container_width=True):
        if ai_q:
            with st.spinner("Přemýšlím..."):
                ans = ai_tutor_chat(ai_q, curr_view_name)
                st.info(ans)
