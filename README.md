# IoT Air & Noise Pollution Monitoring using Raspberry Pi Pico W

A complete IoT-based environmental monitoring system that measures **Temperature**, **Humidity**, **Air Quality**, and **Noise Levels**, displays them on an **SSD1306 OLED**, and uploads live readings to **ThingSpeak** using the **Raspberry Pi Pico 2W**.

---

## Project Overview

This project monitors:

-  Temperature & Humidity using DHT22
-  Air Quality using MQ135
-  Noise Level using MAX4466
-  Local Display using SSD1306 OLED-SPI
-  IoT Logging using ThingSpeak
-  Alerts using Passive Buzzer

The system provides real-time environmental monitoring, both locally and remotely.

---

## Features

- Real-time monitoring of temperature, humidity, noise, and gas concentration  
- Clear live display on 128x64 SSD1306 OLED  
- WiFi-enabled data upload to ThingSpeak (cloud dashboard)  
- Passive buzzer alerts for dangerous levels  
- Compact, fast, and low-power  
- Easy to expand or modify  

---

## Hardware Components

| Component | Description |
|----------|-------------|
| Raspberry Pi Pico 2W | WiFi-enabled microcontroller |
| DHT22 Sensor | Temperature & humidity sensor |
| MQ135 | Air quality sensor |
| MAX4466 | Sound sensor with adjustable gain |
| SSD1306 OLED (SPI) | 128×64 display |
| Passive Buzzer | Audio alerts |
| Jumper Wires | Connections |
| Breadboard | Prototyping |

---

## Software Requirements

- MicroPython
- Thonny IDE (recommended)  
- ThingSpeak IoT account

---

## How It Works

1. Sensors continuously collect environmental data  
2. Pico W processes values & displays them on OLED  
3. Data is uploaded to ThingSpeak via WiFi  
4. ThingSpeak graphs allow remote monitoring  
5. Buzzer alerts activate when values exceed thresholds  

---

## Example Applications

- Indoor air-quality monitoring  
- Classroom/laboratory safety  
- Noise pollution tracking  
- Smart-home environmental analysis  
- IoT learning projects  

---

## Conclusion

This project demonstrates a fully functional **IoT environmental monitoring system** using Raspberry Pi Pico 2W.  
It effectively combines **sensing**, **local display**, **wireless connectivity**, and **cloud analytics**, making it ideal for academic submissions and practical deployments.

---

## Author / Developer

 **Abhirama** 
 
 **Akshay Ballal**
 
 **Adarsha G Acharya**
 
Electronics and Communication Engineering Students at NMAMIT, Nitte  


