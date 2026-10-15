"""PC side of the CAN link with python-can: decode the node's 0x120 frames.
Works with SocketCAN on Linux or the Pi 5, or a USB-CAN adapter on Windows."""
import struct

import can

ENV_ID = 0x120

with can.Bus(interface="socketcan", channel="can0", bitrate=500_000) as bus:
    for msg in bus:                               # iterates forever, one frame at a time
        if msg.arbitration_id != ENV_ID or msg.dlc != 8:
            continue
        t, h, p = struct.unpack("<hHI", msg.data)  # little-endian, as packed on the node
        print(f"{msg.timestamp:.3f}  T {t / 100:.2f} C  H {h / 100:.2f} %  P {p / 100:.2f} hPa")
