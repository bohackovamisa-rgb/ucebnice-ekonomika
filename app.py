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
    try:
        api_key = st.secrets.get("OPENAI_API_KEY", "")
        if api_key:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"
            }
            system_prompt = (
                f"Jsi Eko-Sova 🦉, moudrý, vtipný a lehce praštěný AI mentor pro studenty středních škol. "
                f"Student se právě nachází v modulu: '{aktualni_kapitola}'. "
                "Odpovídej stručně (max 3-4 věty), lidsky, energicky a s humorem, s praktickými přirovnáními ze života. "
                "Používej občas soví houkání ('Húú!'). Žádné suché poučky!"
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
    return "Húúú! 🦉 Skvělá otázka! Zkus se na to podívat jednoduše: v ekonomice nic není zadarmo. Když si vybereš jednu věc, vzdáváš se jiné (náklad obětované příležitosti)."


def ai_analyza_tridy(nazev_tridy: str, data_odpovedi: list, celkem_ukolu_map: dict):
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

st.session_state["vykresli_otazku_fn"] = vykresli_otazku
st.session_state["uloz_odpoved_fn"] = uloz_odpoved

# =========================================================================
# 3. AUTO LOGIN
# =========================================================================
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
                    user_auto.get("jmeno") or user_auto.get("username") or "Uživatel"
                )
                st.session_state["user_class"] = user_auto.get("trida", "")
                saved_view = st.query_params.get("view")
                if saved_view:
                    st.session_state["current_view"] = saved_view
        except Exception:
            pass

# =========================================================================
# 4. GLOBÁLNÍ DESIGN, ACCESSIBILITY & PLOVOUCÍ SOVA
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

/* 🦉 ANIMOVANÁ PLOVOUCÍ SOVA V ROHU 🦉 */
@keyframes floatSova {
    0% { transform: translateY(0px) rotate(0deg); }
    50% { transform: translateY(-10px) rotate(4deg); }
    100% { transform: translateY(0px) rotate(0deg); }
}

div[data-testid="stPopover"] {
    position: fixed !important;
    bottom: 30px !important;
    right: 30px !important;
    z-index: 999999 !important;
}

div[data-testid="stPopover"] > button {
    background: linear-gradient(135deg, #6366f1, #a855f7, #ec4899) !important;
    color: #ffffff !important;
    border-radius: 20px !important;
    width: 68px !important;
    height: 68px !important;
    padding: 0 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    box-shadow: 0 12px 30px rgba(168, 85, 247, 0.45) !important;
    border: 3px solid #ffffff !important;
    font-size: 2.2rem !important;
    animation: floatSova 3s ease-in-out infinite !important;
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

div[data-testid="stPopover"] > button:hover {
    transform: scale(1.15) rotate(8deg) !important;
    box-shadow: 0 18px 40px rgba(168, 85, 247, 0.7) !important;
}

div[data-testid="stPopoverBody"] {
    width: 350px !important;
    padding: 1.5rem !important;
    border-radius: 20px !important;
    border: 1px solid #EAE7DC !important;
    box-shadow: 0 15px 45px rgba(0,0,0,0.15) !important;
    background: #ffffff !important;
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
# 🦉 PLOVOUCÍ EKO-SOVA (AI TUTOR CHAT)
# =========================================================================
with st.popover("🦉"):
    st.markdown("### 🦉 Eko-Sova radí!")
    otazka = st.text_input("Zeptej se mě na cokoliv z ekonomiky:")
    
    if st.button("Zeptat se", key="btn_sova_ptat_se"):
        if otazka:
            with st.spinner("Sova houká a přemýšlí..."):
                # Zavolá vaši už hotovou funkci s OpenAI
                odpoved = ai_tutor_chat(otazka, st.session_state.get("current_view", "Neznámá kapitola"))
                st.info(odpoved)
        else:
            st.warning("Nejprve musíš napsat otázku!")

# =========================================================================
# 7. ROUTING A STRÁNKY APLIKACE (MAIN VIEWS)
# =========================================================================
def zakovsky_panel():
    st.title("👨‍🎓 Můj žákovský profil")
    # ... zbytek vašeho kódu ...
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
        st.write(f"Celkem máš **{current_
