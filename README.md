# Real-time air and noise pollution monitoring using Raspberry Pi Pico 2W and IoT

Environmental monitoring requires the simultaneous collection and network transmission of diverse data streams from heterogeneous sources (air quality, sound, temperature/humidity).

## The core technical challenges addressed by this project are:

- <a> Heterogeneous Data Integration: </a> Successfully interfacing the Raspberry Pi Pico W with Analog (MQ-135, MAX4466) and Digital (DHT22) sensors, and implementing the necessary MicroPython drivers and ADC sampling routines to efficiently acquire, normalize, and condition multiple, disparate data signals.

- <a> Real-Time Data Telemetry and Cloud Integration: </a> Establishing a stable Wi-Fi link and executing a periodic HTTP GET request (ThingSpeak API) to securely transmit time-series data, demonstrating a functional Machine-to-Cloud telemetry channel under resource constraints.

- <a> Local Edge Processing and HMI: </a> Implementing on-device signal processing (specifically RMS to dB conversion for noise) and integrating a Local HMI (OLED) to provide continuous, real-time data visualization and a PWM-driven alarm system for immediate actionable alerts.

## Goal:
To engineer a robust, self-contained, and network-enabled Data Acquisition System (DAS) that leverages the Pico W's capabilities for continuous environmental parameter measurement, signal processing, and integrated cloud telemetry, serving as a functional prototype for distributed sensor networks.
