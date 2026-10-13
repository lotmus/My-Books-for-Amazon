"""Log 'temperature,humidity,pressure' lines from the ESP32-S3 to log.csv with PC timestamps."""
import csv
import sys
from datetime import datetime

import serial  # pyserial

PORT = sys.argv[1] if len(sys.argv) > 1 else "COM5"

with serial.Serial(PORT, 115200, timeout=2) as ser, open("log.csv", "a", newline="") as f:
    writer = csv.writer(f)
    while True:
        line = ser.readline().decode("ascii", errors="replace").strip()
        if not line:
            print("timeout: no data for 2 s")
            continue
        fields = line.split(",")
        if len(fields) != 3:
            print("bad line:", line)
            continue
        try:
            t, h, p = (float(x) for x in fields)
        except ValueError:
            print("bad number:", line)
            continue
        writer.writerow([datetime.now().isoformat(timespec="seconds"), t, h, p])
        f.flush()   # keep the file valid if the script is stopped
