# 🧠 Parser Logic Reference

## 🔹 Tiedostopolkujen resoluutio

Parserin täytyy löytää oikea `README.md`-tiedosto layout-kansiosta. Tämä toimii riippumatta siitä, mistä hakemistosta parseri ajetaan.

### 🔸 Polkulogiikka

```python
import os

BOARD_NAME = "Teensy32"  # Tämä on layout-kansion nimi

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))  # esim. LayoutParser/
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))  # projektin juuri

README_PATH = os.path.join(BASE_DIR, BOARD_NAME, "README.md")
OUTPUT_PATH = os.path.join(BASE_DIR, BOARD_NAME, f"{BOARD_NAME}.md")

print("README_PATH:", README_PATH)
assert os.path.exists(README_PATH), "README.md ei löytynyt!"
```

### 🔸 Esimerkki hakemistorakenteesta

```
projekti/
├── LayoutParser/
│   └── layout_parser.py
├── Teensy32/
│   ├── README.md
│   └── Teensy32.md
```

### 🔸 Vinkki

- Käytä `os.path.abspath()` varmistaaksesi että polut ovat absoluuttisia
- Tämä estää virheet, jos parseria ajetaan eri hakemistosta (esim. VSCode, komentorivi)


## 🔹 Parserin perusasetukset

Jokaisen parserin alkuun tarvitaan nämä rivit:

```python
import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')



print(f"📂 Board: {BOARD_NAME}")
print(f"📄 Reading from: {README_PATH}")
print(f"📝 Writing to: {OUTPUT_PATH}")
```

## 🔹 Lohkologiikka

- Vasemman lohkon rakenne:
  - `CodeFunction ← │ Symbol PinLabel`
  - `CodeFunction`: koodissa käytettävä nimi (ei pilkottava)
  - Nuoli `←`: suunta poispäin pinnistä → `PinInOrOut = OUTPUT`
  - Symboli + Label = pinnin tunnistus
  - `BoardLocation = Left`

- Oikean lohkon rakenne:
  - `PinLabel Symbol │ → CodeFunction`
  - Nuoli `→`: suunta poispäin pinnistä → `PinInOrOut = OUTPUT`
  - Symboli + Label = pinnin tunnistus
  - `BoardLocation = Right`

- Keskilohko (`Inside`):
  - Vain jos keskellä on symboli + label, joka ei kuulu reunoihin
  - `BoardLocation = Inside`

## 🔸 Kenttien nimet

- `PinLine`: rivinumero README.md:ssä
- `BoardLocation`: Left / Right / Inside
- `CodeFunction`: koodissa käytettävä nimi
- `PinLabel`: fyysinen pinnin nimi
- `PinInOrOut`: INPUT / OUTPUT nuolen suunnasta
- `PinStatus`: symbolin perusteella tulkittu tila
- `HasPWM`: `✓` jos symboli sisältää `~`
- `RawFragment`: alkuperäinen fragmentti debug-tarkastelua varten

## 🔸 Symbolien merkitykset (`PIN_STATE`)

- `□`: Free pin
- `■`: Used pin
- `▲`: Special pin (SPI, I2C, INT, UART, Pull-up/down)
- `◊`: Caution needed (sensor, expansion, #!notation)
- `X`: Do not use (reserved, LED, unsafe)
- `≋`: DAC capable
- `↧`: Underside pin (not on header)
- `○`: Pad (solder/contact area)
- `•`: Pad in use (solder/contact area)

## 🔸 Esimerkkirivi

D0/RX1        ← │ □ D0         VUSB □ → AGND □ │ → AGND

- Vasen lohko:
  - `CodeFunction = D0/RX1`
  - `PinLabel = D0`
  - `PinInOrOut = OUTPUT`
  - `BoardLocation = Left`

- Keskilohko:
  - `CodeFunction = VUSB`
  - `PinLabel = VUSB`
  - `PinInOrOut = OUTPUT`
  - `BoardLocation = Inside`

- Oikea lohko:
  - `CodeFunction = AGND`
  - `PinLabel = AGND`
  - `PinInOrOut = OUTPUT`
  - `BoardLocation = Right`


## 🔸 Visuaalisen kohinan suodatus (`VISUAL_NOISE`)

- Poistetaan keskisegmentistä ennen fragmentointia
- Kohinasymbolit:
  - `│`, `└`, `─`, `┘`, `╱`, `╲`, `━`, `┐`, `┌`, `┬`, `┼`, `┤`, `├`, `┴`

## 🔸 Modulaarinen Markdown-taulukon generointi
```python
def generate_markdown_table(results, board_name, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# Pin and Direction Table: {board_name}\n\n")
        f.write("| PinLine | BoardLocation | CodeFunction | PinInOrOut | PinStatus | HasPWM | PinLabel |\n")
        f.write("|---------|----------------|--------------|------------|-----------|--------|----------|\n")
        for r in results:
            f.write(f"| {r['PinLine']} | {r['BoardLocation']} | {r['CodeFunction']} | {r['PinInOrOut']} | {r['PinStatus']} | {'✓' if r['HasPWM'] else ''} | {r['PinLabel']} |\n")
```
## 🔧 Päivitetty main()-funktio

```python
def main():
    if not os.path.exists(README_PATH):
        print(f"❌ README.md not found in {BOARD_NAME}")
        return

    all_results = []
    with open(README_PATH, encoding="utf-8") as f:
        line_counter = 1
        for i, line in enumerate(f.readlines(), start=1):
            parsed = parse_pin_line(line, line_counter)
            if parsed:
                all_results.extend(parsed)
                line_counter += 1

    generate_markdown_table(all_results, BOARD_NAME, OUTPUT_PATH)
    print(f"\n✅ Table written to: {OUTPUT_PATH}")
```


## 🧩 Parserin strategia

- Pilko rivi kolmeen segmenttiin: Left, Middle, Right
- Symbolit ja labelit poimitaan keskeltä
- Function ja suunta poimitaan reunoista
- Inside-pinnit tunnistetaan vain jos ne eivät ole reunoilta
- Kaikki kentät nimetään loogisesti ja semanttisesti

## 🔸 Config.h generointi: CodeFunction → PinLabel

Kun käyttäjä muokkaa layoutia (`README.md`) ja merkitsee pinnin käytetyksi (`■`), voidaan generoida `#define`-rivi `config.h`-tiedostoon.

### 🔹 Generoinnin ehdot

- `PinStatus == "Used pin"`
- `CodeFunction` on annettu
- `PinLabel` on tunnistettu

### 🔹 Esimerkki layoutista

```
D0/RX1 ← │ ■ D0
```

→ Parseri tunnistaa:

- `PinLabel = D0`
- `CodeFunction = D0/RX1`
- `PinStatus = Used pin`

→ Generoitu rivi `config.h`-tiedostoon: `#define RX1 D0`

> Huom: Jos `CodeFunction` sisältää useita nimiä (`D0/RX1`), voidaan käyttää viimeistä (`RX1`) tai kaikkia, riippuen strategiasta.

---

### 🔹 Funktio: `generate_config_defines(results)`

```python
def generate_config_defines(results):
    defines = []
    for r in results:
        if r["PinStatus"] == "Used pin" and r["CodeFunction"]:
            names = r["CodeFunction"].split("/")
            for name in names:
                defines.append(f"#define {name.strip()} {r['PinLabel']}")
    return defines
```

- Palauttaa listan `#define`-rivejä
- Voidaan kirjoittaa tiedostoon `config.h` tai `BOARD_NAME_config.h`
- Tukee useita nimiä per pinni

---

### 🔹 Tuleva laajennusmahdollisuus

- Tuki `#ifdef BOARD_NAME`
- Kommentit layoutista: `// Pin D0 used for RX1`
- Automaattinen generointi kaikille layout-kansioille

