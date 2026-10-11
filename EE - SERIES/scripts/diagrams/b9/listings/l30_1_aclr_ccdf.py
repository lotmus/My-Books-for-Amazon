"""Channel power, ACLR, and CCDF of an OFDM-like signal through an amplifier model, computed the way a
signal analyzer does it: integrate the power spectral density over each channel bandwidth; count how often
the instantaneous power exceeds the average by x dB.

On a real analyzer use its measurement personalities (Keysight X-Series: CONF:ACP / READ:ACP?, and
CONF:PST / READ:PST? for CCDF; R&S FSx: CALC:MARK:FUNC:POW:SEL ACP; check the guide); this listing
shows what those numbers mean and lets you predict them.
Run:  python l30_1_aclr_ccdf.py  [backoff_dB]
"""
import math
import sys
import numpy as np

def ofdm(nsym=200, nfft=1024, used=600, osr=4, seed=30):
    """Baseband OFDM with QPSK on `used` subcarriers, oversampled by osr. Returns samples and fs/bw ratio."""
    rng = np.random.default_rng(seed)
    out = []
    for _ in range(nsym):
        X = np.zeros(nfft * osr, complex)
        k = np.r_[1:used // 2 + 1, -used // 2:0]
        X[k] = (rng.choice([-1, 1], used) + 1j * rng.choice([-1, 1], used)) / math.sqrt(2)
        out.append(np.fft.ifft(X))
    x = np.concatenate(out)
    return x / math.sqrt(np.mean(np.abs(x) ** 2)), used / (nfft * osr)  # occupied bw as fraction of fs

def rapp_pa(x, backoff_db=8.0, p=2.0):
    """Rapp AM/AM model: saturates smoothly at |x| = 1; input scaled so the average is backoff_db below."""
    xin = x * 10 ** (-backoff_db / 20)
    a = np.abs(xin)
    return xin / (1 + a ** (2 * p)) ** (1 / (2 * p))

def psd(x, nseg=4096):
    w = np.hanning(nseg); segs = x[: x.size // nseg * nseg].reshape(-1, nseg)
    s = np.mean(np.abs(np.fft.fft(segs * w, axis=1)) ** 2, axis=0)
    return np.fft.fftshift(np.fft.fftfreq(nseg)), np.fft.fftshift(s)

def aclr(x, bw):
    """Main channel power and adjacent channel ratios (lower, upper) in dB; channel spacing = bw * 1.1."""
    f, s = psd(x)
    band = lambda c: s[np.abs(f - c) <= bw / 2].sum()
    main = band(0.0)
    return 10 * math.log10(band(-1.1 * bw) / main), 10 * math.log10(band(1.1 * bw) / main)

def ccdf(x, probs=(1e-2, 1e-3, 1e-4)):
    """Power level (dB above average) exceeded with each probability."""
    p = np.abs(x) ** 2 / np.mean(np.abs(x) ** 2)
    return [10 * math.log10(np.quantile(p, 1 - q)) for q in probs]

if __name__ == '__main__':
    bo = float(sys.argv[1]) if len(sys.argv) > 1 else 8.0
    x, bw = ofdm()
    print('input  CCDF 1 %%/0.1 %%/0.01 %%: %.1f / %.1f / %.1f dB' % tuple(ccdf(x)))
    y = rapp_pa(x, bo)
    print('output CCDF 1 %%/0.1 %%/0.01 %%: %.1f / %.1f / %.1f dB' % tuple(ccdf(y)))
    lo, hi = aclr(y, bw)
    print('backoff %.1f dB: ACLR lower %.1f dB, upper %.1f dB' % (bo, lo, hi))
