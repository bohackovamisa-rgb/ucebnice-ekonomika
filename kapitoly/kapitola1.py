import streamlit as st
import math

def render():
    st.markdown("<span class='hero-badge'>Kapitola 1</span>", unsafe_allow_html=True)
    st.title("Podnikavost a startupová kultura")
    st.markdown("<p style='font-size: 1rem; color: #64748b; margin-bottom: 1.5rem;'>Od nápadu k odpovědnému podnikání, ověření projektu a výběru právní formy.</p>", unsafe_allow_html=True)

    section_options = [
        "1. Podnikatel a základní pojmy",
        "2. Slovníček základních pojmů",
        "3. OSVČ a živnosti",
        "4. Obchodní korporace",
        "5. Startup: nápad, který hledá funkční byznys",
        "6. Podnikatelský záměr",
        "7. Lean Canvas",
        "8. CSR, etika a odpovědné podnikání",
        "9. Rizika podnikání",
        "10. Švarcsystém",
        "11. Ověřování informací a užitečné zdroje",
        "12. Ukončení podnikání",
        "13. Logická mapa podnikání",
        "14. Reflexe a sebehodnocení",
        "15. Integrované opakování"
    ]
    selected_section = st.selectbox("📌 Přechod na podkapitolu:", section_options, index=0)
    st.divider()

    # --- 1. Podnikatel a základní pojmy ---
    if selected_section == "1. Podnikatel a základní pojmy":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 1</div>", unsafe_allow_html=True)
        st.markdown("## 1. Podnikatel a základní pojmy")
        with st.container(border=True):
            st.write("Zákon chápe podnikání jako soustavnou činnost prováděnou samostatně, vlastním jménem, na vlastní odpovědnost, za účelem dosažení zisku.")
            st.markdown("""<div class='box-gray'><strong>⚖️ Přesná zákonná opora:</strong> Podnikatele definuje zákon č. 89/2012 Sb., občanský zákoník, zejména § 420 odst. 1: <br>„Kdo samostatně vykonává na vlastní účet a odpovědnost výdělečnou činnost živnostenským nebo obdobným způsobem se záměrem činit tak soustavně za účelem dosažení zisku, je považován se zřetelem k této činnosti za podnikatele.“</div>""", unsafe_allow_html=True)
            st.markdown("""<div class='box-blue'><strong>📘 Proč je to důležité:</strong> Zjistíš, kdy se z tvojí aktivity stává podnikání a jaký je rozdíl mezi koníčkem, brigádou, OSVČ a firmou.</div>""", unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 1.2 Čtyři znaky podnikání na praktických příkladech")
            st.markdown("""| Znak podnikání | Co znamená | Příklad ze současnosti |
| :--- | :--- | :--- |
| **Soustavnost** | Činnost se opakuje nebo je plánovaná dlouhodobě. | Každý měsíc prodávám vlastní digitální plánovače. |
| **Samostatnost** | Sám/sama rozhoduji o ceně, zákaznících a způsobu práce. | Nabízím správu sociálních sítí lokálním podnikům. |
| **Vlastní jméno** | Vystupuji vůči zákazníkům a úřadům jako podnikatel. | Mám značku, profil, faktury nebo IČO. |
| **Vlastní odpovědnost**| Nesu riziko ztráty, reklamací a dluhů. | Nakoupím materiál na merch, ale nikdo si ho nekoupí. |""", unsafe_allow_html=True)

    # --- 2. Slovníček základních pojmů ---
    elif selected_section == "2. Slovníček základních pojmů":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2</div><h2>2. Slovníček základních pojmů</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("""| Termín | Co znamená |
| :--- | :--- |
| **Podnikatel** | Osoba, která samostatně vykonává výdělečnou činnost na vlastní účet za účelem zisku. |
| **Fyzická osoba** | Člověk — jednotlivec (např. OSVČ). |
| **Právnická osoba** | Organizovaný subjekt s právní osobností (např. s.r.o., a.s.). |
| **Živnost** | Podnikatelská činnost provozovaná podle živnostenského zákona. |""", unsafe_allow_html=True)

    # --- 3. OSVČ a živnosti ---
    elif selected_section == "3. OSVČ a živnosti":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 3</div><h2>3. OSVČ a živnosti</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("OSVČ znamená osoba samostatně výdělečně činná.")
            st.markdown("""<div class='box-red'><strong>⚠️ Hlavní riziko OSVČ:</strong> OSVČ ručí za závazky z podnikání celým svým osobním majetkem.</div>""", unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 🧮 Kalkulačka hodinové sazby OSVČ")
            col1, col2 = st.columns(2)
            with col1:
                target_net = st.number_input("Cílový čistý měsíční příjem (Kč):", value=35000, step=1000, key="kap1_osvc_net")
                monthly_expenses = st.number_input("Provozní měsíční náklady (Kč):", value=5000, step=500, key="kap1_osvc_exp")
                taxes_insurance = st.number_input("Odhad měsíčních odvodů a daní (Kč):", value=9000, step=500, key="kap1_osvc_tax")
            with col2:
                total_hours = st.number_input("Hodin práce měsíčně:", value=160, step=10, key="kap1_osvc_hrs")
                billable_percent = st.slider("Fakturovatelný čas (%)", 10, 100, 60, 5, key="kap1_osvc_pct")

            if total_hours > 0 and billable_percent > 0:
                total_gross_needed = target_net + monthly_expenses + taxes_insurance
                billable_hours = total_hours * (billable_percent / 100)
                hourly_rate = total_gross_needed / billable_hours
                st.metric("Tvoje minimální hodinová sazba", f"{hourly_rate:,.0f} Kč/h".replace(",", " "))

    # --- 4. Obchodní korporace ---
    elif selected_section == "4. Obchodní korporace":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 4</div><h2>4. Obchodní korporace</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("Obchodní korporace jsou právnické osoby (s.r.o., a.s., v.o.s., k.s., družstva).")

    # --- 5. Startup ---
    elif selected_section == "5. Startup: nápad, který hledá funkční byznys":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 5</div><h2>5. Startup</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("Startup je mladý projekt hledající opakovatelný a škálovatelný byznys model.")

    # --- 6. Podnikatelský záměr ---
    elif selected_section == "6. Podnikatelský záměr":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 6</div><h2>6. Podnikatelský záměr</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("### 🧮 Kalkulačka bodu zvratu")
            col_b1, col_b2 = st.columns(2)
            with col_b1:
                cena = st.number_input("Prodejní cena za kus (Kč):", value=150, key="kap1_bv_cena")
                var_naklad = st.number_input("Variabilní náklad na kus (Kč):", value=80, key="kap1_bv_var")
            with col_b2:
                fix_naklad = st.number_input("Fixní náklady měsíčně (Kč):", value=2800, key="kap1_bv_fix")

            if cena > var_naklad:
                marze = cena - var_naklad
                bod_zvratu = fix_naklad / marze
                st.success(f"**Bod zvratu:** Musíš prodat alespoň **{math.ceil(bod_zvratu)} kusů** měsíčně.")

    # --- Ostatní podkapitoly ---
    else:
        st.markdown(f"<h2>{selected_section}</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write(f"Obsah podkapitoly **{selected_section}** je připraven k procházení.")
