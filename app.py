import streamlit as st

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

# ==========================================
# KAPITOLA 1: PODNIKAVOST A STARTUPY
# ==========================================
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
        "6. Lean Canvas",
        "7. CSR, etika a odpovědné podnikání",
        "8. Rizika podnikání",
        "9. Švarcsystém",
        "10. Ověřování informací a užitečné zdroje",
        "11. Ukončení podnikání",
        "12. Logická mapa podnikání",
        "13. Reflexe a sebehodnocení",
        "14. Integrované opakování"
    ]

    selected_section = st.selectbox("📌 Přechod na podkapitolu:", section_options, index=0)
    st.divider()

    # --- 1. Podnikatel a základní pojmy ---
    if selected_section == "1. Podnikatel a základní pojmy":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 1</div><h2>1. Podnikatel a základní pojmy</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("Zákon chápe podnikání jako soustavnou činnost prováděnou samostatně, vlastním jménem, na vlastní odpovědnost, za účelem dosažení zisku[cite: 3].")
            st.markdown("""
            <div class='box-blue'>
                <strong>Přesná zákonná opora:</strong> Podnikatele definuje zákon č. 89/2012 Sb., občanský zákoník, zejména § 420 odst. 1: „Kdo samostatně vykonává na vlastní účet a odpovědnost výdělečnou činnost živnostenským nebo obdobným způsobem se záměrem činit tak soustavně za účelem dosažení zisku...“[cite: 3]
            </div>
            """, unsafe_allow_html=True)
            st.write("Podnikání dnes nemusí začínat kanceláří. Může začít mobilem, profilem na sociální síti, prodejem digitální šablony nebo e-shopem[cite: 3].")
            
            st.markdown("### Čtyři znaky podnikání[cite: 3]")
            st.markdown("""
            | Znak podnikání | Co znamená | Příklad ze současnosti |
            | :--- | :--- | :--- |
            | **Soustavnost** | Činnost se opakuje nebo je plánovaná dlouhodobě[cite: 3]. | Každý měsíc prodávám digitální plánovače[cite: 3]. |
            | **Samostatnost** | Sám rozhoduji o ceně, zákaznících, způsobu práce[cite: 3]. | Nabízím správu sítí lokálním podnikům[cite: 3]. |
            | **Vlastní jméno** | Vystupuji jako podnikatel nebo firma[cite: 3]. | Mám značku, profil, faktury[cite: 3]. |
            | **Vlastní odpovědnost** | Nesu riziko ztráty, reklamací, dluhů[cite: 3]. | Nakoupím materiál, ale nikdo nekoupí[cite: 3]. |
            """)

            st.markdown("<div class='box-yellow'><strong>Tvůj úkol: Je to podnikání?</strong> U každé situace rozhodni, zda jde o koníček, jednorázový přivýdělek, zaměstnání nebo podnikání[cite: 3].</div>", unsafe_allow_html=True)
            st.selectbox("Student jednou prodá starý mobil[cite: 3]:", ["Vyber odpověď...", "Koníček", "Jednorázový přivýdelek", "Zaměstnání", "Podnikání"])
            st.selectbox("Student každý týden prodává vlastnoručně vyráběné náramky[cite: 3]:", ["Vyber odpověď...", "Koníček", "Jednorázový přivýdelek", "Zaměstnání", "Podnikání"])

    # --- 2. Slovníček základních pojmů ---
    elif selected_section == "2. Slovníček základních pojmů":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2</div><h2>2. Slovníček základních pojmů</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("""
            | Termín | Co znamená | Proč je důležitý |
            | :--- | :--- | :--- |
            | **Fyzická osoba** | Člověk — jednotlivec. V podnikání může vystupovat např. jako OSVČ[cite: 3]. | Rozdíl mezi člověkem a firmou jako právnickou osobou[cite: 3]. |
            | **Právnická osoba** | Organizovaný subjekt s právní osobností (např. s.r.o.)[cite: 3]. | Firma může jednat a vlastnit majetek samostatně[cite: 3]. |
            | **Živnost** | Podnikatelská činnost provozovaná podle živnostenského zákona[cite: 3]. | Pomáhá určit, jaký typ oprávnění řešíš[cite: 3]. |
            | **Švarcsystém** | Člověk formálně vystupuje jako podnikatel, ale pracuje jako zaměstnanec[cite: 3]. | Pomáhá rozpoznat nelegální spolupráci[cite: 3]. |
            """)

    # --- 3. OSVČ a živnosti ---
    elif selected_section == "3. OSVČ a živnosti":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 3</div><h2>3. OSVČ a živnosti</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("OSVČ znamená osoba samostatně výdělečně činná. Jde o podnikání fyzické osoby — tedy člověka, který podniká vlastním jménem a nese plnou odpovědnost[cite: 3].")
            st.markdown("<div class='box-red'><strong>Hlavní riziko OSVČ:</strong> OSVČ ručí za závazky z podnikání celým svým osobním majetkem[cite: 3].</div>", unsafe_allow_html=True)
            
            st.markdown("### Druhy živností[cite: 3]")
            st.markdown("""
            * **Volná:** Není potřeba speciální vzdělání (např. E-shop)[cite: 3].
            * **Řemeslná:** Vyžaduje výuční list nebo praxi (např. Kadeřnictví)[cite: 3].
            * **Vázaná:** Vyžaduje specifické vzdělání (např. Účetní poradenství)[cite: 3].
            * **Koncesovaná:** Vyžaduje státní povolení (např. Taxislužba)[cite: 3].
            """)
            st.markdown("<div class='box-yellow'><strong>Pravidlo pro začátečníka:</strong> To, co přijde na účet, není celé „moje výplata“. Část peněz patří na náklady, daně, sociální a zdravotní pojištění[cite: 3].</div>", unsafe_allow_html=True)

    # --- 4. Obchodní korporace ---
    elif selected_section == "4. Obchodní korporace":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 4</div><h2>4. Obchodní korporace</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("Patří sem obchodní společnosti (v.o.s., k.s., s.r.o., a.s.) a družstva[cite: 3].")
            
            st.markdown("### S.r.o. vs OSVČ: Rychlý test[cite: 3]")
            q1 = st.radio("Plánuješ podnikat sám, nebo v týmu?[cite: 3]", ["Spíš OSVČ: Sám", "Spíš s.r.o.: V týmu"])
            q2 = st.radio("Hrozí větší finanční závazky?[cite: 3]", ["Spíš OSVČ: Ne", "Spíš s.r.o.: Ano"])
            if st.button("Vyhodnotit"):
                if "s.r.o." in q1 and "s.r.o." in q2:
                    st.success("S.r.o. se jeví vhodnější kvůli týmu a riziku[cite: 3].")
                else:
                    st.success("Pro začátek se jeví vhodnější rychlý start jako OSVČ[cite: 3].")

    # --- 5. Startup ---
    elif selected_section == "5. Startup: nápad, který hledá byznys":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 5</div><h2>5. Startup: nápad, který hledá byznys</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("Startup je mladý projekt, který hledá opakovatelný a škálovatelný způsob, jak řešit problém zákazníka[cite: 3].")
            st.markdown("""
            <div class='box-blue'>
                <strong>MVP (Minimum Viable Product):</strong> Nejmenší verze řešení, která dokáže ověřit důležitou otázku. Nemusí být dokonalá. Musí být dostatečná na učení[cite: 3].
            </div>
            """, unsafe_allow_html=True)
            st.markdown("### Metodika Lean Startup[cite: 3]")
            st.write("**Základní cyklus:** Vytvoř — Změř — Pouč se (Build — Measure — Learn)[cite: 3].")

    # --- 6. Lean Canvas ---
    elif selected_section == "6. Lean Canvas":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 6</div><h2>6. Lean Canvas</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("Lean Canvas je rychlá mapa podnikatelského nápadu[cite: 3]. Začíná problémem a zákazníkem[cite: 3].")
            lc_col1, lc_col2, lc_col3 = st.columns(3)
            with lc_col1:
                st.markdown("**1. PROBLÉM**[cite: 3]")
                st.text_area("Jaké hlavní problémy řešíte?[cite: 3]", height=100)
            with lc_col2:
                st.markdown("**4. ŘEŠENÍ**[cite: 3]")
                st.text_area("Jaké řešení navrhujete?[cite: 3]", height=100)
            with lc_col3:
                st.markdown("**2. ZÁKAZNÍCI**[cite: 3]")
                st.text_area("Kdo jsou cíloví zákazníci?[cite: 3]", height=100)

    # --- 7. CSR ---
    elif selected_section == "7. CSR, etika a odpovědné podnikání":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 7</div><h2>7. CSR a ESG</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("CSR znamená společenská odpovědnost firem. ESG sleduje životní prostředí (E), sociální dopady (S) a řízení firmy (G)[cite: 3].")
            st.markdown("<div class='box-red'><strong>Pozor na greenwashing:</strong> Odpovědnost nestačí jen tvrdit v reklamě. Firma by měla umět doložit konkrétní data a výsledky[cite: 3].</div>", unsafe_allow_html=True)

    # --- 8. Rizika podnikání ---
    elif selected_section == "8. Rizika podnikání":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 8</div><h2>8. Rizika podnikání</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("Riziko znamená, že výsledek může být jiný, než očekáváme[cite: 3]. Patří sem tržní riziko, finanční riziko, právní chyba nebo poškození reputace[cite: 3].")

    # --- 9. Švarcsystém ---
    elif selected_section == "9. Švarcsystém":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 9</div><h2>9. Švarcsystém</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("Švarcsystém je situace, kdy člověk formálně vystupuje jako podnikatel, ale fakticky pracuje jako zaměstnanec[cite: 3].")
            st.markdown("<div class='box-red'><strong>Znaky:</strong> Pevná pracovní doba, práce na zařízení firmy, nadřízenost, závislost na jednom zadavateli[cite: 3].</div>", unsafe_allow_html=True)

    # --- 10. Ověřování informací ---
    elif selected_section == "10. Ověřování informací a užitečné zdroje":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 10</div><h2>10. Ověřování informací</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("Při podnikání je důležité umět najít spolehlivé zdroje[cite: 3].")
            st.markdown("""
            * **BusinessInfo.cz** - Oficiální portál pro podnikatele[cite: 3].
            * **Justice.cz** - Veřejný rejstřík, kde lze ověřit firmy a jejich historii[cite: 3].
            """)

    # --- 11. Ukončení podnikání ---
    elif selected_section == "11. Ukončení podnikání":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 11</div><h2>11. Ukončení podnikání</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("**Zrušení = proces:** Rozhodnutí, že firma končí. Může následovat likvidace[cite: 3].")
            st.write("**Zánik = konec:** Definitivní okamžik, kdy firma právně přestává existovat (výmazem z rejstříku)[cite: 3].")
            st.write("**Insolvence:** Pokud má firma více dluhů než majetku a není schopna závazky splácet, může se dostat do úpadku[cite: 3].")

    # --- 12. Logická mapa ---
    elif selected_section == "12. Logická mapa podnikání":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 12</div><h2>12. Logická mapa podnikání</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("""
            <div class="mindmap-wrapper">
                <div class="mm-col">
                    <div class="mm-node"><div class="mm-title">1. Legislativa a definice</div><ul><li>občanský zákoník[cite: 3]</li><li>živnostenský zákon[cite: 3]</li></ul></div>
                    <div class="mm-node"><div class="mm-title">2. Právní formy</div><ul><li>OSVČ, v.o.s.[cite: 3]</li><li>s.r.o., a.s.[cite: 3]</li></ul></div>
                </div>
                <div class="mm-center">PODNIKÁNÍ</div>
                <div class="mm-col">
                    <div class="mm-node"><div class="mm-title">3. Finance a Záměr</div><ul><li>Zákazník, náklady[cite: 3]</li><li>Lean Canvas[cite: 3]</li></ul></div>
                    <div class="mm-node"><div class="mm-title">4. Rizika a Odpovědnost</div><ul><li>Švarcsystém[cite: 3]</li><li>CSR a etika[cite: 3]</li></ul></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # --- 13. Reflexe ---
    elif selected_section == "13. Reflexe a sebehodnocení":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 13</div><h2>13. Reflexe a sebehodnocení</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.checkbox("Umím vysvětlit, co je podnikání a kdo je podnikatel[cite: 3].")
            st.checkbox("Rozliším OSVČ, v.o.s., k.s., s.r.o. a a.s.[cite: 3]")
            st.checkbox("Dokážu navrhnout základ podnikatelského záměru a použít Lean Canvas[cite: 3].")

    # --- 14. Opakování ---
    elif selected_section == "14. Integrované opakování":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 14</div><h2>14. Integrované opakování</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("Závěrečná podnikatelská mise propojuje zákazníka, problém, právní formu, rozpočet, rizika a první ověřitelný test[cite: 3].")
# ==========================================
# KAPITOLA 2: FINANCE A OSOBNÍ MANAGEMENT (BEZ CITE TAGŮ)
# ==========================================
elif view == "Kapitola 2":
    st.markdown("<span class='hero-badge'>Kapitola 2</span>", unsafe_allow_html=True)
    st.title("Finance v běžném životě: peníze, rozhodování a odpovědnost")
    st.markdown("<p style='font-size: 1rem; color: #64748b; margin-bottom: 1.5rem;'>Tahle kapitola propojuje osobní finance, bankovní systém, finanční trh a podnikové finance. Nejde jen o počítání peněz, ale o odpovědné rozhodování.</p>", unsafe_allow_html=True) #[cite: 2]

    with st.container(border=True):
        st.markdown("""
        <div class='box-purple'>
            <strong>🎯 Cíle kapitoly: Co máš po kapitole umět?</strong><br>
            • vysvětlit funkce peněz a princip bankovního systému<br>
            • sestavit jednoduchý osobní rozpočet a tvořit rezervu<br>
            • rozlišit spoření, investování a spekulaci<br>
            • vysvětlit cenu úvěru včetně RPSN<br>
            • propojit osobní finance s finančním řízením podniku
        </div>
        """, unsafe_allow_html=True) #[cite: 2]

    section_options_2 = [
        "2.1 Bankovní systém a peníze v 21. století",
        "2.2 Osobní finance a „Algoritmy bohatství“",
        "2.3 Finanční trh a analýza rizik",
        "2.4 Úvěry, pojištění a ochrana majetku",
        "2.5 Finanční řízení podniku",
        "2.6 Závěrečné aktivity a Slovník"
    ]

    selected_section_2 = st.selectbox("📌 Přechod na podkapitolu (Vyberte téma):", section_options_2, index=0)
    st.divider()

    # --- PODKAPITOLA 2.1 ---
    if selected_section_2 == "2.1 Bankovní systém a peníze v 21. století":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.1</div>", unsafe_allow_html=True)
        st.markdown("## 1. Bankovní systém a peníze v 21. století")
        
        with st.container(border=True):
            st.write("21. století není jen éra umělé inteligence a sociálních sítí. Je to především éra totální transformace toho, jak vnímáme hodnotu. Peníze dnes často nevypadají jako mince nebo bankovky. Jsou to data.") #[cite: 2]
            st.markdown("""
            <div class='box-blue'>
                <strong>Základní myšlenka:</strong> Peníze nejsou jen „věc“. Jsou to hlavně důvěryhodný záznam hodnoty, kterému lidé, firmy a stát věří.
            </div>
            """, unsafe_allow_html=True) #[cite: 2]
            
            st.markdown("### 1.1 Vývoj peněz v čase")
            st.markdown("""
            | Období / forma | Co sloužilo jako peníze | Na čem stála důvěra |
            | :--- | :--- | :--- |
            | **Naturální směna** | Zboží za zboží | Na přímé dohodě dvou lidí |
            | **Komoditní peníze** | Sůl, obilí, dobytek, kovy | Na užitečnosti nebo vzácnosti věci |
            | **Mince** | Kovové mince | Na kovu, hmotnosti, ryzosti a autoritě vydavatele |
            | **Bankovky** | Papírové peníze | Na důvěře ve stát, banku a zákonné platidlo |
            | **Zlatý standard** | Papírové peníze vázané na zlato | Na garanci státu vyměnit bankovky za zlato |
            | **Bezhotovostní peníze**| Zůstatek na účtu | Na bankovním systému, pravidlech a dohledu |
            | **Digitální platby** | Data v bankovních systémech | Na ověření identity, zabezpečení a infrastruktuře |
            | **Kryptoměny** | Distribuovaný záznam (Blockchain) | Na technologii, síti uživatelů a protokolu |
            """) #[cite: 2]

            with st.expander("💡 Přečti si více o Zlatém standardu a Nixonově šoku"):
                st.write("**Zlatý standard:** Stát sliboval, že měna je krytá zlatem. Peníze nebyly jen papírky. Měly být navázané na zásoby zlata, které měl stát k dispozici.") #[cite: 2]
                st.write("**Brettonwoodský systém a Nixonův šok:** Po 2. světové válce byl dolar navázán na zlato. V roce 1971 ale americký prezident Richard Nixon pozastavil směnitelnost dolaru za zlato. Svět se přesunul k „fiat penězům“ – jejich hodnota stojí hlavně na důvěře ve stát a centrální banku.") #[cite: 2]

            st.text_input("🧩 Interaktivní výzva: Vyber jednu komoditu (např. obilí, sůl), která by mohla sloužit jako peníze. V čem by byla praktická a v čem by selhávala?", placeholder="Tvoje odpověď...", key="komodita_vyzva") #[cite: 2]

        with st.container(border=True):
            st.markdown("### 1.2 ČNB a komerční banky")
            st.markdown("""
            <div class='box-gray'>
                <strong>Česká národní banka (ČNB):</strong> Je centrální banka státu. Neobsluhuje běžné občany. Její hlavní cíl je stabilita měny (hlídá inflaci) a dohled nad trhem. Zasahuje do ekonomiky určováním základních úrokových sazeb (např. dvoutýdenní repo sazba).<br><br>
                <strong>Komerční banky:</strong> Subjekty, se kterými běžně pracujeme (např. KB, ČSOB). Přijímají vklady (pasivní operace), poskytují úvěry (aktivní operace) a zajišťují platby (neutrální operace).
            </div>
            """, unsafe_allow_html=True) #[cite: 2]

            with st.expander("🎮 Simulace: Jsi bankovní rada ČNB!"):
                st.write("**Situace:** Inflace je vysoká, ceny v obchodech letí nahoru. Firmám i lidem se zdražuje život. Co uděláte s úrokovou sazbou?") #[cite: 2]
                cnb_action = st.radio("Vaše rozhodnutí:", ["Vyber možnost...", "Zvýšíme sazby", "Snížíme sazby", "Ponecháme sazby beze změny"], key="cnb_sim")
                if st.button("Potvrdit rozhodnutí"):
                    if cnb_action == "Zvýšíme sazby":
                        st.success("Správný krok k tlumení inflace! Úvěry zdraží, lidé budou méně utrácet a více spořit. Tlak na růst cen se sníží.") #[cite: 2]
                    elif cnb_action == "Vyber možnost...":
                        st.warning("Musíš vybrat jednu z možností.")
                    else:
                        st.error("Rizikové! Pokud nesnížíte objem peněz v oběhu (zdražením úvěrů), inflace může dál růst.") #[cite: 2]

        with st.container(border=True):
            st.markdown("### 1.3 Platební styk a Fintech revoluce")
            st.write("Platební styk je infrastruktura důvěry. Umožňuje bezpečně přesouvat peníze. Pokud posíláš peníze v ČR mezi DVĚMA RŮZNÝMI bankami, platba musí projít přes systém **CERTIS**, který provozuje ČNB.") #[cite: 2]
            
            st.markdown("#### Fintech a Neobanky")
            st.write("Služby jako **Revolut** nebo **Wise** mění svět financí. Uživatel očekává rychlost, okamžité notifikace a nízké poplatky. Ne každá finanční aplikace ale má plnou bankovní licenci a pojištění vkladů (do 100 000 EUR).") #[cite: 2]

            st.markdown("#### Digitální bezpečnost")
            st.markdown("""
            <div class='box-red'>
                Karta, mobil nebo hodinky nejsou „peníze samy o sobě“. Jsou to vstupní brány k penězům. Banka po telefonu ani přes SMS nikdy nechce PIN ani autorizační kód!
            </div>
            """, unsafe_allow_html=True) #[cite: 2]

            with st.expander("🚨 Phishing Escape Room: Odhal podvod"):
                st.write("Přečti si e-mail, který ti právě přišel:")
                st.info("„Vážený kliente, vaše karta byla dočasně zablokována z bezpečnostních důvodů. Pro její okamžité odblokování klikněte na tento odkaz a přihlaste se: www.bezpecnabanka-cz.net/login“") #[cite: 2]
                st.markdown("**Správná reakce:** Neklikat na odkaz, nic nevyplňovat! Podvodníci vytvářejí falešný pocit naléhavosti. Situaci ověř přímo ve své oficiální bankovní aplikaci.") #[cite: 2]

    # --- PODKAPITOLA 2.2 ---
    elif selected_section_2 == "2.2 Osobní finance a „Algoritmy bohatství“":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.2</div>", unsafe_allow_html=True)
        st.markdown("## 2. Osobní finance a „Algoritmy bohatství“")
        
        with st.container(border=True):
            st.markdown("### 2.1 Proč je to dnes těžší, než se zdá")
            st.write("Osobní finance nejsou jen otázka toho, kolik člověk vydělává. Jsou to každodenní rozhodnutí: za co utratím peníze, co odložím, co si půjčím a jak poznám riziko.") #[cite: 2]
            st.markdown("""
            <div class='box-red'>
                <strong>Současný problém:</strong> Telefon umožňuje nakoupit, objednat, investovat nebo půjčit si během několika sekund. Finanční chyba tak může vzniknout rychleji než dřív.
            </div>
            """, unsafe_allow_html=True) #[cite: 2]
            
            st.markdown("#### Potřeba vs. Přání")
            st.write("**Potřeba:** Výdaj, bez kterého se neobejdeš nebo který je nutný pro běžné fungování (jídlo, bydlení, doprava do školy, léky).") #[cite: 2]
            st.write("**Přání:** Výdaj, který zvyšuje pohodlí, radost nebo status, ale není nezbytný (značkové oblečení, streamovací služby navíc).") #[cite: 2]

        with st.container(border=True):
            st.markdown("### 2.2 Rozpočet: Mapa peněz")
            st.write("Rozpočet není trest ani omezování života. Je to mapa. Pomáhá zjistit, jestli peníze směřují k tomu, co je pro člověka opravdu důležité.") #[cite: 2]
            st.markdown("""
            | Typ výdaje | Příklad | Otázka ke kontrole |
            | :--- | :--- | :--- |
            | **Fixní** | Nájem, paušál, předplatné, splátka. | Opravdu ho potřebuji každý měsíc? |
            | **Proměnlivý** | Jídlo, doprava, zábava, drogerie. | Dá se upravit bez zásadního poklesu kvality života? |
            | **Skrytý** | Automatické předplatné, mikrotransakce. | Vím, kolik mě stojí za rok? |
            """) #[cite: 2]
            st.markdown("<div class='box-green'><strong>Model 50–30–20:</strong> 50 % na potřeby, 30 % na přání a 20 % na rezervu nebo splácení dluhů.</div>", unsafe_allow_html=True) #[cite: 2]

        with st.container(border=True):
            st.markdown("### 2.3 Algoritmy bohatství")
            st.markdown("""
            <div class='box-blue'>
                <strong>Zaplať nejdřív sobě:</strong> Nečekej, co zbyde na konci měsíce. Část peněz si odlož na rezervu hned po přijetí příjmu.
            </div>
            """, unsafe_allow_html=True) #[cite: 2]
            
            st.markdown("### 2.4 Matematika peněz: Úrok a Inflace")
            st.markdown("""
            * **Jednoduché úročení:** Úrok se počítá stále jen z původně vložené nebo půjčené částky.
            * **Složené úročení:** Úročí se nejen původní částka, ale i již připsané úroky. Peníze vydělávají další peníze.
            * **Inflace:** Růst cenové hladiny. Za stejnou částku si koupíme méně než dříve.
            """) #[cite: 2]

        with st.container(border=True):
            st.markdown("### 2.5 Finanční rezerva: Airbag osobních financí")
            st.write("Finanční rezerva chrání člověka před tím, aby nečekaná situace (rozbitý telefon, výpadek brigády) skončila dluhem. **Obecné doporučení: 3 až 6 měsíců nutných výdajů.**") #[cite: 2]
            st.markdown("<div class='box-yellow'><strong>Kde rezervu držet:</strong> Rezerva má být bezpečná a dostupná. Není určena k riskantnímu investování.</div>", unsafe_allow_html=True) #[cite: 2]

        with st.container(border=True):
            st.markdown("### 2.6 Psychologie utrácení")
            st.write("Lidé nejsou kalkulačky. Často se rozhodujeme podle emocí, únavy, tlaku okolí, reklamy, strachu, že něco propásneme, nebo podle toho, co nám ukáže aplikace.") #[cite: 2]
            st.markdown("""
            * **FOMO (Fear Of Missing Out):** Strach, že mi něco uteče. -> *Obrana: Počkej 24 hodin před nákupem.*
            * **Sleva:** Pocit úspory, i když kupuji zbytečnost. -> *Obrana: Koupil/a bych to i bez slevy?*
            * **Odložená platba (BNPL):** Nákup nebolí hned. -> *Obrana: Ber ji jako dluh, ne jako slevu.*
            """) #[cite: 2]

            st.markdown("#### ⏳ Kalkulačka času: Kolik života stojí nákup")
            st.write("Cena věci není jen částka v korunách. Dá se přepočítat i na čas, který musí člověk pracovat, aby si ji mohl dovolit.") #[cite: 2]
            
            c_time1, c_time2, c_time3 = st.columns(3)
            with c_time1:
                item_price = st.number_input("Cena věci (Kč):", value=2400, step=100, key="calc_item_price")
            with c_time2:
                hourly_wage = st.number_input("Tvoje čistá hodinová mzda (Kč):", value=150, step=10, key="calc_hourly_wage")
            with c_time3:
                if hourly_wage > 0:
                    hours_needed = item_price / hourly_wage
                    st.info(f"**Musíš pracovat:**\n### {hours_needed:.1f} hodin")

    # --- PODKAPITOLA 2.3 ---
    elif selected_section_2 == "2.3 Finanční trh a analýza rizik":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.3</div>", unsafe_allow_html=True)
        st.markdown("## 3. Finanční trh a analýza rizik")
        
        with st.container(border=True):
            st.write("Finanční trh přesouvá peníze v čase. Někdo peníze dnes nepotřebuje a chce je zhodnotit. Někdo jiný peníze potřebuje dnes a je ochoten za jejich použití zaplatit úrok nebo podíl na zisku.") #[cite: 2]
            
            st.markdown("### 3.2 Investiční trojúhelník")
            st.markdown("""
            <div class='box-purple'>
                <strong>1. Výnos:</strong> To, co získáš navíc (úrok, dividenda, nárůst ceny).<br>
                <strong>2. Riziko:</strong> Možnost, že výsledek bude jiný (ztráta, kolísání).<br>
                <strong>3. Likvidita:</strong> Jak snadno lze aktivum proměnit zpět na peníze.
            </div>
            """, unsafe_allow_html=True) #[cite: 2]
            st.warning("Pravidlo: Vyšší možný výnos obvykle znamená vyšší riziko. Vysoký výnos, nulové riziko a okamžitá dostupnost peněz najednou jsou podezřelá kombinace.") #[cite: 2]

        with st.container(border=True):
            st.markdown("### 3.3 Spoření vs. Investování vs. Spekulace")
            st.markdown("""
            | Pojem | Co to je? | Typický příklad | Riziko |
            | :--- | :--- | :--- | :--- |
            | **Spoření** | Odkládání peněz s důrazem na bezpečnost a dostupnost. | Spořicí účet, termínovaný vklad. | Nízké, hrozí inflace. |
            | **Investování** | Vkládání peněz do aktiv s cílem dlouhodobého zhodnocení. | Akcie, dluhopisy, ETF. | Střední až vysoké. |
            | **Spekulace** | Sázka na krátkodobý pohyb ceny. | Krátkodobé obchody, krypto. | Vysoké. |
            """) #[cite: 2]

        with st.container(border=True):
            st.markdown("### 3.4 Základní cenné papíry")
            st.write("Dnes už má cenný papír většinou elektronickou zaknihovanou podobu, nejde o fyzický papír.") #[cite: 2]
            
            st.markdown("""
            * **Akcie:** Představuje podíl na akciové společnosti. Koupí akcie firmě nepůjčuješ, kupuješ si kousek jejího vlastnictví.
            * **Dluhopis:** Cenný papír, kterým si emitent (stát, firma) půjčuje peníze. Kupuješ dluh, jsi věřitel a očekáváš úrok.
            * **Podílové listy / ETF:** Podíl na majetku fondu. Místo jedné akcie kupuješ „košík“ plný různých aktiv, čímž rozkládáš riziko.
            """) #[cite: 2]

        with st.container(border=True):
            st.markdown("### 3.6 Kryptoměny a Blockchain")
            st.write("Kryptoměny jsou digitální aktiva v počítačové síti. Záznamy nejsou vedeny centrální bankou, ale technologií blockchain (sdílenou evidencí).") #[cite: 2]
            
            st.markdown("""
            <div class='box-gray'>
                <strong>Příklady:</strong><br>
                • <strong>Bitcoin:</strong> První a nejznámější kryptoměna, digitální vzácné aktivum.<br>
                • <strong>Ethereum:</strong> Síť umožňující chytré kontrakty a decentralizované aplikace.<br>
                • <strong>Stablecoiny:</strong> Tokeny navázané např. na dolar.
            </div>
            """, unsafe_allow_html=True) #[cite: 2]
            
            st.markdown("<div class='box-red'><strong>Největší rizika kryptoměn:</strong> Vysoká volatilita (prudké kolísání ceny), ztráta přístupu (seed phrase), podvody s falešnými tokeny, technická nevratnost a tlak influencerů (FOMO).</div>", unsafe_allow_html=True) #[cite: 2]

    # --- PODKAPITOLA 2.4 ---
    elif selected_section_2 == "2.4 Úvěry, pojištění a ochrana majetku":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.4</div>", unsafe_allow_html=True)
        st.markdown("## 4. Úvěry, pojištění a ochrana majetku")
        
        with st.container(border=True):
            st.write("Úvěr není „peníze zdarma“. Je to závazek, který přesouvá spotřebu nebo investici z budoucnosti do současnosti.") #[cite: 2]
            
            st.markdown("### 4.2 Úrok a 4.3 RPSN")
            st.markdown("""
            * **Úrok:** Cena za půjčení peněz. Banky s ním často dělají reklamu.
            * **RPSN (Roční procentní sazba nákladů):** Skutečnější cena úvěru. Ukazuje celkovou cenu úvěru za rok vč. poplatků a pojištění. Při porovnávání úvěrů sleduj vždy RPSN!
            """) #[cite: 2]

            st.markdown("### Druhy úvěrů")
            st.markdown("""
            | Typ | Charakteristika | Riziko |
            | :--- | :--- | :--- |
            | **Hypotéka** | Úvěr na bydlení zajištěný nemovitostí. Banka nepůjčí 100 % ceny (sleduje ukazatel LTV). | Dlouhá doba splácení, změna sazeb. |
            | **Spotřebitelský úvěr** | Často není zajištěný hodnotným majetkem. | Vyšší riziko nesplácení a drahé úroky. |
            | **Kreditní karta** | Opakovaně dostupný úvěrový limit s bezúročným obdobím. | Vysoký úrok při nesplacení včas. |
            | **BNPL** | Kup teď, zaplať později (odložená platba). | Psychologicky maskuje dluh jako pohodlnou platbu. |
            """) #[cite: 2]

            with st.expander("🤔 4.4 Ne každý úvěr dostane"):
                st.write("Banka musí posoudit, zda dlužník pravděpodobně zvládne splácet. Posuzuje: Věk, příjem, výdaje (děti, nájem), registry dlužníků a u hypotéky zajištění. Zamítnutý úvěr může být signál, že by splácení bylo příliš rizikové.") #[cite: 2]

        with st.container(border=True):
            st.markdown("### 4.10 Pojištění: Ochrana před finančním nárazem")
            st.write("Pojištění nezabrání tomu, aby se něco stalo, ale může snížit finanční škodu. Zřizuje se pro případ, kdy by škoda byla finančně těžko zvládnutelná.") #[cite: 2]
            
            st.markdown("""
            <div class='box-green'>
                <strong>Životní pojištění:</strong> Chrání před vážným dopadem na příjem domácnosti (smrt, invalidita, vážné onemocnění).<br>
                <strong>Neživotní pojištění:</strong><br>
                • <em>Pojištění nemovitosti:</em> Chrání stavbu (zdi, střechu).<br>
                • <em>Pojištění domácnosti:</em> Chrání vybavení (nábytek, elektroniku).<br>
                • <em>Pojištění odpovědnosti:</em> Chrání před škodou, kterou způsobíme někomu jinému (vytopení souseda).
            </div>
            """, unsafe_allow_html=True) #[cite: 2]
            st.error("Pozor na PODPOJIŠTĚNÍ! Pokud je majetek pojištěn na nižší částku, než je jeho skutečná hodnota, pojišťovna může krátit plnění.") #[cite: 2]

    # --- PODKAPITOLA 2.5 ---
    elif selected_section_2 == "2.5 Finanční řízení podniku":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.5</div>", unsafe_allow_html=True)
        st.markdown("## 5. Finanční řízení v podniku — most k podnikavosti")
        
        with st.container(border=True):
            st.write("Firma může mít skvělý produkt, hezký web a plný kalendář zakázek — a přesto může mít finanční problém. Popularita není totéž co zisk a zisk není totéž co peníze na účtu.") #[cite: 2]

            st.markdown("### 5.2 Základní finanční výkazy")
            st.markdown("""
            * **Rozvaha:** Fotografie firmy k určitému dni. Ukazuje, co firma vlastní (**Aktiva**) a z čeho je to financované (**Pasiva**).
            * **Výkaz zisku a ztráty:** Film za určité období. Výnosy minus Náklady. Ukazuje, zda firma generuje zisk.
            * **Cashflow (Peněžní toky):** Skutečný tok peněz. Firma může být zisková, ale zkrachovat, pokud zákazníci platí pozdě a firmě chybí hotovost na placení mezd.
            """) #[cite: 2]

        with st.container(border=True):
            st.markdown("### 5.3 Bod zvratu (Break-even point)")
            st.write("Ukazuje, kolik musí firma prodat, aby pokryla všechny náklady. Teprve prodeje nad bodem zvratu vytvářejí zisk.") #[cite: 2]
            
            st.markdown("""
            * **Fixní náklady (FN):** Nemění se podle počtu prodaných kusů (nájem, paušální služby).
            * **Variabilní náklady (VN):** Rostou s každým vyrobeným/prodaným kusem (materiál, doprava).
            """) #[cite: 2]
            st.info("**Vzorec:** Bod zvratu v kusech = Fixní náklady ÷ (Cena za kus − Variabilní náklad na kus)") #[cite: 2]

        with st.container(border=True):
            st.markdown("### 5.5 Finanční analýza: kontrola finančního zdraví")
            st.write("Pomáhá zjistit, zda je firma zisková, zadlužená, platebně schopná, efektivní a stabilní.") #[cite: 2]
            
            st.markdown("""
            | Co zkoumá | Ukazatel a Vzorec | Příklad významu |
            | :--- | :--- | :--- |
            | **Rentabilita** | **ROS** (Zisk ÷ Tržby × 100) | Kolik % z tržeb zůstává jako zisk. |
            | **Likvidita** | **Běžná likvidita** (Oběžná aktiva ÷ Krátkodobé závazky) | Zda má firma dost prostředků na faktury a splátky. |
            | **Zadluženost** | **Celková zadluženost** (Cizí zdroje ÷ Aktiva × 100) | Jaká část majetku je financována dluhem. |
            | **Aktivita** | **Doba inkasa pohledávek** (Pohledávky ÷ Tržby × 365) | Za kolik dní firma průměrně dostává zaplaceno od zákazníků. |
            """) #[cite: 2]

            with st.expander("🔎 5.6 Case Study: E-shop DropZone (Modelová analýza)"):
                st.write("E-shop meziročně zvýšil tržby z 800k na 1,2 mil. Kč. Zisk se mu zvedl z 60k na 120k.") #[cite: 2]
                st.markdown("<div class='box-red'>Na první pohled super. Z finanční analýzy ale zjistíme, že mu klesla okamžitá likvidita (z 0,32 na 0,15) a prodloužila se doba inkasa pohledávek (na 32 dní). Firma sice vydělává, ale může mít problém platit včas!</div>", unsafe_allow_html=True) #[cite: 2]

    # --- PODKAPITOLA 2.6 ---
    elif selected_section_2 == "2.6 Závěrečné aktivity a Slovník":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.6</div>", unsafe_allow_html=True)
        st.markdown("## 6. Interaktivní vrstva a Slovník")
        
        with st.container(border=True):
            st.markdown("### 📚 Slovník cizích pojmů")
            st.markdown("""
            <div class='box-gray' style='font-size: 0.85rem;'>
            <strong>Aktiva:</strong> Majetek firmy nebo člověka; např. peníze, zásoby, stroje.<br>
            <strong>Pasiva:</strong> Zdroje financování majetku firmy (vlastní kapitál, dluhy).<br>
            <strong>Akcie:</strong> Cenný papír představující podíl na akciové společnosti.<br>
            <strong>Dluhopis:</strong> Cenný papír, kterým si emitent půjčuje peníze a slibuje jejich splacení s úrokem.<br>
            <strong>Blockchain:</strong> Sdílený digitální záznam transakcí, rozdělený do bloků.<br>
            <strong>Bonita:</strong> Schopnost klienta splácet úvěr, kterou banka posuzuje.<br>
            <strong>Cashflow:</strong> Tok peněz. Ukazuje, kolik peněz skutečně přišlo a odešlo.<br>
            <strong>Diverzifikace:</strong> Rozložení peněz do více investic.<br>
            <strong>Emitent:</strong> Ten, kdo vydává cenný papír (stát, firma).<br>
            <strong>RPSN:</strong> Roční procentní sazba nákladů úvěru.
            </div>
            """, unsafe_allow_html=True) #[cite: 2]

        with st.container(border=True):
            st.markdown("### 🎯 Závěrečný Kvíz: Zvládl/a jsi finance v běžném životě?")
            
            with st.expander("❓ 1. Jaký je zásadní rozdíl v ručení za dluhy mezi OSVČ a společníkem v s.r.o.?"):
                st.write("**Odpověď:** OSVČ ručí celým osobním majetkem, společník s.r.o. ručí omezeně. Firma s.r.o. funguje jako oddělená právnická osoba.") #[cite: 2]

            with st.expander("❓ 2. Co přesně znamená zkratka MVP v metodice Lean Startup?"):
                st.write("**Odpověď:** Minimum Viable Product. Je to nejmenší a nejjednodušší verze produktu, která umožní levně ověřit zájem zákazníků.") #[cite: 2]

            with st.expander("❓ 3. Proč by měla firma sledovat Cashflow, i když je v zisku?"):
                st.write("**Odpověď:** Zisk je jen účetní rozdíl. Zákazníci mohou platit pozdě. Pokud firma nemá reálnou hotovost (cashflow) na zaplacení účtů, může zkrachovat.") #[cite: 2]

            with st.expander("❓ 4. Který z těchto nástrojů se nejvíce hodí na uchování finanční rezervy? a) Akcie b) Spořicí účet c) Krypto"):
                st.write("**Odpověď: b) Spořicí účet.** Rezerva musí být bezpečně a rychle dostupná (likvidní). Akcie a krypto jsou příliš rizikové (kolísají).") #[cite: 2]

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
