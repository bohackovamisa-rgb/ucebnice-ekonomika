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
    st.write("Teorie bez praxe je k ničemu. V této kapitole si vybereš **jeden mikro-projekt**, který budeš postupně rozvíjet v každém bloku. Na konci kapitoly budeš mít kompletní podklady pro svůj vlastní startup nebo akční plán!")

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
        ], key="k6_typ_projektu")

        if "Vlastní nápad" in typ_projektu:
            nazev_projektu = st.text_input("Napiš název a stručný popis svého vlastního projektu:", value="Můj nový startup", key="k6_custom_nazev")
        else:
            nazev_projektu = typ_projektu.split(" ", 1)[1]

        c_p1, c_p2, c_p3 = st.columns(3)
        c_p1.info("**Blok 1: Management**\nDoplníš týmové role, styl řízení, plán, rizika a SWOTku.")
        c_p2.warning("**Blok 2: Marketing**\nUrčíš cílovku (STP) a nastavíš marketingový mix 4P.")
        c_p3.success("**Blok 3: Brand & Etika**\nVytvoříš identitu značky, logo a etickou kampaň.")

        st.markdown(f"<div style='background-color: #f8fafc; padding: 12px; border-radius: 8px; border: 1px dashed #cbd5e1; text-align: center; margin-top: 10px;'>📌 <b>Aktivní projektový pas:</b> <span style='color: #8b5cf6; font-weight: bold;'>{nazev_projektu}</span></div>", unsafe_allow_html=True)

        if st.button("Uložit výběr projektu 💾", key="btn_k6_save_project"):
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"]("Kapitola 6", "Inkubátor - Výběr projektu", f"Projekt: {nazev_projektu}")
            st.success(f"Projekt '{nazev_projektu}' byl zaregistrován!")

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

    st.markdown("📌 <strong>Přechod na podkapitolu:</strong>", unsafe_allow_html=True)
    selected_section_6 = st.selectbox("Přechod na podkapitolu:", section_options_6, index=0, label_visibility="collapsed", key="k6_section_select")

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

        # PODKAPITOLA 1.1
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
            st.info("📌 **Příklady:** Vedoucí týmu, ředitel školy, manažer prodejny.")

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
            
            sara_role = st.radio("Vyber správnou odpověď:", [
                "Vyber odpověď...",
                "A) Je pouze zaměstnankyní své vlastní firmy.",
                "B) Je zároveň Podnikatelka, Vlastník i Manažerka.",
                "C) Je pouze Podnikatelka, řízení lidi pod ni nespadá."
            ], key="k6_1_sara_role")

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
        st.write("Ve větších firmách a organizacích neřeší všichni manažeři to samé. Řízení se dělí do tří základních úrovní, které tvoří tzv. **Pyramidu řízení**:")

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
                <b>Lidé:</b> Mistr ve výrobně, vedoucí směny v McDonald's, team leader brigádníků.<br><br>
                <b>Otázka:</b> <i>Kdo dnes co udělá a jak?</i>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br><div class='box-purple'>🎪 <b>Simulátor pyramidy: Školní benefiční festival</b></div>", unsafe_allow_html=True)
        st.write("Klikni na úroveň řízení a podívej se, jak se rozhodování projevuje na reálném projektu:")

        uroven_sim = st.radio("Vyber úroveň řízení pro školní festival:", [
            "🔴 Top management (Ředitel školy + Hlavní koordinátor)",
            "🟡 Middle management (Vedoucí kapel, Vedoucí občerstvení, Vedoucí PR)",
            "🟢 First-line management (Team leader u vstupu / u stánku s pitím)"
        ], key="k6_1_1_sim_uroven")

        if "Top" in uroven_sim:
            st.error("🏛️ **Rozhodnutí Top managementu:** 'Schvalujeme konání festivalu na 20. června. Cílem je vybrat 100 000 Kč na útulek a získat pro školu skvělé jméno. Schvalujeme celkový rozpočet 50 000 Kč.'")
        elif "Middle" in uroven_sim:
            st.warning("📊 **Rozhodnutí Middle managementu:** 'Sestavili jsme harmonogram vystoupení 5 kapel. Vedoucí PR zajistí plakáty na Instagramu, vedoucí občerstvení domluvil sponzora na nápoje.'")
        else:
            st.success("🛠️ **Rozhodnutí First-line managementu:** 'Ahoj týme! Jirka bude od 14:00 trhat lístky u brány, Terka bude prodávat párečky v rohlíku. Zkontrolujte si, že máte dost drobných na vrácení!'")

        st.divider()

        # WORKBOOK KROK 1
        st.markdown("<div class='box-yellow'>📝 <b>Projektový pas – Krok 1: Rozdělení rolí v tvém projektu</b></div>", unsafe_allow_html=True)
        st.write("Vrať se ke svému projektu zvolenému v úvodu kapitoly a nastav pro něj základní řídící strukturu:")

        with st.form("form_projekt_krok1"):
            k1_top = st.text_input("1. Kdo bude v tvém projektu zastávat roli Top managementu (vize a strategie)?:", placeholder="např. Já jako zakladatel + můj spoluzakladatel", key="k6_k1_top")
            k1_middle = st.text_input("2. Jaká oddělení / Middle management budeš v projektu potřebovat?:", placeholder="např. Výroba/Obsah, Marketing, Finance/Logistika", key="k6_k1_middle")
            k1_line = st.text_area("3. Jaké hlavní úkoly bude muset řešit liniový management v běžném dni?:", placeholder="např. Kontrola kvality příspěvků na sítě, balení zásilek, obsluha zákazníků", key="k6_k1_line")
            
            if st.form_submit_button("Uložit Krok 1 do Projektového pasu 💾"):
                krok1_data = f"Top: {k1_top} | Middle: {k1_middle} | Liniový: {k1_line}"
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"]("Kapitola 6", "Projektový pas - Krok 1 (Struktura)", krok1_data)
                st.success("Krok 1 uložen! Tvá týmová struktura je připravena pro další plánování.")

        # PODKAPITOLA 1.2
        st.divider()
        st.markdown("#### 1.2 Základní manažerské funkce: Proces řízení")
        st.write("Manažerská práce není nahodilé hašení požárů. Je to neustále se opakující cyklus čtyř navazujících kroků: **Plánování ➔ Organizování ➔ Vedení lidí ➔ Kontrola**.")

        col_fnc1, col_fce2, col_fce3, col_fce4 = st.columns(4)
        col_fnc1.info("🎯 **1. Plánování**\nStanovení cílů a cest, jak jich dosáhnout.\n*(Kam jdeme?)*")
        col_fce2.warning("🏗️ **2. Organizování**\nRozdělení práce, úkolů, pravomocí a zdrojů.\n*(Kdo co udělá?)*")
        col_fce3.success("💬 **3. Vedení lidí**\nMotivace, komunikace, týmová atmosféra.\n*(Jak je nadchnout?)*")
        col_fce4.error("🔍 **4. Kontrola**\nMěření výsledků a nápravná opatření.\n*(Splnili jsme to?)*")

        # 1.2.1
        st.markdown("##### 1.2.1 Plánování a SMART cíl")
        st.write("Plánování dává týmu smysl a směr. Podle časového horizontu rozlišujeme operativní, taktické a strategické plánování.")

        st.markdown("<div class='box-purple'>🎯 <b>Trenažér: Vylaď cíl podle pravidla S.M.A.R.T.</b></div>", unsafe_allow_html=True)
        st.write("Vágně zadaný cíl (*'Chceme prodávat hodně mikin'*) vedoucího i tým zmate. Správný cíl musí být **S.M.A.R.T.** (Specific, Measurable, Achievable, Realistic, Time-bound).")

        with st.container(border=True):
            st.write("**Předělej špatný cíl na SMART cíl:**")
            st.caption("🔴 *Špatný cíl:* 'Chceme mít úspěšný školní merch.'")
            
            c_smart1, c_smart2, c_smart3 = st.columns(3)
            s_ks = c_smart1.number_input("Kolik kusů chceme prodat?:", min_value=10, value=80, step=10, key="k6_1_2_ks")
            s_marze = c_smart2.number_input("Minimální zisk/marže na kus (Kč):", min_value=50, value=120, step=10, key="k6_1_2_marze")
            s_termin = c_smart3.date_input("Termín dokončení akce:", key="k6_1_2_termin")

            smart_text = f"Do {s_termin.strftime('%d. %m. %Y')} prodáme přesně {s_ks} kusů školních mikin studentům s minimální marží {s_marze} Kč na kus."
            st.success(f"🟢 **Tvůj vygenerovaný SMART cíl:** *„{smart_text}“*")

        # 1.2.2 ORGANIZOVÁNÍ
        st.markdown("##### 1.2.2 Organizování a Pravomoc vs. Odpovědnost")
        st.write("Organizování znamená vytvořit jasnou strukturu: určovat pravomoci a odpovědnost.")

        st.markdown("""
        <div class='box-yellow'>
            ⚖️ <b>Základní rovnováha managementu:</b><br>
            • <b>Pravomoc:</b> Právo rozhodovat, utrácet peníze a zadávat úkoly.<br>
            • <b>Odpovědnost:</b> Povinnost nést následky a ručit za výsledek.<br>
            <i>Největší past neefektivního manažera? Dát podřízenému 100% odpovědnost za akci, ale nedát mu žádnou pravomoc o ní rozhodnout!</i>
        </div>
        """, unsafe_allow_html=True)

        # 1.2.3 VEDENÍ LIDÍ
        st.markdown("##### 1.2.3 Vedení lidí a Maslowova pyramida potřeb")
        st.write("Rozlišujeme **motivaci** (vnitřní touha) a **stimulaci** (vnější odměny).")

        st.markdown("#### 🔺 1.2.3.1 Maslowova pyramida potřeb v praxi")
        st.write("Psycholog Abraham Maslow ukázal, že lidé mají potřeby uspořádané do hierarchie.")

        úrovně_maslow = ["5. Seberealizace", "4. Uznání a respekt", "3. Sociální potřeby (Tým)", "2. Bezpečí a jistota", "1. Fyziologické potřeby"]
        sirky_maslow = [20, 40, 60, 80, 100]

        fig_maslow = go.Figure(go.Funnel(
            y=úrovně_maslow, x=sirky_maslow, textinfo="label",
            marker={"color": ["#8b5cf6", "#3b82f6", "#10b981", "#f59e0b", "#ef4444"]}
        ))
        fig_maslow.update_layout(title="Maslowova pyramida potřeb", height=350, margin=dict(t=40, b=10, l=10, r=10), showlegend=False)
        st.plotly_chart(fig_maslow, use_container_width=True)

        wybrana_uroven = st.selectbox("🔍 Vyber úroveň pyramidy a podívej se, jak ji řeší dobrý manažer:", [
            "1. Fyziologické potřeby (Základ)", "2. Potřeba bezpečí (Jistota)",
            "3. Sociální potřeby (Vztahy v týmu)", "4. Uznání a respekt (Ocenění)",
            "5. Seberealizace (Růst a smysl)"
        ], key="k6_1_2_maslow_select")

        if "1." in wybrana_uroven:
            st.error("🍎 **1. Fyziologické potřeby:** Důstojný plat, pitný režim, přestávka na oběd a bezpečné prostředí.")
        elif "2." in wybrana_uroven:
            st.warning("🛡️ **2. Potřeba bezpečí:** Stabilní smlouva, bezpečné pracoviště bez šikany, jasná pravidla.")
        elif "3." in wybrana_uroven:
            st.success("🤝 **3. Sociální potřeby:** Přijetí do týmu, dobrá atmosféra, neformální teambuildingy.")
        elif "4." in wybrana_uroven:
            st.info("🏆 **4. Uznání a respekt:** Pochvala před týmem za dobře odvedenou práci, povýšení, ocenění.")
        else:
            st.markdown("<div class='box-purple'>🚀 <b>5. Seberealizace:</b> Svoboda v tvoření, smysluplná práce, možnost učit se nové věci.</div>", unsafe_allow_html=True)

        # WORKBOOK KROK 2
        st.markdown("<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 2: SMART cíl a motivace týmu</b></div>", unsafe_allow_html=True)
        with st.form("form_projekt_krok2"):
            k2_smart = st.text_area("1. Napiš přesný S.M.A.R.T. cíl pro svůj projekt (Co, kolik, do kdy):", value=smart_text, key="k6_k2_smart")
            k2_motivace = st.text_area("2. Jak budeš svůj tým motivovat (kromě peněz) na úrovni Uznání a Seberealizace?:", placeholder="např. Každý člen bude mít v titulcích své jméno, bude mít volnost ve výběru hostů...", key="k6_k2_motivace")
            
            if st.form_submit_button("Uložit Krok 2 do Projektového pasu 💾"):
                krok2_data = f"SMART cíl: {k2_smart} | Motivace: {k2_motivace}"
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"]("Kapitola 6", "Projektový pas - Krok 2 (Cíl a motivace)", krok2_data)
                st.success("Krok 2 uložen! Tvůj cíl je ostrý jako břitva.")

        # 1.2.4 KONTROLA
        st.divider()
        st.markdown("#### 1.2.4 Kontrola: Není to slídění, ale navigace")
        st.write("Smyslem kontroly je ověřit, zda se reálný stav shoduje s plánem, a včas korigovat směr.")

        col_kont1, col_kont2 = st.columns([1, 1])
        with col_kont1:
            st.markdown("""
            <div style="background-color: #f8fafc; padding: 15px; border-left: 5px solid #3b82f6; border-radius: 4px;">
                <h5 style="margin-top:0; color: #1e40af;">🔍 4 fáze kontrolního procesu</h5>
                1. <b>Stanovení standardů</b><br>
                2. <b>Zjištění skutečnosti</b><br>
                3. <b>Srovnání plánu a reality</b><br>
                4. <b>Nápravné opatření</b>
            </div>
            """, unsafe_allow_html=True)

        with col_kont2:
            st.markdown("##### ⏱️ Typy kontroly podle času")
            tab_k1, tab_k2, tab_k3 = st.tabs(["🔮 Předběžná", "⚙️ Průběžná", "🏁 Následná"])
            with tab_k1: st.info("**Předběžná (PŘED):** Kontrola rozpočtu, schválení vzorků před tiskem.")
            with tab_k2: st.warning("**Průběžná (BĚHEM):** Sledování denních prodejů v e-shopu, Trello nástěnka.")
            with tab_k3: st.success("**Následná (PO):** Vyhodnocení zisku a zpětná vazba po akci.")

        # PODKAPITOLA 1.3
        st.divider()
        st.markdown("#### 1.3 Osobnost manažera, dovednosti a role")
        st.write("Manažerské dovednosti: Koncepční, Lidské a Technické.")

        fig_skills = go.Figure()
        fig_skills.add_trace(go.Bar(y=['Top', 'Middle', 'First-line'], x=[50, 25, 10], name='Koncepční', orientation='h', marker_color='#8b5cf6'))
        fig_skills.add_trace(go.Bar(y=['Top', 'Middle', 'First-line'], x=[40, 50, 40], name='Lidské', orientation='h', marker_color='#3b82f6'))
        fig_skills.add_trace(go.Bar(y=['Top', 'Middle', 'First-line'], x=[10, 25, 50], name='Technické', orientation='h', marker_color='#10b981'))
        fig_skills.update_layout(barmode='stack', title="Poměr manažerských dovedností (%)", height=250, margin=dict(t=30, b=20, l=10, r=10))
        st.plotly_chart(fig_skills, use_container_width=True)

        # 1.3.1 MINTZBERGOVY ROLE
        st.markdown("##### 1.3.1 Role manažera podle Mintzberga")
        situace_mintz = st.selectbox("Vyber situaci ze dne manažera:", [
            "1. Vybíráš, kterým 3 projektům z deseti přidělíš peníze z rozpočtu.",
            "2. Novinář se ptá na oficiální stanovisko vaší firmy.",
            "3. Vypadly servery a musíte okamžitě sehnat náhradní řešení.",
            "4. Jdeš na kávu se zakladatelem partnerké firmy zjistit novinky z trhu."
        ], key="k6_1_3_mintz_select")

        if "1." in situace_mintz: st.info("🎯 **Alokátor zdrojů** (rozhodovací role).")
        elif "2." in situace_mintz: st.info("📢 **Mluvčí** (informační role).")
        elif "3." in situace_mintz: st.error("🚨 **Hasič krizí** (rozhodovací role).")
        else: st.success("🔎 **Monitor & Spojovatel** (informační/interpersonální role).")

        # PODKAPITOLA 1.4
        st.divider()
        st.markdown("#### 1.4 Styly řízení: Jak pracovat s mocí a týmem")
        st.write("Autoritativní, Demokratický a Liberální (Laissez-faire) styl.")

        with st.form("debata_musk_form"):
            st.write("**Která filozofie řízení je ti bližší a proč?**")
            postoj_styl = st.radio("Vyber svůj postoj:", [
                "🚀 Dávám přednost autoritativnímu vizionáři (Musk): Bez tvrdé ruky a vysokých nároků nevzniknou revoluční věci.",
                "🎧 Dávám přednost demokratické/svobodné kultuře (Spotify/Google): Nejlepší inovace vznikají v prostředí svobody a bezpečí.",
                "⚖️ Záleží na situaci (Situační řízení): V krizích autoritativní, při vývoji demokratický."
            ], key="k6_1_4_postoj")
            if st.form_submit_button("Odeslat a uložit názor 💾"):
                st.success("Tůj postoj byl zaznamenán!")
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"]("Kapitola 6", "Podkapitola 1.4 - Debata Styl řízení", postoj_styl[:30])

        # WORKBOOK KROK 3
        st.markdown("<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 3: Styl řízení a kontrolní mechanizmus</b></div>", unsafe_allow_html=True)
        with st.form("form_projekt_krok3"):
            k3_styl = st.text_area("1. Jaký styl řízení zvolíš pro svůj projekt a proč?:", placeholder="např. Běžně demokraticky, ale těsně před akcí autoritativně.", key="k6_k3_styl")
            k3_kontrola = st.text_area("2. Jak nastavíš PŘEDBĚŽNOU kontrolu pro svůj projekt?:", placeholder="např. Zkontroluji funkčnost e-shopu týden před spuštěním.", key="k6_k3_kontrola")
            
            if st.form_submit_button("Uložit Krok 3 do Projektového pasu 💾"):
                krok3_data = f"Styl: {k3_styl} | Kontrola: {k3_kontrola}"
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"]("Kapitola 6", "Projektový pas - Krok 3 (Styl a kontrola)", krok3_data)
                st.success("Krok 3 úspěšně uložen!")

        # PODKAPITOLA 1.5
        st.divider()
        st.markdown("#### 1.5 Organizační struktury firem: Mapa tvé organizace")
        st.write("Formální vs. neformální struktura a typy organizačních struktur (Liniová, Štábní, Funkcionální, Maticová).")

        pocet_podrizenych = st.slider("Počet lidí, které přímo řídíš (Rozpětí řízení):", min_value=2, max_value=25, value=5, step=1, key="k6_1_5_rozpeti")
        if pocet_podrizenych <= 6: st.info(f"📏 Úzké rozpětí řízení ({pocet_podrizenych} lidí). Vysoká kontrola, vyšší náklady.")
        elif 7 <= pocet_podrizenych <= 12: st.success(f"⚖️ Vyvážené rozpětí řízení ({pocet_podrizenych} lidí). Ideální rovnováha.")
        else: st.warning(f"📐 Široké rozpětí řízení ({pocet_podrizenych} lidí). Plochá struktura, riziko chaosu.")

        # WORKBOOK KROK 4
        st.markdown("<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 4: Organizační mapa tvého projektu</b></div>", unsafe_allow_html=True)
        with st.form("form_projekt_krok4"):
            k4_typ = st.selectbox("1. Jaký typ organizační struktury se nejlépe hodí pro tvůj projekt?:", [
                "Liniová (Jednoduchá pyramida s jedním šéfem)",
                "Funkcionální (Rozděleno podle oborů: Marketing, Výroba, IT...)",
                "Maticová (Projektový tým se skládá ze specialistů z různých oborů)",
                "Plochá / Široká (Všichni komunikujeme přímo s zakladatelem)"
            ], key="k6_k4_typ")
            k4_detail = st.text_area("2. Jaké zvolíš rozpětí řízení pro hlavního manažera?:", placeholder="např. Hlavní manažer pořídí 4 vedoucí sekcí...", key="k6_k4_detail")
            
            if st.form_submit_button("Uložit Krok 4 do Projektového pasu 💾"):
                krok4_data = f"Typ struktury: {k4_typ} | Detail: {k4_detail}"
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"]("Kapitola 6", "Projektový pas - Krok 4 (Organizační mapa)", krok4_data)
                st.success("Krok 4 úspěšně uložen!")

        # PODKAPITOLA 1.6
        st.divider()
        st.markdown("#### 1.6 Rozhodování a analytické metody")
        st.write("1.6.1 SWOT analýza (Strengths, Weaknesses, Opportunities, Threats) a 1.6.2 Řízení rizik.")

        # WORKBOOK KROK 5
        st.markdown("<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 5: SWOT analýza a Plán B tvého projektu</b></div>", unsafe_allow_html=True)
        with st.form("form_projekt_krok5"):
            col_sw1, col_sw2 = st.columns(2)
            p_s = col_sw1.text_input("Silné stránky (S - Vnitřní):", placeholder="např. Skvělý grafický design", key="k6_k5_s")
            p_w = col_sw1.text_input("Slabé stránky (W - Vnitřní):", placeholder="např. Nulový rozpočet", key="k6_k5_w")
            p_o = col_sw2.text_input("Příležitosti (O - Vnější):", placeholder="např. Rostoucí zájem studentů", key="k6_k5_o")
            p_t = col_sw2.text_input("Hrozby (T - Vnější):", placeholder="např. Konkurence na škole", key="k6_k5_t")
            p_plan_b = st.text_area("Pojmenuj 1 největší riziko a navrhni konkrétní Plán B:", placeholder="např. Riziko: Moderátor onemocní. Plán B: Máme náhradníka.", key="k6_k5_planb")

            if st.form_submit_button("Uložit Krok 5 do Projektového pasu 💾"):
                krok5_data = f"S:{p_s} | W:{p_w} | O:{p_o} | T:{p_t} | Plán B:{p_plan_b}"
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"]("Kapitola 6", "Projektový pas - Krok 5 (SWOT & Plán B)", krok5_data)
                st.success("Krok 5 úspěšně uložen! Blok 1 (Management) je hotov.")

        # PODKAPITOLA 1.7
        st.divider()
        st.markdown("#### 1.7 Moderní přesah: Agilní řízení, remote work a burnout")
        st.write("Scrum, Kanban, OKR, koučování a prevence vyhoření.")

    # =========================================================================
    # SEKCE 2: MARKETING – HRA O POZORNOST A MARKETINGOVÝ MIX
    # =========================================================================
    elif selected_section_6 == section_options_6[1]:
        st.markdown("### 2. Marketing – Hra o pozornost a marketingový mix")
        
        st.markdown("""
        <div class='box-blue'>
            🎯 <b>Moderní hook:</b> Marketing není jen reklama. Je to způsob, jak pochopit, po čem lidé touží, jak vytvořit hodnotu a dostat správnou nabídku ke správnému člověku.
        </div>
        """, unsafe_allow_html=True)

        st.divider()

        # PODKAPITOLA 2.1
        st.markdown("#### 2.1 Podstata a význam marketingu")
        st.write("Potřeba (pocit nedostatku) vs. Přání (konkrétní forma) vs. Poptávka (přání kryté penězi).")

        # WORKBOOK KROK 6
        st.markdown("<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 6: Podstata a koncepce tvého projektu</b></div>", unsafe_allow_html=True)
        with st.form("form_projekt_krok6"):
            k6_potreba = st.text_area("1. Jakou ZÁKLADNÍ POTŘEBU uspokojuje tvůj projekt?:", placeholder="např. Potřeba zábavy a informovanosti.", key="k6_k6_potreba")
            k6_koncepce = st.selectbox("2. Jaká podnikatelská koncepce by k tvému projektu nejlépe seděla?:", [
                "Marketingová (Striktně sledujeme, co zákazník chce)",
                "Výrobková (Sázíme na špičkovou kvalitu)",
                "Sociální/Etická (Sázíme na udržitelný přístup)",
                "Prodejní (Tlačíme přes slevy a reklamu)"
            ], key="k6_k6_koncepce")
            
            if st.form_submit_button("Uložit Krok 6 do Projektového pasu 💾"):
                krok6_data = f"Potřeba: {k6_potreba} | Koncepce: {k6_koncepce}"
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"]("Kapitola 6", "Projektový pas - Krok 6 (Koncepce)", krok6_data)
                st.success("Krok 6 uložen!")

        # PODKAPITOLA 2.2
        st.divider()
        st.markdown("#### 2.2 Marketingový výzkum a analýza trhu")
        st.write("Primární (nová) vs. Sekundární (existující) data. Kvantitativní vs. Kvalitativní výzkum. A/B testování.")

        # WORKBOOK KROK 7
        st.markdown("<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 7: Tvůj marketingový výzkum</b></div>", unsafe_allow_html=True)
        with st.form("form_projekt_krok7"):
            k7_sekundarni = st.text_area("1. Kde získáš SEKUNDÁRNÍ DATA o tvém trhu ještě před startem projektu?:", placeholder="např. Analýza příspěvků konkurenčních školních profilů...", key="k6_k7_sekundarni")
            k7_primarni = st.text_area("2. Jakou metodu použiješ pro sběr PRIMÁRNÍCH DAT od tvé cílovky?:", placeholder="např. Google Forms dotazník mezi studenty...", key="k6_k7_primarni")
            
            if st.form_submit_button("Uložit Krok 7 do Projektového pasu 💾"):
                krok7_data = f"Sekundární data: {k7_sekundarni} | Primární data: {k7_primarni}"
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"]("Kapitola 6", "Projektový pas - Krok 7 (Výzkum)", krok7_data)
                st.success("Krok 7 uložen!")

        # PODKAPITOLA 2.3
        st.divider()
        st.markdown("#### 2.3 STP proces: Segmentace, Cílení (Targeting) a Positioning")
        st.write("S - Segmentace (Geografická, Demografická, Psychografická, Behaviorální), T - Cílení, P - Positioning & USP.")

        # WORKBOOK KROK 8
        st.markdown("<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 8: STP analýza tvého projektu</b></div>", unsafe_allow_html=True)
        with st.form("form_projekt_krok8"):
            col_stp_f1, col_stp_f2 = st.columns(2)
            k8_demo = col_stp_f1.text_input("Demografické údaje (Věk, role...):", placeholder="např. Studenti SŠ 15-19 let", key="k6_k8_demo")
            k8_psycho = col_stp_f1.text_input("Psychografické údaje (Zájmy...):", placeholder="např. Zajímají se o módu", key="k6_k8_psycho")
            k8_typ = col_stp_f2.selectbox("Typ cílení:", ["Koncentrovaný", "Níša / Nika", "Masový"], key="k6_k8_typ")
            k8_usp = st.text_area("Unikátní prodejní argument (USP - 1 věta):", placeholder="např. Náš merch je oversized udržitelná móda od studenta pro studenty.", key="k6_k8_usp")

            if st.form_submit_button("Uložit Krok 8 do Projektového pasu 💾"):
                krok8_data = f"Demo: {k8_demo} | Psycho: {k8_psycho} | Cílení: {k8_typ} | USP: {k8_usp}"
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"]("Kapitola 6", "Projektový pas - Krok 8 (STP & USP)", krok8_data)
                st.success("Krok 8 uložen!")

        # PODKAPITOLA 2.4
        st.divider()
        st.markdown("#### 2.4 Marketingový mix: Klasické 4P")
        st.write("Product, Price, Place, Promotion.")

        # WORKBOOK KROK 9
        st.markdown("<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 9: Nastavení Produktu, Ceny a Distribuce</b></div>", unsafe_allow_html=True)
        with st.form("form_projekt_krok9"):
            k9_rozsireny = st.text_area("1. PRODUKT – Co bude tvořit ROZŠÍŘENÝ PRODUKT tvého projektu?:", placeholder="např. Dárkové balení, samolepky zdarma, výměna velkostí do 30 dní...", key="k6_k9_rozsireny")
            col_p_f1, col_p_f2 = st.columns(2)
            k9_metoda = col_p_f1.selectbox("2. CENA – Cenová metoda:", ["Poptávková", "Konkurenční", "Nákladová"], key="k6_k9_metoda")
            k9_distribuce = col_p_f2.selectbox("3. DISTRIBUCE – Cesta k zákazníkovi:", ["Přímá (Vlastní e-shop)", "Nepřímá (Partneři/stánky)", "Omni-channel"], key="k6_k9_distribuce")

            if st.form_submit_button("Uložit Krok 9 do Projektového pasu 💾"):
                krok9_data = f"Rozšířený produkt: {k9_rozsireny} | Metoda ceny: {k9_metoda} | Distribuce: {k9_distribuce}"
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"]("Kapitola 6", "Projektový pas - Krok 9 (3P)", krok9_data)
                st.success("Krok 9 uložen!")

        # WORKBOOK KROK 10
        st.markdown("<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 10: Komunikační mix a finální rekapitulace 4P</b></div>", unsafe_allow_html=True)
        with st.form("form_projekt_krok10"):
            k10_kanaly = st.text_area("1. Jaké 2 hlavní nástroje propagace použiješ?:", placeholder="např. Instagram Ads + Slevový kód pro první nákup", key="k6_k10_kanaly")
            k10_ugc = st.text_input("2. Využiješ Influencer marketing nebo UGC?:", placeholder="např. Barter s 5 micro-influencery ze školy", key="k6_k10_ugc")

            if st.form_submit_button("Uložit Krok 10 a dokončit Blok 2 (Marketing) 💾"):
                krok10_data = f"Propagace: {k10_kanaly} | Influencer/UGC: {k10_ugc}"
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"]("Kapitola 6", "Projektový pas - Krok 10 (Promotion & 4P)", krok10_data)
                st.success("🎉 Blok 2 (Marketing) je kompletně uplatněn a uložen!")

    # =========================================================================
    # SEKCE 3: BRAND, NÁKUPNÍ PSYCHOLOGIE A ETIKA
    # =========================================================================
    elif selected_section_6 == section_options_6[2]:
        st.markdown("### 3. Brand, nákupní psychologie a etika")
        st.write("Pochopení budování značky, emocí, nákupního rozhodování, neuromarketingu, Dark patterns i právního rámce reklamy.")

        # WORKBOOK KROK 11
        st.markdown("<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 11: Identita a Příběh tvé značky</b></div>", unsafe_allow_html=True)
        with st.form("form_projekt_krok11"):
            k11_story = st.text_area("1. STORYTELLING – Příběh značky:", placeholder="např. Náš projekt vznikl v rohu knihovny, když jsme hledali poctivou kávu...", key="k6_k11_story")
            col_b_f1, col_b_f2 = st.columns(2)
            k11_mise = col_b_f1.text_input("2. MISE ZNAČKY:", placeholder="např. Přinášet energii bez cukrového dojezdu.", key="k6_k11_mise")
            k11_hodnoty = col_b_f1.text_input("3. HODNOTY ZNAČKY:", placeholder="např. Autenticita, Čerstvost", key="k6_k11_hodnoty")
            k11_vizual = col_b_f2.text_input("4. VIZUÁL & STYL:", placeholder="např. Neony, černá a limetková", key="k6_k11_vizual")
            k11_loyalty = col_b_f2.selectbox("5. BRAND LOYALTY:", ["Odměny za věrnost", "Exkluzivní komunita", "UGC"], key="k6_k11_loyalty")

            if st.form_submit_button("Uložit Krok 11 do Projektového pasu 💾"):
                krok11_data = f"Příběh: {k11_story} | Mise: {k11_mise} | Hodnoty: {k11_hodnoty} | Vizuál: {k11_vizual} | Loyalty: {k11_loyalty}"
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"]("Kapitola 6", "Projektový pas - Krok 11 (Brand)", krok11_data)
                st.success("Krok 11 uložen!")

        # WORKBOOK KROK 12
        st.markdown("<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 12: Psychologie a Nákupní cesta tvého zákazníka</b></div>", unsafe_allow_html=True)
        with st.form("form_projekt_krok12"):
            k12_spoustec = st.text_area("1. ROZPOZNÁNÍ POTŘEBY – Jaký problém přiměje zákazníka hledat tvůj produkt?:", placeholder="např. Nemá co nosit na školní akce...", key="k6_k12_spoustec")
            col_b_p1, col_b_p2 = st.columns(2)
            k12_ref = col_b_p1.text_input("2. REFERENČNÍ SKUPINA:", placeholder="např. Spolužáci, tiktokeři", key="k6_k12_ref")
            k12_disonance = col_b_p2.text_input("3. PÉČE PO NÁKUPU:", placeholder="např. Děkovný e-mail a samolepka zdarma", key="k6_k12_disonance")

            if st.form_submit_button("Uložit Krok 12 do Projektového pasu 💾"):
                krok12_data = f"Spouštěč: {k12_spoustec} | Referenční sk.: {k12_ref} | Péče po nákupu: {k12_disonance}"
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"]("Kapitola 6", "Projektový pas - Krok 12 (Psychologie)", krok12_data)
                st.success("Krok 12 uložen!")

        # WORKBOOK KROK 13
        st.markdown("<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 13: Neuromarketing a Etický kodex projektu</b></div>", unsafe_allow_html=True)
        with st.form("form_projekt_krok13"):
            k13_neuro = st.text_area("1. NEUROMARKETING – Jaké podněty použiješ?:", placeholder="např. Kontrastní tlačítko Koupit + znělka v videu", key="k6_k13_neuro")
            k13_etika = st.text_area("2. ETIKA – Jak se vyhneš klamavé reklamě?:", placeholder="např. Jasné označování #spoluprace", key="k6_k13_etika")

            if st.form_submit_button("Uložit Krok 13 do Projektového pasu 💾"):
                krok13_data = f"Neuromarketing: {k13_neuro} | Etika: {k13_etika}"
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"]("Kapitola 6", "Projektový pas - Krok 13 (Neuromarketing & Etika)", krok13_data)
                st.success("Krok 13 uložen!")

        # WORKBOOK KROK 14
        st.markdown("<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 14: Garance ochrany spotřebitele u tvého projektu</b></div>", unsafe_allow_html=True)
        with st.form("form_projekt_krok14"):
            k14_dark = st.text_area("1. OCHRANA SPOTŘEBITELE – Jak se vyhneš 'Dark patterns'?:", placeholder="např. Žádné skryté poplatky v košíku", key="k6_k14_dark")
            k14_reklamace = st.text_area("2. REKLAMACE A VRÁCENÍ – Jaké nastavíš podmínky?:", placeholder="např. Vrácení zdarma do 14 dnů", key="k6_k14_reklamace")

            if st.form_submit_button("Uložit Krok 14 do Projektového pasu 💾"):
                krok14_data = f"Ochrana: {k14_dark} | Reklamace: {k14_reklamace}"
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"]("Kapitola 6", "Projektový pas - Krok 14 (Ochrana spotřebitele)", krok14_data)
                st.success("Krok 14 uložen!")

        # WORKBOOK KROK 15
        st.markdown("<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 15: Digitální a sociální strategie projektu</b></div>", unsafe_allow_html=True)
        with st.form("form_projekt_krok15"):
            col_d_f1, col_d_f2 = st.columns(2)
            k15_sit = col_d_f1.selectbox("1. Primární síť:", ["TikTok", "Instagram", "YouTube", "LinkedIn", "Facebook"], key="k6_k15_sit")
            k15_obsah = col_d_f1.text_input("2. Typ obsahu:", placeholder="např. Zákulisní krátká videa", key="k6_k15_obsah")
            k15_inf = col_d_f2.selectbox("3. Typ influencerů:", ["Mikro-masoví", "Niche odborníci", "Jen UGC"], key="k6_k15_inf")
            k15_guerilla = col_d_f2.text_input("4. Nápad na Virál/Guerillu:", placeholder="např. Samolepky na zrcadla v jídelně", key="k6_k15_guerilla")

            if st.form_submit_button("Uložit Krok 15 do Projektového pasu 💾"):
                krok15_data = f"Síť: {k15_sit} | Obsah: {k15_obsah} | Influencer: {k15_inf} | Guerilla: {k15_guerilla}"
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"]("Kapitola 6", "Projektový pas - Krok 15 (Digitální kampaň)", krok15_data)
                st.success("Krok 15 uložen!")

        # WORKBOOK KROK 16
        st.markdown("<br><div class='box-yellow'>📝 <b>Projektový pas – Krok 16: Návrh Etické kampaně a dokončení Bloku 3</b></div>", unsafe_allow_html=True)
        with st.form("form_projekt_krok16_etika"):
            k16_sdeleni = st.text_input("1. Hlavní sdělení kampaně:", placeholder="např. Obleč se do školy udržitelně", key="k6_k16_sdeleni")
            col_k1, col_k2 = st.columns(2)
            k16_kanaly = col_k1.text_input("2. Kde bude kampaň probíhat?:", placeholder="např. Instagram Reels + Plakáty", key="k6_k16_kanaly")
            k16_kpi = col_k1.text_input("3. Jak poznáš úspěch (KPI)?:", placeholder="např. 100 objednávek", key="k6_k16_kpi")
            k16_greenw = col_k2.text_area("4. Jak se vyhneš greenwashingu?:", placeholder="např. Přesné certifikace materiálu", key="k6_k16_greenw")
            k16_oznaceni = col_k2.text_input("5. Označení spolupráce:", placeholder="např. #spoluprace", key="k6_k16_oznaceni")

            if st.form_submit_button("Uložit Krok 16 a dokončit celý Blok 3 💾"):
                krok16_data = f"Sdělení: {k16_sdeleni} | Kanály: {k16_kanaly} | KPI: {k16_kpi} | Bez greenwashingu: {k16_greenw} | Označení: {k16_oznaceni}"
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"]("Kapitola 6", "Projektový pas - Krok 16 (Etická kampaň)", krok16_data)
                st.success("🎉 Blok 3 je kompletně hotový a uložený!")

    # =========================================================================
    # SEKCE 4: ZÁVĚREČNÝ VÝSTUP KAPITOLY A PŘÍPADOVÉ STUDIE
    # =========================================================================
    elif selected_section_6 == section_options_6[3]:
        st.markdown("### 4. Závěrečný výstup kapitoly a případové studie")

        st.markdown("""
        <div class='box-blue'>
            🚀 <b>Finální výstup kapitoly: Od nápadu k reálné kampani</b><br>
            V předchozích blocích jsi krok za krokem budoval/a svůj vlastním projekt. Nyní je čas dát všechny dílky skládačky dohromady do jednoho uceleného Projektového pasu a prověřit své znalosti na reálné případové studii z praxe!
        </div>
        """, unsafe_allow_html=True)

        st.divider()

        # 4.1 PROJEKTOVÝ PAS
        st.markdown("#### 4.1 Finální projektový výstup")
        st.write("Sestavení kompletního přehledu tvého projektu:")

        st.markdown("""
        | Kritérium | Co se hodnotí |
        | :--- | :--- |
        | **🏛️ Management** | Jasný SMART cíl, rozdělení rolí v týmu, realistický plán a práce s riziky (Plán B). |
        | **🎯 Marketing** | Smysluplně zvolená cílová skupina (STP), originální positioning a propojený marketingový mix 4P. |
        | **💎 Brand** | Srozumitelný příběh značky, definované hodnoty, vizuální identita a důvěryhodná komunikace. |
        | **⚖️ Etika & Právo** | Schopnost rozpoznat manipulaci, klamavou reklamu, greenwashing a dodržení právních pravidel. |
        | **🎤 Prezentace** | Srozumitelné vysvětlení nápadu, konkrétní příklady a schopnost obhájit svá manažerská rozhodnutí. |
        """)

        st.markdown("<br><div class='box-yellow'>📝 <b>Generátor finálního Projektového pasu</b></div>", unsafe_allow_html=True)

        with st.expander("📄 Zobrazit kompletní Projektový pas k exportu", expanded=False):
            st.markdown(f"### 🚀 Projektový pas: **{nazev_projektu}**")
            st.markdown("---")
            st.markdown("##### 🏛️ BLOK 1: MANAGEMENT & ORGANIZACE")
            st.markdown("* **Top Management & Vize:** Řízení strategie a směřování projektu.")
            st.markdown("* **Organizační struktura:** Rozdělení funkcí (Výroba, Marketing, Finance).")
            st.markdown("* **SMART Cíl:** Konkrétní, měřitelný a časově ohraničený výsledek.")
            st.markdown("* **SWOT & Plán B:** Identifikovaná rizika a záložní řešení.")

            st.markdown("---")
            st.markdown("##### 🎯 BLOK 2: MARKETING & STP")
            st.markdown("* **Cílová skupina (Targeting):** Přesně definovaný segment zákazníků.")
            st.markdown("* **Positioning & USP:** Unikátní prodejní argument, který nás odlišuje od konkurence.")
            st.markdown("* **Marketingový mix 4P:** Product, Price, Place, Promotion.")

            st.markdown("---")
            st.markdown("##### 💎 BLOK 3: BRAND & ETIKA")
            st.markdown("* **Příběh značky (Storytelling):** Proč projekt vznikl a jakým hodnotám věří.")
            st.markdown("* **Neuromarketingové prvky:** Zapojení smyslových a psychologických podnětů.")
            st.markdown("* **Etický kodex:** Záruka pravdivosti, označování spoluprací a ochrana spotřebitele.")

        st.divider()

        # 4.2 PŘÍPADOVÉ STUDIE
        st.markdown("#### 4.2 Případové studie na závěr kapitoly")
        st.write("Vyzkoušej si roli konzultanta na reálných chybách z praxe:")

        # PŘÍPADOVÁ STUDIE 1
        st.markdown("##### 👕 Případová studie 1: Školní merch, který nikdo nekupuje")
        with st.container(border=True):
            st.markdown("Studenti objednali 100 mikin na sklad za 850 Kč bez výzkumu. Prodalo se jen 18 ks.")
            with st.form("form_case_study_1"):
                cs1_q1 = st.text_area("1. Jaký MARKETINGOVÝ VÝZKUM měl tým udělat předem?:", key="cs1_q1")
                cs1_q2 = st.text_area("2. Jak bys upravil/a MARKETINGOVÝ MIX 4P?:", key="cs1_q2")
                cs1_q3 = st.text_area("3. Jak eliminovat RIZIKO neprodaných zásob?:", key="cs1_q3")

                if st.form_submit_button("Odeslat a uložit řešení Případové studie 1 💾"):
                    st.success("✅ **Výborná analýza!** Řešením byly předobjednávky (Print-on-Demand) a průzkum mezi studenty.")
                    cs1_data = f"Výzkum: {cs1_q1} | 4P úprava: {cs1_q2} | Riziko zásob: {cs1_q3}"
                    if "uloz_odpoved_fn" in st.session_state:
                        st.session_state["uloz_odpoved_fn"]("Kapitola 6", "Případová studie 1 - Školní merch", cs1_data)

        # PŘÍPADOVÁ STUDIE 2
        st.divider()
        st.markdown("##### ☕ Případová studie 2: Kavárna u školy a boj o pozornost")
        with st.container(border=True):
            st.markdown("Kavárna u školy má nízkou návštěvnost. Studenti chtějí studijní místo, Wi-Fi a levnější nápoje.")
            with st.form("form_case_study_2"):
                cs2_q1 = st.text_area("1. Vytvoř krátkou SWOT analýzu kavárny (S, W, O, T):", key="cs2_q1")
                cs2_q2 = st.text_area("2. Navrhni BRAND (Název, hodnoty, styl):", key="cs2_q2")
                cs2_q3 = st.text_area("3. Navrhni 1 ETICKOU kampaň na sítě:", key="cs2_q3")
                cs2_q4 = st.text_area("4. Jak využít UGC obsah zákazníků?:", key="cs2_q4")

                if st.form_submit_button("Odeslat a uložit řešení Případové studie 2 💾"):
                    st.success("✅ **Skvělá práce!** Propojil/a jsi potřeby studentů s brandingem a 4P.")
                    cs2_data = f"SWOT: {cs2_q1} | Brand: {cs2_q2} | Kampaň: {cs2_q3} | UGC: {cs2_q4}"
                    if "uloz_odpoved_fn" in st.session_state:
                        st.session_state["uloz_odpoved_fn"]("Kapitola 6", "Případová studie 2 - Kavárna", cs2_data)

        # PŘÍPADOVÁ STUDIE 3
        st.divider()
        st.markdown("##### 📱 Případová studie 3: Influencer propaguje „zázračný“ produkt")
        with st.container(border=True):
            st.markdown("Tiktoker propaguje doplňky stravy bez označení reklamy s falešnými odpočty času na e-shopu.")
            with st.form("form_case_study_3"):
                cs3_q1 = st.text_area("1. Pojmenuj 3 neetické/protiprávní prvky v kampani:", key="cs3_q1")
                cs3_q2 = st.text_input("2. Jak měla být spolupráce správně označena?:", key="cs3_q2")
                cs3_q3 = st.text_area("3. Navrhni FÉROVĚJŠÍ variantu kampaně:", key="cs3_q3")
                cs3_q4 = st.text_area("4. Jakou roli zde hraje Social Proof?:", key="cs3_q4")

                if st.form_submit_button("Odeslat a uložit řešení Případové studie 3 💾"):
                    st.success("✅ **Výborně!** Odhalil/a jsi skrytou reklamu i klamavé Dark patterns.")
                    cs3_data = f"Problémy: {cs3_q1} | Označení: {cs3_q2} | Férová verze: {cs3_q3} | Social proof: {cs3_q4}"
                    if "uloz_odpoved_fn" in st.session_state:
                        st.session_state["uloz_odpoved_fn"]("Kapitola 6", "Případová studie 3 - Influencer kampaň", cs3_data)

        # ZÁVĚREČNÁ REFLEXE KAPITOLY
        st.divider()
        st.markdown("##### 🎓 Závěrečná reflexe celou kapitolou")
        with st.form("form_zaverecna_reflexe"):
            ref_vyber = st.selectbox("Vyber si případovou studii k reflexi:", [
                "Případová studie 1: Školní merch",
                "Případová studie 2: Kavárna u školy",
                "Případová studie 3: Influencer a zázračný produkt"
            ], key="k6_ref_vyber")
            ref_odpoved = st.text_area("Co by měl v této situaci rozhodnout dobrý manažer, jak by měl marketér upravit komunikaci a kde leží hranice mezi přesvědčováním a manipulací?:", key="k6_ref_odpoved")

            if st.form_submit_button("Odeslat finální reflexi a UZAVŘÍT KAPITOLU 6 💾"):
                st.balloons()
                st.success("🎉 **GRATULUJEME! Kompletně jsi dokončil/a Kapitolu 6 (Management a Marketing).**")
                reflexe_data = f"Vybrána studie: {ref_vyber} | Reflexe: {ref_odpoved}"
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"]("Kapitola 6", "Závěrečná reflexe Kapitoly 6", reflexe_data)
