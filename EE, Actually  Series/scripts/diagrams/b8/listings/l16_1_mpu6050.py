# MicroPython: minimal MPU-6050 driver on the ESP32-S3 (I2C on GPIO 8/9).
from machine import I2C, Pin
import struct, time

ADDR = 0x68              # AD0 low; 0x69 with AD0 high
WHO_AM_I, PWR_MGMT_1, ACCEL_XOUT_H = 0x75, 0x6B, 0x3B
ACC_LSB_PER_G = 16384    # +-2 g range (reset default)
GYR_LSB_PER_DPS = 131    # +-250 deg/s range (reset default)

i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=400_000)

def init():
    who = i2c.readfrom_mem(ADDR, WHO_AM_I, 1)[0]
    if who != 0x68:
        raise OSError("MPU-6050 not found, WHO_AM_I=0x%02X" % who)
    i2c.writeto_mem(ADDR, PWR_MGMT_1, b"\x01")   # wake up, clock from X gyro PLL
    time.sleep_ms(100)

def read():
    """Return (ax, ay, az) in g and (gx, gy, gz) in deg/s from one 14-byte burst."""
    raw = i2c.readfrom_mem(ADDR, ACCEL_XOUT_H, 14)
    ax, ay, az, _temp, gx, gy, gz = struct.unpack(">7h", raw)   # big-endian, signed
    acc = tuple(v / ACC_LSB_PER_G for v in (ax, ay, az))
    gyr = tuple(v / GYR_LSB_PER_DPS for v in (gx, gy, gz))
    return acc, gyr

init()
while True:
    acc, gyr = read()
    print("acc %.3f %.3f %.3f g  gyro %.2f %.2f %.2f dps" % (acc + gyr))
    time.sleep_ms(100)
