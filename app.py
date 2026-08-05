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
    st.markdown("<div style='padding: 0.5rem 0;'><span style='font-size: 0.7rem; font-weight: 700; color: #6366f1; text-transform: uppercase;'>E-Learning Portal</span><h2 style='margin: 0; padding: 0; border: none; font-size: 1.25rem; font-weight: 800;'>Učebnice Ekonomiky</h2></div>", unsafe_allow_html=True)
    st.divider()

    is_uvod = st.session_state["current_view"] == "Uvod"
    if st.button("Úvodní stránka", use_container_width=True, type="primary" if is_uvod else "secondary"):
        st.session_state["current_view"] = "Uvod"
        st.rerun()

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
        if st.button(title, use_container_width=True, type="primary" if is_active else "secondary"):
            st.session_state["current_view"] = key
            st.rerun()

    st.markdown("<div class='sidebar-section-title'>STUDIUM A METODIKA</div>", unsafe_allow_html=True)
    if st.button("Moje pokroky", use_container_width=True, type="primary" if st.session_state["current_view"] == "Pokroky" else "secondary"):
        st.session_state["current_view"] = "Pokroky"
        st.rerun()
    if st.button("Učitelská základna", use_container_width=True, type="primary" if st.session_state["current_view"] == "Ucitel" else "secondary"):
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
    st.markdown("<p style='font-size: 1.05rem; color: #64748b; margin-bottom: 2rem;'>Moderní učebnice ekonomiky pro střední školy.</p>", unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown("## Začni tady")
        st.write("Tahle stránka je hlavní rozcestník učebnice. Najdeš tu obsah, pravidla práce, výstupy kapitol, společné nástroje a odkaz do učitelského řídícího centra.")
        st.markdown("<div class='box-green'><strong>Cíl učebnice:</strong> Žák má umět propojit nápad, zákazníka, peníze, práci, stát, daně, marketing, rizika a odpovědnost do jednoho praktického rozhodování.</div>", unsafe_allow_html=True)

# ==========================================
# KAPITOLA 1: PODNIKAVOST A STARTUPY
# ==========================================
elif view == "Kapitola 1":
    st.markdown("<span class='hero-badge'>Kapitola 1</span>", unsafe_allow_html=True)
    st.title("Podnikavost a startupová kultura")
    section_options = ["1. Podnikatel a základní pojmy", "2. Slovníček", "3. OSVČ a živnosti", "4. Obchodní korporace", "5. Startup", "6. Podnikatelský záměr", "7. Lean Canvas", "8. CSR a etika", "9. Rizika", "10. Švarcsystém", "11. Logická mapa"]
    selected_section = st.selectbox("📌 Přechod na podkapitolu:", section_options, index=0)
    st.divider()

    if selected_section == "1. Podnikatel a základní pojmy":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 1</div><h2>1. Podnikatel a základní pojmy</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("<div class='box-blue'><strong>Hlavní definice:</strong> Zákon chápe podnikání jako soustavnou činnost prováděnou samostatně, vlastním jménem, na vlastní odpovědnost, za účelem dosažení zisku.</div>", unsafe_allow_html=True)
            st.write("Podnikání dnes nemusí začínat kanceláří. Může začít mobilem, profilem na sociální síti nebo e-shopem.")
            st.markdown("### Tvůj úkol: Je to podnikání?")
            st.selectbox("1. Student jednou prodá starý mobil:", ["Vyber odpověď...", "Koníček", "Jednorázový přivýdelek", "Zaměstnání", "Podnikání"])
            if st.button("Uložit vyhodnocení"): st.success("Uloženo!")

    elif selected_section == "2. Slovníček":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2</div><h2>2. Slovníček základních pojmů</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("**Podnikatel:** Osoba, která samostatně vykonává výdělečnou činnost na vlastní účet a odpovědnost...")
            st.write("**Právnická osoba:** Organizovaný subjekt, který má právní osobnost (např. s.r.o.).")

    elif selected_section == "3. OSVČ a živnosti":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 3</div><h2>3. OSVČ a živnosti</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("**OSVČ** znamená osoba samostatně výdělečně činná. Jde o podnikání fyzické osoby.")
            st.markdown("#### Mini simulace OSVČ")
            st.slider("Kolik % z tržby si odložit na daně a pojištění?", 10, 50, 30, 5)

    elif selected_section == "4. Obchodní korporace":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 4</div><h2>4. Obchodní korporace</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("Obchodní korporace jsou právnické osoby. Patří mezi ně obchodní společnosti (v.o.s., k.s., s.r.o., a.s.) a družstva.")
            st.radio("1️⃣ Plánuješ podnikat sám/sama, nebo v týmu?", ["Spíš OSVČ", "Spíš s.r.o."])

    elif selected_section == "5. Startup":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 5</div><h2>5. Startup: nápad, který hledá funkční byznys</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("Startup je mladý podnikatelský projekt, který hledá opakovatelný a škálovatelný způsob, jak řešit problém zákazníka.")
            st.radio("Co uděláš jako první?", ["A) Utratím 200k za vývoj", "B) Udělám jednoduchý dotazník"])

    elif selected_section == "6. Podnikatelský záměr":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 6</div><h2>6. Podnikatelský záměr</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("#### 🧮 Kalkulačka bodu zvratu")
            c1, c2, c3 = st.columns(3)
            with c1: price = st.number_input("Cena (Kč):", value=150)
            with c2: var_cost = st.number_input("Var. náklad (Kč):", value=80)
            with c3: fix_cost = st.number_input("Fix. náklady (Kč):", value=2800)
            if price - var_cost > 0:
                st.success(f"Bod zvratu: {fix_cost / (price - var_cost):.1f} kusů měsíčně.")

    elif selected_section == "7. Lean Canvas":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 7</div><h2>7. Lean Canvas</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("Rychlá mapa podnikatelského nápadu. Začni Problémem a Zákazníkem.")

    elif selected_section == "10. Švarcsystém":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 10</div><h2>10. Švarcsystém</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("<div class='box-red'><strong>Švarcsystém:</strong> Zastřený pracovněprávní vztah je nelegální. Člověk vystupuje jako OSVČ, ale pracuje jako zaměstnanec.</div>", unsafe_allow_html=True)

    elif selected_section == "11. Logická mapa":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 11</div><h2>11. Logická mapa podnikání</h2>", unsafe_allow_html=True)
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
        st.info("Zvolte sekci v horním menu.")

# ==========================================
# KAPITOLA 2: FINANCE A OSOBNÍ MANAGEMENT
# ==========================================
elif view == "Kapitola 2":
    st.markdown("<span class='hero-badge'>Kapitola 2</span>", unsafe_allow_html=True)
    st.title("Finance v běžném životě")
    st.markdown("<p style='font-size: 1rem; color: #64748b; margin-bottom: 1.5rem;'>Peníze, rozhodování a odpovědnost v 21. století.</p>", unsafe_allow_html=True)

    section_options_2 = [
        "2.1 Bankovní systém a peníze",
        "2.2 Osobní finance a rozpočet",
        "2.3 Finanční trh a analýza rizik",
        "2.4 Úvěry, pojištění a majetek",
        "2.5 Finanční řízení podniku",
        "2.6 Slovník a Aktivity"
    ]

    selected_section_2 = st.selectbox("📌 Přechod na podkapitolu:", section_options_2, index=0)
    st.divider()

    # --- 2.1 BANKOVNÍ SYSTÉM ---
    if selected_section_2 == "2.1 Bankovní systém a peníze":
        st.markdown("<div class='sub-section-header'>SEKCE 1</div><h2>Bankovní systém a peníze v 21. století</h2>", unsafe_allow_html=True)
        
        with st.container(border=True):
            st.write("21. století není jen éra umělé inteligence a sociálních sítí. Je to především éra transformace toho, jak vnímáme hodnotu. Peníze dnes nevypadají jen jako mince. Jsou to data.")
            st.markdown("""
            <div class='box-blue'>
                <strong>Základní myšlenka:</strong> Peníze nejsou jen „věc“. Jsou to hlavně důvěryhodný záznam hodnoty, kterému lidé, firmy a stát věří.
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("### Vývoj peněz v čase")
            st.markdown("""
            | Období / forma | Co sloužilo jako peníze | Na čem stála důvěra |
            | :--- | :--- | :--- |
            | **Naturální směna** | Zboží za zboží | Na přímé dohodě dvou lidí |
            | **Komoditní peníze** | Sůl, obilí, dobytek, mušle, kovy | Na užitečnosti nebo vzácnosti věci |
            | **Mince** | Kovové mince | Na kovu, hmotnosti, ryzosti a autoritě vydavatele |
            | **Bankovky** | Papírové peníze | Na důvěře ve stát, banku a zákonné platidlo |
            | **Bezhotovostní peníze**| Zůstatek na účtu | Na bankovním systému, pravidlech a dohledu |
            | **Digitální platby** | Data v bankovních systémech | Na ověření identity, zabezpečení a infrastruktuře |
            | **Kryptoměny** | Distribuovaný záznam | Na technologii, síti uživatelů a protokolu |
            """)

        with st.container(border=True):
            st.markdown("### Česká národní banka (ČNB) vs. Komerční banky")
            st.markdown("""
            <div class='box-gray'>
                <strong>ČNB:</strong> Centrální banka státu. Neobsluhuje běžné občany. Její cíl je stabilita měny a dohled nad trhem. Zasahuje do ekonomiky určováním základních úrokových sazeb.<br><br>
                <strong>Komerční banky:</strong> Subjekty, se kterými běžně pracujeme (např. KB, ČSOB, Česká spořitelna). Přijímají vklady a poskytují úvěry lidem i firmám.
            </div>
            """, unsafe_allow_html=True)

            with st.expander("🎮 Simulace: Jsi bankovní rada ČNB!"):
                st.write("**Situace:** Inflace je vysoká, ceny v obchodech letí nahoru. Firmám i lidem se zdražuje život. Co uděláte s úrokovou sazbou?")
                cnb_action = st.radio("Vaše rozhodnutí:", ["Zvýšíme sazby", "Snížíme sazby", "Necháme sazby beze změny"])
                if st.button("Potvrdit rozhodnutí"):
                    if "Zvýšíme" in cnb_action:
                        st.success("Správný krok k tlumení inflace! Úvěry zdraží, lidé budou méně utrácet a více spořit. Tím se tlak na růst cen sníží.")
                    else:
                        st.error("Rizikové! Pokud nesnížíte objem peněz v oběhu, inflace může dál růst.")

        with st.container(border=True):
            st.markdown("### Platební styk a Fintech")
            st.write("Platební styk je infrastruktura důvěry. Když posíláš peníze ze své banky do jiné (např. platíš na e-shopu), platba v ČR probíhá přes mezibankovní systém **CERTIS**, který spravuje ČNB.")
            
            st.markdown("#### Fintech a Neobanky")
            st.write("Služby jako **Revolut** nebo **Wise** přesunuly finance z poboček do mobilu. Jsou rychlé, levné pro směnu měn a moderní. Ne každá finanční aplikace ale má plnou bankovní licenci s pojištěním vkladů do 100 000 EUR.")

            with st.expander("🚨 Phishing Escape Room: Odhal podvod"):
                st.write("Přečti si SMS, která ti právě přišla na mobil:")
                st.info("„Vaše karta byla dočasně zablokována z bezpečnostních důvodů. Pro její odblokování klikněte na tento odkaz a zadejte svůj PIN: www.bezpecnabanka-cz.net/login“")
                st.markdown("<div class='box-red'><strong>VAROVÁNÍ:</strong> Tlak na rychlost (odblokování). Podezřelý odkaz (není to oficiální web banky). Banka NIKDY nechce PIN přes SMS! Zprávu ignoruj a smaž.</div>", unsafe_allow_html=True)

    # --- 2.2 OSOBNÍ FINANCE ---
    elif selected_section_2 == "2.2 Osobní finance a rozpočet":
        st.markdown("<div class='sub-section-header'>SEKCE 2</div><h2>Osobní finance, rozpočet a psychologie</h2>", unsafe_allow_html=True)
        
        with st.container(border=True):
            st.write("Finanční gramotnost v 21. století znamená umět zacházet s penězi i s digitálním prostředím, které naše finanční rozhodování ovlivňuje. Aplikace, slevy, předplatná a odložené platby nás vedou k rychlému utrácení.")
            
            st.markdown("### Rozpočet: Mapa peněz")
            st.write("Rozpočet ukazuje, odkud peníze přicházejí a kam odcházejí.")
            st.markdown("""
            | Typ výdaje | Příklad |
            | :--- | :--- |
            | **Fixní** | Nájem, paušál na telefon, splátka úvěru. (Musíš platit každý měsíc). |
            | **Proměnlivý** | Jídlo, doprava, zábava, drogerie. (Dá se upravit). |
            | **Skrytý** | Automatické předplatné (Netflix, Spotify), mikrotransakce ve hrách. |
            """)
            st.markdown("<div class='box-green'><strong>Model 50–30–20:</strong> 50 % příjmů na potřeby, 30 % na přání (radosti) a 20 % na rezervu nebo splácení dluhů.</div>", unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### Algoritmy bohatství")
            st.markdown("""
            <div class='box-blue'>
                1. <strong>Zaplať nejdřív sobě:</strong> Odlož si peníze na rezervu hned, jak ti přijde výplata/brigáda. Nečekej, co ti zbyde na konci měsíce.<br>
                2. <strong>Rezerva:</strong> Slouží jako finanční airbag. Ideálně bys měl mít našetřeno 3 až 6 měsíčních nutných výdajů.<br>
                3. <strong>Vyhni se drahému dluhu:</strong> Spotřebitelské půjčky na elektroniku tě brzdí.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### Matematika peněz: Úrok a Inflace")
            st.write("Inflace znamená růst cenové hladiny. Za stejnou stokorunu si zítra koupíš méně než dnes.")
            st.markdown("""
            **Jednoduché úročení:** Úrok se počítá stále jen z původní částky.<br>
            **Složené úročení:** Úročí se i již připsané úroky. Tvoje peníze vydělávají další peníze (ideální pro dlouhodobé spoření).
            """)

        with st.container(border=True):
            st.markdown("### Psychologie utrácení")
            st.write("Často se nerozhodujeme racionálně. E-shopy a reklamy využívají psychologické pasti.")
            st.markdown("""
            * **FOMO (Fear Of Missing Out):** Strach, že propásneme "jedinečnou" akci. (Obrana: Počkej 24 hodin před nákupem).
            * **Odložená platba (BNPL):** Nákup nebolí hned, odloží se o 30 dní. Mozek má pocit, že je to levnější. (Obrana: Ber to jako skutečný dluh).
            * **Sociální srovnávání:** Kupujeme věci, abychom vypadali úspěšně před ostatními na sítích.
            """)

            st.markdown("#### ⏳ Kalkulačka času: Kolik života tě to stálo?")
            st.write("Cena věci není jen částka v korunách. Je to i čas tvého života, který jsi musel/a strávit v práci.")
            
            c_time1, c_time2, c_time3 = st.columns(3)
            with c_time1:
                item_price = st.number_input("Cena věci (Kč):", value=2400, step=100)
            with c_time2:
                hourly_wage = st.number_input("Tvoje čistá hodinová mzda (Kč):", value=150, step=10)
            with c_time3:
                if hourly_wage > 0:
                    hours_needed = item_price / hourly_wage
                    st.info(f"**Musíš pracovat:**\n### {hours_needed:.1f} hodin")

    # --- 2.3 FINANČNÍ TRH A INVESTICE ---
    elif selected_section_2 == "2.3 Finanční trh a analýza rizik":
        st.markdown("<div class='sub-section-header'>SEKCE 3</div><h2>Finanční trh a investování</h2>", unsafe_allow_html=True)
        
        with st.container(border=True):
            st.write("Finanční trh přesouvá peníze v čase. Někdo má peníze a chce je zhodnotit (investor). Někdo je potřebuje (firma, stát) a je ochoten zaplatit úrok nebo podíl na zisku.")
            
            st.markdown("### Investiční trojúhelník")
            st.markdown("""
            <div class='box-purple'>
                <strong>1. Výnos:</strong> To, co získáš navíc (úrok, dividenda, nárůst ceny).<br>
                <strong>2. Riziko:</strong> Možnost, že výsledek bude jiný, než jsi čekal (ztráta peněz).<br>
                <strong>3. Likvidita:</strong> Jak rychle umíš investici prodat a přeměnit zpět na hotovost.
            </div>
            """, unsafe_allow_html=True)
            st.warning("Pravidlo: Pokud někdo slibuje obrovský výnos, nulové riziko a okamžitou dostupnost peněz, je to téměř jistě podvod.")

        with st.container(border=True):
            st.markdown("### Spoření vs. Investování vs. Spekulace")
            st.markdown("""
            | Pojem | Co to je? | Příklad | Riziko |
            | :--- | :--- | :--- | :--- |
            | **Spoření** | Ochrana a dostupnost peněz. | Spořicí účet v bance. | Nízké, ale ztrácí na inflaci. |
            | **Investování** | Dlouhodobé zhodnocení peněz. | Akcie, Dluhopisy, ETF fondy. | Střední až vysoké. |
            | **Spekulace** | Sázka na krátkodobý pohyb ceny. | Nákup meme krypto coinů. | Extrémně vysoké (Hazard). |
            """)

        with st.container(border=True):
            st.markdown("### Základní cenné papíry")
            st.write("Cenný papír představuje nějaké právo. Dnes už většinou nejde o papír, ale o elektronický (zaknihovaný) záznam.")
            
            st.markdown("""
            * **Akcie (Podíl):** Kupuješ si malý kousek firmy (např. Apple, ČEZ). Máš právo na podíl ze zisku (dividendu). Pokud firma krachne, tvůj podíl klesá na nulu.
            * **Dluhopis (Půjčka):** Stát nebo firma potřebuje peníze, tak vydá dluhopis. Ty si ho koupíš (půjčíš jim) a oni ti pravidelně platí úrok a na konci vrátí vklad. Pokud emitent zkrachuje, o peníze přijdeš.
            * **Podílové fondy a ETF (Košík):** Abys nesázel vše na jednu kartu (jednu firmu), koupíš si ETF. To je "košík", ve kterém jsou stovky akcií najednou (např. index S&P 500 obsahující 500 největších amerických firem).
            """)

        with st.container(border=True):
            st.markdown("### Kryptoměny a Blockchain")
            st.write("Kryptoměny fungují na technologii Blockchain – sdílené účetní knize, kterou nekontroluje žádná centrální banka, ale síť uživatelů.")
            
            st.markdown("""
            <div class='box-gray'>
                <strong>Příklady:</strong><br>
                • <strong>Bitcoin:</strong> První a nejznámější. Digitální vzácnost. Může extrémně kolísat (volatilita).<br>
                • <strong>Ethereum:</strong> Síť, která kromě plateb umí spouštět i chytré kontrakty (Smart Contracts).<br>
                • <strong>Stablecoiny:</strong> Mince vázané např. na kurz Dolaru.
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<div class='box-red'><strong>Největší rizika kryptoměn:</strong> Volatilita (cena spadne přes noc o 30 %), ztráta privátního klíče (seed phrase = ztratíš přístup navždy, banka to neobnoví), hack burzy a podvody influencerů slibujících bohatství.</div>", unsafe_allow_html=True)

    # --- 2.4 ÚVĚRY A POJIŠTĚNÍ ---
    elif selected_section_2 == "2.4 Úvěry, pojištění a majetek":
        st.markdown("<div class='sub-section-header'>SEKCE 4</div><h2>Úvěry a pojištění</h2>", unsafe_allow_html=True)
        
        with st.container(border=True):
            st.write("Úvěr přesouvá spotřebu z budoucnosti do současnosti. Když si půjčíš, nekupuješ si jen věc. Kupuješ si čas. A za ten se platí.")
            
            st.markdown("### Úrok a RPSN")
            st.markdown("""
            * **Úroková sazba:** Procento, které zaplatíš navíc za půjčení peněz. Banky s ním často dělají reklamu.
            * **RPSN (Roční procentní sazba nákladů):** Skutečná, celková cena úvěru za rok. Zahrnuje úrok, ale i poplatky za vedení účtu, vyřízení půjčky atd. **Při porovnávání půjček sleduj vždy RPSN!**
            """)

            st.markdown("### Typy úvěrů")
            st.markdown("""
            | Typ | Charakteristika |
            | :--- | :--- |
            | **Hypotéka** | Úvěr na bydlení zajištěný nemovitostí. Banka nepůjčí 100 % ceny (sleduje ukazatel LTV). Úrok je nižší, protože banka má zástavu. |
            | **Spotřebitelský úvěr** | Půjčka na auto, elektroniku. Není zajištěný, proto má vyšší úrok a RPSN. |
            | **Kreditní karta** | Peníze banky. Pokud dluh splatíš v bezúročném období (např. do 45 dnů), je to zdarma. Pokud ne, naskočí obrovský úrok (klidně 20+ %). |
            | **BNPL (Kup teď, zaplať později)** | Nákupy na e-shopech (Twisto, Klarna). Skrývá pocit dluhu za tlačítko "pohodlné platby". |
            """)

            with st.expander("🤔 Komu banka (ne)půjčí?"):
                st.write("Banka neschválí půjčku každému. Posuzuje tzv. Bonitu klienta. Zkoumá: Věk, stálý příjem, výdaje (děti, nájem), dluhy u jiných bank a zkontroluje tě v Registru dlužníků (zda jsi v minulosti platil/a včas).")

        with st.container(border=True):
            st.markdown("### Pojištění (Ochrana majetku a zdraví)")
            st.write("Pojištění nezabrání tomu, aby se něco stalo (požár, úraz), ale zabrání tomu, aby tě taková událost finančně zruinovala.")
            
            st.markdown("""
            <div class='box-green'>
                <strong>1. Životní pojištění:</strong> Chrání výpadek příjmu při vážné nemoci, invaliditě nebo úmrtí (hlavně pokud máš hypotéku a rodinu).<br>
                <strong>2. Pojištění majetku (Nemovitost vs. Domácnost):</strong> Pojištění nemovitosti chrání zdi a střechu (např. při požáru). Pojištění domácnosti chrání to, co z domu vypadne, když ho obrátíš vzhůru nohama (nábytek, TV).<br>
                <strong>3. Pojištění odpovědnosti (Pojistka na blbost):</strong> Kryje tě, když někomu způsobíš škodu (vytopíš souseda, srazíš někoho na lyžích).
            </div>
            """, unsafe_allow_html=True)
            st.error("Pozor na PODPOJIŠTĚNÍ! Pokud máš dům pojištěný na 3 miliony, ale jeho aktuální hodnota vzrostla na 6 milionů, pojišťovna ti při zničení domu vyplatí výrazně méně.")

    # --- 2.5 FINANČNÍ ŘÍZENÍ PODNIKU ---
    elif selected_section_2 == "2.5 Finanční řízení podniku":
        st.markdown("<div class='sub-section-header'>SEKCE 5</div><h2>Finanční řízení v podniku</h2>", unsafe_allow_html=True)
        
        with st.container(border=True):
            st.write("Firma může mít skvělý produkt, tisíce sledujících na Instagramu, ale pokud neumí řídit finance (ziskovost, dluhy, cashflow), zkrachuje.")

            st.markdown("### Mapa firmy v číslech (Výkazy)")
            st.markdown("""
            * **Rozvaha:** Fotografie firmy k určitému datu. Ukazuje, jaký má firma MAJETEK (Aktiva = hotovost, stroje, zásoby) a z čeho ho financovala (Pasiva = vlastní vklad majitele, cizí dluh od banky). Platí: Aktiva = Pasiva.
            * **Výkaz zisku a ztráty:** Film za daný rok. Ukazuje VÝNOSY (tržby z prodeje) mínus NÁKLADY (mzdy, materiál, nájem). Výsledkem je Zisk nebo Ztráta.
            * **Cashflow (Tok peněz):** To nejdůležitější! Sleduje skutečný pohyb peněz. Firma může v účetnictví vykazovat Zisk (vystavila faktury), ale pokud jí zákazníci nezaplatili, chybí jí hotovost (Cashflow) na zaplacení mezd a firma může padnout.
            """)

        with st.container(border=True):
            st.markdown("### Bod zvratu (Break-even point)")
            st.write("Kolik kusů musím prodat, aby tržby pokryly všechny fixní a variabilní náklady a firma začala být v plusu?")
            
            st.markdown("""
            * **Fixní náklady (FN):** Platíš je, i když nic neprodáš (nájem, software, účetní).
            * **Variabilní náklady (VN):** Rostou s každým vyrobeným kusem (materiál na tričko, poštovné).
            """)

            st.info("**Vzorec:** Bod Zvratu (v kusech) = Fixní náklady / (Prodejní cena za 1 kus - Variabilní náklad na 1 kus)")

        with st.container(border=True):
            st.markdown("### Finanční analýza (Ukazatele zdraví)")
            st.write("Z účetních dat počítáme poměry, abychom zjistili, jak je na tom firma oproti konkurenci nebo loňskému roku.")
            
            st.markdown("""
            | Co měříme | Ukazatel a Vzorec | Jak to číst |
            | :--- | :--- | :--- |
            | **Ziskovost (Rentabilita)** | **ROS** (Zisk / Tržby) | Kolik % z každé stokoruny tržeb mi zůstane jako čistý zisk v kapse. |
            | **Zadluženost** | **Míra dluhu** (Cizí zdroje / Aktiva) | Kolik procent majetku firmy vlastně patří bance. |
            | **Likvidita** | **Běžná likvidita** (Oběžná aktiva / Krátkodobé závazky) | Zda mám dost rychle dostupných peněz na zaplacení faktur, co brzy přijdou. |
            """)

            with st.expander("🔎 Case Study: E-shop DropZone (Modelový případ)"):
                st.write("E-shop zvýšil meziročně tržby z 800k na 1,2 mil. Kč. Zisk se mu zvedl z 60k na 120k. Vypadá to skvěle!")
                st.markdown("<div class='box-red'>Ale pozor! Z finanční analýzy zjistíme, že mu klesla Hotovost na účtu (Okamžitá likvidita šla z 0,32 na 0,15) a prodloužila se Doba inkasa pohledávek. Zákazníci mu platí pozdě, jemu chybí Cashflow na zaplacení dodavatelům. Roste příliš rychle na dluh.</div>", unsafe_allow_html=True)

    # --- 2.6 AKTIVITY A SLOVNÍK ---
    elif selected_section_2 == "2.6 Slovník a Aktivity":
        st.markdown("<div class='sub-section-header'>SEKCE 6</div><h2>Závěrečné aktivity a Slovník</h2>", unsafe_allow_html=True)
        
        with st.container(border=True):
            st.markdown("### 📚 Slovník důležitých pojmů")
            st.markdown("""
            <div class='box-gray' style='font-size: 0.85rem;'>
            <strong>Aktiva:</strong> Majetek firmy (peníze, stroje).<br>
            <strong>Pasiva:</strong> Zdroje financování (vlastní peníze, dluhy).<br>
            <strong>Akcie:</strong> Cenný papír, podíl na firmě (akcionář má nárok na dividendu).<br>
            <strong>Dluhopis:</strong> Cenný papír, kterým si firma/stát půjčuje peníze a platí úrok.<br>
            <strong>Blockchain:</strong> Sdílený digitální záznam, databáze (např. pro Bitcoin).<br>
            <strong>Bonita:</strong> Schopnost klienta splácet dluh, kterou zkoumá banka.<br>
            <strong>Cashflow:</strong> Skutečný tok peněz do firmy a ven.<br>
            <strong>Diverzifikace:</strong> Rozložení rizika (nedávat všechna vejce do jednoho košíku).<br>
            <strong>Emitent:</strong> Ten, kdo vydává cenný papír (firma vydávající dluhopis).<br>
            <strong>RPSN:</strong> Roční procentní sazba nákladů (skutečná cena úvěru s poplatky).
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 🎯 Kvíz: Zvládl/a jsi finance v běžném životě?")
            
            with st.expander("1. Co ti hrozí, když máš rezervu zainvestovanou v kryptoměnách?"):
                st.write("**Odpověď:** Kryptoměny jsou vysoce volatilní (skáčou nahoru a dolů). Pokud se ti rozbije auto ve chvíli, kdy krypto spadne o 40 %, vybereš si rezervu s obrovskou ztrátou. Rezerva patří na bezpečný spořicí účet.")

            with st.expander("2. Banka A ti nabízí úrok 6 % a RPSN 8 %. Banka B nabízí úrok 7 % a RPSN 7,2 %. Co je levnější?"):
                st.write("**Odpověď:** Levnější je Banka B. Sice má vyšší "reklamní" úrok, ale mnohem nižší vedlejší poplatky, takže celkové RPSN (skutečná cena) je nižší.")

            with st.expander("3. Rozdíl mezi Pojištěním nemovitosti a domácnosti?"):
                st.write("**Odpověď:** Nemovitost jsou zdi, střecha, okna. Domácnost je to, co vypadne, když dům obrátíš (TV, gauč, oblečení).")

            with st.expander("4. Proč je u akcií a ETF důležitý 'Časový horizont'?"):
                st.write("**Odpověď:** Akciové trhy v krátkém čase kolísají (mohou klesnout kvůli krizím). Pokud investuješ na 10 a více let, má trh čas se ze ztrát zotavit a projeví se síla složeného úročení.")

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
