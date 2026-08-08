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
# =====================================================================
        # PODKAPITOLA 1.5: ORGANIZAČNÍ STRUKTURY FIREM
        # =====================================================================

        st.divider()
        st.markdown("#### 1.5 Organizační struktury firem: Mapa tvé organizace")
        st.write("Organizační struktura určuje vnitřní uspořádání firmy. Ukazuje, kdo komu odpovídá, jak jsou rozdělené útvary, kudy tečou informace a kdo má pravomoc rozhodovat.")

        st.markdown("""
        <div class='box-blue'>
            🏢 <b>Jednoduše:</b> Organizační struktura je mapa firmy. Pomáhá lidem pochopit, kde jsou jejich role, kdo o čem rozhoduje, s kým spolupracují a na koho se v jaké situaci obrátit.
        </div>
        """, unsafe_allow_html=True)

        # ---------------------------------------------------------------------
        # 1.5.1 FORMÁLNÍ A NEFORMÁLNÍ STRUKTURA
        # ---------------------------------------------------------------------
        st.markdown("##### 1.5.1 Formální a neformální struktura")
        st.write("V každé firmě fungují vedle sebe dvě struktury – ta, která je nakreslená na papíře, a ta, která reálně žije na chodbičkách a v chatu.")

        col_str1, col_str2 = st.columns(2)
        with col_str1:
            st.markdown("""
            <div style="background-color: #f8fafc; padding: 15px; border-left: 5px solid #3b82f6; border-radius: 4px; height: 100%;">
                <h5 style="margin-top: 0; color: #1e40af;">📄 Formální struktura</h5>
                <b>Co znamená:</b> Oficiálně dané vztahy, pozice, pravomoci a odpovědnosti stanovené vedením.<br><br>
                <b>Příklady:</b> Organigram školy, popisy pracovních pozic, smlouva, oficiální vedoucí oddělení.
            </div>
            """, unsafe_allow_html=True)

        with col_str2:
            st.markdown("""
            <div style="background-color: #fef3c7; padding: 15px; border-left: 5px solid #f59e0b; border-radius: 4px; height: 100%;">
                <h5 style="margin-top: 0; color: #b45309;">💬 Neformální struktura</h5>
                <b>Co znamená:</b> Přirozené vztahy, sympatie, osobní vliv a neoficiální autorita mezi lidmi.<br><br>
                <b>Příklady:</b> Člověk, za kterým všichni chodí pro radu (i když není vedoucí), neformální skupinka na oběd, vlivný člen týmu.
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br><div class='box-purple'>🕹️ <b>Reality check: Síla neformální autority</b></div>", unsafe_allow_html=True)
        st.write("Neformální autorita může být obrovským pomocníkem, ale i tichým zabijákem projektu. Záleží na tom, jak s ní manažer pracuje:")

        neformalni_scenar = st.radio("Jak zareaguje neformální autorita v týmu?", [
            "🟢 Kladný vliv: Neformální lídr podporuje změnu a pomáhá ostatním vysvětlit její smysl.",
            "🔴 Záporný vliv: Neformální lídr šíří skepsi, pomluvy a v zákulisí sabotuje rozhodnutí vedení."
        ])

        if "Kladný" in neformalni_scenar:
            st.success("✅ **Výsledek:** Tým přijme změnu 2× rychleji. Manažer získal klíčového spojence a komunikace je přirozená a hladká.")
        else:
            st.error("🚨 **Výsledek:** Projekt drhne, v týmu roste napětí a oficiální autorita manažera kolabuje. Moudrý manažer musí s tímto člověkem okamžitě mluvit mezi čtyřma očima a pochopit jeho výhrady.")

        # ---------------------------------------------------------------------
        # 1.5.2 ZÁKLADNÍ TYPY ORGANIZAČNÍCH STRUKTUR
        # ---------------------------------------------------------------------
        st.divider()
        st.markdown("##### 1.5.2 Základní typy organizačních struktur")
        st.write("Podle toho, jak se ve firmě dělí pravomoci a odbornosti, rozlišujeme 4 základní typy uspořádání:")

        tab_org1, tab_org2, tab_org3, tab_org4 = st.tabs(["📐 Liniová", "🛡️ Štábní", "⚙️ Funkcionální", "🔀 Maticová"])

        with tab_org1:
            st.markdown("##### Liniová struktura (Jasný řetězec)")
            st.write("**Jak funguje:** Nejjednodušší pyramida. Jeden podřízený má přesně jednoho přímého nadřízeného.")
            col_l1, col_l2 = st.columns(2)
            col_l1.success("👍 **Výhody:** Přehlednost, jasné pravomoci, nikdo nemá zmatek v tom, kdo je jeho šéf.")
            col_l2.error("👎 **Rizika:** Nepružnost, přetížení šéfa nahoře, pomalý tok informací přes více pater.")

        with tab_org2:
            st.markdown("##### Štábní / Liniově-štábní struktura")
            st.write("**Jak funguje:** Linioví vedoucí rozhodují, ale k ruce mají **štáb** (odborné poradce bez přímé moci prikazovat).")
            col_s1, col_s2 = st.columns(2)
            col_s1.success("👍 **Výhody:** Manažer má odbornou podporu (např. právník, HR specialista, analytik).")
            col_s2.error("👎 **Rizika:** Štáb sice radí, ale nenese přímou odpovědnost za reálný výsledek na provozu.")

        with tab_org3:
            st.markdown("##### Funkcionální struktura (Podle odbornosti)")
            st.write("**Jak funguje:** Firma je rozdělená na specializovaná oddělení: Marketing, Finance, Výroba, HR, IT.")
            col_f1, col_f2 = st.columns(2)
            col_f1.success("👍 **Výhody:** Vysoká odbornost a specializace lidí v daném oboru.")
            col_f2.error("👎 **Rizika:** Vznik 'sil' – oddělení spolu málo komunikují a hádají se o priority.")

        with tab_org4:
            st.markdown("##### Maticová struktura (Projektová mašinérie)")
            st.write("**Jak funguje:** Kombinuje odborná oddělení a konkrétní projektové týmy. Pracovník má **dva nadřízené**!")
            col_m1, col_m2 = st.columns(2)
            col_m1.success("👍 **Výhody:** Extrémně pružné, skvělé pro projekty, inovace a týmovou spolupráci napříč obory.")
            col_m2.error("👎 **Rizika:** Dvojí podřízenost – riziko konfliktů, čí úkol má přednost.")

        st.markdown("<div class='box-purple'>🎒 <b>Příklad z praxe: Maticová struktura na školním projektu</b></div>", unsafe_allow_html=True)
        st.write("Představ si, že jsi student/ka grafiky. Tví dva šéfové ti zadají úkol:")

        col_mat1, col_mat2 = st.columns(2)
        with col_mat1:
            st.info("🎨 **Funkční vedoucí (Šéf grafického oddělení):**\n*'Zajímá mě vizuální čistota, dodržení brandu a špičková kvalita grafiky. Na plakátu pracuj alespoň 3 dny!'*")
        with col_mat2:
            st.warning("🎪 **Projektový vedoucí (Šéf festivalu):**\n*'Potřebuji plakát hned zítra ráno, jinak nestihneme tisk! Kvalita nemusí být perfektní, hlavní je rychlost.'*")

        st.caption("👉 *A přesně v tento moment vzniká maticové dilema! Výhodou je, že projekt dostane grafika od odborníka, ale grafik musí umět balancovat mezi požadavky obou šéfů.*")

        # ---------------------------------------------------------------------
        # 1.5.3 ROZPĚTÍ ŘÍZENÍ
        # ---------------------------------------------------------------------
        st.divider()
        st.markdown("##### 1.5.3 Rozpětí řízení: Kolik lidí zvládne jeden manažer?")
        st.write("Rozpětí řízení určuje **počet podřízených, kteří přímo podléhají jednomu vedoucímu**.")

        st.markdown("<div class='box-purple'>🕹️ <b>Simulátor rozpětí řízení: Vyzkoušej si roli šéfa</b></div>", unsafe_allow_html=True)
        st.write("Posouvej sliderem a sleduj, jak se mění charakteristika organizace s počtem tvých přímých podřízených:")

        pocet_podrizenych = st.slider("Počet lidí, které přímo řídíš:", min_value=2, max_value=25, value=5, step=1)

        if pocet_podrizenych <= 6:
            st.info(f"📏 **Úzké rozpětí řízení ({pocet_podrizenych} lidí na 1 manažera)**")
            st.markdown("""
            * **Jak vypadá organizace:** 'Vysoká' pyramida s mnoha úrovněmi řízení a mezivedoucími.
            * **Výhody:** Máš na každého čas, můžeš detailně kontrolovat a mentorovat, vhodné pro složité/rizikové úkoly (např. chirurgie, vývoj jádra).
            * **Nevýhody:** Drahý provoz (hodně manažerů), pomalá byrokracie a pomalý tok informací shora dolů.
            """)
        elif 7 <= pocet_podrizenych <= 12:
            st.success(f"⚖️ **Optimalní/Vyvážené rozpětí řízení ({pocet_podrizenych} lidí na 1 manažera)**")
            st.markdown("""
            * **Jak vypadá organizace:** Zdravý kompromis mezi kontrolou a samostatností.
            * **Výhody:** Zvládáš sledovat výstupy, lidé mají prostor pro vlastní nápady a komunikace je dostatečně rychlá.
            """)
        else:
            st.warning(f"📐 **Široké rozpětí řízení ({pocet_podrizenych} lidí na 1 manažera)**")
            st.markdown("""
            * **Jak vypadá organizace:** 'Plochá' struktura s málo úrovněmi (častá u startupů nebo McDonald's).
            * **Výhody:** Blesková komunikace, nízké náklady na manažery, velká samostatnost podřízených.
            * **Nevýhody:** Manažer nestíhá reagovat, hrozí přetížení, přehlížení chyb a chaos u nezkušeného týmu.
            """)

        # WORKBOOK KROK 4 PRO STUDENTŮV PROJEKT
        st.markdown("<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 4: Organizační mapa tvého projektu</b></div>", unsafe_allow_html=True)
        with st.form("form_projekt_krok4"):
            st.selectbox("1. Jaký typ organizační struktury se nejlépe hodí pro tvůj projekt?:", [
                "Liniová (Jednoduchá pyramida s jedním šéfem)",
                "Funkcionální (Rozděleno podle oborů: Marketing, Výroba, IT...)",
                "Maticová (Projektový tým se skládá ze specialistů z různých oborů)",
                "Plochá / Široká (Všichni komunikujeme přímo s zakladatelem)"
            ])
            st.text_area("2. Jaké zvolíš rozpětí řízení pro hlavního manažera a jak ošetříte neformální vztahy v týmu?:", placeholder="např. Hlavní manažer pořídí 4 vedoucí sekcí (úzké rozpětí), aby nebyl přetížen. Neformální lídr bude v týmu mít roli inovátora...")
            
            if st.form_submit_button("Uložit Krok 4 do Projektového pasu"):
                st.success("Krok 4 úspěšně uložen! Tvá organizace má jasnou strukturu i pravidla.")
# =====================================================================
        # PODKAPITOLA 1.6: ROZHODOVÁNÍ A ANALYTICKÉ METODY
        # =====================================================================

        st.divider()
        st.markdown("#### 1.6 Rozhodování a analytické metody")
        st.write("Manažer se neustále dostává do situací, kdy musí vybrat jednu z možností: koho přijmout do týmu, jak rozdělit rozpočet, co udělat při zpoždění nebo jak reagovat na krok konkurence. Dobré rozhodování není jen o pocitu v břiše, ale opírá se o data, alternativy a chladné vyhodnocení důsledků.")

        st.markdown("<div class='box-blue'>🧭 <b>5 kroků rozhodovacího procesu:</b><br>1. <b>Identifikace problému:</b> Co přesně řešíme?<br>2. <b>Sběr informací:</b> Co víme a co ještě musíme zjistit?<br>3. <b>Návrh variant:</b> Jaká řešení připadají v úvahu?<br>4. <b>Výběr nejvhodnější varianty:</b> Která možnost nejlépe odpovídá cíli, zdrojům a rizikům?<br>5. <b>Realizace a kontrola:</b> Provedeme rozhodnutí a sledujeme reálný výsledek.</div>", unsafe_allow_html=True)

        # ---------------------------------------------------------------------
        # 1.6.1 SWOT ANALÝZA
        # ---------------------------------------------------------------------
        st.divider()
        st.markdown("##### 1.6.1 SWOT analýza")
        st.write("SWOT analýza je univerzální nástroj, který pomáhá objektivně zhodnotit situaci firmy, projektu, produktu nebo i tebe samotného. Klíčem je správně rozlišit **vnitřní prostředí** (to, co máš ve svých rukou) a **vnější prostředí** (to, co přichází z okolí a nemůžeš to přímo změnit).")

        col_swot1, col_swot2 = st.columns(2)
        with col_swot1:
            st.markdown("""
            <div style="background-color: #f0fdf4; padding: 15px; border-left: 5px solid #10b981; border-radius: 4px; height: 100%;">
                <h5 style="margin-top: 0; color: #047857;">💪 S — Strengths (Silné stránky)</h5>
                <b>Vnitřní prostředí:</b> V čem jsme skvělí, v čem vynikáme a o co se můžeme opřít.<br><br>
                <i>Otázka: Co nám jde lépe než ostatním? Jaké máme unikátní zdroje?</i>
            </div>
            """, unsafe_allow_html=True)

        with col_swot2:
            st.markdown("""
            <div style="background-color: #fef2f2; padding: 15px; border-left: 5px solid #ef4444; border-radius: 4px; height: 100%;">
                <h5 style="margin-top: 0; color: #b91c1c;">🩹 W — Weaknesses (Slabé stránky)</h5>
                <b>Vnitřní prostředí:</b> Co nás brzdí, v čem zaostáváme a co musíme zlepšit.<br><br>
                <i>Otázka: Kde máme mezery? Co nám chybí oproti konkurenci?</i>
            </div>
            """, unsafe_allow_html=True)

        col_swot3, col_swot4 = st.columns(2)
        with col_swot3:
            st.markdown("""
            <div style="background-color: #eff6ff; padding: 15px; border-left: 5px solid #3b82f6; border-radius: 4px; height: 100%; margin-top: 10px;">
                <h5 style="margin-top: 0; color: #1d4ed8;">🚀 O — Opportunities (Příležitosti)</h5>
                <b>Vnější prostředí:</b> Vývoj na trhu, nové technologie nebo trendy, kterých můžeme využít.<br><br>
                <i>Otázka: Jaká změna kolem nás nám může pomoct k růstu?</i>
            </div>
            """, unsafe_allow_html=True)

        with col_swot4:
            st.markdown("""
            <div style="background-color: #fef3c7; padding: 15px; border-left: 5px solid #f59e0b; border-radius: 4px; height: 100%; margin-top: 10px;">
                <h5 style="margin-top: 0; color: #b45309;">⚠️ T — Threats (Hrozby)</h5>
                <b>Vnější prostředí:</b> Rizika z okolního světa, která nás mohou ohrozit a nemáme nad nimi plnou kontrolu.<br><br>
                <i>Otázka: Co se může pokazit v okolí? Co chystá konkurence?</i>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        <div class='box-gray' style='margin-top: 15px;'>
            📌 <b>Pozor na nejčastější chybu v testech a praxi:</b><br>
            Silné a slabé stránky jsou <b>uvnitř</b> organizace. Příležitosti a hrozby přicházejí <b>zvenčí</b>.<br>
            • <i>„Máme málo peněz na účtu“</i> ➔ Slabá stránka (W).<br>
            • <i>„Majitel budovy skokově zdraží nájem“</i> ➔ Hrozba (T).
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br><div class='box-purple'>🕹️ <b>Trenažér SWOT: Kam patří tento faktor?</b></div>", unsafe_allow_html=True)
        st.write("Otestuj se, zda dokážeš správně rozlišit vnitřní a vnější vlivy:")

        faktor_kviz = st.radio("Kam správně zařadíš faktor: *„Na trhu se objevil nový trend a mladí lidé začínají masivně vyhledávat udržitelnou módu“*?", [
            "Vyber odpověď...",
            "A) Silná stránka (Strengths) – přece je to skvělá věc!",
            "B) Příležitost (Opportunities) – jde o vnější trend na trhu, kterého můžeme využít.",
            "C) Slabá stránka (Weaknesses) – protože jsme ji ještě nezačali vyrábět."
        ])

        if "B)" in faktor_kviz:
            st.success("✅ **Přesně tak!** Jedná se o vnější trend v chování zákazníků, takže jde o **Příležitost (O)**.")
        elif "A)" in faktor_kviz or "C)" in faktor_kviz:
            st.error("❌ Pozor! Změna chování zákazníků přichází z okolního trhu (zvenčí). Správná odpověď je B (Příležitost).")

        # ---------------------------------------------------------------------
        # 1.6.2 ZÁKLADY ŘÍZENÍ RIZIK
        # ---------------------------------------------------------------------
        st.divider()
        st.markdown("##### 1.6.2 Základy řízení rizik")
        st.write("Řízení rizik neznamená být paranoik, ale být připraven. Dobrý manažer přemýšlí dopředu o tom, co se může pokazit, jak moc je to pravděpodobné, jak velký dopad by to mělo a co udělá v případě krize.")

        st.markdown("<div class='box-purple'>🧮 <b>Interaktivní Matice rizik (Pravděpodobnost × Dopad)</b></div>", unsafe_allow_html=True)
        st.write("Vyber si riziko a nastav jeho parametery. Zjisti, jakou reakci vyžaduje:")

        with st.container(border=True):
            col_r1, col_r2 = st.columns(2)
            with col_r1:
                pravdepodobnost = st.select_slider(
                    "Jaká je pravděpodobnost, že k události dojde?",
                    options=["Nízká (Výjimečně)", "Střední (Možná)", "Vysoká (Téměř jistě)"]
                )
            with col_r2:
                dopad = st.select_slider(
                    "Jak velký dopad by to mělo na projekt?",
                    options=["Malý (Drobná nepříjemnost)", "Střední (Zpoždění/Ztráta)", "Kritický (Konec projektu)"]
                )

            st.write("---")
            if "Vysoká" in pravdepodobnost and "Kritický" in dopad:
                st.error("🚨 **KRITICKÉ RIZIKO (Červená zóna):** Nutná okamžitá prevence a detailní Záložní plán B! Tento hazard může zničit celý projekt.")
            elif "Nízká" in pravdepodobnost and "Malý" in dopad:
                st.success("🟢 **NÍZKÉ RIZIKO (Zelená zóna):** Můžeme ho akceptovat. Sledovat, ale neplýtvat na něj příliš mnoho zdrojů.")
            else:
                st.warning("🟡 **STŘEDNÍ RIZIKO (Žlutá zóna):** Vyžaduje preventivní opatření a přípravu záložního scenáře.")

        st.markdown("""
        <div class='box-green'>
            🧠 <b>Pointa řízení rizik:</b> Dobrý manažer není člověk, kterému se nikdy nic nepokazí. Je to člověk, který počítá s tím, že se něco pokazit může, a má v šuplíku připravený funkční <b>Plán B</b>.
        </div>
        """, unsafe_allow_html=True)

        # WORKBOOK KROK 5 PRO STUDENTŮV PROJEKT
        st.markdown("<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 5: SWOT analýza a Plán B tvého projektu</b></div>", unsafe_allow_html=True)
        with st.form("form_projekt_krok5"):
            st.markdown("##### 📊 Vyplň jednoduchou SWOTku pro svůj projekt:")
            col_sw1, col_sw2 = st.columns(2)
            with col_sw1:
                p_s = st.text_input("Silné stránky (S - Vnitřní):", placeholder="např. Skvělý grafický design, nadšený tým")
                p_w = st.text_input("Slabé stránky (W - Vnitřní):", placeholder="např. Nulový rozpočet, málo zkušeností s prodejem")
            with col_sw2:
                p_o = st.text_input("Příležitosti (O - Vnější):", placeholder="např. Rostoucí zájem studentů o podcasty")
                p_t = st.text_input("Hrozby (T - Vnější):", placeholder="např. Konkurenční škola spustí podobný projekt")

            st.markdown("##### 🛡️ Řízení rizik v praxi:")
            st.text_area("Pojmenuj 1 největší riziko tvého projektu a navrhni konkrétní Plán B:", placeholder="např. Riziko: Hlavní moderátor v den natáčení onemocní. Plán B: Máme předtočené 2 epizody do zásoby a náhradního moderátora.")

            if st.form_submit_button("Uložit Krok 5 do Projektového pasu"):
                st.success("Krok 5 úspěšně uložen! Blok 1 (Management) máš kompletně zpracovaný.")
# =====================================================================
        # PODKAPITOLA 1.7: MODERNÍ PŘESAH (AGILITA, REMOTE WORK A BURNOUT)
        # =====================================================================

        st.divider()
        st.markdown("#### 1.7 Moderní přesah: Agilní řízení, remote work a burnout")
        st.write("Současný management se posouvá od pouhého zadávání příkazů k práci s **autonomií, důvěrou, psychologickým bezpečím a průběžnou zpětnou vazbou**. Moderní manažer není policajt hlídající odpracované minuty, ale koordinátor, kouč a stavitel prostředí, ve kterém tým dokáže dlouhodobě podávat výkony bez vyhoření.")

        tab_m1, tab_m2, tab_m3 = st.tabs(["⚡ Agilní metody (Scrum, Kanban, OKR)", "🤝 Vedení & Kultura", "💻 Remote work & Wellbeing"])

        with tab_m1:
            st.markdown("##### Agilní řízení a moderní metodiky")
            st.write("Místo ročního plánování 'od stolu' se dnes pracuje v **krátkých cyklech**. Produkt se rychle spustí v základní verzi (MVP) a vylepšuje se za chodu podle reakcí uživatelů.")

            st.markdown("""
            * 🏃 **Scrum & Sprinty:** Tým pracuje v krátkých časových úsecích (sprinty, např. 2 týdny). Na konci každého sprintu ukáže konkrétní hotový výsledek.
            * 📋 **Kanban:** Vizualizace úkolů ve sloupcích pro přehlednost (*K vyřešení ➔ Probíhá ➔ Hotovo*).
            * 🎯 **OKR (Objectives & Key Results):** Stanovení 1 ambiciózního cíle a 3–4 konkrétních měřitelných výsledků (např. *Cíl: Zvětšit komunitu. Výsledek: +200 nových členů, 30% aktivita*).
            """)

            st.markdown("<div class='box-purple'>📋 <b>Interaktivní Kanban nástěnka</b></div>", unsafe_allow_html=True)
            st.write("Vyzkoušej si přesouvání úkolů mezi sloupci v reálném čase:")

            # Inicializace stavu úkolů v paměti Streamlitu
            if "kanban_tasks" not in st.session_state:
                st.session_state.kanban_tasks = {
                    "Připravit grafiku na kampaň": "To Do",
                    "Sjednat sponzora": "To Do",
                    "Střih videa pro TikTok": "In Progress",
                    "Schválení rozpočtu": "Done"
                }

            col_kan1, col_kan2, col_kan3 = st.columns(3)

            # Sloupec 1: To Do
            with col_kan1:
                st.error("📥 **K vyřešení (To Do)**")
                for task, status in list(st.session_state.kanban_tasks.items()):
                    if status == "To Do":
                        st.write(f"• {task}")
                        if st.button("Posunout ➔", key=f"move_in_{task}"):
                            st.session_state.kanban_tasks[task] = "In Progress"
                            st.rerun()

            # Sloupec 2: In Progress
            with col_kan2:
                st.warning("⚙️ **Probíhá (In Progress)**")
                for task, status in list(st.session_state.kanban_tasks.items()):
                    if status == "In Progress":
                        st.write(f"• {task}")
                        c_left, c_right = st.columns(2)
                        if c_left.button("⬅️", key=f"back_todo_{task}"):
                            st.session_state.kanban_tasks[task] = "To Do"
                            st.rerun()
                        if c_right.button("➔", key=f"move_done_{task}"):
                            st.session_state.kanban_tasks[task] = "Done"
                            st.rerun()

            # Sloupec 3: Done
            with col_kan3:
                st.success("✅ **Hotovo (Done)**")
                for task, status in list(st.session_state.kanban_tasks.items()):
                    if status == "Done":
                        st.write(f"• {task}")
                        if st.button("⬅️ Vrátit", key=f"back_in_{task}"):
                            st.session_state.kanban_tasks[task] = "In Progress"
                            st.rerun()

        with tab_m2:
            st.markdown("##### Koučování, zpětná vazba a psychologické bezpečí")
            st.write("Skvělé nástroje jsou k ničemu, pokud se lidé v týmu bojí mluvit.")

            st.markdown("""
            * ❓ **Koučovací styl:** Místo *"Udělej to přesně takhle"* se manažer ptá: *"Jaký problém v tom vidíš a jaké možnosti řešení navrhuješi?"*
            * 🔄 **Průběžná zpětná vazba:** Hodnocení neprobíhá 1× za rok, ale v krátkých check-inech ihned po splnění úkolu.
            * 🛡️ **Psychologické bezpečí:** Prostředí, kde se lidé nebojí přiznat chybu, požádat o pomoc nebo říct odlišný názor bez strachu ze zesměšnění.
            """)

        with tab_m3:
            st.markdown("##### Remote work, digitální nástroje a hrozba vyhoření (Burnout)")
            st.write("Flexibilita a práce z domova přinášejí svobodu, ale také riziko, že se hranice mezi prací a osobním životem úplně smaže.")

            st.markdown("""
            <div class='box-gray'>
                💻 <b>Digitální nástroje (Notion, Slack, Teams, Trello):</b> Nepředstavují management samy o sobě. Jsou to jen pomocníci. Důležité je, zda tým rozumí prioritám a má jasně nastavenou kulturu komunikace.
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br><div class='box-purple'>🧮 <b>Burnout kalkulačka: Jak je na tom tvůj tým?</b></div>", unsafe_allow_html=True)
        st.write("Nasimuluj pracovní podmínky a zjisti riziko vyhoření zaměstnanců:")

        with st.container(border=True):
            col_b1, col_b2 = st.columns(2)
            with col_b1:
                vecerne_zpravy = st.select_slider(
                    "Očekává se odpovídání na Slack/e-maily večer a o víkendu?",
                    options=["Nikdy (Respektuje se volno)", "Občas (Při krizích)", "Neustále (Pohotovost 24/7)"]
                )
                jasne_priority = st.select_slider(
                    "Jsou v týmu jasně nastavené priority?",
                    options=["Ano (Víme, co je hlavní)", "Částečně", "Chaotické (Všechno hoří)"]
                )
            with col_b2:
                pauzy_volno = st.select_slider(
                    "Podporuje manažer pauzy a čerpání dovolené?",
                    options=["Ano (Aktivně hlídá odpočinek)", "Neutrálně", "Ne (Dovolená je brána jako lenost)"]
                )

            # Bodování rizika vyhoření
            score = 0
            if "Neustále" in vecerne_zpravy: score += 40
            elif "Občas" in vecerne_zpravy: score += 15
            
            if "Chaotické" in jasne_priority: score += 35
            elif "Částečně" in jasne_priority: score += 15
            
            if "Ne" in pauzy_volno: score += 25
            elif "Neutrálně" in pauzy_volno: score += 10

            st.write("---")
            st.markdown(f"##### Odhadované riziko vyhoření v týmu: **{score} %**")
            st.progress(score / 100.0)

            if score > 60:
                st.error("🚨 **VYSOKÉ RIZIKO VYHOŘENÍ:** Tým je přetížený neustálou pohotovostí a chaosem. Hrozí odchody lidí, chybovost a toxická atmosféra. Manažer musí okamžitě nastavit hranice a určení priorit!")
            elif score > 30:
                st.warning("⚠️ **MÍRNÉ RIZIKO:** Tým funguje, ale dlouhodobě by nejasné priority nebo občasné večerní zprávy mohly vést k únavě. Zlepšete odpočinek.")
            else:
                st.success("✅ **ZDRÁVÉ PROSTŘEDÍ:** Tým má skvělé podmínky pro udržitelný výkon, psychologické bezpečí a rovnováhu mezi prací a životem.")

        st.markdown("""
        <div class='box-green'>
            ✅ <b>Co si zapamatovat z Bloku 1 (Management):</b><br>
            Management je schopnost proměnit chaos ve fungující projekt. Stojí na cyklu <b>Plánování (SMART cílů) ➔ Organizování (pravomoc a odpovědnost) ➔ Vedení lidí (Maslowova pyramida a motivace) ➔ Kontrola (porovnání plánu a reality)</b>. Dobrý lídr dokáže střídat styly řízení podle situace, pracuje se SWOT analýzou i riziky a vytváří prostředí, kde lidé mohou bezpečně a udržitelně růst.
        </div>
        """, unsafe_allow_html=True)
# =========================================================================
    # SEKCE 2: MARKETING – HRA O POZORNOST A MARKETINGOVÝ MIX
    # =========================================================================
    elif selected_section_6 == section_options_6[1]:
        st.markdown("### 2. Marketing – Hra o pozornost a marketingový mix")
        
        st.markdown("""
        <div class='box-blue'>
            🎯 <b>Moderní hook:</b> <i>„Proč si koupíš značkové tenisky za 4 000 Kč, když skoro stejný fejk stojí 500 Kč a funkčně tě donese na stejné místo?“</i><br>
            Odpovědí je marketing. Marketing totiž není jen reklama. Je to způsob, jak pochopit, po čem lidé touží, jak vytvořit hodnotu, jak se odlišit od stovek kopií a jak dostat správnou nabídku ke správnému člověku v ten správný čas.
        </div>
        """, unsafe_allow_html=True)

        st.divider()

        # =====================================================================
        # PODKAPITOLA 2.1: PODSTATA A VÝZNAM MARKETINGU
        # =====================================================================
        st.markdown("#### 2.1 Podstata a význam marketingu")
        st.write("Marketing je proces, při kterém firma **zjišťuje potřeby zákazníků, vytváří pro ně hodnotu a uspokojuje tyto potřeby** tak, aby zároveň dosahovala zisku a svých cílů. Nejde tedy jen o to natočit cool video na TikTok nebo vnutit lidem produkt u pokladny.")

        st.markdown("""
        <div class='box-yellow'>
            🧠 <b>Jednoduše (Rozdíl mezi prodejem a marketingem):</b><br>
            • <b>Prodej</b> se ptá: <i>„Jak co nejrychleji prodáme to, co už máme vyrobené?“</i><br>
            • <b>Marketing</b> se ptá: <i>„Co lidé reálně potřebují? Komu to nabídneme, za jakou cenu, jak jim to doručíme a jak o nás budou vůbec vědět?“</i>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("##### 🛒 Slovníček základních pojmů (Nejsou to synonyma!)")
        
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.info("**Potřeba:** Pocit nedostatku něčeho základního. *Příklad: Mám žízeň, potřebuji pít. Cítím se osamělý, potřebuji patřit do skupiny.*")
            st.warning("**Přání:** Konkrétní forma potřeby, ovlivněná kulturou, trendy a penězi. *Příklad: Mám žízeň, ale nechci vodu. Chci prémiové Bubble Tea nebo Matcha latté.*")
        with col_m2:
            st.error("**Poptávka:** Přání podpořené ochotou a hlavně **schopností to zaplatit**. *Příklad: Chci nové boty a mám na ně 3000 Kč na účtu.*")
            st.success("**Spotřebitel vs. Zákazník:** Zákazník (Rodič) zaplatí školní batoh. Spotřebitel (Student) ten batoh reálně každý den nosí do školy a používá ho.")

        st.markdown("<div class='box-purple'>🕹️ <b>Detektivka: Co je co?</b></div>", unsafe_allow_html=True)
        st.write("Přečti si následující větu a správně identifikuj pojmy:")

        with st.container(border=True):
            st.write("*„Petr má obrovský hlad. Hrozně by si dal dvojitý Smash burger s hranolkama z nové burgrárny v centru. V peněžence má ale jen 50 Kč, takže si jde nakonec koupit suchý rohlík do večerky.“*")

            kviz_potreby = st.radio("Co z toho byla reálná POPTÁVKA (Demand)?", [
                "Vyber odpověď...",
                "A) Obrovský hlad.",
                "B) Dvojitý Smash burger s hranolkama.",
                "C) Suchý rohlík za 50 Kč."
            ])

            if "C)" in kviz_potreby:
                st.success("✅ **Přesně tak!** Petr měl POTŘEBU (hlad), jeho PŘÁNÍ byl (drahý burger), ale jeho reálná POPTÁVKA na trhu byla jen na rohlík, protože poptávka musí být krytá penězi!")
            elif "A)" in kviz_potreby:
                st.error("❌ Hlad je pouze základní **Potřeba**, chybí tam ty peníze. Zkus to znovu.")
            elif "B)" in kviz_potreby:
                st.error("❌ Smash burger byl pouze Petrovo **Přání**. Neměl na něj peníze, takže nevytvořil reálnou poptávku. Správně je C.")

        # ---------------------------------------------------------------------
        # 2.1.1 VÝVOJ PODNIKATELSKÝCH KONCEPCÍ
        # ---------------------------------------------------------------------
        st.divider()
        st.markdown("##### 2.1.1 Vývoj podnikatelských koncepcí: Od pásu po záchranu planety")
        st.write("Firmy se v historii nedívaly na zákazníka vždy stejně. Jejich přístup (tzv. koncepce) se vyvíjel podle toho, jak rostla konkurence a bohatla společnost.")

        st.markdown("<div class='box-purple'>🕰️ <b>Time Machine: Nastup do stroje času</b></div>", unsafe_allow_html=True)
        st.write("Posouvej se časem od minulosti do současnosti a sleduj, jak se měnil mozek byznysu:")

        casova_osa = st.select_slider(
            "Vyber si éru trhu:",
            options=["1. Výrobní (Kvantita)", "2. Výrobková (Kvalita)", "3. Prodejní (Tlak)", "4. Marketingová (Zákazník)", "5. Sociální (Planeta)"]
        )

        if "Výrobní" in casova_osa:
            st.markdown("""
            <div style="background-color: #f8fafc; padding: 15px; border-left: 5px solid #94a3b8;">
                <h5 style="margin-top: 0; color: #475569;">🏭 1. Výrobní koncepce (Důraz na masu a nízkou cenu)</h5>
                <b>Hlavní myšlenka:</b> Vyrábět levně, rychle a ve velkém. Zákazník koupí cokoliv, hlavně když to bude dostupné.<br><br>
                <b>Historický příklad:</b> Henry Ford a jeho Model T: <i>"Můžete mít auto v jakékoliv barvě, pokud to bude černá."</i><br>
                <b>Riziko:</b> Firma úplně ignoruje, co zákazník doopravdy chce. Dnes přežívá jen u superlevných základních surovin.
            </div>
            """, unsafe_allow_html=True)
            
        elif "Výrobková" in casova_osa:
            st.markdown("""
            <div style="background-color: #eff6ff; padding: 15px; border-left: 5px solid #3b82f6;">
                <h5 style="margin-top: 0; color: #1d4ed8;">🔬 2. Výrobková koncepce (Důraz na technickou dokonalost)</h5>
                <b>Hlavní myšlenka:</b> Zákazník chce nejlepší kvalitu, inovace a funkce. Musíme vyrobit dokonalý produkt!<br><br>
                <b>Příklad:</b> Inženýři vyrobí notebook z titanu s brutálním výkonem.<br>
                <b>Riziko:</b> Tzv. <i>marketingová krátkozrakost</i>. Vyrobíte sice technicky dokonalý produkt, ale nikdo ho nekoupí, protože je zbytečně složitý, drahý a lidem stačí obyčejný lehký tablet.
            </div>
            """, unsafe_allow_html=True)
            
        elif "Prodejní" in casova_osa:
            st.markdown("""
            <div style="background-color: #fef2f2; padding: 15px; border-left: 5px solid #ef4444;">
                <h5 style="margin-top: 0; color: #b91c1c;">🗣️ 3. Prodejní koncepce (Důraz na tlak a reklamu)</h5>
                <b>Hlavní myšlenka:</b> Lidé sami od sebe nenakupují dost. Musíme je přemluvit, ukecat a produkt jim vnutit masivní reklamou.<br><br>
                <b>Příklad:</b> Agresivní teleshopping (<i>"Volejte ihned a dostanete sadu nožů!"</i>), slevoví prodejci, tlak pojišťováků.<br>
                <b>Riziko:</b> Člověk si věc možná pod tlakem koupí, ale jakmile přijde domů, lituje toho. Ztratíte důvěru a zákazník se už nikdy nevrátí.
            </div>
            """, unsafe_allow_html=True)
            
        elif "Marketingová" in casova_osa:
            st.markdown("""
            <div style="background-color: #f0fdf4; padding: 15px; border-left: 5px solid #10b981;">
                <h5 style="margin-top: 0; color: #047857;">🎯 4. Marketingová koncepce (Důraz na zákazníka)</h5>
                <b>Hlavní myšlenka:</b> Otočení logiky. Nejdřív se zeptáme, co zákazník chce a jaký má problém. Až TEPŘVE POTOM to vyrobíme a prodáme mu to s profitem.<br><br>
                <b>Příklad:</b> Moderní e-shopy. Zjistí ze svých dat, že lidé nesnáší čekání na poštu ➔ vymyslí AlzaBoxy nebo Zásilkovnu.<br>
                <b>Riziko:</b> Slepé plnění tužeb zákazníků může vést k tomu, že ignorujete dlouhodobé dopady na přírodu nebo společnost.
            </div>
            """, unsafe_allow_html=True)
            
        else:
            st.markdown("""
            <div style="background-color: #fef3c7; padding: 15px; border-left: 5px solid #f59e0b;">
                <h5 style="margin-top: 0; color: #b45309;">🌍 5. Sociální / Etická koncepce (Důraz na udržitelnost a hodnoty)</h5>
                <b>Hlavní myšlenka:</b> Firma musí uspokojit zákazníka, vydělat peníze, ale ZÁROVEŇ chránit společnost a planetu.<br><br>
                <b>Příklad:</b> Značky Patagonia (udržitelná móda), bio-potraviny, kosmetika netestovaná na zvířatech.<br>
                <b>Riziko:</b> <i>Greenwashing</i>. Pokud o tom firma jen lže v reklamách, ale reálně vyrábí toxicky v Asii, dříve či později ji to zničí.
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        <div class='box-gray' style='margin-top: 15px;'>
            🧠 <b>Moderní přesah:</b> Dnešní marketing (fáze 4 a 5) už často neprodává jen funkční produkt, ale prodává <b>životní styl, emoci a identitu</b>. Nekupuješ si iPhone jen proto, abys mohl telefonovat (to umí i mobil za dva tisíce). Kupuješ si ho proto, co to o tobě říká a do jaké komunity tě to řadí.
        </div>
        """, unsafe_allow_html=True)

        # WORKBOOK KROK 6 PRO STUDENTŮV PROJEKT
        st.markdown("<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 6: Podstata a koncepce tvého projektu</b></div>", unsafe_allow_html=True)
        with st.form("form_projekt_krok6"):
            st.text_area("1. Jakou ZÁKLADNÍ POTŘEBU uspokojuje tvůj projekt? (Proč by to měl někdo chtít?):", placeholder="např. Uspokojuje potřebu informovanosti a zábavy během nudné cesty tramvají (školní podcast).")
            st.selectbox("2. Jaká podnikatelská koncepce by k tvému projektu nejlépe seděla?:", [
                "Marketingová (Striktně sledujeme, co zákazník chce a my mu to dáme)",
                "Výrobková (Sázíme na absolutně špičkovou, prémiovou kvalitu bez kompromisů)",
                "Sociální/Etická (Sázíme na udržitelný, bio a férový přístup)",
                "Prodejní (Budeme to tvrdě a agresivně tlačit přes slevy a reklamu)"
            ])
            
            if st.form_submit_button("Uložit Krok 6 do Projektového pasu"):
                st.success("Krok 6 uložen! Tvůj projekt teď pevně stojí na pochopení potřeb.")
# =====================================================================
        # PODKAPITOLA 2.2: MARKETINGOVÝ VÝZKUM A ANALÝZA TRHU
        # =====================================================================

        st.divider()
        st.markdown("#### 2.2 Marketingový výzkum a analýza trhu")
        st.write("Marketingový výzkum znamená systematický sběr, třídění a vyhodnocování informací o trhu, zákaznících, konkurenci a prostředí firmy. Jeho hlavním cílem je **snížit riziko při rozhodování**.")

        st.markdown("""
        <div class='box-blue'>
            🔍 <b>Proč firmy dělají výzkum:</b> Bez dat firma často jen hádá a doufá. Výzkum pomáhá s jistotou zjistit, kdo je zákazník, jaký problém řeší, kolik je ochoten zaplatit, kde nakupuje, jak vnímá naši značku a proč třeba dává přednost konkurenci.
        </div>
        """, unsafe_allow_html=True)

        st.write("**Správný výzkum ti odpoví na klíčové otázky:**")
        st.markdown("* *Kdo je náš zákazník a jaký problém mu produkt řeší?* \n* *Jakou cenu je ochoten zaplatit?* \n* *Která reklama funguje lépe?* \n* *Proč lidé opouštějí košík v e-shopu těsně před platbou?*")

        # ---------------------------------------------------------------------
        # 2.2.1 ZDROJE DAT
        # ---------------------------------------------------------------------
        st.markdown("##### 2.2.1 Zdroje dat: Kde vezmeme informace?")
        
        col_zd1, col_zd2 = st.columns(2)
        with col_zd1:
            st.markdown("""
            <div style="background-color: #f0fdf4; padding: 15px; border-left: 5px solid #10b981; border-radius: 4px; height: 100%;">
                <h5 style="margin-top: 0; color: #047857;">🥇 Primární data (Data z první ruky)</h5>
                <b>Co to je:</b> Nově sesbíraná data vytvořená <i>přímo a jen pro tvůj konkrétní účel</i>.<br><br>
                <b>Výhody:</b> Jsou přesně zaměřená na tvůj problém. Konkurence je nemá.<br>
                <b>Nevýhody:</b> Sběr je dražší a trvá dlouho.<br><br>
                <b>Příklady:</b> Vlastní dotazník mezi spolužáky, rozhovor se zákazníkem.
            </div>
            """, unsafe_allow_html=True)
            
        with col_zd2:
            st.markdown("""
            <div style="background-color: #eff6ff; padding: 15px; border-left: 5px solid #3b82f6; border-radius: 4px; height: 100%;">
                <h5 style="margin-top: 0; color: #1d4ed8;">🥈 Sekundární data (Data z druhé ruky)</h5>
                <b>Co to je:</b> Již existující data, která někdo sesbíral dříve nebo pro jiný účel.<br><br>
                <b>Výhody:</b> Jsou levná (nebo zdarma) a získáš je okamžitě.<br>
                <b>Nevýhody:</b> Nemusí přesně odpovídat tvému problému. Má je i konkurence.<br><br>
                <b>Příklady:</b> Statistiky ČSÚ, staré prodejní výkazy e-shopu, veřejné recenze.
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br><div class='box-purple'>🕹️ <b>Kvíz: Primární nebo sekundární?</b></div>", unsafe_allow_html=True)
        st.write("Jako markeťák potřebuješ zjistit, proč klesají prodeje batohů. Přečti si akci a urči typ dat:")

        kviz_data = st.radio("Jdeš na Heureku a pročítáš si veřejné recenze od lidí, kteří si batoh koupili loni.", [
            "Vyber odpověď...",
            "A) Jsou to Primární data, protože to psali reální zákazníci.",
            "B) Jsou to Sekundární data, protože ta data už existují a leží veřejně na internetu."
        ])

        if "B)" in kviz_data:
            st.success("✅ **Přesně tak!** Tím, že data už existovala a ty si je jen 'stáhl/a' z internetu, jde o sekundární výzkum (tzv. výzkum od stolu). Kdybys těm lidem zavolal/a a položil/a jim vlastní nové otázky, šlo by o primární data.")
        elif "A)" in kviz_data:
            st.error("❌ Kdepak. Kdo data napsal, není důležité. Důležité je, zda jsi data *nově vytvořil/a*, nebo jen *převzal/a již existující*. Správně je B.")

        # ---------------------------------------------------------------------
        # 2.2.2 METODY VÝZKUMU
        # ---------------------------------------------------------------------
        st.divider()
        st.markdown("##### 2.2.2 Metody výzkumu: Jak se ptát a co sledovat")
        
        tab_v1, tab_v2, tab_v3, tab_v4 = st.tabs(["🔢 Kvantitativní", "💬 Kvalitativní", "👁️ Pozorování", "🧪 Experiment"])
        
        with tab_v1:
            st.markdown("##### Kvantitativní výzkum (Otázka: KOLIK?)")
            st.write("Pracuje s velkým počtem respondentů a výsledkem jsou tvrdá čísla, procenta a grafy.")
            st.info("📊 **Příklad:** Pošleš dotazník 300 studentům. Zjistíš, že *75 % studentů by za školní mikinu zaplatilo max 600 Kč.*")
            
        with tab_v2:
            st.markdown("##### Kvalitativní výzkum (Otázka: PROČ?)")
            st.write("Jde do hloubky. Zkoumá motivace, postoje, pocity a emoce. Nepotřebuješ stovky lidí, stačí pár, se kterými mluvíš dlouho.")
            st.warning("🗣️ **Příklad:** Pozveš 5 studentů na hloubkový rozhovor (Focus group). Zjistíš, že *mikinu nechtějí nosit proto, že se stydí za staré logo školy.*")
            
        with tab_v3:
            st.markdown("##### Pozorování")
            st.write("Lidé v dotaznících často lžou (nebo si věci pamatují jinak). Pozorování sleduje jejich **skutečné chování**.")
            st.error("👀 **Příklad:** Majitelka večerky sleduje na kamerách, že se většina studentů zastaví u regálu s energy drinky celkem na 15 vteřin, ale nakonec si vezmou levnější limonádu o regál vedle.")
            
        with tab_v4:
            st.markdown("##### Experiment (A/B Testování)")
            st.write("Změníš na trhu (nebo na webu) jednu jedinou věc a sleduješ, jak to ovlivní chování lidí.")
            st.success("💻 **Příklad:** Polovině návštěvníků e-shopu ukážeš červené tlačítko 'Koupit', druhé polovině zelené. Změříš, které generuje víc nákupů.")

        st.markdown("<br><div class='box-purple'>🧪 <b>Simulátor: Vyhodnoť svůj první A/B Test</b></div>", unsafe_allow_html=True)
        st.write("Spustil/a jsi e-shop se studentským merchem. Chtěl/a jsi zvýšit prodeje. Nasadil/a jsi experiment: polovině návštěvníků se ukázala **Varianta A**, druhé polovině **Varianta B**. Obě varianty vidělo přesně 1000 lidí. Která dopadla lépe?")

        with st.container(border=True):
            col_ab1, col_ab2 = st.columns(2)
            col_ab1.markdown("<div style='text-align:center; padding: 20px; background-color: #f1f5f9; border: 2px solid #cbd5e1; border-radius: 8px;'><b>Varianta A:</b><br>Tričko za 500 Kč<br>+ Poštovné 100 Kč</div>", unsafe_allow_html=True)
            col_ab2.markdown("<div style='text-align:center; padding: 20px; background-color: #f1f5f9; border: 2px dashed #3b82f6; border-radius: 8px;'><b>Varianta B:</b><br>Tričko za 600 Kč<br>+ Doprava ZDARMA</div>", unsafe_allow_html=True)
            
            st.write("")
            ab_tip = st.radio("Zákazník zaplatí v obou případech přesně 600 Kč. Jaká verze ale podle tebe přinesla reálně víc nákupů (konverzí)?", [
                "Vyber svůj tip...",
                "Varianta A (Nižší cena produktu vypadá na první pohled lépe).",
                "Varianta B (Slovo 'Doprava zdarma' funguje v psychologii jako magnet)."
            ])

            if "Varianta B" in ab_tip:
                st.success("✅ **Výborně! Varianta B vyhrála.** V reálných testech na e-shopech lidé bytostně nesnášejí platit za poštovné (berou to jako peníze vyhozené oknem). Raději zaplatí o stovku víc za produkt samotný, pokud vidí nápis 'ZDARMA'. Takhle marketingový výzkum vydělává peníze!")
            elif "Varianta A" in ab_tip:
                st.error("❌ Tady tě data vyvedla z omylu! Ačkoliv je matematika stejná (600 Kč), **vyhrála Varianta B**. Lidé psychologicky nesnáší placení poštovného u pokladny a často kvůli němu opustí košík. Přesně proto firmy experimenty dělají – aby nespoléhaly jen na selský rozum.")

        st.markdown("""
        <div class='box-gray' style='margin-top: 15px;'>
            📱 <b>Sociální sítě jako průběžný výzkum trhu:</b> Sítě jako TikTok, Instagram nebo YouTube ti neustále ukazují, na co lidé reagují. Počet zhlédnutí, míra dokoukání videa, komentáře nebo uložení jsou jasná analytická data. <b>Pozor ale na jednu věc:</b> Mít vysoký dosah (virál) neznamená automaticky důvěru. Tisíc zhlédnutí od relevantní cílovky prodá víc, než milion zhlédnutí od lidí, co se chtějí jen zasmát.
        </div>
        """, unsafe_allow_html=True)

        # WORKBOOK KROK 7 PRO STUDENTŮV PROJEKT
        st.markdown("<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 7: Tvůj marketingový výzkum</b></div>", unsafe_allow_html=True)
        with st.form("form_projekt_krok7"):
            st.text_area("1. Kde získáš SEKUNDÁRNÍ DATA o tvém trhu ještě před startem projektu?:", placeholder="např. Podívám se na konkurenční školní Instagramy a spočítám, jaké typy příspěvků mají nejvíce lajků.")
            st.text_area("2. Jakou metodu použiješ pro sběr PRIMÁRNÍCH DAT od tvé cílovky?:", placeholder="např. Použiji kvantitativní dotazník (Google Forms) mezi studenty 2. a 3. ročníku, abych zjistil/a max. akceptovatelnou cenu lístku na ples.")
            
            if st.form_submit_button("Uložit Krok 7 do Projektového pasu"):
                st.success("Krok 7 uložen! Než začneš utrácet peníze, víš, že musíš zjistit tvrdá data.")
# =====================================================================
        # PODKAPITOLA 2.3: STP PROCES (SEGMENTACE, TARGETING, POSITIONING)
        # =====================================================================

        st.divider()
        st.markdown("#### 2.3 STP proces: Segmentace, Cílení (Targeting) a Positioning")
        st.write("Firma nemůže prodávat všem. Lidé mají různé vkusy, potřeby i peněženky. STP proces je tříkroková strategie, jak z obřího davu vybrat přesně ty správné zákazníky a získat si pevné místo v jejich mysli.")

        col_stp1, col_str2, col_stp3 = st.columns(3)
        col_stp1.info("✂️ **S — Segmentation**\nRozdělíme trh na menší, podobné skupiny lidí.")
        col_str2.warning("🎯 **T — Targeting**\nVybereme nejvhodnější skupinu, na kterou se zaměříme.")
        col_stp3.success("📌 **P — Positioning**\nUrčíme, jak chceme být zapamatováni v hlavě zákazníka.")

        # ---------------------------------------------------------------------
        # 2.3.1 SEGMENTACE TRHU
        # ---------------------------------------------------------------------
        st.markdown("##### 2.3.1 Segmentace trhu: Rozdělení koláče")
        st.write("Segmentace rozděluje trh na menší skupiny (segmenty). Lidé v jednom segmentu mají podobné chování, potřeby a reakce na nabídku. Trh dělíme podle **4 základních kritérií**:")

        tab_seg1, tab_seg2, tab_seg3, tab_seg4 = st.tabs(["🌍 Geografická", "👥 Demografická", "🧠 Psychografická", "🛒 Behaviorální"])

        with tab_seg1:
            st.markdown("##### Geografická segmentace (KDE?)")
            st.write("Místo, region, město, stát, klima nebo typ lokality.")
            st.info("📌 **Příklad:** Nabídka kavárny v centru Prahy bude jiná než kavárna na malovesnické návsi. Prodejce zimních bund cílí na horské oblasti, ne na pobřeží Španělska.")

        with tab_seg2:
            st.markdown("##### Demografická segmentace (KDO?)")
            st.write("Věk, pohlaví, příjem, vzdělání, rodinný stav, povolání.")
            st.info("📌 **Příklad:** Bankovní účet pro studenty (zdarma), kosmetika pro teenagery s akné, rodinné balení rodinného auta, prémiové hodinky pro vysokopříjmové manažery.")

        with tab_seg3:
            st.markdown("##### Psychografická segmentace (JAK MYSLÍ?)")
            st.write("Životní styl, hodnoty, zájmy, osobnost a postoje.")
            st.info("📌 **Příklad:** Značka Patagonia cílí na lidi milující přírodu a udržitelný životní styl. Jiná značka cílí na extravagantní lidi, co chtějí šokovat okolí.")

        with tab_seg4:
            st.markdown("##### Behaviorální segmentace (JAK NAKUPUJÍ?)")
            st.write("Nákupní chování, frekvence užívání, věrnost značce, reakce na slevy.")
            st.info("📌 **Příklad:** E-shop rozlišuje zákazníky na: *lovce slev* (nakoupí jen v akcích), *loajální štamgasty* (nakupují každý měsíc) a *váhavce* (často opouštějí košík).")

        # ---------------------------------------------------------------------
        # 2.3.2 CÍLENÍ (TARGETING)
        # ---------------------------------------------------------------------
        st.divider()
        st.markdown("##### 2.3.2 Cílení (Targeting): Na koho namíříme své úsilí?")
        st.write("Jakmile máme trh rozdělený, musíme se rozhodnout, na které segmenty vložíme své peníze, čas a kapacitu.")

        col_t1, col_t2, col_t3 = st.columns(3)
        with col_t1:
            st.markdown("""
            <div style="background-color: #f8fafc; padding: 15px; border-top: 5px solid #94a3b8; border-radius: 4px; height: 100%;">
                <h5 style="margin-top:0; color: #475569;">🌊 Masový marketing</h5>
                <b>Jak funguje:</b> Oslovujeme co nejširší trh jednou univerzální nabídkou.<br><br>
                <b>Příklady:</b> Běžná balená voda, rohlíky, toaletní papír, základní saponáty.
            </div>
            """, unsafe_allow_html=True)

        with col_t2:
            st.markdown("""
            <div style="background-color: #eff6ff; padding: 15px; border-top: 5px solid #3b82f6; border-radius: 4px; height: 100%;">
                <h5 style="margin-top:0; color: #1d4ed8;">🎯 Koncentrovaný marketing</h5>
                <b>Jak funguje:</b> Soustředíme se na 1 velký konkrétní segment a přizpůsobíme mu nabídku.<br><br>
                <b>Příklady:</b> Značka běžeckého oblečení cílí výhradně na rekreační i profi běžce.
            </div>
            """, unsafe_allow_html=True)

        with col_t3:
            st.markdown("""
            <div style="background-color: #f0fdf4; padding: 15px; border-top: 5px solid #10b981; border-radius: 4px; height: 100%;">
                <h5 style="margin-top:0; color: #047857;">🔬 Nika / Níšový marketing</h5>
                <b>Jak funguje:</b> Cílíme na velmi úzkou, specifickou skupinu s jasným, opomíjeným problémem.<br><br>
                <b>Příklady:</b> Veganské proteinové tyčinky bez celeru pro lidi s celiakií a intolerancí laktózy.
            </div>
            """, unsafe_allow_html=True)

        # ---------------------------------------------------------------------
        # 2.3.3 POSITIONING A USP
        # ---------------------------------------------------------------------
        st.divider()
        st.markdown("##### 2.3.3 Positioning a USP (Unikátní prodejní argument)")
        st.write("Positioning je vytvoření jedinečného obrazu značky v mysli zákazníka. Kde 'sedíme' v jeho hlavě, když se řekne kategorie nášeho produktu?")

        st.markdown("""
        <div class='box-yellow'>
            💎 <b>USP (Unique Selling Proposition):</b> Unikátní prodejní argument. Je to jasná, stručná odpověď na otázku zákazníka: <i>„Proč si mám koupit tohle zrovna od vás a ne od deseti dalších konkurentů?“</i>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>##### 📊 Příklady úspěšného Positioningu a USP:")
        st.markdown("""
        | Značka / Produkt | Positioning v hlavě zákazníka | Unikátní prodejní argument (USP) |
        | :--- | :--- | :--- |
        | **Studentská kavárna** | Tiché a klidné studijní místo hned u školy. | Káva + zaručené místo u zásuvky + 20% sleva na ISIC. |
        | **Udržitelný merch** | Školní oblečení, které nevypadá jako levný reklamní dárek. | Lokální bio bavlna, moderní oversized střih a unikátní art design. |
        | **Aplikace na učení** | Rychlá příprava na maturitní testy bez zbytečného šprtání. | Bleskové kartičky, AI procvičování podle vlastních chyb, 10 minut denně. |
        """)

        st.markdown("<br><div class='box-purple'>🕹️ <b>Trenažér USP: Poznáš silný positioning od klišé?</b></div>", unsafe_allow_html=True)
        st.write("Otestuj své marketingové oko. Která z těchto vět představuje SKUTEČNĚ silný a zapamatovatelný positioning?")

        usp_vyber = st.radio("Vyber nejlepší vyjádření Positioningu:", [
            "Vyber odpověď...",
            "A) „Jsme mladá dynamická firma, která nabízí nejvyšší kvalitu za nejnižší ceny na trhu.“",
            "B) „Doručíme ti čerstvou horkou pizzu do 30 minut od objednání, nebo ji máš úplně ZDARMA.“",
            "C) „Záleží nám na zákazníkovi a náš zákaznický servis je vždy na prvním místě.“"
        ])

        if "B)" in usp_vyber:
            st.success("✅ **Přesně tak! B je slavné legendární USP pizzy Domino's.** Je to konkrétní, měřitelný, odvážný a snadno ověřitelný slib. Možnosti A a C jsou jen prázdná marketingová klišé, která tvrdí všichni, ale nikdo jim nevěří.")
        elif "A)" in usp_vyber or "C)" in usp_vyber:
            st.error("❌ Pozor! Fráze typu 'nejvyšší kvalita za nejnižší ceny' nebo 'zákazník na prvním místě' říká každá druhá firma na svém webu. To není positioning, ale klišé. Správná odpověď je B.")

        # WORKBOOK KROK 8 PRO STUDENTŮV PROJEKT
        st.markdown("<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 8: STP analýza tvého projektu</b></div>", unsafe_allow_html=True)
        with st.form("form_projekt_krok8"):
            st.markdown("##### 🎯 Definuj svoji Cílovou skupinu (Targeting):")
            col_stp_f1, col_stp_f2 = st.columns(2)
            with col_stp_f1:
                p_demo = st.text_input("Demografické údaje (Věk, role...):", placeholder="např. Studenti SŠ ve věku 15-19 let")
                p_psycho = st.text_input("Psychografické údaje (Zájmy, životní styl...):", placeholder="např. Zajímají se o módu, tvoří obsah na sítě")
            with col_stp_f2:
                p_typ_mkt = st.selectbox("Typ cílení:", ["Koncentrovaný (Jedna větší skupina)", "Níša / Nika (Úzká specifická skupina)", "Masový (Skoro všichni)"])

            st.markdown("##### 💎 Formuluj svoje USP a Positioning:")
            st.text_area("Proč si má zákazník vybrat tvůj projekt a ne konkurenci? Napiš 1 údernou větu (USP):", placeholder="např. Náš školní merch není jen tričko s logem, ale oversized udržitelné oblečení od návrháře ze 4.B, které chceš nosit i do města.")

            if st.form_submit_button("Uložit Krok 8 do Projektového pasu"):
                st.success("Krok 8 úspěšně uložen! Tvá značka má jasně definovaný profil a unikátní hodnotu.")
# =====================================================================
        # PODKAPITOLA 2.4: MARKETINGOVÝ MIX (4P)
        # =====================================================================

        st.divider()
        st.markdown("#### 2.4 Marketingový mix: Klasické 4P")
        st.write("Marketingový mix je soubor čtyř základních nástrojů, které firma kombinuje a ladí tak, aby oslovila vybranou cílovou skupinu a splnila své cíle.")

        col_4p1, col_4p2, col_4p3, col_4p4 = st.columns(4)
        col_4p1.info("📦 **Product**\n*(Produkt)*\nCo nabízíme a jakou hodnotu to přináší?")
        col_4p2.warning("💸 **Price**\n*(Cena)*\nKolik to stojí a jak cena ovlivní vnímání?")
        col_4p3.success("🚚 **Place**\n*(Distribuce)*\nKde a jak se produkt dostane k zákazníkovi?")
        col_4p4.error("📢 **Promotion**\n*(Propagace)*\nJak se o nás zákazník dozví a proč nám má věřit?")

        st.markdown("""
        <div class='box-blue'>
            🧩 <b>Pointa 4P: Všechno musí ladit v harmonii!</b><br>
            Prvky 4P nemohou fungovat odděleně. Luxusní hodinky s prémiovou cenou (Price) prodávané v levném plastovém obalu (Product) na stánku u nádraží (Place) působí jako fejk. Levné zboží s obří drahou kampaní zase finančně nevyjde.
        </div>
        """, unsafe_allow_html=True)

        # ---------------------------------------------------------------------
        # 2.4.1 PRODUCT / PRODUKT
        # ---------------------------------------------------------------------
        st.divider()
        st.markdown("##### 2.4.1 Product / Produkt: Nabídka hodnoty")
        st.write("Produktem je vše, co uspokojuje potřebu zákazníka — fyzické zboží, služba, aplikace, kurz nebo zážitek.")

        st.markdown("##### 🧅 Vrstvy produktu: Cibule hodnoty")
        st.write("Produkt se skládá ze tří vrstev. Zákazník si málokdy kupuje jen samotnou fyzickou věc:")

        tab_p_lay1, tab_p_lay2, tab_p_lay3 = st.tabs(["🎯 Jádro produktu", "📦 Reálný produkt", "🌟 Rozšířený produkt"])

        with tab_p_lay1:
            st.markdown("**1. Jádro produktu (Základní užitek):**")
            st.write("Základní pocit nebo potřebný užitek, kvůli kterému zákazník utrácí.")
            st.info("🚗 *Příklad Auto:* Potřeba dostat se bezpečně z bodu A do bodu B.\n\n👕 *Příklad Školní merch:* Pocit příslušnosti ke komunitě školy a vyjádření identity.")

        with tab_p_lay2:
            st.markdown("**2. Reálný produkt (Konkrétní podoba):**")
            st.write("To, na co si zákazník může sáhnout: značka, design, materiál, obal, funkce a kvalita.")
            st.warning("🚗 *Příklad Auto:* Červené SUV značky Škoda, výkon 150 koní, kožený volant.\n\n👕 *Příklad Školní merch:* Oversized mikina, černá bavlna 320g/m², vyšité logo na prsou.")

        with tab_p_lay3:
            st.markdown("**3. Rozšířený produkt (Doplňkové služby):**")
            st.write("Služby a výhody navíc, které budují věrnost a odlišují nás od konkurence.")
            st.success("🚗 *Příklad Auto:* Záruka 5 let, bezplatný servis, výhodné financování, náhradní vůz zdarma.\n\n👕 *Příklad Školní merch:* Bezplatná výměna velikosti do 30 dnů, osobní doručení do skříňky ve škole.")

        st.markdown("##### 📈 Životní cyklus produktu")
        st.write("Každý produkt na trhu se rodí, roste, dospívá a nakonec stárne. V každé fázi musí markeťáci měnit strategii:")

        # Plotly křivka životního cyklu
        faze_x = ["1. Zavádění", "2. Růst", "3. Zralost", "4. Pokles"]
        trzby_y = [10, 50, 95, 30]
        zisk_y = [-20, 30, 70, 10]

        fig_lc = go.Figure()
        fig_lc.add_trace(go.Scatter(x=faze_x, y=trzby_y, mode='lines+markers', name='Tržby (Prodeje)', line=dict(color='#3b82f6', width=4)))
        fig_lc.add_trace(go.Scatter(x=faze_x, y=zisk_y, mode='lines+markers', name='Čistý zisk', line=dict(color='#10b981', width=3, dash='dash')))

        fig_lc.update_layout(
            title="Křivka životního cyklu produktu (Tržby vs. Zisk)",
            xaxis_title="Fáze cyklu",
            yaxis_title="Hodnota (Relativní)",
            height=320,
            margin=dict(t=40, b=20, l=10, r=10)
        )
        st.plotly_chart(fig_lc, use_container_width=True)

        faze_detail = st.selectbox("🔍 Klikni a zjisti, co má firma v dané fázi dělat:", [
            "1. Zavádění (Novinka na trhu)",
            "2. Růst (Hit a raketový vzestup)",
            "3. Zralost (Vrchol a nasycení trhu)",
            "4. Pokles (Propad a zastarávání)"
        ])

        if "Zavádění" in faze_detail:
            st.error("🚀 **1. Zavádění:** Prodeje rostou pomalu, zisk je v mínusu kvůli vysokým nákladům na vývoj a reklamu. **Úkol marketingu:** Vysvětlit lidem, k čemu produkt je, a získat první nadšence.")
        elif "Růst" in faze_detail:
            st.success("📈 **2. Růst:** Tržby i zisk prudce rostou, o produkt je zájem. Přichází ale první konkurence! **Úkol marketingu:** Posilovat značku, odlišit se a rozšiřovat distribuci.")
        elif "Zralost" in faze_detail:
            st.warning("👑 **3. Zralost:** Tržby dosahují maxima, ale růst se zastavuje. Trh je nasycený a konkurence svádí cenové války. **Úkol marketingu:** Nabízet slevy, věrnostní programy, inovovat obal nebo hledat nové využití.")
        else:
            st.info("📉 **4. Pokles:** Prodeje klesají, zákazníci přecházejí na nové technologie a trendy. **Úkol marketingu:** Rozhodnout, zda produkt omladit, nebo ho včas stáhnout z prodeje.")

        # ---------------------------------------------------------------------
        # 2.4.2 PRICE / CENA
        # ---------------------------------------------------------------------
        st.divider()
        st.markdown("##### 2.4.2 Price / Cena: Jediný prvek, který vydělává")
        st.write("Zatímco produkt, distribuce a reklama stojí peníze (náklady), **Cena je jediný prvek mixu, který přináší tržby**. Zároveň skrze cenu zákazník posuzuje kvalitu.")

        st.markdown("<div class='box-purple'>🧮 <b>Trenažér: 3 metody stanovování ceny</b></div>", unsafe_allow_html=True)
        st.write("Vyzkoušej si, jak různé myšlení vede k úplně jiné cenovce u stejného produktu:")

        with st.container(border=True):
            vyrobni_naklady = 300
            st.write(f"📦 *Základní výrobní náklad na 1 kus mikiny je {vyrobni_naklady} Kč.*")
            
            c_m1, c_m2, c_m3 = st.columns(3)
            with c_m1:
                st.markdown("<b>1. Nákladová metoda</b>")
                marze_pct = st.slider("Přidáme ziskovou marži (%):", 10, 100, 50)
                cena_naklad = vyrobni_naklady * (1 + marze_pct/100)
                st.caption(f"Cena pro zákazníka: **{int(cena_naklad)} Kč**")

            with c_m2:
                st.markdown("<b>2. Konkurenční metoda</b>")
                cena_konkurence = st.number_input("Průměrná cena konkurence:", value=590, step=10)
                st.caption(f"Cena pro zákazníka: **{cena_konkurence} Kč** *(podle trhu)*")

            with c_m3:
                st.markdown("<b>3. Poptávková metoda</b>")
                st.caption("Cena vychází z vnímané hodnoty v hlavě zákazníka (limitovaná edice).")
                cena_poptavka = st.number_input("Ochota zákazníků zaplatit:", value=890, step=50)
                st.caption(f"Cena pro zákazníka: **{cena_poptavka} Kč** *(marže +{cena_poptavka-vyrobni_naklady} Kč!)*")

        st.markdown("##### 🎯 Cenové strategie u novinek")
        col_strat1, col_strat2 = st.columns(2)
        with col_strat1:
            st.markdown("""
            <div style="background-color: #eff6ff; padding: 15px; border-left: 5px solid #3b82f6; border-radius: 4px; height: 100%;">
                <h5 style="margin-top:0; color: #1d4ed8;">🌊 Skimming (Smetání smetany)</h5>
                <b>Jak funguje:</b> Nasadíme vysokou počáteční cenu pro nadšence, kteří chtějí novinku jako první. Jakmile opadne zájem, cenu postupně snižujeme.<br><br>
                <b>Příklady:</b> Nové modely iPhone, herní konzole PlayStation při vydání, vlajkové lodi televizorů.
            </div>
            """, unsafe_allow_html=True)

        with col_strat2:
            st.markdown("""
            <div style="background-color: #f0fdf4; padding: 15px; border-left: 5px solid #10b981; border-radius: 4px; height: 100%;">
                <h5 style="margin-top:0; color: #047857;">🚀 Penetrační cena (Pronikání na trh)</h5>
                <b>Jak funguje:</b> Nasadíme neobvykle nízkou počáteční cenu, abychom bleskově urvali velký podíl na trhu a získali tisíce zákazníků.<br><br>
                <b>Příklady:</b> Vstup nové streamovací služby (Disney+ za 99 Kč na startu), nová taxislužba.
            </div>
            """, unsafe_allow_html=True)

        # ---------------------------------------------------------------------
        # 2.4.3 PLACE / DISTRIBUCE
        # ---------------------------------------------------------------------
        st.divider()
        st.markdown("##### 2.4.3 Place / Distribuce: Cesta k zákazníkovi")
        st.write("Distribuce řeší, jak, kde a kdy si zákazník náš produkt nakoupí a převezme ho. Můžeš mít nejlepší produkt na světě za skvělou cenu, ale pokud je složité ho koupit, zákazník odejde ke konkurenci.")

        col_d1, col_d2 = st.columns(2)
        with col_d1:
            st.info("🛒 **Přímá cesta (Direct):**\nVýrobce prodává přímo spotřebiteli bez jakéhokoliv prostředníka.\n\n*Příklady:* Pekárna prodává ve svém krámku, tvůrce prodává e-book na svém webu, Tesla e-shop.")
        with col_d2:
            st.warning("🏬 **Nepřímá cesta (Indirect):**\nMezi výrobcem a spotřebitelem stojí zprostředkovatelé (**Velkoobchod** nakupuje po paletách, **Maloobchod** prodává po kusech).\n\n*Příklady:* Coca-Cola prodává přes Albert a Kaufland.")

        st.markdown("""
        <div class='box-gray' style='margin-top: 15px;'>
            📦 <b>Omni-channel v moderním e-commerce:</b> Moderní zákazník nerozlišuje světy online a offline. Zákazník si tenisky prohlédne na TikToku, objedná na e-shopu přes mobil, vyzvedne v kamenné prodejně na pobočce a případnou reklamaci řeší přes WhatsApp chat. Pro zákazníka to musí být <b>jeden plynulý zážitek</b>.
        </div>
        """, unsafe_allow_html=True)

        # WORKBOOK KROK 9 PRO STUDENTŮV PROJEKT
        st.markdown("<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 9: Nastavení Produktu, Ceny a Distribuce</b></div>", unsafe_allow_html=True)
        with st.form("form_projekt_krok9"):
            st.text_area("1. PRODUKT – Co bude tvořit ROZŠÍŘENÝ PRODUKT tvého projektu? (Služba/výhoda navíc):", placeholder="např. Možnost bezplatné výměny zboží do 30 dnů, věrnostní kartička s nápojem zdarma...")
            col_p_f1, col_p_f2 = st.columns(2)
            with col_p_f1:
                st.selectbox("2. CENA – Jakou metodu tvorby ceny zvolíš?:", ["Poptávková (Podle vnímané hodnoty)", "Konkurenční (Sledujeme trh)", "Nákladová (Náklady + marže)"])
            with col_p_f2:
                st.selectbox("3. DISTRIBUCE – Jakou distribuční cestu použiješ?:", ["Přímá (Vlastní e-shop / osobní prodej)", "Nepřímá (Prodej přes partnery/chovatele/stánky)", "Kombinovaná / Omni-channel"])

            if st.form_submit_button("Uložit Krok 9 do Projektového pasu"):
                st.success("Krok 9 úspěšně uložen! První 3P tvého mixu jsou kompletní.")
# ---------------------------------------------------------------------
        # 2.4.4 PROMOTION / PROPAGACE A KOMUNIKAČNÍ MIX
        # ---------------------------------------------------------------------
        st.divider()
        st.markdown("##### 2.4.4 Promotion / Propagace a komunikační mix")
        st.write("Propagace neznamená jen zaplatit si reklamu na Instagramu. Je to celá strategie, jak firma komunikuje se zákazníky, médii, veřejností a partnery. Cílem je informovat, přesvědčit, připomenout značku a budovat dlouhodobý vztah.")

        st.markdown("##### 📣 5 nástrojů komunikačního mixu")
        tab_pr1, tab_pr2, tab_pr3, tab_pr4, tab_pr5 = st.tabs([
            "📢 Reklama", 
            "🏷️ Podpora prodeje", 
            "📰 Public Relations", 
            "🤝 Osobní prodej", 
            "📩 Přímý marketing"
        ])

        with tab_pr1:
            st.markdown("**Reklama (Advertising)**")
            st.write("Placená, neosobní forma prezentace přes masmédia nebo digitální kanály. Má velký dosah, ale zákazník ví, že si ji firma zaplatila.")
            st.info("📌 **Příklady:** TV spot, billboard u dálnice, reklama na YouTube, banner na webu, placený sponzorovaný příspěvek na Instagramu nebo TikToku.")

        with tab_pr2:
            st.markdown("**Podpora prodeje (Sales Promotion)**")
            st.write("Krátkodobé stimuly a výhody, které mají zákazníka přimět k **okamžitému nákupu**.")
            st.warning("📌 **Příklady:** Slevový kupón v aplikaci, vzorek zdarma v časopise, akce 1+1 zdarma, věrnostní body, soutěž o ceny.")

        with tab_pr3:
            st.markdown("**Public Relations (PR / Vztahy s veřejností)**")
            st.write("Budování dobrého jména firmy, důvěry a vztahů s veřejností, médii a komunitou. PR prodává nepřímo přes příběh.")
            st.success("📌 **Příklady:** Tisková zpráva v novinách, rozhovor se zakladatelem v podcastu, sponzorování dětského domova, zvládnutí krizové komunikace.")

        with tab_pr4:
            st.markdown("**Osobní prodej (Personal Selling)**")
            st.write("Osobní komunikace se zákazníkem tváří v tvář nebo online. Extrémně účinná, ale drahá metoda.")
            st.error("📌 **Příklady:** Obchodní zástupce prodávající software firmám (B2B), specializovaný konzultant v prodejně elektro, video-ukázka produktu.")

        with tab_pr5:
            st.markdown("**Přímý marketing (Direct Marketing)**")
            st.write("Přímé a adresné oslovení konkrétně vybraných zákazníků z databáze.")
            st.info("📌 **Příklady:** Personalizovaný e-mailing, SMS s narozeninovou slevou, adresný katalog do schránky, nabídka přímo v mobilní aplikaci.")

        st.markdown("<br>", unsafe_allow_html=True)
        col_mkt_trend1, col_mkt_trend2 = st.columns(2)
        with col_mkt_trend1:
            st.markdown("""
            <div style="background-color: #f8fafc; padding: 15px; border-left: 5px solid #8b5cf6; border-radius: 4px; height: 100%;">
                <h5 style="margin-top:0; color: #6d28d9;">📱 Influencer marketing & UGC</h5>
                V moderní propagaci hrají obrovskou roli <b>influencer marketing</b> a <b>UGC (User-Generated Content)</b>.<br><br>
                UGC je obsah (recenze, unboxing videa, fotky), který zdarma nebo za odměnu tvoří běžní uživatelé. Působí autenticky a zákazníci mu věří více než klasické reklamě. Placené spolupráce ale musí být vždy transparentně označené!
            </div>
            """, unsafe_allow_html=True)

        with col_mkt_trend2:
            st.markdown("""
            <div style="background-color: #fff7ed; padding: 15px; border-left: 5px solid #f97316; border-radius: 4px; height: 100%;">
                <h5 style="margin-top:0; color: #c2410c;">⚠️ Virál není strategie sám o sobě</h5>
                Virální video s miliony zhlédnutí je super pro ego, ale nemusí přinést ani jedinou korunu do pokladny.<br><br>
                Pokud virál neodpovídá pozici značky, cílům a produktu, lidé si zapamatují vtipné video, ale vůbec nebudou vědět, co prodáváš nebo kdo jsi.
            </div>
            """, unsafe_allow_html=True)

        # WORKBOOK KROK 10 PRO STUDENTŮV PROJEKT
        st.markdown("<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 10: Komunikační mix a finální rekapitulace 4P</b></div>", unsafe_allow_html=True)
        with st.form("form_projekt_krok10"):
            st.markdown("##### 📢 Propagace tvého projektu:")
            st.text_area("1. Jaké 2 hlavní nástroje komunikačního mixu použiješ pro oslovení zákazníků a proč?:", placeholder="např. 1. Instagram Ads a TikTok (Reklama na zásah) + 2. Slevový kód 15 % na první nákup (Podpora prodeje na konverzi).")
            st.text_input("2. Využiješ Influencer marketing nebo UGC? Pokud ano, jak?:", placeholder="např. Pošleme 5 balíčků micro-influencerům ze školy výměnou za unboxing video.")

            st.markdown("##### 🎯 Rekapitulace finálního Marketingového mixu 4P:")
            col_4p_rec1, col_4p_rec2 = st.columns(2)
            with col_4p_rec1:
                st.caption("📦 **PRODUCT:** Hlavní hodnota produktu")
                st.caption("💸 **PRICE:** Cenová strategie a cenovka")
            with col_4p_rec2:
                st.caption("🚚 **PLACE:** Kde a jak se prodává")
                st.caption("📢 **PROMOTION:** Hlavní komunikační kanál")

            if st.form_submit_button("Uložit Krok 10 a dokončit Blok 2 (Marketing)"):
                st.success("🎉 Gratulujeme! Blok 2 (Marketing) je kompletně zpracovaný. Tvůj projekt má jasný produkt, cenovku, distribuci i promo kampaň!")
# =========================================================================
    # SEKCE 3: BRAND, NÁKUPNÍ PSYCHOLOGIE A ETIKA
    # =========================================================================
    elif selected_section_6 == section_options_6[2]:
        st.markdown("### 3. Brand, nákupní psychologie a etika")

        st.markdown("""
        <div class='box-blue'>
            🧠 <b>Moderní hook:</b> <i>„Jak tě značky nutí utrácet peníze, které nemáš, za věci, které nepotřebuješ?“</i><br>
            Marketing nepracuje jen s chladnými číslicemi v tabulkách. Pracuje s lidskými emocemi, pozorností, touhou patřit do komunity a stavěním vlastní identity. Značka je to, co mění obyčejné zboží v objekt touhy. Proto je nutné rozumět tomu, kde končí přesvědčování a začíná manipulace.
        </div>
        """, unsafe_allow_html=True)

        st.divider()

        # =====================================================================
        # PODKAPITOLA 3.1: ZNAČKA A BUDOVÁNÍ BRANDU
        # =====================================================================
        st.markdown("#### 3.1 Značka a budování brandu")
        st.write("Značka neboli **brand** není jen grafické logo nebo název vyražený na krabičce. Je to soubor všech představ, emocí, paměťových stop, zkušeností a asociací, které si lidé s produktem nebo firmou spojují v hlavě. Fyzický produkt může mít identické parametry jako konkurenční výrobek, ale značka rozhoduje o tom, jak mu zákazník věří a kolik je za něj ochoten zaplatit.")

        st.markdown("""
        <div class='box-yellow'>
            🧠 <b>Jednoduše (Rozdíl mezi produktem a značkou):</b><br>
            • <b>Produkt</b> je to, co firma fyzicky vyrábí nebo poskytuje (např. látka, plast, kód).<br>
            • <b>Značka</b> je to, co si o tom zákazník myslí, co při tom cítí a jakou hodnotu tomu přisuzuje.
        </div>
        """, unsafe_allow_html=True)

        # Trenažér vnímané hodnoty
        st.markdown("<div class='box-purple'>🕹️ <b>Trenažér vnímané hodnoty: Příběh jednoho trička</b></div>", unsafe_allow_html=True)
        st.write("Podívej se, jak značka mění ochotu zákazníka zaplatit za stejný základní materiál:")

        with st.container(border=True):
            col_t1, col_t2 = st.columns(2)
            with col_t1:
                st.markdown("""
                <div style='background-color: #f8fafc; padding: 15px; border-radius: 8px; border: 1px solid #e2e8f0; text-align: center;'>
                    <h5>👕 Obyčejné bílé tričko</h5>
                    <b>Materiál:</b> 100% bavlna, 180g/m²<br>
                    <b>Obal:</b> Plastový sáček<br>
                    <b>Značka:</b> Bez značky (no-name)<br><br>
                    <h4 style='color: #475569;'>Cena: 150 Kč</h4>
                </div>
                """, unsafe_allow_html=True)
            with col_t2:
                st.markdown("""
                <div style='background-color: #fef2f2; padding: 15px; border-radius: 8px; border: 1px solid #fca5a5; text-align: center;'>
                    <h5>🔥 Značkové oversized tričko</h5>
                    <b>Materiál:</b> 100% bavlna, 180g/m² (stejný materiál)<br>
                    <b>Obal:</b> Designová krabice s nálepkami<br>
                    <b>Značka:</b> Světová streetwear značka / merch influencera<br><br>
                    <h4 style='color: #b91c1c;'>Cena: 2 500 Kč</h4>
                </div>
                """, unsafe_allow_html=True)

            st.caption("👉 *Materiál i základní užitek (zakrytí těla) jsou totožné. Zákazník ale neplatí 2 500 Kč za bavlnu, ale za POCIT, status, příslušnost ke komunitě a styl.*")

        # ---------------------------------------------------------------------
        # 3.1.1 ANATOMIE A PRVKY ZNAČKY
        # ---------------------------------------------------------------------
        st.divider()
        st.markdown("##### 3.1.1 Anatomie a prvky značky")
        st.write("Silná značka nevzniká náhodou. Je to pečlivě poskládaná mozaika z několika prvků, které musí fungovat v naprosté harmonii:")

        tab_b1, tab_b2, tab_b3, tab_b4, tab_b5 = st.tabs([
            "🎨 Vizuální identita", 
            "🔊 Audio & Senzorika", 
            "📖 Storytelling", 
            "🚀 Mise a Vize", 
            "💎 Hodnoty"
        ])

        with tab_b1:
            st.markdown("**Vizuální identita (To, co vidíme)**")
            st.write("Všechny vizuální prvky: název, logo, typografie (písmo), paleta barev, obaly a jednotný grafický styl na sociálních sítích a webu.")
            st.info("📌 **Příklad:** Typická tyrkysová barva Dáme jídlo / Foodora, červené logo Coca-Coly, minimalistický design Apple boxů.")

        with tab_b2:
            st.markdown("**Audio & Senzorická identita (To, co slyšíme a cítíme)**")
            st.write("Zvuky, znělky, hlas značky nebo typické vůně v prodejnách.")
            st.warning("📌 **Příklad:** Znělka Netflixu (*„Tudum“*), zvuk nastartování počítače Mac, charakteristická vůně v prodejnách Abercrombie & Fitch.")

        with tab_b3:
            st.markdown("**Storytelling (Příběh značky)**")
            st.write("Příběh o tom, proč značka vznikla, jaké překážky zakladatelé překonali a jaký problém ve světě chce řešit.")
            st.success("📌 **Příklad:** Příběh garážového vzniku Apple, česká značka Fusakle vracející výrobu ponožek do ČR, příběh nápoje Red Bull a extrémních sportů.")

        with tab_b4:
            st.markdown("**Mise a Vize (Smysl a cíl)**")
            st.write("• **Mise:** Říká, proč značka existuje DNES a co dělá pro své zákazníky.\n• **Vize:** Dlouhodobý sen a cíl, kam chce značka směřovat v BUDOUCNOSTI.")
            st.info("📌 **Příklad Google:** *Mise:* Uspořádat informace celého světa a učinit je univerzálně přístupné. *Vize:* Poskytnout přístup k informacím jedním kliknutím komukoliv na Zemi.")

        with tab_b5:
            st.markdown("**Hodnoty značky (Etický kompas)**")
            st.write("Zásadní principy, ze kterých značka nikdy nesleví a podle kterých dělá těžká rozhodnutí.")
            st.error("📌 **Příklad:** Udržitelnost, inovativnost, dostupnost pro všechny, nekompromisní kvalita, transparentnost.")

        st.markdown("""
        <div class='box-gray' style='margin-top: 15px;'>
            📌 <b>Pozor na past:</b> Mít hezké logo neznamená mít silnou značku. Pokud se komunikace značky rozchází s realitou (např. značka tvrdí, že je eko, ale balí věci do tří vrstev plastu), zákazník okamžitě ztratí důvěru.
        </div>
        """, unsafe_allow_html=True)

        # ---------------------------------------------------------------------
        # 3.1.2 BRAND EQUITY A BRAND LOYALTY
        # ---------------------------------------------------------------------
        st.divider()
        st.markdown("##### 3.1.2 Brand equity a brand loyalty")
        st.write("Dva klíčové pojmy, které rozhodují o finanční hodnotě a stabilitě firmy:")

        col_be1, col_be2 = st.columns(2)
        with col_be1:
            st.markdown("""
            <div style="background-color: #f0fdf4; padding: 15px; border-left: 5px solid #10b981; border-radius: 4px; height: 100%;">
                <h5 style="margin-top: 0; color: #047857;">📈 Brand Equity (Hodnota značky)</h5>
                <b>Co to je:</b> Dodatečná finanční i nefinanční hodnota, kterou jméno značky přidává k základnímu produktu.<br><br>
                <b>Projev v praxi:</b> Zákazník je ochoten zaplatit vyšší cenu jen za známe jméno, banky firmě snáze půjčí a dodavatelé dají lepší podmínky.
            </div>
            """, unsafe_allow_html=True)

        with col_be2:
            st.markdown("""
            <div style="background-color: #eff6ff; padding: 15px; border-left: 5px solid #3b82f6; border-radius: 4px; height: 100%;">
                <h5 style="margin-top: 0; color: #1d4ed8;">❤️ Brand Loyalty (Věrnost značce)</h5>
                <b>Co to je:</b> Stupeň věrnosti a emocionálního přimknutí zákazníka ke značce.<br><br>
                <b>Projev v praxi:</b> Zákazník neporovnává ceny u konkurence. Nakupuje opakovaně, nosí merch, brání značku v diskusích na sítích a doporučuje ji přátelům.
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br><div class='box-purple'>👥 <b>Síla komunity značky (Brand Community)</b></div>", unsafe_allow_html=True)
        st.write("Nejvyšší možná úroveň brand loyalty vzniká ve chvíli, kdy kolem značky vznikne **komunita**. Zákazníci se už neztotožňují jen s produktem, ale s ostatními lidmi, kteří značku používají.")
        st.caption("👉 *Příklady: Řidiči Harley-Davidson, fanoušci Apple vs. Android, komunity kolem CrossFitu nebo zákazníci lokální kavárny.*")

        # WORKBOOK KROK 11 PRO STUDENTŮV PROJEKT
        st.markdown("<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 11: Identita a Příběh tvé značky</b></div>", unsafe_allow_html=True)
        with st.form("form_projekt_krok11"):
            st.text_area("1. STORYTELLING – Jaký je příběh tvé značky? (Proč tvůj projekt vznikl a jaký problém řeší?):", placeholder="např. Náš projekt vznikl v rohu školní knihovny, když jsme si uvědomili, že v bufetu chybí zdravé a dostupné jídlo pro studenty...")
            col_b_f1, col_b_f2 = st.columns(2)
            with col_b_f1:
                st.text_input("2. MISE ZNAČKY (Co děláte dnes pro zákazníka):", placeholder="např. Přinášet studentům energii bez cukrového dojezdu.")
                st.text_input("3. HODNOTY ZNAČKY (3 klíčová slova):", placeholder="např. Autenticita, Čerstvost, Zábava")
            with col_b_f2:
                st.text_input("4. VIZUÁLNÍ A AUDIO IDENTITA (Barvy, styl, zvuk):", placeholder="např. Neony, černá a limetkově zelená, lo-fi hudba na pozadí")
                st.selectbox("5. BRAND LOYALTY STRATEGIE:", ["Odměny za věrnost (Slevy/Kartičky)", "Exkluzivní komunita (Discord/Instagram)", "UGC - Sdílení obsahu zákazníků"])

            if st.form_submit_button("Uložit Krok 11 do Projektového pasu"):
                st.success("Krok 11 úspěšně uložen! Tvá značka má svůj příběh, vizi i jasnou tvář.")
# ---------------------------------------------------------------------
        # 3.1.3 STRATEGIE ZNAČKY: REBRANDING A EXTENZE ZNAČKY
        # ---------------------------------------------------------------------
        st.divider()
        st.markdown("##### 3.1.3 Strategie značky: Rebranding a Extenze značky")
        st.write("Jakmile značka na trhu vyroste, čelí dvěma výzvám: jak zůstat moderní pro novou generaci (**Rebranding**) a jak využít své dobré jméno pro nové produkty (**Extenze značky**).")

        col_str1, col_str2 = st.columns(2)
        with col_str1:
            st.markdown("""
            <div style="background-color: #f8fafc; padding: 15px; border-left: 5px solid #3b82f6; border-radius: 4px; height: 100%;">
                <h5 style="margin-top: 0; color: #1e40af;">🔄 Rebranding (Změna tváře)</h5>
                <b>Co to je:</b> Změna image značky – od nového loga, barev a vizuálu až po celkový tón komunikace.<br><br>
                <b>Kdy se dělá:</b> Značka působí zastarale, chce oslovit mladší generaci, změnila majitele nebo napravuje poškozenou reputaci.<br><br>
                <b>Příklad:</b> McDonald's změnil podklad loga z červené na tmavě zelenou, aby působil více ekologicky a prémiově.
            </div>
            """, unsafe_allow_html=True)

        with col_str2:
            st.markdown("""
            <div style="background-color: #fef3c7; padding: 15px; border-left: 5px solid #f59e0b; border-radius: 4px; height: 100%;">
                <h5 style="margin-top: 0; color: #b45309;">🌿 Extenze značky (Využití dobrého jména)</h5>
                <b>Co to je:</b> Rozšíření známé značky do úplně nové kategorie produktů.<br><br>
                <b>Výhody:</b> Novinka hned od startu těží z důvěry existující značky.<br>
                <b>Riziko (Rozmělnění značky):</b> Pokud se rozšíření nepovede nebo nedává smysl, poškodí to i původní značku.<br><br>
                <b>Příklad:</b> Značka sportovního oblečení začne prodávat hodinky nebo parfémy.
            </div>
            """, unsafe_allow_html=True)

        # =====================================================================
        # PODKAPITOLA 3.2: NÁKUPNÍ CHOVÁNÍ A PSYCHOLOGIE SPOTŘEBITELE
        # =====================================================================
        st.divider()
        st.markdown("#### 3.2 Nákupní chování a psychologie spotřebitele")
        st.write("Nákupní chování zkoumá, jak se lidé rozhodují při utrácení peněz, co je ovlivňuje a proč si vyberou konkrétní produkt. **Člověk se málokdy rozhoduje 100% racionálně.** Do nákupu masivně vstupují emoce, společenský tlak, strach z vyčlenění, nálada i okamžité impulzy.")

        # ---------------------------------------------------------------------
        # 3.2.1 PROCES NÁKUPNÍHO ROZHODOVÁNÍ
        # ---------------------------------------------------------------------
        st.markdown("##### 3.2.1 Proces nákupního rozhodování (5 fází)")
        st.write("Každý větší nákup probíhá v pěti na sebe navazujících krokách:")

        tab_dec1, tab_dec2, tab_dec3, tab_dec4, tab_dec5 = st.tabs([
            "1️⃣ Rozpoznání potřeby", 
            "2️⃣ Hledání informací", 
            "3️⃣ Hodnocení alternativ", 
            "4️⃣ Nákupní rozhodnutí", 
            "5️⃣ Poprodejní chování"
        ])

        with tab_dec1:
            st.markdown("**1. Rozpoznání potřeby (Uvědomění problému)**")
            st.write("Zákazník si uvědomí rozdíl mezi současným stavem a tím, co by chtěl mít.")
            st.info("💻 *Příklad:* Studentovi praskne displej na starém notebooku nebo zjistí, že současný počítač nestíhá školní programy.")

        with tab_dec2:
            st.markdown("**2. Hledání informací (Průzkum)**")
            st.write("Zákazník zjišťuje možnosti, čte recenze, sleduje videa na YouTube, ptá se kamarádů nebo hledá na Heurece.")
            st.warning("🔍 *Příklad:* Student sleduje srovnávací recenze notebooků do 15 000 Kč a ptá se spolužáků v chatu.")

        with tab_dec3:
            st.markdown("**3. Hodnocení alternativ (Porovnávání)**")
            st.write("Porovnává kritéria: cena, výkon, značka, design, záruka, výdrž baterie.")
            st.error("⚖️ *Příklad:* Rozhoduje se mezi lehkým notebookem s dlouhou výdrží baterie a výkonnějším, ale těžším modelem.")

        with tab_dec4:
            st.markdown("**4. Nákupní rozhodnutí (Akce)**")
            st.write("Vybere konkrétní produkt a provede nákup v e-shopu nebo kamenné prodejně.")
            st.success("🛒 *Příklad:* Vloží vybraný notebook do košíku, zvolí platbu a doručení do Zásilkovny.")

        with tab_dec5:
            st.markdown("**5. Poprodejní chování (Vyhodnocení a kognitivní disonance)**")
            st.write("Po nákupu vyhodnocuje spokojenost. Zde vzniká buď radost a doporučení, nebo pochybnosti.")

        st.markdown("""
        <div class='box-purple' style='margin-top: 15px;'>
            🧠 <b>Kognitivní disonance (Nákupní výčitky):</b><br>
            Je to nepříjemný pocit pochybnosti těsně po drahém nákupu: <i>„Utratil/a jsem zbytečně moc peněz? Neměl/a jsem koupit raději jiný model?“</i><br>
            <b>Co dělají moudré firmy:</b> Posílají e-mail s ubezpečením (<i>„Skvělá volba! Tady je návod, jak z notebooku vytěžit maximum“</i>), dávají prodlouženou záruku a nabízejí snadné vrácení zboží.
        </div>
        """, unsafe_allow_html=True)

        # ---------------------------------------------------------------------
        # 3.2.2 FAKTORY OVLIVŇUJÍCÍ NÁKUPNÍ CHOVÁNÍ
        # ---------------------------------------------------------------------
        st.divider()
        st.markdown("##### 3.2.2 Faktory ovlivňující nákupní chování")
        st.write("Nákupní rozhodnutí ovlivňují 4 hlavní skupiny vlivů:")

        col_f1, col_f2 = st.columns(2)
        with col_f1:
            st.markdown("""
            <div style="background-color: #f8fafc; padding: 15px; border-left: 5px solid #3b82f6; border-radius: 4px; height: 100%;">
                <h5 style="margin-top: 0; color: #1e40af;">🧑 Osobní faktory</h5>
                Věk, příjem, životní fáze, povolání, životní styl, vzdělání a zkušenosti.<br><br>
                <i>Příklad: Student, rodič samoživitel a generální ředitel mají úplně jiné nákupní priority a finanční limity.</i>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div style="background-color: #fef3c7; padding: 15px; border-left: 5px solid #f59e0b; border-radius: 4px; height: 100%; margin-top: 10px;">
                <h5 style="margin-top: 0; color: #b45309;">🧠 Psychologické faktory</h5>
                Vnímání, postoje, motivace, emoce, osobnost a potlačené potřeby.<br><br>
                <i>Příklad: Maslowova pyramida vysvětluje, proč někdo kupuje jídlo pro přežití, zatímco jiný si kupuje luxusní značku pro uznání.</i>
            </div>
            """, unsafe_allow_html=True)

        with col_f2:
            st.markdown("""
            <div style="background-color: #f0fdf4; padding: 15px; border-left: 5px solid #10b981; border-radius: 4px; height: 100%;">
                <h5 style="margin-top: 0; color: #047857;">👥 Sociální faktory</h5>
                Rodina, přátelé, vrstevníci, influenceři, celebrity a <b>referenční skupiny</b>.<br><br>
                <i>Příklad: Teenager si koupí konkrétní boty ne proto, že jsou nejlepší, ale proto, že je nosí všichni v jeho partě.</i>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div style="background-color: #eff6ff; padding: 15px; border-left: 5px solid #6366f1; border-radius: 4px; height: 100%; margin-top: 10px;">
                <h5 style="margin-top: 0; color: #4338ca;">🌍 Kulturní faktory</h5>
                Kultura, podkultura, hodnoty společnosti, tradice a náboženské normy.<br><br>
                <i>Příklad: V některých zemích jsou symbolem statusu drahá auta, v jiných udržitelnost a střídmý životní styl.</i>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        <div class='box-gray' style='margin-top: 15px;'>
            👥 <b>Co je to Referenční skupina?:</b> Je to skupina lidí, se kterými se člověk porovnává nebo ke kterým chce patřit (např. spolužáci, herní komunita, lidé z fitka, oblíbený streamer). Doporučení od referenční skupiny funguje 10× silněji než běžná reklama.
        </div>
        """, unsafe_allow_html=True)

        # WORKBOOK KROK 12 PRO STUDENTŮV PROJEKT
        st.markdown("<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 12: Psychologie a Nákupní cesta tvého zákazníka</b></div>", unsafe_allow_html=True)
        with st.form("form_projekt_krok12"):
            st.text_area("1. ROZPOZNÁNÍ POTŘEBY – Jaký konkrétní 'spouštěč' nebo problém přiměje zákazníka hledat tvůj produkt?:", placeholder="např. Zákazníkovi dojde šťáva před důležitou zkouškou / nemá co nosit na školní akce...")
            col_b_p1, col_b_p2 = st.columns(2)
            with col_b_p1:
                st.text_input("2. REFERENČNÍ SKUPINA (Kdo ovlivňuje jeho nákup?):", placeholder="např. Spolužáci ze třídy, známí tiktokeři")
            with col_b_p2:
                st.text_input("3. OBRANA PROTI KOGNITIVNÍ DISONANCI (Jak ho uklidníš po nákupu?):", placeholder="např. Pošleme děkovný e-mail s dárkovým stickerem")

            if st.form_submit_button("Uložit Krok 12 do Projektového pasu"):
                st.success("Krok 12 úspěšně uložen! Máš zmapované chování i psychologii svého zákazníka.")
# ---------------------------------------------------------------------
        # 3.2.3 RACIONÁLNÍ VS. EMOČNÍ A IMPULZIVNÍ NÁKUPY
        # ---------------------------------------------------------------------
        st.divider()
        st.markdown("##### 3.2.3 Racionální vs. emoční a impulzivní nákupy")
        st.write("Zákazníci rádi věří, že nakupují chladně a logicky. Psychologie ale ukazuje, že **většina nákupních rozhodnutí vzniká na základě emocí** a rozum následně dodatečně hledá argumenty, jak si nákup obhájit.")

        col_em1, col_em2, col_em3 = st.columns(3)
        col_em1.info("📊 **Racionální nákup**\nZaložený na faktech, specifikaci, ceně a porovnání recenzí.\n\n*Příklad:* Výběr kalkulačky na maturitu podle povolených funkcí.")
        col_em2.warning("❤️ **Emoční nákup**\nZaložený na touze, pocitu, statusu, identitě nebo strachu (FOMO).\n\n*Příklad:* Limitovaná edice tenisek od oblíbeného rappera.")
        col_em3.error("⚡ **Impulzivní nákup**\nBleskové rozhodnutí bez plánování vyvolané podnětem v daný moment.\n\n*Příklad:* Sladkost u pokladny, 'poslední 2 kusy na skladě!'.")

        st.markdown("<div class='box-purple'>🕹️ <b>Trenažér nákupního typu: Co tě přimělo k nákupu?</b></div>", unsafe_allow_html=True)
        st.write("Poznáš, jaký typ motivace stál za tímto nákupem?")

        nakup_scenar = st.radio("Jdeš kolem kavárny, ucítíš čerstvou vůni skořicových šneků a uvidíš ceduli 'Poslední 3 kusy z dnešního pečení!'. Ačkoliv nemáš hlad, okamžitě si jednoho koupíš.", [
            "Vyber odpověď...",
            "A) Racionální nákup – vyhodnotil/a jsi výživovou hodnotu a cenu.",
            "B) Kombinace Emočního a Impulzivního nákupu (vůně + pocit nedostatku).",
            "C) Plánovaný nákup."
        ])

        if "B)" in nakup_scenar:
            st.success("✅ **Přesně tak!** Smyslový podnět (vůně) a psychologický tlak (nedostatek) vyvolal impulzivní emoční reakci. Rozum byl v tu chvíli na druhé koleji.")
        elif "A)" in nakup_scenar or "C)" in nakup_scenar:
            st.error("❌ Kdepak! Vůně a limitovaný počet kusů útočí na emoce a impulzivitu, ne na chladnou logiku. Správně je B.")

        # ---------------------------------------------------------------------
        # 3.2.4 NEUROMARKETING
        # ---------------------------------------------------------------------
        st.divider()
        st.markdown("##### 3.2.4 Neuromarketing: Tlačítka v lidském mozku")
        st.write("Neuromarketing zkoumá, jak podvědomí spotřebitele reaguje na barvy, zvuky, vůně, rozložení prodejny, slova nebo tvar tlačítka na webu. Využívá poznatky neurověd k tomu, aby značka snáze získala pozornost.")

        st.markdown("""
        <div class='box-blue'>
            🧠 <b>Jak neuromarketing funguje v praxi:</b><br>
            • <b>Červená a oranžová barva:</b> Vyvolávají pocit naléhavosti (akce, výprodej, tlačítko 'Koupit').<br>
            • <b>Pomalá hudba v supermarketu:</b> Podvědomě zpomaluje krok zákazníků, ti stráví v obchodě více času a utratí více peněz.<br>
            • <b>Příjemná vůně pečiva u vchodu:</b> Aktivuje podvědomý pocit hladu a bezpečí.<br>
            • <b>Rozložení webu:</b> Oči čtou po tvaru písmene 'F' – klíčové tlačítko musí být v pravém horním nebo středním zorném poli.
        </div>
        """, unsafe_allow_html=True)

        # ---------------------------------------------------------------------
        # 3.3 ETIKA, PRÁVO A OCHRANA SPOTŘEBITELE
        # ---------------------------------------------------------------------
        st.divider()
        st.markdown("#### 3.3 Etika, právo a ochrana spotřebitele")
        st.write("Marketing má obrovský vliv na chování společnosti. Proto musí mít jasné hranice. Etický a legální marketing nesmí zákazníka klamat, manipulovat ani zneužívat jeho neznalost.")

        st.markdown("##### 3.3.1 Právní rámec reklamy v ČR a EU")
        st.write("Podnikání a reklama podléhají přísným zákonům na ochranu spotřebitele a férové hospodářské soutěže:")

        tab_l1, tab_l2, tab_l3, tab_l4 = st.tabs(["⚖️ Zákon o regulaci reklamy", "🚫 Nekalá soutěž & Klamání", "📢 Srovnávací reklama", "🕵️ Skrytá reklama & Influencer marketing"])

        with tab_l1:
            st.markdown("**Zákon o regulaci reklamy (Omezení pro citlivá odvětví)**")
            st.write("Přísně reguluje nebo zakazuje reklamu na produkty, které mohou ohrozit zdraví nebo bezpečnost.")
            st.error("📌 **Příklady:** Reklama na alkohol nesmí vyvolávat dojem, že pití zvyšuje společenský nebo sexuální úspěch. Zákaz reklamy na cigarety, omezení hazardu, přísné podmínky pro energetické nápoje a léky.")

        with tab_l2:
            st.markdown("**Nekalá soutěž a klamavá reklama**")
            st.write("Chrání poctivé podnikatele i spotřebitele před lží. Reklama nesmí uvádět nepravdivé nebo zavádějící informace.")
            st.warning("📌 **Příklady:** Firma tvrdí, že prodává '100% bio lokální produkt', ale surovinou je levný dovoz z Asie. Zákaz parazitování na pověsti cizí značky.")

        with tab_l3:
            st.markdown("**Srovnávací reklama**")
            st.write("Porovnávat se s konkurencí je dovoleno, ale jen za velmi přísných podmínek.")
            st.info("📌 **Pravidlo:** Srovnání musí být **pravdivé, objektivní, ověřitelné** a nesmí konkurenci očerňovat nebo zesměšňovat.")

        with tab_l4:
            st.markdown("**Skrytá reklama a povinnost označovat spolupráce**")
            st.write("Komerční sdělení nesmí být maskováno jako 'nezávislé doporučení' nebo 'osobní názor'. Zákazník musí ihned poznat, že jde o reklamu.")
            st.success("📌 **Pravidlo pro influencery:** Placená spolupráce, sponzorovaný produkt nebo bartering musí být v příspěvku/videu jasně a viditelně označen (např. *#spoluprace*, *Placená propagace*). Nestačí to schovat mezi 30 dalších hashtagů!")

        st.markdown("<br><div class='box-purple'>⚖️ <b>Detektivní aréna: Najdeš právní nebo etický průšvih?</b></div>", unsafe_allow_html=True)
        st.write("Přečti si 3 reálné marketingové situace a urči, která porušuje pravidla:")

        scenar_pravo = st.selectbox("Vyber situaci k posouzení:", [
            "1. Tiktokerka natáčí 'ranní rutinu' a líčí se řasenkou. Do videa řekne: 'Tuhle řasenku naprosto miluju, doporučuji všem!'. V popisku videa chybí jakákoliv zmínka o tom, že za video dostala 15 000 Kč od kosmetické značky.",
            "2. Značka minerálek napíše na billboard: 'Náš nápoj obsahuje o 20 % více hořčíku než běžné pramenité vody v ČR' a na webu zveřejní odkaz na nezávislou laboratorní analýzu.",
            "3. E-shop se školními potřebami dá týden před začátkem školního roku slevu 20 % na vybrané batohy a napíše 'Sezónní slevová akce'."
        ])

        if "1." in scenar_pravo:
            st.error("🚨 **PRÁVNÍ A ETICKÝ PRŮŠVIH (Skrytá reklama)!** Influencerka přijala finanční odměnu, ale předstírala nezávislé doporučení. Jedná se o skrytou reklamu a klamání spotřebitele, za které hrozí pokuta jak influencerovi, tak zadavateli reklamy.")
        elif "2." in scenar_pravo:
            st.success("✅ **V POŘÁDKU.** Jedná se o povolenou srovnávací reklamu. Srovnání je objektivní, pravdivé a podložené ověřitelnou analýzou.")
        else:
            st.success("✅ **V POŘÁDKU.** Běžná slevová akce v rámci podpory prodeje, pokud e-shop uměle nezdražil cenu den předem.")

        # WORKBOOK KROK 13 PRO STUDENTŮV PROJEKT
        st.markdown("<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 13: Neuromarketing a Etický kodex projektu</b></div>", unsafe_allow_html=True)
        with st.form("form_projekt_krok13"):
            st.text_area("1. NEUROMARKETING – Jaký smyslový nebo psychologický podnět použiješ pro svůj projekt?:", placeholder="např. Použijeme výrazné kontrastní žluté tlačítko na webu + příjemnou znělku v úvodu podcastu.")
            st.text_area("2. ETIKA A PRÁVO – Jak zajistíš, aby kampaň tvého projektu nebyla klamavá a dodržovala pravidla?:", placeholder="např. Všechny sponzorované příspěvky od studentů budou v prvním řádku popisku mít jasné označení #spoluprace.")

            if st.form_submit_button("Uložit Krok 13 do Projektového pasu"):
                st.success("Krok 13 úspěšně uložen! Tvůj projekt je nejen atraktivní, ale i etický a právně čistý.")
