# MicroPython (Pico or ESP32-S3): a button interrupt that only records the time;
# the main loop applies a 50 ms lockout and does the work.
from machine import Pin
import time

button = Pin(14, Pin.IN, Pin.PULL_UP)     # button to GND, active low
last_edge = 0
pressed = False

def on_edge(pin):
    global last_edge, pressed
    last_edge = time.ticks_ms()
    pressed = True                       # keep the handler tiny

button.irq(trigger=Pin.IRQ_FALLING, handler=on_edge)

count = 0
while True:
    if pressed and time.ticks_diff(time.ticks_ms(), last_edge) > 50:
        pressed = False
        if button.value() == 0:          # still held after the bounces: a real press
            count += 1
            print("press", count)
    time.sleep_ms(5)
