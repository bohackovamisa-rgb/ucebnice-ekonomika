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

        with st.container(border=True):
            st.markdown("### 1.1 Podnikatel v realitě současné generace")
            st.write("""
            Podnikání dnes nemusí začínat kanceláří, provozovnou ani výrobní halou. Může začít mobilem, profilem na sociální síti, prodejem digitální šablony, správou obsahu pro lokální firmu, výrobou merch produktů, doučováním, e-shopem, aplikací, kurzem, grafickou službou, tvorbou videí nebo komunitním projektem.
            """)

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
            st.markdown("### Tvůj úkol: Je to podnikání?")
            st.write("U každé situace rozhodni, zda jde spíš o koníček, jednorázový přivýdelek, zaměstnání, nebo podnikání. Zdůvodni odpověď podle čtyř znaků podnikání.")

            ex1 = st.selectbox("1. Student jednou prodá starý mobil:", ["Vyber odpověď...", "Koníček", "Jednorázový přivýdelek", "Zaměstnání", "Podnikání"], key="p1_ex1")
            ex2 = st.selectbox("2. Student každý týden prodává vlastnoručně vyráběné náramky přes Instagram:", ["Vyber odpověď...", "Koníček", "Jednorázový přivýdelek", "Zaměstnání", "Podnikání"], key="p1_ex2")
            ex3 = st.selectbox("3. Student pracuje v kavárně podle rozpisu směn:", ["Vyber odpověď...", "Koníček", "Jednorázový přivýdelek", "Zaměstnání", "Podnikání"], key="p1_ex3")
            
            if st.button("Uložit vyhodnocení úkolu"):
                st.success("Odpovědi byly uloženy do vašeho profilu pokroků!")

    elif selected_section == "2. Slovníček základních pojmů":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2</div>", unsafe_allow_html=True)
        st.markdown("## 2. Slovníček základních pojmů")
        
        with st.container(border=True):
            st.markdown("""
            | Termín | Co znamená | Proč je důležitý |
            | :--- | :--- | :--- |
            | **Podnikatel** | Osoba, která samostatně vykonává výdělečnou činnost na vlastní účet a odpovědnost se záměrem dělat ji soustavně za účelem dosažení zisku. | Pomáhá rozlišit, kdy už nejde jen o koníček nebo jednorázový přivýdelek. |
            | **Podnikání** | Soustavná samostatná činnost vykonávaná na vlastní odpovědnost za účelem dosažení zisku. | Je základním pojmem celé kapitoly a určuje, kdy vznikají právní a finanční povinnosti. |
            | **Fyzická osoba** | Člověk — jednotlivec. V podnikání může vystupovat například jako OSVČ. | Máš poznat rozdíl mezi člověkem podnikatelem a firmou jako právnickou osobou. |
            | **Právnická osoba** | Organizovaný subjekt, který má právní osobnost. Typicky jde například o s.r.o., a.s., družstvo, spolek nebo nadaci. | Vysvětluje, proč firma může jednat, vlastnit majetek a nést odpovědnost samostatně. |
            | **OSVČ** | Osoba samostatně výdělečně činná — fyzická osoba, která podniká vlastním jménem a na vlastní odpovědnost. | Je častou formou začátku malého podnikání, freelancingu nebo služeb. |
            """)

    elif selected_section == "3. OSVČ a živnosti":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 3</div>", unsafe_allow_html=True)
        st.markdown("## 3. OSVČ a živnosti")
        
        with st.container(border=True):
            st.write("**OSVČ** znamená osoba samostatně výdělečně činná. Jde o podnikání fyzické osoby — tedy člověka, který podniká vlastním jménem a nese za své podnikání plnou odpovědnost.")

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

    elif selected_section == "4. Obchodní korporace":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 4</div>", unsafe_allow_html=True)
        st.markdown("## 4. Obchodní korporace")
        
        with st.container(border=True):
            st.markdown("### 4.4 Volba právní formy podle situace (9 otázek: OSVČ, nebo s.r.o.?)")
            st.write("U každé otázky vyber odpověď, která lépe odpovídá tvému projektu:")

            q1 = st.radio("1️⃣ Plánuješ podnikat sám/sama, nebo v týmu?", ["Spíš OSVČ: Podnikám sám/sama a rozhoduji hlavně za sebe.", "Spíš s.r.o.: Podnikáme v týmu a potřebujeme jasně rozdělit role, odpovědnost a podíly."], key="q1_full")
            q2 = st.radio("2️⃣ Jde hlavně o osobní práci, nebo projekt s růstem?", ["Spíš OSVČ: Nabízím hlavně vlastní práci, službu nebo dovednost.", "Spíš s.r.o.: Projekt má růst, rozšiřovat se a fungovat jako samostatná firma."], key="q2_full")
            
            if st.button("Vyhodnotit test (Ukázka)"):
                st.success("Test uložen.")

    elif selected_section == "5. Startup: nápad, který hledá byznys":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 5</div>", unsafe_allow_html=True)
        st.markdown("## 5. Startup: nápad, který hledá funkční byznys")
        
        with st.container(border=True):
            st.write("Startup je mladý podnikatelský projekt, který hledá opakovatelný a škálovatelný způsob, jak řešit problém zákazníka.")
            
            st.markdown("#### 🎯 SIMULACE: Máš nápad na novou aplikaci. Co uděláš jako první?")
            sim_choice = st.radio("Vyber odpověď:", ["A) Utratím 200 000 Kč za vývoj plné verze", "B) Udělám jednoduchý dotazník a jednoduchý web pro zájemce"], key="p5_sim_app")
            
            if st.button("Vyhodnotit simulaci"):
                if "A)" in sim_choice:
                    st.markdown("<div class='box-red'>❌ <strong>CHYBA!</strong> Utratil jsi peníze a zbytečně postavil něco, co lidé nechtějí. Chybělo ti otestování nápadu.</div>", unsafe_allow_html=True)
                else:
                    st.markdown("<div class='box-green'>🎉 <strong>SKVĚLE!</strong> Získal jsi zdarma 500 zájemců a ověřil trh. Můžeš bezpečně stavět MVP!</div>", unsafe_allow_html=True)

    elif selected_section == "6. Podnikatelský záměr":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 6</div>", unsafe_allow_html=True)
        st.markdown("## 6. Podnikatelský záměr")
        
        with st.container(border=True):
            st.markdown("#### 🧮 Interaktivní kalkulačka bodu zvratu (Break-even point)")
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

    elif selected_section == "7. Lean Canvas":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 7</div>", unsafe_allow_html=True)
        st.markdown("## 7. Lean Canvas")
        
        with st.container(border=True):
            st.markdown("### 🗂️ 7.9 Od teorie k praxi: Pracovní Lean Canvas")
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

            if st.button("💾 Uložit pracovní Lean Canvas", use_container_width=True):
                st.success("Tento pracovní Lean Canvas byl úspěšně uložen do vašeho profilu pokroků!")

    elif selected_section == "8. CSR, etika a odpovědné podnikání":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 8</div>", unsafe_allow_html=True)
        st.markdown("## 8. CSR, etika a odpovědné podnikání")
        with st.container(border=True):
            st.write("Společenská odpovědnost firem (ESG) a etické rozhodování v praxi.")

    elif selected_section == "9. Rizika podnikání":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 9</div>", unsafe_allow_html=True)
        st.markdown("## 9. Rizika podnikání")
        with st.container(border=True):
            st.write("Identifikace, matice rizik a preventivní opatření.")

    elif selected_section == "10. Švarcsystém":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 10</div>", unsafe_allow_html=True)
        st.markdown("## 10. Švarcsystém")
        with st.container(border=True):
            st.markdown("<div class='box-red'><strong>Pozor na švarcsystém:</strong> Zastřený pracovněprávní vztah je nelegální.</div>", unsafe_allow_html=True)
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

    elif selected_section == "11. Ověřování informací a užitečné zdroje":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 11</div>", unsafe_allow_html=True)
        st.markdown("## 11. Ověřování informací a užitečné zdroje")
        with st.container(border=True):
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

    elif selected_section == "12. Ukončení podnikání":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 12</div>", unsafe_allow_html=True)
        st.markdown("## 12. Ukončení podnikání")
        with st.container(border=True):
            st.text_input("🧩 Interaktivní výzva: Vysvětli vlastními slovy rozdíl mezi zrušením a zánikem firmy na jednoduchém příkladu:", placeholder="Zrušení vs zánik...", key="p12_cancel_vs_end")
            with st.expander("💡 Zobrazit správné vysvětlení (Zrušení vs. Zánik)"):
                st.markdown("""
                * **Zrušení = proces:** Rozhodnutí, že firma končí. Může následovat likvidace, vypořádání majetku, dluhů a závazků.
                * **Zánik = konec:** Definitivní okamžik, kdy firma právně přestává existovat. Obchodní korporace zaniká výmazem z obchodního rejstříku.
                """)

    elif selected_section == "13. Logická mapa podnikání":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 13</div>", unsafe_allow_html=True)
        st.markdown("## 13. Logická mapa podnikání")
        with st.container(border=True):
            st.markdown("### Vizualizace logické mapy podnikání:")
            st.markdown("""
            <div class="mindmap-wrapper">
                <div class="mm-col">
                    <div class="mm-node">
                        <div class="mm-title">1. Legislativa a definice</div>
                        <ul>
                            <li>občanský zákoník</li>
                            <li>živnostenský zákon</li>
                            <li>ZOK</li>
                            <li>znaky podnikání</li>
                        </ul>
                    </div>
                    <div class="mm-node">
                        <div class="mm-title">2. Právní formy</div>
                        <ul>
                            <li>OSVČ, v.o.s., k.s.</li>
                            <li>s.r.o., a.s.</li>
                        </ul>
                    </div>
                    <div class="mm-node">
                        <div class="mm-title">3. Záměr a Lean Canvas</div>
                        <ul>
                            <li>zákazník a problém</li>
                            <li>řešení, první test</li>
                            <li>náklady a příjmy</li>
                        </ul>
                    </div>
                </div>
                
                <div class="mm-center">
                    PODNIKÁNÍ<br>
                    <span style="font-size:0.9rem; font-weight: 500;">Logická mapa</span>
                </div>
                
                <div class="mm-col">
                    <div class="mm-node">
                        <div class="mm-title">4. CSR a etika</div>
                        <ul>
                            <li>férové jednání</li>
                            <li>odpovědnost (zaměstnanci, společnost, prostředí)</li>
                        </ul>
                    </div>
                    <div class="mm-node">
                        <div class="mm-title">5. Rizika</div>
                        <ul>
                            <li>finanční riziko</li>
                            <li>právní a tržní riziko</li>
                            <li>švarcsystém</li>
                        </ul>
                    </div>
                    <div class="mm-node">
                        <div class="mm-title">6. Zdroje a ukončení</div>
                        <ul>
                            <li>veřejné rejstříky</li>
                            <li>zrušení a zánik</li>
                            <li>insolvence</li>
                        </ul>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    elif selected_section == "14. Reflexe a sebehodnocení":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 14</div>", unsafe_allow_html=True)
        st.markdown("## 14. Reflexe a sebehodnocení")
        with st.container(border=True):
            st.write("Vyhodnocení vlastní práce a posunu v kapitole.")

    elif selected_section == "15. Integrované opakování":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 15</div>", unsafe_allow_html=True)
        st.markdown("## 15. Integrované opakování")
        with st.container(border=True):
            st.write("Závěrečný test a souhrnné aktivity Kapitoly 1.")


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
            st.write("Cena věci není jen částka v korunách. Dá se přepočítat i na čas, který musí člověk pracovat, aby si ji mohl dovolit.")
            st.markdown("**Vzorec:** Cena věci ÷ čistá hodinová mzda = počet hodin práce")

    elif selected_section_2 == "2.7 Finanční trh a analýza rizik":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.7</div>", unsafe_allow_html=True)
        st.markdown("## Finanční trh a analýza rizik")
        
        with st.container(border=True):
            st.write("Finanční trh umožňuje, aby se peníze přesouvaly od těch, kteří je mají k dispozici, k těm, kteří je chtějí využít.")

            st.markdown("""
            **Trojúhelník investování:**
            1. **Výnos:** to, co investor získá navíc oproti původně vložené částce.
            2. **Riziko:** možnost, že výsledek bude jiný, než člověk očekával (ztráta, kolísání).
            3. **Likvidita:** jak snadno lze aktivum proměnit zpět na peníze.
            """)

            st.markdown("""
            <div class='box-yellow'>
                <strong>Pravidlo:</strong> Vyšší možný výnos obvykle znamená vyšší riziko. Vysoký výnos, nulové riziko a okamžitá dostupnost peněz najednou jsou podezřelá kombinace.
            </div>
            """, unsafe_allow_html=True)

    elif selected_section_2 == "2.8 Spoření, investování a spekulace":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.8</div>", unsafe_allow_html=True)
        st.markdown("## Spoření, investování a spekulace")
        
        with st.container(border=True):
            st.write("Tato tři slova se často pletou, ale znamenají rozdílné chování.")

            st.markdown("""
            | Pojem | Co znamená | Typický příklad | Riziko |
            | :--- | :--- | :--- | :--- |
            | **Spoření** | Odkládání peněz s důrazem na bezpečnost a dostupnost. | Spořicí účet, termínovaný vklad. | Nízké, ale hrozí ztráta kupní síly kvůli inflaci. |
            | **Investování** | Vkládání peněz do aktiv s cílem dlouhodobého zhodnocení. | Akcie, dluhopisy, fondy, ETF. | Střední až vysoké podle produktu. |
            | **Spekulace** | Sázka na krátkodobý pohyb ceny. | Rychlé nákupy a prodeje kryptoměn. | Vysoké. |
            """)

    elif selected_section_2 == "2.9 Cenné papíry v praxi":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.9</div>", unsafe_allow_html=True)
        st.markdown("## Cenné papíry v praxi")
        
        with st.container(border=True):
            st.write("Cenný papír je listina nebo digitální záznam, se kterým jsou spojena určitá práva.")

            st.markdown("""
            * **Akcie:** Podíl na akciové společnosti. Koupí akcie firmě nepůjčuješ, kupuješ si kousek jejího vlastnictví a podílíš se na jejím úspěchu i neúspěchu.
            * **Dluhopis:** Cenný papír, kterým si emitent (stát, firma) půjčuje peníze. Kupuješ dluh, stáváš se věřitelem. Očekáváš úrok.
            * **Podílové listy / ETF:** Podíl na majetku fondu. Místo jedné akcie kupuješ „košík“ plný různých aktiv.
            """)

            st.markdown("""
            <div class='box-blue'>
                <strong>Srovnání základních produktů:</strong><br>
                • Spořicí účet (nízké riziko, jistota, vliv inflace)<br>
                • Dluhopis (riziko nesplacení emitentem)<br>
                • Akcie (podíl na firmě, růst ceny, dividenda, riziko poklesu trhu)<br>
                • ETF (investice do celého indexu, nižší riziko než jedna akcie)
            </div>
            """, unsafe_allow_html=True)

    elif selected_section_2 == "2.10 Kryptoměny":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.10</div>", unsafe_allow_html=True)
        st.markdown("## Kryptoměny: technologie, peníze, spekulace i riziko")
        
        with st.container(border=True):
            st.write("Kryptoměny jsou digitální aktiva, která existují v počítačové síti (Blockchain). Záznamy o vlastnictví a převodech nejsou vedeny jednou bankou, ale sdílenou evidencí transakcí.")

            st.markdown("""
            | Typ | Co je hlavní myšlenka | Riziko |
            | :--- | :--- | :--- |
            | **Bitcoin** | První a nejznámější kryptoměna, digitální vzácné aktivum. | Vysoká volatilita, regulace. |
            | **Ethereum** | Síť umožňující chytré kontrakty a decentralizované aplikace. | Technologická složitost, kolísání ceny. |
            | **Stablecoiny** | Tokeny, které se snaží držet hodnotu vůči měně (např. dolaru). | Riziko emitenta, ztráty navázání. |
            | **Meme coiny** | Tokeny postavené na humoru a virálním trendu. | Extrémní spekulace, prudké pády na nulu. |
            """)

            st.markdown("""
            <div class='box-red'>
                <strong>Největší rizika kryptoměn:</strong> Volatilita (cena prudce kolísá), Ztráta přístupu (ztráta seed phrase = konec), Hack burzy, Krypto podvody (sliby garantovaného výnosu).
            </div>
            """, unsafe_allow_html=True)

    elif selected_section_2 == "2.11 Úvěry, pojištění a majetek":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.11</div>", unsafe_allow_html=True)
        st.markdown("## Úvěry, pojištění a ochrana majetku")
        
        with st.container(border=True):
            st.write("Úvěr není „peníze zdarma“. Je to závazek, který přesouvá spotřebu nebo investici z budoucnosti do současnosti.")

            st.markdown("""
            **Úrok vs. RPSN:**
            * **Úrok:** cena za půjčení peněz (často marketingově lákavá).
            * **RPSN (Roční procentní sazba nákladů):** skutečná cena úvěru za rok, započítávající i všechny poplatky, pojištění a náklady na vyřízení.
            """)

            st.markdown("""
            <div class='box-gray'>
                <strong>BNPL (Buy Now, Pay Later - Kup teď, zaplať později):</strong><br>
                Pro současnou generaci velmi lákavé. Tváří se jako pohodlná platba, ale je to skrytý dluh, který může podpořit impulzivní nakupování věcí, na které člověk reálně nemá.
            </div>
            """, unsafe_allow_html=True)

            st.markdown("### Pojištění")
            st.write("Pojištění nezabrání tomu, aby se něco stalo, ale může snížit finanční škodu. Zřizujeme si ho na události, které by zničily náš rozpočet (invalidita, zničení domu, velká škoda někomu jinému).")

    elif selected_section_2 == "2.12 Finanční řízení podniku":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.12</div>", unsafe_allow_html=True)
        st.markdown("## Finanční řízení v podniku — most k podnikavosti")
        
        with st.container(border=True):
            st.write("Finanční řízení pomáhá firmě odpovědět: Kolik vydělává? Má peníze na účtu? Zvládne splácet? Vyplatí se růst?")

            st.markdown("""
            ### Základní finanční výkazy
            * **Rozvaha:** Fotografie firmy. Ukazuje, co firma vlastní (Aktiva) a z čeho je to financované (Pasiva).
            * **Výkaz zisku a ztráty:** Film za určité období. Výnosy minus Náklady = Zisk (nebo Ztráta).
            * **Cashflow (Peněžní toky):** Skutečný tok peněz. Firma může být zisková, ale zkrachovat, pokud jí chybí hotovost (např. zákazníci neplatí faktury včas).
            """)

            st.markdown("""
            ### Zdroje financování
            * **Vlastní kapitál:** Peníze majitele, zisk ponechaný ve firmě (bezpečnější, ale pomalejší).
            * **Cizí zdroje:** Úvěr z banky, vydané dluhopisy (rychlejší růst, ale dluh se musí splácet i ve špatných časech).
            """)

    elif selected_section_2 == "2.13 Finanční analýza: E-shop DropZone":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.13</div>", unsafe_allow_html=True)
        st.markdown("## Modelová finanční analýza: e-shop „DropZone“")
        
        with st.container(border=True):
            st.write("Zde vidíš data fiktivního studentského e-shopu prodávajícího merch. V tabulce zjistíš, že ačkoliv firmě rostou tržby a zisk, zhoršuje se jí likvidita.")

            st.markdown("""
            | Položka | Rok 1 | Rok 2 |
            | :--- | :--- | :--- |
            | **Tržby** | 800 000 Kč | 1 200 000 Kč |
            | **Zisk** | 60 000 Kč | 120 000 Kč |
            | **Aktiva celkem** | 500 000 Kč | 700 000 Kč |
            | **Peníze** | 45 000 Kč | 35 000 Kč |
            | **Krátkodobé závazky** | 140 000 Kč | 230 000 Kč |
            """)

            st.markdown("""
            | Ukazatel | Výpočet Rok 1 | Výsledek Rok 1 | Výpočet Rok 2 | Výsledek Rok 2 |
            | :--- | :--- | :--- | :--- | :--- |
            | **ROS (Rentabilita tržeb)** | 60k ÷ 800k × 100 | **7,5 %** | 120k ÷ 1,2M × 100 | **10 %** |
            | **Okamžitá likvidita** | 45k ÷ 140k | **0,32** | 35k ÷ 230k | **0,15** |
            | **Celková zadluženost** | 250k ÷ 500k × 100 | **50 %** | 400k ÷ 700k × 100 | **57,1 %** |
            """)

            st.markdown("""
            <div class='box-yellow'>
                <strong>Interpretace (Závěr finanční analýzy):</strong><br>
                Firma meziročně zvýšila tržby i zisk, což ukazuje lepší ziskovost a rostoucí poptávku. Zároveň se ale zhoršila likvidita a vzrostly krátkodobé závazky, takže největším rizikem je nedostatek peněz na včasné platby (peníze klesly ze 45k na 35k, závazky stouply na 230k). E-shop musí lépe hlídat cashflow a zásoby.
            </div>
            """, unsafe_allow_html=True)

    elif selected_section_2 == "2.14 Závěrečné interaktivní opakování":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.14</div>", unsafe_allow_html=True)
        st.markdown("## Závěrečné interaktivní opakování (Finance)")
        
        with st.container(border=True):
            st.markdown("### 🧠 Otestuj své znalosti financí")
            
            with st.expander("❓ 1. Jaký je rozdíl mezi debetní a kreditní kartou?"):
                st.markdown("<div class='box-blue'><strong>Odpověď:</strong> U debetní karty platíš svými vlastními penězi z účtu. U kreditní karty platíš penězi banky (jde o úvěr), které musíš později splatit.</div>", unsafe_allow_html=True)
                
            with st.expander("❓ 2. Co je to RPSN?"):
                st.markdown("<div class='box-blue'><strong>Odpověď:</strong> Roční procentní sazba nákladů. Udává skutečnou cenu úvěru za rok, protože na rozdíl od samotného úroku obsahuje i všechny poplatky spojené s úvěrem.</div>", unsafe_allow_html=True)

            with st.expander("❓ 3. Proč by měla firma sledovat Cashflow, i když je v zisku?"):
                st.markdown("<div class='box-blue'><strong>Odpověď:</strong> Protože zisk je jen účetní rozdíl mezi výnosy a náklady. Zákazníci mohou platit faktury pozdě. Pokud firma nemá reálnou hotovost (cashflow) na zaplacení svých aktuálních účtů, může zkrachovat i přes to, že je na papíře v zisku.</div>", unsafe_allow_html=True)

            with st.expander("❓ 4. Který z těchto nástrojů se nejvíce hodí na uchování finanční rezervy (3 měsíce výdajů) a proč? a) Akcie b) Spořicí účet c) Kryptoměny"):
                st.markdown("<div class='box-blue'><strong>Odpověď: b) Spořicí účet.</strong><br>Finanční rezerva musí být rychle dostupná (vysoká likvidita) a nesmí kolísat její hodnota (nízké riziko). Akcie a kryptoměny kolísají a mohly by v době, kdy peníze akutně potřebuješ, být ve ztrátě.</div>", unsafe_allow_html=True)


elif view == "Pokroky":
    st.markdown("<span class='hero-badge'>Studentská zóna</span>", unsafe_allow_html=True)
    st.title("Moje pokroky")
    st.markdown("<p style='font-size: 1rem; color: #64748b; margin-bottom: 2rem;'>Přehled dokončených kapitol, uložených odpovědí a rozpracovaných projektů.</p>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        with st.container(border=True):
            st.metric(label="Dokončené kapitoly", value="2 / 6", delta="33 %")
    with c2:
        with st.container(border=True):
            st.metric(label="Test právní formy", value="Hotovo", delta="OSVČ vs s.r.o.")
    with c3:
        with st.container(border=True):
            st.metric(label="Aktivní kalkulace", value="Bod zvratu", delta="Dokončeno")

elif view == "Ucitel":
    st.markdown("<span class='hero-badge'>Metodik & Dashboard</span>", unsafe_allow_html=True)
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
            st.markdown("**Vyplněné úkoly Kapitoly 1 a 2:**")
            st.markdown("• Test právní formy: *Vyplněno*")
            st.markdown("• Bod zvratu kalkulace: *Vyplněno*")
            st.text_area("Napsat žákovi poznámku / schválení záměru:", placeholder="Zpětná vazba...", key=f"note_{selected_student}")

    with tab_metodika:
        with st.container(border=True):
            st.header("Projektové aktivity do hodin (Kapitola 1 a 2)")
            st.write("Aktivita: Vyhledávání reálných firem v obchodním rejstříku Justice.cz.")
            st.write("Aktivita: Tvorba firemního rozpočtu a posouzení Cashflow.")

else:
    st.markdown("<span class='hero-badge'>Kapitola</span>", unsafe_allow_html=True)
    st.title(chapters.get(view, view))
    with st.container(border=True):
        st.info("Tato kapitola čeká na vložení textu. Stačí poslat podklady.")
