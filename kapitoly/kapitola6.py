import math
import requests
import plotly.graph_objects as go
import streamlit as st


def ziskej_odpoved_od_ai(zprava_zaka):
    """
    Neprůstřelná funkce pro volání AI. Pokud selže API, přepne na offline hodnocení.
    """
    # 1. POKUS: Volání skutečné AI přes čisté HTTP (nepodléhá změnám SDK verzí)
    try:
        api_key = st.secrets.get("OPENAI_API_KEY", "")
        if api_key:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"
            }
            # Systémový prompt, který instruuje AI, jak má hrát roli
            system_prompt = (
                "Jsi Karel, arogantní ale nesmírně talentovaný grafik. Šéf ti právě píše ohledně tvého "
                "včerejšího toxického chování k juniorovi. Odpověz mu z pohledu Karla. "
                "Hned pod to přidej oddělovač '---' a napiš hodnocení jako AI Mentor. "
                "Ohodnoť jeho zprávu (0-10) v kategoriích: Empatie, Jasnost, Autorita a dej mu krátkou radu."
            )
            
            payload = {
                "model": "gpt-4o-mini", # Standardní stabilní model
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": zprava_zaka}
                ],
                "temperature": 0.7,
                "max_tokens": 500
            }
            
            # Timeout 10 sekund, aby aplikace nezamrzla, pokud má AI výpadek
            response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                return data["choices"][0]["message"]["content"]
    except Exception:
        pass # Pokud API selže, tiše to přejdeme a spustíme Záchranný plán B
        
    # 2. ZÁCHRANNÝ PLÁN B (Offline heuristika, pokud AI spadne)
    delka = len(zprava_zaka.split())
    text_lower = zprava_zaka.lower()
    
    if delka < 5:
        return (
            "👨‍🎨 **Karel:** „To jako vážně? Takhle stručně to se mnou řešíš? Nemám čas na hádanky, jdu pracovat.“\n\n"
            "---\n\n"
            "🤖 **AI Mentor (Offline režim):** Tvá zpráva byla příliš krátká. "
            "**Jasnost (2/10), Empatie (1/10), Autorita (3/10).** Jako manažer musíš problém vysvětlit a jasně komunikovat svá očekávání."
        )
    elif "vyhazov" in text_lower or "končíš" in text_lower or "výpověď" in text_lower:
        return (
            "👨‍🎨 **Karel:** „Fajn! Mám tři další nabídky, kde mě aspoň docení. Zítra už nepřijdu.“\n\n"
            "---\n\n"
            "🤖 **AI Mentor (Offline režim):** Reagoval jsi velmi radikálně. "
            "**Jasnost (9/10), Empatie (0/10), Autorita (9/10).** Vyhodit toxického zaměstnance je někdy nutné, ale v této situaci firma právě přišla o klíčového klienta. Zkus to příště více diplomaticky."
        )
    elif "prosím" in text_lower or "omlouvám" in text_lower or "mrzí mě" in text_lower:
        return (
            "👨‍🎨 **Karel:** „No dobře, vím, že jsem to přehnal. Omlouvám se.“\n\n"
            "---\n\n"
            "🤖 **AI Mentor (Offline režim):** Použil jsi mírný a vyjednávací tón. "
            "**Jasnost (6/10), Empatie (8/10), Autorita (4/10).** Uklidnil jsi situaci, ale dej pozor, aby tě Karel nezačal brát jako slabého šéfa. Hranice musí být pevné."
        )
    else:
        return (
            "👨‍🎨 **Karel:** „Jasně, rozumím. Srovnám se. Neuvědomil jsem si, že to vyznělo tak blbě.“\n\n"
            "---\n\n"
            "🤖 **AI Mentor (Offline režim):** Standardní a profesionální komunikace. "
            "**Jasnost (7/10), Empatie (6/10), Autorita (7/10).** Věcně jsi upozornil na problém. Dobrá manažerská práce."
        )

def render_ai_treenazer():
    st.markdown("#### 🎭 AI Manažerský trenažér: Toxický talent")
    
    st.markdown("""
    <div class='box-red'>
        <strong>🚨 Situace:</strong> Tvůj hlavní grafik Karel je brilantní, ale včera na poradě veřejně zesměšnil juniorního kolegu. Zbytek týmu je naštvaný. Karla potřebuješ kvůli velké zakázce, ale nesmíš ztratit respekt týmu.
    </div>
    <div class='box-blue'>
        <strong>🎯 Tvůj úkol:</strong> Napiš Karlovi zprávu (jako šéf). Musíš mu dát jasnou zpětnou vazbu, zachovat si autoritu, ale nevyprovokovat ho k výpovědi. AI analyzuje tvůj styl a odpoví za Karla.
    </div>
    """, unsafe_allow_html=True)

    if "manazer_chat" not in st.session_state:
        st.session_state["manazer_chat"] = []

    for message in st.session_state["manazer_chat"]:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if prompt := st.chat_input("Napiš zprávu Karlovi... (např. 'Karle, potřebuji s tebou probrat včerejšek...')"):
        with st.chat_message("user"):
            st.write(prompt)
        st.session_state["manazer_chat"].append({"role": "user", "content": prompt})

        with st.chat_message("assistant"):
            with st.spinner("Karel čte tvou zprávu a AI hodnotí tvůj styl..."):
                odpoved_ai = ziskej_odpoved_od_ai(prompt)
                st.write(odpoved_ai)
                
        st.session_state["manazer_chat"].append({"role": "assistant", "content": odpoved_ai})
        
        # Ukládáme výsledek rovnou učiteli do databáze (aby viděl, jak žák konflikt vyřešil)
        if "uloz_odpoved_fn" in st.session_state:
            st.session_state["uloz_odpoved_fn"]("Kapitola 6", "AI Roleplay Trenažér", prompt + "\n\nVýsledek:\n" + odpoved_ai)


def render():
    # =========================================================================
    # 📌 HLAVIČKA KAPITOLY
    # =========================================================================
    st.markdown(
        "<span class='hero-badge'>Kapitola 6</span>", unsafe_allow_html=True
    )
    st.markdown("## 6. Management a marketing")
    st.markdown(
        "<p style='font-size: 1.1rem; color: #64748b; margin-bottom: 1.5rem;'>"
        "Management a marketing nejsou jen poučky z učebnice. Jsou to dovednosti, "
        "které potkáváš každý den: při práci v týmu, plánování školní akce, "
        "sledování influencerů, nákupech v e-shopech, budování profilu na sociálních sítích "
        "i při rozhodování, proč věříš jedné značce víc než druhé.</p>",
        unsafe_allow_html=True,
    )

    # 🧠 POINTA KAPITOLY
    with st.container(border=True):
        st.markdown(
            "<div class='box-blue'>"
            "<strong>🧠 Pointa kapitoly:</strong><br>"
            "Dobrý nápad nestačí. Někdo musí určit směr, sestavit tým, rozdělit práci, "
            "rozhodovat se pod tlakem, pochopit zákazníka a vytvořit nabídku, která dává smysl. "
            "Management řeší, jak věci zorganizovat. Marketing řeší, pro koho tvoříme hodnotu a jak ji komunikujeme."
            "</div>",
            unsafe_allow_html=True,
        )

    # 🎯 CÍLE KAPITOLY (ROZBALOVACÍ)
    with st.expander(
        "🎯 Co máš po této kapitole ovládnout? (Klikni pro rozbalení)",
        expanded=False,
    ):
        st.markdown(
            "- vysvětlit podstatu a základní funkce managementu,\n"
            "- rozlišit manažerské role, dovednosti a styly řízení,\n"
            "- použít SWOT analýzu pro projekt, firmu nebo osobní rozvoj,\n"
            "- vysvětlit podstatu marketingu, výzkumu trhu a zákaznické hodnoty,\n"
            "- použít STP proces: segmentace, targeting, positioning,\n"
            "- sestavit marketingový mix 4P,\n"
            "- vysvětlit význam značky, brand equity a personal brandingu,\n"
            "- rozpoznat vybrané principy nákupní psychologie a dark patterns,\n"
            "- posoudit etiku reklamy, influencer marketingu, greenwashingu a AI reklamy,\n"
            "- navrhnout jednoduchý projekt od řízení týmu až po etickou marketingovou kampaň."
        )

    st.divider()
    
    st.markdown("**🧭 Doporučené pořadí studia:**")
    st.markdown(
        "1. **Management – Jak z chaosu udělat fungující firmu**\n"
        "   Nejdřív pochopíš, jak se z nápadu stává organizovaný projekt: plánování, tým, role, vedení lidí, kontrola, rozhodování a rizika.\n\n"
        "2. **Marketing – Hra o pozornost a marketingový mix**\n"
        "   Potom se zaměříš na zákazníka, trh, data, segmentaci, positioning a 4P: produkt, cenu, distribuci a propagaci.\n\n"
        "3. **Brand, nákupní psychologie a etika**\n"
        "   Nakonec propojíš značku, personal branding, psychologii nákupního chování, dark patterns, greenwashing, regulaci reklamy a odpovědnost firem."
    )

    st.divider()

    # =========================================================================
    # 💡 PRAKTICKÁ LINKA: PROJEKT NAPŘÍČ KAPITOLOU
    # =========================================================================
    st.markdown("## 💡 Projekt napříč kapitolou: Vytvoř si vlastní projekt")
    st.write(
        "**Hlavní praktická linka kapitoly:** Vyber si jeden mikro-projekt a budeš ho postupně rozvíjet ve všech třech blocích. "
        "Na konci kapitoly budeš mít jednoduchý návrh projektu, jeho řízení, marketingový mix, značku a etickou kampaň."
    )

    # Interaktivní výběr a konfigurátor projektu
    with st.container(border=True):
        st.markdown(
            "<div class='box-purple'>🚀 <b>Inkubátor projektů: Zvol si své téma</b></div>",
            unsafe_allow_html=True,
        )

        typ_projektu = st.selectbox(
            "Možné projekty k výběru:",
            [
                "🎒 školní akce nebo festival",
                "🛒 studentský e-shop",
                "👕 značka udržitelného oblečení",
                "☕ lokální kavárna nebo food truck",
                "📱 mobilní aplikace",
                "🌱 nezisková kampaň",
                "💼 osobní brand na LinkedInu nebo sociálních sítích",
                "🎙️ školní podcast, YouTube kanál nebo TikTok profil",
                "✏️ Vlastní nápad (napíšu níže)",
            ],
            key="k6_typ_projektu",
        )

        if "Vlastní nápad" in typ_projektu:
            nazev_projektu = st.text_input(
                "Napiš název a stručný popis svého vlastního projektu:",
                value="Můj nový startup",
                key="k6_custom_nazev",
            )
        else:
            nazev_projektu = typ_projektu.split(" ", 1)[1]

        c_p1, c_p2, c_p3 = st.columns(3)
        c_p1.info(
            "**Blok 1: Management**\n\n**Co doplníš:** Cíl, týmové role, styl řízení, plán a SWOT analýzu.\n\n**Výstup:** Mini manažerský plán."
        )
        c_p2.warning(
            "**Blok 2: Marketing**\n\n**Co doplníš:** Zákazníka, segment, positioning a 4P.\n\n**Výstup:** Marketingový návrh."
        )
        c_p3.success(
            "**Blok 3: Brand & Etika**\n\n**Co doplníš:** Název, hodnoty, personal brand a etická pravidla.\n\n**Výstup:** Etická kampaň."
        )

        st.markdown(
            f"<div style='background-color: #f8fafc; padding: 12px; border-radius: 8px; border: 1px dashed #cbd5e1; text-align: center; margin-top: 10px;'>"
            f"📌 <b>Aktivní projektový pas:</b> <span style='color: #8b5cf6; font-weight: bold;'>{nazev_projektu}</span></div>",
            unsafe_allow_html=True,
        )

        if st.button("Uložit výběr projektu 💾", key="btn_k6_save_project"):
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"](
                    "Kapitola 6",
                    "Inkubátor - Výběr projektu",
                    f"Projekt: {nazev_projektu}",
                )
            st.success(f"Projekt '{nazev_projektu}' byl zaregistrován!")

    st.divider()

    # =========================================================================
    # 📌 VÝRAZNÝ NAVIGAČNÍ PANEL
    # =========================================================================
    st.markdown(
        """
        <div style='background-color: #f0fdf4; padding: 20px; border-radius: 10px; border-left: 6px solid #16a34a; margin-bottom: 20px;'>
            <h3 style='margin-top: 0; color: #166534; margin-bottom: 5px;'>🧭 Navigace kapitolou</h3>
            <p style='margin-bottom: 0px; color: #14532d;'>Vyber si v roletce podkapitolu, kterou chceš právě studovat:</p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    section_options_6 = [
        "1.1 Management: Podstata a role",
        "1.2 Základní manažerské funkce",
        "1.3 Osobnost manažera a role",
        "1.4 Styly řízení a řešení konfliktů",
        "1.5 Organizační struktury firem",
        "1.6 Rozhodování a analytické metody",
        "1.7 Moderní přesah: Agilní řízení, remote work",
        "2.1 Marketing: Podstata a vývoj",
        "2.2 Marketingový výzkum a analýza trhu",
        "2.3 STP proces: Segmentace, Cílení, Positioning",
        "2.4 Marketingový mix: Klasické 4P",
        "3.1 Značka a budování brandu",
        "3.2 Nákupní chování a psychologie spotřebitele",
        "3.3 Etika, právo a ochrana spotřebitele",
        "3.4 Moderní formy a trendy v digitálním marketingu",
        "4. Závěrečný výstup a případové studie"
    ]

    selected_section_6 = st.selectbox(
        "Vyber podkapitolu:",
        section_options_6,
        index=0,
        label_visibility="collapsed",
        key="k6_section_select",
    )

    idx = section_options_6.index(selected_section_6)

    st.divider()

    # =========================================================================
    # BLOK 0: 1.1 Management: Podstata a role
    # =========================================================================
    if idx == 0:
        st.markdown("## 1. Management – Jak z chaosu udělat fungující firmu")

        st.markdown(
            "<div class='box-blue'>"
            "🏗️ <b>Moderní hook:</b> <i>„Boss vs. Leader: Proč už nikdo nechce pracovat pro šéfa z minulého století?“</i><br>"
            "Management není o komandování a razítkování papírů. Je to schopnost určit směr, nadchnout a vést tým, férově rozdělit práci, řešit konflikty, rozhodovat se v nejistotě a udržet projekt při životě."
            "</div>",
            unsafe_allow_html=True,
        )

        st.markdown(
            "<div class='box-green'>"
            "🎯 <b>Cíl 1. bloku:</b> Pochopíš, jak se z nápadu stává funkční organizace nebo projekt. Naučíš se rozlišit základní funkce managementu, styly řízení, manažerské role, organizační struktury a praktické nástroje pro rozhodování."
            "</div>",
            unsafe_allow_html=True,
        )

        st.markdown("### 1.1 Podstata a význam managementu")
        st.write(
            "Management znamená **řízení organizace nebo projektu tak, aby bylo dosaženo stanovených cílů**. Často se říká, že management je *proces dosahování cílů prostřednictvím činnosti jiných lidí*. Manažer tedy nemusí dělat všechno sám – jeho úkolem je nastavit směr, rozdělit práci, motivovat tým, rozhodovat a kontrolovat výsledek."
        )

        st.markdown(
            "<div class='box-yellow'>"
            "🧠 <b>Jednoduše:</b> Management je schopnost proměnit chaos v plán, plán v konkrétní úkoly a úkoly v reálný výsledek."
            "</div>",
            unsafe_allow_html=True,
        )

        st.write(
            "Management se objevuje všude, kde lidé spolupracují: ve firmě, škole, neziskovce, sportovním týmu, startupu, nemocnici, restauraci i při organizaci studentského plesu. Čím složitější je projekt, tím důležitější je řízení času, lidí, peněz, informací a rizik."
        )

        st.markdown("#### 👥 Kdo je kdo v ekonomickém světě? (Rozlišení rolí)")
        st.markdown(
            "| Role | Co znamená | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Manažer** | Řídí lidi, procesy nebo část organizace. Odpovídá za dosažení cílů. | Vedoucí týmu, ředitel školy, manažer pobočky, projektový manažer. |\n"
            "| **Podnikatel** | Přichází s podnikatelským nápadem, nese riziko a snaží se vytvořit hodnotu na trhu. | Zakladatel e-shopu, majitel kavárny, startupový founder. |\n"
            "| **Vlastník** | Vlastní firmu nebo její část. Nemusí ji každodenně řídit. | Společník v s.r.o., akcionář, investor. |\n"
            "| **Zaměstnanec** | Vykonává práci podle pracovní smlouvy nebo dohody a dostává za ni odměnu. | Prodavač, účetní, grafik, pracovník ve výrobě, brigádník. |"
        )
        st.write("**Důležité rozlišení:** Jeden člověk může mít více rolí najednou. Zakladatel startupu může být zároveň podnikatel, vlastník i manažer. Investor může být vlastník, ale nemusí firmu řídit. Zaměstnanec může vést tým, a tedy být manažerem, i když firmu nevlastní.")

        st.markdown(
            "<div class='box-purple'>🕹️ <b>Trenažér rolí: Poznáš, kdo je kdo?</b></div>",
            unsafe_allow_html=True,
        )
        with st.container(border=True):
            st.write("👤 **Příběh:** *Sára založila vlastní značku udržitelné kosmetiky, investovala do ní své úspory (vlastní 100 % firmy) a zároveň sama řídí tým 5 vývojářů a markeťáků.* Jaké všechny role Sára v tuto chvíli má?")
            sara_role = st.radio(
                "Vyber správnou odpověď:",
                [
                    "Vyber odpověď...",
                    "A) Je pouze zaměstnankyní své vlastní firmy.",
                    "B) Je zároveň Podnikatelka, Vlastník i Manažerka.",
                    "C) Je pouze Podnikatelka, řízení lidí pod ni nespadá.",
                ],
                key="k6_1_sara_role",
            )
            if st.button("Uložit vyhodnocení rolí 💾", key="btn_k6_1_sara"):
                if "B)" in sara_role:
                    st.success("✅ **Přesně tak!** Sára přišla s nápadem (Podnikatelka), dala do toho peníze a vlastní firmu (Vlastník) a zároveň denně vede tým k cílům (Manažerka).")
                else:
                    st.error("❌ Kdepak! Sára v sobě kombinuje všechny 3 role. Správná odpověď je B.")
                if "uloz_odpoved_fn" in st.session_state and sara_role != "Vyber odpověď...":
                    st.session_state["uloz_odpoved_fn"]("Kapitola 6", "Podkapitola 1.1 - Trenažér rolí", sara_role[:30])

        st.markdown("#### 1.1.1 Úrovně managementu: pyramida řízení")
        st.write("Ve větších organizacích existují různé úrovně řízení. Každá řeší jiný typ rozhodnutí.")

        st.markdown(
            "| Úroveň managementu | Co řeší | Příklad | Typická otázka |\n"
            "| :--- | :--- | :--- | :--- |\n"
            "| **Vrcholový management / Top management** | Dlouhodobý směr, strategii, zásadní rozhodnutí, odpovědnost za celou organizaci. | CEO, generální ředitel, ředitel školy, představenstvo. | Kam má organizace směřovat za 3–5 let? |\n"
            "| **Střední management / Middle management** | Převádí strategii do plánů oddělení, koordinuje týmy a kontroluje výsledky. | Vedoucí marketingu, vedoucí výroby, manažer závodu, zástupce ředitele. | Jak splníme cíle v našem oddělení? |\n"
            "| **Liniový management / First-line management** | Řídí každodenní práci lidí v provozu nebo konkrétním týmu. | Mistr ve výrobě, vedoucí směny, team leader, vedoucí brigádníků. | Kdo dnes co udělá a jak poznáme, že je práce hotová? |"
        )
        st.write("**Příklad ze školní akce:** Vrcholový tým rozhodne, že škola uspořádá benefiční festival. Střední manažeři řeší program, rozpočet, propagaci a partnery. Linioví vedoucí organizují konkrétní směny u vstupu, občerstvení, techniky nebo úklidu.")

        st.markdown(
            "<br><div class='box-purple'>🎪 <b>Simulátor pyramidy: Školní benefiční festival</b></div>",
            unsafe_allow_html=True,
        )
        st.write("Klikni na úroveň řízení a podívej se, jak se rozhodování projevuje na reálném projektu:")
        uroven_sim = st.radio(
            "Vyber úroveň řízení pro školní festival:",
            [
                "🔴 Top management (Ředitel školy + Hlavní koordinátor)",
                "🟡 Middle management (Vedoucí kapel, Vedoucí občerstvení, Vedoucí PR)",
                "🟢 First-line management (Team leader u vstupu / u stánku s pitím)",
            ],
            key="k6_1_1_sim_uroven",
        )
        if "Top" in uroven_sim:
            st.error("🏛️ **Rozhodnutí Top managementu:** 'Schvalujeme konání festivalu na 20. června. Cílem je vybrat 100 000 Kč na útulek a získat pro školu skvělé jméno. Schvalujeme celkový rozpočet 50 000 Kč.'")
        elif "Middle" in uroven_sim:
            st.warning("📊 **Rozhodnutí Middle managementu:** 'Sestavili jsme harmonogram vystoupení 5 kapel. Vedoucí PR zajistí plakáty na Instagramu, vedoucí občerstvení domluvil sponzora na nápoje.'")
        else:
            st.success("🛠️ **Rozhodnutí First-line managementu:** 'Ahoj týme! Jirka bude od 14:00 trhat lístky u brány, Terka bude prodávat párečky v rohlíku. Zkontrolujte si, že máte dost drobných na vrácení!'")

        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 1: Rozdělení rolí v tvém projektu</b></div>",
            unsafe_allow_html=True,
        )
        st.write("Vrať se ke svému projektu zvolenému v úvodu kapitoly a nastav pro něj základní řídící strukturu:")
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"]("6.1.1", "1. Kdo bude v tvém projektu zastávat roli Top managementu (vize a strategie)?", "6", st.session_state.get("ulozene_odpovedi", {}))
            st.session_state["vykresli_otazku_fn"]("6.1.2", "2. Jaká oddělení / Middle management budeš v projektu potřebovat?", "6", st.session_state.get("ulozene_odpovedi", {}))
            st.session_state["vykresli_otazku_fn"]("6.1.3", "3. Jaké hlavní úkoly bude muset řešit liniový management v běžném dni?", "6", st.session_state.get("ulozene_odpovedi", {}))

    # =========================================================================
    # BLOK 1: 1.2 Základní manažerské funkce
    # =========================================================================
    elif idx == 1:
        st.markdown("## 1. Management – Jak z chaosu udělat fungující firmu")
        
        st.markdown("### 1.2 Základní manažerské funkce: proces řízení")
        st.write("Manažerská práce se často popisuje jako soubor čtyř navazujících funkcí: plánování, organizování, vedení lidí a kontrola. Nejde o jednorázové kroky, ale o cyklus. Manažer plánuje, rozdělí práci, vede tým, kontroluje výsledek a podle zjištění plán upravuje.")

        st.markdown(
            "| Funkce | Co znamená | Otázka pro manažera |\n"
            "| :--- | :--- | :--- |\n"
            "| **Plánování** | Stanovení cílů a cest, jak jich dosáhnout. | Čeho chceme dosáhnout a jak se tam dostaneme? |\n"
            "| **Organizování** | Rozdělení práce, pravomocí, odpovědnosti a zdrojů. | Kdo co udělá, s čím a do kdy? |\n"
            "| **Vedení lidí** | Motivace, komunikace, koordinace a řešení konfliktů. | Jak zajistíme, aby tým chtěl a mohl dobře pracovat? |\n"
            "| **Kontrola** | Měření výsledků, porovnání s plánem a nápravná opatření. | Splnili jsme cíl? Pokud ne, co změníme? |"
        )

        col_fnc1, col_fce2, col_fce3, col_fce4 = st.columns(4)
        col_fnc1.info("🎯 **1. Plánování**\nStanovení cílů a cest.\n*(Kam jdeme?)*")
        col_fce2.warning("🏗️ **2. Organizování**\nRozdělení práce a úkolů.\n*(Kdo co udělá?)*")
        col_fce3.success("💬 **3. Vedení lidí**\nMotivace a komunikace.\n*(Jak je nadchnout?)*")
        col_fce4.error("🔍 **4. Kontrola**\nMěření výsledků.\n*(Splnili jsme to?)*")

        st.markdown("#### 1.2.1 Plánování")
        st.write("Plánování znamená určit, čeho chce organizace dosáhnout, proč je to důležité a jakými kroky se k cíli dostane. Bez plánování tým často jen „hasí požáry“ a reaguje na problémy, místo aby měl jasný směr.")
        st.write("Podle časového hlediska rozlišujeme:")
        
        st.markdown(
            "| Typ plánování | Časový horizont | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Krátkodobé / operativní** | Dny, týdny, nejbližší měsíce. | Rozpis směn, plán příspěvků na sociální sítě na příští týden. |\n"
            "| **Střednědobé / taktické** | Měsíce až zhruba 1–2 roky. | Plán kampaně na pololetí, rozvoj nového produktu, nábor týmu. |\n"
            "| **Dlouhodobé / strategické** | Několik let. | Vstup na nový trh, změna značky, digitalizace firmy, dlouhodobý růst školy nebo organizace. |"
        )

        st.markdown(
            "<div class='box-purple'>🎯 <b>Trenažér: Vylaď cíl podle pravidla S.M.A.R.T.</b></div>",
            unsafe_allow_html=True,
        )
        st.write("Vágně zadaný cíl (*'Chceme prodávat hodně mikin'*) vedoucího i tým zmate. Správný cíl musí být **S.M.A.R.T.**:")
        st.markdown(
            "* **S – Specific:** konkrétní,\n"
            "* **M – Measurable:** měřitelný,\n"
            "* **A – Achievable:** dosažitelný,\n"
            "* **R – Realistic:** realistický vzhledem ke zdrojům,\n"
            "* **T – Time-bound:** časově ohraničený."
        )

        with st.container(border=True):
            st.caption("🔴 *Příklad špatného cíle:* „Chceme mít úspěšný školní merch.“")
            c_smart1, c_smart2, c_smart3 = st.columns(3)
            s_ks = c_smart1.number_input("Kolik kusů prodáme?:", min_value=10, value=80, step=10, key="k6_1_2_ks")
            s_marze = c_smart2.number_input("Minimální marže (Kč):", min_value=50, value=120, step=10, key="k6_1_2_marze")
            s_termin = c_smart3.date_input("Termín dokončení akce:", key="k6_1_2_termin")

            smart_text = f"Do {s_termin.strftime('%d. %m. %Y')} prodáme alespoň {s_ks} kusů mikin studentům 2.–4. ročníku s minimální marží {s_marze} Kč na kus."
            st.success(f"🟢 **Tvůj vygenerovaný SMART cíl:** *„{smart_text}“*")

        st.markdown("#### 1.2.2 Organizování")
        st.write("Organizování znamená vytvořit strukturu, ve které lidé vědí, co mají dělat, kdo o čem rozhoduje, kdo komu předává informace a kdo za co odpovídá.")
        st.markdown(
            "Manažer při organizování řeší hlavně:\n"
            "* dělení práce,\n"
            "* přidělení úkolů,\n"
            "* přidělení pravomocí,\n"
            "* stanovení odpovědnosti,\n"
            "* koordinaci mezi lidmi a týmy,\n"
            "* nastavení pravidel komunikace."
        )
        
        st.markdown(
            "<div class='box-yellow'>"
            "⚖️ <b>Pravomoc vs. odpovědnost:</b><br>"
            "• <b>Pravomoc</b> znamená právo rozhodovat nebo zadávat úkoly.<br>"
            "• <b>Odpovědnost</b> znamená povinnost nést důsledky za výsledek.<br>"
            "<i>Problém vzniká, když má člověk odpovědnost, ale nemá dostatečnou pravomoc — například má zařídit akci, ale nesmí rozhodnout o rozpočtu.</i>"
            "</div>",
            unsafe_allow_html=True,
        )

        st.markdown("#### 1.2.3 Vedení lidí")
        st.write("Vedení lidí znamená ovlivňovat tým tak, aby lidé rozuměli cíli, chtěli na něm pracovat a měli podmínky k dobrému výkonu. Dobrý manažer neřeší jen úkoly, ale také motivaci, komunikaci, atmosféru a konflikty.")
        
        st.markdown(
            "| Pojem | Co znamená | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Motivace** | Vnitřní důvod, proč člověk něco dělá. | Student chce vést tým, protože ho baví organizovat akce a učit se leadership. |\n"
            "| **Stimulace** | Vnější podnět nebo odměna, která podporuje určité chování. | Odměna, bonus, pochvala, certifikát, volno, soutěž. |"
        )

        st.markdown("#### 1.2.3.1 Maslowova pyramida potřeb")
        st.write(
            "Abraham Harold Maslow byl americký psycholog 20. století, který patří mezi představitele humanistické psychologie. "
            "Zabýval se tím, co lidi motivuje, jaké mají potřeby a proč člověk neusiluje jen o peníze nebo přežití, ale také o vztahy, uznání, smysl a osobní rozvoj."
        )
        st.write("**Maslowova pyramida potřeb:** Maslow popsal lidské potřeby jako hierarchii. Člověk obvykle nejdřív řeší základní potřeby a teprve potom se může plně soustředit na vyšší potřeby.")
        st.markdown(
            "1. **Fyziologické potřeby** — jídlo, pití, spánek, odpočinek.\n"
            "2. **Potřeba bezpečí** — jistota, stabilita, safe pracovní prostředí.\n"
            "3. **Sociální potřeby** — vztahy, tým, přijetí, spolupráce.\n"
            "4. **Uznání** — respekt, ocenění, status, pocit užitečnosti.\n"
            "5. **Seberealizace** — rozvoj talentu, smysluplná práce, kreativita, růst."
        )

        úrovně_maslow = [
            "5. Seberealizace",
            "4. Uznání a respekt",
            "3. Sociální potřeby (Tým)",
            "2. Bezpečí a jistota",
            "1. Fyziologické potřeby",
        ]
        sirky_maslow = [20, 40, 60, 80, 100]

        fig_maslow = go.Figure(
            go.Funnel(
                y=úrovně_maslow,
                x=sirky_maslow,
                textinfo="label",
                marker={"color": ["#8b5cf6", "#3b82f6", "#10b981", "#f59e0b", "#ef4444"]},
            )
        )
        fig_maslow.update_layout(title="Maslowova pyramida potřeb", height=350, margin=dict(t=40, b=10, l=10, r=10), showlegend=False)
        st.plotly_chart(fig_maslow, use_container_width=True)

        st.write("**V managementu:** Maslowova pyramida pomáhá pochopit, že lidé nepracují jen kvůli výplatě. Pokud se zaměstnanec bojí o místo, je přetížený nebo se v týmu necítí bezpečně, těžko bude kreativní a motivovaný. Dobrý manažer proto řeší nejen výkon, ale i bezpečí, vztahy, uznání a prostor pro rozvoj.")
        st.write("**Komunikace v týmu:** Manažer musí umět vysvětlit zadání, poslouchat zpětnou vazbu, řešit nedorozumění a pojmenovat problém dřív, než přeroste v konflikt. V digitálních týmech je důležité domluvit, co patří do chatu, co do úkolovníku a co už vyžaduje schůzku.")

        wybrana_uroven = st.selectbox(
            "🔍 Vyber úroveň pyramidy a podívej se, jak ji řeší dobrý manažer:",
            [
                "1. Fyziologické potřeby (Základ)",
                "2. Potřeba bezpečí (Jistota)",
                "3. Sociální potřeby (Vztahy v týmu)",
                "4. Uznání a respekt (Ocenění)",
                "5. Seberealizace (Růst a smysl)",
            ],
            key="k6_1_2_maslow_select",
        )

        if "1." in wybrana_uroven:
            st.error("🍎 **1. Fyziologické potřeby:** Důstojný plat, pitný režim, přestávka na oběd a bezpečné prostředí.")
        elif "2." in wybrana_uroven:
            st.warning("🛡️ **2. Potřeba bezpečí:** Stabilní smlouva, bezpečné pracoviště bez šikany, jasná pravidla.")
        elif "3." in wybrana_uroven:
            st.success("🤝 **3. Sociální potřeby:** Přijetí do týmu, dobrá atmosféra, neformální teambuildingy.")
        elif "4." in wybrana_uroven:
            st.info("🏆 **4. Uznání a respekt:** Pochvala před týmem za dobře odvedenou práci, povýšení, ocenění.")
        else:
            st.success("🚀 **5. Seberealizace:** Svoboda v tvoření, smysluplná práce, možnost učit se nové věci.")

        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 2: SMART cíl a motivace týmu</b></div>",
            unsafe_allow_html=True,
        )

        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"]("6.1.4", "1. Napiš přesný S.M.A.R.T. cíl pro svůj projekt (Co, kolik, do kdy):", "6", st.session_state.get("ulozene_odpovedi", {}))
            st.session_state["vykresli_otazku_fn"]("6.1.5", "2. Jak budeš svůj tým motivovat (kromě peněz) na úrovni Uznání a Seberealizace?", "6", st.session_state.get("ulozene_odpovedi", {}))

        st.markdown("#### 1.2.4 Kontrola")
        st.write("Kontrola neznamená jen „nachytat někoho při chybě“. Jejím smyslem je zjistit, zda se realita shoduje s plánem, a pokud ne, přijmout nápravná opatření.")
        
        st.markdown(
            "| Fáze kontroly | Co se děje |\n"
            "| :--- | :--- |\n"
            "| **1. Stanovení standardů** | Určíme, jak má vypadat dobrý výsledek. |\n"
            "| **2. Zjištění skutečnosti** | Změříme, co se opravdu stalo. |\n"
            "| **3. Srovnání** | Porovnáme plán a realitu. |\n"
            "| **4. Nápravná opatření** | Rozhodneme, co upravit. |"
        )
        
        st.markdown(
            "| Typ kontroly | Kdy probíhá | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Předběžná kontrola** | Před zahájením činnosti. | Kontrola rozpočtu, smluv, techniky a povolení před akcí. |\n"
            "| **Průběžná kontrola** | Během činnosti. | Sledování prodeje vstupenek, docházky týmu nebo plnění úkolů v Notionu. |\n"
            "| **Následná kontrola** | Po skončení činnosti. | Vyhodnocení zisku, spokojenosti účastníků a chyb po festivalu. |"
        )

        col_kont1, col_kont2 = st.columns([1, 1])
        with col_kont1:
            st.markdown(
                "<div style=\"background-color: #f8fafc; padding: 15px; border-left: 5px solid #3b82f6; border-radius: 4px;\">"
                "<h5 style=\"margin-top:0; color: #1e40af;\">🔍 4 fáze kontrolního procesu</h5>"
                "1. <b>Stanovení standardů</b> - určíme, jak má vypadat dobrý výsledek.<br>"
                "2. <b>Zjištění skutečnosti</b> - změříme, co se opravdu stalo.<br>"
                "3. <b>Srovnání plánu a reality</b> - porovnáme plán a realitu.<br>"
                "4. <b>Nápravné opatření</b> - rozhodneme, co upravit."
                "</div>",
                unsafe_allow_html=True,
            )

        with col_kont2:
            st.markdown("##### ⏱️ Typy kontroly podle času")
            tab_k1, tab_k2, tab_k3 = st.tabs(["🔮 Předběžná", "⚙️ Průběžná", "🏁 Následná"])
            with tab_k1:
                st.info("**Předběžná (PŘED):** Kontrola rozpočtu, schválení vzorků před tiskem.")
            with tab_k2:
                st.warning("**Průběžná (BĚHEM):** Sledování denních prodejů v e-shopu, Trello nástěnka.")
            with tab_k3:
                st.success("**Následná (PO):** Vyhodnocení zisku a zpětná vazba po akci.")

    # =========================================================================
    # BLOK 3: 1.3 Osobnost manažera a 1.4 Styly řízení
    # =========================================================================
    elif idx == 2:
        st.markdown("## 1. Management – Jak z chaosu udělat fungující firmu")
        
        st.markdown("### 1.3 Osobnost manažera a role")
        st.write("Manažer potřebuje kombinaci odbornosti, práce s lidmi a schopnosti vidět celek. Jinak bude působit v malé kavárně, jinak ve škole, jinak ve výrobní firmě a jinak ve startupu. Základní dovednosti se ale opakují.")
        
        st.markdown(
            "| Dovednost manažera | Co znamená | Kdy je nejvíc potřeba |\n"
            "| :--- | :--- | :--- |\n"
            "| **Koncepční dovednosti** | Schopnost vidět organizaci jako celek, chápat souvislosti a přemýšlet strategicky. | Hlavně u vrcholového managementu. |\n"
            "| **Lidské / interpersonální dovednosti** | Komunikace, empatie, vedení lidí, vyjednávání, řešení konfliktů. | Na všech úrovních managementu. |\n"
            "| **Technické / odborné dovednosti** | Znalost oboru, procesů, nástrojů a konkrétní práce týmu. | Hlavně u liniového a středního managementu. |"
        )
        
        st.write("**Moderní pohled:** Dobrý manažer nemusí být největší expert na všechno. Musí ale rozumět práci týmu natolik, aby dokázal dobře rozhodovat, klást správné otázky a nepřekážet lidem, kteří jsou v konkrétní odbornosti silnější.")

        fig_skills = go.Figure()
        fig_skills.add_trace(go.Bar(y=["Top", "Middle", "First-line"], x=[50, 25, 10], name="Koncepční", orientation="h", marker_color="#8b5cf6"))
        fig_skills.add_trace(go.Bar(y=["Top", "Middle", "First-line"], x=[40, 50, 40], name="Lidské", orientation="h", marker_color="#3b82f6"))
        fig_skills.add_trace(go.Bar(y=["Top", "Middle", "First-line"], x=[10, 25, 50], name="Technické", orientation="h", marker_color="#10b981"))
        fig_skills.update_layout(barmode="stack", title="Poměr manažerských dovedností (%)", height=250, margin=dict(t=30, b=20, l=10, r=10))
        st.plotly_chart(fig_skills, use_container_width=True)

        st.markdown("#### 1.3.1 Role manažera podle Mintzberga")
        st.write("Henry Mintzberg popsal manažerskou práci jako soubor rolí. Manažer během dne často přepíná mezi reprezentací firmy, vedením lidí, sběrem informací, komunikací a rozhodováním.")
        
        st.markdown(
            "| Skupina rolí | Co zahrnuje | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Interpersonální role** | Reprezentant a lídr. Manažer vystupuje jménem organizace a vede lidi. | Ředitel reprezentuje školu na veřejnosti, team leader vede poradu. |\n"
            "| **Informační role** | Sleduje informace, vybírá podstatné zprávy a předává je dál. | Manažer předá týmu změny v harmonogramu nebo výsledky prodeje. |\n"
            "| **Rozhodovací role** | Rozhoduje o změnách, řeší krize, rozděluje zdroje a vyjednává. | Rozhodne, co se škrtne z rozpočtu, když dodavatel zdraží techniku. |"
        )

        situace_mintz = st.selectbox(
            "Vyber situaci ze dne manažera:",
            [
                "1. Vybíráš, kterým 3 projektům z deseti přidělíš peníze z rozpočtu.",
                "2. Novinář se ptá na oficiální stanovisko vaší firmy.",
                "3. Vypadly servery a musíte okamžitě sehnat náhradní řešení.",
                "4. Jdeš na kávu se zakladatelem partnerké firmy zjistit novinky z trhu.",
            ],
            key="k6_1_3_mintz_select",
        )

        if "1." in situace_mintz:
            st.info("🎯 **Alokátor zdrojů** (rozhodovací role).")
        elif "2." in situace_mintz:
            st.info("📢 **Mluvčí** (informační role).")
        elif "3." in situace_mintz:
            st.error("🚨 **Hasič krizí** (rozhodovací role).")
        else:
            st.success("🔎 **Monitor & Spojovatel** (informační/interpersonální role).")

    elif idx == 3:
        st.markdown("## 1. Management – Jak z chaosu udělat fungující firmu")
        
        st.markdown("### 1.4 Styly řízení a řešení konfliktů")
        st.write("Styl řízení ukazuje, jak manažer pracuje s mocí, odpovědností a zapojením týmu. Neexistuje jeden styl, který by byl nejlepší vždy. Záleží na situaci, zkušenosti týmu, času, riziku a typu úkolu.")

        st.markdown(
            "| Styl řízení | Jak funguje | Výhody | Rizika |\n"
            "| :--- | :--- | :--- | :--- |\n"
            "| **Autoritativní / autokratický** | Manažer rozhoduje sám, dává jasné pokyny a očekává jejich splnění. | Rychlost, jasná odpovědnost, vhodné v krizích nebo při nízké zkušenosti týmu. | Nižší motivace, strach z chyb, málo nápadů od týmu, riziko toxické kultury. |\n"
            "| **Demokratický / participativní** | Manažer zapojuje tým do rozhodování, podporuje diskusi a deleguje pravomoci. | Vyšší motivace, lepší nápady, větší odpovědnost týmu. | Pomalejší rozhodování, riziko dlouhých debat, nemusí fungovat v akutní krizi. |\n"
            "| **Liberální / laissez-faire** | Manažer nechává týmu velkou volnost a zasahuje minimálně. | Podporuje samostatnost, kreativitu a odpovědnost zkušených lidí. | Chaos, nejasné priority, slabá kontrola, problémy u nezkušeného týmu. |"
        )

        st.write("**Boss vs. leader: v čem je rozdíl?**")
        st.write("„Boss“ často stojí na příkazech, kontrole a formální autoritě. „Leader“ umí vysvětlit smysl práce, získat důvěru, rozvíjet lidi a nést odpovědnost. V praxi dobrý manažer někdy musí rozhodnout tvrdě a rychle, ale dlouhodobě nemůže tým řídit jen strachem.")
        
        st.write("**Debata:** Je lepší autoritativní Elon Musk, nebo demokratická firemní kultura typu Google / Spotify? V jaké situaci může být každý styl užitečný a kdy začne škodit?")

        with st.form("debata_musk_form"):
            st.write("**Která filozofie řízení je ti bližší a proč?**")
            postoj_styl = st.radio(
                "Vyber svůj postoj:",
                [
                    "🚀 Dávám přednost autoritativnímu vizionáři (Musk): Bez tvrdé ruky a vysokých nároků nevzniknou revoluční věci.",
                    "🎧 Dávám přednost demokratické/svobodné kultuře (Spotify/Google): Nejlepší inovace vznikají v prostředí svobody a bezpečí.",
                    "⚖️ Záleží na situaci (Situační řízení): V krizích autoritativní, při vývoji demokratický.",
                ],
                key="k6_1_4_postoj",
            )
            if st.form_submit_button("Odeslat a uložit názor 💾"):
                st.success("Tvůj postoj byl zaznamenán!")
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"]("Kapitola 6", "Podkapitola 1.4 - Debata Styl řízení", postoj_styl[:30])

        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 3: Styl řízení a kontrolní mechanizmus</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"]("6.1.6", "1. Jaký styl řízení zvolíš pro svůj projekt a proč?", "6", st.session_state.get("ulozene_odpovedi", {}))
            st.session_state["vykresli_otazku_fn"]("6.1.7", "2. Jak nastavíš PŘEDBĚŽNOU kontrolu pro svůj projekt?", "6", st.session_state.get("ulozene_odpovedi", {}))

        # -------------------------------------------------------------
        # AI TRENAŽÉR PŘESNĚ ZA STYLY ŘÍZENÍ
        # -------------------------------------------------------------
        st.divider()
        st.markdown("#### 1.4.1 Řešení konfliktů a Soft-skills")
        st.write("Manažer tráví většinu času řešením problémů s lidmi, ne papírováním. Komunikace, empatie a schopnost zvládat krizové situace (soft-skills) jsou často důležitější než technické znalosti.")

        render_ai_treenazer()


    # =========================================================================
    # BLOK 4: 1.5 Organizační struktury firem
    # =========================================================================
    elif idx == 4:
        st.markdown("## 1. Management – Jak z chaosu udělat fungující firmu")
        
        st.markdown("### 1.5 Organizační struktury firem")
        st.write("Organizační struktura je způsob, jakým je firma nebo instituce vnitřně uspořádána. Ukazuje, kdo komu odpovídá, jak jsou rozdělené útvary, kudy tečou informace a kdo má pravomoc rozhodovat.")
        st.write("**Jednoduše:** Organizační struktura je mapa firmy. Pomáhá lidem pochopit, kde jsou jejich role, kdo rozhoduje, s kým spolupracují a na koho se obrátit.")

        st.markdown("#### 1.5.1 Formální a neformální struktura")
        st.markdown(
            "| Typ struktury | Co znamená | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Formální struktura** | Oficiálně dané vztahy, pozice, pravomoci a odpovědnosti. | Organigram školy, popis pracovních pozic, vedoucí oddělení. |\n"
            "| **Neformální struktura** | Přirozené vztahy, vliv a neoficiální autority mezi lidmi. | Člověk, za kterým všichni chodí pro radu, i když není vedoucí. |"
        )
        st.write("**Reality check:** Neformální autorita může týmu hodně pomoct, když podporuje spolupráci. Může ale i škodit, pokud šíří odpor, pomluvy nebo sabotuje změny.")

        st.markdown("#### 1.5.2 Základní typy organizačních struktur")
        st.markdown(
            "| Typ struktury | Jak funguje | Výhoda | Riziko |\n"
            "| :--- | :--- | :--- | :--- |\n"
            "| **Liniová** | Jasná hierarchie: jeden podřízený má jednoho přímého nadřízeného. | Přehlednost, jasné pravomoci a odpovědnost. | Může být nepružná a závislá na rozhodnutí shora. |\n"
            "| **Štábní / liniově-štábní** | Linioví vedoucí rozhodují, ale pomáhají jim odborné poradní útvary. | Manažer má odbornou podporu například v právu, HR nebo financích. | Štáb radí, ale nemusí nést přímou odpovědnost za realizaci. |\n"
            "| **Funkcionální** | Firma je členěná podle odborných funkcí: marketing, finance, výroba, HR, IT. | Specializace a odbornost jednotlivých oddělení. | Oddělení mohou pracovat v „silech“ a málo spolu komunikovat. |\n"
            "| **Maticová** | Kombinuje funkční řízení a projektové týmy. Člověk může mít dva nadřízené. | Vhodná pro projekty, inovace a spolupráci napříč firmou. | Dvojí podřízenost může vést ke konfliktům priorit. |"
        )
        st.write("**Maticová struktura na školním projektu:** Student může patřit do „marketingového týmu“, ale zároveň pracovat na konkrétní akci jako člen projektového týmu festivalu. Funkční vedoucí řeší kvalitu marketingu, projektový vedoucí řeší termíny festivalu. Výhoda je spolupráce napříč obory, riziko je zmatek v tom, kdo má poslední slovo.")

        st.markdown("#### 1.5.3 Rozpětí řízení")
        st.write("Rozpětí řízení znamená, kolik podřízených přímo připadá na jednoho vedoucího.")
        st.markdown(
            "| Typ rozpětí | Jak vypadá | Výhody | Rizika |\n"
            "| :--- | :--- | :--- |\n"
            "| **Úzké rozpětí řízení** | Vedoucí má málo přímých podřízených, organizace má více úrovní. | Více kontroly, bližší vedení, vhodné pro složité nebo rizikové úkoly. | Více hierarchie, pomalejší komunikace, vyšší náklady. |\n"
            "| **Široké rozpětí řízení** | Vedoucí má hodně přímých podřízených, organizace má méně úrovní. | Rychlejší komunikace, větší samostatnost, plošší struktura. | Manažer nemusí stíhat podporu a kontrolu všech lidí. |"
        )

        pocet_podrizenych = st.slider("Počet lidí, které přímo řídíš (Rozpětí řízení):", min_value=2, max_value=25, value=5, step=1, key="k6_1_5_rozpeti")
        if pocet_podrizenych <= 6:
            st.info(f"📏 Úzké rozpětí řízení ({pocet_podrizenych} lidí). Vysoká kontrola, vyšší náklady.")
        elif 7 <= pocet_podrizenych <= 12:
            st.success(f"⚖️ Vyvážené rozpětí řízení ({pocet_podrizenych} lidí). Ideální rovnováha.")
        else:
            st.warning(f"📐 Široké rozpětí řízení ({pocet_podrizenych} lidí). Plochá struktura, riziko chaosu.")

        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 4: Organizační mapa tvého projektu</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"]("6.1.8", "1. Jaký typ organizační struktury se nejlépe hodí pro tvůj projekt a jaké zvolíš rozpětí řízení?", "6", st.session_state.get("ulozene_odpovedi", {}))

    # =========================================================================
    # BLOK 5: 1.6 Rozhodování a 1.7 Moderní přesah
    # =========================================================================
    elif idx == 5:
        st.markdown("## 1. Management – Jak z chaosu udělat fungující firmu")
        
        st.markdown("### 1.6 Rozhodování a analytické metody")
        st.write("Manažer se neustále rozhoduje: koho přijmout do týmu, jak rozdělit rozpočet, co udělat při zpoždění, jak reagovat na konkurenci nebo jak řešit konflikt. Dobré rozhodování není jen pocit. Opírá se o informace, varianty a vyhodnocení důsledků.")
        
        st.markdown("""
        **Rozhodovací proces:**
        1. **Identifikace problému** — co přesně řešíme?
        2. **Sběr informací** — co víme a co ještě potřebujeme zjistit?
        3. **Návrh variant** — jaká řešení připadají v úvahu?
        4. **Výběr nejvhodnější varianty** — která možnost nejlépe odpovídá cíli, zdrojům a rizikům?
        5. **Realizace a kontrola** — provedeme rozhodnutí a sledujeme výsledek.
        """)

        st.markdown("#### 1.6.1 SWOT analýza")
        st.write("SWOT analýza je jednoduchý nástroj, který pomáhá posoudit situaci firmy, projektu, produktu nebo člověka. Rozlišuje vnitřní a vnější prostředí.")
        st.markdown(
            "| Část SWOT | Prostředí | Co znamená | Otázka |\n"
            "| :--- | :--- | :--- | :--- |\n"
            "| **S — Strengths / Silné stránky** | Vnitřní prostředí | V čem jsme dobří a o co se můžeme opřít. | Co nám jde lépe než ostatním? |\n"
            "| **W — Weaknesses / Slabé stránky** | Vnitřní prostředí | Co nás brzdí nebo oslabuje. | Kde máme mezery? |\n"
            "| **O — Opportunities / Příležitosti** | Vnější prostředí | Co se děje kolem nás a můžeme toho využít. | Jaký trend nebo změna nám může pomoct? |\n"
            "| **T — Threats / Hrozby** | Vnější prostředí | Co nás může ohrozit. | Co se může pokazit nebo kdo nás může předběhnout? |"
        )
        st.write("**Pozor na častou chybu:** Silné a slabé stránky jsou uvnitř organizace nebo člověka. Příležitosti a hrozby přicházejí zvenčí. „Máme málo peněz“ je slabá stránka. „Zdraží nájem“ je hrozba.")

        st.markdown("#### 1.6.2 Základy řízení rizik")
        st.write("Řízení rizik znamená přemýšlet dopředu o tom, co se může pokazit, jak moc je to pravděpodobné, jak velký dopad by to mělo a co s tím uděláme.")
        st.markdown(
            "| Krok | Otázka | Příklad pro školní akci |\n"
            "| :--- | :--- | :--- |\n"
            "| **Identifikace rizika** | Co se může pokazit? | Nepřijde dost lidí, onemocní moderátor, selže technika. |\n"
            "| **Vyhodnocení rizika** | Jak pravděpodobné to je a jak velký dopad to bude mít? | Selhání mikrofonu má vysoký dopad, ale dá se snadno zálohovat. |\n"
            "| **Prevence** | Co uděláme, aby riziko nenastalo? | Technická zkouška den předem, předprodej vstupenek, jasný harmonogram. |\n"
            "| **Záložní plán / Plan B** | Co uděláme, když riziko nastane? | Náhradní mikrofon, náhradní moderátor, přesun programu dovnitř při dešti. |"
        )
        st.write("**Pointa řízení rizik:** Dobrý manažer není člověk, kterému se nikdy nic nepokazí. Je to člověk, který počítá s tím, že se něco pokazit může, a má připravený plán B.")

        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Cvičení k bloku 1: Osobní nebo projektová SWOT</b><br>"
            "Vyber sebe, školní projekt nebo lokální podnik. Doplň: S — Strengths (V čem je silný?), W — Weaknesses (Co ho brzdí?), O — Opportunities (Jaké příležitosti může využít?), T — Threats (Jaká rizika mu hrozí?)</div>",
            unsafe_allow_html=True,
        )

        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 5: SWOT analýza a Plán B tvého projektu</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"]("6.1.9", "Sestav SWOT analýzu svého projektu (Silné, Slabé stránky, Příležitosti, Hrozby) a pojmenuj 1 největší riziko a Plán B.", "6", st.session_state.get("ulozene_odpovedi", {}))

    elif idx == 6:
        st.markdown("## 1. Management – Jak z chaosu udělat fungující firmu")
        
        st.markdown("### 1.7 Moderní přesah: Agilní řízení, remote work")
        st.write("Současné řízení lidí se posouvá od prostého zadávání úkolů k práci s autonomií, důvěrou, smyslem práce, psychologickým bezpečím a průběžnou zpětnou vazbou. Moderní manažer není jen kontrolor výkonu, ale spíš koordinátor, kouč a tvůrce podmínek, ve kterých tým dokáže dlouhodobě fungovat.")
        
        st.markdown(
            "| Moderní technika | Co znamená | Příklad v praxi |\n"
            "| :--- | :--- | :--- |\n"
            "| **Agilní řízení** | Práce v krátkých cyklech, rychlé testování, pravidelné vyhodnocování a úpravy podle zpětné vazby. | Tým aplikace nejdřív spustí základní verzi a podle reakcí uživatelů ji postupně zlepšuje. |\n"
            "| **Scrum / sprinty** | Tým pracuje v krátkých časových úsecích, na jejichž konci ukáže konkrétní výsledek. | Dvoutýdenní sprint: připravit landing page, otestovat reklamu a vyhodnotit data. |\n"
            "| **Kanban** | Vizualizace práce ve sloupcích, například „čeká“, „probíhá“, „hotovo“. | Nástěnka v Trellu, Asaně nebo Notionu pro školní projekt. |\n"
            "| **OKR** | Stanovení ambiciózního cíle a měřitelných klíčových výsledků. | Cíl: zvýšit účast na školní akci. Klíčové výsledky: 200 registrací, 30 % účast prvních ročníků, 20 sdílení kampaně. |\n"
            "| **Koučovací styl vedení** | Manažer nepředává jen příkazy, ale klade otázky, rozvíjí lidi a pomáhá jim hledat řešení. | Místo „udělej to takhle“ se ptá: „Jaké možnosti máme a co doporučuješ?“ |\n"
            "| **Průběžná zpětná vazba** | Zpětná vazba se nedává jen jednou za rok, ale pravidelně a konkrétně. | Krátký check-in po kampani: co fungovalo, co upravíme, co si odnášíme. |\n"
            "| **Psychologické bezpečí** | Tým se nebojí říct názor, přiznat chybu nebo požádat o pomoc. | Na poradě se řeší chyba v kampani bez zesměšňování viníka. |\n"
            "| **Hybridní a remote řízení** | Vedení týmu, který pracuje částečně nebo úplně online. | Jasná pravidla pro Slack, Notion, online meetingy, termíny a dostupnost lidí. |\n"
            "| **Wellbeing a prevence vyhoření** | Manažer sleduje nejen výkon, ale i dlouhodobou udržitelnost práce. | Realistické termíny, rozdělení zátěže, pauzy, hranice mezi prací a volnem. |"
        )
        st.write("**Digitální nástroje:** Trello, Asana, Notion, Slack, Teams nebo Google Workspace nepředstavují management samy o sobě. Jsou to jen nástroje. Důležité je, zda tým rozumí cíli, ví, kdo za co odpovídá, a má jasně nastavenou komunikaci.")
        st.write("**Riziko moderní práce:** Flexibilita může být výhoda, ale také past. Když je člověk pořád online, odpovídá večer, nemá jasné priority a práce se nikdy „nevypne“, roste riziko stresu a vyhoření.")

    # =========================================================================
    # BLOK 6: 2. Marketing (Úvod a 2.1 Podstata)
    # =========================================================================
    elif idx == 7:
        st.markdown("## 2. Marketing – Hra o pozornost a marketingový mix")

        st.markdown(
            "<div class='box-blue'>"
            "🎯 <b>Moderní hook:</b> <i>„Proč si koupíš boty za 4 000 Kč, když skoro stejný fejk stojí 500 Kč?“</i><br>"
            "Marketing není jen reklama. Je to způsob, jak pochopit potřeby lidí, vytvořit hodnotu, odlišit se od konkurence a dostat správnou nabídku ke správnému člověku."
            "</div>",
            unsafe_allow_html=True,
        )

        st.markdown(
            "<div class='box-green'>"
            "🎯 <b>Cíl 2. bloku:</b> Pochopíš, jak firmy zkoumají trh, rozdělují zákazníky do segmentů, volí cílovou skupinu, nastavují positioning a skládají marketingový mix 4P."
            "</div>",
            unsafe_allow_html=True,
        )

        st.markdown("### 2.1 Podstata a vývoj marketingu")
        st.write("Marketing je proces, při kterém firma zjišťuje potřeby zákazníků, vytváří pro ně hodnotu a uspokojuje jejich potřeby tak, aby zároveň dosahovala svých cílů, typicky zisku. Nejde tedy jen o reklamu nebo prodej. Reklama je pouze jedna část marketingové komunikace a prodej je okamžik, kdy zákazník skutečně nakoupí.")
        
        st.markdown(
            "<div class='box-yellow'>"
            "🧠 <b>Jednoduše:</b> Prodej se ptá: „Jak prodáme to, co už máme?“ Marketing se ptá: „Co lidé opravdu potřebují, komu to nabídneme, za jakou cenu, kde a jak o tom budou vědět?“"
            "</div>",
            unsafe_allow_html=True,
        )
        
        st.write("Marketing pomáhá firmě pochopit trh, zákazníka, konkurenci i vlastní nabídku. Dobře nastavený marketing nezačíná plakátem ani TikTok videem, ale otázkou: komu pomáháme, jakou hodnotu vytváříme a proč by si měl zákazník vybrat právě nás?")
        
        st.markdown(
            "| Pojem | Co znamená | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Potřeba** | Pocit nedostatku něčeho důležitého. Potřeby mohou být základní, sociální i psychologické. | Potřeba jíst, být v bezpečí, patřit do skupiny, odlišit se. |\n"
            "| **Přání** | Konkrétní podoba potřeby ovlivněná kulturou, osobností, trendy a příjmem. | Potřebu pít lze naplnit vodou, ale přání může být bubble tea nebo prémiová limonáda. |\n"
            "| **Poptávka** | Přání podpořené ochotou a schopností zaplatit. | Student chce nové tenisky a má peníze nebo rodičovský souhlas je koupit. |\n"
            "| **Trh** | Prostor, kde se setkává nabídka a poptávka. | Trh s oblečením, mobilními aplikacemi, kávou, doučováním nebo streamovacími službami. |\n"
            "| **Zákazník** | Ten, kdo nakupuje nebo platí. | Rodič koupí školní batoh. |\n"
            "| **Spotřebitel** | Ten, kdo produkt skutečně používá nebo spotřebuje. | Student batoh nosí do školy. |"
        )

        st.markdown("#### 2.1.1 Vývoj podnikatelských koncepcí")
        st.write("Firmy se v historii nedívaly na zákazníka vždy stejně. Podnikatelské koncepce ukazují, na co se firma při řízení trhu hlavně soustředí.")
        st.markdown(
            "| Koncepce | Hlavní myšlenka | Příklad | Riziko |\n"
            "| :--- | :--- | :--- | :--- |\n"
            "| **Výrobní koncepce** | Vyrábět levně, efektivně a ve velkém. Zákazník koupí to, co je dostupné a levné. | Levná základní trička nebo potraviny vyráběné ve velkých sériích. | Firma může podcenit kvalitu, značku a skutečné potřeby zákazníka. |\n"
            "| **Výrobková koncepce** | Důraz na co nejlepší produkt, kvalitu, technické parametry a inovace. | Telefon s výborným fotoaparátem, prémiové sportovní boty, kvalitní notebook. | Firma může vyrábět „dokonalý“ produkt, který lidé nepotřebují nebo si ho nemohou dovolit. |\n"
            "| **Prodejní koncepce** | Hlavní je zákazníka přesvědčit, přemluvit a prodat mu co nejvíc. | Agresivní telefonní nabídky, tlak na okamžitý nákup, „jen dnes“ akce. | Může poškodit důvěru a vést k manipulaci. |\n"
            "| **Marketingová koncepce** | Nejdřív zjistit potřeby zákazníka a potom vytvořit nabídku, která je naplní lépe než konkurence. | E-shop analyzuje chování zákazníků a upraví sortiment, cenu i komunikaci. | Pokud se sledují jen krátkodobá data, firma může přehlédnout etiku nebo dlouhodobou hodnotu. |\n"
            "| **Sociální / etická koncepce** | Firma bere ohled nejen na zisk a zákazníka, ale i na společnost, životní prostředí a dlouhodobý užitek. | Udržitelná móda, férové dodavatelské řetězce, omezení greenwashingu. | Pokud firma jen předstírá odpovědnost, vzniká greenwashing. |"
        )
        st.write("**Moderní přesah:** Dnešní marketing už často neprodává jen produkt, ale také životní styl, hodnoty a identitu. Proto je důležité rozlišovat mezi férovou komunikací a manipulací.")

        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 6: Podstata a koncepce tvého projektu</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"]("6.2.1", "1. Jakou ZÁKLADNÍ POTŘEBU uspokojuje tvůj projekt a jaká podnikatelská koncepce k němu nejlépe sedí?", "6", st.session_state.get("ulozene_odpovedi", {}))

    # =========================================================================
    # BLOK 7: 2.2 Marketingový výzkum
    # =========================================================================
    elif idx == 8:
        st.markdown("## 2. Marketing – Hra o pozornost a marketingový mix")
        
        st.markdown("### 2.2 Marketingový výzkum a analýza trhu")
        st.write("Marketingový výzkum znamená systematický sběr, třídění a vyhodnocování informací o trhu, zákaznících, konkurenci a prostředí firmy. Jeho cílem je snížit riziko při rozhodování.")
        st.write("**Proč firmy dělají výzkum:** Bez dat firma často jen hádá. Výzkum pomáhá zjistit, kdo je zákazník, co řeší, kolik je ochoten zaplatit, kde nakupuje, jak vnímá značku a proč dává přednost konkurenci.")
        st.write("Marketingový výzkum může odpovídat například na otázky:")
        st.markdown(
            "- Kdo je náš zákazník?\n"
            "- Jaký problém mu produkt řeší?\n"
            "- Jakou cenu je ochoten zaplatit?\n"
            "- Která reklama funguje lépe?\n"
            "- Proč zákazníci opouštějí košík v e-shopu?\n"
            "- Jak nás zákazníci vnímají oproti konkurenci?"
        )
        
        st.markdown("#### 2.2.1 Zdroje dat")
        st.markdown(
            "| Typ dat | Co znamená | Výhody | Nevýhody |\n"
            "| :--- | :--- | :--- | :--- |\n"
            "| **Primární data** | Nově sesbíraná data přímo pro konkrétní účel výzkumu. | Jsou přesně zaměřená na problém firmy. | Sběr může být dražší a časově náročnější. |\n"
            "| **Sekundární data** | Již existující data, která byla původně sesbírána pro jiný účel. | Jsou rychle dostupná a často levnější. | Nemusí přesně odpovídat aktuálnímu problému. |"
        )
        st.write("**Příklady sekundárních dat:** Statistiky Českého statistického úřadu, veřejné databáze, výroční zprávy, prodejní výkazy, data z e-shopu, informace ze sociálních sítí, recenze zákazníků nebo analýzy konkurence.")

        st.markdown("#### 2.2.2 Metody výzkumu")
        st.markdown(
            "| Metoda | Co zjišťuje | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Kvantitativní výzkum** | Odpovídá hlavně na otázku „kolik?“ Pracuje s větším počtem odpovědí a čísly. | Dotazník mezi 300 studenty: kolik by zaplatili za školní merch? |\n"
            "| **Kvalitativní výzkum** | Odpovídá hlavně na otázku „proč?“ Zkoumá motivace, postoje a emoce. | Hloubkové rozhovory nebo focus group se studenty o tom, proč se jim školní merch líbí nebo nelíbí. |\n"
            "| **Pozorování** | Sleduje skutečné chování lidí, ne jen to, co říkají. | Obchod sleduje, u kterého regálu se lidé zastavují nejdéle. |\n"
            "| **Experiment** | Testuje, jak změna jedné věci ovlivní chování zákazníků. | A/B test: jedna skupina vidí zelené tlačítko „Koupit“, druhá černé. Firma porovná konverze. |"
        )
        st.write("**Sociální sítě jako výzkum trhu:** TikTok, Instagram nebo YouTube neustále ukazují, na co lidé reagují. Počet zhlédnutí, komentáře, sdílení, uložení a míra prokliku jsou signály, které firmám pomáhají pochopit publikum. Pozor ale: vysoký dosah nemusí vždy znamenat důvěru ani dlouhodobý prodej.")

        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 7: Tvůj marketingový výzkum</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"]("6.2.2", "1. Kde získáš SEKUNDÁRNÍ DATA o tvém trhu a jakou metodu použiješ pro sběr PRIMÁRNÍCH DAT?", "6", st.session_state.get("ulozene_odpovedi", {}))

    # =========================================================================
    # BLOK 8: 2.3 STP proces
    # =========================================================================
    elif idx == 9:
        st.markdown("## 2. Marketing – Hra o pozornost a marketingový mix")
        
        st.markdown("### 2.3 STP proces: Segmentace, Cílení a Positioning")
        st.write("STP proces pomáhá firmě vybrat správné zákazníky a odlišit se od konkurence. Místo snahy oslovit „všechny“ firma rozdělí trh na skupiny, vybere nejvhodnější segment a nastaví jasnou pozici značky.")
        st.markdown("**STP jednoduše:**\n* **S – Segmentation:** rozdělíme trh na skupiny.\n* **T – Targeting:** vybereme, komu se budeme věnovat.\n* **P – Positioning:** určíme, jak chceme být v hlavě zákazníka zapamatovaní.")
        
        st.markdown("#### 2.3.1 Segmentace trhu")
        st.write("Segmentace trhu je rozdělení trhu na menší, relativně podobné skupiny zákazníků. Lidé v jednom segmentu mají podobné potřeby, chování nebo očekávání.")
        st.markdown(
            "| Kritérium segmentace | Co sleduje | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Geografická segmentace** | Místo, region, město, stát, klima nebo typ lokality. | Jiná nabídka kavárny v centru Prahy a jiná v menším městě. |\n"
            "| **Demografická segmentace** | Věk, pohlaví, příjem, vzdělání, rodinná situace nebo povolání. | Kosmetika pro teenagery, bankovní účet pro studenty, pojištění pro rodiny. |\n"
            "| **Psychografická segmentace** | Životní styl, hodnoty, zájmy, osobnost a postoje. | Značka oblečení cílí na lidi, kteří chtějí udržitelnost a minimalismus. |\n"
            "| **Behaviorální segmentace** | Nákupní chování, frekvence užívání, věrnost značce, reakce na slevy. | E-shop rozlišuje nové zákazníky, věrné zákazníky a ty, kteří často opouštějí košík. |"
        )

        st.markdown("#### 2.3.2 Cílení: targeting")
        st.write("Cílení znamená výběr segmentu nebo segmentů, na které firma zaměří své úsilí. Firma nemůže dělat všechno pro všechny, protože má omezené peníze, čas, tým i pozornost zákazníků.")
        st.markdown(
            "| Typ cílení | Jak funguje | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Masový marketing** | Firma oslovuje co nejširší trh jednou nabídkou. | Základní potraviny, běžná balená voda, některé produkty denní spotřeby. |\n"
            "| **Koncentrovaný marketing** | Firma se soustředí na jeden vybraný segment a snaží se mu dobře porozumět. | Malá značka sportovního oblečení pro běžce. |\n"
            "| **Nika / níšový marketing** | Firma cílí na úzkou, specifickou skupinu s jasnou potřebou. | Veganské proteinové tyčinky pro sportovce s intolerancí laktózy. |"
        )

        st.markdown("#### 2.3.3 Positioning a USP")
        st.write("Positioning znamená vytvoření jedinečného obrazu značky v mysli zákazníka vůči konkurenci. Nejde jen o to, co firma říká o sobě, ale hlavně o to, jak si ji zákazník pamatuje.")
        st.write("USP – Unique Selling Proposition znamená unikátní prodejní argument. Je to jasná odpověď na otázku: Proč si má zákazník vybrat právě nás, a ne konkurenci?")
        st.markdown(
            "| Značka / produkt | Možný positioning | Možné USP |\n"
            "| :--- | :--- | :--- |\n"
            "| **Studentská kavárna** | Klidné místo na učení blízko školy. | Káva + tiché studijní místo + studentská sleva. |\n"
            "| **Udržitelný merch** | Školní oblečení, které nevypadá jako reklamní tričko. | Lokální výroba, kvalitní střih a design navržený studenty. |\n"
            "| **Aplikace na učení** | Rychlá příprava na testy bez zahlcení. | Krátké kartičky, gamifikace a opakování podle chyb. |"
        )
        st.warning("**Častá chyba:** „Jsme kvalitní a levní“ není silný positioning. Stejně to tvrdí skoro všichni. Silnější je konkrétní, zapamatovatelný a ověřitelný rozdíl.")

        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 8: STP analýza tvého projektu</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"]("6.2.3", "Popiš Cílovou skupinu (Demografické a psychografické údaje) a napiš Unikátní prodejní argument (USP v 1 větě) pro svůj projekt.", "6", st.session_state.get("ulozene_odpovedi", {}))

    # =========================================================================
    # BLOK 9: 2.4 Marketingový mix 4P
    # =========================================================================
    elif idx == 10:
        st.markdown("## 2. Marketing – Hra o pozornost a marketingový mix")
        
        st.markdown("### 2.4 Marketingový mix: Klasické 4P")
        st.write("Marketingový mix je soubor nástrojů, které firma kombinuje, aby uspěla na trhu. Klasický model se označuje jako 4P: Product, Price, Place, Promotion.")
        
        st.markdown(
            "| 4P | Česky | Hlavní otázka |\n"
            "| :--- | :--- | :--- |\n"
            "| **Product** | Produkt | Co nabízíme a jakou hodnotu to zákazníkovi přináší? |\n"
            "| **Price** | Cena | Kolik to bude stát a jak cena ovlivní vnímání hodnoty? |\n"
            "| **Place** | Distribuce | Kde a jak se produkt dostane k zákazníkovi? |\n"
            "| **Promotion** | Propagace / komunikace | Jak se o nabídce zákazník dozví a proč jí má věřit? |"
        )
        st.info("**Pointa 4P:** Jednotlivé prvky musí dávat smysl dohromady. Luxusní produkt s prémiovou cenou, levným obalem a chaotickou komunikací působí nedůvěryhodně. Levný produkt s drahou kampaní zase nemusí ekonomicky vycházet.")

        st.markdown("#### 2.4.1 Product / Produkt")
        st.write("Produkt je všechno, co firma nabízí zákazníkovi k uspokojení potřeby nebo přání. Může jít o fyzickou věc, službu, aplikaci, zážitek, událost, kurz nebo kombinaci více prvků.")
        
        st.write("**Vrstvy produktu**")
        st.markdown(
            "| Vrstva produktu | Co znamená | Příklad: auto | Příklad: školní merch |\n"
            "| :--- | :--- | :--- | :--- |\n"
            "| **Jádro produktu** | Základní užitek, kvůli kterému zákazník produkt pořizuje. | Potřeba přepravit se z místa na místo. | Oblečení, sounáležitost se školou, identita. |\n"
            "| **Reálný produkt** | Konkrétní podoba produktu: značka, design, kvalita, obal, funkce. | Konkrétní značka auta, výkon, barva, výbava, bezpečnost. | Mikina, materiál, střih, logo, barva, kvalita potisku. |\n"
            "| **Rozšířený produkt** | Doplňkové služby a výhody kolem produktu. | Záruka, servis, financování, dovoz, asistence. | Možnost výměny velikosti, předobjednávka, balení, doručení do školy. |"
        )

        st.write("**Životní cyklus produktu**")
        st.write("Produkt obvykle prochází několika fázemi. V každé fázi se mění tržby, zisk, konkurence i marketingová strategie.")
        st.markdown(
            "| Fáze | Co se děje | Typická marketingová výzva |\n"
            "| :--- | :--- | :--- |\n"
            "| **Zavádění** | Produkt je nový, lidé ho neznají, prodeje rostou pomalu a náklady na uvedení jsou vysoké. | Vysvětlit, k čemu produkt je, získat první zákazníky a důvěru. |\n"
            "| **Růst** | Produkt získává popularitu, rostou tržby a přichází konkurence. | Odlišit se, posílit značku a zvládnout vyšší poptávku. |\n"
            "| **Zralost** | Trh je nasycený, růst se zpomaluje, konkurence je silná. | Udržet zákazníky, inovovat, pracovat s cenou a věrnostními programy. |\n"
            "| **Pokles** | Prodeje klesají, produkt zastarává nebo ho nahrazují nové technologie a trendy. | Rozhodnout, zda produkt inovovat, stáhnout z trhu nebo nahradit novým. |"
        )
        
        st.write("**Značka a obal:** Značka pomáhá produkt odlišit, vytváří důvěru a zjednodušuje rozhodování zákazníka. Obal není jen „krabička“. Má několik funkcí:")
        st.markdown(
            "- **ochrannou** — chrání produkt při přepravě a skladování,\n"
            "- **informační** — obsahuje složení, návod, velikost, původ, datum spotřeby,\n"
            "- **propagační** — přitahuje pozornost a komunikuje značku."
        )
        st.write("**Příklad:** U energetického nápoje obal neřeší jen ochranu plechovky. Barvy, název, typografie a styl komunikují energii, výkon, gaming, sport nebo status.")

        st.markdown("#### 2.4.2 Price / Cena")
        st.write("Cena je jediný prvek marketingového mixu, který přímo generuje příjmy. Produkt, distribuce i propagace obvykle vytvářejí náklady. Cena zároveň silně ovlivňuje vnímání hodnoty a pozici značky. Cena není jen číslo: Nízká cena může přilákat zákazníky, ale také vyvolat dojem nízké kvality. Vysoká cena může působit prémiově, ale musí být podpořená kvalitou, značkou nebo jedinečností.")
        st.write("**Metody stanovení ceny**")
        st.markdown(
            "| Metoda | Jak funguje | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Nákladově orientovaná cena** | Firma spočítá náklady a přidá přirážku nebo požadovaný zisk. | Výroba mikiny stojí 420 Kč, firma přidá marži 180 Kč, cena je 600 Kč. |\n"
            "| **Poptávkově orientovaná cena** | Cena vychází z toho, kolik je zákazník ochoten zaplatit. | Limitovaná edice tenisek se prodává dráž, protože ji lidé silně chtějí. |\n"
            "| **Konkurenčně orientovaná cena** | Firma nastaví cenu podle konkurence na trhu. | Kavárna sleduje ceny podobných kaváren v okolí. |"
        )

        st.write("**Cenové strategie**")
        st.markdown(
            "| Strategie | Co znamená | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Skimming** | Vysoká počáteční cena u novinky, později může cena klesat. | Nový telefon nebo herní konzole při uvedení na trh. |\n"
            "| **Penetrační cena** | Nízká počáteční cena pro rychlé získání zákazníků a podílu na trhu. | Nová streamovací služba nabídne první měsíce velmi levně. |\n"
            "| **Slevy** | Dočasné snížení ceny pro podporu nákupu. | Black Friday, studentská sleva, sezónní výprodej. |\n"
            "| **Skonto** | Sleva za rychlou platbu nebo splnění určité platební podmínky. | Firma poskytne odběrateli 2 % slevu, pokud zaplatí fakturu do 10 dnů. |"
        )
        st.warning("**Pozor:** Sleva může krátkodobě zvýšit prodej, ale při častém používání učí zákazníky čekat na akci a oslabuje vnímanou hodnotu značky.")

        st.markdown("#### 2.4.3 Place / Distribuce")
        st.write("Distribuce řeší, jak se produkt dostane od výrobce ke konečnému zákazníkovi. Nestačí mít dobrý produkt — zákazník ho musí umět pohodlně najít, koupit a získat včas.")
        
        st.markdown("**Distribuční cesty**")
        st.markdown(
            "| Typ cesty | Jak funguje | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Přímá distribuční cesta** | Výrobce prodává přímo spotřebiteli bez prostředníka. | Tvůrce prodává vlastní e-book přes svůj web. Pekárna prodává pečivo ve vlastní prodejně. |\n"
            "| **Nepřímá distribuční cesta** | Mezi výrobcem a spotřebitelem je zprostředkovatel. | Výrobce nápojů prodává přes velkoobchod a supermarket. |"
        )
        
        st.markdown("**Zprostředkovatelé**")
        st.markdown(
            "| Zprostředkovatel | Co dělá | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Velkoobchod** | Nakupuje ve velkém a prodává dalším podnikatelům, obchodům nebo institucím. | Velkoobchod dodává nápoje do kaváren a školních bufetů. |\n"
            "| **Maloobchod** | Prodává konečnému spotřebiteli. | Supermarket, drogerie, knihkupectví, e-shop s oblečením. |"
        )
        st.write("**Logistika a e-commerce:** Logistika zahrnuje plánování a řízení toku zboží, informací a objednávek (skladování, doprava, balení, objednávky, reklamace). E-commerce znamená prodej online. Omni-channel v praxi: Zákazník si produkt najde na Instagramu, porovná ho na e-shopu, vyzvedne v kamenné prodejně a reklamaci řeší přes zákaznickou podporu online. Pro zákazníka by to měl být jeden plynulý zážitek.")

        st.markdown("#### 2.4.4 Promotion / Propagace a komunikační mix")
        st.write("Propagace neznamená jen reklamu. Jde o celou komunikaci firmy se zákazníky, veřejností, médii a partnery. Cílem je informovat, přesvědčit, připomenout značku a budovat vztah.")
        st.markdown(
            "| Prvek komunikačního mixu | Co znamená | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Reklama** | Placená, neosobní forma prezentace přes masmédia nebo digitální kanály. | TV spot, billboard, reklama na YouTube, banner, placený příspěvek na Instagramu. |\n"
            "| **Podpora prodeje (Sales promotion)** | Krátkodobé stimuly k okamžitému nákupu. | Slevový kupón, vzorek zdarma, akce 1+1, soutěž, věrnostní program. |\n"
            "| **Public Relations (PR)** | Budování dobrého jména firmy a vztahů s veřejností, médii a komunitou. | Tisková zpráva, rozhovor v médiích, sponzoring, krizová komunikace, charitativní projekt. |\n"
            "| **Osobní prodej (Personal selling)** | Osobní komunikace se zákazníkem tváří v tvář nebo online. | Obchodní zástupce, konzultace v prodejně, B2B jednání, online demo produktu. |\n"
            "| **Přímý marketing (Direct marketing)** | Přímé oslovení konkrétně vybraných zákazníků. | E-mailing, SMS nabídka, telemarketing, adresná zásilka, personalizovaná nabídka v aplikaci. |"
        )
        st.write("**Influencer marketing a UGC:** V moderní propagaci hrají velkou roli influenceři a obsah vytvářený uživateli (UGC). UGC jsou recenze, videa, fotky nebo doporučení od běžných lidí. Často působí důvěryhodněji než klasická reklama, ale placené spolupráce musí být jasně označené.")
        st.write("**Virál není strategie sám o sobě:** Virální příspěvek může přinést velký dosah, ale pokud neodpovídá značce, cílové skupině a produktu, nemusí vést k prodeji ani dlouhodobé důvěře.")

        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 9: Nastavení Produktu, Ceny a Distribuce</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"]("6.2.4", "1. PRODUKT, CENA a DISTRIBUCE – Co tvoří rozšířený produkt, jakou zvolíš cenovou metodu a jakou cestou se dostane k zákazníkovi?", "6", st.session_state.get("ulozene_odpovedi", {}))

        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 10: Komunikační mix a finální rekapitulace 4P</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"]("6.2.5", "1. PROPAGACE – Jaké 2 hlavní nástroje propagace použiješ a využiješ Influencer marketing či UGC?", "6", st.session_state.get("ulozene_odpovedi", {}))

    # =========================================================================
    # BLOK 10: 3. Brand (Úvod a 3.1)
    # =========================================================================
    elif idx == 11:
        st.markdown("## 3. Brand, nákupní psychologie a etika")
        
        st.markdown(
            "<div class='box-blue'>"
            "🎯 <b>Moderní hook:</b> <i>„Jak tě značky nutí utrácet peníze, které nemáš, za věci, které nepotřebuješ.“</i><br> Marketing pracuje s emocemi, pozorností, důvěrou a identitou. Proto je důležité rozumět nejen tomu, jak značky fungují, ale i tomu, kde končí přesvědčování a začíná manipulace."
            "</div>",
            unsafe_allow_html=True,
        )
        
        st.markdown("### 3.1 Značka a budování brandu")
        st.write("Značka neboli brand není jen logo nebo název produktu. Je to soubor představ, emocí, zkušeností a asociací, které si lidé s produktem nebo firmou spojují. Fyzický produkt může být technicky podobný jako konkurenční výrobek, ale značka rozhoduje o tom, jak mu zákazník věří, jakou hodnotu mu přisuzuje a zda se k němu opakovaně vrací.")
        st.write("**Jednoduše:** Produkt je to, co firma vyrábí nebo nabízí. Značka je to, co si o tom lidé myslí, cítí a pamatují.")
        st.write("Příklad: Bílé tričko může stát 150 Kč bez značky, ale několik tisíc korun, pokud je spojeno se známým logem, komunitou, statusem nebo životním stylem. Materiál může být podobný, ale vnímaná hodnota je jiná.")

        st.markdown("#### 3.1.1 Anatomie a prvky značky")
        st.markdown(
            "| Prvek značky | Co znamená | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Vizuální identita** | To, co zákazník vidí: název, logo, barvy, typografie, obal, grafický styl. | Minimalistické logo, typická barva obalu, jednotný styl příspěvků na Instagramu. |\n"
            "| **Audio / senzorická identita** | Zvuky, znělky, vůně nebo jiné smyslové prvky spojené se značkou. | Znělka streamovací služby, typická vůně v obchodě, zvuk při zapnutí zařízení. |\n"
            "| **Storytelling** | Příběh značky: proč vznikla, čemu věří a jaký problém chce řešit. | Značka oblečení vypráví příběh lokální výroby a férových podmínek. |\n"
            "| **Mise a vize** | Mise říká, proč značka existuje dnes. Vize ukazuje, kam chce směřovat. | Mise: zpřístupnit kvalitní vzdělávání. Vize: aby se každý student učil podle sebe. |\n"
            "| **Hodnoty značky** | Principy, které značka zastává a podle kterých se rozhoduje. | Udržitelnost, férovost, kreativita, jednoduchost, dostupnost. |"
        )
        st.write("**Pozor:** Silná značka nevzniká jen tím, že má hezké logo. Pokud se komunikace značky neshoduje s realitou produktu, zákazník ztratí důvěru.")

        st.markdown("#### 3.1.2 Brand equity a brand loyalty")
        st.write("Brand equity znamená hodnotu značky. Může být peněžní i nepeněžní. Silná značka umožňuje prodávat dráž, snáze zavádět nové produkty, získávat doporučení a lépe přežít krize. Brand loyalty znamená věrnost značce.")
        st.markdown(
            "| Pojem | Co znamená | Jak se projevuje |\n"
            "| :--- | :--- | :--- |\n"
            "| **Brand equity** | Dodatečná hodnota, kterou značka přináší produktu. | Zákazník je ochoten zaplatit víc za známou a důvěryhodnou značku. |\n"
            "| **Brand loyalty** | Věrnost zákazníka značce. | Opakované nákupy, členství v komunitě, doporučování přátelům. |\n"
            "| **Komunita značky** | Skupina lidí, kteří se kolem značky sdružují a sdílí podobné hodnoty. | Fanoušci sportovní značky, herní komunity, zákazníci lokální kavárny. |"
        )

        st.markdown("#### 3.1.3 Strategie značky: rebranding a extenze značky")
        st.write("Rebranding je změna image značky. Může zahrnovat nové logo, barvy, slogan, tón komunikace nebo celkovou strategii. Firma k němu sahá, když chce působit moderněji, oslovit novou cílovou skupinu nebo se odlišit od minulosti.")
        st.write("Extenze značky znamená rozšíření známé značky do nové kategorie produktů. Výhodou je, že novinka může těžit z důvěry existující značky. Rizikem je, že pokud se rozšíření nepovede, může poškodit i původní značku.")
        st.write("**Příklad:** Značka známá pro sportovní oblečení začne prodávat parfémy nebo chytré hodinky. Pokud to odpovídá jejím hodnotám a zákazníci tomu věří, může to fungovat. Pokud to působí náhodně, značka se rozmělní.")

        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 11: Identita a Příběh tvé značky</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"]("6.3.1", "1. Napiš příběh, misi, hodnoty a vizuální styl své značky (Brand).", "6", st.session_state.get("ulozene_odpovedi", {}))

    # =========================================================================
    # BLOK 11: 3.2 Nákupní chování a psychologie
    # =========================================================================
    elif idx == 12:
        st.markdown("## 3. Brand, nákupní psychologie a etika")
        
        st.markdown("### 3.2 Nákupní chování a psychologie spotřebitele")
        st.write("Nákupní chování zkoumá, jak se lidé rozhodují při nákupu, co je ovlivňuje a proč si vyberou jeden produkt místo druhého. Zákazník se často nerozhoduje jen racionálně. Do nákupu vstupují emoce, sociální tlak, zkušenosti, značka, cena, pohodlí i momentální nálada.")

        st.markdown("#### 3.2.1 Proces nákupního rozhodování")
        st.markdown(
            "| Fáze | Co se děje | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **1. Rozpoznání potřeby** | Zákazník si uvědomí problém nebo přání. | Student zjistí, že potřebuje notebook na školu. |\n"
            "| **2. Hledání informací** | Zjišťuje možnosti, čte recenze, ptá se okolí nebo sleduje videa. | Porovnává modely, kouká na YouTube recenze a ptá se spolužáků. |\n"
            "| **3. Hodnocení alternativ** | Porovnává cenu, výkon, značku, design, dostupnost a záruku. | Vybírá mezi levnějším modelem, výkonnějším modelem a známější značkou. |\n"
            "| **4. Nákupní rozhodnutí** | Vybere produkt a provede nákup. | Koupí notebook v e-shopu nebo kamenné prodejně. |\n"
            "| **5. Poprodejní chování** | Po nákupu hodnotí spokojenost. Může přijít nadšení, reklamace nebo pochybnosti. | Říká si, jestli neměl koupit jiný model — tomu se říká kognitivní disonance. |"
        )
        st.write("**Kognitivní disonance** znamená nepříjemný pocit pochybnosti po rozhodnutí. Zákazník si například po drahém nákupu říká: „Nebylo to zbytečně moc? Neměl/a jsem vybrat jinou značku?“ Firmy ji snižují kvalitní podporou, jasnou komunikací, zárukou, recenzemi a potvrzením, že zákazník zvolil dobře.")

        st.markdown("#### 3.2.2 Faktory ovlivňující nákupní chování")
        st.write("Faktory ovlivňující nákupní chování ukazují, že zákazník se nerozhoduje izolovaně. Jeho nákupní rozhodnutí ovlivňuje osobní situace, psychika, okolí, kultura, hodnoty i skupiny, ke kterým patří nebo ke kterým chce patřit.")
        st.markdown(
            "| Faktor | Co zahrnuje | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Osobní faktory** | Věk, příjem, životní fáze, životní styl, vzdělání a zkušenosti. | Student, rodič malého dítěte a manažer firmy mají jiné nákupní priority. |\n"
            "| **Psychologické faktory** | Vnímání, postoje, motivace, emoce, osobnost a potřeby. | Maslowova pyramida potřeb pomáhá vysvětlit, proč lidé řeší bezpečí, vztahy, uznání i seberealizaci. |\n"
            "| **Sociální faktory** | Rodina, přátelé, vrstevníci, influenceři, celebrity a referenční skupiny. | Teenager si koupí značku, kterou nosí oblíbený tvůrce nebo kamarádi. |\n"
            "| **Kulturní faktory** | Kultura, hodnoty společnosti, tradice, normy a společenský status. | Jiné produkty se prodávají jako symbol statusu, jiné jako praktická volba. |"
        )
        st.write("**Referenční skupina:** Skupina lidí, podle které se člověk porovnává nebo které se chce podobat. Může jít o spolužáky, sportovní tým, influencera, herní komunitu nebo profesní vzor.")

        st.markdown("#### 3.2.3 Racionální vs. emoční nákupy")
        st.write("Racionální nákup je založený hlavně na porovnání ceny, kvality, užitku a parametrů. Emoční nákup je ovlivněný pocitem, touhou, statusem, identitou, strachem, FOMO nebo impulzem.")
        st.markdown(
            "| Typ nákupu | Jak vypadá | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Racionální nákup** | Zákazník porovnává fakta, cenu, výkon, recenze a dlouhodobý užitek. | Výběr notebooku podle výkonu, baterie, ceny a záruky. |\n"
            "| **Emoční nákup** | Zákazník nakupuje podle pocitu, identity, značky, nálady nebo sociálního tlaku. | Limitované tenisky, merch oblíbeného tvůrce, impulzivní nákup ve slevě. |\n"
            "| **Impulzivní nákup** | Rychlý nákup bez delšího plánování. | Sladkost u pokladny, kosmetika v akci, „poslední kus“ na e-shopu. |"
        )

        st.markdown("#### 3.2.4 Neuromarketing")
        st.write("Neuromarketing zkoumá, jak na zákazníka působí podněty jako barvy, hudba, vůně, uspořádání prodejny, obal, slova, obrázky nebo rozložení webu. Vychází z poznatků psychologie a neurověd, ale v praxi se často používá jednoduše jako práce se smysly a pozorností.")
        st.write("**Příklady neuromarketingu:** Příjemná vůně v obchodě, hudba zpomalující tempo nakupování, červená barva u slev, velké fotky jídla v aplikaci, tlačítko „Koupit“ na výrazném místě nebo obal, který působí prémiově.")

        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 12: Psychologie a Nákupní cesta tvého zákazníka</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"]("6.3.2", "1. Popiš nákupní cestu zákazníka: Jaký spouštěč ho přiměje hledat produkt a jak o něj pečuješ po nákupu?", "6", st.session_state.get("ulozene_odpovedi", {}))

        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 13: Neuromarketing a Etický kodex projektu</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"]("6.3.3", "1. Jaké neuromarketingové podněty použiješ a jak se vyhneš klamavé reklamě?", "6", st.session_state.get("ulozene_odpovedi", {}))

    # =========================================================================
    # BLOK 12: 3.3 Etika, právo a ochrana
    # =========================================================================
    elif idx == 13:
        st.markdown("## 3. Brand, nákupní psychologie a etika")
        
        st.markdown("### 3.3 Etika, právo a ochrana spotřebitele")
        st.write("Marketing má velký vliv na rozhodování lidí. Proto musí řešit nejen účinnost kampaní, ale také férovost, pravdivost, bezpečnost a ochrana spotřebitele. Cílem etického marketingu není jen „prodat za každou cenu“, ale komunikovat tak, aby zákazník nebyl klamán ani manipulován.")

        st.markdown("#### 3.3.1 Právní rámec reklamy v ČR a EU")
        st.write("Reklama v ČR a EU podléhá právním pravidlům. Patří sem zejména regulace reklamy, pravidla nekalé soutěže, ochrana spotřebitele, povinnost pravdivých informací a pravidla pro označování komerčních sdělení.")
        st.markdown(
            "| Oblast | Co řeší | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Zákon o regulaci reklamy** | Zakazuje některé typy reklamy a stanovuje pravidla pro citlivé oblasti. | Omezení reklamy na alkohol, tabákové výrobky, léčiva nebo hazard. |\n"
            "| **Nekalá soutěž** | Chrání férové soutěžení mezi podnikateli a zákazníky. | Klamavé označení produktu, parazitování na pověsti značky, nepravdivé srovnání. |\n"
            "| **Klamavá reklama** | Reklama nesmí uvádět nepravdivé nebo zavádějící informace. | Produkt tvrdí, že je „100% ekologický“, ale firma to neumí doložit. |\n"
            "| **Srovnávací reklama** | Srovnání s konkurencí je možné jen tehdy, pokud je pravdivé, objektivní a nezavádějící. | Firma může porovnat cenu nebo výkon, pokud používá ověřitelná data. |\n"
            "| **Skrytá reklama** | Komerční sdělení nesmí být maskované jako nezávislý názor. | Influencer propaguje produkt bez označení spolupráce. |"
        )
        st.write("**Označování spolupráce:** Placená spolupráce, barter nebo jiná výhoda musí být jasně označena. Nestačí, aby to bylo schované v hashtazích nebo nejasně naznačené.")

        st.markdown("#### 3.3.2 Ochrana spotřebitele")
        st.write("Spotřebitel má právo na pravdivé, srozumitelné a úplné informace. Firma nesmí zamlčovat podstatné údaje, používat klamavé praktiky nebo vytvářet falešný tlak na nákup.")
        st.markdown(
            "| Právo spotřebitele | Co znamená | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Právo na pravdivé informace** | Zákazník musí vědět, co kupuje, za jakou cenu a za jakých podmínek. | E-shop musí jasně uvést cenu, dopravu, vlastnosti produktu a podmínky nákupu. |\n"
            "| **Reklamace** | Zákazník může uplatnit práva z vadného plnění, pokud produkt nefunguje nebo neodpovídá popisu. | Sluchátka přestanou fungovat a zákazník řeší opravu, výměnu nebo vrácení peněz podle situace. |\n"
            "| **Odstoupení od smlouvy online** | Při nákupu na dálku má spotřebitel typicky právo odstoupit od smlouvy ve lhůtě stanovené zákonem. | Zákazník vrátí zboží koupené přes e-shop, pokud splní zákonné podmínky. |"
        )
        st.write("**Kontrolní orgány pomáhají dohlížet na férové jednání:** Česká obchodní inspekce (ČOI) kontroluje dodržování pravidel ochrany spotřebitele. Rada pro reklamu řeší etickou samoregulaci reklamy a posuzuje stížnosti na nevhodnou nebo neetickou reklamu.")

        st.markdown("#### 3.3.3 Neetické a manipulativní praktiky")
        st.markdown(
            "| Praktika | Co znamená | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Greenwashing** | Firma se tváří ekologičtěji, než skutečně je. | Produkt má zelený obal a slova „eco“, ale bez důkazů nebo reálné změny výroby. |\n"
            "| **Pinkwashing** | Firma využívá podporu určité společenské skupiny nebo tématu hlavně pro image, bez skutečné podpory. | Značka využije duhové logo v kampani, ale dlouhodobě nepodporuje rovnost ani bezpečné prostředí. |\n"
            "| **Dark patterns** | Manipulativní prvky na webech a e-shopech, které tlačí zákazníka k rozhodnutí. | Skryté poplatky, matoucí tlačítka, falešné odpočítávání času, předem zaškrtnuté souhlasy. |\n"
            "| **Falešný sociální důkaz** | Firma vytváří dojem popularity, který není pravdivý. | Falešné recenze, koupené komentáře, „právě nakupuje 25 lidí“, i když to není pravda. |\n"
            "| **Cílení na zranitelné skupiny** | Reklama využívá nižší zkušenosti, strachu nebo zranitelnosti určité skupiny. | Manipulativní reklama na děti, seniory, zadlužené osoby nebo nemocné lidi. |"
        )
        st.write("**Rizikové produkty:** Zvláštní opatrnost vyžaduje reklama na alkohol, hazard, energetické nápoje, kryptoměny, půjčky, doplňky stravy nebo produkty spojené se zdravím. U těchto oblastí může špatná reklama způsobit skutečnou škodu.")

        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 14: Garance ochrany spotřebitele u tvého projektu</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"]("6.3.4", "1. Jak se vyhneš 'Dark patterns' a jaké nastavíš podmínky pro reklamace a vrácení?", "6", st.session_state.get("ulozene_odpovedi", {}))

    # =========================================================================
    # BLOK 13: 3.4 Moderní formy marketingu
    # =========================================================================
    elif idx == 14:
        st.markdown("## 3. Brand, nákupní psychologie a etika")
        
        st.markdown("### 3.4 Moderní formy a trendy v digitálním marketingu")
        st.write("Moderní marketing se stále víc odehrává online. Firmy pracují s daty, algoritmy, obsahem, influencery, automatizací a personalizací. Výhodou digitálního marketingu je přesnější cílení a měření. Rizikem je ztráta soukromí, zahlcení reklamou a manipulace.")

        st.markdown("#### 3.4.1 Digitální / online marketing")
        st.markdown(
            "| Nástroj | Co znamená | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **SEO (Search Engine Optimization)** | Optimalizace obsahu tak, aby se stránka zobrazovala co nejlépe ve vyhledávačích bez přímé platby za klik. | Článek „Jak vybrat běžecké boty“ přivádí zákazníky z Googlu. |\n"
            "| **PPC reklama (Pay Per Click)** | Placená reklama, kde firma obvykle platí za kliknutí nebo jinou akci. | Reklama ve výsledcích vyhledávání nebo placený banner. |\n"
            "| **E-mailový marketing** | Komunikace se zákazníky přes e-mail, často s nabídkami, novinkami nebo edukací. | Newsletter s novou kolekcí, slevou nebo připomenutím opuštěného košíku. |\n"
            "| **Marketingová automatizace** | Automatické posílání zpráv nebo nabídek podle chování zákazníka. | Zákazník si prohlédne produkt a později dostane e-mail s doporučením nebo slevou. |"
        )

        st.markdown("#### 3.4.2 Social media marketing a content marketing")
        st.write("Social Media Marketing (SMM) je marketing na sociálních sítích. Content marketing znamená tvorbu užitečného, zábavného nebo vzdělávacího obsahu, který přitahuje publikum a buduje důvěru.")
        st.markdown(
            "| Pojem | Co znamená | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Přirozený dosah** | Počet lidí, ke kterým se obsah dostane bez placené propagace. | Video se šíří díky sdílení, komentářům a zájmu publika. |\n"
            "| **Placená propagace** | Firma zaplatí platformě za doručení obsahu vybrané cílové skupině. | Reklama na Instagramu cílená na studenty v určitém městě. |\n"
            "| **Algoritmus sociální sítě** | Systém, který rozhoduje, komu se jaký obsah zobrazí. | Platforma zvýhodní video, u kterého lidé dlouho sledují, komentují a sdílejí. |\n"
            "| **Content marketing** | Budování vztahu pomocí obsahu, ne jen přímým prodejem. | Kavárna sdílí tipy na učení, zákulisí přípravy kávy a příběhy studentů. |"
        )
        st.write("**Platformy nejsou stejné:** TikTok se hodí pro krátká dynamická videa, Instagram pro vizuální identitu a komunitu, YouTube pro delší obsah, LinkedIn pro profesní komunikaci a newsletter pro přímý vztah bez závislosti na algoritmu.")

        st.markdown("#### 3.4.3 Influencer marketing a UGC")
        st.write("Influencer marketing využívá důvěru a dosah tvůrců obsahu. Influencer může značce pomoci oslovit konkrétní komunitu, ale spolupráce musí působit důvěryhodně a být jasně označená.")
        st.markdown(
            "| Typ influencera | Jak vypadá | Výhody | Rizika |\n"
            "| :--- | :--- | :--- | :--- |\n"
            "| **Mikro influencer** | Menší publikum, často užší komunita. | Vyšší důvěra, konkrétnější cílová skupina, dostupnější spolupráce. | Menší dosah. |\n"
            "| **Makro influencer** | Velké publikum a vysoký dosah. | Rychlé zviditelnění značky. | Vyšší cena, nižší osobní důvěra, riziko nesouladu s hodnotami značky. |"
        )
        st.write("UGC – User Generated Content znamená obsah vytvořený uživateli: recenze, fotky, videa, unboxing, komentáře nebo doporučení. Funguje jako social proof, tedy sociální důkaz. Lidé často věří více zkušenosti jiných zákazníků než oficiální reklamě.")

        st.markdown("#### 3.4.4 Guerilla marketing a virální marketing")
        st.write("Guerilla marketing je netradiční, často nízkonákladová forma propagace, která se snaží překvapit, pobavit nebo vyvolat silnou reakci. Může probíhat na ulici, ve škole, na akci nebo online.")
        st.write("Virální marketing se snaží vytvořit obsah, který lidé sami šíří dál. Virál může vzniknout díky humoru, překvapení, emoci, kontroverzi nebo vysoké užitečnosti.")
        st.write("**Příklad:** Malá značka nemá rozpočet na televizní reklamu, a tak vytvoří vtipnou instalaci ve městě, kterou lidé fotí a sdílí. Pokud je akce propojená se značkou a cílovou skupinou, může mít velký dopad.")
        st.warning("⚠️ **Pozor:** Šokující kampaň může přinést pozornost, ale také odpor. Virální dosah není automaticky úspěch, pokud poškozuje důvěru nebo nevede k pochopení značky.")

        st.markdown("#### 3.4.5 Nové technologie v marketingu")
        st.write("Nové technologie umožňují marketing více personalizovat, automatizovat a měřit. Zároveň však vyvolávají otázky soukromí, férovosti a transparentnosti.")
        st.markdown(
            "| Technologie | Co umožňuje | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Datová analytika** | Vyhodnocování chování zákazníků a výkonu kampaní. | E-shop sleduje, odkud lidé přicházejí, co si prohlížejí a kde opouštějí košík. |\n"
            "| **Personalizace nabídky** | Přizpůsobení obsahu, produktů nebo ceny konkrétnímu zákazníkovi nebo segmentu. | Doporučení „Mohlo by se vám líbit“ podle předchozího chování. |\n"
            "| **Umělá inteligence v obsahu** | Pomoc s texty, grafikou, videem, nápady a variantami reklam. | AI navrhne popisky produktů, e-mailovou kampaň nebo vizuály pro sociální sítě. |\n"
            "| **Chatboti a zákaznická podpora** | Automatické odpovědi na časté dotazy a pomoc s nákupem. | Chatbot pomůže najít velikost, sledovat objednávku nebo vyřešit reklamaci. |\n"
            "| **AI a deepfake reklama** | Tvorba realistického obrazu, hlasu nebo videa pomocí AI. | Virtuální influencer nebo video s člověkem, který ve skutečnosti danou reklamu nenatočil. |"
        )
        st.write("**Etická otázka AI:** Pokud značka používá umělou inteligenci, měla by dbát na pravdivost, transparentnost, ochranu osobních údajů a férové označování obsahu. Deepfake reklama bez souhlasu může být zásadně neetická i právně problematická.")

        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Cvičení k bloku 3: Etická kampaň</b><br>"
            "Navrhni krátkou kampaň pro svůj projekt:<br>"
            "- Jaké sdělení použiješ?<br>"
            "- Kde bude kampaň probíhat?<br>"
            "- Jak poznáš, že je úspěšná?<br>"
            "- Jak se vyhneš manipulaci, klamavé reklamě a greenwashingu?<br>"
            "- Jak označíš placenou spolupráci, pokud využiješ influencera?<br>"
            "<i>Výstup do projektu: Student vytvoří základ značky, jednoduchou komunikační kampaň a etická pravidla marketingu.</i></div>",
            unsafe_allow_html=True,
        )

        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 15: Digitální a sociální strategie projektu</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"]("6.3.5", "1. Vyber primární sociální síť, typ obsahu, styl influencerů a nápad na Guerilla kampaň.", "6", st.session_state.get("ulozene_odpovedi", {}))

        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 16: Návrh Etické kampaně a dokončení Bloku 3</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"]("6.3.6", "1. Popiš hlavní sdělení etické kampaně, kanály, KPI a jak se vyhneš greenwashingu.", "6", st.session_state.get("ulozene_odpovedi", {}))

    # =========================================================================
    # BLOK 14: 4. Závěrečný výstup
    # =========================================================================
    elif idx == 15:
        st.markdown("## 4. Závěrečný výstup kapitoly a případové studie")

        st.markdown(
            "<div class='box-blue'>"
            "🚀 <b>Finální výstup kapitoly: Od nápadu k reálné kampani</b><br>"
            "V předchozích blocích jsi krok za krokem budoval/a svůj vlastní projekt. Nyní je čas dát všechny dílky skládačky dohromady do jednoho uceleného Projektového pasu a prověřit své znalosti na reálné případové studii z praxe!"
            "</div>",
            unsafe_allow_html=True,
        )

        st.divider()

        st.markdown("### 4.1 Finální projektový výstup")
        st.write("Sestavení kompletního přehledu tvého projektu:")

        st.markdown("#### Finální úkol: Mini projekt od řízení po kampaň")
        st.write("Na konci kapitoly odevzdáš krátkou prezentaci nebo dokument, který obsahuje:")
        st.markdown(
            "1. název projektu,\n"
            "2. problém nebo potřebu, kterou řeší,\n"
            "3. cílovou skupinu,\n"
            "4. týmové role a styl řízení,\n"
            "5. SWOT analýzu,\n"
            "6. marketingový mix 4P,\n"
            "7. základ značky,\n"
            "8. návrh kampaně,\n"
            "9. etická pravidla komunikace,\n"
            "10. krátké zhodnocení rizik."
        )

        st.markdown(
            "| Kritérium | Co se hodnotí |\n"
            "| :--- | :--- |\n"
            "| **🏛️ Management** | Jasný cíl, rozdělení rolí, realistický plán a práce s riziky. |\n"
            "| **🎯 Marketing** | Smysluplná cílová skupina, positioning a propojený marketingový mix. |\n"
            "| **💎 Brand** | Srozumitelná značka, hodnoty a důvěryhodná komunikace. |\n"
            "| **⚖️ Etika** | Schopnost rozpoznat manipulaci, klamavou reklamu, greenwashing a rizika digitální propagace. |\n"
            "| **🎤 Prezentace** | Srozumitelné vysvětlení, konkrétní příklady a schopnost obhájit rozhodnutí. |"
        )

        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Generátor finálního Projektového pasu</b></div>",
            unsafe_allow_html=True,
        )

        with st.expander(
            "📄 Zobrazit kompletní Projektový pas k exportu", expanded=False
        ):
            st.markdown(f"### 🚀 Projektový pas: **{nazev_projektu}**")
            st.markdown("---")
            st.markdown("#### 🏛️ BLOK 1: MANAGEMENT & ORGANIZACE")
            st.markdown(
                "* **Top Management & Vize:** Řízení strategie a směřování projektů.\n"
                "* **Organizační struktura:** Rozdělení funkcí (Výroba, Marketing, Finance).\n"
                "* **SMART Cíl:** Konkrétní, měřitelný a časově ohraničený výsledek.\n"
                "* **SWOT & Plán B:** Identifikovaná rizika a záložní řešení."
            )

            st.markdown("---")
            st.markdown("#### 🎯 BLOK 2: MARKETING & STP")
            st.markdown(
                "* **Cílová skupina (Targeting):** Přesně definovaný segment zákazníků.\n"
                "* **Positioning & USP:** Unikátní prodejní argument, který nás odlišuje od konkurence.\n"
                "* **Marketingový mix 4P:** Product, Price, Place, Promotion."
            )

            st.markdown("---")
            st.markdown("#### 💎 BLOK 3: BRAND & ETIKA")
            st.markdown(
                "* **Příběh značky (Storytelling):** Proč projekt vznikl a jakým hodnotám věří.\n"
                "* **Neuromarketingové prvky:** Zapojení smyslových a psychologických podnětů.\n"
                "* **Etický kodex:** Záruka pravdivosti, označování spoluprací a ochrana spotřebitele."
            )

        st.divider()

        st.markdown(
            "<div class='box-green'>"
            "✅ <b>Co si zapamatovat:</b><br>"
            "Management pomáhá proměnit nápad v organizovanou akci. Marketing pomáhá pochopit zákazníka a doručit mu hodnotu. Brand vytváří důvěru a identitu. Etika připomíná, že pozornost a prodej nejsou jediným cílem — důležité je také férové jednání, pravdivá komunikace a odpovědnost vůči zákazníkům i společnosti."
            "</div>",
            unsafe_allow_html=True,
        )

        st.markdown("### 4.2 Případové studie na závěr kapitoly")
        st.write("Vyzkoušej si roli konzultanta na reálných chybách z praxe:")

        st.markdown("#### 👕 Případová studie 1: Školní merch, který nikdo nekupuje")
        with st.container(border=True):
            st.markdown(
                "**Situace:** Studentský tým chce spustit školní merch. Navrhne mikiny s velkým logem školy, nastaví cenu 850 Kč a objedná 100 kusů dopředu. Po měsíci se prodalo jen 18 mikin. Studenti říkají, že jsou mikiny drahé, design je moc „školní“ a nikdo se jich předem neptal, co by skutečně nosili.\n\n"
                "**Co se v případu objevuje:**\n"
                "* špatně provedený nebo úplně chybějící marketingový výzkum,\n"
                "* nejasná cílová skupina,\n"
                "* slabý positioning,\n"
                "* problém v marketingovém mixu:\n"
                "  * Product: design neodpovídá vkusu studentů,\n"
                "  * Price: cena neodpovídá ochotě platit,\n"
                "  * Place: prodej jen přes školní nástěnku nestačí,\n"
                "  * Promotion: komunikace nevysvětluje hodnotu produktu,\n"
                "* riziko špatného plánování a zásob v managementu."
            )
            if "vykresli_otazku_fn" in st.session_state:
                st.session_state["vykresli_otazku_fn"](
                    "6.4.1",
                    "Případová studie 1 (Školní merch): 1. Navrhni, jaký marketingový výzkum měl tým udělat před objednávkou. 2. Urči cílový segment a možný positioning merche. 3. Uprav 4P tak, aby měl projekt větší šanci uspět. 4. Navrhni, jak by tým mohl snížit riziko neprodaných zásob.",
                    "6",
                    st.session_state.get("ulozene_odpovedi", {}),
                )

        st.divider()
        st.markdown("#### ☕ Případová studie 2: Kavárna u školy a boj o pozornost")
        with st.container(border=True):
            st.markdown(
                "**Situace:** U školy vznikne malá kavárna. Majitel chce oslovit studenty, ale konkurence v okolí je silná. Kavárna má dobré nápoje, ale nízkou návštěvnost. Po analýze zjistí, že studenti chtějí místo, kde se dá učit, nabít telefon, sedět s kamarády a koupit si cenově dostupné menší nápoje.\n\n"
                "**Co se v případu objevuje:**\n"
                "* práce s potřebami, přáními a poptávkou,\n"
                "* segmentace studentů podle chování a životního stylu,\n"
                "* USP: klidné místo na učení blízko školy,\n"
                "* propojení značky, atmosféry a služby,\n"
                "* možnost využití sociálních sítí, UGC a věrnostního programu,\n"
                "* rozhodování o ceně, distribuci služby a propagaci.\n\n"
                "| Oblast | Možné řešení |\n"
                "| :--- | :--- |\n"
                "| **Product** | Menší studentské nápoje, zásuvky, Wi-Fi, tichý studijní koutek. |\n"
                "| **Price** | Studentská cena, věrnostní kartička, zvýhodněné ranní menu. |\n"
                "| **Place** | Kavárna u školy + možnost předobjednávky přes Instagram nebo jednoduchý formulář. |\n"
                "| **Promotion** | Reels ze zákulisí, studentské recenze, spolupráce se školními projekty. |"
            )
            if "vykresli_otazku_fn" in st.session_state:
                st.session_state["vykresli_otazku_fn"](
                    "6.4.2",
                    "Případová studie 2 (Kavárna): 1. Vytvoř krátkou SWOT analýzu kavárny. 2. Navrhni brand: název, hodnoty, vizuální styl a tón komunikace. 3. Navrhni jednu etickou kampaň na sociální sítě. 4. Vysvětli, jak by kavárna mohla využít UGC bez manipulace.",
                    "6",
                    st.session_state.get("ulozene_odpovedi", {}),
                )

        st.divider()
        st.markdown("#### 📱 Případová studie 3: Influencer propaguje „zázračný“ produkt")
        with st.container(border=True):
            st.markdown(
                "**Situace:** Známý influencer natočí video o doplňku stravy, který má údajně „rychle zlepšit soustředění a energii“. Video působí jako osobní doporučení, ale není jasně označeno jako placená spolupráce. V komentářích se objevují studenti, kteří píší, že si produkt koupí před maturitou. Na webu produktu běží odpočítávání s textem „sleva končí za 10 minut“ a hláška „zbývají poslední 3 kusy“.\n\n"
                "**Co se v případu objevuje:**\n"
                "* skrytá nebo nedostatečně označená reklama,\n"
                "* riziko klamavých zdravotních tvrzení,\n"
                "* cílení na zranitelnou skupinu studentů ve stresu,\n"
                "* dark patterns na webu,\n"
                "* práce s emocemi, autoritou influencera a sociálním důkazem,\n"
                "* otázka odpovědnosti značky i tvůrce obsahu.\n\n"
                "**Etický problém:** Kampaň může být účinná, ale není férová, pokud zamlčuje placenou spolupráci, vyvolává falešný tlak nebo slibuje účinky, které nejsou doložené."
            )
            if "vykresli_otazku_fn" in st.session_state:
                st.session_state["vykresli_otazku_fn"](
                    "6.4.3",
                    "Případová studie 3 (Influencer): 1. Najdi v případu alespoň tři manipulativní nebo neetické prvky. 2. Vysvětli, jak by měla být spolupráce správně označena. 3. Navrhni férovější variantu kampaně. 4. Posuď, jakou roli zde hraje brand loyalty, social proof a nákupní psychologie.",
                    "6",
                    st.session_state.get("ulozene_odpovedi", {}),
                )

        st.divider()
        st.markdown("### 🎓 Závěrečná reflexe celou kapitolou")
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"](
                "6.4.4",
                "Vyber jednu případovou studii a odpověz: Co by měl dobrý manažer rozhodnout? Jak by měl marketér upravit 4P nebo komunikaci? A kde je hranice mezi přesvědčováním a manipulací?",
                "6",
                st.session_state.get("ulozene_odpovedi", {}),
            )

        st.divider()
        st.success(
            "🎉 **GRATULUJEME! Kompletně jsi dokončil/a Kapitolu 6 (Management a Marketing).**"
        )
        
        st.markdown(
            "<p style='text-align: right; color: #94a3b8; font-size: 0.8rem;'>Naposledy aktualizováno: 31. 7. 2026</p>",
            unsafe_allow_html=True
        )
