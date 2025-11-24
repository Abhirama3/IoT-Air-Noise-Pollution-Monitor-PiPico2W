# MicroPython SSD1306 OLED driver, I2C and SPI interfaces

import time
from micropython import const
from machine import Pin

# Commands
SET_CONTRAST        = const(0x81)
SET_ENTIRE_ON       = const(0xA4)
SET_NORM_INV        = const(0xA6)
SET_DISP            = const(0xAE)
SET_MEM_ADDR        = const(0x20)
SET_COL_ADDR        = const(0x21)
SET_PAGE_ADDR       = const(0x22)
SET_DISP_START_LINE = const(0x40)
SET_SEG_REMAP       = const(0xA0)
SET_MUX_RATIO       = const(0xA8)
SET_COM_OUT_DIR     = const(0xC0)
SET_DISP_OFFSET     = const(0xD3)
SET_COM_PIN_CFG     = const(0xDA)
SET_DISP_CLK_DIV    = const(0xD5)
SET_PRECHARGE       = const(0xD9)
SET_VCOM_DESEL      = const(0xDB)
SET_CHARGE_PUMP     = const(0x8D)


class SSD1306:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pages = self.height // 8
        self.buffer = bytearray(self.pages * self.width)
        self.init_display()

    def init_display(self):
        for cmd in (
            SET_DISP | 0x00,
            SET_MEM_ADDR, 0x00,
            SET_DISP_START_LINE | 0x00,
            SET_SEG_REMAP | 0x01,
            SET_MUX_RATIO, self.height - 1,
            SET_COM_OUT_DIR | 0x08,
            SET_DISP_OFFSET, 0x00,
            SET_COM_PIN_CFG, 0x12,
            SET_DISP_CLK_DIV, 0x80,
            SET_PRECHARGE, 0xF1,
            SET_VCOM_DESEL, 0x30,
            SET_CONTRAST, 0xFF,
            SET_ENTIRE_ON,
            SET_NORM_INV,
            SET_CHARGE_PUMP, 0x14,
            SET_DISP | 0x01,
        ):
            self.write_cmd(cmd)
        self.fill(0)
        self.show()

    def poweroff(self):
        self.write_cmd(SET_DISP | 0x00)

    def poweron(self):
        self.write_cmd(SET_DISP | 0x01)

    def contrast(self, contrast):
        self.write_cmd(SET_CONTRAST)
        self.write_cmd(contrast)

    def invert(self, invert):
        self.write_cmd(SET_NORM_INV | (invert & 1))

    def show(self):
        self.write_cmd(SET_COL_ADDR)
        self.write_cmd(0)
        self.write_cmd(self.width - 1)

        self.write_cmd(SET_PAGE_ADDR)
        self.write_cmd(0)
        self.write_cmd(self.pages - 1)

        self.write_data(self.buffer)

    def fill(self, col):
        for i in range(len(self.buffer)):
            self.buffer[i] = 0xFF * col

    def pixel(self, x, y, col):
        index = x + (y // 8) * self.width
        mask = 1 << (y & 7)
        if col:
            self.buffer[index] |= mask
        else:
            self.buffer[index] &= ~mask

    def text(self, string, x, y):
        from framebuf import FrameBuffer, MONO_VLSB
        fb = FrameBuffer(self.buffer, self.width, self.height, MONO_VLSB)
        fb.text(string, x, y)


class SSD1306_I2C(SSD1306):
    def __init__(self, width, height, i2c, addr=0x3C):
        self.i2c = i2c
        self.addr = addr
        super().__init__(width, height)

    def write_cmd(self, cmd):
        self.i2c.writeto(self.addr, b"\x00" + bytes([cmd]))

    def write_data(self, buf):
        self.i2c.writeto(self.addr, b"\x40" + buf)


class SSD1306_SPI(SSD1306):
    def __init__(self, width, height, spi, dc, res, cs):
        self.spi = spi
        self.dc = dc
        self.res = res
        self.cs = cs

        self.dc.init(self.dc.OUT, value=0)
        self.res.init(self.res.OUT, value=0)
        self.cs.init(self.cs.OUT, value=1)

        # Reset
        self.res(1)
        time.sleep_ms(1)
        self.res(0)
        time.sleep_ms(10)
        self.res(1)

        super().__init__(width, height)

    def write_cmd(self, cmd):
        self.cs(1)
        self.dc(0)
        self.cs(0)
        self.spi.write(bytearray([cmd]))
        self.cs(1)

    def write_data(self, buf):
        self.cs(1)
        self.dc(1)
        self.cs(0)
        self.spi.write(buf)
        self.cs(1)

