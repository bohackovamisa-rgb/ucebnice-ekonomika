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

 # 📌 JEDNOTNÁ NABÍDKA PODKAPITOL
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
        "3.10 Právní a etický disclaimer",

        # Sekce 4: Úvěry, pojištění a ochrana majetku
        "4.1 Co je úvěr",
        "4.2 Úrok: cena půjčených peněz",
        "4.3 RPSN: skutečnější cena úvěru",
        "4.4 Ne každý úvěr dostane",
        "4.5 Postup poskytnutí spotřebitelského úvěru",
        "4.6 Hypotéka: úvěr na bydlení",
        "4.7 Podnikatelské úvěry",
        "4.8 Když se splácení pokazí",
        "4.9 Past jménem „Kup teď, zaplať později“",
        "4.10 Pojištění: ochrana před finančním nárazem",
        "4.11 Životní pojištění",
        "4.12 Neživotní pojištění",
        "4.13 Jak poznat dobré pojištění",
        "4.14 Praktické rozhodování: úvěr a pojištění dohromady",
        "4.15 Shrnutí: co si odnést",

        # Sekce 5: Finanční řízení v podniku — most k podnikavosti
        "5.1 Proč podnik řeší finance",
        "5.2 Základní finanční výkazy: mapa firmy v číslech",
        "5.3 Náklady, výnosy a bod zvratu",
        "5.4 Zdroje financování podniku",
        "5.5 Finanční analýza: kontrola finančního zdraví",
        "5.6 Modelová finanční analýza: e-shop „DropZone“",
        "5.7 Prázdná šablona finanční analýzy k vyplnění",
        "5.8 Jak napsat závěr finanční analýzy",
        "5.9 Case study: Influencer jako firma",
        "5.10 Digitální generace a finanční řízení",
        "5.11 Praktická aktivita: finanční manažer na 45 minut",
        "5.12 Shrnutí: co si odnést",

        # Závěrečné moduly
        "6. Interaktivní vrstva celé kapitoly",
        "7. Aktivita",
        "8. Slovník cizích pojmů"
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
            st.write("Bankovky mají ochranné prvky proto, aby bylo možné ověřit jejich pravost a snížit riziko padělání. Nejde jen o „ozdobu“ bankovky. Ochranné prvky pomáhají běžným lidem, obchodníkům, bankám i státu poznat, zda je bankovka skutečná a zda jí mohou důvěřovať.")

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

            st.markdown("##### 🔎 Interaktivní aktivita: Ochranné prvky peněz (1000 Kč - František Palacký)")
            st.write("Zvol prvek v nabídce níže, sleduj jeho přesné umístění přímo na reálné bankovce a zjisti, jak ho v praxi ověřit:")

            # Bezpečné načtení obrázku 1000 Kč do Base64
            @st.cache_data
            def get_bankovka_1000_base64():
                import os, base64
                # 1. Pokus o načtení z lokálního souboru v repozitáři
                local_paths = ["1000_czk.jpg", "kapitoly/1000_czk.jpg", "assets/1000_czk.jpg"]
                for path in local_paths:
                    if os.path.exists(path):
                        with open(path, "rb") as img_f:
                            return f"data:image/jpeg;base64,{base64.b64encode(img_f.read()).decode()}"
                
                # 2. Stažení z webu s plnými Chrome hlavičkami
                try:
                    import requests
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
                    }
                    url = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/1000_Czech_koruna_Obverse.jpg/800px-1000_Czech_koruna_Obverse.jpg"
                    resp = requests.get(url, headers=headers, timeout=5)
                    if resp.status_code == 200:
                        return f"data:image/jpeg;base64,{base64.b64encode(resp.content).decode()}"
                except Exception:
                    pass
                return None

            img_base64 = get_bankovka_1000_base64()

            # Databáze prvků pro 1000 Kč s Františkem Palackým
            prvky_bankovky = {
                "Vodoznak (pohledem)": {
                    "ikona": "💧",
                    "top": "48%", "left": "14%",
                    "nazev": "Vodoznak (František Palacký)",
                    "misto": "Levý nepotištěný okraj bankovky",
                    "popis": "Zřetelný stínovaný portrét Františka Palackého s číselným označením '1000' a motivem lipového listu, viditelný z obou stran při pohledu proti světlu.",
                    "kontrola": "👀 **Jak zkontrolovat:** Zvedni bankovku a podívej se na nepotištěný levý okraj proti světelnému zdroji."
                },
                "Ochranný proužek (pohledem)": {
                    "ikona": "📏",
                    "top": "50%", "left": "55.8%",
                    "nazev": "Ochranný proužek s mikrotextem",
                    "misto": "Svislý metalický pás zapuštěný do papíru (uprostřed bankovky)",
                    "popis": "Tmavý okenníkový proužek z pokovené umělé hmoty s negativním mikrotextem 'ČNB 1000 Kč'. Při naklonění mění barvu z hnědofialové na zelenou.",
                    "kontrola": "☀️ **Jak zkontrolovat:** Podívej se na bankovku proti světlu (vidíš souvislý pás) nebo ji nakloň a sleduj proměnu barev."
                },
                "Soutisková značka (pohledem)": {
                    "ikona": "🧩",
                    "top": "14.5%", "left": "29.5%",
                    "nazev": "Soutisková značka (CS / ČR)",
                    "misto": "Horní část bankovky vlevo od stromu",
                    "popis": "Oboustranný tisk kroužku s písmeny. Z lícní strany vidíš jen část, z rubové druhou část. Proti světlu se přesně doplňují v celistvý symbol.",
                    "kontrola": "🔍 **Jak zkontrolovat:** Prohlédni si značku proti světlu – obě poloviny vytvoří přesný kruhový symbol."
                },
                "Opticky proměnlivá barva (naklopením)": {
                    "ikona": "🎨",
                    "top": "18.5%", "left": "41.5%",
                    "nazev": "Opticky proměnlivá barva (Lipový list)",
                    "misto": "Horní část stromu nad nápisem TISÍC",
                    "popis": "Stylizovaný lipový list vytištěný speciální barvou. Při naklonění bankovky mění barvu ze zlatavé/hnědé na zelenou.",
                    "kontrola": "🔄 **Jak zkontrolovat:** Nakloň bankovku pod úhlem naproti světlu – sleduj proměnu barvy lipového listu."
                },
                "Reliéfní tisk (hmatem)": {
                    "ikona": "🖐️",
                    "top": "48%", "left": "70%",
                    "nazev": "Reliéfní tisk (Portrét Františka Palackého)",
                    "misto": "Portrét Palackého, texty a hmatové značky",
                    "popis": "Vystouplý povrch hlubotisku nahmatatelný prsty na lícové straně bankovky.",
                    "kontrola": "👉 **Jak zkontrolovat:** Přejeď bříškem prstu po portrétu Františka Palackého nebo po nápisu 'TISÍC KORUN ČESKÝCH'."
                },
                "Hmatová značka pro nevidomé (hmatem)": {
                    "ikona": "🔲",
                    "top": "9%", "left": "93%",
                    "nazev": "Hmatová značka pro nevidomé",
                    "misto": "Pravý horní roh lícní strany",
                    "popis": "Speciální vystouplé čárky vytištěné hlubotiskem v pravém horním rohu, které slouží zrakově postiženým k rozpoznání hodnoty 1000 Kč.",
                    "kontrola": "👉 **Jak zkontrolovat:** Nahmatáš prstem vystoupené svislé čárky v pravém rohu."
                },
                "UV prvky (pomůckami)": {
                    "ikona": "🔦",
                    "top": "75%", "left": "41.5%",
                    "nazev": "UV prvky a fluorescenční vlákna",
                    "misto": "Kořeny stromu a plocha bankovky",
                    "popis": "Skryté tiskové motivy (světélkující zelená a žlutá vlákna a tisk v oblasti kořenů), které reagují pod ultrafialovým světlem.",
                    "kontrola": "💡 **Jak zkontrolovat:** Posviť na bankovku UV lampou v bance nebo v obchodě."
                }
            }

            p_sel = st.selectbox(
                "Zvol ochranný prvek pro zobrazení popisu:",
                list(prvky_bankovky.keys()),
                key="k2_1_2_4_bankovka_sel"
            )

            det = prvky_bankovky[p_sel]

            # Vykreslení obrázku nebo vektorové zálohy
            if img_base64:
                html_bankovka = (
                    f'<div style="position: relative; width: 100%; max-width: 650px; margin: 15px auto; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">'
                    f'<img src="{img_base64}" alt="1000 Kč - František Palacký" style="width: 100%; height: auto; display: block;" />'
                    f'<div style="position: absolute; top: {det["top"]}; left: {det["left"]}; transform: translate(-50%, -50%); z-index: 10;">'
                    f'<div style="background-color: #ef4444; color: white; width: 38px; height: 38px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 18px; border: 2.5px solid white; box-shadow: 0 0 15px #ef4444;">'
                    f'{det["ikona"]}'
                    f'</div></div></div>'
                )
            else:
                # Vektorová záloha bankovky 1000 Kč
                html_bankovka = (
                    f'<div style="position: relative; width: 100%; max-width: 650px; height: 260px; background: linear-gradient(135deg, #f5e6f0 0%, #d8b4e2 100%); border: 2px solid #8e44ad; border-radius: 10px; margin: 15px auto; overflow: hidden; font-family: sans-serif;">'
                    f'<div style="position: absolute; top: 10px; left: 15px; font-weight: 900; color: #4a154b; font-size: 24px;">1000 Kč</div>'
                    f'<div style="position: absolute; top: 12px; left: 35%; font-weight: bold; color: #4a154b; font-size: 13px;">ČESKÁ NÁRODNÍ BANKA</div>'
                    f'<div style="position: absolute; top: 20%; right: 8%; width: 120px; height: 160px; border: 1px solid #8e44ad; border-radius: 8px; background: rgba(255,255,255,0.3); display: flex; flex-direction: column; align-items: center; justify-content: center; color: #4a154b;">'
                    f'<div style="font-size: 50px;">👨‍💼</div>'
                    f'<div style="font-size: 11px; font-weight: bold; text-align: center;">FRANTIŠEK PALACKÝ</div>'
                    f'</div>'
                    f'<div style="position: absolute; top: {det["top"]}; left: {det["left"]}; transform: translate(-50%, -50%); z-index: 10;">'
                    f'<div style="background-color: #ef4444; color: white; width: 38px; height: 38px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 18px; border: 2.5px solid white; box-shadow: 0 0 15px #ef4444;">'
                    f'{det["ikona"]}'
                    f'</div></div></div>'
                )

            st.markdown(html_bankovka, unsafe_allow_html=True)

            # Kartička s detailem
            st.info(f"{det['ikona']} **{det['nazev']}** ({det['misto']})\n\n{det['popis']}\n\n{det['kontrola']}")
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
        
        st.write("Cenný papír je listina nebo digitální záznam, se kterým jsou spojena určitá práva. Může jít například o právo na podíl ve firmě, právo na splacení dluhu, právo na úrok, právo na dividendu nebo právo podílet se na majetku fondu. Dříve si lidé pod cenným papírem představili hlavně fyzický papír s názvem firmy, hodnotou, podpisy a ochrannými prvky. Dnes je většina cenných papírů v praxi zaknihovaná — existuje jako elektronický záznam v evidenci.")
        
        st.info("🧾 **Cenný papír jednoduše:** Není důležité jen to, jak „vypadá“. Důležité je, jaké právo představuje. U akcie jde o vlastnictví části firmy. U dluhopisu jde o půjčku. U podílového listu jde o podíl na majetku fondu.")
        
        st.write("**Cenné papíry používají:**")
        st.markdown("""
        * **domácnosti a drobní investoři** — ke spoření, investování a tvorbě majetku,
        * **podnikatelé a firmy** — k uložení volných peněz, získání kapitálu, řízení likvidity nebo financování rozvoje,
        * **banky, pojišťovny a fondy** — k profesionálnímu řízení peněz a rizik,
        * **stát a obce** — hlavně prostřednictvím dluhopisů k financování svých potřeb,
        * **velké korporace** — při emisích akcií, dluhopisů, akvizicích, fúzích a správě firemní hotovosti.
        """)

        # 3.4.1
        with st.container(border=True):
            st.markdown("### 3.4.1 Jak cenný papír vypadá dnes")
            st.write("Cenný papír může mít dvě základní podoby:")
            st.markdown("""
            | Podoba | Jak vypadá | Příklad |
            | :--- | :--- | :--- |
            | **Listinný cenný papír** | Fyzická listina. Může obsahovat název emitenta, hodnotu, práva vlastníka, datum vydání, podpisy, razítka nebo ochranné prvky. | Historická akcie, listinný dluhopis, směnka. |
            | **Zaknihovaný cenný papír** | Elektronický záznam v evidenci. Investor ho vidí na investičním účtu nebo v aplikaci. | Moderní akcie obchodovaná na burze, státní dluhopis, ETF. |
            """)
            
            st.write("**U cenného papíru nebo v jeho elektronickém záznamu se obvykle uvádí:**")
            st.markdown("""
            * emitent — kdo cenný papír vydal,
            * druh cenného papíru — akcie, dluhopis, podílový list atd.,
            * jmenovitá hodnota nebo počet kusů,
            * práva vlastníka,
            * datum vydání,
            * měna,
            * identifikátor — často například ISIN,
            * u dluhopisu také úrok, splatnost a emisní podmínky,
            * u akcie také druh akcie a hlasovací práva,
            * u fondu také správce, strategie, poplatky a riziková kategorie.
            """)
            st.info("📱 **Jak to vidí student v aplikaci:** Obvykle nevidí papírovou listinu, ale název instrumentu, ticker, ISIN, aktuální cenu, měnu, graf, počet kusů, hodnotu pozice, poplatky a tlačítko koupit/prodat.")

        # 3.4.2 až 3.4.4
        with st.container(border=True):
            st.markdown("### 3.4.2 Akcie: podíl na firmě")
            st.write("Akcie představuje podíl na akciové společnosti. Když investor koupí akcii, stává se akcionářem, tedy spoluvlastníkem malé části firmy. Neznamená to, že může přijít do firmy a odnést si počítač nebo židli. Znamená to, že má určitá práva podle zákona, stanov společnosti a druhu akcie.")
            st.write("Firma vydává akcie hlavně proto, aby získala vlastní kapitál. Na rozdíl od úvěru nebo dluhopisu tyto peníze nemusí klasicky splatit. Na oplátku ale přijímá akcionáře — tedy vlastníky, kteří očekávají růst hodnoty firmy, dividendy nebo vliv na rozhodování.")
            
            st.info("🏢 **Akcie v jedné větě:** Koupí akcie firmě nepůjčuješ. Kupuješ si kousek jejího vlastnictví a podílíš se na jejím úspěchu i neúspěchu.")
            
            st.write("**Akcionář může mít:**")
            st.markdown("""
            * právo na dividendu, pokud ji firma vyplácí,
            * hlasovací právo na valné hromadě, pokud ho daný druh akcie obsahuje,
            * právo na informace podle pravidel společnosti,
            * právo podílet se na likvidačním zůstatku, pokud firma zaniká a po zaplacení dluhů něco zůstane,
            * možnost akcii prodat, pokud je převoditelná a existuje kupec.
            """)

            st.markdown("### 3.4.3 Druhy akcií")
            st.write("Akcie nejsou všechny stejné. Liší se podle práv, podoby i způsobu obchodování.")
            st.markdown("""
            | Druh akcie | Co znamená | Jak to vysvětlit studentům |
            | :--- | :--- | :--- |
            | **Kmenová akcie** | Nejběžnější akcie. Obvykle dává právo hlasovat a podílet se na zisku. | Klasický „kousek firmy“. |
            | **Prioritní akcie** | Může dávat přednostní právo na dividendu, ale někdy omezuje hlasovací právo. | Investor může mít přednost u výnosu, ale menší vliv. |
            | **Akcie na jméno** | Je spojena s konkrétním vlastníkem zapsaným v evidenci. | Firma ví, kdo je akcionářem. |
            | **Akcie na majitele** | Vlastník je určen evidencí nebo držením podle právní úpravy; moderně jde často o zaknihovanou podobu. | Dnes nerozhoduje „papír v ruce“, ale evidence. |
            | **Zaknihovaná akcie** | Existuje jako elektronický záznam. | Nejběžnější forma u akcií na burze. |
            | **Listinná akcie** | Má podobu fyzické listiny. | Dnes méně běžná, ale dobře ukazuje původ pojmu cenný papír. |
            | **Veřejně obchodovaná akcie** | Obchoduje se na burze nebo regulovaném trhu. | Má veřejně dostupnou cenu a obvykle vyšší likviditu. |
            | **Neveřejně obchodovaná akcie** | Není běžně dostupná na burze. | Prodej může být složitější a méně transparentní. |
            """)

            st.markdown("### 3.4.4 Co je napsáno na akcii")
            st.write("**Na listinné akcii nebo v elektronickém záznamu akcie bývá uvedeno:**")
            st.markdown("""
            * název akciové společnosti,
            * sídlo a identifikační údaje společnosti,
            * druh a forma akcie,
            * jmenovitá hodnota,
            * počet akcií nebo označení konkrétní akcie,
            * datum emise,
            * údaje o převoditelnosti,
            * podpisy nebo potvrzení vydání u listinné podoby,
            * identifikátor cenného papíru.
            """)
            
            st.write("**Jmenovitá hodnota vs. tržní cena akcie**")
            st.write("Jmenovitá hodnota je účetní nebo právní hodnota uvedená na akcii nebo ve stanovách. Tržní cena je cena, za kterou se akcie aktuálně prodává na trhu. Tyto částky se mohou výrazně lišit. Akcie může mít jmenovitou hodnotu 100 Kč, ale na trhu se může obchodovat za 850 Kč nebo za 40 Kč.")

        # 3.4.5 a 3.4.6
        with st.container(border=True):
            st.markdown("### 3.4.5 Jak se akcie kupují a prodávají")
            st.write("Běžný člověk si většinou nekupuje akcie přímo od firmy. Nejčastěji je kupuje přes banku, brokera, obchodníka s cennými papíry nebo investiční platformu.")
            st.write("**Typický postup u fyzické osoby nepodnikatele:**")
            st.markdown("""
            1. Vybere si regulovanou banku, brokera nebo investiční platformu.
            2. Ověří totožnost.
            3. Vyplní investiční dotazník.
            4. Pošle peníze na investiční účet.
            5. Vyhledá akcii podle názvu, tickeru nebo ISIN.
            6. Zadá pokyn k nákupu.
            7. Po vypořádání obchodu vidí akcii na svém účtu.
            """)
            
            st.write("**Základní typy pokynů:**")
            st.markdown("""
            * **market pokyn** — nákup nebo prodej za aktuální dostupnou cenu,
            * **limitní pokyn** — investor stanoví maximální nákupní nebo minimální prodejní cenu,
            * **stop pokyn** — aktivuje se až po dosažení určité ceny.
            """)
            st.warning("⚠️ **Pozor:** To, že lze akcii koupit během pár sekund, neznamená, že je rozhodnutí jednoduché. Investor by měl vědět, co firma dělá, jak vydělává, jaké má dluhy, konkurenci, rizika, měnu obchodování a poplatky.")

            st.markdown("### 3.4.6 Jak akcie používají firmy a velké společnosti")
            st.write("**Firmy používají akcie hlavně k financování a změnám vlastnické struktury:**")
            st.markdown("""
            * **založení akciové společnosti** — vlastníci vloží kapitál a získají akcie,
            * **navýšení kapitálu** — firma vydá nové akcie a získá peníze,
            * **IPO** — první veřejná nabídka akcií, tedy vstup firmy na burzu,
            * **další emise akcií** — firma později vydá nové akcie,
            * **akvizice** — firma může použít vlastní akcie při koupi jiné firmy,
            * **zaměstnanecké akcie a opce** — motivace zaměstnanců podílem na růstu firmy,
            * **zpětný odkup akcií** — firma nakupuje vlastní akcie z trhu.
            """)
            st.write("Velké firmy s akciemi neobchodují jako student v aplikaci. Často využívají investiční banky, právní poradce, makléře, burzy, blokové obchody a neveřejné transakce. Řeší nejen cenu, ale také vlastnickou kontrolu, dopad na kurz akcie, pověst, regulaci a vztahy s investory.")

        # 3.4.7 až 3.4.10
        with st.container(border=True):
            st.markdown("### 3.4.7 Dluhopis: půjčka se slibem splacení")
            st.write("Dluhopis je cenný papír, kterým si emitent půjčuje peníze. Emitentem může být stát, obec, banka nebo firma. Investor dluhopis koupí a tím emitentovi půjčí. Emitent se zavazuje, že peníze vrátí a obvykle zaplatí úrok.")
            st.info("💸 **Dluhopis v jedné větě:** Koupí dluhopisu se nestáváš vlastníkem firmy. Stáváš se jejím věřitelem.")
            
            st.write("**Základní logika dluhopisu:**")
            st.markdown("""
            1. Emitent potřebuje peníze.
            2. Vydá dluhopisy.
            3. Investor dluhopis koupí.
            4. Emitent vyplácí úrok nebo jiný výnos.
            5. Na konci splatnosti vrátí jmenovitou hodnotu, pokud je schopný splácet.
            """)
            
            st.markdown("""
            | Pojem | Význam |
            | :--- | :--- |
            | **Emitent** | Ten, kdo dluhopis vydává a půjčuje si peníze. |
            | **Jmenovitá hodnota** | Částka, kterou má emitent při splatnosti vrátit. |
            | **Kupón** | Úrok nebo pravidelný výnos vyplácený investorovi. |
            | **Splatnost** | Datum, kdy má být dluhopis splacen. |
            | **Emisní kurz** | Cena, za kterou se dluhopis prodává při vydání. |
            | **Výnos do splatnosti** | Celkový výnos, pokud investor drží dluhopis do splatnosti a emitent splní závazky. |
            | **Rating** | Hodnocení schopnosti emitenta splácet závazky. |
            """)

            st.markdown("### 3.4.8 Druhy dluhopisů")
            st.write("Dluhopisy se liší podle emitenta, výnosu, splatnosti a rizika.")
            st.markdown("""
            | Druh dluhopisu | Co znamená | Typické riziko |
            | :--- | :--- | :--- |
            | **Státní dluhopis** | Vydává ho stát. | Riziko závisí na důvěryhodnosti státu. |
            | **Municipální dluhopis** | Vydává ho obec, město nebo kraj. | Schopnost samosprávy splácet. |
            | **Firemní dluhopis** | Vydává ho firma. | Firma nemusí vydělat dost peněz na splacení. |
            | **Bankovní dluhopis** | Vydává ho banka. | Závisí na stabilitě banky a typu dluhopisu. |
            | **Hypoteční zástavní list** | Speciální dluhopis krytý pohledávkami z hypotečních úvěrů. | Kvalita zajištění a hypotečního portfolia. |
            | **Dluhopis s pevným kupónem** | Vyplácí předem daný úrok. | Při růstu tržních sazeb může jeho tržní cena klesnout. |
            | **Dluhopis s pohyblivým kupónem** | Úrok se mění podle referenční sazby. | Výnos není dopředu úplně jistý. |
            | **Bezkuponový dluhopis** | Neplatí průběžný úrok; prodává se levněji a při splatnosti vyplatí jmenovitou hodnotu. | Investor čeká na výnos až do konce. |
            | **Konvertibilní dluhopis** | Lze ho za určitých podmínek vyměnit za akcie. | Kombinuje riziko dluhu a akcií. |
            | **Podřízený dluhopis** | Při problémech emitenta se splácí až po jiných věřitelích. | Vyšší riziko, často vyšší výnos. |
            """)
            st.warning("⚠️ **Pozor:** Dluhopis není automaticky bezpečný. Státní dluhopis stabilní země má jiné riziko než firemní dluhopis neznámé společnosti slibující vysoký úrok. Vysoký úrok často znamená vyšší riziko.")

            st.markdown("### 3.4.9 Co je napsáno na dluhopisu")
            st.write("**U dluhopisu nebo v jeho emisních podmínkách bývá uvedeno:**")
            st.markdown("""
            * název emitenta,
            * celkový objem emise,
            * jmenovitá hodnota jednoho dluhopisu,
            * měna,
            * datum vydání,
            * datum splatnosti,
            * výše kupónu nebo způsob výpočtu úroku,
            * termíny výplaty úroku,
            * způsob splacení,
            * zajištění, pokud existuje,
            * pořadí uspokojení věřitelů,
            * rizikové faktory,
            * ISIN,
            * informace, zda je dluhopis obchodovaný na trhu.
            """)
            st.write("**Proč číst emisní podmínky**")
            st.write("Reklama může ukazovat hlavně úrok, například „8 % ročně“. Emisní podmínky ale říkají, kdo si půjčuje, na co peníze použije, kdy má splácet, zda je dluhopis zajištěný a co se stane při problémech.")

            st.markdown("### 3.4.10 Jak se dluhopisy kupují")
            st.write("**Fyzická osoba nepodnikatel může dluhopisy koupit:**")
            st.markdown("""
            * přes banku,
            * přes obchodníka s cennými papíry,
            * přes brokera,
            * přímo v některých emisích,
            * nepřímo přes dluhopisový fond nebo ETF.
            """)
            st.write("**Podnikatel nebo firma může dluhopisy:**")
            st.markdown("""
            * koupit jako uložení volných peněz,
            * použít k řízení likvidity,
            * držet jako konzervativnější část portfolia,
            * vydat vlastní dluhopisy jako zdroj financování.
            """)
            st.write("Velké firmy a instituce obchodují dluhopisy často ve velkých objemech přes banky, dealingová oddělení, investiční banky a specializované trhy. Sledují úrokové sazby, rating, splatnost, likviditu, měnu, účetnictví a riziko protistrany.")

        # 3.4.11 až 3.4.14
        with st.container(border=True):
            st.markdown("### 3.4.11 Podílové listy: podíl na majetku fondu")
            st.write("Podílový list vyjadřuje podíl investora na majetku podílového fondu. Investor tedy nekupuje přímo jednu konkrétní akcii nebo jeden dluhopis, ale kupuje podíl ve fondu, který drží celé portfolio.")
            st.write("Fond shromažďuje peníze mnoha investorů a investuje je podle předem popsané strategie. Může investovat do akcií, dluhopisů, nástrojů peněžního trhu, nemovitostí nebo kombinace aktiv.")
            st.info("🧺 **Podílový fond jednoduše:** Místo jedné položky kupuješ košík. V košíku mohou být desítky, stovky nebo tisíce investic podle strategie fondu.")

            st.markdown("### 3.4.12 Druhy podílových fondů a podílových listů")
            st.write("Podílové fondy se liší podle toho, do čeho investují a jak fungují.")
            st.markdown("""
            | Druh fondu | Do čeho investuje | Typické riziko |
            | :--- | :--- | :--- |
            | **Fond peněžního trhu** | Krátkodobé a relativně konzervativní nástroje. | Nižší riziko, nižší očekávaný výnos. |
            | **Dluhopisový fond** | Dluhopisy států, firem nebo bank. | Úrokové a úvěrové riziko. |
            | **Akciový fond** | Akcie firem. | Vyšší kolísání hodnoty. |
            | **Smíšený fond** | Kombinace akcií, dluhopisů a dalších aktiv. | Riziko podle poměru jednotlivých složek. |
            | **Nemovitostní fond** | Nemovitosti nebo firmy spojené s nemovitostmi. | Riziko trhu nemovitostí a nižší likvidita. |
            | **Indexový fond** | Sleduje vybraný index. | Kopíruje vývoj trhu, který sleduje. |
            | **ETF** | Fond obchodovaný na burze, často sleduje index. | Tržní riziko, měnové riziko, poplatky. |
            """)
            st.write("**Podílové listy mohou mít různé třídy:**")
            st.markdown("""
            * **akumulační třída** — výnosy se nevyplácejí, ale zůstávají ve fondu,
            * **distribuční třída** — výnosy se vyplácejí investorům,
            * **měnově zajištěná třída** — snaží se omezit dopad změny kurzu,
            * **měnově nezajištěná třída** — investor nese i měnové riziko.
            """)

            st.markdown("### 3.4.13 Co je uvedeno u podílového listu nebo fondu")
            st.write("**Investor by měl sledovat:**")
            st.markdown("""
            * název fondu,
            * správce fondu,
            * depozitáře,
            * investiční strategii,
            * rizikovou kategorii,
            * měnu fondu,
            * vstupní, výstupní a průběžné poplatky,
            * historický vývoj hodnoty,
            * složení portfolia,
            * pravidla pro nákup a odkup,
            * dokument s klíčovými informacemi,
            * zda fond výnosy vyplácí, nebo reinvestuje.
            """)
            st.info("🔍 **Otázka před nákupem fondu:** Vím, do čeho fond investuje, kolik stojí na poplatcích, jak moc může kolísat a za jak dlouho se dostanu zpět k penězům?")

            st.markdown("### 3.4.14 Jak se podílové listy kupují")
            st.write("**Fyzická osoba nepodnikatel může koupit podílové listy:**")
            st.markdown("""
            * v bance,
            * u investiční společnosti,
            * přes finančního zprostředkovatele,
            * přes obchodníka s cennými papíry,
            * přes investiční platformu,
            * pravidelnou investicí menších částek.
            """)
            st.write("**Podnikatel nebo firma může fondy využít:**")
            st.markdown("""
            * pro zhodnocení dočasně volných peněz,
            * jako diverzifikovanou část finančních rezerv,
            * jako součást dlouhodobého finančního plánování,
            * přes firemní investiční účet,
            * s ohledem na účetnictví, daně, likviditu a investiční politiku firmy.
            """)
            st.write("U podílového fondu investor obvykle podílový list nakupuje od fondu a při prodeji ho fondu odprodává zpět. U ETF je to jiné: ETF se obchoduje na burze podobně jako akcie, takže ho investor kupuje a prodává přes brokera za tržní cenu.")

        # 3.4.15 až 3.4.17
        with st.container(border=True):
            st.markdown("### 3.4.15 Které cenné papíry se používají při obchodování firem")
            st.write("Firmy nepoužívají cenné papíry jen jako investici. V podnikové praxi mohou sloužit k financování, placení, zajištění i řízení rizik.")
            st.markdown("""
            | Cenný papír / nástroj | Jak ho firmy používají | Příklad |
            | :--- | :--- | :--- |
            | **Akcie** | Získání vlastního kapitálu, změna vlastnické struktury, vstup na burzu, akvizice. | Firma vydá nové akcie a získá peníze na expanzi. |
            | **Dluhopisy** | Získání cizího kapitálu bez klasického bankovního úvěru. | Firma vydá dluhopisy na financování nové technologie. |
            | **Směnka** | Písemný slib nebo příkaz zaplatit určitou částku v určité době. | Firma použije směnku při obchodním financování. |
            | **Šek** | Příkaz bance zaplatit určitou částku; v ČR dnes méně běžný. | Historicky používaný platební nástroj v obchodě. |
            | **Skladní list / náložný list** | Dokládá právo ke zboží nebo jeho přepravě. | V mezinárodním obchodě může dokument představovat nárok na zboží. |
            | **Podílové listy a fondy** | Uložení nebo diverzifikace volných prostředků. | Firma uloží část rezervy do konzervativního fondu podle své investiční politiky. |
            """)
            st.info("🏭 **Firemní pohled:** Domácnost řeší hlavně bezpečnost, výnos a dostupnost peněz. Firma navíc řeší cashflow, účetnictví, daně, kurzové riziko, vztahy s bankami, rating, pověst a odpovědnost vedení.")

            st.markdown("### 3.4.16 Jak obchodují velké firmy a instituce")
            st.write("Velké firmy, banky, pojišťovny, penzijní fondy a investiční fondy obchodují ve větších objemech než běžný investor. Proto řeší i věci, které student v běžné aplikaci nevidí:")
            st.markdown("""
            * likviditu trhu,
            * protistranu obchodu,
            * regulaci a interní pravidla,
            * účetní dopady,
            * daňové dopady,
            * měnové zajištění,
            * úrokové riziko,
            * reputační riziko,
            * schvalovací procesy uvnitř firmy.
            """)
            st.write("**Příklad rozdílu:**")
            st.markdown("""
            * Drobný investor koupí 2 akcie přes aplikaci.
            * Firma může nakupovat dluhopisy za miliony korun jako součást řízení likvidity.
            * Investiční fond může přesouvat peníze mezi stovkami titulů.
            * Korporace může vydat dluhopis, aby získala kapitál na výstavbu nové továrny.
            * Velká společnost může použít akcie při koupi jiné firmy.
            """)

            st.markdown("### 3.4.17 Kde může nakupovat fyzická osoba a kde podnikatel")
            st.markdown("""
            | Kdo nakupuje | Kde může nakupovat | Na co si dát pozor |
            | :--- | :--- | :--- |
            | **Fyzická osoba nepodnikatel** | Banka, broker, obchodník s cennými papíry, investiční platforma, investiční společnost. | Poplatky, riziko, regulace, měna, daně, investiční horizont, ochrana účtu. |
            | **OSVČ / podnikatel** | Podobně jako fyzická osoba, ale musí řešit, zda investuje soukromé, nebo podnikatelské peníze. | Oddělení osobních a podnikatelských financí, účetnictví, daně, likvidita pro podnikání. |
            | **Právnická osoba / firma** | Firemní investiční účet, banka, broker, treasury oddělení, investiční banka. | Schválení vedením, investiční politika, účetní zachycení, rizikové limity, cashflow. |
            | **Velká korporace** | Investiční banky, kapitálové trhy, burzy, neveřejné transakce, emise vlastních cenných papírů. | Dopad na cenu, regulace, rating, vztahy s investory, reputace, strategické cíle. |
            """)
            st.info("🧠 **Důležité rozlišení:** Když nakupuje fyzická osoba pro sebe, jde o osobní investiční rozhodnutí. Když nakupuje firma, jde o rozhodnutí v rámci podnikání, které může ovlivnit účetnictví, daně, likviditu a odpovědnost vedení.")

# =========================================================================
        # 3.4.18 Praktická aktivita
        # =========================================================================
        with st.container(border=True):
            st.markdown("### 3.4.18 Praktická aktivita: pitva cenného papíru")
            st.write("🔎 **Pitva cenného papíru: co přesně kupuji?**")
            st.write("Vyber si jeden příklad: akcii, dluhopis, podílový fond nebo ETF. Neřeš, jestli je „dobrý“, ale zjisti, co přesně představuje.")
            
            cp_vyber = st.selectbox(
                "Vyber si aktivum pro pitvu:", 
                ["...", "Akcie", "Dluhopis", "Podílový fond", "ETF"], 
                key="k3_pitva_aktivita"
            )
            
            st.write("**Zjisti a odpověz si na tyto otázky:**")
            st.markdown("""
            * Kdo je emitent nebo správce?
            * Je to podíl na firmě, půjčka, nebo podíl ve fondu?
            * Jaký výnos může přinášet?
            * Jaké jsou hlavní druhy rizika?
            * Je obchodovaný na burze, nebo se nakupuje přímo u fondu?
            * V jaké měně je vedený?
            * Jaké má poplatky?
            * Jak rychle ho lze prodat?
            * Je vhodný spíš pro krátký, nebo dlouhý horizont?
            * Co by se muselo stát, aby investor prodělal?
            """)

            # Jakmile student vybere aktivum, otevře se mu prostor pro vypracování
            if cp_vyber != "...":
                st.markdown(f"📄 **Tvůj výstup pro cenný papír: {cp_vyber}**")
                
                # Skutečné interaktivní pole pro vypracování úkolu
                student_odpoved = st.text_area(
                    "Vytvoř jednu stránku „rodný list cenného papíru“ se všemi těmito zjištěnými informacemi:", 
                    height=250, 
                    key="k3_pitva_odpoved"
                )
                
                if st.button("Uložit / Odevzdat rodný list", key="k3_pitva_btn"):
                    if student_odpoved.strip() == "":
                        st.error("Musíš nejdřív něco napsat, než úkol odevzdáš!")
                    else:
                        st.success(f"✅ Výborně! Tvůj rodný list pro **{cp_vyber}** byl úspěšně uložen.")
                
                # Zlepšovák: Skrytá ukázka, kterou si student může rozbalit po vypracování
                with st.expander("💡 Nevíš si rady? Zobrazit vzorový rodný list pro kontrolu"):
                    if cp_vyber == "Akcie":
                        st.info("**Ukázka - Akcie ČEZ, a.s.**\n* **Emitent:** ČEZ, a.s.\n* **Podstata:** Podíl na firmě.\n* **Výnos:** Dividenda a růst ceny akcie.\n* **Rizika:** Tržní a specifická (změna zákonů, cena elektřiny).\n* **Kde se obchoduje:** Burza cenných papírů Praha.\n* **Měna:** CZK.\n* **Poplatky:** Poplatek brokerovi za provedení transakce.\n* **Likvidita:** Velmi rychlá (na burze prodáš okamžitě).\n* **Horizont:** Dlouhý (ideálně 5+ let).\n* **Jak prodělám:** Klesne tržní cena akcie a firma přestane vyplácet dividendy.")
                    elif cp_vyber == "Dluhopis":
                        st.info("**Ukázka - Státní dluhopis ČR**\n* **Emitent:** Ministerstvo financí ČR.\n* **Podstata:** Půjčka státu (jsi věřitel).\n* **Výnos:** Předem daný roční úrok (kupón).\n* **Rizika:** Inflační riziko.\n* **Kde se obchoduje:** Přes banky nebo na sekundárním trhu.\n* **Měna:** CZK.\n* **Poplatky:** Žádné nebo minimální.\n* **Likvidita:** Střední (lze vybrat v určitých termínech).\n* **Horizont:** Střední (např. 3-6 let).\n* **Jak prodělám:** Inflace znehodnotí peníze rychleji, než ti vydělá úrok.")
                    elif cp_vyber == "Podílový fond":
                        st.info("**Ukázka - Akciový podílový fond v bance**\n* **Správce:** Investiční společnost tvé banky.\n* **Podstata:** Podíl ve fondu.\n* **Výnos:** Podle zhodnocení košíku držených akcií.\n* **Rizika:** Tržní riziko (pokles trhů).\n* **Kde se obchoduje:** Přímo u tvé banky/fondu.\n* **Měna:** CZK.\n* **Poplatky:** Vstupní poplatek (cca 2-3 %) + průběžný (cca 1,5 % ročně).\n* **Likvidita:** Dobrá (peníze dorazí za pár dní).\n* **Horizont:** Dlouhý.\n* **Jak prodělám:** Trh se propadne v krizi a ty ze strachu vše odprodáš ve ztrátě dřív, než se trh srovná.")
                    elif cp_vyber == "ETF":
                        st.info("**Ukázka - Globální ETF (S&P 500)**\n* **Správce:** Vanguard / iShares (BlackRock).\n* **Podstata:** Podíl ve fondu (indexu největších firem).\n* **Výnos:** Růst hodnoty amerického trhu a dividendy.\n* **Rizika:** Tržní a měnové.\n* **Kde se obchoduje:** Přímo na mezinárodní burze.\n* **Měna:** USD nebo EUR.\n* **Poplatky:** Velmi nízké správcovské (cca 0,07 % ročně) + poplatek brokerovi.\n* **Likvidita:** Velmi rychlá (okamžitě přes aplikaci).\n* **Horizont:** Velmi dlouhý (10+ let).\n* **Jak prodělám:** Trh se propadne v krizi a ty ze strachu vše odprodáš ve ztrátě dřív, než se trh srovná.")
        # =========================================================================
        # 3.4.19 Srovnání základních produktů
        # =========================================================================
        with st.container(border=True):
            st.markdown("### 3.4.19 Srovnání základních produktů")
            st.markdown("""
            | Produkt | Co kupuji | Možný výnos | Hlavní riziko | Pro koho se může hodit |
            | :--- | :--- | :--- | :--- | :--- |
            | **Spořicí účet** | Vklad u banky. | Úrok. | Inflace může být vyšší než úrok. | Rezerva a krátkodobé cíle. |
            | **Termínovaný vklad** | Vklad na určitou dobu. | Úrok. | Nižší dostupnost peněz. | Peníze, které chvíli nepotřebuji. |
            | **Dluhopis** | Půjčku emitentovi. | Úrok nebo rozdíl ceny. | Emitent nemusí splatit. | Investor, který rozumí emitentovi a riziku. |
            | **Akcie** | Podíl na firmě. | Růst ceny, dividenda. | Pokles ceny firmy nebo trhu. | Dlouhodobý investor. |
            | **Fond / ETF** | Podíl v portfoliu více aktiv. | Podle vývoje aktiv. | Tržní pokles, poplatky. | Začátečník i dlouhodobý investor. |
            | **Kryptoměna** | Digitální aktivum v síti. | Růst ceny, případně jiné výnosy podle služby. | Vysoká volatilita, ztráta přístupu, podvod, regulace. | Pouze pro člověka, který chápe technologii a unese ztrátu. |
            """)
# =========================================================================
    # 3.5 ANALÝZA DAT: INVESTIČNÍ LABORATOŘ
    # =========================================================================
    elif "3.5 Analýza dat" in selected_section_2:
        st.markdown("<div class='sub-section-header'>3. FINANČNÍ TRH A ANALÝZA RIZIK</div><h2>3.5 Analýza dat: investiční laboratoř</h2>", unsafe_allow_html=True)
        
        st.write("Investiční rozhodování nemá stát na větě „kamarád říkal“ nebo „viděl/a jsem video na TikToku“. Důležitá je práce s daty, ale i schopnost chápat jejich limity.")
        
        st.write("**Studenti by měli umět sledovat:**")
        st.markdown("""
        * dlouhodobý vývoj ceny,
        * největší propady,
        * délku zotavení po propadu,
        * rozdíl mezi nominálním a reálným výnosem,
        * vliv inflace,
        * poplatky,
        * riziko krátkého časového horizontu.
        """)

        # 🔬 Analytická laboratoř
        with st.container(border=True):
            st.markdown("### 🔬 Analytická laboratoř")
            st.write("Vyber jedno aktivum nebo index — například akciový index, státní dluhopisový fond, zlato nebo kryptoměnu. Najdi si (např. na Google Finance) graf jeho vývoje za delší období. Označ si největší propad, období růstu a období stagnace.")
            
            lab_vyber = st.selectbox(
                "Otestuj svou psychologii. Vyber si aktivum:", 
                ["...", "Akciový index (např. S&P 500)", "Státní dluhopisový fond", "Zlato", "Kryptoměna (např. Bitcoin)"], 
                key="k3_lab_vyber"
            )
            
            if lab_vyber != "...":
                st.info(f"📊 **Představ si, že se graf pro {lab_vyber} propadne o 30 % až 50 % své hodnoty.**")
                st.write("**Otázka k zamyšlení:** Vydržel/a bych psychicky držet tuto investici i v době takového propadu?")
                
                odpoved_lab = st.radio(
                    "Vyber upřímnou odpověď:", 
                    ["Vyber...", "Ano, nepanikařil/a bych a čekal/a na zotavení", "Asi ne, raději bych to se ztrátou prodal/a", "Zatím nevím"], 
                    key="k3_lab_radio"
                )
                
                if odpoved_lab == "Ano, nepanikařil/a bych a čekal/a na zotavení":
                    st.success("Skvělý přístup! Ale pamatuj, že na papíře to bolí mnohem méně, než když vidíš mizet své skutečné peníze.")
                elif odpoved_lab == "Asi ne, raději bych to se ztrátou prodal/a":
                    st.warning("To je naprosto upřímné a racionální. Právě proto je důležité znát svou toleranci k riziku a nedávat všechny úspory do příliš kolísavých aktiv.")
                elif odpoved_lab == "Zatím nevím":
                    st.write("Nevadí. Zkušenost se buduje postupně, ideálně s malými částkami.")

        # 🚀 Simulátor (PROPOJENÍ NA NOVOU STRÁNKU)
        with st.container(border=True):
            st.markdown("### 🚀 SPUSTIT ŠKOLNÍ INVESTIČNÍ SIMULÁTOR")
            st.markdown("#### Otevřít simulátor akcií a bitcoinu")
            st.write("Interaktivní aktivita: Vyzkoušej si modelové investování nanečisto — bez skutečných peněz a bez rizika. Sleduj, jak se může měnit hodnota akcií a bitcoinu v čase.")
            
            st.write("") # drobná mezera pro hezčí vzhled
            
            # TADY JE TEN ODKAZ NA NOVÝ SOUBOR:
            st.page_link("pages/Školní_investiční_simulátor.py", label="🚀 PŘEJÍT DO SIMULÁTORU", use_container_width=True)
            
            st.write("")
            st.caption("Důležité: Simulátor je pouze vzdělávací pomůcka. Nejde o investiční doporučení.")

        # 3.5.1
        with st.container(border=True):
            st.markdown("### 3.5.1 Historický výnos není slib")
            st.write("Historická data jsou užitečná, ale nejsou zárukou budoucnosti. Pokud nějaké aktivum v minulosti rostlo, neznamená to, že poroste dál. Trh se mění, firmy krachují, technologie zastarávají, regulace se mění a nálada investorů může být extrémně proměnlivá.")
            
            st.warning("⚠️ **Varování před grafem:** Graf začínající ve vhodně vybraném roce může vypadat skvěle. Jiný začátek může ukázat dlouhé období ztráty. Proto je nutné ptát se: Kdo graf vybral? Proč právě toto období? Co v grafu není vidět?")
# =========================================================================
    # 3.6 KRYPTOMĚNY: TECHNOLOGIE, PENÍZE, SPEKULACE I RIZIKO
    # =========================================================================
    if "3.6 Kryptoměny" in selected_section_2:  # Uprav název proměnné podle tvého selectboxu
        st.markdown("<div class='sub-section-header'>6. KRYPTOMĚNY A NOVÉ FINANČNÍ TECHNOLOGIE</div>", unsafe_allow_html=True)
        
        st.markdown("## 3.6 Kryptoměny: technologie, peníze, spekulace i riziko")
        st.write(
            "Kryptoměny jsou pro současnou generaci atraktivní, protože spojují technologie, internetovou kulturu, "
            "možnost rychlého zisku, nedůvěru k institucím a příběh „nového finančního systému“. "
            "Právě proto je potřeba je vysvětlit srozumitelně — bez strašení, ale také bez reklamního nadšení."
        )

        st.markdown("""
        <div class="box-blue">
            <b>🪙 Kryptoměna jednoduše:</b> Kryptoměna je digitální aktivum, které existuje v počítačové síti.
            Záznamy o vlastnictví a převodech nejsou vedeny jednou běžnou bankou, ale pomocí technologie, která umožňuje sdílenou evidenci transakcí.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="box-red">
            <b>🚫 Důležité:</b> Tato kapitola není investiční doporučení. Cílem není přesvědčit tě, abys kryptoměny kupoval/a nebo odmítal/a.
            Cílem je rozumět principu, rizikům, reklamním trikům a rozdílu mezi technologií a spekulací.
        </div>
        """, unsafe_allow_html=True)

        # --- 3.6.1 ---
        st.markdown("### 3.6.1 Proč kryptoměny vznikly")
        st.write(
            "Kryptoměny vznikly jako reakce na otázku: *Lze vytvořit digitální peníze, které nepůjde jednoduše kopírovat a které nebudou závislé na jedné centrální autoritě?*"
        )
        st.write("U běžných digitálních peněz se problém řeší přes banku. Banka vede účetní záznam a hlídá, aby člověk neutratil stejné peníze dvakrát.")
        st.write("U kryptoměn se tento problém řeší jinak:")

        st.markdown("""
        * **Sdílená databáze:** Transakce se zapisují do sdílené databáze.
        * **Síťová validace:** Síť účastníků ověřuje, co je platné.
        * **Protokol:** Pravidla jsou pevně dány protokolem.
        * **Kryptografie:** Vlastnictví se prokazuje kryptografickými klíči.
        """)

        st.markdown("**Problém dvojí útraty**")
        st.write(
            "Když pošleš kamarádovi fotku, můžeš si ji stále nechat. Digitální soubor lze kopírovat. U peněz by to byl problém: "
            "kdyby šlo stejnou digitální stokorunu poslat dvěma lidem, peníze by ztratily smysl. Kryptoměnové sítě se snaží řešit právě to, "
            "aby šlo ověřit, kdo co vlastní a zda už danou hodnotu neutratil."
        )

        # --- 3.6.2 ---
        st.markdown("### 3.6.2 Blockchain: účetní kniha, kterou sdílí síť")
        st.write(
            "Blockchain si můžeš představit jako řetěz bloků záznamů. Do bloků se zapisují transakce. Jakmile je blok potvrzen a navázán na předchozí bloky, "
            "je velmi obtížné ho zpětně změnit bez toho, aby si toho síť všimla."
        )
        st.write("Blockchain není kouzlo. Je to kombinace:")

        st.markdown("""
        * Databáze
        * Kryptografie
        * Pravidel sítě
        * Motivace účastníků
        * Mechanismu ověřování transakcí
        """)

        st.markdown("""
        <div class="box-yellow">
            <b>📒 Přirovnání:</b> Představ si třídní účetní knihu, kterou nemá jen jeden pokladník, ale kopii má mnoho lidí.
            Když někdo zapíše novou platbu, ostatní kontrolují, zda zápis dává smysl. Pokud by jeden člověk chtěl zápis podvést, ostatní kopie ho mohou odhalit.
        </div>
        """, unsafe_allow_html=True)

        # --- 3.6.3 ---
        st.markdown("### 3.6.3 Peněženka, adresa, veřejný a soukromý klíč")
        st.write("Kryptoměny nejsou uložené „v peněžence“ stejným způsobem, jako máš mince v kapse. Peněženka spíš spravuje klíče, které umožňují s kryptoměnou nakládat.")

        st.markdown("""
        | Pojem | Co znamená | Přirovnání |
        | :--- | :--- | :--- |
        | **Veřejná adresa** | Adresa, na kterou lze poslat kryptoměnu. | Číslo účtu. |
        | **Soukromý klíč** | Tajný údaj, kterým se prokazuje právo s kryptoměnou nakládat. | Kombinace podpisového práva a trezoru. |
        | **Seed phrase** | Sada slov, ze které lze obnovit přístup k peněžence. | Hlavní klíč ke všemu. |
        | **Burza** | Služba, kde lze kryptoměny nakupovat, prodávat nebo držet. | Směnárna a investiční platforma. |
        | **Transakční poplatek** | Poplatek za zpracování transakce v síti. | Poplatek za převod, ale proměnlivý podle sítě. |
        """)

        st.markdown("""
        <div class="box-red">
            <b>🔐 Nejdůležitější bezpečnostní pravidlo:</b> Kdo zná tvůj soukromý klíč nebo seed phrase, může získat přístup ke kryptoměnám.
            Banka ti ztracený soukromý klíč neobnoví jako heslo do internetového bankovnictví.
        </div>
        """, unsafe_allow_html=True)

        # --- 3.6.4 ---
        st.markdown("### 3.6.4 Bitcoin, Ethereum, stablecoiny a tokeny")
        st.write("Kryptoměny nejsou všechny stejné.")

        st.markdown("""
        | Typ | Co je hlavní myšlenka | Riziko |
        | :--- | :--- | :--- |
        | **Bitcoin** | První a nejznámější kryptoměna, často chápaná jako digitální vzácné aktivum. | Vysoká volatilita, technologická a regulační rizika. |
        | **Ethereum** | Síť umožňující chytré kontrakty a decentralizované aplikace. | Technologická složitost, chyby v aplikacích, kolísání ceny. |
        | **Stablecoiny** | Tokeny, které se snaží držet hodnotu vůči měně, například dolaru. | Riziko rezerv, emitenta, regulace a ztráty navázání na měnu. |
        | **Meme coiny** | Tokeny postavené často na internetové komunitě, humoru a virálním trendu. | Extrémní spekulace, manipulace, prudké pády. |
        | **Utility tokeny** | Tokeny slibující využití v určité službě nebo ekosystému. | Projekt nemusí uspět, token nemusí mít reálnou hodnotu. |
        """)

        # --- 3.6.5 ---
        st.markdown("### 3.6.5 Těžba, validace a spotřeba energie")
        st.write("Některé kryptoměny používají systém **Proof of Work**. Ten vyžaduje výpočetní výkon a spotřebu energie. Nejznámějším příkladem je Bitcoin.")
        st.write("Jiné sítě používají **Proof of Stake**, kde se transakce ověřují jiným způsobem — účastníci uzamykají určité množství tokenů jako ekonomickou záruku.")

        st.markdown("""
        | Mechanismus | Princip | Diskutované téma |
        | :--- | :--- | :--- |
        | **Proof of Work** | Ověřování pomocí výpočetní práce. | Energetická náročnost, bezpečnost sítě. |
        | **Proof of Stake** | Ověřování pomocí uzamčeného podílu v síti. | Koncentrace bohatství, pravidla validátorů. |
        """)

        # --- 3.6.6 ---
        st.markdown("### 3.6.6 Chytré kontrakty, DeFi a NFT")
        st.write("**Chytrý kontrakt** je program běžící na blockchainu, který může automaticky provádět určité kroky podle pravidel. Neznamená to, že je právně „chytrý“ nebo bezpečný. Znamená to, že jde o kód.")
        st.write("**DeFi** znamená decentralizované finance. Jde o služby, které se snaží napodobit finanční produkty — půjčování, směnu, úročení — bez klasické banky.")
        st.write("**NFT** je unikátní token, který může odkazovat na digitální objekt, členství, herní předmět nebo jiný záznam.")

        st.markdown("""
        <div class="box-purple">
            <b>⚠️ Pozor na slovo „decentralizované“:</b> To, že služba používá blockchain, neznamená, že je bezpečná, férová nebo bez prostředníků.
            Rizikem může být chyba v kódu, podvodný tým, manipulace trhu, falešná likvidita nebo nejasná odpovědnost.
        </div>
        """, unsafe_allow_html=True)

        # --- 3.6.7 ---
        st.markdown("### 3.6.7 Proč cena kryptoměn tolik kolísá")
        st.write("Cena je silně závislá na nabídce, poptávce, očekávání, náladě trhu, regulaci, mediálních trendech a chování velkých držitelů.")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Cena může růst kvůli:**")
            st.markdown("""
            * Zájmu investorů a FOMO
            * Mediální pozornosti
            * Omezené nabídce
            * Vstupu institucí
            """)
        with col2:
            st.markdown("**Cena může klesat kvůli:**")
            st.markdown("""
            * Panice na trhu a výprodejům
            * Hackerskému útoku nebo pádu burzy
            * Tvrdé regulaci
            * Nesplnění slibů projektu
            """)

        st.markdown("""
        <div class="box-blue">
            <b>🎢 Volatilita lidsky:</b> Pokud aktivum může za měsíc vyrůst o desítky procent, může také o desítky procent spadnout.
            Vysoký pohyb nahoru a dolů není chyba systému — u kryptoměn je to běžná vlastnost trhu.
        </div>
        """, unsafe_allow_html=True)

        # --- 3.6.8 ---
        st.markdown("### 3.6.8 Největší rizika kryptoměn")

        st.markdown("""
        | Riziko | Jak se projevuje | Jak se bránit |
        | :--- | :--- | :--- |
        | **Volatilita** | Cena prudce kolísá. | Neinvestovat peníze potřebné na běžný život nebo rezervu. |
        | **Ztráta přístupu** | Ztráta seed phrase nebo klíče. | Bezpečně zálohovat, nikdy nesdílet klíče. |
        | **Podvod** | Falešná investice, falešná burza. | Ověřovat zdroje, nedůvěřovat garantovaným výnosům. |
        | **Hack burzy / aplikace** | Služba přijde o prostředky klientů. | Rozumět rozdílu mezi vlastní peněženkou a burzou. |
        | **Regulace** | Změna pravidel omezí obchodování. | Sledovat právní prostředí, nesázet na jeden scénář. |
        | **Manipulace trhu** | Velcí hráči ovlivňují cenu. | Nenakupovat podle virálních příspěvků. |
        | **Technická nevratnost** | Chybně odeslaná platba nejde vrátit. | Kontrolovat adresy, posílat testovací malé částky. |
        """)

        # --- 3.6.9 ---
        st.markdown("### 3.6.9 Krypto podvody a varovné signály")
        st.write("Kryptoměny jsou oblíbeným prostředím pro podvody, protože kombinují technologickou složitost s touhou po rychlém zisku.")

        st.markdown("**🚩 Varovné signály:**")
        st.markdown("""
        * „Garantovaný výnos“ nebo tvrzení „bez rizika“
        * Tlak na rychlé rozhodnutí
        * Influencer ukazující luxusní život s příslibem jednoduchého návodu
        * Není jasné, odkud se bere výnos (lidé vydělávají náborem dalších)
        * Někdo vyžaduje seed phrase nebo přístupové údaje
        """)

        st.markdown("""
        <div class="box-red">
            <b>🚨 Zlaté pravidlo:</b> Pokud nerozumíš tomu, odkud se bere výnos, pravděpodobně nejsi investor — jsi zdroj peněz pro někoho jiného.
        </div>
        """, unsafe_allow_html=True)

        # --- 3.6.10 ---
        st.markdown("### 3.6.10 Kryptoměny vs. běžné peníze")

        st.markdown("""
        | Otázka | Běžné peníze na účtu | Kryptoměny |
        | :--- | :--- | :--- |
        | **Kdo vede záznam?** | Banka a platební systém. | Síť podle pravidel protokolu. |
        | **Kdo ručí za systém?** | Stát, regulace, banky, dohled. | Kód, síť, komunita, ekonomická motivace. |
        | **Je hodnota stabilní?** | Řeší se hlavně inflace. | Cena většiny kryptoměn silně kolísá. |
        | **Lze transakci reklamovat?** | Existují reklamační postupy. | Transakce bývají nevratné. |
        | **Kdo obnoví přístup?** | Banka může pomoci s heslem. | Ztracený klíč znamená trvalou ztrátu. |
        | **Je to vhodné na rezervu?** | Vhodné pro rezervu. | Nevhodné pro nouzovou rezervu. |
        """)

        # --- 3.6.11 ---
        st.markdown("### 3.6.11 Kryptoměny a daně")
        st.markdown("""
        <div class="box-gray">
            <b>📄 Praktická poznámka:</b> „Mám to v aplikaci“ neznamená, že to není skutečná finanční operace.
            Pokud člověk kryptoměnu prodá se ziskem nebo ji použije k platbě, vzniká povinnost řešit zdanění.
            U kryptoměn je důležité vést si přehled nákupů, prodejů, směn a poplatků.
        </div>
        """, unsafe_allow_html=True)

        # --- 3.6.12 ---
        st.markdown("### 3.6.12 Jak o kryptoměnách přemýšlet odpovědně")
        st.write("Před nákupem kryptoměny si polož tyto otázky:")

        st.markdown("""
        1. Rozumím tomu, co kupuji a vím, proč by cena měla růst?
        2. Unesu ztrátu celé částky a neinvestuji peníze z rezervy?
        3. Nekupuji jen kvůli influencerovi, kamarádovi nebo FOMO?
        4. Vím, kde a jak aktivum bezpečně držím?
        5. Mám plán, nebo jen emoci?
        """)

        st.markdown("""
        <div class="box-green">
            <b>🧠 Rozumný závěr:</b> Blockchain může být zajímavá technologie a inovace. 
            Žádná technologie ale neruší základní pravidla finanční gramotnosti: rozumět riziku, nevěřit garantovaným výnosům,
            chránit přístupové údaje a neinvestovat peníze, které si nemůžeš dovolit ztratit.
        </div>
        """, unsafe_allow_html=True)

# --- ÚKOL (INTERAKTIVNÍ) ---
        st.markdown("### 🧪 Krypto detektiv: ověř projekt dřív, než mu uvěříš")
        st.write("Vyber libovolný kryptoměnový projekt nebo token. **Nehodnoť, zda ho koupit, ale zda mu rozumíš.**")
        
        st.markdown("""
        **Co máš zjistit:**
        * Jaký problém údajně řeší a kdo za ním stojí?
        * Odkud se má brát hodnota a neslibuje někdo garantovaný výnos?
        * Je projekt spíš technologie, komunita, nebo meme?
        """)

        st.markdown("---")
        st.markdown("**🎯 Tvůj závěr a hodnocení rizika:**")
        
        # Interaktivní prvky Streamlitu
        semafor = st.selectbox(
            "Zvol úroveň rizika (Semafor):",
            [
                "Vyber hodnocení...", 
                "🟢 Zelená (Nízké riziko, srozumitelný projekt)", 
                "🟠 Oranžová (Střední riziko, nejasnosti nebo velká spekulace)", 
                "🔴 Červená (Vysoké riziko, varovné signály, možný podvod)"
            ]
        )
        
        zduvodneni = st.text_area(
            "Napiš max. 3 věty zdůvodnění, proč jsi zvolil/a tuto barvu:", 
            height=100,
            placeholder="Tento projekt mi přijde rizikový, protože..."
        )
        
        if st.button("Uložit hodnocení", type="primary"):
            if semafor == "Vyber hodnocení..." or not zduvodneni.strip():
                st.warning("⚠️ Prosím, vyber barvu na semaforu a napiš své zdůvodnění.")
            else:
                st.success(f"✅ Skvělá práce, detektive! Hodnocení **{semafor.split(' ')[0]}** bylo zaznamenáno.")
                st.info(f"**Tvé zdůvodnění:** {zduvodneni}")

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
    # 3.7 OCHRANA SPOTŘEBITELE A INVESTIČNÍ REKLAMA
    # =========================================================================
    if "3.7 Ochrana spotřebitele" in selected_section_2:  # Uprav název podle položky v selectboxu
        st.markdown("<div class='sub-section-header'>7. OCHRANA SPOTŘEBITELE A REKLAMA</div>", unsafe_allow_html=True)
        
        st.markdown("## 3.7 Ochrana spotřebitele a investiční reklama")
        st.write(
            "Finanční produkty se často prodávají jazykem emocí. Reklama může zdůraznit svobodu, "
            "rychlý zisk, strach z inflace, strach z promarněné šance nebo společenský status."
        )

        st.markdown("**Typické věty, u kterých je potřeba zpozornět:**")
        st.markdown("""
        * „Začni vydělávat pasivně hned.“
        * „Tuhle příležitost nesmíš propásnout.“
        * „Garantovaný výnos.“
        * „Vydělávají na tom všichni.“
        * „Stačí kopírovat moje obchody.“
        * „Banky nechtějí, abys to věděl/a.“
        """)

        st.markdown("""
        <div class="box-blue">
            <b>🛡️ Ochrana spotřebitele začíná otázkou:</b> Kdo mi to nabízí, jak na tom vydělává, jaké riziko mi neříká a proč mám rozhodnout právě teď?
        </div>
        """, unsafe_allow_html=True)
        # =========================================================================
    # 3.8 INTERAKTIVNÍ AKTIVITY K FINANČNÍMU TRHU
    # =========================================================================
    if "3.8 Interaktivní aktivity" in selected_section_2:  # Uprav název podle položky v selectboxu
        st.markdown("<div class='sub-section-header'>8. INTERAKTIVNÍ AKTIVITY K FINANČNÍMU TRHU</div>", unsafe_allow_html=True)
        st.markdown("## 3.8 Interaktivní aktivity k finančnímu trhu")
        
        # --- AKTIVITA 1: TŘÍDĚNÍ ---
        st.markdown("### 🧩 Aktivita 1: Třídění finančních nástrojů")
        st.write("Rozděl následující položky do správných kategorií podle míry rizika a účelu. Přemýšlej, než vybereš!")
        
        kategorie = ["Vyber...", "Spoření", "Investování", "Spekulace", "Hazard / Extrémní riziko"]
        
        # Formulář pro třídění
        with st.form("trideni_form"):
            col1, col2 = st.columns(2)
            with col1:
                q1 = st.selectbox("Spořicí účet", kategorie)
                q2 = st.selectbox("Státní dluhopis", kategorie)
                q3 = st.selectbox("Akcie jedné firmy (stock picking)", kategorie)
                q4 = st.selectbox("ETF na široký index", kategorie)
                q5 = st.selectbox("Podílový fond", kategorie)
            with col2:
                q6 = st.selectbox("Termínovaný vklad", kategorie)
                q7 = st.selectbox("Nákup meme coinu podle TikToku", kategorie)
                q8 = st.selectbox("Sázení na sport / ruleta", kategorie)
                q9 = st.selectbox("Kryptoměna držená bez pochopení rizika", kategorie)
                q10 = st.selectbox("Pravidelná investice do diverzifikovaného fondu", kategorie)
                
            submitted_trideni = st.form_submit_button("Vyhodnotit moje odpovědi", type="primary")
            
        if submitted_trideni:
            if "Vyber..." in [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]:
                st.warning("⚠️ Nezapomeň zařadit všechny položky!")
            else:
                st.success("✅ Odesláno k zamyšlení! Zde je expertní pohled na to, kam položky typicky patří:")
                with st.expander("Zobrazit správné řešení a bonusové detaily (rozbalit)"):
                    st.markdown("""
                    * **Spoření (nízké riziko, vysoká likvidita, nízký výnos):** Spořicí účet, Termínovaný vklad.
                    * **Investování (střední riziko, dlouhý horizont, reálný výnos):** ETF na široký index, Podílový fond, Pravidelná investice do diverzifikovaného fondu, Státní dluhopis.
                    * **Spekulace (vyšší riziko, sázka na konkrétní vývoj):** Akcie jedné firmy (stock picking).
                    * **Hazard / Extrémní riziko (vysoká šance na ztrátu všeho):** Nákup meme coinu podle TikToku, Sázení, Kryptoměna držená bez pochopení rizika.
                    """)
        
        st.divider()
# --- AKTIVITA 2: INVESTIČNÍ POČASÍ (VYLEPŠENÁ VERZE) ---
        st.markdown("### 📉 Aktivita 2: Investiční počasí")
        st.write("Jak reagují lidé na výkyvy trhu? Vyber situaci a zkus správně přiřadit, jak se zachová **Impulzivní začátečník** a jak **Informovaný investor**.")

        scenare = {
            "Vyber situaci...": None,
            "Trh raketově roste a všichni mluví o rychlém zisku": {
                "reakce_A": "Okamžitě nakupuje za jakoukoliv cenu, protože má strach, že mu ujede vlak (FOMO).",
                "reakce_B": "Zůstává v klidu, drží se svého dlouhodobého plánu a nepanikaří, i když ostatní 'rychle bohatnou'.",
                "zacatecnik": "A",
                "vysvetleni": "Když trh strmě roste, začátečníci často naskakují na vrcholu bubliny, protože vnímají jen nadšení zisků. Investor ví, že stromy nerostou do nebe."
            },
            "Trh nečekaně spadl o 30 %": {
                "reakce_A": "Ví, že propady jsou normální. Ujistí se, že firmy/aktiva neztratily svou skutečnou hodnotu, a případně využije 'slevu' k dalším nákupům.",
                "reakce_B": "Vyděsí se, že přijde o všechno, prodá v panice se ztrátou a z trhu definitivně uteče.",
                "zacatecnik": "B",
                "vysvetleni": "Nejhorší investiční chybou je nakupovat draze (v euforii) a prodávat levně (v panice). Investor využívá propady jako příležitost, začátečník jako důvod k útěku."
            },
            "Influencer doporučuje na TikToku 'zaručený' nový token": {
                "reakce_A": "Uvědomí si, že influencer už pravděpodobně nakoupil levně dřív a teď jen potřebuje fanoušky, kteří mu nákupem zvednou cenu (exit liquidity).",
                "reakce_B": "Bez rozmýšlení nakoupí, protože influencer má luxusní auto, statisíce sledujících a slibuje zisk 1000 %.",
                "zacatecnik": "B",
                "vysvetleni": "Pokud má někdo 'zaručený' tip na bohatství, nepotřebuje ho křičet do světa na sociálních sítích. Ti, kteří tak činí, většinou potřebují tebe jako svůj zdroj peněz."
            },
            "Centrální banky zvedají úrokové sazby": {
                "reakce_A": "Ignoruje to a diví se, že se mu prodražuje hypotéka a splátky za auto, které si zrovna vzal na dluh.",
                "reakce_B": "Upraví své portfolio — ví, že teď lépe ponesou konzervativní nástroje jako spořicí účty a státní dluhopisy, a zlevní se hypotéky pro budoucí nákup nemovitosti.",
                "zacatecnik": "A",
                "vysvetleni": "Úrokové sazby určují 'cenu peněz'. Když rostou, dluhy jsou dražší a bezpečné spoření výhodnější. Investor s těmito cykly aktivně pracuje."
            }
        }

        vybrana_situace = st.selectbox("Vyber situaci na trhu:", list(scenare.keys()))

        if vybrana_situace != "Vyber situaci...":
            data = scenare[vybrana_situace]
            
            st.markdown(f"**Tvá situace:** *{vybrana_situace}*")
            st.markdown("Přečti si následující dvě reakce a rozhodni, komu patří:")
            
            # Karty s reakcemi a výběrem
            with st.container(border=True):
                col1, col2 = st.columns(2)
                with col1:
                    st.info(f"**Reakce A:**\n\n{data['reakce_A']}")
                    odpoved_A = st.radio("Kdo podle tebe provede Akci A?", ["Vyber...", "Impulzivní začátečník", "Informovaný investor"], key="rad_A")
                    
                with col2:
                    st.warning(f"**Reakce B:**\n\n{data['reakce_B']}")
                    odpoved_B = st.radio("Kdo podle tebe provede Akci B?", ["Vyber...", "Impulzivní začátečník", "Informovaný investor"], key="rad_B")
            
            if st.button("Vyhodnotit moje skóre", type="primary"):
                if odpoved_A == "Vyber..." or odpoved_B == "Vyber...":
                    st.error("⚠️ Nejdřív přiřaď k oběma reakcím příslušného člověka.")
                elif odpoved_A == odpoved_B:
                    st.error("⚠️ Nemůžou oba udělat to samé! Jeden je začátečník, druhý investor.")
                else:
                    # Zjistíme, jestli se uživatel trefil podle našeho klíče
                    spravne_A = odpoved_A == "Impulzivní začátečník" if data["zacatecnik"] == "A" else odpoved_A == "Informovaný investor"
                    spravne_B = odpoved_B == "Impulzivní začátečník" if data["zacatecnik"] == "B" else odpoved_B == "Informovaný investor"
                    
                    if spravne_A and spravne_B:
                        st.success("✅ Přesně tak! Skvěle jsi prokoukl/a psychologii obou přístupů.")
                    else:
                        st.error("❌ Tady ses trochu nechal/a nachytat. Pojďme se podívat proč.")
                        
                    st.markdown(f"""
                    <div class="box-blue">
                        <b>💡 Co si z toho odnést:</b><br>{data['vysvetleni']}
                    </div>
                    """, unsafe_allow_html=True)

        st.divider()

# --- AKTIVITA 3: ČTENÍ GRAFU BEZ ILUZÍ (INTERAKTIVNÍ) ---
        st.markdown("### 📊 Aktivita 3: Čtení grafu bez iluzí (Zoom Efekt)")
        st.write("Grafy mohou vyprávět úplně jiný příběh podle toho, jaký časový výsek si vybereš. Zjisti, jak snadné je nechat se oklamat.")

        typ_grafu = st.selectbox(
            "Vyber aktivum k analýze:", 
            ["Vyber...", "🚀 Aktivum A: Nový revoluční token (Hype)", "📈 Aktivum B: Široký akciový index (S&P 500)"]
        )

        if typ_grafu == "🚀 Aktivum A: Nový revoluční token (Hype)":
            st.markdown("Představ si, že ti kamarád nebo influencer ukáže tento graf se slovy: *„Koukej, za měsíc to udělalo 400 %! Musíme hned nakoupit, než to vyletí ještě výš!“*")
            
            pohled = st.radio("Zvol úhel pohledu:", ["Pohled začátečníka (Poslední 1 měsíc)", "Pohled experta (Celé 2 roky)"], horizontal=True)
            
            if "začátečníka" in pohled:
                # Zobrazíme jen raketový růst (čistá data pro Streamlit line_chart)
                st.line_chart([100, 150, 220, 350, 500], height=250)
                st.warning("👀 **Co vidíš:** Nádherný, strmý růst. Graf vyvolává obrovské FOMO. Zdá se, že to může jít jen nahoru.")
            else:
                # Zobrazíme celou bublinu a následný pád
                st.line_chart([10, 12, 11, 15, 20, 100, 150, 220, 350, 500, 180, 60, 25, 12, 8, 5, 3], height=250)
                st.error("📉 **Realita bez iluzí:** Ten úžasný měsíc byla jen špička splaskávající bubliny (tzv. Pump and Dump). Kdo nakoupil na vrcholu plný emocí, přišel o 99 % svých peněz.")
                
        elif typ_grafu == "📈 Aktivum B: Široký akciový index (S&P 500)":
            st.markdown("Tohle je reálný historický vývoj globálního trhu. Jak vnímáš krize?")
            
            pohled = st.radio("Zvol úhel pohledu:", ["Pohled panikařícího investora (Krize 2008)", "Dlouhodobý horizont (1990 - 2024)"], horizontal=True)
            
            if "panikařícího" in pohled:
                # Zobrazíme jen propad (cca 2007-2009)
                st.line_chart([1565, 1400, 1300, 1100, 900, 735, 676], height=250)
                st.error("👀 **Co vidíš:** Trh padá volným pádem o více než 50 %. Vypadá to jako konec finančního světa. Spousta lidí tady v panice prodala všechno se ztrátou.")
            else:
                # Zobrazíme dlouhodobý trend s krizí jako pouhým "zubem"
                st.line_chart([350, 450, 750, 1400, 1100, 800, 1565, 676, 1100, 1800, 2500, 3200, 4700, 3900, 5000], height=250)
                st.success("📈 **Realita bez iluzí:** Ten hrozivý propad z roku 2008 je v dlouhodobém měřítku jen jeden z mnoha 'zubů'. Trh se časem zotavil a pokračoval v růstu. Dlouhodobý investor krizi jednoduše 'vyseděl'.")

        # Závěrečný check emocí
        if typ_grafu != "Vyber...":
            st.divider()
            st.markdown("#### 🧠 Rychlý test emocí")
            emoc = st.slider("Jakou emoci bys cítil/a, kdybys viděl/a svůj graf padat o 40 % a měl/a v něm své úspory?", 0, 100, 50, help="0 = Extrémní panika a chuť vše prodat, 100 = Zlatá příležitost k nákupu ve slevě")
            
            if emoc < 35:
                st.info("💡 **Tvá reakce:** To je naprosto přirozená lidská reakce. Právě proto bys do kolísavých aktiv neměl/a dávat peníze, které budeš brzy potřebovat. Železné nervy se budují postupně s praxí.")
            elif emoc > 65:
                st.info("💡 **Tvá reakce:** Skvělý přístup! Propady vnímáš jako výprodej a příležitost. Pozor jen na to, abys nekupoval/a 'padající nůž' u pochybných projektů bez vnitřní hodnoty.")
            else:
                st.info("💡 **Tvá reakce:** Klidný střed. Nechceš dělat ukvapené závěry, držíš se svého plánu a nejednáš impulzivně. To je pro dlouhodobého investora ten nejdůležitější stav mysli.")
# =========================================================================
    # 3.9 SHRNUTÍ: CO SI Z FINANČNÍHO TRHU ODNÉST
    # =========================================================================
    if "3.9 Shrnutí" in selected_section_2:  # Zkontroluj název podle tvého selectboxu
        st.markdown("<div class='sub-section-header'>9. SHRNUTÍ KAPITOLY</div>", unsafe_allow_html=True)
        
        st.markdown("## 3.9 Shrnutí: co si z finančního trhu odnést")

        st.markdown("""
        <div class="box-green">
            <b>✅ Klíčové věty:</b>
            <ul>
                <li>Vyšší možný výnos obvykle znamená vyšší riziko.</li>
                <li>Spoření, investování a spekulace nejsou totéž.</li>
                <li>Diverzifikace snižuje závislost na jednom aktivu, ale neruší riziko.</li>
                <li>Historický výnos není slib budoucího výnosu.</li>
                <li>Kryptoměny je nutné chápat jako vysoce rizikové digitální aktivum, ne jako jistý recept na zbohatnutí.</li>
                <li>Pokud nerozumím produktu, poplatkům, rizikům a zdroji výnosu, neměl/a bych do něj vkládat peníze.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="box-purple">
            <b>🤖 AI mentoring:</b> Zkopíruj tento prompt do AI asistenta (např. ChatGPT nebo Claude):
            <br><br>
            <i>„Vysvětli mi rozdíl mezi spořením, investováním a spekulací na příkladu studenta, který má 10 000 Kč. U každé možnosti popiš výnos, riziko, likviditu a vhodný časový horizont.“</i>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("") # prázdný řádek pro vizuální oddělení
        st.success("🎉 Gratuluji k dokončení kapitoly o finančních trzích! Nyní jsi připraven/a využít tyto znalosti v praxi.")
# =========================================================================
    # 3.10 PRÁVNÍ A ETICKÝ DISCLAIMER
    # =========================================================================
    if "3.10 Právní a etický disclaimer" in selected_section_2:  # Zkontroluj název podle tvého selectboxu
        st.markdown("<div class='sub-section-header'>10. ZÁVĚREČNÉ UPOZORNĚNÍ</div>", unsafe_allow_html=True)
        
        st.markdown("## 3.10 Právní a etický disclaimer")
        
        st.write(
            "Tato učebnice a všechny její součásti (včetně textů, interaktivních aktivit, grafů, výpočtů i simulátoru) slouží **výhradně ke vzdělávacím účelům**. "
            "Cílem je naučit tě přemýšlet o penězích, chápat principy finančního trhu a včas rozeznávat rizika."
        )

        st.markdown("""
        <div class="box-red">
            <b>⚖️ Důležité právní upozornění:</b>
            <br><br>
            Žádný text, příklad, výpočet, graf ani scénář v této kapitole <b>není investičním doporučením, finančním ani daňovým poradenstvím a nepředstavuje výzvou k nákupu či prodeji</b> žádného konkrétního finančního aktiva (akcií, fondů, dluhopisů, kryptoměn atd.).
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Co bys měl/a mít vždy na paměti:")
        
        st.markdown("""
        * **Osobní odpovědnost:** Svá reálná finanční rozhodnutí děláš vždy zcela na vlastní zodpovědnost. Trh nebere ohledy na to, jestli jsi udělal/a chybu z neznalosti.
        * **Individuální situace:** Každý člověk má jinou výchozí životní situaci. Co je skvělá investice pro někoho s velkou rezervou a vysokým příjmem, může být finanční sebevražda pro někoho, kdo má dluhy a žije od výplaty k výplatě. Každý má také jinou schopnost snášet případnou ztrátu (toleranci k riziku) a jiný časový horizont.
        * **Historie vs. budoucnost:** Historické výnosy (to, jak se aktivum chovalo včera nebo před deseti lety) nikdy nezaručují stejné nebo podobné výnosy v budoucnosti.
        * **Riziko je všudypřítomné:** Každý finanční produkt nese riziko ztráty. Bez rizika není výnosu. Pokud ti někdo tvrdí, že nabízí „bezpečnou investici s vysokým a garantovaným ziskem“, s největší pravděpodobností lže nebo se jedná o podvod.
        """)

        st.markdown("""
        <div class="box-gray">
            <b>🎓 Závěrečná rada:</b> Než začneš na skutečném trhu investovat své reálné peníze, ujisti se, že máš vybudovanou <b>dostatečnou finanční rezervu na bezpečně dostupném místě</b> (např. spořicí účet). Pro složitá životní rozhodnutí se neboj využít služeb nezávislého odborníka, který je placený přímo tebou za radu, nikoliv z tajných provizí za prodej konkrétních produktů.
        </div>
        """, unsafe_allow_html=True)
        # =========================================================================
    # 4.1 CO JE ÚVĚR
    # =========================================================================
    elif "4.1 " in selected_section_2:
        st.markdown("<div class='sub-section-header'>1. ÚVĚRY A POJIŠTĚNÍ</div>", unsafe_allow_html=True)
        st.markdown("## 4.1 Co je úvěr")
        
        # Úvod k celé kapitole 4
        st.write(
            "Úvěr není „peníze zdarma“. Je to závazek, který přesouvá spotřebu nebo investici z budoucnosti "
            "do současnosti. Díky úvěru může člověk bydlet dříve, než by našetřil celou cenu nemovitosti, "
            "firma může koupit stroj dříve, než na něj vydělá, a domácnost může překlenout dočasný nedostatek peněz."
        )
        st.write(
            "Zároveň ale úvěr vytváří povinnost splácet — i tehdy, když se změní příjem, zdraví, ceny energií "
            "nebo tvá životní situace."
        )
        
        # Designové boxy pro Asides
        st.markdown("""
        <div class="box-blue">
            <b>💳 Základní myšlenka:</b> Úvěr může být užitečný nástroj, pokud financuje smysluplnou potřebu a člověk rozumí ceně, riziku a splácení. Stejný úvěr se ale může stát pastí, pokud vznikne impulzivně, bez rezervy nebo jen proto, že aplikace umožní kliknout na „koupit teď“.
        </div>
        """, unsafe_allow_html=True)
        
        # Nenápadný box pro učitele/RVP
        with st.expander("📘 Informace pro vyučující (Vazba na RVP)"):
            st.write("Tato část rozvíjí finanční gramotnost, odpovědné spotřebitelské rozhodování, orientaci ve finančních produktech, schopnost posoudit cenu úvěru, porovnat nabídky, rozpoznat riziko zadlužení a pochopit význam pojištění pro ochranu osoby, domácnosti i podnikání.")
            
        st.divider()
        
        # Podstata úvěru
        st.markdown("### Jak úvěr funguje?")
        st.write("Úvěr je situace, kdy věřitel poskytne dlužníkovi peníze a dlužník se zaváže, že je v budoucnu vrátí. Obvykle vrací nejen půjčenou částku, ale také úrok a další náklady.")
        
        st.markdown("""
        <div class="box-green">
            <b>🧠 Jednoduše:</b> Když si půjčíš, nekupuješ jen věc. Kupuješ si také čas. A za čas se ve financích platí.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 📖 Slovníček základních pojmů")
        st.write("Proklikni si jednotlivé karty a seznam se s pojmy, které tě budou světem úvěrů provázet. Budeš je potřebovat v aktivitě níže!")
        
        # Interaktivní layout pro slovníček
        col1, col2, col3 = st.columns(3)
        with col1:
            with st.expander("Věřitel & Dlužník"):
                st.write("**Věřitel:** Ten, kdo půjčuje peníze (např. banka nebo nebankovní společnost).")
                st.write("**Dlužník:** Ten, kdo si půjčuje (např. ty).")
        with col2:
            with st.expander("Jistina & Úrok"):
                st.write("**Jistina:** Původně půjčená částka (kolik sis reálně odnesl/a).")
                st.write("**Úrok:** Cena za půjčení peněz (odměna věřiteli).")
        with col3:
            with st.expander("Splátka & Splatnost"):
                st.write("**Splátka:** Pravidelná částka, kterou dlužník platí (např. každý měsíc).")
                st.write("**Splatnost:** Doba, za kterou má být celý úvěr splacen.")
                
        col4, col5 = st.columns(2)
        with col4:
            with st.expander("Zajištění & Ručitel"):
                st.write("**Zajištění:** Majetek nebo jiná jistota pro věřitele (např. byt u hypotéky – když neplatíš, věřitel ho prodá).")
                st.write("**Ručitel:** Osoba, která na sebe bere povinnost splácet, pokud dlužník přestane.")
        with col5:
            with st.expander("RPSN (Nejdůležitější zkratka!)"):
                st.write("**RPSN = Roční procentní sazba nákladů.**")
                st.write("Nejdůležitější ukazatel! Vyjadřuje *celkovou* cenu úvěru za rok, včetně úplně všech poplatků (za vedení, za schválení atd.). Samotný úrok může být klamavý, RPSN říká celou pravdu.")
        
        st.divider()
        
        # --- AKTIVITA: ROZKLÍČUJ ÚVĚR V PRAXI ---
        st.markdown("### 🧩 Aktivita: Úvěr v praxi")
        st.write("Přečti si následující situaci a zkus správně zařadit pojmy k číslům.")
        
        with st.container(border=True):
            st.info("Příběh: **Klára (25)** potřebuje auto na dojíždění do práce. Půjčí si **200 000 Kč** od **Banky XY**. Dohodnou se, že Klára bude platit **4 500 Kč** každý měsíc po dobu **5 let**. Celková cena úvěru se všemi poplatky vychází na **8,5 % ročně**.")
            
            # Kvíz
            q1 = st.selectbox("Kdo je v tomto příběhu VĚŘITEL?", ["Vyber odpověď...", "Klára", "Banka XY", "Prodejce aut"])
            q2 = st.selectbox("Co představuje částka 200 000 Kč?", ["Vyber odpověď...", "Jistinu", "Úrok", "RPSN"])
            q3 = st.selectbox("Co představuje hodnota 8,5 %?", ["Vyber odpověď...", "Splatnost", "Jistinu", "RPSN"])
            q4 = st.selectbox("Co představuje doba 5 let?", ["Vyber odpověď...", "Splatnost", "Zajištění", "Splátku"])
            
            if st.button("Zkontrolovat mé odpovědi", type="primary"):
                if "Vyber odpověď..." in [q1, q2, q3, q4]:
                    st.warning("⚠️ Nejdříve vyber všechny odpovědi!")
                elif q1 == "Banka XY" and q2 == "Jistinu" and q3 == "RPSN" and q4 == "Splatnost":
                    st.success("✅ Výborně! Všechny pojmy jsi správně zařadil/a. Můžeme pokračovat dál.")
                    st.balloons()
                else:
                    st.error("❌ Někde je chybka. Zkus to ještě jednou. Nápovědu najdeš ve slovníčku výše.")
                    # =========================================================================
    # 4.2 ÚROK: CENA PŮJČENÝCH PENĚZ
    # =========================================================================
    elif "4.2" in selected_section_2:
        st.markdown("<div class='sub-section-header'>2. ÚVĚRY A POJIŠTĚNÍ</div>", unsafe_allow_html=True)
        st.markdown("## 4.2 Úrok: cena půjčených peněz")
        
        st.write(
            "Úrok je odměna věřiteli za to, že dlužník může používat jeho peníze. Úrok zároveň kompenzuje riziko, "
            "že dlužník nesplatí, a čas, po který věřitel peníze nemůže využít jinak."
        )
        st.write("Úroková sazba se obvykle uvádí v procentech za rok. Pokud je úroková sazba **10 % p. a.**, znamená to „per annum“, tedy ročně.")
        
        # Tabulka pojmů
        st.markdown("### 📊 Základní pojmy v číslech")
        st.markdown("""
        | Pojem | Co to znamená | Příklad |
        | :--- | :--- | :--- |
        | **Jistina** | Půjčená částka. | 100 000 Kč |
        | **Úroková sazba** | Procento, podle kterého se počítá úrok. | 8 % ročně |
        | **Úrok** | Částka zaplacená navíc za půjčení peněz. | 8 000 Kč za rok (při jednoduchém úročení) |
        | **Splátka** | Částka pravidelně placená věřiteli. | např. 3 200 Kč měsíčně |
        """)
        
        st.write("**Výši úroku v praxi ovlivňuje:** výše půjčené částky, úroková sazba, délka splácení, způsob splácení, rizikovost klienta, typ úvěru, zajištění a situace na trhu (sazby v ekonomice).")
        
        st.divider()
        
        st.markdown("### 4.2.1 Proč je úrok u různých úvěrů jiný")
        st.write("Ne každý úvěr má stejnou úrokovou sazbu. Banka posuzuje riziko. Čím vyšší riziko, tím vyšší cena úvěru obvykle bývá.")
        
        with st.expander("🏠 Hypotéka"):
            st.write("Je zajištěná nemovitostí, proto bývá levnější než nezajištěný úvěr.")
            st.warning("**Typické riziko:** Dlouhá doba splácení, změna úrokových sazeb, pokles příjmu během desítek let.")
            
        with st.expander("🚗 Spotřebitelský úvěr"):
            st.write("Často není zajištěný hodnotným majetkem.")
            st.warning("**Typické riziko:** Vyšší riziko nesplácení, peníze se často utratí za věci s klesající hodnotou.")
            
        with st.expander("💳 Kreditní karta & Kontokorent"):
            st.write("**Kreditní karta:** Jde o rychle dostupný úvěrový rámec. **Kontokorent:** Krátkodobé přečerpání účtu do mínusu.")
            st.warning("**Typické riziko:** Snadné zvyknutí si na život „v mínusu“ a extrémně vysoký úrok, pokud peníze nevrátíš v bezúročném období.")
            
        with st.expander("🏢 Podnikatelský úvěr"):
            st.write("Závisí na stabilitě podnikání, cashflow a zajištění.")
            st.warning("**Typické riziko:** Nejisté tržby, sezónnost, celkové podnikatelské riziko (firma může zkrachovat).")

        st.divider()
        
        # --- AKTIVITA: INTERAKTIVNÍ KALKULAČKA ---
        st.markdown("### 🧮 Interaktivní zóna: Jak délka úvěru prodražuje půjčku")
        st.write("Vyzkoušej si, co se stane, když si půjčíš 100 000 Kč s úrokem 8 % a budeš měnit dobu splácení.")
        
        doba_splaceni = st.slider("Doba splácení (v letech):", min_value=1, max_value=10, value=5)
        
        # Jednoduchý anuitní výpočet pro ukázku
        sazba_mesicni = 0.08 / 12
        pocet_splatek = doba_splaceni * 12
        jistina = 100000
        # Vzorec pro anuitní splátku
        splatka = jistina * (sazba_mesicni * (1 + sazba_mesicni)**pocet_splatek) / ((1 + sazba_mesicni)**pocet_splatek - 1)
        celkem_zaplaceno = splatka * pocet_splatek
        preplatek = celkem_zaplaceno - jistina
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Měsíční splátka", f"{int(splatka):,} Kč".replace(",", " "))
        col2.metric("Celkem zaplatíš", f"{int(celkem_zaplaceno):,} Kč".replace(",", " "))
        col3.metric("Přeplatek (čistý úrok)", f"{int(preplatek):,} Kč".replace(",", " "), delta_color="inverse")
        
        st.info("💡 **Všimni si:** Čím déle splácíš, tím je sice měsíční splátka menší (vypadá to lákavě), ale tím víc peněz celkově vyhodíš oknem na úrocích!")

    # =========================================================================
    # 4.3 RPSN: SKUTEČNĚJŠÍ CENA ÚVĚRU
    # =========================================================================
    elif "4.3" in selected_section_2:
        st.markdown("<div class='sub-section-header'>3. ÚVĚRY A POJIŠTĚNÍ</div>", unsafe_allow_html=True)
        st.markdown("## 4.3 RPSN: skutečnější cena úvěru")
        
        st.write("Úroková sazba neříká celou pravdu. Úvěr může mít kromě úroku také poplatky, pojištění, náklady na vyřízení, vedení úvěrového účtu nebo jiné povinné platby. Proto existuje **RPSN — roční procentní sazba nákladů**.")
        st.write("RPSN ukazuje, kolik úvěr stojí za rok v procentech, když se započítají **nejen úroky, ale i další povinné náklady** související s úvěrem.")
        
        st.markdown("""
        <div class="box-green">
            <b>🔎 RPSN jednoduše:</b> Úrok je jen část ceny. RPSN se snaží ukázat celkovou cenu úvěru. Když porovnáváš dvě půjčky, samotný úrok nestačí — dívej se hlavně na RPSN a celkovou částku, kterou zaplatíš.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 4.3.1 Proč může být nízký úrok drahý")
        st.write("Představ si dvě nabídky na stejnou částku. Kterou by sis vybral/a, kdyby ses díval/a jen na úrok?")
        
        col1, col2 = st.columns(2)
        with col1:
            st.info("**Nabídka A (Férová)**\n* Úrok: **7 %**\n* Poplatky: Nízké\n* **RPSN: 7,5 %**\n\n*Úrok i celkové náklady jsou si velmi podobné.*")
        with col2:
            st.error("**Nabídka B (Chyták)**\n* Úrok: **5 %**\n* Poplatky: Extrémně vysoké\n* **RPSN: 12 %**\n\n*Nízký úrok je jen marketing, úvěr je reálně mnohem dražší.*")

        st.markdown("""
        <div class="box-red">
            <b>⚠️ Pozor na reklamu:</b> Věta „úrok od 4,9 %“ neznamená, že přesně takový úvěr dostane každý. Slovo „od“ znamená nejlepší možnou sazbu pro vybrané, dokonalé klienty. Skutečná nabídka závisí na tvém příjmu, závazcích a historii.
        </div>
        """, unsafe_allow_html=True)
        
        st.divider()
        
        st.markdown("### 4.3.2 Předletová kontrola: Co sledovat u každého úvěru")
        st.write("Před podpisem jakékoliv smlouvy bys měl/a znát odpovědi na všechny tyto body. Zkus si je odškrtat!")
        
        # Interaktivní checklist
        c1 = st.checkbox("Vím, kolik si půjčuji a kolik přesně celkem vrátím.")
        c2 = st.checkbox("Znám výši měsíční splátky a vím, jak dlouho budu splácet.")
        c3 = st.checkbox("Znám nejen úrokovou sazbu, ale hlavně RPSN.")
        c4 = st.checkbox("Vím o všech dalších poplatcích (za vedení, sjednání atd.).")
        c5 = st.checkbox("Vím, zda je úvěr zajištěný mým majetkem (a o co můžu přijít).")
        c6 = st.checkbox("Vím, jaké jsou sankce, když se se splátkou opozdím.")
        c7 = st.checkbox("Vím, zda a za kolik můžu úvěr splatit předčasně.")
        
        if c1 and c2 and c3 and c4 and c5 and c6 and c7:
            st.success("✅ Výborně! Jsi zodpovědný spotřebitel. Takhle by měla vypadat tvá kontrola před každým podpisem.")
            
        st.markdown("""
        <div class="box-blue">
            <b>🧮 Pravidlo bezpečné splátky:</b> Splátka nemá být nastavena tak, že člověk přežije jen v ideálním měsíci. Musí počítat i s nemocí, výpadkem brigády, zdražením energií nebo nečekanou opravou.
        </div>
        """, unsafe_allow_html=True)

# =========================================================================
    # 4.4 NE KAŽDÝ ÚVĚR DOSTANE
    # =========================================================================
    elif "4.4" in selected_section_2:
        st.markdown("<div class='sub-section-header'>4. ÚVĚRY A POJIŠTĚNÍ</div>", unsafe_allow_html=True)
        st.markdown("## 4.4 Ne každý úvěr dostane")
        
        st.write("Banky a další věřitelé neposkytují úvěr automaticky každému. Musí posoudit, zda dlužník pravděpodobně zvládne splácet. Smyslem není jen ochrana banky, ale také ochrana klienta před nebezpečným předlužením.")
        
        st.markdown("### Co banka posuzuje (Scoring klienta):")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("- **Věk:** Dosažení 18 let a u dlouhých úvěrů max. věk při doplacení.")
            st.markdown("- **Příjem:** Zda je dostatečný a hlavně pravidelný.")
            st.markdown("- **Výdaje:** Nájem, energie, děti, životní minimum.")
            st.markdown("- **Stávající dluhy:** Kreditky, kontokorent, jiné úvěry.")
        with col2:
            st.markdown("- **Platební historie:** Zda člověk v minulosti splácel včas.")
            st.markdown("- **Registry dlužníků:** Databáze, kde banky vidí všechny tvé dluhy a průšvihy.")
            st.markdown("- **Typ zaměstnání:** Stabilita práce (smlouva na neurčito vs. zkušební doba).")
            st.markdown("- **Zajištění a účel:** Co bance ručíš a na co peníze chceš.")
            
        st.markdown("""
        <div class="box-gray">
            <b>🚦 Důležité:</b> Zamítnutý úvěr nemusí být „nespravedlnost“. Může to být signál, že by splácení bylo příliš rizikové. Pokud banka nepůjčí, často tím říká: podle matematiky by tohle tvůj rozpočet už nemusel unést.
        </div>
        """, unsafe_allow_html=True)
        
        st.divider()

        # --- NOVÝ BLOK: SPECIFICKÉ LIMITY ---
        st.markdown("### 🧮 Zlatá pravidla: Kolik mi banka reálně půjčí?")
        st.write("Neexistuje jedna univerzální částka, protože každý má jiný plat a jiné výdaje. Banky se ale řídí přísnými matematickými vzorci (často podle doporučení České národní banky). Tady je orientační přehled toho, co musíš splňovat:")

        col_m1, col_m2, col_m3 = st.columns(3)
        with col_m1:
            st.metric(label="Max. splátky k platu", value="45 – 50 %", delta="Z čistého příjmu", delta_color="off")
            st.write("Všechny tvé měsíční splátky dohromady (včetně té nové) by nikdy neměly spolknout víc než polovinu tvého čistého měsíčního platu. Pokud bereš 30 000 Kč čistého, tvé splátky nesmí přesáhnout zhruba 15 000 Kč.")
        with col_m2:
            st.metric(label="Zůstatek pro život", value="Životní min.", delta="+ Běžné výdaje", delta_color="off")
            st.write("Po odečtení všech splátek ti musí na účtu zůstat dostatek peněz na zákonné životní minimum a základní chod domácnosti (nájem, jídlo, poplatky). Pokud ti po splátce nezbude na jídlo, banka úvěr zamítne.")
        with col_m3:
            st.metric(label="Vlastní úspory", value="10 – 20 %", delta="Nutné u hypoték", delta_color="off")
            st.write("U hypoték (úvěrů na bydlení) banka ze zákona nesmí půjčit 100 % ceny. Pokud chceš koupit byt za 5 milionů Kč, musíš mít na svém účtu naspořeno alespoň 500 000 až 1 000 000 Kč z vlastních peněz.")

        st.divider()
        
        st.markdown("### 4.4.1 Proč mi nepůjčí tolik, kolik chci")
        st.write("Častý omyl zní: *„Když zvládnu měsíční splátku podle sebe, banka mi musí půjčit.“* Nemusí. Banka musí pracovat s přísnými pravidly a odpovědným posouzením schopnosti splácet.")
        
        st.write("**Banka může půjčit méně, nebo vůbec, protože:**")
        st.markdown("""
        * Tvůj oficiální čistý příjem nestačí na požadovanou splátku podle pravidla výše.
        * Máš už jiné závazky (byť je právě nesplácíš, např. nepoužívanou kreditní kartu – i ta se počítá jako dluh a snižuje tvůj limit).
        * Tvůj příjem je nepravidelný (např. jsi OSVČ s výkyvy), pracuješ na brigády, nebo jsi ve zkušební/výpovědní lhůtě.
        * Máš škraloup v registrech dlužníků (třeba i za pozdě zaplacený paušál za telefon).
        * Nemovitost, kterou chceš koupit, má podle odhadce banky nižší hodnotu, než za ni chceš zaplatit prodejci.
        * Nemáš dostatek vlastních naspořených peněz pro základ vkladu.
        """)
        # =========================================================================
    # 4.5 POSTUP POSKYTNUTÍ SPOTŘEBITELSKÉHO ÚVĚRU
    # =========================================================================
    elif "4.5" in selected_section_2:
        st.markdown("<div class='sub-section-header'>5. ÚVĚRY A POJIŠTĚNÍ</div>", unsafe_allow_html=True)
        st.markdown("## 4.5 Postup poskytnutí spotřebitelského úvěru")
        
        st.write("Spotřebitelský úvěr je úvěr pro fyzickou osobu — spotřebitele. Může sloužit například na vybavení domácnosti, auto, elektroniku, rekonstrukci, studium nebo konsolidaci dluhů.")
        st.write("**Základní pravidlo:** Úvěr by nikdy neměl sloužit k zakrývání dlouhodobého problému, kdy člověk pravidelně utrácí víc, než vydělává.")

        st.markdown("""
        <div class="box-purple">
            <b>📱 Současná realita:</b> Úvěr lze dnes někdy sjednat v mobilu za pár minut. Rychlost ale nesmí nahradit přemýšlení. Čím rychlejší je tlačítko „půjčit si“, tím pomalejší by mělo být tvé rozhodnutí.
        </div>
        """, unsafe_allow_html=True)
        
        st.divider()

        # --- INTERAKTIVNÍ ČASOVÁ OSA ---
        st.markdown("### ⏱️ Typický postup (Časová osa)")
        st.write("Posouvej jezdcem a podívej se, čím vším musíš projít, než peníze opravdu dostaneš.")
        
        faze = st.select_slider(
            "Fáze úvěru:",
            options=["1. Výběr", "2. Žádost", "3. Ověření", "4. Posouzení", "5. Smlouva", "6. Čerpání a splácení"]
        )

        with st.container(border=True):
            if faze == "1. Výběr":
                st.info("**1. Výběr nabídky**\n\nKlient porovná úrok, RPSN, splátku, celkovou zaplacenou částku a podmínky u různých bank.")
            elif faze == "2. Žádost":
                st.info("**2. Žádost o úvěr**\n\nVyplníš údaje o sobě, svých příjmech, výdajích a dalších závazcích (jiné úvěry, děti, nájem).")
            elif faze == "3. Ověření":
                st.info("**3. Ověření totožnosti a doložení příjmu**\n\nBanka si tě prověří (online nebo osobně). Bude chtít potvrzení od zaměstnavatele nebo výpisy z účtu za poslední měsíce.")
            elif faze == "4. Posouzení":
                st.info("**4. Kontrola registrů a posouzení schopnosti splácet**\n\nVěřitel ověřuje tvou úvěrovou historii (zda nedlužíš jinde) a matematicky vyhodnotí, zda tvůj rozpočet úvěr unese.")
            elif faze == "5. Smlouva":
                st.info("**5. Nabídka podmínek a podpis smlouvy**\n\nDostaneš finální nabídku (skutečná sazba se může lišit od reklamy!). Po podpisu se zavazuješ splácet.")
            elif faze == "6. Čerpání a splácení":
                st.info("**6. Čerpání peněz a splácení**\n\nPeníze přijdou na tvůj účet (nebo přímo obchodníkovi). Začíná platit splátkový kalendář.")

        st.divider()

        st.markdown("### 4.5.1 Druhy spotřebitelských úvěrů")
        
        st.markdown("""
        | Druh | Jak to funguje | Typické riziko |
        | :--- | :--- | :--- |
        | **Účelový úvěr** | Peníze jsou určeny na konkrétní věc (auto, rekonstrukce). | Menší flexibilita, ale často získáš lepší podmínky a nižší úrok. |
        | **Neúčelový úvěr** | Klient nemusí přesně dokládat, na co peníze použije. | Volnost může svádět k financování hloupostí a zbytečností. |
        | **Kreditní karta** | Opakovaně dostupný limit s bezúročným obdobím. | Extrémně vysoký úrok při nesplacení včas. |
        | **Kontokorent** | Možnost jít na svém běžném účtu do mínusu. | Člověk si snadno zvykne žít z peněz, které nemá, a uvízne v pasti. |
        | **Konsolidace** | Sloučení více malých úvěrů do jednoho velkého. | Může sice snížit měsíční splátku, ale často prodlouží splácení a zvýší celkové náklady. |
        | **Odložená platba (BNPL)** | „Kup teď, zaplať později“ (např. v e-shopu). | Psychologicky maskuje dluh jako pohodlnou platbu. |
        """)


    # =========================================================================
    # 4.6 HYPOTÉKA: ÚVĚR NA BYDLENÍ
    # =========================================================================
    elif "4.6" in selected_section_2:
        st.markdown("<div class='sub-section-header'>6. ÚVĚRY A POJIŠTĚNÍ</div>", unsafe_allow_html=True)
        st.markdown("## 4.6 Hypotéka: úvěr na bydlení")
        
        st.write("Hypotéka je dlouhodobý úvěr, obvykle **zajištěný nemovitostí**. Používá se hlavně na koupi, výstavbu nebo rekonstrukci bydlení. Protože jde často o milionové částky a splácení na desítky let, patří mezi nejvážnější finanční rozhodnutí v životě.")

        st.markdown("""
        <div class="box-green">
            <b>🏠 Hypotéka jednoduše:</b> Banka ti půjčí peníze na dům, ale jako zajištění má k němu zástavní právo. Pokud bys dlouhodobě nesplácel/a, banka může svou pohledávku řešit tím, že nemovitost prodá.
        </div>
        """, unsafe_allow_html=True)
        
        st.divider()

        # --- LTV KALKULAČKA ---
        st.markdown("### 4.6.1 Proč banka nepůjčí 100 % ceny (Ukazatel LTV)")
        st.write("U hypotéky musí mít žadatel zpravidla část vlastních peněz. Pokud by cena nemovitosti v krizi klesla a klient přestal splácet, banka by při prodeji nemusela získat zpět celou půjčenou částku.")
        st.write("Základním metrikou je **LTV (Loan to Value)** — poměr výše úvěru k odhadní hodnotě nemovitosti. Banky standardně půjčují maximálně 80 % (pro mladé do 36 let někdy 90 %).")

        with st.container(border=True):
            st.markdown("#### 🧮 Otestuj si LTV")
            cena_nemovitosti = st.slider("Hodnota nemovitosti (Kč):", 1000000, 10000000, 4000000, step=100000)
            vlastni_penize = st.slider("Tvé vlastní úspory (Kč):", 0, 5000000, 800000, step=50000)
            
            pozadovany_uver = cena_nemovitosti - vlastni_penize
            
            if cena_nemovitosti > 0:
                ltv = (pozadovany_uver / cena_nemovitosti) * 100
            else:
                ltv = 0

            col1, col2, col3 = st.columns(3)
            col1.metric("Banka ti půjčí", f"{pozadovany_uver:,} Kč".replace(",", " "))
            col2.metric("Tvé peníze", f"{vlastni_penize:,} Kč".replace(",", " "))
            
            if ltv > 90:
                col3.metric("LTV", f"{ltv:.1f} %", delta="Zamítnuto (nad 90 %)", delta_color="inverse")
                st.error("❌ Takto hypotéku nedostaneš. LTV je příliš vysoké. Musíš buď naspořit více vlastních peněz, nebo si vybrat levnější nemovitost.")
            elif ltv > 80:
                col3.metric("LTV", f"{ltv:.1f} %", delta="Hraniční (80 - 90 %)", delta_color="off")
                st.warning("⚠️ LTV mezi 80 % a 90 % banky schvalují jen výjimečně, většinou jen žadatelům do 36 let a s přísnějšími podmínkami.")
            else:
                col3.metric("LTV", f"{ltv:.1f} %", delta="Ideální (pod 80 %)", delta_color="normal")
                st.success("✅ Tvé LTV je v bezpečné zóně. Z tohoto pohledu by banka úvěr schválila.")

        st.markdown("""
        <div class="box-red">
            <b>⚠️ Pozor na skryté náklady:</b> Vlastní peníze nejsou jen „část kupní ceny“. Jako kupující musíš mít rezervu na právní služby, odhad nemovitosti, stěhování, provizi realitce, rekonstrukci nebo nábytek! Tyto věci z hypotéky většinou nezaplatíš.
        </div>
        """, unsafe_allow_html=True)

        st.divider()

        st.markdown("### 4.6.2 Postup získání hypotéky")
        st.write("Proces je mnohem složitější a delší než u běžného úvěru v mobilu. Zahrnuje:")
        
        st.markdown("""
        1. **Předběžné posouzení:** Zjištění, jakou splátku tvůj rozpočet snese.
        2. **Kontrola vlastních peněz:** Kolik máš a kolik musí zbýt jako rezerva.
        3. **Výběr nemovitosti:** Nalezení vysněného bydlení.
        4. **Odhad nemovitosti:** Odhadce banky posoudí hodnotu (často bývá nižší než kupní cena v inzerátu!).
        5. **Žádost o hypotéku:** Doložení hromady papírů o příjmech a nemovitosti.
        6. **Posouzení bonity:** Banka hodnotí schopnost splácet na dekády dopředu.
        7. **Podpis dokumentace:** Úvěrová smlouva a zástavní právo (řeší se přes katastr nemovitostí).
        8. **Čerpání a splácení.**
        """)

        st.divider()

        st.markdown("### 4.6.3 Fixace úrokové sazby")
        st.write("U hypotéky se úrok sjednává na dobu určitou (fixace). Během této doby se ti nemůže zvednout splátka, ani kdyby byla na trhu krize. Po skončení fixace ti banka nabídne úrok nový.")

        col4, col5 = st.columns(2)
        with col4:
            st.info("**Kratší fixace (např. 1 - 3 roky)**\n\n**Výhoda:** Možnost dříve reagovat, pokud úroky na trhu klesají.\n\n**Riziko:** Splátka ti může rychle zdražit, pokud sazby na trhu vzrostou.")
        with col5:
            st.info("**Delší fixace (např. 7 - 10 let)**\n\n**Výhoda:** Jistota a klidný spánek, splátka se dlouho nezmění.\n\n**Riziko:** Nemusíš využít případný pokles sazeb na trhu a předčasné splacení může mít podmínky.")

        st.divider()

        st.markdown("### 4.6.4 Hypotéka vs. Spotřebitelský úvěr")
        st.markdown("""
        | Vlastnost | Spotřebitelský úvěr | Hypotéka |
        | :--- | :--- | :--- |
        | **Účel** | Auto, elektronika, spotřeba | Bydlení, nemovitost, výstavba |
        | **Výše částky** | Desítky až stovky tisíc Kč | Často miliony Kč |
        | **Doba splácení** | Měsíce až jednotky let | Desítky let (např. 25–30 let) |
        | **Zajištění** | Většinou bez zajištění | Zástavní právo k nemovitosti |
        | **Posouzení** | Příjem, výdaje, registry | To samé + hodnota nemovitosti, vlastní zdroje a LTV |
        """)
# =========================================================================
    # 4.7 PODNIKATELSKÉ ÚVĚRY
    # =========================================================================
    elif "4.7" in selected_section_2:
        st.markdown("<div class='sub-section-header'>7. ÚVĚRY A POJIŠTĚNÍ</div>", unsafe_allow_html=True)
        st.markdown("## 4.7 Podnikatelské úvěry")
        
        st.write("Podnikatelé a firmy si nepůjčují jen na osobní spotřebu. Úvěr může sloužit k rozjezdu podnikání, nákupu stroje, zásob, auta, vybavení provozovny, překlenutí období mezi fakturací a zaplacením nebo k celkové expanzi.")

        st.markdown("""
        <div class="box-blue">
            <b>🏭 Podnikatelský rozdíl:</b> U domácnosti se banka ptá hlavně: <i>„Zvládne člověk splácet ze svého stabilního příjmu?“</i> U firmy se ale ptá: <i>„Bude toto podnikání vytvářet dost peněz (cashflow), aby úvěr samo splatilo?“</i>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### Možnosti financování firmy")
        st.write("Klikni na jednotlivé kategorie a podívej se, jaké nástroje firmy využívají:")
        
        tab1, tab2, tab3 = st.tabs(["Klasické úvěry", "Provoz a cashflow", "Alternativy k dluhu"])
        with tab1:
            st.info("**Provozní úvěr:** Financování běžného chodu firmy, nákupu zásob, mezd nebo nezaplacených faktur.\n\n**Investiční úvěr:** Nákup drahých strojů, technologií, vozidel, vybavení nebo nemovitostí.\n\n**Hypoteční úvěr pro podnikání:** Financování podnikatelské nemovitosti (haly, kanceláře).")
        with tab2:
            st.info("**Kontokorent pro podnikatele:** Krátkodobé přečerpání podnikatelského účtu pro vyrovnání výkyvů.\n\n**Faktoring:** Firma získá peníze od banky dříve, než jí reálně zaplatí její zákazníci za vystavené faktury.\n\n**Bankovní záruka:** Banka nepůjčí peníze, ale ručí obchodnímu partnerovi za to, že firma splní svůj závazek.")
        with tab3:
            st.info("**Leasing:** Financování auta, stroje nebo vybavení (stroj často patří leasingovce, dokud se nesplatí).\n\n**Úvěr se zárukou:** Například s podporou státní záruční instituce (pro začínající podnikatele).\n\n**Investor místo úvěru:** Firma nevytvoří dluh, ale prodá část svého podílu investorovi (získá peníze za část vlastnictví).")

        st.divider()

        st.markdown("### 4.7.1 Co banka řeší u podnikatele")
        st.write("Při žádosti o firemní úvěr banka posuzuje spoustu věcí. Není to jen o jednom platu jako u zaměstnance.")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("- **Historie podnikání:** Jak dlouho firma funguje.")
            st.markdown("- **Účetnictví:** Daňová přiznání nebo účetní výkazy.")
            st.markdown("- **Tržby a zisk:** Kolik firma prodá a co jí zbyde.")
            st.markdown("- **Cashflow:** Reálný tok peněz (viz box níže!).")
            st.markdown("- **Stávající dluhy a zajištění:** Čím může firma ručit.")
        with col2:
            st.markdown("- **Obor a sezónnost:** Zda firma prodává jen v létě/v zimě.")
            st.markdown("- **Účel úvěru:** Dává nákup stroje matematický smysl?")
            st.markdown("- **Podnikatelský plán:** Jaké má firma vyhlídky do budoucna.")
            st.markdown("- **Osobní ručení majitele:** Někdy musí majitel ručit i svým domem.")
            st.markdown("- **Odolnost:** Schopnost přežít horší období (krize).")

        st.markdown("""
        <div class="box-gray">
            <b>📊 Cashflow je klíč:</b> Firma může být na papíře (v účetnictví) zisková. Ale pokud jí zákazníci platí faktury se zpožděním 3 měsíce a ona musí každý měsíc platit mzdy, nájem a dodavatele, reálně nemá na účtu peníze a může zkrachovat i přesto, že je „zisková“.
        </div>
        """, unsafe_allow_html=True)


    # =========================================================================
    # 4.8 KDYŽ SE SPLÁCENÍ POKAZÍ
    # =========================================================================
    elif "4.8" in selected_section_2:
        st.markdown("<div class='sub-section-header'>8. ÚVĚRY A POJIŠTĚNÍ</div>", unsafe_allow_html=True)
        st.markdown("## 4.8 Když se splácení pokazí")
        
        st.write("Problém se splácením není dobré ignorovat. Ztráta práce, nemoc nebo náhlé výdaje mohou potkat každého.")
        
        st.error("💀 **Nejhorší možná strategie:** Přestat komunikovat, hrát „mrtvého brouka“, neotvírat dopisy, smazat bankovní aplikaci a doufat, že se dluh vyřeší sám. Nevyřeší. Jen neuvěřitelně naroste o sankce a soudní poplatky.")

        with st.container(border=True):
            st.markdown("### 🚑 Záchranný plán: Co dělat, když hrozí problém")
            st.write("Odškrtni si kroky, které bys měl okamžitě podniknout:")
            st.checkbox("Zastavit jakékoliv další zadlužování (žádné nové půjčky na zaplacení starých!).")
            st.checkbox("Spočítat si krutě upřímný a reálný měsíční rozpočet (kde můžu osekat výdaje).")
            st.checkbox("Kontaktovat věřitele co nejdříve (banky preferují lidi, kteří problém hlásí předem).")
            st.checkbox("Požádat banku o úpravu splátek, odklad nebo restrukturalizaci (pokud to jde).")
            st.checkbox("Vyhledat odbornou pomoc zdarma (např. Poradna při finanční tísni, občanská poradna).")

        st.divider()

        st.markdown("### ⚠️ Rizika nesplácení")
        st.write("Pokud situaci neřešíš, banka po určité době přistoupí k tvrdým krokům:")
        
        col_r1, col_r2 = st.columns(2)
        with col_r1:
            st.markdown("1. **Upomínky a sankce** (dluh se prodražuje).")
            st.markdown("2. **Zápis v registrech dlužníků** (na roky zničená úvěrová historie).")
            st.markdown("3. **Zesplatnění úvěru** (banka chce doplatit zbytek dluhu okamžitě celý).")
        with col_r2:
            st.markdown("4. **Ztráta majetku** (u zajištěných úvěrů - banka prodá dům/auto).")
            st.markdown("5. **Soud a Exekuce** (exekutor ti zablokuje účty a srazí peníze z platu).")
            st.markdown("6. **Dlouhodobý psychický stres** (často končící rozpadem rodiny).")


    # =========================================================================
    # 4.9 PAST JMÉNEM „KUP TEĎ, ZAPLAŤ POZDĚJI“
    # =========================================================================
    elif "4.9" in selected_section_2:
        st.markdown("<div class='sub-section-header'>9. ÚVĚRY A POJIŠTĚNÍ</div>", unsafe_allow_html=True)
        st.markdown("## 4.9 Past jménem „Kup teď, zaplať později“ (BNPL)")
        
        st.write("**BNPL (Buy Now, Pay Later)** je pro současnou generaci extrémně lákavá věc. Tváří se totiž jako moderní, pohodlná platební funkce v e-shopu (Twisto, Klarna, Skip Pay, Apple Pay Later), nikoliv jako dluh. Člověk dostane věc hned a placení se posune do budoucnosti (obvykle o 14 až 30 dní).")

        st.markdown("""
        <div class="box-red">
            <b>📱 Hlavní psychologický problém:</b> BNPL odstraňuje „bolest z placení“. Když musíš vytáhnout z peněženky 3 tisíce, bolí to. Když klikneš na „zaplatit za měsíc“, tvůj mozek má pocit, že je nákup zadarmo, protože peníze z účtu neodešly.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Co ti u BNPL hrozí:")
        st.markdown("""
        * **Ztráta přehledu:** Máš 5 různých odložených plateb v různých e-shopech a zapomeneš na ně.
        * **Efekt sněhové koule:** Drobné částky (jídlo, tričko, kosmetika) se na konci měsíce poskládají do obřího dluhu.
        * **Impulzivita:** Koupíš si věc, kterou vlastně nepotřebuješ a na kterou reálně nemáš peníze.
        * **Poplatky:** Jakmile platbu nestihneš doplatit včas, naskáčou ti obrovské sankční poplatky.
        """)

        st.divider()

        # --- AKTIVITA: ANALYZÁTOR NÁKUPU ---
        st.markdown("### 🧩 Aktivita: Je to potřeba, přání, nebo dluhová past?")
        st.write("Vyber si jeden z typických nákupů mladých lidí na odloženou platbu. Odpověz upřímně na otázky a zjisti svůj výsledek.")

        nakup = st.selectbox("Vyber nákup, který bys chtěl/a zaplatit přes BNPL:", 
                             ["Vyber...", 
                              "Značkové tenisky (4 000 Kč)", 
                              "Lístky na letní festival s kamarády (3 500 Kč)", 
                              "Objednávka jídla na večerní párty (1 500 Kč)",
                              "Nový herní doplněk / skiny (1 000 Kč)",
                              "Rozbitý mobil, bez kterého nemůžu fungovat do školy/práce (5 000 Kč)"])

        if nakup != "Vyber...":
            with st.container(border=True):
                st.markdown(f"**Tvůj nákup:** {nakup}")
                
                q1 = st.radio("1. Je to pro tebe objektivní POTŘEBA, nebo spíš PŘÁNÍ?", 
                              ["Je to potřeba (základ k fungování/přežití)", "Je to přání (chci to pro radost, status nebo zážitek)"], key="bnpl_1")
                
                q2 = st.radio("2. Koupil/a bys to teď, kdybys to musel/a zaplatit na dřevo v HOTOVOSTI?", 
                              ["Ano, peníze na to reálně mám už teď", "Ne, tolik peněz bych z peněženky prostě nedal/a (nebo je teď nemám)"], key="bnpl_2")
                
                q3 = st.radio("3. Co se stane, když ti výplata/brigáda za měsíc nepřijde nebo přijde nižší?", 
                              ["Mám železnou rezervu, doplatím to z ní", "Budu mít velký problém a nezbude mi na nájem/jídlo"], key="bnpl_3")

                if st.button("Vyhodnotit nákup", type="primary"):
                    if "potřeba" in q1.lower() and "Ano" in q2 and "rezervu" in q3:
                        st.success("✅ **Zelená:** Jde o promyšlený nákup. Máš rezervu a jde o potřebu. Odloženou platbu můžeš bezpečně využít jako nástroj pro cashflow.")
                    elif "přání" in q1.lower() and "Ne" in q2:
                        st.error("🚨 **Kritické varování:** Chceš si vzít dluh na něco, co nepotřebuješ, a maskuješ si to tím, že peníze neplatíš hned. Toto je definice dluhové pasti. Nákup zruš!")
                    elif "problém" in q3:
                        st.warning("⚠️ **Riziko:** Sice to možná zaplatíš, ale hraješ ruskou ruletu. Nemáš rezervu a spoléháš, že se příští měsíc nic nepokazí. Co když onemocníš? Raději počkej, až peníze reálně naspoříš.")
                    else:
                        st.info("💡 **Výsledek k zamyšlení:** Tvé odpovědi jsou na pomezí. Než klikneš na 'Koupit', dej si pravidlo 24 hodin. Vrať se k tomu zítra – často zjistíš, že už tu věc vlastně nechceš.")
# =========================================================================
    # 4.10 POJIŠTĚNÍ: OCHRANA PŘED FINANČNÍM NÁRAZEM
    # =========================================================================
    elif "4.10" in selected_section_2:
        st.markdown("<div class='sub-section-header'>10. ÚVĚRY A POJIŠTĚNÍ</div>", unsafe_allow_html=True)
        st.markdown("## 4.10 Pojištění: ochrana před finančním nárazem")
        
        st.write("Pojištění je nástroj, který pomáhá zvládnout finanční dopady nepříjemné události. Nezabrání tomu, aby se něco stalo (pojištění domu nezabrání požáru), ale může radikálně snížit finanční škodu, kterou to způsobí.")
        
        st.markdown("""
        <div class="box-green">
            <b>🛟 Pojištění jednoduše:</b> Mnoho lidí platí menší částky do společného systému. Když někoho z nich potká pojistná událost, pojišťovna mu podle smlouvy vyplatí peníze. Smyslem není „na pojištění vydělat“, ale ochránit se před škodou, která by zničila tvůj rozpočet.
        </div>
        """, unsafe_allow_html=True)
        
        st.write("Pojištění úzce souvisí i s úvěry. U hypotéky banka často vyžaduje pojištění nemovitosti, protože dům je pro ni zástava. U běžných úvěrů se nabízí tzv. pojištění schopnosti splácet. To může pomoci při nemoci nebo ztrátě příjmu, ale je nutné pečlivě číst podmínky a výluky.")

        st.divider()

        st.markdown("### 4.10.1 Proč si pojištění zřizujeme")
        st.write("Zlaté pravidlo zní: Pojištění má smysl hlavně tehdy, když by škoda byla pro tebe nebo tvou rodinu **finančně těžko zvládnutelná**.")
        
        st.markdown("""
        <div class="box-purple">
            <b>🧠 Dobrá otázka:</b> <i>Kdyby se tahle událost stala zítra, zvládnu ji zaplatit ze své úsporné rezervy?</i> Pokud ne, může dávat velký smysl se proti ní pojistit. Pokud ano (např. rozbitý displej u mobilu), pojištění bývá zbytečně drahé.
        </div>
        """, unsafe_allow_html=True)

        # --- AKTIVITA: SIMULÁTOR NÁRAZU ---
        st.markdown("### 💥 Aktivita: Simulátor finančního nárazu")
        st.write("Vyzkoušej si, jak by tvůj rozpočet ustál různé životní situace. Nastav si svou pomyslnou finanční rezervu a vyber událost.")

        with st.container(border=True):
            rezerva = st.slider("Jak velkou máš naspořenou rezervu na účtu?", 0, 500000, 50000, step=10000, format="%d Kč")
            
            udalost = st.selectbox("Co se ti právě stalo?", [
                "Vyber událost...",
                "Rozbil se mi displej u mobilu (Škoda: 4 000 Kč)",
                "Ukradli mi starší kolo z garáže (Škoda: 15 000 Kč)",
                "Vytopil jsem sousedy pod sebou (Škoda: 180 000 Kč)",
                "Měl jsem vážný úraz a rok nebudu pracovat (Ztráta: 400 000 Kč)",
                "Dům mi lehl popelem (Škoda: 6 000 000 Kč)"
            ])

            if udalost != "Vyber událost...":
                # Extrakce škody z textu
                skoda = int(udalost.split(":")[-1].replace(" Kč)", "").replace(" ", ""))
                zustatek = rezerva - skoda
                
                col1, col2 = st.columns(2)
                col1.metric("Tvoje rezerva", f"{rezerva:,} Kč".replace(",", " "))
                col2.metric("Finanční škoda", f"-{skoda:,} Kč".replace(",", " "))
                
                if zustatek >= 0:
                    st.success(f"✅ **Tohle zvládneš!** Po zaplacení škody ti zbude {zustatek:,} Kč. Tuto věc (pokud to není zákonná povinnost) nutně pojišťovat nemusíš, zvládneš to pokrýt z vlastních peněz.".replace(",", " "))
                else:
                    st.error(f"🚨 **Kritický náraz!** Tvá rezerva nestačí. Chybělo by ti {abs(zustatek):,} Kč. Dostal/a by ses do tvrdých dluhů nebo bys přišel/a o střechu nad hlavou. **Toto je přesně situace, kterou by mělo krýt pojištění.**".replace(",", " "))


    # =========================================================================
    # 4.11 ŽIVOTNÍ POJIŠTĚNÍ (+ 4.11.1)
    # =========================================================================
    elif "4.11" in selected_section_2:
        st.markdown("<div class='sub-section-header'>11. ÚVĚRY A POJIŠTĚNÍ</div>", unsafe_allow_html=True)
        st.markdown("## 4.11 Životní pojištění")
        
        st.write("Životní pojištění se vztahuje k životu, zdraví, pracovní schopnosti a tvému příjmu. **Nemá být automaticky bráno jako „spoření“.** Jeho hlavní smysl je ochrana před situací, která by měla vážný a dlouhodobý dopad na příjem tvé domácnosti.")

        st.markdown("### Co může životní pojištění krýt:")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.info("⚰️ Smrt pojištěného")
            st.info("♿ Invaliditu")
        with c2:
            st.info("🏥 Vážné onemocnění")
            st.info("🛌 Dlouhodobou pracovní neschopnost")
        with c3:
            st.info("🤕 Trvalé následky úrazu")
            st.info("🩹 Denní odškodné při nemoci/úrazu")

        st.markdown("""
        <div class="box-red">
            <b>⚠️ Pozor:</b> Životní pojištění není automaticky výhodná investice. Je obrovský rozdíl mezi <b>rizikovým</b> životním pojištěním (platíš čistě za ochranu) a <b>investičním</b> životním pojištěním (kombinuje pojištění a investování, často se skrytými poplatky a složitými podmínkami, což se většinou nevyplatí).
        </div>
        """, unsafe_allow_html=True)
        
        st.divider()

        # --- AKTIVITA: OSOBNÍ ANALYZÁTOR ---
        st.markdown("### 🧭 Analyzátor: Potřebuji životní pojištění?")
        st.write("Ne každý potřebuje platit tisíce měsíčně za životko. Odpověz na 3 otázky a zjisti svou situaci:")

        with st.container(border=True):
            a1 = st.checkbox("1. Živím někoho dalšího (děti, partner/ka na mateřské, závislý rodič).")
            a2 = st.checkbox("2. Mám hypotéku nebo jiný vysoký úvěr, který bych nedokázal/a splatit najednou.")
            a3 = st.checkbox("3. Kdybych zítra přišel/a o příjem, NEMÁM majetek nebo rezervu na přežití delší než 1 rok.")
            
            if st.button("Vyhodnotit mou situaci", type="primary"):
                skore = sum([a1, a2, a3])
                
                if skore == 0:
                    st.success("✅ **Spíše nepotřebuješ.** Nikoho neživíš, nemáš dluhy a máš rezervy. Pro tebe může dávat smysl maximálně základní pojištění trvalých následků úrazu, ale drahé komplexní životní pojištění by pro tebe teď byly vyhozené peníze.")
                elif skore == 1:
                    st.warning("⚠️ **Stojí za zvážení.** Máš alespoň jeden rizikový faktor. Ztráta tvé schopnosti pracovat by bolela, měl/a bys zvážit pokrytí těch nejvážnějších rizik (invalidita, vážné nemoci).")
                else:
                    st.error("🚨 **Kritická potřeba!** Tvá rodina nebo tvé bydlení je existenčně závislé na tom, že jsi zdravý/á a vyděláváš. Kvalitní životní pojištění kryjící invaliditu, smrt a dlouhodobý výpadek příjmu by pro tebe mělo být absolutní prioritou.")

        st.divider()

        # --- 4.11.1 POJIŠTĚNÍ SCHOPNOSTI SPLÁCET ---
        st.markdown("### 4.11.1 Pojištění schopnosti splácet")
        st.write("Toto pojištění se velmi často nabízí přímo v bance k úvěrům (hypotékám i spotřebitelským úvěrům). Může krýt pracovní neschopnost, invaliditu, ztrátu zaměstnání nebo smrt. Může pomoci, ale **rozhodně to není magický štít**.")

        st.write("Před podpisem je absolutně nutné ověřit následující (zda není lepší vyřešit to přes své vlastní životní pojištění):")
        st.markdown("- Co přesně pojištění kryje a jaké má výluky?")
        st.markdown("- Od kdy pojišťovna reálně plní? (Tzv. karenční doba – např. až po 60 dnech nemoci).")
        st.markdown("- Jak dlouho bude splátky hradit? (Někdy to je omezeno jen na 12 měsíců).")
        st.markdown("- Platí pojištění i pro OSVČ, nebo jen pro zaměstnance s trvalou smlouvou?")
        
        # --- AKTIVITA: DETEKTIV VÝLUK ---
        st.markdown("#### 🕵️‍♂️ Hra na detektiva: Najdi skrytý háček (Výluky)")
        st.write("Pojišťovny mají ve smlouvách tzv. **výluky** = situace, kdy ti nezaplatí ani korunu, i když jsi poctivě platil. Přečti si příběh a zkus uhodnout, proč pojišťovna peníze nedala.")

        tab_v1, tab_v2, tab_v3 = st.tabs(["Případ 1: Ztráta práce", "Případ 2: Bolest zad", "Případ 3: Úraz o víkendu"])
        
        with tab_v1:
            st.markdown("**Situace:** Tomáš si vzal úvěr s pojištěním proti ztrátě zaměstnání. Za měsíc ho vyhodili v rámci zkušební doby. Nahlásil to pojišťovně, ale ta mu splátky nezaplatila. Proč?")
            with st.expander("Zobrazit řešení"):
                st.error("❌ **Výluka:** Ztráta práce ve zkušební době, ukončení dohodou nebo výpověď pro hrubé porušení kázně jsou téměř vždy ve výlukách. Pojištění funguje většinou jen tehdy, pokud dostaneš výpověď pro nadbytečnost z klasické smlouvy.")
                
        with tab_v2:
            st.markdown("**Situace:** Jana má pojištění dlouhodobé pracovní neschopnosti. Už třetí měsíc je doma s těžkými bolestmi zad (chronické problémy s páteří). Pojišťovna plnění zamítla. Proč?")
            with st.expander("Zobrazit řešení"):
                st.error("❌ **Výluka:** Bolesti zad a psychická onemocnění (vyhoření, deprese) bývají u mnoha pojišťoven vyloučeny, nebo je jejich plnění silně omezeno, protože se těžko objektivně prokazují.")
                
        with tab_v3:
            st.markdown("**Situace:** Martin si při amatérském adrenalinovém závodě na horských kolech (downhill) zlomil obě nohy. Pojišťovna mu úrazové plnění krátila o 50 %. Proč?")
            with st.expander("Zobrazit řešení"):
                st.error("❌ **Výluka:** Extrémní a rizikové sporty vyžadují speciální připojištění. Běžná pojistka tě kryje při rekreačním sportu, ale ne při závodech s vysokým rizikem zranění. Pojišťovna může plnění také krátit, pokud byl v krvi alkohol.")
# =========================================================================
    # 4.12 NEŽIVOTNÍ POJIŠTĚNÍ
    # =========================================================================
    elif "4.12" in selected_section_2:
        st.markdown("<div class='sub-section-header'>12. ÚVĚRY A POJIŠTĚNÍ</div>", unsafe_allow_html=True)
        st.markdown("## 4.12 Neživotní pojištění")
        
        st.write("Zatímco životní pojištění chrání tebe a tvé tělo, neživotní pojištění se týká tvého majetku, odpovědnosti a konkrétních rizik. Chrání tě před škodami, které by ti jinak udělaly obří díru do rozpočtu.")

        st.markdown("### Co sem patří?")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info("🏠 Pojištění nemovitosti\n\n🛋️ Pojištění domácnosti\n\n🛡️ Pojištění odpovědnosti")
        with col2:
            st.info("🚗 Povinné ručení (auto)\n\n🚙 Havarijní pojištění\n\n✈️ Cestovní pojištění")
        with col3:
            st.info("🤕 Úrazové pojištění\n\n🏭 Pojištění podnikání\n\n📦 Pojištění strojů a zásob")

        st.divider()

        # --- 4.12.1 NEMOVITOST VS DOMÁCNOST ---
        st.markdown("### 4.12.1 Pojištění nemovitosti vs. domácnosti")
        st.write("Tyto dva pojmy se lidem neustále pletou. Přitom je rozdíl naprosto zásadní!")
        
        st.markdown("""
        <div class="box-blue">
            <b>💡 Trik, jak si to zapamatovat:</b> Představ si, že bys vzal svůj dům nebo byt, obrátil ho vzhůru nohama a pořádně s ním zatřásl. Všechno, co spadne na strop (nábytek, televize, oblečení, ty), je <b>DOMÁCNOST</b>. Všechno, co zůstane pevně držet (zdi, střecha, trubky, vana, podlaha), je <b>NEMOVITOST</b>.
        </div>
        """, unsafe_allow_html=True)
        
        st.write("U hypotéky banka vždy požaduje pojištění **nemovitosti**. Kdyby dům vyhořel, ztratila by totiž svou zástavu.")

        # HRA: CO JE CO?
        with st.container(border=True):
            st.markdown("#### 🧩 Kvíz: Roztřiď majetek")
            
            c_q1, c_q2 = st.columns(2)
            with c_q1:
                ans1 = st.selectbox("Vestavěná kuchyňská linka na míru:", ["Vyber...", "Nemovitost", "Domácnost"])
                ans2 = st.selectbox("Notebook a herní konzole:", ["Vyber...", "Nemovitost", "Domácnost"])
            with c_q2:
                ans3 = st.selectbox("Radiátory a kotel:", ["Vyber...", "Nemovitost", "Domácnost"])
                ans4 = st.selectbox("Drahý koberec a sedací souprava:", ["Vyber...", "Nemovitost", "Domácnost"])
                
            if st.button("Zkontrolovat", type="primary"):
                if "Vyber..." in [ans1, ans2, ans3, ans4]:
                    st.warning("Vyber všechny odpovědi!")
                elif ans1 == "Nemovitost" and ans2 == "Domácnost" and ans3 == "Nemovitost" and ans4 == "Domácnost":
                    st.success("✅ Skvěle! Pochopil/a jsi to naprosto přesně. Vestavěné a pevné věci = nemovitost. Volné věci = domácnost.")
                else:
                    st.error("❌ Někde je chyba. Vzpomeň si na trik s třesením domu!")

        st.divider()

        # --- 4.12.2 POJIŠTĚNÍ ODPOVĚDNOSTI ---
        st.markdown("### 4.12.2 Pojištění odpovědnosti (tzv. pojistka na blbost)")
        st.write("Chrání tě před škodou, kterou **ty (nebo tvé dítě/pes)** způsobíš někomu jinému. Může jít o škodu na zdraví, na majetku, nebo o finanční škodu.")
        
        st.markdown("""
        <div class="box-purple">
            <b>🛡️ Proč je odpovědnost často důležitější než pojištění majetku:</b> Pokud ti ukradnou starší auto, přijdeš třeba o 100 000 Kč. To bolí, ale nezničí tě to. Pokud ale na lyžích srazíš manažera, který bude mít trvalé následky a ušlý zisk, soud ti může nařídit platit miliony. Pojištění odpovědnosti tě chrání před tím, abys cizí škodu platil do konce života ze svého platu.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("**Typické příklady, kdy tě to zachrání:**")
        st.markdown("- Vytopíš souseda pod sebou prasklou hadičkou od pračky.")
        st.markdown("- Tvé dítě v obchodě shodí regál s drahou elektronikou.")
        st.markdown("- Tvůj pes vběhne pod auto a způsobí nehodu.")
        st.markdown("- Na kole nebo koloběžce srazíš chodce.")


    # =========================================================================
    # 4.13 JAK POZNAT DOBRÉ POJIŠTĚNÍ
    # =========================================================================
    elif "4.13" in selected_section_2:
        st.markdown("<div class='sub-section-header'>13. ÚVĚRY A POJIŠTĚNÍ</div>", unsafe_allow_html=True)
        st.markdown("## 4.13 Jak poznat dobré pojištění")
        
        st.write("U pojištění nestačí sledovat jen cenu. Levná pojistka je často k ničemu, protože má nízké limity nebo spoustu výluk (situací, kdy neplatí).")
        
        st.markdown("### 🔍 Na co si dát pozor ve smlouvě:")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("- **Pojistné limity:** Maximální částka, kterou ti pojišťovna dá.")
            st.markdown("- **Spoluúčast:** Částka, kterou platíš ze svého (např. prvních 5 000 Kč škody platíš ty).")
            st.markdown("- **Výluky:** Seznam výjimek (např. neplatí při alkoholu v krvi).")
            st.markdown("- **Čekací doby:** Kdy pojištění začne reálně platit.")
        with c2:
            st.markdown("- **Způsob výpočtu:** Dostaneš novou cenu věci, nebo jen tu aktuální, opotřebenou?")
            st.markdown("- **Zda řeší tvá rizika:** Pojištění lyží u moře ti nepomůže.")
            st.markdown("- **Co není pojištěno:** Někdy chybí základní věci jako povodeň.")

        st.divider()

        # --- SIMULÁTOR PODPOJIŠTĚNÍ ---
        st.markdown("### ⚠️ Neviditelný zabiják: Podpojištění")
        st.write("Podpojištění vzniká, když je tvůj majetek pojištěn na mnohem **nižší částku, než je jeho skutečná dnešní hodnota** (typicky kvůli inflaci u domů). Pokud se to stane, pojišťovna ti při škodě **krátí plnění**, a to i u malých škod!")

        with st.container(border=True):
            st.markdown("#### 🧮 Simulátor tvrdé reality")
            st.write("Představ si, že jsi před 10 lety koupil dům a pojistil ho na tehdejší cenu. Dnes má dům dvojnásobnou hodnotu, ale pojistku jsi neaktualizoval. Vichřice ti strhne část střechy (škoda za 500 000 Kč).")
            
            pojistna_castka = st.slider("Na kolik je dům papírově pojištěn (Smlouva):", 2000000, 10000000, 3000000, step=500000)
            skutecna_hodnota = st.slider("Jakou má dům skutečnou hodnotu dnes:", 2000000, 15000000, 6000000, step=500000)
            skoda = 500000
            
            # Výpočet plnění (vzorec podpojištění)
            if pojistna_castka < skutecna_hodnota:
                koeficient = pojistna_castka / skutecna_hodnota
                vyplaceno = skoda * koeficient
                doplatis_sam = skoda - vyplaceno
                
                col_a, col_b, col_c = st.columns(3)
                col_a.metric("Škoda na střeše", f"{skoda:,} Kč".replace(",", " "))
                col_b.metric("Pojišťovna zaplatí", f"{int(vyplaceno):,} Kč".replace(",", " "), delta="Kráceno kvůli podpojištění!", delta_color="inverse")
                col_c.metric("Musíš doplatit ze svého", f"{int(doplatis_sam):,} Kč".replace(",", " "), delta="To bolí", delta_color="inverse")
                
                st.error(f"🚨 **Banka/Pojišťovna tě nachytala na matematice!** Protože jsi měl dům pojištěný jen na {int(koeficient*100)} % jeho reálné hodnoty, pojišťovna ti i z blbé škody na střeše vyplatí pouze {int(koeficient*100)} %! Zbytek musíš zaplatit ze svého.")
            
            else:
                col_a, col_b = st.columns(2)
                col_a.metric("Škoda na střeše", f"{skoda:,} Kč".replace(",", " "))
                col_b.metric("Pojišťovna zaplatí", f"{skoda:,} Kč".replace(",", " "))
                st.success("✅ **Vše v pořádku.** Pojistná částka odpovídá reálné hodnotě domu. Pojišťovna zaplatí celou škodu na střeše (mínus případná spoluúčast).")
# =========================================================================
    # 4.14 PRAKTICKÉ ROZHODNŮVÁNÍ: ÚVĚR A POJIŠTĚNÍ DOHROMADY
    # =========================================================================
    elif "4.14" in selected_section_2:
        st.markdown("<div class='sub-section-header'>14. ÚVĚRY A POJIŠTĚNÍ</div>", unsafe_allow_html=True)
        st.markdown("## 4.14 Praktické rozhodování: úvěr a pojištění dohromady")
        
        st.write("Úvěry a pojištění spolu neoddělitelně souvisí. Čím větší finanční závazek na sobě máš, tím více musíš řešit, co se stane při výpadku příjmu, nemoci, požáru nebo jiné životní krizi.")

        with st.container(border=True):
            st.markdown("### 👨‍👩‍👧‍👦 Modelový příklad z praxe:")
            st.write("- **Situace:** Rodina si vzala hypotéku na dům 4 000 000 Kč. Mají jedno malé dítě.")
            st.write("- **Příjem:** Rodina spoléhá převážně na jeden hlavní příjem otce (45 000 Kč), matka je na rodičovské (10 000 Kč).")
            st.write("- **Závazek:** Měsíční splátka hypotéky činí 22 000 Kč. Dům je zastaven bance.")
            st.warning("⚠️ **Riziko:** Pokud hlavní živitel dlouhodobě onemocní nebo utrpí úraz, rodina do 2 měsíců nedokáže platit splátku a hrozí jí ztráta střechy nad hlavou!")
            st.success("💡 **Řešení:** Vhodná kombinace: 1) Životní pojištění živitele (kryjící invaliditu a smrt), 2) Pojištění nemovitosti (zástava pro banku), 3) Finanční rezerva ve výši 6 splátek na spořicím účtu.")

        st.divider()

        # --- SIMULACE 1: BANKÉŘEM NA ZKOUŠKU ---
        st.markdown("### 🧪 Finanční simulace: Dostane žadatel úvěr?")
        st.write("Vžij se do role bankovního risk manažera. Vyber si profil žadatele, posuď jeho situaci a rozhodni, zda mu půjčíš!")

        profil = st.selectbox("Vyber profil žadatele o úvěr:", [
            "Vyber žadatele...",
            "Žadatel A: Petr (22 let) – První auto na úvěr (150 000 Kč)",
            "Žadatelka B: Eva a Martin (30 let) – Hypotéka na byt (5 000 000 Kč)",
            "Žadatel C: Pavel (35 let) – Spotřebitelský úvěr na dovolenou (60 000 Kč)"
        ])

        if profil.startswith("Žadatel A"):
            with st.container(border=True):
                st.markdown("#### 📋 Profil: Petr (22 let)")
                st.markdown("- **Požadavek:** 150 000 Kč na auto")
                st.markdown("- **Čistý příjem:** 24 000 Kč/měsíc (pracuje 4 měsíce, po zkušební době)")
                st.markdown("- **Výdaje a nájem:** 14 000 Kč/měsíc")
                st.markdown("- **Stávající dluhy:** Žádné")
                st.markdown("- **Vlastní úspory:** 5 000 Kč")
                
                sim_a1 = st.radio("1. Jak vyhodnotíš bonitu a schválení?", ["Schválit v plné výši", "Zamítnout nebo nabídnout nižší částku", "Schválit 100% částku bez doložení"], key="sim_a1")
                sim_a2 = st.radio("2. Jaké je pro Petra největší riziko?", ["Pokles ceny auta", "Ztráta práce / nemoc bez finanční rezervy", "Zvýšení úrokových sazeb u hypotéky"], key="sim_a2")
                
                if st.button("Vyhodnotit jako banka"):
                    if "Zamítnout" in sim_a1 and "Ztráta práce" in sim_a2:
                        st.success("✅ **Správně!** Petr má extrémně nízkou rezervu (jen 5 000 Kč). Měsíčně mu po výdajích zbývá 10 000 Kč, ze kterých by splátka auta vzala většinu. Banka mu buď nabídne nižší částku, nebo doporučí nejdříve naspořit rezervu.")
                    else:
                        st.error("❌ **Chybně.** Jako bankéř bys riskoval/a. Petr nemá téměř žádné úspory a v případě nemoci by hned v prvním měsíci spadl do nesplácení.")

        elif profil.startswith("Žadatelka B"):
            with st.container(border=True):
                st.markdown("#### 📋 Profil: Eva a Martin (30 let)")
                st.markdown("- **Požadavek:** Hypotéka 4 500 000 Kč na byt v hodnotě 5 000 000 Kč (LTV 90 %)")
                st.markdown("- **Čistý příjem:** Společně 65 000 Kč/měsíc (smlouvy na neurčito)")
                st.markdown("- **Výdaje:** 25 000 Kč/měsíc")
                st.markdown("- **Vlastní úspory:** 600 000 Kč")
                
                sim_b1 = st.radio("1. Kolik vlastních peněz musí dát ze svého?", ["Alespoň 10–20 % (tj. min. 500 000 Kč)", "Nemusí dát nic, banka půjčí 100 %", "Musí mít naspořeno 50 %"], key="sim_b1")
                sim_b2 = st.radio("2. Jaké pojištění by měli absolutně prioritně sjednat?", ["Pojištění displeje mobilu", "Pojištění nemovitosti + Životní pojištění pro případ invalidity/smrti", "Havarijní pojištění auta"], key="sim_b2")
                
                if st.button("Vyhodnotit jako banka"):
                    if "10–20 %" in sim_b1 and "Pojištění nemovitosti" in sim_b2:
                        st.success("✅ **Výborně!** Žadatelé mají dostatečný příjem i vlastní úspory na LTV 90 %. Pojištění nemovitosti bude vyžadovat sama banka jako zástavu a životní pojištění ochrání jejich společný rozpočet.")
                    else:
                        st.error("❌ **Chyba v posouzení.** U hypotéky je nutný vlastní základ a krytí životních rizik při takto velkém dluhu.")

        elif profil.startswith("Žadatel C"):
            with st.container(border=True):
                st.markdown("#### 📋 Profil: Pavel (35 let)")
                st.markdown("- **Požadavek:** 60 000 Kč na luxusní dovolenou v Karibiku")
                st.markdown("- **Čistý příjem:** 32 000 Kč/měsíc")
                st.markdown("- **Stávající dluhy:** Splácí už kontokorent (20 000 Kč) a kreditku (30 000 Kč)")
                
                if st.button("Vyhodnotit jako banka"):
                    st.error("🚨 **ZAMÍTNUTO!** Pavel vykazuje jasné známky předlužení (kumuluje spotřebitelské dluhy) a chce si půjčit na zážitek/spotřebu, která nemá žádnou trvalou hodnotu. Banka úvěr zamítne z důvodu ochrany spotřebitele i vysokého rizika dlužníka.")

        st.divider()

        # --- AKTIVITA 2: SROVNÁVAČ DVE PŮJČEK ---
        st.markdown("### 🧾 Aktivita: Porovnej dvě nabídky půjčky")
        st.write("Potřebuješ si půjčit **50 000 Kč** na nový notebook do školy/práce se splatností na **2 roky (24 měsíců)**. Prohlédni si dvě nabídky:")

        col_n1, col_n2 = st.columns(2)
        with col_n1:
            st.info("""
            **Nabídka A (Tradiční banka)**
            * **Úroková sazba:** 6,9 % p. a.
            * **RPSN:** 7,2 %
            * **Měsíční splátka:** 2 236 Kč
            * **Poplatek za sjednání:** 0 Kč
            * **Pojištění:** Volitelné (100 Kč/měs)
            * **Celkem zaplatíš:** ~53 664 Kč
            """)
        with col_n2:
            st.error("""
            **Nabídka B (Rychlá nebankovní půjčka)**
            * **Úroková sazba:** 4,9 % p. a. *(Lákavá reklama!)*
            * **RPSN:** 28,5 %
            * **Měsíční splátka:** 2 720 Kč
            * **Poplatek za sjednání:** 3 500 Kč
            * **Správa úvěru:** 150 Kč / měsíčně
            * **Celkem zaplatíš:** ~65 280 Kč
            """)

        rozhodnuti = st.radio("Kterou možnost bysis vybral/a?", [
            "Vyber možnost...",
            "Zvolil/a bych Nabídku A",
            "Zvolil/a bych Nabídku B (má přece nižší úrok 4,9 %!)",
            "Nepůjčil/a bych si vůbec – našetřil/a bych nebo koupil/a levnější repasovaný notebook"
        ])

        if rozhodnuti == "Zvolil/a bych Nabídku A":
            st.success("✅ **Dobrá volba spotřebitele:** Nabídka A má sice o něco vyšší udávaný úrok, ale díky nízkému RPSN a absenci skrytých poplatků tě celkově stojí o 11 616 Kč MÉNĚ než Nabídka B.")
        elif rozhodnuti == "Zvolil/a bych Nabídku B (má přece nižší úrok 4,9 %!)":
            st.error("❌ **Skočil/a jsi na marketingový trik!** Nízký úrok 4,9 % je jen návnada. Kvůli obřím poplatkům za sjednání a vedení účtu je RPSN celých 28,5 % a přeplatíš o více než 11 tisíc korun navíc!")
        elif "Nepůjčil/a bych si vůbec" in rozhodnuti:
            st.success("🏆 **Nejlepší finanční rozhodnutí!** Na věci běžné spotřeby nebo elektroniku je vždy nejbezpečnější si našetřit z vlastních zdrojů nebo zvolit dostupnější alternativu bez zadlužování.")


    # =========================================================================
    # 4.15 SHRNUTÍ: CO SI ODNÉST
    # =========================================================================
    elif "4.15" in selected_section_2:
        st.markdown("<div class='sub-section-header'>15. ÚVĚRY A POJIŠTĚNÍ</div>", unsafe_allow_html=True)
        st.markdown("## 4.15 Shrnutí kapitoly: Co si odnést")
        
        st.write("Gratulujeme! Prošel/prošla jsi celou kapitolu o úvěrech, hypotékách a pojištění. Zde jsou nejdůležitější pravidla pro tvůj finanční život:")

        st.markdown("""
        <div class="box-green">
            <h3>✅ Klíčová pravidla pro život:</h3>
            <ul>
                <li><b>Úvěr není peníze navíc:</b> Je to jen přesun tvé budoucí spotřeby do přítomnosti, za který vždy zaplatíš úrokem a časem.</li>
                <li><b>RPSN je tvůj nejlepší přítel:</b> Samotný úrok nestačí. Vždy porovnávej <b>RPSN</b> a <b>celkovou zaplacenou částku</b>.</li>
                <li><b>Dostatečná rezerva:</b> Splátka úvěru musí být nastavena tak, abys dokázal/a žít a tvořit si rezervu i při výpadku příjmu.</li>
                <li><b>Hypotéka vyžaduje přípravu:</b> Bez vlastních úspor (10–20 % LTV) a dobré platební historie ti banka na bydlení nepůjčí.</li>
                <li><b>Pozor na impulzivní dlužení:</b> Služby typu <i>BNPL (Kup teď, zaplať později)</i> nebo kontokorenty odbourávají pocit z placení a vedou do dluhové pasti.</li>
                <li><b>Pojištění chrání před katastrofou:</b> Pojišťuj věci, které by zničily tvůj rozpočet (invalidita, ztráta domu, obří škoda třetí osobě). Drobnosti zvládni z vlastní rezervy.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.divider()

        # --- AI MENTORING BOX ---
        st.markdown("### 🤖 Vyzkoušej AI Mentora")
        st.write("Chceš si téma ještě lépe upevnit nebo se zeptat na cokoliv, co ti nebylo jasné? Zkopíruj tento text a vlož ho do svého oblíbeného AI asistenta:")

        prompt_text = "Vysvětli mi rozdíl mezi úrokem a RPSN na jednoduchém příkladu půjčky. Potom mi ukaž, jak banka posuzuje, jestli člověk dostane spotřebitelský úvěr nebo hypotéku."
        
        st.code(prompt_text, language="text")
        st.caption("💡 Tip: Můžeš AI požádat, aby ti položila 3 kontrolní otázky z této kapitoly!")
# =========================================================================
    # 5.1 PROČ PODNIK ŘEŠÍ FINANCE
    # =========================================================================
    elif selected_section_2.startswith("5.1 "):
        st.markdown("<div class='sub-section-header'>5. FINANČNÍ ŘÍZENÍ V PODNIKU</div>", unsafe_allow_html=True)
        st.markdown("## 5.1 Proč podnik řeší finance")
        
        st.write(
            "Finanční řízení podniku není jen práce účetní nebo „něco pro majitele firmy“. Je to způsob, jak firma zjišťuje, "
            "jestli dokáže přežít, růst, platit své závazky, zvládat rizika a dělat rozhodnutí podle dat místo pouhých pocitů."
        )
        st.write(
            "Pro dnešní generaci je to důležité i proto, že podnikání už nemusí vypadat jako obří továrna nebo kancelářský komplex. "
            "Firma může být **e-shop z pokoje, freelance tvorba grafiky, streamovací kanál, kosmetické studio, food truck, vývoj aplikace, "
            "školní projekt nebo profil influencera.** V každém případě ale platí stejná základní otázka: *přichází do podnikání víc hodnoty, než z něj odchází?*"
        )

        st.markdown("""
        <div class="box-blue">
            <b>📊 Základní myšlenka:</b> Finanční řízení pomáhá odpovědět na otázky: Kolik firma vydělává? Kolik skutečně utrácí? Má peníze na účtu? Zvládne splácet? Vyplatí se růst? Není příliš zadlužená? A pozná včas, že se blíží průšvih?
        </div>
        """, unsafe_allow_html=True)

        st.divider()

        st.markdown("### ⚠️ Paradox: Skvělý produkt ≠ Úspěšná firma")
        st.write("Firma může mít skvělý produkt, tisíce sledujících, hezký web a plný kalendář zakázek — a přesto může mít obří finanční problém. Důvod je jednoduchý: **popularita není totéž co zisk a zisk není totéž co peníze na účtu.**")

        # Interaktivní demo: Paradox ziskovosti
        with st.container(border=True):
            st.markdown("#### 🧪 Mini-simulátor: Proč zkrachoval úspěšný Food Truck?")
            st.write("Představ si food truck prodávající prémiové burgery. Místní ho milují, fronta je až za roh!")
            
            prodejni_cena = st.slider("Prodejní cena burgeru (Kč):", 100, 300, 180, step=10)
            naklady_suroviny = 110 # Suroviny
            ostatni_naklady_na_burger = 80 # Mzdy, nájem auta, elektřina rozpočtená na 1 ks
            
            celkove_naklady = naklady_suroviny + ostatni_naklady_na_burger
            zisk_na_kus = prodejni_cena - celkove_naklady

            col_sim1, col_sim2 = st.columns(2)
            col_sim1.metric("Celkové náklady na 1 burger", f"{celkove_naklady} Kč")
            
            if zisk_na_kus < 0:
                col_sim2.metric("Zisk / Ztráta na 1 burger", f"{zisk_na_kus} Kč", delta="Kráčíš ke krachu!", delta_color="inverse")
                st.error(f"🚨 **Katastrofa!** I když prodáš 10 000 burgerů měsíčně a všichni tě chválí, na každém burgeru proděláváš {abs(zisk_na_kus)} Kč. Čím více prodáváš, tím větší díru do rozpočtu děláš!")
            else:
                col_sim2.metric("Zisk / Ztráta na 1 burger", f"{zisk_na_kus} Kč", delta="Firma generuje zisk", delta_color="normal")
                st.success(f"✅ **Super!** Na každém burgeru vyděláš {zisk_na_kus} Kč. Pokud ti zákazníci zaplatí včas, firma se udrží v zisku.")

        st.markdown("""
        <div class="box-green">
            <b>🧠 Pointa pro studenty:</b> Finanční řízení není o tom „být posedlý penězi“. Je o odpovědnosti. Pokud firma neumí řídit finance, může ohrozit nejen majitele, ale i zaměstnance, zákazníky, dodavatele a další lidi, kteří jsou na jejím fungování závislí.
        </div>
        """, unsafe_allow_html=True)

        st.divider()

        # =========================================================================
        # 5.1.1 KOHO ZAJÍMÁ FINANČNÍ ZDRAVÍ PODNIKU
        # =========================================================================
        st.markdown("### 5.1.1 Koho zajímá finanční zdraví podniku")
        st.write("Finanční zdraví neřeší jen majitel. Zajímá mnoho skupin v okolí firmy (tzv. *stakeholderů*), protože každá z nich nese jiné riziko a pokládá si jiné otázky.")

        st.markdown("#### 👥 Proklikni si optiku jednotlivých aktérů:")

        # Interaktivní výběr stakeholderů
        aktéri = {
            "👑 Majitelé a společníci": {
                "důvod": "Chtějí vědět, zda firma vydělává, roste a neztrácí hodnotu.",
                "otázka": "„Vyplatí se v tomto podnikání pokračovat, nebo peníze raději vytáhnout?“",
                "riziko": "Ztráta vloženého kapitálu a času."
            },
            "👔 Management": {
                "důvod": "Potřebuje řídit ceny, náklady, investice, zásoby a lidi na denní bázi.",
                "otázka": "„Kde přesně nám utíkají peníze a co musíme od příštího měsíce změnit?“",
                "riziko": "Špatná rozhodnutí a ztráta konkurenceschopnosti."
            },
            "👷 Zaměstnanci": {
                "důvod": "Zajímá je stabilita práce, pravidelné výplaty a budoucnost firmy.",
                "otázka": "„Bude mít firma příští měsíc na mé mzdy, nebo si mám hledat novou práci?“",
                "riziko": "Ztráta zaměstnání a neproplacené mzdy."
            },
            "🏦 Banka": {
                "důvod": "Posuzuje, zda firma zvládne bezpečně splácet úvěr i s úroky.",
                "otázka": "„Má firma dostatečně stabilní cashflow na měsíční splátky?“",
                "riziko": "Nesplacení půjčky a vznik nespláceného dluhu."
            },
            "🚀 Investor": {
                "důvod": "Hledá potenciál rychlého růstu, vysokou návratnost a míru rizika.",
                "otázka": "„Má tato firma šanci desetinásobně vyrůst a ovládnout trh?“",
                "riziko": "Investice do podniku, který zkrachuje."
            },
            "🚚 Dodavatelé": {
                "důvod": "Řeší, jestli firma zaplatí vystavené faktury včas a v plné výši.",
                "otázka": "„Není riziko dodávat jim zboží na fakturu se splatností 30 dní?“",
                "riziko": "Druhotná platební neschopnost (nedostanou zaplaceno za své zboží)."
            },
            "🛒 Zákazníci": {
                "důvod": "U dlouhodobých služeb a záruk potřebují jistotu, že firma ze dne na den nezmizí.",
                "otázka": "„Bude tato služba nebo garance fungovat i za rok?“",
                "riziko": "Ztráta zaplacené zálohy nebo nefunkční záruka."
            },
            "🏛️ Stát a Obec": {
                "důvod": "Zajímá je řádné placení daní, pojistného, tvorba pracovních míst a rozvoj regionu.",
                "otázka": "„Plní firma své zákonné povinnosti a podporuje lokální ekonomiku?“",
                "riziko": "Daňové úniky nebo růst nezaměstnanosti v regionu."
            }
        }

        vybrany_akter = st.selectbox("Vyber skupinu, jejíž pohled tě zajímá:", list(aktéri.keys()))

        if vybrany_akter:
            data = aktéri[vybrany_akter]
            with st.container(border=True):
                st.markdown(f"### {vybrany_akter}")
                st.write(f"**Proč je to zajímá:** {data['důvod']}")
                st.info(f"❓ **Typická otázka:** {data['otázka']}")
                st.warning(f"⚠️ **Největší riziko pro ně:** {data['riziko']}")

        st.divider()

        # --- AKTIVITA PODKAPITOLY ---
        st.markdown("### 🧩 Aktivita: Domino efekt v tvém okolí")
        st.write("Vyber si libovolnou firmu z okolí své školy nebo bydliště (např. lokální kavárnu, autoservis, e-shop nebo tělocvičnu) a zkus se zamyslet nad řetězovou reakcí.")

        with st.container(border=True):
            st.text_input("Napiš název/typ vybrané firmy z okolí:", placeholder="Např. Kavárna U Školáka / Lokální autoservis Procházka")
            st.text_area("Co všechno by se stalo a kdo by utrpěl škodu, kdyby tato firma přestala ze dne na den platit své závazky?", 
                         placeholder="Např. Zaměstnanci by nedostali výplatu a nemohli zaplatit nájem. Dodavatel kávy by přišel o velkého odběratele...")
            
            if st.button("Uložit mé zamyšlení", type="primary"):
                st.success("✅ Skvělá úvaha! Takhle funguje ekonomický ekosystém. Finanční problém jedné firmy se jako domino šíří k desítkám dalších lidí.")
# =========================================================================
    # 5.2 ZÁKLADNÍ FINANČNÍ VÝKAZY: MAPA FIRMY V ČÍSLECH
    # =========================================================================
    elif selected_section_2.startswith("5.2 "):
        st.markdown("<div class='sub-section-header'>5. FINANČNÍ ŘÍZENÍ V PODNIKU</div>", unsafe_allow_html=True)
        st.markdown("## 5.2 Základní finanční výkazy: mapa firmy v číslech")
        
        st.write(
            "Aby šlo firmu bezpečně řídit, nestačí říct „daří se nám“ nebo „nějak to funguje“. Firma potřebuje přesná čísla. "
            "Základní finanční výkazy fungují jako palubní deska v autě — ukazují, co firma vlastní, co dluží, kolik vydělala, kolik utratila a jak se pohybovaly peníze."
        )

        st.markdown("""
        <div class="box-blue">
            <b>🧭 Jednoduché přirovnání:</b><br>
            📸 <b>Rozvaha</b> je <i>fotografie</i> firmy k určitému dni (statický stav majetku a dluhů).<br>
            🎬 <b>Výkaz zisku a ztráty</b> je <i>film</i> za určité období (jak hospodařila od 1. 1. do 31. 12.).<br>
            💧 <b>Cashflow</b> ukazuje, kudy reálně tekly peníze v peněžence/na účtu.
        </div>
        """, unsafe_allow_html=True)

        st.divider()

        # -------------------------------------------------------------------------
        # 5.2.1 ROZVAHA: CO FIRMA MÁ A Z ČEHO TO FINANCUJE
        # -------------------------------------------------------------------------
        st.markdown("### 5.2.1 Rozvaha: co firma má a z čeho to financuje")
        st.write(
            "Rozvaha ukazuje majetek firmy (**Aktiva**) a současně zdroje, ze kterých je tento majetek financovaný (**Pasiva**). "
            "V rozvaze musí vždy platit základní rovnováha:"
        )

        st.markdown("""
        <div class="box-purple" style="text-align: center; font-size: 1.2em;">
            <b>AKTIVA (Majetek) = PASIVA (Zdroje financování)</b><br>
            <small><i>Majetek firmy = Vlastní kapitál + Cizí zdroje (úvěry, dluhy)</i></small>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("#### ⚖️ Interaktivní balancér rozvahy studentského e-shopu")
        st.write("Sestav rozvahu pro e-shop. Vyzkoušej si, jak každé pořízení majetku musí mít svůj finanční zdroj!")

        with st.container(border=True):
            col_a, col_p = st.columns(2)
            
            with col_a:
                st.markdown("#### 📦 AKTIVA (Co firma má)")
                penize = st.number_input("Peníze na účtu a v pokladně (Kč):", value=25000, step=5000, key="act_penize")
                zasoby = st.number_input("Zásoby zboží na skladě (Kč):", value=30000, step=5000, key="act_zasoby")
                vybaveni = st.number_input("Notebook a balicí technika (Kč):", value=15000, step=5000, key="act_vyb")
                aktiva_celkem = penize + zasoby + vybaveni
                st.metric("Aktiva Celkem", f"{aktiva_celkem:,} Kč".replace(",", " "))

            with col_p:
                st.markdown("#### 💳 PASIVA (Z čeho to zaplatila)")
                vklad = st.number_input("Vlastní vklad majitele (Kč):", value=40000, step=5000, key="pas_vklad")
                uver = st.number_input("Bankovní úvěr (Kč):", value=20000, step=5000, key="pas_uver")
                zavazky = st.number_input("Nezaplacené faktury dodavatelům (Kč):", value=10000, step=5000, key="pas_zavazky")
                pasiva_celkem = vklad + uver + zavazky
                st.metric("Pasiva Celkem", f"{pasiva_celkem:,} Kč".replace(",", " "))

            # Vyhodnocení bilanční rovnováhy
            diference = aktiva_celkem - pasiva_celkem
            if diference == 0:
                st.success("✅ **Rozvaha je v rovnováze! (Aktiva = Pasiva)** E-shop má majetek za 70 000 Kč. Část financoval majitel ze svého, část úvěrem a část tím, že ještě nezaplatil dodavatelům.")
            elif diference > 0:
                st.error(f"❌ **Rozvaha nevychází!** Máš o {diference:,} Kč více majetku (Aktiva) než zdrojů (Pasiva). Kde jsi vzal/a peníze na tento majetek?".replace(",", " "))
            else:
                st.error(f"❌ **Rozvaha nevychází!** Zdroje (Pasiva) přesahují majetek o {abs(diference):,} Kč. Kde jsou ty peníze?".replace(",", " "))

        st.divider()

        # -------------------------------------------------------------------------
        # 5.2.2 VÝKAZ ZISKU A ZTRÁTY: VYDĚLÁVÁ FIRMA?
        # -------------------------------------------------------------------------
        st.markdown("### 5.2.2 Výkaz zisku a ztráty: vydělává firma?")
        st.write(
            "Výkaz zisku a ztráty (tzv. *Výsledovka*) ukazuje výnosy, náklady a výsledek hospodaření za dané období (např. za měsíc nebo rok)."
        )

        st.markdown("""
        <div class="box-green">
            <b>Základní logika výsledovky:</b><br>
            <b>Výnosy − Náklady = Výsledek hospodaření</b><br>
            • Výnosy > Náklady ➔ <b>ZISK</b> (Firma vydělala více, než spotřebovala)<br>
            • Náklady > Výnosy ➔ <b>ZTRÁTA</b> (Firma spotřebovala více, než vydělala)
        </div>
        """, unsafe_allow_html=True)

        st.markdown("#### 📊 Výsledovka e-shopu v praxi")
        st.write("Vyzkoušej si změnit tržby nebo náklady a sleduj, jak se mění Hrubý zisk a Zisk před zdaněním.")

        with st.container(border=True):
            col_v1, col_v2 = st.columns(2)
            with col_v1:
                trzby = st.slider("Tržby za prodej zboží (Výnosy):", 10000, 200000, 80000, step=5000, key="vys_trzby")
                naklady_zbozi = st.slider("Nákupní cena prodaného zboží:", 5000, 100000, 42000, step=2000, key="vys_zbozi")
            
            hruby_zisk = trzby - naklady_zbozi

            with col_v2:
                reklama = st.slider("Marketing a reklama:", 0, 30000, 8000, step=1000, key="vys_rek")
                doprava = st.slider("Doprava a balicí materiál:", 0, 20000, 6000, step=1000, key="vys_dopr")
                software = st.slider("Software a doména e-shopu:", 0, 10000, 2000, step=500, key="vys_soft")
                ostatni_op = st.slider("Ostatní provozní náklady:", 0, 15000, 4000, step=500, key="vys_ost")

            provozni_naklady_celkem = reklama + doprava + software + ostatni_op
            zisk_pred_zdanenim = hruby_zisk - provozni_naklady_celkem

            st.divider()
            c_m1, c_m2, c_m3 = st.columns(3)
            c_m1.metric("Celkové Tržby", f"{trzby:,} Kč".replace(",", " "))
            c_m2.metric("Hrubý zisk (Tržby - Zboží)", f"{hruby_zisk:,} Kč".replace(",", " "))
            
            if zisk_pred_zdanenim >= 0:
                c_m3.metric("Zisk před zdaněním", f"{zisk_pred_zdanenim:,} Kč".replace(",", " "), delta="Ziskový měsíc", delta_color="normal")
            else:
                c_m3.metric("Výsledek hospodaření", f"{zisk_pred_zdanenim:,} Kč".replace(",", " "), delta="Ztrátový měsíc!", delta_color="inverse")

        st.markdown("""
        <div class="box-red">
            <b>⚠️ Pozor — Důležitý chyták:</b> Výnos není vždy totéž co přijaté peníze na účtu! Firma může vystavit fakturu a ihned mít výnos (účtuje se okamžikem prodeje), ale zákazník jí zaplatí až za 60 dní. Proto samotný zisk nestačí a musíme sledovat Cashflow!
        </div>
        """, unsafe_allow_html=True)

        st.divider()

        # -------------------------------------------------------------------------
        # 5.2.3 CASHFLOW: PENÍZE JSOU KYSLÍK FIRMY
        # -------------------------------------------------------------------------
        st.markdown("### 5.2.3 Cashflow: peníze jsou kyslík firmy")
        st.write(
            "Cashflow znamená **reálný tok peněz**. Ukazuje, kolik peněz do firmy fyzicky přiteklo (na účet nebo do pokladny) "
            "a kolik z ní odešlo."
        )

        st.markdown("""
        <div class="box-gray">
            <b>💧 Cashflow jednoduše:</b> Zisk ukazuje, jestli podnikání dává dlouhodobý ekonomický smysl. Cashflow ukazuje, jestli má firma peníze na zaplacení nájmu a mezd příští úterý!
        </div>
        """, unsafe_allow_html=True)

        st.markdown("#### 🚨 Příběh ze života: Jak zkrachovala papírově úspěšná firma")
        
        with st.container(border=True):
            st.markdown("##### 📅 Případová studie: Vývojářská agentura 'CodeCraft'")
            st.write(
                "• **1. ledna:** Agentura dokončila aplikaci pro velkého klienta a vystavila fakturu na **120 000 Kč** se splatností 60 dní. Ve výsledovce má zisk 60 000 Kč!<br>"
                "• **15. ledna:** Musí zaplatit 30 000 Kč nájem kanceláře a 40 000 Kč mzdy grafikovi.<br>"
                "• **1. února:** Na účtu jí zbývá 5 000 Kč. Klient ještě nezaplatil (má čas do 1. března).<br>"
                "• **15. února:** Přichází další mzdy a nájem (70 000 Kč). Bankovní účet jde na 0 Kč, dodavatelé hrozí soudem.<br>"
                "• **Konec února:** Firma vyhlašuje insolvenci a krachuje, i když je 'papírově' v zisku!"
            , unsafe_allow_html=True)
            
            st.info("💡 **Poučení:** Firma nespravovala své Cashflow. Zákazníkům nabídla příliš dlouhou splatnost (60 dní), zatímco své vlastní výdaje musela platit hned.")


# =========================================================================
    # 5.3 NÁKLADY, VÝNOSY A BOD ZVRATU
    # =========================================================================
    elif selected_section_2.startswith("5.3"):
        import math
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt

        st.markdown("<div class='sub-section-header'>5. FINANČNÍ ŘÍZENÍ V PODNIKU</div>", unsafe_allow_html=True)
        st.markdown("## 5.3 Náklady, výnosy a bod zvratu")
        
        st.write(
            "Aby firma věděla, zda se jí podnikání vůbec vyplatí, musí dokonale rozumět svým nákladům. "
            "Nestačí si říct: *„Prodávám za víc, než nakupuji.“* Firma musí započítat i nájem, software, "
            "reklamu, dopravu, svůj čas, daně, poplatky, vybavení a riziko neprodaných zásob."
        )

        st.markdown("### 5.3.1 Fixní a variabilní náklady")
        st.write("Náklady dělíme do dvou hlavních skupin podle toho, jak se chovají, když firma zvyšuje výrobu nebo prodej.")

        # Tabulka nákladů
        st.markdown("""
        <table class="styled-table">
            <thead>
                <tr>
                    <th>Typ nákladu</th>
                    <th>Co znamená</th>
                    <th>Příklad</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><b>Fixní náklady (FN)</b></td>
                    <td>Nemění se přímo podle počtu prodaných kusů. Platí se, i když firma neprodá nic.</td>
                    <td>Nájem, software, účetní, paušální služby, základní část mezd.</td>
                </tr>
                <tr>
                    <td><b>Variabilní náklady (VN)</b></td>
                    <td>Rostou nebo klesají přímo úměrně podle objemu výroby nebo prodeje.</td>
                    <td>Materiál, nákupní cena zboží, obaly, provize bráně, doprava za kus.</td>
                </tr>
            </tbody>
        </table>
        <br>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="box-blue">
            <b>🧮 Bod zvratu (Break-Even Point - BEP):</b> Ukazuje, kolik přesně musí firma prodat kusů (nebo utržit peněz), aby pokryla všechny své fixní i variabilní náklady. Teprve prodeje NAD bodem zvratu vytvářejí zisk!
        </div>
        """, unsafe_allow_html=True)
        
        st.divider()

        st.markdown("### 🎢 Interaktivní kalkulačka Bodu zvratu a zisku")
        st.write("Zadej hodnoty níže. Graf a výpočty se okamžitě přizpůsobí, abys viděl/a, kdy přesně firma začne vydělávat.")

        with st.container(border=True):
            col1, col2, col3 = st.columns(3)
            with col1:
                fixni = st.number_input("Fixní náklady [Kč]", min_value=0, value=50000, step=1000)
            with col2:
                variabilni = st.number_input("Variabilní náklady/ks [Kč]", min_value=0, value=200, step=10)
            with col3:
                cena = st.number_input("Prodejní cena/ks [Kč]", min_value=0, value=400, step=10)

            marze = cena - variabilni

            st.divider()

            if marze <= 0:
                st.error("⚠️ **Chyba:** Prodejní cena musí být vyšší než variabilní náklady, jinak s každým kusem prohlubuješ ztrátu!")
            else:
                # Matematický výpočet
                bep_ks = fixni / marze
                bep_kc = bep_ks * cena
                
                # Výpočet prvního kusu, který generuje zisk
                prvni_ziskovy_kus = math.floor(bep_ks) + 1
                
                # Formátování čísel pro hezké zobrazení v češtině (mezery místo tisíců)
                bep_ks_str = f"{bep_ks:,.1f}".replace(",", " ").replace(".0", "")
                bep_kc_str = f"{bep_kc:,.0f}".replace(",", " ")
                marze_str = f"{marze:,.0f}".replace(",", " ")

                st.success(f"🎯 **Bod zvratu (zisk = 0):** {bep_ks_str} ks (Tržby: {bep_kc_str} Kč)")
                
                # Vysvětlení pro studenty, odkdy generují zisk
                st.markdown(f"""
                **💡 Co to přesně znamená?**
                * Při prodeji **{bep_ks_str} ks** jste přesně na nule (pokryli jste všechny náklady).
                * 🚀 **Firma začne generovat čistý zisk až od prodeje {prvni_ziskovy_kus}. kusu!**
                * Z každého dalšího kusu získáte čistý zisk **{marze_str} Kč** (což je vaše hrubá marže / krycí příspěvek).
                """)

        # Generování grafu pouze pokud je byznys logicky nastaven (marže > 0)
        if marze > 0:
            st.markdown("#### 📈 Graf vývoje nákladů, tržeb a zisku")
            
            # Příprava dat pro graf
            max_ks = int(bep_ks * 2) if bep_ks > 0 else 100
            x = np.linspace(0, max_ks, 100)
            naklady = fixni + (variabilni * x)
            trzby = cena * x
            zisk = trzby - naklady

            fig, ax = plt.subplots(figsize=(10, 6))
            
            # Černá osa pro nulu
            ax.axhline(y=0, color='black', linewidth=1)

            # Hlavní přímky s jemnějšími barvami
            ax.plot(x, naklady, label='Celkové náklady', color='#e74c3c', linewidth=3)
            ax.plot(x, trzby, label='Tržby', color='#2ecc71', linewidth=3)
            ax.plot(x, zisk, label='Vývoj zisku', color='#3498db', linewidth=2, linestyle='--')

            if bep_ks > 0 and bep_ks < max_ks:
                ax.axhline(y=bep_kc, color='gray', linestyle=':')
                ax.axvline(x=bep_ks, color='gray', linestyle=':')
                
                # Tečka v bodu zvratu
                ax.scatter(bep_ks, bep_kc, color='black', s=100, label='Bod zvratu', zorder=5)
                # Tečka, kde zisk protíná osu nula
                ax.scatter(bep_ks, 0, color='#3498db', s=70, zorder=5)

                # Výrazná textová šipka přímo v grafu!
                y_offset = - (cena * max_ks * 0.15)
                ax.annotate(f'Zisk od {prvni_ziskovy_kus}. ks', 
                            xy=(bep_ks, 0), xytext=(bep_ks + (max_ks*0.05), y_offset),
                            arrowprops=dict(facecolor='#3498db', shrink=0.05, width=1.5, headwidth=7, edgecolor='none'),
                            fontsize=11, color='#3498db', fontweight='bold',
                            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#3498db", lw=1))

            # Barevné šrafování zón
            ax.fill_between(x, naklady, trzby, where=(naklady > trzby), interpolate=True, color='#e74c3c', alpha=0.15, label='Zóna ztráty')
            ax.fill_between(x, naklady, trzby, where=(naklady < trzby), interpolate=True, color='#2ecc71', alpha=0.15, label='Zóna zisku')

            # Nastavení popisků os
            ax.set_xlabel('Počet prodaných kusů [ks]', fontsize=12)
            ax.set_ylabel('Částka [Kč]', fontsize=12)
            ax.set_title('Zóna zisku a ztráty', fontsize=14, fontweight='bold')
            
            # Legenda odsunuta vlevo nahoru, aby nepřekážela křivkám
            ax.legend(loc='upper left', fontsize=10)
            ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

            # Formátování čísel os na tisíce s mezerou
            ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda val, p: format(int(val), ',').replace(',', ' ')))
            ax.get_xaxis().set_major_formatter(plt.FuncFormatter(lambda val, p: format(int(val), ',').replace(',', ' ')))

            # Zobrazení grafu
            st.pyplot(fig)

            st.write(
                "💡 *Vysvětlivka: Plocha označená červeně představuje ztrátu, zelená zisk. "
                "Modrá přerušovaná čára ukazuje vývoj zisku (pod nulou je podnik ve ztrátě, v bodě zvratu protíná nulu a roste do zisku).*"
            )
            # =========================================================================
    # 5.4 ZDROJE FINANCOVÁNÍ PODNIKU
    # =========================================================================
    elif selected_section_2.startswith("5.4 "):
        st.markdown("<div class='sub-section-header'>5. FINANČNÍ ŘÍZENÍ V PODNIKU</div>", unsafe_allow_html=True)
        st.markdown("## 5.4 Zdroje financování podniku")
        
        st.write("Firma potřebuje peníze na start, provoz i růst. Tyto zdroje financování se dělí hlavně na **vlastní** (tvé peníze) a **cizí** (cizí peníze, které musíš vrátit).")

        st.markdown("### 🏦 Přehled zdrojů financování")
        
        zdroje = {
            "Vlastní kapitál": {"co": "Peníze majitele nebo společníků vložené do firmy.", "vyhoda": "Není nutné splácet jako úvěr.", "riziko": "Majitel riskuje vlastní peníze."},
            "Bootstrapping": {"co": "Firma roste čistě z vlastních tržeb a úspor bez cizí pomoci.", "vyhoda": "Majitel si drží 100% kontrolu.", "riziko": "Růst může být velmi pomalý a vyčerpávající."},
            "Zisk ponechaný ve firmě": {"co": "Firma nevyplatí zisk majitelům, ale použije ho na rozvoj.", "vyhoda": "Nejlevnější financování z vlastního výkonu.", "riziko": "Majitelé si nemohou peníze hned užít."},
            "Bankovní úvěr": {"co": "Banka nebo věřitel půjčí peníze za úrok.", "vyhoda": "Majitel neztrácí podíl ve firmě.", "riziko": "Úvěr se musí splácet i v měsících, kdy nejsou tržby."},
            "Leasing": {"co": "Pronájem a financování auta, stroje nebo vybavení.", "vyhoda": "Firma nemusí platit obrovskou částku najednou.", "riziko": "Celkové přeplacené náklady mohou být vyšší."},
            "Investor (Business Angel/VC)": {"co": "Investor vloží peníze výměnou za podíl ve firmě.", "vyhoda": "Přinese velký kapitál, kontakty a cenné know-how.", "riziko": "Majitel ztrácí část kontroly a budoucího zisku."},
            "Dotace a granty": {"co": "Finanční podpora z veřejných programů (EU, stát).", "vyhoda": "Často se nemusí vracet (peníze zdarma).", "riziko": "Pekelná administrativa, přísná pravidla a nejistota."}
        }

        # Interaktivní zobrazení zdrojů pomocí expanderů
        for nazev, data in zdroje.items():
            with st.expander(f"**{nazev}**"):
                st.write(f"📖 **Co to znamená:** {data['co']}")
                st.success(f"✅ **Výhoda:** {data['vyhoda']}")
                st.warning(f"⚠️ **Riziko / Nevýhoda:** {data['riziko']}")

        st.markdown("""
        <div class="box-red">
            <b>⚖️ Důležité rozhodnutí:</b> Rychlý růst není vždy zdravý. Firma může získat ohromné množství objednávek, ale pokud nemá peníze na nákup zásob, platy lidí a drahou dopravu, může ji paradoxně samotný růst poslat do krachu (ukončení cashflow).
        </div>
        """, unsafe_allow_html=True)

        st.divider()

        st.markdown("### 🎮 Mini-scénář: Jak bys financoval/a tento projekt?")
        st.write("Máš úspěšný malý e-shop. Získal jsi nečekanou nabídku dodávat své produkty do velké sítě supermarketů. Potřebuješ ale okamžitě **1 000 000 Kč** na výrobu první obří várky. Nemáš je. Co uděláš?")
        
        volba_finance = st.radio("Vyber si strategii:", [
            "Vyber možnost...",
            "Vezmu si bankovní úvěr (Půjčka na 1 milion Kč).",
            "Najdu investora a dám mu 30 % firmy za 1 milion Kč.",
            "Odmítnu to. Pojedu si dál svůj malý e-shop a bootstrapping."
        ])

        if volba_finance == "Vezmu si bankovní úvěr (Půjčka na 1 milion Kč).":
            st.info("🏦 **Cesta dluhu:** Zůstane ti 100 % firmy! Pokud se prodeje v supermarketu uchytí, vyděláš balík. Ale pozor – pokud supermarket zboží neprodá a vrátí ti ho, zůstane ti na krku dluh, který tě může zničit.")
        elif volba_finance == "Najdu investora a dám mu 30 % firmy za 1 milion Kč.":
            st.info("🤝 **Cesta partnerství:** Chytré sdílení rizika. Pokud to nevyjde, investor přijde o peníze, ale ty nebudeš v dluzích. Pokud to ale bude hit, právě jsi navždy odevzdal/a 30 % všech svých budoucích zisků někomu jinému.")
        elif volba_finance == "Odmítnu to. Pojedu si dál svůj malý e-shop a bootstrapping.":
            st.info("🐢 **Cesta bezpečí:** Nulové finanční riziko. Zůstaneš svým pánem a v klidu spíš. Z byznysového hlediska jsi ale možná právě zahodil/a životní šanci na raketový růst.")


    # =========================================================================
    # 5.5 FINANČNÍ ANALÝZA: KONTROLA FINANČNÍHO ZDRAVÍ
    # =========================================================================
    elif selected_section_2.startswith("5.5 "):
        st.markdown("<div class='sub-section-header'>5. FINANČNÍ ŘÍZENÍ V PODNIKU</div>", unsafe_allow_html=True)
        st.markdown("## 5.5 Finanční analýza: kontrola finančního zdraví")
        
        st.write(
            "Finanční analýza je práce s čísly, která pomáhá posoudit zdraví podniku. Nejde jen o slepé dosazování do vzorců. "
            "Důležité je umět výsledky interpretovat: co číslo znamená, proč vzniklo a co by měla firma udělat dál."
        )

        st.markdown("""
        <div class="box-blue">
            <b>🔍 K čemu je to dobré:</b> Pomáhá zjistit, zda je firma zisková, zadlužená, platebně schopná, efektivní a stabilní. Sama o sobě firmu nezachrání, ale funguje jako rentgen – včas ukáže, kde přesně to hoří.
        </div>
        """, unsafe_allow_html=True)

        # 5.5.1 KROK ZA KROKEM
        with st.expander("🛠️ 5.5.1 Jak se finanční analýza sestavuje krok za krokem"):
            st.markdown("""
            1. **Vyber firmu** – Reálný nebo fiktivní podnik.
            2. **Získej data** – Tržby, náklady, zisk, aktiva, vlastní kapitál, závazky, peníze.
            3. **Uprav data** – Do přehledné tabulky ve stejných jednotkách (např. v tisících Kč).
            4. **Spočítej ukazatele** – Rentabilita, likvidita, zadluženost, aktivita.
            5. **Porovnej v čase** – Jeden rok nestačí. Sleduj trend (zlepšuje se to?).
            6. **Vysvětli výsledky** – Zkus odhalit příběh za čísly.
            7. **Navrhni opatření** – Snížit náklady? Změnit ceny? Vymáhat pohledávky?
            8. **Upozorni na limity** – Čísla bez znalosti situace na trhu mohou klamat.
            """)
            st.markdown("""
            <div class="box-green">
                <b>🧠 Nejdůležitější věta:</b> Finanční analýza není opisování vzorců. Je to příběh firmy vyprávěný čísly.
            </div>
            """, unsafe_allow_html=True)

        st.divider()

        # 5.5.2 AŽ 5.5.6 - INTERAKTIVNÍ DASHBOARD
        st.markdown("### 🎛️ Palubní deska finančního ředitele (Ukazatele v praxi)")
        st.write("Vlož základní data své firmy a nech si v záložkách spočítat a analyzovat všech pět hlavních skupin ukazatelů: Rentabilitu (5.5.3), Likviditu (5.5.4), Zadluženost (5.5.5) a Aktivitu (5.5.6).")

        # Vstupní data pro simulátor
        with st.container(border=True):
            st.markdown("#### 📥 Zadej data o firmě (v Kč)")
            c1, c2, c3, c4 = st.columns(4)
            trzby = c1.number_input("Celkové Tržby", value=1000000, step=100000)
            zisk = c2.number_input("Čistý zisk", value=80000, step=10000)
            aktiva = c3.number_input("Aktiva (Majetek)", value=2000000, step=100000)
            vlastni_kapital = c4.number_input("Vlastní kapitál", value=1100000, step=100000)

            c5, c6, c7, c8 = st.columns(4)
            cizi_zdroje = c5.number_input("Cizí zdroje (Dluhy)", value=900000, step=100000)
            obezna_aktiva = c6.number_input("Oběžná aktiva", value=500000, step=50000)
            kratkodobe_zavazky = c7.number_input("Krátk. závazky (do roka)", value=300000, step=50000)
            penize = c8.number_input("Peníze v hotovosti/na účtu", value=150000, step=10000)

        # Prevence dělení nulou
        trzby = max(trzby, 1)
        aktiva = max(aktiva, 1)
        vlastni_kapital = max(vlastni_kapital, 1)
        kratkodobe_zavazky = max(kratkodobe_zavazky, 1)

        # Záložky pro jednotlivé skupiny
        tab_rent, tab_likv, tab_zadl, tab_akt = st.tabs(["📈 Rentabilita (Ziskovost)", "💧 Likvidita (Platební schopnost)", "💳 Zadluženost", "⚙️ Aktivita"])

# --- 5.5.3 RENTABILITA ---
        with tab_rent:
            st.markdown("#### 5.5.3 Ukazatele rentability: Vydělává podnik dost?")
            st.write("Rentabilita ukazuje, jak dobře firma vytváří zisk.")
            
            ros = (zisk / trzby) * 100
            roa = (zisk / aktiva) * 100
            roe = (zisk / vlastni_kapital) * 100

            col_r1, col_r2, col_r3 = st.columns(3)
            
            # --- ROS ---
            with col_r1:
                st.metric("ROS (Rentabilita tržeb)", f"{ros:.1f} %")
                st.latex(r"\frac{\text{Zisk}}{\text{Tržby}} \times 100")
                st.caption(f"Z každých 100 Kč tržeb zbývá {ros:.1f} Kč zisku.")
                
                if ros < 0:
                    st.error("🚨 **Ztráta:** Z každého prodeje firma prodělává.")
                elif ros < 5:
                    st.warning("⚠️ **Nízká marže:** Běžné u supermarketů (žijí z objemu), ale u jiných oborů je to rizikové.")
                elif ros <= 15:
                    st.success("✅ **Zdravý výsledek:** Firma má dostatečnou ziskovost.")
                else:
                    st.info("🏆 **Skvělé:** Extrémně ziskový byznys (typické pro IT, služby nebo luxusní zboží).")

            # --- ROA ---
            with col_r2:
                st.metric("ROA (Rentabilita aktiv)", f"{roa:.1f} %")
                st.latex(r"\frac{\text{Zisk}}{\text{Aktiva}} \times 100")
                st.caption("Jak efektivně majetek generuje zisk.")
                
                if roa < 0:
                    st.error("🚨 **Špatné:** Majetek negeneruje žádný zisk.")
                elif roa < 4:
                    st.warning("⚠️ **Nízká efektivita:** Majetek leží ladem nebo je ho zbytečně moc na to, kolik vydělává.")
                elif roa <= 10:
                    st.success("✅ **Dobrý standard:** Firma efektivně využívá to, co vlastní.")
                else:
                    st.info("🏆 **Výborné:** Firma dokáže s málem majetku vydělat spoustu peněz.")

            # --- ROE ---
            with col_r3:
                st.metric("ROE (Rent. vl. kapitálu)", f"{roe:.1f} %")
                st.latex(r"\frac{\text{Zisk}}{\text{Vlastní kapitál}} \times 100")
                st.caption("Jaké je zhodnocení vložených peněz majitele.")
                
                if roe < 0:
                    st.error("🚨 **Kritické:** Majitel prodělává své vlastní peníze.")
                elif roe < 5:
                    st.warning("⚠️ **Slabé:** Majitel by udělal lépe, kdyby firmu zavřel a peníze dal na bezpečný spořicí účet v bance.")
                elif roe <= 15:
                    st.success("✅ **Slušné:** Zhodnocení je lepší než v bance, investor je spokojený.")
                else:
                    st.info("🏆 **Skvělé:** Vysoce atraktivní zhodnocení. Taková čísla lákají další investory!")

            st.markdown("""
            <div class="box-gray">
                <b>💡 Důležitý kontext pro analytiky:</b> Co je „dobré“ a „špatné“ číslo, vždy závisí na oboru! Supermarket může mít ROS pouhá 2 % a je to skvělé (protože denně prodá tuny zboží). Softwarová firma má běžně ROS i 30 %. Proto se finanční analýza <b>vždy porovnává s konkurencí v oboru</b>.
            </div>
            """, unsafe_allow_html=True)

        # --- 5.5.4 LIKVIDITA ---
        with tab_likv:
            st.markdown("#### 5.5.4 Ukazatele likvidity: Zvládne podnik platit včas?")
            st.write("Mít majetek neznamená mít peníze. Likvidita měří schopnost platit faktury.")
            
            bezna_likvidita = obezna_aktiva / kratkodobe_zavazky
            okamzita_likvidita = penize / kratkodobe_zavazky

            col_l1, col_l2 = st.columns(2)
            col_l1.metric("Běžná likvidita", f"{bezna_likvidita:.2f}")
            col_l1.latex(r"\frac{\text{Oběžná aktiva}}{\text{Krátkodobé závazky}}")
            if bezna_likvidita < 1:
                col_l1.error("🚨 Pod 1,0: Firma nemá dost aktiv na zaplacení dluhů!")
            elif bezna_likvidita > 2.5:
                col_l1.warning("⚠️ Nad 2,5: Firma drží moc majetku ladem a neinvestuje ho.")
            else:
                col_l1.success("✅ Ideální hodnota (kolem 1,5 – 2,5).")

            col_l2.metric("Okamžitá likvidita", f"{okamzita_likvidita:.2f}")
            col_l2.latex(r"\frac{\text{Peníze}}{\text{Krátkodobé závazky}}")
            col_l2.caption("Kolik dluhů umí zaplatit IHNED z účtu.")
            
            st.markdown("""
            <div class="box-red">
                <b>⚠️ Pozor:</b> Příliš nízká likvidita znamená riziko krachu. Příliš vysoká znamená, že peníze leží ladem a ztrácejí hodnotu.
            </div>
            """, unsafe_allow_html=True)

        # --- 5.5.5 ZADLUŽENOST ---
        with tab_zadl:
            st.markdown("#### 5.5.5 Ukazatele zadluženosti: Kolik firma dluží?")
            st.write("Dluh není špatný, pokud pomáhá růst. Problém je, když ho firma neutáhne.")
            
            celkova_zadluzenost = (cizi_zdroje / aktiva) * 100
            mira_zadluzenosti = cizi_zdroje / vlastni_kapital

            col_z1, col_z2 = st.columns(2)
            col_z1.metric("Celková zadluženost", f"{celkova_zadluzenost:.1f} %")
            col_z1.latex(r"\frac{\text{Cizí zdroje}}{\text{Aktiva}} \times 100")
            if celkova_zadluzenost > 70:
                col_z1.error("🚨 Extrémní zadlužení! Firma je v rukou věřitelů.")
            elif celkova_zadluzenost < 30:
                col_z1.success("✅ Nízká zadluženost (možná firma nevyužívá potenciál úvěru k růstu).")
            else:
                col_z1.info("Odpovídající zadlužení.")

            col_z2.metric("Míra zadluženosti", f"{mira_zadluzenosti:.2f}")
            col_z2.latex(r"\frac{\text{Cizí zdroje}}{\text{Vlastní kapitál}}")
            col_z2.caption("Kolik cizích peněz připadá na 1 Kč vlastních.")

        # --- 5.5.6 AKTIVITA ---
        with tab_akt:
            st.markdown("#### 5.5.6 Ukazatele aktivity: Nezasekávají se peníze?")
            st.write("Tyto ukazatele měří rychlost oběhu. Dosaď sem hodnoty zásob a pohledávek pro výpočet dní.")
            
            c_a1, c_a2 = st.columns(2)
            zasoby = c_a1.number_input("Hodnota zásob na skladě", value=200000, step=10000)
            pohledavky = c_a2.number_input("Pohledávky (Zákazníci dluží nám)", value=150000, step=10000)
            
            obrat_aktiv = trzby / aktiva
            doba_zasob = (zasoby / trzby) * 365
            doba_inkasa = (pohledavky / trzby) * 365
            doba_splatnosti = (kratkodobe_zavazky / trzby) * 365
            
            st.divider()
            c_m1, c_m2, c_m3 = st.columns(3)
            
            c_m1.metric("Obrat aktiv", f"{obrat_aktiv:.2f}x")
            c_m1.caption("Kolikrát do roka se majetek 'otočí' v tržbách.")
            
            c_m2.metric("Doba inkasa (čekání na platbu)", f"{doba_inkasa:.0f} dní")
            if doba_inkasa > doba_splatnosti:
                c_m2.error("🚨 Čekáš na peníze déle, než máš na zaplacení vlastních dluhů!")
            else:
                c_m2.success("✅ Peníze inkasuješ rychleji.")
                
            c_m3.metric("Doba splatnosti (tvých faktur)", f"{doba_splatnosti:.0f} dní")
            
            st.markdown("""
            <div class="box-purple">
                <b>💡 Praktický význam:</b> Pokud firma čeká na peníze od zákazníků 60 dní (Doba inkasa), ale dodavatelům musí platit do 14 dní (Doba splatnosti), vyčerpá si hotovost a může zkrachovat na cashflow problém, i když je zisková!
            </div>
            """, unsafe_allow_html=True)
# =========================================================================
    # 5.6 MODELOVÁ FINANČNÍ ANALÝZA: E-SHOP DROPZONE
    # =========================================================================
    elif selected_section_2.startswith("5.6"):
        import pandas as pd
        
        st.markdown("<div class='sub-section-header'>5. FINANČNÍ ŘÍZENÍ V PODNIKU</div>", unsafe_allow_html=True)
        st.markdown("## 5.6 Modelová finanční analýza: e-shop „DropZone“")
        
        st.write(
            "Představ si úspěšný studentský e-shop **DropZone**, který prodává vlastní limitovaný streetwear merch. "
            "Na první pohled firma raketově roste. Je ale opravdu finančně zdravá? "
            "Vyzkoušej si roli finančního ředitele: analyzuj výchozí stav a pak zkus čísla pro Rok 2 upravit tak, abys firmu zachránil před krachem na cashflow!"
        )

        st.divider()

        # Pevná data pro Rok 1 (Historie)
        data_y1 = {
            "Tržby": 800000, "Náklady": 740000, "Zisk": 60000,
            "Aktiva": 500000, "Vlastní kapitál": 250000, "Cizí zdroje": 250000,
            "Oběžná aktiva": 220000, "Zásoby": 120000, "Peníze": 45000,
            "Krátkodobé závazky": 140000, "Pohledávky": 55000
        }

        st.markdown("### 🎛️ Interaktivní simulátor: Zachraň DropZone")
        st.write("Hodnoty pro **Rok 1 jsou pevné**. Čísla pro **Rok 2 můžeš libovolně měnit**. (Výchozí čísla ukazují nebezpečný růst na dluh).")

        with st.container(border=True):
            st.markdown("#### 📥 Zadej data pro Rok 2 (v Kč)")
            
            col_in1, col_in2, col_in3 = st.columns(3)
            
            with col_in1:
                st.markdown("**Výsledovka**")
                trzby_y2 = st.number_input("Tržby", value=1200000, step=50000, key="dz_trzby")
                naklady_y2 = st.number_input("Náklady", value=1080000, step=50000, key="dz_naklady")
                zisk_y2 = trzby_y2 - naklady_y2
                st.metric("Automatický čistý zisk", f"{zisk_y2:,} Kč".replace(",", " "))
                
            with col_in2:
                st.markdown("**Rozvaha (Majetek a zdroje)**")
                aktiva_y2 = st.number_input("Aktiva celkem", value=700000, step=50000, key="dz_aktiva")
                vk_y2 = st.number_input("Vlastní kapitál", value=300000, step=50000, key="dz_vk")
                cz_y2 = st.number_input("Cizí zdroje (Dluhy)", value=400000, step=50000, key="dz_cz")
                
            with col_in3:
                st.markdown("**Hotovost a provoz**")
                ob_aktiva_y2 = st.number_input("Oběžná aktiva", value=310000, step=50000, key="dz_oa")
                zasoby_y2 = st.number_input("Zásoby na skladě", value=170000, step=10000, key="dz_zas")
                pohledavky_y2 = st.number_input("Pohledávky (Dluží nám)", value=105000, step=10000, key="dz_pohl")
                penize_y2 = st.number_input("Peníze na účtu", value=35000, step=5000, key="dz_pen")
                kz_y2 = st.number_input("Krátkodobé závazky", value=230000, step=10000, key="dz_kz")

        # Dramatický graf úvodu - Zisk vs Peníze (Reaguje na změny)
        st.markdown("### 📊 Rychlý pohled na zdraví firmy (Zisk vs. Peníze)")
        
        chart_data = pd.DataFrame(
            {
                "Čistý zisk": [data_y1["Zisk"], zisk_y2],
                "Peníze na účtu": [data_y1["Peníze"], penize_y2]
            },
            index=["Rok 1", "Rok 2 (Tvá čísla)"]
        )
        st.bar_chart(chart_data, color=["#2ecc71", "#e74c3c"])
        
        st.markdown("### 🕵️‍♂️ Hloubková analýza na základě tvých čísel")
        tab_rentabilita, tab_likvidita, tab_aktivita, tab_zaver = st.tabs([
            "📈 Ziskovost", 
            "💧 Likvidita", 
            "⚙️ Aktivita & Dluh", 
            "🚨 Finální verdikt"
        ])

        # Prevence dělení nulou pro bezpečnost
        trzby_y2_safe = max(trzby_y2, 1)
        aktiva_y2_safe = max(aktiva_y2, 1)
        vk_y2_safe = max(vk_y2, 1)
        kz_y2_safe = max(kz_y2, 1)

        # Výpočty Rok 1
        ros_1 = (data_y1["Zisk"] / data_y1["Tržby"]) * 100
        roa_1 = (data_y1["Zisk"] / data_y1["Aktiva"]) * 100
        roe_1 = (data_y1["Zisk"] / data_y1["Vlastní kapitál"]) * 100
        bl_1 = data_y1["Oběžná aktiva"] / data_y1["Krátkodobé závazky"]
        pl_1 = (data_y1["Oběžná aktiva"] - data_y1["Zásoby"]) / data_y1["Krátkodobé závazky"]
        ol_1 = data_y1["Peníze"] / data_y1["Krátkodobé závazky"]
        zadl_1 = (data_y1["Cizí zdroje"] / data_y1["Aktiva"]) * 100
        obrat_1 = data_y1["Tržby"] / data_y1["Aktiva"]
        inkaso_1 = (data_y1["Pohledávky"] / data_y1["Tržby"]) * 365

        # Výpočty Rok 2
        ros_2 = (zisk_y2 / trzby_y2_safe) * 100
        roa_2 = (zisk_y2 / aktiva_y2_safe) * 100
        roe_2 = (zisk_y2 / vk_y2_safe) * 100
        bl_2 = ob_aktiva_y2 / kz_y2_safe
        pl_2 = (ob_aktiva_y2 - zasoby_y2) / kz_y2_safe
        ol_2 = penize_y2 / kz_y2_safe
        zadl_2 = (cz_y2 / aktiva_y2_safe) * 100
        obrat_2 = trzby_y2 / aktiva_y2_safe
        inkaso_2 = (pohledavky_y2 / trzby_y2_safe) * 365

        with tab_rentabilita:
            st.markdown("#### Ukazatele rentability (Ziskovosti)")
            c1, c2, c3 = st.columns(3)
            
            c1.metric("ROS (Rentabilita tržeb)", f"{ros_2:.1f} %", f"{ros_2 - ros_1:.1f} % (z {ros_1:.1f} %)")
            c2.metric("ROA (Rentabilita aktiv)", f"{roa_2:.1f} %", f"{roa_2 - roa_1:.1f} % (z {roa_1:.1f} %)")
            c3.metric("ROE (Rent. vl. kapitálu)", f"{roe_2:.1f} %", f"{roe_2 - roe_1:.1f} % (z {roe_1:.1f} %)")
            
            if ros_2 > ros_1 and roe_2 > roe_1:
                st.success("✅ Firma se z pohledu ziskovosti zlepšuje (nebo drží skvělá čísla).")
            else:
                st.warning("⚠️ Rentabilita klesá. Zkontroluj, zda neplýtváš náklady.")

        with tab_likvidita:
            st.markdown("#### Ukazatele likvidity (Schopnost platit)")
            c1, c2, c3 = st.columns(3)
            
            c1.metric("Běžná likvidita", f"{bl_2:.2f}", f"{bl_2 - bl_1:.2f} (z {bl_1:.2f})")
            c2.metric("Pohotová likvidita", f"{pl_2:.2f}", f"{pl_2 - pl_1:.2f} (z {pl_1:.2f})")
            c3.metric("Okamžitá likvidita", f"{ol_2:.2f}", f"{ol_2 - ol_1:.2f} (z {ol_1:.2f})")
            
            if ol_2 < 0.2:
                st.error("🚨 Kritický nedostatek hotovosti! Zvyš peníze na účtu, nebo sniž krátkodobé závazky.")
            elif bl_2 > bl_1:
                st.success("✅ Platební morálka firmy se oproti prvnímu roku zlepšila.")
            else:
                st.info("Likvidita se drží, ale hlídej si hotovostní polštář.")

        with tab_aktivita:
            st.markdown("#### Ukazatele aktivity a zadluženosti")
            c1, c2, c3 = st.columns(3)
            
            # Zadluženost a inkaso jsou inverzní (růst je špatný)
            c1.metric("Celková zadluženost", f"{zadl_2:.1f} %", f"{zadl_2 - zadl_1:.1f} % (z {zadl_1:.1f} %)", delta_color="inverse")
            c2.metric("Obrat aktiv", f"{obrat_2:.2f}x", f"{obrat_2 - obrat_1:.2f}x (z {obrat_1:.2f}x)")
            c3.metric("Doba inkasa pohledávek", f"{inkaso_2:.0f} dní", f"{inkaso_2 - inkaso_1:.0f} dní (z {inkaso_1:.0f} dní)", delta_color="inverse")
            
            if inkaso_2 > 30:
                st.warning("⚠️ Zákazníci ti platí moc dlouho (více než měsíc). Zkus v zadání snížit pohledávky!")
            else:
                st.success("✅ Zákazníci platí rychle, peníze se ti vrací plynule.")

        with tab_zaver:
            st.markdown("#### 📝 Závěrečná zpráva (Dynamicky hodnoceno)")
            
            if zisk_y2 > data_y1["Zisk"] and penize_y2 < data_y1["Peníze"]:
                st.error("🚨 **Varování z výchozího scénáře:** Tohle je klasická past! Zisk se ti sice zvýšil, ale peníze na účtu mizí. Pravděpodobně ti utekly do rostoucích zásob a nezaplacených faktur (pohledávek). Zároveň tě začínají drtit narůstající krátkodobé závazky. **Zkus ve vstupech nahoře zmenšit Zásoby, vybrat Pohledávky (čímž se ti zvýší Peníze) a uvidíš, jak se firma uzdraví!**")
            elif zisk_y2 > data_y1["Zisk"] and penize_y2 >= data_y1["Peníze"]:
                st.success("🏆 **Výborná práce CEO!** Dokázal jsi nejen zvýšit zisk, ale i udržet zdravou hotovost. Takhle má vypadat udržitelný růst podniku.")
            elif zisk_y2 <= 0:
                st.error("💀 **Firma je ve ztrátě.** Než začneš řešit likviditu a zásoby, musíš spravit samotný byznys model (zvýšit tržby nebo osekat náklady).")
            else:
                st.info("Firma je stabilní, zkus si pohrát s hodnotami a najít ideální poměr mezi ziskem a hotovostí.")
                
# =========================================================================
    # 5.7 PRÁZDNÁ ŠABLONA FINANČNÍ ANALÝZY
    # =========================================================================
    elif selected_section_2.startswith("5.7"):
        import pandas as pd
        
        st.markdown("<div class='sub-section-header'>5. FINANČNÍ ŘÍZENÍ V PODNIKU</div>", unsafe_allow_html=True)
        st.markdown("## 5.7 Prázdná šablona finanční analýzy (Interaktivní cvičení)")
        st.write(
            "Tuto šablonu můžeš využít pro svůj vlastní školní projekt, fiktivní studentskou firmu nebo rychlou analýzu reálného podniku. "
            "Nemusíš nic složitě počítat na kalkulačce – stačí vyplnit vstupní data a aplikace se o zbytek postará sama!"
        )

        st.markdown("### 📝 Krok 1: Zadej data svého projektu")
        st.info("💡 **Návod k tabulce:** Dvakrát klikni na jakékoliv číslo ve sloupcích **Rok 1** a **Rok 2**, přepiš ho na své vlastní a stiskni **Enter**. Výpočty dole se hned aktualizují.")

        # Výchozí data (čistá čísla bez formátování měny, aby šla snadno přepisovat)
        vstupy = {
            "Položka": [
                "Tržby", "Náklady celkem", "Zisk", "Aktiva celkem", "Vlastní kapitál", 
                "Cizí zdroje", "Oběžná aktiva", "Zásoby", "Peníze", 
                "Krátkodobé závazky", "Pohledávky"
            ],
            "Nápověda k položce": [
                "Vše, co firma utržila", "Vše, co firma zaplatila", "Zisk (Tržby mínus Náklady)", 
                "Celkový majetek firmy", "Peníze majitelů", "Dluhy (Úvěry, atd.)", 
                "Krátkodobý majetek", "Zboží na skladě", "Hotovost a peníze v bance", 
                "Faktury k zaplacení do 1 roku", "Peníze, které dluží zákazníci nám"
            ],
            "Rok 1": [500000, 450000, 50000, 300000, 200000, 100000, 150000, 50000, 40000, 80000, 60000],
            "Rok 2": [750000, 650000, 100000, 450000, 300000, 150000, 250000, 80000, 70000, 120000, 100000]
        }
        df_vstupy = pd.DataFrame(vstupy).set_index("Položka")

        # Interaktivní tabulka (zakážeme úpravu pouze sloupce s nápovědou)
        edited_df = st.data_editor(
            df_vstupy,
            disabled=["Nápověda k položce"],
            use_container_width=True
        )

        st.divider()
        st.markdown("### 🧮 Krok 2: Automatické výsledky (Vysvědčení firmy)")

        # Bezpečné dělení (aby aplikace nespadla, když student zadá nulu)
        def safe_div(a, b):
            return a / b if b != 0 else 0

        # Funkce pro vytažení dat z tabulky
        def get_val(rok_col, polozka):
            try:
                return float(edited_df.loc[polozka, rok_col])
            except:
                return 0.0

        # Získání dat pro oba roky
        y1 = {k: get_val("Rok 1", k) for k in df_vstupy.index}
        y2 = {k: get_val("Rok 2", k) for k in df_vstupy.index}

        tab_r, tab_l, tab_z = st.tabs(["📈 Ziskovost (Rentabilita)", "💧 Likvidita (Hotovost)", "⚙️ Zadluženost a Aktivita"])

        with tab_r:
            c1, c2, c3 = st.columns(3)
            # Výpočty
            ros_2 = safe_div(y2["Zisk"], y2["Tržby"]) * 100
            roa_2 = safe_div(y2["Zisk"], y2["Aktiva celkem"]) * 100
            roe_2 = safe_div(y2["Zisk"], y2["Vlastní kapitál"]) * 100
            
            ros_1 = safe_div(y1["Zisk"], y1["Tržby"]) * 100
            roa_1 = safe_div(y1["Zisk"], y1["Aktiva celkem"]) * 100
            roe_1 = safe_div(y1["Zisk"], y1["Vlastní kapitál"]) * 100

            c1.metric("ROS (Marže z tržeb)", f"{ros_2:.1f} %", f"{ros_2 - ros_1:.1f} %")
            c1.caption("Kolik % z tržeb zůstává jako zisk?")
            
            c2.metric("ROA (Využití majetku)", f"{roa_2:.1f} %", f"{roa_2 - roa_1:.1f} %")
            c2.caption("Jak efektivně firma využívá majetek?")
            
            c3.metric("ROE (Zhodnocení vkladu)", f"{roe_2:.1f} %", f"{roe_2 - roe_1:.1f} %")
            c3.caption("Jak se zhodnocují peníze vlastníků?")

        with tab_l:
            c1, c2, c3 = st.columns(3)
            bl_2 = safe_div(y2["Oběžná aktiva"], y2["Krátkodobé závazky"])
            pl_2 = safe_div(y2["Oběžná aktiva"] - y2["Zásoby"], y2["Krátkodobé závazky"])
            ol_2 = safe_div(y2["Peníze"], y2["Krátkodobé závazky"])
            
            bl_1 = safe_div(y1["Oběžná aktiva"], y1["Krátkodobé závazky"])
            pl_1 = safe_div(y1["Oběžná aktiva"] - y1["Zásoby"], y1["Krátkodobé závazky"])
            ol_1 = safe_div(y1["Peníze"], y1["Krátkodobé závazky"])

            c1.metric("Běžná likvidita", f"{bl_2:.2f}", f"{bl_2 - bl_1:.2f}")
            c1.caption("Zvládne firma platit závazky z majetku?")
            
            c2.metric("Pohotová likvidita", f"{pl_2:.2f}", f"{pl_2 - pl_1:.2f}")
            c2.caption("Jak je na tom, když neprodá zásoby?")
            
            c3.metric("Okamžitá likvidita", f"{ol_2:.2f}", f"{ol_2 - ol_1:.2f}")
            c3.caption("Co lze zaplatit IHNED z účtu?")

        with tab_z:
            c1, c2, c3 = st.columns(3)
            zadl_2 = safe_div(y2["Cizí zdroje"], y2["Aktiva celkem"]) * 100
            mira_2 = safe_div(y2["Cizí zdroje"], y2["Vlastní kapitál"])
            inkaso_2 = safe_div(y2["Pohledávky"], y2["Tržby"]) * 365
            
            zadl_1 = safe_div(y1["Cizí zdroje"], y1["Aktiva celkem"]) * 100
            mira_1 = safe_div(y1["Cizí zdroje"], y1["Vlastní kapitál"])
            inkaso_1 = safe_div(y1["Pohledávky"], y1["Tržby"]) * 365

            c1.metric("Celková zadluženost", f"{zadl_2:.1f} %", f"{zadl_2 - zadl_1:.1f} %", delta_color="inverse")
            c1.caption("Jak moc firma funguje na dluh?")
            
            c2.metric("Míra zadluženosti", f"{mira_2:.2f}x", f"{mira_2 - mira_1:.2f}x", delta_color="inverse")
            c2.caption("Kolik dluhu připadá na 1 Kč vlastních peněz?")
            
            c3.metric("Doba inkasa pohledávek", f"{inkaso_2:.0f} dní", f"{inkaso_2 - inkaso_1:.0f} dní", delta_color="inverse")
            c3.caption("Za kolik dní průměrně zákazníci platí?")

        st.markdown("""
        <div class="box-blue">
            <b>✍️ Úkol pro tebe:</b> Vyplň tabulku pro fiktivní podnik. Prohlédni si výsledky nahoře a zamysli se: 
            <i>Co se firmě daří? Kde číhá největší riziko? Jaké JEDNO konkrétní opatření bys majiteli poradil/a?</i>
        </div>
        """, unsafe_allow_html=True)


    # =========================================================================
    # 5.8 JAK NAPSAT ZÁVĚR FINANČNÍ ANALÝZY
    # =========================================================================
    elif selected_section_2.startswith("5.8"):
        st.markdown("<div class='sub-section-header'>5. FINANČNÍ ŘÍZENÍ V PODNIKU</div>", unsafe_allow_html=True)
        st.markdown("## 5.8 Jak napsat závěr finanční analýzy")
        
        st.write(
            "Samotné výpočty nestačí. Dobrý závěr finanční analýzy (manažerské shrnutí) má být **krátký, konkrétní a srozumitelný** "
            "i pro člověka, který není účetní. Pokud vysypeš na šéfa nebo investora jen procenta, nepochopí tě. Musíš vyprávět příběh čísel."
        )

        st.markdown("""
        **Struktura dokonalého závěru:**
        * **📈 Ziskovost:** Vyděláváme / proděláváme a proč.
        * **💧 Likvidita:** Máme / nemáme na účtu dost peněz na včasné zaplacení faktur.
        * **💳 Zadluženost:** Náš dluh je bezpečný / rizikový.
        * **⚙️ Efektivita:** Využíváme majetek dobře / peníze se nám zasekávají ve skladu a u neplatičů.
        * **🚀 Doporučení:** Co konkrétně musíme zítra ráno udělat jinak.
        """)

        with st.container(border=True):
            st.markdown("#### 🤖 Generátor profi závěru")
            st.write("Vyber si aktuální stav tvé fiktivní firmy (třeba z předchozí kapitoly) a podívej se, jak by tvé hodnocení zapsal profesionální finanční ředitel.")
            
            col_g1, col_g2 = st.columns(2)
            with col_g1:
                gen_zisk = st.selectbox("1. Jak je na tom firma se ziskem?", [
                    "Tržby i zisk stabilně rostou.",
                    "Firma je v zisku, ale marže klesá.",
                    "Firma propadla do ztráty."
                ])
                gen_likvidita = st.selectbox("2. Co peníze a likvidita?", [
                    "Hotovosti je dostatek, závazky platíme včas.",
                    "Likvidita se zhoršuje, peníze chybí.",
                    "Hrozí okamžitá platební neschopnost!"
                ])
            with col_g2:
                gen_dluh = st.selectbox("3. Jaká je zadluženost?", [
                    "Zadlužení je nízké a bezpečné.",
                    "Dluh roste, ale zatím je zvládnutelný.",
                    "Firma je předlužena a dusí ji splátky."
                ])
                gen_sklad = st.selectbox("4. Co zásoby a zákazníci?", [
                    "Zákazníci platí včas, sklad se točí.",
                    "Peníze se začínají zasekávat ve skladu.",
                    "Zákazníci neplatí a zásoby leží ladem."
                ])

            st.markdown("##### 📄 Výsledný report pro majitele:")
            
            # Generování dynamického textu na základě výběru
            report_text = f"Firma aktuálně vykazuje smíšené výsledky. Z pohledu rentability {gen_zisk.lower().replace('.', '')}. "
            report_text += f"V oblasti cashflow {gen_likvidita.lower().replace('.', '')}, přičemž z hlediska cizích zdrojů platí, že {gen_dluh.lower().replace('.', '')}. "
            report_text += f"Když se podíváme na provozní aktivitu, vidíme, že {gen_sklad.lower().replace('.', '')}. "
            
            # Doporučení na základě nejhoršího problému
            if "Hrozí okamžitá" in gen_likvidita or "předlužena" in gen_dluh:
                doporuceni = "🚨 **Krizové doporučení:** Firma musí okamžitě zastavit zbytné výdaje, vyjednat s bankou odklad splátek a tvrdě vymáhat pohledávky. Jinak hrozí úpadek."
            elif "zasekávat ve skladu" in gen_sklad or "zhoršuje" in gen_likvidita:
                doporuceni = "⚠️ **Doporučení k optimalizaci:** Prioritou pro další kvartál je uvolnit zamrzlou hotovost. Navrhuji zavést slevy na staré zásoby, vyprodat sklad a zkrátit dobu splatnosti faktur pro naše odběratele."
            elif "ztráty" in gen_zisk:
                doporuceni = "⚠️ **Strategické doporučení:** Musíme přehodnotit byznys model. Doporučuji provést detailní analýzu nákladů (osekat fixní náklady) a případně zdražit klíčové produkty."
            else:
                doporuceni = "✅ **Doporučení pro růst:** Firma je ve výborné kondici. Doporučuji udržet stávající kurz, volnou hotovost reinvestovat do marketingu a zvážit bezpečné využití úvěru pro rychlejší expanzi."

            st.info(f"**Shrnutí:** {report_text}\n\n{doporuceni}")
# =========================================================================
    # 5.9 CASE STUDY: INFLUENCER JAKO FIRMA
    # =========================================================================
    elif selected_section_2.startswith("5.9"):
        import pandas as pd

        st.markdown("<div class='sub-section-header'>5. FINANČNÍ ŘÍZENÍ V PODNIKU</div>", unsafe_allow_html=True)
        st.markdown("## 5.9 Case study: Influencer jako firma")
        
        st.write(
            "Influencer, streamer, youtuber, tvůrce podcastu nebo správce komunitního profilu může na první pohled působit "
            "jen jako „člověk, co se točí na internetu“. Ve skutečnosti je to ale plnohodnotné podnikání s příjmy, náklady, "
            "smlouvami, daněmi a velkými riziky."
        )

        st.divider()

        tab_sim, tab_dane, tab_rizika = st.tabs([
            "🎮 1. Simulátor byznysu", 
            "⚖️ 2. Hra na účetního (Daně)", 
            "🔥 3. Zkouška ohněm (Rizika)"
        ])

        # --- TAB 1: SIMULÁTOR BYZNYSU ---
        with tab_sim:
            st.markdown("### 🎛️ Sestav si svůj online byznys")
            st.write("Nastav si měsíční příjmy a výdaje svého fiktivního profilu. Sleduj, jak se ti mění zisk.")

            col_p, col_n, col_v = st.columns(3)

            with col_p:
                st.markdown("#### 💰 Příjmy (Kč/měsíc)")
                p_spoluprace = st.slider("Placené spolupráce (Sponzoři)", 0, 150000, 45000, step=5000, key="inf_p1")
                p_reklama = st.slider("Reklama z platforem (YouTube/Twitch)", 0, 50000, 10000, step=1000, key="inf_p2")
                p_affil = st.slider("Affiliate odkazy (Provize z prodeje)", 0, 30000, 8000, step=1000, key="inf_p3")
                p_subs = st.slider("Předplatné (Herohero, Patreon)", 0, 100000, 12000, step=2000, key="inf_p4")
                p_merch = st.slider("Prodej vlastního merche/kurzů", 0, 80000, 0, step=5000, key="inf_p5")
                
                prijmy_celkem = p_spoluprace + p_reklama + p_affil + p_subs + p_merch

            with col_n:
                st.markdown("#### 💸 Náklady (Kč/měsíc)")
                n_technika = st.slider("Technika a software (Kamera, střih)", 0, 30000, 8000, step=1000, key="inf_n1")
                n_produkce = st.slider("Produkce (Studio, editor videa, cesty)", 0, 50000, 14000, step=1000, key="inf_n2")
                n_reklama = st.slider("Vlastní reklama a propagace", 0, 20000, 5000, step=1000, key="inf_n3")
                n_sluzby = st.slider("Účetní a právní služby", 0, 10000, 3000, step=500, key="inf_n4")
                
                naklady_celkem = n_technika + n_produkce + n_reklama + n_sluzby

            with col_v:
                st.markdown("#### 📊 Výsledovka")
                zisk_pred_zdanenim = prijmy_celkem - naklady_celkem
                
                st.metric("Celkové příjmy", f"{prijmy_celkem:,} Kč".replace(",", " "))
                st.metric("Celkové náklady", f"- {naklady_celkem:,} Kč".replace(",", " "))
                
                st.divider()
                if zisk_pred_zdanenim > 0:
                    st.metric("Zisk (Před zdaněním!)", f"{zisk_pred_zdanenim:,} Kč".replace(",", " "), "Ziskový měsíc")
                    st.success("Tohle vypadá jako solidní byznys. Nezapomeň ale, že z této částky ještě musíš zaplatit daně, sociální a zdravotní pojištění!")
                else:
                    st.metric("Zisk (Před zdaněním)", f"{zisk_pred_zdanenim:,} Kč".replace(",", " "), "- Ztráta", delta_color="inverse")
                    st.error("Jsi ve ztrátě! Takhle to dlouho nevydrží. Musíš buď získat víc sponzorů, nebo osekat náklady.")

            # Vizualizace struktury příjmů
            if prijmy_celkem > 0:
                st.markdown("##### Odkud plynou tvé peníze? (Diverzifikace)")
                chart_data = pd.DataFrame(
                    [p_spoluprace, p_reklama, p_affil, p_subs, p_merch],
                    index=["Spolupráce", "Reklama z videí", "Affiliate", "Předplatné", "Merch"],
                    columns=["Kč"]
                )
                st.bar_chart(chart_data.T)

        # --- TAB 2: HRA NA ÚČETNÍHO ---
        with tab_dane:
            st.markdown("### ⚖️ Daňová past: Co si mohu dát do nákladů?")
            st.write(
                "Ne každý osobní výdaj je automaticky nákladem podnikání. Aby šlo o daňově uznatelný náklad, "
                "musí **souviset s dosažením, zajištěním nebo udržením příjmů**. Zkus rozhodnout, co by ti u finančního úřadu prošlo."
            )

            with st.container(border=True):
                q1 = st.radio("1. Koupil sis nový iPhone za 35 000 Kč. Točíš na něj 90 % svých videí na TikTok.", 
                              ["Vyber odpověď...", "Ano, je to uznatelný náklad.", "Ne, je to osobní spotřeba."])
                if q1 == "Ano, je to uznatelný náklad.":
                    st.success("✅ Správně. Slouží k tvorbě tvého produktu (obsahu).")
                elif q1 == "Ne, je to osobní spotřeba.":
                    st.error("❌ Špatně. Pokud ho prokazatelně používáš k tvorbě obsahu, do nákladů (nebo do majetku) jít může.")

                st.divider()

                q2 = st.radio("2. Koupil sis herní konzoli za 15 000 Kč, abys na ní hrál o víkendu po večerech s kamarády. Nejsi herní streamer (děláš fitness).", 
                              ["Vyber odpověď...", "Ano, je to uznatelný náklad.", "Ne, je to osobní spotřeba."])
                if q2 == "Ne, je to osobní spotřeba.":
                    st.success("✅ Přesně tak! Finanční úřad by ti to vyhodil. Nesouvisí to s tvým fitness podnikáním.")
                elif q2 == "Ano, je to uznatelný náklad.":
                    st.error("❌ Kdepak. Fitness streamer těžko obhájí nákup herní konzole pro volný čas jako nutnost pro svůj byznys.")
                
                st.divider()

                q3 = st.radio("3. Zaplatil jsi 5 000 Kč za kampaň na Instagramu, která láká lidi na tvůj nový e-book.", 
                              ["Vyber odpověď...", "Ano, je to uznatelný náklad.", "Ne, je to osobní spotřeba."])
                if q3 == "Ano, je to uznatelný náklad.":
                    st.success("✅ Ano! Je to klasický výdaj na reklamu a propagaci za účelem dosažení zisku.")
                elif q3 == "Ne, je to osobní spotřeba.":
                    st.error("❌ Špatně. Reklama propagující tvůj komerční produkt je jasný uznatelný náklad.")

            st.markdown("""
            <div class="box-red">
                <b>⚠️ Důležité:</b> Mnoho začínajících tvůrců míchá firemní a osobní peníze. Když si z firemního účtu platí osobní obědy a dovolené (které nevydávají za tvorbu obsahu), zadělávají si na obrovský problém s finančním úřadem.
            </div>
            """, unsafe_allow_html=True)

        # --- TAB 3: ZKOUŠKA OHNĚM ---
        with tab_rizika:
            st.markdown("### 🔥 Finanční stabilita pod palbou")
            st.write(
                "Nyní otestujeme tvůj byznys (ten, co sis naklikal v první záložce). Co se stane, když přijde krize? "
                "Je tvůj příjem stabilní, nebo visí na vlásku jediné spolupráce?"
            )

            scenar = st.selectbox("Vyber krizový scénář:", [
                "Všechno běží podle plánu (Základní stav)",
                "Scénář A: Změna algoritmu YouTube/Tiktoku (Ztráta dosahu)",
                "Scénář B: Hlavní sponzor odstoupil",
                "Scénář C: Vyhoření (Burnout) – měsíc netvoříš"
            ])

            # Původní hodnoty ze simulátoru
            krizovy_prijem = prijmy_celkem
            krizovy_naklad = naklady_celkem
            popis_krize = ""

            if scenar == "Scénář A: Změna algoritmu YouTube/Tiktoku (Ztráta dosahu)":
                krizovy_prijem = p_spoluprace + (p_reklama * 0.2) + (p_affil * 0.3) + p_subs + (p_merch * 0.5)
                popis_krize = "Algoritmus tě přestal doporučovat. Zhlédnutí klesla o 80 %. Příjmy z platformových reklam a affiliate prokliků se propadly. Merch se prodává hůř, protože na něj nekouká tolik lidí. Předplatitelé a dlouhodobí sponzoři tě naštěstí zatím drží."
            
            elif scenar == "Scénář B: Hlavní sponzor odstoupil":
                krizovy_prijem = (p_spoluprace * 0.1) + p_reklama + p_affil + p_subs + p_merch
                popis_krize = "Tvůj hlavní partner změnil marketingovou strategii a neprodloužil smlouvu. Přišel jsi o 90 % příjmů ze spoluprací ze dne na den. Ostatní příjmy zůstávají."
            
            elif scenar == "Scénář C: Vyhoření (Burnout) – měsíc netvoříš":
                krizovy_prijem = 0 + 0 + (p_affil * 0.5) + (p_subs * 0.8) + (p_merch * 0.3)
                # Náklady ale běží dál!
                popis_krize = "Nemůžeš natáčet. Spolupráce stojí, nová reklama nenabíhá. Zůstávají ti jen pasivní příjmy (staré affiliate odkazy) a věrní předplatitelé (i když jich 20 % odešlo kvůli neaktivitě). ALE POZOR: Fixní náklady (nájem studia, software, účetní) musíš zaplatit stejně!"

            novy_zisk = krizovy_prijem - krizovy_naklad

            st.info(f"**Co se stalo:** {popis_krize}" if popis_krize else "Zatím je klid a peníze se sypou.")

            col_k1, col_k2, col_k3 = st.columns(3)
            col_k1.metric("Příjmy po krizi", f"{krizovy_prijem:,.0f} Kč".replace(",", " "))
            col_k2.metric("Náklady (zůstávají)", f"- {krizovy_naklad:,.0f} Kč".replace(",", " "))
            
            if novy_zisk > 0:
                col_k3.metric("Nový zisk", f"{novy_zisk:,.0f} Kč".replace(",", " "), f"{novy_zisk - zisk_pred_zdanenim:,.0f} Kč (Oproti plánu)")
                st.success("✅ Přežil jsi! Tvůj byznys je dostatečně diverzifikovaný (stojí na více nohách), abys ustál i velký výpadek.")
            else:
                col_k3.metric("Nový zisk", f"{novy_zisk:,.0f} Kč".replace(",", " "), f"{novy_zisk - zisk_pred_zdanenim:,.0f} Kč", delta_color="inverse")
                st.error("🚨 Zkrachoval jsi! Tvé příjmy nedokázaly pokrýt ani běžné náklady. Pokud nemáš finanční rezervu vytvořenou z minulých měsíců, končíš s podnikáním.")

            st.markdown("""
            <div class="box-purple">
                <b>🧠 Poučení z analýzy:</b> Influencer musí mít vytvořenou finanční rezervu (alespoň na 3–6 měsíců života) a nesmí být závislý jen na jedné sociální síti nebo jednom sponzorovi.
            </div>
            """, unsafe_allow_html=True)
# =========================================================================
    # 5.10 DIGITÁLNÍ GENERACE A FINANČNÍ ŘÍZENÍ
    # =========================================================================
    elif selected_section_2.startswith("5.10"):
        st.markdown("<div class='sub-section-header'>5. FINANČNÍ ŘÍZENÍ V PODNIKU</div>", unsafe_allow_html=True)
        st.markdown("## 5.10 Digitální generace a finanční řízení")
        
        st.write(
            "Dnešní podnikání je neuvěřitelně rychlé, řízené daty a často absolutně závislé na digitálních platformách. "
            "To přináší obrovské příležitosti k raketovému růstu, ale i zcela nová finanční rizika, která dřívější podnikatelé neznali."
        )

        st.markdown("### 🔍 Detektor skrytých rizik")
        st.write("Vyber si moderní byznysovou situaci, která na první pohled vypadá jako splněný sen, a odhal, jaké temné finanční riziko se za ní skrývá.")

        scenare = {
            "🚀 E-shop raketově roste díky virálu na TikToku": {
                "otazka": "Má firma dost zásob a peněz na masivní expedici?",
                "riziko": "Růst objednávek může předběhnout cashflow (firma musí platit za dodávky, krabice a poštu dřív, než jí dorazí všechny peníze z dobírek). Úspěch ji může paradoxně přivést k bankrotu!"
            },
            "📸 Influencer získal obří exkluzivní spolupráci": {
                "otazka": "Co když značka za půl roku smlouvu neprodlouží?",
                "riziko": "Extrémní závislost na jednom zdroji příjmu. Pokud influencer přizpůsobí své fixní výdaje (hypotéka, drahé auto) tomuto příjmu, výpadek ho okamžitě zničí."
            },
            "🦄 Aplikace (Startup) získala miliony od investora": {
                "otazka": "Jak dlouho vydrží peníze při současném tempu utrácení (tzv. Burn rate)?",
                "riziko": "Rychlé spálení kapitálu za drahé kanceláře a marketing bez odpovídajícího růstu tržeb. Až peníze dojdou, investor už další nedá."
            },
            "☕ Hipster kavárna má neustále plno": {
                "otazka": "Kolik peněz skutečně zůstane po zaplacení nájmu, baristů, energií a prémiové kávy?",
                "riziko": "Vysoké tržby nemusí znamenat vysoký zisk. Nízké marže u produktů s vysokými fixními náklady znamenají, že se majitel dře, ale firma nevydělává."
            },
            "🏢 Firma dodává velké korporaci na fakturu": {
                "otazka": "Kdy peníze skutečně dorazí na účet?",
                "riziko": "Pozdní platby. Korporace mají často splatnost 60 až 90 dní. Malá firma tak úvěruje obří korporaci a sama nemá na výplaty pro své lidi."
            }
        }

        vybrany_scenar = st.selectbox("Vyber situaci k analýze:", ["Vyber situaci..."] + list(scenare.keys()))

        if vybrany_scenar != "Vyber situaci...":
            data_scenare = scenare[vybrany_scenar]
            st.markdown(f"#### Analýza: {vybrany_scenar}")
            st.info(f"🤔 **Finanční otázka manažera:** {data_scenare['otazka']}")
            st.error(f"🚨 **Skryté riziko:** {data_scenare['riziko']}")


    # =========================================================================
    # 5.11 PRAKTICKÁ AKTIVITA: FINANČNÍ MANAŽER NA 45 MINUT
    # =========================================================================
    elif selected_section_2.startswith("5.11"):
        st.markdown("<div class='sub-section-header'>5. FINANČNÍ ŘÍZENÍ V PODNIKU</div>", unsafe_allow_html=True)
        st.markdown("## 5.11 Praktická aktivita: Finanční manažer na 45 minut")
        
        st.markdown("""
        <div class="box-purple">
            <b>🧪 Aktivita: Audit finančního zdraví podniku</b><br>
            Pracujte ve dvojici nebo skupině. Vaším úkolem je navrhnout modelovou firmu (nebo si vzít existující projekt) a provést její kompletní audit. Využijte tento digitální pracovní sešit.
        </div>
        """, unsafe_allow_html=True)

        tab1, tab2, tab3, tab4 = st.tabs(["📝 Krok 1: Podnik", "🔢 Krok 2: Čísla", "🧮 Krok 3: Výpočty", "📄 Krok 4: Závěr"])

        with tab1:
            st.markdown("### Krok 1: Popište svůj podnik")
            st.write("Vyberte si modelovou firmu (např. e-shop, kavárnu, barber shop, grafické studio, studentský merch, fitness trenéra, food truck, youtubera nebo aplikaci).")
            
            p_nazev = st.text_input("Název vaší firmy:")
            p_co = st.text_input("Co přesně prodáváte?")
            p_komu = st.text_input("Komu to prodáváte (cílová skupina)?")
            p_prijmy = st.text_input("Jak z toho máte příjmy (jednorázový prodej, předplatné, reklama)?")
            p_naklady = st.text_area("Jaké jsou vaše 3 největší náklady?")

        with tab2:
            st.markdown("### Krok 2: Doplňte finanční čísla")
            st.write("Dohodněte se na odhadovaných číslech pro 1 kalendářní rok. Zkuste být realističtí.")
            
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("**Výsledovka**")
                v_trzby = st.number_input("Tržby celkem [Kč]", value=500000, step=50000)
                v_naklady = st.number_input("Náklady celkem [Kč]", value=400000, step=50000)
                v_zisk = v_trzby - v_naklady
                st.metric("Automatický Zisk [Kč]", f"{v_zisk:,}".replace(",", " "))
            
            with c2:
                st.markdown("**Rozvaha a Cashflow**")
                v_aktiva = st.number_input("Aktiva (Celkový majetek) [Kč]", value=300000, step=10000)
                v_vk = st.number_input("Vlastní kapitál [Kč]", value=200000, step=10000)
                v_cz = st.number_input("Cizí zdroje (Dluhy) [Kč]", value=100000, step=10000)
                
                st.divider()
                v_oa = st.number_input("Oběžná aktiva celkem [Kč]", value=150000, step=10000)
                v_penize = st.number_input("Z toho Peníze na účtu [Kč]", value=50000, step=5000)
                v_pohl = st.number_input("Z toho Pohledávky [Kč]", value=40000, step=5000)
                v_kz = st.number_input("Krátkodobé závazky [Kč]", value=80000, step=5000)

        with tab3:
            st.markdown("### Krok 3: Automatické výpočty (Analýza)")
            st.write("Aplikace za vás nyní spočítá klíčové ukazatele na základě zadaných čísel z Kroku 2.")
            
            def safe_div(a, b):
                return a / b if b != 0 else 0
                
            ros = safe_div(v_zisk, v_trzby) * 100
            roa = safe_div(v_zisk, v_aktiva) * 100
            roe = safe_div(v_zisk, v_vk) * 100
            bl = safe_div(v_oa, v_kz)
            ol = safe_div(v_penize, v_kz)
            zadl = safe_div(v_cz, v_aktiva) * 100
            inkaso = safe_div(v_pohl, v_trzby) * 365
            
            col_a1, col_a2 = st.columns(2)
            col_a1.metric("ROS (Rentabilita tržeb)", f"{ros:.1f} %")
            col_a1.metric("ROA (Rentabilita aktiv)", f"{roa:.1f} %")
            col_a1.metric("ROE (Rentabilita vl. kapitálu)", f"{roe:.1f} %")
            
            col_a2.metric("Běžná likvidita", f"{bl:.2f}")
            col_a2.metric("Okamžitá likvidita", f"{ol:.2f}")
            col_a2.metric("Celková zadluženost", f"{zadl:.1f} %")
            col_a2.metric("Doba inkasa pohledávek", f"{inkaso:.0f} dní")

        with tab4:
            st.markdown("### Krok 4: Manažerský závěr")
            st.write("Prohlédněte si spočítané ukazatele a napište slovní hodnocení vaší firmy.")
            
            z_silna = st.text_area("1. Co je podle čísel silná stránka firmy?")
            z_slaba = st.text_area("2. Co je naopak slabina nebo problém?")
            z_riziko = st.text_area("3. Jaké riziko hrozí do 3 měsíců (např. ohledně hotovosti)?")
            z_doporuceni = st.text_area("4. Jaké jedno opatření byste doporučili vedení firmy udělat ihned?")
            
            if st.button("Generovat finální report pro učitele/investora"):
                st.success("Tento report si můžete zkopírovat nebo přečíst třídě:")
                st.markdown(f"""
                **Analýza firmy:** {p_nazev if p_nazev else 'Nezadáno'}  
                **Byznys model:** Prodáváme {p_co} pro {p_komu}.
                
                **Klíčové metriky:** ROS = {ros:.1f} %, Zadluženost = {zadl:.1f} %, Likvidita = {bl:.2f}.
                
                **Manažerské shrnutí:**  
                Silnou stránkou je *{z_silna if z_silna else '...'}*. Naopak bojujeme s *{z_slaba if z_slaba else '...'}*.
                V nejbližších měsících si musíme dát pozor na *{z_riziko if z_riziko else '...'}*.
                Naše doporučení pro majitele zní: **{z_doporuceni if z_doporuceni else '...'}**
                """)


    # =========================================================================
    # 5.12 SHRNUTÍ A AI MENTORING
    # =========================================================================
    elif selected_section_2.startswith("5.12"):
        st.markdown("<div class='sub-section-header'>5. FINANČNÍ ŘÍZENÍ V PODNIKU</div>", unsafe_allow_html=True)
        st.markdown("## 5.12 Shrnutí: co si odnést")
        
        st.write("Finanční řízení je mozek celé firmy. Zhodnoť si, co už ovládáš. Odškrtni si vše, co jsi z této kapitoly pochopil/a.")

        # Interaktivní checklist pokroku
        points = [
            "Finanční řízení pomáhá firmě přežít, růst a rozhodovat podle dat.",
            "Zisk NEZNAMENÁ automaticky peníze na účtu (Cashflow je král).",
            "Rozvaha ukazuje, co firma má a z čeho to financuje (Zdroje).",
            "Výkaz zisku a ztráty ukazuje, zda firma vůbec vydělává.",
            "Finanční analýza převádí účetní čísla na srozumitelné závěry o zdraví firmy.",
            "Nejčastější ukazatele sledují rentabilitu (zisk), likviditu (hotovost), zadluženost a aktivitu.",
            "Finanční zdraví firmy zajímá všechny: majitele, banky, investory i zaměstnance.",
            "Smyslem analýzy není „vyplnit vzorce“, ale pochopit, co se ve firmě děje a jak se rozhodnout dál."
        ]
        
        checked_count = 0
        for i, point in enumerate(points):
            if st.checkbox(point, key=f"sum_{i}"):
                checked_count += 1
                
        progress = int((checked_count / len(points)) * 100)
        st.progress(checked_count / len(points))
        st.caption(f"Tvé mistrovství ve financích: {progress} %")
        
        if progress == 100:
            st.balloons()
            st.success("Skvělá práce! Rozumíš základům finančního řízení jako pravý CFO.")

        st.divider()

        st.markdown("### 🤖 AI Mentoring: Tvůj osobní analytik")
        st.write(
            "Chceš si finanční analýzu procvičit na další firmě, ale nechce se ti to počítat? Zkopíruj si tento prompt "
            "a vlož ho do ChatGPT, Clauda nebo Gemini. AI se stane tvým osobním tutorem."
        )

        ai_prompt = """Pomoz mi udělat jednoduchou finanční analýzu fiktivní firmy. 
Nejdřív se mě zeptej na tržby, náklady, zisk, aktiva, vlastní kapitál, cizí zdroje, peníze, zásoby, pohledávky a krátkodobé závazky. 
Až ti data zadám, spočítej ROS, ROA, ROE, běžnou likviditu, okamžitou likviditu, celkovou zadluženost a dobu inkasa pohledávek. 
Nakonec mi napiš závěr jako pro studenta střední školy a doporuč jedno opatření."""

        st.code(ai_prompt, language="text")
        
        st.markdown("""
        <div style="font-size: 0.9em; color: #555;">
            <i>Tip: Stačí kliknout na ikonku kopírování vpravo nahoře v rámečku a můžeš prompt rovnou vložit do svého oblíbeného AI nástroje.</i>
        </div>
        """, unsafe_allow_html=True)
# =========================================================================
    # KAPITOLA 6: INTERAKTIVNÍ VRSTVA CELÉ KAPITOLY (PRACOVNÍ SEŠIT)
    # =========================================================================
    elif selected_section_2.startswith("6"):
        
        st.markdown("<div class='sub-section-header'>6. INTERAKTIVNÍ CVIČENÍ A ÚKOLY</div>", unsafe_allow_html=True)
        st.markdown("## 6. Interaktivní pracovní sešit")
        
        st.write(
            "Tato sekce neslouží jako „test na známku“. Je to tvůj digitální pracovní sešit. "
            "Finance si tu převedeš do vlastního života, naučíš se rozhodovat, bránit se podvodům a pochopit, "
            "jak firmy a algoritmy cílí na tvou peněženku."
        )

        # Navigace uvnitř pracovní sekce (přidán key pro jistotu paměti)
        workbook_section = st.radio("Vyber si aktivitu:", [
            "🧭 Startovací diagnostika",
            "🔐 Bezpečnostní challenge (Poznej podvod)",
            "📱 Algoritmy utrácení",
            "🛟 Simulátor nečekané události",
            "🧮 Můj první byznys (Bod zvratu)",
            "✅ Exit ticket (Co si odnáším)"
        ], horizontal=True, key="wb_nav")

        st.divider()

        # --- AKTIVITA 1: DIAGNOSTIKA ---
        if workbook_section == "🧭 Startovací diagnostika":
            st.markdown("### 🧭 Startovací diagnostika: Co už o financích vím?")
            st.write("Vyplň před začátkem studia. Ohodnoť se na škále 0 (Nevím nic) až 10 (Umím to vysvětlit tátovi).")

            with st.container(border=True):
                st.slider("Jak dobře chápu rozdíl mezi ČNB a běžnou komerční bankou?", 0, 10, 5, key="diag_1")
                st.slider("Dokážu poznat rizikovou finanční nabídku (podvod)?", 0, 10, 5, key="diag_2")
                st.slider("Rozumím, proč může být firma zisková, ale přesto nemá na účtu peníze na výplaty?", 0, 10, 5, key="diag_3")
                st.slider("Vím, co přesně znamená hrubá a čistá mzda?", 0, 10, 5, key="diag_4")

            st.info("💡 **Úkol pro tebe:** Po prostudování všech kapitol se sem vrať. Pokud se tvé skóre posunulo z 5 na 9, kapitola splnila svůj účel!")

        # --- AKTIVITA 2: POZNEJ PODVOD ---
        elif workbook_section == "🔐 Bezpečnostní challenge (Poznej podvod)":
            st.markdown("### 🔐 Bezpečnostní challenge: Poznej finanční podvod (Phishing / Scam)")
            st.write(
                "Představ si, že ti na mobil pípnou následující zprávy. Pracuj ve dvojici a u každé zprávy rozhodni, "
                "zda je to bezpečná notifikace, nebo nebezpečný podvod."
            )

            zpravy = [
                {"text": "Vaše karta byla zablokována. Klikněte na tento odkaz (bit.ly/banka-overeni) a přihlaste se pro odblokování.", "spravne": "Nebezpečné", "vysvetleni": "Banka NIKDY neposílá odkazy na přihlášení přes SMS nebo e-mail. Je to phishing, který chce ukrást tvé heslo."},
                {"text": "Dobrý den, jsem z bezpečnostního oddělení vaší banky. Na vašem účtu je podezřelá transakce. Nadiktujte mi prosím kód, který vám právě přišel v SMS.", "spravne": "Nebezpečné", "vysvetleni": "Vishing (hlasový podvod). Banka nikdy nechce diktovat kódy po telefonu. Útočník se právě snaží zadat platbu a potřebuje tvé potvrzení."},
                {"text": "Vaše trvalá platba za nájem (8 500 Kč) neproběhla kvůli nedostatku zůstatku.", "spravne": "Bezpečné", "vysvetleni": "Standardní notifikace. Neobsahuje žádný odkaz, nevyvolává nátlak, jen tě informuje."},
                {"text": "Garantovaný výnos 20 % měsíčně! Investujte do nové AI kryptoměny. Akce končí za 3 hodiny!", "spravne": "Nebezpečné", "vysvetleni": "Klasický scam. Jakmile někdo slibuje obří výnos, garantuje ho a navíc vytváří časový nátlak (FOMO), jde vždy o podvod."}
            ]

            for i, zprava in enumerate(zpravy):
                with st.chat_message("user", avatar="📱"):
                    st.write(zprava["text"])
                    volba = st.radio(f"Hodnocení zprávy č. {i+1}:", ["Vyber hodnocení...", "Bezpečné", "Podezřelé", "Nebezpečné"], key=f"msg_sec_{i}")
                    
                    if volba != "Vyber hodnocení...":
                        if volba == zprava["spravne"] or (volba == "Podezřelé" and zprava["spravne"] == "Nebezpečné"):
                            st.success(f"✅ Správný odhad! **Varovný signál:** {zprava['vysvetleni']}")
                        else:
                            st.error(f"❌ Tohle by tě stálo peníze! **Proč je to špatně:** {zprava['vysvetleni']}")

        # --- AKTIVITA 3: ALGORITMY UTRÁCENÍ ---
        elif workbook_section == "📱 Algoritmy utrácení":
            st.markdown("### 🧠 Algoritmy utrácení: Kdo mě ovlivňuje?")
            st.write(
                "Vyber jeden svůj nedávný nákup (např. skin ve hře, mikinu, drahý drink), ke kterému tě navedla reklama, "
                "sleva, influencer nebo tlak okolí."
            )

            with st.container(border=True):
                st.text_input("1. Co jsi koupil/a?", key="alg_1")
                
                st.selectbox("2. Jakou emoci nebo taktiku na tebe nabídka použila?", [
                    "FOMO (Strach, že o něco přijdu - 'Akce končí za hodinu!')",
                    "Společenský status ('Budu vypadat dobře před ostatními')",
                    "Pohodlí ('Klikni a koupíš hned bez přemýšlení')",
                    "Autoritu ('Oblíbený influencer to doporučil')"
                ], key="alg_2")
                
                st.radio("3. Koupil/a bys to, i kdyby to nebylo ve slevě?", ["Ano, potřeboval/a jsem to.", "Spíše ne, nechal/a jsem se strhnout."], key="alg_3")
                
                st.markdown("#### Přepočet na hodiny života")
                cena = st.number_input("Kolik to stálo (Kč)?", min_value=0, value=500, step=50, key="alg_cena")
                mzda = st.number_input("Tvá reálná (nebo vysněná) hodinová mzda z brigády (Kč/h)?", min_value=1, value=150, step=10, key="alg_mzda")
                if mzda > 0:
                    hodiny = cena / mzda
                    st.info(f"💡 Tento nákup tě stál **{hodiny:.1f} hodin čistého času** (práce). Stálo ti to za to?")

        # --- AKTIVITA 4: SIMULÁTOR REZERVY ---
        elif workbook_section == "🛟 Simulátor nečekané události":
            st.markdown("### 🛟 Rezerva: Simulátor nečekané události")
            st.write("Finanční rezerva funguje jako airbag v autě. Otestuj tvůj (fiktivní) rozpočet.")

            prijem = 18000
            vylohy = 13500
            rezerva = 4000
            volne_mesicne = prijem - vylohy

            col1, col2, col3 = st.columns(3)
            col1.metric("Měsíční příjem", f"{prijem} Kč")
            col2.metric("Nutné výdaje", f"{vylohy} Kč")
            col3.metric("Pohotovostní rezerva", f"{rezerva} Kč")

            st.write(f"Každý měsíc ti po zaplacení nutných věcí zbude **{volne_mesicne} Kč**. Našetřeno máš **{rezerva} Kč**.")

            udalost = st.selectbox("Co se právě stalo?", [
                "Zvol krizový scénář...",
                "Spadl ti mobil a rozbilo se sklo (Oprava: 3 500 Kč)",
                "Kvůli zkouškám/nemoci jsi přišel o 2 týdny brigády (Ztráta: 4 000 Kč)",
                "Přišel nedoplatek za energie a internet na bytě (Výdaj: 2 800 Kč)"
            ], key="sim_udalost")

            if udalost != "Zvol krizový scénář...":
                if "mobil" in udalost:
                    naklad = 3500
                elif "nemoci" in udalost:
                    naklad = 4000
                else:
                    naklad = 2800

                zbytek = rezerva - naklad
                
                st.divider()
                st.markdown("#### Následky")
                
                if zbytek >= 0:
                    st.success(f"✅ Tvůj airbag zafungoval! Zaplatil jsi {naklad} Kč z rezervy. Zbylo ti na ní {zbytek} Kč.")
                    obnova = naklad / volne_mesicne
                    import math
                    st.info(f"⏱️ Při tvém tempu spoření ({volne_mesicne} Kč měsíčně) potrvá **{math.ceil(obnova)} měsíce**, než rezervu znovu doplníš.")
                else:
                    st.error(f"🚨 Tvůj airbag praskl! Tvá rezerva nestačila. Na zaplacení ti **chybí {abs(zbytek)} Kč**.")
                    st.warning("⚠️ Jak to vyřešíš? Budeš si muset půjčit nevýhodně, nebo požádat rodiče?")

        # --- AKTIVITA 5: BOD ZVRATU (OPRAVENO) ---
        elif workbook_section == "🧮 Můj první byznys (Bod zvratu)":
            st.markdown("### 🧮 Podnikové finance: Bod zvratu na vlastním nápadu")
            st.write(
                "Vymysli jednoduchý produkt: školní merch, tisk samolepek, doučování... "
                "Spočítej si, kolik jich musíš prodat, abys pokryl náklady."
            )

            with st.container(border=True):
                produkt = st.text_input("Co budeš prodávat?", "Školní plátěná taška (Merch)", key="bz_produkt")
                
                c1, c2 = st.columns(2)
                # Oprava: min_value nastavena na 1, aby šly zadávat i velmi levné produkty (např. samolepky za 10 Kč)
                s_cena = c1.number_input("Prodejní cena za 1 ks [Kč]", min_value=1, value=300, step=10, key="bz_cena")
                s_vn = c2.number_input("Variabilní náklad na 1 ks (Nákup materiálu) [Kč]", min_value=1, value=150, step=10, key="bz_vn")
                s_fn = st.number_input("Fixní náklady celkem (E-shop, reklama, design) [Kč]", min_value=0, value=3000, step=500, key="bz_fn")

                if s_cena <= s_vn:
                    st.error("Chyba! Prodejní cena musí být vyšší než variabilní náklad na kus, jinak proděláváš už při výrobě.")
                else:
                    marze = s_cena - s_vn
                    bep = s_fn / marze
                    
                    import math
                    bep_kusy = math.ceil(bep)
                    
                    st.success(f"🎯 **Tvá marže je {marze} Kč z každého kusu.**")
                    st.info(f"🚀 **Bod zvratu:** Musíš prodat **{bep_kusy} kusů** ({produkt}), abys pokryl/a fixní náklady. Od kusu číslo {bep_kusy + 1} začínáš generovat čistý zisk!")

# --- AKTIVITA 6: EXIT TICKET (ZABALENO DO FORMULÁŘE) ---
        elif workbook_section == "✅ Exit ticket (Co si odnáším)":
            st.markdown("### ✅ Exit ticket: Závěrečná reflexe")
            st.write("Představ si, že bys měl/a předstoupit před třídu a shrnout, co sis z financí odnesl/a. Vyplň tyto body:")

            # Zabalíme to do st.form – tím se zabrání nechtěnému načítání stránky
            with st.form("exit_ticket_form"):
                t1 = st.text_area("1. Jedna věc, kterou jsem pochopil/a nově:")
                t2 = st.text_area("2. Jedno finanční rozhodnutí, u kterého příště zpomalím:")
                t3 = st.text_area("3. Jedna otázka, kterou bych položil/a finančnímu poradci nebo podnikateli:")

                # Tlačítko pro odeslání formuláře
                submitted = st.form_submit_button("Uložit moji reflexi")

                if submitted:
                    if t1.strip() != "" and t2.strip() != "" and t3.strip() != "":
                        st.balloons()
                        st.success("Tvá reflexe je úspěšně uložená. Gratulujeme k úspěšnému absolvování bloku o financích!")
                    else:
                        st.warning("Zkus prosím vyplnit všechna tři pole, ať je tvá reflexe kompletní.")
# =========================================================================
    # KAPITOLA 7: AKTIVITA - OPTIMALIZACE VÝDAJŮ
    # =========================================================================
    elif selected_section_2.startswith("7"):
        st.markdown("<div class='sub-section-header'>7. PRAKTICKÁ AKTIVITA</div>", unsafe_allow_html=True)
        st.markdown("## 7. Aktivita: Optimalizace rozpočtu")
        
        st.write(
            "Finanční zdraví nezačíná tím, že přestaneš utrácet za všechno, co tě baví. "
            "Jde o to najít místa, kde peníze unikají zbytečně. Zkusíme si to na tvém (nebo fiktivním) rozpočtu."
        )

        st.markdown("""
        <div class="box-purple">
            <b>✍️ Mini úkol:</b> Sepiš tři pravidelné výdaje, které by šly snížit bez výrazného poklesu kvality života. U každého navrhni konkrétní změnu a podívej se, co to udělá s tvým rozpočtem za celý rok.
        </div>
        """, unsafe_allow_html=True)

        with st.form("form_uspory"):
            c1, c2, c3, c4 = st.columns([3, 2, 3, 2])
            c1.markdown("**Název výdaje** (např. Předplatné, Káva)")
            c2.markdown("**Původní cena měsíčně**")
            c3.markdown("**Jak to změním?** (např. Zruším, udělám doma)")
            c4.markdown("**Nová cena měsíčně**")

            # Položka 1
            v1_nazev = c1.text_input("Výdaj 1", key="v1_n", label_visibility="collapsed")
            v1_stara = c2.number_input("Cena 1", min_value=0, value=300, step=50, key="v1_s", label_visibility="collapsed")
            v1_zmena = c3.text_input("Změna 1", key="v1_z", label_visibility="collapsed")
            v1_nova = c4.number_input("Nová cena 1", min_value=0, value=0, step=50, key="v1_no", label_visibility="collapsed")

            # Položka 2
            v2_nazev = c1.text_input("Výdaj 2", key="v2_n", label_visibility="collapsed")
            v2_stara = c2.number_input("Cena 2", min_value=0, value=800, step=50, key="v2_s", label_visibility="collapsed")
            v2_zmena = c3.text_input("Změna 2", key="v2_z", label_visibility="collapsed")
            v2_nova = c4.number_input("Nová cena 2", min_value=0, value=400, step=50, key="v2_no", label_visibility="collapsed")

            # Položka 3
            v3_nazev = c1.text_input("Výdaj 3", key="v3_n", label_visibility="collapsed")
            v3_stara = c2.number_input("Cena 3", min_value=0, value=1200, step=50, key="v3_s", label_visibility="collapsed")
            v3_zmena = c3.text_input("Změna 3", key="v3_z", label_visibility="collapsed")
            v3_nova = c4.number_input("Nová cena 3", min_value=0, value=800, step=50, key="v3_no", label_visibility="collapsed")

            submitted = st.form_submit_button("Spočítat moji roční úsporu")

            if submitted:
                uspora_mesic = (v1_stara - v1_nova) + (v2_stara - v2_nova) + (v3_stara - v3_nova)
                uspora_rok = uspora_mesic * 12

                st.divider()
                if uspora_rok > 0:
                    st.success("Tohle je síla drobných změn! 🎉")
                    col_a, col_b = st.columns(2)
                    col_a.metric("Měsíční úspora", f"{uspora_mesic:,} Kč".replace(",", " "))
                    col_b.metric("Ušetřeno za 1 rok", f"{uspora_rok:,} Kč".replace(",", " "))
                    st.info(f"💡 Za ušetřených **{uspora_rok:,} Kč** už by se dalo pořídit něco mnohem hodnotnějšího (investice, cestování, vzdělání), než byly původní výdaje.")
                else:
                    st.warning("Zatím to nevypadá na žádnou úsporu. Zkus navrhnout radikálnější změnu v kolonce 'Nová cena'.")

    # =========================================================================
    # KAPITOLA 8: SLOVNÍK CIZÍCH POJMŮ
    # =========================================================================
    elif selected_section_2.startswith("8"):
        import pandas as pd
        import random
        
        st.markdown("<div class='sub-section-header'>8. ZÁVĚREČNÝ PŘEHLED</div>", unsafe_allow_html=True)
        st.markdown("## 8. Slovník cizích pojmů")
        
        st.write(
            "Finanční svět má svůj vlastní jazyk. Tady najdeš rychlý překlad do lidštiny. "
            "Pojmy si můžeš vyhledat v tabulce, nebo si níže vyzkoušet generátor kartiček."
        )

        slovnik_data = [
            {"Pojem": "Aktiva", "Vysvětlení": "Majetek firmy nebo člověka; například peníze, zásoby, budovy, stroje, pohledávky nebo investice."},
            {"Pojem": "Akcie", "Vysvětlení": "Cenný papír představující podíl na akciové společnosti. Vlastník akcie se stává akcionářem."},
            {"Pojem": "Akcionář", "Vysvětlení": "Vlastník akcie, tedy člověk nebo instituce, která vlastní podíl ve firmě."},
            {"Pojem": "Bankovní licence", "Vysvětlení": "Povolení, které musí mít instituce, aby mohla působit jako banka."},
            {"Pojem": "Blockchain", "Vysvětlení": "Sdílený digitální záznam transakcí, který je rozdělen do bloků a zabezpečen pravidly sítě."},
            {"Pojem": "Bonita", "Vysvětlení": "Schopnost klienta splácet úvěr. Banka ji posuzuje podle příjmů, výdajů, dluhů a platební historie."},
            {"Pojem": "Broker", "Vysvětlení": "Zprostředkovatel, přes kterého může investor nakupovat a prodávat investiční nástroje."},
            {"Pojem": "Burza", "Vysvětlení": "Organizovaný trh, kde se podle pravidel obchoduje například s akciemi, dluhopisy nebo fondy."},
            {"Pojem": "Cashflow", "Vysvětlení": "Tok peněz. Ukazuje, kolik peněz skutečně přišlo a odešlo."},
            {"Pojem": "Cenný papír", "Vysvětlení": "Listina nebo digitální záznam, se kterým jsou spojena určitá práva (podíl ve firmě, splacení dluhu)."},
            {"Pojem": "ČNB", "Vysvětlení": "Česká národní banka. Centrální banka ČR, která pečuje o měnovou a finanční stabilitu."},
            {"Pojem": "Deficit", "Vysvětlení": "Schodek. Situace, kdy výdaje převyšují příjmy."},
            {"Pojem": "Diverzifikace", "Vysvětlení": "Rozložení peněz do více investic, aby člověk nebyl závislý jen na jednom aktivu (Nedávej všechna vejce do jednoho košíku)."},
            {"Pojem": "Dluhopis", "Vysvětlení": "Cenný papír, kterým si emitent půjčuje peníze od investorů a slibuje jejich splacení + úrok."},
            {"Pojem": "Emitent", "Vysvětlení": "Ten, kdo vydává cenný papír, například stát, obec, banka nebo firma."},
            {"Pojem": "Fintech", "Vysvětlení": "Spojení financí a technologií. Moderní finanční služby a aplikace."},
            {"Pojem": "Fixní náklady", "Vysvětlení": "Náklady, které se nemění přímo podle počtu prodaných kusů, například nájem nebo licence na software."},
            {"Pojem": "Inflace", "Vysvětlení": "Růst cenové hladiny. Za stejnou částku si člověk koupí méně než dříve."},
            {"Pojem": "Investice", "Vysvětlení": "Vložení peněz do aktiva s očekáváním budoucího výnosu, ale s určitým rizikem."},
            {"Pojem": "Jistina", "Vysvětlení": "Původně půjčená nebo vložená částka, ze které se počítá úrok."},
            {"Pojem": "Kryptoměna", "Vysvětlení": "Digitální aktivum fungující v počítačové síti, často bez jedné centrální banky."},
            {"Pojem": "Likvidita", "Vysvětlení": "Schopnost rychle proměnit aktivum na peníze nebo schopnost firmy včas platit své závazky."},
            {"Pojem": "LTV", "Vysvětlení": "Poměr výše úvěru k hodnotě nemovitosti (Loan to Value). Používá se hlavně u hypoték."},
            {"Pojem": "Neobanka", "Vysvětlení": "Moderní banka nebo finanční služba zaměřená hlavně na mobilní prostředí (např. Revolut)."},
            {"Pojem": "Pasiva", "Vysvětlení": "Zdroje financování majetku firmy, například vlastní kapitál, úvěry nebo závazky."},
            {"Pojem": "Pohledávka", "Vysvětlení": "Částka, kterou má někdo dostat zaplacenou. (Firma čeká, až jí zákazník zaplatí)."},
            {"Pojem": "Repo sazba", "Vysvětlení": "Důležitá úroková sazba ČNB, která ovlivňuje cenu (úroky) peněz v celé ekonomice."},
            {"Pojem": "Rentabilita", "Vysvětlení": "Ziskovost. Ukazuje, jak dobře firma vytváří zisk vzhledem k tržbám, majetku nebo kapitálu."},
            {"Pojem": "Rezerva", "Vysvětlení": "Peníze odložené stranou pro nečekané situace (finanční airbag)."},
            {"Pojem": "Riziko", "Vysvětlení": "Možnost, že výsledek bude jiný, než člověk očekával — například ztráta peněz."},
            {"Pojem": "RPSN", "Vysvětlení": "Roční procentní sazba nákladů. Ukazuje CELKOVÉ roční náklady úvěru (úrok + všechny poplatky)."},
            {"Pojem": "Složené úročení", "Vysvětlení": "Úročení, při kterém se úročí nejen původní částka, ale i dříve připsané úroky (úroky z úroků)."},
            {"Pojem": "Spekulace", "Vysvětlení": "Sázka na krátkodobý pohyb ceny s vysokým rizikem (vs. dlouhodobé investování)."},
            {"Pojem": "Token", "Vysvětlení": "Digitální jednotka v kryptoměnovém nebo blockchainovém prostředí."},
            {"Pojem": "Úrok", "Vysvětlení": "Cena za půjčení peněz (když platíš bance) nebo odměna za jejich uložení (když banka platí tobě)."},
            {"Pojem": "Variabilní náklady", "Vysvětlení": "Náklady, které rostou nebo klesají přímo podle objemu výroby/prodeje (např. nákup surovin)."},
            {"Pojem": "Volatilita", "Vysvětlení": "Kolísání ceny aktiva. Vysoká volatilita = cena lítá prudce nahoru a dolů."},
            {"Pojem": "Závazek", "Vysvětlení": "Částka nebo povinnost, kterou musí člověk nebo firma zaplatit někomu jinému (Dluh)."}
        ]
        
        df_slovnik = pd.DataFrame(slovnik_data)

        tab_db, tab_flash = st.tabs(["📚 Databáze pojmů", "🧠 Trénink (Flashcards)"])

        with tab_db:
            st.markdown("### Prohledávatelný slovník")
            st.dataframe(
                df_slovnik, 
                use_container_width=True, 
                hide_index=True,
                column_config={
                    "Pojem": st.column_config.TextColumn("Pojem", width="medium"),
                    "Vysvětlení": st.column_config.TextColumn("Jednoduché vysvětlení", width="large")
                }
            )

        with tab_flash:
            st.markdown("### Otestuj se: Dokážeš to vysvětlit ze života?")
            st.write("Skutečné porozumění poznáš tak, že dokážeš odborný pojem vysvětlit na příkladu z běžného života. Vylosuj si pojem a zkus to!")
            
            # Inicializace session state pro uchování vylosovaného pojmu
            if 'random_term' not in st.session_state:
                st.session_state['random_term'] = random.choice(slovnik_data)

            if st.button("🎲 Vylosovat nový pojem", key="btn_losuj"):
                st.session_state['random_term'] = random.choice(slovnik_data)
                
            vybrany_pojem = st.session_state['random_term']

            with st.container(border=True):
                st.markdown(f"#### Tvé slovo je: **{vybrany_pojem['Pojem']}**")
                
                with st.form("flashcard_form", clear_on_submit=False):
                    priklad = st.text_input("Napiš sem svůj vlastní příklad ze života (např. 'Je to jako když...'):")
                    ukazat_odpoved = st.form_submit_button("Zkontrolovat správnou definici")
                    
                    if ukazat_odpoved:
                        st.divider()
                        st.info(f"**Učebnicová definice:** {vybrany_pojem['Vysvětlení']}")
                        if len(priklad) > 5:
                            st.success("Skvěle! Pokud se tvůj příklad shoduje s logikou výše, právě jsi tento pojem dokonale pochopil/a.")
                        else:
                            st.warning("Zkus příště napsat reálný příklad, víc si to tak zapamatuješ!")
