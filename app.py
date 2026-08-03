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

    /* LEGENDA UČEBNICE - BAREVNÉ BLOKY PODLE DESIGN SYSTEMU */
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
    </style>
""", unsafe_allow_html=True)

# --- MODERNÍ LINETYPE SVG IKONY ---
SVG_COMPASS = '<svg class="icon-inline" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#4f46e5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>'
SVG_TARGET = '<svg class="icon-inline" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>'
SVG_BOOK = '<svg class="icon-inline" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#4f46e5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>'
SVG_TOOL = '<svg class="icon-inline" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>'
SVG_CHART = '<svg class="icon-inline" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#2563eb" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>'
SVG_TEACHER = '<svg class="icon-inline" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>'
SVG_DICT = '<svg class="icon-inline" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#0284c7" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m16 6 4 14"/><path d="M12 6v14"/><path d="M8 8v12"/><path d="M4 4v16"/></svg>'
SVG_PROJ = '<svg class="icon-inline" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#4f46e5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20h16a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.93a2 2 0 0 1-1.66-.9l-.82-1.2A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2z"/></svg>'

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

    with st.container(border=True):
        st.markdown("<h2>Legenda učebnice</h2>", unsafe_allow_html=True)
        st.markdown("""
        <div class='box-blue'><strong>Modrá</strong> = Výklad, struktura, důležité vysvětlení</div>
        <div class='box-yellow'><strong>Žlutá</strong> = Úkol, otázka, aktivita, procvičení</div>
        <div class='box-purple'><strong>Fialová</strong> = AI mentoring a práce s asistencí</div>
        <div class='box-green'><strong>Zelená</strong> = Praxe, doporučení, dobrý postup</div>
        <div class='box-red'><strong>Červená / Oranžová</strong> = Riziko, varování, právní nebo etický problém</div>
        <div class='box-gray'><strong>Šedá</strong> = Zdroje, ověřování, učitelské nebo organizační poznámky</div>
        """, unsafe_allow_html=True)

    st.markdown(f"<h2>{SVG_TOOL} Společné nástroje učebnice</h2>", unsafe_allow_html=True)
    st.write("Tyto nástroje propojují kapitoly do jedné učebnice. Slouží k opakování, projektu, sledování pokroku a práci s pojmy.")

    c1, c2 = st.columns(2)
    with c1:
        with st.container(border=True):
            st.markdown(f"### {SVG_DICT} Slovníček pojmů", unsafe_allow_html=True)
            st.write("Společné místo pro pojmy napříč kapitolami: podnikatel, rozpočet, náklady, mzda, daň, marketing, CSR, KPI a další.")
        with st.container(border=True):
            st.markdown(f"### {SVG_PROJ} Závěrečný projekt", unsafe_allow_html=True)
            st.write("Žák nebo tým navrhne vlastní projekt a obhájí ho podle zákazníka, nákladů, právní formy, rizik, etiky a marketingu.")
    with c2:
        with st.container(border=True):
            st.markdown(f"### {SVG_CHART} Databáze aktivit", unsafe_allow_html=True)
            st.write("Přehled úkolů, případových studií, výpočtů, reflexí a AI mentoring promptů.")
        with st.container(border=True):
            st.markdown(f"### {SVG_TEACHER} Sebehodnocení", unsafe_allow_html=True)
            st.write("Na konci kapitoly i celé učebnice žák vyhodnotí, co už umí vysvětlit, použít a obhájit.")

elif view == "Kapitola 1":
    st.markdown("<span style='color: #6366f1; font-weight: 700; font-size: 0.8rem; letter-spacing: 0.08em;'>KAPITOLA 1</span>", unsafe_allow_html=True)
    st.title("Podnikavost a startupová kultura")
    st.markdown("<p style='font-size: 1rem; color: #64748b; margin-bottom: 2rem;'>Od nápadu k odpovědnému podnikání, ověření projektu a výběru právní formy.</p>", unsafe_allow_html=True)

    # Záložky kapitoly
    tab_vyklad, tab_korporace, tab_ukoly, tab_slovnicek = st.tabs([
        "1–3. Podnikatel & OSVČ", 
        "4. Obchodní korporace", 
        "Pracovní úkoly & Test", 
        "Slovníček pojmů"
    ])

    with tab_vyklad:
        # Úvodní blok
        with st.container(border=True):
            st.markdown("### 🎯 Úvod kapitoly")
            st.write("""
            Máš předpoklady stát se zakladatelem startupu? V této kapitole zjistíš, jak převést nápad na ověřitelný projekt, 
            jak zvolit právní formu a jak přemýšlet o rizicích, etice i odpovědnosti.
            """)
            st.markdown("""
            <div class='box-green'>
                <strong>Rychlá orientace:</strong><br>
                • <strong>Téma:</strong> Podnikavost, startup, právní formy, Lean Canvas<br>
                • <strong>Výstup:</strong> Návrh mini projektu<br>
                • <strong>Způsob práce:</strong> Rozhodování, ověřování, počítání, reflexe
            </div>
            """, unsafe_allow_html=True)

        # 1. Podnikatel
        with st.container(border=True):
            st.markdown("## 1. Podnikatel a základní definice")
            st.markdown("""
            <div class='box-blue'>
                <strong>Základní definice podnikání:</strong><br>
                Zákon chápe podnikání jako soustavnou činnost prováděnou samostatně, vlastním jménem, na vlastní odpovědnost, za účelem dosažení zisku.
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class='box-gray'>
                <strong>Přesná zákonná opora:</strong> Podnikatele definuje občanský zákoník (č. 89/2012 Sb., § 420 odst. 1).
            </div>
            """, unsafe_allow_html=True)

        # 3. OSVČ a živnosti
        with st.container(border=True):
            st.markdown("## 3. OSVČ a živnosti")
            st.write("""
            **OSVČ** znamená osoba samostatně výdělečně činná. Jde o podnikání fyzické osoby — člověka, který podniká vlastním jménem a nese plnou odpovědnost.
            """)
            st.markdown("""
            <div class='box-red'>
                <strong>Hlavní riziko OSVČ:</strong> OSVČ ručí za závazky z podnikání celým svým osobním majetkem.
            </div>
            """, unsafe_allow_html=True)

        # Kalkulačka OSVČ
        with st.container(border=True):
            st.markdown("### 🧮 Kalkulačka hodinové sazby OSVČ")
            col_calc1, col_calc2 = st.columns(2)
            with col_calc1:
                target_pay = st.number_input("Požadovaný čistý příjem měsíčně (Kč):", value=30000, step=1000)
                fixed_costs = st.number_input("Měsíční náklady na podnikání (Kč):", value=5000, step=500)
            with col_calc2:
                billable_hours = st.number_input("Počet fakturovatelných hodin měsíčně:", value=100, step=10)
                tax_estimate = 8311

            total_needed = target_pay + fixed_costs + tax_estimate
            hourly_rate = total_needed / billable_hours if billable_hours > 0 else 0

            st.markdown(f"""
            <div class='box-green'>
                Minimální hodinová sazba činí: <span style='font-size: 1.2rem; font-weight: 700;'>{hourly_rate:.0f} Kč / hod.</span>
            </div>
            """, unsafe_allow_html=True)

    with tab_korporace:
        with st.container(border=True):
            st.markdown("## 4. Obchodní korporace")
            st.write("""
            Obchodní korporace jsou právnické osoby založené podle zákona o obchodních korporacích (ZOK). 
            Vytvářejí samostatný subjekt — firmu, která má vlastní název, sídlo, majetek, orgány a odpovědnost.
            """)
            st.markdown("""
            <div class='box-blue'>
                <strong>Právní forma určuje:</strong> Kdo podnik vlastní, kdo za něj jedná, jak se ručí za dluhy, jak se vkládá kapitál a rozděluje zisk.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 4.2 Rozdělení obchodních korporací")
            
            c_korp1, c_korp2, c_korp3 = st.columns(3)
            with c_korp1:
                st.markdown("""
                <div class='box-gray'>
                    <strong>Osobní společnosti</strong><br>
                    • v.o.s., k.s.<br>
                    • Důležitá osobní účast a ručení majetkem společníků.
                </div>
                """, unsafe_allow_html=True)
            with c_korp2:
                st.markdown("""
                <div class='box-gray'>
                    <strong>Kapitálové společnosti</strong><br>
                    • s.r.o., a.s.<br>
                    • Důležitý je vklad kapitálu, majetek firmy oddělen od vlastníků.
                </div>
                """, unsafe_allow_html=True)
            with c_korp3:
                st.markdown("""
                <div class='box-gray'>
                    <strong>Družstva</strong><br>
                    • Družstvo, SCE<br>
                    • Důležité je členství, spolupráce a společný prospěch.
                </div>
                """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 4.6–4.7 Přehled hlavních forem")
            
            st.markdown("#### Společnost s ručením omezeným (s.r.o.)")
            st.write("Nejčastější firemní forma. Zakládá ji 1 a více osob, min. vklad od 1 Kč (prakticky však vyšší). Ručení společníků je omezené nesplaceným vkladem.")
            
            st.markdown("#### Akciová společnost (a.s.)")
            st.write("Vhodná pro velké projekty a investory. Kapitál je rozdělen na akcie. Min. základní kapitál činí 2 000 000 Kč. Akcionáři osobně neručí.")

            st.markdown("#### Veřejná obchodní společnost (v.o.s.) & Komanditní společnost (k.s.)")
            st.write("U v.o.s. všichni společníci ručí celým majetkem. U k.s. komplementář ručí celým majetkem a komanditista do výše nesplaceného vkladu.")

        with st.container(border=True):
            st.markdown("### 4.8 Péče řádného hospodáře")
            st.markdown("""
            <div class='box-red'>
                <strong>Pozor:</strong> Jednatelé a členové orgánů musí jednat informovaně, pečlivě a loajálně. Omezené ručení firmy neznamená beztrestnost vedení při porušení povinností!
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 4.12 Zrušení, likvidace a zánik firmy")
            st.markdown("""
            1. **Zrušení:** Rozhodnutí společníků nebo soudu, že firma končí.
            2. **Likvidace:** Vypořádání majetku, dluhů a pohledávek.
            3. **Zánik:** Konec právní existence firmy výmazem z Obchodního rejstříku.
            """)

        with st.container(border=True):
            st.markdown("### 4.16 Další a přeshraniční formy (EU)")
            st.write("• **Pobočka / Odštěpný závod:** Organizační složka bez vlastní právní subjektivity.<br>• **Evropská společnost (SE):** Nadnárodní akciová společnost v EU.<br>• **Tiché společenství:** Smluvní investice bez zápisu do rejstříku.", unsafe_allow_html=True)

    with tab_ukoly:
        with st.container(border=True):
            st.markdown("## 📊 Interaktivní test: OSVČ, nebo s.r.o.?")
            st.write("Odpovězte na 9 otázek a zjistěte, která právní forma je vhodnější pro váš projekt:")

            q1_opt = st.radio("1. Plánuješ podnikat sám/sama, nebo v týmu?", ["Podnikám sám/sama (Spíš OSVČ)", "Podnikáme v týmu (Spíš s.r.o.)"], key="t_q1")
            q2_opt = st.radio("2. Jde hlavně o osobní práci, nebo projekt s růstem?", ["Nabízím vlastní práci (Spíš OSVČ)", "Projekt má růst jako firma (Spíš s.r.o.)"], key="t_q2")
            q3_opt = st.radio("3. Hrozí projektem větší finanční závazky?", ["Nízké náklady (Spíš OSVČ)", "Větší nákupy, úvěry, sklad (Spíš s.r.o.)"], key="t_q3")
            q4_opt = st.radio("4. Chceš chránit osobní majetek před rizikem dluhů?", ["Nevadí mi osobní ručení (Spíš OSVČ)", "Chci oddělit osobní majetek (Spíš s.r.o.)"], key="t_q4")
            q5_opt = st.radio("5. Budeš potřebovat investora nebo bankovní úvěr?", ["Nepotřebuji investora (Spíš OSVČ)", "Chci jednat s investory (Spíš s.r.o.)"], key="t_q5")

            score_osvc = sum([1 for x in [q1_opt, q2_opt, q3_opt, q4_opt, q5_opt] if "OSVČ" in x])
            score_sro = 5 - score_osvc

            if st.button("Vyhodnotit doporučení právní formy"):
                if score_sro > score_osvc:
                    st.markdown(f"""
                    <div class='box-blue'>
                        <strong>Výsledek testu: Spíš s.r.o. ({score_sro} z 5 bodů)</strong><br>
                        Váš projekt vykazuje znaky týmové práce, vyššího rizika nebo potřeby oddělení majetku.
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class='box-green'>
                        <strong>Výsledek testu: Spíš OSVČ ({score_osvc} z 5 bodů)</strong><br>
                        Pro váš začátek bude pravděpodobně jednodušší a rychlejší začít jako OSVČ na živnost.
                    </div>
                    """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("## 🟣 AI Mentoring Prompty pro Sekci 4")
            st.code("Porovnej pro můj projekt OSVČ, s.r.o. a a.s. podle rizika, administrativy, zdanění a růstu.", language="markdown")
            st.code("Porovnej pro můj projekt OSVČ, s.r.o., v.o.s., k.s., a.s. a družstvo. U každé formy napiš výhodu, riziko a zákonný znak.", language="markdown")

    with tab_slovnicek:
        with st.container(border=True):
            st.markdown("## 📖 Slovníček pojmů (vč. Obchodních korporací)")
            st.markdown("""
            • **Obchodní korporace:** Souhrnný pojem pro obchodní společnosti a družstva.<br>
            • **Obchodní rejstřík:** Veřejný seznam na Justice.cz k ověřování údajů o firmách.<br>
            • **Společenská smlouva / Zakladatelská listina:** Základní dokument při zakládání firmy.<br>
            • **Péče řádného hospodáře:** Povinnost jednatelů jednat informovaně, pečlivě a v zájmu firmy.<br>
            • **Likvidace:** Proces vypořádání majetku a dluhů před zánikem korporace.<br>
            • **Dividenda:** Podíl na zisku vyplácený akcionářům a.s.
            """, unsafe_allow_html=True)

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
            st.markdown("• Test právní formy: *Doporučeno s.r.o.*")
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
