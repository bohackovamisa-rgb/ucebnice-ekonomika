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
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 1</div>", unsafe_allow_html=True)
        st.markdown("## 1. Podnikatel a základní pojmy <span style='display:none'>[cite: 1]</span>", unsafe_allow_html=True)
        
        with st.container(border=True):
            st.write("Zákon chápe podnikání jako soustavnou činnost prováděnou samostatně, vlastním jménem, na vlastní odpovědnost, za účelem dosažení zisku. <span style='display:none'>[cite: 1]</span>", unsafe_allow_html=True)
            
            st.markdown("""
            <div class='box-gray'>
                <strong>⚖️ Přesná zákonná opora:</strong> Podnikatele definuje zákon č. 89/2012 Sb., občanský zákoník, zejména § 420 odst. 1: <br>„Kdo samostatně vykonává na vlastní účet a odpovědnost výdělečnou činnost živnostenským nebo obdobným způsobem se záměrem činit tak soustavně za účelem dosažení zisku, je považován se zřetelem k této činnosti za podnikatele.“ <span style='display:none'>[cite: 1]</span><br><br>
                Jednoduše řečeno: Podnikatelem je ten, kdo podniká samostatně, na vlastní účet, na vlastní odpovědnost, dělá výdělečnou činnost soustavně a jejím cílem je zisk. <span style='display:none'>[cite: 1]</span>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class='box-blue'>
                <strong>📘 Proč je to důležité:</strong> Možná už máš nápad, něco prodáváš, tvoříš na zakázku nebo si jen přivyděláváš. Tady zjistíš, kdy už se z takové aktivity stává podnikání a proč je důležité poznat rozdíl mezi koníčkem, brigádou, OSVČ a firmou. <span style='display:none'>[cite: 1]</span>
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 1.1 Podnikatel v realitě současné generace <span style='display:none'>[cite: 1]</span>", unsafe_allow_html=True)
            st.write("Podnikání dnes nemusí začínat kanceláří, provozovnou ani výrobní halou. Může začít mobilem, profilem na sociální síti, prodejem digitální šablony, správou obsahu pro lokální firmu, výrobou merch produktů, doučováním, e-shopem, aplikací, kurzem, grafickou službou, tvorbou videí nebo komunitním projektem. <span style='display:none'>[cite: 1]</span>", unsafe_allow_html=True)
            st.write("Právě proto je důležité umět rozpoznat hranici mezi: <span style='display:none'>[cite: 1]</span>", unsafe_allow_html=True)
            
            st.markdown("""
            * **koníčkem** — dělám něco pro radost, bez soustavného záměru vydělávat, <span style='display:none'>[cite: 1]</span>
            * **jednorázovým přivýdělkem** — například prodám vlastní staré věci, <span style='display:none'>[cite: 1]</span>
            * **brigádou nebo zaměstnáním** — pracuji podle pokynů zaměstnavatele, <span style='display:none'>[cite: 1]</span>
            * **podnikáním** — samostatně nabízím produkt nebo službu, nesu riziko a chci dlouhodobě vydělávat. <span style='display:none'>[cite: 1]</span>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class='box-blue'>
                <strong>📱 Příklad pro dnešní studenty:</strong> Když jednou prodáš staré tenisky, nejde obvykle o podnikání. Když ale pravidelně nakupuješ, upravuješ, propaguješ a prodáváš zboží se záměrem vydělat, už se blížíš podnikání a musíš řešit pravidla. <span style='display:none'>[cite: 1]</span>
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 1.2 Čtyři znaky podnikání na praktických příkladech <span style='display:none'>[cite: 1]</span>", unsafe_allow_html=True)
            st.markdown("""
            | Znak podnikání | Co znamená | Příklad ze současnosti | Otázka pro žáka |
            | :--- | :--- | :--- | :--- |
            | **Soustavnost** | Činnost se opakuje nebo je plánovaná dlouhodobě. <span style='display:none'>[cite: 1]</span> | Každý měsíc prodávám vlastní digitální plánovače. <span style='display:none'>[cite: 1]</span> | Dělám to jednou, nebo z toho chci pravidelný příjem? <span style='display:none'>[cite: 1]</span> |
            | **Samostatnost** | Sám/sama rozhoduji o ceně, zákaznících, způsobu práce a organizaci. <span style='display:none'>[cite: 1]</span> | Nabízím správu sociálních sítí lokálním podnikům. <span style='display:none'>[cite: 1]</span> | Kdo určuje, jak, kdy a pro koho pracuji? <span style='display:none'>[cite: 1]</span> |
            | **Vlastní jméno** | Vystupuji vůči zákazníkům a úřadům jako podnikatel nebo firma. <span style='display:none'>[cite: 1]</span> | Mám značku, profil, faktury, obchodní podmínky nebo IČO. <span style='display:none'>[cite: 1]</span> | Kdo nese odpovědnost před zákazníkem? <span style='display:none'>[cite: 1]</span> |
            | **Vlastní odpovědnost**| Nesu riziko ztráty, reklamací, dluhů a špatných rozhodnutí. <span style='display:none'>[cite: 1]</span> | Nakoupím materiál na merch, ale nikdo si ho nekoupí. <span style='display:none'>[cite: 1]</span> | Co se stane, když plán nevyjde? <span style='display:none'>[cite: 1]</span> |
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 1.3 Podnikatel není jen „někdo, kdo vydělává“ <span style='display:none'>[cite: 1]</span>", unsafe_allow_html=True)
            st.write("Podnikatel vytváří hodnotu pro zákazníka. Peníze jsou důsledkem toho, že někdo považuje produkt nebo službu za užitečnou. Moderní podnikavost proto zahrnuje nejen prodej, ale i schopnost: <span style='display:none'>[cite: 1]</span>", unsafe_allow_html=True)
            st.markdown("""
            * vidět problém, <span style='display:none'>[cite: 1]</span>
            * navrhnout řešení, <span style='display:none'>[cite: 1]</span>
            * ověřit zájem, <span style='display:none'>[cite: 1]</span>
            * komunikovat férově, <span style='display:none'>[cite: 1]</span>
            * počítat náklady a cenu, <span style='display:none'>[cite: 1]</span>
            * nést odpovědnost, <span style='display:none'>[cite: 1]</span>
            * učit se z chyb, <span style='display:none'>[cite: 1]</span>
            * používat technologie bezpečně a smysluplně. <span style='display:none'>[cite: 1]</span>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("<div class='box-yellow'><strong>🧪 Tvůj úkol: Je to podnikání?</strong><br>U každé situace rozhodni, zda jde spíš o koníček, jednorázový přivýdělek, zaměstnání, nebo podnikání. Zdůvodni odpověď podle čtyř znaků podnikání. <span style='display:none'>[cite: 1]</span></div>", unsafe_allow_html=True)
            st.selectbox("1. Student jednou prodá starý mobil. <span style='display:none'>[cite: 1]</span>", ["Vyber odpověď...", "Koníček", "Jednorázový přivýdělek", "Zaměstnání", "Podnikání"], key="p1_q1")
            st.selectbox("2. Student každý týden prodává vlastnoručně vyráběné náramky přes Instagram. <span style='display:none'>[cite: 1]</span>", ["Vyber odpověď...", "Koníček", "Jednorázový přivýdělek", "Zaměstnání", "Podnikání"], key="p1_q2")
            st.selectbox("3. Student pracuje v kavárně podle rozpisu směn. <span style='display:none'>[cite: 1]</span>", ["Vyber odpověď...", "Koníček", "Jednorázový přivýdělek", "Zaměstnání", "Podnikání"], key="p1_q3")
            st.selectbox("4. Student nabízí grafiku loga pro malé podniky a sám si domlouvá cenu. <span style='display:none'>[cite: 1]</span>", ["Vyber odpověď...", "Koníček", "Jednorázový přivýdělek", "Zaměstnání", "Podnikání"], key="p1_q4")
            st.selectbox("5. Student vytvoří placený online kurz pro mladší žáky. <span style='display:none'>[cite: 1]</span>", ["Vyber odpověď...", "Koníček", "Jednorázový přivýdělek", "Zaměstnání", "Podnikání"], key="p1_q5")

            st.markdown("""
            <div class='box-purple'>
                <strong>🤖 AI mentoring:</strong> „Zeptej se mě na můj nápad a podle čtyř znaků podnikání mi vysvětli, jestli už jde o podnikání. U každého znaku mi dej jednu kontrolní otázku.“ <span style='display:none'>[cite: 1]</span>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<div class='box-yellow'><strong>🧩 Interaktivní výzva:</strong> Popiš svůj nápad jednou větou a označ, jak v něm bude vidět soustavnost, samostatnost a odpovědnost. <span style='display:none'>[cite: 1]</span></div>", unsafe_allow_html=True)
            st.text_area("Tvoje odpověď:", key="p1_idea")

            st.markdown("""
            <div class='box-purple'>
                <strong>🤖 AI mentoring:</strong> Zkopíruj tento prompt do AI asistenta: „Pomoz mi rozlišit, jestli je můj nápad spíš jednorázová aktivita, nebo skutečné podnikání.“ <span style='display:none'>[cite: 1]</span>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class='box-blue'>
                <strong>📌 Základní definice:</strong> Podnikání není jednorázová aktivita. Je to dlouhodobá, samostatná a odpovědná činnost, při které podnikatel vystupuje vlastním jménem a usiluje o zisk. <span style='display:none'>[cite: 1]</span>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class='box-blue'>
                <strong>📌 Čtyři pilíře podnikání:</strong> <span style='display:none'>[cite: 1]</span><br>
                • <strong>Soustavnost:</strong> nejde o jednorázový prodej, ale o činnost vykonávanou opakovaně nebo dlouhodobě. <span style='display:none'>[cite: 1]</span><br>
                • <strong>Samostatnost:</strong> podnikatel rozhoduje o tom, co dělá, jak pracuje a jak organizuje svou činnost. <span style='display:none'>[cite: 1]</span><br>
                • <strong>Vlastní jméno:</strong> podnikatel vystupuje vůči zákazníkům, úřadům a partnerům sám za sebe nebo za svou firmu. <span style='display:none'>[cite: 1]</span><br>
                • <strong>Vlastní odpovědnost:</strong> podnikatel nese následky svých rozhodnutí, včetně rizik, závazků a případných dluhů. <span style='display:none'>[cite: 1]</span>
            </div>
            """, unsafe_allow_html=True)

            st.info("🤔 **Otázka k zamyšlení:** V čem je podle vás největší rozdíl mezi zaměstnancem a podnikatelem? <span style='display:none'>[cite: 1]</span>")

    # --- 2. Slovníček základních pojmů ---
    elif selected_section == "2. Slovníček základních pojmů":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2</div><h2>2. Slovníček základních pojmů</h2> <span style='display:none'>[cite: 1]</span>", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("""
            | Termín | Co znamená | Proč je důležitý |
            | :--- | :--- | :--- |
            | **Podnikatel** | Osoba, která samostatně vykonává výdělečnou činnost na vlastní účet a odpovědnost se záměrem dělat ji soustavně za účelem dosažení zisku. <span style='display:none'>[cite: 1]</span> | Pomáhá rozlišit, kdy už nejde jen o koníček nebo jednorázový přivýdělek. <span style='display:none'>[cite: 1]</span> |
            | **Podnikání** | Soustavná samostatná činnost vykonávaná na vlastní odpovědnost za účelem dosažení zisku. <span style='display:none'>[cite: 1]</span> | Je základním pojmem celé kapitoly a určuje, kdy vznikají právní a finanční povinnosti. <span style='display:none'>[cite: 1]</span> |
            | **Fyzická osoba** | Člověk — jednotlivec. V podnikání může vystupovat například jako OSVČ. <span style='display:none'>[cite: 1]</span> | Máš poznat rozdíl mezi člověkem podnikatelem a firmou jako právnickou osobou. <span style='display:none'>[cite: 1]</span> |
            | **Právnická osoba** | Organizovaný subjekt, který má právní osobnost. Typicky jde například o s.r.o., a.s., družstvo, spolek nebo nadaci. <span style='display:none'>[cite: 1]</span> | Vysvětluje, proč firma může jednat, vlastnit majetek a nést odpovědnost samostatně. <span style='display:none'>[cite: 1]</span> |
            | **OSVČ** | Osoba samostatně výdělečně činná — fyzická osoba, která podniká vlastním jménem a na vlastní odpovědnost. <span style='display:none'>[cite: 1]</span> | Je častou formou začátku malého podnikání, freelancingu nebo služeb. <span style='display:none'>[cite: 1]</span> |
            | **Živnost** | Podnikatelská činnost provozovaná podle živnostenského zákona, pokud splňuje zákonné podmínky. <span style='display:none'>[cite: 1]</span> | Pomáhá určit, jestli podnikatel potřebuje živnostenské oprávnění a jaký typ živnosti řeší. <span style='display:none'>[cite: 1]</span> |
            | **Živnostenské oprávnění**| Právo provozovat živnost. U ohlašovacích živností vzniká ohlášením, u koncesovaných udělením koncese. <span style='display:none'>[cite: 1]</span> | Bez něj nelze legálně provozovat činnost, která ho vyžaduje. <span style='display:none'>[cite: 1]</span> |
            | **Obchodní korporace** | Souhrnný pojem pro obchodní společnosti a družstva, například v.o.s., k.s., s.r.o., a.s. a družstvo. <span style='display:none'>[cite: 1]</span> | Pomáhá zařadit základní právní formy podnikání. <span style='display:none'>[cite: 1]</span> |
            | **Obchodní rejstřík** | Veřejný seznam, ve kterém se zapisují obchodní korporace a další zákonem stanovené subjekty. <span style='display:none'>[cite: 1]</span> | Slouží k ověření firmy, její právní formy, sídla a osob, které za ni jednají. <span style='display:none'>[cite: 1]</span> |
            | **Švarcsystém** | Nelegální nastavení, kdy člověk formálně vystupuje jako podnikatel, ale fakticky pracuje jako zaměstnanec. <span style='display:none'>[cite: 1]</span> | Pomáhá rozpoznat rizikovou spolupráci a rozdíl mezi podnikáním a zaměstnáním. <span style='display:none'>[cite: 1]</span> |
            | **Lean Canvas** | Stručná mapa podnikatelského nápadu, která zachycuje problém, zákazníka, řešení, náklady, příjmy a rizika. <span style='display:none'>[cite: 1]</span> | Pomáhá rychle ověřovat nápad dřív, než tým investuje hodně času nebo peněz. <span style='display:none'>[cite: 1]</span> |
            | **MVP** | Minimální životaschopný produkt — nejmenší verze řešení, která umožní ověřit důležitý předpoklad. <span style='display:none'>[cite: 1]</span> | Učí testovat nápad levně, rychle a bezpečně. <span style='display:none'>[cite: 1]</span> |
            """, unsafe_allow_html=True)
            st.markdown("<div class='box-gray'><strong>📚 Opora v legislativě:</strong> občanský zákoník, živnostenský zákon, zákon o obchodních korporacích a zákon o veřejných rejstřících. <span style='display:none'>[cite: 1]</span></div>", unsafe_allow_html=True)

    # --- 3. OSVČ a živnosti ---
    elif selected_section == "3. OSVČ a živnosti":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 3</div><h2>3. OSVČ a živnosti</h2>", unsafe_allow_html=True)
        
        with st.container(border=True):
            st.write("OSVČ znamená osoba samostatně výdělečně činná. Jde o podnikání fyzické osoby — tedy člověka, který podniká vlastním jménem a nese za své podnikání odpovědnost. <span style='display:none'>[cite: 1]</span>", unsafe_allow_html=True)
            
            st.markdown("### 3.1 OSVČ jako nejčastější start malé podnikavosti <span style='display:none'>[cite: 1]</span>", unsafe_allow_html=True)
            st.write("OSVČ je pro mnoho lidí nejjednodušší cesta, jak začít. Hodí se pro malé služby, freelancing, řemeslo, doučování, správu sociálních sítí, grafiku, fotografování, tvorbu webů, e-shop v menším rozsahu nebo lokální podnikání. <span style='display:none'>[cite: 1]</span>", unsafe_allow_html=True)
            st.markdown("""
            | Situace | Proč může OSVČ dávat smysl | Na co si dát pozor |
            | :--- | :--- | :--- |
            | **Student spravuje sociální sítě lokální kavárně.** <span style='display:none'>[cite: 1]</span> | Nízké vstupní náklady, služba založená na dovednosti. <span style='display:none'>[cite: 1]</span> | Smlouva, fakturace, daně, autorská práva k obsahu. <span style='display:none'>[cite: 1]</span> |
            | **Grafik tvoří loga a šablony.** <span style='display:none'>[cite: 1]</span> | Lze začít s notebookem a portfoliem. <span style='display:none'>[cite: 1]</span> | Licenční podmínky, termíny, reklamace, komunikace s klientem. <span style='display:none'>[cite: 1]</span> |
            | **Kadeřník nebo kosmetička pracuje samostatně.** <span style='display:none'>[cite: 1]</span> | Vlastní zákazníci, možnost budovat značku. <span style='display:none'>[cite: 1]</span> | Odborná způsobilost, hygiena, provozovna, odpovědnost. <span style='display:none'>[cite: 1]</span> |
            | **Malý e-shop prodává vlastní produkty.** <span style='display:none'>[cite: 1]</span> | Jednoduchý start a přímý kontakt se zákazníkem. <span style='display:none'>[cite: 1]</span> | Obchodní podmínky, reklamace, sklad, ochrana spotřebitele. <span style='display:none'>[cite: 1]</span> |
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 3.2 OSVČ a digitální realita <span style='display:none'>[cite: 1]</span>", unsafe_allow_html=True)
            st.write("Dnešní OSVČ často nepotřebuje jen živnostenské oprávnění. Potřebuje také digitální a finanční gramotnost: oddělit osobní a podnikatelské peníze, evidovat příjmy a výdaje, zálohovat doklady, chránit osobní údaje zákazníků, nepoužívat cizí fotografie a hudbu bez práv, a počítat s daněmi a odvody dřív, než peníze utratí. <span style='display:none'>[cite: 1]</span>", unsafe_allow_html=True)
            st.markdown("<div class='box-yellow'><strong>💡 Pravidlo pro začátečníka:</strong> To, co přijde na účet, není celé „moje výplata“. Část peněz patří na náklady, daně, sociální a zdravotní pojištění, rezervu a budoucí investice. <span style='display:none'>[cite: 1]</span></div>", unsafe_allow_html=True)

            st.markdown("#### 🧮 Mini simulace OSVČ <span style='display:none'>[cite: 1]</span>", unsafe_allow_html=True)
            st.write("Představ si, že OSVČ za měsíc vyfakturuje **28 000 Kč**. Náklady na software, dopravu, materiál a reklamu jsou **6 000 Kč**. <span style='display:none'>[cite: 1]</span>", unsafe_allow_html=True)
            profit_calc = 28000 - 6000
            st.markdown(f"**Orientační zisk před daněmi a odvody:** **{profit_calc:,} Kč**")
            reserve_pct = st.slider("Kolik % by si měla OSVČ odložit stranou?", 10, 50, 30, 5)
            st.info(f"Při {reserve_pct} % si odložíte: {28000 * (reserve_pct/100):,.0f} Kč.")
            st.markdown("<div class='box-red'><strong>⚠️ Hlavní riziko OSVČ:</strong> OSVČ ručí za závazky z podnikání celým svým osobním majetkem. Jednoduchý start tedy neznamená nulové riziko. <span style='display:none'>[cite: 1]</span></div>", unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 3.3 Podmínky pro podnikání a 3.4 Druhy živností <span style='display:none'>[cite: 1]</span>", unsafe_allow_html=True)
            st.write("Základní podmínky pro začínající OSVČ: dosažení věku 18 let, svéprávnost, bezúhonnost, případně odborná způsobilost podle druhu živnosti. <span style='display:none'>[cite: 1]</span>", unsafe_allow_html=True)
            st.markdown("""
            | Druh živnosti | Co znamená | Příklad |
            | :--- | :--- | :--- |
            | **Volná živnost** | Není potřeba speciální vzdělání ani praxe. Stačí splnit všeobecné podmínky. <span style='display:none'>[cite: 1]</span> | E-shop, marketingové služby, správa sociálních sítí. <span style='display:none'>[cite: 1]</span> |
            | **Řemeslná živnost** | Vyžaduje odbornou způsobilost, například výuční list nebo praxi. <span style='display:none'>[cite: 1]</span> | Truhlářství, kadeřnictví, opravy strojů. <span style='display:none'>[cite: 1]</span> |
            | **Vázaná živnost** | Vyžaduje specifické vzdělání, praxi nebo zkoušku. <span style='display:none'>[cite: 1]</span> | Účetní poradenství, průvodcovská činnost, masérské služby. <span style='display:none'>[cite: 1]</span> |
            | **Koncesovaná živnost**| Vyžaduje státní povolení — koncesi. Jde o regulovanější nebo rizikovější činnosti. <span style='display:none'>[cite: 1]</span> | Taxislužba, provozování střelnice, prodej zbraní. <span style='display:none'>[cite: 1]</span> |
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 3.6 Povinnosti živnostníka a 3.7 Daně a odvody <span style='display:none'>[cite: 1]</span>", unsafe_allow_html=True)
            st.write("OSVČ neřeší jen zákazníky a cenu. Musí také ohlásit živnost, platit daň z příjmů fyzických osob (základní sazba 15 %), sociální pojištění a zdravotní pojištění. <span style='display:none'>[cite: 1]</span>", unsafe_allow_html=True)
            st.write("Během roku se obvykle platí měsíční **zálohy** a po skončení roku se podává daňové přiznání a přehledy pro pojišťovny. <span style='display:none'>[cite: 1]</span>", unsafe_allow_html=True)
            st.markdown("<div class='box-blue'><strong>Paušální daň:</strong> OSVČ může za splnění zákonných podmínek vstoupit do paušálního režimu. V jedné měsíční platbě pak řeší daň z příjmů, sociální pojištění i zdravotní pojištění. Paušální daň se často vyplatí tehdy, když má OSVČ vyšší příjmy, nižší skutečné výdaje a splní podmínky. <span style='display:none'>[cite: 1]</span></div>", unsafe_allow_html=True)
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
