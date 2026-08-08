import streamlit as st
import plotly.graph_objects as go

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

        # =====================================================================
        # MAGICKÝ ČTYŘÚHELNÍK (INTERAKTIVNÍ GRAF) A NÁSTROJE STÁTU
        # =====================================================================

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

        # -----------------------------------------------------------------
        # Vykreslení interaktivního grafu (Plotly Radar Chart)
        # -----------------------------------------------------------------
        kategorie = ['Růst HDP (%)', 'Nezaměstnanost (%)', 'Inflace (%)', 'Platební bilance (%)']

        fig = go.Figure()

        # Období 1
        fig.add_trace(go.Scatterpolar(
            r=[hdp1, nez1, inf1, bil1],
            theta=kategorie,
            fill='toself',
            name='Období 1',
            line_color='#10b981'  # Zelená
        ))
        
        # Období 2
        fig.add_trace(go.Scatterpolar(
            r=[hdp2, nez2, inf2, bil2],
            theta=kategorie,
            fill='toself',
            name='Období 2',
            line_color='#ef4444'  # Červená
        ))

        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[-10, 25]  # Zajištění stejného měřítka pro všechny osy
                )
            ),
            showlegend=True,
            margin=dict(l=40, r=40, t=40, b=40)
        )

        # Zobrazení grafu
        st.plotly_chart(fig, use_container_width=True)

        # -----------------------------------------------------------------
        # Dynamické zhodnocení situace na základě zadaných posuvníků
        # -----------------------------------------------------------------
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
            q1 = st.selectbox("1. Vláda zvedne daně lidem s vysokými příjmy a peníze použije na podporu samoživitelů.", ["Vyber...", "Alokační funkce", "Redistribuční funkce", "Monetární politika", "Právní rámec"])
            q2 = st.selectbox("2. Stát financuje opravu mostu, který používají obyvatelé i firmy.", ["Vyber...", "Alokační funkce (Veřejný statek)", "Monetární politika", "Sociální politika", "Redistribuční funkce"])
            q3 = st.selectbox("3. ČNB zvýší úrokové sazby, aby pomohla brzdit inflaci.", ["Vyber...", "Fiskální politika", "Regulační politika", "Monetární politika (Stabilizační)", "Alokační funkce"])
            q4 = st.selectbox("4. Úřad řeší firmu, která klame zákazníky falešnou slevou.", ["Vyber...", "Monetární politika", "Právní a institucionální rámec (Regulace)", "Sociální politika", "Redistribuční funkce"])
            q5 = st.selectbox("5. Stát podporuje vzdělávání, protože z chytrých lidí má přínos i okolí a celá společnost.", ["Vyber...", "Negativní externalita", "Pozitivní externalita", "Monopol", "Platební bilance"])
            
            if st.form_submit_button("Zkontrolovat mé odpovědi"):
                if q1 == "Redistribuční funkce" and q2 == "Alokační funkce (Veřejný statek)" and q3 == "Monetární politika (Stabilizační)" and q4 == "Právní a institucionální rámec (Regulace)" and q5 == "Pozitivní externalita":
                    st.success("✅ **Všechno správně!** Perfektně rozumíš tomu, jaké páky má stát v ruce.")
                else:
                    st.error("❌ Některá z odpovědí je chybná. \n\n*Správné řešení: 1. Redistribuční (přerozdělování). 2. Alokační (veřejná infrastruktura). 3. Monetární (úroky řeší ČNB). 4. Právní (ochrana spotřebitele). 5. Pozitivní externalita.*")

        st.divider()
        st.markdown("#### 1.6 Mini aktivita: Stát jako správce společného účtu")
        st.write("Představ si, že tvá třída má společný rozpočet **100 000 Kč** na zlepšení života ve škole.")
        
        with st.form("mini_aktivita_16_v3"):
            st.write("Navrhni řešení a zamysli se nad souvislostmi s ekonomikou státu:")
            st.text_area("1. Rozděl peníze mezi 3 oblasti: A) bezpečnost/vybavení, B) pomoc slabším studentům, C) akce a rozvoj školy.")
            st.text_area("2. Ke každé oblasti napiš, jakou funkci státu to připomíná (alokační, redistribuční, stabilizační...):")
            st.text_area("3. Co by se stalo, kdyby o všem rozhodoval jen trh? (Tedy: kdo zaplatí, ten má službu/pomoc, kdo nezaplatí, nemá nic):")
            st.text_area("4. Napiš jedno riziko příliš malého a jedno riziko příliš velkého zásahu státu/vedení školy:")
            
            if st.form_submit_button("Uložit mé řešení"):
                st.success("Skvělá práce! Uvědomil/a sis, že každé rozdělování peněz nese výhody i oběti, přesně jako státní rozpočet.")

        st.markdown("""
        <aside>
            🤖 <b>AI mentoring:</b> Zkopíruj tento prompt do ChatGPT nebo Claude a nech si látku vysvětlit:<br>
            <i>„Vysvětli mi funkce státu v ekonomice na příkladu školy jako malé společnosti. Použij pojmy veřejný statek, externalita, monopol, redistribuce, fiskální politika, monetární politika a magický čtyřúhelník.“</i>
        </aside>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='box-green'>
            ✅ <b>Co si z tohoto bloku zapamatovat:</b> Stát v ekonomice není jen výběr daní. Vytváří pravidla hry, financuje veřejné statky, řeší tržní selhání, zmírňuje nerovnosti a snaží se stabilizovat ekonomiku. Zároveň ale každý zásah něco stojí a může mít vedlejší dopady — proto je hospodářská politika neustálé hledání kompromisů (viz magický čtyřúhelník).
        </div>
        """, unsafe_allow_html=True)

    # =========================================================================
    # SEKCE 2: DANĚ A STÁTNÍ ROZPOČET
    # =========================================================================
      

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
    # SEKCE 2: DANĚ A STÁTNÍ ROZPOČET
    # =========================================================================
    elif selected_section_5 == "2. Daně, státní rozpočet a ekonomická realita" or "2." in selected_section_5:
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
        st.markdown("<div class='box-purple'>💻 <b>Interaktivní průvodce: Musím to zdanit?</b></div>", unsafe_allow_html=True)
        st.write("Brigády, OnlyFans, kryptoměny nebo Vinted. Pojďme zbořit mýtus, že „z internetu a brigád se daně neplatí“. Zvol si situaci a zjisti, jaká jsou pravidla:")

        tab_brigada, tab_online, tab_vinted, tab_investice = st.tabs(["🍔 Brigáda a růžový papír", "📱 TikTok a Twitch", "👗 Vinted a Bazoš", "🪙 Krypto a Akcie"])

        with tab_brigada:
            st.markdown("##### Brigády, limity a „Růžový papír“")
            st.write("U dohod jako DPP nebo DPČ záleží na dvou věcech: jestli přesáhneš zákonný limit pro odvody a jestli podepíšeš **Prohlášení poplatníka k dani** (tzv. růžový papír).")
            st.write("Toto prohlášení ti umožňuje uplatnit základní *slevu na poplatníka* (2 570 Kč měsíčně), která ti čistou mzdu výrazně zvýší. Pozor: v jednom měsíci ho můžeš mít podepsaný jen u jednoho zaměstnavatele!")
            
            st.markdown("🧮 **Kalkulačka výdělku z brigády (DPP a DPČ):**")
            
            col_kalk1, col_kalk2 = st.columns(2)
            with col_kalk1:
                typ_dohody = st.radio("Vyber typ smlouvy:", ["DPP (Dohoda o provedení práce)", "DPČ (Dohoda o pracovní činnosti)"])
            with col_kalk2:
                roz_podepsano = st.radio("Máš podepsaný Růžový papír?", ["Ano, mám podepsáno", "Ne, nemám podepsáno"])
                
            hruby_vydelek = st.slider("Tvůj hrubý výdělek za měsíc (Kč):", 1000, 30000, 5000, step=500)
            
            # Logika zákonných limitů pro placení odvodů
            odvody_se_plati = False
            if "DPP" in typ_dohody and hruby_vydelek > 10000:
                odvody_se_plati = True
            elif "DPČ" in typ_dohody and hruby_vydelek >= 4000:
                odvody_se_plati = True

            # Výpočty daní a odvodů
            soc_poj = int(hruby_vydelek * 0.071) if odvody_se_plati else 0
            zdr_poj = int(hruby_vydelek * 0.045) if odvody_se_plati else 0
            dan_zaklad = int(hruby_vydelek * 0.15)
            
            if "Ano" in roz_podepsano:
                dan_konecna = max(0, dan_zaklad - 2570)
            else:
                dan_konecna = dan_zaklad
                
            cista_mzda = hruby_vydelek - soc_poj - zdr_poj - dan_konecna
            
            st.divider()
            
            # Dynamické upozornění na překročení limitu
            if odvody_se_plati:
                st.warning(f"⚠️ **Překročil/a jsi limit!** U {typ_dohody[:3]} se z částek nad limit musí odvádět sociální (7,1 %) a zdravotní pojištění (4,5 %) stejně jako u běžného zaměstnání.")
            else:
                st.success(f"✅ **Výdělek je v limitu.** Z této částky se neodvádí žádné sociální ani zdravotní pojištění.")
                
            # Přehledná tabulka výsledků
            col_v1, col_v2, col_v3 = st.columns(3)
            col_v1.metric("Hrubá mzda", f"{hruby_vydelek} Kč")
            col_v2.metric("Odvody (Soc+Zdr)", f"- {soc_poj + zdr_poj} Kč")
            col_v3.metric("Daň z příjmu", f"- {dan_konecna} Kč")
            
            st.markdown(f"<div style='background-color: #f0fdf4; padding: 15px; border-radius: 8px; border: 1px solid #10b981; text-align: center; margin-top: 15px;'><h3 style='margin: 0; color: #047857;'>💸 Čistá mzda na účet: {cista_mzda} Kč</h3></div>", unsafe_allow_html=True)
            
            if "Ne" in roz_podepsano and dan_konecna > 0:
                st.info("💡 **Tip:** Strženou daň si můžeš vyžádat zpět od státu, pokud si na jaře podáš Daňové přiznání (protože za rok jako student/brigádník pravděpodobně nevyčerpáš celou svou slevu na poplatníka).")
        with tab_online:
            st.markdown("##### Twitch, TikTok, Patreon, OnlyFans a Barter")
            st.write("Pokud dlouhodobě a soustavně vyděláváš tvorbou obsahu (spolupráce, předplatné, dary, prodej), jde obvykle o zdanitelný příjem a může se jednat o podnikání (na IČO).")
            st.warning("⚠️ **Pozor na Barter!** Pokud ti firma pošle zdarma drahý telefon nebo boty za to, že jim uděláš reklamu, nejedná se o „dárek“. Je to nepeněžní příjem v hodnotě té věci, a ten se musí také danit!")

        with tab_vinted:
            st.markdown("##### Prodej na Vinted, Bazoši a Aukru")
            st.write("Tady je potřeba si položit klíčovou otázku:")
            
            vinted_typ = st.radio("Jakým způsobem prodáváš?", [
                "Prodávám jen občas své vlastní použité oblečení, ze kterého jsem vyrostl/a.",
                "Soustavně nakupuji levné věci v sekáčích a přeprodávám je s přirážkou za účelem zisku."
            ])
            
            if "své vlastní" in vinted_typ:
                st.success("Tohle je v pořádku. Prodej vlastních použitých osobních věcí bývá od daně osvobozen. Nejde o podnikání.")
            else:
                st.error("Tohle už může být problém! Nakupování za účelem dalšího prodeje a zisku (soustavnost) je definicí podnikání. K tomu potřebuješ živnostenský list a musíš odvádět daně, jinak riskuješ pokutu.")

        with tab_investice:
            st.markdown("##### Kryptoměny, Akcie a ETF")
            st.write("Aplikace jako Revolut dělají nákup snadným, ale nezbaví tě povinnosti danit. Pravidla se navíc liší:")
            st.markdown("""
            * 📈 **Akcie a ETF:** V ČR existuje *časový test*. Pokud cenné papíry držíš déle než 3 roky, výnos z prodeje nedaníš (případně pokud neprodáš za více než 100 000 Kč za rok).
            * 🪙 **Kryptoměny (Bitcoin atd.):** Tady pozor! Z kryptoměn se platí daně ze zisku a *žádný 3letý časový test pro ně neplatí*! Navíc se daní i nákup jední kryptoměny za jinou.
            """)
            st.info("Pravidla investic a osvobození se často mění. Je vždy dobré sledovat aktuální legislativu nebo se poradit s účetním.")
