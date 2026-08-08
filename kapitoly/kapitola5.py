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

    # =========================================================================
    # SEKCE 4: GLOBÁLNÍ SOUVISLOSTI
    # =========================================================================
   
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
# =====================================================================
        # PODKAPITOLA 2.11: ÚNIKY, OPTIMALIZACE A STÍNOVÁ EKONOMIKA
        # =====================================================================

        st.divider()
        st.markdown("#### 2.11 Daňové úniky, optimalizace a stínová ekonomika")
        st.write("Ne každé snížení daní je hned zločin. Je obrovský rozdíl mezi tím, když uplatníš zákonnou slevu pro studenta, a tím, když prodáváš kradené telefony. Pojďme si v tom udělat pořádek:")

        tab_opt, tab_seda, tab_cerna = st.tabs(["✅ Legální optimalizace", "🌫️ Šedá ekonomika (Úniky)", "🏴‍☠️ Černá ekonomika"])

        with tab_opt:
            st.markdown("##### Legální daňová optimalizace")
            st.write("**Co to je:** Využití zákonných možností k tomu, abys zaplatil/a státu na daních co nejméně.")
            st.success("Tohle je naprosto legální a v pořádku. Patří sem: uplatnění slevy na studenta, odečtení úroků z hypotéky, využití paušálních výdajů u živnostníků, nebo investice s daňovým zvýhodněním.")
            
        with tab_seda:
            st.markdown("##### Šedá ekonomika a nelegální daňové úniky")
            st.write("**Co to je:** Samotná práce nebo produkt jsou sice legální (např. oprava auta, ostříhání vlasů, doučování), ale příjem za ně **není zdaněn a přiznán**.")
            st.warning("Patří sem: peníze vyplácené 'na ruku' bez smlouvy, práce na černo, nebo když ti řemeslník nabídne 'udělám vám to levněji, ale bez papíru a bez DPH'. Jde o krácení daní, což je trestný čin.")
            
        with tab_cerna:
            st.markdown("##### Černá ekonomika")
            st.write("**Co to je:** Samotná činnost je nelegální a mimo zákonný systém.")
            st.error("Patří sem: prodej drog, obchod s padělky (falešné kabelky Gucci z tržnice), pašování zbraní nebo prostituce. Tyto peníze nikdy neprojdou systémem.")

        st.markdown("<div class='box-purple'>🛠️ <b>Simulátor řemeslníka: Chceš to levněji „bez papíru“?</b></div>", unsafe_allow_html=True)
        st.write("Představ si situaci: Necháváš si opravit dům. Zedník ti řekne: *„Pokud mi to dáte v hotovosti bez faktury (a já nebudu platit daně a pojištění), udělám vám to o 20 % levněji.“* Ušetříš ty a vydělá zedník. Je to win-win? Ne tak úplně.")
        
        with st.container(border=True):
            volba_prace = st.radio("Zvol si svou cestu jako zedník:", [
                "Být poctivý OSVČ: Dám zákazníkovi fakturu, zaplatím sociální, zdravotní a DPH.",
                "Šedá zóna (na ruku): Vezmu to bez dokladu v hotovosti, ušetřím na daních a o peníze se nepodělím."
            ])
            
            if "poctivý" in volba_prace:
                st.success("✅ **Zákazník sice zaplatil o něco víc, ale ty jako zedník máš zajištěnou budoucnost.**")
                st.write("* Platíš si pojištění. Pokud na stavbě spadneš a zlomíš si nohu, dostaneš **nemocenskou** a zaplatí ti operaci.")
                st.write("* Tvé příjmy se počítají do **starobního důchodu**.")
                st.write("* Zákazník má doklad, takže pokud mu zednická práce do týdne spadne na hlavu, může ji reklamovat a domáhat se nápravy.")
            else:
                st.error("🚨 **Peníze v hotovosti máš, ale za jakou cenu?**")
                st.write("* Lhal jsi státu (daňový podvod).")
                st.write("* **Neplatíš sociální pojištění.** Až budeš starý, stát ti vypočítá důchod třeba jen 6 000 Kč a neuživíš se.")
                st.write("* Pokud si zlomíš ruku a nemůžeš 3 měsíce pracovat, **nemáš nárok na žádnou nemocenskou**. Jsi bez příjmu.")
                st.write("* Zákazník je hlupák. Nemá fakturu. Když oprava praskne, nemůže reklamovat vůbec nic, protože oficiálně tam nikdo nikdy nebyl.")

        st.markdown("##### 🏢 Jak se vyhýbají daním obří korporace?")
        st.write("Malý podnikatel to řeší 'prací na ruku', ale nadnárodní giganti (Google, Apple, Amazon) to dělají chytřeji. Mají obří týmy právníků a využívají mezer v mezinárodním právu.")
        
        st.markdown("""
        * 🌴 **Daňové ráje:** Firma vytvoří obrovský zisk z prodeje reklamy v ČR, ale peníze formálně převede (např. přes fiktivní poplatky za licenci) do své pobočky na Bahamách nebo v Irsku, kde je daň ze zisku třeba jen 1 % nebo nulová.
        * 🌍 **Co s tím dělá stát?** Běžný stát proti tomu nic nezmůže. Proto se státy sdružují (Evropská unie, OECD) a snaží se zavést **Globální minimální daň** (aby velké firmy platily alespoň 15 % daň bez ohledu na to, kam se na světě papírově přestěhují). Řeší se také tzv. **Digitální daň**.
        """)
# =====================================================================
        # PODKAPITOLA 2.12: PRAKTICKÉ PRVKY DO NOTION A ZÁVĚR
        # =====================================================================

        st.divider()
        st.markdown("#### 2.12 Praktické prvky: Mzda, účtenka a daňové dilema")
        st.write("Všechny tyhle teorie z učebnice se střetnou s realitou přesně v momentě, kdy dostaneš svou první výplatní pásku z brigády, nebo když poprvé pošleš fakturu za správu sociálních sítí.")

        st.markdown("<div class='box-purple'>🧮 <b>Interaktivní kalkulačka: Jak z tebe stát udělá plátce?</b></div>", unsafe_allow_html=True)
        st.write("Vyzkoušej si modelovou brigádu (Dohodu o provedení práce - DPP). Nastav si hodinovku a počet hodin, které za měsíc odpracuješ. Sleduj, jak drasticky se změní výsledek, když překročíš magický zákonný limit (který je aktuálně 10 000 Kč).")

        # Edukativní kalkulačka mzdy z brigády (aktualizováno)
        col_mzda1, col_mzda2 = st.columns(2)
        with col_mzda1:
            hodinovka = st.slider("Tvá hodinová odměna (Kč/hod):", 120, 250, 150, step=10)
        with col_mzda2:
            hodiny_mesic = st.slider("Odpracováno hodin za měsíc:", 10, 100, 40, step=5)
            
        st.write("*Pro tento příklad předpokládáme, že MÁŠ podepsaný růžový papír (slevu na poplatníka).*")

        hruba_mzda_dpp = hodinovka * hodiny_mesic
        
        # Logika překročení limitu 10 000 Kč (nutnost platit sociální a zdravotní z celé částky!)
        if hruba_mzda_dpp > 10000:
            soc = int(hruba_mzda_dpp * 0.071)
            zdr = int(hruba_mzda_dpp * 0.045)
            odvody_strzeno = soc + zdr
            upozorneni_limit = "⚠️ **Překročen limit 10 000 Kč!** Z celé tvé výplaty ti stát okamžitě strhl sociální (7,1 %) a zdravotní (4,5 %) pojištění."
        else:
            odvody_strzeno = 0
            upozorneni_limit = "✅ **Jsi pod limitem 10 000 Kč.** Neplatíš žádné zdravotní ani sociální pojištění."

        # Výpočet daně z příjmu (15 %) po odečtení odvodů (pro zjednodušenou edukaci) a aplikaci slevy na poplatníka
        dan = max(0, int(hruba_mzda_dpp * 0.15) - 2570) # 2570 je sleva na poplatníka
        
        cista_mzda_dpp = hruba_mzda_dpp - odvody_strzeno - dan

        st.markdown(f"**Hrubá mzda (co sis vydělal/a): {hruba_mzda_dpp} Kč**")
        if odvody_strzeno > 0:
            st.error(upozorneni_limit)
        else:
            st.success(upozorneni_limit)
            
        col_f1, col_f2 = st.columns(2)
        col_f1.metric("Strženo na odvodech a daních", f"- {odvody_strzeno + dan} Kč")
        col_f2.metric("Tvá čistá mzda na účet", f"{cista_mzda_dpp} Kč")

        st.markdown("##### 🔗 Odkazy do reality: Kde si věci ověřovat?")
        st.write("Dobrý občan nemusí znát všechny zákony nazpaměť. Musí ale vědět, kde najít pravdu, když má pochybnosti o svých výdělcích online nebo ze studentského podnikání.")
        
        st.markdown("""
        * 🏢 [Finanční správa ČR (mojedane.cz)](https://www.mojedane.cz/) — Hlavní portál státu.
        * 💻 **Elektronické formuláře (EPO):** Na portálu Moje daně si můžeš *bez přihlašování* rozkliknout formulář k Daňovému přiznání. Zkuste si ve třídě společně v 'Průvodci' nacvakat fiktivního studenta, který fotí na IČO.
        * 🧮 [Kalkulačky MPSV](https://www.mpsv.cz/kalkulacky) — Oficiální státní kalkulačky k důchodům a dávkám. Na hrubou/čistou mzdu používej raději kalkulačky renomovaných ekonomických portálů (např. Kurzy.cz, Peníze.cz) a **vždy si zkontroluj aktuální rok**, protože pravidla se často mění.
        """)

        st.markdown("##### ⚖️ Optimalizace vs. Únik: Tahák pro praxi")
        st.write("Tenká, ale zásadní hranice mezi chytrostí a kriminálem:")
        st.markdown("""
        | ✅ Legální optimalizace (Jsi chytrý) | 🚨 Nelegální daňový únik (Jsi zločinec) |
        | :--- | :--- |
        | Uplatním slevu na poplatníka (jsem student). | Zatajím část příjmů z Instagramu. |
        | Využiji tzv. paušální výdaje pro OSVČ (např. 60 %). | Vymyslím si fiktivní faktury za věci, co jsem nekoupil. |
        | Vedu si přesnou evidenci a uchovávám všechny doklady. | Nevystavím účtenku, ačkoliv jsem peníze dostal. |
        | Zjistím si pravidla PŘED tím, než začnu podnikat. | Spoléhám na to, že *"se na to nepřijde"*. |
        """)

        st.markdown("<div class='box-purple'>🕵️ <b>Mini aktivita: Daňový detektiv</b></div>", unsafe_allow_html=True)
        st.write("Tvoji spolužáci se dostali do zajímavých finančních situací a neví, co mají dělat. Vyber jednu z nich a napiš, jaké 3 věci si musí daný člověk urychleně ověřit a co se stane, když se na to vykašle.")
        
        with st.form("detektiv_form"):
            situace = st.selectbox("Vyber situaci, kterou chceš jako detektiv řešit:", [
                "1. Spolužačka dostala novou kosmetiku zdarma (barter) výměnou za sérii reels na Instagramu.",
                "2. Spolužák před dvěma lety koupil Bitcoin, ten vyrostl o 200 %, a on ho teď celý prodal a peníze si poslal na bankovní účet.",
                "3. Kamarádka má o víkendu první brigádu na letním hudebním festivalu na DPP (Dohodu o provedení práce).",
                "4. Známý neustále nakupuje zlevněné boty ve výprodejích a následně je se ziskem masivně přeprodává na Vinted."
            ])
            detektiv_reseni = st.text_area("Tvé rady jako detektiva (co si ověřit a jaká hrozí rizika):")
            if st.form_submit_button("Odeslat tvé doporučení"):
                st.success("Skvělá práce! Každá z těchto situací skrývá daňovou past, pokud si lidé myslí, že 'internetové peníze se nedaní'. Odesláno do třídní diskuze.")

        st.markdown("""
        <div class='box-green'>
            ✅ <b>Co si zapamatovat z celého bloku Daně a státní rozpočet:</b><br>
            Daně nejsou jen "kolik mi stát sebere peněz z výplaty". Jsou to pravidla, která financují naši solidaritu, záchranku, školy a dálnice. Regulují to, kolik pijeme alkoholu a kolik vypouštíme smogu. Dobrý občan nemusí být certifikovaný daňový poradce. Měl by ale ovládat základy: chápat rozdíl mezi hrubou a čistou mzdou z brigády, vědět, že podepsat Růžový papír mu zachrání peníze, a rozumět tomu, proč práce 'na ruku' a nelegální prodeje na internetu ničí jeho vlastní důchodovou budoucnost i celou společnost.
        </div>
        """, unsafe_allow_html=True)
# =========================================================================
    # SEKCE 3: MOJE DANĚ V PRAXI
    # =========================================================================
    elif selected_section_5 == "3. Moje daně v praxi" or "3." in selected_section_5:
        st.markdown("### 3. Moje daně v praxi")
        
        st.markdown("""
        <div class='box-blue'>
            💻 <b>Praktický přesah:</b> Daňový portál, datová schránka, elektronická identita a Portál občana ukazují, že ekonomika není jen teorie. Moderní občan potřebuje rozumět tomu, kde hledat informace, jak ověřovat povinnosti a proč je digitální komunikace se státem zásadní součástí finanční gramotnosti.
        </div>
        """, unsafe_allow_html=True)

        st.divider()
        st.markdown("#### 3.1 Digitální stát (eGovernment): Konec front na úřadech")
        st.write("Generace před tebou musely kvůli každému papíru stát hodiny na úřadě. Dnes už máš státní úřady doslova ve svém mobilu. Stačí k tomu klíč, kterému se říká **Elektronická identita** (nejčastěji tvá bankovní identita – BankID).")

        col_eg1, col_eg2 = st.columns(2)
        with col_eg1:
            st.success("📱 **Identita občana (např. BankID)**\nFunguje jako tvá digitální občanka. Tvá banka státu zaručí, že u klávesnice sedíš opravdu ty. Přihlásíš se s ní do všech státních portálů stejně jednoduše jako do internetového bankovnictví.")
            st.info("📬 **Datová schránka**\nTvůj oficiální, státem garantovaný e-mail. Když pošleš zprávu úřadu přes 'datovku', má to stejnou právní váhu, jako bys to poslal/a doporučeně poštou s podpisem.")
        with col_eg2:
            st.warning("🏛️ **Portál občana**\nTvé hlavní digitální velitelství. Zjistíš tu, kdy ti propadne pas, kolik máš bodů na řidičáku, získáš výpis z rejstříku trestů nebo založíš živnost.")
            st.error("🧾 **Portál MOJE daně**\nOnline finanční úřad. Zde si můžeš vyplnit a jedním kliknutím odeslat daňové přiznání. Systém za tebe spoustu věcí sám spočítá a zkontroluje chyby.")

        st.markdown("##### 🔗 Tvé digitální záložky (Kde to najdeš v realitě):")
        st.markdown("""
        * 🔑 [Identita občana (identitaobcana.cz)](https://www.identitaobcana.cz/)
        * ✉️ [Moje datová schránka (mojedatovaschranka.cz)](https://www.mojedatovaschranka.cz/)
        * 🏢 [Portál občana (obcan.portal.gov.cz)](https://obcan.portal.gov.cz/)
        * 💰 [Portál MOJE daně (mojedane.cz)](https://www.mojedane.cz/)
        """)

        st.markdown("<div class='box-purple'>🕹️ <b>Kvíz: Jaký portál na to použiješ?</b></div>", unsafe_allow_html=True)
        st.write("Otestuj se, jestli bys v dnešním digitálním státě přežil/a bez návštěvy úřadu.")
        
        q_egov = st.radio("Jsi na dovolené v zahraničí a potřebuješ nutně zjistit, jestli nemáš v ČR nezaplacenou pokutu za rychlost, kvůli které ti hrozí exekuce. Kam se přihlásíš?", [
            "Vyber odpověď...",
            "A) Přihlásím se do své e-mailové schránky na Seznamu/Gmailu.",
            "B) Přihlásím se na Portál občana pomocí své Bankovní identity.",
            "C) Přihlásím se na portál MOJE daně."
        ])
        if "B)" in q_egov:
            st.success("✅ Správně! Portál občana je místo, kde máš přehled o svých přestupcích, dokladech a komunikaci se státem.")
        elif "A)" in q_egov or "C)" in q_egov:
            st.error("❌ Kdepak. Běžný e-mail není oficiální státní kanál a Portál MOJE daně řeší čistě finance a daňová přiznání. Správná odpověď je B (Portál občana).")

        st.divider()
        st.markdown("#### 3.2 Trenažér: „Tohle přece danit nemusím!“")
        st.write("Tohle je slavná poslední věta mnoha mladých lidí předtím, než jim přijde dopis z finančního úřadu. Podnikání a zdanitelné příjmy totiž už dávno nejsou jen o tom, že máš kamenný obchod.")
        
        st.markdown("""
        <div class='box-yellow'>
            🧩 <b>Mini úkol: Daňový průzkumník</b><br>
            Vyber si jednu ze situací níže. Tvým úkolem je zamyslet se a vypsat, <b>jaké kontrolní otázky by sis musel/a zodpovědět a ověřit v zákonech</b>, než bys s klidným svědomím prohlásil/a: <i>„Z tohto příjmu neplatím státu ani korunu.“</i>
        </div>
        """, unsafe_allow_html=True)

        with st.form("form_dane_praxe"):
            situace_praxe = st.selectbox("Vyber si svou životní situaci:", [
                "👗 1. Prodej oblečení na Vinted",
                "🎥 2. Příjmy z YouTube / TikToku (Reklamy a dary)",
                "🏠 3. Pronájem pokoje turistům přes Airbnb",
                "🪙 4. Zisk z prodeje kryptoměn (Bitcoin)",
                "📚 5. Pravidelné doučování angličtiny za hotové",
                "🍔 6. Nárazová brigáda (Dohoda o provedení práce)"
            ])
            
            otazky_student = st.text_area("Napiš 2-3 klíčové otázky, které si podle tebe musíš zjistit (např. Jde o jednorázový příjem?):")
            
            submit_praxe = st.form_submit_button("Ověřit mé otázky s Daňovým poradcem (AI)")
            
            if submit_praxe:
                st.write("---")
                st.markdown(f"**Tvá zvolená situace:** {situace_praxe}")
                st.markdown("👨‍💼 **Komentář daňového experta. Tyto otázky sis měl/a položit:**")
                
                if "Vinted" in situace_praxe:
                    st.success("1. **Soustavnost:** Prodávám jen své staré obnošené věci (osvobozeno), nebo soustavně nakupuji věci v sekáči, abych je s přirážkou prodal (podnikání)?\n2. **Záměr zisku:** Dělám to za účelem zisku?\n3. **Limit příležitostného příjmu:** Nepřesáhl jsem roční limit pro příležitostné příjmy (aktuálně 30 000 Kč)?")
                elif "YouTube" in situace_praxe:
                    st.success("1. **Pravidelnost:** Je tvorba obsahu mým pravidelným zdrojem příjmů?\n2. **Živnost:** Mám zřízené živnostenské oprávnění (IČO)?\n3. **Barter:** Uvědomuji si, že produkty 'zdarma' za recenzi (mobil, oblečení) jsou nepeněžní příjem, který se musí zdanit?")
                elif "Airbnb" in situace_praxe:
                    st.success("1. **Služby vs. Nájem:** Poskytuji jen holý nájem, nebo i služby (úklid, snídaně, povlečení)? Pokud služby, jde o ubytovací službu (podnikání).\n2. **Místní poplatky:** Odvádím obci rekreační/ubytovací poplatek za každého hosta?\n3. **DPH:** Nezačal/a jsem poskytováním služeb do zahraničí (platformě Airbnb) splňovat podmínky pro registraci k DPH (tzv. identifikovaná osoba)?")
                elif "kryptoměn" in situace_praxe:
                    st.success("1. **Kryptoměna jako majetek:** Vím o tom, že krypto se v ČR nedaní jako akcie, ale jako nehmotný majetek?\n2. **Časový test:** Jsem si vědom/a, že na krypto NEPLATÍ tříletý časový test pro osvobození daně jako u akcií?\n3. **Směna:** Vím, že se daní nejen prodej za koruny, ale i to, když za Bitcoin nakoupím Ethereum nebo si za krypto koupím auto?")
                elif "doučování" in situace_praxe:
                    st.success("1. **Soustavnost:** Doučuji někoho jednorázově před maturitou (příležitostný příjem do 30 000 Kč ročně), nebo učím každý týden (soustavná činnost = nutnost živnosti)?\n2. **Evidence:** Vedu si evidenci, kolik peněz jsem reálně převzal/a, abych případně doložil/a, že jsem pod limitem?")
                elif "brigáda" in situace_praxe:
                    st.success("1. **Limit odvodů:** Mám hrubý výdělek do 10 000 Kč měsíčně (DPP), abych neplatil/a sociální a zdravotní pojištění?\n2. **Růžový papír:** Mám podepsané Prohlášení poplatníka (slevu na dani), a nemám ho podepsané u dvou zaměstnavatelů zároveň?\n3. **Vrácení daně:** Vím o tom, že si na jaře mohu podat Daňové přiznání a stát mi sraženou daň pravděpodobně vrátí?")

        st.markdown("""
        <div class='box-green'>
            ✅ <b>Co si zapamatovat z tohoto bloku:</b><br>
            Moderní stát s tebou mluví digitálně. Mít datovou schránku a BankID znamená ušetřit dny života strávené na úřadech. A hlavně: Danit nemusíš jen to, co ti stát v zákoně <b>výslovně osvobodí</b>. Aplikace a internetové platformy sice usnadňují výdělek, ale <b>nezbavují tě odpovědnosti znát zákony</b>. Ignorance ("já myslel, že z TikToku se daně neplatí") před finančním úřadem nikdy neobstojí.
        </div>
        """, unsafe_allow_html=True)
# =========================================================================
    # SEKCE 4: GLOBÁLNÍ SOUVISLOSTI A SVĚT BEZ HRANIC
    # =========================================================================
    elif selected_section_5 == "4. Globální souvislosti a svět bez hranic" or "4." in selected_section_5:
        st.markdown("### 4. Globální souvislosti a svět bez hranic")
        
        st.markdown("""
        <div class='box-blue'>
            🌐 <b>Moderní hook:</b> Tričko z Temu, mobil navržený v USA, čip z Tchaj-wanu, baterie z Číny, kompletace ve Vietnamu, doprava přes Suez a prodej v Česku. Globalizace znamená, že věci, které denně používáš, nevznikají „v jedné zemi“, ale ve složité síti firem, států, dopravních cest a datových kabelů.
        </div>
        """, unsafe_allow_html=True)

        st.divider()
        st.markdown("#### 4.1 Globalizace a mezinárodní obchod: Jak se svět propojil")
        st.write("Globalizace je neustále rostoucí propojení ekonomik, firem, technologií a lidí napříč státy. Ekonomika jedné země je dnes absolutně závislá na tom, co se děje na druhém konci planety (což jsme viděli, když jedna zaseknutá loď v Suezském průplavu zastavila výrobu aut v Evropě).")

        st.markdown("##### 🤝 Proč státy vůbec obchodují?")
        st.write("Není efektivní, aby si každý stát vyráběl úplně všechno sám (od banánů přes auta až po mikročipy). Mezinárodní obchod je jako obří **týmová práce**. Státy se specializují podle toho, jaké mají suroviny, klima, technologie a vzdělanost lidí.")

        tab_teorie1, tab_teorie2, tab_teorie3 = st.tabs(["🌍 Mezinárodní dělba práce", "🥇 Absolutní výhoda", "🧠 Komparativní výhoda"])
        
        with tab_teorie1:
            st.markdown("##### Mezinárodní dělba práce")
            st.write("Země a firmy se specializují na různé části výrobního řetězce.")
            st.success("📱 **Příklad (iPhone):** Design a software vzniká v USA (vysoká přidaná hodnota), špičkové čipy na Tchaj-wanu (technologický monopol), fotoaparáty v Japonsku a celá kompletace probíhá z důvodu levné a masové pracovní síly v Číně nebo Indii.")
            
        with tab_teorie2:
            st.markdown("##### Absolutní výhoda")
            st.write("Jeden stát dokáže vyrábět produkt **levněji nebo efektivněji** než ostatní (např. díky přírodě).")
            st.success("🍌 **Příklad:** Kolumbie má absolutní výhodu v pěstování banánů oproti Norsku. Norsko má zase absolutní výhodu v těžbě ropy a chytání lososů. Nemá smysl, aby Norsko stavělo vyhřívané skleníky na banány – raději prodá lososy a banány si koupí.")
            
        with tab_teorie3:
            st.markdown("##### Komparativní výhoda (Trochu složitější, ale geniální)")
            st.write("Vyplatí se specializovat na to, v čem jsi **relativně nejlepší (kde máš nejnižší náklady obětované příležitosti)**, i když bys teoreticky zvládl/a skvěle i jiné věci.")
            st.info("Pochopit komparativní výhodu je klíč k tomu, proč bohaté státy přenechávají výrobu jednoduchých věcí chudším státům, i když by si je uměly vyrobit samy.")

        # Interaktivní vysvětlení komparativní výhody
        st.markdown("<div class='box-yellow'>👩‍⚖️ <b>Mini kvíz: Pochop komparativní výhodu na příkladu advokátky</b></div>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("Představ si, že jsi **nejlepší a nejdražší advokátka ve městě** (tvůj čas stojí 3 000 Kč/hod). Zároveň jsi ale dřív pracovala jako asistentka a **píšeš na klávesnici 2x rychleji než jakákoliv asistentka**, kterou by sis mohla najmout (za 300 Kč/hod).")
            
            kviz_advokatka = st.radio("Máš před sebou hodiny přepisování nudných smluv. Co uděláš?", [
                "Vyber řešení...",
                "A) Přepíšu si to sama. Jsem přece 2x rychlejší než asistentka, ušetřím tak čas i peníze za její plat.",
                "B) Najmu si asistentku. I když je pomalejší, můj ušetřený čas věnuji právní analýze, za kterou mi klienti platí."
            ])
            
            if "B)" in kviz_advokatka:
                st.success("✅ **Přesně tak! Objevila jsi komparativní výhodu.** Ačkoliv máš absolutní výhodu v psaní všemi deseti (jsi nejrychlejší), tvá komparativní výhoda je v právu. Pokud bys sama hodinu psala, 'ušetříš' sice 300 Kč za asistentku, ale **přijdeš o 3 000 Kč**, které jsi mohla vydělat jako advokátka. Přesně proto bohaté státy s inženýry (USA, Německo) přenechávají šití triček asijským zemím – jejich 'asistentkám' – i když by ta trička uměly ušít také.")
            elif "A)" in kviz_advokatka:
                st.error("❌ Zkus to promyslet jako ekonom. Sice jsi ušetřila 300 Kč za asistentku, ale zabila jsi hodinu času, během které ti mohl klient zaplatit 3 000 Kč za právní radu. Prodělala jsi 2 700 Kč! Správná odpověď je B.")

        st.divider()
        st.markdown("#### 4.1.1 Temný stín globalizace: Proč je tričko levnější než jízdenka?")
        st.write("Rychlá móda (Fast fashion) a e-shopy z Asie (Shein, Temu, AliExpress) chrlí extrémně levné zboží. Nízká cena je kombinací masové výroby, levné práce, dotované dopravy, ale často i **skrytých nákladů**.")

        st.markdown("<div class='box-purple'>👕 <b>Pitevna ceny: Co kupuješ za 100 Kč?</b></div>", unsafe_allow_html=True)
        st.write("Nasimuluj si rozpad ceny levného trička objednaného z asijského tržiště.")
        
        cena_tricka = st.slider("Cena trička v e-shopu (Kč):", 50, 500, 100, step=10)
        
        ukaz_skryte = st.toggle("👁️ Zobrazit i neviditelnou daň (Externality a skryté náklady pro planetu)")
        
        # Orientacni rozpad levneho e-commerce textilu (v procentech)
        naklad_material = int(cena_tricka * 0.15)
        naklad_prace = int(cena_tricka * 0.05) # Často jen zlomky procent, max jednotky
        naklad_doprava = int(cena_tricka * 0.10)
        naklad_marketing = int(cena_tricka * 0.40) # Platformy a reklamy sypou obrovské peníze do algoritmů
        zisk_firmy = int(cena_tricka * 0.30)
        
        fig_tricko = go.Figure(data=[go.Pie(
            labels=['Materiál', 'Mzda dělníka', 'Doprava a logistika', 'Marketing a platforma', 'Zisk značky'],
            values=[naklad_material, naklad_prace, naklad_doprava, naklad_marketing, zisk_firmy],
            hole=.4,
            marker_colors=['#94a3b8', '#ef4444', '#f59e0b', '#8b5cf6', '#10b981']
        )])
        fig_tricko.update_layout(margin=dict(t=10, b=10, l=10, r=10), height=300)
        
        col_t1, col_t2 = st.columns([1, 1])
        with col_t1:
            st.plotly_chart(fig_tricko, use_container_width=True)
        with col_t2:
            st.write(f"**Rozpad ceny {cena_tricka} Kč na účtence:**")
            st.markdown(f"🧵 Materiál: **{naklad_material} Kč**")
            st.markdown(f"🧑‍🏭 Mzda švadleny: **{naklad_prace} Kč** *(ano, takto málo)*")
            st.markdown(f"🚢 Doprava k tobě: **{naklad_doprava} Kč**")
            st.markdown(f"📱 Reklama (TikTok/Insta): **{naklad_marketing} Kč**")
            st.markdown(f"💰 Zisk korporace: **{zisk_firmy} Kč**")
            
        if ukaz_skryte:
            st.markdown("""
            <div style='background-color: #1f2937; color: #f9fafb; padding: 20px; border-radius: 8px; margin-top: 20px;'>
                <h4 style='color: #ef4444; margin-top:0;'>☠️ Neviditelná daň (Externality)</h4>
                <p>Nízká cena na účtence neznamená, že je produkt levný. Znamená to jen, že <b>zbytek ceny zaplatil někdo jiný</b>. Zde je reálná daň, kterou za tvé tričko platí celá planeta:</p>
                <ul>
                    <li><b>💧 Toxická voda:</b> Rychlá móda odpovídá za 20 % znečištění průmyslových vod na světě (barviva vypouštěná do řek v Asii).</li>
                    <li><b>🌍 Uhlíková stopa:</b> Letecká doprava levných balíčků po jednom kusu přímo k zákazníkům generuje extrémní emise.</li>
                    <li><b>🗑️ Hory odpadu:</b> Levné tričko vydrží pár vyprání. Končí na obřích skládkách textilu v Africe nebo Jižní Americe. Oblečení z polyesteru se bude rozkládat 200 let.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
# =====================================================================
        # PODKAPITOLA 4.2: VOLNÝ OBCHOD A PROTEKCIONISMUS
        # =====================================================================

        st.divider()
        st.markdown("#### 4.2 Volný obchod, protekcionismus a obchodní bariéry")
        st.write("Každý stát řeší dilema: Máme naše hranice úplně otevřít všemu zboží ze světa, nebo máme chránit naše vlastní firmy a továrny před levnou cizí konkurencí?")

        col_obchod1, col_obchod2 = st.columns(2)
        with col_obchod1:
            st.markdown("""
            <div style="background-color: #f0fdf4; padding: 15px; border-left: 5px solid #10b981; height: 100%;">
                <h5 style="margin-top: 0; color: #047857;">🕊️ Volný obchod</h5>
                <b>Co znamená:</b> Stát neklade obchodu překážky. Zboží a služby volně překračují hranice.<br><br>
                <b>Výhody pro nás:</b> Levnější zboží, obrovský výběr v obchodech, tlak na kvalitu a inovace firem.<br><br>
                <b>Rizika:</b> Extrémní závislost na cizích zemích (co když přestanou dodávat?), ztráta pracovních míst v domácích továrnách, které nezvládnou cenově konkurovat Asii.
            </div>
            """, unsafe_allow_html=True)
            
        with col_obchod2:
            st.markdown("""
            <div style="background-color: #fef2f2; padding: 15px; border-left: 5px solid #ef4444; height: 100%;">
                <h5 style="margin-top: 0; color: #b91c1c;">🛡️ Protekcionismus</h5>
                <b>Co znamená:</b> Stát úmyslně chrání (ochranářství) domácí výrobce před zahraniční konkurencí.<br><br>
                <b>Výhody pro stát:</b> Záchrana domácích pracovních míst a klíčového průmyslu (např. chceme mít vlastní potraviny a léky pro případ krize).<br><br>
                <b>Rizika pro nás:</b> Zboží v obchodech zákazníkům brutálně zdraží, je menší výběr. Navíc hrozí "obchodní válka" (cizí státy nám na oplátku zablokují náš vývoz).
            </div>
            """, unsafe_allow_html=True)

        st.markdown("##### 🧱 Zbraně protekcionismu: Obchodní bariéry")
        st.write("Když chce stát omezit dovoz, nevyhlásí hned opravdovou válku. Použije tyto čtyři nástroje:")
        
        c_bar1, c_bar2, c_bar3, c_bar4 = st.columns(4)
        c_bar1.info("💰 **Clo**\nDaň (poplatek) na dovážené zboží. Uměle ho zdraží.")
        c_bar2.warning("🔢 **Kvóta**\nMnožstevní limit. *(Dovolíme k nám dovézt max 10 000 aut ročně).*")
        c_bar3.error("🛑 **Embargo**\nÚplný zákaz obchodu s danou zemí. *(Sankce)*")
        c_bar4.success("📐 **Technické normy**\nPravidla bezpečnosti či původu. *(Když nesplní testy, nesmí na trh).*")

        st.markdown("<div class='box-purple'>🚗 <b>Simulátor obchodní války: Cla na čínské elektromobily</b></div>", unsafe_allow_html=True)
        st.write("Čína masivně dotuje své továrny na auta. Díky tomu dokáže dovézt do Evropy skvělé elektroauto mnohem levněji, než ho vyrobí evropská Škodovka nebo Volkswagen. Evropská unie se bojí, že naše automobilky zkrachují, a proto zvažuje **cla**.")
        
        with st.container(border=True):
            st.write("**Nastav si roli šéfa Evropské komise a urči výši cla:**")
            clo_eu = st.slider("Výše cla na dovoz čínských aut (% z ceny):", 0, 50, 0, step=5)
            
            cena_cina_zaklad = 700000
            cena_cina_konecna = int(cena_cina_zaklad * (1 + (clo_eu / 100)))
            cena_eu_auto = 900000
            
            col_auto1, col_auto2 = st.columns(2)
            col_auto1.metric("Čínské auto (s tvým clem)", f"{cena_cina_konecna:,} Kč".replace(',', ' '))
            col_auto2.metric("Evropské auto (bez cla)", f"{cena_eu_auto:,} Kč".replace(',', ' '))
            
            if cena_cina_konecna < cena_eu_auto:
                st.error("📉 Čínské auto je stále levnější. Evropští občané sice kupují levná auta a jásají, ale domácí továrny (např. v Německu a ČR) začínají propouštět dělníky, protože jejich dražší auta nikdo nekupuje.")
            elif cena_cina_konecna == cena_eu_auto:
                st.warning("⚖️ Ceny se srovnaly. Evropské automobilky mají šanci přežít. Boj o zákazníka teď rozhodne design a kvalita.")
            else:
                st.success(f"🏭 Čínské auto je o {cena_cina_konecna - cena_eu_auto:,} Kč dražší! Ochránil/a jsi evropské továrny a pracovní místa. **ALE:** Běžní občané nadávají, protože jsi jim sebral šanci koupit si levné auto a donutil jsi je platit víc. To je přesně daň za protekcionismus!".replace(',', ' '))

        st.markdown("<div class='box-yellow'>🗣️ <b>Debatní aréna: Kdo má pravdu?</b></div>", unsafe_allow_html=True)
        with st.form("debata_protekce"):
            st.write("Debatní otázka: Má stát chránit domácí průmysl a továrny, i když tím svým vlastním zákazníkům úmyslně zdraží výrobky?")
            debata_odpoved = st.radio("Zvol si svůj postoj:", [
                "Zastávám Protekcionismus: Ochrana našich pracovních míst a klíčových firem je přednější. Navíc nemůžeme být plně závislí na Asii.",
                "Zastávám Volný obchod: Je to nespravedlivé vůči běžným lidem. Pokud naše firmy neumí vyrábět levně a kvalitně, stát by je neměl uměle dotovat penězi zákazníků."
            ])
            if st.form_submit_button("Odeslat do debaty"):
                st.info("Odesláno! Přesně na tomto dilematu se dnes štěpí politici po celém světě.")

        st.markdown("##### 📦 Kauza: Levné balíčky z Asie (Temu, Shein, AliExpress)")
        st.write("Další živý příklad protekcionismu vs. volného obchodu se týká drobných zásilek (oblečení, doplňky) z mimoevropských e-shopů. Dlouhou dobu platily výjimky, díky kterým se z malých a levných balíčků neplatilo clo (a někdy ani DPH).")
        st.write("To vytvořilo **nefér výhodu**: asijský e-shop mohl prodat věc levněji než ten český, který u nás musel odvádět všechny daně a dodržovat přísné bezpečnostní certifikáty. Státy a EU proto nyní tyto daňové a celní výjimky ruší, aby srovnaly podmínky pro domácí prodejce.")
# =====================================================================
        # PODKAPITOLA 4.3: GLOBÁLNÍ DODAVATELSKÉ ŘETĚZCE
        # =====================================================================

        st.divider()
        st.markdown("#### 4.3 Globální dodavatelské řetězce a zranitelnost ekonomiky")
        st.write("Moderní ekonomika nefunguje tak, že by jedna továrna nakoupila železo a vyrobila celé auto. Funguje v obří síti dodavatelů. Jeden složitější výrobek (mobil, auto) může během výroby projít přes desítky zemí.")

        st.markdown("##### ⏱️ Extrémní efektivita: Just-in-Time")
        st.write("Firmy dnes nechtějí platit za obrovské a drahé sklady. Místo toho používají systém **Just-in-Time (Právě včas)**. Díly (např. sedačky do auta) se nevyrábí do zásoby, ale dorazí kamionem do továrny přesně v tu minutu, kdy se mají namontovat do auta na lince.")

        col_jit1, col_jit2 = st.columns(2)
        with col_jit1:
            st.success("✅ **Výhody Just-in-Time:**\nNižší náklady (neplatíš sklady), obrovská rychlost, efektivita, levnější výrobek pro zákazníka.")
        with col_jit2:
            st.error("🚨 **Rizika Just-in-Time:**\nZtráta odolnosti. Továrna má zásoby dílů třeba jen na 12 hodin. Když se někde ve světě zasekne kamion, loď nebo továrna, do pár hodin stojí celý řetězec!")

        st.markdown("<div class='box-purple'>🚢 <b>Simulátor: Motýlí efekt a zaseknutý Suez</b></div>", unsafe_allow_html=True)
        st.write("Představ si, že jsi šéfem logistiky v české automobilce. Čekáš na klíčové mikročipy z Asie. Využíváš systém Just-in-Time (máš zásobu čipů na skladě přesně na 3 dny výroby). Najednou se v Suezském průplavu v Egyptě vzpříčí obří kontejnerová loď Ever Given a zablokuje celou dopravní tepnu.")

        with st.container(border=True):
            trasa = st.radio("Jak zareaguješ? Zvol náhradní trasu pro tvou loď s čipy:", [
                "A) Počkat, až Suezský průplav vybagrují a uvolní (Zpoždění cca 7 dní).",
                "B) Přikázat lodi, ať Suez objede celou cestou kolem afrického kontinentu - Mys Dobré naděje (Zpoždění cca 14 dní, masivní spálení paliva)."
            ])
            
            st.write("---")
            if "A)" in trasa:
                st.warning("⏳ **Výsledek: Továrna stojí!** Zásoby čipů ti došly po 3 dnech. Další 4 dny mají dělníci v české továrně nucenou dovolenou, auta se nevyrábí, ale platy musíš platit dál. Ztráty jdou do stovek milionů korun, ale ušetřil jsi za palivo lodi.")
            else:
                st.error("📉 **Výsledek: Extrémní zdražení!** Tvá loď pluje kolem celé Afriky. Zpoždění je obrovské (14 dní), takže česká továrna na skoro dva týdny úplně zastaví výrobu. Navíc lodní společnost spálila tisíce tun nafty navíc a zdražila ti dopravu kontejneru o 300 %. Tuto ztrátu budeš muset promítnout do konečné ceny auta pro zákazníky.")

        st.markdown("##### 🌍 4 hlavní rizika globalizace (Co všechno se může pokazit?)")
        st.write("Zde jsou reálné hrozby, které mohou globální řetězce roztrhat na kusy:")

        tab_riz1, tab_riz2, tab_riz3, tab_riz4 = st.tabs(["💻 Krize čipů", "🚢 Blokáda dopravy", "⚔️ Geopolitika a válka", "🔄 Deglobalizace (Reshoring)"])

        with tab_riz1:
            st.markdown("**Krize mikročipů**")
            st.write("Chybí čipy pro auta, mobily, herní konzole nebo průmyslové stroje (vyrábí se drtivou většinou jen na Tchaj-wanu).")
            st.info("🇨🇿 **Dopad na Česko:** Automobilový průmysl tvoří páteř české ekonomiky. Když nejsou čipy, Škodovka a její dodavatelé nemohou dokončit auta, odstavují je na letiště a lidé přicházejí o peníze.")
            
        with tab_riz2:
            st.markdown("**Blokáda dopravy**")
            st.write("Suezský průplav, Panamský průplav nebo Rudé moře (útoky pirátů). Zpoždění lodí a extrémně dražší lodní kontejnery.")
            st.info("🇨🇿 **Dopad na Česko:** Téměř všechna levná elektronika, oblečení a součástky do českých firem jedou přes tyto světové trasy. Výpadek znamená okamžité zdražení pro českého spotřebitele.")

        with tab_riz3:
            st.markdown("**Válka a geopolitické konflikty**")
            st.write("Válka přináší výpadky klíčových komodit (energií, plynu, ropy, potravin).")
            st.info("🇨🇿 **Dopad na Česko:** Růst cen plynu, elektřiny a hnojiv se okamžitě promítne do obrovské inflace. Pekárně zdraží plyn -> zdraží chleba. Firmám rostou náklady a lidem padá životní úroveň.")

        with tab_riz4:
            st.markdown("**Deglobalizace a Reshoring**")
            st.write("Firmy se poučily z krizí a zjistily, že být 100% závislý na Asii je nebezpečné. Začínají přesouvat výrobu zpět blíž k zákazníkům nebo do bezpečnějších spřátelených zemí (tomu se říká **Reshoring** nebo *Friendshoring*).")
            st.info("🇨🇿 **Dopad na Česko:** Na jednu stranu to může Evropě přinést nová pracovní místa (např. stavba továren na baterie či čipy v EU). Na druhou stranu – evropský dělník je mnohem dražší než asijský, takže produkty v obchodech budou ve výsledku dražší.")
# =====================================================================
        # PODKAPITOLA 4.4: EVROPSKÁ UNIE A JEDNOTNÝ TRH
        # =====================================================================

        st.divider()
        st.markdown("#### 4.4 Evropská unie a jednotný vnitřní trh: Náš domácí prostor")
        st.write("Česká republika není ekonomický ostrov. Přes 80 % všeho, co vyrobíme, vyvážíme do zemí Evropské unie. Jsme pevnou součástí jejího **jednotného vnitřního trhu**, který funguje jako jeden obří stát bez hranic a patří mezi největší a nejbohatší obchodní prostory na světě.")

        st.markdown("<div class='box-blue'>🇪🇺 <b>Kouzlo čtyř svobod EU</b><br>Jednotný trh nestojí na slibech, ale na čtyřech základních pilířích, které nám absolutně změnily život:</div>", unsafe_allow_html=True)

        col_sv1, col_sv2, col_sv3, col_sv4 = st.columns(4)
        col_sv1.success("📦 **1. Zboží**\nŽádná cla, žádné čekání kamionů na hranicích. Firma pošle balík z Brna do Paříže stejně snadno jako do Prahy.")
        col_sv2.info("🚶 **2. Osoby**\nMůžeš se sebrat a jít žít, studovat nebo pracovat do Finska či Španělska, aniž bys potřeboval/a složitá víza.")
        col_sv3.warning("🛠️ **3. Služby**\nČeský architekt nebo programátor může legálně nabízet své služby klientům v Německu bez byrokratických překážek.")
        col_sv4.error("💸 **4. Kapitál**\nPeníze a investice mohou volně protékat celou Evropou. Můžeš si bez problému koupit akcie francouzské firmy.")

        st.markdown("##### 🎒 Co znamená EU v praxi pro tvou generaci (Gen Z)?")
        tab_eu1, tab_eu2, tab_eu3 = st.tabs(["✈️ Studium a práce", "📱 Roaming", "🛡️ Ochrana a Brussels Effect"])

        with tab_eu1:
            st.write("**Erasmus+ a práce v zahraničí**")
            st.write("Díky EU můžeš během střední nebo vysoké školy vyjet na placený studijní pobyt do zahraničí (Erasmus+), kde získáš kontakty a jazyk. Následně můžeš kdekoliv v EU legálně pracovat za stejných podmínek jako místní občané.")
        
        with tab_eu2:
            st.write("**Roaming jako doma**")
            st.write("Ještě nedávno znamenalo přehrát si video na dovolené v Itálii účet za telefon v tisících korun. Dnes díky regulaci EU voláš a datuješ všude v Unii za stejné ceny jako doma v ČR.")
            
        with tab_eu3:
            st.write("**Ochrana spotřebitele a tzv. Brussels Effect (Bruselský efekt)**")
            st.write("EU je tak obrovský a bohatý trh, že když zdejší politici schválí nějaké pravidlo (např. *'Všechny mobily musí mít nabíječku USB-C'*, nebo pravidla ochrany dat *GDPR*), globálním gigantům jako Apple nebo Google se nevyplatí vyrábět dvě verze iPhonu. Raději zavedou USB-C pro celý svět. Tomu se říká **Brussels Effect** – EU diktuje globální pravidla hry.")

        st.markdown("<div class='box-purple'>⚖️ <b>Debatní aréna: Velký evropský regulátor</b></div>", unsafe_allow_html=True)
        with st.form("debata_eu_regulace"):
            st.write("EU velmi tvrdě reguluje trh: nařídila USB-C, chrání tvá osobní data (GDPR), nařizuje limity emisí, reguluje umělou inteligenci (AI Act). Někdo to chválí, jiný kritizuje.")
            postoj_eu = st.radio("Zvol si svůj postoj k evropské regulaci:", [
                "🛡️ EU je náš štít: Chrání běžné spotřebitele před zvůlí obřích korporací, kterým jde jen o zisk. Bez EU by si s námi firmy dělaly, co chtějí.",
                "⚓ EU je kotva inovací: Přehnaná byrokracie a neustálé zákazy dusí evropské firmy. Proto nám technologicky utíkají USA a Asie, my totiž místo vývoje vymýšlíme směrnice."
            ])
            if st.form_submit_button("Hlasovat o roli EU"):
                st.info("Tvůj hlas byl zaznamenán! Na tomto dilematu se dnes naprosto reálně štěpí evropská politická scéna.")

        st.divider()
        st.markdown("#### 4.4.1 Mělo by Česko přijmout Euro?")
        st.write("Tohle je jedno z nejcitlivějších politických témat u nás. Zatímco firmy obvykle prosí vládu, aby Euro co nejdříve zavedla, velká část běžných občanů se ho bojí a chce si nechat Korunu.")

        # Simulátor kurzového rizika
        st.markdown("##### 📉 Simulátor kurzového rizika: Proč firmy chtějí Euro?")
        st.write("Představ si, že jsi česká firma. Podepsal/a jsi smlouvu s Německem, že jim za měsíc dodáš stroje za **100 000 Eur**. Tvé náklady na platy dělníků a materiál v ČR jsou přesně **2 400 000 Kč**. Smlouvu jsi podepsal/a v době, kdy byl kurz 25 Kč za Euro. Co se stane za měsíc, až ti Němci pošlou Eura a ty si je směníš na Koruny?")
        
        kurz_eur = st.slider("Zahýbej kurzem! Jaký bude kurz za měsíc, až přijdou Eura?", 22.0, 28.0, 25.0, step=0.5)
        
        prijem_v_kc = 100000 * kurz_eur
        zisk_firmy = prijem_v_kc - 2400000
        
        col_kurz1, col_kurz2 = st.columns(2)
        col_kurz1.metric("Tvůj příjem v Kč", f"{int(prijem_v_kc):,} Kč".replace(',', ' '))
        
        with col_kurz2:
            if zisk_firmy > 0:
                st.metric("Zisk tvé firmy", f"{int(zisk_firmy):,} Kč".replace(',', ' '))
                st.success("Vydělal/a jsi! Koruna oslabila a tobě to nečekaně přineslo zisk navíc.")
            elif zisk_firmy == 0:
                st.metric("Zisk tvé firmy", "0 Kč")
                st.warning("Jsi na nule. Vše, co jsi vydělal/a, padlo na zaplacení dělníků.")
            else:
                st.metric("Zisk tvé firmy", f"{int(zisk_firmy):,} Kč".replace(',', ' '), delta_color="inverse")
                st.error(f"Katastrofa! Koruna posílila a ty jsi kvůli kurzu ve ztrátě. Prodělal/a jsi a nemáš na platy. **A přesně kvůli tomuto neustálému stresu a nejistotě české firmy chtějí Euro!**")

        st.markdown("##### 🪙 Argumenty: Česká koruna vs. Euro")
        col_euro_pro, col_euro_proti = st.columns(2)
        with col_euro_pro:
            st.success("**👍 Argumenty PRO přijetí Eura**")
            st.markdown("""
            * **Žádné měnové riziko:** Firmy budou vědět, na čem jsou. Nezkrachují kvůli výkyvu kurzu.
            * **Úspory za poplatky:** Odpadnou miliardové poplatky bankám za směnu peněz při exportu i dovolených.
            * **Pevnější začlenění:** Byli bychom u hlavního stolu, kde se rozhoduje o ekonomice Evropy (dnes tam nejsme).
            """)
            
        with col_euro_proti:
            st.error("**👎 Argumenty PROTI přijetí Eura**")
            st.markdown("""
            * **Ztráta nezávislosti:** Ztratili bychom Českou národní banku (ČNB). Úrokové sazby by nám určovali ve Frankfurtu, což nemusí naší ekonomice vždy vyhovovat.
            * **Strach ze zdražování:** Lidé se bojí psychologického efektu zaokrouhlování cen směrem nahoru, když se přejde na novou měnu.
            * **Ručení za ostatní:** Stali bychom se součástí měny, kde jsou i zadlužené státy (např. Řecko, Itálie).
            """)

        with st.form("form_euro_postoj"):
            st.write("**Tvůj osobní verdikt jako občana:**")
            euro_rozhodnuti = st.text_area("Napiš své stanovisko: „Euro bych v ČR přijal/a / nepřijal/a, protože...“")
            if st.form_submit_button("Uložit mé stanovisko"):
                st.success("Skvělé! Umět obhájit svůj postoj argumenty (a nejen emocemi) je klíč k dobré ekonomické debatě.")
