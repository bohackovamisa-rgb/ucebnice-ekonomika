import math
import streamlit as st


def render():
    # =========================================================================
    # 📌 HLAVIČKA KAPITOLY
    # =========================================================================
    st.markdown(
        "<span class='hero-badge'>Kapitola 4</span>", unsafe_allow_html=True
    )
    st.markdown(
        "## 4. Cesta zaměstnance: od první orientace po kariérní rozhodnutí"
    )
    st.markdown(
        "<p style='font-size: 1.1rem; color: #64748b; margin-bottom: 1.5rem;'>"
        "Práce není jen výplata. Je to rozhodování o vlastní hodnotě, dovednostech, právní ochraně, penězích, "
        "vztazích na pracovišti i o tom, jak se člověk přizpůsobuje světu, který mění digitalizace, AI a globální konkurence.<br><br>"
        "Tato kapitola je postavená jako cesta zaměstnance: od otázky „kdo jsem a co umím?“ přes hledání práce, "
        "smlouvu a výplatní pásku až po wellbeing, kariérní růst, výpověď a krizové situace.</p>",
        unsafe_allow_html=True,
    )

    with st.container(border=True):
        st.markdown(
            """
        <div class='box-blue'>
            <strong>⚙️ Pointa kapitoly:</strong> Tato kapitola je postavená jako kompletní cesta zaměstnance: od otázky „Kdo jsem a co umím?“ přes hledání práce, nábor, smlouvu a výplatní pásku až po wellbeing, kariérní růst, výpověď a krizové situace.
        </div>
        """,
            unsafe_allow_html=True,
        )

    # 📌 PŘEHLED A NAVIGACE KAPITOLOU
    with st.expander(
        "🧭 O čem kapitola je, kde ji využijete a co si z ní odnesete (Rozbalit)", expanded=False
    ):
        c_nav1, c_nav2 = st.columns(2)
        with c_nav1:
            st.markdown("""
            **🎯 Co si z kapitoly odnesete:**
            * 🧭 **Orientace na trhu práce:** Proč se některé dovednosti na trhu práce oceňují více než jiné a jak se profese mění vlivem AI, automatizace a globalizace.
            * 🧑‍💼 **HR, zaměstnání a právo:** Personalistika, nábor, pracovní smlouva, DPP, DPČ, OSVČ, freelancing, gig economy a rizika švarcsystému.
            * 🚩 **Red flags:** Varovné signály v inzerátu, na pohovoru i ve smlouvě.
            * 💵 **Mzda a cena práce:** Hrubá mzda, čistá mzda, nominální a reálná mzda i celkové náklady zaměstnavatele.
            * 🤖 **AI jako pomocník:** Generativní AI může pomoci s přípravou na pohovor, motivační dopis, životopis i analýzu pracovního trhu.
            * 🧘 **Wellbeing a kariéra:** Souvislost firemní kultury, vyhoření, práva na odpojení, upskillingu a reskillingu s dlouhodobou kariérou.
            """)
            st.markdown(
                """
            <div style="font-size: 0.85rem; color: #64748b; margin-top: 10px;">
                <i>💼 <b>Kde to využijete:</b> Při výběru oboru, brigády nebo první práce, při psaní životopisu, pohovoru, čtení smlouvy, vyjednávání mzdy i při řešení problémů na pracovišti.</i>
            </div>
            """,
                unsafe_allow_html=True,
            )

        with c_nav2:
            st.markdown("""
            **🧭 Doporučené pořadí studia:**
            1. 🧭 **Já na trhu práce** — Nejdřív přichází orientace v tom, co trh práce oceňuje, jak funguje nabídka a poptávka po práci, jaké profese mění AI a proč je důležitá digitální stopa.
            2. 📜 **Hra podle pravidel** — Potom přichází orientace v náboru, pracovních smlouvách, DPP, DPČ, zkušební době, švarcsystému a platformové práci.
            3. 💰 **Hodnota mé práce** — Následně se rozkrývá mzda, odvody, čistý příjem, celkové náklady zaměstnavatele, inflace a celková odměna včetně benefitů.
            4. 🧘 **Život v práci** — Poté přichází firemní kultura, wellbeing, vyhoření, právo na odpojení, intrapreneurship a celoživotní učení.
            5. 🚪 **Když se cesty rozejdou** — Nakonec se řeší výpověď, odstupné, úřad práce, podpora, rekvalifikace a krizové situace.
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
        "5.3 Co dělat, když... (Krizový trenažér)",
        "6.1 Praktická dílna (Aktivity 1–5)",
        "7.1 Případové studie z praxe",
        "7.2 Slovníček, rychlé opakování a prověrka",
    ]

    st.markdown("### 📌 Přechod na podkapitolu:")
    selected_section_4 = st.selectbox(
        "Přechod na podkapitolu:",
        section_options_4,
        index=0,
        label_visibility="collapsed",
        key="k4_section_select",
    )
    st.divider()

    # =========================================================================
    # SEKCE 1: JÁ NA TRHU PRÁCE: PŘÍPRAVA A ORIENTACE
    # =========================================================================
    if selected_section_4 == "1.1 Proč trh platí různé profese různě":
        st.markdown("## 1. Já na trhu práce: příprava a orientace")
        st.markdown("### 1.1 Proč trh platí různé profese různě")
        st.markdown(
            """
        <div class='box-blue'>
            🧭 <b>Základní otázka:</b> Kdo jsem, co umím a proč by za mou práci měl někdo zaplatit?
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.write(
            "Trh práce není jen místo, kde „zaměstnavatelé nabízejí práci“. Je to prostředí, kde se potkává:"
        )
        st.markdown("""
        * **nabídka práce** — lidé nabízejí svůj čas, dovednosti, znalosti, odpovědnost a energii,
        * **poptávka po práci** — firmy, instituce nebo zákazníci potřebují určité činnosti vykonat,
        * **cena práce** — mzda, odměna nebo honorář, který je výsledkem hodnoty práce, dostupnosti lidí, odpovědnosti, rizika a vyjednávání.
        """)

        st.write(
            "Nejde jen o to, jestli je práce „těžká“ nebo jak moc se člověk fyzicky nadře. Mzdu ovlivňuje kombinace následujících faktorů:"
        )

        st.markdown(
            """
        | Faktor | Co znamená | Příklad z praxe |
        | :--- | :--- | :--- |
        | 💎 **Nedostatek dovedností** | Čím méně lidí danou věc umí, tím vyšší může být odměna. | Datová analýza, kyberbezpečnost, specializovaný řemeslník. |
        | ⚖️ **Odpovědnost** | Čím větší dopad má chyba, tím vyšší nároky i odměna. | Lékař, pilot, hlavní účetní, jeřábník. |
        | 🚀 **Produktivita a přidaná hodnota** | Kolik hodnoty či úspor dokáže člověk vytvořit za jednotku času. | Programátor, který automatizuje proces pro tisíce uživatelů. |
        | ⚠️ **Riziko a náročnost** | Fyzické, psychické nebo bezpečnostní nároky práce. | Práce ve zdravotnictví, výškové práce, směnný provoz. |
        | 💬 **Vyjednávací síla a region** | Schopnost doložit výsledky, praxe, reference, vzdělání a místo výkonu práce. | Portfolio, reference, praxe, Praha vs. menší regiony. |
        """,
            unsafe_allow_html=True,
        )

        st.info(
            "💡 **Příklad:** IT analytik může být placen více než administrativní asistent ne proto, že by „pracoval víc“, "
            "ale protože jeho dovednosti jsou vzácnější, mají vyšší dopad na fungování firmy a často umožňují ušetřit nebo vydělat velké částky."
        )

        st.markdown(
            """
        <div class='box-red'>
            ⚠️ <b>Zlaté pravidlo trhu práce:</b> V pracovních inzerátech, na pohovorech i v pracovní smlouvě se <b>VŽDY uvádí HRUBÁ MZDA</b>, nikoli čistá! Čistá mzda závisí na vašich osobních poměrech (zda uplatňujete slevu na studenta, na děti, invaliditu apod.), které zaměstnavatel předem nezná.
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.divider()
        st.markdown(
            "<div class='box-yellow'>🧮 <b>Interaktivní kalkulačka: Reálné faktory mzdy v ČR</b></div>",
            unsafe_allow_html=True,
        )
        st.write(
            "Vyber obor, přesný kraj, vzdělání a praxi. Kalkulačka vychází z reálných mzdových mediánů v České republice:"
        )

        col_sim1, col_sim2 = st.columns(2)
        with col_sim1:
            s_obor = st.selectbox(
                "Vyber obor / odvětví:",
                [
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
                    "Management a Vedení týmů",
                ],
                key="k4_1_1_obor",
            )

            s_kraj = st.selectbox(
                "Kraj (místo výkonu práce):",
                [
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
                    "Karlovarský kraj",
                ],
                key="k4_1_1_kraj",
            )

            s_vzdelani = st.radio(
                "Dosažené vzdělání:",
                [
                    "Výuční list / Základní",
                    "SŠ s maturitou",
                    "Vysokoškolské (Bc. / Mgr. / Ing.)",
                ],
                horizontal=True,
                key="k4_1_1_vzd",
            )

            s_praxe = st.selectbox(
                "Délka praxe v oboru:",
                [
                    "Absolvent (bez praxe)",
                    "Junior (1–3 roky praxe)",
                    "Medior (3–5 let praxe)",
                    "Senior / Expert (5+ let praxe)",
                ],
                key="k4_1_1_praxe",
            )

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
                "Management a Vedení týmů": 70000,
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
                "Karlovarský kraj": 0.88,
            }[s_kraj]

            koef_vzdelani = {
                "Výuční list / Základní": 0.90,
                "SŠ s maturitou": 1.05,
                "Vysokoškolské (Bc. / Mgr. / Ing.)": 1.25,
            }[s_vzdelani]

            koef_praxe = {
                "Absolvent (bez praxe)": 0.80,
                "Junior (1–3 roky praxe)": 1.00,
                "Medior (3–5 let praxe)": 1.18,
                "Senior / Expert (5+ let praxe)": 1.35,
            }[s_praxe]

            odhad_mzdy = int(
                base_obor * koef_kraj * koef_vzdelani * koef_praxe
            )

            st.metric(
                "Odhadovaná HRUBÁ mzda v inzerátu",
                f"{odhad_mzdy:,} Kč".replace(",", " "),
            )

            if st.button("Uložit odhad mzdy 💾", key="btn_k4_1_1"):
                mzda_data = (
                    f"Obor: {s_obor} | Kraj: {s_kraj} | Vzdělání: {s_vzdelani} |"
                    f" Praxe: {s_praxe} | Odhad: {odhad_mzdy} Kč"
                )
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"](
                        "Kapitola 4",
                        "Podkapitola 1.1 - Kalkulačka mzdy",
                        mzda_data,
                    )
                st.success("Odhad mzdy byl uložen!")

    elif selected_section_4 == "1.2 Trh práce 4.0 a AI":
        st.markdown("### 1.2 Trh práce 4.0 a AI")
        st.write(
            "Trh práce se mění rychleji než dříve. Tradiční představa, že po škole nastoupíte do jedné firmy a"
            " zůstanete v ní 40 let, už neplatí. Důvodem jsou zejména:"
        )

        st.markdown("""
        * ⚙️ **Automatizace** — stroje a software přebírají rutinní a opakující se úkoly.
        * 🤖 **Umělá inteligence (AI)** — pomáhá psát, analyzovat data, vyhledávat, překládat, kódovat, navrhovat grafiku i vyhodnocovat dokumenty.
        * 🏠 **Remote work a hybridní práce** — práce na dálku rozšiřuje konkurenci i možnosti (můžete pracovat z regionu pro pražskou nebo zahraniční firmu).
        * 📲 **Platformová ekonomika (Gig Economy)** — část práce se přesouvá do aplikací a digitálních platforem (Uber, Bolt, Foodora, Freelance portály).
        * 🌐 **Globální trh práce** — u některých profesí nekonkurujete jen lidem z města nebo ze třídy, ale pracovníkům z celého světa.
        """)

        st.markdown(
            """
        <div class='box-purple'>
            🤖 <b>Důležité pravidlo AI na trhu práce:</b><br>
            AI většinou nenahrazuje celé profese najednou. Častěji mění jednotlivé činnosti uvnitř profese. Člověk, který AI umí používat, může získat výhodu proti člověku, který ji ignoruje.<br><br>
            <b>Platí krédo:</b> <i>„AI vás o práci nepřipraví. O práci vás připraví člověk, který s AI umí pracovat lépe než vy.“</i>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.divider()
        st.markdown(
            "<div class='box-yellow'>🧩 <b>Kvíz: Jak AI mění jednotlivé obory?</b></div>",
            unsafe_allow_html=True,
        )

        with st.form("kviz_ai_trh"):
            q_ai1 = st.radio(
                "Co udělá AI s profesí účetního / datového analytika?",
                [
                    "Zruší ji úplně ze dne na den",
                    (
                        "Přebere rutinní zadávání faktur, analytik se posune k"
                        " poradenství a strategii"
                    ),
                    "Nebude mít na profesi žádný vliv",
                ],
                key="k4_1_2_q1",
            )
            q_ai2 = st.radio(
                "Jaká je největší výhoda znalosti AI nástrojů pro juniorního zaměstnance?",
                [
                    "Může v práci 8 hodin spát a nic nedělat",
                    (
                        "Zvýší svou produktivitu, zrychlí rutinní úkoly a"
                        " přinese firmě vyšší hodnotu"
                    ),
                    (
                        "Díky AI nemusí mít žádné vzdělání ani kritické"
                        " myšlení"
                    ),
                ],
                key="k4_1_2_q2",
            )

            if st.form_submit_button("Vyhodnotit a uložit kvíz 💾"):
                if (
                    "Přebere rutinní zadávání" in q_ai1
                    and "Zvýší svou produktivitu" in q_ai2
                ):
                    st.success(
                        "✅ Přesně tak! AI posouvá lidi od rutiny k řešení složitějších problémů."
                    )
                else:
                    st.error(
                        "Zkus to znovu. Pamatuj, že AI nahrazuje úkoly, ne lidskou odpovědnost a kritické myšlení."
                    )

                ai_quiz_data = f"1: {q_ai1} | 2: {q_ai2}"
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"](
                        "Kapitola 4",
                        "Podkapitola 1.2 - Kvíz AI na trhu práce",
                        ai_quiz_data,
                    )

    elif selected_section_4 == "1.3 Profese a dovednosti budoucnosti":
        st.markdown("### 1.3 Profese a dovednosti budoucnosti")
        st.write(
            "Technické znalosti konkrétního softwaru stárnou. Co zůstává trvale cenné, jsou **hard skills (odborné dovednosti)** spojené s **soft skills (měkkými dovednostmi)**."
        )

        col_sk1, col_sk2 = st.columns(2)
        with col_sk1:
            st.markdown("##### 🧠 Klíčové dovednosti budoucnosti:")
            st.markdown("""
            * 🔍 **Práce s informacemi a ověřování zdrojů** (kritické myšlení),
            * 💬 **Komunikace a spolupráce**,
            * 💻 **Digitální gramotnost**,
            * 🤖 **Práce s AI nástroji a prompting**,
            * 📊 **Analytické a logické myšlení**,
            * 🎨 **Kreativita a inovativnost**,
            * 🔄 **Schopnost učit se nové věci** (Adaptabilita),
            * 🧘 **Odolnost vůči stresu**,
            * 🛡️ **Etické rozhodování**.
            """)
        with col_sk2:
            st.markdown("##### 🤝 Lidské dovednosti (které AI nenahradí):")
            st.markdown("""
            * 💬 **Empatie, naslouchání a vyjednávání**,
            * 👥 **Týmové vedení a motivace lidí**,
            * 🛡️ **Morální odpovědnost a lidský úsudek**,
            * 🧘 **Resilience (psychická odolnost vůči změnám)**.
            """)

        st.divider()
        st.markdown(
            "<div class='box-purple'>🧪 <b>Mini-úkol: AI Rozřazovač činností u profesí</b></div>",
            unsafe_allow_html=True,
        )
        st.write(
            "Vyberte jednu profesi, která vás zajímá. Zkuste rozřadit její činnosti do tří skupin:\n"
            "1. Co může AI převzít?\n"
            "2. Co může AI zrychlit?\n"
            "3. Co zůstane silně lidské?"
        )

        profese_vyber = st.selectbox(
            "Vyber profesi k analýze:",
            [
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
                "Novinář / Copywriter",
            ],
            key="k4_1_3_profese",
        )

        if profese_vyber != "Vyber...":
            if "vykresli_otazku_fn" in st.session_state:
                st.session_state["vykresli_otazku_fn"](
                    "4.1.1",
                    f"Rozřaď náplň práce pro profesi ({profese_vyber}): Co přebere AI, co AI zrychlí a co zůstane čistě lidské?",
                    "4",
                    st.session_state.get("ulozene_odpovedi", {}),
                )

    elif selected_section_4 == "1.4 Osobní brand a digitální stopa":
        st.markdown("### 1.4 Osobní brand a digitální stopa")
        st.markdown(
            """
        <div class='box-blue'>
            🔎 <b>Otázka k zamyšlení:</b> Kdyby si vás budoucí zaměstnavatel vyhledal online, co by o vás zjistil? Pomohlo by vám to, nebo uškodilo?
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.write(
            "Zaměstnavatel často nehledá jen „životopis“. Hledá důkaz, že člověk umí přemýšlet, komunikovat a pracovat na sobě. "
            "**Osobní brand (osobní značka)** je obraz, který o sobě dlouhodobě vytváříte."
        )

        st.markdown("##### Co tvoří tvůj osobní brand:")
        st.markdown("""
        * 📄 **Životopis (CV)**,
        * 🎨 **Portfolio** (reálné ukázky prací a projektů),
        * 🌐 **LinkedIn nebo jiný profesní profil**,
        * 🏆 **Školní a osobní projekty, dobrovolnictví a soutěže**,
        * 📱 **Komunikace na sociálních sítích a digitální stopa**,
        * 💬 **Reference** od učitelů či předchozích zaměstnavatelů,
        * 🔍 **Výsledky dohledatelné online**.
        """)

        st.divider()
        st.markdown(
            "<div class='box-yellow'>📋 <b>Audit tvé digitální stopy (Rychlá kontrola)</b></div>",
            unsafe_allow_html=True,
        )
        st.write("Zaškrtni položky, které máš v pořádku:")

        d1 = st.checkbox(
            "Mám uzamčené soukromé profily (Instagram/Facebook) nebo na nich"
            " nemám nevhodný obsah (alkohol, vulgarismy).",
            key="k4_1_4_d1",
        )
        d2 = st.checkbox(
            "Mám založený a vyplněný profesní profil na LinkedIn nebo online"
            " portfolio svých prací.",
            key="k4_1_4_d2",
        )
        d3 = st.checkbox(
            "Moje e-mailová adresa v životopisu je profesionální (např."
            " jmeno.prijmeni@email.cz, ne dravec123@seznam.cz).",
            key="k4_1_4_d3",
        )
        d4 = st.checkbox(
            "Kdybych si zadal/a své jméno do Google, nevyjedou žádné"
            " kompromitující fotografie nebo komentáře.",
            key="k4_1_4_d4",
        )

        score_d = sum([d1, d2, d3, d4])
        st.progress(score_d / 4)

        if score_d == 4:
            st.success(
                "🎉 **Vynikající! Tvá digitální stopa působí profesionálně a bezpečně.**"
            )
        elif score_d >= 2:
            st.info(
                "👍 Dobrý základ! Podívej se na nezaškrtnutá políčka a vylepši"
                " je před posíláním první přihlášky na brigádu či práci."
            )
        else:
            st.warning(
                "⚠️ **Pozor!** Zaměstnavatelé si uchazeče běžně vyhledávají."
                " Vyčisti si veřejné profily a založ si profesionální e-mail."
            )

        if st.button("Uložit audit digitální stopy 💾", key="btn_k4_1_4"):
            audit_data = f"Skóre audit stopy: {score_d}/4"
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"](
                    "Kapitola 4",
                    "Podkapitola 1.4 - Audit digitální stopy",
                    audit_data,
                )
            st.success("Audit byl uložen!")

        st.divider()
        st.markdown(
            "#### 📱 Hybridní prvek učebnice: Otestuj si profese budoucnosti"
        )
        st.write(
            "Naskenuj QR kód nebo klikni na tlačítko a vyzkoušej si oficiální kariérní dotazník národního systému kvalifikací na test „Jaká profese budoucnosti se ke mně hodí?“ a na aktuální přehled pracovních nabídek v regionu nebo oboru:"
        )

        col_qr1, col_qr2 = st.columns([1, 2])
        with col_qr1:
            st.image(
                "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://www.nsp.cz",
                caption="Kariérní kompas NSP.cz",
                width=150,
            )
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
        st.markdown("## 2. Hra podle pravidel: HR, získání práce a pracovní právo")
        st.markdown("### 2.1 HR a personalistika: co znamenají")
        st.markdown(
            """
        <div class='box-blue'>
            ⚖️ <b>Základní otázka:</b> Jak získat práci, porozumět roli HR a zároveň se nenechat nachytat na neférové podmínky?
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.write(
            "**HR** znamená *Human Resources* — lidské zdroje. V češtině"
            " se často používá pojem **personalistika**. Jde o oblast, která řeší"
            " lidi ve firmě: nábor, smlouvy, adaptaci nováčků, vzdělávání, hodnocení,"
            " odměňování, benefity, firemní kulturu i ukončování pracovního poměru."
        )
        st.write(
            "Personalistika není jen „oddělení, které vede pohovory“. Dobré HR pomáhá"
            " firmě najít vhodné lidi, nastavit férové podmínky a podporovat vztah"
            " mezi zaměstnavatelem a zaměstnanci."
        )

        st.markdown("#### Co HR ve firmě obvykle řeší")
        st.markdown(
            """
        | Oblast HR | Co znamená | Příklad z praxe |
        | :--- | :--- | :--- |
        | 🔍 **Nábor a výběr** | Hledání vhodných uchazečů a vedení výběrového řízení. | Pracovní inzerát, pohovor, testovací úkol. |
        | 🚀 **Onboarding** | Zaškolení a začlenění nového člověka do firmy. | První den v práci, školení, mentor. |
        | 📄 **Pracovní dokumentace** | Smlouvy, dohody, mzdové výměry, interní pravidla. | Pracovní smlouva, DPP, DPČ, dodatky. |
        | 💵 **Odměňování a benefity** | Nastavení mzdy, bonusů, benefitů a dalších forem odměny. | Mzda, prémie, stravenky, home office. |
        | 📈 **Hodnocení a rozvoj** | Zpětná vazba, cíle, vzdělávání a kariérní růst. | Hodnoticí rozhovor, kurz, plán rozvoje. |
        | 🤝 **Firemní kultura** | Způsob komunikace, spolupráce a řešení problémů ve firmě. | Atmosféra v týmu, pravidla komunikace, řešení konfliktů. |
        | 🚪 **Offboarding** | Proces odchodu zaměstnance z firmy. | Výstupní pohovor, předání práce, potvrzení dokumentů. |
        """,
            unsafe_allow_html=True,
        )

        st.markdown("#### HR z pohledu uchazeče")
        st.write("Při hledání práce se HR může objevit v několika rolích:")
        st.markdown("""
        * připravuje nebo zveřejňuje pracovní inzerát,
        * komunikuje s uchazeči,
        * vede nebo organizuje pohovor,
        * posílá testovací úkol,
        * vysvětluje benefity a podmínky,
        * připravuje smluvní dokumenty,
        * předává informace o nástupu.
        """)

        st.info(
            "📌 **Praktická poznámka:** HR není automaticky „kamarád uchazeče“, ale ani nepřítel. "
            "HR zastupuje zaměstnavatele, zároveň by mělo hlídat férový, profesionální a zákonný průběh náboru i pracovního vztahu."
        )

        with st.expander("📖 HR pojmy, které se hodí znát (Slovníček)"):
            st.markdown("""
            * **Recruitment:** Nábor nových zaměstnanců.
            * **Recruiter:** Člověk, který vyhledává a oslovuje uchazeče.
            * **HR generalist:** Personalista, který řeší širší agendu HR.
            * **Talent acquisition:** Strategické vyhledávání lidí s vhodnými dovednostmi.
            * **Onboarding:** Zaškolení a začlenění nového člověka.
            * **Employer branding:** Budování pověsti zaměstnavatele.
            * **Performance review:** Hodnocení pracovního výkonu.
            * **Offboarding:** Proces odchodu z firmy.
            """)

        st.divider()
        st.markdown(
            "<div class='box-yellow'>🧪 <b>Mini-úkol: Detektiv firemní kultury z inzerátu</b></div>",
            unsafe_allow_html=True,
        )
        st.write(
            "Vyberte jeden pracovní inzerát a určete, co v něm vypovídá o HR a firemní kultuře. Je komunikace konkrétní, férová a srozumitelná, nebo spíš neurčitá a plná frází?"
        )

        inzerat_typ = st.radio(
            "Vyber znění fiktivního inzerátu k analýze:",
            [
                (
                    "1️⃣ 'Hledáme dynamického nindžu do mladého kolektivu!"
                    " Nabízíme práci pod tlakem, prémie dle výkonu a"
                    " multisportku.'"
                ),
                (
                    "2️⃣ 'Hledáme juniorního účetního. Nabízíme 38 000 Kč"
                    " hrubého, zkušební dobu 3 měsíce, fixní pracovní dobu a"
                    " 25 dní dovolené.'"
                ),
                (
                    "3️⃣ 'Atraktivní výdělek až 100 000 Kč měsíčně! Žádný šéf,"
                    " svoboda. Nutné vlastní IČO, zápisné 2 000 Kč za školení.'"
                ),
                (
                    "4️⃣ 'Jsme rodinná firma s tradicí. Hledáme loajálního"
                    " pracovníka, který se nebojí vzít za práci. Odměna dohodou"
                    " na pohovoru.'"
                ),
                (
                    "5️⃣ 'Do startupu hledáme rockstar vývojáře! Neomezená"
                    " dovolená, fotbálek v kanclu, pizza zdarma, práce v"
                    " rychlém tempu, 10h denně není problém.'"
                ),
            ],
            key="k4_2_1_inz",
        )

        if inzerat_typ.startswith("1️⃣"):
            st.warning(
                "⚠️ **Fráze a toxická kultura:** Slova jako 'nindža' nebo 'práce"
                " pod tlakem' často zakrývají chaos, obrovský stres a"
                " neplacené přesčasy. Multisportka nevyváží vyhoření."
            )
        elif inzerat_typ.startswith("2️⃣"):
            st.success(
                "✅ **Profesionální inzerát:** Jasný, stručný, transparentní."
                " Uvádí konkrétní hrubou mzdu, typ úvazku, nárok na dovolenou i"
                " očekávání. Tady HR hraje fér."
            )
        elif inzerat_typ.startswith("3️⃣"):
            st.error(
                "🚨 **Kritický RED FLAG:** Slib pohádkových příjmů, nutnost"
                " vlastního IČO pro juniora a poplatek předem za školení = znak"
                " nelegálního Švarcsystému nebo letadla!"
            )
        elif inzerat_typ.startswith("4️⃣"):
            st.info(
                "🤔 **Riziko zneužití:** 'Rodinná firma' a 'nebojí se vzít za"
                " práci' často v překladu znamená: děláte práci za 3 lidi. A"
                " chybějící mzda ukazuje neochotu být transparentní."
            )
        elif inzerat_typ.startswith("5️⃣"):
            st.warning(
                "🍕 **Past na mladé (Hustle culture):** Pizza a fotbálek znějí"
                " super, ale '10h denně není problém' a 'rockstar' znamená, že"
                " tam necháte duši a osobní život. Benefity mají jen udržet lidi"
                " déle v kanceláři."
            )

        if st.button("Uložit analýzu inzerátu 💾", key="btn_k4_2_1"):
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"](
                    "Kapitola 4",
                    "Podkapitola 2.1 - Detektiv inzerátu",
                    inzerat_typ[:30],
                )
            st.success("Analýza inzerátu byla uložena!")

    elif selected_section_4 == "2.2 Nábor v éře AI":
        st.markdown("### 2.2 Nábor v éře AI")
        st.write(
            "Nábor už často nezačíná u člověka. Životopisy mohou nejdříve procházet přes systémy **ATS (Applicant Tracking System)**,"
            " tedy software, který pomáhá třídit uchazeče podle klíčových slov a požadavků."
        )

        st.markdown("##### 📌 Co z toho plyne v praxi:")
        st.markdown("""
        * 📄 **Přehledný formát:** Životopis má být přehledný a čitelný. Vyhněte se složitým grafickým sloupcům, které ATS nepřečte.
        * 🔑 **Klíčová slova:** Názvy dovedností mají odpovídat inzerátu.
        * 🎯 **Mírná úprava na míru:** Není dobré posílat jeden stejný životopis na všechny (20 různých) pozic.
        * 🖼️ **Portfolio jako trumf:** Konkrétní ukázka práce (web, grafika, text) může být silnější než obecná tvrzení.
        * 🤖 **Pomoc AI, ale s opatrností:** AI může pomoci s přípravou, ale nesmí za vás vymýšlet nepravdivé zkušenosti.
        """)

        st.divider()
        st.markdown(
            "<div class='box-purple'>🤖 <b>Interaktivní trenažér: Pohovor nanečisto s AI</b></div>",
            unsafe_allow_html=True,
        )
        st.write(
            "Chceš si vyzkoušet pohovor na jakoukoliv brigádu nebo pozici"
            " nanečisto? Zkopíruj si tento speciální prompt a vlož ho do ChatGPT"
            " nebo Claude:"
        )

        pozice_input = st.text_input(
            "Zadej pozici, na kterou se chceš připravit (např. Prodavač, Junior"
            " vývojář, Asistent/ka):",
            value="Prodavač v e-shopu",
            key="k4_2_2_pozice",
        )

        prompt_text = (
            "Chovej se jako přísný, ale férový HR manažer. Ucházím se o pozici"
            f" {pozice_input}. Ptej se mě postupně na otázky jako u pracovního"
            " pohovoru. Po pěti otázkách mi dej zpětnou vazbu: co bylo přesvědčivé,"
            " co bylo slabé a jak bych mohl/a odpovědi zlepšit."
        )

        st.markdown(
            f"""
        <div style="background-color: #f8f9fa; padding: 15px; border-left: 5px solid #8b5cf6; border-radius: 5px; font-family: monospace; font-size: 1.1em; color: #333; white-space: pre-wrap; word-wrap: break-word; line-height: 1.5;">
        {prompt_text}
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.caption(
            "💡 Tip: Označ text výše, zkopíruj (Ctrl+C / Cmd+C) a vlož ho"
            " rovnou do svého oblíbeného AI chatu."
        )

    elif selected_section_4 == "2.3 Životopis, motivační dopis a portfolio":
        st.markdown("### 2.3 Životopis, motivační dopis a portfolio")
        st.write(
            "Dobré materiály nejsou seznamem všeho, co jste v životě dělali."
            " Jsou jasnou odpovědí na otázku: **Proč se hodím právě na tuto"
            " konkrétní pozici?**"
        )

        st.markdown("#### 📄 Životopis by měl ukázat:")
        st.markdown("""
        * kdo jsem,
        * co umím,
        * jaké mám zkušenosti,
        * co jsem vytvořil/a,
        * jaké mám výsledky,
        * jak mě lze kontaktovat.
        """)

        st.write(
            "**Portfolio** je důkaz schopností. Může obsahovat školní projekt, grafiku, web, prezentaci, fotografii výrobku, analýzu, text, video, dobrovolnickou aktivitu nebo ukázku práce."
        )

        st.markdown("#### 🖼️ Pěkná ukázka životopisu")
        st.write(
            "Vizuální životopis může obsahovat i fotografii, pokud se hodí k dané pozici a působí profesionálně. "
            "Důležité je, aby byl přehledný, čitelný, stručný a aby grafika nepřebila obsah."
        )

        try:
            st.image(
                "ukazka_zivotopisu.png",
                caption="Vzorový strukturovaný životopis (Ing. Petr Novák)",
                use_container_width=True,
            )
        except Exception:
            st.markdown(
                """
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
            """,
                unsafe_allow_html=True,
            )

        st.warning("⚠️ **Pozor:** Fotografie v životopisu není vždy nutná. Pokud se použije, měla by být kvalitní, přirozená, slušná a profesně vhodná — ne selfie, momentka z dovolené ani příliš upravená fotka.")

        st.divider()
        st.markdown(
            "#### 🔍 Proč tento životopis funguje a na co si dát pozor"
        )

        st.markdown(
            """
        | Část životopisu | Proč je důležitá | Na co si dát pozor |
        | :--- | :--- | :--- |
        | 👤 **Profil / Hlavička** | Rychle shrne, kdo se hlásí a co může nabídnout. | Nepoužívat prázdné fráze typu „jsem flexibilní a dynamický člověk“ bez důkazu. |
        | 🎓 **Vzdělání** | U žáků a absolventů často nahrazuje dlouhou pracovní praxi. | Vybrat jen relevantní předměty, projekty nebo úspěchy. |
        | 💼 **Praxe a projekty** | Ukazují konkrétní zkušenost, i když nejde o klasické zaměstnání. | Psát konkrétní činnosti, ne jen název akce nebo projektu. |
        | 🧠 **Dovednosti** | Pomáhají HR rychle posoudit, jestli člověk odpovídá inzerátu. | Nepřehánět úroveň znalostí. U pohovoru se může ověřovat. |
        | 🔗 **Kontakt a odkazy** | Usnadňují další komunikaci a ukazují portfolio. | E-mail má působit profesionálně, ne jako přezdívka z dětství. |
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
        <div class='box-red'>
            🚩 <b>Co do životopisu RADĚJI NEPATŘÍ:</b> Neprofesionální e-mail, nepravdivé zkušenosti, příliš osobní informace, dlouhé odstavce, pravopisné chyby, fotografie z dovolené nebo seznam dovedností, které s pozicí vůbec nesouvisí.
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.divider()
        st.markdown(
            "<div class='box-yellow'>🧪 <b>Mini úkol: Kontrolor životopisu</b></div>",
            unsafe_allow_html=True,
        )
        st.write(
            "Vyberte si jednu pracovní nabídku a upravte ukázkový životopis tak, aby odpovídal konkrétní pozici. "
            "Zvýrazněte dovednosti, projekty a zkušenosti, které jsou pro danou práci nejdůležitější. Níže si pak otestuj odhalování chyb:"
        )

        with st.form("form_cv_check"):
            st.write(
                "Vyber, které z následujících prvků v životopisu jsou CHYBNÉ:"
            )
            cv_c1 = st.checkbox(
                "E-mail: dravec_ostrava_69@seznam.cz", key="k4_2_3_c1"
            )
            cv_c2 = st.checkbox(
                "Odrážka u praxe: 'Koordinace 4členného týmu při organizaci školního plesu'",
                key="k4_2_3_c2",
            )
            cv_c3 = st.checkbox(
                "Dovednosti: 'Práce na PC - 100 %, Angličtina - 100 %'",
                key="k4_2_3_c3",
            )
            cv_c4 = st.checkbox(
                "Fotografie: Selfie v zrcadle v tělocvičně", key="k4_2_3_c4"
            )

            if st.form_submit_button("Zkontrolovat a uložit 💾"):
                if cv_c1 and not cv_c2 and cv_c3 and cv_c4:
                    st.success(
                        "🎉 **Skvěle! Odhalil/a jsi všechny chyby!**\n* Neformální"
                        " e-mail působí neprofesionálně.\n* Hodnocení v"
                        " procentech (100 %) je subjektivní nesmysl (raději"
                        " uvádějte úrovně A1-C2 nebo konkrétní dovednosti).\n*"
                        " Selfie v zrcadle do CV nepatří."
                    )
                else:
                    st.error(
                        "Něco jsi přehlédl/a. Správné odrážky s výsledky (jako u"
                        " plesu) jsou v pořádku, ale neformální e-maily,"
                        " procentuální stupnice a selfie jsou chyby!"
                    )

                cv_check_data = (
                    f"Chyby označené: 1:{cv_c1}, 2:{cv_c2}, 3:{cv_c3},"
                    f" 4:{cv_c4}"
                )
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"](
                        "Kapitola 4",
                        "Podkapitola 2.3 - Kontrolor životopisu",
                        cv_check_data,
                    )

    elif selected_section_4 == "2.4 Pracovní smlouva, DPP a DPČ":
        st.markdown("### 2.4 Pracovní smlouva, DPP a DPČ")
        st.markdown(
            """
        <div class='box-blue'>
            ⚖️ <b>Základní princip:</b> V České republice existuje více forem práce. Každá má jiné výhody, zákonné povinnosti, odvody a míru právní ochrany.
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown("""
        | Forma práce | Kdy se používá | Typická výhoda | Typické riziko |
        | :--- | :--- | :--- | :--- |
        | **Pracovní poměr** | Dlouhodobá práce. | Vyšší ochrana, dovolená, stabilita. | Menší flexibilita. |
        | **DPP (Dohoda o provedení práce)** | Menší rozsah práce, brigády. | Jednoduchost, flexibilita. | Limity hodin, menší jistota. |
        | **DPČ (Dohoda o pracovní činnosti)** | Pravidelnější menší úvazek. | Vhodné pro částečnou práci. | Závisí na rozsahu a odvodech. |
        | **OSVČ** | Podnikání na vlastní účet. | Samostatnost. | Odpovědnost, nejistý příjem. |
        | **Freelancer** | Projektová práce. | Volnost a různí klienti. | Nutnost shánět zakázky. |
        | **Platformová práce** | Aplikace typu rozvoz, doprava, mikropráce. | Rychlý vstup. | Slabší ochrana, kolísavý příjem. |
        """)

        st.divider()
        st.markdown("#### ⚖️ DPP a DPČ: rozdíly a zákonné povinnosti")
        st.write(
            "DPP a DPČ jsou dohody o pracích konaných mimo pracovní poměr. Nejde tedy o klasický pracovní poměr, ale pořád platí, že práce musí mít jasná pravidla, písemnou dohodu a zákonnou ochranu."
        )

        st.markdown(
            """
        | Oblast | DPP (Dohoda o provedení práce) | DPČ (Dohoda o pracovní činnosti) |
        | :--- | :--- | :--- |
        | **Typické použití** | Jednorázová, nárazová nebo menší práce. | Pravidelnější práce menšího rozsahu. |
        | **Rozsah práce (Limit)** | Nejvýše **300 hodin za kalendářní rok** u jednoho zaměstnavatele. | Práce nesmí v průměru překročit polovinu stanovené týdenní pracovní doby (prakticky cca **20 hodin týdně**). |
        | **Písemná forma** | **Musí být vždy uzavřena písemně!** | **Musí být vždy uzavřena písemně!** |
        | **Co má obsahovat** | Druh práce, rozsah práce, doba trvání, odměna a podmínky. | Sjednaná práce, rozsah pracovní doby, doba trvání, odměna a podmínky. |
        | **Odvody (Soc/Zdr)** | Odvádí se až při překročení zákonného měsíčního limitu příjmu. | U pravidelnější práce vzniká povinnost odvodů častěji než u nárazové DPP. |
        | **Daň z příjmů** | Řeší se podle výše odměny a podpisu prohlášení poplatníka. | Řeší se podle výše odměny a podpisu prohlášení poplatníka. |
        | **Dovolená** | Může vzniknout nárok při splnění zákonných podmínek a rozsahu. | Může vzniknout nárok při splnění zákonných podmínek a rozsahu. |
        | **Ukončení dohody** | Lze ukončit písemnou výpovědí s **15denní lhůtou**. | Lze ukončit písemnou výpovědí s **15denní lhůtou**. |
        """,
            unsafe_allow_html=True,
        )

        st.warning(
            "⚠️ **Zákonné minimum u DPP a DPČ:** Dohoda má být písemná, odměna nesmí porušovat pravidla minimální mzdy, zaměstnavatel musí vést evidenci odpracované doby, řešit bezpečnost práce, případné příplatky a odvody. Zaměstnanec by měl dostat jasně uvedeno, co bude dělat, za kolik, kdy, kde a v jakém rozsahu."
        )

        st.markdown(
            """
        <div class='box-green'>
            💡 <b>Jednoduchá pomůcka do praxe:</b><br>
            • <b>DPP</b> se hodí spíše na menší a nárazovou práci (např. jednorázová výpomoc, akce, krátká letní brigáda na festivalu).<br>
            • <b>DPČ</b> se hodí spíše na pravidelnější práci v menším rozsahu (např. několik směn týdně po delší dobu v kavárně).
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.info("Na co si dát pozor: Pokud člověk pracuje dlouhodobě, pravidelně, podle směn zaměstnavatele a ve větším rozsahu, nemusí být DPP vhodná forma. Vždy je potřeba hlídat rozsah hodin, odvody, písemnou dohodu, výši odměny a to, zda dohoda nezastírá běžný pracovní poměr.")
        st.caption("*Pozor: U konkrétních částek, limitů a sazeb se pravidla mohou měnit. Učebnice vysvětluje princip, pro aktuální limity sledujte portál MPSV nebo kalkulačky.*")

    elif selected_section_4 == "2.5 Ukázka pracovní smlouvy a její náležitosti":
        st.markdown("### 2.5 Ukázka pracovní smlouvy a její povinné náležitosti")
        st.write(
            "Pracovní smlouva musí být **uzavřena písemně**. Než ji člověk podepíše, měl by rozumět nejen mzdě, "
            "ale i druhu práce, místu výkonu práce, pracovní době, zkušební době, dovolené, odpovědnosti a způsobu ukončení."
        )

        st.markdown("#### 📝 Povinné náležitosti pracovní smlouvy")
        st.write(
            "Pracovní smlouva musí ze zákona (Zákoníku práce) obsahovat **tři základní povinné údaje**. Pokud byť jen jeden chybí, je smlouva neplatná:"
        )

        st.markdown("""
        * **1. Druh práce:** Jakou práci bude zaměstnanec vykonávat. *(Na co si dát pozor: Příliš široký popis může znamenat, že člověk bude dělat skoro všechno).*
        * **2. Místo výkonu práce:** Kde bude práce vykonávána. *(Na co si dát pozor: Příliš široké místo, například „Česká republika“, může znamenat časté přesuny a služební cesty).*
        * **3. Den nástupu do práce:** Od kdy pracovní poměr vzniká. *(Na co si dát pozor: Od tohoto dne vznikají práva a povinnosti zaměstnance i zaměstnavatele).*
        """)

        st.markdown(
            """
        <div class='box-red'>
            🚨 <b>Pozor na mzdový výměr:</b><br>
            Mzda není vždy přímo v pracovní smlouvě. Může být uvedena v samostatném <b>mzdovém výměru</b>. I tak musí být zaměstnanci jasné, jaká mzda mu náleží, kdy se vyplácí a za jakých podmínek.<br>
            • Co je ve <b>smlouvě</b>, lze změnit jen s vaším písemným souhlasem.<br>
            • <b>Mzdový výměr</b> může zaměstnavatel jednostranně změnit i bez vás (nesmí jít pod minimální mzdu).
        </div>
        """,
            unsafe_allow_html=True,
        )

        with st.expander("📋 Co by měla smlouva nebo související dokumenty ještě řešit:"):
            st.markdown("""
            Kromě povinných náležitostí je praktické zkontrolovat také:
            - označení zaměstnance a zaměstnavatele,
            - délku pracovního poměru — na dobu určitou, nebo neurčitou,
            - délku úvazku a rozvržení směn,
            - zkušební dobu,
            - mzdu nebo plat a způsob odměňování,
            - výplatní termín a způsob výplaty,
            - nárok na dovolenou,
            - benefity a příspěvky,
            - místo a způsob výkonu práce na dálku (home office),
            - mlčenlivost a ochranu dat,
            - odpovědnost za svěřené věci,
            - pravidla pro přesčasy a pohotovost,
            - výpovědní dobu a odkaz na vnitřní předpisy zaměstnavatele.
            """)

        st.markdown("#### 📄 Modelová ukázka pracovní smlouvy (zjednodušený výukový vzor)")
        st.markdown(
            """
        <div style="background-color: #ffffff; padding: 25px; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; color: #1e293b; margin-bottom: 20px;">
            <h3 style="margin-top: 0; color: #0f172a; text-align: center; border-bottom: 2px solid #0284c7; padding-bottom: 10px;">PRACOVNÍ SMLOUVA</h3>
            <p><b>Zaměstnavatel:</b> ABC služby, s. r. o., IČO: 12345678, se sídlem Praha 1, Vzorová 10<br>
            <b>Zaměstnanec:</b> Jana Nováková, datum narození 12. 5. 2007, bydliště Brno, Ulice 15</p>
            <ol style="font-size: 0.95rem; line-height: 1.6;">
                <li><b>Druh práce:</b> administrativní pracovník/pracovnice zákaznické podpory</li>
                <li><b>Místo výkonu práce:</b> Brno, pobočka zaměstnavatele, případně home office po předchozí domluvě</li>
                <li><b>Den nástupu do práce:</b> 1. 9. 2026</li>
                <li><b>Pracovní poměr:</b> na dobu neurčitou</li>
                <li><b>Úvazek:</b> 40 hodin týdně</li>
                <li><b>Zkušební doba:</b> 3 měsíce</li>
                <li><b>Mzda:</b> 32 000 Kč hrubého měsíčně podle mzdového výměru</li>
                <li><b>Výplatní termín:</b> do 15. dne následujícího měsíce na bankovní účet zaměstnance</li>
                <li><b>Dovolená:</b> podle zákoníku práce a vnitřních předpisů zaměstnavatele</li>
                <li><b>Ostatní práva a povinnosti:</b> řídí se zákoníkem práce, touto smlouvou a vnitřními předpisy zaměstnavatele</li>
            </ol>
            <div style="display: flex; justify-content: space-between; margin-top: 25px;">
                <div>V Brně dne 20. 8. 2026<br><br>..........................................<br>Podpis zaměstnance</div>
                <div><br><br>..........................................<br>Podpis zaměstnavatele</div>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
        <div class='box-red'>
            🚩 <b>Red flags ve smlouvě:</b> Nejasný druh práce, chybějící místo výkonu práce, tlak na okamžitý podpis bez přečtení, mzda jen „ústně“, práce na IČO při jasně zaměstnaneckém režimu, neurčité formulace typu „zaměstnanec vykonává i další činnosti dle potřeby zaměstnavatele“ bez rozumných hranic.
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.divider()
        st.markdown(
            "<div class='box-yellow'>🛠️ <b>Interaktivní dílna: Sestav a zkontroluj smlouvu</b></div>",
            unsafe_allow_html=True,
        )
        st.write(
            "Navrhni parametry své pracovní smlouvy a zjisti, jaké výhody nebo skrytá rizika tvá volba přináší:"
        )

        with st.form("form_smlouva"):
            f_druh = st.selectbox(
                "1. Jak specifikuješ druh práce?",
                [
                    "Přesná pozice: 'Specialista marketingu a správy sociálních sítí'",
                    "Všeobecná pozice: 'Pracovník provozu dle potřeb zaměstnavatele'",
                ],
                key="k4_2_5_druh",
            )

            f_misto = st.selectbox(
                "2. Jak určité bude místo výkonu práce?",
                [
                    "Přesné místo: 'Kancelář Plzeň, Květná 15'",
                    "Široké místo: 'Všechny pobočky zaměstnavatele v ČR'",
                ],
                key="k4_2_5_misto",
            )

            f_mzda = st.radio(
                "3. Kde chceš mít uvedenou svou sjednanou mzdu (45 000 Kč)?",
                [
                    "Přímo v textu Pracovní smlouvy",
                    "Na samostatném Mzdovém výměru",
                ],
                key="k4_2_5_mzda",
            )

            submit_smlouva = st.form_submit_button(
                "🔍 Vyhodnotit a uložit bezpečnost smlouvy 💾"
            )

        if submit_smlouva:
            st.markdown("##### 📊 Rozbor tvé smlouvy:")

            if "Specialista" in f_druh:
                st.success(
                    "✅ **Druh práce OK:** Máš jasně vymezené kompetence. Zaměstnavatel ti nemůže nakázat činnosti, které nesouvisí s marketingem."
                )
            else:
                st.error(
                    "⚠️ **Riziko u druhu práce:** Formulace 'dle potřeb' dává firmě možnost nutit tě do úklidu, skladu i cizí práce bez nároku na příplatek."
                )

            if "Plzeň" in f_misto:
                st.success(
                    "✅ **Místo práce OK:** Pracuješ na konkrétní adrese. Změna pobočky do jiného města by vyžadovala tvůj písemný souhlas."
                )
            else:
                st.error(
                    "⚠️ **Riziko u místa:** Při volbě 'všechny pobočky v ČR' tě firma může poslat na služební cestu či přeložit kamkoliv bez nároku na kompenzaci."
                )

            if "Přímo v textu" in f_mzda:
                st.success(
                    "🔒 **Maximální garance mzdy:** Mzda je pevně zakotvena ve smlouvě. Firma ti ji nemůže snížit, ani kdyby se jí nedařilo."
                )
            else:
                st.info(
                    "ℹ️ **Standardní praxe (Mzdový výměr):** Je to běžné, ale pozor – zaměstnavatel ti může mzdovým výměrem mzdu do budoucna jednostranně snížit."
                )

            smlouva_data = (
                f"Druh: {f_druh} | Místo: {f_misto} | Mzda v: {f_mzda}"
            )
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"](
                    "Kapitola 4",
                    "Podkapitola 2.5 - Sestavení smlouvy",
                    smlouva_data,
                )

    elif selected_section_4 == "2.6 Zkušební doba":
        st.markdown("### 2.6 Zkušební doba")
        st.write(
            "Zkušební doba slouží k tomu, aby si zaměstnanec i zaměstnavatel ověřili, zda spolupráce funguje. "
            "Není to období „bez pravidel“. I během zkušební doby má člověk práva a povinnosti. "
            "Během ní lze pracovní poměr zrušit **písemně, z jakéhokoliv důvodu i bez udání důvodu**."
        )

        st.markdown("#### ⏳ Jak dlouhá může být zkušební doba ze zákona:")
        st.markdown("""
        | Typ zaměstnance | Maximální zkušební doba | Co to znamená v praxi |
        | :--- | :--- | :--- |
        | **Běžný zaměstnanec** | Nejvýše **4 měsíce**. | Zaměstnavatel nemůže dát běžnému zaměstnanci zkušební dobu delší jen proto, že „to tak firma dělá“. |
        | **Vedoucí zaměstnanec / manažer** | Nejvýše **8 měsíců**. | U vyšších vedoucích pozic může být zkušební doba delší, protože odpovědnost a dopad rozhodnutí jsou větší. |
        | **Pracovní poměr na dobu určitou** | Nejvýše **polovina** sjednané doby. | Když je smlouva například na 6 měsíců, zkušební doba nesmí být delší než 3 měsíce. |
        """)

        st.warning("⚠️ **Důležité:** Zkušební doba musí být sjednána **písemně**. Pokud není sjednána písemně v pracovní smlouvě před nástupem, nelze se na ni jen „ústně odvolat“.")

        with st.expander("🛡️ Co si u zkušební doby hlídat & Ochrana při nemoci:"):
            st.markdown("""
            * zda je zkušební doba sjednána písemně,
            * jak dlouho trvá a od kdy přesně běží,
            * zda odpovídá typu pracovního vztahu a nepřesahuje zákonný limit,
            * jaké jsou podmínky ukončení.
            
            **Nemoc ve zkušební době:** Zaměstnavatel vás **nesmí** vyhodit během prvních 14 dnů vaší dočasné pracovní neschopnosti (nemoci). Zkušební doba se navíc o dny nemoci a překážek v práci automaticky prodlužuje.
            """)

        st.divider()
        st.markdown(
            "<div class='box-yellow'>⚖️ <b>Právní poradna: Rozhodni reálné situace</b></div>",
            unsafe_allow_html=True,
        )

        sit1 = st.radio(
            "Situace 1: Panu Novákovi končí 4měsíční zkušebka v pátek. V pondělí za ním přijde šéf s tím, že mu zkušebku 'o další měsíc prodlužuje', protože si jím ještě není jistý. Může to udělat?",
            [
                "Vyber...",
                "Ano, pokud se na tom dohodnou.",
                "Ne, zkušební dobu nelze dodatečně prodlužovat nad zákonný rámec.",
            ],
            key="k4_2_6_sit1",
        )
        if (
            sit1
            == "Ne, zkušební dobu nelze dodatečně prodlužovat nad zákonný rámec."
        ):
            st.success(
                "✅ Přesně tak! Zkušební dobu nelze po sjednání svévolně prodlužovat. Prodlužuje se pouze automaticky o celodenní překážky v práci (nemoc, dovolená)."
            )

        sit2 = st.radio(
            "Situace 2: Lenka je ve zkušební době. Zjistila, že jí práce ničí psychiku a chce okamžitě odejít. Šéf jí řekl, že musí dodržet dvouměsíční výpovědní lhůtu. Má pravdu?",
            [
                "Vyber...",
                "Ano, výpovědní lhůta platí vždy.",
                "Ne, ve zkušební době může odejít ze dne na den (písemně).",
            ],
            key="k4_2_6_sit2",
        )
        if (
            sit2
            == "Ne, ve zkušební době může odejít ze dne na den (písemně)."
        ):
            st.success(
                "✅ Správně! Kouzlo zkušební doby funguje obousměrně. Pokud se vám tam nelíbí, doručíte písemné zrušení a zítra už v práci nemusíte být."
            )

        if st.button("Uložit řešení situací zkušební doby 💾", key="btn_k4_2_6"):
            sit_data = f"Situace 1: {sit1} | Situace 2: {sit2}"
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"](
                    "Kapitola 4",
                    "Podkapitola 2.6 - Zkušební doba situace",
                    sit_data,
                )
            st.success("Odpovědi byly uloženy!")

    elif selected_section_4 == "2.7 Smlouva na dobu určitou a neurčitou":
        st.markdown("### 2.7 Smlouva na dobu určitou a neurčitou")
        st.write(
            "Pracovní poměr může být sjednán na dobu určitou, nebo neurčitou. "
            "**Doba určitá** znamená, že smlouva má předem daný konec. **Doba neurčitá** znamená stabilnější pracovní vztah bez předem stanoveného data konce."
        )

        st.markdown("#### 🔄 Pravidlo „3 a dost“")
        st.write(
            "U pracovního poměru na dobu určitou platí jednoduchá zákonná pomůcka pro ochranu zaměstnanců před řetězením smluv:"
        )

        st.markdown("""
        | Pravidlo | Význam | Příklad |
        | :--- | :--- | :--- |
        | **1. Maximálně 3 roky** | Jedna smlouva na dobu určitou může být sjednána nejvýše na 3 roky. | Smlouva od 1. 9. 2026 do 31. 8. 2029. |
        | **2. Nejvýše 2 opakování** | Zaměstnavatel může dobu určitou po první smlouvě ještě dvakrát prodloužit nebo znovu sjednat. | 1. smlouva + 1. prodloužení + 2. prodloužení. |
        | **3. Celkem zpravidla 3 smlouvy** | Po vyčerpání pravidla by další pokračování mělo být na dobu neurčitou. | Zaměstnanec nemá donekonečna dostávat nové krátké smlouvy. |
        """)

        st.markdown(
            """
        <div class='box-green'>
            💡 <b>Jednoduchá pomůcka & Automatická změna:</b><br>
            Zaměstnavatel vám zpravidla nemůže dávat smlouvu na dobu určitou pořád dokola. Běžně platí: maximálně tři roky a nejvýše dvakrát zopakovat.<br><br>
            <b>Kdy se poměr změní na dobu neurčitou:</b> Pokud zaměstnanec po skončení sjednané doby určité dál pokračuje v práci s vědomím zaměstnavatele, pracovní poměr se <b>ze zákona automaticky mění na dobu neurčitou</b>!
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.info("ℹ️ **Pozor na výjimky:** Některé situace mohou mít zvláštní režim, například zástup za mateřskou nebo rodičovskou dovolenou, sezónní práce nebo vážné provozní důvody.")

        st.divider()
        st.markdown(
            "<div class='box-yellow'>📅 <b>Kalkulačka kariérní jistoty</b></div>",
            unsafe_allow_html=True,
        )
        st.write(
            "Otestuj si pravidlo '3 a dost' v praxi. Tvůj zaměstnavatel ti dává neustále smlouvy jen na 1 rok. Kolik jich můžeš dostat?"
        )

        poradi_smlouvy = st.slider(
            "Počet smluv na dobu určitou v řadě u stejné firmy:",
            1,
            5,
            1,
            key="k4_2_7_smlouvy",
        )

        if poradi_smlouvy == 1:
            st.info(
                "📄 Podepsal jsi 1. smlouvu. Běžný postup při nástupu do nové práce."
            )
        elif poradi_smlouvy == 2:
            st.info("📄 Podepsal jsi 1. prodloužení. Vše je v pořádku.")
        elif poradi_smlouvy == 3:
            st.warning(
                "⚠️ **Poslední povoleno!** Toto je tvá celkově třetí a ze zákona poslední smlouva na dobu určitou. Až vyprší, musí přijít smlouva na neurčito."
            )
        else:
            st.error(
                "🚨 **PORUŠENÍ ZÁKONA:** Čtvrtá smlouva na dobu určitou v řadě je (až na specifické sezónní výjimky) nezákonná! Máš právo písemně oznámit zaměstnavateli, že trváš na zaměstnávání a tvůj poměr se tím mění na dobu neurčitou."
            )

        if st.button("Uložit test pravidla '3 a dost' 💾", key="btn_k4_2_7"):
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"](
                    "Kapitola 4",
                    "Podkapitola 2.7 - Pravidlo 3 a dost",
                    f"Počet smluv: {poradi_smlouvy}",
                )
            st.success("Výsledek byl uložen!")

    elif selected_section_4 == "2.8 Švarcsystém a gig economy":
        st.markdown("### 2.8 Švarcsystém a gig economy")
        st.write(
            "**Švarcsystém** je situace, kdy člověk formálně pracuje jako OSVČ (na živnostenský list / IČO), ale fakticky funguje v pozici běžného zaměstnance. "
            "Zaměstnavatel se tím snaží ušetřit na povinných odvodech (cca 34 %) a zákonných povinnostech."
        )

        st.markdown("#### 🚨 Varovné znaky švarcsystému:")
        st.markdown("""
        * pracujete pravidelně a dlouhodobě výhradně pro jednoho zadavatele,
        * zadavatel vám přímo určuje pracovní dobu a místo,
        * používáte vybavení, nástroje a techniku zadavatele (firemní notebook, auto),
        * nemáte možnost práci organizovat samostatně nebo ji delegovat,
        * vystupujete jménem firmy vůči zákazníkům,
        * nesete podnikatelské riziko, ale nemáte skutečnou podnikatelskou svobodu.
        """)

        st.markdown(
            """
        <div class='box-red'>
            ⚠️ <b>Rizika Švarcsystému pro tebe:</b><br>
            Nemáš nárok na placenou dovolenou, odstupné, příplatky za víkendy, a pokud onemocníš, jsi zcela bez příjmu. Hrozí ti navíc doměření daní od finančního úřadu a pokuta až 100 000 Kč! (Firmě pak až 10 000 000 Kč).
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.divider()
        st.markdown(
            "<div class='box-yellow'>📋 <b>Diagnostika: Jsem oběť Švarcsystému?</b></div>",
            unsafe_allow_html=True,
        )
        st.write(
            "Zaškrtni všechny výroky, které platí pro tvou 'podnikatelskou' činnost (na IČO) u dané firmy:"
        )

        svarc1 = st.checkbox(
            "Pracuji pravidelně a výhradně pouze pro tuto jedinou firmu.",
            key="k4_2_8_s1",
        )
        svarc2 = st.checkbox(
            "Šéf mi nařizuje pracovní dobu (od 8 do 16) a musím se hlásit o pauzy.",
            key="k4_2_8_s2",
        )
        svarc3 = st.checkbox(
            "Pracuji na firemním notebooku a nosím firemní tričko s jejich logem.",
            key="k4_2_8_s3",
        )
        svarc4 = st.checkbox(
            "Nemám možnost práci delegovat na někoho jiného, musím ji vykonat osobně.",
            key="k4_2_8_s4",
        )

        skore_svarc = sum([svarc1, svarc2, svarc3, svarc4])

        if skore_svarc >= 3:
            st.error(
                "🚩 **Tohle je učebnicový Švarcsystém!** Splňuješ všechny znaky závislé práce podle § 2 Zákoníku práce (vztah nadřízenosti, osobní výkon, náklady zaměstnavatele). Pracuješ nelegálně na IČO."
            )
        elif skore_svarc > 0:
            st.warning(
                "⚠️ **Riziková zóna:** Tvá práce má znaky zaměstnání. Jako skutečný podnikatel na IČO bys měl mít svobodu v organizaci času a nést vlastní podnikatelské riziko."
            )
        else:
            st.success(
                "✅ **Zdravé podnikání:** Pokud nevykazuješ tyto znaky, funguješ jako skutečný freelancer (např. IT specialista či grafik pracující na zakázkách pro více klientů)."
            )

        if st.button("Uložit diagnostiku Švarcsystému 💾", key="btn_k4_2_8"):
            svarc_data = f"Skóre Švarcsystému: {skore_svarc}/4 znaky"
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"](
                    "Kapitola 4",
                    "Podkapitola 2.8 - Diagnostika Švarcsystému",
                    svarc_data,
                )
            st.success("Diagnostika byla uložena!")

        st.divider()
        st.markdown("#### 🚴 Gig economy (Platformová ekonomika)")
        st.write(
            "Platformová práce, například rozvoz jídla (Foodora, Wolt), jízdy přes aplikace (Bolt, Uber) nebo mikropráce přes portály, může přinést flexibilitu. "
            "Zároveň ale často znamená menší jistotu příjmu, méně benefitů a plnou odpovědnost za vlastní pojištění, daně a opotřebení techniky."
        )

        col_gig1, col_gig2 = st.columns(2)
        with col_gig1:
            st.success(
                "🟢 **Výhody Gig Economy:**\n"
                "* Okamžitý nástup a nízká bariéra vstupu.\n"
                "* Extrémní flexibilita (aplikaci zapnete jen když chcete vydělávat).\n"
                "* Možnost kombinovat s jinou prací nebo studiem."
            )
        with col_gig2:
            st.error(
                "🔴 **Temná strana (Rizika):**\n"
                "* Odměna se mění podle toho, jak algoritmus sníží/zvýší sazby.\n"
                "* Falešná svoboda: aplikace vás penalizuje za odmítání zakázek.\n"
                "* Z opotřebení vlastního auta/kola nebo telefonu vám nikdo nic nezaplatí."
            )

    elif selected_section_4 == "2.9 Red flags v inzerátech a smlouvách":
        st.markdown(
            "### 2.9 Red flags v inzerátech a smlouvách"
        )
        st.write(
            "Místo memorování paragrafů je užitečné umět včas rozpoznat varovné signály (*Red flags*) v inzerátech, na pohovorech i ve smlouvách:"
        )

        st.markdown("""
        | Red flag (Co firma napíše / řekne) | Co to může v praxi znamenat | Na co se zeptat u pohovoru |
        | :--- | :--- | :--- |
        | 🚩 **„Jsme jako rodina.“** | Tlak na loajalitu a práci nad rámec smlouvy (neplacené přesčasy). | *Jak u vás řešíte přesčasy, víkendy a hranice práce?* |
        | 🚩 **„Dynamické prostředí.“** | Chaos, absence procesů, zadávání úkolů na poslední chvíli. | *Jak přesně vypadá běžný pracovní den na této pozici?* |
        | 🚩 **„Mzda podle výkonu / bez stropu.“** | Nejistý příjem, minimální základ a nereálné provize. | *Jaká je garantovaná fixní složka mzdy a jaká jsou kritéria bonusů?* |
        | 🚩 **„Práce na IČO, ale jako full-time.“** | Riziko nelegálního Švarcsystému a ztráta ochrany. | *Budu mít skutečně vlastní organizaci práce a další klienty?* |
        | 🚩 **Nejasná náplň práce („dle potřeb“)** | Riziko přetěžování a úkolování nesouvisející prací. | *Jaké budou moje hlavní konkrétní odpovědnosti a kompetence?* |
        | 🚩 **Odmítání písemné dohody („domluvíme se“)** | Právní nejistota a nevymahatelnost slibů. | *Dostanu písemný návrh smlouvy a mzdového výměru před nástupem?* |
        """)

        st.markdown(
            "#### 📝 Red Flags přímo v pracovních smlouvách a dohodách"
        )
        st.markdown("""
        * ❌ **Závazek mlčenlivosti o mzdě pod pokutou:** V ČR zákoník práce takovou smluvní pokutu neumožňuje. Zaměstnanci se o svých mzdách ze zákona bavit mohou (řeší směrnici EU o transparentnosti odměňování).
        * ❌ **Konkurenční doložka u běžných pozic:** Zákaz pracovat v oboru po odchodu z firmy. (Je platná POUZE tehdy, pokud vám za ni firma po dobu jejího trvání platí minimálně 50 % průměrného výdělku měsíčně!).
        * ❌ **Srážky ze mzdy bez dohody:** Smlouva obsahuje pasáž, že firma může strhávat peníze za 'špatný výkon' nebo rozbitý hrnek v kuchyňce automaticky.
        * ❌ **Podpis bianko směnky:** Absolutní extrém u některých 'finančně poradenských' firem = okamžitě odejděte!
        """)

        st.divider()
        st.markdown(
            "<div class='box-yellow'>🧪 <b>Simulátor pohovoru: Jak se bránit manipulaci</b></div>",
            unsafe_allow_html=True,
        )

        with st.form("red_flags_form"):
            st.write(
                "Sedíš na pohovoru. Personalista ti s úsměvem položí smlouvu na stůl a řekne:"
            )
            st.markdown(
                "*„Tak tady to máme. Je to standardní smlouva, všichni u nás ji mají stejnou. Tady do kolonky druh práce jsme raději dali 'Pracovník provozu', abychom to nekomplikovali, a mzdu si dohodneme pak ústně, víte, že my na papíry moc nehrajeme. Kde vám to mám podepsat?“*"
            )

            odp = st.radio(
                "Tvoje reakce:",
                [
                    (
                        "A) Super, děkuji za důvěru! (Podepíšu to hned, ať dělám dobrý dojem)."
                    ),
                    (
                        "B) 'Pracovník provozu' je moc široký pojem. Rád/a bych to změnil/a na 'Asistent prodeje'. A mzdu musíme mít před nástupem určenou minimálně písemným mzdovým výměrem."
                    ),
                    (
                        "C) Řeknu, ať do smlouvy napíšou mzdu 150 000 Kč, jinak odcházím."
                    ),
                ],
                key="k4_2_9_odp",
            )

            if st.form_submit_button("Vyhodnotit a uložit reakci 💾"):
                if odp.startswith("B"):
                    st.success(
                        "✅ **Skvělá reakce dospělého člověka!** Chráníš se před tím, abys dělal děvečku pro všechno, a trváš na transparentnosti. Na ústní dohody se v pracovním právu nehraje."
                    )
                elif odp.startswith("A"):
                    st.error(
                        "❌ **Prohrál jsi hru podle pravidel.** Právě jsi podepsal souhlas s tím, že tě firma může úkolovat čímkoliv. A pokud ti na konci měsíce dají minimální mzdu, nemáš v ruce jediný důkaz, že slíbili víc."
                    )
                elif odp.startswith("C"):
                    st.warning(
                        "⚠️ **Příliš arogantní.** Být asertivní neznamená být neslušný nebo klást absurdní ultimáta. Cílem je narovnat podmínky podle zákona."
                    )

                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"](
                        "Kapitola 4",
                        "Podkapitola 2.9 - Reakce na Red Flag",
                        odp[:30],
                    )

    # =========================================================================
    # SEKCE 3: HODNOTA MÉ PRÁCE: ODMĚŇOVÁNÍ A PENÍZE
    # =========================================================================
    elif (
        selected_section_4
        == "3.1 Hrubá mzda, čistá mzda a superhrubé uvažování"
    ):
        st.markdown("## 3. Hodnota mé práce: odměňování a peníze")
        st.markdown(
            "### 3.1 Hrubá mzda, čistá mzda a superhrubé uvažování"
        )
        st.markdown(
            """
        <div class='box-blue'>
            💵 <b>Základní otázka:</b> Kolik za práci skutečně dostanu — a kolik moje práce stojí zaměstnavatele?
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.write(
            "Na pracovní nabídce často vidíme **hrubou mzdu**. Na účet ale přijde **čistá mzda**. "
            "Zaměstnavatele přitom práce stojí ještě více, protože kromě mzdy řeší odvody, vybavení, prostor, software, školení, administrativu a řízení."
        )

        st.markdown("""
        | Mzdový pojem | Význam |
        | :--- | :--- |
        | **Hrubá mzda** | Částka před odvody a daní sjednaná v pracovní smlouvě. |
        | **Čistá mzda** | Částka, která reálně přijde zaměstnanci na bankovní účet. |
        | **Odvody zaměstnance** | Část sociálního (7,1 %) a zdravotního (4,5 %) pojištění placená zaměstnancem. |
        | **Odvody zaměstnavatele** | Část sociálního (24,8 %) a zdravotního (9 %) pojištění placená zaměstnavatelem navíc. |
        | **Celkové náklady zaměstnavatele** | Hrubá mzda + odvody firmy (33,8 %) + další provozní náklady spojené s pracovním místem. |
        """)

        st.markdown(
            """
        <div class='box-gray'>
            🤔 <b>Superhrubé uvažování v praxi:</b><br>
            Pojem <i>superhrubá mzda</i> byl v ČR sice v roce 2021 zrušen a daň se počítá rovnou z hrubé mzdy, přesto firmy stále uplatňují <b>superhrubé uvažování</b>. Když vám firma nabídne 40 000 Kč hrubého, její skutečný náklad je téměř 54 000 Kč kvůli povinným odvodům.
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown("#### 📊 Tři úrovně financí na trhu práce:")

        col_m1, col_m2, col_m3 = st.columns(3)
        with col_m1:
            st.markdown("##### 1️⃣ Čistá mzda")
            st.info(
                "Peníze, které vám reálně přijdou na bankovní účet po odečtení odvodů a daně z příjmu."
            )
        with col_m2:
            st.markdown("##### 2️⃣ Hrubá mzda")
            st.warning(
                "Částka ve vaší smlouvě, o které se vyjednává na pohovoru a počítají se z ní daně a odvody."
            )
        with col_m3:
            st.markdown("##### 3️⃣ Celkové náklady")
            st.error(
                "Skutečná cena vaší práce pro firmu (hrubá mzda + dalších 33,8 % povinných odvodů státu)."
            )

    elif selected_section_4 == "3.2 Nominální a reálná mzda":
        st.markdown("### 3.2 Nominální a reálná mzda")
        st.write(
            "Pokud vám šéf přidá 5 % ke mzdě, jste na tom lépe? **Ne vždy!** "
            "Záleží totiž na tom, jak rychle v zemi rostou ceny zboží a služeb (tzv. inflace)."
        )

        st.markdown("""
        * 💸 **Nominální mzda:** Částka vyjádřená v korunách na výplatní pásce.
        * 🛒 **Reálná mzda:** Říká, **co si za tuto částku skutečně koupíte** (vyjadřuje vaši kupní sílu).
        """)

        st.info(
            "💡 **Příklad:** Pokud mzda vzroste o 5 %, ale ceny v obchodech vzrostou o 10 %, člověk má sice vyšší nominální mzdu, ale nižší reálnou kupní sílu (zchudnul o 5 %)."
        )

        st.markdown(
            """
        <div class='box-green'>
            🧮 <b>Jednoduchý princip:</b><br>
            • Když ceny (inflace) rostou rychleji než mzda, <b>reálná mzda klesá</b>.<br>
            • Když mzda roste rychleji než ceny, <b>reálná mzda roste</b>.
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.divider()
        st.markdown(
            "<div class='box-yellow'>📉 <b>Simulátor: Skutečně jsi zbohatl? (Kupní síla)</b></div>",
            unsafe_allow_html=True,
        )
        st.write(
            "Zadej svou výplatu a změň inflaci, ať vidíš, jestli si toho koupíš víc nebo míň:"
        )

        col_inf1, col_inf2 = st.columns(2)
        with col_inf1:
            puvodni_mzda = 30000
            st.metric("Původní mzda (Loni)", f"{puvodni_mzda} Kč")
            zvyseni_mzdy = st.slider(
                "Šéf ti přidal ke mzdě (%):", 0, 20, 5, key="k4_3_2_zvyseni"
            )
            inflace = st.slider(
                "Inflace (zdražení v obchodech %):",
                0,
                20,
                8,
                key="k4_3_2_inflace",
            )

        with col_inf2:
            nova_mzda = int(puvodni_mzda * (1 + (zvyseni_mzdy / 100)))
            st.metric(
                "Nová mzda (Letos)", f"{nova_mzda} Kč", delta=f"+{zvyseni_mzdy}%"
            )

            rust_realne_mzdy = zvyseni_mzdy - inflace
            if rust_realne_mzdy < 0:
                st.error(
                    f"🚨 **Chudneš!** Tvá reálná mzda klesla o"
                    f" {-rust_realne_mzdy} %. Sice máš v peněžence víc korun,"
                    " ale věci v obchodě zdražily mnohem víc."
                )
            elif rust_realne_mzdy == 0:
                st.warning(
                    "⚖️ **Jsi na nule.** Tvá mzda vzrostla přesně stejně jako"
                    " ceny zboží. Můžeš si dovolit úplně to samé co loni."
                )
            else:
                st.success(
                    f"📈 **Bohatneš!** Tvá reálná mzda vzrostla o"
                    f" {rust_realne_mzdy} %. Mzda překonala zdražování a ty si"
                    " můžeš dovolit koupit více věcí."
                )

        if st.button("Uložit výpočet kupní síly 💾", key="btn_k4_3_2"):
            kupni_data = (
                f"Zvýšení: {zvyseni_mzdy}% | Inflace: {inflace}% | Změna reálné"
                f" mzdy: {rust_realne_mzdy}%"
            )
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"](
                    "Kapitola 4",
                    "Podkapitola 3.2 - Kupní síla mzdy",
                    kupni_data,
                )
            st.success("Výpočet byl uložen!")

    elif selected_section_4 == "3.3 Výplatní páska a její náležitosti":
        st.markdown("### 3.3 Výplatní páska")
        st.write(
            "Výplatní páska je **kontrolní dokument**. Ukazuje, jak se z hrubé mzdy stává čistá mzda, "
            "z čeho se mzda skládá, co bylo přičteno, co bylo sraženo a jak vznikla částka, která přijde na účet."
        )

        st.markdown("#### 🧾 Na výplatní pásce se typicky objevuje:")
        st.markdown("""
        * **hrubá mzda** a základní mzda,
        * **odpracované hodiny** a časový fond,
        * **příplatky** (přesčasy, víkendy, noční směny),
        * **náhrady mzdy** (placená dovolená, svátky),
        * **sociální a zdravotní pojištění** (srážky zaměstnance i odvody firmy),
        * **daň z příjmů** a uplatněné **slevy na dani**,
        * **ostatní srážky** (stravenky, penzijko),
        * **čistá mzda k výplatě**.
        """)

        st.divider()
        st.markdown("#### 📊 Modelová výplatní páska (Rozpad položek):")
        st.markdown("""
        | Položka výplatní pásky | Částka | Vysvětlení |
        | :--- | :--- | :--- |
        | **Hrubá mzda (základní)** | 32 000 Kč | Mzda sjednaná před odvody a daní. |
        | **Příplatek za práci o víkendu** | 1 200 Kč | Příklad mzdové složky navíc. |
        | **Hrubý příjem celkem** | **33 200 Kč** | **Základ pro výpočet odvodů a daně.** |
        | **Sociální pojištění zaměstnance (7,1 %)** | −2 357 Kč | Srážka ze mzdy zaměstnance na ČSSZ. |
        | **Zdravotní pojištění zaměstnance (4,5 %)** | −1 494 Kč | Srážka ze mzdy zaměstnance zdravotní pojišťovně. |
        | **Záloha na daň před slevami (15 %)** | −4 980 Kč | Daň vypočtená ze základu daně. |
        | **Sleva na poplatníka (prohlášení)** | +2 570 Kč | Měsíční sleva snižující daň. |
        | **Záloha na daň po slevě** | −2 410 Kč | Daň po uplatnění slevy (4 980 − 2 570). |
        | **ČISTÁ MZDA K VÝPLATĚ** | **26 939 Kč** | **Částka k výplatě na bankovní účet.** |
        """)

        st.caption("📌 *Poznámka: Jde o zjednodušený výukový příklad. Skutečné sazby a podmínky se mohou měnit podle platné legislativy.*")

        st.divider()
        st.markdown(
            "<div class='box-yellow'>🧪 <b>Aktivita: Výplatní páska s chybami</b></div>",
            unsafe_allow_html=True,
        )
        st.write(
            "Jako brigádník / zaměstnanec jsi dostal tuto výplatní pásku za minulý měsíc. Víš jistě, že jsi odpracoval celý měsíc (168 h) a navíc jeden den o víkendu (8 h přesčas). "
            "Najdi v tomto reálně vypadajícím výpisu **3 zásadní chyby**:"
        )

        st.markdown(
            """
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
        """,
            unsafe_allow_html=True,
        )

        with st.form("chyby_paska"):
            st.write(
                "Kde tě zaměstnavatel (ať už omylem, nebo úmyslně) připravil o peníze?"
            )
            chyb1 = st.checkbox(
                "Chybí povinný příplatek za práci o víkendu (i když je uvedeno 8 odpracovaných hodin).",
                key="k4_3_3_c1",
            )
            chyb2 = st.checkbox(
                "Záloha na daň je špatně vypočítaná (nemá být 15 %).",
                key="k4_3_3_c2",
            )
            chyb3 = st.checkbox(
                "Není uplatněna sleva na poplatníka (firma zřejmě nepředložila 'Růžové prohlášení' k podpisu).",
                key="k4_3_3_c3",
            )
            chyb4 = st.checkbox(
                "Jednostranná srážka 'Pokuta-sklad' je nelegální.",
                key="k4_3_3_c4",
            )
            chyb5 = st.checkbox(
                "Zůstatek dovolené je zapsán v desetinných číslech, což zákoník práce neumožňuje.",
                key="k4_3_3_c5",
            )

            if st.form_submit_button("Odhalit a uložit chyby 💾"):
                if chyb1 and chyb3 and chyb4 and not chyb2 and not chyb5:
                    st.success(
                        "✅ **Výborně! Skvělé postřeh!**\n\n1. **Víkend"
                        " zadarmo:** Máš tam 8h o víkendu, ale 0 Kč příplatek."
                        " Firmy 'zapomínají' platit přesčasy a víkendy velmi"
                        " často.\n2. **Ztráta tisíců na dani:** Máš"
                        " neuplatněnou slevu na poplatníka. Buď jsi nepodepsal"
                        " tzv. růžový papír (Prohlášení k dani), nebo to mzdová"
                        " účetní zapomněla zadat.\n3. **Nelegální srážka:**"
                        " Zaměstnavatel ti NESMÍ dát 'pokutu' srážkou ze mzdy"
                        " bez tvého písemného souhlasu, i kdybys ve skladu něco"
                        " rozbil."
                    )
                else:
                    st.error(
                        "Něco ti uniklo. Záloha 15 % je správně a dovolená se v"
                        " půldnech evidovat může. Chybí ale peníze za víkend,"
                        " sleva na dani a srážka jako 'pokuta' porušuje zákoník"
                        " práce!"
                    )

                paska_data = (
                    f"Chyby označené: 1:{chyb1}, 2:{chyb2}, 3:{chyb3},"
                    f" 4:{chyb4}, 5:{chyb5}"
                )
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"](
                        "Kapitola 4",
                        "Podkapitola 3.3 - Chyby na pásce",
                        paska_data,
                    )

    elif selected_section_4 == "3.4 Výpočet čisté mzdy krok za krokem":
        st.markdown("### 3.4 Výpočet čisté mzdy krok za krokem")
        st.write(
            "Čistá mzda nevzniká tak, že se z hrubé mzdy „něco náhodně odečte“. Výpočet má přesnou logiku:"
        )

        st.markdown("""
        1. **Určí se hrubá mzda** — základní mzda plus příplatky, odměny nebo náhrady.
        2. **Odečte se sociální pojištění zaměstnance** (7,1 %).
        3. **Odečte se zdravotní pojištění zaměstnance** (4,5 %).
        4. **Vypočítá se záloha na daň z příjmů** (15 % ze základu daně).
        5. **Uplatní se měsíční slevy na dani**, například základní sleva na poplatníka (2 570 Kč/měsíc).
        6. **Zohlední se další srážky nebo zvýhodnění** (např. daňový bonus na děti).
        7. **Výsledkem je čistá mzda**, tedy částka vyplacená zaměstnanci na bankovní účet.
        """)

        st.markdown(
            """
        <div class='box-blue'>
            🧮 <b>Zjednodušený vzorec výplaty:</b><br>
            Čistá mzda = Hrubá mzda − Sociální pojištění zaměstnance − Zdravotní pojištění zaměstnance − Daň po slevách ± další položky
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown("#### 🧾 Modelový výpočet čisté mzdy krok za krokem:")
        st.markdown(
            """
        | Krok | Položka | Výpočet | Částka |
        | :--- | :--- | :--- | :--- |
        | 1. | **Hrubý příjem (základ pro daně a odvody)** | Základ (32 000 Kč) + Příplatky (1 200 Kč) | **33 200 Kč** |
        | 2. | **Sociální pojištění zaměstnance (7,1 %)** | 33 200 × 7,1 % | **−2 357 Kč** |
        | 3. | **Zdravotní pojištění zaměstnance (4,5 %)**| 33 200 × 4,5 % | **−1 494 Kč** |
        | 4. | **Daň před slevami (15 %)** | 33 200 × 15 % | 4 980 Kč |
        | 5. | **Sleva na poplatníka** | Měsíční daňová sleva (prohlášení k dani) | **+2 570 Kč** |
        | 6. | **Reálná daň po slevě** | 4 980 − 2 570 | **−2 410 Kč** |
        | 7. | **ČISTÁ MZDA K VÝPLATĚ** | 33 200 − 2 357 − 1 494 − 2 410 | **26 939 Kč** |
        """,
            unsafe_allow_html=True,
        )

        st.caption(
            "📌 *Poznámka: Výpočet je zjednodušený pro výukové účely (zaokrouhlování na celé koruny).*"
        )

    elif (
        selected_section_4
        == "3.5 Sazby pojištění, daně a náklady zaměstnavatele"
    ):
        st.markdown(
            "### 3.5 Sazby pojištění, daně a celkové náklady zaměstnavatele"
        )
        st.write(
            "**Základní princip:** Zaměstnanec ze své mzdy platí sociální pojištění, zdravotní pojištění a daň z příjmů. "
            "Zaměstnavatel k tomu navíc platí **další sociální a zdravotní pojištění za zaměstnance jako svůj vlastní náklad**."
        )

        st.markdown("""
        | Položka | Platí zaměstnanec | Platí zaměstnavatel (navíc) | K čemu slouží |
        | :--- | :--- | :--- | :--- |
        | **Sociální pojištění** | **7,1 %** z hrubé mzdy | **24,8 %** z hrubé mzdy | Důchody (21,5 %), nemocenské pojištění (2,1 %) a politika zaměstnanosti (1,2 %). |
        | **Zdravotní pojištění** | **4,5 %** z hrubé mzdy | **9,0 %** z hrubé mzdy | Financování zdravotní péče, nemocnic a léků ze systému veřejného pojištění. |
        | **Daň z příjmů (DPFO)** | **15 %** ze základu daně | Neplatí se jako odvod firmy | Příjem veřejných rozpočtů (po výpočtu se snižuje o slevy na dani). |
        """)

        st.markdown("#### 🏢 Proč je práce dražší než hrubá mzda?")
        st.write(
            "Když má zaměstnanec hrubou mzdu 33 200 Kč, zaměstnavatel neplatí jen těchto 33 200 Kč. "
            "Navíc odvádí **33,8 % na sociálním a zdravotním pojištění**. Proto jsou celkové náklady zaměstnavatele podstatně vyšší:"
        )

        st.markdown("""
        | Položka nákladů | Výpočet | Částka |
        | :--- | :--- | :--- |
        | **Hrubá mzda zaměstnance** | — | 33 200 Kč |
        | **Sociální pojištění zaměstnavatele (24,8 %)** | 33 200 × 24,8 % | 8 234 Kč |
        | **Zdravotní pojištění zaměstnavatele (9,0 %)** | 33 200 × 9,0 % | 2 988 Kč |
        | **CELKOVÉ MZDOVÉ NÁKLADY ZAMĚSTNAVATELE** | 33 200 + 8 234 + 2 988 | **44 422 Kč** |
        """)

        st.markdown(
            """
        <div class='box-red'>
            💡 <b>Pointa pro finanční gramotnost:</b><br>
            Když přijdete za šéfem a řeknete si o přidání <b>1 000 Kč k hrubé mzdě</b>, musí šéf ve firemním rozpočtu najít <b>1 338 Kč</b>. Těch 338 Kč navíc spolkne stát. Proto firmy někdy raději nabízejí nefinanční benefity (např. mobil, auto, flexibilitu), které se daní a odvádějí jiným (levnějším) způsobem.
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.divider()
        st.markdown(
            "<div class='box-yellow'>🧮 <b>Interaktivní simulátor: Z firemní kasy až k tobě na účet</b></div>",
            unsafe_allow_html=True,
        )
        st.write(
            "Vžij se do role majitele firmy. Chceš zaměstnat nového člověka. Zadej hrubou mzdu, kterou mu nabídneš na pohovoru, a sleduj, jak se peníze rozdělí mezi něj a stát:"
        )

        vysnena_mzda = st.slider(
            "Nabízená hrubá mzda na smlouvě (Kč):",
            20000,
            100000,
            40000,
            step=1000,
            key="k4_3_5_mzda",
        )

        soc_zam = int(vysnena_mzda * 0.071)
        zdr_zam = int(vysnena_mzda * 0.045)
        dan_pred = int(vysnena_mzda * 0.15)
        dan_po = max(0, dan_pred - 2570)
        cista = vysnena_mzda - soc_zam - zdr_zam - dan_po

        soc_firma = int(vysnena_mzda * 0.248)
        zdr_firma = int(vysnena_mzda * 0.09)
        naklady_firmy = vysnena_mzda + soc_firma + zdr_firma

        stat_celkem = soc_zam + zdr_zam + dan_po + soc_firma + zdr_firma

        podil_zamestnanec = cista / naklady_firmy
        podil_stat = stat_celkem / naklady_firmy

        col_k1, col_k2, col_k3 = st.columns(3)
        with col_k1:
            st.metric(
                "1. Náklad firmy celkem",
                f"{naklady_firmy:,} Kč".replace(",", " "),
            )
            st.caption("Peníze, které reálně odejdou z účtu firmy.")
        with col_k2:
            st.metric(
                "2. Peníze pro stát", f"{stat_celkem:,} Kč".replace(",", " ")
            )
            st.caption("Daně a odvody od firmy i zaměstnance.")
        with col_k3:
            st.metric("3. Čistá mzda", f"{cista:,} Kč".replace(",", " "))
            st.caption("To, co přistane zaměstnanci na účtu.")

        st.write("📊 **Jak se firemní peníze (náklady) rozdělily procentuálně:**")
        st.progress(
            podil_zamestnanec,
            text=(
                f"Zaměstnanec dostane cca {int(podil_zamestnanec*100)} % z"
                " firemních nákladů (Zbytek bere stát)."
            ),
        )

        if st.button("Uložit simulaci nákladů firmy 💾", key="btn_k4_3_5"):
            sim_firma_data = (
                f"Hrubá: {vysnena_mzda} Kč | Náklad firmy: {naklady_firmy} Kč |"
                f" Stát: {stat_celkem} Kč | Čistá: {cista} Kč"
            )
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"](
                    "Kapitola 4",
                    "Podkapitola 3.5 - Náklady zaměstnavatele",
                    sim_firma_data,
                )
            st.success("Simulace byla uložena!")

    elif selected_section_4 == "3.6 Slevy na dani a odčitatelné položky":
        st.markdown(
            "### 3.6 Slevy na dani, daňové zvýhodnění a odčitatelné položky"
        )
        st.write(
            "V oblasti daní se často používají tři pojmy, které znějí podobně, ale fungují úplně jinak. "
            "Pokud chcete maximalizovat svou výplatu (nebo vratku daní z finančního úřadu), musíte znát rozdíl!"
        )

        st.markdown("#### ⚖️ Tři klíčové pojmy (Co je co?)")
        st.markdown(
            """
        | Pojem | Co přesně snižuje? | Kdy se obvykle uplatňuje |
        | :--- | :--- | :--- |
        | 💎 **Sleva na dani** | Snižuje **přímo vypočtenou daň**. Koruna slevy = koruna v kapse. | Často měsíčně (ve výplatě). |
        | 👨‍👩‍👧 **Daňové zvýhodnění** | Snižuje daň. Pokud vám daň už klesla na nulu, stát vám zbytek slevy **doplatí (Daňový bonus)**. | Měsíčně (uplatňuje jen 1 rodič). |
        | 📉 **Odčitatelná položka** | Nesnižuje daň, ale jen **základ, ze kterého se daň počítá**. Ušetří vám 15 % ze své hodnoty. | Typicky 1x ročně (v daňovém přiznání). |
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
        <div class='box-blue'>
            💡 <b>Rozdíl polopaticky:</b><br>
            • <b>Sleva 1 000 Kč</b> = Na dani zaplatíte o rovných 1 000 Kč méně. Peníze vám zůstávají v kapse.<br>
            • <b>Odčitatelná položka 1 000 Kč</b> = Sníží váš daňový základ. Reálně vám to ale na finální dani ušetří jen 15 % z oné tisícikoruny (tj. pouhých 150 Kč).
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.divider()
        st.markdown(
            "#### 💎 Přehled: Slevy na dani a Daňové zvýhodnění (pro rok 2026)"
        )
        st.write(
            "Abyste mohli slevy uplatňovat už z měsíční výplaty, musíte v práci podepsat tzv. **Prohlášení poplatníka k dani** (známý „růžový papír“)."
        )

        st.markdown("""
        | Položka | Výše v roce 2026 | Jak se uplatňuje | Praktická poznámka |
        | :--- | :--- | :--- | :--- |
        | **Sleva na poplatníka** | **30 840 Kč ročně** / 2 570 Kč měsíčně | Měsíčně v zaměstnání nebo ročně v přiznání | Základní sleva pro většinu poplatníků se zdanitelným příjmem. |
        | **Daňové zvýhodnění na 1. dítě** | **15 204 Kč ročně** / 1 267 Kč měsíčně | Měsíčně nebo ročně | Uplatnit ho může jen 1 osoba ve společně hospodařící domácnosti. |
        | **Daňové zvýhodnění na 2. dítě** | **22 320 Kč ročně** / 1 860 Kč měsíčně | Měsíčně nebo ročně | Pořadí dětí se posuzuje podle počtu vyživovaných dětí v domácnosti. |
        | **Daňové zvýhodnění na 3. a další dítě** | **27 840 Kč ročně** / 2 320 Kč měsíčně | Měsíčně nebo ročně | U dítěte se ZTP/P se částka daňového zvýhodnění zvyšuje na dvojnásobek. |
        | **Sleva na manžela/manželku** | **24 840 Kč ročně** | Zpravidla ročně | Jen při splnění podmínek (vlastní příjem do 68 000 Kč/rok a péče o dítě do 3 let). |
        | **Základní sleva na invaliditu** | **2 520 Kč ročně** / 210 Kč měsíčně | Měsíčně nebo ročně | Pro invaliditu I. nebo II. stupně. |
        | **Rozšířená sleva na invaliditu** | **5 040 Kč ročně** / 420 Kč měsíčně | Měsíčně nebo ročně | Pro invaliditu III. stupně. |
        | **Sleva pro držitele průkazu ZTP/P** | **16 140 Kč ročně** / 1 345 Kč měsíčně | Měsíčně nebo ročně | Nárok se dokládá průkazem ZTP/P. |
        """)

        st.warning(
            "⚠️ **Poznámka k roku 2026:** Částky slev a zvýhodnění je vhodné pravidelně kontrolovat. Některé dřívější slevy, například sleva na studenta nebo školkovné, už se neuplatňují."
        )

        st.divider()
        st.markdown(
            "#### 📉 Běžné Odčitatelné položky (Nezdanitelné části základu daně)"
        )
        st.write(
            "Tyto položky řešíte typicky až na jaře v **ročním zúčtování daně** (udělá to za vás účetní) nebo v **daňovém přiznání**. "
            "Stát vám díky nim vrátí část zaplacených daní za loňský rok na účet jako hezký přeplatek."
        )

        st.markdown("""
        * 🩸 **Dary a darování krve:** Darovali jste peníze na charitu, nebo krev? Za 1 bezpříspěvkový odběr krve si snížíte základ daně o 3 000 Kč (vratka na dani = **450 Kč** čistého za odběr). Odběr kostní dřeně = 20 000 Kč.
        * 🏠 **Úroky z hypotéky:** Ze základu daně si můžete odečíst zaplacené úroky z úvěru na bydlení. Maximální limit je **150 000 Kč ročně**. Pokud ho využijete naplno, stát vám na jaře vrátí **až 22 500 Kč**.
        * 🐖 **Spoření na stáří (Penzijko, Životní pojištění, DIP):** Od roku 2024 stát zavedl **jeden společný limit 48 000 Kč ročně** pro všechny produkty spoření na stáří dohromady (Doplňkové penzijní spoření, Životní pojištění a Dlouhodobý investiční produkt - DIP). Pokud limit naplníte, stát vám vrátí na dani **7 200 Kč**.
        """)

        st.markdown(
            """
        <div class='box-green'>
            🎁 <b>Firemní benefit snů: Příspěvek zaměstnavatele na stáří</b><br>
            Firma vám může na Penzijko, DIP nebo Životní pojištění přispívat ze svého <b>až 50 000 Kč ročně</b>. Proč je to pro obě strany tak výhodné?<br>
            Jsou to totiž absolutně <b>čisté nezdaněné peníze!</b> Z tohoto příspěvku zaměstnavatele se neodvádí žádná 15% daň, žádné zdravotní ani sociální pojištění. Pokud vám firma pošle na DIP 2 000 Kč, přistane vám tam přesně 2 000 Kč. Kdyby vám stejné peníze dali do hrubé mzdy jako bonus, zbylo by vám z nich na účtu sotva čtrnáct stovek.
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.divider()
        st.markdown(
            "<div class='box-yellow'>🧩 <b>Simulátor: Kouzlo daňového bonusu a slev</b></div>",
            unsafe_allow_html=True,
        )
        st.write(
            "Nastav hrubou mzdu a přidej životní situaci. Sleduj, co to udělá s daní. Můžeš mít dokonce **čistou mzdu vyšší než hrubou**?"
        )

        col_slev1, col_slev2 = st.columns(2)
        with col_slev1:
            hruba_slevy = st.slider(
                "Hrubá mzda:",
                20000,
                60000,
                30000,
                step=1000,
                key="k4_3_6_hruba",
            )
            deti = st.selectbox(
                "Počet vyživovaných dětí (pro rok 2026):",
                [0, 1, 2, 3],
                key="k4_3_6_deti",
            )

            dan_zaklad = int(hruba_slevy * 0.15)
            sleva_poplatnik = 2570

            sleva_deti = 0
            if deti == 1:
                sleva_deti = 1267
            elif deti == 2:
                sleva_deti = 1267 + 1860
            elif deti >= 3:
                sleva_deti = 1267 + 1860 + 2320

            dan_po_poplatnikovi = max(0, dan_zaklad - sleva_poplatnik)
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
            st.write(
                f"1. Vypočtená daň z hrubé (15 %): **{dan_zaklad} Kč**"
            )
            st.write(
                f"2. Mínus základní sleva na tebe: **- {sleva_poplatnik} Kč**"
            )
            st.write(f"3. Mínus slevy na děti: **- {sleva_deti} Kč**")
            st.divider()

            if bonus > 0:
                st.success(
                    f"🚀 **Vznikl ti Daňový Bonus: {bonus} Kč!**\nStát tě"
                    " nenechá platit žádnou daň, a ještě ti tuto částku přihodí"
                    " k výplatě navíc!"
                )
                st.metric(
                    "Tvoje finální čistá mzda:",
                    f"{cista_mzda_konecna:,} Kč".replace(",", " "),
                )
            else:
                st.info(
                    "Konečná daň z příjmů, kterou reálně zaplatíš:"
                    f" {realna_dan} Kč"
                )
                st.metric(
                    "Tvoje finální čistá mzda:",
                    f"{cista_mzda_konecna:,} Kč".replace(",", " "),
                )

            if cista_mzda_konecna > hruba_slevy:
                st.balloons()
                st.markdown(
                    "**WOW! Tvá čistá mzda je vyšší než hrubá!** To je možné"
                    " právě díky státnímu daňovému bonusu za děti."
                )

        if st.button("Uložit výpočet daňových slev 💾", key="btn_k4_3_6"):
            slevy_data = (
                f"Hrubá: {hruba_slevy} Kč | Dětí: {deti} | Bonus: {bonus} Kč |"
                f" Čistá mzda: {cista_mzda_konecna} Kč"
            )
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"](
                    "Kapitola 4",
                    "Podkapitola 3.6 - Daňový bonus a slevy",
                    slevy_data,
                )
            st.success("Výpočet byl uložen!")

    elif (
        selected_section_4
        == "3.7 Kam jdou odvody (sociální a zdravotní pojištění)"
    ):
        st.markdown("### 3.7 Kam jdou odvody? Solidarita v praxi")
        st.write(
            "Odvody, které vám strhnou z výplaty, nejsou jen 'peníze pryč, které"
            " už nikdy neuvidíte'. Financují systémy, které vás a vaši rodinu"
            " mají chránit v krizových životních situacích."
        )

        col_kam1, col_kam2 = st.columns(2)
        with col_kam1:
            st.markdown(
                """
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
            """,
                unsafe_allow_html=True,
            )

        with col_kam2:
            st.markdown(
                """
            <div style="background-color: #eff6ff; padding: 20px; border-radius: 8px; border: 1px solid #bfdbfe; height: 100%;">
                <h4 style="color: #1e3a8a; margin-top: 0;">🏛️ Sociální pojištění</h4>
                <p style="color: #1d4ed8; font-size: 0.95rem;">Jde do státního rozpočtu (ČSSZ) a rozděluje se na tři hlavní pilíře, které chrání při výpadku příjmů:</p>
                <ul style="color: #1e3a8a; font-size: 0.9rem;">
                    <li><b>Důchodové poj.:</b> Platí se z něj starobní, invalidní a pozůstalostní (sirotčí) důchody.</li>
                    <li><b>Nemocenské poj.:</b> Vyplácí tzv. nemocenskou (při dlouhé nemoci), mateřskou a ošetřovné.</li>
                    <li><b>Politika zaměstnanosti:</b> Hradí chod úřadů práce a podpory v nezaměstnanosti.</li>
                </ul>
            </div>
            """,
                unsafe_allow_html=True,
            )

    elif (
        selected_section_4 == "3.8 Celková odměna za práci a vyjednávání o mzdě"
    ):
        st.markdown(
            "### 3.8 Celková odměna za práci a vyjednávání o mzdě"
        )

        st.write(
            "Peníze nejsou jediná odměna. Při výběru práce je potřeba porovnat"
            " **celkový balíček** (tzv. Total Reward). Práce s nejvyšší hrubou"
            " mzdou totiž může být ve finále ta nejméně výhodná."
        )

        st.markdown("#### ⚖️ Co vše tvoří reálnou hodnotu práce?")
        st.markdown("""
        * 💵 **Finance:** Základní mzda, roční bonusy, příplatky za víkendy, třináctý plat.
        * 🕒 **Čas a flexibilita:** Možnost pracovat z domova (Home Office), pružná pracovní doba, 5. týden dovolené navíc, Sick days.
        * 🚗 **Náklady na dojíždění:** Čas strávený v zácpách a peníze za benzín/jízdenky (práce daleko od domova reálně snižuje vaši čistou mzdu).
        * 🍔 **Další benefity:** Stravenky, příspěvek na penzijní spoření (nedaní se!), Multisport karta, služební auto i k soukromým účelům.
        * 📈 **Růst a prostředí:** Firemní vzdělávání, zdravá firemní kultura a šéf, který vás neničí stresem.
        """)

        st.divider()
        st.markdown(
            "<div class='box-yellow'>⚖️ <b>Rozhodovací simulátor: Která"
            " nabídka je skutečně lepší?</b></div>",
            unsafe_allow_html=True,
        )
        st.write(
            "Dostal jsi dvě pracovní nabídky. Papírově vypadá jedna lépe. Ale"
            " co když započítáš náklady na dopravu a tvůj volný čas? (Počítáme,"
            " že tvůj volný čas má pro tebe hodnotu 150 Kč / hodina)."
        )

        col_nab1, col_nab2 = st.columns(2)
        with col_nab1:
            st.markdown("##### 🏢 Nabídka A: Korporát v centru")
            mzda_a = 40000
            dojizdeni_minuty_a = st.slider(
                "Čas strávený dojížděním denně tam i zpět (v minutách):",
                0,
                180,
                90,
                key="doj_a",
            )
            naklady_doprava_a = st.slider(
                "Měsíční náklady na dojíždění (palivo/jízdenky v Kč):",
                0,
                5000,
                3000,
                key="nak_a",
            )

            ztraceny_cas_a = (dojizdeni_minuty_a / 60) * 21 * 150
            realna_hodnota_a = mzda_a - naklady_doprava_a - ztraceny_cas_a

            st.write(f"Hrubá mzda: **{mzda_a} Kč**")
            st.info(
                f"Peníze vyhozené za dopravu: -{naklady_doprava_a} Kč\n\nHodnota"
                f" ztraceného času v MHD/autě: -{int(ztraceny_cas_a)} Kč"
            )
            st.metric(
                "Skutečná hodnota nabídky A:",
                f"{int(realna_hodnota_a)} Kč",
            )

        with col_nab2:
            st.markdown("##### 🏠 Nabídka B: Startup na Home Office")
            mzda_b = 35000
            st.write(
                "Firma ti dovolí pracovat 100% z domova. Nikam nedojíždíš."
            )

            realna_hodnota_b = mzda_b

            st.write(f"Hrubá mzda: **{mzda_b} Kč**")
            st.success(
                "Peníze vyhozené za dopravu: 0 Kč\n\nHodnota ztraceného času v"
                " MHD/autě: 0 Kč"
            )
            st.metric(
                "Skutečná hodnota nabídky B:",
                f"{int(realna_hodnota_b)} Kč",
            )

        if realna_hodnota_b > realna_hodnota_a:
            st.markdown(
                "🚨 **Výsledek:** Přestože je Nabídka B na papíře o 5 000 Kč"
                " chudší, **ve skutečnosti je pro tebe výhodnější!** Ušetříš"
                " peníze za benzín a hlavně získáš zpět desítky hodin svého"
                " života měsíčně."
            )
        else:
            st.markdown(
                "⚖️ **Výsledek:** I přes započítání nákladů na dojíždění se"
                " Nabídka A stále finančně vyplatí. Záleží ale i na tom, zda ti"
                " stres z dojíždění za ty peníze stojí."
            )

        if st.button("Uložit porovnání nabídek práce 💾", key="btn_k4_3_8"):
            nabidky_data = (
                f"Hodnota A: {int(realna_hodnota_a)} Kč | Hodnota B:"
                f" {int(realna_hodnota_b)} Kč"
            )
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"](
                    "Kapitola 4",
                    "Podkapitola 3.8 - Rozhodovací simulátor nabídek",
                    nabidky_data,
                )
            st.success("Porovnání bylo uloženo!")

        st.divider()
        st.markdown("#### 🗣️ Vyjednávání o mzdě")
        st.write(
            "Vyjednávání není hádka na tržnici. Je to **profesionální obchodní"
            " rozhovor o hodnotě tvé práce**. Většina firem počítá s tím, že o"
            " prvním návrhu mzdy se bude diskutovat."
        )

        prompt_plat = (
            "Hrajeme hru na vyjednávání o mzdě. Ty jsi tvrdý, ale racionální HR"
            " manažer firmy. Já jsem zaměstnanec, který pracuje na pozici"
            " Junior Marketing Specialista už rok a jde si za tebou říct o"
            " zvýšení hrubé mzdy o 15 %. Začni konverzaci tím, že se zeptáš,"
            " co potřebuji. Já vznesu požadavek. Ty nejprve odmítni a hledej"
            " důvody, proč mi přidat nemůžeš. Nenuť mě vyhrát hned. Čekej na mé"
            " argumenty. Pokud mé argumenty budou logické, podložené čísly nebo"
            " mi navrhneš kompromis v podobě nefinančních benefitů, můžeme se"
            " dohodnout. Po 6 výměnách zpráv hru ukonči a dej mi jako AI"
            " feedback, jak jsem si ve vyjednávání vedl."
        )

        st.markdown(
            f"""
        <div style="background-color: #f8f9fa; padding: 15px; border-left: 5px solid #8b5cf6; border-radius: 5px; font-family: monospace; font-size: 1.1em; color: #333; white-space: pre-wrap; word-wrap: break-word; line-height: 1.5;">
        {prompt_plat}
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.caption(
            "💡 Tip: Zkopíruj text z fialového boxu výše a zkus AI přesvědčit,"
            " že si peníze navíc zasloužíš!"
        )

    # =========================================================================
    # SEKCE 4: ŽIVOT V PRÁCI: KULTURA, WELLBEING A KARIÉRNÍ RŮST
    # =========================================================================
    elif selected_section_4 == "4.1 Firemní kultura a wellbeing":
        st.markdown("### 4.1 Firemní kultura a wellbeing")
        st.markdown(
            """
        <div class='box-blue'>
            🧘 <b>Základní otázka:</b> Jak poznat práci, ve které se dá dlouhodobě kariérně růst a neztratit přitom zdraví a nervy?
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.write(
            "**Firemní kultura** není to, co má firma napsané zlatým písmem na"
            " webu. Je to způsob, jakým se lidé ve firmě chovají, komunikují"
            " a rozhodují, když se nikdo nedívá."
        )

        col_kult1, col_kult2 = st.columns(2)
        with col_kult1:
            st.success(
                "🟢 **Znaky zdravé kultury:**\n"
                "* Chyby se berou jako příležitost k učení, ne jako důvod k"
                " trestu.\n"
                "* Lidé se nebojí na cokoliv zeptat.\n"
                "* Firma drží své sliby.\n"
                "* Přesčasy jsou výjimečné, ne každodenní pravidlo."
            )
        with col_kult2:
            st.error(
                "🔴 **Toxická kultura (Red flags):**\n"
                "* *„Kdo se ptá, ten na to asi nemá.“*\n"
                "* *„U nás se na hodinky nekouká, prostě makáme, dokud není"
                " hotovo.“*\n"
                "* Vedení mluví o zákaznících a podřízených s despektem a"
                " výsměchem."
            )

        st.divider()
        st.markdown(
            "#### 🔋 Wellbeing a prevence vyhoření"
        )
        st.write(
            "**Wellbeing (životní a pracovní pohoda)** opravdu neznamená, že"
            " vám firma dá do kuchyňky banány zdarma nebo vám zaplatí lekci"
            " jógy. Skutečný wellbeing znamená **podmínky, ve kterých člověk"
            " může dlouhodobě pracovat bez poškozování fyzického a duševního"
            " zdraví**."
        )

        st.markdown(
            "<div class='box-yellow'>📋 <b>Osobní test: Hrozí ti vyhoření?"
            " (Burnout Check)</b></div>",
            unsafe_allow_html=True,
        )
        st.write(
            "Syndrom vyhoření nevzniká ze dne na den. Je to plíživý proces."
            " Zaškrtni tvrzení, která momentálně zažíváš ve škole, na brigádě"
            " nebo v práci:"
        )

        b1 = st.checkbox(
            "Mám neustále pocit, že nestíhám, a žiju v dlouhodobém stresu.",
            key="k4_4_1_b1",
        )
        b2 = st.checkbox(
            "Často vůbec nevím, co se ode mě přesně očekává (nejasná zadání).",
            key="k4_4_1_b2",
        )
        b3 = st.checkbox(
            "Nemám kontrolu nad svým časem (všechno řídí někdo jiný).",
            key="k4_4_1_b3",
        )
        b4 = st.checkbox(
            "Neumím nebo se bojím říct 'NE', když mě někdo požádá o úkol navíc.",
            key="k4_4_1_b4",
        )
        b5 = st.checkbox(
            "Moje práce/studium mi nedává smysl a dělám to jen jako robot.",
            key="k4_4_1_b5",
        )
        b6 = st.checkbox(
            "Nemám čas na odpočinek, koníčky a spánek.", key="k4_4_1_b6"
        )

        skore_vyhoreni = sum([b1, b2, b3, b4, b5, b6])
        st.progress(skore_vyhoreni / 6)

        if skore_vyhoreni >= 4:
            st.error(
                "🚨 **KRITICKÉ RIZIKO VYHOŘENÍ!** Tvůj systém hlásí přetížení."
                " Chybí ti 'ochranné faktory'. Musíš si okamžitě nastavit"
                " hranice, naučit se říkat ne a najít si čas na digitální detox"
                " a spánek."
            )
        elif skore_vyhoreni >= 2:
            st.warning(
                "⚠️ **Zvýšené riziko:** Začínáš balancovat na hraně. Zaměř se"
                " na to, abys měl jasně vymezený čas na práci a čas, kdy"
                " úplně 'vypneš' hlavu."
            )
        elif skore_vyhoreni > 0:
            st.info(
                "ℹ️ **Běžná zátěž:** Občasný stres je normální, ale hlídej si,"
                " aby se z těchto bodů nestala každodenní rutina."
            )
        else:
            st.success(
                "✅ **Skvělá práce s hranicemi!** Tvé mentální zdraví a"
                " wellbeing jsou aktuálně v rovnováze. Máš nastavené zdravé"
                " priority."
            )

        if st.button("Uložit výsledek testu vyhoření 💾", key="btn_k4_4_1"):
            burnout_data = f"Riziko vyhoření: {skore_vyhoreni}/6 příznaků"
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"](
                    "Kapitola 4",
                    "Podkapitola 4.1 - Test vyhoření",
                    burnout_data,
                )
            st.success("Výsledek testu byl uložen!")

    elif selected_section_4 == "4.2 Právo na odpojení a podnikavost v zaměstnání":
        st.markdown(
            "### 4.2 Právo na odpojení a Intrapreneurship"
        )

        st.markdown("#### 📵 Právo na odpojení (Right to disconnect)")
        st.write(
            "V digitální době je hranice mezi prací a volnem extrémně křehká."
            " Právo na odpojení znamená, že **nemáte povinnost být neustále"
            " dostupní (číst e-maily a zvedat telefony) ve svém osobním"
            " volnu**, jen proto, že máte v kapse smartphone."
        )

        st.markdown(
            "<div class='box-yellow'>⚖️ <b>Rozhodovací scénář: Páteční zpráva"
            " od šéfa</b></div>",
            unsafe_allow_html=True,
        )
        st.write(
            "Je pátek, 20:30. Sedíš s přáteli v kině. Najednou ti pípne WhatsApp"
            " od šéfa: *„Ahoj, prosím tě, můžeš mi do toho reportu rychle dopsat"
            " čísla za tento týden? Potřebuju se na to podívat. Díky!“* (Nemáš"
            " sjednanou placenou pohotovost)."
        )

        reakce_boss = st.radio(
            "Jak zareaguješ?",
            [
                (
                    "A) Omluvím se přátelům, vyjdu z kina, otevřu na telefonu"
                    " tabulku a rychle to udělám. Chci ukázat, že jsem pracovitý."
                ),
                (
                    "B) Zprávu si přečtu, naštve mě to, ale odepíšu: 'Jsem v"
                    " kině, udělám to zítra ráno, o víkendu.'"
                ),
                (
                    "C) Zprávu ignoruji nebo odepíšu: 'Ahoj, teď mám volno,"
                    " podívám se na to hned v pondělí ráno, jak přijdu do"
                    " práce.'"
                ),
            ],
            key="k4_4_2_boss",
        )

        if reakce_boss.startswith("A"):
            st.error(
                "❌ **Špatně (Cesta do pekla):** Právě jsi šéfovi ukázal, že"
                " tvůj osobní čas nemá hodnotu a jsi mu k dispozici 24/7. Příště"
                " ti napíše v sobotu o půlnoci."
            )
        elif reakce_boss.startswith("B"):
            st.warning(
                "⚠️ **Napůl špatně:** Sice jsi práci odložil, ale stejně jsi"
                " obětoval svůj víkend. Navíc už sis zkazil náladu v kině"
                " přemýšlením nad prací."
            )
        elif reakce_boss.startswith("C"):
            st.success(
                "✅ **Správně! (Zdravé hranice):** Pokud se nejedná o hořící"
                " budovu nebo nemáš ve smlouvě placenou pohotovost, tvůj volný"
                " čas je svatý. Dobrý šéf to bude respektovat. Špatný šéf to"
                " bude zkoušet znovu – a pak je načase změnit firmu."
            )

        if st.button("Uložit reakci na zprávu od šéfa 💾", key="btn_k4_4_2"):
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"](
                    "Kapitola 4",
                    "Podkapitola 4.2 - Právo na odpojení",
                    reakce_boss[:30],
                )
            st.success("Reakce byla uložena!")

    elif selected_section_4 == "4.3 Upskilling a reskilling":
        st.markdown(
            "### 4.3 Upskilling a reskilling: Jak nezestárnout na trhu práce"
        )
        st.write(
            "V době automatizace a umělé inteligence už neplatí, že vystudujete"
            " jednu školu a s těmito znalostmi vystačíte do důchodu. Vaše tržní"
            " hodnota a bezpečnost závisí na vaší ochotě a schopnosti se učit."
        )

        profese = st.selectbox(
            "Vyber profesi pro analýzu dovedností:",
            [
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
                "Stavař / Řemeslník",
            ],
            key="k4_4_3_profese",
        )

        if profese != "Vyber profesi...":
            if "vykresli_otazku_fn" in st.session_state:
                st.session_state["vykresli_otazku_fn"](
                    "4.4.1",
                    f"Generátor dovedností pro profesi ({profese}): Napiš 2"
                    " konkrétní dovednosti, které se musíte naučit, abyste"
                    " zvýšili svou hodnotu v příštích 5 letech.",
                    "4",
                    st.session_state.get("ulozene_odpovedi", {}),
                )

    # =========================================================================
    # SEKCE 5: KDYŽ SE CESTY ROZEJDOU: KONEC PRÁCE A KRIZOVÉ SITUACE
    # =========================================================================
    elif selected_section_4 == "5.1 Jak dát a dostat výpověď profesionálně":
        st.markdown(
            "### 5.1 Jak ukončit pracovní poměr (Možnosti a lhůty)"
        )
        st.markdown(
            """
        <div class='box-blue'>
            🧯 <b>Základní pravidlo:</b> Pojem „výpověď dohodou“ neexistuje! Jsou to dvě úplně odlišné věci, které mají zcela jiné dopady na vaše peníze a čas. Všechna ukončení musí být vždy <b>písemná</b>.
        </div>
        """,
            unsafe_allow_html=True,
        )

        mesic_podani = st.selectbox(
            "Ve kterém měsíci předáš šéfovi papír s výpovědí?",
            [
                "Leden",
                "Únor",
                "Březen",
                "Duben",
                "Květen",
                "Červen",
                "Červenec",
                "Srpen",
                "Září",
                "Říjen",
                "Listopad",
                "Prosinec",
            ],
            key="k4_5_1_mesic",
        )

        mesice_kruh = [
            "Leden",
            "Únor",
            "Březen",
            "Duben",
            "Květen",
            "Červen",
            "Červenec",
            "Srpen",
            "Září",
            "Říjen",
            "Listopad",
            "Prosinec",
        ]
        idx = mesice_kruh.index(mesic_podani)

        start_idx = (idx + 1) % 12
        konec_idx = (idx + 2) % 12

        rok_navic_start = " (příštího roku)" if start_idx < idx else ""
        rok_navic_konec = " (příštího roku)" if konec_idx < idx else ""

        col_lhuta1, col_lhuta2 = st.columns(2)
        with col_lhuta1:
            st.info(
                "⏳ **Tvá výpovědní lhůta ZAHÁJÍ běh:**\nAž 1. dne měsíce"
                f" **{mesice_kruh[start_idx]}**{rok_navic_start}."
            )
        with col_lhuta2:
            st.error(
                "🚪 **Tvá práce SKONČÍ a jsi volný/á:**\nAž na konci měsíce"
                f" **{mesice_kruh[konec_idx]}**{rok_navic_konec}."
            )

        if st.button("Uložit výpočet výpovědní doby 💾", key="btn_k4_5_1"):
            vyp_data = (
                f"Podáno v měsíci: {mesic_podani} | Běží od:"
                f" {mesice_kruh[start_idx]} | Končí na konci:"
                f" {mesice_kruh[konec_idx]}"
            )
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"](
                    "Kapitola 4",
                    "Podkapitola 5.1 - Kalkulačka výpovědní doby",
                    vyp_data,
                )
            st.success("Výpočet byl uložen!")

    elif (
        selected_section_4
        == "5.2 Úřad práce, podpora v nezaměstnanosti a rekvalifikace"
    ):
        st.markdown(
            "### 5.2 Kdy mám nárok na podporu a jak pomáhá Úřad práce"
        )

        with st.form("podminky_up"):
            podm_1 = st.checkbox(
                "Během posledních 2 let jsem odpracoval/a alespoň 12 měsíců,"
                " ze kterých se odvádělo důchodové pojištění.",
                key="k4_5_2_p1",
            )
            podm_2 = st.checkbox(
                "Moje poslední práce neskončila vyhazovem za hrubé porušení"
                " pracovní kázně.",
                key="k4_5_2_p2",
            )

            if st.form_submit_button("Zjistit a uložit nárok na podporu 💾"):
                if podm_1 and podm_2:
                    st.success("✅ **Máš nárok na podporu v nezaměstnanosti!**")
                else:
                    st.error("❌ **Zamítnuto.** Nesplňuješ zákonné podmínky.")

                narok_data = (
                    f"Odpracováno 12m: {podm_1} | Bez hrubého porušení:"
                    f" {podm_2}"
                )
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"](
                        "Kapitola 4",
                        "Podkapitola 5.2 - Nárok na podporu",
                        narok_data,
                    )

    elif selected_section_4 == "5.3 Co dělat, když... (Krizový trenažér)":
        st.markdown("### 5.3 Co dělat, když... (Krizový trenažér)")

        with st.form("krize_form"):
            st.write(
                "**Šéf (hází ti na stůl papír):** *„Tady mi okamžitě podepiš"
                " dohodu o ukončení. Končíš! Když to nepodepíšeš hned, napíšu ti"
                " do papírů k výpovědi takové věci, že si už práci nenajdeš.“*"
            )

            k_odp = st.radio(
                "Vyber své řešení:",
                [
                    (
                        "A) Leknu se. Zjevně má na mě nějaké páky. Radši dohodu"
                        " podepíšu a odejdu v tichosti."
                    ),
                    (
                        "B) Papír si vezmu, poděkuji a řeknu: 'Nic hned"
                        " podepisovat nebudu. Vezmu si to domů, přečtu si to v"
                        " klidu a poradím se s právníkem. Vyjádřím se zítra.'"
                    ),
                    (
                        "C) Začnu na něj křičet, zmačkám papír a hodím mu ho na"
                        " hlavu."
                    ),
                ],
                key="k4_5_3_odp",
            )

            if st.form_submit_button("Odeslat a uložit tvou reakci 💾"):
                if k_odp.startswith("B"):
                    st.success("✅ **Zlatá medaile za profesionalitu!**")
                else:
                    st.error("❌ **Chybná reakce.**")

                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"](
                        "Kapitola 4",
                        "Podkapitola 5.3 - Krizový trenažér",
                        k_odp[:30],
                    )

    # =========================================================================
    # SEKCE 6: PRAKTICKÁ DÍLNA
    # =========================================================================
    elif selected_section_4 == "6.1 Praktická dílna (Aktivity 1–5)":
        st.markdown("### 🛠️ 6.1 Praktická dílna")

        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "🗺️ Aktivita 1",
            "🕵️ Aktivita 2",
            "🤖 Aktivita 3",
            "🧾 Aktivita 4",
            "🎭 Aktivita 5",
        ])

        with tab1:
            st.markdown("#### Aktivita 1: Moje profesní mapa")
            if "vykresli_otazku_fn" in st.session_state:
                st.session_state["vykresli_otazku_fn"](
                    "4.6.1",
                    "Aktivita 1 - Moje profesní mapa: Napiš v 3-4 větách, jaké"
                    " dovednosti máš, jaké ti chybí a co plánuješ vyzkoušet.",
                    "4",
                    st.session_state.get("ulozene_odpovedi", {}),
                )

        with tab2:
            st.markdown("#### Aktivita 2: Analýza pracovního inzerátu")
            if "vykresli_otazku_fn" in st.session_state:
                st.session_state["vykresli_otazku_fn"](
                    "4.6.2",
                    "Aktivita 2 - Analýza inzerátu: Vyber si reálný inzerát a"
                    " vypiš požadované dovednosti, výhody a případné Red Flags.",
                    "4",
                    st.session_state.get("ulozene_odpovedi", {}),
                )

        with tab3:
            st.markdown("#### Aktivita 3: AI jako kariérní kouč")
            pozice_ai = st.text_input(
                "Zadejte název pozice:", value="[pozice]", key="a3_pozice"
            )
            prompt = (
                "Pomoz mi připravit se na pohovor na pozici"
                f" {pozice_ai}.\nNejprve mi polož 5 otázek jako personalista. Po"
                " každé mé odpovědi polož doplňující otázku. Na konci vyhodnoť"
                " moje silné stránky, slabá místa a navrhni konkrétní"
                " formulace, které znějí profesionálně, ale přirozeně."
            )
            st.code(prompt, language="text")

        with tab4:
            st.markdown("#### Aktivita 4: Výplatní páska s chybami")
            if "vykresli_otazku_fn" in st.session_state:
                st.session_state["vykresli_otazku_fn"](
                    "4.6.4",
                    "Aktivita 4 - Výplatní páska s chybami: Napiš krátký e-mail"
                    " zaměstnavateli, ve kterém slušně upozorňuješ na chybějící"
                    " příplatek a nelegální srážku.",
                    "4",
                    st.session_state.get("ulozene_odpovedi", {}),
                )

        with tab5:
            st.markdown("#### Aktivita 5: Role-play vyjednávání o mzdě")
            with st.form("form_akt5"):
                st.write("**Hodnocení:**")
                h1 = st.checkbox("Věcnost", key="a5_h1")
                h2 = st.checkbox("Práce s důkazy", key="a5_h2")
                h3 = st.checkbox("Respekt", key="a5_h3")
                if st.form_submit_button("Uložit hodnocení 💾"):
                    st.success("Hodnocení role-play uloženo!")
                    roleplay_data = (
                        f"Hodnocení: Věcnost:{h1}, Důkazy:{h2}, Respekt:{h3}"
                    )
                    if "uloz_odpoved_fn" in st.session_state:
                        st.session_state["uloz_odpoved_fn"](
                            "Kapitola 4",
                            "Dílna - Aktivita 5 Role-play",
                            roleplay_data,
                        )

    # =========================================================================
    # SEKCE 7: ZÁVĚR KAPITOLY A OPAKOVÁNÍ
    # =========================================================================
    elif (
        selected_section_4 == "7.1 Případové studie z praxe"
        or "7.1" in selected_section_4
    ):
        st.markdown("### 📚 7.1 Případové studie z praxe")

        tab_case1, tab_case2 = st.tabs(["🍾 Případ 1", "🚴 Případ 2"])

        with tab_case1:
            st.markdown("#### Případ 1: Studentka na kase a rozbité lahve")
            with st.form("case1_form"):
                c1_odp = st.radio(
                    "Může zaměstnavatel škodu automaticky strhnout ze mzdy?",
                    [
                        "A) Ano, v plné výši.",
                        "B) Ne, bez jejího písemného souhlasu nesmí.",
                    ],
                    key="cs1_rad",
                )
                if st.form_submit_button("Uložit 💾"):
                    if c1_odp.startswith("B"):
                        st.success("✅ Správně!")
                    if "uloz_odpoved_fn" in st.session_state:
                        st.session_state["uloz_odpoved_fn"](
                            "Kapitola 4",
                            "Podkapitola 7.1 - Případ 1 Lahve",
                            c1_odp[:30],
                        )

        with tab_case2:
            st.markdown("#### Případ 2: Kurýr na platformě (Gig economy)")
            with st.form("case2_form"):
                c2_odp = st.radio(
                    "V čem je hlavní finanční chyták práce přes platformy?",
                    [
                        "A) Tržba za zakázku není čistý zisk.",
                        "B) Aplikace neposílá peníze.",
                    ],
                    key="cs2_rad",
                )
                if st.form_submit_button("Uložit 💾"):
                    if c2_odp.startswith("A"):
                        st.success("✅ Správně!")
                    if "uloz_odpoved_fn" in st.session_state:
                        st.session_state["uloz_odpoved_fn"](
                            "Kapitola 4",
                            "Podkapitola 7.1 - Případ 2 Kurýr",
                            c2_odp[:30],
                        )

    elif (
        selected_section_4 == "7.2 Slovníček, rychlé opakování a prověrka"
        or "7.2" in selected_section_4
    ):
        st.markdown("### 🎓 7.2 Závěrečná prověrka")

        with st.form("final_quiz_ch4"):
            q1 = st.radio(
                "1. Proč se konkrétní sazby daní hodí spíše do digitální"
                " aplikace než do tištěné učebnice?",
                [
                    "A) Protože v učebnici by vypadaly nehezky.",
                    "B) Protože se sazby a limity často mění podle legislativy.",
                ],
                key="k4_7_2_q1",
            )
            q2 = st.radio(
                "2. Kdy má člověk nárok na podporu v nezaměstnanosti?",
                [
                    "A) Kdykoliv, když ztratí jakoukoliv práci.",
                    (
                        "B) Pokud má za poslední 2 roky odpracováno alespoň 12"
                        " měsíců a neporušil hrubě kázeň."
                    ),
                ],
                key="k4_7_2_q2",
            )

            if st.form_submit_button("Odeslat test a uložit výsledek 💾"):
                score = 0
                if q1.startswith("B"):
                    score += 1
                if q2.startswith("B"):
                    score += 1

                st.success(f"Výsledek testu: {score}/2")
                proverka_data = f"Skóre testu Kapitoly 4: {score}/2."
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"](
                        "Kapitola 4",
                        "Podkapitola 7.2 - Závěrečná prověrka",
                        proverka_data,
                    )
