import streamlit as st
import math

def render():
    st.markdown("<span class='hero-badge'>Kapitola 3</span>", unsafe_allow_html=True)
    st.title("3. Výroba, náklady a efektivita")
    st.markdown("<p style='font-size: 1rem; color: #64748b; margin-bottom: 1.5rem;'>Od výrobního procesu a řízení zásob až po kalkulace, ceny a štíhlou výrobu.</p>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown("""
        <div class='box-blue'>
            <strong>⚙️ Pointa kapitoly:</strong> Výroba a efektivita nejsou jen o strojích na lince. Je to o schopnosti proměnit nápad v reálný produkt, správně spočítat náklady, nastavit cenovku, řídit majetek a neustále zefektivňovat procesy tak, aby firma neplýtvala zdroji.
        </div>
        """, unsafe_allow_html=True)

    # 📌 JEDNOTNÁ NABÍDKA PODKAPITOL
    section_options_3 = [
        # Sekce 1: Výrobní proces a organizace výroby
        "1.1 Výrobní proces",
        "1.2 Výrobní faktory",
        "1.3 Typy výroby",
        "1.4 Výrobní kapacita",
        "1.5 Logistika, zásobování a Just-in-Time",

        # Sekce 2: Řízení jakosti
        "2.1 Kontrola kvality vs. řízení jakosti",
        "2.2 Normy a certifikace",
        "2.3 Total Quality Management (TQM)",
        "2.4 Následky nekvality",

        # Sekce 3: Náklady, výnosy a zisk
        "3.1 Náklady, výnosy a zisk: základní teorie",
        "3.2 Náklad vs. výdaj",
        "3.3 Výnos vs. příjem",
        "3.4 Účetní pohled na zisk",
        "3.5 Pohled finanční analýzy a finančního řízení",
        "3.6 Ekonomický zisk",
        "3.7 Fixní a variabilní náklady",
        "3.8 Přímé a nepřímé náklady",
        "3.9 Kalkulační vzorec",
        "3.10 Jak lze snižovat variabilní náklady",
        "3.11 Jak lze snižovat fixní náklady",
        "3.12 Kalkulace nákladů",
        "3.13 Kalkulace úplných nákladů",
        "3.14 Kalkulace neúplných nákladů",
        "3.15 Bod zvratu",
        "3.16 Graf bodu zvratu",
        "3.17 Postup sestavení kalkulace",
        "3.18 Jak měřit výkon firmy",
        "3.19 Rentabilita",

        # Sekce 4: Majetek firmy
        "4.1 Oběžný majetek",
        "4.2 Plánování materiálu",
        "4.3 Stanovení optimální zásoby",
        "4.4 Pořízení materiálu",
        "4.5 Evidence a skladování materiálu",
        "4.6 Metody vyskladňování zásob (FIFO, LIFO, Vážený průměr)",
        "4.7 Moderní řízení zásob (ABC analýza, Kanban, JIT)",
        "4.8 Digitální skladové systémy a predikce poptávky",
        "4.9 Výpočty k oběžnému majetku a zásobám",
        "4.10 Dlouhodobý majetek a jeho dělení",
        "4.11 Plánování investic a pořízení dlouhodobého majetku",
        "4.12 Opotřebení a odpisy",
        "4.13 Výpočet odpisů",
        "4.14 Vyřazení a evidence dlouhodobého majetku",
        "4.15 Výpočty k dlouhodobému majetku",

        # Sekce 5: Kalkulace, ceny a bod zvratu
        "5.1 Cena jako strategie v praxi",
        "5.2 Moderní cenové strategie",
        "5.3 Náklady v digitálním světě: nulové mezní náklady",
        "5.4 Podnikání bez vlastního skladu a strojů",

        # Sekce 6: Efektivita, štíhlá výroba a technologie
        "6.1 Štíhlá výroba",
        "6.2 Poka-Yoke: proces bez chyb",
        "6.3 5S a Kanban",
        "6.4 Průmysl 4.0, AI a automatizace",
        "6.5 Cirkulární ekonomika a udržitelná výroba",
        "6.6 KPI a dashboardy",

        # Závěrečné moduly
        "7. Praktická dílna / mini-projekt",
        "8. Případové studie"
    ]
    
    selected_section_3 = st.selectbox("📌 Přechod na podkapitolu:", section_options_3, index=0)
    st.divider()

    # --- ZOBRAZENÍ OBSAHU PODLE VYBRANÉ PODKAPITOLY ---
    if selected_section_3.startswith("1.1"):
        st.markdown("### 1.1 Výrobní proces")
        st.write("Zde bude výklad k výrobnímu procesu...")

    elif selected_section_3.startswith("1.2"):
        st.markdown("### 1.2 Výrobní faktory")
        st.write("Zde bude výklad k výrobním faktorům...")

# =========================================================================
    # SEKCE 1: VÝROBNÍ PROCES A ORGANIZACE VÝROBY
    # =========================================================================
    if selected_section_3 == "1.1 Výrobní proces":
        st.markdown("### 1.1 Výrobní proces")
        
        st.markdown("""
        <div class='box-blue'>
            🏭 <b>Podstata výroby:</b> Výroba je transformační proces, při kterém firma mění vstupy na výstupy. Zjednodušeně platí: vstupy → technologie → výstupy.
        </div>
        """, unsafe_allow_html=True)

        st.write("Výrobní proces zahrnuje všechny činnosti, které vedou ke vzniku výrobku nebo služby. Firma do procesu vkládá zdroje, používá určitou technologii a výsledkem je produkt, který má hodnotu pro zákazníka.")
        
        st.info("📦 **Vstupy** → ⚙️ **Technologie a práce** → 🎁 **Výstupy**")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Co jsou vstupy?**")
            st.write("Například materiál, práce lidí, stroje, energie, informace, kapitál nebo know-how.")
        with col2:
            st.markdown("**Co jsou výstupy?**")
            st.write("Hotové výrobky, služby, polotovary nebo jiné výsledky činnosti firmy.")

    elif selected_section_3 == "1.2 Výrobní faktory":
        st.markdown("### 1.2 Výrobní faktory")
        st.write("Mezi základní výrobní faktory patří:")
        
        st.markdown("""
        * 🧑‍🏭 **Lidská práce** — znalosti, dovednosti, čas a výkon pracovníků.
        * 🏗️ **Dlouhodobý majetek** — stroje, budovy, zařízení, výrobní linky nebo software.
        * 📦 **Oběžný majetek** — materiál, zásoby, polotovary, hotové výrobky a peníze.
        * 📊 **Informace** — data, technologické postupy, receptury, plány, objednávky a know-how.
        """)

        st.markdown("""
        <div class='box-green'>
            🧠 <b>Důležité:</b> Moderní výroba nestojí jen na strojích a materiálu. Velkou hodnotu mají také informace — například přesná data o objednávkách, kvalitě, zásobách nebo spotřebě energie.
        </div>
        """, unsafe_allow_html=True)

    elif selected_section_3 == "1.3 Typy výroby":
        st.markdown("### 1.3 Typy výroby")
        st.write("Výrobu lze rozdělit podle toho, kolik kusů firma vyrábí a jak moc se jednotlivé výrobky liší. Typ výroby ovlivňuje cenu, organizaci práce, potřebu zásob, nároky na stroje i způsob kontroly kvality.")

        # Tabulka typů výroby
        st.markdown("""
        | Typ výroby | Charakteristika | Příklad z praxe |
        | :--- | :--- | :--- |
        | 🎨 **Kusová výroba** | Vyrábí se jednotlivé kusy podle konkrétní zakázky | Nábytek na míru, svatební šaty, prototyp |
        | 📦 **Sériová výroba** | Vyrábí se menší nebo větší série stejných výrobků | Limitovaná edice mikin, školní diáře, komponenty |
        | 🏭 **Hromadná výroba** | Vyrábí se velké množství stejných výrobků | Nápoje, pečivo, šroubky, běžná elektronika |
        """)

        st.divider()
        st.markdown("<div class='box-yellow'>🧩 <b>Kvíz: O jaký typ výroby jde?</b></div>", unsafe_allow_html=True)
        
        with st.form("kviz_vyroba"):
            q1 = st.selectbox("1. Nábytek vyrobený přesně podle rozměrů zákazníka:", ["Vyber možnost...", "Kusová", "Sériová", "Hromadná"])
            q2 = st.selectbox("2. 300 stejných školních mikin:", ["Vyber možnost...", "Kusová", "Sériová", "Hromadná"])
            q3 = st.selectbox("3. Tisíce rohlíků každý den:", ["Vyber možnost...", "Kusová", "Sériová", "Hromadná"])
            
            if st.form_submit_button("Zkontrolovat odpovědi"):
                if q1 == "Kusová" and q2 == "Sériová" and q3 == "Hromadná":
                    st.success("✅ Perfektní! Chápeš to naprosto přesně.")
                    st.balloons()
                else:
                    st.warning("Něco tam ještě nesedí. Zkus to znovu! Nápověda: rohlíky se pečou ve velkém, nábytek na míru je unikát.")

    elif selected_section_3 == "1.4 Výrobní kapacita":
        st.markdown("### 1.4 Výrobní kapacita")
        st.write("Výrobní kapacita vyjadřuje maximální možný objem produkce za určité období (např. počet kusů za hodinu, směnu nebo měsíc).")
        
        st.markdown("<div class='box-blue'><b>Výrobní kapacita</b> = maximální možný objem výroby za jednotku času</div>", unsafe_allow_html=True)
        
        st.write("Firma se obvykle nesnaží kapacitu využívat za každou cenu na 100 %. Příliš vysoké vytížení může vést k přetížení pracovníků, poruchám, zmetkům nebo zpoždění zakázek. Cílem je optimální využití.")

        st.divider()
        st.markdown("<div class='box-yellow'>🧮 <b>Interaktivní kalkulačka: Využití kapacity</b></div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 1])
        with col1:
            max_kapacita = st.number_input("Maximální kapacita (ks za měsíc):", min_value=1, value=10000, step=100)
            skutecnost = st.number_input("Skutečně vyrobeno (ks):", min_value=0, max_value=max_kapacita, value=8500, step=100)
        
        vyuziti = (skutecnost / max_kapacita) * 100
        
        with col2:
            st.metric("Využití výrobní kapacity", f"{vyuziti:.1f} %")
            st.progress(vyuziti / 100)
            
            if vyuziti < 50:
                st.error("Kapacita je silně nevyužitá. Firma platí drahé stroje a lidi, kteří nemají co dělat.")
            elif vyuziti > 95:
                st.warning("Pozor! Jste na hraně přetížení. Hrozí poruchy a únava materiálu i lidí.")
            else:
                st.success("Ideální stav! Výroba běží efektivně a zbývá polštář pro nečekané události.")

    elif selected_section_3 == "1.5 Logistika, zásobování a Just-in-Time":
        st.markdown("### 1.5 Logistika, zásobování a Just-in-Time")
        st.write("Logistika řeší tok materiálu, výrobků, informací a peněz. Zásobování zajišťuje, aby firma měla správný materiál ve správném množství, kvalitě, čase a za přijatelnou cenu.")
        
        st.markdown("#### Filozofie Just-in-Time (JIT)")
        st.write("Metoda Just-in-Time znamená, že materiál přichází do výroby co nejpozději — ideálně právě ve chvíli, kdy je potřeba. Cílem je minimalizovat skladové zásoby.")
        
        col_pro, col_con = st.columns(2)
        with col_pro:
            st.markdown("<div class='box-green'>✅ <b>Výhoda JIT:</b> Firma neváže tolik peněz ve skladu a šetří místo.</div>", unsafe_allow_html=True)
        with col_con:
            st.markdown("<div class='box-red'>⚠️ <b>Riziko JIT:</b> Pokud se dodávka zpozdí, výroba se může rychle zastavit.</div>", unsafe_allow_html=True)

        st.divider()
        st.markdown("<div class='box-yellow'>⚖️ <b>Rozhodovací scénář: Jak bys řídil zásoby ty?</b></div>", unsafe_allow_html=True)
        
        rozhodnuti = st.radio("Jsi manažerem automobilky. Dodávky čipů z Asie jsou poslední dobou kvůli dopravě velmi nespolehlivé. Jaký systém zvolíš?", 
                              ["Vyber strategii...", "Striktní Just-in-Time", "Vytvoření pojistné zásoby", "Kombinace obojího"])
        
        if rozhodnuti == "Striktní Just-in-Time":
            st.error("Tohle je v době výpadků obrovské riziko. Stačí, aby se zpozdila jedna loď, a celá linka stojí. Automobilky takto v nedávné době přišly o miliardy.")
        elif rozhodnuti == "Vytvoření pojistné zásoby":
            st.warning("Bezpečné řešení, ale vázání obrovského množství peněz ve skladu může firmu finančně vyčerpat.")
        elif rozhodnuti == "Kombinace obojího":
            st.success("Nejlepší volba pro dnešní dobu! Levné a dostupné díly řešit přes JIT, ale u kritických čipů z Asie držet strategickou pojistnou zásobu.")

    # =========================================================================
    # SEKCE 2: ŘÍZENÍ JAKOSTI
    # =========================================================================
    elif selected_section_3 == "2.1 Kontrola kvality vs. řízení jakosti":
        st.markdown("### 2.1 Kontrola kvality vs. řízení jakosti")
        st.markdown("""
        <div class='box-blue'>
            ✅ <b>Jakost (kvalita)</b> znamená schopnost výrobku nebo služby splnit požadavky a očekávání zákazníka.
        </div>
        """, unsafe_allow_html=True)
        
        st.write("Kontrola kvality se často zaměřuje na odhalení chyb na konci výroby. Řízení jakosti jde dál: snaží se nastavit celý proces tak, aby chyby pokud možno vůbec nevznikaly.")

        st.markdown("""
        | Přístup | Co řeší | Příklad z praxe |
        | :--- | :--- | :--- |
        | 🔍 **Kontrola kvality** | Hledá chyby u hotového výrobku | Vyřazení zmetků po dokončení výroby |
        | 🛡️ **Řízení jakosti** | Předchází chybám během procesu | Standardy práce, školení, Poka-Yoke, průběžné měření |
        """)

        st.divider()
        st.markdown("<div class='box-yellow'>🔍 <b>Kvíz: Jde o kontrolu, nebo prevenci?</b></div>", unsafe_allow_html=True)
        
        with st.form("kviz_kvalita"):
            k1 = st.radio("Vyřazení vadných výrobků po dokončení:", ["Kontrola kvality", "Prevence (Řízení jakosti)"], horizontal=True)
            k2 = st.radio("Školení pracovníků před výrobou:", ["Kontrola kvality", "Prevence (Řízení jakosti)"], horizontal=True)
            k3 = st.radio("Poka-Yoke (nástroj znemožňující chybu):", ["Kontrola kvality", "Prevence (Řízení jakosti)"], horizontal=True)
            k4 = st.radio("Měření hotového výrobku před odesláním:", ["Kontrola kvality", "Prevence (Řízení jakosti)"], horizontal=True)
            
            if st.form_submit_button("Zkontrolovat"):
                if k1 == "Kontrola kvality" and k2 == "Prevence (Řízení jakosti)" and k3 == "Prevence (Řízení jakosti)" and k4 == "Kontrola kvality":
                    st.success("Výborně! Kontrola řeší problém až když vznikne, prevence mu předchází.")
                else:
                    st.error("Něco je špatně. Pamatuj: Pokud se něco děje až s HOTOVÝM výrobkem, je to kontrola.")

    elif selected_section_3 == "2.2 Normy a certifikace":
        st.markdown("### 2.2 Normy a certifikace")
        st.write("Ve firmách se často používají normy a certifikace, které pomáhají nastavit jednotný systém řízení kvality. Známé jsou například normy ISO řady 9000.")
        
        st.markdown("""
        <div class='box-gray'>
            📜 <b>Smysl certifikace:</b> Neznamená automaticky dokonalý výrobek. Znamená, že firma má popsaný a kontrolovaný systém, jak kvalitu řídit a zlepšovat.
        </div>
        """, unsafe_allow_html=True)

    elif selected_section_3 == "2.3 Total Quality Management (TQM)":
        st.markdown("### 2.3 Total Quality Management (TQM)")
        st.write("TQM je přístup, ve kterém se na kvalitě podílí celá firma — nejen kontrolor na konci výroby. Do zlepšování se zapojují pracovníci výroby, vedení, obchod, nákup i zákaznická podpora.")
        
        st.markdown("**TQM zdůrazňuje:**")
        st.markdown("""
        * 🛡️ prevenci chyb,
        * 🤝 zapojení zaměstnanců,
        * 📈 průběžné zlepšování,
        * 📊 práci s daty,
        * 🎯 orientaci na zákazníka.
        """)

    elif selected_section_3 == "2.4 Následky nekvality":
        st.markdown("### 2.4 Následky nekvality")
        st.write("Nekvalita není jen technický problém. Má přímé ekonomické dopady.")
        
        st.markdown("**Co může nekvalita způsobit?**")
        st.write("Reklamace, vrácení zboží, dodatečné opravy, vyšší náklady, zpoždění zakázek, ztrátu zákazníků a poškození dobrého jména firmy (goodwill).")

        st.markdown("""
        <div class='box-red'>
            ⚠️ <b>Ekonomická pointa:</b> Nekvalitní výrobek může být dražší než poctivá prevence. Firma zaplatí materiál, práci i opravy — a navíc může přijít o důvěru zákazníka.
        </div>
        """, unsafe_allow_html=True)

        st.divider()
        st.markdown("<div class='box-yellow'>🧮 <b>Simulátor: Skrytá cena zmetků</b></div>", unsafe_allow_html=True)
        st.write("Vyzkoušej si, jak rychle dokáže malá chybovost sežrat firemní peníze.")
        
        c1, c2 = st.columns(2)
        with c1:
            vyrobeno_ks = st.number_input("Celkem vyrobeno kusů za měsíc:", value=5000, step=500)
            chybovost_pct = st.slider("Chybovost výroby (%)", min_value=0.0, max_value=20.0, value=3.0, step=0.5)
            naklad_ks = st.number_input("Náklad na výrobu 1 kusu (Kč):", value=1500, step=100)
            
        vadne_ks = int(vyrobeno_ks * (chybovost_pct / 100))
        ztrata_kc = vadne_ks * naklad_ks
        
        with c2:
            st.metric("Počet vadných kusů (zmetků)", f"{vadne_ks} ks")
            st.metric("Přímá finanční ztráta", f"{ztrata_kc:,} Kč".replace(",", " "))
            
            if ztrata_kc > 0:
                st.markdown(f"<div class='box-purple'>💡 <b>K zamyšlení:</b> Za tyto peníze by mohla firma měsíčně zaplatit např. {int(ztrata_kc/50000)} nových kvalitářů, kteří by chybám předešli. Prevence se vyplatí!</div>", unsafe_allow_html=True)
