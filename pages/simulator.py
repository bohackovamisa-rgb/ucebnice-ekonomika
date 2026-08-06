# 🚀 Simulátor
        with st.container(border=True):
            st.markdown("### 🚀 SPUSTIT ŠKOLNÍ INVESTIČNÍ SIMULÁTOR")
            st.markdown("#### Otevřít simulátor akcií a bitcoinu")
            st.write("Interaktivní aktivita: Vyzkoušej si modelové investování nanečisto — bez skutečných peněz a bez rizika. Sleduj, jak se může měnit hodnota akcií a bitcoinu v čase.")
            
            st.write("")
            
            # Tímto příkazem aplikace vytvoří tlačítko, které tě přesměruje do souboru pages/simulator.py
            st.page_link("pages/simulator.py", label="🚀 PŘEJÍT DO SIMULÁTORU", use_container_width=True)
            
            st.write("")
            st.caption("Důležité: Simulátor je pouze vzdělávací pomůcka. Nejde o investiční doporučení.")
