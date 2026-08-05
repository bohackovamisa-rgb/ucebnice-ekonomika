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

    is_uvod = st.session_state["current_view"] == "Uvod"
    if st.button("Úvodní stránka", key="nav_uvod", use_container_width=True, type="primary" if is_uvod else "secondary"):
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
        btn_type = "primary" if is_active else "secondary"
        if st.button(title, key=f"nav_{key}", use_container_width=True, type=btn_type):
            st.session_state["current_view"] = key
            st.rerun()

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
        společné nástroje a odkaz do učitelského řídícího centra.
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

    if selected_section == "1. Podnikatel a základní pojmy":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 1</div>", unsafe_allow_html=True)
        st.markdown("## 1. Podnikatel a základní pojmy")
        with st.container(border=True):
            st.markdown("""
            <div class='box-blue'>
                <strong>Hlavní definice:</strong><br>
                Zákon chápe podnikání jako soustavnou činnost prováděnou samostatně, vlastním jménem, na vlastní odpovědnost, za účelem dosažení zisku.
            </div>
            """, unsafe_allow_html=True)
            st.write("Podnikání dnes nemusí začínat kanceláří. Může začít mobilem, profilem na sociální síti, prodejem digitální šablony nebo e-shopem.")
            st.markdown("### Tvůj úkol: Je to podnikání?")
            ex1 = st.selectbox("1. Student jednou prodá starý mobil:", ["Vyber odpověď...", "Koníček", "Jednorázový přivýdelek", "Zaměstnání", "Podnikání"], key="p1_ex1")
            
    elif selected_section == "13. Logická mapa podnikání":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 13</div>", unsafe_allow_html=True)
        st.markdown("## 13. Logická mapa podnikání")
        with st.container(border=True):
            st.markdown("""
            <div class='box-gray'>
                <strong>Přehled tématu:</strong> Tato mapa shrnuje hlavní oblasti podnikání od právního rámce přes právní formy až po záměr, rizika a ukončení podnikání.
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
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

    else:
        st.info("Vyberte podkapitolu z menu nahoře. (Ostatní podkapitoly jsou zkráceny pro přehlednost).")

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
        "2.8 Spoření, investování a spekulace"
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

    elif selected_section_2 == "2.2 Osobní finance a rozpočet":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.2</div>", unsafe_allow_html=True)
        st.markdown("## Osobní finance a rozpočet")
        with st.container(border=True):
            st.write("Osobní finance nejsou jen otázka toho, kolik člověk vydělává. Jsou to každodenní rozhodnutí: za co utratím peníze, co odložím, co si půjčím, jak poznám riziko.")
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

    elif selected_section_2 == "2.4 Matematika peněz":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.4</div>", unsafe_allow_html=True)
        st.markdown("## Matematika peněz: čas, úrok a inflace")
        with st.container(border=True):
            st.markdown("### Jednoduché a Složené úročení")
            st.markdown("""
            * **Jednoduché úročení:** úrok se počítá stále jen z původně vložené nebo půjčené částky.
            * **Složené úročení:** úročí se nejen původní částka, ale postupně i již připsané úroky nebo výnosy. Peníze tedy mohou vydělávat další peníze.
            """)

    elif selected_section_2 == "2.5 Finanční rezerva":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.5</div>", unsafe_allow_html=True)
        st.markdown("## Finanční rezerva: airbag osobních financí")
        with st.container(border=True):
            st.write("Finanční rezerva chrání člověka před tím, aby každá nečekaná situace skončila dluhem. Může jít o rozbitý telefon, ztrátu brigády, nemoc, opravu auta.")

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
            st.write("Cena věci není jen částka v korunách. Dá se přepočítat i na čas, který musí člověk pracovat, aby si ji mohl dovolit.")
            st.markdown("**Vzorec:** Cena věci ÷ čistá hodinová mzda = počet hodin práce")

    else:
        st.info("Tato sekce bude brzy doplněna.")

# ==========================================
# POKROKY A UČITEL
# ==========================================
elif view == "Pokroky":
    st.title("Moje pokroky")
    st.write("Přehled dokončených kapitol a uložených odpovědí.")

elif view == "Ucitel":
    st.title("Učitelská základna")
    st.write("Metodické pokyny a sledování práce jednotlivých žáků podle tříd.")

else:
    st.title(chapters.get(view, view))
    st.info("Tato kapitola čeká na vložení textu. Stačí poslat podklady.")
