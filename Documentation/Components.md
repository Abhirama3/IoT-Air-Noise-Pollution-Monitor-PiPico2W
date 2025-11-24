 # Components Used
 ## IoT Air & Noise Pollution Monitoring System  

This project uses low-cost sensors with the latest Raspberry Pi Pico 2W, which includes WiFi and a faster RP2350 chip.

---

## 1. Microcontroller  
### **Raspberry Pi Pico 2W**
- RP2350 dual-core processor  
- Built-in WiFi 2.4 GHz  
- Multiple high-resolution ADC channels  
- Very low power consumption  
**Role:** Reads sensors, processes data, shows output on OLED, and uploads to ThingSpeak.

---

## 2. Temperature & Humidity Sensor  
### **DHT22**
- Temp: –40°C to +80°C  
- Humidity: 0–100%  
- Higher accuracy than DHT11  
**Role:** Measures ambient temperature and humidity.

---

## 3. Air Quality Sensor  
### **MQ135**
- Detects harmful gases: CO₂, NH₃, benzene, alcohol, smoke  
- Analog output  
**Role:** Approximate air quality index (Good / Normal / Poor / Bad / Hazard).

---

## 4. Sound Sensor  
### **MAX4466 Electret Microphone with Adjustable Gain**
- Real analog microphone  
- Very low noise  
- Adjustable amplification  
**Role:** Detects ambient noise level and converts to approximate decibels (dB).

---

## 5. Display  
### **0.96" OLED Display (SSD1306 – 7-pin SPI version)**
- 128×64 resolution  
- SPI communication  
**Role:** Displays temperature, humidity, air quality, sound level, and WiFi status.

---

## 6. Buzzer  
### **Passive Buzzer (3-pin: +, –, S)**
- Controlled using PWM  
**Role:** Alerts user when temperature or air quality exceed safe limits.

---

## 7. Miscellaneous Components  
- Breadboard  
- Jumper wires 
- USB cable for Pico 2W  
- External 5V mobile charger / Battery (optional)  

---

## 8. Software Requirement  
- MicroPython firmware for **Pico 2W**  
- Thonny IDE or VS Code   
- ThingSpeak account  

---

## 9. IoT Cloud  
### **ThingSpeak**
Used for:
- Real-time sensor graphs  
- Storing data  
- Triggering alerts  
- Dashboard visualisation

---

## Summary  
With Pico 2W, DHT22, MQ135, MAX4466, OLED, and a buzzer, the system provides a simple but effective solution for monitoring **air quality**, **temperature**, **humidity**, and **noise pollution**, with both **local alerts** and **internet cloud logging**.

---
