## Sources

Some of the ASCII pinout diagrams in this repository are based on or adapted from publicly available resources:

- [Busy Ducks – ASCII Art Arduino Pinouts](https://busyducks.com/ascii-art-arduino-pinouts/index.html)
- [Arduino Nano by /u/plasticluthier](https://www.reddit.com/r/arduino/comments/3tb0d2/i_made_some_asciiart_arduinos_to_paste_in/cx5oyjp)
- [SP-8266 D1-Mini by pete100x](https://github.com/Pete100x/Pete100xPublic/tree/main/AllLayouts) 

The diagrams have been visually and technically modified to match the documentation style and layout used in this project. Original versions are available at the link above.

USB connector types:
- **B** = USB-B (large square connector, e.g. Mega, Uno)
- **b** = USB-B mini (e.g. Nano)
- **μ** = USB Micro-B (e.g. Teensy 3.2)
- **C** = USB-C (e.g. D1 Mini)

These symbols indicate the physical USB connector type used on each board.
They are shown in the diagram header or near the USB port for quick identification.

# Arduino Nano-V3 ATmega328P       

                                ┌─────┐               
                   ┌────────────┤USB-b├────────────┐  
                   │            └─────┘            │  
          D13  ←   │ □ LED/D13/SCK      MISO/D12 □ │   → D12
          3.3V ←   │ □ 3.3V        ^    MOSI/D11 □~│   → D11
          AREF ←   │ □ AREF       ╱ ╲     SS/D10 □~│   → D10
          A0   ←   │ □ A0        ╱ N ╲        D9 □~│   → D9
          A1   ←   │ □ A1       ╱  A  ╲       D8 □ │   → D8
          A2   ←   │ □ A2       ╲  N  ╱       D7 □ │   → D7
          A3   ←   │ □ A3        ╲ O ╱        D6 □~│   → D6
          A4   ←   │ □ SDA/A4     ╲ ╱         D5 □~│   → D5
          A5   ←   │ □ SCL/A5      v          D4 □ │   → D4
          A6   ←   │ □ A6                INT1/D3 □~│   → D3
          A7   ←   │ □ A7          ●     INT0/D2 □ │   → D2
          5V   ←   │ □ 5V      (RST BTN)     GND □ │   → GND
          RST  ←   │ □ RST                   RST □ │   → RST
          GND  ←   │ □ GND    5V MOSI GND TX1/D0 □ │   → D0
          Vin  ←   │ □ Vin     □↑  □↑  □↑ RX1/D1 □ │   → D1
                   │           □↓  □↓  □↓          │  
                   │         MISO SCK RST          │  
                   │                               │ 
                   │ ATmega328P NANO-V3            │  
                   └───────────────────────────────┘  

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
