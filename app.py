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

    p, li {
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

    /* KARTY LEAN CANVAS */
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
    .mindmap-wrapper {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 2rem 1rem;
        flex-wrap: wrap;
        gap: 2rem;
        background: #f1f5f9;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        margin-bottom: 1.5rem;
    }
    .mm-col {
        display: flex;
        flex-direction: column;
        gap: 1.5rem;
    }
    .mm-center {
        background: #ef4444;
        color: white;
        padding: 1.8rem 2.5rem;
        border-radius: 20px;
        font-weight: 800;
        font-size: 1.5rem;
        text-align: center;
        box-shadow: 0 10px 15px -3px rgba(239, 68, 68, 0.3);
        border: 3px solid #b91c1c;
        z-index: 2;
    }
    .mm-node {
        background: #ffffff;
        border: 2px solid #cbd5e1;
        padding: 1rem;
        border-radius: 16px;
        width: 260px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        position: relative;
        transition: all 0.2s ease;
    }
    .mm-node:hover {
        border-color: #6366f1;
        box-shadow: 0 10px 15px -3px rgba(99, 102, 241, 0.2);
        transform: translateY(-2px);
    }
    .mm-title {
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 0.5rem;
        text-align: center;
        border-bottom: 2px solid #e2e8f0;
        padding-bottom: 0.5rem;
        text-transform: uppercase;
        font-size: 0.85rem;
        letter-spacing: 0.05em;
    }
    .mm-node ul {
        margin: 0;
        padding-left: 1.2rem;
        font-size: 0.85rem;
        color: #475569;
    }
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

    # PODKAPITOLA 1
    if selected_section == "1. Podnikatel a základní pojmy":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 1</div>", unsafe_allow_html=True)
        st.markdown("## 1. Podnikatel a základní pojmy")
        
        with st.container(border=True):
            st.markdown("### Základní definice podnikání")
            st.markdown("""
            <div class='box-blue'>
                <strong>Hlavní definice:</strong><br>
                Zákon chápe podnikání jako soustavnou činnost prováděnou samostatně, vlastním jménem, na vlastní odpovědnost, za účelem dosažení zisku.
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class='box-gray'>
                <strong>Přesná zákonná opora:</strong> Podnikatele definuje zákon č. 89/2012 Sb., občanský zákoník, zejména § 420 odst. 1:<br>
                <i>„Kdo samostatně vykonává na vlastní účet a odpovědnost výdělečnou činnost živnostenským nebo obdobným způsobem se záměrem činit tak soustavně za účelem dosažení zisku, je považován se zřetelem k této činnosti za podnikatele.“</i><br><br>
                <strong>Jednoduše řečeno:</strong> Podnikatelem je ten, kdo podniká samostatně, na vlastní účet, na vlastní odpovědnost, dělá výdělečnou činnost soustavně a jejím cílem je zisk.
            </div>
            """, unsafe_allow_html=True)

            st.markdown("### Proč je to důležité")
            st.write("""
            Možná už máš nápad, něco prodáváš, tvoříš na zakázku nebo si jen přivyděláváš. Tady zjistíš, kdy už se z takové aktivity stává podnikání a proč je důležité poznat rozdíl mezi koníčkem, brigádou, OSVČ a firmou.
            """)

        with st.container(border=True):
            st.markdown("### 1.1 Podnikatel v realitě současné generace")
            st.write("""
            Podnikání dnes nemusí začínat kanceláří, provozovnou ani výrobní halou. Může začít mobilem, profilem na sociální síti, prodejem digitální šablony, správou obsahu pro lokální firmu, výrobou merch produktů, doučováním, e-shopem, aplikací, kurzem, grafickou službou, tvorbou videí nebo komunitním projektem.
            """)

            st.markdown("#### Hranice mezi koníčkem, přivýdělkem, zaměstnáním a podnikáním")
            st.write("""
            Právě proto je důležité umět rozpoznat hranici mezi:
            * **Koníčkem** — dělám něco pro radost, bez soustavného záměru vydělávat,
            * **Jednorázovým přivýdělkem** — například prodám vlastní staré věci,
            * **Brigádou nebo zaměstnáním** — pracuji podle pokynů zaměstnavatele,
            * **Podnikáním** — samostatně nabízím produkt nebo službu, nesu riziko a chci dlouhodobě vydělávat.
            """)

            st.markdown("""
            <div class='box-green'>
                <strong>Příklad pro dnešní studenty:</strong> Když jednou prodáš staré tenisky, nejde obvykle o podnikání. Když ale pravidelně nakupuješ, upravuješ, propaguješ a prodáváš zboží se záměrem vydělat, už se blížíš podnikání a musíš řešit pravidla.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 1.2 Čtyři znaky podnikání na praktických příkladech")
            st.markdown("""
            | Znak podnikání | Co znamená | Příklad ze současnosti | Otázka pro žáka |
            | :--- | :--- | :--- | :--- |
            | **Soustavnost** | Činnost se opakuje nebo je plánovaná dlouhodobě. | Každý měsíc prodávám vlastní digitální plánovače. | Dělám to jednou, nebo z toho chci pravidelný příjem? |
            | **Samostatnost** | Sám/sama rozhoduji o ceně, zákaznících, způsobu práce a organizaci. | Nabízím správu sociálních sítí lokálním podnikům. | Kdo určuje, jak, kdy a pro koho pracuji? |
            | **Vlastní jméno** | Vystupuji vůči zákazníkům a úřadům jako podnikatel nebo firma. | Mám značku, profil, faktury, obchodní podmínky nebo IČO. | Kdo nese odpovědnost před zákazníkem? |
            | **Vlastní odpovědnost** | Nesu riziko ztráty, reklamací, dluhů a špatných rozhodnutí. | Nakoupím materiál na merch, ale nikdo si ho nekoupí. | Co se stane, když plán nevyjde? |
            """)

        with st.container(border=True):
            st.markdown("### 1.3 Podnikatel není jen „někdo, kdo vydělává“")
            st.write("""
            Podnikatel vytváří hodnotu pro zákazníka. Peníze jsou důsledkem toho, že někdo považuje produkt nebo službu za užitečnou.
            
            Moderní podnikavost proto zahrnuje nejen prodej, ale i schopnost:
            * vidět problém,
            * navrhnout řešení,
            * ověřit zájem,
            * komunikovat férově,
            * počítat náklady a cenu,
            * nést odpovědnost,
            * učit se z chyb,
            * používat technologie bezpečně a smysluplně.
            """)

        # AKTIVITY A ÚKOLY K PODKAPITOLE 1
        with st.container(border=True):
            st.markdown("### Tvůj úkol: Je to podnikání?")
            st.write("U každé situace rozhodni, zda jde spíš o koníček, jednorázový přivýdelek, zaměstnání, nebo podnikání. Zdůvodni odpověď podle čtyř znaků podnikání.")

            ex1 = st.selectbox("1. Student jednou prodá starý mobil:", ["Vyber odpověď...", "Koníček", "Jednorázový přivýdelek", "Zaměstnání", "Podnikání"], key="p1_ex1")
            ex2 = st.selectbox("2. Student každý týden prodává vlastnoručně vyráběné náramky přes Instagram:", ["Vyber odpověď...", "Koníček", "Jednorázový přivýdelek", "Zaměstnání", "Podnikání"], key="p1_ex2")
            ex3 = st.selectbox("3. Student pracuje v kavárně podle rozpisu směn:", ["Vyber odpověď...", "Koníček", "Jednorázový přivýdelek", "Zaměstnání", "Podnikání"], key="p1_ex3")
            ex4 = st.selectbox("4. Student nabízí grafiku loga pro malé podniky a sám si domlouvá cenu:", ["Vyber odpověď...", "Koníček", "Jednorázový přivýdelek", "Zaměstnání", "Podnikání"], key="p1_ex4")
            ex5 = st.selectbox("5. Student vytvoří placený online kurz pro mladší žáky:", ["Vyber odpověď...", "Koníček", "Jednorázový přivýdelek", "Zaměstnání", "Podnikání"], key="p1_ex5")

            if st.button("Uložit vyhodnocení úkolu"):
                st.success("Odpovědi byly uloženy do vašeho profilu pokroků!")

        with st.container(border=True):
            st.markdown("### Interaktivní výzva: vlastní nápad")
            user_idea = st.text_area("Popiš svůj nápad jednou větou a označ, jak v něm bude vidět soustavnost, samostatnost a odpovědnost:", placeholder="Můj nápad je...", height=100, key="p1_user_idea")
            if st.button("Uložit můj nápad"):
                st.success("Nápad uložen!")

        # AI MENTORING
        with st.container(border=True):
            st.markdown("### AI mentoring k podnikání")
            st.write("Použij tyto prompty pro analýzu svého nápadu s pomocí AI asistenta:")

            st.markdown("""
            <div class='box-purple'>
                <strong>Prompt 1 — Analýza 4 znaků podnikání:</strong><br>
                Zeptej se mě na můj nápad a podle čtyř znaků podnikání mi vysvětli, jestli už jde o podnikání. U každého znaku mi dej jednu kontrolní otázku.
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class='box-purple'>
                <strong>Prompt 2 — Rozlišení aktivity:</strong><br>
                Pomoz mi rozlišit, jestli je můj nápad spíš jednorázová aktivita, nebo skutečné podnikání.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 📌 Shrnující přehled & Čtyři pilíře")
            st.markdown("""
            <div class='box-blue'>
                <strong>Základní definice:</strong> Podnikání není jednorázová aktivita. Je to dlouhodobá, samostatná a odpovědná činnost, při které podnikatel vystupuje vlastním jménem a usiluje o zisk.
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            * **Soustavnost:** nejde o jednorázový prodej, ale o činnost vykonávanou opakovaně nebo dlouhodobě.
            * **Samostatnost:** podnikatel rozhoduje o tom, co dělá, jak pracuje a jak organizuje svou činnost.
            * **Vlastní jméno:** podnikatel vystupuje vůči zákazníkům, úřadům a partnerům sám za sebe nebo za svou firmu.
            * **Vlastní odpovědnost:** podnikatel nese následky svých rozhodnutí, včetně rizik, závazků a případných dluhů.
            """)

            st.text_area("Otázka k zamyšlení: V čem je podle vás největší rozdíl mezi zaměstnancem a podnikatelem?", placeholder="Vaše odpověď...", height=80, key="p1_reflect")

    # PODKAPITOLA 2
    elif selected_section == "2. Slovníček základních pojmů":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2</div>", unsafe_allow_html=True)
        st.markdown("## 2. Slovníček základních pojmů")
        
        with st.container(border=True):
            st.markdown("""
            <div class='box-blue'>
                <strong>Proč jsou definice důležité:</strong> V podnikání nestačí používat pojmy „přibližně“. Výrazy jako podnikatel, fyzická osoba, právnická osoba nebo živnostenské oprávnění mají oporu v právních předpisech.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 📖 Přehledný slovníček pojmů")
            st.markdown("""
            | Termín | Co znamená | Proč je důležitý |
            | :--- | :--- | :--- |
            | **Podnikatel** | Osoba, která samostatně vykonává výdělečnou činnost na vlastní účet a odpovědnost se záměrem dělat ji soustavně za účelem dosažení zisku. | Pomáhá rozlišit, kdy už nejde jen o koníček nebo jednorázový přivýdelek. |
            | **Podnikání** | Soustavná samostatná činnost vykonávaná na vlastní odpovědnost za účelem dosažení zisku. | Je základním pojmem celé kapitoly a určuje, kdy vznikají právní a finanční povinnosti. |
            | **Fyzická osoba** | Člověk — jednotlivec. V podnikání může vystupovat například jako OSVČ. | Máš poznat rozdíl mezi člověkem podnikatelem a firmou jako právnickou osobou. |
            | **Právnická osoba** | Organizovaný subjekt, který má právní osobnost. Typicky jde například o s.r.o., a.s., družstvo, spolek nebo nadaci. | Vysvětluje, proč firma může jednat, vlastnit majetek a nést odpovědnost samostatně. |
            | **OSVČ** | Osoba samostatně výdělečně činná — fyzická osoba, která podniká vlastním jménem a na vlastní odpovědnost. | Je častou formou začátku malého podnikání, freelancingu nebo služeb. |
            | **Živnost** | Podnikatelská činnost provozovaná podle živnostenského zákona, pokud splňuje zákonné podmínky. | Pomáhá určuje, jestli podnikatel potřebuje živnostenské oprávnění a jaký typ živnosti řeší. |
            | **Živnostenské oprávnění** | Právo provozovat živnost. U ohlašovacích živností vzniká zpravidla ohlášením, u koncesovaných živností až udělením koncese. | Bez něj nelze legálně provozovat činnost, která živnostenské oprávnění vyžaduje. |
            | **Volná živnost** | Živnost, u které není potřeba speciální vzdělání ani praxe; stačí splnit všeobecné podmínky. | Patří sem mnoho běžných začátků podnikání, například marketingové služby nebo e-shop. |
            | **Řemeslná živnost** | Živnost, která vyžaduje odbornou způsobilost, například výuční list nebo praxi. | Ukazuje, že některé činnosti nelze začít dělat bez kvalifikace. |
            | **Vázaná živnost** | Živnost, která vyžaduje specifické vzdělání, praxi nebo jinou zákonem stanovenou způsobilost. | Pomáhá pochopit, že u některých služeb stát chrání zákazníka požadavkem na odbornost. |
            | **Koncesovaná živnost** | Živnost, kterou lze provozovat až po udělení státního povolení — koncesi. | Typicky jde o regulované nebo rizikovější činnosti. |
            | **Obchodní korporace** | Souhrnný pojem pro obchodní společnosti a družstva, například v.o.s., k.s., s.r.o., a.s. a družstvo. | Pomáhá zařadit základní právní formy podnikání. |
            | **Obchodní rejstřík** | Veřejný seznam, ve kterém se zapisují obchodní korporace a další zákonem stanovené subjekty. | Slouží k ověření firmy, její právní formy, sídla a osob, které za ni jednají. |
            | **Živnostenský rejstřík** | Evidence osob podnikajících na základě živnostenského oprávnění. | Slouží k ověření, zda má podnikatel oprávnění k určité činnosti. |
            | **Ručení** | Odpovědnost za dluhy a závazky podnikatele nebo firmy. | Je klíčové při volbě právní formy, protože OSVČ a některé společnosti nesou vyšší osobní riziko. |
            | **Švarcsystém** | Nelegální nastavení, kdy člověk formálně vystupuje jako podnikatel, ale fakticky pracuje jako zaměstnanec. | Pomáhá rozpoznat rizikovou spolupráci a rozdíl mezi podnikáním a zaměstnáním. |
            | **CSR** | Společenská odpovědnost firem — přístup, kdy firma sleduje nejen zisk, ale i dopady na lidi, společnost a životní prostředí. | Ukazuje, že podnikání má také etický a společenský rozměr. |
            | **Lean Canvas** | Stručná mapa podnikatelského nápadu, která zachycuje problém, zákazníka, řešení, náklady, příjmy a rizika. | Pomáhá rychle ověřovat nápad dřív, než tým investuje hodně času nebo peněz. |
            | **MVP** | Minimální životaschopný produkt — nejmenší verze řešení, která umožní ověřit důležitý předpoklad. | Učí testovat nápad levně, rychle a bezpečně. |
            """)

        with st.container(border=True):
            st.markdown("### Interaktivní výzva: Aplikace pojmů")
            st.write("Vyber tři pojmy ze slovníčku a napiš k nim vlastní příklad z reálného nebo vymyšleného podnikání.")
            
            c_p1, c_p2 = st.columns(2)
            with c_p1:
                term_1 = st.text_input("1. Vybraný pojem:", placeholder="Např. Volná živnost", key="p2_t1")
                ex_1 = st.text_area("Příklad z praxe k 1. pojmu:", placeholder="Příklad...", height=70, key="p2_e1")
            with c_p2:
                term_2 = st.text_input("2. Vybraný pojem:", placeholder="Např. Právnická osoba", key="p2_t2")
                ex_2 = st.text_area("Příklad z praxe k 2. pojmu:", placeholder="Příklad...", height=70, key="p2_e2")
                
            term_3 = st.text_input("3. Vybraný pojem:", placeholder="Např. CSR", key="p2_t3")
            ex_3 = st.text_area("Příklad z praxe k 3. pojmu:", placeholder="Příklad...", height=70, key="p2_e3")

            if st.button("Uložit mé příklady do slovníčku"):
                st.success("Vaše příklady byly uloženy!")

        with st.container(border=True):
            st.markdown("### AI mentoring ke slovníčku")
            st.write("Zkopíruj tento prompt do svého AI asistenta:")
            st.markdown("""
            <div class='box-purple'>
                <strong>Prompt pro AI asistenta:</strong><br>
                Vysvětli mi tyto pojmy na mém podnikatelském nápadu: podnikatel, fyzická osoba, právnická osoba a živnost.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("""
            <div class='box-gray'>
                <strong>Opora v legislativě:</strong> Občanský zákoník, živnostenský zákon, zákon o obchodních korporacích a zákon o veřejných rejstřících.
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class='box-green'>
                <strong>Etika v podnikání:</strong> Podnikání není jen o legálnosti. Férový podnikatel nezneužívá švarcsystém, platí daně, jedná poctivě se zákazníky a chová se ohleduplně k zaměstnancům, partnerům i životnímu prostředí.
            </div>
            """, unsafe_allow_html=True)

    # PODKAPITOLA 3
    elif selected_section == "3. OSVČ a živnosti":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 3</div>", unsafe_allow_html=True)
        st.markdown("## 3. OSVČ a živnosti")
        
        with st.container(border=True):
            st.write("""
            **OSVČ** znamená osoba samostatně výdělečně činná. Jde o podnikání fyzické osoby — tedy člověka, který podniká vlastním jménem a nese za své podnikání plnou odpovědnost.
            """)
            st.markdown("""
            <div class='box-blue'>
                <strong>Proč je to důležité:</strong> Podnikání jako OSVČ vypadá jednoduše, ale má právní, daňové a sociální důsledky. Je proto důležité znát základní podmínky živnostenského podnikání, povinnosti vůči státu a riziko osobního ručení.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 3.1 OSVČ jako nejčastější start malé podnikavosti")
            st.write("""
            OSVČ je pro mnoho lidí nejjednodušší cesta, jak začít. Hodí se pro malé služby, freelancing, řemeslo, doučování, správu sociálních sítí, grafiku, fotografování, tvorbu webů, e-shop v menším rozsahu nebo lokální podnikání.
            
            **Výhoda:** Rychlý start a menší administrativa než u firmy.<br>
            **Nevýhoda:** Vyšší osobní riziko — OSVČ obvykle ručí za závazky celým svým osobním majetkem.
            """, unsafe_allow_html=True)

            st.markdown("""
            | Situace | Proč může OSVČ dávat smysl | Na co si dát pozor |
            | :--- | :--- | :--- |
            | **Student spravuje sociální sítě lokální kavárně.** | Nízké vstupní náklady, služba založená na dovednosti. | Smlouva, fakturace, daně, autorská práva k obsahu. |
            | **Grafik tvoří loga a šablony.** | Lze začít s notebookem a portfoliem. | Licenční podmínky, termíny, reklamace, komunikace s klientem. |
            | **Kadeřník nebo kosmetička chce pracovat samostatně.** | Vlastní zákazníci, možnost budovat značku. | Odborná způsobilost, hygiena, provozovna, odpovědnost. |
            | **Malý e-shop prodává vlastní produkty.** | Jednoduchý start a přímý kontakt se zákazníkem. | Obchodní podmínky, reklamace, sklad, ochrana spotřebitele. |
            """)

        with st.container(border=True):
            st.markdown("### 3.2 OSVČ a digitální realita")
            st.write("""
            Dnešní OSVČ často nepotřebuje jen živnostenské oprávnění. Potřebuje také digitální a finanční gramotnost:
            * oddělit osobní a podnikatelské peníze,
            * evidovat příjmy a výdaje,
            * zálohovat doklady,
            * chránit osobní údaje zákazníků (GDPR),
            * nepoužívat cizí fotografie, hudbu a texty bez práv,
            * komunikovat transparentně cenu, dodání a podmínky,
            * počítat s daněmi a odvody dřív, než peníze utratí.
            """)

            st.markdown("""
            <div class='box-green'>
                <strong>Pravidlo pro začátečníka:</strong> To, co přijde na účet, není celé „moje výplata“. Část peněz patří na náklady, daně, sociální a zdravotní pojištění, rezervu a budoucí investice.
            </div>
            """, unsafe_allow_html=True)

            st.markdown("#### Mini simulace OSVČ & Kalkulačka hodinové sazby")
            st.write("Představ si, že OSVČ za měsíc vyfakturuje **28 000 Kč**. Náklady na software, dopravu, materiál a reklamu jsou **6 000 Kč**.")
            
            c_sim1, c_sim2 = st.columns(2)
            with c_sim1:
                profit_calc = 28000 - 6000
                st.markdown(f"**Orientační zisk před daněmi:** **{profit_calc:,} Kč** (28 000 − 6 000 Kč).")
                reserve_pct = st.slider("Kolik % z tržby by si měla OSVČ odložit stranou?", min_value=10, max_value=50, value=30, step=5)
                st.info(f"Při {reserve_pct} % si odložíte: {28000 * (reserve_pct/100):,.0f} Kč.")
            with c_sim2:
                st.text_area("Vysvětli, proč není bezpečné utratit celých 28 000 Kč:", placeholder="Napište důvod...", height=110, key="p3_sim_ans")

            # KALKULAČKA SAZBY
            st.markdown("##### Výpočet minimální potřebné hodinové sazby")
            c_calc1, c_calc2 = st.columns(2)
            with c_calc1:
                prijem_calc = st.number_input("Požadovaný čistý příjem měsíčně (Kč):", value=35000, step=1000, key="calc_prijem")
                naklady_calc = st.number_input("Měsíční provozní náklady (Kč):", value=6000, step=500, key="calc_nakklady")
            with c_calc2:
                hodiny_calc = st.number_input("Odpracované fakturovatelné hodiny / měsíc:", value=110, step=10, key="calc_hodiny")
                odvody_calc = st.number_input("Měsíční zálohy na odvody (Kč):", value=8311, step=500, key="calc_odvody")

            potrebny_prijem = prijem_calc + naklady_calc + odvody_calc
            vysledna_sazba = potrebny_prijem / hodiny_calc if hodiny_calc > 0 else 0
            
            st.markdown(f"""
            <div class='box-green'>
                <strong>Minimální potřebná hodinová sazba:</strong> <span style='font-size: 1.2rem; font-weight: 800;'>{vysledna_sazba:.0f} Kč / hod.</span><br>
                <small>(Celkem potřebuješ vyfakturovat <strong>{potrebny_prijem:,} Kč</strong> měsíčně na pokrytí odvodů, nákladů a čistého příjmu).</small>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class='box-yellow'>
                <strong>Interaktivní výzva:</strong> Napiš, jestli by se tvůj projekt dal na začátku provozovat jako OSVČ, a uveď jedno hlavní riziko.
            </div>
            """, unsafe_allow_html=True)
            st.text_input("Váš projekt jako OSVČ + hlavní riziko:", placeholder="Napište odpověď...", key="p3_user_risk")

            st.markdown("""
            <div class='box-purple'>
                <strong>AI mentoring:</strong> Zkopíruj tento prompt do AI asistenta:<br>
                <i>„Podívej se na můj nápad a navrhni, jaký typ živnosti by mohl připadat v úvahu a co si mám ověřit.“</i>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class='box-red'><strong>Hlavní riziko OSVČ:</strong> OSVČ ručí za závazky z podnikání celým svým osobním majetkem. Jednoduchý start tedy neznamená nulové riziko.</div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 3.3 Podmínky pro podnikání jako OSVČ")
            st.write("""
            **Co musí splnit začínající OSVČ?**
            1. Dosažení věku 18 let (plná svéprávnost),
            2. Svéprávnost,
            3. Bezúhonnost (dokládá se výpisem z trestního rejstříku),
            4. Případně odborná způsobilost podle druhu živnosti.
            """)
            st.text_area("Interaktivní výzva: Vypiš, které podmínky by musel splnit začínající podnikatel ve tvém konkrétním příkladu:", placeholder="Moje podmínky...", height=80, key="p3_cond_user")

        with st.container(border=True):
            st.markdown("### 3.4 Druhy živností")
            st.markdown("""
            | Druh živnosti | Co znamená | Příklad |
            | :--- | :--- | :--- |
            | **Volná živnost** | Není potřeba speciální vzdělání ani praxe. Stačí splnit všeobecné podmínky. | E-shop, marketingové služby, správa sociálních sítí. |
            | **Řemeslná živnost** | Vyžaduje odbornou způsobilost, například výuční list nebo praxi. | Truhlářství, kadeřnictví, opravy strojů. |
            | **Vázaná živnost** | Vyžaduje specifické vzdělání, praxi nebo zkoušku. | Účetní poradenství, průvodcovská činnost, masérské služby. |
            | **Koncesovaná živnost** | Vyžaduje státní povolení — koncesi. Jde o více regulované nebo rizikovější činnosti. | Taxislužba, provozování střelnice, prodej zbraní. |
            """)

            st.markdown("#### Zařazení vlastního nápadu k živnosti")
            c_z1, c_z2 = st.columns(2)
            with c_z1:
                st.text_input("Můj nápad:", placeholder="Název nápadu...", key="p3_z_idea")
                st.selectbox("Pravděpodobný typ živnosti:", ["Volná živnost", "Řemeslná živnost", "Vázaná živnost", "Koncesovaná živnost"], key="p3_z_type")
            with c_z2:
                st.text_area("Proč si myslím, že jde o tento typ:", placeholder="Důvod...", height=70, key="p3_z_why")
                st.text_input("Co si ještě musím ověřit:", placeholder="Ověření...", key="p3_z_check")

        with st.container(border=True):
            st.markdown("### 3.5 Jak si zařídit živnost")
            st.markdown("""
            1. Rozhodnout se, o jaký typ živnosti jde.
            2. Ověřit podmínky — všeobecné i případné zvláštní.
            3. Vyplnit **Jednotný registrační formulář (JRF)** – nové podání.
            4. Ohlásit živnost nebo požádat o koncesi (osobně na ŽÚ nebo elektronicky).
            5. Ověřit daňové, zdravotní a sociální povinnosti.
            """)
            st.markdown("""
            <div class='box-green'>
                <strong>Digitální praxe:</strong> Portál živnostenského podnikání (rzp.cz) a veřejné rejstříky slouží k ověřování údajů, podávání žádostí a kontrole obchodních partnerů.
            </div>
            """, unsafe_allow_html=True)
            st.text_area("Interaktivní výzva: Sepiš první tři kroky, které bys udělal/a před ohlášením živnosti u svého projektu:", placeholder="1. krok...\n2. krok...\n3. krok...", height=90, key="p3_steps_user")

        with st.container(border=True):
            st.markdown("### 3.6 Povinnosti živnostníka: legislativní minimum")
            st.write("Živnostník neřeší jen zákazníky a cenu. Musí také splnit základní registrační, daňové a pojistné povinnosti.")
            
            st.markdown("""
            <div class='box-blue'>
                <strong>Legislativní minimum pro OSVČ:</strong> Přesné částky a termíny se mohou měnit, proto je potřeba ověřovat aktuální informace na stránkách Finanční správy, ČSSZ, zdravotní pojišťovny a Portálu živnostenského podnikání.
            </div>
            """, unsafe_allow_html=True)

            st.write("""
            **Co musí živnostník typicky dělat?**
            * **Ohlásit živnost nebo požádat o koncesi:** na živnostenském úřadě, často přes Jednotný registrační formulář (JRF), který zároveň pomůže s oznámením vůči FÚ, ČSSZ a ZP.
            * **Platit daň z příjmů fyzických osob:** podává se daňové přiznání. Lhůta je do 3 měsíců (písemně), 4 měsíců (elektronicky) nebo 6 měsíců (s daňovým poradcem).
            * **Zvážit paušální daň:** v jedné měsíční platbě řeší daň, sociální i zdravotní pojištění.
            * **Platit sociální pojištění:** měsíční zálohy na ČSSZ + roční přehled o příjmech a výdajích.
            * **Platit zdravotní pojištění:** měsíční zálohy zdravotní pojišťovně + roční přehled.
            * **Vést evidenci:** daňovou evidenci, účetnictví nebo evidenci příjmů při uplatnění výdajů procentem (paušální výdaje).
            * **Hlásit důležité změny:** změnu adresy, přerušení/ukončení činnosti, změnu zdravotní pojišťovny.
            """)

            st.markdown("""
            <div class='box-yellow'>
                <strong>Praktické pravidlo:</strong> Živnostník by si měl od každé přijaté platby odkládat část peněz na daň, sociální a zdravotní pojištění. To, co přijde na účet, ještě není čistý příjem.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 3.7 Daně a odvody OSVČ úplně jednoduše")
            st.markdown("""
            <div class='box-red'>
                <strong>Důležité zjednodušení:</strong> Přesné částky se každý rok mění. V první kapitole stačí pochopit princip: OSVČ platí daň z příjmů a odvody na sociální a zdravotní pojištění.
            </div>
            """, unsafe_allow_html=True)

            st.write("""
            **Co OSVČ typicky platí?**
            * **Daň z příjmů FO:** základní sazba 15 % ze základu daně (zisk = příjmy − výdaje).
            * **Sociální pojištění:** na důchodový systém a státní politiku zaměstnanosti.
            * **Zdravotní pojištění:** na financování zdravotní péče.
            * **Zálohy:** pravidelné měsíční platby během roku.
            """)

            st.markdown("""
            <div class='box-blue'>
                <strong>Jednoduchý příklad:</strong> Jana má za rok příjmy 300 000 Kč a výdaje 120 000 Kč. Její zisk je tedy 180 000 Kč. Z tohoto zisku se teprve počítá daň a pojistné. Neznamená to, že si může celých 180 000 Kč nechat bez dalších povinností.
            </div>
            """, unsafe_allow_html=True)

            st.markdown("#### Modelový výpočet odvodů OSVČ (2026)")
            st.write("Příklad počítá s OSVČ na hlavní činnost (neplátce DPH, příjmy 300 000 Kč, výdaje 120 000 Kč, zisk 180 000 Kč):")

            st.markdown("""
            | Varianta | Jak se platí | Co je v částce zahrnuto | Orientační částka |
            | :--- | :--- | :--- | :--- |
            | **Bez paušální daně** | OSVČ řeší platby zvlášť. | Daň vyjde po slevě 0 Kč. Dále min. sociální p. (5 005 Kč/měs.) + min. zdravotní p. (3 306 Kč/měs.). | **~8 311 Kč / měsíc** (99 732 Kč / rok) |
            | **S paušální daní (I. pásmo)** | OSVČ posílá jednu platbu. | Zahrnuje daň z příjmů, sociální i zdravotní pojištění dohromady. | **9 162 Kč / měsíc** (109 944 Kč / rok) |
            """)

            st.write("""
            **Co z příkladu plyne?**
            Bez paušální daně se platby počítají odděleně. Paušální daň je administrativně jednodušší (jedna platba, bez přiznání), ale u nižšího zisku nemusí být levnější.
            
            **Kdy se paušální daň vyplatí?**
            Představ si OSVČ v roce 2026 s ročním příjmem **1 000 000 Kč** a 60% výdajovým paušálem (výdaje 600 000 Kč, základ 400 000 Kč). Tady už je paušální daň v I. pásmu (9 162 Kč/měs.) výhodnější finančně i administrativně.
            """)

            st.markdown("""
            | Krok | Jednoduché vysvětlení |
            | :--- | :--- |
            | **Příjmy** | Kolik OSVČ vyfakturovala zákazníkům. |
            | **Výdaje** | Kolik ji stálo podnikání (materiál, software, doprava, reklama). |
            | **Zisk / základ** | Příjmy minus výdaje. Z něj se řeší daň a pojistné. |
            | **Zálohy** | Pravidelné platby během roku. |
            """)

            st.markdown("""
            <div class='box-yellow'>
                <strong>Praktické pravidlo pro začátečníka:</strong> Když OSVČ dostane zaplaceno, neměla by všechno utratit. Část peněz si musí odložit na daň, sociální a zdravotní pojištění.
            </div>
            """, unsafe_allow_html=True)

    # PODKAPITOLA 4
    elif selected_section == "4. Obchodní korporace":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 4</div>", unsafe_allow_html=True)
        st.markdown("## 4. Obchodní korporace")
        
        with st.container(border=True):
            st.write("""
            Obchodní korporace jsou právnické osoby založené podle zákona o obchodních korporacích. Patří mezi ně **obchodní společnosti** a **družstva**. V praxi vytvářejí samostatný subjekt — firmu, která má vlastní název, sídlo, majetek, orgány, pravidla rozhodování a odpovědnost.
            
            Je důležité pochopit, že obchodní korporace není jen „větší podnikání“. Je to právní forma, která určuje:
            * kdo podnik vlastní,
            * kdo za něj jedná,
            * jak se ručí za dluhy,
            * jak se vkládají peníze nebo práce,
            * jak se rozhoduje,
            * jak se rozděluje zisk,
            * jak firma vzniká a zaniká,
            * jakou administrativu musí plnit.
            """)

            st.markdown("""
            <div class='box-blue'>
                <strong>Proč je to důležité:</strong> Právní forma podnikání ovlivňuje ručení, povinnosti, daně, administrativu i důvěryhodnost vůči zákazníkům, bankám a partnerům. Nejde o učení paragrafů nazpaměť, ale o pochopení, proč se právní forma volí odpovědně.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 4.1 Proč právní forma není formalita")
            st.write("""
            Právní forma rozhoduje o tom, kdo nese riziko, kdo jedná za podnik, jak se rozděluje zisk, jak složitá je administrativa a jak podnik působí na banky, investory, dodavatele i zákazníky.
            Pro současnou generaci je důležité pochopit, že právní forma není „nudná kolonka ve formuláři“. Je to bezpečnostní a strategické rozhodnutí.
            """)

            st.markdown("""
            <div class='box-gray'>
                <strong>Zákonný základ:</strong> Obchodní korporace upravuje zejména zákon č. 90/2012 Sb., o obchodních korporacích (ZOK). Jejich vznik, zápis a veřejné údaje souvisejí také s občanským zákoníkem, živnostenským zákonem, zákonem o veřejných rejstřících a daňovými předpisy.
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            | Otázka | Proč je důležitá | Příklad |
            | :--- | :--- | :--- |
            | **Kolik riskuji?** | Určuje, zda podnikatel ohrožuje i osobní majetek. | OSVČ ručí jinak než společník v s.r.o. |
            | **Podnikám sám/sama, nebo v týmu?** | Ovlivňuje rozhodování, podíly a odpovědnost. | Dva zakladatelé e-shopu potřebují jasná pravidla. |
            | **Potřebuji investora?** | Investor obvykle chce přehlednou vlastnickou strukturu. | Startup může kvůli investorovi zvolit s.r.o. nebo a.s. |
            | **Jak moc poroste podnikání?** | Růst zvyšuje rizika, počet smluv, zaměstnance a finance. | Malý freelancing zvládne OSVČ, větší tým spíš firma. |
            """)

        with st.container(border=True):
            st.markdown("### 4.2 Co patří mezi obchodní korporace")
            st.write("""
            Obchodní korporace se dělí na:
            1. **obchodní společnosti**,
            2. **družstva**.

            Obchodní společnosti se dále dělí na:
            * **osobní společnosti** — veřejná obchodní společnost (v.o.s.) a komanditní společnost (k.s.),
            * **kapitálové společnosti** — společnost s ručením omezeným (s.r.o.) a akciová společnost (a.s.).
            """)

            st.markdown("""
            | Skupina | Formy | Typický znak |
            | :--- | :--- | :--- |
            | **Osobní společnosti** | v.o.s., k.s. | Důležitá je osobní účast společníků, důvěra a často vyšší míra ručení. |
            | **Kapitálové společnosti** | s.r.o., a.s. | Důležitý je vklad kapitálu, podíly nebo akcie a oddělení firmy od osobního majetku vlastníků. |
            | **Družstva** | družstvo, evropská družstevní forma (SCE) | Důležité je členství, spolupráce a společný prospěch členů. |
            """)

        with st.container(border=True):
            st.markdown("### 4.3 Obecné zákonné podmínky vzniku obchodní korporace")
            st.write("Každá obchodní korporace má svá specifická pravidla, ale některé kroky se opakují u většiny forem.")

            st.markdown("""
            | Krok | Co znamená | Proč je důležitý |
            | :--- | :--- | :--- |
            | **Zakladatelské právní jednání** | Sepsání společenské smlouvy, zakladatelské listiny nebo stanov podle typu korporace. | Určuje základní pravidla firmy: název, sídlo, společníky, vklady, orgány a rozhodování. |
            | **Obchodní firma** | Název, pod kterým korporace vystupuje. | Musí být odlišitelný a nesmí být klamavý. Zákazník má vědět, s kým jedná. |
            | **Sídlo** | Adresa zapsaná ve veřejném rejstříku. | Slouží pro kontakt, doručování a identifikaci firmy. |
            | **Předmět podnikání / činnosti** | Vymezení, co bude korporace dělat. | Často je potřeba živnostenské oprávnění nebo jiné povolení. |
            | **Vklady** | Peníze nebo jiné hodnoty, které společníci nebo členové do korporace vkládají. | Ukazují majetkovou účast a mohou ovlivnit podíl na zisku i hlasování. |
            | **Orgány korporace** | Osoby nebo skupiny, které rozhodují a jednají za firmu. | Bez jasných orgánů není zřejmé, kdo firmu řídí a kdo ji zastupuje navenek. |
            | **Zápis do obchodního rejstříku** | Veřejný zápis základních údajů o korporaci. | Obchodní korporace zpravidla **vzniká až zápisem do obchodního rejstříku**. |
            """)

            st.markdown("""
            <div class='box-gray'>
                <strong>Praktická poznámka pro tebe:</strong> Firma nezačíná jen logem a Instagramem. Nejdřív musí být jasné, kdo ji zakládá, za jakým účelem, jak ručí, kdo rozhoduje a jaké údaje budou veřejně dohledatelné.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 4.4 Volba právní formy podle situace (9 otázek: OSVČ, nebo s.r.o.?)")
            st.write("U každé otázky vyber odpověď, která lépe odpovídá tvému projektu:")

            q1 = st.radio("1️⃣ Plánuješ podnikat sám/sama, nebo v týmu?", ["Spíš OSVČ: Podnikám sám/sama a rozhoduji hlavně za sebe.", "Spíš s.r.o.: Podnikáme v týmu a potřebujeme jasně rozdělit role, odpovědnost a podíly."], key="q1_full")
            q2 = st.radio("2️⃣ Jde hlavně o osobní práci, nebo projekt s růstem?", ["Spíš OSVČ: Nabízím hlavně vlastní práci, službu nebo dovednost.", "Spíš s.r.o.: Projekt má růst, rozšiřovat se a fungovat jako samostatná firma."], key="q2_full")
            q3 = st.radio("3️⃣ Potřebujete řešit podíly a zakladatelskou dohodu?", ["Spíš OSVČ: Zatím nepotřebuji řešit podíly mezi více zakladateli.", "Spíš s.r.o.: Je nás víc a potřebujeme jasně určit, kdo má jaký podíl a kdo o čem rozhoduje."], key="q3_full")
            q4 = st.radio("4️⃣ Hrozí větší finanční závazky?", ["Spíš OSVČ: Náklady jsou nízké a projekt lze rychle zastavit bez velkých dluhů.", "Spíš s.r.o.: Projekt vyžaduje větší nákupy, úvěr, sklad, drahé vybavení nebo dlouhodobé smlouvy."], key="q4_full")
            q5 = st.radio("5️⃣ Může vzniknout škoda, reklamace nebo odpovědnost vůči zákazníkům?", ["Spíš OSVČ: Riziko škody nebo reklamací je malé a dobře zvládnutelné.", "Spíš s.r.o.: Chyba může způsobit větší škodu, reklamace nebo právní odpovědnost."], key="q5_full")
            q6 = st.radio("6️⃣ Potřebuješ chránit osobní majetek?", ["Spíš OSVČ: Riziko je malé a nevadí mi vyšší osobní odpovědnost.", "Spíš s.r.o.: Chci lépe oddělit osobní majetek od podnikání."], key="q6_full")
            q7 = st.radio("7️⃣ Budeš potřebovat investora, banku nebo větší partnery?", ["Spíš OSVČ: Nepotřebuji investora ani složitější vlastnickou strukturu.", "Spíš s.r.o.: Chci jednat s investorem, bankou nebo většími obchodními partnery."], key="q7_full")
            q8 = st.radio("8️⃣ Chceš rychle otestovat nápad, nebo budovat firmu?", ["Spíš OSVČ: Chci začít jednoduše a nejdřív si ověřit, jestli nápad funguje.", "Spíš s.r.o.: Od začátku počítám s budováním značky, týmu a dlouhodobé firmy."], key="q8_full")
            q9 = st.radio("9️⃣ Bude projekt pracovat s dalšími lidmi?", ["Spíš OSVČ: Většinu práce zvládne jeden člověk nebo občasná jednoduchá spolupráce.", "Spíš s.r.o.: Projekt bude potřebovat tým, zaměstnance, dodavatele nebo jasnější řízení spolupráce."], key="q9_full")

            if st.button("Vyhodnotit test 9 otázek"):
                sro_cnt = sum([1 for q in [q1, q2, q3, q4, q5, q6, q7, q8, q9] if "Spíš s.r.o." in q])
                osvc_cnt = 9 - sro_cnt
                if sro_cnt > osvc_cnt:
                    st.markdown(f"""
                    <div class='box-blue'>
                        <strong>Výsledek testu ({sro_cnt}× s.r.o. vs {osvc_cnt}× OSVČ):</strong> Pro váš projekt se jeví vhodnější uvažovat o <strong>s.r.o.</strong> z důvodu týmu, vyššího rizika, plánovaného růstu nebo ochrany majetku.
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class='box-green'>
                        <strong>Výsledek testu ({osvc_cnt}× OSVČ vs {sro_cnt}× s.r.o.):</strong> Pro váš start je pravděpodobně vhodnější začít jako <strong>OSVČ</strong> pro rychlé ověření nápadu s nižší administrativou.
                    </div>
                    """, unsafe_allow_html=True)

            st.markdown("""
            <div class='box-yellow'>
                <strong>Jak si výsledek vyložit:</strong> Pokud převažují zaškrtnuté odpovědi Spíš OSVČ, bude pro začátek pravděpodobně vhodnější OSVČ. Pokud převažují zaškrtnuté odpovědi Spíš s.r.o., bude pro projekt pravděpodobně vhodnější uvažovat o s.r.o. Nejde o právní radu, ale o pomůcku k rozhodování podle rizika, týmu, růstu a odpovědnosti.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 4.5 Moderní pohled: firma jako důvěryhodná značka")
            st.write("""
            Zákazník dnes často posuzuje firmu podle webu, sociálních sítí, recenzí a transparentnosti. Právní forma může ovlivnit důvěru:
            * zákazník chce vědět, s kým uzavírá smlouvu,
            * dodavatel chce vědět, kdo zaplatí fakturu,
            * banka chce vědět, kdo ručí,
            * investor chce vědět, kdo vlastní podíly,
            * zaměstnanec chce vědět, kdo ho zaměstnává.
            """)

            st.markdown("""
            <div class='box-gray'>
                <strong>Digitální stopa firmy:</strong> U každého podnikání je dobré ověřit název, IČO, právní formu, osobu jednající za firmu, web, recenze a veřejné rejstříky. Důvěryhodnost dnes vzniká i tím, že informace souhlasí napříč zdroji.
            </div>
            """, unsafe_allow_html=True)

            st.text_input("🧩 Interaktivní výzva: Rozhodni, jestli by tvému projektu pomohlo oddělit firmu od osobního majetku zakladatele. Napiš jeden důvod:", placeholder="Můj důvod...", key="p4_sep_reason")

            st.markdown("""
            <div class='box-purple'>
                <strong>AI mentoring:</strong> Zkopíruj tento prompt do AI asistenta:<br>
                <i>„Porovnej pro můj projekt OSVČ, s.r.o. a a.s. podle rizika, administrativy a růstu.“</i>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class='box-blue'>
                <strong>Jednoduše řečeno:</strong> Právní forma je „kabát“, ve kterém podnikání vystupuje navenek. Jinak se podniká jako jednotlivec na živnost a jinak jako firma.<br><br>
                <strong>Proč to souvisí s důvěryhodností:</strong> Zákazník, dodavatel i investor se podle právní formy lépe orientují v tom, s kým jednají, kdo rozhoduje a kdo nese odpovědnost.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 4.6 Osobní společnosti")
            st.write("Osobní společnosti stojí hlavně na osobní účasti, důvěře a odpovědnosti společníků.")
            st.text_input("🧩 Interaktivní výzva: Napiš, kdy by ve tvém projektu dávalo smysl podnikat s další osobou na základě vysoké důvěry:", placeholder="Odpověď...", key="p4_trust_user")

            st.markdown("#### Veřejná obchodní společnost (v.o.s.)")
            st.write("""
            Veřejná obchodní společnost je osobní společnost, ve které podnikají alespoň dvě osoby pod společnou firmou. Zákonně jde o formu vhodnou spíše pro osoby, které si velmi důvěřují. Důvod je jednoduchý: **společníci ručí za dluhy společnosti společně a nerozdílně celým svým majetkem**. To znamená, že věřitel se může domáhat splnění dluhu i po jednom ze společníků, a ten si potom případně vypořádává vztahy s ostatními.

            * Společníci se obvykle osobně podílejí na řízení firmy.
            * Zákon nestanoví povinný základní kapitál.
            * Společníci ručí za závazky společnosti společně a nerozdílně celým svým majetkem.

            **Zákonné a praktické znaky v.o.s.:**
            * zakládají ji alespoň dvě osoby,
            * společnost vzniká zápisem do obchodního rejstříku,
            * obchodní firma obvykle obsahuje označení „veřejná obchodní společnost“ nebo zkratku „v.o.s.“,
            * společníci se podílejí na podnikání a ručí osobním majetkem,
            * zisk a ztráta se rozdělují podle společenské smlouvy, jinak podle zákonných pravidel,
            * kvůli vysokému ručení je potřeba silná důvěra mezi společníky.
            """)

            st.text_input("🧩 Interaktivní výzva: Uveď jednu situaci, kdy by ručení celým majetkem bylo pro společníky příliš velké riziko:", placeholder="Situace...", key="p4_vos_risk")

            c_v1, c_v2 = st.columns(2)
            with c_v1:
                st.markdown("<div class='box-red'><strong>Hlavní nevýhoda v.o.s.:</strong> Vysoké osobní riziko společníků.</div>", unsafe_allow_html=True)
            with c_v2:
                st.markdown("<div class='box-green'><strong>Hlavní výhoda v.o.s.:</strong> Jednoduché založení a silná osobní důvěra mezi společníky.</div>", unsafe_allow_html=True)

            st.markdown("""
            <div class='box-gray'>
                <strong>Příklad z praxe — v.o.s.:</strong> Jako veřejná obchodní společnost v ČR působí například Kaufland Česká republika v.o.s. Právní formu je vždy nejlepší ověřit podle přesného názvu nebo IČO v obchodním rejstříku.
            </div>
            """, unsafe_allow_html=True)

            st.markdown("#### Komanditní společnost (k.s.)")
            st.write("Komanditní společnost kombinuje prvky osobní a kapitálové společnosti. Vždy v ní vystupují dva typy společníků:")
            
            st.text_input("🧩 Interaktivní výzva: Vymysli příklad, kdo by ve tvém projektu mohl být aktivní podnikatel a kdo investor:", placeholder="Aktivní vs Investor...", key="p4_ks_roles")

            st.markdown("""
            | Role | Komplementář | Komanditista |
            | :--- | :--- | :--- |
            | **Postavení** | Aktivně řídí společnost. | Spíše vkládá kapitál. |
            | **Ručení** | Ručí celým svým majetkem. | Ručí do výše nesplaceného vkladu. |
            | **Typická role** | „Ten, kdo podnik řídí.“ | „Ten, kdo přináší kapitál.“ |
            """)

            st.write("""
            **Zákonné a praktické znaky k.s.:**
            * musí mít alespoň jednoho komplementáře a alespoň jednoho komanditistu,
            * komplementář řídí společnost a ručí za její dluhy celým svým majetkem,
            * komanditista vkládá kapitál a ručí omezeně, typicky podle výše nesplaceného vkladu zapsaného v obchodním rejstříku,
            * společnost vzniká zápisem do obchodního rejstříku,
            * obchodní firma obsahuje označení „komanditní společnost“ nebo zkratku „k.s.“,
            * hodí se pro situace, kdy jeden človek projekt aktivně řídí a druhý spíše poskytuje kapitál.
            """)

            st.markdown("""
            <div class='box-red'>
                <strong>Riziko pro komplementáře:</strong> Komplementář je v k.s. v podobné rizikové pozici jako společník v.o.s. Pokud projekt vytváří vysoké závazky, je potřeba velmi dobře zvážit, zda je tato forma bezpečná.
            </div>
            """, unsafe_allow_html=True)

            c_k1, c_k2 = st.columns(2)
            with c_k1:
                st.markdown("<div class='box-green'><strong>Hlavní výhoda k.s.:</strong> Umožňuje spojit aktivního podnikatele s investorem, který do firmy vkládá kapitál.</div>", unsafe_allow_html=True)
            with c_k2:
                st.markdown("<div class='box-red'><strong>Hlavní nevýhoda k.s.:</strong> Komplementář ručí za závazky společnosti celým svým majetkem.</div>", unsafe_allow_html=True)

            st.markdown("""
            <div class='box-gray'>
                <strong>Příklad z praxe — k.s.:</strong> Komanditní společnost se dnes používá méně často než s.r.o. nebo a.s., ale stále existuje. Aktuální příklady je vhodné hledat přímo v obchodním rejstříku podle právní formy komanditní společnost / k.s. a ověřit, kdo je komplementář a kdo komanditista.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 4.7 Kapitálové společnosti")
            st.write("Kapitálové společnosti stojí více na vloženém kapitálu než na osobní účasti společníků. Typicky lépe oddělují firmu od osobního majetku vlastníků.")
            st.text_input("🧩 Interaktivní výzva: Napiš, jaký kapitál, vybavení nebo tým by tvůj projekt potřeboval, aby dávala smysl kapitálová společnost:", placeholder="Kapitál a vybavení...", key="p4_cap_req")

            st.markdown("#### Společnost s ručením omezeným (s.r.o.)")
            st.write("""
            Společnost s ručením omezeným je jednou z nejčastějších forem podnikání v ČR. Je oblíbená proto, že umožňuje poměrně dostupné založení firmy a zároveň lépe odděluje podnikání od osobního života zakladatele. S.r.o. je vhodná pro menší a střední podnikání, rodinné firmy, startupy, e-shopy, služby i týmové projekty.

            * Vystupují v ní společníci a jednatel nebo více jednatelů.
            * Společníci mají vkladovou povinnost.
            * Ručení společníků je omezené hlavně výší nesplaceného vkladu.
            """)

            st.text_input("🧩 Interaktivní výzva: Napiš, v jakém okamžiku by se tvému projektu vyplatilo přejít z OSVČ na s.r.o.:", placeholder="Okamžik přechodu...", key="p4_switch_moment")

            st.write("""
            **Zákonné a praktické podmínky s.r.o.:**
            * může ji založit jedna nebo více osob,
            * zakládá se společenskou smlouvou nebo zakladatelskou listinou,
            * vzniká zápisem do obchodního rejstříku,
            * obchodní firma obsahuje označení „společnost s ručením omezeným“, „spol. s r.o.“ nebo „s.r.o.“,
            * základní kapitál je tvořen vklady společníků,
            * minimální výše vkladu společníka může být podle zákona 1 Kč, pokud společenská smlouva neurčí více,
            * **poznámka k praxi:** zákon tedy sice umožňuje založit s.r.o. s vkladem 1 Kč, ale v praxi to nemusí být bezpečné — firma pak nemá žádnou finanční rezervu na první náklady, chyby nebo reklamace,
            * společníci ručí za dluhy společnosti jen do výše, v jaké nesplnili vkladovou povinnost podle zápisu v obchodním rejstříku,
            * statutárním orgánem je jeden nebo více jednatelů,
            * nejvyšším orgánem je valná hromada, případně jediný společník vykonává její působnost.
            """)

            st.markdown("""
            | Otázka u s.r.o. | Co máš pochopit |
            | :--- | :--- |
            | **Stačí vklad 1 Kč?** | Zákon to umožňuje, ale pro podnikatele to není příliš bezpečný start. Firma s vkladem 1 Kč nemá téměř žádný vlastní kapitál, takže i běžné počáteční náklady, zpožděné platby nebo reklamace mohou rychle vytvořit problém. Bezpečnější je počítat s reálnou finanční rezervou. |
            | **Ručí společník osobním majetkem?** | Společník obvykle neručí jako OSVČ celým majetkem, ale musí splnit vkladovou povinnost. Odpovědnost jednatele je samostatné téma. |
            | **Kdo jedná za firmu?** | Jednatel. Je zapsaný v obchodním rejstříku a má povinnost jednat s péčí řádného hospodáře. |
            | **Kdo rozhoduje o důležitých věcech?** | Valná hromada společníků nebo jediný společník. Rozhoduje například o zásadních otázkách, změnách smlouvy nebo rozdělení zisku. |
            """)

            st.markdown("""
            <div class='box-yellow'>
                <strong>Praktické pravidlo:</strong> OSVČ bývá jednodušší pro start. S.r.o. dává větší smysl tehdy, když podnikání roste, přibývají rizika, vzniká tým nebo je potřeba oddělit osobní majetek od podnikání.
            </div>
            """, unsafe_allow_html=True)

            st.write("""
            **Orgány s.r.o. a rozdělení zisku:**
            * **Nejvyšší orgán:** valná hromada — tvoří ji společníci a rozhoduje o zásadních otázkách společnosti, například o schválení účetní závěrky a rozdělení zisku.
            * **Statutární orgán:** jeden nebo více jednatelů — jednají za společnost navenek a řídí její běžné záležitosti.
            * **Kontrolní orgán:** dozorčí rada — u s.r.o. je obvykle nepovinná, pokud ji neurčí společenská smlouva nebo zákon.
            * **Zisk:** rozděluje se až po zdanění daní z příjmů právnických osob a po schválení valnou hromadou. Společníci se na zisku obvykle podílejí podle výše svých podílů, pokud společenská smlouva neurčí jinak.
            """)

            st.markdown("#### Akciová společnost (a.s.)")
            st.write("""
            Akciová společnost je kapitálová společnost vhodná spíše pro větší projekty, investory a podnikání s významnějším kapitálem. Její základní kapitál je rozdělen na akcie.
            """)

            st.text_input("🧩 Interaktivní výzva: Představ si, že tvůj projekt hledá větší investory. Co by muselo být připravené, aby dávala smysl a.s.?:", placeholder="Příprava pro a.s....", key="p4_as_investors")

            st.write("""
            * Vlastníky jsou akcionáři.
            * Základní kapitál činí nejméně **2 000 000 Kč** nebo odpovídající částku v eurech podle zákona.
            * Základní kapitál vzniká úpisem akcií — akcionáři vkládají do společnosti kapitál a získávají za něj akcie.
            * Akcie je cenný papír nebo zaknihovaný cenný papír, se kterým jsou spojena práva akcionáře.
            * Akcionář má typicky právo podílet se na řízení společnosti hlasováním na valné hromadě, právo na podíl na zisku (dividendu) a právo na podíl na likvidačním zůstatku.
            * Akcionáři za závazky společnosti osobně neručí.

            **Zákonné a praktické podmínky a.s.:**
            * zakládá se přijetím stanov,
            * vzniká zápisem do obchodního rejstříku,
            * obchodní firma obsahuje označení „akciová společnost“ nebo zkratku „a.s.“,
            * základní kapitál je rozvržen na akcie,
            * minimální základní kapitál je 2 000 000 Kč nebo odpovídající částku v eurech podle zákonných pravidel,
            * akcionáři za dluhy společnosti neručí,
            * akcie vyjadřují podíl akcionáře na společnosti a jsou s nimi spojena práva,
            * společnost má složitější strukturu řízení a vyšší administrativní nároky než s.r.o.
            """)

            st.markdown("""
            <div class='box-blue'>
                <strong>Jednoduše:</strong> A.s. není vhodná pro většinu malých školních projektů. Je důležitá hlavně proto, abys pochopil/a svět větších firem, investorů, akcií, dividend a řízení kapitálové společnosti.
            </div>
            """, unsafe_allow_html=True)

            st.write("""
            **Orgány a.s. a dva systémy řízení:**
            * **Nejvyšší orgán:** valná hromada — rozhodují na ní akcionáři, například o zásadních změnách, volbě orgánů podle stanov a rozdělení zisku.
            * **Dualistický systém:** statutární orgán je představenstvo a kontrolní orgán je dozorčí rada. Řízení a kontrola jsou oddělené.
            * **Monistický systém:** statutárním orgánem je správní rada. V praxi soustřeďuje řízení a kontrolu blíže k jednomu orgánu.
            * **Zisk:** rozděluje se až po zdanění daní z příjmů právnických osob a po schválení valnou hromadou. Podíl akcionáře na zisku se nazývá **dividenda**.
            """)

            st.markdown("#### Družstvo")
            st.write("""
            Družstvo je právnická osoba založená na členství. Jeho smyslem není jen zisk pro vlastníky, ale také společný prospěch členů — například bydlení, práce, prodej výrobků nebo společné využívání služeb.
            """)

            st.text_input("🧩 Interaktivní výzva: Vymysli příklad, kdy by lidem dávalo smysl spojit se do družstva místo toho, aby každý řešil problém sám:", placeholder="Příklad družstva...", key="p4_druzstvo_ex")

            st.write("""
            * Členové družstva se podílejí na jeho činnosti.
            * Družstvo může sloužit k podnikání i k zajišťování potřeb členů.
            * Typickým příkladem může být bytové, výrobní, zemědělské nebo spotřební družstvo.
            * Důležitá je spolupráce, členství a společný zájem.

            **Zákonné a praktické znaky družstva:**
            * je založeno na členství,
            * má zpravidla alespoň tři členy,
            * vzniká zápisem do obchodního rejstříku,
            * obchodní firma obsahuje označení „družstvo“,
            * členové se podílejí na činnosti družstva,
            * orgány družstva typicky zahrnují členskou schůzi, představenstvo a kontrolní komisi; u menších družstev mohou být pravidla jednodušší podle zákonných možností,
            * smyslem může být podnikání i zajišťování potřeb členů,
            * hodí se tam, kde je důležitá spolupráce a společný prospěch.
            """)

            st.markdown("""
            <div class='box-blue'>
                <strong>Funkce družstva:</strong> Družstvo umožňuje lidem spojit síly, sdílet náklady, společně rozhodovat a řešit potřebu, kterou by jednotlivec zvládal obtížněji.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 4.8 Povinnosti členů orgánů: péče řádného hospodáře")
            st.write("""
            Osoby, které řídí obchodní korporaci nebo za ni jednají, nemohou rozhodovat libovolně. Musí jednat informovaně, pečlivě, loajálně a v zájmu korporace. Tento princip se označuje jako **péče řádného hospodáře**.
            Pro tebe je to důležité hlavně u jednatele s.r.o., členů představenstva a dalších osob ve vedení. Pokud někdo firmu řídí nezodpovědně, může nést právní následky.
            """)

            st.markdown("""
            | Situace | Odpovědné jednání | Rizikové jednání |
            | :--- | :--- | :--- |
            | **Firma podepisuje velkou smlouvu.** | Vedení si ověří cenu, rizika, závazky a schopnost plnit. | Podepíše smlouvu bez čtení, jen proto, že „to vypadá dobře“. |
            | **Firma má finanční problémy.** | Vedení sleduje cashflow, jedná s věřiteli a řeší situaci včas. | Ignoruje dluhy a objednává další služby, i když ví, že nezaplatí. |
            | **Firma pracuje s daty zákazníků.** | Nastaví přístupy, ochranu dat a jasná pravidla. | Sdílí zákaznická data v nechráněné tabulce bez pravidel. |
            """)

            st.markdown("""
            <div class='box-gray'>
                <strong>Didaktická pointa:</strong> Omezené ručení neznamená nulovou odpovědnost. Společník, jednatel, člen představenstva nebo člen družstva musí chápat svou roli a rozhodovat odpovědně.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 4.9 Přehled právních forem")
            st.text_input("🧩 Interaktivní výzva: Vyber pro svůj projekt jednu právní formu z tabulky a napiš její hlavní výhodu a riziko:", placeholder="Vybraná forma + výhoda a riziko...", key="p4_form_select")

            st.markdown("""
            | Forma | Administrativní náročnost | Míra rizika | Kapitál | Typický znak |
            | :--- | :--- | :--- | :--- | :--- |
            | **OSVČ** | Nízká | Vysoká — ručení celým majetkem | Není vyžadován | Rychlý a jednoduchý start |
            | **v.o.s.** | Střední | Vysoká — společníci ručí celým majetkem | Není vyžadován | Osobní důvěra společníků |
            | **k.s.** | Střední | Různé ručení komplementářů a komanditistů | Vklad komanditisty | Kombinace aktivního společníka a investora |
            | **s.r.o.** | Střední | Nižší — oddělení firmy od osobního majetku | Od 1 Kč, reálně více nákladů | Dostupná firemní forma |
            | **a.s.** | Vysoká | Nižší — akcionáři osobně neručí | Vyšší základní kapitál (min 2 mil. Kč) | Akcie, investoři, větší kapitál |
            | **družstvo** | Střední | Záleží na pravidlech a situaci družstva | Členské vklady | Společný prospěch členů |
            """)

        with st.container(border=True):
            st.markdown("### 4.10 Vznik obchodní korporace")
            st.write("Založení právnické osoby, například s.r.o. nebo a.s., je formální proces. Obvykle vyžaduje součinnost s notářem a zápis do obchodního rejstříku.")
            
            st.text_area("🧩 Interaktivní výzva: Seřaď kroky vzniku firmy podle toho, co bys musel/a řešit jako první, druhé a třetí:", placeholder="1. krok...\n2. krok...\n3. krok...", height=80, key="p4_steps_order")

            st.markdown("""
            1. Sepsání společenské smlouvy nebo zakladatelské listiny.
            2. Splacení vkladu nebo základního kapitálu.
            3. Získání živnostenského oprávnění, pokud je potřeba.
            4. Zápis do obchodního rejstříku.
            """)

            st.markdown("""
            <div class='box-blue'>
                <strong>Důležité pravidlo:</strong> Obchodní korporace **vzniká až dnem zápisu do obchodního rejstříku**.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 4.11 Co se zapisuje do obchodního rejstříku")
            st.write("Obchodní rejstřík je veřejný seznam. Díky němu si může zákazník, dodavatel, banka, úřad nebo budoucí zaměstnanec ověřit základní údaje o firmě.")
            
            st.markdown("""
            **Typicky se zapisuje:**
            * název firmy (obchodní firma),
            * sídlo,
            * právní forma,
            * identifikační číslo osoby (IČO),
            * předmět podnikání nebo činnosti,
            * statutární orgán a způsob jednání,
            * u některých forem také společníci, výše vkladů, základní kapitál nebo další údaje,
            * změny, zrušení, likvidace nebo další důležité skutečnosti.
            """)

            st.markdown("""
            <div class='box-gray'>
                <strong>Praktická aktivita:</strong> Otevři veřejný rejstřík na Justice.cz, najdi jednu s.r.o. a jednu a.s. a porovnej: právní formu, sídlo, statutární orgán, předmět podnikání a základní kapitál.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 4.12 Zrušení, likvidace a zánik obchodní korporace")
            st.write("Obchodní korporace nemusí existovat navždy. Může být zrušena dobrovolně, rozhodnutím orgánu společnosti, uplynutím doby, splněním účelu, rozhodnutím soudu nebo z jiných zákonných důvodů.")
            
            st.markdown("""
            **Je potřeba rozlišovat:**
            * **Zrušení** — rozhodnutí nebo právní skutečnost, že korporace končí,
            * **Likvidace** — vypořádání majetku, dluhů a vztahů, pokud zákon nestanoví jiný postup,
            * **Zánik** — konec právní existence, obvykle výmazem z obchodního rejstříku.
            """)

            st.markdown("""
            | Pojem | Jednoduché vysvětlení | Příklad |
            | :--- | :--- | :--- |
            | **Zrušení** | Firma vstoupí do fáze ukončování. | Společníci rozhodnou, že s.r.o. už nebude pokračovat. |
            | **Likvidace** | Firma vypořádá majetek, dluhy a pohledávky. | Prodá vybavení, zaplatí závazky a rozdělí zbytek podle pravidel. |
            | **Zánik** | Firma právně přestane existovat. | Po výmazu z obchodního rejstříku už korporace neexistuje. |
            """)

        with st.container(border=True):
            st.markdown("### 4.13 Daně a odvody u obchodních korporací úplně jednoduše")
            st.write("U obchodních korporací je důležité rozlišit firmu a člověka, který z ní dostává peníze. Firma může platit daň ze svého zisku. Pokud má zaměstnance, řeší také mzdy, sociální a zdravotní pojištění za zaměstnance. Když si vlastník vyplácí podíl na zisku, řeší se další zdanění podle pravidel pro daný typ příjmu.")

            st.markdown("""
            <div class='box-red'>
                <strong>Důležité zjednodušení:</strong> V první kapitole nejde o přesný výpočet účetnictví. Cílem je pochopit, že s.r.o. nebo a.s. není „bez daní“. Jen se peníze daní jinak než u OSVČ.
            </div>
            """, unsafe_allow_html=True)

            st.write("""
            **Co může platit například s.r.o.?**
            * **Daň z příjmů právnických osob (DPPO):** platí ji firma ze svého zisku; sazba je 21 %.
            * **Sociální a zdravotní pojištění za zaměstnance:** pokud firma zaměstnává lidi, odvádí za ně pojistné a část strhává ze mzdy.
            * **Daň ze mzdy:** pokud si zakladatel vyplácí mzdu jako zaměstnanec nebo jednatel, řeší se zdanění mzdy.
            * **Zdanění podílu na zisku:** pokud si společník vyplácí zisk, nejde o běžnou tržbu, ale o výplatu podílu na zisku.
            """)

            st.markdown("""
            <div class='box-blue'>
                <strong>Jednoduchý příklad:</strong> Malé s.r.o. vydělá za rok 500 000 Kč a náklady má 350 000 Kč. Zisk firmy je 150 000 Kč. Firma z tohoto zisku nejdříve řeší daň z příjmů právnických osob. Teprve potom může přemýšlet, co udělá se zbylými penězi — například je nechá ve firmě na rozvoj, nebo část vyplatí společníkům podle pravidel.
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            | Situace | Kdo platí | Co je pointa |
            | :--- | :--- | :--- |
            | **OSVČ vydělá peníze** | Podnikatel jako fyzická osoba | Řeší daň z příjmů, sociální a zdravotní pojištění. |
            | **s.r.o. vytvoří zisk** | Firma jako právnická osoba | Firma platí daň ze zisku (DPPO 21 %). |
            | **s.r.o. má zaměstnance** | Firma jako zaměstnavatel | Řeší mzdu, daň ze mzdy a odvody na sociální a zdravotní pojištění. |
            | **Společník si vyplatí zisk** | Společník / firma podle pravidel výplaty | Nejde o totéž jako tržba. Výplata zisku má vlastní daňová pravidla (srážková daň). |
            """)

            st.markdown("""
            <div class='box-yellow'>
                <strong>Praktické srovnání:</strong> OSVČ bývá jednodušší na start, ale ručí osobním majetkem. Společnost s ručením omezeným lépe odděluje firmu od osobního života, ale má složitější administrativu, účetnictví a pravidla pro daně.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 4.14 Srovnání OSVČ a s.r.o. pro tvůj projekt")
            st.markdown("""
            | Otázka | OSVČ | s.r.o. |
            | :--- | :--- | :--- |
            | **Jak rychle lze začít?** | Obvykle jednodušší a rychlejší. | Složitější založení, zápis a administrativa. |
            | **Ručení** | Podnikatel typicky ručí celým osobním majetkem. | Společník ručí omezeně podle nesplaceného vkladu; firma má vlastní majetek. |
            | **Důvěryhodnost pro větší partnery** | Může stačit pro menší služby. | Často působí vhodněji pro týmy, investory nebo větší zakázky. |
            | **Administrativa** | Jednodušší evidence podle situace. | Vyšší nároky, podvojné účetnictví, orgány, zápisy a rozhodování. |
            | **Vhodné pro** | Freelancing, malé služby, start jednotlivce. | Rostoucí projekt, tým, vyšší rizika, investice nebo potřeba oddělit majetek. |
            """)

        with st.container(border=True):
            st.markdown("### 4.15 Aktivita: Vyber právní formu podle situace")
            st.write("U každé situace rozhodni, která právní forma dává největší smysl na začátku. Své rozhodnutí zdůvodni podle ručení, administrativy, počtu osob, kapitálu a rizika.")

            s1 = st.selectbox("1. Student nabízí grafické služby třem lokálním firmám:", ["Vyber formu...", "OSVČ", "s.r.o.", "v.o.s.", "k.s.", "a.s.", "Družstvo"], key="act_s1")
            s2 = st.selectbox("2. Dva kamarádi chtějí dlouhodobě provozovat e-shop s vlastní značkou:", ["Vyber formu...", "OSVČ", "s.r.o.", "v.o.s.", "k.s.", "a.s.", "Družstvo"], key="act_s2")
            s3 = st.selectbox("3. Skupina pěti lidí chce společně sdílet vybavení a prodávat výrobky členů:", ["Vyber formu...", "OSVČ", "s.r.o.", "v.o.s.", "k.s.", "a.s.", "Družstvo"], key="act_s3")
            s4 = st.selectbox("4. Startup hledá investora a plánuje rychlý růst:", ["Vyber formu...", "OSVČ", "s.r.o.", "v.o.s.", "k.s.", "a.s.", "Družstvo"], key="act_s4")
            s5 = st.selectbox("5. Dva společníci chtějí podnikat společně, ale projekt může vytvářet vysoké dluhy:", ["Vyber formu...", "OSVČ", "s.r.o.", "v.o.s.", "k.s.", "a.s.", "Družstvo"], key="act_s5")
            s6 = st.selectbox("6. Tým studentů chce jednorázově prodávat výrobky na školní akci:", ["Vyber formu...", "OSVČ", "s.r.o.", "v.o.s.", "k.s.", "a.s.", "Družstvo"], key="act_s6")

            if st.button("Uložit vyhodnocení aktivity"):
                st.success("Vaše odpovědi byly uloženy!")

            st.markdown("""
            <div class='box-purple'>
                <strong>AI mentoring:</strong> Zkopíruj tento prompt do AI asistenta:<br>
                <i>„Porovnej pro můj projekt OSVČ, s.r.o., v.o.s., k.s., a.s. a družstvo. U každé formy napiš výhodu, riziko, zákonný znak a otázku, kterou si musím ověřit.“</i>
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 4.16 Jiné formy podnikání v ČR a v rámci EU")
            st.write("Vedle OSVČ a obchodních korporací existují i další způsoby, jak může podnikání fungovat. Některé jsou běžné v českém prostředí, jiné pomáhají podnikat napříč státy Evropské unie.")

            st.markdown("""
            <div class='box-blue'>
                <strong>Proč to znát:</strong> V praxi se podnikání nemusí vždy vejít jen do jednoduchého rozdělení OSVČ vs. s.r.o. Firma může mít pobočku, podnikatel může spolupracovat smluvně s dalšími osobami, nezisková organizace může vykonávat doplňkovou hospodářskou činnost a větší podniky mohou využívat evropské právní formy.
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            | Forma | Kde se používá | Jednoduché vysvětlení | Na co si dát pozor |
            | :--- | :--- | :--- | :--- |
            | **Odštěpný závod / pobočka** | ČR i zahraničí | Část podniku, která vystupuje navenek jako organizační jednotka. Zahraniční firma tak může podnikat v ČR bez založení nové české společnosti. | Nejde o samostatnou právnickou osobu jako s.r.o.; důležitý je zápis a odpovědnost mateřské firmy. |
            | **Tiché společenství** | ČR | Tichý společník poskytne podnikateli vklad a podílí se na výsledku podnikání, ale navenek obvykle nevystupuje. | Je to smluvní forma spolupráce, ne samostatná obchodní korporace. |
            | **Smluvní spolupráce více osob** | ČR | Více osob může spolupracovat na základě smlouvy, aniž by hned zakládaly novou firmu. | Je nutné jasně upravit odpovědnost, rozdělení nákladů, příjmů a vlastnictví výsledků práce. |
            | **Spolek, ústav, nadace** | ČR | Neziskové právnické osoby. Jejich hlavním účelem není podnikání, ale mohou mít doplňkovou hospodářskou činnost, pokud podporuje jejich hlavní smysl. | Zisk se obvykle nemá rozdělovat jako u obchodní společnosti; má sloužit k naplňování účelu organizace. |
            | **Státní podnik** | ČR | Podnik založený státem pro plnění veřejného nebo strategického zájmu. | Není běžnou volbou pro začínajícího podnikatele. |
            | **Evropská společnost (SE)** | EU | Akciová společnost evropského typu, která může usnadnit podnikání ve wait... států EU. | Hodí se spíše pro větší podniky; má vyšší nároky na kapitál, správu a přeshraniční fungování. |
            | **Evropské hospodářské zájmové sdružení (EHZS)** | EU | Forma spolupráce podnikatelů nebo firem z různých států EU. Pomáhá členům rozvíjet jejich činnost, například společný projekt, výzkum, nákup nebo obchod. | Smyslem není samostatně nahrazovat podnikání členů, ale podporovat jejich spolupráci. |
            | **Evropské družstvo (SCE)** | EU | Družstvo evropského typu, které umožňuje členům podnikat nebo spolupracovat přes hranice členských států. | Je vhodné hlavně pro přeshraniční družstevní projekty, ne pro běžný malý start. |
            """)

            st.markdown("""
            <div class='box-green'>
                <strong>Co si z toho odnést?</strong><br>
                • Pro běžný začátek podnikání v ČR se nejčastěji řeší OSVČ nebo s.r.o.<br>
                • Pokud podnikání roste do zahraničí, může být důležitá pobočka, odštěpný závod nebo evropská právní forma.<br>
                • Neziskové organizace mohou vykonávat hospodářskou činnost, ale jejich hlavní smysl je jiný než rozdělování zisku vlastníkům.<br>
                • V Evropské unii existují formy, které mají usnadnit přeshraniční podnikání a spolupráci.
            </div>
            """, unsafe_allow_html=True)

    # PODKAPITOLA 5
    elif selected_section == "5. Startup: nápad, který hledá byznys":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 5</div>", unsafe_allow_html=True)
        st.markdown("## 5. Startup: nápad, který hledá funkční byznys")
        
        with st.container(border=True):
            st.write("""
            Startup je mladý podnikatelský projekt, který hledá opakovatelný a škálovatelný způsob, jak řešit problém zákazníka. Nejde jen o „malou firmu“. Startup často začíná nejistotou: tým má nápad, ale ještě neví, zda o něj zákazníci opravdu stojí, kolik za něj zaplatí a jak rychle může růst.
            """)
            st.markdown("""
            <div class='box-blue'>
                <strong>Proč je to důležité:</strong> Startupové téma rozvíjí podnikavost, kreativitu, práci s informacemi, digitální kompetence, týmovou spolupráci, finanční uvažování, komunikaci se zákazníkem a schopnost ověřovat nápady před investicí peněz.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 5.1 Startup pro současnou generaci")
            st.write("""
            **💡 Co je to vlastně podnikavost?**<br>
            Je to schopnost vidět příležitosti tam, kde ostatní vidí problémy, a mít odvahu realizovat nápady.

            **🎲 Pilíř 1: Přijímání kalkulovaného rizika**<br>
            Podnikatel nehazarduje, ale spočítá si, co nejhoršího se může stát a zda to zvládne.

            **🔄 Pilíř 2: Odolnost vůči nezdaru (Resilience)**<br>
            Pravidlo „Fail fast, learn faster“. Chyba není ostuda, ale lekce pro další pokus.
            """, unsafe_allow_html=True)

            c_st1, c_sim2 = st.columns(2)
            with c_st1:
                st.markdown("""
                <div class='box-gray'>
                    <strong>🏛️ Tradiční firma (Pekařství na rohu)</strong><br><br>
                    • <strong>Cíl:</strong> Stabilita a stálý zisk. Udržet si zákazníky a vydělávat pravidelně na nájem, mzdy a suroviny.<br>
                    • <strong>Riziko:</strong> Malé až střední. Pracuje s ověřeným modelem (pečivo lidé znají).<br>
                    • <strong>Trh:</strong> Místní sousedství. Úspěch závisí na poloze a stálé komunitě.
                </div>
                """, unsafe_allow_html=True)
            with c_sim2:
                st.markdown("""
                <div class='box-gray'>
                    <strong>🚀 Startup (Aplikace na sdílení kol)</strong><br><br>
                    • <strong>Cíl:</strong> Obrovský a rychlý růst do celého světa. Hledá model, který se dá rychle opakovat ve více městech.<br>
                    • <strong>Riziko:</strong> Extrémně vysoké (buď uspěje, nebo zanikne). Pracuje s obrovskou nejistotou.<br>
                    • <strong>Trh:</strong> Celá planeta. Řeší problém, který se týká mnoha lidí na různých místech.
                </div>
                """, unsafe_allow_html=True)

            st.markdown("#### 🎯 SIMULACE: Máš nápad na novou aplikaci. Co uděláš jako první?")
            sim_choice = st.radio("Vyber odpověď:", ["A) Utratím 200 000 Kč za vývoj plné verze", "B) Udělám jednoduchý dotazník a jednoduchý web pro zájemce"], key="p5_sim_app")
            
            if st.button("Vyhodnotit simulaci"):
                if "A)" in sim_choice:
                    st.markdown("<div class='box-red'>❌ <strong>CHYBA!</strong> Utratil jsi peníze a zbytečně postavil něco, co lidé nechtějí. Chybělo ti otestování nápadu.</div>", unsafe_allow_html=True)
                else:
                    st.markdown("<div class='box-green'>🎉 <strong>SKVĚLE!</strong> Získal jsi zdarma 500 zájemců a ověřil trh. Můžeš bezpečně stavět MVP!</div>", unsafe_allow_html=True)

            st.markdown("#### ❓ Dvě otázky pro představivost")
            
            with st.expander("❓ Otázka 1: Proč většina startupů selže v prvním roce? (Klikni pro zobrazení odpovědi)"):
                st.markdown("<div class='box-blue'><strong>Odpověď:</strong> Vyrobí produkt, který ve skutečnosti nikdo nepotřebuje (neověří si poptávku).</div>", unsafe_allow_html=True)
                
            with st.expander("❓ Otázka 2: Co znamená zkratka MVP? (Klikni pro zobrazení odpovědi)"):
                st.markdown("<div class='box-blue'><strong>Odpověď:</strong> Minimum Viable Product – nejjednodušší verze produktu, která už funguje a dá se testovat na lidech.</div>", unsafe_allow_html=True)

            st.write("""
            Startupová kultura je blízká dnešní generaci, protože spojuje technologie, sociální sítě, AI, komunitu, rychlé testování a možnost tvořit i s malým rozpočtem. Zároveň ale svádí k iluzi, že stačí dobrý nápad, virální video nebo hezká aplikace.

            **Ve skutečnosti startup stojí na ověřování:**
            * Existuje skutečný problém?
            * Koho problém bolí natolik, že za řešení zaplatí?
            * Umíme zákazníka oslovit?
            * Vyjdou ekonomicky náklady a příjmy?
            * Umíme růst bez toho, aby se zhroutila kvalita, tým nebo cashflow?
            """)

            st.markdown("""
            <div class='box-red'>
                <strong>⚠️ Častý omyl:</strong> „Mám nápad na aplikaci“ ještě neznamená startup. Startup vzniká až tehdy, když existuje problém, zákazník, test, zpětná vazba a možnost opakovaně vytvářet hodnotu.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 5.2 Startupová hypotéza")
            st.write("Každý startup začíná předpoklady. Ty je potřeba převést na hypotézy, které se dají ověřit.")

            st.markdown("""
            | Nejasný předpoklad | Lepší hypotéza | Jak ji ověřit |
            | :--- | :--- | :--- |
            | **Lidem se náš nápad bude líbit.** | Alespoň 15 studentů z 30 řekne, že by službu použilo každý týden. | Krátký rozhovor nebo dotazník. |
            | **Zákazníci budou platit.** | Alespoň 5 lidí si předobjedná produkt za 99 Kč. | Předobjednávkový formulář. |
            | **Marketing na TikToku bude fungovat.** | Video získá 1 000 zhlédnutí a 20 kliknutí na formulář. | Testovací příspěvek a měření odkazu. |
            | **Výroba nebude drahá.** | Variabilní náklad na kus nepřekročí 60 % prodejní ceny. | Kalkulace dodavatelů a test malého množství. |
            """)

        with st.container(border=True):
            st.markdown("### 5.3 AI-first, ale odpovědně")
            st.write("AI může startupu pomoci s rešerší trhu, návrhem textů, zákaznickými personami, analýzou zpětné vazby, automatizací podpory nebo tvorbou prototypu. Současně ale přináší rizika:")

            st.markdown("""
            * neověřené informace,
            * generický obsah bez odlišení,
            * porušení autorských práv,
            * práce s osobními údaji,
            * falešný pocit, že AI nahradí kontakt se zákazníkem.
            """)

            st.markdown("""
            <div class='box-purple'>
                <strong>🤖 AI prompt pro startup:</strong> Zkopíruj tento prompt do asistenta:<br>
                <i>„Pomoz mi z mého nápadu vytvořit 5 ověřitelných hypotéz. U každé navrhni nejlevnější test, metriku úspěchu a riziko, že si výsledek špatně vyložím.“</i>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("#### 🚀 Aktivita: Startup za 30 minut")
            st.write("Ve skupině vyberte jeden problém ze školy nebo běžného života:")

            c_a1, c_a2 = st.columns(2)
            with c_a1:
                st.text_input("1. Popište problém jednou větou:", placeholder="Problém...", key="p5_p_desc")
                st.text_input("2. Určete konkrétního zákazníka:", placeholder="Zákazník...", key="p5_p_cust")
                st.text_input("3. Navrhněte nejjednodušší řešení:", placeholder="Řešení...", key="p5_p_sol")
            with c_a2:
                st.text_input("4. Sepište jednu hypotézu:", placeholder="Hypotéza...", key="p5_p_hyp")
                st.text_input("5. Navrhněte test bez velkých nákladů:", placeholder="Test...", key="p5_p_test")
                st.text_input("6. Metrika úspěchu (podle čeho poznáte zájem?):", placeholder="Metrika...", key="p5_p_met")

            if st.button("Uložit výstup aktivity Startup za 30 min"):
                st.success("Aktualizováno!")

            st.text_input("🧩 Interaktivní výzva: Vymysli jeden problém, který lidé kolem tebe řeší, a napiš, jaké jednoduché řešení by mohlo vzniknout jako startup:", placeholder="Problém + řešení...", key="p5_user_prob")

            st.markdown("""
            <div class='box-purple'>
                <strong>🤖 AI mentoring:</strong> Zkopíruj tento prompt do AI asistenta:<br>
                <i>„Pomoz mi převést můj nápad na startupovou hypotézu: problém, zákazník, řešení, cena a první test.“</i>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class='box-blue'>
                <strong>Jednoduše řečeno:</strong> Startup není hotová firma. Je to pokus najít funkční podnikatelský model, který se dá rychle ověřovat, upravovat a případně zvětšovat.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 5.4 Jak startup vzniká")
            st.write("""
            Startup obvykle nevzniká tak, že někdo rovnou napíše dokonalý podnikatelský plán. Častější cesta je postupné ověřování. Tým nejdřív pracuje s nejistotou: má domněnky o zákazníkovi, problému, řešení, ceně a způsobu prodeje. Teprve když získá důkazy, rozhoduje, jestli pokračovat, upravit směr, nebo projekt ukončit.
            """)

            st.text_input("🧩 Interaktivní výzva: Vyber jeden krok z následujícího postupu a napiš, co bys v něm konkrétně udělal/a u vlastního nápadu:", placeholder="Vybraný krok + akce...", key="p5_step_action")

            st.markdown("""
            1. **Problém:** někdo si všimne potřeby, nespokojenosti nebo neefektivního řešení.
            2. **Zákazník:** tým určí, komu chce pomoci.
            3. **Návrh řešení:** vznikne první jednoduchá verze produktu nebo služby.
            4. **Ověření:** tým mluví se zákazníky, sbírá zpětnou vazbu a testuje zájem.
            5. **Úprava nápadu:** pokud test nevyjde, startup změní řešení, zákazníka, cenu, kanál nebo rozsah.
            6. **Růst:** když se ukáže, že zákazníci mají zájem, startup hledá způsob, jak růst opakovatelně a finančně udržitelně.
            """)

            st.markdown("""
            <div class='box-gray'>
                <strong>Příklad vzniku startupu:</strong> Studenti zjistí, že jejich spolužáci často nestíhají plánovat učení. Nevytvoří hned velkou aplikaci, ale nejdřív sdílenou Notion šablonu nebo jednoduchou tabulku. Tu vyzkouší ve třídě, sledují, kdo ji skutečně používá, co studentům chybí a zda by za rozšířenou verzi zaplatili. Pokud ji lidé používají a doporučují dál, tým může řešit cenu, marketing a další rozvoj.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 5.5 Metodika Lean Startup")
            st.write("""
            Metodika Lean Startup pomáhá začínajícím týmům netrávit měsíce tvorbou produktu, o který nakonec nikdo nestojí. Její základní myšlenka je jednoduchá: **nejdřív ověř nejrizikovější předpoklad, potom investuj víc času a peněz**.

            Lean Startup vychází z toho, že startup není zmenšená verze velké firmy. Velká firma často ví, kdo je její zákazník, jaký produkt prodává a jak vydělává. Startup to teprve hledá. Proto potřebuje rychlé učení, malé experimenty a ochotu měnit plán podle dat.
            """)

            st.markdown("""
            <div class='box-blue'>
                <strong>Jednoduše řečeno:</strong> Lean Startup je způsob práce, při kterém tým rychle vytvoří malý test, získá zpětnou vazbu, změří výsledky a podle nich se rozhodne, co dál.
            </div>
            """, unsafe_allow_html=True)

            st.markdown("#### Základní cyklus: Vytvoř — Změř — Pouč se (Build — Measure — Learn)")

            st.markdown("""
            | Krok | Co tým dělá | Příklad ve školním startupu | Častá chyba |
            | :--- | :--- | :--- | :--- |
            | **Vytvoř** | Tým připraví nejmenší verzi testu nebo prototypu. | Místo celé aplikace vytvoří klikací návrh, formulář, šablonu nebo testovací stánek. | Tým chce hned dokonalý produkt a ztratí týdny přípravou. |
            | **Změř** | Tým sbírá data, ne pouze dojmy. | Sleduje počet registrací, předobjednávek, rozhovorů, opakovaných použití nebo skutečných plateb. | Tým se spokojí s větou „lidem se to líbilo“. |
            | **Pouč se** | Tým vyhodnotí, co data znamenají, a rozhodne další krok. | Pokračuje, upraví zákazníka, změní cenu, zjednoduší řešení nebo projekt ukončí. | Tým ignoruje negativní výsledky, protože se do nápadu zamiloval. |
            """)

            st.markdown("""
            <div class='box-yellow'>
                <strong>🧪 Pravidlo Lean Startup:</strong> Neověřuj všechno najednou. Nejdřív testuj předpoklad, který může projekt nejrychleji zbořit — například zda problém opravdu existuje, zda zákazník zaplatí nebo zda řešení umíte dodat za rozumné náklady.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 5.6 MVP: minimální životaschopný produkt")
            st.write("""
            MVP znamená **minimum viable product**, česky minimální životaschopný produkt. Nejde o nejlevnější ani nejodbytější verzi. Jde o nejmenší verzi, která dokáže ověřit důležitou otázku.

            **MVP má odpovědět například:**
            * Chce zákazník tento problém řešit?
            * Rozumí hodnotě řešení?
            * Je ochoten udělat akci — zapsat se, objednat, zaplatit, přijít, doporučit?
            * Funguje navržený kanál komunikace?
            * Umí tým řešení dodat v přijatelné kvalitě?
            * Vycházejí náklady a čas?
            """)

            st.markdown("""
            | Nápad | Špatný první krok | Lean Startup MVP | Co ověřujeme |
            | :--- | :--- | :--- | :--- |
            | **Aplikace na plánování učení** | Programovat kompletní aplikaci s účty a notifikacemi. | Notion šablona nebo Google tabulka pro 20 studentů. | Zda studenti plánovač reálně používají. |
            | **E-shop se studentským merchem** | Nakoupit sklad a spustit celý e-shop. | Předobjednávka tří návrhů přes formulář. | Zda lidé zaplatí za konkrétní motiv a cenu. |
            | **ReStart Batoh** | Sbírat desítky batohů bez ověření zájmu. | Testovací série 5–10 kusů s jasným popisem stavu. | Zda lidé koupí použitý upravený batoh. |
            | **Doučovací služba** | Budovat platformu pro všechny předměty. | Ručně propojit 5 dvojic studentů a měřit spokojenost. | Zda je problém dost silný a zda funguje párování. |
            """)

            st.markdown("""
            <div class='box-red'>
                <strong>Pozor:</strong> MVP není výmluva pro nekvalitu. I malý test musí být bezpečný, férový a srozumitelný. Pokud prodáváme produkt, zákazník musí vědět, co přesně dostane.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 5.7 Validované učení")
            st.write("Cílem Lean Startup není jen „něco zkusit“. Cílem je validované učení — tedy ověřené poznání, které pomůže rozhodnout. Tým musí umět říct: *„Mysleli jsme si X, otestovali jsme Y, výsledek byl Z, proto uděláme další krok.“*")

            st.markdown("""
            | Slabé vyhodnocení | Validované učení |
            | :--- | :--- |
            | **„Dotazník dopadl dobře.“** | „Z 60 respondentů 42 uvedlo, že problém řeší alespoň jednou týdně, ale pouze 6 by bylo ochotno zaplatit více než 100 Kč. Musíme upravit cenu nebo hodnotu nabídky.“ |
            | **„Příspěvek měl hodně lajků.“** | „Příspěvek měl 180 lajků, ale jen 4 kliknutí na objednávkový formulář. Lajky tedy nejsou důkaz nákupního zájmu.“ |
            | **„Lidem se batohy líbily.“** | „Z 12 testovacích batohů se prodalo 9 během dvou dnů, 3 zákazníci žádali nižší cenu a 1 reklamoval zip. Další série potřebuje lepší kontrolu zipů.“ |
            """)

            st.markdown("""
            <div class='box-gray'>
                <strong>Věta pro vyhodnocení experimentu:</strong><br>
                Předpokládali jsme, že…<br>
                Ověřili jsme to pomocí…<br>
                Naměřili jsme…<br>
                Zjistili jsme…<br>
                Proto teď rozhodujeme, že…
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 5.8 Pivot, pokračování nebo ukončení")
            st.write("Po testu má startup tři základní možnosti:")

            st.markdown("""
            | Rozhodnutí | Kdy dává smysl | Příklad |
            | :--- | :--- | :--- |
            | **Pokračovat** | Test ukázal jasný zájem a ekonomika dává smysl. | Předobjednávky pokryly náklady a zákazníci doporučují produkt dál. |
            | **Pivotovat** | Problém existuje, ale řešení, zákazník, cena nebo kanál nefunguje. | Studenti nechtějí aplikaci, ale chtějí hotovou šablonu a krátké připomínky. |
            | **Ukončit** | Test opakovaně ukazuje slabý zájem nebo neudržitelnou ekonomiku. | Zákazníci nápad chválí, ale nikdo se nezapíše, nezaplatí ani nepoužije prototyp. |
            """)

            st.write("""
            **Pivot neznamená selhání.** Znamená změnu směru na základě učení. Tým může změnit:
            cílového zákazníka, problém, řešení, cenu, distribuční kanál, způsob monetizace nebo rozsah produktu.
            """)

            st.markdown("""
            <div class='box-blue'>
                <strong>🧭 Podnikatelská zralost:</strong> Dobrý tým neobhajuje nápad za každou cenu. Dobrý tým chrání čas, peníze a energii tím, že se umí rozhodnout podle důkazů.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 5.9 Lean Startup v mini projektu SŠ")
            st.write("""
            Pro školní projekt stačí Lean Startup použít v jednoduché podobě. Nemusíš znát odborné termíny nazpaměť, důležité je umět pracovat v tomto sledu:
            1. **Najdi problém:** Co někomu vadí, chybí nebo zdržuje?
            2. **Urči zákazníka:** Komu se to děje nejčastěji?
            3. **Zapiš hypotézu:** Co si myslíme, že bude pravda?
            4. **Navrhni MVP:** Jak to ověříme co nejmenším testem?
            5. **Změř výsledek:** Jaké číslo nebo důkaz rozhodne?
            6. **Vyhodnoť:** Co jsme se naučili?
            7. **Rozhodni:** pokračovat, pivotovat, nebo ukončit.
            """)

            st.markdown("""
            | Krok | Výstup studenta | Kontrolní otázka učitele |
            | :--- | :--- | :--- |
            | **Problém** | Jedna konkrétní věta o problému. | Je to problém zákazníka, nebo jen nápad týmu? |
            | **Zákazník** | Konkrétní skupina a situace. | Není skupina příliš široká? |
            | **Hypotéza** | Věta „Věříme, že…“ s měřitelným výsledkem. | Dá se hypotéza vyvrátit? |
            | **MVP** | Malý test bez zbytečných nákladů. | Je test dostatečný k učení, ale bezpečný a férový? |
            | **Metrika** | Číslo nebo pozorování, podle kterého rozhodneme. | Měříme skutečný zájem, nebo jen popularitu? |
            | **Vyhodnocení** | Krátký závěr: co data znamenají. | Je rozhodnutí opřené o důkaz? |
            """)

            st.markdown("""
            <div class='box-yellow'>
                <strong>🧩 Aktivita: Lean Startup sprint na 45 minut</strong><br>
                • Popiš problém jednou větou.<br>
                • Urči konkrétního zákazníka.<br>
                • Napiš jednu rizikovou hypotézu.<br>
                • Navrhni MVP test, který zvládneš bez velkých nákladů.<br>
                • Urči metriku úspěchu.<br>
                • Napiš, co uděláš, když test vyjde, a co uděláš, když nevyjde.
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class='box-purple'>
                <strong>🤖 AI mentoring:</strong> Zkopíruj tento prompt do AI asistenta:<br>
                <i>„Použij metodiku Lean Startup na můj nápad. Pomoz mi určit nejrizikovější hypotézu, navrhni MVP test, metriku úspěchu, možné výsledky a rozhodnutí: pokračovat, pivotovat nebo ukončit.“</i>
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 5.10 Kam jít s novým nápadem & 5.11 Podpora startupů")
            st.write("Začínající tým nemusí být na všechno sám. V ČR existuje startupový ekosystém — síť organizací, mentorů, investorů, soutěží, inkubátorů, akcelerátorů a coworkingových center.")

            st.markdown("""
            | Kam se obrátit | Co může pomoci získat |
            | :--- | :--- |
            | **Inkubátor** | Pomoc v úplném začátku, mentoring, prostor, kontakty. |
            | **Akcelerátor** | Intenzivní program pro rychlejší rozvoj nápadu, často zakončený prezentací investorům. |
            | **Coworkingové centrum** | Místo pro práci, networking a setkávání s dalšími podnikavými lidmi. |
            | **Startupová soutěž / hackathon** | Rychlé ověření nápadu, zpětnou vazbu, kontakty a někdy i cenu nebo podporu. |
            | **Investor / business angel** | Kapitál, zkušenosti a kontakty výměnou za podíl nebo jinou formu dohody. |
            | **Univerzita / inovační centrum** | Odborníky, laboratoře, mentoring a propojení s výzkumem. |
            """)

            st.markdown("""
            <div class='box-gray'>
                <strong>Příklady podpory v ČR:</strong> CzechInvest a portál CzechStartups.gov.cz, regionální inovační centra jako JIC v Brně, startupové akcelerátory jako StartupYard, univerzitní inkubátory, podnikatelské soutěže, coworkingová centra a místní podnikatelská centra.
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class='box-green'>
                <strong>💡 Proč stát a regiony startupy podporují:</strong> Startupy přinášejí nové produkty, pracovní místa, inovace a vyšší konkurenceschopnost ekonomiky. Podpora není „dárek zdarma“, ale investice do budoucích firem.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 5.12 Moderní startupové pilíře")
            st.markdown("""
            <div class='box-blue'>
                <strong>Proč se učíme o startupech?</strong> Tradiční formy podnikání dnes doplňuje dynamický svět technologických startupů. Pochopení jejich pilířů — škálovatelnosti, inovací, práce s daty, rizikového kapitálu a rychlého ověřování nápadů — pomáhá studentům pochopit moderní digitální ekonomiku a proměny trhu práce.<br><br>
                <strong>Moderní startupové pilíře:</strong> AI-First, Solopreneurship, Build in Public a Founder Wellbeing pomáhají přemýšlet o tom, jak bude projekt fungovat v praxi — nejen co prodává, ale také jak se tvoří, komunikuje a dlouhodobě zvládá.
            </div>
            """, unsafe_allow_html=True)

            st.markdown("🧩 **Interaktivní výzva: Vyplň plán pro svůj startup u jednotlivých pilířů:**")

            col_p1, col_p2 = st.columns(2)
            with col_p1:
                st.text_area("1. AI-First (Jak tvůj projekt využívá AI? Např. analýza zákazníků, podpora):", placeholder="Využití AI...", height=80, key="pil_ai")
                st.text_area("2. Solopreneurship (Jaké automatizace ti ušetří čas? Např. plánování příspěvků, fakturace):", placeholder="Automatizace...", height=80, key="pil_solo")
            with col_p2:
                st.text_area("3. Build in Public (Co budeš sdílet na sítích a komu tím chceš pomoci?):", placeholder="Plán sdílení...", height=80, key="p_bip")
                st.text_area("4. Founder Wellbeing (Jaké máš rituály pro psychohygienu a jak poznáš, že je toho moc?):", placeholder="Psychohygiena...", height=80, key="pil_well")

            if st.button("Uložit plán 4 pilířů"):
                st.success("Plán startupových pilířů uložen!")

            st.markdown("""
            <div class='box-yellow'>
                <strong>Doplň: Je dobré si pamatovat:</strong><br>
                • Startup začíná hypotézou, ne jistotou.<br>
                • Nejdřív se ověřuje problém a zákazník, potom se řeší velké investice.<br>
                • Podpora může mít podobu rad, kontaktů, prostoru, soutěže, programu nebo financování.<br>
                • I neúspěšný test má hodnotu, protože šetří čas a peníze.
            </div>
            """, unsafe_allow_html=True)

    # PODKAPITOLA 6 - PODNIKATELSKÝ ZÁMĚR
    elif selected_section == "6. Podnikatelský záměr":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 6</div>", unsafe_allow_html=True)
        st.markdown("## 6. Podnikatelský záměr")
        
        with st.container(border=True):
            st.write("""
            Podnikatelský záměr je dokument nebo pracovní plán, který pomáhá ověřit, zda má nápad šanci fungovat. Není to slohová práce ani „povinný papír do šuplíku“. Je to mapa rozhodování: ukazuje, komu projekt pomáhá, jakou hodnotu nabízí, kolik bude stát, jak bude vydělávat, jaká má rizika a podle čeho poznáme, že má smysl pokračovat.
            """)
            st.markdown("""
            <div class='box-blue'>
                <strong>Proč je to důležité:</strong> Podnikatelský záměr pomáhá převést nápad do praktického návrhu, posoudit rizika, spočítat náklady a ověřit, jestli má projekt šanci fungovat. Nejde o opis definice, ale o plán pro konkrétní situaci.
            </div>
            """, unsafe_allow_html=True)

            st.text_input("🧩 Interaktivní výzva: Napiš svůj podnikatelský nápad ve formátu:", placeholder="Pomáhám komu, s čím, pomocí čeho a proč by za to měl někdo zaplatit...", key="p6_idea_format")

            st.markdown("""
            <div class='box-purple'>
                <strong>🤖 AI mentoring:</strong> Zkopíruj tento prompt do AI asistenta:<br>
                <i>„Zkontroluj můj podnikatelský záměr. Najdi nejasného zákazníka, slabé místo v ceně, podceněné náklady, právní riziko a jednu otázku, kterou musím ověřit rozhovorem se zákazníkem.“</i>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class='box-green'>
                <strong>Shrnutí:</strong> Podnikatelský záměr pomáhá převést nápad do konkrétních rozhodnutí. Dobrý záměr neříká jen „co chceme dělat“, ale také pro koho, proč, za kolik, s jakými náklady, s jakým rizikem a jak ověříme zájem.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 6.1 Proč podnikatelský záměr vzniká")
            st.write("""
            Podnikatel často začíná nadšením: má nápad, vidí příležitost a chce rychle začít. Podnikatelský záměr ale nutí tým zpomalit a položit si otázky, které mohou ušetřit čas, peníze i zklamání.

            **Záměr pomáhá:**
            * ujasnit problém a zákazníka,
            * oddělit přání od ověřených informací,
            * zjistit, zda cena pokryje náklady,
            * připravit první test trhu,
            * domluvit role v týmu,
            * odhalit právní, finanční a etická rizika,
            * vysvětlit projekt učiteli, mentorovi, investorovi, bance nebo spolužákům.
            """)

            st.markdown("""
            | Špatný záměr | Lepší záměr |
            | :--- | :--- |
            | **„Budeme prodávat moderní doplňky pro mladé.“** | „Budeme testovat prodej reflexních přívěsků na batohy pro žáky 1. ročníku, kteří chodí domů za šera a chtějí levný doplněk do 80 Kč.“ |
            | **„Cena bude nízká, aby to lidé kupovali.“** | „Cena bude 79 Kč, protože variabilní náklad je 38 Kč, potřebujeme rezervu na neprodané kusy a v dotazníku byla nejčastější ochota platit 60–90 Kč.“ |
            | **„Budeme ekologičtí.“** | „Použijeme recyklovatelný obal, budeme evidovat množství odpadu a nebudeme používat tvrzení, která neumíme doložit.“ |
            """)

        with st.container(border=True):
            st.markdown("### 6.2 Co by měl podnikatelský záměr obsahovat")
            
            st.markdown("""
            | Část záměru | Kontrolní otázka | Co má být výstupem |
            | :--- | :--- | :--- |
            | **Vize a nápad** | Co chceme vytvořit a proč? | Jedna srozumitelná věta bez marketingových frází. |
            | **Zákazník** | Komu přesně pomáháme? | Konkrétní skupina, situace a potřeba. |
            | **Problém** | Jakou nepříjemnost, potřebu nebo překážku zákazník řeší? | Popis problému z pohledu zákazníka. |
            | **Hodnota** | Co zákazník získá? | Úspora času, peněz, jistota, pohodlí, bezpečí, styl, zážitek nebo jiný přínos. |
            | **Konkurence** | Jak zákazník řeší problém dnes? | 3 alternativy a vysvětlení, čím se lišíme. |
            | **Cena** | Kolik je zákazník ochoten zaplatit a proč? | Návrh ceny opřený o náklady, hodnotu, konkurenci a test. |
            | **Náklady** | Co bude stát start a provoz? | Jednorázové, fixní a variabilní náklady plus rezerva. |
            | **Marketing** | Jak se zákazník o nabídce dozví? | Kanály, sdělení, ukázka příspěvku nebo pitch. |
            | **Právní forma** | Je to jednorázový projekt, OSVČ, nebo firma? | Zdůvodnění podle soustavnosti, rizika a odpovědnosti. |
            | **Rizika** | Co se může pokazit? | Riziková matice a preventivní opatření. |
            | **První test** | Jak ověříme zájem levně a rychle? | Rozhovor, dotazník, prototyp, předobjednávka nebo zkušební prodej. |
            """)

        with st.container(border=True):
            st.markdown("### 6.3 Analýza trhu")
            st.write("""
            Než podnikatel začne vyrábět nebo prodávat, musí zjistit, jestli o jeho nabídku někdo stojí. Analýza trhu neznamená jen „vygooglit konkurenci“. Znamená pochopit zákazníka, jeho současné chování a alternativy, ze kterých si vybírá.
            """)

            st.text_input("🧩 Interaktivní výzva k analýze trhu: Najdi tři podobné firmy nebo alternativní řešení pro tvůj projekt:", placeholder="1. Alternativa, 2. Alternativa, 3. Alternativa...", key="p6_mkt_anal")

            st.markdown("#### Zákazník není „všichni“")
            st.write("""
            Častá chyba začínajících projektů je tvrzení: *„Naším zákazníkem jsou všichni studenti.“* Jenže prvák, maturant, student odborného výcviku, rodič a učitel mají jiné potřeby, rozpočet i motivaci.

            **Lepší popis zákazníka:**
            * konkrétní skupina,
            * konkrétní situace,
            * konkrétní problém,
            * konkrétní důvod, proč by změnila chování.

            *Příklad:* „Studenti prvního ročníku, kteří dojíždějí a potřebují levné, skladné a rychle dostupné svačiny mezi výukou a odpolední praxí.“
            """)

            st.markdown("#### Konkurence není jen stejný produkt")
            st.write("""
            Konkurencí je každé řešení, které zákazník používá místo nás. Pokud prodáváme svačinový box, konkurencí není jen jiný box. Konkurencí je školní bufet, obchod cestou do školy, jídlo z domova, automat, rozvoz nebo rozhodnutí nejíst vůbec.
            """)

            st.markdown("""
            | Co zkoumáme | Otázky | Příklad výstupu |
            | :--- | :--- | :--- |
            | **Zákazník** | Kdo má problém a kdy ho řeší? | Studenti dojíždějící do školy mají málo času mezi výukou a praxí. |
            | **Současné řešení** | Jak to řeší dnes? | Kupují si dražší jídlo cestou, nosí svačinu z domova nebo nejí. |
            | **Konkurence** | Kdo nebo co může nahradit náš produkt? | Bufet, supermarket, automat, donáška, domácí příprava. |
            | **Odlišení** | Proč by zákazník zvolil nás? | Rychlé vyzvednutí ve škole, jasná cena, možnost předobjednávky. |
            """)

        with st.container(border=True):
            st.markdown("### 6.4 Zakladatelský rozpočet & Kalkulačka bodu zvratu")
            st.write("""
            Zakladatelský rozpočet odpovídá na otázku: **Kolik peněz potřebuji na start a kolik mě bude stát provoz?** Nestačí započítat jen materiál. Podnikatel musí myslet i na čas, propagaci, obaly, software, dopravu, rezervu a neprodané kusy.
            """)

            st.markdown("""
            | Typ nákladu | Co znamená | Příklad |
            | :--- | :--- | :--- |
            | **Jednorázové náklady** | Platí se při startu projektu. | První materiál, jednoduchý web, vybavení, registrace, grafika. |
            | **Fixní náklady** | Platí se pravidelně bez ohledu na počet prodejů. | Nájem, software, účetnictví, paušální služby, doména. |
            | **Variabilní náklady** | Rostou s každým kusem nebo zakázkou. | Materiál, obal, doprava, platební poplatek, provize. |
            | **Rezerva** | Peníze na chyby, zpoždění a nečekané situace. | Reklamace, zmetky, zdražení materiálu, neprodané kusy. |
            | **Čas práce** | Práce týmu má hodnotu, i když si ji hned nevyplácí. | Příprava, komunikace, balení, focení, sociální sítě, evidence. |
            """)

            st.markdown("#### 🧮 Interaktivní kalkulačka bodu zvratu (Break-even point)")
            st.write("Zadej své hodnoty a zjisti, kolik kusů musíš prodat, abys nebyl/a ve ztrátě:")

            col_be1, col_be2, col_be3 = st.columns(3)
            with col_be1:
                price_per_unit = st.number_input("Prodejní cena za 1 ks (Kč):", value=150, step=10, key="be_price")
            with col_be2:
                var_cost_per_unit = st.number_input("Variabilní náklad na 1 ks (Kč):", value=80, step=5, key="be_var")
            with col_be3:
                fixed_costs_total = st.number_input("Měsíční fixní náklady (Kč):", value=2800, step=100, key="be_fix")

            margin_per_unit = price_per_unit - var_cost_per_unit

            if margin_per_unit <= 0:
                st.error("⚠️ Prodejní cena musí být vyšší než variabilní náklady na 1 kus!")
            else:
                break_even_units = fixed_costs_total / margin_per_unit
                st.markdown(f"""
                <div class='box-green'>
                    <strong>Marže na 1 kus:</strong> {margin_per_unit} Kč<br>
                    <strong>Bod zvratu:</strong> Musíš prodat minimálně <span style='font-size: 1.2rem; font-weight: 800;'>{break_even_units:.1f} kusů</span> (tj. cca <strong>{int(break_even_units if break_even_units == int(break_even_units) else break_even_units + 1)} ks</strong>) měsíčně pro pokrytí fixních nákladů!
                </div>
                """, unsafe_allow_html=True)

                # Dynamický graf bodu zvratu
                units_range = list(range(0, int(break_even_units * 2) + 10, max(1, int(break_even_units / 5))))
                revenues = [u * price_per_unit for u in units_range]
                total_costs = [fixed_costs_total + (u * var_cost_per_unit) for u in units_range]

                chart_data = {
                    "Kusy": units_range,
                    "Celkové příjmy (Kč)": revenues,
                    "Celkové náklady (Kč)": total_costs
                }
                st.line_chart(chart_data, x="Kusy")

        with st.container(border=True):
            st.markdown("### 6.5 Marketing a prodej v podnikatelském záměru")
            st.write("""
            Marketing není jen reklama. V podnikatelském záměru má ukázat, jak se zákazník dozví o nabídce, proč jí porozumí a proč jí bude důvěřovat.

            **Dobrý marketingový plán odpovídá:**
            * kde zákazník tráví pozornost,
            * jakým jazykem mu vysvětlíme hodnotu,
            * jak ukážeme důkaz kvality,
            * jak zabráníme přehnaným slibům,
            * jak budeme měřit, zda marketing funguje.
            """)

            st.markdown("""
            | Kanál | Kdy dává smysl | Riziko | Metrika |
            | :--- | :--- | :--- | :--- |
            | **Školní Instagram** | Studentský projekt pro školní komunitu. | Lajky nemusí znamenat nákup. | Kliknutí na formulář, rezervace, předobjednávky. |
            | **Plakát ve škole** | Lokální prodej nebo akce. | Studenti si nemusí zapamatovat detail. | QR skeny, návštěvy stánku. |
            | **Osobní doporučení** | Malá komunita, důvěra, první zákazníci. | Pomalejší šíření. | Počet doporučení a opakovaných nákupů. |
            | **Krátké video (TikTok/Reels)** | Produkt jde dobře ukázat vizuálně. | Přehnaný slib nebo povrchní viralita. | Zprávy, poptávky, objednávky. |
            """)

        with st.container(border=True):
            st.markdown("### 6.6 Rizika a plán B")
            st.write("Podnikatelský záměr má obsahovat i nepříjemné otázky. Silný tým nepůsobí slabě tím, že mluví o rizicích. Naopak ukazuje, že přemýšlí realisticky.")

            st.markdown("""
            | Riziko | Jak se projeví | Prevence | Plán B |
            | :--- | :--- | :--- | :--- |
            | **Nízký zájem** | Málo objednávek, nízká účast, slabá zpětná vazba. | Rozhovory, předobjednávka, test malého množství. | Změnit cílovou skupinu, cenu nebo problém. |
            | **Podceněné náklady** | Projekt prodává, ale nevydělává. | Kalkulace, rezerva, kontrola dodavatelů. | Zdražit, zjednodušit produkt, snížit rozsah. |
            | **Konflikt v týmu** | Nerovnoměrná práce, hádky, zpoždění. | Týmová dohoda, role, pravidelná kontrola. | Přerozdělit role nebo zmenšit projekt. |
            | **Právní problém** | Nejasné oprávnění, reklamace, autorská práva, data. | Ověření pravidel a transparentní podmínky. | Pozastavit prodej a upravit podmínky. |
            """)

        # 6.7 ŠABLONA JEDNOSTRÁNKOVÉHO PODNIKATELSKÉHO ZÁMĚRU
        with st.container(border=True):
            st.markdown("### 📄 6.7 Šablona jednostránkového podnikatelského záměru")
            st.write("Vyplň si kompletní podnikatelský záměr pro svůj projekt na jednom místě:")

            col_z1, col_z2 = st.columns(2)
            with col_z1:
                st.text_input("Název projektu:", placeholder="Název...", key="z_name")
                st.text_input("Jedna věta projektu:", placeholder="Pomáháme [komu] řešit [jaký problém] pomocí [jakého řešení]...", key="z_one_sentence")
                st.text_area("Zákazník (komu přesně pomáháme):", placeholder="Cílová skupina...", height=70, key="z_cust")
                st.text_area("Problém (co zákazníka trápí):", placeholder="Popis problému...", height=70, key="z_prob")
                st.text_area("Hodnota pro zákazníka:", placeholder="Co tím získá...", height=70, key="z_val")
                st.text_area("Řešení & Konkurence:", placeholder="Návrh řešení a čím se lišíme...", height=70, key="z_sol")
            with col_z2:
                st.text_input("Navržená cena:", placeholder="Cena v Kč...", key="z_price")
                st.text_input("Odhadované náklady (jednorázové, fixní, variabilní):", placeholder="Náklady...", key="z_costs")
                st.text_area("První test & Metrika úspěchu:", placeholder="Jak levně ověříte zájem...", height=70, key="z_test")
                st.text_area("Hlavní riziko & Plán B:", placeholder="Co se může pokazit...", height=70, key="z_risk")
                st.text_input("Právní forma pro start:", placeholder="OSVČ / s.r.o. / Záměr v rámci školy...", key="z_legal")
                st.text_input("Etické pravidlo projektu:", placeholder="Pravidlo poctivosti...", key="z_ethics")

            if st.button("💾 Uložit můj podrobný podnikatelský záměr", use_container_width=True):
                st.success("Podnikatelský záměr byl úspěšně uložen do vašeho profilu pokroků!")

            st.markdown("""
            <div class='box-green'>
                <strong>Výstup pro mini projekt:</strong> Máš umět představit podnikatelský záměr v jedné stránce a obhájit, proč dává ekonomický, právní a etický smysl.
            </div>
            """, unsafe_allow_html=True)

    # PODKAPITOLA 7 - LEAN CANVAS
    elif selected_section == "7. Lean Canvas":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 7</div>", unsafe_allow_html=True)
        st.markdown("## 7. Lean Canvas")
        
        with st.container(border=True):
            st.write("""
            Lean Canvas je rychlá mapa podnikatelského nápadu. Pomáhá zachytit hlavní předpoklady a rizika dřív, než podnikatel investuje mnoho času nebo peněz. Na rozdíl od klasického podnikatelského plánu je stručný, pracovní a snadno se upravuje.
            """)
            st.markdown("""
            <div class='box-blue'>
                <strong>Proč je to důležité:</strong> Lean Canvas pomáhá řešit problém, pracovat s hypotézami, ověřovat informace, plánovat podnikatelskou aktivitu, posoudit ekonomickou proveditelnost a vyhodnocovat rizika. Podnikání není hádání, ale ověřování předpokladů.
            </div>
            """, unsafe_allow_html=True)

            st.text_input("🧩 Interaktivní výzva: Vyber jednu domněnku ze svého Lean Canvasu a přepiš ji jako ověřitelnou hypotézu:", placeholder="Věříme, že…, ověříme to pomocí…, úspěch poznáme podle…", key="p7_hypo_test")

            st.markdown("""
            <div class='box-purple'>
                <strong>🤖 AI mentoring:</strong> Zkopíruj tento prompt do AI asistenta:<br>
                <i>„Pomoz mi převést můj Lean Canvas na ověřitelné hypotézy. U každé napiš test, metriku úspěchu, riziko špatné interpretace a rozhodnutí, co udělat, když test nevyjde.“</i>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class='box-gray'>
                <strong>Tým pracuje s lístečky na Lean Canvasu:</strong> Lean Canvas není hotový podnikatelský plán. Je to pracovní nástroj pro ověřování nápadu. Největší hodnotu má tehdy, když se po testech mění.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 7.1 Proč Lean Canvas začíná problémem")
            st.write("""
            Mnoho týmů začíná řešením: aplikací, e-shopem, produktem, logem nebo profilem na sociální síti. Lean Canvas nutí začít otázkou: **Jaký problém vlastně řešíme a pro koho?**

            Pokud problém není důležitý, zákazník nebude měnit chování. Pokud zákazník není konkrétní, marketing bude obecný. Pokud cena nevychází z hodnoty a nákladů, projekt může být populární, ale ztrátový.
            """)

        with st.container(border=True):
            st.markdown("### 7.2 Devět bloků Lean Canvasu")
            st.write("U každého bloku bys měl umět napsat maximálně dvě věty. Kde si nejsi jistý/á, označ to jako hypotézu a navrhni test.")

            st.markdown("""
            | Blok | Co znamená | Dobrá otázka | Častá chyba |
            | :--- | :--- | :--- | :--- |
            | **1. Problém** | 1–3 konkrétní problémy zákazníka. | Kdy zákazník problém naposledy řešil? | Popisujeme naše řešení místo zákazníkova problému. |
            | **2. Zákaznické segmenty** | Konkrétní skupiny lidí, které problém řeší. | Kdo problém cítí nejsilněji? | Píšeme „všichni studenti“ nebo „všichni lidé“. |
            | **3. Unikátní nabídka hodnoty** | Jasné vysvětlení, proč má zákazník zpozornět. | Proč by si měl vybrat právě nás? | Používáme obecné fráze jako „kvalitní, levné, moderní“. |
            | **4. Řešení** | Jednoduchý návrh, jak problém řešíme. | Jaká je nejmenší funkční verze? | Navrhujeme příliš složitý produkt hned na začátku. |
            | **5. Kanály** | Cesty, kterými se dostaneme k zákazníkovi. | Kde zákazník skutečně je? | Vybereme sociální síť bez měření výsledků. |
            | **6. Příjmy** | Za co zákazník platí a jak často. | Je to jednorázový prodej, předplatné, služba, provize? | Zaměníme popularitu za ochotu platit. |
            | **7. Náklady** | Co stojí start, provoz a každý prodaný kus. | Který náklad nejčastěji podceňujeme? | Nezapočítáme čas, obaly, dopravu, reklamu a rezervu. |
            | **8. Klíčové metriky** | Čísla, podle kterých poznáme pokrok. | Které číslo nám pomůže rozhodnout? | Sledujeme lajky místo objednávek nebo opakovaného zájmu. |
            | **9. Neférová výhoda** | Něco, co konkurence nemůže snadno okopírovat. | Co máme jen my nebo co se těžko napodobuje? | Píšeme běžné věci jako „dobrý nápad“ nebo „nadšení“. |
            """)

        with st.container(border=True):
            st.markdown("### 7.3 Jak poznat dobrou hypotézu")
            st.write("Hypotéza je předpoklad, který se dá ověřit. Nemá znít jako přání, ale jako tvrzení s testem a měřítkem úspěchu.")

            st.markdown("""
            | Slabá domněnka | Ověřitelná hypotéza | Test | Metrika úspěchu |
            | :--- | :--- | :--- | :--- |
            | **Studentům se to bude líbit.** | Alespoň 20 z 50 oslovených studentů označí problém za častý a 8 z nich se zapíše k testu. | Rozhovor a registrační formulář. | 20 potvrzených problémů, 8 registrací. |
            | **Lidé za to zaplatí.** | Alespoň 10 lidí si předobjedná produkt za 149 Kč. | Předobjednávková stránka nebo formulář. | 10 předobjednávek. |
            | **Instagram bude fungovat.** | Testovací příspěvek přivede alespoň 30 kliknutí na formulář a 5 objednávek. | Příspěvek s měřeným odkazem. | 30 kliknutí, 5 objednávek. |
            | **Náklady budou nízké.** | Variabilní náklad na kus nepřekročí 60 % plánované prodejní ceny. | Kalkulace a test výroby 5 kusů. | Náklad max. 60 % ceny. |
            """)

        with st.container(border=True):
            st.markdown("### 7.4 MVP: nejmenší ověřitelná verze")
            st.write("MVP znamená nejmenší verzi řešení, která dokáže ověřit nejdůležitější předpoklad. Nemusí být dokonalá. Musí být dostatečná na učení.")

            st.markdown("""
            | Nápad | Drahý start | MVP test |
            | :--- | :--- | :--- |
            | **Aplikace na plánování učení** | Vývoj celé aplikace. | Notion šablona nebo sdílená tabulka pro 20 studentů. |
            | **E-shop s merchem** | Nákup zásob a spuštění plného e-shopu. | Předobjednávka se třemi návrhy a jasnou cenou. |
            | **Svačinové boxy** | Pronájem kuchyně a nákup vybavení. | Jeden testovací den s omezeným počtem objednávek. |
            | **Doučovací platforma** | Programování tržiště s účty a platbami. | Ručně propojit 10 dvojic přes formulář. |
            """)

        with st.container(border=True):
            st.markdown("### 7.5 Jak Lean Canvas vyhodnotit")
            st.write("""
            Po vyplnění Canvasu tým označí každé políčko jako:
            * **ověřeno** — máme data nebo zkušenost,
            * **hypotéza** — myslíme si to, ale ještě nevíme,
            * **riziko** — pokud se mýlíme, projekt může selhat.
            """)

            st.markdown("""
            <div class='box-yellow'>
                <strong>🧪 Pravidlo:</strong> Nejprve testuj políčka, která jsou zároveň nejistá a důležitá. Typicky problém, zákazník, ochota platit, náklady a kanály.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 7.6 Příklad Lean Canvasu: školní projekt „StudyBites“")
            
            st.markdown("""
            | Blok | Příklad vyplnění |
            | :--- | :--- |
            | **Problém** | Studenti nestíhají kvalitní svačinu mezi výukou a praxí; bufet je drahý nebo ve špatný čas; část studentů nejí vůbec. |
            | **Zákazníci** | Dojíždějící studenti 1.–3. ročníku, kteří mají dlouhý školní den. |
            | **Unikátní hodnota** | Předem objednaná svačina k vyzvednutí ve škole bez čekání. |
            | **Řešení** | Tři typy svačinových boxů s objednávkou přes formulář. |
            | **Kanály** | Třídní skupiny, QR plakát, školní Instagram, osobní doporučení. |
            | **Příjmy** | Prodej boxu za 65–79 Kč podle varianty. |
            | **Náklady** | Suroviny, obal, etiketa, doprava, čas přípravy, rezerva na nevyzvednuté kusy. |
            | **Metriky** | Počet předobjednávek, opakované objednávky, nevyzvednuté kusy, spokojenost. |
            | **Neférová výhoda** | Přímý kontakt se školní komunitou a přesná znalost rozvrhu studentů. |
            """)

        with st.container(border=True):
            st.markdown("### 7.7 Nejčastější chyby při práci s Lean Canvasem")
            st.markdown("""
            * Tým popíše řešení dřív než problém.
            * Zákazník je příliš obecný.
            * Cena je zvolená podle pocitu.
            * Náklady nezahrnují čas a rezervu.
            * Marketing měří lajky místo objednávek.
            * Canvas se po testování neupraví.
            * Tým se zamiluje do nápadu a ignoruje data.
            * „Neférová výhoda“ je jen běžná vlastnost, kterou může konkurence snadno okopírovat.
            """)

            st.markdown("""
            <div class='box-red'>
                <strong>Častá chyba:</strong> Vyplnit Lean Canvas jednou a považovat ho za hotový. Canvas je živý dokument. Po každém testu se má upravit.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 7.8 Jak Canvas správně vyplnit")
            st.markdown("""
            1. Začni problémem a zákazníkem.
            2. Teprve potom popiš řešení.
            3. Zapiš nejistoty jako hypotézy.
            4. Ověř, zda existují příjmy a zda náklady dávají smysl.
            5. Urči metriky, které pomohou rozhodnout.
            6. Navrhni MVP nebo první test.
            7. Po testování Canvas upravuj.
            """)

            st.markdown("""
            <div class='box-green'>
                <strong>✅ Výstup pro mini projekt:</strong> Máš odevzdat Lean Canvas, jednu ověřitelnou hypotézu, návrh MVP testu, metriku úspěchu a krátké rozhodnutí, co uděláš podle výsledku testu.
            </div>
            """, unsafe_allow_html=True)

        # 7.9 INTERAKTIVNÍ LEAN CANVAS - PRACOVNÍ PLÁTNO
        with st.container(border=True):
            st.markdown("### 🗂️ 7.9 Od teorie k praxi: Pracovní Lean Canvas")
            st.write("""
            Do nového Lean Canvasu zapisuj jednotlivé kartičky jako Post-it lístečky. Začni bloky Problém a Zákazník. Teprve potom doplň Řešení a Unikátní hodnotu. U Příjmů a Nákladů ověř, jestli projekt dává ekonomický smysl. Do Metrik napiš, podle čeho poznáš skutečný zájem.
            
            **Jakmile se projekt po testování změní, kartičky uprav!**
            """)

            st.markdown("""
            <div class='box-yellow'>
                <strong>🧪 Propojení s databází Hypotézy:</strong> Každý neověřený předpoklad z plátna by se měl proměnit v ověřitelný test.
            </div>
            """, unsafe_allow_html=True)

            lc_col1, lc_col2, lc_col3, lc_col4, lc_col5 = st.columns(5)
            
            with lc_col1:
                st.markdown("<div class='lc-title'>🔴 1. PROBLÉM</div>", unsafe_allow_html=True)
                lc_problem = st.text_area("Jaké hlavní problémy řešíte?", placeholder="Co je trápí...", height=150, key="lc7_prob")
            
            with lc_col2:
                st.markdown("<div class='lc-title'>🟢 4. ŘEŠENÍ</div>", unsafe_allow_html=True)
                lc_solution = st.text_area("Jaké řešení navrhujete?", placeholder="Jak to vyřešíte...", height=150, key="lc7_sol")
            
            with lc_col3:
                st.markdown("<div class='lc-title'>🟡 3. UNIKÁTNÍ HODNOTA</div>", unsafe_allow_html=True)
                lc_uvp = st.text_area("Proč má zákazník zpozornět?", placeholder="Jasné sdělení...", height=150, key="lc7_uvp")
            
            with lc_col4:
                st.markdown("<div class='lc-title'>🟤 9. NEFÉROVÁ VÝHODA</div>", unsafe_allow_html=True)
                lc_advantage = st.text_area("Co máte, co konkurence nemá?", placeholder="Těžko napodobitelná výhoda...", height=150, key="lc7_adv")
            
            with lc_col5:
                st.markdown("<div class='lc-title'>🟠 2. ZÁKAZNÍCI</div>", unsafe_allow_html=True)
                lc_customers = st.text_area("Kdo jsou cíloví zákazníci?", placeholder="Kdo zaplatí nejdřív...", height=150, key="lc7_cust")

            lc_row2_1, lc_row2_2 = st.columns(2)
            with lc_row2_1:
                st.markdown("<div class='lc-title'>⚪ 8. KLÍČOVÉ METRIKY</div>", unsafe_allow_html=True)
                lc_metrics = st.text_area("Podle čeho poznáte úspěch?", placeholder="Registrace, prodeje...", height=100, key="lc7_met")
            with lc_row2_2:
                st.markdown("<div class='lc-title'>🔵 5. KANÁLY</div>", unsafe_allow_html=True)
                lc_channels = st.text_area("Jak se o vás zákazník dozví?", placeholder="Cesta k zákazníkům...", height=100, key="lc7_chan")

            lc_row3_1, lc_row3_2 = st.columns(2)
            with lc_row3_1:
                st.markdown("<div class='lc-title'>🌸 7. NÁKLADY</div>", unsafe_allow_html=True)
                lc_costs = st.text_area("Jaké hlavní náklady vzniknou?", placeholder="Vývoj, materiál, reklama...", height=100, key="lc7_cost")
            with lc_row3_2:
                st.markdown("<div class='lc-title'>🟣 6. PŘÍJMY</div>", unsafe_allow_html=True)
                lc_revenue = st.text_area("Za co a kolik bude zákazník platit?", placeholder="Model zisku a ceny...", height=100, key="lc7_rev")

            st.text_input("🧩 Interaktivní výzva: Navrhni jeden rychlý test zákazníka, který zvládneš provést během 20 minut, a zapiš ho jako kartičku do části Metriky nebo Problém:", placeholder="Váš návrh na 20minutový test...", key="p7_quick_test")

            if st.button("💾 Uložit pracovní Lean Canvas", use_container_width=True):
                st.success("Tento pracovní Lean Canvas byl úspěšně uložen do vašeho profilu pokroků!")

    # PODKAPITOLA 8 (CSR, ETIKA A ODPOVĚDNÉ PODNIKÁNÍ)
    elif selected_section == "8. CSR, etika a odpovědné podnikání":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 8</div>", unsafe_allow_html=True)
        st.markdown("## 8. CSR, etika a odpovědné podnikání")
        
        with st.container(border=True):
            st.write("""
            CSR znamená společenská odpovědnost firem. Připomíná, že podnikání nemá sledovat pouze zisk, ale také dopady na zákazníky, zaměstnance, společnost a životní prostředí. V moderní ekonomice se často používá také pojem ESG — tedy odpovědnost v oblasti životního prostředí (Environmental), lidí a společnosti (Social) a řízení firmy (Governance).
            """)
            st.markdown("""
            <div class='box-blue'>
                <strong>Proč je to důležité:</strong> Podnikání ovlivňuje zákazníky, zaměstnance, dodavatele, společnost i životní prostředí. Legální jednání nemusí být vždy automaticky férové nebo udržitelné, proto je potřeba přemýšlet i o etice a odpovědnosti.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 8.1 Odpovědnost jako součást podnikatelského rozhodování")
            st.write("""
            Moderní zákazník často neřeší jen cenu. Sleduje také původ produktu, pracovní podmínky, obaly, ekologickou stopu, pravdivost reklamy, ochranu dat a chování značky v krizových situacích.

            Odpovědné podnikání neznamená, že firma musí být dokonalá. Znamená, že:
            * zná své dopady,
            * umí je měřit,
            * komunikuje je pravdivě,
            * nastavuje pravidla,
            * řeší chyby,
            * neprodává odpovědnost jen jako marketingový slogan.
            """)

            st.markdown("""
            <div class='box-gray'>
                <strong>🧠 Pointa pro tebe:</strong> Etika není doplněk až „po zisku“. Etika rozhoduje o tom, jestli firma dlouhodobě získá důvěru lidí.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 8.2 Etické dilema: co když je výhodné něco zamlčet?")
            st.write("""
            Podnikatel může být v situaci, kdy krátkodobě vydělá tím, že něco neřekne: neupozorní na omezení produktu, použije zavádějící slevu, schová poplatek, přehání ekologičnost nebo manipuluje recenzemi.
            """)

            st.markdown("""
            | Situace | Krátkodobé pokušení | Dlouhodobé riziko | Férovější řešení |
            | :--- | :--- | :--- | :--- |
            | **Produkt má omezenou životnost.** | Neříct to zákazníkovi. | Reklamace, špatné recenze, ztráta důvěry. | Uvést reálnou životnost a nabídnout servis. |
            | **E-shop nabízí slevu.** | Uměle navýšit původní cenu. | Klamavá komunikace a poškození značky. | Ukázat skutečné srovnání ceny. |
            | **Firma používá ekologický obal.** | Tvrdit, že celý produkt je „eko“. | Greenwashing. | Popisovat konkrétně jen to, co firma opravdu zlepšila. |
            | **Aplikace sbírá data.** | Schovat souhlas do dlouhých podmínek. | Nedůvěra, právní problém, poškození uživatele. | Vysvětlit jednoduše, jaká data a proč se sbírají. |
            """)

        with st.container(border=True):
            st.markdown("### 8.3 ESG v malém projektu")
            st.write("""
            ESG se nemusí týkat jen velkých firem. I školní nebo studentský projekt může přemýšlet:
            * **E (Environment):** Kolik odpadu vytváříme? Jaké obaly používáme? Jak řešíme dopravu?
            * **S (Social):** Chováme se férově ke členům týmu, zákazníkům a dodavatelům?
            * **G (Governance):** Máme jasná pravidla rozhodování, peněz, dat a odpovědnosti?
            """)

            st.markdown("#### 🌱 Mini audit odpovědnosti projektu")
            st.write("Vyber vlastní projekt a odpověz:")
            
            col_esg1, col_esg2 = st.columns(2)
            with col_esg1:
                st.text_input("1. Jaký pozitivní dopad může mít?", placeholder="Pozitiva...", key="esg_pos")
                st.text_input("2. Jaký negativní dopad může mít?", placeholder="Negativa...", key="esg_neg")
                st.text_input("3. Jak budeme komunikovat pravdivě?", placeholder="Komunikace...", key="esg_com")
            with col_esg2:
                st.text_input("4. Jak budeme chránit osobní údaje?", placeholder="Ochrana dat...", key="esg_data")
                st.text_input("5. Jak poznáme, že nejde o greenwashing?", placeholder="Důkaz...", key="esg_green")
                st.text_input("6. Jaké pravidlo férovosti si dáme do týmu?", placeholder="Pravidlo týmu...", key="esg_team")

            if st.button("Uložit mini audit ESG", use_container_width=True):
                st.success("Tvůj audit odpovědnosti byl uložen!")

            st.text_input("🧩 Interaktivní výzva: Napiš jedno pravidlo férového chování, které by měl tvůj projekt dodržovat vůči zákazníkům nebo zaměstnancům:", placeholder="Moje pravidlo férovosti...", key="p8_fair_rule")

            st.markdown("""
            <div class='box-purple'>
                <strong>🤖 AI mentoring:</strong> Zkopíruj tento prompt do AI asistenta:<br>
                <i>„Navrhni pro můj projekt jednoduchý etický kodex v pěti bodech.“</i>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class='box-green'>
                <strong>Etika v podnikání:</strong> Férový podnikatel nezneužívá švarcsystém, platí daně, jedná poctivě se zákazníky a chová se ohleduplně k zaměstnancům, partnerům i životnímu prostředí.
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class='box-gray'>
                <strong>Aktuální souvislost k roku 2026:</strong> Udržitelnost už není jen dobrovolná „hezká aktivita“ navíc. Velké firmy a jejich dodavatelé stále častěji sledují data o emisích, spotřebě energií, pracovních podmínkách, bezpečnosti, diverzitě, ochraně osobních údajů a transparentním řízení. Menší firmy se s ESG setkávají hlavně jako dodavatelé větších společností, při žádosti o financování nebo při komunikaci se zákazníky.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 8.4 Proč CSR řešit")
            st.text_input("🧩 Interaktivní výzva: Vyber jednu skupinu, kterou tvůj projekt ovlivní, a napiš možný pozitivní i negativní dopad:", placeholder="Skupina a dopady...", key="p8_impact_group")

            st.markdown("""
            * Firma ovlivňuje své okolí — zákazníky, zaměstnance, dodavatele, obec, krajinu i veřejnou debatu.
            * Zákazníci často sledují, zda se firma chová férově a zda její reklama odpovídá realitě.
            * Odpovědné podnikání může posilovat důvěru, pověst značky a dlouhodobou stabilitu firmy.
            * Etika pomáhá předcházet problémům, které jsou sice někdy krátkodobě „výhodné“, ale dlouhodobě škodí.
            * Banky, investoři a obchodní partneři stále častěji sledují, zda firma umí řídit i nefinanční rizika.
            """)

        with st.container(border=True):
            st.markdown("### 8.5 ESG jednoduše: tři oblasti odpovědnosti")
            st.markdown("""
            | Oblast | Co znamená | Příklad z praxe |
            | :--- | :--- | :--- |
            | **E — Environment** | Dopad na životní prostředí. | Spotřeba energií, emise CO₂, odpady, obaly, voda, doprava, recyklace. |
            | **S — Social** | Vztah k lidem. | Bezpečnost práce, férové mzdy, vzdělávání zaměstnanců, diverzita, ochrana zákazníků. |
            | **G — Governance** | Způsob řízení firmy. | Etický kodex, transparentnost, prevence korupce, ochrana dat, odpovědné rozhodování vedení. |
            """)

            st.markdown("""
            <div class='box-red'>
                <strong>Pozor na greenwashing:</strong> Odpovědnost nestačí jen tvrdit v reklamě. Firma by měla umět doložit konkrétní data, cíle a výsledky. Pokud se prezentuje jako „zelená“, ale skutečné dopady neřeší, může jít o klamavou komunikaci.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 8.6 Příklady odpovědného podnikání")
            st.text_input("🧩 Interaktivní výzva: Vyber dva příklady odpovědného podnikání z tohoto seznamu a uprav je na konkrétní pravidla pro svůj projekt:", placeholder="Moje 2 pravidla...", key="p8_resp_examples")

            st.markdown("""
            * férové zacházení se zaměstnanci,
            * pravdivá reklama,
            * odpovědné nakládání s osobními údaji,
            * ekologičtější výroba,
            * snižování odpadu a lepší práce s obaly,
            * bezpečné pracovní prostředí,
            * podpora místní komunity,
            * transparentní komunikace se zákazníky,
            * prevence korupce a střetu zájmů,
            * odpovědný výběr dodavatelů.
            """)

        with st.container(border=True):
            st.markdown("### 8.7 Firmy působící v ČR: aktuální příklady odpovědnosti")
            st.write("Následující příklady nejsou „žebříček nejhodnějších firem“. Jsou to ukázky firem působících na českém trhu, které veřejně komunikují odpovědnost, ESG, etiku nebo udržitelnost a zveřejňují konkrétní kroky či reporty.")

            st.markdown("""
            | Firma působící v ČR | Oblast odpovědnosti | Co lze studentům ukázat |
            | :--- | :--- | :--- |
            | **Škoda Auto** | ESG strategie, výroba, regionální odpovědnost | Automobilka veřejně komunikuje udržitelnost, řízení dopadů výroby, firemní kulturu, integritu a odpovědnost vůči regionům, kde má závody. |
            | **ČEZ** | Energetika, ESG data, dekarbonizace | Energetická firma zveřejňuje rozsáhlá ESG data a strategii zaměřenou na transformaci energetiky, emise, bezpečnost a řízení dopadů. |
            | **O2 Czech Republic** | Digitální bezpečnost, vzdělávání, emise | Telekomunikační firma reportuje ochranu zákazníků v online prostředí, digitální vzdělávání, nadační aktivity a snižování uhlíkové stopy. |
            | **Coca‑Cola HBC Česko a Slovensko** | Obaly, voda, bezpečnost práce, transparentní reporting | Firma zveřejňuje zprávy o udržitelnosti, řeší obaly, vodu, bezpečnost zaměstnanců a uvádí výsledky v environmentální, sociální i řídicí oblasti. |
            | **IKEA** | Cirkularita, dostupnost, klima, dodavatelský řetězec | IKEA dlouhodobě komunikuje cíle v oblasti klimatu, dostupnějšího udržitelného bydlení, cirkulární ekonomiky a odpovědného dodavatelského řetězce. |
            | **Kofola ČeskoSlovensko** | Lokální značka, voda, obaly, vztah ke krajině | Kofola je vhodný příklad pro debatu o tom, jak může potravinářská firma řešit vodní zdroje, obaly, lokální značky a dopady výroby. |
            | **Albert Česká republika** | Maloobchod, potraviny, odpady, dodavatelé | U obchodního řetězce lze řešit plýtvání potravinami, práci s dodavateli, obaly, zaměstnance a odpovědný prodej. |
            """)

            st.markdown("#### Jak s příklady pracovat ve výuce?")
            st.markdown("""
            * Nehodnoť firmu jen podle reklamy nebo sloganu.
            * Najdi konkrétní report, výroční zprávu, ESG stránku nebo nezávislé hodnocení.
            * Rozlišuj mezi tvrzením, cílem a doloženým výsledkem.
            * Ptej se: Co firma měří? Co zveřejňuje? Co zlepšila? Kde může mít problém?
            * Porovnej odpovědnost podle oboru — jiná rizika má energetika, jiná maloobchod, automobilka nebo technologická firma.
            """)

        with st.container(border=True):
            st.markdown("### 8.8 Mini případová studie: Jak poznat odpovědnou firmu?")
            st.text_input("🧩 Interaktivní výzva: Vyber jednu firmu působící v ČR a najdi její stránku o udržitelnosti, ESG report nebo etický kodex. Vypiš jednu silnou stránku a jednu otázku, kterou bys firmě položil/a:", placeholder="Firma, silná stránka, otázka...", key="p8_mini_case")

            st.markdown("""
            | Otázka | Co sledovat |
            | :--- | :--- |
            | **Má firma konkrétní cíle?** | Například snížení emisí, menší spotřeba vody, méně odpadu, bezpečnost práce. |
            | **Ukazuje data?** | Čísla za několik let, srovnání, metodika výpočtu, vysvětlení změn. |
            | **Řeší lidi?** | Zaměstnance, zákazníky, dodavatele, komunity, bezpečnost a férové podmínky. |
            | **Má pravidla řízení?** | Etický kodex, ochrana dat, protikorupční pravidla, mechanismus pro oznamování problémů. |
            | **Je komunikace důvěryhodná?** | Nejde jen o hezká slova; firma ukazuje i rizika, limity a oblasti ke zlepšení. |
            """)

            st.markdown("""
            <div class='box-yellow'>
                <strong>Pointa pro tebe:</strong> Odpovědné podnikání neznamená, že firma je dokonalá. Znamená to, že zná své dopady, měří je, zveřejňuje informace, nastavuje pravidla a snaží se zlepšovat.
            </div>
            """, unsafe_allow_html=True)

    # PODKAPITOLA 9 - RIZIKA PODNIKÁNÍ
    elif selected_section == "9. Rizika podnikání":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 9</div>", unsafe_allow_html=True)
        st.markdown("## 9. Rizika podnikání")
        
        with st.container(border=True):
            st.write("""
            Podnikání vždy obsahuje nejistotu. Podnikatel musí umět přemýšlet nejen o příležitostech, ale i o tom, co se může pokazit.
            """)
            st.markdown("""
            <div class='box-blue'>
                <strong>Proč je to důležité:</strong> Podnikání vždy obsahuje nejistotu. Důležité je umět rizika pojmenovat, posoudit jejich dopad, navrhnout preventivní opatření a rozhodovat se odpovědně finančně, právně i eticky.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 9.1 Riziko není důvod nepodnikat — je to důvod plánovat")
            st.write("""
            Riziko znamená, že výsledek může být jiný, než očekáváme. Podnikatel riziko neignoruje, ale pracuje s ním: odhaduje pravděpodobnost, dopad a možnosti prevence.
            Současná generace často začíná projekty rychle: profil, landing page, e-shop, předobjednávka, placená reklama, AI nástroj. Rychlý start je výhoda, ale může vytvořit rychlé chyby:
            * špatně nastavená cena,
            * podceněné náklady,
            * chybějící obchodní podmínky,
            * nejasné autorství obsahu,
            * nezvládnuté reklamace,
            * neověřený dodavatel,
            * závislost na jedné platformě,
            * ztráta účtu na sociální síti,
            * nečekané odvody a daně.
            """)

        with st.container(border=True):
            st.markdown("### 9.2 Matice rizik")
            st.markdown("""
            | Riziko | Pravděpodobnost | Dopad | Preventivní opatření |
            | :--- | :--- | :--- | :--- |
            | **Nízký zájem zákazníků** | Střední až vysoká | Vysoký | Ověřit problém rozhovory a předobjednávkou. |
            | **Vyšší náklady než plán** | Střední | Vysoký | Přidat rezervu, spočítat bod zvratu, porovnat dodavatele. |
            | **Právní chyba** | Střední | Vysoký | Ověřit živnost, smlouvy, obchodní podmínky a ochranu spotřebitele. |
            | **Závislost na jedné platformě** | Vysoká | Střední až vysoký | Budovat vlastní databázi kontaktů, web, e-mail a více kanálů. |
            | **Konflikt v týmu** | Střední | Střední až vysoký | Dohodnout role, podíly, rozhodování a pravidla komunikace předem. |
            | **Poškození reputace** | Střední | Vysoký | Pravdivá komunikace, rychlé řešení reklamací, etický kodex. |
            """)

        with st.container(border=True):
            st.markdown("### 9.3 Rizika digitálního podnikání")
            st.write("""
            Digitální podnikání má specifická rizika:
            * účet na sociální síti může být zablokován,
            * algoritmus sníží dosah,
            * reklama se prodraží,
            * zákaznická data mohou uniknout,
            * platební brána může mít výpadek,
            * AI může vytvořit chybný nebo právně problematický obsah,
            * konkurence může rychle okopírovat nápad.
            """)

            st.markdown("""
            <div class='box-gray'>
                <strong>🔐 Digitální bezpečnost:</strong> Hesla, dvoufázové ověření, zálohy, přístupy v týmu a ochrana zákaznických dat jsou součást podnikatelského rizika, ne „IT detail“.
            </div>
            """, unsafe_allow_html=True)

            st.markdown("#### 🧯 Aktivita: Krizový plán startupu")
            st.write("Vyber jedno riziko a připrav krizový plán:")

            col_kp1, col_kp2 = st.columns(2)
            with col_kp1:
                st.text_input("1. Jak poznáme, že problém nastal?", placeholder="Indikátor problému...", key="kp_ind")
                st.text_input("2. Koho se problém dotkne?", placeholder="Zasažené strany...", key="kp_who")
                st.text_input("3. Co uděláme během prvních 24 hodin?", placeholder="První akce...", key="kp_24h")
            with col_kp2:
                st.text_input("4. Jak budeme komunikovat se zákazníky?", placeholder="Plán komunikace...", key="kp_com")
                st.text_input("5. Jak zabráníme opakování?", placeholder="Prevence do budoucna...", key="kp_prev")

            if st.button("Uložit krizový plán"):
                st.success("Krizový plán byl úspěšně uložen!")

            st.text_input("🧩 Interaktivní výzva: Napiš tři největší rizika svého projektu a ke každému jednu možnost, jak ho snížit:", placeholder="1. Riziko - Opatření...", key="p9_top3_risks")

            st.markdown("""
            <div class='box-purple'>
                <strong>🤖 AI mentoring:</strong> Zkopíruj tento prompt do AI asistenta:<br>
                <i>„Udělej mi rizikovou analýzu mého startupu a seřaď rizika podle dopadu.“</i>
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 9.4 Typická podnikatelská rizika")
            st.markdown("""
            * zákazníci nebudou mít o produkt zájem,
            * náklady budou vyšší než očekávané,
            * konkurence nabídne lepší řešení,
            * podnikatel podcení daně a odvody,
            * vzniknou právní nebo reklamační problémy,
            * firma nebude mít dost peněz na provoz.
            """)

            st.text_input("🧩 Interaktivní výzva: Označ, které riziko je pro tvůj nápad nejpravděpodobnější, a napiš první preventivní krok:", placeholder="Moje největší riziko a prevence...", key="p9_most_prob_risk")

            st.markdown("""
            <div class='box-yellow'>
                <strong>Praktické minimum pro start podnikání:</strong><br>
                • počítat s daněmi a odvody,<br>
                • odlišit jednorázový přivýdělek od soustavné činnosti,<br>
                • znát základní pravidla ochrany spotřebitele,<br>
                • nakládat odpovědně s osobními údaji.
            </div>
            """, unsafe_allow_html=True)

    # PODKAPITOLA 10 - ŠVARCSYSTÉM
    elif selected_section == "10. Švarcsystém":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 10</div>", unsafe_allow_html=True)
        st.markdown("## 10. Švarcsystém")
        
        with st.container(border=True):
            st.write("""
            Švarcsystém je situace, kdy člověk formálně vystupuje jako podnikatel (OSVČ), ale fakticky pracuje jako zaměstnanec.
            """)

            st.text_input("🧩 Interaktivní výzva: Vymysli příklad spolupráce, která je férová, a příklad, který už by mohl připomínat švarcsystém:", placeholder="Férová vs Švarcsystém...", key="p10_fair_vs_svarc")

            with st.expander("💡 Zobrazit znaky rizikového nastavení spolupráce (Nápověda k výzvě)"):
                st.markdown("""
                **Jak poznat rizikové nastavení spolupráce?**
                * pracovník pracuje jen pro jednu firmu,
                * dostává pravidelné pokyny jako zaměstnanec,
                * má pevně určenou pracovní dobu,
                * pracuje v prostorách firmy,
                * používá vybavení firmy,
                * vystupuje jménem firmy.
                """)

            st.markdown("""
            <div class='box-purple'>
                <strong>🤖 AI mentoring:</strong> Zkopíruj tento prompt do AI asistenta:<br>
                <i>„Zkontroluj modelovou spolupráci a vysvětli, jestli v ní hrozí znaky švarcsystému.“</i>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class='box-red'>
                <strong>⚠️ Švarcsystém:</strong> Nelegální nastavení spolupráce, které může vést k pokutám, doměření odvodů a dalším problémům.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 10.1 Mini-hra: Švarc-detektiv")
            st.write("Zahraj si na inspektora práce. U každé situace nejdřív rozhodni, jestli jde o férový freelancing, nebo švarcsystém. Potom si rozklikni verdikt detektiva.")

            with st.expander("🕵️ Případ 1: Programátor v kanceláři"):
                st.write("**Situace:** Petr má živnostenský list, ale každý den od 8:00 do 16:30 sedí v kanceláři firmy XYZ, používá firemní notebook, nosí firemní tričko a dovolenou hlásí šéfovi.")
                st.markdown("<div class='box-red'><strong>Odpověď: ŠVARCSYSTÉM!</strong><br>Znaky: pevná pracovní doba, práce na zařízení firmy, nadřízenost, vystupování jako součást firmy a závislost na jednom zadavateli. Hrozí pokuta od úřadu práce.</div>", unsafe_allow_html=True)

            with st.expander("🕵️ Případ 2: Grafik s více klienty"):
                st.write("**Situace:** Grafik pracuje z vlastního studia, má pět různých klientů, sám si určuje cenu, termíny i způsob práce a fakturuje za konkrétní zakázky.")
                st.markdown("<div class='box-green'><strong>Odpověď: FÉROVÝ FREELANCING.</strong><br>Znaky: samostatnost, více klientů, vlastní vybavení, vlastní organizace práce a podnikatelské riziko.</div>", unsafe_allow_html=True)

            with st.expander("🕵️ Případ 3: „OSVČ“ s firemním e-mailem"):
                st.write("**Situace:** Člověk má IČO, ale používá e-mail firmy, vybavení firmy, pracuje podle pokynů manažera a o volnu musí žádat stejně jako zaměstnanci.")
                st.markdown("<div class='box-red'><strong>Odpověď: PRAVDĚPODOBNĚ ŠVARCSYSTÉM.</strong><br>Znaky: podřízenost, práce podle pokynů, využívání firemního vybavení, začlenění do firmy a omezená samostatnost.</div>", unsafe_allow_html=True)

            with st.expander("🕵️ Případ 4: Fotograf na zakázku"):
                st.write("**Situace:** Fotograf fotí pro různé klienty, používá vlastní techniku, domlouvá si cenu za konkrétní focení a sám rozhoduje, kdy a jak práci provede.")
                st.markdown("<div class='box-green'><strong>Odpověď: FÉROVÝ FREELANCING.</strong><br>Znaky: vlastní vybavení, více zakázek, samostatné rozhodování, výsledek práce místo řízené pracovní doby.</div>", unsafe_allow_html=True)

            st.markdown("""
            <div class='box-yellow'>
                <strong>Detektivní stopa:</strong> Pokud někdo formálně fakturuje jako OSVČ, ale fakticky pracuje jako zaměstnanec — má pevnou pracovní dobu, nadřízeného, firemní vybavení a malou samostatnost — může jít o švarcsystém.
            </div>
            """, unsafe_allow_html=True)

            st.text_area("K zamyšlení: Proč stát rozlišuje mezi zaměstnancem a podnikatelem? Koho tím chrání?", placeholder="Váš názor...", height=80, key="p10_reflect")

    # PODKAPITOLA 11 - OVĚŘOVÁNÍ INFORMACÍ A ZDROJE
    elif selected_section == "11. Ověřování informací a užitečné zdroje":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 11</div>", unsafe_allow_html=True)
        st.markdown("## 11. Ověřování informací a užitečné zdroje")
        
        with st.container(border=True):
            st.write("Při podnikání je důležité umět najít spolehlivé zdroje a ověřovat aktuální informace.")

            st.text_input("🧩 Interaktivní výzva: Ověř jednu existující firmu v online rejstříku a napiš, jakou má právní formu a kdo za ni jedná:", placeholder="Firma, forma, zástupce...", key="p11_verify_firm")

            st.markdown("""
            <div class='box-purple'>
                <strong>🤖 AI mentoring:</strong> Zkopíruj tento prompt do AI asistenta:<br>
                <i>„Připrav mi kontrolní seznam pro ověření firmy před spoluprací.“</i>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            ### Klíčové online zdroje:
            | Zdroj | K čemu slouží |
            | :--- | :--- |
            | **[BusinessInfo.cz](https://www.businessinfo.cz/)** | Oficiální portál pro podnikatele. |
            | **[Portál živnostenského podnikání](https://www.rzp.cz/)** | Vyhledávání živností a informace k podnikání na živnost. |
            | **[Justice.cz](https://or.justice.cz/)** | Veřejný rejstřík, kde lze ověřit firmy a jejich historii. |
            | **[Zákony pro lidi](https://www.zakonyprolidi.cz/)** | Aktuální znění zákonů. |
            | **[Moje daně](https://adisspr.mfcr.cz/)** | Portál Finanční správy pro správu daňových povinností. |
            """)

            st.markdown("""
            <div class='box-blue'>
                <strong>🔍 Ověř firmu krok za krokem:</strong><br>
                1. Najdi firmu podle názvu nebo IČO.<br>
                2. Ověř právní formu.<br>
                3. Zjisti, kdo za firmu jedná.<br>
                4. Podívej se, zda je aktivní, v likvidaci nebo v insolvenci.<br>
                5. Vysvětli, proč je tato kontrola důležitá pro zákazníka, dodavatele nebo budoucího zaměstnance.
            </div>
            """, unsafe_allow_html=True)

    # PODKAPITOLA 12 - UKONČENÍ PODNIKÁNÍ
    elif selected_section == "12. Ukončení podnikání":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 12</div>", unsafe_allow_html=True)
        st.markdown("## 12. Ukončení podnikání")
        
        with st.container(border=True):
            st.write("Podnikání může skončit dobrovolně, rozhodnutím soudu nebo například v důsledku insolvence.")

            st.text_input("🧩 Interaktivní výzva: Napiš dva varovné signály, podle kterých by podnikatel poznal, že musí změnit plán nebo podnikání ukončit:", placeholder="Signál 1, signál 2...", key="p12_warning_signals")

            st.markdown("""
            <div class='box-purple'>
                <strong>🤖 AI mentoring:</strong> Zkopíruj tento prompt do AI asistenta:<br>
                <i>„Navrhni plán B pro můj startup, pokud první verze nebude fungovat.“</i>
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 12.1 Zrušení vs. zánik")
            st.text_input("🧩 Interaktivní výzva: Vysvětli vlastními slovy rozdíl mezi zrušením a zánikem firmy na jednoduchém příkladu:", placeholder="Zrušení vs zánik...", key="p12_cancel_vs_end")

            with st.expander("💡 Zobrazit správné vysvětlení (Zrušení vs. Zánik)"):
                st.markdown("""
                * **Zrušení = proces:** Rozhodnutí, že firma končí. Může následovat likvidace, vypořádání majetku, dluhů a závazků.
                * **Zánik = konec:** Definitivní okamžik, kdy firma právně přestává existovat. Obchodní korporace zaniká výmazem z obchodního rejstříku.
                """)

            st.markdown("""
            <div class='box-red'>
                <strong>Důležitá poznámka k insolvenci:</strong> Pokud má firma více dluhů než majetku a není schopna závazky splácet, může se dostat do úpadku.
            </div>
            """, unsafe_allow_html=True)

    # PODKAPITOLA 13 - LOGICKÁ MAPA PODNIKÁNÍ
    elif selected_section == "13. Logická mapa podnikání":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 13</div>", unsafe_allow_html=True)
        st.markdown("## 13. Logická mapa podnikání")
        
        with st.container(border=True):
            st.markdown("""
            <div class='box-gray'>
                <strong>Přehled tématu:</strong> Tato mapa shrnuje hlavní oblasti podnikání od právního rámce přes právní formy až po záměr, rizika a ukončení podnikání.
            </div>
            """, unsafe_allow_html=True)

            st.text_input("🧩 Interaktivní výzva: Vyber jednu větev mapy, která je pro tvůj projekt nejdůležitější, a napiš proč:", placeholder="Zvolená větev a důvod...", key="p13_map_choice")

            st.markdown("""
            <div class='box-purple'>
                <strong>🤖 AI mentoring:</strong> Zkopíruj tento prompt do AI asistenta:<br>
                <i>„Vytvoř mi logickou mapu mého startupu podle oblastí: právo, zákazník, finance, rizika a odpovědnost.“</i>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("### Vizualizace logické mapy podnikání:")
            
            # Vylepšená grafická Mind Mapa pomocí HTML/CSS - ODSTRANĚNY PRÁZDNÉ ŘÁDKY PROTI ROZBITÍ MARKDOWNU
            st.markdown("""
            <style>
            .mindmap-wrapper {
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 2rem 1rem;
                flex-wrap: wrap;
                gap: 2rem;
                background: #f1f5f9;
                border-radius: 12px;
                border: 1px solid #e2e8f0;
                margin-bottom: 1.5rem;
            }
            .mm-col {
                display: flex;
                flex-direction: column;
                gap: 1.5rem;
            }
            .mm-center {
                background: #ef4444;
                color: white;
                padding: 1.8rem 2.5rem;
                border-radius: 20px;
                font-weight: 800;
                font-size: 1.5rem;
                text-align: center;
                box-shadow: 0 10px 15px -3px rgba(239, 68, 68, 0.3);
                border: 3px solid #b91c1c;
                z-index: 2;
            }
            .mm-node {
                background: #ffffff;
                border: 2px solid #cbd5e1;
                padding: 1rem;
                border-radius: 16px;
                width: 260px;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
                position: relative;
                transition: all 0.2s ease;
            }
            .mm-node:hover {
                border-color: #6366f1;
                box-shadow: 0 10px 15px -3px rgba(99, 102, 241, 0.2);
                transform: translateY(-2px);
            }
            .mm-title {
                font-weight: 700;
                color: #1e293b;
                margin-bottom: 0.5rem;
                text-align: center;
                border-bottom: 2px solid #e2e8f0;
                padding-bottom: 0.5rem;
                text-transform: uppercase;
                font-size: 0.85rem;
                letter-spacing: 0.05em;
            }
            .mm-node ul {
                margin: 0;
                padding-left: 1.2rem;
                font-size: 0.85rem;
                color: #475569;
            }
            .mm-node li { margin-bottom: 0.3rem; }
            </style>
            <div class="mindmap-wrapper">
                <div class="mm-col">
                    <div class="mm-node"><div class="mm-title">1. Legislativa a definice</div><ul><li>občanský zákoník</li><li>živnostenský zákon</li><li>ZOK</li><li>znaky podnikání</li></ul></div>
                    <div class="mm-node"><div class="mm-title">2. Právní formy</div><ul><li>OSVČ, v.o.s., k.s.</li><li>s.r.o., a.s.</li></ul></div>
                    <div class="mm-node"><div class="mm-title">3. Záměr a Lean Canvas</div><ul><li>zákazník a problém</li><li>řešení, první test</li><li>náklady a příjmy</li></ul></div>
                </div>
                <div class="mm-center">PODNIKÁNÍ<br><span style="font-size:0.9rem; font-weight: 500;">Logická mapa</span></div>
                <div class="mm-col">
                    <div class="mm-node"><div class="mm-title">4. CSR a etika</div><ul><li>férové jednání</li><li>odpovědnost (zaměstnanci, společnost, prostředí)</li></ul></div>
                    <div class="mm-node"><div class="mm-title">5. Rizika</div><ul><li>finanční riziko</li><li>právní a tržní riziko</li><li>švarcsystém</li></ul></div>
                    <div class="mm-node"><div class="mm-title">6. Zdroje a ukončení</div><ul><li>veřejné rejstříky</li><li>zrušení a zánik</li><li>insolvence</li></ul></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # PODKAPITOLA 14 - REFLEXE A SEBEHODNOCENÍ
    elif selected_section == "14. Reflexe a sebehodnocení":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 14</div>", unsafe_allow_html=True)
        st.markdown("## 14. Reflexe a sebehodnocení")
        
        with st.container(border=True):
            st.markdown("""
            <div class='box-purple'>
                <strong>Formativní hodnocení:</strong> Nejde o známku. Cílem je zjistit, čemu už rozumíš, co umíš použít v praxi a kde ještě potřebuješ další příklad.
            </div>
            """, unsafe_allow_html=True)

            st.text_input("🧩 Interaktivní výzva: Po dokončení kapitoly si vyber jednu oblast, ve které máš největší nejistotu, a napiš otázku pro další konzultaci:", placeholder="Moje otázka...", key="p14_uncertainty")

            st.markdown("""
            <div class='box-purple'>
                <strong>🤖 AI mentoring:</strong> Zkopíruj tento prompt do AI asistenta:<br>
                <i>„Vyzkoušej mě z Kapitoly 1 pomocí pěti otázek a potom mi dej zpětnou vazbu.“</i>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("### 📝 Vyplň svou reflexi kapitoly:")
            
            st.text_area("1. Co jsem se dnes naučil/a? (Napiš vlastními slovy 3 věci, které si z kapitoly odnášíš):", height=80, key="p14_r1")
            st.text_area("2. Co umím vysvětlit vlastními slovy? (Zkus vysvětlit rozdíl mezi zaměstnancem, OSVČ a s.r.o.):", height=80, key="p14_r2")
            st.text_area("3. V čem mám ještě nejasnosti? (Vyber jednu část: právní formy, ručení, záměr, Lean Canvas, CSR, švarcsystém nebo ukončení):", height=80, key="p14_r3")
            st.text_area("4. Která právní forma by se hodila pro můj nápad? (A vysvětli proč):", height=80, key="p14_r4")
            st.text_area("5. Jaký je můj první praktický krok? (Konkurence, rozhovor, ověření v rejstříku, nebo Lean Canvas?):", height=80, key="p14_r5")

            if st.button("💾 Uložit moji reflexi", use_container_width=True):
                st.success("Tvoje reflexe byla úspěšně uložena!")

            st.markdown("### ✅ Checklist sebehodnocení:")
            st.checkbox("Umím vysvětlit, co je podnikání a kdo je podnikatel.", key="chk1")
            st.checkbox("Rozliším OSVČ, v.o.s., k.s., s.r.o. a a.s.", key="chk2")
            st.checkbox("Chápu rozdíl mezi fyzickou a právnickou osobou.", key="chk3")
            st.checkbox("Dokážu navrhnout základ podnikatelského záměru.", key="chk4")
            st.checkbox("Umím použít Lean Canvas na jednoduchý nápad.", key="chk5")
            st.checkbox("Chápu, proč je důležitá etika, CSR a férové podnikání.", key="chk6")
            st.checkbox("Umím ověřit základní údaje o firmě v online rejstříku.", key="chk7")

    # PODKAPITOLA 15 - INTEGROVANÉ OPAKOVÁNÍ
    elif selected_section == "15. Integrované opakování":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 15</div>", unsafe_allow_html=True)
        st.markdown("## 15. Integrované opakování: od nápadu k odpovědnému podnikání")
        
        with st.container(border=True):
            st.markdown("""
            <div class='box-blue'>
                <strong>Proč je tato část důležitá:</strong> Tady si neposkládáš další nové definice, ale propojíš celou kapitolu do jedné praktické cesty. Půjdeš od prvního nápadu přes zákazníka, právní formu, finance, ověřování startupu, Lean Canvas, marketing, rizika a etiku až k závěrečnému rozhodnutí, jestli má projekt smysl rozvíjet.
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class='box-gray'>
                <strong>Jak s touto částí pracovat:</strong> Ber ji jako závěrečný pracovní modul. Postupně si ověříš, co už umíš z předchozích částí, a převedeš to do vlastního podnikatelského rozhodnutí: co chceš řešit, pro koho, za kolik, s jakým rizikem a jak poznáš, jestli pokračovat.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 15.1 Mapa závěrečného modulu")
            st.markdown("""
            | Část | Na co navazuje | Co má student vytvořit nebo rozhodnout |
            | :--- | :--- | :--- |
            | **1. Podnikavé uvažování** | Podnikatel, znaky podnikání, odpovědnost | Rozlišit koníček, přivýdělek, zaměstnání a podnikání. |
            | **2. Zákazník a hodnota** | Startup, Lean Canvas, záměr | Popsat konkrétní problém, zákazníka a hodnotu řešení. |
            | **3. Právní a organizační rámec** | OSVČ, živnosti, korporace, švarcsystém | Zdůvodnit vhodnou formu pro start projektu. |
            | **4. Finance a proveditelnost** | Cena, náklady, marže, bod zvratu | Sestavit základní kalkulaci a posoudit ekonomický smysl. |
            | **5. Ověřování a rozhodování** | Lean Startup, MVP, hypotézy | Navrhnout první test a rozhodnout, co udělat podle výsledku. |
            | **6. Marketing, data a důvěra** | Digitální podnikání, reputace | Připravit pravdivé sdělení pro zákazníka a pravidla dat. |
            | **7. Etika, CSR a rizika** | Odpovědné podnikání, ESG, rizika | Navrhnout etická pravidla, rizikovou matici a opatření. |
            | **8. Závěrečná podnikatelská mise** | Celá kapitola | Propojit všechny části do obhajitelného návrhu projektu. |
            """)

        with st.container(border=True):
            st.markdown("### 15.2 Co si máš z kapitoly opravdu odnést")
            st.write("Po projití celé kapitoly bys neměl/a mít pocit, že podnikání je jen seznam definic. Podnikání je hlavně způsob rozhodování: propojuje nápad, zákazníka, cenu, náklady, riziko, právo, odpovědnost a komunikaci.")
            
            st.markdown("""
            **Měl/a bys umět:**
            * vysvětlit, kdy se z nápadu stává podnikání,
            * rozlišit OSVČ, obchodní korporaci a další právní formy,
            * posoudit výhody a rizika konkrétní formy,
            * navrhnout jednoduchý podnikatelský záměr a Lean Canvas,
            * formulovat hypotézu a navrhnout test,
            * odhadnout náklady, příjmy a bod zvratu,
            * poznat rozdíl mezi férovým podnikáním, greenwashingem a švarcsystémem,
            * ověřit firmu ve veřejných zdrojích.
            """)

            st.markdown("#### 🎯 Aktivita: Můj posun v podnikavosti")
            st.write("Porovnej své odpovědi teď s tím, co sis myslel/a na začátku kapitoly:")

            c_q1, c_q2 = st.columns(2)
            with c_q1:
                st.text_area("Co podle mě znamená podnikat?", height=70, key="p15_a1")
                st.text_area("Čeho bych se při podnikání nejvíc bál/a?", height=70, key="p15_a2")
                st.text_area("Jaký problém bych chtěl/a řešit?", height=70, key="p15_a3")
            with c_q2:
                st.text_area("Co bych musel/a zjistit, než bych začal/a?", height=70, key="p15_a4")
                st.text_area("Podle čeho poznám, že můj nápad má smysl?", height=70, key="p15_a5")

        with st.container(border=True):
            st.markdown("### 15.3 Podnikání jako příběh: od problému k odpovědnosti")
            st.write("""
            Představ si, že studentka založí malý projekt: vyrábí personalizované studijní plánovače pro spolužáky. Na začátku to vypadá jednoduše. Má nápad, grafický program a několik lidí, kteří říkají, že by si plánovač koupili. Jenže podnikání nezačíná až fakturou. Začíná otázkami:
            
            * Kdo přesně je zákazník a jaký problém řeší?
            * Kolik je ochoten zaplatit a kolik stojí výroba?
            * Kdo vlastní grafiku a jak se budou řešit reklamace?
            * Je to jednorázová akce, nebo soustavná činnost?
            
            Tento příklad ukazuje, proč se v kapitole propojují právní formy, finance, marketing, etika a rizika. V reálném životě nejsou oddělené.
            """)

            st.markdown("""
            <div class='box-purple'>
                <strong>🧠 Důležitá myšlenka:</strong> Podnikání není jen „mít nápad a vydělat“. Podnikání je schopnost převést nápad do odpovědného systému, který vytváří hodnotu pro zákazníka a zároveň zvládá pravidla, rizika a dopady.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 15.4 Podnikatel očima různých lidí")
            st.write("Jedna firma může vypadat jinak podle toho, kdo se na ni dívá.")

            st.markdown("""
            | Kdo se dívá | Co ho zajímá | Proč je to důležité |
            | :--- | :--- | :--- |
            | **Zákazník** | Cena, kvalita, důvěryhodnost, reklamace. | Zákazník rozhoduje, jestli firma získá tržby. |
            | **Podnikatel** | Zisk, náklady, čas, riziko, růst. | Podnikatel nese následky rozhodnutí. |
            | **Zaměstnanec** | Mzda, pracovní podmínky, jistota. | Bez lidí firma často nedokáže růst. |
            | **Stát** | Daně, odvody, zákonnost. | Podnikání se odehrává v právním systému. |
            | **Banka / Investor** | Schopnost splácet, růst, tým, návratnost. | Posuzují riziko financování a šanci na hodnotu. |
            | **Obec / Společnost**| Služby, dopad na okolí, udržitelnost. | Firma může vytvářet hodnotu, ale i škody. |
            """)

        with st.container(border=True):
            st.markdown("### 15.5 OSVČ a cena práce: Hodinová sazba není kapesné")
            st.write("""
            Mnoho začínajících podnikatelů si špatně nastaví cenu. Řeknou si: „Chci 200 Kč za hodinu.“ Jenže v ceně musí být i čas, který zákazník nevidí: komunikace, příprava, úpravy, fakturace, vzdělávání, marketing, administrativa, opravy chyb, neproplacené poptávky a čas bez zakázek. Pokud si OSVČ nastaví příliš nízkou cenu, může mít hodně práce, ale málo peněz.
            """)

            st.markdown("#### 🧮 Aktivita: Kolik má stát moje hodina?")
            st.write("Představ si, že chceš jako OSVČ vydělat 30 000 Kč měsíčně hrubého a můžeš reálně fakturovat 90 hodin. Spočítej to krok za krokem:")
            
            c_calc1, c_calc2 = st.columns(2)
            with c_calc1:
                st.text_input("Základní sazba (30 000 / 90):", placeholder="Napiš svůj výpočet...", key="p15_calc1")
                st.text_input("Když přidáš 20 % na náklady (např. SW, doprava):", placeholder="Přičti k základu 20 %...", key="p15_calc2")
            with c_calc2:
                st.text_input("Když přidáš dalších 15 % jako rezervu na období bez zakázek:", placeholder="Přičti dalších 15 %...", key="p15_calc3")
                st.text_input("Byl by zákazník ochoten toto zaplatit?", placeholder="Tvůj názor...", key="p15_calc_opin")

        with st.container(border=True):
            st.markdown("### 15.6 Obchodní korporace jako systém pravidel")
            st.write("""
            S.r.o. umožňuje oddělit podnikání od soukromého života zakladatelů, přibrat společníky a nastavit podíly. Nejčastější chybou začínajících týmů je, že řeší produkt a logo, ale neřeší pravidla mezi zakladateli. Pokud projekt začne vydělávat nebo se dostane do problémů, nejasná dohoda může být větším rizikem než konkurence.
            """)

            st.markdown("""
            <div class='box-red'>
                <strong>⚖️ Zakladatelská otázka:</strong> Co se stane, když jeden člověk pracuje na projektu každý den a druhý skoro vůbec, ale oba mají stejný podíl?
            </div>
            """, unsafe_allow_html=True)

            st.markdown("#### 🤝 Aktivita: Zakladatelská dohoda v jedné stránce")
            st.write("Vytvořte jednoduchou dohodu pro váš tým:")

            st.text_area("Název projektu, role členů a rozdělení práce:", height=60, key="p15_doc_1")
            st.text_area("Pravidla pro peníze a vlastnictví výstupů (grafika, web):", height=60, key="p15_doc_2")
            st.text_area("Postup při odchodu člena a řešení konfliktu:", height=60, key="p15_doc_3")

        with st.container(border=True):
            st.markdown("### 15.7 Podnikatelský záměr a Lean Canvas v praxi")
            st.write("""
            Podnikatelský záměr nemá být slohová práce. Dobře napsaný záměr ukazuje, komu pomáháme, s čím, za kolik a jaká jsou rizika. Lean Canvas je užitečný právě proto, že startup na začátku nezná všechny odpovědi — slouží k zapsání hypotéz a jejich testování.
            """)

            st.markdown("#### 🧪 Aktivita: Přepiš domněnku na hypotézu")
            st.write("Přepiš obecné věty na ověřitelné hypotézy s měřitelným testem:")

            st.text_input("„Studentům se náš produkt bude líbit.“ ->", placeholder="Hypotéza a test...", key="p15_hyp1")
            st.text_input("„Lidé za to zaplatí.“ ->", placeholder="Hypotéza a test...", key="p15_hyp2")
            st.text_input("„Instagram nám přivede zákazníky.“ ->", placeholder="Hypotéza a test...", key="p15_hyp3")

        with st.container(border=True):
            st.markdown("### 15.8 Ekonomika sdílení")
            st.write("""
            Ekonomika sdílení je model, ve kterém lidé nebo firmy umožňují ostatním využívat majetek, prostor, čas nebo službu, které by jinak zůstaly nevyužité (např. Airbnb, Uber, Coworking). Digitální platforma zprostředkovává důvěru a bere si poplatek.
            """)

            st.markdown("""
            | Model | Viditelné náklady | Skryté nebo podceňované náklady |
            | :--- | :--- | :--- |
            | **Krátkodobé ubytování** | Úklid, energie, poplatek platformě | Opotřebení, opravy, čas komunikace, pojištění, prázdné noci, daně. |
            | **Přeprava (Uber)** | Palivo, servis auta, provize | Amortizace vozu, čekání bez jízdy, riziko nízké poptávky. |
            """)

            st.markdown("""
            <div class='box-blue'>
                <strong>Jednoduché pravidlo:</strong> V ekonomice sdílení se podnikatel neptá jen „kolik dostanu za transakci“, ale hlavně „kolik mi zůstane po odečtení všech nákladů, času, rizika a neobsazené kapacity“.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 15.9 CSR, etika a švarcsystém")
            st.write("""
            Odpovědné podnikání se nesmí zredukovat na fráze. Firma musí umět doložit, co měří a jak chrání zaměstnance, zákazníky a přírodu. Greenwashing vzniká, když firma působí ekologičtěji, než jaká ve skutečnosti je.

            Švarcsystém je otázka férovosti a zákonnosti. Pokud se pracovník formálně tváří jako OSVČ, ale fakticky funguje jako zaměstnanec (pevná doba, firemní notebook, jeden zadavatel), jedná se o nelegální švarcsystém.
            """)

            st.markdown("#### 🕵️ Aktivita: Detektiv švarcsystému")
            st.write("Která z těchto situací je riziková?")
            svarc_opt = st.radio("Vyberte případ:", [
                "A) Grafik s vlastním ateliérem, 5 klienty a vlastní technikou.",
                "B) Lektor, který fakturuje za konkrétní odučený kurz podle své osnovy.",
                "C) Programátor s IČO, který musí být v kanceláři jedné firmy od 9 do 17 na firemním notebooku."
            ])
            if st.button("Vyhodnotit případ"):
                if "C)" in svarc_opt:
                    st.markdown("<div class='box-red'><strong>Správně!</strong> Toto je ukázkový švarcsystém (pravidelná pracovní doba, vybavení firmy, jediný zadavatel, nesamostatnost).</div>", unsafe_allow_html=True)
                else:
                    st.markdown("<div class='box-yellow'>Toto se zdá být legitimní freelancing. Zkuste hledat znaky závislé práce.</div>", unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 15.10 Závěrečný velký úkol: Podnikatelská mise")
            st.write("Tento úkol propojuje celou kapitolu. Vytvoř komplexní návrh svého projektu a propoj všechny disciplíny:")

            st.checkbox("Zákazník a definovaný problém.")
            st.checkbox("Ověřitelné MVP a Lean Canvas.")
            st.checkbox("Zvolená právní forma s argumentací (OSVČ vs s.r.o.).")
            st.checkbox("Rozpočet, cenotvorba a bod zvratu.")
            st.checkbox("Marketing s ohledem na reálné konverze (nejen lajky).")
            st.checkbox("Riziková matice (co když se to pokazí).")
            st.checkbox("Etický kodex a vyhnutí se greenwashingu a švarcsystému.")

            st.markdown("""
            <div class='box-green'>
                <strong>🎉 Shrnutí kapitoly 1:</strong> Podnikání je praktická kombinace odvahy, znalostí a odpovědnosti. Nestačí mít nápad. Je potřeba rozumět zákazníkovi, právní formě, penězům, rizikům, datům, etice a dopadům. Ať už budeš podnikat nebo ne, tyto dovednosti ti pomohou orientovat se v moderním světě.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 🧠 15.11 Interaktivní Kvíz: Závěrečné ověření")
            st.write("Otestuj si své znalosti ze všech částí Kapitoly 1. Kliknutím na otázku se rozbalí správná odpověď s vysvětlením.")

            with st.expander("❓ 1. Student vyrábí o víkendech náramky. Když je prodá kamarádům, výnos si nechá. Když je nikdo nekoupí, přišel o peníze za korálky. O který znak podnikání se jedná?"):
                st.markdown("<div class='box-blue'><strong>Odpověď: B) Vlastní odpovědnost.</strong><br>Podnikatel nese riziko ztráty, neprodaných zásob nebo špatných rozhodnutí sám za sebe.</div>", unsafe_allow_html=True)

            with st.expander("❓ 2. Jaký je zásadní rozdíl v ručení za dluhy mezi OSVČ a společníkem v s.r.o.?"):
                st.markdown("<div class='box-blue'><strong>Odpověď: C) OSVČ ručí celým osobním majetkem, společník s.r.o. ručí omezeně.</strong><br>Pokud se OSVČ dostane do dluhů, může přijít o osobní úspory. Firma s.r.o. funguje jako oddělená právnická osoba.</div>", unsafe_allow_html=True)

            with st.expander("❓ 3. Co přesně znamená zkratka MVP v metodice Lean Startup?"):
                st.markdown("<div class='box-blue'><strong>Odpověď: Minimum Viable Product.</strong><br>Je to nejmenší a nejjednodušší verze produktu, která umožní levně ověřit zájem zákazníků.</div>", unsafe_allow_html=True)

            with st.expander("❓ 4. Proč by měl Lean Canvas začínat blokem Problém a Zákazník, a ne blokem Řešení?"):
                st.markdown("<div class='box-blue'><strong>Odpověď: Aby tým nestrávil měsíce vývojem produktu, který nikdo nepotřebuje.</strong><br>Častý důvod selhání startupů je, že ignorují reálný problém zákazníka.</div>", unsafe_allow_html=True)

            with st.expander("❓ 5. Rozhodovací situace: Grafička dostala nabídku od agentury. Má si založit IČO, sedět v kanceláři agentury od 9 do 17 na jejich počítači a plnit úkoly od šéfa. Co hrozí?"):
                st.markdown("<div class='box-red'><strong>Odpověď: Hrozí švarcsystém.</strong><br>Pracovní vztah vykazuje všechny znaky závislé práce. Agentura tím nelegálně obchází zákoník práce.</div>", unsafe_allow_html=True)

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
        "2.3 Algoritmy bohatství",
        "2.4 Matematika peněz",
        "2.5 Finanční rezerva",
        "2.6 Psychologie utrácení",
        "2.7 Finanční trh a analýza rizik",
        "2.8 Spoření, investování a spekulace",
        "2.9 Cenné papíry v praxi",
        "2.10 Kryptoměny",
        "2.11 Úvěry, pojištění a majetek",
        "2.12 Finanční řízení podniku",
        "2.13 Finanční analýza: E-shop DropZone",
        "2.14 Závěrečné interaktivní opakování"
    ]

    selected_section_2 = st.selectbox("📌 Přechod na podkapitolu (Vyberte téma):", section_options_2, index=0)
    st.divider()

    if selected_section_2 == "2.1 Bankovní systém a peníze":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.1</div>", unsafe_allow_html=True)
        st.markdown("## Bankovní systém a peníze v 21. století")
        
        with st.container(border=True):
            st.write("21. století není jen éra umělé inteligence a sociálních sítí. Je to především éra totální transformace toho, jak vnímáme hodnotu.")
            st.markdown("""
            <div class='box-blue'>
                <strong>Peníze jako digitální data:</strong> Peníze dnes často nevypadají jako mince nebo bankovky. V bankovním systému se změní digitální záznam: jednomu účtu se částka odečte a druhému připíše.
            </div>
            """, unsafe_allow_html=True)

            st.markdown("### Proč peníze vůbec vznikly")
            st.write("""
            Na úplném začátku lidé používali naturální směnu — vyměňovali zboží za zboží nebo službu za službu. 
            Problém byl v tom, že směna fungovala jen tehdy, když se potkaly dvě potřeby najednou. Tomu se říká **dvojí shoda potřeb**.
            """)

            st.markdown("""
            | Forma peněz | Výhoda | Problém |
            | :--- | :--- | :--- |
            | **Dobytek, obilí, sůl** | Lidé je uměli použít v běžném životě. | Špatně se dělily, skladovaly nebo převážely. |
            | **Mušle, kožešiny, vzácné předměty** | Byly rozpoznatelné a někde společensky ceněné. | Jejich hodnota závisela na místě a zvyklostech. |
            | **Zlato a stříbro** | Byly vzácné, trvanlivé a dobře dělitelné. | Bylo nutné ověřovat ryzost a hmotnost. |
            """)

            st.text_input("🧩 Interaktivní výzva: Vyber jednu komoditu, která by mohla sloužit jako peníze. Napiš, v čem by byla praktická a v čem by selhávala:", placeholder="Vybraná komodita a hodnocení...", key="c2_comodity")

        with st.container(border=True):
            st.markdown("### ČNB a komerční banky")
            st.markdown("""
            <div class='box-gray'>
                <strong>Základní rozlišení:</strong><br>
                • <strong>Česká národní banka (ČNB)</strong> je centrální banka ČR. Nejde o běžnou banku pro občany. Hlídá stabilitu měny a finančního systému.<br>
                • <strong>Komerční banky</strong> vedou účty, přijímají vklady, poskytují úvěry a zajišťují platby pro lidi a firmy.
            </div>
            """, unsafe_allow_html=True)

            st.write("**Hlavním cílem ČNB je péče o cenovou stabilitu.** Se snaží, aby peníze neztrácely hodnotu příliš rychle a aby inflace nebyla dlouhodobě příliš vysoká ani nebezpečně nízká.")

            with st.expander("🎮 Interaktivní simulace: Jsi bankovní rada ČNB"):
                st.write("**Situace:** Inflace je vysoká, lidé si stěžují na zdražování, hypotéky jsou drahé a firmy říkají, že zákazníci méně utrácejí. Tvoje skupina představuje bankovní radu ČNB.")
                cnb_decision = st.radio("Rozhodněte:", ["Zvýšíte úrokové sazby", "Snížíte úrokové sazby", "Ponecháte sazby beze změny"])
                if st.button("Uložit rozhodnutí"):
                    if "Zvýšíte" in cnb_decision:
                        st.success("Tímto krokem brzdíte inflaci (úvěry zdraží, lidé budou více spořit), ale ekonomika se může zpomalit.")
                    else:
                        st.warning("Toto rozhodnutí může podpořit utrácení, ale riziko vysoké inflace zůstává.")

    elif selected_section_2 == "2.2 Osobní finance a rozpočet":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.2</div>", unsafe_allow_html=True)
        st.markdown("## Osobní finance a rozpočet")
        
        with st.container(border=True):
            st.write("Osobní finance nejsou jen otázka toho, kolik člověk vydělává. Jsou to každodenní rozhodnutí: za co utratím peníze, co odložím, co si půjčím, jak poznám riziko a jak se nenechám řídit reklamou.")
            
            st.markdown("""
            **Rozpočet: mapa peněz**<br>
            Rozpočet ukazuje, odkud peníze přicházejí a kam odcházejí. Bez rozpočtu člověk často neví, jestli má problém s nízkými příjmy, vysokými výdaji, impulzivním utrácením, dluhy nebo chybějící rezervou.
            """)

            st.markdown("""
            | Typ výdaje | Příklad | Otázka ke kontrole |
            | :--- | :--- | :--- |
            | **Fixní výdaj** | nájem, paušál, předplatné, splátka | Opravdu ho potřebuji každý měsíc? |
            | **Proměnlivý výdaj** | jídlo, doprava, drogerie, zábava | Dá se upravit bez zásadního poklesu kvality života? |
            | **Jednorázový výdaj** | telefon, oprava, dovolená | Mám na něj připravené peníze dopředu? |
            | **Skrytý výdaj** | automatické předplatné, poplatky | Vím, kolik mě stojí za rok? |
            """)

            st.markdown("""
            <div class='box-green'>
                <strong>Jednoduché pravidlo pro rozpočet (50–30–20):</strong><br>
                • 50 % na potřeby<br>
                • 30 % na přání<br>
                • 20 % na rezervu, spoření nebo splácení dluhů
            </div>
            """, unsafe_allow_html=True)

    elif selected_section_2 == "2.3 Algoritmy bohatství":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.3</div>", unsafe_allow_html=True)
        st.markdown("## Algoritmy bohatství: malé návyky, velký rozdíl")
        
        with st.container(border=True):
            st.write("Slovo „algoritmus“ tu neznamená počítačový program. Znamená opakovatelný postup, který člověku pomáhá rozhodovat se lépe. Bohatství nevzniká jen jedním velkým rozhodnutím. Často vzniká z malých pravidelných kroků, které se opakují dlouhou dobu.")
            
            st.markdown("""
            <div class='box-blue'>
                <strong>Algoritmus finanční stability:</strong><br>
                1. Nejdřív zaplať nutné výdaje.<br>
                2. Hned po příjmu odlož část peněz stranou.<br>
                3. Utrať jen to, co zůstane po odložení rezervy.<br>
                4. Vyhýbej se drahému dluhu.<br>
                5. Pravidelně kontroluj, kam peníze mizí.
            </div>
            """, unsafe_allow_html=True)

            st.write("**Zaplať nejdřív sobě:** Část peněz si odlož hned po přijetí příjmu, ne až na konci měsíce (kdy už většinou nic nezbyde).")

    elif selected_section_2 == "2.4 Matematika peněz":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.4</div>", unsafe_allow_html=True)
        st.markdown("## Matematika peněz: čas, úrok a inflace")
        
        with st.container(border=True):
            st.write("Peníze mají časovou hodnotu. Stokoruna dnes nemá stejnou hodnotu jako stokoruna za deset let, protože ceny se mění a peníze mohou nést úrok nebo výnos.")

            st.markdown("### Jednoduché a Složené úročení")
            st.markdown("""
            * **Jednoduché úročení:** úrok se počítá stále jen z původně vložené nebo půjčené částky.
            * **Složené úročení:** úročí se nejen původní částka, ale postupně i již připsané úroky nebo výnosy. Peníze tedy mohou vydělávat další peníze.
            """)

            st.markdown("""
            | Typ úročení | Z čeho se počítá úrok | Výsledek při 10 000 Kč, 5 % ročně, 3 roky |
            | :--- | :--- | :--- |
            | **Jednoduché úročení** | Pořád z původní částky | 11 500 Kč |
            | **Složené úročení** | Z původní částky i z připsaných úroků | 11 576,25 Kč |
            """)

            st.markdown("### Inflace")
            st.write("Inflace znamená růst cenové hladiny. Když ceny rostou, za stejnou částku si koupíme méně než dříve.")
            st.text_input("🧩 Interaktivní výzva: Vyber pět věcí, které pravidelně kupuješ. Zjisti nebo odhadni, kolik stály dříve a kolik stojí dnes. Která položka zdražila nejvíc?", placeholder="Moje položky...", key="c2_inflation")

    elif selected_section_2 == "2.5 Finanční rezerva":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.5</div>", unsafe_allow_html=True)
        st.markdown("## Finanční rezerva: airbag osobních financí")
        
        with st.container(border=True):
            st.write("Finanční rezerva chrání člověka před tím, aby každá nečekaná situace skončila dluhem. Může jít o rozbitý telefon, ztrátu brigády, nemoc, opravu auta, vyšší vyúčtování energií nebo stěhování.")

            st.markdown("""
            | Životní situace | První rozumný cíl | Silnější rezerva |
            | :--- | :--- | :--- |
            | **Student s podporou rodiny** | 1 000–5 000 Kč | 1 měsíc vlastních výdajů |
            | **Člověk na brigádě nebo první práci** | 1 měsíc nutných výdajů | 3 měsíce nutných výdajů |
            | **Samostatně žijící člověk** | 3 měsíce nutných výdajů | 6 měsíců nutných výdajů |
            | **Rodina nebo podnikatel** | 3–6 měsíců nutných výdajů | více podle rizika příjmů |
            """)

            st.markdown("""
            <div class='box-red'>
                <strong>Častá chyba:</strong> Investovat nouzovou rezervu do rizikových aktiv. Když pak přijde problém, může být člověk nucen prodat v nevýhodnou chvíli se ztrátou.
            </div>
            """, unsafe_allow_html=True)

    elif selected_section_2 == "2.6 Psychologie utrácení":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.6</div>", unsafe_allow_html=True)
        st.markdown("## Psychologie utrácení: proč nerozhodujeme vždy racionálně")
        
        with st.container(border=True):
            st.write("Lidé nejsou kalkulačky. Často se rozhodujeme podle emocí, únavy, tlaku okolí, reklamy, strachu, že něco propásneme, nebo podle toho, co nám ukáže aplikace.")

            st.markdown("""
            | Past | Jak funguje | Obrana |
            | :--- | :--- | :--- |
            | **FOMO** | Strach, že mi něco uteče. | Počkej 24 hodin před nákupem. |
            | **Sleva** | Pocit úspory, i když kupuji zbytečnost. | Ptej se: koupil/a bych to i bez slevy? |
            | **Sociální srovnávání** | Chci životní styl, který vidím u ostatních. | Rozliš realitu a vybraný obsah na sítích. |
            | **Mikrotransakce** | Malé částky vypadají neškodně. | Spočítej roční součet. |
            | **Odložená platba** | Nákup nebolí hned. | Ber ji jako dluh, ne jako slevu. |
            """)

            st.markdown("### Kalkulačka času: kolik života stojí nákup")
            st.write("Cena věci není jen částka v korunách. Dá seNa něco takového nejsem naprogramovaný.
