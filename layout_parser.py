import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

BOARD_NAME = "Mega2560"
README_PATH = os.path.join(BOARD_NAME, "README.md")
OUTPUT_PATH = os.path.join(BOARD_NAME, f"{BOARD_NAME}.md")

PIN_STATE = {
    "□": "Free pin",
    "■": "Used pin",
    "▲": "Special pin (SPI, I2C, INT, UART, Pull-up/down)",
    "◊": "Caution needed (sensor, expansion, #!notation)",
    "X": "Do not use (reserved, LED, unsafe)",
    "≋": "DAC capable",
    "↧": "Underside pin (not on header)",
    "○": "Pad (solder/contact area)",
    "•": "Pad in use (solder/contact area)"
}

VISUAL_NOISE = r"[│└─┘╱╲━┐┌┬┼┤├┴]"

def line_has_diagram_chars(line):
    return any(char in line for char in PIN_STATE or char in "←→↑↓│")

def extract_block(line, side):
    parts = [s.strip() for s in line.split("│")]
    if len(parts) < 2:
        return None

    if side == "left":
        left = parts[0]
        right = parts[1]
        direction = "OUTPUT" if "←" in left else "INPUT"
        function = re.sub(r"[←→↑↓]", "", left).strip()
        label_match = re.findall(r"[A-Za-z0-9.]+(?:/[A-Za-z0-9.]+)?", right)
        label = label_match[0] if label_match else ""
        if function in label_match:
            label = function
        pwm = "~" in right
        symbol = next((c for c in right if c in PIN_STATE), "")
        raw = f"{left} │ {right}"
    else:
        left = parts[-2]
        right = parts[-1]
        direction = "OUTPUT" if "→" in right else "INPUT"
        function = re.sub(r"[←→↑↓]", "", right).strip()
        label_match = re.findall(r"[A-Za-z0-9.]+(?:/[A-Za-z0-9.]+)?", left)
        label = label_match[0] if label_match else ""
        if function in label_match:
            label = function
        pwm = "~" in left
        symbol = next((c for c in left if c in PIN_STATE), "")
        raw = f"{left} │ {right}"

    state = PIN_STATE.get(symbol, "Unknown")

    return {
        "raw": raw,
        "function": re.sub(VISUAL_NOISE, "", function).strip(),
        "label": label,
        "direction": direction,
        "symbol": symbol,
        "state": state,
        "pwm": pwm
    }

def debug_parse_line(line, line_number):
    if not line_has_diagram_chars(line):
        print(f"Line {line_number}: skipped (no diagram symbols)")
        return []

    results = []
    for side in ["left", "right"]:
        block = extract_block(line, side)
        if block:
            print(f"Line {line_number} [{side.capitalize()}]:")
            print(f"  Raw: '{block['raw']}'")
            print(f"  Function: '{block['function']}'")
            print(f"  Direction: {block['direction']}")
            print(f"  State: {block['state']}")
            print(f"  PWM: {'✓' if block['pwm'] else ''}")
            print(f"  Label: {block['label']}")
            results.append({
                "line": line_number,
                "side": side.capitalize(),
                **block
            })
    return results

def main():
    if not os.path.exists(README_PATH):
        print(f"❌ README.md not found in {BOARD_NAME}")
        return

    all_results = []
    with open(README_PATH, encoding="utf-8") as f:
        for i, line in enumerate(f.readlines(), start=1):
            parsed = debug_parse_line(line, i)
            all_results.extend(parsed)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(f"# Pin and Direction Table: {BOARD_NAME}\n\n")
        f.write("| Line | Side | Function | Direction | State | PWM | Label |\n")
        f.write("|------|------|----------|-----------|-------|-----|--------|\n")
        for r in all_results:
            f.write(f"| {r['line']} | {r['side']} | {r['function']} | {r['direction']} | {r['state']} | {'✓' if r['pwm'] else ''} | {r['label']} |\n")

    print(f"\n✅ Table written to: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
