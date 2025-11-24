# Project schematic 
## IoT Air & Noise Pollution Monitoring System

Below is the wiring diagram and connection table for the project.  

---

## Pin-to-Pin Connections 

**Microcontroller:** Raspberry Pi Pico 2W

### DHT22 (Temperature & Humidity)
- DHT22 VCC  → Pico 2W 3.3V
- DHT22 DATA → Pico GP4
- DHT22 GND  → Pico GND

### MQ135 (Gas / Air Quality) — analog module
- MQ135 VCC  → Pico 2W 3.3V   
- MQ135 AOUT → Pico GP27 (ADC1)
- MQ135 GND  → Pico GND

### MAX4466 (Sound)
- MAX4466 VCC → Pico 3.3V
- MAX4466 GND → Pico GND
- MAX4466 OUT → Pico GP26 (ADC0)

### SSD1306 OLED (7-pin SPI variant)
- OLED GND  → Pico GND
- OLED VCC  → Pico 3.3V
- OLED D0/SCK → Pico GP10
- OLED D1/MOSI→ Pico GP11
- OLED RES  → Pico GP12
- OLED DC   → Pico GP13
- OLED CS   → Pico GP14

### Passive Buzzer (3-pin module: +, -, S)
- Buzzer + → Pico 3.3V
- Buzzer - → Pico GND
- Buzzer S (signal / PWM) → Pico GP16


---

## Summary table 

| Component | Module pin | Pico 2W pin |
|----------:|:-----------|:------------|
| DHT22     | VCC        | 3.3V        |
|           | DATA       | GP4         |
|           | GND        | GND         |
|           |            |             |
| MQ135     | VCC        | 3.3V        |
|           | AOUT       | GP27 (ADC)  |
|           | GND        | GND         |
|           |            |             |
| MAX4466   | VCC        | 3.3V        |
|           | OUT        | GP26 (ADC)  |
|           | GND        | GND         |
|           |            |             |
| OLED (SSD1306 - SPI) | VCC | 3.3V |
|           | GND        | GND         |
|           | SCK (D0)   | GP10        |
|           | MOSI (D1)  | GP11        |
|           | RES        | GP12        |
|           | DC         | GP13        |
|           | CS         | GP14        |
|           |            |             |
| Buzzer    | +          | 3.3V        |
|           | -          | GND         |
|           | S (signal) | GP16 (PWM)  |



---

