"""Book 4, Chapter 48: a minimal Touchstone 1.1 reader for a 2-port file with a noise block,
and the stability, gain and noise calculations of Worked Examples 48.1-48.5.
Standard library only. Check against scikit-rf with check_skrf() if it is installed."""
import cmath, math
def read_s2p(path):
    unit, fmt, z0 = 1e9, 'MA', 50.0
    scale = {'HZ': 1, 'KHZ': 1e3, 'MHZ': 1e6, 'GHZ': 1e9}
    s, noise, last_f, in_noise = [], [], -1.0, False
    for line in open(path):
        line = line.split('!')[0].strip()
        if not line: continue
        if line.startswith('#'):
            tok = line[1:].upper().split(); unit = 1e9; fmt = 'MA'
            for i, t in enumerate(tok):
                if t in scale: unit = scale[t]
                elif t in ('MA', 'DB', 'RI'): fmt = t
                elif t == 'R': z0 = float(tok[i + 1])
                elif t in ('Y', 'Z', 'H', 'G'): raise ValueError('this reader handles S-parameters only')
            continue
        v = [float(x) for x in line.split()]; f = v[0] * unit
        if f <= last_f: in_noise = True        # Touchstone 1.x: noise block starts when frequency does not increase
        last_f = f
        if in_noise:
            noise.append((f, v[1], cmath.rect(v[2], math.radians(v[3])), v[4] * z0)); continue
        def c(a, b):
            if fmt == 'MA': return cmath.rect(a, math.radians(b))
            if fmt == 'DB': return cmath.rect(10 ** (a / 20), math.radians(b))
            return complex(a, b)
        p = [c(v[k], v[k + 1]) for k in (1, 3, 5, 7)]
        s.append((f, p[0], p[1], p[2], p[3]))   # file order N11 N21 N12 N22: S21 comes before S12
    return s, noise, z0
def stability(s11, s21, s12, s22):
    d = s11 * s22 - s12 * s21
    k = (1 - abs(s11) ** 2 - abs(s22) ** 2 + abs(d) ** 2) / (2 * abs(s12 * s21))
    mu = (1 - abs(s11) ** 2) / (abs(s22 - d * s11.conjugate()) + abs(s12 * s21))
    return k, mu, abs(d)
def msg_db(s21, s12): return 10 * math.log10(abs(s21) / abs(s12))
def nf_db(gs, fmin_db, gopt, rn, z0=50.0):
    fmin = 10 ** (fmin_db / 10)
    return 10 * math.log10(fmin + 4 * rn / z0 * abs(gs - gopt) ** 2 / ((1 - abs(gs) ** 2) * abs(1 + gopt) ** 2))
def ga_db(gs, s11, s21, s12, s22):
    gout = s22 + s12 * s21 * gs / (1 - s11 * gs)
    return 10 * math.log10(abs(s21) ** 2 * (1 - abs(gs) ** 2) / (abs(1 - s11 * gs) ** 2 * (1 - abs(gout) ** 2)))
def noise_circle(nf_target_db, fmin_db, gopt, rn, z0=50.0):
    fmin = 10 ** (fmin_db / 10); F = 10 ** (nf_target_db / 10)
    N = (F - fmin) / (4 * rn / z0) * abs(1 + gopt) ** 2
    return gopt / (N + 1), math.sqrt(N * (N + 1 - abs(gopt) ** 2)) / (N + 1)
if __name__ == '__main__':
    import sys
    s, noise, z0 = read_s2p(sys.argv[1] if len(sys.argv) > 1 else 'ATF-54143_3V_60mA.s2p')
    f, s11, s21, s12, s22 = [x for x in s if abs(x[0] - 2e9) < 1][0]
    k, mu, d = stability(s11, s21, s12, s22)
    print('2 GHz: K = %.3f, mu = %.3f, |D| = %.3f, MSG = %.2f dB' % (k, mu, d, msg_db(s21, s12)))
    fn, fmin_db, gopt, rn = [x for x in noise if abs(x[0] - 2e9) < 1][0]
    print('NF with 50 ohm source: %.2f dB; at Gopt: %.2f dB; GA at Gopt: %.2f dB' % (
        nf_db(0, fmin_db, gopt, rn), nf_db(gopt, fmin_db, gopt, rn), ga_db(gopt, s11, s21, s12, s22)))
    for t in (0.6, 0.8, 1.0): print('NF %.1f dB circle: center %s, radius %.3f' % ((t,) + noise_circle(t, fmin_db, gopt, rn)))
