"""FMCW chirp linearity from an I/Q capture: instantaneous frequency from the phase derivative, a straight-
line fit over the stated fit window (the middle 90 % of the ramp, skipping the turnaround), the residual,
and what the nonlinearity does to range resolution. Also the LoRa symbol time and bit rate.

The capture is a wideband I/Q record from a VSA (or a downconverted record from a scope); the chirp here is
a 4 GHz ramp scaled to baseband: the analysis is identical. Run:  python l32_1_chirp_linearity.py
"""
import math
import numpy as np

C = 299792458.0

def chirp_iq(bw=4e9, T=40e-6, fs=10e9, quad=0.002, ripple=0.0005, fr=3, snr_db=40, seed=32):
    """Ramp of bw in T, with a bowed (quadratic) error of quad*bw and a ripple of ripple*bw (fr cycles)."""
    t = np.arange(int(T * fs)) / fs; u = t / T
    f = bw * (u - 0.5) + quad * bw * (4 * u * (1 - u) - 2 / 3) + ripple * bw * np.sin(2 * np.pi * fr * u)
    ph = 2 * np.pi * np.cumsum(f) / fs
    rng = np.random.default_rng(seed)
    n = (rng.normal(0, 1, t.size) + 1j * rng.normal(0, 1, t.size)) * 10 ** (-snr_db / 20) / math.sqrt(2)
    return t, np.exp(1j * ph) + n, fs

def linearity(t, z, fs, keep=0.9, smooth=64):
    fi = np.diff(np.unwrap(np.angle(z))) * fs / (2 * np.pi)
    fi = np.convolve(fi, np.ones(smooth) / smooth, mode='same'); tt = t[1:]
    T = t[-1]; m = (tt > T * (1 - keep) / 2) & (tt < T * (1 + keep) / 2) # fit window: middle 90 %
    m[:smooth] = False; m[-smooth:] = False
    slope, icpt = np.polyfit(tt[m], fi[m], 1)
    res = fi - (slope * tt + icpt)
    return slope, res, m, tt

if __name__ == '__main__':
    bw, T = 4e9, 40e-6
    t, z, fs = chirp_iq(bw, T)
    S, res, m, tt = linearity(t, z, fs)
    rms, pk = res[m].std(), np.abs(res[m]).max()
    print('fit window %.1f to %.1f us; slope %.4f MHz/us (nominal %.4f)' % (tt[m][0] * 1e6, tt[m][-1] * 1e6, S / 1e12, bw / T / 1e12))
    print('residual rms %.2f MHz (%.3f %% of bw), peak %.2f MHz (%.3f %%)' % (rms / 1e6, 100 * rms / bw, pk / 1e6, 100 * pk / bw))
    R = 10.0; fb = 2 * R * S / C
    print('target at %.0f m: beat %.3f MHz; ideal resolution %.2f cm' % (R, fb / 1e6, 100 * C / (2 * bw)))
    u = (tt[m] - tt[m].mean()) / T                                         # smooth model of the residual
    dres = np.polyder(np.polyfit(u, res[m], 9)); sl = np.polyval(dres, u) / T  # local slope error (Hz/s)
    spread = 2 * R / C * (sl.max() - sl.min())
    print('local slope varies %.2f %% peak to peak; beat spread at %.0f m %.0f kHz vs FFT bin %.0f kHz'
          % (100 * (sl.max() - sl.min()) / S, R, spread / 1e3, 1 / T / 1e3))
    sf, B, cr = 9, 125e3, 4 / 5
    print('LoRa SF%d, %.0f kHz: symbol %.3f ms, bit rate %.0f bit/s' % (sf, B / 1e3, 2 ** sf / B * 1e3, sf * B / 2 ** sf * cr))
