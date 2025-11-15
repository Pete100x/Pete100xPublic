# Pin and Direction Table: Teensy32

| PinLine | BoardLocation | CodeFunction | PinInOrOut | PinStatus | HasPWM | PinLabel |
|---------|----------------|--------------|------------|-----------|--------|----------|
| 8 | Left | GND           ← | INPUT | Free pin |  | Vin |
| 9 | Left | D0/RX1        ← | OUTPUT | Free pin |  | VUSB |
| 9 | Right | → AGND | INPUT | Free pin |  | AGND |
| 10 | Left | D1/TX1        ← | INPUT | Free pin |  | 3.3V |
| 11 | Left | D2            ← | INPUT | Caution needed (sensor, expansion, #!notation) |  | A11 |
| 11 | Right | → A9/D23 | INPUT | Free pin |  | D23 |
| 12 | Right | → A8/D22 | INPUT | Free pin |  | D22 |
| 12 | Inside | A10 ◊ | INPUT | Caution needed (sensor, expansion, #!notation) |  | A10 |
| 13 | Right | → A7/D21/(SS)/(RX1) | INPUT | Free pin |  | D21 |
| 13 | Inside | AREF □ → | OUTPUT | Free pin |  | AREF |
| 14 | Right | → A6/D20/(SS) | INPUT | Free pin |  | D20 |
| 15 | Right | → A5/D19/SCL | INPUT | Free pin |  | D19 |
| 20 | Left | D11/MOSI      ← | INPUT | Free pin |  | D14 |
| 21 | Left | D12/MISO      ← | INPUT | Caution needed (sensor, expansion, #!notation) |  | LED/D13 |
| 40 | Left |  | INPUT | Pad (solder/contact area) |  | #!3 |
| 42 | Left | A13 ←↧ | INPUT | Pad (solder/contact area) |  | A12 |
| 43 | Left | 3.3V ←↧ | INPUT | Pad (solder/contact area) |  | GND |
| 44 | Left | D33 ←↧ | INPUT | Pad (solder/contact area) |  | D24 |
| 45 | Right | ↧→ D25 | INPUT | Pad (solder/contact area) |  | D25 |
| 46 | Left | D31/A20/(TX2) ←↧ | INPUT | Pad (solder/contact area) |  | D26 |
| 47 | Left | D30/A19/SDA1 ←↧ | INPUT | Pad (solder/contact area) |  | D27 |
| 48 | Left | D29/A18/SCL1 ←↧ | INPUT | Pad (solder/contact area) |  | D28 |