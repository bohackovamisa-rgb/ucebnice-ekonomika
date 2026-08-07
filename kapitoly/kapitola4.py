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
