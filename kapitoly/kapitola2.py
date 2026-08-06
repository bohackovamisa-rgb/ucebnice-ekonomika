import streamlit as st

def render():
    st.markdown("<span class='hero-badge'>Kapitola 2</span>", unsafe_allow_html=True)
    st.title("2. Finance a osobní management")
    st.markdown("<p style='font-size: 1rem; color: #64748b; margin-bottom: 1.5rem;'>Finance v běžném životě: peníze, rozhodování a odpovědnost.</p>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown("""
        <div class='box-blue'>
            <strong>🪙 Pointa kapitoly:</strong> Finanční gramotnost není jen znalost pojmů. Je to schopnost rozumět penězům jako systému, bezpečně se rozhodovat, vyhodnocovat rizika a plánovat osobní i podnikové finance tak, aby člověk dokázal reagovat na běžné i krizové situace.
        </div>
        """, unsafe_allow_html=True)

    section_options_2 = [
        "1.1 Peníze jako digitální data (1.1.1 - 1.1.15)",
        "1.2 ČNB a komerční banky",
        "1.3 Platební styk",
        "1.4 Fintech revoluce"
    ]
    selected_section_2 = st.selectbox("📌 Přechod na podkapitolu:", section_options_2, index=0)
    st.divider()

    # --- 1.1 PENÍZE JAKO DIGITÁLNÍ DATA ---
    if selected_section_2 == "1.1 Peníze jako digitální data (1.1.1 - 1.1.15)":
        st.markdown("<div class='sub-section-header'>1. BANKOVNÍ SYSTÉM A PENÍZE V 21. STOLETÍ</div><h2>1.1 Peníze jako digitální data</h2>", unsafe_allow_html=True)
        
        st.write("21. století není jen éra umělé inteligence a sociálních sítí. Je to především éra totální transformace toho, jak vnímáme hodnotu. Ještě před pár desítkami let znamenalo „být v bance“ fyzickou návštěvu přepážky, papírování a čekání na úřední hodiny. Dnes? Bankovní systém se stal neviditelným operačním systémem našeho života.")

        with st.container(border=True):
            st.markdown("""
            <div class='box-blue'>
                <strong>💡 Proč je to důležité právě teď?</strong>
                <ul>
                    <li><strong>Technologie jako hybatel:</strong> Od okamžitých mezinárodních plateb až po investování v mobilu.</li>
                    <li><strong>Nekonečné možnosti a nová rizika:</strong> Peníze jsou data vyžadující novou úroveň digitální gramotnosti.</li>
                    <li><strong>Bankovnictví 2.0:</strong> Tradiční banky soupeří s agilními fintech startupy.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 1.1.1 Proč peníze vůbec vznikly")
            st.write("Na úplném začátku lidé používali **naturální směnu** (zboží za zboží). Problém byl v tom, že směna fungovala jen při **dvojí shodě potřeb**.")
            st.info("🍞 **Příklad:** Pekař chce boty, ale švec nechce chléb. Pekař musí složitě hledat někoho dalšího.")

        with st.container(border=True):
            st.markdown("### 1.1.2 Komoditní peníze")
            st.write("První peníze měly podobu komodit — sůl, obilí, dobytek, kožešiny, mušle, drahé kovy.")
            
            kom_sel = st.selectbox("Zvol komoditu:", ["Vyber...", "Sůl 🧂", "Dobytek / Kráva 🐄", "Mušle 🐚", "Zlatý prach ✨"], key="k2_1_1_2_kom")
            if kom_sel == "Sůl 🧂":
                st.info("Sůl je užitečná, ale při kontaktu s vodou se rozpustí!")
            elif kom_sel == "Dobytek / Kráva 🐄":
                st.error("❌ Kráva se špatně dělí a musíte ji neustále krmit.")
            elif kom_sel == "Mušle 🐚":
                st.warning("⚠️ Mimo pobřeží nemusí mít žádnou uznávanou hodnotu.")
            elif kom_sel == "Zlatý prach ✨":
                st.success("✅ Skvělé k uchování hodnoty, ale musíte ho při platbě složitě vážit.")

        with st.container(border=True):
            st.markdown("### 1.1.3 až 1.1.8 Od mincí k Fiat penězům")
            st.write("Mince přinesly standardizaci kovu, bankovky nahradily těžké kovy papírovými stvrzenkami a Zlatý standard pevně vázal měnu na zásoby zlata.")
            st.write("V roce 1971 (**Nixonův šok**) byla zrušena vazba dolaru na zlato a svět přešel k dnešním **fiat penězům**, jejichž hodnota stojí na důvěře ve stát a centrální banku.")

        with st.container(border=True):
            st.markdown("### 1.1.9 až 1.1.12 Bezhotovostní peníze, karty a Fintech")
            st.write("Peníze dnes fungují jako účetní záznam v bance. Karta, mobil nebo hodinky jsou pouze **klíče k tomuto účtu**.")
            
            st.markdown("##### 🚨 Trenažér phishingu:")
            st.info("**Od:** bezpecnost@bnka-podpora-klientu.cz\n**Předmět:** ZABLOKOVANÝ ÚČET - OKAMŽITÁ AKCE!\nPro odblokování karty klikněte ZDE: www.mojebanka-rychle-overeni.com/login")

            p_chk1 = st.checkbox("Podezřelá adresa odesílatele (překlepy)", key="k2_1_1_ph1")
            p_chk2 = st.checkbox("Výzva k nahlášení na Policii", key="k2_1_1_ph2")
            p_chk3 = st.checkbox("Tlak na čas a vyvolání strachu", key="k2_1_1_ph3")
            p_chk4 = st.checkbox("Falešný odkaz nevedoucí na web banky", key="k2_1_1_ph4")

            if st.button("Vyhodnotit hrozbu phishingu", key="k2_1_1_ph_btn"):
                if p_chk1 and p_chk3 and p_chk4 and not p_chk2:
                    st.success("✅ Správně! Odhalil jsi všechny varovné signály phishingu.")
                else:
                    st.error("Zkus to znovu. Označ 3 varovné znaky.")

        with st.container(border=True):
            st.markdown("### 1.1.13 Kryptoměny a blockchain")
            st.write("Kryptoměny fungují na technologii **blockchain** — sdílené digitální účetní knize bez centrální banky.")

            scen_sel = st.selectbox("Vyber scénář vývoje (Model 13 000 Kč):", [
                "Pesimistický scénář (-20 % ročně)",
                "Nulový scénář (0 % ročně)",
                "Mírně růstový scénář (+5 % ročně)",
                "Silně růstový scénář (+15 % ročně)"
            ], key="k2_dca_1_1_sel")

            if "Pesimistický" in scen_sel:
                st.metric("Hodnota po 5 letech", "cca 7 700 Kč", delta="-5 300 Kč")
            elif "Nulový" in scen_sel:
                st.metric("Hodnota po 5 letech", "13 000 Kč", delta="0 Kč")
            elif "Mírně růstový" in scen_sel:
                st.metric("Hodnota po 5 letech", "cca 14 800 Kč", delta="+1 800 Kč")
            else:
                st.metric("Hodnota po 5 letech", "cca 19 300 Kč", delta="+6 300 Kč")

        with st.container(border=True):
            st.markdown("### 1.1.14 & 1.1.15 CBDC a shrnutí vývoje")
            st.write("CBDC představuje digitální měnu vydávanou přímo centrální bankou (např. Digitální Euro).")

    # --- 1.2 ČNB A KOMERČNÍ BANKY ---
    elif selected_section_2 == "1.2 ČNB a komerční banky":
        st.markdown("<div class='sub-section-header'>1. BANKOVNÍ SYSTÉM A PENÍZE V 21. STOLETÍ</div><h2>1.2 ČNB a komerční banky</h2>", unsafe_allow_html=True)
        
        with st.container(border=True):
            st.markdown("### 🎛️ Simulátor 2T repo sazby ČNB")
            sim_repo = st.slider("2T repo sazba ČNB (%):", min_value=0.5, max_value=10.0, value=4.75, step=0.25, key="k2_1_2_repo")
            
            col_s1, col_s2, col_s3 = st.columns(3)
            hypo_rate = round(sim_repo + 2.1, 2)
            spor_rate = round(max(0.1, sim_repo - 1.5), 2)
            
            col_s1.metric("Odhad sazby hypotéky", f"{hypo_rate} % p.a.")
            col_s2.metric("Odhad spořicího účtu", f"{spor_rate} % p.a.")
            
            if sim_repo >= 6.0:
                col_s3.metric("Dopad na inflaci", "Zpomaluje 📉", delta="- Vysoké úroky")
            elif sim_repo <= 2.0:
                col_s3.metric("Dopad na inflaci", "Roste 📈", delta="+ Rychlé půjčky")
            else:
                col_s3.metric("Dopad na inflaci", "Stabilizovaná ⚖️", delta="Neutralita")

    # --- 1.3 PLATEBNÍ STYK ---
    elif selected_section_2 == "1.3 Platební styk":
        st.markdown("<div class='sub-section-header'>1. BANKOVNÍ SYSTÉM A PENÍZE V 21. STOLETÍ</div><h2>1.3 Platební styk</h2>", unsafe_allow_html=True)
        st.write("Platební styk znamená převod peněz mezi plátcem a příjemcem.")

    # --- 1.4 FINTECH REVOLUCE ---
    elif selected_section_2 == "1.4 Fintech revoluce":
        st.markdown("<div class='sub-section-header'>1. BANKOVNÍ SYSTÉM A PENÍZE V 21. STOLETÍ</div><h2>1.4 Fintech revoluce</h2>", unsafe_allow_html=True)
        st.write("Fintech označuje firmy a služby, které pomocí technologií mění způsob, jak platíme a investujeme.")
