# IoT Dashboard Analytics
## ThingSpeak Dashboard for Air & Noise Monitoring System  

The project uses **ThingSpeak** as the IoT platform to visualize real-time temperature, humidity, air quality, and noise levels remotely.

This document explains the dashboard layout, fields used, and how the data appears.

---

## 1. ThingSpeak Channel Structure

ThingSpeak channel contains the following fields:

| Field No. | Parameter        | Source Sensor |
|-----------|------------------|---------------|
| Field 1   | Temperature (°C) | DHT22         |
| Field 2   | Humidity (%)     | DHT22         |
| Field 3   | Sound (dB)       | MAX4466       |
| Field 4   | Air Quality (Raw)| MQ135         |

These values are updated every **15 seconds** from the Pico 2W.

---

## 2. Dashboard Visualization

You should configure the following widgets inside your ThingSpeak channel:

### 2.1 Line Graphs  
Use line charts for:

- **Temperature vs Time**  
- **Humidity vs Time**  
- **Sound Level (dB) vs Time**  
- **Air Quality Raw Value vs Time**

These help observe environmental variations throughout the day.

### 2.2 Status Box Widgets  
Add status displays showing the latest reading:

- Latest temperature  
- Latest humidity  
- Latest noise level  
- Current gas sensor status (*Good / Normal / Poor / Bad / Hazard*)

### 2.3 Alert Visualization (Optional)
You can add:

- Custom text widget titled **“Alerts”**
- It displays messages like:
  - “High Temperature”
  - “Poor Air Quality”
  - “Noise Level Loud”

These messages come from your own interpretation of the readings.

---

## 3. Data Upload Logic (From Code)

Data is sent using:

https://api.thingspeak.com/update?api_key=YOUR_KEY&field1=temp&field2=hum&field3=sound&field4=gas

Uploads happen every **15 seconds**, providing a near-real-time dashboard.

---

## 4. Example Dashboard Layout

Your channel should look like:

- **Graph 1:** Temperature (°C)  
- **Graph 2:** Humidity (%)  
- **Graph 3:** Noise Level (dB)  
- **Graph 4:** MQ135 Raw Value  
- **Value Widgets:** Latest values for quick view   

This creates a full IoT monitoring page accessible from mobile or PC.

---

## 5. Future Expansion (Optional)

You may extend the dashboard by adding:

- Gauge meters for real-time indicators  
- Email/SMS alert triggers using ThingSpeak “React”  
- Comparison of historical datasets  
- Exporting CSV logs for analysis  

---

## Summary

The ThingSpeak dashboard provides:

- Real-time environmental monitoring  
- Remote access from anywhere  
- Automatic graphing and data storage  
- A clean, organized view of sensor behavior  

This turns the Pico 2W system into a complete IoT monitoring solution.



Data is sent using:

