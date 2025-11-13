# Arduino Uno R3 ATmega328P
												  
                        ┌─────┐                  ┌─────┐
                   ┌────┤ PWR ├──────────────────┤ USB ├───┐
                   │    │6–20V│                  │  B  │ ● │(RST BTN)
                   │    └─────┘GND/RST2 ←□  □→   └─────┘   │       
                   │         MOSI2/SCK2 ←□  □→SCL/A5/D19 □ │   → A5/D19
                   │           5V/MISO2 ←□  □→SDA/A4/D18 □ │   → A4/D18
                   │                                AREF □ │   → AREF
                   │                                 GND □ │   → GND
       N/C     ←   │ □ N/C                    ED/SCK/D13 □ │   → D13
       IOREF   ←   │ □ IOREF                    MISO/D12 □ │   → D12
       RST     ←   │ □ RST                      MOSI/D11 □~│   → D11
       3V3     ←   │ □ 3V3     ┌───┐                 D10 □~│   → D10
       5V      ←   │ □ 5V      │ A │                  D9 □~│   → D9
       GND     ←   │ □ GND     │ R │                  D8 □ │   → D8
       GND     ←   │ □ GND     │ D │                       │       
       Vin     ←   │ □ Vin     │ U │                  D7 □ │   → D7
                   │           │ I │                  D6 □~│   → D6
       A0/D14  ←   │ □ A0/D14  │ N │                  D5 □~│   → D5
       A1/D15  ←   │ □ A1/D15  │ O │                  D4 □ │   → D4
       A2/D16  ←   │ □ A2/D16  └───┘             INT1/D3 □~│   → D3
       A3/D17  ←   │ □ A3/D17                    INT0/D2 □ │   → D2
       A4/D18  ←   │ □ A4/D18    RST SCK MISO      TX>D1 □ │   → D1
       A5/D19  ←   │ □ A5/D19     □↑  □↑  □↑       RX<D0 □ │   → D0
                   │              □↓  □↓  □↓               │     
                   ╰╮ UNO_R3    GND MOSI  5V╭──────────────╯   
                    ╰───────────────────────╯ 

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