import math
import unicodedata
import pandas as pd
import streamlit as st
from supabase import create_client, Client
from kapitoly import kapitola1, kapitola2, kapitola3, kapitola4, kapitola5, kapitola6
import gspread
import json
import yfinance as yf

# =========================================================================
# 1. KONFIGURACE STRÁNKY & INICIALIZACE STAVU
# =========================================================================
st.set_page_config(
    page_title="Učebnice ekonomiky",
    page_icon="📖",
    layout="wide"
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

# =========================================================================
# 2. POMOCNÉ FUNKCE A DATABÁZE SUPABASE & GOOGLE SHEETS
# =========================================================================
def ocisti_username(text: str) -> str:
    """Odstraní diakritiku a převede text na malá písmena pro bezpečný dotaz do DB."""
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

@st.cache_resource(ttl=60) # Připojení na Google Sheets se obnoví max jednou za minutu
def init_gspread():
    raw_creds = st.secrets["google_credentials"]
    tajemstvi = json.loads(raw_creds) if isinstance(raw_creds, str) else dict(raw_creds)
    if "private_key" in tajemstvi:
        tajemstvi["private_key"] = tajemstvi["private_key"].replace("\\n", "\n").replace("\r", "").strip()
    return gspread.service_account_from_dict(tajemstvi)


# --- 1. FUNKCE PRO VYKRESLENÍ A ZÁPIS OTÁZKY V KAPITOLÁCH ---
def vykresli_otazku(otazka_id, text_otazky, kapitola_id, ulozene_odpovedi):
    st.markdown(f"**{text_otazky}**")
    staved_text = ulozene_odpovedi.get(otazka_id, "")
    
    if staved_text:
        st.success("✅ **Tento úkol už máš splněný!** (Můžeš ho níže upravit)")
    else:
        st.info("💡 **Tento úkol zatím nemáš vyplněný.**")
        
    odpoved_zaka = st.text_area("Tvoje odpověď:", value=staved_text, key=f"in_{otazka_id}")
    
    if st.button("Uložit odpověď 💾", key=f"btn_{otazka_id}"):
        if not odpoved_zaka.strip():
            st.warning("Před uložením nejprve napiš odpověď!")
            return
            
        nazev_kapitoly = f"Kapitola {kapitola_id}" if not str(kapitola_id).startswith("Kapitola") else kapitola_id
        
        try:
            supabase.table("odpovedi").upsert({
                "username": st.session_state.get("username", "demo.zak"),
                "kapitola": nazev_kapitoly,
                "otazka_id": otazka_id,
                "odpoved": odpoved_zaka
            }).execute()
            
            # Okamžitý zápis do paměti aplikace
            if "ulozene_odpovedi" not in st.session_state:
                st.session_state["ulozene_odpovedi"] = {}
            st.session_state["ulozene_odpovedi"][otazka_id] = odpoved_zaka
            
            st.toast("Odpověď byla uložena!", icon="💾")
            st.rerun()
        except Exception as e:
            st.error(f"Chyba při zápisu do databáze: {e}")

st.session_state["vykresli_otazku_fn"] = vykresli_otazku


# --- FUNKCE PRO POMOCNÉ UKLÁDÁNÍ RŮZNÝCH INTERAKTIVNÍCH AKTIVIT ---
def uloz_odpoved(kapitola: str, otazka_id: str, odpoved_text: str):
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
# 📝 ŽÁKOVSKÝ PANEL (PŘEHLED ÚKOLŮ + INVESTIČNÍ SIMULÁTOR)
# =========================================================================
def zakovsky_panel():
    st.title("👨‍🎓 Můj žákovský panel")
    
    username = st.session_state.get("username")
    if not username:
        st.warning("Nejprve se prosím přihlaste.")
        return

    tab_ukoly, tab_investice = st.tabs(["📝 Moje úkoly z učebnice", "📈 Můj investiční profil"])

    # -------------------------------------------------------------------------
    # ZÁLOŽKA 1: ÚKOLY A ODPOVĚDI
    # -------------------------------------------------------------------------
    with tab_ukoly:
        st.write("Zde vidíš všechny své uložené odpovědi napříč celou učebnicí. Můžeš sledovat svůj pokrok a odpovědi upravovat.")
        
        try:
            res = supabase.table("odpovedi").select("*").eq("username", username).execute()
            odpovedi_data = res.data if res.data else []
        except Exception as e:
            st.error(f"❌ **Chyba při načítání ze Supabase:** {e}")
            odpovedi_data = []

        if not odpovedi_data:
            st.info("💡 **Zatím nemáš uložené žádné odpovědi.** Otevři kapitolu, vyplň úkol a klikni na *Uložit odpověď*.")
        else:
            CELKEM_UKOLU = {
                "Kapitola 1": 15, "Kapitola 2": 11, "Kapitola 3": 12,
                "Kapitola 4": 15, "Kapitola 5": 14, "Kapitola 6": 21
            }

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
                                        "odpoved": nova_odpoved
                                    }).execute()
                                    
                                    if "ulozene_odpovedi" not in st.session_state:
                                        st.session_state["ulozene_odpovedi"] = {}
                                    st.session_state["ulozene_odpovedi"][otazka_id] = nova_odpoved
                                    
                                    st.toast("Odpověď byla upravena!", icon="✅")
                                    st.rerun()
                                except Exception as ex:
                                    st.error(f"Chyba při ukládání: {ex}")
                        st.markdown("---")

    # -------------------------------------------------------------------------
    # ZÁLOŽKA 2: OSOBNÍ INVESTIČNÍ PROFIL ŽÁKA
    # -------------------------------------------------------------------------
    with tab_investice:
        st.markdown("### 📈 Tvé investiční portfolio")
        st.write("Zde živě vidíš, jak si vedeš na burze. Pokud chceš nakupovat nebo prodávat další akcie a kryptoměny, přejdi přímo do obchodní aplikace.")
        
        # Dynamický odkaz předávající uživatele do simulátoru
        muj_nick = username.strip().lower()
        url_sim = f"https://skolni-investice-jcu32nvp35ymaymjb9g2k5.streamlit.app/?user={muj_nick}&nick={muj_nick}"
        st.link_button("🚀 Přejít do investičního simulátoru (Koupit / Prodat)", url_sim, type="primary")
        
        st.divider()

        with st.spinner("Aktualizuji data z burzy... ⏳"):
            try:
                # 1. NAPOJENÍ NA GOOGLE SHEETS
                client = init_gspread()
                soubor = client.open("Skolni_Investice_DB")
                sheet_uziv = soubor.sheet1
                
                # 2. VYNUCENÍ ČERSTVÝCH DAT (Odstranění paměťového zpoždění)
                data_inv = sheet_uziv.get_all_records(value_render_option="UNFORMATTED_VALUE")
                df_inv = pd.DataFrame(data_inv)

                df_zaka = df_inv[df_inv["Nick"].astype(str).str.strip().str.lower() == muj_nick]

                if not df_zaka.empty:
                    row = df_zaka.iloc[0]
                    zustatek = float(row.get("Zustatek", 0.0))
                    
                    AKTIVA_MAP = {
                        "AAPL": ("Apple (AAPL)", "USD"), "TSLA": ("Tesla (TSLA)", "USD"), "MSFT": ("Microsoft (MSFT)", "USD"),
                        "GOOGL": ("Google (GOOGL)", "USD"), "AMZN": ("Amazon (AMZN)", "USD"), "NVDA": ("Nvidia (NVDA)", "USD"),
                        "META": ("Meta (META)", "USD"), "CEZ": ("ČEZ", "CZK"), "BTC": ("Bitcoin", "USD"), "ETH": ("Ethereum", "USD")
                    }

                    try:
                        kurz_usd = yf.Ticker("CZK=X").history(period="1d")['Close'].iloc[-1]
                    except Exception:
                        kurz_usd = 23.5

                    hodnota_aktiv = 0.0
                    drzena_aktiva = {}

                    for db_col, (nazev, mena) in AKTIVA_MAP.items():
                        ks = float(row.get(db_col, 0.0))
                        if ks > 0:
                            try:
                                ticker_symbol = "CEZ.PR" if db_col == "CEZ" else ("BTC-USD" if db_col == "BTC" else ("ETH-USD" if db_col == "ETH" else db_col))
                                cena = yf.Ticker(ticker_symbol).history(period="1d")['Close'].iloc[-1]
                                cena_czk = cena * kurz_usd if mena == "USD" else cena
                            except Exception:
                                cena_czk = 0.0
                            
                            hodnota_aktiv += (ks * cena_czk)
                            drzena_aktiva[nazev] = ks

                    celkovy_majetek = zustatek + hodnota_aktiv
                    zisk_ztrata = celkovy_majetek - 20000.0

                    col_met1, col_met2 = st.columns(2)
                    col_met1.metric("Celkový majetek", f"{celkovy_majetek:,.2f} Kč")
                    
                    if zisk_ztrata > 0:
                        col_met2.metric("Čistý zisk / ztráta", f"+{zisk_ztrata:,.2f} Kč")
                    else:
                        col_met2.metric("Čistý zisk / ztráta", f"{zisk_ztrata:,.2f} Kč")

                    col_inf1, col_inf2 = st.columns(2)
                    with col_inf1:
                        st.info(f"💵 **Volná hotovost k nákupu:**\n\n`{zustatek:,.2f} Kč`")
                        st.info(f"📈 **Hodnota nakoupených aktiv:**\n\n`{hodnota_aktiv:,.2f} Kč`")
                        
                    with col_inf2:
                        st.write("**Tvé aktuální portfolio:**")
                        if drzena_aktiva:
                            for aktivum, kusy in drzena_aktiva.items():
                                st.write(f"⚡ {aktivum}: `{kusy} ks`")
                        else:
                            st.write("Zatím nedržíš žádné akcie ani krypto.")

                    st.divider()
                    st.markdown("#### 📜 Historie tvých obchodů")
                    try:
                        sheet_trans = soubor.worksheet("Transakce")
                        # Opět vynucení načtení pro historii transakcí
                        data_trans = sheet_trans.get_all_records() 
                        
                        if data_trans:
                            df_trans = pd.DataFrame(data_trans)
                            df_trans_zak = df_trans[df_trans["Nick"].astype(str).str.strip().str.lower() == muj_nick]
                            
                            if not df_trans_zak.empty:
                                sloupce_k_zobrazeni = [c for c in df_trans_zak.columns if c not in ["Nick", "Jmeno"]]
                                st.dataframe(df_trans_zak[sloupce_k_zobrazeni], use_container_width=True, hide_index=True)
                            else:
                                st.write("Zatím jsi neprovedl/a žádný obchod.")
                    except Exception:
                        st.warning("Nepodařilo se načíst historii tvých transakcí.")
                else:
                    st.info("Tvůj účet zatím v simulátoru nemá žádná data (nebo se uživatelské jméno neshoduje s databází).")

            except Exception as e:
                st.error(f"Chyba při stahování dat z burzy: {e}")
                
# =========================================================================
# 3. ORIGINÁLNÍ STYLOVÁNÍ A DESIGN UČEBNICE
# =========================================================================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&display=swap');

[data-testid="stSidebarNav"] { display: none !important; }

html, body, [class*="css"], .stApp { 
    font-family: 'Montserrat', -apple-system, sans-serif !important; 
    background-color: #FAF8F5 !important; 
    color: #1C1917 !important; 
}
.main .block-container { 
    max-width: 920px !important; 
    padding-top: 2.5rem !important; 
    padding-bottom: 5rem !important; 
}

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
# 5. PŘIHLAŠOVACÍ A REGISTRAČNÍ BRÁNA
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
            
            # --- TAB 1: PŘIHLÁŠENÍ ---
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
                                    st.rerun()
                                else:
                                    st.error("Nesprávné heslo!")
                            else:
                                st.error("Uživatel s tímto jménem neexistuje!")
                        except Exception as e:
                            st.error(f"Chyba při připojování: {e}")

            # --- TAB 2: REGISTRACE ---
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
                                            "trida": nazev_tridy
                                        }
                                        supabase.table("uzivatele").insert(new_user).execute()
                                        st.success("Účet byl úspěšně vytvořen! Nyní se můžete přihlásit.")
                            except Exception as e:
                                st.error(f"Chyba při registraci: {e}")
    return False

# Stopne vykreslování, pokud uživatel není přihlášen
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
        <div style='background-color: #F2EFE9; padding: 0.8rem; border-radius: 12px; margin-bottom: 1rem; border: 1px solid #EAE7DC;'>
            <div style='font-size: 0.75rem; color: #78716C; font-weight: 600;'>PŘIHLÁŠEN(A):</div>
            <div style='font-size: 0.95rem; font-weight: 700; color: #1C1917;'>👤 {st.session_state.get('user_name', 'Uživatel')}</div>
            <div style='font-size: 0.8rem; color: #44403C;'>Role: {st.session_state.get('user_role', 'student').capitalize()} {f"({st.session_state.get('user_class', '')})" if st.session_state.get('user_class') else ""}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Učitelský panel jen pro učitele
    if st.session_state.get("user_role") == "teacher":
        st.markdown("<div class='sidebar-section-title'>👩‍🏫 UČITELSKÝ PANEL</div>", unsafe_allow_html=True)
        
        if st.button("📊 Správa tříd a odpovědí", use_container_width=True, type="primary" if st.session_state["current_view"] == "Ucitel_Panel" else "secondary"):
            st.session_state["current_view"] = "Ucitel_Panel"
            st.rerun()
            
        if st.button("📂 Materiály a testy", use_container_width=True, type="primary" if st.session_state["current_view"] == "Ucitel_Materialy" else "secondary"):
            st.session_state["current_view"] = "Ucitel_Materialy"
            st.rerun()
            
        st.divider()

    st.markdown("<div class='sidebar-section-title'>PŘEHLED A ŽÁK</div>", unsafe_allow_html=True)
    
    if st.button("Úvodní stránka 🏠", use_container_width=True, type="primary" if st.session_state["current_view"] == "Uvod" else "secondary"):
        st.session_state["current_view"] = "Uvod"
        st.rerun()

    if st.button("Moje odpovědi 📝", use_container_width=True, type="primary" if st.session_state["current_view"] == "Moje_Odpovedi" else "secondary"):
        st.session_state["current_view"] = "Moje_Odpovedi"
        st.rerun()

    st.markdown("<div class='sidebar-section-title'>KAPITOLY KURZU</div>", unsafe_allow_html=True)
    
    # 🔐 CHYTRÝ ZÁMEK: Odemčeno jen pro plné uživatele. "demo" a "nakladatel" vidí jen 2 kapitoly.
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
            st.rerun()

    st.divider()
    if st.button("Odhlásit se 🚪", use_container_width=True):
        st.session_state.clear()
        st.rerun()


# =========================================================================
# 7. SMĚROVÁNÍ OBSAHU (ROUTING)
# =========================================================================

# 1. Žákovský panel
if st.session_state["current_view"] == "Moje_Odpovedi":
    zakovsky_panel()

# 2. Učitelský panel
elif st.session_state["current_view"] == "Ucitel_Panel":
    st.title("👩‍🏫 Učitelský panel")
    
    tab_tridy, tab_vysledky, tab_investice = st.tabs([
        "➕ Správa a tvorba tříd", 
        "📊 Odpovědi z učebnice", 
        "📈 Výsledky ze simulátoru"
    ])
    
    with tab_tridy:
        st.markdown("### Vytvořit novou třídu")
        with st.form("nova_trida_form"):
            novy_nazev = st.text_input("Název třídy (např. 4.B - Ekonomika):")
            novy_kod = st.text_input("Zvolte Zvací kód pro žáky (např. EKO4B):", help="Tento kód zadají žáci při registraci.")
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
        st.markdown("### Přehled odevzdaných prací z učebnice")
        
        # 🎯 Cílové počty úkolů pro výpočet procent
        CELKEM_UKOLU = {
            "Kapitola 1": 15,
            "Kapitola 2": 11,
            "Kapitola 3": 12,
            "Kapitola 4": 15,
            "Kapitola 5": 14,
            "Kapitola 6": 21
        }
        
        try:
            t_res = supabase.table("tridy").select("nazev_tridy").eq("ucitel_username", st.session_state["username"]).execute()
            list_trid = [x["nazev_tridy"] for x in t_res.data] if t_res.data else []
            
            if list_trid:
                vybrana_t = st.selectbox("Vyberte třídu:", list_trid, key="sel_trida_uc")
                zaci_res = supabase.table("uzivatele").select("username, jmeno").eq("trida", vybrana_t).execute()
                
                if zaci_res.data:
                    zaci_dict = {z["jmeno"]: z["username"] for z in zaci_res.data}
                    
                    # ---------------------------------------------------------
                    # 📊 1. HROMADNÝ PŘEHLED CELÉ TŘÍDY
                    # ---------------------------------------------------------
                    st.markdown(f"#### 📊 Celkový pokrok třídy **{vybrana_t}**")
                    usernames_tridy = list(zaci_dict.values())
                    vsechny_odp_res = supabase.table("odpovedi").select("username, kapitola").in_("username", usernames_tridy).execute()
                    
                    if vsechny_odp_res.data:
                        pokrok_data = []
                        celkem_vsech_ukolu = sum(CELKEM_UKOLU.values())
                        
                        for jmeno, uname in zaci_dict.items():
                            odp_zaka = [o for o in vsechny_odp_res.data if o["username"] == uname]
                            zak_stats = {"Žák": jmeno}
                            celkem_hotovo_zaka = 0
                            
                            for kap, celkem_kap in CELKEM_UKOLU.items():
                                hotovo_kap = len([o for o in odp_zaka if o["kapitola"] == kap])
                                celkem_hotovo_zaka += hotovo_kap
                                zak_stats[kap] = f"{hotovo_kap} / {celkem_kap}"
                            
                            pct_celkem = int((celkem_hotovo_zaka / celkem_vsech_ukolu) * 100) if celkem_vsech_ukolu > 0 else 0
                            zak_stats["✅ Celkem hotovo"] = f"{celkem_hotovo_zaka} úkolů"
                            zak_stats["📈 Úspěšnost"] = f"{pct_celkem} %"
                            pokrok_data.append(zak_stats)
                            
                        df_pokrok = pd.DataFrame(pokrok_data)
                        st.dataframe(df_pokrok, use_container_width=True, hide_index=True)
                    else:
                        st.info("Zatím žádný žák v této třídě neodevzdal odpověď.")
                    
                    st.divider()

                    # ---------------------------------------------------------
                    # 🔍 2. DETAIL A EXPORT KONKRÉTNÍHO ŽÁKA
                    # ---------------------------------------------------------
                    st.markdown("#### 🔍 Detailní odpovědi konkrétního žáka")
                    vybrany_zak_jmeno = st.selectbox("Vyberte žáka pro zobrazení textů:", list(zaci_dict.keys()), key="sel_zak_uc")
                    vybrany_zak_user = zaci_dict[vybrany_zak_jmeno]
                    
                    odpovedi_res = supabase.table("odpovedi").select("*").eq("username", vybrany_zak_user).execute()
                    
                    if odpovedi_res.data:
                        # Příprava dat pro export do CSV
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
                            label=f"📥 Stáhnout odpovědi žáka {vybrany_zak_jmeno} v CSV (pro Excel)",
                            data=csv_data,
                            file_name=f"odpovedi_{vybrany_zak_user}.csv",
                            mime="text/csv"
                        )
                        st.write("")
                        
                        # Seskupení odpovědí podle kapitol pro zobrazení s Progress Barem
                        kapitoly_zaka_dict = {}
                        for o in odpovedi_res.data:
                            k = o.get("kapitola", "Ostatní")
                            if k not in kapitoly_zaka_dict:
                                kapitoly_zaka_dict[k] = []
                            kapitoly_zaka_dict[k].append(o)
                            
                        # Vykreslení kapitol
                        for kap_nazev in sorted(kapitoly_zaka_dict.keys()):
                            odp_v_kapitole = kapitoly_zaka_dict[kap_nazev]
                            hotovo = len(odp_v_kapitole)
                            celkem = CELKEM_UKOLU.get(kap_nazev, hotovo)
                            pct_cislo = min((hotovo / celkem), 1.0) if celkem > 0 else 1.0
                            pct_zobrazeni = int(pct_cislo * 100)
                            
                            with st.expander(f"📘 {kap_nazev} — splněno {hotovo}/{celkem} ({pct_zobrazeni} %)", expanded=False):
                                st.progress(pct_cislo)
                                st.write("")
                                # Výpis odpovědí seřazených podle ID
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
                # 1. ZJISTĚNÍ TŘÍD A ŽÁKŮ TOHOTO UČITELE
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
                    
                    # Načtení dat ze Sheets
                    vsechna_data_zaci = soubor.sheet1.get_all_records(value_render_option="UNFORMATTED_VALUE")
                    vsechny_transakce = soubor.worksheet("Transakce").get_all_records(value_render_option="UNFORMATTED_VALUE")
                    
                    df_zaci = pd.DataFrame(vsechna_data_zaci)
                    df_transakce = pd.DataFrame(vsechny_transakce)
                    
                    # Filtrujeme jen žáky tohoto učitele
                    if not df_zaci.empty:
                        df_zaci["Nick_lower"] = df_zaci["Nick"].astype(str).str.strip().str.lower()
                        df_zaci = df_zaci[df_zaci["Nick_lower"].isin(moje_usernames)]
                    
                    if not df_zaci.empty:
                        # NAČTENÍ ŽIVÝCH CEN (aby mohl učitel vidět reálný žebříček majetku)
                        AKTIVA_MAP = {
                            "AAPL": ("Apple (AAPL)", "USD"), "TSLA": ("Tesla (TSLA)", "USD"), "MSFT": ("Microsoft (MSFT)", "USD"),
                            "GOOGL": ("Google (GOOGL)", "USD"), "AMZN": ("Amazon (AMZN)", "USD"), "NVDA": ("Nvidia (NVDA)", "USD"),
                            "META": ("Meta (META)", "USD"), "CEZ": ("ČEZ", "CZK"), "BTC": ("Bitcoin", "USD"), "ETH": ("Ethereum", "USD")
                        }

                        try:
                            kurz_usd = yf.Ticker("CZK=X").history(period="1d")['Close'].iloc[-1]
                        except Exception:
                            kurz_usd = 23.5

                        zive_ceny = {}
                        for db_col, (nazev, mena) in AKTIVA_MAP.items():
                            try:
                                ticker_symbol = "CEZ.PR" if db_col == "CEZ" else ("BTC-USD" if db_col == "BTC" else ("ETH-USD" if db_col == "ETH" else db_col))
                                cena = yf.Ticker(ticker_symbol).history(period="1d")['Close'].iloc[-1]
                                zive_ceny[db_col] = cena * kurz_usd if mena == "USD" else cena
                            except Exception:
                                zive_ceny[db_col] = 0.0
                        
                        # VÝPOČET MAJETKU PRO KAŽDÉHO ŽÁKA
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
                                "Zustatek": zustatek,
                                "HodnotaAktiv": hodnota_aktiv,
                                "CelkovyMajetek": celkovy_majetek,
                                "Zisk": celkovy_majetek - 20000.0,
                                "Portfolio": drzena_aktiva
                            })

                        # Seřadit od nejbohatšího (žebříček)
                        zaci_list = sorted(zaci_list, key=lambda x: x["CelkovyMajetek"], reverse=True)

                        # VYKRESLENÍ ŽEBŘÍČKU POMOCÍ ROZBALOVACÍCH LIŠT
                        st.markdown("#### 🥇 Žebříček mých studentů")
                        st.write("Kliknutím na žáka rozbalíte detail jeho portfolia a historii nákupů/prodejů.")
                        
                        for i, zak in enumerate(zaci_list):
                            poradi = i + 1
                            medaile = "🥇" if poradi == 1 else "🥈" if poradi == 2 else "🥉" if poradi == 3 else f"{poradi}."
                            zisk_str = f"+{zak['Zisk']:,.2f} Kč" if zak['Zisk'] > 0 else f"{zak['Zisk']:,.2f} Kč"
                            
                            nadpis_expanderu = f"{medaile} {zak['Jmeno']} (Nick: {zak['Nick']}) — Majetek: {zak['CelkovyMajetek']:,.2f} Kč | Zisk: {zisk_str}"
                            
                            with st.expander(nadpis_expanderu):
                                c1, c2 = st.columns(2)
                                with c1:
                                    st.write("**Detail účtu:**")
                                    st.info(f"💵 Volná hotovost k nákupu: `{zak['Zustatek']:,.2f} Kč`\n\n📈 Hodnota nakoupených akcií: `{zak['HodnotaAktiv']:,.2f} Kč`")
                                with c2:
                                    st.write("**Aktuální portfolio žáka:**")
                                    if zak["Portfolio"]:
                                        for aktivum, kusy in zak["Portfolio"].items():
                                            st.write(f"⚡ {aktivum}: `{kusy} ks`")
                                    else:
                                        st.write("Tento žák zatím nedrží žádné akcie ani kryptoměny.")
                                
                                st.write("**📜 Historie obchodů:**")
                                if not df_transakce.empty:
                                    # Filtrujeme transakce jen pro tohoto žáka
                                    df_trans_zak = df_transakce[df_transakce["Nick"].astype(str).str.strip().str.lower() == zak["Nick"].strip().lower()]
                                    if not df_trans_zak.empty:
                                        # Odstraníme zbytečné sloupce a otočíme tak, aby nejnovější byly nahoře
                                        sloupce_k_zobrazeni = [c for c in df_trans_zak.columns if c not in ["Nick", "Jmeno"]]
                                        st.dataframe(df_trans_zak[sloupce_k_zobrazeni].iloc[::-1], use_container_width=True, hide_index=True)
                                    else:
                                        st.write("Tento žák zatím neprovedl žádný obchod.")
                                else:
                                    st.write("Tabulka historie obchodů je zcela prázdná.")
                                    
                    else:
                        st.info("Vaši žáci zatím nemají založené účty v simulátoru.")

            except Exception as e:
                st.error(f"Chyba při načítání dat pro učitele: {e}")

# 3. Učitelské materiály
elif st.session_state["current_view"] == "Ucitel_Materialy":
    st.title("📂 Materiály k výuce a testy")
    st.markdown("""
    <div class="box-gray">
        Tato sekce je viditelná <b>pouze pro přihlášené učitele</b>. 
        Najdete zde metodické podklady, prezentace, pracovní listy a testy ke všem kapitolám.
    </div>
    """, unsafe_allow_html=True)

    tab_metodika, tab_testy = st.tabs(["📄 Metodické balíčky ke kapitolám", "📝 Písemné práce a testy"])

    # --- ZÁLOŽKA 1: METODIKY ---
    with tab_metodika:
        vybrana_kap = st.selectbox(
            "Vyberte kapitolu učebnice:",
            [
                "Kapitola 1: Podnikavost a startupy",
                "Kapitola 2: Finance a osobní management",
                "Kapitola 3: Výroba, náklady a efektivita",
                "Kapitola 4: Zaměstnanci a trh práce",
                "Kapitola 5: Stát, daně a ekonomika",
                "Kapitola 6: Management a marketing"
            ]
        )
        
        st.divider()

        # Zobrazení materiálů pro Kapitolu 1
        if vybrana_kap == "Kapitola 1: Podnikavost a startupy":
            st.markdown("### 📘 Materiály ke Kapitole 1")
            
            with st.container(border=True):
                st.markdown("#### 📦 Výukový modul: Influencer jako firma")
                st.markdown("""
                **Popis materiálu:**  
                Komplexní výukový balíček zaměřený na téma podnikání v digitální době a světě influencerů. Obsahuje metodickou příručku pro vyučujícího, prezentaci pro výklad v hodině, pracovní listy pro žáky a praktické případové studie. Žáci na reálných příkladech pochopí principy OSVČ, zdanění příjmů a obchodní modely na sociálních sítích.
                
                **Obsah balíčku:**  
                * 📄 Metodická příručka a průvodní list (PDF / DOCX)
                * 📊 Prezentace k výkladu (PPTX)
                * 📝 Pracovní listy a případové studie pro žáky
                * 📈 Praktická kalkulační tabulka (XLSX)
                """)
                
                try:
                    with open("Influencer - podnikání.zip", "rb") as file:
                        st.download_button(
                            label="📥 Stáhnout balíček: Influencer jako firma (ZIP)",
                            data=file,
                            file_name="Influencer_podnikani.zip",
                            mime="application/zip",
                            type="primary"
                        )
                except FileNotFoundError:
                    st.warning("Soubor 'Influencer - podnikání.zip' nebyl na GitHubu nalezen.")

        else:
            st.info(f"Pro **{vybrana_kap}** zatím nebyly nahrány žádné metodické balíčky.")

    # --- ZÁLOŽKA 2: TESTY ---
    with tab_testy:
        st.markdown("### 📝 Návrhy písemných prací a testů")
        st.info("Testy ke stažení se připravují.")


# 4. Úvodní stránka
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

# 5. Načítání konkrétních kapitol (1 až 6)
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
            # Připravíme si obě možné varianty zápisu kapitoly
            kap_nazev = f"Kapitola {kap_num}" if not str(kap_num).startswith("Kapitola") else kap_num
            
            res = (
                supabase.table("odpovedi")
                .select("otazka_id, odpoved")
                .eq("username", st.session_state["username"])
                .in_("kapitola", [kap_nazev, str(kap_num)])
                .execute()
            )
            if res.data:
                st.session_state["ulozene_odpovedi"] = {
                    row["otazka_id"]: row["odpoved"] for row in res.data
                }

        if hasattr(modul, "render"):
            modul.render()
        elif hasattr(modul, "show"):
            modul.show()
