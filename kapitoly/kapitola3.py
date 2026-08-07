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
        "3. Náklady, výnosy a zisk (připravuje se)",
        "4. Majetek firmy (připravuje se)",
        "5. Kalkulace a bod zvratu (připravuje se)",
        "6. Efektivita a štíhlá výroba (připravuje se)"
    ]
    
    selected_section_3 = st.selectbox("📌 Přechod na podkapitolu:", section_options_3, index=0)
    st.divider()

    # =========================================================================
    # SEKCE 1: VÝROBNÍ PROCES A ORGANIZACE VÝROBY
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

        st.markdown("""
        <div class='box-green'>
            🧠 <b>Důležité:</b> Moderní výroba nestojí jen na strojích a materiálu. Velkou hodnotu mají také informace — například přesná data o objednávkách, kvalitě, zásobách nebo spotřebě energie.
        </div>
        """, unsafe_allow_html=True)

    elif selected_section_3 == "1.2 Typy výroby":
        st.markdown("### 1.2 Typy výroby")
        st.write("Výrobu lze rozdělit podle toho, kolik kusů firma vyrábí a jak moc se jednotlivé výrobky liší. Typ výroby ovlivňuje cenu, organizaci práce, potřebu zásob, nároky na stroje i způsob kontroly kvality.")

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
        st.write("Výrobní kapacita vyjadřuje maximální možný objem produkce za určité období (např. počet kusů za hodinu, směnu nebo měsíc).")
        
        st.markdown("<div class='box-blue'><b>Výrobní kapacita = maximální možný objem výroby za jednotku času</b></div>", unsafe_allow_html=True)
        
        st.write("Firma se obvykle nesnaží kapacitu využívat za každou cenu na 100 %. Příliš vysoké vytížení může vést k přetížení pracovníků, poruchám, zmetkům nebo zpoždění zakázek. Cílem je optimální využití (obvykle kolem 80–90 %), které nechává polštář pro údržbu a výkyvy poptávky.")

        st.divider()
        st.markdown("<div class='box-yellow'>🧮 <b>Kalkulačka využití kapacity</b></div>", unsafe_allow_html=True)
        st.write("Vyzkoušej si namodelovat výrobu a sleduj, co se stane, když kapacitu přeženeš.")
        
        col1, col2 = st.columns([1, 1])
        with col1:
            max_kapacita = st.number_input("Maximální kapacita (ks):", min_value=1, value=5000, step=100)
            skutecnost = st.slider("Skutečná výroba (ks):", min_value=0, max_value=int(max_kapacita * 1.2), value=4200, step=50)
        
        vyuziti = (skutecnost / max_kapacita) * 100
        
        with col2:
            st.metric("Využití výrobní kapacity", f"{vyuziti:.1f} %")
            
            # Bezpečnostní pojistka pro zobrazení progress baru (musí být 0.0 - 1.0)
            progress_val = min(vyuziti / 100, 1.0)
            st.progress(progress_val)
            
            if vyuziti > 100:
                st.error("💥 KRITICKÝ STAV: Výroba jede nad limit! Hrozí havárie strojů, vyhoření lidí a obrovská chybovost. Nutné investovat do nových strojů.")
            elif vyuziti >= 95:
                st.warning("⚠️ RIZIKO: Jste na hraně. Každá malá porucha zastaví dodávky zákazníkům. Nemáte čas na údržbu.")
            elif vyuziti >= 75:
                st.success("✅ OPTIMÁLNÍ: Výroba běží efektivně a zároveň máte prostor pro údržbu strojů nebo nečekanou zakázku.")
            else:
                st.info("📉 NEEFEKTIVNÍ: Stroje a lidé stojí. Platíte fixní náklady (např. nájem), ale nevyrábíte dost, aby se to zaplatilo.")

    elif selected_section_3 == "1.4 Logistika, zásobování a JIT":
        st.markdown("### 1.4 Logistika a zásobování")
        st.write("Logistika řeší tok materiálu, výrobků, informací a peněz. Zásobování zajišťuje, aby firma měla správný materiál ve správném množství, kvalitě, čase a za přijatelnou cenu.")
        
        st.markdown("#### Možnosti řízení zásob")
        st.write("Neexistuje jeden správný systém. Moderní firmy kombinují různé přístupy podle typu materiálu:")
        
        st.markdown("""
        * 🛡️ **Pojistná zásoba:** Firma drží materiál na skladě "pro jistotu". Váže to sice peníze, ale výroba se nezastaví při výpadku dodavatele.
        * ⚡ **Just-in-Time (JIT):** Materiál přichází do výroby co nejpozději — ideálně právě ve chvíli, kdy je potřeba.
        * 🚥 **Kanban:** Vizuální systém (karty/bedýnky). Další materiál se objedná až ve chvíli, kdy se vyprázdní bedýnka na lince. Zabraňuje přehlcení skladu.
        """)

        st.markdown("""
        <div class='box-green'>
            ⚖️ <b>Výhoda Just-in-Time:</b> Firma neváže tolik peněz ve skladu a šetří místo.
        </div>
        <div class='box-red'>
            ⚠️ <b>Riziko Just-in-Time:</b> Pokud se dodávka zpozdí (např. kvůli havárii nebo zpožděné lodi), výroba se může rychle zastavit.
        </div>
        """, unsafe_allow_html=True)

        st.divider()
        st.markdown("<div class='box-yellow'>⚖️ <b>Rozhodnutí manažera: Just-in-Time, nebo pojistná zásoba?</b></div>", unsafe_allow_html=True)
        st.write("Jsi ředitel výroby horských kol. Dodávky speciálních přehazovaček z Asie váznou. Běžné šroubky ale odebíráš ze železářství ve vedlejším městě. Jakou strategii zvolíš pro celou firmu?")
        
        rozhodnuti = st.radio("Tvoje strategie:", ["Vyber...", "Vše jet přes Just-in-Time", "Vše držet jako Pojistnou zásobu", "Kombinace obojího"])
        zdovodneni = st.text_area("Tvé zdůvodnění (proč ses tak rozhodl/a?):", placeholder="Napiš svou úvahu...")
        
        if st.button("Vyhodnotit rozhodnutí"):
            if rozhodnuti == "Kombinace obojího" and len(zdovodneni) > 5:
                st.success("Výborné manažerské rozhodnutí! U běžných a levných dílů (šroubky) dává smysl JIT nebo malá zásoba. U strategických a nejistých dílů (přehazovačky) je nutná pojistná zásoba, jinak se zastaví prodej celých kol.")
            elif rozhodnuti == "Vyber...":
                st.warning("Musíš zvolit jednu z možností.")
            elif len(zdovodneni) <= 5:
                st.warning("Napiš alespoň krátké zdůvodnění.")
            else:
                st.error("Toto je riskantní. Extrém (vše JIT = riziko zastavení výroby; vše na sklad = došly by vám peníze na účtu) v reálném světě často nefunguje. Zkus kombinaci.")

    # =========================================================================
    # SEKCE 2: ŘÍZENÍ JAKOSTI
    # =========================================================================
    elif selected_section_3 == "2.1 Řízení jakosti a kvality":
        st.markdown("### 2.1 Řízení jakosti: kvalita ve výrobě")
        st.markdown("""
        <div class='box-blue'>
            ✅ <b>Jakost (kvalita)</b> znamená schopnost výrobku nebo služby splnit požadavky a očekávání zákazníka.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### Kontrola kvality vs. řízení jakosti")
        st.write("Kontrola kvality se často zaměřuje na odhalení chyb na konci výroby. Řízení jakosti jde dál: snaží se nastavit celý proces tak, aby chyby pokud možno vůbec nevznikaly.")

        st.markdown("""
        | Přístup | Co řeší | Příklad z praxe |
        | :--- | :--- | :--- |
        | 🔍 **Kontrola kvality** | Hledá chyby u hotového výrobku. | Vyřazení zmetků po dokončení výroby. |
        | 🛡️ **Řízení jakosti** | Předchází chybám během procesu. | Standardy práce, školení, průběžné měření. |
        """)

        st.divider()
        st.markdown("<div class='box-yellow'>🔍 <b>Kvíz: Jde o kontrolu, nebo prevenci?</b></div>", unsafe_allow_html=True)
        
        k1 = st.radio("Vyřazení vadných výrobků po dokončení:", ["-", "Kontrola kvality", "Prevence (Řízení jakosti)"], horizontal=True, key="kvalita1")
        k2 = st.radio("Školení pracovníků před výrobou:", ["-", "Kontrola kvality", "Prevence (Řízení jakosti)"], horizontal=True, key="kvalita2")
        k3 = st.radio("Poka-Yoke (tvarování dílu tak, aby nešel vložit obráceně):", ["-", "Kontrola kvality", "Prevence (Řízení jakosti)"], horizontal=True, key="kvalita3")
        k4 = st.radio("Zkouška funkčnosti hotového výrobku před odesláním:", ["-", "Kontrola kvality", "Prevence (Řízení jakosti)"], horizontal=True, key="kvalita4")
        
        if st.button("Vyhodnotit kvíz"):
            if k1 == "Kontrola kvality" and k2 == "Prevence (Řízení jakosti)" and k3 == "Prevence (Řízení jakosti)" and k4 == "Kontrola kvality":
                st.success("Přesně! Všechno, co se děje před nebo během procesu, je řízení. Co se děje až s hotovým kusem, je kontrola.")
            else:
                st.warning("Zkus to ještě promyslet. Pravidlo: Prevence zabrání chybě. Kontrola ji jen najde, když už se stala.")

    elif selected_section_3 == "2.2 Následky nekvality a TQM":
        st.markdown("### 2.2 Normy, TQM a následky nekvality")
        
        st.write("**Normy a certifikace** (např. ISO) pomáhají nastavit jednotný systém. Znamenají, že firma má jasně popsaný a kontrolovaný systém, jak kvalitu řídit.")
        
        st.write("**Total Quality Management (TQM)** je přístup, ve kterém se na kvalitě podílí celá firma (od výroby až po zákaznickou podporu). Zdůrazňuje orientaci na zákazníka, práci s daty a zapojení zaměstnanců.")

        st.markdown("#### Následky nekvality")
        st.write("Nekvalita má přímé ekonomické dopady: reklamace, vrácení zboží, opravy, zpoždění zakázek a fatální ztrátu dobrého jména (goodwill).")

        st.markdown("""
        <div class='box-red'>
            ⚠️ <b>Ekonomická pointa:</b> Nekvalitní výrobek je vždy dražší než poctivá prevence. Zaplatíte materiál i práci zbytečně, a ještě naštvete zákazníka.
        </div>
        """, unsafe_allow_html=True)

        st.divider()
        st.markdown("<div class='box-yellow'>🧮 <b>Kalkulačka nákladů na zmetky</b></div>", unsafe_allow_html=True)
        st.write("Podívejme se, kolik peněz firmu stojí, když kašle na kvalitu.")
        
        c1, c2 = st.columns(2)
        with c1:
            vyrobeno = st.number_input("Celkový počet vyrobených kusů:", min_value=1, value=1000, step=100)
            chybovost = st.slider("Chybovost výroby (%)", min_value=0, max_value=20, value=5)
            cena_kusu = st.number_input("Výrobní náklad na jeden kus (Kč):", min_value=1, value=500, step=50)
            
        zmetky_ks = int(vyrobeno * (chybovost / 100))
        ztrata = zmetky_ks * cena_kusu
        
        with c2:
            st.metric("Počet vadných kusů", f"{zmetky_ks} ks")
            st.metric("Finanční ztráta firmy", f"{ztrata:,} Kč".replace(",", " "))
            
            if ztrata > 0:
                st.markdown(f"<div class='box-purple'>🧠 <b>AI Mentoring:</b> Představte si, že byste těchto {ztrata:,} Kč investovali raději do školení zaměstnanců. Co myslíte, vyplatilo by se to?</div>", unsafe_allow_html=True)

    else:
        st.info("Obsah pro tuto podkapitolu se právě připravuje. Pokračujte ve výběru výše.")
