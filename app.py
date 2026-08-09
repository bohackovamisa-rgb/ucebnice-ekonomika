import math
import pandas as pd
import streamlit as st
from supabase import create_client, Client
from kapitoly import kapitola1, kapitola2, kapitola3, kapitola4, kapitola5, kapitola6
import unicodedata

def ocisti_username(text: str) -> str:
    """Odstraní diakritiku a převede text na malá písmena pro bezpečný dotaz do DB."""
    if not text:
        return ""
    text = unicodedata.normalize('NFD', text)
    text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
    return text.strip().lower()

# =========================================================================
# 1. KONFIGURACE STRÁNKY
# =========================================================================
st.set_page_config(
    page_title="Učebnice ekonomiky",
    page_icon="📖",
    layout="wide"
)

# =========================================================================
# 2. PROPOJENÍ S DATABÁZÍ SUPABASE
# =========================================================================
@st.cache_resource
def init_supabase() -> Client:
    url = st.secrets["connections"]["supabase"]["SUPABASE_URL"]
    key = st.secrets["connections"]["supabase"]["SUPABASE_KEY"]
    return create_client(url, key)

supabase = init_supabase()

# =========================================================================
# 3. STYLOVÁNÍ
# =========================================================================
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

# =========================================================================
# 4. POMOCNÁ FUNKCE PRO UKLÁDÁNÍ ODPOVĚDÍ
# =========================================================================
def uloz_odpoved(kapitola: str, otazka_id: str, odpoved_text: str):
    """Uloží nebo aktualizuje odpověď přihlášeného žáka v Supabase."""
    username = st.session_state.get("username")
    if not username:
        return
    
    try:
        existing = supabase.table("odpovedi")\
            .select("username")\
            .eq("username", username)\
            .eq("kapitola", kapitola)\
            .eq("otazka_id", otazka_id)\
            .execute()
        
        if existing.data:
            supabase.table("odpovedi").update({"odpoved": odpoved_text})\
                .eq("username", username)\
                .eq("kapitola", kapitola)\
                .eq("otazka_id", otazka_id)\
                .execute()
        else:
            new_record = {
                "username": username,
                "kapitola": kapitola,
                "otazka_id": otazka_id,
                "odpoved": odpoved_text
            }
            supabase.table("odpovedi").insert(new_record).execute()
        st.toast("✅ Odpověď byla uložena!", icon="💾")
    except Exception as e:
        st.error(f"Chyba při ukládání odpovědi: {e}")

st.session_state["uloz_odpoved_fn"] = uloz_odpoved

# =========================================================================
# 5. PŘIHLAŠOVACÍ A REGISTRAČNÍ BRÁNA (S OŠETŘENÍM DIAKRITIKY)
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
            
            # --- TAB 1: PŘIHLÁŠENÍ (BOD 1) ---
            with tab_login:
                with st.form("login_form", border=False):
                    username_input = st.text_input("Uživatelské jméno:", placeholder="Zadejte uživatelské jméno...")
                    password_input = st.text_input("Heslo:", type="password", placeholder="Vaše heslo...")
                    submit = st.form_submit_button("Vstoupit do učebnice", use_container_width=True)
                    
                    if submit:
                        try:
                            # 1. OŠETŘENÍ DIAKRITIKY PŘI PŘIHLÁŠENÍ
                            ciste_jmeno = ocisti_username(username_input)
                            res = supabase.table("uzivatele").select("*").eq("username", ciste_jmeno).execute()
                            
                            if res.data:
                                user = res.data[0]
                                if str(user.get("password")) == password_input:
                                    st.session_state["is_logged_in"] = True
                                    st.session_state["username"] = user.get("username")
                                    st.session_state["user_role"] = user.get("role", "student")
                                    st.session_state["user_name"] = user.get("jmeno", "Uživatel")
                                    st.session_state["user_class"] = user.get("trida", "")
                                    st.rerun()
                                else:
                                    st.error("Nesprávné heslo!")
                            else:
                                st.error("Uživatel s tímto jménem neexistuje!")
                        except Exception as e:
                            st.error(f"Chyba při připojování: {e}")

            # --- TAB 2: REGISTRACE (BOD 2) ---
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
                                    
                                    # 2. OŠETŘENÍ DIAKRITIKY PŘI REGISTRACI
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
                                        st.success("Účet byl úspěšně vytvořen! Nyní se můžete přihlásit.")
                            except Exception as e:
                                st.error(f"Chyba při registraci: {e}")
    return False
# =========================================================================
# 6. NAVIGAČNÍ STAV A BOČNÍ PANEL
# =========================================================================
if "current_view" not in st.session_state:
    st.session_state["current_view"] = "Uvod"

with st.sidebar:
    st.markdown(
        f"""
        <div style='padding: 0.5rem 0;'>
            <span style='font-size: 0.72rem; font-weight: 800; color: #78716C; text-transform: uppercase;'>E-Learning Portal</span>
            <h2 style='margin: 0; padding: 0; border: none; font-size: 1.25rem; color: #0F172A; font-weight: 800;'>Učebnice Ekonomiky</h2>
        </div>
        <div style='background-color: #F2EFE9; padding: 0.8rem; border-radius: 12px; margin-bottom: 1rem; border: 1px solid #EAE7DC;'>
            <div style='font-size: 0.75rem; color: #78716C; font-weight: 600;'>PŘIHLÁŠEN(A):</div>
            <div style='font-size: 0.95rem; font-weight: 700; color: #1C1917;'>👤 {st.session_state['user_name']}</div>
            <div style='font-size: 0.8rem; color: #44403C;'>Role: {st.session_state['user_role'].capitalize()} {f"({st.session_state['user_class']})" if st.session_state.get('user_class') else ""}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.session_state["user_role"] == "teacher":
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
    if st.button("Odhlásit se", use_container_width=True):
        st.session_state.clear()
        st.rerun()

# =========================================================================
# 7. SMĚROVÁNÍ OBSAHU
# =========================================================================

if st.session_state["current_view"] == "Ucitel_Panel":
    st.title("👩‍🏫 Učitelský panel")
    
    tab_tridy, tab_vysledky = st.tabs(["➕ Správa a tvorba tříd", "📊 Výsledky žáků"])
    
    with tab_tridy:
        st.markdown("### Vytvořit novou třídu")
        with st.form("nova_trida_form"):
            novy_nazev = st.text_input("Název třídy (např. 4.B - Ekonomika):")
            novy_kod = st.text_input("Zvolte Zvací kód pro žáky (např. EKO4B):", help="Tento kód dají žáci při registraci.")
            btn_vytvorit = st.form_submit_button("Vytvořit třídu 🚀")
            
            if btn_vytvorit:
                if novy_nazev and novy_kod:
                    try:
                        kod_clean = novy_kod.strip().upper()
                        check = supabase.table("tridy").select("kod_tridy").eq("kod_tridy", kod_clean).execute()
                        if check.data:
                            st.error("Tento Zvací kód již existuje, zvolte jiný.")
                        else:
                            new_trida = {
                                "kod_tridy": kod_clean,
                                "nazev_tridy": novy_nazev.strip(),
                                "ucitel_username": st.session_state["username"]
                            }
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
        st.markdown("### Přehled odevzdaných prací")
        try:
            t_res = supabase.table("tridy").select("nazev_tridy").eq("ucitel_username", st.session_state["username"]).execute()
            list_trid = [x["nazev_tridy"] for x in t_res.data] if t_res.data else []
            
            if list_trid:
                vybrana_t = st.selectbox("Vyberte třídu:", list_trid)
                zaci_res = supabase.table("uzivatele").select("username, jmeno").eq("trida", vybrana_t).execute()
                
                if zaci_res.data:
                    zaci_dict = {z["jmeno"]: z["username"] for z in zaci_res.data}
                    vybrany_zak_jmeno = st.selectbox("Vyberte žáka:", list(zaci_dict.keys()))
                    vybrany_zak_user = zaci_dict[vybrany_zak_jmeno]
                    
                    odpovedi_res = supabase.table("odpovedi").select("*").eq("username", vybrany_zak_user).execute()
                    if odpovedi_res.data:
                        st.markdown(f"#### Odpovědi žáka: {vybrany_zak_jmeno}")
                        
                        df_export = pd.DataFrame(odpovedi_res.data)
                        povolene_sloupce = [c for c in ["username", "kapitola", "otazka_id", "odpoved"] if c in df_export.columns]
                        df_export = df_export[povolene_sloupce]
                        df_export = df_export.rename(columns={
                            "username": "Žák (Username)",
                            "kapitola": "Kapitola",
                            "otazka_id": "Úkol / Otázka",
                            "odpoved": "Odpověď"
                        })
                        
                        csv_data = df_export.to_csv(index=False, sep=';').encode('utf-8-sig')
                        
                        st.download_button(
                            label="📥 Stáhnout odpovědi v CSV (pro Excel)",
                            data=csv_data,
                            file_name=f"odpovedi_{vybrany_zak_user}.csv",
                            mime="text/csv"
                        )
                        
                        for o in odpovedi_res.data:
                            with st.expander(f"📘 {o['kapitola']} — Úkol: {o['otazka_id']}"):
                                st.write(o["odpoved"])
                    else:
                        st.write("Tento žák zatím neodevzdal žádné odpovědi.")
                else:
                    st.write("V této třídě zatím nejsou zaregistrovaní žádní žáci.")
            else:
                st.write("Nejprve vytvořte třídu v záložce 'Správa a tvorba tříd'.")
        except Exception as e:
            st.error(f"Chyba při načítání výsledků: {e}")

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
    if hasattr(kapitola1, "render"): kapitola1.render()
    elif hasattr(kapitola1, "show"): kapitola1.show()

elif st.session_state["current_view"] == "Kapitola 2":
    if hasattr(kapitola2, "render"): kapitola2.render()
    elif hasattr(kapitola2, "show"): kapitola2.show()

elif st.session_state["current_view"] == "Kapitola 3":
    if hasattr(kapitola3, "render"): kapitola3.render()
    elif hasattr(kapitola3, "show"): kapitola3.show()

elif st.session_state["current_view"] == "Kapitola 4":
    if hasattr(kapitola4, "render"): kapitola4.render()
    elif hasattr(kapitola4, "show"): kapitola4.show()

elif st.session_state["current_view"] == "Kapitola 5":
    if hasattr(kapitola5, "render"): kapitola5.render()
    elif hasattr(kapitola5, "show"): kapitola5.show()

elif st.session_state["current_view"] == "Kapitola 6":
    if hasattr(kapitola6, "render"): kapitola6.render()
    elif hasattr(kapitola6, "show"): kapitola6.show()
