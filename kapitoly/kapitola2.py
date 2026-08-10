import base64
import math
import os
import streamlit as st


def render():
    st.markdown(
        "<span class='hero-badge'>Kapitola 2</span>", unsafe_allow_html=True
    )
    st.title("2. Finance a osobní management")
    st.markdown(
        "<p style='font-size: 1rem; color: #64748b; margin-bottom: 1.5rem;'>"
        "Finance v běžném životě: peníze, rozhodování a odpovědnost.</p>",
        unsafe_allow_html=True,
    )

    with st.container(border=True):
        st.markdown(
            """
        <div class='box-blue'>
            <strong>🪙 Pointa kapitoly:</strong> Finanční gramotnost není jen znalost pojmů. Je to schopnost rozumět penězům jako systému, bezpečně se rozhodovat, vyhodnocovat rizika a plánovat osobní i podnikové finance tak, aby člověk dokázal reagovat na běžné i krizové situace.
        </div>
        """,
            unsafe_allow_html=True,
        )

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
        "8. Slovník cizích pojmů",
    ]

    st.markdown(
        "📌 <strong>Přechod na podkapitolu:</strong>", unsafe_allow_html=True
    )
    selected_section_2 = st.selectbox(
        "Přechod na podkapitolu:",
        section_options_2,
        index=0,
        label_visibility="collapsed",
    )
    st.divider()

    # =========================================================================
    # 1.1 PENÍZE JAKO DIGITÁLNÍ DATA
    # =========================================================================
    if "1.1 Peníze jako digitální data" in selected_section_2:
        st.markdown(
            "<div class='sub-section-header'>1. BANKOVNÍ SYSTÉM A PENÍZE V 21."
            " STOLETÍ</div><h2>1.1 Peníze jako digitální data</h2>",
            unsafe_allow_html=True,
        )

        st.write(
            "21. století není jen éra umělé inteligence a sociálních sítí. Je"
            " to především éra totální transformace toho, jak vnímáme hodnotu."
            " Ještě před pár desítkami let znamenalo „být v bance“ fyzickou"
            " návštěvu přepážky, papírování a čekání na úřední hodiny. Dnes?"
            " Bankovní systém se stal neviditelným operačním systémem našeho"
            " života. Běží na pozadí každého našeho kliknutí, každého „pípnutí“"
            " mobilem u pokladny a každého online nákupu."
        )

        with st.container(border=True):
            st.markdown(
                """
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
            """,
                unsafe_allow_html=True,
            )

        st.write(
            "Peníze dnes často nevypadají jako mince nebo bankovky. Když platíš"
            " kartou, mobilem nebo hodinkami, většinou se nepřesouvá žádný"
            " fyzický předmět. V bankovním systému se změní digitální záznam:"
            " jednomu účtu se částka odečte a druhému připíše. Abychom tomu"
            " rozuměli, je dobré projít si vývoj peněz od nejstarších forem"
            " směny až po současná digitální data."
        )

        st.markdown(
            """
        <div class='box-gray'>
            <strong>💡 Základní myšlenka:</strong> Peníze nejsou jen „věc“. Jsou to hlavně důvěryhodný záznam hodnoty, kterému lidé, firmy a stát věří. V různých dobách měl tento záznam podobu dobytka, obilí, kovu, mince, papírové bankovky, bankovního účtu nebo digitální platby v mobilu.
        </div>
        """,
            unsafe_allow_html=True,
        )

        # 1.1.1 PROČ PENÍZE VŮBEC VZNIKLY
        with st.container(border=True):
            st.markdown("### 1.1.1 Proč peníze vůbec vznikly")
            st.write(
                "Na úplném začátku lidé používali **naturální směnu** —"
                " vyměňovali zboží za zboží nebo službu za službu. Například"
                " někdo měl obilí a potřeboval boty, jiný uměl boty vyrobit a"
                " potřeboval jídlo."
            )
            st.write(
                "Problém byl v tom, že směna fungovala jen tehdy, když se"
                " potkaly dvě potřeby najednou. Tomu se říká **dvojí shoda"
                " potřeb**."
            )

            st.info("""
            **🍞 Příklad dvojí shoda potřeb:**  
            Pekař chce nové boty. Švec by mu je mohl vyrobit, ale zrovna nepotřebuje chleba. Pekař tedy musí najít někoho dalšího, kdo chce chleba a zároveň má něco, co chce švec. Taková směna je nepraktická, pomalá a omezuje obchod.
            """)
            st.write(
                "Proto se postupně objevily předměty, které lidé přijímali ne"
                " proto, že je hned sami potřebovali, ale protože věřili, že"
                " je později vymění s někým dalším. Tak vznikl základ peněz."
            )

        # 1.1.2 KOMODITNÍ PENÍZE
        with st.container(border=True):
            st.markdown(
                "### 1.1.2 Komoditní peníze: hodnota ukrytá ve věci"
            )
            st.write(
                "První peníze měly často podobu komodit — tedy věcí, které"
                " měly hodnotu samy o sobě. Mohlo jít například o sůl, obilí,"
                " dobytek, kožešiny, mušle, drahé kovy nebo jiné vzácné a žádané"
                " předměty."
            )

            st.markdown(
                """
            <div class='box-gray'>
                <strong>🧵 Česká stopa: plátno jako platidlo</strong><br>
                V českých zemích se podle zprávy cestovatele Ibráhíma ibn Jákúba z 10. století používaly jako prostředek směny také kousky plátna. Právě s tím se často spojuje původ českých slov <em>platit</em>, <em>platba</em> nebo <em>platidlo</em> — tedy dát „plátno“ jako hodnotu při směně. Je to dobrý příklad toho, že peníze nemusely být vždy mince nebo bankovky. Mohly mít podobu věci, které lidé v dané společnosti důvěřovali a kterou byli ochotni přijímat.
            </div>
            """,
                unsafe_allow_html=True,
            )

            st.markdown(
                """
            | Forma peněz | Výhoda | Problém |
            | :--- | :--- | :--- |
            | **Dobytek, obilí, sůl** | Lidé je uměli použít v běžném životě. | Špatně se dělily, skladovaly nebo převážely. |
            | **Mušle, kožešiny, vzácné předměty** | Byly rozpoznatelné a někde společensky ceněné. | Jejich hodnota závisela na místě a zvyklostech. |
            | **Zlato a stříbro** | Byly vzácné, trvanlivé a dobře dělitelné. | Bylo nutné ověřovat ryzost a hmotnost. |
            """,
                unsafe_allow_html=True,
            )

            st.markdown(
                "##### 🧠 Interaktivní výzva: Vyber komoditu pro platbu"
            )
            st.write(
                "Vyber jednu komoditu, která by mohla sloužit jako peníze."
                " Napiš, v čem by byla praktická a v čem by naopak selhávala:"
            )

            kom_sel = st.selectbox(
                "Zvol komoditu:",
                [
                    "Vyber...",
                    "Sůl 🧂",
                    "Dobytek / Kráva 🐄",
                    "Mušle 🐚",
                    "Zlatý prach ✨",
                ],
                key="k2_1_1_2_kom",
            )
            if kom_sel == "Sůl 🧂":
                st.info(
                    "Sůl je sice užitečná k jídlu, ale při kontaktu s vodou se"
                    " rozpustí a zničí!"
                )
            elif kom_sel == "Dobytek / Kráva 🐄":
                st.error(
                    "❌ Kráva se špatně dělí (jak zaplatíš za jedno kafe?) a"
                    " navíc ji musíš neustále krmit."
                )
            elif kom_sel == "Mušle 🐚":
                st.warning(
                    "⚠️ Hodnota závisí na zvyklostech. Pokud je kavárník"
                    " neuznává, kávu ti nedá."
                )
            elif kom_sel == "Zlatý prach ✨":
                st.success(
                    "✅ Skvělé k uchování hodnoty, ale barista musí prach u"
                    " kasy složitě vážit a ověřovat ryzost."
                )

            if "vykresli_otazku_fn" in st.session_state:
                st.session_state["vykresli_otazku_fn"](
                    "2.1.1",
                    f"Slovní obhajoba tvojí volby pro komoditu ({kom_sel}):",
                    "2",
                    st.session_state.get("ulozene_odpovedi", {}),
                )

        # 1.1.3 MINCE A 1.1.4 PAPÍROVÉ PENÍZE
        with st.container(border=True):
            st.markdown("### 1.1.3 Mince: hodnota se začíná standardizovat")
            st.write(
                "Velký posun nastal se vznikem mincí. Mince měly určenou"
                " hmotnost, kov, tvar a označení autority, která je vydala. Díky"
                " tomu nebylo nutné při každé platbě znovu vážit kus kovu a"
                " ověřovat jeho kvalitu."
            )
            st.write("Mince tedy přinesly:")
            st.markdown("""
            * jednodušší placení,
            * lepší rozpoznatelnost hodnoty,
            * větší důvěru v obchodě,
            * možnost vybírat daně a platit vojsko,
            * silnější roli státu nebo panovníka.
            """)
            st.info(
                "⚖️ **Důležitý princip:** Čím více obchod roste, tím důležitější"
                " je, aby lidé věřili, že peníze mají jasnou hodnotu a že je"
                " ostatní přijmou."
            )

            st.markdown(
                "### 1.1.4 Papírové peníze: od potvrzení ke státní měně"
            )
            st.write(
                "Papírové peníze vznikaly postupně. Původně mohly fungovat jako"
                " potvrzení, že má člověk někde uložený drahý kov nebo jinou"
                " hodnotu. Místo přenášení těžkého zlata bylo jednodušší předat"
                " papírový doklad."
            )
            st.write(
                "Později se z těchto potvrzení staly bankovky. Jejich hodnota"
                " už nespočívala v samotném papíru, ale v důvěře, že je přijme"
                " společnost a že za nimi stojí banka nebo stát."
            )

            st.markdown(
                """
            <div class='box-blue'>
                <strong>Proč má bankovka hodnotu, když je to jen papír?</strong><br>
                Bankovka má hodnotu proto, že ji stát uznává jako zákonné platidlo a lidé věří, že s ní zaplatí i jinde. Hodnota tedy není v materiálu, ale v důvěře, pravidlech a fungujícím systému.
            </div>
            """,
                unsafe_allow_html=True,
            )

        # 1.1.5 až 1.1.8 ZLATÝ STANDARD, BRETTONWOODS, NIXON A FIAT
        with st.container(border=True):
            st.markdown(
                "### 1.1.5 Zlatý standard: když byly peníze navázané na zlato"
            )
            st.write(
                "Dlouhou dobu nebyly papírové peníze chápány jen jako samostatná"
                " hodnota. Často fungovaly jako slib, že je lze vyměnit za"
                " určité množství zlata. Tomu se říká **zlatý standard**."
            )
            st.markdown(
                """
            <div class='box-gray'>
                🥇 <strong>Zlatý standard jednoduše:</strong> Stát nebo centrální banka slíbily, že měna je krytá zlatem. Peníze tedy nebyly jen papírky. Měly být navázané na zásoby zlata, které měl stát nebo centrální banka k dispozici.
            </div>
            """,
                unsafe_allow_html=True,
            )
            st.write("V praxi to znamenalo, že:")
            st.markdown("""
            * měna měla pevně stanovený vztah ke zlatu,
            * bankovky mohly být za určitých podmínek směnitelné za zlato,
            * stát nemohl jednoduše vytvářet neomezené množství peněz, pokud neměl dost zlata,
            * kurz měn byl stabilnější, protože se odvozoval od zlata,
            * mezinárodní obchod měl pevnější pravidla.
            """)

            st.markdown(
                "### 1.1.6 Brettonwoodský systém: dolar, zlato a svět po druhé"
                " světové válce"
            )
            st.write(
                "Po druhé světové válce vznikl nový mezinárodní měnový systém"
                " nazývaný **Brettonwoodský systém** (1944). Americký dolar byl"
                " navázán na zlato (35 USD za trojskou unci) a ostatní měny na"
                " americký dolar."
            )

            st.markdown("### 1.1.7 Konec vazby na zlato: Nixonův šok")
            st.write(
                "V roce 1971 americký prezident Richard Nixon pozastavil"
                " směnitelnost dolaru za zlato (**Nixonův šok**). Tím se svět"
                " posunul k systému dnešních **fiat peněz**, jejichž hodnota"
                " stojí výhradně na důvěře ve stát, centrální banku a ekonomiku."
            )

            st.markdown("### 1.1.8 Je lepší mít peníze kryté zlatem, nebo ne?")
            st.markdown(
                """
            | Systém | Výhody | Nevýhody |
            | :--- | :--- | :--- |
            | **Peníze navázané na zlato** | Omezují přílišné „tištění peněz“, podporují dlouhodobou důvěru a stabilnější měnové kurzy. | Svazují ekonomiku množstvím zlata, ztěžují reakci na krize a mohou prohlubovat poklesy. |
            | **Fiat peníze (dnešní)** | Centrální banka může pružněji reagovat na krize, inflaci, nezaměstnanost. | Vyžadují důvěru v odpovědnou politiku. Při špatném řízení hrozí vysoká inflace. |
            """,
                unsafe_allow_html=True,
            )

            st.markdown("##### 🧩 Aktivita: Zlatý standard vs. dnešní peníze")
            v_sys = st.radio(
                "Který systém obhajuješ?",
                ["Peníze kryté zlatem", "Fiat peníze (dnešní systém)"],
                key="k2_1_1_8_rad",
            )

            if "vykresli_otazku_fn" in st.session_state:
                st.session_state["vykresli_otazku_fn"](
                    "2.1.2",
                    f"Vaše obhajoba pro systém ({v_sys}):",
                    "2",
                    st.session_state.get("ulozene_odpovedi", {}),
                )

        # 1.1.9 & 1.1.10 BEZHOOTOVOSTNÍ PENÍZE A KARTY
        with st.container(border=True):
            st.markdown(
                "### 1.1.9 Bezhotovostní peníze: peníze jako účetní záznam"
            )
            st.write(
                "S rozvojem bank se začaly stále více používat bezhotovostní"
                " peníze. Člověk nemusel držet všechny peníze v hotovosti. Mohl"
                " je mít uložené v bance a platit převodem, šekem, později kartou"
                " nebo internetovým bankovnictvím."
            )
            st.info(
                "🏦 **Jednoduše řečeno:** Když máš na účtu 2 000 Kč, neleží někde"
                " v bance krabička s bankovkami označená tvým jménem. Banka"
                " vede záznam, že máš vůči ní nárok na určitou částku."
            )

            st.markdown("### 1.1.10 Platební karta: plastový klíč k účtu")
            st.write(
                "Platební karta sama o sobě nejsou peníze. Je to nástroj,"
                " kterým dáváš pokyn k platbě."
            )

            st.markdown(
                """
            <div class='box-red'>
                <strong>🔐 Bezpečnostní pravidlo:</strong> Karta, mobil nebo hodinky nejsou „peníze samy o sobě“. Jsou to vstupní brány k penězům na účtu nebo k úvěrovému limitu. Kdo získá přístup k platebnímu nástroji a k ověřovacím prvkům, může dát pokyn k platbě.
            </div>
            """,
                unsafe_allow_html=True,
            )

            with st.expander(
                "🛡️ Jaké technologie platbu chrání (Detailní rozbor)"
            ):
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
            st.write(
                "Správa peněz přes mobil je pohodlná, ale vyžaduje obezřetnost"
                " před podvody."
            )

            st.markdown(
                "##### 🚨 Ukázka podvodného e-mailu (Phishing trenažér)"
            )
            st.info("""
            **Od:** bezpecnost@bnka-podpora-klientu.cz  
            **Předmět:** ZABLOKOVANÝ ÚČET - OKAMŽITÁ AKCE!  
            Vážený kliente, vaše karta byla dočasně zablokována. Pro její okamžité odblokování klikněte IHNED na odkaz níže a přihlaste se:  
            👉 [www.mojebanka-rychle-overeni.com/login](https://#)
            """)

            p_chk1 = st.checkbox(
                "Podezřelá e-mailová adresa odesílatele (překlepy)",
                key="k2_1_1_11_ph1",
            )
            p_chk2 = st.checkbox(
                "Výzva k nahlášení na Policii", key="k2_1_1_11_ph2"
            )
            p_chk3 = st.checkbox(
                "Text vytváří tlak na rychlé rozhodnutí", key="k2_1_1_11_ph3"
            )
            p_chk4 = st.checkbox(
                "Nebezpečný odkaz nevedoucí na ofic. web banky",
                key="k2_1_1_11_ph4",
            )

            if st.button("Vyhodnotit hrozbu phishingu 💾", key="k2_1_1_11_btn"):
                if p_chk1 and p_chk3 and p_chk4 and not p_chk2:
                    st.success(
                        "Správně! Odhalil jsi všechny 3 varovné signály."
                        " Správná reakce: Neklikat na odkaz, nic nevyplňovat a"
                        " situaci ověřit v oficiální aplikaci banky."
                    )
                    if "uloz_odpoved_fn" in st.session_state:
                        st.session_state["uloz_odpoved_fn"](
                            "Kapitola 2",
                            "Podkapitola 1.1.11 - Phishing trenažér",
                            "Úspěšně odhaleno (odesílatel, časový tlak,"
                            " podezřelý odkaz)",
                        )
                else:
                    st.error(
                        "Zkus to znovu. Označ 3 varovné znaky (odesílatel, časový"
                        " tlak, podezřelý odkaz)."
                    )

            st.markdown("### 1.1.12 Okamžité platby, QR platby a fintech")
            st.write(
                "Okamžité platby doručí peníze během sekund, QR kód šetří čas"
                " při opisování účtu a **fintech firmy** přinášejí přehledné"
                " mobilní správy rozpočtů."
            )

        # 1.1.13 KRYPTOMĚNY A BLOCKCHAIN
        with st.container(border=True):
            st.markdown("### 1.1.13 Kryptoměny a blockchain")
            st.write(
                "Kryptoměny fungují na technologii **blockchain** — sdílené"
                " digitální účetní knize bez centrální banky."
            )
            st.write(
                "Princip stojí na **decentralizaci**, **transparentnosti**,"
                " **nevratnosti** a **vlastní odpovědnosti** za soukromý klíč."
            )

            st.markdown(
                "##### 🧮 Modelový příklad pravidelného investování (DCA):"
            )
            st.write(
                "Model vkladu 1 000 Kč na začátku + 200 Kč měsíčně po dobu 5"
                " let (Celkem vložených **13 000 Kč**):"
            )

            scen_sel = st.selectbox(
                "Vyber modelový scénář vývoje kryptoměny:",
                [
                    "Pesimistický scénář (-20 % ročně)",
                    "Nulový scénář (0 % ročně)",
                    "Mírně růstový scénář (+5 % ročně)",
                    "Silně růstový scénář (+15 % ročně)",
                    "Extrémně růstový scénář (+30 % ročně)",
                ],
                key="k2_dca_1_1_13_sel",
            )

            if "Pesimistický" in scen_sel:
                st.metric(
                    "Orientační hodnota po 5 letech",
                    "cca 7 700 Kč",
                    delta="-5 300 Kč (ztráta)",
                )
            elif "Nulový" in scen_sel:
                st.metric(
                    "Orientační hodnota po 5 letech",
                    "13 000 Kč",
                    delta="0 Kč (bez zisku)",
                )
            elif "Mírně růstový" in scen_sel:
                st.metric(
                    "Orientační hodnota po 5 letech",
                    "cca 14 800 Kč",
                    delta="+1 800 Kč zisk",
                )
            elif "Silně růstový" in scen_sel:
                st.metric(
                    "Orientační hodnota po 5 letech",
                    "cca 19 300 Kč",
                    delta="+6 300 Kč zisk",
                )
            else:
                st.metric(
                    "Orientační hodnota po 5 letech",
                    "cca 30 700 Kč",
                    delta="+17 700 Kč zisk",
                )

            st.markdown(
                "##### 🏦 Srovnání: Kryptoměny vs. Spořicí účet vs. Penzijní"
                " spoření"
            )
            st.markdown(
                """
            | Možnost | Modelové zhodnocení | Orientační hodnota po 5 letech | Co je hlavní rozdíl |
            | :--- | :--- | :--- | :--- |
            | **Spořicí účet** | cca 3,5 % p.a. | cca 14 200 Kč | Peníze jsou dostupné rychle, výnos je nižší. |
            | **Termínovaný vklad** | cca 3,5–4,0 % p.a. | cca 14 300–14 500 Kč | Sazba garantovaná, peníze jsou vázané. |
            | **Penzijní spoření** | cca 3–5 % p.a. + podpora | cca 14 100–15 100 Kč | Dlouhodobý produkt na stáří se státní podporou. |
            | **Krypto (Nulový scen.)**| 0 % ročně | 13 000 Kč | Bez růstu ceny nevzniká zisk, působí inflace. |
            | **Krypto (Pesim. scen.)**| -20 % ročně | cca 7 700 Kč | U kryptoměn je reálná i výrazná ztráta hodnoty. |
            """,
                unsafe_allow_html=True,
            )

        # 1.1.14 & 1.1.15 CBDC A SHRNUTÍ VÝVOJE PENĚZ
        with st.container(border=True):
            st.markdown(
                "### 1.1.14 Digitální měny centrálních bank (CBDC)"
            )
            st.write(
                "CBDC představují digitální peníze vydávané přímo centrální"
                " bankou (např. Digitální Euro). Na rozdíl od kryptoměny za"
                " nimi stojí stát a zákony."
            )

            st.markdown("### 1.1.15 Shrnutí vývoje peněz")
            st.markdown(
                """
            | Období / forma | Co sloužilo jako peníze | Na čem stála důvěra |
            | :--- | :--- | :--- |
            | **Naturální směna** | Zboží za zboží | Na přímé dohodě dvou lidí |
            | **Komoditní peníze** | Sůl, obilí, dobytek, mušle, kovy | Na užitečnosti nebo vzácnosti věci |
            | **Mince** | Kovové mince | Na kovu, hmotnosti, ryzosti a autoritě panovníka |
            | **Bankovky** | Papírové peníze | Na důvěře ve stát, banku a zákonné platidlo |
            | **Bezhotovostní peníze** | Zůstatek na účtu | Na bankovním systému, pravidlech a dohledu |
            | **Digitální platby** | Data v bankovních systémech | Na ověření identity a bezpečnosti infrastruktury |
            | **Kryptoměny** | Distribuovaný digitální záznam | Na technologii, síti uživatelů a protokolu |
            """,
                unsafe_allow_html=True,
            )

            st.markdown(
                """
            <div class='box-purple'>
                🤖 <strong>AI mentoring prompt:</strong> Zkopíruj tento prompt do AI asistenta:<br>
                <em>„Vysvětli mi vývoj peněz od směny po digitální platby na příkladu běžného nákupu oběda.“</em>
            </div>
            """,
                unsafe_allow_html=True,
            )

            st.markdown("🎮 **Mikroaktivita: Peníze nejsou jen papír**")

            if "vykresli_otazku_fn" in st.session_state:
                st.session_state["vykresli_otazku_fn"](
                    "2.1.3",
                    "Ve dvojici vyberte jednu platbu z běžného dne. Popište"
                    " cestu peněz: kdo platí, komu, jaký nástroj použije a kde"
                    " vzniká digitální záznam.",
                    "2",
                    st.session_state.get("ulozene_odpovedi", {}),
                )

    # =========================================================================
    # 1.2 ČNB A KOMERČNÍ BANKY
    # =========================================================================
    elif "1.2 ČNB" in selected_section_2:
        st.markdown(
            "<div class='sub-section-header'>1. BANKOVNÍ SYSTÉM A PENÍZE V 21."
            " STOLETÍ</div><h2>1.2 ČNB a komerční banky</h2>",
            unsafe_allow_html=True,
        )
        st.write(
            "Bankovní systém není jen síť poboček a bankomatů. Je to jeden z"
            " nejdůležitějších „nervových systémů“ ekonomiky. Přes banky tečou"
            " mzdy, platby za zboží, splátky úvěrů, daně, sociální dávky,"
            " investice i peníze firem. Aby tento systém fungoval, musí mu lidé"
            " věřit."
        )

        with st.container(border=True):
            st.markdown(
                """
            <div class='box-blue'>
                🏦 <strong>Základní rozlišení:</strong><br>
                • <strong>Česká národní banka (ČNB):</strong> Centrální banka České republiky. Nejde o běžnou banku pro občany. Je to instituce, která hlídá stabilitu měny, finančního systému a pravidla pro banky.<br>
                • <strong>Komerční banky:</strong> Banky, se kterými běžně pracují lidé, firmy a obce. Vedou účty, přijímají vklady, poskytují úvěry, vydávají platební karty a zajišťují platby.
            </div>
            <div class='box-purple'>
                🧠 <strong>Pointa pro běžný život:</strong> Když platíš kartou, bereš si hypotéku, dostáváš výplatu na účet nebo sleduješ inflaci, nepřímo se setkáváš s rozhodnutími centrální banky i se službami komerčních bank.
            </div>
            """,
                unsafe_allow_html=True,
            )

        # 1.2.1 Postavení ČNB v ČR
        with st.container(border=True):
            st.markdown("### 1.2.1 Postavení ČNB v České republice")
            st.write(
                "Česká národní banka je centrální banka České republiky. Její"
                " postavení je zakotveno v právním řádu ČR a její činnost"
                " upravuje zejména zákon o České národní bance. ČNB je"
                " veřejnoprávní instituce se zvláštním postavením: není"
                " komerční firmou, neusiluje o zisk jako běžný podnik a"
                " neposkytuje běžné bankovní služby občanům."
            )

            st.markdown(
                """
            <div class='box-gray'>
                ⚖️ <strong>Důležité:</strong> ČNB je při plnění svých hlavních úkolů nezávislá. To znamená, že vláda jí nemá diktovat, jak má nastavovat úrokové sazby nebo měnovou politiku. Smyslem nezávislosti je chránit stabilitu měny a finančního systému před krátkodobým politickým tlakem.
            </div>
            """,
                unsafe_allow_html=True,
            )

            st.write(
                "ČNB sídlí v Praze a působí pro celou Českou republiku. Je"
                " součástí Evropského systému centrálních bank, protože Česká"
                " republika je členem Evropské unie. Dokud ale ČR nepřijme euro,"
                " ČNB provádí vlastní měnovou politiku pro českou korunu."
            )

            with st.expander(
                "🇪🇺 ČNB a euro: proč je česká situace trochu jiná"
            ):
                st.write(
                    "To, že má Česká republika vlastní měnu (korunu) a vlastní"
                    " centrální banku, která samostatně nastavuje měnovou"
                    " politiku, není v Evropské unii u všech států běžné. Mnoho"
                    " členských zemí EU už přijalo euro a patří do eurozóny. V"
                    " těchto zemích nerozhoduje o hlavních úrokových sazbách"
                    " jejich národní centrální banka samostatně, ale společně"
                    " systém vedený Evropskou centrální bankou (ECB)."
                )
                st.write(
                    "**Příklad:** Slovensko přijalo euro v roce 2009. Národní"
                    " banka Slovenska dál existuje, ale už nevydává vlastní"
                    " slovenskou korunu a samostatně neurčuje měnovou politiku"
                    " pro vlastní měnu. Podílí se na fungování eurozóny,"
                    " dohledu a finanční stabilitě, ale hlavní měnová politika"
                    " se řeší na evropské úrovni přes ECB."
                )
                st.write(
                    "**Jak by to fungovalo po přijetí eura v ČR:** Česká koruna"
                    " by byla nahrazena eurem. ČNB by nezanikla, ale změnila by"
                    " se její role. Dál by působila jako národní centrální"
                    " banka, dohlížela by na finanční trh, pečovala o"
                    " hotovostní oběh eura v ČR, podílela se na finanční"
                    " stabilitě a byla by součástí Eurosystému. O hlavních"
                    " úrokových sazbách pro eurozónu by se ale rozhodovalo"
                    " společně v rámci ECB, nikoli samostatně jen podle české"
                    " ekonomiky."
                )
                st.write(
                    "**Konkrétní modelový příklad rozdílu:** Představ si, že v"
                    " Česku je inflace vyšší než v eurozóně a česká ekonomika"
                    " potřebuje brzdit zdražování. Pokud má ČR vlastní korunu,"
                    " může ČNB zvýšit úrokové sazby výrazněji — například na"
                    " 6–7 %. Tím zdraží úvěry, hypotéky i půjčky, ale zároveň"
                    " podpoří spoření a může pomoci tlumit inflaci. Pokud by ČR"
                    " už platila eurem, sazby by se nastavovaly pro celou"
                    " eurozónu. ECB by se dívala na průměrnou situaci mnoha"
                    " zemí, například Německa, Francie, Itálie, Slovenska nebo"
                    " Španělska. Kdyby eurozóna jako celek potřebovala mírnější"
                    " politiku, mohly by být sazby třeba jen 3–4 %, i když by"
                    " Česku samostatně vyhovovaly vyšší sazby."
                )
                st.write(
                    "**Co by to znamenalo v běžném životě:** Po přijetí eura"
                    " by úrokové sazby v ČR mohly být v některých obdobích"
                    " nižší, než jaké by nastavila samostatná ČNB. To by mohlo"
                    " zlevnit hypotéky a úvěry, ale zároveň by to mohlo méně"
                    " brzdit inflaci, pokud by české ceny rostly rychleji než"
                    " v eurozóně. Výhoda eura je větší měnová stabilita a"
                    " jednodušší obchodování v eurozóně. Nevýhoda je menší"
                    " možnost přizpůsobit měnovou politiku jen české"
                    " ekonomice."
                )

                euro_sim = st.radio(
                    "Zvol simulovaný režim při vysoké české inflaci:",
                    [
                        "Vlastní měna (CZK) — ČNB zvýší sazby na 7 %",
                        "Společné Euro (EUR) — ECB drží sazby na 3,5 %",
                    ],
                    key="k2_1_2_1_euro_sim",
                )
                if "CZK" in euro_sim:
                    st.success(
                        "✅ **Samostatná ČNB:** Vyšší sazby zdraží úvěry a"
                        " hypotéky v ČR, ale účinněji tlumí inflaci a chrání"
                        " úspory."
                    )
                else:
                    st.warning(
                        "⚠️ **Společné Euro (ECB):** Zůstávají levnější úvěry,"
                        " ale inflace v ČR může trvat déle a více"
                        " znehodnocovat kupní sílu."
                    )

        # 1.2.2 Hlavní cíl ČNB
        with st.container(border=True):
            st.markdown("### 1.2.2 Hlavní cíl ČNB")
            st.write(
                "Hlavním cílem ČNB je péče o cenovou stabilitu. Jinými slovy:"
                " ČNB se snaží, aby peníze neztrácely hodnotu příliš rychle a"
                " aby inflace nebyla dlouhodobě příliš vysoká ani nebezpečně"
                " nízká."
            )

            st.markdown(
                """
            <div class='box-gray'>
                🎯 <strong>Cenová stabilita jednoduše:</strong> Neznamená, že se nikdy nic nezdraží. Znamená, že růst cen má být dlouhodobě předvídatelný a zvládnutelný. Když je inflace příliš vysoká, lidem klesá kupní síla, firmám se hůř plánuje a ekonomika ztrácí stabilitu.
            </div>
            """,
                unsafe_allow_html=True,
            )
            st.write(
                "ČNB v praxi používá inflační cílování. To znamená, že sleduje"
                " vývoj inflace a nastavuje nástroje měnové politiky tak, aby"
                " se inflace ve střednědobém horizontu pohybovala kolem"
                " stanoveného cíle."
            )

            st.markdown("#### 🎮 Interaktivní simulace: Jsi bankovní rada ČNB")
            st.write(
                "**Situace:** Inflace je vysoká, lidé si stěžují na zdražování,"
                " hypotéky jsou drahé a firmy říkají, že zákazníci méně"
                " utrácejí. Tvoje skupina představuje bankovní radu ČNB."
            )

            c_rada_action = st.radio(
                "Rozhodněte o sazbách:",
                [
                    "zvýšíte úrokové sazby",
                    "snížíte úrokové sazby",
                    "ponecháte sazby beze změny",
                    "použijete komunikaci směrem k veřejnosti",
                    "budete zvažovat devizové intervence",
                ],
                key="k2_1_2_2_rada_act",
            )

            st.write("**Musíte zdůvodnit:**")
            q1 = st.text_input("1. Co se stane s úvěry?", key="k2_q1_uvery")
            q2 = st.text_input("2. Co se stane se spořením?", key="k2_q2_sporeni")
            q3 = st.text_input(
                "3. Jaký může být dopad na inflaci?", key="k2_q3_inflace"
            )
            q4 = st.text_input(
                "4. Komu vaše rozhodnutí pomůže a komu může zkomplikovat"
                " život?",
                key="k2_q4_komu",
            )
            q5 = st.text_input(
                "5. Jaké riziko vznikne, pokud se rozhodnete špatně?",
                key="k2_q5_riziko",
            )

            if st.button(
                "Výstup: Jedna minuta tiskové konference a uložení 💾",
                key="k2_1_2_2_rada_btn",
            ):
                st.markdown(
                    "**Tiskové prohlášení Bankovní rady:** „ČNB dnes rozhodla,"
                    f" že {c_rada_action}...“"
                )
                st.success("✅ Rozhodnutí Bankovní rady bylo uloženo!")

                rada_data = (
                    f"Akce sazeb: {c_rada_action} | Úvěry: {q1} | Spoření:"
                    f" {q2} | Dopad inflace: {q3} | Komu pomůže: {q4} |"
                    f" Riziko: {q5}"
                )
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"](
                        "Kapitola 2",
                        "Podkapitola 1.2.2 - Simulace Bankovní rady ČNB",
                        rada_data,
                    )

        # 1.2.3 Co přesně ČNB dělá
        with st.container(border=True):
            st.markdown("### 1.2.3 Co přesně ČNB dělá")
            st.write(
                "ČNB má několik klíčových funkčních oblastí. Každá z nich se"
                " týká jiné části ekonomiky, ale dohromady tvoří systém důvěry"
                " v peníze."
            )

            st.markdown(
                """
            | Funkce ČNB | Co to znamená | Příklad dopadu na běžný život |
            | :--- | :--- | :--- |
            | **Měnová politika** | Nastavuje podmínky pro hodnotu peněz, hlavně pomocí úrokových sazeb. | Ovlivňuje úroky u hypoték, spoření i úvěrů. |
            | **Emise hotovosti** | Vydává bankovky a mince české koruny a pečuje o jejich oběh. | Určuje, jaké bankovky a mince platí a jak vypadají. |
            | **Dohled nad finančním trhem** | Dohlíží na banky, pojišťovny, družstevní záložny, penzijní společnosti, investiční společnosti a další finanční instituce. | Hlídá, aby instituce dodržovaly pravidla a neohrožovaly klienty ani systém. |
            | **Finanční stabilita** | Sleduje rizika, která by mohla ohrozit celý finanční systém. | Řeší například, zda banky mají dost kapitálu a nejsou příliš rizikové. |
            | **Platební systémy** | Provozuje a dohlíží na důležité platební a zúčtovací systémy. | Pomáhá tomu, aby převody mezi bankami fungovaly bezpečně a spolehlivě. |
            | **Správa devizových rezerv** | Spravuje zásoby zahraničních měn a dalších aktiv státu. | Pomáhá stabilitě měny a důvěře v ekonomiku. |
            | **Banka státu** | Vede účty státu a poskytuje vybrané služby veřejnému sektoru. | Souvisí s pohybem peněz státu, například při placení výdajů veřejných institucí. |
            """,
                unsafe_allow_html=True,
            )

        # 1.2.4 Hotovost a ochranné prvky
        with st.container(border=True):
            st.markdown(
                "### 1.2.4 Hotovost, ochranné prvky bankovek a důvěra v peníze"
            )
            st.write(
                "Jednou z viditelných činností ČNB je péče o hotovostní oběh."
                " ČNB vydává české bankovky a mince, stahuje z oběhu poškozené"
                " nebo neplatné peníze a stará se o to, aby hotovost byla"
                " důvěryhodná. Právě sem patří také ochranné prvky bankovek."
            )
            st.write(
                "Bankovky mají ochranné prvky proto, aby bylo možné ověřit"
                " jejich pravost a snížit riziko padělání. Nejde jen o „ozdobu“"
                " bankovky. Ochranné prvky pomáhají běžným lidem, obchodníkům,"
                " bankám i státu poznat, zda je bankovka skutečná a zda jí mohou"
                " důvěřovat."
            )

            st.markdown(
                """
            <div class='box-gray'>
                🛡️ <strong>Proč ochranné prvky patří k tématu ČNB?</strong><br>
                ČNB odpovídá za českou měnu a hotovostní oběh. Pokud by bylo snadné bankovky padělat, lidé i obchody by se báli hotovost přijímat. Ochranné prvky proto chrání důvěru v peníze, ztěžují padělání a umožňují rychlou kontrolu pravosti při běžném placení.
            </div>
            """,
                unsafe_allow_html=True,
            )

            st.write(
                "Ochranné prvky můžeme rozdělit podle toho, jak je člověk"
                " kontroluje:"
            )
            st.markdown("""
            * **pohledem** — například vodoznak, ochranný proužek, soutisková značka nebo proměnlivá barva,
            * **hmatem** — například speciální papír a reliéfní tisk,
            * **naklopením bankovky** — například opticky proměnlivé prvky,
            * **pomůckami** — například kontrola pod UV světlem.
            """)

            st.markdown(
                "##### 🔎 Interaktivní aktivita: Ochranné prvky peněz (1000 Kč"
                " - František Palacký)"
            )
            st.write(
                "Prohlédni si přední (lícovou) i zadní (rubovou) stranu"
                " tisícikoruny a prozkoumej její ochranné prvky:"
            )

            @st.cache_data
            def nacist_obrazek_bankovky(nazvy_souboru):
                for nazev in nazvy_souboru:
                    mozne_cesty = [
                        nazev,
                        f"kapitoly/{nazev}",
                        f"assets/{nazev}",
                    ]
                    for cesta in mozne_cesty:
                        if os.path.exists(cesta):
                            with open(cesta, "rb") as f:
                                encoded = base64.b64encode(f.read()).decode()
                                return f"data:image/jpeg;base64,{encoded}"
                return None

            img_lic_base64 = nacist_obrazek_bankovky(
                ["1000_czk_lic.jpg", "1000_czk.jpg"]
            )
            img_rub_base64 = nacist_obrazek_bankovky(["1000_czk_rub.jpg"])

            tab_lic, tab_rub = st.tabs([
                "📄 Lícní strana (Přední - Palacký)",
                "🦅 Rubová strana (Zadní - Orlice)",
            ])

            with tab_lic:
                prvky_lic = {
                    "Vodoznak (pohledem)": {
                        "ikona": "💧",
                        "top": "48%",
                        "left": "14%",
                        "nazev": "Vodoznak (František Palacký)",
                        "misto": "Levý nepotištěný okraj bankovky",
                        "popis": (
                            "Zřetelný stínovaný portrét Františka Palackého s"
                            " číselným označením '1000' a motivem lipového"
                            " listu, viditelný z obou stran při pohledu proti"
                            " světlu."
                        ),
                        "kontrola": (
                            "👀 **Jak zkontrolovat:** Zvedni bankovku a podívej"
                            " se na nepotištěný levý okraj proti světelnému"
                            " zdroji."
                        ),
                    },
                    "Ochranný proužek (pohledem)": {
                        "ikona": "📏",
                        "top": "50%",
                        "left": "55.8%",
                        "nazev": "Ochranný proužek s mikrotextem",
                        "misto": (
                            "Svislý metalický pás zapuštěný do papíru"
                            " (uprostřed)"
                        ),
                        "popis": (
                            "Tmavý okenníkový proužek z pokovené umělé hmoty s"
                            " negativním mikrotextem 'ČNB 1000 Kč'. Při"
                            " naklonění mění barvu z hnědofialové na zelenou."
                        ),
                        "kontrola": (
                            "☀️ **Jak zkontrolovat:** Podívej se na bankovku"
                            " proti světlu (vidíš souvislý pás) nebo ji nakloň"
                            " a sleduj proměnu barev."
                        ),
                    },
                    "Soutisková značka (pohledem)": {
                        "ikona": "🧩",
                        "top": "14.5%",
                        "left": "29.5%",
                        "nazev": "Soutisková značka (Lícní část)",
                        "misto": "Horní část bankovky vlevo od stromu",
                        "popis": (
                            "Lícní část kroužku s písmeny. Při pohledu proti"
                            " světlu se přesně spojí s druhou částí vytištěnou"
                            " na rubu v celistvý symbol."
                        ),
                        "kontrola": (
                            "🔍 **Jak zkontrolovat:** Prohlédni si značku"
                            " proti světlu – obě poloviny (z líce i rubu)"
                            " vytvoří přesný kruhový symbol."
                        ),
                    },
                    "Opticky proměnlivá barva (naklopením)": {
                        "ikona": "🎨",
                        "top": "18.5%",
                        "left": "41.5%",
                        "nazev": "Opticky proměnlivá barva (Lipový list)",
                        "misto": "Horní část stromu nad nápisem TISÍC",
                        "popis": (
                            "Stylizovaný lipový list vytištěný speciální"
                            " barvou. Při naklonění bankovky mění barvu ze"
                            " zlatavé/hnědé na zelenou."
                        ),
                        "kontrola": (
                            "🔄 **Jak zkontrolovat:** Nakloň bankovku pod"
                            " úhlem naproti světlu – sleduj proměnu barvy"
                            " lipového listu."
                        ),
                    },
                    "Reliéfní tisk (hmatem)": {
                        "ikona": "🖐️",
                        "top": "48%",
                        "left": "70%",
                        "nazev": "Reliéfní tisk (Portrét Františka Palackého)",
                        "misto": "Portrét Palackého, texty a hmatové značky",
                        "popis": (
                            "Vystouplý povrch hlubotisku nahmatatelný prsty na"
                            " lícové straně bankovky."
                        ),
                        "kontrola": (
                            "👉 **Jak zkontrolovat:** Přejeď bříškem prstu po"
                            " portrétu Františka Palackého nebo po nápisu"
                            " 'TISÍC KORUN ČESKÝCH'."
                        ),
                    },
                    "Hmatová značka pro nevidomé (hmatem)": {
                        "ikona": "🔲",
                        "top": "9%",
                        "left": "93%",
                        "nazev": "Hmatová značka pro nevidomé",
                        "misto": "Pravý horní roh lícní strany",
                        "popis": (
                            "Speciální vystouplé čárky vytištěné hlubotiskem v"
                            " pravém horním rohu k rozpoznání hodnoty 1000 Kč"
                            " hmatem."
                        ),
                        "kontrola": (
                            "👉 **Jak zkontrolovat:** Nahmatáš prstem"
                            " vystoupené svislé čárky v pravém rohu."
                        ),
                    },
                }

                p_sel_lic = st.selectbox(
                    "Zvol prvek na lícní straně:",
                    list(prvky_lic.keys()),
                    key="k2_lic_sel",
                )
                det_lic = prvky_lic[p_sel_lic]

                if img_lic_base64:
                    st.markdown(
                        f"""
                    <div style="position: relative; width: 100%; max-width: 650px; margin: 15px auto; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.2); border: 1px solid #cbd5e1;">
                        <img src="{img_lic_base64}" alt="1000 Kč - Líc" style="width: 100%; height: auto; display: block;" />
                        <div style="position: absolute; top: {det_lic["top"]}; left: {det_lic["left"]}; transform: translate(-50%, -50%); z-index: 10;">
                            <div style="background-color: #ef4444; color: white; width: 38px; height: 38px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 18px; border: 2.5px solid white; box-shadow: 0 0 15px #ef4444;">
                                {det_lic["ikona"]}
                            </div>
                        </div>
                    </div>
                    """,
                        unsafe_allow_html=True,
                    )
                else:
                    st.warning(
                        "⚠️ Obrázek '1000_czk_lic.jpg' nebyl nalezen v"
                        " repozitáři."
                    )

                st.info(
                    f"{det_lic['ikona']} **{det_lic['nazev']}**"
                    f" ({det_lic['misto']})\n\n{det_lic['popis']}\n\n{det_lic['kontrola']}"
                )

            with tab_rub:
                prvky_rub = {
                    "Soutisková značka z rubu (pohledem)": {
                        "ikona": "🧩",
                        "top": "14.5%",
                        "left": "70.5%",
                        "nazev": "Soutisková značka (Rubová část)",
                        "misto": "Pravá horní část rubové strany",
                        "popis": (
                            "Druhá polovina soutiskové značky. Z rubu je vidět"
                            " zrcadlově doplněná část kroužku. Proti světlu"
                            " vytváří kompletní symbol."
                        ),
                        "kontrola": (
                            "🔍 **Jak zkontrolovat:** Při pohledu proti světlu"
                            " zapadne do lícní části."
                        ),
                    },
                    "Vodoznak z rubu (pohledem)": {
                        "ikona": "💧",
                        "top": "48%",
                        "left": "86%",
                        "nazev": "Vodoznak (pohled z rubu)",
                        "misto": "Pravý nepotištěný okraj rubové strany",
                        "popis": (
                            "Vodoznak je stranově převrácený (zrcadlový)"
                            " portrét Františka Palackého, viditelný stejně"
                            " zřetelně i z rubové strany."
                        ),
                        "kontrola": (
                            "👀 **Jak zkontrolovat:** Zvedni bankovku a podívej"
                            " se na pravý nepotištěný okraj proti světlu."
                        ),
                    },
                    "Sériové číslo vodorovné": {
                        "ikona": "🔢",
                        "top": "85%",
                        "left": "60%",
                        "nazev": "Sériové číslo (černé vodorovné)",
                        "misto": "Pravá spodní část pod státním znakem",
                        "popis": (
                            "Vodorovně tištěné sériové číslo bankovky v černé"
                            " barvě, které pod UV světlem zeleně světélkuje."
                        ),
                        "kontrola": (
                            "💡 **Jak zkontrolovat:** Zkontroluj číslo očima"
                            " nebo pod UV lampou."
                        ),
                    },
                    "Sériové číslo svislé": {
                        "ikona": "🔤",
                        "top": "50%",
                        "left": "5%",
                        "nazev": "Sériové číslo (červené svislé)",
                        "misto": "Levý okraj rubové strany",
                        "popis": (
                            "Svisle tištěná série a číslo bankovky v červené"
                            " barvě."
                        ),
                        "kontrola": (
                            "👀 **Jak zkontrolovat:** Zkontroluj shodu série s"
                            " vodorovným číslem."
                        ),
                    },
                    "Státní znak ČR": {
                        "ikona": "🦁",
                        "top": "48%",
                        "left": "63%",
                        "nazev": "Velký státní znak ČR",
                        "misto": "Pravá středová část rubu",
                        "popis": (
                            "Vyobrazení velkého státního znaku České republiky"
                            " v rohu nad zámeckým motivem."
                        ),
                        "kontrola": (
                            "🔍 **Jak zkontrolovat:** Detailní tisk státního"
                            " znaku."
                        ),
                    },
                }

                p_sel_rub = st.selectbox(
                    "Zvol prvek na rubové straně:",
                    list(prvky_rub.keys()),
                    key="k2_rub_sel",
                )
                det_rub = prvky_rub[p_sel_rub]

                if img_rub_base64:
                    st.markdown(
                        f"""
                    <div style="position: relative; width: 100%; max-width: 650px; margin: 15px auto; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.2); border: 1px solid #cbd5e1;">
                        <img src="{img_rub_base64}" alt="1000 Kč - Rub" style="width: 100%; height: auto; display: block;" />
                        <div style="position: absolute; top: {det_rub["top"]}; left: {det_rub["left"]}; transform: translate(-50%, -50%); z-index: 10;">
                            <div style="background-color: #3b82f6; color: white; width: 38px; height: 38px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 18px; border: 2.5px solid white; box-shadow: 0 0 15px #3b82f6;">
                                {det_rub["ikona"]}
                            </div>
                        </div>
                    </div>
                    """,
                        unsafe_allow_html=True,
                    )
                else:
                    st.warning(
                        "⚠️ Obrázek '1000_czk_rub.jpg' nebyl nalezen v"
                        " repozitáři."
                    )

                st.info(
                    f"{det_rub['ikona']} **{det_rub['nazev']}**"
                    f" ({det_rub['misto']})\n\n{det_rub['popis']}\n\n{det_rub['kontrola']}"
                )

        # 1.2.5 Kdo ČNB řídí
        with st.container(border=True):
            st.markdown("### 1.2.5 Kdo ČNB řídí")
            st.write(
                "Nejvyšším řídicím orgánem ČNB je **bankovní rada**. Ta"
                " rozhoduje například o měnové politice, úrokových sazbách a"
                " dalších zásadních otázkách fungování ČNB."
            )
            st.write("Bankovní rada má **sedm členů**:")
            st.markdown("""
            * guvernér,
            * dva viceguvernéři,
            * čtyři další členové bankovní rady.
            """)
            st.write(
                "Členy bankovní rady jmenuje prezident republiky. V čele ČNB"
                " stojí guvernér. Guvernér reprezentuje ČNB navenek a řídí"
                " jednání bankovní rady. V současnosti je guvernérem ČNB Aleš"
                " Michl."
            )

            st.markdown(
                """
            <div class='box-gray'>
                🧭 <strong>Jak si to představit:</strong> Bankovní rada je jako „řídicí tým“ centrální banky. Nerozhoduje o tom, komu banka dá spotřebitelský úvěr. Rozhoduje o pravidlech a nastavení systému, který ovlivňuje všechny banky a celou ekonomiku.
            </div>
            """,
                unsafe_allow_html=True,
            )

        # 1.2.6 Jak ČNB zasahuje do ekonomiky
        with st.container(border=True):
            st.markdown("### 1.2.6 Jak ČNB zasahuje do ekonomiky")
            st.write(
                "ČNB neřídí ekonomiku příkazem typu „zdražte“ nebo „zlevněte“."
                " Ovlivňuje ekonomiku hlavně nepřímo — přes cenu peněz, důvěru"
                " a pravidla finančního trhu."
            )
            st.write("Nejdůležitější nástroje jsou:")
            st.markdown("""
            * **úrokové sazby** — když ČNB sazby zvýší, úvěry bývají dražší a spoření atraktivnější; když sazby sníží, úvěry mohou zlevnit a ekonomická aktivita se může podpořit,
            * **operace na finančním trhu** — ČNB může stahovat nebo dodávat likviditu bankovnímu systému,
            * **povinné minimální rezervy** — banky musí držet část prostředků u centrální banky,
            * **devizové intervence** — ve výjimečných situacích může ČNB nakupovat nebo prodávat měny a tím ovlivňovat kurz koruny,
            * **makroobezřetnostní politika** — ČNB může nastavovat pravidla, která mají zabránit nadměrnému zadlužování a přehřívání finančního trhu,
            * **dohled a regulace** — kontroluje, zda finanční instituce dodržují pravidla a mají dostatečnou odolnost.
            """)

            st.markdown(
                """
            <div class='box-gray'>
                🧰 <strong>Hlavní nástroje ČNB:</strong> ČNB používá hlavně nástroje měnové politiky, nástroje pro řízení likvidity bankovního systému, devizové nástroje, dohledové nástroje a makroobezřetnostní pravidla. Nejde o jeden „kouzelný knoflík“, ale o kombinaci opatření, která ovlivňují cenu peněz, množství peněz v oběhu, chování bank a stabilitu finančního systému.
            </div>
            """,
                unsafe_allow_html=True,
            )

            st.markdown(
                """
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
            """,
                unsafe_allow_html=True,
            )

            st.markdown("##### Repo sazba lidsky")
            st.write(
                "Když média říkají, že „ČNB zvýšila sazby“, často mluví hlavně"
                " o repo sazbě. Ta je důležitým signálem pro celý finanční trh."
                " Banky podle ní upravují vlastní sazby u úvěrů a vkladů."
                " Neznamená to, že se hypotéka nebo spořicí účet změní přes"
                " noc stejně u všech bank, ale směr rozhodnutí ČNB se do"
                " bankovních produktů postupně promítá."
            )

            st.markdown("#### 🧮 Mini kalkulačka: Repo sazba v praxi")
            st.write("Porovnej dvě situace:")
            st.markdown("""
            | Situace | Spoření | Úvěry | Typický dopad |
            | :--- | :--- | :--- | :--- |
            | **Nižší sazby** | nižší výnos | levnější půjčky | větší chuť utrácet a investovat |
            | **Vyšší sazby** | vyšší výnos | dražší půjčky | větší motivace spořit, menší chuť se zadlužovat |
            """)

            st.write(
                "**Úkol:** Vyber částku 20 000 Kč na spořicím účtu a půjčku 100"
                " 000 Kč. Spočítej orientačně, jak se změní roční úrok při"
                " sazbě 3 %, 5 % a 7 %:"
            )

            c_sazba = st.select_slider(
                "Zvol úrokovou sazbu:",
                options=[3.0, 5.0, 7.0],
                value=5.0,
                key="k2_exact_repo_slider",
            )

            calc_vynos = 20000 * (c_sazba / 100)
            calc_urok = 100000 * (c_sazba / 100)

            res_c1, res_c2 = st.columns(2)
            res_c1.metric(
                "Roční výnos ze spoření (20 000 Kč)",
                f"{calc_vynos:,.0f} Kč".replace(",", " "),
            )
            res_c2.metric(
                "Roční úrok z půjčky (100 000 Kč)",
                f"{calc_urok:,.0f} Kč".replace(",", " "),
            )

            if "vykresli_otazku_fn" in st.session_state:
                st.session_state["vykresli_otazku_fn"](
                    "2.2.1",
                    "Napiš krátký komentář: Proč stejné rozhodnutí ČNB může"
                    " někomu pomoci a jinému uškodit?",
                    "2",
                    st.session_state.get("ulozene_odpovedi", {}),
                )

            st.write(
                "**Příklad: co se stane, když ČNB zvýší úrokové sazby?** Vyšší"
                " sazby obvykle zdražují půjčky. Domácnosti a firmy si proto"
                " mohou méně půjčovat a méně utrácet. Zároveň může být"
                " výhodnější spořit. Tlak na růst cen se tím může snížit."
                " Nevýhodou je, že dražší úvěry mohou zpomalit investice firem,"
                " hypotéky nebo spotřebu."
            )

            st.markdown(
                "#### 🧮 Simulace: Vyšší sazby, inflace a hypotéka"
            )
            st.write(
                "Situace: ČNB drží měnovou politiku přísnější, aby brzdila"
                " inflaci. V roce 2026 byla repo sazba ČNB kolem 3,5 %,"
                " průměrné hypoteční sazby se u nových hypoték pohybovaly"
                " přibližně okolo 5 % p.a. a nižší inflaci budeme v modelu"
                " počítat jako 2 %, protože přibližně kolem této hodnoty se"
                " pohybujeme v dlouhodobém inflačním cíli ČNB."
            )
            st.write(
                "Aby to bylo na první pohled: Porovnáme jednu domácnost ve dvou"
                " světech. V obou světech má stejnou hypotéku 3 000 000 Kč na"
                " 25 let a stejné běžné měsíční výdaje 40 000 Kč bez"
                " hypotéky. Liší se jen úroky a inflace."
            )

            with st.expander(
                "Co znamená „koš 40 000 Kč“ (Detailní rozpis)"
            ):
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

            st.write(
                "**Jednoduchý závěr pro žáka:** Pokud má domácnost velkou"
                " hypotéku, vyšší sazby ji bolí hned a velmi viditelně. Nižší"
                " inflace jí sice pomáhá, protože nákupy nezdražují tak"
                " rychle, ale v tomto modelu to nestačí vyrovnat dražší"
                " hypotéku. Proto lidé často reagují na vysoké sazby jako na"
                " „červenou na býka“ — splátka úvěru je jedna konkrétní částka"
                " na účtu, zatímco přínos nižší inflace je rozptýlený v cenách"
                " mnoho nákupů."
            )
            st.write(
                "**Pozor:** To neznamená, že vyšší sazby jsou zbytečné."
                " Pomáhají brzdit inflaci v celé ekonomice, chránit hodnotu"
                " mezd a úspor a bránit tomu, aby se zdražování utrhlo z řetězu."
                " Jen je potřeba rozlišit pohled celé ekonomiky a pohled"
                " konkrétní zadlužené domácnosti."
            )

            st.write(
                "**Příklad: co se stane, když ČNB sníží úrokové sazby?** Nižší"
                " sazby mohou zlevnit úvěry a podpořit spotřebu i investice."
                " Lidé a firmy si mohou snadněji půjčovat. Pokud je ale"
                " ekonomika už přehřátá, příliš levné peníze mohou podporovat"
                " inflaci nebo vznik cenových bublin, například na trhu"
                " nemovitostí."
            )

        # 1.2.7 Koho a co ČNB řídí
        with st.container(border=True):
            st.markdown("### 1.2.7 Koho a co ČNB „řídí“ a koho ne")
            st.write(
                "ČNB neřídí osobní účty občanů a neurčuje jednotlivým lidem,"
                " kolik si mohou půjčit. Neřídí ani každodenní obchodní"
                " rozhodnutí komerčních bank. Má ale silný vliv na pravidla a"
                " prostředí, ve kterém banky a další finanční instituce fungují."
            )
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

            st.markdown(
                """
            <div class='box-red'>
                ⚠️ <strong>Pozor na častý omyl:</strong> ČNB není „nadřízená pobočka“ tvojí banky, která řeší každou reklamaci platební karty. Reklamaci řeší nejdříve tvoje banka. ČNB ale dohlíží na to, aby finanční instituce dodržovaly pravidla.
            </div>
            """,
                unsafe_allow_html=True,
            )

            st.markdown("#### 🧩 Třídicí hra: ČNB, nebo komerční banka?")
            st.write(
                "Rozděl výroky do tří skupin: ČNB, komerční banka, souvisí s"
                " oběma:"
            )

            v1 = st.selectbox(
                "1. vydává bankovky a mince:",
                ["Vyber...", "ČNB", "Komerční banka", "Souvisí s oběma"],
                key="k2_v1",
            )
            v2 = st.selectbox(
                "2. vede běžný účet:",
                ["Vyber...", "ČNB", "Komerční banka", "Souvisí s oběma"],
                key="k2_v2",
            )
            v3 = st.selectbox(
                "3. poskytuje hypotéku:",
                ["Vyber...", "ČNB", "Komerční banka", "Souvisí s oběma"],
                key="k2_v3",
            )
            v4 = st.selectbox(
                "4. nastavuje základní úrokové sazby:",
                ["Vyber...", "ČNB", "Komerční banka", "Souvisí s oběma"],
                key="k2_v4",
            )
            v5 = st.selectbox(
                "5. vydává platební kartu:",
                ["Vyber...", "ČNB", "Komerční banka", "Souvisí s oběma"],
                key="k2_v5",
            )
            v6 = st.selectbox(
                "6. dohlíží na banky:",
                ["Vyber...", "ČNB", "Komerční banka", "Souvisí s oběma"],
                key="k2_v6",
            )
            v7 = st.selectbox(
                "7. spravuje devizové rezervy:",
                ["Vyber...", "ČNB", "Komerční banka", "Souvisí s oběma"],
                key="k2_v7",
            )
            v8 = st.selectbox(
                "8. umožňuje platbu mobilem:",
                ["Vyber...", "ČNB", "Komerční banka", "Souvisí s oběma"],
                key="k2_v8",
            )
            v9 = st.selectbox(
                "9. podílí se na důvěře ve finanční systém:",
                ["Vyber...", "ČNB", "Komerční banka", "Souvisí s oběma"],
                key="k2_v9",
            )
            v10 = st.selectbox(
                "10. souvisí s platebním stykem:",
                ["Vyber...", "ČNB", "Komerční banka", "Souvisí s oběma"],
                key="k2_v10",
            )

            if "vykresli_otazku_fn" in st.session_state:
                st.session_state["vykresli_otazku_fn"](
                    "2.2.2",
                    "Bonus k třídicí hře: U každého výroku vysvětli, jak se"
                    " dotýká běžného života:",
                    "2",
                    st.session_state.get("ulozene_odpovedi", {}),
                )

            if st.button(
                "Vyhodnotit třídicí hru 💾", key="k2_v_eval_btn"
            ):
                if (
                    v1 == "ČNB"
                    and v2 == "Komerční banka"
                    and v3 == "Komerční banka"
                    and v4 == "ČNB"
                    and v5 == "Komerční banka"
                    and v6 == "ČNB"
                    and v7 == "ČNB"
                    and v8 == "Komerční banka"
                    and v9 == "Souvisí s oběma"
                    and v10 == "Souvisí s oběma"
                ):
                    st.success(
                        "🎉 Skvělé! Všechny položky jsi zařadil/a přesně podle"
                        " textu."
                    )
                else:
                    st.error(
                        "Některé položky nejsou zařazeny správně. Zkontroluj si"
                        " zařazení!"
                    )

        # 1.2.8 Komerční banky
        with st.container(border=True):
            st.markdown("### 1.2.8 Komerční banky: banky pro občany a firmy")
            st.write(
                "Komerční banky jsou finanční instituce, které podnikají na"
                " finančním trhu. Jejich hlavní činností je přijímat vklady,"
                " poskytovat úvěry a zprostředkovávat platební styk. Potřebují"
                " bankovní licenci a podléhají dohledu ČNB."
            )

            st.markdown(
                """
            <div class='box-blue'>
                🏧 <strong>Komerční banka v jedné větě:</strong> Přijímá peníze od klientů, vede jim účty, umožňuje platby a část získaných zdrojů půjčuje jiným klientům formou úvěrů.
            </div>
            """,
                unsafe_allow_html=True,
            )
            st.write(
                "Komerční banky jsou obchodní společnosti. Řídí je jejich"
                " vlastní orgány, například představenstvo a management banky,"
                " a kontrolují je vlastníci, dozorčí orgány, auditoři a"
                " regulátor. Zároveň musí dodržovat zákony, pravidla"
                " kapitálové přiměřenosti, pravidla proti praní špinavých peněz,"
                " pravidla ochrany spotřebitele a další regulaci."
            )

        # 1.2.9 Co poskytují občanům
        with st.container(border=True):
            st.markdown("### 1.2.9 Co komerční banky poskytují občanům")
            st.write(
                "Pro běžného člověka je banka hlavně místem, kde se spravují"
                " každodenní peníze. Banka může poskytovat například:"
            )
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

            st.markdown(
                """
            <div class='box-purple'>
                📱 <strong>Moderní realita:</strong> Pro mnoho mladých lidí už banka není pobočka. Je to aplikace, ve které vidí zůstatek, platí mobilem, nastavují limity, blokují kartu, kontrolují předplatná a posílají peníze přes QR kód.
            </div>
            """,
                unsafe_allow_html=True,
            )

        # 1.2.10 Co poskytují firmám
        with st.container(border=True):
            st.markdown("### 1.2.10 Co komerční banky poskytují firmám")
            st.write(
                "Firmy potřebují banky nejen k placení faktur. Banky jim"
                " pomáhají financovat provoz, investice a obchod."
            )
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
            st.markdown(
                "### 1.2.11 Aktivní, pasivní a neutrální operace bank"
            )
            st.write(
                "Činnosti komerčních bank se často rozdělují na pasivní,"
                " aktivní a neutrální operace."
            )

            st.markdown(
                """
            | Typ operace | Co znamená | Příklady |
            | :--- | :--- | :--- |
            | **Pasivní operace** | Banka získává zdroje. Z pohledu banky jde o závazky vůči klientům nebo investorům. | běžné účty, spořicí účty, termínované vklady, vydané bankovní dluhopisy, přijaté mezibankovní úvěry |
            | **Aktivní operace** | Banka peníze umísťuje tak, aby vydělávala. Z pohledu banky jde o aktiva. | spotřebitelské úvěry, hypotéky, podnikatelské úvěry, kontokorenty, kreditní karty, nákup cenných papírů, mezibankovní úvěry poskytnuté jiným bankám |
            | **Neutrální operace** | Banka poskytuje služby, ze kterých získává poplatky nebo provize, ale přímo při nich nepůjčuje vlastní peníze jako u úvěru. | platební styk, vedení účtu, směna měn, zprostředkování investic, úschova cenností, poradenství, bankovní záruky, inkaso, dokumentární akreditiv |
            """,
                unsafe_allow_html=True,
            )

            st.markdown(
                """
            <div class='box-gray'>
                🧮 <strong>Jednoduchá logika banky:</strong> Banka přijímá vklady za určitý úrok a půjčuje peníze za vyšší úrok. Rozdíl mezi úrokem z úvěrů a úrokem z vkladů je jedním ze zdrojů jejích výnosů. Dalším zdrojem jsou poplatky a provize za služby.
            </div>
            """,
                unsafe_allow_html=True,
            )

            with st.expander(
                "Pasivní operace: jak banka získává peníze (Podrobně)"
            ):
                st.write(
                    "Pasivní operace jsou činnosti, při kterých banka získává"
                    " zdroje. Říká se jim pasivní proto, že z pohledu bankovní"
                    " rozvahy vzniká bance závazek: banka peníze klientovi"
                    " dluží."
                )
                st.markdown("""
                * **běžné účty** — klient má peníze dostupné pro každodenní platby; banka je eviduje jako závazek vůči klientovi,
                * **spořicí účty** — klient ukládá peníze s vyšším úrokem než na běžném účtu, ale obvykle s vysokou dostupností,
                * **termínované vklady** — klient uloží peníze na předem určenou dobu a za to získá sjednaný úrok,
                * **vkladové produkty pro firmy** — firmy ukládají volné prostředky a banka s nimi může dále pracovat podle pravidel likvidity,
                * **emise bankovních dluhopisů** — banka si půjčuje od investorů tím, že vydá dluhopis,
                * **mezibankovní úvěry přijaté** — banka si půjčí od jiné banky,
                * **vlastní kapitál banky** — peníze vlastníků, které slouží jako bezpečnostní polštář.
                """)
                st.info(
                    "📥 **Příklad pasivní operace:** Student si uloží 5 000 Kč"
                    " na spořicí účet. Pro studenta je to úspora. Pro banku je to"
                    " zdroj peněz a zároveň závazek, protože banka musí umožnit"
                    " výběr podle podmínky účtu."
                )

            with st.expander(
                "Aktivní operace: jak banka peníze používá (Podrobně)"
            ):
                st.write(
                    "Aktivní operace jsou činnosti, při kterých banka umísťuje"
                    " získané peníze tak, aby vydělávala. Z pohledu banky jde o"
                    " aktiva: banka má pohledávku za klientem nebo vlastní"
                    " určitý finanční nástroj."
                )
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
                st.info(
                    "📤 **Příklad aktivní operace:** Banka poskytne rodině"
                    " hypotéku. Rodina získá peníze na bydlení, ale bance vzniká"
                    " pohledávka: rodina musí úvěr splácet i s úrokem."
                )

            with st.expander(
                "Neutrální operace: služby za poplatky a provize (Podrobně)"
            ):
                st.write(
                    "Neutrální operace nejsou hlavně o tom, že banka přijímá"
                    " vklady nebo poskytuje úvěry. Banka při nich zajišťuje"
                    " služby a vydělává například na poplatcích nebo provizích."
                )
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

            st.markdown(
                "#### 🧩 Rozhodovací karty: aktivní, pasivní, nebo neutrální?"
            )
            st.write(
                "U každé situace urči typ bankovní operace a vysvětli ji z"
                " pohledu banky:"
            )

            rk1 = st.selectbox(
                "1. Klient vloží 10 000 Kč na spořicí účet:",
                ["Vyber...", "Pasivní", "Aktivní", "Neutrální"],
                key="k2_rk1",
            )
            rk2 = st.selectbox(
                "2. Rodina si vezme hypotéku:",
                ["Vyber...", "Pasivní", "Aktivní", "Neutrální"],
                key="k2_rk2",
            )
            rk3 = st.selectbox(
                "3. Student zaplatí kartou v kavárně:",
                ["Vyber...", "Pasivní", "Aktivní", "Neutrální"],
                key="k2_rk3",
            )
            rk4 = st.selectbox(
                "4. Firma požádá o provozní úvěr:",
                ["Vyber...", "Pasivní", "Aktivní", "Neutrální"],
                key="k2_rk4",
            )
            rk5 = st.selectbox(
                "5. Klient si smění koruny na eura:",
                ["Vyber...", "Pasivní", "Aktivní", "Neutrální"],
                key="k2_rk5",
            )
            rk6 = st.selectbox(
                "6. Banka vydá vlastní dluhopis:",
                ["Vyber...", "Pasivní", "Aktivní", "Neutrální"],
                key="k2_rk6",
            )
            rk7 = st.selectbox(
                "7. Podnikatel používá platební terminál:",
                ["Vyber...", "Pasivní", "Aktivní", "Neutrální"],
                key="k2_rk7",
            )

            if st.button("Vyhodnotit rozhodovací karty 💾", key="k2_rk_btn"):
                if (
                    rk1 == "Pasivní"
                    and rk2 == "Aktivní"
                    and rk3 == "Neutrální"
                    and rk4 == "Aktivní"
                    and rk5 == "Neutrální"
                    and rk6 == "Pasivní"
                    and rk7 == "Neutrální"
                ):
                    st.success(
                        "🎉 Skvělé! Rozdíly mezi aktivními, pasivními a"
                        " neutrálními operacemi ovládáš na jedničku."
                    )
                else:
                    st.error(
                        "Některá odpověď nesouhlasí. Zkontroluj tabulku výše!"
                    )

        # 1.2.12 Jak banka vydělává a rizika
        with st.container(border=True):
            st.markdown(
                "### 1.2.12 Jak banka vydělává a proč musí hlídat riziko"
            )
            st.write(
                "Banka nevydělává jen tím, že „má peníze“. Vydělává hlavně na:"
            )
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

            st.markdown(
                """
            <div class='box-red'>
                🔐 <strong>Proč existuje regulace:</strong> Kdyby banky riskovaly příliš mnoho, neohrozily by jen sebe. Ohrozily by vklady klientů, firmy, platební systém i celou ekonomiku. Proto jsou banky přísně regulované a dohlížené.
            </div>
            """,
                unsafe_allow_html=True,
            )

        # 1.2.13 Licence a dohled
        with st.container(border=True):
            st.markdown("### 1.2.13 Bankovní licence a dohled")
            st.write(
                "Banka nemůže začít fungovat jen proto, že si někdo založí"
                " aplikaci a napíše „banka“. K poskytování bankovních služeb"
                " potřebuje povolení. V České republice nad bankami dohlíží"
                " ČNB."
            )
            st.write("ČNB sleduje například:")
            st.markdown("""
            * zda banka má dost kapitálu,
            * zda rozumně řídí rizika,
            * zda dodržuje pravidla pro ochranu klientů,
            * zda plní povinnosti proti praní špinavých peněz,
            * zda má bezpečné systémy,
            * zda je schopna zvládnout krizové situace.
            """)

            st.write(
                "**Proč banka nemůže půjčit úplně všechno, co má?** Protože"
                " musí zvládnout běžné výběry klientů, platby, regulatorní"
                " požadavky a krizové situace. Banka musí držet určité rezervy"
                " a kapitál. Pokud by půjčovala příliš rizikově, mohla by"
                " ohrozit důvěru klientů i stabilitu celého systému."
            )

            st.markdown("#### 🛠️ Mini audit banky")
            st.write(
                "Představ si, že jsi bankovní analytik. Máš posoudit, jestli"
                " banka nepodstupuje moc velké riziko. Sleduj tři otázky:"
            )

            ma1 = st.radio(
                "1. Půjčuje banka lidem a firmám, kteří pravděpodobně zvládnou"
                " splácet?",
                [
                    "Ano, prověřuje bonitu",
                    "Ne, půjčí úplně každému bez kontroly",
                ],
                key="k2_ma1",
            )
            ma2 = st.radio(
                "2. Má dost peněz pro běžné výběry a platby klientů?",
                [
                    "Ano, drží likviditní rezervy",
                    "Ne, všechno rozjala do 30letých půjček",
                ],
                key="k2_ma2",
            )
            ma3 = st.radio(
                "3. Má dost kapitálu, aby zvládla případné ztráty?",
                [
                    "Ano, drží vyžadovaný kapitál",
                    "Ne, nemá žádný vlastní kapitál",
                ],
                key="k2_ma3",
            )

            if "vykresli_otazku_fn" in st.session_state:
                st.session_state["vykresli_otazku_fn"](
                    "2.2.3",
                    "Na závěr napiš doporučení: Co by měla banka zlepšit, aby"
                    " byla bezpečnější?",
                    "2",
                    st.session_state.get("ulozene_odpovedi", {}),
                )

            if st.button("Vyhodnotit audit banky 💾", key="k2_ma_btn"):
                if (
                    ma1 == "Ano, prověřuje bonitu"
                    and ma2 == "Ano, drží likviditní rezervy"
                    and ma3 == "Ano, drží vyžadovaný kapitál"
                ):
                    st.success(
                        "✅ **Správný audit:** Banka splňuje klíčové podmínky"
                        " obezřetného podnikání a ochrany vkladatelů."
                    )
                else:
                    st.error(
                        "⚠️ **Rizikové zjištění:** Banka nesplňuje bezpečnostní"
                        " pravidla a hrozí jí zásah ze strany ČNB!"
                    )

        # 1.2.14 Vklady a jejich ochrana
        with st.container(border=True):
            st.markdown("### 1.2.14 Vklady a jejich ochrana")
            st.write(
                "Vklady klientů v bankách jsou v zákonem stanoveném rozsahu"
                " chráněny systémem pojištění vkladů. Smyslem je posílit důvěru"
                " lidí v bankovní systém a snížit riziko paniky při problémech"
                " banky."
            )

            st.markdown(
                """
            <div class='box-blue'>
                🛟 <strong>Do jaké výše jsou vklady pojištěny:</strong> V České republice jsou pojištěné vklady u bank, družstevních záložen a stavebních spořitelen chráněny zpravidla do výše 100 000 EUR na jednoho klienta u jedné banky. V přepočtu jde přibližně o 2,4–2,5 milionu Kč, podle aktuálního kurzu. Pokud má člověk u jedné banky více účtů, limit se obvykle počítá dohromady za daného klienta u dané banky, ne zvlášť za každý účet.
            </div>
            """,
                unsafe_allow_html=True,
            )

            st.markdown(
                """
            | Situace | Jak to zjednodušeně funguje | Příklad |
            | :--- | :--- | :--- |
            | **Klient má u jedné banky 500 000 Kč** | Částka je pod limitem pojištění vkladů. | Při krachu banky by měla být chráněna celá částka. |
            | **Klient má u jedné banky 2 000 000 Kč** | Částka je stále přibližně pod limitem 100 000 EUR. | Vklad by byl obvykle chráněn celý. |
            | **Klient má u jedné banky 4 000 000 Kč** | Část přesahuje základní limit pojištění. | Pojištěna by byla jen část do limitu; zbytek by nesl riziko. |
            | **Klient má 2 000 000 Kč v jedné bance a 2 000 000 Kč v jiné bance** | Limit se posuzuje u každé banky zvlášť. | Rozložení peněz mezi banky může snížit riziko překročení limitu. |
            """,
                unsafe_allow_html=True,
            )

            st.write(
                "**Kdo pojištění vkladů zajišťuje?** V České republice"
                " výplatu náhrad zajišťuje Garanční systém finančního trhu"
                " prostřednictvím Fondu pojištění vkladů. Pokud by banka"
                " zkrachovala a nebyla schopná vyplatit klientům vklady,"
                " systém pojištění vkladů slouží k tomu, aby klienti dostali"
                " náhradu do zákonem stanoveného limitu."
            )

            st.markdown(
                "##### Výběr hotovosti: kolik lze vybrat a kdy to hlásit bance"
            )
            st.write(
                "To, že má člověk peníze na účtu, neznamená, že si může kdykoliv"
                " bez přípravy odnést z pobočky libovolně vysokou hotovost."
                " Banka musí mít hotovost fyzicky připravenou na pobočce a"
                " zároveň musí plnit pravidla proti praní špinavých peněz."
            )

            st.markdown(
                """
            | Typ výběru | Jak to běžně funguje | Na co si dát pozor |
            | :--- | :--- | :--- |
            | **Výběr z bankomatu** | Řídí se limitem platební karty a limitem konkrétního bankomatu. | Limit si člověk často nastavuje v aplikaci, ale bankomat může mít i vlastní technické omezení. |
            | **Menší výběr na pobočce** | Obvykle lze vybrat bez předchozího objednání, pokud má pobočka hotovost k dispozici. | Každá banka může mít vlastní pravidla a limity. |
            | **Větší hotovostní výběr** | Často je vhodné nebo nutné oznámit ho bance předem, ale hranice se mezi bankami výrazně liší. | Například u ČSOB je podle zveřejněných informací potřeba předem objednat až částku převyšující 300 000 Kč; u KB se naopak uvádí hlášení už nad 100 000 Kč. |
            | **Velmi vysoký výběr** | Banka může požadovat písemné oznámení, objednání hotovosti nebo vysvětlení účelu. | Nejde o zvědavost pokladníka, ale o provozní a zákonné povinnosti banky. |
            """,
                unsafe_allow_html=True,
            )

            st.markdown(
                """
            <div class='box-red'>
                ⚠️ <strong>Důležité:</strong> Neexistuje jedno univerzální číslo, které by platilo pro všechny banky jako „do této částky nikdy nic nehlaš“. U velkých výběrů hotovosti záleží na pravidlech konkrétní banky, typu pobočky, měně, dostupnosti hotovosti a bezpečnostních pravidlech.
            </div>
            """,
                unsafe_allow_html=True,
            )

            st.markdown(
                """
            <div class='box-purple'>
                🧠 <strong>Proč banka řeší velké hotovostní výběry:</strong><br>
                • <strong>Provozní důvod:</strong> pobočka nemusí mít okamžitě připravené velké množství hotovosti.<br>
                • <strong>Bezpečnost:</strong> převoz a výdej vysoké hotovosti je rizikový.<br>
                • <strong>AML pravidla:</strong> banka musí sledovat podezřelé transakce a původ peněz.<br>
                • <strong>Ochrana klienta:</strong> neobvyklý výběr může být i signál, že je klient pod tlakem podvodníka.
            </div>
            """,
                unsafe_allow_html=True,
            )

            st.write(
                "**Příklad: výběr 300 000 Kč nebo 600 000 Kč na koupi auta:**"
                " Pokud chce klient vybrat 300 000 Kč v hotovosti, u některých"
                " bank to může být ještě běžně proveditelné bez zvláštního"
                " objednání, pokud má pobočka hotovost a klient splňuje limity"
                " účtu nebo karty. Například ČSOB uvádí, že předem je potřeba"
                " objednat až částku převyšující 300 000 Kč. Pokud ale chce"
                " klient vybrat třeba 600 000 Kč, už je mnohem"
                " pravděpodobnější, že banka bude chtít výběr předem objednat."
                " Potřebuje připravit hotovost, zajistit bezpečný provoz"
                " pobočky a splnit pravidla proti praní špinavých peněz."
            )

            st.markdown(
                """
            <div class='box-blue'>
                🛟 <strong>Co si zapamatovat:</strong> Peníze na běžném nebo spořicím účtu nejsou totéž jako hotovost v peněžence. Jsou to pohledávky vůči bance. Základní pojištění vkladů je do 100 000 EUR na klienta u jedné banky.
            </div>
            """,
                unsafe_allow_html=True,
            )

    # =========================================================================
    # 1.3 PLATEBNÍ STYK
    # =========================================================================
    elif "1.3 Platební styk" in selected_section_2:
        st.markdown(
            "<div class='sub-section-header'>1. BANKOVNÍ SYSTÉM A PENÍZE V 21."
            " STOLETÍ</div><h2>1.3 Platební styk</h2>",
            unsafe_allow_html=True,
        )
        st.write(
            "Platební styk znamená převod peněz mezi plátcem a příjemcem. Díky"
            " platebnímu styku můžeme zaplatit oběd kartou, poslat nájem"
            " převodem, nakoupit online, zaplatit fakturu přes QR kód nebo"
            " přijmout výplatu na účet."
        )

        with st.container(border=True):
            st.markdown(
                """
            <div class='box-blue'>
                💳 <strong>Základní myšlenka:</strong> Platební styk je infrastruktura důvěry. Umožňuje, aby se peníze bezpečně a prokazatelně přesunuly od toho, kdo platí, k tomu, kdo má peníze dostat.
            </div>
            """,
                unsafe_allow_html=True,
            )

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

            st.markdown(
                """
            | Druh | Co znamená | Příklady |
            | :--- | :--- | :--- |
            | **Hotovostní** | Platí se fyzickými penězi. | bankovky, mince, výběr z bankomatu, vklad hotovosti |
            | **Bezhotovostní** | Peníze se převádějí jako záznam mezi účty. | bankovní převod, platba kartou, trvalý příkaz, inkaso, QR platba |
            | **Tuzemský** | Platba probíhá v rámci České republiky. | převod mezi českými bankami v Kč |
            | **Zahraniční** | Platba směřuje do jiné země nebo v jiné měně. | SEPA platba v eurech, mezinárodní převod, platba kartou v zahraničí |
            | **Jednorázový** | Platba se zadává pro jeden konkrétní převod. | jednorázová úhrada faktury |
            | **Opakovaný** | Platba se provádí pravidelně nebo automaticky. | trvalý příkaz, SIPO, inkaso, předplatné |
            | **Okamžitý** | Peníze dorazí během několika sekund, pokud to banky podporují. | okamžitá platba mezi bankami |
            """,
                unsafe_allow_html=True,
            )

            st.markdown("#### 🧭 Aktivita: Vyber správný typ platby")
            st.write(
                "U každé situace urči, zda jde o platbu"
                " hotovostní/bezhotovostní, tuzemskou/zahraniční a"
                " jednorázovou/opakovanou:"
            )

            act_1 = st.selectbox(
                "1. Platím kávu v hotovosti:",
                [
                    "Vyber...",
                    "Hotovostní / Tuzemská / Jednorázová",
                    "Bezhotovostní / Tuzemská / Opakovaná",
                ],
                key="k2_act1",
            )
            act_2 = st.selectbox(
                "2. Posílám nájem trvalým příkazem:",
                [
                    "Vyber...",
                    "Bezhotovostní / Tuzemská / Opakovaná",
                    "Hotovostní / Zahraniční / Jednorázová",
                ],
                key="k2_act2",
            )
            act_3 = st.selectbox(
                "3. Platím Spotify předplatné:",
                [
                    "Vyber...",
                    "Bezhotovostní / Zahraniční / Opakovaná",
                    "Hotovostní / Tuzemská / Jednorázová",
                ],
                key="k2_act3",
            )
            act_4 = st.selectbox(
                "4. Nakupuji v zahraničním e-shopu:",
                [
                    "Vyber...",
                    "Bezhotovostní / Zahraniční / Jednorázová",
                    "Hotovostní / Tuzemská / Opakovaná",
                ],
                key="k2_act4",
            )
            act_5 = st.selectbox(
                "5. Posílám peníze na školní výlet přes QR kód:",
                [
                    "Vyber...",
                    "Bezhotovostní / Tuzemská / Jednorázová",
                    "Hotovostní / Zahraniční / Opakovaná",
                ],
                key="k2_act5",
            )
            act_6 = st.selectbox(
                "6. Vybírám peníze z bankomatu:",
                [
                    "Vyber...",
                    "Hotovostní operace / Tuzemská / Jednorázová",
                    "Bezhotovostní převod",
                ],
                key="k2_act6",
            )
            act_7 = st.selectbox(
                "7. Platím kartou na dovolené v cizině:",
                [
                    "Vyber...",
                    "Bezhotovostní / Zahraniční / Jednorázová",
                    "Hotovostní / Tuzemská",
                ],
                key="k2_act7",
            )

            if "vykresli_otazku_fn" in st.session_state:
                st.session_state["vykresli_otazku_fn"](
                    "2.3.1",
                    "Bonus k aktivitě plateb: U každé situace navrhni"
                    " nejbezpečnější platební nástroj:",
                    "2",
                    st.session_state.get("ulozene_odpovedi", {}),
                )

            if st.button("Vyhodnotit aktivitu plateb 💾", key="k2_act_btn"):
                if (
                    act_1 == "Hotovostní / Tuzemská / Jednorázová"
                    and act_2 == "Bezhotovostní / Tuzemská / Opakovaná"
                    and act_3 == "Bezhotovostní / Zahraniční / Opakovaná"
                    and act_4 == "Bezhotovostní / Zahraniční / Jednorázová"
                    and act_5 == "Bezhotovostní / Tuzemská / Jednorázová"
                    and act_6 == "Hotovostní operace / Tuzemská / Jednorázová"
                    and act_7 == "Bezhotovostní / Zahraniční / Jednorázová"
                ):
                    st.success(
                        "🎉 Skvělá práce! Všechny typy plateb jsi určil/a zcela"
                        " správně."
                    )
                else:
                    st.error(
                        "Některý z typů plateb je vybrán špatně. Zkontroluj"
                        " správné zařazení!"
                    )

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

            if "vykresli_otazku_fn" in st.session_state:
                st.session_state["vykresli_otazku_fn"](
                    "2.3.2",
                    "🧩 Interaktivní výzva: Vyber tři platby, které jsi"
                    " provedl/a za poslední týden. Urči, zda šlo o hotovostní"
                    " nebo bezhotovostní platbu, jednorázovou nebo opakovanou,"
                    " tuzemskou nebo zahraniční.",
                    "2",
                    st.session_state.get("ulozene_odpovedi", {}),
                )

        # 1.3.4
        with st.container(border=True):
            st.markdown("### 1.3.4 Kdo platební styk řídí a reguluje")
            st.write(
                "Platební styk není divoký prostor bez pravidel. Funguje díky"
                " spolupráci bank, platebních institucí, karetních společností,"
                " technologických poskytovatelů, obchodníků, státu a"
                " regulátorů."
            )
            st.write("V České republice má důležitou roli:")
            st.markdown("""
            * **ČNB** — provozuje a dohlíží na vybrané platební systémy a dohlíží na finanční instituce,
            * **komerční banky** — vedou účty klientů a zpracovávají platby,
            * **platební instituce a fintech firmy** — poskytují některé platební služby,
            * **karetní asociace** — nastavují pravidla karetních sítí,
            * **obchodníci a platební brány** — přijímají platby od zákazníků,
            * **právní předpisy ČR a EU** — stanovují pravidla bezpečnosti, práv klientů, odpovědnosti a ochrany spotřebitele.
            """)

            st.markdown(
                "##### CERTIS: „dálnice“ pro platby mezi českými bankami"
            )
            st.write(
                "Když posíláme peníze v českých korunách, je důležité rozlišit,"
                " jestli jde platba v rámci jedné banky, nebo mezi dvěma"
                " různými bankami."
            )

            st.markdown(
                """
            <div class='box-blue'>
                🏦 <strong>Co je CERTIS:</strong> CERTIS je český systém mezibankovního platebního styku. Zjednodušeně řečeno je to systém, přes který se v České republice zúčtovávají platby v korunách mezi různými bankami. Název CERTIS znamená Czech Express Real Time Interbank Gross Settlement System. Systém spravuje a provozuje Česká národní banka.
            </div>
            """,
                unsafe_allow_html=True,
            )

            st.markdown(
                """
            | Situace | Co se děje s platbou | Jde přes CERTIS? |
            | :--- | :--- | :--- |
            | **Platba v rámci stejné banky** | Oba účty jsou u stejné banky. Banka si platbu zúčtuje ve vlastním systému: jednomu klientovi částku odepíše, druhému připíše. | Obvykle ne. Zůstává uvnitř banky. |
            | **Platba mezi různými bankami** | Plátce má účet u jedné banky a příjemce u jiné banky. Banka plátce musí poslat mezibankovní pokyn přes systém CERTIS. | Ano. Platba se vypořádá mezi bankami přes CERTIS. |
            | **Okamžitá platba mezi různými bankami** | Pokud obě banky podporují okamžité platby, převod může proběhnout během několika sekund i mezi různými bankami. | Ano, v režimu okamžitých plateb v rámci mezibankovního systému. |
            """,
                unsafe_allow_html=True,
            )

            st.write(
                "**Příklad: spolužák ve stejné bance vs. spolužák v jiné bance:**"
                " Představ si, že posíláš 500 Kč za společný dárek."
            )
            st.markdown("""
            1. **Spolužák má účet u stejné banky:** Tvoje banka pouze upraví záznamy ve svém systému. Tobě 500 Kč odečte a spolužákovi 500 Kč připíše. Peníze nemusí „opustit“ banku.
            2. **Spolužák má účet u jiné banky:** Tvoje banka odešle pokyn do mezibankovního systému CERTIS. Přes něj se platba vypořádá mezi bankami a banka spolužáka částku připíše na jeho účet.
            """)
            st.info(
                "💡 **Jednoduše:** Když jsou oba účty ve stejné bance, banka si"
                " platbu vyřeší sama. Když jsou účty v různých bankách, musí"
                " se banky mezi sebou „domluvit“ přes mezibankovní systém. V ČR"
                " je pro korunové mezibankovní platby klíčový právě CERTIS,"
                " který spravuje ČNB."
            )

        # 1.3.5
        with st.container(border=True):
            st.markdown("### 1.3.5 Jak probíhá platba kartou")
            st.write(
                "Když přiložíš kartu nebo mobil k terminálu, vše vypadá jako"
                " jedna sekunda. Ve skutečnosti se v pozadí odehraje několik"
                " kroků:"
            )
            st.markdown("""
            1. Terminál načte platební údaje.
            2. Obchodník pošle požadavek přes platební síť.
            3. Banka ověří kartu, limit, bezpečnostní pravidla a dostupné prostředky.
            4. Platba se autorizuje nebo zamítne.
            5. Později proběhne zúčtování mezi bankami a obchodníkem.
            """)

            st.markdown(
                """
            <div class='box-red'>
                🔐 <strong>Bezpečnost:</strong> U plateb se používají limity, PIN, biometrie, potvrzení v aplikaci, 3D Secure, monitoring podezřelých transakcí a další ochranné prvky. Bezpečnost ale začíná i u uživatele: neklikat na podezřelé odkazy, nesdělovat kódy a chránit přístup do bankovnictví.
            </div>
            """,
                unsafe_allow_html=True,
            )

            st.markdown("#### 🔁 Skládačka: Cesta platby kartou")
            st.write(
                "Seřaď kroky platby kartou nebo mobilem ve správném pořadí:"
            )

            s_krok1 = st.selectbox(
                "1. krok:",
                [
                    "Vyber...",
                    "přiložení karty nebo mobilu k terminálu",
                    "terminál načte platební údaje",
                    "obchodník odešle požadavek přes platební síť",
                    "banka ověří kartu, limit a bezpečnostní pravidla",
                    "platba se schválí nebo zamítne",
                    "později proběhne zúčtování mezi bankami a obchodníkem",
                ],
                key="k2_sk1",
            )
            s_krok2 = st.selectbox(
                "2. krok:",
                [
                    "Vyber...",
                    "přiložení karty nebo mobilu k terminálu",
                    "terminál načte platební údaje",
                    "obchodník odešle požadavek přes platební síť",
                    "banka ověří kartu, limit a bezpečnostní pravidla",
                    "platba se schválí nebo zamítne",
                    "později proběhne zúčtování mezi bankami a obchodníkem",
                ],
                key="k2_sk2",
            )
            s_krok3 = st.selectbox(
                "3. krok:",
                [
                    "Vyber...",
                    "přiložení karty nebo mobilu k terminálu",
                    "terminál načte platební údaje",
                    "obchodník odešle požadavek přes platební síť",
                    "banka ověří kartu, limit a bezpečnostní pravidla",
                    "platba se schválí nebo zamítne",
                    "později proběhne zúčtování mezi bankami a obchodníkem",
                ],
                key="k2_sk3",
            )
            s_krok4 = st.selectbox(
                "4. krok:",
                [
                    "Vyber...",
                    "přiložení karty nebo mobilu k terminálu",
                    "terminál načte platební údaje",
                    "obchodník odešle požadavek přes platební síť",
                    "banka ověří kartu, limit a bezpečnostní pravidla",
                    "platba se schválí nebo zamítne",
                    "později proběhne zúčtování mezi bankami a obchodníkem",
                ],
                key="k2_sk4",
            )
            s_krok5 = st.selectbox(
                "5. krok:",
                [
                    "Vyber...",
                    "přiložení karty nebo mobilu k terminálu",
                    "terminál načte platební údaje",
                    "obchodník odešle požadavek přes platební síť",
                    "banka ověří kartu, limit a bezpečnostní pravidla",
                    "platba se schválí nebo zamítne",
                    "později proběhne zúčtování mezi bankami a obchodníkem",
                ],
                key="k2_sk5",
            )
            s_krok6 = st.selectbox(
                "6. krok:",
                [
                    "Vyber...",
                    "přiložení karty nebo mobilu k terminálu",
                    "terminál načte platební údaje",
                    "obchodník odešle požadavek přes platební síť",
                    "banka ověří kartu, limit a bezpečnostní pravidla",
                    "platba se schválí nebo zamítne",
                    "později proběhne zúčtování mezi bankami a obchodníkem",
                ],
                key="k2_sk6",
            )

            if "vykresli_otazku_fn" in st.session_state:
                st.session_state["vykresli_otazku_fn"](
                    "2.3.3",
                    "Otázky k zamyšlení u platby kartou (Kde může selhat, kdo"
                    " se účastní a proč nejde o kouzlo):",
                    "2",
                    st.session_state.get("ulozene_odpovedi", {}),
                )

            if st.button("Vyhodnotit skládačku 💾", key="k2_sk_eval_btn"):
                if (
                    s_krok1 == "přiložení karty nebo mobilu k terminálu"
                    and s_krok2 == "terminál načte platební údaje"
                    and s_krok3 == "obchodník odešle požadavek přes platební síť"
                    and s_krok4
                    == "banka ověří kartu, limit a bezpečnostní pravidla"
                    and s_krok5 == "platba se schválí nebo zamítne"
                    and s_krok6
                    == "později proběhne zúčtování mezi bankami a obchodníkem"
                ):
                    st.success(
                        "🎉 Skvělé! Kompletní řetězec platby kartou máš seřazený"
                        " zcela přesně."
                    )
                else:
                    st.error(
                        "Některý krok v pořadí nesouhlasí. Zkontroluj seznam v"
                        " bodě 1.3.5!"
                    )

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

            st.markdown(
                """
            | Situace | Co dělat | Proč |
            | :--- | :--- | :--- |
            | Přijde SMS s odkazem na „blokaci účtu“ | Neotevírat odkaz, ověřit situaci přímo v aplikaci banky nebo na oficiální lince. | Podvodníci často vytvářejí falešný pocit naléhavosti. |
            | Někdo chce autorizační kód | Nikdy ho nesdělovat. | Kód může potvrdit platbu nebo přístup k účtu. |
            | Aplikace nabízí „garantované zhodnocení“ | Ověřit licenci, rizika a reálnost slibu. | Vysoký výnos bez rizika je varovný signál. |
            """,
                unsafe_allow_html=True,
            )

            st.markdown(
                "#### 🚨 Phishing escape room: nenech se okrást jedním klikem"
            )
            st.write(
                "Pro každou zprávu rozhodni, zda je bezpečná, podezřelá nebo"
                " nebezpečná. Najdi varovný signál a navrhni správnou reakci:"
            )

            er1 = st.radio(
                "1. „Vaše karta byla zablokována. Klikněte zde a ověřte účet.“",
                ["Bezpečná", "Podezřelá / Nebezpečná (Phishing)"],
                key="k2_er1",
            )
            er2 = st.radio(
                "2. „Jsem z bezpečnostního oddělení banky. Nadiktujte mi kód z"
                " SMS.“",
                ["Bezpečná", "Podezřelá / Nebezpečná (Vishing)"],
                key="k2_er2",
            )
            er3 = st.radio(
                "3. „Investice s garantovaným výnosem 30 % měsíčně.“",
                ["Bezpečná", "Podezřelá / Nebezpečná (Podvod)"],
                key="k2_er3",
            )
            er4 = st.radio(
                "4. „Potvrďte přístup do internetového bankovnictví přes tento"
                " odkaz.“",
                ["Bezpečná", "Podezřelá / Nebezpečná (Phishing)"],
                key="k2_er4",
            )
            er5 = st.radio(
                "5. E-shop nabízí uložení karty pro příští nákup.",
                ["Standardní funkce platební brány", "Podezřelá / Nebezpečná"],
                key="k2_er5",
            )

            st.info(
                "🛡️ **Pravidlo přežití:** Banka po telefonu ani přes zprávu"
                " nechce heslo, PIN ani autorizační kód. Když cítíš tlak na"
                " rychlost, zpomal a ověřuj oficiální cestou."
            )

            if st.button("Vyhodnotit Escape Room 💾", key="k2_er_eval_btn"):
                if (
                    er1 == "Podezřelá / Nebezpečná (Phishing)"
                    and er2 == "Podezřelá / Nebezpečná (Vishing)"
                    and er3 == "Podezřelá / Nebezpečná (Podvod)"
                    and er4 == "Podezřelá / Nebezpečná (Phishing)"
                    and er5 == "Standardní funkce platební brány"
                ):
                    st.success(
                        "🎉 Skvělé! Bezpečně jsi rozpoznal/a všechna rizika"
                        " digitálního světa."
                    )
                else:
                    st.error(
                        "Některá zpráva byla vyhodnocena špatně. Pozor na"
                        " falešný tlak na čas a žádosti o kódy!"
                    )

    # =========================================================================
    # 1.4 FINTECH REVOLUCE
    # =========================================================================
    elif "1.4 Fintech" in selected_section_2:
        st.markdown(
            "<div class='sub-section-header'>1. BANKOVNÍ SYSTÉM A PENÍZE V 21."
            " STOLETÍ</div><h2>1.4 Fintech revoluce</h2>",
            unsafe_allow_html=True,
        )
        st.write(
            "Fintech je spojení slov **finance** a **technology**. Označuje"
            " firmy a služby, které pomocí technologií mění způsob, jak"
            " platíme, spoříme, investujeme, půjčujeme si, ověřujeme identitu"
            " nebo spravujeme rozpočet."
        )

        with st.container(border=True):
            st.markdown(
                """
            <div class='box-blue'>
                🚀 <strong>Fintech změna:</strong> Finance se přesunuly z pobočky do mobilu. Uživatel očekává rychlost, jednoduché ovládání, okamžité notifikace, nízké poplatky a možnost vyřídit vše online.
            </div>
            """,
                unsafe_allow_html=True,
            )

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
            st.markdown(
                "### 1.4.2 Neobanky a moderní finanční aplikace"
            )
            st.write(
                "Neobanky jsou bankovní nebo finanční služby stavěné hlavně"
                " pro mobilní prostředí. Často nemají klasickou síť poboček a"
                " soutěží jednoduchostí aplikace, rychlostí a cenou. Někdy jde o"
                " banku s bankovní licencí, jindy spíše o fintechovou platební"
                " aplikaci, která nabízí účet, kartu, směnu měn nebo další"
                " finanční služby."
            )

            st.markdown(
                """
            <div class='box-gray'>
                📱 <strong>Příklady neobank a digitálních finančních služeb dostupných v ČR:</strong><br><br>
                • <strong>Revolut</strong> — velmi známá mobilní finanční aplikace používaná pro účet, kartu, směnu měn, cestování, platby v zahraničí, investice nebo kryptoměny.<br><br>
                • <strong>Wise</strong> — služba zaměřená hlavně na levnější mezinárodní převody, víceměnový účet a platby v různých měnách.<br><br>
                • <strong>bunq</strong> — evropská digitální banka s důrazem na mobilní ovládání, více účtů, karty a práci s rozpočtem.<br><br>
                • <strong>mBank</strong> — banka s výrazně digitálním modelem a menším důrazem na klasické pobočky.<br><br>
                • <strong>Air Bank</strong> — česká banka, která se často uvádí jako příklad modernějšího, jednoduššího a digitálně orientovaného bankovnictví.
            </div>
            """,
                unsafe_allow_html=True,
            )

            st.markdown(
                """
            <div class='box-red'>
                ⚠️ <strong>Pozor na pojem neobanka:</strong> Ne každá aplikace, která vypadá jako banka, je stejná jako klasická banka v ČR. Liší se bankovní licence, pojištění vkladů, zákaznická podpora, poplatky, měny, ochrana klienta i to, kdo službu reguluje.
            </div>
            """,
                unsafe_allow_html=True,
            )

            st.markdown(
                """
            | Klasické bankovnictví | Moderní fintech / neobanka |
            | :--- | :--- |
            | Důraz na pobočku a dlouhodobý vztah s bankou. | Důraz na mobilní aplikaci a rychlé ovládání. |
            | Služby se často řešily osobně nebo přes internetbanking. | Mnoho služeb se vyřídí v telefonu během minut. |
            | Poplatky a kurzovní marže nemusely být pro klienta přehledné. | Aplikace často ukazuje poplatky, kurzy a transakce okamžitě. |
            | Změny byly pomalejší. | Nové funkce přibývají rychleji, ale uživatel musí víc hlídat rizika. |
            """,
                unsafe_allow_html=True,
            )

        # 1.4.3
        with st.container(border=True):
            st.markdown(
                "### 1.4.3 Open banking: když si aplikace rozumí s bankou"
            )
            st.write(
                "Důležitou změnou je **open banking**. Znamená, že klient může"
                " za určitých bezpečnostních podmínek povolit vybrané aplikaci"
                " přístup k informacím o účtu nebo zadání platby."
            )
            st.write("Příklad:")
            st.markdown("""
            * jedna aplikace zobrazí zůstatky z více bank,
            * rozpočtová aplikace roztřídí výdaje,
            * účetní systém firmy si načte bankovní pohyby,
            * platba v e-shopu se zadá přímo z bankovního účtu.
            """)
            st.info(
                "🔑 **Důležité:** Přístup k účtu má být vždy vědomý, omezený a"
                " odvolatelný. Uživatel by měl vědět, komu dává souhlas, k čenu"
                " a na jak dlouho."
            )

        # 1.4.4
        with st.container(border=True):
            st.markdown("### 1.4.4 Rizika fintechu")
            st.write(
                "Fintech není automaticky dobrý nebo špatný. Je to nástroj."
                " Může pomoct, ale také zrychlit chybná rozhodnutí."
            )
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
            st.markdown(
                """
            <div class='box-purple'>
                🧠 <strong>Finanční gramotnost dnes:</strong> Nestačí vědět, co je úrok. Je potřeba umět poznat, kdy aplikace tlačí na rychlost, emoce nebo FOMO. Digitální pohodlí musí jít ruku v ruce s kritickým myšlením.
            </div>
            """,
                unsafe_allow_html=True,
            )

        # 1.4.5
        with st.container(border=True):
            st.markdown(
                "### 1.4.5 Jak poznat důvěryhodnou finanční službu"
            )
            st.write(
                "Před použitím nové finanční aplikace je dobré zkontrolovat:"
            )
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

            if "vykresli_otazku_fn" in st.session_state:
                st.session_state["vykresli_otazku_fn"](
                    "2.4.1",
                    "Audit finanční aplikace (Vyber např. Revolut, Wise, PayPal"
                    " a popiš: Název, Provozovatele, Funkce, Jak vydělává,"
                    " Data, Výhody/Rizika a tvoje doporučení):",
                    "2",
                    st.session_state.get("ulozene_odpovedi", {}),
                )

            st.markdown("---")

            st.markdown("#### ⚖️ Debata: Fintech — pomocník, nebo past?")
            col_deb1, col_deb2 = st.columns(2)
            with col_deb1:
                st.success(
                    "💚 **Tým A (Pomocník):**\n"
                    "Fintech zvyšuje finanční gramotnost, šetří čas, snižuje"
                    " poplatky za převody a směnu a umožňuje snadnou kontrolu"
                    " rozpočtu."
                )
            with col_deb2:
                st.error(
                    "🔴 **Tým B (Past):**\n"
                    "Fintech zrychluje impulzivní utrácení, zjednodušuje"
                    " neuvážené zadlužování, využívá gamifikaci k investičnímu"
                    " riziku a sbírá osobní data."
                )

            if "vykresli_otazku_fn" in st.session_state:
                st.session_state["vykresli_otazku_fn"](
                    "2.4.2",
                    "Napiš své argumenty do debaty Fintech (Pomocník vs."
                    " Past) a příklad z běžného života:",
                    "2",
                    st.session_state.get("ulozene_odpovedi", {}),
                )

    # =========================================================================
    # 2.1 OSOBNÍ FINANCE V 21. STOLETÍ
    # =========================================================================
    elif "2.1 Osobní finance" in selected_section_2:
        st.markdown(
            "<div class='sub-section-header'>2. OSOBNÍ FINANCE A „ALGORITMY"
            " BOHATSTVÍ“</div><h2>2.1 Osobní finance v 21. století: proč je to"
            " těžší, než se zdá</h2>",
            unsafe_allow_html=True,
        )
        st.write(
            "Osobní finance nejsou jen otázka toho, kolik člověk vydělává. Jsou"
            " to každodenní rozhodnutí: za co utratím peníze, co odložím, co si"
            " půjčím, jak poznám riziko a jak se nenechám řídit reklamou, tlakem"
            " okolí nebo algoritmem v aplikaci."
        )

        with st.container(border=True):
            st.markdown(
                """
            <div class='box-purple'>
                🧠 <strong>Základní myšlenka:</strong> Finanční gramotnost v 21. století znamená umět zacházet nejen s penězi, ale i s digitálním prostředím, které naše finanční rozhodování ovlivňuje.
            </div>
            """,
                unsafe_allow_html=True,
            )

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
            st.markdown(
                """
            <div class='box-red'>
                ⚠️ <strong>Současný problém:</strong> Mnoho lidí nemá problém jen s nedostatkem informací, ale s prostředím, které podporuje okamžité rozhodování. Telefon umožňuje nakoupit, objednat, investovat nebo půjčit si během několika sekund.
            </div>
            """,
                unsafe_allow_html=True,
            )

        # 2.1.1 Co znamená osobní finanční management
        with st.container(border=True):
            st.markdown("### 2.1.1 Co znamená osobní finanční management")
            st.write(
                "Osobní finanční management je schopnost plánovat a řídit"
                " vlastní peníze tak, aby člověk zvládal běžné výdaje, nečekané"
                " situace i dlouhodobé cíle."
            )
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
            st.write(
                "**Potřeba** je výdaj, bez kterého se člověk dlouhodobě neobejde"
                " nebo který je nutný pro běžné fungování — například jídlo,"
                " bydlení, doprava do školy nebo práce, léky, základní oblečení."
            )
            st.write(
                "**Přání** je výdaj, který zvyšuje pohodlí, radost nebo"
                " status, ale není nezbytný — například nové značkové oblečení,"
                " dražší telefon, streamovací služby navíc, kosmetika, herní"
                " doplňky nebo časté objednávání jídla."
            )

            st.markdown("#### 🧩 Třídič: Je to potřeba, nebo přání?")

            p_q1 = st.selectbox(
                "1. Nájemné nebo poplatek za kolej / bydlení:",
                ["Vyber...", "Potřeba", "Přání"],
                key="k2_p_q1",
            )
            p_q2 = st.selectbox(
                "2. Třetí aktivní streamovací služba (Netflix/Spotify/Disney):",
                ["Vyber...", "Potřeba", "Přání"],
                key="k2_p_q2",
            )
            p_q3 = st.selectbox(
                "3. Základní jídlo a potraviny v e-shopu/supermarketu:",
                ["Vyber...", "Potřeba", "Přání"],
                key="k2_p_q3",
            )
            p_q4 = st.selectbox(
                "4. Každodenní objednávání hotového jídla přes rozvoz:",
                ["Vyber...", "Potřeba", "Přání"],
                key="k2_p_q4",
            )
            p_q5 = st.selectbox(
                "5. Předepsané léky nebo jízdné do školy:",
                ["Vyber...", "Potřeba", "Přání"],
                key="k2_p_q5",
            )

            if st.button("Vyhodnotit třídič 💾", key="k2_potreby_btn"):
                if (
                    p_q1 == "Potřeba"
                    and p_q2 == "Přání"
                    and p_q3 == "Potřeba"
                    and p_q4 == "Přání"
                    and p_q5 == "Potřeba"
                ):
                    st.success(
                        "🎉 Skvěle! Přesně rozumíš hranici mezi nezbytnou"
                        " potřebou a volitelným přáním."
                    )
                else:
                    st.error(
                        "Některé položky jsou zařazeny špatně. Potřeba je nutná"
                        " k přežití a fungování, přání zvyšuje komfort."
                    )

    # =========================================================================
    # 2.2 ROZPOČET: MAPA PENĚZ
    # =========================================================================
    elif "2.2 Rozpočet" in selected_section_2:
        st.markdown(
            "<div class='sub-section-header'>2. OSOBNÍ FINANCE A „ALGORITMY"
            " BOHATSTVÍ“</div><h2>2.2 Rozpočet: mapa peněz</h2>",
            unsafe_allow_html=True,
        )
        st.write(
            "Rozpočet ukazuje, odkud peníze přicházejí a kam odcházejí. Bez"
            " rozpočtu člověk často neví, jestli má problém s nízkými příjmy,"
            " vysokými výdaji, impulzivním utrácením, dluhy nebo chybějící"
            " rezervou."
        )

        with st.container(border=True):
            st.markdown(
                """
            <div class='box-blue'>
                🧭 <strong>Jednoduše řečeno:</strong> Rozpočet není trest ani omezování života. Je to mapa. Pomáhá zjistit, jestli peníze směřují k tomu, co je pro člověka opravdu důležité.
            </div>
            """,
                unsafe_allow_html=True,
            )

        # 2.2.1 Příjmy
        with st.container(border=True):
            st.markdown("### 2.2.1 Příjmy")
            st.write(
                "Příjmy jsou peníze, které člověk získává. Mohou být pravidelné"
                " nebo nepravidelné."
            )

            st.markdown(
                """
            | Typ příjmu | Příklad | Na co si dát pozor |
            | :--- | :--- | :--- |
            | **Pravidelný příjem** | mzda, brigáda, kapesné, stipendium | Lze s ním lépe plánovat. |
            | **Nepravidelný příjem** | jednorázová odměna, prodej věcí, sezónní brigáda | Není dobré na něm stavět pravidelné výdaje. |
            | **Pasivnější příjem** | úrok, dividenda, příjem z pronájmu | Většinou vyžaduje kapitál, čas nebo riziko. |
            """,
                unsafe_allow_html=True,
            )

        # 2.2.2 Výdaje
        with st.container(border=True):
            st.markdown("### 2.2.2 Výdaje")
            st.write(
                "Výdaje je vhodné rozdělit podle toho, jak snadno je lze"
                " změnit."
            )

            st.markdown(
                """
            | Typ výdaje | Příklad | Otázka ke kontrole |
            | :--- | :--- | :--- |
            | **Fixní výdaj** | nájem, paušál, předplatné, splátka | Opravdu ho potřebuji každý měsíc? |
            | **Proměnlivý výdaj** | jídlo, doprava, drogerie, zábava | Dá se upravit bez zásadního poklesu kvality života? |
            | **Jednorázový výdaj** | telefon, oprava, dovolená, školní pomůcky | Mám na něj připravené peníze dopředu? |
            | **Skrytý výdaj** | automatické předplatné, poplatky, mikrotransakce | Vím, kolik mě stojí za rok? |
            """,
                unsafe_allow_html=True,
            )

            if "vykresli_otazku_fn" in st.session_state:
                st.session_state["vykresli_otazku_fn"](
                    "2.5.1",
                    "🧩 Interaktivní výzva: Projdi si posledních 10 plateb v"
                    " mobilním bankovnictví. Rozděl je na potřeby, přání a"
                    " skryté nebo automatické výdaje.",
                    "2",
                    st.session_state.get("ulozene_odpovedi", {}),
                )

        # 2.2.3 Pravidlo 50-30-20
        with st.container(border=True):
            st.markdown(
                "### 2.2.3 Jednoduché pravidlo pro rozpočet (50–30–20)"
            )
            st.write("Jedním z možných rules je model **50–30–20**:")
            st.markdown("""
            * **50 %** na potřeby,
            * **30 %** na přání,
            * **20 %** na rezervu, spoření, investování nebo splácení dluhů.
            """)

            st.markdown(
                """
            <div class='box-gray'>
                ⚖️ <strong>Pozor na zjednodušení:</strong> Pravidlo 50–30–20 není povinnost a nemusí fungovat pro každého. Někdo má vysoké náklady na bydlení, někdo nízký příjem, někdo splácí dluh. Smyslem pravidla je ukázat princip: část peněz má pokrýt dnešek, část radost a část budoucnost.
            </div>
            """,
                unsafe_allow_html=True,
            )

            st.markdown("#### 🧮 Kalkulačka rozpočtu 50–30–20")
            b_income = st.number_input(
                "Zadej svůj měsíční čistý příjem (Kč):",
                value=20000,
                step=1000,
                key="k2_budget_calc_inc",
            )

            c_needs = b_income * 0.50
            c_wants = b_income * 0.30
            c_saves = b_income * 0.20

            col_b1, col_b2, col_b3 = st.columns(3)
            col_b1.metric(
                "Potřeby (50 %)", f"{c_needs:,.0f} Kč".replace(",", " ")
            )
            col_b2.metric(
                "Přání (30 %)", f"{c_wants:,.0f} Kč".replace(",", " ")
            )
            col_b3.metric(
                "Rezerva / Úspory (20 %)", f"{c_saves:,.0f} Kč".replace(",", " ")
            )

            if st.button("Uložit výpočet rozpočtu 💾", key="btn_k2_budget"):
                roz_data = (
                    f"Příjem: {b_income} Kč | Potřeby: {c_needs} Kč | Přání:"
                    f" {c_wants} Kč | Rezerva: {c_saves} Kč"
                )
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"](
                        "Kapitola 2",
                        "Podkapitola 2.2.3 - Kalkulačka rozpočtu",
                        roz_data,
                    )

    # =========================================================================
    # 2.3 ALGORITMY BOHATSTVÍ
    # =========================================================================
    elif "2.3 Algoritmy" in selected_section_2:
        st.markdown(
            "<div class='sub-section-header'>2. OSOBNÍ FINANCE A „ALGORITMY"
            " BOHATSTVÍ“</div><h2>2.3 Algoritmy bohatství: malé návyky, velký"
            " rozdíl</h2>",
            unsafe_allow_html=True,
        )
        st.write(
            "Slovo „algoritmus“ tu neznamená počítačový program. Znamená"
            " opakovatelný postup, který člověku pomáhá rozhodovat se lépe."
            " Bohatství nevzniká jen jedním velkým rozhodnutím. Často vzniká z"
            " malých pravidelných kroků, které se opakují dlouhou dobu."
        )

        with st.container(border=True):
            st.markdown(
                """
            <div class='box-blue'>
                🔁 <strong>Algoritmus finanční stability:</strong><br>
                1. Nejdřív zaplať nutné výdaje.<br>
                2. Hned po příjmu odlož část peněz stranou.<br>
                3. Utrať jen to, co zůstane po odložení rezervy.<br>
                4. Vyhýbej se drahému dluhu.<br>
                5. Pravidelně kontroluj, kam peníze mizí.
            </div>
            """,
                unsafe_allow_html=True,
            )

        with st.container(border=True):
            st.markdown("### 2.3.1 Zaplať nejdřív sobě")
            st.write(
                "Princip „zaplať nejdřív sobě“ znamená, že člověk nečeká,"
                " jestli mu na konci měsíce něco zbyde. Část peněz si odloží"
                " hned po přijetí příjmu."
            )
            st.write("Příklad:")
            st.markdown("""
            * přijde výplata nebo brigáda,
            * pokud používáš pravidlo 50–30–20, odložíš 20 %, případně začneš s menší částkou (třeba 10 % nebo pevná částka),
            * teprve zbytek je určený na běžné výdaje.
            """)
            st.write(
                "**Proč to funguje?** Když člověk čeká, co zbyde, často nezbyde"
                " nic. Digitální platby, drobné nákupy, jídlo venku, doprava,"
                " předplatná a impulzivní objednávky peníze postupně"
                " „rozpustí“. Automatické odložení peněz snižuje závislost na"
                " vůli."
            )

        with st.container(border=True):
            st.markdown(
                "### 2.3.2 Automatizace pomáhá, ale musí být pod kontrolou"
            )
            st.write(
                "Automatické platby mohou být užitečné: pomáhají platit včas,"
                " odkládat rezervu nebo pravidelně spořit. Zároveň ale mohou"
                " vytvářet výdaje, kterých si člověk nevšímá."
            )

            st.markdown(
                """
            <div class='box-purple'>
                🤖 <strong>AI mentoring:</strong> Zkopíruj tento prompt do AI asistenta:<br>
                <em>„Pomoz mi najít v mém měsíčním rozpočtu tři automatické výdaje, které bych měl/a zkontrolovat, a navrhni, jak poznám, jestli mi za to stojí.“</em>
            </div>
            """,
                unsafe_allow_html=True,
            )

    # =========================================================================
    # 2.4 MATEMATIKA PENĚZ
    # =========================================================================
    elif "2.4 Matematika" in selected_section_2:
        st.markdown(
            "<div class='sub-section-header'>2. OSOBNÍ FINANCE A „ALGORITMY"
            " BOHATSTVÍ“</div><h2>2.4 Matematika peněz: čas, úrok a"
            " inflace</h2>",
            unsafe_allow_html=True,
        )
        st.write(
            "Peníze mají časovou hodnotu. Stokoruna dnes nemá stejnou hodnotu"
            " jako stokoruna za deset let, protože ceny se mění a peníze mohou"
            " nést úrok nebo výnos."
        )

        # 2.4.1 Jednoduché úročení
        with st.container(border=True):
            st.markdown("### 2.4.1 Jednoduché úročení")
            st.write(
                "Jednoduché úročení znamená, že se úrok počítá stále jen z"
                " původně vložené nebo půjčené částky. Úroky se v dalších"
                " obdobích nepřičítají k základu pro další úročení."
            )

            st.markdown(
                """
            <div class='box-gray'>
                🧮 <strong>Vzorec pro jednoduché úročení:</strong><br>
                $$K = J \\times (1 + r \\times t)$$<br>
                • <strong>K</strong> = konečná částka<br>
                • <strong>J</strong> = jistina (původní vklad)<br>
                • <strong>r</strong> = roční úroková sazba v desetinném tvaru (např. 5 % = 0,05)<br>
                • <strong>t</strong> = čas v letech
            </div>
            """,
                unsafe_allow_html=True,
            )

            st.write(
                "**Příklad jednoduchého úročení:** Vložíš 10 000 Kč na 3 roky"
                " s roční úrokovou sazbou 5 %. Úrok se počítá pořád jen z"
                " původních 10 000 Kč."
            )
            st.write(
                "Výpočet: $K = 10\\ 000 \\times (1 + 0{,}05 \\times 3) = 10\\"
                " 000 \\times 1{,}15 = 11\\ 500\\ \\text{Kč}$. Za 3 roky získáš"
                " úrok 1 500 Kč."
            )

        # 2.4.2 Složené úročení
        with st.container(border=True):
            st.markdown("### 2.4.2 Složené úročení")
            st.write(
                "Složené úročení znamená, že se úročí nejen původní částka, ale"
                " postupně i již připsané úroky nebo výnosy. Peníze tedy mohou"
                " vydělávat další peníze."
            )

            st.markdown(
                """
            <div class='box-gray'>
                🧮 <strong>Vzorec pro složené úročení:</strong><br>
                $$K = J \\times (1 + r)^n$$<br>
                • <strong>K</strong> = konečná částka<br>
                • <strong>J</strong> = jistina<br>
                • <strong>r</strong> = úroková sazba za období v desetinném tvaru<br>
                • <strong>n</strong> = počet úročených období
            </div>
            """,
                unsafe_allow_html=True,
            )

            st.write(
                "**Příklad složeného úročení:** Vložíš 10 000 Kč na 3 roky s"
                " roční úrokovou sazbou 5 %. Úrok se každý rok připíše k"
                " částce a další rok se úročí i tento připsaný úrok."
            )
            st.write(
                "Výpočet: $K = 10\\ 000 \\times (1 + 0{,}05)^3 = 10\\ 000 \\times"
                " 1{,}157625 = 11\\ 576{,}25\\ \\text{Kč}$. Za 3 roky získáš"
                " úrok 1 576,25 Kč."
            )

            st.markdown(
                """
            | Typ úročení | Z čeho se počítá úrok | Výsledek při 10 000 Kč, 5 % p.a., 3 roky |
            | :--- | :--- | :--- |
            | **Jednoduché úročení** | Pořád z původní částky | **11 500,00 Kč** |
            | **Složené úročení** | Z původní částky i z připsaných úroků | **11 576,25 Kč** |
            """,
                unsafe_allow_html=True,
            )

            st.markdown(
                "#### 🧮 Srovnávací kalkulačka: Jednoduché vs. Složené úročení"
            )
            col_u1, col_u2, col_u3 = st.columns(3)
            with col_u1:
                jistina_input = st.number_input(
                    "Vklad J (Kč):", value=10000, step=1000, key="k2_u_jistina"
                )
            with col_u2:
                sazba_input = st.number_input(
                    "Sazba r (% p.a.):",
                    value=5.0,
                    step=0.5,
                    key="k2_u_sazba",
                )
            with col_u3:
                roky_input = st.number_input(
                    "Čas t (roky):", value=3, step=1, key="k2_u_roky"
                )

            r_dec = sazba_input / 100.0
            res_jednoduse = jistina_input * (1 + r_dec * roky_input)
            res_slozene = jistina_input * ((1 + r_dec) ** roky_input)
            diff_urok = res_slozene - res_jednoduse

            c_u_res1, c_u_res2, c_u_res3 = st.columns(3)
            c_u_res1.metric(
                "Jednoduché úročení",
                f"{res_jednoduse:,.2f} Kč".replace(",", " "),
            )
            c_u_res2.metric(
                "Složené úročení", f"{res_slozene:,.2f} Kč".replace(",", " ")
            )
            c_u_res3.metric(
                "Rozdíl ve prospěch složeného",
                f"+{diff_urok:,.2f} Kč".replace(",", " "),
            )

            if st.button("Uložit výpočet úročení 💾", key="btn_k2_uroceni"):
                ur_data = (
                    f"Vklad: {jistina_input} Kč | Sazba: {sazba_input}% | Čas:"
                    f" {roky_input} let | Jednoduché: {res_jednoduse:.2f} Kč |"
                    f" Složené: {res_slozene:.2f} Kč | Rozdíl:"
                    f" {diff_urok:.2f} Kč"
                )
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"](
                        "Kapitola 2",
                        "Podkapitola 2.4.2 - Úročení kalkulačka",
                        ur_data,
                    )

            with st.expander(
                "✍️ Procvičování: Spočítej úročení (3 příklady)"
            ):
                st.write(
                    "**1. Jednoduché úročení:** Vložíš 8 000 Kč na 2 roky při"
                    " sazbě 4 % p.a."
                )
                ex1_ans = st.number_input(
                    "Zadej vypočtenou konečnou částku (Kč):",
                    value=0,
                    key="k2_ex1_val",
                )
                if st.button("Zkontrolovat příklad 1", key="k2_ex1_btn"):
                    if abs(ex1_ans - 8640) < 1:
                        st.success(
                            "✅ Správně! K = 8 000 × (1 + 0,04 × 2) = 8 640 Kč."
                            " Úrok je 640 Kč."
                        )
                    else:
                        st.error(
                            "Chyba. Výpočet: 8000 * (1 + 0.04 * 2) = 8 640 Kč."
                        )

                st.write(
                    "**2. Složené úročení:** Vložíš 8 000 Kč na 2 roky při"
                    " sazbě 4 % p.a. (roční připisování)."
                )
                ex2_ans = st.number_input(
                    "Zadej vypočtenou konečnou částku (Kč):",
                    value=0.0,
                    step=0.1,
                    key="k2_ex2_val",
                )
                if st.button("Zkontrolovat příklad 2", key="k2_ex2_btn"):
                    if abs(ex2_ans - 8652.80) < 1:
                        st.success(
                            "✅ Správně! K = 8 000 × (1 + 0,04)² = 8 652,80"
                            " Kč. Rozdíl je 12,80 Kč."
                        )
                    else:
                        st.error(
                            "Chyba. Výpočet: 8000 * (1.04)^2 = 8 652,80 Kč."
                        )

                st.write(
                    "**3. Porovnání delšího období (5 let, 15 000 Kč, 6 %"
                    " p.a.):**"
                )
                st.write(
                    "• Jednoduché: $15\\ 000 \\times (1 + 0{,}06 \\times 5) ="
                    " 19\\ 500\\ \\text{Kč}$"
                )
                st.write(
                    "• Složené: $15\\ 000 \\times (1 + 0{,}06)^5 = 20\\ 073{,}38\\"
                    " \\text{Kč}$"
                )
                st.info(
                    "💡 Rozdíl je **573,38 Kč** ve prospěch složeného úročení."
                    " Čím delší doba, tím více se projevuje efekt úroků z"
                    " úroků."
                )

        # 2.4.3 Inflace
        with st.container(border=True):
            st.markdown("### 2.4.3 Inflace")
            st.write(
                "Inflace znamená růst cenové hladiny. Když ceny rostou, za"
                " stejnou částku si koupíme méně než dříve."
            )
            st.write(
                "Oficiální inflace je průměr za celou ekonomiku. Každý človek"
                " ale může mít jinou **„osobní inflaci“**. Student, rodina s"
                " dětmi, senior nebo človek dojíždějící autem vnímají"
                " zdražování jinak, protože utrácejí za jiné věci."
            )

            if "vykresli_otazku_fn" in st.session_state:
                st.session_state["vykresli_otazku_fn"](
                    "2.6.1",
                    "🧩 Interaktivní výzva: Vyber pět věcí, které pravidelně"
                    " kupuješ. Zjisti nebo odhadni, kolik stály dříve a kolik"
                    " stojí dnes. Která položka zdražila nejvíc?",
                    "2",
                    st.session_state.get("ulozene_odpovedi", {}),
                )

    # =========================================================================
    # 2.5 FINANČNÍ REZERVA
    # =========================================================================
    elif "2.5 Finanční rezerva" in selected_section_2:
        st.markdown(
            "<div class='sub-section-header'>2. OSOBNÍ FINANCE A „ALGORITMY"
            " BOHATSTVÍ“</div><h2>2.5 Finanční rezerva: airbag osobních"
            " financí</h2>",
            unsafe_allow_html=True,
        )
        st.write(
            "Finanční rezerva chrání člověka před tím, aby každá nečekaná"
            " situace skončila dluhem. Může jít o rozbitý telefon, ztrátu"
            " brigády, nemoc, opravu auta, vyšší vyúčtování energií nebo"
            " stěhování."
        )

        with st.container(border=True):
            st.markdown(
                """
            <div class='box-blue'>
                🛟 <strong>Jednoduše řečeno:</strong> Rezerva je finanční airbag. Doufáš, že ji nebudeš potřebovat, ale když přijde náraz, může zabránit větším škodám.
            </div>
            """,
                unsafe_allow_html=True,
            )

        with st.container(border=True):
            st.markdown("### 2.5.1 Jak velká má být rezerva")
            st.write(
                "Obecné doporučení bývá mít rezervu alespoň ve výši 3 až 6"
                " měsíců nutných výdajů. U studenta může být začátek menší:"
                " třeba první cíl 1 000 Kč, potom 5 000 Kč, potom jeden měsíc"
                " výdajů."
            )

            st.markdown(
                """
            | Životní situace | První rozumný cíl | Silnější rezerva |
            | :--- | :--- | :--- |
            | **Student s podporou rodiny** | 1 000–5 000 Kč | 1 měsíc vlastních výdajů |
            | **Člověk na brigádě nebo v první práci** | 1 měsíc nutných výdajů | 3 měsíce nutných výdajů |
            | **Samostatně žijící človek** | 3 měsíce nutných výdajů | 6 měsíců nutných výdajů |
            | **Rodina nebo podnikatel** | 3–6 měsíců nutných výdajů | více podle rizika příjmů |
            """,
                unsafe_allow_html=True,
            )

            st.markdown("#### 🧮 Kalkulačka cílové finanční rezervy")
            user_sit = st.selectbox(
                "Zvol svou aktuální životní situaci:",
                [
                    "Student s podporou rodiny",
                    "Člověk na brigádě / v první práci",
                    "Samostatně žijící človek",
                    "Rodina nebo podnikatel",
                ],
                key="k2_res_sit",
            )

            m_exp = st.number_input(
                "Zadej své měsíční nutné výdaje (Kč):",
                value=8000,
                step=1000,
                key="k2_res_m_exp",
            )

            if "Student" in user_sit:
                r_min, r_target = 3000, m_exp * 1
            elif "brigádě" in user_sit:
                r_min, r_target = m_exp * 1, m_exp * 3
            elif "Samostatně" in user_sit:
                r_min, r_target = m_exp * 3, m_exp * 6
            else:
                r_min, r_target = m_exp * 6, m_exp * 9

            col_res1, col_res2 = st.columns(2)
            col_res1.metric(
                "Minimální základní rezerva",
                f"{r_min:,.0f} Kč".replace(",", " "),
            )
            col_res2.metric(
                "Doporučená optimální rezerva",
                f"{r_target:,.0f} Kč".replace(",", " "),
            )

            if st.button("Uložit výpočet finanční rezervy 💾", key="btn_k2_rezerva"):
                rez_data = (
                    f"Situace: {user_sit} | Měsíční výdaje: {m_exp} Kč | Min."
                    f" rezerva: {r_min} Kč | Opt. rezerva: {r_target} Kč"
                )
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"](
                        "Kapitola 2",
                        "Podkapitola 2.5.1 - Kalkulačka rezervy",
                        rez_data,
                    )

        with st.container(border=True):
            st.markdown("### 2.5.2 Kde rezervu držet")
            st.write(
                "Rezerva má být bezpečná a dostupná. Není určena k riskantnímu"
                " investování. Vhodné vlastnosti:"
            )
            st.markdown("""
            * rychlá dostupnost,
            * nízké riziko ztráty,
            * oddělení od běžného účtu,
            * možnost použít ji při nečekané situaci.
            """)

            st.markdown(
                """
            <div class='box-red'>
                🚫 <strong>Častá chyba:</strong> Investovat nouzovou rezervu do rizikových aktiv. Když pak přijde problém, může být človek nucen prodat v nevýhodnou chvíli se ztrátou.
            </div>
            """,
                unsafe_allow_html=True,
            )
# =========================================================================
    # 2.6 PSYCHOLOGIE UTRÁCENÍ
    # =========================================================================
    elif "2.6 Psychologie" in selected_section_2:
        st.markdown(
            "<div class='sub-section-header'>2. OSOBNÍ FINANCE A „ALGORITMY"
            " BOHATSTVÍ“</div><h2>2.6 Psychologie utrácení: proč nerozhodujeme"
            " vždy racionálně</h2>",
            unsafe_allow_html=True,
        )
        st.write(
            "Lidé nejsou kalkulačky. Často se rozhodujeme podle emocí, únavy,"
            " tlaku okolí, reklamy, strachu, že něco propásneme, nebo podle"
            " toho, co nám ukáže aplikace."
        )

        with st.container(border=True):
            st.markdown("### 2.6.1 Nejčastější pasti")
            st.markdown(
                """
            | Past | Jak funguje | Obrana |
            | :--- | :--- | :--- |
            | **FOMO** | Strach, že mi něco uteče. | Počkej 24 hodin před nákupem. |
            | **Sleva** | Pocit úspory, i když kupuji zbytečnost. | Ptej se: koupil/a bych to i bez slevy? |
            | **Sociální srovnávání** | Chci životní styl, který vidím u ostatních. | Rozliš realitu a vybraný obsah na sítích. |
            | **Mikrotransakce** | Malé částky vypadají neškodně. | Spočítej roční součet. |
            | **Odložená platba (BNPL)** | Nákup nebolí hned. | Ber ji jako dluh, ne jako slevu. |
            """,
                unsafe_allow_html=True,
            )

        with st.container(border=True):
            st.markdown("### 2.6.2 Algoritmy a personalizovaná reklama")
            st.write(
                "E-shopy, sociální sítě a aplikace sbírají data o tom, co"
                " sledujeme, hledáme, lajkujeme a kupujeme. Díky tomu nám mohou"
                " ukazovat nabídky, které přesně míří na naše zájmy, slabiny"
                " nebo aktuální náladu."
            )

            st.markdown(
                """
            <div class='box-purple'>
                📱 <strong>Moderní realita:</strong> Dříve človek viděl stejnou reklamu jako ostatní v televizi nebo časopise. Dnes může každý vidět jinou reklamu podle toho, co o něm platforma ví. Proto je finanční gramotnost propojená s digitální gramotností.
            </div>
            """,
                unsafe_allow_html=True,
            )

            st.write("**Jak poznat, že mě prostředí tlačí k nákupu?**")
            st.markdown("""
            * Vidím odpočet času nebo nápis „zbývají poslední kusy“.
            * Aplikace mi nabízí dopravu zdarma až od určité částky.
            * Po jednom vyhledávání mě produkt pronásleduje v reklamách.
            * Influencer ukazuje produkt jako součást úspěšného životního stylu.
            * Platba je tak jednoduchá, že skoro nevnímám, že utrácím.
            """)

            if "vykresli_otazku_fn" in st.session_state:
                st.session_state["vykresli_otazku_fn"](
                    "2.6.2",
                    "🧩 Interaktivní výzva: Najdi jednu reklamu nebo nabídku,"
                    " která tě nedávno zaujala. Popiš, jakou emoci používá:"
                    " strach, radost, tlak na výkon, pocit výhodné koupě,"
                    " krásu, úspěch, pohodlí nebo srovnávání s ostatními.",
                    "2",
                    st.session_state.get("ulozene_odpovedi", {}),
                )

    # =========================================================================
    # 2.7 KALKULAČKA ČASU NÁKUPU
    # =========================================================================
    elif "2.7 Kalkulačka" in selected_section_2:
        st.markdown(
            "<div class='sub-section-header'>2. OSOBNÍ FINANCE A „ALGORITMY"
            " BOHATSTVÍ“</div><h2>2.7 Kalkulačka času: kolik života stojí"
            " nákup</h2>",
            unsafe_allow_html=True,
        )
        st.write(
            "Cena věci není jen částka v korunách. Dá se přepočítat i na čas,"
            " který musí človek pracovat, aby si ji mohl dovolit."
        )

        with st.container(border=True):
            st.markdown(
                """
            <div class='box-gray'>
                ⏱️ <strong>Vzorec pro výpočet časové ceny:</strong><br>
                $$\\text{Čas práce (hodiny)} = \\frac{\\text{Cena věci (Kč)}}{\\text{Čistá hodinová mzda (Kč/h)}}$$
            </div>
            """,
                unsafe_allow_html=True,
            )

            st.write(
                "**Příklad:** Sluchátka stojí 2 400 Kč. Čistá hodinová mzda z"
                " brigády je 150 Kč. $2\\ 400 \\div 150 = 16\\ \\text{hodin"
                " práce}$."
            )

            st.markdown("#### ⏳ Interaktivní kalkulačka času nákupu")
            col_t1, col_t2 = st.columns(2)
            with col_t1:
                price_item = st.number_input(
                    "Cena plánovaného nákupu (Kč):",
                    value=2400,
                    step=100,
                    key="k2_time_price",
                )
            with col_t2:
                wage_hourly = st.number_input(
                    "Tvoje čistá hodinová mzda / odměna (Kč/hod):",
                    value=150,
                    step=10,
                    key="k2_time_wage",
                )

            if wage_hourly > 0:
                hours_needed = price_item / wage_hourly
                st.metric(
                    "Počet hodin práce nutný na tento nákup",
                    f"{hours_needed:.1f} hodin",
                )
                st.info(
                    f"👉 Aby sis mohl/a koupit tuto věc za **{price_item} Kč**,"
                    f" musíš strávit v práci **{hours_needed:.1f} hodin**. Stojí"
                    " ti to za ten čas?"
                )

                if st.button("Uložit výpočet času nákupu 💾", key="btn_k2_time_calc"):
                    time_data = (
                        f"Cena věci: {price_item} Kč | Hodinová mzda:"
                        f" {wage_hourly} Kč/h | Potřebný čas:"
                        f" {hours_needed:.1f} h"
                    )
                    if "uloz_odpoved_fn" in st.session_state:
                        st.session_state["uloz_odpoved_fn"](
                            "Kapitola 2",
                            "Podkapitola 2.7 - Kalkulačka času",
                            time_data,
                        )

    # =========================================================================
    # 2.8 OSOBNÍ FINANČNÍ AUDIT
    # =========================================================================
    elif "2.8 Osobní" in selected_section_2:
        st.markdown(
            "<div class='sub-section-header'>2. OSOBNÍ FINANCE A „ALGORITMY"
            " BOHATSTVÍ“</div><h2>2.8 Praktický výstup: můj osobní finanční"
            " audit</h2>",
            unsafe_allow_html=True,
        )
        st.write(
            "Na konci této části by měl být človek schopný udělat jednoduchý"
            " audit vlastních financí."
        )

        with st.container(border=True):
            st.markdown("#### ✅ Kontrolní checklist osobního auditu")
            st.write("Zaškrtni body, které už bezpečně ovládáš a uplatňuješ:")

            st.checkbox(
                "1. Vím, jaké mám pravidelné příjmy.", key="k2_audit_chk1"
            )
            st.checkbox(
                "2. Vím, kam mi odcházejí peníze.", key="k2_audit_chk2"
            )
            st.checkbox(
                "3. Znám své automatické platby a předplatná.",
                key="k2_audit_chk3",
            )
            st.checkbox(
                "4. Mám plán, jak tvořit rezervu.", key="k2_audit_chk4"
            )
            st.checkbox(
                "5. Umím rozlišit potřebu, přání a impulzivní nákup.",
                key="k2_audit_chk5",
            )
            st.checkbox(
                "6. Chápu, že inflace snižuje kupní sílu peněz.",
                key="k2_audit_chk6",
            )
            st.checkbox(
                "7. Umím přepočítat cenu věci na hodiny práce.",
                key="k2_audit_chk7",
            )
            st.checkbox(
                "8. Vím, že digitální prostředí ovlivňuje moje finanční"
                " rozhodování.",
                key="k2_audit_chk8",
            )

            if st.button("Uložit výsledek auditu 💾", key="btn_k2_audit"):
                splneno = []
                if st.session_state.get("k2_audit_chk1"):
                    splneno.append("Příjmy")
                if st.session_state.get("k2_audit_chk2"):
                    splneno.append("Výdaje")
                if st.session_state.get("k2_audit_chk3"):
                    splneno.append("Předplatná")
                if st.session_state.get("k2_audit_chk4"):
                    splneno.append("Rezerva")
                if st.session_state.get("k2_audit_chk5"):
                    splneno.append("Potřeby a přání")
                if st.session_state.get("k2_audit_chk6"):
                    splneno.append("Inflace")
                if st.session_state.get("k2_audit_chk7"):
                    splneno.append("Časová cena nákupu")
                if st.session_state.get("k2_audit_chk8"):
                    splneno.append("Digitální vlivy")

                audit_res = f"Splněné body ({len(splneno)}/8): " + ", ".join(
                    splneno
                )
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"](
                        "Kapitola 2",
                        "Podkapitola 2.8 - Finanční audit",
                        audit_res,
                    )

            st.markdown(
                """
            <div class='box-purple'>
                🤖 <strong>AI mentoring:</strong> Zkopíruj tento prompt do AI asistenta:<br>
                <em>„Pomoz mi udělat osobní finanční audit. Zeptej se mě postupně na příjmy, pravidelné výdaje, předplatná, rezervu, dluhy a finanční cíle. Na konci mi navrhni tři malé změny na příští měsíc.“</em>
            </div>
            """,
                unsafe_allow_html=True,
            )

    # =========================================================================
    # 3. FINANČNÍ TRH A ANALÝZA RIZIK
    # =========================================================================
    # =========================================================================
    # 3.1 CO JE TO FINANČNÍ TRH A BURZA
    # =========================================================================
    elif "3.1 Co je" in selected_section_2:
        st.markdown(
            "<div class='sub-section-header'>3. FINANČNÍ TRH A ANALÝZA"
            " RIZIK</div><h2>3.1 Co je to finanční trh</h2>",
            unsafe_allow_html=True,
        )

        st.write(
            "Finanční trh umožňuje, aby se peníze přesouvaly od těch, kteří je"
            " mají k dispozici, k těm, kteří je chtějí využít. Může jít o"
            " domácnosti, firmy, banky, investory, stát, obce, fondy nebo"
            " mezinárodní instituce."
        )

        st.write("**Představ si to jednoduše:**")
        st.markdown("""
        * člověk má úspory a nechce, aby mu jen ležely na účtu,
        * firma potřebuje peníze na rozšíření výroby,
        * stát si půjčuje na financování svých výdajů,
        * investor hledá příležitost, kde by peníze mohly pracovat,
        * banka, burza nebo investiční platforma pomáhá tyto strany propojit.
        """)

        st.info(
            "🧠 **Finanční trh není kasino** — ale může se tak chovat, pokud"
            " člověk neví, co dělá. Rozdíl mezi odpovědným investováním a"
            " hazardem není jen v produktu, ale hlavně v informovanosti,"
            " riziku, časovém horizontu a chování člověka."
        )

        # 3.1.1
        with st.container(border=True):
            st.markdown("### 3.1.1 Hlavní funkce finančního trhu")
            st.write("Finanční trh má několik důležitých funkcí:")
            st.markdown(
                """
            | Funkce | Co znamená | Příklad |
            | :--- | :--- | :--- |
            | **Přesun kapitálu** | Volné peníze se dostávají k těm, kdo je potřebují. | Investor koupí dluhopis firmy, firma získá peníze na rozvoj. |
            | **Zhodnocení úspor** | Lidé a firmy hledají možnost, jak peníze ochránit před inflací nebo je rozmnožit. | Domácnost investuje pravidelně do fondu. |
            | **Stanovení ceny peněz a aktiv** | Trh ukazuje, za kolik se obchodují akcie, dluhopisy, měny nebo komodity. | Cena akcie se mění podle nabídky a poptávky. |
            | **Rozložení rizika** | Riziko lze rozdělit mezi více investorů nebo produktů. | Fond drží stovky akcií místo jedné. |
            | **Likvidita** | Některá aktiva lze rychleji prodat a proměnit zpět na peníze. | Akcii velké firmy lze často prodat rychleji než nemovitost. |
            """,
                unsafe_allow_html=True,
            )

        # 3.1.2
        with st.container(border=True):
            st.markdown("### 3.1.2 Primární a sekundární trh")
            st.write("Finanční trh se často dělí na primární a sekundární.")
            st.markdown(
                """
            | Typ trhu | Co se děje | Příklad |
            | :--- | :--- | :--- |
            | **Primární trh** | Cenný papír se prodává poprvé. Peníze získává emitent — tedy ten, kdo cenný papír vydává. | Firma vydá nové akcie nebo stát vydá nový dluhopis. |
            | **Sekundární trh** | Investoři obchodují mezi sebou už dříve vydané cenné papíry. | Investor prodá akcii jiné osobě přes burzu. |
            """,
                unsafe_allow_html=True,
            )
            st.write("**Příklad ze života**")
            st.write(
                "Když si koupíš nově vydaný státní dluhopis přímo při emisi, jde"
                " o primární trh. Když později koupíš akcii od jiného investora"
                " přes burzu, firma už peníze z této konkrétní koupě"
                " nedostává — jde o sekundární trh."
            )

        # 3.1.3
        with st.container(border=True):
            st.markdown("### 3.1.3 Burza, broker a investiční platforma")
            st.write(
                "**Burza** je organizovaný trh, kde se obchoduje podle"
                " pravidel. Neznamená to nutně hlučný sál s lidmi v oblecích."
                " Dnes velká část obchodování probíhá elektronicky."
            )
            st.write(
                "**Broker** je zprostředkovatel, přes kterého může investor"
                " nakupovat a prodávat investiční nástroje."
            )
            st.write(
                "**Investiční aplikace** je uživatelské rozhraní, které může"
                " působit jednoduše jako e-shop. Právě proto je nutné"
                " zpomalit: to, že investici koupíš jedním klikem, neznamená, že"
                " jí rozumíš."
            )
            st.warning(
                "📱 **Moderní riziko:** Investiční aplikace umí vytvořit pocit"
                " hry. Grafy, notifikace, zelená čísla a rychlé nákupy mohou"
                " člověka tlačit k impulzivnímu obchodování. Finanční"
                " gramotnost dnes znamená umět poznat, kdy aplikace pomáhá — a"
                " kdy manipuluje chováním."
            )

        # 3.1.4
        with st.container(border=True):
            st.markdown(
                "### 3.1.4 Burza: organizované tržiště pro cenné papíry"
            )
            st.write(
                "Burza je organizovaný a regulovaný trh, kde se podle jasných"
                " pravidel obchoduje s investičními nástroji — nejčastěji s"
                " akciemi, dluhopisy, ETF, deriváty nebo komoditními nástroji."
                " Burzu si mnoho lidí představuje jako hlučný sál plný"
                " makléřů, kteří křičí a mávají papíry. Tak to historicky"
                " opravdu někde vypadalo. Dnes je ale většina obchodování"
                " elektronická: objednávky se zadávají přes obchodní systémy,"
                " párují se automaticky a vypořádávají se přes specializované"
                " instituce."
            )
            st.info(
                "🏛️ **Burza jednoduše:** Burza je jako přísně hlídané"
                " digitální tržiště. Neprodává se tam ovoce nebo oblečení, ale"
                " cenné papíry a další finanční nástroje. Aby obchodování"
                " fungovalo, musí mít pravidla, dohled, evidenci a systém, který"
                " určuje, kdo co koupil, za kolik a kdy se obchod vypořádá."
            )
            st.write("**Burza plní několik důležitých funkcí:**")
            st.markdown("""
            * umožňuje obchodování — investoři mohou nakupovat a prodávat cenné papíry,
            * pomáhá tvořit cenu — cena vzniká střetem nabídky a poptávky,
            * zvyšuje likviditu — investor má větší šance najít kupce nebo prodávajícího,
            * zvyšuje transparentnost — u regulovaných trhů jsou pravidla, zveřejňování informací a dohled,
            * umožňuje firmám získat kapitál — například při vstupu na burzu nebo vydání dluhopisů,
            * poskytuje signál o důvěře trhu — vývoj cen může ukazovat očekávání investorů.
            """)

        # 3.1.5
        with st.container(border=True):
            st.markdown("### 3.1.5 Jak burza funguje krok za krokem")
            st.write(
                "Když investor koupí akcii přes aplikaci, na obrazovce to"
                " vypadá jako jednoduché kliknutí. Ve skutečnosti za tím stojí"
                " celý řetězec institucí a pravidel."
            )
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
            st.write(
                "Cena na burze nevzniká tak, že ji někdo „od stolu“ vyhlásí jako"
                " cenu rohlíku v obchodě. Vzniká tím, že se potkávají kupující"
                " a prodávající. Pokud chce hodně lidí akcii koupit a málo lidí"
                " ji prodává, cena může růst. Pokud mnoho investorů prodává a"
                " málo kupuje, cena může klesat."
            )
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
            st.write(
                "Běžný občan většinou neobchoduje přímo na burze jako člen"
                " burzy. Obchoduje přes zprostředkovatele — například banku,"
                " obchodníka s cennými papíry nebo brokera. Tito zprostředkovatelé"
                " mají technický a právní přístup na trh nebo využívají"
                " další napojené instituce."
            )
            st.info(
                "🚪 **Důležité rozlišení:** Občan může investovat do cenných"
                " papírů obchodovaných na burze, ale obvykle nevstupuje přímo do"
                " burzovního systému. Používá brokera, podobně jako cestující"
                " používá dopravce, neřídí celé nádraží."
            )
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
            st.markdown(
                "### 3.1.7 Kdo burzu spravuje a kdo na ni dohlíží"
            )
            st.write(
                "Burza není chaotická skupina investorů. Má provozovatele,"
                " pravidla, členy, dohled a technickou infrastrukturu."
            )
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
            st.write(
                "V České republice hraje významnou roli Česká národní banka,"
                " která vykonává dohled nad finančním trhem. To neznamená, že"
                " ČNB určuje, za kolik má stát konkrétní akcie. Znamená to, že"
                " dohlíží na pravidla, instituce, ochranu trhu a férové"
                " fungování finančního systému."
            )

        # 3.1.8
        with st.container(border=True):
            st.markdown("### 3.1.8 Burza cenných papírů Praha")
            st.write(
                "Burza cenných papírů Praha, zkráceně BCPP, je hlavní"
                " regulovaný akciový trh v České republice. Obchodují se zde"
                " například akcie významných českých nebo ve střední Evropě"
                " působících společností, dluhopisy a další investiční"
                " nástroje."
            )
            st.info(
                "🇨🇿 **BCPP jednoduše:** Pražská burza je hlavní české"
                " organizované místo pro obchodování s cennými papíry. Pro české"
                " studenty je důležitá proto, že ukazuje, že kapitálový trh"
                " není jen Wall Street, ale existuje i v českém prostředí."
            )
            st.write(
                "**Na pražské burze se lze setkat například s těmito pojmy:**"
            )
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
            st.write(
                "Pro investory burza znamená možnost koupit nebo prodat cenné"
                " papíry za tržní cenu. Zároveň ale platí, že i akcie známé"
                " firmy může klesnout. Známé jméno firmy není záruka výnosu."
            )

        # 3.1.9
        with st.container(border=True):
            st.markdown(
                "### 3.1.9 RM-SYSTÉM: český trh dostupný i občanům"
            )
            st.write(
                "V českém prostředí existuje také RM-SYSTÉM, česká burza"
                " cenných papírů. Historicky navazuje na období kupónové"
                " privatizace a dlouhou dobu byl spojován s možností obchodování"
                " pro širší veřejnost. Dnes už nepůsobí tak moderně nebo"
                " mediálně výrazně jako velké investiční aplikace, ale stále"
                " jde o existující organizovaný trh, na kterém lze obchodovat"
                " vybrané cenné papíry."
            )
            st.info(
                "🇨🇿 **Proč RM-SYSTÉM zmínit:** Ukazuje, že český kapitálový"
                " trh nemá jen pražskou burzu. RM-SYSTÉM je důležitý i"
                " historicky, protože byl spojen s přístupem drobných investorů"
                " k obchodování s českými akciemi."
            )
            st.write("**Jak RM-SYSTÉM funguje zjednodušeně:**")
            st.markdown("""
            * je to český trh pro obchodování s vybranými cennými papíry,
            * investor může obchodovat prostřednictvím oprávněného obchodníka nebo napojené služby,
            * obchoduje se elektronicky,
            * nabídka instrumentů je omezenější než na největších světových burzách,
            * pro běžného občana může být srozumitelnější tím, že je zaměřen na české prostředí,
            * i zde platí rizika investování, poplatky, kolísání cen a nutnost rozumět tomu, co člověk kupuje.
            """)
            st.warning(
                "⚠️ **Pozor:** To, že je trh dostupný občanům, neznamená, že je"
                " bez rizika. Přístupnost není totéž co bezpečnost. I na"
                " českém trhu může investor prodělat, pokud kupuje bez"
                " znalostí, podle emocí nebo bez diverzifikace."
            )

        # 3.1.10
        with st.container(border=True):
            st.markdown("### 3.1.10 Nejznámější světové burzy")
            st.write(
                "Světové burzy propojují firmy a investory v globálním"
                " měřítku. Některé jsou známé hlavně akciemi technologických"
                " firem, jiné širokým spektrem společností, jiné komoditami"
                " nebo deriváty."
            )
            st.markdown(
                """
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
            """,
                unsafe_allow_html=True,
            )
            st.write("**Proč se burzy liší?**")
            st.write(
                "Burzy se liší velikostí, pravidly, typem obchodovaných firem,"
                " měnou, časovým pásmem, poplatky, likviditou a regulací. Pro"
                " investora je důležité vědět, že nákup americké akcie přes"
                " českou aplikaci znamená také měnové riziko, jiné obchodní"
                " hodiny a odlišné daňové nebo informační prostředí."
            )

        # 3.1.11
        with st.container(border=True):
            st.markdown("### 3.1.11 Burzovní indexy: teploměr trhu")
            st.write(
                "Když média říkají, že „americký trh roste“ nebo „pražská burza"
                " klesla“, často tím nemyslí každou jednu akcii. Mluví o"
                " burzovním indexu. Index sleduje vybranou skupinu akcií a"
                " ukazuje jejich souhrnný vývoj."
            )
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
            st.info(
                "🌡️ **Index jako teploměr:** Index neříká, že všechny firmy"
                " rostou nebo klesají stejně. Ukazuje průměrný nebo vážený vývoj"
                " vybrané skupiny firem. Je to orientační měřítko nálady a"
                " vývoje trhu."
            )

        # 3.1.12
        with st.container(border=True):
            st.markdown("### 3.1.12 Kdo na burze obchoduje")
            st.write("Na burze se potkávají různé typy účastníků:")
            st.markdown(
                """
            | Účastník | Co dělá | Příklad motivace |
            | :--- | :--- | :--- |
            | **Drobný investor** | Nakupuje menší objemy přes brokera nebo banku. | Dlouhodobé investování, dividenda, růst hodnoty. |
            | **Trader** | Obchoduje aktivněji a snaží se využít pohyb cen. | Krátkodobý zisk, vyšší riziko. |
            | **Investiční fond** | Spravuje peníze mnoha investorů. | Diverzifikované portfolio podle strategie. |
            | **Penzijní fond** | Spravuje peníze na dlouhodobé zabezpečení klientů. | Dlouhý horizont a řízení rizika. |
            | **Banka** | Obchoduje pro klienty nebo v rámci vlastního řízení rizik. | Likvidita, zajištění, investiční služby. |
            | **Firma / emitent** | Vydává akcie nebo dluhopisy, komunikuje s investory. | Získání kapitálu, důvěryhodnost, růst. |
            | **Market maker** | Pomáhá zajišťovat likviditu tím, že nabízí nákupní i prodejní ceny. | Vydělává na rozdílu cen a službě trhu. |
            """,
                unsafe_allow_html=True,
            )

        # 3.1.13
        with st.container(border=True):
            st.markdown(
                "### 3.1.13 Proč burza není totéž co kasino"
            )
            st.write(
                "Na burze může člověk spekulovat a chovat se podobně jako"
                " hazardní hráč. Burza sama o sobě ale není kasino. Rozdíl je v"
                " tom, že cenné papíry často představují reálná práva: podíl ve"
                " firmě, pohledávku za emitentem nebo podíl ve fondu. Problém"
                " nastává, když člověk nakupuje bez porozumění, podle emocí,"
                " podle videí na sociálních sítích nebo s penězi, které si"
                " nemůže dovolit ztratit."
            )
            st.info(
                "🧠 **Zralé investiční chování:** Rozumím, co kupuji. Vím, proč"
                " to kupuji. Znám riziko. Nesázím všechno na jednu kartu."
                " Nepanikařím při každém poklesu. Nepletu si investování se"
                " zábavní aplikací."
            )

        # Aktivita
        with st.container(border=True):
            st.markdown("#### 🎮 Aktivita: Staň se burzovním reportérem")
            st.write(
                "Vyber jednu burzu nebo index: BCPP, RM-SYSTÉM, NYSE, Nasdaq,"
                " DAX, S&P 500 nebo PX."
            )

            rep_market = st.selectbox(
                "Vyber burzu/index pro report:",
                ["BCPP", "RM-SYSTÉM", "NYSE", "Nasdaq", "DAX", "S&P 500", "PX"],
                key="k3_rep_mkt",
            )
            rep_firma = st.text_input(
                "Zadej typickou firmu / cenný papír pro report:",
                value="ČEZ",
                key="k3_rep_firm",
            )
            rep_riziko = st.text_input(
                "Hlavní riziko pro běžného investora:",
                value="Tržní propad a volatilita",
                key="k3_rep_riziko",
            )

            if st.button(
                "Vygenerovat a uložit výstup reportéra 💾", key="btn_k3_rep"
            ):
                zprava = (
                    f"🎙️ **Zpráva z trhu {rep_market}:** „Dobrý den, hlásíme se"
                    f" ze světa financí! Dnes se pozornost investorů zaměřila"
                    f" na {rep_firma}. Nezapomínejme ale na klíčová rizika,"
                    f" mezi kterými dominuje {rep_riziko}. Investujte opatrně,"
                    " přejeme vám úspěšný den a vracíme slovo do studia!“"
                )
                st.success(zprava)

                rep_data = (
                    f"Trh: {rep_market} | Firma: {rep_firma} | Riziko:"
                    f" {rep_riziko}"
                )
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"](
                        "Kapitola 2",
                        "Podkapitola 3.1 - Burzovní reportér",
                        rep_data,
                    )

    # =========================================================================
    # 3.2 VÝNOS, RIZIKO, LIKVIDITA A ČAS
    # =========================================================================
    elif "3.2 Výnos" in selected_section_2:
        st.markdown(
            "<div class='sub-section-header'>3. FINANČNÍ TRH A ANALÝZA"
            " RIZIK</div><h2>3.2 Výnos, riziko, likvidita a čas</h2>",
            unsafe_allow_html=True,
        )

        st.write(
            "Než se člověk začne bavit o konkrétních produktech, musí chápat"
            " čtyři základní otázky:"
        )
        st.markdown("""
        * Jaký může být výnos?
        * Jaké nesu riziko?
        * Jak rychle se dostanu k penězům?
        * Na jak dlouho peníze odkládám?
        """)

        st.info(
            "⚖️ **Investiční trojúhelník:** Výnos, riziko a likvidita spolu"
            " souvisejí. Vyšší možný výnos obvykle znamená vyšší riziko. Vysoký"
            " výnos, nulové riziko a okamžitá dostupnost peněz najednou jsou"
            " podezřelá kombinace."
        )

        # 3.2.1
        with st.container(border=True):
            st.markdown("### 3.2.1 Výnos")
            st.write(
                "Výnos je to, co investor získá navíc oproti původně vložené"
                " částce. Může mít podobu:"
            )
            st.markdown("""
            * úroku,
            * dividendy,
            * růstu ceny aktiva,
            * nájemného,
            * kurzového zisku,
            * kombinace více zdrojů.
            """)
            st.write(
                "Výnos ale není totéž co jistota. U některých produktů je"
                " předvídatelnější, u jiných se může výrazně měnit."
            )

        # 3.2.2
        with st.container(border=True):
            st.markdown("### 3.2.2 Riziko")
            st.write(
                "Riziko znamená možnost, že výsledek bude jiný, než člověk"
                " očekával. Může jít o nižší výnos, kolísání hodnoty, ztrátu"
                " části peněz nebo v extrémním případě ztrátu celé investice."
            )
            st.markdown(
                """
            | Druh rizika | Co znamená | Příklad |
            | :--- | :--- | :--- |
            | **Tržní riziko** | Cena aktiva kolísá podle vývoje trhu. | Akcie klesnou při ekonomické nejistotě. |
            | **Úvěrové riziko** | Dlužník nemusí splatit svůj závazek. | Firma nevykoupí dluhopis. |
            | **Likviditní riziko** | Aktivum nejde rychle prodat za rozumnou cenu. | Malý token nebo podíl v projektu nemá kupce. |
            | **Měnové riziko** | Změna kurzu měny ovlivní výsledek. | Investice v dolarech se přepočítává do korun. |
            | **Inflační riziko** | Výnos nestačí pokrýt růst cen. | Spoření nese 3 %, inflace je 6 %. |
            | **Regulační riziko** | Změna pravidel ovlivní dané aktivum nebo trh. | Stát zpřísní pravidla pro kryptoměnové služby. |
            | **Technologické riziko** | Selže systém, aplikace, úschova nebo zabezpečení. | Ztráta přístupu do kryptopeněženky. |
            """,
                unsafe_allow_html=True,
            )

        # 3.2.3 a 3.2.4
        with st.container(border=True):
            st.markdown("### 3.2.3 Likvidita")
            st.write(
                "Likvidita znamená, jak snadno lze aktivum proměnit zpět na"
                " peníze. Hotovost je velmi likvidní. Nemovitost bývá méně"
                " likvidní. Některé kryptoměnové tokeny mohou být prakticky"
                " nelikvidní, pokud je nikdo nechce koupit."
            )

            st.markdown("### 3.2.4 Časový horizont")
            st.write(
                "Časový horizont je doba, po kterou člověk plánuje peníze"
                " nechat investované. Krátký horizont se nehodí pro vysoce"
                " kolísavé investice. Pokud člověk ví, že peníze bude potřebovat"
                " za tři měsíce, neměl by je vystavovat velkým výkyvům."
            )

            st.success(
                "🧭 **Jednoduché pravidlo:** Nouzová rezerva patří do bezpečných"
                " a dostupných nástrojů. Investice s vyšším rizikem patří až k"
                " penězům, které člověk nepotřebuje na běžné výdaje ani na"
                " krizové situace."
            )

    # =========================================================================
    # 3.3 SPOŘENÍ, INVESTOVÁNÍ A SPEKULACE
    # =========================================================================
    elif "3.3 Spoření" in selected_section_2:
        st.markdown(
            "<div class='sub-section-header'>3. FINANČNÍ TRH A ANALÝZA"
            " RIZIK</div><h2>3.3 Spoření, investování a spekulace</h2>",
            unsafe_allow_html=True,
        )

        st.write("Tato tři slova se často pletou, ale znamenají rozdílné chování.")

        with st.container(border=True):
            st.markdown(
                """
            | Pojem | Co znamená | Typický příklad | Riziko |
            | :--- | :--- | :--- | :--- |
            | **Spoření** | Odkládání peněz s důrazem na bezpečnost a dostupnost. | Spořicí účet, termínovaný vklad. | Nízké, ale hrozí ztráta kupní síly kvůli inflaci. |
            | **Investování** | Vkládání peněz do aktiv s cílem dlouhodobého zhodnocení. | Akcie, dluhopisy, fondy, ETF. | Střední až vysoké podle produktu. |
            | **Spekulace** | Sázka na krátkodobý pohyb ceny. | Rychlé nákupy a prodeje kryptoměn nebo akcií podle trendu. | Vysoké. |
            """,
                unsafe_allow_html=True,
            )

            st.warning(
                "🧠 **Otázka před každým nákupem investice:** Kupuješ aktivum"
                " proto, že rozumíš jeho principu a riziku, nebo proto, že máš"
                " strach, že ti „ujede vlak“?"
            )

    # =========================================================================
    # 3.4 CENNÉ PAPÍRY V TEORII I PRAXI
    # =========================================================================
    elif "3.4 Cenné" in selected_section_2:
        st.markdown(
            "<div class='sub-section-header'>3. FINANČNÍ TRH A ANALÝZA"
            " RIZIK</div><h2>3.4 Cenné papíry v teorii i praxi</h2>",
            unsafe_allow_html=True,
        )

        st.write(
            "Cenný papír je listina nebo digitální záznam, se kterým jsou"
            " spojena určitá práva. Může jít například o právo na podíl ve"
            " firmě, právo na splacení dluhu, právo na úrok, právo na dividendu"
            " nebo právo podílet se na majetku fondu. Dříve si lidé pod cenným"
            " papírem představili hlavně fyzický papír s názvem firmy,"
            " hodnotou, podpisy a ochrannými prvky. Dnes je většina cenných"
            " papírů v praxi zaknihovaná — existuje jako elektronický záznam v"
            " evidenci."
        )

        st.info(
            "🧾 **Cenný papír jednoduše:** Není důležité jen to, jak „vypadá“."
            " Důležité je, jaké právo představuje. U akcie jde o vlastnictví"
            " části firmy. U dluhopisu jde o půjčku. U podílového listu jde o"
            " podíl na majetku fondu."
        )

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
            st.markdown(
                """
            | Podoba | Jak vypadá | Příklad |
            | :--- | :--- | :--- |
            | **Listinný cenný papír** | Fyzická listina. Může obsahovat název emitenta, hodnotu, práva vlastníka, datum vydání, podpisy, razítka nebo ochranné prvky. | Historická akcie, listinný dluhopis, směnka. |
            | **Zaknihovaný cenný papír** | Elektronický záznam v evidenci. Investor ho vidí na investičním účtu nebo v aplikaci. | Moderní akcie obchodovaná na burze, státní dluhopis, ETF. |
            """,
                unsafe_allow_html=True,
            )

            st.write(
                "**U cenného papíru nebo v jeho elektronickém záznamu se"
                " obvykle uvádí:**"
            )
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
            st.info(
                "📱 **Jak to vidí student v aplikaci:** Obvykle nevidí papírovou"
                " listinu, ale název instrumentu, ticker, ISIN, aktuální cenu,"
                " měnu, graf, počet kusů, hodnotu pozice, poplatky a tlačítko"
                " koupit/prodat."
            )

        # 3.4.2 až 3.4.4
        with st.container(border=True):
            st.markdown("### 3.4.2 Akcie: podíl na firmě")
            st.write(
                "Akcie představuje podíl na akciové společnosti. Když investor"
                " koupí akcii, stává se akcionářem, tedy spoluvlastníkem malé"
                " části firmy. Neznamená to, že může přijít do firmy a odnést"
                " si počítač nebo židli. Znamená to, že má určitá práva podle"
                " zákona, stanov společnosti a druhu akcie."
            )
            st.write(
                "Firma vydává akcie hlavně proto, aby získala vlastní kapitál."
                " Na rozdíl od úvěru nebo dluhopisu tyto peníze nemusí klasicky"
                " splatit. Na oplátku ale přijímá akcionáře — tedy vlastníky,"
                " kteří očekávají růst hodnoty firmy, dividendy nebo vliv na"
                " rozhodování."
            )

            st.info(
                "🏢 **Akcie v jedné větě:** Koupí akcie firmě nepůjčuješ."
                " Kupuješ si kousek jejího vlastnictví a podílíš se na jejím"
                " úspěchu i neúspěchu."
            )

            st.write("**Akcionář může mít:**")
            st.markdown("""
            * právo na dividendu, pokud ji firma vyplácí,
            * hlasovací právo na valné hromadě, pokud ho daný druh akcie obsahuje,
            * právo na informace podle pravidel společnosti,
            * právo podílet se na likvidačním zůstatku, pokud firma zaniká a po zaplacení dluhů něco zůstane,
            * možnost akcii prodat, pokud je převoditelná a existuje kupec.
            """)

            st.markdown("### 3.4.3 Druhy akcií")
            st.write(
                "Akcie nejsou všechny stejné. Liší se podle práv, podoby i"
                " způsobu obchodování."
            )
            st.markdown(
                """
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
            """,
                unsafe_allow_html=True,
            )

            st.markdown("### 3.4.4 Co je napsáno na akcii")
            st.write(
                "**Na listinné akcii nebo v elektronickém záznamu akcie bývá"
                " uvedeno:**"
            )
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
            st.write(
                "Jmenovitá hodnota je účetní nebo právní hodnota uvedená na"
                " akcii nebo ve stanovách. Tržní cena je cena, za kterou se"
                " akcie aktuálně prodává na trhu. Tyto částky se mohou výrazně"
                " lišit. Akcie může mít jmenovitou hodnotu 100 Kč, ale na trhu"
                " se může obchodovat za 850 Kč nebo za 40 Kč."
            )

        # 3.4.5 a 3.4.6
        with st.container(border=True):
            st.markdown(
                "### 3.4.5 Jak se akcie kupují a prodávají"
            )
            st.write(
                "Běžný člověk si většinou nekupuje akcie přímo od firmy."
                " Nejčastěji je kupuje přes banku, brokera, obchodníka s"
                " cennými papíry nebo investiční platformu."
            )
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
            * **limit pokyn** — investor stanoví maximální nákupní nebo minimální prodejní cenu,
            * **stop pokyn** — aktivuje se až po dosažení určité ceny.
            """)
            st.warning(
                "⚠️ **Pozor:** To, že lze akcii koupit během pár sekund,"
                " neznamená, že je rozhodnutí jednoduché. Investor by měl vědět,"
                " co firma dělá, jak vydělává, jaké má dluhy, konkurenci,"
                " rizika, měnu obchodování a poplatky."
            )

            st.markdown(
                "### 3.4.6 Jak akcie používají firmy a velké společnosti"
            )
            st.write(
                "**Firmy používají akcie hlavně k financování a změnám"
                " vlastnické struktury:**"
            )
            st.markdown("""
            * **založení akciové společnosti** — vlastníci vloží kapitál a získají akcie,
            * **navýšení kapitálu** — firma vydá nové akcie a získá peníze,
            * **IPO** — první veřejná nabídka akcií, tedy vstup firmy na burzu,
            * **další emise akcií** — firma později vydá nové akcie,
            * **akvizice** — firma může použít vlastní akcie při koupi jiné firmy,
            * **zaměstnanecké akcie a opce** — motivace zaměstnanců podílem na růstu firmy,
            * **zpětný odkup akcií** — firma nakupuje vlastní akcie z trhu.
            """)
            st.write(
                "Velké firmy s akciemi neobchodují jako student v aplikaci."
                " Často využívají investiční banky, právní poradce, makléře,"
                " burzy, blokové obchody a neveřejné transakce. Řeší nejen cenu,"
                " ale také vlastnickou kontrolu, dopad na kurz akcie, pověst,"
                " regulaci a vztahy s investory."
            )

        # 3.4.7 až 3.4.10
        with st.container(border=True):
            st.markdown(
                "### 3.4.7 Dluhopis: půjčka se slibem splacení"
            )
            st.write(
                "Dluhopis je cenný papír, kterým si emitent půjčuje peníze."
                " Emitentem může být stát, obec, banka nebo firma. Investor"
                " dluhopis koupí a tím emitentovi půjčí. Emitent se zavazuje,"
                " že peníze vrátí a obvykle zaplatí úrok."
            )
            st.info(
                "💸 **Dluhopis v jedné větě:** Koupí dluhopisu se nestáváš"
                " vlastníkem firmy. Stáváš se jejím věřitelem."
            )

            st.write("**Základní logika dluhopisu:**")
            st.markdown("""
            1. Emitent potřebuje peníze.
            2. Vydá dluhopisy.
            3. Investor dluhopis koupí.
            4. Emitent vyplácí úrok nebo jiný výnos.
            5. Na konci splatnosti vrátí jmenovitou hodnotu, pokud je schopný splácet.
            """)

            st.markdown(
                """
            | Pojem | Význam |
            | :--- | :--- |
            | **Emitent** | Ten, kdo dluhopis vydává a půjčuje si peníze. |
            | **Jmenovitá hodnota** | Částka, kterou má emitent při splatnosti vrátit. |
            | **Kupón** | Úrok nebo pravidelný výnos vyplácený investorovi. |
            | **Splatnost** | Datum, kdy má být dluhopis splacen. |
            | **Emisní kurz** | Cena, za kterou se dluhopis prodává při vydání. |
            | **Výnos do splatnosti** | Celkový výnos, pokud investor drží dluhopis do splatnosti a emitent splní závazky. |
            | **Rating** | Hodnocení schopnosti emitenta splácet závazky. |
            """,
                unsafe_allow_html=True,
            )

            st.markdown("### 3.4.8 Druhy dluhopisů")
            st.write(
                "Dluhopisy se liší podle emitenta, výnosu, splatnosti a rizika."
            )
            st.markdown(
                """
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
            """,
                unsafe_allow_html=True,
            )
            st.warning(
                "⚠️ **Pozor:** Dluhopis není automaticky bezpečný. Státní"
                " dluhopis stabilní země má jiné riziko než firemní dluhopis"
                " neznámé společnosti slibující vysoký úrok. Vysoký úrok často"
                " znamená vyšší riziko."
            )

            st.markdown("### 3.4.9 Co je napsáno na dluhopisu")
            st.write(
                "**U dluhopisu nebo v jeho emisních podmínkách bývá"
                " uvedeno:**"
            )
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
            st.write(
                "Reklama může ukazovat hlavně úrok, například „8 % ročně“."
                " Emisní podmínky ale říkají, kdo si půjčuje, na co peníze"
                " použije, kdy má splácet, zda je dluhopis zajištěný a co se"
                " stane při problémech."
            )

            st.markdown("### 3.4.10 Jak se dluhopisy kupují")
            st.write(
                "**Fyzická osoba nepodnikatel může dluhopisy koupit:**"
            )
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
            st.write(
                "Velké firmy a instituce obchodují dluhopisy často ve velkých"
                " objemech přes banky, dealingová oddělení, investiční banky a"
                " specializované trhy. Sledují úrokové sazby, rating,"
                " splatnost, likviditu, měnu, účetnictví a riziko protistrany."
            )

        # 3.4.11 až 3.4.14
        with st.container(border=True):
            st.markdown(
                "### 3.4.11 Podílové listy: podíl na majetku fondu"
            )
            st.write(
                "Podílový list vyjadřuje podíl investora na majetku podílového"
                " fondu. Investor tedy nekupuje přímo jednu konkrétní akcii"
                " nebo jeden dluhopis, ale kupuje podíl ve fondu, který drží"
                " celé portfolio."
            )
            st.write(
                "Fond shromažďuje peníze mnoha investorů a investuje je podle"
                " předem popsané strategie. Může investovat do akcií, dluhopisů,"
                " nástrojů peněžního trhu, nemovitostí nebo kombinace aktiv."
            )
            st.info(
                "🧺 **Podílový fond jednoduše:** Místo jedné položky kupuješ"
                " košík. V košíku mohou být desítky, stovky nebo tisíce investic"
                " podle strategie fondu."
            )

            st.markdown(
                "### 3.4.12 Druhy podílových fondů a podílových listů"
            )
            st.write(
                "Podílové fondy se liší podle toho, do čeho investují a jak"
                " fungují."
            )
            st.markdown(
                """
            | Druh fondu | Do čeho investuje | Typické riziko |
            | :--- | :--- | :--- |
            | **Fond peněžního trhu** | Krátkodobé a relativně konzervativní nástroje. | Nižší riziko, nižší očekávaný výnos. |
            | **Dluhopisový fond** | Dluhopisy států, firem nebo bank. | Úrokové a úvěrové riziko. |
            | **Akciový fond** | Akcie firem. | Vyšší kolísání hodnoty. |
            | **Smíšený fond** | Kombinace akcií, dluhopisů a dalších aktiv. | Riziko podle poměru jednotlivých složek. |
            | **Nemovitostní fond** | Nemovitosti nebo firmy spojené s nemovitostmi. | Riziko trhu nemovitostí a nižší likvidita. |
            | **Indexový fond** | Sleduje vybraný index. | Kopíruje vývoj trhu, který sleduje. |
            | **ETF** | Fond obchodovaný na burze, často sleduje index. | Tržní riziko, měnové riziko, poplatky. |
            """,
                unsafe_allow_html=True,
            )
            st.write("**Podílové listy mohou mít různé třídy:**")
            st.markdown("""
            * **akumulační třída** — výnosy se nevyplácejí, ale zůstávají ve fondu,
            * **distribuční třída** — výnosy se vyplácejí investorům,
            * **měnově zajištěná třída** — snaží se omezit dopad změny kurzu,
            * **měnově nezajištěná třída** — investor nese i měnové riziko.
            """)

            st.markdown(
                "### 3.4.13 Co je uvedeno u podílového listu nebo fondu"
            )
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
            st.info(
                "🔍 **Otázka před nákupem fondu:** Vím, do čeho fond investuje,"
                " kolik stojí na poplatcích, jak moc může kolísat a za jak"
                " dlouho se dostanu zpět k penězům?"
            )

            st.markdown("### 3.4.14 Jak se podílové listy kupují")
            st.write(
                "**Fyzická osoba nepodnikatel může koupit podílové listy:**"
            )
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
            st.write(
                "U podílového fondu investor obvykle podílový list nakupuje od"
                " fondu a při prodeji ho fondu odprodává zpět. U ETF je to"
                " jiné: ETF se obchoduje na burze podobně jako akcie, takže ho"
                " investor kupuje a prodává přes brokera za tržní cenu."
            )

        # 3.4.15 až 3.4.17
        with st.container(border=True):
            st.markdown(
                "### 3.4.15 Které cenné papíry se používají při obchodování"
                " firem"
            )
            st.write(
                "Firmy nepoužívají cenné papíry jen jako investici. V podnikové"
                " praxi mohou sloužit k financování, placení, zajištění i"
                " řízení rizik."
            )
            st.markdown(
                """
            | Cenný papír / nástroj | Jak ho firmy používají | Příklad |
            | :--- | :--- | :--- |
            | **Akcie** | Získání vlastního kapitálu, změna vlastnické struktury, vstup na burzu, akvizice. | Firma vydá nové akcie a získá peníze na expanzi. |
            | **Dluhopisy** | Získání cizího kapitálu bez klasického bankovního úvěru. | Firma vydá dluhopisy na financování nové technologie. |
            | **Směnka** | Písemný slib nebo příkaz zaplatit určitou částku v určité době. | Firma použije směnku při obchodním financování. |
            | **Šek** | Příkaz bance zaplatit určitou částku; v ČR dnes méně běžný. | Historicky používaný platební nástroj v obchodě. |
            | **Skladní list / náložný list** | Dokládá právo ke zboží nebo jeho přepravě. | V mezinárodním obchodě může dokument představovat nárok na zboží. |
            | **Podílové listy a fondy** | Uložení nebo diverzifikace volných prostředků. | Firma uloží část rezervy do konzervativního fondu podle své investiční politiky. |
            """,
                unsafe_allow_html=True,
            )
            st.info(
                "🏭 **Firemní pohled:** Domácnost řeší hlavně bezpečnost, výnos"
                " a dostupnost peněz. Firma navíc řeší cashflow, účetnictví,"
                " daně, kurzové riziko, vztahy s bankami, rating, pověst a"
                " odpovědnost vedení."
            )

            st.markdown(
                "### 3.4.16 Jak obchodují velké firmy a instituce"
            )
            st.write(
                "Velké firmy, banky, pojišťovny, penzijní fondy a investiční"
                " fondy obchodují ve větších objemech než běžný investor. Proto"
                " řeší i věci, které student v běžné aplikaci nevidí:"
            )
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

            st.markdown(
                "### 3.4.17 Kde může nakupovat fyzická osoba a kde podnikatel"
            )
            st.markdown(
                """
            | Kdo nakupuje | Kde může nakupovat | Na co si dát pozor |
            | :--- | :--- | :--- |
            | **Fyzická osoba nepodnikatel** | Banka, broker, obchodník s cennými papíry, investiční platforma, investiční společnost. | Poplatky, riziko, regulace, měna, daně, investiční horizont, ochrana účtu. |
            | **OSVČ / podnikatel** | Podobně jako fyzická osoba, ale musí řešit, zda investuje soukromé, nebo podnikatelské peníze. | Oddělení osobních a podnikatelských financí, účetnictví, daně, likvidita pro podnikání. |
            | **Právnická osoba / firma** | Firemní investiční účet, banka, broker, treasury oddělení, investiční banka. | Schválení vedením, investiční politika, účetní zachycení, rizikové limity, cashflow. |
            | **Velká korporace** | Investiční banky, kapitálové trhy, burzy, neveřejné transakce, emise vlastních cenných papírů. | Dopad na cenu, regulace, rating, vztahy s investory, reputace, strategické cíle. |
            """,
                unsafe_allow_html=True,
            )

        # 3.4.18 Praktická aktivita
        with st.container(border=True):
            st.markdown(
                "### 3.4.18 Praktická aktivita: pitva cenného papíru"
            )
            st.write("🔎 **Pitva cenného papíru: co přesně kupuji?**")
            st.write(
                "Vyber si jeden příklad: akcii, dluhopis, podílový fond nebo"
                " ETF. Neřeš, jestli je „dobrý“, ale zjisti, co přesně"
                " představuje."
            )

            cp_vyber = st.selectbox(
                "Vyber si aktivum pro pitvu:",
                ["...", "Akcie", "Dluhopis", "Podílový fond", "ETF"],
                key="k3_pitva_aktivita",
            )

            if cp_vyber != "...":
                if "vykresli_otazku_fn" in st.session_state:
                    st.session_state["vykresli_otazku_fn"](
                        "2.3.4",
                        f"Vytvoř rodný list pro cenný papír ({cp_vyber}):"
                        " Zjisti emitenta, podstatu, výnos, riziko, měnu,"
                        " poplatky, likviditu a horizont.",
                        "2",
                        st.session_state.get("ulozene_odpovedi", {}),
                    )

                with st.expander(
                    "💡 Nevíš si rady? Zobrazit vzorový rodný list pro kontrolu"
                ):
                    if cp_vyber == "Akcie":
                        st.info(
                            "**Ukázka - Akcie ČEZ, a.s.**\n* **Emitent:** ČEZ,"
                            " a.s.\n* **Podstata:** Podíl na firmě.\n*"
                            " **Výnos:** Dividenda a růst ceny akcie.\n*"
                            " **Rizika:** Tržní a specifická (změna zákonů,"
                            " cena elektřiny).\n* **Kde se obchoduje:** Burza"
                            " cenných papírů Praha.\n* **Měna:** CZK.\n*"
                            " **Poplatky:** Poplatek brokerovi za provedení"
                            " transakce.\n* **Likvidita:** Velmi rychlá (na"
                            " burze prodáš okamžitě).\n* **Horizont:** Dlouhý"
                            " (ideálně 5+ let).\n* **Jak prodělám:** Klesne"
                            " tržní cena akcie a firma přestane vyplácet"
                            " dividendy."
                        )
                    elif cp_vyber == "Dluhopis":
                        st.info(
                            "**Ukázka - Státní dluhopis ČR**\n* **Emitent:**"
                            " Ministerstvo financí ČR.\n* **Podstata:**"
                            " Půjčka státu (jsi věřitel).\n* **Výnos:** Předem"
                            " daný roční úrok (kupón).\n* **Rizika:**"
                            " Inflační riziko.\n* **Kde se obchoduje:** Přes"
                            " banky nebo na sekundárním trhu.\n* **Měna:**"
                            " CZK.\n* **Poplatky:** Žádné nebo minimální.\n*"
                            " **Likvidita:** Střední (lze vybrat v určitých"
                            " termínech).\n* **Horizont:** Střední (např. 3-6"
                            " let).\n* **Jak prodělám:** Inflace znehodnotí"
                            " peníze rychleji, než ti vydělá úrok."
                        )
                    elif cp_vyber == "Podílový fond":
                        st.info(
                            "**Ukázka - Akciový podílový fond v bance**\n*"
                            " **Správce:** Investiční společnost tvé"
                            " banky.\n* **Podstata:** Podíl ve fondu.\n*"
                            " **Výnos:** Podle zhodnocení košíku držených"
                            " akcií.\n* **Rizika:** Tržní riziko (pokles"
                            " trhů).\n* **Kde se obchoduje:** Přímo u tvé"
                            " banky/fondu.\n* **Měna:** CZK.\n* **Poplatky:**"
                            " Vstupní poplatek (cca 2-3 %) + průběžný (cca 1,5 %"
                            " ročně).\n* **Likvidita:** Dobrá (peníze dorazí"
                            " za pár dní).\n* **Horizont:** Dlouhý.\n* **Jak"
                            " prodělám:** Trh se propadne v krizi a ty ze"
                            " strachu vše odprodáš ve ztrátě dřív, než se trh"
                            " srovná."
                        )
                    elif cp_vyber == "ETF":
                        st.info(
                            "**Ukázka - Globální ETF (S&P 500)**\n*"
                            " **Správce:** Vanguard / iShares (BlackRock).\n*"
                            " **Podstata:** Podíl ve fondu (indexu největších"
                            " firem).\n* **Výnos:** Růst hodnoty amerického"
                            " trhu a dividendy.\n* **Rizika:** Tržní a"
                            " měnové.\n* **Kde se obchoduje:** Přímo na"
                            " mezinárodní burze.\n* **Měna:** USD nebo EUR.\n*"
                            " **Poplatky:** Velmi nízké správcovské (cca 0,07 %"
                            " ročně) + poplatek brokerovi.\n* **Likvidita:**"
                            " Velmi rychlá (okamžitě přes aplikaci).\n*"
                            " **Horizont:** Velmi dlouhý (10+ let).\n* **Jak"
                            " prodělám:** Trh se propadne v krizi a ty ze"
                            " strachu vše odprodáš ve ztrátě dřív, než se trh"
                            " srovná."
                        )

        # 3.4.19 Srovnání základních produktů
        with st.container(border=True):
            st.markdown("### 3.4.19 Srovnání základních produktů")
            st.markdown(
                """
            | Produkt | Co kupuji | Možný výnos | Hlavní riziko | Pro koho se může hodit |
            | :--- | :--- | :--- | :--- | :--- |
            | **Spořicí účet** | Vklad u banky. | Úrok. | Inflace může být vyšší než úrok. | Rezerva a krátkodobé cíle. |
            | **Termínovaný vklad** | Vklad na určitou dobu. | Úrok. | Nižší dostupnost peněz. | Peníze, které chvíli nepotřebuji. |
            | **Dluhopis** | Půjčku emitentovi. | Úrok nebo rozdíl ceny. | Emitent nemusí splatit. | Investor, který rozumí emitentovi a riziku. |
            | **Akcie** | Podíl na firmě. | Růst ceny, dividenda. | Pokles ceny firmy nebo trhu. | Dlouhodobý investor. |
            | **Fond / ETF** | Podíl v portfoliu více aktiv. | Podle vývoje aktiv. | Tržní pokles, poplatky. | Začátečník i dlouhodobý investor. |
            | **Kryptoměna** | Digitální aktivum v síti. | Růst ceny, případně jiné výnosy podle služby. | Vysoká volatilita, ztráta přístupu, podvod, regulace. | Pouze pro člověka, který chápe technologii a unese ztrátu. |
            """,
                unsafe_allow_html=True,
            )

    # =========================================================================
    # 3.5 ANALÝZA DAT: INVESTIČNÍ LABORATOŘ
    # =========================================================================
    elif "3.5 Analýza dat" in selected_section_2:
        st.markdown(
            "<div class='sub-section-header'>3. FINANČNÍ TRH A ANALÝZA"
            " RIZIK</div><h2>3.5 Analýza dat: investiční laboratoř</h2>",
            unsafe_allow_html=True,
        )

        st.write(
            "Investiční rozhodování nemá stát na větě „kamarád říkal“ nebo"
            " „viděl/a jsem video na TikToku“. Důležitá je práce s daty, ale i"
            " schopnost chápat jejich limity."
        )

        with st.container(border=True):
            st.markdown("### 🔬 Analytická laboratoř")
            st.write(
                "Vyber jedno aktivum nebo index — například akciový index,"
                " státní dluhopisový fond, zlato nebo kryptoměnu."
            )

            lab_vyber = st.selectbox(
                "Otestuj svou psychologii. Vyber si aktivum:",
                [
                    "...",
                    "Akciový index (např. S&P 500)",
                    "Státní dluhopisový fond",
                    "Zlato",
                    "Kryptoměna (např. Bitcoin)",
                ],
                key="k3_lab_vyber",
            )

            if lab_vyber != "...":
                st.info(
                    f"📊 **Představ si, že se graf pro {lab_vyber} propadne o 30"
                    " % až 50 % své hodnoty.**"
                )
                st.write(
                    "**Otázka k zamyšlení:** Vydržel/a bych psychicky držet"
                    " tuto investici i v době takového propadu?"
                )

                odpoved_lab = st.radio(
                    "Vyber upřímnou odpověď:",
                    [
                        "Vyber...",
                        "Ano, nepanikařil/a bych a čekal/a na zotavení",
                        "Asi ne, raději bych to se ztrátou prodal/a",
                        "Zatím nevím",
                    ],
                    key="k3_lab_radio",
                )

                if st.button(
                    "Uložit výsledek psychologického testu 💾", key="btn_k3_lab"
                ):
                    if odpoved_lab != "Vyber...":
                        if "uloz_odpoved_fn" in st.session_state:
                            st.session_state["uloz_odpoved_fn"](
                                "Kapitola 2",
                                "Podkapitola 3.5 - Investiční laboratoř"
                                " psychologie",
                                f"Aktivum: {lab_vyber} | Reakce: {odpoved_lab}",
                            )
                        st.success(
                            "Tvá odpověď k analytické laboratoři se uložila."
                        )
                    else:
                        st.warning("Vyber svou odpověď!")

        with st.container(border=True):
            st.markdown("### 🚀 SPUSTIT ŠKOLNÍ INVESTIČNÍ SIMULÁTOR")
            st.markdown("#### Otevřít simulátor akcií a bitcoinu")
            st.write(
                "Interaktivní aktivita: Vyzkoušej si modelové investování"
                " nanečisto — bez skutečných peněz a bez rizika. Sleduj, jak se"
                " může měnit hodnota akcií a bitcoinu v čase."
            )

            st.page_link(
                "pages/Školní_investiční_simulátor.py",
                label="🚀 PŘEJÍT DO SIMULÁTORU",
                use_container_width=True,
            )

        with st.container(border=True):
            st.markdown("### 3.5.1 Historický výnos není slib")
            st.write(
                "Historická data jsou užitečná, ale nejsou zárukou budoucnosti."
                " Pokud nějaké aktivum v minulosti rostlo, neznamená to, že"
                " poroste dál."
            )

    # =========================================================================
    # 3.6 KRYPTOMĚNY
    # =========================================================================
    elif "3.6 Kryptoměny" in selected_section_2:
        st.markdown(
            "<div class='sub-section-header'>6. KRYPTOMĚNY A NOVÉ FINANČNÍ"
            " TECHNOLOGIE</div>",
            unsafe_allow_html=True,
        )

        st.markdown(
            "## 3.6 Kryptoměny: technologie, peníze, spekulace i riziko"
        )
        st.write(
            "Kryptoměny jsou pro současnou generaci atraktivní, protože"
            " spojují technologie, internetovou kulturu, možnost rychlého"
            " zisku a příběh „nového finančního systému“."
        )

        st.markdown(
            """
        <div class="box-blue">
            <b>🪙 Kryptoměna jednoduše:</b> Kryptoměna je digitální aktivum, které existuje v počítačové síti.
            Záznamy o vlastnictví a převodech nejsou vedeny jednou běžnou bankou, ale pomocí technologie, která umožňuje sdílenou evidenci transakcí.
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
        <div class="box-red">
            <b>🚫 Důležité:</b> Tato kapitola není investiční doporučení. Cílem je rozumět principu, rizikům, reklamním trikům a rozdílu mezi technologií a spekulací.
        </div>
        """,
            unsafe_allow_html=True,
        )

        # 3.6.1 a 3.6.2
        st.markdown("### 3.6.1 Proč kryptoměny vznikly")
        st.write(
            "Kryptoměny vznikly jako reakce na otázku: *Lze vytvořit digitální"
            " peníze, které nepůjde jednoduše kopírovat a které nebudou závislé"
            " na jedné centrální autoritě?*"
        )

        st.markdown("### 3.6.2 Blockchain: účetní kniha, kterou sdílí síť")
        st.write(
            "Blockchain si můžeš představit jako řetěz bloků záznamů. Do bloků"
            " se zapisují transakce."
        )

        # 3.6.3 a 3.6.4
        st.markdown(
            "### 3.6.3 Peněženka, adresa, veřejný a soukromý klíč"
        )
        st.write(
            "Kryptoměny nejsou uložené „v peněžence“ stejným způsobem, jako máš"
            " mince v kapse."
        )

        st.markdown(
            """
        | Pojem | Co znamená | Přirovnání |
        | :--- | :--- | :--- |
        | **Veřejná adresa** | Adresa, na kterou lze poslat kryptoměnu. | Číslo účtu. |
        | **Soukromý klíč** | Tajný údaj, kterým se prokazuje právo s kryptoměnou nakládat. | Kombinace podpisového práva a trezoru. |
        | **Seed phrase** | Sada slov, ze které lze obnovit přístup k peněžence. | Hlavní klíč ke všemu. |
        """,
            unsafe_allow_html=True,
        )

        st.markdown("### 3.6.4 Bitcoin, Ethereum, stablecoiny a tokeny")
        st.write("Kryptoměny nejsou všechny stejné.")

        # --- ÚKOL (INTERAKTIVNÍ) ---
        st.markdown(
            "### 🧪 Krypto detektiv: ověř projekt dřív, než mu uvěříš"
        )
        st.write(
            "Vyber libovolný kryptoměnový projekt nebo token. **Nehodnoť, zda"
            " ho koupit, ale zda mu rozumíš.**"
        )

        semafor = st.selectbox(
            "Zvol úroveň rizika (Semafor):",
            [
                "Vyber hodnocení...",
                "🟢 Zelená (Nízké riziko, srozumitelný projekt)",
                "🟠 Oranžová (Střední riziko, nejasnosti nebo velká spekulace)",
                "🔴 Červená (Vysoké riziko, varovné signály, možný podvod)",
            ],
            key="k3_detektiv_semafor",
        )

        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"](
                "2.3.6",
                f"Krypto detektiv pro semafor ({semafor}): Zdůvodni v max. 3"
                " větách své hodnocení projektu.",
                "2",
                st.session_state.get("ulozene_odpovedi", {}),
            )

    # =========================================================================
    # 3.7 OCHRANA SPOTŘEBITELE
    # =========================================================================
    elif (
        "3.7 Ochrana spotřebitele" in selected_section_2
        or "3.7 Ochrana" in selected_section_2
    ):
        st.markdown(
            "<div class='sub-section-header'>7. OCHRANA SPOTŘEBITELE A"
            " REKLAMA</div>",
            unsafe_allow_html=True,
        )
        st.markdown("## 3.7 Ochrana spotřebitele a investiční reklama")
        st.write(
            "Finanční produkty se často prodávají jazykem emocí. Reklama může"
            " zdůraznit svobodu, rychlý zisk, strach z inflace nebo"
            " společenský status."
        )

    # =========================================================================
    # 3.8 INTERAKTIVNÍ AKTIVITY
    # =========================================================================
    elif "3.8 Interaktivní aktivity" in selected_section_2:
        st.markdown(
            "<div class='sub-section-header'>8. INTERAKTIVNÍ AKTIVITY K"
            " FINANČNÍMU TRHU</div>",
            unsafe_allow_html=True,
        )
        st.markdown("## 3.8 Interaktivní aktivity k finančnímu trhu")

        # AKTIVITA 1: TŘÍDĚNÍ
        st.markdown("### 🧩 Aktivita 1: Třídění finančních nástrojů")
        kategorie = [
            "Vyber...",
            "Spoření",
            "Investování",
            "Spekulace",
            "Hazard / Extrémní riziko",
        ]

        with st.form("trideni_form"):
            col1, col2 = st.columns(2)
            with col1:
                q1 = st.selectbox("Spořicí účet", kategorie, key="k3_a1_q1")
                q2 = st.selectbox("Státní dluhopis", kategorie, key="k3_a1_q2")
                q3 = st.selectbox(
                    "Akcie jedné firmy (stock picking)",
                    kategorie,
                    key="k3_a1_q3",
                )
                q4 = st.selectbox(
                    "ETF na široký index", kategorie, key="k3_a1_q4"
                )
                q5 = st.selectbox("Podílový fond", kategorie, key="k3_a1_q5")
            with col2:
                q6 = st.selectbox(
                    "Termínovaný vklad", kategorie, key="k3_a1_q6"
                )
                q7 = st.selectbox(
                    "Nákup meme coinu podle TikToku", kategorie, key="k3_a1_q7"
                )
                q8 = st.selectbox(
                    "Sázení na sport / ruleta", kategorie, key="k3_a1_q8"
                )
                q9 = st.selectbox(
                    "Kryptoměna držená bez pochopení rizika",
                    kategorie,
                    key="k3_a1_q9",
                )
                q10 = st.selectbox(
                    "Pravidelná investice do diverzifikovaného fondu",
                    kategorie,
                    key="k3_a1_q10",
                )

            submitted_trideni = st.form_submit_button(
                "Vyhodnotit a uložit moje odpovědi", type="primary"
            )

        if submitted_trideni:
            if "Vyber..." in [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]:
                st.warning("⚠️ Nezapomeň zařadit všechny položky!")
            else:
                st.success("✅ Odesláno! Výsledek uložen.")
                trideni_data = (
                    f"1:{q1} | 2:{q2} | 3:{q3} | 4:{q4} | 5:{q5} | "
                    f"6:{q6} | 7:{q7} | 8:{q8} | 9:{q9} | 10:{q10}"
                )
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"](
                        "Kapitola 2",
                        "Podkapitola 3.8 - Aktivita 1 Třídění",
                        trideni_data,
                    )

        st.divider()

        # AKTIVITA 2: POČASÍ
        st.markdown("### 📉 Aktivita 2: Investiční počasí")
        scenare = {
            "Vyber situaci...": None,
            "Trh raketově roste a všichni mluví o rychlém zisku": {
                "reakce_A": (
                    "Okamžitě nakupuje za jakoukoliv cenu, protože má strach, že"
                    " mu ujede vlak (FOMO)."
                ),
                "reakce_B": (
                    "Zůstává v klidu, drží se svého dlouhodobého plánu a"
                    " nepanikaří, i když ostatní 'rychle bohatnou'."
                ),
                "zacatecnik": "A",
                "vysvetleni": (
                    "Když trh strmě roste, začátečníci často naskakují na"
                    " vrcholu bubliny, protože vnímají jen nadšení zisků."
                ),
            },
            "Trh nečekaně spadl o 30 %": {
                "reakce_A": (
                    "Ví, že propady jsou normální. Ujistí se, že firmy/aktiva"
                    " neztratily svou skutečnou hodnotu, a případně využije"
                    " 'slevu' k dalším nákupům."
                ),
                "reakce_B": (
                    "Vyděsí se, že přijde o všechno, prodá v panice se ztrátou a"
                    " z trhu definitivně uteče."
                ),
                "zacatecnik": "B",
                "vysvetleni": (
                    "Nejhorší investiční chybou je nakupovat draze (v euforii) a"
                    " prodávat levně (v panice)."
                ),
            },
        }

        vybrana_situace = st.selectbox(
            "Vyber situaci na trhu:", list(scenare.keys()), key="k3_a2_situace"
        )

        if vybrana_situace != "Vyber situaci...":
            data = scenare[vybrana_situace]
            with st.container(border=True):
                col1, col2 = st.columns(2)
                with col1:
                    st.info(f"**Reakce A:**\n\n{data['reakce_A']}")
                    odpoved_A = st.radio(
                        "Kdo podle tebe provede Akci A?",
                        [
                            "Vyber...",
                            "Impulzivní začátečník",
                            "Informovaný investor",
                        ],
                        key="k3_a2_rad_A",
                    )
                with col2:
                    st.warning(f"**Reakce B:**\n\n{data['reakce_B']}")
                    odpoved_B = st.radio(
                        "Kdo podle tebe provede Akci B?",
                        [
                            "Vyber...",
                            "Impulzivní začátečník",
                            "Informovaný investor",
                        ],
                        key="k3_a2_rad_B",
                    )

                if st.button(
                    "Vyhodnotit a uložit moje skóre",
                    type="primary",
                    key="btn_k3_a2_pocasí",
                ):
                    if (
                        odpoved_A != "Vyber..."
                        and odpoved_B != "Vyber..."
                        and odpoved_A != odpoved_B
                    ):
                        st.success("✅ Přesně tak!")
                        pocasi_data = (
                            f"Situace: {vybrana_situace} | Reakce A:"
                            f" {odpoved_A} | Reakce B: {odpoved_B}"
                        )
                        if "uloz_odpoved_fn" in st.session_state:
                            st.session_state["uloz_odpoved_fn"](
                                "Kapitola 2",
                                "Podkapitola 3.8 - Aktivita 2 Investiční"
                                " počasí",
                                pocasi_data,
                            )

    # =========================================================================
    # 3.9 SHRNUTÍ & 3.10 DISCLAIMER
    # =========================================================================
    elif "3.9 Shrnutí" in selected_section_2:
        st.markdown(
            "<div class='sub-section-header'>9. SHRNUTÍ KAPITOLY</div>",
            unsafe_allow_html=True,
        )
        st.markdown("## 3.9 Shrnutí: co si z finančního trhu odnést")
        st.success(
            "🎉 Gratuluji k dokončení kapitoly o finančních trzích! Nyní jsi"
            " připraven/a využít tyto znalosti v praxi."
        )

    elif "3.10 Právní a etický disclaimer" in selected_section_2:
        st.markdown(
            "<div class='sub-section-header'>10. ZÁVĚREČNÉ UPOZORNĚNÍ</div>",
            unsafe_allow_html=True,
        )
        st.markdown("## 3.10 Právní a etický disclaimer")
        st.write(
            "Tato učebnice a všechny její součásti slouží **výhradně ke"
            " vzdělávacím účelům**."
        )

    # =========================================================================
    # 4.1 CO JE ÚVĚR
    # =========================================================================
    elif "4.1 " in selected_section_2:
        st.markdown(
            "<div class='sub-section-header'>1. ÚVĚRY A POJIŠTĚNÍ</div>",
            unsafe_allow_html=True,
        )
        st.markdown("## 4.1 Co je úvěr")
        st.write(
            "Úvěr není „peníze zdarma“. Je to závazek, který přesouvá spotřebu"
            " nebo investici z budoucnosti do současnosti."
        )

        with st.container(border=True):
            st.info(
                "Příběh: **Klára (25)** potřebuje auto na dojíždění do práce."
                " Půjčí si **200 000 Kč** od **Banky XY**. Dohodnou se, že Klára"
                " bude platit **4 500 Kč** každý měsíc po dobu **5 let**."
                " Celková cena úvěru se všemi poplatky vychází na **8,5 %"
                " ročně**."
            )

            q1 = st.selectbox(
                "Kdo je v tomto příběhu VĚŘITEL?",
                ["Vyber odpověď...", "Klára", "Banka XY", "Prodejce aut"],
                key="k4_1_q1",
            )
            q2 = st.selectbox(
                "Co představuje částka 200 000 Kč?",
                ["Vyber odpověď...", "Jistinu", "Úrok", "RPSN"],
                key="k4_1_q2",
            )
            q3 = st.selectbox(
                "Co představuje hodnota 8,5 %?",
                ["Vyber odpověď...", "Splatnost", "Jistinu", "RPSN"],
                key="k4_1_q3",
            )
            q4 = st.selectbox(
                "Co představuje doba 5 let?",
                ["Vyber odpověď...", "Splatnost", "Zajištění", "Splátku"],
                key="k4_1_q4",
            )

            if st.button(
                "Zkontrolovat a uložit mé odpovědi 💾",
                type="primary",
                key="btn_k4_1_uver",
            ):
                if "Vyber odpověď..." not in [q1, q2, q3, q4]:
                    if (
                        q1 == "Banka XY"
                        and q2 == "Jistinu"
                        and q3 == "RPSN"
                        and q4 == "Splatnost"
                    ):
                        st.success("✅ Výborně! Všechny pojmy jsi správně zařadil/a.")
                    odpovedi = f"1: {q1} | 2: {q2} | 3: {q3} | 4: {q4}"
                    if "uloz_odpoved_fn" in st.session_state:
                        st.session_state["uloz_odpoved_fn"](
                            "Kapitola 2",
                            "Podkapitola 4.1 - Úvěr v praxi",
                            odpovedi,
                        )

    # =========================================================================
    # 4.2 ÚROK & 4.3 RPSN
    # =========================================================================
    elif "4.2" in selected_section_2:
        st.markdown(
            "<div class='sub-section-header'>2. ÚVĚRY A POJIŠTĚNÍ</div>",
            unsafe_allow_html=True,
        )
        st.markdown("## 4.2 Úrok: cena půjčených peněz")

        doba_splaceni = st.slider(
            "Doba splácení (v letech):",
            min_value=1,
            max_value=10,
            value=5,
            key="k4_doba_splaceni",
        )
        sazba_mesicni = 0.08 / 12
        pocet_splatek = doba_splaceni * 12
        jistina = 100000
        splatka = (
            jistina
            * (sazba_mesicni * (1 + sazba_mesicni) ** pocet_splatek)
            / ((1 + sazba_mesicni) ** pocet_splatek - 1)
        )
        celkem_zaplaceno = splatka * pocet_splatek
        preplatek = celkem_zaplaceno - jistina

        col1, col2, col3 = st.columns(3)
        col1.metric("Měsíční splátka", f"{int(splatka):,} Kč".replace(",", " "))
        col2.metric(
            "Celkem zaplatíš", f"{int(celkem_zaplaceno):,} Kč".replace(",", " ")
        )
        col3.metric(
            "Přeplatek (čistý úrok)",
            f"{int(preplatek):,} Kč".replace(",", " "),
            delta_color="inverse",
        )

        if st.button("Uložit výpočet úvěru 💾", key="btn_k4_uver_calc"):
            uver_data = (
                f"Půjčka 100 000 na {doba_splaceni} let | Splátka:"
                f" {int(splatka)} Kč | Přeplatek: {int(preplatek)} Kč"
            )
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"](
                    "Kapitola 2", "Podkapitola 4.2 - Kalkulačka úvěru", uver_data
                )

    elif "4.3" in selected_section_2:
        st.markdown(
            "<div class='sub-section-header'>3. ÚVĚRY A POJIŠTĚNÍ</div>",
            unsafe_allow_html=True,
        )
        st.markdown("## 4.3 RPSN: skutečnější cena úvěru")

        c1 = st.checkbox(
            "Vím, kolik si půjčuji a kolik přesně celkem vrátím.",
            key="k4_chk_1",
        )
        c2 = st.checkbox(
            "Znám výši měsíční splátky a vím, jak dlouho budu splácet.",
            key="k4_chk_2",
        )
        c3 = st.checkbox(
            "Znám nejen úrokovou sazbu, ale hlavně RPSN.", key="k4_chk_3"
        )
        c4 = st.checkbox(
            "Vím o všech dalších poplatcích (za vedení, sjednání atd.).",
            key="k4_chk_4",
        )
        c5 = st.checkbox(
            "Vím, zda je úvěr zajištěný mým majetkem.", key="k4_chk_5"
        )
        c6 = st.checkbox(
            "Vím, jaké jsou sankce, když se se splátkou opozdím.",
            key="k4_chk_6",
        )
        c7 = st.checkbox(
            "Vím, zda a za kolik můžu úvěr splatit předčasně.", key="k4_chk_7"
        )

        if st.button("Uložit checklist před úvěrem 💾", key="btn_k4_predletova"):
            skore = sum([c1, c2, c3, c4, c5, c6, c7])
            chk_data = f"Odškrtnuto předletové kontroly: {skore}/7 bodů."
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"](
                    "Kapitola 2",
                    "Podkapitola 4.3 - Předletová kontrola úvěru",
                    chk_data,
                )

    # =========================================================================
    # 4.4 NE KAŽDÝ ÚVĚR DOSTANE & 4.5 POSTUP & 4.6 HYPOTÉKA
    # =========================================================================
    elif "4.4" in selected_section_2:
        st.markdown(
            "<div class='sub-section-header'>4. ÚVĚRY A POJIŠTĚNÍ</div>",
            unsafe_allow_html=True,
        )
        st.markdown("## 4.4 Ne každý úvěr dostane")

    elif "4.5" in selected_section_2:
        st.markdown(
            "<div class='sub-section-header'>5. ÚVĚRY A POJIŠTĚNÍ</div>",
            unsafe_allow_html=True,
        )
        st.markdown("## 4.5 Postup poskytnutí spotřebitelského úvěru")

    elif "4.6" in selected_section_2:
        st.markdown(
            "<div class='sub-section-header'>6. ÚVĚRY A POJIŠTĚNÍ</div>",
            unsafe_allow_html=True,
        )
        st.markdown("## 4.6 Hypotéka: úvěr na bydlení")

        cena_nemovitosti = st.slider(
            "Hodnota nemovitosti (Kč):",
            1000000,
            10000000,
            4000000,
            step=100000,
            key="k4_cena_nem",
        )
        vlastni_penize = st.slider(
            "Tvé vlastní úspory (Kč):",
            0,
            5000000,
            800000,
            step=50000,
            key="k4_vlastni_pen",
        )
        pozadovany_uver = cena_nemovitosti - vlastni_penize
        ltv = (
            (pozadovany_uver / cena_nemovitosti) * 100
            if cena_nemovitosti > 0
            else 0
        )

        col1, col2, col3 = st.columns(3)
        col1.metric(
            "Banka ti půjčí", f"{pozadovany_uver:,} Kč".replace(",", " ")
        )
        col2.metric("Tvé peníze", f"{vlastni_penize:,} Kč".replace(",", " "))
        col3.metric("LTV", f"{ltv:.1f} %")

        if st.button("Uložit výpočet LTV 💾", key="btn_k4_ltv"):
            ltv_data = (
                f"Nemovitost: {cena_nemovitosti} Kč | Vlastní: {vlastni_penize}"
                f" Kč | LTV: {ltv:.1f}%"
            )
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"](
                    "Kapitola 2", "Podkapitola 4.6 - Kalkulačka LTV", ltv_data
                )

    # =========================================================================
    # 4.7 až 4.10 POJIŠTĚNÍ & BNPL
    # =========================================================================
    elif "4.7" in selected_section_2:
        st.markdown(
            "<div class='sub-section-header'>7. ÚVĚRY A POJIŠTĚNÍ</div>",
            unsafe_allow_html=True,
        )
        st.markdown("## 4.7 Podnikatelské úvěry")

    elif "4.8" in selected_section_2:
        st.markdown(
            "<div class='sub-section-header'>8. ÚVĚRY A POJIŠTĚNÍ</div>",
            unsafe_allow_html=True,
        )
        st.markdown("## 4.8 Když se splácení pokazí")

    elif "4.9" in selected_section_2:
        st.markdown(
            "<div class='sub-section-header'>9. ÚVĚRY A POJIŠTĚNÍ</div>",
            unsafe_allow_html=True,
        )
        st.markdown("## 4.9 Past jménem „Kup teď, zaplať později“ (BNPL)")

        nakup = st.selectbox(
            "Vyber nákup, který bys chtěl/a zaplatit přes BNPL:",
            [
                "Vyber...",
                "Značkové tenisky (4 000 Kč)",
                "Lístky na letní festival s kamarády (3 500 Kč)",
                "Objednávka jídla na večerní párty (1 500 Kč)",
                "Nový herní doplněk / skiny (1 000 Kč)",
                (
                    "Rozbitý mobil, bez kterého nemůžu fungovat do školy/práce"
                    " (5 000 Kč)"
                ),
            ],
            key="k4_bnpl_nakup",
        )

        if nakup != "Vyber...":
            q1 = st.radio(
                "1. Je to pro tebe objektivní POTŘEBA, nebo spíš PŘÁNÍ?",
                [
                    "Je to potřeba (základ k fungování/přežití)",
                    "Je to přání (chci to pro radost, status nebo zážitek)",
                ],
                key="bnpl_1",
            )
            q2 = st.radio(
                "2. Koupil/a bys to teď, kdybys to musel/a zaplatit v HOTOVOSTI?",
                [
                    "Ano, peníze na to reálně mám už teď",
                    "Ne, tolik peněz bych z peněženky nedal/a",
                ],
                key="bnpl_2",
            )
            q3 = st.radio(
                "3. Co se stane, když ti výplata/brigáda nepřijde?",
                [
                    "Mám železnou rezervu, doplatím to z ní",
                    "Budu mít velký problém",
                ],
                key="bnpl_3",
            )

            if st.button(
                "Vyhodnotit a uložit nákup BNPL 💾",
                type="primary",
                key="btn_k4_bnpl_eval",
            ):
                bnpl_data = (
                    f"Nákup: {nakup} | Potřeba/Přání: {q1} | Hotovost: {q2} |"
                    f" Rezerva: {q3}"
                )
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"](
                        "Kapitola 2",
                        "Podkapitola 4.9 - BNPL Analyzátor",
                        bnpl_data,
                    )

    elif "4.10" in selected_section_2:
        st.markdown(
            "<div class='sub-section-header'>10. ÚVĚRY A POJIŠTĚNÍ</div>",
            unsafe_allow_html=True,
        )
        st.markdown("## 4.10 Pojištění: ochrana před finančním nárazem")

        rezerva = st.slider(
            "Jak velkou máš naspořenou rezervu na účtu?",
            0,
            500000,
            50000,
            step=10000,
            format="%d Kč",
            key="k4_10_rezerva",
        )
        udalost = st.selectbox(
            "Co se ti právě stalo?",
            [
                "Vyber událost...",
                "Rozbil se mi displej u mobilu (Škoda: 4 000 Kč)",
                "Ukradli mi starší kolo z garáže (Škoda: 15 000 Kč)",
                "Vytopil jsem sousedy pod sebou (Škoda: 180 000 Kč)",
                (
                    "Měl jsem vážný úraz a rok nebudu pracovat (Ztráta: 400 000"
                    " Kč)"
                ),
                "Dům mi lehl popelem (Škoda: 6 000 000 Kč)",
            ],
            key="k4_10_udalost",
        )

        if udalost != "Vyber událost...":
            skoda = int(
                udalost.split(":")[-1].replace(" Kč)", "").replace(" ", "")
            )
            zustatek = rezerva - skoda
            if st.button("Uložit výsledek nárazu 💾", key="btn_k4_10_naraz"):
                naraz_data = (
                    f"Rezerva: {rezerva} Kč | Událost: {udalost} | Zůstatek:"
                    f" {zustatek} Kč"
                )
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"](
                        "Kapitola 2",
                        "Podkapitola 4.10 - Finanční náraz",
                        naraz_data,
                    )

    elif "4.11" in selected_section_2:
        st.markdown(
            "<div class='sub-section-header'>11. ÚVĚRY A POJIŠTĚNÍ</div>",
            unsafe_allow_html=True,
        )
        st.markdown("## 4.11 Životní pojištění")

        a1 = st.checkbox("1. Živím někoho dalšího.", key="k4_11_a1")
        a2 = st.checkbox("2. Mám hypotéku nebo vysoký úvěr.", key="k4_11_a2")
        a3 = st.checkbox(
            "3. Nemám majetek ani rezervu na 1 rok.", key="k4_11_a3"
        )

        if st.button(
            "Vyhodnotit a uložit mou situaci 💾",
            type="primary",
            key="btn_k4_11_analyzator",
        ):
            skore = sum([a1, a2, a3])
            zivotko_data = f"Skóre potřeby: {skore}/3 rizika odškrtnuta."
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"](
                    "Kapitola 2",
                    "Podkapitola 4.11 - Analyzátor životního pojištění",
                    zivotko_data,
                )

    elif "4.12" in selected_section_2:
        st.markdown(
            "<div class='sub-section-header'>12. ÚVĚRY A POJIŠTĚNÍ</div>",
            unsafe_allow_html=True,
        )
        st.markdown("## 4.12 Neživotní pojištění")

        ans1 = st.selectbox(
            "Vestavěná kuchyňská linka na míru:",
            ["Vyber...", "Nemovitost", "Domácnost"],
            key="k4_12_ans1",
        )
        ans2 = st.selectbox(
            "Notebook a herní konzole:",
            ["Vyber...", "Nemovitost", "Domácnost"],
            key="k4_12_ans2",
        )
        ans3 = st.selectbox(
            "Radiátory a kotel:",
            ["Vyber...", "Nemovitost", "Domácnost"],
            key="k4_12_ans3",
        )
        ans4 = st.selectbox(
            "Drahý koberec a sedací souprava:",
            ["Vyber...", "Nemovitost", "Domácnost"],
            key="k4_12_ans4",
        )

        if st.button(
            "Zkontrolovat a uložit 💾", type="primary", key="btn_k4_12_kviz"
        ):
            majetek_data = (
                f"Linka: {ans1} | Notebook: {ans2} | Kotel: {ans3} | Koberec:"
                f" {ans4}"
            )
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"](
                    "Kapitola 2",
                    "Podkapitola 4.12 - Třídění majetku",
                    majetek_data,
                )

    elif "4.13" in selected_section_2:
        st.markdown(
            "<div class='sub-section-header'>13. ÚVĚRY A POJIŠTĚNÍ</div>",
            unsafe_allow_html=True,
        )
        st.markdown("## 4.13 Jak poznat dobré pojištění")

        pojistna_castka = st.slider(
            "Na kolik je dům pojištěn:",
            2000000,
            10000000,
            3000000,
            step=500000,
            key="k4_13_poj_castka",
        )
        skutecna_hodnota = st.slider(
            "Skutečná hodnota dnes:",
            2000000,
            15000000,
            6000000,
            step=500000,
            key="k4_13_skut_hodnota",
        )
        skoda = 500000
        vyplaceno = (
            skoda * (pojistna_castka / skutecna_hodnota)
            if pojistna_castka < skutecna_hodnota
            else skoda
        )

        if st.button("Uložit výsledek podpojištění 💾", key="btn_k4_13_podpojisteni"):
            podpojisteni_data = (
                f"Pojištěno na: {pojistna_castka} Kč | Skutečnost:"
                f" {skutecna_hodnota} Kč | Vyplaceno: {int(vyplaceno)} Kč"
            )
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"](
                    "Kapitola 2",
                    "Podkapitola 4.13 - Podpojištění domu",
                    podpojisteni_data,
                )
# =========================================================================
    # 4.14 PRAKTICKÉ ROZHODNOVÁNÍ: ÚVĚR A POJIŠTĚNÍ DOHROMADY
    # =========================================================================
    elif "4.14" in selected_section_2:
        st.markdown(
            "<div class='sub-section-header'>14. ÚVĚRY A POJIŠTĚNÍ</div>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "## 4.14 Praktické rozhodování: úvěr a pojištění dohromady"
        )

        st.write(
            "Úvěry a pojištění spolu neoddělitelně souvisí. Čím větší finanční"
            " závazek na sobě máš, tím více musíš řešit, co se stane při výpadku"
            " příjmu, nemoci, požáru nebo jiné životní krizi."
        )

        with st.container(border=True):
            st.markdown("### 👨‍👩‍👧‍👦 Modelový příklad z praxe:")
            st.write(
                "- **Situace:** Rodina si vzala hypotéku na dům 4 000 000 Kč."
                " Mají jedno malé dítě."
            )
            st.write(
                "- **Příjem:** Rodina spoléhá převážně na jeden hlavní příjem"
                " otce (45 000 Kč), matka je na rodičovské (10 000 Kč)."
            )
            st.write(
                "- **Závazek:** Měsíční splátka hypotéky činí 22 000 Kč. Dům je"
                " zastaven bance."
            )
            st.warning(
                "⚠️ **Riziko:** Pokud hlavní živitel dlouhodobě onemocní nebo"
                " utrpí úraz, rodina do 2 měsíců nedokáže platit splátku a"
                " hrozí jí ztráta střechy nad hlavou!"
            )
            st.success(
                "💡 **Řešení:** Vhodná kombinace: 1) Životní pojištění živitele"
                " (kryjící invaliditu a smrt), 2) Pojištění nemovitosti"
                " (zástava pro banku), 3) Finanční rezerva ve výši 6 splátek na"
                " spořicím účtu."
            )

        st.divider()

        # --- SIMULACE 1: BANKÉŘEM NA ZKOUŠKU ---
        st.markdown("### 🧪 Finanční simulace: Dostane žadatel úvěr?")
        st.write(
            "Vžij se do role bankovního risk manažera. Vyber si profil žadatele,"
            " posuď jeho situaci a rozhodni, zda mu půjčíš!"
        )

        profil = st.selectbox(
            "Vyber profil žadatele o úvěr:",
            [
                "Vyber žadatele...",
                "Žadatel A: Petr (22 let) – První auto na úvěr (150 000 Kč)",
                (
                    "Žadatelka B: Eva a Martin (30 let) – Hypotéka na byt (5 000"
                    " 000 Kč)"
                ),
                (
                    "Žadatel C: Pavel (35 let) – Spotřebitelský úvěr na"
                    " dovolenou (60 000 Kč)"
                ),
            ],
            key="k4_14_profil",
        )

        if profil.startswith("Žadatel A"):
            with st.container(border=True):
                st.markdown("#### 📋 Profil: Petr (22 let)")
                st.markdown("- **Požadavek:** 150 000 Kč na auto")
                st.markdown(
                    "- **Čistý příjem:** 24 000 Kč/měsíc (pracuje 4 měsíce, po"
                    " zkušební době)"
                )
                st.markdown("- **Výdaje a nájem:** 14 000 Kč/měsíc")
                st.markdown("- **Stávající dluhy:** Žádné")
                st.markdown("- **Vlastní úspory:** 5 000 Kč")

                sim_a1 = st.radio(
                    "1. Jak vyhodnotíš bonitu a schválení?",
                    [
                        "Schválit v plné výši",
                        "Zamítnout nebo nabídnout nižší částku",
                        "Schválit 100% částku bez doložení",
                    ],
                    key="sim_a1",
                )
                sim_a2 = st.radio(
                    "2. Jaké je pro Petra největší riziko?",
                    [
                        "Pokles ceny auta",
                        "Ztráta práce / nemoc bez finanční rezervy",
                        "Zvýšení úrokových sazeb u hypotéky",
                    ],
                    key="sim_a2",
                )

                if st.button("Vyhodnotit jako banka a uložit 💾", key="btn_sim_a"):
                    if "Zamítnout" in sim_a1 and "Ztráta práce" in sim_a2:
                        st.success(
                            "✅ **Správně!** Petr má extrémně nízkou rezervu"
                            " (jen 5 000 Kč). Měsíčně mu po výdajích zbývá 10"
                            " 000 Kč, ze kterých by splátka auta vzala معظم."
                            " Banka mu buď nabídne nižší částku, nebo"
                            " doporučí nejdříve naspořit rezervu."
                        )
                    else:
                        st.error(
                            "❌ **Chybně.** Jako bankéř bys riskoval/a. Petr"
                            " nemá téměř žádné úspory a v případě nemoci by"
                            " hned v prvním měsíci spadl do nesplácení."
                        )
                    if "uloz_odpoved_fn" in st.session_state:
                        st.session_state["uloz_odpoved_fn"](
                            "Kapitola 2",
                            "Podkapitola 4.14 - Bankéř (Petr)",
                            f"1:{sim_a1} | 2:{sim_a2}",
                        )

        elif profil.startswith("Žadatelka B"):
            with st.container(border=True):
                st.markdown("#### 📋 Profil: Eva a Martin (30 let)")
                st.markdown(
                    "- **Požadavek:** Hypotéka 4 500 000 Kč na byt v hodnotě"
                    " 5 000 000 Kč (LTV 90 %)"
                )
                st.markdown(
                    "- **Čistý příjem:** Společně 65 000 Kč/měsíc (smlouvy na"
                    " neurčito)"
                )
                st.markdown("- **Výdaje:** 25 000 Kč/měsíc")
                st.markdown("- **Vlastní úspory:** 600 000 Kč")

                sim_b1 = st.radio(
                    "1. Kolik vlastních peněz musí dát ze svého?",
                    [
                        "Alespoň 10–20 % (tj. min. 500 000 Kč)",
                        "Nemusí dát nic, banka půjčí 100 %",
                        "Musí mít naspořeno 50 %",
                    ],
                    key="sim_b1",
                )
                sim_b2 = st.radio(
                    "2. Jaké pojištění by měli absolutně prioritně sjednat?",
                    [
                        "Pojištění displeje mobilu",
                        (
                            "Pojištění nemovitosti + Životní pojištění pro"
                            " případ invalidity/smrti"
                        ),
                        "Havarijní pojištění auta",
                    ],
                    key="sim_b2",
                )

                if st.button("Vyhodnotit jako banka a uložit 💾", key="btn_sim_b"):
                    if "10–20 %" in sim_b1 and "Pojištění nemovitosti" in sim_b2:
                        st.success(
                            "✅ **Výborně!** Žadatelé mají dostatečný příjem i"
                            " vlastní úspory na LTV 90 %. Pojištění"
                            " nemovitosti bude vyžadovat sama banka jako"
                            " zástavu a životní pojištění ochrání jejich"
                            " společný rozpočet."
                        )
                    else:
                        st.error(
                            "❌ **Chyba v posouzení.** U hypotéky je nutný"
                            " vlastní základ a krytí životních rizik při"
                            " takto velkém dluhu."
                        )
                    if "uloz_odpoved_fn" in st.session_state:
                        st.session_state["uloz_odpoved_fn"](
                            "Kapitola 2",
                            "Podkapitola 4.14 - Bankéř (Eva a Martin)",
                            f"1:{sim_b1} | 2:{sim_b2}",
                        )

        elif profil.startswith("Žadatel C"):
            with st.container(border=True):
                st.markdown("#### 📋 Profil: Pavel (35 let)")
                st.markdown(
                    "- **Požadavek:** 60 000 Kč na luxusní dovolenou v"
                    " Karibiku"
                )
                st.markdown("- **Čistý příjem:** 32 000 Kč/měsíc")
                st.markdown(
                    "- **Stávající dluhy:** Splácí už kontokorent (20 000 Kč)"
                    " a kreditku (30 000 Kč)"
                )

                if st.button("Vyhodnotit jako banka a uložit 💾", key="btn_sim_c"):
                    st.error(
                        "🚨 **ZAMÍTNUTO!** Pavel vykazuje jasné známky"
                        " předlužení (kumuluje spotřebitelské dluhy) a chce si"
                        " půjčit na zážitek/spotřebu, která nemá žádnou trvalou"
                        " hodnotu. Banka úvěr zamítne z důvodu ochrany"
                        " spotřebitele i vysokého rizika dlužníka."
                    )
                    if "uloz_odpoved_fn" in st.session_state:
                        st.session_state["uloz_odpoved_fn"](
                            "Kapitola 2",
                            "Podkapitola 4.14 - Bankéř (Pavel)",
                            "Zamítnuto (Předlužení)",
                        )

        st.divider()

        # --- AKTIVITA 2: SROVNÁVAČ DVE PŮJČEK ---
        st.markdown("### 🧾 Aktivita: Porovnej dvě nabídky půjčky")
        st.write(
            "Potřebuješ si půjčit **50 000 Kč** na nový notebook do školy/práce"
            " se splatností na **2 roky (24 měsíců)**. Prohlédni si dvě nabídky:"
        )

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

        rozhodnuti = st.radio(
            "Kterou možnost bysis vybral/a?",
            [
                "Vyber možnost...",
                "Zvolil/a bych Nabídku A",
                "Zvolil/a bych Nabídku B (má přece nižší úrok 4,9 %!)",
                (
                    "Nepůjčil/a bych si vůbec – našetřil/a bych nebo koupil/a"
                    " levnější repasovaný notebook"
                ),
            ],
            key="k4_14_nabidka",
        )

        if st.button("Uložit mé rozhodnutí o půjčce 💾", key="btn_k4_14_srovnani"):
            if rozhodnuti == "Zvolil/a bych Nabídku A":
                st.success(
                    "✅ **Dobrá volba spotřebitele:** Nabídka A má sice o něco"
                    " vyšší udávaný úrok, ale díky nízkému RPSN a absenci"
                    " skrytých poplatků tě celkově stojí o 11 616 Kč MÉNĚ než"
                    " Nabídka B."
                )
            elif (
                rozhodnuti
                == "Zvolil/a bych Nabídku B (má přece nižší úrok 4,9 %!)"
            ):
                st.error(
                    "❌ **Skočil/a jsi na marketingový trik!** Nízký úrok 4,9 %"
                    " je jen návnada. Kvůli obřím poplatkům za sjednání a"
                    " vedení účtu je RPSN celých 28,5 % a přeplatíš o více než"
                    " 11 tisíc korun navíc!"
                )
            elif "Nepůjčil/a bych si vůbec" in rozhodnuti:
                st.success(
                    "🏆 **Nejlepší finanční rozhodnutí!** Na věci běžné"
                    " spotřeby nebo elektroniku je vždy nejbezpečnější si"
                    " našetřit z vlastních zdrojů nebo zvolit dostupnější"
                    " alternativu bez zadlužování."
                )

            if (
                "uloz_odpoved_fn" in st.session_state
                and rozhodnuti != "Vyber možnost..."
            ):
                st.session_state["uloz_odpoved_fn"](
                    "Kapitola 2",
                    "Podkapitola 4.14 - Srovnávač půjček",
                    rozhodnuti,
                )

    # =========================================================================
    # 4.15 SHRNUTÍ: CO SI ODNÉST
    # =========================================================================
    elif selected_section_2.startswith("4.15"):
        st.markdown(
            "<div class='sub-section-header'>15. ÚVĚRY A POJIŠTĚNÍ</div>",
            unsafe_allow_html=True,
        )
        st.markdown("## 4.15 Shrnutí kapitoly: Co si odnést")

        st.write(
            "Gratulujeme! Prošel/prošla jsi celou kapitolu o úvěrech,"
            " hypotékách a pojištění. Zde jsou nejdůležitější pravidla pro tvůj"
            " finanční život:"
        )

        st.markdown(
            """
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
        """,
            unsafe_allow_html=True,
        )

        st.divider()

        # --- AI MENTORING BOX ---
        st.markdown("### 🤖 Vyzkoušej AI Mentora")
        st.write(
            "Chceš si téma ještě lépe upevnit nebo se zeptat na cokoliv, co ti"
            " nebylo jasné? Zkopíruj tento text a vlož ho do svého oblíbeného AI"
            " asistenta:"
        )

        prompt_text = (
            "Vysvětli mi rozdíl mezi úrokem a RPSN na jednoduchém příkladu"
            " půjčky. Potom mi ukaž, jak banka posuzuje, jestli člověk dostane"
            " spotřebitelský úvěr nebo hypotéku."
        )

        st.code(prompt_text, language="text")
        st.caption(
            "💡 Tip: Můžeš AI požádat, aby ti položila 3 kontrolní otázky z této"
            " kapitoly!"
        )

    # =========================================================================
    # 5.1 PROČ PODNIK ŘEŠÍ FINANCE
    # =========================================================================
    elif selected_section_2.startswith("5.1 "):
        st.markdown(
            "<div class='sub-section-header'>5. FINANČNÍ ŘÍZENÍ V"
            " PODNIKU</div>",
            unsafe_allow_html=True,
        )
        st.markdown("## 5.1 Proč podnik řeší finance")

        st.write(
            "Finanční řízení podniku není jen práce účetní nebo „něco pro"
            " majitele firmy“. Je to způsob, jak firma zjišťuje, jestli dokáže"
            " přežít, růst, platit své závazky, zvládat rizika a dělat"
            " rozhodnutí podle dat místo pouhých pocitů."
        )
        st.write(
            "Pro dnešní generaci je to důležité i proto, že podnikání už nemusí"
            " vypadat jako obří továrna nebo kancelářský komplex. Firma může"
            " být **e-shop z pokoje, freelance tvorba grafiky, streamovací"
            " kanál, kosmetické studio, food truck, vývoj aplikace, školní"
            " projekt nebo profil influencera.** V každém případě ale platí"
            " stejná základní otázka: *přichází do podnikání víc hodnoty, než"
            " z něj odchází?*"
        )

        st.markdown(
            """
        <div class="box-blue">
            <b>📊 Základní myšlenka:</b> Finanční řízení pomáhá odpovědět na otázky: Kolik firma vydělává? Kolik skutečně utrácí? Má peníze na účtu? Zvládne splácet? Vyplatí se růst? Není příliš zadlužená? A pozná včas, že se blíží průšvih?
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.divider()

        st.markdown("### ⚠️ Paradox: Skvělý produkt ≠ Úspěšná firma")
        st.write(
            "Firma může mít skvělý produkt, tisíce sledujících, hezký web a"
            " plný kalendář zakázek — a přesto může mít obří finanční problém."
            " Důvod je jednoduchý: **popularita není totéž co zisk a zisk není"
            " totéž co peníze na účtu.**"
        )

        with st.container(border=True):
            st.markdown(
                "#### 🧪 Mini-simulátor: Proč zkrachoval úspěšný Food Truck?"
            )
            st.write(
                "Představ si food truck prodávající prémiové burgery. Místní ho"
                " milují, fronta je až za roh!"
            )

            prodejni_cena = st.slider(
                "Prodejní cena burgeru (Kč):",
                100,
                300,
                180,
                step=10,
                key="k5_1_cena_burgeru",
            )
            naklady_suroviny = 110
            ostatni_naklady_na_burger = 80

            celkove_naklady = naklady_suroviny + ostatni_naklady_na_burger
            zisk_na_kus = prodejni_cena - celkove_naklady

            col_sim1, col_sim2 = st.columns(2)
            col_sim1.metric("Celkové náklady na 1 burger", f"{celkove_naklady} Kč")

            if zisk_na_kus < 0:
                col_sim2.metric(
                    "Zisk / Ztráta na 1 burger",
                    f"{zisk_na_kus} Kč",
                    delta="Kráčíš ke krachu!",
                    delta_color="inverse",
                )
                st.error(
                    f"🚨 **Katastrofa!** I když prodáš 10 000 burgerů měsíčně a"
                    " všichni tě chválí, na každém burgeru proděláváš"
                    f" {abs(zisk_na_kus)} Kč. Čím více prodáváš, tím větší díru"
                    " do rozpočtu děláš!"
                )
            else:
                col_sim2.metric(
                    "Zisk / Ztráta na 1 burger",
                    f"{zisk_na_kus} Kč",
                    delta="Firma generuje zisk",
                    delta_color="normal",
                )
                st.success(
                    f"✅ **Super!** Na každém burgeru vyděláš {zisk_na_kus} Kč."
                    " Pokud ti zákazníci zaplatí včas, firma se udrží v zisku."
                )

        st.markdown(
            """
        <div class="box-green">
            <b>🧠 Pointa pro studenty:</b> Finanční řízení není o tom „být posedlý penězi“. Je o odpovědnosti. Pokud firma neumí řídit finance, může ohrozit nejen majitele, ale i zaměstnance, zákazníky, dodavatele a další lidi, kteří jsou na jejím fungování závislí.
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.divider()

        # =========================================================================
        # 5.1.1 KOHO ZAJÍMÁ FINANČNÍ ZDRAVÍ PODNIKU
        # =========================================================================
        st.markdown("### 5.1.1 Koho zajímá finanční zdraví podniku")
        st.write(
            "Finanční zdraví neřeší jen majitel. Zajímá mnoho skupin v okolí"
            " firmy (tzv. *stakeholderů*), protože každá z nich nese jiné"
            " riziko a pokládá si jiné otázky."
        )

        st.markdown("#### 👥 Proklikni si optiku jednotlivých aktérů:")

        aktéri = {
            "👑 Majitelé a společníci": {
                "důvod": (
                    "Chtějí vědět, zda firma vydělává, roste a neztrácí"
                    " hodnotu."
                ),
                "otázka": (
                    "„Vyplatí se v tomto podnikání pokračovat, nebo peníze"
                    " raději vytáhnout?“"
                ),
                "riziko": "Ztráta vloženého kapitálu a času.",
            },
            "👔 Management": {
                "důvod": (
                    "Potřebuje řídit ceny, náklady, investice, zásoby a lidi na"
                    " denní bázi."
                ),
                "otázka": (
                    "„Kde přesně nám utíkají peníze a co musíme od příštího"
                    " měsíce změnit?“"
                ),
                "riziko": (
                    "Špatná rozhodnutí a ztráta konkurenceschopnosti."
                ),
            },
            "👷 Zaměstnanci": {
                "důvod": (
                    "Zajímá je stabilita práce, pravidelné výplaty a budoucnost"
                    " firmy."
                ),
                "otázka": (
                    "„Bude mít firma příští měsíc na mé mzdy, nebo si mám"
                    " hledat novou práci?“"
                ),
                "riziko": "Ztráta zaměstnání a neproplacené mzdy.",
            },
            "🏦 Banka": {
                "důvod": (
                    "Posuzuje, zda firma zvládne bezpečně splácet úvěr i s"
                    " úroky."
                ),
                "otázka": (
                    "„Má firma dostatečně stabilní cashflow na měsíční"
                    " splátky?“"
                ),
                "riziko": "Nesplacení půjčky a vznik nespláceného dluhu.",
            },
            "🚀 Investor": {
                "důvod": (
                    "Hledá potenciál rychlého růstu, vysokou návratnost a míru"
                    " rizika."
                ),
                "otázka": (
                    "„Má tato firma šanci desetinásobně vyrůst a ovládnout"
                    " trh?“"
                ),
                "riziko": "Investice do podniku, který zkrachuje.",
            },
            "🚚 Dodavatelé": {
                "důvod": (
                    "Řeší, jestli firma zaplatí vystavené faktury včas a v plné"
                    " výši."
                ),
                "otázka": (
                    "„Není riziko dodávat jim zboží na fakturu se splatností 30"
                    " dní?“"
                ),
                "riziko": (
                    "Druhotná platební neschopnost (nedostanou zaplaceno za"
                    " své zboží)."
                ),
            },
            "🛒 Zákazníci": {
                "důvod": (
                    "U dlouhodobých služeb a záruk potřebují jistotu, že firma"
                    " ze dne na den nezmizí."
                ),
                "otázka": (
                    "„Bude tato služba nebo garance fungovat i za rok?“"
                ),
                "riziko": "Ztráta zaplacené zálohy nebo nefunkční záruka.",
            },
            "🏛️ Stát a Obec": {
                "důvod": (
                    "Zajímá je řádné placení daní, pojistného, tvorba"
                    " pracovních míst a rozvoj regionu."
                ),
                "otázka": (
                    "„Plní firma své zákonné povinnosti a podporuje lokální"
                    " ekonomiku?“"
                ),
                "riziko": "Daňové úniky nebo růst nezaměstnanosti v regionu.",
            },
        }

        vybrany_akter = st.selectbox(
            "Vyber skupinu, jejíž pohled tě zajímá:",
            list(aktéri.keys()),
            key="k5_1_akter",
        )

        if vybrany_akter:
            data = aktéri[vybrany_akter]
            with st.container(border=True):
                st.markdown(f"### {vybrany_akter}")
                st.write(f"**Proč je to zajímá:** {data['důvod']}")
                st.info(f"❓ **Typická otázka:** {data['otázka']}")
                st.warning(f"⚠️ **Největší riziko pro ně:** {data['riziko']}")

        st.divider()

        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"](
                "2.5.1",
                "🧩 Aktivita: Domino efekt – Vyber si libovolnou firmu z okolí"
                " a popiš, co by se stalo a kdo by utrpěl škodu, kdyby přestala"
                " ze dne na den platit své závazky.",
                "2",
                st.session_state.get("ulozene_odpovedi", {}),
            )

    # =========================================================================
    # 5.2 ZÁKLADNÍ FINANČNÍ VÝKAZY: MAPA FIRMY V ČÍSLECH
    # =========================================================================
    elif selected_section_2.startswith("5.2 "):
        st.markdown(
            "<div class='sub-section-header'>5. FINANČNÍ ŘÍZENÍ V"
            " PODNIKU</div>",
            unsafe_allow_html=True,
        )
        st.markdown("## 5.2 Základní finanční výkazy: mapa firmy v číslech")

        st.write(
            "Aby šlo firmu bezpečně řídit, nestačí říct „daří se nám“ nebo"
            " „nějak to funguje“. Firma potřebuje přesná čísla. Základní"
            " finanční výkazy fungují jako palubní deska v autě — ukazují, co"
            " firma vlastní, co dluží, kolik vydělala, kolik utratila a jak se"
            " pohybovaly peníze."
        )

        with st.container(border=True):
            st.markdown(
                "### 5.2.1 Rozvaha: co firma má a z čeho to financuje"
            )
            st.write(
                "Rozvaha ukazuje majetek firmy (**Aktiva**) a současně zdroje,"
                " ze kterých je tento majetek financovaný (**Pasiva**)."
            )

            col_a, col_p = st.columns(2)
            with col_a:
                penize = st.number_input(
                    "Peníze na účtu a v pokladně (Kč):",
                    value=25000,
                    step=5000,
                    key="act_penize",
                )
                zasoby = st.number_input(
                    "Zásoby zboží na skladě (Kč):",
                    value=30000,
                    step=5000,
                    key="act_zasoby",
                )
                vybaneni = st.number_input(
                    "Notebook a balicí technika (Kč):",
                    value=15000,
                    step=5000,
                    key="act_vyb",
                )
                aktiva_celkem = penize + zasoby + vybaneni
                st.metric(
                    "Aktiva Celkem", f"{aktiva_celkem:,} Kč".replace(",", " ")
                )

            with col_p:
                vklad = st.number_input(
                    "Vlastní vklad majitele (Kč):",
                    value=40000,
                    step=5000,
                    key="pas_vklad",
                )
                uver = st.number_input(
                    "Bankovní úvěr (Kč):",
                    value=20000,
                    step=5000,
                    key="pas_uver",
                )
                zavazky = st.number_input(
                    "Nezaplacené faktury dodavatelům (Kč):",
                    value=10000,
                    step=5000,
                    key="pas_zavazky",
                )
                pasiva_celkem = vklad + uver + zavazky
                st.metric(
                    "Pasiva Celkem", f"{pasiva_celkem:,} Kč".replace(",", " ")
                )

        with st.container(border=True):
            st.markdown("### 5.2.2 Výkaz zisku a ztráty & 5.2.3 Cashflow")
            st.write("Výkaz zisku a ztráty ukazuje výnosy a náklady za období.")

    # =========================================================================
    # 5.3 NÁKLADY, VÝNOSY A BOD ZVRATU
    # =========================================================================
    elif selected_section_2.startswith("5.3"):
        import matplotlib.pyplot as plt
        import numpy as np

        st.markdown(
            "<div class='sub-section-header'>5. FINANČNÍ ŘÍZENÍ V"
            " PODNIKU</div>",
            unsafe_allow_html=True,
        )
        st.markdown("## 5.3 Náklady, výnosy a bod zvratu")

        with st.container(border=True):
            col1, col2, col3 = st.columns(3)
            with col1:
                fixni = st.number_input(
                    "Fixní náklady [Kč]",
                    min_value=0,
                    value=50000,
                    step=1000,
                    key="k5_bep_fix",
                )
            with col2:
                variabilni = st.number_input(
                    "Variabilní náklady/ks [Kč]",
                    min_value=0,
                    value=200,
                    step=10,
                    key="k5_bep_var",
                )
            with col3:
                cena = st.number_input(
                    "Prodejní cena/ks [Kč]",
                    min_value=0,
                    value=400,
                    step=10,
                    key="k5_bep_cena",
                )

            marze = cena - variabilni

            if marze > 0:
                bep_ks = fixni / marze
                bep_kc = bep_ks * cena
                prvni_ziskovy_kus = math.floor(bep_ks) + 1
                st.success(
                    f"🎯 **Bod zvratu (zisk = 0):** {bep_ks:.1f} ks (Tržby:"
                    f" {bep_kc:,.0f} Kč)"
                )

                max_ks = int(bep_ks * 2) if bep_ks > 0 else 100
                x = np.linspace(0, max_ks, 100)
                naklady = fixni + (variabilni * x)
                trzby = cena * x
                zisk = trzby - naklady

                fig, ax = plt.subplots(figsize=(8, 4))
                ax.plot(x, naklady, label="Celkové náklady", color="#e74c3c")
                ax.plot(x, trzby, label="Tržby", color="#2ecc71")
                ax.scatter(bep_ks, bep_kc, color="black", zorder=5)
                ax.grid(True)
                st.pyplot(fig)

    # =========================================================================
    # 5.4 ZDROJE FINANCOVÁNÍ & 5.5 FINANČNÍ ANALÝZA
    # =========================================================================
    elif selected_section_2.startswith("5.4 "):
        st.markdown(
            "<div class='sub-section-header'>5. FINANČNÍ ŘÍZENÍ V"
            " PODNIKU</div>",
            unsafe_allow_html=True,
        )
        st.markdown("## 5.4 Zdroje financování podniku")

    elif selected_section_2.startswith("5.5 "):
        st.markdown(
            "<div class='sub-section-header'>5. FINANČNÍ ŘÍZENÍ V"
            " PODNIKU</div>",
            unsafe_allow_html=True,
        )
        st.markdown("## 5.5 Finanční analýza: kontrola finančního zdraví")

    elif selected_section_2.startswith("5.6"):
        st.markdown(
            "<div class='sub-section-header'>5. FINANČNÍ ŘÍZENÍ V"
            " PODNIKU</div>",
            unsafe_allow_html=True,
        )
        st.markdown("## 5.6 Modelová finanční analýza: e-shop „DropZone“")

    elif selected_section_2.startswith("5.7"):
        import pandas as pd

        st.markdown(
            "<div class='sub-section-header'>5. FINANČNÍ ŘÍZENÍ V"
            " PODNIKU</div>",
            unsafe_allow_html=True,
        )
        st.markdown("## 5.7 Prázdná šablona finanční analýzy")

    elif selected_section_2.startswith("5.8"):
        st.markdown(
            "<div class='sub-section-header'>5. FINANČNÍ ŘÍZENÍ V"
            " PODNIKU</div>",
            unsafe_allow_html=True,
        )
        st.markdown("## 5.8 Jak napsat závěr finanční analýzy")

    elif selected_section_2.startswith("5.9"):
        st.markdown(
            "<div class='sub-section-header'>5. FINANČNÍ ŘÍZENÍ V"
            " PODNIKU</div>",
            unsafe_allow_html=True,
        )
        st.markdown("## 5.9 Case study: Influencer jako firma")

    elif selected_section_2.startswith("5.10"):
        st.markdown(
            "<div class='sub-section-header'>5. FINANČNÍ ŘÍZENÍ V"
            " PODNIKU</div>",
            unsafe_allow_html=True,
        )
        st.markdown("## 5.10 Digitální generace a finanční řízení")

    elif selected_section_2.startswith("5.11"):
        st.markdown(
            "<div class='sub-section-header'>5. FINANČNÍ ŘÍZENÍ V"
            " PODNIKU</div>",
            unsafe_allow_html=True,
        )
        st.markdown("## 5.11 Praktická aktivita: Finanční manažer na 45 minut")

    elif selected_section_2.startswith("5.12"):
        st.markdown(
            "<div class='sub-section-header'>5. FINANČNÍ ŘÍZENÍ V"
            " PODNIKU</div>",
            unsafe_allow_html=True,
        )
        st.markdown("## 5.12 Shrnutí: co si odnést")

    # =========================================================================
    # KAPITOLA 6: INTERAKTIVNÍ VRSTVA CELÉ KAPITOLY (PRACOVNÍ SEŠIT)
    # =========================================================================
    elif selected_section_2.startswith("6"):
        st.markdown(
            "<div class='sub-section-header'>6. INTERAKTIVNÍ CVIČENÍ A"
            " ÚKOLY</div>",
            unsafe_allow_html=True,
        )
        st.markdown("## 6. Interaktivní pracovní sešit")

        workbook_section = st.radio(
            "Vyber si aktivitu:",
            [
                "🧭 Startovací diagnostika",
                "🔐 Bezpečnostní challenge (Poznej podvod)",
                "📱 Algoritmy utrácení",
                "🛟 Simulátor nečekané události",
                "🧮 Můj první byznys (Bod zvratu)",
                "✅ Exit ticket (Co si odnáším)",
            ],
            horizontal=True,
            key="wb_nav",
        )

        st.divider()

        if workbook_section == "📱 Algoritmy utrácení":
            st.markdown("### 🧠 Algoritmy utrácení: Kdo mě ovlivňuje?")

            if "vykresli_otazku_fn" in st.session_state:
                st.session_state["vykresli_otazku_fn"](
                    "2.6.1",
                    "🧠 Algoritmy utrácení: Vyber jeden svůj nedávný nákup a"
                    " popiš, co jsi koupil/a, jaká taktika na tebe zapůsobila a"
                    " zda bys to koupil/a i bez slevy.",
                    "2",
                    st.session_state.get("ulozene_odpovedi", {}),
                )

        elif workbook_section == "✅ Exit ticket (Co si odnáším)":
            st.markdown("### ✅ Exit ticket: Závěrečná reflexe")

            if "vykresli_otazku_fn" in st.session_state:
                st.session_state["vykresli_otazku_fn"](
                    "2.6.2",
                    "✅ Exit ticket: Napiš 1. věc, kterou jsi pochopil/a"
                    " nově, 2. rozhodnutí, u kterého příště zpomalíš, a 3."
                    " otázku pro poradce/podnikatele.",
                    "2",
                    st.session_state.get("ulozene_odpovedi", {}),
                )

    # =========================================================================
    # KAPITOLA 7: AKTIVITA - OPTIMALIZACE VÝDAJŮ
    # =========================================================================
    elif selected_section_2.startswith("7"):
        st.markdown(
            "<div class='sub-section-header'>7. PRAKTICKÁ AKTIVITA</div>",
            unsafe_allow_html=True,
        )
        st.markdown("## 7. Aktivita: Optimalizace rozpočtu")

        with st.form("form_uspory"):
            c1, c2, c3, c4 = st.columns([3, 2, 3, 2])
            c1.markdown("**Název výdaje**")
            c2.markdown("**Původní cena**")
            c3.markdown("**Jak to změním?**")
            c4.markdown("**Nová cena**")

            v1_nazev = c1.text_input(
                "Výdaj 1", key="v1_n", label_visibility="collapsed"
            )
            v1_stara = c2.number_input(
                "Cena 1",
                min_value=0,
                value=300,
                step=50,
                key="v1_s",
                label_visibility="collapsed",
            )
            v1_zmena = c3.text_input(
                "Změna 1", key="v1_z", label_visibility="collapsed"
            )
            v1_nova = c4.number_input(
                "Nová cena 1",
                min_value=0,
                value=0,
                step=50,
                key="v1_no",
                label_visibility="collapsed",
            )

            submitted = st.form_submit_button(
                "Spočítat a uložit moji roční úsporu 💾"
            )

            if submitted:
                uspora_mesic = v1_stara - v1_nova
                uspora_rok = uspora_mesic * 12
                st.success(f"Ušetřeno za rok: {uspora_rok:,} Kč")
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"](
                        "Kapitola 2",
                        "Aktivita 7 - Optimalizace rozpočtu",
                        f"Úspora rok: {uspora_rok} Kč",
                    )

    # =========================================================================
    # KAPITOLA 8: SLOVNÍK CIZÍCH POJMŮ
    # =========================================================================
    elif selected_section_2.startswith("8"):
        import random
        import pandas as pd

        st.markdown(
            "<div class='sub-section-header'>8. ZÁVĚREČNÝ PŘEHLED</div>",
            unsafe_allow_html=True,
        )
        st.markdown("## 8. Slovník cizích pojmů")

        slovnik_data = [
            {
                "Pojem": "Aktiva",
                "Vysvětlení": "Majetek firmy nebo člověka.",
            },
            {
                "Pojem": "RPSN",
                "Vysvětlení": "Roční procentní sazba nákladů úvěru.",
            },
        ]
        df_slovnik = pd.DataFrame(slovnik_data)
        st.dataframe(df_slovnik, use_container_width=True, hide_index=True)
