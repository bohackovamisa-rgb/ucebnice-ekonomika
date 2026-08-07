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
        # =========================================================================
    # SEKCE 3: NÁKLADY, VÝNOSY A ZISK
    # =========================================================================
    elif selected_section_3 == "3.1 Náklad vs. výdaj a pojetí zisku":
        st.markdown("### 3.1 Náklady, výnosy a zisk: základní teorie")
        
        st.markdown("""
        <div class='box-blue'>
            🧮 <b>Základní vztah:</b> Zisk vzniká tehdy, když jsou výnosy vyšší než náklady. Důležité je ale vědět, které náklady do výpočtu opravdu patří.
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Náklad vs. Výdaj")
            st.write("V běžné řeči se zaměňují, ale v ekonomice mají odlišný význam.")
            st.markdown("""
            * **Náklad:** Spotřeba zdrojů v penězích (např. spotřeba materiálu, odpis stroje).
            * **Výdaj:** Skutečný odtok peněz z účtu/pokladny (např. zaplacení faktury).
            """)
            st.markdown("<div class='box-gray'>💡 <b>Příklad:</b> Koupíte stroj za 240 000 Kč. Peníze odejdou hned (výdaj), ale do nákladů se stroj dostává postupně přes odpisy.</div>", unsafe_allow_html=True)
            
        with col2:
            st.markdown("#### Výnos vs. Příjem")
            st.write("Podobně je potřeba rozlišovat výnos a příjem.")
            st.markdown("""
            * **Výnos:** Vznik nároku na zaplacení (např. vystavená faktura).
            * **Příjem:** Skutečný přítok peněz na účet (např. zákazník fakturu zaplatí).
            """)
            st.markdown("<div class='box-gray'>🧾 <b>Příklad:</b> Výnos máte už při vystavení faktury, ale příjem vznikne až tehdy, kdy zákazník pošle peníze.</div>", unsafe_allow_html=True)

        st.divider()
        st.markdown("#### Různé pohledy na zisk")
        st.markdown("""
        1. **Účetní zisk:** Účetní výnosy − účetní náklady. (Kolik firma "papírově" vydělala).
        2. **Pohled finančního řízení:** Zkoumá, zda zisk není jen na papíře, zda má firma hotovost a není předlužená.
        3. **Ekonomický zisk:** Zohledňuje i *implicitní (alternativní) náklady* = hodnotu nejlepší nevyužité příležitosti (např. ušlý úrok z vlastních peněz, kdyby byly v bance).
        """)
        
        st.divider()
        st.markdown("<div class='box-yellow'>📝 <b>Kvíz: O jaký pojem se jedná?</b></div>", unsafe_allow_html=True)
        with st.form("kviz_pojmy"):
            q1 = st.selectbox("Zaplacení faktury dodavateli:", ["Vyber...", "Náklad", "Výdaj", "Výnos", "Příjem"])
            q2 = st.selectbox("Spotřeba materiálu ve výrobě:", ["Vyber...", "Náklad", "Výdaj", "Výnos", "Příjem"])
            q3 = st.selectbox("Vystavená faktura zákazníkovi:", ["Vyber...", "Náklad", "Výdaj", "Výnos", "Příjem"])
            q4 = st.selectbox("Peníze skutečně přijaté na účet:", ["Vyber...", "Náklad", "Výdaj", "Výnos", "Příjem"])
            
            if st.form_submit_button("Zkontrolovat test"):
                if q1 == "Výdaj" and q2 == "Náklad" and q3 == "Výnos" and q4 == "Příjem":
                    st.success("✅ Výborně! Rozdíly mezi pojmy chápeš naprosto přesně.")
                else:
                    st.error("Něco se nepovedlo. Pamatuj: Výdaj/Příjem je fyzický pohyb peněz. Náklad/Výnos je účetní spotřeba/nárok.")

    elif selected_section_3 == "3.2 Členění nákladů a kalkulační vzorec":
        st.markdown("### 3.2 Fixní, variabilní, přímé a nepřímé náklady")
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("#### Fixní a variabilní")
            st.markdown("""
            * 🔒 **Fixní náklady:** Nemění se přímo s počtem vyrobených kusů (nájem, pojištění, odpisy, fixní mzdy).
            * 📈 **Variabilní náklady:** Rostou nebo klesají podle objemu výroby (materiál, obaly, energie na výrobu).
            """)
        with c2:
            st.markdown("#### Přímé a nepřímé")
            st.markdown("""
            * 🎯 **Přímé náklady:** Lze je přesně určit na jeden konkrétní kus (materiál na jedno tričko, potisk).
            * 🌫️ **Nepřímé náklady:** Jsou společné pro celou firmu, musí se rozpočítat (účetnictví, nájem budovy).
            """)
        
        st.divider()
        st.markdown("#### Kalkulační vzorec")
        st.write("Pomáhá zjistit, zda navržená cena pokrývá nejen materiál a práci, ale také režii a zisk.")
        st.markdown("""
        <div class='box-blue'>
            Přímý materiál<br>
            + Přímé mzdy<br>
            + Ostatní přímé náklady<br>
            + Výrobní režie<br>
            <b>= Vlastní náklady výroby</b><br>
            + Správní režie<br>
            <b>= Vlastní náklady výkonu</b><br>
            + Odbytové náklady<br>
            <b>= Úplné vlastní náklady výkonu</b><br>
            + Zisková přirážka<br>
            <b>= Prodejní cena bez DPH</b>
        </div>
        """, unsafe_allow_html=True)
        
        st.divider()
        with st.expander("🛠️ Jak lze snižovat VARIABILNÍ náklady?"):
            st.write("Vyjednat lepší cenu materiálu, snížit zmetkovitost, omezit plýtvání, zkrátit čas výroby kusu, využívat množstevní slevy.")
        with st.expander("🛠️ Jak lze snižovat FIXNÍ náklady?"):
            st.write("Přestěhovat se do levnějšího, sdílet kanceláře/stroje, pronajímat místo nákupu, automatizovat administrativu, outsourcovat činnosti.")
            st.markdown("<div class='box-red'>⚠️ <b>Pozor:</b> Snižování nákladů nesmí automaticky znamenat zhoršení kvality! Ztráta důvěry zákazníka je to nejdražší.</div>", unsafe_allow_html=True)

    elif selected_section_3 == "3.3 Kalkulace nákladů":
        st.markdown("### 3.3 Kalkulace nákladů")
        st.write("Kalkulace je postup, kterým firma zjišťuje, kolik ji stojí jeden výrobek, zakázka nebo projekt. Odpovídá na otázky jako: *Za jakou cenu prodávat? Vyplatí se zakázka?*")
        
        st.markdown("#### 1. Kalkulace úplných nákladů")
        st.write("Zahrnuje všechny náklady — přímé i nepřímé.")
        st.markdown("<div class='box-gray'><b>Úplné vlastní náklady = přímé náklady + podíl nepřímých nákladů</b></div>", unsafe_allow_html=True)
        st.write("Nepřímé náklady se rozpočítávají pomocí zvolené rozvrhové základny (např. podle strojových hodin). *Nevýhodou je, že rozpočítání může být nepřesné.*")
        
        st.markdown("#### 2. Kalkulace neúplných nákladů")
        st.write("Pracuje jen s variabilními náklady. Fixní náklady se sledují za firmu jako celek. Důležitým pojmem je zde **příspěvek na úhradu**.")
        st.markdown("<div class='box-blue'><b>Příspěvek na úhradu na kus = prodejní cena za kus − variabilní náklady na kus</b></div>", unsafe_allow_html=True)
        st.write("Tento příspěvek říká, kolik z ceny jednoho kusu zbývá na úhradu fixních nákladů a tvorbu zisku.")

        st.divider()
        st.markdown("#### Postup sestavení kalkulace")
        st.markdown("""
        1. **Určit předmět** (Co počítáme? Kus, zakázku?)
        2. **Vymezit období** (Měsíc? Rok?)
        3. **Sepsat přímé náklady** (Materiál, přímé mzdy)
        4. **Určit nepřímé náklady** (Nájem, energie, administrativa)
        5. **Zvolit způsob rozvržení** (Např. podle hodin práce)
        6. **Spočítat náklady na jednotku**
        7. **Porovnat náklady s cenou** a vyhodnotit výsledek.
        """)

    elif selected_section_3 == "3.4 Bod zvratu a jeho graf":
        st.markdown("### 3.4 Bod zvratu (Break-even point)")
        st.write("Bod zvratu je objem výroby nebo prodeje, při kterém firma nemá ani zisk, ani ztrátu. Výnosy se právě rovnají nákladům.")
        st.markdown("<div class='box-gray'><b>Bod zvratu (ks) = Fixní náklady / (Cena za kus − Variabilní náklady na kus)</b></div>", unsafe_allow_html=True)
        st.caption("Poznámka: Výraz v závorce je právě *příspěvek na úhradu na kus*.")
        
        st.divider()
        st.markdown("<div class='box-purple'>🕹️ <b>Simulátor: Kdy začneš vydělávat?</b></div>", unsafe_allow_html=True)
        st.write("Namodeluj si bod zvratu pro tvůj budoucí byznys!")
        
        col_in, col_out = st.columns([1, 1.2])
        with col_in:
            be_fix = st.number_input("Fixní náklady za měsíc (Kč):", value=20000, step=1000)
            be_cena = st.number_input("Prodejní cena za 1 kus (Kč):", value=500, step=50)
            be_var = st.number_input("Variabilní náklad na 1 kus (Kč):", value=200, step=50)
        
        with col_out:
            prispevek = be_cena - be_var
            if prispevek <= 0:
                st.error("Chyba: Tvá cena nepokryje ani variabilní náklady! Vždy budeš ve ztrátě.")
            else:
                bod_zvratu = math.ceil(be_fix / prispevek)
                st.metric("Příspěvek na úhradu na kus", f"{prispevek} Kč")
                st.metric("Bod zvratu (musíš prodat)", f"{bod_zvratu} kusů")
                st.success(f"Až prodáš {bod_zvratu} kusů, jsi na nule. Každý další kus ti přinese čistý zisk {prispevek} Kč!")
        
        if prispevek > 0:
            try:
                import pandas as pd
                max_x = int(bod_zvratu * 2.2) if bod_zvratu > 0 else 100
                kroky = max(1, max_x // 50)
                
                df_graf = pd.DataFrame({
                    "Kusy": range(0, max_x, kroky)
                })
                df_graf["Tržby (Výnosy)"] = df_graf["Kusy"] * be_cena
                df_graf["Celkové náklady"] = be_fix + (df_graf["Kusy"] * be_var)
                df_graf["Fixní náklady"] = be_fix
                
                df_graf = df_graf.set_index("Kusy")
                
                st.markdown("##### Graf bodu zvratu")
                st.line_chart(df_graf, color=["#22c55e", "#ef4444", "#64748b"])
                st.caption("Zelená = Tržby, Červená = Celkové náklady, Šedá = Fixní náklady. Kde se zelená a červená protnou, tam je tvůj bod zvratu!")
            except ImportError:
                st.warning("Graf bodu zvratu vyžaduje knihovnu Pandas.")

    elif selected_section_3 == "3.5 Měření výkonu a rentabilita":
        st.markdown("### 3.5 Jak měřit výkon firmy (KPI) a rentabilita")
        st.write("Výkon nelze hodnotit jen podle toho, zda firma „něco vydělala“. Důležité je sledovat více ukazatelů (KPI), protože každý ukazuje jinou část reality.")
        
        st.markdown("""
        * 💰 **Ziskovost:** Zisková marže, rentabilita tržeb (zda firma vydělává).
        * 📉 **Náklady:** Variabilní náklady na kus (jak efektivně firma vyrábí).
        * 🧑‍🏭 **Produktivita:** Výkon na pracovníka, kusy za hodinu (jak dobře využívá práci).
        * 💧 **Likvidita:** Schopnost platit závazky (zda má firma dostatek peněz).
        * 🛡️ **Kvalita:** Počet reklamací, zmetkovitost (zda se výkon nedělá na úkor kvality).
        * 🚀 **Růst:** Růst tržeb, počet opakovaných nákupů (zda se firmě daří rozvíjet).
        """)
        
        st.markdown("<div class='box-green'>🎯 <b>Pravidlo KPI:</b> Dobré KPI má pomáhat rozhodování. Pokud ukazatel nikdo nepoužívá k rozhodnutí, je to spíš číslo do tabulky než nástroj řízení.</div>", unsafe_allow_html=True)
        
        st.divider()
        st.markdown("#### Rentabilita")
        st.write("Rentabilita ukazuje, jak výnosně firma využívá své náklady, tržby nebo kapitál (vyjadřuje se v %). Čím vyšší rentabilita, tím lépe firma dokáže z vložených prostředků vytvářet zisk.")
        
        st.markdown("""
        * **Rentabilita nákladů** = Zisk / Náklady × 100
        * **Rentabilita tržeb** = Zisk / Tržby × 100
        * **Rentabilita kapitálu** = Zisk / Vložený kapitál × 100
        """)

        st.divider()
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
                st.warning("Rentabilita je velmi nízká. I malý výkyv na trhu pošle firmu do ztráty.")
            else:
                st.success("Firma je zdravě zisková!")
