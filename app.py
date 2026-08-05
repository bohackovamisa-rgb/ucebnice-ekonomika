import streamlit as st

# --- KONFIGURACE STRÁNKY ---
st.set_page_config(page_title="Učebnice Ekonomiky", page_icon="📖", layout="wide", initial_sidebar_state="expanded")

# --- PŘIHLAŠOVÁNÍ ---
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
            st.markdown("<h2 style='text-align: center; margin-bottom: 0;'>Soukromá učebnice</h2>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center; color: #64748b;'>Zadejte přístupové heslo pro odemknutí kurzu.</p>", unsafe_allow_html=True)
            password = st.text_input("Heslo:", type="password", label_visibility="collapsed")
            if st.button("Vstoupit do učebnice", use_container_width=True):
                if password == app_pwd:
                    st.session_state["password_correct"] = True
                    st.rerun()
                else:
                    st.error("Nesprávné heslo")
    return False

if not check_password():
    st.stop()

# --- CSS STYLOVÁNÍ ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800&display=swap');
    html, body, [class*="css"] { font-family: 'Montserrat', sans-serif !important; }
    .stApp { background-color: #f8fafc; color: #0f172a; }
    div[data-testid="stVerticalBlockBorderWrapper"] { background-color: #ffffff !important; border-radius: 12px !important; border: 1px solid #e2e8f0 !important; box-shadow: 0 1px 3px rgba(15,23,42,0.03); padding: 1.5rem !important; margin-bottom: 1.25rem !important; }
    .box-blue { background-color: #f0f9ff; border-left: 4px solid #0284c7; padding: 1rem; border-radius: 0 8px 8px 0; margin: 1rem 0; }
    .box-yellow { background-color: #fefce8; border-left: 4px solid #eab308; padding: 1rem; border-radius: 0 8px 8px 0; margin: 1rem 0; }
    .box-red { background-color: #fef2f2; border-left: 4px solid #ef4444; padding: 1rem; border-radius: 0 8px 8px 0; margin: 1rem 0; }
    .box-green { background-color: #f0fdf4; border-left: 4px solid #22c55e; padding: 1rem; border-radius: 0 8px 8px 0; margin: 1rem 0; }
    .box-purple { background-color: #faf5ff; border-left: 4px solid #a855f7; padding: 1rem; border-radius: 0 8px 8px 0; margin: 1rem 0; }
    .box-gray { background-color: #f8fafc; border-left: 4px solid #64748b; padding: 1rem; border-radius: 0 8px 8px 0; margin: 1rem 0; }
    .hero-badge { background: #e0e7ff; color: #4338ca; font-size: 0.75rem; font-weight: 700; padding: 0.3rem 0.8rem; border-radius: 20px; text-transform: uppercase; margin-bottom: 0.8rem; display: inline-block; }
    </style>
""", unsafe_allow_html=True)

# --- NAVIGACE A BOČNÍ PANEL ---
if "current_view" not in st.session_state:
    st.session_state["current_view"] = "Uvod"

with st.sidebar:
    st.markdown("<h2>Učebnice Ekonomiky</h2>", unsafe_allow_html=True)
    st.divider()

    if st.button("Úvodní stránka", use_container_width=True, type="primary" if st.session_state["current_view"] == "Uvod" else "secondary"):
        st.session_state["current_view"] = "Uvod"
        st.rerun()

    st.markdown("<p style='font-size:0.8rem; color:#64748b; font-weight:bold; margin-top:1rem;'>KAPITOLY KURZU</p>", unsafe_allow_html=True)
    chapters = ["Kapitola 1", "Kapitola 2", "Kapitola 3", "Kapitola 4", "Kapitola 5", "Kapitola 6"]
    for ch in chapters:
        if st.button(ch, key=f"nav_{ch}", use_container_width=True, type="primary" if st.session_state["current_view"] == ch else "secondary"):
            st.session_state["current_view"] = ch
            st.rerun()

    st.divider()
    if st.button("Odhlásit se", use_container_width=True):
        st.session_state["password_correct"] = False
        st.rerun()

# --- HLAVNÍ OBSAH ---
view = st.session_state["current_view"]

if view == "Uvod":
    st.markdown("<span class='hero-badge'>Digitální Učebnice</span>", unsafe_allow_html=True)
    st.title("Ekonomika, která dává smysl")
    with st.container(border=True):
        st.write("Vítejte v interaktivní učebnici ekonomiky. Vyberte kapitolu v levém menu.")

elif view == "Kapitola 1":
    st.title("Kapitola 1: Podnikavost a startupy")
    st.info("Obsah Kapitoly 1 je zde zkrácen pro přehlednost. Nyní se soustředíme na Kapitolu 2.")

elif view == "Kapitola 2":
    st.markdown("<span class='hero-badge'>Kapitola 2</span>", unsafe_allow_html=True)
    st.title("Finance v běžném životě: peníze, rozhodování a odpovědnost")
    st.write("Tahle kapitola propojuje osobní finance, bankovní systém, finanční trh a podnikové finance[cite: 2]. Nejde jen o počítání peněz, ale o odpovědné rozhodování v běžném životě[cite: 2].")
    
    with st.container(border=True):
        st.markdown("""
        <div class='box-purple'>
            <strong>🎯 Cíle kapitoly: Co máš po kapitole umět?</strong><br>
            • vysvětlit funkce peněz a princip bankovního systému[cite: 2]<br>
            • sestavit jednoduchý osobní nebo rodinný rozpočet[cite: 2]<br>
            • rozlišit spoření, investování a spekulaci[cite: 2]<br>
            • vysvětlit cenu úvěru včetně RPSN[cite: 2]<br>
            • propojit osobní finance s finančním řízením podniku[cite: 2]
        </div>
        """, unsafe_allow_html=True)

    sekce_k2 = [
        "2.1 Bankovní systém a peníze",
        "2.2 Osobní finance a rozpočet",
        "2.3 Finanční trh a rizika",
        "2.4 Úvěry a pojištění",
        "2.5 Finanční řízení podniku",
        "2.6 Slovník a aktivity"
    ]
    vybrana_sekce_k2 = st.selectbox("📌 Vyberte podkapitolu:", sekce_k2)
    st.divider()

    # --- 2.1 BANKOVNÍ SYSTÉM ---
    if vybrana_sekce_k2 == "2.1 Bankovní systém a peníze":
        st.markdown("## 1. Bankovní systém a peníze v 21. století")
        with st.container(border=True):
            st.write("21. století není jen éra umělé inteligence a sociálních sítí. Je to především éra totální transformace toho, jak vnímáme hodnotu[cite: 2].")
            st.markdown("<div class='box-blue'><strong>Základní myšlenka:</strong> Peníze nejsou jen „věc“. Jsou to hlavně důvěryhodný záznam hodnoty, kterému lidé, firmy a stát věří[cite: 2].</div>", unsafe_allow_html=True)
            
            st.markdown("### Vývoj peněz[cite: 2]")
            st.markdown("""
            * **Naturální směna:** Zboží za zboží.
            * **Komoditní peníze:** Kovy, sůl, obilí.
            * **Mince a bankovky:** Hotovostní systém garantovaný státem.
            * **Bezhotovostní a digitální peníze:** Zůstatek na účtu, data v systémech.
            """)

            with st.expander("💡 Přečti si více o Zlatém standardu a Nixonově šoku"):
                st.write("**Zlatý standard:** Stát sliboval, že měna je krytá zlatem[cite: 2]. **Nixonův šok:** V roce 1971 prezident USA zrušil vazbu dolaru na zlato[cite: 2]. Svět se přesunul k „fiat penězům“ – jejich hodnota stojí na důvěře ve stát a centrální banku[cite: 2].")

        with st.container(border=True):
            st.markdown("### ČNB a komerční banky[cite: 2]")
            st.markdown("""
            <div class='box-gray'>
                <strong>Česká národní banka (ČNB):</strong> Centrální banka státu. Její hlavní cíl je cenová stabilita (hlídá inflaci) a dohled nad finančním trhem[cite: 2].<br><br>
                <strong>Komerční banky:</strong> Banky pro lidi a firmy. Přijímají vklady (pasivní operace), poskytují úvěry (aktivní operace) a zajišťují platby (neutrální operace)[cite: 2].
            </div>
            """, unsafe_allow_html=True)

            with st.expander("🎮 Simulace: Jsi bankovní rada ČNB!"):
                st.write("**Situace:** Inflace je vysoká, ceny v obchodech letí nahoru. Co uděláte s úrokovou sazbou?[cite: 2]")
                cnb_action = st.radio("Vaše rozhodnutí:", ["Vyber...", "Zvýšíme sazby", "Snížíme sazby"])
                if st.button("Potvrdit rozhodnutí"):
                    if cnb_action == "Zvýšíme sazby":
                        st.success("Správně! Úvěry zdraží, lidé budou méně utrácet a více spořit. Tlak na růst cen se sníží[cite: 2].")
                    elif cnb_action == "Snížíme sazby":
                        st.error("Špatně. Pokud zlevníte úvěry, do oběhu se dostane víc peněz a inflace ještě víc stoupne[cite: 2].")

        with st.container(border=True):
            st.markdown("### Platební styk a CERTIS[cite: 2]")
            st.write("Platební styk je infrastruktura důvěry[cite: 2]. Pokud posíláš peníze v ČR mezi DVĚMA RŮZNÝMI bankami, platba se vypořádá přes mezibankovní systém **CERTIS**, který provozuje ČNB[cite: 2].")

    # --- 2.2 OSOBNÍ FINANCE ---
    elif vybrana_sekce_k2 == "2.2 Osobní finance a rozpočet":
        st.markdown("## 2. Osobní finance a „Algoritmy bohatství“")
        with st.container(border=True):
            st.write("Finanční gramotnost znamená umět zacházet s penězi i s digitálním prostředím. Aplikace, slevy, předplatná a odložené platby nás vedou k rychlému utrácení[cite: 2].")
            st.markdown("### Rozpočet: Mapa peněz[cite: 2]")
            st.markdown("""
            * **Fixní výdaj:** Nájem, paušál. (Opravdu ho potřebuji každý měsíc?)[cite: 2]
            * **Proměnlivý výdaj:** Jídlo, zábava. (Dá se upravit?)[cite: 2]
            * **Skrytý výdaj:** Automatická předplatná. (Vím, kolik mě to stojí ročně?)[cite: 2]
            """)
            st.markdown("<div class='box-green'><strong>Pravidlo 50-30-20:</strong> 50 % na potřeby, 30 % na přání, 20 % na rezervu nebo dluhy[cite: 2].</div>", unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### Algoritmy bohatství[cite: 2]")
            st.markdown("<div class='box-blue'><strong>Zaplať nejdřív sobě:</strong> Nečekej, co zbyde na konci měsíce. Hned po výplatě odlož peníze na rezervu[cite: 2].</div>", unsafe_allow_html=True)
            st.markdown("### Matematika peněz[cite: 2]")
            st.write("**Složené úročení:** Úročí se nejen původní částka, ale i již připsané úroky. Peníze vydělávají další peníze[cite: 2].")

        with st.container(border=True):
            st.markdown("### Psychologie utrácení a Kalkulačka času[cite: 2]")
            st.write("Cena věci se dá přepočítat na čas, který musí člověk pracovat, aby si ji mohl dovolit[cite: 2].")
            c_time1, c_time2, c_time3 = st.columns(3)
            with c_time1: item_price = st.number_input("Cena věci (Kč):", value=2400, step=100)
            with c_time2: hourly_wage = st.number_input("Čistá hodinová mzda (Kč):", value=150, step=10)
            with c_time3:
                if hourly_wage > 0:
                    st.info(f"**Musíš pracovat:**\n### {item_price / hourly_wage:.1f} hodin[cite: 2]")

    # --- 2.3 FINANČNÍ TRH ---
    elif vybrana_sekce_k2 == "2.3 Finanční trh a rizika":
        st.markdown("## 3. Finanční trh a analýza rizik")
        with st.container(border=True):
            st.markdown("### Investiční trojúhelník[cite: 2]")
            st.markdown("""
            <div class='box-purple'>
                <strong>1. Výnos:</strong> To, co získáš navíc[cite: 2].<br>
                <strong>2. Riziko:</strong> Možnost, že ztratíš hodnotu[cite: 2].<br>
                <strong>3. Likvidita:</strong> Jak snadno lze aktivum proměnit zpět na peníze[cite: 2].
            </div>
            """, unsafe_allow_html=True)
            st.warning("Pravidlo: Vyšší možný výnos obvykle znamená vyšší riziko[cite: 2].")

        with st.container(border=True):
            st.markdown("### Základní cenné papíry[cite: 2]")
            st.markdown("""
            * **Akcie:** Podíl na akciové společnosti. Koupí akcie se stáváš spoluvlastníkem[cite: 2].
            * **Dluhopis:** Půjčka firmě nebo státu. Stáváš se věřitelem a očekáváš úrok[cite: 2].
            * **Podílový fond / ETF:** „Košík“ s více investicemi. Slouží k rozložení rizika (diverzifikaci)[cite: 2].
            """)

        with st.container(border=True):
            st.markdown("### Kryptoměny a Blockchain[cite: 2]")
            st.write("Kryptoměny fungují na technologii blockchain (sdílený digitální záznam transakcí)[cite: 2].")
            st.markdown("<div class='box-red'><strong>Rizika:</strong> Vysoká volatilita (cena prudce kolísá), ztráta přístupu (soukromého klíče), podvody a hacky[cite: 2].</div>", unsafe_allow_html=True)

    else:
        st.info("Zvolená sekce se připravuje k doplnění.")

else:
    st.info("Tato sekce se teprve připravuje.")
