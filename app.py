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
        "5. Startup: nápad, který hledá funkční byznys",
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
        st.markdown("## 1. Podnikatel a základní pojmy") #[cite: 1]
        
        with st.container(border=True):
            st.write("Zákon chápe podnikání jako soustavnou činnost prováděnou samostatně, vlastním jménem, na vlastní odpovědnost, za účelem dosažení zisku.") #[cite: 1]
            
            st.markdown("""
            <div class='box-gray'>
                <strong>⚖️ Přesná zákonná opora:</strong> Podnikatele definuje zákon č. 89/2012 Sb., občanský zákoník, zejména § 420 odst. 1: <br>„Kdo samostatně vykonává na vlastní účet a odpovědnost výdělečnou činnost živnostenským nebo obdobným způsobem se záměrem činit tak soustavně za účelem dosažení zisku, je považován se zřetelem k této činnosti za podnikatele.“<br><br>
                Jednoduše řečeno: Podnikatelem je ten, kdo podniká samostatně, na vlastní účet, na vlastní odpovědnost, dělá výdělečnou činnost soustavně a jejím cílem je zisk.
            </div>
            """, unsafe_allow_html=True) #[cite: 1]
            
            st.markdown("""
            <div class='box-blue'>
                <strong>📘 Proč je to důležité:</strong> Možná už máš nápad, něco prodáváš, tvoříš na zakázku nebo si jen přivyděláváš. Tady zjistíš, kdy už se z takové aktivity stává podnikání a proč je důležité poznat rozdíl mezi koníčkem, brigádou, OSVČ a firmou.
            </div>
            """, unsafe_allow_html=True) #[cite: 1]

        with st.container(border=True):
            st.markdown("### 1.1 Podnikatel v realitě současné generace") #[cite: 1]
            st.write("Podnikání dnes nemusí začínat kanceláří, provozovnou ani výrobní halou. Může začít mobilem, profilem na sociální síti, prodejem digitální šablony, správou obsahu pro lokální firmu, výrobou merch produktů, doučováním, e-shopem, aplikací, kurzem, grafickou službou, tvorbou videí nebo komunitním projektem.") #[cite: 1]
            st.write("Právě proto je důležité umět rozpoznat hranici mezi:") #[cite: 1]
            
            st.markdown("""
            * **koníčkem** — dělám něco pro radost, bez soustavného záměru vydělávat,
            * **jednorázovým přivýdělkem** — například prodám vlastní staré věci,
            * **brigádou nebo zaměstnáním** — pracuji podle pokynů zaměstnavatele,
            * **podnikáním** — samostatně nabízím produkt nebo službu, nesu riziko a chci dlouhodobě vydělávat.
            """, unsafe_allow_html=True) #[cite: 1]
            
            st.markdown("""
            <div class='box-blue'>
                <strong>📱 Příklad pro dnešní studenty:</strong> Když jednou prodáš staré tenisky, nejde obvykle o podnikání. Když ale pravidelně nakupuješ, upravuješ, propaguješ a prodáváš zboží se záměrem vydělat, už se blížíš podnikání a musíš řešit pravidla.
            </div>
            """, unsafe_allow_html=True) #[cite: 1]

        with st.container(border=True):
            st.markdown("### 1.2 Čtyři znaky podnikání na praktických příkladech") #[cite: 1]
            st.markdown("""
            | Znak podnikání | Co znamená | Příklad ze současnosti | Otázka pro žáka |
            | :--- | :--- | :--- | :--- |
            | **Soustavnost** | Činnost se opakuje nebo je plánovaná dlouhodobě. | Každý měsíc prodávám vlastní digitální plánovače. | Dělám to jednou, nebo z toho chci pravidelný příjem? |
            | **Samostatnost** | Sám/sama rozhoduji o ceně, zákaznících, způsobu práce a organizaci. | Nabízím správu sociálních sítí lokálním podnikům. | Kdo určuje, jak, kdy a pro koho pracuji? |
            | **Vlastní jméno** | Vystupuji vůči zákazníkům a úřadům jako podnikatel nebo firma. | Mám značku, profil, faktury, obchodní podmínky nebo IČO. | Kdo nese odpovědnost před zákazníkem? |
            | **Vlastní odpovědnost**| Nesu riziko ztráty, reklamací, dluhů a špatných rozhodnutí. | Nakoupím materiál na merch, ale nikdo si ho nekoupí. | Co se stane, když plán nevyjde? |
            """, unsafe_allow_html=True) #[cite: 1]

        with st.container(border=True):
            st.markdown("### 1.3 Podnikatel není jen „někdo, kdo vydělává“") #[cite: 1]
            st.write("Podnikatel vytváří hodnotu pro zákazníka. Peníze jsou důsledkem toho, že někdo považuje produkt nebo službu za užitečnou. Moderní podnikavost proto zahrnuje nejen prodej, ale i schopnost:") #[cite: 1]
            st.markdown("""
            * vidět problém,
            * navrhnout řešení,
            * ověřit zájem,
            * komunikovat férově,
            * počítat náklady a cenu,
            * nést odpovědnost,
            * učit se z chyb,
            * používat technologie bezpečně a smysluplně.
            """, unsafe_allow_html=True) #[cite: 1]

        with st.container(border=True):
            st.markdown("<div class='box-yellow'><strong>🧪 Tvůj úkol: Je to podnikání?</strong><br>U každé situace rozhodni, zda jde spíš o koníček, jednorázový přivýdělek, zaměstnání, nebo podnikání. Zdůvodni odpověď podle čtyř znaků podnikání.</div>", unsafe_allow_html=True) #[cite: 1]
            st.selectbox("1. Student jednou prodá starý mobil.", ["Vyber odpověď...", "Koníček", "Jednorázový přivýdělek", "Zaměstnání", "Podnikání"], key="p1_q1") #[cite: 1]
            st.selectbox("2. Student každý týden prodává vlastnoručně vyráběné náramky přes Instagram.", ["Vyber odpověď...", "Koníček", "Jednorázový přivýdělek", "Zaměstnání", "Podnikání"], key="p1_q2") #[cite: 1]
            st.selectbox("3. Student pracuje v kavárně podle rozpisu směn.", ["Vyber odpověď...", "Koníček", "Jednorázový přivýdělek", "Zaměstnání", "Podnikání"], key="p1_q3") #[cite: 1]
            st.selectbox("4. Student nabízí grafiku loga pro malé podniky a sám si domlouvá cenu.", ["Vyber odpověď...", "Koníček", "Jednorázový přivýdělek", "Zaměstnání", "Podnikání"], key="p1_q4") #[cite: 1]
            st.selectbox("5. Student vytvoří placený online kurz pro mladší žáky.", ["Vyber odpověď...", "Koníček", "Jednorázový přivýdělek", "Zaměstnání", "Podnikání"], key="p1_q5") #[cite: 1]

            st.markdown("""
            <div class='box-purple'>
                <strong>🤖 AI mentoring:</strong> „Zeptej se mě na můj nápad a podle čtyř znaků podnikání mi vysvětli, jestli už jde o podnikání. U každého znaku mi dej jednu kontrolní otázku.“
            </div>
            """, unsafe_allow_html=True) #[cite: 1]

            st.markdown("<div class='box-yellow'><strong>🧩 Interaktivní výzva:</strong> Popiš svůj nápad jednou větou a označ, jak v něm bude vidět soustavnost, samostatnost a odpovědnost.</div>", unsafe_allow_html=True) #[cite: 1]
            st.text_area("Tvoje odpověď:", key="p1_idea") #[cite: 1]

            st.markdown("""
            <div class='box-purple'>
                <strong>🤖 AI mentoring:</strong> Zkopíruj tento prompt do AI asistenta: „Pomoz mi rozlišit, jestli je můj nápad spíš jednorázová aktivita, nebo skutečné podnikání.“
            </div>
            """, unsafe_allow_html=True) #[cite: 1]

            st.markdown("""
            <div class='box-blue'>
                <strong>📌 Základní definice:</strong> Podnikání není jednorázová aktivita. Je to dlouhodobá, samostatná a odpovědná činnost, při které podnikatel vystupuje vlastním jménem a usiluje o zisk.
            </div>
            """, unsafe_allow_html=True) #[cite: 1]

            st.markdown("""
            <div class='box-blue'>
                <strong>📌 Čtyři pilíře podnikání:</strong><br>
                • <strong>Soustavnost:</strong> nejde o jednorázový prodej, ale o činnost vykonávanou opakovaně nebo dlouhodobě.<br>
                • <strong>Samostatnost:</strong> podnikatel rozhoduje o tom, co dělá, jak pracuje a jak organizuje svou činnost.<br>
                • <strong>Vlastní jméno:</strong> podnikatel vystupuje vůči zákazníkům, úřadům a partnerům sám za sebe nebo za svou firmu.<br>
                • <strong>Vlastní odpovědnost:</strong> podnikatel nese následky svých rozhodnutí, včetně rizik, závazků a případných dluhů.
            </div>
            """, unsafe_allow_html=True) #[cite: 1]

            st.info("🤔 **Otázka k zamyšlení:** V čem je podle vás největší rozdíl mezi zaměstnancem a podnikatelem?") #[cite: 1]

   # --- 2. Slovníček základních pojmů ---
    elif selected_section == "2. Slovníček základních pojmů":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2</div><h2>2. Slovníček základních pojmů</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("""
            <div class='box-gray'>
                <strong>⚖️ Proč jsou definice důležité:</strong> V podnikání nestačí používat pojmy „přibližně“. Výrazy jako podnikatel, fyzická osoba, právnická osoba nebo živnostenské oprávnění mají oporu v právních předpisech.
            </div>
            """, unsafe_allow_html=True) #[cite: 1]

            st.markdown("<div class='box-yellow'><strong>🧩 Interaktivní výzva:</strong> Vyber tři pojmy ze slovníčku a napiš k nim vlastní příklad z reálného nebo vymyšleného podnikání.</div>", unsafe_allow_html=True) #[cite: 1]
            
            st.markdown("""
            <div class='box-purple'>
                <strong>🤖 AI mentoring:</strong> Zkopíruj tento prompt do AI asistenta: „Vysvětli mi tyto pojmy na mém podnikatelském nápadu: podnikatel, fyzická osoba, právnická osoba a živnost.“
            </div>
            """, unsafe_allow_html=True) #[cite: 1]

            st.markdown("""
            | Termín | Co znamená | Proč je důležitý |
            | :--- | :--- | :--- |
            | **Podnikatel** | Osoba, která samostatně vykonává výdělečnou činnost na vlastní účet a odpovědnost se záměrem dělat ji soustavně za účelem dosažení zisku. | Pomáhá rozlišit, kdy už nejde jen o koníček nebo jednorázový přivýdělek. |
            | **Podnikání** | Soustavná samostatná činnost vykonávaná na vlastní odpovědnost za účelem dosažení zisku. | Je základním pojmem celé kapitoly a určuje, kdy vznikají právní a finanční povinnosti. |
            | **Fyzická osoba** | Člověk — jednotlivec. V podnikání může vystupovat například jako OSVČ. | Máš poznat rozdíl mezi člověkem podnikatelem a firmou jako právnickou osobou. |
            | **Právnická osoba** | Organizovaný subjekt, který má právní osobnost. Typicky jde například o s.r.o., a.s., družstvo, spolek nebo nadaci. | Vysvětluje, proč firma může jednat, vlastnit majetek a nést odpovědnost samostatně. |
            | **OSVČ** | Osoba samostatně výdělečně činná — fyzická osoba, která podniká vlastním jménem a na vlastní odpovědnost. | Je častou formou začátku malého podnikání, freelancingu nebo služeb. |
            | **Živnost** | Podnikatelská činnost provozovaná podle živnostenského zákona, pokud splňuje zákonné podmínky. | Pomáhá určit, jestli podnikatel potřebuje živnostenské oprávnění a jaký typ živnosti řeší. |
            | **Živnostenské oprávnění** | Právo provozovat živnost. U ohlašovacích živností vzniká zpravidla ohlášením, u koncesovaných živností až udělením koncese. | Bez něj nelze legálně provozovat činnost, která živnostenské oprávnění vyžaduje. |
            | **Volná živnost** | Živnost, u které není potřeba speciální vzdělání ani praxe; stačí splnit všeobecné podmínky. | Patří sem mnoho běžných začátků podnikání, například marketingové služby nebo e-shop. |
            | **Řemeslná živnost** | Živnost, která vyžaduje odbornou způsobilost, například výuční list nebo praxi. | Ukazuje, že některé činnosti nelze začít dělat bez kvalifikace. |
            | **Vázaná živnost** | Živnost, která vyžaduje specifické vzdělání, praxi nebo jinou zákonem stanovenou způsobilost. | Pomáhá pochopit, že u některých služeb stát chrání zákazníka požadavkem na odbornost. |
            | **Koncesovaná živnost** | Živnost, kterou lze provozovat až po udělení státního povolení — koncese. | Typicky jde o regulované nebo rizikovější činnosti. |
            | **Obchodní korporace** | Souhrnný pojem pro obchodní společnosti a družstva, například v.o.s., k.s., s.r.o., a.s. a družstvo. | Pomáhá zařadit základní právní formy podnikání. |
            | **Obchodní rejstřík** | Veřejný seznam, ve kterém se zapisují obchodní korporace a další zákonem stanovené subjekty. | Slouží k ověření firmy, její právní formy, sídla a osob, které za ni jednají. |
            | **Živnostenský rejstřík** | Evidence osob podnikajících na základě živnostenského oprávnění. | Slouží k ověření, zda má podnikatel oprávnění k určité činnosti. |
            | **Ručení** | Odpovědnost za dluhy a závazky podnikatele nebo firmy. | Je klíčové při volbě právní formy, protože OSVČ a některé společnosti nesou vyšší osobní riziko. |
            | **Švarcsystém** | Nelegální nastavení, kdy člověk formálně vystupuje jako podnikatel, ale fakticky pracuje jako zaměstnanec. | Pomáhá rozpoznat rizikovou spolupráci a rozdíl mezi podnikáním a zaměstnáním. |
            | **CSR** | Společenská odpovědnost firem — přístup, kdy firma sleduje nejen zisk, ale i dopady na lidi, společnost a životní prostředí. | Ukazuje, že podnikání má také etický a společenský rozměr. |
            | **Lean Canvas** | Stručná mapa podnikatelského nápadu, která zachycuje problém, zákazníka, řešení, náklady, příjmy a rizika. | Pomáhá rychle ověřovat nápad dřív, než tým investuje hodně času nebo peněz. |
            | **MVP** | Minimální životaschopný produkt — nejmenší verze řešení, která umožní ověřit důležitý předpoklad. | Učí testovat nápad levně, rychle a bezpečně. |
            """) #[cite: 1]

            st.markdown("""
            <div class='box-gray'>
                <strong>📚 Opora v legislativě:</strong> občanský zákoník, živnostenský zákon, zákon o obchodních korporacích a zákon o veřejných rejstřících.
            </div>
            """, unsafe_allow_html=True) #[cite: 1]
            
            st.markdown("""
            <div class='box-green'>
                <strong>🌱 Etika v podnikání:</strong> Podnikání není jen o legálnosti. Férový podnikatel nezneužívá švarcsystém, platí daně, jedná poctivě se zákazníky a chová se ohleduplně k zaměstnancům, partnerům i životnímu prostředí.
            </div>
            """, unsafe_allow_html=True) #[cite: 1]

   # --- 3. OSVČ a živnosti ---
    elif selected_section == "3. OSVČ a živnosti":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 3</div><h2>3. OSVČ a živnosti</h2>", unsafe_allow_html=True)

        with st.container(border=True):
            st.write("OSVČ znamená osoba samostatně výdělečně činná. Jde o podnikání fyzické osoby — tedy člověka, který podniká vlastním jménem a nese za své podnikání odpovědnost.") #[cite: 1]
            
            st.markdown("""
            <div class='box-blue'>
                <strong>📘 Proč je to důležité:</strong> Podnikání jako OSVČ vypadá jednoduše, ale má právní, daňové a sociální důsledky. Je proto důležité znát základní podmínky živnostenského podnikání, povinnosti vůči státu a riziko osobního ručení.
            </div>
            """, unsafe_allow_html=True) #[cite: 1]

        with st.container(border=True):
            st.markdown("### 3.1 OSVČ jako nejčastější start malé podnikavosti") #[cite: 1]
            st.write("OSVČ je pro mnoho lidí nejjednodušší cesta, jak začít. Hodí se pro malé služby, freelancing, řemeslo, doučování, správu sociálních sítí, grafiku, fotografování, tvorbu webů, e-shop v menším rozsahu nebo lokální podnikání.") #[cite: 1]
            st.write("Výhoda je rychlý start a menší administrativa než u firmy. Nevýhoda je vyšší osobní riziko: OSVČ obvykle ručí za závazky celým svým majetkem.") #[cite: 1]
            
            st.markdown("""
            | Situace | Proč může OSVČ dávat smysl | Na co si dát pozor |
            | :--- | :--- | :--- |
            | **Student spravuje sociální sítě lokální kavárně.** | Nízké vstupní náklady, služba založená na dovednosti. | Smlouva, fakturace, daně, autorská práva k obsahu. |
            | **Grafik tvoří loga a šablony.** | Lze začít s notebookem a portfoliem. | Licenční podmínky, termíny, reklamace, komunikace s klientem. |
            | **Kadeřník nebo kosmetička chce pracovat samostatně.** | Vlastní zákazníci, možnost budovat značku. | Odborná způsobilost, hygiena, provozovna, odpovědnost. |
            | **Malý e-shop prodává vlastní produkty.** | Jednoduchý start a přímý kontakt se zákazníkem. | Obchodní podmínky, reklamace, sklad, ochrana spotřebitele. |
            """) #[cite: 1]

        with st.container(border=True):
            st.markdown("### 3.2 OSVČ a digitální realita") #[cite: 1]
            st.write("Dnešní OSVČ často nepotřebuje jen živnostenské oprávnění. Potřebuje také digitální a finanční gramotnost:") #[cite: 1]
            st.markdown("""
            * oddělit osobní a podnikatelské peníze,
            * evidovat příjmy a výdaje,
            * zálohovat doklady,
            * chránit osobní údaje zákazníků,
            * nepoužívat cizí fotografie, hudbu a texty bez práv,
            * komunikovat transparentně cenu, dodání a podmínky,
            * počítat s daněmi a odvody dřív, než peníze utratí.
            """) #[cite: 1]
            
            st.markdown("""
            <div class='box-yellow'>
                <strong>💡 Pravidlo pro začátečníka:</strong> To, co přijde na účet, není celé „moje výplata“. Část peněz patří na náklady, daně, sociální a zdravotní pojištění, rezervu a budoucí investice.
            </div>
            """, unsafe_allow_html=True) #[cite: 1]

            st.markdown("#### 🧮 Mini simulace OSVČ") #[cite: 1]
            st.write("Představ si, že OSVČ za měsíc vyfakturuje 28 000 Kč. Náklady na software, dopravu, materiál a reklamu jsou 6 000 Kč.") #[cite: 1]
            
            zisk_osvc = 28000 - 6000
            st.info(f"**Orientační zisk před daněmi a odvody:** {zisk_osvc} Kč") #[cite: 1]
            
            reserve_pct = st.slider("Navrhni, kolik procent by si měla OSVČ odložit stranou:", 0, 50, 30, 5) #[cite: 1]
            st.write(f"Při {reserve_pct} % si odložíte: {28000 * (reserve_pct/100):.0f} Kč.") #[cite: 1]
            st.write("Vysvětli, proč není bezpečné utratit celých 28 000 Kč.") #[cite: 1]
            
            st.markdown("<div class='box-yellow'><strong>🧩 Interaktivní výzva:</strong> Napiš, jestli by se tvůj projekt dal na začátku provozovat jako OSVČ, a uveď jedno hlavní riziko.</div>", unsafe_allow_html=True) #[cite: 1]
            st.text_input("Tvoje odpověď:", key="osvc_vyzva") #[cite: 1]
            
            st.markdown("""
            <div class='box-purple'>
                <strong>🤖 AI mentoring:</strong> Zkopíruj tento prompt do AI asistenta: „Podívej se na můj nápad a navrhni, jaký typ živnosti by mohl připadat v úvahu a co si mám ověřit.“
            </div>
            """, unsafe_allow_html=True) #[cite: 1]

            st.markdown("""
            <div class='box-red'>
                <strong>⚠️ Hlavní riziko OSVČ:</strong> OSVČ ručí za závazky z podnikání celým svým osobním majetkem. Jednoduchý start tedy neznamená nulové riziko.
            </div>
            """, unsafe_allow_html=True) #[cite: 1]

        with st.container(border=True):
            st.markdown("### 3.3 Podmínky pro podnikání jako OSVČ") #[cite: 1]
            st.markdown("<div class='box-yellow'><strong>🧩 Interaktivní výzva:</strong> Vypiš, které podmínky by musel splnit začínající podnikatel ve tvém příkladu.</div>", unsafe_allow_html=True) #[cite: 1]
            st.write("**Co musí splnit začínající OSVČ?**") #[cite: 1]
            st.markdown("""
            * dosažení věku 18 let,
            * svéprávnost,
            * bezúhonnost,
            * případně odbornou způsobilost podle druhu živnosti.
            """) #[cite: 1]

        with st.container(border=True):
            st.markdown("### 3.4 Druhy živností") #[cite: 1]
            st.markdown("<div class='box-yellow'><strong>🧩 Interaktivní výzva:</strong> Zařaď svůj nápad k volné, řemeslné, vázané nebo koncesované živnosti a napiš, proč.</div>", unsafe_allow_html=True) #[cite: 1]
            
            st.markdown("""
            | Druh živnosti | Co znamená | Příklad |
            | :--- | :--- | :--- |
            | **Volná živnost** | Není potřeba speciální vzdělání ani praxe. Stačí splnit všeobecné podmínky. | E-shop, marketingové služby, správa sociálních sítí. |
            | **Řemeslná živnost** | Vyžaduje odbornou způsobilost, například výuční list nebo praxi. | Truhlářství, kadeřnictví, opravy strojů. |
            | **Vázaná živnost** | Vyžaduje specifické vzdělání, praxi nebo zkoušku. | Účetní poradenství, průvodcovská činnost, masérské služby. |
            | **Koncesovaná živnost** | Vyžaduje státní povolení — koncesi. Jde o více regulované nebo rizikovější činnosti. | Taxislužba, provozování střelnice, prodej zbraní. |
            """) #[cite: 1]

        with st.container(border=True):
            st.markdown("### 3.5 Jak si zařídit živnost") #[cite: 1]
            st.markdown("<div class='box-yellow'><strong>🧩 Interaktivní výzva:</strong> Sepiš první tři kroky, které bys udělal/a před ohlášením živnosti.</div>", unsafe_allow_html=True) #[cite: 1]
            
            st.markdown("""
            1. Rozhodnout se, o jaký typ živnosti jde.
            2. Ověřit podmínky — všeobecné i případné zvláštní.
            3. Vyplnit Jednotný registrační formulář – nové podání.
            4. Ohlásit živnost nebo požádat o koncesi.
            5. Ověřit daňové, zdravotní a sociální povinnosti.
            """) #[cite: 1]
            
            st.markdown("""
            <div class='box-green'>
                <strong>🌍 Digitální praxe:</strong> Portál živnostenského podnikání a veřejné rejstříky slouží k ověřování údajů, podávání žádostí a kontrole obchodních partnerů.
            </div>
            """, unsafe_allow_html=True) #[cite: 1]

        with st.container(border=True):
            st.markdown("### 3.6 Povinnosti živnostníka: legislativní minimum") #[cite: 1]
            st.write("Živnostník neřeší jen zákazníky a cenu. Musí také splnit základní registrační, daňové a pojistné povinnosti.") #[cite: 1]
            
            st.markdown("""
            <div class='box-blue'>
                <strong>⚖️ Legislativní minimum pro OSVČ:</strong> Přesné částky a termíny se mohou měnit, proto je potřeba ověřovat aktuální informace na stránkách Finanční správy, ČSSZ, zdravotní pojišťovny a Portálu živnostenského podnikání.
            </div>
            """, unsafe_allow_html=True) #[cite: 1]
            
            st.write("**Co musí živnostník typicky dělat?**") #[cite: 1]
            st.markdown("""
            * **Ohlásit živnost nebo požádat o koncesi:** podle druhu činnosti na živnostenském úřadě, často přes Jednotný registrační formulář. Ten může zároveň pomoci s oznámením vůči finančnímu úřadu, ČSSZ a zdravotní pojišťovně.
            * **Platit daň z příjmů fyzických osob:** běžně se podává daňové přiznání po skončení roku. Základní lhůta je do 3 měsíců po skončení zdaňovacího období; při elektronickém podání se lhůta prodlužuje na 4 měsíce a při využití daňového poradce zpravidla na 6 měsíců.
            * **Zvážit paušální daň:** OSVČ může za splnění zákonných podmínek vstoupit do paušálního režimu. V jedné měsíční platbě pak řeší daň z příjmů, sociální pojištění i zdravotní pojištění. Paušální režim se nehodí pro každého, proto je nutné ověřit podmínky a pásmo.
            * **Platit sociální pojištění:** OSVČ obvykle platí měsíční zálohy a po skončení roku podává přehled o příjmech a výdajích pro ČSSZ.
            * **Platit zdravotní pojištění:** OSVČ obvykle platí měsíční zálohy a po skončení roku podává přehled své zdravotní pojišťovně.
            * **Vést evidenci:** podle situace může jít o daňovou evidenci, účetnictví nebo evidenci příjmů při uplatnění výdajů procentem z příjmů. Smyslem je prokázat příjmy, výdaje a základ daně.
            * **Hlásit důležité změny:** například změnu adresy, přerušení nebo ukončení činnosti, změnu zdravotní pojišťovny nebo skutečnosti důležité pro sociální a zdravotní pojištění.
            """) #[cite: 1]
            
            st.markdown("""
            <div class='box-yellow'>
                <strong>💡 Praktické pravidlo:</strong> Živnostník by si měl od každé přijaté platby odkládat část peněz na daň, sociální a zdravotní pojištění. To, co přijde na účet, ještě není čistý příjem.
            </div>
            """, unsafe_allow_html=True) #[cite: 1]

        with st.container(border=True):
            st.markdown("### 3.7 Daně a odvody OSVČ úplně jednoduše") #[cite: 1]
            st.write("OSVČ neřeší jen zákazníky a cenu. Musí také počítat s tím, že část vydělaných peněz odvede státu a pojišťovnám.") #[cite: 1]
            
            st.markdown("""
            <div class='box-red'>
                <strong>⚠️ Důležité zjednodušení:</strong> Přesné částky se každý rok mění. V první kapitole stačí pochopit princip: OSVČ platí daň z příjmů a odvody na sociální a zdravotní pojištění.
            </div>
            """, unsafe_allow_html=True) #[cite: 1]
            
            st.write("**Co OSVČ typicky platí?**") #[cite: 1]
            st.markdown("""
            * **Daň z příjmů fyzických osob:** základní sazba je 15 % ze základu daně; u velmi vysokých příjmů se používá vyšší sazba.
            * **Sociální pojištění:** slouží hlavně na důchodový systém a další dávky.
            * **Zdravotní pojištění:** slouží na financování zdravotní péče.
            * **Zálohy:** OSVČ obvykle platí během roku měsíční zálohy a po skončení roku podá daňové přiznání a přehledy pro pojišťovny.
            """) #[cite: 1]
            
            st.markdown("""
            <div class='box-blue'>
                <strong>🧮 Jednoduchý příklad:</strong> Jana má za rok příjmy 300 000 Kč a výdaje 120 000 Kč. Její zisk je tedy 180 000 Kč. Z tohoto zisku se teprve počítá daň a pojistné. Neznamená to, že si může celých 180 000 Kč nechat bez dalších povinností.
            </div>
            """, unsafe_allow_html=True) #[cite: 1]

            with st.expander("🧮 Konkrétní příklad odvodů OSVČ v roce 2026"):
                st.write("Příklad počítá s OSVČ na hlavní činnost, která není plátcem DPH, má roční příjmy 300 000 Kč, skutečné výdaje 120 000 Kč a zisk 180 000 Kč. Částky jsou zjednodušené pro pochopení principu a je potřeba je vždy ověřit podle aktuálního roku.") #[cite: 1]
                st.markdown("""
                | Varianta | Jak se platí | Co je v částce zahrnuto | Orientační částka |
                | :--- | :--- | :--- | :--- |
                | **Bez paušální daně** | OSVČ řeší platby zvlášť. | Daň z příjmů vyjde v tomto příkladu po základní slevě 0 Kč: 15 % ze zisku 180 000 Kč je 27 000 Kč, ale základní sleva na poplatníka je vyšší než vypočtená daň, takže daň k zaplacení vyjde nulová. Neznamená to ale, že OSVČ nic neplatí — pořád musí řešit sociální a zdravotní pojištění. K tomu se platí minimální sociální pojištění 5 005 Kč měsíčně a minimální zdravotní pojištění 3 306 Kč měsíčně. | přibližně 8 311 Kč měsíčně, tedy 99 732 Kč ročně |
                | **S paušální daní — I. pásmo** | OSVČ posílá jednu pravidelnou platbu. | V jedné částce je zahrnutá daň z příjmů, sociální pojištění i zdravotní pojištění. | 9 162 Kč měsíčně, tedy 109 944 Kč ročně |
                """) #[cite: 1]
                st.write("**Co z příkladu plyne:** Bez paušální daně se jednotlivé platby počítají a řeší odděleně, proto je důležité rozlišit daň, sociální a zdravotní pojištění. Paušální daň je jednodušší administrativně, protože se platí jednou částkou, ale nemusí být automaticky levnější.") #[cite: 1]
                st.write("**Kdy se může paušální daň vyplatit:** Představ si OSVČ v roce 2026, která má roční příjmy 1 000 000 Kč a používá 60% výdajový paušál. To znamená, že do daňového výpočtu nemusí vypisovat každou účtenku za notebook, telefon, dopravu nebo reklamu. Místo toho stát dovolí odečíst výdaje jednoduše procentem z příjmů. V tomto příkladu jsou výdaje paušálem 600 000 Kč, základ pro výpočet je tedy 400 000 Kč. Daň před slevou je 15 % z 400 000 Kč, tedy 60 000 Kč. Po základní slevě na poplatníka vyjde daň přibližně 29 160 Kč. K tomu se připočítá sociální a zdravotní pojištění. V takové situaci může být paušální daň v I. pásmu 9 162 Kč měsíčně, tedy 109 944 Kč ročně, výhodná nejen administrativně, ale i finančně.") #[cite: 1]
                st.write("**Jednoduše:** Paušální daň se často vyplatí tehdy, když má OSVČ vyšší příjmy, nižší skutečné výdaje a splní podmínky pro příslušné pásmo. Naopak u nízkého zisku nemusí být výhodná.") #[cite: 1]
                st.write("**Kde ověřit aktuální částky:** ČSSZ — OSVČ v paušálním režimu, Finanční správa — paušální daň a zdravotní pojišťovna OSVČ.") #[cite: 1]

            st.markdown("""
            | Krok | Jednoduché vysvětlení |
            | :--- | :--- |
            | **Příjmy** | Kolik OSVČ vyfakturovala zákazníkům. |
            | **Výdaje** | Kolik ji stálo podnikání — materiál, software, doprava, reklama. |
            | **Zisk / základ pro výpočet** | Příjmy minus výdaje. Z něj se řeší daň a pojistné. |
            | **Zálohy** | Pravidelné platby během roku, aby OSVČ neplatila všechno najednou až po skončení roku. |
            """) #[cite: 1]

            st.markdown("""
            <div class='box-yellow'>
                <strong>💡 Praktické pravidlo pro začátečníka:</strong> Když OSVČ dostane zaplaceno, neměla by všechno utratit. Část peněz si musí odložit na daň, sociální a zdravotní pojištění.
            </div>
            """, unsafe_allow_html=True) #[cite: 1]

        # --- NOVÁ KALKULAČKA HODINOVÉ SAZBY ---
        with st.container(border=True):
            st.markdown("### 🧮 Kalkulačka hodinové sazby OSVČ")
            st.write("Spousta začínajících freelancerů si špatně nastaví hodinovou sazbu, protože zapomenou, že ne každá pracovní hodina je placená (fakturovatelná) a že z příjmů musí platit daně, odvody a provozní náklady.")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### Tvoje potřeby a náklady")
                target_net = st.number_input("Cílový čistý měsíční příjem (Kč):", value=35000, step=1000)
                monthly_expenses = st.number_input("Provozní měsíční náklady (Kč) (software, účetní, doprava):", value=5000, step=500)
                taxes_insurance = st.number_input("Odhad měsíčních odvodů a daní (Kč) (např. min. zálohy):", value=9000, step=500)
                
            with col2:
                st.markdown("#### Tvůj pracovní čas")
                total_hours = st.number_input("Kolik hodin celkem měsíčně chceš pracovat?", value=160, step=10)
                billable_percent = st.slider("Kolik % času reálně fakturuješ klientovi? (zbytek je administrativa, schůzky, marketing)", min_value=10, max_value=100, value=60, step=5)
            
            st.divider()
            
            if total_hours > 0 and billable_percent > 0:
                total_gross_needed = target_net + monthly_expenses + taxes_insurance
                billable_hours = total_hours * (billable_percent / 100)
                hourly_rate = total_gross_needed / billable_hours
                
                c_res1, c_res2, c_res3 = st.columns(3)
                with c_res1:
                    st.metric(label="Nutný hrubý měsíční příjem", value=f"{total_gross_needed:,.0f} Kč".replace(",", " "))
                with c_res2:
                    st.metric(label="Fakturovatelné hodiny (měsíčně)", value=f"{billable_hours:.0f} h")
                with c_res3:
                    st.metric(label="Tvůj minimální hodinový tarif", value=f"{hourly_rate:,.0f} Kč/h".replace(",", " "))
                    
                st.info(f"**Vysvětlení:** Abys měl/a čistého **{target_net} Kč**, musíš si vydělat **{total_gross_needed} Kč** (kvůli nákladům a odvodům). Protože reálně pro klienty pracuješ jen **{billable_hours:.0f} hodin**, musíš si za jednu hodinu účtovat alespoň **{hourly_rate:,.0f} Kč**.")
# --- 4. Obchodní korporace ---
    elif selected_section == "4. Obchodní korporace":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 4</div><h2>4. Obchodní korporace</h2>", unsafe_allow_html=True)
        
        with st.container(border=True):
            st.write("Obchodní korporace jsou právnické osoby založené podle zákona o obchodních korporacích. Patří mezi ně obchodní společnosti a družstva. V praxi vytvářejí samostatný subjekt — firmu, která má vlastní název, sídlo, majetek, orgány, pravidla rozhodování a odpovědnost.") #[cite: 1]
            st.write("Je důležité pochopit, že obchodní korporace není jen „větší podnikání“. Je to právní forma, která určuje:") #[cite: 1]
            st.markdown("""
            * kdo podnik vlastní,
            * kdo za něj jedná,
            * jak se ručí za dluhy,
            * jak se vkládají peníze nebo práce,
            * jak se rozhoduje,
            * jak se rozděluje zisk,
            * jak firma vzniká a zaniká,
            * jakou administrativu musí plnit.
            """) #[cite: 1]
            st.markdown("""
            <div class='box-blue'>
                <strong>📘 Proč je to důležité:</strong> Právní forma podnikání ovlivňuje ručení, povinnosti, daně, administrativu i důvěryhodnost vůči zákazníkům, bankám a partnerům. Nejde o učení paragrafů nazpaměť, ale o pochopení, proč se právní forma volí odpovědně.
            </div>
            """, unsafe_allow_html=True) #[cite: 1]

        with st.container(border=True):
            st.markdown("### 4.1 Proč právní forma není formalita") #[cite: 1]
            st.write("Právní forma rozhoduje o tom, kdo nese riziko, kdo jedná za podnik, jak se rozděluje zisk, jak složitá je administrativa a jak podnik působí na banky, investory, dodavatele i zákazníky.") #[cite: 1]
            st.write("Pro současnou generaci je důležité pochopit, že právní forma není „nudná kolonka ve formuláři“. Je to bezpečnostní a strategické rozhodnutí.") #[cite: 1]
            
            st.markdown("""
            <div class='box-gray'>
                <strong>⚖️ Zákonný základ:</strong> Obchodní korporace upravuje zejména zákon o obchodních korporacích. Jejich vznik, zápis a veřejné údaje souvisejí také s občanským zákoníkem, živnostenským zákonem, zákonem o veřejných rejstřících a daňovými předpisy.
            </div>
            """, unsafe_allow_html=True) #[cite: 1]
            
            st.markdown("""
            | Otázka | Proč je důležitá | Příklad |
            | :--- | :--- | :--- |
            | **Kolik riskuji?** | Určuje, zda podnikatel ohrožuje i osobní majetek. | OSVČ ručí jinak než společník v s.r.o. |
            | **Podnikám sám/sama, nebo v týmu?** | Ovlivňuje rozhodování, podíly a odpovědnost. | Dva zakladatelé e-shopu potřebují jasná pravidla. |
            | **Potřebuji investora?** | Investor obvykle chce přehlednou vlastnickou strukturu. | Startup může kvůli investorovi zvolit s.r.o. nebo a.s. |
            | **Jak moc poroste podnikání?** | Růst zvyšuje rizika, počet smluv, zaměstnance a finance. | Malý freelancing zvládne OSVČ, větší tým spíš firma. |
            """) #[cite: 1]

        with st.container(border=True):
            st.markdown("### 4.2 Co patří mezi obchodní korporace") #[cite: 1]
            st.write("Obchodní korporace se dělí na obchodní společnosti a družstva. Obchodní společnosti se dále dělí na osobní společnosti (v.o.s., k.s.) a kapitálové společnosti (s.r.o., a.s.).") #[cite: 1]
            
            st.markdown("""
            | Skupina | Formy | Typický znak |
            | :--- | :--- | :--- |
            | **Osobní společnosti** | v.o.s., k.s. | Důležitá je osobní účast společníků, důvěra a často vyšší míra ručení. |
            | **Kapitálové společnosti** | s.r.o., a.s. | Důležitý je vklad kapitálu, podíly nebo akcie a oddělení firmy od osobního majetku vlastníků. |
            | **Družstva** | družstvo, evropská družstevní forma | Důležité je členství, spolupráce a společný prospěch členů. |
            """) #[cite: 1]

        with st.container(border=True):
            st.markdown("### 4.3 Obecné zákonné podmínky vzniku obchodní korporace") #[cite: 1]
            st.write("Každá obchodní korporace má svá specifická pravidla, ale některé kroky se opakují u většiny forem.") #[cite: 1]
            
            st.markdown("""
            | Krok | Co znamená | Proč je důležitý |
            | :--- | :--- | :--- |
            | **Zakladatelské právní jednání** | Sepsání společenské smlouvy, zakladatelské listiny nebo stanov podle typu korporace. | Určuje základní pravidla firmy: název, sídlo, společníky, vklady, orgány a rozhodování. |
            | **Obchodní firma** | Název, pod kterým korporace vystupuje. | Musí být odlišitelný a nesmí být klamavý. Zákazník má vědět, s kým jedná. |
            | **Sídlo** | Adresa zapsaná ve veřejném rejstříku. | Slouží pro kontakt, doručování a identifikaci firmy. |
            | **Předmět podnikání nebo činnosti** | Vymezení, co bude korporace dělat. | Často je potřeba živnostenské oprávnění nebo jiné povolení. |
            | **Vklady** | Peníze nebo jiné hodnoty, které společníci nebo členové do korporace vkládají. | Ukazují majetkovou účast a mohou ovlivnit podíl na zisku i hlasování. |
            | **Orgány korporace** | Osoby nebo skupiny, které rozhodují a jednají za firmu. | Bez jasných orgánů není zřejmé, kdo firmu řídí a kdo ji zastupuje navenek. |
            | **Zápis do obchodního rejstříku** | Veřejný zápis základních údajů o korporaci. | Obchodní korporace zpravidla vzniká až zápisem do obchodního rejstříku. |
            """) #[cite: 1]
            
            st.markdown("""
            <div class='box-gray'>
                <strong>🔍 Praktická poznámka pro tebe:</strong> Firma nezačíná jen logem a Instagramem. Nejdřív musí být jasné, kdo ji zakládá, za jakým účelem, jak ručí, kdo rozhoduje a jaké údaje budou veřejně dohledatelné.
            </div>
            """, unsafe_allow_html=True) #[cite: 1]

        with st.container(border=True):
            st.markdown("### 4.4 Volba právní formy podle situace") #[cite: 1]
            st.markdown("<div class='box-yellow'><strong>🧭 9 otázek: OSVČ, nebo s.r.o.?</strong><br>U každé otázky zaškrtni tu odpověď, která lépe odpovídá tvému projektu. Na konci se podívej, kterých odpovědí máš víc.</div>", unsafe_allow_html=True) #[cite: 1]
            
            q1 = st.radio("1️⃣ Plánuješ podnikat sám/sama, nebo v týmu?", ["Spíš OSVČ: Podnikám sám/sama a rozhoduji hlavně za sebe.", "Spíš s.r.o.: Podnikáme v týmu a potřebujeme jasně rozdělit role, odpovědnost a podíly."], key="kviz_q1") #[cite: 1]
            q2 = st.radio("2️⃣ Jde hlavně o osobní práci, nebo projekt s růstem?", ["Spíš OSVČ: Nabízím hlavně vlastní práci, službu nebo dovednost.", "Spíš s.r.o.: Projekt má růst, rozšiřovat se a fungovat jako samostatná firma."], key="kviz_q2") #[cite: 1]
            q3 = st.radio("3️⃣ Potřebujete řešit podíly a zakladatelskou dohodu?", ["Spíš OSVČ: Zatím nepotřebuji řešit podíly mezi více zakladateli.", "Spíš s.r.o.: Je nás víc a potřebujeme jasně určit, kdo má jaký podíl a kdo o čem rozhoduje."], key="kviz_q3") #[cite: 1]
            q4 = st.radio("4️⃣ Hrozí větší finanční závazky?", ["Spíš OSVČ: Náklady jsou nízké a projekt lze rychle zastavit bez velkých dluhů.", "Spíš s.r.o.: Projekt vyžaduje větší nákupy, úvěr, sklad, drahé vybavení nebo dlouhodobé smlouvy."], key="kviz_q4") #[cite: 1]
            q5 = st.radio("5️⃣ Může vzniknout škoda, reklamace nebo odpovědnost vůči zákazníkům?", ["Spíš OSVČ: Riziko škody nebo reklamací je malé a dobře zvládnutelné.", "Spíš s.r.o.: Chyba může způsobit větší škodu, reklamace nebo právní odpovědnost."], key="kviz_q5") #[cite: 1]
            q6 = st.radio("6️⃣ Potřebuješ chránit osobní majetek?", ["Spíš OSVČ: Riziko je malé a nevadí mi vyšší osobní odpovědnost.", "Spíš s.r.o.: Chci lépe oddělit osobní majetek od podnikání."], key="kviz_q6") #[cite: 1]
            q7 = st.radio("7️⃣ Budeš potřebovat investora, banku nebo větší partnery?", ["Spíš OSVČ: Nepotřebuji investora ani složitější vlastnickou strukturu.", "Spíš s.r.o.: Chci jednat s investorem, bankou nebo většími obchodními partnery."], key="kviz_q7") #[cite: 1]
            q8 = st.radio("8️⃣ Chceš rychle otestovat nápad, nebo budovat firmu?", ["Spíš OSVČ: Chci začít jednoduše a nejdřív si ověřit, jestli nápad funguje.", "Spíš s.r.o.: Od začátku počítám s budováním značky, týmu a dlouhodobé firmy."], key="kviz_q8") #[cite: 1]
            q9 = st.radio("9️⃣ Bude projekt pracovat s dalšími lidmi?", ["Spíš OSVČ: Většinu práce zvládne jeden člověk nebo občasná jednoduchá spolupráce.", "Spíš s.r.o.: Projekt bude potřebovat tým, zaměstnance, dodavatele nebo jasnější řízení spolupráce."], key="kviz_q9") #[cite: 1]
            
            if st.button("Vyhodnotit test"):
                odpovedi = [q1, q2, q3, q4, q5, q6, q7, q8, q9]
                sro_body = sum([1 for odpoved in odpovedi if "s.r.o." in odpoved])
                osvc_body = 9 - sro_body
                st.write(f"**Skóre:** OSVČ ({osvc_body}/9) | s.r.o. ({sro_body}/9)")
                st.info("💡 **Jak si výsledek vyložit:** Pokud převažují zaškrtnuté odpovědi Spíš OSVČ, bude pro začátek pravděpodobně vhodnější OSVČ. Pokud převažují zaškrtnuté odpovědi Spíš s.r.o., bude pro projekt pravděpodobně vhodnější uvažovat o s.r.o. Nejde o právní radu, ale o pomůcku k rozhodování podle rizika, týmu, růstu a odpovědnosti.") #[cite: 1]

        with st.container(border=True):
            st.markdown("### 4.5 Moderní pohled: firma jako důvěryhodná značka") #[cite: 1]
            st.write("Zákazník dnes často posuzuje firmu podle webu, sociálních sítí, recenzí a transparentnosti. Právní forma může ovlivnit důvěru: zákazník chce vědět, s kým uzavírá smlouvu, dodavatel chce vědět, kdo zaplatí fakturu, banka chce vědět, kdo ručí, investor chce vědět, kdo vlastní podíly, zaměstnanec chce vědět, kdo ho zaměstnává.") #[cite: 1]
            
            st.markdown("""
            <div class='box-gray'>
                <strong>🔍 Digitální stopa firmy:</strong> U každého podnikání je dobré ověřit název, IČO, právní formu, osobu jednající za firmu, web, recenze a veřejné rejstříky. Důvěryhodnost dnes vzniká i tím, že informace souhlasí napříč zdroji.
            </div>
            """, unsafe_allow_html=True) #[cite: 1]
            
            st.markdown("<div class='box-yellow'><strong>🧩 Interaktivní výzva:</strong> Rozhodni, jestli by tvému projektu pomohlo oddělit firmu od osobního majetku zakladatele. Napiš jeden důvod.</div>", unsafe_allow_html=True) #[cite: 1]
            st.text_input("Tvoje odpověď:", key="firma_vyzva_oddělení") #[cite: 1]
            
            st.markdown("""
            <div class='box-purple'>
                <strong>🤖 AI mentoring:</strong> Zkopíruj tento prompt do AI asistenta: „Porovnej pro můj projekt OSVČ, s.r.o. a a.s. podle rizika, administrativy a růstu.“
            </div>
            """, unsafe_allow_html=True) #[cite: 1]
            
            st.markdown("""
            <div class='box-blue'>
                <strong>📚 Jednoduše řečeno:</strong> Právní forma je „kabát“, ve kterém podnikání vystupuje navenek. Jinak se podniká jako jednotlivec na živnost a jinak jako firma.<br><br>
                <strong>🔍 Proč to souvisí s důvěryhodností:</strong> Zákazník, dodavatel i investor se podle právní formy lépe orientují v tom, s kým jednají, kdo rozhoduje a kdo nese odpovědnost.
            </div>
            """, unsafe_allow_html=True) #[cite: 1]

        with st.container(border=True):
            st.markdown("### 4.6 Osobní společnosti") #[cite: 1]
            st.write("Osobní společnosti stojí hlavně na osobní účasti, důvěře a odpovědnosti společníků.") #[cite: 1]
            st.markdown("<div class='box-yellow'><strong>🧩 Interaktivní výzva:</strong> Napiš, kdy by ve tvém projektu dávalo smysl podnikat s další osobou na základě vysoké důvěry.</div>", unsafe_allow_html=True) #[cite: 1]
            
            with st.expander("Veřejná obchodní společnost (v.o.s.)"):
                st.write("Veřejná obchodní společnost je osobní společnost, ve které podnikají alespoň dvě osoby pod společnou firmou. Zákonně jde o formu vhodnou spíše pro osoby, které si velmi důvěřují. Důvod je jednoduchý: společníci ručí za dluhy společnosti společně a nerozdílně celým svým majetkem. To znamená, že věřitel se může domáhat splnění dluhu i po jednom ze společníků, a ten si potom případně vypořádává vztahy s ostatními.") #[cite: 1]
                st.write("**Zákonné a praktické znaky v.o.s.:**") #[cite: 1]
                st.markdown("""
                * zakládají ji alespoň dvě osoby,
                * společnost vzniká zápisem do obchodního rejstříku,
                * obchodní firma obvykle obsahuje označení „veřejná obchodní společnost“ nebo zkratku „v.o.s.“,
                * společníci se podílejí na podnikání a ručí osobním majetkem,
                * zisk a ztráta se rozdělují podle společenské smlouvy, jinak podle zákonných pravidel,
                * kvůli vysokému ručení je potřeba silná důvěra mezi společníky.
                """) #[cite: 1]
                st.markdown("<div class='box-red'><strong>⚠️ Hlavní nevýhoda v.o.s.:</strong> vysoké osobní riziko společníků.</div>", unsafe_allow_html=True) #[cite: 1]
                st.markdown("<div class='box-green'><strong>✅ Hlavní výhoda v.o.s.:</strong> jednoduché založení a silná osobní důvěra mezi společníky.</div>", unsafe_allow_html=True) #[cite: 1]
                st.write("🏪 *Příklad z praxe — v.o.s.: Jako veřejná obchodní společnost v ČR působí například Kaufland Česká republika v.o.s. Právní formu je vždy nejlepší ověřit podle přesného názvu nebo IČO v obchodním rejstříku.*") #[cite: 1]

            with st.expander("Komanditní společnost (k.s.)"):
                st.write("Komanditní společnost kombinuje prvky osobní a kapitálové společnosti. Vždy v ní vystupují dva typy společníků:") #[cite: 1]
                st.markdown("""
                | Role | Komplementář | Komanditista |
                | :--- | :--- | :--- |
                | **Postavení** | Aktivně řídí společnost. | Spíše vkládá kapitál. |
                | **Ručení** | Ručí celým svým majetkem. | Ručí do výše nesplaceného vkladu. |
                | **Typická role** | „Ten, kdo podnik řídí.“ | „Ten, kdo přináší kapitál.“ |
                """) #[cite: 1]
                st.write("**Zákonné a praktické znaky k.s.:**") #[cite: 1]
                st.markdown("""
                * musí mít alespoň jednoho komplementáře a alespoň jednoho komanditistu,
                * komplementář řídí společnost a ručí za její dluhy celým svým majetkem,
                * komanditista vkládá kapitál a ručí omezeně, typicky podle výše nesplaceného vkladu zapsaného v obchodním rejstříku,
                * společnost vzniká zápisem do obchodního rejstříku,
                * obchodní firma obsahuje označení „komanditní společnost“ nebo zkratku „k.s.“,
                * hodí se pro situace, kdy jeden člověk projekt aktivně řídí a druhý spíše poskytuje kapitál.
                """) #[cite: 1]
                st.markdown("<div class='box-gray'><strong>⚖️ Riziko pro komplementáře:</strong> Komplementář je v k.s. v podobné rizikové pozici jako společník v.o.s. Pokud projekt vytváří vysoké závazky, je potřeba velmi dobře zvážit, zda je tato forma bezpečná.</div>", unsafe_allow_html=True) #[cite: 1]

        with st.container(border=True):
            st.markdown("### 4.7 Kapitálové společnosti") #[cite: 1]
            st.write("Kapitálové společnosti stojí více na vloženém kapitálu než na osobní účasti společníků. Typicky lépe oddělují firmu od osobního majetku vlastníků.") #[cite: 1]
            
            with st.expander("Společnost s ručením omezeným (s.r.o.)"):
                st.write("Společnost s ručením omezeným je jednou z nejčastějších forem podnikání v ČR. Je oblíbená proto, že umožňuje poměrně dostupné založení firmy a zároveň lépe odděluje podnikání od osobního života zakladatele. S.r.o. je vhodná pro menší a střední podnikání, rodinné firmy, startupy, e-shopy, služby i týmové projekty.") #[cite: 1]
                st.write("**Zákonné a praktické podmínky s.r.o.:**") #[cite: 1]
                st.markdown("""
                * může ji založit jedna nebo více osob,
                * zakládá se společenskou smlouvou nebo zakladatelskou listinou,
                * vzniká zápisem do obchodního rejstříku,
                * obchodní firma obsahuje označení „společnost s ručením omezeným“, „spol. s r.o.“ nebo „s.r.o.“,
                * základní kapitál je tvořen vklady společníků,
                * minimální výše vkladu společníka může být podle zákona 1 Kč, pokud společenská smlouva neurčí více,
                * zákon tedy sice umožňuje založit s.r.o. s velmi nízkým vkladem, ale v praxi to nemusí být bezpečné: firma pak nemá téměř žádnou finanční rezervu na první náklady, chyby, reklamace nebo období bez příjmů,
                * společníci ručí za dluhy společnosti jen do výše, v jaké nesplnili vkladovou povinnost podle zápisu v obchodním rejstříku,
                * statutárním orgánem je jeden nebo více jednatelů,
                * nejvyšším orgánem je valná hromada, případně jediný společník vykonává její působnost.
                """) #[cite: 1]
                st.markdown("""
                | Otázka u s.r.o. | Co máš pochopit |
                | :--- | :--- |
                | **Stačí vklad 1 Kč?** | Zákon to umožňuje, ale pro podnikatele to není příliš bezpečný start. Firma s vkladem 1 Kč nemá téměř žádný vlastní kapitál, takže i běžné počáteční náklady, zpožděné platby nebo reklamace mohou rychle vytvořit problém. Bezpečnější je počítat s reálnou finanční rezervou. |
                | **Ručí společník osobním majetkem?** | Společník obvykle neručí jako OSVČ celým majetkem, ale musí splnit vkladovou povinnost. Odpovědnost jednatele je samostatné téma. |
                | **Kdo jedná za firmu?** | Jednatel. Je zapsaný v obchodním rejstříku a má povinnost jednat s péčí řádného hospodáře. |
                | **Kdo rozhoduje o důležitých věcech?** | Valná hromada společníků nebo jediný společník. Rozhoduje například o zásadních otázkách, změnách smlouvy nebo rozdělení zisku. |
                """) #[cite: 1]
                st.markdown("<div class='box-yellow'><strong>💡 Praktické pravidlo:</strong> OSVČ bývá jednodušší pro start. S.r.o. dává větší smysl tehdy, když podnikání roste, přibývají rizika, vzniká tým nebo je potřeba oddělit osobní majetek od podnikání.</div>", unsafe_allow_html=True) #[cite: 1]

            with st.expander("Akciová společnost (a.s.)"):
                st.write("Akciová společnost je kapitálová společnost vhodná spíše pro větší projekty, investory a podnikání s významnějším kapitálem. Její základní kapitál je rozdělen na akcie.") #[cite: 1]
                st.write("**Zákonné a praktické podmínky a.s.:**") #[cite: 1]
                st.markdown("""
                * zakládá se přijetím stanov,
                * vzniká zápisem do obchodního rejstříku,
                * obchodní firma obsahuje označení „akciová společnost“ nebo zkratku „a.s.“,
                * základní kapitál je rozvržen na akcie,
                * minimální základní kapitál je 2 000 000 Kč nebo odpovídající částka v eurech podle zákonných pravidel,
                * akcionáři za dluhy společnosti neručí,
                * akcie vyjadřují podíl akcionáře na společnosti a jsou s nimi spojena práva,
                * společnost má složitější strukturu řízení a vyšší administrativní nároky než s.r.o.,
                * hodí se pro větší podnikání, investory, významnější kapitál a projekty s ambicí růstu.
                """) #[cite: 1]
                st.write("**Orgány a.s. a dva systémy řízení:**") #[cite: 1]
                st.markdown("""
                * **Nejvyšší orgán:** valná hromada — rozhodují na ní akcionáři.
                * **Dualistický systém:** statutární orgán je představenstvo a kontrolní orgán je dozorčí rada. Řízení a kontrola jsou oddělené.
                * **Monistický systém:** statutárním orgánem je správní rada. V praxi soustřeďuje řízení a kontrolu blíže k jednomu orgánu.
                * **Zisk:** rozděluje se až po zdanění daní z příjmů právnických osob a po schválení valnou hromadou. Podíl akcionáře na zisku se nazývá dividenda.
                """) #[cite: 1]
                st.info("💡 Jednoduše: A.s. není vhodná pro většinu malých školních projektů. Je důležitá hlavně proto, abys pochopil/a svět větších firem, investorů, akcií, dividend a řízení kapitálové společnosti.") #[cite: 1]

            with st.expander("Družstvo"):
                st.write("Družstvo je právnická osoba založená na členství. Jeho smyslem není jen zisk pro vlastníky, ale také společný prospěch členů — například bydlení, práce, prodej výrobků nebo společné využívání služeb.") #[cite: 1]
                st.write("**Zákonné a praktické znaky družstva:**") #[cite: 1]
                st.markdown("""
                * je založeno na členství,
                * má zpravidla alespoň tři členy,
                * vzniká zápisem do obchodního rejstříku,
                * obchodní firma obsahuje označení „družstvo“,
                * členové se podílejí na činnosti družstva,
                * orgány družstva typicky zahrnují členskou schůzi, představenstvo a kontrolní komisi; u menších družstev mohou být pravidla jednodušší podle zákonných možností,
                * smyslem může být podnikání i zajišťování potřeb členů,
                * hodí se tam, kde je důležitá spolupráce a společný prospěch.
                """) #[cite: 1]
                st.markdown("<div class='box-blue'><strong>👥 Funkce družstva:</strong> Družstvo umožňuje lidem spojit síly, sdílet náklady, společně rozhodovat a řešit potřebu, kterou by jednotlivec zvládal obtížněji.</div>", unsafe_allow_html=True) #[cite: 1]

        with st.container(border=True):
            st.markdown("### 4.8 Povinnosti členů orgánů: péče řádného hospodáře") #[cite: 1]
            st.write("Osoby, které řídí obchodní korporaci nebo za ni jednají, nemohou rozhodovat libovolně. Musí jednat informovaně, pečlivě, loajálně a v zájmu korporace. Tento princip se označuje jako péče řádného hospodáře. Pro tebe je to důležité hlavně u jednatele s.r.o., členů představenstva a dalších osob ve vedení. Pokud někdo firmu řídí nezodpovědně, může nést právní následky.") #[cite: 1]
            
            st.markdown("""
            | Situace | Odpovědné jednání | Rizikové jednání |
            | :--- | :--- | :--- |
            | **Firma podepisuje velkou smlouvu.** | Vedení si ověří cenu, rizika, závazky a schopnost plnit. | Podepíše smlouvu bez čtení, jen proto, že „to vypadá dobře“. |
            | **Firma má finanční problémy.** | Vedení sleduje cashflow, jedná s věřiteli a řeší situaci včas. | Ignoruje dluhy a objednává další služby, i když ví, že nezaplatí. |
            | **Firma pracuje s daty zákazníků.** | Nastaví přístupy, ochranu dat a jasná pravidla. | Sdílí zákaznická data v nechráněné tabulce bez pravidel. |
            """) #[cite: 1]
            st.markdown("<div class='box-gray'><strong>⚖️ Didaktická pointa:</strong> Omezené ručení neznamená nulovou odpovědnost. Společník, jednatel, člen představenstva nebo člen družstva musí chápat svou roli a rozhodovat odpovědně.</div>", unsafe_allow_html=True) #[cite: 1]

        with st.container(border=True):
            st.markdown("### 4.9 Přehled právních forem") #[cite: 1]
            st.markdown("""
            | Forma | Administrativní náročnost | Míra rizika | Kapitál | Typický znak |
            | :--- | :--- | :--- | :--- | :--- |
            | **OSVČ** | Nízká | Vysoká — ručení celým majetkem | Není vyžadován | Rychlý a jednoduchý start |
            | **v.o.s.** | Střední | Vysoká — společníci ručí celým majetkem | Není vyžadován | Osobní důvěra společníků |
            | **k.s.** | Střední | Různé ručení komplementářů a komanditistů | Vklad komanditisty | Kombinace aktivního společníka a investora |
            | **s.r.o.** | Střední | Nižší — oddělení firmy od osobního majetku | Od 1 Kč, reálně více nákladů | Dostupná firemní forma |
            | **a.s.** | Vysoká | Nižší — akcionáři osobně neručí | Vyšší základní kapitál | Akcie, investoři, větší kapitál |
            | **družstvo** | Střední | Záleží na pravidlech a situaci družstva | Členské vklady | Společný prospěch členů |
            """) #[cite: 1]

        with st.container(border=True):
            st.markdown("### 4.10 Vznik obchodní korporace") #[cite: 1]
            st.write("Založení právnické osoby, například s.r.o. nebo a.s., je formální proces. Obvykle vyžaduje součinnost s notářem a zápis do obchodního rejstříku.") #[cite: 1]
            st.markdown("""
            1. Sepsání společenské smlouvy nebo zakladatelské listiny.
            2. Splacení vkladu nebo základního kapitálu.
            3. Získání živnostenského oprávnění, pokud je potřeba.
            4. Zápis do obchodního rejstříku.
            """) #[cite: 1]
            st.markdown("<div class='box-blue'><strong>🏛️ Důležité pravidlo:</strong> Obchodní korporace vzniká až dnem zápisu do obchodního rejstříku.</div>", unsafe_allow_html=True) #[cite: 1]

        with st.container(border=True):
            st.markdown("### 4.11 Co se zapisuje do obchodního rejstříku") #[cite: 1]
            st.write("Obchodní rejstřík je veřejný seznam. Díky němu si může zákazník, dodavatel, banka, úřad nebo budoucí zaměstnanec ověřit základní údaje o firmě.") #[cite: 1]
            st.write("Typicky se zapisuje: název firmy, sídlo, právní forma, identifikační číslo osoby, předmět podnikání nebo činnosti, statutární orgán a způsob jednání, společníci, výše vkladů, základní kapitál, změny, zrušení, likvidace.") #[cite: 1]

        with st.container(border=True):
            st.markdown("### 4.12 Zrušení, likvidace a zánik obchodní korporace") #[cite: 1]
            st.write("Obchodní korporace nemusí existovat navždy. Může být zrušena dobrovolně, rozhodnutím orgánu společnosti, uplynutím doby, splněním účelu, rozhodnutím soudu nebo z jiných zákonných důvodů.") #[cite: 1]
            st.markdown("""
            | Pojem | Jednoduché vysvětlení | Příklad |
            | :--- | :--- | :--- |
            | **Zrušení** | Firma vstoupí do fáze ukončování. | Společníci rozhodnou, že s.r.o. už nebude pokračovat. |
            | **Likvidace** | Firma vypořádá majetek, dluhy a pohledávky. | Prodá vybavení, zaplatí závazky a rozdělí zbytek podle pravidel. |
            | **Zánik** | Firma právně přestane existovat. | Po výmazu z obchodního rejstříku už korporace neexistuje. |
            """) #[cite: 1]

        with st.container(border=True):
            st.markdown("### 4.13 Daně a odvody u obchodních korporací úplně jednoduše") #[cite: 1]
            st.write("U obchodních korporací je důležité rozlišit firmu a člověka, který z ní dostává peníze. Firma může platit daň ze svého zisku. Pokud má zaměstnance, řeší také mzdy, sociální a zdravotní pojištění za zaměstnance. Když si vlastník vyplácí podíl na zisku, řeší se další zdanění podle pravidel pro daný typ příjmu.") #[cite: 1]
            st.markdown("<div class='box-red'><strong>⚠️ Důležité zjednodušení:</strong> V první kapitole nejde o přesný výpočet účetnictví. Cílem je pochopit, že s.r.o. nebo a.s. není „bez daní“. Jen se peníze daní jinak než u OSVČ.</div>", unsafe_allow_html=True) #[cite: 1]
            
            st.write("**Co může platit například s.r.o.?**") #[cite: 1]
            st.markdown("""
            * **Daň z příjmů právnických osob:** platí ji firma ze svého zisku; sazba je 21 %.
            * **Sociální a zdravotní pojištění za zaměstnance:** pokud firma zaměstnává lidi, odvádí za ně pojistné a část strhává ze mzdy.
            * **Daň ze mzdy:** pokud si zakladatel vyplácí mzdu jako zaměstnanec nebo jednatel, řeší se zdanění mzdy.
            * **Zdanění podílu na zisku:** pokud si společník vyplácí zisk, nejde o běžnou tržbu, ale o výplatu podílu na zisku.
            """) #[cite: 1]
            
            st.markdown("""
            | Situace | Kdo platí | Co je pointa |
            | :--- | :--- | :--- |
            | **OSVČ vydělá peníze** | Podnikatel jako fyzická osoba | Řeší daň z příjmů, sociální a zdravotní pojištění. |
            | **s.r.o. vytvoří zisk** | Firma jako právnická osoba | Firma platí daň ze zisku. |
            | **s.r.o. má zaměstnance** | Firma jako zaměstnavatel | Řeší mzdu, daň ze mzdy a odvody na sociální a zdravotní pojištění. |
            | **Společník si vyplatí zisk** | Společník / firma podle pravidel výplaty | Nejde o totéž jako tržba. Výplata zisku má vlastní daňová pravidla. |
            """) #[cite: 1]
            
            st.markdown("<div class='box-yellow'><strong>💡 Praktické srovnání:</strong> OSVČ bývá jednodušší na start, ale ručí osobním majetkem. Společnost s ručením omezeným lépe odděluje firmu od osobního života, ale má složitější administrativu, účetnictví a pravidla pro daně.</div>", unsafe_allow_html=True) #[cite: 1]

        with st.container(border=True):
            st.markdown("### 4.14 Srovnání OSVČ a s.r.o. pro tvůj projekt") #[cite: 1]
            st.markdown("""
            | Otázka | OSVČ | s.r.o. |
            | :--- | :--- | :--- |
            | **Jak rychle lze začít?** | Obvykle jednodušší a rychlejší. | Složitější založení, zápis a administrativa. |
            | **Ručení** | Podnikatel typicky ručí celým osobním majetkem. | Společník ručí omezeně podle nesplaceného vkladu; firma má vlastní majetek. |
            | **Důvěryhodnost pro větší partnery** | Může stačit pro menší služby. | Často působí vhodněji pro tým, investora nebo větší zakázky. |
            | **Administrativa** | Jednodušší evidence podle situace. | Vyšší nároky, účetnictví, orgány, zápisy a rozhodování. |
            | **Vhodné pro** | Freelancing, malé služby, start jednotlivce. | Rostoucí projekt, tým, vyšší rizika, investice nebo potřeba oddělit majetek. |
            """) #[cite: 1]

        with st.container(border=True):
            st.markdown("### 4.15 Aktivita: Vyber právní formu podle situace") #[cite: 1]
            st.write("U každé situace rozhodni, která právní forma dává největší smysl na začátku. Své rozhodnutí zdůvodni podle ručení, administrativy, počtu osob, kapitálu a rizika.") #[cite: 1]
            st.selectbox("Student nabízí grafické služby třem lokálním firmám.", ["Vyber odpověď...", "OSVČ", "s.r.o.", "Družstvo", "a.s."], key="pf_1") #[cite: 1]
            st.selectbox("Dva kamarádi chtějí dlouhodobě provozovat e-shop s vlastní značkou.", ["Vyber odpověď...", "OSVČ", "s.r.o.", "Družstvo", "a.s."], key="pf_2") #[cite: 1]
            st.selectbox("Skupina pěti lidí chce společně sdílet vybavení a prodávat výrobky členů.", ["Vyber odpověď...", "OSVČ", "s.r.o.", "Družstvo", "a.s."], key="pf_3") #[cite: 1]
            st.selectbox("Startup hledá investora a plánuje rychlý růst.", ["Vyber odpověď...", "OSVČ", "s.r.o.", "Družstvo", "a.s."], key="pf_4") #[cite: 1]
            st.selectbox("Dva společníci chtějí podnikat společně, ale projekt může vytvářet vysoké dluhy.", ["Vyber odpověď...", "v.o.s.", "s.r.o.", "Družstvo", "OSVČ"], key="pf_5") #[cite: 1]
            st.selectbox("Tým studentů chce jednorázově prodávat výrobky na školní akci.", ["Vyber odpověď...", "Jednorázová aktivita bez ŽL (do limitu)", "OSVČ", "s.r.o.", "a.s."], key="pf_6") #[cite: 1]
            
            st.markdown("""
            <div class='box-purple'>
                <strong>🤖 AI mentoring:</strong> Zkopíruj tento prompt do AI asistenta: „Porovnej pro můj projekt OSVČ, s.r.o., v.o.s., k.s., a.s. a družstvo. U každé formy napiš výhodu, riziko, zákonný znak a otázku, kterou si musím ověřit.“
            </div>
            """, unsafe_allow_html=True) #[cite: 1]

        with st.container(border=True):
            st.markdown("### 4.16 Jiné formy podnikání v ČR a v rámci EU") #[cite: 1]
            st.write("Vedle OSVČ a obchodních korporací existují i další způsoby, jak může podnikání fungovat. Některé jsou běžné v českém prostředí, jiné pomáhají podnikat napříč státy Evropské unie.") #[cite: 1]
            st.markdown("<div class='box-blue'><strong>🌍 Proč to znát:</strong> V praxi se podnikání nemusí vždy vejít jen do jednoduchého rozdělení OSVČ vs. s.r.o. Firma může mít pobočku, podnikatel může spolupracovat smluvně s dalšími osobami, nezisková organizace může vykonávat doplňkovou hospodářskou činnost a větší podniky mohou využívat evropské právní formy.</div>", unsafe_allow_html=True) #[cite: 1]
            
            st.markdown("""
            | Forma | Kde se používá | Jednoduché vysvětlení | Na co si dát pozor |
            | :--- | :--- | :--- | :--- |
            | **Odštěpný závod / pobočka** | ČR i zahraničí | Část podniku, která vystupuje navenek jako organizační jednotka. Zahraniční firma tak může podnikat v ČR bez založení nové české společnosti. | Nejde o samostatnou právnickou osobu jako s.r.o.; důležitý je zápis a odpovědnost mateřské firmy. |
            | **Tiché společenství** | ČR | Tichý společník poskytne podnikateli vklad a podílí se na výsledku podnikání, ale navenek obvykle nevystupuje. | Je to smluvní forma spolupráce, ne samostatná obchodní korporace. |
            | **Smluvní spolupráce více osob** | ČR | Více osob může spolupracovat na základě smlouvy, aniž by hned zakládaly novou firmu. | Je nutné jasně upravit odpovědnost, rozdělení nákladů, příjmů a vlastnictví výsledků práce. |
            | **Spolek, ústav, nadace** | ČR | Neziskové právnické osoby. Jejich hlavním účelem není podnikání, ale mohou mít doplňkovou hospodářskou činnost, pokud podporuje jejich hlavní smysl. | Zisk se obvykle nemá rozdělovat jako u obchodní společnosti; má sloužit k naplňování účelu organizace. |
            | **Státní podnik** | ČR | Podnik založený státem pro plnění veřejného nebo strategického zájmu. | Není běžnou volbou pro začínajícího podnikatele. |
            | **Evropská společnost (SE)** | EU | Akciová společnost evropského typu, která může usnadnit podnikání ve více členských státech EU. | Hodí se spíše pro větší podniky; má vyšší nároky na kapitál, správu a přeshraniční fungování. |
            | **Evropské hospodářské zájmové sdružení (EHZS)** | EU | Forma spolupráce podnikatelů nebo firem z různých států EU. Pomáhá členům rozvíjet jejich činnost, například společný projekt, výzkum, nákup nebo obchod. | Smyslem není samostatně nahrazovat podnikání členů, ale podporovat jejich spolupráci. |
            | **Evropské družstvo (SCE)** | EU | Družstvo evropského typu, které umožňuje členům podnikat nebo spolupracovat přes hranice členských států. | Je vhodné hlavně pro přeshraniční družstevní projekty, ne pro běžný malý start. |
            """) #[cite: 1]

            st.write("**Co si z toho odnést?**") #[cite: 1]
            st.markdown("""
            * Pro běžný začátek podnikání v ČR se nejčastěji řeší OSVČ nebo s.r.o.
            * Pokud podnikání roste do zahraničí, může být důležitá pobočka, odštěpný závod nebo evropská právní forma.
            * Neziskové organizace mohou vykonávat hospodářskou činnost, ale jejich hlavní smysl je jiný než rozdělování zisku vlastníkům.
            * V Evropské unii existují formy, které mají usnadnit přeshraniční podnikání a spolupráci.
            """) 
# --- 5. Startup: nápad, který hledá funkční byznys ---
    elif "5. Startup" in selected_section:
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 5</div><h2>5. Startup: nápad, který hledá funkční byznys</h2>", unsafe_allow_html=True)
        
        with st.container(border=True):
            st.write("Startup je mladý podnikatelský projekt, který hledá opakovatelný a škálovatelný způsob, jak řešit problém zákazníka. Nejde jen o „malou firmu“. Startup často začíná nejistotou: tým má nápad, ale ještě neví, zda o něj zákazníci opravdu stojí, kolik za něj zaplatí a jak rychle může růst.")
            
            st.markdown("""
            <div class='box-blue'>
                <strong>📘 Proč je to důležité:</strong> Startupové téma rozvíjí podnikavost, kreativitu, práci s informacemi, digitální kompetence, týmovou spolupráci, finanční uvažování, komunikaci se zákazníkem a schopnost ověřovat nápady před investicí peněz.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 5.1 Startup pro současnou generaci")
            st.write("💡 **Co je to vlastně podnikavost?** Je to schopnost vidět příležitosti tam, kde ostatní vidí problémy, a mít odvahu realizovat nápady.")
            st.write("🎲 **Pilíř 1: Přijímání kalkulovaného rizika:** Podnikatel nehazarduje, ale spočítá si, co nejhoršího se může stát a zda to zvládne.")
            st.write("🔄 **Pilíř 2: Odolnost vůči nezdaru (Resilience):** Pravidlo 'Fail fast, learn faster'. Chyba není ostuda, ale lekce pro další pokus.")
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("""
                <div class='box-gray'>
                    <strong>🏛️ Tradiční firma (Pekařství na rohu)</strong><br><br>
                    <strong>Cíl:</strong> Stabilita a stálý zisk. Cílem tradiční firmy je dlouhodobě fungovat, udržet si zákazníky a vydělávat pravidelně. Pekařství na rohu nepotřebuje během měsíce dobýt celý svět — potřebuje, aby se místní lidé vraceli pro pečivo, byli spokojení a podnik měl jisté příjmy na nájem, mzdy, suroviny a další provoz.<br><br>
                    <strong>Riziko:</strong> Malé až střední. Riziko je obvykle nižší než u startupu, protože podnik často pracuje s ověřeným modelem: lidé pečivo znají a pravidelně ho kupují. Přesto riziko existuje — mohou zdražit suroviny, přijít konkurence, změnit se nájem nebo klesnout počet zákazníků. Podnikatel proto musí hlídat náklady, kvalitu a vztah se zákazníky.<br><br>
                    <strong>Trh:</strong> Místní sousedství. Trhem je hlavně okolí provozovny: lidé z ulice, školy, kanceláře nebo sídliště. Úspěch závisí na dobré poloze, pověsti, kvalitě výrobků a pravidelném kontaktu se zákazníky. Pekařství nemusí oslovit miliony lidí — stačí mu stabilní komunita, která se vrací.
                </div>
                """, unsafe_allow_html=True)
            with col2:
                st.markdown("""
                <div class='box-green'>
                    <strong>🚀 Startup (Aplikace na sdílení kol)</strong><br><br>
                    <strong>Cíl:</strong> Obrovský a rychlý růst do celého světa. Startup nechce jen pomalu provozovat jednu službu v jedné čtvrti. Hledá model, který se dá rychle opakovat ve více městech nebo zemích. Pokud aplikace na sdílení kol funguje v jednom městě, tým chce ověřit, zda ji lze spustit i jinde, získat hodně uživatelů a růst výrazně rychleji než běžná lokální firma.<br><br>
                    <strong>Riziko:</strong> Extrémně vysoké (buď uspěje, nebo zanikne). Startup pracuje s velkou nejistotou. Nemusí být jasné, jestli lidé službu opravdu použijí, zda za ni zaplatí, jestli město povolí provoz, zda se kola nebudou ztrácet nebo ničit a jestli náklady na údržbu nepřevýší příjmy. Proto může startup rychle vyrůst, ale také rychle skončit, pokud se ukáže, že model nefunguje.<br><br>
                    <strong>Trh:</strong> Celá planeta. Trh startupu může být mnohem širší než jedno sousedství. Aplikace se dá teoreticky nabídnout ve více městech, státech nebo regionech, pokud se podaří přizpůsobit pravidlům, dopravě a chování zákazníků. Startup proto přemýšlí globálně: hledá problém, který řeší mnoho lidí na různých místech.
                </div>
                """, unsafe_allow_html=True)

            st.divider()
            st.markdown("#### 🎯 SIMULACE: Máš nápad na novou aplikaci. Co uděláš jako první?")
            sim_choice = st.radio("Vyber si svůj první krok:", ["Vyber...", "A) Utratím 200 000 Kč za vývoj plné verze", "B) Udělám jednoduchý dotazník a jednoduchý web pro zájemce"])
            
            if sim_choice == "A) Utratím 200 000 Kč za vývoj plné verze":
                st.error("❌ CHYBA! Utratil jsi peníze a zbytečně postavil něco, co lidé nechtějí. Chybělo ti otestování nápadu.")
            elif sim_choice == "B) Udělám jednoduchý dotazník a jednoduchý web pro zájemce":
                st.success("🎉 SKVĚLE! Získal jsi zdarma 500 zájemců a ověřil trh. Můžeš bezpečně stavět MVP!")

            with st.expander("💡 Dvě otázky pro představivost"):
                st.write("**Otázka 1: Proč většina startupů selže v prvním roce?**")
                st.write("*Odpověď:* Vyrobí produkt, který ve skutečnosti nikdo nepotřebuje (neověří si poptávku).")
                st.write("**Otázka 2: Co znamená zkratka MVP?**")
                st.write("*Odpověď:* Minimum Viable Product – nejjednodušší verze produktu, která už funguje a dá se testovat na lidech.")

            st.write("Startupová kultura je blízká dnešní generaci, protože spojuje technologie, sociální sítě, AI, komunitu, rychlé testování a možnost tvořit i s malým rozpočtem. Zároveň ale svádí k iluzi, že stačí dobrý nápad, virální video nebo hezká aplikace.")
            st.write("Ve skutečnosti startup stojí na ověřování:")
            st.markdown("""
            * Existuje skutečný problém?
            * Koho problém bolí natolik, že za řešení zaplatí?
            * Umíme zákazníka oslovit?
            * Vyjdou ekonomicky náklady a příjmy?
            * Umíme růst bez toho, aby se zhroutila kvalita, tým nebo cashflow?
            """)
            st.markdown("<div class='box-red'><strong>⚠️ Častý omyl:</strong> „Mám nápad na aplikaci“ ještě neznamená startup. Startup vzniká až tehdy, když existuje problém, zákazník, test, zpětná vazba a možnost opakovaně vytvářet hodnotu.</div>", unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 5.2 Startupová hypotéza")
            st.write("Každý startup začíná předpoklady. Ty je potřeba převést na hypotézy, které se dají ověřit.")
            st.markdown("""
            | Nejasný předpoklad | Lepší hypotéza | Jak ji ověřit |
            | :--- | :--- | :--- |
            | Lidem se náš nápad bude líbit. | Alespoň 15 studentů z 30 řekne, že by službu použilo každý týden. | Krátký rozhovor nebo dotazník. |
            | Zákazníci budou platit. | Alespoň 5 lidí si předobjedná produkt za 99 Kč. | Předobjednávkový formulář. |
            | Marketing na TikToku bude fungovat. | Video získá 1 000 zhlédnutí a 20 kliknutí na formulář. | Testovací příspěvek a měření odkazu. |
            | Výroba nebude drahá. | Variabilní náklad na kus nepřekročí 60 % prodejní ceny. | Kalkulace dodavatelů a test malého množství. |
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
                <strong>🤖 AI prompt pro startup:</strong> „Pomoz mi z mého nápadu vytvořit 5 ověřitelných hypotéz. U každé navrhni nejlevnější test, metriku úspěchu a riziko, že si výsledek špatně vyložím.“
            </div>
            """, unsafe_allow_html=True)

            st.markdown("#### 🚀 Aktivita: Startup za 30 minut")
            st.write("Ve skupině vyberte jeden problém ze školy nebo běžného života.")
            st.markdown("""
            1. Popište problém jednou větou.
            2. Určete konkrétního zákazníka.
            3. Navrhněte nejjednodušší řešení.
            4. Sepište jednu hypotézu.
            5. Navrhněte test bez velkých nákladů.
            6. Určete metriku: podle čeho poznáte zájem?
            """)
            st.info("**Výstup:** Jedna stránka „nápad → hypotéza → test → metrika“.")
            
            st.markdown("<div class='box-yellow'><strong>🧩 Interaktivní výzva:</strong> Vymysli jeden problém, který lidé kolem tebe řeší, a napiš, jaké jednoduché řešení by mohlo vzniknout jako startup.</div>", unsafe_allow_html=True)
            st.text_input("Tvoje odpověď:", key="startup_vymysli_problem")
            
            st.markdown("""
            <div class='box-purple'>
                <strong>🤖 AI mentoring:</strong> Zkopíruj tento prompt do AI asistenta: „Pomoz mi převést můj nápad na startupovou hypotézu: problém, zákazník, řešení, cena a první test.“
            </div>
            """, unsafe_allow_html=True)
            st.markdown("<div class='box-blue'><strong>🚀 Jednoduše řečeno:</strong> Startup není hotová firma. Je to pokus najít funkční podnikatelský model, který se dá rychle ověřovat, upravovat a případně zvětšovat.</div>", unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 5.4 Jak startup vzniká")
            st.write("Startup obvykle nevzniká tak, že někdo rovnou napíše dokonalý podnikatelský plán. Častější cesta je postupné ověřování. Tým nejdřív pracuje s nejistotou: má domněnky o zákazníkovi, problému, řešení, ceně a způsobu prodeje. Teprve když získá důkazy, rozhoduje, jestli pokračovat, upravit směr, nebo projekt ukončit.")
            st.markdown("<div class='box-yellow'><strong>🧩 Interaktivní výzva:</strong> Vyber jeden krok z následujícího postupu a napiš, co bys v něm konkrétně udělal/a u vlastního nápadu.</div>", unsafe_allow_html=True)
            st.markdown("""
            * **Problém:** někdo si všimne potřeby, nespokojenosti nebo neefektivního řešení.
            * **Zákazník:** tým určí, komu chce pomoci.
            * **Návrh řešení:** vznikne první jednoduchá verze produktu nebo služby.
            * **Ověření:** tým mluví se zákazníky, sbírá zpětnou vazbu a testuje zájem.
            * **Úprava nápadu:** pokud test nevyjde, startup změní řešení, zákazníka, cenu, kanál nebo rozsah.
            * **Růst:** když se ukáže, že zákazníci mají zájem, startup hledá způsob, jak růst opakovatelně a finančně udržitelně.
            """)
            st.markdown("**Příklad vzniku startupu:** Studenti zjistí, že jejich spolužáci často nestíhají plánovat učení. Nevytvoří hned velkou aplikaci, ale nejdřív sdílenou Notion šablonu nebo jednoduchou tabulku. Tu vyzkouší ve třídě, sledují, kdo ji skutečně používá, co studentům chybí a zda by za rozšířenou verzi zaplatili. Pokud ji lidé používají a doporučují dál, tým může řešit cenu, marketing a další rozvoj.")

        with st.container(border=True):
            st.markdown("### 5.5 Metodika Lean Startup")
            st.write("Metodika Lean Startup pomáhá začínajícím týmům netrávit měsíce tvorbou produktu, o který nakonec nikdo nestojí. Její základní myšlenka je jednoduchá: nejdřív ověř nejrizikovější předpoklad, potom investuj víc času a peněz.")
            st.write("Lean Startup vychází z toho, že startup není zmenšená verze velké firmy. Velká firma často ví, kdo je její zákazník, jaký produkt prodává a jak vydělává. Startup to teprve hledá. Proto potřebuje rychlé učení, malé experimenty a ochotu měnit plán podle dat.")
            st.markdown("<div class='box-blue'><strong>🚀 Jednoduše řečeno:</strong> Lean Startup je způsob práce, při kterém tým rychle vytvoří malý test, získá zpětnou vazbu, změří výsledky a podle nich se rozhodne, co dál.</div>", unsafe_allow_html=True)
            
            st.markdown("#### Základní cyklus: vytvoř — změř — pouč se")
            st.write("Lean Startup se často vysvětluje pomocí cyklu Build — Measure — Learn, česky vytvoř — změř — pouč se.")
            st.markdown("""
            | Krok | Co tým dělá | Příklad ve školním startupu | Častá chyba |
            | :--- | :--- | :--- | :--- |
            | **Vytvoř** | Tým připraví nejmenší verzi testu nebo prototypu. | Místo celé aplikace vytvoří klikací návrh, formulář, šablonu nebo testovací stánek. | Tým chce hned dokonalý produkt a ztratí týdny přípravou. |
            | **Změř** | Tým sbírá data, ne pouze dojmy. | Sleduje počet registrací, předobjednávek, rozhovorů, opakovaných použití nebo skutečných plateb. | Tým se spokojí s větou „lidem se to líbilo“. |
            | **Pouč se** | Tým vyhodnotí, co data znamenají, a rozhodne další krok. | Pokračuje, upraví zákazníka, změní cenu, zjednoduší řešení nebo projekt ukončí. | Tým ignoruje negativní výsledky, protože se do nápadu zamiloval. |
            """)
            st.markdown("<div class='box-gray'><strong>🧪 Pravidlo Lean Startup:</strong> Neověřuj všechno najednou. Nejdřív testuj předpoklad, který může projekt nejrychleji zbořit — například zda problém opravdu existuje, zda zákazník zaplatí nebo zda řešení umíte dodat za rozumné náklady.</div>", unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 5.6 MVP: minimální životaschopný produkt")
            st.write("MVP znamená minimum viable product, česky minimální životaschopný produkt. Nejde o nejlevnější ani nejodbytější verzi. Jde o nejmenší verzi, která dokáže ověřit důležitou otázku.")
            st.write("MVP má odpovědět například:")
            st.markdown("""
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
            st.markdown("<div class='box-red'><strong>⚠️ Pozor:</strong> MVP není výmluva pro nekvalitu. I malý test musí být bezpečný, férový a srozumitelný. Pokud prodáváme produkt, zákazník musí vědět, co přesně dostane.</div>", unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 5.7 Validované učení")
            st.write("Cílem Lean Startup není jen „něco zkusit“. Cílem je validované učení — tedy ověřené poznání, které pomůže rozhodnout. Tým musí umět říct: „Mysleli jsme si X, otestovali jsme Y, výsledek byl Z, proto uděláme další krok.“")
            st.markdown("""
            | Slabé vyhodnocení | Validované učení |
            | :--- | :--- |
            | „Dotazník dopadl dobře.“ | „Z 60 respondentů 42 uvedlo, že problém řeší alespoň jednou týdně, ale pouze 6 by bylo ochotno zaplatit více než 100 Kč. Musíme upravit cenu nebo hodnotu nabídky.“ |
            | „Příspěvek měl hodně lajků.“ | „Příspěvek měl 180 lajků, ale jen 4 kliknutí na objednávkový formulář. Lajky tedy nejsou důkaz nákupního zájmu.“ |
            | „Lidem se batohy líbily.“ | „Z 12 testovacích batohů se prodalo 9 během dvou dnů, 3 zákazníci žádali nižší cenu a 1 reklamoval zip. Další série potřebuje lepší kontrolu zipů.“ |
            """)
            st.info("**Věta pro vyhodnocení experimentu:** Předpokládali jsme, že… Ověřili jsme to pomocí… Naměřili jsme… Zjistili jsme… Proto teď rozhodujeme, že…")

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
            st.write("Pivot neznamená selhání. Znamená změnu směru na základě učení. Tým může změnit: cílového zákazníka, problém, řešení, cenu, distribuční kanál, způsob monetizace, rozsah produktu.")
            st.markdown("<div class='box-gray'><strong>🧭 Podnikatelská zralost:</strong> Dobrý tým neobhajuje nápad za každou cenu. Dobrý tým chrání čas, peníze a energii tím, že se umí rozhodnout podle důkazů.</div>", unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 5.9 Lean Startup v mini projektu SŠ")
            st.write("Pro školní projekt stačí Lean Startup použít v jednoduché podobě. Nemusíš znát odborné termíny nazpaměť, důležité je umět pracovat v tomto sledu:")
            st.markdown("""
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
            st.markdown("<div class='box-yellow'><strong>🧩 Aktivita: Lean Startup sprint na 45 minut</strong><br>Popiš problém, urči zákazníka, napiš hypotézu, navrhni MVP test, urči metriku úspěchu a rozhodni se, co uděláš podle výsledku.</div>", unsafe_allow_html=True)
            st.markdown("""
            <div class='box-purple'>
                <strong>🤖 AI mentoring:</strong> Zkopíruj tento prompt do AI asistenta: „Použij metodiku Lean Startup na můj nápad. Pomoz mi určit nejrizikovější hypotézu, navrhni MVP test, metriku úspěchu, možné výsledky a rozhodnutí: pokračovat, pivotovat nebo ukončit.“
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 5.10 Kam jít s novým nápadem")
            st.write("Začínající tým nemusí být na všechno sám. V ČR existuje startupový ekosystém — síť organizací, mentorů, investorů, soutěží, inkubátorů, akcelerátorů a coworkingových center.")
            st.markdown("""
            | Kam se obrátit | Co může pomoci získat |
            | :--- | :--- |
            | **Inkubátor** | Pomoc v úplném začátku, mentoring, prostor, kontakty. |
            | **Akcelerátor** | Intenzivní program pro rychlejší rozvoj nápadu, často zakončený prezentací investorům. |
            | **Coworkingové centrum** | Místo pro práci, networking a setkávání s dalšími podnikavými lidmi. |
            | **Startupová soutěž nebo hackathon** | Rychlé ověření nápadu, zpětnou vazbu, kontakty a někdy i cenu nebo podporu. |
            | **Investor nebo business angel** | Kapitál, zkušenosti a kontakty výměnou za podíl nebo jinou formu dohody. |
            | **Univerzita nebo inovační centrum** | Odborníky, laboratoře, mentoring a propojení s výzkumem. |
            """)
            st.markdown("<div class='box-blue'><strong>🔍 Příklady podpory v ČR:</strong> CzechInvest a portál CzechStartups.gov.cz, regionální inovační centra jako JIC v Brně, startupové akcelerátory jako StartupYard, univerzitní inkubátory, podnikatelské soutěže, coworkingová centra a místní podnikatelská centra.</div>", unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 5.11 Proč stát a regiony startupy podporují")
            st.write("Startupy jsou podporované proto, že mohou přinášet nové produkty, pracovní místa, inovace a vyšší konkurenceschopnost ekonomiky. Ne každý startup uspěje, ale úspěšné projekty mohou vyrůst do firem, které platí daně, zaměstnávají lidi a přinášejí řešení využitelná i v zahraničí.")
            st.markdown("<div class='box-yellow'><strong>💡 Důvod podpory:</strong> Podpora startupů není „dárek zdarma“. Je to investice do nápadů, inovací, podnikavosti a budoucích firem, které mohou posílit ekonomiku.</div>", unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 5.12 Moderní startupové pilíře")
            st.write("Tradiční formy podnikání dnes doplňuje dynamický svět technologických startupů. Pochopení jejich pilířů — škálovatelnosti, inovací, práce s daty, rizikového kapitálu a rychlého ověřování nápadů — pomáhá studentům pochopit moderní digitální ekonomiku a proměny trhu práce.")
            st.write("Moderní startup dnes často nestaví jen na nápadu a právní formě. Musí umět chytře využívat technologie, pracovat efektivně, komunikovat s komunitou a zároveň myslet na dlouhodobou udržitelnost práce zakladatele.")
            st.markdown("<div class='box-blue'><strong>🚀 Moderní startupové pilíře:</strong> AI-First, Solopreneurship, Build in Public a Founder Wellbeing pomáhají přemýšlet o tom, jak bude projekt fungovat v praxi — nejen co prodává, ale také jak se tvoří, komunikuje a dlouhodobě zvládá.</div>", unsafe_allow_html=True)
            
            st.markdown("<div class='box-yellow'><strong>🧩 Interaktivní výzva:</strong> Vyber jeden pilíř z tabulky a doplň, jak by se mohl projevit ve tvém startupu.</div>", unsafe_allow_html=True)
            st.markdown("""
            | Téma | Proč na tom záleží | Jak to implementuji v mém projektu? |
            | :--- | :--- | :--- |
            | **AI-First** | Aby projekt nebyl jen „balíček“ běžných služeb, ale chytře využíval AI tam, kde dává smysl. | Zde si napíšeš, jak tvůj projekt využívá AI — například pro analýzu zákazníků, tvorbu obsahu, automatizaci podpory nebo návrh řešení. |
            | **Solopreneurship** | Efektivita jednoho člověka: i jednotlivec může díky nástrojům, šablonám a automatizacím zvládnout víc práce. | Zde si vypíšeš automatizace, které použiješ — například plánování příspěvků, fakturaci, odpovědi zákazníkům nebo sběr zpětné vazby. |
            | **Build in Public** | Budování komunity: lidé mohou sledovat vznik projektu, dávat zpětnou vazbu a stát se prvními zákazníky. | Zde si napíšeš plán příspěvků na sítě — co budeš sdílet, jak často a komu tím chceš pomoci. |
            | **Founder Wellbeing** | Prevence vyhoření: zakladatel projektu je důležitý zdroj energie, nápadů i rozhodování. | Zde si napíšeš své rituály pro psychohygienu — například odpočinek, hranice práce, pohyb, reflexi nebo pravidelné vyhodnocení zátěže. |
            """)
            
            st.write("**Jak s pilíři pracovat v mini projektu:**")
            st.markdown("""
            * U každého pilíře napiš jednu konkrétní větu.
            * Nepiš obecně „budu používat AI“ — napiš k čemu přesně.
            * U automatizací napiš, co ti ušetří čas.
            * U Build in Public napiš, komu budeš ukazovat postup a proč.
            * U Founder Wellbeing napiš, jak poznáš, že je toho na tebe moc.
            """)
            
            st.info("**Je dobré si pamatovat:** Startup začíná hypotézou, ne jistotou. Nejdřív se ověřuje problém a zákazník, potom se řeší velké investice. Podpora může mít podobu rad, kontaktů, prostoru, soutěže, programu nebo financování. I neúspěšný test má hodnotu, protože šetří čas a peníze.")
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
