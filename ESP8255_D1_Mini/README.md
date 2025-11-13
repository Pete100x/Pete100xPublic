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
	
	*Note on A0 (Analog Input):  
	- Pin A0 is input only!
    This board includes a built-in voltage divider on A0, allowing direct measurement of 0–3.3 V signals.
    Confirmed linear readings with potentiometer suggest onboard divider is present on this board revision.	
    No external divider is needed unless measuring voltages above 3.3V. Check if your board needs external divider for 1V input!

	*Note TX and RX:
	- GPIO1 and GPIO3 doesn't have any other function than UART serial send and receive data.
	
	*Pin Mapping Note:  
    All pin labels (D0–D8, A0, TX, RX) are mapped to their corresponding GPIO numbers for direct use in code.  
    Use `GPIOx` in config files for clarity and compatibility across platforms.

Diagram and documentation © Pete100x, shared under MIT License.  
Source: https://github.com/Pete100x/Pete100xPublic/tree/main/AllLayouts

#