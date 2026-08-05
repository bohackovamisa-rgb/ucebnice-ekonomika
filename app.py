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
    p, li { font-family: 'Montserrat', sans-serif !important; color: #334155; font-size: 0.94rem; line-height: 1.7; font-weight: 400; }
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
    .lc-title { font-size: 0.78rem; font-weight: 700; color: #4f46e5; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.3rem; }
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
    section_options = ["1. Podnikatel a základní pojmy", "2. Slovníček základních pojmů", "3. OSVČ a živnosti", "4. Obchodní korporace", "5. Startup: nápad, který hledá byznys", "6. Podnikatelský záměr", "7. Lean Canvas", "8. CSR, etika a odpovědné podnikání", "9. Rizika podnikání", "10. Švarcsystém", "11. Ověřování informací a užitečné zdroje", "12. Ukončení podnikání", "13. Logická mapa podnikání", "14. Reflexe a sebehodnocení", "15. Integrované opakování"]
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

    elif selected_section == "2. Slovníček základních pojmů":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2</div><h2>2. Slovníček základních pojmů</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("**Podnikatel:** Osoba, která samostatně vykonává výdělečnou činnost na vlastní účet a odpovědnost...")
            st.write("**Právnická osoba:** Organizovaný subjekt, který má právní osobnost (např. s.r.o.).")

    elif selected_section == "3. OSVČ a živnosti":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 3</div><h2>3. OSVČ a živnosti</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("**OSVČ** znamená osoba samostatně výdělečně činná. Jde o podnikání fyzické osoby.")
            st.markdown("#### Mini simulace OSVČ")
            profit_calc = 28000 - 6000
            st.markdown(f"**Orientační zisk:** **{profit_calc:,} Kč**")
            st.slider("Kolik % z tržby si odložit?", 10, 50, 30, 5)

    elif selected_section == "4. Obchodní korporace":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 4</div><h2>4. Obchodní korporace</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("Obchodní korporace jsou právnické osoby. Patří mezi ně obchodní společnosti (v.o.s., k.s., s.r.o., a.s.) a družstva.")
            st.radio("1️⃣ Plánuješ podnikat sám/sama, nebo v týmu?", ["Spíš OSVČ", "Spíš s.r.o."])

    elif selected_section == "5. Startup: nápad, který hledá byznys":
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
            c1, c2 = st.columns(2)
            with c1: st.text_area("Problém")
            with c2: st.text_area("Zákazníci")

    elif selected_section == "8. CSR, etika a odpovědné podnikání":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 8</div><h2>8. CSR, etika a odpovědné podnikání</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("Společenská odpovědnost firem (ESG) a etické rozhodování. Pozor na greenwashing.")

    elif selected_section == "9. Rizika podnikání":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 9</div><h2>9. Rizika podnikání</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("Riziko znamená, že výsledek může být jiný, než očekáváme. Tržní riziko, finanční riziko, právní chyba atd.")

    elif selected_section == "10. Švarcsystém":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 10</div><h2>10. Švarcsystém</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("<div class='box-red'><strong>Švarcsystém:</strong> Zastřený pracovněprávní vztah je nelegální. Člověk vystupuje jako OSVČ, ale pracuje jako zaměstnanec.</div>", unsafe_allow_html=True)
            with st.expander("💡 Zobrazit znaky rizikového nastavení spolupráce"):
                st.write("Práce pro 1 firmu, pevná pracovní doba, vybavení firmy, úkoly od šéfa.")

    elif selected_section == "11. Ověřování informací a užitečné zdroje":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 11</div><h2>11. Ověřování informací a užitečné zdroje</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("""
            | Zdroj | K čemu slouží |
            | :--- | :--- |
            | **[BusinessInfo.cz](https://www.businessinfo.cz/)** | Oficiální portál pro podnikatele. |
            | **[Portál živnostenského podnikání](https://www.rzp.cz/)** | Vyhledávání živností. |
            | **[Justice.cz](https://or.justice.cz/)** | Obchodní rejstřík firem. |
            """)

    elif selected_section == "12. Ukončení podnikání":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 12</div><h2>12. Ukončení podnikání</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            with st.expander("💡 Zrušení vs. Zánik"):
                st.write("**Zrušení:** Rozhodnutí, že firma končí (následuje likvidace).")
                st.write("**Zánik:** Firma právně přestává existovat výmazem z rejstříku.")

    elif selected_section == "13. Logická mapa podnikání":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 13</div><h2>13. Logická mapa podnikání</h2>", unsafe_allow_html=True)
        with st.container(border=True):
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

    elif selected_section == "14. Reflexe a sebehodnocení":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 14</div><h2>14. Reflexe a sebehodnocení</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.text_area("Co jsem se dnes naučil/a?")
            st.button("Uložit reflexi")

    elif selected_section == "15. Integrované opakování":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 15</div><h2>15. Integrované opakování</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("Závěrečný test a propojení celé Kapitoly 1.")


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
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.1</div><h2>Bankovní systém a peníze v 21. století</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("<div class='box-blue'><strong>Peníze jako digitální data:</strong> Peníze dnes často nevypadají jako mince nebo bankovky. V bankovním systému se změní digitální záznam: jednomu účtu se částka odečte a druhému připíše.</div>", unsafe_allow_html=True)
            st.write("Na úplném začátku lidé používali naturální směnu — vyměňovali zboží za zboží nebo službu za službu. Problém byl v tom, že směna fungovala jen tehdy, když se potkaly dvě potřeby najednou. Tomu se říká **dvojí shoda potřeb**.")
            st.markdown("<div class='box-gray'><strong>Základní rozlišení:</strong><br>• <strong>Česká národní banka (ČNB)</strong> je centrální banka ČR. Hlídá stabilitu měny.<br>• <strong>Komerční banky</strong> vedou účty, přijímají vklady a poskytují úvěry lidem a firmám.</div>", unsafe_allow_html=True)
            with st.expander("🎮 Interaktivní simulace: Jsi bankovní rada ČNB"):
                st.write("**Situace:** Inflace je vysoká. Jak zasáhneš?")
                st.radio("Rozhodněte:", ["Zvýšíte úrokové sazby", "Snížíte úrokové sazby"])

    elif selected_section_2 == "2.2 Osobní finance a rozpočet":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.2</div><h2>Osobní finance a rozpočet</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("Osobní finance nejsou jen otázka toho, kolik člověk vydělává. Jsou to každodenní rozhodnutí: za co utratím peníze, co odložím, co si půjčím, jak poznám riziko a jak se nenechám řídit reklamou.")
            st.markdown("""
            | Typ výdaje | Příklad | Otázka ke kontrole |
            | :--- | :--- | :--- |
            | **Fixní výdaj** | nájem, paušál, předplatné, splátka | Opravdu ho potřebuji každý měsíc? |
            | **Proměnlivý výdaj** | jídlo, doprava, drogerie, zábava | Dá se upravit bez zásadního poklesu kvality života? |
            | **Skrytý výdaj** | automatické předplatné, poplatky | Vím, kolik mě stojí za rok? |
            """)
            st.markdown("<div class='box-green'><strong>Pravidlo 50–30–20:</strong> 50 % na potřeby, 30 % na přání, 20 % na rezervu nebo dluhy.</div>", unsafe_allow_html=True)

    elif selected_section_2 == "2.3 Algoritmy bohatství":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.3</div><h2>Algoritmy bohatství: malé návyky, velký rozdíl</h2>", unsafe_allow_html=True)
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
            st.write("**Zaplať nejdřív sobě:** Část peněz si odlož hned po přijetí příjmu, ne až na konci měsíce.")

    elif selected_section_2 == "2.4 Matematika peněz":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.4</div><h2>Matematika peněz: čas, úrok a inflace</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("""
            * **Jednoduché úročení:** úrok se počítá stále jen z původně vložené nebo půjčené částky.
            * **Složené úročení:** úročí se nejen původní částka, ale postupně i již připsané úroky nebo výnosy. Peníze tedy mohou vydělávat další peníze.
            """)
            st.write("**Inflace** znamená růst cenové hladiny. Když ceny rostou, za stejnou částku si koupíme méně než dříve.")

    elif selected_section_2 == "2.5 Finanční rezerva":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.5</div><h2>Finanční rezerva: airbag osobních financí</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("Finanční rezerva chrání člověka před tím, aby každá nečekaná situace skončila dluhem. Běžně se doporučuje mít rezervu ve výši 3 až 6 měsíců nutných výdajů.")
            st.markdown("<div class='box-red'><strong>Častá chyba:</strong> Investovat nouzovou rezervu do rizikových aktiv.</div>", unsafe_allow_html=True)

    elif selected_section_2 == "2.6 Psychologie utrácení":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.6</div><h2>Psychologie utrácení: proč nerozhodujeme vždy racionálně</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("Lidé nejsou kalkulačky. Často se rozhodujeme podle emocí, únavy, tlaku okolí, reklamy, strachu, že něco propásneme, nebo podle toho, co nám ukáže aplikace.")
            st.markdown("""
            | Past | Jak funguje | Obrana |
            | :--- | :--- | :--- |
            | **FOMO** | Strach, že mi něco uteče. | Počkej 24 hodin před nákupem. |
            | **Sleva** | Pocit úspory, i když kupuji zbytečnost. | Ptej se: koupil/a bych to i bez slevy? |
            | **Odložená platba** | Nákup nebolí hned (BNPL). | Ber ji jako dluh, ne jako slevu. |
            """)
            st.markdown("**Vzorec Kalkulačky času:** Cena věci ÷ čistá hodinová mzda = počet hodin práce.")

    elif selected_section_2 == "2.7 Finanční trh a analýza rizik":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.7</div><h2>Finanční trh a analýza rizik</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("Finanční trh přesouvá peníze v čase. Někdo peníze dnes nepotřebuje a chce je zhodnotit. Někdo jiný peníze potřebuje dnes a je ochoten za jejich použití zaplatit úrok nebo podíl na zisku.")
            st.markdown("""
            **Trojúhelník investování:**
            1. **Výnos:** to, co získáš navíc.
            2. **Riziko:** možnost, že výsledek bude jiný (ztráta, kolísání).
            3. **Likvidita:** jak snadno lze aktivum proměnit zpět na peníze.
            """)
            st.markdown("<div class='box-yellow'><strong>Pravidlo:</strong> Vyšší možný výnos obvykle znamená vyšší riziko. Vysoký výnos, nulové riziko a okamžitá dostupnost peněz najednou jsou podezřelá kombinace.</div>", unsafe_allow_html=True)

    elif selected_section_2 == "2.8 Spoření, investování a spekulace":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.8</div><h2>Spoření, investování a spekulace</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("""
            | Pojem | Co znamená | Typický příklad | Riziko |
            | :--- | :--- | :--- | :--- |
            | **Spoření** | Odkládání peněz s důrazem na bezpečnost a dostupnost. | Spořicí účet, termínovaný vklad. | Nízké, hrozí inflace. |
            | **Investování** | Vkládání peněz do aktiv s cílem dlouhodobého zhodnocení. | Akcie, dluhopisy, ETF. | Střední až vysoké. |
            | **Spekulace** | Sázka na krátkodobý pohyb ceny. | Krátkodobé obchody, krypto. | Vysoké. |
            """)

    elif selected_section_2 == "2.9 Cenné papíry v praxi":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.9</div><h2>Cenné papíry v praxi</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("""
            * **Akcie:** Podíl na akciové společnosti. Koupí akcie firmě nepůjčuješ, kupuješ si kousek jejího vlastnictví.
            * **Dluhopis:** Cenný papír, kterým si stát nebo firma půjčuje peníze. Kupuješ dluh, jsi věřitel. Očekáváš úrok.
            * **Podílové listy / ETF:** Podíl na majetku fondu. Místo jedné akcie kupuješ „košík“ plný různých aktiv.
            """)

    elif selected_section_2 == "2.10 Kryptoměny":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.10</div><h2>Kryptoměny: technologie, peníze, spekulace i riziko</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("Kryptoměny jsou digitální aktiva v počítačové síti (Blockchain). Záznamy nejsou vedeny centrální bankou, ale sdílenou evidencí.")
            st.markdown("""
            | Typ | Co je hlavní myšlenka | Riziko |
            | :--- | :--- | :--- |
            | **Bitcoin** | Nejznámější kryptoměna, digitální vzácné aktivum. | Vysoká volatilita. |
            | **Ethereum** | Síť umožňující chytré kontrakty. | Technologická složitost. |
            | **Stablecoiny** | Tokeny navázané např. na dolar. | Ztráta navázání. |
            | **Meme coiny** | Tokeny postavené na humoru a trendu. | Extrémní spekulace a pády. |
            """)

    elif selected_section_2 == "2.11 Úvěry, pojištění a majetek":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.11</div><h2>Úvěry, pojištění a ochrana majetku</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("Úvěr není peníze zdarma. Je to závazek, který přesouvá spotřebu z budoucnosti do současnosti.")
            st.markdown("""
            * **Úrok:** Cena za půjčení peněz.
            * **RPSN:** Roční procentní sazba nákladů. Udává skutečnou cenu úvěru za rok vč. poplatků a pojištění.
            """)
            st.markdown("<div class='box-gray'><strong>BNPL (Kup teď, zaplať později):</strong> Psychologicky maskuje dluh jako pohodlnou platbu. Bolest z placení se odloží.</div>", unsafe_allow_html=True)
            st.write("**Pojištění:** Nezabrání tomu, aby se něco stalo, ale může snížit finanční škodu z událostí, které by zničily náš rozpočet.")

    elif selected_section_2 == "2.12 Finanční řízení podniku":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.12</div><h2>Finanční řízení podniku</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("""
            ### Základní finanční výkazy
            * **Rozvaha:** Fotografie firmy. Ukazuje, co firma vlastní (Aktiva) a z čeho je to financované (Pasiva).
            * **Výkaz zisku a ztráty:** Film za určité období. Výnosy minus Náklady.
            * **Cashflow (Peněžní toky):** Skutečný tok peněz. Firma může být na papíře zisková, ale zkrachovat, pokud jí chybí hotovost.
            """)
            st.write("**Zdroje financování:** Vlastní kapitál (vklady majitele, zisk) vs. Cizí zdroje (úvěr, leasing, dluhopisy).")

    elif selected_section_2 == "2.13 Finanční analýza: E-shop DropZone":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.13</div><h2>Finanční analýza: E-shop DropZone</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("Příklad e-shopu: Tržby rostou, zisk roste, ale klesá hotovost a rostou závazky. Zhoršuje se likvidita.")
            st.markdown("""
            | Ukazatel | Rok 1 | Rok 2 | Význam |
            | :--- | :--- | :--- | :--- |
            | **ROS (Rentabilita tržeb)** | 7,5 % | 10 % | Kolik % z tržeb je zisk. Ziskovost se zlepšila. |
            | **Okamžitá likvidita** | 0,32 | 0,15 | Množství hotovosti na okamžité platby kriticky kleslo. |
            | **Zadluženost** | 50 % | 57,1 % | Podíl dluhu roste. |
            """)

    elif selected_section_2 == "2.14 Závěrečné interaktivní opakování":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.14</div><h2>Závěrečné interaktivní opakování</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("Otestuj si své znalosti ze všech částí Kapitoly 2.")
            with st.expander("❓ 1. Jaký je rozdíl mezi debetní a kreditní kartou?"):
                st.write("**Odpověď:** U debetní platíš svými vlastními penězi. U kreditní platíš penězi banky (jde o úvěr), které musíš splatit.")
            with st.expander("❓ 2. Co je to RPSN a proč je důležité?"):
                st.write("**Odpověď:** Roční procentní sazba nákladů. Udává skutečnou cenu úvěru za rok, protože na rozdíl od samotného úroku obsahuje i všechny poplatky.")
            with st.expander("❓ 3. Proč by měla firma sledovat Cashflow, i když je v zisku?"):
                st.write("**Odpověď:** Zisk je jen účetní rozdíl. Zákazníci mohou platit pozdě. Pokud firma nemá reálnou hotovost (cashflow) na zaplacení účtů, může zkrachovat.")
            with st.expander("❓ 4. Který z těchto nástrojů se nejvíce hodí na uchování finanční rezervy? a) Akcie b) Spořicí účet c) Krypto"):
                st.write("**Odpověď: b) Spořicí účet.** Rezerva musí být bezpečně a rychle dostupná (likvidní). Akcie a krypto jsou příliš rizikové (kolísají).")

# ==========================================
# POKROKY A UČITEL
# ==========================================
elif view == "Pokroky":
    st.markdown("<span class='hero-badge'>Studentská zóna</span>", unsafe_allow_html=True)
    st.title("Moje pokroky")
    st.markdown("<p style='font-size: 1rem; color: #64748b; margin-bottom: 2rem;'>Přehled dokončených kapitol, uložených odpovědí a rozpracovaných projektů.</p>", unsafe_allow_html=True)
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
            st.header("Sledování práce žáků")
            col_treda, col_zak = st.columns(2)
            with col_treda: selected_class = st.selectbox("Vyberte třídu:", ["3.A", "3.B", "4.A"])
            with col_zak: selected_student = st.selectbox("Vyberte žáka:", ["Jan Novák", "Ema Dvořáková"])
            st.divider()
            st.subheader(f"Karta žáka: {selected_student}")
            st.markdown("**Vyplněné úkoly:**")
            st.text_area("Napsat žákovi poznámku:")
    with tab_metodika:
        with st.container(border=True):
            st.header("Projektové aktivity do hodin")
            st.write("Aktivita: Vyhledávání reálných firem v obchodním rejstříku Justice.cz.")
            st.write("Aktivita: Tvorba firemního rozpočtu a posouzení Cashflow.")
