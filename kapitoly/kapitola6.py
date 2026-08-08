import streamlit as st
import plotly.graph_objects as go

def render():
    # =========================================================================
    # 📌 HLAVIČKA KAPITOLY
    # =========================================================================
    st.markdown("<span class='hero-badge'>Kapitola 6</span>", unsafe_allow_html=True)
    st.title("6. Management a marketing")
    st.markdown("<p style='font-size: 1.1rem; color: #64748b; margin-bottom: 1.5rem;'>Management a marketing nejsou jen poučky z učebnice. Jsou to dovednosti, které potkáváš každý den: při týmovce ve škole, organizaci festivalu, sledování influencerů, nákupech na e-shopech i při přemýšlení, proč věříš jedné značce víc než druhé.</p>", unsafe_allow_html=True)

    # 🧠 POINTA KAPITOLY
    with st.container(border=True):
        st.markdown("""
        <div class='box-blue'>
            <strong>🧠 Pointa kapitoly:</strong> Dobrý nápad sám o sobě nestačí. Někdo musí určit směr, sestavit tým, rozdělit práci, rozhodovat pod tlakem, pochopit zákazníka a vytvořit nabídku, která dává smysl.<br><br>
            • <b>Management</b> řeší, jak věci zorganizovat a dostat nápad do reality.<br>
            • <b>Marketing</b> řeší, pro koho tvoříme hodnotu a jak získat jeho pozornost.
        </div>
        """, unsafe_allow_html=True)

    # 🎯 CÍLE KAPITOLY (ROZBALOVACÍ)
    with st.expander("🎯 Co máš po této kapitole ovládnout? (Klikni pro rozbalení)", expanded=False):
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
    st.write("Teorie bez praxe je k ničemu. V této kapitole si vybereš **jeden mikro-projekt**, který budeš postupně rozvíjet v každém bloku. Na konci kapitoly budeš mít kompletní podklady pro svůj vlastní star-tup nebo akční plán!")

    # Interaktivní výběr a konfigurátor projektu
    with st.container(border=True):
        st.markdown("<div class='box-purple'>🚀 <b>Inkubátor projektů: Zvol si své téma</b></div>", unsafe_allow_html=True)
        
        typ_projektu = st.selectbox("Vyber si projekt, na kterém chceš pracovat:", [
            "🎒 Školní merch / značka udržitelného oblečení",
            "🎪 Školní festival, turnaj nebo maturitní ples",
            "☕ Lokální kavárna, food truck nebo pop-up bistro",
            "📱 Mobilní aplikace nebo digitální služba pro studenty",
            "🎙️ Školní podcast, YouTube kanál nebo TikTok profil",
            "🌱 Nezisková kampaň / charitativní projekt",
            "💼 Osobní značka (Personal brand) na LinkedInu / Instagramu",
            "✏️ Vlastní nápad (napíšu níže)"
        ])

        if "Vlastní nápad" in typ_projektu:
            nazev_projektu = st.text_input("Napiš název a stručný popis svého vlastního projektu:", value="Můj nový startup")
        else:
            nazev_projektu = typ_projektu.split(" ", 1)[1]

        c_p1, c_p2, c_p3 = st.columns(3)
        c_p1.info("**Blok 1: Management**\nDoplníš týmové role, styl řízení, plán, rizika a SWOTku.")
        c_p2.warning("**Blok 2: Marketing**\nUrčíš cílovku (STP) a nastavíš marketingový mix 4P.")
        c_p3.success("**Blok 3: Brand & Etika**\nVytvoříš identitu značky, logo a etickou kampaň.")

        st.markdown(f"<div style='background-color: #f8fafc; padding: 12px; border-radius: 8px; border: 1px dashed #cbd5e1; text-align: center; margin-top: 10px;'>📌 <b>Aktivní projektový pas:</b> <span style='color: #8b5cf6; font-weight: bold;'>{nazev_projektu}</span></div>", unsafe_allow_html=True)

    st.divider()

    # =========================================================================
    # 📌 JEDNOTNÁ NABÍDKA PODKAPITOL (NAVIGACE KAPITOLOU 6)
    # =========================================================================
    section_options_6 = [
        "1. Management – Jak z chaosu udělat fungující firmu",
        "2. Marketing – Hra o pozornost a marketingový mix",
        "3. Brand, nákupní psychologie a etika",
        "4. Závěrečný výstup kapitoly a případové studie"
    ]

    selected_section_6 = st.selectbox("📌 Přechod na hlavní blok kapitoly:", section_options_6, index=0)
    st.divider()

    # =========================================================================
    # SEKCE 1: MANAGEMENT
    # =========================================================================
    if selected_section_6 == section_options_6[0]:
        st.markdown("### 1. Management – Jak z chaosu udělat fungující firmu")
        st.info("Zde bude pokračovat podkapitola 1.1 Podstata a význam managementu...")

    # =========================================================================
    # SEKCE 2: MARKETING
    # =========================================================================
    elif selected_section_6 == section_options_6[1]:
        st.markdown("### 2. Marketing – Hra o pozornost a marketingový mix")
        st.info("Zde bude pokračovat blok 2. Marketing...")

    # =========================================================================
    # SEKCE 3: BRAND A ETIKA
    # =========================================================================
    elif selected_section_6 == section_options_6[2]:
        st.markdown("### 3. Brand, nákupní psychologie a etika")
        st.info("Zde bude pokračovat blok 3. Brand a etika...")

    # =========================================================================
    # SEKCE 4: ZÁVĚREČNÝ VÝSTUP A STUDIE
    # =========================================================================
    elif selected_section_6 == section_options_6[3]:
        st.markdown("### 4. Závěrečný výstup kapitoly a případové studie")
        st.info("Zde bude zobrazen celkový projektový pas a 3 případové studie...")
# =========================================================================
    # SEKCE 1: MANAGEMENT – JAK Z CHAOSU UDĚLAT FUNGUJÍCÍ FIRMU
    # =========================================================================
    if selected_section_6 == section_options_6[0]:
        st.markdown("### 1. Management – Jak z chaosu udělat fungující firmu")
        
        st.markdown("""
        <div class='box-blue'>
            🏗️ <b>Moderní hook:</b> <i>„Boss vs. Leader: Proč už nikdo nechce pracovat pro šéfa z minulého století?“</i><br>
            Management není o komandování a razítkování papírů. Je to schopnost určit směr, nadchnout a vést tým, férově rozdělit práci, řešit konflikty, rozhodovat se v nejistotě a udržet projekt při životě.
        </div>
        """, unsafe_allow_html=True)

        st.divider()

        # =====================================================================
        # PODKAPITOLA 1.1: PODSTATA A VÝZNAM MANAGEMENTU
        # =====================================================================
        st.markdown("#### 1.1 Podstata a význam managementu")
        st.write("Management znamená **řízení organizace nebo projektu tak, aby bylo dosáhnuto stanovených cílů**. Často se říká, že management je *umění dosahovat cílů prostřednictvím činnosti jiných lidí*. Manažer tedy nemusí dělat všechno sám – jeho úkolem je nastavit směr, rozdělit práci, motivovat tým, rozhodovat a kontrolovat výsledky.")

        st.markdown("""
        <div class='box-yellow'>
            🧠 <b>Jednoduše:</b> Management je schopnost proměnit chaos v plán, plán v konkrétní úkoly a úkoly v reálný výsledek.
        </div>
        """, unsafe_allow_html=True)

        st.write("Management se objevuje všude, kde lidé na něčem spolupracují: ve firmě, škole, neziskovce, sportovním týmu, startupu, nemocnici, restauraci i při organizaci maturitního plesu.")

        st.markdown("##### 👥 Kdo je kdo v ekonomickém světě? (Rozlišení rolí)")
        st.write("V praxi se často pletou pojmy jako podnikatel, manažer, vlastník a zaměstnanec. Jeden člověk přitom může zastávat více rolí najednou!")

        tab_role1, tab_role2, tab_role3, tab_role4 = st.tabs(["👨‍💼 Manažer", "💡 Podnikatel", "🏛️ Vlastník", "🧑‍💻 Zaměstnanec"])

        with tab_role1:
            st.markdown("##### Manažer")
            st.write("**Co dělá:** Řídí lidi, procesy nebo část organizace. Odpovídá za splnění cílů a efektivitu.")
            st.info("📌 **Příklady:** Vedoucí týmu, ředitel školy, manažer pobočky, projektový manažer v IT.")

        with tab_role2:
            st.markdown("##### Podnikatel")
            st.write("**Co dělá:** Přichází s nápadem, vyhledává příležitosti na trhu, nese riziko a chce vytvořit novou hodnotu.")
            st.info("📌 **Příklady:** Zakladatel e-shopu, majitel kavárny, startupový founder.")

        with tab_role3:
            st.markdown("##### Vlastník (Investor)")
            st.write("**Co dělá:** Vlastní firmu nebo její podíl (akcie). Dává do ní kapitál. Nemusí v ní ale vůbec pracovat ani ji denně řídit.")
            st.info("📌 **Příklady:** Společník v s.r.o., akcionář, investor z pořadu typu *Den D* / *Shark Tank*.")

        with tab_role4:
            st.markdown("##### Zaměstnanec")
            st.write("**Co dělá:** Vykonává práci podle pracovní smlouvy/dohody a dostává za ni sjednanou odměnu (mzdu/plat).")
            st.info("📌 **Příklady:** Programátor, grafik, prodavač, účetní, brigádník.")

        st.markdown("<div class='box-purple'>🕹️ <b>Trenažér rolí: Poznáš, kdo je kdo?</b></div>", unsafe_allow_html=True)
        st.write("Přečti si následující příběh a urči správnou kombinaci rolí:")

        with st.container(border=True):
            st.write("👤 **Příběh:** *Sára založila vlastní značku udržitelné kosmetiky, investovala do ní své úspory (vlastní 100 % firmy) a zároveň sama řídí tým 5 vývojářů a markeťáků.* Jaké všechny role Sára v tuto chvíli má?")
            
            sara_role = st.radio("Vyber správnou odpoveď:", [
                "Vyber odpověď...",
                "A) Je pouze zaměstnankyní své vlastní firmy.",
                "B) Je zároveň Podnikatelka, Vlastník i Manažerka.",
                "C) Je pouze Podnikatelka, řízení lidi pod ni nespadá."
            ])

            if "B)" in sara_role:
                st.success("✅ **Přesně tak!** Sára přišla s nápadem (Podnikatelka), dala do toho peníze a vlastní firmu (Vlastník) a zároveň denně vede tým k cílům (Manažerka). Jakmile firma vyroste, může na řízení najmout profesionálního manažera a zůstat jen vlastnicí.")
            elif "A)" in sara_role or "C)" in sara_role:
                st.error("❌ Kdepak! Sára v sobě kombinuje všechny 3 role. Správná odpověď je B.")

        st.divider()

        # =====================================================================
        # PODKAPITOLA 1.1.1: ÚROVNĚ MANAGEMENTU
        # =====================================================================
        st.markdown("#### 1.1.1 Úrovně managementu: Pyramida řízení")
        st.write("Ve větších firmách a organizacích neřeší všichni manažeři to samé. Řízení se dělí do tří základních úrovní, které tvoří tzv. **Pyramidu řízení**:")

        # Vizualizace pyramidy řízení pomocí 3 barevných sloupců/boxů
        col_pyr1, col_pyr2, col_pyr3 = st.columns(3)
        with col_pyr1:
            st.markdown("""
            <div style="background-color: #fef2f2; padding: 15px; border-left: 5px solid #ef4444; height: 100%;">
                <h5 style="margin-top: 0; color: #b91c1c;">👑 Vrcholový management (Top)</h5>
                <b>Co řeší:</b> Dlouhodobou strategii (3–5 let), vizi, velká rizika a směr celé firmy.<br><br>
                <b>Lidé:</b> CEO, generální ředitel, ředitel školy, představenstvo.<br><br>
                <b>Otázka:</b> <i>Kam má organizace směřovat?</i>
            </div>
            """, unsafe_allow_html=True)

        with col_pyr2:
            st.markdown("""
            <div style="background-color: #fef3c7; padding: 15px; border-left: 5px solid #f59e0b; height: 100%;">
                <h5 style="margin-top: 0; color: #b45309;">📊 Střední management (Middle)</h5>
                <b>Co řeší:</b> Převádí strategii z vrchu do konkrétních plánů oddělení, koordinuje týmy.<br><br>
                <b>Lidé:</b> Vedoucí marketingu, vedoucí výroby, manažer závodu, zástupce ředitele.<br><br>
                <b>Otázka:</b> <i>Jak splníme cíle v našem úseku?</i>
            </div>
            """, unsafe_allow_html=True)

        with col_pyr3:
            st.markdown("""
            <div style="background-color: #f0fdf4; padding: 15px; border-left: 5px solid #10b981; height: 100%;">
                <h5 style="margin-top: 0; color: #047857;">🛠️ Liniový management (First-line)</h5>
                <b>Co řeší:</b> Každodenní provoz, konkrétní úkoly, řízení pracovníků 'v první linii'.<br><br>
                <b>Lidé:</b> Mistr ve výrobně, vedoucí směny v Mcdonald's, team leader brigádníků.<br><br>
                <b>Otázka:</b> <i>Kdo dnes co udělá a jak?</i>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br><div class='box-purple'>🎪 <b>Simulátor pyramidy: Školní benefiční festival</b></div>", unsafe_allow_html=True)
        st.write("Klikni na úroveň řízení a podívej se, jak se rozhodování projevuje na reálném projektu:")

        uroven_sim = st.radio("Vyber úroveň řízení pro školní festival:", [
            "🔴 Top management (Ředitel školy + Hlavní koordinátor)",
            "🟡 Middle management (Vedoucí kapel, Vedoucí občerstvení, Vedoucí PR)",
            "🟢 First-line management (Team leader u vstupu / u stánku s pitím)"
        ])

        if "Top" in uroven_sim:
            st.error("🏛️ **Rozhodnutí Top managementu:** 'Schvalujeme konání festivalu na 20. června. Cílem je vybrat 100 000 Kč na útulek a získat pro školu skvělé jméno. Schvalujeme celkový rozpočet 50 000 Kč.'")
        elif "Middle" in uroven_sim:
            st.warning("📊 **Rozhodnutí Middle managementu:** 'Sestavili jsme harmonogram vystoupení 5 kapel. Vedoucí PR zajistí plakáty na Instagramu, vedoucí občerstvení domluvil sponzora na nápoje.'")
        else:
            st.success("🛠️ **Rozhodnutí First-line managementu:** 'Ahoj týme! Jirka bude od 14:00 trhat lístky u brány, Terka bude prodávat párečky v rohlíku. Zkontrolujte si, že máte dost drobných na vrracení!'")

        st.divider()

        # =====================================================================
        # WORKBOOK KROK 1 PRO STUDENTŮV PROJEKT
        # =====================================================================
        st.markdown("<div class='box-yellow'>📝 <b>Projektový pas – Krok 1: Rozdělení rolí v tvém projektu</b></div>", unsafe_allow_html=True)
        st.write("Vrať se ke svému projektu zvolenému v úvodu kapitoly a nastav pro něj základní řídící strukturu:")

        with st.form("form_projekt_krok1"):
            st.text_input("1. Kdo bude v tvém projektu zastávat roli Top managementu (vize a strategie)?:", placeholder="např. Já jako zakladatel + můj spoluzakladatel")
            st.text_input("2. Jaká oddělení / Middle management budeš v projektu potřebovat?:", placeholder="např. Výroba/Obsah, Marketing, Finance/Logistika")
            st.text_area("3. Jaké hlavní úkoly bude muset řešit liniový management v běžném dni?:", placeholder="např. Kontrola kvality příspěvků na sítě, balení zásilek, obsluha zákazníků")
            
            if st.form_submit_button("Uložit Krok 1 do Projektového pasu"):
                st.success("Krok 1 uložen! Tvá týmová struktura je připravena pro další plánování.")
