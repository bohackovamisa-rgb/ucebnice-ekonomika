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

    # Sem budeme postupně přidávat další elif pro všechny podkapitoly z tvého Notion!
