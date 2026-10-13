# MicroPython: publish once per minute with umqtt.simple, reconnecting with back-off.
import network, time, json, random
from umqtt.simple import MQTTClient
import secrets                      # secrets.py on the board: SSID, PASSWORD, BROKER

TOPIC = b"lab/garden/bme280"

def wifi_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        wlan.connect(secrets.SSID, secrets.PASSWORD)
        for _ in range(100):          # up to 10 s
            if wlan.isconnected():
                break
            time.sleep_ms(100)
    return wlan.isconnected()

def backoff_s(attempt):
    base = min(2 ** attempt, 60)
    return base - random.random() * base / 4

client = MQTTClient(b"garden-node-1", secrets.BROKER, keepalive=120)
attempt = 0
while True:
    try:
        if not wifi_connect():
            raise OSError("Wi-Fi")
        client.connect()
        attempt = 0
        while True:
            reading = {"t": 23.41, "h": 45.2, "p": 1013.25}   # from the Chapter 9 driver
            client.publish(TOPIC, json.dumps(reading))
            time.sleep(60)
    except OSError as e:
        wait = backoff_s(attempt)
        print("connection lost (%s), retry in %.1f s" % (e, wait))
        attempt += 1
        time.sleep(wait)
