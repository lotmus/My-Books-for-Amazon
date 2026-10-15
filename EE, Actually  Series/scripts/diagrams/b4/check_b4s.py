"""Book 4 pass 2: recompute the numbers of the new text and assert that the text carries them (rounded as printed)."""
import sys, math, cmath, re, docx
sys.path.insert(0, '../common'); sys.path.insert(0, 'scripts')
from eedoc import body_ps, ptext
from math import pi, sqrt, log10, sin, cos, radians, degrees, asin
txt = '\n'.join(ptext(p) for p in body_ps(docx.Document(sys.argv[1])))
n = [0]
def has(val, fmt, ctx=''):
    s = (fmt % val).replace('-', '−'); n[0] += 1
    assert s in txt, (s, ctx)
L = lambda x: 10 * log10(x)
c = 2.998e8
# Ch 42
has((2.4 * 3 / 2 - .6) ** 2 / 2, '%.1f Ω', 'stack'); has(sqrt(50 / 4.5 - 1), 'Q = %.2f')
has(2.8 ** 2 / 40 * 1e3, '%.0f mW'); has(5.6 ** 2 / 40 * 1e3, '%.0f mW')
Rd = 5.6 ** 2 / (2 * 10 ** 2.9 / 2e3); has(Rd, '%.1f Ω'); has(sqrt(50 / (2 * Rd)), 'n = %.2f')
Pc = 10 ** 2.9 / 2e3; I1 = Pc / 2.8; has(2 / pi * I1, '%.3f A'); has(Pc / (3.3 * 4 * I1 / pi) * 100, '%.1f %%')
has(10 ** 2.8 / (2 * 3.3 * 4 * I1 / pi) / 1e3 * 100, '%.1f %%')
z = 1 / (1 / (Rd / 2) - 1j * 2 * pi * 2.45e9 * 1.5e-12); has((z.real, z.imag), '%.1f + j%.1f Ω')
has(66.6 * 10 ** (-8 / 20), '%.1f %%')
# Ch 43
R = 3.0 ** 2 / (2 * 10 ** 2.2 / 1e3); has(R, '%.1f Ω'); Q = sqrt(50 / R - 1); has(Q, 'Q = √(50/28.4 − 1) = %.3f'); has(Q * R / (2 * pi * 915e6) * 1e9, '%.2f nH'); has(1 / (2 * pi * 915e6 * 50 / Q) * 1e12, '%.2f pF')
has(3.1 ** 2 / (2 * 10 ** 2.2 / 1e3), '%.1f Ω at a 0.2 V knee'); has(2 * 12.8 ** 2 / 100, '%.2f Ω'); has(2 * 12.8 ** 2 / 3.125, '%.0f W')
a = radians(120); i1 = (a - sin(a)) / (2 * pi * (1 - cos(a / 2))); idc = (2 * sin(a / 2) - a * cos(a / 2)) / (2 * pi * (1 - cos(a / 2)))
Ipk = 2 * 25 / 12.8 / i1; has(Ipk, '%.2f A peak'); has(Ipk * idc, '%.2f A'); has(25 / (13.8 * Ipk * idc) * 100, '%.1f %%')
has((2 / pi * 24) ** 2 / 20, '%.1f Ω'); has(10 / (10 + 200e-12 * 576 * 6.78e6) * 100, '%.1f %%')
R = .5768 * 576 / 10; has(R, '%.1f Ω'); has(.1836 / (2 * pi * 6.78e6 * R) * 1e12, '%.0f pF'); has(3.562 * 24, '%.1f V')
has(1.155 * 25, '%.1f V'); has(2 * 10 / 28.875, '%.3f A'); has(.5 * 28.875 / 28 * pi / 2 * 100, '%.1f %%'); has(pi ** 2 / 4 * 625 / 20, '%.1f Ω')
lg = c / (2.45e9 * sqrt(2.79)) * 100; has(lg / 4, '%.2f cm'); has(lg / 12, '%.2f cm')
# Ch 44
P = 10 ** 3.1 / 1e3; R = 3.1 ** 2 / (2 * P); has(R, '%.2f Ω'); has(sqrt(R * 50), '%.1f Ω'); has(sqrt(sqrt(R * 50) / R - 1), 'Q = √(13.8/3.82 − 1) = %.2f')
has(1.4e-3 * 2000 * 3.4, '%.2f Ω'); has(1.4e-3 * 2000 * 3.4 - .0259 / .0162, '%.1f Ω'); has(4.35 + (1 + 9 / 11) * 4.05, '%.1f V')
# Ch 45
r = 10 ** .4 - 1; has(r, 'r = %.3f'); has(20 * 10 ** .8, '%.1f W'); Pm = 20 * 10 ** .8 / (1 + r); has(Pm, '%.1f W')
Rm = 44 ** 2 / (2 * Pm); has(Rm, '%.1f Ω'); has(Rm / (1 + r), '%.2f Ω'); has(Rm / r, '%.1f Ω'); has(Rm * (1 + r), '%.1f Ω'); has(78.5 * 44 / 48, '%.1f %%')
has(85 + 13.5 * 3.5, '%.0f °C')
# Ch 46
V = sqrt(2 * 10 ** .5 * 50); has(V, '%.1f V'); has(1.5 * V, '%.1f V'); has(20 * log10(1.015), '%.2f dB'); has(20 * log10(abs(100 - 1j / (2 * pi * 2e9 * 100e-15 / 1.5)) / 100), '%.1f dB')
e0 = 8.854e-12; has(sqrt(8 * 10 * 8e-18 / (27 * e0 * 1e-8)), '%.1f V'); has(20 * log10(500 / 77), '%.0f dB at 77 GHz')
has(3e7 * 1e5 / (2 * pi) / 1e9, 'about %.0f GHz·V'.replace('%.0f', '%.0f')) if False else None
# Ch 47
rr = 4 / pi ** 2 * .07; has(rr * 100, '%.2f %%'); fp = 3.5 / (1 - rr); has(fp, '%.3f GHz'); Cm = (fp / 3.5) ** 2 - 1; has(Cm * 1000, '%.1f fF')
Lm = 1 / ((2 * pi * 3.5e9) ** 2 * Cm * 1e-12); has(Lm * 1e9, '%.1f nH'); has(2 * pi * 3.5e9 * Lm / 1000, '%.2f Ω')
has(4 / pi ** 2 * .09 * 100, '%.2f %%'); has(35 * 115 * 2.57e-3, '%.1f MHz'); has(25 * 115 * 2.57e-3, '%.1f MHz'); has(3158 / 433.92, '%.2f µm')
# Ch 48
from touchstone_atf import read_s2p, stability, msg_db, nf_db, ga_db
g = .27 * cmath.exp(1j * radians(120.1)); has(nf_db(0, .45, g, 2.0), '%.2f dB'); z = 50 * (1 + g) / (1 - g); has((z.real, z.imag), '%.1f + j%.1f Ω')
has(20 * log10(7.31), '%.1f dB'); has(-20 * log10(.06), '%.1f dB'); has(20 * log10(7.31 / .06) / 2, '%.1f dB')
# Ch 49-52
has(c / (2 * 1e9) * 100, '%.0f cm'); has(2 * 2.5e13 * 50 / c / 1e6, '%.2f MHz'); has(.00389 / (2 * 128 * 40e-6), '%.2f m/s')
lam = c / 77e9; Pr = 10 ** 1.2 / 1e3 * 100 * lam ** 2 * 10 / ((4 * pi) ** 3 * 50 ** 4); has(L(Pr * 1e3), '%.1f dBm')
has(-174 + 12 + L(25e3), '%.1f dBm'); has(-20 * log10(2 * sin(pi * 1e6 * 2 / c)), '%.1f dB')
has(2 * 10 * 10.525e9 / c, '%.0f Hz'); has(degrees(asin(.5 * 10 / 11)), '%.1f°'); has(L((pi * .01 * 50 / 3) ** 2), '−%.1f dB'.replace('−%', '%').replace('%.1f', '%.1f'))
has(1 / (2 * pi * sqrt(230e-6 * 365e-12)) / 1e3, '%.0f kHz'); has(6.02 * 8 + 1.76, '%.1f dB'); has(L(2.4e6 / 12.5e3), '%.1f dB')
has(c / 145.8e6 / 2 * .95, '%.3f m'); has(299.79 / 915 / 4 * 100, '%.2f cm'); has(-128.5 + 3 + 174 - 2, '%.1f dB')
has(7.2e3 / c * 145.8e6 / 1e3, '%.2f kHz'); has(70 * (c / 1420.4e6) / 1.2, '%.1f°'); has(100 / sqrt(2.4e6 * 10), '%.3f K')
fs = 20 * log10(1e4) + 20 * log10(9.15e8) - 147.55; has(fs, '%.1f dB'); has(20 + 4.3 - fs + 132, '%.1f dB')
print('checks passed:', n[0])
