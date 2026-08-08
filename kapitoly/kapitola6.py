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
