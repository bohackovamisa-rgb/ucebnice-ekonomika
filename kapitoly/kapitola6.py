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
# =====================================================================
        # PODKAPITOLA 1.2: ZÁKLADNÍ MANAŽERSKÉ FUNKCE
        # =====================================================================

        st.divider()
        st.markdown("#### 1.2 Základní manažerské funkce: Proces řízení")
        st.write("Manažerská práce není nahodilé hašení požárů. Je to neustále se opakující cyklus čtyř navazujících kroků: **Plánování ➔ Organizování ➔ Vedení lidí ➔ Kontrola**.")

        col_fnc1, col_fce2, col_fce3, col_fce4 = st.columns(4)
        col_fnc1.info("🎯 **1. Plánování**\nStanovení cílů a cest, jak jich dosáhnout.\n*(Kam jdeme?)*")
        col_fce2.warning("🏗️ **2. Organizování**\nRozdělení práce, úkolů, pravomocí a zdrojů.\n*(Kdo co udělá?)*")
        col_fce3.success("💬 **3. Vedení lidí**\nMotivace, komunikace, týmová atmosféra.\n*(Jak je nadchnout?)*")
        col_fce4.error("🔍 **4. Kontrola**\nMěření výsledků a nápravná opatření.\n*(Splnili jsme to?)*")

        # ---------------------------------------------------------------------
        # 1.2.1 PLÁNOVÁNÍ A SMART CÍLE
        # ---------------------------------------------------------------------
        st.markdown("##### 1.2.1 Plánování a SMART cíl")
        st.write("Plánování dává týmu smysl a směr. Podle časového horizontu rozlišujeme:")
        
        st.markdown("""
        * ⏱️ **Krátkodobé (Operativní):** Dny až týdny. *(Rozpis směn na příští týden, plán postů na TikTok).*
        * 🗓️ **Střednědobé (Taktické):** Měsíce až 1–2 roky. *(Kampaň na pololetí, vývoj nového produktu).*
        * 🌐 **Dlouhodobé (Strategické):** Několik let. *(Vstup značky na asijský trh, digitalizace celé firmy).*
        """)

        st.markdown("<div class='box-purple'>🎯 <b>Trenažér: Vyllaď cíl podle pravidla S.M.A.R.T.</b></div>", unsafe_allow_html=True)
        st.write("Vágne zadaný cíl (*'Chceme prodávat hodně mikin'*) vedoucího i tým zmate. Správný cíl musí být **S.M.A.R.T.**:")

        st.markdown("""
        * **S** (Specific) = Konkrétní
        * **M** (Measurable) = Měřitelný (obsahuje číslo)
        * **A** (Achievable) = Dosažitelný
        * **R** (Realistic) = Realistický vzhledem ke zdrojům
        * **T** (Time-bound) = Časově ohraničený (termín)
        """)

        with st.container(border=True):
            st.write("**Předělej špatný cíl na SMART cíl:**")
            st.caption("🔴 *Špatný cíl:* 'Chceme mít úspěšný školní merch.'")
            
            c_smart1, c_smart2, c_smart3 = st.columns(3)
            s_ks = c_smart1.number_input("Kolik kusů chceme prodat?:", min_value=10, value=80, step=10)
            s_marze = c_smart2.number_input("Minimální zisk/marže na kus (Kč):", min_value=50, value=120, step=10)
            s_termin = c_smart3.date_input("Termín dokončení akce:")

            st.success(f"🟢 **Tůj vygenerovaný SMART cíl:** *„Do {s_termin.strftime('%d. %m. %Y')} prodáme přesně {s_ks} kusů školních mikin studentům s minimální marží {s_marze} Kč na kus.“*")

        # ---------------------------------------------------------------------
        # 1.2.2 ORGANIZOVÁNÍ
        # ---------------------------------------------------------------------
        st.markdown("##### 1.2.2 Organizování a Pravomoc vs. Odpovědnost")
        st.write("Organizování znamená vytvořit jasnou strukturu: určit, kdo o čem rozhoduje, kdo komu podléhá a kdo za co ručí.")

        st.markdown("""
        <div class='box-yellow'>
            ⚖️ <b>Základní rovnováha managementu:</b><br>
            • <b>Pravomoc:</b> Právo rozhodovat, utrácet peníze a zadávat úkoly.<br>
            • <b>Odpovědnost:</b> Povinnost nést následky a ručit za výsledek.<br>
            <i>Největší past neefektivního manažera? Dát podřízenému 100% odpovědnost za akci, ale nedát mu žádnou pravomoc o ní rozhodnout!</i>
        </div>
        """, unsafe_allow_html=True)

        # ---------------------------------------------------------------------
        # 1.2.3 VEDENÍ LIDÍ A MASLOWOVA PYRAMIDA
        # ---------------------------------------------------------------------
        st.markdown("##### 1.2.3 Vedení lidí a Maslowova pyramida potřeb")
        st.write("Vedení lidí není o komandování, ale o motivaci. Rozlišujeme:")
        st.markdown("* **Motivace:** Vnitřní touha a smysl něco dělat *(např. student chce vést podcast, protože ho to baví a chce se rozvíjet)*.")
        st.markdown("* **Stimulace:** Vnější odměna nebo podnět *(např. finanční bonus, pochvala, diplom, volno)*.")

        st.markdown("#### 🔺 1.2.3.1 Maslowova pyramida potřeb v praxi")
        st.write("Psycholog Abraham Maslow ukázal, že lidé mají potřeby uspořádané do hierarchie. V managementu to znamená jedinou věc: **Člověk, který se bojí o vyhazov nebo nemá zaplacený nájem, nebude v práci kreativní ani zapálený pro vizi.**")

        # Vizualizace Maslowovy pyramidy pomocí Plotly Funnel/Pyramid chart
        úrovně_maslow = [
            "5. Seberealizace", 
            "4. Uznání a respekt", 
            "3. Sociální potřeby (Tým)", 
            "2. Bezpečí a jistota", 
            "1. Fyziologické potřeby"
        ]
        sirky_maslow = [20, 40, 60, 80, 100]

        fig_maslow = go.Figure(go.Funnel(
            y=úrovně_maslow,
            x=sirky_maslow,
            textinfo="label",
            marker={"color": ["#8b5cf6", "#3b82f6", "#10b981", "#f59e0b", "#ef4444"]}
        ))
        fig_maslow.update_layout(
            title="Maslowova pyramida potřeb (Klikni na úroveň níže pro manažerský význam)",
            height=350, 
            margin=dict(t=40, b=10, l=10, r=10),
            showlegend=False
        )

        st.plotly_chart(fig_maslow, use_container_width=True)

        # Interaktivní průzkumník Maslowovy pyramidy
        wybrana_uroven = st.selectbox("🔍 Vyber úroveň pyramidy a podívej se, jak ji řeší dobrý manažer:", [
            "1. Fyziologické potřeby (Základ)",
            "2. Potřeba bezpečí (Jistota)",
            "3. Sociální potřeby (Vztahy v týmu)",
            "4. Uznání a respekt (Ocenění)",
            "5. Seberealizace (Růst a smysl)"
        ])

        if "1." in wybrana_uroven:
            st.error("🍎 **1. Fyziologické potřeby u zaměstnance:** Důstojný plat, ze kterého zaplatí jídlo a bydlení, větrané prostředí, přestávka na oběd, pitný režim a spánek.")
        elif "2." in wybrana_uroven:
            st.warning("🛡️ **2. Potřeba bezpečí:** Stabilní pracovní smlouva (ne strach z vyhazovu ze dne na den), bezpečné pracoviště bez šikany a jasná pravidla hry.")
        elif "3." in wybrana_uroven:
            st.success("🤝 **3. Sociální potřeby:** Přijetí do týmu, dobrá atmosféra, neformální teambuildingy, vzájemná pomoc a lidská komunikace.")
        elif "4." in wybrana_uroven:
            st.info("🏆 **4. Uznání a respekt:** Pochvala před týmem za dobře odvedenou práci, povýšení, certifikát, titul nebo přidělení důležitého úkolu.")
        else:
            st.markdown("<div class='box-purple'>🚀 <b>5. Seberealizace:</b> Svoboda v tvoření, smysluplná práce, možnost učit se nové věci, realizovat vlastní nápady a odborně růst.</div>", unsafe_allow_html=True)

        # WORKBOOK KROK 2 PRO STUDENTŮV PROJEKT
        st.markdown("<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 2: SMART cíl a motivace týmu</b></div>", unsafe_allow_html=True)
        with st.form("form_projekt_krok2"):
            st.text_area("1. Napiš přesný S.M.A.R.T. cíl pro svůj projekt (Co, kolik, do kdy):", placeholder="např. Do 15. prosince získá náš školní podcast 500 stálých posluchačů na Spotify.")
            st.text_area("2. Jak budeš svůj tým motivovat (kromě peněz) na úrovni Uznání a Seberealizace?:", placeholder="např. Každý člen bude mít v titulcích své jméno, bude mít volnost ve výběru hostů...")
            
            if st.form_submit_button("Uložit Krok 2 do Projektového pasu"):
                st.success("Krok 2 uložen! Tůj cíl je ostrý jako břitva.")
# =====================================================================
        # PODKAPITOLA 1.2.4: KONTROLA
        # =====================================================================

        st.divider()
        st.markdown("#### 1.2.4 Kontrola: Není to slídění, ale navigace")
        st.write("Smyslem kontroly není někoho chytit při chybě a potrestat ho. Kontrola je systém včasného varování, který zjišťuje, zda se **reálný stav shoduje s plánem**, a včas koriguje směr.")

        col_kont1, col_kont2 = st.columns([1, 1])
        with col_kont1:
            st.markdown("""
            <div style="background-color: #f8fafc; padding: 15px; border-left: 5px solid #3b82f6; border-radius: 4px;">
                <h5 style="margin-top:0; color: #1e40af;">🔍 4 fáze kontrolního procesu</h5>
                1. <b>Stanovení standardů:</b> Určíme, jak má vypadat dobrý výsledek (např. <i>zisk 50 000 Kč, nula reklamací</i>).<br>
                2. <b>Zjištění skutečnosti:</b> Změříme reálná data (např. <i>vybralo se jen 30 000 Kč</i>).<br>
                3. <b>Srovnání:</b> Porovnáme plán vs. realitu (např. <i>chybí nám 20 000 Kč k cíli</i>).<br>
                4. <b>Nápravné opatření:</b> Rozhodneme, co upravit (např. <i>přidáme kampaň na sociální sítě</i>).
            </div>
            """, unsafe_allow_html=True)

        with col_kont2:
            st.markdown("##### ⏱️ Typy kontroly podle času")
            tab_k1, tab_k2, tab_k3 = st.tabs(["🔮 Předběžná", "⚙️ Průběžná", "🏁 Následná"])
            
            with tab_k1:
                st.info("**Předběžná kontrola (PŘED spuštěním):** Chrání před zbytečnými krizemi a průšvihy.\n\n*Příklady:* Kontrola rozpočtu, schválení finálního vzorku zboží před tiskem, otestování nefunkčních odkazů na webu 2 hodiny před spuštěním prodeje.")
            with tab_k2:
                st.warning("**Průběžná kontrola (BĚHEM projektu):** Umožňuje reagovat okamžitě na výkyvy.\n\n*Příklady:* Sledování denních prodejů v e-shopu, kontrola plnění harmonogramu na směně, sledování stavu úkolů v Trello/Notionu.")
            with tab_k3:
                st.success("**Následná kontrola (PO dokončení):** Slouží k vyhodnocení a poučení pro příště.\n\n*Příklady:* Spočítání čistého zisku po kampani, vyhodnocení dotazníků spokojenosti zákazníků, rozbor chyb na závěrečné poradě.")
        # =====================================================================
        # PODKAPITOLA 1.3: OSOBNOST MANAŽERA A DOVEDNOSTI
        # =====================================================================

        st.divider()
        st.markdown("#### 1.3 Osobnost manažera, dovednosti a role")
        st.write("Dobrý manažer nemůže být specialistou na úplně všechno. Potřebuje namíchat správný koktejl tří základních dovedností podle toho, na jaké úrovni řízení sedí:")

        # Vizualizace dovedností podle úrovně managementu
        fig_skills = go.Figure()
        fig_skills.add_trace(go.Bar(
            y=['Top Management', 'Middle Management', 'First-line Management'],
            x=[50, 25, 10],
            name='Koncepční (Vize, strategie)',
            orientation='h',
            marker_color='#8b5cf6'
        ))
        fig_skills.add_trace(go.Bar(
            y=['Top Management', 'Middle Management', 'First-line Management'],
            x=[40, 50, 40],
            name='Lidské (Empatie, komunikace)',
            orientation='h',
            marker_color='#3b82f6'
        ))
        fig_skills.add_trace(go.Bar(
            y=['Top Management', 'Middle Management', 'First-line Management'],
            x=[10, 25, 50],
            name='Technické (Detailní znalost oboru)',
            orientation='h',
            marker_color='#10b981'
        ))

        fig_skills.update_layout(
            barmode='stack',
            title="Poměr manažerských dovedností podle úrovně řízení (%)",
            height=280,
            margin=dict(t=40, b=20, l=10, r=10)
        )
        st.plotly_chart(fig_skills, use_container_width=True)

        st.markdown("""
        <div class='box-gray'>
            🧠 <b>Moderní pohled:</b> Šéf nemusí umět nejlépe nakódovat web ani napsat nejlepší reklamní text. Musí ale rozumět práci týmu natolik, aby dokázal pokládat správné otázky, poznal kvalitní výsledek a <b>nepřekážel odborníkům</b>, kteří jsou v konkrétní práci silnější než on.
        </div>
        """, unsafe_allow_html=True)

        # ---------------------------------------------------------------------
        # 1.3.1 MINTZBERGOVY ROLE
        # ---------------------------------------------------------------------
        st.markdown("##### 1.3.1 Role manažera podle Mintzberga")
        st.write("Kanadský profesor Henry Mintzberg zjišťoval, co manažeři reálně dělají celý den. Zjistil, že neustále bleskově přepínají mezi **10 rolemi**, které spadají do 3 skupin:")

        col_r1, col_r2, col_r3 = st.columns(3)
        with col_r1:
            st.markdown("""
            <div style="background-color: #eff6ff; padding: 12px; border-radius: 6px; height: 100%;">
                <h5 style="margin-top:0; color: #1d4ed8;">🤝 Interpersonální role</h5>
                Vstupuje do vztahů s lidmi.<br><br>
                • <b>Reprezentant:</b> Vystupuje jménem firmy nařejnosti.<br>
                • <b>Lídr:</b> Vede a motivuje podřízené.<br>
                • <b>Spojovatel:</b> Buduje sítě kontaktů.
            </div>
            """, unsafe_allow_html=True)
        with col_r2:
            st.markdown("""
            <div style="background-color: #fef3c7; padding: 12px; border-radius: 6px; height: 100%;">
                <h5 style="margin-top:0; color: #b45309;">📡 Informační role</h5>
                Sbírá a šíří informace.<br><br>
                • <b>Monitor:</b> Hledá zprávy na trhu a u konkurence.<br>
                • <b>Siritel:</b> Předává zásadní zprávy týmu.<br>
                • <b>Mluvčí:</b> Dává oficiální vyjádření ven.
            </div>
            """, unsafe_allow_html=True)
        with col_r3:
            st.markdown("""
            <div style="background-color: #f0fdf4; padding: 12px; border-radius: 6px; height: 100%;">
                <h5 style="margin-top:0; color: #047857;">⚡ Rozhodovací role</h5>
                Dělá klíčová rozhodnutí.<br><br>
                • <b>Podnikatel:</b> Vymýšlí inovace a změny.<br>
                • <b>Hasič krizí:</b> Řeší nečekané průšvihy.<br>
                • <b>Alokátor zdrojů:</b> Dělí rozpočet a lidi.<br>
                • <b>Vyjednavač:</b> Smlouvá o cenách a smlouvách.
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br><div class='box-purple'>🕹️ <b>Simulátor: Přepni se do Mintzbergovy role</b></div>", unsafe_allow_html=True)
        st.write("Jsi manažer/ka startupu. Během dopoledne se stane několik událostí. Poznáš, jakou roli právě hraještě?")

        situace_mintz = st.selectbox("Vyber situaci ze dne manažera:", [
            "1. Vybíráš, kterým 3 projektům z deseti přidělíš peníze z rozpočtu na příští měsíc.",
            "2. Novinář z Forbesu se ptá na oficiální stanovisko vaší firmy k novým eko-zákonům.",
            "3. Právě prasklo, že dodavatel serverů skrachoval a vypadly všechny systémy. Musíš okamžitě sehnat náhradní řešení.",
            "4. Jdeš na kávu se zakladatelem partnerké firmy, abys zjistil/a, jaké novinky chystá vaše konkurence."
        ])

        if "1." in situace_mintz:
            st.info("🎯 Hraještě rozhodovací roli **Alokátora zdrojů** (určuješ, kam potečou peníze a kapacity).")
        elif "2." in situace_mintz:
            st.info("📢 Hraještě informační roli **Mluvčího** (oficiálně komunikuješ ven jménem organizace).")
        elif "3." in situace_mintz:
            st.error("🚨 Hraještě rozhodovací roli **Hasiče krizí (Disturbance handler)** – řešíš akutní ohrožení firmy.")
        else:
            st.success("🔎 Hraještě informační roli **Monitora** a interpersonální roli **Spojovatele (Liaison)** – buduješ sítě a nasáváš informace z trhu.")

        # =====================================================================
        # PODKAPITOLA 1.4: STYLY ŘÍZENÍ
        # =====================================================================

        st.divider()
        st.markdown("#### 1.4 Styly řízení: Jak pracovat s mocí a týmem")
        st.write("Styl řízení ukazuje, jak manažer přistupuje k rozhodování, pravomocem a lidem. Neexistuje jediný 'dokonalý' styl – špičkový manažer dokáže styl měnit podle situace, zkušeností týmu i časového tlaku (tzv. **situační řízení**).")

        col_st1, col_st2, col_st3 = st.columns(3)
        with col_st1:
            st.markdown("""
            <div style="background-color: #fef2f2; padding: 15px; border-top: 5px solid #ef4444; border-radius: 4px; height: 100%;">
                <h5 style="margin-top:0; color: #b91c1c;">👑 Autoritativní (Autokratický)</h5>
                <b>Jak funguje:</b> Manažer rozhoduje sám bez debaty, dává příkazy a přísně kontroluje.<br><br>
                <b>Výhody:</b> Blesková rychlost, jasný směr, skvělé v krizích a u nezkušeného týmu.<br><br>
                <b>Rizika:</b> Demotivace lidí, strach z chyb, nula nápadů od týmu, riziko vyhoření.
            </div>
            """, unsafe_allow_html=True)

        with col_st2:
            st.markdown("""
            <div style="background-color: #eff6ff; padding: 15px; border-top: 5px solid #3b82f6; border-radius: 4px; height: 100%;">
                <h5 style="margin-top:0; color: #1d4ed8;">🤝 Demokratický (Participativní)</h5>
                <b>Jak funguje:</b> Manažer zapojuje tým do diskuse, naslouchá nápadům a deleguje pravomoci.<br><br>
                <b>Výhody:</b> Vysoká motivace, skvělé nápady, odpovědnost týmu za výsledek.<br><br>
                <b>Rizika:</b> Pomalejší rozhodování, riziko nekonečných debat, selhává v akutní krizi.
            </div>
            """, unsafe_allow_html=True)

        with col_st3:
            st.markdown("""
            <div style="background-color: #f0fdf4; padding: 15px; border-top: 5px solid #10b981; border-radius: 4px; height: 100%;">
                <h5 style="margin-top:0; color: #047857;">🕊️ Liberální (Laissez-faire)</h5>
                <b>Jak funguje:</b> Manažer nechává týmu absolutní volnost a zasahuje jen minimálně.<br><br>
                <b>Výhody:</b> Obrovská svoboda a prostor pro kreativitu špičkových seniorních expertů.<br><br>
                <b>Rizika:</b> Chaos, nejasné priority, rozpad týmu, selhává u nezkušených lidí.
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>##### ⚖️ Boss vs. Leader: V čem je zásadní rozdíl?")
        st.markdown("""
        | Vlastnost | 👹 Boss (Šéf z minulého století) | 🦁 Leader (Lídr moderní doby) |
        | :--- | :--- | :--- |
        | **Autorita** | Stojí na pozici a strachu (*"Udělej to, nebo letíš"*). | Stojí na důvěře a respektu (*"Pojďme to dokázat"*). |
        | **Při chybě** | Hledá viníka a trestá. | Hledá příčinu a pomáhá ji vyřešit. |
        | **Komunikace** | Dává příkazy a mluví sám. | Kladne otázky a naslouchá týmu. |
        | **Znalosti** | Tajní si informace pro sebe, aby byl postradatelný. | Sdílí informace a vychovává z podřízených nové lídry. |
        | **Zaměření** | Krátkodobý výkon za každou cenu. | Dlouhodobá udržitelnost a rozvoj týmu. |
        """)

        st.markdown("<div class='box-yellow'>🗣️ <b>Debatní aréna: Autoritativní Musk vs. Demokratické Spotify</b></div>", unsafe_allow_html=True)
        st.write("Srovnejme dva odlišné světy. **Elon Musk** (Tesla, SpaceX) uplatňuje extrémně autoritativní styl, mikro-management a tvrdý tlak na výkon. Na druhé straně firmy jako **Google nebo Spotify** sází na týmovou autonomii, svobodu a demokratickou kulturu.")

        with st.form("debata_musk_form"):
            st.write("**Která filozofie řízení je ti bližší a proč?**")
            postoj_styl = st.radio("Vyber svůj postoj:", [
                "🚀 Dávám přednost autoritativnímu vizionáři (Musk): Bez tvrdé ruky, vysokých nároků a rychlého rozhodování jedním člověkem nikdy nevzniknou revoluční věci typu přistání na Marsu.",
                "🎧 Dávám přednost demokratické/svobodné kultuře (Spotify/Google): Lidé pod neustálým strachem vyhoří. Nejlepší inovace vznikají v prostředí, kde mají lidé svobodu, bezpečí a možnost dělat chyby.",
                "⚖️ Záleží na situaci: V krizích a při záchraně firmy je nutný autokratický styl, při vývoji nových nápadů v klidných dobách je lepší demokratický styl."
            ])
            if st.form_submit_button("Odeslat názor do třídní debaty"):
                st.success("Tůj postoj byl zaznamenán! Přesně tohle je podstata *situačního řízení* – pochopit, že každý styl má své místo v jiné fázi firmy.")

        # WORKBOOK KROK 3 PRO STUDENTŮV PROJEKT
        st.markdown("<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 3: Styl řízení a kontrolní mechanizmus</b></div>", unsafe_allow_html=True)
        with st.form("form_projekt_krok3"):
            st.text_area("1. Jaký styl řízení zvolíš pro svůj projekt a proč? (Autoritativní v krizích, Demokratický při nápadech...?):", placeholder="např. Běžně chci řídit tým demokraticky, ale 2 dny před akcí přepnu do autoritativního stylu, aby vše klaplo na minutu.")
            st.text_area("2. Jak nastavíš PŘEDBĚŽNOU kontrolu pro svůj projekt? (Co zkontroluješ ještě před startem?):", placeholder="např. Zkontroluji funkčnost platební brány e-shopu a dostupnost zboží na skladě týden před spuštěním kampaně.")
            
            if st.form_submit_button("Uložit Krok 3 do Projektového pasu"):
                st.success("Krok 3 úspěšně uložen do tvého projektového pasu!")
