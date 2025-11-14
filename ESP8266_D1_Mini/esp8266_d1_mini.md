# Pin and Direction Table: esp8266_d1_mini

| Line | Side | Function | Direction | State | PWM | Label |
|------|------|----------|-----------|-------|-----|--------|
| 6 | Left | RST | OUTPUT | Free pin |  | RST |
| 6 | Right | GPIO1 | OUTPUT | Do not use (reserved, LED, unsafe) |  | TX/GPIO1 |
| 7 | Left | ADC0 | INPUT | Caution needed (sensor, expansion, #!notation) |  | A0 |
| 7 | Right | GPIO3 | INPUT | Do not use (reserved, LED, unsafe) |  | RX/GPIO3 |
| 8 | Left | GPIO16/D0 | OUTPUT | Free pin |  | D0/WAKE |
| 8 | Right | D1/GPIO5 | OUTPUT | Free pin | ✓ | SCL/D1 |
| 9 | Left | GPIO14/D5 | OUTPUT | Free pin | ✓ | D5/SCLK |
| 9 | Right | D2/GPIO4 | OUTPUT | Free pin | ✓ | D5/SCLK |
| 10 | Left | GPIO12/D6 | OUTPUT | Free pin | ✓ | D6/MISO |
| 10 | Right | D3/GPIO0 | OUTPUT | Free pin | ✓ | D6/MISO |
| 11 | Left | GPIO13/D7 | OUTPUT | Free pin | ✓ | D7/MOSI |
| 11 | Right | D4/GPIO2 | OUTPUT | Free pin | ✓ | D7/MOSI |
| 12 | Left | GPIO15/D8 | OUTPUT | Special pin (SPI, I2C, INT, UART, Pull-up/down) | ✓ | D8/CS |
| 12 | Right | GND | OUTPUT | Special pin (SPI, I2C, INT, UART, Pull-up/down) | ✓ | GND |
| 13 | Left | 3.3V | OUTPUT | Free pin |  | 3.3V |
| 13 | Right | 5V | OUTPUT | Free pin |  | 5V |
