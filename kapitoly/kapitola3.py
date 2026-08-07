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
        "4.1 Oběžný majetek a zásoby",
        "4.2 Dlouhodobý majetek a investice",
        "5. Kalkulace a ceny (připravuje se)",
        "6. Efektivita a štíhlá výroba (připravuje se)"
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
    elif selected_section_3 == "4.1 Oběžný majetek a zásoby":
        st.markdown("### 4.1 Oběžný majetek a plánování zásob")
        
        st.markdown("""
        <div class='box-blue'>
            🏢 <b>Podstata majetku:</b> Majetek firmy představuje vše, co firma používá ke své činnosti. Dělí se na <b>oběžný</b> (rychle se mění, spotřebovává) a <b>dlouhodobý</b> (slouží déle než 1 rok).
        </div>
        """, unsafe_allow_html=True)

        st.markdown("#### Oběžný majetek")
        st.write("Oběžný majetek se při činnosti firmy rychle mění. Patří sem materiál, nedokončená výroba, hotové výrobky, zboží, krátkodobé pohledávky (faktury k proplacení) a peníze v hotovosti nebo na účtu.")
        st.markdown("<div class='box-gray'>🔄 <b>Koloběh:</b> Peníze se použijí na nákup materiálu → materiál se změní ve výrobek → výrobek se prodá → do firmy se vrátí peníze.</div>", unsafe_allow_html=True)

        st.divider()
        st.markdown("<div class='box-yellow'>🧩 <b>Rozřazovací kvíz: Co je co?</b></div>", unsafe_allow_html=True)
        c_kviz1, c_kviz2 = st.columns(2)
        with c_kviz1:
            q_auto = st.selectbox("Dodávka na rozvoz zboží:", ["Vyber...", "Oběžný", "Dlouhodobý"], key="q_auto")
            q_mat = st.selectbox("Mouka v pekárně:", ["Vyber...", "Oběžný", "Dlouhodobý"], key="q_mat")
        with c_kviz2:
            q_penize = st.selectbox("Peníze v pokladně:", ["Vyber...", "Oběžný", "Dlouhodobý"], key="q_penize")
            q_sw = st.selectbox("Účetní program (licence):", ["Vyber...", "Oběžný", "Dlouhodobý"], key="q_sw")
        
        if st.button("Vyhodnotit majetek"):
            if q_auto == "Dlouhodobý" and q_mat == "Oběžný" and q_penize == "Oběžný" and q_sw == "Dlouhodobý":
                st.success("✅ Výborně! Auto a licence vydrží roky (dlouhodobý), mouka se sní hned a peníze pořád obíhají (oběžný).")
            else:
                st.warning("Zkus to ještě promyslet. Pamatuj na pravidlo 1 roku!")

        st.divider()
        st.markdown("#### Plánování a druhy zásob")
        st.write("Cílem plánování je najít rovnováhu. Málo zásob = výroba stojí. Moc zásob = utopené peníze ve skladu.")
        
        st.markdown("""
        * **Běžná zásoba:** Slouží k pravidelné spotřebě mezi dvěma dodávkami.
        * **Pojistná zásoba:** Železná rezerva pro případ, že se dodávka zpozdí.
        * **Signální zásoba:** Určuje přesný okamžik, kdy musíte materiál znovu objednat!
        """)

        st.markdown("<div class='box-yellow'>🧮 <b>Kalkulačka: Kdy musím objednat nový materiál? (Signální zásoba)</b></div>", unsafe_allow_html=True)
        col_s1, col_s2 = st.columns([1, 1])
        with col_s1:
            denni_spotreba = st.number_input("Denní spotřeba (např. kg kávy):", value=5, min_value=1)
            dodaci_lhuta = st.number_input("Dodací lhůta (za kolik dní dodavatel přijede?):", value=3, min_value=1)
            pojistna = st.number_input("Pojistná (železná) zásoba (kg):", value=10, min_value=0)
            
        with col_s2:
            signalni = (denni_spotreba * dodaci_lhuta) + pojistna
            st.metric("Signální zásoba", f"{signalni} kg")
            st.info(f"Jakmile ti na skladě zbyde přesně {signalni} kg, musíš zvednout telefon a objednat. Než dodavatel přijede (za {dodaci_lhuta} dny), spotřebuješ {denni_spotreba * dodaci_lhuta} kg a zůstane ti přesně tvá železná rezerva {pojistna} kg.")

        st.divider()
        st.markdown("#### Moderní metody vyskladňování (FIFO vs. Průměr)")
        st.write("Firma nakupuje stejný materiál vícekrát, ale pokaždé za jinou cenu (např. v pondělí za 10 Kč, ve středu za 15 Kč). Jakou cenou se má materiál odepsat do nákladů, když se vydá do výroby?")
        
        tab1, tab2 = st.tabs(["🛒 FIFO (First In, First Out)", "⚖️ Vážený průměr"])
        with tab1:
            st.write("Ze skladu se účetně vydává nejdříve to, co bylo nakoupeno jako první (za původní cenu). Běžné u potravin a léků.")
            st.markdown("<div class='box-gray'>🏷️ <b>Příklad:</b> Koupili jste 100 ks po 20 Kč a pak 100 ks po 25 Kč. Pokud vydáte 80 ks, ocení se cenou 20 Kč/ks.</div>", unsafe_allow_html=True)
        with tab2:
            st.write("Materiál se oceňuje průměrnou cenou ze všech nákupů. Běžné ve stavebnictví, u hutního materiálu nebo pohonných hmot.")
            st.markdown("<div class='box-gray'>🏷️ <b>Vzorec:</b> Průměrná cena = Celková hodnota všech zásob / Celkové množství kusů</div>", unsafe_allow_html=True)
        
        st.markdown("*(Poznámka: Metoda LIFO (Last In, First Out) se v českém účetnictví běžně nepoužívá, ale slouží jako teoretický protipól k FIFO.)*")

    elif selected_section_3 == "4.2 Dlouhodobý majetek a investice":
        st.markdown("### 4.2 Dlouhodobý majetek, investice a odpisy")
        
        st.write("Dlouhodobý majetek firma používá delší dobu (déle než rok). Nespotřebuje se najednou, ale postupně se opotřebovává.")
        st.markdown("""
        * 🏗️ **Hmotný:** Má fyzickou podobu (budovy, stroje, auta).
        * 💿 **Nehmotný:** Nemá fyzickou podobu (software, licence, ochranná známka).
        * 📈 **Finanční:** Dlouhodobé investice, cenné papíry, podíly v jiných firmách.
        """)

        st.divider()
        st.markdown("#### Plánování investic a Návratnost")
        st.write("Pořízení dlouhodobého majetku je investice. Než firma koupí nový drahý stroj, musí vědět, za jak dlouho si na sebe stroj vydělá.")
        
        st.markdown("<div class='box-purple'>🕹️ <b>Simulátor: Vyplatí se firmě koupit nový robotický balicí stroj?</b></div>", unsafe_allow_html=True)
        
        c_i1, c_i2 = st.columns([1, 1.2])
        with c_i1:
            cena_stroje = st.number_input("Cena nového stroje (Kč):", value=500000, step=50000)
            vedlejsi_naklady = st.number_input("Doprava a instalace (Kč):", value=50000, step=10000)
            uspora_mesic = st.number_input("Měsíční úspora na brigádnících (Kč):", value=20000, step=5000)
            
        with c_i2:
            porizovaci_cena = cena_stroje + vedlejsi_naklady
            rocni_prinos = uspora_mesic * 12
            
            st.metric("Celková pořizovací cena", f"{porizovaci_cena:,} Kč".replace(",", " "))
            if rocni_prinos > 0:
                navratnost = porizovaci_cena / rocni_prinos
                st.metric("Doba návratnosti investice", f"{navratnost:.1f} let")
                
                if navratnost < 3:
                    st.success("✅ Tohle je skvělá investice! Stroj se zaplatí velmi rychle.")
                elif navratnost < 6:
                    st.warning("⚠️ Investice je přijatelná, ale záleží na tom, jak dlouho stroj fyzicky vydrží.")
                else:
                    st.error("❌ Riziková investice. Bude trvat příliš dlouho, než se stroj vůbec zaplatí.")
            else:
                st.error("Stroj nepřináší žádnou úsporu!")

        st.divider()
        st.markdown("#### Opotřebení a odpisy")
        st.write("Dlouhodobý majetek stárne buď fyzicky (používáním), nebo morálně (zastará technicky, i když ještě funguje).")
        st.markdown("<div class='box-blue'>🧾 <b>Odpis</b> vyjadřuje postupné přenášení hodnoty majetku do nákladů. Odpis NENÍ výdaj v daném okamžiku (výdaj nastal při pořízení).</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='box-yellow'>🧮 <b>Kalkulačka Rovnoměrných odpisů</b></div>", unsafe_allow_html=True)
        col_odp1, col_odp2 = st.columns(2)
        with col_odp1:
            odp_cena = st.number_input("Pořizovací cena majetku (Kč):", value=porizovaci_cena, disabled=True)
            odp_roky = st.slider("Předpokládaná doba používání (roky):", min_value=2, max_value=20, value=5)
            roky_v_provozu = st.slider("Kolik let už stroj používáte?", min_value=0, max_value=odp_roky, value=2)
            
        with col_odp2:
            rocni_odpis = odp_cena / odp_roky
            opravky = rocni_odpis * roky_v_provozu
            zustatkova = odp_cena - opravky
            
            st.metric("Roční odpis (Náklad do účetnictví)", f"{rocni_odpis:,.0f} Kč".replace(",", " "))
            st.metric("Oprávky (Součet dosavadních odpisů)", f"{opravky:,.0f} Kč".replace(",", " "))
            st.metric("Zůstatková cena (Aktuální účetní hodnota)", f"{zustatkova:,.0f} Kč".replace(",", " "))
            st.info(f"Kdyby firma chtěla stroj dnes prodat, z účetního hlediska má hodnotu {zustatkova:,.0f} Kč.")

    else:
        st.info("Obsah pro tuto podkapitolu se právě připravuje. Pokračujte ve výběru výše.")
