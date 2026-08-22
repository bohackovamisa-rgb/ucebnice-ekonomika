elif selected_section_4 == "3.2 Nominální a reálná mzda":
        st.markdown("### 3.2 Nominální a reálná mzda")
        st.write(
            "Pokud vám šéf přidá 5 % ke mzdě, jste na tom lépe? **Ne vždy!** "
            "Záleží totiž na tom, jak rychle v zemi rostou ceny zboží a služeb."
        )

        st.markdown("""
        * 💸 **Nominální mzda:** Částka vyjádřená v korunách na výplatní pásce.
        * 🛒 **Reálná mzda:** Říká, **co si za tuto částku skutečně koupíte** (vyjadřuje vaši kupní sílu). Je ovlivněna zdražováním.
        * 📈 **Index spotřebitelských cen (ISC / CPI):** Představ si ho jako obří nákupní koš plný zboží a služeb. Statistici sledují, jak se mění jeho cena.
        * 🎈 **Míra inflace (%):** Vyjadřuje procentuální změnu tohoto indexu. Právě toto procento potřebujeme znát, abychom zjistili, o kolik se nám život prodražil.
        """)

        st.info(
            "💡 **Příklad:** Pokud ti mzda vzroste o 5 %, ale ceny v obchodech (míra inflace) vzrostou o 10 %, máš sice na účtu víc korun, ale reálně sis pohoršil (zchudnul jsi o 5 %)."
        )

        st.markdown(
            """
        <div class='box-green'>
            🧮 <b>Jednoduchý princip:</b><br>
            • Když ceny (inflace) rostou rychleji než mzda, <b>reálná mzda klesá</b>.<br>
            • Když mzda roste rychleji než ceny, <b>reálná mzda roste</b>.
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.divider()
        st.markdown(
            "<div class='box-purple'>🔎 <b>Detektivní úkol:</b> Běž na stránky Českého statistického úřadu (czso.cz) a najdi <b>aktuální míru inflace</b> (která se počítá právě z Indexu spotřebitelských cen). Zajímají nás procenta! Zadej zjištěné procento níže.</div>",
            unsafe_allow_html=True,
        )
        st.write(
            "Zadej svou výplatu a změň inflaci, ať vidíš, jestli si toho letos koupíš víc nebo míň:"
        )

        col_inf1, col_inf2 = st.columns(2)
        with col_inf1:
            puvodni_mzda = 30000
            st.metric("Původní mzda (Loni)", f"{puvodni_mzda} Kč")
            zvyseni_mzdy = st.slider(
                "Šéf ti přidal ke mzdě (%):", 0, 20, 5, key="k4_3_2_zvyseni"
            )
            inflace = st.number_input(
                "Aktuální míra inflace (změna Indexu v %):",
                value=8.0,
                step=0.1,
                key="k4_3_2_inflace",
                help="Zadej procentuální míru inflace z webu ČSÚ."
            )

        with col_inf2:
            nova_mzda = int(puvodni_mzda * (1 + (zvyseni_mzdy / 100)))
            st.metric(
                "Nová mzda (Letos)", f"{nova_mzda} Kč", delta=f"+{zvyseni_mzdy}%"
            )

            rust_realne_mzdy = zvyseni_mzdy - inflace
            if rust_realne_mzdy < 0:
                st.error(
                    f"🚨 **Chudneš!** Tvá reálná mzda klesla o"
                    f" {-rust_realne_mzdy:.1f} %. Sice máš v peněžence víc korun,"
                    " ale věci v obchodě zdražily mnohem víc."
                )
            elif rust_realne_mzdy == 0:
                st.warning(
                    "⚖️ **Jsi na nule.** Tvá mzda vzrostla přesně stejně jako"
                    " ceny zboží. Můžeš si dovolit úplně to samé co loni."
                )
            else:
                st.success(
                    f"📈 **Bohatneš!** Tvá reálná mzda vzrostla o"
                    f" {rust_realne_mzdy:.1f} %. Mzda překonala zdražování a ty si"
                    " můžeš dovolit koupit více věcí."
                )

        if st.button("Uložit výpočet kupní síly 💾", key="btn_k4_3_2"):
            kupni_data = (
                f"Zvýšení: {zvyseni_mzdy}% | Inflace: {inflace}% | Změna reálné"
                f" mzdy: {rust_realne_mzdy}%"
            )
            if "uloz_odpoved_fn" in st.session_state:
                st.session_state["uloz_odpoved_fn"](
                    "Kapitola 4",
                    "Podkapitola 3.2 - Kupní síla mzdy",
                    kupni_data,
                )
            st.success("Výpočet byl uložen!")
