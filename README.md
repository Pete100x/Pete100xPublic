# Pete100xPublic
## This is where I Upload publicly available various documents

# 🧠 Modular Hardware Pinout Documentation

This repository contains universal, parsable pinout diagrams for various microcontroller boards. Each board has its own folder with:

- A Unicode-based visual layout
- Symbol and arrow legend
- Parsable pin table with direction, usage, and annotations
- Optional `#!` notes for special cases

## 📂 Boards

| Board         | Description                        | Link |
|---------------|------------------------------------|------|
| 🧠 AllLayouts  | Design notebook and ASCII drafts   | [AllLayouts](./AllLayouts/README.md) |
| 🔵 Mega 2560   | High I/O count, SPI/I2C/UART/DAC   | [Mega2560](./Mega2560/README.md)     |
| 🔹 Nano        | Compact 5V AVR board               | [Nano](./Nano/README.md)             |
| 🔸 Uno         | Classic 5V AVR board               | [Uno](./Uno/README.md)               |
| 🟢 Teensy 3.2  | ARM Cortex-M4, 3.3V, DAC capable   | [Teensy32](./Teensy32/README.md)     |
| 🟠 ESP8266 D1 Mini | ESP8266 WiFi, 3.3V             | [ESP8266 D1 Mini](./ESP8266_D1_Mini/README.md) |
| 🟣 Sunton CYB  | ESP32 with display, 3.3V           | [SuntonCYB](./SuntonCYB/README.md)   |

## 🧩 Symbol Legend

| Symbol | Meaning              |
|--------|----------------------|
| `□`    | Free pin             |
| `■`    | Used pin             |
| `◊`    | Caution / special    |
| `≈`    | DAC output           |
| `○`    | Pad (not header)     |
| `•`    | Pad in use           |

## ➡️ Direction Legend

| Arrow | Meaning                     |
|-------|-----------------------------|
| `←`   | Output (data leaves pin)    |
| `→`   | Input (data enters pin)     |
| `↧`   | Underside pin or pad        |
| `↑`   | Input from top (optional)   |
| `↓`   | Output downward (optional)  |

## 📘 Pin Function Reference

| Label     | Meaning                                | Usage                                            |
|-----------|----------------------------------------|--------------------------------------------------|
| `TX`      | UART Transmit (data out)               | `Serial.begin(9600); Serial.print("Hello");`     |
| `RX`      | UART Receive (data in)                 | `Serial.read();`                                 |
| `A0–AXX`  | Analog input pins (10-bit ADC)         | `analogRead(A0);`                                |
| `D0–DXX`  | Digital I/O pins                       | `digitalWrite(D2, HIGH);` / `digitalRead(D2);`   |
| `PWM or ~`| Pulse Width Modulation capable pin     | `analogWrite(D3, 128);`                          |
| `SDA`     | I2C Data line                          | `Wire.begin(); Wire.write(data);`                |
| `SCL`     | I2C Clock line                         | `Wire.beginTransmission(addr);`                  |
| `MOSI`    | SPI Master Out Slave In                | `SPI.transfer(data);`                            |
| `MISO`    | SPI Master In Slave Out                | (read automatically during `SPI.transfer()`)     |
| `SCK`     | SPI Clock                              | Controlled by `SPI.begin()`                      |
| `SS or CS`| SPI Slave Select or Chip Select        | `digitalWrite(SS, LOW);`                         |
| `DAC`     | Digital-to-Analog Output (if available)| `analogWrite(DAC0, value);` (Teensy/ESP32)       |
| `IOREF`   | Logic level reference (3.3V or 5V)     | Read-only reference pin                          |
| `AREF`    | Analog level reference (3.3V or 5V)    | `analogReference(EXTERNAL);`                     |
| `Vin`     | External power input                   | Connect 7–12V DC input                           |
| `GND`     | Ground                                 | Common ground                                    |
| `3.3V`    | Regulated 3.3V output                  | Power 3.3V sensors                               |
| `5V`      | Regulated 5V output                    | Power 5V sensors                                 |
| `RESET`   | Manual or software reset               | `digitalWrite(RESET, LOW);` (if allowed)         |
| `CANBTX`  | CAN Bus Transmit (data out)            | `CAN.write(msg);` (with CAN library)             |
| `CANBRX`  | CAN Bus Receive (data in)              | `CAN.read();`                                    |
| `VBat`    | External 3.3V battery input            | Connect LiPo or coin cell                        |


---

## 🧠 Input Modes: Pull-up and Pull-down

| Label             | Meaning                                 | Usage                                             |
|-------------------|------------------------------------------|---------------------------------------------------|
| `INPUT`           | Digital input                            | `pinMode(pin, INPUT);`                            |
| `INPUT_PULLUP`    | Internal pull-up resistor (~20–50kΩ)     | `pinMode(pin, INPUT_PULLUP);`                     |
| `INPUT_PULLDOWN`  | Internal pull-down resistor (if available)| `pinMode(pin, INPUT_PULLDOWN);`                   |
| `Pulldown`        | External pull-down resistor required      | `pinMode(pin, INPUT);` + external 10kΩ to GND     |

> **Note:** When using `pinMode(pin, INPUT)`, always use pull-up or pull-down logic when reading buttons, switches, or sensors to avoid floating states.

### 🧠 What Is a Floating Pin?

A **floating pin** is a digital input that is not connected to a defined voltage level. This happens when:

- The pin is set to `INPUT`
- There is no internal pull-up or pull-down resistor
- There is no external resistor or connected device

#### ⚠️ Why It Matters

Floating pins can cause:

- Unstable readings (`digitalRead()` may return HIGH or LOW randomly)
- Electromagnetic interference sensitivity
- Unpredictable behavior in logic or control systems

#### ✅ How to Fix It

Use one of the following methods to ensure a stable input:

| Method              | Description                                      | Example                                  |
|---------------------|--------------------------------------------------|------------------------------------------|
| `INPUT_PULLUP`      | Enables internal pull-up resistor (~20–50kΩ)     | `pinMode(pin, INPUT_PULLUP);`            |
| `INPUT_PULLDOWN`    | Enables internal pull-down resistor (if supported) | `pinMode(pin, INPUT_PULLDOWN);`          |
| External pull-down  | Connect 10kΩ resistor between pin and GND        | `pinMode(pin, INPUT);` + resistor        |

## 🧠 Parsing Logic

Each pin line follows this structure:

```text
← │ □ D13/SCK #!4
The parser extracts:

Direction (←)

Symbol (□)

Label (D13/SCK)

Annotations (#!4)

Line number (automatically)

🛠 Parser Access
See Parser for pseudocode, examples, and usage instructions.
```
