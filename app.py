import math
import unicodedata
import pandas as pd
import streamlit as st
from supabase import create_client, Client
from kapitoly import kapitola1, kapitola2, kapitola3, kapitola4, kapitola5, kapitola6

# =========================================================================
# 1. KONFIGURACE STRÁNKY & INICIALIZACE STAVU
# =========================================================================
st.set_page_config(
    page_title="Učebnice ekonomiky",
    page_icon="📖",
    layout="wide"
)

# Inicializace výchozích proměnných relace
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

# =========================================================================
# 2. POMOCNÉ FUNKCE A DATABÁZE
# =========================================================================
def ocisti_username(text: str) -> str:
    """Odstraní diakritiku a převede text na malá písmena."""
    if not text:
        return ""
    text = unicodedata.normalize('NFD', text)
    text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
    return text.strip().lower()

@st.cache_resource
def init_supabase() -> Client:
    url = st.secrets["connections"]["supabase"]["SUPABASE_URL"]
    key = st.secrets["connections"]["supabase"]["SUPABASE_KEY"]
    return create_client(url, key)

supabase = init_supabase()

# =========================================================================
# 3. PŘIHLAŠOVACÍ A REGISTRAČNÍ BRÁNA
# =========================================================================
def login_screen():
    if st.session_state.get("is_logged_in", False):
        return True

    col1, col2, col3 = st.columns([1, 1.8, 1])
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("<h2 style='text-align: center; border: none; font-weight: 800; margin-bottom: 0;'>Učebnice ekonomiky</h2>", unsafe_allow_html=True)
            
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
                                    st.session_state["username"] = user.get("username", "")
                                    st.session_state["user_role"] = user.get("role", "student")
                                    # Načtení reálného jména (případně fallback na username)
                                    st.session_state["user_name"] = user.get("jmeno") or user.get("username") or "Uživatel"
                                    st.session_state["user_class"] = user.get("trida", "")
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
                                    st.error("Zadaný kód třídy neexistuje!")
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
                                            "trida": nazev_tridy
                                        }
                                        supabase.table("uzivatele").insert(new_user).execute()
                                        st.success("Účet vytvořen! Nyní se můžete přihlásit.")
                            except Exception as e:
                                st.error(f"Chyba při registraci: {e}")
    return False

# --- KLÍČOVÝ KROK: ZASTAVENÍ APLIKACE PRO NEPŘIHLÁŠENÉ ---
if not login_screen():
    st.stop()

# =========================================================================
# 4. NAVIGAČNÍ STAV A BOČNÍ PANEL (ZOBRAZÍ SE AŽ PO PŘIHLÁŠENÍ)
# =========================================================================
with st.sidebar:
    st.markdown(
        f"""
        <div style='padding: 0.5rem 0;'>
            <span style='font-size: 0.72rem; font-weight: 800; color: #78716C; text-transform: uppercase;'>E-Learning Portal</span>
            <h2 style='margin: 0; padding: 0; border: none; font-size: 1.25rem; color: #0F172A; font-weight: 800;'>Učebnice Ekonomiky</h2>
        </div>
        <div style='background-color: #F2EFE9; padding: 0.8rem; border-radius: 12px; margin-bottom: 1rem; border: 1px solid #EAE7DC;'>
            <div style='font-size: 0.75rem; color: #78716C; font-weight: 600;'>PŘIHLÁŠEN(A):</div>
            <div style='font-size: 0.95rem; font-weight: 700; color: #1C1917;'>👤 {st.session_state.get('user_name', 'Uživatel')}</div>
            <div style='font-size: 0.8rem; color: #44403C;'>Role: {st.session_state.get('user_role', 'student').capitalize()} {f"({st.session_state.get('user_class', '')})" if st.session_state.get('user_class') else ""}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.session_state.get("user_role") == "teacher":
        st.markdown("<div class='sidebar-section-title'>👩‍🏫 UČITELSKÝ PANEL</div>", unsafe_allow_html=True)
        if st.button("📊 Přehled a správa tříd", use_container_width=True, type="primary" if st.session_state["current_view"] == "Ucitel_Panel" else "secondary"):
            st.session_state["current_view"] = "Ucitel_Panel"
            st.rerun()
        st.divider()

    st.markdown("<div class='sidebar-section-title'>KAPITOLY KURZU</div>", unsafe_allow_html=True)
    
    if st.button("Úvodní stránka", use_container_width=True, type="primary" if st.session_state["current_view"] == "Uvod" else "secondary"):
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
        if st.button(title, key=f"nav_{key}", use_container_width=True, type="primary" if is_active else "secondary"):
            st.session_state["current_view"] = key
            st.rerun()

    st.divider()
    
    # --- BEZPEČNÉ ODHLÁŠENÍ ---
    if st.button("Odhlásit se", use_container_width=True):
        st.session_state["is_logged_in"] = False
        st.session_state["username"] = ""
        st.session_state["user_name"] = "Uživatel"
        st.session_state["user_role"] = "student"
        st.session_state["user_class"] = ""
        st.session_state["current_view"] = "Uvod"
        st.rerun()
# =========================================================================
# 5. HLAVNÍ OBSAH A VYKRSLOVÁNÍ STRÁNEK
# =========================================================================
current_view = st.session_state.get("current_view", "Uvod")

if current_view == "Ucitel_Panel":
    st.title("📊 Učitelský panel a výsledky tříd")
    # Zde máš svůj kód pro přehled odpovědí a výsledků žáků
    
elif current_view == "Uvod":
    st.title("📖 Vítejte v Učebnici ekonomiky")
    st.write(f"Vítej, **{st.session_state.get('user_name')}**! Vyber si v levém menu kapitolu a můžeš začít.")

elif current_view == "Kapitola 1":
    kapitola1.render()
elif current_view == "Kapitola 2":
    kapitola2.render()
elif current_view == "Kapitola 3":
    kapitola3.render()
elif current_view == "Kapitola 4":
    kapitola4.render()
elif current_view == "Kapitola 5":
    kapitola5.render()
elif current_view == "Kapitola 6":
    kapitola6.render()        
