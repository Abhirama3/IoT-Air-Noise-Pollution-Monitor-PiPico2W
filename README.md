# Real-time air and noise pollution monitoring using Raspberry Pi Pico 2W and IoT

Environmental monitoring requires the simultaneous collection and network transmission of diverse data streams from heterogeneous sources (air quality, sound, temperature/humidity).


## The core technical challenges addressed by this project are:

- <a> Heterogeneous Data Integration: </a> Successfully interfacing the Raspberry Pi Pico W with Analog (MQ-135, MAX4466) and Digital (DHT22) sensors, and implementing the necessary MicroPython drivers and ADC sampling routines to efficiently acquire, normalize, and condition multiple, disparate data signals.

- <a> Real-Time Data Telemetry and Cloud Integration: </a> Establishing a stable Wi-Fi link and executing a periodic HTTP GET request (ThingSpeak API) to securely transmit time-series data, demonstrating a functional Machine-to-Cloud telemetry channel under resource constraints.

- <a> Local Edge Processing and HMI: </a> Implementing on-device signal processing (specifically RMS to dB conversion for noise) and integrating a Local HMI (OLED) to provide continuous, real-time data visualization and a PWM-driven alarm system for immediate actionable alerts.


## Goal:
To engineer a robust, self-contained, and network-enabled Data Acquisition System (DAS) that leverages the Pico W's capabilities for continuous environmental parameter measurement, signal processing, and integrated cloud telemetry, serving as a functional prototype for distributed sensor networks.


## Scope of the solution

The scope of this solution defines the precise technical boundaries and verifiable deliverables of the system demonstrated by the provided code:

|Component|Technical Delivarable|Engineering focus|
|---------|---------------------|-----------------|
|Data Acquisition|Integration of DHT22 (Temperature/Humidity), MQ-135 (Gas), and MAX4466 (Sound) sensors via GPIO and ADC peripherals of the Raspberry Pi Pico|Multi-sensor hardware interfacing and data polling|
|Signal Processing|Implementation of RMS algorithm to convert raw sound ADC values into the dB scale, and application of boundary clipping (MIN_DB, MAX_DB) to ensure stable output|Real-time signal conditioning and environmental metrics calculation|
|Telemetry & Cloud|Successful Wi-Fi connection management and periodic (15-second interval) publishing of all four sensor readings (Temp, Hum, Sound dB, Gas Raw) to a ThingSpeak channel using formatted HTTP GET requests|Network protocol handling and I/O rate management|
|Local HMI & Alerting|Implementation of an SSD1306 OLED display driven by SPI to locally display all current readings and network status. A PWM-driven buzzer provides discrete audio alerts for critical thresholds|Edge device output, user interaction, and state signaling|
|Firmware|The entire system is implemented in MicroPython, demonstrating efficient memory management and synchronous loop execution to balance data acquisition, display update, and network transmission tasks|Embedded software development and resource optimization|
