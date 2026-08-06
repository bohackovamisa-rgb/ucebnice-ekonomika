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
    if "1.1 Peníze jako digitální data" in selected_section_2:
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
    elif "1.2 ČNB" in selected_section_2:
        st.markdown("<div class='sub-section-header'>1. BANKOVNÍ SYSTÉM A PENÍZE V 21. STOLETÍ</div><h2>1.2 ČNB a komerční banky</h2>", unsafe_allow_html=True)
        st.write("Bankovní systém není jen síť poboček a bankomatů[cite: 2]. Je to jeden z nejdůležitějších „nervových systémů“ ekonomiky[cite: 2]. Přes banky tečou mzdy, platby za zboží, splátky úvěrů, daně, sociální dávky, investice i peníze firem[cite: 2]. Aby tento systém fungoval, musí mu lidé věřit[cite: 2].")

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
            """, unsafe_allow_html=True) #[cite: 2]

        # 1.2.1 Postavení ČNB v ČR
        with st.container(border=True):
            st.markdown("### 1.2.1 Postavení ČNB v České republice")
            st.write("Česká národní banka je centrální banka ČR[cite: 2]. Její činnost upravuje zejména zákon o České národní bance[cite: 2]. Je to veřejnoprávní instituce se zvláštním postavením: neusiluje o zisk jako běžný podnik a neposkytuje běžné bankovní služby občanům[cite: 2].")
            
            st.markdown("""
            <div class='box-gray'>
                ⚖️ <strong>Důležité (Nezávislost):</strong> ČNB je při plnění svých hlavních úkolů nezávislá. To znamená, že vláda jí nemá diktovat, jak má nastavovat úrokové sazby nebo měnovou politiku. Smyslem je chránit stabilitu měny a finančního systému před krátkodobým politickým tlakem.
            </div>
            """, unsafe_allow_html=True) #[cite: 2]

            with st.expander("🇪🇺 ČNB a euro: proč je česká situace jiná (Slovensko vs. ČR)"):
                st.write("To, že má ČR vlastní měnu (korunu) a vlastní centrální banku, která samostatně nastavuje měnovou politiku, není v EU u všech států běžné[cite: 2]. Mnoho členských zemí EU už přijalo euro a patří do eurozóny[cite: 2]. V těchto zemích nerozhoduje o hlavních úrokových sazbách jejich národní centrální banka samostatně, ale Evropská centrální banka (ECB)[cite: 2].")
                st.write("**Příklad Slovensko (2009):** Národní banka Slovenska dál existuje a dohlíží na trh, ale hlavní měnová politika a úrokové sazby se řeší na evropské úrovni přes ECB[cite: 2].")
                
                st.markdown("##### 🧮 Modelový příklad (CZK vs. EUR):")
                st.write("Představ si, že v Česku je inflace vyšší než v eurozóně a česká ekonomika potřebuje brzdit zdražování[cite: 2]. Pokud má ČR vlastní korunu, ČNB může zvýšit úrokové sazby výrazněji — například na 6–7 %[cite: 2]. Tím zdraží úvěry a hypotéky, ale podpoří spoření a pomůže tlumit inflaci[cite: 2]. Pokud by ČR platila eurem, ECB by se dívala na průměr eurozóny a sazby by mohly být jen 3–4 %[cite: 2].")
                
                euro_mode = st.radio("Zvol simulovaný měnový režim ČR při vysoké české inflaci:", [
                    "Vlastní korunová měna (ČNB zvýší sazby na 7 %)",
                    "Společné Euro (ECB drží sazby na 3,5 % pro celou eurozónu)"
                ], key="k2_1_2_1_euro_rad")
                
                if "Vlastní" in euro_mode:
                    st.success("✅ **Výsledek:** Vyšší sazby zdraží půjčky a hypotéky v ČR, ale účinněji tlumí inflaci a chrání kupní sílu obyvatel[cite: 2].")
                else:
                    st.warning("⚠️ **Výsledek:** Zůstávají levnější hypotéky, ale nižší sazby méně brzdí inflaci, pokud české ceny rostou rychleji než v eurozóně[cite: 2].")

        # 1.2.2 Hlavní cíl ČNB
        with st.container(border=True):
            st.markdown("### 1.2.2 Hlavní cíl ČNB: Cenová stabilita")
            st.write("Hlavním cílem ČNB je **péče o cenovou stabilitu**[cite: 2]. Neznamená to, že se nikdy nic nezdraží[cite: 2]. Znamená to, že růst cen má být dlouhodobě předvídatelný a zvládnutelný (tzv. inflační cílování)[cite: 2].")
            
            st.markdown("#### 🎮 Interaktivní simulace: Jsi bankovní rada ČNB")
            st.write("**Situace:** Inflace je vysoká, lidé si stěžují na zdražování, hypotéky jsou drahé a firmy říkají, že zákazníci méně utrácejí[cite: 2]. Tvoje skupina představuje Bankovní radu ČNB[cite: 2].")
            
            br_action = st.radio("Jako Bankovní rada ČNB rozhodněte o sazbách:", [
                "Zvýšíme úrokové sazby 📈",
                "Snížíme úrokové sazby 📉",
                "Ponecháme sazby beze změny ⚖️"
            ], key="k2_1_2_2_br_rad")
            
            br_txt = st.text_area("Napiš 1 větu tiskového prohlášení: „ČNB dnes rozhodla…“", key="k2_1_2_2_br_txt")
            
            if st.button("Vydat tiskové prohlášení", key="k2_1_2_2_br_btn"):
                if "Zvýšíme" in br_action:
                    st.success("✅ **Správný krok k tlumění inflace!** Úvěry zdraží, lidé budou méně utráce a více spořit, což pomůže zbrzdit zdražování[cite: 2]. Nevýhoda: Dražší hypotéky a zpomalení investic firem[cite: 2].")
                elif "Snížíme" in br_action:
                    st.error("❌ **Rizikové rozhodnutí!** Snížení sazeb zlevní úvěry, povzbudí utrácení a přileje olej do inflačního ohně[cite: 2].")
                else:
                    st.warning("⚠️ **Neutralita:** Vyčkáváte na další data. Pokud je ale inflace vysoká, nečinnost může prodloužit znehodnocování úspor[cite: 2].")

        # 1.2.3 Co přesně ČNB dělá
        with st.container(border=True):
            st.markdown("### 1.2.3 Co přesně ČNB dělá (8 hlavních funkcí)")
            st.markdown("""
            | Funkce ČNB | Co to znamená | Příklad dopadu na běžný život |
            | :--- | :--- | :--- |
            | **Měnová politika** | Nastavuje podmínky pro hodnotu peněz přes úrokové sazby. | Ovlivňuje úroky u hypoték, spoření i úvěrů. |
            | **Emise hotovosti** | Vydává bankovky a mince české koruny a pečuje o oběh. | Určuje vzhled, ochranné prvky a platnost peněz. |
            | **Dohled nad fin. trhem** | Dohlíží na banky, pojišťovny, záložny, penzijní a investiční firmy. | Hlídá, aby instituce dodržovaly pravidla a neohrožovaly klienty. |
            | **Finanční stabilita** | Sleduje rizika, která by mohla ohrozit celý finanční systém. | Nastavuje pravidla pro hypotéky (např. LTV, DTI). |
            | **Platební systémy** | Provozuje a dohlíží na mezibankovní zúčtování CERTIS. | Pomáhá tomu, aby převody mezi bankami fungovaly bezpečně. |
            | **Správa devizových rezerv**| Spravuje zásoby zahraničních měn a zlata. | Pomáhá stabilitě měny a důvěře v ekonomiku. |
            | **Banka státu** | Vede účty státu a poskytuje služby veřejnému sektoru. | Souvisí s výplatami dávek nebo příjmy z daní. |
            """) #[cite: 2]

        # 1.2.4 Ochranné prvky
        with st.container(border=True):
            st.markdown("### 1.2.4 Hotovost a ochranné prvky bankovek")
            st.write("ČNB odpovídá za českou měnu a hotovostní oběh[cite: 2]. Pokud by bylo snadné bankovky padělat, lidé i obchody by se báli hotovost přijímat[cite: 2]. Ochranné prvky chrání důvěru v peníze[cite: 2].")
            st.write("Ochranné prvky dělíme podle kontroly: **pohledem** (vodoznak, proužek), **hmatem** (reliéfní tisk), **naklopením** (proměnlivá barva) a **pomůckami** (UV světlo)[cite: 2].")
            
            st.markdown("##### 🔎 Prohlížeč ochranných prvků:")
            prvek_opt = st.selectbox("Zvol ochranný prvek k prozkoumání:", [
                "Vodoznak (pohledem proti světlu)",
                "Ochranný proužek s mikrotextem (pohledem proti světlu)",
                "Reliéfní tisk (hmatem)",
                "Opticky proměnlivá barva (naklopením bankovky)",
                "Soutisková značka (pohledem proti světlu)"
            ], key="k2_1_2_4_prvek")
            
            if "Vodoznak" in prvek_opt:
                st.info("💧 **Vodoznak:** Zřetelný portrét osobnosti viditelný v nepotištěném okraji při pohledu proti světlu[cite: 2].")
            elif "Ochranný proužek" in prvek_opt:
                st.info("📏 **Ochranný proužek:** Metalický proužek zapuštěný do papíru, při pohledu proti světlu tvoří tmavou čáru s mikrotextem nominální hodnoty[cite: 2].")
            elif "Reliéfní tisk" in prvek_opt:
                st.info("🖐️ **Reliéfní tisk:** Hmatatelně vystoupený povrch tiskového obrazce a čísla na lícové straně[cite: 2].")
            elif "Opticky proměnlivá barva" in prvek_opt:
                st.info("🎨 **Opticky proměnlivá barva:** Speciální tisk, který při naklonění mění odstín (např. ze zelené na zlatavou)[cite: 2].")
            else:
                st.info("🧩 **Soutisková značka:** Prvek tištěný z obou stran, který se proti světlu přesně doplní v celistvý symbol[cite: 2].")

        # 1.2.5 Vedení ČNB
        with st.container(border=True):
            st.markdown("### 1.2.5 Kdo ČNB řídí")
            st.write("Nejvyšším řídicím orgánem je **7členná Bankovní rada** (guvernér, 2 viceguvernéři, 4 členové)[cite: 2]. Členy jmenuje prezident republiky[cite: 2]. V čele stojí guvernér (v současnosti Aleš Michl)[cite: 2].")
            st.caption("🧭 Bankovní rada nerozhoduje o tom, komu banka dá osobní úvěr, ale rozhoduje o pravidlech pro celou ekonomiku[cite: 2].")

        # 1.2.6 Nástroje ČNB & REPO SAZBA (VYSVĚTLENÍ + KALKULAČKA)
        with st.container(border=True):
            st.markdown("### 1.2.6 Jak ČNB zasahuje do ekonomiky: Repo sazba v praxi")
            
            st.markdown("""
            <div class='box-blue'>
                💡 <strong>Co je to dvoutýdenní Repo sazba (lidsky)?</strong><br>
                ČNB neřídí ceny v obchodech příkazem[cite: 2]. Ovlivňuje je přes „cenu peněz“[cite: 2]. 
                <strong>2T repo sazba</strong> je úrok, za který si komerční banky mohou u ČNB bezpečně uložit svoje přebytečné peníze na 2 týdny[cite: 2].<br><br>
                • <strong>Když ČNB repo sazbu ZVÝŠÍ (např. z 3 % na 6 %):</strong> Komerční banky raději uloží peníze u ČNB[cite: 2]. Aby přilákaly peníze od lidí, zvednou úroky na spořicích účtech[cite: 2]. Zroveň ale zdraží půjčky a hypotéky (aby se jim vyplatilo půjčit člověku místo ČNB)[cite: 2]. Lidé si méně půjčují, méně utrácejí a inflace klesá[cite: 2].<br>
                • <strong>Když ČNB repo sazbu SNÍŽÍ:</strong> Půjčky a hypotéky zlevní, spoření vynáší méně, lidé a firmy více utrácejí a investují, což podporuje ekonomiku[cite: 2].
            </div>
            """, unsafe_allow_html=True)

            st.markdown("#### 🧮 Jasná kalkulačka: Jak Repo sazba mění spoření a úvěr")
            st.write("Vyber výši 2T repo sazby ČNB a podívej se, jak se orientačně změní roční úroky u **spoření (20 000 Kč)** a **půjčky (100 000 Kč)**[cite: 2]:")

            repo_choice = st.select_slider("Zvol výši Repo sazby ČNB:", options=[3.0, 5.0, 7.0], value=5.0, key="k2_1_2_6_repo_slider_new")

            # Výpočty: Spoření má typicky úrok nižší než repo sazba (př. Repo - 1.5%), Půjčka má úrok vyšší (př. Repo + 3.0%)
            vynos_20k = max(0, round(20000 * ((repo_choice - 1.5) / 100)))
            urok_100k = round(100000 * ((repo_choice + 3.0) / 100))

            col_rc1, col_cr2 = st.columns(2)
            with col_rc1:
                st.metric("Roční výnos ze spoření (20 000 Kč)", f"{vynos_20k:,.0f} Kč".replace(",", " "), delta=f"Sazba spoření cca {max(0, repo_choice-1.5):.1f} %")
            with col_cr2:
                st.metric("Roční úrok u půjčky (100 000 Kč)", f"{urok_100k:,.0f} Kč".replace(",", " "), delta=f"Sazba půjčky cca {repo_choice+3.0:.1f} %", delta_color="inverse")

            st.write(f"**Shrnutí při sazbě {repo_choice:.1f} %:** Při vyšší sazbě více vyděláš na spoření ({vynos_20k} Kč/rok), ale půjčka tě stojí podstatně více ({urok_100k} Kč/rok)[cite: 2].")

            st.divider()

            st.markdown("#### 🧮 Simulace: Vyšší sazby vs. Inflace a hypotéka")
            st.write("Porovnáme rodinu s hypotékou 3 000 000 Kč (na 25 let) a měsíčním nákupním košem 40 000 Kč (potraviny 15k, energie 8k, doprava 5k, telefon/net 3k, oblečení/volný čas 6k, rezerva 3k)[cite: 2]:")

            st.markdown("""
            | Modelový svět | Úrok hypotéky | Měsíční splátka | Inflace měsíčního koše | Celkový dopad na rozpočet |
            | :--- | :--- | :--- | :--- | :--- |
            | **Levné úvěry, vyšší inflace** | 2,5 % p.a. | **13 500 Kč** | Inflace 5 % → **+2 000 Kč/měs** | Splátka je nízká, ale běžné nákupy citelně zdražují. |
            | **Dražší úvěry, nižší inflace** | 5,0 % p.a. | **17 500 Kč** | Inflace 2 % → **+800 Kč/měs** | **Splátka stoupne o 4 000 Kč**, nákupy rostou pomaleji. |
            """) #[cite: 2]

            st.info("💡 **Proč lidé nadávají na vysoké sazby?** Splátka hypotéky je jedna konkrétní velká částka, která stoupne ihned a viditelně[cite: 2]. Přínos nižší inflace je rozptýlený do mnoha drobných nákupů v obchodě[cite: 2]. Vyšší sazby ale chrání celou ekonomiku a úspory před znehodnocením[cite: 2].")

        # 1.2.7 Třídicí hra
        with st.container(border=True):
            st.markdown("### 🧩 1.2.7 Třídicí hra: ČNB, nebo komerční banka?")
            st.write("Rozřaď činnosti podle toho, kdo je vykonává[cite: 2]:")

            t_ans1 = st.selectbox("1. Vydává české bankovky a mince:", ["Vyber...", "ČNB", "Komerční banka"], key="k2_1_2_7_t1")
            t_ans2 = st.selectbox("2. Vede běžný a spořicí účet občanům:", ["Vyber...", "ČNB", "Komerční banka"], key="k2_1_2_7_t2")
            t_ans3 = st.selectbox("3. Poskytuje hypotéku a spotřebitelský úvěr:", ["Vyber...", "ČNB", "Komerční banka"], key="k2_1_2_7_t3")
            t_ans4 = st.selectbox("4. Nastavuje základní 2T repo sazbu:", ["Vyber...", "ČNB", "Komerční banka"], key="k2_1_2_7_t4")
            t_ans5 = st.selectbox("5. Dohlíží na stabilitu finančního trhu:", ["Vyber...", "ČNB", "Komerční banka"], key="k2_1_2_7_t5")
            
            if st.button("Vyhodnotit třídicí hru", key="k2_1_2_7_btn"):
                if t_ans1 == "ČNB" and t_ans2 == "Komerční banka" and t_ans3 == "Komerční banka" and t_ans4 == "ČNB" and t_ans5 == "ČNB":
                    st.success("🎉 Skvěle! Perfektně rozlišuješ roli centrální a komerční banky[cite: 2].")
                else:
                    st.error("Některé odpovědi nejsou správně. Zkuste to znovu! (Nápověda: Běžné účty a hypotéky řeší komerční banky, sazby a dohled ČNB)[cite: 2].")

        # 1.2.8 až 1.2.10 Komerční banky (Občané a Firmy)
        with st.container(border=True):
            st.markdown("### 1.2.8 – 1.2.10 Komerční banky: Služby pro občany a firmy")
            st.write("Komerční banky jsou obchodní firmy podnikající na finančním trhu[cite: 2]. Přijímají vklady, poskytují úvěry a zprostředkovávají platby[cite: 2]. Potřebují bankovní licenci a podléhají dohledu ČNB[cite: 2].")

            col_kb1, col_kb2 = st.columns(2)
            with col_kb1:
                st.markdown("##### 👤 Co banky poskytují občanům:")
                st.markdown("""
                * Běžné a spořicí účty, termínované vklady[cite: 2]
                * Platební karty, internetové a mobilní bankovnictví[cite: 2]
                * Spotřebitelské úvěry, kontokorenty, kreditní karty, hypotéky[cite: 2]
                * Směnu měn, zprostředkování investic a pojištění[cite: 2]
                * Bezpečnostní nástroje (3D Secure, limity)[cite: 2]
                """)
            with col_kb2:
                st.markdown("##### 🏢 Co banky poskytují firmám:")
                st.markdown("""
                * Podnikatelské účty a platební terminály[cite: 2]
                * Provozní a investiční úvěry, kontokorenty[cite: 2]
                * Bankovní záruky, dokumentární platby v int. obchodě[cite: 2]
                * Správu likvidity a směnárenské/devizové služby[cite: 2]
                * Financování exportu a firemní karty[cite: 2]
                """)

        # 1.2.11 Aktivní, pasivní a neutrální operace
        with st.container(border=True):
            st.markdown("### 1.2.11 Aktivní, pasivní a neutrální operace bank")
            st.write("Činnosti komerčních bank se dělí podle toho, zda zdroje získávají, půjčují nebo poskytují služby[cite: 2]:")

            st.markdown("""
            | Typ operace | Co znamená pro banku | Příklady |
            | :--- | :--- | :--- |
            | **Pasivní operace** | Banka získává zdroje. Z pohledu banky jde o **závazky** (vklady dluží klientům)[cite: 2]. | Běžné a spořicí účty, termínované vklady, bankovní dluhopisy, přijaté úvěry[cite: 2]. |
            | **Aktivní operace** | Banka peníze umísťuje tak, aby vydělávala. Z pohledu banky jde o **aktiva** (pohledávky)[cite: 2]. | Spotřebitelské úvěry, hypotéky, kontokorenty, kreditní karty, podnikatelské úvěry[cite: 2]. |
            | **Neutrální operace** | Banka poskytuje služby a vydělává na **poplatcích a provizích** (nepůjčuje vlastní peníze)[cite: 2]. | Zpracování plateb, vedení účtu, směna měn, zprostředkování investic/pojištění, úschova[cite: 2]. |
            """) #[cite: 2]

            st.markdown("#### 🧩 Rozhodovací karty bankovních operací")
            st.write("Urči typ operace z pohledu banky u následujících situací[cite: 2]:")

            op_1 = st.selectbox("1. Student vkládá 5 000 Kč na spořicí účet:", ["Vyber...", "Pasivní operace", "Aktivní operace", "Neutrální operace"], key="k2_op1")
            op_2 = st.selectbox("2. Banka poskytne rodině hypotéku na dům:", ["Vyber...", "Pasivní operace", "Aktivní operace", "Neutrální operace"], key="k2_op2")
            op_3 = st.selectbox("3. Klient si v bance smění koruny za eura na dovolenou:", ["Vyber...", "Pasivní operace", "Aktivní operace", "Neutrální operace"], key="k2_op3")

            if st.button("Vyhodnotit operace", key="k2_op_btn"):
                if op_1 == "Pasivní operace" and op_2 == "Aktivní operace" and op_3 == "Neutrální operace":
                    st.success("🎉 Výborně! Vklad je závazek (Pasivní), úvěr je pohledávka (Aktivní) a směna je služba za poplatek (Neutrální)[cite: 2].")
                else:
                    st.error("Některá odpověď je špatně. Zkus to znovu[cite: 2]!")

        # 1.2.12 & 1.2.13 Jak banka vydělává, rizika a dohled ČNB
        with st.container(border=True):
            st.markdown("### 1.2.12 & 1.2.13 Jak banka vydělává, její rizika a dohled ČNB")
            
            st.markdown("##### 💵 Na čem banka vydělává:")
            st.markdown("""
            * **Úroková marže:** Rozdíl mezi úrokem, který banka platí vkladatelům (např. 3 % na spoření), a úrokem, za který půjčuje (např. 6 % u hypotéky)[cite: 2].
            * **Poplatky a provize:** Za vedení účtu, zahraniční platby, terminály, zprostředkování pojištění či investic[cite: 2].
            * **Investiční a devizové operace:** Obchodování na finančních a měnových trzích[cite: 2].
            """) #[cite: 2]

            st.markdown("##### ⚠️ Jaká rizika banka nese:")
            st.markdown("""
            * **Úvěrové riziko:** Klient přestane splácet svůj úvěr[cite: 2].
            * **Likviditní riziko:** Banka nemá v daný okamžik dostatek hotovosti pro denní výběry klientů[cite: 2].
            * **Úrokové riziko:** Změna úrokových sazeb na trhu nepříznivě ovlivní výnosy banky[cite: 2].
            * **Měnové riziko:** Změny kurzů cizích měn ovlivní hodnotu obchodů[cite: 2].
            * **Operační a Kybernetické riziko:** Selhání IT systémů, lidská chyba nebo hackreský útok[cite: 2].
            """) #[cite: 2]

            st.markdown("##### 🏛️ Dohled ČNB a bankovní licence:")
            st.write("Banka nemůže půjčit 100 % všech vkladů[cite: 2]. Musí plnit **kapitálovou přiměřenost** (držet rezervní kapitál na ztráty) a limity likvidity[cite: 2]. ČNB kontroluje plnění pravidel a může udělovat sankce či odebrat licencí[cite: 2].")

            st.markdown("#### 🛠️ Mini audit bankovního analytika")
            st.write("Jsi analytik ČNB a hodnotíš zdraví komerční banky. Zaškrtni 3 správné podmínky bezpečné banky[cite: 2]:")
            
            chk_a1 = st.checkbox("Banka půjčuje jen klientům s ověřenou schopností splácet.", key="k2_audit_1")
            chk_a2 = st.checkbox("Banka půjčí úplně všechny vklady na 30leté hypotéky, aby měla maximální zisk.", key="k2_audit_2")
            chk_a3 = st.checkbox("Banka drží dostatek kapitálu jako bezpečnostní polštář pro krytí ztrát.", key="k2_audit_3")
            chk_a4 = st.checkbox("Banka udržuje dostatečnou likviditu pro denní výběry a platby klientů.", key="k2_audit_4")

            if st.button("Vyhodnotit audit", key="k2_audit_btn"):
                if chk_a1 and chk_a3 and chk_a4 and not chk_a2:
                    st.success("✅ Excelentní audit! Banka musí držet rezervy i kapitál a řídit úvěrové riziko[cite: 2].")
                else:
                    st.error("Chyba v auditu! Banka nikdy nesmí rozpůjčovat 100 % vkladů bez rezerv na výběry[cite: 2].")

        # 1.2.14 Vklady a jejich ochrana
        with st.container(border=True):
            st.markdown("### 1.2.14 Vklady, pojištění a limity výběru hotovosti")
            st.write("Vklady u bank v ČR jsou ze zákona pojištěny do výše **100 000 EUR** (přibližně 2,4–2,5 milionu Kč) na jednoho klienta u jedné banky[cite: 2]. Pojištění zajišťuje Garanční systém finančního trhu (Fond pojištění vkladů)[cite: 2].")

            st.markdown("""
            | Situace vkladu u 1 banky | Jak funguje pojištění vkladů |
            | :--- | :--- |
            | **Klient má v bance 500 000 Kč** | Celá částka je 100% pojištěna pod zákonným limitem[cite: 2]. |
            | **Klient má v bance 2 000 000 Kč** | Celá částka je pod limitem 100 000 EUR a je pojištěna[cite: 2]. |
            | **Klient má v bance 4 000 000 Kč** | Pojištěna je jen část do cca 2,5 mil. Kč; zbývající část nese riziko[cite: 2]. |
            | **Klient má 2 mil. v Bance A a 2 mil. v Bance B** | Pojištěny jsou obě částky plně (limit platí pro každou banku zvlášť)[cite: 2]. |
            """) #[cite: 2]

            st.markdown("##### 💵 Výběry hotovosti na pobočce (Proč nelze vybrat miliony ihned?):")
            st.markdown("""
            * **Pobočka nemá neomezený trezor:** Z bezpečnostních důvodů nedrží pobočky miliony v hotovosti na přepážce[cite: 2].
            * **AML pravidla (proti praní špinavých peněz):** Banka musí prověřovat neobvyklé transakce a původ peněz[cite: 2].
            * **Hranice pro objednání:** Hranice pro hlášení se liší. Například KB uvádí hlášení u výběrů nad 100 000 Kč, zatímco ČSOB má hranice pro objednání až nad 300 000 Kč[cite: 2]. Výběr např. 600 000 Kč na auto je nutné objednat 1–2 dny předem u všech bank[cite: 2].
            """) #[cite: 2]

    # =========================================================================
    # 1.3 PLATEBNÍ STYK
    # =========================================================================
    elif "1.3 Platební styk" in selected_section_2:
        st.markdown("<div class='sub-section-header'>1. BANKOVNÍ SYSTÉM A PENÍZE V 21. STOLETÍ</div><h2>1.3 Platební styk</h2>", unsafe_allow_html=True)
        st.write("Platební styk znamená převod peněz mezi plátcem a příjemcem[cite: 2]. Je to infrastruktura důvěry, která umožňuje bezpečný přesun financí[cite: 2].")

        with st.container(border=True):
            st.markdown("### 1.3.2 Druhy platebního styku")
            st.markdown("""
            | Druh | Co znamená | Příklady |
            | :--- | :--- | :--- |
            | **Hotovostní** | Platí se fyzickými bankovkami a mincemi[cite: 2]. | Nákup v obchodě za papírové peníze, výběr z bankomatu[cite: 2]. |
            | **Bezhotovostní** | Peníze se převádějí jako účetní záznamy mezi účty[cite: 2]. | Platba kartou, bankovní převod, QR platba, Apple Pay[cite: 2]. |
            | **Tuzemský** | Platba probíhá v rámci České republiky v CZK[cite: 2]. | Převod mezi českými bankami přes CERTIS[cite: 2]. |
            | **Zahraniční** | Platba směřuje do jiné země nebo v cizí měně[cite: 2]. | SEPA platba v eurech, mezinárodní převod SWIFT[cite: 2]. |
            | **Jednorázový vs. Opakovaný** | Jednorázová úhrada vs. pravidelný automatický převod[cite: 2]. | Úhrada faktury vs. trvalý příkaz, inkaso, SIPO, předplatné[cite: 2]. |
            """) #[cite: 2]

            st.markdown("##### 🧭 Urči správný typ platby:")
            scen_p = st.selectbox("Vyber platbu:", [
                "1. Posílám nájem trvalým příkazem majiteli v ČR",
                "2. Kupuji kávu za papírovou stovku",
                "3. Kupuji hry na německém e-shopu v EUR"
            ], key="k2_1_3_2_scen")

            if "1." in scen_p:
                st.info("👉 **Bezhotovostní, tuzemská, opakovaná platba**[cite: 2].")
            elif "2." in scen_p:
                st.info("👉 **Hotovostní, tuzemská, jednorázová platba**[cite: 2].")
            else:
                st.info("👉 **Bezhotovostní, zahraniční, jednorázová platba**[cite: 2].")

        with st.container(border=True):
            st.markdown("### 1.3.4 CERTIS: Zúčtovací dálnice ČNB")
            st.write("**CERTIS** (Czech Express Real Time Interbank Gross Settlement System) je systém mezibankovního platebního styku v ČR spravovaný ČNB[cite: 2].")

            st.markdown("""
            | Situace platby | Jak proběhne zúčtování | Jde přes CERTIS? |
            | :--- | :--- | :--- |
            | **Platba ve stejné bance** | Banka si platbu upraví ve svém interním systému[cite: 2]. | ❌ Ne (zůstává uvnitř banky)[cite: 2]. |
            | **Platba do jiné banky** | Banka odešle pokyn do CERTIS v ČNB, která ho vypořádá s druhou bankou[cite: 2]. | ✅ Ano (prochází přes CERTIS)[cite: 2]. |
            | **Okamžitá platba do jiné banky** | Převod proběhne v řádu sekund přes systém okamžitých plateb CERTIS[cite: 2]. | ✅ Ano[cite: 2]. |
            """) #[cite: 2]

        with st.container(border=True):
            st.markdown("### 1.3.5 Jak probíhá platba kartou (Skládačka)")
            st.write("Seřaď kroky platby kartou nebo mobilem v terminálu do správného pořadí[cite: 2]:")

            krok1 = st.selectbox("1. krok:", ["Vyber...", "Přiložení karty/mobilu k terminálu", "Terminál odešle požadavek přes karetní síť", "Banka plátce ověří zůstatek a PIN", "Schválení/Zamítnutí platby"], key="k2_k1")
            krok2 = st.selectbox("2. krok:", ["Vyber...", "Přiložení karty/mobilu k terminálu", "Terminál odešle požadavek přes karetní síť", "Banka plátce ověří zůstatek a PIN", "Schválení/Zamítnutí platby"], key="k2_k2")

            if st.button("Zkontrolovat pořadí", key="k2_card_btn"):
                if krok1 == "Přiložení karty/mobilu k terminálu" and krok2 == "Terminál odešle požadavek přes karetní síť":
                    st.success("✅ Správný začátek! Následuje ověření bankou a schválení transakce[cite: 2].")
                else:
                    st.error("Chyba v pořadí. První je přiložení karty, druhý odeslání požadavku přes síť[cite: 2].")

        with st.container(border=True):
            st.markdown("### 🚨 1.3.6 Phishing escape room: Nenech se okrást")
            st.write("Posouzení podvodných zpráv[cite: 2]:")

            st.error("📩 Zpráva 1: „Vaše karta byla zablokována. Pro odblokování se přihlaste na www.vasa-banka-sec.com“[cite: 2]")
            st.warning("📞 Telefonát: „Volám z bezpečnostního oddělení banky. Nadiktujte mi kód z SMS pro záchranu účtu.“[cite: 2]")

            ph_ans = st.radio("Správná reakce na tyto situace:", [
                "Kliknout na odkaz a zadat PIN",
                "Nadiktovat kód z SMS pánovi po telefonu",
                "Zavěsit / zprávu ignorovat a kontaktovat banku přes oficiální aplikaci"
            ], key="k2_ph_ans")

            if ph_ans == "Zavěsit / zprávu ignorovat a kontaktovat banku přes oficiální aplikaci":
                st.success("✅ Zachránil jsi peníze! Banka nikdy neposílá odkazy na přihlášení v SMS a nikdy nechce PIN/kódy po telefonu[cite: 2].")
            else:
                st.error("❌ Stala se chyba! Toto byl phishing/vishing. Útočník by získal plný přístup k účtu[cite: 2].")

    # =========================================================================
    # 1.4 FINTECH REVOLUCE
    # =========================================================================
    elif "1.4 Fintech" in selected_section_2:
        st.markdown("<div class='sub-section-header'>1. BANKOVNÍ SYSTÉM A PENÍZE V 21. STOLETÍ</div><h2>1.4 Fintech revoluce</h2>", unsafe_allow_html=True)
        st.write("Fintech (Finance + Technology) označuje moderní služby, které pomocí technologií mění způsob placení, spoření a správy rozpočtu[cite: 2].")

        with st.container(border=True):
            st.markdown("### 1.4.2 Neobanky a moderní finanční aplikace v ČR")
            st.markdown("""
            * **Revolut:** Mobilní finanční aplikace pro víceměnový účet, levnou směnu měn, platby v zahraničí a investice[cite: 2].
            * **Wise:** Služba zaměřená na mezinárodní převody v reálných středových kurzech[cite: 2].
            * **mBank / Air Bank:** Banky s českou licencí opírající se o špičkové mobilní bankovnictví[cite: 2].
            """) #[cite: 2]

            st.markdown("""
            | Klasické bankovnictví | Moderní fintech / Neobanka |
            | :--- | :--- |
            | Důraz na pobočku a osobní kontakt[cite: 2]. | Důraz na mobilní aplikaci a rychlé ovládání[cite: 2]. |
            | Vyřizování osobně nebo přes internetbanking[cite: 2]. | Vyřízení v telefonu během několika minut[cite: 2]. |
            | Poplatky a kurzy nemusely být přehledné[cite: 2]. | Zobrazení poplatků a kurzů okamžitě v aplikaci[cite: 2]. |
            """) #[cite: 2]

        with st.container(border=True):
            st.markdown("### 📱 1.4.5 Audit finanční aplikace")
            st.write("Zhodnoť svou oblíbenou finanční aplikaci[cite: 2]:")

            a_name = st.text_input("Zadej název aplikace (např. Revolut, Air Bank, Portu):", key="k2_a_name")
            a_model = st.selectbox("Jak tato aplikace primárně vydělává?", ["Poplatky z transakcí", "Měsíční předplatné", "Provize z doplňkových služeb", "Nevím"], key="k2_a_model")
            a_res = st.radio("Tvůj závěr:", ["Pomáhá mi lépe hospodařit", "Spíše mě tlačí k impulzivnímu utrácení"], key="k2_a_res")

            if st.button("Uložit audit", key="k2_audit_save"):
                st.success(f"Audit aplikace **{a_name}** uložen[cite: 2]! Znalost poplatkového modelu je základem finanční gramotnosti[cite: 2].")

        with st.container(border=True):
            st.markdown("### ⚖️ Debata: Fintech — Pomocník, nebo past?")
            col_fin1, col_fin2 = st.columns(2)
            with col_fin1:
                st.success("💚 **Tým A (Pomocník):**\n* Šetří čas a poplatky za směnu[cite: 2].\n* Přehledné automatické rozpočty[cite: 2].\n* Zpřístupňuje investice malých částek[cite: 2].")
            with col_fin2:
                st.error("🔴 **Tým B (Past):**\n* Podporuje impulzivní utrácení na 1 klik[cite: 2].\n* Rychlé nebezpečné půjčky (BNPL)[cite: 2].\n* Riziko sdílení dat s neověřenými službami[cite: 2].")
