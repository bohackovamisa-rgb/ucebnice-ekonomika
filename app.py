elif selected_section_2 == "2.6 Psychologie utrácení":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2.6</div>", unsafe_allow_html=True)
        st.markdown("## Psychologie utrácení: proč nerozhodujeme vždy racionálně")
        
        with st.container(border=True):
            st.write("Lidé nejsou kalkulačky. Často se rozhodujeme podle emocí, únavy, tlaku okolí, reklamy, strachu, že něco propásneme, nebo podle toho, co nám ukáže aplikace.")

            st.markdown("""
            | Past | Jak funguje | Obrana |
            | :--- | :--- | :--- |
            | **FOMO** | Strach, že mi něco uteče. | Počkej 24 hodin před nákupem. |
            | **Sleva** | Pocit úspory, i když kupuji zbytečnost. | Ptej se: koupil/a bych to i bez slevy? |
            | **Sociální srovnávání** | Chci životní styl, který vidím u ostatních. | Rozliš realitu a vybraný obsah na sítích. |
            | **Mikrotransakce** | Malé částky vypadají neškodně. | Spočítej roční součet. |
            | **Odložená platba** | Nákup nebolí hned. | Ber ji jako dluh, ne jako slevu. |
            """)

            st.markdown("### Kalkulačka času: kolik života stojí nákup")
            st.write("Cena věci není jen částka v korunách. Dá se přepočítat i na čas, který musí člověk pracovat, aby si ji mohl dovolit.")
            st.markdown("**Vzorec:** Cena věci ÷ čistá hodinová mzda = počet hodin práce")
