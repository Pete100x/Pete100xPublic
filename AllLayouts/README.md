## Sources

Some of the ASCII pinout diagrams in this repository are based on or adapted from publicly available resources:

- [Busy Ducks – ASCII Art Arduino Pinouts](https://busyducks.com/ascii-art-arduino-pinouts/index.html)
- [Arduino Nano by /u/plasticluthier](https://www.reddit.com/r/arduino/comments/3tb0d2/i_made_some_asciiart_arduinos_to_paste_in/cx5oyjp)
- [SP-8266 D1-Mini by pete100x] 

The diagrams have been visually and technically modified to match the documentation style and layout used in this project. Original versions are available at the link above.

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
          5V   ←   │ □ 5V       (RST BTN)    GND □ │   → GND
          RST  ←   │ □ RST                   RST □ │   → RST
          GND  ←   │ □ GND    5V MOSI GND TX1/D0 □ │   → D0
          Vin  ←   │ □ Vin      □  □  □   RX1/D1 □ │   → D1
                   │            □  □  □            │  
                   │         MISO SCK RST          │  
                   │                               │ 
                   │ ATmega328P NANO-V3            │  
                   └───────────────────────────────┘  

                    □ = Free pin (default)  
                    ■ = Used pin  
                    ▲ = Protocol pin (SPI, I2C, INT, UART)  
                    ◊ = Reserved pin (sensor or expansion)  
                    X = Do not use (reserved, LED or unsafe)    
                    ~ = PWM capable (append to pin label)
                    ● = Onboard reset button					

    These symbols are used consistently across all board diagrams to clarify pin availability and function.  
    Protocol pins (▲) may overlap with digital or analog pins depending on context (e.g. SDA = A4 = D18).

#

###

         ````First Conversion to UniCode
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
		 ````
###
 
###	Original ASCII art below: Nano-v3

		  	 
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
###		 

# Arduino Uno R3 ATmega328P
												  
                        ┌─────┐                  ┌─────┐
                   ┌────┤ PWR ├──────────────────┤ USB ├──┐
                   │    │6–20V│                  │  B  │ ●│(RST BTN)
                   │    └─────┘ GND/RST2 □  □    └─────┘  │       
                   │          MOSI2/SCK2 □  □ SCL/A5/D19□ │   → A5/D19
                   │            5V/MISO2 □  □ SDA/A4/D18□ │   → A4/D18
                   │                                AREF□ │   → AREF
                   │                                 GND□ │   → GND
       N/C     ←   │ □N/C                    LED/SCK/D13□ │   → D13
       IOREF   ←   │ □IOREF                     MISO/D12□ │   → D12
       RST     ←   │ □RST                       MOSI/D11□~│   → D11
       3V3     ←   │ □3V3     ┌───┐                  D10□~│   → D10
       5V      ←   │ □5V      │ A │                   D9□~│   → D9
       GND     ←   │ □GND     │ R │                   D8□ │   → D8
       GND     ←   │ □GND     │ D │                       │       
       Vin     ←   │ □Vin     │ U │                   D7□ │   → D7
                   │          │ I │                   D6□~│   → D6
       A0/D14  ←   │ □A0/D14  │ N │                   D5□~│   → D5
       A1/D15  ←   │ □A1/D15  │ O │                   D4□ │   → D4
       A2/D16  ←   │ □A2/D16  └───┘              INT1/D3□~│   → D3
       A3/D17  ←   │ □A3/D17                     INT0/D2□ │   → D2
       A4/D18  ←   │ □A4/D18    RST SCK MISO       TX>D1□ │   → D1
       A5/D19  ←   │ □A5/D19     □   □   □         RX<D0□ │   → D0
                   │             □   □   □                │     
                   │  UNO_R3    GND MOSI 5V ╭─────────────╯   
                    ╲──────────────────────╱  

                    □ = Free pin (default)  
                    ■ = Used pin  
                    ▲ = Protocol pin (SPI, I2C, INT, UART)  
                    ◊ = Reserved pin (sensor or expansion)  
                    X = Do not use (reserved, LED or unsafe)    
                    ~ = PWM capable (append to pin label)
                    ● = Onboard reset button					

    These symbols are used consistently across all board diagrams to clarify pin availability and function.  
    Protocol pins (▲) may overlap with digital or analog pins depending on context (e.g. SDA = A4 = D18).

#

###	Original ASCII art below: Uno R3

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
###		                

# Arduino Mega ATmega2560

       
                         ┌─────┐                 ┌─────┐
                    ┌────┤ PWR ├─────────────────┤ USB ├──┐
                    │    │6–20V│                 │  B  │  │
                    │    └─────┘  GND/RST2  □ □  └─────┘  │
                    │           MOSI2/SCK2  □ □  SCL/D0 □ │   →   D0
                    │             5V/MISO2  □ □  SDA/D1 □ │   →   D1
                    │                              AREF □ │   →   AREF
                ←   │                               GND □ │   →   GND 
       N/C      ←   │ □ N/C                     LED/D13 □~│   →   D13
       IOREF    ←   │ □ IOREF                       D12 □~│   →   D12
       RST      ←   │ □ RST                         D11 □~│   →   D11
       3.3V     ←   │ □ 3.3V      ┌──────────┐      D10 □~│   →   D10
       5V       ←   │ □ 5V        │ ARDUINO  │       D9 □~│   →   D9
       GND      ←   │ □ GND       │ ATMEGA   │       D8 □~│   →   D8
       GND      ←   │ □ GND       │ 2560     │            │
       Vin      ←   │ □ Vin       └──────────┘       D7 □~│   →   D7
                    │                                D6 □~│   →   D6
       A0/D54   ←   │ □ A0/D54                  INT5/D5 □~│   →   D5
       A1/D55   ←   │ □ A1/D55                  INT4/D4 □~│   →   D4
       A2/D56   ←   │ □ A2/D56                  INT3/D3 □~│   →   D3
       A3/D57   ←   │ □ A3/D57                  INT2/D2 □~│   →   D2
       A4/D58   ←   │ □ A4/D58                   TX1/D1 □~│   →   D1
       A5/D59   ←   │ □ A5/D59                   RX0/D0 □~│   →   D0
       A6/D60   ←   │ □ A6/D60                            │
       A7/D61   ←   │ □ A7/D61                  TX3/D14 □ │   →   D14
                    │                           RX3/D15 □ │   →   D15
       A8/D62   ←   │ □ A8/D62                  TX2/D16 □ │   →   D16
       A9/D63   ←   │ □ A9/D63                  RX2/D17 □ │   →   D17
       A10/D64  ←   │ □ A10/D64            TX1/INT1/D18 □ │   →   D18
       A11/D65  ←   │ □ A11/D65            RX1/INT0/D19 □ │   →   D19
       A12/D66  ←   │ □ A12/D66        I2C-SDA/INT3/D20 □ │   →   D20
       A13/D67  ←   │ □ A13/D67        I2C-SCL/INT2/D21 □ │   →   D21
       A14/D68  ←   │ □ A14/D68                           │
       A15/D69  ←   │ □ A15/D69     RST SCK MISO          │  □ 22 = D22/A0    □ 23 = D23/A1         
                    │           ICSP □   □   □            │  □ 24 = D24/A2    □ 25 = D25/A3         
                    │                □   □   □            │  □ 26 = D26/A4    □ 27 = D27/A5         
                    │               GND MOSI 5V           │  □ 28 = D28/A6    □ 29 = D29/A7         
                    │                  ● (RST BTN)        │  □ 30 = D30       □ 31 = D31         
                    │ G                                   │  □ 32 = D32       □ 33 = D33         
                    │ N 5 5 4 4 4 4 4 3 3 3 3 3 2 2 2 2 5 │  □ 34 = D34       □ 35 = D35         
                    │ D 2 0 8 6 4 2 0 8 6 4 2 0 8 6 4 2 V │  □ 36 = D36       □ 37 = D37         
                    │         ~ ~                         │  □ 38 = D38       □ 39 = D39         
                    │ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ │  □ 40 = D40       □ 41 = D41         
                    │ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ │  □ 42 = D42       □ 43 = D43         
                    │ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ □ │  □~44 = D44       □~45 = D45         
                    │ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ │  □~46 = D46       □ 47 = D47         
                    │           ~                         │  □ 48 = D48       □ 49 = D49         
                    │ G 5 5 4 4 4 4 4 3 3 3 3 3 2 2 2 2 5 │  □ 50 = D50/MISO  □ 51 = D51/MOSI         
                    │ N 3 1 9 7 5 3 1 9 7 5 3 1 9 7 5 3 V │  □ 52 = D52/SCK   □ 53 = D53/SS         
                    │ D                                   │                                           
                    │                                     │                                           
                    │ ATMEGA2560              ╭───────────╯ 
                    ╰─────────────────────────╯
	               
                    □ = Free pin (default)  
                    ■ = Used pin  
                    ▲ = Protocol pin (SPI, I2C, INT, UART)  
                    ◊ = Reserved pin (sensor or expansion)  
                    X = Do not use (reserved, LED or unsafe)    
                    ~ = PWM capable (append to pin label)
                    ● = Onboard reset button					

    These symbols are used consistently across all board diagrams to clarify pin availability and function.  
    Protocol pins (▲) may overlap with digital or analog pins depending on context (e.g. SDA = A4 = D18).
#


###	Original ASCII art below; Arduino Mega


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
	               

#  D1 Mini ESP8266
      

                    ╭────────────┬─────┬────────────╮ 
                    │            │ ESP │            │
                    │            │  8  │            │
          RST   ←   │ □ RST      │  2  │       TX □~│  →   GPIO01
          A0    ←   │ □ A0       │  6  │       RX □~│  →   GPIO03
          D0    ←   │~□ D0/WAKE  │  6  │   SCL/D1 □~│  →   D1
          D5    ←   │~□ D5/SCLK  └─────┘   SDA/D2 □~│  →   D2
          D6    ←   │~□ D6/MISO          FLASH/D3 □~│  →   D3
          D7    ←   │~□ D7/MOSI            LED/D4 X~│  →   D4
          D8    ←   │~□ D8/CS                 GND □ │  →   GND
          3.3V  ←   │ □ 3.3V                   5V □ │  →   5V
                    ╰─╮                             │
                     ●│(RST BTN) ┌─────┐  D1 MINI   │
                      └──────────┤USB-C├────────────┘
                                 └─────┘              
        
                    □ = Free pin (default)  
                    ■ = Used pin  
                    ▲ = Protocol pin (SPI, I2C, INT, UART)  
                    ◊ = Reserved pin (sensor or expansion)  
                    X = Do not use (reserved, LED or unsafe)    
                    ~ = PWM capable (append to pin label)
                    ● = Onboard reset button					

    These symbols are used consistently across all board diagrams to clarify pin availability and function.  
    Protocol pins (▲) may overlap with digital or analog pins depending on context (e.g. SDA = A4 = D18).
#

###	Original ASCII art below: D1 Mini
	
                     _______________________________ 
                    /            | ESP |            \
                    |            |  8  |            |
                    | [ ]RST     |  2  |      TX[ ]~|    GPIO01
            ADC0    | [ ]A0      |  6  |      RX[ ]~|    GPIO03
              D0    |~[ ]D0/WAKE |  6  |  SCL/D1[ ]~|    D1
              D5    |~[ ]D5/SCLK |_____|  SDA/D2[ ]~|    D2
              D6    |~[ ]D6/MISO        FLASH/D3[ ]~|    D3
              D7    |~[ ]D7/MOSI              D4[ ]~|    D4
              D8    |~[ ]D8/CS               GND[ ] |    GND
            3.3V    | [ ]3.3V                 5V[ ] |    5V
                     \                              |
                      O (RST BTN)+-----+  D1 MINI   |
                       \---------|USB-C|------------+
                                 +-----+

###        