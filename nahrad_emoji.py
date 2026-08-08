import os

# Slovník převodu emoji na černé čárové ikony Flaticon Bold
REPLACEMENTS = {
    "📖": '<i class="fi fi-bs-book-alt"></i>',
    "<i class='fi fi-bs-bookmark'></i>": '<i class="fi fi-bs-bookmark"></i>',
    "🧩": '<i class="fi fi-bs-puzzle-piece"></i>',
    "🚀": '<i class="fi fi-bs-rocket-lunch"></i>',
    "🤖": '<i class="fi fi-bs-sparkles"></i>',
    "💡": '<i class="fi fi-bs-bulb"></i>',
    "🎯": '<i class="fi fi-bs-crosshair"></i>',
    "🔍": '<i class="fi fi-bs-search"></i>',
    "🔎": '<i class="fi fi-bs-search"></i>',
    "⚠️": '<i class="fi fi-bs-exclamation"></i>',
    "🛡️": '<i class="fi fi-bs-shield"></i>',
    "👉": '<i class="fi fi-bs-angle-right"></i>',
    "👀": '<i class="fi fi-bs-eye"></i>',
    "🧠": '<i class="fi fi-bs-brain"></i>',
    "☕": '<i class="fi fi-bs-mug-hot"></i>',
    "📱": '<i class="fi fi-bs-mobile-button"></i>',
    "👕": '<i class="fi fi-bs-shirt"></i>',
    "⚙️": '<i class="fi fi-bs-settings"></i>',
    "👥": '<i class="fi fi-bs-users"></i>',
    "📊": '<i class="fi fi-bs-chart-histogram"></i>',
    "💧": '<i class="fi fi-bs-drop"></i>',
    "📏": '<i class="fi fi-bs-ruler-vertical"></i>',
    "🎨": '<i class="fi fi-bs-palette"></i>',
    "🖐️": '<i class="fi fi-bs-hand"></i>',
    "🔲": '<i class="fi fi-bs-square"></i>',
    "🔦": '<i class="fi fi-bs-flashlight"></i>',
}

# Seznam všech souborů kapitol ke zpracování
SOUBORY = [
    "kapitola1.py",
    "kapitola2.py",
    "kapitola3.py",
    "kapitola4.py",
    "kapitola5.py",
    "kapitola6.py",
    "kapitoly/kapitola1.py",
    "kapitoly/kapitola2.py",
    "kapitoly/kapitola3.py",
    "kapitoly/kapitola4.py",
    "kapitoly/kapitola5.py",
    "kapitoly/kapitola6.py",
]


def automaticky_nahradit():
    upraveno_celkem = 0
    for cesta in SOUBORY:
        if os.path.exists(cesta):
            with open(cesta, "r", encoding="utf-8") as f:
                obsah = f.read()

            puvodni_obsah = obsah
            for emoji_symbol, html_ikona in REPLACEMENTS.items():
                obsah = obsah.replace(emoji_symbol, html_ikona)

            if obsah != puvodni_obsah:
                with open(cesta, "w", encoding="utf-8") as f:
                    f.write(obsah)
                print(f"✅ Úspěšně upraveno: {cesta}")
                upraveno_celkem += 1

    print(f"\nHotovo! Celkem aktualizováno {upraveno_celkem} souborů.")


if __name__ == "__main__":
    automaticky_nahradit()
