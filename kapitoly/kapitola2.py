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

    # 📌 JEDNOTNÁ NABÍDKA PODKAPITOL (1.1 AŽ 3.10)
    section_options_2 = [
        # Sekce 1: Bankovní systém
        "1.1 Peníze jako digitální data",
        "1.2 ČNB a komerční banky",
        "1.3 Platební styk",
        "1.4 Fintech revoluce",
        
        # Sekce 2: Osobní finance
        "2.1 Osobní finance v 21. století",
        "2.2 Rozpočet: mapa peněz",
        "2.3 Algoritmy bohatství",
        "2.4 Matematika peněz (úročení a inflace)",
        "2.5 Finanční rezerva",
        "2.6 Psychologie utrácení",
        "2.7 Kalkulačka času nákupu",
        "2.8 Osobní finanční audit",
        
        # Sekce 3: Finanční trh
        "3.1 Co je to finanční trh a burza",
        "3.2 Výnos, riziko, likvidita a časový horizont",
        "3.3 Spoření, investování a spekulace",
        "3.4 Cenné papíry v teorii i praxi",
        "3.5 Analýza dat a Školní investiční simulátor",
        "3.6 Kryptoměny: technologie, spekulace a riziko",
        "3.7 Ochrana spotřebitele a investiční reklama",
        "3.8 Interaktivní aktivity a cvičebnice",
        "3.9 Shrnutí: Co si z finančního trhu odnést",
        "3.10 Právní a etický disclaimer"
    ]
    
    selected_section_2 = st.selectbox("📌 Přechod na podkapitolu:", section_options_2, index=0)
    st.divider()

    # Následuje blok podmínek: if "1.1 Peníze" in selected_section_2: ...

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

        # 1.2.1 Postavení ČNB v ČR
        with st.container(border=True):
            st.markdown("### 1.2.1 Postavení ČNB v České republice")
            st.write("Česká národní banka je centrální banka České republiky. Její postavení je zakotveno v právním řádu ČR a její činnost upravuje zejména zákon o České národní bance. ČNB je veřejnoprávní instituce se zvláštním postavením: není komerční firmou, neusiluje o zisk jako běžný podnik a neposkytuje běžné bankovní služby občanům.")
            
            st.markdown("""
            <div class='box-gray'>
                ⚖️ <strong>Důležité:</strong> ČNB je při plnění svých hlavních úkolů nezávislá. To znamená, že vláda jí nemá diktovat, jak má nastavovat úrokové sazby nebo měnovou politiku. Smyslem nezávislosti je chránit stabilitu měny a finančního systému před krátkodobým politickým tlakem.
            </div>
            """, unsafe_allow_html=True)

            st.write("ČNB sídlí v Praze a působí pro celou Českou republiku. Je součástí Evropského systému centrálních bank, protože Česká republika je členem Evropské unie. Dokud ale ČR nepřijme euro, ČNB provádí vlastní měnovou politiku pro českou korunu.")

            with st.expander("🇪🇺 ČNB a euro: proč je česká situace trochu jiná"):
                st.write("To, že má Česká republika vlastní měnu (korunu) a vlastní centrální banku, která samostatně nastavuje měnovou politiku, není v Evropské unii u všech států běžné. Mnoho členských zemí EU už přijalo euro a patří do eurozóny. V těchto zemích nerozhoduje o hlavních úrokových sazbách jejich národní centrální banka samostatně, ale společně systém vedený Evropskou centrální bankou (ECB).")
                st.write("**Příklad:** Slovensko přijalo euro v roce 2009. Národní banka Slovenska dál existuje, ale už nevydává vlastní slovenskou korunu a samostatně neurčuje měnovou politiku pro vlastní měnu. Podílí se na fungování eurozóny, dohledu a finanční stabilitě, ale hlavní měnová politika se řeší na evropské úrovni přes ECB.")
                st.write("**Jak by to fungovalo po přijetí eura v ČR:** Česká koruna by byla nahrazena eurem. ČNB by nezanikla, ale změnila by se její role. Dál by působila jako národní centrální banka, dohlížela by na finanční trh, pečovala o hotovostní oběh eura v ČR, podílela se na finanční stabilitě a byla by součástí Eurosystému. O hlavních úrokových sazbách pro eurozónu by se ale rozhodovalo společně v rámci ECB, nikoli samostatně jen podle české ekonomiky.")
                st.write("**Konkrétní modelový příklad rozdílu:** Představ si, že v Česku je inflace vyšší než v eurozóně a česká ekonomika potřebuje brzdit zdražování. Pokud má ČR vlastní korunu, může ČNB zvýšit úrokové sazby výrazněji — například na 6–7 %. Tím zdraží úvěry, hypotéky i půjčky, ale zároveň podpoří spoření a může pomoci tlumit inflaci. Pokud by ČR už platila eurem, sazby by se nastavovaly pro celou eurozónu. ECB by se dívala na průměrnou situaci mnoha zemí, například Německa, Francie, Itálie, Slovenska nebo Španělska. Kdyby eurozóna jako celek potřebovala mírnější politiku, mohly by být sazby třeba jen 3–4 %, i když by Česku samostatně vyhovovaly vyšší sazby.")
                st.write("**Co by to znamenalo v běžném životě:** Po přijetí eura by úrokové sazby v ČR mohly být v některých obdobích nižší, než jaké by nastavila samostatná ČNB. To by mohlo zlevnit hypotéky a úvěry, ale zároveň by to mohlo méně brzdit inflaci, pokud by české ceny rostly rychleji než v eurozóně. Výhoda eura je větší měnová stabilita a jednodušší obchodování v eurozóně. Nevýhoda je menší možnost přizpůsobit měnovou politiku jen české ekonomice.")
                
                euro_sim = st.radio("Zvol simulovaný režim při vysoké české inflaci:", [
                    "Vlastní měna (CZK) — ČNB zvýší sazby na 7 %",
                    "Společné Euro (EUR) — ECB drží sazby na 3,5 %"
                ], key="k2_1_2_1_euro_sim")
                if "CZK" in euro_sim:
                    st.success("✅ **Samostatná ČNB:** Vyšší sazby zdraží úvěry a hypotéky v ČR, ale účinněji tlumí inflaci a chrání úspory.")
                else:
                    st.warning("⚠️ **Společné Euro (ECB):** Zůstávají levnější úvěry, ale inflace v ČR může trvat déle a více znehodnocovat kupní sílu.")

        # 1.2.2 Hlavní cíl ČNB
        with st.container(border=True):
            st.markdown("### 1.2.2 Hlavní cíl ČNB")
            st.write("Hlavním cílem ČNB je péče o cenovou stabilitu. Jinými slovy: ČNB se snaží, aby peníze neztrácely hodnotu příliš rychle a aby inflace nebyla dlouhodobě příliš vysoká ani nebezpečně nízká.")
            
            st.markdown("""
            <div class='box-gray'>
                🎯 <strong>Cenová stabilita jednoduše:</strong> Neznamená, že se nikdy nic nezdraží. Znamená, že růst cen má být dlouhodobě předvídatelný a zvládnutelný. Když je inflace příliš vysoká, lidem klesá kupní síla, firmám se hůř plánuje a ekonomika ztrácí stabilitu.
            </div>
            """, unsafe_allow_html=True)
            st.write("ČNB v praxi používá inflační cílování. To znamená, že sleduje vývoj inflace a nastavuje nástroje měnové politiky tak, aby se inflace ve střednědobém horizontu pohybovala kolem stanoveného cíle.")

            st.markdown("#### 🎮 Interaktivní simulace: Jsi bankovní rada ČNB")
            st.write("**Situace:** Inflace je vysoká, lidé si stěžují na zdražování, hypotéky jsou drahé a firmy říkají, že zákazníci méně utrácejí. Tvoje skupina představuje bankovní radu ČNB.")
            
            c_rada_action = st.radio("Rozhodněte o sazbách:", [
                "zvýšíte úrokové sazby",
                "snížíte úrokové sazby",
                "ponecháte sazby beze změny",
                "použijete komunikaci směrem k veřejnosti",
                "budete zvažovat devizové intervence"
            ], key="k2_1_2_2_rada_act")

            st.write("**Musíte zdůvodnit:**")
            q1 = st.text_input("1. Co se stane s úvěry?", key="k2_q1_uvery")
            q2 = st.text_input("2. Co se stane se spořením?", key="k2_q2_sporeni")
            q3 = st.text_input("3. Jaký může být dopad na inflaci?", key="k2_q3_inflace")
            q4 = st.text_input("4. Komu vaše rozhodnutí pomůže a komu může zkomplikovat život?", key="k2_q4_komu")
            q5 = st.text_input("5. Jaké riziko vznikne, pokud se rozhodnete špatně?", key="k2_q5_riziko")

            if st.button("Výstup: Jedna minuta tiskové konference", key="k2_1_2_2_rada_btn"):
                st.markdown(f"**Tiskové prohlášení Bankovní rady:** „ČNB dnes rozhodla, že {c_rada_action}...“")

        # 1.2.3 Co přesně ČNB dělá
        with st.container(border=True):
            st.markdown("### 1.2.3 Co přesně ČNB dělá")
            st.write("ČNB má několik klíčových funkčních oblastí. Každá z nich se týká jiné části ekonomiky, ale dohromady tvoří systém důvěry v peníze.")

            st.markdown("""
            | Funkce ČNB | Co to znamená | Příklad dopadu na běžný život |
            | :--- | :--- | :--- |
            | **Měnová politika** | Nastavuje podmínky pro hodnotu peněz, hlavně pomocí úrokových sazeb. | Ovlivňuje úroky u hypoték, spoření i úvěrů. |
            | **Emise hotovosti** | Vydává bankovky a mince české koruny a pečuje o jejich oběh. | Určuje, jaké bankovky a mince platí a jak vypadají. |
            | **Dohled nad finančním trhem** | Dohlíží na banky, pojišťovny, družstevní záložny, penzijní společnosti, investiční společnosti a další finanční instituce. | Hlídá, aby instituce dodržovaly pravidla a neohrožovaly klienty ani systém. |
            | **Finanční stabilita** | Sleduje rizika, která by mohla ohrozit celý finanční systém. | Řeší například, zda banky mají dost kapitálu a nejsou příliš rizikové. |
            | **Platební systémy** | Provozuje a dohlíží na důležité platební a zúčtovací systémy. | Pomáhá tomu, aby převody mezi bankami fungovaly bezpečně a spolehlivě. |
            | **Správa devizových rezerv** | Spravuje zásoby zahraničních měn a dalších aktiv státu. | Pomáhá stabilitě měny a důvěře v ekonomiku. |
            | **Banka státu** | Vede účty státu a poskytuje vybrané služby veřejnému sektoru. | Souvisí s pohybem peněz státu, například při placení výdajů veřejných institucí. |
            """)

        # 1.2.4 Hotovost a ochranné prvky
        with st.container(border=True):
            st.markdown("### 1.2.4 Hotovost, ochranné prvky bankovek a důvěra v peníze")
            st.write("Jednou z viditelných činností ČNB je péče o hotovostní oběh. ČNB vydává české bankovky a mince, stahuje z oběhu poškozené nebo neplatné peníze a stará se o to, aby hotovost byla důvěryhodná. Právě sem patří také ochranné prvky bankovek.")
            st.write("Bankovky mají ochranné prvky proto, aby bylo možné ověřit jejich pravost a snížit riziko padělání. Nejde jen o „ozdobu“ bankovky. Ochranné prvky pomáhají běžným lidem, obchodníkům, bankám i státu poznat, zda je bankovka skutečná a zda jí mohou důvěřovat.")

            st.markdown("""
            <div class='box-gray'>
                🛡️ <strong>Proč ochranné prvky patří k tématu ČNB?</strong><br>
                ČNB odpovídá za českou měnu a hotovostní oběh. Pokud by bylo snadné bankovky padělat, lidé i obchody by se báli hotovost přijímat. Ochranné prvky proto chrání důvěru v peníze, ztěžují padělání a umožňují rychlou kontrolu pravosti při běžném placení.
            </div>
            """, unsafe_allow_html=True)

            st.write("Ochranné prvky můžeme rozdělit podle toho, jak je člověk kontroluje:")
            st.markdown("""
            * **pohledem** — například vodoznak, ochranný proužek, soutisková značka nebo proměnlivá barva,
            * **hmatem** — například speciální papír a reliéfní tisk,
            * **naklopením bankovky** — například opticky proměnlivé prvky,
            * **pomůckami** — například kontrola pod UV světlem.
            """)

            st.markdown("##### 🔎 Interaktivní aktivita: Ochranné prvky peněz")
            st.write("Prohlédni si bankovku a najdi její ochranné prvky:")
            
            p_sel = st.selectbox("Zvol ochranný prvek pro zobrazení popisu:", [
                "Vodoznak (pohledem)",
                "Ochranný proužek s mikrotextem (pohledem)",
                "Reliéfní tisk (hmatem)",
                "Opticky proměnlivá barva (naklopením)",
                "Soutisková značka (pohledem)",
                "UV prvky (pomůckami)"
            ], key="k2_1_2_4_bankovka_sel")

            if "Vodoznak" in p_sel:
                st.info("💧 **Vodoznak:** Zřetelný portrét osobnosti viditelný z obou stran při pohledu proti světlu v nepotištěném okraji.")
            elif "Ochranný proužek" in p_sel:
                st.info("📏 **Ochranný proužek:** Tmavý souvislý pás s negativním mikrotextem nominální hodnoty viditelný proti světlu.")
            elif "Reliéfní tisk" in p_sel:
                st.info("🖐️ **Reliéfní tisk:** Vystoupený povrch hlubotisku nahmatatelný na lícové straně.")
            elif "Opticky proměnlivá barva" in p_sel:
                st.info("🎨 **Opticky proměnlivá barva:** Mění barvu při naklonění bankovky (např. ze zelené na zlatou).")
            elif "Soutisková značka" in p_sel:
                st.info("🧩 **Soutisková značka:** Oboustranný tisk, který se proti světlu přesně doplňuje v celistvý symbol.")
            else:
                st.info("🔦 **UV prvky:** Svítící vlákna a tiskové motivy viditelné pod UV lampou.")

        # 1.2.5 Kdo ČNB řídí
        with st.container(border=True):
            st.markdown("### 1.2.5 Kdo ČNB řídí")
            st.write("Nejvyšším řídicím orgánem ČNB je **bankovní rada**. Ta rozhoduje například o měnové politice, úrokových sazbách a dalších zásadních otázkách fungování ČNB.")
            st.write("Bankovní rada má **sedm členů**:")
            st.markdown("""
            * guvernér,
            * dva viceguvernéři,
            * čtyři další členové bankovní rady.
            """)
            st.write("Členy bankovní rady jmenuje prezident republiky. V čele ČNB stojí guvernér. Guvernér reprezentuje ČNB navenek a řídí jednání bankovní rady. V současnosti je guvernérem ČNB Aleš Michl.")
            
            st.markdown("""
            <div class='box-gray'>
                🧭 <strong>Jak si to představit:</strong> Bankovní rada je jako „řídicí tým“ centrální banky. Nerozhoduje o tom, komu banka dá spotřebitelský úvěr. Rozhoduje o pravidlech a nastavení systému, který ovlivňuje všechny banky a celou ekonomiku.
            </div>
            """, unsafe_allow_html=True)

        # 1.2.6 Jak ČNB zasahuje do ekonomiky
        with st.container(border=True):
            st.markdown("### 1.2.6 Jak ČNB zasahuje do ekonomiky")
            st.write("ČNB neřídí ekonomiku příkazem typu „zdražte“ nebo „zlevněte“. Ovlivňuje ekonomiku hlavně nepřímo — přes cenu peněz, důvěru a pravidla finančního trhu.")
            st.write("Nejdůležitější nástroje jsou:")
            st.markdown("""
            * **úrokové sazby** — když ČNB sazby zvýší, úvěry bývají dražší a spoření atraktivnější; když sazby sníží, úvěry mohou zlevnit a ekonomická aktivita se může podpořit,
            * **operace na finančním trhu** — ČNB může stahovat nebo dodávat likviditu bankovnímu systému,
            * **povinné minimální rezervy** — banky musí držet část prostředků u centrální banky,
            * **devizové intervence** — ve výjimečných situacích může ČNB nakupovat nebo prodávat měny a tím ovlivňovat kurz koruny,
            * **makroobezřetnostní politika** — ČNB může nastavovat pravidla, která mají zabránit nadměrnému zadlužování a přehřívání finančního trhu,
            * **dohled a regulace** — kontroluje, zda finanční instituce dodržují pravidla a mají dostatečnou odolnost.
            """)

            st.markdown("""
            <div class='box-gray'>
                🧰 <strong>Hlavní nástroje ČNB:</strong> ČNB používá hlavně nástroje měnové politiky, nástroje pro řízení likvidity bankovního systému, devizové nástroje, dohledové nástroje a makroobezřetnostní pravidla. Nejde o jeden „kouzelný knoflík“, ale o kombinaci opatření, která ovlivňují cenu peněz, množství peněz v oběhu, chování bank a stabilitu finančního systému.
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            | Nástroj ČNB | Jak funguje | Co ovlivňuje |
            | :--- | :--- | :--- |
            | **Základní úrokové sazby** | ČNB nastavuje sazby, za kterých si banky ukládají peníze u ČNB nebo si od ní krátkodobě půjčují. Nejsledovanější je dvoutýdenní repo sazba. | Cenu úvěrů, výnosnost spoření, kurz koruny, inflaci a ochotu domácností i firem utrácet nebo investovat. |
            | **Repo operace** | ČNB pomocí obchodů s bankami stahuje nebo dodává peníze do bankovního systému. V české praxi často stahuje přebytečnou likviditu. | Množství dostupných peněz v bankovním systému a krátkodobé tržní úrokové sazby. |
            | **Diskontní sazba** | Sazba spojená s možností bank uložit přebytečné prostředky u ČNB. | Spodní hranici krátkodobých sazeb na peněžním trhu. |
            | **Lombardní sazba** | Sazba, za kterou si banky mohou půjčit od ČNB proti zástavě cenných papírů. | Horní hranici krátkodobých sazeb a nouzové krátkodobé financování bank. |
            | **Povinné minimální rezervy** | Banky musí držet určitou část vkladů u ČNB. | Likviditu bank a stabilitu bankovního systému. |
            | **Devizové intervence** | ČNB může nakupovat nebo prodávat zahraniční měny, aby ovlivnila kurz koruny. | Kurz koruny, dovozní ceny, export, inflaci a očekávání na finančním trhu. |
            | **Devizové rezervy** | ČNB spravuje aktiva v zahraničních měnách. | Důvěru v měnu, schopnost zasáhnout na devizovém trhu a finanční stabilitu. |
            | **Makroobezřetnostní limity** | ČNB může nastavovat pravidla pro bezpečnější úvěrování, například u hypoték sleduje vztah výše úvěru k hodnotě nemovitosti nebo příjmům žadatele. | Zadlužení domácností, stabilitu bank a riziko cenových bublin. |
            | **Kapitálové požadavky na banky**| Banky musí mít dost vlastního kapitálu, aby zvládly ztráty. | Odolnost bank při krizi a ochranu finančního systému. |
            | **Dohled a sankce** | ČNB kontroluje finanční instituce, může požadovat nápravu nebo uložit sankce. | Dodržování pravidel, ochranu klientů a důvěru ve finanční trh. |
            """)

            st.markdown("##### Repo sazba lidsky")
            st.write("Když média říkají, že „ČNB zvýšila sazby“, často mluví hlavně o repo sazbě. Ta je důležitým signálem pro celý finanční trh. Banky podle ní upravují vlastní sazby u úvěrů a vkladů. Neznamená to, že se hypotéka nebo spořicí účet změní přes noc stejně u všech bank, ale směr rozhodnutí ČNB se do bankovních produktů postupně promítá.")

            st.markdown("#### 🧮 Mini kalkulačka: Repo sazba v praxi")
            st.write("Porovnej dvě situace:")
            st.markdown("""
            | Situace | Spoření | Úvěry | Typický dopad |
            | :--- | :--- | :--- | :--- |
            | **Nižší sazby** | nižší výnos | levnější půjčky | větší chuť utrácet a investovat |
            | **Vyšší sazby** | vyšší výnos | dražší půjčky | větší motivace spořit, menší chuť se zadlužovat |
            """)

            st.write("**Úkol:** Vyber částku 20 000 Kč na spořicím účtu a půjčku 100 000 Kč. Spočítej orientačně, jak se změní roční úrok při sazbě 3 %, 5 % a 7 %:")
            
            c_sazba = st.select_slider("Zvol úrokovou sazbu:", options=[3.0, 5.0, 7.0], value=5.0, key="k2_exact_repo_slider")
            
            calc_vynos = 20000 * (c_sazba / 100)
            calc_urok = 100000 * (c_sazba / 100)

            res_c1, res_c2 = st.columns(2)
            res_c1.metric("Roční výnos ze spoření (20 000 Kč)", f"{calc_vynos:,.0f} Kč".replace(",", " "))
            res_c2.metric("Roční úrok z půjčky (100 000 Kč)", f"{calc_urok:,.0f} Kč".replace(",", " "))

            st.text_area("Potom napiš krátký komentář: Proč stejné rozhodnutí ČNB může někomu pomoci a jinému uškodit?", key="k2_repo_koment")

            st.write("**Příklad: co se stane, když ČNB zvýší úrokové sazby?** Vyšší sazby obvykle zdražují půjčky. Domácnosti a firmy si proto mohou méně půjčovat a méně utrácet. Zároveň může být výhodnější spořit. Tlak na růst cen se tím může snížit. Nevýhodou je, že dražší úvěry mohou zpomalit investice firem, hypotéky nebo spotřebu.")

            st.markdown("#### 🧮 Simulace: Vyšší sazby, inflace a hypotéka")
            st.write("Situace: ČNB drží měnovou politiku přísnější, aby brzdila inflaci. V roce 2026 byla repo sazba ČNB kolem 3,5 %, průměrné hypoteční sazby se u nových hypoték pohybovaly přibližně okolo 5 % p.a. a nižší inflaci budeme v modelu počítat jako 2 %, protože přibližně kolem této hodnoty se pohybujeme v dlouhodobém inflačním cíli ČNB.")
            st.write("Aby to bylo na první pohled: Porovnáme jednu domácnost ve dvou světech. V obou světech má stejnou hypotéku 3 000 000 Kč na 25 let a stejné běžné měsíční výdaje 40 000 Kč bez hypotéky. Liší se jen úroky a inflace.")

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
                """)

            st.markdown("""
            | Modelový svět | Hypotéka | Inflace a běžné výdaje | Co domácnost pocítí za měsíc |
            | :--- | :--- | :--- | :--- |
            | **Levné úvěry, ale vyšší inflace** | úrok 2,5 % → splátka cca 13 500 Kč | inflace 5 % → koš 40 000 Kč zdraží zhruba o 2 000 Kč za měsíc | nižší splátka, ale dražší nákupy |
            | **Dražší úvěry, ale nižší inflace** | úrok 5 % → splátka cca 17 500 Kč | inflace 2 % → koš 40 000 Kč zdraží zhruba o 800 Kč za měsíc | vyšší splátka, ale pomalejší zdražování |
            | **Rozdíl** | hypotéka je dražší asi o 4 000 Kč měsíčně | běžné výdaje rostou asi o 1 200 Kč měsíčně méně | domácnost s hypotékou je v tomto modelu pořád asi 2 800 Kč měsíčně v mínusu |
            """)

            st.write("**Jednoduchý závěr pro žáka:** Pokud má domácnost velkou hypotéku, vyšší sazby ji bolí hned a velmi viditelně. Nižší inflace jí sice pomáhá, protože nákupy nezdražují tak rychle, ale v tomto modelu to nestačí vyrovnat dražší hypotéku. Proto lidé často reagují na vysoké sazby jako na „červenou na býka“ — splátka úvěru je jedna konkrétní částka na účtu, zatímco přínos nižší inflace je rozptýlený v cenách mnoha nákupů.")
            st.write("**Pozor:** To neznamená, že vyšší sazby jsou zbytečné. Pomáhají brzdit inflaci v celé ekonomice, chránit hodnotu mezd a úspor a bránit tomu, aby se zdražování utrhlo z řetězu. Jen je potřeba rozlišit pohled celé ekonomiky a pohled konkrétní zadlužené domácnosti.")

            st.write("**Příklad: co se stane, když ČNB sníží úrokové sazby?** Nižší sazby mohou zlevnit úvěry a podpořit spotřebu i investice. Lidé a firmy si mohou snadněji půjčovat. Pokud je ale ekonomika už přehřátá, příliš levné peníze mohou podporovat inflaci nebo vznik cenových bublin, například na trhu nemovitostí.")

        # 1.2.7 Koho a co ČNB řídí
        with st.container(border=True):
            st.markdown("### 1.2.7 Koho a co ČNB „řídí“ a koho ne")
            st.write("ČNB neřídí osobní účty občanů a neurčuje jednotlivým lidem, kolik si mohou půjčit. Neřídí ani každodenní obchodní rozhodnutí komerčních bank. Má ale silný vliv na pravidla a prostředí, ve kterém banky a další finanční instituce fungují.")
            st.write("ČNB zejména:")
            st.markdown("""
            * uděluje vybraným finančním institucím povolení k činnosti,
            * dohlíží na banky a další finanční instituce,
            * může ukládat nápravná opatření nebo sankce,
            * nastavuje některá pravidla pro stabilitu bankovního sektoru,
            * provozuje důležité platební systémy,
            * vydává hotovost,
            * ovlivňuje cenu peněz v ekonomice.
            """)

            st.markdown("""
            <div class='box-red'>
                ⚠️ <strong>Pozor na častý omyl:</strong> ČNB není „nadřízená pobočka“ tvojí banky, která řeší každou reklamaci platební karty. Reklamaci řeší nejdříve tvoje banka. ČNB ale dohlíží na to, aby finanční instituce dodržovaly pravidla.
            </div>
            """, unsafe_allow_html=True)

            st.markdown("#### 🧩 Třídicí hra: ČNB, nebo komerční banka?")
            st.write("Rozděl výroky do tří skupin: ČNB, komerční banka, souvisí s oběma:")

            v1 = st.selectbox("1. vydává bankovky a mince:", ["Vyber...", "ČNB", "Komerční banka", "Souvisí s oběma"], key="k2_v1")
            v2 = st.selectbox("2. vede běžný účet:", ["Vyber...", "ČNB", "Komerční banka", "Souvisí s oběma"], key="k2_v2")
            v3 = st.selectbox("3. poskytuje hypotéku:", ["Vyber...", "ČNB", "Komerční banka", "Souvisí s oběma"], key="k2_v3")
            v4 = st.selectbox("4. nastavuje základní úrokové sazby:", ["Vyber...", "ČNB", "Komerční banka", "Souvisí s oběma"], key="k2_v4")
            v5 = st.selectbox("5. vydává platební kartu:", ["Vyber...", "ČNB", "Komerční banka", "Souvisí s oběma"], key="k2_v5")
            v6 = st.selectbox("6. dohlíží na banky:", ["Vyber...", "ČNB", "Komerční banka", "Souvisí s oběma"], key="k2_v6")
            v7 = st.selectbox("7. spravuje devizové rezervy:", ["Vyber...", "ČNB", "Komerční banka", "Souvisí s oběma"], key="k2_v7")
            v8 = st.selectbox("8. umožňuje platbu mobilem:", ["Vyber...", "ČNB", "Komerční banka", "Souvisí s oběma"], key="k2_v8")
            v9 = st.selectbox("9. podílí se na důvěře ve finanční systém:", ["Vyber...", "ČNB", "Komerční banka", "Souvisí s oběma"], key="k2_v9")
            v10 = st.selectbox("10. souvisí s platebním stykem:", ["Vyber...", "ČNB", "Komerční banka", "Souvisí s oběma"], key="k2_v10")

            st.text_area("Bonus: U každého výroku vysvětli, jak se dotýká běžného života:", key="k2_v_bonus")

            if st.button("Vyhodnotit třídicí hru", key="k2_v_eval_btn"):
                if v1=="ČNB" and v2=="Komerční banka" and v3=="Komerční banka" and v4=="ČNB" and v5=="Komerční banka" and v6=="ČNB" and v7=="ČNB" and v8=="Komerční banka" and v9=="Souvisí s oběma" and v10=="Souvisí s oběma":
                    st.success("🎉 Skvělé! Všechny položky jsi zařadil/a přesně podle textu.")
                else:
                    st.error("Některé položky nejsou zařazeny správně. Zkontroluj si zařazení!")

        # 1.2.8 Komerční banky
        with st.container(border=True):
            st.markdown("### 1.2.8 Komerční banky: banky pro občany a firmy")
            st.write("Komerční banky jsou finanční instituce, které podnikají na finančním trhu. Jejich hlavní činností je přijímat vklady, poskytovat úvěry a zprostředkovávat platební styk. Potřebují bankovní licenci a podléhají dohledu ČNB.")
            
            st.markdown("""
            <div class='box-blue'>
                🏧 <strong>Komerční banka v jedné větě:</strong> Přijímá peníze od klientů, vede jim účty, umožňuje platby a část získaných zdrojů půjčuje jiným klientům formou úvěrů.
            </div>
            """, unsafe_allow_html=True)
            st.write("Komerční banky jsou obchodní společnosti. Řídí je jejich vlastní orgány, například představenstvo a management banky, a kontrolují je vlastníci, dozorčí orgány, auditoři a regulátor. Zároveň musí dodržovat zákony, pravidla kapitálové přiměřenosti, pravidla proti praní špinavých peněz, pravidla ochrany spotřebitele a další regulaci.")

        # 1.2.9 Co poskytují občanům
        with st.container(border=True):
            st.markdown("### 1.2.9 Co komerční banky poskytují občanům")
            st.write("Pro běžného člověka je banka hlavně místem, kde se spravují každodenní peníze. Banka může poskytovat například:")
            st.markdown("""
            * běžný účet,
            * spořicí účet,
            * termínovaný vklad,
            * platební kartu,
            * internetové a mobilní bankovnictví,
            * tuzemské i zahraniční platby,
            * trvalé příkazy a inkasa,
            * hotovostní služby,
            * spotřebitelský úvěr,
            * kontokorent,
            * kreditní kartu,
            * hypotéku,
            * směnu měn,
            * investiční produkty nebo jejich zprostředkování,
            * pojištění nebo jeho zprostředkování,
            * bezpečnostní nástroje, například limity plateb, 3D Secure nebo potvrzování v aplikaci.
            """)

            st.markdown("""
            <div class='box-purple'>
                📱 <strong>Moderní realita:</strong> Pro mnoho mladých lidí už banka není pobočka. Je to aplikace, ve které vidí zůstatek, platí mobilem, nastavují limity, blokují kartu, kontrolují předplatná a posílají peníze přes QR kód.
            </div>
            """, unsafe_allow_html=True)

        # 1.2.10 Co poskytují firmám
        with st.container(border=True):
            st.markdown("### 1.2.10 Co komerční banky poskytují firmám")
            st.write("Firmy potřebují banky nejen k placení faktur. Banky jim pomáhají financovat provoz, investice a obchod.")
            st.write("Firmám banky poskytují například:")
            st.markdown("""
            * podnikatelské účty,
            * platební terminály,
            * provozní úvěry,
            * investiční úvěry,
            * kontokorentní financování,
            * bankovní záruky,
            * dokumentární platby v mezinárodním obchodě,
            * směnárenské a devizové služby,
            * správu likvidity,
            * financování exportu,
            * firemní platební karty.
            """)

        # 1.2.11 Aktivní, pasivní a neutrální operace
        with st.container(border=True):
            st.markdown("### 1.2.11 Aktivní, pasivní a neutrální operace bank")
            st.write("Činnosti komerčních bank se často rozdělují na pasivní, aktivní a neutrální operace.")

            st.markdown("""
            | Typ operace | Co znamená | Příklady |
            | :--- | :--- | :--- |
            | **Pasivní operace** | Banka získává zdroje. Z pohledu banky jde o závazky vůči klientům nebo investorům. | běžné účty, spořicí účty, termínované vklady, vydané bankovní dluhopisy, přijaté mezibankovní úvěry |
            | **Aktivní operace** | Banka peníze umísťuje tak, aby vydělávala. Z pohledu banky jde o aktiva. | spotřebitelské úvěry, hypotéky, podnikatelské úvěry, kontokorenty, kreditní karty, nákup cenných papírů, mezibankovní úvěry poskytnuté jiným bankám |
            | **Neutrální operace** | Banka poskytuje služby, ze kterých získává poplatky nebo provize, ale přímo při nich nepůjčuje vlastní peníze jako u úvěru. | platební styk, vedení účtu, směna měn, zprostředkování investic, úschova cenností, poradenství, bankovní záruky, inkaso, dokumentární akreditiv |
            """)

            st.markdown("""
            <div class='box-gray'>
                🧮 <strong>Jednoduchá logika banky:</strong> Banka přijímá vklady za určitý úrok a půjčuje peníze za vyšší úrok. Rozdíl mezi úrokem z úvěrů a úrokem z vkladů je jedním ze zdrojů jejích výnosů. Dalším zdrojem jsou poplatky a provize za služby.
            </div>
            """, unsafe_allow_html=True)

            with st.expander("Pasivní operace: jak banka získává peníze (Podrobně)"):
                st.write("Pasivní operace jsou činnosti, při kterých banka získává zdroje. Říká se jim pasivní proto, že z pohledu bankovní rozvahy vzniká bance závazek: banka peníze klientovi dluží.")
                st.markdown("""
                * **běžné účty** — klient má peníze dostupné pro každodenní platby; banka je eviduje jako závazek vůči klientovi,
                * **spořicí účty** — klient ukládá peníze s vyšším úrokem než na běžném účtu, ale obvykle s vysokou dostupností,
                * **termínované vklady** — klient uloží peníze na předem určenou dobu a za to získá sjednaný úrok,
                * **vkladové produkty pro firmy** — firmy ukládají volné prostředky a banka s nimi může dále pracovat podle pravidel likvidity,
                * **emise bankovních dluhopisů** — banka si půjčuje od investorů tím, že vydá dluhopis,
                * **mezibankovní úvěry přijaté** — banka si půjčí od jiné banky,
                * **vlastní kapitál banky** — peníze vlastníků, které slouží jako bezpečnostní polštář.
                """)
                st.info("📥 **Příklad pasivní operace:** Student si uloží 5 000 Kč na spořicí účet. Pro studenta je to úspora. Pro banku je to zdroj peněz a zároveň závazek, protože banka musí umožnit výběr podle podmínek účtu.")

            with st.expander("Aktivní operace: jak banka peníze používá (Podrobně)"):
                st.write("Aktivní operace jsou činnosti, při kterých banka umisťuje získané peníze tak, aby vydělávala. Z pohledu banky jde o aktiva: banka má pohledávku za klientem nebo vlastní určitý finanční nástroj.")
                st.markdown("""
                * **spotřebitelské úvěry** — půjčky domácnostem například na vybavení, auto nebo jiné potřeby,
                * **hypoteční úvěry** — dlouhodobé úvěry na bydlení zajištěné nemovitostí,
                * **kontokorent** — možnost jít na běžném účtu do mínusu do stanoveného limitu,
                * **kreditní karta** — úvěrový rámec spojený s kartou; pokud se nesplatí v bezúročném období, úrok bývá vysoký,
                * **podnikatelské úvěry** — úvěry pro firmy na provoz, zásoby, mzdy nebo investice,
                * **investiční úvěry** — úvěry na stroje, technologie, budovy nebo rozšíření podnikání,
                * **provozní financování** — krátkodobé financování chodu firmy,
                * **nákup cenných papírů** — banka může část peněz investovat do bezpečnějších i výnosnějších aktiv podle pravidel řízení rizik,
                * **mezibankovní úvěry poskytnuté** — banka půjčí jiné bance.
                """)
                st.info("📤 **Příklad aktivní operace:** Banka poskytne rodině hypotéku. Rodina získá peníze na bydlení, ale bance vzniká pohledávka: rodina musí úvěr splácet i s úrokem.")

            with st.expander("Neutrální operace: služby za poplatky a provize (Podrobně)"):
                st.write("Neutrální operace nejsou hlavně o tom, že banka přijímá vklady nebo poskytuje úvěry. Banka při nich zajišťuje služby a vydělává například na poplatcích nebo provizích.")
                st.markdown("""
                * vedení účtu,
                * zpracování plateb,
                * vydání a správa platební karty,
                * směna měn,
                * výběry a vklady hotovosti,
                * zprostředkování investic,
                * zprostředkování pojištění,
                * bankovní záruky,
                * dokumentární akreditivy a inkasa v zahraničním obchodě,
                * úschova cenností,
                * finanční poradenství.
                """)

            st.markdown("""
            | Situace klienta | Typ operace banky | Proč |
            | :--- | :--- | :--- |
            | Klient vloží peníze na spořicí účet. | **Pasivní** | Banka získává zdroj a má závazek vůči klientovi. |
            | Klient si vezme hypotéku. | **Aktivní** | Banka poskytuje úvěr a očekává splácení s úrokem. |
            | Klient zaplatí kartou v obchodě. | **Neutrální** | Banka zajišťuje platební službu. |
            | Firma získá provozní úvěr. | **Aktivní** | Banka financuje firmu a nese úvěrové riziko. |
            | Klient si vymění koruny za eura. | **Neutrální** | Banka poskytuje směnárenskou službu a může vydělat na kurzu nebo poplatku. |
            """)

            st.markdown("#### 🧩 Rozhodovací karty: aktivní, pasivní, nebo neutrální?")
            st.write("U každé situace urči typ bankovní operace a vysvětli ji z pohledu banky:")

            rk1 = st.selectbox("1. Klient vloží 10 000 Kč na spořicí účet:", ["Vyber...", "Pasivní", "Aktivní", "Neutrální"], key="k2_rk1")
            rk2 = st.selectbox("2. Rodina si vezme hypotéku:", ["Vyber...", "Pasivní", "Aktivní", "Neutrální"], key="k2_rk2")
            rk3 = st.selectbox("3. Student zaplatí kartou v kavárně:", ["Vyber...", "Pasivní", "Aktivní", "Neutrální"], key="k2_rk3")
            rk4 = st.selectbox("4. Firma požádá o provozní úvěr:", ["Vyber...", "Pasivní", "Aktivní", "Neutrální"], key="k2_rk4")
            rk5 = st.selectbox("5. Klient si smění koruny na eura:", ["Vyber...", "Pasivní", "Aktivní", "Neutrální"], key="k2_rk5")
            rk6 = st.selectbox("6. Banka vydá vlastní dluhopis:", ["Vyber...", "Pasivní", "Aktivní", "Neutrální"], key="k2_rk6")
            rk7 = st.selectbox("7. Podnikatel používá platební terminál:", ["Vyber...", "Pasivní", "Aktivní", "Neutrální"], key="k2_rk7")

            if st.button("Vyhodnotit rozhodovací karty", key="k2_rk_btn"):
                if rk1=="Pasivní" and rk2=="Aktivní" and rk3=="Neutrální" and rk4=="Aktivní" and rk5=="Neutrální" and rk6=="Pasivní" and rk7=="Neutrální":
                    st.success("🎉 Skvělé! Rozdíly mezi aktivními, pasivními a neutrálními operacemi ovládáš na jedničku.")
                else:
                    st.error("Některá odpověď nesouhlasí. Zkontroluj tabulku výše!")

        # 1.2.12 Jak banka vydělává a rizika
        with st.container(border=True):
            st.markdown("### 1.2.12 Jak banka vydělává a proč musí hlídat riziko")
            st.write("Banka nevydělává jen tím, že „má peníze“. Vydělává hlavně na:")
            st.markdown("""
            * úrokové marži,
            * poplatcích,
            * provizích,
            * investičních a devizových operacích,
            * službách pro firmy a instituce.
            """)
            st.write("Zároveň ale nese rizika:")
            st.markdown("""
            * **úvěrové riziko** — klient nesplatí úvěr,
            * **likviditní riziko** — banka nemá v daný okamžik dost dostupných peněz,
            * **úrokové riziko** — změna sazeb ovlivní výnosy a náklady banky,
            * **měnové riziko** — změna kurzu ovlivní hodnotu obchodů v cizí měně,
            * **operační riziko** — selže systém, proces nebo člověk,
            * **kybernetické riziko** — útok na digitální bankovnictví nebo data klientů.
            """)

            st.markdown("""
            <div class='box-red'>
                🔐 <strong>Proč existuje regulace:</strong> Kdyby banky riskovaly příliš mnoho, neohrozily by jen sebe. Ohrozily by vklady klientů, firmy, platební systém i celou ekonomiku. Proto jsou banky přísně regulované a dohlížené.
            </div>
            """, unsafe_allow_html=True)

        # 1.2.13 Licence a dohled
        with st.container(border=True):
            st.markdown("### 1.2.13 Bankovní licence a dohled")
            st.write("Banka nemůže začít fungovat jen proto, že si někdo založí aplikaci a napíše „banka“. K poskytování bankovních služeb potřebuje povolení. V České republice nad bankami dohlíží ČNB.")
            st.write("ČNB sleduje například:")
            st.markdown("""
            * zda banka má dost kapitálu,
            * zda rozumně řídí rizika,
            * zda dodržuje pravidla pro ochranu klientů,
            * zda plní povinnosti proti praní špinavých peněz,
            * zda má bezpečné systémy,
            * zda je schopna zvládnout krizové situace.
            """)

            st.write("**Proč banka nemůže půjčit úplně všechno, co má?** Protože musí zvládnout běžné výběry klientů, platby, regulatorní požadavky a krizové situace. Banka musí držet určité rezervy a kapitál. Pokud by půjčovala příliš rizikově, mohla by ohrozit důvěru klientů i stabilitu celého systému.")

            st.markdown("#### 🛠️ Mini audit banky")
            st.write("Představ si, že jsi bankovní analytik. Máš posoudit, jestli banka nepodstupuje moc velké riziko. Sleduj tři otázky:")

            ma1 = st.radio("1. Půjčuje banka lidem a firmám, kteří pravděpodobně zvládnou splácet?", ["Ano, prověřuje bonitu", "Ne, půjčí úplně každému bez kontroly"], key="k2_ma1")
            ma2 = st.radio("2. Má dost peněz pro běžné výběry a platby klientů?", ["Ano, drží likviditní rezervy", "Ne, všechno rozjala do 30letých půjček"], key="k2_ma2")
            ma3 = st.radio("3. Má dost kapitálu, aby zvládla případné ztráty?", ["Ano, drží vyžadovaný kapitál", "Ne, nemá žádný vlastní kapitál"], key="k2_ma3")

            ma_text = st.text_area("Na závěr napiš doporučení: Co by měla banka zlepšit, aby byla bezpečnější?", key="k2_ma_text")

            if st.button("Vyhodnotit mini audit", key="k2_ma_btn"):
                if ma1=="Ano, prověřuje bonitu" and ma2=="Ano, drží likviditní rezervy" and ma3=="Ano, drží vyžadovaný kapitál":
                    st.success("✅ **Správný audit:** Banka splňuje klíčové podmínky obezřetného podnikání a ochrany vkladatelů.")
                else:
                    st.error("⚠️ **Rizikové zjištění:** Banka nesplňuje bezpečnostní pravidla a hrozí jí zásah ze strany ČNB!")

        # 1.2.14 Vklady a jejich ochrana
        with st.container(border=True):
            st.markdown("### 1.2.14 Vklady a jejich ochrana")
            st.write("Vklady klientů v bankách jsou v zákonem stanoveném rozsahu chráněny systémem pojištění vkladů. Smyslem je posílit důvěru lidí v bankovní systém a snížit riziko paniky při problémech banky.")

            st.markdown("""
            <div class='box-blue'>
                🛟 <strong>Do jaké výše jsou vklady pojištěny:</strong> V České republice jsou pojištěné vklady u bank, družstevních záložen a stavebních spořitelen chráněny zpravidla do výše 100 000 EUR na jednoho klienta u jedné banky. V přepočtu jde přibližně o 2,4–2,5 milionu Kč, podle aktuálního kurzu. Pokud má člověk u jedné banky více účtů, limit se obvykle počítá dohromady za daného klienta u dané banky, ne zvlášť za každý účet.
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            | Situace | Jak to zjednodušeně funguje | Příklad |
            | :--- | :--- | :--- |
            | **Klient má u jedné banky 500 000 Kč** | Částka je pod limitem pojištění vkladů. | Při krachu banky by měla být chráněna celá částka. |
            | **Klient má u jedné banky 2 000 000 Kč** | Částka je stále přibližně pod limitem 100 000 EUR. | Vklad by byl obvykle chráněn celý. |
            | **Klient má u jedné banky 4 000 000 Kč** | Část přesahuje základní limit pojištění. | Pojištěna by byla jen část do limitu; zbytek by nesl riziko. |
            | **Klient má 2 000 000 Kč v jedné bance a 2 000 000 Kč v jiné bance** | Limit se posuzuje u každé banky zvlášť. | Rozložení peněz mezi banky může snížit riziko překročení limitu. |
            """)

            st.write("**Kdo pojištění vkladů zajišťuje?** V České republice výplatu náhrad zajišťuje Garanční systém finančního trhu prostřednictvím Fondu pojištění vkladů. Pokud by banka zkrachovala a nebyla schopná vyplatit klientům vklady, systém pojištění vkladů slouží k tomu, aby klienti dostali náhradu do zákonem stanoveného limitu.")

            st.markdown("##### Výběr hotovosti: kolik lze vybrat a kdy to hlásit bance")
            st.write("To, že má člověk peníze na účtu, neznamená, že si může kdykoliv bez přípravy odnést z pobočky libovolně vysokou hotovost. Banka musí mít hotovost fyzicky připravenou na pobočce a zároveň musí plnit pravidla proti praní špinavých peněz.")

            st.markdown("""
            | Typ výběru | Jak to běžně funguje | Na co si dát pozor |
            | :--- | :--- | :--- |
            | **Výběr z bankomatu** | Řídí se limitem platební karty a limitem konkrétního bankomatu. | Limit si člověk často nastavuje v aplikaci, ale bankomat může mít i vlastní technické omezení. |
            | **Menší výběr na pobočce** | Obvykle lze vybrat bez předchozího objednání, pokud má pobočka hotovost k dispozici. | Každá banka může mít vlastní pravidla a limity. |
            | **Větší hotovostní výběr** | Často je vhodné nebo nutné oznámit ho bance předem, ale hranice se mezi bankami výrazně liší. | Například u ČSOB je podle zveřejněných informací potřeba předem objednat až částku převyšující 300 000 Kč; u KB se naopak uvádí hlášení už nad 100 000 Kč. |
            | **Velmi vysoký výběr** | Banka může požadovat písemné oznámení, objednání hotovosti nebo vysvětlení účelu. | Nejde o zvědavost pokladníka, ale o provozní a zákonné povinnosti banky. |
            """)

            st.markdown("""
            <div class='box-red'>
                ⚠️ <strong>Důležité:</strong> Neexistuje jedno univerzální číslo, které by platilo pro všechny banky jako „do této částky nikdy nic nehlaš“. U velkých výběrů hotovosti záleží na pravidlech konkrétní banky, typu pobočky, měně, dostupnosti hotovosti a bezpečnostních pravidlech. Proto je lepší neuvádět 100 000 Kč jako obecnou hranici pro celý trh. Realističtější formulace je: u některých bank může být hranice nižší, u jiných lze bez předchozího objednání vybrat i vyšší částky — například u ČSOB se jako hranice pro objednání uvádí až částka nad 300 000 Kč.
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class='box-purple'>
                🧠 <strong>Proč banka řeší velké hotovostní výběry:</strong><br>
                • <strong>Provozní důvod:</strong> pobočka nemusí mít okamžitě připravené velké množství hotovosti.<br>
                • <strong>Bezpečnost:</strong> převoz a výdej vysoké hotovosti je rizikový.<br>
                • <strong>AML pravidla:</strong> banka musí sledovat podezřelé transakce a původ peněz, aby se bránilo praní špinavých peněz a financování nelegálních aktivit.<br>
                • <strong>Ochrana klienta:</strong> neobvyklý výběr může být i signál, že je klient pod tlakem podvodníka.
            </div>
            """, unsafe_allow_html=True)

            st.write("**Příklad: výběr 300 000 Kč nebo 600 000 Kč na koupi auta:** Pokud chce klient vybrat 300 000 Kč v hotovosti, u některých bank to může být ještě běžně proveditelné bez zvláštního objednání, pokud má pobočka hotovost a klient splňuje limity účtu nebo karty. Například ČSOB uvádí, že předem je potřeba objednat až částku převyšující 300 000 Kč, případně výběr v cizí měně nebo požadovanou konkrétní skladbu bankovek. Pokud ale chce klient vybrat třeba 600 000 Kč, už je mnohem pravděpodobnější, že banka bude chtít výběr předem objednat. Potřebuje připravit hotovost, zajistit bezpečný provoz pobočky a splnit pravidla proti praní špinavých peněz. Neznamená to, že peníze nejsou klienta. Znamená to, že vysoká hotovost je pro banku provozní, bezpečnostní a regulatorní situace.")

            st.markdown("""
            <div class='box-blue'>
                🛟 <strong>Co si zapamatovat:</strong> Peníze na běžném nebo spořicím účtu nejsou totéž jako hotovost v peněžence. Jsou to pohledávky vůči bance. Proto je důležité, aby banky byly regulované, dohlížené a aby existovala pravidla ochrany vkladatelů. Základní pojištění vkladů je do 100 000 EUR na klienta u jedné banky. U hotovostních výběrů neplatí jedna hranice pro všechny banky — například ČSOB uvádí objednání až nad 300 000 Kč, zatímco jiné banky mohou chtít hlášení dříve.
            </div>
            """, unsafe_allow_html=True)

    # =========================================================================
    # 1.3 PLATEBNÍ STYK
    # =========================================================================
    elif "1.3 Platební styk" in selected_section_2:
        st.markdown("<div class='sub-section-header'>1. BANKOVNÍ SYSTÉM A PENÍZE V 21. STOLETÍ</div><h2>1.3 Platební styk</h2>", unsafe_allow_html=True)
        st.write("Platební styk znamená převod peněz mezi plátcem a příjemcem. Díky platebnímu styku můžeme zaplatit oběd kartou, poslat nájem převodem, nakoupit online, zaplatit fakturu přes QR kód nebo přijmout výplatu na účet.")

        with st.container(border=True):
            st.markdown("""
            <div class='box-blue'>
                💳 <strong>Základní myšlenka:</strong> Platební styk je infrastruktura důvěry. Umožňuje, aby se peníze bezpečně a prokazatelně přesunuly od toho, kdo platí, k tomu, kdo má peníze dostat.
            </div>
            """, unsafe_allow_html=True)

        # 1.3.1
        with st.container(border=True):
            st.markdown("### 1.3.1 Co nám platební styk umožňuje")
            st.write("Platební styk umožňuje:")
            st.markdown("""
            * platit za zboží a služby,
            * přijímat mzdu, kapesné, dávky nebo platby od zákazníků,
            * splácet úvěry,
            * platit nájem, energie, školní akce nebo faktury,
            * převádět peníze mezi vlastními účty,
            * platit v zahraničí,
            * podnikům přijímat platby kartou nebo online,
            * státu vybírat daně a vyplácet veřejné výdaje.
            """)

        # 1.3.2
        with st.container(border=True):
            st.markdown("### 1.3.2 Druhy platebního styku")
            st.write("Platební styk lze rozdělit několika způsoby:")

            st.markdown("""
            | Druh | Co znamená | Příklady |
            | :--- | :--- | :--- |
            | **Hotovostní** | Platí se fyzickými penězi. | bankovky, mince, výběr z bankomatu, vklad hotovosti |
            | **Bezhotovostní** | Peníze se převádějí jako záznam mezi účty. | bankovní převod, platba kartou, trvalý příkaz, inkaso, QR platba |
            | **Tuzemský** | Platba probíhá v rámci České republiky. | převod mezi českými bankami v Kč |
            | **Zahraniční** | Platba směřuje do jiné země nebo v jiné měně. | SEPA platba v eurech, mezinárodní převod, platba kartou v zahraničí |
            | **Jednorázový** | Platba se zadává pro jeden konkrétní převod. | jednorázová úhrada faktury |
            | **Opakovaný** | Platba se provádí pravidelně nebo automaticky. | trvalý příkaz, SIPO, inkaso, předplatné |
            | **Okamžitý** | Peníze dorazí během několika sekund, pokud to banky podporují. | okamžitá platba mezi bankami |
            """)

            st.markdown("#### 🧭 Aktivita: Vyber správný typ platby")
            st.write("U každé situace urči, zda jde o platbu hotovostní/bezhotovostní, tuzemskou/zahraniční a jednorázovou/opakovanou:")

            act_1 = st.selectbox("1. Platím kávu v hotovosti:", ["Vyber...", "Hotovostní / Tuzemská / Jednorázová", "Bezhotovostní / Tuzemská / Opakovaná"], key="k2_act1")
            act_2 = st.selectbox("2. Posílám nájem trvalým příkazem:", ["Vyber...", "Bezhotovostní / Tuzemská / Opakovaná", "Hotovostní / Zahraniční / Jednorázová"], key="k2_act2")
            act_3 = st.selectbox("3. Platím Spotify předplatné:", ["Vyber...", "Bezhotovostní / Zahraniční / Opakovaná", "Hotovostní / Tuzemská / Jednorázová"], key="k2_act3")
            act_4 = st.selectbox("4. Nakupuji v zahraničním e-shopu:", ["Vyber...", "Bezhotovostní / Zahraniční / Jednorázová", "Hotovostní / Tuzemská / Opakovaná"], key="k2_act4")
            act_5 = st.selectbox("5. Posílám peníze na školní výlet přes QR kód:", ["Vyber...", "Bezhotovostní / Tuzemská / Jednorázová", "Hotovostní / Zahraniční / Opakovaná"], key="k2_act5")
            act_6 = st.selectbox("6. Vybírám peníze z bankomatu:", ["Vyber...", "Hotovostní operace / Tuzemská / Jednorázová", "Bezhotovostní převod"], key="k2_act6")
            act_7 = st.selectbox("7. Platím kartou na dovolené v cizině:", ["Vyber...", "Bezhotovostní / Zahraniční / Jednorázová", "Hotovostní / Tuzemská"], key="k2_act7")

            st.text_area("Bonus: U každé situace navrhni nejbezpečnější platební nástroj:", key="k2_act_bonus")

            if st.button("Vyhodnotit aktivitu plateb", key="k2_act_btn"):
                if act_1=="Hotovostní / Tuzemská / Jednorázová" and act_2=="Bezhotovostní / Tuzemská / Opakovaná" and act_3=="Bezhotovostní / Zahraniční / Opakovaná" and act_4=="Bezhotovostní / Zahraniční / Jednorázová" and act_5=="Bezhotovostní / Tuzemská / Jednorázová" and act_6=="Hotovostní operace / Tuzemská / Jednorázová" and act_7=="Bezhotovostní / Zahraniční / Jednorázová":
                    st.success("🎉 Skvělá práce! Všechny typy plateb jsi určil/a zcela správně.")
                else:
                    st.error("Některý z typů plateb je vybrán špatně. Zkontroluj správné zařazení!")

        # 1.3.3
        with st.container(border=True):
            st.markdown("### 1.3.3 Nejběžnější platební nástroje")
            st.write("Mezi nejčastější nástroje platebního styku patří:")
            st.markdown("""
            * **hotovost** — bankovky a mince,
            * **příkaz k úhradě** — zadáš platbu ze svého účtu,
            * **trvalý příkaz** — pravidelná platba stejné částky,
            * **inkaso** — příjemce si stáhne platbu se souhlasem plátce, například energie,
            * **SIPO** — sdružené inkaso plateb obyvatelstva,
            * **platební karta** — debetní nebo kreditní,
            * **mobilní platby** — Apple Pay, Google Pay a podobné služby,
            * **QR platba** — načtení platebních údajů z QR kódu,
            * **online platební brána** — platba v e-shopu,
            * **SEPA platba** — převod v eurech v rámci evropského prostoru,
            * **zahraniční převod** — platba mimo běžný tuzemský nebo SEPA režim.
            """)

            st.markdown("""
            <div class='box-purple'>
                🧩 <strong>Interaktivní výzva:</strong> Vyber tři platby, které jsi provedl/a za poslední týden. Urči, zda šlo o hotovostní nebo bezhotovostní platbu, jednorázovou nebo opakovanou, tuzemskou nebo zahraniční.
            </div>
            """, unsafe_allow_html=True)
            st.text_area("Zapiš své 3 platby:", key="k2_3_my_payments")

        # 1.3.4
        with st.container(border=True):
            st.markdown("### 1.3.4 Kdo platební styk řídí a reguluje")
            st.write("Platební styk není divoký prostor bez pravidel. Funguje díky spolupráci bank, platebních institucí, karetních společností, technologických poskytovatelů, obchodníků, státu a regulátorů.")
            st.write("V České republice má důležitou roli:")
            st.markdown("""
            * **ČNB** — provozuje a dohlíží na vybrané platební systémy a dohlíží na finanční instituce,
            * **komerční banky** — vedou účty klientů a zpracovávají platby,
            * **platební instituce a fintech firmy** — poskytují některé platební služby,
            * **karetní asociace** — nastavují pravidla karetních sítí,
            * **obchodníci a platební brány** — přijímají platby od zákazníků,
            * **právní předpisy ČR a EU** — stanovují pravidla bezpečnosti, práv klientů, odpovědnosti a ochrany spotřebitele.
            """)

            st.markdown("##### CERTIS: „dálnice“ pro platby mezi českými bankami")
            st.write("Když posíláme peníze v českých korunách, je důležité rozlišit, jestli jde platba v rámci jedné banky, nebo mezi dvěma různými bankami.")

            st.markdown("""
            <div class='box-blue'>
                🏦 <strong>Co je CERTIS:</strong> CERTIS je český systém mezibankovního platebního styku. Zjednodušeně řečeno je to systém, přes který se v České republice zúčtovávají platby v korunách mezi různými bankami. Název CERTIS znamená Czech Express Real Time Interbank Gross Settlement System. Systém spravuje a provozuje Česká národní banka.
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            | Situace | Co se děje s platbou | Jde přes CERTIS? |
            | :--- | :--- | :--- |
            | **Platba v rámci stejné banky** | Oba účty jsou u stejné banky. Banka si platbu zúčtuje ve vlastním systému: jednomu klientovi částku odepíše, druhému připíše. | Obvykle ne. Zůstává uvnitř banky. |
            | **Platba mezi různými bankami** | Plátce má účet u jedné banky a příjemce u jiné banky. Banka plátce musí poslat mezibankovní pokyn přes systém CERTIS. | Ano. Platba se vypořádá mezi bankami přes CERTIS. |
            | **Okamžitá platba mezi různými bankami** | Pokud obě banky podporují okamžité platby, převod může proběhnout během několika sekund i mezi různými bankami. | Ano, v režimu okamžitých plateb v rámci mezibankovního systému. |
            """)

            st.write("**Příklad: spolužák ve stejné bance vs. spolužák v jiné bance:** Představ si, že posíláš 500 Kč za společný dárek.")
            st.markdown("""
            1. **Spolužák má účet u stejné banky:** Tvoje banka pouze upraví záznamy ve svém systému. Tobě 500 Kč odečte a spolužákovi 500 Kč připíše. Peníze nemusí „opustit“ banku.
            2. **Spolužák má účet u jiné banky:** Tvoje banka odešle pokyn do mezibankovního systému CERTIS. Přes něj se platba vypořádá mezi bankami a banka spolužáka částku připíše na jeho účet.
            """)
            st.info("💡 **Jednoduše:** Když jsou oba účty ve stejné bance, banka si platbu vyřeší sama. Když jsou účty v různých bankách, musí se banky mezi sebou „domluvit“ přes mezibankovní systém. V ČR je pro korunové mezibankovní platby klíčový právě CERTIS, který spravuje ČNB.")

        # 1.3.5
        with st.container(border=True):
            st.markdown("### 1.3.5 Jak probíhá platba kartou")
            st.write("Když přiložíš kartu nebo mobil k terminálu, vše vypadá jako jedna sekunda. Ve skutečnosti se v pozadí odehraje několik kroků:")
            st.markdown("""
            1. Terminál načte platební údaje.
            2. Obchodník pošle požadavek přes platební síť.
            3. Banka ověří kartu, limit, bezpečnostní pravidla a dostupné prostředky.
            4. Platba se autorizuje nebo zamítne.
            5. Později proběhne zúčtování mezi bankami a obchodníkem.
            """)

            st.markdown("""
            <div class='box-red'>
                🔐 <strong>Bezpečnost:</strong> U plateb se používají limity, PIN, biometrie, potvrzení v aplikaci, 3D Secure, monitoring podezřelých transakcí a další ochranné prvky. Bezpečnost ale začíná i u uživatele: neklikat na podezřelé odkazy, nesdělovat kódy a chránit přístup do bankovnictví.
            </div>
            """, unsafe_allow_html=True)

            st.markdown("#### 🔁 Skládačka: Cesta platby kartou")
            st.write("Seřaď kroky platby kartou nebo mobilem ve správném pořadí:")

            s_krok1 = st.selectbox("1. krok:", ["Vyber...", "přiložení karty nebo mobilu k terminálu", "terminál načte platební údaje", "obchodník odešle požadavek přes platební síť", "banka ověří kartu, limit a bezpečnostní pravidla", "platba se schválí nebo zamítne", "později proběhne zúčtování mezi bankami a obchodníkem"], key="k2_sk1")
            s_krok2 = st.selectbox("2. krok:", ["Vyber...", "přiložení karty nebo mobilu k terminálu", "terminál načte platební údaje", "obchodník odešle požadavek přes platební síť", "banka ověří kartu, limit a bezpečnostní pravidla", "platba se schválí nebo zamítne", "později proběhne zúčtování mezi bankami a obchodníkem"], key="k2_sk2")
            s_krok3 = st.selectbox("3. krok:", ["Vyber...", "přiložení karty nebo mobilu k terminálu", "terminál načte platební údaje", "obchodník odešle požadavek přes platební síť", "banka ověří kartu, limit a bezpečnostní pravidla", "platba se schválí nebo zamítne", "později proběhne zúčtování mezi bankami a obchodníkem"], key="k2_sk3")
            s_krok4 = st.selectbox("4. krok:", ["Vyber...", "přiložení karty nebo mobilu k terminálu", "terminál načte platební údaje", "obchodník odešle požadavek přes platební síť", "banka ověří kartu, limit a bezpečnostní pravidla", "platba se schválí nebo zamítne", "později proběhne zúčtování mezi bankami a obchodníkem"], key="k2_sk4")
            s_krok5 = st.selectbox("5. krok:", ["Vyber...", "přiložení karty nebo mobilu k terminálu", "terminál načte platební údaje", "obchodník odešle požadavek přes platební síť", "banka ověří kartu, limit a bezpečnostní pravidla", "platba se schválí nebo zamítne", "později proběhne zúčtování mezi bankami a obchodníkem"], key="k2_sk5")
            s_krok6 = st.selectbox("6. krok:", ["Vyber...", "přiložení karty nebo mobilu k terminálu", "terminál načte platební údaje", "obchodník odešle požadavek přes platební síť", "banka ověří kartu, limit a bezpečnostní pravidla", "platba se schválí nebo zamítne", "později proběhne zúčtování mezi bankami a obchodníkem"], key="k2_sk6")

            st.write("**Otázky k zamyšlení:**")
            st.text_input("1. Kde může platba selhat?", key="k2_q_fail")
            st.text_input("2. Kdo všechno se platby účastní?", key="k2_q_who")
            st.text_input("3. Proč platba mobilem není „kouzlo“, ale datový proces?", key="k2_q_magic")

            if st.button("Vyhodnotit skládačku platby kartou", key="k2_sk_eval_btn"):
                if s_krok1=="přiložení karty nebo mobilu k terminálu" and s_krok2=="terminál načte platební údaje" and s_krok3=="obchodník odešle požadavek přes platební síť" and s_krok4=="banka ověří kartu, limit a bezpečnostní pravidla" and s_krok5=="platba se schválí nebo zamítne" and s_krok6=="později proběhne zúčtování mezi bankami a obchodníkem":
                    st.success("🎉 Skvělé! Kompletní řetězec platby kartou máš seřazený zcela přesně.")
                else:
                    st.error("Některý krok v pořadí nesouhlasí. Zkontroluj seznam v bodě 1.3.5!")

        # 1.3.6
        with st.container(border=True):
            st.markdown("### 1.3.6 Digitální bezpečnost plateb")
            st.write("Nejčastější rizika:")
            st.markdown("""
            * phishingové e-maily a SMS,
            * falešné stránky bank,
            * podvodné telefonáty „z banky“,
            * falešné investiční nabídky,
            * krádež přihlašovacích údajů,
            * zneužití platební karty,
            * tlak na rychlé rozhodnutí.
            """)

            st.markdown("""
            | Situace | Co dělat | Proč |
            | :--- | :--- | :--- |
            | Přijde SMS s odkazem na „blokaci účtu“ | Neotevírat odkaz, ověřit situaci přímo v aplikaci banky nebo na oficiální lince. | Podvodníci často vytvářejí falešný pocit naléhavosti. |
            | Někdo chce autorizační kód | Nikdy ho nesdělovat. | Kód může potvrdit platbu nebo přístup k účtu. |
            | Aplikace nabízí „garantované zhodnocení“ | Ověřit licenci, rizika a reálnost slibu. | Vysoký výnos bez rizika je varovný signál. |
            """)

            st.markdown("#### 🚨 Phishing escape room: nenech se okrást jedním klikem")
            st.write("Pro každou zprávu rozhodni, zda je bezpečná, podezřelá nebo nebezpečná. Najdi varovný signál a navrhni správnou reakci:")

            er1 = st.radio("1. „Vaše karta byla zablokována. Klikněte zde a ověřte účet.“", ["Bezpečná", "Podezřelá / Nebezpečná (Phishing)"], key="k2_er1")
            er2 = st.radio("2. „Jsem z bezpečnostního oddělení banky. Nadiktujte mi kód z SMS.“", ["Bezpečná", "Podezřelá / Nebezpečná (Vishing)"], key="k2_er2")
            er3 = st.radio("3. „Investice s garantovaným výnosem 30 % měsíčně.“", ["Bezpečná", "Podezřelá / Nebezpečná (Podvod)"], key="k2_er3")
            er4 = st.radio("4. „Potvrďte přístup do internetového bankovnictví přes tento odkaz.“", ["Bezpečná", "Podezřelá / Nebezpečná (Phishing)"], key="k2_er4")
            er5 = st.radio("5. E-shop nabízí uložení karty pro příští nákup.", ["Standardní funkce platební brány", "Podezřelá / Nebezpečná"], key="k2_er5")

            st.info("🛡️ **Pravidlo přežití:** Banka po telefonu ani přes zprávu nechce heslo, PIN ani autorizační kód. Když cítíš tlak na rychlost, zpomal a ověřuj oficiální cestou.")

            if st.button("Vyhodnotit Phishing Escape Room", key="k2_er_eval_btn"):
                if er1=="Podezřelá / Nebezpečná (Phishing)" and er2=="Podezřelá / Nebezpečná (Vishing)" and er3=="Podezřelá / Nebezpečná (Podvod)" and er4=="Podezřelá / Nebezpečná (Phishing)" and er5=="Standardní funkce platební brány":
                    st.success("🎉 Skvělé! Bezpečně jsi rozpoznal/a všechna rizika digitálního světa.")
                else:
                    st.error("Některá zpráva byla vyhodnocena špatně. Pozor na falešný tlak na čas a žádosti o kódy!")

    # =========================================================================
    # 1.4 FINTECH REVOLUCE
    # =========================================================================
    elif "1.4 Fintech" in selected_section_2:
        st.markdown("<div class='sub-section-header'>1. BANKOVNÍ SYSTÉM A PENÍZE V 21. STOLETÍ</div><h2>1.4 Fintech revoluce</h2>", unsafe_allow_html=True)
        st.write("Fintech je spojení slov **finance** a **technology**. Označuje firmy a služby, které pomocí technologií mění způsob, jak platíme, spoříme, investujeme, půjčujeme si, ověřujeme identitu nebo spravujeme rozpočet.")

        with st.container(border=True):
            st.markdown("""
            <div class='box-blue'>
                🚀 <strong>Fintech změna:</strong> Finance se přesunuly z pobočky do mobilu. Uživatel očekává rychlost, jednoduché ovládání, okamžité notifikace, nízké poplatky a možnost vyřídit vše online.
            </div>
            """, unsafe_allow_html=True)

        # 1.4.1
        with st.container(border=True):
            st.markdown("### 1.4.1 Co fintech přinesl")
            st.write("Fintech služby přinesly například:")
            st.markdown("""
            * online založení účtu,
            * okamžité notifikace o platbách,
            * jednoduché investování malých částek,
            * levnější směnu měn,
            * virtuální platební karty,
            * rozpočtové aplikace,
            * propojení účtů z více bank,
            * platby mobilem a hodinkami,
            * QR platby,
            * rychlé online půjčky,
            * crowdfunding,
            * peer-to-peer platby,
            * digitální ověření identity,
            * automatické třídění výdajů.
            """)

        # 1.4.2
        with st.container(border=True):
            st.markdown("### 1.4.2 Neobanky a moderní finanční aplikace")
            st.write("Neobanky jsou bankovní nebo finanční služby stavěné hlavně pro mobilní prostředí. Často nemají klasickou síť poboček a soutěží jednoduchostí aplikace, rychlostí a cenou. Někdy jde o banku s bankovní licencí, jindy spíše o fintechovou platební aplikaci, která nabízí účet, kartu, směnu měn nebo další finanční služby.")

            st.markdown("""
            <div class='box-gray'>
                📱 <strong>Příklady neobank a digitálních finančních služeb dostupných v ČR:</strong><br><br>
                • <strong>Revolut</strong> — velmi známá mobilní finanční aplikace používaná pro účet, kartu, směnu měn, cestování, platby v zahraničí, investice nebo kryptoměny. Pro studenty je dobrým příkladem „banky v mobilu“, i když je důležité rozlišovat, pod jakou licencí a ochranou služba funguje.<br><br>
                • <strong>Wise</strong> — služba zaměřená hlavně na levnější mezinárodní převody, víceměnový účet a platby v různých měnách. Hodí se jako příklad fintechu, který řeší hlavně zahraniční platby a směnu měn.<br><br>
                • <strong>bunq</strong> — evropská digitální banka s důrazem na mobilní ovládání, více účtů, karty a práci s rozpočtem. V ČR může být dostupná, ale není tak běžná jako klasické české banky.<br><br>
                • <strong>mBank</strong> — banka s výrazně digitálním modelem a menším důrazem na klasické pobočky. V českém prostředí ji lze použít jako příklad banky, která se dlouhodobě opírá o online a mobilní bankovnictví.<br><br>
                • <strong>Air Bank</strong> — česká banka, která sice není čistá neobanka bez zázemí, ale často se uvádí jako příklad modernějšího, jednoduššího a digitálně orientovaného bankovnictví.
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class='box-red'>
                ⚠️ <strong>Pozor na pojem neobanka:</strong> Ne každá aplikace, která vypadá jako banka, je stejná jako klasická banka v ČR. Liší se bankovní licence, pojištění vkladů, zákaznická podpora, poplatky, měny, ochrana klienta i to, kdo službu reguluje. Před používáním je dobré zjistit: Kdo službu provozuje? Má bankovní licenci? Kde jsou pojištěné vklady? Jaké má poplatky a limity?
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            | Klasické bankovnictví | Moderní fintech / neobanka |
            | :--- | :--- |
            | Důraz na pobočku a dlouhodobý vztah s bankou. | Důraz na mobilní aplikaci a rychlé ovládání. |
            | Služby se často řešily osobně nebo přes internetbanking. | Mnoho služeb se vyřídí v telefonu během minut. |
            | Poplatky a kurzovní marže nemusely být pro klienta přehledné. | Aplikace často ukazuje poplatky, kurzy a transakce okamžitě. |
            | Změny byly pomalejší. | Nové funkce přibývají rychleji, ale uživatel musí víc hlídat rizika. |
            """)

        # 1.4.3
        with st.container(border=True):
            st.markdown("### 1.4.3 Open banking: když si aplikace rozumí s bankou")
            st.write("Důležitou změnou je **open banking**. Znamená, že klient může za určitých bezpečnostních podmínek povolit vybrané aplikaci přístup k informacím o účtu nebo zadání platby.")
            st.write("Příklad:")
            st.markdown("""
            * jedna aplikace zobrazí zůstatky z více bank,
            * rozpočtová aplikace roztřídí výdaje,
            * účetní systém firmy si načte bankovní pohyby,
            * platba v e-shopu se zadá přímo z bankovního účtu.
            """)
            st.info("🔑 **Důležité:** Přístup k účtu má být vždy vědomý, omezený a odvolatelný. Uživatel by měl vědět, komu dává souhlas, k čemu a na jak dlouho.")

        # 1.4.4
        with st.container(border=True):
            st.markdown("### 1.4.4 Rizika fintechu")
            st.write("Fintech není automaticky dobrý nebo špatný. Je to nástroj. Může pomoct, ale také zrychlit chybná rozhodnutí.")
            st.write("Rizika:")
            st.markdown("""
            * příliš snadné utrácení,
            * rychlé půjčky bez promyšlení,
            * investování bez pochopení rizika,
            * falešné aplikace,
            * sdílení dat s neověřenými službami,
            * závislost na telefonu a notifikacích,
            * dojem, že „když je to v aplikaci, je to bezpečné“.
            """)
            st.markdown("""
            <div class='box-purple'>
                🧠 <strong>Finanční gramotnost dnes:</strong> Nestačí vědět, co je úrok. Je potřeba umět poznat, kdy aplikace tlačí na rychlost, emoce nebo FOMO. Digitální pohodlí musí jít ruku v ruce s kritickým myšlením.
            </div>
            """, unsafe_allow_html=True)

        # 1.4.5
        with st.container(border=True):
            st.markdown("### 1.4.5 Jak poznat důvěryhodnou finanční službu")
            st.write("Před použitím nové finanční aplikace je dobré zkontrolovat:")
            st.markdown("""
            * kdo službu provozuje,
            * zda má potřebné oprávnění nebo dohled,
            * jak vydělává,
            * jaké má poplatky,
            * jak nakládá s daty,
            * zda slibuje nereálně vysoké výnosy,
            * jak lze službu zrušit,
            * zda má srozumitelné podmínky.
            """)

            st.markdown("#### 📱 Audit finanční aplikace")
            st.write("Vyber jednu službu nebo aplikaci: Revolut, Wise, PayPal, Apple Pay, Google Pay, bankovní aplikaci, investiční aplikaci, rozpočtovou aplikaci nebo službu typu „kup teď, zaplať později“.")

            au_name = st.text_input("1. Název aplikace:", key="k2_au_name")
            au_owner = st.text_input("2. Kdo ji provozuje:", key="k2_au_owner")
            au_feat = st.text_area("3. Co uživateli umožňuje:", key="k2_au_feat")
            au_rev = st.text_area("4. Jak vydělává a jaké má poplatky:", key="k2_au_rev")
            au_data = st.text_area("5. Jaká data po uživateli chce:", key="k2_au_data")
            au_pc = st.text_area("6. Výhody a rizika:", key="k2_au_pc")
            au_rec = st.radio("7. Doporučení spolužákovi:", ["Doporučil/a bych", "Nedoporučil/a bych"], key="k2_au_rec")

            if st.button("Uložit audit aplikace", key="k2_au_btn"):
                st.success(f"Audit pro aplikaci **{au_name}** byl zaznamenán! Výstup: recenze „Pomáhá mi tahle aplikace řídit peníze, nebo mě spíš tlačí k utrácení?“")

            st.markdown("---")

            st.markdown("#### ⚖️ Debata: Fintech — pomocník, nebo past?")
            col_deb1, col_deb2 = st.columns(2)
            with col_deb1:
                st.success("💚 **Tým A (Pomocník):**\nFintech zvyšuje finanční gramotnost, šetří čas, snižuje poplatky za převody a směnu a umožňuje snadnou kontrolu rozpočtu.")
            with col_deb2:
                st.error("🔴 **Tým B (Past):**\nFintech zrychluje impulzivní utrácení, zjednodušuje neuvážené zadlužování, využívá gamifikaci k investičnímu riziku a sbírá osobní data.")

            st.text_area("Vaše argumenty a příklad z běžného života:", key="k2_deb_text")
# =========================================================================
    # 2.1 OSOBNÍ FINANCE V 21. STOLETÍ
    # =========================================================================
    elif "2.1 Osobní finance" in selected_section_2:
        st.markdown("<div class='sub-section-header'>2. OSOBNÍ FINANCE A „ALGORITMY BOHATSTVÍ“</div><h2>2.1 Osobní finance v 21. století: proč je to těžší, než se zdá</h2>", unsafe_allow_html=True)
        st.write("Osobní finance nejsou jen otázka toho, kolik člověk vydělává. Jsou to každodenní rozhodnutí: za co utratím peníze, co odložím, co si půjčím, jak poznám riziko a jak se nenechám řídit reklamou, tlakem okolí nebo algoritmem v aplikaci.")

        with st.container(border=True):
            st.markdown("""
            <div class='box-purple'>
                🧠 <strong>Základní myšlenka:</strong> Finanční gramotnost v 21. století znamená umět zacházet nejen s penězi, ale i s digitálním prostředím, které naše finanční rozhodování ovlivňuje. Nestačí znát pojmy jako rozpočet, úrok nebo inflace. Je potřeba rozumět i tomu, proč nás aplikace, sociální sítě, slevy, předplatná a odložené platby vedou k rychlému utrácení.
            </div>
            """, unsafe_allow_html=True)

        st.write("Dnešní generace řeší několik nových problémů:")
        st.markdown("""
        * platby jsou rychlé a „neviditelné“, takže méně bolí než hotovost,
        * mnoho služeb funguje na předplatném a peníze odcházejí automaticky,
        * reklama je personalizovaná podle dat o našem chování,
        * sociální sítě zvyšují tlak na vzhled, zážitky, značky a životní styl,
        * odložené platby vytvářejí dojem, že si člověk může dovolit víc, než reálně může,
        * inflace mění hodnotu peněz a zdražuje běžný život,
        * finanční produkty jsou dostupné v mobilu, ale ne vždy jsou dobře pochopené.
        """)

        with st.container(border=True):
            st.markdown("""
            <div class='box-red'>
                ⚠️ <strong>Současný problém:</strong> Mnoho lidí nemá problém jen s nedostatkem informací, ale s prostředím, které podporuje okamžité rozhodování. Telefon umožňuje nakoupit, objednat, investovat nebo půjčit si během několika sekund. Finančníchyba tak může vzniknout rychleji než dřív.
            </div>
            """, unsafe_allow_html=True)

        # 2.1.1 Co znamená osobní finanční management
        with st.container(border=True):
            st.markdown("### 2.1.1 Co znamená osobní finanční management")
            st.write("Osobní finanční management je schopnost plánovat a řídit vlastní peníze tak, aby člověk zvládal běžné výdaje, nečekané situace i dlouhodobé cíle.")
            st.write("Patří sem hlavně:")
            st.markdown("""
            * evidence příjmů a výdajů,
            * plánování rozpočtu,
            * tvorba rezervy,
            * rozlišování potřeb a přání,
            * práce s inflací,
            * bezpečné používání finančních služeb,
            * odpovědné zadlužování,
            * základní orientace ve spoření, investování a riziku.
            """)

            st.markdown("##### Potřeba vs. přání")
            st.write("**Potřeba** je výdaj, bez kterého se člověk dlouhodobě neobejde nebo který je nutný pro běžné fungování — například jídlo, bydlení, doprava do školy nebo práce, léky, základní oblečení.")
            st.write("**Přání** je výdaj, který zvyšuje pohodlí, radost nebo status, ale není nezbytný — například nové značkové oblečení, dražší telefon, streamovací služby navíc, kosmetika, herní doplňky nebo časté objednávání jídla.")

            st.markdown("#### 🧩 Třídič: Je to potřeba, nebo přání?")
            
            p_q1 = st.selectbox("1. Nájemné nebo poplatek za kolej / bydlení:", ["Vyber...", "Potřeba", "Přání"], key="k2_p_q1")
            p_q2 = st.selectbox("2. Třetí aktivní streamovací služba (Netflix/Spotify/Disney):", ["Vyber...", "Potřeba", "Přání"], key="k2_p_q2")
            p_q3 = st.selectbox("3. Základní jídlo a potraviny v e-shopu/supermarketu:", ["Vyber...", "Potřeba", "Přání"], key="k2_p_q3")
            p_q4 = st.selectbox("4. Každodenní objednávání hotového jídla přes rozvoz:", ["Vyber...", "Potřeba", "Přání"], key="k2_p_q4")
            p_q5 = st.selectbox("5. Předepsané léky nebo jízdné do školy:", ["Vyber...", "Potřeba", "Přání"], key="k2_p_q5")

            if st.button("Vyhodnotit potřeby a přání", key="k2_potreby_btn"):
                if p_q1 == "Potřeba" and p_q2 == "Přání" and p_q3 == "Potřeba" and p_q4 == "Přání" and p_q5 == "Potřeba":
                    st.success("🎉 Skvěle! Přesně rozumíš hranici mezi nezbytnou potřebou a volitelným přáním.")
                else:
                    st.error("Některé položky jsou zařazeny špatně. Potřeba je nutná k přežití a fungování, přání zvyšuje komfort.")

    # =========================================================================
    # 2.2 ROZPOČET: MAPA PENĚZ
    # =========================================================================
    elif "2.2 Rozpočet" in selected_section_2:
        st.markdown("<div class='sub-section-header'>2. OSOBNÍ FINANCE A „ALGORITMY BOHATSTVÍ“</div><h2>2.2 Rozpočet: mapa peněz</h2>", unsafe_allow_html=True)
        st.write("Rozpočet ukazuje, odkud peníze přicházejí a kam odcházejí. Bez rozpočtu člověk často neví, jestli má problém s nízkými příjmy, vysokými výdaji, impulzivním utrácením, dluhy nebo chybějící rezervou.")

        with st.container(border=True):
            st.markdown("""
            <div class='box-blue'>
                🧭 <strong>Jednoduše řečeno:</strong> Rozpočet není trest ani omezování života. Je to mapa. Pomáhá zjistit, jestli peníze směřují k tomu, co je pro člověka opravdu důležité.
            </div>
            """, unsafe_allow_html=True)

        # 2.2.1 Příjmy
        with st.container(border=True):
            st.markdown("### 2.2.1 Příjmy")
            st.write("Příjmy jsou peníze, které člověk získává. Mohou být pravidelné nebo nepravidelné.")

            st.markdown("""
            | Typ příjmu | Příklad | Na co si dát pozor |
            | :--- | :--- | :--- |
            | **Pravidelný příjem** | mzda, brigáda, kapesné, stipendium | Lze s ním lépe plánovat. |
            | **Nepravidelný příjem** | jednorázová odměna, prodej věcí, sezónní brigáda | Není dobré na něm stavět pravidelné výdaje. |
            | **Pasivnější příjem** | úrok, dividenda, příjem z pronájmu | Většinou vyžaduje kapitál, čas nebo riziko. |
            """)

        # 2.2.2 Výdaje
        with st.container(border=True):
            st.markdown("### 2.2.2 Výdaje")
            st.write("Výdaje je vhodné rozdělit podle toho, jak snadno je lze změnit.")

            st.markdown("""
            | Typ výdaje | Příklad | Otázka ke kontrole |
            | :--- | :--- | :--- |
            | **Fixní výdaj** | nájem, paušál, předplatné, splátka | Opravdu ho potřebuji každý měsíc? |
            | **Proměnlivý výdaj** | jídlo, doprava, drogerie, zábava | Dá se upravit bez zásadního poklesu kvality života? |
            | **Jednorázový výdaj** | telefon, oprava, dovolená, školní pomůcky | Mám na něj připravené peníze dopředu? |
            | **Skrytý výdaj** | automatické předplatné, poplatky, mikrotransakce | Vím, kolik mě stojí za rok? |
            """)

            st.markdown("<div class='box-yellow'><strong>🧩 Interaktivní výzva:</strong> Projdi si posledních 10 plateb v mobilním bankovnictví. Rozděl je na potřeby, přání a skryté nebo automatické výdaje.</div>", unsafe_allow_html=True)
            st.text_area("Zapiš svou analýzu posledních 10 plateb:", key="k2_last_10_payments")

        # 2.2.3 Pravidlo 50-30-20
        with st.container(border=True):
            st.markdown("### 2.2.3 Jednoduché pravidlo pro rozpočet (50–30–20)")
            st.write("Jedním z možných pravidel je model **50–30–20**:")
            st.markdown("""
            * **50 %** na potřeby,
            * **30 %** na přání,
            * **20 %** na rezervu, spoření, investování nebo splácení dluhů.
            """)

            st.markdown("""
            <div class='box-gray'>
                ⚖️ <strong>Pozor na zjednodušení:</strong> Pravidlo 50–30–20 není povinnost a nemusí fungovat pro každého. Někdo má vysoké náklady na bydlení, někdo nízký příjem, někdo splácí dluh. Smyslem pravidla je ukázat princip: část peněz má pokrýt dnešek, část radost a část budoucnost.
            </div>
            """, unsafe_allow_html=True)

            st.markdown("#### 🧮 Kalkulačka rozpočtu 50–30–20")
            b_income = st.number_input("Zadej svůj měsíční čistý příjem (Kč):", value=20000, step=1000, key="k2_budget_calc_inc")
            
            c_needs = b_income * 0.50
            c_wants = b_income * 0.30
            c_saves = b_income * 0.20

            col_b1, col_b2, col_b3 = st.columns(3)
            col_b1.metric("Potřeby (50 %)", f"{c_needs:,.0f} Kč".replace(",", " "))
            col_b2.metric("Přání (30 %)", f"{c_wants:,.0f} Kč".replace(",", " "))
            col_b3.metric("Rezerva / Úspory (20 %)", f"{c_saves:,.0f} Kč".replace(",", " "))

    # =========================================================================
    # 2.3 ALGORITMY BOHATSTVÍ
    # =========================================================================
    elif "2.3 Algoritmy" in selected_section_2:
        st.markdown("<div class='sub-section-header'>2. OSOBNÍ FINANCE A „ALGORITMY BOHATSTVÍ“</div><h2>2.3 Algoritmy bohatství: malé návyky, velký rozdíl</h2>", unsafe_allow_html=True)
        st.write("Slovo „algoritmus“ tu neznamená počítačový program. Znamená opakovatelný postup, který člověku pomáhá rozhodovat se lépe. Bohatství nevzniká jen jedním velkým rozhodnutím. Často vzniká z malých pravidelných kroků, které se opakují dlouhou dobu.")

        with st.container(border=True):
            st.markdown("""
            <div class='box-blue'>
                🔁 <strong>Algoritmus finanční stability:</strong><br>
                1. Nejdřív zaplať nutné výdaje.<br>
                2. Hned po příjmu odlož část peněz stranou.<br>
                3. Utrať jen to, co zůstane po odložení rezervy.<br>
                4. Vyhýbej se drahému dluhu.<br>
                5. Pravidelně kontroluj, kam peníze mizí.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 2.3.1 Zaplať nejdřív sobě")
            st.write("Princip „zaplať nejdřív sobě“ znamená, že člověk nečeká, jestli mu na konci měsíce něco zbyde. Část peněz si odloží hned po přijetí příjmu.")
            st.write("Příklad:")
            st.markdown("""
            * přijde výplata nebo brigáda,
            * pokud používáš pravidlo 50–30–20, odložíš 20 %, případně začneš s menší částkou (třeba 10 % nebo pevná částka),
            * teprve zbytek je určený na běžné výdaje.
            """)
            st.write("**Proč to funguje?** Když člověk čeká, co zbyde, často nezbyde nic. Digitální platby, drobné nákupy, jídlo venku, doprava, předplatná a impulzivní objednávky peníze postupně „rozpustí“. Automatické odložení peněz snižuje závislost na vůli.")

        with st.container(border=True):
            st.markdown("### 2.3.2 Automatizace pomáhá, ale musí být pod kontrolou")
            st.write("Automatické platby mohou být užitečné: pomáhají platit včas, odkládat rezervu nebo pravidelně spořit. Zároveň ale mohou vytvářet výdaje, kterých si člověk nevšímá.")

            st.markdown("""
            <div class='box-purple'>
                🤖 <strong>AI mentoring:</strong> Zkopíruj tento prompt do AI asistenta:<br>
                <em>„Pomoz mi najít v mém měsíčním rozpočtu tři automatické výdaje, které bych měl/a zkontrolovat, a navrhni, jak poznám, jestli mi za to stojí.“</em>
            </div>
            """, unsafe_allow_html=True)

    # =========================================================================
    # 2.4 MATEMATIKA PENĚZ
    # =========================================================================
    elif "2.4 Matematika" in selected_section_2:
        st.markdown("<div class='sub-section-header'>2. OSOBNÍ FINANCE A „ALGORITMY BOHATSTVÍ“</div><h2>2.4 Matematika peněz: čas, úrok a inflace</h2>", unsafe_allow_html=True)
        st.write("Peníze mají časovou hodnotu. Stokoruna dnes nemá stejnou hodnotu jako stokoruna za deset let, protože ceny se mění a peníze mohou nést úrok nebo výnos.")

        # 2.4.1 Jednoduché úročení
        with st.container(border=True):
            st.markdown("### 2.4.1 Jednoduché úročení")
            st.write("Jednoduché úročení znamená, že se úrok počítá stále jen z původně vložené nebo půjčené částky. Úroky se v dalších obdobích nepřičítají k základu pro další úročení.")

            st.markdown("""
            <div class='box-gray'>
                🧮 <strong>Vzorec pro jednoduché úročení:</strong><br>
                $$K = J \\times (1 + r \\times t)$$<br>
                • <strong>K</strong> = konečná částka<br>
                • <strong>J</strong> = jistina (původní vklad)<br>
                • <strong>r</strong> = roční úroková sazba v desetinném tvaru (např. 5 % = 0,05)<br>
                • <strong>t</strong> = čas v letech
            </div>
            """, unsafe_allow_html=True)

            st.write("**Příklad jednoduchého úročení:** Vložíš 10 000 Kč na 3 roky s roční úrokovou sazbou 5 %. Úrok se počítá pořád jen z původních 10 000 Kč.")
            st.write("Výpočet: $K = 10\\ 000 \\times (1 + 0{,}05 \\times 3) = 10\\ 000 \\times 1{,}15 = 11\\ 500\\ \\text{Kč}$. Za 3 roky získáš úrok 1 500 Kč.")

        # 2.4.2 Složené úročení
        with st.container(border=True):
            st.markdown("### 2.4.2 Složené úročení")
            st.write("Složené úročení znamená, že se úročí nejen původní částka, ale postupně i již připsané úroky nebo výnosy. Peníze tedy mohou vydělávat další peníze.")

            st.markdown("""
            <div class='box-gray'>
                🧮 <strong>Vzorec pro složené úročení:</strong><br>
                $$K = J \\times (1 + r)^n$$<br>
                • <strong>K</strong> = konečná částka<br>
                • <strong>J</strong> = jistina<br>
                • <strong>r</strong> = úroková sazba za období v desetinném tvaru<br>
                • <strong>n</strong> = počet úročených období
            </div>
            """, unsafe_allow_html=True)

            st.write("**Příklad složeného úročení:** Vložíš 10 000 Kč na 3 roky s roční úrokovou sazbou 5 %. Úrok se každý rok připíše k částce a další rok se úročí i tento připsaný úrok.")
            st.write("Výpočet: $K = 10\\ 000 \\times (1 + 0{,}05)^3 = 10\\ 000 \\times 1{,}157625 = 11\\ 576{,}25\\ \\text{Kč}$. Za 3 roky získáš úrok 1 576,25 Kč.")

            st.markdown("""
            | Typ úročení | Z čeho se počítá úrok | Výsledek při 10 000 Kč, 5 % p.a., 3 roky |
            | :--- | :--- | :--- |
            | **Jednoduché úročení** | Pořád z původní částky | **11 500,00 Kč** |
            | **Složené úročení** | Z původní částky i z připsaných úroků | **11 576,25 Kč** |
            """)

            st.markdown("#### 🧮 Srovnávací kalkulačka: Jednoduché vs. Složené úročení")
            col_u1, col_u2, col_u3 = st.columns(3)
            with col_u1:
                jistina_input = st.number_input("Vklad J (Kč):", value=10000, step=1000, key="k2_u_jistina")
            with col_u2:
                sazba_input = st.number_input("Sazba r (% p.a.):", value=5.0, step=0.5, key="k2_u_sazba")
            with col_u3:
                roky_input = st.number_input("Čas t (roky):", value=3, step=1, key="k2_u_roky")

            r_dec = sazba_input / 100.0
            res_jednoduse = jistina_input * (1 + r_dec * roky_input)
            res_slozene = jistina_input * ((1 + r_dec) ** roky_input)
            diff_urok = res_slozene - res_jednoduse

            c_u_res1, c_u_res2, c_u_res3 = st.columns(3)
            c_u_res1.metric("Jednoduché úročení", f"{res_jednoduse:,.2f} Kč".replace(",", " "))
            c_u_res2.metric("Složené úročení", f"{res_slozene:,.2f} Kč".replace(",", " "))
            c_u_res3.metric("Rozdíl ve prospěch složeného", f"+{diff_urok:,.2f} Kč".replace(",", " "))

            with st.expander("✍️ Procvičování: Spočítej úročení (3 příklady)"):
                st.write("**1. Jednoduché úročení:** Vložíš 8 000 Kč na 2 roky při sazbě 4 % p.a.")
                ex1_ans = st.number_input("Zadej vypočtenou konečnou částku (Kč):", value=0, key="k2_ex1_val")
                if st.button("Zkontrolovat příklad 1", key="k2_ex1_btn"):
                    if abs(ex1_ans - 8640) < 1:
                        st.success("✅ Správně! K = 8 000 × (1 + 0,04 × 2) = 8 640 Kč. Úrok je 640 Kč.")
                    else:
                        st.error("Chyba. Výpočet: 8000 * (1 + 0.04 * 2) = 8 640 Kč.")

                st.write("**2. Složené úročení:** Vložíš 8 000 Kč na 2 roky při sazbě 4 % p.a. (roční připisování).")
                ex2_ans = st.number_input("Zadej vypočtenou konečnou částku (Kč):", value=0.0, step=0.1, key="k2_ex2_val")
                if st.button("Zkontrolovat příklad 2", key="k2_ex2_btn"):
                    if abs(ex2_ans - 8652.80) < 1:
                        st.success("✅ Správně! K = 8 000 × (1 + 0,04)² = 8 652,80 Kč. Rozdíl je 12,80 Kč.")
                    else:
                        st.error("Chyba. Výpočet: 8000 * (1.04)^2 = 8 652,80 Kč.")

                st.write("**3. Porovnání delšího období (5 let, 15 000 Kč, 6 % p.a.):**")
                st.write("• Jednoduché: $15\\ 000 \\times (1 + 0{,}06 \\times 5) = 19\\ 500\\ \\text{Kč}$")
                st.write("• Složené: $15\\ 000 \\times (1 + 0{,}06)^5 = 20\\ 073{,}38\\ \\text{Kč}$")
                st.info("💡 Rozdíl je **573,38 Kč** ve prospěch složeného úročení. Čím delší doba, tím více se projevuje efekt úroků z úroků.")

        # 2.4.3 Inflace
        with st.container(border=True):
            st.markdown("### 2.4.3 Inflace")
            st.write("Inflace znamená růst cenové hladiny. Když ceny rostou, za stejnou částku si koupíme méně než dříve.")
            st.write("Oficiální inflace je průměr za celou ekonomiku. Každý človek ale může mít jinou **„osobní inflaci“**. Student, rodina s dětmi, senior nebo človek dojíždějící autem vnímají zdražování jinak, protože utrácejí za jiné věci.")

            st.markdown("<div class='box-yellow'><strong>🧩 Interaktivní výzva:</strong> Vyber pět věcí, které pravidelně kupuješ. Zjisti nebo odhadni, kolik stály dříve a kolik stojí dnes. Která položka zdražila nejvíc?</div>", unsafe_allow_html=True)
            st.text_area("Seznam 5 věcí a odhad změny ceny:", key="k2_inflation_5_items")

    # =========================================================================
    # 2.5 FINANČNÍ REZERVA
    # =========================================================================
    elif "2.5 Finanční rezerva" in selected_section_2:
        st.markdown("<div class='sub-section-header'>2. OSOBNÍ FINANCE A „ALGORITMY BOHATSTVÍ“</div><h2>2.5 Finanční rezerva: airbag osobních financí</h2>", unsafe_allow_html=True)
        st.write("Finanční rezerva chrání člověka před tím, aby každá nečekaná situace skončila dluhem. Může jít o rozbitý telefon, ztrátu brigády, nemoc, opravu auta, vyšší vyúčtování energií nebo stěhování.")

        with st.container(border=True):
            st.markdown("""
            <div class='box-blue'>
                🛟 <strong>Jednoduše řečeno:</strong> Rezerva je finanční airbag. Doufáš, že ji nebudeš potřebovat, ale když přijde náraz, může zabránit větším škodám.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 2.5.1 Jak velká má být rezerva")
            st.write("Obecné doporučení bývá mít rezervu alespoň ve výši 3 až 6 měsíců nutných výdajů. U studenta může být začátek menší: třeba první cíl 1 000 Kč, potom 5 000 Kč, potom jeden měsíc výdajů.")

            st.markdown("""
            | Životní situace | První rozumný cíl | Silnější rezerva |
            | :--- | :--- | :--- |
            | **Student s podporou rodiny** | 1 000–5 000 Kč | 1 měsíc vlastních výdajů |
            | **Člověk na brigádě nebo v první práci** | 1 měsíc nutných výdajů | 3 měsíce nutných výdajů |
            | **Samostatně žijící človek** | 3 měsíce nutných výdajů | 6 měsíců nutných výdajů |
            | **Rodina nebo podnikatel** | 3–6 měsíců nutných výdajů | více podle rizika příjmů |
            """)

            st.markdown("#### 🧮 Kalkulačka cílové finanční rezervy")
            user_sit = st.selectbox("Zvol svou aktuální životní situaci:", [
                "Student s podporou rodiny",
                "Člověk na brigádě / v první práci",
                "Samostatně žijící človek",
                "Rodina nebo podnikatel"
            ], key="k2_res_sit")
            
            m_exp = st.number_input("Zadej své měsíční nutné výdaje (Kč):", value=8000, step=1000, key="k2_res_m_exp")

            if "Student" in user_sit:
                r_min, r_target = 3000, m_exp * 1
            elif "brigádě" in user_sit:
                r_min, r_target = m_exp * 1, m_exp * 3
            elif "Samostatně" in user_sit:
                r_min, r_target = m_exp * 3, m_exp * 6
            else:
                r_min, r_target = m_exp * 6, m_exp * 9

            col_res1, col_res2 = st.columns(2)
            col_res1.metric("Minimální základní rezerva", f"{r_min:,.0f} Kč".replace(",", " "))
            col_res2.metric("Doporučená optimální rezerva", f"{r_target:,.0f} Kč".replace(",", " "))

        with st.container(border=True):
            st.markdown("### 2.5.2 Kde rezervu držet")
            st.write("Rezerva má být bezpečná a dostupná. Není určena k riskantnímu investování. Vhodné vlastnosti:")
            st.markdown("""
            * rychlá dostupnost,
            * nízké riziko ztráty,
            * oddělení od běžného účtu,
            * možnost použít ji při nečekané situaci.
            """)

            st.markdown("""
            <div class='box-red'>
                🚫 <strong>Častá chyba:</strong> Investovat nouzovou rezervu do rizikových aktiv. Když pak přijde problém, může být človek nucen prodat v nevýhodnou chvíli se ztrátou.
            </div>
            """, unsafe_allow_html=True)

    # =========================================================================
    # 2.6 PSYCHOLOGIE UTRÁCENÍ
    # =========================================================================
    elif "2.6 Psychologie" in selected_section_2:
        st.markdown("<div class='sub-section-header'>2. OSOBNÍ FINANCE A „ALGORITMY BOHATSTVÍ“</div><h2>2.6 Psychologie utrácení: proč nerozhodujeme vždy racionálně</h2>", unsafe_allow_html=True)
        st.write("Lidé nejsou kalkulačky. Často se rozhodujeme podle emocí, únavy, tlaku okolí, reklamy, strachu, že něco propásneme, nebo podle toho, co nám ukáže aplikace.")

        with st.container(border=True):
            st.markdown("### 2.6.1 Nejčastější pasti")
            st.markdown("""
            | Past | Jak funguje | Obrana |
            | :--- | :--- | :--- |
            | **FOMO** | Strach, že mi něco uteče. | Počkej 24 hodin před nákupem. |
            | **Sleva** | Pocit úspory, i když kupuji zbytečnost. | Ptej se: koupil/a bych to i bez slevy? |
            | **Sociální srovnávání** | Chci životní styl, který vidím u ostatních. | Rozliš realitu a vybraný obsah na sítích. |
            | **Mikrotransakce** | Malé částky vypadají neškodně. | Spočítej roční součet. |
            | **Odložená platba (BNPL)** | Nákup nebolí hned. | Ber ji jako dluh, ne jako slevu. |
            """)

        with st.container(border=True):
            st.markdown("### 2.6.2 Algoritmy a personalizovaná reklama")
            st.write("E-shopy, sociální sítě a aplikace sbírají data o tom, co sledujeme, hledáme, lajkujeme a kupujeme. Díky tomu nám mohou ukazovat nabídky, které přesně míří na naše zájmy, slabiny nebo aktuální náladu.")

            st.markdown("""
            <div class='box-purple'>
                📱 <strong>Moderní realita:</strong> Dříve človek viděl stejnou reklamu jako ostatní v televizi nebo časopise. Dnes může každý vidět jinou reklamu podle toho, co o něm platforma ví. Proto je finanční gramotnost propojená s digitální gramotností.
            </div>
            """, unsafe_allow_html=True)

            st.write("**Jak poznat, že mě prostředí tlačí k nákupu?**")
            st.markdown("""
            * Vidím odpočet času nebo nápis „zbývají poslední kusy“.
            * Aplikace mi nabízí dopravu zdarma až od určité částky.
            * Po jednom vyhledávání mě produkt pronásleduje v reklamách.
            * Influencer ukazuje produkt jako součást úspěšného životního stylu.
            * Platba je tak jednoduchá, že skoro nevnímám, že utrácím.
            """)

            st.markdown("<div class='box-yellow'><strong>🧩 Interaktivní výzva:</strong> Najdi jednu reklamu nebo nabídku, která tě nedávno zaujala. Popiš, jakou emoci používá: strach, radost, tlak na výkon, pocit výhodné koupě, krásu, úspěch, pohodlí nebo srovnávání s ostatními.</div>", unsafe_allow_html=True)
            st.text_area("Popis reklamy a emoce, kterou využívala:", key="k2_ad_emotion_analysis")

    # =========================================================================
    # 2.7 KALKULAČKA ČASU NÁKUPU
    # =========================================================================
    elif "2.7 Kalkulačka" in selected_section_2:
        st.markdown("<div class='sub-section-header'>2. OSOBNÍ FINANCE A „ALGORITMY BOHATSTVÍ“</div><h2>2.7 Kalkulačka času: kolik života stojí nákup</h2>", unsafe_allow_html=True)
        st.write("Cena věci není jen částka v korunách. Dá se přepočítat i na čas, který musí človek pracovat, aby si ji mohl dovolit.")

        with st.container(border=True):
            st.markdown("""
            <div class='box-gray'>
                ⏱️ <strong>Vzorec pro výpočet časové ceny:</strong><br>
                $$\\text{Čas práce (hodiny)} = \\frac{\\text{Cena věci (Kč)}}{\\text{Čistá hodinová mzda (Kč/h)}}$$
            </div>
            """, unsafe_allow_html=True)

            st.write("**Příklad:** Sluchátka stojí 2 400 Kč. Čistá hodinová mzda z brigády je 150 Kč. $2\\ 400 \\div 150 = 16\\ \\text{hodin práce}$.")

            st.markdown("#### ⏳ Interaktivní kalkulačka času nákupu")
            col_t1, col_t2 = st.columns(2)
            with col_t1:
                price_item = st.number_input("Cena plánovaného nákupu (Kč):", value=2400, step=100, key="k2_time_price")
            with col_t2:
                wage_hourly = st.number_input("Tvoje čistá hodinová mzda / odměna (Kč/hod):", value=150, step=10, key="k2_time_wage")

            if wage_hourly > 0:
                hours_needed = price_item / wage_hourly
                st.metric("Počet hodin práce nutný na tento nákup", f"{hours_needed:.1f} hodin")
                st.info(f"👉 Aby sis mohl/a koupit tuto věc za **{price_item} Kč**, musíš strávit v práci **{hours_needed:.1f} hodin**. Stojí ti to za ten čas?")

    # =========================================================================
    # 2.8 OSOBNÍ FINANČNÍ AUDIT
    # =========================================================================
    elif "2.8 Osobní" in selected_section_2:
        st.markdown("<div class='sub-section-header'>2. OSOBNÍ FINANCE A „ALGORITMY BOHATSTVÍ“</div><h2>2.8 Praktický výstup: můj osobní finanční audit</h2>", unsafe_allow_html=True)
        st.write("Na konci této části by měl být človek schopný udělat jednoduchý audit vlastních financí.")

        with st.container(border=True):
            st.markdown("#### ✅ Kontrolní checklist osobního auditu")
            st.write("Zaškrtni body, které už bezpečně ovládáš a uplatňuješ:")

            st.checkbox("1. Vím, jaké mám pravidelné příjmy.", key="k2_audit_chk1")
            st.checkbox("2. Vím, kam mi odcházejí peníze.", key="k2_audit_chk2")
            st.checkbox("3. Znám své automatické platby a předplatná.", key="k2_audit_chk3")
            st.checkbox("4. Mám plán, jak tvořit rezervu.", key="k2_audit_chk4")
            st.checkbox("5. Umím rozlišit potřebu, přání a impulzivní nákup.", key="k2_audit_chk5")
            st.checkbox("6. Chápu, že inflace snižuje kupní sílu peněz.", key="k2_audit_chk6")
            st.checkbox("7. Umím přepočítat cenu věci na hodiny práce.", key="k2_audit_chk7")
            st.checkbox("8. Vím, že digitální prostředí ovlivňuje moje finanční rozhodování.", key="k2_audit_chk8")

            st.markdown("""
            <div class='box-purple'>
                🤖 <strong>AI mentoring:</strong> Zkopíruj tento prompt do AI asistenta:<br>
                <em>„Pomoz mi udělat osobní finanční audit. Zeptej se mě postupně na příjmy, pravidelné výdaje, předplatná, rezervu, dluhy a finanční cíle. Na konci mi navrhni tři malé změny na příští měsíc.“</em>
            </div>
            """, unsafe_allow_html=True)
# =========================================================================
    # 3. FINANČNÍ TRH A ANALÝZA RIZIK
    # =========================================================================
# =========================================================================
    # 3.1 CO JE TO FINANČNÍ TRH A BURZA
    # =========================================================================
    elif "3.1 Co je" in selected_section_2:
        st.markdown("<div class='sub-section-header'>3. FINANČNÍ TRH A ANALÝZA RIZIK</div><h2>3.1 Co je to finanční trh</h2>", unsafe_allow_html=True)
        
        st.write("Finanční trh umožňuje, aby se peníze přesouvaly od těch, kteří je mají k dispozici, k těm, kteří je chtějí využít. Může jít o domácnosti, firmy, banky, investory, stát, obce, fondy nebo mezinárodní instituce.")
        
        st.write("**Představ si to jednoduše:**")
        st.markdown("""
        * člověk má úspory a nechce, aby mu jen ležely na účtu,
        * firma potřebuje peníze na rozšíření výroby,
        * stát si půjčuje na financování svých výdajů,
        * investor hledá příležitost, kde by peníze mohly pracovat,
        * banka, burza nebo investiční platforma pomáhá tyto strany propojit.
        """)
        
        st.info("🧠 **Finanční trh není kasino** — ale může se tak chovat, pokud člověk neví, co dělá. Rozdíl mezi odpovědným investováním a hazardem není jen v produktu, ale hlavně v informovanosti, riziku, časovém horizontu a chování člověka.")

        # 3.1.1
        with st.container(border=True):
            st.markdown("### 3.1.1 Hlavní funkce finančního trhu")
            st.write("Finanční trh má několik důležitých funkcí:")
            st.markdown("""
            | Funkce | Co znamená | Příklad |
            | :--- | :--- | :--- |
            | **Přesun kapitálu** | Volné peníze se dostávají k těm, kdo je potřebují. | Investor koupí dluhopis firmy, firma získá peníze na rozvoj. |
            | **Zhodnocení úspor** | Lidé a firmy hledají možnost, jak peníze ochránit před inflací nebo je rozmnožit. | Domácnost investuje pravidelně do fondu. |
            | **Stanovení ceny peněz a aktiv** | Trh ukazuje, za kolik se obchodují akcie, dluhopisy, měny nebo komodity. | Cena akcie se mění podle nabídky a poptávky. |
            | **Rozložení rizika** | Riziko lze rozdělit mezi více investorů nebo produktů. | Fond drží stovky akcií místo jedné. |
            | **Likvidita** | Některá aktiva lze rychleji prodat a proměnit zpět na peníze. | Akcii velké firmy lze často prodat rychleji než nemovitost. |
            """)

        # 3.1.2
        with st.container(border=True):
            st.markdown("### 3.1.2 Primární a sekundární trh")
            st.write("Finanční trh se často dělí na primární a sekundární.")
            st.markdown("""
            | Typ trhu | Co se děje | Příklad |
            | :--- | :--- | :--- |
            | **Primární trh** | Cenný papír se prodává poprvé. Peníze získává emitent — tedy ten, kdo cenný papír vydává. | Firma vydá nové akcie nebo stát vydá nový dluhopis. |
            | **Sekundární trh** | Investoři obchodují mezi sebou už dříve vydané cenné papíry. | Investor prodá akcii jiné osobě přes burzu. |
            """)
            st.write("**Příklad ze života**")
            st.write("Když si koupíš nově vydaný státní dluhopis přímo při emisi, jde o primární trh. Když později koupíš akcii od jiného investora přes burzu, firma už peníze z této konkrétní koupě nedostává — jde o sekundární trh.")

        # 3.1.3
        with st.container(border=True):
            st.markdown("### 3.1.3 Burza, broker a investiční platforma")
            st.write("**Burza** je organizovaný trh, kde se obchoduje podle pravidel. Neznamená to nutně hlučný sál s lidmi v oblecích. Dnes velká část obchodování probíhá elektronicky.")
            st.write("**Broker** je zprostředkovatel, přes kterého může investor nakupovat a prodávat investiční nástroje.")
            st.write("**Investiční aplikace** je uživatelské rozhraní, které může působit jednoduše jako e-shop. Právě proto je nutné zpomalit: to, že investici koupíš jedním klikem, neznamená, že jí rozumíš.")
            st.warning("📱 **Moderní riziko:** Investiční aplikace umí vytvořit pocit hry. Grafy, notifikace, zelená čísla a rychlé nákupy mohou člověka tlačit k impulzivnímu obchodování. Finanční gramotnost dnes znamená umět poznat, kdy aplikace pomáhá — a kdy manipuluje chováním.")

        # 3.1.4
        with st.container(border=True):
            st.markdown("### 3.1.4 Burza: organizované tržiště pro cenné papíry")
            st.write("Burza je organizovaný a regulovaný trh, kde se podle jasných pravidel obchoduje s investičními nástroji — nejčastěji s akciemi, dluhopisy, ETF, deriváty nebo komoditními nástroji. Burzu si mnoho lidí představuje jako hlučný sál plný makléřů, kteří křičí a mávají papíry. Tak to historicky opravdu někde vypadalo. Dnes je ale většina obchodování elektronická: objednávky se zadávají přes obchodní systémy, párují se automaticky a vypořádávají se přes specializované instituce.")
            st.info("🏛️ **Burza jednoduše:** Burza je jako přísně hlídané digitální tržiště. Neprodává se tam ovoce nebo oblečení, ale cenné papíry a další finanční nástroje. Aby obchodování fungovalo, musí mít pravidla, dohled, evidenci a systém, který určuje, kdo co koupil, za kolik a kdy se obchod vypořádá.")
            st.write("**Burza plní několik důležitých funkcí:**")
            st.markdown("""
            * umožňuje obchodování — investoři mohou nakupovat a prodávat cenné papíry,
            * pomáhá tvořit cenu — cena vzniká střetem nabídky a poptávky,
            * zvyšuje likviditu — investor má větší šanci najít kupce nebo prodávajícího,
            * zvyšuje transparentnost — u regulovaných trhů jsou pravidla, zveřejňování informací a dohled,
            * umožňuje firmám získat kapitál — například při vstupu na burzu nebo vydání dluhopisů,
            * poskytuje signál o důvěře trhu — vývoj cen může ukazovat očekávání investorů.
            """)

        # 3.1.5
        with st.container(border=True):
            st.markdown("### 3.1.5 Jak burza funguje krok za krokem")
            st.write("Když investor koupí akcii přes aplikaci, na obrazovce to vypadá jako jednoduché kliknutí. Ve skutečnosti za tím stojí celý řetězec institucí a pravidel.")
            st.write("**Zjednodušený průběh obchodu:**")
            st.markdown("""
            1. Investor zadá pokyn k nákupu nebo prodeji u brokera.
            2. Broker pokyn odešle na příslušný trh nebo obchodní místo.
            3. Obchodní systém hledá protistranu — někoho, kdo chce prodat nebo koupit za odpovídající cenu.
            4. Pokud se pokyny potkají, obchod se uzavře.
            5. Následuje vypořádání — převedou se peníze a cenné papíry.
            6. Investor vidí cenný papír na svém účtu a peníze se odečtou nebo připíšou.
            """)
            st.write("**Nabídka, poptávka a cena**")
            st.write("Cena na burze nevzniká tak, že ji někdo „od stolu“ vyhlásí jako cenu rohlíku v obchodě. Vzniká tím, že se potkávají kupující a prodávající. Pokud chce hodně lidí akcii koupit a málo lidí ji prodává, cena může růst. Pokud mnoho investorů prodává a málo kupuje, cena může klesat.")
            st.write("**Základní pojmy:**")
            st.markdown("""
            * **nákupní cena / bid** — cena, za kterou jsou kupující ochotni nakupovat,
            * **prodejní cena / ask** — cena, za kterou jsou prodávající ochotni prodávat,
            * **spread** — rozdíl mezi nákupní a prodejní cenou,
            * **objem obchodů** — kolik kusů nebo jaká hodnota se zobchodovala,
            * **likvidita** — jak snadno lze instrument koupit nebo prodat bez velkého pohybu ceny,
            * **vypořádání** — technické dokončení obchodu, tedy převod peněz a cenných papírů.
            """)

        # 3.1.6
        with st.container(border=True):
            st.markdown("### 3.1.6 Může na burze obchodovat každý?")
            st.write("Běžný občan většinou neobchoduje přímo na burze jako člen burzy. Obchoduje přes zprostředkovatele — například banku, obchodníka s cennými papíry nebo brokera. Tito zprostředkovatelé mají technický a právní přístup na trh nebo využívají další napojené instituce.")
            st.info("🚪 **Důležité rozlišení:** Občan může investovat do cenných papírů obchodovaných na burze, ale obvykle nevstupuje přímo do burzovního systému. Používá brokera, podobně jako cestující používá dopravce, neřídí celé nádraží.")
            st.write("**Co potřebuje běžný investor:**")
            st.markdown("""
            * vybrat regulovaného brokera, banku nebo obchodníka s cennými papíry,
            * ověřit totožnost,
            * vyplnit investiční dotazník,
            * poslat peníze na investiční účet,
            * rozumět poplatkům, měně, riziku a daňovým dopadům,
            * zadávat pokyny k nákupu nebo prodeji.
            """)
            st.write("**Kdo může obchodovat přímo jako člen burzy:**")
            st.markdown("""
            * banky,
            * obchodníci s cennými papíry,
            * specializované finanční instituce,
            * členové burzy splňující pravidla daného trhu.
            """)

        # 3.1.7
        with st.container(border=True):
            st.markdown("### 3.1.7 Kdo burzu spravuje a kdo na ni dohlíží")
            st.write("Burza není chaotická skupina investorů. Má provozovatele, pravidla, členy, dohled a technickou infrastrukturu.")
            st.write("**Na fungování burzy se podílí:**")
            st.markdown("""
            * **provozovatel burzy** — organizuje trh a nastavuje pravidla obchodování,
            * **členové burzy** — instituce oprávněné přímo obchodovat,
            * **emitenti** — firmy, státy nebo instituce, jejichž cenné papíry se obchodují,
            * **investoři** — domácnosti, firmy, fondy, banky, pojišťovny a další,
            * **clearingové a vypořádací instituce** — zajišťují dokončení obchodů,
            * **centrální depozitář** — vede evidenci zaknihovaných cenných papírů,
            * **regulátor** — dohlíží, zda trh dodržuje pravidla a chrání investory.
            """)
            st.write("V České republice hraje významnou roli Česká národní banka, která vykonává dohled nad finančním trhem. To neznamená, že ČNB určuje, za kolik má stát konkrétní akcie. Znamená to, že dohlíží na pravidla, instituce, ochranu trhu a férové fungování finančního systému.")

        # 3.1.8
        with st.container(border=True):
            st.markdown("### 3.1.8 Burza cenných papírů Praha")
            st.write("Burza cenných papírů Praha, zkráceně BCPP, je hlavní regulovaný akciový trh v České republice. Obchodují se zde například akcie významných českých nebo ve střední Evropě působících společností, dluhopisy a další investiční nástroje.")
            st.info("🇨🇿 **BCPP jednoduše:** Pražská burza je hlavní české organizované místo pro obchodování s cennými papíry. Pro české studenty je důležitá proto, že ukazuje, že kapitálový trh není jen Wall Street, ale existuje i v českém prostředí.")
            st.write("**Na pražské burze se lze setkat například s těmito pojmy:**")
            st.markdown("""
            * **Prime Market** — trh pro největší a nejvýznamnější emise,
            * **Standard Market** — trh pro další obchodované cenné papíry,
            * **Free Market** — trh s jednoduššími pravidly přijetí,
            * **START Market** — trh zaměřený na menší a střední firmy, které chtějí získat kapitál.
            """)
            st.write("**Pro firmy může být vstup na burzu způsobem, jak:**")
            st.markdown("""
            * získat kapitál na růst,
            * zvýšit důvěryhodnost a viditelnost,
            * umožnit investorům obchodovat s jejich akciemi,
            * vytvořit tržní ocenění firmy,
            * nabídnout akcie investorům nebo zaměstnancům.
            """)
            st.write("Pro investory burza znamená možnost koupit nebo prodat cenné papíry za tržní cenu. Zároveň ale platí, že i akcie známé firmy může klesnout. Známé jméno firmy není záruka výnosu.")

        # 3.1.9
        with st.container(border=True):
            st.markdown("### 3.1.9 RM-SYSTÉM: český trh dostupný i občanům")
            st.write("V českém prostředí existuje také RM-SYSTÉM, česká burza cenných papírů. Historicky navazuje na období kupónové privatizace a dlouhou dobu byl spojován s možností obchodování pro širší veřejnost. Dnes už nepůsobí tak moderně nebo mediálně výrazně jako velké investiční aplikace, ale stále jde o existující organizovaný trh, na kterém lze obchodovat vybrané cenné papíry.")
            st.info("🇨🇿 **Proč RM-SYSTÉM zmínit:** Ukazuje, že český kapitálový trh nemá jen pražskou burzu. RM-SYSTÉM je důležitý i historicky, protože byl spojen s přístupem drobných investorů k obchodování s českými akciemi.")
            st.write("**Jak RM-SYSTÉM funguje zjednodušeně:**")
            st.markdown("""
            * je to český trh pro obchodování s vybranými cennými papíry,
            * investor může obchodovat prostřednictvím oprávněného obchodníka nebo napojené služby,
            * obchoduje se elektronicky,
            * nabídka instrumentů je omezenější než na největších světových burzách,
            * pro běžného občana může být srozumitelnější tím, že je zaměřen na české prostředí,
            * i zde platí rizika investování, poplatky, kolísání cen a nutnost rozumět tomu, co člověk kupuje.
            """)
            st.warning("⚠️ **Pozor:** To, že je trh dostupný občanům, neznamená, že je bez rizika. Přístupnost není totéž co bezpečnost. I na českém trhu může investor prodělat, pokud kupuje bez znalostí, podle emocí nebo bez diverzifikace.")

        # 3.1.10
        with st.container(border=True):
            st.markdown("### 3.1.10 Nejznámější světové burzy")
            st.write("Světové burzy propojují firmy a investory v globálním měřítku. Některé jsou známé hlavně akciemi technologických firem, jiné širokým spektrem společností, jiné komoditami nebo deriváty.")
            st.markdown("""
            | Burza | Země / město | Čím je známá |
            | :--- | :--- | :--- |
            | **New York Stock Exchange / NYSE** | USA, New York | Jedna z největších světových burz, obchodují se zde akcie mnoha velkých tradičních firem. |
            | **Nasdaq** | USA | Silně spojený s technologickými firmami a elektronickým obchodováním. |
            | **London Stock Exchange / LSE** | Velká Británie, Londýn | Významné evropské a globální finanční centrum. |
            | **Tokyo Stock Exchange / TSE** | Japonsko, Tokio | Hlavní japonská burza a jedna z největších burz v Asii. |
            | **Shanghai Stock Exchange** | Čína, Šanghaj | Významný čínský akciový trh. |
            | **Hong Kong Stock Exchange** | Hongkong | Důležité propojení čínského a mezinárodního kapitálu. |
            | **Euronext** | Evropa | Propojuje více evropských trhů, například Paříž, Amsterdam, Brusel nebo Lisabon. |
            | **Deutsche Börse / Frankfurt Stock Exchange** | Německo, Frankfurt | Významný evropský trh, spojovaný například s indexem DAX. |
            """)
            st.write("**Proč se burzy liší?**")
            st.write("Burzy se liší velikostí, pravidly, typem obchodovaných firem, měnou, časovým pásmem, poplatky, likviditou a regulací. Pro investora je důležité vědět, že nákup americké akcie přes českou aplikaci znamená také měnové riziko, jiné obchodní hodiny a odlišné daňové nebo informační prostředí.")

        # 3.1.11
        with st.container(border=True):
            st.markdown("### 3.1.11 Burzovní indexy: teploměr trhu")
            st.write("Když média říkají, že „americký trh roste“ nebo „pražská burza klesla“, často tím nemyslí každou jednu akcii. Mluví o burzovním indexu. Index sleduje vybranou skupinu akcií a ukazuje jejich souhrnný vývoj.")
            st.write("**Příklady indexů:**")
            st.markdown("""
            * **PX** — index pražské burzy,
            * **S&P 500** — sleduje velké americké společnosti,
            * **Nasdaq Composite** — silně zastoupené technologické firmy,
            * **Dow Jones Industrial Average** — známý americký index velkých firem,
            * **DAX** — významný německý akciový index,
            * **FTSE 100** — významný britský index,
            * **Nikkei 225** — známý japonský index.
            """)
            st.info("🌡️ **Index jako teploměr:** Index neříká, že všechny firmy rostou nebo klesají stejně. Ukazuje průměrný nebo vážený vývoj vybrané skupiny firem. Je to orientační měřítko nálady a vývoje trhu.")

        # 3.1.12
        with st.container(border=True):
            st.markdown("### 3.1.12 Kdo na burze obchoduje")
            st.write("Na burze se potkávají různé typy účastníků:")
            st.markdown("""
            | Účastník | Co dělá | Příklad motivace |
            | :--- | :--- | :--- |
            | **Drobný investor** | Nakupuje menší objemy přes brokera nebo banku. | Dlouhodobé investování, dividenda, růst hodnoty. |
            | **Trader** | Obchoduje aktivněji a snaží se využít pohyb cen. | Krátkodobý zisk, vyšší riziko. |
            | **Investiční fond** | Spravuje peníze mnoha investorů. | Diverzifikované portfolio podle strategie. |
            | **Penzijní fond** | Spravuje peníze na dlouhodobé zabezpečení klientů. | Dlouhý horizont a řízení rizika. |
            | **Banka** | Obchoduje pro klienty nebo v rámci vlastního řízení rizik. | Likvidita, zajištění, investiční služby. |
            | **Firma / emitent** | Vydává akcie nebo dluhopisy, komunikuje s investory. | Získání kapitálu, důvěryhodnost, růst. |
            | **Market maker** | Pomáhá zajišťovat likviditu tím, že nabízí nákupní i prodejní ceny. | Vydělává na rozdílu cen a službě trhu. |
            """)

        # 3.1.13
        with st.container(border=True):
            st.markdown("### 3.1.13 Proč burza není totéž co kasino")
            st.write("Na burze může člověk spekulovat a chovat se podobně jako hazardní hráč. Burza sama o sobě ale není kasino. Rozdíl je v tom, že cenné papíry často představují reálná práva: podíl ve firmě, pohledávku za emitentem nebo podíl ve fondu. Problém nastává, když člověk nakupuje bez porozumění, podle emocí, podle videí na sociálních sítích nebo s penězi, které si nemůže dovolit ztratit.")
            st.info("🧠 **Zralé investiční chování:** Rozumím, co kupuji. Vím, proč to kupuji. Znám riziko. Nesázím všechno na jednu kartu. Nepanikařím při každém poklesu. Nepletu si investování se zábavní aplikací.")

        # Aktivita
        with st.container(border=True):
            st.markdown("#### 🎮 Aktivita: Staň se burzovním reportérem")
            st.write("Vyber jednu burzu nebo index: BCPP, RM-SYSTÉM, NYSE, Nasdaq, DAX, S&P 500 nebo PX.")
            st.write("**Zjisti a vysvětli:**")
            st.markdown("""
            * V jaké zemi nebo městě trh působí?
            * Co se na něm obchoduje?
            * Kdo na něm může obchodovat přímo a kdo přes brokera?
            * Jaký index se s ním spojuje?
            * Jaká firma nebo cenný papír je pro něj typický?
            * Jaké riziko by měl znát běžný investor?
            """)
            
            rep_market = st.selectbox("Vyber burzu/index pro report:", ["BCPP", "RM-SYSTÉM", "NYSE", "Nasdaq", "DAX", "S&P 500", "PX"], key="k3_rep_mkt")
            rep_firma = st.text_input("Zadej typickou firmu / cenný papír pro report:", value="ČEZ", key="k3_rep_firm")
            rep_riziko = st.text_input("Hlavní riziko pro běžného investora:", value="Tržní propad a volatilita", key="k3_rep_riziko")
            
            if st.button("Vygenerovat výstup reportéra", key="k3_rep_btn"):
                st.success(f"🎙️ **Zpráva z trhu {rep_market}:** „Dobrý den, hlásíme se ze světa financí! Dnes se pozornost investorů zaměřila na {rep_firma}. Nezapomínejme ale na klíčová rizika, mezi kterými dominuje {rep_riziko}. Investujte opatrně, přejeme vám úspěšný den a vracíme slovo do studia!“")
            st.caption("Výstup: Krátká zpráva ve stylu ekonomického podcastu pro spolužáky.")

# =========================================================================
    # 3.2 VÝNOS, RIZIKO, LIKVIDITA A ČAS
    # =========================================================================
    elif "3.2 Výnos" in selected_section_2:
        st.markdown("<div class='sub-section-header'>3. FINANČNÍ TRH A ANALÝZA RIZIK</div><h2>3.2 Výnos, riziko, likvidita a čas</h2>", unsafe_allow_html=True)
        
        st.write("Než se člověk začne bavit o konkrétních produktech, musí chápat čtyři základní otázky:")
        st.markdown("""
        * Jaký může být výnos?
        * Jaké nesu riziko?
        * Jak rychle se dostanu k penězům?
        * Na jak dlouho peníze odkládám?
        """)
        
        st.info("⚖️ **Investiční trojúhelník:** Výnos, riziko a likvidita spolu souvisejí. Vyšší možný výnos obvykle znamená vyšší riziko. Vysoký výnos, nulové riziko a okamžitá dostupnost peněz najednou jsou podezřelá kombinace.")

        # 3.2.1
        with st.container(border=True):
            st.markdown("### 3.2.1 Výnos")
            st.write("Výnos je to, co investor získá navíc oproti původně vložené částce. Může mít podobu:")
            st.markdown("""
            * úroku,
            * dividendy,
            * růstu ceny aktiva,
            * nájemného,
            * kurzového zisku,
            * kombinace více zdrojů.
            """)
            st.write("Výnos ale není totéž co jistota. U některých produktů je předvídatelnější, u jiných se může výrazně měnit.")

        # 3.2.2
        with st.container(border=True):
            st.markdown("### 3.2.2 Riziko")
            st.write("Riziko znamená možnost, že výsledek bude jiný, než člověk očekával. Může jít o nižší výnos, kolísání hodnoty, ztrátu části peněz nebo v extrémním případě ztrátu celé investice.")
            st.markdown("""
            | Druh rizika | Co znamená | Příklad |
            | :--- | :--- | :--- |
            | **Tržní riziko** | Cena aktiva kolísá podle vývoje trhu. | Akcie klesnou při ekonomické nejistotě. |
            | **Úvěrové riziko** | Dlužník nemusí splatit svůj závazek. | Firma nevykoupí dluhopis. |
            | **Likviditní riziko** | Aktivum nejde rychle prodat za rozumnou cenu. | Malý token nebo podíl v projektu nemá kupce. |
            | **Měnové riziko** | Změna kurzu měny ovlivní výsledek. | Investice v dolarech se přepočítává do korun. |
            | **Inflační riziko** | Výnos nestačí pokrýt růst cen. | Spoření nese 3 %, inflace je 6 %. |
            | **Regulační riziko** | Změna pravidel ovlivní dané aktivum nebo trh. | Stát zpřísní pravidla pro kryptoměnové služby. |
            | **Technologické riziko** | Selže systém, aplikace, úschova nebo zabezpečení. | Ztráta přístupu do kryptopeněženky. |
            """)

        # 3.2.3 a 3.2.4
        with st.container(border=True):
            st.markdown("### 3.2.3 Likvidita")
            st.write("Likvidita znamená, jak snadno lze aktivum proměnit zpět na peníze. Hotovost je velmi likvidní. Nemovitost bývá méně likvidní. Některé kryptoměnové tokeny mohou být prakticky nelikvidní, pokud je nikdo nechce koupit.")
            
            st.markdown("### 3.2.4 Časový horizont")
            st.write("Časový horizont je doba, po kterou člověk plánuje peníze nechat investované. Krátký horizont se nehodí pro vysoce kolísavé investice. Pokud člověk ví, že peníze bude potřebovat za tři měsíce, neměl by je vystavovat velkým výkyvům.")
            
            st.success("🧭 **Jednoduché pravidlo:** Nouzová rezerva patří do bezpečných a dostupných nástrojů. Investice s vyšším rizikem patří až k penězům, které člověk nepotřebuje na běžné výdaje ani na krizové situace.")

    # =========================================================================
    # 3.3 SPOŘENÍ, INVESTOVÁNÍ A SPEKULACE
    # =========================================================================
    elif "3.3 Spoření" in selected_section_2:
        st.markdown("<div class='sub-section-header'>3. FINANČNÍ TRH A ANALÝZA RIZIK</div><h2>3.3 Spoření, investování a spekulace</h2>", unsafe_allow_html=True)
        st.write("Tato tři slova se často pletou, ale znamenají rozdílné chování.")

        with st.container(border=True):
            st.markdown("""
            | Pojem | Co znamená | Typický příklad | Riziko |
            | :--- | :--- | :--- | :--- |
            | **Spoření** | Odkládání peněz s důrazem na bezpečnost a dostupnost. | Spořicí účet, termínovaný vklad. | Nízké, ale hrozí ztráta kupní síly kvůli inflaci. |
            | **Investování** | Vkládání peněz do aktiv s cílem dlouhodobého zhodnocení. | Akcie, dluhopisy, fondy, ETF. | Střední až vysoké podle produktu. |
            | **Spekulace** | Sázka na krátkodobý pohyb ceny. | Rychlé nákupy a prodeje kryptoměn nebo akcií podle trendu. | Vysoké. |
            """)
            
            st.warning("🧠 **Otázka před každým nákupem investice:** Kupuješ aktivum proto, že rozumíš jeho principu a riziku, nebo proto, že máš strach, že ti „ujede vlak“?")

    # =========================================================================
    # 3.4 CENNÉ PAPÍRY V TEORII I PRAXI
    # =========================================================================
    elif "3.4 Cenné" in selected_section_2:
        st.markdown("<div class='sub-section-header'>3. FINANČNÍ TRH A ANALÝZA RIZIK</div><h2>3.4 Cenné papíry v teorii i praxi</h2>", unsafe_allow_html=True)
        st.write("Cenný papír je listina nebo digitální záznam, se kterým jsou spojena určitá práva (podíl ve firmě, splacení dluhu, úrok). Dnes je většina cenných papírů v praxi zaknihovaná — existuje jako elektronický záznam.")
        
        with st.container(border=True):
            st.markdown("### 3.4.1 Jak cenný papír vypadá dnes")
            st.markdown("""
            | Podoba | Jak vypadá | Příklad |
            | :--- | :--- | :--- |
            | **Listinný** | Fyzická listina (název, hodnota, práva, podpisy). | Historická akcie, směnka. |
            | **Zaknihovaný** | Elektronický záznam v evidenci. | Moderní akcie na burze, ETF. |
            """)

        with st.container(border=True):
            st.markdown("### 3.4.2 - 3.4.6 Akcie: podíl na firmě")
            st.write("Koupí akcie se stáváš akcionářem, tedy spoluvlastníkem malé části firmy.")
            st.markdown("""
            * **Kmenová akcie:** Běžná akcie (hlasovací právo, podíl na zisku).
            * **Prioritní akcie:** Přednostní dividenda, ale často omezené hlasování.
            """)
            st.write("**Jmenovitá hodnota vs. tržní cena:** Jmenovitá je účetní hodnota (např. 100 Kč), tržní je cena na burze (např. 850 Kč).")

        with st.container(border=True):
            st.markdown("### 3.4.7 - 3.4.10 Dluhopis: půjčka se slibem splacení")
            st.write("Koupí dluhopisu se nestáváš vlastníkem firmy, ale jejím věřitelem.")
            st.markdown("""
            | Druh dluhopisu | Co znamená | Typické riziko |
            | :--- | :--- | :--- |
            | **Státní** | Vydává stát. | Závisí na důvěryhodnosti státu. |
            | **Firemní** | Vydává firma. | Firma nemusí vydělat na splacení. |
            | **Hypoteční zástavní list** | Krytý hypotečními úvěry. | Kvalita zajištění. |
            """)
            st.error("⚠️ **Pozor:** Dluhopis není automaticky bezpečný. Vysoký úrok často znamená vyšší riziko nesplacení.")

        with st.container(border=True):
            st.markdown("### 3.4.11 - 3.4.14 Podílové listy a fondy")
            st.write("Místo jedné konkrétní akcie kupuješ „košík“ investic. Fond shromažďuje peníze investorů a investuje podle strategie.")
            st.markdown("""
            * **Akciový fond:** Akcie firem (vyšší kolísání).
            * **Dluhopisový fond:** Dluhopisy (úrokové a úvěrové riziko).
            * **ETF (Exchange Traded Fund):** Fond obchodovaný na burze, často sleduje index.
            """)

        with st.container(border=True):
            st.markdown("### 3.4.18 Praktická aktivita: pitva cenného papíru")
            cp_typ = st.selectbox("Vyber aktivum:", ["Akcie ČEZ", "Státní dluhopis ČR", "Podílový fond", "S&P 500 ETF"], key="k3_pitva1")
            cp_riziko = st.radio("Zvol odhadované riziko:", ["Nízké", "Střední", "Vysoké"], horizontal=True, key="k3_pitva2")
            
            if st.button("Vygenerovat rodný list", key="k3_pitva_btn"):
                st.success(f"🔎 **Rodný list:** Vybral jsi {cp_typ}. Tvé odhadované riziko: {cp_riziko}. Vždy si zjisti emitenta, poplatky a likviditu před nákupem!")

        with st.container(border=True):
            st.markdown("### 3.4.19 Srovnání základních produktů")
            st.markdown("""
            | Produkt | Možný výnos | Hlavní riziko | Pro koho se hodí |
            | :--- | :--- | :--- | :--- |
            | **Spořicí účet** | Úrok | Inflace | Rezerva, krátkodobé cíle |
            | **Dluhopis** | Úrok / kupón | Emitent nesplatí | Znalý investor |
            | **Akcie** | Růst ceny, dividenda | Pokles ceny firmy/trhu | Dlouhodobý investor |
            | **ETF fond** | Podle vývoje trhu | Tržní pokles | Začátečník i pokročilý |
            """)

    # =========================================================================
    # 3.5 ANALÝZA DAT A ŠKOLNÍ INVESTIČNÍ SIMULÁTOR
    # =========================================================================
    elif "3.5 Analýza" in selected_section_2:
        st.markdown("<div class='sub-section-header'>3. FINANČNÍ TRH A ANALÝZA RIZIK</div><h2>3.5 Analýza dat: investiční laboratoř</h2>", unsafe_allow_html=True)
        st.write("Investiční rozhodování nemá stát na větě „kamarád říkal“ nebo videu z TikToku. Důležitá je práce s daty.")
        
        st.warning("⚠️ **Varování před grafem:** Historická data jsou užitečná, ale nejsou zárukou budoucnosti. Graf začínající ve vhodně vybraném roce může vypadat skvěle, ale skrývat velký předchozí propad.")

        with st.container(border=True):
            st.markdown("### 🚀 SPUSTIT ŠKOLNÍ INVESTIČNÍ SIMULÁTOR")
            st.write("Vyzkoušej si modelové investování nanečisto — bez skutečných peněz a bez rizika. Sleduj, jak se může měnit hodnota portfolia v čase.")

            sim_mesicne = st.number_input("Měsíční pravidelná úspora (Kč):", value=1000, step=500, key="k3_sim_m")
            sim_roky = st.slider("Doba investování (roky):", min_value=1, max_value=30, value=10, key="k3_sim_r")
            
            st.write("**Rozdělení portfolia (%):**")
            col1, col2, col3 = st.columns(3)
            p_etf = col1.number_input("Akcie/ETF (oč. 7% p.a.)", value=70, min_value=0, max_value=100, step=10, key="k3_sim_e")
            p_bond = col2.number_input("Dluhopisy (oč. 3% p.a.)", value=20, min_value=0, max_value=100, step=10, key="k3_sim_b")
            p_krypto = col3.number_input("Krypto (spekulace 12% p.a.)", value=10, min_value=0, max_value=100, step=10, key="k3_sim_k")

            if p_etf + p_bond + p_krypto != 100:
                st.error("⚠️ Součet musí být přesně 100 %!")
            else:
                avg_rate = (p_etf * 0.07 + p_bond * 0.03 + p_krypto * 0.12) / 100.0
                r_m = avg_rate / 12.0
                n_months = sim_roky * 12
                
                total_dep = sim_mesicne * n_months
                total_val = 0.0
                for _ in range(n_months):
                    total_val = (total_val + sim_mesicne) * (1 + r_m)

                c1, c2, c3 = st.columns(3)
                c1.metric("Celkem vloženo", f"{total_dep:,.0f} Kč".replace(",", " "))
                c2.metric("Hodnota na konci", f"{total_val:,.0f} Kč".replace(",", " "))
                c3.metric("Zisk z trhu", f"+{(total_val - total_dep):,.0f} Kč".replace(",", " "))
                st.caption("Poznámka: Simulátor je pouze vzdělávací pomůcka a počítá s teoretickým průměrem. Nejde o investiční doporučení.")

    # =========================================================================
    # 3.6 KRYPTOMĚNY: TECHNOLOGIE, SPEKULACE A RIZIKO
    # =========================================================================
    elif "3.6 Kryptoměny" in selected_section_2:
        st.markdown("<div class='sub-section-header'>3. FINANČNÍ TRH A ANALÝZA RIZIK</div><h2>3.6 Kryptoměny: technologie, peníze, spekulace i riziko</h2>", unsafe_allow_html=True)
        st.write("Kryptoměny spojují technologie, internetovou kulturu, možnost rychlého zisku a nedůvěru k institucím.")
        
        st.info("🪙 **Kryptoměna jednoduše:** Digitální aktivum, které existuje v počítačové síti. Záznamy nejsou vedeny jednou bankou, ale sdílenou evidencí (blockchainem).")
        st.warning("🚫 **Důležité:** Tato kapitola není investiční doporučení. Cílem je rozumět principu, rizikům a trikům.")

        with st.container(border=True):
            st.markdown("### 3.6.1 a 3.6.2 Blockchain")
            st.write("Blockchain si představ jako třídní účetní knihu, kterou nemá jeden pokladník, ale kopii má mnoho lidí v síti. Je těžké do ní zapsat podvodnou platbu, protože by si toho ostatní kopie všimly.")

        with st.container(border=True):
            st.markdown("### 3.6.3 Peněženka a klíče")
            st.markdown("""
            | Pojem | Co znamená | Přirovnání |
            | :--- | :--- | :--- |
            | **Veřejná adresa** | Adresa pro příjem krypto. | Číslo účtu. |
            | **Soukromý klíč** | Tajný údaj pro podepsání transakce. | Klíč k trezoru. |
            | **Seed phrase** | Sada slov pro obnovení peněženky. | Hlavní master klíč. |
            """)
            st.error("🔐 **Pravidlo:** Kdo zná tvůj soukromý klíč nebo seed phrase, má tvé peníze. Banka ti heslo neobnoví!")

        with st.container(border=True):
            st.markdown("### 3.6.4 Druhy a mechanismy")
            st.write("**Bitcoin:** První kryptoměna. **Ethereum:** Síť pro chytré kontrakty. **Stablecoiny:** Navázané na dolar. **Meme coiny:** Extrémní spekulace založená na virálním trendu.")

        with st.container(border=True):
            st.markdown("### 3.6.8 a 3.6.9 Rizika a podvody")
            st.write("Cena kolísá (volatilita). Hrozí ztráta přístupu, hack burzy nebo podvod.")
            st.markdown("""
            **Varovné signály:**
            * Slib „garantovaného výnosu“ a „bez rizika“.
            * Tlak na rychlé rozhodnutí.
            * Někdo chce tvou seed phrase.
            """)
            st.error("🚨 **Pravidlo:** Pokud nerozumíš tomu, odkud se bere výnos, pravděpodobně nejsi investor — jsi zdroj peněz pro někoho jiného.")

        with st.container(border=True):
            st.markdown("#### 🧪 Krypto detektiv: ověř projekt")
            kd_name = st.text_input("Zadej název tokenu:", value="MemeDogeCoin", key="k3_kd1")
            kd_vynos = st.selectbox("Slibovaný výnos:", ["Závisí na trhu", "Garantovaných 10 % měsíčně", "Bez rizika"], key="k3_kd2")
            
            if st.button("Analyzovat", key="k3_kd_btn"):
                if kd_vynos == "Závisí na trhu":
                    st.success(f"✅ U tokenu {kd_name} výnos závisí na trhu. Pamatuj ale na extrémní volatilitu a riziko ztráty.")
                else:
                    st.error(f"🔴 **POZOR PODVOD!** Pokud projekt {kd_name} slibuje '{kd_vynos}', vykazuje hlavní znaky krypto podvodu (scamu).")

    # =========================================================================
    # 3.7 OCHRANA SPOTŘEBITELE A INVESTIČNÍ REKLAMA
    # =========================================================================
    elif "3.7 Ochrana" in selected_section_2:
        st.markdown("<div class='sub-section-header'>3. FINANČNÍ TRH A ANALÝZA RIZIK</div><h2>3.7 Ochrana spotřebitele a investiční reklama</h2>", unsafe_allow_html=True)
        st.write("Finanční produkty se často prodávají jazykem emocí. Reklama může zdůraznit svobodu, rychlý zisk nebo strach z promarněné šance.")
        
        with st.container(border=True):
            st.markdown("### Typické věty, u kterých zpozornět:")
            st.markdown("""
            * „Začni vydělávat pasivně hned.“
            * „Tuhle příležitost nesmíš propásnout.“
            * „Garantovaný výnos.“
            * „Vydělávají na tom všichni.“
            * „Stačí kopírovat moje obchody.“
            * „Banky nechtějí, abys to věděl/a.“
            """)
            
            st.success("🛡️ **Ochrana spotřebitele začíná otázkou:** Kdo mi to nabízí, jak na tom vydělává, jaké riziko mi neříká a proč mám rozhodnout právě teď?")

    # =========================================================================
    # 3.8 INTERAKTIVNÍ AKTIVITY A CVIČEBNICE
    # =========================================================================
    elif "3.8 Interaktivní" in selected_section_2:
        st.markdown("<div class='sub-section-header'>3. FINANČNÍ TRH A ANALÝZA RIZIK</div><h2>3.8 Interaktivní aktivity k finančnímu trhu</h2>", unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 🧩 Třídění: spoření, investice, spekulace, hazard")
            t1 = st.selectbox("Spořicí účet:", ["Spoření", "Investování", "Spekulace", "Hazard"], key="k3_t1")
            t2 = st.selectbox("ETF na široký index:", ["Spoření", "Investování", "Spekulace", "Hazard"], index=1, key="k3_t2")
            t3 = st.selectbox("Nákup meme coinu podle TikToku:", ["Spoření", "Investování", "Spekulace", "Hazard"], index=2, key="k3_t3")
            
            if st.button("Vyhodnotit", key="k3_t_btn"):
                st.success("Skvělé! Chápeš rozdíl mezi bezpečím, dlouhodobým růstem a rizikovým hazardem.")

        with st.container(border=True):
            st.markdown("### 📉 Investiční počasí")
            st.write("Trh spadl o 30 %.")
            st.text_area("Co udělá impulzivní začátečník a co udělá informovaný investor?", key="k3_pocasi")

        with st.container(border=True):
            st.markdown("### 📊 Čtení grafu bez iluzí")
            st.write("Otázky k zamyšlení: Jaké období graf ukazuje? Co by se změnilo, kdyby začínal v jiném roce? Jsou započteny poplatky?")

    # =========================================================================
    # 3.9 SHRNUTÍ: CO SI Z FINANČNÍHO TRHU ODNÉST
    # =========================================================================
    elif "3.9 Shrnutí" in selected_section_2:
        st.markdown("<div class='sub-section-header'>3. FINANČNÍ TRH A ANALÝZA RIZIK</div><h2>3.9 Shrnutí: co si z finančního trhu odnést</h2>", unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("""
            ✅ **Klíčové věty:**
            * Vyšší možný výnos obvykle znamená vyšší riziko.
            * Spoření, investování a spekulace nejsou totéž.
            * Diverzifikace snižuje závislost na jednom aktivu, ale neruší riziko.
            * Historický výnos není slib budoucího výnosu.
            * Kryptoměny je nutné chápat jako vysoce rizikové digitální aktivum, ne jako jistý recept na zbohatnutí.
            * Pokud nerozumím produktu, poplatkům, rizikům a zdroji výnosu, neměl/a bych do něj vkládat peníze.
            """)
            
            st.info("🤖 **AI mentoring:** Zkopíruj tento prompt do AI asistenta: *„Vysvětli mi rozdíl mezi spořením, investováním a spekulací na příkladu studenta, který má 10 000 Kč. U každé možnosti popiš výnos, riziko, likviditu a vhodný časový horizont.“*")

    # =========================================================================
    # 3.10 PRÁVNÍ A ETICKÝ DISCLAIMER
    # =========================================================================
    elif "3.10 Právní" in selected_section_2:
        st.markdown("<div class='sub-section-header'>3. FINANČNÍ TRH A ANALÝZA RIZIK</div><h2>3.10 Právní a etický disclaimer</h2>", unsafe_allow_html=True)

        with st.container(border=True):
            st.write("Všechny příklady, výpočty, grafy a scénáře v této kapitole slouží pouze ke vzdělávání. Nejde o investiční doporučení, investiční poradenství ani výzvu k nákupu nebo prodeji konkrétního aktiva. Každý finanční produkt má rizika a každý člověk má jinou životní situaci, rezervu, příjem, cíle a schopnost snášet ztrátu.")
