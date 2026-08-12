from datetime import datetime
import json
import gspread
import pandas as pd
import plotly.express as px
import streamlit as st
import yfinance as yf

# --- 1. SVĚTLÝ DESIGN UČEBNICE (MONTSERRAT + KRÉMOVÉ POZADÍ) ---
LIGHT_UCEBNICE_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&display=swap');

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
[data-testid="stSidebarNav"] {display: none !important;}

/* Základní světlý motiv */
html, body, [class*="css"], .stApp { 
    font-family: 'Montserrat', -apple-system, sans-serif !important; 
    background-color: #FAF8F5 !important; 
    color: #1C1917 !important; 
}

.main .block-container { 
    max-width: 920px !important; 
    padding-top: 2rem !important; 
    padding-bottom: 5rem !important; 
}

/* Nadpisy a texty */
h1, h2, h3, h4 { 
    font-family: 'Montserrat', sans-serif !important; 
    color: #0F172A !important; 
    font-weight: 800 !important; 
}
p, li, td, th, label, span, .stMarkdown { 
    font-family: 'Montserrat', sans-serif !important; 
    color: #334155 !important; 
    font-size: 0.95rem !important; 
}

/* Vstupní políčka */
.stTextInput input, .stTextArea textarea, div[data-baseweb="select"] > div {
    font-family: 'Montserrat', sans-serif !important;
    border-radius: 12px !important;
    border: 1px solid #E2DEC6 !important;
    background-color: #FFFFFF !important;
    color: #0F172A !important;
    font-size: 0.92rem !important;
}

/* Tlačítka */
button[data-testid="baseButton-primary"], button[kind="primary"], div.stButton > button, a[data-testid="stPageLink-NavLink"], a[data-testid="stLinkButton"] {
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
    text-decoration: none !important;
}

button:hover, div.stButton > button:hover, a[data-testid="stPageLink-NavLink"]:hover, a[data-testid="stLinkButton"]:hover {
    background-color: #334155 !important;
    border-color: #334155 !important;
    transform: translateY(-1px);
}

div.stButton > button *, a[data-testid="stPageLink-NavLink"] *, a[data-testid="stLinkButton"] * {
    color: #FFFFFF !important;
}

/* Karta metrik */
div[data-testid="stMetric"] {
    background-color: #FFFFFF !important;
    border: 1px solid #EAE7DC !important;
    border-radius: 16px !important;
    padding: 18px !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.03) !important;
}
div[data-testid="stMetricLabel"] { color: #78716C !important; font-weight: 600 !important; }
div[data-testid="stMetricValue"] { color: #0F172A !important; font-weight: 800 !important; font-family: 'Montserrat', sans-serif !important; }

/* Záložky (Tabs) */
.stTabs [data-baseweb="tab-list"] {
    background-color: #F2EFE9 !important;
    border-radius: 12px !important;
    padding: 6px !important;
    border: 1px solid #EAE7DC !important;
}
.stTabs [data-baseweb="tab"] { color: #44403C !important; font-weight: 600 !important; border: none !important; }
.stTabs [aria-selected="true"] {
    background-color: #FFFFFF !important;
    color: #111111 !important;
    border-radius: 8px !important;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05) !important;
}

/* Tabulky */
.stDataFrame { border: 1px solid #EAE7DC !important; border-radius: 12px !important; overflow: hidden !important; }
</style>
"""
st.markdown(LIGHT_UCEBNICE_CSS, unsafe_allow_html=True)

# Tlačítko návratu do hlavní učebnice
st.page_link("app.py", label="🏠 Zpět do Učebnice ekonomiky")

# --- POMOCNÉ FUNKCE ---
def bezpecny_float(hodnota):
    try:
        return float(hodnota)
    except (ValueError, TypeError):
        return 0.0

def hezke_kusy(hodnota):
    if float(hodnota).is_integer():
        return f"{int(hodnota)}"
    return f"{hodnota}"

def barva_zisku_ztraty(val):
    try:
        val = float(val)
        if val > 0:
            return 'background-color: #E6F4EA; color: #137333; font-weight: bold;'
        elif val < 0:
            return 'background-color: #FCE8E6; color: #C5221F; font-weight: bold;'
    except (ValueError, TypeError):
        pass
    return ''

# --- PAMĚŤ APLIKACE ---
if "prihlasen" not in st.session_state:
    st.session_state["prihlasen"] = False
    st.session_state["nick"] = ""
    st.session_state["jmeno"] = ""
    st.session_state["role"] = "ZAK"
    st.session_state["trida"] = ""
    st.session_state["zustatek"] = 0.0

# --- PŘIPOJENÍ K DATABÁZI GOOGLE SHEETS ---
@st.cache_resource
def pripojit_databazi():
    raw_creds = st.secrets["google_credentials"]
    
    if isinstance(raw_creds, str):
        tajemstvi = json.loads(raw_creds)
    else:
        tajemstvi = dict(raw_creds)
        
    if "private_key" in tajemstvi:
        tajemstvi["private_key"] = tajemstvi["private_key"].replace("\\n", "\n").replace("\r", "").strip()

    client = gspread.service_account_from_dict(tajemstvi)
    soubor = client.open("Skolni_Investice_DB")
    sheet_uzivatele = soubor.sheet1
    
    try:
        sheet_transakce = soubor.worksheet("Transakce")
    except Exception:
        sheet_transakce = None
        
    return sheet_uzivatele, sheet_transakce

try:
    db_uzivatele, db_transakce = pripojit_databazi()
except Exception as e:
    st.error(f"❌ Chyba při připojování databáze: {e}")
    st.stop()

AKTIVA = {
    "Apple": ("AAPL", "USD", "AAPL"),
    "Tesla": ("TSLA", "USD", "TSLA"),
    "Microsoft": ("MSFT", "USD", "MSFT"),
    "Google": ("GOOGL", "USD", "GOOGL"),
    "Amazon": ("AMZN", "USD", "AMZN"),
    "Nvidia": ("NVDA", "USD", "NVDA"),
    "Meta (Facebook)": ("META", "USD", "META"),
    "ČEZ": ("CEZ.PR", "CZK", "CEZ"),
    "Bitcoin": ("BTC-USD", "USD", "BTC"),
    "Ethereum": ("ETH-USD", "USD", "ETH")
}

# ==========================================
# --- AUTOMATICKÉ PROPOJENÍ S UČEBNICÍ ---
# ==========================================
if st.session_state.get("is_logged_in", False) and not st.session_state.get("prihlasen", False):
    st.session_state["prihlasen"] = True
    st.session_state["nick"] = st.session_state.get("username", "zak")
    st.session_state["jmeno"] = st.session_state.get("user_name", "Žák")
    st.session_state["trida"] = st.session_state.get("user_class", "Nezadána")
    st.session_state["role"] = "UCITEL" if st.session_state.get("user_role") == "teacher" else "ZAK"
    
    try:
        zaznamy = db_uzivatele.get_all_records(value_render_option="UNFORMATTED_VALUE")
        moje_db_data = next((r for r in zaznamy if str(r.get("Nick", "")).strip().lower() == st.session_state["nick"].lower()), None)
        
        if moje_db_data:
            st.session_state["zustatek"] = bezpecny_float(moje_db_data.get("Zustatek", 20000.0))
        else:
            role_str = st.session_state["role"]
            db_uzivatele.append_row([
                role_str, 
                st.session_state["nick"], 
                st.session_state["jmeno"], 
                st.session_state["trida"], 
                "0000",
                20000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
            ])
            st.session_state["zustatek"] = 20000.0
    except Exception as e:
        st.warning(f"Chyba při automatickém načítání účtu: {e}")

# ==========================================
# --- POMOCNÁ FUNKCE PRO OBCHODOVÁNÍ na BURZE ---
# ==========================================
def vykresli_obchodovani_burzu(moje_data):
    st.metric(label="💵 Volný kapitál k dispozici", value=f"{st.session_state['zustatek']:.2f} Kč")
    st.write("")
    
    vybrane_aktivum = st.selectbox("Vyber aktivum k obchodování:", list(AKTIVA.keys()), key="sel_aktivum_trade")
    ticker_symbol, mena, sloupec_db = AKTIVA[vybrane_aktivum]
    
    with st.spinner(f"Načítám živý kurz pro {vybrane_aktivum}..."):
        try:
            if mena == "USD":
                kurz_usd_czk = yf.Ticker("CZK=X").history(period="1d")['Close'].iloc[-1]
            else:
                kurz_usd_czk = 1.0
            
            historie = yf.Ticker(ticker_symbol).history(period="1mo")['Close']
            historie_czk = historie * kurz_usd_czk
            aktualni_cena = round(float(historie_czk.iloc[-1]), 2)
            
            st.markdown(f"### **{vybrane_aktivum}** — `< {aktualni_cena:.2f} Kč / ks >`", unsafe_allow_html=True)
            st.line_chart(historie_czk)
            
            je_krypto = vybrane_aktivum in ["Bitcoin", "Ethereum"]
            if je_krypto:
                st.caption("💡 Kryptoměny lze nakupovat i po malých částech (např. 0.005 ks).")
                krok_formulare = 0.001
                format_cisla = "%.4f"
            else:
                krok_formulare = 1.0
                format_cisla = "%.2f"
            
            stav_aktiva_ted = bezpecny_float(moje_data.get(sloupec_db, 0)) if moje_data else 0.0

            col_nakup, col_prodej = st.columns(2)
            
            with col_nakup:
                st.write("#### 🛒 Nákup")
                pocet_koupit = st.number_input("Počet ks", min_value=0.0, step=krok_formulare, format=format_cisla, value=0.0, key="nakup_in")
                cena_koupit = round(pocet_koupit * aktualni_cena, 2)
                st.write(f"Celkem: `{cena_koupit:.2f} Kč`")
                
                if st.button("KOUPIT ➔", use_container_width=True, key="btn_koupit_act"):
                    if pocet_koupit > 0:
                        if st.session_state["zustatek"] >= cena_koupit:
                            with st.spinner("Zpracovávám příkaz..."):
                                novy_zustatek = round(st.session_state["zustatek"] - cena_koupit, 2)
                                novy_stav_aktiva = round(stav_aktiva_ted + pocet_koupit, 4)
                                
                                nicky_sloupec = [str(n).strip() for n in db_uzivatele.col_values(2)]
                                cislo_radku = nicky_sloupec.index(st.session_state["nick"]) + 1
                                hlavicky = db_uzivatele.row_values(1)
                                cislo_sloupce_aktiva = hlavicky.index(sloupec_db) + 1
                                cislo_sloupce_zustatek = hlavicky.index("Zustatek") + 1
                                
                                db_uzivatele.update_cell(cislo_radku, cislo_sloupce_zustatek, novy_zustatek) 
                                db_uzivatele.update_cell(cislo_radku, cislo_sloupce_aktiva, novy_stav_aktiva)
                                
                                if db_transakce:
                                    try:
                                        cas_ted = datetime.now().strftime("%d.%m.%Y %H:%M")
                                        db_transakce.append_row([cas_ted, st.session_state["nick"], "NÁKUP", vybrane_aktivum, pocet_koupit, cena_koupit])
                                    except Exception:
                                        pass
                                
                                st.session_state["zustatek"] = novy_zustatek
                                st.success("✅ Nákup proveden!")
                                st.rerun()
                        else:
                            st.error("❌ Nedostatek prostředků.")
            
            with col_prodej:
                st.write("#### 💰 Prodej")
                st.write(f"Vlastníš: `{hezke_kusy(stav_aktiva_ted)} ks`")
                pocet_prodat = st.number_input("Počet ks k prodeji", min_value=0.0, max_value=float(stav_aktiva_ted) if stav_aktiva_ted > 0 else 0.0, step=krok_formulare, format=format_cisla, value=0.0, key="prodej_in")
                cena_prodat = round(pocet_prodat * aktualni_cena, 2)
                st.write(f"Získáš: `{cena_prodat:.2f} Kč`")
                
                if st.button("PRODAT ➔", use_container_width=True, key="btn_prodat_act"):
                    if pocet_prodat > 0 and pocet_prodat <= stav_aktiva_ted:
                        with st.spinner("Zpracovávám příkaz..."):
                            novy_zustatek = round(st.session_state["zustatek"] + cena_prodat, 2)
                            novy_stav_aktiva = round(stav_aktiva_ted - pocet_prodat, 4)
                            
                            nicky_sloupec = [str(n).strip() for n in db_uzivatele.col_values(2)]
                            cislo_radku = nicky_sloupec.index(st.session_state["nick"]) + 1
                            hlavicky = db_uzivatele.row_values(1)
                            cislo_sloupce_aktiva = hlavicky.index(sloupec_db) + 1
                            cislo_sloupce_zustatek = hlavicky.index("Zustatek") + 1
                            
                            db_uzivatele.update_cell(cislo_radku, cislo_sloupce_zustatek, novy_zustatek)
                            db_uzivatele.update_cell(cislo_radku, cislo_sloupce_aktiva, novy_stav_aktiva)
                            
                            if db_transakce:
                                try:
                                    cas_ted = datetime.now().strftime("%d.%m.%Y %H:%M")
                                    db_transakce.append_row([cas_ted, st.session_state["nick"], "PRODEJ", vybrane_aktivum, pocet_prodat, cena_prodat])
                                except Exception:
                                    pass
                            
                            st.session_state["zustatek"] = novy_zustatek
                            st.success("✅ Prodej proveden!")
                            st.rerun()

        except Exception as e:
            st.warning(f"Chyba při stahování dat: {e}")

# ==========================================
# --- A: OBRAZOVKA PRO NEPŘIHLÁŠENÉ ---
# ==========================================
if not st.session_state["prihlasen"]:
    st.markdown("<h1 style='text-align: center; color: #0F172A; margin-bottom: 5px;'>📈 Školní Investiční Simulátor</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #44403C; font-size: 1.05rem; margin-bottom: 30px;'>Vyzkoušej si obchodování na reálné burze bez rizika ztráty peněz</p>", unsafe_allow_html=True)

    col_left, col_main, col_right = st.columns([1, 2, 1])

    with col_main:
        tab1, tab2 = st.tabs(["🔐 Přihlášení", "📝 Nová registrace"])

        with tab1:
            st.write("")
            login_nick = st.text_input("Přezdívka (Nick / Login):", key="login_nick_in").strip()
            login_pin = st.text_input("PIN (4 čísla):", type="password", max_chars=4, key="login_pin_in").strip()
            st.write("")
            
            if st.button("PŘIHLÁSIT SE ➔", use_container_width=True):
                if login_nick and login_pin:
                    zaznamy = db_uzivatele.get_all_records(value_render_option="UNFORMATTED_VALUE")
                    nalezen = False
                    for radek in zaznamy:
                        if str(radek.get("Nick", "")).strip().lower() == login_nick.lower() and str(radek.get("PIN", "")).strip() == login_pin:
                            nalezen = True
                            st.session_state["prihlasen"] = True
                            st.session_state["nick"] = str(radek.get("Nick", "")).strip()
                            st.session_state["jmeno"] = str(radek.get("Jmeno", "")).strip()
                            st.session_state["role"] = str(radek.get("Role", "ZAK")).upper()
                            st.session_state["trida"] = str(radek.get("Trida", "")).strip().upper()
                            st.session_state["zustatek"] = bezpecny_float(radek.get("Zustatek", 0))
                            st.rerun()
                    if not nalezen:
                        st.error("❌ Chybná přezdívka nebo PIN.")
                else:
                    st.warning("⚠️ Vyplň přezdívku i PIN.")

        with tab2:
            st.write("")
            reg_nick = st.text_input("Přezdívka (Nick pro přihlášení):", key="reg_nick_in").strip()
            reg_jmeno = st.text_input("Celé jméno a příjmení:", key="reg_jmeno_in").strip()
            je_ucitel = st.checkbox("👩‍🏫 Účet pro UČITELE")
            
            if je_ucitel:
                reg_trida = ""
                tajny_kod_input = st.text_input("🔐 Učitelské heslo:", type="password", key="reg_pass_in")
            else:
                reg_trida = st.text_input("Třída žáka (např. 8.A, 9.B):", key="reg_trida_in").strip().upper()
                tajny_kod_input = ""
                
            reg_pin = st.text_input("Vymysli si osobní PIN (4 čísla):", type="password", max_chars=4, help="Zadej přesně 4 číslice, např. 1234", key="reg_pin_in").strip()
            st.write("")

            if st.button("VYTVOŘIT ÚČET ➔", use_container_width=True):
                zadane_heslo_ciste = tajny_kod_input.strip().strip('"').strip("'")
                heslo_ze_secrets = str(st.secrets.get("ucitelske_heslo", "Ucitel2026")).strip().strip('"').strip("'")
                povolena_hesla = [heslo_ze_secrets, "Ucitel2026", "Ucitel123"]
                
                if not reg_nick or not reg_jmeno or not reg_pin or (not je_ucitel and not reg_trida):
                    st.warning("⚠️ Vyplň prosím všechny potřebné údaje.")
                elif not (reg_pin.isdigit() and len(reg_pin) == 4):
                    st.error("❌ PIN musí mít přesně 4 číslice.")
                elif je_ucitel and zadane_heslo_ciste not in povolena_hesla:
                    st.error("❌ Nesprávné učitelské heslo.")
                else:
                    zaznamy = db_uzivatele.get_all_records(value_render_option="UNFORMATTED_VALUE")
                    existujici_nicky = [str(r.get("Nick", "")).strip().lower() for r in zaznamy]
                    
                    if reg_nick.lower() in existujici_nicky:
                        st.error("⚠️ Tato přezdívka je již zabraná. Zvol si jinou.")
                    else:
                        role_str = "UCITEL" if je_ucitel else "ZAK"
                        db_uzivatele.append_row([role_str, reg_nick, reg_jmeno, reg_trida, reg_pin, 20000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
                        st.success("🎉 Účet úspěšně vytvořen! Nyní se přihlaš.")

# ==========================================
# --- B: OBRAZOVKA PRO UČITELE / DEMO ---
# ==========================================
elif st.session_state["role"] == "UCITEL":
    sloupec1, sloupec2 = st.columns([3, 1])
    with sloupec1:
        st.markdown("<h2 style='color: #0F172A;'>👩‍🏫 Učitelský Panel & Simulátor</h2>", unsafe_allow_html=True)
        st.write(f"Učitel / Demo: **{st.session_state['jmeno']}** | Nick: `{st.session_state['nick']}`")
    with sloupec2:
        st.write("")
        if st.button("🚪 ODHLÁSIT", use_container_width=True):
            st.session_state["prihlasen"] = False
            st.rerun()

    st.divider()
    
    vsechna_data = db_uzivatele.get_all_records(value_render_option="UNFORMATTED_VALUE")
    moje_data = next((r for r in vsechna_data if str(r.get("Nick", "")).strip().lower() == st.session_state["nick"].lower()), None)

    # HLAVNÍ PŘEPÍNAČ MEZI PŘEHLEDEM TŘÍDY A VLASTNÍM SIMULÁTOREM
    hlavni_tab1, hlavni_tab2 = st.tabs(["👩‍🏫 Přehled tříd a výsledky", "📈 Moje obchodování na burze"])
    
    with hlavni_tab1:
        trida_raw = str(st.session_state.get("trida") or "")
        moje_ulozene_tridy = [t.strip().upper() for t in trida_raw.split(",") if t.strip()]
        
        is_demo = st.session_state["nick"].lower() in ["demo.nakladatel", "nakladatel"]
        
        if not is_demo:
            with st.expander("⚙️ Spravovat moje výukové třídy"):
                st.info("Zadejte názvy tříd přesně tak, jak je žáci zadávají při registraci.")
                nove_tridy_input = st.text_input("Moje třídy (oddělujte čárkou, např. 1A, 4.B):", value=", ".join(moje_ulozene_tridy))
                if st.button("Uložit výukové třídy"):
                    nove_tridy_str = nove_tridy_input.strip().upper()
                    nicky_sloupec = [str(n).strip() for n in db_uzivatele.col_values(2)]
                    cislo_radku = nicky_sloupec.index(st.session_state["nick"]) + 1
                    hlavicky = db_uzivatele.row_values(1)
                    cislo_sloupce_trida = hlavicky.index("Trida") + 1
                    
                    db_uzivatele.update_cell(cislo_radku, cislo_sloupce_trida, nove_tridy_str)
                    st.session_state["trida"] = nove_tridy_str
                    st.success("✅ Třídy uloženy!")
                    st.rerun()

        # Ukázková třída pro nakladatele
        tridy_k_zobrazeni = ["Ukázková třída"] if is_demo else moje_ulozene_tridy
        
        if not tridy_k_zobrazeni:
            st.warning("Zatím nemáte přiřazené žádné třídy. Můžete si je přidat v nastavení výše.")
        else:
            vybrana_trida = st.selectbox("🎯 Vybraná třída:", tridy_k_zobrazeni)
            
            tab_zebricek_ucitel, tab_detail_zaka, tab_sprava_ucitel = st.tabs(["🏆 Výsledky třídy", "🔍 Detail & Historie žáka", "🔑 Správa PINů"])
            
            with tab_zebricek_ucitel:
                with st.spinner(f"Načítám aktuální data trhu pro {vybrana_trida}..."):
                    try:
                        kurz_usd = yf.Ticker("CZK=X").history(period="1d")['Close'].iloc[-1]
                        ceny_aktiv = {}
                        for nazev, (ticker, mena, _) in AKTIVA.items():
                            c = yf.Ticker(ticker).history(period="1d")['Close'].iloc[-1]
                            if mena == "USD":
                                c *= kurz_usd
                            ceny_aktiv[nazev] = c
                        
                        zebricek_data = []
                        zaci_tridy = [r for r in vsechna_data if str(r.get("Trida", "")).strip().upper() == vybrana_trida.upper() and str(r.get("Role", "")).upper() != "UCITEL"]
                        
                        for radek in zaci_tridy:
                            jmeno_zaka = str(radek.get("Jmeno", ""))
                            nick_zaka = str(radek.get("Nick", ""))
                            if not jmeno_zaka and not nick_zaka:
                                continue
                            
                            zustatek_zaka = bezpecny_float(radek.get("Zustatek", 0))
                            majetek_zaka = zustatek_zaka
                            
                            for nazev, (_, _, db_sloupec) in AKTIVA.items():
                                ks = bezpecny_float(radek.get(db_sloupec, 0))
                                if ks > 0 and nazev in ceny_aktiv:
                                    majetek_zaka += (ks * ceny_aktiv[nazev])
                            
                            zisk_zaka = majetek_zaka - 20000.0
                            zebricek_data.append({
                                "Žák": f"{jmeno_zaka} ({nick_zaka})",
                                "Celkový majetek": round(majetek_zaka, 2),
                                "Zisk / Ztráta": round(zisk_zaka, 2),
                                "Hotovost": round(zustatek_zaka, 2)
                            })
                        
                        if zebricek_data:
                            df_zebricek = pd.DataFrame(zebricek_data)
                            df_zebricek = df_zebricek.sort_values(by="Celkový majetek", ascending=False).reset_index(drop=True)
                            df_zebricek.index += 1
                            
                            df_styled = df_zebricek.style.map(barva_zisku_ztraty, subset=["Zisk / Ztráta"]).format({
                                "Celkový majetek": "{:.2f} Kč",
                                "Zisk / Ztráta": "{:+.2f} Kč",
                                "Hotovost": "{:.2f} Kč"
                            })
                            st.dataframe(df_styled, use_container_width=True)
                        else:
                            st.info(f"Ve třídě {vybrana_trida} zatím nejsou zaregistrovaní žáci.")
                    except Exception as e:
                        st.error(f"Chyba při načítání dat: {e}")

            with tab_detail_zaka:
                zaci_v_tride_seznam = [r for r in vsechna_data if str(r.get("Trida", "")).strip().upper() == vybrana_trida.upper() and str(r.get("Role", "")).upper() != "UCITEL"]
                
                if zaci_v_tride_seznam:
                    zaci_moznosti = [f"{str(r.get('Jmeno', ''))} ({str(r.get('Nick', ''))})" for r in zaci_v_tride_seznam]
                    vybrany_zak_opt = st.selectbox("Vyber žáka k náhledu:", zaci_moznosti, key="detail_zak_select")
                    
                    vybrany_nick = vybrany_zak_opt.split("(")[-1].replace(")", "").strip()
                    data_zaka = next((r for r in zaci_v_tride_seznam if str(r.get("Nick", "")).strip().lower() == vybrany_nick.lower()), None)
                    
                    if data_zaka:
                        st.write(f"### 💼 Portfolio žáka: **{data_zaka.get('Jmeno', '')}**")
                        zustatek = bezpecny_float(data_zaka.get("Zustatek", 0))
                        st.write(f"💵 **Volná hotovost:** `{zustatek:.2f} Kč`")
                        
                        st.write("**Držená aktiva:**")
                        vlastni_aktiva = False
                        for nazev, (_, _, db_sloupec) in AKTIVA.items():
                            ks = bezpecny_float(data_zaka.get(db_sloupec, 0))
                            if ks > 0:
                                vlastni_aktiva = True
                                st.write(f"⚡ **{nazev}**: `{hezke_kusy(ks)} ks`")
                        
                        if not vlastni_aktiva:
                            st.caption("Žák momentálně nedrží žádná aktiva.")
                        
                        st.divider()
                        st.write(f"### 📜 Historie obchodů (`{vybrany_nick}`)")
                        if db_transakce:
                            try:
                                vsechny_transakce = db_transakce.get_all_records(value_render_option="UNFORMATTED_VALUE")
                                transakce_zaka = []
                                jmeno_zaka_full = str(data_zaka.get('Jmeno', '')).strip().lower()
                                
                                for t in vsechny_transakce:
                                    user_in_t = str(t.get("Nick", t.get("Jmeno", ""))).strip().lower()
                                    if user_in_t in [vybrany_nick.lower(), jmeno_zaka_full]:
                                        transakce_zaka.append({
                                            "Čas": str(t.get("Cas", "")),
                                            "Typ": str(t.get("Typ", "")),
                                            "Aktivum": str(t.get("Aktivum", "")),
                                            "Kusů": hezke_kusy(bezpecny_float(t.get("Kusu", 0))),
                                            "Celková cena": f"{bezpecny_float(t.get('Cena_CZK', 0)):.2f} Kč"
                                        })
                                
                                if transakce_zaka:
                                    df_t_clean = pd.DataFrame(transakce_zaka)
                                    st.dataframe(df_t_clean, use_container_width=True)
                                else:
                                    st.info("Žák zatím neprovedl žádné obchody.")
                            except Exception as e:
                                st.warning(f"Nelze načíst historii: {e}")
                else:
                    st.info(f"Ve třídě {vybrana_trida} zatím nejsou žádní žáci.")

            with tab_sprava_ucitel:
                st.write("### 🔑 Obnovení PINu žáka")
                zaci_v_tride = [f"{str(r.get('Jmeno', ''))} ({str(r.get('Nick', ''))})" for r in vsechna_data if str(r.get("Trida", "")).strip().upper() == vybrana_trida.upper() and str(r.get("Role", "")).upper() != "UCITEL"]
                
                if zaci_v_tride:
                    vybrany_zak_str = st.selectbox("Vyber žáka:", zaci_v_tride)
                    novy_pin = st.text_input("Nový 4místný PIN:", value="1234", max_chars=4)
                    
                    if st.button("Uložit nový PIN"):
                        if novy_pin.isdigit() and len(novy_pin) == 4:
                            vybrany_nick = vybrany_zak_str.split("(")[-1].replace(")", "").strip()
                            nicky_sloupec = [str(n).strip() for n in db_uzivatele.col_values(2)]
                            cislo_radku = nicky_sloupec.index(vybrany_nick) + 1
                            hlavicky = db_uzivatele.row_values(1)
                            cislo_sloupce_pin = hlavicky.index("PIN") + 1
                            
                            db_uzivatele.update_cell(cislo_radku, cislo_sloupce_pin, str(novy_pin))
                            st.success(f"✅ PIN změněn pro {vybrany_zak_str}!")
                        else:
                            st.error("❌ PIN musí mít 4 číslice.")

    with hlavni_tab2:
        st.write("### 📈 Vyzkoušejte si obchodování jako žák")
        vykresli_obchodovani_burzu(moje_data)

# ==========================================
# --- C: OBRAZOVKA PRO ŽÁKY ---
# ==========================================
else:
    sloupec1, sloupec2 = st.columns([3, 1])
    with sloupec1:
        st.markdown(f"<h2 style='color: #0F172A;'>Vítej, {st.session_state['jmeno']}! ⚡</h2>", unsafe_allow_html=True)
        st.write(f"Nick: `{st.session_state['nick']}` | Třída: **{st.session_state['trida']}**")
    with sloupec2:
        st.write("")
        if st.button("🚪 ODHLÁSIT", use_container_width=True):
            st.session_state["prihlasen"] = False
            st.rerun()

    st.divider()
    tab_burza, tab_portfolio, tab_zebricek = st.tabs(["📈 Burza & Trh", "💼 Moje Portfolio", "🏆 Žebříček"])
    
    vsechna_data = db_uzivatele.get_all_records(value_render_option="UNFORMATTED_VALUE")
    moje_data = next((r for r in vsechna_data if str(r.get("Nick", "")).strip().lower() == st.session_state["nick"].lower()), None)
    
    # ---------------- ZÁLOŽKA 1: BURZA ----------------
    with tab_burza:
        vykresli_obchodovani_burzu(moje_data)

    # ---------------- ZÁLOŽKA 2: PORTFOLIO ----------------
    with tab_portfolio:
        if moje_data:
            with st.spinner("Oceňuji majetek podle živých dat..."):
                try:
                    kurz_usd_czk = yf.Ticker("CZK=X").history(period="1d")['Close'].iloc[-1]
                except Exception:
                    kurz_usd_czk = 23.0 
                
                hodnota_aktiv_celkem = 0.0
                ma_neco = False
                graf_data = {"Položka": ["Hotovost"], "Hodnota (Kč)": [st.session_state["zustatek"]]}
                
                st.write("### 💼 Přehled vlastněných aktiv")
                
                for nazev, (ticker_symbol, mena, db_sloupec) in AKTIVA.items():
                    mnozstvi = bezpecny_float(moje_data.get(db_sloupec, 0))
                    if mnozstvi > 0:
                        ma_neco = True
                        try:
                            cena_aktiva = yf.Ticker(ticker_symbol).history(period="1d")['Close'].iloc[-1]
                            if mena == "USD":
                                cena_aktiva *= kurz_usd_czk
                                
                            hodnota_polozky = round(mnozstvi * cena_aktiva, 2)
                            hodnota_aktiv_celkem += hodnota_polozky
                            
                            graf_data["Položka"].append(nazev)
                            graf_data["Hodnota (Kč)"].append(hodnota_polozky)
                            
                            st.write(f"⚡ **{nazev}**: `{hezke_kusy(mnozstvi)} ks` — *(hodnota cca {hodnota_polozky:.2f} Kč)*")
                        except Exception:
                            st.write(f"⚡ **{nazev}**: `{hezke_kusy(mnozstvi)} ks`")
                
                if not ma_neco:
                    st.info("Zatím nevlastníš žádná aktiva.")
                
                st.divider()
                celkovy_majetek = round(st.session_state["zustatek"] + hodnota_aktiv_celkem, 2)
                zisk_ztrata = round(celkovy_majetek - 20000.0, 2)
                
                st.metric(
                    label="🏆 CELKOVÁ HODNOTA PORTFOLIA", 
                    value=f"{celkovy_majetek:.2f} Kč", 
                    delta=f"{zisk_ztrata:.2f} Kč od začátku"
                )
                
                if ma_neco:
                    st.divider()
                    st.write("### 📊 Struktura majetku")
                    df_graf = pd.DataFrame(graf_data)
                    
                    fig = px.pie(df_graf, values="Hodnota (Kč)", names="Položka", hole=0.5)
                    
                    fig.update_layout(
                        paper_bgcolor="rgba(0,0,0,0)",
                        plot_bgcolor="rgba(0,0,0,0)",
                        font=dict(color="#0F172A", family="Montserrat", size=14),
                        legend=dict(font=dict(color="#0F172A")),
                        colorway=["#111111", "#8AA2B6", "#8DAE93", "#D8C397", "#B4A2B8"]
                    )
                    fig.update_traces(textposition='outside', textinfo='percent+label')
                    
                    st.plotly_chart(fig, use_container_width=True)
                
                st.divider()
                st.write("### 📜 Moje historie obchodů")
                if db_transakce:
                    try:
                        vsechny_transakce = db_transakce.get_all_records(value_render_option="UNFORMATTED_VALUE")
                        moje_transakce = []
                        moje_jmeno_full = str(moje_data.get('Jmeno', '')).strip().lower()
                        
                        for t in vsechny_transakce:
                            user_in_t = str(t.get("Nick", t.get("Jmeno", ""))).strip().lower()
                            if user_in_t in [st.session_state["nick"].lower(), moje_jmeno_full]:
                                moje_transakce.append({
                                    "Čas": str(t.get("Cas", "")),
                                    "Typ": str(t.get("Typ", "")),
                                    "Aktivum": str(t.get("Aktivum", "")),
                                    "Kusů": hezke_kusy(bezpecny_float(t.get("Kusu", 0))),
                                    "Celková cena": f"{bezpecny_float(t.get('Cena_CZK', 0)):.2f} Kč"
                                })
                        
                        if moje_transakce:
                            df_transakce = pd.DataFrame(moje_transakce)
                            st.dataframe(df_transakce, use_container_width=True)
                        else:
                            st.caption("Zatím jsi neprovedl(a) žádné obchody.")
                    except Exception:
                        st.caption("Historii obchodů se nepodařilo načíst.")

    # ---------------- ZÁLOŽKA 3: ŽEBŘÍČEK ŽÁKA ----------------
    with tab_zebricek:
        moje_trida = st.session_state["trida"]
        st.write(f"### 🏆 Žebříček třídy **{moje_trida}**")
        
        with st.spinner("Sestavuji pořadí..."):
            try:
                kurz_usd = yf.Ticker("CZK=X").history(period="1d")['Close'].iloc[-1]
                ceny_aktiv = {}
                for nazev, (ticker, mena, _) in AKTIVA.items():
                    c = yf.Ticker(ticker).history(period="1d")['Close'].iloc[-1]
                    if mena == "USD":
                        c *= kurz_usd
                    ceny_aktiv[nazev] = c
                
                zebricek_data = []
                zaci_tridy = [r for r in vsechna_data if str(r.get("Trida", "")).strip().upper() == moje_trida.upper() and str(r.get("Role", "")).upper() != "UCITEL"]
                
                for radek in zaci_tridy:
                    jmeno_zaka = str(radek.get("Jmeno", ""))
                    nick_zaka = str(radek.get("Nick", ""))
                    if not jmeno_zaka and not nick_zaka:
                        continue
                    
                    zustatek_zaka = bezpecny_float(radek.get("Zustatek", 0))
                    majetek_zaka = zustatek_zaka
                    
                    for nazev, (_, _, db_sloupec) in AKTIVA.items():
                        ks = bezpecny_float(radek.get(db_sloupec, 0))
                        if ks > 0 and nazev in ceny_aktiv:
                            majetek_zaka += (ks * ceny_aktiv[nazev])
                    
                    zisk_zaka = majetek_zaka - 20000.0
                    zebricek_data.append({
                        "Žák": f"{jmeno_zaka} ({nick_zaka})",
                        "Celkový majetek": round(majetek_zaka, 2),
                        "Zisk / Ztráta": round(zisk_zaka, 2)
                    })
                
                if zebricek_data:
                    df_zebricek = pd.DataFrame(zebricek_data)
                    df_zebricek = df_zebricek.sort_values(by="Celkový majetek", ascending=False).reset_index(drop=True)
                    df_zebricek.index += 1
                    
                    df_styled = df_zebricek.style.map(barva_zisku_ztraty, subset=["Zisk / Ztráta"]).format({
                        "Celkový majetek": "{:.2f} Kč",
                        "Zisk / Ztráta": "{:+.2f} Kč"
                    })
                    st.dataframe(df_styled, use_container_width=True)
                else:
                    st.info("V tvé třídě zatím nikdo jiný není.")
                
            except Exception as e:
                st.error(f"Chyba při sestavování žebříčku: {e}")
