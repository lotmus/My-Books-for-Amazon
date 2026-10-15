# MicroPython on the ESP32-S3: SSD1306 128x64 OLED over SPI at 8 MHz,
# using the ssd1306 driver module from micropython-lib.
from machine import Pin, SPI
import time
import ssd1306

spi = SPI(1, baudrate=8_000_000, polarity=0, phase=0,      # SPI mode 0
          sck=Pin(12), mosi=Pin(11))
oled = ssd1306.SSD1306_SPI(128, 64, spi, dc=Pin(13), res=Pin(14), cs=Pin(10))

frames = 0
t0 = time.ticks_ms()
while True:
    oled.fill(0)
    oled.text("BME280 node", 0, 0)
    oled.text("T 23.41 C", 0, 16)
    oled.text("frame %d" % frames, 0, 32)
    oled.show()                       # sends the 1024-byte frame buffer
    frames += 1
    if frames % 100 == 0:
        dt = time.ticks_diff(time.ticks_ms(), t0)
        print("%.1f frames/s" % (100_000 / dt))
        t0 = time.ticks_ms()
