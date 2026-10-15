"""Affine int8 quantization as used by TensorFlow Lite Micro: real = scale * (q - zero_point)."""
import numpy as np

def qparams(rmin, rmax):
    scale = (rmax - rmin) / 255.0
    zero_point = int(round(-128 - rmin / scale))
    return scale, zero_point

def quantize(x, scale, zp):
    return np.clip(np.round(x / scale) + zp, -128, 127).astype(np.int8)

def dequantize(q, scale, zp):
    return scale * (q.astype(np.int32) - zp)

if __name__ == "__main__":
    s, zp = qparams(-2.0, 6.0)
    print("scale %.5f (8/255), zero point %d" % (s, zp))
    x = np.array([-2.0, 0.0, 1.0, 3.3, 6.0])
    q = quantize(x, s, zp)
    print("q =", q.tolist(), " back =", np.round(dequantize(q, s, zp), 4).tolist())
    rng = np.random.default_rng(0)
    v = rng.uniform(-2, 6, 10_000)
    err = np.abs(dequantize(quantize(v, s, zp), s, zp) - v)
    print("max error %.5f (scale/2 = %.5f)" % (err.max(), s / 2))
    # A dot product the way an int8 kernel does it: int8 x int8 products summed in int32.
    w = rng.uniform(-1, 1, 64); a = rng.uniform(-2, 6, 64)
    sw, zw = qparams(-1, 1); qw = quantize(w, sw, zw); qa = quantize(a, s, zp)
    acc = np.sum((qw.astype(np.int32) - zw) * (qa.astype(np.int32) - zp))
    print("float %.4f, int8 %.4f" % (w @ a, sw * s * acc))
