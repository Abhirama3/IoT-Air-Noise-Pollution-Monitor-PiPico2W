# dht.py - MicroPython DHT11/DHT22 driver
# Works on RP2040 (Raspberry Pi Pico / Pico W)

import time
from machine import Pin

class DHTBase:
    def __init__(self, pin):
        self.pin = Pin(pin, Pin.OPEN_DRAIN)
        self.pin.value(1)
        self.last_measure = time.ticks_ms()
        self.temperature = None
        self.humidity = None

    def measure(self):
        raise NotImplementedError

    def _send_and_receive(self):
        self.pin.init(Pin.OPEN_DRAIN)
        self.pin.value(0)
        time.sleep_ms(20)
        self.pin.value(1)
        time.sleep_us(40)

        self.pin.init(Pin.IN, Pin.PULL_UP)

        # Wait for sensor response
        for _ in range(100):
            if not self.pin.value():
                break
            time.sleep_us(1)

        # Sensor pulls low
        for _ in range(100):
            if self.pin.value():
                break
            time.sleep_us(1)

        # Sensor pulls high
        for _ in range(100):
            if not self.pin.value():
                break
            time.sleep_us(1)

        data = []
        for _ in range(40):
            # Start of bit
            while not self.pin.value():
                pass
            # Measure length of high signal
            t = 0
            while self.pin.value():
                t += 1
                time.sleep_us(1)
                if t > 100:
                    break
            data.append(1 if t > 30 else 0)

        return data

class DHT22(DHTBase):
    def measure(self):
        data = self._send_and_receive()

        # Parse 40 bits
        bits = data
        hum = 0
        temp = 0

        for i in range(16):
            hum = (hum << 1) | bits[i]
        for i in range(16, 32):
            temp = (temp << 1) | bits[i]

        # checksum
        chk = 0
        for i in range(32, 40):
            chk = (chk << 1) | bits[i]

        if (((hum >> 8) + (hum & 0xFF) + (temp >> 8) + (temp & 0xFF)) & 0xFF) != chk:
            raise Exception("Checksum error")

        self.humidity = hum / 10.0
        if temp & 0x8000:  # Negative temperature
            temp = temp & 0x7FFF
            self.temperature = -temp / 10.0
        else:
            self.temperature = temp / 10.0


class DHT11(DHTBase):
    def measure(self):
        data = self._send_and_receive()

        hum = 0
        temp = 0

        for i in range(8):
            hum = (hum << 1) | data[i]
        for i in range(16, 24):
            temp = temp << 1 | data[i]

        chk = 0
        for i in range(32, 40):
            chk = (chk << 1) | data[i]

        if ((hum + temp) & 0xFF) != chk:
            raise Exception("Checksum error")

        self.humidity = hum
        self.temperature = temp
