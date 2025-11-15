# 🧠 Parser Logic Reference

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

## 🧩 Parserin strategia

- Pilko rivi kolmeen segmenttiin: Left, Middle, Right
- Symbolit ja labelit poimitaan keskeltä
- Function ja suunta poimitaan reunoista
- Inside-pinnit tunnistetaan vain jos ne eivät ole reunoilta
- Kaikki kentät nimetään loogisesti ja semanttisesti
