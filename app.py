# PODKAPITOLA 13 - LOGICKÁ MAPA PODNIKÁNÍ
    elif selected_section == "13. Logická mapa podnikání":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 13</div>", unsafe_allow_html=True)
        st.markdown("## 13. Logická mapa podnikání")
        
        with st.container(border=True):
            st.markdown("""
            <div class='box-gray'>
                <strong>Přehled tématu:</strong> Tato mapa shrnuje hlavní oblasti podnikání od právního rámce přes právní formy až po záměr, rizika a ukončení podnikání.
            </div>
            """, unsafe_allow_html=True)

            st.text_input("🧩 Interaktivní výzva: Vyber jednu větev mapy, která je pro tvůj projekt nejdůležitější, a napiš proč:", placeholder="Zvolená větev a důvod...", key="p13_map_choice")

            st.markdown("""
            <div class='box-purple'>
                <strong>🤖 AI mentoring:</strong> Zkopíruj tento prompt do AI asistenta:<br>
                <i>„Vytvoř mi logickou mapu mého startupu podle oblastí: právo, zákazník, finance, rizika a odpovědnost.“</i>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("### Vizualizace logické mapy podnikání:")
            
            # Vylepšená grafická Mind Mapa pomocí HTML/CSS - ODSTRANĚNY PRÁZDNÉ ŘÁDKY PROTI ROZBITÍ MARKDOWNU
            st.markdown("""
            <style>
            .mindmap-wrapper {
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 2rem 1rem;
                flex-wrap: wrap;
                gap: 2rem;
                background: #f1f5f9;
                border-radius: 12px;
                border: 1px solid #e2e8f0;
                margin-bottom: 1.5rem;
            }
            .mm-col {
                display: flex;
                flex-direction: column;
                gap: 1.5rem;
            }
            .mm-center {
                background: #ef4444;
                color: white;
                padding: 1.8rem 2.5rem;
                border-radius: 20px;
                font-weight: 800;
                font-size: 1.5rem;
                text-align: center;
                box-shadow: 0 10px 15px -3px rgba(239, 68, 68, 0.3);
                border: 3px solid #b91c1c;
                z-index: 2;
            }
            .mm-node {
                background: #ffffff;
                border: 2px solid #cbd5e1;
                padding: 1rem;
                border-radius: 16px;
                width: 260px;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
                position: relative;
                transition: all 0.2s ease;
            }
            .mm-node:hover {
                border-color: #6366f1;
                box-shadow: 0 10px 15px -3px rgba(99, 102, 241, 0.2);
                transform: translateY(-2px);
            }
            .mm-title {
                font-weight: 700;
                color: #1e293b;
                margin-bottom: 0.5rem;
                text-align: center;
                border-bottom: 2px solid #e2e8f0;
                padding-bottom: 0.5rem;
                text-transform: uppercase;
                font-size: 0.85rem;
                letter-spacing: 0.05em;
            }
            .mm-node ul {
                margin: 0;
                padding-left: 1.2rem;
                font-size: 0.85rem;
                color: #475569;
            }
            .mm-node li { margin-bottom: 0.3rem; }
            </style>
            <div class="mindmap-wrapper">
                <div class="mm-col">
                    <div class="mm-node"><div class="mm-title">1. Legislativa a definice</div><ul><li>občanský zákoník</li><li>živnostenský zákon</li><li>ZOK</li><li>znaky podnikání</li></ul></div>
                    <div class="mm-node"><div class="mm-title">2. Právní formy</div><ul><li>OSVČ, v.o.s., k.s.</li><li>s.r.o., a.s.</li></ul></div>
                    <div class="mm-node"><div class="mm-title">3. Záměr a Lean Canvas</div><ul><li>zákazník a problém</li><li>řešení, první test</li><li>náklady a příjmy</li></ul></div>
                </div>
                <div class="mm-center">PODNIKÁNÍ<br><span style="font-size:0.9rem; font-weight: 500;">Logická mapa</span></div>
                <div class="mm-col">
                    <div class="mm-node"><div class="mm-title">4. CSR a etika</div><ul><li>férové jednání</li><li>odpovědnost (zaměstnanci, společnost, prostředí)</li></ul></div>
                    <div class="mm-node"><div class="mm-title">5. Rizika</div><ul><li>finanční riziko</li><li>právní a tržní riziko</li><li>švarcsystém</li></ul></div>
                    <div class="mm-node"><div class="mm-title">6. Zdroje a ukončení</div><ul><li>veřejné rejstříky</li><li>zrušení a zánik</li><li>insolvence</li></ul></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
