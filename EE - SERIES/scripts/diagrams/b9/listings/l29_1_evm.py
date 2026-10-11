"""EVM and MER of a 16-QAM signal with known impairments, and the budget that predicts them.

Data-aided measurement as a VSA does it after symbol recovery: fit one complex gain to the reference
symbols, then EVM = rms(error) / rms(reference). With a real analyzer, fetch the measured symbols (or
read the EVM result directly: Keysight 89600/X-Series "FETC:EVM?"-style queries, R&S "FETC:...:EVM?";
check the guide) and use this to explain the number.
Run:  python l29_1_evm.py  [snr_dB phase_rms_deg gain_imbalance_dB]
"""
import math
import sys
import numpy as np

LEV = np.array([-3, -1, 1, 3])

def qam16(n, seed=29):
    rng = np.random.default_rng(seed)
    s = rng.choice(LEV, n) + 1j * rng.choice(LEV, n)
    return s / math.sqrt(10)                                            # unit average power

def impair(s, snr_db=30.0, phase_rms_deg=0.0, gain_db=0.0, seed=291):
    rng = np.random.default_rng(seed)
    g = 10 ** (gain_db / 20)
    x = s.real * math.sqrt(g) + 1j * s.imag / math.sqrt(g)              # I/Q gain imbalance (split)
    x = x * np.exp(1j * rng.normal(0, math.radians(phase_rms_deg), s.size))
    n = (rng.normal(0, 1, s.size) + 1j * rng.normal(0, 1, s.size)) * 10 ** (-snr_db / 20) / math.sqrt(2)
    return x + n

def evm(meas, ref):
    a = np.vdot(ref, meas) / np.vdot(ref, ref)                          # best complex gain (normalization)
    e = meas / a - ref
    rms = math.sqrt(np.mean(np.abs(e) ** 2) / np.mean(np.abs(ref) ** 2))
    mer = 10 * math.log10(np.mean(np.abs(ref) ** 2) / np.mean(np.abs(e) ** 2))
    return 100 * rms, 20 * math.log10(rms), mer

def budget(snr_db, phase_rms_deg, gain_db):
    """Predicted EVM (%) from independent contributions added in power."""
    g = 10 ** (gain_db / 20)
    parts = {'noise': 10 ** (-snr_db / 20), 'phase noise': math.radians(phase_rms_deg),
             'IQ gain': abs(math.sqrt(g) - 1 / math.sqrt(g)) / 2}            # I up, Q down: +-half the split
    return 100 * math.sqrt(sum(v * v for v in parts.values())), parts

if __name__ == '__main__':
    snr, ph, gdb = (float(x) for x in sys.argv[1:4]) if len(sys.argv) > 3 else (30.0, 0.81, 0.2)
    ref = qam16(20000)
    pct, db, mer = evm(impair(ref, snr, ph, gdb), ref)
    pred, parts = budget(snr, ph, gdb)
    print('measured EVM %.2f %% (%.1f dB), MER %.1f dB' % (pct, db, mer))
    print('predicted %.2f %%: ' % pred + ', '.join('%s %.2f %%' % (k, 100 * v) for k, v in parts.items()))
