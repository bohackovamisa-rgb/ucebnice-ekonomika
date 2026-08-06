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
            
            st.markdown("""
            <div class='box-gray'>
                <strong>⚖️ Přesná zákonná opora:</strong> Podnikatele definuje zákon č. 89/2012 Sb., občanský zákoník, zejména § 420 odst. 1: <br>„Kdo samostatně vykonává na vlastní účet a odpovědnost výdělečnou činnost živnostenským nebo obdobným způsobem se záměrem činit tak soustavně za účelem dosažení zisku, je považován se zřetelem k této činnosti za podnikatele.“<br><br>
                Jednoduše řečeno: Podnikatelem je ten, kdo podniká samostatně, na vlastní účet, na vlastní odpovědnost, dělá výdělečnou činnost soustavně a jejím cílem je zisk.
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class='box-blue'>
                <strong>📘 Proč je to důležité:</strong> Možná už máš nápad, něco prodáváš, tvoříš na zakázku nebo si jen přivyděláváš. Tady zjistíš, kdy už se z takové aktivity stává podnikání a proč je důležité poznat rozdíl mezi koníčkem, brigádou, OSVČ a firmou.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 1.1 Podnikatel v realitě současné generace")
            st.write("Podnikání dnes nemusí začínat kanceláří, provozovnou ani výrobní halou. Může začít mobilem, profilem na sociální síti, prodejem digitální šablony, správou obsahu pro lokální firmu, výrobou merch produktů, doučováním, e-shopem, aplikací, kurzem, grafickou službou, tvorbou videí nebo komunitním projektem.")
            st.write("Právě proto je důležité umět rozpoznat hranici mezi:")
            
            st.markdown("""
            * **koníčkem** — dělám něco pro radost, bez soustavného záměru vydělávat,
            * **jednorázovým přivýdělkem** — například prodám vlastní staré věci,
            * **brigádou nebo zaměstnáním** — pracuji podle pokynů zaměstnavatele,
            * **podnikáním** — samostatně nabízím produkt nebo službu, nesu riziko a chci dlouhodobě vydělávat.
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class='box-blue'>
                <strong>📱 Příklad pro dnešní studenty:</strong> Když jednou prodáš staré tenisky, nejde obvykle o podnikání. Když ale pravidelně nakupuješ, upravuješ, propaguješ a prodáváš zboží se záměrem vydělat, už se blížíš podnikání a musíš řešit pravidla.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 1.2 Čtyři znaky podnikání na praktických příkladech")
            st.markdown("""
            | Znak podnikání | Co znamená | Příklad ze současnosti | Otázka pro žáka |
            | :--- | :--- | :--- | :--- |
            | **Soustavnost** | Činnost se opakuje nebo je plánovaná dlouhodobě. | Každý měsíc prodávám vlastní digitální plánovače. | Dělám to jednou, nebo z toho chci pravidelný příjem? |
            | **Samostatnost** | Sám/sama rozhoduji o ceně, zákaznících, způsobu práce a organizaci. | Nabízím správu sociálních sítí lokálním podnikům. | Kdo určuje, jak, kdy a pro koho pracuji? |
            | **Vlastní jméno** | Vystupuji vůči zákazníkům a úřadům jako podnikatel nebo firma. | Mám značku, profil, faktury, obchodní podmínky nebo IČO. | Kdo nese odpovědnost před zákazníkem? |
            | **Vlastní odpovědnost**| Nesu riziko ztráty, reklamací, dluhů a špatných rozhodnutí. | Nakoupím materiál na merch, ale nikdo si ho nekoupí. | Co se stane, když plán nevyjde? |
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 1.3 Podnikatel není jen „někdo, kdo vydělává“")
            st.write("Podnikatel vytváří hodnotu pro zákazníka. Peníze jsou důsledkem toho, že někdo považuje produkt nebo službu za užitečnou. Moderní podnikavost proto zahrnuje nejen prodej, ale i schopnost:")
            st.markdown("""
            * vidět problém,
            * navrhnout řešení,
            * ověřit zájem,
            * komunikovat férově,
            * počítat náklady a cenu,
            * nést odpovědnost,
            * učit se z chyb,
            * používat technologie bezpečně a smysluplně.
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("<div class='box-yellow'><strong>🧪 Tvůj úkol: Je to podnikání?</strong><br>U každé situace rozhodni, zda jde spíš o koníček, jednorázový přivýdělek, zaměstnání, nebo podnikání. Zdůvodni odpověď podle čtyř znaků podnikání.</div>", unsafe_allow_html=True)
            st.selectbox("1. Student jednou prodá starý mobil.", ["Vyber odpověď...", "Koníček", "Jednorázový přivýdělek", "Zaměstnání", "Podnikání"], key="p1_q1")
            st.selectbox("2. Student každý týden prodává vlastnoručně vyráběné náramky přes Instagram.", ["Vyber odpověď...", "Koníček", "Jednorázový přivýdělek", "Zaměstnání", "Podnikání"], key="p1_q2")
            st.selectbox("3. Student pracuje v kavárně podle rozpisu směn.", ["Vyber odpověď...", "Koníček", "Jednorázový přivýdělek", "Zaměstnání", "Podnikání"], key="p1_q3")
            st.selectbox("4. Student nabízí grafiku loga pro malé podniky a sám si domlouvá cenu.", ["Vyber odpověď...", "Koníček", "Jednorázový přivýdělek", "Zaměstnání", "Podnikání"], key="p1_q4")
            st.selectbox("5. Student vytvoří placený online kurz pro mladší žáky.", ["Vyber odpověď...", "Koníček", "Jednorázový přivýdělek", "Zaměstnání", "Podnikání"], key="p1_q5")
            
            st.markdown("""
            <div class='box-purple'>
                <strong>🤖 AI mentoring:</strong> „Zeptej se mě na můj nápad a podle čtyř znaků podnikání mi vysvětli, jestli už jde o podnikání. U každého znaku mi dej jednu kontrolní otázku.“
            </div>
            """, unsafe_allow_html=True)
            st.markdown("<div class='box-yellow'><strong>🧩 Interaktivní výzva:</strong> Popiš svůj nápad jednou větou a označ, jak v něm bude vidět soustavnost, samostatnost a odpovědnost.</div>", unsafe_allow_html=True)
            st.text_area("Tvoje odpověď:", key="p1_idea")
            st.info("🤔 **Otázka k zamyšlení:** V čem je podle vás největší rozdíl mezi zaměstnancem a podnikatelem?")

    # --- 2. Slovníček základních pojmů ---
    elif selected_section == "2. Slovníček základních pojmů":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 2</div><h2>2. Slovníček základních pojmů</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("""
            <div class='box-gray'>
                <strong>⚖️ Proč jsou definice důležité:</strong> V podnikání nestačí používat pojmy „přibližně“. Výrazy jako podnikatel, fyzická osoba, právnická osoba nebo živnostenské oprávnění mají oporu v právních předpisech.
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            | Termín | Co znamená | Proč je důležitý |
            | :--- | :--- | :--- |
            | **Podnikatel** | Osoba, která samostatně vykonává výdělečnou činnost na vlastní účet a odpovědnost se záměrem dělat ji soustavně za účelem dosažení zisku. | Pomáhá rozlišit, kdy už nejde jen o koníček nebo jednorázový přivýdělek. |
            | **Podnikání** | Soustavná samostatná činnost vykonávaná na vlastní odpovědnost za účelem dosažení zisku. | Je základním pojmem celé kapitoly a určuje, kdy vznikají právní a finanční povinnosti. |
            | **Fyzická osoba** | Člověk — jednotlivec. V podnikání může vystupovat například jako OSVČ. | Máš poznat rozdíl mezi člověkem podnikatelem a firmou jako právnickou osobou. |
            | **Právnická osoba** | Organizovaný subjekt, který má právní osobnost. Typicky jde například o s.r.o., a.s., družstvo, spolek nebo nadaci. | Vysvětluje, proč firma může jednat, vlastnit majetek a nést odpovědnost samostatně. |
            | **OSVČ** | Osoba samostatně výdělečně činná — fyzická osoba, která podniká vlastním jménem a na vlastní odpovědnost. | Je častou formou začátku malého podnikání, freelancingu nebo služeb. |
            | **Živnost** | Podnikatelská činnost provozovaná podle živnostenského zákona, pokud splňuje zákonné podmínky. | Pomáhá určit, jestli podnikatel potřebuje živnostenské oprávnění a jaký typ živnosti řeší. |
            | **Živnostenské oprávnění** | Právo provozovat živnost. U ohlašovacích živností vzniká zpravidla ohlášením, u koncesovaných živností až udělením koncese. | Bez něj nelze legálně provozovat činnost, která živnostenské oprávnění vyžaduje. |
            | **Volná živnost** | Živnost, u které není potřeba speciální vzdělání ani praxe; stačí splnit všeobecné podmínky. | Patří sem mnoho běžných začátků podnikání, například marketingové služby nebo e-shop. |
            | **Řemeslná živnost** | Živnost, která vyžaduje odbornou způsobilost, například výuční list nebo praxi. | Ukazuje, že některé činnosti nelze začít dělat bez kvalifikace. |
            | **Vázaná živnost** | Živnost, která vyžaduje specifické vzdělání, praxi nebo jinou zákonem stanovenou způsobilost. | Pomáhá pochopit, že u některých služeb stát chrání zákazníka požadavkem na odbornost. |
            | **Koncesovaná živnost** | Živnost, kterou lze provozovat až po udělení státního povolení — koncese. | Typicky jde o regulované nebo rizikovější činnosti. |
            | **Obchodní korporace** | Souhrnný pojem pro obchodní společnosti a družstva, například v.o.s., k.s., s.r.o., a.s. a družstvo. | Pomáhá zařadit základní právní formy podnikání. |
            | **Obchodní rejstřík** | Veřejný seznam, ve kterém se zapisují obchodní korporace a další zákonem stanovené subjekty. | Slouží k ověření firmy, její právní formy, sídla a osob, které za ni jednají. |
            | **Živnostenský rejstřík** | Evidence osob podnikajících na základě živnostenského oprávnění. | Slouží k ověření, zda má podnikatel oprávnění k určité činnosti. |
            | **Ručení** | Odpovědnost za dluhy a závazky podnikatele nebo firmy. | Je klíčové při volbě právní formy, protože OSVČ a některé společnosti nesou vyšší osobní riziko. |
            | **Švarcsystém** | Nelegální nastavení, kdy člověk formálně vystupuje jako podnikatel, ale fakticky pracuje jako zaměstnanec. | Pomáhá rozpoznat rizikovou spolupráci a rozdíl mezi podnikáním a zaměstnáním. |
            | **CSR** | Společenská odpovědnost firem — přístup, kdy firma sleduje nejen zisk, ale i dopady na lidi, společnost a životní prostředí. | Ukazuje, že podnikání má také etický a společenský rozměr. |
            | **Lean Canvas** | Stručná mapa podnikatelského nápadu, která zachycuje problém, zákazníka, řešení, náklady, příjmy a rizika. | Pomáhá rychle ověřovat nápad dřív, než tým investuje hodně času nebo peněz. |
            | **MVP** | Minimální životaschopný produkt — nejmenší verze řešení, která umožní ověřit důležitý předpoklad. | Učí testovat nápad levně, rychle a bezpečně. |
            """)

    # --- 3. OSVČ a živnosti ---
    elif selected_section == "3. OSVČ a živnosti":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 3</div><h2>3. OSVČ a živnosti</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("OSVČ znamená osoba samostatně výdělečně činná. Jde o podnikání fyzické osoby — tedy člověka, který podniká vlastním jménem a nese za své podnikání odpovědnost.")
            st.markdown("""
            <div class='box-blue'>
                <strong>📘 Proč je to důležité:</strong> Podnikání jako OSVČ vypadá jednoduše, ale má právní, daňové a sociální důsledky. Je proto důležité znát základní podmínky živnostenského podnikání, povinnosti vůči státu a riziko osobního ručení.
            </div>
            """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("### 3.1 OSVČ jako nejčastější start malé podnikavosti")
            st.write("OSVČ je pro mnoho lidí nejjednodušší cesta, jak začít. Hodí se pro malé služby, freelancing, řemeslo, doučování, správu sociálních sítí, grafiku, fotografování, tvorbu webů, e-shop v menším rozsahu nebo lokální podnikání.")
            
            st.markdown("""
            | Situace | Proč může OSVČ dávat smysl | Na co si dát pozor |
            | :--- | :--- | :--- |
            | **Student spravuje sociální sítě lokální kavárně.** | Nízké vstupní náklady, služba založená na dovednosti. | Smlouva, fakturace, daně, autorská práva k obsahu. |
            | **Grafik tvoří loga a šablony.** | Lze začít s notebookem a portfoliem. | Licenční podmínky, termíny, reklamace, komunikace s klientem. |
            | **Kadeřník nebo kosmetička chce pracovat samostatně.** | Vlastní zákazníci, možnost budovat značku. | Odborná způsobilost, hygiena, provozovna, odpovědnost. |
            | **Malý e-shop prodává vlastní produkty.** | Jednoduchý start a přímý kontakt se zákazníkem. | Obchodní podmínky, reklamace, sklad, ochrana spotřebitele. |
            """)

        with st.container(border=True):
            st.markdown("### 3.2 OSVČ a digitální realita")
            st.write("Dnešní OSVČ často nepotřebuje jen živnostenské oprávnění. Potřebuje také digitální a finanční gramotnost:")
            st.markdown("""
            * oddělit osobní a podnikatelské peníze,
            * evidovat příjmy a výdaje,
            * zálohovat doklady,
            * chránit osobní údaje zákazníků,
            * nepoužívat cizí fotografie, hudbu a texty bez práv,
            * komunikovat transparentně cenu, dodání a podmínky,
            * počítat s daněmi a odvody dřív, než peníze utratí.
            """)

            st.markdown("#### 🧮 Mini simulace OSVČ")
            st.write("Představ si, že OSVČ za měsíc vyfakturuje 28 000 Kč. Náklady na software, dopravu, materiál a reklamu jsou 6 000 Kč.")
            zisk_osvc = 28000 - 6000
            st.info(f"**Orientační zisk před daněmi a odvody:** {zisk_osvc} Kč")
            reserve_pct = st.slider("Navrhni, kolik procent by si měla OSVČ odložit stranou:", 0, 50, 30, 5, key="osvc_sim_res")
            st.write(f"Při {reserve_pct} % si odložíte: {28000 * (reserve_pct/100):.0f} Kč.")

        with st.container(border=True):
            st.markdown("### 🧮 Kalkulačka hodinové sazby OSVČ")
            st.write("Spousta začínajících freelancerů si špatně nastaví hodinovou sazbu, protože zapomenou, že ne každá pracovní hodina je placená (fakturovatelná).")
            
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
                
                st.metric("Tvůj minimální hodinový tarif", f"{hourly_rate:,.0f} Kč/h".replace(",", " "))
                st.info(f"Abys měl/a čistého **{target_net} Kč**, musíš si vydělat **{total_gross_needed} Kč**. Protože reálně fakturuješ jen **{billable_hours:.0f} hodin**, účtuj si alespoň **{hourly_rate:,.0f} Kč/h**.")

    # --- 4. Obchodní korporace ---
    elif selected_section == "4. Obchodní korporace":
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 4</div><h2>4. Obchodní korporace</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("Obchodní korporace jsou právnické osoby založené podle zákona o obchodních korporacích. Patří mezi ně obchodní společnosti a družstva.")
            
            st.markdown("""
            | Skupina | Formy | Typický znak |
            | :--- | :--- | :--- |
            | **Osobní společnosti** | v.o.s., k.s. | Důležitá je osobní účast společníků, důvěra a vyšší ručení. |
            | **Kapitálové společnosti** | s.r.o., a.s. | Důležitý je vklad kapitálu a oddělení firmy od osobního majetku. |
            | **Družstva** | družstvo | Důležité je členství a společný prospěch členů. |
            """)

        with st.container(border=True):
            st.markdown("### 🧭 Test: OSVČ, nebo s.r.o.?")
            q1 = st.radio("1️⃣ Plánuješ podnikat sám/sama, nebo v týmu?", ["Spíš OSVČ: Sám/sama", "Spíš s.r.o.: V týmu"], key="kviz_q1")
            q2 = st.radio("2️⃣ Hrozí větší finanční závazky?", ["Spíš OSVČ: Nízké náklady", "Spíš s.r.o.: Větší úvěry/sklad"], key="kviz_q2")
            
            if st.button("Vyhodnotit test", key="btn_eval_osvc_sro"):
                st.info("💡 Pokud převažují odpoveďi Spíš s.r.o., dává smysl uvažovat o založení právnické osoby kvůli ochrannému ručení.")

    # --- 5. Startup ---
    elif "5. Startup" in selected_section:
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 5</div><h2>5. Startup: nápad, který hledá funkční byznys</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("Startup je mladý podnikatelský projekt, který hledá opakovatelný a škálovatelný způsob, jak řešit problém zákazníka.")
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("<div class='box-gray'><strong>🏛️ Tradiční firma (Pekařství)</strong><br>Cíl: Stabilita a stálý zisk na lokálním trhu.</div>", unsafe_allow_html=True)
            with col2:
                st.markdown("<div class='box-green'><strong>🚀 Startup (Aplikace)</strong><br>Cíl: Rychlý a obrovský růst globálně. Vysoké riziko.</div>", unsafe_allow_html=True)

    # --- 6. Podnikatelský záměr ---
    elif "6. Podnikatelský záměr" in selected_section:
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
                st.success(f"**Marže na kus:** {marze} Kč. **Bod zvratu:** Musíš prodat alespoň **{math.ceil(bod_zvratu)} kusů** měsíčně.")

    # --- 7. Lean Canvas ---
    elif "7. Lean Canvas" in selected_section:
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 7</div><h2>7. Lean Canvas</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("### 🖼️ Interaktivní Lean Canvas")
            lc_col1, lc_col2, lc_col3 = st.columns(3)
            with lc_col1:
                st.text_area("🔴 Problém", height=120, key="lc_prob")
                st.text_area("🟢 Řešení", height=120, key="lc_sol")
                st.text_area("🌸 Náklady", height=120, key="lc_cost")
            with lc_col2:
                st.text_area("🟡 Unikátní hodnota", height=120, key="lc_val")
                st.text_area("⚪ Metriky", height=120, key="lc_met")
                st.text_area("🟤 Výhoda", height=120, key="lc_adv")
            with lc_col3:
                st.text_area("🟠 Zákazník", height=120, key="lc_cust")
                st.text_area("🔵 Kanály", height=120, key="lc_chan")
                st.text_area("🟣 Příjmy", height=120, key="lc_rev")

    # --- 8. CSR ---
    elif "8. CSR" in selected_section or "Odpovědné podnikání" in selected_section:
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 8</div><h2>8. CSR, etika a odpovědné podnikání (ESG)</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("CSR znamená společenská odpovědnost firem. Připomíná, že podnikání nemá sledovat pouze zisk, ale i dopady na společnost a přírodu.")

    # --- 9. Rizika ---
    elif "9. Rizika" in selected_section:
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 9</div><h2>9. Rizika podnikání</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("Podnikatelské riziko znamená nejistotu. Místo ignorování rizika s ním podnikatel pracují pomocí prevence.")

    # --- 10. Švarcsystém ---
    elif "10. Švarcsystém" in selected_section:
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 10</div><h2>10. Švarcsystém</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.error("⚠️ Švarcsystém je nelegální stav, kdy člověk vystupuje jako OSVČ (na IČO), ale fakticky vykonává běžnou závislou práci zaměstnance.")

    # --- 11. Ověřování informací ---
    elif "11. Ověřování" in selected_section:
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 11</div><h2>11. Ověřování informací a zdroje</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("Každý podnikatel by měl umět pracovat s veřejnými rejstříky (ARES, OR, RŽP, Justice.cz).")

    # --- 12. Ukončení podnikání ---
    elif "Ukončení podnikání" in selected_section:
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 12</div><h2>12. Ukončení podnikání</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("Rozlišujeme mezi **zrušením** (proces likvidace/vypořádání) a **zánikem** (definitivní výmaz z rejstříku).")

    # --- 13. Logická mapa ---
    elif "Logická mapa" in selected_section:
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 13</div><h2>13. Logická mapa podnikání</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("Stručná přehledná mapa propojující právo, formy, záměr, Lean Canvas, finance a etiku.")

    # --- 14. Reflexe ---
    elif "Reflexe" in selected_section:
        st.markdown("<div class='sub-section-header'>PODKAPITOLA 14</div><h2>14. Reflexe a sebehodnocení</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.text_area("Co nejdůležitějšího si z Kapitoly 1 odnášíš?", key="kap1_ref_txt")

    # --- 15. Integrované opakování ---
    elif "15. Integrované" in selected_section or "Integrované" in selected_section:
        st.markdown("<div class='sub-section-header'>ZÁVĚREČNÝ MODUL</div><h2>15. Integrované opakování</h2>", unsafe_allow_html=True)
        with st.container(border=True):
            st.write("Závěrečný modul propojující veškeré poznatky v praxi.")
