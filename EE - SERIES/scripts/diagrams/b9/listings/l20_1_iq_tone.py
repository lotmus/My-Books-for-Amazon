"""I/Q samples of a +1 MHz single-sideband tone with gain and phase imbalance and a DC offset; the spectrum
shows the image at -1 MHz and the LO leakage at 0 Hz, as a VSG's modulator would produce them.

Run:  python l20_1_iq_tone.py  [gain_dB phase_deg dc]
The samples (i, q) can be written to a file for a VSG's arbitrary waveform memory.
"""
import math
import sys
import numpy as np

def iq_tone(f=1e6, fs=100e6, n=100000, gain_db=0.1, phase_deg=1.0, dc=0.0):
    t = np.arange(n) / fs
    g = 10 ** (gain_db / 20); ph = math.radians(phase_deg)
    i = np.cos(2 * np.pi * f * t) + dc
    q = g * np.sin(2 * np.pi * f * t + ph) + dc
    return i, q, fs

def levels(i, q, fs, f=1e6):
    z = i + 1j * q
    s = np.fft.fftshift(np.fft.fft(z * np.hanning(z.size)))
    fr = np.fft.fftshift(np.fft.fftfreq(z.size, 1 / fs))
    p = 20 * np.log10(np.abs(s) + 1e-30)
    at = lambda x: p[int(np.argmin(abs(fr - x)))]
    ref = at(f)
    return at(-f) - ref, at(0.0) - ref

if __name__ == '__main__':
    gdb, pdeg, dc = (float(x) for x in sys.argv[1:4]) if len(sys.argv) > 3 else (0.1, 1.0, 0.0)
    i, q, fs = iq_tone(gain_db=gdb, phase_deg=pdeg, dc=dc)
    img, lo = levels(i, q, fs)
    g = 10 ** (gdb / 20); ph = math.radians(pdeg)
    irr = 10 * math.log10((1 + 2 * g * math.cos(ph) + g * g) / (1 - 2 * g * math.cos(ph) + g * g))
    print('image %.1f dBc (formula: %.1f dB rejection); LO leakage %.1f dBc' % (img, irr, lo))
