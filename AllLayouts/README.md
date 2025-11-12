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

####

         First Conversion to UniCode
                                ┌─────┐
                   ┌────────────┤ USB ├────────────┐
                   │            └─────┘            │
          B5   ←   │ [ ]D13/SCK        MISO/D12[ ] │   →   B4
               ←   │ [ ]3.3V           MOSI/D11[ ]~│   →   B3
               ←   │ [ ]V.ref     ⎯⎯⎯    SS/D10[ ]~│   →   B2
          C0   ←   │ [ ]A0       ╱ N ╲       D9[ ]~│   →   B1
          C1   ←   │ [ ]A1      ╱  A  ╲      D8[ ] │   →   B0
          C2   ←   │ [ ]A2      ╲  N  ╱      D7[ ] │   →   D7
          C3   ←   │ [ ]A3       ╲_0_/       D6[ ]~│   →   D6
          C4   ←   │ [ ]A4/SDA               D5[ ]~│   →   D5
          C5   ←   │ [ ]A5/SCL               D4[ ] │   →   D4
               ←   │ [ ]A6              INT1/D3[ ]~│   →   D3
               ←   │ [ ]A7              INT0/D2[ ] │   →   D2
               ←   │ [ ]5V                  GND[ ] │   →    
          C6   ←   │ [ ]RST                 RST[ ] │   →   C6
               ←   │ [ ]GND   5V MOSI GND   TX1[ ] │   →   D0
               ←   │ [ ]Vin   [ ] [ ] [ ]   RX1[ ] │   →   D1
               ←   │          [ ] [ ] [ ]          │
               ←   │          MISO SCK RST         │
               ←   │ NANO-V3                       │
                   └───────────────────────────────┘
		
####
 
####	Original ASCII art below: Nano-v3

		  	 
                                +-----+
                   +------------| USB |------------+
                   |            +-----+            |
              B5   | [ ]D13/SCK        MISO/D12[ ] |   B4
                   | [ ]3.3V           MOSI/D11[ ]~|   B3
                   | [ ]V.ref     ___    SS/D10[ ]~|   B2
              C0   | [ ]A0       / N \       D9[ ]~|   B1
              C1   | [ ]A1      /  A  \      D8[ ] |   B0
              C2   | [ ]A2      \  N  /      D7[ ] |   D7
              C3   | [ ]A3       \_0_/       D6[ ]~|   D6
              C4   | [ ]A4/SDA               D5[ ]~|   D5
              C5   | [ ]A5/SCL               D4[ ] |   D4
                   | [ ]A6              INT1/D3[ ]~|   D3
                   | [ ]A7              INT0/D2[ ] |   D2
                   | [ ]5V                  GND[ ] |     
              C6   | [ ]RST                 RST[ ] |   C6
                   | [ ]GND   5V MOSI GND   TX1[ ] |   D0
                   | [ ]Vin   [ ] [ ] [ ]   RX1[ ] |   D1
                   |          [ ] [ ] [ ]          |
                   |          MISO SCK RST         |
                   | NANO-V3                       |
                   +-------------------------------+
####		 

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

####	Original ASCII art below: Uno R3

                                                +-----+
                   +----[PWR]-------------------| USB |--+
                   |                            +-----+  |
                   |           GND/RST2  [ ] [ ]         |
                   |         MOSI2/SCK2  [ ] [ ]  SCL[ ] |   C5
                   |            5V/MISO2 [ ] [ ]  SDA[ ] |   C4
                   |                             AREF[ ] |
                   |                              GND[ ] |
                   | [ ]N/C                    SCK/13[A] |   B5
                   | [ ]v.ref                 MISO/12[A] |   .
                   | [ ]RST                   MOSI/11[A]~|   .
                   | [ ]3V3    +---+               10[ ]~|   .
                   | [ ]5v     | A |                9[ ]~|   .
                   | [ ]GND   -| R |-               8[B] |   B0
                   | [ ]GND   -| D |-                    |
                   | [ ]Vin   -| U |-               7[A] |   D7
                   |          -| I |-               6[A]~|   .
                   | [ ]A0    -| N |-               5[C]~|   .
                   | [ ]A1    -| O |-               4[A] |   .
                   | [ ]A2     +---+           INT1/3[A]~|   .
                   | [ ]A3                     INT0/2[ ] |   .
                   | [ ]A4      RST SCK MISO     TX>1[ ] |   .
                   | [ ]A5      [ ] [ ] [ ]      RX<0[ ] |   D0
                   |            [ ] [ ] [ ]              |
                   |  UNO_R3    GND MOSI 5V  ____________/
                    \_______________________/
####		                

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


####	Original ASCII art below; Arduino Mega


                                                +-----+
                   +----[PWR]-------------------| USB |--+
                   |                            +-----+  |
                   |           GND/RST2  [ ] [ ]         |
                   |         MOSI2/SCK2  [ ] [ ]  SCL[ ] |   D0
                   |            5V/MISO2 [ ] [ ]  SDA[ ] |   D1
                   |                             AREF[ ] |
                   |                              GND[ ] |
                   | [ ]N/C                        13[ ]~|   B7
                   | [ ]IOREF                      12[ ]~|   B6
                   | [ ]RST                        11[ ]~|   B5
                   | [ ]3V3      +----------+      10[ ]~|   B4
                   | [ ]5v       | ARDUINO  |       9[ ]~|   H6
                   | [ ]GND      |   MEGA   |       8[ ]~|   H5
                   | [ ]GND      +----------+            |
                   | [ ]Vin                         7[ ]~|   H4
                   |                                6[ ]~|   H3
                   | [ ]A0                          5[ ]~|   E3
                   | [ ]A1                          4[ ]~|   G5
                   | [ ]A2                     INT5/3[ ]~|   E5
                   | [ ]A3                     INT4/2[ ]~|   E4
                   | [ ]A4                       TX>1[ ]~|   E1
                   | [ ]A5                       RX<0[ ]~|   E0
                   | [ ]A6                               |   
                   | [ ]A7                     TX3/14[ ] |   J1
                   |                           RX3/15[ ] |   J0
                   | [ ]A8                     TX2/16[ ] |   H1         
                   | [ ]A9                     RX2/17[ ] |   H0
                   | [ ]A10               TX1/INT3/18[ ] |   D3         
                   | [ ]A11               RX1/INT2/19[ ] |   D2
                   | [ ]A12           I2C-SDA/INT1/20[ ] |   D1         
                   | [ ]A13           I2C-SCL/INT0/21[ ] |   D0
                   | [ ]A14                              |            
                   | [ ]A15                              |   Ports:
                   |              RST SCK MISO           |    22=A0  23=A1   
                   |         ICSP [ ] [ ] [ ]            |    24=A2  25=A3   
                   |              [ ] [ ] [ ]            |    26=A4  27=A5   
                   |              GND MOSI 5V            |    28=A6  29=A7   
                   | G               ● (RST BTN)         |    30=C7  31=C6   
                   | N 5 5 4 4 4 4 4 3 3 3 3 3 2 2 2 2 5 |    32=C5  33=C4   
                   | D 2 0 8 6 4 2 0 8 6 4 2 0 8 6 4 2 V |    34=C3  35=C2   
                   |         ~ ~                         |    36=C1  37=C0   
                   |                                     |    38=D7  39=G2            
                   | # # # # # # # # # # # # # # # # # # |    40=G1  41=G0    
                   | # # # # # # # # # # # # # # # # # # |    42=L7  43=L6   
                   |                                     |    44=L5  45=L4            
                   |           ~                         |    46=L3  47=L2   
                   | G 5 5 4 4 4 4 4 3 3 3 3 3 2 2 2 2 5 |    48=L1  49=L0   
                   | N 3 1 9 7 5 3 1 9 7 5 3 1 9 7 5 3 V |    50=B3  51=B2   
                   | D                                   |    52=B1  53=B0    SPI:
                   |                                     |                     50=MISO 51=MOSI
                   |     2560                ____________/                     52=SCK  53=SS 
                    \_______________________/  

####	               

#  D1 Mini ESP8266
  
                   ╭────────────┬─────┬────────────╮ 
                   │            │ ESP │            │
                   │            │  8  │            │
          RST   ←  │ □ RST      │  2  │ TX/GPIO1 ▲ │  →   GPIO1
         ADC0   →  │ ◊ A0       │  6  │ RX/GPIO3 ▲ │  ←   GPIO3
    GPIO16/D0   ←  │ □ D0/WAKE  │  6  │   SCL/D1 □~│  →   D1/GPIO5
    GPIO14/D5   ←  │~□ D5/SCLK  └─────┘   SDA/D2 □~│  →   D2/GPIO4
    GPIO12/D6   ←  │~□ D6/MISO          FLASH/D3 ▲~│  →   D3/GPIO0
    GPIO13/D7   ←  │~□ D7/MOSI            LED/D4 □~│  →   D4/GPIO2
    GPIO15/D8   ←  │~▲ D8/CS                 GND □ │  →   GND
         3.3V   ←  │ □ 3.3V                   5V □ │  →   5V
                   ╰─╮                             │
                    ●│(RST BTN) ┌─────┐  D1 MINI   │
                     └──────────┤USB-C├────────────┘
                                └─────┘              
        
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
    
    *Note: 
	- Pin D3 (GPIO0) requires a 10 kΩ pull-up resistor to ensure proper boot.  
    Avoid pressing the D3-connected button during boot, as it may trigger flash mode.  
    - Pin D8 (GPIO15) may require a 10 kΩ pull-down resistor to prevent boot failure.  
    Ensure the pin is LOW during startup if used.
	
	**Note on A0 (Analog Input):  
	- Pin A0 is input only!
    This board includes a built-in voltage divider on A0, allowing direct measurement of 0–3.3 V signals.
    Confirmed linear readings with potentiometer suggest onboard divider is present on this board revision.	
    No external divider is needed unless measuring voltages above 3.3V. Check if your board needs external divider for 1V input!

	***Pin Mapping Note:  
    All pin labels (D0–D8, A0, TX, RX) are mapped to their corresponding GPIO numbers for direct use in code.  
    Use `GPIOx` in config files for clarity and compatibility across platforms.

Diagram and documentation © Pete100x, shared under MIT License.  
Source: https://github.com/Pete100x/Pete100xPublic/tree/main/AllLayouts

#

####	Original ASCII art below: D1 Mini
	
                     _______________________________ 
                    /            | ESP |            \
                    |            |  8  |            |
             RST    | [ ]RST     |  2  |TX/GPIO1[ ] |    GPIO1
              A0    | [ ]A0      |  6  |RX/GPIO3[ ] |    GPIO3
       GPIO16/D0    | [ ]D0/WAKE |  6  |  SCL/D1[ ]~|    D1/GPIO5
       GPIO14/D5    |~[ ]D5/SCLK |_____|  SDA/D2[ ]~|    D2/GPIO4
       GPIO12/D6    |~[ ]D6/MISO        FLASH/D3[ ]~|    D3/GPIO0
       GPIO13/D7    |~[ ]D7/MOSI          LED/D4[ ]~|    D4/GPIO2
       GPIO15/D8    |~[ ]D8/CS               GND[ ] |    GND
            3.3V    | [ ]3.3V                 5V[ ] |    5V
                     \                              |
                      O (RST BTN)+-----+  D1 MINI   |
                       \---------|USB-C|------------+
                                 +-----+

####    


# Teensy 3.2 Pinout and Pad Reference

## Top Side Layout


                                    ┌─────┐                             
                        ┌───────────┤USB-μ├────────────┐                
        GND           ← │ □ GND     └─────┘      Vin □ │ → Vin          
        D0/RX1        ← │ □ D0           VUSB □ AGND □ │ → AGND         
        D1/TX1        ← │ □ D1                  3.3V □ │ → 3.3V         
        D2/           ← │ □ D2        #!4 A11 ◊  D23 □ │ → A9/D23       
        D3/CANBTX     ← │~□ D3 #!5    #!4 A10 ◊  D22 □ │ → A8/D22       
        D4/CANBRX     ← │~□ D4 #!5       AREF □  D21 □ │ → A7/D21/(SS)/(RX1) 
        D5/(TX1)      ← │~□ D5                   D20 □ │ → A6/D20/(SS)    
        D6            ← │~□ D6    ┌────────┐     D19 □ │ → A5/D19/SCL   
        D7/(MOSI)/RX3 ← │ □ D7    │ TEENSY │     D18 □ │ → A4/D18/SDA   
        D8/(MISO)/RX3 ← │ □ D8    │  v3.2  │     D17 □ │ → A3/D17/(SDA)   
        D9/(SS)/RX2   ← │~□ D9    │        │     D16 □ │ → A2/D16/(SCL)   
        D10/SS/TX2    ← │~□ D10   │        │     D15 □ │ → A1/D15/(SS)    
        D11/MOSI      ← │ □ D11   └────────┘     D14 □ │ → A0/D14/(SCK)   
        D12/MISO      ← │ □ D12        ●     LED/D13 □ │ → D13/SCK      
                        │          (RST BTN)           │                
                        │ VBat  3.3V  GND  Prog A14/DAC│                
                        │ ← □  ← □  ←  □  ←  □  ← □≈   │                
                        └──────────────────────────────┘                
                                                   	                    
                                                                         
				     
## Bottom Side Layout
		    
                                                                         
                                                                          
                                  BOTTOM SIDE                            
                                ┏╍╍╍╍╍╍╍╍╍╍╍╍╍┓                          
                                ╎ ◊ ◊   ◊   ◊ ╎   #!1 Cut between pads if using external power for USB Device mode
                                ╎ ○-○   ○   ○ ╎   #!2 Add 150μF Capacitor between pads for USB host mode          
                                ╎ VUSB  150μF ╎   #!3 USB Data- and Data+
                                ╎  #!1   #!2  ╎   #!4 Only 3.3V on Pins A10-A13(Pins A10-A11 and A12-A13 feature differential amplifiers)
                                ╎   ◊     ◊   ╎   #!5 CAN Bus Transmit and Recieve                        
                                ╎ D-○ #!3 ○D+ ╎                          
                                ╎ #!4     #!4 ╎                          
                         A13 ←↧ ╎◊○A13   A12○◊╎ ↧→ A12                   
                        3.3V ←↧ ╎ ○3.3V  GND○ ╎ ↧→ GND                   
                         D33 ←↧ ╎ ○D33   D24○ ╎ ↧→ D24                   
                         D32 ←↧ ╎~○D32   D25○~╎ ↧→ D25                   
               D31/A20/(TX2) ←↧ ╎ ○D31   D26○ ╎ ↧→ D26/A15/(RX2)         
                D30/A19/SDA1 ←↧ ╎ ○D30   D27○ ╎ ↧→ D26/A15               
                D29/A18/SCL1 ←↧ ╎ ○D29   D28○ ╎ ↧→ D26/A15               
                                ┗╍╍╍╍╍╍╍╍╍╍╍╍╍┛                          
                                                                          

## Symbol Legend

| Symbol | Meaning |
|--------|---------|
| `□`    | Free pin (default)  
| `■`    | Used pin  
| `▲`    | Special pin (SPI, I2C, INT, UART, Pull-up, Pull-down)  
| `◊`    | Caution needed pin (sensor, expansion, special requirements)  
| `X`    | Do not use (reserved, LED or unsafe)  
| `~`    | PWM capable  
| `≈`    | DAC capable (analog output)  
| `↧`    | Underside pin (not on header)  
| `○`    | Pad (solder point or contact area, not a standard pin)  
| `•`    | Pad in use (solder point or contact area, not a standard pin)  
| `→`    | Pin used in code or config (logical direction only)  
| `μ`    | USB Micro-B connector  
| `●`    | Onboard reset button  

## Notes and Warnings

- `#!1` Cut between pads if using external power for USB Device mode  
- `#!2` Add 150μF capacitor between pads for USB host mode  
- `#!3` USB Data- and Data+  
- `#!4` Only 3.3V on Pins A10–A13 (Pins A10–A11 and A12–A13 feature differential amplifiers)  
- `#!5` CAN Bus Transmit and Recieve
- `#!6` All digital pins are Interrupt capable and have INPUT_PULLUP and INPUT_PULLDOWN built_in

## Board Metadata

- MCU: NXP MK20DX256VLH7  
- Voltage: 3.3V logic, 5V tolerant (except A10–A13)  
- USB: Micro-B connector  
- DAC: 12-bit analog output on A14  
- Pads: Underside pads for VUSB, Program, DAC, and extra GPIOs

## License and Attribution

This layout is designed by Pete100x.  
Symbols and annotation logic are standardized for reproducibility and international accessibility.  
Licensed under [MIT] or [CC BY-SA] — choose your preferred license.




                    □ = Free pin (default)  
                    ■ = Used pin  
                    ▲ = Special pin (SPI, I2C, INT, UART, Pull-up, Pull-down)  
                    ◊ = Caution needed pin (sensor, expansion, special requirements, See #!notation)  
                    X = Do not use (reserved, LED or unsafe)    
                    ~ = PWM capable (append to pin label)  
                    ≋ = DAC capable  
                    ↧ = Underside pin (not on header)  
                    → = Pin used in code or config (logical direction only; all arrows point outward for consistency)  
                    μ = USB Micro-B connector  
                    ● = Onboard reset button
                    ◊ = Analog input A10–A13 max 3.3V  
                    ○ = Pad (solder point or contact area, not a standard pin)  
                    • = Pad in use (solder point or contact area, not a standard pin)

#    