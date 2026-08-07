import streamlit as st
import math

def render():
    st.markdown("<span class='hero-badge'>Kapitola 4</span>", unsafe_allow_html=True)
    st.title("4. Cesta zaměstnance: od první orientace po kariérní rozhodnutí")
    st.markdown("<p style='font-size: 1rem; color: #64748b; margin-bottom: 1.5rem;'>Práce není jen o výplatní pásce. Je to o hledání hodnoty, rozpoznání vlastních dovedností, právní ochraně a kariérním růstu na měnícím se trhu práce.</p>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown("""
        <div class='box-blue'>
            <strong>⚙️ Pointa kapitoly:</strong> V této kapitole se naučíte orientovat na moderním trhu práce 4.0, správně číst pracovní smlouvy i výplatní pásky, vyjednávat o mzdě a chránit se před nekalými praktikami (jako je Švarcsystém).
        </div>
        """, unsafe_allow_html=True)

    # 📌 JEDNOTNÁ NABÍDKA PODKAPITOL (přesně podle podkladů)
    section_options_4 = [
        "1.1 Proč trh platí různé profese různě",
        "1.2 Trh práce 4.0 a AI",
        "1.3 Profese a dovednosti budoucnosti",
        "1.4 Osobní brand a digitální stopa",
        "2.1 HR a personalistika: co znamenají",
        "2.2 Nábor v éře AI",
        "2.3 Životopis, motivační dopis a portfolio",
        "2.4 Pracovní smlouva, DPP a DPČ",
        "2.5 Ukázka pracovní smlouvy a její náležitosti",
        "2.6 Zkušební doba",
        "2.7 Smlouva na dobu určitou a neurčitou",
        "2.8 Švarcsystém a gig economy",
        "2.9 Red flags v inzerátech a smlouvách",
        "3.1 Hrubá mzda, čistá mzda a superhrubé uvažování",
        "3.2 Nominální a reálná mzda",
        "3.3 Výplatní páska a její náležitosti",
        "3.4 Výpočet čisté mzdy krok za krokem",
        "3.5 Sazby pojištění, daně a náklady zaměstnavatele",
        "3.6 Slevy na dani a odčitatelné položky",
        "3.7 Kam jdou odvody (sociální a zdravotní pojištění)",
        "3.8 Celková odměna za práci a vyjednávání o mzdě",
        "4.1 Firemní kultura a wellbeing",
        "4.2 Právo na odpojení a podnikavost v zaměstnání",
        "4.3 Upskilling a reskilling",
        "5.1 Jak dát a dostat výpověď profesionálně",
        "5.2 Úřad práce, podpora v nezaměstnanosti a rekvalifikace",
        "6.1 Praktická dílna (Aktivity 1–5)",
        "7.1 Případové studie z praxe",
        "7.2 Slovníček, rychlé opakování a prověrka"
    ]
    
    selected_section_4 = st.selectbox("📌 Přechod na podkapitolu:", section_options_4, index=0)
    st.divider()

    # =========================================================================
    # SEKCE 1: JÁ NA TRHU PRÁCE: PŘÍPRAVA A ORIENTACE
    # =========================================================================
    if selected_section_4 == "1.1 Proč trh platí různé profese různě":
        st.markdown("### 1.1 Proč trh platí různé profese různě")
        st.markdown("""
        <div class='box-blue'>
            💡 <b>Cena práce (mzda):</b> Není určována tím, jak moc je práce namáhavá, ale vzácností dovedností, nabídkou a poptávkou na trhu a hodnotou, kterou zaměstnanec vytváří.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### Co ovlivňuje výši mzdy?")
        st.markdown("""
        * ⚖️ **Nabídka a poptávka:** Pokud po profesi všichni touží, ale málokdo ji umí (např. AI vývojář, cévní chirurg), mzda roste. Pokud práci zvládne každý po hodinové instruktáži, mzda je nižší.
        * 🧠 **Odpovědnost a riziko:** Lidé s hmotnou odpovědností nebo ti, kdo rozhodují o zdraví a bezpečnosti, mají vyšší finanční ohodnocení.
        * 🏭 **Přidaná hodnota:** Kolik peněz nebo úspor práce zaměstnance firmě přinese.
        * 📍 **Region:** Mzdy v Praze a krajských městech jsou z důvodu vyšších životních nákladů vyšší než v menších regionech.
        """)

        st.divider()
        st.markdown("<div class='box-yellow'>🕹️ <b>Simulátor trhu práce: Proč se mění mzda?</b></div>", unsafe_allow_html=True)
        st.write("Vyzkoušej si, jak vzácnost dovedností a náročnost profese mění nabízenou mzdu na trhu.")

        col_s1, col_s2 = st.columns(2)
        with col_s1:
            poptavka = st.slider("Poptávka firem po této profesi (kolik firem hledá):", 1, 10, 8)
            nabidka = st.slider("Nabídka uchazečů (kolik lidí to umí):", 1, 10, 2)
            odpovednost = st.slider("Míra odpovědnosti a rizika:", 1, 10, 7)

        with col_s2:
            # Výpočet teoretické orientační mzdy
            zakladni_mzda = 25000
            faktor_vzacnosti = (poptavka / nabidka)
            odhad_mzdy = int(zakladni_mzda * faktor_vzacnosti * (1 + (odpovednost * 0.08)))

            st.metric("Předpokládaná měsíční mzda", f"{odhad_mzdy:,} Kč".replace(",", " "))

            if nabidka < poptavka:
                st.success("🔥 **Nedostatková profese:** Firmy přeplácejí odborníky, protože uchazeči chybí!")
            elif nabidka == poptavka:
                st.info("⚖️ **Vyrovnaný trh:** Mzda odpovídá průměru v oboru.")
            else:
                st.warning("📉 **Přebytek uchazečů:** Na jedno místo se hlásí desítky lidí, zaměstnavatel si může vybírat a mzdy nerostou.")

    elif selected_section_4 == "1.2 Trh práce 4.0 a AI":
        st.markdown("### 1.2 Trh práce 4.0 a AI")
        st.write("Obsah této podkapitoly připravujeme...")

    elif selected_section_4 == "1.3 Profese a dovednosti budoucnosti":
        st.markdown("### 1.3 Profese a dovednosti budoucnosti")
        st.write("Obsah této podkapitoly připravujeme...")

    elif selected_section_4 == "1.4 Osobní brand a digitální stopa":
        st.markdown("### 1.4 Osobní brand a digitální stopa")
        st.write("Obsah této podkapitoly připravujeme...")

    # =========================================================================
    # SEKCE 2: HR, ZÍSKÁNÍ PRÁCE A PRACOVNÍ PRÁVO
    # =========================================================================
    elif selected_section_4 == "2.1 HR a personalistika: co znamenají":
        st.markdown("### 2.1 HR a personalistika: co znamenají")
        st.write("Obsah této podkapitoly připravujeme...")

    elif selected_section_4 == "2.2 Nábor v éře AI":
        st.markdown("### 2.2 Nábor v éře AI")
        st.write("Obsah této podkapitoly připravujeme...")

    elif selected_section_4 == "2.3 Životopis, motivační dopis a portfolio":
        st.markdown("### 2.3 Životopis, motivační dopis a portfolio")
        st.write("Obsah této podkapitoly připravujeme...")

    elif selected_section_4 == "2.4 Pracovní smlouva, DPP a DPČ":
        st.markdown("### 2.4 Pracovní smlouva, DPP a DPČ")
        st.write("Obsah této podkapitoly připravujeme...")

    elif selected_section_4 == "2.5 Ukázka pracovní smlouvy a její náležitosti":
        st.markdown("### 2.5 Ukázka pracovní smlouvy a její povinné náležitosti")
        st.write("Obsah této podkapitoly připravujeme...")

    elif selected_section_4 == "2.6 Zkušební doba":
        st.markdown("### 2.6 Zkušební doba")
        st.write("Obsah této podkapitoly připravujeme...")

    elif selected_section_4 == "2.7 Smlouva na dobu určitou a neurčitou":
        st.markdown("### 2.7 Smlouva na dobu určitou a neurčitou")
        st.write("Obsah této podkapitoly připravujeme...")

    elif selected_section_4 == "2.8 Švarcsystém a gig economy":
        st.markdown("### 2.8 Švarcsystém a gig economy")
        st.write("Obsah této podkapitoly připravujeme...")

    elif selected_section_4 == "2.9 Red flags v inzerátech a smlouvách":
        st.markdown("### 2.9 Red flags v inzerátech a smlouvách")
        st.write("Obsah této podkapitoly připravujeme...")

    # =========================================================================
    # SEKCE 3: HODNOTA MÉ PRÁCE: ODMĚŇOVÁNÍ A PENÍZE
    # =========================================================================
    elif selected_section_4 == "3.1 Hrubá mzda, čistá mzda a superhrubé uvažování":
        st.markdown("### 3.1 Hrubá mzda, čistá mzda a superhrubé uvažování")
        st.write("Obsah této podkapitoly připravujeme...")

    elif selected_section_4 == "3.2 Nominální a reálná mzda":
        st.markdown("### 3.2 Nominální a reálná mzda")
        st.write("Obsah této podkapitoly připravujeme...")

    elif selected_section_4 == "3.3 Výplatní páska a jejínáležitosti":
        st.markdown("### 3.3 Výplatní páska a ukázka výplatní pásky")
        st.write("Obsah této podkapitoly připravujeme...")

    elif selected_section_4 == "3.4 Výpočet čisté mzdy krok za krokem":
        st.markdown("### 3.4 Výpočet čisté mzdy krok za krokem")
        st.write("Obsah této podkapitoly připravujeme...")

    elif selected_section_4 == "3.5 Sazby pojištění, daně a náklady zaměstnavatele":
        st.markdown("### 3.5 Sazby sociálního, zdravotního pojištění a daně z příjmů")
        st.write("Obsah této podkapitoly připravujeme...")

    elif selected_section_4 == "3.6 Slevy na dani a odčitatelné položky":
        st.markdown("### 3.6 Slevy na dani, daňové zvýhodnění a odčitatelné položky")
        st.write("Obsah této podkapitoly připravujeme...")

    elif selected_section_4 == "3.7 Kam jdou odvody (sociální a zdravotní pojištění)":
        st.markdown("### 3.7 Kam jdou odvody")
        st.write("Obsah této podkapitoly připravujeme...")

    elif selected_section_4 == "3.8 Celková odměna za práci a vyjednávání o mzdě":
        st.markdown("### 3.8 Celková odměna za práci a vyjednávání o mzdě")
        st.write("Obsah této podkapitoly připravujeme...")

    # =========================================================================
    # SEKCE 4: ŽIVOT V PRÁCI: KULTURA, WELLBEING A KARIÉRNÍ RŮST
    # =========================================================================
    elif selected_section_4 == "4.1 Firemní kultura a wellbeing":
        st.markdown("### 4.1 Firemní kultura, wellbeing a prevence vyhoření")
        st.write("Obsah této podkapitoly připravujeme...")

    elif selected_section_4 == "4.2 Právo na odpojení a podnikavost v zaměstnání":
        st.markdown("### 4.2 Právo na odpojení a Intrapreneurship")
        st.write("Obsah této podkapitoly připravujeme...")

    elif selected_section_4 == "4.3 Upskilling a reskilling":
        st.markdown("### 4.3 Upskilling a reskilling")
        st.write("Obsah této podkapitoly připravujeme...")

    # =========================================================================
    # SEKCE 5: KONEC PRÁCE A KRIZOVÉ SITUACE
    # =========================================================================
    elif selected_section_4 == "5.1 Jak dát a dostat výpověď profesionálně":
        st.markdown("### 5.1 Jak dát a dostat výpověď")
        st.write("Obsah této podkapitoly připravujeme...")

    elif selected_section_4 == "5.2 Úřad práce, podpora v nezaměstnanosti a rekvalifikace":
        st.markdown("### 5.2 Úřad práce, podpora a rekvalifikace")
        st.write("Obsah této podkapitoly připravujeme...")

    # =========================================================================
    # SEKCE 6 A 7: PRAKTICKÁ DÍLNA, PŘÍPADOVÉ STUDIE A TEST
    # =========================================================================
    elif selected_section_4 == "6.1 Praktická dílna (Aktivity 1–5)":
        st.markdown("### 6.1 Praktická dílna")
        st.write("Obsah aktivit z praktické dílny připravujeme...")

    elif selected_section_4 == "7.1 Případové studie z praxe":
        st.markdown("### 7.1 Případové studie z praxe")
        st.write("Případové studie připravujeme...")

    elif selected_section_4 == "7.2 Slovníček, rychlé opakování a prověrka":
        st.markdown("### 7.2 Slovníček, rychlé opakování a prověrka kapitoly")
        st.write("Závěrečné opakování připravujeme...")

    else:
        st.info("Obsah pro tuto podkapitolu se právě připravuje. Pokračujte ve výběru výše.")
