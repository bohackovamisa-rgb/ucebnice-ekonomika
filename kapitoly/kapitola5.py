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
# =========================================================================
    # DOKONČENÍ SEKCE 2: NEPŘÍMÉ DANĚ A ROZPOČET (2.6 - 2.9)
    # =========================================================================

# =====================================================================
        # DOKONČENÍ SEKCE 2: NEPŘÍMÉ DANĚ A SCHÉMA ROZDĚLOVÁNÍ (2.6 - 2.6.1)
        # =====================================================================

# =====================================================================
        # DOKONČENÍ SEKCE 2: NEPŘÍMÉ DANĚ A SCHÉMA ROZDĚLOVÁNÍ (2.6 - 2.6.1)
        # =====================================================================

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
                cena_s_dph = st.number_input("Zadej celkovou cenu nákupu na účtence (Kč):", value=15000, step=100)
            with col_calc2:
                sazba_dph = st.radio("Vyber sazbu DPH pro tento nákup:", ["21 % (Oblečení, mobil, většina zboží)", "12 % (Potraviny, léky, knihy, časopisy)"])
            
            # Výpočet DPH tzv. "shora"
            sazba_cislo = 1.21 if "21" in sazba_dph else 1.12
            zaklad_dane = round(cena_s_dph / sazba_cislo, 2)
            castka_dph = round(cena_s_dph - zaklad_dane, 2)
            
            st.write("**Rozpad tvé zaplacené částky:**")
            col_u1, col_u2, col_u3 = st.columns(3)
            col_u1.metric("Základ daně (Zůstane obchodu)", f"{zaklad_dane} Kč")
            col_u2.metric("Sazba DPH", sazba_dph.split(" ")[0] + " %")
            col_u3.metric("Částka DPH (Jde státu)", f"{castka_dph} Kč")
            
        with tab_spotrebni:
            st.markdown("##### Spotřební daně (Daně z hříchu / Sin taxes)")
            st.write("Daně uvalené na vybrané výrobky, které mají negativní dopad na zdraví. Stát tím získává obrovské příjmy a zároveň se snaží odrazovat lidi od škodlivé spotřeby (např. aby omezil budoucí náklady na léčbu nemocí).")
            
            st.markdown("<div class='box-purple'>🕹️ <b>Kalkulačka neřestí: Komu vlastně platíš?</b></div>", unsafe_allow_html=True)
            st.write("Vyber si produkt a podívej se, kolik peněz z tvé kapsy jde výrobci a kolik shrábne stát (přes DPH a brutální spotřební daň).")
            
            typ_neresti = st.selectbox("Co si kupuješ?", [
                "Krabička cigaret (cca 150 Kč)", 
                "Litr tvrdého alkoholu 40% (např. rum, vodka - cca 300 Kč)", 
                "Půllitr točeného piva 12° (cca 50 Kč)"
            ])

            # Hodnoty pro kalkulaci (přibližné reálné zdanění pro výuku)
            if "cigaret" in typ_neresti:
                cena_n = 150
                spotrebni_n = 85  # Spotřební daň z krabičky
            elif "alkoholu" in typ_neresti:
                cena_n = 300
                spotrebni_n = 158 # 39500 Kč / hl čistého lihu -> 40% z 1l = 158 Kč
            else:
                cena_n = 50
                spotrebni_n = 2   # Cca 2 Kč na půllitr 12° piva

            dph_n = round(cena_n - (cena_n / 1.21), 2)
            zbytek_n = round(cena_n - spotrebni_n - dph_n, 2)
            zdaneni_procento = round(((spotrebni_n + dph_n) / cena_n) * 100, 1)

            fig_nerest = go.Figure(go.Bar(
                x=[cena_n],
                y=['Cena'],
                orientation='h',
                marker=dict(color='rgba(0,0,0,0)'),
                showlegend=False,
                hoverinfo='none'
            ))
            fig_nerest.add_trace(go.Bar(name='Zisk výrobce a obchodu', x=[zbytek_n], y=['Rozpad ceny'], orientation='h', marker_color='#10b981'))
            fig_nerest.add_trace(go.Bar(name='Spotřební daň (Stát)', x=[spotrebni_n], y=['Rozpad ceny'], orientation='h', marker_color='#ef4444'))
            fig_nerest.add_trace(go.Bar(name='DPH (Stát)', x=[dph_n], y=['Rozpad ceny'], orientation='h', marker_color='#f59e0b'))
            fig_nerest.update_layout(barmode='stack', height=200, margin=dict(t=0, b=0, l=0, r=0))
            
            st.plotly_chart(fig_nerest, use_container_width=True)
            
            col_n1, col_n2 = st.columns(2)
            with col_n1:
                st.markdown(f"**Cena pro tebe:** {cena_n} Kč")
                st.markdown(f"**Reálná hodnota produktu:** jen {zbytek_n} Kč")
            with col_n2:
                st.error(f"**Stát si z nákupu bere celkem: {zdaneni_procento} %**")
            
        with tab_eko:
            st.markdown("##### Ekologické daně (Zdanění uhlíkové stopy)")
            st.write("Cílem je promítnout ničení životního prostředí (emise, smog, hluk) do ceny produktu. Aby 'levné na účtence' neznamenalo skrytě 'drahé pro přírodu a společnost'. Spadají sem daně z elektřiny, plynu a pevných paliv. V širším smyslu má tento ekologický efekt i zdanění pohonných hmot.")
            
            st.markdown("<div class='box-purple'>🚗 <b>Rozpitvej si cenu benzínu na pumpě</b></div>", unsafe_allow_html=True)
            
            cena_benzinu = st.slider("Cena 1 litru benzínu (Kč):", 25.0, 55.0, 38.0, step=0.5)
            
            # Spotřební/Ekologická daň na benzín je pevná (cca 12,84 Kč/litr)
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
                st.write("Stát touto daní vybírá peníze na opravu dálnic, ale také tím uměle zdražuje jízdu autem. Kdyby byl litr benzínu jen za 18 Kč (bez daní), lidé by jezdili auty mnohem více a dopady na smog, zácpy a emise by byly drastické.")

        st.divider()
        st.markdown("#### 2.6.1 Schéma: Jak se daně dělí a kam putují")
        st.markdown("""
        <div class='box-blue'>
            🧭 <b>Jak schéma číst:</b> Daně se dělí na <b>přímé</b> (z příjmu/majetku) a <b>nepřímé</b> (schované v cenách v obchodě). Jakmile stát peníze vybere, musí je podle tabulek rozdělit mezi <b>státní rozpočet, kraje a obce</b>. Přesné podíly se v čase mění, proto je důležité pochopit hlavní princip (kdo co dostává), než se učit nazpaměť procenta.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("##### 🗺️ Mapa daňových toků (Kde končí tvé peníze?)")
        
        with st.expander("💸 DPFO, DPPO a DPH (Tzv. Sdílené daně)"):
            st.write("**Daň z příjmů (fyzických i právnických osob) a DPH** se označují jako sdílené daně. Nejdou celé jednomu úřadu, ale obrovský balík peněz se dělí (tzv. Rozpočtové určení daní):")
            st.markdown("""
            * 🏛️ **Stát** si nechá většinu. Platí z ní plošné věci: důchody, sociální systém, armádu, platy hasičů, dálnice.
            * 🏢 **Obce a Kraje** dostanou svou porci, ze které financují regionální věci: místní školy, nemocnice, MHD a stavbu infrastruktury.
            """)
            
        with st.expander("🏡 Daň z nemovitých věcí (Přímo tvé obci)"):
            st.write("**Tato daň připadá typicky ze 100 % přímo obci nebo městu, kde nemovitost stojí.**")
            st.info("🏙️ **Příklad z praxe:** Když tvá rodina zaplatí daň z pozemku nebo domu, peníze pomáhají rozpočtu vaší radnice. Obec z nich neplatí 'jen tu jednu lampu před vaším domem', ale hodí je do společné kasy – na chodníky, údržbu zeleně, svoz odpadu, provoz místní školky nebo hřiště.")
            
        with st.expander("🚬 Spotřební a 🌱 Ekologické daně (Přímo státu)"):
            st.write("**Směřují především do státního (nebo veřejného) rozpočtu.**")
            st.write("Financují obecné výdaje státu a zároveň plní funkci jakési pokuty za to, že daný produkt vytváří budoucí zdravotní či ekologické náklady pro celou společnost.")

        with st.expander("📦 Clo (Přímo Evropské unii)"):
            st.write("**Souvisí s ochranou trhu celé EU.**")
            st.write("Když si objednáš balíček ze země mimo EU, vybírá se clo. Část peněz (provize) zůstane ČR za to, že to úředníci zpracovali, ale naprostá většina putuje rovnou do společného rozpočtu Evropské unie na financování evropských politik.")

        st.markdown("<br><div class='box-yellow'>💬 <b>Diskusní aréna: Spravedlnost mezi regiony</b></div>", unsafe_allow_html=True)
        with st.form("diskuse_regiony"):
            st.write("Je spravedlivější, aby víc peněz z daní zůstávalo obcím, kde se vyberou (např. v bohaté Praze nebo v místech s velkými fabrikami), nebo aby se velká část přerozdělovala od bohatších k chudším regionům, aby se rozvíjel celý stát?")
            nazor_region = st.radio("Zvol si svůj postoj:", [
                "Ať peníze zůstanou tam, kde vznikly. Úspěšná města by neměla doplácet na ta pasivní.",
                "Stát musí být solidární. Peníze z bohatých center se musí rozdělovat i do chudších regionů (např. na kvalitní školy a silnice pro všechny).",
                "Měl by se najít kompromis. Zohlednit, kde peníze vznikly, ale nastavit i minimální podporu pro chudší."
            ])
            if st.form_submit_button("Odeslat názor k zamyšlení"):
                st.success("Přesně kvůli této otázce se starostové s vládou hádají u každé úpravy zákona o rozpočtovém určení daní! Každý pohled má své silné argumenty.")
        st.divider()
# =====================================================================
        # DOKONČENÍ SEKCE 2: STÁTNÍ ROZPOČET (2.7)
        # =====================================================================

        st.divider()
        st.markdown("#### 2.7 Státní rozpočet: Velká státní peněženka")
        st.write("Státní rozpočet je plán příjmů a výdajů státu na určité období, obvykle na 1 rok. Ukazuje, odkud stát očekává peníze a za co je plánuje utratit.")

        # Tabulka příjmů a výdajů
        col_prijmy, col_vydaje = st.columns(2)
        with col_prijmy:
            st.success("📥 **Příjmy státního rozpočtu (Kde stát bere)**")
            st.markdown("""
            * Daně, pojistné a další povinné platby (drtivá většina).
            * Poplatky, příjmy z majetku státu, evropské dotace a prostředky.
            * *Případně půjčené peníze, pokud stát hospodaří s deficitem.*
            """)
            
        with col_vydaje:
            st.error("📤 **Výdaje státního rozpočtu (Za co stát utrácí)**")
            st.markdown("""
            * Důchody, sociální dávky, školství, obrana, bezpečnost.
            * Platy zaměstnanců veřejného sektoru (hasiči, učitelé, policisté), provoz úřadů, investice.
            * Obsluha státního dluhu (placení úroků), infrastruktura, krizová pomoc.
            """)

        st.markdown("<br><div class='box-purple'>📊 <b>Kam přesně jdou tvoje daně?</b></div>", unsafe_allow_html=True)
        st.write("Lidé si často myslí, že nejvíc peněz stát utratí za provoz úřadů nebo platy politiků. Podívej se na ilustrační rozpad rozpočtu. Přejeď myší přes jednotlivé dílky a uvidíš, že většinu peněz spolknou důchody a sociální služby:")

        # Interaktivní koláčový graf (Plotly) s ilustračními daty běžného rozpočtu ČR
        labels_rozpocet = [
            'Důchody a sociální věci', 
            'Školství a vzdělávání', 
            'Doprava a investice', 
            'Zdravotnictví (Státní část)', 
            'Obrana a bezpečnost', 
            'Obsluha státního dluhu (úroky)', 
            'Ostatní (Provoz státu, kultura, dotace)'
        ]
        values_rozpocet = [42, 13, 11, 9, 8, 5, 12] # Hodnoty v procentech

        fig_rozpocet = go.Figure(data=[go.Pie(
            labels=labels_rozpocet, 
            values=values_rozpocet, 
            hole=.4,
            marker_colors=['#ef4444', '#3b82f6', '#f59e0b', '#10b981', '#6366f1', '#8b5cf6', '#94a3b8']
        )])
        fig_rozpocet.update_layout(margin=dict(t=20, b=20, l=0, r=0), height=400)
        
        st.plotly_chart(fig_rozpocet, use_container_width=True)

        st.info("💡 **Kam jdou tvoje daně:** Velká část veřejných výdajů směřuje na sociální systém, důchody, školství, zdravotnictví a bezpečnost. Přesné podíly se samozřejmě každý rok mírně mění podle schváleného rozpočtu.")

        # Klikací zdroje
        st.markdown("##### 🔗 Odkazy do reality: Podívej se na skutečná data")
        st.write("Nevěř učebnicím, ověř si to na reálných vládních datech. Tady jsou aktuální zdroje:")
        
        st.markdown("""
        * 🏛️ [Monitor státní pokladny](https://monitor.statnipokladna.cz/) — Nejlepší přehled veřejných rozpočtů a reálného hospodaření státu (až na úroveň jednotlivých obcí).
        * 📄 [Ministerstvo financí ČR (Státní rozpočet)](https://www.mfcr.cz/cs/verejny-sektor/makroekonomika/statni-rozpocet) — Kompletní dokumenty, návrhy, schválené rozpočty a závěrečné účty.
        * 📈 [Státní dluhopisy ČR](https://www.sporicidluhopisycr.cz/) — Informace pro běžné občany k vybraným státním dluhopisům, pokud do nich chceš investovat.
        """)
# =====================================================================
        # DOKONČENÍ SEKCE 2: VÝDAJE ROZPOČTU (2.8)
        # =====================================================================

        st.divider()
        st.markdown("#### 2.8 Výdaje rozpočtu: Mandatorní a nemandatorní")
        st.write("V diskusích často zaznívá: *„Stát má velký dluh? Tak ať prostě přestane tolik utrácet a škrtne zbytečnosti!“* V realitě to ale zdaleka tak jednoduché není. Ne všechny výdaje státu se dají „škrtnout“ – většina z nich je totiž pevně daná zákony.")

        col_vyd1, col_vyd2 = st.columns(2)
        with col_vyd1:
            st.markdown("""
            <div style="background-color: #fef2f2; padding: 15px; border-left: 5px solid #ef4444; height: 100%;">
                <h5 style="margin-top: 0; color: #b91c1c;">🔒 Mandatorní výdaje (Povinné)</h5>
                <b>Co znamenají:</b> Výdaje pevně dané zákonem nebo smluvními závazky.<br><br>
                <b>Příklady:</b> Důchody, sociální dávky, podpora v nezaměstnanosti, platy státních zaměstnanců (často i zdravotnictví/školství) a splácení úroků ze státního dluhu.<br><br>
                <b>Proč jsou problém:</b> Stát je <b>musí</b> platit. Pokud je chce snížit, musí vláda změnit zákony, což musí projít parlamentem, prezidentem a často to vyvolá obrovské protesty veřejnosti. Zabírají zhruba 80 % rozpočtu ČR!
            </div>
            """, unsafe_allow_html=True)

        with col_vyd2:
            st.markdown("""
            <div style="background-color: #f0fdf4; padding: 15px; border-left: 5px solid #10b981; height: 100%;">
                <h5 style="margin-top: 0; color: #047857;">🛠️ Nemandatorní výdaje (Flexibilní)</h5>
                <b>Co znamenají:</b> Výdaje, o kterých se rozhoduje pružněji při schvalování rozpočtu.<br><br>
                <b>Příklady:</b> Investice do infrastruktury (nové dálnice), nákup armádní techniky, dotace firmám, věda a výzkum, podpora sportu.<br><br>
                <b>Proč jsou důležité:</b> Jsou to jediné peníze, o kterých mohou politici při tvorbě rozpočtu reálně a rychle vyjednávat. Právě zde se škrtá nejčastěji, což ale může brzdit budoucí rozvoj země (např. se nedostaví klíčová dálnice).
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br><div class='box-purple'>🕹️ <b>Reality check: Zahraj si na Ministra financí</b></div>", unsafe_allow_html=True)
        st.write("Stát má v našem ilustračním příkladu dluh 200 miliard Kč. Tvým úkolem je rozpočet zachránit a výdaje seškrtat. Jak se ti to povede?")

        # Simulátor škrtání rozpočtu
        with st.container(border=True):
            st.markdown("**Celkové roční výdaje státu: 2 200 miliard Kč**")
            st.progress(1.0) # Plný bar indikující 100% utrácení
            
            st.write("🔒 **Mandatorní výdaje:** 1 800 miliard Kč *(Tyto peníze jsou uzamčené v zákonech. Nelze je rychle škrtnout)*")
            
            st.write("🛠️ **Nemandatorní výdaje (Volné k dispozici):** 400 miliard Kč")
            skrty = st.slider("Kolik miliard z této volné částky se rozhodneš okamžitě škrtnout, abys snížil/a dluh?", 0, 400, 0, step=10)
            
            if skrty == 0:
                st.info("Zatím jsi neudělal/a žádné škrty. Dluh vesele roste o 200 miliard Kč ročně. Budeš nepopulární u ekonomů, ale voliči jsou zatím v klidu.")
            elif 0 < skrty < 150:
                st.warning(f"Ušetřil/a jsi {skrty} miliard Kč. Mírně jsi snížil/a dluh, ale zastavil/a jsi opravy několika dálnic a omezil/a dotace do zemědělství. Dluh ale dál roste.")
            elif 150 <= skrty < 300:
                st.error(f"Ušetřil/a jsi obrovských {skrty} miliard Kč! Dluh se zastavuje. Daní za to je ale úplné zastavení výstavby infrastruktury, zamrznutí peněz pro univerzity a nula peněz na inovace firem. Ekonomika může začít stagnovat.")
            else:
                st.error(f"Škrtl/a jsi extrémních {skrty} miliard Kč! Sice jsi vymazal/a dluh a ještě vytvořil/a přebytek, ale naprosto jsi ochromil/a chod země. Zrušil/a jsi vesměs všechny investice. V příštích volbách tě pravděpodobně smetou naštvaní voliči a podnikatelé.")

        st.markdown("""
        <div class='box-gray'>
            💡 <b>Co kdyby byl stát domácnost?</b><br>
            Domácnost má povinné platby (mandatorní výdaje): nájem, energie, splátky, jídlo. Těžko je můžeš ze dne na den nezaplatit. Stát to má podobně, ale <b>je tu jeden obrovský rozdíl:</b> Stát není běžná rodina. Na rozdíl od rodiny může stát legálně vybrat daně navíc, nebo vydávat státní dluhopisy a půjčovat si na finančních trzích. Přesto platí základní gravitace – dlouhodobé a neřízené deficity vytvářejí obrovský tlak na to, že v budoucnu bude muset stát buď dramaticky zvednout daně, nebo radikálně snížit kvalitu služeb a důchodů.
        </div>
        """, unsafe_allow_html=True)
# =====================================================================
        # PODKAPITOLA 2.9: TYPY ROZPOČTŮ
        # =====================================================================

        st.divider()
        st.markdown("#### 2.9 Vyrovnaný, přebytkový a schodkový rozpočet")
        st.write("Státní rozpočet může na konci roku dopadnout třemi způsoby. Vše závisí na tom, jak se poperou příjmy (vybrané daně) s výdaji (útrata státu).")

        col_r1, col_r2, col_r3 = st.columns(3)
        with col_r1:
            st.info("⚖️ **Vyrovnaný rozpočet**\nPříjmy se přesně rovnají výdajům.\n*(Stát vybere 100, utratí 100)*")
        with col_r2:
            st.success("📈 **Přebytkový rozpočet**\nPříjmy jsou vyšší než výdaje.\n*(Stát vybere 100, utratí 95)*")
        with col_r3:
            st.error("📉 **Schodkový rozpočet (Deficit)**\nVýdaje jsou vyšší než příjmy.\n*(Stát vybere 100, utratí 120. Rozdíl 20 si musí půjčit!)*")

        st.markdown("""
        <div class='box-yellow'>
            ⚠️ <b>Život na dluh:</b> Deficit (schodek) nemusí být vždy automaticky katastrofa — například během tvrdé krize, pandemie nebo povodní musí stát masivně podpořit ekonomiku. Problém vzniká ve chvíli, kdy se deficity opakují dlouhodobě i v době, kdy ekonomika roste a daří se jí. Dluh pak roste rychleji než schopnost státu ho unést.
        </div>
        """, unsafe_allow_html=True)


# =====================================================================
        # PODKAPITOLA 2.10: STÁTNÍ DLUH A DLUHOPISY (VČETNĚ BANKROTU)
        # =====================================================================

        st.divider()
        st.markdown("#### 2.10 Státní dluh a státní dluhopisy")
        st.write("Pokud má stát dlouhodobě schodkový rozpočet (utrácí víc, než vybere na daních), logicky mu chybí peníze. Jak už víme, stát si nemůže peníze donekonečna jen tak tisknout. Musí si je legálně půjčit na finančních trzích. Tím vzniká **státní dluh**. Hlavním nástrojem, jak si stát půjčuje, jsou **státní dluhopisy**.")

        st.markdown("""
        <div class='box-blue'>
            📄 <b>Státní dluhopis jednoduše:</b> Když stát vydá dluhopis, nabízí tím investorům "dlužní úpis". Investor (banka, fond, nebo i ty) státu půjčí své peníze a stát slíbí, že je za několik let vrátí zpět a jako odměnu přidá pravidelný úrok.
        </div>
        """, unsafe_allow_html=True)

        with st.expander("❓ FAQ: Kdo dluhopisy kupuje a proč stát dluhy dělá?"):
            st.markdown("""
            * **Kdo kupuje státní dluhopisy?** Banky, investiční fondy, pojišťovny, zahraniční investoři, ale někdy i běžní občané (např. v ČR tzv. Dluhopis Republiky).
            * **Proč je stát vůbec vydává?** Aby financoval letošní schodek rozpočtu, pokryl nečekané krizové výdaje, nebo tzv. refinancoval starší dluh (zkrátka si vezme novou půjčku, aby mohl splatit tu starou, jejíž čas právě vypršel).
            """)

        st.markdown("<div class='box-purple'>💸 <b>Simulátor investora: Zničí ti inflace tvůj dluhopis?</b></div>", unsafe_allow_html=True)
        st.write("Rozhodl/a ses půjčit českému státu peníze na **5 let** formou dluhopisů. Stát ti slíbil garantovaný úrok. Budou ale peníze, které ti stát za pět let pošle zpět, reálně stačit na víc věcí? Nasimuluj si vliv inflace:")

        col_dluh1, col_dluh2, col_dluh3 = st.columns(3)
        with col_dluh1:
            investice = st.number_input("Kolik státu půjčíš (Kč):", min_value=1000, value=100000, step=5000)
        with col_dluh2:
            urok_dluhopisu = st.slider("Roční úrok od státu (%):", 1.0, 10.0, 4.0, step=0.5)
        with col_dluh3:
            inflace = st.slider("Průměrná roční inflace (%):", 0.0, 15.0, 5.0, step=0.5)

        # Matematika složeného úročení na 5 let
        roky = 5
        konecna_castka = investice * ((1 + (urok_dluhopisu / 100)) ** roky)
        cisty_zisk_nominalni = konecna_castka - investice
        
        # Očištění o inflaci (reálná kupní síla peněz za 5 let v dnešních cenách)
        realna_hodnota = konecna_castka / ((1 + (inflace / 100)) ** roky)
        rozdil_kupni_sily = realna_hodnota - investice

        col_res1, col_res2 = st.columns(2)
        with col_res1:
            st.metric("Peníze fyzicky na účtu (Nominální)", f"{int(konecna_castka)} Kč", f"+ {int(cisty_zisk_nominalni)} Kč z úroků")
            st.write("*(Tohle číslo uvidíš v bance. Stát dodržel slovo a vyplatil tě.)*")
            
        with col_res2:
            if rozdil_kupni_sily >= 0:
                st.metric("Skutečná hodnota peněz (Reálná)", f"{int(realna_hodnota)} Kč", f"+ {int(rozdil_kupni_sily)} Kč v kupní síle")
                st.success("✅ **Vyhrál/a jsi!** Úrok z dluhopisu byl vyšší než inflace. Skutečně jsi zbohatl/a.")
            else:
                st.metric("Skutečná hodnota peněz (Reálná)", f"{int(realna_hodnota)} Kč", f"{int(rozdil_kupni_sily)} Kč v kupní síle", delta_color="inverse")
                st.error("❌ **Prohrál/a jsi s inflací.** Sice máš víc peněz, ale v obchodech vše zdražilo ještě víc.")

        st.divider()
        st.markdown("##### 📈 Tvůj osobní podíl na státním dluhu")
        st.write("Dluh státu se neplatí sám od sebe. Dluží ho občané. Pokud celkový dluh ČR (který je v bilionech korun) vydělíme počtem obyvatel (včetně novorozenců), získáme **dluh na jednoho Čecha**.")

        # Simulátor budoucího dluhu
        st.markdown("**Vyzkoušej si, kde to může skončit:** Nastav, jaký průměrný roční schodek (deficit) budou politici v následujících 10 letech sekat. Graf ti ukáže, jak se vyvíjel tvůj osobní dluh v minulosti a kam vystřelí v budoucnu.")
        
        roky_historie = [2000, 2005, 2010, 2015, 2020, 2024]
        dluh_historie = [28000, 68000, 128000, 158000, 192000, 295000] # Orientační data vývoje v ČR
        
        budouci_schodek = st.slider("Průměrný roční schodek vlády na dalších 10 let (mld. Kč):", 0, 500, 250, step=25)
        
        # Výpočet pro rok 2034 (10 let od 2024): 10 let * schodek mld / 10.9 milionu obyvatel
        # 1 mld / 10.9 mil obyvatel = cca 91.7 Kč na osobu
        prirustek_na_osobu = budouci_schodek * 10 * 91.7
        dluh_2034 = 295000 + prirustek_na_osobu
        
        fig_dluh = go.Figure()
        fig_dluh.add_trace(go.Scatter(x=roky_historie, y=dluh_historie, mode='lines+markers', name='Historie', line=dict(color='#3b82f6', width=3)))
        fig_dluh.add_trace(go.Scatter(x=[2024, 2034], y=[295000, dluh_2034], mode='lines+markers', name='Tvá prognóza', line=dict(color='#ef4444', width=3, dash='dash')))
        
        fig_dluh.update_layout(title="Vývoj státního dluhu na 1 obyvatele ČR (Kč)", margin=dict(t=40, b=20, l=20, r=20), height=350)
        st.plotly_chart(fig_dluh, use_container_width=True)

        st.markdown("##### 💥 Co se stane, když stát zkrachuje (Státní bankrot)?")
        st.write("Pokud dluh roste příliš rychle, investoři (banky) státu přestanou věřit. Řeknou si: *„Tenhle stát už nemá šanci to splatit.“* V tu chvíli odmítnou státu dál půjčovat, nebo požadují extrémní úroky (klidně 30 % ročně).")
        
        st.markdown("""
        <div style="background-color: #fef2f2; padding: 15px; border-left: 5px solid #dc2626;">
            <p><b>Státní bankrot (Default) neznamená, že stát přestane existovat na mapě. Znamená to, že státní pokladna je prázdná a stát ze dne na den oznámí, že nemůže splatit své dluhy. A dopady na občany jsou brutální:</b></p>
            <ul>
                <li><b>Zmrznutí státních peněz:</b> Stát nemá na účtu hotovost. Ze dne na den se tak zpozdí nebo nevyplatí důchody a dramaticky se sníží platy učitelů, hasičů, policistů či lékařů.</li>
                <li><b>Drastické škrty a daně:</b> Vláda musí okamžitě najít peníze. Služby (jako školy a nemocnice) přestanou být zdarma, zruší se veškeré dotace a skokově se zvýší daně obyvatelům.</li>
                <li><b>Propad měny a hyperinflace:</b> Pokud se stát pokusí z dluhu "vykupit" tím, že natiskne nové peníze, měna ztratí hodnotu. V obchodech vše extrémně zdraží a celoživotní úspory lidí se promění v bezcenné papírky.</li>
                <li><b>Ztráta důvěry:</b> Na záchranu často musí přijet MMF (Mezinárodní měnový fond). Ten státu půjčí jen pod podmínkou těch nejtvrdších a nejbolestivějších škrtů (přesně to zažilo např. <b>Řecko nebo Argentina</b>).</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.info("💡 **Poučení pro Gen Z:** Každý dluh se musí zaplatit. Extrémní dluh znamená, že stát musí platit obrovské úroky (tzv. obsluha dluhu). Tyto peníze pak chybí na školy, modernizaci nebo platy. V budoucnu to tak zaplatí dnešní mladá generace – mnohem vyššími daněmi nebo nižšími důchody.")
