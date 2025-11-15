# Pin and Direction Table: Teensy32

| PinLine | BoardLocation | CodeFunction | PinInOrOut | PinStatus | HasPWM | PinLabel |
|---------|----------------|--------------|------------|-----------|--------|----------|
| 8 | Inside | Vin | INPUT | Free pin |  | Vin |
| 9 | Left | D0/RX1        ← | INPUT | Do not use (reserved, LED, unsafe) |  | D0/RX1 |
| 9 | Inside | VUSB | OUTPUT | Free pin |  | VUSB |
| 9 | Inside | AGND | INPUT | Free pin |  | AGND |
| 10 | Left | D1/TX1        ← | INPUT | Do not use (reserved, LED, unsafe) |  | D1/TX1 |
| 10 | Inside | 3.3V | INPUT | Free pin |  | 3.3V |
| 11 | Inside | A11 | INPUT | Caution needed (sensor, expansion, #!notation) |  | A11 |
| 11 | Inside | D23 | INPUT | Free pin |  | D23 |
| 12 | Left | D3/CANBTX     ← | INPUT | Do not use (reserved, LED, unsafe) |  | D3/CANBTX |
| 12 | Inside | A10 | INPUT | Caution needed (sensor, expansion, #!notation) |  | A10 |
| 12 | Inside | D22 | INPUT | Free pin |  | D22 |
| 13 | Left | D4/CANBRX     ← | INPUT | Do not use (reserved, LED, unsafe) |  | D4/CANBRX |
| 13 | Right | → A7/D21/(SS)/(RX1) | OUTPUT | Do not use (reserved, LED, unsafe) |  | RX1 |
| 13 | Inside | AREF | OUTPUT | Free pin |  | AREF |
| 13 | Inside | D21 | INPUT | Free pin |  | D21 |
| 14 | Left | D5/(TX1)      ← | INPUT | Do not use (reserved, LED, unsafe) |  | TX1 |
| 14 | Inside | D20 | INPUT | Free pin |  | D20 |
| 15 | Inside | D19 | INPUT | Free pin |  | D19 |
| 16 | Left | D7/(MOSI)/RX3 ← | INPUT | Do not use (reserved, LED, unsafe) |  | /RX3 |
| 17 | Left | D8/(MISO)/RX3 ← | INPUT | Do not use (reserved, LED, unsafe) |  | /RX3 |
| 18 | Left | D9/(SS)/RX2   ← | INPUT | Do not use (reserved, LED, unsafe) |  | /RX2 |
| 19 | Left | D10/SS/TX2    ← | INPUT | Do not use (reserved, LED, unsafe) |  | D10/SS/TX2 |
| 20 | Inside | D14 | INPUT | Free pin |  | D14 |
| 21 | Inside | LED | INPUT | Caution needed (sensor, expansion, #!notation) |  | LED/D13 |
| 40 | Inside | #!3 | INPUT | Pad (solder/contact area) |  | #!3 |
| 42 | Left | A13 ←↧ | INPUT | Underside pin (not on header) |  | A13 |
| 42 | Right | ↧→ A12 | OUTPUT | Underside pin (not on header) |  | A12 |
| 43 | Left | 3.3V ←↧ | INPUT | Underside pin (not on header) |  | 3.3V |
| 43 | Right | ↧→ GND | OUTPUT | Underside pin (not on header) |  | GND |
| 44 | Left | D33 ←↧ | INPUT | Underside pin (not on header) |  | D33 |
| 44 | Right | ↧→ D24 | OUTPUT | Underside pin (not on header) |  | D24 |
| 45 | Left | D32 ←↧ | INPUT | Underside pin (not on header) |  | D32 |
| 45 | Right | ↧→ D25 | OUTPUT | Underside pin (not on header) |  | D25 |
| 46 | Left | D31/A20/(TX2) ←↧ | INPUT | Do not use (reserved, LED, unsafe) |  | TX2 |
| 46 | Right | ↧→ D26/A15/(RX2) | OUTPUT | Underside pin (not on header) |  | RX2 |
| 46 | Inside | D26 | INPUT | Pad (solder/contact area) |  | D26 |
| 47 | Left | D30/A19/SDA1 ←↧ | INPUT | Underside pin (not on header) |  | D30/A19/SDA1 |
| 47 | Right | ↧→ D26/A15 | OUTPUT | Underside pin (not on header) |  | D26/A15 |
| 47 | Inside | D27 | INPUT | Pad (solder/contact area) |  | D27 |
| 48 | Left | D29/A18/SCL1 ←↧ | INPUT | Underside pin (not on header) |  | D29/A18/SCL1 |
| 48 | Right | ↧→ D26/A15 | OUTPUT | Underside pin (not on header) |  | D26/A15 |
| 48 | Inside | D28 | INPUT | Pad (solder/contact area) |  | D28 |