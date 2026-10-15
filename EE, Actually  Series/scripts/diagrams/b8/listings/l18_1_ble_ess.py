# MicroPython with aioble: a BLE Environmental Sensing peripheral on the ESP32-S3.
import asyncio
import struct
import aioble
import bluetooth

ESS_UUID = bluetooth.UUID(0x181A)        # Environmental Sensing service
TEMP_UUID = bluetooth.UUID(0x2A6E)       # Temperature: sint16, 0.01 degC
HUM_UUID = bluetooth.UUID(0x2A6F)        # Humidity: uint16, 0.01 %
PRES_UUID = bluetooth.UUID(0x2A6D)       # Pressure: uint32, 0.1 Pa
ADV_INTERVAL_US = 250_000                # advertise every 250 ms

ess = aioble.Service(ESS_UUID)
temp_c = aioble.Characteristic(ess, TEMP_UUID, read=True, notify=True)
hum_c = aioble.Characteristic(ess, HUM_UUID, read=True, notify=True)
pres_c = aioble.Characteristic(ess, PRES_UUID, read=True, notify=True)
aioble.register_services(ess)

def read_sensor():
    return 23.41, 45.2, 1013.25          # from the Chapter 9 driver

async def sensor_task():
    while True:
        t, h, p = read_sensor()
        temp_c.write(struct.pack("<h", round(t * 100)), send_update=True)   # little-endian
        hum_c.write(struct.pack("<H", round(h * 100)), send_update=True)
        pres_c.write(struct.pack("<I", round(p * 1000)), send_update=True)  # hPa -> 0.1 Pa
        await asyncio.sleep_ms(2000)

async def advertise_task():
    while True:
        async with await aioble.advertise(ADV_INTERVAL_US, name="garden-node",
                                          services=[ESS_UUID]) as connection:
            print("connected:", connection.device)
            await connection.disconnected(timeout_ms=None)

async def main():
    await asyncio.gather(sensor_task(), advertise_task())

asyncio.run(main())
