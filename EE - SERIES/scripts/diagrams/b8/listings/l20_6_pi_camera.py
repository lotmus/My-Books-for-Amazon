"""Raspberry Pi 5: capture frames with Picamera2 and flag motion by frame differencing."""
import time
import numpy as np
from picamera2 import Picamera2

picam2 = Picamera2()
picam2.configure(picam2.create_video_configuration(main={"size": (640, 480), "format": "RGB888"}))
picam2.start()
time.sleep(1.0)                                   # let exposure and white balance settle

prev = None
t0, n = time.monotonic(), 0
while n < 300:
    frame = picam2.capture_array()                # 480 x 640 x 3, uint8
    gray = frame.mean(axis=2).astype(np.int16)
    if prev is not None:
        changed = np.count_nonzero(np.abs(gray - prev) > 25) / gray.size
        if changed > 0.02:                        # more than 2 % of pixels changed
            print("motion: %.1f %% of pixels" % (changed * 100))
    prev, n = gray, n + 1
print("%.1f fps" % (n / (time.monotonic() - t0)))
picam2.stop()
