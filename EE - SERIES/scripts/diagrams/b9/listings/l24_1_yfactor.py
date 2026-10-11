"""Y-factor noise figure with ENR interpolation and second-stage (Friis) correction, and integration of a
phase-noise curve to RMS phase error and jitter.
Run:  python l24_1_yfactor.py
"""
import math
import numpy as np

def db(x): return 10 * math.log10(x)
def lin(x): return 10 ** (x / 10)

def enr_at(f, table):
    """Linear interpolation of the noise source's ENR table [(f_Hz, ENR_dB), ...]."""
    fs, es = zip(*table)
    return float(np.interp(f, fs, es))

def y_factor_nf(enr_db, y_db, nf2_db=None, gain_db=None):
    f_sys = lin(enr_db) / (lin(y_db) - 1)
    if nf2_db is None:
        return db(f_sys), None
    f_dut = f_sys - (lin(nf2_db) - 1) / lin(gain_db)
    return db(f_sys), db(f_dut)

def integrate_phase_noise(f, L_dbc):
    """RMS phase (rad) from single-sideband L(f) in dBc/Hz: phi^2 = 2 * integral of 10^(L/10) df."""
    s = 10 ** (np.asarray(L_dbc) / 10)
    return math.sqrt(2 * np.trapezoid(s, f))

if __name__ == '__main__':
    table = [(1e9, 15.12), (2e9, 15.0), (3e9, 14.86)]
    enr = enr_at(2e9, table)
    nf_sys, nf_dut = y_factor_nf(enr, 9.50, nf2_db=10.0, gain_db=20.0)
    print('ENR %.2f dB at 2 GHz; NF system %.2f dB, DUT %.2f dB' % (enr, nf_sys, nf_dut))
    f = np.logspace(3, 6, 2000)
    phi = integrate_phase_noise(f, np.full_like(f, -100.0))
    print('flat -100 dBc/Hz, 1 kHz..1 MHz: phi = %.4f rad = %.2f deg, jitter at 1 GHz = %.2f ps'
          % (phi, math.degrees(phi), phi / (2 * math.pi * 1e9) * 1e12))
