import streamlit as st

def render():
    # 📌 HLAVIČKA KAPITOLY
    st.markdown("<span class='hero-badge'>Kapitola 5</span>", unsafe_allow_html=True)
    st.title("5. Stát, daně a globální souvislosti")
    st.markdown("<p style='font-size: 1rem; color: #64748b; margin-bottom: 1.5rem;'>Stát není jen úřad, formulář nebo položka na výplatní pásce. Je to systém, který vybírá daně, financuje veřejné služby, nastavuje pravidla trhu a reaguje na problémy, které jednotlivci ani firmy sami nevyřeší — od infrastruktury přes digitální stát až po regulaci Big Tech, globální obchod a klimatickou odpovědnost.</p>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown("""
        <div class='box-blue'>
            <strong>🧠 Pointa kapitoly:</strong> Ekonomika státu není abstraktní tabulka. Promítá se do toho, kolik zaplatíš z brigády, proč je v ceně mobilu DPH, jak stát financuje školy a silnice, proč řeší daňové úniky, jak funguje eGovernment a proč levné zboží z druhého konce světa může mít skryté ekologické i sociální náklady.
        </div>
        """, unsafe_allow_html=True)

    # 📌 PŘEHLED A NAVIGACE KAPITOLOU
    with st.expander("🧭 Cíle kapitoly a logická cesta (Rozbalit)", expanded=False):
        c_nav1, c_nav2 = st.columns(2)
        with c_nav1:
            st.markdown("""
            **🎯 Co máš po kapitole umět?**
            * **Vysvětlit** funkce státu v ekonomice a důvody státních zásahů.
            * **Rozlišit** veřejné statky, komerční služby a tržní selhání.
            * **Popsat** základní princip státního rozpočtu, deficitu a veřejného dluhu.
            * **Rozlišit** přímé a nepřímé daně na běžných příkladech.
            * **Vysvětlit**, proč se daně týkají brigád, podnikání, tvorby obsahu (YouTube, TikTok), investic i kryptoměn.
            * **Popsat** globalizaci, mezinárodní obchod a dodavatelské řetězce (vč. EU a jednotného trhu).
            * **Posoudit** dopady levného zboží (fast fashion, e-commerce) na lidi i životní prostředí.
            * **Porozumět** pojmům jako Green Deal, ESG a odpovědnost firem.
            """)
            st.markdown("""
            <div style="font-size: 0.85rem; color: #64748b; margin-top: 10px;">
                <i>📘 <b>Vazba na RVP:</b> Kapitola rozvíjí ekonomické, občanské a digitální kompetence v oblastech funkce státu v ekonomice, hospodářská politika, daňová soustava, státní rozpočet, veřejné finance, globalizace, EU a udržitelný rozvoj.</i>
            </div>
            """, unsafe_allow_html=True)

        with c_nav2:
            st.markdown("""
            **🧭 Logická cesta kapitolou:**
            1. 🏛️ **Stát jako hospodář:** Proč stát v ekonomice vůbec existuje, co jsou veřejné statky a tržní selhání.
            2. 📊 **Daně a státní rozpočet:** Odkud stát bere peníze, za co je utrácí, proč vzniká deficit a proč daně nejsou jen „trest za výdělek“.
            3. 💸 **Moje daně v praxi:** Propojení s reálným životem (brigády, Vinted, OnlyFans, Uber, kryptoměny, DPH).
            4. 🌍 **Globální souvislosti:** Cesta výrobků (fast fashion, čipy z Asie, Temu) a rizika závislosti na dodavatelských řetězcích.
            5. 🌱 **ESG a udržitelná ekonomika:** Uhlíková stopa, greenwashing a společenská odpovědnost firem.
            """)

    # 📌 JEDNOTNÁ NABÍDKA PODKAPITOL
    # Sdruženo do 6 hlavních bloků podle tvé osnovy z obrázků pro přehlednost UI
    section_options_5 = [
        "1. Stát jako „hospodář“ — proč ho vůbec máme?",
        "2. Daně, státní rozpočet a ekonomická realita",
        "3. Moje daně v praxi",
        "4. Globální souvislosti a svět bez hranic",
        "5. ESG a udržitelná ekonomika",
        "6. Aktivity a případové studie na závěr"
    ]
    
    selected_section_5 = st.selectbox("📌 Přechod na podkapitolu:", section_options_5, index=0)
    st.divider()

    # =========================================================================
    # SEKCE 1: STÁT JAKO HOSPODÁŘ
    # =========================================================================
    if selected_section_5 == "1. Stát jako „hospodář“ — proč ho vůbec máme?":
        st.markdown("### 1. Stát jako „hospodář“ — proč ho vůbec máme?")
        st.info("Zde bude obsah pro podkapitoly 1.1 až 1.6 (Tržní selhání, funkce státu, magický čtyřúhelník...)")
        # Sem vložíme kód v dalším kroku...

    # =========================================================================
    # SEKCE 2: DANĚ A STÁTNÍ ROZPOČET
    # =========================================================================
    elif selected_section_5 == "2. Daně, státní rozpočet a ekonomická realita":
        st.markdown("### 2. Daně, státní rozpočet a ekonomická realita")
        st.info("Zde bude obsah pro podkapitoly 2.1 až 2.12 (Zásady zdaňování, přímé/nepřímé daně, rozpočet, dluh...)")

    # =========================================================================
    # SEKCE 3: MOJE DANĚ V PRAXI
    # =========================================================================
    elif selected_section_5 == "3. Moje daně v praxi":
        st.markdown("### 3. Moje daně v praxi")
        st.info("Zde bude praktický průvodce daněmi pro mladé (brigády, online výdělky, krypto...)")

    # =========================================================================
    # SEKCE 4: GLOBÁLNÍ SOUVISLOSTI
    # =========================================================================
    elif selected_section_5 == "4. Globální souvislosti a svět bez hranic":
        st.markdown("### 4. Globální souvislosti a svět bez hranic")
        st.info("Zde bude obsah pro 4.1 až 4.7 (Globalizace, EU, dodavatelské řetězce...)")

    # =========================================================================
    # SEKCE 5: ESG A UDRŽITELNOST
    # =========================================================================
    elif selected_section_5 == "5. ESG a udržitelná ekonomika":
        st.markdown("### 5. ESG a udržitelná ekonomika")
        st.info("Zde bude obsah pro 5.1 až 5.6 (Greenwashing, cirkulární ekonomika, odpovědný spotřebitel...)")

    # =========================================================================
    # SEKCE 6: AKTIVITY A PŘÍPADOVÉ STUDIE
    # =========================================================================
    elif selected_section_5 == "6. Aktivity a případové studie na závěr":
        st.markdown("### 6. Aktivity a případové studie na závěr")
        st.info("Zde budou interaktivní případové studie (Levné tričko, Student vydělává online, Obec rozhoduje o rozpočtu...)")
