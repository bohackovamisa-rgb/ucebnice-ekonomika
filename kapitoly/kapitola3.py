import base64
import math
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

def render():
    st.markdown(
        "<span class='hero-badge'>Kapitola 3</span>", unsafe_allow_html=True
    )
    st.title("3. Výroba, náklady a efektivita")
    st.markdown(
        "<p style='font-size: 1rem; color: #64748b; margin-bottom: 1.5rem;'>"
        "Výroba není jen „něco vyrobit“. Je to práce s náklady, časem, kvalitou a"
        " rozhodováním o tom, co zákazník skutečně považuje za hodnotu.</p>",
        unsafe_allow_html=True,
    )

    with st.container(border=True):
        st.markdown(
            """
        <div class='box-blue'>
            <strong>⚙️ Pointa kapitoly:</strong> V této kapitole se propojí ekonomické počítání s praktickým pohledem na to, jak firma nastavuje cenu, odstraňuje plýtvání a sleduje výkon. Naučíte se rozdíl mezi náklady, výnosy a ziskem a zjistíte, jak zlepšovat procesy bez zbytečného chaosu.
        </div>
        """,
            unsafe_allow_html=True,
        )

    # 📌 PŘEHLED A NAVIGACE KAPITOLOU
    with st.expander(
        "🧭 O čem kapitola je, kde ji využijete a co si z ní odnesete (Rozbalit)", expanded=False
    ):
        c_nav1, c_nav2 = st.columns(2)
        with c_nav1:
            st.markdown("""
            **🎯 Co si z kapitoly odnesete:**
            * 💰 **Náklady, výnosy a zisk:** Rozlišíte základní ekonomické pojmy a pochopíte, proč nejsou zaměnitelné.
            * 🏷️ **Cena jako rozhodnutí:** Pochopíte, proč cena nevzniká jen součtem nákladů, ale i podle hodnoty v očích zákazníka.
            * 🚀 **Štíhlé procesy:** Popíšete princip štíhlé výroby a rozpoznáte základní typy plýtvání.
            * 📊 **KPI a měření výkonu:** Navrhnete jednoduché ukazatele, které skutečně pomáhají při rozhodování.
            """)
            st.markdown(
                """
            <div style="font-size: 0.85rem; color: #64748b; margin-top: 10px;">
                <i>💼 <b>Kde to využijete:</b> Při odhadu ceny produktu, při školním projektu, v podnikatelském záměru i při hodnocení efektivity práce.</i>
            </div>
            """,
                unsafe_allow_html=True,
            )

        with c_nav2:
            st.markdown("""
            **🧭 Doporučené pořadí studia:**
            1. 🏭 **Výrobní proces a organizace výroby** — Nejdřív si ujasníš, co je výroba, jaké má vstupy, typy, kapacitu a jak souvisí s logistikou.
            2. ✅ **Řízení jakosti** — Potom se zaměříš na kvalitu, prevenci chyb, normy, TQM a následky nekvality.
            3. 📉 **Náklady, výnosy a zisk** — Následně projdeš náklady, výdaje, výnosy, příjmy, kalkulace, zisk, ztrátu a bod zvratu.
            4. 📦 **Majetek firmy a zásoby** — Potom navážeš oběžným a dlouhodobým majetkem, evidencí zásob, metodami vyskladňování a moderním řízením skladu.
            5. 🧮 **Kalkulace, ceny a bod zvratu** — Dále propojíš náklady s cenou, cenovou strategií a rozhodováním o objemu výroby.
            6. ⚡ **Efektivita, štíhlá výroba a technologie** — Nakonec projdeš Lean, Kanban, automatizaci, KPI, dashboardy a udržitelnou výrobu.
            7. 🛠️ **Praktická dílna a případové studie** — Na závěr použiješ poznatky v mini projektu a třech modelových situacích.
            """)

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
        "7.2 Závěrečný checklist a prověrka kapitoly",
    ]

    st.markdown(
        "📌 <strong>Přechod na podkapitolu:</strong>", unsafe_allow_html=True
    )
    selected_section_3 = st.selectbox(
        "Přechod na podkapitolu:",
        section_options_3,
        index=0,
        label_visibility="collapsed",
    )
    st.divider()

    # =========================================================================
    # SEKCE 1: VÝROBNÍ PROCES A ORGANIZACE VÝROBY
    # =========================================================================
    if selected_section_3 == "1.1 Výrobní proces a faktory":
        st.markdown("### 1.1 Výrobní proces a výrobní faktory")

        st.markdown(
            """
        <div class='box-blue'>
            🏭 <b>Podstata výroby:</b> Výroba je transformační proces, při kterém firma mění vstupy na výstupy. Zjednodušeně platí: vstupy → technologie → výstupy.
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown("#### Výrobní proces")
        st.write(
            "Výrobní proces zahrnuje všechny činnosti, které vedou ke vzniku"
            " výrobku nebo služby. Firma do procesu vkládá zdroje, používá"
            " určitou technologii a výsledkem je produkt, který má hodnotu pro"
            " zákazníka."
        )
        st.info(
            "📦 **Vstupy** (materiál, práce lidí, stroje, energie, informace, kapitál nebo know-how) "
            "→ ⚙️ **Technologie a práce** "
            "→ 🎁 **Výstupy** (hotové výrobky, služby, polotovary nebo jiné výsledky činnosti firmy)."
        )

        st.divider()
        st.markdown("#### Výrobní faktory")
        st.write("Mezi základní výrobní faktory patří:")
        st.markdown("""
        * 🧑‍🏭 **Lidská práce** — znalosti, dovednosti, čas a výkon pracovníků.
        * 🏗️ **Dlouhodobý majetek** — stroje, budovy, zařízení, výrobní linky nebo software.
        * 📦 **Oběžný majetek** — materiál, zásoby, polotovary, hotové výrobky a peníze.
        * 📊 **Informace** — data, technologické postupy, receptury, plány, objednávky a know-how.
        """)

        st.markdown(
            """
        <div class='box-green'>
            🧠 <b>Důležité:</b> Moderní výroba nestojí jen na strojích a materiálu. Velkou hodnotu mají také informace — například přesná data o objednávkách, kvalitě, zásobách nebo spotřebě energie.
        </div>
        """,
            unsafe_allow_html=True,
        )

    elif selected_section_3 == "1.2 Typy výroby":
        st.markdown("### 1.2 Typy výroby")
        st.write(
            "Výrobu lze rozdělit podle toho, kolik kusů firma vyrábí a jak moc"
            " se jednotlivé výrobky liší. Typ výroby ovlivňuje cenu, organizaci"
            " práce, potřebu zásob, nároky na stroje i způsob kontroly kvality."
        )

        st.markdown(
            """
        | Typ výroby | Charakteristika | Příklad z praxe |
        | :--- | :--- | :--- |
        | 🎨 **Kusová výroba** | Vyrábí se jednotlivé kusy podle konkrétní zakázky. | Nábytek na míru, svatební šaty, prototyp. |
        | 📦 **Sériová výroba** | Vyrábí se menší nebo větší série stejných výrobků. | Limitovaná edice mikin, školní diáře, komponenty. |
        | 🏭 **Hromadná výroba** | Vyrábí se velké množství stejných výrobků. | Nápoje, pečivo, šroubky, běžná elektronika. |
        """,
            unsafe_allow_html=True,
        )

        st.divider()
        st.markdown(
            "<div class='box-yellow'>🧩 <b>Kvíz: O jaký typ výroby"
            " jde?</b></div>",
            unsafe_allow_html=True,
        )

        with st.form("kviz_vyroba"):
            q1 = st.selectbox(
                "1. Nábytek vyrobený přesně podle rozměrů zákazníka:",
                ["Vyber možnost...", "Kusová", "Sériová", "Hromadná"],
                key="k3_1_2_q1",
            )
            q2 = st.selectbox(
                "2. 300 stejných školních mikin:",
                ["Vyber možnost...", "Kusová", "Sériová", "Hromadná"],
                key="k3_1_2_q2",
            )
            q3 = st.selectbox(
                "3. Tisíce rohlíků každý den:",
                ["Vyber možnost...", "Kusová", "Sériová", "Hromadná"],
                key="k3_1_2_q3",
            )

            if st.form_submit_button("Zkontrolovat a uložit odpovědi 💾"):
                if q1 == "Kusová" and q2 == "Sériová" and q3 == "Hromadná":
                    st.success("✅ Perfektní! Chápeš to naprosto přesně.")
                else:
                    st.error(
                        "Něco tam ještě nesedí. Zkus to znovu! Nápověda:"
                        " rohlíky se pečou ve velkém, nábytek na míru je"
                        " unikát."
                    )

                kviz_data = f"1:{q1} | 2:{q2} | 3:{q3}"
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"](
                        "Kapitola 3",
                        "Podkapitola 1.2 - Kvíz Typy výroby",
                        kviz_data,
                    )

    elif selected_section_3 == "1.3 Výrobní kapacita":
        st.markdown("### 1.3 Výrobní kapacita")
        st.write(
            "Výrobní kapacita vyjadřuje maximální možný objem produkce za"
            " určité období. Může jít například o počet kusů za hodinu, směnu,"
            " den nebo měsíc."
        )

        st.markdown(
            "<div class='box-blue'><b>Výrobní kapacita = maximální možný objem"
            " výroby za jednotku času</b></div>",
            unsafe_allow_html=True,
        )

        st.write(
            "Firma se obvykle nesnaží kapacitu využívat za každou cenu na 100"
            " %. Příliš vysoké vytížení může vést k přetížení pracovníků,"
            " poruchám, zmetkům nebo zpoždění zakázek. Cílem je optimální"
            " využití kapacity."
        )

        st.divider()
        st.markdown(
            "<div class='box-yellow'>🧮 <b>Interaktivní model: Tisková farma na"
            " 3D klíčenky</b></div>",
            unsafe_allow_html=True,
        )

        st.write(
            "Představ si, že máš 5 3D tiskáren. Každá zvládne vytisknout"
            " maximálně 10 klíčenek za den. Tvá absolutní denní kapacita je tedy"
            " **50 klíčenek**."
        )
        st.write(
            "Otevřeš svůj e-shop. Kolik objednávek na dnešek zákazníkům"
            " slíbíš dodat?"
        )

        zakazky = st.slider(
            "Skutečná výroba (Počet slíbených zakázek na dnešek):",
            min_value=0,
            max_value=60,
            value=40,
            key="k3_1_3_zakazky",
        )

        vyuziti = (zakazky / 50) * 100

        st.metric("Vytížení tvých tiskáren", f"{vyuziti:.0f} %")

        progress_val = min(vyuziti / 100, 1.0)
        st.progress(progress_val)

        if vyuziti > 100:
            st.error(
                "💥 KRITICKÁ CHYBA: Slíbil jsi víc, než tvé stroje fyzicky"
                " zvládnou! Zákazníci nedostanou zboží včas, dostaneš špatné"
                " recenze."
            )
        elif vyuziti == 100:
            st.warning(
                "⚠️ RIZIKO: Jedeš na absolutní doraz. Pokud se u jediné"
                " tiskárny zasekne struna, nestihneš dodat slíbené kusy!"
            )
        elif vyuziti >= 80:
            st.success(
                "✅ IDEÁLNÍ STAV: Vyděláváš skvělé peníze, ale máš malou"
                " rezervu, kdyby se něco pokazilo."
            )
        elif vyuziti > 0:
            st.info(
                "📉 NEEFEKTIVNÍ: Tiskárny stojí a nevydělávají, i když by"
                " mohly. Platíš fixní náklady, ale máš málo zakázek."
            )
        else:
            st.write("Zatím nemáš žádné objednávky. Stroje leží ladem.")

        if st.button("Uložit nastavení kapacity 💾", key="btn_k3_1_3_kapacita"):
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"](
                    "Kapitola 3",
                    "Podkapitola 1.3 - Výrobní kapacita",
                    f"Slíbené zakázky: {zakazky} ks (Vytížení {vyuziti:.0f}%)",
                )
            st.success("Nastavení kapacity bylo uloženo!")

    elif selected_section_3 == "1.4 Logistika, zásobování a JIT":
        st.markdown("### 1.4 Logistika, zásobování a Just-in-Time")
        st.write(
            "Logistika řeší tok materiálu, výrobků, informací a peněz."
            " Zásobování zajišťuje, aby firma měla správný materiál ve"
            " správném množství, kvalitě, čase a za přijatelnou cenu."
        )

        st.markdown("#### Metoda Just-in-Time (JIT)")
        st.write(
            "Metoda Just-in-Time znamená, že materiál přichází do výroby co nejpozději — ideálně"
            " právě ve chvíli, kdy je potřeba. Cílem je minimalizovat skladové"
            " zásoby."
        )

        col_pro, col_con = st.columns(2)
        with col_pro:
            st.markdown(
                "<div class='box-green'>✅ <b>Výhoda Just-in-Time:</b> Firma"
                " neváže tolik peněz ve skladu a šetří místo.</div>",
                unsafe_allow_html=True,
            )
        with col_con:
            st.markdown(
                "<div class='box-red'>⚠️ <b>Riziko Just-in-Time:</b> Pokud se"
                " dodávka zpozdí, výroba se může rychle zastavit.</div>",
                unsafe_allow_html=True,
            )

        st.divider()
        st.markdown(
            "<div class='box-yellow'>⚖️ <b>Rozhodnutí: Just-in-Time, nebo"
            " pojistná zásoba?</b></div>",
            unsafe_allow_html=True,
        )

        st.write(
            "Jsi manažerem automobilky. Dodávky kritických čipů z Asie jsou"
            " nespolehlivé. Běžné šroubky máš ze železářství vedle závodu. Jaký"
            " systém zásobování zvolíš pro celou firmu?"
        )

        rozhodnuti = st.radio(
            "Vyber strategii:",
            [
                "Vyber...",
                "Vše přes Just-in-Time",
                "Vše držet jako Pojistnou zásobu",
                "Kombinace obojího",
            ],
            key="k3_1_4_rozhodnuti",
        )

        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"](
                "3.1.4",
                f"Tvé zdůvodnění pro strategii ({rozhodnuti}):",
                "3",
                st.session_state.get("ulozene_odpovedi", {}),
            )

        if (
            st.button(
                "Vyhodnotit strategii zásobování 💾",
                key="btn_k3_1_4_logistika",
            )
            and rozhodnuti != "Vyber..."
        ):
            if rozhodnuti == "Kombinace obojího":
                st.success(
                    "Výborně! Kombinace je nejlepší. Šroubky lze brát JIT, ale u"
                    " kritických čipů potřebuješ pojistnou zásobu."
                )
            else:
                st.error(
                    "Toto by v praxi pravděpodobně selhalo. Extrémy nesvědčí."
                    " Zvaž riziko zastavení linky vs. vázání peněz."
                )

    # =========================================================================
    # SEKCE 2: ŘÍZENÍ JAKOSTI
    # =========================================================================
    elif selected_section_3 == "2.1 Řízení jakosti a kvality":
        st.markdown("### 2.1 Řízení jakosti: kvalita ve výrobě")
        st.markdown(
            """
        <div class='box-blue'>
            ✅ <b>Jakost neboli kvalita</b> znamená schopnost výrobku nebo služby splnit požadavky a očekávání zákazníka.
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown("#### Kontrola kvality vs. řízení jakosti")
        st.write(
            "Kontrola kvality se často zaměřuje na odhalení chyb na konci"
            " výroby. Řízení jakosti jde dál: snaží se nastavit celý proces"
            " tak, aby chyby pokud možno vůbec nevznikaly."
        )

        st.markdown(
            """
        | Přístup | Co řeší | Příklad z praxe |
        | :--- | :--- | :--- |
        | 🔍 **Kontrola kvality** | Hledá chyby u hotového výrobku. | Vyřazení zmetků po dokončení výroby. |
        | 🛡️ **Řízení jakosti** | Předchází chybám během procesu. | Standardy práce, školení, Poka-Yoke, průběžné měření. |
        """,
            unsafe_allow_html=True,
        )

        st.divider()
        st.markdown(
            "<div class='box-yellow'>🔍 <b>Kvíz: Jde o kontrolu, nebo"
            " prevenci?</b></div>",
            unsafe_allow_html=True,
        )

        with st.form("kviz_kvalita"):
            k1 = st.radio(
                "Vyřazení vadných výrobků po dokončení:",
                ["Kontrola kvality", "Prevence (Řízení jakosti)"],
                horizontal=True,
                key="k3_2_1_k1",
            )
            k2 = st.radio(
                "Školení pracovníků před výrobou:",
                ["Kontrola kvality", "Prevence (Řízení jakosti)"],
                horizontal=True,
                key="k3_2_1_k2",
            )
            k3 = st.radio(
                "Poka-Yoke (pomůcka znemožňující chybu):",
                ["Kontrola kvality", "Prevence (Řízení jakosti)"],
                horizontal=True,
                key="k3_2_1_k3",
            )
            k4 = st.radio(
                "Měření hotového výrobku před odesláním:",
                ["Kontrola kvality", "Prevence (Řízení jakosti)"],
                horizontal=True,
                key="k3_2_1_k4",
            )

            if st.form_submit_button("Zkontrolovat a uložit 💾"):
                if (
                    k1 == "Kontrola kvality"
                    and k2 == "Prevence (Řízení jakosti)"
                    and k3 == "Prevence (Řízení jakosti)"
                    and k4 == "Kontrola kvality"
                ):
                    st.success(
                        "✅ Výborně! Kontrola řeší problém až když vznikne"
                        " (hotový výrobek). Prevence mu předchází."
                    )
                else:
                    st.error(
                        "Něco je špatně. Pamatuj: Pokud se něco děje až s"
                        " HOTOVÝM výrobkem, je to vždy kontrola."
                    )

                kviz_k_data = f"1:{k1} | 2:{k2} | 3:{k3} | 4:{k4}"
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"](
                        "Kapitola 3",
                        "Podkapitola 2.1 - Kvíz Kontrola vs Prevence",
                        kviz_k_data,
                    )

    elif selected_section_3 == "2.2 Následky nekvality a TQM":
        st.markdown("### 2.2 Normy, TQM a následky nekvality")

        st.markdown("#### Normy a certifikace")
        st.write(
            "Ve firmách se často používají normy a certifikace, které pomáhají"
            " nastavit jednotný systém řízení kvality (např. normy ISO řady"
            " 9000)."
        )
        st.markdown(
            """
        <div class='box-gray'>
            📜 <b>Smysl certifikace:</b> Neznamená automaticky dokonalý výrobek. Znamená, že firma má popsaný a kontrolovaný systém, jak kvalitu řídit a zlepšovat.
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown("#### Total Quality Management (TQM)")
        st.write(
            "Total Quality Management (TQM) je přístup, ve kterém se na"
            " kvalitě podílí celá firma — nejen kontrolor na konci výroby. Do"
            " zlepšování se zapojují pracovníci výroby, vedení, obchod, nákup i"
            " zákaznická podpora."
        )
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
        st.write(
            "Nekvalita není jen technický problém. Má přímé ekonomické dopady."
            " Může způsobit: reklamace, vrácení zboží, dodatečné opravy, vyšší"
            " náklady, zpoždění zakázek, ztrátu zákazníků a poškození dobrého"
            " jména firmy (goodwill)."
        )

        st.markdown(
            """
        <div class='box-red'>
            ⚠️ <b>Ekonomická pointa:</b> Nekvalitní výrobek může být dražší než poctivá prevence. Firma zaplatí materiál, práci i opravy — a navíc může přijít o důvěru zákazníka.
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.divider()
        st.markdown(
            "<div class='box-yellow'>🧮 <b>Kalkulačka nákladů na"
            " zmetky</b></div>",
            unsafe_allow_html=True,
        )

        c1, c2 = st.columns(2)
        with c1:
            vyrobeno_ks = st.number_input(
                "Celkový počet vyrobených kusů:",
                min_value=1,
                value=1000,
                step=100,
                key="k3_2_2_vyrobeno",
            )
            chybovost_pct = st.slider(
                "Chybovost výroby (%)",
                min_value=0.0,
                max_value=20.0,
                value=3.0,
                step=0.5,
                key="k3_2_2_chybovost",
            )
            naklad_ks = st.number_input(
                "Náklad na 1 vadný kus (Kč):",
                min_value=1,
                value=500,
                step=50,
                key="k3_2_2_naklad",
            )

        vadne_ks = int(vyrobeno_ks * (chybovost_pct / 100))
        ztrata_kc = vadne_ks * naklad_ks

        with c2:
            st.metric("Počet vadných kusů (zmetků)", f"{vadne_ks} ks")
            st.metric(
                "Finanční ztráta z výroby zmetků",
                f"{ztrata_kc:,} Kč".replace(",", " "),
            )

            if ztrata_kc > 0:
                st.info(
                    f"O tuto částku ({ztrata_kc:,} Kč) firma přišla kvůli špatné"
                    " kvalitě. Prevence by byla pravděpodobně levnější."
                )

        if st.button("Uložit výpočet ztráty zmetků 💾", key="btn_k3_2_2_zmetky"):
            zmetky_data = (
                f"Vyrobeno: {vyrobeno_ks} ks | Chybovost: {chybovost_pct}% |"
                f" Vadné: {vadne_ks} ks | Ztráta: {ztrata_kc} Kč"
            )
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"](
                    "Kapitola 3",
                    "Podkapitola 2.2 - Náklady na zmetky",
                    zmetky_data,
                )
            st.success("Výpočet ztráty byl uložen!")

    # =========================================================================
    # SEKCE 3: NÁKLADY, VÝNOSY A ZISK
    # =========================================================================
    elif selected_section_3 == "3.1 Náklad vs. výdaj a pojetí zisku":
        st.markdown("### 3.1 Náklady, výnosy a zisk: základní teorie")
        
        st.write(
            "Náklady vyjadřují spotřebu zdrojů potřebných k výrobě nebo poskytování služby. Může jít o materiál, mzdy, energie, nájem, odpisy strojů, dopravu, marketing nebo služby dodavatelů.\n\n"
            "Výnosy jsou peněžně vyjádřené výsledky činnosti firmy — nejčastěji tržby za prodané výrobky nebo služby."
        )

        st.markdown(
            """
        <div class='box-blue'>
            🧮 <b>Základní vztah:</b> Zisk vzniká tehdy, když jsou výnosy vyšší než náklady. Důležité je ale vědět, které náklady do výpočtu opravdu patří.<br><br>
            <b>Základní vzorec:</b> Zisk = výnosy − náklady<br>
            Pokud jsou náklady vyšší než výnosy, firma je ve ztrátě. Ztráta = náklady − výnosy
        </div>
        """,
            unsafe_allow_html=True,
        )

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Náklad vs. Výdaj")
            st.write(
                "V běžné řeči se často zaměňují, ale v ekonomice a účetnictví"
                " mají odlišný význam."
            )
            st.markdown("""
            * **Náklad:** Spotřeba zdrojů vyjádřená v penězích (např. spotřeba materiálu ve výrobě, mzda za odvedenou práci, odpis stroje).
            * **Výdaj:** Skutečný odtok peněz z pokladny nebo bankovního účtu (např. zaplacení faktury dodavateli, nákup materiálu, úhrada nájmu).
            """)
            st.markdown(
                "<div class='box-gray'>💡 <b>Příklad:</b> Firma koupí stroj"
                " za 240 000 Kč. Peníze odejdou z účtu hned — to je výdaj. Do"
                " nákladů se ale stroj dostává postupně pomocí odpisů.</div>",
                unsafe_allow_html=True,
            )

        with col2:
            st.markdown("#### Výnos vs. Příjem")
            st.write("Podobně je potřeba rozlišovat výnos a příjem.")
            st.markdown("""
            * **Výnos:** Peněžně vyjádřený výkon firmy, vznik nároku na zaplacení (např. vystavená faktura za prodané výrobky).
            * **Příjem:** Skutečný přítok peněz do pokladny nebo na bankovní účet (např. zákazník fakturu opravdu zaplatí).
            """)
            st.markdown(
                "<div class='box-gray'>🧾 <b>Důležité:</b> Firma může mít"
                " výnos už při vystavení faktury, ale příjem vznikne až ve"
                " chvíli, kdy zákazník zaplatí.</div>",
                unsafe_allow_html=True,
            )
            
        st.divider()
        st.markdown(
            "<div class='box-yellow'>📝 <b>Kvíz: náklad/výdaj a výnos/příjem</b></div>",
            unsafe_allow_html=True,
        )
        with st.form("kviz_naklady"):
            q1 = st.radio("1. Zaplacení faktury dodavateli:", ["Vyber...", "výdaj", "náklad", "výnos", "příjem"], key="q1_3_1", horizontal=True)
            q2 = st.radio("2. Spotřeba materiálu ve výrobě:", ["Vyber...", "výdaj", "náklad", "výnos", "příjem"], key="q2_3_1", horizontal=True)
            q3 = st.radio("3. Vystavená faktura zákazníkovi:", ["Vyber...", "výdaj", "náklad", "výnos", "příjem"], key="q3_3_1", horizontal=True)
            q4 = st.radio("4. Peníze přijaté na účet:", ["Vyber...", "výdaj", "náklad", "výnos", "příjem"], key="q4_3_1", horizontal=True)
            
            if st.form_submit_button("Zkontrolovat a uložit 💾"):
                if q1 == "výdaj" and q2 == "náklad" and q3 == "výnos" and q4 == "příjem":
                    st.success("✅ Perfektní! Máš v pojmech naprosté jasno.")
                else:
                    st.error("Něco se nepovedlo. Zkus to znovu a pamatuj: Výdaj/Příjem řeší pohyb peněz, Náklad/Výnos řeší spotřebu/výkon bez ohledu na to, kdy se platilo.")
                
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"](
                        "Kapitola 3",
                        "Podkapitola 3.1 - Kvíz Náklady",
                        f"1:{q1}, 2:{q2}, 3:{q3}, 4:{q4}",
                    )

        st.divider()
        st.markdown("#### Tři pohledy na zisk")
        st.markdown("**1. Účetní pohled na zisk**")
        st.write(
            "Z účetního pohledu se zisk počítá jako rozdíl mezi účetními výnosy"
            " a účetními náklady za určité období. Vychází z pravidel"
            " účetnictví a zachycuje tržby, mzdy, nájem, energie, odpisy, úroky, daně."
            " Odpovídá na otázku: *Kolik firma podle účetnictví vydělala nebo prodělala?*"
        )

        st.markdown("**2. Pohled finanční analýzy a finančního řízení**")
        st.write(
            "Finanční analýza se nezajímá jen o to, zda firma vykázala zisk. Sleduje také, zda je firma dlouhodobě zdravá, stabilní a schopná platit své závazky. "
            "Finanční řízení řeší například, zda má firma dostatek peněz na provoz, zda není příliš zadlužená, zda se jí vyplatí investovat do nového stroje, "
            "zda je cena výrobku nastavena správně nebo zda firma vydělává dostatečně vzhledem k riziku. "
            "**Důležité:** Zisk a peníze na účtu nejsou totéž. Firma může vykázat zisk, ale zároveň mít problém s hotovostí (pokud jí zákazníci neplatí včas)."
        )

        st.markdown("**3. Ekonomický zisk**")
        st.write(
            "Ekonomický zisk jde dál než účetní zisk. Zohledňuje nejen skutečně zaplacené (explicitní) náklady, ale také tzv. implicitní "
            "(alternativní) náklady — tedy hodnotu nejlepší nevyužité příležitosti. Ukazuje, zda se podnikání vyplatí i ve srovnání s jinými možnostmi využití peněz, času a práce."
        )
        st.markdown(
            "<div class='box-green'>🧠 <b>Příklad:</b> Pokud podnikatel vloží"
            " do podnikání vlastní peníze, mohl je místo toho investovat"
            " jinam (ušlý úrok). Pokud sám pracuje ve firmě, přichází o možnou mzdu jinde. Ušlý výnos z této jiné možnosti je alternativní náklad.</div>",
            unsafe_allow_html=True,
        )

        st.divider()
        st.markdown(
            "<div class='box-yellow'>🧮 <b>Kalkulačka: Účetní vs. Ekonomický"
            " zisk</b></div>",
            unsafe_allow_html=True,
        )
        st.write(
            "Spočítej si, jestli se ti podnikání vyplatí víc, než kdybys šel"
            " do zaměstnání a peníze dal do banky."
        )

        c_in, c_out = st.columns([1, 1])
        with c_in:
            vynosy = st.number_input(
                "Celkové roční výnosy (tržby):",
                value=1500000,
                step=100000,
                key="k3_3_1_vynosy",
            )
            exp_naklady = st.number_input(
                "Explicitní náklady (materiál, nájem atd.):",
                value=900000,
                step=50000,
                key="k3_3_1_exp_naklady",
            )
            st.markdown("*Alternativní (implicitní) náklady:*")
            usla_mzda = st.number_input(
                "Ušlá čistá mzda (kdybys pracoval pro jiného):",
                value=480000,
                step=20000,
                key="k3_3_1_usla_mzda",
            )
            usly_urok = st.number_input(
                "Ušlý úrok (kdybys peníze investoval jinam):",
                value=50000,
                step=10000,
                key="k3_3_1_usly_urok",
            )

        with c_out:
            ucetni_zisk = vynosy - exp_naklady
            eko_zisk = ucetni_zisk - usla_mzda - usly_urok

            st.metric(
                "Účetní zisk (Papírový zisk)",
                f"{ucetni_zisk:,} Kč".replace(",", " "),
            )
            st.metric(
                "Ekonomický zisk", f"{eko_zisk:,} Kč".replace(",", " ")
            )

            if eko_zisk > 0:
                st.success(
                    "✅ Podnikání se ti vyplatí! Vyděláváš víc, než kdybys"
                    " chodil do práce a peníze měl v bance."
                )
            else:
                st.error(
                    "⚠️ Ekonomická ztráta! Z účetního pohledu jsi možná v"
                    " plusu, ale ve skutečnosti by se ti víc vyplatilo jít do"
                    " běžného zaměstnání."
                )

        if st.button(
            "Uložit výpočet ekonomického zisku 💾", key="btn_k3_3_1_zisk"
        ):
            zisk_data = (
                f"Tržby: {vynosy} | Exp. náklady: {exp_naklady} | Účetní zisk:"
                f" {ucetni_zisk} | Eko zisk: {eko_zisk}"
            )
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"](
                    "Kapitola 3",
                    "Podkapitola 3.1 - Účetní vs Ekonomický zisk",
                    zisk_data,
                )
            st.success("Výpočet byl uložen!")

    elif selected_section_3 == "3.2 Členění nákladů a kalkulační vzorec":
        st.markdown("### 3.2 Členění nákladů a kalkulační vzorec")

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("#### Fixní a variabilní náklady")
            st.write("Náklady můžeme rozdělit podle toho, zda se mění s objemem výroby. Celkové náklady = fixní + variabilní.")
            st.markdown("""
            * 🔒 **Fixní náklady:** Nemění se přímo s počtem vyrobených kusů (nájem, pojištění, mzda administrativy, odpis stroje).
            * 📈 **Variabilní náklady:** Rostou nebo klesají podle objemu výroby (materiál, obaly, přímé mzdy, energie na výrobu).
            """)
            with st.expander("🛠️ Jak lze snižovat variabilní náklady?"):
                st.write(
                    "Variabilní náklady se snižují hlavně zlepšením spotřeby zdrojů na jeden kus výrobku nebo služby. "
                    "Možné postupy: vyjednat lepší cenu materiálu, hledat vhodnější dodavatele, snížit zmetkovitost a reklamace, "
                    "lépe plánovat výrobu, omezit plýtvání materiálem, zkrátit čas potřebný na výrobu jednoho kusu, zlepšit technologický postup, "
                    "využívat množstevní slevy, standardizovat obaly či komponenty."
                )
            with st.expander("🛠️ Jak lze snižovat fixní náklady?"):
                st.write(
                    "Fixní náklady se snižují obtížněji, protože vznikají i tehdy, když firma vyrábí málo nebo vůbec. "
                    "Možné postupy: přestěhovat se do levnějších prostor, sdílet kanceláře/sklady, pronajímat stroje místo nákupu, "
                    "automatizovat opakující se administrativu, lépe využít kapacitu strojů, omezit zbytečné služby, outsourcovat činnosti."
                    "\n\n**Pozor:** Snižování nákladů nesmí automaticky znamenat zhoršení kvality. Pokud firma ušetří tak, že zákazník ztratí důvěru, může se jí úspora prodražit."
                )

        with c2:
            st.markdown("#### Přímé a nepřímé náklady")
            st.write(
                "Při sestavování ceny je důležité rozlišit, které náklady lze přiřadit přímo ke konkrétnímu výrobku a které jsou společné."
            )
            st.markdown("""
            * 🎯 **Přímé náklady:** Lze je přesně určit na jeden kus, zakázku nebo službu (materiál na jedno tričko, obal, potisk, přímá mzda).
            * 🌫️ **Nepřímé náklady:** Jsou společné pro více výrobků nebo celou firmu a musí se rozpočítat (nájem dílny, účetnictví, marketing, energie provozovny).
            """)
            st.info(
                "Nepřímé náklady se často rozpočítávají pomocí režijní přirážky: "
                "Režijní přirážka = režijní náklady / zvolená rozvrhová"
                " základna × 100"
            )

        st.divider()
        st.markdown("#### Kalkulační vzorec")
        st.write(
            "Kalkulační vzorec pomáhá firmě sestavit cenu tak, aby pokryla"
            " nejen materiál a práci, ale také režii, prodejní náklady a umožnila zisk. Vyzkoušej si to:"
        )

        st.markdown(
            "<div class='box-yellow'>🧮 <b>Interaktivní sestavení prodejní"
            " ceny</b></div>",
            unsafe_allow_html=True,
        )

        k_in, k_out = st.columns([1, 1])
        with k_in:
            mat = st.number_input(
                "Přímý materiál (Kč):", value=150, step=10, key="k3_3_2_mat"
            )
            mzdy = st.number_input(
                "Přímé mzdy (Kč):", value=100, step=10, key="k3_3_2_mzdy"
            )
            ostatni_prime = st.number_input(
                "Ostatní přímé náklady (Kč):", value=20, step=10, key="k3_3_2_ost"
            )
            v_rezie = st.number_input(
                "Výrobní režie (Kč):", value=50, step=10, key="k3_3_2_vrezie"
            )
            s_rezie = st.number_input(
                "Správní režie (Kč):", value=30, step=10, key="k3_3_2_srezie"
            )
            o_naklady = st.number_input(
                "Odbytové náklady (marketing, prodej) (Kč):",
                value=20,
                step=10,
                key="k3_3_2_onaklady",
            )
            zisk_prirazka = st.slider(
                "Zisková přirážka (%)",
                min_value=0,
                max_value=100,
                value=20,
                key="k3_3_2_zisk",
            )

        with k_out:
            vn_vyroby = mat + mzdy + ostatni_prime + v_rezie
            vn_vykonu = vn_vyroby + s_rezie
            uplne_vn = vn_vykonu + o_naklady
            zisk_kc = uplne_vn * (zisk_prirazka / 100)
            cena_bez_dph = uplne_vn + zisk_kc

            st.markdown(f"**Vlastní náklady výroby:** {vn_vyroby} Kč")
            st.markdown(f"**Vlastní náklady výkonu:** {vn_vykonu} Kč")
            st.markdown(f"**Úplné vlastní náklady výkonu:** {uplne_vn} Kč")
            st.markdown(f"**Zisk ({zisk_prirazka} %):** + {zisk_kc:.1f} Kč")
            st.markdown(
                "<h3 style='color: #4f46e5; margin-top: 10px;'>Prodejní cena"
                f" bez DPH: {cena_bez_dph:.1f} Kč</h3>",
                unsafe_allow_html=True,
            )

        if st.button("Uložit kalkulaci ceny 💾", key="btn_k3_3_2_cena"):
            kalk_data = (
                f"Materiál: {mat} | Mzdy: {mzdy} | Úplné náklady: {uplne_vn} Kč"
                f" | Výsledná cena bez DPH: {cena_bez_dph:.1f} Kč"
            )
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"](
                    "Kapitola 3",
                    "Podkapitola 3.2 - Kalkulační vzorec",
                    kalk_data,
                )
            st.success("Kalkulace ceny byla uložena!")

    elif selected_section_3 == "3.3 Kalkulace nákladů":
        st.markdown("### 3.3 Kalkulace nákladů")
        st.write(
            "Kalkulace nákladů je postup, kterým firma zjišťuje, kolik ji stojí jeden"
            " výrobek, služba, zakázka nebo projekt."
        )
        st.write("Kalkulace pomáhá odpovědět například na otázky:")
        st.markdown("""
        * Kolik stojí výroba jednoho kusu?
        * Za jakou cenu můžeme výrobek prodávat?
        * Který produkt je výhodnější?
        * Kde vznikají největší náklady?
        * Vyplatí se zakázku přijmout?
        * Kolik kusů musíme prodat, aby se podnikání vyplatilo?
        """)

        st.markdown("#### Kalkulace úplných nákladů")
        st.write(
            "Zahrnuje všechny náklady, které s výrobkem nebo službou souvisejí"
            " — přímé i nepřímé. Nepřímé náklady (nájem, energie) se rozpočítávají pomocí zvolené rozvrhové základny."
        )
        st.markdown(
            "<div class='box-gray'><b>Úplné vlastní náklady = přímé náklady +"
            " podíl nepřímých nákladů</b></div>",
            unsafe_allow_html=True,
        )
        st.markdown(
            """
        <div class='box-blue'>
            📊 <b>Výhoda:</b> Ukazuje celkové náklady výrobku.<br>
            ⚠️ <b>Nevýhoda:</b> Rozpočítání nepřímých nákladů může být nepřesné a závisí na zvolené metodě.
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown("#### Kalkulace neúplných nákladů (Krycí příspěvek)")
        st.write(
            "Kalkulace neúplných nákladů pracuje jen s částí nákladů — často s variabilními náklady. "
            "Fixní náklady se neposuzují na každý kus zvlášť, ale sledují se za firmu jako celek. "
            "Je užitečná při rozhodování, zda přijmout zakázku, jak nastavit cenu nebo jak posoudit bod zvratu."
        )
        st.markdown(
            "<div class='box-gray'><b>Příspěvek na úhradu na kus = prodejní cena"
            " za kus − variabilní náklady na kus</b></div>",
            unsafe_allow_html=True,
        )
        st.write(
            "Příspěvek na úhradu říká, kolik z ceny jednoho prodaného kusu zbývá na úhradu fixních nákladů a tvorbu zisku. "
            "Celkový příspěvek na úhradu = příspěvek na úhradu na kus × počet prodaných kusů."
        )

        st.divider()
        st.markdown(
            "<div class='box-yellow'>🧮 <b>Kalkulačka příspěvku na"
            " úhradu</b></div>",
            unsafe_allow_html=True,
        )

        col_in, col_out = st.columns(2)
        with col_in:
            cena_ks = st.number_input(
                "Prodejní cena za 1 kus (Kč):", value=800, key="k3_3_3_cena"
            )
            var_ks = st.number_input(
                "Variabilní náklady na 1 kus (Kč):", value=350, key="k3_3_3_var"
            )
            prodano_ks = st.number_input(
                "Očekávaný prodej (ks):", value=500, key="k3_3_3_prodano"
            )

        with col_out:
            prispevek_ks = cena_ks - var_ks
            prispevek_celkem = prispevek_ks * prodano_ks

            st.metric("Příspěvek na úhradu (1 kus)", f"{prispevek_ks} Kč")
            st.metric(
                "Celkový příspěvek na úhradu",
                f"{prispevek_celkem:,} Kč".replace(",", " "),
            )
            st.info(
                f"Z této částky {prispevek_celkem:,} Kč musí firma nejprve"
                " zaplatit všechny své fixní náklady (nájem, energie). Cokoliv"
                " zbyde, je čistý zisk."
            )

        if st.button(
            "Uložit výpočet příspěvku na úhradu 💾",
            key="btn_k3_3_3_prispevek",
        ):
            prispevek_data = (
                f"Cena/ks: {cena_ks} | Var. náklady/ks: {var_ks} |"
                f" Příspěvek/ks: {prispevek_ks} Kč | Celkem příspěvek:"
                f" {prispevek_celkem} Kč"
            )
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"](
                    "Kapitola 3",
                    "Podkapitola 3.3 - Příspěvek na úhradu",
                    prispevek_data,
                )
            st.success("Příspěvek na úhradu byl uložen!")

    elif selected_section_3 == "3.4 Bod zvratu a jeho graf":
        st.markdown("### 3.4 Bod zvratu a postup sestavení kalkulace")

        st.markdown("#### Bod zvratu (Break-even point)")
        st.write(
            "Bod zvratu je objem výroby nebo prodeje, při kterém firma nemá ani"
            " zisk, ani ztrátu. Výnosy se právě rovnají nákladům."
        )
        st.markdown(
            "<div class='box-gray'><b>Bod zvratu v kusech = fixní náklady /"
            " (cena za kus − variabilní náklady na kus)</b></div>",
            unsafe_allow_html=True,
        )
        st.write("Výraz v závorce je vlastně *příspěvek na úhradu na kus*.")

        st.divider()
        st.markdown(
            "<div class='box-purple'>🕹️ <b>Simulátor Bodu Zvratu s Křivkou"
            " zisku</b></div>",
            unsafe_allow_html=True,
        )

        col_in, col_out = st.columns([1, 1.2])
        with col_in:
            be_fix = st.number_input(
                "Fixní náklady za období (Kč):",
                value=30000,
                step=1000,
                key="k3_3_4_fix",
            )
            be_cena = st.number_input(
                "Prodejní cena kusu (Kč):",
                value=1000,
                step=100,
                key="k3_3_4_cena",
            )
            be_var = st.number_input(
                "Variabilní náklad kusu (Kč):",
                value=400,
                step=100,
                key="k3_3_4_var",
            )

        with col_out:
            prispevek = be_cena - be_var
            if prispevek <= 0:
                st.error(
                    "Chyba: Tvá cena nepokryje variabilní náklady. Bod zvratu"
                    " neexistuje."
                )
            else:
                bod_zvratu = math.ceil(be_fix / prispevek)
                st.metric("Bod zvratu (musíš prodat)", f"{bod_zvratu} kusů")
                st.success(
                    f"Při prodeji {bod_zvratu} kusů jsi na nule. Každý další"
                    f" kus = čistý zisk {prispevek} Kč."
                )

        if st.button("Uložit výpočet Bodu zvratu 💾", key="btn_k3_3_4_bep"):
            if prispevek > 0:
                bep_data = (
                    f"Fixní: {be_fix} | Cena: {be_cena} | Var: {be_var} | Bod"
                    f" zvratu: {bod_zvratu} ks"
                )
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"](
                        "Kapitola 3", "Podkapitola 3.4 - Bod zvratu", bep_data
                    )
                st.success("Bod zvratu byl uložen!")

        if prispevek > 0:
            try:
                import pandas as pd

                max_x = int(bod_zvratu * 2.5) if bod_zvratu > 0 else 100
                kroky = max(1, max_x // 50)
                df_graf = pd.DataFrame({"Kusy": range(0, max_x, kroky)})

                df_graf["Tržby (Výnosy)"] = df_graf["Kusy"] * be_cena
                df_graf["Celkové náklady"] = be_fix + (
                    df_graf["Kusy"] * be_var
                )
                df_graf["Fixní náklady"] = be_fix
                df_graf["Variabilní náklady"] = df_graf["Kusy"] * be_var

                df_graf = df_graf.set_index("Kusy")

                # Colors matching the theoretical description in Notion
                st.line_chart(
                    df_graf[["Tržby (Výnosy)", "Celkové náklady", "Fixní náklady", "Variabilní náklady"]],
                    color=["#3b82f6", "#ef4444", "#ec4899", "#22c55e"] # Blue, Red, Pink, Green
                )
                st.markdown(
                    "<p style='font-size: 0.9em; color: #64748b;'><b>Jak graf číst:</b> Modrá přímka znázorňuje celkové tržby, "
                    "červená přímka celkové náklady, růžová vodorovná čára fixní náklady a zelená přímka variabilní náklady. "
                    "Bod zvratu je místo, kde se celkové tržby protínají s celkovými náklady.</p>",
                    unsafe_allow_html=True,
                )
            except ImportError:
                st.warning("Graf vyžaduje knihovnu Pandas.")

        st.divider()
        st.markdown("#### Postup sestavení kalkulace")
        st.write(
            "Při sestavování kalkulace je důležité postupovat systematicky. Zde je 8 kroků:"
        )
        st.markdown("""
        1. **Určit předmět kalkulace:** Co počítáme? Jeden výrobek, službu, zakázku, projekt nebo zákazníka?
        2. **Vymezit období nebo objem výroby:** Počítáme náklady na jeden kus, měsíc, rok nebo konkrétní zakázku?
        3. **Sepsat přímé náklady:** Materiál, přímé mzdy, obaly, doprava ke konkrétní zakázce.
        4. **Určit nepřímé náklady:** Nájem, energie, administrativa, odpisy, marketing, účetnictví.
        5. **Zvolit způsob rozvržení nepřímých nákladů:** Například podle počtu kusů, hodin práce, strojových hodin nebo přímých mezd.
        6. **Spočítat náklady na jednotku:** Celkové náklady se převedou na jeden výrobek nebo službu.
        7. **Porovnat náklady s cenou:** Firma zjistí, zda cena pokryje náklady a umožní zisk.
        8. **Vyhodnotit výsledek:** Pokud je zisk nízký nebo záporný, firma hledá možnosti úprav ceny, nákladů nebo procesu.
        """)

    elif selected_section_3 == "3.5 Měření výkonu a rentabilita":
        st.markdown("### 3.5 Jak měřit výkon firmy a rentabilita")
        st.write(
            "Výkon firmy nelze hodnotit jen podle toho, zda „něco vydělala“."
            " Důležité je sledovat více ukazatelů, protože každý ukazuje jinou"
            " část reality."
        )

        st.markdown(
            """
        | Oblast | Ukazatel (KPI) | Co říká |
        | :--- | :--- | :--- |
        | 💰 **Ziskovost** | Zisk, zisková marže, rentabilita tržeb | Zda firma vydělává. |
        | 📉 **Náklady** | Náklady na kus, podíl fixních nákladů, var. náklady na kus | Jak efektivně firma vyrábí. |
        | 🧑‍🏭 **Produktivita** | Výkon na pracovníka, kusy za hodinu, tržby na zaměstnance | Jak dobře firma využívá práci. |
        | 💧 **Likvidita** | Schopnost platit závazky | Zda má firma dostatek peněz. |
        | ⚖️ **Zadluženost** | Podíl cizích zdrojů | Jak moc je firma závislá na dluhu. |
        | 🛡️ **Kvalita** | Počet reklamací, zmetkovitost, spokojenost zákazníků | Zda výkon není dosažen na úkor kvality. |
        | 🚀 **Růst** | Růst tržeb, počet zákazníků, opakované nákupy | Zda se firmě daří rozvíjet. |
        """,
            unsafe_allow_html=True,
        )
        
        st.write("**Vybrané vzorce:**")
        st.markdown("""
        * **Zisková marže** = zisk / tržby × 100
        * **Náklady na kus** = celkové náklady / počet vyrobených kusů
        * **Produktivita práce** = výstup / počet pracovníků
        * **Rentabilita tržeb** = zisk / tržby × 100
        """)

        st.markdown(
            "<div class='box-green'>🎯 <b>Pravidlo KPI:</b> Dobré KPI má"
            " pomáhat rozhodování. Pokud ukazatel nikdo nepoužívá k"
            " rozhodnutí, je to spíš číslo do tabulky než skutečný nástroj"
            " řízení.</div>",
            unsafe_allow_html=True,
        )

        st.divider()
        st.markdown("#### Rentabilita")
        st.write(
            "Rentabilita ukazuje, jak výnosně firma využívá své náklady, tržby"
            " nebo kapitál. Vyjadřuje se obvykle v procentech."
        )
        st.markdown("""
        * **Rentabilita nákladů** = Zisk / Náklady × 100
        * **Rentabilita tržeb** = Zisk / Tržby × 100
        * **Rentabilita kapitálu** = Zisk / Vložený kapitál × 100
        """)
        st.info("**Interpretace:** Čím vyšší rentabilita, tím lépe firma dokáže z vložených prostředků vytvářet zisk. Samotné procento je ale potřeba porovnávat s oborem, rizikem a dlouhodobým vývojem.")

        st.divider()
        st.markdown(
            "<div class='box-yellow'>🧮 <b>Dashboard výkonu firmy (KPI"
            " kalkulačka)</b></div>",
            unsafe_allow_html=True,
        )

        rc1, rc2 = st.columns(2)
        with rc1:
            k_trzby = st.number_input(
                "Tržby celkem (Kč):",
                value=2000000,
                step=100000,
                key="k3_3_5_trzby",
            )
            k_naklady = st.number_input(
                "Náklady celkem (Kč):",
                value=1600000,
                step=100000,
                key="k3_3_5_naklady",
            )
            k_pracovnici = st.number_input(
                "Počet pracovníků:", value=5, min_value=1, key="k3_3_5_pracovnici"
            )
            k_kusy = st.number_input(
                "Počet vyrobených kusů:",
                value=10000,
                step=1000,
                key="k3_3_5_kusy",
            )

        with rc2:
            k_zisk = k_trzby - k_naklady
            rent_trzeb = (k_zisk / k_trzby) * 100 if k_trzby > 0 else 0
            prod_ks = k_kusy / k_pracovnici
            naklad_na_kus = k_naklady / k_kusy if k_kusy > 0 else 0

            st.metric("Zisk firmy", f"{k_zisk:,} Kč".replace(",", " "))
            st.metric("Rentabilita tržeb (Marže)", f"{rent_trzeb:.1f} %")
            st.metric(
                "Produktivita (ks na 1 pracovníka)",
                f"{prod_ks:,.0f} ks".replace(",", " "),
            )
            st.metric(
                "Náklad na 1 kus", f"{naklad_na_kus:,.1f} Kč".replace(",", " ")
            )

            if rent_trzeb < 0:
                st.error("Firma je ve ztrátě. Hodnota rentability je záporná.")
            elif rent_trzeb < 10:
                st.warning("Pozor, rentabilita je nízká (pod 10 %).")
            else:
                st.success("Skvělá práce, rentabilita i výkonnost jsou zdravé.")

        if st.button("Uložit výpočet KPI dashboardu 💾", key="btn_k3_3_5_kpi"):
            kpi_data = (
                f"Zisk: {k_zisk} | Marže: {rent_trzeb:.1f}% | Prod/pracovník:"
                f" {prod_ks:.0f} ks | Náklad/ks: {naklad_na_kus:.1f} Kč"
            )
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"](
                    "Kapitola 3",
                    "Podkapitola 3.5 - Dashboard KPI",
                    kpi_data,
                )
            st.success("KPI dashboard byl uložen!")

    # =========================================================================
    # SEKCE 4: MAJETEK FIRMY
    # =========================================================================
    elif selected_section_3 == "4.1 Oběžný majetek a plánování zásob":
        st.markdown("### 4.1 Oběžný majetek a plánování zásob")

        st.markdown(
            """
        <div class='box-blue'>
            🏢 <b>Podstata majetku:</b> Majetek firmy představuje vše, co firma používá ke své činnosti. Část majetku se ve firmě rychle spotřebuje nebo přemění na peníze, jiná část slouží dlouhodobě. Dělí se na <b>oběžný</b> a <b>dlouhodobý</b> majetek.
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown("#### Oběžný majetek")
        st.write(
            "Oběžný majetek je majetek, který se při činnosti firmy rychle"
            " mění. Typicky se spotřebuje, prodá, přemění na hotové výrobky"
            " nebo na peníze."
        )
        st.write(
            "Patří sem například: zásoby materiálu, nedokončená výroba, hotové"
            " výrobky, zboží, krátkodobé pohledávky, peníze v hotovosti a na"
            " bankovním účtu."
        )
        st.info("🔄 **Oběžný majetek „obíhá“ firmou:** Peníze se použijí na nákup materiálu, materiál se změní ve výrobek, výrobek se prodá a zpět do firmy se vrátí peníze.")

        st.markdown("#### Plánování materiálu")
        st.write(
            "Plánování materiálu znamená určit, kolik materiálu bude firma"
            " potřebovat, kdy ho má objednat a jak velkou zásobu má držet na"
            " skladě. Firma musí hlídat dvě rizika:"
        )
        st.markdown("""
        * ❌ **Příliš nízká zásoba:** výroba se může zastavit, protože chybí materiál.
        * ❌ **Příliš vysoká zásoba:** firma má peníze zbytečně vázané ve skladu.
        """)
        st.write("**Při plánování materiálu se sleduje:**")
        st.markdown("""
        - plánovaný objem výroby,
        - spotřeba materiálu na jeden výrobek,
        - dodací lhůta dodavatele,
        - minimální zásoba,
        - pojistná zásoba,
        - skladovací náklady,
        - riziko znehodnocení nebo zastarání materiálu.
        """)

        st.markdown("#### Stanovení optimální zásoby a druhy zásob")
        st.write("**Optimální zásoba** je taková zásoba, která umožňuje plynulou výrobu, ale zároveň zbytečně neváže peníze a nezvyšuje skladovací náklady. **Cíl:** Najít rovnováhu mezi bezpečností výroby a náklady na skladování.")

        st.markdown("""
        | Druh zásoby | Význam |
        | :--- | :--- |
        | **Běžná zásoba** | Slouží k pravidelné spotřebě mezi dvěma dodávkami. |
        | **Pojistná zásoba** | Chrání firmu před zpožděním dodávky nebo nečekanou spotřebou. |
        | **Minimální zásoba** | Nejnižší stav zásoby, pod který by firma neměla klesnout. |
        | **Maximální zásoba** | Nejvyšší stav zásoby, který ještě dává ekonomický smysl. |
        """)
        
        st.markdown("Vzorce pro výpočet:")
        st.markdown("""
        * **Průměrná zásoba** = (počáteční zásoba + konečná zásoba) / 2
        * **Signální zásoba** = denní spotřeba × dodací lhůta + pojistná zásoba (určuje okamžik, kdy je vhodné materiál znovu objednat)
        """)

        st.divider()
        st.markdown(
            "<div class='box-yellow'>🧮 <b>Kalkulačka: Průměrná a Signální"
            " zásoba</b></div>",
            unsafe_allow_html=True,
        )

        c_z1, c_z2 = st.columns(2)
        with c_z1:
            st.markdown("**Výpočet Průměrné zásoby**")
            pocatecni = st.number_input(
                "Počáteční zásoba na začátku měsíce (ks):",
                value=100,
                key="k3_4_1_pocatecni",
            )
            konecna = st.number_input(
                "Konečná zásoba na konci měsíce (ks):",
                value=50,
                key="k3_4_1_konecna",
            )
            prumerna = (pocatecni + konecna) / 2
            st.metric("Průměrná zásoba", f"{prumerna} ks")

        with c_z2:
            st.markdown("**Výpočet Signální zásoby**")
            denni_spotreba = st.number_input(
                "Denní spotřeba materiálu (ks):",
                value=10,
                key="k3_4_1_spotreba",
            )
            dodaci_lhuta = st.number_input(
                "Dodací lhuta od dodavatele (dny):",
                value=3,
                key="k3_4_1_lhuta",
            )
            pojistna = st.number_input(
                "Pojistná zásoba (ks):", value=20, key="k3_4_1_pojistna"
            )
            signalni = (denni_spotreba * dodaci_lhuta) + pojistna
            st.metric("Signální zásoba", f"{signalni} ks")
            st.info(
                f"Jakmile ti na skladě zbyde {signalni} ks, musíš ihned objednat"
                " další materiál."
            )

        if st.button("Uložit výpočet zásob 💾", key="btn_k3_4_1_zasoby"):
            zasoby_calc_data = (
                f"Průměrná zásoba: {prumerna} ks | Signální zásoba:"
                f" {signalni} ks"
            )
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"](
                    "Kapitola 3",
                    "Podkapitola 4.1 - Kalkulačka zásob",
                    zasoby_calc_data,
                )
            st.success("Výpočet zásob byl uložen!")

        st.divider()
        st.markdown("#### Pořízení materiálu")
        st.write("Pořízení materiálu zahrnuje všechny kroky od zjištění potřeby až po převzetí materiálu na sklad. Typický postup:")
        st.markdown("""
        1. **Zjištění potřeby materiálu** — Firma určí, co a v jakém množství potřebuje.
        2. **Výběr dodavatele** — Posuzuje se cena, kvalita, spolehlivost, dodací lhůta a platební podmínky.
        3. **Objednávka** — Firma vystaví objednávku nebo uzavře smlouvu.
        4. **Dodání materiálu** — Materiál dorazí do firmy.
        5. **Přejímka materiálu** — Kontroluje se množství, kvalita a shoda s objednávkou.
        6. **Uskladnění** — Materiál se uloží na sklad a zaeviduje.
        7. **Výdej do spotřeby** — Materiál se vydává do výroby podle potřeby.
        """)

        st.markdown("#### Evidence a skladování materiálu")
        st.write("Materiál se musí evidovat, aby firma věděla, kolik ho má, kde se nachází a jakou má hodnotu. Evidence může obsahovat: název materiálu, skladové číslo (kód), množství, cenu za jednotku, datum příjmu, dodavatele, místo uložení, výdeje do spotřeby a aktuální zůstatek na skladě.")
        st.write("**Mezi běžné skladové doklady patří:**")
        st.markdown("""
        - **Příjemka** — doklad o přijetí materiálu na sklad,
        - **Výdejka** — doklad o vydání materiálu ze skladu,
        - **Skladní karta** — přehled příjmů, výdejů a zůstatků materiálu.
        """)
        st.success("💡 Dobré skladování snižuje ztráty, záměny, poškození i zbytečné nákupy materiálu, který už firma ve skladu má.")

    elif selected_section_3 == "4.2 Oceňování a moderní řízení zásob":
        st.markdown("### 4.2 Oceňování a moderní řízení zásob")
        st.markdown("#### Metody vyskladňování zásob")
        st.write("Při výdeji materiálu ze skladu musí firma určit, v jaké hodnotě se materiál ze skladu odepíše. To je důležité hlavně tehdy, když firma nakupuje stejný materiál opakovaně, ale za různé ceny. Vyskladňování znamená výdej materiálu nebo zboží ze skladu do spotřeby, výroby nebo prodeje.")
        st.write("**Zvolená metoda ovlivňuje hodnotu spotřebovaného materiálu, výši nákladů, hodnotu zásob na skladě a tím i vykázaný zisk.**")

        st.markdown("""
        | Metoda | Význam | Jak funguje | Kde se používá dnes |
        | :--- | :--- | :--- | :--- |
        | **FIFO** | First In, First Out (první do skladu, první ze skladu) | Ze skladu se účetně vydává nejdříve to, co bylo nakoupeno jako první. (Např. nakoupím 100 ks po 20 Kč, pak 100 ks po 25 Kč. Při výdeji 80 ks počítám cenu 20 Kč/ks.) | Potravinářství, farmacie, kosmetika, gastronomie, supermarkety (hlídání expirace). |
        | **LIFO** | Last In, First Out (poslední do skladu, první ze skladu) | Ze skladu se účetně vydává nejdříve to, co bylo nakoupeno jako poslední. | V českém účetnictví se běžně nepoužívá, fyzicky odpovídá hromadě sypkého materiálu. |
        | **Vážený průměr** | Průměrná cena zásob | Materiál se oceňuje průměrnou cenou z více nákupů (celková hodnota / celkové množství). Používá se, když firma nechce sledovat přesnou cenu každé dávky. | Výrobní firmy, velkoobchody, sklady hutního materiálu, textilu, obalů nebo pohonných hmot. |
        """)

        st.divider()
        st.markdown("#### Moderní řízení zásob")
        st.write(
            "Rozdíl: FIFO, LIFO a vážený průměr řeší hlavně **ocenění zásob při výdeji**. "
            "Kromě nich firmy používají také modernější postupy, které pomáhají řídit zásoby efektivněji, rychleji a s menším rizikem chyb. Moderní metody (Kanban, JIT) řeší spíš to, **kolik zásob držet, kdy objednávat, co hlídat nejvíc a jak zabránit plýtvání a výpadkům**."
        )

        st.markdown("##### ABC analýza zásob")
        st.write("Pomáhá firmě rozdělit zásoby podle důležitosti. Ne všechny položky ve skladu mají stejnou hodnotu nebo stejný význam pro provoz. Používají ji výrobní podniky, e-shopy, nemocnice i supermarkety.")
        st.markdown("""
        * 🥇 **Skupina A (cca 10 % položek, ale 70 % hodnoty):** Nejdůležitější, drahé nebo klíčové položky (např. kávovar). Pečlivé sledování, častá kontrola, minimální zásoby.
        * 🥈 **Skupina B (cca 20 % položek, 20 % hodnoty):** Středně důležité (např. kvalitní káva). Pravidelná kontrola, běžné plánování.
        * 🥉 **Skupina C (cca 70 % položek, ale jen 10 % hodnoty):** Méně důležité, levné drobnosti (kelímky, šroubky, gumičky). Jednodušší evidence, větší tolerance zásoby.
        """)

        st.markdown("##### Vizuální systém KANBAN 🚥")
        st.write(
            "Kanban pochází z japonštiny (znamená „cedulka“ nebo „vizuální signál“). Proslavil ho Taiichi Ohno v automobilce Toyota jako způsob řízení výroby. "
            "Jde o systém, kdy si další krok výroby „táhne“ materiál až ve chvíli, kdy ho potřebuje. Pomáhá: rychle vidět, co chybí, omezit rozpracovanou výrobu, zabránit hromadění zásob a odhalit úzká místa. "
            "Dnes se používá nejen ve výrobě, ale také v IT, projektovém řízení (Trello, Jira, Notion)."
        )

        col_k1, col_k2, col_k3 = st.columns(3)
        with col_k1:
            st.info(
                "📦 **Bedýnka 1 (Používám)**\n\nBeru z ní šroubky. Dokud v ní"
                " něco je, nic neřeším."
            )
        with col_k2:
            st.warning(
                "🪹 **Bedýnka 1 se vyprázdní!**\n\nTo je **SIGNÁL (Kanban)**."
                " Prázdnou bedýnku pošlu do skladu jako objednávku."
            )
        with col_k3:
            st.success(
                "📦 **Bedýnka 2 (Záložní)**\n\nZačnu brát z druhé bedýnky. Než ji"
                " vyprázdním, sklad mi vrátí plnou Bedýnku 1."
            )

        st.markdown("##### Just-in-Time (JIT) dnes")
        st.write("Metoda JIT usiluje o to, aby materiál dorazil do výroby přesně tehdy, kdy je potřeba, což snižuje náklady na skladování. Proslavila ho Toyota. "
                 "V současnosti se ale používá opatrněji. Po zkušenostech s výpadky dodavatelských řetězců si firmy často nechávají i určitou bezpečnostní zásobu. "
                 "Současný přístup hledá rovnováhu mezi nízkými náklady a bezpečností dodávek.")

        st.markdown("##### Digitální skladové systémy")
        st.write("Moderní sklady využívají technologie, které umožňují sledovat zásoby v reálném čase (čárové a QR kódy, RFID čipy, skladový software, propojení e-shopu se skladem). "
                 "Systém například vidí, že na skladě zbývá posledních 12 kusů, a automaticky připraví objednávku. Běžné v e-commerce, logistice a farmacii.")

        st.markdown("##### Predikce poptávky a automatické objednávky")
        st.write("Firmy stále častěji využívají data (minulý prodej, sezónnost, počasí, trendy) k odhadu budoucí poptávky. To pomáhá rozhodnout: kolik a kdy objednat, co mít skladem, kde hrozí vyprodání nebo neprodané zásoby. Moderním trendem je využití algoritmů a AI pro automatické navrhování objednávek.")

    elif selected_section_3 == "4.3 Výpočty k oběžnému majetku":
        st.markdown("### 4.3 Výpočty k oběžnému majetku a zásobám")

        st.markdown("#### 1. Stanovení spotřeby materiálu")
        st.markdown("<div class='box-gray'><b>Spotřeba materiálu = norma spotřeby na kus × počet výrobků</b></div>", unsafe_allow_html=True)
        st.write("*Příklad: Firma vyrábí 500 kusů výrobku. Na jeden kus potřebuje 0,4 kg materiálu. Spotřeba = 0,4 × 500 = 200 kg.*")

        st.markdown("#### 2. Stanovení nákupu materiálu")
        st.markdown("<div class='box-gray'><b>Plánovaný nákup = plánovaná spotřeba + konečná zásoba − počáteční zásoba</b></div>", unsafe_allow_html=True)
        st.write("*Příklad: Firma plánuje spotřebovat 200 kg materiálu. Na začátku má 30 kg a na konci chce mít 50 kg. Plánovaný nákup = 200 + 50 − 30 = 220 kg.*")

        st.divider()
        st.markdown("#### 3. Rychlost a doba obratu zásob")
        st.write(
            "Každá zásoba, která leží na skladě, jsou **„utopené“ peníze**, za které firma mohla koupit něco jiného nebo je úročit v bance. "
            "Proto manažery zajímá, jak rychle se zásoby točí."
        )
        st.markdown("""
        * **Rychlost obratu zásob** = spotřeba za období / průměrná zásoba (říká, kolikrát se zásoba za určité období „otočí“).
        * **Doba obratu zásob** = počet dní období / rychlost obratu zásob (říká, kolik dní je zásoba průměrně vázaná ve firmě).
        """)
        st.info("📉 **Interpretace:** Vyšší rychlost obratu většinou znamená, že firma zásoby využívá efektivněji. Příliš nízké zásoby ale mohou ohrozit plynulost výroby.")

        c_obr1, c_obr2 = st.columns([1, 1.2])
        with c_obr1:
            rocni_trzby = st.number_input(
                "Roční tržby e-shopu (Kč):",
                value=3600000,
                step=100000,
                key="k3_4_3_trzby",
            )
            hodnota_skladu = st.slider(
                "Průměrná hodnota zboží na skladě (Kč):",
                min_value=100000,
                max_value=2000000,
                value=600000,
                step=50000,
                key="k3_4_3_sklad",
            )

        with c_obr2:
            obratky = rocni_trzby / hodnota_skladu
            doba_obratu = 360 / obratky if obratky > 0 else 0

            st.metric("Počet obrátek za rok", f"{obratky:.1f}x")
            st.metric(
                "Doba obratu (Zboží leží ve skladu)", f"{doba_obratu:.0f} dní"
            )

        if st.button("Uložit výpočet obratu zásob 💾", key="btn_k3_4_3_obrat"):
            obrat_data = (
                f"Tržby: {rocni_trzby} | Hodnota skladu: {hodnota_skladu} |"
                f" Obrátky: {obratky:.1f}x | Doba obratu: {doba_obratu:.0f} dní"
            )
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"](
                    "Kapitola 3", "Podkapitola 4.3 - Obrat zásob", obrat_data
                )
            st.success("Výpočet byl uložen!")

    elif selected_section_3 == "4.4 Dlouhodobý majetek a investice":
        st.markdown("### 4.4 Dlouhodobý majetek a plánování investic")
        st.write(
            "Dlouhodobý majetek je majetek, který firma používá delší dobu"
            " (déle než rok)."
        )

        c_i1, c_i2 = st.columns([1, 1])
        with c_i1:
            cena_stroje = st.number_input(
                "Cena nového stroje vč. instalace (Kč):",
                value=500000,
                step=50000,
                key="k3_4_4_cena",
            )
            rocni_uspora = st.number_input(
                "Roční finanční přínos stroje (Kč):",
                value=125000,
                step=5000,
                key="k3_4_4_uspora",
            )
        with c_i2:
            if rocni_uspora > 0:
                navratnost = cena_stroje / rocni_uspora
                st.metric("Doba návratnosti", f"{navratnost:.1f} let")
                st.success(
                    "Pokud stroj fyzicky vydrží déle než vypočítaná doba"
                    " návratnosti, investice má smysl."
                )

        if st.button(
            "Uložit výpočet návratnosti investice 💾",
            key="btn_k3_4_4_investice",
        ):
            if rocni_uspora > 0:
                inv_data = (
                    f"Cena stroje: {cena_stroje} | Roční přínos: {rocni_uspora}"
                    f" | Návratnost: {navratnost:.1f} let"
                )
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"](
                        "Kapitola 3",
                        "Podkapitola 4.4 - Návratnost investice",
                        inv_data,
                    )
                st.success("Návratnost investice byla uložena!")

    elif selected_section_3 == "4.5 Odpisy a evidence majetku":
        st.markdown("### 4.5 Odpisy (Účetní vs. Daňové) a grafické srovnání")
        st.write(
            "Dlouhodobý majetek si firma nedá do nákladů celý najednou v roce"
            " nákupu. Náklady se rozloží do více let – tomu se říká **Odpis**."
        )

        c_kalk1, c_kalk2 = st.columns([1, 1.2])
        with c_kalk1:
            odp_cena = st.number_input(
                "Pořizovací cena majetku (Kč):",
                value=500000,
                step=50000,
                min_value=10000,
                key="k3_4_5_cena",
            )
        with c_kalk2:
            skupiny = {
                "1. skupina (3 roky) - Počítače, nářadí": {
                    "roky": 3,
                    "rov_1": 20,
                    "rov_dalsi": 40,
                    "zrych_1": 3,
                    "zrych_dalsi": 4,
                },
                "2. skupina (5 let) - Auta, běžné stroje": {
                    "roky": 5,
                    "rov_1": 11,
                    "rov_dalsi": 22.25,
                    "zrych_1": 5,
                    "zrych_dalsi": 6,
                },
                "3. skupina (10 let) - Těžké stroje, turbíny": {
                    "roky": 10,
                    "rov_1": 5.5,
                    "rov_dalsi": 10.5,
                    "zrych_1": 10,
                    "zrych_dalsi": 11,
                },
                "4. skupina (20 let) - Dřevěné budovy, ploty": {
                    "roky": 20,
                    "rov_1": 2.15,
                    "rov_dalsi": 5.15,
                    "zrych_1": 20,
                    "zrych_dalsi": 21,
                },
                "5. skupina (30 let) - Cihlové/betonové budovy": {
                    "roky": 30,
                    "rov_1": 1.4,
                    "rov_dalsi": 3.4,
                    "zrych_1": 30,
                    "zrych_dalsi": 31,
                },
                "6. skupina (50 let) - Kancelářské budovy, hotely": {
                    "roky": 50,
                    "rov_1": 1.02,
                    "rov_dalsi": 2.02,
                    "zrych_1": 50,
                    "zrych_dalsi": 51,
                },
            }
            vybrana_skupina = st.selectbox(
                "Vyber odpisovou skupinu:",
                list(skupiny.keys()),
                index=1,
                key="k3_4_5_skupina",
            )

        param = skupiny[vybrana_skupina]
        roky = param["roky"]

        rovnomerne = []
        for rok in range(1, roky + 1):
            if rok == 1:
                odpis = odp_cena * (param["rov_1"] / 100)
            else:
                odpis = odp_cena * (param["rov_dalsi"] / 100)
            rovnomerne.append(round(odpis))

        zrychlene = []
        zustatek_zrych = odp_cena
        for rok in range(1, roky + 1):
            if rok == 1:
                odpis = odp_cena / param["zrych_1"]
            else:
                odpis = (2 * zustatek_zrych) / (
                    param["zrych_dalsi"] - (rok - 1)
                )
            zustatek_zrych -= odpis
            zrychlene.append(round(odpis))

        try:
            import pandas as pd

            df_odpisy = pd.DataFrame({
                "Rok": [f"{r}. rok" for r in range(1, roky + 1)],
                "Rovnoměrný odpis (Kč)": rovnomerne,
                "Zrychlený odpis (Kč)": zrychlene,
            })

            st.markdown("##### 📊 Výpočet odpisů rok po roce")
            st.dataframe(
                df_odpisy.style.format({
                    "Rovnoměrný odpis (Kč)": "{:,.0f}",
                    "Zrychlený odpis (Kč)": "{:,.0f}",
                }),
                use_container_width=True,
            )

            st.markdown("##### 📈 Grafické srovnání nákladů")
            df_graf = df_odpisy.set_index("Rok")
            st.bar_chart(df_graf, color=["#3b82f6", "#22c55e"])
        except ImportError:
            st.warning(
                "Pro zobrazení tabulek a grafů je potřeba knihovna Pandas."
            )

        if st.button("Uložit kalkulaci odpisů 💾", key="btn_k3_4_5_odpisy"):
            odpisy_data = (
                f"Cena: {odp_cena} Kč | Skupina: {vybrana_skupina} | Odpis 1."
                f" rok (Rovnoměrný/Zrychlený): {rovnomerne[0]}/{zrychlene[0]} Kč"
            )
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"](
                    "Kapitola 3",
                    "Podkapitola 4.5 - Odpisy majetku",
                    odpisy_data,
                )
            st.success("Kalkulace odpisů byla uložena!")

    # =========================================================================
    # SEKCE 5: KALKULACE, CENY A CENOVÉ STRATEGIE
    # =========================================================================
    elif selected_section_3 == "5.1 Cenové strategie v praxi":
        st.markdown("### 5.1 Cenové strategie v praxi")

        prod_typ = st.selectbox(
            "Vyber typ produktu / projektu:",
            [
                "Vyber...",
                "Mobilní aplikace na plánování tréninků",
                "Limitovaná edice 50 kusů designer mikin",
                "Taxi služba v pátek v noc po koncertě",
                "Set šamponu, kondicionéru a hřebenu",
            ],
            key="k3_5_1_prod",
        )

        if prod_typ != "Vyber...":
            strat_volba = st.radio(
                "Jaká strategie je pro tento produkt nejvhodnější?",
                [
                    "Freemium",
                    "Předplatné",
                    "Dynamická cena",
                    "Balíčkování",
                    "Prémiová cena",
                ],
                horizontal=True,
                key="k3_5_1_strat",
            )

            if "vykresli_otazku_fn" in st.session_state:
                st.session_state["vykresli_otazku_fn"](
                    "3.5.1",
                    f"Zdůvodni, proč strategie '{strat_volba}' pro '{prod_typ}'"
                    " dává ekonomický smysl:",
                    "3",
                    st.session_state.get("ulozene_odpovedi", {}),
                )

    elif selected_section_3 == "5.2 Náklady v digitálním světě a Asset-Light":
        st.markdown(
            "### 5.2 Náklady v digitálním světě a Asset-Light model"
        )

        cd1, cd2 = st.columns(2)
        with cd1:
            f_fix = st.number_input(
                "Fixní náklady (fyzické):",
                value=50000,
                step=10000,
                key="f_fix",
            )
            f_var = st.number_input(
                "Variabilní náklad/ks:", value=150, step=10, key="f_var"
            )
            f_kusy = st.slider(
                "Počet ks (fyzické):",
                min_value=100,
                max_value=10000,
                value=1000,
                step=100,
                key="f_kusy",
            )
            f_celk = f_fix + (f_var * f_kusy)
            f_prum = f_celk / f_kusy
            st.metric("Průměrný náklad na 1 ks", f"{f_prum:.1f} Kč")

        with cd2:
            d_fix = st.number_input(
                "Fixní náklady (digitální):",
                value=300000,
                step=50000,
                key="d_fix",
            )
            d_var = st.number_input(
                "Variabilní náklad/stažení:", value=2, step=1, key="d_var"
            )
            d_kusy = st.slider(
                "Počet stažení:",
                min_value=100,
                max_value=100000,
                value=10000,
                step=1000,
                key="d_kusy",
            )
            d_celk = d_fix + (d_var * d_kusy)
            d_prum = d_celk / d_kusy
            st.metric("Průměrný náklad na 1 uživatele", f"{d_prum:.1f} Kč")

        if st.button(
            "Uložit porovnání produktů 💾", key="btn_k3_5_2_porovnani"
        ):
            digital_data = (
                f"Fyzický průměr/ks: {f_prum:.1f} Kč | Digitální"
                f" průměr/uživatel: {d_prum:.1f} Kč"
            )
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"](
                    "Kapitola 3",
                    "Podkapitola 5.2 - Fyzický vs Digitální produkt",
                    digital_data,
                )
            st.success("Porovnání bylo uloženo!")

    # =========================================================================
    # SEKCE 6: EFEKTIVITA, ŠTÍHLÁ VÝROBA A TECHNOLOGIE
    # =========================================================================
    elif selected_section_3 == "6.1 Štíhlá výroba, Poka-Yoke a 5S":
        st.markdown("### 6.1 Štíhlá výroba (Lean), Poka-Yoke a 5S")

        sit = st.text_area(
            "Popiš situaci ze školní jídelny, dílny nebo brigády, kde vzniká"
            " chaos:",
            value=(
                "Při výdeji obědů kuchařka musí běhat pro příbory do vedlejší"
                " místnosti a studenti čekají ve 20metrové frontě."
            ),
            key="k3_6_1_sit",
        )
        plytvani_typ = st.multiselect(
            "Jaké druhy plýtvání (MUDA) zde vznikají?",
            [
                "Čekání",
                "Zbytečný pohyb",
                "Zbytečná doprava",
                "Chyby a opravy",
                "Nadbytečné zásoby",
                "Nadvýroba",
            ],
            default=["Čekání", "Zbytečný pohyb"],
            key="k3_6_1_muda",
        )

        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"](
                "3.6.1",
                "Navrhni jedno jednoduché zlepšení této situace (Poka-Yoke /"
                " 5S):",
                "3",
                st.session_state.get("ulozene_odpovedi", {}),
            )

    elif selected_section_3 == "6.2 Průmysl 4.0, Cirkulární ekonomika a KPI":
        st.markdown(
            "### 6.2 Průmysl 4.0, Cirkulární ekonomika a Dashboardy"
        )

        c_kpi1, c_kpi2 = st.columns([1, 1.2])
        with c_kpi1:
            kpi_navstevnost = st.number_input(
                "Měsíční návštěvnost webu:",
                value=10000,
                step=1000,
                key="k3_6_2_navst",
            )
            kpi_konverze = st.slider(
                "Konverzní poměr (%):",
                min_value=0.1,
                max_value=10.0,
                value=2.0,
                step=0.1,
                key="k3_6_2_konv",
            )
            kpi_kosik = st.number_input(
                "Průměrná objednávka (Kč):",
                value=850,
                step=50,
                key="k3_6_2_kosik",
            )
            kpi_vratky = st.slider(
                "Míra vratek (%):",
                min_value=0.0,
                max_value=30.0,
                value=5.0,
                step=1.0,
                key="k3_6_2_vratky",
            )

        with c_kpi2:
            kpi_objednavky = int(kpi_navstevnost * (kpi_konverze / 100))
            kpi_hrube_trzby = kpi_objednavky * kpi_kosik
            kpi_ztrata_vratky = kpi_hrube_trzby * (kpi_vratky / 100)
            kpi_ciste_trzby = kpi_hrube_trzby - kpi_ztrata_vratky

            st.metric("Počet objednávek", f"{kpi_objednavky} ks")
            st.metric(
                "Čisté tržby", f"{kpi_ciste_trzby:,.0f} Kč".replace(",", " ")
            )

        if st.button("Uložit nastavení KPI Dashboardu 💾", key="btn_k3_6_2_kpi"):
            kpi_dash_data = (
                f"Objednávky: {kpi_objednavky} ks | Čisté tržby:"
                f" {kpi_ciste_trzby:.0f} Kč"
            )
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"](
                    "Kapitola 3",
                    "Podkapitola 6.2 - Dashboard KPI",
                    kpi_dash_data,
                )
            st.success("KPI Dashboard byl uložen!")

    elif selected_section_3 == "6.3 Projektová dílna: Launch vlastního merche":
        st.markdown(
            "### 6.3 Projektová dílna: Launch vlastního merche / e-shopu"
        )

        p_nazev = st.text_input(
            "Název produktu / projektu:",
            value="Školní edice mikin s kapucí",
            key="k3_6_3_nazev",
        )
        p_cena = st.number_input(
            "Prodejní cena za 1 kus (Kč):",
            value=890,
            step=50,
            key="k3_6_3_cena",
        )
        p_var = st.number_input(
            "Variabilní náklady na 1 kus (Kč):",
            value=420,
            step=20,
            key="k3_6_3_var",
        )
        p_fix = st.number_input(
            "Fixní náklady celkem (Kč):",
            value=15000,
            step=1000,
            key="k3_6_3_fix",
        )
        p_odhad = st.number_input(
            "Očekávaný počet prodaných kusů:",
            value=50,
            step=10,
            key="k3_6_3_odhad",
        )

        p_prispevek = p_cena - p_var
        if p_prispevek > 0:
            p_bz = math.ceil(p_fix / p_prispevek)
            st.metric("Bod zvratu (musíš prodat)", f"{p_bz} kusů")

        if "vykresli_otazku_fn" in st.session_state:
            st.session_state["vykresli_otazku_fn"](
                "3.6.3",
                "Shrnutí strategického rozhodnutí pro prezentaci před"
                " třídou/vedením:",
                "3",
                st.session_state.get("ulozene_odpovedi", {}),
            )

    # =========================================================================
    # SEKCE 7: PŘÍPADOVÉ STUDIE A ZÁVĚREČNÝ CHECKLIST
    # =========================================================================
    elif selected_section_3 == "7.1 Případové studie z praxe":
        st.markdown("### 7.1 Případové studie z praxe")

        with st.form("form_studie_kavarna"):
            st.markdown("##### ☕ 1. Kavárna u školy: Kdy se začne vyplácet?")
            s1_prispevek = st.number_input(
                "Příspěvek na úhradu na 1 nápoj (Kč):",
                value=0,
                step=1,
                key="cs_k_prisp",
            )
            s1_bz = st.number_input(
                "Bod zvratu (kolik nápojů musíte prodat k zaplacení stánku 12"
                " 000 Kč?):",
                value=0,
                step=1,
                key="cs_k_bz",
            )
            s1_dostacujici = st.radio(
                "Je plánovaný prodej 500 nápojů dostatečný?",
                ["Vyber...", "Ano", "Ne"],
                horizontal=True,
                key="cs_k_dost",
            )

            if st.form_submit_button("Zkontrolovat a uložit výpočty kavárny 💾"):
                cs_kavarna_data = (
                    f"Příspěvek: {s1_prispevek} | BZ: {s1_bz} | Stačí 500ks:"
                    f" {s1_dostacujici}"
                )
                if "uloz_odpoved_fn" in st.session_state:
                    st.session_state["uloz_odpoved_fn"](
                        "Kapitola 3",
                        "Podkapitola 7.1 - Případová studie Kavárna",
                        cs_kavarna_data,
                    )
                st.success("Uloženo!")

    elif selected_section_3 == "7.2 Závěrečný checklist a prověrka kapitoly":
        st.markdown("### 7.2 Závěrečný checklist a prověrka kapitoly")

        ch1 = st.checkbox(
            "Umím rozlišit náklad, výdaj, výnos a příjem.", key="k3_7_2_ch1"
        )
        ch2 = st.checkbox(
            "Umím spočítat účetní i ekonomický zisk.", key="k3_7_2_ch2"
        )
        ch3 = st.checkbox(
            "Umím vysvětlit rozdríl mezi fixními a variabilními náklady.",
            key="k3_7_2_ch3",
        )
        ch4 = st.checkbox(
            "Umím spočítat bod zvratu v kusech.", key="k3_7_2_ch4"
        )

        splneno_pocet = sum([ch1, ch2, ch3, ch4])
        st.progress(splneno_pocet / 4)

        if st.button("Uložit výsledek checklistu 💾", key="btn_k3_7_2_chk"):
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"](
                    "Kapitola 3",
                    "Podkapitola 7.2 - Checklist Kapitoly 3",
                    f"Splněno {splneno_pocet}/4 bodů.",
                )
            st.success("Výsledek checklistu byl uložen!")
