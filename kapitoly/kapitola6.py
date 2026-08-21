import math
import plotly.graph_objects as go
import streamlit as st


def render():
    # =========================================================================
    # 📌 HLAVIČKA KAPITOLY
    # =========================================================================
    st.markdown(
        "<span class='hero-badge'>Kapitola 6</span>", unsafe_allow_html=True
    )
    st.title("6. Management a marketing")
    st.markdown(
        "<p style='font-size: 1.1rem; color: #64748b; margin-bottom: 1.5rem;'>"
        "Management a marketing nejsou jen poučky z učebnice. Jsou to"
        " dovednosti, které potkáváš každý den: při týmovce ve škole, organizaci"
        " festivalu, sledování influencerů, nákupech na e-shopech i při"
        " přemýšlení, proč věříš jedné značce víc než druhé.</p>",
        unsafe_allow_html=True,
    )

    # 🧠 POINTA KAPITOLY
    with st.container(border=True):
        st.markdown(
            "<div class='box-blue'>"
            "<strong>🧠 Pointa kapitoly:</strong> Dobrý nápad sám o sobě nestačí. Někdo musí určit směr, sestavit tým, rozdělit práci, rozhodovat pod tlakem, pochopit zákazníka a vytvořit nabídku, která dává smysl.<br><br>"
            "• <b>Management</b> řeší, jak věci zorganizovat a dostat nápad do reality.<br>"
            "• <b>Marketing</b> řeší, pro koho tvoříme hodnotu a jak získat jeho pozornost."
            "</div>",
            unsafe_allow_html=True,
        )

    # 🎯 CÍLE KAPITOLY (ROZBALOVACÍ)
    with st.expander(
        "🎯 Co máš po této kapitole ovládnout? (Klikni pro rozbalení)",
        expanded=False,
    ):
        col_c1, col_c2 = st.columns(2)
        with col_c1:
            st.markdown(
                "**🏛️ V bloku Management:**\n"
                "* Vysvětlit podstatu, funkce a pyramidu managementu.\n"
                "* Rozlišit manažerské role, dovednosti a styly řízení.\n"
                "* Sestavit **SWOT analýzu** pro projekt nebo svůj osobní rozvoj.\n"
                "* Řídit rizika, týmovou strukturu a pochopit agilní řízení."
            )
        with col_c2:
            st.markdown(
                "**🎯 V bloku Marketing & Brand:**\n"
                "* Sestavit **STP proces** (Segmentace, Targeting, Positioning).\n"
                "* Sestavit kompletní **Marketingový mix 4P** (Produkt, Cena, Distribuce, Propagace).\n"
                "* Budovat značku (Brand equity) a svůj vlastní **Personal Brand**.\n"
                "* Odhalit nákupní psychologii, triky e-shopů (**Dark patterns**) a etiku AI reklamy."
            )

    st.divider()

    # =========================================================================
    # 💡 PRAKTICKÁ LINKA: PROJEKT NAPŘÍČ KAPITOLOU
    # =========================================================================
    st.markdown("### 💡 Projekt napříč kapitolou: Vytvoř si vlastní nápad")
    st.write(
        "Teorie bez praxe je k ničemu. V této kapitole si vybereš **jeden"
        " mikro-projekt**, který budeš postupně rozvíjet v každém bloku. Na"
        " konci kapitoly budeš mít kompletní podklady pro svůj vlastní startup"
        " nebo akční plán!"
    )

    # Interaktivní výběr a konfigurátor projektu
    with st.container(border=True):
        st.markdown(
            "<div class='box-purple'>🚀 <b>Inkubátor projektů: Zvol si své"
            " téma</b></div>",
            unsafe_allow_html=True,
        )

        typ_projektu = st.selectbox(
            "Vyber si projekt, na kterém chceš pracovat:",
            [
                "🎒 Školní merch / značka udržitelného oblečení",
                "🎪 Školní festival, turnaj nebo maturitní ples",
                "☕ Lokální kavárna, food truck nebo pop-up bistro",
                "📱 Mobilní aplikace nebo digitální služba pro studenty",
                "🎙️ Školní podcast, YouTube kanál nebo TikTok profil",
                "🌱 Nezisková kampaň / charitativní projekt",
                (
                    "💼 Osobní značka (Personal brand) na LinkedInu /"
                    " Instagramu"
                ),
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
            "**Blok 1: Management**\nDoplníš týmové role, styl řízení, plán,"
            " rizika a SWOTku."
        )
        c_p2.warning(
            "**Blok 2: Marketing**\nUrčíš cílovku (STP) a nastavíš marketingový"
            " mix 4P."
        )
        c_p3.success(
            "**Blok 3: Brand & Etika**\nVytvoříš identitu značky, logo a"
            " etickou kampaň."
        )

        st.markdown(
            f"<div style='background-color: #f8fafc; padding: 12px;"
            " border-radius: 8px; border: 1px dashed #cbd5e1; text-align: center;"
            " margin-top: 10px;'>📌 <b>Aktivní projektový pas:</b> <span"
            f" style='color: #8b5cf6; font-weight: bold;'>{nazev_projektu}</span></div>",
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
    # 📌 JEDNOTNÁ NABÍDKA PODKAPITOL (NAVIGACE KAPITOLOU 6)
    # =========================================================================
    section_options_6 = [
        "1. Management – Jak z chaosu udělat fungující firmu",
        "2. Marketing – Hra o pozornost a marketingový mix",
        "3. Brand, nákupní psychologie a etika",
        "4. Závěrečný výstup kapitoly a případové studie",
    ]

    st.markdown(
        "📌 <strong>Přechod na podkapitolu:</strong>", unsafe_allow_html=True
    )
    selected_section_6 = st.selectbox(
        "Přechod na podkapitolu:",
        section_options_6,
        index=0,
        label_visibility="collapsed",
        key="k6_section_select",
    )

    # =========================================================================
    # SEKCE 1: MANAGEMENT – JAK Z CHAOSU UDĚLAT FUNGUJÍCÍ FIRMU
    # =========================================================================
    if selected_section_6 == section_options_6[0]:
        st.markdown("### 1. Management – Jak z chaosu udělat fungující firmu")

        st.markdown(
            "<div class='box-blue'>"
            "🏗️ <b>Moderní hook:</b> <i>„Boss vs. Leader: Proč už nikdo nechce pracovat pro šéfa z minulého století?“</i><br>"
            "Management není jen kontrolování lidí. Je to schopnost nastavit směr, rozdělit práci, vést tým, řešit konflikty, rozhodovat se v nejistotě a udržet projekt při životě."
            "</div>",
            unsafe_allow_html=True,
        )

        st.divider()

        # PODKAPITOLA 1.1
        st.markdown("#### 1.1 Podstata a význam managementu")
        st.write(
            "Management znamená **řízení organizace nebo projektu tak, aby"
            " bylo dosáhnuto stanovených cílů**. Často se říká, že management je"
            " *proces dosahování cílů prostřednictvím činnosti jiných lidí*. Manažer"
            " tedy nemusí dělat všechno sám – jeho úkolem je nastavit směr,"
            " rozdělit práci, motivovat tým, rozhodovat a kontrolovat výsledky."
        )

        st.markdown(
            "<div class='box-yellow'>"
            "🧠 <b>Jednoduše:</b> Management je schopnost proměnit chaos v plán, plán v konkrétní úkoly a úkoly ve výsledek."
            "</div>",
            unsafe_allow_html=True,
        )

        st.write(
            "Management se objevuje všude, kde lidé spolupracují: ve firmě, škole, neziskovce, sportovním týmu, startupu, nemocnici, restauraci i při organizaci studentského plesu. Čím složitější je projekt, tím důležitější je řízení času, lidí, peněz, informací a rizik."
        )

        st.markdown("##### 👥 Kdo je kdo v ekonomickém světě? (Rozlišení rolí)")
        
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
            "<div class='box-purple'>🕹️ <b>Trenažér rolí: Poznáš, kdo je"
            " kdo?</b></div>",
            unsafe_allow_html=True,
        )
        st.write("Přečti si následující příběh a urči správnou kombinaci rolí:")

        with st.container(border=True):
            st.write(
                "👤 **Příběh:** *Sára založila vlastní značku udržitelné kosmetiky, investovala do ní své úspory (vlastní 100 % firmy) a zároveň sama řídí tým 5 vývojářů a markeťáků.* Jaké všechny role Sára v tuto chvíli má?"
            )

            sara_role = st.radio(
                "Vyber správnou odpověď:",
                [
                    "Vyber odpověď...",
                    "A) Je pouze zaměstnankyní své vlastní firmy.",
                    "B) Je zároveň Podnikatelka, Vlastník i Manažerka.",
                    "C) Je pouze Podnikatelka, řízení lidi pod ni nespadá.",
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

        st.divider()

        # PODKAPITOLA 1.1.1
        st.markdown("#### 1.1.1 Úrovně managementu: Pyramida řízení")
        st.write("Ve větších organizacích existují různé úrovně řízení. Každá řeší jiný typ rozhodnutí.")

        st.markdown(
            "| Úroveň managementu | Co řeší | Příklad | Typická otázka |\n"
            "| :--- | :--- | :--- | :--- |\n"
            "| **Vrcholový management (Top management)** | Dlouhodobý směr, strategii, zásadní rozhodnutí, odpovědnost za celou organizaci. | CEO, generální ředitel, ředitel školy, představenstvo. | Kam má organizace směřovat za 3–5 let? |\n"
            "| **Střední management (Middle management)** | Převádí strategii do plánů oddělení, koordinuje týmy a kontroluje výsledky. | Vedoucí marketingu, vedoucí výroby, manažer závodu, zástupce ředitele. | Jak splníme cíle v našem oddělení? |\n"
            "| **Liniový management (First-line management)** | Řídí každodenní práci lidí v provozu nebo konkrétním týmu. | Mistr ve výrobě, vedoucí směny, team leader, vedoucí brigádníků. | Kdo dnes co udělá a jak poznáme, že je práce hotová? |"
        )

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

        st.divider()

        # WORKBOOK KROK 1
        st.markdown(
            "<div class='box-yellow'>📝 <b>Projektový pas – Krok 1: Rozdělení rolí v tvém projektu</b></div>",
            unsafe_allow_html=True,
        )
        st.write("Vrať se ke svému projektu zvolenému v úvodu kapitoly a nastav pro něj základní řídící strukturu:")

        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"]("6.1.1", "1. Kdo bude v tvém projektu zastávat roli Top managementu (vize a strategie)?", "6", st.session_state.get("ulozene_odpovedi", {}))
            st.session_state["vykresli_otazku_fn"]("6.1.2", "2. Jaká oddělení / Middle management budeš v projektu potřebovat?", "6", st.session_state.get("ulozene_odpovedi", {}))
            st.session_state["vykresli_otazku_fn"]("6.1.3", "3. Jaké hlavní úkoly bude muset řešit liniový management v běžném dni?", "6", st.session_state.get("ulozene_odpovedi", {}))

        # PODKAPITOLA 1.2
        st.divider()
        st.markdown("#### 1.2 Základní manažerské funkce: Proces řízení")
        st.write("Manažerská práce se často popisuje jako soubor čtyř navazujících funkcí: plánování, organizování, vedení lidí a kontrola. Nejde o jednorázové kroky, ale o cyklus.")

        st.markdown(
            "| Funkce | Co znamená | Otázka pro manažera |\n"
            "| :--- | :--- | :--- |\n"
            "| **Plánování** | Stanovení cílů a cest, jak jich dosáhnout. | Čeho chceme dosáhnout a jak se tam dostaneme? |\n"
            "| **Organizování** | Rozdělení práce, pravomocí, odpovědnosti a zdrojů. | Kdo co udělá, s čím a do kdy? |\n"
            "| **Vedení lidí** | Motivace, komunikace, koordinace a řešení konfliktů. | Jak zajistíme, aby tým chtěl a mohl dobře pracovat? |\n"
            "| **Kontrola** | Měření výsledků, porovnání s plánem a nápravná opatření. | Splnili jsme cíl? Pokud ne, co změníme? |"
        )

        # 1.2.1
        st.markdown("##### 1.2.1 Plánování a SMART cíl")
        st.write("Plánování znamená určit, čeho chce organizace dosáhnout, proč je to důležité a jakými kroky se k cíli dostane.")
        
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
            st.write("**Předělej špatný cíl na SMART cíl:**")
            st.caption("🔴 *Špatný cíl:* 'Chceme mít úspěšný školní merch.'")

            c_smart1, c_smart2, c_smart3 = st.columns(3)
            s_ks = c_smart1.number_input("Kolik kusů chceme prodat?:", min_value=10, value=80, step=10, key="k6_1_2_ks")
            s_marze = c_smart2.number_input("Minimální zisk/marže na kus (Kč):", min_value=50, value=120, step=10, key="k6_1_2_marze")
            s_termin = c_smart3.date_input("Termín dokončení akce:", key="k6_1_2_termin")

            smart_text = f"Do {s_termin.strftime('%d. %m. %Y')} prodáme alespoň {s_ks} kusů mikin studentům 2.–4. ročníku s minimální marží {s_marze} Kč na kus."
            st.success(f"🟢 **Tvůj vygenerovaný SMART cíl:** *„{smart_text}“*")

        # 1.2.2 ORGANIZOVÁNÍ
        st.markdown("##### 1.2.2 Organizování a Pravomoc vs. Odpovědnost")
        st.write("Organizování znamená vytvořit strukturu, ve které lidé vědí, co mají dělat, kdo o čem rozhoduje, kdo komu předává informace a kdo za co odpovídá.")
        
        st.markdown(
            "<div class='box-yellow'>"
            "⚖️ <b>Základní rovnováha managementu:</b><br>"
            "• <b>Pravomoc:</b> Právo rozhodovat nebo zadávat úkoly.<br>"
            "• <b>Odpovědnost:</b> Povinnost nést důsledky za výsledek.<br>"
            "<i>Problém vzniká, když má člověk odpovědnost, ale nemá dostatečnou pravomoc — například má zařídit akci, ale nesmí rozhodnout o rozpočtu.</i>"
            "</div>",
            unsafe_allow_html=True,
        )

        # 1.2.3 VEDENÍ LIDÍ
        st.markdown("##### 1.2.3 Vedení lidí a Maslowova pyramida potřeb")
        st.write("Vedení lidí znamená ovlivňovat tým tak, aby lidé rozuměli cíli, chtěli na něm pracovat a měli podmínky k dobrému výkonu. Dobrý manažer neřeší jen úkoly, ale také motivaci, komunikaci, atmosféru a konflikty.")
        
        st.markdown(
            "| Pojem | Co znamená | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Motivace** | Vnitřní důvod, proč člověk něco dělá. | Student chce vést tým, protože ho baví organizovat akce a učit se leadership. |\n"
            "| **Stimulace** | Vnější podnět nebo odměna, která podporuje určité chování. | Odměna, bonus, pochvala, certifikát, volno, soutěž. |"
        )

        st.write("Abraham Maslow popsal lidské potřeby jako hierarchii. Člověk obvykle nejdřív řeší základní potřeby a teprve potom se může plně soustředit na vyšší potřeby (Fyziologické, Bezpečí, Sociální, Uznání, Seberealizace).")
        st.write("**V managementu:** Pokud se zaměstnanec bojí o místo, je přetížený nebo se v týmu necítí bezpečně, těžko bude kreativní a motivovaný.")

        # WORKBOOK KROK 2
        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 2: SMART cíl a motivace týmu</b></div>",
            unsafe_allow_html=True,
        )

        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"]("6.1.4", "1. Napiš přesný S.M.A.R.T. cíl pro svůj projekt (Co, kolik, do kdy):", "6", st.session_state.get("ulozene_odpovedi", {}))
            st.session_state["vykresli_otazku_fn"]("6.1.5", "2. Jak budeš svůj tým motivovat (kromě peněz) na úrovni Uznání a Seberealizace?", "6", st.session_state.get("ulozene_odpovedi", {}))

        # 1.2.4 KONTROLA
        st.divider()
        st.markdown("#### 1.2.4 Kontrola")
        st.write("Kontrola neznamená jen „nachytat někoho při chybě“. Jejím smyslem je zjistit, zda se realita shoduje s plánem, a pokud ne, přijmout nápravná opatření.")
        
        st.markdown(
            "| Typ kontroly | Kdy probíhá | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Předběžná kontrola** | Před zahájením činnosti. | Kontrola rozpočtu, smluv, techniky a povolení před akcí. |\n"
            "| **Průběžná kontrola** | Během činnosti. | Sledování prodeje vstupenek, docházky týmu nebo plnění úkolů v Notionu. |\n"
            "| **Následná kontrola** | Po skončení činnosti. | Vyhodnocení zisku, spokojenosti účastníků a chyb po festivalu. |"
        )

        # PODKAPITOLA 1.3
        st.divider()
        st.markdown("#### 1.3 Osobnost manažera, dovednosti a role")
        
        st.markdown(
            "| Dovednost manažera | Co znamená | Kdy je nejvíc potřeba |\n"
            "| :--- | :--- | :--- |\n"
            "| **Koncepční dovednosti** | Schopnost vidět organizaci jako celek, chápat souvislosti a přemýšlet strategicky. | Hlavně u vrcholového managementu. |\n"
            "| **Lidské / interpersonální dovednosti** | Komunikace, empatie, vedení lidí, vyjednávání, řešení konfliktů. | Na všech úrovních managementu. |\n"
            "| **Technické / odborné dovednosti** | Znalost oboru, procesů, nástrojů a konkrétní práce týmu. | Hlavně u liniového a středního managementu. |"
        )
        
        st.markdown("##### 1.3.1 Role manažera podle Mintzberga")
        st.markdown(
            "| Skupina rolí | Co zahrnuje | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Interpersonální role** | Reprezentant a lídr. Manažer vystupuje jménem organizace a vede lidi. | Ředitel reprezentuje školu na veřejnosti, team leader vede poradu. |\n"
            "| **Informační role** | Sleduje informace, vybírá podstatné zprávy a předává je dál. | Manažer předá týmu změny v harmonogramu nebo výsledky prodeje. |\n"
            "| **Rozhodovací role** | Rozhoduje o změnách, řeší krize, rozděluje zdroje a vyjednává. | Rozhodne, co se škrtne z rozpočtu, když dodavatel zdraží techniku. |"
        )

        # PODKAPITOLA 1.4
        st.divider()
        st.markdown("#### 1.4 Styly řízení")
        st.write("Styl řízení ukazuje, jak manažer pracuje s mocí, odpovědností a zapojením týmu. Neexistuje jeden styl, který by byl nejlepší vždy.")

        st.markdown(
            "| Styl řízení | Jak funguje | Výhody | Rizika |\n"
            "| :--- | :--- | :--- | :--- |\n"
            "| **Autoritativní / autokratický** | Manažer rozhoduje sám, dává jasné pokyny a očekává jejich splnění. | Rychlost, jasná odpovědnost, vhodné v krizích nebo při nízké zkušenosti týmu. | Nižší motivace, strach z chyb, málo nápadů od týmu, riziko toxické kultury. |\n"
            "| **Demokratický / participativní** | Manažer zapojuje tým do rozhodování, podporuje diskusi a deleguje pravomoci. | Vyšší motivace, lepší nápady, větší odpovědnost týmu. | Pomalejší rozhodování, riziko dlouhých debat, nemusí fungovat v akutní krizi. |\n"
            "| **Liberální / laissez-faire** | Manažer nechává týmu velkou volnost a zasahuje minimálně. | Podporuje samostatnost, kreativitu a odpovědnost zkušených lidí. | Chaos, nejasné priority, slabá kontrola, problémy u nezkušeného týmu. |"
        )

        # WORKBOOK KROK 3
        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 3: Styl řízení a kontrolní mechanizmus</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"]("6.1.6", "1. Jaký styl řízení zvolíš pro svůj projekt a proč?", "6", st.session_state.get("ulozene_odpovedi", {}))
            st.session_state["vykresli_otazku_fn"]("6.1.7", "2. Jak nastavíš PŘEDBĚŽNOU kontrolu pro svůj projekt?", "6", st.session_state.get("ulozene_odpovedi", {}))

        # PODKAPITOLA 1.5
        st.divider()
        st.markdown("#### 1.5 Organizační struktury firem")
        st.write("Organizační struktura je způsob, jakým je firma nebo instituce vnitřně uspořádána. Ukazuje, kdo komu odpovídá, jak jsou rozdělené útvary, kudy tečou informace a kdo má pravomoc rozhodovat.")

        st.markdown("##### 1.5.1 Formální a neformální struktura")
        st.markdown(
            "| Typ struktury | Co znamená | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Formální struktura** | Oficiálně dané vztahy, pozice, pravomoci a odpovědnosti. | Organigram školy, popis pracovních pozic, vedoucí oddělení. |\n"
            "| **Neformální struktura** | Přirozené vztahy, vliv a neoficiální autority mezi lidmi. | Člověk, za kterým všichni chodí pro radu, i když není vedoucí. |"
        )

        st.markdown("##### 1.5.2 Základní typy organizačních struktur")
        st.markdown(
            "| Typ struktury | Jak funguje | Výhoda | Riziko |\n"
            "| :--- | :--- | :--- | :--- |\n"
            "| **Liniová** | Jasná hierarchie: jeden podřízený má jednoho přímého nadřízeného. | Přehlednost, jasné pravomoci a odpovědnost. | Může být nepružná a závislá na rozhodnutí shora. |\n"
            "| **Štábní / liniově-štábní** | Linioví vedoucí rozhodují, ale pomáhají jim odborné poradní útvary. | Manažer má odbornou podporu například v právu, HR nebo financích. | Štáb radí, ale nemusí nést přímou odpovědnost za realizaci. |\n"
            "| **Funkcionální** | Firma je členěná podle odborných funkcí: marketing, finance, výroba, HR, IT. | Specializace a odbornost jednotlivých oddělení. | Oddělení mohou pracovat v „silech“ a málo spolu komunikovat. |\n"
            "| **Maticová** | Kombinuje funkční řízení a projektové týmy. Člověk může mít dva nadřízené. | Vhodná pro projekty, inovace a spolupráci napříč firmou. | Dvojí podřízenost může vést ke konfliktům priorit. |"
        )

        st.markdown("##### 1.5.3 Rozpětí řízení")
        st.markdown(
            "| Typ rozpětí | Jak vypadá | Výhody | Rizika |\n"
            "| :--- | :--- | :--- | :--- |\n"
            "| **Úzké rozpětí řízení** | Vedoucí má málo přímých podřízených, organizace má více úrovní. | Více kontroly, bližší vedení, vhodné pro složité nebo rizikové úkoly. | Více hierarchie, pomalejší komunikace, vyšší náklady. |\n"
            "| **Široké rozpětí řízení** | Vedoucí má hodně přímých podřízených, organizace má méně úrovní. | Rychlejší komunikace, větší samostatnost, plošší struktura. | Manažer nemusí stíhat podporu a kontrolu všech lidí. |"
        )

        # WORKBOOK KROK 4
        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 4: Organizační mapa tvého projektu</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"]("6.1.8", "1. Jaký typ organizační struktury se nejlépe hodí pro tvůj projekt a jaké zvolíš rozpětí řízení?", "6", st.session_state.get("ulozene_odpovedi", {}))

        # PODKAPITOLA 1.6
        st.divider()
        st.markdown("#### 1.6 Rozhodování a analytické metody")
        st.write("Dobré rozhodování není jen pocit. Opírá se o informace, varianty a vyhodnocení důsledků.")

        st.markdown("##### 1.6.1 SWOT analýza")
        st.markdown(
            "| Část SWOT | Prostředí | Co znamená | Otázka |\n"
            "| :--- | :--- | :--- | :--- |\n"
            "| **S — Strengths / Silné stránky** | Vnitřní prostředí | V čem jsme dobří a o co se můžeme opřít. | Co nám jde lépe než ostatním? |\n"
            "| **W — Weaknesses / Slabé stránky** | Vnitřní prostředí | Co nás brzdí nebo oslabuje. | Kde máme mezery? |\n"
            "| **O — Opportunities / Příležitosti** | Vnější prostředí | Co se děje kolem nás a můžeme toho využít. | Jaký trend nebo změna nám může pomoct? |\n"
            "| **T — Threats / Hrozby** | Vnější prostředí | Co nás může ohrozit. | Co se může pokazit nebo kdo nás může předběhnout? |"
        )

        st.markdown("##### 1.6.2 Základy řízení rizik")
        st.markdown(
            "| Krok | Otázka | Příklad pro školní akci |\n"
            "| :--- | :--- | :--- |\n"
            "| **Identifikace rizika** | Co se může pokazit? | Nepřijde dost lidí, onemocní moderátor, selže technika. |\n"
            "| **Vyhodnocení rizika** | Jak pravděpodobné to je a jak velký dopad to bude mít? | Selhání mikrofonu má vysoký dopad, ale dá se snadno zálohovat. |\n"
            "| **Prevence** | Co uděláme, aby riziko nenastalo? | Technická zkouška den předem, předprodej vstupenek, jasný harmonogram. |\n"
            "| **Záložní plán / Plan B** | Co uděláme, když riziko nastane? | Náhradní mikrofon, náhradní moderátor, přesun programu dovnitř při dešti. |"
        )

        # WORKBOOK KROK 5
        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 5: SWOT analýza a Plán B tvého projektu</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"]("6.1.9", "Sestav SWOT analýzu svého projektu (Silné, Slabé stránky, Příležitosti, Hrozby) a pojmenuj 1 největší riziko a Plán B.", "6", st.session_state.get("ulozene_odpovedi", {}))

        # PODKAPITOLA 1.7
        st.divider()
        st.markdown("#### 1.7 Moderní přesah: Agilní řízení, remote work a burnout")
        st.write("Současné řízení lidí se posouvá od prostého zadávání úkolů k práci s autonomií, důvěrou, smyslem práce, psychologickým bezpečím a průběžnou zpětnou vazbou.")
        
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

    # =========================================================================
    # SEKCE 2: MARKETING – HRA O POZORNOST A MARKETINGOVÝ MIX
    # =========================================================================
    elif selected_section_6 == section_options_6[1]:
        st.markdown("### 2. Marketing – Hra o pozornost a marketingový mix")

        st.markdown(
            "<div class='box-blue'>"
            "🎯 <b>Moderní hook:</b> <i>„Proč si koupíš boty za 4 000 Kč, když skoro stejný fejk stojí 500 Kč?“</i><br> Marketing není jen reklama. Je to způsob, jak pochopit potřeby lidí, vytvořit hodnotu, odlišit se od konkurence a dostat správnou nabídku ke správnému člověku."
            "</div>",
            unsafe_allow_html=True,
        )

        st.divider()

        # PODKAPITOLA 2.1
        st.markdown("#### 2.1 Podstata a význam marketingu")
        st.write("Marketing je proces, při kterém firma zjišťuje potřeby zákazníků, vytváří pro ně hodnotu a uspokojuje jejich potřeby tak, aby zároveň dosahovala svých cílů. Nejde tedy jen o reklamu.")
        
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

        st.markdown("##### 2.1.1 Vývoj podnikatelských koncepcí")
        st.markdown(
            "| Koncepce | Hlavní myšlenka | Příklad | Riziko |\n"
            "| :--- | :--- | :--- | :--- |\n"
            "| **Výrobní koncepce** | Vyrábět levně, efektivně a ve velkém. Zákazník koupí to, co je dostupné a levné. | Levná základní trička nebo potraviny vyráběné ve velkých sériích. | Firma může podcenit kvalitu, značku a skutečné potřeby zákazníka. |\n"
            "| **Výrobková koncepce** | Důraz na co nejlepší produkt, kvalitu, technické parametry a inovace. | Telefon s výborným fotoaparátem, prémiové sportovní boty, kvalitní notebook. | Firma může vyrábět „dokonalý“ produkt, který lidé nepotřebují nebo si ho nemohou dovolit. |\n"
            "| **Prodejní koncepce** | Hlavní je zákazníka přesvědčit, přemluvit a prodat mu co nejvíc. | Agresivní telefonní nabídky, tlak na okamžitý nákup, „jen dnes“ akce. | Může poškodit důvěru a vést k manipulaci. |\n"
            "| **Marketingová koncepce** | Nejdřív zjistit potřeby zákazníka a potom vytvořit nabídku, která je naplní lépe než konkurence. | E-shop analyzuje chování zákazníků a upraví sortiment, cenu i komunikaci. | Pokud se sledují jen krátkodobá data, firma může přehlédnout etiku nebo dlouhodobou hodnotu. |\n"
            "| **Sociální / etická koncepce** | Firma bere ohled nejen na zisk a zákazníka, ale i na společnost, životní prostředí a dlouhodobý užitek. | Udržitelná móda, férové dodavatelské řetězce, omezení greenwashingu. | Pokud firma jen předstírá odpovědnost, vzniká greenwashing. |"
        )

        # WORKBOOK KROK 6
        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 6: Podstata a koncepce tvého projektu</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"]("6.2.1", "1. Jakou ZÁKLADNÍ POTŘEBU uspokojuje tvůj projekt a jaká podnikatelská koncepce k němu nejlépe sedí?", "6", st.session_state.get("ulozene_odpovedi", {}))

        # PODKAPITOLA 2.2
        st.divider()
        st.markdown("#### 2.2 Marketingový výzkum a analýza trhu")
        
        st.markdown("##### 2.2.1 Zdroje dat")
        st.markdown(
            "| Typ dat | Co znamená | Výhody | Nevýhody |\n"
            "| :--- | :--- | :--- | :--- |\n"
            "| **Primární data** | Nově sesbíraná data přímo pro konkrétní účel výzkumu. | Jsou přesně zaměřená na problém firmy. | Sběr může být dražší a časově náročnější. |\n"
            "| **Sekundární data** | Již existující data, která byla původně sesbírána pro jiný účel. | Jsou rychle dostupná a často levnější. | Nemusí přesně odpovídat aktuálnímu problému. |"
        )

        st.markdown("##### 2.2.2 Metody výzkumu")
        st.markdown(
            "| Metoda | Co zjišťuje | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Kvantitativní výzkum** | Odpovídá hlavně na otázku „kolik?“ Pracuje s větším počtem odpovědí a čísly. | Dotazník mezi 300 studenty: kolik by zaplatili za školní merch? |\n"
            "| **Kvalitativní výzkum** | Odpovídá hlavně na otázku „proč?“ Zkoumá motivace, postoje a emoce. | Hloubkové rozhovory nebo focus group se studenty o tom, proč se jim školní merch líbí nebo nelíbí. |\n"
            "| **Pozorování** | Sleduje skutečné chování lidí, ne jen to, co říkají. | Obchod sleduje, u kterého regálu se lidé zastavují nejdéle. |\n"
            "| **Experiment** | Testuje, jak změna jedné věci ovlivní chování zákazníků. | A/B test: jedna skupina vidí zelené tlačítko „Koupit“, druhá černé. Firma porovná konverze. |"
        )

        # WORKBOOK KROK 7
        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 7: Tvůj marketingový výzkum</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"]("6.2.2", "1. Kde získáš SEKUNDÁRNÍ DATA o tvém trhu a jakou metodu použiješ pro sběr PRIMÁRNÍCH DAT?", "6", st.session_state.get("ulozene_odpovedi", {}))

        # PODKAPITOLA 2.3
        st.divider()
        st.markdown("#### 2.3 STP proces: Segmentace, Cílení (Targeting) a Positioning")
        
        st.markdown("##### 2.3.1 Segmentace trhu")
        st.markdown(
            "| Kritérium segmentace | Co sleduje | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Geografická segmentace** | Místo, region, město, stát, klima nebo typ lokality. | Jiná nabídka kavárny v centru Prahy a jiná v menším městě. |\n"
            "| **Demografická segmentace** | Věk, pohlaví, příjem, vzdělání, rodinná situace nebo povolání. | Kosmetika pro teenagery, bankovní účet pro studenty, pojištění pro rodiny. |\n"
            "| **Psychografická segmentace** | Životní styl, hodnoty, zájmy, osobnost a postoje. | Značka oblečení cílí na lidi, kteří chtějí udržitelnost a minimalismus. |\n"
            "| **Behaviorální segmentace** | Nákupní chování, frekvence užívání, věrnost značce, reakce na slevy. | E-shop rozlišuje nové zákazníky, věrné zákazníky a ty, kteří často opouštějí košík. |"
        )

        st.markdown("##### 2.3.2 Cílení: targeting")
        st.markdown(
            "| Typ cílení | Jak funguje | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Masový marketing** | Firma oslovuje co nejširší trh jednou nabídkou. | Základní potraviny, běžná balená voda, některé produkty denní spotřeby. |\n"
            "| **Koncentrovaný marketing** | Firma se soustředí na jeden vybraný segment a snaží se mu dobře porozumět. | Malá značka sportovního oblečení pro běžce. |\n"
            "| **Nika / níšový marketing** | Firma cílí na úzkou, specifickou skupinu s jasnou potřebou. | Veganské proteinové tyčinky pro sportovce s intolerancí laktózy. |"
        )

        st.markdown("##### 2.3.3 Positioning a USP")
        st.write("Positioning znamená vytvoření jedinečného obrazu značky v mysli zákazníka vůči konkurenci. USP – Unique Selling Proposition znamená unikátní prodejní argument.")
        st.markdown(
            "| Značka / produkt | Možný positioning | Možné USP |\n"
            "| :--- | :--- | :--- |\n"
            "| **Studentská kavárna** | Klidné místo na učení blízko školy. | Káva + tiché studijní místo + studentská sleva. |\n"
            "| **Udržitelný merch** | Školní oblečení, které nevypadá jako reklamní tričko. | Lokální výroba, kvalitní střih a design navržený studenty. |\n"
            "| **Aplikace na učení** | Rychlá příprava na testy bez zahlcení. | Krátké kartičky, gamifikace a opakování podle chyb. |"
        )

        # WORKBOOK KROK 8
        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 8: STP analýza tvého projektu</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"]("6.2.3", "Popiš Cílovou skupinu (Demografické a psychografické údaje) a napiš Unikátní prodejní argument (USP v 1 větě) pro svůj projekt.", "6", st.session_state.get("ulozene_odpovedi", {}))

        # PODKAPITOLA 2.4
        st.divider()
        st.markdown("#### 2.4 Marketingový mix: Klasické 4P")
        
        st.markdown(
            "| 4P | Česky | Hlavní otázka |\n"
            "| :--- | :--- | :--- |\n"
            "| **Product** | Produkt | Co nabízíme a jakou hodnotu to zákazníkovi přináší? |\n"
            "| **Price** | Cena | Kolik to bude stát a jak cena ovlivní vnímání hodnoty? |\n"
            "| **Place** | Distribuce | Kde a jak se produkt dostane k zákazníkovi? |\n"
            "| **Promotion** | Propagace / komunikace | Jak se o nabídce zákazník dozví a proč jí má věřit? |"
        )

        st.markdown("##### 2.4.1 Product / Produkt")
        st.markdown(
            "| Vrstva produktu | Co znamená | Příklad: auto | Příklad: školní merch |\n"
            "| :--- | :--- | :--- | :--- |\n"
            "| **Jádro produktu** | Základní užitek, kvůli kterému zákazník produkt pořizuje. | Potřeba přepravit se z místa na místo. | Oblečení, sounáležitost se školou, identita. |\n"
            "| **Reálný produkt** | Konkrétní podoba produktu: značka, design, kvalita, obal, funkce. | Konkrétní značka auta, výkon, barva, výbava, bezpečnost. | Mikina, materiál, střih, logo, barva, kvalita potisku. |\n"
            "| **Rozšířený produkt** | Doplňkové služby a výhody kolem produktu. | Záruka, servis, financování, dovoz, asistence. | Možnost výměny velikosti, předobjednávka, balení, doručení do školy. |"
        )

        st.markdown(
            "| Fáze (Životní cyklus) | Co se děje | Typická marketingová výzva |\n"
            "| :--- | :--- | :--- |\n"
            "| **Zavádění** | Produkt je nový, lidé ho neznají, prodeje rostou pomalu a náklady na uvedení jsou vysoké. | Vysvětlit, k čemu produkt je, získat první zákazníky a důvěru. |\n"
            "| **Růst** | Produkt získává popularitu, rostou tržby a přichází konkurence. | Odlišit se, posílit značku a zvládnout vyšší poptávku. |\n"
            "| **Zralost** | Trh je nasycený, růst se zpomaluje, konkurence je silná. | Udržet zákazníky, inovovat, pracovat s cenou a věrnostními programy. |\n"
            "| **Pokles** | Prodeje klesají, produkt zastarává nebo ho nahrazují nové technologie a trendy. | Rozhodnout, zda produkt inovovat, stáhnout z trhu nebo nahradit novým. |"
        )

        st.markdown("##### 2.4.2 Price / Cena")
        st.markdown(
            "| Metoda | Jak funguje | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Nákladově orientovaná cena** | Firma spočítá náklady a přidá přirážku nebo požadovaný zisk. | Výroba mikiny stojí 420 Kč, firma přidá marži 180 Kč, cena je 600 Kč. |\n"
            "| **Poptávkově orientovaná cena** | Cena vychází z toho, kolik je zákazník ochoten zaplatit. | Limitovaná edice tenisek se prodává dráž, protože ji lidé silně chtějí. |\n"
            "| **Konkurenčně orientovaná cena** | Firma nastaví cenu podle konkurence na trhu. | Kavárna sleduje ceny podobných kaváren v okolí. |"
        )

        st.markdown(
            "| Strategie | Co znamená | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Skimming** | Vysoká počáteční cena u novinky, později může cena klesat. | Nový telefon nebo herní konzole při uvedení na trh. |\n"
            "| **Penetrační cena** | Nízká počáteční cena pro rychlé získání zákazníků a podílu na trhu. | Nová streamovací služba nabídne první měsíce velmi levně. |\n"
            "| **Slevy** | Dočasné snížení ceny pro podporu nákupu. | Black Friday, studentská sleva, sezónní výprodej. |\n"
            "| **Skonto** | Sleva za rychlou platbu nebo splnění určité platební podmínky. | Firma poskytne odběrateli 2 % slevu, pokud zaplatí fakturu do 10 dnů. |"
        )

        st.markdown("##### 2.4.3 Place / Distribuce")
        st.markdown(
            "| Typ cesty | Jak funguje | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Přímá distribuční cesta** | Výrobce prodává přímo spotřebiteli bez prostředníka. | Tvůrce prodává vlastní e-book přes svůj web. Pekárna prodává pečivo ve vlastní prodejně. |\n"
            "| **Nepřímá distribuční cesta** | Mezi výrobcem a spotřebitelem je zprostředkovatel. | Výrobce nápojů prodává přes velkoobchod a supermarket. |"
        )
        st.markdown(
            "| Zprostředkovatel | Co dělá | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Velkoobchod** | Nakupuje ve velkém a prodává dalším podnikatelům, obchodům nebo institucím. | Velkoobchod dodává nápoje do kaváren a školních bufetů. |\n"
            "| **Maloobchod** | Prodává konečnému spotřebiteli. | Supermarket, drogerie, knihkupectví, e-shop s oblečením. |"
        )

        st.markdown("##### 2.4.4 Promotion / Propagace a komunikační mix")
        st.markdown(
            "| Prvek komunikačního mixu | Co znamená | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Reklama** | Placená, neosobní forma prezentace přes masmédia nebo digitální kanály. | TV spot, billboard, reklama na YouTube, banner, placený příspěvek na Instagramu. |\n"
            "| **Podpora prodeje (Sales promotion)** | Krátkodobé stimuly k okamžitému nákupu. | Slevový kupón, vzorek zdarma, akce 1+1, soutěž, věrnostní program. |\n"
            "| **Public Relations (PR)** | Budování dobrého jména firmy a vztahů s veřejností, médii a komunitou. | Tisková zpráva, rozhovor v médiích, sponzoring, krizová komunikace, charitativní projekt. |\n"
            "| **Osobní prodej (Personal selling)** | Osobní komunikace se zákazníkem tváří v tvář nebo online. | Obchodní zástupce, konzultace v prodejně, B2B jednání, online demo produktu. |\n"
            "| **Přímý marketing (Direct marketing)** | Přímé oslovení konkrétně vybraných zákazníků. | E-mailing, SMS nabídka, telemarketing, adresná zásilka, personalizovaná nabídka v aplikaci. |"
        )

        # WORKBOOK KROK 9
        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 9: Nastavení Produktu, Ceny a Distribuce</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"]("6.2.4", "1. PRODUKT, CENA a DISTRIBUCE – Co tvoří rozšířený produkt, jakou zvolíš cenovou metodu a jakou cestou se dostane k zákazníkovi?", "6", st.session_state.get("ulozene_odpovedi", {}))

        # WORKBOOK KROK 10
        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 10: Komunikační mix a finální rekapitulace 4P</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"]("6.2.5", "1. PROPAGACE – Jaké 2 hlavní nástroje propagace použiješ a využiješ Influencer marketing či UGC?", "6", st.session_state.get("ulozene_odpovedi", {}))

    # =========================================================================
    # SEKCE 3: BRAND, NÁKUPNÍ PSYCHOLOGIE A ETIKA
    # =========================================================================
    elif selected_section_6 == section_options_6[2]:
        st.markdown("### 3. Brand, nákupní psychologie a etika")
        st.markdown(
            "<div class='box-blue'>"
            "🎯 <b>Moderní hook:</b> <i>„Jak tě značky nutí utrácet peníze, které nemáš, za věci, které nepotřebuješ.“</i><br> Marketing pracuje s emocemi, pozorností, důvěrou a identitou. Proto je důležité rozumět nejen tomu, jak značky fungují, ale i tomu, kde končí přesvědčování a začíná manipulace."
            "</div>",
            unsafe_allow_html=True,
        )

        st.markdown("#### 3.1 Značka a budování brandu")
        st.markdown("##### 3.1.1 Anatomie a prvky značky")
        st.markdown(
            "| Prvek značky | Co znamená | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Vizuální identita** | To, co zákazník vidí: název, logo, barvy, typografie, obal, grafický styl. | Minimalistické logo, typická barva obalu, jednotný styl příspěvků na Instagramu. |\n"
            "| **Audio / senzorická identita** | Zvuky, znělky, vůně nebo jiné smyslové prvky spojené se značkou. | Znělka streamovací služby, typická vůně v obchodě, zvuk při zapnutí zařízení. |\n"
            "| **Storytelling** | Příběh značky: proč vznikla, čemu věří a jaký problém chce řešit. | Značka oblečení vypráví příběh lokální výroby a férových podmínek. |\n"
            "| **Mise a vize** | Mise říká, proč značka existuje dnes. Vize ukazuje, kam chce směřovat. | Mise: zpřístupnit kvalitní vzdělávání. Vize: aby se každý student učil podle sebe. |\n"
            "| **Hodnoty značky** | Principy, které značka zastává a podle kterých se rozhoduje. | Udržitelnost, férovost, kreativita, jednoduchost, dostupnost. |"
        )

        st.markdown("##### 3.1.2 Brand equity a brand loyalty")
        st.markdown(
            "| Pojem | Co znamená | Jak se projevuje |\n"
            "| :--- | :--- | :--- |\n"
            "| **Brand equity** | Dodatečná hodnota, kterou značka přináší produktu. | Zákazník je ochoten zaplatit víc za známou a důvěryhodnou značku. |\n"
            "| **Brand loyalty** | Věrnost zákazníka značce. | Opakované nákupy, členství v komunitě, doporučování přátelům. |\n"
            "| **Komunita značky** | Skupina lidí, kteří se kolem značky sdružují a sdílí podobné hodnoty. | Fanoušci sportovní značky, herní komunity, zákazníci lokální kavárny. |"
        )

        # WORKBOOK KROK 11
        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 11: Identita a Příběh tvé značky</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"]("6.3.1", "1. Napiš příběh, misi, hodnoty a vizuální styl své značky (Brand).", "6", st.session_state.get("ulozene_odpovedi", {}))

        st.divider()
        st.markdown("#### 3.2 Nákupní chování a psychologie spotřebitele")
        st.markdown("##### 3.2.1 Proces nákupního rozhodování")
        st.markdown(
            "| Fáze | Co se děje | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **1. Rozpoznání potřeby** | Zákazník si uvědomí problém nebo přání. | Student zjistí, že potřebuje notebook na školu. |\n"
            "| **2. Hledání informací** | Zjišťuje možnosti, čte recenze, ptá se okolí nebo sleduje videa. | Porovnává modely, kouká na YouTube recenze a ptá se spolužáků. |\n"
            "| **3. Hodnocení alternativ** | Porovnává cenu, výkon, značku, design, dostupnost a záruku. | Vybírá mezi levnějším modelem, výkonnějším modelem a známější značkou. |\n"
            "| **4. Nákupní rozhodnutí** | Vybere produkt a provede nákup. | Koupí notebook v e-shopu nebo kamenné prodejně. |\n"
            "| **5. Poprodejní chování** | Po nákupu hodnotí spokojenost. Může přijít nadšení, reklamace nebo pochybnosti. | Říká si, jestli neměl koupit jiný model — tomu se říká kognitivní disonance. |"
        )

        st.markdown("##### 3.2.2 Faktory ovlivňující nákupní chování")
        st.markdown(
            "| Faktor | Co zahrnuje | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Osobní faktory** | Věk, příjem, životní fáze, životní styl, vzdělání a zkušenosti. | Student, rodič malého dítěte a manažer firmy mají jiné nákupní priority. |\n"
            "| **Psychologické faktory** | Vnímání, postoje, motivace, emoce, osobnost a potřeby. | Maslowova pyramida potřeb pomáhá vysvětlit, proč lidé řeší bezpečí, vztahy, uznání i seberealizaci. |\n"
            "| **Sociální faktory** | Rodina, přátelé, vrstevníci, influenceři, celebrity a referenční skupiny. | Teenager si koupí značku, kterou nosí oblíbený tvůrce nebo kamarádi. |\n"
            "| **Kulturní faktory** | Kultura, hodnoty společnosti, tradice, normy a společenský status. | Jiné produkty se prodávají jako symbol statusu, jiné jako praktická volba. |"
        )

        st.markdown("##### 3.2.3 Racionální vs. emoční nákupy")
        st.markdown(
            "| Typ nákupu | Jak vypadá | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Racionální nákup** | Zákazník porovnává fakta, cenu, výkon, recenze a dlouhodobý užitek. | Výběr notebooku podle výkonu, baterie, ceny a záruky. |\n"
            "| **Emoční nákup** | Zákazník nakupuje podle pocitu, identity, značky, nálady nebo sociálního tlaku. | Limitované tenisky, merch oblíbeného tvůrce, impulzivní nákup ve slevě. |\n"
            "| **Impulzivní nákup** | Rychlý nákup bez delšího plánování. | Sladkost u pokladny, kosmetika v akci, „poslední kus“ na e-shopu. |"
        )

        # WORKBOOK KROK 12
        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 12: Psychologie a Nákupní cesta tvého zákazníka</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"]("6.3.2", "1. Popiš nákupní cestu zákazníka: Jaký spouštěč ho přiměje hledat produkt a jak o něj pečuješ po nákupu?", "6", st.session_state.get("ulozene_odpovedi", {}))

        # WORKBOOK KROK 13
        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 13: Neuromarketing a Etický kodex projektu</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"]("6.3.3", "1. Jaké neuromarketingové podněty použiješ a jak se vyhneš klamavé reklamě?", "6", st.session_state.get("ulozene_odpovedi", {}))

        st.divider()
        st.markdown("#### 3.3 Etika, právo a ochrana spotřebitele")
        st.markdown("##### 3.3.1 Právní rámec reklamy v ČR a EU")
        st.markdown(
            "| Oblast | Co řeší | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Zákon o regulaci reklamy** | Zakazuje některé typy reklamy a stanovuje pravidla pro citlivé oblasti. | Omezení reklamy na alkohol, tabákové výrobky, léčiva nebo hazard. |\n"
            "| **Nekalá soutěž** | Chrání férové soutěžení mezi podnikateli a zákazníky. | Klamavé označení produktu, parazitování na pověsti značky, nepravdivé srovnání. |\n"
            "| **Klamavá reklama** | Reklama nesmí uvádět nepravdivé nebo zavádějící informace. | Produkt tvrdí, že je „100% ekologický“, ale firma to neumí doložit. |\n"
            "| **Srovnávací reklama** | Srovnání s konkurencí je možné jen tehdy, pokud je pravdivé, objektivní a nezavádějící. | Firma může porovnat cenu nebo výkon, pokud používá ověřitelná data. |\n"
            "| **Skrytá reklama** | Komerční sdělení nesmí být maskované jako nezávislý názor. | Influencer propaguje produkt bez označení spolupráce. |"
        )

        st.markdown("##### 3.3.2 Ochrana spotřebitele")
        st.markdown(
            "| Právo spotřebitele | Co znamená | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Právo na pravdivé informace** | Zákazník musí vědět, co kupuje, za jakou cenu a za jakých podmínek. | E-shop musí jasně uvést cenu, dopravu, vlastnosti produktu a podmínky nákupu. |\n"
            "| **Reklamace** | Zákazník může uplatnit práva z vadného plnění, pokud produkt nefunguje nebo neodpovídá popisu. | Sluchátka přestanou fungovat a zákazník řeší opravu, výměnu nebo vrácení peněz podle situace. |\n"
            "| **Odstoupení od smlouvy online** | Při nákupu na dálku má spotřebitel typicky právo odstoupit od smlouvy ve lhůtě stanovené zákonem. | Zákazník vrátí zboží koupené přes e-shop, pokud splní zákonné podmínky. |"
        )

        st.markdown("##### 3.3.3 Neetické a manipulativní praktiky")
        st.markdown(
            "| Praktika | Co znamená | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Greenwashing** | Firma se tváří ekologičtěji, než skutečně je. | Produkt má zelený obal a slova „eco“, ale bez důkazů nebo reálné změny výroby. |\n"
            "| **Pinkwashing** | Firma využívá podporu určité společenské skupiny nebo tématu hlavně pro image, bez skutečné podpory. | Značka využije duhové logo v kampani, ale dlouhodobě nepodporuje rovnost ani bezpečné prostředí. |\n"
            "| **Dark patterns** | Manipulativní prvky na webech a e-shopech, které tlačí zákazníka k rozhodnutí. | Skryté poplatky, matoucí tlačítka, falešné odpočítávání času, předem zaškrtnuté souhlasy. |\n"
            "| **Falešný sociální důkaz** | Firma vytváří dojem popularity, který není pravdivý. | Falešné recenze, koupené komentáře, „právě nakupuje 25 lidí“, i když to není pravda. |\n"
            "| **Cílení na zranitelné skupiny** | Reklama využívá nižší zkušenosti, strachu nebo zranitelnosti určité skupiny. | Manipulativní reklama na děti, seniory, zadlužené osoby nebo nemocné lidi. |"
        )

        # WORKBOOK KROK 14
        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 14: Garance ochrany spotřebitele u tvého projektu</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"]("6.3.4", "1. Jak se vyhneš 'Dark patterns' a jaké nastavíš podmínky pro reklamace a vrácení?", "6", st.session_state.get("ulozene_odpovedi", {}))

        st.divider()
        st.markdown("#### 3.4 Moderní formy a trendy v digitálním marketingu")
        st.markdown("##### 3.4.1 Digitální / online marketing")
        st.markdown(
            "| Nástroj | Co znamená | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **SEO (Search Engine Optimization)** | Optimalizace obsahu tak, aby se stránka zobrazovala co nejlépe ve vyhledávačích bez přímé platby za klik. | Článek „Jak vybrat běžecké boty“ přivádí zákazníky z Googlu. |\n"
            "| **PPC reklama (Pay Per Click)** | Placená reklama, kde firma obvykle platí za kliknutí nebo jinou akci. | Reklama ve výsledcích vyhledávání nebo placený banner. |\n"
            "| **E-mailový marketing** | Komunikace se zákazníky přes e-mail, často s nabídkami, novinkami nebo edukací. | Newsletter s novou kolekcí, slevou nebo připomenutím opuštěného košíku. |\n"
            "| **Marketingová automatizace** | Automatické posílání zpráv nebo nabídek podle chování zákazníka. | Zákazník si prohlédne produkt a později dostane e-mail s doporučením nebo slevou. |"
        )

        st.markdown("##### 3.4.2 Social media marketing a content marketing")
        st.markdown(
            "| Pojem | Co znamená | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Přirozený dosah** | Počet lidí, ke kterým se obsah dostane bez placené propagace. | Video se šíří díky sdílení, komentářům a zájmu publika. |\n"
            "| **Placená propagace** | Firma zaplatí platformě za doručení obsahu vybrané cílové skupině. | Reklama na Instagramu cílená na studenty v určitém městě. |\n"
            "| **Algoritmus sociální sítě** | Systém, který rozhoduje, komu se jaký obsah zobrazí. | Platforma zvýhodní video, u kterého lidé dlouho sledují, komentují a sdílejí. |\n"
            "| **Content marketing** | Budování vztahu pomocí obsahu, ne jen přímým prodejem. | Kavárna sdílí tipy na učení, zákulisí přípravy kávy a příběhy studentů. |"
        )

        st.markdown("##### 3.4.3 Influencer marketing a UGC")
        st.markdown(
            "| Typ influencera | Jak vypadá | Výhody | Rizika |\n"
            "| :--- | :--- | :--- | :--- |\n"
            "| **Mikro influencer** | Menší publikum, často užší komunita. | Vyšší důvěra, konkrétnější cílová skupina, dostupnější spolupráce. | Menší dosah. |\n"
            "| **Makro influencer** | Velké publikum a vysoký dosah. | Rychlé zviditelnění značky. | Vyšší cena, nižší osobní důvěra, riziko nesouladu s hodnotami značky. |"
        )

        st.markdown("##### 3.4.5 Nové technologie v marketingu")
        st.markdown(
            "| Technologie | Co umožňuje | Příklad |\n"
            "| :--- | :--- | :--- |\n"
            "| **Datová analytika** | Vyhodnocování chování zákazníků a výkonu kampaní. | E-shop sleduje, odkud lidé přicházejí, co si prohlížejí a kde opouštějí košík. |\n"
            "| **Personalizace nabídky** | Přizpůsobení obsahu, produktů nebo ceny konkrétnímu zákazníkovi nebo segmentu. | Doporučení „Mohlo by se vám líbit“ podle předchozího chování. |\n"
            "| **Umělá inteligence v obsahu** | Pomoc s texty, grafikou, videem, nápady a variantami reklam. | AI navrhne popisky produktů, e-mailovou kampaň nebo vizuály pro sociální sítě. |\n"
            "| **Chatboti a zákaznická podpora** | Automatické odpovědi na časté dotazy a pomoc s nákupem. | Chatbot pomůže najít velikost, sledovat objednávku nebo vyřešit reklamaci. |\n"
            "| **AI a deepfake reklama** | Tvorba realistického obrazu, hlasu nebo videa pomocí AI. | Virtuální influencer nebo video s člověkem, který ve skutečnosti danou reklamu nenatočil. |"
        )

        # WORKBOOK KROK 15
        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 15: Digitální a sociální strategie projektu</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"]("6.3.5", "1. Vyber primární sociální síť, typ obsahu, styl influencerů a nápad na Guerilla kampaň.", "6", st.session_state.get("ulozene_odpovedi", {}))

        # WORKBOOK KROK 16
        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 16: Návrh Etické kampaně a dokončení Bloku 3</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"]("6.3.6", "1. Popiš hlavní sdělení etické kampaně, kanály, KPI a jak se vyhneš greenwashingu.", "6", st.session_state.get("ulozene_odpovedi", {}))

    # =========================================================================
    # SEKCE 4: ZÁVĚREČNÝ VÝSTUP KAPITOLY A PŘÍPADOVÉ STUDIE
    # =========================================================================
    elif selected_section_6 == section_options_6[3]:
        st.markdown("### 4. Závěrečný výstup kapitoly a případové studie")

        st.markdown(
            "<div class='box-blue'>"
            "🚀 <b>Finální výstup kapitoly: Od nápadu k reálné kampani</b><br>"
            "V předchozích blocích jsi krok za krokem budoval/a svůj vlastním projekt. Nyní je čas dát všechny dílky skládačky dohromady do jednoho uceleného Projektového pasu a prověřit své znalosti na reálné případové studii z praxe!"
            "</div>",
            unsafe_allow_html=True,
        )

        st.divider()

        # 4.1 PROJEKTOVÝ PAS
        st.markdown("#### 4.1 Finální projektový výstup")
        st.write("Sestavení kompletního přehledu tvého projektu:")

        st.markdown(
            "| Kritérium | Co se hodnotí |\n"
            "| :--- | :--- |\n"
            "| **🏛️ Management** | Jasný SMART cíl, rozdělení rolí v týmu, realistický plán a práce s riziky (Plán B). |\n"
            "| **🎯 Marketing** | Smysluplně zvolená cílová skupina (STP), originální positioning a propojený marketingový mix 4P. |\n"
            "| **💎 Brand** | Srozumitelný příběh značky, definované hodnoty, vizuální identita a důvěryhodná komunikace. |\n"
            "| **⚖️ Etika & Právo** | Schopnost rozpoznat manipulaci, klamavou reklamu, greenwashing a dodržení právních pravidel. |\n"
            "| **🎤 Prezentace** | Srozumitelné vysvětlení nápadu, konkrétní příklady a schopnost obhájit svá manažerská rozhodnutí. |"
        )

        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Generátor finálního Projektového"
            " pasu</b></div>",
            unsafe_allow_html=True,
        )

        with st.expander(
            "📄 Zobrazit kompletní Projektový pas k exportu", expanded=False
        ):
            st.markdown(f"### 🚀 Projektový pas: **{nazev_projektu}**")
            st.markdown("---")
            st.markdown("##### 🏛️ BLOK 1: MANAGEMENT & ORGANIZACE")
            st.markdown(
                "* **Top Management & Vize:** Řízení strategie a směřování projektů.\n"
                "* **Organizační struktura:** Rozdělení funkcí (Výroba, Marketing, Finance).\n"
                "* **SMART Cíl:** Konkrétní, měřitelný a časově ohraničený výsledek.\n"
                "* **SWOT & Plán B:** Identifikovaná rizika a záložní řešení."
            )

            st.markdown("---")
            st.markdown("##### 🎯 BLOK 2: MARKETING & STP")
            st.markdown(
                "* **Cílová skupina (Targeting):** Přesně definovaný segment zákazníků.\n"
                "* **Positioning & USP:** Unikátní prodejní argument, který nás odlišuje od konkurence.\n"
                "* **Marketingový mix 4P:** Product, Price, Place, Promotion."
            )

            st.markdown("---")
            st.markdown("##### 💎 BLOK 3: BRAND & ETIKA")
            st.markdown(
                "* **Příběh značky (Storytelling):** Proč projekt vznikl a jakým hodnotám věří.\n"
                "* **Neuromarketingové prvky:** Zapojení smyslových a psychologických podnětů.\n"
                "* **Etický kodex:** Záruka pravdivosti, označování spoluprací a ochrana spotřebitele."
            )

        st.divider()

        # 4.2 PŘÍPADOVÉ STUDIE
        st.markdown("#### 4.2 Případové studie na závěr kapitoly")
        st.write("Vyzkoušej si roli konzultanta na reálných chybách z praxe:")

        # PŘÍPADOVÁ STUDIE 1
        st.markdown(
            "##### 👕 Případová studie 1: Školní merch, který nikdo nekupuje"
        )
        with st.container(border=True):
            st.markdown(
                "**Situace:** Studentský tým chce spustit školní merch. Navrhne mikiny s velkým logem školy, nastaví cenu 850 Kč a objedná 100 kusů dopředu. Po měsíci se prodalo jen 18 mikin. Studenti říkají, že jsou mikiny drahé, design je moc „školní“ a nikdo se jich předem neptal, co by skutečně nosili.\n\n"
                "**Co se v případu objevuje:**\n"
                "* špatně provedený nebo úplně chybějící marketingový výzkum,\n"
                "* nejasná cílová skupina,\n"
                "* slabý positioning,\n"
                "* problém v marketingovém mixu: Product (design neodpovídá vkusu), Price (cena neodpovídá ochotě platit), Place (prodej jen přes školní nástěnku nestačí), Promotion (komunikace nevysvětluje hodnotu),\n"
                "* riziko špatného plánování a zásob v managementu."
            )
            if "vykresli_otazku_fn" in st.session_state:
                st.session_state["vykresli_otazku_fn"](
                    "6.4.1",
                    "Případová studie 1 (Školní merch): 1. Jaký MARKETINGOVÝ"
                    " VÝZKUM měl tým udělat? 2. Jak upravit 4P? 3. Jak eliminovat"
                    " riziko zásob?",
                    "6",
                    st.session_state.get("ulozene_odpovedi", {}),
                )

        # PŘÍPADOVÁ STUDIE 2
        st.divider()
        st.markdown(
            "##### ☕ Případová studie 2: Kavárna u školy a boj o pozornost"
        )
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
                    "Případová studie 2 (Kavárna): 1. Vytvoř SWOT analýzu 2."
                    " Navrhni Brand 3. Navrhni 1 etickou kampaň 4. Jak využít"
                    " UGC obsah?",
                    "6",
                    st.session_state.get("ulozene_odpovedi", {}),
                )

        # PŘÍPADOVÁ STUDIE 3
        st.divider()
        st.markdown(
            "##### 📱 Případová studie 3: Influencer propaguje „zázračný“"
            " produkt"
        )
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
                    "Případová studie 3 (Influencer): 1. Pojmenuj 3 neetické"
                    " prvky 2. Jak měla být kampaň správně označena? 3."
                    " Navrhni férovější variantu.",
                    "6",
                    st.session_state.get("ulozene_odpovedi", {}),
                )

        # ZÁVĚREČNÁ REFLEXE KAPITOLY
        st.divider()
        st.markdown("##### 🎓 Závěrečná reflexe celou kapitolou")
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"](
                "6.4.4",
                "Závěrečná reflexe Kapitoly 6: Co by v krizové situaci měl"
                " rozhodnout dobrý manažer, jak by marketér upravil komunikaci"
                " a kde leží hranice mezi přesvědčováním a manipulací?",
                "6",
                st.session_state.get("ulozene_odpovedi", {}),
            )

        st.divider()
        st.success(
            "🎉 **GRATULUJEME! Kompletně jsi dokončil/a Kapitolu 6 (Management a"
            " Marketing).**"
        )
