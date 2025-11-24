import time
import math
import network
import urequests
from machine import Pin, ADC, SPI, PWM
import ssd1306
import dht


# ------------------------------------------------------------
# WiFi + ThingSpeak DETAILS INITIALIZATION
# ------------------------------------------------------------
WIFI_SSID = "ssid"
WIFI_PASS = "password"

THINGSPEAK_API_KEY = "apikey"
THINGSPEAK_URL = "https://api.thingspeak.com/update"

# ------------------------------------------------------------
# Initialization of I/O devices
# ------------------------------------------------------------

dht_sensor = dht.DHT22(Pin(4))
mq135 = ADC(27)
sound = ADC(26)

buzzer = PWM(Pin(16))
buzzer.duty_u16(0)

# OLED SPI initialization
spi = SPI(1, baudrate=8000000, polarity=0, phase=0,
          sck=Pin(10), mosi=Pin(11))
dc = Pin(13)
res = Pin(12)
cs = Pin(14)
oled = ssd1306.SSD1306_SPI(128, 64, spi, dc, res, cs)

# ------------------------------------------------------------
# Calibration for sound sensor
# ------------------------------------------------------------
CAL_REF_VRMS = 0.005
MIN_DB = 30
MAX_DB = 120

# ------------------------------------------------------------
# FUNCTIONS
# ------------------------------------------------------------

def read_sound_db(adc, samples=200, delay_us=0):
    vals = []
    for _ in range(samples):
        vals.append(adc.read_u16())

    volts = [v * (3.3 / 65535) for v in vals]
    mean_v = sum(volts)/len(volts)
    ac = [v - mean_v for v in volts]

    sq = 0.0
    for a in ac:
        sq += a*a
    rms = (sq/len(ac))**0.5

    if rms < 1e-6:
        rms = 0.0

    if rms > 0:
        db = 20.0 * math.log10(rms / CAL_REF_VRMS) + 40.0
    else:
        db = MIN_DB

    db = max(MIN_DB, min(MAX_DB, db))
    return int(db)

def classify_gas(v):
    if v < 30000: return "Good"
    if v < 40000: return "Normal"
    if v < 50000: return "Poor"
    if v < 60000: return "Bad"
    return "Hazard"

def classify_temp(t):
    if t < 15: return "Cold"
    if t < 30: return "Normal"
    if t < 40: return "Warm"
    return "Hot"

def classify_humidity(h):
    if h < 30: return "Dry"
    if h < 60: return "Normal"
    return "Humid"

def classify_sound(db):
    if db < 50: return "Quiet"
    if db < 80: return "Normal"
    return "Loud"

# Tone control of Passive buzzer 
def beep(freq, duration=0.15):
    buzzer.freq(freq)
    buzzer.duty_u16(30000)
    time.sleep(duration)
    buzzer.duty_u16(0)

# ------------------------------------------------------------
# WiFi connect
# ------------------------------------------------------------
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    print("Connecting to WiFi...")
    wlan.connect(WIFI_SSID, WIFI_PASS)

    while not wlan.isconnected():
        print("Connecting...")
        time.sleep(1)

    print("WiFi Connected:", wlan.ifconfig())
    return wlan


wlan = connect_wifi()

# ------------------------------------------------------------
# MAIN LOOP
# ------------------------------------------------------------
last_upload = time.ticks_ms()

while True:

    # ---- DHT22 ----
    try:
        dht_sensor.measure()
        temp = dht_sensor.temperature()
        hum = dht_sensor.humidity()
    except:
        temp = -1
        hum = -1

    # ---- MQ135 ----
    gas_raw = mq135.read_u16()
    gas_status = classify_gas(gas_raw)

    # ---- SOUND ----
    snd_db = read_sound_db(sound, samples=250)
    sound_status = classify_sound(snd_db)

    # ---- BUZZER ALERT ----
    if temp > 30:
        beep(1200)

    if gas_status in ["Bad", "Hazard"]:
        beep(2000)

    # ---- SERIAL LOG ----
    print("T:", temp, "| H:", hum, "| Gas:", gas_raw, gas_status,
          "| Sound:", snd_db, "dB", sound_status)

    # ---- OLED ----
    oled.fill(0)
    oled.text("T:{:.2f}C {}".format(temp, classify_temp(temp)), 0, 0)
    oled.text("H:{:.2f}% {}".format(hum, classify_humidity(hum)), 0, 12)
    oled.text("Gas:{} {}".format(gas_raw, gas_status), 0, 24)
    oled.text("Sound:{}dB {}".format(snd_db, sound_status), 0, 36)

    if wlan.isconnected():
        oled.text("WiFi connected", 0, 52)
    else:
        oled.text("WiFi disconnected", 0, 52)

    oled.show()

    # ---- THINGSPEAK EVERY 15 SEC ----
    if time.ticks_diff(time.ticks_ms(), last_upload) > 15000:
        try:
            url = (
                THINGSPEAK_URL +
                "?api_key=" + THINGSPEAK_API_KEY +
                "&field1=" + str(temp) +
                "&field2=" + str(hum) +
                "&field3=" + str(snd_db) +
                "&field4=" + str(gas_raw) 
            )
            response = urequests.get(url)
            print("ThingSpeak Response:", response.text)
            response.close()
        except Exception as e:
            print("ThingSpeak Upload Error:", e)

        last_upload = time.ticks_ms()

    time.sleep(0.5)

