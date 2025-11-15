# Teensy 3.2 Pinout and Pad Reference

## Top Side Layout


                                    ┌─────┐                             
                        ┌───────────┤USB-μ├────────────┐                
        GND           ← │ □ GND     └─────┘      Vin □ │ → Vin          
        D0/RX1        ← │ □ D0         VUSB □ → AGND □ │ → AGND         
        D1/TX1        ← │ □ D1                  3.3V □ │ → 3.3V         
        D2            ← │ □ D2     #!4 A11 ◊□ →  D23 □~│ → A9/D23       
        D3/CANBTX     ← │~□ D3 #!5 #!4 A10 ◊□ →  D22 □~│ → A8/D22       
        D4/CANBRX     ← │~□ D4 #!5     AREF □ →  D21 □~│ → A7/D21/(SS)/(RX1) 
        D5/(TX1)      ← │~□ D5                   D20 □~│ → A6/D20/(SS)    
        D6            ← │~□ D6    ┌────────┐     D19 □ │ → A5/D19/SCL   
        D7/(MOSI)/RX3 ← │ □ D7    │ TEENSY │     D18 □ │ → A4/D18/SDA   
        D8/(MISO)/RX3 ← │ □ D8    │  v3.2  │     D17 □ │ → A3/D17/(SDA)   
        D9/(SS)/RX2   ← │~□ D9    │        │     D16 □ │ → A2/D16/(SCL)   
        D10/SS/TX2    ← │~□ D10   │        │     D15 □ │ → A1/D15/(SS)    
        D11/MOSI      ← │ □ D11   └────────┘     D14 □ │ → A0/D14/(SCK)   
        D12/MISO      ← │ □ D12        ● #!6 LED/D13◊□ │ → D13/SCK      
                        │          (RST BTN)           │                
                        │ VBat  3.3V  GND  Prog A14/DAC│                
                        │ ← □  ← □  ←  □  ←  □  ← □≈   │                
                        └──────────────────────────────┘                
                                                   	                    
                                                                         
				     
## Bottom Side Layout
		    
                                                                         
                                                                          
                                  BOTTOM SIDE                            
                                ┏╍╍╍╍╍╍╍╍╍╍╍╍╍┓                          
                                ╎ ◊ ◊   ◊   ◊ ╎   
                                ╎ ○-○   ○   ○ ╎   
                                ╎ VUSB  150μF ╎   
                                ╎  #!1   #!2  ╎   
                                ╎   ◊     ◊   ╎   
                                ╎ D-○ #!3 ○D+ ╎    
                                ╎  #!4   #!4  ╎                          
                         A13 ←↧ ╎◊○ A13 A12 ○◊╎ ↧→ A12                   
                        3.3V ←↧ ╎ ○ 3V3 GND ○ ╎ ↧→ GND                   
                         D33 ←↧ ╎ ○ D33 D24 ○ ╎ ↧→ D24                   
                         D32 ←↧ ╎~○ D32 D25 ○~╎ ↧→ D25                   
               D31/A20/(TX2) ←↧ ╎ ○ D31 D26 ○ ╎ ↧→ D26/A15/(RX2)         
                D30/A19/SDA1 ←↧ ╎ ○ D30 D27 ○ ╎ ↧→ D26/A15               
                D29/A18/SCL1 ←↧ ╎ ○ D29 D28 ○ ╎ ↧→ D26/A15               
                                ┗╍╍╍╍╍╍╍╍╍╍╍╍╍┛                          


                                #!1 Cut between pads if using external power for USB Device mode
                                #!2 Add 150μF Capacitor between pads for USB host mode          
                                #!3 USB Data- and Data+
                                #!4 Only 3.3V on Pins A10-A13(Pins A10-A11 and A12-A13 feature differential amplifiers)
                                #!5 CAN Bus Transmit and Recieve                        
                                #!6 When using pin D13 as an input, ensure that the external signal can drive the LED when it is logic HIGH. Do not use pinMode INPUT_PULLUP with pin D13.


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
- `#!6` When using pin D13 as an input, ensure that the external signal can drive the LED when it is logic HIGH. Do not use pinMode INPUT_PULLUP with pin D13.
- *Note: All digital pins are Interrupt capable and have INPUT_PULLUP and INPUT_PULLDOWN built_in

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

#    