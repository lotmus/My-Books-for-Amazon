# MicroPython on the ESP32-S3: count wake-ups in RTC memory, sleep 10 minutes or until the PIR fires.
import esp32
import machine
from machine import Pin

pir = Pin(5, Pin.IN, Pin.PULL_DOWN)
esp32.wake_on_ext0(pin=pir, level=esp32.WAKEUP_ANY_HIGH)

rtc = machine.RTC()
mem = rtc.memory()                       # bytes kept through deep sleep
boots = int(mem) + 1 if mem else 1
rtc.memory(str(boots))

if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print("woke, boot", boots, "wake reason", machine.wake_reason())
else:
    print("power-on")

# ... read the sensor and send the reading ...
machine.deepsleep(10 * 60 * 1000)        # milliseconds
