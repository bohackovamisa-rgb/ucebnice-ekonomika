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

# --- STYLOVÁNÍ (MONTSERRAT + SAAS MINIMALISMUS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Montserrat', sans-serif !important;
    }

    .stApp {
        background-color: #f8fafc;
        color: #0f172a;
    }

    .main .block-container {
        max-width: 880px !important;
        padding-top: 2.5rem !important;
        padding-bottom: 5rem !important;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #ffffff !important;
        border-radius: 12px !important;
        border: 1px solid #e2e8f0 !important;
        box-shadow: 0 1px 3px 0 rgba(15, 23, 42, 0.03) !important;
        padding: 1.75rem !important;
        margin-bottom: 1.25rem !important;
    }

    h1 {
        font-family: 'Montserrat', sans-serif !important;
        color: #0f172a !important;
        font-weight: 800 !important;
        font-size: 2.1rem !important;
        letter-spacing: -0.02em !important;
        line-height: 1.25 !important;
        margin-bottom: 0.5rem !important;
    }

    h2 {
        font-family: 'Montserrat', sans-serif !important;
        color: #1e293b !important;
        font-weight: 700 !important;
        font-size: 1.25rem !important;
        letter-spacing: -0.01em !important;
        margin-top: 1.5rem !important;
        margin-bottom: 0.75rem !important;
        border-bottom: 1px solid #f1f5f9;
        padding-bottom: 0.4rem;
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
        font-size: 0.95rem;
        line-height: 1.7;
        font-weight: 400;
    }

    /* LEGENDA UČEBNICE */
    .box-blue {
        background-color: #f0f9ff;
        border-left: 3px solid #0284c7;
        padding: 1rem 1.25rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
        color: #0369a1;
        font-size: 0.93rem;
    }
    
    .box-yellow {
        background-color: #fefce8;
        border-left: 3px solid #eab308;
        padding: 1rem 1.25rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
        color: #854d0e;
        font-size: 0.93rem;
    }

    .box-purple {
        background-color: #faf5ff;
        border-left: 3px solid #a855f7;
        padding: 1rem 1.25rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
        color: #6b21a8;
        font-size: 0.93rem;
        word-wrap: break-word;
    }

    .box-green {
        background-color: #f0fdf4;
        border-left: 3px solid #22c55e;
        padding: 1rem 1.25rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
        color: #166534;
        font-size: 0.93rem;
    }

    .box-red {
        background-color: #fef2f2;
        border-left: 3px solid #ef4444;
        padding: 1rem 1.25rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
        color: #991b1b;
        font-size: 0.93rem;
    }

    .box-gray {
        background-color: #f8fafc;
        border-left: 3px solid #64748b;
        padding: 1rem 1.25rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
        color: #334155;
        font-size: 0.93rem;
    }

    .icon-inline {
        display: inline-flex;
        align-items: center;
        margin-right: 8px;
        vertical-align: -3px;
    }

    .stTextInput input, .stTextArea textarea, .stSelectbox select {
        font-family: 'Montserrat', sans-serif !important;
        border-radius: 8px !important;
        border: 1px solid #cbd5e1 !important;
        background-color: #ffffff !important;
        color: #0f172a !important;
        font-size: 0.9rem !important;
        padding: 0.6rem 0.8rem !important;
    }

    .stButton > button {
        font-family: 'Montserrat', sans-serif !important;
        border-radius: 8px !important;
        border: 1px solid #cbd5e1 !important;
        background-color: #ffffff !important;
        color: #1e293b !important;
        font-weight: 600 !important;
        font-size: 0.85rem !important;
        padding: 0.5rem 1rem !important;
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
        margin-top: 1.2rem;
        margin-bottom: 0.4rem;
    }

    button[data-baseweb="tab"] {
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 600 !important;
        font-size: 0.88rem !important;
    }

    .sub-section-header {
        color: #4f46e5;
        font-weight: 700;
        font-size: 0.85rem;
        letter-spacing: 0.05em;
        text-transform: uppercase;
    }
    </style>
""", unsafe_allow_html=True)

# --- MODERNÍ LINETYPE SVG IKONY ---
SVG_COMPASS = '<svg class="icon-inline" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#4f46e5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>'
SVG_TARGET = '<svg class="icon-inline" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>'
SVG_BOOK = '<svg class="icon-inline" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#4f46e5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>'

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
    st.markdown("<span style='color: #6366f1; font-weight: 700; font-size: 0.8rem; letter-spacing: 0.08em;'>DIGITÁLNÍ UČEBNICE</span>", unsafe_allow_html=True)
    st.title("Ekonomika, která dává smysl")
    st.markdown("<p style='font-size: 1.05rem; color: #64748b; margin-bottom: 2rem;'>Moderní učebnice ekonomiky pro střední školy: Podnikavost, finance & ekonomika v souvislostech.</p>", unsafe_allow_html=True)

    with st.container(border=True):
        st.markdown(f"<h2>{SVG_COMPASS} Začni tady</h2>", unsafe_allow_html=True)
        st.write("""
        Tahle stránka je hlavní rozcestník učebnice. Najdeš tu obsah, pravidla práce, výstupy kapitol, 
        společné nástroje a odkaz do učitelského řídícího centra. Propojuje podnikavost, osobní finance, výrobu, 
        trh práce, stát, daně, management a marketing s rozhodnutími z reálného života.
        """)
        
        st.markdown(f"""
        <div class='box-green'>
            <strong>{SVG_TARGET} Cíl učebnice:</strong><br>
            Žák má umět propojit nápad, zákazníka, peníze, práci, stát, daně, marketing, rizika a odpovědnost do jednoho praktického rozhodování.
        </div>
        """, unsafe_allow_html=True)

    with st.container(border=True):
        st.markdown(f"<h2>{SVG_BOOK} Jak s učebnicí pracovat</h2>", unsafe_allow_html=True)
        st.markdown("""
        1. **Otevři kapitolu z obsahu.** Nejprve si projdi úvod, rychlou orientaci a cíle kapitoly.
        2. **Čti po menších blocích.** Každá kapitola je členěná na výklad, příklady, tabulky, aktivity a reflexi.
        3. **Plň průběžné úkoly.** Žluté bloky slouží jako pracovní úkoly, otázky a aktivity.
        4. **Používej AI mentoring.** Fialové bloky obsahují prompty, které pomáhají s vysvětlením, kontrolou nebo rozvojem vlastního projektu.
        5. **Na konci kapitoly udělej reflexi.** Shrň, co už chápeš, co ještě potřebuješ dovysvětlit a jak bys téma použil/a v praxi.
        6. **V závěrečném projektu propojíš všechno dohromady.** Výstupem učebnice je návrh odpovědného ekonomického nebo podnikatelského projektu.
        """)

elif view == "Kapitola 1":
    st.markdown("<span style='color: #6366f1; font-weight: 700; font-size: 0.8rem; letter-spacing: 0.08em;'>KAPITOLA 1</span>", unsafe_allow_html=True)
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
            st.markdown("### 🟡 Tvůj úkol: Je to podnikání?")
            st.write("U každé situace rozhodni, zda jde spíš o koníček, jednorázový přivýdělek, zaměstnání, nebo podnikání. Zdůvodni odpověď podle čtyř znaků podnikání.")

            ex1 = st.selectbox("1. Student jednou prodá starý mobil:", ["Vyber odpověď...", "Koníček", "Jednorázový přivýdělek", "Zaměstnání", "Podnikání"], key="p1_ex1")
            ex2 = st.selectbox("2. Student každý týden prodává vlastnoručně vyráběné náramky přes Instagram:", ["Vyber odpověď...", "Koníček", "Jednorázový přivýdělek", "Zaměstnání", "Podnikání"], key="p1_ex2")
            ex3 = st.selectbox("3. Student pracuje v kavárně podle rozpisu směn:", ["Vyber odpověď...", "Koníček", "Jednorázový přivýdělek", "Zaměstnání", "Podnikání"], key="p1_ex3")
            ex4 = st.selectbox("4. Student nabízí grafiku loga pro malé podniky a sám si domlouvá cenu:", ["Vyber odpověď...", "Koníček", "Jednorázový přivýdělek", "Zaměstnání", "Podnikání"], key="p1_ex4")
            ex5 = st.selectbox("5. Student vytvoří placený online kurz pro mladší žáky:", ["Vyber odpověď...", "Koníček", "Jednorázový přivýdělek", "Zaměstnání", "Podnikání"], key="p1_ex5")

            if st.button("Uložit vyhodnocení úkolu"):
                st.success("Odpovědi byly uloženy do vašeho profilu pokroků!")

        with st.container(border=True):
            st.markdown("### 📝 Interaktivní výzva: vlastní nápad")
            user_idea = st.text_area("Popiš svůj nápad jednou větou a označ, jak v něm bude vidět soustavnost, samostatnost a odpovědnost:", placeholder="Můj nápad je...", height=100, key="p1_user_idea")
            if st.button("Uložit můj nápad"):
                st.success("Nápad uložen!")

        # AI MENTORING - FIALOVÉ BOXY BEZ POSUVOVÁNÍ KURZOREM
        with st.container(border=True):
            st.markdown("### 🟣 AI mentoring k podnikání")
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

    elif selected_section == "2. Slovníček základních pojmů":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2</div>", unsafe_allow_html=True)
        st.markdown("## 2. Slovníček základních pojmů")
        
        with st.container(border=True):
            st.markdown("""
            • **Podnikatel:** Osoba samostatně vykonávající výdělečnou činnost na vlastní účet a odpovědnost.<br>
            • **Fyzická osoba:** Člověk – jednotlivec (v podnikání typicky jako OSVČ).<br>
            • **Právnická osoba:** Organizovaný subjekt (např. s.r.o., a.s., spolek).<br>
            • **OSVČ:** Osoba samostatně výdělečně činná.<br>
            • **Živnostenské oprávnění:** Právo provozovat živnost získané ohlášením nebo koncesí.
            """, unsafe_allow_html=True)

    elif selected_section == "3. OSVČ a živnosti":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 3</div>", unsafe_allow_html=True)
        st.markdown("## 3. OSVČ a živnosti")
        
        with st.container(border=True):
            st.write("OSVČ je fyzická osoba podnikající vlastním jménem na vlastní odpovědnost celým svým majetkem.")
            st.markdown("<div class='box-red'><strong>Hlavní riziko OSVČ:</strong> Ručení za závazky celým osobním majetkem.</div>", unsafe_allow_html=True)

            st.markdown("### Druhy živností")
            st.markdown("""
            1. **Volná:** Bez nutnosti kvalifikace (např. e-shop, marketing).
            2. **Řemeslná:** Vyžaduje výuční list nebo praxi (např. truhlář, kadeřník).
            3. **Vázaná:** Vyžaduje odbornou způsobilost podle zákona (např. autoškola).
            4. **Koncesovaná:** Vyžaduje státní koncesi (např. taxislužba).
            """)

        with st.container(border=True):
            st.markdown("### 🧮 Hodinová sazba OSVČ (Simulace)")
            c1, c2 = st.columns(2)
            with c1:
                prijem = st.number_input("Požadovaný čistý příjem (Kč):", value=35000, step=1000)
                naklady = st.number_input("Měsíční náklady (Kč):", value=5000, step=500)
            with c2:
                hodiny = st.number_input("Odpracované hodiny za měsíc:", value=110, step=10)
                odvody = 8311

            sazba = (prijem + naklady + odvody) / hodiny if hodiny > 0 else 0
            st.markdown(f"<div class='box-green'>Minimální potřebná sazba: <strong>{sazba:.0f} Kč / hod.</strong></div>", unsafe_allow_html=True)

    elif selected_section == "4. Obchodní korporace":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 4</div>", unsafe_allow_html=True)
        st.markdown("## 4. Obchodní korporace")
        
        with st.container(border=True):
            st.write("Obchodní korporace jsou právnické osoby zřízené podle ZOK (Zákon o obchodních korporacích).")
            
            c_k1, c_k2, c_k3 = st.columns(3)
            with c_k1:
                st.markdown("<div class='box-gray'><strong>Osobní společnosti</strong><br>• v.o.s., k.s.<br>• Neomezené ručení společníků.</div>", unsafe_allow_html=True)
            with c_k2:
                st.markdown("<div class='box-gray'><strong>Kapitálové společnosti</strong><br>• s.r.o., a.s.<br>• Oddělený majetek firmy.</div>", unsafe_allow_html=True)
            with c_k3:
                st.markdown("<div class='box-gray'><strong>Družstva</strong><br>• Družstvo, SCE<br>• Založeno na členství.</div>", unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 📊 Test: OSVČ, nebo s.r.o.?")
            q1_opt = st.radio("1. Plánuješ podnikat sám/sama, nebo v týmu?", ["Sám/sama (OSVČ)", "V týmu (s.r.o.)"], key="t1_new")
            q2_opt = st.radio("2. Hrozí projektem větší finanční závazky a škody?", ["Nízké riziko (OSVČ)", "Vysoké riziko / úvěry (s.r.o.)"], key="t2_new")

            if st.button("Vyhodnotit doporučenou formu"):
                if "s.r.o." in q1_opt or "s.r.o." in q2_opt:
                    st.markdown("<div class='box-blue'><strong>Doporučení:</strong> Pro váš projekt se jeví vhodnější <strong>s.r.o.</strong></div>", unsafe_allow_html=True)
                else:
                    st.markdown("<div class='box-green'><strong>Doporučení:</strong> Pro váš start je vhodnější <strong>OSVČ</strong>.</div>", unsafe_allow_html=True)

    elif selected_section == "5. Startup: nápad, který hledá byznys":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 5</div>", unsafe_allow_html=True)
        st.markdown("## 5. Startup: nápad, který hledá byznys")
        with st.container(border=True):
            st.write("Tato podkapitola je připravena pro vložení ČÁSTI 3 textu. (Čeká na zaslání podkladů).")

    elif selected_section == "6. Lean Canvas":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 6</div>", unsafe_allow_html=True)
        st.markdown("## 6. Lean Canvas")
        with st.container(border=True):
            st.write("Jednostránkový podnikatelský model zaměřený na rychlé testování hypotéz.")

    elif selected_section == "7. CSR, etika a odpovědné podnikání":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 7</div>", unsafe_allow_html=True)
        st.markdown("## 7. CSR, etika a odpovědné podnikání")
        with st.container(border=True):
            st.write("Společenská odpovědnost firem (ESG) a etické rozhodování v praxi.")

    elif selected_section == "8. Rizika podnikání":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 8</div>", unsafe_allow_html=True)
        st.markdown("## 8. Rizika podnikání")
        with st.container(border=True):
            st.write("Identifikace, matice rizik a preventivní opatření.")

    elif selected_section == "9. Švarcsystém":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 9</div>", unsafe_allow_html=True)
        st.markdown("## 9. Švarcsystém")
        with st.container(border=True):
            st.markdown("<div class='box-red'><strong>Pozor na švarcsystém:</strong> Zastřený pracovněprávní vztah je nelegální.</div>", unsafe_allow_html=True)

    elif selected_section == "10. Ověřování informací a užitečné zdroje":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 10</div>", unsafe_allow_html=True)
        st.markdown("## 10. Ověřování informací a užitečné zdroje")
        with st.container(border=True):
            st.write("Veřejné rejstříky: ARES, Obchodní rejstřík (Justice.cz), Živnostenský rejstřík (RŽP).")

    elif selected_section == "11. Ukončení podnikání":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 11</div>", unsafe_allow_html=True)
        st.markdown("## 11. Ukončení podnikání")
        with st.container(border=True):
            st.write("Zrušení, likvidace a zánik podniku.")

    elif selected_section == "12. Logická mapa podnikání":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 12</div>", unsafe_allow_html=True)
        st.markdown("## 12. Logická mapa podnikání")
        with st.container(border=True):
            st.write("Přehledná syntéza celé Kapitoly 1.")

    elif selected_section == "13. Reflexe a sebehodnocení":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 13</div>", unsafe_allow_html=True)
        st.markdown("## 13. Reflexe a sebehodnocení")
        with st.container(border=True):
            st.write("Vyhodnocení vlastní práce a posunu v kapitole.")

    elif selected_section == "14. Integrované opakování":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 14</div>", unsafe_allow_html=True)
        st.markdown("## 14. Integrované opakování")
        with st.container(border=True):
            st.write("Závěrečný test a souhrnné aktivity Kapitoly 1.")

elif view == "Pokroky":
    st.markdown("<span style='color: #6366f1; font-weight: 700; font-size: 0.8rem; letter-spacing: 0.08em;'>STUDENTSKÁ ZÓNÁ</span>", unsafe_allow_html=True)
    st.title("Moje pokroky")
    st.markdown("<p style='font-size: 1rem; color: #64748b; margin-bottom: 2rem;'>Přehled dokončených kapitol, uložených odpovědí a rozpracovaných projektů.</p>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        with st.container(border=True):
            st.metric(label="Dokončené kapitoly", value="1 / 6", delta="16 %")
    with c2:
        with st.container(border=True):
            st.metric(label="Test právní formy", value="Hotovo", delta="OSVČ vs s.r.o.")
    with c3:
        with st.container(border=True):
            st.metric(label="Aktivní kalkulace", value="OSVČ Sazba", delta="Dokončeno")

elif view == "Ucitel":
    st.markdown("<span style='color: #6366f1; font-weight: 700; font-size: 0.8rem; letter-spacing: 0.08em;'>METODIK & DASHBOARD</span>", unsafe_allow_html=True)
    st.title("Učitelská základna")
    st.markdown("<p style='font-size: 1rem; color: #64748b; margin-bottom: 2rem;'>Metodické pokyny a sledování práce jednotlivých žáků podle tříd.</p>", unsafe_allow_html=True)

    tab_prehled, tab_metodika = st.tabs(["Přehled žáků a tříd", "Metodické plány do hodin"])

    with tab_prehled:
        with st.container(border=True):
            st.header("Sledování práce žáků")
            col_treda, col_zak = st.columns(2)
            with col_treda:
                selected_class = st.selectbox("Vyberte třídu:", ["3.A (Obchodní akademie)", "3.B (Ekonomické lyceum)", "4.A (Podnikání)"])
            with col_zak:
                zaci_map = {
                    "3.A (Obchodní akademie)": ["Jan Novák", "Ema Dvořáková", "Petr Svoboda"],
                    "3.B (Ekonomické lyceum)": ["Klára Horáková", "Martin Černý"],
                    "4.A (Podnikání)": ["Lucie Kučerová", "David Veselý"]
                }
                selected_student = st.selectbox("Vyberte žáka:", zaci_map[selected_class])

            st.divider()

            st.subheader(f"Karta žáka: {selected_student} ({selected_class})")
            st.markdown("**Vyplněné úkoly Kapitoly 1:**")
            st.markdown("• Test právní formy: *Vyplněno*")
            st.text_area("Napsat žákovi poznámku / schválení záměru:", placeholder="Zpětná vazba...", key=f"note_{selected_student}")

    with tab_metodika:
        with st.container(border=True):
            st.header("Projektové aktivity do hodin (Kapitola 1)")
            st.write("Aktivita: Vyhledávání reálných firem v obchodním rejstříku Justice.cz.")

else:
    st.markdown("<span style='color: #6366f1; font-weight: 700; font-size: 0.8rem; letter-spacing: 0.08em;'>KAPITOLA</span>", unsafe_allow_html=True)
    st.title(chapters.get(view, view))
    with st.container(border=True):
        st.info("Tato kapitola čeká na vložení textu. Stačí poslat podklady.")
