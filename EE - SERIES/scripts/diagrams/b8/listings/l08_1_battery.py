# MicroPython on a Pico: 18650 cell voltage through a 100k/100k divider on GPIO 26 (ADC0).
from machine import ADC
import time

adc = ADC(26)
VREF = 3.3            # replace with the measured 3V3 rail for better accuracy
DIVIDER = 2.0         # (100k + 100k) / 100k

def cell_volts(n=16):
    total = 0
    for _ in range(n):
        total += adc.read_u16() >> 4      # read_u16 scales to 16 bits; the ADC has 12
    code = total / n
    return code * VREF / 4096 * DIVIDER

while True:
    v = cell_volts()
    state = "LOW - shut down soon" if v < 3.3 else "ok"
    print("cell %.3f V  %s" % (v, state))
    time.sleep(5)
