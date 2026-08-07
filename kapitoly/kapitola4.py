import streamlit as st
import math

def render():
    st.markdown("<span class='hero-badge'>Kapitola 4</span>", unsafe_allow_html=True)
    st.title("4. Cesta zaměstnance: od první orientace po kariérní rozhodnutí")
    st.markdown("<p style='font-size: 1rem; color: #64748b; margin-bottom: 1.5rem;'>Práce není jen o výplatní pásce. Je to rozhodování o vlastní hodnotě, dovednostech, právní ochraně, penězích, vztazích na pracovišti i o tom, jak se přizpůsobit světu, který mění digitalizace, AI a globální konkurence.</p>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown("""
        <div class='box-blue'>
            <strong>⚙️ Pointa kapitoly:</strong> Tato kapitola je postavená jako kompletní cesta zaměstnance: od otázky „Kdo jsem a co umím?“ přes hledání práce, nábor, smlouvu a výplatní pásku až po wellbeing, kariérní růst, výpověď a krizové situace.
        </div>
        """, unsafe_allow_html=True)

    # 📌 PŘEHLED A NAVIGACE KAPITOLOU
    with st.expander("🧭 Co si z kapitoly odnesete a doporučené pořadí studia", expanded=False):
        c_nav1, c_nav2 = st.columns(2)
        with c_nav1:
            st.markdown("""
            **🎯 Klíčové výstupy:**
            * 🧭 **Orientace na trhu práce:** Proč se některé dovednosti oceňují více a jak trh mění AI.
            * 🧑‍💼 **HR, zaměstnání a právo:** Nábor, pracovní smlouva, DPP, DPČ, Švarcsystém a gig economy.
            * 🚩 **Red flags:** Varovné signály v inzerátech, na pohovoru i ve smlouvě.
            * 💵 **Mzda a cena práce:** Hrubá vs. čistá mzda, odvody a celkové náklady zaměstnavatele.
            * 🧘 **Wellbeing a kariéra:** Firemní kultura, prevence vyhoření, upskilling a reskilling.
            """)
        with c_nav2:
            st.markdown("""
            **🧭 Doporučené pořadí studia:**
            1. 🧭 **Já na trhu práce** (orientace v hodnotě práce, AI a digitální stopě)
            2. 📜 **Hra podle pravidel** (nábor, smlouvy, DPP, DPČ, zkušební doba, Švarcsystém)
            3. 💰 **Hodnota mé práce** (výplatní páska, čistá mzda, odvody, daně)
            4. 🧘 **Život v práci** (kultura, wellbeing, vyhoření, právo na odpojení)
            5. 🚪 **Když se cesty rozejdou** (výpověď, odstupné, úřad práce, podpora)
            """)

    # 📌 JEDNOTNÁ NABÍDKA PODKAPITOL
    section_options_4 = [
        "1.1 Proč trh platí různé profese různě",
        "1.2 Trh práce 4.0 a AI",
        "1.3 Profese a dovednosti budoucnosti",
        "1.4 Osobní brand a digitální stopa",
        "2.1 HR a personalistika: co znamenají",
        "2.2 Nábor v éře AI",
        "2.3 Životopis, motivační dopis a portfolio",
        "2.4 Pracovní smlouva, DPP a DPČ",
        "2.5 Ukázka pracovní smlouvy a její náležitosti",
        "2.6 Zkušební doba",
        "2.7 Smlouva na dobu určitou a neurčitou",
        "2.8 Švarcsystém a gig economy",
        "2.9 Red flags v inzerátech a smlouvách",
        "3.1 Hrubá mzda, čistá mzda a superhrubé uvažování",
        "3.2 Nominální a reálná mzda",
        "3.3 Výplatní páska a její náležitosti",
        "3.4 Výpočet čisté mzdy krok za krokem",
        "3.5 Sazby pojištění, daně a náklady zaměstnavatele",
        "3.6 Slevy na dani a odčitatelné položky",
        "3.7 Kam jdou odvody (sociální a zdravotní pojištění)",
        "3.8 Celková odměna za práci a vyjednávání o mzdě",
        "4.1 Firemní kultura a wellbeing",
        "4.2 Právo na odpojení a podnikavost v zaměstnání",
        "4.3 Upskilling a reskilling",
        "5.1 Jak dát a dostat výpověď profesionálně",
        "5.2 Úřad práce, podpora v nezaměstnanosti a rekvalifikace",
        "6.1 Praktická dílna (Aktivity 1–5)",
        "7.1 Případové studie z praxe",
        "7.2 Slovníček, rychlé opakování a prověrka"
    ]
    
    selected_section_4 = st.selectbox("📌 Přechod na podkapitolu:", section_options_4, index=0)
    st.divider()

    # =========================================================================
    # SEKCE 1: JÁ NA TRHU PRÁCE: PŘÍPRAVA A ORIENTACE
    # =========================================================================
    if selected_section_4 == "1.1 Proč trh platí různé profese různě":
        st.markdown("### 1.1 Proč trh platí různé profese různě")
        st.markdown("""
        <div class='box-blue'>
            🧭 <b>Základní otázka:</b> Kdo jsem, co umím a proč by za mou práci měl někdo zaplatit?
        </div>
        """, unsafe_allow_html=True)
        
        st.write("Trh práce je prostředí, kde se potkává **nabídka práce** (lidé nabízející čas a dovednosti), **poptávka po práci** (firmy potřebující vykonat činnost) a **cena práce** (mzda či odměna).")
        st.write("Mzda se neodvíjí od toho, jak moc se člověk fyzicky nadře. Ovlivňuje ji kombinace následujících faktorů:")

        st.markdown("""
        | Faktor | Co znamená | Příklad z praxe |
        | :--- | :--- | :--- |
        | 💎 **Nedostatek dovedností** | Čím méně lidí danou věc umí, tím vyšší je odměna. | Datová analýza, kyberbezpečnost, specializovaný řemeslník. |
        | ⚖️ **Odpovědnost** | Čím větší dopad má ошибка/chyba, tím vyšší jsou nároky i mzda. | Lékař, pilot, hlavní účetní, jeřábník. |
        | 🚀 **Produktivita a přidaná hodnota** | Kolik hodnoty či úspor dokáže člověk vytvořit za jednotku času. | Programátor, který automatizuje proces pro tisíce uživatelů. |
        | ⚠️ **Riziko a náročnost** | Fyzické, psychické nebo bezpečnostní nároky práce. | Práce ve zdravotnictví, výškové práce, směnný provoz. |
        | 💬 **Vyjednávací síla a region** | Místo výkonu práce, praxe, vzdělání a schopnost doložit výsledky. | Praha vs. menší regiony, junior vs. seniorní specialista. |
        """)

        st.markdown("""
        <div class='box-gray'>
            💡 <b>Příklad:</b> IT analytik v Praze může mít vyšší mzdu než administrativní pracovník v menším městě ne proto, že by „pracoval více hodin“, ale kvůli kombinaci vzácnosti dovedností, vysoké přidané hodnotě pro firmu a vyšším životním nákladům v kraji.
        </div>
        """, unsafe_allow_html=True)

        st.divider()
        st.markdown("<div class='box-yellow'>🧮 <b>Interaktivní kalkulačka: Reálné faktory mzdy v ČR</b></div>", unsafe_allow_html=True)
        st.write("Měň parametry podle českého trhu práce a sleduj, jak obor, kraj, vzdělání a praxe ovlivňují průměrnou hrubou mzdu:")

        col_sim1, col_sim2 = st.columns(2)
        with col_sim1:
            s_obor = st.selectbox("Vyber obor:", [
                "Služby, Gastro a Maloobchod",
                "Administrativa a Zákaznická podpora",
                "Průmysl, Výroba a Řemesla",
                "Zdravotnictví a Sociální péče",
                "IT, Vývoj softwaru a Data"
            ])
            
            s_kraj = st.selectbox("Kraj (místo výkonu práce):", [
                "Praha (nejvyšší životní náklady)",
                "Jihomoravský / Středočeský / Plzeňský kraj",
                "Moravskoslezský / Ústecký / Karlovarský kraj",
                "Ostatní kraje ČR"
            ])
            
            s_vzdelani = st.radio("Dosažené vzdělání:", [
                "Výuční list / Základní",
                "SŠ s maturitou",
                "Vysokoškolské (Bc. / Mgr. / Ing.)"
            ], horizontal=True)

            s_praxe = st.select_slider("Délka praxe v oboru:", options=[
                "Absolvent (0 let)", "1–3 roky praxe", "5+ let (Senior)"
            ])

        with col_sim2:
            # Základní orientační mediány pro ČR
            base_obor = {
                "Služby, Gastro a Maloobchod": 28000,
                "Administrativa a Zákaznická podpora": 34000,
                "Průmysl, Výroba a Řemesla": 38000,
                "Zdravotnictví a Sociální péče": 42000,
                "IT, Vývoj softwaru a Data": 62000
            }[s_obor]

            koef_kraj = {
                "Praha (nejvyšší životní náklady)": 1.25,
                "Jihomoravský / Středočeský / Plzeňský kraj": 1.05,
                "Moravskoslezský / Ústecký / Karlovarský kraj": 0.90,
                "Ostatní kraje ČR": 0.95
            }[s_kraj]

            koef_vzdelani = {
                "Výuční list / Základní": 0.90,
                "SŠ s maturitou": 1.05,
                "Vysokoškolské (Bc. / Mgr. / Ing.)": 1.25
            }[s_vzdelani]

            koef_praxe = {
                "Absolvent (0 let)": 0.80,
                "1–3 roky praxe": 1.00,
                "5+ let (Senior)": 1.35
            }[s_praxe]

            odhad_mzdy = int(base_obor * koef_kraj * koef_vzdelani * koef_praxe)

            st.metric("Předpokládaná hrubá mzda (odhad v ČR)", f"{odhad_mzdy:,} Kč".replace(",", " "))

            st.markdown("##### 📌 Co z toho pro žáka vyplývá?")
            if s_praxe == "Absolvent (0 let)":
                st.info("💡 **Nástupní mzda absolventa:** Jako začátečník bez praxe začínáš na nižší částce. Praxe a spolehlivost jsou hlavní pákou pro růst mzdy v prvních 3 letech.")
            elif s_obor == "IT, Vývoj softwaru a Data":
                st.success("🔥 **Vysoká poptávka:** IT obor má dlouhodobě nedostatek lidí, což žene mzdy nahoru, ale vyžaduje neustálé samo-vzdělávání.")
            elif koef_kraj > 1.1:
                st.write("🏙️ **Pražský příplatek:** Vyšší mzda v Praze kompenzuje výrazně dražší bydlení a nájmy.")
            else:
                st.write("⚖️ **Realita trhu:** Mzda je výsledkem oboru, regionu a zkušeností – nestačí jen chodit do práce, záleží na přidané hodnotě.")

    elif selected_section_4 == "1.2 Trh práce 4.0 a AI":
        st.markdown("### 1.2 Trh práce 4.0 a AI")
        st.write("Trh práce se pod vlivem technologií mění nejrychleji v historii. Tradiční představa, že po škole nastoupíte do jedné firmy a zůstanete v ní 40 let, už neplatí.")

        st.markdown("#### Hlavní hýbatelé Trhu práce 4.0:")
        st.markdown("""
        * ⚙️ **Automatizace:** Stroje, algoritmy a roboti přebírají rutinní a opakující se činnosti.
        * 🤖 **Generativní umělá inteligence (AI):** Pomáhá psát texty, analyzovat data, překládat, kódovat, navrhovat grafiku i vyhodnocovat dokumenty.
        * 🏠 **Remote work a hybridní práce:** Práce na dálku odstraňuje hranice měst – můžete pracovat z regionu pro pražskou nebo zahraniční firmu.
        * 📲 **Platformová ekonomika (Gig Economy):** Část práce se přesouvá do aplikací a zakázkových platforem (Uber, Bolt, Foodora, Freelance portály).
        * 🌐 **Globální konkurence:** U digitálních profesí nesoutěžíte jen s kolegy ze třídy, ale s pracovníky z celého světa.
        """)

        st.markdown("""
        <div class='box-purple'>
            🤖 <b>Důležité pravidlo AI na trhu práce:</b> AI většinou nenahrazuje celé profese najednou. Častěji mění jednotlivé činnosti uvnitř profese.<br>
            <b>Platí krédo:</b> <i>„AI vás o práci nepřipraví. O práci vás připraví člověk, který s AI umí pracovat lépe než vy.“</i>
        </div>
        """, unsafe_allow_html=True)

        st.divider()
        st.markdown("<div class='box-yellow'>🧩 <b>Kvíz: Jak AI mění jednotlivé obory?</b></div>", unsafe_allow_html=True)
        
        with st.form("kviz_ai_trh"):
            q_ai1 = st.radio("Co udělá AI s profesí účetního / datového analytika?", [
                "Zruší ji úplně ze dne na den",
                "Přebere rutinní zadávání faktur, analytik se posune k poradenství a strategii",
                "Nebude mít na profesi žádný vliv"
            ])
            q_ai2 = st.radio("Jaká je největší výhoda znalosti AI nástrojů pro juniorního zaměstnance?", [
                "Může v práci 8 hodin spát a nic nedělat",
                "Zvýší svou produktivitu, zrychlí rutinní úkoly a přinese firmě vyšší hodnotu",
                "Díky AI nemusí mít žádné vzdělání ani kritické myšlení"
            ])

            if st.form_submit_button("Vyhodnotit kvíz"):
                if "Přebere rutinní zadávání" in q_ai1 and "Zvýší svou produktivitu" in q_ai2:
                    st.success("✅ Přesně tak! AI posouvá lidi od rutiny k řešení složitějších problémů.")
                else:
                    st.error("Zkus to znovu. Pamatuj, že AI nahrazuje úkoly, ne lidskou odpovědnost a kritické myšlení.")

    elif selected_section_4 == "1.3 Profese a dovednosti budoucnosti":
        st.markdown("### 1.3 Profese a dovednosti budoucnosti")
        st.write("Technické znalosti konkrétního softwaru stárnou. Co zůstává trvale cenné, jsou **hard skills (odborné dovednosti)** spojené s **soft skills (měkkými dovednostmi)**.")

        col_sk1, col_sk2 = st.columns(2)
        with col_sk1:
            st.markdown("##### 🧠 Klíčové dovednosti budoucnosti:")
            st.markdown("""
            * 🔍 **Práce s informacemi** a ověřování zdrojů (kritické myšlení),
            * 🤖 **Prompting a práce s AI nástroji**,
            * 📊 **Analytické a logické myšlení**,
            * 🎨 **Kreativita a inovativnost**,
            * 🔄 **Schopnost učit se nové věci** (Adaptabilita).
            """)
        with col_sk2:
            st.markdown("##### 🤝 Lidské dovednosti (které AI nenahradí):")
            st.markdown("""
            * 💬 **Komunikace, empatie a vyjednávání**,
            * 👥 **Týmová spolupráce a vedení lidí**,
            * 🛡️ **Etické rozhodování a morální odpovědnost**,
            * 🧘 **Resilience (odolnost vůči stresu a změnám)**.
            """)

        st.divider()
        st.markdown("<div class='box-purple'>🧪 <b>Mini-úkol: AI Rozřazovač činností u profesí</b></div>", unsafe_allow_html=True)
        st.write("Vyber profesi a zkus rozřadit její náplň práce: Co převzneme AI, co AI zrychlí a co zůstane čistě lidské?")

        profese_vyber = st.selectbox("Vyber profesi k analýze:", [
            "Vyber...",
            "Grafický designér / Marketer",
            "Praktický lékař / Sestra",
            "Učitel / Lektor",
            "Právník / Koncipient"
        ])

        if profese_vyber == "Grafický designér / Marketer":
            st.info("🤖 **AI převzneme:** Generování variant pozadí, úprava formátů bannerů, základní korektury.\n\n⚡ **AI zrychlí:** Tvorbu skic, psaní textů do reklam, návrhy vizuálních konceptů.\n\n🧠 **Lidské zůstane:** Pochopení emoce a strategie značky, osobní vztah s klientem, finální estetický úsudek.")
        elif profese_vyber == "Praktický lékař / Sestra":
            st.info("🤖 **AI převzneme:** Přepis lékařských zpráv, hlídání termínů očkování, analýzu rentgenových snímků.\n\n⚡ **AI zrychlí:** Diagnostiku vzácných chorob, vyhledávání v lékařských studiích.\n\n🧠 **Lidské zůstane:** Empatie, komunikace s pacientem, provedení zákroku, finální odpovědnost za léčbu.")
        elif profese_vyber == "Učitel / Lektor":
            st.info("🤖 **AI převzneme:** Opravování testů s výběrem odpovědí, generování příkladů na procvičení.\n\n⚡ **AI zrychlí:** Přípravu pracovních listů, překlady materiálů, tvorbu prezentací.\n\n🧠 **Lidské zůstane:** Motivace žáků, osobní mentorování, řešení konfliktů ve tříde, vysvětlení látky s ohledem na emoce.")
        elif profese_vyber == "Právník / Koncipient":
            st.info("🤖 **AI převzneme:** Prohledávání tisíců stránek zákonů a judikátů, kontrola formalit ve smlouvách.\n\n⚡ **AI zrychlí:** Návrh prvních verzí standardních smluv.\n\n🧠 **Lidské zůstane:** Obhajoba u soudu, vyjednávání s protistranou, etické posouzení sporu.")

    elif selected_section_4 == "1.4 Osobní brand a digitální stopa":
        st.markdown("### 1.4 Osobní brand a digitální stopa")
        st.markdown("""
        <div class='box-blue'>
            🔎 <b>Otázka k zamyšlení:</b> Kdyby si vás budoucí zaměstnavatel vyhledal online, co by o vás zjistil? Pomohlo by vám to, nebo uškodilo?
        </div>
        """, unsafe_allow_html=True)

        st.write("Zaměstnavatel dnes nehledá jen strohý papírový životopis. Hledá důkaz, že umíte přemýšlet, komunikovat a pracovat na sobě. **Osobní brand (osobní značka)** je obraz, který o sobě dlouhodobě vytváříte.")

        st.markdown("##### Co tvoří tvůj osobní brand:")
        st.markdown("""
        * 📄 **Profesionální Životopis (CV) a portfolio** (reálné ukázky projektů),
        * 🌐 **LinkedIn profil** nebo profesní síť,
        * 📱 **Digitální stopa** na sociálních sítích (Instagram, TikTok, Facebook, Discord),
        * 🏆 **Školní a mimoškolní projekty, dobrovolnictví, soutěže**,
        * 💬 **Reference** od předchozích zaměstnavatelů nebo učitelů.
        """)

        st.divider()
        st.markdown("<div class='box-yellow'>📋 <b>Audit tvé digitální stopy (Rychlá kontrola)</b></div>", unsafe_allow_html=True)
        st.write("Zaškrtni položky, které máš v pořádku:")

        d1 = st.checkbox("Mám uzamčené soukromé profily (Instagram/Facebook) nebo na nich nemám nevhodný obsah (alkohol, vulgarismy).")
        d2 = st.checkbox("Mám založený a vyplněný profesní profil na LinkedIn nebo online portfolio svých prací.")
        d3 = st.checkbox("Moje e-mailová adresa v životopisu je profesionální (např. jmeno.prijmeni@email.cz, ne dravec123@seznam.cz).")
        d4 = st.checkbox("Kdybych si zadal/a své jméno do Google, nevyjedou žádné kompromitující fotografie nebo komentáře.")

        score_d = sum([d1, d2, d3, d4])
        st.progress(score_d / 4)

        if score_d == 4:
            st.success("🎉 **Vynikající! Tvá digitální stopa působí profesionálně a bezpečně.**")
        elif score_d >= 2:
            st.info("👍 Dobrý základ! Podívej se na nezaškrtnutá políčka a vylepši je před posíláním první přihlášky na brigádu či práci.")
        else:
            st.warning("⚠️ **Pozor!** Zaměstnavatelé si uchazeče běžně vyhledávají. Vyčisti si veřejné profily a založ si profesionální e-mail.")

        st.divider()
        st.markdown("#### 📱 Hybridní prvek: Otestuj si profese budoucnosti")
        st.write("Naskenuj QR kód nebo klikni na tlačítko a vyzkoušej si oficiální kariérní dotazník národního systému kvalifikací:")
        
        col_qr1, col_qr2 = st.columns([1, 2])
        with col_qr1:
            st.image("https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://www.nsp.cz", caption="Kariérní kompas NSP.cz", width=150)
        with col_qr2:
            st.markdown("""
            **Kam pokračovat dále?**
            * 🔗 **[Národní soustava povolání (NSP.cz)](https://www.nsp.cz):** Databáze všech profesí v ČR vč. požadavků na vzdělání a průměrných mezd.
            * 🔗 **[Kariérní kompas](https://www.nsp.cz):** Zjisti, jaké dovednosti ti chybí pro tvou vysněnou práci.
            """)

    # =========================================================================
    # REZERVOVANÉ ELIF PRO DALŠÍ SEKCE
    # =========================================================================
    elif selected_section_4 == "2.1 HR a personalistika: co znamenají":
        st.markdown("### 2.1 HR a personalistika: co znamenají")
        st.info("Obsah podkapitoly 2.1 se připravuje...")

    elif selected_section_4 == "2.2 Nábor v éře AI":
        st.markdown("### 2.2 Nábor v éře AI")
        st.info("Obsah podkapitoly 2.2 se připravuje...")

    elif selected_section_4 == "2.3 Životopis, motivační dopis a portfolio":
        st.markdown("### 2.3 Životopis, motivační dopis a portfolio")
        st.info("Obsah podkapitoly 2.3 se připravuje...")

    elif selected_section_4 == "2.4 Pracovní smlouva, DPP a DPČ":
        st.markdown("### 2.4 Pracovní smlouva, DPP a DPČ")
        st.info("Obsah podkapitoly 2.4 se připravuje...")

    elif selected_section_4 == "2.5 Ukázka pracovní smlouvy a její náležitosti":
        st.markdown("### 2.5 Ukázka pracovní smlouvy a její povinné náležitosti")
        st.info("Obsah podkapitoly 2.5 se připravuje...")

    elif selected_section_4 == "2.6 Zkušební doba":
        st.markdown("### 2.6 Zkušební doba")
        st.info("Obsah podkapitoly 2.6 se připravuje...")

    elif selected_section_4 == "2.7 Smlouva na dobu určitou a neurčitou":
        st.markdown("### 2.7 Smlouva na dobu určitou a neurčitou")
        st.info("Obsah podkapitoly 2.7 se připravuje...")

    elif selected_section_4 == "2.8 Švarcsystém a gig economy":
        st.markdown("### 2.8 Švarcsystém a gig economy")
        st.info("Obsah podkapitoly 2.8 se připravuje...")

    elif selected_section_4 == "2.9 Red flags v inzerátech a smlouvách":
        st.markdown("### 2.9 Red flags v inzerátech a smlouvách")
        st.info("Obsah podkapitoly 2.9 se připravuje...")

    elif selected_section_4 == "3.1 Hrubá mzda, čistá mzda a superhrubé uvažování":
        st.markdown("### 3.1 Hrubá mzda, čistá mzda a superhrubé uvažování")
        st.info("Obsah podkapitoly 3.1 se připravuje...")

    elif selected_section_4 == "3.2 Nominální a reálná mzda":
        st.markdown("### 3.2 Nominální a reálná mzda")
        st.info("Obsah podkapitoly 3.2 se připravuje...")

    elif selected_section_4 == "3.3 Výplatní páska a její náležitosti":
        st.markdown("### 3.3 Výplatní páska a její náležitosti")
        st.info("Obsah podkapitoly 3.3 se připravuje...")

    elif selected_section_4 == "3.4 Výpočet čisté mzdy krok za krokem":
        st.markdown("### 3.4 Výpočet čisté mzdy krok za krokem")
        st.info("Obsah podkapitoly 3.4 se připravuje...")

    elif selected_section_4 == "3.5 Sazby pojištění, daně a náklady zaměstnavatele":
        st.markdown("### 3.5 Sazby pojištění, daně a náklady zaměstnavatele")
        st.info("Obsah podkapitoly 3.5 se připravuje...")

    elif selected_section_4 == "3.6 Slevy na dani a odčitatelné položky":
        st.markdown("### 3.6 Slevy na dani a odčitatelné položky")
        st.info("Obsah podkapitoly 3.6 se připravuje...")

    elif selected_section_4 == "3.7 Kam jdou odvody (sociální a zdravotní pojištění)":
        st.markdown("### 3.7 Kam jdou odvody")
        st.info("Obsah podkapitoly 3.7 se připravuje...")

    elif selected_section_4 == "3.8 Celková odměna za práci a vyjednávání o mzdě":
        st.markdown("### 3.8 Celková odměna za práci a vyjednávání o mzdě")
        st.info("Obsah podkapitoly 3.8 se připravuje...")

    elif selected_section_4 == "4.1 Firemní kultura a wellbeing":
        st.markdown("### 4.1 Firemní kultura a wellbeing")
        st.info("Obsah podkapitoly 4.1 se připravuje...")

    elif selected_section_4 == "4.2 Právo na odpojení a podnikavost v zaměstnání":
        st.markdown("### 4.2 Právo na odpojení a Intrapreneurship")
        st.info("Obsah podkapitoly 4.2 se připravuje...")

    elif selected_section_4 == "4.3 Upskilling a reskilling":
        st.markdown("### 4.3 Upskilling a reskilling")
        st.info("Obsah podkapitoly 4.3 se připravuje...")

    elif selected_section_4 == "5.1 Jak dát a dostat výpověď profesionálně":
        st.markdown("### 5.1 Jak dát a dostat výpověď")
        st.info("Obsah podkapitoly 5.1 se připravuje...")

    elif selected_section_4 == "5.2 Úřad práce, podpora v nezaměstnanosti a rekvalifikace":
        st.markdown("### 5.2 Úřad práce, podpora a rekvalifikace")
        st.info("Obsah podkapitoly 5.2 se připravuje...")

    elif selected_section_4 == "6.1 Praktická dílna (Aktivity 1–5)":
        st.markdown("### 6.1 Praktická dílna")
        st.info("Obsah praktické dílny se připravuje...")

    elif selected_section_4 == "7.1 Případové studie z praxe":
        st.markdown("### 7.1 Případové studie z praxe")
        st.info("Případové studie se připravují...")

    elif selected_section_4 == "7.2 Slovníček, rychlé opakování a prověrka":
        st.markdown("### 7.2 Slovníček, rychlé opakování a prověrka kapitoly")
        st.info("Závěrečné opakování se připravuje...")

    else:
        st.info("Obsah pro tuto podkapitolu se právě připravuje. Pokračujte ve výběru výše.")
