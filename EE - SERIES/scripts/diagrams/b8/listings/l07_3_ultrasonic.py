# MicroPython: ultrasonic distance with temperature compensation.
# Use a 3.3 V sensor, or divide a 5 V module's echo down to 3.3 V (Book 1).
from machine import Pin, time_pulse_us
import time

TRIG = Pin(6, Pin.OUT, value=0)
ECHO = Pin(7, Pin.IN)

def distance_m(temp_c=20.0):
    TRIG.value(1)
    time.sleep_us(10)                          # 10 us trigger pulse
    TRIG.value(0)
    t_us = time_pulse_us(ECHO, 1, 30_000)      # 30 ms timeout, about 5 m
    if t_us < 0:
        return None                            # no echo: out of range or wiring
    c = 331.3 + 0.606 * temp_c                 # speed of sound in m/s
    return c * t_us * 1e-6 / 2                 # out and back

while True:
    d = distance_m(temp_c=21.5)                # later: the BME280 temperature
    print("no echo" if d is None else "%.3f m" % d)
    time.sleep_ms(100)
