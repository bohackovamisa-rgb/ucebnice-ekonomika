import streamlit as st

def render():
    # 📌 HLAVIČKA KAPITOLY
    st.markdown("<span class='hero-badge'>Kapitola 5</span>", unsafe_allow_html=True)
    st.title("5. Stát, daně a globální souvislosti")
    st.markdown("<p style='font-size: 1rem; color: #64748b; margin-bottom: 1.5rem;'>Stát není jen úřad, formulář nebo položka na výplatní pásce. Je to systém, který vybírá daně, financuje veřejné služby, nastavuje pravidla trhu a reaguje na problémy, které jednotlivci ani firmy sami nevyřeší — od infrastruktury přes digitální stát až po regulaci Big Tech, globální obchod a klimatickou odpovědnost.</p>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown("""
        <div class='box-blue'>
            <strong>🧠 Pointa kapitoly:</strong> Ekonomika státu není abstraktní tabulka. Promítá se do toho, kolik zaplatíš z brigády, proč je v ceně mobilu DPH, jak stát financuje školy a silnice, proč řeší daňové úniky, jak funguje eGovernment a proč levné zboží z druhého konce světa může mít skryté ekologické i sociální náklady.
        </div>
        """, unsafe_allow_html=True)

    # 📌 PŘEHLED A NAVIGACE KAPITOLOU
    with st.expander("🧭 Cíle kapitoly a logická cesta (Rozbalit)", expanded=False):
        c_nav1, c_nav2 = st.columns(2)
        with c_nav1:
            st.markdown("""
            **🎯 Co máš po kapitole umět?**
            * **Vysvětlit** funkce státu v ekonomice a důvody státních zásahů.
            * **Rozlišit** veřejné statky, komerční služby a tržní selhání.
            * **Popsat** základní princip státního rozpočtu, deficitu a veřejného dluhu.
            * **Rozlišit** přímé a nepřímé daně na běžných příkladech.
            * **Vysvětlit**, proč se daně týkají brigád, podnikání, tvorby obsahu (YouTube, TikTok), investic i kryptoměn.
            * **Popsat** globalizaci, mezinárodní obchod a dodavatelské řetězce (vč. EU a jednotného trhu).
            * **Posoudit** dopady levného zboží (fast fashion, e-commerce) na lidi i životní prostředí.
            * **Porozumět** pojmům jako Green Deal, ESG a odpovědnost firem.
            """)
            st.markdown("""
            <div style="font-size: 0.85rem; color: #64748b; margin-top: 10px;">
                <i>📘 <b>Vazba na RVP:</b> Kapitola rozvíjí ekonomické, občanské a digitální kompetence v oblastech funkce státu v ekonomice, hospodářská politika, daňová soustava, státní rozpočet, veřejné finance, globalizace, EU a udržitelný rozvoj.</i>
            </div>
            """, unsafe_allow_html=True)

        with c_nav2:
            st.markdown("""
            **🧭 Logická cesta kapitolou:**
            1. 🏛️ **Stát jako hospodář:** Proč stát v ekonomice vůbec existuje, co jsou veřejné statky a tržní selhání.
            2. 📊 **Daně a státní rozpočet:** Odkud stát bere peníze, za co je utrácí, proč vzniká deficit a proč daně nejsou jen „trest za výdělek“.
            3. 💸 **Moje daně v praxi:** Propojení s reálným životem (brigády, Vinted, OnlyFans, Uber, kryptoměny, DPH).
            4. 🌍 **Globální souvislosti:** Cesta výrobků (fast fashion, čipy z Asie, Temu) a rizika závislosti na dodavatelských řetězcích.
            5. 🌱 **ESG a udržitelná ekonomika:** Uhlíková stopa, greenwashing a společenská odpovědnost firem.
            """)

    # 📌 JEDNOTNÁ NABÍDKA PODKAPITOL
    # Sdruženo do 6 hlavních bloků podle tvé osnovy z obrázků pro přehlednost UI
    section_options_5 = [
        "1. Stát jako „hospodář“ — proč ho vůbec máme?",
        "2. Daně, státní rozpočet a ekonomická realita",
        "3. Moje daně v praxi",
        "4. Globální souvislosti a svět bez hranic",
        "5. ESG a udržitelná ekonomika",
        "6. Aktivity a případové studie na závěr"
    ]
    
    selected_section_5 = st.selectbox("📌 Přechod na podkapitolu:", section_options_5, index=0)
    st.divider()

    # =========================================================================
    # SEKCE 1: STÁT JAKO HOSPODÁŘ
    # =========================================================================
    if selected_section_5 == "1. Stát jako „hospodář“ — proč ho vůbec máme?":
        st.markdown("### 1. Stát jako „hospodář“ — proč ho vůbec máme?")
        st.info("Zde bude obsah pro podkapitoly 1.1 až 1.6 (Tržní selhání, funkce státu, magický čtyřúhelník...)")
        # Sem vložíme kód v dalším kroku...

    # =========================================================================
    # SEKCE 2: DANĚ A STÁTNÍ ROZPOČET
    # =========================================================================
    elif selected_section_5 == "2. Daně, státní rozpočet a ekonomická realita":
        st.markdown("### 2. Daně, státní rozpočet a ekonomická realita")
        st.info("Zde bude obsah pro podkapitoly 2.1 až 2.12 (Zásady zdaňování, přímé/nepřímé daně, rozpočet, dluh...)")

    # =========================================================================
    # SEKCE 3: MOJE DANĚ V PRAXI
    # =========================================================================
    elif selected_section_5 == "3. Moje daně v praxi":
        st.markdown("### 3. Moje daně v praxi")
        st.info("Zde bude praktický průvodce daněmi pro mladé (brigády, online výdělky, krypto...)")

    # =========================================================================
    # SEKCE 4: GLOBÁLNÍ SOUVISLOSTI
    # =========================================================================
    elif selected_section_5 == "4. Globální souvislosti a svět bez hranic":
        st.markdown("### 4. Globální souvislosti a svět bez hranic")
        st.info("Zde bude obsah pro 4.1 až 4.7 (Globalizace, EU, dodavatelské řetězce...)")

    # =========================================================================
    # SEKCE 5: ESG A UDRŽITELNOST
    # =========================================================================
    elif selected_section_5 == "5. ESG a udržitelná ekonomika":
        st.markdown("### 5. ESG a udržitelná ekonomika")
        st.info("Zde bude obsah pro 5.1 až 5.6 (Greenwashing, cirkulární ekonomika, odpovědný spotřebitel...)")

    # =========================================================================
    # SEKCE 6: AKTIVITY A PŘÍPADOVÉ STUDIE
    # =========================================================================
    elif selected_section_5 == "6. Aktivity a případové studie na závěr":
        st.markdown("### 6. Aktivity a případové studie na závěr")
        st.info("Zde budou interaktivní případové studie (Levné tričko, Student vydělává online, Obec rozhoduje o rozpočtu...)")
# =========================================================================
    # SEKCE 1: STÁT JAKO HOSPODÁŘ
    # =========================================================================
    if selected_section_5 == "1. Stát jako „hospodář“ — proč ho vůbec máme?":
        st.markdown("### 1. Stát jako „hospodář“ — proč ho vůbec máme?")
        
        st.markdown("""
        <div class='box-blue'>
            🏛️ <b>Představ si stát jako „předplatné na fungující společnost“.</b><br>
            Netflix si platíš přímo ze své karty, protože chceš sledovat seriály. Ale dálnice, veřejné osvětlení, policii, soudy, školy nebo nemocnice nejde rozumně platit „po jednotlivých kliknutích“ jako na Patreonu. Proto existují daně, státní rozpočty a pravidla, kterým říkáme hospodářská politika.
        </div>
        """, unsafe_allow_html=True)

        st.divider()
        st.markdown("#### 1.1 Proč stát zasahuje do trhu: Tržní selhání")
        st.write("Trh je skvělý vynález. Umí propojit lidi, motivuje firmy ke zlepšování a tlačí ceny dolů. Jenže trh není kouzelný algoritmus, který automaticky vyřeší všechno spravedlivě a dlouhodobě udržitelně. Čas od času dojde k **tržnímu selhání** – situaci, kdy trh sám o sobě vytváří pro společnost problém. A právě tehdy nastupuje stát.")

        tab_selhani1, tab_selhani2, tab_selhani3 = st.tabs(["🛣️ Veřejné statky", "🏭 Externality", "👑 Monopol"])

        with tab_selhani1:
            st.markdown("##### Veřejné statky (Proč neplatíme silnice přes Kickstarter?)")
            st.write("Existují věci, u kterých je obrovský problém vybírat vstupné a kde vaše spotřeba neomezuje nikoho dalšího. Tomu se říká **veřejný statek**.")
            st.markdown("""
            * **Nevylučitelnost:** Nemůžete rozumně zakázat někomu, aby se v noci díval na světlo z pouliční lampy, i když na ni nepřispěl.
            * **Problém černého pasažéra:** Kdyby se policie nebo dálnice platily čistě dobrovolně formou sbírky, spousta lidí by je využívala zdarma a systém by zkrachoval. Proto tyto věci platíme povinně z daní.
            """)

        with tab_selhani2:
            st.markdown("##### Externality (Skrytá cena za levné tričko)")
            st.write("**Externalita** je vedlejší efekt výroby nebo obchodu, který „odnese“ někdo třetí (kdo se toho obchodu vůbec neúčastnil).")
            st.markdown("""
            * 🔴 **Negativní externalita:** Koupíte si velmi levné tričko (tzv. Fast fashion). Vy ušetříte a firma vydělá. Ale toxický odpad z barvení látky zničí řeku lidem na druhém konci světa, nebo kamiony způsobí zácpy a hluk ve vašem městě. Stát proti tomu bojuje např. ekologickými daněmi nebo regulací dopravy.
            * 🟢 **Pozitivní externalita:** Vzdělaný člověk (školy zdarma). Nejenže on sám má vyšší plat, ale vymyslí třeba lék, ze kterého těží celá společnost. Proto stát dotuje školství.
            """)

        with tab_selhani3:
            st.markdown("##### Monopoly a Big Tech (Proč máme všichni USB-C?)")
            st.write("**Monopol** vzniká, když jedna firma ovládne trh natolik, že si může diktovat ceny, diktovat absurdní podmínky a likvidovat slabší konkurenci. Stát a Evropská unie proto tvoří antimonopolní úřady.")
            st.info("💡 **Příklad z praxe:** Regulace gigantů jako Apple nebo Google ze strany EU. Nařízení sjednotit nabíječky na formát USB-C nebo právo uživatele vybrat si svobodně jiný internetový prohlížeč než ten tovární. Bez státního donucení by trh tuto změnu sám neudělal.")

        st.divider()
        st.markdown("#### 1.2 Co přesně stát v ekonomice dělá: 4 Funkce státu")
        st.write("Stát neřídí každou cenu rohlíku v obchodě. Zajišťuje pouze rámec, ve kterém můžeme my všichni svobodně hrát hru jménem kapitalismus.")

        col_fce1, col_fce2 = st.columns(2)
        with col_fce1:
            st.markdown("""
            <div style="background-color: #f8fafc; padding: 15px; border-left: 5px solid #3b82f6; margin-bottom: 10px;">
                <h5 style="margin-top: 0; color: #1e40af;">⚖️ 1. Právní a institucionální (Pravidla hry)</h5>
                Zajišťuje ochranu soukromého vlastnictví, soudy, policii a Českou obchodní inspekci. Zaručuje, že když ti e-shop nedodá boty, můžeš se bránit a nevládne právo silnějšího.
            </div>
            <div style="background-color: #f8fafc; padding: 15px; border-left: 5px solid #10b981;">
                <h5 style="margin-top: 0; color: #065f46;">🏗️ 2. Alokační</h5>
                Směřuje naše společné peníze (z daní) do míst, kde by je komerční trh sám nezaplatil (stavba mostů, nemocnic, hasiči, provoz národních parků).
            </div>
            """, unsafe_allow_html=True)

        with col_fce2:
            st.markdown("""
            <div style="background-color: #f8fafc; padding: 15px; border-left: 5px solid #8b5cf6; margin-bottom: 10px;">
                <h5 style="margin-top: 0; color: #4c1d95;">🤝 3. Redistribuční (Přeberozdělovací)</h5>
                Bere část peněz bohatším (daně) a dává je potřebným (důchody, invalidé, podpora v nezaměstnanosti, plošné obědy ve školách), aby se společnost nerozpadla.
            </div>
            <div style="background-color: #f8fafc; padding: 15px; border-left: 5px solid #f59e0b;">
                <h5 style="margin-top: 0; color: #92400e;">📉 4. Stabilizační</h5>
                Snaží se mírnit extrémní výkyvy krize. Během pandemie dotuje zavřené provozy (Kurzarbeit) a během cenových krizí například zastropuje ceny energií.
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br><div class='box-yellow'>🗣️ <b>Debatní aréna: Mají miliardáři platit vyšší daně?</b></div>", unsafe_allow_html=True)
        st.write("Jedno z největších ekonomických dilemat redistribuční funkce. Jaký je tvůj postoj?")
        
        with st.form("debata_dane_form"):
            nazor_dane = st.radio("Měl by stát výrazně zvýšit daně velmi bohatým lidem, aby mohl financovat bezplatné služby pro chudší?", [
                "Ano, je to morální a zajistí to sociální mír a lepší služby pro všechny (tzv. solidarita).",
                "Ne, bohatí své peníze vydělali a vysoké zdanění by je motivovalo odejít s podnikáním do zahraničí, čímž by stát ztratil pracovní místa.",
                "Hledal bych kompromis. Zdanit nadnárodní korporace, ale běžným podnikatelům daně nezvyšovat."
            ])
            submit_dane = st.form_submit_button("Odeslat můj názor do diskuze")
            
            if submit_dane:
                st.success("Tento problém nemá 'správnou' matematickou odpověď. Je to politické a filozofické rozhodnutí, které formuje podobu státu ve kterém chceme žít.")

        st.divider()
        st.markdown("#### 1.3 Makroekonomické ukazatele: Krevní tlak státu")
        st.write("Nejde o nudná čísla do tabulek. Když se změní inflace nebo klesne HDP, projeví se to okamžitě v tom, kolik stojí chleba, jestli banky zlevní hypotéky, a jak těžké bude najít v létě brigádu.")

        st.markdown("##### 🩺 4 klíčové hodnoty (Magický čtyřúhelník)")
        st.markdown("""
        1. 📈 **HDP (Hrubý domácí produkt):** Roste nám celkové bohatství vyprodukované v ČR za rok? (Pokud HDP klesá dva kvartály po sobě, jsme v recesi a firmy propouští).
        2. 🛒 **Inflace:** Jak rychle zdražují ceny v obchodech? (Cílem státu, přesněji České národní banky, je držet ji na zdravých 2 % ročně).
        3. 🧑‍🔧 **Míra nezaměstnanosti:** Kolik procent práceschopných lidí chce pracovat, ale nedaří se jim najít místo? (ČR má dlouhodobě jednu z nejnižších v EU).
        4. 🌍 **Platební bilance:** Vyvážíme z Česka do světa více zboží a peněz, než kolik dovážíme ze zahraničí?
        """)

        st.markdown("<div class='box-purple'>💻 <b>Interaktivní detektivka s reálnými daty z ČSÚ</b></div>", unsafe_allow_html=True)
        st.write("Nehádej. Otevři si skutečná, včerejší data z Českého statistického úřadu a staň se na chvíli ekonomickým analytikem.")
        
        st.markdown("""
        **Zdroje pro vyřešení úkolu:**
        * [ČSÚ: Hlavní makroekonomické ukazatele](https://www.czso.cz/csu/czso/hlavni-makroekonomicke-ukazatele)
        * [ČSÚ: Aktuální inflace](https://www.czso.cz/csu/czso/mira_inflace)
        """)

        with st.form("detektiv_csu_form"):
            st.write("**Tvůj úkol:** Najdi aktuální hodnoty na webech ČSÚ výše a napiš své závěrečné hodnocení jako ekonomický komentátor zpráv:")
            analyza_text = st.text_area("Vyplň svou ekonomickou zprávu:", value="Na základě aktuálních dat ČSÚ (růst HDP: ___ %, inflace: ___ %) soudím, že se česká ekonomika nachází ve fázi (růstu / útlumu / krize). Protože...")
            
            if st.form_submit_button("Vydat zprávu do médií"):
                st.success("Tvá analýza byla přijata k otištění! Právě sis vyzkoušel práci reálného datového analytika.")
