# IoT Air & Noise Pollution Monitoring System  
## Code_Logic (MicroPython)

This document briefly explains how the program works.  
It summarizes the sensor logic, display logic, alert logic, and IoT upload steps.

---

## 1. WiFi & ThingSpeak Setup
- Pico 2W connects to WiFi using SSID + Password.
- Every 15 seconds, data is uploaded to ThingSpeak through a simple HTTP GET request.
- Uploaded fields:
  - **field1:** Temperature  
  - **field2:** Humidity  
  - **field3:** Sound (dB)  
  - **field4:** Gas reading  

---

## 2. Sensor Initialization
- **DHT22** on GP4 → temperature & humidity  
- **MQ135** on GP27 (ADC1) → air quality  
- **MAX4466** on GP26 (ADC0) → sound amplitude  
- **SSD1306 OLED** via SPI (GP10, 11, 12, 13, 14)  
- **Passive buzzer** on GP16 via PWM  

All sensors are configured once at startup.

---

## 3. Temperature & Humidity Logic (DHT22)
- The sensor gives raw temperature (°C) and humidity (%).
- Values are classified:
  - Temperature → *Cold / Normal / Warm / Hot*
  - Humidity → *Dry / Normal / Humid*
- Classification helps show meaningful status on the OLED.

---

## 4. Air Quality Logic (MQ135)
The MQ135 provides an analog reading (0–65535).  
It is classified as:

| Value | Status |
|-------|--------|
| < 30000 | Good |
| < 40000 | Normal |
| < 50000 | Poor |
| < 60000 | Bad |
| ≥ 60000 | Hazard |

Used for both display and alerts.

---

## 5. Sound Measurement Logic (MAX4466)
- 200–250 samples are captured from the microphone.
- AC RMS is computed by subtracting DC mean.
- RMS is converted to approximate **dB** using a reference value.
- Output is categorized as:
  - Quiet  
  - Normal  
  - Loud  

This gives a meaningful noise level.

---

## 6. Buzzer Alert Logic
The buzzer produces different tones:

- **1200 Hz** → High temperature alert  
- **2000 Hz** → Bad or Hazard air quality  

The buzzer is driven using PWM on GP16 with a short-duration beep.

---

## 7. OLED Display Logic
The OLED shows five lines:

1. Temperature + status  
2. Humidity + status  
3. Gas reading + status  
4. Sound in dB  
5. WiFi status  

The display updates every 0.5 seconds for a live dashboard.

---

## 8. Main Loop Logic
Inside the continuous loop:

1. Read all sensors  
2. Process and classify values  
3. Activate buzzer if needed  
4. Update OLED  
5. Upload data to ThingSpeak every 15 seconds  
6. Small delay to stabilize readings  

This keeps the system running smoothly in real-time.

---

## Summary
The program integrates sensing, processing, display, alerts, and IoT uploading into one efficient MicroPython loop on the **Raspberry Pi Pico 2W**, enabling real-time air and noise monitoring.

