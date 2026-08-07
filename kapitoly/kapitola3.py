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
        "4.1 Oběžný majetek a plánování zásob",
        "4.2 Oceňování a moderní řízení zásob",
        "4.3 Výpočty k oběžnému majetku",
        "4.4 Dlouhodobý majetek a investice",
        "4.5 Odpisy a evidence majetku",
        "5.1 Cenové strategie v praxi",
        "5.2 Náklady v digitálním světě a Asset-Light",
        "6.1 Štíhlá výroba, Poka-Yoke a 5S",
        "6.2 Průmysl 4.0, Cirkulární ekonomika a KPI",
        "6.3 Projektová dílna: Launch vlastního merche",
        "7.1 Případové studie z praxe",
        "7.2 Závěrečný checklist a prověrka kapitoly"
    ]
    
    selected_section_3 = st.selectbox("📌 Přechod na podkapitolu:", section_options_3, index=0)
    st.divider()

# =========================================================================
    # SEKCE 1: VÝROBNÍ PROCES A ORGANIZACE VÝROBY
    # =========================================================================
    if selected_section_3 == "1.1 Výrobní proces a faktory":
        st.markdown("### 1.1 Výrobní proces a výrobní faktory")
        
        st.markdown("""
        <div class='box-blue'>
            🏭 <b>Podstata výroby:</b> Výroba je transformační proces, při kterém firma mění vstupy na výstupy. Zjednodušeně platí: vstupy → technologie → výstupy.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("#### Výrobní proces")
        st.write("Výrobní proces zahrnuje všechny činnosti, které vedou ke vzniku výrobku nebo služby. Firma do procesu vkládá zdroje, používá určitou technologii a výsledkem je produkt, který má hodnotu pro zákazníka.")
        st.info("📦 **Vstupy** (materiál, práce, stroje, energie, informace, know-how) → ⚙️ **Technologie a práce** → 🎁 **Výstupy** (hotové výrobky, služby, polotovary).")
        
        st.divider()
        st.markdown("#### Výrobní faktory")
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

    elif selected_section_3 == "1.2 Typy výroby":
        st.markdown("### 1.2 Typy výroby")
        st.write("Výrobu lze rozdělit podle toho, kolik kusů firma vyrábí a jak moc se jednotlivé výrobky liší. Typ výroby ovlivňuje cenu, organizaci práce, potřebu zásob, nároky na stroje i způsob kontroly kvality.")

        st.markdown("""
        | Typ výroby | Charakteristika | Příklad z praxe |
        | :--- | :--- | :--- |
        | 🎨 **Kusová výroba** | Vyrábí se jednotlivé kusy podle konkrétní zakázky. | Nábytek na míru, svatební šaty, prototyp. |
        | 📦 **Sériová výroba** | Vyrábí se menší nebo větší série stejných výrobků. | Limitovaná edice mikin, školní diáře, komponenty. |
        | 🏭 **Hromadná výroba** | Vyrábí se velké množství stejných výrobků. | Nápoje, pečivo, šroubky, běžná elektronika. |
        """)

        st.divider()
        st.markdown("<div class='box-yellow'>🧩 <b>Kvíz: O jaký typ výroby jde?</b></div>", unsafe_allow_html=True)
        
        with st.form("kviz_vyroba"):
            q1 = st.selectbox("Nábytek vyrobený přesně podle rozměrů zákazníka:", ["Vyber možnost...", "Kusová", "Sériová", "Hromadná"])
            q2 = st.selectbox("300 stejných školních mikin:", ["Vyber možnost...", "Kusová", "Sériová", "Hromadná"])
            q3 = st.selectbox("Tisíce rohlíků každý den:", ["Vyber možnost...", "Kusová", "Sériová", "Hromadná"])
            
            if st.form_submit_button("Zkontrolovat odpovědi"):
                if q1 == "Kusová" and q2 == "Sériová" and q3 == "Hromadná":
                    st.success("✅ Perfektní! Chápeš to naprosto přesně.")
                else:
                    st.error("Něco tam ještě nesedí. Zkus to znovu! Nápověda: rohlíky se pečou ve velkém, nábytek na míru je unikát.")

    elif selected_section_3 == "1.3 Výrobní kapacita":
        st.markdown("### 1.3 Výrobní kapacita")
        st.write("Výrobní kapacita vyjadřuje maximální možný objem produkce za určité období. Může jít například o počet kusů za hodinu, směnu, den nebo měsíc.")
        
        st.markdown("<div class='box-blue'><b>Výrobní kapacita = maximální možný objem výroby za jednotku času</b></div>", unsafe_allow_html=True)
        
        st.write("Firma se obvykle nesnaží kapacitu využívat za každou cenu na 100 %. Příliš vysoké vytížení může vést k přetížení pracovníků, poruchám, zmetkům nebo zpoždění zakázek. Cílem je optimální využití, které ponechává rezervu na údržbu.")

        st.divider()
        st.markdown("<div class='box-yellow'>🧮 <b>Interaktivní model: Tisková farma na 3D klíčenky</b></div>", unsafe_allow_html=True)
        
        st.write("Představ si, že máš 5 3D tiskáren. Každá zvládne vytisknout maximálně 10 klíčenek za den. Tvá absolutní denní kapacita je tedy **50 klíčenek**.")
        st.write("Otevřeš svůj e-shop. Kolik objednávek na dnešek zákazníkům slíbíš dodat?")
        
        zakazky = st.slider("Počet slíbených zakázek na dnešek (kusů):", min_value=0, max_value=60, value=40)
        
        vyuziti = (zakazky / 50) * 100
        
        st.metric("Vytížení tvých tiskáren", f"{vyuziti:.0f} %")
        
        progress_val = min(vyuziti / 100, 1.0)
        st.progress(progress_val)
        
        if vyuziti > 100:
            st.error("💥 KRITICKÁ CHYBA: Slíbil jsi víc, než tvé stroje fyzicky zvládnou! Zákazníci nedostanou zboží včas, dostaneš špatné recenze.")
        elif vyuziti == 100:
            st.warning("⚠️ RIZIKO: Jedeš na absolutní doraz. Pokud se u jediné tiskárny zasekne struna, nestihneš dodat slíbené kusy!")
        elif vyuziti >= 80:
            st.success("✅ IDEÁLNÍ STAV: Vyděláváš skvělé peníze, ale máš malou rezervu, kdyby se něco pokazilo.")
        elif vyuziti > 0:
            st.info("📉 NEEFEKTIVNÍ: Tiskárny stojí a nevydělávají, i když by mohly. Platíš fixní náklady, ale máš málo zakázek.")
        else:
            st.write("Zatím nemáš žádné objednávky. Stroje leží ladem.")

    elif selected_section_3 == "1.4 Logistika, zásobování a JIT":
        st.markdown("### 1.4 Logistika, zásobování a Just-in-Time")
        st.write("Logistika řeší tok materiálu, výrobků, informací a peněz. Zásobování zajišťuje, aby firma měla správný materiál ve správném množství, kvalitě, čase a za přijatelnou cenu.")
        
        st.markdown("#### Metoda Just-in-Time (JIT)")
        st.write("Znamená, že materiál přichází do výroby co nejpozději — ideálně právě ve chvíli, kdy je potřeba. Cílem je minimalizovat skladové zásoby.")
        
        col_pro, col_con = st.columns(2)
        with col_pro:
            st.markdown("<div class='box-green'>✅ <b>Výhoda Just-in-Time:</b> Firma neváže tolik peněz ve skladu a šetří místo.</div>", unsafe_allow_html=True)
        with col_con:
            st.markdown("<div class='box-red'>⚠️ <b>Riziko Just-in-Time:</b> Pokud se dodávka zpozdí, výroba se může rychle zastavit.</div>", unsafe_allow_html=True)

        st.divider()
        st.markdown("<div class='box-yellow'>⚖️ <b>Rozhodnutí: Just-in-Time, nebo pojistná zásoba?</b></div>", unsafe_allow_html=True)
        
        st.write("Jsi manažerem automobilky. Dodávky kritických čipů z Asie jsou nespolehlivé. Běžné šroubky máš ze železářství vedle závodu. Jaký systém zásobování zvolíš pro celou firmu?")
        
        rozhodnuti = st.radio("Vyber strategii:", ["Vyber...", "Vše přes Just-in-Time", "Vše držet jako Pojistnou zásobu", "Kombinace obojího"])
        zdovodneni = st.text_input("Tvé zdůvodnění:")
        
        if st.button("Vyhodnotit rozhodnutí"):
            if rozhodnuti == "Kombinace obojího" and len(zdovodneni) > 2:
                st.success("Výborně! Kombinace je nejlepší. Šroubky lze brát JIT, ale u kritických čipů potřebuješ pojistnou zásobu.")
            elif rozhodnuti != "Vyber...":
                st.error("Toto by v praxi pravděpodobně selhalo. Extrémy nesvědčí. Zvaž riziko zastavení linky vs. vázání peněz.")

    # =========================================================================
    # SEKCE 2: ŘÍZENÍ JAKOSTI
    # =========================================================================
    elif selected_section_3 == "2.1 Řízení jakosti a kvality":
        st.markdown("### 2.1 Řízení jakosti: kvalita ve výrobě")
        st.markdown("""
        <div class='box-blue'>
            ✅ <b>Jakost neboli kvalita</b> znamená schopnost výrobku nebo služby splnit požadavky a očekávání zákazníka.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### Kontrola kvality vs. řízení jakosti")
        st.write("Kontrola kvality se často zaměřuje na odhalení chyb na konci výroby. Řízení jakosti jde dál: snaží se nastavit celý proces tak, aby chyby pokud možno vůbec nevznikaly.")

        st.markdown("""
        | Přístup | Co řeší | Příklad z praxe |
        | :--- | :--- | :--- |
        | 🔍 **Kontrola kvality** | Hledá chyby u hotového výrobku. | Vyřazení zmetků po dokončení výroby. |
        | 🛡️ **Řízení jakosti** | Předchází chybám během procesu. | Standardy práce, školení, Poka-Yoke, průběžné měření. |
        """)

        st.divider()
        st.markdown("<div class='box-yellow'>🔍 <b>Kvíz: Jde o kontrolu, nebo prevenci?</b></div>", unsafe_allow_html=True)
        
        with st.form("kviz_kvalita"):
            k1 = st.radio("Vyřazení vadných výrobků po dokončení:", ["Kontrola kvality", "Prevence (Řízení jakosti)"], horizontal=True)
            k2 = st.radio("Školení pracovníků před výrobou:", ["Kontrola kvality", "Prevence (Řízení jakosti)"], horizontal=True)
            k3 = st.radio("Poka-Yoke (nástroj/pomůcka znemožňující chybu):", ["Kontrola kvality", "Prevence (Řízení jakosti)"], horizontal=True)
            k4 = st.radio("Měření hotového výrobku před odesláním:", ["Kontrola kvality", "Prevence (Řízení jakosti)"], horizontal=True)
            
            if st.form_submit_button("Zkontrolovat"):
                if k1 == "Kontrola kvality" and k2 == "Prevence (Řízení jakosti)" and k3 == "Prevence (Řízení jakosti)" and k4 == "Kontrola kvality":
                    st.success("✅ Výborně! Kontrola řeší problém až když vznikne (hotový výrobek). Prevence mu předchází.")
                else:
                    st.error("Něco je špatně. Pamatuj: Pokud se něco děje až s HOTOVÝM výrobkem, je to vždy kontrola.")

    elif selected_section_3 == "2.2 Následky nekvality a TQM":
        st.markdown("### 2.2 Normy, TQM a následky nekvality")
        
        st.markdown("#### Normy a certifikace")
        st.write("Ve firmách se často používají normy a certifikace, které pomáhají nastavit jednotný systém řízení kvality (např. normy ISO řady 9000).")
        st.markdown("""
        <div class='box-gray'>
            📜 <b>Smysl certifikace:</b> Neznamená automaticky dokonalý výrobek. Znamená, že firma má popsaný a kontrolovaný systém, jak kvalitu řídit a zlepšovat.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("#### Total Quality Management (TQM)")
        st.write("Total Quality Management (TQM) je přístup, ve kterém se na kvalitě podílí celá firma — nejen kontrolor na konci výroby. Do zlepšování se zapojují pracovníci výroby, vedení, obchod, nákup i zákaznická podpora.")
        st.write("**TQM zdůrazňuje:**")
        st.markdown("""
        * Prevenci chyb,
        * Zapojení zaměstnanců,
        * Průběžné zlepšování,
        * Práci s daty,
        * Orientaci na zákazníka.
        """)

        st.divider()
        st.markdown("#### Následky nekvality")
        st.write("Nekvalita není jen technický problém. Má přímé ekonomické dopady. Může způsobit: reklamace, vrácení zboží, dodatečné opravy, vyšší náklady, zpoždění zakázek, ztrátu zákazníků a poškození dobrého jména firmy (goodwill).")

        st.markdown("""
        <div class='box-red'>
            ⚠️ <b>Ekonomická pointa:</b> Nekvalitní výrobek může být dražší než poctivá prevence. Firma zaplatí materiál, práci i opravy — a navíc může přijít o důvěru zákazníka.
        </div>
        """, unsafe_allow_html=True)

        st.divider()
        st.markdown("<div class='box-yellow'>🧮 <b>Kalkulačka nákladů na zmetky</b></div>", unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            vyrobeno_ks = st.number_input("Celkový počet vyrobených kusů:", min_value=1, value=1000, step=100)
            chybovost_pct = st.slider("Chybovost výroby (%)", min_value=0.0, max_value=20.0, value=3.0, step=0.5)
            naklad_ks = st.number_input("Náklad na výrobu 1 kusu (Kč):", min_value=1, value=500, step=50)
            
        vadne_ks = int(vyrobeno_ks * (chybovost_pct / 100))
        ztrata_kc = vadne_ks * naklad_ks
        
        with c2:
            st.metric("Počet vadných kusů (zmetků)", f"{vadne_ks} ks")
            st.metric("Finanční ztráta z výroby zmetků", f"{ztrata_kc:,} Kč".replace(",", " "))
            
            if ztrata_kc > 0:
                st.info(f"O tuto částku ({ztrata_kc:,} Kč) firma přišla kvůli špatné kvalitě. Prevence by byla pravděpodobně levnější.")
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
            st.write("V běžné řeči se často zaměňují, ale v ekonomice a účetnictví mají odlišný význam.")
            st.markdown("""
            * **Náklad:** Spotřeba zdrojů vyjádřená v penězích (např. spotřeba materiálu ve výrobě, mzda, odpis stroje).
            * **Výdaj:** Skutečný odtok peněz z pokladny nebo bankovního účtu (např. zaplacení faktury, nákup materiálu).
            """)
            st.markdown("<div class='box-gray'>💡 <b>Příklad:</b> Firma koupí stroj za 240 000 Kč. Peníze odejdou z účtu hned — to je výdaj. Do nákladů se ale stroj dostává postupně pomocí odpisů.</div>", unsafe_allow_html=True)
            
        with col2:
            st.markdown("#### Výnos vs. Příjem")
            st.write("Podobně je potřeba rozlišovat výnos a příjem.")
            st.markdown("""
            * **Výnos:** Peněžně vyjádřený výkon firmy, vznik nároku na zaplacení (např. vystavená faktura).
            * **Příjem:** Skutečný přítok peněz do pokladny nebo na účet (např. zákazník fakturu opravdu zaplatí).
            """)
            st.markdown("<div class='box-gray'>🧾 <b>Důležité:</b> Firma může mít výnos už při vystavení faktury, ale příjem vznikne až ve chvíli, kdy zákazník zaplatí.</div>", unsafe_allow_html=True)

        st.divider()
        st.markdown("#### Tři pohledy na zisk")
        st.markdown("**1. Účetní pohled na zisk**")
        st.write("Z účetního pohledu se zisk počítá jako rozdíl mezi účetními výnosy a účetními náklady za určité období. Vychází z pravidel účetnictví a zachycuje tržby, mzdy, nájem, energie, odpisy. Odpovídá na otázku: *Kolik firma podle účetnictví vydělala?*")
        
        st.markdown("**2. Pohled finanční analýzy a řízení**")
        st.write("Finanční řízení nesleduje jen " + "papírový" + " zisk, ale řeší, zda má firma hotovost, není předlužená a zisk se promítá do peněžních toků. Firma může vykázat zisk, ale zkrachovat na tom, že jí zákazníci neplatí včas (nemá hotovost).")
        
        st.markdown("**3. Ekonomický zisk**")
        st.write("Ekonomický zisk jde dál než účetní zisk. Zohledňuje nejen skutečně zaplacené (explicitní) náklady, ale také tzv. implicitní (alternativní) náklady — tedy hodnotu nejlepší nevyužité příležitosti.")
        st.markdown("<div class='box-green'>🧠 <b>Příklad:</b> Pokud podnikatel vloží do podnikání vlastní peníze, mohl je místo toho investovat jinam. Ušlý výnos je alternativní náklad.</div>", unsafe_allow_html=True)

        st.divider()
        st.markdown("<div class='box-yellow'>🧮 <b>Kalkulačka: Účetní vs. Ekonomický zisk</b></div>", unsafe_allow_html=True)
        st.write("Spočítej si, jestli se ti podnikání vyplatí víc, než kdybys šel do zaměstnání a peníze dal do banky.")
        
        c_in, c_out = st.columns([1, 1])
        with c_in:
            vynosy = st.number_input("Celkové roční výnosy (tržby):", value=1500000, step=100000)
            exp_naklady = st.number_input("Explicitní náklady (materiál, nájem atd.):", value=900000, step=50000)
            st.markdown("*Alternativní (implicitní) náklady:*")
            usla_mzda = st.number_input("Ušlá čistá mzda (kdybys pracoval pro jiného):", value=480000, step=20000)
            usly_urok = st.number_input("Ušlý úrok (kdybys peníze investoval jinam):", value=50000, step=10000)
            
        with c_out:
            ucetni_zisk = vynosy - exp_naklady
            eko_zisk = ucetni_zisk - usla_mzda - usly_urok
            
            st.metric("Účetní zisk (Papírový zisk)", f"{ucetni_zisk:,} Kč".replace(",", " "))
            st.metric("Ekonomický zisk", f"{eko_zisk:,} Kč".replace(",", " "))
            
            if eko_zisk > 0:
                st.success("✅ Podnikání se ti vyplatí! Vyděláváš víc, než kdybys chodil do práce a peníze měl v bance.")
            else:
                st.error("⚠️ Ekonomická ztráta! Z účetního pohledu jsi možná v plusu, ale ve skutečnosti by se ti víc vyplatilo jít do běžného zaměstnání.")

    elif selected_section_3 == "3.2 Členění nákladů a kalkulační vzorec":
        st.markdown("### 3.2 Členění nákladů a kalkulační vzorec")
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("#### Fixní a variabilní náklady")
            st.write("Dělení podle toho, zda se mění s objemem výroby.")
            st.markdown("""
            * 🔒 **Fixní náklady:** Nemění se přímo s počtem vyrobených kusů (nájem, pojištění, mzda administrativy, odpis stroje).
            * 📈 **Variabilní náklady:** Rostou nebo klesají podle objemu výroby (materiál, obaly, přímé mzdy, energie na výrobu).
            """)
            with st.expander("🛠️ Jak snižovat variabilní náklady?"):
                st.write("Vyjednat lepší cenu materiálu, najít vhodnější dodavatele, snížit zmetkovitost, omezit plýtvání materiálem, zkrátit čas potřebný na výrobu jednoho kusu, využívat množstevní slevy.")
            with st.expander("🛠️ Jak snižovat fixní náklady?"):
                st.write("Přestěhovat se do levnějších prostor, sdílet kanceláře/sklady, pronajímat stroje místo nákupu, automatizovat administrativu, outsourcovat činnosti.")
        
        with c2:
            st.markdown("#### Přímé a nepřímé náklady")
            st.write("Dělení pro přiřazení ceny ke konkrétnímu výrobku.")
            st.markdown("""
            * 🎯 **Přímé náklady:** Lze je přesně určit na jeden kus, zakázku nebo službu (materiál na jedno tričko, potisk, přímá mzda).
            * 🌫️ **Nepřímé náklady:** Jsou společné pro více výrobků nebo celou firmu a musí se rozpočítat (nájem dílny, účetnictví, marketing).
            """)
            st.info("Režijní přirážka = režijní náklady / zvolená rozvrhová základna × 100")
        
        st.divider()
        st.markdown("#### Kalkulační vzorec")
        st.write("Kalkulační vzorec pomáhá firmě sestavit cenu tak, aby pokryla náklady a umožnila zisk. Vyzkoušej si sestavit cenu vlastního produktu.")
        
        st.markdown("<div class='box-yellow'>🧮 <b>Interaktivní sestavení prodejní ceny</b></div>", unsafe_allow_html=True)
        
        k_in, k_out = st.columns([1, 1])
        with k_in:
            mat = st.number_input("Přímý materiál (Kč):", value=150, step=10)
            mzdy = st.number_input("Přímé mzdy (Kč):", value=100, step=10)
            v_rezie = st.number_input("Výrobní režie (Kč):", value=50, step=10)
            s_rezie = st.number_input("Správní režie (Kč):", value=30, step=10)
            o_naklady = st.number_input("Odbytové náklady (marketing, prodej) (Kč):", value=20, step=10)
            zisk_prirazka = st.slider("Zisková přirážka (%)", min_value=0, max_value=100, value=20)
            
        with k_out:
            vn_vyroby = mat + mzdy + v_rezie
            vn_vykonu = vn_vyroby + s_rezie
            uplne_vn = vn_vykonu + o_naklady
            zisk_kc = uplne_vn * (zisk_prirazka / 100)
            cena_bez_dph = uplne_vn + zisk_kc
            
            st.markdown(f"**Vlastní náklady výroby:** {vn_vyroby} Kč")
            st.markdown(f"**Vlastní náklady výkonu:** {vn_vykonu} Kč")
            st.markdown(f"**Úplné vlastní náklady:** {uplne_vn} Kč")
            st.markdown(f"**Zisk ({zisk_prirazka} %):** + {zisk_kc:.1f} Kč")
            st.markdown(f"<h3 style='color: #4f46e5; margin-top: 10px;'>Prodejní cena bez DPH: {cena_bez_dph:.1f} Kč</h3>", unsafe_allow_html=True)

    elif selected_section_3 == "3.3 Kalkulace nákladů":
        st.markdown("### 3.3 Kalkulace nákladů")
        st.write("Kalkulace je postup, kterým firma zjišťuje, kolik ji stojí jeden výrobek, služba nebo zakázka. Pomáhá odpovědět na otázky: *Kolik stojí výroba kusu? Za jakou cenu prodávat? Vyplatí se zakázka?*")
        
        st.markdown("#### Kalkulace úplných nákladů")
        st.write("Zahrnuje všechny náklady, které s výrobkem nebo službou souvisejí — přímé i nepřímé.")
        st.markdown("<div class='box-gray'><b>Úplné vlastní náklady = přímé náklady + podíl nepřímých nákladů</b></div>", unsafe_allow_html=True)
        st.markdown("""
        <div class='box-blue'>
            📊 <b>Výhoda:</b> Ukazuje celkové náklady výrobku.<br>
            ⚠️ <b>Nevýhoda:</b> Rozpočítání nepřímých nákladů může být nepřesné a závisí na zvolené metodě (např. zda se rozpočítává podle hodin nebo podle spotřebovaného materiálu).
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### Kalkulace neúplných nákladů (Krycí příspěvek)")
        st.write("Pracuje jen s částí nákladů — často s variabilními náklady. Fixní náklady se neposuzují na každý kus zvlášť, ale sledují se za firmu jako celek. Zde se používá klíčový manažerský pojem **příspěvek na úhradu** (tzv. krycí příspěvek). V reálném byznysu se tento výpočet používá denně k rychlému rozhodování.")
        st.markdown("<div class='box-gray'><b>Příspěvek na úhradu na kus = prodejní cena za kus − variabilní náklady na kus</b></div>", unsafe_allow_html=True)
        st.write("Příspěvek na úhradu říká, kolik z ceny jednoho prodaného kusu zbývá na úhradu fixních nákladů (např. nájmu) a tvorbu zisku.")

        st.divider()
        st.markdown("<div class='box-yellow'>🧮 <b>Kalkulačka příspěvku na úhradu</b></div>", unsafe_allow_html=True)
        
        col_in, col_out = st.columns(2)
        with col_in:
            cena_ks = st.number_input("Prodejní cena za 1 kus (Kč):", value=800)
            var_ks = st.number_input("Variabilní náklady na 1 kus (Kč):", value=350)
            prodano_ks = st.number_input("Očekávaný prodej (ks):", value=500)
        
        with col_out:
            prispevek_ks = cena_ks - var_ks
            prispevek_celkem = prispevek_ks * prodano_ks
            
            st.metric("Příspěvek na úhradu (1 kus)", f"{prispevek_ks} Kč")
            st.metric("Celkový příspěvek na úhradu", f"{prispevek_celkem:,} Kč".replace(",", " "))
            st.info(f"Z této částky {prispevek_celkem:,} Kč musí firma nejprve zaplatit všechny své fixní náklady (nájem, energie). Cokoliv zbyde, je čistý zisk.")

    elif selected_section_3 == "3.4 Bod zvratu a jeho graf":
        st.markdown("### 3.4 Bod zvratu a postup sestavení kalkulace")
        
        st.markdown("#### Bod zvratu (Break-even point)")
        st.write("Bod zvratu je objem výroby nebo prodeje, při kterém firma nemá ani zisk, ani ztrátu. Výnosy se právě rovnají nákladům.")
        st.markdown("<div class='box-gray'><b>Bod zvratu v kusech = Fixní náklady / (Cena za kus − Variabilní náklady na kus)</b></div>", unsafe_allow_html=True)
        
        st.divider()
        st.markdown("<div class='box-purple'>🕹️ <b>Simulátor Bodu Zvratu s Křivkou zisku</b></div>", unsafe_allow_html=True)
        
        col_in, col_out = st.columns([1, 1.2])
        with col_in:
            be_fix = st.number_input("Fixní náklady za období (Kč):", value=30000, step=1000)
            be_cena = st.number_input("Prodejní cena kusu (Kč):", value=1000, step=100)
            be_var = st.number_input("Variabilní náklad kusu (Kč):", value=400, step=100)
        
        with col_out:
            prispevek = be_cena - be_var
            if prispevek <= 0:
                st.error("Chyba: Tvá cena nepokryje variabilní náklady. Bod zvratu neexistuje.")
            else:
                bod_zvratu = math.ceil(be_fix / prispevek)
                st.metric("Bod zvratu (musíš prodat)", f"{bod_zvratu} kusů")
                st.success(f"Při prodeji {bod_zvratu} kusů jsi na nule. Každý další kus = čistý zisk {prispevek} Kč.")
        
        if prispevek > 0:
            try:
                import pandas as pd
                max_x = int(bod_zvratu * 2.5) if bod_zvratu > 0 else 100
                kroky = max(1, max_x // 50)
                df_graf = pd.DataFrame({"Kusy": range(0, max_x, kroky)})
                
                # Výpočty pro graf
                df_graf["Tržby (Výnosy)"] = df_graf["Kusy"] * be_cena
                df_graf["Celkové náklady"] = be_fix + (df_graf["Kusy"] * be_var)
                df_graf["Fixní náklady"] = be_fix
                # Přidaná křivka zisku/ztráty
                df_graf["Zisk / Ztráta"] = df_graf["Tržby (Výnosy)"] - df_graf["Celkové náklady"]
                
                df_graf = df_graf.set_index("Kusy")
                
                # Barvy: Zelená (Tržby), Červená (Náklady), Šedá (Fix. nák.), Fialová (Zisk)
                st.line_chart(df_graf, color=["#22c55e", "#ef4444", "#64748b", "#8b5cf6"])
                st.caption("📈 <b>Zelená</b> = Tržby | <b>Červená</b> = Celkové náklady | <b>Fialová</b> = Zisk / Ztráta. <br>Všimni si, jak fialová křivka začíná v minusu (ztráta) a přesně v bodě zvratu protíná nulu a roste do zisku!", unsafe_allow_html=True)
            except ImportError:
                st.warning("Graf vyžaduje knihovnu Pandas.")

        st.divider()
        st.markdown("#### Postup sestavení kalkulace")
        st.write("Při sestavování kalkulace je důležité postupovat systematicky:")
        st.markdown("""
        1. **Určit předmět kalkulace:** Co počítáme? Jeden výrobek, zakázku, projekt?
        2. **Vymezit období nebo objem:** Počítáme náklady na kus, měsíc nebo konkrétní zakázku?
        3. **Sepsat přímé náklady:** Materiál, přímé mzdy, obaly, doprava ke konkrétní zakázce.
        4. **Určit nepřímé náklady:** Nájem, energie, administrativa, odpisy, marketing.
        5. **Zvolit způsob rozvržení nepřímých nákladů:** Podle počtu kusů, hodin práce nebo strojových hodin.
        6. **Spočítat náklady na jednotku:** Celkové náklady se převedou na jeden výrobek.
        7. **Porovnat náklady s cenou:** Zjistit, zda cena pokryje náklady a umožní zisk.
        8. **Vyhodnotit výsledek:** Pokud je zisk nízký/záporný, firma hledá možnosti úprav ceny, nákladů nebo procesu.
        """)

    elif selected_section_3 == "3.5 Měření výkonu a rentabilita":
        st.markdown("### 3.5 Jak měřit výkon firmy a rentabilita")
        st.write("Výkon firmy nelze hodnotit jen podle toho, zda „něco vydělala“. Důležité je sledovat více ukazatelů, protože každý ukazuje jinou část reality.")
        
        st.markdown("""
        | Oblast | Ukazatel (KPI) | Co říká |
        | :--- | :--- | :--- |
        | 💰 **Ziskovost** | Zisk, zisková marže, rentabilita tržeb | Zda firma vydělává. |
        | 📉 **Náklady** | Náklady na kus, podíl fixních nákladů | Jak efektivně firma vyrábí. |
        | 🧑‍🏭 **Produktivita** | Výkon na pracovníka, kusy za hodinu | Jak dobře firma využívá práci. |
        | 💧 **Likvidita** | Schopnost platit závazky | Zda má firma dostatek peněz. |
        | ⚖️ **Zadluženost** | Podíl cizích zdrojů | Jak moc je firma závislá na dluhu. |
        | 🛡️ **Kvalita** | Počet reklamací, zmetkovitost | Zda výkon není dosažen na úkor kvality. |
        | 🚀 **Růst** | Růst tržeb, opakované nákupy | Zda se firmě daří rozvíjet. |
        """)
        
        st.markdown("<div class='box-green'>🎯 <b>Pravidlo KPI:</b> Dobré KPI má pomáhat rozhodování. Pokud ukazatel nikdo nepoužívá k rozhodnutí, je to spíš číslo do tabulky než skutečný nástroj řízení.</div>", unsafe_allow_html=True)
        
        st.divider()
        st.markdown("#### Vybrané vzorce a Rentabilita")
        st.write("Rentabilita ukazuje, jak výnosně firma využívá své náklady, tržby nebo kapitál.")
        st.markdown("""
        * **Rentabilita nákladů** = Zisk / Náklady × 100
        * **Rentabilita tržeb (Zisková marže)** = Zisk / Tržby × 100
        * **Rentabilita kapitálu** = Zisk / Vložený kapitál × 100
        * **Produktivita práce** = Výstup (ks nebo tržby) / Počet pracovníků
        """)

        st.divider()
        st.markdown("<div class='box-yellow'>🧮 <b>Dashboard výkonu firmy (KPI kalkulačka)</b></div>", unsafe_allow_html=True)
        
        rc1, rc2 = st.columns(2)
        with rc1:
            k_trzby = st.number_input("Tržby celkem (Kč):", value=2000000, step=100000)
            k_naklady = st.number_input("Náklady celkem (Kč):", value=1600000, step=100000)
            k_pracovnici = st.number_input("Počet pracovníků:", value=5, min_value=1)
            k_kusy = st.number_input("Počet vyrobených kusů:", value=10000, step=1000)
            
        with rc2:
            k_zisk = k_trzby - k_naklady
            rent_trzeb = (k_zisk / k_trzby) * 100 if k_trzby > 0 else 0
            prod_ks = k_kusy / k_pracovnici
            naklad_na_kus = k_naklady / k_kusy if k_kusy > 0 else 0
            
            st.metric("Zisk firmy", f"{k_zisk:,} Kč".replace(",", " "))
            st.metric("Rentabilita tržeb (Marže)", f"{rent_trzeb:.1f} %")
            st.metric("Produktivita (ks na 1 pracovníka)", f"{prod_ks:,.0f} ks".replace(",", " "))
            st.metric("Náklad na 1 kus", f"{naklad_na_kus:,.1f} Kč".replace(",", " "))
            
            if rent_trzeb < 0:
                st.error("Firma je ve ztrátě. Hodnota rentability je záporná.")
            elif rent_trzeb < 10:
                st.warning("Pozor, rentabilita je nízká (pod 10 %).")
            else:
                st.success("Skvělá práce, rentabilita i výkonnost jsou zdravé.")
# =========================================================================
    # SEKCE 4: MAJETEK FIRMY
    # =========================================================================
    elif selected_section_3 == "4.1 Oběžný majetek a plánování zásob":
        st.markdown("### 4.1 Oběžný majetek a plánování zásob")
        
        st.markdown("""
        <div class='box-blue'>
            🏢 <b>Podstata majetku:</b> Majetek firmy představuje vše, co firma používá ke své činnosti. Část majetku se ve firmě rychle spotřebuje nebo přemění na peníze, jiná část slouží dlouhodobě. Dělí se na <b>oběžný</b> a <b>dlouhodobý</b> majetek.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("#### Oběžný majetek")
        st.write("Oběžný majetek je majetek, který se při činnosti firmy rychle mění. Typicky se spotřebuje, prodá, přemění na hotové výrobky nebo na peníze.")
        st.write("Patří sem například: zásoby materiálu, nedokončená výroba, hotové výrobky, zboží, krátkodobé pohledávky, peníze v hotovosti a na bankovním účtu.")
        st.markdown("<div class='box-gray'>🔄 <b>Koloběh:</b> Oběžný majetek „obíhá“ firmou: peníze se použijí na nákup materiálu, materiál se změní ve výrobek, výrobek se prodá a zpět do firmy se vrátí peníze.</div>", unsafe_allow_html=True)

        st.markdown("#### Plánování materiálu")
        st.write("Plánování materiálu znamená určit, kolik materiálu bude firma potřebovat, kdy ho má objednat a jak velkou zásobu má držet na skladě. Firma musí hlídat dvě rizika:")
        st.markdown("""
        * ❌ **Příliš nízká zásoba:** výroba se může zastavit, protože chybí materiál.
        * ❌ **Příliš vysoká zásoba:** firma má peníze zbytečně vázané ve skladu.
        """)
        st.write("Při plánování materiálu se sleduje: plánovaný objem výroby, spotřeba materiálu na jeden výrobek, dodací lhůta dodavatele, minimální zásoba, pojistná zásoba, skladovací náklady a riziko znehodnocení materiálu.")
        
        st.markdown("#### Stanovení optimální zásoby a druhy zásob")
        st.markdown("<div class='box-green'>⚖️ <b>Cíl optimální zásoby:</b> Najít rovnováhu mezi bezpečností výroby a náklady na skladování.</div>", unsafe_allow_html=True)
        st.markdown("""
        | Druh zásoby | Význam |
        | :--- | :--- |
        | 📦 **Běžná zásoba** | Slouží k pravidelné spotřebě mezi dvěma dodávkami. |
        | 🛡️ **Pojistná zásoba** | Chrání firmu před zpožděním dodávky nebo nečekanou spotřebou. |
        | 📉 **Minimální zásoba** | Nejnižší stav zásoby, pod který by firma neměla klesnout. |
        | 📈 **Maximální zásoba** | Nejvyšší stav zásoby, který ještě dává ekonomický smysl. |
        """)

        st.divider()
        st.markdown("<div class='box-yellow'>🧮 <b>Kalkulačka: Průměrná a Signální zásoba</b></div>", unsafe_allow_html=True)
        st.write("Vyzkoušej si výpočty. **Průměrná zásoba** = (počáteční zásoba + konečná zásoba) / 2. **Signální zásoba** určuje okamžik, kdy je vhodné materiál znovu objednat.")
        
        c_z1, c_z2 = st.columns(2)
        with c_z1:
            st.markdown("**Výpočet Průměrné zásoby**")
            pocatecni = st.number_input("Počáteční zásoba na začátku měsíce (ks):", value=100)
            konecna = st.number_input("Konečná zásoba na konci měsíce (ks):", value=50)
            prumerna = (pocatecni + konecna) / 2
            st.metric("Průměrná zásoba", f"{prumerna} ks")
            
        with c_z2:
            st.markdown("**Výpočet Signální zásoby**")
            denni_spotreba = st.number_input("Denní spotřeba materiálu (ks):", value=10)
            dodaci_lhuta = st.number_input("Dodací lhůta od dodavatele (dny):", value=3)
            pojistna = st.number_input("Pojistná zásoba (ks):", value=20)
            signalni = (denni_spotreba * dodaci_lhuta) + pojistna
            st.metric("Signální zásoba", f"{signalni} ks")
            st.info(f"Jakmile ti na skladě zbyde {signalni} ks, musíš ihned objednat další materiál.")

        st.divider()
        st.markdown("#### Pořízení materiálu, evidence a skladování")
        st.write("Pořízení materiálu zahrnuje tyto kroky: Zjištění potřeby → Výběr dodavatele → Objednávka → Dodání → Přejímka materiálu (kontrola kvality) → Uskladnění → Výdej do spotřeby.")
        st.write("Mezi běžné skladové doklady patří:")
        st.markdown("""
        * 📝 **Příjemka:** doklad o přijetí materiálu na sklad.
        * 📤 **Výdejka:** doklad o vydání materiálu ze skladu.
        * 🗂️ **Skladní karta:** přehled příjmů, výdejů a zůstatků materiálu.
        """)
        st.markdown("<div class='box-gray'>📦 Dobré skladování snižuje ztráty, záměny, poškození i zbytečné nákupy materiálu, který už firma ve skladu má.</div>", unsafe_allow_html=True)

    elif selected_section_3 == "4.2 Oceňování a moderní řízení zásob":
        st.markdown("### 4.2 Oceňování a moderní řízení zásob")
        
        st.write("Rozdíl: FIFO, LIFO a vážený průměr řeší hlavně **ocenění zásob při výdeji**. Moderní metody (Kanban, JIT) řeší spíš to, **kolik zásob držet, kdy objednávat a jak zabránit plýtvání**.")
        
        st.markdown("#### Vizuální systém KANBAN 🚥")
        st.write("Kanban pochází z japonštiny (znamená „cedulka“ nebo „vizuální signál“). Proslavila ho automobilka Toyota. Jde o systém, kdy si další krok výroby „táhne“ materiál až ve chvíli, kdy ho potřebuje.")
        
        st.markdown("<div class='box-green'><b>Princip dvou bedýnek (Dvoubinový systém)</b></div>", unsafe_allow_html=True)
        st.write("Představ si, že montuješ kola a máš před sebou dvě bedýnky se šroubky.")
        
        col_k1, col_k2, col_k3 = st.columns(3)
        with col_k1:
            st.info("📦 **Bedýnka 1 (Používám)**\n\nBeru z ní šroubky. Dokud v ní něco je, nic neřeším.")
        with col_k2:
            st.warning("🪹 **Bedýnka 1 se vyprázdní!**\n\nTo je **SIGNÁL (Kanban)**. Prázdnou bedýnku pošlu do skladu jako objednávku.")
        with col_k3:
            st.success("📦 **Bedýnka 2 (Záložní)**\n\nZačnu brát z druhé bedýnky. Než ji vyprázdním, sklad mi vrátí plnou Bedýnku 1.")
            
        st.markdown("💡 *Dnes se Kanban nepoužívá jen ve výrobě, ale i v IT a projektovém řízení (aplikace jako Trello nebo Jira), kde se místo bedýnek posouvají úkoly ve sloupcích (To Do → In Progress → Done).*")

        st.divider()
        st.markdown("#### Just-in-Time (JIT)")
        st.write("Materiál dorazí přesně tehdy, kdy je potřeba. Firma nemá téměř žádné sklady. V současnosti se ale po zkušenostech s výpadky dodavatelských řetězců (např. chybějící čipy) firmy snaží o rovnováhu a často kombinují JIT s bezpečnostní zásobou.")
        
        st.markdown("#### ABC analýza zásob")
        st.write("Rozděluje zásoby podle důležitosti a hodnoty, protože nemá smysl počítat každý šroubek se stejnou pečlivostí jako drahé motory.")
        st.markdown("""
        * 🥇 **Skupina A (cca 10 % položek, ale 70 % hodnoty):** Nejdražší položky. Hlídají se denně, zásoby jsou minimální (např. drahé čipy, motory).
        * 🥈 **Skupina B (cca 20 % položek, 20 % hodnoty):** Středně důležité. Kontrolují se pravidelně.
        * 🥉 **Skupina C (cca 70 % položek, ale jen 10 % hodnoty):** Levné drobnosti (šroubky, gumičky, kancelářský papír). Objednávají se ve velkém, zásoba se moc nehlídá.
        """)

    elif selected_section_3 == "4.3 Výpočty k oběžnému majetku":
        st.markdown("### 4.3 Rychlost a doba obratu zásob")
        st.write("Každá zásoba, která leží na skladě, jsou **„utopené“ peníze**, za které firma mohla koupit něco jiného nebo je úročit v bance. Proto manažery zajímá, jak rychle se zásoby točí.")
        
        st.markdown("""
        * 🔄 **Počet obrátek (Rychlost obratu):** Říká, kolikrát za rok se sklad kompletně vyprázdní a znovu naplní. Čím vyšší číslo, tím lépe!
        * ⏳ **Doba obratu (ve dnech):** Říká, kolik dní průměrně leží materiál na skladě, než z něj vyrobíme produkt a ten prodáme. Čím kratší doba, tím lépe!
        """)
        
        st.markdown("<div class='box-gray'><b>Počet obrátek</b> = Tržby (nebo spotřeba) / Průměrná zásoba<br><b>Doba obratu</b> = 360 dní / Počet obrátek</div>", unsafe_allow_html=True)

        st.divider()
        st.markdown("<div class='box-purple'>🕹️ <b>Simulátor: Proč na obratu záleží?</b></div>", unsafe_allow_html=True)
        st.write("Podívej se, jak snížení zásob na skladě radikálně zkrátí dobu, po kterou ti v nich leží peníze.")
        
        c_obr1, c_obr2 = st.columns([1, 1.2])
        with c_obr1:
            rocni_trzby = st.number_input("Roční tržby e-shopu (Kč):", value=3600000, step=100000)
            hodnota_skladu = st.slider("Průměrná hodnota zboží na skladě (Kč):", min_value=100000, max_value=2000000, value=600000, step=50000)
            
        with c_obr2:
            obratky = rocni_trzby / hodnota_skladu
            doba_obratu = 360 / obratky if obratky > 0 else 0
            
            st.metric("Počet obrátek za rok", f"{obratky:.1f}x")
            st.metric("Doba obratu (Zboží leží ve skladu)", f"{doba_obratu:.0f} dní")
            
            if doba_obratu > 90:
                st.error("📉 Zboží leží na skladě moc dlouho (více než 3 měsíce)! Zbytečně v něm vážeš peníze a riskuješ, že vyjde z módy nebo se zkazí.")
            elif doba_obratu < 30:
                st.success("✅ Skvělá práce! Sklad se točí rychle, peníze se ti vrací na účet a můžeš je znovu investovat.")
            else:
                st.info("⚖️ Standardní rychlost obratu. Dá se to ale ještě optimalizovat (např. Kanbanem).")

    elif selected_section_3 == "4.4 Dlouhodobý majetek a investice":
        st.markdown("### 4.4 Dlouhodobý majetek a plánování investic")
        
        st.write("Dlouhodobý majetek je majetek, který firma používá delší dobu (déle než rok). Nespotřebuje se najednou, ale postupně se opotřebovává.")
        
        st.markdown("#### Dělení dlouhodobého majetku")
        st.markdown("""
        | Druh majetku | Charakteristika | Příklad z praxe |
        | :--- | :--- | :--- |
        | 🏗️ **Dlouhodobý hmotný** | Má fyzickou podobu. | Budova, výrobní stroj, automobil. |
        | 💿 **Dlouhodobý nehmotný** | Nemá fyzickou podobu. | Software, licence, ochranná známka. |
        | 📈 **Dlouhodobý finanční** | Finanční investice držené delší dobu. | Podíly v jiných firmách, dlouhodobé cenné papíry. |
        """)

        st.divider()
        st.markdown("#### Plánování investic a Doba návratnosti")
        st.write("Pořízení dlouhodobého majetku je investice. Firma by měla předem zvažovat, proč majetek potřebuje a za jak dlouho se investice vrátí.")
        st.markdown("<div class='box-gray'><b>Doba návratnosti = Pořizovací cena / Roční čistý přínos investice</b></div>", unsafe_allow_html=True)
        
        c_i1, c_i2 = st.columns([1, 1])
        with c_i1:
            cena_stroje = st.number_input("Cena nového stroje vč. instalace (Kč):", value=500000, step=50000)
            rocni_uspora = st.number_input("Roční finanční přínos stroje (Kč):", value=125000, step=5000)
        with c_i2:
            if rocni_uspora > 0:
                navratnost = cena_stroje / rocni_uspora
                st.metric("Doba návratnosti", f"{navratnost:.1f} let")
                st.success("Pokud stroj fyzicky vydrží déle než vypočítaná doba návratnosti, investice má smysl.")
            else:
                st.error("Stroj nepřináší zisk.")

    elif selected_section_3 == "4.5 Odpisy a evidence majetku":
        st.markdown("### 4.5 Odpisy (Účetní vs. Daňové) a grafické srovnání")
        
        st.write("Dlouhodobý majetek (např. auto za 1 milion Kč) si firma nedá do nákladů celý najednou v roce nákupu. Náklady se rozloží do více let – tomu se říká **Odpis**.")
        
        st.markdown("#### Rozdíl mezi účetními a daňovými odpisy")
        st.markdown("""
        * 📘 **Účetní odpisy:** Mají zobrazovat SKUTEČNÉ opotřebení majetku. Firma si sama určí, jak dlouho bude majetek používat (např. notebook na 4 roky). Cílem je věrný obraz účetnictví.
        * 🏛️ **Daňové odpisy:** Jsou striktně dané státem (Zákonem o daních z příjmů). Snižují základ daně. Stát rozděluje majetek do **6 odpisových skupin**.
        """)

        st.divider()
        st.markdown("#### Přehled 6 odpisových skupin podle zákona")
        st.markdown("""
        | Skupina | Doba odpisování | Typický majetek (příklady) |
        | :---: | :---: | :--- |
        | **1.** | **3 roky** | Počítače, notebooky, kancelářské stroje, ruční nářadí, skot. |
        | **2.** | **5 let** | Osobní a užitková auta, motocykly, nábytek, většina strojů a přístrojů. |
        | **3.** | **10 let** | Těžké stroje, lokomotivy, turbíny, trezory, skleníky. |
        | **4.** | **20 let** | Budovy ze dřeva a plastů, oplocení, průmyslové plynovody. |
        | **5.** | **30 let** | Běžné budovy (cihlové, betonové), mosty, dálnice, tunely. |
        | **6.** | **50 let** | Administrativní budovy, hotely, domy kultury, historické památky. |
        """)

        st.divider()
        st.markdown("#### Vzorce pro výpočet daňových odpisů")
        
        c_v1, c_v2 = st.columns(2)
        with c_v1:
            st.markdown("<div class='box-blue'><b>Rovnoměrné odpisy (Lineární)</b><br>Počítají se pomocí státem daných procentuálních sazeb.</div>", unsafe_allow_html=True)
            st.markdown("""
            * **Odpis v 1. roce:**
            `Pořizovací cena × (Sazba pro 1. rok / 100)`
            * **Odpis v dalších letech:**
            `Pořizovací cena × (Sazba pro další roky / 100)`
            """)
            
        with c_v2:
            st.markdown("<div class='box-green'><b>Zrychlené odpisy (Degresivní)</b><br>Počítají se pomocí státem daných koeficientů.</div>", unsafe_allow_html=True)
            st.markdown("""
            * **Odpis v 1. roce:**
            `Pořizovací cena / Koeficient pro 1. rok`
            * **Odpis v dalších letech:**
            `(2 × Zůstatková cena) / (Koeficient pro další roky − počet let, po které se již odpisovalo)`
            """)

        st.divider()
        st.markdown("<div class='box-yellow'>🧮 <b>Interaktivní kalkulačka: Všech 6 odpisových skupin</b></div>", unsafe_allow_html=True)
        st.write("Vyber odpisovou skupinu a zadej cenu. Kalkulačka spočítá odpisy pro všech 6 zákonných skupin.")
        
        c_kalk1, c_kalk2 = st.columns([1, 1.2])
        with c_kalk1:
            odp_cena = st.number_input("Pořizovací cena majetku (Kč):", value=500000, step=50000, min_value=10000)
        with c_kalk2:
            skupiny = {
                "1. skupina (3 roky) - Počítače, nářadí": {"roky": 3, "rov_1": 20, "rov_dalsi": 40, "zrych_1": 3, "zrych_dalsi": 4},
                "2. skupina (5 let) - Auta, běžné stroje": {"roky": 5, "rov_1": 11, "rov_dalsi": 22.25, "zrych_1": 5, "zrych_dalsi": 6},
                "3. skupina (10 let) - Těžké stroje, turbíny": {"roky": 10, "rov_1": 5.5, "rov_dalsi": 10.5, "zrych_1": 10, "zrych_dalsi": 11},
                "4. skupina (20 let) - Dřevěné budovy, ploty": {"roky": 20, "rov_1": 2.15, "rov_dalsi": 5.15, "zrych_1": 20, "zrych_dalsi": 21},
                "5. skupina (30 let) - Cihlové/betonové budovy": {"roky": 30, "rov_1": 1.4, "rov_dalsi": 3.4, "zrych_1": 30, "zrych_dalsi": 31},
                "6. skupina (50 let) - Kancelářské budovy, hotely": {"roky": 50, "rov_1": 1.02, "rov_dalsi": 2.02, "zrych_1": 50, "zrych_dalsi": 51}
            }
            vybrana_skupina = st.selectbox("Vyber odpisovou skupinu:", list(skupiny.keys()), index=1)
            
        param = skupiny[vybrana_skupina]
        roky = param["roky"]

        # 1. Výpočet rovnoměrných odpisů
        rovnomerne = []
        for rok in range(1, roky + 1):
            if rok == 1:
                odpis = odp_cena * (param["rov_1"] / 100)
            else:
                odpis = odp_cena * (param["rov_dalsi"] / 100)
            rovnomerne.append(round(odpis))

        # 2. Výpočet zrychlených odpisů
        zrychlene = []
        zustatek_zrych = odp_cena
        for rok in range(1, roky + 1):
            if rok == 1:
                odpis = odp_cena / param["zrych_1"]
            else:
                odpis = (2 * zustatek_zrych) / (param["zrych_dalsi"] - (rok - 1))
            zustatek_zrych -= odpis
            zrychlene.append(round(odpis))

        try:
            import pandas as pd
            
            df_odpisy = pd.DataFrame({
                "Rok": [f"{r}. rok" for r in range(1, roky + 1)],
                "Rovnoměrný odpis (Kč)": rovnomerne,
                "Zrychlený odpis (Kč)": zrychlene
            })
            
            st.markdown("##### 📊 Výpočet odpisů rok po roce")
            st.dataframe(df_odpisy.style.format({"Rovnoměrný odpis (Kč)": "{:,.0f}", "Zrychlený odpis (Kč)": "{:,.0f}"}), use_container_width=True)
            
            st.markdown("##### 📈 Grafické srovnání nákladů")
            df_graf = df_odpisy.set_index("Rok")
            st.bar_chart(df_graf, color=["#3b82f6", "#22c55e"])
            st.caption("🟦 Modrá = Rovnoměrný odpis | 🟩 Zelená = Zrychlený odpis.")
            
        except ImportError:
            st.warning("Pro zobrazení tabulek a grafů je potřeba knihovna Pandas.")

        st.divider()
        st.markdown("#### Vyřazení a evidence dlouhodobého majetku")
        st.write("Dlouhodobý majetek se z evidence vyřazuje tehdy, když už ho firma nepoužívá. Důvody mohou být: prodej, likvidace, darování, škoda/zničení, krádež nebo převod do osobního užívání.")
        st.markdown("<div class='box-gray'>🗂️ <b>Evidence:</b> Dlouhodobý majetek se eviduje na <i>kartách majetku</i> (inventární číslo, název, pořizovací cena, odpisový plán, oprávky, odpovědná osoba).</div>", unsafe_allow_html=True)


# =========================================================================
    # SEKCE 5: KALKULACE, CENY A CENOVÉ STRATEGIE
    # =========================================================================
    elif selected_section_3 == "5.1 Cenové strategie v praxi":
        st.markdown("### 5.1 Cenové strategie v praxi")
        st.markdown("""
        <div class='box-blue'>
            🏷️ <b>Klíčová myšlenka:</b> Zákazník neplatí jen za výrobek. Platí také za značku, pohodlí, důvěru, rychlost a vnímanou hodnotu.
        </div>
        """, unsafe_allow_html=True)
        
        st.write("Cena není jen matematický výsledek kalkulace. Firma musí znát své náklady, ale zároveň přemýšlí o tom, jakou hodnotu zákazník v produktu vidí a kolik je ochoten zaplatit.")
        
        st.markdown("**Na cenu působí například:** Náklady na výrobu či službu, ceny konkurence, značka a důvěra, rychlost dodání, pohodlí, kvalita a design, vzácnost a ochota zákazníka zaplatit.")
        
        st.markdown("<div class='box-gray'>💬 <b>Otázka k zamyšlení:</b> Proč si někdo koupí mikinu za 1 200 Kč, i když její výroba stála 350 Kč? Často neplatí jen za látku a potisk, ale za značku, komunitu, styl a pocit, že k něčemu patří.</div>", unsafe_allow_html=True)
        
        st.divider()
        st.markdown("#### Moderní cenové strategie")
        
        tab_c1, tab_c2, tab_c3, tab_c4, tab_c5 = st.tabs([
            "🆓 Freemium", "📅 Předplatné", "📈 Dynamická cena", "📦 Balíčkování", "💎 Prémiová cena"
        ])
        
        with tab_c1:
            st.markdown("##### Freemium")
            st.write("**Jak funguje:** Základní verze je zdarma, pokročilé funkce nebo odstranění reklam jsou placené.")
            st.markdown("<div class='box-green'>🎮 <b>Příklady z praxe:</b> Spotify, Canva, Duolingo, mobilní hry.</div>", unsafe_allow_html=True)
        with tab_c2:
            st.markdown("##### Předplatné (Subscription)")
            st.write("**Jak funguje:** Zákazník neplatí jednorázově, ale pravidelně (měsíčně/ročně) za trvalý přístup.")
            st.markdown("<div class='box-green'>🎬 <b>Příklady z praxe:</b> Netflix, Adobe, posilovny, cloudová úložiště (iCloud, Google One).</div>", unsafe_allow_html=True)
        with tab_c3:
            st.markdown("##### Dynamická cena (Dynamic Pricing)")
            st.write("**Jak funguje:** Cena se mění v reálném čase podle poptávky, času, počasí nebo obsazenosti.")
            st.markdown("<div class='box-green'>✈️ <b>Příklady z praxe:</b> Letenky, hotely, Uber, lístky na koncerty a zápasy.</div>", unsafe_allow_html=True)
        with tab_c4:
            st.markdown("##### Balíčkování (Bundling)")
            st.write("**Jak funguje:** Více produktů či služeb se prodává společně za výhodnější cenu, než kdyby se kupovaly zvlášť.")
            st.markdown("<div class='box-green'>🍔 <b>Příklady z praxe:</b> Menu ve fast foodu, balíček aplikací Microsoft 365, výhodný výhodový set na e-shopu.</div>", unsafe_allow_html=True)
        with tab_c5:
            st.markdown("##### Prémiová cena (Skimming / Premium Pricing)")
            st.write("**Jak funguje:** Záměrně vysoká cena podporuje dojem luxusu, výjimečnosti a špičkové kvality.")
            st.markdown("<div class='box-green'>🏎️ <b>Příklady z praxe:</b> Apple, limitované edice oblečení, luxusní parfémové značky.</div>", unsafe_allow_html=True)
            
        st.divider()
        st.markdown("<div class='box-yellow'>🎲 <b>Mini-aplikace: Vyber ideální cenovou strategii</b></div>", unsafe_allow_html=True)
        
        prod_typ = st.selectbox("Vyber typ produktu / projektu:", [
            "Vyber...",
            "Mobilní aplikace na plánování tréninků",
            "Limitovaná edice 50 kusů designer mikin",
            "Taxi služba v pátek v noc po koncertě",
            "Set šamponu, kondicionéru a hřebenu"
        ])
        
        if prod_typ != "Vyber...":
            strat_volba = st.radio("Jaká strategie je pro tento produkt nejvhodnější?", [
                "Freemium", "Předplatné", "Dynamická cena", "Balíčkování", "Prémiová cena"
            ], horizontal=True)
            
            dovud = st.text_input("Zdůvodni, proč tato strategie dává ekonomický smysl:")
            
            if st.button("Vyhodnotit strategii"):
                sprat_map = {
                    "Mobilní aplikace na plánování tréninků": ["Freemium", "Předplatné"],
                    "Limitovaná edice 50 kusů designer mikin": ["Prémiová cena"],
                    "Taxi služba v pátek v noc po koncertě": ["Dynamická cena"],
                    "Set šamponu, kondicionéru a hřebenu": ["Balíčkování"]
                }
                if strat_volba in sprat_map.get(prod_typ, []):
                    st.success(f"✅ Výborně! Strategie '{strat_volba}' je pro tento případ ideální.")
                else:
                    st.warning(f"Zvážil/a jsi všechny aspekty? Pro tento typ produktu se častěji využívá {', '.join(sprat_map.get(prod_typ, []))}.")

    elif selected_section_3 == "5.2 Náklady v digitálním světě a Asset-Light":
        st.markdown("### 5.2 Náklady v digitálním světě a Asset-Light model")
        
        st.markdown("#### Nulové mezní náklady v digitálním světě")
        st.write("U fyzického produktu má každý další kus obvykle další náklady (tričko potřebuje látku, potisk, obal, práci a dopravu). U digitálního produktu je situace jiná.")
        st.markdown("<div class='box-purple'>🎮 <b>Aha moment:</b> Vývoj mobilní hry může stát 2 000 000 Kč. Jakmile je ale hra hotová, stažení 100 000. kopie už firmu téměř nic nestojí. Fixní náklady jsou obrovské, ale variabilní náklady na jednu další kopii se blíží nule.</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='box-gray'><b>Průměrné náklady na uživatele</b> = Celkové náklady / Počet uživatelů</div>", unsafe_allow_html=True)
        st.write("Čím více uživatelů digitální službu využívá, tím více se vysoké fixní vývojové náklady rozpočítají.")

        st.divider()
        st.markdown("<div class='box-yellow'>🧮 <b>Kalkulačka: Fyzický vs. Digitální produkt</b></div>", unsafe_allow_html=True)
        
        cd1, cd2 = st.columns(2)
        with cd1:
            st.markdown("##### 👕 Fyzický produkt (Kniha / Tričko)")
            f_fix = st.number_input("Fixní náklady (tiskové desky/grafika):", value=50000, step=10000, key="f_fix")
            f_var = st.number_input("Variabilní náklad na 1 kus (materiál):", value=150, step=10, key="f_var")
            f_kusy = st.slider("Počet vyrobených a prodaných kusů:", min_value=100, max_value=10000, value=1000, step=100, key="f_kusy")
            
            f_celk = f_fix + (f_var * f_kusy)
            f_prum = f_celk / f_kusy
            st.metric("Celkové náklady", f"{f_celk:,} Kč".replace(",", " "))
            st.metric("Průměrný náklad na 1 kus", f"{f_prum:.1f} Kč")
            
        with cd2:
            st.markdown("##### 📱 Digitální produkt (Aplikace / E-kniha)")
            d_fix = st.number_input("Fixní náklady (vývoj hry/aplikace):", value=300000, step=50000, key="d_fix")
            d_var = st.number_input("Variabilní náklad na 1 stažení (server):", value=2, step=1, key="d_var")
            d_kusy = st.slider("Počet stažení / uživatelů:", min_value=100, max_value=100000, value=10000, step=1000, key="d_kusy")
            
            d_celk = d_fix + (d_var * d_kusy)
            d_prum = d_celk / d_kusy
            st.metric("Celkové náklady", f"{d_celk:,} Kč".replace(",", " "))
            st.metric("Průměrný náklad na 1 uživatele", f"{d_prum:.1f} Kč")

        st.divider()
        st.markdown("#### Podnikání bez vlastního skladu a strojů (Asset-Light)")
        st.write("Některé moderní firmy se snaží vlastnit co nejméně majetku. Místo skladu, strojů a velkých zásob využívají dodavatele, platformy a outsourcing. Tomuto přístupu se říká **asset-light business**.")
        
        st.markdown("""
        * 📦 **Dropshipping:** E-shop prodá zboží, ale skladování, balení a odeslání řeší přímo dodavatel.
        * 🖨️ **Print-on-Demand (POD):** Tričko, mikina nebo plakát se vyrobí a potiskne až ve chvíli, kdy zákazník vytvoří objednávku. (Nulové neprodané zásoby!).
        * ☁️ **Cloudové služby:** Firma si nekupuje vlastní servery, ale pronajímá si výpočetní výkon (AWS, Azure).
        * 🏢 **Sdílené kanceláře (Coworking):** Firma nevlastní budovu, ale platí jen za stoly, které využívala.
        """)

        st.divider()
        st.markdown("<div class='box-yellow'>⚖️ <b>Rozhodovací simulátor: Sklad vs. Print-on-Demand vs. Dropshipping</b></div>", unsafe_allow_html=True)
        
        model_volba = st.selectbox("Vyber obchodní model pro svůj nový e-shop:", [
            "Vyber...",
            "Vlastní sklad a nákup zásob dopředu",
            "Print-on-Demand (výroba po objednávce)",
            "Dropshipping"
        ])
        
        if model_volba == "Vlastní sklad a nákup zásob dopředu":
            st.info("📊 **Vlastnosti:** Vyšší marže na kus, plná kontrola nad kvalitou a balením. **Riziko:** Vázaný kapitál a neprodané zásoby ležící na skladě.")
        elif model_volba == "Print-on-Demand (výroba po objednávce)":
            st.success("📊 **Vlastnosti:** Nulové riziko neprodaných zásob, nízký startovací kapitál. **Riziko:** Nižší marže z jednoho kusu, delší doba doručení zákazníkovi.")
        elif model_volba == "Dropshipping":
            st.success("📊 **Vlastnosti:** Nemusíš řešit logistiku ani sklad. **Riziko:** Žádná kontrola nad kvalitou zboží a reklamacemi, vysoká konkurence.")

    # =========================================================================
    # SEKCE 6: EFEKTIVITA, ŠTÍHLÁ VÝROBA A TECHNOLOGIE
    # =========================================================================
    elif selected_section_3 == "6.1 Štíhlá výroba, Poka-Yoke a 5S":
        st.markdown("### 6.1 Štíhlá výroba (Lean), Poka-Yoke a 5S")
        st.markdown("""
        <div class='box-blue'>
            ⚙️ <b>Praktický přesah:</b> Efektivita neznamená pracovat rychleji za každou cenu. Znamená odstraňovat plýtvání a zlepšovat procesy.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### Štíhlá výroba (Lean Production) a plýtvání MUDA")
        st.write("Štíhlá výroba vznikla v japonské automobilce Toyota. Jejím hlavním cílem je identifikovat a eliminovat **plýtvání (v japonštině MUDA)** — tedy jakoukoliv činnost, která spotřebovává zdroje, ale nepřináší zákazníkovi žádnou hodnotu.")
        
        st.markdown("##### 8 hlavních druhů plýtvání (Muda):")
        st.markdown("""
        1. 🏭 **Nadvýroba:** Vyrábění většího množství nebo dříve, než zákazník požaduje (nejhorší druh plýtvání).
        2. ⏳ **Čekání:** Prostoje lidí nebo strojů z důvodu chybějícího materiálu, informací nebo poruchy.
        3. 🚚 **Zbytečná doprava:** Přesouvání materiálu a polotovarů z jednoho konce haly na druhý.
        4. 🛠️ **Nadbytečné zpracování (Overprocessing):** Dělání práce navíc, kterou zákazník nevyžaduje ani nezaplatí (např. příliš leštěný povrch vnitřního skrytého dílu).
        5. 📦 **Nadbytečné zásoby:** Držet na skladě tuny materiálu nebo hotových výrobků, ve kterých leží vázané peníze.
        6. 🏃 **Zbytečné pohyby:** Pracovník se musí ohýbat, natahovat nebo chodit pro nářadí, protože ho nemá po ruce.
        7. 🔧 **Chyby a opravy (Zmetky):** Výroba vadných kusů, které se musí opravit nebo vyhodit.
        8. 🧠 **Nevyužitý potenciál lidí:** Ignorování nápadů a zkušeností řadových zaměstnanců ze strany vedení.
        """)
        st.divider()

        st.markdown("#### Poka-Yoke: Ochrana před neúmyslnou chybou")
        st.write("**Poka-Yoke** (v japonštině *„poka“ = neúmyslná chyba*, *„yoke“ = zabránění*) je technický nebo procesní prvek, který fyzicky znemožňuje udělat chybu, nebo na ni okamžitě upozorní.")
        
        c_py1, c_v2 = st.columns(2)
        with c_py1:
            st.markdown("<div class='box-blue'><b>Preventivní Poka-Yoke (Chyba se nemůže stát)</b></div>", unsafe_allow_html=True)
            st.markdown("""
            * 📱 **SIM karta / SD karta:** Má seříznutý roh, nelze ji zasunout špatně.
            * 🔌 **USB-C konektor:** Je symetrický, pasuje z obou stran.
            * ⛽ **Naftová pistole na čerpací stanici:** Je širší než hrdlo benzínové nádrže, naftu do benzíňáku nenatankujete.
            """)
        with c_v2:
            st.markdown("<div class='box-yellow'><b>Detekční Poka-Yoke (Systém na chybu ihned upozorní)</b></div>", unsafe_allow_html=True)
            st.markdown("""
            * 🚗 **Senzor zapnutí pásů v autě:** Auto začne hlasitě pískat, pokud nebuďte připoutaní.
            * 💻 **Webový formulář:** Zervená kolonka, pokud chybí `@` v e-mailu.
            * 🛒 **Samoobslužná pokladna:** Zablokuje se, pokud nepoložíte zboží na váhu.
            """)
        st.divider()

        st.markdown("#### Metoda 5S: Organizace a čistota pracoviště")
        st.write("Metoda 5S představuje pět kroků k vytvoření organizovaného, čistého a bezpečného prostředí. Původní japonské názvy byly přeloženy do praktických kroků:")
        
        st.markdown("""
        * 1️⃣ **Seiri (Vytřídit):** Projít pracoviště a nekompromisně vyhodit nebo odvézt vše, co se nepoužívá.
        * 2️⃣ **Seiton (Srovnat / Uspořádat):** „Místo pro všechno a všechno na svém místě.“ Každé nářadí má vyznačené přesné místo nebo stín na tabuli.
        * 3️⃣ **Seiso (Soustavně čistit):** Pravidelný úklid pracoviště a kontrola strojů (při čištění se často odhalí drobné závady a úniky oleje).
        * 4️⃣ **Seiketsu (Standardizovat):** Vytvořit jasná pravidla, návody a barevné značení, aby každý hned poznal správný stav.
        * 5️⃣ **Shitsuke (Stále udržovat / Disciplína):** Proměnit dodržování pravidel v osobní návyk a neustále stav kontrolovat.
        """)

        st.divider()
        st.markdown("<div class='box-yellow'>🔎 <b>Detektiv plýtvání (Lean cvičení)</b></div>", unsafe_allow_html=True)
        sit = st.text_area("Popiš situaci z vaší školní jídelny, dílny nebo brigády, kde vzniká chaos:", 
                           value="Při výdeji obědů kuchařka musí běhat pro příbory do vedlejší místnosti a studenti čekají ve 20metrové frontě.")
        c_l1, c_v2 = st.columns(2)
        with c_l1:
            plytvani_typ = st.multiselect("Jaké druhy plýtvání (MUDA) zde vznikají?", [
                "Čekání", "Zbytečný pohyb", "Zbytečná doprava", "Chyby a opravy", "Nadbytečné zásoby", "Nadvýroba"
            ], default=["Čekání", "Zbytečný pohyb"])
        with c_v2:
            reseni_lean = st.text_input("Navrhni jedno jednoduché zlepšení (Poka-Yoke / 5S):", 
                                       value="Příbory umístit přímo k výdejnímu okénku do označeného stojanu (Seiton).")
        if st.button("Uložit návrh zlepšení"):
            st.success("✅ Skvělý postřeh! Přesně takhle uvažují Lean procesní inženýři ve firmách.")

    elif selected_section_3 == "6.2 Průmysl 4.0, Cirkulární ekonomika a KPI":
        st.markdown("### 6.2 Průmysl 4.0, Cirkulární ekonomika a Dashboardy")
        
        st.markdown("#### Průmysl 4.0, AI a Automatizace")
        st.write("Moderní výroba už nejsou jen lidé u pásu. Do výroby vstupují roboti, IoT senzory, umělá inteligence, datová analytika a automatizované sklady.")
        
        st.markdown("""
        * 📈 **Rostou fixní náklady** na nákup technologií a softwaru,
        * 📉 **Klesají variabilní náklady** na výrobu jednoho kusu,
        * ⚙️ Zvyšuje se potřeba odborné údržby, IT specialistů a datové kontroly.
        """)

        st.divider()
        st.markdown("<div class='box-purple'>🤖 <b>Kalkulačka návratnosti robota / automatizace</b></div>", unsafe_allow_html=True)
        
        c_r1, c_r2 = st.columns(2)
        with c_r1:
            investice_robot = st.number_input("Investiční výdaj na robota/software (Kč):", value=2000000, step=100000)
            uspora_rok = st.number_input("Roční úspora nákladů / vyšší výkon (Kč):", value=500000, step=50000)
        with c_r2:
            if uspora_rok > 0:
                doba_n = investice_robot / uspora_rok
                st.metric("Doba návratnosti robota", f"{doba_n:.1f} let")
                if doba_n <= 4:
                    st.success(f"✅ Doba návratnosti je {doba_n:.1f} let. Investice do automatizace se firmě velmi rychle vrátí!")
                else:
                    st.warning(f"Doba návratnosti je {doba_n:.1f} let. Firma musí posoudit životnost robota a rizika zastarání.")

        st.divider()
        st.markdown("#### Cirkulární ekonomika a udržitelná výroba")
        st.write("Udržitelnost není jen marketing. Pro firmu znamená nižší spotřebu materiálu, méně odpadu a nižší náklady.")
        
        st.markdown("""
        | Lineární ekonomika (Starý model) | Cirkulární ekonomika (Udržitelný model) |
        | :--- | :--- |
        | Vytěžit → Vyrobit → Prodat → Použít → Vyhodit | Navrhnout → Vyrobit → Používat → Opravit → Znovu využít → Recyklovat |
        """)
        
        st.markdown("""
        * 🔄 **Upcycling:** Starý nebo odpadní materiál se promění v produkt s vyšší hodnotou (např. tašky ze starých autoplacht).
        * 👶 **Cradle to Cradle („od kolébky ke kolébce“):** Návrh produktu tak, aby se jeho materiály daly nekonečně znovu využívat bez ztráty kvality.
        * 🛠️ **Design pro opravitelnost:** Výrobek je navržen tak, aby ho šlo snadno rozmontovat a vyměnit rozbitelný díl.
        * 📊 **ESG:** Sledování dopadů firmy na životní prostředí (Environmental), společnost (Social) a způsob řízení (Governance).
        """)

        st.divider()
        st.markdown("#### KPI a Přehledové Dashboardy: Jak řídit firmu podle dat")
        
        st.markdown("""
        <div class='box-blue'>
            📊 <b>KPI (Key Performance Indicators / Klíčové ukazatele výkonnosti):</b> Měřitelná čísla, která ukazují, jak úspěšně firma plní své hlavní cíle. 
        </div>
        """, unsafe_allow_html=True)

        st.markdown("##### 🚗 Metafora přístrojové desky v autě")
        st.write("Představ si, že řídíš auto. Na palubní desce nesleduješ teploměr v kufru ani počet šroubků v motoru. Sleduješ jen to podstatné: **rychlost (KPI 1)**, **stav paliva (KPI 2)** a **otáčky (KPI 3)**. Podle toho se rozhoduješ: *Přidám plyn? Musím k benzínce?* Přesně tak funguje firemní **Dashboard**.")

        st.markdown("##### ⚠️ Past jménem „Vanity Metrics“ (Marnivá čísla)")
        st.write("Firma se nesmí nechat opít čísly, která sice vypadají hezky na papíře, ale neříkají nic o skutečném zisku nebo zdraví podniku.")

        st.markdown("""
        | Oblast | 🎭 Vanity Metric (Pěkné na pohled, ale nezaplatí účty) | 🎯 Skutečné Business KPI (Dá se podle něj rozhodnout) |
        | :--- | :--- | :--- |
        | **E-shop** | Celková návštěvnost webu | **Konverzní poměr (%)** & **Čistá zisková marže** |
        | **Sociální sítě** | Počet sledujících / Lajky pod fotkou | **Míra prokliku (CTR)** & **Cena za získání zákazníka (CAC)** |
        | **Výroba** | Počet vyrobených kusů za směnu | **Zmetkovitost (%)** & **Doba obratu zásoby** |
        | **Student** | Počet hodin prosezených nad knížkou | **Počet zvládnutých otázek** & **Známkový průměr** |
        """)

        st.divider()
        st.markdown("<div class='box-purple'>🕹️ <b>Interaktivní simulátor: Sestav si řídící Dashboard e-shopu</b></div>", unsafe_allow_html=True)
        st.write("Jsi ředitel/ka e-shopu s oblečením. Měň parametry vlevo a sleduj, jak tvůj živý Dashboard vpravo reaguje na zdraví firmy.")

        c_kpi1, c_kpi2 = st.columns([1, 1.2])
        with c_kpi1:
            kpi_navstevnost = st.number_input("Měsíční návštěvnost webu (lidí):", value=10000, step=1000)
            kpi_konverze = st.slider("Konverzní poměr (%) - kolik % lidí nakoupí:", min_value=0.1, max_value=10.0, value=2.0, step=0.1)
            kpi_kosik = st.number_input("Průměrná hodnota objednávky (Kč):", value=850, step=50)
            kpi_vratky = st.slider("Míra vratek a reklamací (%):", min_value=0.0, max_value=30.0, value=5.0, step=1.0)

        with c_kpi2:
            kpi_objednavky = int(kpi_navstevnost * (kpi_konverze / 100))
            kpi_hrube_trzby = kpi_objednavky * kpi_kosik
            kpi_ztrata_vratky = kpi_hrube_trzby * (kpi_vratky / 100)
            kpi_ciste_trzby = kpi_hrube_trzby - kpi_ztrata_vratky

            st.markdown("##### 🚗 Živý Manažerský Dashboard:")
            st.metric("Počet vyřízených objednávek", f"{kpi_objednavky} ks")
            st.metric("Čisté tržby (po odečtení vratek)", f"{kpi_ciste_trzby:,.0f} Kč".replace(",", " "))
            st.metric("Ztráta z vratek a reklamací", f"{kpi_ztrata_vratky:,.0f} Kč".replace(",", " "))

            st.markdown("##### 🚦 Diagnostika podle KPI:")
            if kpi_konverze < 1.5:
                st.warning("⚠️ **Nízká konverze!** Lidé na web chodí, ale nenakupují. Rozbitý košík nebo drahá doprava?")
            elif kpi_konverze >= 3.5:
                st.success("✅ **Skvělá konverze!** Web přesvědčí k nákupu nadprůměrné množství lidí.")

            if kpi_vratky > 12:
                st.error("🚨 **Kritická vratkovost!** Zákazníci masivně vracejí zboží. Velikosti nesedí nebo fotky neodpovídají realitě.")
    elif selected_section_3 == "6.3 Projektová dílna: Launch vlastního merche":
        st.markdown("### 6.3 Projektová dílna: Launch vlastního merche / e-shopu")
        st.markdown("""
        <div class='box-blue'>
            ✍️ <b>Projektový úkol:</b> Představte si, že jako tvůrce obsahu, streamer, školní tým nebo studentská značka chcete pustit na trh vlastní edici mikin, triček, plakátů nebo školních zápisníků.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div class='box-yellow'>🧪 <b>Projektová kalkulačka & Diagnostika merche</b></div>", unsafe_allow_html=True)
        st.write("Zadej své plánované náklady a cenovou strategii. Kalkulačka spočítá příspěvek na úhradu, bod zvratu i očekávaný zisk.")
        
        cp1, cp2 = st.columns(2)
        with cp1:
            p_nazev = st.text_input("Název produktu / projektu:", value="Školní edice mikin s kapucí")
            p_cena = st.number_input("Prodejní cena za 1 kus (Kč):", value=890, step=50)
            p_var = st.number_input("Variabilní náklady na 1 kus (potisk, textil, obal) (Kč):", value=420, step=20)
            p_fix = st.number_input("Fixní náklady celkem (grafika, reklama, e-shop) (Kč):", value=15000, step=1000)
            p_odhad = st.number_input("Očekávaný počet prodaných kusů:", value=50, step=10)
            
        with cp2:
            p_prispevek = p_cena - p_var
            st.markdown("##### 📐 Výsledky projektu:")
            
            if p_prispevek <= 0:
                st.error("💥 KRITICKÁ CHYBA: Prodejní cena je nižší nebo rovna variabilním nákladům! Na každém kusu proděláváš.")
            else:
                p_bz = math.ceil(p_fix / p_prispevek)
                p_trzby = p_odhad * p_cena
                p_naklady_celkem = p_fix + (p_odhad * p_var)
                p_zisk = p_trzby - p_naklady_celkem
                p_marze = (p_zisk / p_trzby * 100) if p_trzby > 0 else 0
                
                st.metric("Příspěvek na úhradu na 1 kus", f"{p_prispevek} Kč")
                st.metric("Bod zvratu (musíš prodat)", f"{p_bz} kusů")
                st.metric("Předpokládaný zisk / ztráta", f"{p_zisk:,} Kč".replace(",", " "))
                st.metric("Zisková marže", f"{p_marze:.1f} %")
                
                st.divider()
                st.markdown("##### 🚦 Diagnostika projektu:")
                if p_odhad < p_bz:
                    st.error(f"❌ **Projekt je rizikový!** Tvůj odhad prodeje ({p_odhad} ks) nepokryje ani bod zvratu ({p_bz} ks). Budeš ve ztrátě {abs(p_zisk):,} Kč.")
                    st.info("💡 **Doporučení:** Zvyš cenu, vyjednej levnější textil nebo zvyšte propagační kampaň.")
                else:
                    st.success(f"🎉 **Projekt je ziskový!** Po prodeji {p_bz} kusů začínáš vydělávat. Při prodeji {p_odhad} kusů bude čistý zisk {p_zisk:,} Kč.")

        st.divider()
        st.markdown("#### Moje manažerské rozhodnutí k projektu")
        
        m_model = st.radio("Zvolený model výroby:", [
            "Print-on-Demand (výroba po objednávce - nulové zásoby)",
            "Nákup na sklad dopředu (vyšší marže, ale riziko neprodaných kusů)"
        ])
        
        m_kpi = st.multiselect("Které KPI budeš sledovat pro vyhodnocení úspěchu?", [
            "Počet prodaných kusů", "Čistá zisková marže", "Rychlost vyprodání edice", 
            "Návratnost investic do reklamy (ROAS)", "Míra vratek a reklamací"
        ], default=["Počet prodaných kusů", "Čistá zisková marže"])
        
        rozhodnuti_text = st.text_area("Shrnutí strategického rozhodnutí pro prezentaci před třídou/vedením:", 
                                       value="Projekt spustíme jako limitovanou edici v předprodeji (Print-on-Demand), čímž eliminujeme riziko neprodaných zásob. Počáteční grafické náklady pokryjeme z příspěvku na úhradu po prodeji prvních 32 kusů.")
        
        if st.button("Uložit projektový list"):
            st.balloons()
            st.success("✅ Projektový list byl úspěšně sestaven a připraven k obhajobě!")

 # =========================================================================
    # SEKCE 7: PŘÍPADOVÉ STUDIE A ZÁVĚREČNÝ CHECKLIST
    # =========================================================================
elif selected_section_3 == "7.1 Případové studie z praxe":
        st.markdown("### 7.1 Případové studie z praxe")
        st.write("Aplikuj získané znalosti z výroby, kalkulací, odpisů a řízení jakosti na reálných příkladech z praxe.")

        st.divider()
        st.markdown("#### 1. Kavárna u školy: Kdy se začne vyplácet?")
        st.markdown("<div class='box-blue'>☕ <b>Situace:</b> Studentský tým chce otevřít malý stánek s kávou a domácí limonádou během školních akcí.</div>", unsafe_allow_html=True)
        
        st.markdown("""
        * 🔒 **Fixní náklady na vybavení a povolení:** 12 000 Kč
        * 📈 **Variabilní náklady na 1 nápoj:** 18 Kč
        * 🏷️ **Prodejní cena 1 nápoje:** 45 Kč
        * 📊 **Očekávaný prodej:** 500 nápojů za měsíc
        """)

        with st.form("form_studie_kavarna"):
            st.markdown("##### 📝 Vyplň řešení:")
            s1_prispevek = st.number_input("Příspěvek na úhradu na 1 nápoj (Kč):", value=0, step=1)
            s1_bz = st.number_input("Bod zvratu (počet nápojů k pokrytí fixních nákladů):", value=0, step=1)
            s1_dostacujici = st.radio("Je plánovaný prodej 500 nápojů dostatečný k dosažení zisku?", ["Vyber...", "Ano", "Ne"], horizontal=True)
            s1_opatreni = st.text_input("Navrhni jedno opatření, jak snížit riziko ztráty:")

            if st.form_submit_button("Zkontrolovat výpočty kavárny"):
                spravny_prispevek = 45 - 18
                spravny_bz = math.ceil(12000 / spravny_prispevek)
                
                if s1_prispevek == spravny_prispevek and abs(s1_bz - spravny_bz) <= 1 and s1_dostacujici == "Ano":
                    st.success(f"🎉 **Skvěle! Všechny výpočty máš správně!**\n* Příspěvek na úhradu = {spravny_prispevek} Kč na nápoj.\n* Bod zvratu = {spravny_bz} nápojů.\n* Plánovaných 500 nápojů stačí, zisk bude {(500 - spravny_bz) * spravny_prispevek:,} Kč.".replace(",", " "))
                    st.balloons()
                else:
                    st.error(f"Něco tam nesedí. **Nápověda:** Příspěvek na úhradu = cena (45) − variabilní náklady (18) = **27 Kč**. Bod zvratu = 12 000 / 27 ≈ **445 nápojů**.")

        st.divider()
        st.markdown("#### 2. Mikiny pro školní tým: Sklad, nebo Print-on-Demand?")
        st.markdown("<div class='box-blue'>👕 <b>Situace:</b> Školní tým chce prodávat mikiny s vlastním potiskem. Zvažuje dvě varianty výroby.</div>", unsafe_allow_html=True)
        
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.markdown("<div class='box-gray'><b>Varianta A: Výroba na sklad</b><br>• Fixní náklady: 8 000 Kč<br>• Nákup a potisk 1 mikiny: 420 Kč<br>• Cena: 750 Kč<br>⚠️ <i>Riziko neprodaných kusů.</i></div>", unsafe_allow_html=True)
        with col_m2:
            st.markdown("<div class='box-green'><b>Varianta B: Print-on-Demand</b><br>• Fixní náklady: 8 000 Kč<br>• Výroba 1 mikiny po objednání: 560 Kč<br>• Cena: 750 Kč<br>✅ <i>Nulové zásoby.</i></div>", unsafe_allow_html=True)

        if st.checkbox("📈 Zobrazit grafické srovnání zisku obou variant"):
            try:
                import pandas as pd
                kusy_range = list(range(0, 100, 5))
                zisk_a = [(k * (750 - 420)) - 8000 for k in kusy_range]
                zisk_b = [(k * (750 - 560)) - 8000 for k in kusy_range]
                
                df_mikiny = pd.DataFrame({
                    "Prodané kusy": kusy_range,
                    "Zisk Varianta A (Sklad)": zisk_a,
                    "Zisk Varianta B (Print-on-Demand)": zisk_b
                }).set_index("Prodané kusy")
                st.line_chart(df_mikiny, color=["#3b82f6", "#22c55e"])
                st.caption("🟦 Modrá = Výroba na sklad (strmější růst zisku) | 🟩 Zelená = Print-on-Demand (bezpečnější při malých prodejích).")
            except ImportError:
                st.warning("Pro zobrazení grafu je potřeba knihovna Pandas.")

        with st.form("form_studie_mikiny"):
            st.markdown("##### 👕 Vyplň porovnání variant:")
            m_a_prisp = st.number_input("Varianta A — příspěvek na úhradu na kus (Kč):", value=0)
            m_b_prisp = st.number_input("Varianta B — příspěvek na úhradu na kus (Kč):", value=0)
            m_vyssi_marze = st.radio("Která varianta má vyšší marži na 1 kus?", ["Vyber...", "Varianta A (Sklad)", "Varianta B (Print-on-Demand)"], horizontal=True)
            m_nizsi_riziko = st.radio("Která varianta má nižší riziko neprodaných zásob?", ["Vyber...", "Varianta A (Sklad)", "Varianta B (Print-on-Demand)"], horizontal=True)

            if st.form_submit_button("Zkontrolovat porovnání"):
                if m_a_prisp == 330 and m_b_prisp == 190 and m_vyssi_marze == "Varianta A (Sklad)" and m_nizsi_riziko == "Varianta B (Print-on-Demand)":
                    st.success("✅ **Výborně, máš to absolutně přesně!**\n* Varianta A: příspěvek = 330 Kč/ks (vyšší zisk při velkém prodeji).\n* Varianta B: příspěvek = 190 Kč/ks (bezpečnější při nejistém prodeji).")
                else:
                    st.error("Zkontroluj výpočty: Varianta A = 750 − 420 = 330 Kč. Varianta B = 750 − 560 = 190 Kč.")

        st.divider()
        st.markdown("#### 3. Výrobní dílna: Problém se zmetkovitostí")
        st.markdown("<div class='box-blue'>🛠️ <b>Situace:</b> Malá výrobní dílna vyrábí dřevěné stojany na notebooky. V posledním měsíci výrazně vzrostl počet vadných kusů.</div>", unsafe_allow_html=True)

        st.markdown("""
        * 📦 **Měsíční výroba:** 1 000 kusů
        * 📉 **Zmetkovitost dříve:** 3 % | 📈 **Zmetkovitost nyní:** 11 %
        * 💸 **Náklady na 1 vadný kus:** 160 Kč
        """)

        with st.form("form_studie_zmetky"):
            st.markdown("##### 🛠️ Vyplň analýzu zmetkovitosti:")
            z_driv = st.number_input("Vadné kusy dříve (ks):", value=0)
            z_ted = st.number_input("Vadné kusy nyní (ks):", value=0)
            z_rozdil_kc = st.number_input("O kolik Kč se zvýšily finanční ztráty z nákladů na zmetky? (Kč):", value=0)

            if st.form_submit_button("Zkontrolovat analýzu zmetkovitosti"):
                if z_driv == 30 and z_ted == 110 and z_rozdil_kc == 12800:
                    st.success("🎉 **Skvělá práce!**\n* Vadné kusy dříve: 30 ks (3 % z 1 000).\n* Vadné kusy nyní: 110 ks (11 % z 1 000).\n* Rozdíl je 80 vadných kusů × 160 Kč = **12 800 Kč zbytečné finanční ztráty!**")
                else:
                    st.error("Nápověda: Dříve = 1 000 × 0,03 = 30 ks. Nyní = 1 000 × 0,11 = 110 ks. Zvýšení o 80 ks × 160 Kč = 12 800 Kč.")

    elif selected_section_3 == "7.2 Závěrečný checklist a prověrka kapitoly":
        st.markdown("### 7.2 Závěrečný checklist a prověrka kapitoly")
        st.write("Projdi si klíčové dovednosti Kapitoly 3. Zaškrtni všechny body, které bezpečně zvládáš!")

        st.markdown("<div class='box-yellow'>✅ <b>Sebehodnotící checklist Kapitoly 3</b></div>", unsafe_allow_html=True)
        
        ch1 = st.checkbox("Umím rozlišit náklad, výdaj, výnos a příjem a uvést příklady.")
        ch2 = st.checkbox("Umím spočítat účetní i ekonomický zisk nebo ztrátu.")
        ch3 = st.checkbox("Umím vysvětlit rozdríl mezi fixními a variabilními náklady.")
        ch4 = st.checkbox("Umím spočítat bod zvratu v kusech a interpretovat ho.")
        ch5 = st.checkbox("Rozumím rozdílu mezi účetními a daňovými odpisy (rovnoměrné vs. zrychlené).")
        ch6 = st.checkbox("Umím vysvětlit principy Lean výroby (plýtvání Muda, Poka-Yoke, metoda 5S, Kanban).")
        ch7 = st.checkbox("Rozumím moderním cenovým strategiím (Freemium, POD, Asset-Light) a umím navrhnout KPI.")

        splneno_pocet = sum([ch1, ch2, ch3, ch4, ch5, ch6, ch7])
        procento = int((splneno_pocet / 7) * 100)

        st.progress(splneno_pocet / 7)
        st.metric("Tvé skóre v Kapitole 3", f"{splneno_pocet} z 7 bodů ({procento} %)")

        if splneno_pocet == 7:
            st.balloons()
            st.success("🎉 **GRATULUJEME!** Zvládl/a jsi kompletní látku 3. kapitoly s plným počtem bodů. Jsi připraven/a na reálné řízení firmy!")
        elif splneno_pocet >= 4:
            st.info("👍 **Skvělý výkon!** Většině témat rozumíš. Doporučujeme si ještě zopakovat chybějící podkapitoly výše.")
        else:
            st.warning("⚠️ Zkus si projít jednotlivé podkapitoly znovu a vyzkoušet si v nich interaktivní kalkulačky a kvízy.")

        st.divider()
        st.markdown("#### 🏆 Blesková závěrečná prověrka znalostí (5 otázek)")
        
        with st.form("form_proverka_k3"):
            p1 = st.selectbox("1. Nákup nového výrobního stroje zaplacený převodem z účtu je v roce nákupu:", [
                "Vyber...", "Náklad v plné výši", "Výdaj v plné výši, do nákladů jde postupně přes odpisy", "Příjem firmy"
            ])
            p2 = st.selectbox("2. Bod zvratu je okamžik, kdy:", [
                "Vyber...", "Jsou tržby vyšší než náklady a firma dosahuje maximálního zisku", "Tržby pokryjí celkové náklady a zisk je přesně 0 Kč", "Firma zaplatí své první daně"
            ])
            p3 = st.selectbox("3. Počítač z 1. odpisové skupiny se podle českého zákona odpisuje daňově po dobu:", [
                "Vyber...", "3 roky", "5 let", "10 let"
            ])
            p4 = st.selectbox("4. Systém Poka-Yoke ve štíhlé výrobě představuje:", [
                "Vyber...", "Kontrolu kvality na konci výroby", "Technický nebo procesní prvek znemožňující vznik chyby", "Drahý nákup robotických ramen"
            ])
            p5 = st.selectbox("5. Který z následujících ukazatelů je tzv. 'Vanity Metric' (marnivé číslo)?", [
                "Vyber...", "Konverzní poměr e-shopu", "Čistá zisková marže", "Celkový počet zobrazení stránek (bez ohledu na prodej)"
            ])

            if st.form_submit_button("Vyhodnotit prověrku"):
                body = 0
                if p1 == "Výdaj v plné výši, do nákladů jde postupně přes odpisy": body += 1
                if p2 == "Tržby pokryjí celkové náklady a zisk je přesně 0 Kč": body += 1
                if p3 == "3 roky": body += 1
                if p4 == "Technický nebo procesní prvek znemožňující vznik chyby": body += 1
                if p5 == "Celkový počet zobrazení stránek (bez ohledu na prodej)": body += 1

                if body == 5:
                    st.success(f"🥇 **Perfektní test! Získal/a jsi {body}/5 bodů!**")
                    st.balloons()
                elif body >= 3:
                    st.info(f"🥈 **Dobrá práce! Získal/a jsi {body}/5 bodů.**")
                else:
                    st.error(f"❌ **Získal/a jsi {body}/5 bodů.** Projděte si ještě jednou odpovídající sekce v nabídce.")
