import streamlit as st

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

    # Samostatné výběrové menu pro Kapitolu 2
    section_options_2 = [
        "1.1 Peníze jako digitální data (1.1.1 - 1.1.15)",
        "1.2 ČNB a komerční banky",
        "1.3 Platební styk",
        "1.4 Fintech revoluce"
    ]
    selected_section_2 = st.selectbox("📌 Přechod na podkapitolu:", section_options_2, index=0)
    st.divider()

    # =========================================================================
    # 1.1 PENÍZE JAKO DIGITÁLNÍ DATA (1.1.1 až 1.1.15)
    # =========================================================================
    if selected_section_2 == "1.1 Peníze jako digitální data (1.1.1 - 1.1.15)":
        st.markdown("<div class='sub-section-header'>1. BANKOVNÍ SYSTÉM A PENÍZE V 21. STOLETÍ</div><h2>1.1 Peníze jako digitální data</h2>", unsafe_allow_html=True)
        
        st.write("21. století není jen éra umělé inteligence a sociálních sítí. Je to především éra totální transformace toho, jak vnímáme hodnotu. Ještě před pár desítkami let znamenalo „být v bance“ fyzickou návštěvu přepážky, papírování a čekání na úřední hodiny. Dnes? Bankovní systém se stal neviditelným operačním systémem našeho života. Běží na pozadí každého našeho kliknutí, každého „pípnutí“ mobilem u pokladny a každého online nákupu.")

        with st.container(border=True):
            st.markdown("""
            <div class='box-blue'>
                <strong>💡 Proč je to důležité právě teď?</strong>
                <ul>
                    <li><strong>Technologie jako hybatel:</strong> Díky moderním technologiím máme dnes přístup k finančním nástrojům, o kterých se našim rodičům ani nesnilo — od okamžitých mezinárodních plateb až po investování pár korun z mobilní aplikace.</li>
                    <li><strong>Nekonečné možnosti a nová rizika:</strong> Peníze už nejsou jen papírky v peněžence. Jsou to data. A stejně jako každá jiná data, i peníze v 21. století vyžadují novou úroveň digitální gramotnosti.</li>
                    <li><strong>Bankovnictví 2.0:</strong> Tradiční bankovní domy dnes soupeří s agilními fintech startupy. Výsledek? Lepší služby, nižší poplatky, ale také potřeba se v digitálním finančním prostředí umět správně zorientovat.</li>
                </ul>
            </div>
            <div class='box-purple'>
                <strong>🎯 Cíl této sekce:</strong> Nechceme se učit zastaralé definice. Chceme pochopit, jak technologie mění pravidla hry, jaké nástroje máme dnes v kapse a jak je používat tak, aby nám peníze sloužily — a ne naopak.
            </div>
            """, unsafe_allow_html=True)

        st.write("Peníze dnes často nevypadají jako mince nebo bankovky. Když platíš kartou, mobilem nebo hodinkami, většinou se nepřesouvá žádný fyzický předmět. V bankovním systému se změní digitální záznam: jednomu účtu se částka odečte a druhému připíše. Abychom tomu rozuměli, je dobré projít si vývoj peněz od nejstarších forem směny až po současná digitální data.")

        st.markdown("""
        <div class='box-gray'>
            <strong>💡 Základní myšlenka:</strong> Peníze nejsou jen „věc“. Jsou to hlavně důvěryhodný záznam hodnoty, kterému lidé, firmy a stát věří. V různých dobách měl tento záznam podobu dobytka, obilí, kovu, mince, papírové bankovky, bankovního účtu nebo digitální platby v mobilu.
        </div>
        """, unsafe_allow_html=True)

        # 1.1.1 PROČ PENÍZE VŮBEC VZNIKLY
        with st.container(border=True):
            st.markdown("### 1.1.1 Proč peníze vůbec vznikly")
            st.write("Na úplném začátku lidé používali **naturální směnu** — vyměňovali zboží za zboží nebo službu za službu. Například někdo měl obilí a potřeboval boty, jiný uměl boty vyrobit a potřeboval jídlo.")
            st.write("Problém byl v tom, že směna fungovala jen tehdy, když se potkaly dvě potřeby najednou. Tomu se říká **dvojí shoda potřeb**.")
            
            st.info("""
            **🍞 Příklad dvojí shody potřeb:**  
            Pekař chce nové boty. Švec by mu je mohl vyrobit, ale zrovna nepotřebuje chleba. Pekař tedy musí najít někoho dalšího, kdo chce chleba a zároveň má něco, co chce švec. Taková směna je nepraktická, pomalá a omezuje obchod.
            """)
            st.write("Proto se postupně objevily předměty, které lidé přijímali ne proto, že je hned sami potřebovali, ale protože věřili, že je později vymění s někým dalším. Tak vznikl základ peněz.")

        # 1.1.2 KOMODITNÍ PENÍZE
        with st.container(border=True):
            st.markdown("### 1.1.2 Komoditní peníze: hodnota ukrytá ve věci")
            st.write("První peníze měly často podobu komodit — tedy věcí, které měly hodnotu samy o sobě. Mohlo jít například o sůl, obilí, dobytek, kožešiny, mušle, drahé kovy nebo jiné vzácné a žádané předměty.")
            
            st.markdown("""
            <div class='box-gray'>
                <strong>🧵 Česká stopa: plátno jako platidlo</strong><br>
                V českých zemích se podle zprávy cestovatele Ibráhíma ibn Jákúba z 10. století používaly jako prostředek směny také kousky plátna. Právě s tím se často spojuje původ českých slov <em>platit</em>, <em>platba</em> nebo <em>platidlo</em> — tedy dát „plátno“ jako hodnotu při směně. Je to dobrý příklad toho, že peníze nemusely být vždy mince nebo bankovky. Mohly mít podobu věci, které lidé v dané společnosti důvěřovali a kterou byli ochotni přijímat.
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            | Forma peněz | Výhoda | Problém |
            | :--- | :--- | :--- |
            | **Dobytek, obilí, sůl** | Lidé je uměli použít v běžném životě. | Špatně se dělily, skladovaly nebo převážely. |
            | **Mušle, kožešiny, vzácné předměty** | Byly rozpoznatelné a někde společensky ceněné. | Jejich hodnota závisela na místě a zvyklostech. |
            | **Zlato a stříbro** | Byly vzácné, trvanlivé a dobře dělitelné. | Bylo nutné ověřovat ryzost a hmotnost. |
            """)

            st.markdown("##### 🧠 Interaktivní výzva: Vyber komoditu pro platbu")
            st.write("Vyber jednu komoditu, která by mohla sloužit jako peníze. Napiš, v čem by byla praktická a v čem by naopak selhávala:")
            
            kom_sel = st.selectbox("Zvol komoditu:", ["Vyber...", "Sůl 🧂", "Dobytek / Kráva 🐄", "Mušle 🐚", "Zlatý prach ✨"], key="k2_1_1_2_kom")
            if kom_sel == "Sůl 🧂":
                st.info("Sůl je sice užitečná k jídlu, ale při kontaktu s vodou se rozpustí a zničí!")
            elif kom_sel == "Dobytek / Kráva 🐄":
                st.error("❌ Kráva se špatně dělí (jak zaplatíš za jedno kafe?) a navíc ji musíš neustále krmit.")
            elif kom_sel == "Mušle 🐚":
                st.warning("⚠️ Hodnota závisí na zvyklostech. Pokud je kavárník neuznává, kávu ti nedá.")
            elif kom_sel == "Zlatý prach ✨":
                st.success("✅ Skvělé k uchování hodnoty, ale barista musí prach u kasy složitě vážit a ověřovat ryzost.")
            
            st.text_area("Slovní obhajoba tvojí volby:", key="k2_1_1_2_txt")

        # 1.1.3 MINCE A 1.1.4 PAPÍROVÉ PENÍZE
        with st.container(border=True):
            st.markdown("### 1.1.3 Mince: hodnota se začíná standardizovat")
            st.write("Velký posun nastal se vznikem mincí. Mince měly určenou hmotnost, kov, tvar a označení autority, která je vydala. Díky tomu nebylo nutné při každé platbě znovu vážit kus kovu a ověřovat jeho kvalitu.")
            st.write("Mince tedy přinesly:")
            st.markdown("""
            * jednodušší placení,
            * lepší rozpoznatelnost hodnoty,
            * větší důvěru v obchodě,
            * možnost vybírat daně a platit vojsko,
            * silnější roli státu nebo panovníka.
            """)
            st.info("⚖️ **Důležitý princip:** Čím více obchod roste, tím důležitější je, aby lidé věřili, že peníze mají jasnou hodnotu a že je ostatní přijmou.")

            st.markdown("### 1.1.4 Papírové peníze: od potvrzení ke státní měně")
            st.write("Papírové peníze vznikaly postupně. Původně mohly fungovat jako potvrzení, že má člověk někde uložený drahý kov nebo jinou hodnotu. Místo přenášení těžkého zlata bylo jednodušší předat papírový doklad.")
            st.write("Později se z těchto potvrzení staly bankovky. Jejich hodnota už nespočívala v samotném papíru, ale v důvěře, že je přijme společnost a že za nimi stojí banka nebo stát.")
            
            st.markdown("""
            <div class='box-blue'>
                <strong>Proč má bankovka hodnotu, když je to jen papír?</strong><br>
                Bankovka má hodnotu proto, že ji stát uznává jako zákonné platidlo a lidé věří, že s ní zaplatí i jinde. Hodnota tedy není v materiálu, ale v důvěře, pravidlech a fungujícím systému.
            </div>
            """, unsafe_allow_html=True)

        # 1.1.5 až 1.1.8 ZLATÝ STANDARD, BRETTONWOODS, NIXON A FIAT
        with st.container(border=True):
            st.markdown("### 1.1.5 Zlatý standard: když byly peníze navázané na zlato")
            st.write("Dlouhou dobu nebyly papírové peníze chápány jen jako samostatná hodnota. Často fungovaly jako slib, že je lze vyměnit za určité množství zlata. Tomu se říká **zlatý standard**.")
            st.markdown("""
            <div class='box-gray'>
                🥇 <strong>Zlatý standard jednoduše:</strong> Stát nebo centrální banka slíbily, že měna je krytá zlatem. Peníze tedy nebyly jen papírky. Měly být navázané na zásoby zlata, které měl stát nebo centrální banka k dispozici.
            </div>
            """, unsafe_allow_html=True)
            st.write("V praxi to znamenalo, že:")
            st.markdown("""
            * měna měla pevně stanovený vztah ke zlatu,
            * bankovky mohly být za určitých podmínek směnitelné za zlato,
            * stát nemohl jednoduše vytvářet neomezené množství peněz, pokud neměl dost zlata,
            * kurz měn byl stabilnější, protože se odvozoval od zlata,
            * mezinárodní obchod měl pevnější pravidla.
            """)

            st.markdown("### 1.1.6 Brettonwoodský systém: dolar, zlato a svět po druhé světové válce")
            st.write("Po druhé světové válce vznikl nový mezinárodní měnový systém nazývaný **Brettonwoodský systém** (1944). Americký dolar byl navázán na zlato (35 USD za trojskou unci) a ostatní měny na americký dolar.")

            st.markdown("### 1.1.7 Konec vazby na zlato: Nixonův šok")
            st.write("V roce 1971 americký prezident Richard Nixon pozastavil směnitelnost dolaru za zlato (**Nixonův šok**). Tím se svět posunul k systému dnešních **fiat peněz**, jejichž hodnota stojí výhradně na důvěře ve stát, centrální banku a ekonomiku.")

            st.markdown("### 1.1.8 Je lepší mít peníze kryté zlatem, nebo ne?")
            st.markdown("""
            | Systém | Výhody | Nevýhody |
            | :--- | :--- | :--- |
            | **Peníze navázané na zlato** | Omezují přílišné „tištění peněz“, podporují dlouhodobou důvěru a stabilnější měnové kurzy. | Svazují ekonomiku množstvím zlata, ztěžují reakci na krize a mohou prohlubovat poklesy. |
            | **Fiat peníze (dnešní)** | Centrální banka může pružněji reagovat na krize, inflaci, nezaměstnanost. | Vyžadují důvěru v odpovědnou politiku. Při špatném řízení hrozí vysoká inflace. |
            """)

            st.markdown("##### 🧩 Aktivita: Zlatý standard vs. dnešní peníze")
            v_sys = st.radio("Který systém obhajuješ?", ["Peníze kryté zlatem", "Fiat peníze (dnešní systém)"], key="k2_1_1_8_rad")
            st.text_area(f"Vaše obhajoba pro {v_sys}:", key="k2_1_1_8_txt")

        # 1.1.9 & 1.1.10 BEZHOOTOVOSTNÍ PENÍZE A KARTY
        with st.container(border=True):
            st.markdown("### 1.1.9 Bezhotovostní peníze: peníze jako účetní záznam")
            st.write("S rozvojem bank se začaly stále více používat bezhotovostní peníze. Člověk nemusel držet všechny peníze v hotovosti. Mohl je mít uložené v bance a platit převodem, šekem, později kartou nebo internetovým bankovnictvím.")
            st.info("🏦 **Jednoduše řečeno:** Když máš na účtu 2 000 Kč, neleží někde v bance krabička s bankovkami označená tvým jménem. Banka vede záznam, že máš vůči ní nárok na určitou částku.")

            st.markdown("### 1.1.10 Platební karta: plastový klíč k účtu")
            st.write("Platební karta sama o sobě nejsou peníze. Je to nástroj, kterým dáváš pokyn k platbě.")
            
            st.markdown("""
            <div class='box-red'>
                <strong>🔐 Bezpečnostní pravidlo:</strong> Karta, mobil nebo hodinky nejsou „peníze samy o sobě“. Jsou to vstupní brány k penězům na účtu nebo k úvěrovému limitu. Kdo získá přístup k platebnímu nástroji a k ověřovacím prvkům, může dát pokyn k platbě.
            </div>
            """, unsafe_allow_html=True)
            
            with st.expander("🛡️ Jaké technologie platbu chrání (Detailní rozbor)"):
                st.markdown("""
                * **PIN** — číselný kód pro autorizaci.
                * **Biometrie** — otisk prstu / FaceID v telefonu.
                * **Tokenizace** — nahrazení reálného čísla karty dočasným tokenem.
                * **NFC** — bezkontaktní přenos dat na krátkou vzdálenost.
                * **Čip na kartě** — bezpečnější technologie než starý magnetický proužek.
                * **CVC/CVV kód** — bezpečnostní kód pro online platby.
                * **3D Secure** — potvzení platby na internetu v aplikaci banky.
                * **Limity a Notifikace** — kontrola a okamžité upozornění na platbu.
                """)

        # 1.1.11 & 1.1.12 BANKOVNICTVÍ V MOBILU, PHISHING A FINTECH
        with st.container(border=True):
            st.markdown("### 1.1.11 Internetové a mobilní bankovnictví")
            st.write("Správa peněz přes mobil je pohodlná, ale vyžaduje obezřetnost před podvody.")

            st.markdown("##### 🚨 Ukázka podvodného e-mailu (Phishing trenažér)")
            st.info("""
            **Od:** bezpecnost@bnka-podpora-klientu.cz  
            **Předmět:** ZABLOKOVANÝ ÚČET - OKAMŽITÁ AKCE!  
            Vážený kliente, vaše karta byla dočasně zablokována. Pro její okamžité odblokování klikněte IHNED na odkaz níže a přihlaste se:  
            👉 [www.mojebanka-rychle-overeni.com/login](https://#)
            """)

            p_chk1 = st.checkbox("Podezřelá e-mailová adresa odesílatele (překlepy)", key="k2_1_1_11_ph1")
            p_chk2 = st.checkbox("Výzva k nahlášení na Policii", key="k2_1_1_11_ph2")
            p_chk3 = st.checkbox("Text vytváří tlak na rychlé rozhodnutí", key="k2_1_1_11_ph3")
            p_chk4 = st.checkbox("Nebezpečný odkaz nevedoucí na ofic. web banky", key="k2_1_1_11_ph4")

            if st.button("Vyhodnotit hrozbu phishingu", key="k2_1_1_11_btn"):
                if p_chk1 and p_chk3 and p_chk4 and not p_chk2:
                    st.success("Správně! Odhalil jsi všechny 3 varovné signály. Správná reakce: Neklikat na odkaz, nic nevyplňovat a situaci ověřit v oficiální aplikaci banky.")
                else:
                    st.error("Zkus to znovu. Označ 3 varovné znaky (odesílatel, tlak na čas, podezřelý odkaz).")

            st.markdown("### 1.1.12 Okamžité platby, QR platby a fintech")
            st.write("Okamžité platby doručí peníze během sekund, QR kód šetří čas při opisování účtu a **fintech firmy** přinášejí přehledné mobilní správy rozpočtů.")

        # 1.1.13 KRYPTOMĚNY A BLOCKCHAIN
        with st.container(border=True):
            st.markdown("### 1.1.13 Kryptoměny a blockchain")
            st.write("Kryptoměny fungují na technologii **blockchain** — sdílené digitální účetní knize bez centrální banky.")
            st.write("Princip stojí na **decentralizaci**, **transparentnosti**, **nevratnosti** a **vlastní odpovědnosti** za soukromý klíč.")

            st.markdown("##### 🧮 Modelový příklad pravidelného investování (DCA):")
            st.write("Model vkladu 1 000 Kč na začátku + 200 Kč měsíčně po dobu 5 let (Celkem vložených **13 000 Kč**):")
            
            scen_sel = st.selectbox("Vyber modelový scénář vývoje kryptoměny:", [
                "Pesimistický scénář (-20 % ročně)",
                "Nulový scénář (0 % ročně)",
                "Mírně růstový scénář (+5 % ročně)",
                "Silně růstový scénář (+15 % ročně)",
                "Extrémně růstový scénář (+30 % ročně)"
            ], key="k2_dca_1_1_13_sel")

            if "Pesimistický" in scen_sel:
                st.metric("Orientační hodnota po 5 letech", "cca 7 700 Kč", delta="-5 300 Kč (ztráta)")
            elif "Nulový" in scen_sel:
                st.metric("Orientační hodnota po 5 letech", "13 000 Kč", delta="0 Kč (bez zisku)")
            elif "Mírně růstový" in scen_sel:
                st.metric("Orientační hodnota po 5 letech", "cca 14 800 Kč", delta="+1 800 Kč zisk")
            elif "Silně růstový" in scen_sel:
                st.metric("Orientační hodnota po 5 letech", "cca 19 300 Kč", delta="+6 300 Kč zisk")
            else:
                st.metric("Orientační hodnota po 5 letech", "cca 30 700 Kč", delta="+17 700 Kč zisk")

            st.markdown("##### 🏦 Srovnání: Kryptoměny vs. Spořicí účet vs. Penzijní spoření")
            st.markdown("""
            | Možnost | Modelové zhodnocení | Orientační hodnota po 5 letech | Co je hlavní rozdíl |
            | :--- | :--- | :--- | :--- |
            | **Spořicí účet** | cca 3,5 % p.a. | cca 14 200 Kč | Peníze jsou dostupné rychle, výnos je nižší. |
            | **Termínovaný vklad** | cca 3,5–4,0 % p.a. | cca 14 300–14 500 Kč | Sazba garantovaná, peníze jsou vázané. |
            | **Penzijní spoření** | cca 3–5 % p.a. + podpora | cca 14 100–15 100 Kč | Dlouhodobý produkt na stáří se státní podporou. |
            | **Krypto (Nulový scen.)**| 0 % ročně | 13 000 Kč | Bez růstu ceny nevzniká zisk, působí inflace. |
            | **Krypto (Pesim. scen.)**| -20 % ročně | cca 7 700 Kč | U kryptoměn je reálná i výrazná ztráta hodnoty. |
            """)

        # 1.1.14 & 1.1.15 CBDC A SHRNUTÍ VÝVOJE PENĚZ
        with st.container(border=True):
            st.markdown("### 1.1.14 Digitální měny centrálních bank (CBDC)")
            st.write("CBDC představují digitální peníze vydávané přímo centrální bankou (např. Digitální Euro). Na rozdíl od kryptoměny za nimi stojí stát a zákony.")

            st.markdown("### 1.1.15 Shrnutí vývoje peněz")
            st.markdown("""
            | Období / forma | Co sloužilo jako peníze | Na čem stála důvěra |
            | :--- | :--- | :--- |
            | **Naturální směna** | Zboží za zboží | Na přímé dohodě dvou lidí |
            | **Komoditní peníze** | Sůl, obilí, dobytek, mušle, kovy | Na užitečnosti nebo vzácnosti věci |
            | **Mince** | Kovové mince | Na kovu, hmotnosti, ryzosti a autoritě panovníka |
            | **Bankovky** | Papírové peníze | Na důvěře ve stát, banku a zákonné platidlo |
            | **Bezhotovostní peníze** | Zůstatek na účtu | Na bankovním systému, pravidlech a dohledu |
            | **Digitální platby** | Data v bankovních systémech | Na ověření identity a bezpečnosti infrastruktury |
            | **Kryptoměny** | Distribuovaný digitální záznam | Na technologii, síti uživatelů a protokolu |
            """)

            st.markdown("""
            <div class='box-purple'>
                🤖 <strong>AI mentoring prompt:</strong> Zkopíruj tento prompt do AI asistenta:<br>
                <em>„Vysvětli mi vývoj peněz od směny po digitální platby na příkladu běžného nákupu oběda.“</em>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("🎮 **Mikroaktivita: Peníze nejsou jen papír**")
            st.write("Ve dvojici vyberte jednu platbu z běžného dne. Popište cestu peněz: kdo platí, komu, jaký nástroj použije a kde vzniká digitální záznam.")
            st.text_area("Odpověď na mikroaktivitu:", key="k2_1_1_15_micro")

    # =========================================================================
    # 1.2 ČNB A KOMERČNÍ BANKY
    # =========================================================================
    elif selected_section_2 == "1.2 ČNB a komerční banky":
        st.markdown("<div class='sub-section-header'>1. BANKOVNÍ SYSTÉM A PENÍZE V 21. STOLETÍ</div><h2>1.2 ČNB a komerční banky</h2>", unsafe_allow_html=True)
        st.write("Bankovní systém je jeden z nejdůležitějších nervových systémů ekonomiky.")
        
        with st.container(border=True):
            st.markdown("""
            <div class='box-blue'>
                <strong>🏠 Dvoustupňový bankovní systém:</strong>
                <ul>
                    <li><strong>Česká národní banka (ČNB):</strong> Centrální banka ČR. Neobsluhuje běžné občany. Hlídá cenovou stabilitu (inflaci ~2 %) a dohlíží na trh. Je nezávislá na vládě.</li>
                    <li><strong>Komerční banky:</strong> Soukromé banky pro občany a firmy (přijímají vklady, poskytují úvěry a zprostředkovávají platby).</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 1.2.2 Hlavní cíl ČNB: Cenová stabilita")
            st.write("ČNB se snaží, aby peníze neztrácely hodnotu příliš rychle a inflace byla předvídatelná.")
            
            st.markdown("#### 🎮 Simulace: Jsi bankovní rada ČNB!")
            st.write("**Situace:** Inflace je vysoká, ceny v obchodech letí nahoru. Co uděláte s úrokovou sazbou?")
            cnb_action = st.radio("Vaše rozhodnutí:", ["Vyber možnost...", "Zvýšíme sazby", "Snížíme sazby", "Ponecháme sazby beze změny"], key="k2_1_2_cnb_rad")
            
            if st.button("Potvrdit rozhodnutí ČNB", key="k2_1_2_cnb_btn"):
                if cnb_action == "Zvýšíme sazby":
                    st.success("Správný krok k tlumení inflace! Úvěry zdraží, lidé budou méně utrácet a více spořit.")
                elif cnb_action == "Vyber možnost...":
                    st.warning("Musíš vybrat jednu z možností.")
                else:
                    st.error("Rizikové! Pokud nesnížíte objem peněz v oběhu zdražením úvěrů, inflace může dál růst.")

        with st.container(border=True):
            st.markdown("### 🎛️ Simulátor 2T repo sazby ČNB")
            sim_repo = st.slider("2T repo sazba ČNB (%):", min_value=0.5, max_value=10.0, value=4.75, step=0.25, key="k2_1_2_repo")
            
            col_s1, col_s2, col_s3 = st.columns(3)
            hypo_rate = round(sim_repo + 2.1, 2)
            spor_rate = round(max(0.1, sim_repo - 1.5), 2)
            
            col_s1.metric("Odhad sazby hypotéky", f"{hypo_rate} % p.a.")
            col_s2.metric("Odhad spořicího účtu", f"{spor_rate} % p.a.")
            
            if sim_repo >= 6.0:
                col_s3.metric("Dopad na inflaci", "Zpomaluje 📉", delta="- Vysoké úroky")
            elif sim_repo <= 2.0:
                col_s3.metric("Dopad na inflaci", "Roste 📈", delta="+ Rychlé půjčky")
            else:
                col_s3.metric("Dopad na inflaci", "Stabilizovaná ⚖️", delta="Neutralita")

        with st.container(border=True):
            st.markdown("### 🛡️ Pojištění vkladů (100 000 EUR)")
            st.write("Vklady u bank v ČR jsou pojištěny do výše 100 000 EUR (cca 2,5 mil. Kč) na jednoho klienta u jedné banky.")
            
            test_banka = st.radio("Zvol situaci klienta:", [
                "Klient A: 1 800 000 Kč v jedné bance",
                "Klient B: 4 000 000 Kč v jedné bance",
                "Klient C: 4 000 000 Kč rozdělených po 2 000 000 Kč ve dvou bankách"
            ], key="k2_1_2_gar_rad")

            if test_banka == "Klient A: 1 800 000 Kč v jedné bance":
                st.success("✅ **100% Chráněno:** Vklad je pod limitem 100 000 EUR.")
            elif test_banka == "Klient B: 4 000 000 Kč v jedné bance":
                st.error("❌ **Riziko ztráty:** Pojištěno je pouze cca 2,5 mil. Kč. O zbytek nad limit může klient při krachu banky přijít!")
            else:
                st.success("✅ **100% Chráněno:** Vklad je diverzifikován do 2 bank pod zákonný limit.")

    # =========================================================================
    # 1.3 PLATEBNÍ STYK
    # =========================================================================
    elif selected_section_2 == "1.3 Platební styk":
        st.markdown("<div class='sub-section-header'>1. BANKOVNÍ SYSTÉM A PENÍZE V 21. STOLETÍ</div><h2>1.3 Platební styk</h2>", unsafe_allow_html=True)
        st.write("Platební styk znamená převod peněz mezi plátcem a příjemcem. Umožňuje bezpečný a prokazatelný přesun hodnoty.")
        
        with st.container(border=True):
            st.markdown("""
            | Druh | Co znamená | Příklady |
            | :--- | :--- | :--- |
            | **Hotovostní** | Platí se fyzickými penězi. | Bankovky, mince, výběr z bankomatu |
            | **Bezhotovostní** | Peníze se převádějí jako záznam mezi účty. | Bankovní převod, karta, QR platba |
            | **Tuzemský** | Platba v rámci ČR v korunách. | Mezibankovní převod přes CERTIS |
            | **Zahraniční** | Platba do jiné země nebo v jiné měně. | SEPA platba v EUR, mezinárodní převod |
            """)

        with st.container(border=True):
            st.markdown("### 🏛️ CERTIS: Mezibankovní dálnice")
            st.write("Když posíláte peníze do jiné banky v ČR, platba prochází přes systém **CERTIS**, který provozuje Česká národní banka.")

    # =========================================================================
    # 1.4 FINTECH REVOLUCE
    # =========================================================================
    elif selected_section_2 == "1.4 Fintech revoluce":
        st.markdown("<div class='sub-section-header'>1. BANKOVNÍ SYSTÉM A PENÍZE V 21. STOLETÍ</div><h2>1.4 Fintech revoluce</h2>", unsafe_allow_html=True)
        st.write("Fintech (Finance + Technology) označuje firmy a mobilní aplikace, které mění způsob, jakým platíme, spoříme a investujeme.")
        
        with st.container(border=True):
            st.markdown("""
            <div class='box-blue'>
                <strong>📱 Neobanky a moderní služby v ČR:</strong>
                <ul>
                    <li><strong>Revolut / Wise:</strong> Rychlá směna měn, víceměnové účty, mezinárodní platby.</li>
                    <li><strong>mBank / Air Bank:</strong> Banky zaměřené na mobilní aplikaci a jednoduché ovládání bez poboček.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
