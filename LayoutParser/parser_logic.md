# 🧠 Parser Logic Reference

## 🔹 Path resolution for layout files

The parser must locate the correct `README.md` file inside the layout folder, regardless of where the script is executed from.

### 🔸 Path logic

```python
import os

BOARD_NAME = "Teensy32"  # Layout folder name, this is an example README.md board in a same named folder

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))  # e.g. LayoutParser/
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))  # Project root

README_PATH = os.path.join(BASE_DIR, BOARD_NAME, "README.md")
OUTPUT_PATH = os.path.join(BASE_DIR, BOARD_NAME, f"{BOARD_NAME}.md")

print("README_PATH:", README_PATH)
assert os.path.exists(README_PATH), "README.md not found!"
```

### 🔸 Example folder structure

```
project/
├── LayoutParser/
│   └── layout_parser.py
├── Teensy32/
│   ├── README.md
│   └── Teensy32.md
```

### 🔸 Tips

- Use `os.path.abspath()` to ensure paths are absolute
- This prevents errors when running the parser from different working directories (e.g. VSCode, CLI)


### 🔹 Parses basic setup

Every parser needs these lines at the beginning

```python
import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

BOARD_NAME = "Teensy32"  # Layout folder name, this is an example README.md board in a same named folder

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))  # e.g. LayoutParser/
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))  # Project root

README_PATH = os.path.join(BASE_DIR, BOARD_NAME, "README.md")
OUTPUT_PATH = os.path.join(BASE_DIR, BOARD_NAME, f"{BOARD_NAME}.md")

print("README_PATH:", README_PATH)
assert os.path.exists(README_PATH), "README.md not found!"
print(f"📂 Board: {BOARD_NAME}")
print(f"📄 Reading from: {README_PATH}")
print(f"📝 Writing to: {OUTPUT_PATH}")
```

### 🔹 Segmentlogic

- **When reading the Unicode layout from README.md the Layout is divided into three sections**

- Left section structure:
  - `CodeFunction ← │ Symbol PinLabel`
  - `CodeFunction`: This is the name used in the code (Don't Split) user will define it manually
  - Arrow `←`: away from pin → `PinInOrOut = OUTPUT`
  - Symbol + Label  = pin recognition
  - `BoardLocation = Left`

- Right section structure:
  - `PinLabel Symbol │ → CodeFunction`
  - Arrow `→`: away from pin → `PinInOrOut = OUTPUT`
  - Symbol + Label = pin recognition
  - `BoardLocation = Right`

- Middle section (`Inside`):
  - Only if there is a Symbol + Label which does not belong to edges
  - `BoardLocation = Inside`

### 🔸 Labels for Table output

- `PinLine`: Line number where is a pin in README.md
- `BoardLocation`: Left / Right / Inside tells parser where the location of a Pin is relative to Board Edge which are marked with │ or ╎
- `CodeFunction`: This is for the Function in you code which you can select from available functions in that pin
- `PinLabel`: This is the name of the pin, it may contain possible Pin functions to help to choose the possible Function like (D0, A0, RX/TX) it may also contain Power and Ground markings
- `PinInOrOut`: INPUT / OUTPUT depends of the chosen direction relative to pin it's closest to marked with arrows
- `PinStatus`: The symbol used tells teh status of the pin if it's in use or if there's some special function or to be aware of probable issues
- `HasPWM`: `✓` If the symbol has `~` next to it, it's telling that it has PWM capability if needed
- `RawFragment`: If Debug enabled else not created. Original parsed board fragment for debugging if the parser is reading pins correctly and the regex is working

### 🔸 These are the Symbols for pins that boards have (`PIN_STATE`)

- `□`: Free pin
- `■`: Used pin
- `▲`: Special pin (SPI, I2C, INT, UART, Pull-up/down)
- `◊`: Caution needed (sensor, expansion, #!notation)
- `X`: Do not use (reserved, LED, unsafe)
- `≋`: DAC capable
- `↧`: Underside pin (not on header)
- `○`: Pad (solder/contact area)
- `•`: Pad in use (solder/contact area)

### 🔸 Example line for parser

D0/RX1        ← │~□ D0         VUSB □ → AGND □ │ → AGND

- Left Section:
  - `CodeFunction = D0/RX1`
  - `PinLabel = D0`
  - `PinInOrOut = OUTPUT`
  - `HasPWM`
  - `BoardLocation = Left`

- Middle section:
  - `CodeFunction = VUSB`
  - `PinLabel = VUSB`
  - `PinInOrOut = OUTPUT`
  - `BoardLocation = Inside`

- Right section:
  - `CodeFunction = AGND`
  - `PinLabel = AGND`
  - `PinInOrOut = OUTPUT`
  - `BoardLocation = Right`

### 🔹 Pin direction logic: `PinInOrOut`

The parser determines whether a pin is used as an input or output based on the arrow symbol and its position relative to any symbol marker (`■`). The logic differs depending on whether the pin is on the **left**, **right**, or **vertical** side of the layout.

#### Horizontal layout

- **The pin itself tells if the closest arrow points towards it is Input, arrow pointing away from the pin is Output**

- **Left side pin** (arrow on the left):
  - `←` before `■` = `Output`
  - `→` before `■` = `Input`

- **Right side pin** (arrow on the right):
  - `→` after `■` = `Output`
  - `←` after `■` = `Input`

-**Middle section** (Arrow should point up or down to tell if the pin is Input or Output and is determined by proximity to closest pin, see below)
  - `↑` after or before `■` = `Output`
  
#### Vertical layout (special case)

> ⚠️ In vertical layouts, arrows (`↑`, `↓`) must appear on the **same line** as the pin label or symbol marker (`■`).  
> This ensures the parser can associate the direction with the correct pin.  
> Arrows placed above or below the pin line are not supported and will be ignored.

- `↓` on the same line = `Input`
- `↑` on the same line = `Output`
- `~` on the same pin = `HasPWM`

#### Result field

```python
"PinInOrOut": "Output"  # or "Input", or "Unknown"
```

#### Examples

```
D0/RX1 ← │ ■ D0, PinInOrOut = Output

D1 │ ■ D1 → TX1, PinInOrOut = Output

■ A0 ↑, PinInOrOut = Output

■ A1 ↓, PinInOrOut = Input
```

### 🔸 There might be some visual elements embedded in the middle (`VISUAL_NOISE`)

- Removed from middle segment before fragmentation
- Noise symbols:
  - `│`, `└`, `─`, `┘`, `╱`, `╲`, `━`, `┐`, `┌`, `┬`, `┼`, `┤`, `├`, `┴`
- Also any number, letter or text here without a pin is considered as noise

### 🔸 Modular Markdown Table Generation 
```python
def generate_markdown_table(results, board_name, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# Pin and Direction Table: {board_name}\n\n")
        f.write("| PinLine | BoardLocation | CodeFunction | PinInOrOut | PinStatus | HasPWM | PinLabel |\n")
        f.write("|---------|----------------|--------------|------------|-----------|--------|----------|\n")
        for r in results:
            f.write(f"| {r['PinLine']} | {r['BoardLocation']} | {r['CodeFunction']} | {r['PinInOrOut']} | {r['PinStatus']} | {'✓' if r['HasPWM'] else ''} | {r['PinLabel']} |\n")
```
### This is the (main) function

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

### Add debug function!!!

- Add Debug function for either console or make and extra table field for raw output

### 🧩 Parser strategy (Work In Progress)

- Split the line into three sctions Left, Middle, Right
- Symnols and labels are collected from the middle
- Collectiong Function for example (D0/RX1) from text and then PinInput or Output are collected from the edges from arrow symbol
- Inside Pins are recognised by up and down arrows
- All the table fields are named logically and semantically
- If vertical Pin lines (Usually in the middle section) might be a good idea to mark somehow that the pin function is separated in grude table outside the board layout. This is hard if there's little space to write more than state, direction and PWM
  Probably a new symbol and numer to look for table outside and to get the parser connect these together. This needs to be tested. It might then set up and down arrows obsolete.

### 🔸 Config.h generation: CodeFunction → PinLabel

When the user edits the layout (`README.md`) and marks a pin as used (`■`), a `#define` line can be generated for the `config.h` file.

### 🔹 Generation conditions

- `PinStatus == "Used pin"`
- `CodeFunction` is provided
- `PinLabel` is recognized

### 🔹 Layout example

```
D0/RX1 ← │ ■ D0
```

→ Parser detects:

- `PinLabel = D0`
- `CodeFunction = D0/RX1`
- `PinStatus = Used pin`

→ Generated line for `config.h`: `#define RX1 D0`

> Note: If `CodeFunction` contains multiple names (`D0/RX1`), the last one (`RX1`) or all of them can be used, depending on the strategy.

---

### 🔹 Function: `generate_config_defines(results)`

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

- Returns a list of `#define` lines
- Can be written to `config.h` or `BOARD_NAME_config.h`
- Supports multiple names per pin

---

### 🔹 Future extension ideas

- Support for `#ifdef BOARD_NAME`
- Layout-based comments: `// Pin D0 used for RX1`
- Automatic generation for all layout folders
