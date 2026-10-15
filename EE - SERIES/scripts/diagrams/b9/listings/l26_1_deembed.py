"""De-embedding with transfer (T) matrices: measured = A * D * B, so D = A^-1 * measured * B^-1.
The self-test embeds a known device in two lossy, mismatched fixture halves and recovers it.
Run:  python l26_1_deembed.py
"""
import numpy as np

def s2t(s):
    s11, s12, s21, s22 = s[0, 0], s[0, 1], s[1, 0], s[1, 1]
    return np.array([[-(s11 * s22 - s12 * s21) / s21, s11 / s21], [-s22 / s21, 1 / s21]])

def t2s(t):
    t11, t12, t21, t22 = t[0, 0], t[0, 1], t[1, 0], t[1, 1]
    return np.array([[t12 / t22, (t11 * t22 - t12 * t21) / t22], [1 / t22, -t21 / t22]])

def cascade(*s_list):
    t = np.eye(2, dtype=complex)
    for s in s_list:
        t = t @ s2t(s)
    return t2s(t)

def deembed(meas, fix_a, fix_b):
    return t2s(np.linalg.inv(s2t(fix_a)) @ s2t(meas) @ np.linalg.inv(s2t(fix_b)))

def line(theta, loss_db, gamma=0.0):
    """A line section of electrical length theta (rad) and loss, with a small mismatch at its ports."""
    a = 10 ** (-loss_db / 20) * np.exp(-1j * theta)
    return np.array([[gamma, a], [a, -gamma]], dtype=complex)

if __name__ == '__main__':
    dut = np.array([[0.30 * np.exp(1j * 0.4), 0.80 * np.exp(-1j * 1.1)],
                    [0.80 * np.exp(-1j * 1.1), 0.25 * np.exp(-1j * 0.7)]])
    fa, fb = line(1.3, 0.4, 0.08), line(0.9, 0.3, 0.05)
    meas = cascade(fa, dut, fb)
    back = deembed(meas, fa, fb)
    print('measured S21 %.3f dB, de-embedded %.3f dB, true %.3f dB'
          % (20 * np.log10(abs(meas[1, 0])), 20 * np.log10(abs(back[1, 0])), 20 * np.log10(abs(dut[1, 0]))))
    print('max error after de-embedding: %.2e' % np.max(np.abs(back - dut)))
    thru = cascade(fa, fb)
    print('de-embedded through: S21 = %.4f dB' % (20 * np.log10(abs(deembed(thru, fa, fb)[1, 0]))))
