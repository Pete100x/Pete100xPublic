# Arduino Mega ATmega2560

       
                        ┌─────┐                 ┌─────┐
                   ┌────┤ PWR ├─────────────────┤ USB ├──┐
                   │    │6–20V│                 │  B  │  │
                   │    └─────┘ GND/RST2 ←□  □→ └─────┘  │
                   │          MOSI2/SCK2 ←□  □→ SCL/D0 □ │   →   D0
                   │            5V/MISO2 ←□  □→ SDA/D1 □ │   →   D1
                   │                              AREF □ │   →   AREF
                ←  │                               GND □ │   →   GND 
       N/C      ←  │ □ N/C                     LED/D13 □~│   →   D13
       IOREF    ←  │ □ IOREF                       D12 □~│   →   D12
       RST      ←  │ □ RST                         D11 □~│   →   D11
       3.3V     ←  │ □ 3.3V      ┌──────────┐      D10 □~│   →   D10
       5V       ←  │ □ 5V        │ ARDUINO  │       D9 □~│   →   D9
       GND      ←  │ □ GND       │ ATMEGA   │       D8 □~│   →   D8
       GND      ←  │ □ GND       │ 2560     │            │
       Vin      ←  │ □ Vin       └──────────┘       D7 □~│   →   D7
                   │                                D6 □~│   →   D6
       A0/D54   ←  │ □ A0/D54                  INT5/D5 □~│   →   D5
       A1/D55   ←  │ □ A1/D55                  INT4/D4 □~│   →   D4
       A2/D56   ←  │ □ A2/D56                  INT3/D3 □~│   →   D3
       A3/D57   ←  │ □ A3/D57                  INT2/D2 □~│   →   D2
       A4/D58   ←  │ □ A4/D58                   TX1/D1 □~│   →   D1
       A5/D59   ←  │ □ A5/D59                   RX0/D0 □~│   →   D0
       A6/D60   ←  │ □ A6/D60                            │
       A7/D61   ←  │ □ A7/D61                  TX3/D14 □ │   →   D14
                   │                           RX3/D15 □ │   →   D15
       A8/D62   ←  │ □ A8/D62                  TX2/D16 □ │   →   D16
       A9/D63   ←  │ □ A9/D63                  RX2/D17 □ │   →   D17
       A10/D64  ←  │ □ A10/D64            TX1/INT1/D18 □ │   →   D18
       A11/D65  ←  │ □ A11/D65            RX1/INT0/D19 □ │   →   D19
       A12/D66  ←  │ □ A12/D66        I2C-SDA/INT3/D20 □ │   →   D20
       A13/D67  ←  │ □ A13/D67        I2C-SCL/INT2/D21 □ │   →   D21
       A14/D68  ←  │ □ A14/D68                           │
       A15/D69  ←  │ □ A15/D69     RST SCK MISO          │   ← □ 22 = D22/A0    ← □ 23 = D23/A1         
                   │           ICSP □↑  □↑  □↑           │   ← □ 24 = D24/A2    ← □ 25 = D25/A3         
                   │                □↓  □↓  □↓           │   ← □ 26 = D26/A4    ← □ 27 = D27/A5         
                   │               GND MOSI 5V           │   ← □ 28 = D28/A6    ← □ 29 = D29/A7         
                   │                  ● (RST BTN)        │   ← □ 30 = D30       ← □ 31 = D31         
                   │ G                                   │   ← □ 32 = D32       ← □ 33 = D33         
                   │ N 5 5 4 4 4 4 4 3 3 3 3 3 2 2 2 2 5 │   ← □ 34 = D34       ← □ 35 = D35         
                   │ D 2 0 8 6 4 2 0 8 6 4 2 0 8 6 4 2 V │   ← □ 36 = D36       ← □ 37 = D37         
                   │         ~ ~                         │   ← □ 38 = D38       ← □ 39 = D39         
                   │ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ │   ← □ 40 = D40       ← □ 41 = D41         
                   │ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ │   ← □ 42 = D42       ← □ 43 = D43         
                   │ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ │   ← □~44 = D44       ← □~45 = D45         
                   │ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ │   ← □~46 = D46       ← □ 47 = D47         
                   │           ~                         │   ← □ 48 = D48       ← □ 49 = D49         
                   │ G 5 5 4 4 4 4 4 3 3 3 3 3 2 2 2 2 5 │   ← □ 50 = D50/MISO  ← □ 51 = D51/MOSI         
                   │ N 3 1 9 7 5 3 1 9 7 5 3 1 9 7 5 3 V │   ← □ 52 = D52/SCK   ← □ 53 = D53/SS         
                   │ D                                   │                                              
                   │                                     │                                           
                   │ ATMEGA2560              ╭───────────╯ 
                   ╰─────────────────────────╯
	              
                   □ = Free pin (default)  
                   ■ = Used pin  
                   ▲ = Special pin (SPI, I2C, INT, UART, Pull-up, Pull-down)  
                   ◊ = Caution needed pin (sensor, expansion, special requirements)  
                   X = Do not use (reserved, LED or unsafe)    
                   ~ = PWM capable (append to pin label)  
                   ● = Onboard reset button  
                   → = Pin used in code or config (logical direction only; all arrows point outward for consistency)				

    These symbols are used consistently across all board diagrams to clarify pin availability and function.  
    Special pins (▲) may overlap with digital or analog pins depending on context (e.g. SDA = A4 = D18).
#