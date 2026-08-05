import streamlit as st

# 1. Konfigurace stránky
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

    html, body, [class*="css"] {
        font-family: 'Montserrat', -apple-system, sans-serif !important;
    }

    .stApp {
        background-color: #f8fafc;
        color: #0f172a;
    }

    .main .block-container {
        max-width: 940px !important;
        padding-top: 2rem !important;
        padding-bottom: 5rem !important;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #ffffff !important;
        border-radius: 12px !important;
        border: 1px solid #e2e8f0 !important;
        box-shadow: 0 1px 3px 0 rgba(15, 23, 42, 0.03), 0 1px 2px 0 rgba(15, 23, 42, 0.02) !important;
        padding: 1.75rem !important;
        margin-bottom: 1.25rem !important;
        transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }

    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        border-color: #cbd5e1 !important;
        box-shadow: 0 4px 12px -2px rgba(15, 23, 42, 0.05) !important;
    }

    h1 {
        font-family: 'Montserrat', sans-serif !important;
        color: #0f172a !important;
        font-weight: 800 !important;
        font-size: 2.1rem !important;
        letter-spacing: -0.025em !important;
        line-height: 1.25 !important;
        margin-bottom: 0.5rem !important;
    }

    h2 {
        font-family: 'Montserrat', sans-serif !important;
        color: #1e293b !important;
        font-weight: 700 !important;
        font-size: 1.25rem !important;
        letter-spacing: -0.015em !important;
        margin-top: 1.25rem !important;
        margin-bottom: 0.75rem !important;
        border-bottom: 1px solid #f1f5f9;
        padding-bottom: 0.5rem;
    }

    h3 {
        font-family: 'Montserrat', sans-serif !important;
        color: #334155 !important;
        font-weight: 600 !important;
        font-size: 1.05rem !important;
        margin-top: 1.25rem !important;
    }

    p, li, td, th {
        font-family: 'Montserrat', sans-serif !important;
        color: #334155;
        font-size: 0.94rem;
        line-height: 1.7;
        font-weight: 400;
    }

    .hero-badge {
        background: #e0e7ff;
        color: #4338ca;
        font-size: 0.72rem;
        font-weight: 700;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        display: inline-block;
        margin-bottom: 0.8rem;
    }

    .box-blue {
        background-color: #f0f9ff;
        border-left: 4px solid #0284c7;
        padding: 1.1rem 1.3rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
        color: #0f172a;
        font-size: 0.93rem;
    }
    
    .box-yellow {
        background-color: #fefce8;
        border-left: 4px solid #eab308;
        padding: 1.1rem 1.3rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
        color: #0f172a;
        font-size: 0.93rem;
    }

    .box-purple {
        background-color: #faf5ff;
        border-left: 4px solid #a855f7;
        padding: 1.1rem 1.3rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
        color: #0f172a;
        font-size: 0.93rem;
        word-wrap: break-word;
    }

    .box-green {
        background-color: #f0fdf4;
        border-left: 4px solid #22c55e;
        padding: 1.1rem 1.3rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
        color: #0f172a;
        font-size: 0.93rem;
    }

    .box-red {
        background-color: #fef2f2;
        border-left: 4px solid #ef4444;
        padding: 1.1rem 1.3rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
        color: #0f172a;
        font-size: 0.93rem;
    }

    .box-gray {
        background-color: #f8fafc;
        border-left: 4px solid #64748b;
        padding: 1.1rem 1.3rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
        color: #0f172a;
        font-size: 0.93rem;
    }

    .stTextInput input, .stTextArea textarea, .stSelectbox select {
        font-family: 'Montserrat', sans-serif !important;
        border-radius: 8px !important;
        border: 1px solid #cbd5e1 !important;
        background-color: #ffffff !important;
        color: #0f172a !important;
        font-size: 0.9rem !important;
        padding: 0.65rem 0.9rem !important;
    }

    .stButton > button {
        font-family: 'Montserrat', sans-serif !important;
        border-radius: 8px !important;
        border: 1px solid #cbd5e1 !important;
        background-color: #ffffff !important;
        color: #0f172a !important;
        font-weight: 600 !important;
        font-size: 0.88rem !important;
        padding: 0.55rem 1.1rem !important;
        box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.04) !important;
        transition: all 0.15s ease !important;
    }

    .stButton > button:hover {
        border-color: #4f46e5 !important;
        color: #4f46e5 !important;
        background-color: #f5f3ff !important;
    }

    section[data-testid="stSidebar"] {
        background-color: #ffffff !important;
        border-right: 1px solid #e2e8f0 !important;
    }

    .sidebar-section-title {
        font-size: 0.7rem;
        font-weight: 700;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-top: 1.4rem;
        margin-bottom: 0.5rem;
    }

    .sub-section-header {
        color: #4f46e5;
        font-weight: 700;
        font-size: 0.85rem;
        letter-spacing: 0.05em;
        text-transform: uppercase;
    }

    .lc-card {
        background-color: #ffffff;
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        padding: 0.8rem;
        margin-bottom: 0.5rem;
    }
    .lc-title {
        font-size: 0.78rem;
        font-weight: 700;
        color: #4f46e5;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.3rem;
    }
    
    /* MIND MAPA CSS */
    .mindmap-wrapper { display: flex; justify-content: center; align-items: center; padding: 2rem 1rem; flex-wrap: wrap; gap: 2rem; background: #f1f5f9; border-radius: 12px; border: 1px solid #e2e8f0; margin-bottom: 1.5rem; }
    .mm-col { display: flex; flex-direction: column; gap: 1.5rem; }
    .mm-center { background: #ef4444; color: white; padding: 1.8rem 2.5rem; border-radius: 20px; font-weight: 800; font-size: 1.5rem; text-align: center; box-shadow: 0 10px 15px -3px rgba(239, 68, 68, 0.3); border: 3px solid #b91c1c; z-index: 2; }
    .mm-node { background: #ffffff; border: 2px solid #cbd5e1; padding: 1rem; border-radius: 16px; width: 260px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05); position: relative; transition: all 0.2s ease; }
    .mm-node:hover { border-color: #6366f1; box-shadow: 0 10px 15px -3px rgba(99, 102, 241, 0.2); transform: translateY(-2px); }
    .mm-title { font-weight: 700; color: #1e293b; margin-bottom: 0.5rem; text-align: center; border-bottom: 2px solid #e2e8f0; padding-bottom: 0.5rem; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 0.05em; }
    .mm-node ul { margin: 0; padding-left: 1.2rem; font-size: 0.85rem; color: #475569; }
    .mm-node li { margin-bottom: 0.3rem; }
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

elif view == "Kapitola 1":
    st.markdown("<span class='hero-badge'>Kapitola 1</span>", unsafe_allow_html=True)
    st.title("Podnikavost a startupová kultura")
    st.markdown("<p style='font-size: 1rem; color: #64748b; margin-bottom: 1.5rem;'>Od nápadu k odpovědnému podnikání, ověření projektu a výběru právní formy.</p>", unsafe_allow_html=True)

    section_options = [
        "1. Podnikatel a základní pojmy",
        "2. Slovníček základních pojmů",
        "3. OSVČ a živnosti",
        "4. Obchodní korporace",
        "5. Startup: nápad, který hledá byznys",
        "6. Podnikatelský záměr",
        "7. Lean Canvas",
        "8. CSR, etika a odpovědné podnikání",
        "9. Rizika podnikání",
        "10. Švarcsystém",
        "11. Ověřování informací a užitečné zdroje",
        "12. Ukončení podnikání",
        "13. Logická mapa podnikání",
        "14. Reflexe a sebehodnocení",
        "15. Integrované opakování"
    ]

    selected_section = st.selectbox("📌 Přechod na podkapitolu (Vyberte téma):", section_options, index=0)

    st.divider()

    # Zde ponechávám základní strukturu Kapitoly 1 tak, jak jsi ji měl/a v předchozím kódu
    if selected_section == "1. Podnikatel a základní pojmy":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 1</div>", unsafe_allow_html=True)
        st.markdown("## 1. Podnikatel a základní pojmy")
        with st.container(border=True):
            st.markdown("### Základní definice podnikání")
            st.markdown("<div class='box-blue'><strong>Hlavní definice:</strong> Zákon chápe podnikání jako soustavnou činnost prováděnou samostatně, vlastním jménem, na vlastní odpovědnost, za účelem dosažení zisku.</div>", unsafe_allow_html=True)
    elif selected_section == "6. Podnikatelský záměr":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 6</div>", unsafe_allow_html=True)
        st.markdown("## 6. Podnikatelský záměr")
        with st.container(border=True):
            st.markdown("#### 🧮 Kalkulačka bodu zvratu")
            c1, c2, c3 = st.columns(3)
            with c1: price = st.number_input("Cena (Kč):", value=150)
            with c2: var_cost = st.number_input("Var. náklad (Kč):", value=80)
            with c3: fix_cost = st.number_input("Fix. náklady (Kč):", value=2800)
            if price - var_cost > 0:
                st.success(f"Bod zvratu: {fix_cost / (price - var_cost):.1f} kusů měsíčně.")
    elif selected_section == "13. Logická mapa podnikání":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 13</div>", unsafe_allow_html=True)
        st.markdown("## 13. Logická mapa podnikání")
        with st.container(border=True):
            st.markdown("""
            <div class="mindmap-wrapper">
                <div class="mm-col">
                    <div class="mm-node"><div class="mm-title">1. Legislativa a definice</div><ul><li>občanský zákoník</li><li>ZOK</li></ul></div>
                    <div class="mm-node"><div class="mm-title">2. Právní formy</div><ul><li>OSVČ, v.o.s., k.s.</li><li>s.r.o., a.s.</li></ul></div>
                </div>
                <div class="mm-center">PODNIKÁNÍ</div>
                <div class="mm-col">
                    <div class="mm-node"><div class="mm-title">3. Finance a Záměr</div><ul><li>Zákazník, náklady</li></ul></div>
                    <div class="mm-node"><div class="mm-title">4. Rizika a Zánik</div><ul><li>Švarcsystém, insolvence</li></ul></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("Zvolte sekci v horním menu. Ostatní podkapitoly z Kapitoly 1 jsou zde skryté, abychom se mohli soustředit na Kapitolu 2.")

# ==========================================
# KAPITOLA 2: FINANCE A OSOBNÍ MANAGEMENT (CELÁ OBSÁHLÁ KAPITOLA Z DOCX)
# ==========================================
elif view == "Kapitola 2":
    st.markdown("<span class='hero-badge'>Kapitola 2</span>", unsafe_allow_html=True)
    st.title("Finance v běžném životě: peníze, rozhodování a odpovědnost")
    st.markdown("<p style='font-size: 1rem; color: #64748b; margin-bottom: 1.5rem;'>Tahle kapitola propojuje osobní finance, bankovní systém, finanční trh a podnikové finance. Nejde jen o počítání peněz, ale o odpovědné rozhodování v běžném životě.</p>", unsafe_allow_html=True)

    with st.container(border=True):
        st.markdown("""
        <div class='box-purple'>
            <strong>🎯 Cíle kapitoly:</strong> Co máš po kapitole umět?<br>
            • vysvětlit funkce peněz a princip bankovního systému,<br>
            • rozlišit roli ČNB a komerčních bank,<br>
            • používat zásady bezpečného platebního styku,<br>
            • sestavit jednoduchý osobní nebo rodinný rozpočet,<br>
            • vysvětlit složené úročení, inflaci a tvorbu finanční rezervy,<br>
            • rozlišit spoření, investování a spekulaci,<br>
            • popsat základní finanční produkty, cenné papíry a rizika,<br>
            • vysvětlit cenu úvěru včetně RPSN,<br>
            • posoudit smysl pojištění podle životní situace,<br>
            • propojit osobní finance s finančním řízením podniku, náklady, výnosy a cashflow.
        </div>
        """, unsafe_allow_html=True)

    section_options_2 = [
        "1. Bankovní systém a peníze v 21. století",
        "2. Osobní finance a „Algoritmy bohatství“",
        "3. Finanční trh a analýza rizik",
        "4. Úvěry, pojištění a ochrana majetku",
        "5. Finanční řízení v podniku",
        "6. Interaktivní vrstva a Slovník"
    ]

    selected_section_2 = st.selectbox("📌 Přechod na podkapitolu (Vyberte téma):", section_options_2, index=0)
    st.divider()

    # --- SEKCE 1: BANKOVNÍ SYSTÉM ---
    if selected_section_2 == "1. Bankovní systém a peníze v 21. století":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 1</div>", unsafe_allow_html=True)
        st.markdown("## 1. Bankovní systém a peníze v 21. století")
        
        with st.container(border=True):
            st.write("21. století není jen éra umělé inteligence a sociálních sítí. Je to především éra totální transformace toho, jak vnímáme hodnotu. Ještě před pár desítkami let znamenalo „být v bance“ fyzickou návštěvu přepážky. Dnes? Bankovní systém se stal neviditelným operačním systémem našeho života[cite: 2].")
            st.markdown("""
            <div class='box-blue'>
                <strong>Základní myšlenka:</strong> Peníze nejsou jen „věc“. Jsou to hlavně důvěryhodný záznam hodnoty, kterému lidé, firmy a stát věří. V různých dobách měl tento záznam podobu dobytka, obilí, kovu, mince, papírové bankovky, bankovního účtu nebo digitální platby v mobilu[cite: 2].
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("### 1.1 Peníze jako digitální data")
            st.write("Peníze dnes často nevypadají jako mince nebo bankovky. Když platíš kartou, mobilem nebo hodinkami, většinou se nepřesouvá žádný fyzický předmět. V bankovním systému se změní digitální záznam: jednomu účtu se částka odečte a druhému připíše[cite: 2].")
            
            st.markdown("#### Shrnutí vývoje peněz[cite: 2]")
            st.markdown("""
            | Období / forma | Co sloužilo jako peníze | Na čem stála důvěra |
            | :--- | :--- | :--- |
            | **Naturální směna** | Zboží za zboží | Na přímé dohodě dvou lidí |
            | **Komoditní peníze** | Sůl, obilí, dobytek, mušle, kovy | Na užitečnosti nebo vzácnosti věci |
            | **Mince** | Kovové mince | Na kovu, hmotnosti, ryzosti a autoritě vydavatele |
            | **Bankovky** | Papírové peníze | Na důvěře ve stát, banku a zákonné platidlo |
            | **Zlatý standard** | Papírové peníze vázané na zlato | Na garanci státu vyměnit bankovky za zlato |
            | **Bezhotovostní peníze**| Zůstatek na účtu | Na bankovním systému, pravidlech a dohledu |
            | **Digitální platby** | Data v bankovních systémech | Na ověření identity, zabezpečení a infrastruktuře |
            | **Kryptoměny** | Distribuovaný digitální záznam | Na technologii, síti uživatelů a protokolu |
            """)

            with st.expander("💡 Přečti si více o Zlatém standardu a Nixonově šoku[cite: 2]"):
                st.write("**Zlatý standard:** Stát sliboval, že měna je krytá zlatem. Peníze nebyly jen papírky. Měly být navázané na zásoby zlata, které měl stát k dispozici[cite: 2].")
                st.write("**Brettonwoodský systém a Nixonův šok:** Po 2. světové válce byl dolar navázán na zlato a ostatní měny na dolar. V roce 1971 ale americký prezident Richard Nixon pozastavil směnitelnost dolaru za zlato (tzv. Nixonův šok). Svět se přesunul k „fiat penězům“ – jejich hodnota stojí hlavně na důvěře ve stát a centrální banku, ne na zásobách drahých kovů[cite: 2].")

            st.markdown("""
            <div class='box-yellow'>
                <strong>🧠 Interaktivní výzva:</strong> Vyber jednu komoditu (např. obilí, sůl, mušle), která by mohla sloužit jako peníze. Napiš, v čem by byla praktická a v čem by naopak selhávala[cite: 2].
            </div>
            """, unsafe_allow_html=True)
            st.text_input("Tvoje komodita a zhodnocení:", placeholder="Např. sůl - dá se dělit, ale...[cite: 2]", key="komodita_vyzva")

        with st.container(border=True):
            st.markdown("### 1.2 ČNB a komerční banky[cite: 2]")
            st.markdown("""
            <div class='box-gray'>
                <strong>Česká národní banka (ČNB):</strong> Je centrální banka státu. Neobsluhuje běžné občany. Její hlavní cíl je stabilita měny (hlídá inflaci) a dohled nad trhem. Zasahuje do ekonomiky určováním základních úrokových sazeb (např. dvoutýdenní repo sazba)[cite: 2].<br><br>
                <strong>Komerční banky:</strong> Banky, se kterými běžně pracujeme my i firmy. Přijímají vklady (pasivní operace), poskytují úvěry (aktivní operace) a zajišťují platby (neutrální operace)[cite: 2].
            </div>
            """, unsafe_allow_html=True)

            with st.expander("🎮 Interaktivní simulace: Jsi bankovní rada ČNB![cite: 2]"):
                st.write("**Situace:** Inflace je vysoká, ceny v obchodech letí nahoru. Firmám i lidem se zdražuje život. Tvoje skupina představuje bankovní radu ČNB[cite: 2].")
                cnb_action = st.radio("Vaše rozhodnutí[cite: 2]:", ["Zvýšíme úrokové sazby", "Snížíme úrokové sazby", "Ponecháme sazby beze změny"])
                if st.button("Potvrdit rozhodnutí ČNB"):
                    if "Zvýšíme" in cnb_action:
                        st.success("Správný krok k tlumení inflace! Úvěry zdraží (lidé si méně půjčují), spoření bude výhodnější. Lidé budou méně utrácet a tlak na růst cen se sníží[cite: 2].")
                    else:
                        st.error("Rizikové! Pokud nesnížíte objem peněz v oběhu zlevněním úvěrů, inflace může dál růst[cite: 2].")

        with st.container(border=True):
            st.markdown("### 1.3 Platební styk[cite: 2]")
            st.write("Platební styk znamená převod peněz mezi plátcem a příjemcem. Umožňuje bezpečně přesouvat peníze od toho, kdo platí, k tomu, kdo má peníze dostat[cite: 2].")
            
            st.write("**CERTIS:** Když posíláme peníze v českých korunách mezi dvěma RŮZNÝMI bankami, musí platba projít přes systém CERTIS, který spravuje ČNB. Je to pomyslná „dálnice“ pro platby[cite: 2].")

            st.markdown("#### Digitální bezpečnost plateb[cite: 2]")
            st.markdown("""
            Karta, mobil nebo hodinky nejsou „peníze samy o sobě“. Jsou to vstupní brány k penězům na účtu. Nejčastější rizika jsou[cite: 2]:
            * phishingové e-maily a SMS[cite: 2],
            * podvodné telefonáty „z banky“[cite: 2],
            * krádež přihlašovacích údajů[cite: 2],
            * falešné investiční nabídky (garantovaný výnos)[cite: 2].
            """)

            with st.expander("🚨 Phishing Escape Room: Odhal podvod[cite: 2]"):
                st.write("Přečti si SMS, která ti právě přišla na mobil:")
                st.info("„Vaše karta byla zablokována. Klikněte zde a ověřte účet: www.bezpecnabanka-cz.net/login“[cite: 2]")
                st.markdown("<div class='box-red'><strong>VAROVÁNÍ:</strong> Tlak na rychlost (odblokování). Podezřelý odkaz. Banka NIKDY nechce PIN přes SMS! Zprávu ignoruj a ověř situaci přímo v aplikaci banky[cite: 2].</div>", unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 1.4 Fintech revoluce a Neobanky[cite: 2]")
            st.write("Fintech služby (např. Revolut, Wise) přesunuly finance z poboček do mobilu. Uživatel očekává rychlost, okamžité notifikace a nízké poplatky[cite: 2].")
            st.markdown("""
            <div class='box-yellow'>
                <strong>Rizika fintechu:</strong> Příliš snadné utrácení, rychlé půjčky bez promyšlení, falešné aplikace a dojem, že „když je to v aplikaci, je to bezpečné“[cite: 2].
            </div>
            """, unsafe_allow_html=True)

    # --- SEKCE 2: OSOBNÍ FINANCE ---
    elif selected_section_2 == "2. Osobní finance a „Algoritmy bohatství“":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2</div>", unsafe_allow_html=True)
        st.markdown("## 2. Osobní finance a „Algoritmy bohatství“")
        
        with st.container(border=True):
            st.write("Osobní finance nejsou jen otázka toho, kolik člověk vydělává. Jsou to každodenní rozhodnutí: za co utratím peníze, co odložím, co si půjčím, jak poznám riziko a jak se nenechám řídit reklamou v aplikaci[cite: 2].")
            
            st.markdown("### 2.2 Rozpočet: Mapa peněz[cite: 2]")
            st.write("Rozpočet ukazuje, odkud peníze přicházejí a kam odcházejí. Je dobré rozlišovat **Potřebu** (jídlo, bydlení, doprava) a **Přání** (značkové oblečení, streamovací služby navíc)[cite: 2].")
            st.markdown("""
            | Typ výdaje | Příklad | Otázka ke kontrole |
            | :--- | :--- | :--- |
            | **Fixní** | Nájem, paušál na telefon, splátka úvěru[cite: 2]. | Opravdu ho potřebuji každý měsíc?[cite: 2] |
            | **Proměnlivý** | Jídlo, doprava, drogerie, zábava[cite: 2]. | Dá se upravit bez zásadního poklesu kvality života?[cite: 2] |
            | **Skrytý** | Automatické předplatné, mikrotransakce[cite: 2]. | Vím, kolik mě stojí za rok?[cite: 2] |
            """)
            st.markdown("<div class='box-green'><strong>Model 50–30–20:</strong> 50 % příjmů na potřeby, 30 % na přání (radosti) a 20 % na rezervu nebo splácení dluhů[cite: 2].</div>", unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 2.3 Algoritmy bohatství[cite: 2]")
            st.markdown("""
            <div class='box-blue'>
                1. <strong>Zaplať nejdřív sobě:</strong> Odlož si část peněz hned po přijetí příjmu, nečekej, co ti zbyde na konci měsíce[cite: 2].<br>
                2. <strong>Rezerva:</strong> Tvůj finanční airbag. Chráni tě před tím, aby rozbitý telefon nebo ztráta brigády skončily dluhem. Cíl je mít 3 až 6 měsíců nutných výdajů[cite: 2].<br>
                3. <strong>Vyhýbej se drahému dluhu:</strong> A pravidelně kontroluj, kam ti peníze mizí[cite: 2].
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 2.4 Matematika peněz: Čas, úrok a inflace[cite: 2]")
            st.write("Peníze mají časovou hodnotu. Ceny se mění a peníze mohou nést úrok[cite: 2].")
            
            st.markdown("""
            * **Jednoduché úročení:** Úrok se počítá stále jen z původně vložené nebo půjčené částky (jistiny)[cite: 2].
            * **Složené úročení:** Úročí se nejen původní částka, ale postupně i již připsané úroky! Tvoje peníze vydělávají další peníze[cite: 2].
            * **Inflace:** Růst cenové hladiny. Za stejnou částku si koupíme méně než dříve[cite: 2].
            """)

        with st.container(border=True):
            st.markdown("### 2.6 Psychologie utrácení[cite: 2]")
            st.write("Lidé nejsou kalkulačky. E-shopy, sítě a aplikace nás často vedou k impulzivním nákupům[cite: 2].")
            st.markdown("""
            * **FOMO (Fear Of Missing Out):** Strach, že mi něco uteče. Obrana: Počkej 24 hodin před nákupem[cite: 2].
            * **Sleva:** Pocit úspory, i když kupuji zbytečnost. Obrana: Ptej se, koupil/a bych to i bez slevy?[cite: 2]
            * **Odložená platba (BNPL):** Nákup nebolí hned. Obrana: Ber ji jako dluh, ne jako slevu[cite: 2].
            """)

            st.markdown("#### ⏳ Kalkulačka času: Kolik života tě to stálo?[cite: 2]")
            st.write("Cena věci není jen částka v korunách. Dá se přepočítat i na čas, který musí člověk pracovat, aby si ji mohl dovolit[cite: 2].")
            
            c_time1, c_time2, c_time3 = st.columns(3)
            with c_time1:
                item_price = st.number_input("Cena věci (Kč):", value=2400, step=100)
            with c_time2:
                hourly_wage = st.number_input("Tvoje čistá hodinová mzda (Kč):", value=150, step=10)
            with c_time3:
                if hourly_wage > 0:
                    hours_needed = item_price / hourly_wage
                    st.info(f"**Musíš pracovat:**\n### {hours_needed:.1f} hodin[cite: 2]")

    # --- SEKCE 3: FINANČNÍ TRH A KRYPTO ---
    elif selected_section_2 == "3. Finanční trh a analýza rizik":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 3</div>", unsafe_allow_html=True)
        st.markdown("## 3. Finanční trh a analýza rizik")
        
        with st.container(border=True):
            st.write("Finanční trh přesouvá peníze v čase. Někdo peníze dnes nepotřebuje a chce je zhodnotit. Někdo jiný peníze potřebuje dnes a je ochoten za jejich použití zaplatit úrok nebo podíl na zisku[cite: 2].")
            
            st.markdown("### 3.2 Investiční trojúhelník[cite: 2]")
            st.markdown("""
            <div class='box-purple'>
                <strong>1. Výnos:</strong> To, co získáš navíc (úrok, dividenda, nárůst ceny)[cite: 2].<br>
                <strong>2. Riziko:</strong> Možnost, že výsledek bude jiný (ztráta, kolísání)[cite: 2].<br>
                <strong>3. Likvidita:</strong> Jak snadno lze aktivum proměnit zpět na peníze[cite: 2].
            </div>
            """, unsafe_allow_html=True)
            st.warning("Pravidlo: Vyšší možný výnos obvykle znamená vyšší riziko. Vysoký výnos, nulové riziko a okamžitá dostupnost peněz najednou jsou podezřelá kombinace[cite: 2].")

        with st.container(border=True):
            st.markdown("### 3.3 Spoření vs. Investování vs. Spekulace[cite: 2]")
            st.markdown("""
            | Pojem | Co to je? | Typický příklad | Riziko |
            | :--- | :--- | :--- | :--- |
            | **Spoření** | Odkládání peněz s důrazem na bezpečnost a dostupnost[cite: 2]. | Spořicí účet, termínovaný vklad[cite: 2]. | Nízké, hrozí inflace[cite: 2]. |
            | **Investování** | Vkládání peněz do aktiv s cílem dlouhodobého zhodnocení[cite: 2]. | Akcie, dluhopisy, ETF[cite: 2]. | Střední až vysoké[cite: 2]. |
            | **Spekulace** | Sázka na krátkodobý pohyb ceny[cite: 2]. | Krátkodobé obchody, krypto[cite: 2]. | Vysoké[cite: 2]. |
            """)

        with st.container(border=True):
            st.markdown("### 3.4 Základní cenné papíry[cite: 2]")
            st.write("Dnes už má cenný papír většinou elektronickou zaknihovanou podobu, nejde o fyzický papír[cite: 2].")
            
            st.markdown("""
            * **Akcie:** Představuje podíl na akciové společnosti. Koupí akcie firmě nepůjčuješ, kupuješ si kousek jejího vlastnictví[cite: 2].
            * **Dluhopis:** Cenný papír, kterým si emitent (stát, firma) půjčuje peníze. Kupuješ dluh, jsi věřitel a očekáváš úrok[cite: 2].
            * **Podílové listy / ETF:** Podíl na majetku fondu. Místo jedné akcie kupuješ „košík“ plný různých aktiv, čímž rozkládáš riziko[cite: 2].
            """)

        with st.container(border=True):
            st.markdown("### 3.6 Kryptoměny a Blockchain[cite: 2]")
            st.write("Kryptoměny jsou digitální aktiva v počítačové síti. Záznamy nejsou vedeny centrální bankou, ale technologií blockchain (sdílenou evidencí)[cite: 2].")
            
            st.markdown("""
            <div class='box-gray'>
                <strong>Příklady:</strong><br>
                • <strong>Bitcoin:</strong> První a nejznámější kryptoměna, digitální vzácné aktivum[cite: 2].<br>
                • <strong>Ethereum:</strong> Síť umožňující chytré kontrakty a decentralizované aplikace[cite: 2].<br>
                • <strong>Stablecoiny:</strong> Tokeny navázané např. na dolar[cite: 2].
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<div class='box-red'><strong>Největší rizika kryptoměn:</strong> Vysoká volatilita (prudké kolísání ceny), ztráta přístupu (seed phrase), podvody s falešnými tokeny, technická nevratnost a tlak influencerů (FOMO)[cite: 2].</div>", unsafe_allow_html=True)

    # --- SEKCE 4: ÚVĚRY A POJIŠTĚNÍ ---
    elif selected_section_2 == "4. Úvěry, pojištění a ochrana majetku":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 4</div>", unsafe_allow_html=True)
        st.markdown("## 4. Úvěry, pojištění a ochrana majetku")
        
        with st.container(border=True):
            st.write("Úvěr není „peníze zdarma“. Je to závazek, který přesouvá spotřebu nebo investici z budoucnosti do současnosti[cite: 2].")
            
            st.markdown("### 4.2 Úrok a 4.3 RPSN[cite: 2]")
            st.markdown("""
            * **Úrok:** Cena za půjčení peněz. Banky s ním často dělají reklamu[cite: 2].
            * **RPSN (Roční procentní sazba nákladů):** Skutečnější cena úvěru. Ukazuje celkovou cenu úvěru za rok vč. poplatků a pojištění. Při porovnávání úvěrů sleduj vždy RPSN![cite: 2]
            """)

            st.markdown("### Druhy úvěrů[cite: 2]")
            st.markdown("""
            | Typ | Charakteristika | Riziko |
            | :--- | :--- | :--- |
            | **Hypotéka** | Úvěr na bydlení zajištěný nemovitostí. Banka nepůjčí 100 % ceny (sleduje ukazatel LTV)[cite: 2]. | Dlouhá doba splácení, změna sazeb[cite: 2]. |
            | **Spotřebitelský úvěr** | Často není zajištěný hodnotným majetkem[cite: 2]. | Vyšší riziko nesplácení a drahé úroky[cite: 2]. |
            | **Kreditní karta** | Opakovaně dostupný úvěrový limit s bezúročným obdobím[cite: 2]. | Vysoký úrok při nesplacení včas[cite: 2]. |
            | **BNPL** | Kup teď, zaplať později (odložená platba)[cite: 2]. | Psychologicky maskuje dluh jako pohodlnou platbu[cite: 2]. |
            """)

            with st.expander("🤔 4.4 Ne každý úvěr dostane[cite: 2]"):
                st.write("Banka musí posoudit, zda dlužník pravděpodobně zvládne splácet. Posuzuje: Věk, příjem, výdaje (děti, nájem), registry dlužníků a u hypotéky zajištění. Zamítnutý úvěr může být signál, že by splácení bylo příliš rizikové[cite: 2].")

        with st.container(border=True):
            st.markdown("### 4.10 Pojištění: Ochrana před finančním nárazem[cite: 2]")
            st.write("Pojištění nezabrání tomu, aby se něco stalo, ale může snížit finanční škodu. Zřizuje se pro případ, kdy by škoda byla finančně těžko zvládnutelná[cite: 2].")
            
            st.markdown("""
            <div class='box-green'>
                <strong>Životní pojištění:</strong> Chrání před vážným dopadem na příjem domácnosti (smrt, invalidita, vážné onemocnění)[cite: 2].<br>
                <strong>Neživotní pojištění:</strong><br>
                • <em>Pojištění nemovitosti:</em> Chrání stavbu (zdi, střechu)[cite: 2].<br>
                • <em>Pojištění domácnosti:</em> Chrání vybavení (nábytek, elektroniku)[cite: 2].<br>
                • <em>Pojištění odpovědnosti:</em> Chrání před škodou, kterou způsobíme někomu jinému (vytopení souseda)[cite: 2].
            </div>
            """, unsafe_allow_html=True)
            st.error("Pozor na PODPOJIŠTĚNÍ! Pokud je majetek pojištěn na nižší částku, než je jeho skutečná hodnota, pojišťovna může krátit plnění[cite: 2].")

    # --- SEKCE 5: FINANČNÍ ŘÍZENÍ PODNIKU ---
    elif selected_section_2 == "5. Finanční řízení v podniku":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 5</div>", unsafe_allow_html=True)
        st.markdown("## 5. Finanční řízení v podniku — most k podnikavosti")
        
        with st.container(border=True):
            st.write("Firma může mít skvělý produkt, hezký web a plný kalendář zakázek — a přesto může mít finanční problém. Popularita není totéž co zisk a zisk není totéž co peníze na účtu[cite: 2].")

            st.markdown("### 5.2 Základní finanční výkazy[cite: 2]")
            st.markdown("""
            * **Rozvaha:** Fotografie firmy k určitému dni. Ukazuje, co firma vlastní (**Aktiva**) a z čeho je to financované (**Pasiva**)[cite: 2].
            * **Výkaz zisku a ztráty:** Film za určité období. Výnosy minus Náklady. Ukazuje, zda firma generuje zisk[cite: 2].
            * **Cashflow (Peněžní toky):** Skutečný tok peněz. Firma může být zisková, ale zkrachovat, pokud zákazníci platí pozdě a firmě chybí hotovost na placení mezd[cite: 2].
            """)

        with st.container(border=True):
            st.markdown("### 5.3 Bod zvratu (Break-even point)[cite: 2]")
            st.write("Ukazuje, kolik musí firma prodat, aby pokryla všechny náklady. Teprve prodeje nad bodem zvratu vytvářejí zisk[cite: 2].")
            
            st.markdown("""
            * **Fixní náklady (FN):** Nemění se podle počtu prodaných kusů (nájem, paušální služby)[cite: 2].
            * **Variabilní náklady (VN):** Rostou s každým vyrobeným/prodaným kusem (materiál, doprava)[cite: 2].
            """)
            st.info("**Vzorec:** Bod zvratu v kusech = Fixní náklady ÷ (Cena za kus − Variabilní náklad na kus)[cite: 2]")

        with st.container(border=True):
            st.markdown("### 5.5 Finanční analýza: kontrola finančního zdraví[cite: 2]")
            st.write("Pomáhá zjistit, zda je firma zisková, zadlužená, platebně schopná, efektivní a stabilní[cite: 2].")
            
            st.markdown("""
            | Co zkoumá | Ukazatel a Vzorec | Příklad významu |
            | :--- | :--- | :--- |
            | **Rentabilita** | **ROS** (Zisk ÷ Tržby × 100) | Kolik % z tržeb zůstává jako zisk[cite: 2]. |
            | **Likvidita** | **Běžná likvidita** (Oběžná aktiva ÷ Krátkodobé závazky) | Zda má firma dost prostředků na faktury a splátky[cite: 2]. |
            | **Zadluženost** | **Celková zadluženost** (Cizí zdroje ÷ Aktiva × 100) | Jaká část majetku je financována dluhem[cite: 2]. |
            | **Aktivita** | **Doba inkasa pohledávek** (Pohledávky ÷ Tržby × 365) | Za kolik dní firma průměrně dostává zaplaceno od zákazníků[cite: 2]. |
            """)

            with st.expander("🔎 5.6 Case Study: E-shop DropZone (Modelová analýza)[cite: 2]"):
                st.write("E-shop meziročně zvýšil tržby z 800k na 1,2 mil. Kč. Zisk se mu zvedl z 60k na 120k[cite: 2].")
                st.markdown("<div class='box-red'>Na první pohled super. Z finanční analýzy ale zjistíme, že mu klesla okamžitá likvidita (z 0,32 na 0,15) a prodloužila se doba inkasa pohledávek (na 32 dní). Firma sice vydělává, ale může mít problém platit včas![cite: 2]</div>", unsafe_allow_html=True)

    # --- SEKCE 6: AKTIVITY A SLOVNÍK ---
    elif selected_section_2 == "6. Interaktivní vrstva a Slovník":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 6</div>", unsafe_allow_html=True)
        st.markdown("## 6. Interaktivní vrstva a Slovník")
        
        with st.container(border=True):
            st.markdown("### 📚 Slovník cizích pojmů[cite: 2]")
            st.markdown("""
            <div class='box-gray' style='font-size: 0.85rem;'>
            <strong>Aktiva:</strong> Majetek firmy nebo člověka; např. peníze, zásoby, stroje[cite: 2].<br>
            <strong>Pasiva:</strong> Zdroje financování majetku firmy (vlastní kapitál, dluhy)[cite: 2].<br>
            <strong>Akcie:</strong> Cenný papír představující podíl na akciové společnosti[cite: 2].<br>
            <strong>Dluhopis:</strong> Cenný papír, kterým si emitent půjčuje peníze a slibuje jejich splacení s úrokem[cite: 2].<br>
            <strong>Blockchain:</strong> Sdílený digitální záznam transakcí, rozdělený do bloků[cite: 2].<br>
            <strong>Bonita:</strong> Schopnost klienta splácet úvěr, kterou banka posuzuje[cite: 2].<br>
            <strong>Cashflow:</strong> Tok peněz. Ukazuje, kolik peněz skutečně přišlo a odešlo[cite: 2].<br>
            <strong>Diverzifikace:</strong> Rozložení peněz do více investic[cite: 2].<br>
            <strong>Emitent:</strong> Ten, kdo vydává cenný papír (stát, firma)[cite: 2].<br>
            <strong>RPSN:</strong> Roční procentní sazba nákladů úvěru[cite: 2].
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 🎯 Závěrečný Kvíz: Zvládl/a jsi finance v běžném životě?")
            
            with st.expander("❓ 1. Jaký je zásadní rozdíl v ručení za dluhy mezi OSVČ a společníkem v s.r.o.?[cite: 2]"):
                st.write("**Odpověď:** OSVČ ručí celým osobním majetkem, společník s.r.o. ručí omezeně. Firma s.r.o. funguje jako oddělená právnická osoba[cite: 2].")

            with st.expander("❓ 2. Co přesně znamená zkratka MVP v metodice Lean Startup?[cite: 2]"):
                st.write("**Odpověď:** Minimum Viable Product. Je to nejmenší a nejjednodušší verze produktu, která umožní levně ověřit zájem zákazníků[cite: 2].")

            with st.expander("❓ 3. Proč by měla firma sledovat Cashflow, i když je v zisku?[cite: 2]"):
                st.write("**Odpověď:** Zisk je jen účetní rozdíl. Zákazníci mohou platit pozdě. Pokud firma nemá reálnou hotovost (cashflow) na zaplacení účtů, může zkrachovat[cite: 2].")

            with st.expander("❓ 4. Který z těchto nástrojů se nejvíce hodí na uchování finanční rezervy? a) Akcie b) Spořicí účet c) Krypto"):
                st.write("**Odpověď: b) Spořicí účet.** Rezerva musí být bezpečně a rychle dostupná (likvidní). Akcie a krypto jsou příliš rizikové (kolísají)[cite: 2].")

# ==========================================
# POKROKY A UČITEL
# ==========================================
elif view == "Pokroky":
    st.markdown("<span class='hero-badge'>Studentská zóna</span>", unsafe_allow_html=True)
    st.title("Moje pokroky")
    st.markdown("<p style='font-size: 1rem; color: #64748b; margin-bottom: 2rem;'>Přehled dokončených kapitol a úkolů.</p>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        with st.container(border=True): st.metric(label="Dokončené kapitoly", value="2 / 6", delta="33 %")
    with c2:
        with st.container(border=True): st.metric(label="Test právní formy", value="Hotovo", delta="OSVČ vs s.r.o.")
    with c3:
        with st.container(border=True): st.metric(label="Aktivní kalkulace", value="Bod zvratu", delta="Dokončeno")

elif view == "Ucitel":
    st.markdown("<span class='hero-badge'>Metodik & Dashboard</span>", unsafe_allow_html=True)
    st.title("Učitelská základna")
    st.markdown("<p style='font-size: 1rem; color: #64748b; margin-bottom: 2rem;'>Metodické pokyny a sledování práce jednotlivých žáků podle tříd.</p>", unsafe_allow_html=True)
    tab_prehled, tab_metodika = st.tabs(["Přehled žáků a tříd", "Metodické plány do hodin"])
    with tab_prehled:
        with st.container(border=True):
            col_treda, col_zak = st.columns(2)
            with col_treda: selected_class = st.selectbox("Vyberte třídu:", ["3.A", "3.B", "4.A"])
            with col_zak: selected_student = st.selectbox("Vyberte žáka:", ["Jan Novák", "Ema Dvořáková"])
            st.divider()
            st.subheader(f"Karta žáka: {selected_student}")
            st.markdown("**Vyplněné úkoly (KAP 1 a 2):**\n- Podnikatelský záměr\n- Výpočet hodinové sazby OSVČ\n- Bod zvratu")
    with tab_metodika:
        with st.container(border=True):
            st.write("1. Analýza firem v rejstříku (Justice.cz)")
            st.write("2. Skupinová práce na výpočtu Cashflow modelové firmy.")
