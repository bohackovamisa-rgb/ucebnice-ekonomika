import streamlit as st
import math

def render():
    st.markdown("<span class='hero-badge'>Kapitola 3</span>", unsafe_allow_html=True)
    st.title("3. Výroba, náklady a efektivita")
    st.markdown("<p style='font-size: 1rem; color: #64748b; margin-bottom: 1.5rem;'>Výroba není jen „něco vyrobit“. Je to práce s náklady, časem, kvalitou a rozhodováním o tom, co zákazník skutečně považuje za hodnotu.</p>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown("""
        <div class='box-blue'>
            <strong>⚙️ Pointa kapitoly:</strong> V této kapitole se propojí ekonomické počítání s praktickým pohledem na to, jak firma nastavuje cenu, odstraňuje plýtvání a sleduje výkon. Naučíte se rozdíl mezi náklady, výnosy a ziskem a zjistíte, jak zlepšovat procesy bez zbytečného chaosu.
        </div>
        """, unsafe_allow_html=True)

    # 📌 JEDNOTNÁ NABÍDKA PODKAPITOL
    section_options_3 = [
        "1.1 Výrobní proces a faktory",
        "1.2 Typy výroby",
        "1.3 Výrobní kapacita",
        "1.4 Logistika, zásobování a JIT",
        "2.1 Řízení jakosti a kvality",
        "2.2 Následky nekvality a TQM",
        "3.1 Náklad vs. výdaj a pojetí zisku",
        "3.2 Členění nákladů a kalkulační vzorec",
        "3.3 Kalkulace nákladů",
        "3.4 Bod zvratu a jeho graf",
        "3.5 Měření výkonu a rentabilita",
        "4. Majetek firmy (připravuje se)",
        "5. Kalkulace a ceny (připravuje se)",
        "6. Efektivita a štíhlá výroba (připravuje se)"
    ]
    
    selected_section_3 = st.selectbox("📌 Přechod na podkapitolu:", section_options_3, index=0)
    st.divider()

    # =========================================================================
    # SEKCE 1: VÝROBNÍ PROCES
    # =========================================================================
    if selected_section_3 == "1.1 Výrobní proces a faktory":
        st.markdown("### 1.1 Výrobní proces a faktory")
        st.markdown("""
        <div class='box-blue'>
            🏭 <b>Podstata výroby:</b> Výroba je transformační proces, při kterém firma mění vstupy na výstupy. Zjednodušeně platí: vstupy → technologie → výstupy.
        </div>
        """, unsafe_allow_html=True)
        st.write("Výrobní proces zahrnuje všechny činnosti, které vedou ke vzniku výrobku nebo služby. Firma do procesu vkládá zdroje, používá určitou technologii a výsledkem je produkt, který má hodnotu pro zákazníka.")
        st.markdown("#### Základní výrobní faktory:")
        st.markdown("""
        * 🧑‍🏭 **Lidská práce** — znalosti, dovednosti, čas a výkon pracovníků.
        * 🏗️ **Dlouhodobý majetek** — stroje, budovy, zařízení, výrobní linky nebo software.
        * 📦 **Oběžný majetek** — materiál, zásoby, polotovary, hotové výrobky a peníze.
        * 📊 **Informace** — data, technologické postupy, receptury, plány, objednávky a know-how.
        """)
        st.markdown("<div class='box-green'>🧠 <b>Důležité:</b> Moderní výroba nestojí jen na strojích a materiálu. Velkou hodnotu mají také informace.</div>", unsafe_allow_html=True)

    elif selected_section_3 == "1.2 Typy výroby":
        st.markdown("### 1.2 Typy výroby")
        st.write("Výrobu lze rozdělit podle toho, kolik kusů firma vyrábí a jak moc se jednotlivé výrobky liší.")
        st.markdown("""
        | Typ výroby | Charakteristika | Příklad |
        | :--- | :--- | :--- |
        | 🎨 **Kusová výroba** | Vyrábí se jednotlivé kusy podle konkrétní zakázky. | Nábytek na míru, svatební šaty, prototyp. |
        | 📦 **Sériová výroba** | Vyrábí se menší nebo větší série stejných výrobků. | Limitovaná edice mikin, školní diáře. |
        | 🏭 **Hromadná výroba** | Vyrábí se velké množství stejných výrobků. | Nápoje, pečivo, šroubky, běžná elektronika. |
        """)
        st.divider()
        st.markdown("<div class='box-yellow'>🧩 <b>Kvíz: O jaký typ výroby se jedná?</b></div>", unsafe_allow_html=True)
        q1 = st.selectbox("Nábytek vyrobený přesně podle rozměrů zákazníka:", ["Vyber...", "Kusová", "Sériová", "Hromadná"], key="q1")
        q2 = st.selectbox("300 stejných školních mikin:", ["Vyber...", "Kusová", "Sériová", "Hromadná"], key="q2")
        q3 = st.selectbox("Tisíce rohlíků každý den:", ["Vyber...", "Kusová", "Sériová", "Hromadná"], key="q3")
        if st.button("✅ Zkontrolovat řešení"):
            if q1 == "Kusová" and q2 == "Sériová" and q3 == "Hromadná":
                st.success("Přesně tak! Skvělá práce. 🎯")
            else:
                st.error("Něco tam nesedí. Zkus se zamyslet nad tím, kolik kusů se vyrábí a zda jsou na míru.")

    elif selected_section_3 == "1.3 Výrobní kapacita":
        st.markdown("### 1.3 Výrobní kapacita")
        st.markdown("<div class='box-blue'><b>Výrobní kapacita = maximální možný objem výroby za jednotku času</b></div>", unsafe_allow_html=True)
        st.write("Firma se obvykle nesnaží kapacitu využívat za každou cenu na 100 %. Cílem je optimální využití (obvykle kolem 80–90 %), které nechává polštář pro údržbu a nečekané výkyvy.")
        st.divider()
        st.markdown("<div class='box-yellow'>🧮 <b>Interaktivní model: Tisková farma na 3D klíčenky</b></div>", unsafe_allow_html=True)
        st.write("Máš 5 3D tiskáren. Každá vytiskne max 10 klíčenek denně. Absolutní denní kapacita je **50 klíčenek**.")
        zakazky = st.slider("Počet slíbených zakázek (kusů):", min_value=0, max_value=60, value=40)
        vyuziti = (zakazky / 50) * 100
        st.metric("Vytížení tvých tiskáren", f"{vyuziti:.0f} %")
        progress_val = min(vyuziti / 100, 1.0)
        st.progress(progress_val)
        if vyuziti > 100:
            st.error("💥 KRITICKÁ CHYBA: Slíbil jsi víc, než tvé stroje fyzicky zvládnou!")
        elif vyuziti == 100:
            st.warning("⚠️ RIZIKO: Jedeš na absolutní doraz. Není prostor pro jedinou chybu.")
        elif vyuziti >= 80:
            st.success("✅ IDEÁLNÍ STAV: Vyděláváš a máš rezervu pro nenadálé události.")
        else:
            st.info("📉 NEEFEKTIVNÍ: Tiskárny stojí a nevydělávají.")

    elif selected_section_3 == "1.4 Logistika, zásobování a JIT":
        st.markdown("### 1.4 Logistika a zásobování")
        st.write("Zásobování zajišťuje materiál ve správném množství, kvalitě, čase a za přijatelnou cenu.")
        st.markdown("""
        * 🛡️ **Pojistná zásoba:** Materiál na skladě "pro jistotu". Váže peníze, ale jistí výrobu.
        * ⚡ **Just-in-Time (JIT):** Materiál přichází do výroby právě ve chvíli potřeby.
        * 🚥 **Kanban:** Vizuální systém objednávání podle okamžité spotřeby.
        """)
        st.markdown("""
        <div class='box-green'>⚖️ <b>Výhoda Just-in-Time:</b> Firma neváže tolik peněz ve skladu.</div>
        <div class='box-red'>⚠️ <b>Riziko Just-in-Time:</b> Pokud se dodávka zpozdí, výroba okamžitě stojí.</div>
        """, unsafe_allow_html=True)
        st.divider()
        st.markdown("<div class='box-yellow'>⚖️ <b>Rozhodnutí manažera: Just-in-Time, nebo pojistná zásoba?</b></div>", unsafe_allow_html=True)
        rozhodnuti = st.radio("Dodávky speciálních přehazovaček z Asie váznou, běžné šroubky ale bereš z vedlejšího města. Tvoje strategie:", ["Vyber...", "Vše jet přes Just-in-Time", "Vše držet jako Pojistnou zásobu", "Kombinace obojího"])
        if st.button("Vyhodnotit rozhodnutí"):
            if rozhodnuti == "Kombinace obojího":
                st.success("Správně! U levných a dostupných dílů JIT, u rizikových pojistná zásoba.")
            elif rozhodnuti != "Vyber...":
                st.error("Extrémní řešení v praxi nefunguje. Zkus kombinaci.")

    # =========================================================================
    # SEKCE 2: ŘÍZENÍ JAKOSTI
    # =========================================================================
    elif selected_section_3 == "2.1 Řízení jakosti a kvality":
        st.markdown("### 2.1 Řízení jakosti: kvalita ve výrobě")
        st.markdown("<div class='box-blue'>✅ <b>Jakost (kvalita)</b> znamená schopnost výrobku splnit požadavky zákazníka.</div>", unsafe_allow_html=True)
        st.markdown("""
        | Přístup | Co řeší | Příklad z praxe |
        | :--- | :--- | :--- |
        | 🔍 **Kontrola kvality** | Hledá chyby u hotového výrobku. | Vyřazení zmetků po dokončení. |
        | 🛡️ **Řízení jakosti** | Předchází chybám během procesu. | Standardy, školení, prevence. |
        """)
        st.divider()
        st.markdown("<div class='box-yellow'>🔍 <b>Kvíz: Jde o kontrolu, nebo prevenci?</b></div>", unsafe_allow_html=True)
        k1 = st.radio("Vyřazení vadných výrobků po dokončení:", ["-", "Kontrola", "Prevence"], horizontal=True, key="kvalita1")
        k2 = st.radio("Školení pracovníků před výrobou:", ["-", "Kontrola", "Prevence"], horizontal=True, key="kvalita2")
        if st.button("Vyhodnotit kvíz"):
            if k1 == "Kontrola" and k2 == "Prevence":
                st.success("Přesně! Prevence zabrání chybě. Kontrola ji jen najde, když už se stala.")
            else:
                st.warning("Zkus to ještě promyslet.")

    elif selected_section_3 == "2.2 Následky nekvality a TQM":
        st.markdown("### 2.2 Normy, TQM a následky nekvality")
        st.write("**Total Quality Management (TQM)** je přístup, ve kterém se na kvalitě podílí celá firma (od výroby až po zákaznickou podporu).")
        st.markdown("<div class='box-red'>⚠️ <b>Ekonomická pointa:</b> Nekvalitní výrobek je vždy dražší než poctivá prevence. Zaplatíte materiál i práci zbytečně, a ještě naštvete zákazníka.</div>", unsafe_allow_html=True)
        st.divider()
        st.markdown("<div class='box-yellow'>🧮 <b>Kalkulačka nákladů na zmetky</b></div>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            vyrobeno = st.number_input("Celkem vyrobených kusů:", min_value=1, value=1000, step=100)
            chybovost = st.slider("Chybovost výroby (%)", min_value=0, max_value=20, value=5)
            cena_kusu = st.number_input("Náklad na kus (Kč):", min_value=1, value=500, step=50)
        zmetky_ks = int(vyrobeno * (chybovost / 100))
        ztrata = zmetky_ks * cena_kusu
        with c2:
            st.metric("Počet vadných kusů", f"{zmetky_ks} ks")
            st.metric("Finanční ztráta", f"{ztrata:,} Kč".replace(",", " "))

    # =========================================================================
    # SEKCE 3: NÁKLADY, VÝNOSY A ZISK
    # =========================================================================
    elif selected_section_3 == "3.1 Náklad vs. výdaj a pojetí zisku":
        st.markdown("### 3.1 Náklady, výnosy a zisk: základní teorie")
        st.markdown("<div class='box-blue'>🧮 <b>Základní vztah:</b> Zisk vzniká tehdy, když jsou výnosy vyšší než náklady.</div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Náklad vs. Výdaj")
            st.markdown("""
            * **Náklad:** Spotřeba zdrojů v penězích (odpis stroje).
            * **Výdaj:** Skutečný odtok peněz z účtu (zaplacení faktury).
            """)
        with col2:
            st.markdown("#### Výnos vs. Příjem")
            st.markdown("""
            * **Výnos:** Vznik nároku na zaplacení (vystavená faktura).
            * **Příjem:** Skutečný přítok peněz na účet (zákazník zaplatí).
            """)
        
        st.divider()
        st.markdown("<div class='box-yellow'>📝 <b>Kvíz: O jaký pojem se jedná?</b></div>", unsafe_allow_html=True)
        with st.form("kviz_pojmy"):
            q1 = st.selectbox("Zaplacení faktury dodavateli:", ["Vyber...", "Náklad", "Výdaj", "Výnos", "Příjem"])
            q2 = st.selectbox("Spotřeba materiálu ve výrobě:", ["Vyber...", "Náklad", "Výdaj", "Výnos", "Příjem"])
            if st.form_submit_button("Zkontrolovat"):
                if q1 == "Výdaj" and q2 == "Náklad":
                    st.success("✅ Výborně!")
                else:
                    st.error("Něco se nepovedlo. Výdaj/Příjem je pohyb peněz. Náklad/Výnos je spotřeba/nárok.")

    elif selected_section_3 == "3.2 Členění nákladů a kalkulační vzorec":
        st.markdown("### 3.2 Fixní, variabilní, přímé a nepřímé náklady")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
            * 🔒 **Fixní:** Nemění se podle počtu kusů (nájem, odpisy).
            * 📈 **Variabilní:** Rostou podle objemu výroby (materiál).
            """)
        with c2:
            st.markdown("""
            * 🎯 **Přímé:** Určitelné na jeden kus (materiál na 1 tričko).
            * 🌫️ **Nepřímé:** Společné pro firmu, musí se rozpočítat (nájem).
            """)
        
        st.divider()
        st.markdown("#### Kalkulační vzorec")
        st.markdown("<div class='box-blue'>Přímý materiál + Přímé mzdy + Ostatní přímé náklady + Výrobní režie = <b>Vlastní náklady výroby</b><br>+ Správní režie = <b>Vlastní náklady výkonu</b><br>+ Odbytové náklady = <b>Úplné vlastní náklady</b><br>+ Zisková přirážka = <b>Prodejní cena bez DPH</b></div>", unsafe_allow_html=True)

    elif selected_section_3 == "3.3 Kalkulace nákladů":
        st.markdown("### 3.3 Kalkulace nákladů")
        st.write("Odpovídá na otázky jako: *Za jakou cenu prodávat? Vyplatí se zakázka?*")
        st.markdown("#### 1. Kalkulace úplných nákladů")
        st.markdown("<div class='box-gray'><b>Úplné vlastní náklady = přímé náklady + podíl nepřímých nákladů</b></div>", unsafe_allow_html=True)
        st.markdown("#### 2. Kalkulace neúplných nákladů")
        st.write("Pracuje jen s variabilními náklady.")
        st.markdown("<div class='box-blue'><b>Příspěvek na úhradu na kus = prodejní cena za kus − variabilní náklady na kus</b></div>", unsafe_allow_html=True)

    elif selected_section_3 == "3.4 Bod zvratu a jeho graf":
        st.markdown("### 3.4 Bod zvratu (Break-even point)")
        st.write("Bod zvratu je objem prodeje, při kterém firma nemá ani zisk, ani ztrátu.")
        st.markdown("<div class='box-gray'><b>Bod zvratu (ks) = Fixní náklady / (Cena za kus − Variabilní náklady na kus)</b></div>", unsafe_allow_html=True)
        
        st.divider()
        st.markdown("<div class='box-purple'>🕹️ <b>Simulátor: Kdy začneš vydělávat?</b></div>", unsafe_allow_html=True)
        col_in, col_out = st.columns([1, 1.2])
        with col_in:
            be_fix = st.number_input("Fixní náklady za měsíc (Kč):", value=20000, step=1000)
            be_cena = st.number_input("Prodejní cena za 1 kus (Kč):", value=500, step=50)
            be_var = st.number_input("Variabilní náklad na 1 kus (Kč):", value=200, step=50)
        
        with col_out:
            prispevek = be_cena - be_var
            if prispevek <= 0:
                st.error("Chyba: Tvá cena nepokryje ani variabilní náklady!")
            else:
                bod_zvratu = math.ceil(be_fix / prispevek)
                st.metric("Příspěvek na úhradu na kus", f"{prispevek} Kč")
                st.metric("Bod zvratu (musíš prodat)", f"{bod_zvratu} kusů")
                st.success(f"Až prodáš {bod_zvratu} kusů, jsi na nule. Další kus ti přinese zisk {prispevek} Kč!")
        
        if prispevek > 0:
            try:
                import pandas as pd
                max_x = int(bod_zvratu * 2.2) if bod_zvratu > 0 else 100
                kroky = max(1, max_x // 50)
                df_graf = pd.DataFrame({"Kusy": range(0, max_x, kroky)})
                df_graf["Tržby (Výnosy)"] = df_graf["Kusy"] * be_cena
                df_graf["Celkové náklady"] = be_fix + (df_graf["Kusy"] * be_var)
                df_graf["Fixní náklady"] = be_fix
                df_graf = df_graf.set_index("Kusy")
                
                st.markdown("##### Graf bodu zvratu")
                st.line_chart(df_graf, color=["#22c55e", "#ef4444", "#64748b"])
            except ImportError:
                st.warning("Graf bodu zvratu vyžaduje knihovnu Pandas.")

    elif selected_section_3 == "3.5 Měření výkonu a rentabilita":
        st.markdown("### 3.5 Jak měřit výkon firmy (KPI) a rentabilita")
        st.markdown("<div class='box-green'>🎯 <b>Pravidlo KPI:</b> Dobré KPI má pomáhat rozhodování. Pokud ukazatel nikdo nepoužívá, je zbytečný.</div>", unsafe_allow_html=True)
        st.divider()
        st.markdown("#### Rentabilita")
        st.write("Ukazuje, jak výnosně firma využívá své zdroje.")
        st.markdown("<div class='box-yellow'>🧮 <b>Kalkulačka Rentability tržeb</b></div>", unsafe_allow_html=True)
        
        rc1, rc2 = st.columns(2)
        with rc1:
            r_trzby = st.number_input("Celkové tržby (Kč):", value=1000000, step=100000)
            r_naklady = st.number_input("Celkové náklady (Kč):", value=850000, step=100000)
        
        r_zisk = r_trzby - r_naklady
        rent_trzeb = (r_zisk / r_trzby) * 100 if r_trzby > 0 else 0
        
        with rc2:
            st.metric("Vypočítaný Zisk", f"{r_zisk:,} Kč".replace(",", " "))
            st.metric("Rentabilita tržeb (Marže)", f"{rent_trzeb:.1f} %")
            if rent_trzeb < 0:
                st.error("Firma je ve ztrátě. Rentabilita je záporná.")
            elif rent_trzeb < 5:
                st.warning("Rentabilita je velmi nízká.")
            else:
                st.success("Firma je zdravě zisková!")

    else:
        st.info("Obsah pro tuto podkapitolu se právě připravuje. Pokračujte ve výběru výše.")
