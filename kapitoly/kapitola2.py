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
                • <strong>Česká národní banka (ČNB):</strong> Centrální banka České republiky[cite: 2]. Nejde o běžnou banku pro občany[cite: 2]. Je to instituce, která hlídá stabilitu měny, finančního systému a pravidla pro banky[cite: 2].<br>
                • <strong>Komerční banky:</strong> Banky, se kterými běžně pracují lidé, firmy a obce[cite: 2]. Vedou účty, přijímají vklady, poskytují úvěry, vydávají platební karty a zajišťují platby[cite: 2].
            </div>
            <div class='box-purple'>
                🧠 <strong>Pointa pro běžný život:</strong> Když platíš kartou, bereš si hypotéku, dostáváš výplatu na účet nebo sleduješ inflaci, nepřímo se setkáváš s rozhodnutími centrální banky i se službami komerčních bank[cite: 2].
            </div>
            """, unsafe_allow_html=True)

        # 1.2.1
        with st.container(border=True):
            st.markdown("### 1.2.1 Postavení ČNB v České republice")
            st.write("Česká národní banka je centrální banka České republiky[cite: 2]. Její postavení je zakotveno v právním řádu ČR a její činnost upravuje zejména zákon o České národní bance[cite: 2]. ČNB je veřejnoprávní instituce se zvláštním postavením: není komerční firmou, neusiluje o zisk jako běžný podnik a neposkytuje běžné bankovní služby občanům[cite: 2].")
            
            st.markdown("""
            <div class='box-gray'>
                ⚖️ <strong>Důležité:</strong> ČNB je při plnění svých hlavních úkolů nezávislá[cite: 2]. To znamená, že vláda jí nemá diktovat, jak má nastavovat úrokové sazby nebo měnovou politiku[cite: 2]. Smyslem nezávislosti je chránit stabilitu měny a finančního systému před krátkodobým politickým tlakem[cite: 2].
            </div>
            """, unsafe_allow_html=True)

            st.write("ČNB sídlí v Praze a působí pro celou Českou republiku[cite: 2]. Je součástí Evropského systému centrálních bank, protože Česká republika je členem Evropské unie[cite: 2]. Dokud ale ČR nepřijme euro, ČNB provádí vlastní měnovou politiku pro českou korunu[cite: 2].")

            with st.expander("🇪🇺 ČNB a euro: proč je česká situace trochu jiná"):
                st.write("To, že má Česká republika vlastní měnu (korunu) a vlastní centrální banku, která samostatně nastavuje měnovou politiku, není v Evropské unii u všech států běžné[cite: 2]. Mnoho členských zemí EU už přijalo euro a patří do eurozóny[cite: 2]. V těchto zemích nerozhoduje o hlavních úrokových sazbách jejich národní centrální banka samostatně, ale společně systém vedený Evropskou centrální bankou (ECB)[cite: 2].")
                st.write("**Příklad:** Slovensko přijalo euro v roce 2009[cite: 2]. Národní banka Slovenska dál existuje, ale už nevydává vlastní slovenskou korunu a samostatně neurčuje měnovou politiku pro vlastní měnu[cite: 2]. Podílí se na fungování eurozóny, dohledu a finanční stabilitě, ale hlavní měnová politika se řeší na evropské úrovni přes ECB[cite: 2].")
                st.write("**Jak by to fungovalo po přijetí eura v ČR:** Česká koruna by byla nahrazena eurem[cite: 2]. ČNB by nezanikla, ale změnila by se její role[cite: 2]. Dál by působila jako národní centrální banka, dohlížela by na finanční trh, pečovala o hotovostní oběh eura v ČR, podílela se na finanční stabilitě a byla by součástí Eurosystému[cite: 2]. O hlavních úrokových sazbách pro eurozónu by se ale rozhodovalo společně v rámci ECB, nikoli samostatně jen podle české ekonomiky[cite: 2].")
                
                st.markdown("##### 🧮 Konkrétní modelový příklad rozdílu:")
                st.write("Představ si, že v Česku je inflace vyšší než v eurozóně a česká ekonomika potřebuje brzdit zdražování[cite: 2]. Pokud má ČR vlastní korunu, může ČNB zvýšit úrokové sazby výrazněji — například na 6–7 %[cite: 2]. Tím zdraží úvěry, hypotéky i půjčky, ale zároveň podpoří spoření a může pomoci tlumit inflaci[cite: 2]. Pokud by ČR už platila eurem, sazby by se nastavovaly pro celou eurozónu[cite: 2]. ECB by se dívala na průměrnou situaci mnoha zemí, například Německa, Francie, Itálie, Slovenska nebo Španělska[cite: 2]. Kdyby eurozóna jako celek potřebovala mírnější politiku, mohly by být sazby třeba jen 3–4 %, i když by Česku samostatně vyhovovaly vyšší sazby[cite: 2].")
                
                euro_sim = st.radio("Zvol režim pro modelovou situaci vysoké české inflace:", [
                    "Vlastní měna (CZK) — ČNB zvýší sazby na 7 %",
                    "Přijaté Euro (EUR) — ECB drží sazby na 3,5 %"
                ], key="k2_1_2_1_euro_sim")
                
                if "CZK" in euro_sim:
                    st.success("✅ **Samostatná ČNB:** Dražší úvěry a hypotéky v ČR tlumí poptávku a pomáhají rychleji srazit českou inflaci[cite: 2].")
                else:
                    st.warning("⚠️ **Společné Euro (ECB):** Úvěry zůstávají relativně levnější, což je výhodné pro dlužníky, ale inflace v ČR může trvat déle[cite: 2].")

        # 1.2.2
        with st.container(border=True):
            st.markdown("### 1.2.2 Hlavní cíl ČNB")
            st.write("Hlavním cílem ČNB je **péče o cenovou stabilitu**[cite: 2]. Jinými slovy: ČNB se snaží, aby peníze neztrácely hodnotu příliš rychle a aby inflace nebyla dlouhodobě příliš vysoká ani nebezpečně nízká[cite: 2].")
            
            st.markdown("""
            <div class='box-gray'>
                🎯 <strong>Cenová stabilita jednoduše:</strong> Neznamená, že se nikdy nic nezdraží[cite: 2]. Znamená, že růst cen má být dlouhodobě předvídatelný a zvládnutelný[cite: 2]. Když je inflace příliš vysoká, lidem klesá kupní síla, firmám se hůř plánuje a ekonomika ztrácí stabilitu[cite: 2].
            </div>
            """, unsafe_allow_html=True)
            st.write("ČNB v praxi používá inflační cílování[cite: 2]. To znamená, že sleduje vývoj inflace a nastavuje nástroje měnové politiky tak, aby se inflace ve střednědobém horizontu pohybovala kolem stanoveného cíle (2 %)[cite: 2].")

            st.markdown("#### 🎮 Interaktivní simulace: Jsi bankovní rada ČNB")
            st.write("**Situace:** Inflace je vysoká, lidé si stěžují na zdražování, hypotéky jsou drahé a firmy říkají, že zákazníci méně utrácejí[cite: 2]. Tvoje skupina představuje bankovní rada ČNB[cite: 2].")
            
            c_rada_action = st.radio("Rozhodněte o sazbách:", [
                "Zvýšíme úrokové sazby 📈",
                "Snížíme úrokové sazby 📉",
                "Ponecháme sazby beze změny ⚖️"
            ], key="k2_1_2_2_rada_act")

            st.write("**Odpovězte na kontrolní otázky tiskové konference:**")
            q_uvery = st.text_input("1. Co se stane s úvěry a hypotékami?", key="k2_q_uvery")
            q_sporeni = st.text_input("2. Co se stane se spořením?", key="k2_q_sporeni")
            q_inflace = st.text_input("3. Jaký bude dopad na inflaci?", key="k2_q_inflace")
            
            if st.button("Vyhlásit rozhodnutí (1 minuta tiskové konference)", key="k2_1_2_2_rada_btn"):
                st.markdown(f"**Tiskové prohlášení Bankovní rady:** „ČNB dnes rozhodla, že {c_rada_action.lower()}...“")
                if "Zvýšíme" in c_rada_action:
                    st.success("✅ **Správná reakce na vysokou inflaci!** Zdražení úvěrů motivuje k šetření a brzdí zdražování[cite: 2]. Pomáhá střadatelům, komplikuje život žadatelům o hypotéky[cite: 2].")
                elif "Snížíme" in c_rada_action:
                    st.error("❌ **Varování!** Snížením sazeb zlevníte půjčky, což ještě více podpoří utrácení a zrychlí inflaci[cite: 2].")
                else:
                    st.warning("⚠️ **Neutralita:** Ponechání sazeb vyčkává na další data, ale inflace může dál znehodnocovat úspory[cite: 2].")

        # 1.2.3
        with st.container(border=True):
            st.markdown("### 1.2.3 Co přesně ČNB dělá")
            st.write("ČNB má několik klíčových funkčních oblastí[cite: 2]. Každá z nich se týká jiné části ekonomiky, ale dohromady tvoří systém důvěry v peníze[cite: 2].")

            st.markdown("""
            | Funkce ČNB | Co to znamená | Příklad dopadu na běžný život |
            | :--- | :--- | :--- |
            | **Měnová politika** | Nastavuje podmínky pro hodnotu peněz, hlavně pomocí úrokových sazeb[cite: 2]. | Ovlivňuje úroky u hypoték, spoření i úvěrů[cite: 2]. |
            | **Emise hotovosti** | Vydává bankovky a mince české koruny a pečuje o jejich oběh[cite: 2]. | Určuje, jaké bankovky a mince platí a jak vypadají[cite: 2]. |
            | **Dohled nad finančním trhem** | Dohlíží na banky, pojišťovny, družstevní záložny, penzijní společnosti, investiční společnosti a další finanční instituce[cite: 2]. | Hlídá, aby instituce dodržovaly pravidla a neohrožovaly klienty ani systém[cite: 2]. |
            | **Finanční stabilita** | Sleduje rizika, která by mohla ohrozit celý finanční systém[cite: 2]. | Řeší například, zda banky mají dost kapitálu a nejsou příliš rizikové[cite: 2]. |
            | **Platební systémy** | Provozuje a dohlíží na důležité platební a zúčtovací systémy[cite: 2]. | Pomáhá tomu, aby převody mezi bankami fungovaly bezpečně a spolehlivě[cite: 2]. |
            | **Správa devizových rezerv** | Spravuje zásoby zahraničních měn a dalších aktiv státu[cite: 2]. | Pomáhá stabilitě měny a důvěře v ekonomiku[cite: 2]. |
            | **Banka státu** | Vede účty státu a poskytuje vybrané služby veřejnému sektoru[cite: 2]. | Souvisí s pohybem peněz státu, například při placení výdajů veřejných institucí[cite: 2]. |
            """) #[cite: 2]

        # 1.2.4
        with st.container(border=True):
            st.markdown("### 1.2.4 Hotovost, ochranné prvky bankovek a důvěra v peníze")
            st.write("Jednou z viditelných činností ČNB je péče o hotovostní oběh[cite: 2]. ČNB vydává české bankovky a mince, stahuje z oběhu poškozené nebo neplatné peníze a stará se o to, aby hotovost byla důvěryhodná[cite: 2]. Právě sem patří také ochranné prvky bankovek[cite: 2].")
            st.write("Bankovky mají ochranné prvky proto, aby bylo možné ověřit jejich pravost a snížit riziko padělání[cite: 2]. Nejde jen o „ozdobu“ bankovky[cite: 2]. Ochranné prvky pomáhají běžným lidem, obchodníkům, bankám i státu poznat, zda je bankovka skutečná a zda jí mohou důvěřovat[cite: 2].")

            st.markdown("""
            <div class='box-gray'>
                🛡️ <strong>Proč ochranné prvky patří k tématu ČNB?</strong><br>
                ČNB odpovídá za českou měnu a hotovostní oběh[cite: 2]. Pokud by bylo snadné bankovky padělat, lidé i obchody by se báli hotovost přijímat[cite: 2]. Ochranné prvky proto chrání důvěru v peníze, ztěžují padělání a umožňují rychlou kontrolu pravosti při běžném placení[cite: 2].
            </div>
            """, unsafe_allow_html=True)

            st.write("Ochranné prvky můžeme rozdělit podle toho, jak je člověk kontroluje[cite: 2]:")
            st.markdown("""
            * **pohledem** — například vodoznak, ochranný proužek, soutisková značka nebo proměnlivá barva[cite: 2],
            * **hmatem** — například speciální papír a reliéfní tisk[cite: 2],
            * **naklopením bankovky** — například opticky proměnlivé prvky[cite: 2],
            * **pomůckami** — například kontrola pod UV světlem[cite: 2].
            """)

            st.markdown("##### 🔎 Interaktivní aktivita: Ochranné prvky peněz")
            st.write("Prohlédni si níže jednotlivé kategorie ochranných prvků české bankovky[cite: 2]:")
            
            p_sel = st.selectbox("Vyber ochranný prvek pro detailní popis:", [
                "1. Vodoznak (pohledem proti světlu)",
                "2. Ochranný proužek s mikrotextem (pohledem)",
                "3. Reliéfní tisk (hmatem)",
                "4. Opticky proměnlivá barva (naklopením)",
                "5. Soutisková značka (pohledem)",
                "6. UV prvek (pomůckou)"
            ], key="k2_1_2_4_bankovka_sel")

            if "1." in p_sel:
                st.info("💧 **Vodoznak:** Zřetelný portrét osobnosti zobrazené na bankovce, který je viditelný z obou stran při pohledu proti světlu v nepotištěném okraji[cite: 2].")
            elif "2." in p_sel:
                st.info("📏 **Ochranný proužek:** Metalický proužek zapuštěný do papíru[cite: 2]. Při pohledu proti světlu je vidět jako tmavý souvislý pás s negativním mikrotextem označujícím nominální hodnotu[cite: 2].")
            elif "3." in p_sel:
                st.info("🖐️ **Reliéfní tisk:** Hmatatelný hlubotisk na portrétu, číselném označení hodnoty a státním znaku na lícové straně[cite: 2].")
            elif "4." in p_sel:
                st.info("🎨 **Opticky proměnlivá barva:** Tisk speciální barvou, která při naklonění bankovky mění svůj odstín (např. ze zelené na zlatavou)[cite: 2].")
            elif "5." in p_sel:
                st.info("🧩 **Soutisková značka:** Prvek tištěný částečně z lícové a částečně z rubové strany[cite: 2]. Proti světlu se obě části přesně doplňují v celistvý symbol (např. značku ČNB)[cite: 2].")
            else:
                st.info("🔦 **UV prvky:** Vlákna a tiskové motivy, které se rozsvítí pouze pod ultrafialovým světlem u pokladen a v bankách[cite: 2].")

        # 1.2.5
        with st.container(border=True):
            st.markdown("### 1.2.5 Kdo ČNB řídí")
            st.write("Nejvyšším řídicím orgánem ČNB je **bankovní rada**[cite: 2]. Ta rozhoduje například o měnové politice, úrokových sazbách a dalších zásadních otázkách fungování ČNB[cite: 2].")
            st.write("Bankovní rada má **sedm členů**[cite: 2]:")
            st.markdown("""
            * guvernér[cite: 2],
            * dva viceguvernéři[cite: 2],
            * čtyři další členové bankovní rady[cite: 2].
            """)
            st.write("Členy bankovní rady jmenuje prezident republiky[cite: 2]. V čele ČNB stojí guvernér, který reprezentuje ČNB navenek a řídí jednání bankovní rady[cite: 2]. V současnosti je guvernérem ČNB Aleš Michl[cite: 2].")
            
            st.markdown("""
            <div class='box-gray'>
                🧭 <strong>Jak si to představit:</strong> Bankovní rada je jako „řídicí tým“ centrální banky[cite: 2]. Nerozhoduje o tom, komu banka dá spotřebitelský úvěr[cite: 2]. Rozhoduje o pravidlech a nastavení systému, který ovlivňuje všechny banky a celou ekonomiku[cite: 2].
            </div>
            """, unsafe_allow_html=True)

        # 1.2.6
        with st.container(border=True):
            st.markdown("### 1.2.6 Jak ČNB zasahuje do ekonomiky")
            st.write("ČNB neřídí ekonomiku příkazem typu „zdražte“ nebo „zlevněte“[cite: 2]. Ovlivňuje ekonomiku hlavně nepřímo — přes cenu peněz, důvěru a pravidla finančního trhu[cite: 2].")
            st.write("Nejdůležitější nástroje jsou[cite: 2]:")
            st.markdown("""
            * **úrokové sazby** — když ČNB sazby zvýší, úvěry bývají dražší a spoření atraktivnější; když sazby sníží, úvěry mohou zlevnit a ekonomická aktivita se může podpořit[cite: 2],
            * **operace na finančním trhu** — ČNB může stahovat nebo dodávat likviditu bankovnímu systému[cite: 2],
            * **povinné minimální rezervy** — banky musí držet část prostředků u centrální banky[cite: 2],
            * **devizové intervence** — ve výjimečných situacích může ČNB nakupovat nebo prodávat měny a tím ovlivňovat kurz koruny[cite: 2],
            * **makroobezřetnostní politika** — ČNB může nastavovat pravidla, která mají zabránit nadměrnému zadlužování a přehřívání finančního trhu[cite: 2],
            * **dohled a regulace** — kontroluje, zda finanční instituce dodržují pravidla a mají dostatečnou odolnost[cite: 2].
            """)

            st.markdown("""
            <div class='box-gray'>
                🧰 <strong>Hlavní nástroje ČNB:</strong> ČNB používá hlavně nástroje měnové politiky, nástroje pro řízení likvidity bankovního systému, devizové nástroje, dohledové nástroje a makroobezřetnostní pravidla[cite: 2]. Nejde o jeden „kouzelný knoflík“, ale o kombinaci opatření, která ovlivňují cenu peněz, množství peněz v oběhu, chování bank a stabilitu finančního systému[cite: 2].
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            | Nástroj ČNB | Jak funguje | Co ovlivňuje |
            | :--- | :--- | :--- |
            | **Základní úrokové sazby** | ČNB nastavuje sazby, za kterých si banky ukládají peníze u ČNB nebo si od ní krátkodobě půjčují. Nejsledovanější je dvoutýdenní repo sazba[cite: 2]. | Cenu úvěrů, výnosnost spoření, kurz koruny, inflaci a ochotu domácností i firem utrácet nebo investovat[cite: 2]. |
            | **Repo operace** | ČNB pomocí obchodů s bankami stahuje nebo dodává peníze do bankovního systému. V české praxi často stahuje přebytečnou likviditu[cite: 2]. | Množství dostupných peněz v bankovním systému a krátkodobé tržní úrokové sazby[cite: 2]. |
            | **Diskontní sazba** | Sazba spojená s možností bank uložit přebytečné prostředky u ČNB[cite: 2]. | Spodní hranici krátkodobých sazeb na peněžním trhu[cite: 2]. |
            | **Lombardní sazba** | Sazba, za kterou si banky mohou půjčit od ČNB proti zástavě cenných papírů[cite: 2]. | Horní hranici krátkodobých sazeb a nouzové krátkodobé financování bank[cite: 2]. |
            | **Povinné minimální rezervy** | Banky musí držet určitou část vkladů u ČNB[cite: 2]. | Likviditu bank a stabilitu bankovního systému[cite: 2]. |
            | **Devizové intervence** | ČNB může nakupovat nebo prodávat zahraniční měny, aby ovlivnila kurz koruny[cite: 2]. | Kurz koruny, dovozní ceny, export, inflaci a očekávání na finančním trhu[cite: 2]. |
            | **Devizové rezervy** | ČNB spravuje aktiva v zahraničních měnách[cite: 2]. | Důvěru v měnu, schopnost zasáhnout na devizovém trhu a finanční stabilitu[cite: 2]. |
            | **Makroobezřetnostní limity** | ČNB může nastavovat pravidla pro bezpečnější úvěrování, například u hypoték sleduje vztah výše úvěru k hodnotě nemovitosti nebo příjmům žadatele[cite: 2]. | Zadlužení domácností, stabilitu bank a riziko cenových bublin[cite: 2]. |
            | **Kapitálové požadavky na banky**| Banky musí mít dost vlastního kapitálu, aby zvládly ztráty[cite: 2]. | Odolnost bank při krizi a ochranu finančního systému[cite: 2]. |
            | **Dohled a sankce** | ČNB kontroluje finanční instituce, může požadovat nápravu nebo uložit sankce[cite: 2]. | Dodržování pravidel, ochranu klientů a důvěru ve finanční trh[cite: 2]. |
            """) #[cite: 2]

            st.markdown("##### Repo sazba lidsky")
            st.write("Když média říkají, že „ČNB zvýšila sazby“, často mluví hlavně o repo sazbě[cite: 2]. Ta je důležitým signálem pro celý finanční trh[cite: 2]. Banky podle ní upravují vlastní sazby u úvěrů a vkladů[cite: 2]. Neznamená to, že se hypotéka nebo spořicí účet změní přes noc stejně u všech bank, ale směr rozhodnutí ČNB se do bankovních produktů postupně promítá[cite: 2].")

            st.markdown("#### 🧮 Mini kalkulačka: Repo sazba v praxi")
            st.write("Porovnej dvě situace[cite: 2]:")
            st.markdown("""
            | Situace | Spoření | Úvěry | Typický dopad |
            | :--- | :--- | :--- | :--- |
            | **Nižší sazby** | nižší výnos | levnější půjčky | větší chuť utrácet a investovat |
            | **Vyšší sazby** | vyšší výnos | dražší půjčky | větší motivace spořit, menší chuť se zadlužovat |
            """) #[cite: 2]

            st.write("**Úkol:** Spočítej si orientační roční úrok při různých sazbách[cite: 2]:")
            col_calc1, col_calc2 = st.columns(2)
            with col_calc1:
                calc_spor_val = st.number_input("Částka na spořicím účtu (Kč):", value=20000, step=1000, key="k2_c_spor")
            with col_calc2:
                calc_pujck_val = st.number_input("Částka půjčky (Kč):", value=100000, step=5000, key="k2_c_pujck")

            repo_rate_pct = st.select_slider("Zvol výši úrokové sazby (p.a.):", options=[3.0, 5.0, 7.0], value=5.0, key="k2_repo_slider_exact")

            res_spor = calc_spor_val * (repo_rate_pct / 100)
            res_pujck = calc_pujck_val * (repo_rate_pct / 100)

            c_res1, c_res2 = st.columns(2)
            c_res1.metric("Orientační roční výnos ze spoření", f"{res_spor:,.0f} Kč".replace(",", " "))
            c_res2.metric("Orientační roční úrok z půjčky", f"{res_pujck:,.0f} Kč".replace(",", " "))

            st.text_area("Komentář: Proč stejné rozhodnutí ČNB může někomu pomoci a jinému uškodit?", key="k2_repo_comment")

            st.write("**Příklad: co se stane, když ČNB zvýší úrokové sazby?** Vyšší sazby obvykle zdražují půjčky[cite: 2]. Domácnosti a firmy si proto mohou méně půjčovat a méně utráce[cite: 2]. Zároveň může být výhodnější spořit[cite: 2]. Tlak na růst cen se tím může snížit[cite: 2]. Nevýhodou je, že dražší úvěry mohou zpomalit investice firem, hypotéky nebo spotřebu[cite: 2].")

            st.markdown("#### 🧮 Simulace: Vyšší sazby, inflace a hypotéka")
            st.write("Situace: ČNB drží měnovou politiku přísnější, aby brzdila inflaci[cite: 2]. V roce 2026 byla repo sazba ČNB kolem 3,5 %, průměrné hypoteční sazby se u nových hypoték pohybovaly přibližně okolo 5 % p.a. a nižší inflaci budeme v modelu počítat jako 2 %, protože přibližně kolem této hodnoty se pohybuje dlouhodobý inflační cíl ČNB[cite: 2].")
            st.write("Aby to bylo na první pohled: Porovnáme jednu domácnost ve dvou světech[cite: 2]. V obou světech má stejnou hypotéku 3 000 000 Kč na 25 let a stejné běžné měsíční výdaje 40 000 Kč bez hypotéky[cite: 2]. Liší se jen úroky a inflace[cite: 2].")

            with st.expander("Co znamená „koš 40 000 Kč“ (Detailní rozpis)"):
                st.markdown("""
                | Položka v měsíčním koši | Modelová částka | Co si pod tím představit |
                | :--- | :--- | :--- |
                | **Potraviny a drogerie** | 15 000 Kč | běžné nákupy v obchodě, základní potřeby, hygienické zboží |
                | **Energie a služby spojené s bydlením** | 8 000 Kč | elektřina, plyn, voda, teplo, odpad, poplatky za služby |
                | **Doprava** | 5 000 Kč | benzín, MHD, vlak, servis auta, parkování |
                | **Telefon, internet, předplatná** | 3 000 Kč | mobilní tarif, internet, streamovací služby, cloud |
                | **Oblečení, škola, zdraví, volný čas** | 6 000 Kč | oblečení, léky, kroužky, školní pomůcky, sport, kultura |
                | **Ostatní rezerva v měsíčních výdajích**| 3 000 Kč | drobné opravy, nečekané nákupy, dárky, domácnost |
                | **Celkem běžné výdaje bez hypotéky** | 40 000 Kč | částka, na které ukazujeme dopad inflace |
                """) #[cite: 2]

            st.markdown("""
            | Modelový svět | Hypotéka | Inflace a běžné výdaje | Co domácnost pocítí za měsíc |
            | :--- | :--- | :--- | :--- |
            | **Levné úvěry, ale vyšší inflace** | úrok 2,5 % → splátka cca 13 500 Kč | inflace 5 % → koš 40 000 Kč zdraží zhruba o 2 000 Kč za měsíc | nižší splátka, ale dražší nákupy |
            | **Dražší úvěry, ale nižší inflace** | úrok 5 % → splátka cca 17 500 Kč | inflace 2 % → koš 40 000 Kč zdraží zhruba o 800 Kč za měsíc | vyšší splátka, ale pomalejší zdražování |
            | **Rozdíl** | hypotéka je dražší asi o 4 000 Kč měsíčně | běžné výdaje rostou asi o 1 200 Kč měsíčně méně | domácnost s hypotékou je v tomto modelu pořád asi 2 800 Kč měsíčně v mínusu |
            """) #[cite: 2]

            st.write("**Jednoduchý závěr pro žáka:** Pokud má domácnost velkou hypotéku, vyšší sazby ji bolí hned a velmi viditelně[cite: 2]. Nižší inflace jí sice pomáhá, protože nákupy nezdražují tak rychle, ale v tomto modelu to nestačí vyrovnat dražší hypotéku[cite: 2]. Proto lidé často reagují na vysoké sazby jako na „červenou na býka“ — splátka úvěru je jedna konkrétní částka na účtu, zatímco přínos nižší inflace je rozptýlený v cenách mnoha nákupů[cite: 2].")
            st.write("**Pozor:** To neznamená, že vyšší sazby jsou zbytečné[cite: 2]. Pomáhají brzdit inflaci v celé ekonomice, chránit hodnotu mezd a úspor a bránit tomu, aby se zdražování utrhlo z řetězu[cite: 2]. Jen je potřeba rozlišit pohled celé ekonomiky a pohled konkrétní zadlužené domácnosti[cite: 2].")

            st.write("**Příklad: co se stane, když ČNB sníží úrokové sazby?** Nižší sazby mohou zlevnit úvěry a podpořit spotřebu i investice[cite: 2]. Lidé a firmy si mohou snadněji půjčovat[cite: 2]. Pokud je ale ekonomika už přehřátá, příliš levné peníze mohou podporovat inflaci nebo vznik cenových bublin, například na trhu nemovitostí[cite: 2].")

        # 1.2.7
        with st.container(border=True):
            st.markdown("### 1.2.7 Koho a co ČNB „řídí“ a koho ne")
            st.write("ČNB neřídí osobní účty občanů a neurčuje jednotlivým lidem, kolik si mohou půjčit[cite: 2]. Neřídí ani každodenní obchodní rozhodnutí komerčních bank[cite: 2]. Má ale silný vliv na pravidla a prostředí, ve kterém banky a další finanční instituce fungují[cite: 2].")
            st.write("ČNB zejména[cite: 2]:")
            st.markdown("""
            * uděluje vybraným finančním institucím povolení k činnosti[cite: 2],
            * dohlíží na banky a další finanční instituce[cite: 2],
            * může ukládat nápravná opatření nebo sankce[cite: 2],
            * nastavuje některá pravidla pro stabilitu bankovního sektoru[cite: 2],
            * provozuje důležité platební systémy[cite: 2],
            * vydává hotovost[cite: 2],
            * ovlivňuje cenu peněz v ekonomice[cite: 2].
            """)

            st.markdown("""
            <div class='box-red'>
                ⚠️ <strong>Pozor na častý omyl:</strong> ČNB není „nadřízená pobočka“ tvojí banky, která řeší každou reklamaci platební karty[cite: 2]. Reklamaci řeší nejdříve tvoje banka[cite: 2]. ČNB ale dohlíží na to, aby finanční instituce dodržovaly pravidla[cite: 2].
            </div>
            """, unsafe_allow_html=True)

            st.markdown("#### 🧩 Třídicí hra: ČNB, nebo komerční banka?")
            st.write("Rozděl výroky do správných skupin (ČNB / Komerční banka)[cite: 2]:")

            g1 = st.selectbox("1. Vydává bankovky a mince:", ["Vyber...", "ČNB", "Komerční banka"], key="k2_g1")
            g2 = st.selectbox("2. Vede běžný účet občanům:", ["Vyber...", "ČNB", "Komerční banka"], key="k2_g2")
            g3 = st.selectbox("3. Poskytuje hypotéku:", ["Vyber...", "ČNB", "Komerční banka"], key="k2_g3")
            g4 = st.selectbox("4. Nastavuje základní úrokové sazby:", ["Vyber...", "ČNB", "Komerční banka"], key="k2_g4")
            g5 = st.selectbox("5. Vydává platební kartu klientovi:", ["Vyber...", "ČNB", "Komerční banka"], key="k2_g5")
            g6 = st.selectbox("6. Dohlíží na banky:", ["Vyber...", "ČNB", "Komerční banka"], key="k2_g6")
            g7 = st.selectbox("7. Spravuje devizové rezervy:", ["Vyber...", "ČNB", "Komerční banka"], key="k2_g7")
            g8 = st.selectbox("8. Umožňuje platbu mobilem:", ["Vyber...", "ČNB", "Komerční banka"], key="k2_g8")

            if st.button("Vyhodnotit třídicí hru", key="k2_game_eval"):
                if g1=="ČNB" and g2=="Komerční banka" and g3=="Komerční banka" and g4=="ČNB" and g5=="Komerční banka" and g6=="ČNB" and g7=="ČNB" and g8=="Komerční banka":
                    st.success("🎉 Skvělé! Všechny položky jsi zařadil/a absolutně správně[cite: 2].")
                else:
                    st.error("Některé položky nejsou zařazeny správně[cite: 2]. Zkontroluj si: ČNB neposkytuje běžné účty ani karty veřejnosti[cite: 2]!")

        # 1.2.8
        with st.container(border=True):
            st.markdown("### 1.2.8 Komerční banky: banky pro občany a firmy")
            st.write("Komerční banky jsou finanční instituce, které podnikají na finančním trhu[cite: 2]. Jejich hlavní činností je přijímat vklady, poskytovat úvěry a zprostředkovávat platební styk[cite: 2]. Potřebují bankovní licenci a podléhají dohledu ČNB[cite: 2].")
            
            st.markdown("""
            <div class='box-blue'>
                🏧 <strong>Komerční banka v jedné větě:</strong> Přijímá peníze od klientů, vede jim účty, umožňuje platby a část získaných zdrojů půjčuje jiným klientům formou úvěrů[cite: 2].
            </div>
            """, unsafe_allow_html=True)
            st.write("Komerční banky jsou obchodní společnosti[cite: 2]. Řídí je jejich vlastní orgány, například představenstvo a management banky, a kontrolují je vlastníci, dozorčí orgány, auditoři a regulátor[cite: 2]. Zároveň musí dodržovat zákony, pravidla kapitálové přiměřenosti, pravidla proti praní špinavých peněz, pravidla ochrany spotřebitele a další regulaci[cite: 2].")

        # 1.2.9
        with st.container(border=True):
            st.markdown("### 1.2.9 Co komerční banky poskytují občanům")
            st.write("Pro běžného člověka je banka hlavně místem, kde se spravují každodenní peníze[cite: 2]. Banka může poskytovat například[cite: 2]:")
            st.markdown("""
            * běžný účet[cite: 2],
            * spořicí účet[cite: 2],
            * termínovaný vklad[cite: 2],
            * platební kartu[cite: 2],
            * internetové a mobilní bankovnictví[cite: 2],
            * tuzemské i zahraniční platby[cite: 2],
            * trvalé příkazy a inkasa[cite: 2],
            * hotovostní služby[cite: 2],
            * spotřebitelský úvěr[cite: 2],
            * kontokorent[cite: 2],
            * kreditní kartu[cite: 2],
            * hypotéku[cite: 2],
            * směnu měn[cite: 2],
            * investiční produkty nebo jejich zprostředkování[cite: 2],
            * pojištění nebo jeho zprostředkování[cite: 2],
            * bezpečnostní nástroje, například limity plateb, 3D Secure nebo potvrzování v aplikaci[cite: 2].
            """)

            st.markdown("""
            <div class='box-purple'>
                📱 <strong>Moderní realita:</strong> Pro mnoho mladých lidí už banka není pobočka[cite: 2]. Je to aplikace, ve které vidí zůstatek, platí mobilem, nastavují limity, blokují kartu, kontrolují předplatná a posílají peníze přes QR kód[cite: 2].
            </div>
            """, unsafe_allow_html=True)

        # 1.2.10
        with st.container(border=True):
            st.markdown("### 1.2.10 Co komerční banky poskytují firmám")
            st.write("Firmy potřebují banky nejen k placení faktur[cite: 2]. Banky jim pomáhají financovat provoz, investice a obchod[cite: 2].")
            st.write("Firmám banky poskytují například[cite: 2]:")
            st.markdown("""
            * podnikatelské účty[cite: 2],
            * platební terminály[cite: 2],
            * provozní úvěry[cite: 2],
            * investiční úvěry[cite: 2],
            * kontokorentní financování[cite: 2],
            * bankovní záruky[cite: 2],
            * dokumentární platby v mezinárodním obchodě[cite: 2],
            * směnárenské a devizové služby[cite: 2],
            * správu likvidity[cite: 2],
            * financování exportu[cite: 2],
            * firemní platební karty[cite: 2].
            """)

        # 1.2.11
        with st.container(border=True):
            st.markdown("### 1.2.11 Aktivní, pasivní a neutrální operace bank")
            st.write("Činnosti komerčních bank se často rozdělují na pasivní, aktivní a neutrální operace[cite: 2].")

            st.markdown("""
            | Typ operace | Co znamená | Příklady |
            | :--- | :--- | :--- |
            | **Pasivní operace** | Banka získává zdroje. Z pohledu banky jde o závazky vůči klientům nebo investorům[cite: 2]. | běžné účty, spořicí účty, termínované vklady, vydané bankovní dluhopisy, přijaté mezibankovní úvěry[cite: 2] |
            | **Aktivní operace** | Banka peníze umísťuje tak, aby vydělávala. Z pohledu banky jde o aktiva[cite: 2]. | spotřebitelské úvěry, hypotéky, podnikatelské úvěry, kontokorenty, kreditní karty, nákup cenných papírů[cite: 2] |
            | **Neutrální operace** | Banka poskytuje služby, ze kterých získává poplatky nebo provize, ale přímo při nich nepůjčuje vlastní peníze jako u úvěru[cite: 2]. | platební styk, vedení účtu, směna měn, zprostředkování investic, úschova cenností, poradenství, bankovní záruky[cite: 2] |
            """) #[cite: 2]

            st.markdown("""
            <div class='box-gray'>
                🧮 <strong>Jednoduchá logika banky:</strong> Banka přijímá vklady za určitý úrok a půjčuje peníze za vyšší úrok[cite: 2]. Rozdíl mezi úrokem z úvěrů a úrokem z vkladů je jedním ze zdrojů jejích výnosů[cite: 2]. Dalším zdrojem jsou poplatky a provize za služby[cite: 2].
            </div>
            """, unsafe_allow_html=True)

            with st.expander("Podrobný rozbor: Pasivní operace (jak banka získává peníze)"):
                st.write("Pasivní operace jsou činnosti, při kterých banka získává zdroje[cite: 2]. Říká se jim pasivní proto, že z pohledu bankovní rozvahy vzniká bance závazek: banka peníze klientovi dluží[cite: 2].")
                st.markdown("""
                * **běžné účty** — klient má peníze dostupné pro každodenní platby; banka je eviduje jako závazek[cite: 2],
                * **spořicí účty** — klient ukládá peníze s vyšším úrokem než na běžném účtu[cite: 2],
                * **termínované vklady** — klient uloží peníze na předem určenou dobu a za to získá sjednaný úrok[cite: 2],
                * **vkladové produkty pro firmy** — firmy ukládají volné prostředky[cite: 2],
                * **emise bankovních dluhopisů** — banka si půjčuje od investorů tím, že vydá dluhopis[cite: 2],
                * **mezibankovní úvěry přijaté** — banka si půjčí od jiné banky[cite: 2],
                * **vlastní kapitál banky** — peníze vlastníků, které slouží jako bezpečnostní polštář[cite: 2].
                """)
                st.info("📥 **Příklad pasivní operace:** Student si uloží 5 000 Kč na spořicí účet. Pro studenta je to úspora. Pro banku je to zdroj peněz a zároveň závazek, protože banka musí umožnit výběr podle podmínek účtu[cite: 2].")

            with st.expander("Podrobný rozbor: Aktivní operace (jak banka peníze používá)"):
                st.write("Aktivní operace jsou činnosti, při kterých banka umisťuje získané peníze tak, aby vydělávala[cite: 2]. Z pohledu banky jde o aktiva: banka má pohledávku za klientem nebo vlastní určitý finanční nástroj[cite: 2].")
                st.markdown("""
                * **spotřebitelské úvěry** — půjčky domácnostem například na vybavení, auto nebo jiné potřeby[cite: 2],
                * **hypoteční úvěry** — dlouhodobé úvěry na bydlení zajištěné nemovitostí[cite: 2],
                * **kontokorent** — možnost jít na běžném účtu do mínusu do stanoveného limitu[cite: 2],
                * **kreditní karta** — úvěrový rámec spojený s kartou[cite: 2],
                * **podnikatelské a investiční úvěry** — úvěry pro firmy na provoz, stroje nebo rozšíření[cite: 2],
                * **nákup cenných papírů** — banka investuje část peněz podle pravidel řízení rizik[cite: 2].
                """)
                st.info("📤 **Příklad aktivní operace:** Banka poskytne rodině hypotéku. Rodina získá peníze na bydlení, ale bance vzniká pohledávka: rodina musí úvěr splácet i s úrokem[cite: 2].")

            with st.expander("Podrobný rozbor: Neutrální operace (služby za poplatky)"):
                st.write("Neutrální operace nejsou hlavně o přijímání vkladů nebo poskytování úvěrů[cite: 2]. Banka při nich zajišťuje služby a vydělává například na poplatcích nebo provizích[cite: 2]. Patří sem vedení účtu, zpracování plateb, vydání karty, směna měn, výklady/výběry hotovosti, zprostředkování investic či pojištění, úschova cenností a finanční poradenství[cite: 2].")

            st.markdown("""
            | Situace klienta | Typ operace banky | Proč |
            | :--- | :--- | :--- |
            | Klient vloží peníze na spořicí účet. | **Pasivní** | Banka získává zdroj a má závazek vůči klientovi[cite: 2]. |
            | Klient si vezme hypotéku. | **Aktivní** | Banka poskytuje úvěr a očekává splácení s úrokem[cite: 2]. |
            | Klient zaplatí kartou v obchodě. | **Neutrální** | Banka zajišťuje platební službu[cite: 2]. |
            | Firma získá provozní úvěr. | **Aktivní** | Banka financuje firmu a nese úvěrové riziko[cite: 2]. |
            | Klient si vymění koruny za eura. | **Neutrální** | Banka poskytuje směnárenskou službu a vydělává na kurzu nebo poplatku[cite: 2]. |
            """) #[cite: 2]

            st.markdown("#### 🧩 Rozhodovací karty operací")
            st.write("U každé situace urči typ bankovní operace[cite: 2]:")

            cards_q1 = st.selectbox("1. Klient vloží 10 000 Kč na spořicí účet:", ["Vyber...", "Pasivní", "Aktivní", "Neutrální"], key="k2_cards1")
            cards_q2 = st.selectbox("2. Rodina si vezme hypotéku:", ["Vyber...", "Pasivní", "Aktivní", "Neutrální"], key="k2_cards2")
            cards_q3 = st.selectbox("3. Student zaplatí kartou v kavárně:", ["Vyber...", "Pasivní", "Aktivní", "Neutrální"], key="k2_cards3")
            cards_q4 = st.selectbox("4. Firma požádá o provozní úvěr:", ["Vyber...", "Pasivní", "Aktivní", "Neutrální"], key="k2_cards4")
            cards_q5 = st.selectbox("5. Klient si smění koruny na eura:", ["Vyber...", "Pasivní", "Aktivní", "Neutrální"], key="k2_cards5")

            if st.button("Vyhodnotit rozhodovací karty", key="k2_cards_eval"):
                if cards_q1=="Pasivní" and cards_q2=="Aktivní" and cards_q3=="Neutrální" and cards_q4=="Aktivní" and cards_q5=="Neutrální":
                    st.success("🎉 Výborně! Přesně chápeš rozdíl mezi získáváním zdrojů, půjčováním a službami[cite: 2].")
                else:
                    st.error("Některá odpověď nesouhlasí[cite: 2]. Zkontroluj: Vklady = Pasivní, Úvěry = Aktivní, Služby = Neutrální[cite: 2].")

        # 1.2.12
        with st.container(border=True):
            st.markdown("### 1.2.12 Jak banka vydělává a proč musí hlídat riziko")
            st.write("Banka nevydělává jen tím, že „má peníze“[cite: 2]. Vydělává hlavně na[cite: 2]:")
            st.markdown("""
            * úrokové marži[cite: 2],
            * poplatcích[cite: 2],
            * provizích[cite: 2],
            * investičních a devizových operacích[cite: 2],
            * službách pro firmy a instituce[cite: 2].
            """)
            st.write("Zároveň ale nese rizika[cite: 2]:")
            st.markdown("""
            * **úvěrové riziko** — klient nesplatí úvěr[cite: 2],
            * **likviditní riziko** — banka nemá v daný okamžik dost dostupných peněz[cite: 2],
            * **úrokové riziko** — změna sazeb ovlivní výnosy a náklady banky[cite: 2],
            * **měnové riziko** — změna kurzu ovlivní hodnotu obchodů v cizí měně[cite: 2],
            * **operační riziko** — selže systém, proces nebo človek[cite: 2],
            * **kybernetické riziko** — útok na digitální bankovnictví nebo data klientů[cite: 2].
            """)

            st.markdown("""
            <div class='box-red'>
                🔐 <strong>Proč existuje regulace:</strong> Kdyby banky riskovaly příliš mnoho, neohrozily by jen sebe[cite: 2]. Ohrozily by vklady klientů, firmy, platební systém i celou ekonomiku[cite: 2]. Proto jsou banky přísně regulované a dohlížené[cite: 2].
            </div>
            """, unsafe_allow_html=True)

        # 1.2.13
        with st.container(border=True):
            st.markdown("### 1.2.13 Bankovní licence a dohled")
            st.write("Banka nemůže začít fungovat jen proto, že si někdo založí aplikaci a napíše „banka“[cite: 2]. K poskytování bankovních služeb potřebuje povolení[cite: 2]. V České republice nad bankami dohlíží ČNB[cite: 2].")
            st.write("ČNB sleduje například[cite: 2]:")
            st.markdown("""
            * zda banka má dost kapitálu[cite: 2],
            * zda rozumně řídí rizika[cite: 2],
            * zda dodržuje pravidla pro ochranu klientů[cite: 2],
            * zda plní povinnosti proti praní špinavých peněz[cite: 2],
            * zda má bezpečné systémy[cite: 2],
            * zda je schopna zvládnout krizové situace[cite: 2].
            """)

            st.write("**Proč banka nemůže půjčit úplně všechno, co má?** Protože musí zvládnout běžné výběry klientů, platby, regulatorní požadavky a krizové situace[cite: 2]. Banka musí držet určité rezervy a kapitál[cite: 2]. Pokud by půjčovala příliš rizikově, mohla by ohrozit důvěru klientů i stabilitu celého systému[cite: 2].")

            st.markdown("#### 🛠️ Mini audit banky")
            st.write("Představ si, že jsi bankovní analytik[cite: 2]. Máš posoudit, jestli banka nepodstupuje moc velké riziko[cite: 2]. Odpověz na tři otázky[cite: 2]:")

            audit_q1 = st.radio("1. Půjčuje banka lidem a firmám, kteří pravděpodobně zvládnou splácet?", ["Ano, má přísná pravidla", "Ne, půjčí komukoliv bez kontroly"], key="k2_aud1")
            audit_q2 = st.radio("2. Má banka dost peněz pro běžné denní výběry a platby klientů?", ["Ano, drží dostatečnou likviditu", "Ne, všechny peníze rozpůjčovala na 30 let"], key="k2_aud2")
            audit_q3 = st.radio("3. Má banka dost kapitálu, aby zvládla případné ztráty?", ["Ano, plní kapitálové požadavky", "Ne, nemá žádné vlastní rezervy"], key="k2_aud3")

            audit_rec = st.text_area("Napiš doporučení: Co by měla banka zlepšit, aby byla bezpečnější?", key="k2_aud_rec")

            if st.button("Vyhodnotit mini audit banky", key="k2_aud_btn"):
                if audit_q1 == "Ano, má přísná pravidla" and audit_q2 == "Ano, drží dostatečnou likviditu" and audit_q3 == "Ano, plní kapitálové požadavky":
                    st.success("✅ **Výborný audit:** Banka splňuje základní pilíře finanční stability[cite: 2].")
                else:
                    st.error("⚠️ **Varování auditu:** Banka podstupuje vysoká rizika, která mohou vedoucí k ohrožení vkladatelů[cite: 2]!")

        # 1.2.14
        with st.container(border=True):
            st.markdown("### 1.2.14 Vklady a jejich ochrana")
            st.write("Vklady klientů v bankách jsou v zákonem stanoveném rozsahu chráněny systémem pojištění vkladů[cite: 2]. Smyslem je posílit důvěru lidí v bankovní systém a snížit riziko paniky při problémech banky[cite: 2].")

            st.markdown("""
            <div class='box-blue'>
                🛟 <strong>Do jaké výše jsou vklady pojištěny:</strong> V České republice jsou pojištěné vklady u bank, družstevních záložen a stavebních spořitelen chráněny zpravidla do výše 100 000 EUR na jednoho klienta u jedné banky[cite: 2]. V přepočtu jde přibližně o 2,4–2,5 milionu Kč, podle aktuálního kurzu[cite: 2]. Pokud má člověk u jedné banky více účtů, limit se obvykle počítá dohromady za daného klienta u dané banky, ne zvlášť za každý účet[cite: 2].
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            | Situace | Jak to zjednodušeně funguje | Příklad |
            | :--- | :--- | :--- |
            | **Klient má u jedné banky 500 000 Kč** | Částka je pod limitem pojištění vkladů[cite: 2]. | Při krachu banky by měla být chráněna celá částka[cite: 2]. |
            | **Klient má u jedné banky 2 000 000 Kč** | Částka je stále přibližně pod limitem 100 000 EUR[cite: 2]. | Vklad by byl obvykle chráněn celý[cite: 2]. |
            | **Klient má u jedné banky 4 000 000 Kč** | Část přesahuje základní limit pojištění[cite: 2]. | Pojištěna by byla jen část do limitu; zbytek by nesl riziko[cite: 2]. |
            | **Klient má 2 000 000 Kč v jedné bance a 2 000 000 Kč v jiné bance** | Limit se posuzuje u každé banky zvlášť[cite: 2]. | Rozložení peněz mezi banky může snížit riziko překročení limitu[cite: 2]. |
            """) #[cite: 2]

            st.write("**Kdo pojištění vkladů zajišťuje?** V České republice výplatu náhrad zajišťuje Garanční systém finančního trhu prostřednictvím Fondu pojištění vkladů[cite: 2]. Pokud by banka zkrachovala a nebyla schopná vyplatit klientům vklady, systém pojištění vkladů slouží k tomu, aby klienti dostali náhradu do zákonem stanoveného limitu[cite: 2].")

            st.markdown("##### Výběr hotovosti: kolik lze vybrat a kdy to hlásit bance")
            st.write("To, že má člověk peníze na účtu, neznamená, že si může kdykoliv bez přípravy odnést z pobočky libovolně vysokou hotovost[cite: 2]. Banka musí mít hotovost fyzicky připravenou na pobočce a zároveň musí plnit pravidla proti praní špinavých peněz[cite: 2].")

            st.markdown("""
            | Typ výběru | Jak to běžně funguje | Na co si dát pozor |
            | :--- | :--- | :--- |
            | **Výběr z bankomatu** | Řídí se limitem platební karty a limitem konkrétního bankomatu[cite: 2]. | Limit si člověk často nastavuje v aplikaci, ale bankomat může mít i vlastní technické omezení[cite: 2]. |
            | **Menší výběr na pobočce** | Obvykle lze vybrat bez předchozího objednání, pokud má pobočka hotovost k dispozici[cite: 2]. | Každá banka může mít vlastní pravidla a limity[cite: 2]. |
            | **Větší hotovostní výběr** | Často je vhodné nebo nutné oznámit ho bance předem, ale hranice se mezi bankami výrazně liší[cite: 2]. | Například u ČSOB je podle zveřejněných informací potřeba předem objednat až částku převyšující 300 000 Kč; u KB se naopak uvádí hlášení už nad 100 000 Kč[cite: 2]. |
            | **Velmi vysoký výběr** | Banka může požadovat písemné oznámení, objednání hotovosti nebo vysvětlení účelu[cite: 2]. | Nejde o zvědavost pokladníka, ale o provozní a zákonné povinnosti banky[cite: 2]. |
            """) #[cite: 2]

            st.markdown("""
            <div class='box-red'>
                ⚠️ <strong>Důležité:</strong> Neexistuje jedno univerzální číslo, které by platilo pro všechny banky jako „do této částky nikdy nic nehlaš“[cite: 2]. U velkých výběrů hotovosti záleží na pravidlech konkrétní banky, typu pobočky, měně, dostupnosti hotovosti a bezpečnostních pravidlech[cite: 2].
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class='box-purple'>
                🧠 <strong>Proč banka řeší velké hotovostní výběry:</strong><br>
                • <strong>Provozní důvod:</strong> pobočka nemusí mít okamžitě připravené velké množství hotovosti[cite: 2].<br>
                • <strong>Bezpečnost:</strong> převoz a výdej vysoké hotovosti je rizikový[cite: 2].<br>
                • <strong>AML pravidla:</strong> banka musí sledovat podezřelé transakce a původ peněz, aby se bránilo praní špinavých peněz a financování nelegálních aktivit[cite: 2].<br>
                • <strong>Ochrana klienta:</strong> neobvyklý výběr může být i signál, že je klient pod tlakem podvodníka[cite: 2].
            </div>
            """, unsafe_allow_html=True)

            st.write("**Příklad: výběr 300 000 Kč nebo 600 000 Kč na koupi auta:** Pokud chce klient vybrat 300 000 Kč v hotovosti, u některých bank to může být ještě běžně proveditelné bez zvláštního objednání, pokud má pobočka hotovost a klient splňuje limity účtu nebo karty[cite: 2]. Například ČSOB uvádí, že předem je potřeba objednat až částku převyšující 300 000 Kč, případně výběr v cizí měně nebo požadovanou konkrétní skladbu bankovek[cite: 2]. Pokud ale chce klient vybrat třeba 600 000 Kč, už je mnohem pravděpodobnější, že banka bude chtít výběr předem objednat[cite: 2]. Potřebuje připravit hotovost, zajistit bezpečný provoz pobočky a splnit pravidla proti praní špinavých peněz[cite: 2]. Neznamená to, že peníze nejsou klienta[cite: 2]. Znamená to, že vysoká hotovost je pro banku provozní, bezpečnostní a regulatorní situace[cite: 2].")

            st.markdown("""
            <div class='box-blue'>
                🛟 <strong>Co si zapamatovat:</strong> Peníze na běžném nebo spořicím účtu nejsou totéž jako hotovost v peněžence[cite: 2]. Jsou to pohledávky vůči bance[cite: 2]. Proto je důležité, aby banky byly regulované, dohlížené a aby existovala pravidla ochrany vkladatelů[cite: 2]. Základní pojištění vkladů je do 100 000 EUR na klienta u jedné banky[cite: 2]. U hotovostních výběrů neplatí jedna hranice pro všechny banky — například ČSOB uvádí objednání až nad 300 000 Kč, zatímco jiné banky mohou chtít hlášení dříve[cite: 2].
            </div>
            """, unsafe_allow_html=True)

    # =========================================================================
    # 1.3 PLATEBNÍ STYK
    # =========================================================================
    elif "1.3 Platební styk" in selected_section_2:
        st.markdown("<div class='sub-section-header'>1. BANKOVNÍ SYSTÉM A PENÍZE V 21. STOLETÍ</div><h2>1.3 Platební styk</h2>", unsafe_allow_html=True)
        st.write("Platební styk znamená převod peněz mezi plátcem a příjemcem[cite: 2]. Díky platebnímu styku můžeme zaplatit oběd kartou, poslat nájem převodem, nakoupit online, zaplatit fakturu přes QR kód nebo přijmout výplatu na účet[cite: 2].")

        with st.container(border=True):
            st.markdown("""
            <div class='box-blue'>
                💳 <strong>Základní myšlenka:</strong> Platební styk je infrastruktura důvěry[cite: 2]. Umožňuje, aby se peníze bezpečně a prokazatelně přesunuly od toho, kdo platí, k tomu, kdo má peníze dostat[cite: 2].
            </div>
            """, unsafe_allow_html=True)

        # 1.3.1
        with st.container(border=True):
            st.markdown("### 1.3.1 Co nám platební styk umožňuje")
            st.write("Platební styk umožňuje[cite: 2]:")
            st.markdown("""
            * platit za zboží a služby[cite: 2],
            * přijímat mzdu, kapesné, dávky nebo platby od zákazníků[cite: 2],
            * splácet úvěry[cite: 2],
            * platit nájem, energie, školní akce nebo faktury[cite: 2],
            * převádět peníze mezi vlastními účty[cite: 2],
            * platit v zahraničí[cite: 2],
            * podnikům přijímat platby kartou nebo online[cite: 2],
            * státu vybírat daně a vyplácet veřejné výdaje[cite: 2].
            """)

        # 1.3.2
        with st.container(border=True):
            st.markdown("### 1.3.2 Druhy platebního styku")
            st.write("Platební styk lze rozdělit několika způsoby[cite: 2]:")

            st.markdown("""
            | Druh | Co znamená | Příklady |
            | :--- | :--- | :--- |
            | **Hotovostní** | Platí se fyzickými penězi[cite: 2]. | bankovky, mince, výběr z bankomatu, vklad hotovosti[cite: 2] |
            | **Bezhotovostní** | Peníze se převádějí jako záznam mezi účty[cite: 2]. | bankovní převod, platba kartou, trvalý příkaz, inkaso, QR platba[cite: 2] |
            | **Tuzemský** | Platba probíhá v rámci České republiky[cite: 2]. | převod mezi českými bankami v Kč[cite: 2] |
            | **Zahraniční** | Platba směřuje do jiné země nebo v jiné měně[cite: 2]. | SEPA platba v eurech, mezinárodní převod, platba kartou v zahraničí[cite: 2] |
            | **Jednorázový** | Platba se zadává pro jeden konkrétní převod[cite: 2]. | jednorázová úhrada faktury[cite: 2] |
            | **Opakovaný** | Platba se provádí pravidelně nebo automaticky[cite: 2]. | trvalý příkaz, SIPO, inkaso, předplatné[cite: 2] |
            | **Okamžitý** | Peníze dorazí během několika sekund, pokud to banky podporují[cite: 2]. | okamžitá platba mezi bankami[cite: 2] |
            """) #[cite: 2]

            st.markdown("#### 🧭 Aktivita: Vyber správný typ platby")
            st.write("U každé situace urči její charakteristiky[cite: 2]:")

            ps1 = st.selectbox("1. Platím kávu v hotovosti:", ["Vyber...", "Hotovostní, tuzemská, jednorázová", "Bezhotovostní, tuzemská, opakovaná"], key="k2_ps1")
            ps2 = st.selectbox("2. Posílám nájem trvalým příkazem:", ["Vyber...", "Bezhotovostní, tuzemská, opakovaná", "Hotovostní, zahraniční, jednorázová"], key="k2_ps2")
            ps3 = st.selectbox("3. Platím Spotify předplatné:", ["Vyber...", "Bezhotovostní, zahraniční/opakovaná", "Hotovostní, tuzemská, jednorázová"], key="k2_ps3")
            ps4 = st.selectbox("4. Posílám peníze na výlet přes QR kód:", ["Vyber...", "Bezhotovostní, tuzemská, jednorázová", "Hotovostní, zahraniční, opakovaná"], key="k2_ps4")

            if st.button("Vyhodnotit druhy plateb", key="k2_ps_btn"):
                if ps1=="Hotovostní, tuzemská, jednorázová" and ps2=="Bezhotovostní, tuzemská, opakovaná" and ps3=="Bezhotovostní, zahraniční/opakovaná" and ps4=="Bezhotovostní, tuzemská, jednorázová":
                    st.success("🎉 Správně zanalyzováno[cite: 2]!")
                else:
                    st.error("Zkontroluj své zařazení u jednotlivých situací[cite: 2].")

        # 1.3.3
        with st.container(border=True):
            st.markdown("### 1.3.3 Nejběžnější platební nástroje")
            st.write("Mezi nejčastější nástroje platebního styku patří[cite: 2]:")
            st.markdown("""
            * **hotovost** — bankovky a mince[cite: 2],
            * **příkaz k úhradě** — zadáš platbu ze svého účtu[cite: 2],
            * **trvalý příkaz** — pravidelná platba stejné částky[cite: 2],
            * **inkaso** — příjemce si stáhne platbu se souhlasem plátce, například energie[cite: 2],
            * **SIPO** — sdružené inkaso plateb obyvatelstva[cite: 2],
            * **platební karta** — debetní nebo kreditní[cite: 2],
            * **mobilní platby** — Apple Pay, Google Pay a podobné služby[cite: 2],
            * **QR platba** — načtení platebních údajů z QR kódu[cite: 2],
            * **online platební brána** — platba v e-shopu[cite: 2],
            * **SEPA platba** — převod v eurech v rámci evropského prostoru[cite: 2],
            * **zahraniční převod** — platba mimo běžný tuzemský nebo SEPA režim[cite: 2].
            """)

            st.markdown("#### 🧩 Interaktivní výzva")
            st.write("Vyber tři platby, které jsi provedl/a za poslední týden, a popiš je[cite: 2]:")
            st.text_area("Tvoje 3 platby (nástroj, typ, cíl):", key="k2_3_payments")

        # 1.3.4
        with st.container(border=True):
            st.markdown("### 1.3.4 Kdo platební styk řídí a reguluje")
            st.write("Platební styk není divoký prostor bez pravidel[cite: 2]. Funguje díky spolupráci bank, platebních institucí, karetních společností, technologických poskytovatelů, obchodníků, státu a regulátorů[cite: 2].")
            st.write("V České republice má důležitou roli[cite: 2]:")
            st.markdown("""
            * **ČNB** — provozuje a dohlíží na vybrané platební systémy a dohlíží na finanční instituce[cite: 2],
            * **komerční banky** — vedou účty klientů a zpracovávají platby[cite: 2],
            * **platební instituce a fintech firmy** — poskytují některé platební služby[cite: 2],
            * **karetní asociace** — nastavují pravidla karetních sítí[cite: 2],
            * **obchodníci a platební brány** — přijímají platby od zákazníků[cite: 2],
            * **právní předpisy ČR a EU** — stanovují pravidla bezpečnosti, práv klientů, odpovědnosti a ochrany spotřebitele[cite: 2].
            """)

            st.markdown("##### CERTIS: „dálnice“ pro platby mezi českými bankami")
            st.write("Když posíláme peníze v českých korunách, je důležité rozlišit, jestli jde platba v rámci jedné banky, nebo mezi dvěma různými bankami[cite: 2].")

            st.markdown("""
            <div class='box-blue'>
                🏦 <strong>Co je CERTIS:</strong> CERTIS je český systém mezibankovního platebního styku[cite: 2]. Zjednodušeně řečeno je to systém, přes který se v České republice zúčtovávají platby v korunách mezi různými bankami[cite: 2]. Název CERTIS znamená Czech Express Real Time Interbank Gross Settlement System[cite: 2]. Systém spravuje a provozuje Česká národní banka[cite: 2].
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            | Situace | Co se děje s platbou | Jde přes CERTIS? |
            | :--- | :--- | :--- |
            | **Platba v rámci stejné banky** | Oba účty jsou u stejné banky[cite: 2]. Banka si platbu zúčtuje ve vlastním systému: jednomu klientovi částku odepíše, druhému připíše[cite: 2]. | Obvykle ne[cite: 2]. Zůstává uvnitř banky[cite: 2]. |
            | **Platba mezi různými bankami** | Plátce má účet u jedné banky a příjemce u jiné banky[cite: 2]. Banka plátce musí poslat mezibankovní pokyn přes systém CERTIS[cite: 2]. | Ano[cite: 2]. Platba se vypořádá mezi bankami přes CERTIS[cite: 2]. |
            | **Okamžitá platba mezi různými bankami** | Pokud obě banky podporují okamžité platby, převod může proběhnout během několika sekund i mezi různými bankami[cite: 2]. | Ano, v režimu okamžitých plateb v rámci mezibankovního systému[cite: 2]. |
            """) #[cite: 2]

            st.write("**Příklad: spolužák ve stejné bance vs. spolužák v jiné bance:** Představ si, že posíláš 500 Kč za společný dárek[cite: 2].")
            st.markdown("""
            1. **Spolužák má účet u stejné banky:** Tvoje banka pouze upraví záznamy ve svém systému[cite: 2]. Tobě 500 Kč odečte a spolužákovi 500 Kč připíše[cite: 2]. Peníze nemusí „opustit“ banku[cite: 2].
            2. **Spolužák má účet u jiné banky:** Tvoje banka odešle pokyn do mezibankovního systému CERTIS[cite: 2]. Přes něj se platba vypořádá mezi bankami a banka spolužáka částku připíše na jeho účet[cite: 2].
            """)
            st.info("💡 **Jednoduše:** Když jsou oba účty ve stejné bance, banka si platbu vyřeší sama[cite: 2]. Když jsou účty v různých bankách, musí se banky mezi sebou „domluvit“ přes mezibankovní systém CERTIS spravovaný ČNB[cite: 2].")

        # 1.3.5
        with st.container(border=True):
            st.markdown("### 1.3.5 Jak probíhá platba kartou")
            st.write("Když přiložíš kartu nebo mobil k terminálu, vše vypadá jako jedna sekunda[cite: 2]. Ve skutečnosti se v pozadí odehraje několik kroků[cite: 2]:")
            st.markdown("""
            1. Terminál načte platební údaje[cite: 2].
            2. Obchodník pošle požadavek přes platební síť[cite: 2].
            3. Banka ověří kartu, limit, bezpečnostní pravidla a dostupné prostředky[cite: 2].
            4. Platba se autorizuje nebo zamítne[cite: 2].
            5. Později proběhne zúčtování mezi bankami a obchodníkem[cite: 2].
            """)

            st.markdown("""
            <div class='box-red'>
                🔐 <strong>Bezpečnost:</strong> U plateb se používají limity, PIN, biometrie, potvrzení v aplikaci, 3D Secure, monitoring podezřelých transakcí a další ochranné prvky[cite: 2]. Bezpečnost ale začíná i u uživatele: neklikat na podezřelé odkazy, nesdělovat kódy a chránit přístup do bankovnictví[cite: 2].
            </div>
            """, unsafe_allow_html=True)

            st.markdown("#### 🔁 Skládačka: Cesta platby kartou")
            st.write("Seřaď kroky platby kartou nebo mobilem ve správném pořadí[cite: 2]:")

            step_a = st.selectbox("1. krok procesoru:", ["Vyber...", "přiložení karty nebo mobilu k terminálu", "terminál načte platební údaje", "obchodník odešle požadavek přes platební síť", "banka ověří kartu, limit a bezpečnostní pravidla", "platba se schválí nebo zamítne", "později proběhne zúčtování mezi bankami a obchodníkem"], key="k2_step_a")
            step_b = st.selectbox("2. krok procesoru:", ["Vyber...", "přiložení karty nebo mobilu k terminálu", "terminál načte platební údaje", "obchodník odešle požadavek přes platební síť", "banka ověří kartu, limit a bezpečnostní pravidla", "platba se schválí nebo zamítne", "později proběhne zúčtování mezi bankami a obchodníkem"], key="k2_step_b")
            step_c = st.selectbox("3. krok procesoru:", ["Vyber...", "přiložení karty nebo mobilu k terminálu", "terminál načte platební údaje", "obchodník odešle požadavek přes platební síť", "banka ověří kartu, limit a bezpečnostní pravidla", "platba se schválí nebo zamítne", "později proběhne zúčtování mezi bankami a obchodníkem"], key="k2_step_c")
            step_d = st.selectbox("4. krok procesoru:", ["Vyber...", "přiložení karty nebo mobilu k terminálu", "terminál načte platební údaje", "obchodník odešle požadavek přes platební síť", "banka ověří kartu, limit a bezpečnostní pravidla", "platba se schválí nebo zamítne", "později proběhne zúčtování mezi bankami a obchodníkem"], key="k2_step_d")

            if st.button("Zkontrolovat řazení kroků", key="k2_card_seq_btn"):
                if step_a == "přiložení karty nebo mobilu k terminálu" and step_b == "terminál načte platební údaje" and step_c == "obchodník odešle požadavek přes platební síť" and step_d == "banka ověří kartu, limit a bezpečnostní pravidla":
                    st.success("🎉 Výborně! Kroky jsou ve správném technickém pořadí[cite: 2].")
                else:
                    st.error("Chyba v sekvenci. Zkontroluj si text v kapitole 1.3.5[cite: 2].")

        # 1.3.6
        with st.container(border=True):
            st.markdown("### 1.3.6 Digitální bezpečnost plateb")
            st.write("Nejčastější rizika[cite: 2]:")
            st.markdown("""
            * phishingové e-maily a SMS[cite: 2],
            * falešné stránky bank[cite: 2],
            * podvodné telefonáty „z banky“[cite: 2],
            * falešné investiční nabídky[cite: 2],
            * krádež přihlašovacích údajů[cite: 2],
            * zneužití platební karty[cite: 2],
            * tlak na rychlé rozhodnutí[cite: 2].
            """)

            st.markdown("""
            | Situace | Co dělat | Proč |
            | :--- | :--- | :--- |
            | Přijde SMS s odkazem na „blokaci účtu“ | Neotevírat odkaz, ověřit situaci přímo v aplikaci banky nebo na oficiální lince[cite: 2]. | Podvodníci často vytvářejí falešný pocit naléhavosti[cite: 2]. |
            | Někdo chce autorizační kód | Nikdy ho nesdělovat[cite: 2]. | Kód může potvrdit platbu nebo přístup k účtu[cite: 2]. |
            | Aplikace nabízí „garantované zhodnocení“ | Ověřit licenci, rizika a reálnost slibu[cite: 2]. | Vysoký výnos bez rizika je varovný signál[cite: 2]. |
            """) #[cite: 2]

            st.markdown("#### 🚨 Phishing escape room: nenech se okrást jedním klikem")
            st.write("Pro každou zprávu rozhodni, zda je bezpečná, podezřelá nebo nebezpečná[cite: 2]:")

            e1 = st.radio("1. „Vaše karta byla zablokována. Klikněte zde a ověřte účet.“", ["Bezpečná", "Nebezpečná / Phishing"], key="k2_e1")
            e2 = st.radio("2. „Jsem z bezpečnostního oddělení banky. Nadiktujte mi kód z SMS.“", ["Bezpečná", "Nebezpečná / Vishing"], key="k2_e2")
            e3 = st.radio("3. „Investice s garantovaným výnosem 30 % měsíčně.“", ["Bezpečná", "Nebezpečná / Podvod"], key="k2_e3")
            e4 = st.radio("4. „Potvrďte přístup do internetového bankovnictví přes tento odkaz v SMS.“", ["Bezpečná", "Nebezpečná / Phishing"], key="k2_e4")
            e5 = st.radio("5. E-shop nabízí uložení karty pro příští nákup.", ["Běžná funkce e-shopu (při známé bráně)", "Vždy podvod"], key="k2_e5")

            if st.button("Vyhodnotit Phishing Escape Room", key="k2_phish_btn"):
                if e1=="Nebezpečná / Phishing" and e2=="Nebezpečná / Vishing" and e3=="Nebezpečná / Podvod" and e4=="Nebezpečná / Phishing" and e5=="Běžná funkce e-shopu (při známé bráně)":
                    st.success("🎉 Unikl/a jsi všem pastem podvodníků! Pravidlo přežití: Banka po telefonu ani přes zprávu nechce heslo, PIN ani autorizační kód[cite: 2].")
                else:
                    st.error("Pozor! Zde byla chyba v rozpoznání rizikových zpráv[cite: 2]. Banka nikdy neposílá odkazy na odblokování účtu přes SMS[cite: 2]!")

    # =========================================================================
    # 1.4 FINTECH REVOLUCE
    # =========================================================================
    elif "1.4 Fintech" in selected_section_2:
        st.markdown("<div class='sub-section-header'>1. BANKOVNÍ SYSTÉM A PENÍZE V 21. STOLETÍ</div><h2>1.4 Fintech revoluce</h2>", unsafe_allow_html=True)
        st.write("Fintech je spojení slov **finance** a **technology**[cite: 2]. Označuje firmy a služby, které pomocí technologií mění způsob, jak platíme, spoříme, investujeme, půjčujeme si, ověřujeme identitu nebo spravujeme rozpočet[cite: 2].")

        with st.container(border=True):
            st.markdown("""
            <div class='box-blue'>
                🚀 <strong>Fintech změna:</strong> Finance se přesunuly z pobočky do mobilu[cite: 2]. Uživatel očekává rychlost, jednoduché ovládání, okamžité notifikace, nízké poplatky a možnost vyřídit vše online[cite: 2].
            </div>
            """, unsafe_allow_html=True)

        # 1.4.1
        with st.container(border=True):
            st.markdown("### 1.4.1 Co fintech přinesl")
            st.write("Fintech služby přinesly například[cite: 2]:")
            st.markdown("""
            * online založení účtu[cite: 2],
            * okamžité notifikace o platbách[cite: 2],
            * jednoduché investování malých částek[cite: 2],
            * levnější směnu měn[cite: 2],
            * virtuální platební karty[cite: 2],
            * rozpočtové aplikace[cite: 2],
            * propojení účtů z více bank[cite: 2],
            * platby mobilem a hodinkami[cite: 2],
            * QR platby[cite: 2],
            * rychlé online půjčky[cite: 2],
            * crowdfunding[cite: 2],
            * peer-to-peer platby[cite: 2],
            * digitální ověření identity[cite: 2],
            * automatické třídění výdajů[cite: 2].
            """)

        # 1.4.2
        with st.container(border=True):
            st.markdown("### 1.4.2 Neobanky a moderní finanční aplikace")
            st.write("Neobanky jsou bankovní nebo finanční služby stavěné hlavně pro mobilní prostředí[cite: 2]. Často nemají klasickou síť poboček a soutěží jednoduchostí aplikace, rychlostí a cenou[cite: 2]. Někdy jde o banku s bankovní licencí, jindy spíše o fintechovou platební aplikaci, která nabízí účet, kartu, směnu měn nebo další finanční služby[cite: 2].")

            st.markdown("""
            <div class='box-gray'>
                📱 <strong>Příklady neobank a digitálních finančních služeb dostupných v ČR:</strong><br><br>
                • <strong>Revolut</strong> — velmi známá mobilní finanční aplikace používaná pro účet, kartu, směnu měn, cestování, platby v zahraničí, investice nebo kryptoměny[cite: 2]. Pro studenty je dobrým příkladem „banky v mobilu“, i když je důležité rozlišovat, pod jakou licencí a ochranou služba funguje[cite: 2].<br><br>
                • <strong>Wise</strong> — služba zaměřená hlavně na levnější mezinárodní převody, víceměnový účet a platby v různých měnách[cite: 2]. Hodí se jako příklad fintechu, který řeší hlavně zahraniční platby a směnu měn[cite: 2].<br><br>
                • <strong>bunq</strong> — evropská digitální banka s důrazem na mobilní ovládání, více účtů, karty a práci s rozpočtem[cite: 2]. V ČR může být dostupná, ale není tak běžná jako klasické české banky[cite: 2].<br><br>
                • <strong>mBank</strong> — banka s výrazně digitálním modelem a menším důrazem na klasické pobočky[cite: 2]. V českém prostředí ji lze použít jako příklad banky, která se dlouhodobě opírá o online a mobilní bankovnictví[cite: 2].<br><br>
                • <strong>Air Bank</strong> — česká banka, která sice není čistá neobanka bez zázemí, ale často se uvádí jako příklad modernějšího, jednoduššího a digitálně orientovaného bankovnictví[cite: 2].
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class='box-red'>
                ⚠️ <strong>Pozor na pojem neobanka:</strong> Ne každá aplikace, která vypadá jako banka, je stejná jako klasická banka v ČR[cite: 2]. Liší se bankovní licence, pojištění vkladů, zákaznická podpora, poplatky, měny, ochrana klienta i to, kdo službu reguluje[cite: 2]. Před používáním je dobré zjistit: Kdo službu provozuje? Má bankovní licenci? Kde jsou pojištěné vklady? Jaké má poplatky a limity[cite: 2]?
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            | Klasické bankovnictví | Moderní fintech / neobanka |
            | :--- | :--- |
            | Důraz na pobočku a dlouhodobý vztah s bankou[cite: 2]. | Důraz na mobilní aplikaci a rychlé ovládání[cite: 2]. |
            | Služby se často řešily osobně nebo přes internetbanking[cite: 2]. | Mnoho služeb se vyřídí v telefonu během minut[cite: 2]. |
            | Poplatky a kurzovní marže nemusely být pro klienta přehledné[cite: 2]. | Aplikace často ukazuje poplatky, kurzy a transakce okamžitě[cite: 2]. |
            | Změny byly pomalejší[cite: 2]. | Nové funkce přibývají rychleji, ale uživatel musí víc hlídat rizika[cite: 2]. |
            """) #[cite: 2]

        # 1.4.3
        with st.container(border=True):
            st.markdown("### 1.4.3 Open banking: když si aplikace rozumí s bankou")
            st.write("Důležitou změnou je **open banking**[cite: 2]. Znamená, že klient může za určitých bezpečnostních podmínek povolit vybrané aplikaci přístup k informacím o účtu nebo zadání platby[cite: 2].")
            st.write("Příklady[cite: 2]:")
            st.markdown("""
            * jedna aplikace zobrazí zůstatky z více bank[cite: 2],
            * rozpočtová aplikace roztřídí výdaje[cite: 2],
            * účetní systém firmy si načte bankovní pohyby[cite: 2],
            * platba v e-shopu se zadá přímo z bankovního účtu[cite: 2].
            """)
            st.info("🔑 **Důležité:** Přístup k účtu má být vždy vědomý, omezený a odvolatelný[cite: 2]. Uživatel by měl vědět, komu dává souhlas, k čemu a na jak dlouho[cite: 2].")

        # 1.4.4
        with st.container(border=True):
            st.markdown("### 1.4.4 Rizika fintechu")
            st.write("Fintech není automaticky dobrý nebo špatný[cite: 2]. Je to nástroj[cite: 2]. Může pomoct, ale také zrychlit chybná rozhodnutí[cite: 2].")
            st.write("Rizika[cite: 2]:")
            st.markdown("""
            * příliš snadné utrácení[cite: 2],
            * rychlé půjčky bez promyšlení[cite: 2],
            * investování bez pochopení rizika[cite: 2],
            * falešné aplikace[cite: 2],
            * sdílení dat s neověřenými službami[cite: 2],
            * závislost na telefonu a notifikacích[cite: 2],
            * dojem, že „když je to v aplikaci, je to bezpečné“[cite: 2].
            """)
            st.markdown("""
            <div class='box-purple'>
                🧠 <strong>Finanční gramotnost dnes:</strong> Nestačí vědět, co je úrok[cite: 2]. Je potřeba umět poznat, kdy aplikace tlačí na rychlost, emoce nebo FOMO[cite: 2]. Digitální pohodlí musí jít ruku v ruce s kritickým myšlením[cite: 2].
            </div>
            """, unsafe_allow_html=True)

        # 1.4.5
        with st.container(border=True):
            st.markdown("### 1.4.5 Jak poznat důvěryhodnou finanční službu")
            st.write("Před použitím nové finanční aplikace je dobré zkontrolovat[cite: 2]:")
            st.markdown("""
            * kdo službu provozuje[cite: 2],
            * zda má potřebné oprávnění nebo dohled[cite: 2],
            * jak vydělává[cite: 2],
            * jaké má poplatky[cite: 2],
            * jak nakládá s daty[cite: 2],
            * zda slibuje nereálně vysoké výnosy[cite: 2],
            * jak lze službu zrušit[cite: 2],
            * zda má srozumitelné podmínky[cite: 2].
            """)

            st.markdown("#### 📱 Audit finanční aplikace")
            st.write("Vyber jednu službu nebo aplikaci: Revolut, Wise, PayPal, Apple Pay, Google Pay, bankovní aplikaci, investiční aplikaci, rozpočtovou aplikaci nebo službu typu „kup teď, zaplať později“[cite: 2].")

            audit_app_name = st.text_input("1. Název vybrané aplikace/služby:", key="k2_fintech_app_name")
            audit_owner = st.text_input("2. Kdo ji provozuje:", key="k2_fintech_owner")
            audit_features = st.text_area("3. Co uživateli umožňuje:", key="k2_fintech_feat")
            audit_revenue = st.text_area("4. Jak vydělává a jaké má poplatky:", key="k2_fintech_rev")
            audit_data = st.text_area("5. Jaká data po uživateli vyžaduje:", key="k2_fintech_data")
            audit_pros_cons = st.text_area("6. Hlavní výhody a hlavní rizika:", key="k2_fintech_pc")
            audit_rec_text = st.radio("7. Doporučení spolužákovi:", ["Doporučil/a bych (s obezřetností)", "Nedoporučil/a bych (vysoká rizika/poplatky)"], key="k2_fintech_rec")

            if st.button("Uložit audit aplikace", key="k2_save_fintech_audit"):
                st.success(f"Audit aplikace **{audit_app_name}** byl úspěšně zaznamenán[cite: 2]!")

            st.markdown("---")

            st.markdown("#### ⚖️ Debata: Fintech — pomocník, nebo past?")
            st.write("Dva pohledy na fintech v dnešním světě[cite: 2]:")
            
            col_deb1, col_deb2 = st.columns(2)
            with col_deb1:
                st.success("💚 **Tým A (Pomocník):**\nFintech zvyšuje finanční gramotnost, šetří čas, snižuje poplatky za převody a směnu a umožňuje snadnou kontrolu rozpočtu[cite: 2].")
            with col_deb2:
                st.error("🔴 **Tým B (Past):**\nFintech zrychluje impulzivní utrácení, zjednodušuje neuvážené zadlužování, využívá gamifikaci k investičnímu riziku a sbírá osobní data[cite: 2].")

            st.text_area("Napiš svůj vlastní názor a alespoň 1 konkrétní příklad ze života:", key="k2_deb_opinion")
