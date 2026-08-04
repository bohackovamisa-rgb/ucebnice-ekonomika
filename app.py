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

# --- STYLOVÁNÍ (SAAS MINIMALISMUS / LUCIDE UI) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }

    .stApp {
        background-color: #f8fafc;
        color: #0f172a;
    }

    .main .block-container {
        max-width: 900px !important;
        padding-top: 2rem !important;
        padding-bottom: 5rem !important;
    }

    /* KARTY A KONTEJNERY */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #ffffff !important;
        border-radius: 12px !important;
        border: 1px solid #e2e8f0 !important;
        box-shadow: 0 1px 3px 0 rgba(15, 23, 42, 0.03) !important;
        padding: 1.75rem !important;
        margin-bottom: 1.25rem !important;
        transition: box-shadow 0.2s ease, border-color 0.2s ease;
    }

    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        border-color: #cbd5e1 !important;
        box-shadow: 0 4px 12px -2px rgba(15, 23, 42, 0.05) !important;
    }

    /* NADPISY */
    h1 {
        font-family: 'Montserrat', sans-serif !important;
        color: #0f172a !important;
        font-weight: 800 !important;
        font-size: 2.1rem !important;
        letter-spacing: -0.025em !important;
        line-height: 1.2 !important;
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
        display: flex;
        align-items: center;
        gap: 8px;
    }

    h3 {
        font-family: 'Montserrat', sans-serif !important;
        color: #334155 !important;
        font-weight: 600 !important;
        font-size: 1.05rem !important;
        margin-top: 1.25rem !important;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    p, li {
        font-family: 'Montserrat', sans-serif !important;
        color: #334155;
        font-size: 0.94rem;
        line-height: 1.7;
        font-weight: 400;
    }

    /* BAREVNÉ SYSTÉMOVÉ BOXY S VEKTOROVOU GRAFIKOU */
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

    .icon-svg {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        vertical-align: -3px;
        margin-right: 6px;
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

    .sub-section-header {
        color: #4f46e5;
        font-weight: 700;
        font-size: 0.85rem;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        display: flex;
        align-items: center;
        gap: 6px;
    }
    </style>
""", unsafe_allow_html=True)

# --- MODERNÍ LUCIDE VEKTOROVÉ IKONY (SVG STRINGY) ---
def get_icon(name, color="#4f46e5", size=18):
    icons = {
        "compass": f'<svg class="icon-svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>',
        "target": f'<svg class="icon-svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>',
        "book": f'<svg class="icon-svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>',
        "bot": f'<svg class="icon-svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="10" rx="2"/><circle cx="12" cy="5" r="2"/><path d="M12 7v4"/><line x1="8" y1="16" x2="8" y2="16"/><line x1="16" y1="16" x2="16" y2="16"/></svg>',
        "calc": f'<svg class="icon-svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2" width="16" height="20" rx="2"/><line x1="8" y1="6" x2="16" y2="6"/><line x1="16" y1="14" x2="16" y2="18"/><path d="M16 10h.01"/><path d="M12 10h.01"/><path d="M8 10h.01"/><path d="M12 14h.01"/><path d="M8 14h.01"/><path d="M12 18h.01"/><path d="M8 18h.01"/></svg>',
        "alert": f'<svg class="icon-svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>',
        "check": f'<svg class="icon-svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',
        "lightbulb": f'<svg class="icon-svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/></svg>',
        "puzzle": f'<svg class="icon-svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19.439 7.85c-.049-.322.059-.648.289-.878l1.568-1.568a2.41 2.41 0 0 0 0-3.408 2.41 2.41 0 0 0-3.408 0l-1.568 1.568c-.23.23-.556.338-.878.289a2.41 2.41 0 0 0-2.732 2.378V7a2 2 0 0 1-2 2H9a2 2 0 0 1-2-2v-.58a2.41 2.41 0 0 0-2.378-2.732c-.322-.049-.648.059-.878.289L2.176 5.545a2.41 2.41 0 0 0 0 3.408 2.41 2.41 0 0 0 3.408 0l1.568-1.568c.23-.23.556-.338.878-.289A2.41 2.41 0 0 0 10.41 9.47V10a2 2 0 0 1 2 2v1a2 2 0 0 1-2 2v.53a2.41 2.41 0 0 0 2.378 2.732c.322.049.648-.059.878-.289l1.568-1.568a2.41 2.41 0 0 0 0-3.408 2.41 2.41 0 0 0-3.408 0l-1.568 1.568c-.23.23-.556.338-.878.289a2.41 2.41 0 0 0-2.732-2.378V17a2 2 0 0 1-2-2h-1a2 2 0 0 1-2-2v-.53a2.41 2.41 0 0 0-2.378-2.732"/></svg>',
        "scale": f'<svg class="icon-svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m16 16 3-8 3 8a3 3 0 0 1-6 0z"/><path d="m2 16 3-8 3 8a3 3 0 0 1-6 0z"/><path d="M7 21h10"/><path d="M12 3v18"/><path d="M3 7h18"/></svg>'
    }
    return icons.get(name, "")

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
        st.markdown(f"<h2>{get_icon('compass', '#4f46e5', 22)} Začni tady</h2>", unsafe_allow_html=True)
        st.write("""
        Tahle stránka je hlavní rozcestník učebnice. Najdeš tu obsah, pravidla práce, výstupy kapitol, 
        společné nástroje a odkaz do učitelského řídícího centra. Propojuje podnikavost, osobní finance, výrobu, 
        trh práce, stát, daně, management a marketing s rozhodnutími z reálného života.
        """)
        
        st.markdown(f"""
        <div class='box-green'>
            <strong>{get_icon('target', '#166534', 18)} Cíl učebnice:</strong><br>
            Žák má umět propojit nápad, zákazníka, peníze, práci, stát, daně, marketing, rizika a odpovědnost do jednoho praktického rozhodování.
        </div>
        """, unsafe_allow_html=True)

    with st.container(border=True):
        st.markdown(f"<h2>{get_icon('book', '#4f46e5', 22)} Jak s učebnicí pracovat</h2>", unsafe_allow_html=True)
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

            st.markdown(f"""
            <div class='box-green'>
                <strong>{get_icon('check', '#166534', 18)} Příklad pro dnešní studenty:</strong> Když jednou prodáš staré tenisky, nejde obvykle o podnikání. Když ale pravidelně nakupuješ, upravuješ, propaguješ a prodáváš zboží se záměrem vydělat, už se blížíš podnikání a musíš řešit pravidla.
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
            st.markdown(f"### {get_icon('lightbulb', '#eab308', 20)} Tvůj úkol: Je to podnikání?")
            st.write("U každé situace rozhodni, zda jde spíš o koníček, jednorázový přivýdele, zaměstnání, nebo podnikání. Zdůvodni odpověď podle čtyř znaků podnikání.")

            ex1 = st.selectbox("1. Student jednou prodá starý mobil:", ["Vyber odpověď...", "Koníček", "Jednorázový přivýdelek", "Zaměstnání", "Podnikání"], key="p1_ex1")
            ex2 = st.selectbox("2. Student každý týden prodává vlastnoručně vyráběné náramky přes Instagram:", ["Vyber odpověď...", "Koníček", "Jednorázový přivýdelek", "Zaměstnání", "Podnikání"], key="p1_ex2")
            ex3 = st.selectbox("3. Student pracuje v kavárně podle rozpisu směn:", ["Vyber odpověď...", "Koníček", "Jednorázový přivýdelek", "Zaměstnání", "Podnikání"], key="p1_ex3")
            ex4 = st.selectbox("4. Student nabízí grafiku loga pro malé podniky a sám si domlouvá cenu:", ["Vyber odpověď...", "Koníček", "Jednorázový přivýdelek", "Zaměstnání", "Podnikání"], key="p1_ex4")
            ex5 = st.selectbox("5. Student vytvoří placený online kurz pro mladší žáky:", ["Vyber odpověď...", "Koníček", "Jednorázový přivýdelek", "Zaměstnání", "Podnikání"], key="p1_ex5")

            if st.button("Uložit vyhodnocení úkolu"):
                st.success("Odpovědi byly uloženy do vašeho profilu pokroků!")

        with st.container(border=True):
            st.markdown(f"### {get_icon('puzzle', '#4f46e5', 20)} Interaktivní výzva: vlastní nápad")
            user_idea = st.text_area("Popiš svůj nápad jednou větou a označ, jak v něm bude vidět soustavnost, samostatnost a odpovědnost:", placeholder="Můj nápad je...", height=100, key="p1_user_idea")
            if st.button("Uložit můj nápad"):
                st.success("Nápad uložen!")

        # AI MENTORING
        with st.container(border=True):
            st.markdown(f"### {get_icon('bot', '#a855f7', 22)} AI mentoring k podnikání")
            st.write("Použij tyto prompty pro analýzu svého nápadu s pomocí AI asistenta:")

            st.markdown(f"""
            <div class='box-purple'>
                <strong>{get_icon('bot', '#6b21a8', 16)} Prompt 1 — Analýza 4 znaků podnikání:</strong><br>
                Zeptej se mě na můj nápad a podle čtyř znaků podnikání mi vysvětli, jestli už jde o podnikání. U každého znaku mi dej jednu kontrolní otázku.
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class='box-purple'>
                <strong>{get_icon('bot', '#6b21a8', 16)} Prompt 2 — Rozlišení aktivity:</strong><br>
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
            st.markdown(f"""
            <div class='box-blue'>
                <strong>{get_icon('scale', '#0369a1', 18)} Proč jsou definice důležité:</strong> V podnikání nestačí používat pojmy „přibližně“. Výrazy jako podnikatel, fyzická osoba, právnická osoba nebo živnostenské oprávnění mají oporu v právních předpisech.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 📖 Přehledný slovníček pojmů")
            st.markdown("""
            | Termín | Co znamená | Proč je důležitý |
            | :--- | :--- | :--- |
            | **Podnikatel** | Osoba, která samostatně vykonává výdělečnou činnost na vlastní účet a odpovědnost se záměrem dělat ji soustavně za účelem dosažení zisku. | Pomáhá rozlišit, kdy už nejde jen o koníček nebo jednorázový přivýdelek. |
            | **Podnikání** | Soustavná samostatná činnost vykonávaná na vlastní odpovědnost za účelem dosažení zisku. | Je základním pojmem celé kapitoly a určuje, kdy vznikají právní a finanční povinnosti. |
            | **Fyzická osoba** | Člověk — jednotlivec. V podnikání může vystupovat například jako OSVČ. | Máš poznat rozdíl mezi človekem podnikatelem a firmou jako právnickou osobou. |
            | **Právnická osoba** | Organizovaný subjekt, který má právní osobnost. Typicky jde například o s.r.o., a.s., družstvo, spolek nebo nadaci. | Vysvětluje, proč firma může jednat, vlastnit majetek a nést odpovědnost samostatně. |
            | **OSVČ** | Osoba samostatně výdělečně činná — fyzická osoba, která podniká vlastním jménem a na vlastní odpovědnost. | Je častou formou začátku malého podnikání, freelancingu nebo služeb. |
            | **Živnost** | Podnikatelská činnost provozovaná podle živnostenského zákona, pokud splňuje zákonné podmínky. | Pomáhá určuje, jestli podnikatel potřebuje živnostenské oprávnění a jaký typ živnosti řeší. |
            | **Živnostenské oprávnění** | Právo provozovat živnost. U ohlašovacích živností vzniká zpravidla ohlášením, u koncesovaných živností až udělením koncese. | Bez něj nelze legálně provozovat činnost, která živnostenské oprávnění vyžaduje. |
            | **Volná živnost** | Živnost, u které není potřeba speciální vzdělání ani praxe; stačí splnit všeobecné podmínky. | Patří sem mnoho běžných začátků podnikání, například marketingové služby nebo e-shop. |
            | **Řemeslná živnost** | Živnost, která vyžaduje odbornou způsobilost, například výuční list nebo praxi. | Ukazuje, že některé činnosti nelze začít dělat bez kvalifikace. |
            | **Vázaná živnost** | Živnost, která vyžaduje specifické vzdělání, praxi nebo jinou zákonem stanovenou způsobilost. | Pomáhá pochopit, že u některých služeb stát chrání zákazníka požadavkem na odbornost. |
            | **Koncesovaná živnost** | Živnost, kterou lze provozovat až po udělení státního povolení — koncese. | Typicky jde o regulované nebo rizikovější činnosti. |
            | **Obchodní korporace** | Souhrnný pojem pro obchodní společnosti a družstva, například v.o.s., k.s., s.r.o., a.s. a družstvo. | Pomáhá zařadit základní právní formy podnikání. |
            | **Obchodní rejstřík** | Veřejný seznam, ve kterém se zapisují obchodní korporace a další zákonem stanovené subjekty. | Slouží k ověření firmy, její právní formy, sídla a osob, které za ni jednají. |
            | **Živnostenský rejstřík** | Evidence osob podnikajících na základě živnostenského oprávnění. | Slouží k ověření, zda má podnikatel oprávnění k určité činnosti. |
            | **Ručení** | Odpovědnost za dluhy a závazky podnikatele nebo firmy. | Je klíčové při volbě právní formy, protože OSVČ a některé společnosti nesou vyšší osobní riziko. |
            | **Švarcsystém** | Nelegální nastavení, kdy človek formálně vystupuje jako podnikatel, ale fakticky pracuje jako zaměstnanec. | Pomáhá rozpoznat rizikovou spolupráci a rozdíl mezi podnikáním a zaměstnáním. |
            | **CSR** | Společenská odpovědnost firem — přístup, kdy firma sleduje nejen zisk, ale i dopady na lidi, společnost a životní prostředí. | Ukazuje, že podnikání má také etický a společenský rozměr. |
            | **Lean Canvas** | Stručná mapa podnikatelského nápadu, která zachycuje problém, zákazníka, řešení, náklady, příjmy a rizika. | Pomáhá rychle ověřovat nápad dřív, než tým investuje hodně času nebo peněz. |
            | **MVP** | Minimální životaschopný produkt — nejmenší verze řešení, která umožní ověřit důležitý předpoklad. | Učí testovat nápad levně, rychle a bezpečně. |
            """)

        with st.container(border=True):
            st.markdown(f"### {get_icon('puzzle', '#4f46e5', 20)} Interaktivní výzva: Aplikace pojmů")
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
            st.markdown(f"### {get_icon('bot', '#a855f7', 22)} AI mentoring ke slovníčku")
            st.write("Zkopíruj tento prompt do svého AI asistenta:")
            st.markdown(f"""
            <div class='box-purple'>
                <strong>{get_icon('bot', '#6b21a8', 16)} Prompt pro AI asistenta:</strong><br>
                Vysvětli mi tyto pojmy na mém podnikatelském nápadu: podnikatel, fyzická osoba, právnická osoba a živnost.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown(f"""
            <div class='box-gray'>
                <strong>Opora v legislativě:</strong> Občanský zákoník, živnostenský zákon, zákon o obchodních korporacích a zákon o veřejných rejstřících.
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
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

            st.markdown(f"""
            <div class='box-green'>
                <strong>{get_icon('lightbulb', '#166534', 18)} Pravidlo pro začátečníka:</strong> To, co přijde na účet, není celé „moje výplata“. Část peněz patří na náklady, daně, sociální a zdravotní pojištění, rezervu a budoucí investice.
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"#### {get_icon('calc', '#2563eb', 20)} Mini simulace OSVČ & Kalkulačka hodinové sazby")
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

            st.markdown(f"""
            <div class='box-yellow'>
                <strong>{get_icon('puzzle', '#854d0e', 18)} Interaktivní výzva:</strong> Napiš, jestli by se tvůj projekt dal na začátku provozovat jako OSVČ, a uveď jedno hlavní riziko.
            </div>
            """, unsafe_allow_html=True)
            st.text_input("Váš projekt jako OSVČ + hlavní riziko:", placeholder="Napište odpověď...", key="p3_user_risk")

            st.markdown(f"""
            <div class='box-purple'>
                <strong>{get_icon('bot', '#6b21a8', 16)} AI mentoring:</strong> Zkopíruj tento prompt do AI asistenta:<br>
                <i>„Podívej se na můj nápad a navrhni, jaký typ živnosti by mohl připadat v úvahu a co si mám ověřit.“</i>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class='box-red'><strong>{get_icon('alert', '#991b1b', 18)} Hlavní riziko OSVČ:</strong> OSVČ ručí za závazky z podnikání celým svým osobním majetkem. Jednoduchý start tedy neznamená nulové riziko.</div>
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

            st.markdown(f"#### {get_icon('puzzle', '#4f46e5', 18)} Zařazení vlastního nápadu k živnosti")
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
            st.markdown(f"""
            <div class='box-green'>
                <strong>{get_icon('check', '#166534', 18)} Digitální praxe:</strong> Portál živnostenského podnikání (rzp.cz) a veřejné rejstříky slouží k ověřování údajů, podávání žádostí a kontrole obchodních partnerů.
            </div>
            """, unsafe_allow_html=True)
            st.text_area("Interaktivní výzva: Sepiš první tři kroky, které bys udělal/a před ohlášením živnosti u svého projektu:", placeholder="1. krok...\n2. krok...\n3. krok...", height=90, key="p3_steps_user")

        with st.container(border=True):
            st.markdown("### 3.6 Povinnosti živnostníka: legislativní minimum")
            st.write("Živnostník neřeší jen zákazníky a cenu. Musí také splnit základní registrační, daňové a pojistné povinnosti.")
            
            st.markdown(f"""
            <div class='box-blue'>
                <strong>{get_icon('scale', '#0369a1', 18)} Legislativní minimum pro OSVČ:</strong> Přesné částky a termíny se mohou měnit, proto je potřeba ověřovat aktuální informace na stránkách Finanční správy, ČSSZ, zdravotní pojišťovny a Portálu živnostenského podnikání.
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

            st.markdown(f"""
            <div class='box-yellow'>
                <strong>{get_icon('lightbulb', '#854d0e', 18)} Praktické pravidlo:</strong> Živnostník by si měl od každé přijaté platby odkládat část peněz na daň, sociální a zdravotní pojištění. To, co přijde na účet, ještě není čistý příjem.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 3.7 Daně a odvody OSVČ úplně jednoduše")
            st.markdown(f"""
            <div class='box-red'>
                <strong>{get_icon('alert', '#991b1b', 18)} Důležité zjednodušení:</strong> Přesné částky se každý rok mění. V první kapitole stačí pochopit princip: OSVČ platí daň z příjmů a odvody na sociální a zdravotní pojištění.
            </div>
            """, unsafe_allow_html=True)

            st.write("""
            **Co OSVČ typicky platí?**
            * **Daň z příjmů FO:** základní sazba 15 % ze základu daně (zisk = příjmy − výdaje).
            * **Sociální pojištění:** na důchodový systém a státní politiku zaměstnanosti.
            * **Zdravotní pojištění:** na financování zdravotní péče.
            * **Zálohy:** pravidelné měsíční platby během roku.
            """)

            st.markdown(f"""
            <div class='box-blue'>
                <strong>{get_icon('calc', '#0369a1', 18)} Jednoduchý příklad:</strong> Jana má za rok příjmy 300 000 Kč a výdaje 120 000 Kč. Její zisk je tedy 180 000 Kč. Z tohoto zisku se teprve počítá daň a pojistné. Neznamená to, že si může celých 180 000 Kč nechat bez dalších povinností.
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"#### {get_icon('calc', '#2563eb', 20)} Modelový výpočet odvodů OSVČ (2026)")
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

            st.markdown(f"""
            <div class='box-yellow'>
                <strong>{get_icon('lightbulb', '#854d0e', 18)} Praktické pravidlo pro začátečníka:</strong> Když OSVČ dostane zaplaceno, neměla by všechno utratit. Část peněz si musí odložit na daň, sociální a zdravotní pojištění.
            </div>
            """, unsafe_allow_html=True)

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
