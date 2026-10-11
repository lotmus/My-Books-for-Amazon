"""Analog demodulation from I/Q captures: FM deviation from the derivative of the phase, AM depth from the
envelope, and the Bessel-null check (carrier vanishes at beta = 2.405) for calibrating a deviation meter.

The instrument part fetches I/Q from a signal analyzer's I/Q (basic) mode; command names differ by vendor
(Keysight X-Series: CONF:WAV, READ:WAV0?; R&S FSx: TRAC:IQ ON, TRAC:IQ:DATA?). Check the programming guide.
Run:  python l28_1_fm_deviation.py --sim
"""
import argparse
import math
import numpy as np

def fm_iq(fm=1e3, dev=2.405e3, fs=1e6, n=200000, snr_db=60, am=0.0, seed=28):
    t = np.arange(n) / fs
    phase = dev / fm * np.sin(2 * np.pi * fm * t)                       # beta = dev/fm
    env = 1 + am * np.cos(2 * np.pi * fm * t)
    rng = np.random.default_rng(seed)
    noise = (rng.normal(0, 1, n) + 1j * rng.normal(0, 1, n)) * 10 ** (-snr_db / 20) / math.sqrt(2)
    return env * np.exp(1j * phase) + noise, fs

def demod(z, fs):
    """Return (peak deviation in Hz, AM depth) of an I/Q record; deviation from the instantaneous frequency."""
    fi = np.diff(np.unwrap(np.angle(z))) * fs / (2 * np.pi)
    fi -= fi.mean()                                                     # remove carrier offset
    k = np.ones(25) / 25; fi = np.convolve(fi, k, mode='valid')         # post-detection low-pass (~40 kHz)
    env = np.abs(z); m = (env.max() - env.min()) / (env.max() + env.min())
    return math.sqrt(2) * fi.std(), m                                    # sine tone: peak = sqrt(2) x rms

def carrier_dbc(z):
    """Carrier level relative to total power, from an FFT of the record (Bessel null check)."""
    s = np.abs(np.fft.fft(z * np.hanning(z.size))) ** 2
    return 10 * math.log10(s[0] / s.sum() * 1.5 + 1e-30)                # Hann: main lobe spans 3 bins (sum 1.5)

class SimVSA:
    def __init__(self, dev): self.dev = dev
    def query(self, cmd): return 'SIM,VSA,0,1.0'
    def iq(self): return fm_iq(dev=self.dev)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('resource', nargs='?'); ap.add_argument('--sim', action='store_true')
    a = ap.parse_args()
    if not a.sim:
        raise SystemExit('connect a real analyzer: replace SimVSA.iq() with the vendor I/Q fetch (see docstring)')
    for dev in (1.0e3, 2.405e3, 5.0e3):
        z, fs = SimVSA(dev).iq()
        d, m = demod(z, fs)
        print('set %.3f kHz: measured deviation %.3f kHz, AM depth %.4f, carrier %.1f dBc'
              % (dev / 1e3, d / 1e3, m, carrier_dbc(z)))
    print('Carson bandwidth for 75 kHz deviation, 15 kHz audio: %.0f kHz' % (2 * (75 + 15)))

if __name__ == '__main__':
    main()
