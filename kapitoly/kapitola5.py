import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

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
            6. 🧩 **Aktivity a případové studie:** Praktický trénink na reálných situacích.
            """)

    # 📌 JEDNOTNÁ NABÍDKA PODKAPITOL
    section_options_5 = [
        "1. Stát jako „hospodář“ — proč ho vůbec máme?",
        "2. Daně, státní rozpočet a ekonomická realita",
        "3. Moje daně v praxi",
        "4. Globální souvislosti a svět bez hranic",
        "5. ESG a udržitelná ekonomika",
        "6. Aktivity a případové studie na závěr"
    ]
    
    st.markdown("📌 <strong>Přechod na podkapitolu:</strong>", unsafe_allow_html=True)
    selected_section_5 = st.selectbox("Přechod na podkapitolu:", section_options_5, index=0, label_visibility="collapsed")
    st.divider()

    # =========================================================================
    # SEKCE 1: STÁT JAKO HOSPODÁŘ
    # =========================================================================
    if selected_section_5.startswith("1."):
        st.markdown("### 1. Stát jako „hospodář“ — proč ho vůbec máme?")
        
        st.markdown("""
        <div class='box-blue'>
            🏛️ <b>Představ si stát jako „předplatné na fungující společnost“.</b><br>
            Netflix si platíš přímo ze své karty, protože chceš sledovat seriály. Ale dálnice, veřejné osvětlení, policii, soudy, školy nebo nemocnice nejde rozumně platit „po jednotlivých kliknutích“ jako na Patreonu. Proto existují daně, státní rozpočty a pravidla, kterým říkáme hospodářská politika.
        </div>
        """, unsafe_allow_html=True)

        st.divider()
        with st.expander("📖 Slovníček cizích pojmů v kapitole (Rychlý tahák)", expanded=False):
            st.markdown("""
            Pokud narazíš na slovo, kterému nerozumíš, tady najdeš jeho lidské vysvětlení:
            
            * **Externalita:** Vedlejší dopad výroby nebo spotřeby na někoho, kdo se obchodu vůbec neúčastnil (např. *negativní:* smog z továrny, *pozitivní:* vzdělaný člověk, který vymyslí nový lék).
            * **Monopol:** Situace na trhu, kdy existuje pouze jediný prodejce/dodavatel bez konkurence, a může si tak diktovat vysoké ceny.
            * **Fiskální politika:** Hospodářská politika státu, kterou řídí vláda pomocí státního rozpočtu (výběr daní a utrácení státních peněz).
            * **Monetární (měnová) politika:** Politika centrální banky (ČNB), která řídí množství peněz v oběhu a nastavuje úrokové sazby k tlumění inflace.
            * **Protekcionismus:** Ochranářská politika státu, který zavedením cel či kvót chrání své domácí firmy před levnou cizí konkurencí.
            * **Reshoring / Friendshoring:** Přesouvání výroby z Asie zpět do domovské země nebo do spřátelených a bezpečných států pro snížení rizika výpadků.
            * **Just-in-Time:** Výrobní systém, kdy se díly nevyrábí na sklad, ale dorazí do továrny přesně v minutu, kdy se montují do výrobku.
            * **Brussels Effect (Bruselský efekt):** Jev, kdy přísné regulace schválené v EU (např. USB-C nabíječky, GDPR) fakticky přijmou globální firmy pro celý svět.
            * **CBAM (Uhlíkové clo):** Poplatek na hranicích EU uvalený na 'špinavé' výrobky z Asie, který vyrovnává ceny vůči ekologicky zatíženým evropským firmám.
            * **ESG (Environmental, Social, Governance):** Tři pilíře (ekologie, společnost, řízení), podle kterých banky a investoři hodnotí udržitelnou odpovědnost firem.
            * **Greenwashing:** 'Lakováni na zeleno' – reklamní trik, kdy se firma tváří ekologicky jen na plakátu, ale její hlavní byznys zůstává neudržitelný.
            """)

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
            ], key="k5_1_debata_dane")
            submit_dane = st.form_submit_button("Odeslat a uložit můj názor 💾")
            
            if submit_dane:
                st.success("Tento problém nemá 'správnou' matematickou odpověď. Je to politické a filozofické rozhodnutí, které formuje podobu státu ve kterém chceme žít.")
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"]("Kapitola 5", "Podkapitola 1.2 - Debata Zdanění bohatých", nazor_dane)

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
        st.write("Nehádej. Otevři si skutečná data z Českého statistického úřadu a staň se na chvíli ekonomickým analytikem.")
        
        st.markdown("""
        **Zdroje pro vyřešení úkolu:**
        * [ČSÚ: Hlavní makroekonomické ukazatele](https://www.czso.cz/csu/czso/hlavni-makroekonomicke-ukazatele)
        * [ČSÚ: Aktuální inflace](https://www.czso.cz/csu/czso/mira_inflace)
        """)

        with st.form("detektiv_csu_form"):
            st.write("**Tvůj úkol:** Najdi aktuální hodnoty na webech ČSÚ výše a napiš své závěrečné hodnocení jako ekonomický komentátor zpráv:")
            analyza_text = st.text_area("Vyplň svou ekonomickou zprávu:", value="Na základě aktuálních dat ČSÚ (růst HDP: ___ %, inflace: ___ %) soudím, že se česká ekonomika nachází ve fázi (růstu / útlumu / krize). Protože...", key="k5_1_analyza_csu")
            
            if st.form_submit_button("Vydat a uložit zprávu 💾"):
                st.success("Tvá analýza byla přijata k otištění! Právě sis vyzkoušel práci reálného datového analytika.")
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"]("Kapitola 5", "Podkapitola 1.3 - Zpráva ČSÚ Detektiv", analyza_text)

        st.markdown("#### 1.3.1 Magický čtyřúhelník hospodářské politiky")
        st.write("Hospodářská politika sleduje několik cílů najednou. Klasicky se znázorňují jako **magický čtyřúhelník**. Je „magický“ proto, že **všechny cíle nejdou dokonale splnit současně**. Když se stát snaží masivně podpořit ekonomiku a snížit nezaměstnanost, obvykle tím vyvolá zdražování (zvýší inflaci). Proto je to vždy hledání rovnováhy.")

        st.markdown("""
        <div class='box-blue'>
            📐 <b>Pravidlo čtení grafu:</b><br>
            V ideálním světě by stát měl vysoký <b>hospodářský růst</b>, vysokou <b>vnější rovnováhu</b>, ale naopak velmi nízkou <b>inflaci</b> a nízkou <b>nezaměstnanost</b>. V reálných datech proto ideální čtyřúhelník nevypadá jako pravidelný čtverec, ale jako tvar, který je roztažený u růstu a smrsknutý u inflace/nezaměstnanosti.
        </div>
        """, unsafe_allow_html=True)

        st.divider()
        st.markdown("<div class='box-purple'>🕹️ <b>Simulátor: Nakresli si stav ekonomiky</b></div>", unsafe_allow_html=True)
        st.write("Zadej data pro dvě různá období (např. rok před krizí vs. krizový rok) a sleduj, jak se ekonomika zdeformuje.")

        col_obdobi1, col_obdobi2 = st.columns(2)

        with col_obdobi1:
            st.markdown("##### 📅 Období 1 (Před krizí)")
            hdp1 = st.slider("Růst HDP (%):", -10.0, 15.0, 3.0, step=0.5, key="hdp1")
            nez1 = st.slider("Nezaměstnanost (%):", 0.0, 20.0, 3.0, step=0.5, key="nez1")
            inf1 = st.slider("Inflace (%):", -2.0, 25.0, 2.0, step=0.5, key="inf1")
            bil1 = st.slider("Platební bilance k HDP (%):", -10.0, 10.0, 1.0, step=0.5, key="bil1")

        with col_obdobi2:
            st.markdown("##### 🚨 Období 2 (Zásah krize)")
            hdp2 = st.slider("Růst HDP (%):", -10.0, 15.0, -3.0, step=0.5, key="hdp2")
            nez2 = st.slider("Nezaměstnanost (%):", 0.0, 20.0, 8.0, step=0.5, key="nez2")
            inf2 = st.slider("Inflace (%):", -2.0, 25.0, 15.0, step=0.5, key="inf2")
            bil2 = st.slider("Platební bilance k HDP (%):", -10.0, 10.0, -4.0, step=0.5, key="bil2")

        kategorie = ['Růst HDP (%)', 'Nezaměstnanost (%)', 'Inflace (%)', 'Platební bilance (%)']

        fig = go.Figure()

        fig.add_trace(go.Scatterpolar(
            r=[hdp1, nez1, inf1, bil1],
            theta=kategorie,
            fill='toself',
            name='Období 1',
            line_color='#10b981'
        ))
        
        fig.add_trace(go.Scatterpolar(
            r=[hdp2, nez2, inf2, bil2],
            theta=kategorie,
            fill='toself',
            name='Období 2',
            line_color='#ef4444'
        ))

        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[-10, 25]
                )
            ),
            showlegend=True,
            margin=dict(l=40, r=40, t=40, b=40)
        )

        st.plotly_chart(fig, use_container_width=True)

        if st.button("Uložit nastavení čtyřúhelníku 💾", key="btn_k5_1_radar"):
            radar_data = f"Období 1: HDP {hdp1}%, Nez {nez1}%, Inf {inf1}%, Bil {bil1}% | Období 2: HDP {hdp2}%, Nez {nez2}%, Inf {inf2}%, Bil {bil2}%"
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"]("Kapitola 5", "Podkapitola 1.3 - Magický čtyřúhelník", radar_data)
            st.success("Nastavení bylo uloženo!")

        st.markdown("##### 🧐 Co graf říká o změně ekonomiky?")
        
        if hdp2 < 0:
            st.error(f"📉 **Ekonomika se propadla do recese:** HDP klesl na {hdp2} %. Stát přestal vytvářet bohatství, firmy omezují výrobu a odkládají investice.")
        elif hdp2 > hdp1:
            st.success(f"📈 **Zrychlení růstu:** Ekonomice se daří lépe než v Období 1, roste o {hdp2} %.")
            
        if inf2 > 10:
            st.error(f"💸 **Zloděj úspor úřaduje:** Inflace vyletěla na extrémních {inf2} %. Lidem se brutálně zdražily životní náklady a úspory ztrácejí hodnotu. ČNB by měla zakročit!")
        elif inf2 < 0:
            st.warning(f"❄️ **Deflace:** Ceny sice klesají ({inf2} %), ale to může být past – lidé odkládají nákupy a firmy musí zlevňovat a propouštět.")
            
        if nez2 > 7:
            st.error(f"🧑‍🔧 **Sociální problém:** Nezaměstnanost stoupla na {nez2} %. Mnoho lidí je bez práce, roste tlak na státní rozpočet (vyplácení podpor).")
        
        if inf2 > 5 and nez2 > 5 and hdp2 <= 0:
            st.warning("☠️ **STAGFLACE:** Tohle je noční můra ekonomů. Ekonomika neroste, lidé nemají práci, ale ceny přesto rychle rostou. Magický čtyřúhelník je v absolutním rozkladu.")

        st.divider()
        st.markdown("#### 1.4 Nástroje státu: Hospodářská politika")
        st.write("Hospodářská politika je soubor nástrojů, kterými stát a veřejné instituce ovlivňují ekonomiku. Nejde jen o vládu, obrovskou roli hraje i centrální banka.")

        st.markdown("""
        | Nástroj / oblast | Kdo ji používá | Co dělá | Příklad z praxe |
        | :--- | :--- | :--- | :--- |
        | 🏛️ **Fiskální politika** | Vláda, parlament, Ministerstvo financí | Pracuje se státním rozpočtem, daněmi, výdaji, dotacemi a investicemi. | Stát zvýší daně, vyplatí pomoc, investuje do dálnic. |
        | 🏦 **Monetární politika** | ČNB (centrální banka) | Ovlivňuje množství peněz, úrokové sazby a inflaci. | Zvýšení sazeb = dražší hypotéky (brzdí inflaci, ale ztíží bydlení). |
        | 🤝 **Sociální politika** | Ministerstva, obce | Vytváří záchrannou síť při nemoci, stáří, ztrátě práce. | Důchody, podpora v nezaměstnanosti, nemocenská. |
        | ⚖️ **Regulační politika** | Úřady, EU | Pravidla pro firmy, ochrana dat a životního prostředí. | Pravidla pro e-shopy, ochrana osobních údajů, emisní limity. |
        """)
        
        st.info("💡 **ČNB a vláda nejsou totéž:** Vláda rozhoduje o rozpočtu a daních. Česká národní banka (ČNB) je nezávislá a hlídá měnu a inflaci. Obě instituce ale ovlivňují stejnou ekonomiku a musí se navzájem doplňovat.")

        st.divider()
        st.markdown("#### 1.5 Kvíz: Poznáš funkci státu?")
        st.markdown("<div class='box-yellow'>🧠 <b>Otestuj své znalosti:</b> U každé situace urči, o jakou funkci nebo nástroj státu jde. Odpověz a pak si zkontroluj řešení:</div>", unsafe_allow_html=True)
        
        with st.form("fce_statu_quiz_v3"):
            q1 = st.selectbox("1. Vláda zvedne daně lidem s vysokými příjmy a peníze použije na podporu samoživitelů.", ["Vyber...", "Alokační funkce", "Redistribuční funkce", "Monetární politika", "Právní rámec"], key="k5_1_5_q1")
            q2 = st.selectbox("2. Stát financuje opravu mostu, který používají obyvatelé i firmy.", ["Vyber...", "Alokační funkce (Veřejný statek)", "Monetární politika", "Sociální politika", "Redistribuční funkce"], key="k5_1_5_q2")
            q3 = st.selectbox("3. ČNB zvýší úrokové sazby, aby pomohla brzdit inflaci.", ["Vyber...", "Fiskální politika", "Regulační politika", "Monetární politika (Stabilizační)", "Alokační funkce"], key="k5_1_5_q3")
            q4 = st.selectbox("4. Úřad řeší firmu, která klame zákazníky falešnou slevou.", ["Vyber...", "Monetární politika", "Právní a institucionální rámec (Regulace)", "Sociální politika", "Redistribuční funkce"], key="k5_1_5_q4")
            q5 = st.selectbox("5. Stát podporuje vzdělávání, protože z chytrých lidí má přínos i okolí a celá společnost.", ["Vyber...", "Negativní externalita", "Pozitivní externalita", "Monopol", "Platební bilance"], key="k5_1_5_q5")
            
            if st.form_submit_button("Zkontrolovat a uložit mé odpovědi 💾"):
                if q1 == "Redistribuční funkce" and q2 == "Alokační funkce (Veřejný statek)" and q3 == "Monetární politika (Stabilizační)" and q4 == "Právní a institucionální rámec (Regulace)" and q5 == "Pozitivní externalita":
                    st.success("✅ **Všechno správně!** Perfektně rozumíš tomu, jaké páky má stát v ruce.")
                else:
                    st.error("❌ Některá z odpovědí je chybná. \n\n*Správné řešení: 1. Redistribuční. 2. Alokační. 3. Monetární. 4. Právní. 5. Pozitivní externalita.*")

                quiz1_data = f"1:{q1} | 2:{q2} | 3:{q3} | 4:{q4} | 5:{q5}"
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"]("Kapitola 5", "Podkapitola 1.5 - Kvíz Funkce státu", quiz1_data)

        st.divider()
        st.markdown("#### 1.6 Mini aktivita: Stát jako správce společného účtu")
        st.write("Představ si, že tvá třída má společný rozpočet **100 000 Kč** na zlepšení života ve škole.")
        
        with st.form("mini_aktivita_16_v3"):
            st.write("Navrhni řešení a zamysli se nad souvislostmi s ekonomikou státu:")
            a16_1 = st.text_area("1. Rozděl peníze mezi 3 oblasti: A) bezpečnost/vybavení, B) pomoc slabším studentům, C) akce a rozvoj školy:", key="a16_1")
            a16_2 = st.text_area("2. Ke každé oblasti napiš, jakou funkci státu to připomíná (alokační, redistribuční, stabilizační...):", key="a16_2")
            a16_3 = st.text_area("3. Co by se stalo, kdyby o všem rozhodoval jen trh? (Tedy: kdo zaplatí, ten má službu/pomoc, kdo nezaplatí, nemá nic):", key="a16_3")
            a16_4 = st.text_area("4. Napiš jedno riziko příliš malého a jedno riziko příliš velkého zásahu státu/vedení školy:", key="a16_4")
            
            if st.form_submit_button("Uložit mé řešení 💾"):
                st.success("Skvělá práce! Uvědomil/a sis, že každé rozdělování peněz nese výhody i oběti, přesně jako státní rozpočet.")
                act16_data = f"1:{a16_1} | 2:{a16_2} | 3:{a16_3} | 4:{a16_4}"
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"]("Kapitola 5", "Podkapitola 1.6 - Správce společného účtu", act16_data)

        st.markdown("""
        <div class='box-green'>
            ✅ <b>Co si z tohoto bloku zapamatovat:</b> Stát v ekonomice není jen výběr daní. Vytváří pravidla hry, financuje veřejné statky, řeší tržní selhání, zmírňuje nerovnosti a snaží se stabilizovat ekonomiku. Zároveň ale každý zásah něco stojí a může mít vedlejší dopady — proto je hospodářská politika neustálé hledání kompromisů (viz magický čtyřúhelník).
        </div>
        """, unsafe_allow_html=True)

    # =========================================================================
    # SEKCE 2: DANĚ A STÁTNÍ ROZPOČET
    # =========================================================================
    elif selected_section_5.startswith("2."):
        st.markdown("### 2. Daně, státní rozpočet a ekonomická realita")
        
        st.markdown("""
        <div class='box-blue'>
            🧾 <b>Moderní hook:</b> Kolik státu odevzdáš z první brigády, prodeje na Vinted, streamování na Twitchi, spolupráce na TikToku nebo zisku z kryptoměn? Daně nejsou jen nudný formulář. Jsou to pravidla, která propojují tvé soukromé příjmy, veřejné služby, státní rozpočet a solidaritu.
        </div>
        """, unsafe_allow_html=True)

        st.divider()
        st.markdown("#### 2.1 Základy daňového systému: co je daň a proč existuje")
        st.write("Daň je povinná, zákonem stanovená platba do veřejného rozpočtu, za kterou člověk nebo firma obvykle nedostává přímou konkrétní protislužbu. Neplatíš daň z příjmu proto, aby ti stát druhý den opravil přesně tvou ulici. Platíš ji do společného systému.")

        st.markdown("##### ⚖️ Daň vs. Poplatek vs. Clo")
        col_dan1, col_dan2, col_dan3 = st.columns(3)
        with col_dan1:
            st.info("💸 **Daň**\nPovinná platba do společného rozpočtu. *Příklad: Daň z příjmů, DPH.*")
        with col_dan2:
            st.warning("🐕 **Poplatek**\nPlatba za konkrétní úkon, službu nebo evidenci. *Příklad: Poplatek za psa, za občanku.*")
        with col_dan3:
            st.error("📦 **Clo**\nPlatba spojená s dovozem zboží ze zahraničí (mimo EU). *Příklad: Balík z Asie nebo USA.*")

        st.divider()
        st.markdown("#### 2.2 Funkce daní a zásady zdaňování")
        st.write("Dobrá daň by neměla ekonomiku dusit. Měla by být srozumitelná, spravedlivá a efektivní.")
        
        with st.expander("Rozklikni pro zobrazení 4 funkcí daní"):
            st.markdown("""
            * 💰 **Fiskální:** Přináší peníze do státního rozpočtu na fungování státu.
            * 🏗️ **Alokační:** Pomáhá financovat veřejné statky (dálnice, hasiči), které by trh sám nepostavil.
            * 🤝 **Redistribuční:** Přerozděluje bohatství od bohatších k chudším (zmírňuje sociální nerovnosti).
            * 🚭 **Regulační:** Odrazuje od škodlivého chování (např. spotřební daň na alkohol a cigarety).
            """)

        st.markdown("##### ⚖️ Progresivní vs. Rovná daň")
        st.write("Měl by člověk s příjmem 200 000 Kč měsíčně platit vyšší procento než člověk s 30 000 Kč?")
        
        st.markdown("""
        | Typ zdanění | Princip | Výhoda | Riziko / Nevýhoda |
        | :--- | :--- | :--- | :--- |
        | 📏 **Rovná daň** | Všichni platí stejné procento ze základu daně. | Je jednoduchá a přehledná. Míň papírování. | Může být vnímána jako nespravedlivá k chudším. |
        | 📈 **Progresivní daň** | S vyšším příjmem roste procento daňové sazby. | Je solidárnější, bohatí unesou větší zátěž. | Může demotivovat lidi pracovat víc, nebo je nutit k odchodu do zahraničí. |
        """)

        st.markdown("""
        <div class='box-gray'>
            🧠 <b>Mýtus vs. Realita:</b><br>
            <i>Mýtus:</i> „Když mi přidají v práci a přejdu do vyššího daňového pásma (progrese), vydělám ve výsledku méně peněz, protože mi zdaní všechno víc.“<br>
            <i>Realita:</i> U běžné progresivní daně se vyšší sazbou obvykle daní AŽ ta část příjmu nad určitou hranicí, nikoliv úplně celý příjem. Člověk po zvýšení platu nikdy nebere méně peněz.
        </div>
        """, unsafe_allow_html=True)

        st.divider()
        st.markdown("#### 2.5 Přímé daně: Kdo je platí a z čeho?")
        st.write("Přímé daně platí konkrétní člověk nebo firma ze svého příjmu, zisku nebo majetku. Jsou přímo spojené s tvým jménem (nebo IČO).")

        col_pr1, col_pr2, col_pr3 = st.columns(3)
        with col_pr1:
            st.success("**Daň z příjmů fyzických osob (DPFO)**\nPlatíš ty. Z brigády, mzdy, podnikání, pronájmu nebo investic.")
        with col_pr2:
            st.warning("**Daň z příjmů právnických osob (DPPO)**\nPlatí firmy. S.r.o. odvádí státu peníze ze svého čistého zisku.")
        with col_pr3:
            st.info("**Daň z nemovitých věcí**\nPlatí majitel. Každý rok platíš obci za to, že vlastníš byt, dům nebo pozemek.")

        st.divider()
        st.markdown("#### 2.6 Nepřímé daně: Neviditelné daně v každém nákupu")
        st.write("Nepřímé daně jsou zahrnuté přímo v ceně zboží nebo služby. Spotřebitel (ty) je fakticky zaplatí v ceně u pokladny, ale státu je fyzicky odvádí prodejce nebo výrobce.")

        tab_dph, tab_spotrebni, tab_eko = st.tabs(["🛒 DPH (Účtenka)", "🚬 Spotřební daně (Hříchy)", "🌱 Ekologické daně (Příroda)"])
        
        with tab_dph:
            st.markdown("##### DPH (Daň z přidané hodnoty)")
            st.write("Daň zahrnutá v ceně většiny zboží a služeb (mobil, oblečení, kadeřnictví, lístek na akci, software). Je to absolutně největší příjem státního rozpočtu.")
            
            st.markdown("<div class='box-purple'>💻 <b>Kalkulačka: Anatomie tvé účtenky</b></div>", unsafe_allow_html=True)
            st.write("Když si koupíš produkt, část tvých peněz si nenechá obchod, ale musí je odevzdat státu. Zkus si to nasimulovat:")
            
            col_calc1, col_calc2 = st.columns(2)
            with col_calc1:
                cena_s_dph = st.number_input("Zadej celkovou cenu nákupu na účtence (Kč):", value=15000, step=100, key="k5_dph_cena")
            with col_calc2:
                sazba_dph = st.radio("Vyber sazbu DPH pro tento nákup:", ["21 % (Oblečení, mobil, většina zboží)", "12 % (Potraviny, léky, knihy, časopisy)"], key="k5_dph_sazba")
            
            sazba_cislo = 1.21 if "21" in sazba_dph else 1.12
            zaklad_dane = round(cena_s_dph / sazba_cislo, 2)
            castka_dph = round(cena_s_dph - zaklad_dane, 2)
            
            st.write("**Rozpad tvé zaplacené částky:**")
            col_u1, col_u2, col_u3 = st.columns(3)
            col_u1.metric("Základ daně (Zůstane obchodu)", f"{zaklad_dane} Kč")
            col_u2.metric("Sazba DPH", sazba_dph.split(" ")[0] + " %")
            col_u3.metric("Částka DPH (Jde státu)", f"{castka_dph} Kč")

            if st.button("Uložit výpočet DPH 💾", key="btn_k5_dph"):
                dph_data = f"Cena s DPH: {cena_s_dph} Kč | Sazba: {sazba_dph[:4]} | Základ: {zaklad_dane} Kč | DPH: {castka_dph} Kč"
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"]("Kapitola 5", "Podkapitola 2.6 - Kalkulačka DPH", dph_data)
                st.success("Výpočet DPH byl uložen!")

        with tab_spotrebni:
            st.markdown("##### Spotřební daně (Daně z hříchu / Sin taxes)")
            st.write("Daně uvalené na vybrané výrobky, které mají negativní dopad na zdraví. Stát tím získává obrovské příjmy a zároveň se snaží odrazovat lidi od škodlivé spotřeby.")
            
            st.markdown("<div class='box-purple'>🕹️ <b>Kalkulačka neřestí: Komu vlastně platíš?</b></div>", unsafe_allow_html=True)
            
            typ_neresti = st.selectbox("Co si kupuješ?", [
                "Krabička cigaret (cca 150 Kč)", 
                "Litr tvrdého alkoholu 40% (např. rum, vodka - cca 300 Kč)", 
                "Půllitr točeného piva 12° (cca 50 Kč)"
            ], key="k5_nerest_typ")

            if "cigaret" in typ_neresti:
                cena_n = 150
                spotrebni_n = 85
            elif "alkoholu" in typ_neresti:
                cena_n = 300
                spotrebni_n = 158
            else:
                cena_n = 50
                spotrebni_n = 2

            dph_n = round(cena_n - (cena_n / 1.21), 2)
            zbytek_n = round(cena_n - spotrebni_n - dph_n, 2)
            zdaneni_procento = round(((spotrebni_n + dph_n) / cena_n) * 100, 1)

            fig_nerest = go.Figure(go.Bar(
                x=[cena_n], y=['Cena'], orientation='h',
                marker=dict(color='rgba(0,0,0,0)'), showlegend=False, hoverinfo='none'
            ))
            fig_nerest.add_trace(go.Bar(name='Zisk výrobce a obchodu', x=[zbytek_n], y=['Rozpad ceny'], orientation='h', marker_color='#10b981'))
            fig_nerest.add_trace(go.Bar(name='Spotřební daň (Stát)', x=[spotrebni_n], y=['Rozpad ceny'], orientation='h', marker_color='#ef4444'))
            fig_nerest.add_trace(go.Bar(name='DPH (Stát)', x=[dph_n], y=['Rozpad ceny'], orientation='h', marker_color='#f59e0b'))
            fig_nerest.update_layout(barmode='stack', height=200, margin=dict(t=0, b=0, l=0, r=0))
            
            st.plotly_chart(fig_nerest, use_container_width=True)
            
            col_n1, col_n2 = st.columns(2)
            col_n1.markdown(f"**Cena pro tebe:** {cena_n} Kč | **Hodnota produktu:** {zbytek_n} Kč")
            col_n2.error(f"**Stát si z nákupu bere celkem: {zdaneni_procento} %**")

            if st.button("Uložit kalkulaci spotřební daně 💾", key="btn_k5_spotrebni"):
                nerest_data = f"Produkt: {typ_neresti} | Cena: {cena_n} Kč | Stát si bere: {zdaneni_procento}% ({spotrebni_n + dph_n:.1f} Kč)"
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"]("Kapitola 5", "Podkapitola 2.6 - Spotřební daň", nerest_data)
                st.success("Kalkulace neřesti byla uložena!")

        with tab_eko:
            st.markdown("##### Ekologické daně (Zdanění uhlíkové stopy)")
            st.write("Cílem je promítnout ničení životního prostředí (emise, smog, hluk) do ceny produktu.")
            
            cena_benzinu = st.slider("Cena 1 litru benzínu (Kč):", 25.0, 55.0, 38.0, step=0.5, key="k5_benzin_cena")
            
            spotrebni_dan_benzin = 12.84
            dph_benzin = round(cena_benzinu - (cena_benzinu / 1.21), 2)
            cista_cena = round(cena_benzinu - spotrebni_dan_benzin - dph_benzin, 2)
            
            fig_palivo = go.Figure(data=[go.Pie(
                labels=['Samotný benzín a marže pumpy', 'Fixní daň (Ekologická/Spotřební)', 'DPH (21 % z celku)'],
                values=[cista_cena, spotrebni_dan_benzin, dph_benzin],
                hole=.4,
                marker_colors=['#3b82f6', '#ef4444', '#f59e0b']
            )])
            fig_palivo.update_layout(margin=dict(t=20, b=20, l=20, r=20), height=300)
            
            col_graf1, col_graf2 = st.columns([1, 1])
            with col_graf1:
                st.plotly_chart(fig_palivo, use_container_width=True)
            with col_graf2:
                st.write("**Proč je to zdaněné tak moc?**")
                st.write("Stát touto daní vybírá peníze na opravu dálnic, ale také tím uměle zdražuje jízdu autem, aby lidi motivoval k šetření.")

        st.divider()
        st.markdown("#### 2.6.1 Schéma: Jak se daně dělí a kam putují")
        st.write("Daně se dělí na **přímé** (z příjmu/majetku) a **nepřímé** (schované v cenách v obchodě). Jakmile stát peníze vybere, dělí je mezi **státní rozpočet, kraje a obce**.")

        with st.expander("💸 DPFO, DPPO a DPH (Tzv. Sdílené daně)"):
            st.write("Jdou zčásti státu (na důchody, armádu, dálnice) a zčásti obcím/krajům (na školy, MHD, krajské silnice).")
            
        with st.expander("🏡 Daň z nemovitých věcí (Přímo tvé obci)"):
            st.write("Tato daň připadá ze 100 % obci nebo městu, kde nemovitost stojí (na chodníky, hřiště, údržbu).")

        st.markdown("<br><div class='box-yellow'>💬 <b>Diskusní aréna: Spravedlnost mezi regiony</b></div>", unsafe_allow_html=True)
        with st.form("diskuse_regiony"):
            st.write("Je spravedlivější, aby víc peněz z daní zůstávalo obcím, kde se vyberou, nebo aby se přerozdělovaly chudším regionům?")
            nazor_region = st.radio("Zvol si svůj postoj:", [
                "Ať peníze zůstanou tam, kde vznikly. Úspěšná města by neměla doplácet na ta pasivní.",
                "Stát musí být solidární. Peníze z bohatých center se musí rozdělovat i do chudších regionů.",
                "Měl by se najít kompromis."
            ], key="k5_2_6_regiony")
            if st.form_submit_button("Odeslat a uložit názor 💾"):
                st.success("Odesláno! Přesně o tomhle se vláda s kraji neustále hádá.")
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"]("Kapitola 5", "Podkapitola 2.6.1 - Přerozdělování regionům", nazor_region)

        st.divider()
        st.markdown("#### 2.7 Státní rozpočet: Velká státní peněženka")
        st.write("Státní rozpočet je plán příjmů a výdajů státu na 1 rok.")

        col_prijmy, col_vydaje = st.columns(2)
        with col_prijmy:
            st.success("📥 **Příjmy státního rozpočtu**\n* Daně, pojistné, poplatky, dotace z EU.")
        with col_vydaje:
            st.error("📤 **Výdaje státního rozpočtu**\n* Důchody, zdravotnictví, školství, obrana, platy státních zaměstnanců, obsluha dluhu.")

        st.markdown("<br><div class='box-purple'>📊 <b>Kam přesně jdou tvoje daně?</b></div>", unsafe_allow_html=True)
        labels_rozpocet = ['Důchody a sociální věci', 'Školství a vzdělávání', 'Doprava a investice', 'Zdravotnictví', 'Obrana a bezpečnost', 'Obsluha dluhu', 'Ostatní']
        values_rozpocet = [42, 13, 11, 9, 8, 5, 12]

        fig_rozpocet = go.Figure(data=[go.Pie(labels=labels_rozpocet, values=values_rozpocet, hole=.4, marker_colors=['#ef4444', '#3b82f6', '#f59e0b', '#10b981', '#6366f1', '#8b5cf6', '#94a3b8'])])
        fig_rozpocet.update_layout(margin=dict(t=20, b=20, l=0, r=0), height=350)
        st.plotly_chart(fig_rozpocet, use_container_width=True)

        st.divider()
        st.markdown("#### 2.8 Výdaje rozpočtu: Mandatorní a nemandatorní")
        col_vyd1, col_vyd2 = st.columns(2)
        with col_vyd1:
            st.error("🔒 **Mandatorní výdaje (80 % rozpočtu)**\nPovinné ze zákona (důchody, dávky, úroky z dluhu). Nelze je snadno škrtnout.")
        with col_vyd2:
            st.success("🛠️ **Nemandatorní výdaje (20 % rozpočtu)**\nVolné (investice do dálnic, věda, dotace). Zde se škrtá nejčastěji.")

        st.markdown("#### 2.9 Vyrovnaný, přebytkový a schodkový rozpočet")
        st.write("Pokud jsou výdaje vyšší než příjmy, vzniká **schodkový rozpočet (deficit)**. Stát si chybějící peníze musí půjčit.")

        st.divider()
        st.markdown("#### 2.10 Státní dluh a státní dluhopisy")
        st.write("Stát si půjčuje vydáváním **státních dluhopisů**. Dlouhodobé deficity vytvářejí **státní dluh**.")

        st.markdown("<div class='box-purple'>💸 <b>Simulátor investora: Zničí ti inflace tvůj dluhopis?</b></div>", unsafe_allow_html=True)
        col_dluh1, col_dluh2, col_dluh3 = st.columns(3)
        with col_dluh1:
            investice = st.number_input("Kolik státu půjčíš (Kč):", min_value=1000, value=100000, step=5000, key="k5_2_10_inv")
        with col_dluh2:
            urok_dluhopisu = st.slider("Roční úrok od státu (%):", 1.0, 10.0, 4.0, step=0.5, key="k5_2_10_urok")
        with col_dluh3:
            inflace = st.slider("Průměrná roční inflace (%):", 0.0, 15.0, 5.0, step=0.5, key="k5_2_10_inf")

        roky = 5
        konecna_castka = investice * ((1 + (urok_dluhopisu / 100)) ** roky)
        cisty_zisk_nominalni = konecna_castka - investice
        realna_hodnota = konecna_castka / ((1 + (inflace / 100)) ** roky)
        rozdil_kupni_sily = realna_hodnota - investice

        col_res1, col_res2 = st.columns(2)
        col_res1.metric("Peníze na účtu (Nominální)", f"{int(konecna_castka)} Kč", f"+ {int(cisty_zisk_nominalni)} Kč z úroků")
        col_res2.metric("Skutečná hodnota peněz (Reálná)", f"{int(realna_hodnota)} Kč", f"{int(rozdil_kupni_sily)} Kč kupní síla", delta_color="normal" if rozdil_kupni_sily>=0 else "inverse")

        if st.button("Uložit simulaci dluhopisu 💾", key="btn_k5_2_10"):
            dluh_sim_data = f"Investice: {investice} | Úrok: {urok_dluhopisu}% | Inflace: {inflace}% | Reálný zisk: {int(rozdil_kupni_sily)} Kč"
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"]("Kapitola 5", "Podkapitola 2.10 - Simulátor dluhopisu a inflace", dluh_sim_data)
            st.success("Simulace byla uložena!")

        st.divider()
        st.markdown("#### 2.11 Daňové úniky, optimalizace a stínová ekonomika")
        tab_opt, tab_seda, tab_cerna = st.tabs(["✅ Legální optimalizace", "🌫️ Šedá ekonomika (Úniky)", "🏴‍☠️ Černá ekonomika"])
        with tab_opt:
            st.success("Legální využití daňových slev a odpočtů v rámci zákona.")
        with tab_seda:
            st.warning("Nechání si zaplatit 'na ruku' bez dokladu a přiznání daně (šedá zóna).")
        with tab_cerna:
            st.error("Prodej drog, nelegální věci, pašování.")

    # =========================================================================
    # SEKCE 3: MOJE DANĚ V PRAXI
    # =========================================================================
    elif selected_section_5.startswith("3."):
        st.markdown("### 3. Moje daně v praxi")
        st.markdown("""
        <div class='box-blue'>
            💻 <b>Praktický přesah:</b> Daňový portál, datová schránka, elektronická identita a Portál občana ukazují, že moderní občan potřebuje rozumět tomu, jak vyřídit věci digitálně a bez front.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("#### 3.1 Digitální stát (eGovernment)")
        st.write("Identita občana (BankID), Datová schránka, Portál občana a MOJE daně (mojedane.cz).")

        st.markdown("<div class='box-purple'>🕹️ <b>Kvíz: Jaký portál na to použiješ?</b></div>", unsafe_allow_html=True)
        q_egov = st.radio("Jsi na dovolené a potřebuješ zjistit, jestli nemáš nezaplacenou pokutu za rychlost z řidičáku. Kam se přihlásíš?", [
            "Vyber odpověď...",
            "A) Přihlásím se do své e-mailové schránky na Seznamu/Gmailu.",
            "B) Přihlásím se na Portál občana pomocí své Bankovní identity.",
            "C) Přihlásím se na portál MOJE daně."
        ], key="k5_3_1_egov")

        if st.button("Uložit odpoveď na kvíz eGov 💾", key="btn_k5_3_1"):
            if "B)" in q_egov:
                st.success("✅ Správně! Portál občana řeší pokuty, řidičák a osobní doklady.")
            else:
                st.error("❌ Nesprávně. Správná odpověď je B (Portál občana).")
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"]("Kapitola 5", "Podkapitola 3.1 - eGovernment kvíz", q_egov[:30])

        st.divider()
        st.markdown("#### 3.2 Trenažér: „Tohle přece danit nemusím!“")
        with st.form("form_dane_praxe"):
            situace_praxe = st.selectbox("Vyber si svou životní situaci:", [
                "👗 1. Prodej oblečení na Vinted",
                "🎥 2. Příjmy z YouTube / TikToku (Reklamy a dary)",
                "🏠 3. Pronájem pokoje turistům přes Airbnb",
                "🪙 4. Zisk z prodeje kryptoměn (Bitcoin)",
                "📚 5. Pravidelné doučování angličtiny za hotové",
                "🍔 6. Nárazová brigáda (Dohoda o provedení práce)"
            ], key="k5_3_2_situace")
            
            otazky_student = st.text_area("Napiš 2-3 klíčové otázky, které si podle tebe musíš zjistit:", key="k5_3_2_otazky")
            submit_praxe = st.form_submit_button("Ověřit a uložit do databáze 💾")
            
            if submit_praxe:
                st.success("Odpověď uložena! Zde je stanovisko daňového experta:")
                if "Vinted" in situace_praxe:
                    st.info("Prodej vlastních použitých věcí je osvobozen. Prodej nakoupeného zboží za účelem zisku je podnikání.")
                elif "YouTube" in situace_praxe:
                    st.info("Soustavná tvorba obsahu za účelem zisku vyžaduje IČO. Barterové dárky se daní rovněž.")
                elif "kryptoměn" in situace_praxe:
                    st.info("Krypto nemá 3letý časový test. Daní se zisk z prodeje i směna krypto za krypto.")
                else:
                    st.info("Sleduj limity příjmů a soustavnost činnosti.")

                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"]("Kapitola 5", "Podkapitola 3.2 - Trenažér daně v praxi", f"Situace: {situace_praxe} | Otázky: {otazky_student}")

    # =========================================================================
    # SEKCE 4: GLOBÁLNÍ SOUVISLOSTI
    # =========================================================================
    elif selected_section_5.startswith("4."):
        st.markdown("### 4. Globální souvislosti a svět bez hranic")
        
        st.markdown("""
        <div class='box-blue'>
            🌐 <b>Moderní hook:</b> Tričko z Temu, mobil navržený v USA, čip z Tchaj-wanu, baterie z Číny. Globalizace znamená, že věci vznikají v obří mezinárodní síti.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("#### 4.1 Globalizace a mezinárodní obchod")
        st.write("Mezinárodní dělba práce, absolutní a komparativní výhoda.")

        st.markdown("<div class='box-yellow'>👩‍⚖️ <b>Mini kvíz: Komparativní výhoda advokátky</b></div>", unsafe_allow_html=True)
        kviz_advokatka = st.radio("Jsi nejlepší advokátka (3 000 Kč/h) a píšeš na klávesnici 2x rychleji než asistentka (300 Kč/h). Co uděláš?", [
            "Vyber řešení...",
            "A) Přepíšu si smlouvy sama. Jsem přece 2x rychlejší než asistentka.",
            "B) Najmu si asistentku. Můj ušetřený čas věnuji právní analýze (3 000 Kč/h)."
        ], key="k5_4_1_advokatka")

        if st.button("Uložit odpověď advokátky 💾", key="btn_k5_4_1"):
            if "B)" in kviz_advokatka:
                st.success("✅ Přesně tak! Tvá komparativní výhoda je v právu, ne v psaní na klávesnici.")
            elif "A)" in kviz_advokatka:
                st.error("❌ Prodělal/a jsi 2 700 Kč za hodinu, kterou jsi mohla věnovat právu.")
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"]("Kapitola 5", "Podkapitola 4.1 - Komparativní výhoda", kviz_advokatka[:30])

        st.divider()
        st.markdown("#### 4.2 Volný obchod, protekcionismus a cla")
        st.write("Clo, kvóty, embargo a technické normy.")

        st.markdown("<div class='box-purple'>🚗 <b>Simulátor: Cla na čínské elektromobily</b></div>", unsafe_allow_html=True)
        clo_eu = st.slider("Výše cla na dovoz čínských aut (% z ceny):", 0, 50, 0, step=5, key="k5_4_2_clo")
        cena_cina = int(700000 * (1 + (clo_eu / 100)))
        cena_eu = 900000

        c_col1, c_col2 = st.columns(2)
        c_col1.metric("Čínské auto s clem", f"{cena_cina:,} Kč".replace(',', ' '))
        c_col2.metric("Evropské auto", f"{cena_eu:,} Kč".replace(',', ' '))

        if st.button("Uložit výpočet cla 💾", key="btn_k5_4_2_clo"):
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"]("Kapitola 5", "Podkapitola 4.2 - Clo na elektromobily", f"Clo: {clo_eu}% | Čína: {cena_cina} Kč")
            st.success("Výpočet cla byl uložen!")

        st.divider()
        st.markdown("#### 4.4 EU a jednotný trh (Euro)")
        
        with st.form("form_euro_postoj"):
            st.write("**Mělo by Česko přijmout Euro?**")
            euro_rozhodnuti = st.text_area("Napiš své stanovisko: „Euro bych v ČR přijal/a / nepřijal/a, protože...“", key="k5_4_4_euro_text")
            if st.form_submit_button("Uložit mé stanovisko k Euru 💾"):
                st.success("Stanovisko bylo uloženo!")
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"]("Kapitola 5", "Podkapitola 4.4 - Postoj k Euru", euro_rozhodnuti)

    # =========================================================================
    # SEKCE 5: ESG A UDRŽITELNOST
    # =========================================================================
    elif selected_section_5.startswith("5."):
        st.markdown("### 5. ESG a udržitelná ekonomika")
        st.write("ESG: Environmental, Social, Governance. Cirkulární ekonomika a Greenwashing.")

        st.markdown("#### 5.1 Udržitelný rozvoj")
        volba_tenisky = st.selectbox("Zvol byznys strategii výroby tenisek:", [
            "Vyber...",
            "A) Výroba v Bangladéši za 50 Kč/ks (max zisk, škody na přírodě a lidech)",
            "B) Ruční eko-výroba v ČR za 8 000 Kč/ks (příliš drahé, nikdo nekoupí)",
            "C) Zlatá střední cesta: certifikovaná továrna, recykláty, cena 2 500 Kč"
        ], key="k5_5_1_tenisky")

        if st.button("Uložit strategii tenisek 💾", key="btn_k5_5_1"):
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"]("Kapitola 5", "Podkapitola 5.1 - Strategie tenisek", volba_tenisky[:30])
            st.success("Strategie byla uložena!")

        st.divider()
        st.markdown("#### 5.3 Greenwashing detector")
        with st.form("greenwashing_quiz"):
            q_gw1 = st.radio("Firma chrlí 50 000 plastových triček denně, ale udělala 10 'bio' kusů a má eko-kampaň.", ["Vyber...", "Greenwashing ❌", "Poctivé ESG ✅"], key="k5_5_3_q1")
            if st.form_submit_button("Vyhodnotit a uložit 💾"):
                if "Greenwashing" in q_gw1:
                    st.success("Přesně tak, toto je ukázkový Greenwashing!")
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"]("Kapitola 5", "Podkapitola 5.3 - Greenwashing test", q_gw1)

        st.divider()
        with st.form("form_esg_audit"):
            st.markdown("##### 🕵️ Audit značky z pohledu ESG")
            znacka_nazev = st.text_input("Název značky:", value="H&M", key="k5_5_6_znacka")
            znamka = st.select_slider("Známka ESG:", options=["A", "B", "C", "D", "E (Greenwashing)"], value="C", key="k5_5_6_znamka")
            argumenty_text = st.text_area("Zdůvodnění:", key="k5_5_6_arg")
            if st.form_submit_button("Uložit ESG audit značky 💾"):
                st.success(f"Audit pro značku {znacka_nazev} uložen!")
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"]("Kapitola 5", "Podkapitola 5.6 - Audit značky ESG", f"Značka: {znacka_nazev} | Známka: {znamka} | Text: {argumenty_text}")

    # =========================================================================
    # SEKCE 6: AKTIVITY A PŘÍPADOVÉ STUDIE
    # =========================================================================
    elif selected_section_5.startswith("6."):
        st.markdown("### 6. Aktivity a případové studie na závěr")
        
        tab_studie1, tab_studie2, tab_studie3, tab_ukol = st.tabs([
            "👕 1. Levné tričko za 99 Kč", 
            "📱 2. Student vydělává online", 
            "🏙️ 3. Obec rozhoduje o rozpočtu",
            "✍️ Mini úkol: Cesta produktu"
        ])

        with tab_studie1:
            st.markdown("#### Případová studie 1: Levné tričko za 99 Kč")
            with st.form("form_studie1"):
                ans1_1 = st.text_area("1. Kdo se podílel na cestě trička?:", key="cs1_1")
                ans1_2 = st.text_area("2. Jaké jsou viditelné a skryté náklady?:", key="cs1_2")
                ans1_3 = st.text_area("3. Vysvětli pojmy (Externalita, ESG...):", key="cs1_3")
                ans1_4 = st.text_area("4. Návrh opatření:", key="cs1_4")
                
                if st.form_submit_button("Odeslat a uložit Studie 1 💾"):
                    st.success("Řešení Bylo uloženo!")
                    cs1_data = f"Cesta: {ans1_1} | Náklady: {ans1_2} | Pojmy: {ans1_3} | Opatření: {ans1_4}"
                    if "uloz_odpoved_fn" in st.session_state:
                        st.session_state["uloz_odpoved_fn"]("Kapitola 5", "Případová studie 1 - Levné tričko", cs1_data)

        with tab_studie2:
            st.markdown("#### Případová studie 2: Student vydělává online")
            with st.form("form_studie2"):
                ans2_1 = st.text_area("1. Peněžní vs Nepeněžní příjem (Barter):", key="cs2_1")
                ans2_2 = st.text_area("2. Soustavné podnikání vs Jednorázový příjem:", key="cs2_2")
                ans2_3 = st.text_area("3. Na co se zeptat účetního/úřadu?:", key="cs2_3")
                
                if st.form_submit_button("Odeslat a uložit Studie 2 💾"):
                    st.success("Řešení bylo uloženo!")
                    cs2_data = f"Barter: {ans2_1} | Soustavnost: {ans2_2} | Otázky: {ans2_3}"
                    if "uloz_odpoved_fn" in st.session_state:
                        st.session_state["uloz_odpoved_fn"]("Kapitola 5", "Případová studie 2 - Student online", cs2_data)

        with tab_studie3:
            st.markdown("#### Případová studie 3: Obec rozhoduje o rozpočtu 10 mil. Kč")
            m_infra = st.slider("🛤️ Silnice a chodníky (mil. Kč):", 0.0, 10.0, 3.0, step=0.5, key="cs3_infra")
            m_skola = st.slider("🏫 Školství (mil. Kč):", 0.0, 10.0, 3.0, step=0.5, key="cs3_skola")
            m_soc = st.slider("🤝 Sociální péče (mil. Kč):", 0.0, 10.0, 2.0, step=0.5, key="cs3_soc")
            m_biz = st.slider("🏬 Podpora podnikání (mil. Kč):", 0.0, 10.0, 2.0, step=0.5, key="cs3_biz")

            if st.button("Uložit rozdělení obecního rozpočtu 💾", key="btn_cs3_rozpocet"):
                roz_obec_data = f"Silnice: {m_infra}m | Školství: {m_skola}m | Sociální: {m_soc}m | Podnikání: {m_biz}m"
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"]("Kapitola 5", "Případová studie 3 - Obecní rozpočet", roz_obec_data)
                st.success("Rozpočet obce byl uložen!")

        with tab_ukol:
            st.markdown("#### ✍️ Mini úkol: Cesta běžného produktu")
            with st.form("form_mini_ukol_cesta"):
                moj_produkt = st.text_input("Zvolený produkt:", value="Moje tenisky", key="uk_prod")
                st_design = st.text_input("1. Kde vznikl design?:", key="uk_des")
                st_suroviny = st.text_input("2. Odkud jsou suroviny?:", key="uk_sur")
                st_komplet = st.text_input("3. Kde se produkt smontoval?:", key="uk_kom")
                st_zisk = st.text_input("4. Kdo získal největší část marže?:", key="uk_marz")

                if st.form_submit_button("Odeslat a uložit analýzu produktu 💾"):
                    st.success("Analýza byla uložena!")
                    ukol_data = f"Produkt: {moj_produkt} | Design: {st_design} | Suroviny: {st_suroviny} | Kompletace: {st_komplet} | Marže: {st_zisk}"
                    if "uloz_odpoved_fn" in st.session_state:
                        st.session_state["uloz_odpoved_fn"]("Kapitola 5", "Mini úkol - Cesta produktu", ukol_data)

        st.divider()
        st.success("🎉 Gratulujeme k dokončení Kapitoly 5!")
