"""Uncertainty budget of an RF power measurement (Chapter 2 methods), and pulse power from average power.
Run:  python l23_1_power_budget.py
"""
import math

def gamma(vswr):
    return (vswr - 1) / (vswr + 1)

def budget(src_vswr, sen_vswr, cf_pct, lin_pct, noise_pct=0.0, zero_pct=0.0, k=2):
    p = gamma(src_vswr) * gamma(sen_vswr)
    mm_pct = ((1 + p) ** 2 - 1) * 100                      # power limit, U-shaped
    terms = {'mismatch (U-shaped)': mm_pct / math.sqrt(2),
             'cal factor (rect)': cf_pct / math.sqrt(3),
             'linearity (rect)': lin_pct / math.sqrt(3),
             'noise (normal)': noise_pct, 'zero (rect)': zero_pct / math.sqrt(3)}
    u = math.sqrt(sum(v * v for v in terms.values()))
    return p, terms, u, k * u

def pulse_power_dbm(avg_dbm, width_s, prf_hz):
    return avg_dbm - 10 * math.log10(width_s * prf_hz)

if __name__ == '__main__':
    p, terms, u, U = budget(1.5, 1.15, 1.5, 1.0)
    print('|Gs||Gl| = %.4f: mismatch %+.3f / %+.3f dB' % (p, 20 * math.log10(1 + p), 20 * math.log10(1 - p)))
    for name, v in terms.items():
        if v:
            print('  %-20s u = %.2f %%' % (name, v))
    print('combined u = %.2f %%, expanded U (k=2) = %.1f %% = +/-%.2f dB' % (u, U, 10 * math.log10(1 + U / 100)))
    print('radar: average 37 dBm, 1 us at 1 kHz -> pulse %.0f dBm' % pulse_power_dbm(37, 1e-6, 1e3))
