import math
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st


def render_dluhovy_simulator():
    st.markdown("#### ⏳ Živé počítadlo státního dluhu ČR")
    
    st.markdown(
        """
        <div class='box-purple'>
            <strong>🔎 Detektivní úkol: Najdi aktuální data!</strong><br>
            Než spustíš simulátor, otevři si web <b>Ministerstva financí (mfcr.cz)</b> nebo <b>Českého statistického úřadu (czso.cz)</b>. Najdi dva údaje:<br>
            1. Jaký je aktuální celkový státní dluh ČR?<br>
            2. Jaký je plánovaný schodek státního rozpočtu pro letošní rok?<br><br>
            Zadej tato čísla do políček níže. Teprve pak uvidíš reálný stav státní pokladny.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write(
        "⚠️ **Důležité upozornění:** V realitě státní dluh neroste takto plynule každou vteřinou. "
        "Roste **skokově** – například když Ministerstvo financí uspořádá aukci, vydá dluhopisy a půjčí si desítky miliard najednou. "
        "Tento simulátor ale matematicky rozpočítává schodek na vteřiny, abys měl/a představu, jaké obrovské tempo to v průměru je."
    )

    POPULACE_CR = 10_900_000
    EKONOMICKY_AKTIVNI = 5_400_000  # Lidé, kteří reálně platí daně ze mzdy

    col1, col2 = st.columns(2)
    with col1:
        statni_dluh_mld = st.number_input(
            "Aktuální státní dluh ČR (v mld. Kč):",
            value=3350,  
            step=50,
            help="Vyhledej aktuální údaj a přepiš ho."
        )
    with col2:
        aktualni_schodek_mld = st.number_input(
            "Letošní schodek rozpočtu (v mld. Kč):",
            value=250,   
            step=10,
            help="Vyhledej plánovaný schodek na letošní rok."
        )

    st.markdown("##### 🔮 Co přinese budoucnost? Vyber scénář vlády:")
    st.write("Schodek se každý rok mění. Zkus změnit vládní strategii a sleduj, jak se počítadlo dluhu zrychlí nebo zpomalí!")
    
    scenar = st.selectbox(
        "Jak bude hospodařit další vláda?",
        [
            "⚖️ Stávající tempo (Schodek zůstane stejný jako letos)",
            "✂️ Rozpočtová odpovědnost / Úspory (Schodek klesne o polovinu)",
            "💸 Expanzivní politika / Krize (Schodek stoupne o polovinu)",
            "✏️ Vlastní zadání (Zadám přesný schodek ručně)"
        ]
    )

    if "Stávající" in scenar:
        rocni_schodek = aktualni_schodek_mld
    elif "Úspory" in scenar:
        rocni_schodek = aktualni_schodek_mld / 2
    elif "Expanzivní" in scenar:
        rocni_schodek = aktualni_schodek_mld * 1.5
    else:
        rocni_schodek = st.number_input("Zadej vlastní roční schodek na další roky (v mld. Kč):", value=int(aktualni_schodek_mld), step=10)

    # Výpočty pro ŽIVÉ POČÍTADLO
    celkovy_dluh_kc = statni_dluh_mld * 1_000_000_000
    # Přepočet schodku na vteřiny (365 dní * 24 h * 60 min * 60 s = 31 536 000 vteřin)
    narust_za_vterinu = (rocni_schodek * 1_000_000_000) / 31_536_000

    # Dynamický HTML/JS widget
    ticker_html = f"""
    <div style="background-color: #fef2f2; padding: 20px; border-radius: 10px; text-align: center; border: 2px solid #ef4444; margin-bottom: 20px;">
        <h3 style="color: #b91c1c; margin-bottom: 5px; font-family: sans-serif;">Aktuální počítadlo státního dluhu</h3>
        <div id="live-debt" style="font-size: 2.8rem; font-weight: bold; color: #ef4444; font-family: monospace;">Načítám...</div>
        <div style="color: #b91c1c; font-size: 1rem; margin-top: 10px;">
            Při tomto scénáři dluh roste průměrnou rychlostí <b>{narust_za_vterinu:,.0f} Kč za vteřinu</b>.
        </div>
    </div>
    <script>
        let baseDebt = {celkovy_dluh_kc}; 
        let debtPerSecond = {narust_za_vterinu}; 
        let startDate = new Date().getTime();
        
        setInterval(function() {{
            let now = new Date().getTime();
            let secondsPassed = (now - startDate) / 1000;
            let currentDebt = baseDebt + (secondsPassed * debtPerSecond);
            let formattedDebt = Math.floor(currentDebt).toString().replace(/\\B(?=(\\d{{3}})+(?!\\d))/g, " ") + " Kč";
            document.getElementById('live-debt').innerHTML = formattedDebt;
        }}, 100);
    </script>
    """
    st.components.v1.html(ticker_html, height=180)

    # Dlouhodobá simulace v letech
    roky = st.slider("Simuluj vývoj dluhu za kolik let:", min_value=1, max_value=10, value=4)

    if roky == 1:
        text_roky = "1 rok"
    elif 2 <= roky <= 4:
        text_roky = f"{roky} roky"
    else:
        text_roky = f"{roky} let"

    budouci_dluh_mld = statni_dluh_mld + (rocni_schodek * roky)
    budouci_dluh_obcan = (budouci_dluh_mld * 1_000_000_000) / POPULACE_CR
    budouci_dluh_poplatnik = (budouci_dluh_mld * 1_000_000_000) / EKONOMICKY_AKTIVNI

    st.markdown(f"##### 📊 Výsledek za {text_roky} při schodku {rocni_schodek:,.0f} mld. Kč ročně:")
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Celkový budoucí dluh", f"{budouci_dluh_mld:,.0f} mld. Kč".replace(",", " "))
    c2.metric("Dluh na 1 občana", f"{budouci_dluh_obcan:,.0f} Kč".replace(",", " "))
    c3.metric("Dluh na pracujícího", f"{budouci_dluh_poplatnik:,.0f} Kč".replace(",", " "))

    st.info(
        f"💡 **Shrnutí:** Pokud bude stát hospodařit v tomto zvoleném režimu, naroste dluh za **{text_roky}** o **{rocni_schodek * roky:,.0f} mld. Kč**. "
        f"Na každého ekonomicky aktivního občana (toho, kdo reálně platí daně ze mzdy) tak v budoucnu připadne dluhová zátěž **{budouci_dluh_poplatnik:,.0f} Kč**."
    )


def render():
    # 📌 HLAVIČKA KAPITOLY
    st.markdown(
        "<span class='hero-badge'>Kapitola 5</span>", unsafe_allow_html=True
    )
    st.title("5. Stát, daně a globální souvislosti")
    st.markdown(
        "<p style='font-size: 1rem; color: #64748b; margin-bottom: 1.5rem;'>"
        "Stát není jen úřad, formulář nebo položka na výplatní pásce. Je to"
        " systém, který vybírá daně, financuje veřejné služby, nastavuje"
        " pravidla trhu a reaguje na problémy, které jednotlivci ani firmy sami"
        " nevyřeší — od infrastruktury přes digitální stát až po regulaci Big"
        " Tech, globální obchod a klimatickou odpovědnost.</p>",
        unsafe_allow_html=True,
    )

    with st.container(border=True):
        st.markdown(
            """
        <div class='box-blue'>
            <strong>🧠 Pointa kapitoly:</strong> Ekonomika státu není abstraktní tabulka. Promítá se do toho, kolik zaplatíš z brigády, proč je v ceně mobilu DPH, jak stát financuje školy a silnice, proč řeší daňové úniky, jak funguje eGovernment a proč levné zboží z druhého konce světa může mít skryté ekologické i sociální náklady.
        </div>
        """,
            unsafe_allow_html=True,
        )

    # 📌 PŘEHLED A NAVIGACE KAPITOLOU
    with st.expander(
        "🧭 Cíle kapitoly a logická cesta (Rozbalit)", expanded=False
    ):
        c_nav1, c_nav2 = st.columns(2)
        with c_nav1:
            st.markdown("""
            **🎯 Co máš po kapitole umět?**
            * vysvětlit funkce státu v ekonomice a důvody státních zásahů,
            * rozlišit veřejné statky, komerční služby a tržní selhání,
            * popsat základní princip státního rozpočtu, deficitu a veřejného dluhu,
            * rozlišit přímé a nepřímé daně na běžných příkladech,
            * vysvětlit, proč se daně týkají brigád, podnikání, tvorby obsahu, investic i kryptoměn,
            * orientovat se v základní logice digitální komunikace se státem,
            * popsat globalizaci, mezinárodní obchod a dodavatelské řetězce,
            * posoudit dopady levného zboží, fast fashion, e-commerce a dopravy na lidi i životní prostředí,
            * vysvětlit základní význam EU, jednotného trhu, Green Dealu, ESG a odpovědnosti firem,
            * diskutovat ekonomická dilemata bez jednoduchých odpovědí.
            """)
            st.markdown(
                """
            <div style="font-size: 0.85rem; color: #64748b; margin-top: 10px;">
                <i>📘 <b>Vazba na RVP:</b> Kapitola rozvíjí ekonomické, občanské a digitální kompetence v oblastech funkce státu v ekonomice, hospodářská politika, daňová soustava, státní rozpočet, veřejné finance, globalizace, mezinárodní obchod, Evropská unie, udržitelný rozvoj a odpovědné rozhodování.</i>
            </div>
            """,
                unsafe_allow_html=True,
            )

        with c_nav2:
            st.markdown("""
            **🧭 Logická cesta kapitolou:**
            1. 🏛️ **Stát jako hospodář** — nejdřív si ujasníš, proč stát v ekonomice vůbec existuje, co jsou veřejné statky, tržní selhání a proč pravidla trhu nejsou jen zbytečná byrokracie.
            2. 📊 **Daně a státní rozpočet** — potom přejdeš k tomu, odkud stát bere peníze, za co je utrácí, proč vzniká deficit a proč daně nejsou jen „trest za výdělek“.
            3. 💸 **Moje daně v praxi** — následně propojíš teorii s běžným životem: brigáda, Vinted, YouTube, TikTok, OnlyFans, Uber, Airbnb, investice, kryptoměny, DPH na nákupu a digitální komunikace se státem.
            4. 🌍 **Globální dodavatelské řetězce** — potom se podíváš na cestu výrobků: tričko z fast fashion, mobil s čipy z Asie, nákup z Temu nebo Shein a rizika závislosti na dopravě, energiích a geopolitice.
            5. 🌱 **ESG a udržitelná ekonomika** — nakonec propojíš ekonomiku s odpovědností: uhlíková stopa, Green Deal, sociální dopady, greenwashing a otázka, jak firmy vytvářejí hodnotu nejen finančně, ale i společensky.
            """)

    # 📌 JEDNOTNÁ NABÍDKA PODKAPITOL
    section_options_5 = [
        "1. Stát jako „hospodář“ — proč ho vůbec máme?",
        "2. Daně, státní rozpočet a ekonomická realita",
        "3. Moje daně v praxi",
        "4. Globální souvislosti a svět bez hranic",
        "5. ESG a udržitelná ekonomika",
        "6. Aktivity a případové studie na závěr",
    ]

    st.markdown(
        "📌 <strong>Přechod na podkapitolu:</strong>", unsafe_allow_html=True
    )
    selected_section_5 = st.selectbox(
        "Přechod na podkapitolu:",
        section_options_5,
        index=0,
        label_visibility="collapsed",
    )
    st.divider()

    # =========================================================================
    # SEKCE 1: STÁT JAKO HOSPODÁŘ
    # =========================================================================
    if selected_section_5.startswith("1."):
        st.markdown("### 1. Stát jako „hospodář“ — proč ho vůbec máme?")

        st.markdown(
            """
        <div class='box-blue'>
            🏛️ <b>Představ si stát jako „předplatné na fungující společnost“.</b><br>
            Netflix si platíš přímo, protože chceš seriály. Ale silnice, veřejné osvětlení, soudy, policii, školy, nemocnice, ochranu spotřebitele nebo obranu státu nejde rozumně platit po jednotlivých kliknutích jako Patreon. Proto existují daně, veřejné rozpočty a hospodářská politika.
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.divider()
        with st.expander(
            "📖 Slovníček cizích pojmů v kapitole (Rychlý tahák)",
            expanded=False,
        ):
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
        st.write(
            "Trh je silný nástroj. Umí propojit nabídku a poptávku, motivovat firmy ke zlepšování, "
            "tlačit na cenu a umožnit lidem svobodně se rozhodovat. Jenže trh není kouzelný algoritmus, "
            "který automaticky vyřeší všechno spravedlivě, bezpečně a dlouhodobě udržitelně. "
            "**Tržní selhání** znamená situaci, kdy samotný trh nevede k výsledku, který je pro společnost efektivní nebo přijatelný."
        )

        st.markdown(
            "<div class='box-blue'><strong>🧠 Jednoduše:</strong> Stát nezasahuje do ekonomiky proto, že by trh byl zbytečný. Zasahuje tam, kde trh sám vytváří problém, který dopadá na celou společnost.</div>",
            unsafe_allow_html=True
        )

        tab_selhani1, tab_selhani2, tab_selhani3 = st.tabs([
            "🛣️ Veřejné statky",
            "🏭 Externality",
            "👑 Monopol",
        ])

        with tab_selhani1:
            st.markdown("##### Veřejné statky (Proč si silnice a armádu neplatíme přes Kickstarter?)")
            st.write("Veřejné statky jsou statky nebo služby, u kterých obvykle platí dvě vlastnosti:")
            st.markdown("""
            * **Nevylučitelnost ze spotřeby:** je obtížné nebo nemožné vyloučit člověka z užívání, i když přímo nezaplatil. Nemůžete zakázat někomu, aby se v noci díval na světlo z pouliční lampy.
            * **Nerivalita ve spotřebě:** spotřeba jednoho člověka výrazně nesnižuje možnost spotřeby druhého.
            * **Příklady:** veřejné osvětlení, obrana státu, základní bezpečnost, některé silnice, protipovodňová ochrana.
            * **Problém černého pasažéra:** Kdyby se policie nebo dálnice platily čistě dobrovolně formou sbírky, spousta lidí by je využívala zdarma a systém by zkrachoval. Proto tyto věci platíme povinně z daní.
            """)

        with tab_selhani2:
            st.markdown("##### Externality (Proč levné tričko nemusí být opravdu levné?)")
            st.write("**Externalita** je vedlejší efekt výroby nebo spotřeby, který dopadá na někoho, kdo se přímo neúčastní tržní transakce.")
            st.markdown("""
            * 🔴 **Negativní externalita:** Firma něco vyrábí levně, ale část nákladů nese okolí. Moderní příklad: Fast fashion. Tričko může mít nízkou cenu na účtence, ale znečištěná řeka, toxický odpad z barvení látky nebo emise z kamionů dopadají na celou planetu.
            * 🟢 **Pozitivní externalita:** Vzdělání prospívá nejen jednotlivci, ale celé společnosti. Vzdělanější člověk vymyslí lék nebo novou technologii, ze které těží komunita. Proto stát podporuje školství a očkování.
            """)

        with tab_selhani3:
            st.markdown("##### Monopol a nedokonalá konkurence (Co kdyby byl v ČR jen jeden operátor?)")
            st.write("**Monopol** vzniká tehdy, když jeden podnik ovládá trh natolik, že může výrazně ovlivňovat cenu, podmínky nebo dostupnost služby. Problémem není velikost firmy sama o sobě, ale **zneužití tržní síly**.")
            st.markdown("""
            * **Rizika monopolu:** vyšší ceny, horší kvalita, menší tlak na inovace, slabší postavení zákazníka.
            * **Moderní příklady:** debaty o Big Tech firmách, uzavřených ekosystémech.
            * **Role státu a EU:** chránit hospodářskou soutěž, antimonopolní úřady (např. nařízení sjednotit nabíječky na USB-C, právo na jiný prohlížeč).
            """)

        st.markdown(
            "<div class='box-yellow'><strong>❓ Debata:</strong> Kde je hranice mezi užitečnou regulací a zbytečnou byrokracií? Má stát zasahovat do digitálních platforem, AI nástrojů, mobilních ekosystémů nebo pravidel e-shopů?</div>",
            unsafe_allow_html=True
        )

        st.divider()
        st.markdown("#### 1.2 Co přesně stát v ekonomice dělá: 4 funkce státu")
        st.write("Ekonomická role státu se dá shrnout do několika funkcí. Stát vytváří rámec a zasahuje tam, kde samotný trh nestačí.")

        st.markdown("""
        | Funkce státu | RVP vysvětlení | Moderní příklad |
        | :--- | :--- | :--- |
        | **Právní a institucionální rámec** | Stát zajišťuje pravidla hry: ochranu vlastnictví, smlouvy, vymahatelnost práva, ochranu spotřebitele. | Když si objednáš zboží online a přijde padělek nebo nic, existují pravidla reklamace a soudy. |
        | **Alokační funkce** | Stát směřuje zdroje tam, kde je trh sám neposkytuje v dostatečné míře (k veřejným statkům). | Školy, nemocnice, silnice, hasiči, veřejné osvětlení nebo protipovodňová opatření. |
        | **Redistribuční funkce** | Stát zmírňuje sociální nerovnosti pomocí daní, dávek, důchodů nebo veřejných služeb. | Debata, zda mají lidé s vyššími příjmy platit vyšší daně, aby stát mohl financovat obědy ve školách. |
        | **Stabilizační funkce** | Stát se snaží tlumit výkyvy ekonomiky, inflaci, nezaměstnanost a hluboké krize. | Podpora během pandemie (Kurzarbeit), pomoc při energetické krizi, snaha brzdit inflaci. |
        """)

        st.info("🧭 **Pravidla hry:** Bez vymahatelných pravidel by trh nefungoval dobře. Když nevíš, zda smlouva platí, zda můžeš reklamovat zboží, zda někdo chrání tvoje vlastnictví a zda firma může lhát v reklamě, ekonomika se mění v chaos.")
        st.warning("⚖️ **Redistribuce není jen „brát a dávat“:** Smyslem je řešit situace, kdy by příliš velké nerovnosti ohrožovaly soudržnost společnosti, přístup ke vzdělání nebo zdraví. Zároveň to otevírá debatu o motivaci pracovat.")

        with st.expander("Debatní otázka: Mají miliardáři platit vyšší daně?"):
            st.markdown("""
            **Má stát zvyšovat daně lidem s vysokými příjmy, pokud tím financuje služby pro lidi s nízkými příjmy?**
            * **Argumenty pro:** vyšší solidarita, menší nerovnosti, dostupnější vzdělání a zdravotní péče, stabilnější společnost.
            * **Argumenty proti:** riziko odchodu kapitálu, menší motivace investovat, složitější daňový systém.
            * **Výstup:** Napiš své stanovisko ve 4 větách: názor, ekonomický argument, sociální argument, možné riziko.
            """)

        st.divider()
        st.markdown("#### 1.3 Ukazatele výkonu ekonomiky a magický čtyřúhelník")
        st.write("Aby stát, vláda, ČNB, firmy i občané věděli, v jaké kondici ekonomika je, sledují se **makroekonomické ukazatele**. Nejde o čísla „pro ekonomy do tabulek“. Změna se projeví v cenách potravin, dostupnosti brigád, mzdách a hypotékách.")

        st.markdown("""
        **Základní ukazatele výkonu ekonomiky:**
        * **HDP** — hodnota statků a služeb vytvořených v ekonomice za určité období.
        * **Tempo růstu HDP** — ukazuje, zda ekonomika roste, stagnuje, nebo klesá.
        * **Míra inflace** — ukazuje, jak rychle roste cenová hladina.
        * **Míra nezaměstnanosti** — ukazuje, jaká část ekonomicky aktivních lidí nemá práci, ale práci hledá.
        * **Platební bilance** — ukazuje ekonomické vztahy se zahraničím, obchod a toky peněz.
        * **Reálná mzda** — ukazuje, zda mzdy rostou rychleji, nebo pomaleji než ceny.
        """)

        st.markdown(
            "<div class='box-green'><strong>🔗 Klikací zdroje aktuálních dat pro žáky:</strong><br>"
            "- <a href='https://csu.gov.cz/produkty/hmu_cr' target='_blank'>ČSÚ — Hlavní makroekonomické ukazatele</a><br>"
            "- <a href='https://csu.gov.cz/inflace-spotrebitelske-ceny' target='_blank'>ČSÚ — Inflace, spotřebitelské ceny</a><br>"
            "- <a href='https://www.cnb.cz/cs/statistika/inflace/' target='_blank'>ČNB — Inflace a měnová politika</a><br>"
            "- <a href='https://www.cnb.cz/cs/statistika/platebni_bilance_stat/' target='_blank'>ČNB — Statistiky platební bilance</a></div>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<div class='box-yellow'><strong>🧩 Úkol s reálnými daty:</strong> Otevři odkaz na ČSÚ — Hlavní makroekonomické ukazatele. Najdi poslední dostupný rok a opiš: růst HDP, průměrnou roční inflaci, míru nezaměstnanosti a saldo platební bilance. Potom napiš: „Podle těchto čísel ekonomika vypadá spíš stabilně / nestabilně, protože…“</div>",
            unsafe_allow_html=True
        )

        st.markdown("#### 1.3.1 Magický čtyřúhelník hospodářské politiky")
        st.write("Hospodářská politika sleduje několik cílů najednou. Je „magický“ proto, že všechny cíle nejdou dokonale splnit současně. Když se stát snaží rychle podpořit ekonomiku (sníží nezaměstnanost), může vyvolat zdražování (zvýší inflaci).")

        st.markdown("""
        | Vrchol čtyřúhelníku | Ukazatel | Co znamená | Otázka pro studenta | Riziko, když se nedaří |
        | :--- | :--- | :--- | :--- | :--- |
        | **Hospodářský růst** | HDP a tempo růstu HDP | Růst výkonu ekonomiky — kolik hodnoty ekonomika vytvoří. | Vyrábíme a poskytujeme více hodnoty než dřív? | Stagnace, méně investic, nižší životní úroveň. |
        | **Nízká nezaměstnanost** | Míra nezaměstnanosti | Co nejvíce lidí, kteří chtějí pracovat, má práci. | Mají lidé možnost vydělávat a zapojit se do ekonomiky? | Ztráta příjmů, sociální problémy, nižší spotřeba. |
        | **Cenová stabilita** | Míra inflace | Ceny nerostou příliš rychle a peníze si drží hodnotu. | Kolik stál kebab nebo lístek do kina před 5 lety a dnes? | Inflace znehodnocuje úspory a komplikuje plánování. |
        | **Vnější ekonomická rovnováha** | Platební bilance, běžný účet, obchodní bilance | Vyrovnané vztahy se zahraničím — dovoz, vývoz, služby. | Nejsme příliš závislí na dovozu nebo zahraničním financování? | Závislost na zahraničí, tlak na měnu, zranitelnost. |
        """)

        st.markdown(
            "<div class='box-yellow'><strong>🍦 Reality check: inflace jako neviditelný zloděj úspor</strong><br>Zeptej se doma nebo ve třídě: Kolik stál kopeček zmrzliny, kebab, lístek do kina nebo školní oběd před pěti lety? Kolik stojí dnes? Pokud ceny rostou rychleji než příjmy a úspory, člověk si za stejné peníze koupí méně.</div>",
            unsafe_allow_html=True
        )

        with st.expander("Proč nejde mít všechno najednou?"):
            st.write("Když stát výrazně zvyšuje výdaje nebo snižuje daně, může tím podpořit poptávku, firmy a zaměstnanost. Pokud je ale ekonomika už napnutá, může více peněz v oběhu tlačit na růst cen. Naopak přísná politika proti inflaci může zdražit úvěry, zpomalit investice a dočasně zvýšit nezaměstnanost. Příklad: Nižší úrokové sazby zlevní hypotéky, ale mohou urychlit inflaci.")

        st.divider()
        st.markdown(
            "<div class='box-purple'>🕹️ <b>Simulátor: Nakresli si stav ekonomiky</b></div>",
            unsafe_allow_html=True,
        )
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

        kategorie = ["Růst HDP (%)", "Nezaměstnanost (%)", "Inflace (%)", "Platební bilance (%)"]

        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(r=[hdp1, nez1, inf1, bil1], theta=kategorie, fill="toself", name="Období 1", line_color="#10b981"))
        fig.add_trace(go.Scatterpolar(r=[hdp2, nez2, inf2, bil2], theta=kategorie, fill="toself", name="Období 2", line_color="#ef4444"))
        fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[-10, 25])), showlegend=True, margin=dict(l=40, r=40, t=40, b=40))

        st.plotly_chart(fig, use_container_width=True)

        st.divider()
        st.markdown("#### 1.4 Nástroje státu: hospodářská politika")
        st.write("Hospodářská politika je soubor rozhodnutí a nástrojů, kterými stát a veřejné instituce ovlivňují ekonomiku. Nejde jen o vládu. Důležitou roli má také centrální banka, samosprávy, zákony, regulace a systém sociální ochrany.")

        st.markdown("""
        | Nástroj / oblast | Kdo ji používá | Co dělá | Moderní příklad |
        | :--- | :--- | :--- | :--- |
        | **Fiskální politika** | Vláda, parlament, Ministerstvo financí | Pracuje se státním rozpočtem, daněmi, výdaji, dotacemi a veřejnými investicemi. | Stát zvýší nebo sníží daně, vyplatí pomoc během krize, investuje do dálnic, škol nebo digitalizace. |
        | **Monetární politika** | ČNB jako centrální banka | Ovlivňuje množství peněz v ekonomice, úrokové sazby, inflaci a finanční stabilitu. | Vyšší úrokové sazby mohou zdražit hypotéky a ztížit cestu k vlastnímu bydlení, ale pomáhají brzdit inflaci. |
        | **Sociální politika** | Stát, ministerstva, obce, systém sociálního zabezpečení | Vytváří záchrannou síť při nemoci, stáří, ztrátě práce, chudobě nebo péči o děti. | Důchody, nemocenská, podpora v nezaměstnanosti, příspěvek na bydlení, zdravotní pojištění. |
        | **Regulační politika** | Stát, úřady, EU, dohledové instituce | Nastavuje pravidla pro firmy, ochranu spotřebitele, hospodářskou soutěž, data, bezpečnost a životní prostředí. | Pravidla pro e-shopy, ochrana osobních údajů, digitální platformy, zákaz klamavé reklamy, limity emisí. |
        """)

        st.info("🏦 **ČNB a vláda nejsou totéž:** Vláda rozhoduje o rozpočtu a daních. Česká národní banka (ČNB) je nezávislá centrální banka, která nastavuje měnovou politiku. Obě ale ovlivňují stejnou ekonomiku.")

        with st.expander("Proč je těžší dosáhnout na hypotéku?"):
            st.write("Když jsou úrokové sazby vyšší, půjčené peníze jsou dražší. Hypotéka má vyšší měsíční splátku, banka přísněji posuzuje schopnost splácet a část lidí na úvěr nedosáhne. Vyšší sazby mohou brzdit inflaci, ale zároveň komplikují bydlení, investice firem i spotřebu domácností.")

        with st.expander("Co se stane, když onemocníš, ztratíš práci nebo zestárneš?"):
            st.write("To řeší sociální politika a systém sociálního zabezpečení. V ČR existuje veřejné zdravotní pojištění, nemocenské pojištění, důchodový systém, podpora v nezaměstnanosti a různé sociální dávky. Smyslem je, aby životní krize automaticky neznamenala úplný finanční kolaps.")
            st.write("**Srovnání pro pochopení:** V některých zemích může vážnější zdravotní problém znamenat vysoké účty a riziko zadlužení. V ČR člověk u běžné péče často ukáže kartičku pojišťovny, protože zdravotnictví je financováno převážně přes veřejné zdravotní pojištění. Není to „zdarma“ — platí se průběžně z odvodů a veřejných peněz.")

        st.divider()
        st.markdown("#### 1.5 Kvíz: poznáš funkci státu?")
        st.write("U každé situace urči, o jakou funkci nebo nástroj státu jde:")

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

        st.divider()
        st.markdown("#### 1.6 Mini aktivita: Stát jako správce společného účtu")
        st.write("Představ si, že tvá třída má společný rozpočet **100 000 Kč** na zlepšení života ve škole.")

        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"]("5.1.2", "1. Rozděl 100 000 Kč třídního rozpočtu mezi 3 oblasti: A) bezpečnost/vybavení, B) pomoc slabším studentům, C) akce a rozvoj školy.", "5", st.session_state.get("ulozene_odpovedi", {}))
            st.session_state["vykresli_otazku_fn"]("5.1.3", "2. Ke každé oblasti napiš, jakou funkci státu to připomíná (alokační, redistribuční, stabilizační...).", "5", st.session_state.get("ulozene_odpovedi", {}))
            st.session_state["vykresli_otazku_fn"]("5.1.4", "3. Co by se stalo, kdyby o všem rozhodoval jen trh (kdo zaplatí, ten má službu/pomoc, kdo nezaplatí, nemá nic)?", "5", st.session_state.get("ulozene_odpovedi", {}))
            st.session_state["vykresli_otazku_fn"]("5.1.5", "4. Napiš jedno riziko příliš malého a jedno riziko příliš velkého zásahu státu/vedení školy.", "5", st.session_state.get("ulozene_odpovedi", {}))

    # =========================================================================
    # SEKCE 2: DANĚ A STÁTNÍ ROZPOČET
    # =========================================================================
    elif selected_section_5.startswith("2."):
        st.markdown("### 2. Daně, státní rozpočet a ekonomická realita")

        st.markdown(
            "<div class='box-green'>"
            "🧾 <b>Moderní hook:</b> Kolik státu odevzdáš z první brigády, prodeje na Vinted, streamování na Twitchi, spolupráce na TikToku nebo zisku z kryptoměn? Daně nejsou jen formulář. Jsou to pravidla, která propojují soukromé příjmy, veřejné služby, státní rozpočet, solidaritu i ekonomickou odpovědnost."
            "</div>",
            unsafe_allow_html=True,
        )

        st.divider()
        st.markdown("#### 2.1 Základy daňového systému: co je daň a proč existuje")
        st.write("Daň je povinná, zákonem stanovená platba do veřejného rozpočtu, za kterou člověk nebo firma obvykle nedostává přímou konkrétní protislužbu. Neplatíš daň z příjmu proto, aby ti stát druhý den opravil přesně tvoji ulici. Platíš ji do společného systému.")

        st.markdown("""
        | Pojem | Co znamená | Příklad | Jak si to zapamatovat |
        | :--- | :--- | :--- | :--- |
        | **Daň** | Povinná platba do veřejného rozpočtu bez přímé konkrétní protislužby. | Daň z příjmů, DPH, daň z nemovitých věcí. | Platím do společného systému. |
        | **Poplatek** | Platba za konkrétní úkon, službu nebo oprávnění. | Poplatek za psa, komunální odpad, správní poplatek za doklad. | Platím za konkrétní věc nebo administrativní úkon. |
        | **Clo** | Platba spojená s dovozem zboží ze zahraničí, zejména ze zemí mimo EU. | Dovoz určitého zboží z mimoevropského e-shopu. | Souvisí s hranicí, obchodem a ochranou trhu. |
        """)

        with st.expander("Daň vs. poplatek: proč daň z příjmu není totéž co poplatek za psa?"):
            st.write("**Daň z příjmu** platíš podle toho, že máš zdanitelný příjem. Peníze jdou do veřejných rozpočtů. **Poplatek za psa** nebo komunální odpad má užší vazbu na konkrétní místní správu a náklad obce. Daň je obecnější příspěvek.")

        st.divider()
        st.markdown("#### 2.2 Funkce daní: proč stát daně vybírá")
        st.markdown("""
        | Funkce daní | Co znamená | Příklad |
        | :--- | :--- | :--- |
        | **Fiskální funkce** | Daně přinášejí peníze do veřejných rozpočtů. | Z DPH a daně z příjmů stát financuje školy, bezpečnost, důchody. |
        | **Alokační funkce** | Daně financují oblasti, které by trh sám neposkytl dostatečně. | Veřejné školství, silnice, hasiči, obrana, výzkum. |
        | **Redistribuční funkce** | Daně a veřejné výdaje mohou zmírňovat nerovnosti. | Lidé s vyššími příjmy přispívají více a stát financuje dávky a podporu. |
        | **Regulační funkce** | Daně mohou motivovat nebo odrazovat od určitého chování. | Spotřební daň u alkoholu a tabáku; ekologické daně. |
        """)

        st.divider()
        st.markdown("#### 2.3 Zásady zdaňování: jak poznat „dobrou“ daň")
        st.markdown("""
        | Zásada | Co znamená | Otázka pro studenta |
        | :--- | :--- | :--- |
        | **Spravedlnost** | Daňové zatížení má odpovídat schopnosti platit a být vnímáno jako férové. | Mají lidé s vyššími příjmy platit nejen více korun, ale i vyšší procento? |
        | **Efektivnost** | Daň by neměla zbytečně brzdit práci, podnikání, investice a tvorbu hodnoty. | Kdy už vysoká daň lidi odrazuje od práce nebo firmy od investic? |
        | **Jednoduchost** | Daň má být pochopitelná a administrativně zvládnutelná. | Je systém tak složitý, že mu běžný člověk nerozumí bez poradce? |
        | **Právní jistota** | Pravidla mají být předvídatelná a ověřitelná. | Vím předem, co mám zaplatit a kde si to ověřit? |
        """)

        st.divider()
        st.markdown("#### 2.4 Progresivní vs. rovná daň")
        st.markdown("""
        | Typ zdanění | Princip | Výhoda | Riziko |
        | :--- | :--- | :--- | :--- |
        | **Rovná daň** | Všichni platí stejné procento ze základu daně. | Je jednodušší a přehlednější. | Může být vnímána jako méně solidární k chudším. |
        | **Progresivní daň** | S vyšším příjmem roste daňová sazba nebo daňové zatížení. | Více zohledňuje schopnost platit. | Může vyvolat debatu o motivaci pracovat a podnikat. |
        """)

        with st.expander("Mýtus vs. realita progresivní daně"):
            st.write("**Mýtus:** „Když přejdu do vyššího daňového pásma, vydělám ve výsledku méně peněz.“\n\n**Realita:** U běžné progresivní daně se vyšší sazbou obvykle daní až *část příjmu nad určitou hranicí*, ne celý příjem. Člověk tedy po zvýšení hrubého příjmu zpravidla nemá méně peněz než předtím — jen z dodatečné části příjmu odvede vyšší podíl.")

        st.divider()
        st.markdown("#### 2.5 Přímé daně: peníze, které se vážou ke konkrétní osobě nebo firmě")
        st.write("Přímé daně platí konkrétní člověk nebo firma ze svého příjmu, zisku nebo majetku. Daň je tedy přímo spojena s poplatníkem.")

        st.markdown("""
        | Přímá daň | Kdo ji platí | Co zdaňuje | Příklad |
        | :--- | :--- | :--- | :--- |
        | **Daň z příjmů fyzických osob (DPFO)** | Jednotlivci. | Mzdu, podnikání, pronájmy, kapitálové příjmy. | Brigáda, zaměstnání, OSVČ, online příjmy. |
        | **Daň z příjmů právnických osob (DPPO)** | Firmy a jiné právnické osoby. | Zisk právnické osoby. | S.r.o. platí daň ze zisku. |
        | **Daň z nemovitých věcí** | Vlastníci nemovitostí. | Vlastnictví nemovitosti. | Majitel bytu nebo domu platí daň obci/státu. |
        | **Silniční daň** | U vybraných vozidel podle zákona. | Používání určitých vozidel v podnikatelském kontextu. | Týká se spíše firemních a nákladních vozidel. |
        """)

        st.info("📌 **Reality check: první brigáda:** U DPP nebo DPČ není důležité jen „kolik je hodinová mzda“. Záleží na typu dohody, výši příjmu, odvodech, dani, podepsaném Prohlášení poplatníka a slevách na dani. Proto hrubá mzda není automaticky částka, která přijde na účet.")

        with st.expander("Co je „růžový papír“?"):
            st.write("**Prohlášení poplatníka k dani** je formulář, díky kterému může zaměstnanec u jednoho zaměstnavatele uplatnit základní slevu na poplatníka. Pokud pracuješ na brigádě, podepsané prohlášení může výrazně ovlivnit čistou částku na účtu. Nelze ho ale běžně uplatňovat u více zaměstnavatelů současně za stejné období.")

        with st.expander("Jak se daní TikTok, Twitch, OnlyFans, Patreon nebo barter na Instagramu?"):
            st.write("Pokud někdo dlouhodobě a soustavně vydělává tvorbou obsahu, spolupracemi, reklamou nebo prodejem, může jít o zdanitelný příjem a někdy i o podnikání. **Barter:** Když influencer dostane produkt výměnou za propagaci, i nepeněžní plnění může mít hodnotu, kterou je potřeba řešit daňově.")

        with st.expander("Vinted, Bazoš, eBay: kdy je to ještě prodej vlastních věcí?"):
            st.write("Když prodáš vlastní staré oblečení, telefon nebo učebnice, obvykle jde o jinou situaci než pravidelný nákup a prodej zboží za účelem zisku. Bezpečná otázka: Prodávám vlastní použité věci, nebo soustavně nakupuji/prodávám se záměrem vydělávat?")

        with st.expander("Kryptoměny, akcie a ETF: co si ověřit před prodejem?"):
            st.write("U investic je důležité rozlišit typ aktiva, dobu držení, výši příjmů. U akcií a ETF se často řeší **časový test** a limity pro osvobození příjmů. U kryptoměn se zdanění liší a časový test nemusí fungovat stejně. Aplikace jako Revolut usnadní nákup, ale nezbaví člověka povinnosti zjistit, jak se řeší daně.")

        st.divider()
        st.markdown("#### 2.6 Nepřímé daně: neviditelné daně v každém nákupu")
        st.write("Nepřímé daně jsou zahrnuté v ceně zboží nebo služby. Spotřebitel je fakticky zaplatí v ceně, ale státu je odvádí prodejce.")

        st.markdown("""
        | Nepřímá daň | Co znamená | Příklad | Proč existuje |
        | :--- | :--- | :--- | :--- |
        | **DPH — daň z přidané hodnoty** | Daň zahrnutá v ceně většiny zboží a služeb. | Mobil, oblečení, lístek na akci. | Je významným příjmem státního rozpočtu. |
        | **Spotřební daně** | Daně u vybraných výrobků s dopadem na zdraví či spotřebu. | Tabák, alkohol, pohonné hmoty. | Přinášejí příjmy a omezují škodlivou spotřebu. |
        | **Ekologické daně** | Daně související s dopady na životní prostředí. | Vybraná paliva, energie. | Motivují k šetrnějšímu chování. |
        """)

        with st.expander("Anatomie ceny mobilu nebo lístku na koncert"):
            st.write("Když si koupíš produkt za konečnou cenu, část ceny tvoří DPH. U plátce DPH je cena pro zákazníka obvykle včetně DPH, zatímco podnikatel sleduje cenu bez DPH a daň, kterou musí odvést nebo si může nárokovat. **Úkol:** Najdi účtenku a zkus určit: celková cena, základ daně, sazba DPH, částka DPH.")

        st.warning("🚬 **Daně z hříchu — sin taxes:** Alkohol, cigarety nebo pohonné hmoty jsou dražší také kvůli spotřebním daním. Stát tím získává příjmy a odrazuje od spotřeby, která má zdravotní či environmentální dopady.")
        st.success("🌱 **Ekologická logika daní:** Pokud činnost vytváří náklady pro okolí (emise, znečištění), stát se může snažit část těchto nákladů promítnout do ceny.")

        st.divider()
        st.markdown("#### 2.6.1 Schéma: jak se daně dělí a kam putují")
        st.write("Daně se v učivu nejčastěji dělí na **přímé** a **nepřímé**. Přesné podíly rozdělování se mohou měnit, proto je důležité pracovat s principem.")

        st.markdown("""
        | Daň | Kam typicky putuje | Co se z ní financuje |
        | :--- | :--- | :--- |
        | **Daň z příjmů fyzických osob** | Sdílená daň — státní rozpočet, obce a kraje. | Důchody, sociální systém, školství, místní a regionální služby. |
        | **Daň z příjmů právnických osob** | Sdílená daň — stát, obce a kraje. | Veřejné služby, infrastruktura, školy, doprava. |
        | **DPH** | Významná sdílená daň. | Široký balík veřejných výdajů: důchody, školství, zdravotnictví, správa státu. |
        | **Daň z nemovitých věcí** | Připadá obci/městu, kde se nemovitost nachází. | Chodníky, osvětlení, zeleň, odpad, školy, kultura. |
        | **Spotřební daně** | Směřují především do státního rozpočtu. | Obecné výdaje státu a částečně regulace škodlivých dopadů. |
        | **Ekologické daně** | Veřejné rozpočty. | Motivace k šetrnějšímu chování vůči klimatu. |
        | **Clo** | Ochrana společného trhu a příjmy rozpočtu EU. | Financování evropských politik. |
        """)

        with st.form("diskuse_regiony"):
            st.write("Diskusní otázka: Je spravedlivější, aby víc peněz z daní zůstávalo obcím, kde se vyberou, nebo aby se více přerozdělovalo mezi bohatší a chudší regiony?")
            nazor_region = st.radio("Zvol si svůj postoj:", [
                "Ať peníze zůstanou tam, kde vznikly. Úspěšná města by neměla doplácet na ta pasivní.",
                "Stát musí být solidární. Peníze z bohatých center se musí rozdělovat i do chudších regionů.",
                "Měl by se najít kompromis."
            ], key="k5_2_6_regiony")
            if st.form_submit_button("Odeslat a uložit názor 💾"):
                st.success("Odesláno!")
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"]("Kapitola 5", "Podkapitola 2.6.1 - Přerozdělování regionům", nazor_region)

        st.divider()
        st.markdown("#### 2.7 Státní rozpočet: velká státní peněženka")
        st.write("Státní rozpočet je **plán příjmů a výdajů státu na určité období**, obvykle na jeden rok.")
        
        st.markdown("""
        | Příjmy státního rozpočtu | Výdaje státního rozpočtu |
        | :--- | :--- |
        | daně, pojistné a další povinné platby | důchody, sociální dávky, školství, obrana, bezpečnost |
        | poplatky, příjmy z majetku, evropské prostředky | platy zaměstnanců veřejného sektoru, provoz úřadů, investice |
        | případně půjčené peníze při deficitu | obsluha státního dluhu, infrastruktura, krizová pomoc |
        """)

        st.markdown("#### 2.8 Výdaje rozpočtu: mandatorní a nemandatorní")
        st.markdown("""
        | Typ výdaje | Co znamená | Příklad | Proč je důležitý |
        | :--- | :--- | :--- | :--- |
        | **Mandatorní výdaje** | Povinné výdaje dané zákonem nebo smluvními závazky. | Důchody, některé sociální dávky, obsluha dluhu. | Stát je nemůže snadno snížit bez změny zákonů. |
        | **Nemandatorní výdaje** | Výdaje, o kterých se rozhoduje pružněji v rámci rozpočtu. | Některé investice, dotace, programy, provozní výdaje. | Politici o nich více vyjednávají při tvorbě rozpočtu. |
        """)

        with st.expander("Rozpočtový reality check: kdyby stát byl domácnost?"):
            st.write("Domácnost má povinné platby: nájem, energie, splátky, jídlo. Stát má podobně výdaje, které jsou velmi těžko okamžitě změnitelné. Rozdíl je v tom, že stát není běžná domácnost: může vybírat daně, vydávat dluhopisy a rozhodovat o veřejných službách. Přesto platí, že dlouhodobé deficity vytvářejí tlak na budoucí rozpočty.")

        st.markdown("#### 2.9 Vyrovnaný, přebytkový a schodkový rozpočet")
        st.markdown("""
        | Typ rozpočtu | Co znamená | Jednoduchý příklad |
        | :--- | :--- | :--- |
        | **Vyrovnaný rozpočet** | Příjmy se rovnají výdajům. | Stát vybere 100 a utratí 100. |
        | **Přebytkový rozpočet** | Příjmy jsou vyšší než výdaje. | Stát vybere 100 a utratí 95. |
        | **Schodkový rozpočet / deficit** | Výdaje jsou vyšší než příjmy. | Stát vybere 100 a utratí 120. Rozdíl si musí půjčit. |
        """)

        # ZDE VLOŽEN AKTUALIZOVANÝ SIMULÁTOR
        render_dluhovy_simulator()

        st.divider()
        st.markdown("#### 2.10 Státní dluh a státní dluhopisy")
        st.write("Státní dluh vzniká, když stát dlouhodobě financuje schodky rozpočtu půjčkami. Jedním z nástrojů financování jsou **státní dluhopisy**. Když stát vydá dluhopis, půjčuje si peníze od investorů a slíbí, že je v budoucnu vrátí a zaplatí úrok.")

        st.markdown("""
        | Otázka | Krátká odpověď |
        | :--- | :--- |
        | Kdo kupuje státní dluhopisy? | Banky, fondy, pojišťovny, zahraniční investoři, firmy i občané podle typu emise. |
        | Proč je stát vydává? | Aby financoval schodek rozpočtu nebo refinancoval starší dluh. |
        | Je státní dluhopis bez rizika? | Obvykle se považuje za relativně bezpečný, ale záleží na státu, měně, inflaci, úroku a době splatnosti. |
        | Jak se dluh týká Gen Z? | Budoucí generace mohou nést náklady vyššího dluhu přes daně, nižší prostor pro investice nebo vyšší výdaje na úroky. |
        """)

        st.divider()
        st.markdown("#### 2.11 Daňové úniky, optimalizace a stínová ekonomika")
        st.write("Ne každé snížení daní je nelegální. Je potřeba rozlišovat legální optimalizaci a nelegální daňový únik.")

        st.markdown("""
        | Situace | Co znamená | Příklad | Hodnocení |
        | :--- | :--- | :--- | :--- |
        | **Legální daňová optimalizace** | Využití zákonných možností ke snížení daňové povinnosti. | Uplatnění slevy na poplatníka, daňově uznatelných výdajů. | Legální, pokud odpovídá pravidlům a realitě. |
        | **Nelegální daňový únik** | Porušení zákona s cílem nezaplatit daň. | Nefakturování příjmů, fiktivní náklady, zatajené tržby. | Nelegální a rizikové. |
        | **Šedá ekonomika** | Činnost, která může být legální sama o sobě, ale není správně evidovaná nebo zdaněná. | Práce „na ruku“ bez dokladu. | Poškozuje rozpočty a může poškodit i pracovníka. |
        | **Černá ekonomika** | Nelegální činnost mimo zákonný systém. | Obchod s nelegálním zbožím. | Nelegální a společensky škodlivá. |
        """)

        with st.expander("Práce „na ruku“: proč je sleva bez účtenky problém?"):
            st.write("Když zákazník zaplatí hotově bez dokladu, může mít pocit, že ušetřil. Jenže chybí doklad pro reklamaci, příjem nemusí být zdaněný a pracovník nemusí mít správně odvody. To může znamenat nižší příjmy veřejných rozpočtů, horší ochranu zákazníka i dopady na sociální a zdravotní pojištění.")

        with st.expander("Jak se vyhýbají daním velké firmy?"):
            st.write("Nadnárodní firmy mohou využívat rozdíly mezi daňovými systémy zemí, přesouvat zisky, licence nebo sídla do států s výhodnějším zdaněním. Proto se řeší **daňové ráje**, digitální daň, pravidla EU/OECD a myšlenka globální minimální daně pro velké korporace. Pointa: Problém není jen v tom, zda firma formálně dodrží zákon, ale také v tom, kde skutečně vzniká hodnota a kde se odvádějí daně.")

        st.divider()
        st.markdown("#### 2.12 Praktická aplikace: mzda, účtenka a daňové dilema")
        
        st.markdown(
            "<div class='box-green'><strong>🔗 Užitečné zdroje k ověřování daní:</strong><br>"
            "- <a href='https://financnisprava.gov.cz/' target='_blank'>Finanční správa ČR</a><br>"
            "- <a href='https://adisspr.mfcr.cz/' target='_blank'>Portál MOJE daně</a><br>"
            "- <a href='https://adisspr.mfcr.cz/pmd/epo/formulare' target='_blank'>MOJE daně — Elektronické formuláře EPO</a><br>"
            "- <a href='https://www.mpsv.cz/kalkulacka-ciste-mzdy' target='_blank'>Kalkulačka čisté mzdy MPSV</a></div>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<div class='box-yellow'><strong>🧾 Praktická ukázka ve třídě: OSVČ a daň z příjmů fyzických osob</strong><br>"
            "Otevřete Elektronické formuláře EPO na portálu MOJE daně. Bez přihlášení vyberte formulář pro daň z příjmů fyzických osob a spusťte vyplnění pomocí průvodce. Ukážte si, jak se zadávají příjmy, výdaje, slevy na dani a jak formulář průběžně kontroluje chyby. Ve třídě používejte jen fiktivní údaje!</div>",
            unsafe_allow_html=True
        )

        st.write("**Mini aktivita: Daňový detektiv**")
        st.write("Vyber jednu situaci a rozhodni, co by si člověk měl ověřit:\n1. Student má první DPP na festivalu.\n2. Student prodává staré oblečení na Vinted.\n3. Tvůrce dostane barter za propagaci na Instagramu.\n4. Někdo prodá kryptoměnu se ziskem.\n5. Opravář nabídne nižší cenu bez dokladu.")
        st.write("**Výstup:** Napiš tři otázky, které je potřeba ověřit, a jeden možný důsledek špatného rozhodnutí.")

    # =========================================================================
    # SEKCE 3: MOJE DANĚ V PRAXI
    # =========================================================================
    elif selected_section_5.startswith("3."):
        st.markdown("### 3. Moje daně v praxi")
        st.markdown(
            "<div class='box-blue'>"
            "💻 <b>Praktický přesah:</b> Daňový portál, datová schránka, elektronická identita a Portál občana ukazují, že ekonomika není jen teorie. Moderní občan potřebuje rozumět tomu, kde hledat informace, jak ověřovat povinnosti a proč je digitální komunikace se státem součástí finanční gramotnosti."
            "</div>",
            unsafe_allow_html=True,
        )

        st.markdown("#### Praktické scénáře pro studenty")
        with st.expander("Proč hrubá mzda není to samé, co mi přijde na účet? (První brigáda a „Růžový papír“)"):
            st.write("U DPP nebo DPČ není důležité jen „kolik je hodinová mzda“. Záleží na typu dohody, výši příjmu, odvodech, dani, podepsaném **Prohlášení poplatníka k dani** (růžový papír) a slevách na dani. Díky růžovému papíru může zaměstnanec uplatnit základní slevu na poplatníka. Lze ho ale uplatňovat v daném měsíci vždy pouze u jednoho zaměstnavatele.")

        with st.expander("Jak se daní TikTok, Twitch, OnlyFans, Patreon nebo barter na Instagramu?"):
            st.write("Pokud někdo dlouhodobě a soustavně vydělává tvorbou obsahu, spolupracemi, reklamou, předplatným, dary od fanoušků nebo prodejem digitálních produktů, nejde jen o „peníze z internetu“. Může jít o zdanitelný příjem a někdy i o podnikání. I barter (produkt výměnou za reklamu) může mít ekonomickou hodnotu a daňové dopady.")

        with st.expander("Vinted, Bazoš, eBay: Kdy je to ještě prodej vlastních věcí?"):
            st.write("Když prodáš vlastní staré oblečení nebo učebnice, obvykle jde o osvobozený příjem. Ale pokud systematicky nakupuješ věci za účelem jejich dalšího prodeje se ziskem, už se to může považovat za podnikání a podléhat zdanění.")

        with st.expander("Kryptoměny, akcie a ETF: Co si ověřit před prodejem?"):
            st.write("U akcií a ETF se často řeší tzv. **časový test** (po určité době držení je prodej osvobozen od daně) a limit ročních příjmů z prodeje. U kryptoměn se zdanění liší od běžných cenných papírů a časový test v ČR na kryptoměny tradičně neplatil (pravidla se mohou měnit, je třeba sledovat platnou legislativu). Revolut a další apky usnadní nákup, ale daně musíš řešit ty.")

        st.markdown(
            "#### 3.2 Trenažér: „Tohle přece danit nemusím!“"
        )
        st.write("Vyber jednu situaci — brigáda, doučování, prodej výrobků, Vinted, YouTube/TikTok, pronájem přes Airbnb, investice nebo kryptoměny. Napiš, jaké otázky by sis musel/a ověřit, než prohlásíš: „Tohle danit nemusím.“")

        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"](
                "5.3.1",
                "Trenažér daně v praxi: Zvol si životní situaci a napiš 2-3 klíčové otázky k daním, které si musíte zjistit.",
                "5",
                st.session_state.get("ulozene_odpovedi", {}),
            )

    # =========================================================================
    # SEKCE 4: GLOBÁLNÍ SOUVISLOSTI
    # =========================================================================
    elif selected_section_5.startswith("4."):
        st.markdown("### 4. Globální souvislosti a svět bez hranic")

        st.markdown(
            "<div class='box-yellow'>"
            "🌐 <b>Moderní hook:</b> Tričko z Temu, mobil navržený v USA, čip z Tchaj-wanu, kompletace ve Vietnamu, doprava přes Suez a prodej v Česku. Globalizace znamená, že věci, které denně používáš, nevznikají „v jedné zemi“, ale v síti firem, států, dopravních cest, dat a pravidel."
            "</div>",
            unsafe_allow_html=True,
        )

        st.markdown("#### 4.1 Globalizace a mezinárodní obchod: jak se svět propojil")
        st.write("**Globalizace** znamená rostoucí propojení ekonomik, firem, lidí, technologií, dat a kapitálu napříč státy. Zboží, služby, peníze i informace se pohybují rychleji než dřív. Státy mezi sebou obchodují proto, že není efektivní vyrábět všechno doma. Každá země má jiné zdroje, technologie, pracovní sílu a kapitál.")
        
        st.markdown("""
        | Pojem | Co znamená | Příklad |
        | :--- | :--- | :--- |
        | **Mezinárodní dělba práce** | Země, firmy a regiony se specializují na různé části výroby a služeb. | Design v USA, čipy na Tchaj-wanu, kompletace v Asii, prodej v Evropě. |
        | **Absolutní výhoda** | Někdo dokáže vyrábět daný produkt s nižšími náklady nebo vyšší produktivitou než jiný. | Země s vhodným klimatem může levněji pěstovat tropické plodiny. |
        | **Komparativní výhoda** | Vyplatí se specializovat na to, v čem má člověk nebo země nejnižší obětovanou příležitost, i když by teoreticky zvládla více věcí. | Expert může umět psát i grafiku, ale pokud je výrazně lepší v psaní, vyplatí se mu grafiku zadat někomu jinému. |
        """)

        with st.expander("Proč tričko z druhého konce světa může stát méně než lístek na MHD?"):
            st.write("Nízká cena může vzniknout kombinací levné práce, obrovského objemu výroby, automatizace, slabší regulace, dotované dopravy, tvrdého tlaku na dodavatele, levných materiálů a digitálního marketingu. **Ale:** Nízká cena na účtence nemusí zahrnovat všechny náklady — například emise z dopravy, odpad, vodu, pracovní podmínky nebo dopady na lokální prodejce.")

        kviz_advokatka = st.radio(
            "Jsi nejlepší advokátka (3 000 Kč/h) a píšeš na klávesnici 2x"
            " rychleji než asistentka (300 Kč/h). Co uděláš?",
            [
                "Vyber řešení...",
                "A) Přepíšu si smlouvy sama. Jsem přece 2x rychlejší než asistentka.",
                "B) Najmu si asistentku. Můj ušetřený čas věnuji právní analýze (3 000 Kč/h).",
            ],
            key="k5_4_1_advokatka",
        )
        if st.button("Uložit odpověď advokátky 💾", key="btn_k5_4_1"):
            if "B)" in kviz_advokatka:
                st.success("✅ Přesně tak! Tvá komparativní výhoda je v právu.")
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"]("Kapitola 5", "Podkapitola 4.1 - Komparativní výhoda", kviz_advokatka[:30])

        st.divider()
        st.markdown("#### 4.2 Volný obchod, protekcionismus a obchodní bariéry")
        st.markdown("""
        | Přístup | Co znamená | Výhody | Rizika |
        | :--- | :--- | :--- | :--- |
        | **Volný obchod** | Stát omezuje překážky obchodu a umožňuje dovoz i vývoz. | Levnější zboží, větší výběr, tlak na konkurenci, růst specializace. | Závislost na zahraničí, tlak na domácí firmy, ztráta některých pracovních míst. |
        | **Protekcionismus** | Stát chrání domácí výrobce před zahraniční konkurencí. | Ochrana pracovních míst, strategických odvětví a bezpečnosti. | Dražší zboží pro zákazníky, odveta jiných států, menší konkurence. |
        """)
        
        st.warning("🧱 **Obchodní bariéry:** **clo** (daň na dovážené zboží), **kvóta** (omezení množství dovozu), **embargo** (zákaz obchodu s určitou zemí nebo zbožím), **technické normy** (pravidla kvality, bezpečnosti, původu nebo složení výrobku).")

        with st.expander("Protekcionismus v praxi: cla na čínské elektromobily"):
            st.write("Pokud EU zavede cla na levnější čínské elektromobily, může tím chránit evropské automobilky a pracovní místa. Zároveň ale může zdražit auta zákazníkům a zpomalit přechod k elektromobilitě. Debatní otázka: Má stát chránit domácí průmysl, i když tím zákazníkům zdraží výrobky?")

        with st.expander("Levné balíčky z Asie a rušení výjimek"):
            st.write("Mnoho států řeší, jak nastavit pravidla pro drobné zásilky z mimoevropských e-shopů. Pokud jsou malé balíčky zvýhodněné, může to podporovat levné dovozy, ale zároveň znevýhodnit domácí firmy a ztížit kontrolu kvality, bezpečnosti i daní.")

        clo_eu = st.slider("Výše cla na dovoz čínských aut (% z ceny):", 0, 50, 0, step=5, key="k5_4_2_clo")
        cena_cina = int(700000 * (1 + (clo_eu / 100)))
        cena_eu = 900000
        c_col1, c_col2 = st.columns(2)
        c_col1.metric("Čínské auto s clem", f"{cena_cina:,} Kč".replace(",", " "))
        c_col2.metric("Evropské auto", f"{cena_eu:,} Kč".replace(",", " "))
        if st.button("Uložit výpočet cla 💾", key="btn_k5_4_2_clo"):
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"]("Kapitola 5", "Podkapitola 4.2 - Clo na elektromobily", f"Clo: {clo_eu}% | Čína: {cena_cina} Kč")

        st.divider()
        st.markdown("#### 4.3 Globální dodavatelské řetězce a zranitelnost ekonomiky")
        st.write("Moderní ekonomika funguje v síti dodavatelů. Jeden výrobek může projít přes desítky zemí. Firmy často používají systém **Just-in-Time**, kdy se neskladuje mnoho zásob a díly přicházejí přesně tehdy, kdy jsou potřeba. Výhoda: nižší náklady, rychlejší výroba. Riziko: když se zasekne doprava, čip nebo energie, zastaví se celý řetězec.")

        st.markdown("""
        | Riziko globalizace | Co se stane | Proč to dopadne i na Česko |
        | :--- | :--- | :--- |
        | **Krize čipů** | Chybí mikročipy pro auta, mobily, konzole, průmyslové stroje. | Automobilový průmysl je pro ČR klíčový a závisí na globálních dodávkách. |
        | **Blokáda dopravy** | Zpoždění lodí, dražší kontejnery, výpadky zboží. | České obchody i firmy používají zboží a díly přepravované přes světové trasy. |
        | **Válka nebo geopolitický konflikt** | Výpadky energií, potravin, surovin nebo dopravy. | Ceny plynu, elektřiny, obilí nebo hnojiv se promítají do inflace a nákladů firem. |
        | **Deglobalizace a reshoring** | Firmy přesouvají výrobu blíž k zákazníkům nebo do bezpečnějších zemí. | Může vzniknout více pracovních míst v Evropě, ale výrobky mohou být dražší. |
        """)

        with st.expander("Když se zasekne Suez nebo Rudé moře"):
            st.write("Suezský průplav a další úzká místa světové dopravy jsou jako „dopravní tepny“ globalizace. Když se zablokují, lodě musí plout oklikou, doprava trvá déle, pojištění a palivo zdraží a část nákladů se promítne do cen zboží.")

        st.divider()
        st.markdown("#### 4.4 Evropská unie a jednotný vnitřní trh: náš domácí prostor")
        st.write("Česká republika není ekonomický ostrov. Je součástí **Evropské unie** a jejího **jednotného vnitřního trhu**, který patří mezi největší obchodní prostory na světě.")
        
        st.markdown("""
        **Čtyři svobody EU:**
        1. **Volný pohyb zboží** — firmy mohou prodávat výrobky v rámci EU bez klasických celních hranic.
        2. **Volný pohyb osob** — občané EU mohou cestovat, studovat, pracovat a žít v jiných státech EU.
        3. **Volný pohyb služeb** — firmy a lidé mohou nabízet služby přes hranice.
        4. **Volný pohyb kapitálu** — peníze a investice se mohou pohybovat mezi státy EU.
        """)

        st.markdown("""
        | EU v praxi | Co to znamená pro Gen Z |
        | :--- | :--- |
        | **Erasmus+ a studium** | Možnost studovat v zahraničí, získat zkušenosti, jazyk a kontakty. |
        | **Práce v EU** | Snazší možnost pracovat od Portugalska po Finsko bez vízového režimu jako mimo EU. |
        | **Roaming jako doma** | Mobilní data a volání v EU bez starých roamingových poplatků podle pravidel EU. |
        | **Ochrana spotřebitele a dat** | Reklamace, bezpečnost výrobků, GDPR, pravidla digitálních platforem. |
        | **Brussels Effect** | Když EU nastaví silná pravidla, globální firmy je často přijmou i mimo Evropu, protože se jim nevyplatí vyrábět dvě verze produktu. |
        """)

        with st.expander("EU jako silný regulátor: USB-C, GDPR a AI Act"):
            st.write("EU dokáže ovlivnit globální firmy, protože evropský trh je velký a bohatý. Proto může prosadit pravidla pro nabíječky, ochranu osobních údajů, digitální platformy nebo umělou inteligenci. Debata: Chrání EU spotřebitele, nebo příliš reguluje inovace?")

        with st.expander("Mělo by Česko přijmout euro?"):
            st.write("**Argumenty PRO:** firmám by odpadlo měnové riziko při obchodování v eurozóně, lidem by odpadla část směn a kurzových poplatků při cestování, Česko by bylo hlouběji propojené s eurozónou.\n\n**Argumenty PROTI:** Česko by ztratilo vlastní měnovou politiku ČNB, přijetí eura může být politicky i psychologicky citlivé, společná měna nemusí všem ekonomikám vyhovovat stejně.")

        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"](
                "5.4.1",
                "Napiš své stanovisko k Euru v ČR (Euro bych v ČR přijal/a /"
                " nepřijal/a, protože...):",
                "5",
                st.session_state.get("ulozene_odpovedi", {}),
            )

        st.divider()
        st.markdown("#### 4.5 Klimatická krize, udržitelný rozvoj a mezinárodní instituce")
        st.write("Hospodářský růst naráží na limity planety. Ekonomika řeší otázku, jak vyrábět, dopravovat a spotřebovávat tak, aby růst neznamenal ničení zdrojů, klimatu a zdraví lidí. **Trvale udržitelný rozvoj:** Rozvoj, který uspokojuje potřeby současné generace, aniž by ohrozil možnost budoucích generací uspokojovat jejich vlastní potřeby.")

        st.markdown("""
        | Pojem / instituce | Co znamená | Proč je důležitá |
        | :--- | :--- | :--- |
        | **Green Deal** | Strategie EU pro přechod k nízkoemisní ekonomice. | Ovlivňuje energetiku, dopravu, průmysl, zemědělství i ceny. |
        | **CBAM / uhlíkové clo** | Mechanismus, který má zohlednit uhlíkovou stopu vybraných dovážených výrobků. | Brání tomu, aby firmy přesunuly výrobu do zemí s volnějšími ekologickými pravidly a pak levně dovážely zpět do EU. |
        | **ESG** | Environmental, Social, Governance — hodnocení environmentálních, sociálních a řídicích dopadů firmy. | Banky a investoři stále častěji řeší, zda je firma dlouhodobě odpovědná a rizikově udržitelná. |
        | **WTO** | Světová obchodní organizace. | Řeší pravidla světového obchodu a obchodní spory. |
        | **MMF** | Mezinárodní měnový fond. | Pomáhá státům při finančních krizích, problémech s platební bilancí nebo stabilitou měny. |
        | **Světová banka** | Instituce podporující rozvojové projekty a snižování chudoby. | Financuje projekty v infrastruktuře, vzdělávání, zdravotnictví nebo správě státu. |
        | **OSN** | Organizace spojených národů. | Řeší globální spolupráci, bezpečnost, rozvojové cíle a humanitární otázky. |
        """)

        with st.expander("Greenwashing: když se firma tváří zeleněji, než je"):
            st.write("Greenwashing znamená, že firma používá ekologickou rétoriku hlavně marketingově, ale skutečné dopady jejího podnikání se zásadně nemění. Kontrolní otázky: Má firma konkrétní data? Je jasné, co měří? Jsou cíle ověřitelné? Nezakrývá jeden „zelený“ produkt celkově problematický byznys?")

        st.divider()
        st.markdown("#### 4.6 Budoucnost práce a financí v globálním světě")
        st.write("Globalizace už není jen o kontejnerech a továrnách. Týká se také práce, dat, online služeb, kapitálu a digitálních měn.")

        st.markdown("""
        | Trend | Co znamená | Otázka pro studenta |
        | :--- | :--- | :--- |
        | **Digitální nomádství** | Člověk může žít v jedné zemi a pracovat online pro firmu nebo klienty z jiné země. | Kde má platit daně, sociální a zdravotní pojištění? |
        | **Remote work** | Práce na dálku rozšiřuje pracovní trh za hranice regionu. | Bude český pracovník soutěžit s lidmi z celého světa? |
        | **Mezinárodní kapitálové toky** | Peníze investorů se pohybují mezi státy, firmami, burzami a měnami. | Proč se krize v jedné zemi může rychle přelít do jiné? |
        | **CBDC a kryptoměny** | Státy zkoumají digitální měny centrálních bank, zatímco kryptoměny fungují decentralizovaně. | Má být budoucnost peněz více státní, nebo více decentralizovaná? |
        """)

        st.info("🏝️ **Digitální nomád není mimo systém:** To, že někdo pracuje z Bali, Portugalska nebo Španělska pro klienta z USA, neznamená, že „nemusí řešit stát“. Musí řešit daňovou rezidenci, zdravotní pojištění, sociální pojištění, víza, pracovní povolení a pravidla země, kde skutečně žije i odkud má příjmy.")

        st.divider()
        st.markdown("#### 4.7 Případová studie: anatomie jednoho produktu")
        st.markdown("""
        **Interaktivní případ: cesta chytrého telefonu**
        * **Nápad a design:** USA / Evropa / Korea
        * **Software a patenty:** globální technologické firmy
        * **Suroviny:** lithium, kobalt, měď, vzácné kovy z různých částí světa
        * **Čipy:** Tchaj-wan, Korea, USA, Nizozemsko a další specializované firmy
        * **Komponenty:** Japonsko, Korea, Čína, Vietnam, EU
        * **Kompletace:** Čína, Vietnam, Indie nebo jiné výrobní země
        * **Doprava:** lodě, letadla, sklady, přístavy, kamiony
        * **Prodej:** český e-shop nebo obchod
        
        **Otázka:** Komu z tohoto řetězce zůstane největší marže — těžaři surovin, továrně, dopravci, značce, platformě nebo prodejci? Proč?
        """)
        
        st.success("✅ **Co si zapamatovat:** Globalizace přinesla levnější zboží, větší výběr, nové příležitosti a propojení světa. Zároveň ale vytvořila závislosti, zranitelné řetězce, ekologické dopady a otázku, kdo skutečně nese náklady levné spotřeby.")

    # =========================================================================
    # SEKCE 5: ESG A UDRŽITELNOST
    # =========================================================================
    elif selected_section_5.startswith("5."):
        st.markdown("### 5. ESG a udržitelná ekonomika")

        st.markdown(
            "<div class='box-green'>"
            "🌱 <b>Moderní hook:</b> Firma dnes nestačí hodnotit jen podle toho, kolik vydělá. Investoři, banky, zákazníci i zaměstnanci se stále častěji ptají: Jak firma zachází s lidmi? Jakou má uhlíkovou stopu? Nezneužívá dodavatele? Není její „zelená“ reklama jen greenwashing?"
            "</div>",
            unsafe_allow_html=True,
        )

        st.markdown("#### 5.1 Udržitelný rozvoj: ekonomika, která nespotřebuje budoucnost")
        st.write("Udržitelný rozvoj znamená takový způsob výroby, spotřeby a života, který uspokojuje potřeby současné generace, aniž by ohrozil možnosti budoucích generací. Nejde jen o ochranu přírody. Udržitelnost má tři propojené roviny:")

        st.markdown("""
        | Rovina udržitelnosti | Co řeší | Příklad |
        | :--- | :--- | :--- |
        | **Ekonomická** | Zda firma, stát nebo domácnost funguje dlouhodobě finančně zdravě. | Firma nevydělává jen krátkodobě, ale investuje do inovací, lidí a kvality. |
        | **Environmentální** | Dopady na klima, vodu, půdu, odpady, biodiverzitu a spotřebu zdrojů. | Nižší emise, menší odpad, obnovitelné zdroje, úspory energie. |
        | **Sociální** | Dopady na lidi: zaměstnance, dodavatele, zákazníky i komunity. | Bezpečné pracovní podmínky, férová mzda, zákaz dětské práce, ochrana zdraví. |
        """)

        volba_tenisky = st.selectbox(
            "Zvol byznys strategii výroby tenisek:",
            [
                "Vyber...",
                "A) Výroba v Bangladéši za 50 Kč/ks (max zisk, škody na přírodě a lidech)",
                "B) Ruční eko-výroba v ČR za 8 000 Kč/ks (příliš drahé, nikdo nekoupí)",
                "C) Zlatá střední cesta: certifikovaná továrna, recykláty, cena 2 500 Kč",
            ],
            key="k5_5_1_tenisky",
        )
        if st.button("Uložit strategii tenisek 💾", key="btn_k5_5_1"):
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"]("Kapitola 5", "Podkapitola 5.1 - Strategie tenisek", volba_tenisky[:30])
            st.success("Strategie byla uložena!")

        st.divider()
        st.markdown("#### 5.2 Co znamená ESG")
        st.write("**ESG** je zkratka pro **Environmental, Social, Governance**. Používá se při hodnocení firem, investic a rizik. Nejde jen o morálku nebo reklamu — ESG může ovlivnit, zda firma získá úvěr, investici, veřejnou zakázku, dobré zaměstnance nebo důvěru zákazníků.")

        st.markdown("""
        | Oblast ESG | Co sleduje | Konkrétní příklady |
        | :--- | :--- | :--- |
        | **E — Environmental** | Dopady firmy na životní prostředí. | Emise CO₂, spotřeba energie, voda, odpady, obaly, doprava, recyklace, uhlíková stopa. |
        | **S — Social** | Dopady firmy na lidi. | Pracovní podmínky, bezpečnost práce, mzdy, diverzita, vztahy s komunitou, dodavatelé, zákaznická bezpečnost. |
        | **G — Governance** | Způsob řízení firmy. | Transparentnost, etika, boj proti korupci, férové účetnictví, odpovědné vedení, kontrola rizik. |
        """)

        with st.expander("Proč banku zajímá, jestli je firma ekologická?"):
            st.write("Banka nechce půjčit peníze firmě, která může za pár let narazit na pokuty, drahé energie, reputační skandál nebo ztrátu zákazníků. ESG proto funguje i jako řízení rizik. Firma se špatným ESG profilem může mít dražší financování nebo horší přístup k investorům.")

        st.divider()
        st.markdown("#### 5.3 Greenwashing: když zelená reklama zakrývá realitu")
        st.write("**Greenwashing** znamená, že firma působí ekologicky nebo odpovědně hlavně v reklamě, ale její skutečné dopady se zásadně nemění. Často používá vágní slova jako „eco“, „green“, „natural“, „planet friendly“ bez jasných dat.")

        st.markdown("""
        **Jak poznat greenwashing:**
        * firma uvádí hezký slogan, ale žádná měřitelná data,
        * zdůrazní jeden malý ekologický detail a mlčí o hlavním problému,
        * používá zelené barvy, listy a přírodu místo konkrétních důkazů,
        * tvrdí „udržitelné“, ale nevysvětlí podle jakých kritérií,
        * nemá nezávislé ověření nebo srovnání.
        """)

        with st.expander("Příklad: „eko“ kolekce ve fast fashion"):
            st.write("Značka může propagovat malou kolekci z recyklovaného materiálu, ale zároveň každý týden vyrábět obrovské množství levného oblečení, které rychle končí v odpadu. To neznamená, že recyklovaný materiál je špatně — problém je, pokud malý zelený prvek zakrývá celkově neudržitelný model.")

        with st.form("greenwashing_quiz"):
            q_gw1 = st.radio(
                "Firma chrlí 50 000 plastových triček denně, ale udělala 10 'bio' kusů a má eko-kampaň.",
                ["Vyber...", "Greenwashing ❌", "Poctivé ESG ✅"],
                key="k5_5_3_q1",
            )
            if st.form_submit_button("Vyhodnotit a uložit 💾"):
                if "Greenwashing" in q_gw1:
                    st.success("Přesně tak, toto je ukázkový Greenwashing!")
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"]("Kapitola 5", "Podkapitola 5.3 - Greenwashing test", q_gw1)

        st.divider()
        st.markdown("#### 5.4 Cirkulární ekonomika: od „vyrobit–použít–vyhodit“ k oběhu")
        st.write("Tradiční lineární model ekonomiky funguje jako **vyrobit → použít → vyhodit**. Cirkulární ekonomika se snaží, aby materiály a výrobky zůstávaly v oběhu co nejdéle.")

        st.markdown("""
        | Lineární ekonomika | Cirkulární ekonomika |
        | :--- | :--- |
        | Těžba surovin → výroba → spotřeba → odpad. | Návrh výrobku → dlouhé používání → oprava → sdílení → opětovné použití → recyklace. |
        | Výrobek se často navrhuje tak, aby byl levný a rychle nahraditelný. | Výrobek se navrhuje tak, aby šel opravit, rozebrat, sdílet nebo recyklovat. |
        """)
        st.info("♻️ **Příklady cirkulární ekonomiky:** opravitelné telefony, vratné obaly, second-hand, repasovaná elektronika, knihovny věcí, sdílená auta, recyklace materiálů, prodloužená záruka, právo na opravu.")

        st.divider()
        st.markdown("#### 5.5 ESG v dodavatelských řetězcích")
        st.write("Firma nenese odpovědnost jen za svou kancelář, ale i za dodavatele: kde vznikly suroviny, za jakých podmínek se kompletovaly komponenty a kolik emisí stála doprava.")

        st.markdown("""
        | Otázka pro firmu | Proč je důležitá |
        | :--- | :--- |
        | Kde vznikají suroviny? | Těžba může souviset s ekologickými škodami, konflikty nebo špatnými pracovními podmínkami. |
        | Kdo vyrábí komponenty? | Dodavatel může porušovat pracovní práva nebo bezpečnostní standardy. |
        | Jak se zboží dopravuje? | Doprava vytváří emise, náklady a zranitelnost řetězce. |
        | Co se stane po použití? | Výrobek může skončit jako odpad, nebo se může opravit, prodat dál či recyklovat. |
        """)

        st.divider()
        st.markdown("#### 5.6 Odpovědný spotřebitel: hlasuješ peněženkou, ale ne všechno je na tobě")
        st.write("Spotřebitel může ovlivnit trh tím, co kupuje, jak často nakupuje a jaké značky podporuje. Zároveň ale není fér svalit veškerou odpovědnost jen na jednotlivce. Pravidla nastavují i státy, EU, firmy, investoři a mezinárodní dohody.")

        with st.expander("Měl by být výrobek dražší, když lépe zahrnuje ekologické a sociální dopady?"):
            st.write("**Argument PRO:** Levné zboží často neobsahuje všechny skutečné náklady — emise, odpad, vodu nebo špatné pracovní podmínky. Vyšší cena může lépe odrážet realitu.\n\n**Argument PROTI:** Vyšší ceny mohou dopadnout hlavně na nízkopříjmové domácnosti. Udržitelnost se pak může stát „luxusem pro bohaté“.\n\n**Vyvážený pohled:** Cílem není jen zdražit všechno, ale nastavit pravidla, podporovat inovace, opravy, dostupné alternativy a férové informace pro zákazníka.")

        st.markdown(
            "<div class='box-green'><strong>🔗 Užitečné zdroje pro práci ve třídě:</strong><br>"
            "- <a href='https://faktaoklimatu.cz/' target='_blank'>Fakta o klimatu</a> — srozumitelná data a grafiky ke klimatu.<br>"
            "- <a href='https://faktaoklimatu.cz/kalkulacka' target='_blank'>Kalkulačka uhlíkové stopy Fakta o klimatu</a> — orientační propojení životního stylu a emisí.<br>"
            "- <a href='https://sdgs.un.org/goals' target='_blank'>OSN — Cíle udržitelného rozvoje</a> — globální rámec pro udržitelný rozvoj.</div>",
            unsafe_allow_html=True
        )

        st.markdown("##### 🕵️ Audit značky z pohledu ESG")
        st.write("Vyber jednu značku, kterou znáš — oblečení, elektronika, kosmetika, banka, e-shop nebo potraviny. Zkus najít: Co značka tvrdí o ekologii? Uvádí konkrétní data, nebo jen slogany? Řeší pracovní podmínky a dodavatele? Má informace o opravách, recyklaci nebo obalech? Co by mohlo být greenwashing?")
        znacka_nazev = st.text_input("Název značky:", value="H&M", key="k5_5_6_znacka")
        znamka = st.select_slider("Dej značce známku ESG:", options=["A", "B", "C", "D", "E (Greenwashing)"], value="C", key="k5_5_6_znamka")

        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"](
                "5.5.1",
                f"Napiš zdůvodnění pro známku ESG pro značku ({znacka_nazev}):",
                "5",
                st.session_state.get("ulozene_odpovedi", {}),
            )

    # =========================================================================
    # SEKCE 6: AKTIVITY A PŘÍPADOVÉ STUDIE
    # =========================================================================
    elif selected_section_5.startswith("6."):
        st.markdown("### 6. Aktivity a případové studie na závěr")
        st.write("Vyberte jednu studii do dvojice nebo skupiny. Nejprve popište ekonomický problém, potom určete roli státu, daní, trhu, globalizace a odpovědnosti firem. Nakonec navrhněte řešení a obhajte ho před třídou.")

        tab_studie1, tab_studie2, tab_studie3, tab_ukol = st.tabs([
            "👕 1. Levné tričko za 99 Kč",
            "📱 2. Student vydělává online",
            "🏙️ 3. Obec rozhoduje o rozpočtu",
            "✍️ Mini úkol: Cesta produktu",
        ])

        with tab_studie1:
            st.markdown("#### Případová studie 1: Levné tričko za 99 Kč")
            st.write(
                "**Situace:** Student si koupí tričko z fast fashion e-shopu za 99 Kč. Na první pohled je to výhodný nákup. "
                "Tričko ale vzniklo v globálním dodavatelském řetězci: bavlna, barvení látky, šití, balení, doprava, sklad, reklama, platforma a doručení až ke dveřím."
            )
            with st.expander("Možné řešení"):
                st.write("Levná cena může vzniknout díky velkému objemu výroby, nízkým mzdovým nákladům, efektivní logistice a silnému tlaku na dodavatele. Skryté náklady mohou být emise z dopravy, spotřeba vody, textilní odpad nebo horší pracovní podmínky. Stát a EU mohou nastavovat pravidla pro bezpečnost výrobků, férovou soutěž, informace pro spotřebitele nebo ekologické standardy. Spotřebitel může omezit impulzivní nákupy, využít second-hand, kupovat kvalitnější věci nebo se ptát na původ výrobku.")

            if "vykresli_otazku_fn" in st.session_state:
                st.session_state["vykresli_otazku_fn"](
                    "5.6.1",
                    "1. Kdo se podílel na cestě trička od bavlny po tvůj šatník?",
                    "5",
                    st.session_state.get("ulozene_odpovedi", {}),
                )
                st.session_state["vykresli_otazku_fn"](
                    "5.6.2",
                    "2. Jaké jsou viditelné a skryté náklady na výrobu a dopravu levného trička?",
                    "5",
                    st.session_state.get("ulozene_odpovedi", {}),
                )
                st.session_state["vykresli_otazku_fn"](
                    "5.6.3",
                    "3. Vysvětli pojmy externalita a ESG na příkladu Fast Fashion.",
                    "5",
                    st.session_state.get("ulozene_odpovedi", {}),
                )
                st.session_state["vykresli_otazku_fn"](
                    "5.6.4",
                    "4. Navrhni opatření pro udržitelný nákup oblečení.",
                    "5",
                    st.session_state.get("ulozene_odpovedi", {}),
                )

        with tab_studie2:
            st.markdown("#### Případová studie 2: Student vydělává online")
            st.write(
                "**Situace:** Student natáčí videa na TikTok, občas dostane barter od značky, prodává digitální šablony a jednou za čas mu přijde příjem z affiliate odkazu. "
                "Říká si: „Je to jen bokovka, daně řešit nemusím.“"
            )
            with st.expander("Možné řešení"):
                st.write("I barter může mít ekonomickou hodnotu, pokud je poskytnut výměnou za propagaci. Pokud se činnost opakuje, má záměr vydělávat a student ji organizuje soustavně, může jít o zdanitelný příjem nebo podnikání. Student by měl ověřit, zda musí podat daňové přiznání, zda potřebuje živnostenské oprávnění, jak evidovat příjmy a výdaje, jak řešit zdravotní a sociální pojištění a jak dokládat nepeněžní plnění. Pointa není studenty strašit, ale ukázat, že „internetový příjem“ není mimo pravidla.")

            if "vykresli_otazku_fn" in st.session_state:
                st.session_state["vykresli_otazku_fn"](
                    "5.6.5",
                    "1. Jaký je rozdíl mezi peněžním a nepeněžním příjmem (barterem)?",
                    "5",
                    st.session_state.get("ulozene_odpovedi", {}),
                )
                st.session_state["vykresli_otazku_fn"](
                    "5.6.6",
                    "2. Kdy se z občasné aktivity stává soustavné podnikání?",
                    "5",
                    st.session_state.get("ulozene_odpovedi", {}),
                )
                st.session_state["vykresli_otazku_fn"](
                    "5.6.7",
                    "3. Na co se zeptat účetního nebo úřadu při online výdělcích?",
                    "5",
                    st.session_state.get("ulozene_odpovedi", {}),
                )

        with tab_studie3:
            st.markdown(
                "#### Případová studie 3: Obec rozhoduje o rozpočtu 10 mil. Kč"
            )
            st.write(
                "**Situace:** Menší obec má rozhodnout, jak využije 10 milionů Kč. Část obyvatel chce opravit silnici a chodníky, část chce podpořit školu a volnočasové aktivity, část požaduje snížení místních poplatků a podnikatelé chtějí lepší parkování u náměstí."
            )
            with st.expander("Možné řešení"):
                st.write("Oprava silnic a chodníků souvisí s alokační funkcí a veřejnou infrastrukturou. Podpora školy může být pozitivní externalita, protože vzdělání prospívá nejen jednotlivci, ale celé komunitě. Sociální pomoc má redistribuční funkci. Podpora podnikání může zvýšit zaměstnanost a služby v obci, ale musí být férová a transparentní. Obec by měla ukázat kritéria rozhodování, očekávané dopady, náklady a důvody, proč nelze splnit všechny požadavky najednou.")

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
            st.write("Vyberte jeden běžný produkt a zkuste odhadnout, jaké země, firmy a dopravní kroky mohly být součástí jeho cesty k zákazníkovi.")
            moj_produkt = st.text_input("Zvolený produkt:", value="Moje tenisky", key="uk_prod")

            if "vykresli_otazku_fn" in st.session_state:
                st.session_state["vykresli_otazku_fn"]("5.6.8", f"1. Kde vznikl design produktu ({moj_produkt})?", "5", st.session_state.get("ulozene_odpovedi", {}))
                st.session_state["vykresli_otazku_fn"]("5.6.9", f"2. Odkud pocházejí suroviny pro ({moj_produkt})?", "5", st.session_state.get("ulozene_odpovedi", {}))
                st.session_state["vykresli_otazku_fn"]("5.6.10", f"3. Kde se produkt ({moj_produkt}) smontoval/vyrobil?", "5", st.session_state.get("ulozene_odpovedi", {}))
                st.session_state["vykresli_otazku_fn"]("5.6.11", f"4. Kdo získal největší část marže z prodeje produktu ({moj_produkt})?", "5", st.session_state.get("ulozene_odpovedi", {}))

        st.divider()
        st.success("🎉 Gratulujeme k dokončení Kapitoly 5!")
