# MicroPython on the ESP32-S3: find the BME280, read its chip ID and raw temperature.
from machine import I2C, Pin
import time

i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=400_000)
print("devices:", [hex(a) for a in i2c.scan()])   # expect 0x3c (OLED) and 0x76

BME = 0x76
chip_id = i2c.readfrom_mem(BME, 0xD0, 1)[0]
print("chip id: 0x%02x" % chip_id)                # 0x60 = BME280, 0x58 = BMP280

i2c.writeto_mem(BME, 0xF2, b"\x01")   # humidity oversampling x1 (set before ctrl_meas)
i2c.writeto_mem(BME, 0xF4, b"\x27")   # temperature x1, pressure x1, normal mode

while True:
    d = i2c.readfrom_mem(BME, 0xFA, 3)            # temp_msb, temp_lsb, temp_xlsb
    raw_t = (d[0] << 12) | (d[1] << 4) | (d[2] >> 4)
    print("raw temperature:", raw_t)              # 20-bit value; compensation needs the calibration data
    time.sleep(1)
