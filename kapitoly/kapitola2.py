import streamlit as st
import math

def render():
    st.markdown("<span class='hero-badge'>Kapitola 2</span>", unsafe_allow_html=True)
    st.title("2. Finance a osobní management")
    st.markdown("<p style='font-size: 1rem; color: #64748b; margin-bottom: 1.5rem;'>Finance v běžném životě: peníze, rozhodování a odpovědnost.</p>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown("""
        <div class='box-blue'>
            <strong>🪙 Pointa kapitoly:</strong> Finanční gramotnost není jen znalost pojmů. Je to schopnost rozumět penězům jako systému, bezpečně se rozhodovat, vyhodnocovat rizika a plánovat osobní i podnikové finance tak, aby člověk dokázal reagovat na běžné i krizové situace.
        </div>
        """, unsafe_allow_html=True)

    section_options_2 = [
        "1.1 Peníze jako digitální data (1.1.1 - 1.1.15)",
        "1.2 ČNB a komerční banky",
        "1.3 Platební styk",
        "1.4 Fintech revoluce"
    ]
    selected_section_2 = st.selectbox("📌 Přechod na podkapitolu:", section_options_2, index=1)
    st.divider()

    # =========================================================================
    # 1.1 PENÍZE JAKO DIGITÁLNÍ DATA
    # =========================================================================
    if selected_section_2 == "1.1 Peníze jako digitální data (1.1.1 - 1.1.15)":
        st.markdown("<div class='sub-section-header'>1. BANKOVNÍ SYSTÉM A PENÍZE V 21. STOLETÍ</div><h2>1.1 Peníze jako digitální data</h2>", unsafe_allow_html=True)
        st.write("21. století je érou totální transformace vnímání hodnoty. Bankovní systém se stal neviditelným operačním systémem našeho života.")

        with st.container(border=True):
            st.markdown("""
            <div class='box-blue'>
                <strong>💡 Proč je to důležité:</strong> Peníze jsou dnes digitální data. Vyžadují novou úroveň gramotnosti, porozumění technologiím i ochranu před riziky.
            </div>
            """, unsafe_allow_html=True)
        st.info("Více detailů k 1.1 naleznete v předchozí části učebnice.")

    # =========================================================================
    # 1.2 ČNB A KOMERČNÍ BANKY
    # =========================================================================
    elif selected_section_2 == "1.2 ČNB a komerční banky":
        st.markdown("<div class='sub-section-header'>1. BANKOVNÍ SYSTÉM A PENÍZE V 21. STOLETÍ</div><h2>1.2 ČNB a komerční banky</h2>", unsafe_allow_html=True)
        st.write("Bankovní systém je jeden z nejdůležitějších „nervových systémů“ ekonomiky. Přes banky tečou mzdy, platby za zboží, splátky úvěrů, daně, sociální dávky, investice i peníze firem. Aby tento systém fungoval, musí mu lidé věřit.")

        with st.container(border=True):
            st.markdown("""
            <div class='box-blue'>
                🏦 <strong>Základní rozlišení:</strong><br>
                • <strong>Česká národní banka (ČNB):</strong> Centrální banka ČR. Nejde o běžnou banku pro občany. Hlídá stabilitu měny, finančního systému a pravidla pro banky.<br>
                • <strong>Komerční banky:</strong> Banky, se kterými běžně pracují lidé, firmy a obce (účty, vklady, úvěry, karty, platby).
            </div>
            <div class='box-purple'>
                🧠 <strong>Pointa pro běžný život:</strong> Když platíš kartou, bereš si hypotéku, dostáváš výplatu nebo sleduješ inflaci, nepřímo se setkáváš s rozhodnutími centrální banky i komerčních bank.
            </div>
            """, unsafe_allow_html=True)

        # 1.2.1 POSTAVENÍ ČNB & EURO SIMULÁTOR
        with st.container(border=True):
            st.markdown("### 1.2.1 Postavení ČNB v České republice")
            st.write("ČNB je veřejnoprávní instituce se zvláštním postavením: není komerční firmou, neusiluje o zisk a neposkytuje služby veřejnosti.")
            st.markdown("""
            <div class='box-gray'>
                ⚖️ <strong>Nezávislost:</strong> ČNB je nezávislá na vládě. Smyslem je chránit stabilitu měny před krátkodobým politickým tlakem.
            </div>
            """, unsafe_allow_html=True)

            with st.expander("🇪🇺 ČNB a euro: prozkoumat rozdíl CZK vs. EUR"):
                st.write("Představ si situaci: V Česku je inflace 8 %, ale průměr v eurozóně je 2 %.")
                euro_scen = st.radio("Zvol měnový režim ČR:", ["Vlastní měna (CZK + samostatná ČNB)", "Přijaté Euro (EUR + rozhodování ECB)"], key="k2_1_2_euro_rad")
                if "CZK" in euro_scen:
                    st.success("✅ **Samostatná ČNB:** Může zvýšit sazby např. na 7 %, čímž zdraží půjčky, zvýší úroky na spoření a aktivně tlumí českou inflaci.")
                else:
                    st.warning("⚠️ **Eurozóna (ECB):** ECB nastaví sazby např. na 3.5 % s ohledem na celek. Pro české potřeby je to málo, půjčky zůstávají levné a inflace může déle roste.")

        # 1.2.2 HLAVNÍ CÍL ČNB & SIMULACE BANKOVNÍ RADY
        with st.container(border=True):
            st.markdown("### 1.2.2 Hlavní cíl ČNB")
            st.write("Hlavním cílem ČNB je **péče o cenovou stabilitu** (inflační cíl bývá okolo 2 %).")
            
            st.markdown("#### 🎮 Interaktivní simulace: Jsi bankovní rada ČNB")
            st.write("**Situace:** Inflace je vysoká, ceny v obchodech letí nahoru, lidé si stěžují a firmy méně utrácejí.")
            
            c_action = st.radio("Vaše rozhodnutí o sazbách:", ["Zvýšit úrokové sazby 📈", "Snížit úrokové sazby 📉", "Ponechat sazby beze změny ⚖️"], key="k2_1_2_rada_act")
            c_just = st.text_area("Stručné zdůvodnění vašeho rozhodnutí (pro tiskovou konferenci):", key="k2_1_2_rada_txt")
            
            if st.button("Vyhlásit rozhodnutí Bankovní rady ČNB", key="k2_1_2_rada_btn"):
                if "Zvýšit" in c_action:
                    st.success("✅ **Správné rozhodnutí pro tlumení inflace!** Úvěry zdraží, lidé začnou více spořit a poptávkové tlaky klesnou. Nevýhoda: Zpomalí se hypotéky a firemní investice.")
                elif "Snížit" in c_action:
                    st.error("❌ **Rizikový krok!** Snížením sazeb zlevníte úvěry a přilejete olej do ohně inflace.")
                else:
                    st.warning("⚠️ **Opatrnost:** Ponechání sazeb vyčkává na další data, ale inflace může nadále poškozovat úspory.")

        # 1.2.3 FUNKCE ČNB
        with st.container(border=True):
            st.markdown("### 1.2.3 Co přesně ČNB dělá")
            st.markdown("""
            | Funkce ČNB | Co to znamená | Příklad dopadu na běžný život |
            | :--- | :--- | :--- |
            | **Měnová politika** | Nastavuje podmínky pro hodnotu peněz přes sazby. | Ovlivňuje úroky u hypoték a spoření. |
            | **Emise hotovosti** | Vydává bankovky a mince české koruny. | Určuje vzhled a platnost platidel. |
            | **Dohled nad fin. trhem** | Dohlíží na banky, pojišťovny a záložny. | Hlídá, aby instituce neohrožovaly klienty. |
            | **Finanční stabilita** | Sleduje rizika ohrožující celý systém. | Nastavuje limit pro hypotéky (LTV, DTI). |
            | **Platební systémy** | Provozuje mezibankovní zúčtování CERTIS. | Zajišťuje bezpečné převody mezi bankami. |
            | **Devizové rezervy** | Spravuje zásoby zahraničních měn. | Pomáhá stabilitě kurzu koruny. |
            | **Banka státu** | Vede účty státního rozpočtu. | Souvisí s výdaji a příjmy státu. |
            """)

        # 1.2.4 OCHRANNÉ PRVKY BANKOVEK
        with st.container(border=True):
            st.markdown("### 1.2.4 Hotovost a ochranné prvky bankovek")
            st.write("Ochranné prvky chrání důvěru v peníze a ztěžují padělání.")
            
            prvek_sel = st.selectbox("🔎 Prohlédnout si ochranný prvek bankovky:", [
                "Vodoznak (pohledem proti světlu)",
                "Ochranný proužek s mikrotextem (pohledem)",
                "Reliéfní tisk (hmatem)",
                "Opticky proměnlivá barva (naklopením)",
                "Soutisková značka (pohledem proti světlu)",
                "UV prvky (pomůckou pod UV lampou)"
            ], key="k2_1_2_bankovky_sel")
            
            if "Vodoznak" in prvek_sel:
                st.info("💧 **Vodoznak:** Zřetelný portrét osobnosti viditelný při pohledu proti světlu v nepotištěném okraji.")
            elif "Ochranný proužek" in prvek_sel:
                st.info("📏 **Ochranný proužek:** Metalický proužek zapuštěný do papíru, při pohledu proti světlu tvoří souvislou čáru s textem hodnoty.")
            elif "Reliéfní tisk" in prvek_sel:
                st.info("🖐️ **Reliéfní tisk:** Vystoupený povrch hlavního tiskového obrazce, portrétu a čísla hodnoty nahmatatelný bříšky prstů.")
            elif "Opticky proměnlivá barva" in prvek_sel:
                st.info("🎨 **Opticky proměnlivá barva:** Prvek vytištěný speciální barvou, která při naklonění bankovky mění odstín (např. ze zelené na zlatavou).")
            else:
                st.info("🔍 **Ostatní prvky:** Pomáhají obchodníkům i bankomatům okamžitě ověřit pravost bankovky.")

        # 1.2.6 NÁSTROJE ČNB, REPO SAZBA & HYPOTENÍ SIMULÁTOR
        with st.container(border=True):
            st.markdown("### 1.2.6 Jak ČNB zasahuje do ekonomiky")
            st.write("ČNB ovlivňuje ekonomiku nepřímo — přes cenu peněz (2T repo sazba), devizové intervence a limity úvěrů.")

            st.markdown("#### 🧮 Mini kalkulačka: Repo sazba u spoření a půjčky")
            calc_repo = st.select_slider("Zvol 2T Repo sazbu ČNB:", options=[3.0, 5.0, 7.0], value=5.0, key="k2_1_2_repocalc")
            
            vynos_spor = round(20000 * (calc_repo - 1.5) / 100, 0)
            urok_pujcka = round(100000 * (calc_repo + 3.0) / 100, 0)
            
            col_r1, col_r2 = st.columns(2)
            col_r1.metric("Roční výnos ze spoření 20 000 Kč", f"{max(0, vynos_spor):,.0f} Kč")
            col_r2.metric("Roční úrok z půjčky 100 000 Kč", f"{urok_pujcka:,.0f} Kč")

            st.markdown("---")
            st.markdown("#### 🧮 Simulace: Vyšší sazby vs. Inflace a Hypotéka")
            st.write("Srovnání dvou světů pro domácnost s hypotékou 3 000 000 Kč (25 let) a koš výdajů 40 000 Kč/měsíc:")

            st.markdown("""
            | Modelový svět | Hypotéka (Splátka) | Inflace 40 tis. koše | Celkový měsíční dopad |
            | :--- | :--- | :--- | :--- |
            | **Levné úvěry, vyšší inflace** | Úrok 2,5 % → **13 500 Kč** | Inflace 5 % → **+2 000 Kč** | **15 500 Kč** dodatečný náklad |
            | **Dražší úvěry, nižší inflace** | Úrok 5,0 % → **17 500 Kč** | Inflace 2 % → **+800 Kč** | **18 300 Kč** dodatečný náklad |
            """)
            st.warning("💡 **Závěr:** Pro rodinu s velkou hypotékou je dražší úvěr ihned viditelný (-4 000 Kč na splátce), zatímco přínos pomalejšího zdražování rohlíků a energií je rozptýlený.")

        # 1.2.7 TŘÍDICÍ HRA: ČNB VS. KOMERČNÍ BANKA
        with st.container(border=True):
            st.markdown("### 🧩 Třídicí hra: ČNB, nebo Komerční banka?")
            
            t1 = st.selectbox("1. Vydává bankovky a mince:", ["Vyber...", "ČNB", "Komerční banka"], key="k2_1_2_t1")
            t2 = st.selectbox("2. Vede běžný a spořicí účet občanům:", ["Vyber...", "ČNB", "Komerční banka"], key="k2_1_2_t2")
            t3 = st.selectbox("3. Nastavuje základní 2T repo sazbu:", ["Vyber...", "ČNB", "Komerční banka"], key="k2_1_2_t3")
            t4 = st.selectbox("4. Poskytuje hypotéky a kreditní karty:", ["Vyber...", "ČNB", "Komerční banka"], key="k2_1_2_t4")
            
            if st.button("Vyhodnotit třídění", key="k2_1_2_t_btn"):
                if t1 == "ČNB" and t2 == "Komerční banka" and t3 == "ČNB" and t4 == "Komerční banka":
                    st.success("🎉 Skvěle! Rozumíš rozdílu mezi centrální a komerční bankou.")
                else:
                    st.error("Některé odpovědi nejsou správně, zkus to znovu.")

        # 1.2.11 AKTIVNÍ, PASIVNÍ A NEUTRÁLNÍ OPERACE
        with st.container(border=True):
            st.markdown("### 1.2.11 Aktivní, pasivní a neutrální operace bank")
            st.markdown("""
            | Typ operace | Co znamená pro banku | Příklady |
            | :--- | :--- | :--- |
            | **Pasivní operace** | Banka získává zdroje (závazek banky). | Běžné a spořicí účty, termínované vklady, dluhopisy. |
            | **Aktivní operace** | Banka peníze umísťuje a půjčuje (pohledávka banky). | Hypotéky, spotřebitelské a podnikatelské úvěry, kontokorent. |
            | **Neutrální operace** | Banka poskytuje služby za poplatek (nepůjčuje). | Zpracování plateb, směna měn, vedení účtu, úschova. |
            """)

            st.markdown("#### 🧩 Kvízové karty operací")
            op_q1 = st.radio("Klient si vloží 10 000 Kč na spořicí účet. Z pohledu banky jde o:", ["Aktivní operaci", "Pasivní operaci", "Neutrální operaci"], key="k2_1_2_op1")
            if st.button("Zkontrolovat operaci", key="k2_1_2_op1_btn"):
                if op_q1 == "Pasivní operaci":
                    st.success("Správně! Banka získala peníze a má vůči klientovi závazek je vrátit.")
                else:
                    st.error("Chyba. Vklad klienta je pro banku závazek = pasivní operace.")

        # 1.2.14 POJIŠTĚNÍ VKLADŮ A VÝBĚRY HOTOVOSTI
        with st.container(border=True):
            st.markdown("### 1.2.14 Vklady a jejich ochrana (100 000 EUR)")
            st.write("Vklady jsou pojištěny ze zákona do výše **100 000 EUR** u jedné banky (Garanční systém finančního trhu).")
            
            vklad_amt = st.number_input("Zadej výši vkladu u jedné banky (Kč):", value=3000000, step=100000, key="k2_1_2_vklad_amt")
            limit_czk = 2500000
            
            if vklad_amt <= limit_czk:
                st.success(f"✅ Vklad {vklad_amt:,.0f} Kč je kompletně 100% pojištěn pod zákonným limitem (cca 2,5 mil. Kč).".replace(",", " "))
            else:
                st.error(f"⚠️ Vklad překračuje limit! Pojištěno je pouze cca 2 500 000 Kč. Částka **{(vklad_amt - limit_czk):,.0f} Kč** nesou plné riziko při krachu banky!".replace(",", " "))

            st.markdown("---")
            st.markdown("#### 💵 Pravidla pro velké výběry hotovosti na pobočce")
            st.markdown("""
            * **Do cca 100 000 Kč:** Běžný výběr z pokladny bez hlášení (podle pravidel konkrétní banky).
            * **Nad 100 000 až 300 000 Kč:** Některé banky (např. KB) vyžadují hlášení 1-2 dny předem.
            * **Nad 300 000 Kč:** Většina bank (např. ČSOB) vyžaduje povinné předchozí objednání hotovosti a prověřuje pravidla AML (proti praní špinavých peněz).
            """)

    # =========================================================================
    # 1.3 PLATEBNÍ STYK
    # =========================================================================
    elif selected_section_2 == "1.3 Platební styk":
        st.markdown("<div class='sub-section-header'>1. BANKOVNÍ SYSTÉM A PENÍZE V 21. STOLETÍ</div><h2>1.3 Platební styk</h2>", unsafe_allow_html=True)
        st.write("Platební styk znamená převod peněz mezi plátcem a příjemcem. Je to infrastruktura důvěry.")

        with st.container(border=True):
            st.markdown("### 1.3.2 Druhy platebního styku")
            st.markdown("""
            | Druh | Co znamená | Příklady |
            | :--- | :--- | :--- |
            | **Hotovostní** | Platí se fyzickými penězi. | Bankovky, mince, výběr z bankomatu. |
            | **Bezhotovostní** | Převod účetních záznamů mezi účty. | Platba kartou, prevod z účtu, QR platba. |
            | **Tuzemský** | Převod v rámci ČR v CZK. | Platba přes CERTIS mezi českými bankami. |
            | **Zahraniční** | Převod do jiné země nebo měny. | SEPA platba v EUR, mezinárodní převod SWIFT. |
            | **Opakovaný** | Platba probíhá pravidelně. | Trvalý příkaz, inkaso, SIPO. |
            """)

            st.markdown("#### 🧭 Aktivita: Poznej správný typ platby")
            p_typ = st.radio("Jaký typ platby představuje trvalý příkaz na nájem v ČR?", [
                "Bezhotovostní, tuzemská, opakovaná platba",
                "Hotovostní, tuzemská, jednorázová platba",
                "Bezhotovostní, zahraniční, okamžitá platba"
            ], key="k2_1_3_ptyp")
            if p_typ == "Bezhotovostní, tuzemská, opakovaná platba":
                st.success("✅ Správně!")

        # 1.3.4 CERTIS
        with st.container(border=True):
            st.markdown("### 1.3.4 CERTIS: Zúčtovací dálnice ČNB")
            st.write("CERTIS (Czech Express Real Time Interbank Gross Settlement System) spravuje ČNB.")
            
            c_bank_scen = st.selectbox("Zvol příjemce platby:", ["Příjemce má účet ve STEJNÉ bance jako vy", "Příjemce má účet v JINÉ bance"], key="k2_1_3_certis_sel")
            if "STEJNÉ" in c_bank_scen:
                st.info("ℹ️ **Interní převod:** Banka si platbu zúčtuje ve vlastním systému. CERTIS se vůbec nepoužije.")
            else:
                st.success("🚀 **Mezibankovní převod:** Banka plátce odešle pokyn do systému CERTIS v ČNB, který platbu bezpečně vypořádá s bankou příjemce.")

        # 1.3.5 CESTA PLATBY KARTOU
        with st.container(border=True):
            st.markdown("### 1.3.5 Cesta platby kartou (Skládačka)")
            st.write("Seřaď krok po kroku, co se stane při přiložení karty k terminálu:")
            
            s1 = st.selectbox("1. Krok:", ["Vyber...", "Přiložení karty/mobilu k terminálu", "Terminál odešle požadavek přes karetní síť", "Banka plátce ověří zůstatek a PIN", "Schválení platby"], key="k2_1_3_s1")
            s2 = st.selectbox("2. Krok:", ["Vyber...", "Přiložení karty/mobilu k terminálu", "Terminál odešle požadavek přes karetní síť", "Banka plátce ověří zůstatek a PIN", "Schválení platby"], key="k2_1_3_s2")
            
            if st.button("Zkontrolovat pořadí platby", key="k2_1_3_card_btn"):
                if "Přiložení" in s1 and "odešle" in s2:
                    st.success("✅ Správný začátek procesu!")
                else:
                    st.error("Zkus to znovu: 1. Přiložení -> 2. Odeslání požadavku terminálem -> 3. Ověření bankou -> 4. Schválení.")

        # 1.3.6 PHISHING ESCAPE ROOM
        with st.container(border=True):
            st.markdown("### 🚨 1.3.6 Phishing escape room: Nenech se okrást")
            st.write("Vyhodnoť bezpečnost zpráv a nenech podvodníky získat tvoje údaje:")

            st.error("📩 Zpráva: 'Váš účet byl zablokován kvůli neobvyklému přihlášení. Pro odblokování se přihlaste na: www.vasa-banka-sec.com'")
            ph_ans1 = st.radio("Tvoje reakce na tuto zprávu:", ["Kliknu na odkaz a zadám údaje", "Zprávu ignoruji a zkontroluji účet v oficiální aplikaci", "Pošlu kód z SMS pro potvrzení"], key="k2_1_3_ph1")
            
            if ph_ans1 == "Zprávu ignoruji a zkontroluji účet v oficiální aplikaci":
                st.success("✅ Zachránil jsi své peníze! Banka nikdy neposílá odkazy na přihlášení v SMS.")
            elif ph_ans1 == "Kliknu na odkaz a zadám údaje":
                st.error("💥 Stala se chyba! Odkaz vedl na falešný web a útočníci získali tvoje heslo.")

    # =========================================================================
    # 1.4 FINTECH REVOLUCE
    # =========================================================================
    elif selected_section_2 == "1.4 Fintech revoluce":
        st.markdown("<div class='sub-section-header'>1. BANKOVNÍ SYSTÉM A PENÍZE V 21. STOLETÍ</div><h2>1.4 Fintech revoluce</h2>", unsafe_allow_html=True)
        st.write("Fintech (Finance + Technology) označuje moderní služby, které mění placení, investice i správu financí v mobilu.")

        with st.container(border=True):
            st.markdown("### 1.4.2 Neobanky a moderní finanční aplikace")
            st.markdown("""
            | Služba | Hlavní zaměření | Na co si dát pozor |
            | :--- | :--- | :--- |
            | **Revolut** | Víceměnový účet, levná směna, cestování, kryptoměny. | Zkontrolovat sídlo a typ bankovní licence. |
            | **Wise** | Mezinárodní převody za reálné středové kurzy. | Není to plnohodnotná běžná banka pro všechny české služby. |
            | **mBank / Air Bank** | Banky s důrazem na špičkové mobilní bankovnictví. | Česká bankovní licence a pojištění vkladů do 100 000 EUR. |
            """)

        with st.container(border=True):
            st.markdown("### 📱 Audit finanční aplikace")
            st.write("Využij formulář k otestování tvojí oblíbené finanční aplikace:")
            
            app_name = st.text_input("Název aplikace (např. Revolut, Air Bank, Portu):", key="k2_1_4_app_name")
            app_fee = st.selectbox("Jak aplikace vydělává?", ["Poplatky z transakcí", "Měsíční předplatné", "Prodej doplňkových služeb", "Nevím"], key="k2_1_4_app_fee")
            app_verdict = st.radio("Hodnocení:", ["Pomáhá mi řídit peníze", "Spíše mě tlačí k impulzivnímu utrácení"], key="k2_1_4_app_verd")
            
            if st.button("Uložit audit aplikace", key="k2_1_4_app_btn"):
                st.success(f"Audit aplikace **{app_name}** byl uložen! Kritické hodnocení poplatků a cílů aplikace je základem finanční gramotnosti.")

        with st.container(border=True):
            st.markdown("### ⚖️ Debata: Fintech — pomocník, nebo past?")
            col_d1, col_d2 = st.columns(2)
            with col_d1:
                st.success("💚 **Tým A (Pomocník):**\n• Rychlé přehledy výdajů\n• Snadné investování malých částek\n• Nízké poplatky za směnu")
            with col_d2:
                st.error("🔴 **Tým B (Past):**\n• Impulzivní nákupy jedním klikem\n• Rychlé nebezpečné půjčky (BNPL)\n• Riziko ztráty dat a podvodů")
