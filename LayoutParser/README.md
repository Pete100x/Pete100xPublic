# 🧠 LayoutParser – Pin Layout Parser Logic

This module defines the logic for parsing pin layout diagrams from each board's `README.md`. It extracts structured data from Unicode-based diagrams and converts it into machine-readable JSON.

---

## 🔍 What It Parses

Each line in a board-specific `README.md` contains a visual pin annotation like:

```text
← │ □ D13/SCK #!4
```

The parser extracts:

- `line_number`: Line index in the file
- `direction`: Arrow symbol (`←`, `→`, `↧`, etc.)
- `symbol`: Usage symbol (`□`, `■`, `○`, etc.)
- `label`: Pin name (`D13`, `A10`, `TX`, etc.)
- `annotations`: Any `#!` markers (e.g. `#!4`, `#!PULLUP`)

---

## 🧩 JSON Output Format

```text
[
  {
    "line_number": 12,
    "direction": "←",
    "symbol": "□",
    "label": "D13/SCK",
    "annotations": ["#!4"]
  },
  ...
]
```

---

## 📘 Symbol Legend

| Symbol | Meaning              |
|--------|----------------------|
| `□`    | Free pin             |
| `■`    | Used pin             |
| `◊`    | Caution / special    |
| `≈`    | DAC output           |
| `○`    | Pad (not header)     |
| `•`    | Pad in use           |

---

## ➡️ Direction Legend

| Arrow | Meaning                     |
|-------|-----------------------------|
| `←`   | Output (data leaves pin)    |
| `→`   | Input (data enters pin)     |
| `↧`   | Underside pin or pad        |
| `↑`   | Input from top (optional)   |
| `↓`   | Output downward (optional)  |

---

## ⚠️ Error Detection

The parser flags:

- Missing direction or symbol
- Unknown symbols or arrows
- Duplicate labels
- Unclosed code blocks
- Floating inputs without pull-up/down logic

---

## 🛠️ Use Cases

- Generate pin usage reports
- Validate documentation consistency
- Auto-generate `config.h` or pin maps
- Visualize pin usage per board
- Detect undocumented or ambiguous pins

---

## 📂 Integration

Each board folder (e.g. `Mega2560/`, `Teensy32/`) contains a `README.md` with parsable layout. The parser runs across all folders and outputs structured data for further use.

---

## 📌 Notes

- All diagrams use Unicode box-drawing characters
- All annotations use `#!` prefix
- All files are UTF-8 encoded and Markdown-compliant
