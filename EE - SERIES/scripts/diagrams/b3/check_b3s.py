"""Numeric checks for Book 3 pass 2: recompute every new worked example and solution figure and assert the
rounded value appears in the text it supports. Run after figs_b3s.py (uses its fits and the ngspice outputs)."""
from math import *
import re, figs_b3s as F, content_b3n as N, content_b3c as C, content_b3x as X
VT = 0.026; eps0 = 8.854e-14
TXT = str(N.NEW) + str(C.CH) + str(X.S2)
n = 0
def has(val, fmt, *alts):
    global n
    import numpy as np; val = float(np.asarray(val).ravel()[0]); s = fmt % val
    assert s in TXT or any(a in TXT for a in alts), (s, alts); n += 1
# Ch 7
has(exp(0.20/0.026), '%.0f', '2,190'); has(exp(0.15/0.026), '%.0f')
has((56-3)/8, '%.1f W/mm'); has((56-6)*0.8/8, '%.1f W/mm')
# Ch 17
has(F.t001(1.8), '%.2f', '2.15×10⁻³'); has(F.Vmax10, '%.2f V'); has(F.t001(1.5), '%.0f', '2,150 h')
has(8*sqrt(100), '%.0f mV')
# Ch 21
has(4150/2e9*1e6, '%.2f µm'); has(11350/4e9*1e6, '%.2f µm'); has(3158/433.92e6*1e6, '%.2f µm')
# Ch 23
nvt = 1.752*VT
for I, s in [(5e-3, '0.663 V'), (10e-3, '0.698 V'), (0.1, '0.854 V')]:
    v = nvt*log(I/2.52e-9) + I*0.568; assert abs(v - float(s[:5])) < 0.0006, (I, v); n += 1
has(20*log(1+10/60), '%.1f ns'); has(F.v_at(5e-3), '%.3f'); has(F.v_at(1e-2), '%.3f'); has(F.v_at(0.1), '%.3f')
Nn = 0.08/(VT*log(10)); Is = 1e-4*exp(-0.56/(Nn*VT)); Rs = (0.83 - Nn*VT*log(0.05/Is))/0.05
has(Nn, '%.3f'); has(Rs, '%.2f Ω'); has(Nn*VT*log(1e-2/Is) + 1e-2*Rs, '%.3f V')
NA, IsA, _ = F.pA; NB, IsB, RB = F.pB
has(NA, 'N = %.2f'); has(IsA*1e9, 'Is = %.2f nA'); has(NB, 'N = %.2f'); has(IsB*1e12, 'Is = %.2f pA'); has(RB, 'Rs = %.2f Ω')
assert F.FIT['inA'] < 2.6 and F.FIT['inB'] < 2.6; has(F.FIT['A_at_10mA'], '%.0f mV'); has(F.FIT['B_at_100nA'], '%.0f mV')
has(exp(F.FIT['B_at_100nA']/1e3/(NB*VT)), 'about %.0f'); has(F.FIT['A_free_Rs'][2]/1e3, '%.1f kΩ', '−5.8 kΩ')
has(0.47e-12*exp(0.3/(1.1*VT))*1e9, '%.0f nA'); has(5e-14*exp(0.3/VT)*1e9, '%.1f nA'); has(5e-10*exp(0.3/0.052)*1e9, '%.0f nA')
assert abs(1.8*VT*log(1e-3/3e-9) - 0.595) < 5e-4; assert abs(NB*VT*log(1e-6/IsB) - 0.416) < 1e-3; n += 2
# Ch 24
for I, s in [(1e-4, 96), (1e-3, 133), (1e-2, 160), (5e-2, 130), (1e-1, 100)]: assert abs(F.HFE[I] - s) < 1, (I, F.HFE[I]); n += 1
has(1/(2*pi*301.2e-12)/1e6, '%.0f MHz'); K = 0.32**2/0.4; has(K, '%.3f A/V²'); Vto = 2.1 - sqrt(2e-3/K); has(Vto, '%.2f V')
has(1/(K*(10-Vto)), '%.2f Ω'); has((10-5)/12, '%.2f A'); has(23e-9/((10-5)/12)*1e9, '%.0f ns')
z = 0.4*(1-exp(-2)) + 1.2*(1-exp(-0.1)); has(z, '%.3f K/W'); has(50*z, '%.0f K'); has(150/94, '%.1f K/W')
has(6e-3*1e3, '%.0f mA'); has(0.060/42.25*5.5**2*1e3, '%.0f mA'); has(30*(0.4+1.2*(1-exp(-1))), '%.1f K')
# Ch 25
has(F.BREL['4H-SiC'], '%.0f times'); has(F.BREL['GaN'], '%.0f times'); has(F.RON['GaN'], '%.2f'); has(F.RON['β-Ga$_2$O$_3$'], '%.3f')
has(F.JREL['β-Ga$_2$O$_3$'], '%.0f'); has(F.BREL['AlN'], '%.0f', '34,500'); has(F.JREL['diamond'], '%.0f')
has(F.RON['GaN']/4, '%.3f'); has(0.3*(3.4/1.12)**2, '%.1f MV/cm')
# Ch 26
has(0.5*5.5, '%.2f mW'); has(0.5*0.85/1.24, '%.2f'); has(2.75/12*100, '%.0f %%'); has(0.02*10+0.98*1.9, '%.2f'); has(4.5+0.55*1.9, '%.2f', '5.55')
has(3e8*50e-12/2*1e3, '%.1f mm'); has(7.5/20, '%.2f mm'); has(20*log10(3000), '%.1f dB'); has(20*log10(sqrt(6000)), '%.1f dB')
has(20*log10(100/sqrt(104)), '%.1f dB'); has(20*log10(10000/1.5), '%.1f dB'); has(0.02*20+0.98*1.95, '%.2f')
# Ch 27
w0 = 2*pi*5000; has(9.81/w0**2*1e9, '%.2f×10⁻⁹', '9.94'); nz = sqrt(4*1.38e-23*300*w0/2e-9); has(nz*1e4, '%.1f×10⁻⁴'); has(nz/9.81*1e6, '%.0f µg')
a = 2*pi/180*2*pi*2e4*1e-5; has(a, '%.3f m/s²'); has(11.2e6/(2*28e9)*1e6, '%.0f µT', '2.0×10⁻⁴ T'); has(1/(1e22*1.602e-19*1e-5), '%.1f V/(A·T)')
has(9.81/(2*pi*2000)**2*1e9, '%.0f nm'); has(100*a, '%.2f m/s²')
# Ch 28
has((3e6-0.2e6)/23, '%.0f', '121,700'); has(4.3e6/23, '%.0f', '187,000')
print('check_b3s: %d assertions passed' % n)
