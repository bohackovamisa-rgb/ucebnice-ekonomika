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
            """
        <div class='box-blue'>
            <strong>🧠 Pointa kapitoly:</strong> Dobrý nápad sám o sobě nestačí. Někdo musí určité směr, sestavit tým, rozdělit práci, rozhodovat pod tlakem, pochopit zákazníka a vytvořit nabídku, která dává smysl.<br><br>
            • <b>Management</b> řeší, jak věci zorganizovat a dostat nápad do reality.<br>
            • <b>Marketing</b> řeší, pro koho tvoříme hodnotu a jak získat jeho pozornost.
        </div>
        """,
            unsafe_allow_html=True,
        )

    # 🎯 CÍLE KAPITOLY (ROZBALOVACÍ)
    with st.expander(
        "🎯 Co máš po této kapitole ovládnout? (Klikni pro rozbalení)",
        expanded=False,
    ):
        col_c1, col_c2 = st.columns(2)
        with col_c1:
            st.markdown("""
            **🏛️ V bloku Management:**
            * Vysvětlit podstatu, funkce a pyramidu managementu.
            * Rozlišit manažerské role, dovednosti a styly řízení.
            * Sestavit **SWOT analýzu** pro projekt nebo svůj osobní rozvoj.
            * Řídit rizika, týmovou strukturu a pochopit agilní řízení.
            """)
        with col_c2:
            st.markdown("""
            **🎯 V bloku Marketing & Brand:**
            * Sestavit **STP proces** (Segmentace, Targeting, Positioning).
            * Sestavit kompletní **Marketingový mix 4P** (Produkt, Cena, Distribuce, Propagace).
            * Budovat značku (Brand equity) a svůj vlastní **Personal Brand**.
            * Odhalit nákupní psychologii, triky e-shopů (**Dark patterns**) a etiku AI reklamy.
            """)

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
        st.markdown(
            "### 1. Management – Jak z chaosu udělat fungující firmu"
        )

        st.markdown(
            """
        <div class='box-blue'>
            🏗️ <b>Moderní hook:</b> <i>„Boss vs. Leader: Proč už nikdo nechce pracovat pro šéfa z minulého století?“</i><br>
            Management není o komandování a razítkování papírů. Je to schopnost určit směr, nadchnout a vést tým, férově rozdělit práci, řešit konflikty, rozhodovat se v nejistotě a udržet projekt při životě.
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.divider()

        # PODKAPITOLA 1.1
        st.markdown("#### 1.1 Podstata a význam managementu")
        st.write(
            "Management znamená **řízení organizace nebo projektu tak, aby"
            " bylo dosáhnuto stanovených cílů**. Často se říká, že management je"
            " *umění dosahovat cílů prostřednictvím činnosti jiných lidí*. Manažer"
            " tedy nemusí dělat všechno sám – jeho úkolem je nastavit směr,"
            " rozdělit práci, motivovat tým, rozhodovat a kontrolovat výsledky."
        )

        st.markdown(
            """
        <div class='box-yellow'>
            🧠 <b>Jednoduše:</b> Management je schopnost proměnit chaos v plán, plán v konkrétní úkoly a úkoly v reálný výsledek.
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.write(
            "Management se objevuje všude, kde lidé na něčem spolupracují: ve"
            " firmě, škole, neziskovce, sportovním týmu, startupu, nemocnici,"
            " restauraci i při organizaci maturitního plesu."
        )

        st.markdown(
            "##### 👥 Kdo je kdo v ekonomickém světě? (Rozlišení rolí)"
        )
        st.write(
            "V praxi se často pletou pojmy jako podnikatel, manažer, vlastník a"
            " zaměstnanec. Jeden člověk přitom může zastávat více rolí najednou!"
        )

        tab_role1, tab_role2, tab_role3, tab_role4 = st.tabs(
            ["👨‍💼 Manažer", "💡 Podnikatel", "🏛️ Vlastník", "🧑‍💻 Zaměstnanec"]
        )

        with tab_role1:
            st.markdown("##### Manažer")
            st.write(
                "**Co dělá:** Řídí lidi, procesy nebo část organizace. Odpovídá"
                " za splnění cílů a efektivitu."
            )
            st.info(
                "📌 **Příklady:** Vedoucí týmu, ředitel školy, manažer"
                " prodejny."
            )

        with tab_role2:
            st.markdown("##### Podnikatel")
            st.write(
                "**Co dělá:** Přichází s nápadem, vyhledává příležitosti na"
                " trhu, nese riziko a chce vytvořit novou hodnotu."
            )
            st.info(
                "📌 **Příklady:** Zakladatel e-shopu, majitel kavárny, startupový"
                " founder."
            )

        with tab_role3:
            st.markdown("##### Vlastník (Investor)")
            st.write(
                "**Co dělá:** Vlastní firmu nebo její podíl (akcie). Dává do ní"
                " kapitál. Nemusí v ní ale vůbec pracovat ani ji denně řídit."
            )
            st.info(
                "📌 **Příklady:** Společník v s.r.o., akcionář, investor z"
                " pořadu typu *Den D* / *Shark Tank*."
            )

        with tab_role4:
            st.markdown("##### Zaměstnanec")
            st.write(
                "**Co dělá:** Vykonává práci podle pracovní smlouvy/dohody a"
                " dostává za ni sjednanou odměnu (mzdu/plat)."
            )
            st.info(
                "📌 **Příklady:** Programátor, grafik, prodavač, účetní,"
                " brigádník."
            )

        st.markdown(
            "<div class='box-purple'>🕹️ <b>Trenažér rolí: Poznáš, kdo je"
            " kdo?</b></div>",
            unsafe_allow_html=True,
        )
        st.write(
            "Přečti si následující příběh a urči správnou kombinaci rolí:"
        )

        with st.container(border=True):
            st.write(
                "👤 **Příběh:** *Sára založila vlastní značku udržitelné"
                " kosmetiky, investovala do ní své úspory (vlastní 100 % firmy)"
                " a zároveň sama řídí tým 5 vývojářů a markeťáků.* Jaké všechny"
                " role Sára v tuto chvíli má?"
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
                    st.success(
                        "✅ **Přesně tak!** Sára přišla s nápadem"
                        " (Podnikatelka), dala do toho peníze a vlastní firmu"
                        " (Vlastník) a zároveň denně vede tým k cílům"
                        " (Manažerka)."
                    )
                else:
                    st.error(
                        "❌ Kdepak! Sára v sobě kombinuje všechny 3 role."
                        " Správná odpověď je B."
                    )
                if (
                    "uloz_odpoved_fn" in st.session_state
                    and sara_role != "Vyber odpověď..."
                ):
                    st.session_state["uloz_odpoved_fn"](
                        "Kapitola 6",
                        "Podkapitola 1.1 - Trenažér rolí",
                        sara_role[:30],
                    )

        st.divider()

        # PODKAPITOLA 1.1.1
        st.markdown("#### 1.1.1 Úrovně managementu: Pyramida řízení")
        st.write(
            "Ve větších firmách a organizacích neřeší všichni manažeři to samé."
            " Řízení se dělí do tří základních úrovní, které tvoří tzv."
            " **Pyramidu řízení**:"
        )

        col_pyr1, col_pyr2, col_pyr3 = st.columns(3)
        with col_pyr1:
            st.markdown(
                """
            <div style="background-color: #fef2f2; padding: 15px; border-left: 5px solid #ef4444; height: 100%;">
                <h5 style="margin-top: 0; color: #b91c1c;">👑 Vrcholový management (Top)</h5>
                <b>Co řeší:</b> Dlouhodobou strategii (3–5 let), vizi, velká rizika a směr celé firmy.<br><br>
                <b>Lidé:</b> CEO, generální ředitel, ředitel školy, představenstvo.<br><br>
                <b>Otázka:</b> <i>Kam má organizace směřovat?</i>
            </div>
            """,
                unsafe_allow_html=True,
            )

        with col_pyr2:
            st.markdown(
                """
            <div style="background-color: #fef3c7; padding: 15px; border-left: 5px solid #f59e0b; height: 100%;">
                <h5 style="margin-top: 0; color: #b45309;">📊 Střední management (Middle)</h5>
                <b>Co řeší:</b> Převádí strategii z vrchu do konkrétních plánů oddělení, koordinuje týmy.<br><br>
                <b>Lidé:</b> Vedoucí marketingu, vedoucí výroby, manažer závodu, zástupce ředitele.<br><br>
                <b>Otázka:</b> <i>Jak splníme cíle v našem úseku?</i>
            </div>
            """,
                unsafe_allow_html=True,
            )

        with col_pyr3:
            st.markdown(
                """
            <div style="background-color: #f0fdf4; padding: 15px; border-left: 5px solid #10b981; height: 100%;">
                <h5 style="margin-top: 0; color: #047857;">🛠️ Liniový management (First-line)</h5>
                <b>Co řeší:</b> Každodenní provoz, konkrétní úkoly, řízení pracovníků 'v první linii'.<br><br>
                <b>Lidé:</b> Mistr ve výrobně, vedoucí směny v McDonald's, team leader brigádníků.<br><br>
                <b>Otázka:</b> <i>Kdo dnes co udělá a jak?</i>
            </div>
            """,
                unsafe_allow_html=True,
            )

        st.markdown(
            "<br><div class='box-purple'>🎪 <b>Simulátor pyramidy: Školní"
            " benefiční festival</b></div>",
            unsafe_allow_html=True,
        )
        st.write(
            "Klikni na úroveň řízení a podívej se, jak se rozhodování projevuje"
            " na reálném projektu:"
        )

        uroven_sim = st.radio(
            "Vyber úroveň řízení pro školní festival:",
            [
                "🔴 Top management (Ředitel školy + Hlavní koordinátor)",
                (
                    "🟡 Middle management (Vedoucí kapel, Vedoucí občerstvení,"
                    " Vedoucí PR)"
                ),
                (
                    "🟢 First-line management (Team leader u vstupu / u stánku s"
                    " pitím)"
                ),
            ],
            key="k6_1_1_sim_uroven",
        )

        if "Top" in uroven_sim:
            st.error(
                "🏛️ **Rozhodnutí Top managementu:** 'Schvalujeme konání festivalu"
                " na 20. června. Cílem je vybrat 100 000 Kč na útulek a získat"
                " pro školu skvělé jméno. Schvalujeme celkový rozpočet 50 000"
                " Kč.'"
            )
        elif "Middle" in uroven_sim:
            st.warning(
                "📊 **Rozhodnutí Middle managementu:** 'Sestavili jsme"
                " harmonogram vystoupení 5 kapel. Vedoucí PR zajistí plakáty na"
                " Instagramu, vedoucí občerstvení domluvil sponzora na nápoje.'"
            )
        else:
            st.success(
                "🛠️ **Rozhodnutí First-line managementu:** 'Ahoj týme! Jirka"
                " bude od 14:00 trhat lístky u brány, Terka bude prodávat párečky"
                " v rohlíku. Zkontrolujte si, že máte dost drobných na"
                " vrácení!'"
            )

        st.divider()

        # WORKBOOK KROK 1
        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 1:"
            " Rozdělení rolí v tvém projektu</b></div>",
            unsafe_allow_html=True,
        )
        st.write(
            "Vrať se ke svému projektu zvolenému v úvodu kapitoly a nastav pro"
            " něj základní řídící strukturu:"
        )

        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"](
                "6.1.1",
                "1. Kdo bude v tvém projektu zastávat roli Top managementu"
                " (vize a strategie)?",
                "6",
                st.session_state.get("ulozene_odpovedi", {}),
            )
            st.session_state["vykresli_otazku_fn"](
                "6.1.2",
                "2. Jaká oddělení / Middle management budeš v projektu"
                " potřebovat?",
                "6",
                st.session_state.get("ulozene_odpovedi", {}),
            )
            st.session_state["vykresli_otazku_fn"](
                "6.1.3",
                "3. Jaké hlavní úkoly bude muset řešit liniový management v"
                " běžném dni?",
                "6",
                st.session_state.get("ulozene_odpovedi", {}),
            )

        # PODKAPITOLA 1.2
        st.divider()
        st.markdown(
            "#### 1.2 Základní manažerské funkce: Proces řízení"
        )
        st.write(
            "Manažerská práce není nahodilé hašení požárů. Je to neustále se"
            " opakující cyklus čtyř navazujících kroků: **Plánování ➔"
            " Organizování ➔ Vedení lidí ➔ Kontrola**."
        )

        col_fnc1, col_fce2, col_fce3, col_fce4 = st.columns(4)
        col_fnc1.info(
            "🎯 **1. Plánování**\nStanovení cílů a cest, jak jich"
            " dosáhnout.\n*(Kam jdeme?)*"
        )
        col_fce2.warning(
            "🏗️ **2. Organizování**\nRozdělení práce, úkolů, pravomocí a"
            " zdrojů.\n*(Kdo co udělá?)*"
        )
        col_fce3.success(
            "💬 **3. Vedení lidí**\nMotivace, komunikace, týmová"
            " atmosféra.\n*(Jak je nadchnout?)*"
        )
        col_fce4.error(
            "🔍 **4. Kontrola**\nMěření výsledků a nápravná"
            " opatření.\n*(Splnili jsme to?)*"
        )

        # 1.2.1
        st.markdown("##### 1.2.1 Plánování a SMART cíl")
        st.write(
            "Plánování dává týmu smysl a směr. Podle časového horizontu"
            " rozlišujeme operativní, taktické a strategické plánování."
        )

        st.markdown(
            "<div class='box-purple'>🎯 <b>Trenažér: Vylaď cíl podle pravidla"
            " S.M.A.R.T.</b></div>",
            unsafe_allow_html=True,
        )
        st.write(
            "Vágně zadaný cíl (*'Chceme prodávat hodně mikin'*) vedoucího i"
            " tým zmate. Správný cíl musí být **S.M.A.R.T.** (Specific,"
            " Measurable, Achievable, Realistic, Time-bound)."
        )

        with st.container(border=True):
            st.write("**Předělej špatný cíl na SMART cíl:**")
            st.caption("🔴 *Špatný cíl:* 'Chceme mít úspěšný školní merch.'")

            c_smart1, c_smart2, c_smart3 = st.columns(3)
            s_ks = c_smart1.number_input(
                "Kolik kusů chceme prodat?:",
                min_value=10,
                value=80,
                step=10,
                key="k6_1_2_ks",
            )
            s_marze = c_smart2.number_input(
                "Minimální zisk/marže na kus (Kč):",
                min_value=50,
                value=120,
                step=10,
                key="k6_1_2_marze",
            )
            s_termin = c_smart3.date_input(
                "Termín dokončení akce:", key="k6_1_2_termin"
            )

            smart_text = (
                f"Do {s_termin.strftime('%d. %m. %Y')} prodáme přesně {s_ks}"
                " kusů školních mikin studentům s minimální marží"
                f" {s_marze} Kč na kus."
            )
            st.success(
                f"🟢 **Tvůj vygenerovaný SMART cíl:** *„{smart_text}“*"
            )

        # 1.2.2 ORGANIZOVÁNÍ
        st.markdown(
            "##### 1.2.2 Organizování a Pravomoc vs. Odpovědnost"
        )
        st.write(
            "Organizování znamená vytvořit jasnou strukturu: určovat pravomoci"
            " a odpovědnost."
        )

        st.markdown(
            """
        <div class='box-yellow'>
            ⚖️ <b>Základní rovnováha managementu:</b><br>
            • <b>Pravomoc:</b> Právo rozhodovat, utrácet peníze a zadávat úkoly.<br>
            • <b>Odpovědnost:</b> Povinnost nést následky a ručit za výsledek.<br>
            <i>Největší past neefektivního manažera? Dát podřízenému 100% odpovědnost za akci, ale nedát mu žádnou pravomoc o ní rozhodnout!</i>
        </div>
        """,
            unsafe_allow_html=True,
        )

        # 1.2.3 VEDENÍ LIDÍ
        st.markdown(
            "##### 1.2.3 Vedení lidí a Maslowova pyramida potřeb"
        )
        st.write(
            "Rozlišujeme **motivaci** (vnitřní touha) a **stimulaci** (vnější"
            " odměny)."
        )

        st.markdown(
            "#### 🔺 1.2.3.1 Maslowova pyramida potřeb v praxi"
        )
        st.write(
            "Psycholog Abraham Maslow ukázal, že lidé mají potřeby uspořádané"
            " do hierarchie."
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
                marker={
                    "color": [
                        "#8b5cf6",
                        "#3b82f6",
                        "#10b981",
                        "#f59e0b",
                        "#ef4444",
                    ]
                },
            )
        )
        fig_maslow.update_layout(
            title="Maslowova pyramida potřeb",
            height=350,
            margin=dict(t=40, b=10, l=10, r=10),
            showlegend=False,
        )
        st.plotly_chart(fig_maslow, use_container_width=True)

        wybrana_uroven = st.selectbox(
            "🔍 Vyber úroveň pyramidy a podívej se, jak ji řeší dobrý"
            " manažer:",
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
            st.error(
                "🍎 **1. Fyziologické potřeby:** Důstojný plat, pitný režim,"
                " přestávka na oběd a bezpečné prostředí."
            )
        elif "2." in wybrana_uroven:
            st.warning(
                "🛡️ **2. Potřeba bezpečí:** Stabilní smlouva, bezpečné"
                " pracoviště bez šikany, jasná pravidla."
            )
        elif "3." in wybrana_uroven:
            st.success(
                "🤝 **3. Sociální potřeby:** Přijetí do týmu, dobrá"
                " atmosféra, neformální teambuildingy."
            )
        elif "4." in wybrana_uroven:
            st.info(
                "🏆 **4. Uznání a respekt:** Pochvala před týmem za dobře"
                " odvedenou práci, povýšení, ocenění."
            )
        else:
            st.markdown(
                "<div class='box-purple'>🚀 <b>5. Seberealizace:</b> Svoboda v"
                " tvoření, smysluplná práce, možnost učit se nové"
                " věci.</div>",
                unsafe_allow_html=True,
            )

        # WORKBOOK KROK 2
        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 2: SMART"
            " cíl a motivace týmu</b></div>",
            unsafe_allow_html=True,
        )

        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"](
                "6.1.4",
                "1. Napiš přesný S.M.A.R.T. cíl pro svůj projekt (Co, kolik, do"
                " kdy):",
                "6",
                st.session_state.get("ulozene_odpovedi", {}),
            )
            st.session_state["vykresli_otazku_fn"](
                "6.1.5",
                "2. Jak budeš svůj tým motivovat (kromě peněz) na úrovni Uznání"
                " a Seberealizace?",
                "6",
                st.session_state.get("ulozene_odpovedi", {}),
            )

        # 1.2.4 KONTROLA
        st.divider()
        st.markdown(
            "#### 1.2.4 Kontrola: Není to slídění, ale navigace"
        )
        st.write(
            "Smyslem kontroly je ověřit, zda se reálný stav shoduje s plánem, a"
            " včas korigovat směr."
        )

        col_kont1, col_kont2 = st.columns([1, 1])
        with col_kont1:
            st.markdown(
                """
            <div style="background-color: #f8fafc; padding: 15px; border-left: 5px solid #3b82f6; border-radius: 4px;">
                <h5 style="margin-top:0; color: #1e40af;">🔍 4 fáze kontrolního procesu</h5>
                1. <b>Stanovení standardů</b><br>
                2. <b>Zjištění skutečnosti</b><br>
                3. <b>Srovnání plánu a reality</b><br>
                4. <b>Nápravné opatření</b>
            </div>
            """,
                unsafe_allow_html=True,
            )

        with col_kont2:
            st.markdown("##### ⏱️ Typy kontroly podle času")
            tab_k1, tab_k2, tab_k3 = st.tabs(
                ["🔮 Předběžná", "⚙️ Průběžná", "🏁 Následná"]
            )
            with tab_k1:
                st.info(
                    "**Předběžná (PŘED):** Kontrola rozpočtu, schválení vzorků"
                    " před tiskem."
                )
            with tab_k2:
                st.warning(
                    "**Průběžná (BĚHEM):** Sledování denních prodejů v e-shopu,"
                    " Trello nástěnka."
                )
            with tab_k3:
                st.success(
                    "**Následná (PO):** Vyhodnocení zisku a zpětná vazba po"
                    " akci."
                )

        # PODKAPITOLA 1.3
        st.divider()
        st.markdown(
            "#### 1.3 Osobnost manažera, dovednosti a role"
        )
        st.write("Manažerské dovednosti: Koncepční, Lidské a Technické.")

        fig_skills = go.Figure()
        fig_skills.add_trace(
            go.Bar(
                y=["Top", "Middle", "First-line"],
                x=[50, 25, 10],
                name="Koncepční",
                orientation="h",
                marker_color="#8b5cf6",
            )
        )
        fig_skills.add_trace(
            go.Bar(
                y=["Top", "Middle", "First-line"],
                x=[40, 50, 40],
                name="Lidské",
                orientation="h",
                marker_color="#3b82f6",
            )
        )
        fig_skills.add_trace(
            go.Bar(
                y=["Top", "Middle", "First-line"],
                x=[10, 25, 50],
                name="Technické",
                orientation="h",
                marker_color="#10b981",
            )
        )
        fig_skills.update_layout(
            barmode="stack",
            title="Poměr manažerských dovedností (%)",
            height=250,
            margin=dict(t=30, b=20, l=10, r=10),
        )
        st.plotly_chart(fig_skills, use_container_width=True)

        # 1.3.1 MINTZBERGOVY ROLE
        st.markdown("##### 1.3.1 Role manažera podle Mintzberga")
        situace_mintz = st.selectbox(
            "Vyber situaci ze dne manažera:",
            [
                (
                    "1. Vybíráš, kterým 3 projektům z deseti přidělíš peníze z"
                    " rozpočtu."
                ),
                "2. Novinář se ptá na oficiální stanovisko vaší firmy.",
                "3. Vypadly servery a musíte okamžitě sehnat náhradní řešení.",
                (
                    "4. Jdeš na kávu se zakladatelem partnerké firmy zjistit"
                    " novinky z trhu."
                ),
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
            st.success(
                "🔎 **Monitor & Spojovatel** (informační/interpersonální role)."
            )

        # PODKAPITOLA 1.4
        st.divider()
        st.markdown(
            "#### 1.4 Styly řízení: Jak pracovat s mocí a týmem"
        )
        st.write("Autoritativní, Demokratický a Liberální (Laissez-faire) styl.")

        with st.form("debata_musk_form"):
            st.write("**Která filozofie řízení je ti bližší a proč?**")
            postoj_styl = st.radio(
                "Vyber svůj postoj:",
                [
                    (
                        "🚀 Dávám přednost autoritativnímu vizionáři (Musk):"
                        " Bez tvrdé ruky a vysokých nároků nevzniknou"
                        " revoluční věci."
                    ),
                    (
                        "🎧 Dávám přednost demokratické/svobodné kultuře"
                        " (Spotify/Google): Nejlepší inovace vznikají v"
                        " prostředí svobody a bezpečí."
                    ),
                    (
                        "⚖️ Záleží na situaci (Situační řízení): V krizích"
                        " autoritativní, při vývoji demokratický."
                    ),
                ],
                key="k6_1_4_postoj",
            )
            if st.form_submit_button("Odeslat a uložit názor 💾"):
                st.success("Tůj postoj byl zaznamenán!")
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"](
                        "Kapitola 6",
                        "Podkapitola 1.4 - Debata Styl řízení",
                        postoj_styl[:30],
                    )

        # WORKBOOK KROK 3
        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 3: Styl"
            " řízení a kontrolní mechanizmus</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"](
                "6.1.6",
                "1. Jaký styl řízení zvolíš pro svůj projekt a proč?",
                "6",
                st.session_state.get("ulozene_odpovedi", {}),
            )
            st.session_state["vykresli_otazku_fn"](
                "6.1.7",
                "2. Jak nastavíš PŘEDBĚŽNOU kontrolu pro svůj projekt?",
                "6",
                st.session_state.get("ulozene_odpovedi", {}),
            )

        # PODKAPITOLA 1.5
        st.divider()
        st.markdown(
            "#### 1.5 Organizační struktury firem: Mapa tvé organizace"
        )
        st.write(
            "Formální vs. neformální struktura a typy organizačních struktur"
            " (Liniová, Štábní, Funkcionální, Maticová)."
        )

        pocet_podrizenych = st.slider(
            "Počet lidí, které přímo řídíš (Rozpětí řízení):",
            min_value=2,
            max_value=25,
            value=5,
            step=1,
            key="k6_1_5_rozpeti",
        )
        if pocet_podrizenych <= 6:
            st.info(
                f"📏 Úzké rozpětí řízení ({pocet_podrizenych} lidí). Vysoká"
                " kontrola, vyšší náklady."
            )
        elif 7 <= pocet_podrizenych <= 12:
            st.success(
                f"⚖️ Vyvážené rozpětí řízení ({pocet_podrizenych} lidí). Ideální"
                " rovnováha."
            )
        else:
            st.warning(
                f"📐 Široké rozpětí řízení ({pocet_podrizenych} lidí). Plochá"
                " struktura, riziko chaosu."
            )

        # WORKBOOK KROK 4
        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 4:"
            " Organizační mapa tvého projektu</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"](
                "6.1.8",
                "1. Jaký typ organizační struktury se nejlépe hodí pro tvůj"
                " projekt a jaké zvolíš rozpětí řízení?",
                "6",
                st.session_state.get("ulozene_odpovedi", {}),
            )

        # PODKAPITOLA 1.6
        st.divider()
        st.markdown(
            "#### 1.6 Rozhodování a analytické metody"
        )
        st.write(
            "1.6.1 SWOT analýza (Strengths, Weaknesses, Opportunities,"
            " Threats) a 1.6.2 Řízení rizik."
        )

        # WORKBOOK KROK 5
        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 5: SWOT"
            " analýza a Plán B tvého projektu</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"](
                "6.1.9",
                "Sestav SWOT analýzu svého projektu (Silné, Slabé stránky,"
                " Příležitosti, Hrozby) a pojmenuj 1 největší riziko a Plán B.",
                "6",
                st.session_state.get("ulozene_odpovedi", {}),
            )

        # PODKAPITOLA 1.7
        st.divider()
        st.markdown(
            "#### 1.7 Moderní přesah: Agilní řízení, remote work a burnout"
        )
        st.write("Scrum, Kanban, OKR, koučování a prevence vyhoření.")

    # =========================================================================
    # SEKCE 2: MARKETING – HRA O POZORNOST A MARKETINGOVÝ MIX
    # =========================================================================
    elif selected_section_6 == section_options_6[1]:
        st.markdown(
            "### 2. Marketing – Hra o pozornost a marketingový mix"
        )

        st.markdown(
            """
        <div class='box-blue'>
            🎯 <b>Moderní hook:</b> Marketing není jen reklama. Je to způsob, jak pochopit, po čem lidé touží, jak vytvořit hodnotu a dostat správnou nabídku ke správnému člověku.
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.divider()

        # PODKAPITOLA 2.1
        st.markdown("#### 2.1 Podstata a význam marketingu")
        st.write(
            "Potřeba (pocit nedostatku) vs. Přání (konkrétní forma) vs. Poptávka"
            " (přání kryté penězi)."
        )

        # WORKBOOK KROK 6
        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 6: Podstata"
            " a koncepce tvého projektu</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"](
                "6.2.1",
                "1. Jakou ZÁKLADNÍ POTŘEBU uspokojuje tvůj projekt a jaká"
                " podnikatelská koncepce k němu nejlépe sedí?",
                "6",
                st.session_state.get("ulozene_odpovedi", {}),
            )

        # PODKAPITOLA 2.2
        st.divider()
        st.markdown(
            "#### 2.2 Marketingový výzkum a analýza trhu"
        )
        st.write(
            "Primární (nová) vs. Sekundární (existující) data. Kvantitativní"
            " vs. Kvalitativní výzkum. A/B testování."
        )

        # WORKBOOK KROK 7
        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 7: Tvůj"
            " marketingový výzkum</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"](
                "6.2.2",
                "1. Kde získáš SEKUNDÁRNÍ DATA o tvém trhu a jakou metodu"
                " použiješ pro sběr PRIMÁRNÍCH DAT?",
                "6",
                st.session_state.get("ulozene_odpovedi", {}),
            )

        # PODKAPITOLA 2.3
        st.divider()
        st.markdown(
            "#### 2.3 STP proces: Segmentace, Cílení (Targeting) a Positioning"
        )
        st.write(
            "S - Segmentace (Geografická, Demografická, Psychografická,"
            " Behaviorální), T - Cílení, P - Positioning & USP."
        )

        # WORKBOOK KROK 8
        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 8: STP"
            " analýza tvého projektu</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"](
                "6.2.3",
                "Popiš Cílovou skupinu (Demografické a psychografické údaje) a"
                " napiš Unikátní prodejní argument (USP v 1 větě) pro svůj"
                " projekt.",
                "6",
                st.session_state.get("ulozene_odpovedi", {}),
            )

        # PODKAPITOLA 2.4
        st.divider()
        st.markdown("#### 2.4 Marketingový mix: Klasické 4P")
        st.write("Product, Price, Place, Promotion.")

        # WORKBOOK KROK 9
        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 9:"
            " Nastavení Produktu, Ceny a Distribuce</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"](
                "6.2.4",
                "1. PRODUKT, CENA a DISTRIBUCE – Co tvoří rozšířený produkt,"
                " jakou zvolíš cenovou metodu a jakou cestou se dostane k"
                " zákazníkovi?",
                "6",
                st.session_state.get("ulozene_odpovedi", {}),
            )

        # WORKBOOK KROK 10
        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 10:"
            " Komunikační mix a finální rekapitulace 4P</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"](
                "6.2.5",
                "1. PROPAGACE – Jaké 2 hlavní nástroje propagace použiješ a"
                " využiješ Influencer marketing či UGC?",
                "6",
                st.session_state.get("ulozene_odpovedi", {}),
            )

    # =========================================================================
    # SEKCE 3: BRAND, NÁKUPNÍ PSYCHOLOGIE A ETIKA
    # =========================================================================
    elif selected_section_6 == section_options_6[2]:
        st.markdown("### 3. Brand, nákupní psychologie a etika")
        st.write(
            "Pochopení budování značky, emocí, nákupního rozhodování,"
            " neuromarketingu, Dark patterns i právního rámce reklamy."
        )

        # WORKBOOK KROK 11
        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 11:"
            " Identita a Příběh tvé značky</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"](
                "6.3.1",
                "1. Napiš příběh, misi, hodnoty a vizuální styl své značky"
                " (Brand).",
                "6",
                st.session_state.get("ulozene_odpovedi", {}),
            )

        # WORKBOOK KROK 12
        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 12:"
            " Psychologie a Nákupní cesta tvého zákazníka</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"](
                "6.3.2",
                "1. Popiš nákupní cestu zákazníka: Jaký spouštěč ho přiměje"
                " hledat produkt a jak o něj pečuješ po nákupu?",
                "6",
                st.session_state.get("ulozene_odpovedi", {}),
            )

        # WORKBOOK KROK 13
        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 13:"
            " Neuromarketing a Etický kodex projektu</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"](
                "6.3.3",
                "1. Jaké neuromarketingové podněty použiješ a jak se vyhneš"
                " klamavé reklamě?",
                "6",
                st.session_state.get("ulozene_odpovedi", {}),
            )

        # WORKBOOK KROK 14
        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 14: Garance"
            " ochrany spotřebitele u tvého projektu</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"](
                "6.3.4",
                "1. Jak se vyhneš 'Dark patterns' a jaké nastavíš podmínky"
                " pro reklamace a vrácení?",
                "6",
                st.session_state.get("ulozene_odpovedi", {}),
            )

        # WORKBOOK KROK 15
        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 15:"
            " Digitální a sociální strategie projektu</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"](
                "6.3.5",
                "1. Vyber primární sociální síť, typ obsahu, styl influencerů"
                " a nápad na Guerilla kampaň.",
                "6",
                st.session_state.get("ulozene_odpovedi", {}),
            )

        # WORKBOOK KROK 16
        st.markdown(
            "<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 16: Návrh"
            " Etické kampaně a dokončení Bloku 3</b></div>",
            unsafe_allow_html=True,
        )
        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"](
                "6.3.6",
                "1. Popiš hlavní sdělení etické kampaně, kanály, KPI a jak se"
                " vyhneš greenwashingu.",
                "6",
                st.session_state.get("ulozene_odpovedi", {}),
            )

    # =========================================================================
    # SEKCE 4: ZÁVĚREČNÝ VÝSTUP KAPITOLY A PŘÍPADOVÉ STUDIE
    # =========================================================================
    elif selected_section_6 == section_options_6[3]:
        st.markdown("### 4. Závěrečný výstup kapitoly a případové studie")

        st.markdown(
            """
        <div class='box-blue'>
            🚀 <b>Finální výstup kapitoly: Od nápadu k reálné kampani</b><br>
            V předchozích blocích jsi krok za krokem budoval/a svůj vlastním projekt. Nyní je čas dát všechny dílky skládačky dohromady do jednoho uceleného Projektového pasu a prověřit své znalosti na reálné případové studii z praxe!
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.divider()

        # 4.1 PROJEKTOVÝ PAS
        st.markdown("#### 4.1 Finální projektový výstup")
        st.write("Sestavení kompletního přehledu tvého projektu:")

        st.markdown(
            """
        | Kritérium | Co se hodnotí |
        | :--- | :--- |
        | **🏛️ Management** | Jasný SMART cíl, rozdělení rolí v týmu, realistický plán a práce s riziky (Plán B). |
        | **🎯 Marketing** | Smysluplně zvolená cílová skupina (STP), originální positioning a propojený marketingový mix 4P. |
        | **💎 Brand** | Srozumitelný příběh značky, definované hodnoty, vizuální identita a důvěryhodná komunikace. |
        | **⚖️ Etika & Právo** | Schopnost rozpoznat manipulaci, klamavou reklamu, greenwashing a dodržení právních pravidel. |
        | **🎤 Prezentace** | Srozumitelné vysvětlení nápadu, konkrétní příklady a schopnost obhájit svá manažerská rozhodnutí. |
        """,
            unsafe_allow_html=True,
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
                "* **Top Management & Vize:** Řízení strategie a směřování"
                " projektu."
            )
            st.markdown(
                "* **Organizační struktura:** Rozdělení funkcí (Výroba,"
                " Marketing, Finance)."
            )
            st.markdown(
                "* **SMART Cíl:** Konkrétní, měřitelný a časově ohraničený"
                " výsledek."
            )
            st.markdown(
                "* **SWOT & Plán B:** Identifikovaná rizika a záložní řešení."
            )

            st.markdown("---")
            st.markdown("##### 🎯 BLOK 2: MARKETING & STP")
            st.markdown(
                "* **Cílová skupina (Targeting):** Přesně definovaný segment"
                " zákazníků."
            )
            st.markdown(
                "* **Positioning & USP:** Unikátní prodejní argument, který nás"
                " odlišuje od konkurence."
            )
            st.markdown(
                "* **Marketingový mix 4P:** Product, Price, Place, Promotion."
            )

            st.markdown("---")
            st.markdown("##### 💎 BLOK 3: BRAND & ETIKA")
            st.markdown(
                "* **Příběh značky (Storytelling):** Proč projekt vznikl a jakým"
                " hodnotám věří."
            )
            st.markdown(
                "* **Neuromarketingové prvky:** Zapojení smyslových a"
                " psychologických podnětů."
            )
            st.markdown(
                "* **Etický kodex:** Záruka pravdivosti, označování spoluprací a"
                " ochrana spotřebitele."
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
                "Studenti objednali 100 mikin na sklad za 850 Kč bez výzkumu."
                " Prodalo se jen 18 ks."
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
                "Kavárna u školy má nízkou návštěvnost. Studenti chtějí studijní"
                " místo, Wi-Fi a levnější nápoje."
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
                "Tiktoker propaguje doplňky stravy bez označení reklamy s"
                " falešnými odpočty času na e-shopu."
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
