"""PC side: subscribe to the garden node and append every reading to a CSV file."""
import csv
import json
from datetime import datetime, timezone

import paho.mqtt.client as mqtt

BROKER = "localhost"          # Mosquitto on the PC or the Pi 5
TOPIC = "lab/garden/#"

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload)
    except ValueError:
        print("bad payload on", msg.topic, msg.payload[:40])
        return
    row = [datetime.now(timezone.utc).isoformat(timespec="seconds"), msg.topic,
           data.get("t"), data.get("h"), data.get("p")]
    with open("garden.csv", "a", newline="") as f:
        csv.writer(f).writerow(row)
    print(*row)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message
client.on_connect = lambda c, u, flags, rc, props: c.subscribe(TOPIC, qos=1)
client.connect(BROKER, 1883, keepalive=60)
client.loop_forever()
