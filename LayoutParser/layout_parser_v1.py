import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

BOARD_NAME = "Teensy32"
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # one level up
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
    parts = [s.strip() for s in re.split(r"[│╎]", line)]
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

def extract_inline_blocks(line, line_number):
    blocks = []
    # Etsi kaikki pinni-fragmentit: label + symbol + mahdollinen nuoli
    fragments = re.findall(r"[A-Za-z0-9./#!~]+(?:\s*[◊□■▲X≋↧○•])(?:\s*[←→])?", line)
    for frag in fragments:
        frag = frag.strip()
        symbol = next((c for c in frag if c in PIN_STATE), None)
        if not symbol:
            continue
        label_match = re.findall(r"[A-Za-z0-9./#!~]+", frag)
        label = label_match[0] if label_match else ""
        direction = "OUTPUT" if "→" in frag else "INPUT"
        pwm = "~" in frag
        state = PIN_STATE.get(symbol, "Unknown")
        blocks.append({
            "raw": frag,
            "function": re.sub(VISUAL_NOISE, "", label).strip(),
            "label": label,
            "direction": direction,
            "symbol": symbol,
            "state": state,
            "pwm": pwm
        })
    return blocks


'''
def extract_inline_blocks(line, line_number):
    blocks = []
    fragments = re.findall(r"[A-Za-z0-9./#!~]+[^A-Za-z0-9./#!~\s]*", line)
    for frag in fragments:
        frag = frag.strip()
        symbol = next((c for c in frag if c in PIN_STATE), None)
        if not symbol:
            continue
        label_match = re.findall(r"[A-Za-z0-9./#!]+", frag)
        label = label_match[0] if label_match else ""
        direction = "INPUT"
        pwm = "~" in frag
        state = PIN_STATE.get(symbol, "Unknown")
        blocks.append({
            "raw": frag,
            "function": re.sub(VISUAL_NOISE, "", label).strip(),
            "label": label,
            "direction": direction,
            "symbol": symbol,
            "state": state,
            "pwm": pwm
        })
    return blocks

'''
'''
def extract_inline_blocks(line, line_number):
    blocks = []
    tokens = re.split(r"\s{2,}|─{2,}|─+", line)  # pilko visuaalisesti erottuvista väleistä
    for token in tokens:
        token = token.strip()
        symbol = next((c for c in token if c in PIN_STATE), None)
        if not symbol:
            continue
        label_match = re.findall(r"[A-Za-z0-9.]+(?:/[A-Za-z0-9.]+)?", token)
        label = label_match[0] if label_match else ""
        direction = "INPUT"  # inline-pinnit oletetaan INPUTiksi
        pwm = "~" in token
        state = PIN_STATE.get(symbol, "Unknown")
        blocks.append({
            "raw": token,
            "function": re.sub(VISUAL_NOISE, "", label).strip(),
            "label": label,
            "direction": direction,
            "symbol": symbol,
            "state": state,
            "pwm": pwm
        })
    return blocks
'''
def debug_parse_line(line, line_number):
    if not line_has_diagram_chars(line):
        print(f"Line {line_number}: skipped (no diagram symbols)")
        return []

    symbol_count = sum(1 for c in line if c in PIN_STATE)
    results = []
    '''
    symbol_count = sum(1 for c in line if c in PIN_STATE)
    results = []

    if symbol_count > 2:
    '''
    if symbol_count > 2 and line.count("│") <= 1 and line.count("╎") <= 1:
        '''
        blocks = extract_inline_blocks(line, line_number)
        '''
    inline_blocks = extract_inline_blocks(line, line_number)

    '''
	for block in blocks:
    '''
    for block in inline_blocks:
            # Vältä duplikaatit: ohita jos label jo lisätty
            if any(r["label"] == block["label"] and r["line"] == line_number for r in results):
                continue			
            print(f"Line {line_number} [Inline]:")
            print(f"  Raw: '{block['raw']}'")
            print(f"  Function: '{block['function']}'")
            print(f"  Direction: {block['direction']}")
            print(f"  State: {block['state']}")
            print(f"  PWM: {'✓' if block['pwm'] else ''}")
            print(f"  Label: {block['label']}")
            results.append({
                "line": line_number,
                "side": "Inline",
                **block
            })
    else:
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

'''
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
'''
def main():
    if not os.path.exists(README_PATH):
        print(f"❌ README.md not found in {BOARD_NAME}")
        return

    all_results = []
    with open(README_PATH, encoding="utf-8") as f:
        line_counter = 1
        for i, line in enumerate(f.readlines(), start=1):
            parsed = debug_parse_line(line, line_counter)
            if parsed:
                all_results.extend(parsed)
                line_counter += 1

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(f"# Pin and Direction Table: {BOARD_NAME}\n\n")
        f.write("| Line | Side | Function | Direction | State | PWM | Label |\n")
        f.write("|------|------|----------|-----------|-------|-----|--------|\n")
        for r in all_results:
            f.write(f"| {r['line']} | {r['side']} | {r['function']} | {r['direction']} | {r['state']} | {'✓' if r['pwm'] else ''} | {r['label']} |\n")

    print(f"\n✅ Table written to: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
