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

    # <i class='fi fi-bs-bookmark'></i> PŘEHLED A NAVIGACE KAPITOLOU
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

    # <i class='fi fi-bs-bookmark'></i> JEDNOTNÁ NABÍDKA PODKAPITOL
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
        "5.3 Co dělat, když... (Krizový trenažér)",
        "6.1 Praktická dílna (Aktivity 1–5)",
        "7.1 Případové studie z praxe",
        "7.2 Slovníček, rychlé opakování a prověrka"
    ]
    
    selected_section_4 = st.markdown("<i class='fi fi-bs-bookmark'></i> <strong>Přechod na podkapitolu:</strong>", unsafe_allow_html=True)
    st.selectbox("Přechod na podkapitolu:", section_options_4, index=0, label_visibility="collapsed")
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
        | ⚖️ **Odpovědnost** | Čím větší dopad má chyba, tím vyšší jsou nároky i mzda. | Lékař, pilot, hlavní účetní, jeřábník. |
        | 🚀 **Produktivita a přidaná hodnota** | Kolik hodnoty či úspor dokáže člověk vytvořit za jednotku času. | Programátor, který automatizuje proces pro tisíce uživatelů. |
        | ⚠️ **Riziko a náročnost** | Fyzické, psychické nebo bezpečnostní nároky práce. | Práce ve zdravotnictví, výškové práce, směnný provoz. |
        | 💬 **Vyjednávací síla a region** | Místo výkonu práce, praxe, vzdělání a schopnost doložit výsledky. | Praha vs. menší regiony, junior vs. seniorní specialista. |
        """)

        st.markdown("""
        <div class='box-red'>
            ⚠️ <b>Zlaté pravidlo trhu práce:</b> V pracovních inzerátech, na pohovorech i v pracovní smlouvě se <b>VŽDY uvádí HRUBÁ MZDA</b>, nikoli čistá! Čistá mzda závisí na vašich osobních poměrech (zda uplatňujete slevu na studenta, na děti, invaliditu apod.), které zaměstnavatel předem nezná.
        </div>
        """, unsafe_allow_html=True)

        st.divider()
        st.markdown("<div class='box-yellow'>🧮 <b>Interaktivní kalkulačka: Reálné faktory mzdy v ČR</b></div>", unsafe_allow_html=True)
        st.write("Vyber obor, přesný kraj, vzdělání a praxi. Kalkulačka vychází z reálných mzdových mediánů v České republice:")

        col_sim1, col_sim2 = st.columns(2)
        with col_sim1:
            s_obor = st.selectbox("Vyber obor / odvětví:", [
                "Gastro, Služby a Úklid",
                "Maloobchod, Prodej a Pokladní",
                "Doprava, Logistika a Sklad",
                "Administrativa, HR a Zákaznický servis",
                "Řemesla a Stavebnictví",
                "Školství, Vzdělávání a Věda",
                "Výroba, Strojírenství a Elektrotechnika",
                "Marketing, Média a PR",
                "Zdravotnictví a Sociální péče",
                "Finance, Účetnictví a Bankovnictví",
                "IT, Vývoj softwaru a Kyberbezpečnost",
                "Management a Vedení týmů"
            ])
            
            s_kraj = st.selectbox("Kraj (místo výkonu práce):", [
                "Hl. m. Praha",
                "Středočeský kraj",
                "Jihomoravský kraj",
                "Plzeňský kraj",
                "Pardubický kraj",
                "Královéhradecký kraj",
                "Jihočeský kraj",
                "Kraj Vysočina",
                "Liberecký kraj",
                "Olomoucký kraj",
                "Zlínský kraj",
                "Moravskoslezský kraj",
                "Ústecký kraj",
                "Karlovarský kraj"
            ])
            
            s_vzdelani = st.radio("Dosažené vzdělání:", [
                "Výuční list / Základní",
                "SŠ s maturitou",
                "Vysokoškolské (Bc. / Mgr. / Ing.)"
            ], horizontal=True)

            s_praxe = st.selectbox("Délka praxe v oboru:", [
                "Absolvent (bez praxe)",
                "Junior (1–3 roky praxe)",
                "Medior (3–5 let praxe)",
                "Senior / Expert (5+ let praxe)"
            ])

        with col_sim2:
            base_obor = {
                "Gastro, Služby a Úklid": 27000,
                "Maloobchod, Prodej a Pokladní": 30000,
                "Doprava, Logistika a Sklad": 35000,
                "Administrativa, HR a Zákaznický servis": 36000,
                "Řemesla a Stavebnictví": 37000,
                "Školství, Vzdělávání a Věda": 39000,
                "Výroba, Strojírenství a Elektrotechnika": 40000,
                "Marketing, Média a PR": 42000,
                "Zdravotnictví a Sociální péče": 44000,
                "Finance, Účetnictví a Bankovnictví": 48000,
                "IT, Vývoj softwaru a Kyberbezpečnost": 65000,
                "Management a Vedení týmů": 70000
            }[s_obor]

            koef_kraj = {
                "Hl. m. Praha": 1.25,
                "Středočeský kraj": 1.08,
                "Jihomoravský kraj": 1.05,
                "Plzeňský kraj": 1.02,
                "Pardubický kraj": 0.98,
                "Královéhradecký kraj": 0.97,
                "Jihočeský kraj": 0.96,
                "Kraj Vysočina": 0.95,
                "Liberecký kraj": 0.95,
                "Olomoucký kraj": 0.93,
                "Zlínský kraj": 0.92,
                "Moravskoslezský kraj": 0.92,
                "Ústecký kraj": 0.90,
                "Karlovarský kraj": 0.88
            }[s_kraj]

            koef_vzdelani = {
                "Výuční list / Základní": 0.90,
                "SŠ s maturitou": 1.05,
                "Vysokoškolské (Bc. / Mgr. / Ing.)": 1.25
            }[s_vzdelani]

            koef_praxe = {
                "Absolvent (bez praxe)": 0.80,
                "Junior (1–3 roky praxe)": 1.00,
                "Medior (3–5 let praxe)": 1.18,
                "Senior / Expert (5+ let praxe)": 1.35
            }[s_praxe]

            odhad_mzdy = int(base_obor * koef_kraj * koef_vzdelani * koef_praxe)

            st.metric("Odhadovaná HRUBÁ mzda v inzerátu", f"{odhad_mzdy:,} Kč".replace(",", " "))

            st.markdown("##### <i class='fi fi-bs-bookmark'></i> Co z tohoto odhadu pro žáka vyplývá?")
            if s_praxe == "Absolvent (bez praxe)":
                st.info("💡 **Nástupní mzda absolventa:** Jako začátečník bez praxe začínáš na nižší částce (cca 80 % průměru). Získaná praxe a spolehlivost jsou hlavní pákou pro růst mzdy v prvních letech.")
            elif s_obor in ["IT, Vývoj softwaru a Kyberbezpečnost", "Management a Vedení týmů"]:
                st.success("🔥 **Vysoká poptávka / Odpovědnost:** Tyto obory nabízejí nadprůměrné mzdy z důvodu kritického nedostatku odborníků a vysoké přidané hodnotě pro firmu.")
            elif s_kraj == "Hl. m. Praha":
                st.write("🏙️ **Pražský příplatek:** Mzdy v Praze bývají o 20–25 % vyšší než celostátní průměr, což kompenzuje výrazně dražší bydlení a životní náklady.")
            else:
                st.write("⚖️ **Regionální realita:** Rozdíly v mzdách mezi kraji odrážejí strukturu místního průmyslu a životní náklady v daném regionu.")

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
            "Právník / Koncipient",
            "Účetní / Daňový poradce",
            "Programátor / IT vývojář",
            "Řidič kamionu / Kurýr",
            "Kuchař / Číšník",
            "Strojírenský technik / Řemeslník",
            "Realitní makléř / Obchodník",
            "Zákaznická podpora / Call centrum",
            "Novinář / Copywriter"
        ])

        if profese_vyber == "Grafický designér / Marketer":
            st.info("🤖 **AI přebere:** Generování variant pozadí, úpravu formátů bannerů, základní gramatické korektury.\n\n⚡ **AI zrychlí:** Tvorbu prvotních skic, generování textových konceptů pro reklamu.\n\n🧠 **Lidské zůstane:** Pochopení emoce a strategie značky, osobní vztah s klientem, finální estetické rozhodnutí.")
        elif profese_vyber == "Praktický lékař / Sestra":
            st.info("🤖 **AI přebere:** Přepis lékařských zpráv, hlídání termínů preventivních prohlídek, prvotní třídění příznaků.\n\n⚡ **AI zrychlí:** Diagnostiku vzácných chorob, vyhledávání v tisících lékařských studií.\n\n🧠 **Lidské zůstane:** Empatie, lidský přístup, fyzické provedení zákroku, finální morální i právní odpovědnost za léčbu.")
        elif profese_vyber == "Učitel / Lektor":
            st.info("🤖 **AI přebere:** Opravování uzavřených testů, generování variací příkladů na procvičení.\n\n⚡ **AI zrychlí:** Přípravu pracovních listů, překlady cizojazyčných podkladů, tvorbu vizuálních prezentací.\n\n🧠 **Lidské zůstane:** Osobní motivace žáků, mentoring, řešení konfliktů ve třídě, vysvětlení látky podle emocí a potřeb žáka.")
        elif profese_vyber == "Právník / Koncipient":
            st.info("🤖 **AI přebere:** Prohledávání tisíců stránek zákonů a judikátů, kontrolu povinných náležitostí ve smlouvách.\n\n⚡ **AI zrychlí:** Návrh prvních verzí standardních smluv a podání.\n\n🧠 **Lidské zůstane:** Obhajoba a vystupování u soudu, vyjednávání s protistranou, etické posouzení sporu.")
        elif profese_vyber == "Účetní / Daňový poradce":
            st.info("🤖 **AI přebere:** Vytěžování dat z faktur, automatické párování plateb v bance, rutina účetních závěrek.\n\n⚡ **AI zrychlí:** Kontrolu neobvyklých transakcí, vyhledávání v daňové legislativě.\n\n🧠 **Lidské zůstane:** Daňové plánování a strategie pro firmu, osobní jednání s klientem a finančním úřadem.")
        elif profese_vyber == "Programátor / IT vývojář":
            st.info("🤖 **AI přebere:** Psaní opakujícího se kódu (boilerplate), hledání syntaktických chyb, testování.\n\n⚡ **AI zrychlí:** Tvorbu dokumentace, učení se nových programovacích knihoven.\n\n🧠 **Lidské zůstane:** Návrh celkové architektury systému, bezpečnostní rozhodnutí, pochopení reálných potřeb uživatele.")
        elif profese_vyber == "Řidič kamionu / Kurýr":
            st.info("🤖 **AI přebere:** Autonomní řízení na dálnicích (výhledově), optimalizaci trasy podle dopravy.\n\n⚡ **AI zrychlí:** Vyřizování celních dokladů, plánování nakládek.\n\n🧠 **Lidské zůstane:** Řešení krizových situací v městském provozu, ruční nakládka a předání zboží zákazníkovi do ruky.")
        elif profese_vyber == "Kuchař / Číšník":
            st.info("🤖 **AI přebere:** Přijímání objednávek přes aplikace, hlídání minimálních zásob surovin v kuchyni.\n\n⚡ **AI zrychlí:** Normování receptur, výpočet kalorií a alergiků v menu.\n\n🧠 **Lidské zůstane:** Chuťové ladění jídel, kulinářská kreativita, vytvoření příjemné atmosféry v restauraci.")
        elif profese_vyber == "Strojírenský technik / Řemeslník":
            st.info("🤖 **AI přebere:** Diagnostiku závad podle senzorů vibrací a teploty stroje.\n\n⚡ **AI zrychlí:** Kreslení 3D modelů dílů, kalkulaci spotřeby materiálu.\n\n🧠 **Lidské zůstane:** Fyzická montáž v nestandardních podmínkách, manuální zručnost, adaptace na místě.")
        elif profese_vyber == "Realitní makléř / Obchodník":
            st.info("🤖 **AI přebere:** Psaní textů inzerátů, generování virtuálních prohlídek nemovitostí.\n\n⚡ **AI zrychlí:** Oceňování nemovitostí podle dat z katastru a trhu.\n\n🧠 **Lidské zůstane:** Osobní prohlídky, budování důvěry, vyjednávání o ceně mezi kupujícím a prodávajícím.")
        elif profese_vyber == "Zákaznická podpora / Call centrum":
            st.info("🤖 **AI přebere:** Odpovídání na 80 % běžných dotazů (kde je zásilka, jak vrátit zboží).\n\n⚡ **AI zrychlí:** Souhrn historie zákazníka před předáním živému operátorovi.\n\n🧠 **Lidské zůstane:** Řešení emotivních a složitých reklamací, empatie při problému zákazníka.")
        elif profese_vyber == "Novinář / Copywriter":
            st.info("🤖 **AI přebere:** Generování krátkých zpráv o sportovních výsledcích nebo kurzech měn.\n\n⚡ **AI zrychlí:** Přepis rozhovorů z audia, rešerše podkladů z více zdrojů.\n\n🧠 **Lidské zůstane:** Investigativní práce na místě, rozhovory s lidmi z očí do očí, kritické ověřování faktů.")

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
    # SEKCE 2: HRA PODLE PRAVIDEL: HR, ZÍSKÁNÍ PRÁCE A PRACOVNÍ PRÁVO
    # =========================================================================
    elif selected_section_4 == "2.1 HR a personalistika: co znamenají":
        st.markdown("### 2.1 HR a personalistika: co znamenají")
        st.markdown("""
        <div class='box-blue'>
            ⚖️ <b>Základní otázka:</b> Jak získat práci, porozumět roli HR a zároveň se nenechat nachytat na neférové podmínky?
        </div>
        """, unsafe_allow_html=True)

        st.write("**HR** znamená *Human Resources* (lidské zdroje). V češtině používáme pojem **personalistika**. Jde o oblast, která řeší kompletní péči o lidi ve firmě: od vyhledání uchazečů přes smlouvy, zaškolení, hodnocení a odměňování až po ukončení pracovního poměru.")

        st.markdown("#### Co HR ve firmě obvykle řeší:")
        st.markdown("""
        | Oblast HR | Co znamená | Příklad z praxe |
        | :--- | :--- | :--- |
        | 🔍 **Nábor a výběr** | Hledání vhodných uchazečů a vedení výběrového řízení. | Pracovní inzerát, pohovor, testovací úkol. |
        | 🚀 **Onboarding** | Zaškolení a začlenění nového člověka do firmy. | První den v práci, úvodní školení, přidělení mentora. |
        | 📄 **Pracovní dokumentace** | Smlouvy, dohody, mzdové výměry, interní pravidla. | Pracovní smlouva, DPP, DPČ, dodatky ke smlouvě. |
        | 💵 **Odměňování a benefity** | Nastavení mzdy, bonusů, benefitů a forem odměny. | Mzda, roční prémie, stravenky, home office. |
        | 📈 **Hodnocení a rozvoj** | Zpětná vazba, plnění cílů, vzdělávání a kariérní růst. | Hodnoticí rozhovor, odborný kurz, plán rozvoje. |
        | 🤝 **Firemní kultura** | Způsob komunikace, spolupráce a řešení problémů. | Atmosféra v týmu, pravidla komunikace, řešení konfliktů. |
        | 🚪 **Offboarding** | Profesionální proces odchodu zaměstnance z firmy. | Výstupní pohovor, předání práce, zápočtový list. |
        """)

        st.divider()
        st.markdown("<div class='box-yellow'>🧪 <b>Mini-úkol: Detektiv firemní kultury z inzerátu</b></div>", unsafe_allow_html=True)
        st.write("Zaměstnavatelé se často snaží znít atraktivně, ale mezi řádky lze vyčíst, jaká je ve firmě reálná atmosféra. Vyber inzerát a odhal jeho skutečný význam:")

        inzerat_typ = st.radio("Vyber znění inzerátu k analýze:", [
            "1️⃣ 'Hledáme dynamického nindžu do mladého kolektivu! Nabízíme práci pod tlakem, prémie dle výkonu a multisportku.'",
            "2️⃣ 'Hledáme juniorního účetního. Nabízíme 38 000 Kč hrubého, zkušební dobu 3 měsíce, fixní pracovní dobu a 25 dní dovolené.'",
            "3️⃣ 'Atraktivní výdělek až 100 000 Kč měsíčně! Žádný šéf, svoboda. Nutné vlastní IČO, zápisné 2 000 Kč za školení.'",
            "4️⃣ 'Jsme rodinná firma s tradicí. Hledáme loajálního pracovníka, který se nebojí vzít za práci. Odměna dohodou na pohovoru.'",
            "5️⃣ 'Do startupu hledáme rockstar vývojáře! Neomezená dovolená, fotbálek v kanclu, pizza zdarma, práce v rychlém tempu, 10h denně není problém.'"
        ])

        if inzerat_typ.startswith("1️⃣"):
            st.warning("⚠️ **Fráze a toxická kultura:** Slova jako 'nindža' nebo 'práce pod tlakem' často zakrývají chaos, obrovský stres a neplacené přesčasy. Multisportka nevyváží vyhoření.")
        elif inzerat_typ.startswith("2️⃣"):
            st.success("✅ **Profesionální inzerát:** Jasný, stručný, transparentní. Uvádí konkrétní hrubou mzdu, typ úvazku, nárok na dovolenou i očekávání. Tady HR hraje fér.")
        elif inzerat_typ.startswith("3️⃣"):
            st.error("🚨 **Kritický RED FLAG:** Slib pohádkových příjmů, nutnost vlastního IČO pro juniora a poplatek předem za školení = znak nelegálního Švarcsystému nebo letadla!")
        elif inzerat_typ.startswith("4️⃣"):
            st.info("🤔 **Riziko zneužití:** 'Rodinná firma' a 'nebojí se vzít za práci' často v překladu znamená: děláte práci za 3 lidi. A chybějící mzda ukazuje neochotu být transparentní.")
        elif inzerat_typ.startswith("5️⃣"):
            st.warning("🍕 **Past na mladé (Hustle culture):** Pizza a fotbálek znějí super, ale '10h denně není problém' a 'rockstar' znamená, že tam necháte duši a osobní život. Benefity mají jen udržet lidi déle v kanceláři.")

    elif selected_section_4 == "2.2 Nábor v éře AI":
        st.markdown("### 2.2 Nábor v éře AI")
        st.write("Nábor u větších firem dnes často nezačíná u člověka. Životopisy nejdříve procházejí přes **ATS (Applicant Tracking System)** — software, který automaticky filtruje uchazeče podle klíčových slov a požadavků z inzerátu.")

        st.markdown("##### <i class='fi fi-bs-bookmark'></i> Jak uspět při náboru řízeném AI / ATS:")
        st.markdown("""
        * 📄 **Přehledný formát:** Používejte standardní písmo, jasné nadpisy a formát PDF (vyhněte se složitým grafickým sloupcům, které ATS nepřečte).
        * 🔑 **Klíčová slova:** Názvy dovedností v CV přizpůsobte přesně slovům v inzerátu (např. 'pokročilý Excel', 'angličtina B2').
        * 🎯 **Mírná úprava na míru:** Neposílejte jeden obecný životopis na 20 různých pozic.
        * 🖼️ **Portfolio jako trumf:** Konkrétní ukázka vaší práce (web, grafika, text) přesvědčí personalistu víc než obecná tvrzení.
        """)

        st.divider()
        st.markdown("<div class='box-purple'>🤖 <b>Interaktivní trenažér: Pohovor nanečisto s AI</b></div>", unsafe_allow_html=True)
        st.write("Chceš si vyzkoušet pohovor na jakoukoliv brigádu nebo pozici nanečisto? Zkopíruj si tento speciální prompt a vlož ho do ChatGPT nebo Claude:")

        pozice_input = st.text_input("Zadej pozici, na kterou se chceš připravit (např. Prodavač, Junior vývojář, Asistent/ka):", value="Prodavač v e-shopu")

        prompt_text = f"Chovej se jako přísný, ale férový HR manažer. Ucházím se o pozici {pozice_input}. Ptej se mě postupně na otázky jako u reálného pracovního pohovoru (vždy jen jedna otázka najednou, čekej na mou odpověď). Po 5. mé odpovědi pohovor ukonči a dej mi detailní zpětnou vazbu: co bylo přesvědčivé, v čem jsem chyboval/a a jak bych mohl/a své odpovědi zlepšit."

        # Vizuálně odlišený box se zalamováním textu (žádné scrollování)
        st.markdown(f"""
        <div style="background-color: #f8f9fa; padding: 15px; border-left: 5px solid #8b5cf6; border-radius: 5px; font-family: monospace; font-size: 1.1em; color: #333; white-space: pre-wrap; word-wrap: break-word; line-height: 1.5;">
        {prompt_text}
        </div>
        """, unsafe_allow_html=True)
        
        st.caption("💡 Tip: Označ text výše, zkopíruj (Ctrl+C / Cmd+C) a vlož ho rovnou do svého oblíbeného AI chatu.")

    elif selected_section_4 == "2.3 Životopis, motivační dopis a portfolio":
        st.markdown("### 2.3 Životopis, motivační dopis a portfolio")
        st.write("Dobré materiály nejsou seznamem všeho, co jste v životě dělali. Jsou jasnou odpovědí na otázku: **Proč se hodím právě na tuto konkrétní pozici?**")

        st.markdown("#### 📄 Vzorový strukturovaný životopis")
        st.write("Podívejte se na reálnou ukázku profesionálně zpracovaného strukturovaného životopisu:")

        # Načtení vkládaného obrázku (s elegantním HTML záložním náhledem)
        try:
            st.image("ukazka_zivotopisu.png", caption="Vzorový strukturovaný životopis (Ing. Petr Novák)", use_container_width=True)
        except:
            st.markdown("""
            <div style="background-color: #ffffff; padding: 25px; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; color: #1e293b; margin-bottom: 20px;">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; border-bottom: 2px solid #0284c7; padding-bottom: 15px; margin-bottom: 15px;">
                    <div>
                        <h2 style="margin: 0; color: #0f172a; font-size: 1.5rem;">ING. PETR NOVÁK</h2>
                        <h4 style="margin: 5px 0 0 0; color: #0284c7; font-size: 1rem; font-weight: 600;">STRUKTUROVANÝ ŽIVOTOPIS</h4>
                    </div>
                    <div style="background-color: #e2e8f0; width: 70px; height: 85px; border-radius: 4px; display: flex; align-items: center; justify-content: center; font-size: 0.75rem; color: #64748b;">[ FOTO ]</div>
                </div>
                <div style="margin-bottom: 15px;">
                    <strong style="color: #0284c7; font-size: 0.9rem;"><i class='fi fi-bs-bookmark'></i> OSOBNÍ A KONTAKTNÍ ÚDAJE</strong><br>
                    <small><b>Telefon:</b> +420 777 123 456 | <b>E-mail:</b> petr.novak@email.cz | <b>Adresa:</b> Praha | <b>LinkedIn:</b> linkedin.com/in/petr-novak</small>
                </div>
                <div style="margin-bottom: 15px;">
                    <strong style="color: #0284c7; font-size: 0.9rem;">💼 PRACOVNÍ ZKUŠENOSTI</strong>
                    <div style="margin-top: 5px; font-size: 0.85rem;">
                        <b>01/2020 – DOSUD: PROJEKTOVÝ MANAŽER</b><br>
                        • Vedení týmů, plánování a kontrola projektů<br>
                        • Příprava smluvních podkladů a rozpočtů | Komunikace se zákazníky<br>
                        <b>06/2016 – 12/2019: ASISTENT PROJEKTŮ</b>
                    </div>
                </div>
                <div style="margin-bottom: 15px;">
                    <strong style="color: #0284c7; font-size: 0.9rem;">🎓 VZDĚLÁNÍ</strong>
                    <div style="margin-top: 5px; font-size: 0.85rem;">
                        <b>2011 – 2016: Vysokoškolské (VŠE v Praze)</b> — Obor Podniková ekonomika a management (Titul Ing.)<br>
                        <b>2007 – 2011: Středoškolské</b> — Gymnázium Jana Nerudy, Praha
                    </div>
                </div>
                <div>
                    <strong style="color: #0284c7; font-size: 0.9rem;">🛠️ DOVEDNOSTI A ZNALOSTI</strong>
                    <div style="margin-top: 5px; font-size: 0.85rem;">
                        • <b>Jazyky:</b> Čeština (rodilý mluvčí), Angličtina (C1), Němčina (B2)<br>
                        • <b>PC znalosti:</b> MS Office (pokročilý), SAP (základní) | <b>Řidičský průkaz:</b> Skupina B
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.divider()
        st.markdown("#### 🔍 Proč tento životopis funguje a na co si dát pozor")
        
        st.markdown("""
        | Část životopisu | Proč je důležitá | Na co si dát pozor |
        | :--- | :--- | :--- |
        | 👤 **Hlavička a kontakt** | Umožňuje okamžitý kontakt a profesionální dojem. | E-mail musí být profesionální (jmeno.prijmeni@email.cz), ne přezdívka z dětství. |
        | 📸 **Fotografie** | Vytváří první osobní dojem (není povinná, ale vhodná). | Pouze profesionální portrét s neutrálním pozadím — ne selfie ani fotka z párty! |
        | 💼 **Pracovní zkušenosti** | Řazeno **chronologicky od nejnovější po nejstarší**. | Vždy uveďte konkrétní náplň práce v odrážkách, ne jen název pozice. |
        | 🎓 **Vzdělání** | Dokládá kvalifikaci (u absolventů nahrazuje chybějící praxi). | Uveďte název školy, obor a případně klíčové školní projekty. |
        | 🧠 **Dovednosti a jazyky** | Pomáhá HR i automatickým systémům (ATS) rychle posoudit shodu. | Uvádějte reálné úrovně (např. B2, C1). Nepoužívejte vymyslená procenta (např. 'PC 100 %'). |
        | 📜 **GDPR doložka** | Uděluje souhlas se zpracováním osobních údajů pro nábor. | V ČR se vyžaduje u většiny větších firem a nadnárodních korporací. |
        """)

        st.markdown("""
        <div class='box-red'>
            🚩 <b>Co do životopisu RADĚJI NEPATŘÍ:</b> Neprofesionální e-mail, rodné číslo, rodinný stav, pravopisné chyby, dlouhé souvislé odstavce bez odrážek a záliby, které nijak nesouvisí s pozicí.
        </div>
        """, unsafe_allow_html=True)

        st.divider()
        st.markdown("<div class='box-yellow'>🧪 <b>Kontrolor životopisu: Odhal chyby v přihlášce</b></div>", unsafe_allow_html=True)
        
        with st.form("form_cv_check"):
            st.write("Vyber, které z následujících prvků v životopisu jsou CHYBNÉ:")
            cv_c1 = st.checkbox("E-mail: dravec_ostrava_69@seznam.cz")
            cv_c2 = st.checkbox("Odrážka u praxe: 'Koordinace 4členného týmu při organizaci školního plesu'")
            cv_c3 = st.checkbox("Dovednosti: 'Práce na PC - 100 %, Angličtina - 100 %'")
            cv_c4 = st.checkbox("Fotografie: Selfie v zrcadle v tělocvičně")

            if st.form_submit_button("Zkontrolovat životopis"):
                if cv_c1 and not cv_c2 and cv_c3 and cv_c4:
                    st.success("🎉 **Skvěle! Odhalil/a jsi všechny chyby!**\n* Neformální e-mail působí neprofesionálně.\n* Hodnocení v procentech (100 %) je subjektivní nesmysl (raději uvádějte úrovně A1-C2 nebo konkrétní dovednosti).\n* Selfie v zrcadle do CV nepatří.")
                else:
                    st.error("Něco jsi přehlédl/a. Správné odrážky s výsledky (jako u plesu) jsou v pořádku, ale neformální e-maily, procentuální stupnice a selfie jsou chyby!")

    elif selected_section_4 == "2.4 Pracovní smlouva, DPP a DPČ":
        st.markdown("### 2.4 Pracovní smlouva, DPP a DPČ")
        st.markdown("""
        <div class='box-blue'>
            ⚖️ <b>Základní princip:</b> V ČR existuje více forem práce. Každá má jiné výhody, zákonné povinnosti, odvody a míru právní ochrany.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("#### 📝 Pracovní smlouva a její 3 povinné náležitosti")
        st.write("Abyste byli chráněni zákonem, **pracovní smlouva musí být vždy uzavřena písemně**! Ze zákona (Zákoníku práce) v ní MUSÍ být obsaženy tyto tři základní věci. Pokud byť jen jedna chybí, je smlouva neplatná:")

        st.markdown("""
        1. 🏢 **Druh práce** (co přesně budete dělat, např. 'skladník', 'programátor', 'prodavač').
        2. 📍 **Místo výkonu práce** (kde budete pracovat, např. 'Praha' nebo konkrétní pobočka firmy).
        3. 📅 **Den nástupu do práce** (od kdy pracovní poměr oficiálně vzniká, např. '1. září 2024').
        """)

        st.markdown("""
        <div class='box-red'>
            🚨 <b>Klíčové pravidlo: Mzda NEMUSÍ být v pracovní smlouvě!</b><br>
            Možná vás to překvapí, ale výše výplaty není povinnou součástí pracovní smlouvy. Zaměstnavatel vám ji může dát jako samostatný dokument, kterému se říká <b>mzdový výměr</b>.<br><br>
            <b>Zásadní rozdíl pro vás jako zaměstnance:</b><br>
            • Pokud je mzda napsaná <b>přímo ve smlouvě</b>, zaměstnavatel vám ji nemůže jednostranně snížit. S jakoukoliv změnou byste museli písemně souhlasit.<br>
            • Pokud dostanete samostatný <b>mzdový výměr</b>, může zaměstnavatel mzdu jednostranně změnit i bez vašeho souhlasu (i snížit, nesmí ale jít pod limit tzv. zaručené minimální mzdy).
        </div>
        """, unsafe_allow_html=True)

        st.divider()
        st.markdown("#### ⚖️ Srovnání brigádních dohod: DPP vs. DPČ")
        
        st.markdown("""
        | Oblast | DPP (Dohoda o provedení práce) | DPČ (Dohoda o pracovní činnosti) |
        | :--- | :--- | :--- |
        | ⏱️ **Hodinový limit** | Max. **300 hodin ročně** u jednoho zaměstnavatele. | Práce nesmí překročit v průměru **20 hodin týdně** (polovinu úvazku). |
        | 📜 **Písemná forma** | **Musí být vždy písemná!** (Ústní dohoda je neplatná). | **Musí být vždy písemná!** |
        | 🏥 **Odvody pojištění** | Odvádí se až při překročení měsíčního limitu příjmu. | Odvádí se při překročení hranice rozhodného příjmu. |
        | 🏖️ **Nárok na dovolenou** | **ANO**, při odpracování dostatečného počtu hodin. | **ANO**, při splnění zákonných podmínek. |
        | 🚪 **Ukončení** | Lze ukončit písemnou výpovědí s **15denní lhůtou**. | Lze ukončit písemnou výpovědí s **15denní lhůtou**. |
        """)

        st.markdown("""
        <div class='box-green'>
            💡 <b>Rychlá pomůcka do praxe:</b><br>
            • <b>DPP</b> se hodí na nárazovou brigádu (např. 2 týdny v létě na festivalu nebo nárazový sběr dat).<br>
            • <b>DPČ</b> se hodí na pravidelnou celoroční brigádu při škole (např. 2 odpoledne týdně v kavárně).
        </div>
        """, unsafe_allow_html=True)
    elif selected_section_4 == "2.5 Ukázka pracovní smlouvy a její náležitosti":
        st.markdown("### 2.5 Pracovní smlouva: Povinné náležitosti a rizika")
        
        st.write("Pracovní smlouva je nejdůležitější dokument vašeho pracovního života. Musí být **vždy uzavřena písemně** a vyhotovena ve dvou stejnopisech (jeden pro vás, jeden pro firmu). Zákoník práce vás chrání, ale jen tehdy, když víte, co podepisujete.")

        st.markdown("#### 📝 3 povinné údaje, bez kterých je smlouva neplatná:")
        st.write("Pokud ve smlouvě chybí byť jen jedna z těchto tří věcí, smlouva oficiálně nevznikla:")
        
        col_s1, col_s2, col_s3 = st.columns(3)
        with col_s1:
            st.markdown("##### 1️⃣ Druh práce")
            st.write("Co přesně budete dělat (např. 'Specialista zákaznické podpory'). Pokud je definice příliš široká, nadřízený vás může nutit dělat cokoliv – od administrativy po úklid.")
        with col_s2:
            st.markdown("##### 2️⃣ Místo výkonu")
            st.write("Kde budete pracovat (např. 'Pobočka Brno, Masarykova 12'). Pokud podepíšete místo 'Česká republika', může vás firma ze dne na den přeložit na druhý konec země.")
        with col_s3:
            st.markdown("##### 3️⃣ Den nástupu")
            st.write("Přesné datum (např. 1. 9. 2026). Od tohoto dne vám vznikají práva a povinnosti, i kdybyste smlouvu podepsali o měsíc dříve.")

        st.markdown("""
        <div class='box-red'>
            🚨 <b>Klíčový omyl: Mzda NEMUSÍ být přímo v pracovní smlouvě!</b><br>
            Plat nebo mzda často není v textu smlouvy, ale na odděleném papíru zvaném <b>mzdový výměr</b>. Proč to firmy dělají?<br>
            • Co je ve <b>smlouvě</b>, to lze změnit POUZE s vaším písemným souhlasem (případně dodatkem ke smlouvě).<br>
            • <b>Mzdový výměr</b> může firma jednostranně změnit i bez vás (může vám mzdu snížit až na hranici zaručené minimální mzdy).
        </div>
        """, unsafe_allow_html=True)

        st.divider()
        st.markdown("<div class='box-yellow'>🛠️ <b>Interaktivní dílna: Sestav a zkontroluj smlouvu</b></div>", unsafe_allow_html=True)
        st.write("Navrhni parametry své pracovní smlouvy a zjisti, jaké výhody nebo skrytá rizika tvá volba přináší:")

        with st.form("form_smlouva"):
            f_druh = st.selectbox("1. Jak specifikuješ druh práce?", [
                "Přesná pozice: 'Specialista marketingu a správy sociálních sítí'",
                "Všeobecná pozice: 'Pracovník provozu dle potřeb zaměstnavatele'"
            ])
            
            f_misto = st.selectbox("2. Jak určité bude místo výkonu práce?", [
                "Přesné místo: 'Kancelář Plzeň, Květná 15'",
                "Široké místo: 'Všechny pobočky zaměstnavatele v ČR'"
            ])
            
            f_mzda = st.radio("3. Kde chceš mít uvedenou svou sjednanou mzdu (45 000 Kč)?", [
                "Přímo v textu Pracovní smlouvy",
                "Na samostatném Mzdovém výměru"
            ])
            
            submit_smlouva = st.form_submit_button("🔍 Vyhodnotit právní bezpečnost smlouvy")

        if submit_smlouva:
            st.markdown("##### 📊 Rozbor tvé smlouvy:")
            
            # Vyhodnocení druhu práce
            if "Specialista" in f_druh:
                st.success("✅ **Druh práce OK:** Máš jasně vymezené kompetence. Zaměstnavatel ti nemůže nakázat činnosti, které nesouvisí s marketingem.")
            else:
                st.error("⚠️ **Riziko u druhu práce:** Formulace 'dle potřeb' dává firmě možnost nutit tě do úklidu, skladu i cizí práce bez nároku na příplatek.")

            # Vyhodnocení místa
            if "Plzeň" in f_misto:
                st.success("✅ **Místo práce OK:** Pracuješ na konkrétní adrese. Změna pobočky do jiného města by vyžadovala tvůj písemný souhlas.")
            else:
                st.error("⚠️ **Riziko u místa:** Při volbě 'všechny pobočky v ČR' tě firma může poslat na služební cestu či přeložit kamkoliv bez nároku na kompenzaci.")

            # Vyhodnocení mzdy
            if "Přímo v textu" in f_mzda:
                st.success("🔒 **Maximální garance mzdy:** Mzda je pevně zakotvena ve smlouvě. Firma ti ji nemůže snížit, ani kdyby se jí nedařilo.")
            else:
                st.info("ℹ️ **Standardní praxe (Mzdový výměr):** Je to běžné, ale pozor – zaměstnavatel ti může mzdovým výměrem mzdu do budoucna jednostranně snížit.")

    elif selected_section_4 == "2.6 Zkušební doba":
        st.markdown("### 2.6 Zkušební doba: Pravidla a ochrana")
        st.write("Zkušební doba slouží k tomu, aby si obě strany vyzkoušely, zda jim spolupráce vyhovuje. Během ní lze pracovní poměr zrušit **písemně, z jakéhokoliv důvodu i bez udání důvodu**, a to i ze dne na den.")

        st.markdown("#### ⏳ Maximální délka zkušební doby ze zákona:")
        st.markdown("""
        * 👷 **Běžný zaměstnanec:** Maximálně **4 měsíce**.
        * 👔 **Vedoucí zaměstnanec (manažer):** Maximálně **8 měsíců**.
        * ⏱️ **U smlouvy na dobu určitou:** Zkušební doba nesmí být delší než **polovina** sjednané doby trvání smlouvy.
        """)

        st.markdown("""
        <div class='box-blue'>
            🛡️ <b>Skrytá ochrana ve zkušební době (Nemoc):</b><br>
            Zaměstnavatel vás <b>nesmí</b> vyhodit během prvních 14 dnů vaší pracovní neschopnosti (nemoci)! Zkušební doba se navíc o dny vaší nemoci automaticky prodlužuje.
        </div>
        """, unsafe_allow_html=True)

        st.divider()
        st.markdown("<div class='box-yellow'>⚖️ <b>Právní poradna: Rozhodni reálné situace</b></div>", unsafe_allow_html=True)
        
        sit1 = st.radio("Situace 1: Panu Novákovi končí 4měsíční zkušebka v pátek. V pondělí za ním přijde šéf s tím, že mu zkušebku 'o další měsíc prodlužuje', protože si jím ještě není jistý. Může to udělat?", 
                      ["Ano, pokud se na tom dohodnou.", "Ne, zkušební dobu nelze dodatečně prodlužovat nad zákonný rámec."])
        if sit1 == "Ne, zkušební dobu nelze dodatečně prodlužovat nad zákonný rámec.":
            st.success("✅ Přesně tak! Zkušební dobu nelze po sjednání svévolně prodlužovat. Prodlužuje se pouze automaticky o celodenní překážky v práci (nemoc, dovolená).")

        sit2 = st.radio("Situace 2: Lenka je ve zkušební době. Zjistila, že jí práce ničí psychiku a chce okamžitě odejít. Šéf jí řekl, že musí dodržet dvouměsíční výpovědní lhůtu. Má pravdu?",
                      ["Ano, výpovědní lhůta platí vždy.", "Ne, ve zkušební době může odejít ze dne na den (písemně)."])
        if sit2 == "Ne, ve zkušební době může odejít ze dne na den (písemně).":
            st.success("✅ Správně! Kouzlo zkušební doby funguje obousměrně. Pokud se vám tam nelíbí, doručíte písemné zrušení a zítra už v práci nemusíte být.")

    elif selected_section_4 == "2.7 Smlouva na dobu určitou a neurčitou":
        st.markdown("### 2.7 Smlouva na dobu určitou a neurčitou")
        st.write("Pracovní poměr se zásadně liší jistotou budoucnosti. Cílem zákoníku práce je, aby lidé pracovali primárně na **dobu neurčitou** (stabilita pro rodinu, hypotéku). **Doba určitá** má chránit zaměstnavatele u dočasných projektů.")

        st.markdown("#### 🔄 Pravidlo „3 a dost“ (Ochrana proti řetězení)")
        st.write("Zaměstnavatel vás nemůže držet navždy v nejistotě krátkými smlouvami. Pro prodlužování smlouvy na dobu určitou u jednoho zaměstnavatele platí:")

        col_prav1, col_prav2, col_prav3 = st.columns(3)
        with col_prav1:
            st.markdown("### 1️⃣")
            st.write("**Jedna smlouva může být sjednána na max. 3 roky.**")
        with col_prav2:
            st.markdown("### 2️⃣")
            st.write("**Lze ji prodloužit nejvýše dvakrát po sobě.**")
        with col_prav3:
            st.markdown("### 3️⃣")
            st.write("**Celkem u jedné firmy dostanete max. 3 tyto smlouvy.**")

        st.markdown("""
        <div class='box-green'>
            💡 <b>Automatická změna na dobu neurčitou:</b><br>
            Pokud vaše smlouva na dobu určitou vypršela (např. 31. prosince), ale vy 2. ledna normálně přijdete do práce, pracujete a šéf o tom ví (nevyhodí vás ze dveří), <b>vaše smlouva se ze zákona automaticky mění na smlouvu na dobu neurčitou!</b>
        </div>
        """, unsafe_allow_html=True)

        st.divider()
        st.markdown("<div class='box-yellow'>📅 <b>Kalkulačka kariérní jistoty</b></div>", unsafe_allow_html=True)
        st.write("Otestuj si pravidlo '3 a dost' v praxi. Tvůj zaměstnavatel ti dává neustále smlouvy jen na 1 rok. Kolik jich můžeš dostat?")

        poradi_smlouvy = st.slider("Počet smluv na dobu určitou v řadě u stejné firmy:", 1, 5, 1)

        if poradi_smlouvy == 1:
            st.info("📄 Podepsal jsi 1. smlouvu. Běžný postup při nástupu do nové práce.")
        elif poradi_smlouvy == 2:
            st.info("📄 Podepsal jsi 1. prodloužení. Vše je v pořádku.")
        elif poradi_smlouvy == 3:
            st.warning("⚠️ **Poslední povoleno!** Toto je tvá celkově třetí a ze zákona poslední smlouva na dobu určitou. Až vyprší, musí přijít smlouva na neurčito.")
        else:
            st.error("🚨 **PORUŠENÍ ZÁKONA:** Čtvrtá smlouva na dobu určitou v řadě je (až na specifické sezónní výjimky) nezákonná! Máš právo písemně oznámit zaměstnavateli, že trváš na zaměstnávání a tvůj poměr se tím mění na dobu neurčitou.")

    elif selected_section_4 == "2.8 Švarcsystém a gig economy":
        st.markdown("### 2.8 Švarcsystém a gig economy")

        st.write("Trh práce nabízí nové formy přivýdělku, ale některé z nich balancují na hraně nebo rovnou za hranou zákona. Je zásadní chápat rozdíl mezi **závislou prací** (zaměstnanec) a **podnikáním** (OSVČ).")

        st.markdown("#### 🚨 Co je to Švarcsystém?")
        st.write("Švarcsystém je **nelegální zastírání závislé práce**. Vykonáváte práci pro firmu jako běžný zaměstnanec, ale na papíře jste OSVČ (živnostník) a vystavujete firmě faktury. Firma to dělá, aby ušetřila cca 34 % na zdravotním a sociálním pojištění.")
        
        st.markdown("""
        <div class='box-red'>
            ⚠️ <b>Rizika Švarcsystému pro tebe:</b><br>
            Nemáš nárok na placenou dovolenou, odstupné, příplatky za víkendy, a pokud onemocníš, jsi zcela bez příjmu. Hrozí ti navíc doměření daní od finančního úřadu a pokuta až 100 000 Kč! (Firmě pak až 10 000 000 Kč).
        </div>
        """, unsafe_allow_html=True)

        st.divider()
        st.markdown("<div class='box-yellow'>📋 <b>Diagnostika: Jsem oběť Švarcsystému?</b></div>", unsafe_allow_html=True)
        st.write("Zaškrtni všechny výroky, které platí pro tvou 'podnikatelskou' činnost (na IČO) u dané firmy:")

        svarc1 = st.checkbox("Pracuji pravidelně a výhradně pouze pro tuto jedinou firmu.")
        svarc2 = st.checkbox("Šéf mi nařizuje pracovní dobu (od 8 do 16) a musím se hlásit o pauzy.")
        svarc3 = st.checkbox("Pracuji na firemním notebooku a nosím firemní tričko s jejich logem.")
        svarc4 = st.checkbox("Nemám možnost práci delegovat na někoho jiného, musím ji vykonat osobně.")

        skore_svarc = sum([svarc1, svarc2, svarc3, svarc4])

        if skore_svarc >= 3:
            st.error("🚩 **Tohle je učebnicový Švarcsystém!** Splňuješ všechny znaky závislé práce podle § 2 Zákoníku práce (vztah nadřízenosti, osobní výkon, náklady zaměstnavatele). Pracuješ nelegálně na IČO.")
        elif skore_svarc > 0:
            st.warning("⚠️ **Riziková zóna:** Tvá práce má znaky zaměstnání. Jako skutečný podnikatel na IČO bys měl mít svobodu v organizaci času a nést vlastní podnikatelské riziko.")
        else:
            st.success("✅ **Zdravé podnikání:** Pokud nevykazuješ tyto znaky, funguješ jako skutečný freelancer (např. IT specialista či grafik pracující na zakázkách pro více klientů).")

        st.divider()
        st.markdown("#### 🚴 Gig economy (Platformová ekonomika)")
        st.write("Rozvoz jídla (Foodora, Wolt), alternativní taxi (Bolt, Uber) nebo drobné IT zakázky přes aplikace. Zde je vaším 'šéfem' často neviditelný algoritmus.")

        col_gig1, col_gig2 = st.columns(2)
        with col_gig1:
            st.success("🟢 **Výhody Gig Economy:**\n* Okamžitý nástup a nízká bariéra vstupu.\n* Extrémní flexibilita (aplikaci zapnete jen když chcete vydělávat).\n* Možnost kombinovat s jinou prací nebo studiem.")
        with col_gig2:
            st.error("🔴 **Temná strana (Rizika):**\n* Odměna se mění podle toho, jak algoritmus sníží/zvýší sazby.\n* Falešná svoboda: aplikace vás penalizuje za odmítání zakázek.\n* Z opotřebení vlastního auta/kola nebo telefonu vám nikdo nic nezaplatí.")

    elif selected_section_4 == "2.9 Red flags v inzerátech a smlouvách":
        st.markdown("### 2.9 Red flags: Varovné signály v inzerátech a smlouvách")
        st.write("Slovo **'Red Flag'** (červená vlajka) označuje signál, že s danou firmou nebo smlouvou něco není v pořádku. V rámci finanční a občanské gramotnosti je klíčové umět tyto triky dekódovat.")

        st.markdown("#### 🕵️ Dekodér inzerátů")
        st.markdown("""
        | Co firma napíše (Red Flag) | Co to ve skutečnosti znamená v praxi |
        | :--- | :--- |
        | 🚩 **„Jsme jako rodina.“** | Toxický tlak na obětování se pro firmu. *„Rodině přece nepolezeš do peněz a uděláš přesčas zdarma o víkendu.“* |
        | 🚩 **„Dynamické a rychlé prostředí.“** | Totální chaos, absence procesů, zadávání úkolů na poslední chvíli a stres. |
        | 🚩 **„Motivující ohodnocení bez stropu.“** | Minimální fixní plat, většina příjmu závisí na nesplnitelných provizích a pokutách. |
        """)

        st.markdown("#### 📝 Red Flags přímo v pracovních smlouvách a dohodách")
        st.markdown("""
        * ❌ **Závazek mlčenlivosti o mzdě pod pokutou:** V ČR zákoník práce takovou smluvní pokutu neumožňuje. Zaměstnanci se o svých mzdách ze zákona bavit mohou (řeší směrnici EU o transparentnosti odměňování).
        * ❌ **Konkurenční doložka u běžných pozic:** Zákaz pracovat v oboru po odchodu z firmy. (Je platná POUZE tehdy, pokud vám za ni firma po dobu jejího trvání platí minimálně 50 % průměrného výdělku měsíčně!).
        * ❌ **Srážky ze mzdy bez dohody:** Smlouva obsahuje pasáž, že firma může strhávat peníze za 'špatný výkon' nebo rozbitý hrnek v kuchyňce automaticky.
        * ❌ **Podpis bianko směnky:** Absolutní extrém u některých 'finančně poradenských' firem = okamžitě odejděte!
        """)

        st.divider()
        st.markdown("<div class='box-yellow'>🧪 <b>Simulátor pohovoru: Jak se bránit manipulaci</b></div>", unsafe_allow_html=True)
        
        with st.form("red_flags_form"):
            st.write("Sedíš na pohovoru. Personalista ti s úsměvem položí smlouvu na stůl a řekne:")
            st.markdown("*„Tak tady to máme. Je to standardní smlouva, všichni u nás ji mají stejnou. Tady do kolonky druh práce jsme raději dali 'Pracovník provozu', abychom to nekomplikovali, a mzdu si dohodneme pak ústně, víte, že my na papíry moc nehrajeme. Kde vám to mám podepsat?“*")
            
            st.write("Jak správně jako finančně gramotný občan zareaguješ?")
            odp = st.radio("Tvoje reakce:", [
                "A) Super, děkuji za důvěru! (Podepíšu to hned, ať dělám dobrý dojem).",
                "B) 'Pracovník provozu' je moc široký pojem. Rád/a bych to změnil/a na 'Asistent prodeje'. A mzdu musíme mít před nástupem určenou minimálně písemným mzdovým výměrem.",
                "C) Řeknu, ať do smlouvy napíšou mzdu 150 000 Kč, jinak odcházím."
            ])
            
            if st.form_submit_button("Vyhodnotit reakci"):
                if odp.startswith("B"):
                    st.success("✅ **Skvělá reakce dospělého člověka!** Chráníš se před tím, abys dělal děvečku pro všechno, a trváš na transparentnosti. Na ústní dohody se v pracovním právu nehraje.")
                elif odp.startswith("A"):
                    st.error("❌ **Prohrál jsi hru podle pravidel.** Právě jsi podepsal souhlas s tím, že tě firma může úkolovat čímkoliv. A pokud ti na konci měsíce dají minimální mzdu, nemáš v ruce jediný důkaz, že slíbili víc.")
                elif odp.startswith("C"):
                    st.warning("⚠️ **Příliš arogantní.** Být asertivní neznamená být neslušný nebo klást absurdní ultimáta. Cílem je narovnat podmínky podle zákona.")
# =========================================================================
    # SEKCE 3: HODNOTA MÉ PRÁCE: ODMĚŇOVÁNÍ A PENÍZE
    # =========================================================================
    elif selected_section_4 == "3.1 Hrubá mzda, čistá mzda a superhrubé uvažování":
        st.markdown("### 3.1 Hrubá mzda, čistá mzda a „superhrubé uvažování“")
        st.markdown("""
        <div class='box-blue'>
            💵 <b>Základní otázka:</b> Kolik za svou práci skutečně dostanu na účet — a kolik reálně stojím zaměstnavatele?
        </div>
        """, unsafe_allow_html=True)

        st.write("Na pracovním inzerátu vidíte **hrubou mzdu**. Na bankovní účet vám ale přijde částka menší — **čistá mzda**. A váš zaměstnavatel musí mít na vaše místo připravenou částku ještě mnohem vyšší — tzv. **celkové náklady zaměstnavatele**.")

        st.markdown("""
        <div class='box-gray'>
            🤔 <b>Proč se v názvu kapitoly píše o „superhrubém uvažování“?</b><br>
            Pojem <i>superhrubá mzda</i> byl v ČR sice v roce 2021 zákonem zrušen a daň se dnes počítá rovnou z hrubé mzdy. Přesto majitelé firem a HR stále musí uplatňovat <b>„superhrubé uvažování“</b>. Tedy uvědomovat si, že když slíbí zaměstnanci 40 000 Kč hrubého, firmu to bude stát celkově skoro 54 000 Kč kvůli povinným státním odvodům za zaměstnance.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("#### 📊 Tři úrovně financí na trhu práce:")
        
        col_m1, col_m2, col_m3 = st.columns(3)
        with col_m1:
            st.markdown("##### 1️⃣ Čistá mzda")
            st.info("Peníze, které vám reálně přijdou na bankovní účet. Je to částka po odečtení vašich odvodů a daně z příjmu.")
        with col_m2:
            st.markdown("##### 2️⃣ Hrubá mzda")
            st.warning("Částka ve vaší smlouvě. O této částce se vyjednává na pohovoru a počítají se z ní daně a odvody.")
        with col_m3:
            st.markdown("##### 3️⃣ Celkové náklady")
            st.error("Skutečná cena vaší práce. Obsahuje hrubou mzdu + dalších cca 33,8 %, které za vás firma MUSÍ odvést státu.")

    elif selected_section_4 == "3.2 Nominální a reálná mzda":
        st.markdown("### 3.2 Nominální a reálná mzda (Kupní síla)")
        st.write("Pokud vám šéf přidá 5 % ke mzdě, jste na tom lépe? **Ne vždy!** Záleží totiž na tom, jak rychle v zemi rostou ceny zboží a služeb (tzv. inflace).")

        st.markdown("""
        * 💸 **Nominální mzda:** Částka v korunách, kterou máte na výplatní pásce. (Např. loni 30 000 Kč, letos 33 000 Kč).
        * 🛒 **Reálná mzda:** Říká, **co si za tyto peníze skutečně koupíte**. Reálná mzda vyjadřuje vaši kupní sílu.
        """)

        st.markdown("""
        <div class='box-green'>
            🧮 <b>Jednoduchý princip (Inflace vs. Mzda):</b><br>
            • Když inflace (ceny v obchodech) roste <b>rychleji</b> než vaše mzda = chudnete (reálná mzda klesá).<br>
            • Když vaše mzda roste <b>rychleji</b> než inflace = bohatnete (reálná mzda roste).
        </div>
        """, unsafe_allow_html=True)

        st.divider()
        st.markdown("<div class='box-yellow'>📉 <b>Simulátor: Skutečně jsi zbohatl? (Kupní síla)</b></div>", unsafe_allow_html=True)
        st.write("Zadej svou výplatu a změň inflaci, ať vidíš, jestli si toho koupíš víc nebo míň:")

        col_inf1, col_inf2 = st.columns(2)
        with col_inf1:
            puvodni_mzda = 30000
            st.metric("Původní mzda (Loni)", f"{puvodni_mzda} Kč")
            zvyseni_mzdy = st.slider("Šéf ti přidal ke mzdě (%):", 0, 20, 5)
            inflace = st.slider("Inflace (zdražení v obchodech %):", 0, 20, 8)
            
        with col_inf2:
            nova_mzda = int(puvodni_mzda * (1 + (zvyseni_mzdy / 100)))
            st.metric("Nová mzda (Letos)", f"{nova_mzda} Kč", delta=f"+{zvyseni_mzdy}%")
            
            rust_realne_mzdy = zvyseni_mzdy - inflace
            if rust_realne_mzdy < 0:
                st.error(f"🚨 **Chudneš!** Tvá reálná mzda klesla o {-rust_realne_mzdy} %. Sice máš v peněžence víc korun, ale věci v obchodě zdražily mnohem víc.")
            elif rust_realne_mzdy == 0:
                st.warning("⚖️ **Jsi na nule.** Tvá mzda vzrostla přesně stejně jako ceny zboží. Můžeš si dovolit úplně to samé co loni.")
            else:
                st.success(f"📈 **Bohatneš!** Tvá reálná mzda vzrostla o {rust_realne_mzdy} %. Mzda překonala zdražování a ty si můžeš dovolit koupit více věcí.")

    elif selected_section_4 == "3.3 Výplatní páska a její náležitosti":
        st.markdown("### 3.3 Výplatní páska a co na ní hledat")
        st.write("Výplatní páska není jen nepřehledný kus papíru plný čísel. Je to klíčový **kontrolní dokument**. Ukazuje vám, zda vás firma nešidí na odpracovaných hodinách, jestli vám proplácí dovolenou a kolik vám z platu sebere stát.")

        st.markdown("#### 🧾 Rozpad výplatní pásky v praxi:")
        
        with st.expander("Klikni pro detailní vysvětlení položek na výplatní pásce", expanded=True):
            st.markdown("""
            1. **Hlavička a kmenová data:** Vaše osobní číslo, kód zdravotní pojišťovny (např. 111 pro VZP).
            2. **PHV (Průměrný hodinový výdělek):** Důležité číslo! Z tohoto průměru (za minulé čtvrtletí) se vám počítá, kolik peněz dostanete, když si vezmete placenou dovolenou nebo máte svátek.
            3. **Časový fond:** Kolik hodin měl daný měsíc (např. 168 h) a kolik jste skutečně odpracovali.
            4. **Základní mzda a příplatky:** Vaše sjednaná hrubá mzda + peníze navíc za přesčasy, víkendy či noční směny.
            5. **Dovolená:** Kolik dní dovolené jste čerpali a jaký je váš zůstatek do konce roku.
            6. **Odvody a daně:** Stržené sociální a zdravotní pojištění a záloha na daň.
            7. **Nezdanitelné části a slevy:** Slevy na dani, které uplatňujete (např. základní sleva na poplatníka nebo na studenta).
            8. **Srážky:** Například srážky za stravenky, obědy ve firemní kantýně, nebo exekuce.
            9. **K VÝPLATĚ:** Peníze, které vám reálně dorazí na bankovní účet.
            """)

        st.divider()
        st.markdown("<div class='box-yellow'>🧪 <b>Aktivita: Výplatní páska s chybami</b></div>", unsafe_allow_html=True)
        st.write("Jako brigádník / zaměstnanec jsi dostal tuto výplatní pásku za minulý měsíc. Víš jistě, že jsi odpracoval celý měsíc (168 h) a navíc jsi byl jeden den o víkendu (8 h přesčas). Najdi v tomto reálně vypadajícím výpisu **3 zásadní chyby**:")

        st.markdown("""
        <div style="background-color: #fdfdfd; padding: 20px; border: 1px dashed #64748b; font-family: 'Courier New', Courier, monospace; font-size: 0.95rem; color: #1e293b; line-height: 1.4; border-radius: 4px; box-shadow: 2px 2px 5px rgba(0,0,0,0.1);">
            <b>ZAMĚSTNAVATEL:</b> ABC Retail s.r.o. &nbsp;&nbsp;&nbsp; <b>OBDOBÍ:</b> 08/2026<br>
            <b>ZAMĚSTNANEC:</b> Jan Novák &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>OS. ČÍSLO:</b> 00458<br>
            <b>ZDR. POJIŠŤOVNA:</b> 111 (VZP) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>PHV:</b> 195,50 Kč/h<br>
            <hr style="border-top: 1px dashed #64748b;">
            <b>Mzdové složky:</b><br>
            Základní hrubá mzda ................ 30 000 Kč<br>
            Odpracováno ........................ 168 hod<br>
            Práce o víkendu (8 hod) ............ 0 Kč<br>
            Náhrada za dovolenou (0 hod) ....... 0 Kč<br>
            <hr style="border-top: 1px dashed #64748b;">
            Zůstatek dovolené .................. 12,5 dne<br>
            Základ daně z příjmů ............... 30 000 Kč<br>
            Záloha na daň (15 %) ............... -4 500 Kč<br>
            Sleva na poplatníka (prohlášení) ... Nepodepsáno (0 Kč)<br>
            Daň po slevě ....................... -4 500 Kč<br>
            Zdravotní poj. (4,5 %) ............. -1 350 Kč<br>
            Sociální poj. (7,1 %) .............. -2 130 Kč<br>
            Ostatní srážky (Pokuta-sklad) ...... -1 500 Kč<br>
            <hr style="border-top: 2px solid #1e293b;">
            <b>K VÝPLATĚ NA ÚČET: ................. 20 520 Kč</b>
        </div>
        """, unsafe_allow_html=True)

        with st.form("chyby_paska"):
            st.write("Kde tě zaměstnavatel (ať už omylem, nebo úmyslně) připravil o peníze?")
            chyb1 = st.checkbox("Chybí povinný příplatek za práci o víkendu (i když je uvedeno 8 odpracovaných hodin).")
            chyb2 = st.checkbox("Záloha na daň je špatně vypočítaná (nemá být 15 %).")
            chyb3 = st.checkbox("Není uplatněna sleva na poplatníka (firma zřejmě nepředložila 'Růžové prohlášení' k podpisu).")
            chyb4 = st.checkbox("Jednostranná srážka 'Pokuta-sklad' je nelegální.")
            chyb5 = st.checkbox("Zůstatek dovolené je zapsán v desetinných číslech, což zákoník práce neumožňuje.")
            
            if st.form_submit_button("Odhalit chyby"):
                if chyb1 and chyb3 and chyb4 and not chyb2 and not chyb5:
                    st.success("✅ **Výborně! Skvělý postřeh!**\n\n1. **Víkend zadarmo:** Máš tam 8h o víkendu, ale 0 Kč příplatek. Firmy 'zapomínají' platit přesčasy a víkendy velmi často.\n2. **Ztráta tisíců na dani:** Máš neuplatněnou slevu na poplatníka. Buď jsi nepodepsal tzv. růžový papír (Prohlášení k dani), nebo to mzdová účetní zapomněla zadat.\n3. **Nelegální srážka:** Zaměstnavatel ti NESMÍ dát 'pokutu' srážkou ze mzdy bez tvého písemného souhlasu, i kdybys ve skladu něco rozbil.")
                else:
                    st.error("Něco ti uniklo. Záloha 15 % je správně a dovolená se v půldnech evidovat může. Chybí ale peníze za víkend, sleva na dani a srážka jako 'pokuta' porušuje zákoník práce!")

    elif selected_section_4 == "3.4 Výpočet čisté mzdy krok za krokem":
        st.markdown("### 3.4 Výpočet čisté mzdy krok za krokem")
        
        st.markdown("""
        <div class='box-blue'>
            🧮 <b>Zjednodušený vzorec výplaty:</b><br>
            Čistá mzda = Hrubá mzda − Sociální pojištění zaměstnance − Zdravotní pojištění zaměstnance − Daň (po uplatnění slev)
        </div>
        """, unsafe_allow_html=True)

        st.markdown("#### 🏥 Co platíte státu? Rozpad Sociálního pojištění")
        st.write("Ze své hrubé mzdy odvádíte 'sociální pojištění' (v ČR aktuálně ve výši **7,1 %**). Z čeho se ale přesně skládá?")
        
        col_soc1, col_soc2 = st.columns(2)
        with col_soc1:
            st.markdown("##### 👴 Důchodové pojištění (6,5 %)")
            st.write("Drtivá většina (6,5 %) jde průběžně státu na vyplácení důchodů současným seniorům. Na svůj důchod si z tohoto de facto 'nešetříte', platíte ho generaci před vámi (tzv. průběžný systém).")
        with col_soc2:
            st.markdown("##### 🤒 Nemocenské pojištění (0,6 %)")
            st.write("Tato malá část (od r. 2024 znovu zavedená i pro zaměstnance) kryje vaše dávky, pokud onemocníte (nemocenská) nebo se staráte o nemocné dítě (OČR).")

        st.divider()
        st.markdown("#### 🧾 Modelový výpočet čisté mzdy")
        
        st.markdown("""
        | Krok | Položka | Výpočet | Částka |
        | :--- | :--- | :--- | :--- |
        | 1. | **Hrubý příjem (základ pro daně a odvody)** | Základ (32 000 Kč) + Příplatky (1 200 Kč) | **33 200 Kč** |
        | 2. | **Sociální pojištění (zaměstnanec)** | 33 200 × 7,1 % | **- 2 357 Kč** |
        | 3. | **Zdravotní pojištění (zaměstnanec)**| 33 200 × 4,5 % | **- 1 494 Kč** |
        | 4. | **Daň před slevami (15 %)** | 33 200 × 15 % | 4 980 Kč |
        | 5. | **Sleva na poplatníka** | Měsíční daňová sleva garantovaná státem všem pracujícím | **+ 2 570 Kč** |
        | 6. | **Reálná Daň po slevě** | 4 980 Kč (Daň) - 2 570 Kč (Sleva) | **- 2 410 Kč** |
        | 7. | **ČISTÁ MZDA K VÝPLATĚ** | 33 200 - 2 357 - 1 494 - 2 410 | **26 939 Kč** |
        """)

        st.caption("<i class='fi fi-bs-bookmark'></i> *Poznámka: Výpočet je zjednodušený pro výukové účely (zaokrouhlování na celé koruny). Skutečné parametry, daňové limity a slevy se mohou v závislosti na legislativě každý rok měnit.*")

    elif selected_section_4 == "3.5 Sazby pojištění, daně a náklady zaměstnavatele":
        st.markdown("### 3.5 Sazby pojištění, daně a celkové náklady zaměstnavatele")
        
        st.write("Doposud jsme se dívali na mzdu pohledem zaměstnance (co mi přijde na účet). Nyní se podíváme na mzdu **pohledem firmy**. Pro firmu nejste jen 'hrubá mzda', jste pro ni **mzdový náklad**.")

        st.markdown("#### 🏢 Proč jste pro firmu mnohem dražší, než si myslíte?")
        st.write("Stát firmám nařizuje, aby za každého zaměstnance na hlavní pracovní poměr platily ze svých firemních peněz **povinné odvody**. Zaměstnavatel musí nad rámec vaší hrubé mzdy zaplatit státu dalších **33,8 %**. Tyto peníze jsou pro firmu povinným **nákladem**, který fyzicky odejde z firemního bankovního účtu přímo státu.")

        st.markdown("#### 🔍 Co přesně zaměstnavatel platí státu (Rozpad 33,8 %)")
        
        col_odv1, col_odv2 = st.columns(2)
        with col_odv1:
            st.markdown("##### 🏥 Zdravotní pojištění (9 %)")
            st.write("Firma odvádí 9 % z vaší hrubé mzdy vaší zdravotní pojišťovně. Tyto peníze financují chod nemocnic, platy lékařů, operace a léky pro celou společnost.")
        with col_odv2:
            st.markdown("##### 🏛️ Sociální pojištění (24,8 %)")
            st.write("Firma posílá 24,8 % z vaší hrubé mzdy na účet České správy sociálního zabezpečení (ČSSZ). Z čeho se tato velká částka skládá?")
            st.markdown("""
            * **21,5 % na důchody:** Z těchto peněz stát rovnou platí penze současným důchodcům.
            * **2,1 % na nemocenské:** Z toho se platí dávky lidem na dlouhodobé neschopence nebo mateřské.
            * **1,2 % na politiku zaměstnanosti:** Financuje úřady práce a podpory v nezaměstnanosti pro lidi bez práce.
            """)

        st.markdown("""
        <div class='box-red'>
            💡 <b>Pointa pro finanční gramotnost:</b><br>
            Když přijdete za šéfem a řeknete si o přidání <b>1 000 Kč k hrubé mzdě</b>, musí šéf ve firemním rozpočtu najít <b>1 338 Kč</b>. Těch 338 Kč navíc spolkne stát. Proto firmy někdy raději nabízejí nefinanční benefity (např. mobil, auto, flexibilitu), které se daní a odvádějí jiným (levnějším) způsobem.
        </div>
        """, unsafe_allow_html=True)

        st.divider()
        st.markdown("<div class='box-yellow'>🧮 <b>Interaktivní simulátor: Z firemní kasy až k tobě na účet</b></div>", unsafe_allow_html=True)
        st.write("Vžij se do role majitele firmy. Chceš zaměstnat nového člověka. Zadej hrubou mzdu, kterou mu nabídneš na pohovoru, a sleduj, jak se peníze rozdělí mezi něj a stát:")

        vysnena_mzda = st.slider("Nabízená hrubá mzda na smlouvě (Kč):", 20000, 100000, 40000, step=1000)

        # Výpočty srážek zaměstnance (to, co platí zaměstnanec ze svého)
        soc_zam = int(vysnena_mzda * 0.071)
        zdr_zam = int(vysnena_mzda * 0.045)
        dan_pred = int(vysnena_mzda * 0.15)
        dan_po = max(0, dan_pred - 2570)  # Základní sleva na poplatníka
        cista = vysnena_mzda - soc_zam - zdr_zam - dan_po

        # Výpočty odvodů placených zaměstnavatelem (to, co platí firma navíc)
        soc_firma = int(vysnena_mzda * 0.248)
        zdr_firma = int(vysnena_mzda * 0.09)
        naklady_firmy = vysnena_mzda + soc_firma + zdr_firma

        # Peníze, které sebere stát celkem (od firmy i od zaměstnance)
        stat_celkem = soc_zam + zdr_zam + dan_po + soc_firma + zdr_firma

        # Podíly pro progress bar
        podil_zamestnanec = cista / naklady_firmy
        podil_stat = stat_celkem / naklady_firmy

        col_k1, col_k2, col_k3 = st.columns(3)
        with col_k1:
            st.metric("1. Náklad firmy celkem", f"{naklady_firmy:,} Kč".replace(",", " "))
            st.caption("Peníze, které reálně odejdou z účtu firmy.")
        with col_k2:
            st.metric("2. Peníze pro stát", f"{stat_celkem:,} Kč".replace(",", " "))
            st.caption("Daně a odvody od firmy i zaměstnance.")
        with col_k3:
            st.metric("3. Čistá mzda", f"{cista:,} Kč".replace(",", " "))
            st.caption("To, co přistane zaměstnanci na účtu.")

        st.write("📊 **Jak se firemní peníze (náklady) rozdělily procentuálně:**")
        st.progress(podil_zamestnanec, text=f"Zaměstnanec dostane cca {int(podil_zamestnanec*100)} % z firemních nákladů (Zbytek bere stát).")
    elif selected_section_4 == "3.6 Slevy na dani a odčitatelné položky":
        st.markdown("### 3.6 Slevy na dani, daňové zvýhodnění a odčitatelné položky")
        
        st.write("V oblasti daní se často používají tři pojmy, které znějí podobně, ale fungují úplně jinak. Pokud chcete maximalizovat svou výplatu (nebo vratku daní z finančního úřadu), musíte znát rozdíl!")

        st.markdown("#### ⚖️ Tři klíčové pojmy (Co je co?)")
        st.markdown("""
        | Pojem | Co přesně snižuje? | Kdy se obvykle uplatňuje |
        | :--- | :--- | :--- |
        | 💎 **Sleva na dani** | Snižuje **přímo vypočtenou daň**. Koruna slevy = koruna v kapse. | Často měsíčně (ve výplatě). |
        | 👨‍👩‍👧 **Daňové zvýhodnění** | Snižuje daň. Pokud vám daň už klesla na nulu, stát vám zbytek slevy **doplatí (Daňový bonus)**. | Měsíčně (uplatňuje jen 1 rodič). |
        | 📉 **Odčitatelná položka** | Nesnižuje daň, ale jen **základ, ze kterého se daň počítá**. Ušetří vám 15 % ze své hodnoty. | Typicky 1x ročně (v daňovém přiznání). |
        """)

        st.markdown("""
        <div class='box-blue'>
            💡 <b>Rozdíl polopaticky:</b><br>
            • <b>Sleva 1 000 Kč</b> = Na dani zaplatíte o rovných 1 000 Kč méně. Peníze vám zůstávají v kapse.<br>
            • <b>Odčitatelná položka 1 000 Kč</b> = Sníží váš daňový základ. Reálně vám to ale na finální dani ušetří jen 15 % z oné tisícikoruny (tj. pouhých 150 Kč).
        </div>
        """, unsafe_allow_html=True)

        st.divider()
        st.markdown("#### 💎 Přehled: Slevy na dani a Daňové zvýhodnění")
        st.write("Abyste mohli slevy uplatňovat už z měsíční výplaty, musíte v práci podepsat tzv. **Prohlášení poplatníka k dani** (známý „růžový papír“).")

        with st.expander("Rozklikni pro zobrazení všech Slev a Zvýhodnění (platné pro rok 2026)"):
            st.markdown("""
            **1. Základní sleva na poplatníka**
            * **Kolik to je:** 30 840 Kč ročně (2 570 Kč měsíčně).
            * **Kdo má nárok:** Každý pracující (i brigádník na DPP/DPČ, pokud podepíše prohlášení).

            **2. Daňové zvýhodnění na děti (lze proměnit v daňový bonus)**
            * **1. dítě:** 15 204 Kč ročně (1 267 Kč měsíčně).
            * **2. dítě:** 22 320 Kč ročně (1 860 Kč měsíčně).
            * **3. a další dítě:** 27 840 Kč ročně (2 320 Kč měsíčně).
            * *Poznámka:* Uplatnit ho může vždy jen jedna osoba ve společné domácnosti. U dítěte se ZTP/P je částka dvojnásobná.

            **3. Slevy pro osoby se zdravotním postižením (ZTP a invalidita)**
            * **Základní invalidita (I. a II. stupeň):** 2 520 Kč ročně (210 Kč měsíčně).
            * **Rozšířená invalidita (III. stupeň):** 5 040 Kč ročně (420 Kč měsíčně).
            * **Držitel průkazu ZTP/P:** 16 140 Kč ročně (1 345 Kč měsíčně).

            **4. Sleva na manžela/manželku (Uplatňuje se POUZE ročně)**
            * **Kolik to je:** 24 840 Kč ročně.
            * **Kdo má nárok:** Pokud má druhý z manželů vlastní příjmy max. 68 000 Kč za rok **A ZÁROVEŇ** pečuje o dítě do 3 let věku.
            """)
            st.warning("⚠️ **Zrušené slevy:** Pamatuj, že tzv. 'Sleva na studenta' a 'Školkovné' byly státem nedávno zrušeny. Na brigádě tě dnes chrání výhradně vysoká 'Základní sleva na poplatníka'.")

        st.divider()
        st.markdown("#### 📉 Běžné Odčitatelné položky (Nezdanitelné části základu daně)")
        st.write("Tyto položky řešíte typicky až na jaře v **ročním zúčtování daně** (udělá to za vás účetní) nebo v **daňovém přiznání**. Stát vám díky nim vrátí část zaplacených daní za loňský rok na účet jako hezký přeplatek.")
        
        st.markdown("""
        * 🩸 **Dary a darování krve:** Darovali jste peníze na charitu, nebo krev? Za 1 bezpříspěvkový odběr krve si snížíte základ daně o 3 000 Kč (vratka na dani = **450 Kč** čistého za odběr). Odběr kostní dřeně = 20 000 Kč.
        * 🏠 **Úroky z hypotéky:** Ze základu daně si můžete odečíst zaplacené úroky z úvěru na bydlení. Maximální limit je **150 000 Kč ročně**. Pokud ho využijete naplno, stát vám na jaře vrátí **až 22 500 Kč**.
        """)

        st.markdown("##### 🐖 Spoření na stáří (Penzijko, Životní pojištění, DIP)")
        st.write("Od roku 2024 stát zavedl **jeden společný limit 48 000 Kč ročně** pro všechny produkty spoření na stáří dohromady (Doplňkové penzijní spoření, Životní pojištění a Dlouhodobý investiční produkt - DIP). Pokud limit naplníte, stát vám vrátí na dani **7 200 Kč**.")
        
        st.markdown("""
        * ⚠️ **Zásadní pravidlo:** Do tohoto limitu se počítají POUZE vaše vlastní vklady (to, co si pošlete ze svého účtu). Nepočítají se sem peníze, které vám posílá zaměstnavatel!
        * 🧮 **Kdy se mi to začne počítat do daní?**
          * U nového **DIPu** si můžete odečíst z daní hned každou korunu, kterou vložíte.
          * U klasického **Penzijka (DPS)** na vás stát uplatňuje tzv. práh. Na vklady od 500 do 1 700 Kč měsíčně vám dává 'Státní příspěvek'. Abyste si něco mohli navíc odečíst i z daní, **musíte spořit více než 1 700 Kč měsíčně**. Do daní se započítá až částka, která oněch 1 700 Kč přesahuje. *(Abyste si z daní odečetli roční maximum 48 000 Kč, musíte měsíčně posílat 5 700 Kč).*
        """)

        st.markdown("""
        <div class='box-green'>
            🎁 <b>Firemní benefit snů: Příspěvek zaměstnavatele na stáří</b><br>
            Firma vám může na Penzijko, DIP nebo Životní pojištění přispívat ze svého <b>až 50 000 Kč ročně</b>. Proč je to pro obě strany tak výhodné?<br>
            Jsou to totiž absolutně <b>čisté nezdaněné peníze!</b> Z tohoto příspěvku zaměstnavatele se neodvádí žádná 15% daň, žádné zdravotní ani sociální pojištění. Pokud vám firma pošle na DIP 2 000 Kč, přistane vám tam přesně 2 000 Kč. Kdyby vám stejné peníze dali do hrubé mzdy jako bonus, zbylo by vám z nich na účtu sotva čtrnáct stovek.
        </div>
        """, unsafe_allow_html=True)

        st.divider()
        st.markdown("<div class='box-yellow'>🧩 <b>Simulátor: Kouzlo daňového bonusu a slev</b></div>", unsafe_allow_html=True)
        st.write("Nastav hrubou mzdu a přidej životní situaci. Sleduj, co to udělá s daní. Můžeš mít dokonce **čistou mzdu vyšší než hrubou**?")

        col_slev1, col_slev2 = st.columns(2)
        with col_slev1:
            hruba_slevy = st.slider("Hrubá mzda:", 20000, 60000, 30000, step=1000)
            deti = st.selectbox("Počet vyživovaných dětí (pro rok 2026):", [0, 1, 2, 3])
            
            # Výpočet pro simulátor
            dan_zaklad = int(hruba_slevy * 0.15)
            sleva_poplatnik = 2570
            
            # Zvýhodnění na děti (měsíční částky 2026)
            sleva_deti = 0
            if deti == 1: sleva_deti = 1267
            elif deti == 2: sleva_deti = 1267 + 1860
            elif deti >= 3: sleva_deti = 1267 + 1860 + 2320
            
            dan_po_poplatnikovi = dan_zaklad - sleva_poplatnik
            if dan_po_poplatnikovi < 0: 
                dan_po_poplatnikovi = 0
                
            dan_po_detech = dan_po_poplatnikovi - sleva_deti
            
            bonus = 0
            if dan_po_detech < 0:
                bonus = abs(dan_po_detech)
                realna_dan = 0
            else:
                realna_dan = dan_po_detech
                
            soc = int(hruba_slevy * 0.071)
            zdr = int(hruba_slevy * 0.045)
            
            cista_mzda_konecna = hruba_slevy - soc - zdr - realna_dan + bonus

        with col_slev2:
            st.write(f"1. Vypočtená daň z hrubé (15 %): **{dan_zaklad} Kč**")
            st.write(f"2. Mínus základní sleva na tebe: **- {sleva_poplatnik} Kč**")
            st.write(f"3. Mínus slevy na děti: **- {sleva_deti} Kč**")
            st.divider()
            
            if bonus > 0:
                st.success(f"🚀 **Vznikl ti Daňový Bonus: {bonus} Kč!**\nStát tě nenechá platit žádnou daň, a ještě ti tuto částku přihodí k výplatě navíc!")
                st.metric("Tvoje finální čistá mzda:", f"{cista_mzda_konecna:,} Kč".replace(",", " "))
            else:
                st.info(f"Konečná daň z příjmů, kterou reálně zaplatíš: {realna_dan} Kč")
                st.metric("Tvoje finální čistá mzda:", f"{cista_mzda_konecna:,} Kč".replace(",", " "))
            
            if cista_mzda_konecna > hruba_slevy:
                st.balloons()
                st.markdown("**WOW! Tvá čistá mzda je vyšší než hrubá!** To je možné právě díky státnímu daňovému bonusu za děti.")
    elif selected_section_4 == "3.8 Kam jdou odvody (sociální a zdravotní pojištění)":
        st.markdown("### 3.8 Kam jdou odvody? Solidarita v praxi")
        st.write("Odvody, které vám strhnou z výplaty, nejsou jen 'peníze pryč, které už nikdy neuvidíte'. Financují systémy, které vás a vaši rodinu mají chránit v krizových životních situacích.")

        col_kam1, col_kam2 = st.columns(2)
        with col_kam1:
            st.markdown("""
            <div style="background-color: #f0fdf4; padding: 20px; border-radius: 8px; border: 1px solid #bbf7d0; height: 100%;">
                <h4 style="color: #166534; margin-top: 0;">🏥 Zdravotní pojištění</h4>
                <p style="color: #15803d; font-size: 0.95rem;">Směřuje do systému veřejného zdravotního pojištění. Není to spoření, ale solidární fond. Hradí se z něj:</p>
                <ul style="color: #166534; font-size: 0.9rem;">
                    <li>Běžné i specializované návštěvy lékaře</li>
                    <li>Akutní a nemocniční péče (operace v řádech statisíců)</li>
                    <li>Část léků a zdravotnických prostředků</li>
                    <li>Preventivní prohlídky</li>
                </ul>
                <p style="font-size: 0.85rem; color: #166534; font-style: italic;">Princip: Bohatý a zdravý platí hodně a nečerpá nic. Chudý a nemocný platí málo, ale čerpá péči za miliony.</p>
            </div>
            """, unsafe_allow_html=True)

        with col_kam2:
            st.markdown("""
            <div style="background-color: #eff6ff; padding: 20px; border-radius: 8px; border: 1px solid #bfdbfe; height: 100%;">
                <h4 style="color: #1e3a8a; margin-top: 0;">🏛️ Sociální pojištění</h4>
                <p style="color: #1d4ed8; font-size: 0.95rem;">Jde do státního rozpočtu (ČSSZ) a rozděluje se na tři hlavní pilíře, které chrání při výpadku příjmů:</p>
                <ul style="color: #1e3a8a; font-size: 0.9rem;">
                    <li><b>Důchodové poj.:</b> Platí se z něj starobní, invalidní a pozůstalostní (sirotčí) důchody.</li>
                    <li><b>Nemocenské poj.:</b> Vyplácí tzv. nemocenskou (při dlouhé nemoci), mateřskou a ošetřovné.</li>
                    <li><b>Politika zaměstnanosti:</b> Hradí chod úřadů práce a podpory v nezaměstnanosti.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

    elif selected_section_4 == "3.8 Celková odměna za práci a vyjednávání o mzdě":
        st.markdown("### 3.8 Celková odměna za práci a vyjednávání o mzdě")
        
        st.write("Peníze nejsou jediná odměna. Při výběru práce je potřeba porovnat **celkový balíček** (tzv. Total Reward). Práce s nejvyšší hrubou mzdou totiž může být ve finále ta nejméně výhodná.")

        st.markdown("#### ⚖️ Co vše tvoří reálnou hodnotu práce?")
        st.markdown("""
        * 💵 **Finance:** Základní mzda, roční bonusy, příplatky za víkendy, třináctý plat.
        * 🕒 **Čas a flexibilita:** Možnost pracovat z domova (Home Office), pružná pracovní doba, 5. týden dovolené navíc, Sick days.
        * 🚗 **Náklady na dojíždění:** Čas strávený v zácpách a peníze za benzín/jízdenky (práce daleko od domova reálně snižuje vaši čistou mzdu).
        * 🍔 **Další benefity:** Stravenky, příspěvek na penzijní spoření (nedaní se!), Multisport karta, služební auto i k soukromým účelům.
        * 📈 **Růst a prostředí:** Firemní vzdělávání, zdravá firemní kultura a šéf, který vás neničí stresem.
        """)

        st.divider()
        st.markdown("<div class='box-yellow'>⚖️ <b>Rozhodovací simulátor: Která nabídka je skutečně lepší?</b></div>", unsafe_allow_html=True)
        st.write("Dostal jsi dvě pracovní nabídky. Papírově vypadá jedna lépe. Ale co když započítáš náklady na dopravu a tvůj volný čas? (Počítáme, že tvůj volný čas má pro tebe hodnotu 150 Kč / hodina).")

        col_nab1, col_nab2 = st.columns(2)
        with col_nab1:
            st.markdown("##### 🏢 Nabídka A: Korporát v centru")
            mzda_a = 40000
            dojizdeni_minuty_a = st.slider("Čas strávený dojížděním denně tam i zpět (v minutách):", 0, 180, 90, key="doj_a")
            naklady_doprava_a = st.slider("Měsíční náklady na dojíždění (palivo/jízdenky v Kč):", 0, 5000, 3000, key="nak_a")
            
            # Výpočet hodnoty ztraceného času (počítáme 21 prac. dní v měsíci)
            ztraceny_cas_a = (dojizdeni_minuty_a / 60) * 21 * 150
            realna_hodnota_a = mzda_a - naklady_doprava_a - ztraceny_cas_a

            st.write(f"Hrubá mzda: **{mzda_a} Kč**")
            st.info(f"Peníze vyhozené za dopravu: -{naklady_doprava_a} Kč\n\nHodnota ztraceného času v MHD/autě: -{int(ztraceny_cas_a)} Kč")
            st.metric("Skutečná hodnota nabídky A:", f"{int(realna_hodnota_a)} Kč")

        with col_nab2:
            st.markdown("##### 🏠 Nabídka B: Startup na Home Office")
            mzda_b = 35000
            st.write("Firma ti dovolí pracovat 100% z domova. Nikam nedojíždíš.")
            
            realna_hodnota_b = mzda_b # Žádné srážky za dopravu a ztracený čas
            
            st.write(f"Hrubá mzda: **{mzda_b} Kč**")
            st.success(f"Peníze vyhozené za dopravu: 0 Kč\n\nHodnota ztraceného času v MHD/autě: 0 Kč")
            st.metric("Skutečná hodnota nabídky B:", f"{int(realna_hodnota_b)} Kč")

        if realna_hodnota_b > realna_hodnota_a:
            st.markdown("🚨 **Výsledek:** Přestože je Nabídka B na papíře o 5 000 Kč chudší, **ve skutečnosti je pro tebe výhodnější!** Ušetříš peníze za benzín a hlavně získáš zpět desítky hodin svého života měsíčně.")
        else:
            st.markdown("⚖️ **Výsledek:** I přes započítání nákladů na dojíždění se Nabídka A stále finančně vyplatí. Záleží ale i na tom, zda ti stres z dojíždění za ty peníze stojí.")

        st.divider()
        st.markdown("#### 🗣️ Vyjednávání o mzdě")
        st.write("Vyjednávání není hádka na tržnici. Je to **profesionální obchodní rozhovor o hodnotě tvé práce**. Většina firem počítá s tím, že o prvním návrhu mzdy se bude diskutovat.")

        st.markdown("##### 🛡️ Jak se připravit na vyjednávání:")
        st.markdown("""
        1. **Data:** Zjisti si předem, jaká je běžná mzda v oboru a regionu (např. přes Platy.cz nebo NSP.cz).
        2. **Důkazy, ne pocity:** Neříkej *'potřebuju víc kvůli drahému nájmu'*. Řekni *'přináším praxi se systémem X, což vám ušetří čas v zácviku'* nebo *'za minulý rok jsem firmě zvedl prodeje o 15 %'*.
        3. **Rozpětí:** Připrav si částku, kterou reálně chceš, ale řekni si o 10 % víc (aby měla firma prostor tě 'smlouvat' dolů a oba jste byli nakonec spokojení).
        4. **Plán B:** Když firma nemá peníze na zvýšení platu, vyjednej si aspoň **benefity** (týden dovolené navíc, služební notebook, kurzy angličtiny). To firmu bolí finančně méně, ale pro tebe to má obrovskou hodnotu.
        """)

        st.markdown("<div class='box-purple'>🤖 <b>Trenažér: Hádej se o plat s AI šéfem</b></div>", unsafe_allow_html=True)
        st.write("Bojíš se říct si o peníze? Natrénuj si to nanečisto proti umělé inteligenci. Zkopíruj tento prompt a vlož ho do ChatGPT nebo Claude:")

        prompt_plat = """Hrajeme hru na vyjednávání o mzdě. Ty jsi tvrdý, ale racionální HR manažer firmy. Já jsem zaměstnanec, který pracuje na pozici Junior Marketing Specialista už rok a jde si za tebou říct o zvýšení hrubé mzdy o 15 %. 
Začni konverzaci tím, že se zeptáš, co potřebuji. Já vznesu požadavek. Ty nejprve odmítni a hledej důvody, proč mi přidat nemůžeš. Nenuť mě vyhrát hned. Čekej na mé argumenty. Pokud mé argumenty budou logické, podložené čísly nebo mi navrhneš kompromis v podobě nefinančních benefitů, můžeme se dohodnout. Po 6 výměnách zpráv hru ukonči a dej mi jako AI feedback, jak jsem si ve vyjednávání vedl."""

        st.markdown(f"""
        <div style="background-color: #f8f9fa; padding: 15px; border-left: 5px solid #8b5cf6; border-radius: 5px; font-family: monospace; font-size: 1.1em; color: #333; white-space: pre-wrap; word-wrap: break-word; line-height: 1.5;">
        {prompt_plat}
        </div>
        """, unsafe_allow_html=True)
        
        st.caption("💡 Tip: Zkopíruj text z fialového boxu výše a zkus AI přesvědčit, že si peníze navíc zasloužíš!")
# =========================================================================
    # SEKCE 4: ŽIVOT V PRÁCI: KULTURA, WELLBEING A KARIÉRNÍ RŮST
    # =========================================================================
    elif selected_section_4 == "4.1 Firemní kultura a wellbeing":
        st.markdown("### 4.1 Firemní kultura a wellbeing")
        
        st.markdown("""
        <div class='box-blue'>
            🧘 <b>Základní otázka:</b> Jak poznat práci, ve které se dá dlouhodobě kariérně růst a neztratit přitom zdraví a nervy?
        </div>
        """, unsafe_allow_html=True)

        st.write("**Firemní kultura** není to, co má firma napsané zlatým písmem na webu. Je to způsob, jakým se lidé ve firmě chovají, komunikují a rozhodují, když se nikdo nedívá.")

        col_kult1, col_kult2 = st.columns(2)
        with col_kult1:
            st.success("🟢 **Znaky zdravé kultury:**\n* Chyby se berou jako příležitost k učení, ne jako důvod k trestu.\n* Lidé se nebojí na cokoliv zeptat.\n* Firma drží své sliby.\n* Přesčasy jsou výjimečné, ne každodenní pravidlo.")
        with col_kult2:
            st.error("🔴 **Toxická kultura (Red flags):**\n* *„Kdo se ptá, ten na to asi nemá.“*\n* *„U nás se na hodinky nekouká, prostě makáme, dokud není hotovo.“*\n* Vedení mluví o zákaznících a podřízených s despektem a výsměchem.")

        st.divider()
        st.markdown("#### 🔋 Wellbeing a prevence vyhoření")
        st.write("**Wellbeing (životní a pracovní pohoda)** opravdu neznamená, že vám firma dá do kuchyňky banány zdarma nebo vám zaplatí lekci jógy. Skutečný wellbeing znamená **podmínky, ve kterých člověk může dlouhodobě pracovat bez poškozování fyzického a duševního zdraví**.")

        st.markdown("<div class='box-yellow'>📋 <b>Osobní test: Hrozí ti vyhoření? (Burnout Check)</b></div>", unsafe_allow_html=True)
        st.write("Syndrom vyhoření nevzniká ze dne na den. Je to plíživý proces. Zaškrtni tvrzení, která momentálně zažíváš ve škole, na brigádě nebo v práci:")

        b1 = st.checkbox("Mám neustále pocit, že nestíhám, a žiju v dlouhodobém stresu.")
        b2 = st.checkbox("Často vůbec nevím, co se ode mě přesně očekává (nejasná zadání).")
        b3 = st.checkbox("Nemám kontrolu nad svým časem (všechno řídí někdo jiný).")
        b4 = st.checkbox("Neumím nebo se bojím říct 'NE', když mě někdo požádá o úkol navíc.")
        b5 = st.checkbox("Moje práce/studium mi nedává smysl a dělám to jen jako robot.")
        b6 = st.checkbox("Nemám čas na odpočinek, koníčky a spánek.")

        skore_vyhoreni = sum([b1, b2, b3, b4, b5, b6])
        st.progress(skore_vyhoreni / 6)

        if skore_vyhoreni >= 4:
            st.error("🚨 **KRITICKÉ RIZIKO VYHOŘENÍ!** Tvůj systém hlásí přetížení. Chybí ti 'ochranné faktory'. Musíš si okamžitě nastavit hranice, naučit se říkat ne a najít si čas na digitální detox a spánek.")
        elif skore_vyhoreni >= 2:
            st.warning("⚠️ **Zvýšené riziko:** Začínáš balancovat na hraně. Zaměř se na to, abys měl jasně vymezený čas na práci a čas, kdy úplně 'vypneš' hlavu.")
        elif skore_vyhoreni > 0:
            st.info("ℹ️ **Běžná zátěž:** Občasný stres je normální, ale hlídej si, aby se z těchto bodů nestala každodenní rutina.")
        else:
            st.success("✅ **Skvělá práce s hranicemi!** Tvé mentální zdraví a wellbeing jsou aktuálně v rovnováze. Máš nastavené zdravé priority.")

    elif selected_section_4 == "4.2 Právo na odpojení a podnikavost v zaměstnání":
        st.markdown("### 4.2 Právo na odpojení a Intrapreneurship")
        
        st.markdown("#### 📵 Právo na odpojení (Right to disconnect)")
        st.write("V digitální době je hranice mezi prací a volnem extrémně křehká. Právo na odpojení znamená, že **nemáte povinnost být neustále dostupní (číst e-maily a zvedat telefony) ve svém osobním volnu**, jen proto, že máte v kapse smartphone.")

        st.markdown("<div class='box-yellow'>⚖️ <b>Rozhodovací scénář: Páteční zpráva od šéfa</b></div>", unsafe_allow_html=True)
        st.write("Je pátek, 20:30. Sedíš s přáteli v kině. Najednou ti pípne WhatsApp od šéfa: *„Ahoj, prosím tě, můžeš mi do toho reportu rychle dopsat čísla za tento týden? Potřebuju se na to podívat. Díky!“* (Nemáš sjednanou placenou pohotovost).")
        
        reakce_boss = st.radio("Jak zareaguješ?", [
            "A) Omluvím se přátelům, vyjdu z kina, otevřu na telefonu tabulku a rychle to udělám. Chci ukázat, že jsem pracovitý.",
            "B) Zprávu si přečtu, naštve mě to, ale odepíšu: 'Jsem v kině, udělám to zítra ráno, o víkendu.'",
            "C) Zprávu ignoruji nebo odepíšu: 'Ahoj, teď mám volno, podívám se na to hned v pondělí ráno, jak přijdu do práce.'"
        ])

        if reakce_boss.startswith("A"):
            st.error("❌ **Špatně (Cesta do pekla):** Právě jsi šéfovi ukázal, že tvůj osobní čas nemá hodnotu a jsi mu k dispozici 24/7. Příště ti napíše v sobotu o půlnoci.")
        elif reakce_boss.startswith("B"):
            st.warning("⚠️ **Napůl špatně:** Sice jsi práci odložil, ale stejně jsi obětoval svůj víkend. Navíc už sis zkazil náladu v kině přemýšlením nad prací.")
        elif reakce_boss.startswith("C"):
            st.success("✅ **Správně! (Zdravé hranice):** Pokud se nejedná o hořící budovu nebo nemáš ve smlouvě placenou pohotovost, tvůj volný čas je svatý. Dobrý šéf to bude respektovat. Špatný šéf to bude zkoušet znovu – a pak je načase změnit firmu.")

        st.divider()
        st.markdown("#### 💡 Intrapreneurship: Podnikavost v zaměstnání")
        st.write("Nemusíte si zakládat vlastní IČO nebo startup, abyste byli 'podnikatelé'. **Intrapreneurship** je schopnost chovat se podnikavě *uvnitř* cizí firmy (jako zaměstnanec). Znamená to přinášet nápady, vylepšovat procesy a brát si odpovědnost.")

        st.markdown("##### 🚀 Příklady, jak být Intrapreneurem:")
        st.markdown("""
        * ⚙️ **Zjednodušení procesů:** Štve tě, že se nějaká tabulka přepisuje ručně? Vytvoříš jednoduché makro (nebo poprosíš AI o skript) a ušetříš oddělení 5 hodin času týdně.
        * 🗣️ **Nová služba:** Pracuješ v kavárně a všimneš si, že si lidé často ptají na ovesné mléko. Navrhneš majiteli, ať ho zařadí, a zvedneš tak prodeje.
        * 📚 **Sdílení know-how:** Začneš sám od sebe tvořit přehledný manuál pro nové brigádníky, aby se nemuseli pořád ptát na to samé.
        """)

        st.info("🎯 **Proč byste to dělali?** Pokud firmě takto prokazatelně šetříte čas nebo vyděláváte peníze, získáváte ultimátní argument pro **vyjednávání o vyšším platu** nebo povýšení.")

    elif selected_section_4 == "4.3 Upskilling a reskilling":
        st.markdown("### 4.3 Upskilling a reskilling: Jak nezestárnout na trhu práce")
        st.write("V době automatizace a umělé inteligence už neplatí, že vystudujete jednu školu a s těmito znalostmi vystačíte do důchodu. Vaše tržní hodnota a bezpečnost závisí na vaší ochotě a schopnosti se učit.")

        col_skill1, col_skill2 = st.columns(2)
        with col_skill1:
            st.markdown("##### 📈 Upskilling (Zlepšování v oboru)")
            st.write("Znamená rozšiřování a prohlubování dovedností ve vaší současné profesi. Děláte to proto, abyste si udrželi práci, zrychlili si ji a zvedli svou finanční hodnotu.")
            st.caption("Příklad: Jste mzdová účetní a uděláte si kurz na to, jak automatizovat faktury pomocí pokročilého Excelu nebo AI.")
        with col_skill2:
            st.markdown("##### 🔄 Reskilling (Přeškolení na jiný obor)")
            st.write("Znamená učení se úplně novým dovednostem pro získání zcela jiné role (často se to děje, když starý obor zaniká nebo vás už nebaví).")
            st.caption("Příklad: Pracovali jste jako operátor na lince (práci převzal robot), a tak se přeškolíte na IT testera nebo řemeslníka.")

        st.markdown("""
        <div class='box-green'>
            🎓 <b>Státní podpora: E-shop s kurzy (Jsemvkurzu.cz)</b><br>
            Věděli jste, že za drahé IT a digitální kurzy nemusíte platit desetitisíce ze svého? Ministerstvo práce a sociálních věcí provozuje portál <b><a href="https://www.jsemvkurzu.cz" target="_blank" style="color: #166534; text-decoration: underline;">jsemvkurzu.cz</a></b>. Můžete se tam přihlásit na kurzy programování, marketingu, grafiky nebo cizích jazyků a <b>stát za vás zaplatí 82 % až 100 % ceny kurzu (až do výše 50 000 Kč)</b>. Je to dostupné i pro studenty nebo pracující, nejen pro nezaměstnané!
        </div>
        """, unsafe_allow_html=True)

        st.divider()
        st.markdown("<div class='box-purple'>🎯 <b>Generátor dovedností budoucnosti</b></div>", unsafe_allow_html=True)
        st.write("Představ si profesi, která tě láká. Co by se člověk v takové profesi měl začít učit (Upskilling), aby ho za 5 let nenahradil algoritmus, ale naopak se stal nepostradatelným?")

        profese = st.selectbox("Vyber profesi pro analýzu:", [
            "Vyber profesi...",
            "Marketingový specialista",
            "Automechanik",
            "Učitel / Lektor",
            "Účetní / Administrativa",
            "Programátor / Vývojář",
            "Zdravotní sestra / Pečovatel",
            "Skladník / Logistik",
            "Právník / Koncipient",
            "Kuchař / Gastronomie",
            "Stavař / Řemeslník"
        ])

        if profese == "Marketingový specialista":
            st.success("**Upskilling na 5 let:**\n* **Prompt engineering (práce s AI):** Nejen psát texty, ale umět zadat AI, ať vygeneruje 50 variant kampaně na základě dat.\n* **Analýza dat a psychologie:** AI napíše text, ale vy musíte chápat data o zákaznících a lidské emoce, na které reklama cílí.\n* *Kde začít dnes:* Založit si účet na ChatGPT/Claude a zkoušet ho používat pro brainstorming.")
        elif profese == "Automechanik":
            st.success("**Upskilling na 5 let:**\n* **Diagnostika elektromobilů a baterií:** Spalovacích motorů bude ubývat. Mechanik budoucnosti je z poloviny elektrikář a IT specialista.\n* **Práce s diagnostickým softwarem:** Hledání chyb v milionech řádků kódu palubních počítačů.\n* *Kde začít dnes:* Sledovat trendy v elektromobilitě a učit se základy elektroniky.")
        elif profese == "Učitel / Lektor":
            st.success("**Upskilling na 5 let:**\n* **Mentoring a facilitace:** Žáci si fakta najdou na internetu za sekundu. Učitel je musí učit *jak* informace kriticky ověřovat a řešit problémy v týmu.\n* **Využití AI ve výuce:** Zapojit technologie do výuky, ne je zakazovat.\n* *Kde začít dnes:* Trénovat koučovací techniky a psychologii komunikace.")
        elif profese == "Účetní / Administrativa":
            st.success("**Upskilling na 5 let:**\n* **Finanční poradenství:** Rutinní přepisování čísel z faktur udělá software. Účetní budoucnosti musí data interpretovat a radit firmám, kde ušetřit.\n* **Automatizace systémů:** Schopnost propojovat různé fakturační systémy a bankovní API.\n* *Kde začít dnes:* Naučit se pokročilé datové funkce (Power Query, Excel) a udělat si kurz datové analytiky na jsemvkurzu.cz.")
        elif profese == "Programátor / Vývojář":
            st.success("**Upskilling na 5 let:**\n* **Soft skills a pochopení byznysu:** Základní kód už umí psát nástroje jako Copilot. Programátor musí umět mluvit s klientem a chápat, jaký byznys problém kód vůbec řeší.\n* **Architektura systémů a kyberbezpečnost:** Navrhovat velké, bezpečné a udržitelné systémy proti hackerům.\n* *Kde začít dnes:* Trénovat komunikaci, vedení projektů a etický hacking.")
        elif profese == "Zdravotní sestra / Pečovatel":
            st.success("**Upskilling na 5 let:**\n* **Telemedicína a digitální záznamy:** Obsluha chytrých monitorovacích náramků, práce s digitální kartou pacienta a vyhodnocování dat na dálku.\n* **Lidská empatie a komunikace:** Tohle žádný robot nenahradí. Role se posune od 'píchání injekcí' (což časem zvládnou přístroje) k psychické podpoře pacientů.\n* *Kde začít dnes:* Kurz komunikace v krizových situacích a seznámení se s moderními medical-tech aplikacemi.")
        elif profese == "Skladník / Logistik":
            st.success("**Upskilling na 5 let:**\n* **Obsluha skladových dronů a robotů:** Těžkou fyzickou práci převezmou stroje. Skladník se stane jejich 'dispečerem'.\n* **Práce s WMS (Warehouse Management System):** Sledování toků zboží na tabletech a optimalizace tras.\n* *Kde začít dnes:* Zlepšovat se v práci s databázemi, Excelem a logickým plánováním procesů.")
        elif profese == "Právník / Koncipient":
            st.success("**Upskilling na 5 let:**\n* **Legal-tech a AI nástroje:** Prohledávání stovek stran smluv za právníka udělá AI. Právník se soustředí na složité vyjednávání u soudu a kličky.\n* **Kybernetické právo a ochrana dat (GDPR, AI Act):** Nový obor, který masivně roste.\n* *Kde začít dnes:* Kurz zaměřený na legislativu technologií a kyberbezpečnosti.")
        elif profese == "Kuchař / Gastronomie":
            st.success("**Upskilling na 5 let:**\n* **Zero-waste management a udržitelnost:** Umět sestavit menu tak, aby se nic nevyhazovalo (šetří to firmě obrovské peníze).\n* **Moderní potravinářské technologie:** Práce s konvektomaty řízenými počítačem, fúze klasického vaření s potravinovou chemií.\n* *Kde začít dnes:* Sledovat trendy v udržitelnosti a optimalizaci nákladů v kuchyni.")
        elif profese == "Stavař / Řemeslník":
            st.success("**Upskilling na 5 let:**\n* **Chytrá domácnost (Smart Home):** Elektrikář už nezapojuje jen dráty, ale nastavuje řídící jednotky na Wi-Fi (topení, žaluzie, bezpečnost).\n* **Čtení 3D modelů (BIM):** Místo papírových výkresů se bude na stavbách pracovat s tabletem a 3D modelem budovy.\n* *Kde začít dnes:* Kurz zapojování prvků chytré domácnosti nebo základy práce s CAD programy.")
# =========================================================================
    # SEKCE 5: KDYŽ SE CESTY ROZEJDOU: KONEC PRÁCE A KRIZOVÉ SITUACE
    # =========================================================================
    elif selected_section_4 == "5.1 Jak dát a dostat výpověď profesionálně":
        st.markdown("### 5.1 Jak ukončit pracovní poměr (Možnosti a lhůty)")
        st.markdown("""
        <div class='box-blue'>
            🧯 <b>Základní pravidlo:</b> Pojem „výpověď dohodou“ neexistuje! Jsou to dvě úplně odlišné věci, které mají zcela jiné dopady na vaše peníze a čas. Všechna ukončení musí být vždy <b>písemná</b>.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("#### ⚖️ 5 legálních způsobů, jak může skončit práce")
        
        tab_ukonceni1, tab_ukonceni2, tab_ukonceni3 = st.tabs(["🤝 Dohoda", "📄 Výpověď", "🚨 Další 3 způsoby"])
        
        with tab_ukonceni1:
            st.markdown("##### Dohoda o rozvázání pracovního poměru")
            st.write("Shodnou se na ní obě strany (zaměstnanec i šéf). Pracovní poměr končí přesně tím dnem, který si do dohody napíšete (klidně zítra).")
            st.error("🚩 **Největší past (Odstupné):** Pokud firma ruší tvé místo (nadbytečnost) a nabídne ti dohodu, **MUSÍ BÝT V DOHODĚ NAPSÁN TENTO DŮVOD**. Pokud tam důvod nenapíšou a ty to podepíšeš, přicházíš automaticky o zákonné odstupné (až 3 platy)!")

        with tab_ukonceni2:
            st.markdown("##### Výpověď (Jednostranná)")
            st.write("Rozhodnutí jen jedné strany. Vy můžete dát výpověď **z jakéhokoliv důvodu i bez udání důvodu**. Zaměstnavatel vám může dát výpověď **POUZE ze zákonem daných důvodů** (např. nadbytečnost, hrubé porušení předpisů, špatné zdravotní posudky).")
            st.info("⏱️ **Výpovědní doba:** Výpovědí práce nekončí hned! Běží zde minimálně **dvouměsíční výpovědní doba**, během které musíte dál chodit do práce a firma vás musí platit.")

        with tab_ukonceni3:
            st.markdown("##### 1. Okamžité zrušení (tzv. Výpověď na hodinu)")
            st.write("Extrémní situace. Zaměstnavatel vás vyhodí okamžitě, pokud něco ukradnete nebo hrubě porušíte pravidla. Vy můžete okamžitě odejít, pokud vám firma nevyplatí mzdu do 15 dnů po termínu splatnosti.")
            st.markdown("##### 2. Zrušení ve zkušební době")
            st.write("Může proběhnout ze dne na den, písemně, z obou stran a bez udání důvodu.")
            st.markdown("##### 3. Uplynutí doby určité")
            st.write("Máte-li smlouvu např. do 31. 12., tímto datem práce automaticky končí (pokud nepodepíšete prodloužení).")

        st.divider()
        st.markdown("<div class='box-yellow'>📅 <b>Kalkulačka: Jak funguje výpovědní doba?</b></div>", unsafe_allow_html=True)
        st.write("Zákon mluví jasně: Dvouměsíční výpovědní doba **začíná běžet až první den následujícího měsíce** po doručení výpovědi. Vyzkoušej si to:")

        mesic_podani = st.selectbox("Ve kterém měsíci předáš šéfovi papír s výpovědí?", 
            ["Leden", "Únor", "Březen", "Duben", "Květen", "Červen", "Červenec", "Srpen", "Září", "Říjen", "Listopad", "Prosinec"])

        mesice_kruh = ["Leden", "Únor", "Březen", "Duben", "Květen", "Červen", "Červenec", "Srpen", "Září", "Říjen", "Listopad", "Prosinec"]
        idx = mesice_kruh.index(mesic_podani)
        
        start_idx = (idx + 1) % 12
        konec_idx = (idx + 2) % 12
        
        rok_navic_start = ""
        rok_navic_konec = ""
        if start_idx < idx: rok_navic_start = " (příštího roku)"
        if konec_idx < idx: rok_navic_konec = " (příštího roku)"

        col_lhuta1, col_lhuta2 = st.columns(2)
        with col_lhuta1:
            st.info(f"⏳ **Tvá výpovědní lhůta ZAHÁJÍ běh:**\nAž 1. dne měsíce **{mesice_kruh[start_idx]}**{rok_navic_start}.")
        with col_lhuta2:
            st.error(f"🚪 **Tvá práce SKONČÍ a jsi volný/á:**\nAž na konci měsíce **{mesice_kruh[konec_idx]}**{rok_navic_konec}.")
            
        st.caption("💡 *Tip z praxe: Je úplně jedno, jestli podáš výpověď 1. nebo 28. v měsíci. Lhůta vždy čeká na začátek dalšího měsíce. Pokud spěcháš, zkus se šéfem raději sepsat Dohodu.*")

    elif selected_section_4 == "5.2 Úřad práce, podpora v nezaměstnanosti a rekvalifikace":
        st.markdown("### 5.2 Kdy mám nárok na podporu a jak pomáhá Úřad práce")
        st.write("Úřad práce (ÚP) není jen instituce 'pro dlouhodobě nezaměstnané'. Je to klíčový partner, který vám **vyřeší zdravotní pojištění** (bude ho za vás platit stát) a pomůže finančně překlenout dobu hledání nového místa.")

        st.markdown("<div class='box-yellow'>📋 <b>Diagnostika: Dostanu vůbec od státu peníze?</b></div>", unsafe_allow_html=True)
        st.write("Ztráta práce neznamená automaticky, že vám stát pošle podporu v nezaměstnanosti. Splňuješ tyto dvě tvrdé podmínky?")

        with st.form("podminky_up"):
            podm_1 = st.checkbox("Během posledních 2 let jsem odpracoval/a alespoň 12 měsíců, ze kterých se odvádělo důchodové pojištění.")
            podm_2 = st.checkbox("Moje poslední práce neskončila vyhazovem za hrubé porušení pracovní kázně (např. krádež, alkohol).")
            
            if st.form_submit_button("Zjistit nárok na podporu"):
                if podm_1 and podm_2:
                    st.success("✅ **Máš nárok na podporu v nezaměstnanosti!** Můžeš se evidovat na Úřadu práce a začnou ti posílat peníze.")
                elif not podm_1:
                    st.error("❌ **Zamítnuto (Pravidlo 12 z 24):** Nemáš odpracováno dost měsíců. Pozor! Běžná brigáda na DPP (do 10 000 Kč měsíčně) se do tohoto nepočítá, protože se z ní neodvádí pojištění. Studium na SŠ/VŠ se také už nepočítá jako náhradní doba!")
                elif not podm_2:
                    st.error("❌ **Zamítnuto (Hrubé porušení):** Pokud tě vyhodí pro hrubé porušení pracovních povinností, stát tě penalizuje a podporu v nezaměstnanosti nedostaneš vůbec.")

        st.divider()
        st.markdown("#### 💰 Výše podpory v nezaměstnanosti (Pravidla 2026)")
        st.write("Aby systém motivoval lidi k rychlejšímu hledání práce, podpora se v čase postupně snižuje. Počítá se z vašeho předchozího průměrného čistého příjmu:")
        
        st.markdown("""
        * **1. fáze:** 80 % předchozí mzdy
        * **2. fáze:** 50 % předchozí mzdy
        * **3. fáze:** 40 % předchozí mzdy
        """)
        st.caption("*(Doba, po kterou podpora běží, závisí na vašem věku. Člověk do 52 let dostává podporu celkem 5 měsíců. Zastropováno na maximálně 38 537 Kč měsíčně).*")

        st.markdown("<div class='box-purple'>🧮 <b>Kalkulačka podpory v nezaměstnanosti</b></div>", unsafe_allow_html=True)
        predchozi_cista_mzda = st.number_input("Tvoje předchozí čistá mzda v poslední práci (Kč):", min_value=10000, max_value=100000, value=30000, step=1000)
        
        podpora_80 = int(predchozi_cista_mzda * 0.8)
        podpora_50 = int(predchozi_cista_mzda * 0.5)
        podpora_40 = int(predchozi_cista_mzda * 0.4)
        
        MAX_PODPORA_2026 = 38537
        
        podpora_80 = min(podpora_80, MAX_PODPORA_2026)
        podpora_50 = min(podpora_50, MAX_PODPORA_2026)
        podpora_40 = min(podpora_40, MAX_PODPORA_2026)

        col_pod1, col_pod2, col_pod3 = st.columns(3)
        with col_pod1:
            st.metric("První 2 měsíce (80 %)", f"{podpora_80:,} Kč".replace(",", " "))
        with col_pod2:
            st.metric("Další 2 měsíce (50 %)", f"{podpora_50:,} Kč".replace(",", " "))
        with col_pod3:
            st.metric("Poslední měsíc (40 %)", f"{podpora_40:,} Kč".replace(",", " "))

        st.markdown("""
        <div class='box-gray'>
            🚩 <b>Pozor na to, jak ukončíte práci!</b> Pokud odejdete sami výpovědí nebo dohodou, aniž byste k tomu měli tzv. <i>vážný důvod</i> (např. stěhování za manželem, péče o dítě, zdraví), Úřad práce vás v prvních měsících penalizuje a nevyplatí vám celých 80 %, ale rovnou vás po celou dobu srazí na nižší procento podpory.
        </div>
        """, unsafe_allow_html=True)

        st.divider()

    elif selected_section_4 == "5.3 Co dělat, když... (Krizový trenažér)":
        st.markdown("### 5.3 Co dělat, když... (Krizový trenažér)")
        
        st.markdown("""
        <div class='box-red'>
            🧯 <b>Krizová sekce:</b> V této části nejde o teorii. Jde o schopnost chránit sám sebe a svá občanská práva ve vyhrocené situaci na pracovišti.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("#### Tvoje první kroky při průšvihu:")
        st.markdown("""
        | Situace | Co udělat jako PRVNÍ | Důkazy, které musíš zajistit |
        | :--- | :--- | :--- |
        | 💸 **Nevyplacená mzda** | Upozornit šéfa/účetní PÍSEMNĚ. | Výplatní pásky, smlouva, záznam docházky, odeslané e-maily. |
        | 🤬 **Šikana (Bossing)** | Zapisovat si konkrétní datum, čas a co přesně se stalo. | E-maily, svědectví kolegů, printscreeny chatu. |
        | ⚠️ **Nebezpečné prostředí** | Odmítnout práci, která ohrožuje život, a nahlásit to. | Fotky porouchaných strojů / chybějících pomůcek. |
        | 📝 **Nátlak na IČO** | Zjistit, jestli mě nenutí do nelegálního Švarcsystému. | Důkazy, že mi nařizují pracovní dobu. |
        """)

        st.divider()
        st.markdown("<div class='box-yellow'>🚨 <b>Trenažér odolnosti: Útok v kanceláři</b></div>", unsafe_allow_html=True)
        st.write("Vyzkoušej si, jestli bys dokázal ustát krizovou situaci s manipulativním šéfem. Jak bys zareagoval?")

        with st.form("krize_form"):
            st.write("**Šéf (hází ti na stůl papír):** *„Tady mi okamžitě podepiš dohodu o ukončení. Končíš! Když to nepodepíšeš hned, napíšu ti do papírů k výpovědi takové věci (hrubé porušení kázně), že si v tomhle městě už nikdy nenajdeš práci.“*")
            
            k_odp = st.radio("Vyber své řešení:", [
                "A) Leknu se. Zjevně má na mě nějaké páky. Radši dohodu podepíšu a odejdu v tichosti.",
                "B) Papír si vezmu, poděkuji a řeknu: 'Nic hned podepisovat nebudu. Vezmu si to domů, přečtu si to v klidu a poradím se s právníkem. Vyjádřím se zítra.'",
                "C) Začnu na něj křičet, ať mi vyhrožuje, zmačkám papír a hodím mu ho na hlavu."
            ])
            
            if st.form_submit_button("Odeslat tvou reakci"):
                if k_odp.startswith("B"):
                    st.success("✅ **Zlatá medaile za profesionalitu a nervy ze železa!** Nikdo na světě tě nemůže fyzicky donutit podepsat žádnou dohodu proti tvé vůli. Čas je teď tvá nejlepší zbraň. Vezmi papír domů.")
                elif k_odp.startswith("A"):
                    st.error("❌ **Stal ses obětí manipulace.** Pokud podepíšeš dohodu o ukončení z vlastní vůle bez odstupného, vzdal ses veškeré právní ochrany. Hrubé porušení by ti musel šéf složitě dokazovat a prohrál by u soudu.")
                elif k_odp.startswith("C"):
                    st.warning("⚠️ **Pozor na emoce.** Pokud začneš ničit firemní majetek nebo někoho fyzicky napadat, dáváš šéfovi skutečný a legální důvod tě okamžitě vyhodit pro hrubé porušení kázně (tzv. Výpověď na hodinu).")
    # =========================================================================
    # SEKCE 6: PRAKTICKÁ DÍLNA (ČISTĚ AKTIVITY 1–5)
    # =========================================================================
    elif selected_section_4 == "6.1 Praktická dílna (Aktivity 1–5)":
        st.markdown("### 🛠️ 6.1 Praktická dílna")
        st.write("Vyberte si aktivitu ze záložek níže a vyzkoušejte si praktické úkoly zaměřené na trh práce:")

        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "🗺️ Aktivita 1", 
            "🕵️ Aktivita 2", 
            "🤖 Aktivita 3", 
            "🧾 Aktivita 4", 
            "🎭 Aktivita 5"
        ])

        with tab1:
            st.markdown("#### Aktivita 1: Moje profesní mapa")
            with st.form("form_akt1"):
                q1 = st.text_area("Jaké činnosti mě baví?")
                q2 = st.text_area("Jaké problémy rád/a řeším?")
                q3 = st.text_area("Jaké dovednosti už mám?")
                q4 = st.text_area("Jaké dovednosti mi chybí?")
                q5 = st.text_area("Jaké profese s tím souvisejí?")
                q6 = st.text_area("Co mohu vyzkoušet během příštích tří měsíců?")
                if st.form_submit_button("Uložit mapu"):
                    st.success("Vaše profesní mapa byla uložena!")

        with tab2:
            st.markdown("#### Aktivita 2: Analýza pracovního inzerátu")
            with st.form("form_akt2"):
                a1 = st.text_area("Jaké dovednosti zaměstnavatel požaduje?")
                a2 = st.text_area("Co je nutné a co je jen výhoda?")
                a3 = st.text_area("Jaké red flags se v inzerátu objevují?")
                a4 = st.text_area("Jaké otázky byste položili na pohovoru?")
                a5 = st.text_area("Jak byste upravili životopis pro tuto pozici?")
                if st.form_submit_button("Uložit analýzu"):
                    st.success("Analýza inzerátu uložena!")

        with tab3:
            st.markdown("#### Aktivita 3: AI jako kariérní kouč")
            pozice_ai = st.text_input("Zadejte název pozice:", value="[pozice]")
            prompt = f"Pomoz mi připravit se na pohovor na pozici {pozice_ai}.\nNejprve mi polož 5 otázek jako personalista. Po každé mé odpovědi polož doplňující otázku. Na konci vyhodnoť moje silné stránky, slabá místa a navrhni konkrétní formulace, které znějí profesionálně, ale přirozeně."
            st.markdown("🤖 **Prompt ke zkopírování do AI:**")
            st.code(prompt, language="text")

        with tab4:
            st.markdown("#### Aktivita 4: Výplatní páska s chybami")
            with st.form("form_akt4"):
                e1 = text_area_1 = st.text_area("1. Najít tři chyby:")
                e2 = text_area_2 = st.text_area("2. Vysvětlit, proč jsou problém:")
                e3 = text_area_3 = st.text_area("3. Navrhnout, jak chybu řešit:")
                e4 = text_area_4 = st.text_area("4. Napsat e-mail zaměstnavateli:")
                if st.form_submit_button("Odeslat řešení"):
                    st.success("Řešení bylo odesláno!")

        with tab5:
            st.markdown("#### Aktivita 5: Role-play vyjednávání o mzdě")
            st.info("Zahrajte si scénku ve třech: Zaměstnavatel, Uchazeč a Pozorovatel.")
            with st.form("form_akt5"):
                st.write("**Hodnocení:**")
                h1 = st.checkbox("Věcnost")
                h2 = st.checkbox("Práce s důkazy")
                h3 = st.checkbox("Respekt")
                h4 = st.checkbox("Schopnost hledat kompromis")
                h5 = st.checkbox("Jasné pojmenování hodnoty práce")
                if st.form_submit_button("Uložit hodnocení"):
                    st.success("Hodnocení role-play uloženo!")
# =========================================================================
    # SEKCE 6: PRAKTICKÁ DÍLNA (ČISTĚ AKTIVITY 1–5)
    # =========================================================================
    elif "6.1" in selected_section_4:
        st.markdown("### 🛠️ 6.1 Praktická dílna")
        st.write("Vyberte si aktivitu ze záložek níže a vyzkoušejte si praktické úkoly zaměřené na trh práce:")

        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "🗺️ Aktivita 1", 
            "🕵️ Aktivita 2", 
            "🤖 Aktivita 3", 
            "🧾 Aktivita 4", 
            "🎭 Aktivita 5"
        ])

        # ---------------------------------------------------------------------
        # AKTIVITA 1: MOJE PROFESNÍ MAPA
        # ---------------------------------------------------------------------
        with tab1:
            st.markdown("#### Aktivita 1: Moje profesní mapa")
            st.write("Vytvořte jednoduchou mapu své budoucí pracovní cesty:")

            with st.form("form_akt1_mapa"):
                q1 = st.text_area("Jaké činnosti mě baví?")
                q2 = st.text_area("Jaké problémy rád/a řeším?")
                q3 = st.text_area("Jaké dovednosti už mám?")
                q4 = st.text_area("Jaké dovednosti mi chybí?")
                q5 = st.text_area("Jaké profese s tím souvisejí?")
                q6 = st.text_area("Co mohu vyzkoušet během příštích tří měsíců?")

                if st.form_submit_button("Uložit profesní mapu"):
                    st.success("Vaše profesní mapa byla uložena! Ideální odrazový můstek pro vaši kariéru.")

        # ---------------------------------------------------------------------
        # AKTIVITA 2: ANALÝZA PRACOVNÍHO INZERÁTU
        # ---------------------------------------------------------------------
        with tab2:
            st.markdown("#### Aktivita 2: Analýza pracovního inzerátu")
            st.write("Vyberte si libovolný pracovní inzerát (např. na portálu Jobs.cz) a odpovězte na tyto otázky:")

            with st.form("form_akt2_inzerat"):
                a2_1 = st.text_area("Jaké dovednosti zaměstnavatel požaduje?")
                a2_2 = st.text_area("Co je nutné a co je jen výhoda?")
                a2_3 = st.text_area("Jaké red flags se v inzerátu objevují?")
                a2_4 = st.text_area("Jaké otázky byste položili na pohovoru?")
                a2_5 = st.text_area("Jak byste upravili životopis pro tuto pozici?")

                if st.form_submit_button("Vyhodnotit inzerát"):
                    st.success("Skvělá práce! Analýza inzerátu vám pomůže nenaletět na špatnou nabídku.")

        # ---------------------------------------------------------------------
        # AKTIVITA 3: AI JAKO KARIÉRNÍ KOUČ
        # ---------------------------------------------------------------------
        with tab3:
            st.markdown("#### Aktivita 3: AI jako kariérní kouč")
            st.write("Použijte AI nástroj (ChatGPT, Claude) k přípravě na pracovní pohovor. Zadejte vysněnou pozici a zkopírujte si vygenerovaný prompt.")

            pozice_ai = st.text_input("Na jakou pozici se hlásíte?", value="Zadejte název pozice...")

            prompt_text = f"Pomoz mi připravit se na pohovor na pozici {pozice_ai}.\nNejprve mi polož 5 otázek jako personalista. Po každé mé odpovědi polož doplňující otázku. Na konci vyhodnoť moje silné stránky, slabá místa a navrhni konkrétní formulace, které znějí profesionálně, ale přirozeně."

            st.markdown("🤖 **Prompt ke zkopírování do AI:**")
            st.code(prompt_text, language="text")

        # ---------------------------------------------------------------------
        # AKTIVITA 4: VÝPLATNÍ PÁSKA S CHYBAMI
        # ---------------------------------------------------------------------
        with tab4:
            st.markdown("#### Aktivita 4: Výplatní páska s chybami")
            st.write("Představte si, že jste na výplatní pásce našli nesrovnalosti. Zkuste je vyřešit:")

            with st.form("form_akt4_paska"):
                a4_1 = st.text_area("1. Najít tři chyby:")
                a4_2 = st.text_area("2. Vysvětlit, proč jsou problém:")
                a4_3 = st.text_area("3. Navrhnout, jak chybu řešit:")
                a4_4 = st.text_area("4. Napsat krátký profesionální e-mail zaměstnavateli:")

                if st.form_submit_button("Odeslat řešení"):
                    st.success("Odesláno! Komunikovat slušně, ale asertivně o penězích je základní dovednost.")

        # ---------------------------------------------------------------------
        # AKTIVITA 5: ROLE-PLAY VYJEDNÁVÁNÍ O MZDĚ
        # ---------------------------------------------------------------------
        with tab5:
            st.markdown("#### Aktivita 5: Role-play vyjednávání o mzdě")
            
            st.markdown("**Role pro scénku ve třídě:**")
            col_r1, col_r2, col_r3 = st.columns(3)
            with col_r1:
                st.info("👔 **Zaměstnavatel**\n(s omezeným rozpočtem)")
            with col_r2:
                st.success("🧑‍💼 **Uchazeč o práci**\n(snaží se vyjednat víc)")
            with col_r3:
                st.warning("⚖️ **Pozorovatel**\n(hodnotí argumenty obou)")

            st.markdown("---")
            st.markdown("**Co pozorovatel hodnotí:**")

            with st.form("form_akt5_roleplay"):
                h1 = st.checkbox("Věcnost (padly konkrétní argumenty, ne pocity?)")
                h2 = st.checkbox("Práce s důkazy (odkazování na trh práce/dovednosti?)")
                h3 = st.checkbox("Respekt (proběhlo to bez nátlaku a hádek?)")
                h4 = st.checkbox("Schopnost hledat kompromis (nabídly se např. benefity?)")
                h5 = st.checkbox("Jasné pojmenování hodnoty práce")
                
                if st.form_submit_button("Uložit hodnocení z role-play"):
                    st.success("Hodnocení uloženo! Vyjednávání o mzdě chce trénink.")
# =========================================================================
    # SEKCE 7: ZÁVĚR KAPITOLY A OPAKOVÁNÍ
    # =========================================================================
    elif selected_section_4 == "7.1 Případové studie z praxe" or "7.1" in selected_section_4:
        st.markdown("### 📚 7.1 Případové studie z praxe")
        st.write("Teorii už znáte, teď je čas na praxi. Vyzkoušejte si vyřešit reálné situace, do kterých se běžně dostávají absolventi a mladí lidé na trhu práce. Co byste hrdinům poradili?")

        tab_case1, tab_case2, tab_case3, tab_case4, tab_case5, tab_case6 = st.tabs([
            "🍾 Případ 1", 
            "🚴 Případ 2", 
            "💻 Případ 3", 
            "⚖️ Případ 4", 
            "☕ Případ 5", 
            "📄 Případ 6"
        ])

        # PŘÍPADOVÁ STUDIE 1
        with tab_case1:
            st.markdown("#### Případ 1: Studentka na kase a rozbité lahve")
            st.markdown("""
            > *Brigádnice pracuje v obchodě. Při vykládání zboží jí spadne přepravka a rozbije se pět lahví drahého alkoholu. Vedoucí jí oznámí, že se částka strhne z výplaty. Brigádnice ale nepodepsala dohodu o hmotné odpovědnosti.*
            """)
            
            with st.form("case1_form"):
                st.write("**Může zaměstnavatel škodu automaticky strhnout ze mzdy?**")
                c1_odp = st.radio("Vyber správnou odpověď:", [
                    "A) Ano, pokud zničila firemní majetek, musí to zaplatit v plné výši a firma to může rovnou strhnout.",
                    "B) Ne, bez jejího písemného souhlasu se srážkou ze mzdy nebo rozhodnutí soudu jí peníze strhnout nesmí.",
                    "C) Ano, ale jen do výše 1 000 Kč."
                ])
                if st.form_submit_button("Vyhodnotit Případ 1"):
                    if c1_odp.startswith("B"):
                        st.success("✅ **Správně!** Srážky ze mzdy k náhradě škody lze provést jen na základě písemné dohody se zaměstnancem. I kdyby škodu zavinila z nedbalosti (tzv. obecná odpovědnost), limit náhrady je max. 4,5násobek jejího průměrného platu.")
                    else:
                        st.error("❌ **Špatně.** Svévolné srážky ze mzdy jsou nelegální. Rozdíl je také v 'hmotné odpovědnosti' (např. za peníze v pokladně - tam se hradí celá škoda) a 'obecné odpovědnosti' (za rozbití věci nedbalostí - tam je limit 4,5násobku platu).")

        # PŘÍPADOVÁ STUDIE 2
        with tab_case2:
            st.markdown("#### Případ 2: Kurýr na platformě (Gig economy)")
            st.markdown("""
            > *Mladý kurýr začne rozvážet jídlo přes aplikaci. Líbí se mu flexibilita, ale zjistí, že po odečtení času, kola, telefonu, dat, pojištění a čekání mezi zakázkami je skutečný výdělek nižší, než čekal.*
            """)
            
            with st.form("case2_form"):
                st.write("**V čem je hlavní finanční chyták práce přes platformy?**")
                c2_odp = st.radio("Vyber největší riziko:", [
                    "A) Tržba za zakázku není čistý zisk. Kurýr musí z tržby zaplatit skryté náklady (palivo/kolo, opotřebení telefonu, mobilní data, vlastní pojištění a daně).",
                    "B) Aplikace většinou peníze vůbec nepošle, je to podvod.",
                    "C) Kurýr musí platit za to, že může aplikaci používat, pevnou měsíční částku."
                ])
                if st.form_submit_button("Vyhodnotit Případ 2"):
                    if c2_odp.startswith("A"):
                        st.success("✅ **Výborně!** Toto je podstata Gig economy. Svoboda (kdy pracovat) je vykoupena obrovskou nejistotou. Čas čekání na zakázku není placen a veškeré náklady a rizika nese pracovník, ne platforma.")
                    else:
                        st.error("❌ **To není hlavní problém.** Hlavním problémem je rozdíl mezi *tržbou* a *ziskem* po odečtení všech nákladů.")

        # PŘÍPADOVÁ STUDIE 3
        with tab_case3:
            st.markdown("#### Případ 3: Nabídka práce, která vypadá skvěle")
            st.markdown("""
            > *Uchazeč dostane nabídku: „Mladý dynamický tým, neomezené výdělky, práce na IČO, full-time docházka do kanceláře, vlastní notebook výhodou, očekáváme loajalitu a flexibilitu.“*
            """)
            
            with st.form("case3_form"):
                st.write("**Proč je kombinace IČO a 'full-time docházky do kanceláře' problematická?**")
                c3_odp = st.radio("Identifikuj hlavní problém (Red Flag):", [
                    "A) Je to nelegální Švarcsystém. Firma vyžaduje chování zaměstnance (docházka), ale přenáší rizika a odvody na IČO pracovníka.",
                    "B) 'Dynamický tým' znamená, že tam pracují jen studenti a neberou uchazeče nad 30 let.",
                    "C) Vlastní notebook na práci nestačí, musí mít firemní."
                ])
                if st.form_submit_button("Vyhodnotit Případ 3"):
                    if c3_odp.startswith("A"):
                        st.success("✅ **Zlaté pravidlo!** Vlastní živnost (IČO) je o svobodě. Pokud musíte sedět full-time v kanceláři a plnit příkazy, je to závislá práce a musíte mít smlouvu, jinak riskujete vy i firma pokutu za Švarcsystém.")
                    else:
                        st.error("❌ **Špatně.** Hlavním 'Red flagem' je skrývání klasického zaměstnání za falešné podnikání na IČO.")

        # PŘÍPADOVÁ STUDIE 4
        with tab_case4:
            st.markdown("#### Případ 4: Dvě pracovní nabídky (Total Reward)")
            st.markdown("""
            > *Uchazečka porovnává dvě nabídky:*
            > * **A:** 35 000 Kč čistého, kancelář, dojíždění 70 min denně.*
            > * **B:** 30 000 Kč čistého, home office, flexibilní režim.*
            """)
            
            with st.form("case4_form"):
                st.write("**Která nabídka je výhodnější a na co nesmí uchazečka při výpočtu zapomenout?**")
                c4_odp = st.radio("Vyber nejsprávnější úvahu:", [
                    "A) Nabídka A je o 5 000 Kč vyšší, takže je vždy výhodnější.",
                    "B) Nabídka B ušetří 70 minut času denně a peníze za dojíždění/obědy, ale doma stoupnou účty za elektřinu a topení. Záleží na tom, jakou hodnotu má pro ni její čas.",
                    "C) Nabídka B je vždy horší, protože práce z domova není opravdová práce."
                ])
                if st.form_submit_button("Vyhodnotit Případ 4"):
                    if c4_odp.startswith("B"):
                        st.success("✅ **Přesně tak.** Tomuto se říká Total Reward (celková odměna). 70 minut denně dělá za měsíc přes 24 hodin (3 pracovní směny) strávených zdarma na cestě. Finanční rozdíl 5 000 Kč se po odečtení dopravy může velmi rychle smazat.")
                    else:
                        st.error("❌ **Peníze nejsou vše.** K hrubé/čisté mzdě musíte připočítat náklady na čas a dojíždění.")

        # PŘÍPADOVÁ STUDIE 5
        with tab_case5:
            st.markdown("#### Případ 5: První brigáda a nejasná dohoda")
            st.markdown("""
            > *Klára nastupuje na letní brigádu do kavárny. Zaměstnavatel jí řekne, že „papíry se dořeší později“ a že zatím může chodit podle domluvy přes zprávy. Po dvou týdnech Klára odpracuje několik směn, ale nemá podepsanou DPP ani DPČ. Když se ptá na výplatu, vedoucí odpoví, že „se to nějak spočítá“.*
            """)
            
            with st.form("case5_form"):
                st.write("**Proč je práce bez papírů problém a co má Klára dělat?**")
                c5_odp = st.radio("Vyber správný postup:", [
                    "A) Klára musí počkat, šéf má asi hodně práce.",
                    "B) Klára by měla ihned přestat pracovat, uložit si výpisy ze zpráv a fotky směn jako důkaz a trvat na sepsání písemné dohody (DPP/DPČ) PŘED další směnou.",
                    "C) Klára by měla zavolat policii a šéfa zatknout."
                ])
                if st.form_submit_button("Vyhodnotit Případ 5"):
                    if c5_odp.startswith("B"):
                        st.success("✅ **Správný postup!** Práce na 'dobré slovo' často končí nevyplacením mzdy. DPP i DPČ musí být ze zákona písemné! Klára potřebuje důkazy (zprávy, fotky rozpisu), aby mohla peníze případně vymáhat.")
                    else:
                        st.error("❌ **Špatně.** Pokud počká, s největší pravděpodobností své peníze už nikdy neuvidí.")

        # PŘÍPADOVÁ STUDIE 6
        with tab_case6:
            st.markdown("#### Případ 6: Výplatní páska, která nesedí")
            st.markdown("""
            > *Adam pracuje na částečný úvazek. Na výplatní pásce vidí hrubou mzdu, ale čistá je nižší, než čekal. Adam zjistí, že nepodepsal 'prohlášení poplatníka' (růžový papír) a neuplatňuje se mu tak měsíční sleva na dani.*
            """)
            
            with st.form("case6_form"):
                st.write("**Jaký je rozdíl mezi daní a odvody a jak získá peníze zpět?**")
                c6_odp = st.radio("Co musí Adam udělat?", [
                    "A) Daně a odvody jsou to samé. Adam peníze nenávratně ztratil.",
                    "B) Daně jdou státu, odvody na zdravotnictví/důchody. Adam o peníze nepřišel úplně – po skončení roku si podá daňové přiznání a stát mu slevu na dani zpětně doplatí.",
                    "C) Musí jít na policii a nahlásit zaměstnavatele z krádeže."
                ])
                if st.form_submit_button("Vyhodnotit Případ 6"):
                    if c6_odp.startswith("B"):
                        st.success("✅ **Výborně!** Pokud nepodepíšete růžový papír, zaměstnavatel VÁM MUSÍ strhnout daň (15 %). Peníze propadly státu, ale stát vám je na jaře při daňovém přiznání rád vrátí.")
                    else:
                        st.error("❌ **Špatně.** O peníze Adam nepřišel a zaměstnavatel nic neukradl, jen plnil zákonnou povinnost z důvodu Adamovy chyby (nepodepsání prohlášení).")


    elif selected_section_4 == "7.2 Slovníček, rychlé opakování a prověrka" or "7.2" in selected_section_4:
        st.markdown("### 🎓 7.2 Slovníček pojmů a Závěrečná prověrka")
        
        st.markdown("#### 📖 Rychlý slovníček pojmů (Pamatujete si?)")
        st.write("Klikněte na pojem pro zobrazení jeho přesné definice.")

        # Slovníček ve 3 sloupcích
        col_voc1, col_voc2, col_voc3 = st.columns(3)
        
        with col_voc1:
            with st.expander("Trh práce"):
                st.markdown("Prostředí, kde se potkává nabídka práce (lidé) a poptávka po práci (firmy).")
            with st.expander("HR / Personalistika"):
                st.markdown("Human Resources; činnosti spojené s náborem, smlouvami, odměňováním, rozvojem a péčí o zaměstnance.")
            with st.expander("Hrubá mzda vs. Čistá mzda"):
                st.markdown("**Hrubá mzda:** mzda před odvody a daní (na smlouvě).<br>**Čistá mzda:** částka, která přijde zaměstnanci na účet.", unsafe_allow_html=True)
            with st.expander("Reálná mzda"):
                st.markdown("Kupní síla mzdy po zohlednění inflace (cen zboží).")

        with col_voc2:
            with st.expander("Onboarding / Offboarding"):
                st.markdown("**Onboarding:** zaškolení a začlenění nového člověka.<br>**Offboarding:** proces odchodu zaměstnance z firmy.", unsafe_allow_html=True)
            with st.expander("DPP a DPČ"):
                st.markdown("**DPP:** dohoda o provedení práce (max 300h/rok).<br>**DPČ:** dohoda o pracovní činnosti (max 20h/týden).", unsafe_allow_html=True)
            with st.expander("OSVČ a Freelancer"):
                st.markdown("**OSVČ:** osoba samostatně výdělečně činná.<br>**Freelancer:** samostatně pracující člověk na zakázkách.", unsafe_allow_html=True)
            with st.expander("Švarcsystém"):
                st.markdown("Nelegální zastírání zaměstnání (závislé práce) podnikáním na IČO.")

        with col_voc3:
            with st.expander("Gig economy"):
                st.markdown("Práce zprostředkovaná platformami nebo aplikacemi (Foodora, Uber).")
            with st.expander("ATS"):
                st.markdown("Systém pro automatické filtrování a třídění životopisů pomocí AI.")
            with st.expander("Upskilling a Reskilling"):
                st.markdown("**Upskilling:** rozšiřování dovedností v současném oboru.<br>**Reskilling:** přeškolení do jiné profese.", unsafe_allow_html=True)
            with st.expander("Wellbeing a Intrapreneurship"):
                st.markdown("**Wellbeing:** dlouhodobá pracovní pohoda.<br>**Intrapreneurship:** podnikavé chování uvnitř zaměstnání.", unsafe_allow_html=True)

        st.divider()
        st.markdown("<div class='box-red'>📝 <b>Závěrečná prověrka z Kapitoly 4</b></div>", unsafe_allow_html=True)
        st.write("Otestujte, jestli jste připraveni na trh práce:")

        with st.form("final_quiz_ch4"):
            q1 = st.radio("1. Proč se konkrétní sazby a částky daní hodí spíše do digitální aplikace než do tištěné učebnice?", 
                ["A) Protože v učebnici by vypadaly nehezky.", 
                 "B) Protože se minimální mzda, daňové slevy i limity pro odvody velmi často mění podle nové legislativy.", 
                 "C) Protože aplikace umí hrát zvuky."])
                 
            q2 = st.radio("2. Kdy má člověk nárok na podporu v nezaměstnanosti od Úřadu práce?", 
                ["A) Kdykoliv, když ztratí jakoukoliv práci.", 
                 "B) Jen pokud ho propustí pro hrubé porušení předpisů.", 
                 "C) Pokud má za poslední 2 roky odpracováno alespoň 12 měsíců a neporušil hrubě kázeň."])
                 
            q3 = st.radio("3. Co je to 'Celková odměna za práci' (Total Reward)?", 
                ["A) Jen to, co je napsáno na Mzdovém výměru.", 
                 "B) Souhrn mzdy, benefitů, pracovních podmínek, ušetřeného času, flexibility a možností růstu.", 
                 "C) Celkové odvody, které firma pošle státu."])
                 
            q4 = st.radio("4. Jak poznáte RED FLAG v pracovním inzerátu?", 
                ["A) Požadují vysokou školu.", 
                 "B) Slibují 'Jsme jako rodina', 'dynamické prostředí' a odmítají sdělit byť jen rámcovou mzdu.", 
                 "C) Nabízejí 5 týdnů dovolené."])

            if st.form_submit_button("Odeslat test k vyhodnocení"):
                score = 0
                if q1.startswith("B"): score += 1
                if q2.startswith("C"): score += 1
                if q3.startswith("B"): score += 1
                if q4.startswith("B"): score += 1
                
                st.progress(score / 4)
                
                if score == 4:
                    st.success("🏆 **Absolutní expert! 4/4.** Trh práce a byrokratické pasti už na tebe neplatí. Jsi připraven!")
                    st.balloons()
                elif score >= 2:
                    st.warning(f"👍 **Dobrý výkon: {score}/4.** Většinu věcí znáš, ale některé chytáky ti unikly. Doporučujeme projít si slovníček pojmů.")
                else:
                    st.error(f"🚨 **Pozor, máš jen {score}/4.** Tohle by tě v reálném životě mohlo stát hodně peněz a nervů. Zkus si kapitolu projít znovu, chráníš tím hlavně sám sebe!")
