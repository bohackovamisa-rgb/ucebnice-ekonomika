import streamlit as st
import math

# --- 1. KONFIGURACE STRÁNKY ---
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
            st.markdown("<h2 style='text-align: center; border: none; font-weight: 700; margin-bottom: 0;'>Soukromá učebnice</h2>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; color: #64748b; font-size: 0.85rem; margin-bottom: 1.5rem;'>Zadejte přístupové heslo pro odemknutí kurzu.</p>", unsafe_allow_html=True)
            password = st.text_input("Heslo:", type="password", label_visibility="collapsed", placeholder="Přístupové heslo...")
            if st.button("Vstoupit do učebnice", use_container_width=True):
                if password == app_pwd:
                    st.session_state["password_correct"] = True
                    st.rerun()
                else:
                    st.error("Nesprávné heslo")
    return False

if not check_password():
    st.stop()

# --- STYLOVÁNÍ (PREMIUM SAAS MINIMALISMUS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800&display=swap');
    html, body, [class*="css"] { font-family: 'Montserrat', -apple-system, sans-serif !important; }
    .stApp { background-color: #f8fafc; color: #0f172a; }
    .main .block-container { max-width: 940px !important; padding-top: 2rem !important; padding-bottom: 5rem !important; }
    div[data-testid="stVerticalBlockBorderWrapper"] { background-color: #ffffff !important; border-radius: 12px !important; border: 1px solid #e2e8f0 !important; box-shadow: 0 1px 3px 0 rgba(15, 23, 42, 0.03), 0 1px 2px 0 rgba(15, 23, 42, 0.02) !important; padding: 1.75rem !important; margin-bottom: 1.25rem !important; transition: border-color 0.2s ease, box-shadow 0.2s ease; }
    div[data-testid="stVerticalBlockBorderWrapper"]:hover { border-color: #cbd5e1 !important; box-shadow: 0 4px 12px -2px rgba(15, 23, 42, 0.05) !important; }
    h1 { font-family: 'Montserrat', sans-serif !important; color: #0f172a !important; font-weight: 800 !important; font-size: 2.1rem !important; letter-spacing: -0.025em !important; line-height: 1.25 !important; margin-bottom: 0.5rem !important; }
    h2 { font-family: 'Montserrat', sans-serif !important; color: #1e293b !important; font-weight: 700 !important; font-size: 1.25rem !important; letter-spacing: -0.015em !important; margin-top: 1.25rem !important; margin-bottom: 0.75rem !important; border-bottom: 1px solid #f1f5f9; padding-bottom: 0.5rem; }
    h3 { font-family: 'Montserrat', sans-serif !important; color: #334155 !important; font-weight: 600 !important; font-size: 1.05rem !important; margin-top: 1.25rem !important; }
    p, li, td, th { font-family: 'Montserrat', sans-serif !important; color: #334155; font-size: 0.94rem; line-height: 1.7; font-weight: 400; }
    .hero-badge { background: #e0e7ff; color: #4338ca; font-size: 0.72rem; font-weight: 700; padding: 0.3rem 0.8rem; border-radius: 20px; text-transform: uppercase; letter-spacing: 0.08em; display: inline-block; margin-bottom: 0.8rem; }
    .box-blue { background-color: #f0f9ff; border-left: 4px solid #0284c7; padding: 1.1rem 1.3rem; border-radius: 0 8px 8px 0; margin: 1rem 0; color: #0f172a; font-size: 0.93rem; }
    .box-yellow { background-color: #fefce8; border-left: 4px solid #eab308; padding: 1.1rem 1.3rem; border-radius: 0 8px 8px 0; margin: 1rem 0; color: #0f172a; font-size: 0.93rem; }
    .box-purple { background-color: #faf5ff; border-left: 4px solid #a855f7; padding: 1.1rem 1.3rem; border-radius: 0 8px 8px 0; margin: 1rem 0; color: #0f172a; font-size: 0.93rem; word-wrap: break-word; }
    .box-green { background-color: #f0fdf4; border-left: 4px solid #22c55e; padding: 1.1rem 1.3rem; border-radius: 0 8px 8px 0; margin: 1rem 0; color: #0f172a; font-size: 0.93rem; }
    .box-red { background-color: #fef2f2; border-left: 4px solid #ef4444; padding: 1.1rem 1.3rem; border-radius: 0 8px 8px 0; margin: 1rem 0; color: #0f172a; font-size: 0.93rem; }
    .box-gray { background-color: #f8fafc; border-left: 4px solid #64748b; padding: 1.1rem 1.3rem; border-radius: 0 8px 8px 0; margin: 1rem 0; color: #0f172a; font-size: 0.93rem; }
    .stTextInput input, .stTextArea textarea, .stSelectbox select { font-family: 'Montserrat', sans-serif !important; border-radius: 8px !important; border: 1px solid #cbd5e1 !important; background-color: #ffffff !important; color: #0f172a !important; font-size: 0.9rem !important; padding: 0.65rem 0.9rem !important; }
    .stButton > button { font-family: 'Montserrat', sans-serif !important; border-radius: 8px !important; border: 1px solid #cbd5e1 !important; background-color: #ffffff !important; color: #0f172a !important; font-weight: 600 !important; font-size: 0.88rem !important; padding: 0.55rem 1.1rem !important; box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.04) !important; transition: all 0.15s ease !important; }
    .stButton > button:hover { border-color: #4f46e5 !important; color: #4f46e5 !important; background-color: #f5f3ff !important; }
    section[data-testid="stSidebar"] { background-color: #ffffff !important; border-right: 1px solid #e2e8f0 !important; }
    .sidebar-section-title { font-size: 0.7rem; font-weight: 700; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.08em; margin-top: 1.4rem; margin-bottom: 0.5rem; }
    .sub-section-header { color: #4f46e5; font-weight: 700; font-size: 0.85rem; letter-spacing: 0.05em; text-transform: uppercase; }
    
    /* LEGENDA CSS */
    .legend-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(270px, 1fr)); gap: 12px; margin-top: 12px; }
    .legend-card { padding: 12px 16px; border-radius: 8px; font-size: 0.9rem; display: flex; align-items: center; gap: 12px; border: 1px solid rgba(0,0,0,0.04); }
    .badge-dot { width: 12px; height: 12px; border-radius: 50%; flex-shrink: 0; }
    </style>
""", unsafe_allow_html=True)

# --- NAVIGAČNÍ STAV ---
if "current_view" not in st.session_state:
    st.session_state["current_view"] = "Uvod"

# --- BOČNÍ PANEL ---
with st.sidebar:
    st.markdown("""
        <div style='padding: 0.5rem 0 0.5rem 0;'>
            <span style='font-size: 0.7rem; font-weight: 700; color: #6366f1; text-transform: uppercase; letter-spacing: 0.08em;'>E-Learning Portal</span>
            <h2 style='margin: 0; padding: 0; border: none; font-size: 1.25rem; color: #0f172a; font-weight: 800;'>Učebnice Ekonomiky</h2>
        </div>
    """, unsafe_allow_html=True)
    
    st.divider()

    # ÚVODNÍ STRÁNKA
    is_uvod = st.session_state["current_view"] == "Uvod"
    if st.button("Úvodní stránka", key="nav_uvod", use_container_width=True, type="primary" if is_uvod else "secondary"):
        st.session_state["current_view"] = "Uvod"
        st.rerun()

    # KAPITOLY KURZU
    st.markdown("<div class='sidebar-section-title'>KAPITOLY KURZU</div>", unsafe_allow_html=True)
    chapters = {
        "Kapitola 1": "1. Podnikavost a startupy",
        "Kapitola 2": "2. Finance a osobní management",
        "Kapitola 3": "3. Výroba, náklady a efektivita",
        "Kapitola 4": "4. Zaměstnanci a trh práce",
        "Kapitola 5": "5. Stát, daně a ekonomika",
        "Kapitola 6": "6. Management a marketing"
    }

    for key, title in chapters.items():
        is_active = st.session_state["current_view"] == key
        btn_type = "primary" if is_active else "secondary"
        if st.button(title, key=f"nav_{key}", use_container_width=True, type=btn_type):
            st.session_state["current_view"] = key
            st.rerun()

    # OSOBNÍ A METODICKÁ ZÓNA
    st.markdown("<div class='sidebar-section-title'>STUDIUM A METODIKA</div>", unsafe_allow_html=True)
    
    is_pokroky = st.session_state["current_view"] == "Pokroky"
    if st.button("Moje pokroky", key="nav_pokroky", use_container_width=True, type="primary" if is_pokroky else "secondary"):
        st.session_state["current_view"] = "Pokroky"
        st.rerun()

    is_ucitel = st.session_state["current_view"] == "Ucitel"
    if st.button("Učitelská základna", key="nav_ucitel", use_container_width=True, type="primary" if is_ucitel else "secondary"):
        st.session_state["current_view"] = "Ucitel"
        st.rerun()

    st.divider()
    
    if st.button("Odhlásit se", use_container_width=True):
        st.session_state["password_correct"] = False
        st.rerun()

# --- HLAVNÍ OBSAHOVÁ PLOCHA ---
view = st.session_state["current_view"]

# ==========================================
# ÚVODNÍ STRÁNKA
# ==========================================
if view == "Uvod":
    st.markdown("<span class='hero-badge'>Digitální Učebnice</span>", unsafe_allow_html=True)
    st.title("Ekonomika, která dává smysl")
    st.markdown("<p style='font-size: 1.05rem; color: #64748b; margin-bottom: 2rem;'>Moderní učebnice ekonomiky pro střední školy: Podnikavost, finance & ekonomika v souvislostech.</p>", unsafe_allow_html=True)

    with st.container(border=True):
        st.markdown("## Začni tady")
        st.write("""
        Tahle stránka je hlavní rozcestník učebnice. Najdeš tu obsah, pravidla práce, výstupy kapitol, 
        společné nástroje a odkaz do učitelského řídícího centra. Propojuje podnikavost, osobní finance, výrobu, 
        trh práce, stát, daně, management a marketing s rozhodnutími z reálného života.
        """)
        
        st.markdown("""
        <div class='box-green'>
            <strong>Cíl učebnice:</strong><br>
            Žák má umět propojit nápad, zákazníka, peníze, práci, stát, daně, marketing, rizika a odpovědnost do jednoho praktického rozhodování.
        </div>
        """, unsafe_allow_html=True)

    with st.container(border=True):
        st.markdown("## Jak s učebnicí pracovat")
        st.markdown("""
        1. **Otevři kapitolu z obsahu.** Nejprve si projdi úvod, rychlou orientaci a cíle kapitoly.
        2. **Čti po menších blocích.** Každá kapitola je členěná na výklad, příklady, tabulky, aktivity a reflexi.
        3. **Plň průběžné úkoly.** Žluté bloky slouží jako pracovní úkoly, otázky a aktivity.
        4. **Používej AI mentoring.** Fialové bloky obsahují prompty, které pomáhají s vysvětlením, kontrolou nebo rozvojem vlastního projektu.
        5. **Na konci kapitoly udělej reflexi.** Shrň, co už chápeš, co ještě potřebuješ dovysvětlit a jak bys téma použil/a v praxi.
        6. **V závěrečném projektu propojíš všechno dohromady.** Výstupem učebnice je návrh odpovědného ekonomického nebo podnikatelského projektu.
        """)

    with st.container(border=True):
        st.markdown("## 🎨 Legenda učebnice")
        st.write("Barevné odlišení v textu ti pomůže okamžitě rozpoznat typ obsahu:")

        st.markdown("""
        <div class="legend-grid">
            <div class="legend-card" style="background: #f0f9ff; border-left: 4px solid #0284c7;">
                <span class="badge-dot" style="background: #0284c7;"></span>
                <div><strong style="color: #0369a1;">Modrá:</strong> Výklad, struktura, důležité vysvětlení</div>
            </div>
            <div class="legend-card" style="background: #fefce8; border-left: 4px solid #eab308;">
                <span class="badge-dot" style="background: #eab308;"></span>
                <div><strong style="color: #854d0e;">Žlutá:</strong> Úkol, otázka, aktivita, procvičení</div>
            </div>
            <div class="legend-card" style="background: #faf5ff; border-left: 4px solid #a855f7;">
                <span class="badge-dot" style="background: #a855f7;"></span>
                <div><strong style="color: #6b21a8;">Fialová:</strong> AI mentoring a práce s asistencí</div>
            </div>
            <div class="legend-card" style="background: #f0fdf4; border-left: 4px solid #22c55e;">
                <span class="badge-dot" style="background: #22c55e;"></span>
                <div><strong style="color: #15803d;">Zelená:</strong> Praxe, doporučení, dobrý postup</div>
            </div>
            <div class="legend-card" style="background: #fef2f2; border-left: 4px solid #ef4444;">
                <span class="badge-dot" style="background: #ef4444;"></span>
                <div><strong style="color: #991b1b;">Oranžová / Červená:</strong> Riziko, varování, problém</div>
            </div>
            <div class="legend-card" style="background: #f8fafc; border-left: 4px solid #64748b;">
                <span class="badge-dot" style="background: #64748b;"></span>
                <div><strong style="color: #334155;">Šedá:</strong> Zdroje, ověřování, poznámky</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# KAPITOLA 1: PODNIKAVOST A STARTUPY
# ==========================================
elif view == "Kapitola 1":
    st.markdown("<span class='hero-badge'>Kapitola 1</span>", unsafe_allow_html=True)
    st.title("Podnikavost a startupová kultura")
    st.markdown("<p style='font-size: 1rem; color: #64748b; margin-bottom: 1.5rem;'>Od nápadu k odpovědnému podnikání, ověření projektu a výběru právní formy.</p>", unsafe_allow_html=True)

    section_options = [
        "1. Podnikatel a základní pojmy",
        "3. OSVČ a živnosti",
        "4. Obchodní korporace",
        "5. Startup: nápad, který hledá funkční byznys",
        "6. Podnikatelský záměr",
        "7. Lean Canvas",
        "8. CSR, etika a odpovědné podnikání",
        "9. Rizika podnikání",
        "10. Švarcsystém",
        "11. Ověřování informací a užitečné zdroje"
    ]
    selected_section = st.selectbox("📌 Přechod na podkapitolu:", section_options, index=0)
    st.divider()

    if selected_section == "1. Podnikatel a základní pojmy":
        st.write("Obsah sekce 1 je připraven na vložení.")
    else:
        st.write(f"Zvolená sekce: {selected_section} (Připraveno na doplnění)")


# ==========================================
# KAPITOLA 2: FINANCE A OSOBNÍ MANAGEMENT
# ==========================================
elif view == "Kapitola 2":
    st.markdown("<span class='hero-badge'>Kapitola 2</span>", unsafe_allow_html=True)
    st.title("Finance v běžném životě: peníze, rozhodování a odpovědnost")
    st.markdown("<p style='font-size: 1rem; color: #64748b; margin-bottom: 1.5rem;'>Osobní finance, bankovní systém, finanční trh a finanční řízení podniku v souvislostech.</p>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown("""
        <div class='box-blue'>
            <strong>🪙 Pointa kapitoly:</strong> Finanční gramotnost není jen znalost pojmů. Je to schopnost rozumět penězům jako systému, bezpečně se rozhodovat, vyhodnocovat rizika a plánovat osobní i podnikové finance tak, aby člověk dokázal reagovat na běžné i krizové situace.
        </div>
        """, unsafe_allow_html=True)

    section_options_2 = [
        "1.1 Peníze jako digitální data a vývoj peněz",
        "1.2 ČNB a komerční banky",
        "1.3 Bezpečné platby a Phishing Trenažér",
        "1.4 Kryptoměny a investiční kalkulačka"
    ]
    selected_section_2 = st.selectbox("📌 Přechod na podkapitolu:", section_options_2, index=0)
    st.divider()

    # -------------------------------------------------------------------------
    # 1.1 PENÍZE JAKO DIGITÁLNÍ DATA
    # -------------------------------------------------------------------------
    if selected_section_2 == "1.1 Peníze jako digitální data a vývoj peněz":
        st.markdown("<div class='sub-section-header'>1. BANKOVNÍ SYSTÉM A PENÍZE V 21. STOLETÍ</div><h2>1.1 Peníze jako digitální data a vývoj peněz</h2>", unsafe_allow_html=True)
        st.write("21. století není jen éra umělé inteligence a sociálních sítí. Je to především éra totální transformace toho, jak vnímáme hodnotu.")
        
        with st.container(border=True):
            st.markdown("""
            <div class='box-blue'>
                <strong>💡 Proč je to důležité právě teď?</strong>
                <ul>
                    <li><strong>Technologie jako hybatel:</strong> Od okamžitých mezinárodních plateb až po investování pár korun z mobilu.</li>
                    <li><strong>Nekonečné možnosti a nová rizika:</strong> Peníze už nejsou papírky, jsou to data vyžadující novou digitální gramotnost.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### Vývoj peněz a směny")
            st.markdown("""
            | Období / forma | Co sloužilo jako peníze | Na čem stála důvěra |
            | :--- | :--- | :--- |
            | **Naturální směna** | Zboží za zboží | Na přímé dohodě dvou lidí (dvojí shoda potřeb) |
            | **Komoditní peníze** | Sůl, obilí, dobytek, plátno | Na užitečnosti nebo vzácnosti věci |
            | **Mince** | Kovové mince | Na kovu, hmotnosti, ryzosti a autoritě vydavatele |
            | **Bankovky** | Papírové peníze | Na důvěře ve stát, banku a zákonné platidlo |
            | **Zlatý standard** | Papírové peníze vázané na zlato | Na garanci státu vyměnit bankovky za zlato |
            | **Fiat peníze** | Dnešní státní měny | Na důvěře v ekonomiku, stát a centrální banku |
            | **Bezhotovostní peníze**| Zůstatek na účtu | Na bankovním systému, pravidlech a dohledu |
            | **Kryptoměny** | Distribuovaný záznam (Blockchain) | Na technologii, síti uživatelů a protokolu |
            """)

            st.markdown("#### 🧠 Interaktivní výzva: Zkus zaplatit komoditou!")
            komodita = st.selectbox("Představ si, že jdeš do kavárny. Čím zkusíš zaplatit?", ["Vyber...", "Krávou 🐄", "Mušlemi 🐚", "Zlatým prachem ✨"], key="k2_1_komodita")
            if komodita == "Krávou 🐄":
                st.error("❌ Nepraktické! Kráva se špatně dělí (jak zaplatíš za jedno kafe?) a navíc ji musíš krmit.")
            elif komodita == "Mušlemi 🐚":
                st.warning("⚠️ Lze to, ale hodnota závisí na zvyklostech. Pokud kavárník mušle neuznává, kávu ti nedá.")
            elif komodita == "Zlatým prachem ✨":
                st.success("✅ Skvělé k uchování hodnoty! Ale barista musí u kasy prach složitě vážit a ověřovat jeho ryzost.")

    # -------------------------------------------------------------------------
    # 1.2 ČNB A KOMERČNÍ BANKY
    # -------------------------------------------------------------------------
    elif selected_section_2 == "1.2 ČNB a komerční banky":
        st.markdown("<div class='sub-section-header'>1. BANKOVNÍ SYSTÉM A PENÍZE V 21. STOLETÍ</div><h2>1.2 ČNB a komerční banky</h2>", unsafe_allow_html=True)
        st.write("Bankovní systém není jen síť poboček a bankomatů. Je to jeden z nejdůležitějších „nervových systémů“ ekonomiky.")

        with st.container(border=True):
            st.markdown("""
            <div class='box-gray'>
                <strong>Česká národní banka (ČNB):</strong> Centrální banka státu. Neobsluhuje běžné občany. Její hlavní cíl je stabilita měny (hlídá inflaci) a dohled nad trhem. Určuje základní úrokové sazby.<br><br>
                <strong>Komerční banky:</strong> Běžné banky pro občany a firmy (přijímají vklady, poskytují úvěry a zajišťují platební styk).
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("#### 🎮 Simulace: Jsi bankovní rada ČNB!")
            st.write("**Situace:** Inflace je vysoká, ceny v obchodech letí nahoru. Co uděláš s úrokovou sazbou?")
            cnb_action = st.radio("Vaše rozhodnutí:", ["Vyber možnost...", "Zvýšíme sazby", "Snížíme sazby", "Ponecháme sazby beze změny"], key="k2_1_cnb")
            
            if st.button("Potvrdit rozhodnutí ČNB", key="k2_1_cnb_btn"):
                if cnb_action == "Zvýšíme sazby":
                    st.success("✅ Správný krok k tlumení inflace! Úvěry zdraží, lidé budou méně utrácet a více spořit. Tlak na růst cen se sníží.")
                elif cnb_action == "Vyber možnost...":
                    st.warning("Musíš vybrat jednu z možností.")
                else:
                    st.error("❌ Rizikové! Pokud nesnížíte objem peněz v oběhu zdražením úvěrů, inflace může dál růst.")

        with st.container(border=True):
            st.markdown("### 1.2.4 Jak ČNB ovlivňuje ekonomiku: 2T repo sazba")
            st.write("Nejdůležitějším nástrojem ČNB je **2T repo sazba** (dvoutýdenní repo sazba). Za tuto sazbu si komerční banky ukládají své přebytečné peníze u ČNB na 2 týdny.")

            st.markdown("##### 🎛️ Interaktivní simulátor: Změna úrokové sazby ČNB")
            sim_repo = st.slider("2T repo sazba ČNB (%):", min_value=0.5, max_value=10.0, value=4.75, step=0.25, key="k2_1_2_repo")
            
            col_s1, col_s2, col_s3 = st.columns(3)
            hypo_rate = round(sim_repo + 2.1, 2)
            spor_rate = round(max(0.1, sim_repo - 1.5), 2)
            
            col_s1.metric("Odhad sazby hypotéky", f"{hypo_rate} % p.a.")
            col_s2.metric("Odhad spořicího účtu", f"{spor_rate} % p.a.")
            
            if sim_repo >= 6.0:
                col_s3.metric("Dopad na inflaci", "Zpomaluje 📉", delta="- Vysoké úroky")
                st.warning("⚠️ **Dopad:** Hypotéky jsou velmi drahé. Lidé odkládají nákupy nemovitostí. Trh chladne, firmy méně investují.")
            elif sim_repo <= 2.0:
                col_s3.metric("Dopad na inflaci", "Roste 📈", delta="+ Rychlé půjčky")
                st.info("💡 **Dopad:** Hypotéky jsou velmi levné a dostupné. Ceny nemovitostí i zboží prudce rostou, investice vzkvétají.")
            else:
                col_s3.metric("Dopad na inflaci", "Stabilizovaná ⚖️", delta="Neutralita")
                st.success("✅ **Dopad:** Měnová politika je v rovnováze. Úvěry jsou dostupné a inflace se blíží cíli.")

    # -------------------------------------------------------------------------
    # 1.3 BEZPEČNÉ PLATBY (PHISHING)
    # -------------------------------------------------------------------------
    elif selected_section_2 == "1.3 Bezpečné platby a Phishing Trenažér":
        st.markdown("<div class='sub-section-header'>1. BANKOVNÍ SYSTÉM A PENÍZE V 21. STOLETÍ</div><h2>1.3 Bezpečné platby a Phishing trenažér</h2>", unsafe_allow_html=True)
        
        with st.container(border=True):
            st.warning("⚠️ **Pravidlo pro běžný život:** Karta, mobil ani hodinky nejsou peníze samy o sobě, ale klíče k tvému účtu. Banka po telefonu ani přes SMS nikdy nechce PIN ani autorizační kód!")
            
            st.markdown("#### 🚨 Trenažér: Odhal podvodný e-mail (Phishing)")
            st.info("""
            **Od:** bezpecnost@bnka-podpora-klientu.cz  
            **Předmět:** ZABLOKOVANÝ ÚČET - OKAMŽITÁ AKCE!  
            Vážený kliente, vaše karta byla dočasně zablokována. Pro její okamžité odblokování klikněte IHNED na odkaz níže a přihlaste se:  
            👉 [www.mojebanka-rychle-overeni.com/login](https://#)
            """)

            col_ph1, col_ph2 = st.columns(2)
            with col_ph1:
                ph_1 = st.checkbox("Podezřelá e-mailová adresa (překlepy, podivná doména)", key="k2_1_ph1")
                ph_2 = st.checkbox("Výzva k nahlášení na Policii", key="k2_1_ph2")
            with col_ph2:
                ph_3 = st.checkbox("Extrémní tlak na čas a vyvolání strachu", key="k2_1_ph3")
                ph_4 = st.checkbox("Odkaz, který nevede na oficiální web banky", key="k2_1_ph4")

            if st.button("Vyhodnotit hrozbu phishingu", key="k2_1_ph_btn"):
                if ph_1 and ph_3 and ph_4 and not ph_2:
                    st.success("Skvělá práce! Odhalil jsi přesně 3 hlavní znaky podvodu. Správná reakce je na nic neklikat a e-mail smazat.")
                else:
                    st.error("Zkus to znovu. Najdi přesně tři znaky typické pro podvodníky z e-mailu výše.")

    # -------------------------------------------------------------------------
    # 1.4 KRYPTOMĚNY A INVESTICE
    # -------------------------------------------------------------------------
    elif selected_section_2 == "1.4 Kryptoměny a investiční kalkulačka":
        st.markdown("<div class='sub-section-header'>1. BANKOVNÍ SYSTÉM A PENÍZE V 21. STOLETÍ</div><h2>1.4 Kryptoměny a pravidelné investování (DCA)</h2>", unsafe_allow_html=True)
        st.write("Kryptoměny využívají **blockchain** (sdílenou účetní knihu). Jsou vysoce rizikové a jejich cena výrazně kolísá.")

        with st.container(border=True):
            col_inv1, col_inv2 = st.columns(2)
            with col_inv1:
                vklad_start = st.slider("Počáteční vklad (Kč):", 0, 50000, 1000, step=500, key="k2_1_vstart")
                vklad_mesic = st.slider("Měsíční vklad (Kč):", 100, 10000, 200, step=100, key="k2_1_vmesic")
                roky = st.slider("Doba investování (roky):", 1, 10, 5, key="k2_1_vroky")
                celkem_vlozeno = vklad_start + (vklad_mesic * 12 * roky)

            def spocitej_zhodnoceni(vklad_s, vklad_m, r, urok_rocne):
                mesicni_urok = urok_rocne / 12
                zustatek = vklad_s
                for _ in range(r * 12):
                    zustatek = (zustatek + vklad_m) * (1 + mesicni_urok)
                return zustatek

            with col_inv2:
                st.metric("Celkem vložíš ze svého:", f"{celkem_vlozeno:,.0f} Kč".replace(",", " "))
                scenar = st.selectbox("Vyber vývoj trhu pro simulaci:", [
                    "Pesimistický (Propad -20 % ročně) 📉",
                    "Nulový (0 % ročně) ⚖️",
                    "Spořicí účet (Fix 3.5 % ročně) 🏦",
                    "Silně růstový trh (+15 % ročně) 🚀",
                    "Extrémní krypto růst (+30 % ročně) 🔥"
                ], key="k2_1_scenar")

                if "Pesimistický" in scenar:
                    vysledek = spocitej_zhodnoceni(vklad_start, vklad_mesic, roky, -0.20)
                elif "Nulový" in scenar:
                    vysledek = celkem_vlozeno
                elif "Spořicí" in scenar:
                    vysledek = spocitej_zhodnoceni(vklad_start, vklad_mesic, roky, 0.035)
                elif "Silně růstový" in scenar:
                    vysledek = spocitej_zhodnoceni(vklad_start, vklad_mesic, roky, 0.15)
                else:
                    vysledek = spocitej_zhodnoceni(vklad_start, vklad_mesic, roky, 0.30)
                
                rozdil = vysledek - celkem_vlozeno
                st.metric("Orientační hodnota na konci:", f"{vysledek:,.0f} Kč".replace(",", " "), delta=f"{rozdil:,.0f} Kč zisk/ztráta")


# ==========================================
# OSTATNÍ KAPITOLY
# ==========================================
elif view in ["Kapitola 3", "Kapitola 4", "Kapitola 5", "Kapitola 6"]:
    st.title(view)
    st.write("Tato sekce je připravena pro budoucí obsah.")

# ==========================================
# POKROKY A UČITEL
# ==========================================
elif view == "Pokroky":
    st.markdown("<span class='hero-badge'>Studentská zóna</span>", unsafe_allow_html=True)
    st.title("Moje pokroky")
    st.markdown("<p style='font-size: 1rem; color: #64748b; margin-bottom: 2rem;'>Přehled dokončených kapitol a úkolů.</p>", unsafe_allow_html=True)

elif view == "Ucitel":
    st.markdown("<span class='hero-badge'>Metodik & Dashboard</span>", unsafe_allow_html=True)
    st.title("Učitelská základna")
    st.markdown("<p style='font-size: 1rem; color: #64748b; margin-bottom: 2rem;'>Metodické pokyny a sledování práce jednotlivých žáků podle tříd.</p>", unsafe_allow_html=True)


