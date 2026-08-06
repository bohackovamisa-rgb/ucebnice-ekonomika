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
        "1.1 Peníze jako digitální data",
        "1.2 ČNB a komerční banky",
        "1.3 Platební styk",
        "1.4 Fintech revoluce"
    ]
    selected_section_2 = st.selectbox("📌 Přechod na podkapitolu:", section_options_2, index=0)
    st.divider()

    # =========================================================================
    # 1.1 PENÍZE JAKO DIGITÁLNÍ DATA 
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
            **🍞 Příklad dvojí shoda potřeb:**  
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
                * **3D Secure** — potvrzení platby na internetu v aplikaci banky.
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
        st.write("Bankovní systém není jen síť poboček a bankomatů. Je to jeden z nejdůležitějších „nervových systémů“ ekonomiky. Přes banky tečou mzdy, platby za zboží, splátky úvěrů, daně, sociální dávky, investice i peníze firem. Aby tento systém fungoval, musí mu lidé věřit.")

        with st.container(border=True):
            st.markdown("""
            <div class='box-blue'>
                🏦 <strong>Základní rozlišení:</strong><br>
                • <strong>Česká národní banka (ČNB):</strong> Centrální banka České republiky. Nejde o běžnou banku pro občany. Je to instituce, která hlídá stabilitu měny, finančního systému a pravidla pro banky.<br>
                • <strong>Komerční banky:</strong> Banky, se kterými běžně pracují lidé, firmy a obce. Vedou účty, přijímají vklady, poskytují úvěry, vydávají platební karty a zajišťují platby.
            </div>
            <div class='box-purple'>
                🧠 <strong>Pointa pro běžný život:</strong> Když platíš kartou, bereš si hypotéku, dostáváš výplatu na účet nebo sleduješ inflaci, nepřímo se setkáváš s rozhodnutími centrální banky i se službami komerčních bank.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 1.2.1 Postavení ČNB v České republice")
            st.write("Česká národní banka je centrální banka ČR. Její činnost upravuje zákon o ČNB. Je to veřejnoprávní instituce: neusiluje o zisk a neposkytuje služby běžným občanům.")
            
            st.markdown("""
            <div class='box-gray'>
                ⚖️ <strong>Důležité (Nezávislost):</strong> ČNB je při plnění úkolů nezávislá na vládě. Smyslem je chránit stabilitu měny před krátkodobými politickými tlaky.
            </div>
            """, unsafe_allow_html=True)

            with st.expander("🇪🇺 ČNB a euro: proč je česká situace jiná"):
                st.write("V eurozóně nerozhoduje národní banka samostatně, ale Evropská centrální banka (ECB).")
                st.write("**Příklad Slovensko (2009):** Národní banka Slovenska dál existuje a dohlíží na trh, ale sazby určí ECB pro celou eurozónu.")
                
                st.markdown("##### 🧮 Modelový příklad (CZK vs. EUR):")
                st.write("Pokud je v ČR vyšší inflace než v eurozóně, samostatná ČNB může zvýšit sazby na 6–7 % a brzdit zdražování. Kdyby ČR platila eurem, ECB by nastavovala sazby pro celou eurozónu (např. 3–4 %), což by českému trhu k tlumení inflace nestačilo.")
                
                euro_mode = st.radio("Zvol simulovaný měnový režim ČR při vysoké české inflaci:", [
                    "Vlastní korunová měna (ČNB zvýší sazby na 7 %)",
                    "Společné Euro (ECB drží sazby na 3.5 %)"
                ], key="k2_1_2_1_euro_rad")
                
                if "Vlastní" in euro_mode:
                    st.success("✅ **Výsledek:** Vyšší sazby zdraží půjčky a hypotéky v ČR, ale účinněji tlumí inflaci a chrání úspory.")
                else:
                    st.warning("⚠️ **Výsledek:** Zůstávají levnější hypotéky, ale inflace v ČR může trvat déle a více znehodnocovat mzdy.")

        with st.container(border=True):
            st.markdown("### 1.2.2 Hlavním cílem ČNB je cenová stabilita")
            st.write("ČNB pečuje o **cenovou stabilitu** (udržovat inflaci kolem cíle 2 %).")
            
            st.markdown("#### 🎮 Interaktivní simulace: Jsi bankovní rada ČNB")
            st.write("**Situace:** Inflace je vysoká, lidé si stěžují na zdražování, hypotéky jsou drahé a firmy méně utrácejí.")
            
            br_action = st.radio("Jako Bankovní rada ČNB rozhodněte o sazbách:", [
                "Zvýšíme úrokové sazby 📈",
                "Snížíme úrokové sazby 📉",
                "Ponecháme sazby beze změny ⚖️"
            ], key="k2_1_2_2_br_rad")
            
            br_txt = st.text_area("Napiš 1 větu tiskového prohlášení zdůvodňující vaše rozhodnutí:", key="k2_1_2_2_br_txt")
            
            if st.button("Vydat rozhodnutí Bankovní rady", key="k2_1_2_2_br_btn"):
                if "Zvýšíme" in br_action:
                    st.success("✅ **Správný krok k tlumění inflace!** Úvěry a hypotéky zdraží, spotřeba klesne a inflace se zpomalí. Nevýhoda: Zpomalení ekonomického růstu.")
                elif "Snížíme" in br_action:
                    st.error("❌ **Rizikové rozhodnutí!** Levnější úvěry povzbudí utrácení a přilejí olej do inflačního ohně.")
                else:
                    st.warning("⚠️ **Neutralita:** Vyčkáváte na další data, ale vysoká inflace nadále znehodnocuje úspory obyvatel.")

        with st.container(border=True):
            st.markdown("### 1.2.3 Co přesně ČNB dělá (8 klíčových funkcí)")
            st.markdown("""
            | Funkce ČNB | Co to znamená | Příklad dopadu na běžný život |
            | :--- | :--- | :--- |
            | **Měnová politika** | Nastavuje podmínky pro hodnotu peněz přes sazby. | Ovlivňuje úroky u hypoték, spoření i úvěrů. |
            | **Emise hotovosti** | Vydává bankovky a mince ČK a pečuje o oběh. | Určuje vzhled, ochranné prvky a platnost peněz. |
            | **Dohled nad fin. trhem**| Dohlíží na banky, pojišťovny, záložny a investiční firmy. | Hlídá, aby banky neohrožovaly vklady klientů. |
            | **Finanční stabilita** | Sleduje rizika ohrožující celý systém. | Nastavuje limity pro hypotéky (LTV, DTI). |
            | **Platební systémy** | Provozuje a dohlíží na mezibankovní zúčtování CERTIS. | Zajišťuje bezpečné převody peněz mezi bankami. |
            | **Devizové rezervy** | Spravuje zásoby zahraničních měn a zlata. | Pomáhá kurzu koruny a důvěře v ekonomiku. |
            | **Banka státu** | Vede účty státního rozpočtu a státních orgánů. | Souvisí s výplatami dávek nebo příjmy z daní. |
            """)

        with st.container(border=True):
            st.markdown("### 1.2.4 Hotovost a ochranné prvky bankovek")
            st.write("Ochranné prvky ztěžují padělání a chrání důvěru v peníze.")
            st.write("Dělí se na prvky kontrolované **pohledem** (vodoznak, proužek), **hmatem** (reliéfní tisk), **naklopením** (opticky proměnlivá barva) a **pomůckami** (UV světlo).")
            
            st.markdown("##### 🔎 Interaktivní prohlížeč ochranných prvků:")
            prvek_opt = st.selectbox("Zvol ochranný prvek k prozkoumání:", [
                "Vodoznak (pohledem proti světlu)",
                "Ochranný proužek s mikrotextem (pohledem proti světlu)",
                "Reliéfní tisk (hmatem)",
                "Opticky proměnlivá barva (naklopením bankovky)",
                "Soutisková značka (pohledem proti světlu)"
            ], key="k2_1_2_4_prvek")
            
            if "Vodoznak" in prvek_opt:
                st.info("💧 **Vodoznak:** Zřetelný portrét osobnosti viditelný v nepotištěném okraji při pohledu proti světlu.")
            elif "Ochranný proužek" in prvek_opt:
                st.info("📏 **Ochranný proužek:** Metalický proužek zapuštěný do papíru, při pohledu proti světlu tvoří tmavou čáru s mikrotextem nominalní hodnoty.")
            elif "Reliéfní tisk" in prvek_opt:
                st.info("🖐️ **Reliéfní tisk:** Hmatatelně vystoupená barva na portrétu a číselné hodnotě na lícové straně.")
            elif "Opticky proměnlivá barva" in prvek_opt:
                st.info("🎨 **Opticky proměnlivá barva:** Speciální tisk, který při naklonění mění barvu (např. ze zelené na zlatavou).")
            else:
                st.info("🧩 **Soutisková značka:** Prvek tištěný z obou stran bankovky, který se proti světlu přesně doplňuje v celek.")

        with st.container(border=True):
            st.markdown("### 1.2.5 Kdo ČNB řídí")
            st.write("Nejvyšším orgánem je **7členná Bankovní rada** (guvernér, 2 viceguvernéři, 4 členové), které jmenuje prezident republiky. V čele stojí guvernér (Aleš Michl).")

        with st.container(border=True):
            st.markdown("### 1.2.6 Jak ČNB zasahuje do ekonomiky & Nástroje")
            st.write("ČNB ovlivňuje ekonomiku nepřímo — přes cenu peněz a pravidla trhu.")
            st.markdown("""
            | Nástroj ČNB | Jak funguje | Co ovlivňuje |
            | :--- | :--- | :--- |
            | **2T Repo sazba** | Hlavní sazba, za kterou si banky ukládají přebytečné peníze u ČNB. | Úroky hypoték, půjček i spořicích účtů. |
            | **Repo operace** | Stahování nebo dodávání peněz bankám. | Množství likvidity na trhu. |
            | **Diskontní / Lombardní sazba** | Spodní a horní hranice krátkodobých sazeb. | Nouzové financování bank a tržní dno sazeb. |
            | **Povinné minimální rezervy (PMR)** | Banky musí držet část vkladů u ČNB. | Množství peněz volně dostupných k půjčkám. |
            | **Devizové intervence** | Nákup nebo prodej cizích měn. | Kurz koruny, dovozní a vývozní ceny. |
            | **Makroobezřetnostní limity** | Pravidla pro hypotéky (LTV, DTI, DSTI). | Riziko přehřátí trhu nemovitostí a dluhů. |
            """)

            st.markdown("#### 🧮 Mini kalkulačka: Repo sazba v praxi")
            repo_val = st.select_slider("Zvol 2T repo sazbu ČNB:", options=[3.0, 5.0, 7.0], value=5.0, key="k2_1_2_6_repo_slider")
            
            vynos_spor = max(0, round(20000 * (repo_val - 1.5) / 100, 0))
            urok_pujc = round(100000 * (repo_val + 3.0) / 100, 0)
            
            col_cr1, col_cr2 = st.columns(2)
            col_cr1.metric("Orientační roční výnos ze spoření 20 000 Kč", f"{vynos_spor:,.0f} Kč".replace(",", " "))
            col_cr2.metric("Orientační roční úrok z půjčky 100 000 Kč", f"{urok_pujc:,.0f} Kč".replace(",", " "))

            st.markdown("---")
            st.markdown("#### 🧮 Simulace: Vyšší sazby vs. Inflace a hypotéka (Koš výdajů 40 000 Kč)")
            st.write("Porovnání dopadu pro rodinu s hypotékou 3 000 000 Kč na 25 let a měsíčními výdaji 40 000 Kč (potraviny 15k, energie 8k, doprava 5k, předplatná 3k, volný čas 6k, rezerva 3k):")

            st.markdown("""
            | Modelový svět | Hypotéka (splátka) | Inflace 40 tis. koše | Celkový dopad na peněženku |
            | :--- | :--- | :--- | :--- |
            | **Levné úvěry, vyšší inflace** | 2,5 % → **13 500 Kč** | Inflace 5 % → **+2 000 Kč** | Splátka levná, nákupy výrazně dražší. |
            | **Dražší úvěry, nižší inflace** | 5,0 % → **17 500 Kč** | Inflace 2 % → **+800 Kč** | **Splátka dražší o 4 000 Kč**, nákupy rostou pomaleji. |
            """)
            st.info("💡 **Poučení:** Pro zadluženou rodinu je dražší hypotéka okamžitou zátěží. Nižší inflace jí sice šetří peníze při nákupu, ale pro peněženku je růst splátky viditelnější.")

        with st.container(border=True):
            st.markdown("### 🧩 Třídicí hra: ČNB, nebo komerční banka?")
            
            t_ans1 = st.selectbox("1. Vydává bankovky a mince:", ["Vyber...", "ČNB", "Komerční banka"], key="k2_1_2_7_t1")
            t_ans2 = st.selectbox("2. Vede běžný a spořicí účet občanům:", ["Vyber...", "ČNB", "Komerční banka"], key="k2_1_2_7_t2")
            t_ans3 = st.selectbox("3. Nastavuje 2T repo sazbu:", ["Vyber...", "ČNB", "Komerční banka"], key="k2_1_2_7_t3")
            t_ans4 = st.selectbox("4. Poskytuje hypotéky občanům:", ["Vyber...", "ČNB", "Komerční banka"], key="k2_1_2_7_t4")
            
            if st.button("Vyhodnotit třídicí hru", key="k2_1_2_7_btn"):
                if t_ans1 == "ČNB" and t_ans2 == "Komerční banka" and t_ans3 == "ČNB" and t_ans4 == "Komerční banka":
                    st.success("🎉 Skvěle! Přesně rozumíš rozdělení rolí mezi ČNB a komerční banky.")
                else:
                    st.error("Některé odpovědi nejsou správně. Zkus to znovu!")

        with st.container(border=True):
            st.markdown("### 1.2.8 až 1.2.10 Komerční banky a jejich služby")
            st.write("Komerční banky přijímají vklady, poskytují úvěry a zajišťují platby za účelem zisku. Potřebují bankovní licencí od ČNB.")
            
            col_b1, col_b2 = st.columns(2)
            with col_b1:
                st.markdown("##### 👤 Služby pro občany:")
                st.markdown("* Běžné a spořicí účty\n* Platební karty a mobilní platby\n* Hypotéky a spotřebitelské úvěry\n* Směna měn a investice")
            with col_b2:
                st.markdown("##### 🏢 Služby pro firmy:")
                st.markdown("* Podnikatelské účty a terminály\n* Provozní a investiční úvěry\n* Bankovní záruky a akreditivy\n* Správa měnových rizik")

        with st.container(border=True):
            st.markdown("### 1.2.11 Aktivní, pasivní a neutrální operace bank")
            st.markdown("""
            | Typ operace | Co znamená | Příklady z praxe |
            | :--- | :--- | :--- |
            | **Pasivní operace** | Banka získává zdroje (závazky banky). | Běžné účty, spořicí účty, termínované vklady, dluhopisy. |
            | **Aktivní operace** | Banka umístí peníze a získá výnos (aktiva banky). | Hypotéky, spotřebitelské půjčky, kontokorenty, nákup cenných papírů. |
            | **Neutrální operace** | Banka poskytuje služby za poplatky/provize. | Zpracování plateb, směna měn, zprostředkování investic/pojištění. |
            """)

            st.markdown("##### 🧩 Rozhodovací karty operací:")
            op_card = st.radio("Zvol situaci: 'Banka poskytne rodině hypotéku 3 000 000 Kč'. Z pohledu banky jde o:", [
                "Pasivní operaci",
                "Aktivní operaci",
                "Neutrální operaci"
            ], key="k2_1_2_11_card")
            
            if st.button("Zkontrolovat operaci", key="k2_1_2_11_btn"):
                if op_card == "Aktivní operaci":
                    st.success("✅ Správně! Banka investovala peníze a vznikla jí vůči klientovi pohledávka = aktivní operace.")
                else:
                    st.error("❌ Špatně. Poskytnutý úvěr je pro banku aktivní operací.")

        with st.container(border=True):
            st.markdown("### 1.2.12 & 1.2.13 Jak banka vydělává, rizika a dohled")
            st.write("Banka vydělává na **úrokové marži** (rozdíl mezi úroky z úvěrů a vkladů) a **poplatcích**.")
            st.write("Nese ale **úvěrové**, **likviditní**, **úrokové**, **měnové**, **operační** a **kybernetické riziko**.")
            
            st.markdown("##### 🛠️ Mini audit bankovního analytika:")
            st.write("Představ si, že hodnotíš bezpečnost banky. Zaškrtni 3 klíčové piláře zdravé banky:")
            a_chk1 = st.checkbox("Banka půjčuje klientům, kteří zvládají splácet (nízké úvěrové riziko)", key="k2_1_2_13_a1")
            a_chk2 = st.checkbox("Banka rozdá 100 % všech vkladů na 30leté hypotéky bez rezerva", key="k2_1_2_13_a2")
            a_chk3 = st.checkbox("Banka drží dostatek kapitálu pro pokrytí případných ztrát", key="k2_1_2_13_a3")
            a_chk4 = st.checkbox("Banka má dostatek likvidity pro běžné denní výběry klientů", key="k2_1_2_13_a4")

            if st.button("Vyhodnotit audit banky", key="k2_1_2_13_btn"):
                if a_chk1 and a_chk3 and a_chk4 and not a_chk2:
                    st.success("✅ Výborně! Banka musí vyvažovat zisk s přísným řízením rizika, likvidity a kapitálu.")
                else:
                    st.error("Zkus to znovu. Označ 3 správné bezpečnostní zásady (bez 100% půjčení vkladů).")

        with st.container(border=True):
            st.markdown("### 1.2.14 Vklady, pojištění a výběry hotovosti")
            st.write("Vklady u bank v ČR jsou zákonem pojištěny do výše **100 000 EUR** (cca 2,5 mil. Kč) na klienta u jedné banky prostřednictvím Fondu pojištění vkladů.")

            st.markdown("""
            | Výše vkladu klienta u 1 banky | Stav pojištění vkladu |
            | :--- | :--- |
            | **500 000 Kč** | 100% pojištěno v plné výši. |
            | **2 000 000 Kč** | 100% pojištěno v plné výši (pod limit cca 2,5 mil. Kč). |
            | **4 000 000 Kč** | Pojištěna je jen část do limitu cca 2,5 mil. Kč; zbytek nese riziko. |
            | **2 mil. v Bance A + 2 mil. v Bance B** | Pojištěno 100 % v obou bankách (limit se počítá pro každou banku zvlášť). |
            """)

            st.markdown("##### 💵 Limity a pravidla výběru hotovosti na pobočce:")
            st.write("Výběr velkých částek vyžaduje přípravu z důvodu bezpečnosti, provozu i zákonů AML (proti praní špinavých peněz).")
            st.markdown("""
            * **Bankomat:** Řídí se denním limitem karty.
            * **Menší výběr na pobočce:** Běžně bez objednání.
            * **Větší výběr (např. nad 100 000 až 300 000 Kč):** Hranice se liší podle banky. Například KB uvádí hlášení nad 100 000 Kč, zatímco ČSOB požaduje objednání až nad 300 000 Kč.
            * **Vysoký výběr (např. 600 000 Kč na koupi auta):** Vždy vyžaduje předchozí objednání hotovosti 1–2 dny předem.
            """)

    # =========================================================================
    # 1.3 PLATEBNÍ STYK
    # =========================================================================
    elif selected_section_2 == "1.3 Platební styk":
        st.markdown("<div class='sub-section-header'>1. BANKOVNÍ SYSTÉM A PENÍZE V 21. STOLETÍ</div><h2>1.3 Platební styk</h2>", unsafe_allow_html=True)
        st.write("Platební styk znamená převod peněz mezi plátcem a příjemcem. Je to infrastruktura důvěry, která umožňuje bezpečný a prokazatelný přesun hodnoty.")

        with st.container(border=True):
            st.markdown("### 1.3.2 Druhy platebního styku")
            st.markdown("""
            | Druh | Co znamená | Příklady |
            | :--- | :--- | :--- |
            | **Hotovostní** | Platí se fyzickými penězi. | Bankovky, mince, výběr z bankomatu. |
            | **Bezhotovostní** | Peníze se převádějí jako záznam mezi účty. | Bankovní převod, karta, QR platba. |
            | **Tuzemský** | Platba v rámci ČR v korunách. | Převod mezi českými bankami přes CERTIS. |
            | **Zahraniční** | Platba do jiné země nebo v jiné měně. | SEPA platba v eurech, mezinárodní SWIFT. |
            | **Jednorázový** | Zadá se pro jeden konkrétní převod. | Úhrada jedné faktury. |
            | **Opakovaný** | Provádí se pravidelně nebo automaticky. | Trvalý příkaz, SIPO, inkaso, předplatné. |
            | **Okamžitý** | Peníze dorazí během několika sekund. | Okamžitá platba mezi bankami. |
            """)

            st.markdown("##### 🧭 Aktivita: Vyber správný typ platby")
            p_scen = st.selectbox("Zvol situaci:", [
                "Platím kávu v hotovosti",
                "Posílám nájem trvalým příkazem v ČR",
                "Platím předplatné Spotify",
                "Nakupuji v německém e-shopu v EUR"
            ], key="k2_1_3_2_scen")

            if p_scen == "Platím kávu v hotovosti":
                st.info("👉 Hotovostní, tuzemská, jednorázová platba.")
            elif p_scen == "Posílám nájem trvalým příkazem v ČR":
                st.info("👉 Bezhotovostní, tuzemská, opakovaná platba.")
            elif p_scen == "Platím předplatné Spotify":
                st.info("👉 Bezhotovostní, mezinárodní/tuzemská, opakovaná platba kartou.")
            else:
                st.info("👉 Bezhotovostní, zahraniční (SEPA/karta), jednorázová platba.")

        with st.container(border=True):
            st.markdown("### 1.3.3 Nejběžnější platební nástroje")
            st.write("Příkaz k úhradě, trvalý příkaz, inkaso, SIPO, platební karta (debetní/kreditní), Apple/Google Pay, QR platba, SEPA platba.")

        with st.container(border=True):
            st.markdown("### 1.3.4 CERTIS: Mezibankovní dálnice v ČR")
            st.write("**CERTIS** (Czech Express Real Time Interbank Gross Settlement System) je systém mezibankovního zúčtování v CZK spravovaný České národní bankou.")

            st.markdown("""
            | Situace platby | Jak proběhne zúčtování | Jde přes CERTIS? |
            | :--- | :--- | :--- |
            | **Oba účty u stejné banky** | Banka provede platbu interně ve svém systému. | ❌ Ne (zůstává v bance). |
            | **Účty u různých bank** | Banka plátce odešle pokyn do CERTIS v ČNB, která platbu vypořádá. | ✅ Ano (prochází přes CERTIS). |
            | **Okamžitá platba do jiné banky** | Převod proběhne v řádu sekund v režimu okamžitých plateb CERTIS. | ✅ Ano. |
            """)

        with st.container(border=True):
            st.markdown("### 1.3.5 Cesta platby kartou (Skládačka)")
            st.write("Při přiložení karty k terminálu proběhne v pozadí 5 rychlých kroků:")
            st.markdown("""
            1. Terminál načte platební údaje.
            2. Obchodník odešle požadavek přes karetní síť (Visa/Mastercard).
            3. Banka plátce ověří kartu, PIN/biometrii, limit a zůstatek.
            4. Platba se autorizuje (schválí) nebo zamítne.
            5. Později proběhne finanční zúčtování mezi bankami a obchodníkem.
            """)

        with st.container(border=True):
            st.markdown("### 🚨 1.3.6 Phishing escape room: Nenech se okrást")
            st.write("Zhodnoť následující bezpečnostní situace:")

            st.error("📩 Zpráva 1: 'Vaše karta byla zablokována. Klikněte ZDE na www.vasa-banka-sec.cz a ověřte účet.'")
            st.warning("📞 Zpráva 2: 'Volám z bezpečnostního oddělení banky. Pro záchranu peněz mi nadiktujte kód z SMS.'")

            ph_choice = st.radio("Správná reakce na tyto výzvy:", [
                "Kliknout na odkaz a zadat PIN pro odblokování",
                "Nadiktovat kód po telefonu, pokud pán zní důvěryhodně",
                "Ignorovat zprávy/zavěsit a situaci ověřit v oficiální aplikaci banky"
            ], key="k2_1_3_6_esc")

            if ph_choice == "Ignorovat zprávy/zavěsit a situaci ověřit v oficiální aplikaci banky":
                st.success("✅ Zachránil jsi své peníze! Banka nikdy neposílá přihlašovací odkazy v SMS a nikdy nepožaduje autorizační kódy po telefonu.")
            else:
                st.error("❌ Pozor! Toto je typický podvod (phishing/vishing). Útočník by získal přístup k tvému účtu.")

    # =========================================================================
    # 1.4 FINTECH REVOLUCE
    # =========================================================================
    elif selected_section_2 == "1.4 Fintech revoluce":
        st.markdown("<div class='sub-section-header'>1. BANKOVNÍ SYSTÉM A PENÍZE V 21. STOLETÍ</div><h2>1.4 Fintech revoluce</h2>", unsafe_allow_html=True)
        st.write("Fintech (Finance + Technology) označuje firmy a služby, které pomocí technologií mění způsob, jak platíme, spoříme, investujeme nebo spravujeme rozpočet.")

        with st.container(border=True):
            st.markdown("### 1.4.1 Co fintech přinesl")
            st.write("Online založení účtu, okamžité notifikace, investování od desítek korun, levnější směnu měn, virtuální karty, QR platby a automatické třídění výdajů.")

        with st.container(border=True):
            st.markdown("### 1.4.2 Neobanky a moderní finanční aplikace v ČR")
            st.markdown("""
            * **Revolut:** Mobilní aplikace pro víceměnový účet, směnu měn, cestování a investice.
            * **Wise:** Služba zaměřená na levné mezinárodní převody v reálných středových kurzech.
            * **mBank / Air Bank:** Banky opírající se o špičkové mobilní bankovnictví a digitální obsluhu.
            """)

            st.markdown("""
            | Klasické bankovnictví | Moderní fintech / neobanka |
            | :--- | :--- |
            | Důraz na pobočku a osobní kontakt. | Důraz na mobilní aplikaci a okamžité vyřízení. |
            | Vyřizování osobní návštěvou nebo přes web. | Vyřízení v telefonu během několika minut. |
            | Změny a funkce přibývají pomaleji. | Rychlé novinky, ale uživatel si musí více hlídat rizika. |
            """)

        with st.container(border=True):
            st.markdown("### 1.4.3 Open banking (Otevřené bankovnictví)")
            st.write("Open banking umožňuje klientovi bezpečně propojit účty z různých bank do jedné rozpočtové aplikace nebo účetnictví.")
            st.info("🔑 **Důležité:** Přístup k datům dává uživatel vždy vědomě a může ho kdykoliv odvolat.")

        with st.container(border=True):
            st.markdown("### 📱 1.4.5 Audit finanční aplikace")
            st.write("Proveď rychlý audit tvojí oblíbené finanční aplikace:")
            
            f_app = st.text_input("Zadej název aplikace (např. Revolut, Air Bank, Portu):", key="k2_1_4_audit_app")
            f_fee = st.selectbox("Jak tato aplikace primárně vydělává?", ["Poplatky z transakcí", "Měsíční předplatné", "Provize z doplňkových služeb", "Nevím"], key="k2_1_4_audit_fee")
            f_verdict = st.radio("Tvůj závěr:", ["Aplikace mi pomáhá lépe hospodařit s penězi", "Aplikace mě spíše tlačí k impulzivnímu utrácení"], key="k2_1_4_audit_verd")
            
            if st.button("Uložit hodnocení aplikace", key="k2_1_4_audit_btn"):
                st.success(f"Audit pro aplikaci **{f_app}** byl uložen. Znát poplatkový model a cíle finančních aplikací je klíčem k bezpečnému využívání fintechu.")

        with st.container(border=True):
            st.markdown("### ⚖️ Debata: Fintech — Pomocník, nebo past?")
            col_d1, col_d2 = st.columns(2)
            with col_d1:
                st.success("💚 **Tým A (Pomocník):**\n* Šetří čas a poplatky za směnu.\n* Umožňuje přehledné měsíční rozpočty.\n* Zpřístupňuje investování mladým.")
            with col_d2:
                st.error("🔴 **Tým B (Past):**\n* Podporuje impulzivní utrácení na 1 kliknutí.\n* Nabízí nebezpečně snadné půjčky (BNPL).\n* Riziko úniku osobních a finančních dat.")
