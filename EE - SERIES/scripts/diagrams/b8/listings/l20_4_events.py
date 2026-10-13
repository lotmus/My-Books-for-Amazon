"""Event-camera data: accumulate (x, y, t, polarity) events into frames, and estimate data rates."""
import numpy as np

W, H = 320, 240
EVENT_DTYPE = np.dtype([("x", "<u2"), ("y", "<u2"), ("t", "<u4")])   # 8 bytes; polarity in bit 15 of x

def synthetic_edge(speed_px_per_s=1000.0, duration_s=0.1, seed=2):
    """A vertical edge sweeping right; every crossed pixel fires one ON event (with timing jitter)."""
    rng = np.random.default_rng(seed)
    xs = np.arange(int(speed_px_per_s * duration_s))
    xx, yy = np.meshgrid(xs, np.arange(H))
    t_us = (xx / speed_px_per_s * 1e6 + rng.normal(0, 50, xx.shape)).clip(0)
    ev = np.zeros(xx.size, EVENT_DTYPE)
    ev["x"] = xx.ravel() | 0x8000          # ON polarity
    ev["y"] = yy.ravel()
    ev["t"] = t_us.ravel().astype(np.uint32)
    return np.sort(ev, order="t")

def accumulate(ev, t0_us, window_us):
    """Sum polarities (+1 ON, -1 OFF) of the events inside one time window into an image."""
    sel = ev[(ev["t"] >= t0_us) & (ev["t"] < t0_us + window_us)]
    img = np.zeros((H, W), np.int16)
    pol = np.where(sel["x"] & 0x8000, 1, -1)
    np.add.at(img, (sel["y"], sel["x"] & 0x7FFF), pol)
    return img

if __name__ == "__main__":
    ev = synthetic_edge()
    rate = len(ev) / 0.1
    print("events: %d in 100 ms, %.2f Mev/s, %.2f MB/s at 8 bytes/event" % (len(ev), rate / 1e6, rate * 8 / 1e6))
    frame = accumulate(ev, 50_000, 10_000)
    cols = np.nonzero(frame.any(axis=0))[0]
    print("10 ms window at t = 50 ms: edge spans columns %d..%d" % (cols.min(), cols.max()))
    print("same scene as 8-bit frames at 100 fps: %.2f MB/s" % (W * H * 100 / 1e6))
