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

            st.markdown("##### 📌 Co z tohoto odhadu pro žáka vyplývá?")
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

        st.markdown("##### 📌 Jak uspět při náboru řízeném AI / ATS:")
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
                    <strong style="color: #0284c7; font-size: 0.9rem;">📌 OSOBNÍ A KONTAKTNÍ ÚDAJE</strong><br>
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
            st.write("Co přesně budete dělat (např. 'Účetní'). Pokud je definice příliš široká (např. 'Pracovník firmy'), nadřízený vás může nutit dělat cokoliv – od účtování po úklid toalet.")
        with col_s2:
            st.markdown("##### 2️⃣ Místo výkonu")
            st.write("Kde budete pracovat (např. 'Pobočka Brno, ulice X'). Pokud podepíšete místo 'Česká republika', může vás firma bez vašeho souhlasu přeložit z Prahy do Ostravy.")
        with col_s3:
            st.markdown("##### 3️⃣ Den nástupu")
            st.write("Přesné datum (např. 1. 9. 2026). Od tohoto dne vám vznikají práva a povinnosti, i kdybyste smlouvu podepsali o měsíc dříve.")

        st.markdown("""
        <div class='box-red'>
            🚨 <b>Klíčový omyl: Mzda NEMUSÍ být přímo v pracovní smlouvě!</b><br>
            Plat nebo mzda často není v textu smlouvy, ale na odděleném papíru zvaném <b>mzdový výměr</b>. Proč to firmy dělají?<br>
            • Co je ve <b>smlouvě</b>, to lze změnit POUZE s vaším písemným souhlasem (např. podepsáním dodatku).<br>
            • <b>Mzdový výměr</b> může firma jednostranně změnit i bez vás (může vám mzdu snížit až na hranici zaručené minimální mzdy).
        </div>
        """, unsafe_allow_html=True)

        st.divider()
        st.markdown("<div class='box-yellow'>🛠️ <b>Interaktivní dílna: Sestav platnou pracovní smlouvu</b></div>", unsafe_allow_html=True)
        st.write("HR oddělení ti poslalo návrh smlouvy, ale chybí v ní důležité pasáže. Doplň je tak, aby tě smlouva maximálně chránila a byla platná:")

        with st.form("form_smlouva"):
            f_druh = st.selectbox("1. Vyber druh práce:", ["Pracovník (cokoliv bude potřeba)", "Specialista marketingu", "Pomocná síla"])
            f_misto = st.selectbox("2. Vyber místo výkonu práce:", ["Česká republika", "Evropská unie", "Kancelář zaměstnavatele, Květná 15, Plzeň"])
            f_mzda = st.radio("3. Kde chceš mít uvedenou svou mzdu 45 000 Kč?", ["Přímo jako bod v Pracovní smlouvě", "Na odděleném Mzdovém výměru"])
            
            if st.form_submit_button("Zkontrolovat smlouvu"):
                if f_druh == "Specialista marketingu" and f_misto == "Kancelář zaměstnavatele, Květná 15, Plzeň" and f_mzda == "Přímo jako bod v Pracovní smlouvě":
                    st.success("✅ **Výborně! Sestavil jsi perfektní smlouvu.** Specifikoval jsi úzký druh práce (nebudou tě nutit dělat cizí práci), přesné místo (nemohou tě bez souhlasu přesunout do jiného města) a mzdu máš přímo ve smlouvě (nemohou ti ji jednostranně snížit).")
                else:
                    st.error("❌ **Tady na tebe zaměstnavatel vyzrál!** Pokud jsi dal široký druh práce nebo místo 'ČR', stáváš se loutkou, kterou lze libovolně přesouvat. Pokud jsi dal mzdu na mzdový výměr, vzdal jsi se jistoty pevné částky.")

    elif selected_section_4 == "2.6 Zkušební doba":
        st.markdown("### 2.6 Zkušební doba: Pravidla a ochrana")
        st.write("Zkušební doba není obdobím 'bezpráví'. Slouží k tomu, aby si obě strany vyzkoušely, zda jim spolupráce vyhovuje. Lze během ní pracovní poměr ukončit **zrušením ve zkušební době**, a to písemně, z jakéhokoliv důvodu i bez udání důvodu, a to i ze dne na den.")

        st.markdown("#### ⏳ Maximální délka zkušební doby ze zákona:")
        st.markdown("""
        * 👷 **Běžný zaměstnanec:** Maximálně **4 měsíce** (dříve 3 měsíce, novela ZP upravila).
        * 👔 **Vedoucí zaměstnanec (manažer):** Maximálně **8 měsíců**.
        * ⏱️ **U smlouvy na dobu určitou:** Zkušební doba nesmí být delší než **polovina** sjednané doby trvání smlouvy.
        """)

        st.markdown("""
        <div class='box-blue'>
            🛡️ <b>Skrytá ochrana ve zkušební době (Nemoc):</b><br>
            Zaměstnavatel vás <b>nesmí</b> vyhodit během prvních 14 dnů vaší pracovní neschopnosti (nemoci), i když jste ve zkušební době! Zkušební doba se navíc o dobu vaší nemoci (či dovolené) automaticky prodlužuje.
        </div>
        """, unsafe_allow_html=True)

        st.divider()
        st.markdown("<div class='box-yellow'>⚖️ <b>Právní poradna: Rozhodni reálné situace</b></div>", unsafe_allow_html=True)
        
        sit1 = st.radio("Situace 1: Panu Novákovi končí 4měsíční zkušebka v pátek. V pondělí za ním přijde šéf s tím, že mu zkušebku 'o další měsíc prodlužuje', protože si jím ještě není jistý. Může to udělat?", 
                      ["Ano, pokud se na tom dohodnou.", "Ne, zkušební dobu nelze dodatečně prodlužovat nad zákonný rámec."])
        if sit1 == "Ne, zkušební dobu nelze dodatečně prodlužovat nad zákonný rámec.":
            st.success("✅ Přesně tak! Zkušební doba se prodlužuje pouze o dny překážek v práci (např. nemoc). Zaměstnavatel ji nemůže svévolně natáhnout.")

        sit2 = st.radio("Situace 2: Lenka je ve zkušební době. Zjistila, že jí práce ničí psychiku a chce okamžitě odejít. Šéf jí řekl, že musí dodržet dvouměsíční výpovědní lhůtu. Má pravdu?",
                      ["Ano, výpovědní lhůta platí vždy.", "Ne, ve zkušební době může odejít ze dne na den (písemně)."])
        if sit2 == "Ne, ve zkušební době může odejít ze dne na den (písemně).":
            st.success("✅ Správně! Kouzlo zkušební doby funguje obousměrně. Pokud se vám tam nelíbí, doručíte písemné zrušení a zítra už tam nemusíte.")

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
            st.warning("⚠️ <b>Poslední povoleno!</b> Toto je tvá celkově třetí a ze zákona poslední smlouva na dobu určitou. Až vyprší, musí přijít smlouva na neurčito.")
        else:
            st.error("🚨 <b>PORUŠENÍ ZÁKONA:</b> Čtvrtá smlouva na dobu určitou v řadě je (až na specifické sezónní výjimky) nezákonná! Máš právo písemně oznámit zaměstnavateli, že trváš na zaměstnávání a tvůj poměr se tím mění na dobu neurčitou.")

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
            st.error(f"🚩 **Tohle je učebnicový Švarcsystém!** Splňuješ všechny znaky závislé práce podle § 2 Zákoníku práce (vztah nadřízenosti, osobní výkon, náklady zaměstnavatele). Pracuješ nelegálně na IČO.")
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
