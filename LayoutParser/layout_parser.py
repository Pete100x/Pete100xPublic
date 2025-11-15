# -*- coding: utf-8 -*-
import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

BOARD_NAME = "Teensy32"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))  # LayoutParser/
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))  # Projektin juuri
README_PATH = os.path.join(BASE_DIR, BOARD_NAME, "README.md")
OUTPUT_PATH = os.path.join(BASE_DIR, BOARD_NAME, f"{BOARD_NAME}.md")

print("README_PATH:", README_PATH)
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

def extract_block(segment, board_location, code_function):
    symbol = next((c for c in segment if c in PIN_STATE), None)
    if not symbol:
        return None
    label_match = re.findall(r"[A-Za-z0-9./#!~]+", segment)
    pin_label = label_match[-1] if label_match else ""
    if pin_label == "~":
        return None
    pin_in_or_out = "OUTPUT" if "→" in segment else "INPUT"
    has_pwm = "~" in segment
    pin_status = PIN_STATE.get(symbol, "Unknown")
    return {
        "RawFragment": segment.strip(),
        "CodeFunction": code_function.strip(),
        "PinLabel": pin_label,
        "PinInOrOut": pin_in_or_out,
        "Symbol": symbol,
        "PinStatus": pin_status,
        "HasPWM": has_pwm,
        "BoardLocation": board_location
    }

def extract_inside_blocks(middle, pin_line, left_label, right_label):
    blocks = []
    PIN_SYMBOLS = "".join(PIN_STATE.keys())
    cleaned = re.sub(VISUAL_NOISE, " ", middle)
    fragments = re.findall(r"[A-Za-z0-9./#!~]+(?:\s*[" + PIN_SYMBOLS + r"])(?:\s*[←→])?", cleaned)
    for frag in fragments:
        frag = frag.strip()
        symbol = next((c for c in frag if c in PIN_STATE), None)
        if not symbol:
            continue
        label_match = re.findall(r"[A-Za-z0-9./#!~]+", frag)
        pin_label = label_match[-1] if label_match else ""
        if pin_label in [left_label, right_label] or pin_label == "~":
            continue
        pin_in_or_out = "OUTPUT" if "→" in frag else "INPUT"
        has_pwm = "~" in frag
        pin_status = PIN_STATE.get(symbol, "Unknown")
        blocks.append({
            "PinLine": pin_line,
            "BoardLocation": "Inside",
            "RawFragment": frag,
            "CodeFunction": pin_label.split("/")[0],
            "PinLabel": pin_label,
            "PinInOrOut": pin_in_or_out,
            "Symbol": symbol,
            "PinStatus": pin_status,
            "HasPWM": has_pwm
        })
    return blocks

def debug_parse_line(line, pin_line):
    results = []
    parts = [s.strip() for s in re.split(r"[│╎]", line)]
    if len(parts) < 3:
        print(f"PinLine {pin_line}: skipped (not enough parts)")
        return results

    left_segment = parts[0]  # D0/RX1 ←
    middle_segment = parts[1]  # □ D0         VUSB □ → AGND □
    right_segment = parts[2]  # → AGND

    left_block = extract_block(left_segment, "Left", left_segment)
    right_block = extract_block(right_segment, "Right", right_segment)


    if left_block:
        print(f"PinLine {pin_line} [Left]:")
        for k, v in left_block.items():
            print(f"  {k}: {v}")
        results.append({
            "PinLine": pin_line,
            **left_block
        })

    if right_block:
        print(f"PinLine {pin_line} [Right]:")
        for k, v in right_block.items():
            print(f"  {k}: {v}")
        results.append({
            "PinLine": pin_line,
            **right_block
        })

    left_label = left_block["PinLabel"] if left_block else None
    right_label = right_block["PinLabel"] if right_block else None

    inside_blocks = extract_inside_blocks(middle_segment, pin_line, left_label, right_label)
    for block in inside_blocks:
        print(f"PinLine {pin_line} [Inside]:")
        for k, v in block.items():
            print(f"  {k}: {v}")
        results.append(block)

    return results

def generate_markdown_table(results):
    lines = []
    lines.append(f"# Pin and Direction Table: {BOARD_NAME}\n")
    lines.append("| PinLine | BoardLocation | CodeFunction | PinInOrOut | PinStatus | HasPWM | PinLabel |")
    lines.append("|---------|----------------|--------------|------------|-----------|--------|----------|")
    for r in results:
        pwm_mark = "✓" if r.get("HasPWM") else ""
        lines.append(
            f"| {r['PinLine']} | {r['BoardLocation']} | {r['CodeFunction']} | {r['PinInOrOut']} | {r['PinStatus']} | {pwm_mark} | {r['PinLabel']} |"
        )
    return "\n".join(lines)

def main():
    if not os.path.exists(README_PATH):
        print(f"❌ README.md not found in {BOARD_NAME}")
        return

    all_results = []
    with open(README_PATH, encoding="utf-8") as f:
        for i, line in enumerate(f.readlines(), start=1):
            parsed = debug_parse_line(line, i)
            if parsed:
                all_results.extend(parsed)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(generate_markdown_table(all_results))

    print(f"\n✅ Table written to: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
