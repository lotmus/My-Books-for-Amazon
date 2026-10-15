# -*- coding: utf-8 -*-
"""Book 3 pass 2, part 3: solutions for the new problems, Appendix A/D/E additions, Appendix B intro, link rules."""
S2 = {}
S2[7] = {
6: "Idea: the valence-band step adds to the barrier that holes must climb, so the back-injected hole current falls by the Boltzmann factor. Factor = exp(ΔEv/kT) = exp(0.15/0.026) = exp(5.77) = 320. Check: Worked Example 7.3's 0.20 eV gave 2,190, and every 0.06 eV changes the factor by about ten, so 0.15 eV giving a few hundred is consistent. The usual mistake is to use the whole bandgap difference; only the valence-band part of the step blocks holes.",
7: "Idea: conduction loss is I²R with the resistance that applies while the switch conducts. DC value: 10² × 0.070 = 7.0 W. Dynamic value: R = 1.3 × 70 = 91 mΩ, so 10² × 0.091 = 9.1 W, 2.1 W more. Check: 30 % more resistance gives 30 % more loss at the same current. The usual mistake is to size the heat sink with the DC data sheet value, which a hard-switched GaN stage never sees right after turn-off.",
}
S2[17] = {
9: "Idea: every 0.1 V lower multiplies the life by ten, while the area and failure-fraction factors of Worked Example 17.6 stay the same. From 1.8 V, where 0.01 % fail after 2.15 h, to 1.5 V is 0.3 V, a factor of 10³: 2.15 h × 1000 = 2,150 h, about three months. Check: still far short of ten years, consistent with the 1.34 V limit of the worked example. The usual mistake is to quote the test capacitor's 63 % life, 10⁸ h at 1.5 V, as if it applied to a whole chip.",
10: "Idea: power-law aging scales as (t2/t1)^n. ΔVth = 8 mV × (10,000/100)^0.5 = 8 × 10 = 80 mV. Check: an exponent of 0.5 means every factor of 100 in time multiplies the shift by ten. The usual mistake is to scale linearly, which would give 800 mV, an impossible shift for a working transistor.",
}
S2[21] = {
9: "Idea: the electrode period of a SAW transducer is one acoustic wavelength. λ = v/f = 3,158/(433.92×10⁶) = 7.28 µm, so the fingers are about 1.82 µm wide. Check: features this large are easy to print, one reason quartz SAW resonators for 433 MHz remote controls cost so little. The usual mistake is to apply the BAW rule f = v/(2t), which describes a thickness, not an electrode period.",
10: "Idea: compare the needed fractional bandwidth with each material's resonance spacing, (4/π²) k². Needed: 100/5,000 = 2.0 %. AlN gives 2.6 %, too little once temperature drift and a ladder's narrower usable passband are counted. AlScN at 13 % gives 5.3 %, ample, and a thin-film lithium niobate XBAR offers more. SAW is ruled out at 5 GHz by sub-quarter-micrometer fingers and limited power handling. Choose an AlScN BAW, or an XBAR if the band grows. Check: Worked Example 21.3 reached the same verdict at 3.5 GHz.",
}
S2[23] = {
1: "Idea: invert the diode law. V = N VT ln(I/Is) = 1.8 × 0.026 × ln(10⁻³/3×10⁻⁹) = 0.0468 × 12.72 = 0.595 V. Check: a large N spreads the exponential, and a large Is lowers the curve, so this diode reaches 1 mA below the roughly 0.65 V of a near-ideal small-signal diode. The usual mistake is to use log10 instead of ln.",
2: "Idea: two points on the straight part of the log curve give the slope and the intercept. N = ΔV/(VT ln(I2/I1)) = 0.07/(0.026 × 2.303) = 1.17. Is = I1 exp(−V1/(N VT)) = 10⁻⁴ × exp(−0.55/(1.17 × 0.026)) = 10⁻⁴ × exp(−18.10) = 1.39×10⁻¹² A. Check: the second point, 1.39×10⁻¹² × exp(0.62/0.0304) = 1.0 mA, is reproduced. The usual mistake is to fit Is first with N = 1, which forces the wrong slope.",
3: "Idea: the residual at high current is what Rs absorbs in a level 1 card. Matching 0.95 V needs 0.15 V across Rs at 200 mA, so Rs = 0.15/0.2 = 0.75 Ω, which moves the 10 mA point by only 2.5 mV. Raising Rs can still be the wrong fix: the extra drop may come from high injection, which a level 1 card cannot represent and which bends the curve differently at other currents, or from fixture and lead resistance in a measurement made without Kelvin connections, in which case the part itself is better than the bench suggests. Check the fixture first, then decide whether the card needs a high-injection term. The usual mistake is to tune Rs until one point fits and declare the model validated.",
4: "Idea: the stored charge Tt × IF drains through the reverse current, with the storage time from Chapter 6. ts ≈ Tt ln(1 + IF/IR) = 20 ns × ln(1 + 10/20) = 20 × 0.405 = 8.1 ns. Check: a stronger reverse current shortens it; Worked Example 23.1's 60 mA gave 3.1 ns. The usual mistake is to take Tt itself as the recovery time.",
5: "Idea: least squares minimizes the residual over the parameters it is allowed to change, so a model with one more free parameter can always do at least as well as before, because setting the new parameter to its old value reproduces the old fit. A smaller in-range residual is therefore guaranteed, not earned. The model is better only if it predicts points the fit did not use, which is why validation data are kept separate. Section 23.4's free Rs of −5.8 kΩ shows the failure: a lower residual and a nonsensical parameter. The usual mistake is to report the in-range residual as the model's accuracy.",
6: "Idea: evaluate the card outside its fitted range and compare. V = N VT ln(I/Is) = 1.10 × 0.026 × ln(10⁻⁶/0.47×10⁻¹²) = 0.0286 × 14.57 = 0.416 V. The device has 0.387 V, so the card is 29 mV high at 1 µA, or about three times too little current at that voltage. Do not trust it there: 1 µA is three decades below the 1 mA bottom of its fitted range. The usual mistake is to assume an exponential fitted over two decades extends to all currents.",
}
S2[24] = {
1: "Idea: Tf is the minimum transit delay, so fT cannot exceed 1/(2π Tf). fT ≤ 1/(2π × 400×10⁻¹²) = 398 MHz. Check: the junction capacitances charged through 1/gm add delay and lower the real fT further, most at low current. The usual mistake is to take 1/Tf, forgetting the 2π.",
2: "Idea: in saturation gm = √(2 K ID), so K = gm²/(2 ID). K = 0.1²/(2 × 0.05) = 0.1 A/V². Check: ID = (K/2) Vov² gives Vov = √(2 × 0.05/0.1) = 1.0 V, and gm = K Vov = 0.1 A/V, as stated. The usual mistake is to use gm = K Vov without first finding Vov.",
3: "Idea: the data sheet threshold is the gate voltage at which the stated current flows, so Vto lies below it by the overdrive needed for that current. Vov = √(2 × 250×10⁻⁶/0.1) = 0.071 V, so Vto = 1.8 − 0.071 = 1.73 V. Check: (0.1/2) × 0.071² = 250 µA. The usual mistake is to set Vto equal to VGS(th).",
4: "Idea: on the Miller plateau the gate current goes entirely into Qgd, so the transition time is charge over current. t = 30 nC/1.5 A = 20 ns. Check: a driver of 0.75 A would double it to 40 ns and double the switching loss. The usual mistake is to use Qg, which includes the charge before and after the plateau.",
5: "Idea: add the Foster terms at t = 10 ms. Zth = 0.4 × (1 − e^(−20)) + 1.2 × (1 − e^(−1)) = 0.400 + 1.2 × 0.632 = 1.159 K/W, so ΔTj = 30 × 1.159 = 34.8 K. Check: the fast term is fully charged and the slow one 63 % charged, so Zth lies between 0.4 and 1.6 K/W. The usual mistake is to use the steady 1.6 K/W, which gives 48 K and an over-designed heat sink.",
6: "Idea: IDSS fixes Beta through ID = Beta (VGS − Vto)². Beta = 0.010/2.5² = 1.6 mA/V². At VGS = −1 V, ID = 1.6×10⁻³ × (−1 + 2.5)² = 1.6×10⁻³ × 2.25 = 3.6 mA. Check: at VGS = 0 the formula returns 10 mA, the stated IDSS. The usual mistake is to drop the sign of Vto and compute (−1 − 2.5)².",
}
S2[25] = {
1: "Idea: BFOM ∝ εr μ Ec³, divided by silicon's 442. AlN: 9.8 × 426 × 15.4³ = 9.8 × 426 × 3,652 = 1.52×10⁷, so 1.52×10⁷/442 = 34,500 times silicon. Check: Figure 25.1 shows about 34,500, second only to diamond. The usual mistake is to forget that Ec is cubed.",
2: "Idea: JFOM ∝ Ec vsat. Diamond: 10 × 2.3 = 23; silicon: 0.3 × 1.0 = 0.3; ratio 77. Check: Figure 25.1 shows about 77. The usual mistake is to use the mobility, which does not appear in the Johnson figure.",
3: "Idea: scale the critical field with the square of the gap. Ec(GaN) ≈ 0.3 × (3.4/1.12)² = 0.3 × 9.22 = 2.8 MV/cm, about 16 % below the 3.3 MV/cm used in this book. Check: the square law is a trend across materials, good to tens of percent, not a formula for any one crystal. The usual mistake is to use it in place of a measured value.",
4: "Idea: Ron,sp = 4 BV²/(εs μ Ec³) from Section 19.1. Ron,sp = 4 × 600²/(10.4 × 8.854×10⁻¹⁴ × 1000 × (3.3×10⁶)³) = 4.35×10⁻⁵ Ω·cm² = 0.044 mΩ·cm². Check: a quarter of the 0.17 mΩ·cm² at 1200 V, as the square law requires. The usual mistake is to leave Ec in MV/cm while ε is in F/cm.",
5: "Idea: a pn junction needs both carrier types. Ga2O3 has no usable p-type doping, so there is no pn junction, no inversion-channel MOSFET body, and no bipolar device; designers use Schottky barriers, depletion-mode and fin transistors, or junctions with other p-type materials. Even a Schottky diode is limited by heat: with 11 to 27 W/m·K, a tenth of SiC's conductivity, the junction temperature rises quickly at high current density, so the die must be thinned, cooled from the top, or bonded to a better conductor. The usual mistake is to read the Baliga figure as a forecast of real device performance.",
6: "Idea: the off-state stack must hold the peak swing with margin, at 2.5 V per transistor. Required: 15 × 1.2 = 18 V, so 18/2.5 = 7.2, rounded up to 8 transistors. Check: 8 × 2.5 = 20 V, which covers 18 V. The usual mistake is to round 7.2 down, which leaves the stack below the required margin.",
}
S2[26] = {
1: "Idea: λ (µm) ≈ 1.24/Eg. λ = 1.24/1.9 = 0.653 µm, red light. Check: AlGaInP red LEDs have gaps near 1.9 to 2.0 eV. The usual mistake is to use 1240 with micrometers, which gives 653 µm.",
2: "Idea: above threshold P = η (I − Ith). I − Ith = 5 mW/0.3 W/A = 16.7 mA, so I = 12 + 16.7 = 28.7 mA. Check: an edge-emitting laser of this kind runs at tens of milliamperes, unlike the sub-milliampere threshold of a VCSEL. The usual mistake is to forget the threshold current.",
3: "Idea: light goes out and back. t = 2d/c = 2 × 15/3×10⁸ = 100 ns. Check: 6.67 ns per meter × 15 m = 100 ns. The usual mistake is to use the one-way distance.",
4: "Idea: McIntyre's formula. F = 0.02 × 20 + 0.98 × (2 − 1/20) = 0.40 + 0.98 × 1.95 = 2.31. Check: doubling M from 10 raised F only from 2.06 to 2.31 for silicon. The usual mistake is to forget the (1 − k) factor.",
5: "Idea: dynamic range = full well/read noise; peak SNR = √(full well). DR = 10,000/1.5 = 6,667, 20 log10(6,667) = 76.5 dB. Peak SNR = √10,000 = 100, or 40 dB. Check: dynamic range and peak SNR are different quantities; the first depends on read noise, the second only on the full well. The usual mistake is to quote dynamic range as the image quality.",
6: "Idea: conversion gain = q/C. 1.602×10⁻¹⁹/2×10⁻¹⁵ = 80 µV per electron. Check: half of the 160 µV/e for 1 fF. The usual mistake is to forget that a larger capacitance lowers the gain while raising the charge the node can hold.",
}
S2[27] = {
1: "Idea: x = a/ω0². x = 9.81/(2π × 2000)² = 9.81/1.58×10⁸ = 62 nm per g. Check: a resonance 2.5 times lower than Worked Example 27.1 gives 6.25 times the motion, 6.25 × 9.94 nm = 62 nm. The usual mistake is to use f instead of ω.",
2: "Idea: the thermomechanical noise scales as 1/√m. Four times the mass halves it: 5.1×10⁻⁴/2 = 2.55×10⁻⁴ m/s² per √Hz, about 26 µg/√Hz. Check: by direct substitution, √(4 × 1.38×10⁻²³ × 300 × 31,416/8×10⁻⁹) = 2.55×10⁻⁴. The usual mistake is to scale linearly with mass.",
3: "Idea: Coriolis acceleration is linear in Ω. At 100 °/s, Ω = 1.745 rad/s, and a = 2 × 1.745 × 1.257 = 4.39 m/s², about 0.45 g. Check: one hundred times Worked Example 27.2's 0.044 m/s². The usual mistake is to leave Ω in degrees per second.",
4: "Idea: VH = S × I × B. VH = 100 × 2×10⁻³ × 0.05 = 10 mV. Check: high-sensitivity plates use low-density, high-mobility InSb or GaAs. The usual mistake is to leave the field in millitesla.",
5: "Idea: the splitting is 2γB. B = 5.6×10⁶/(2 × 28×10⁹) = 1.0×10⁻⁴ T = 100 µT. Check: half the splitting of Worked Example 27.4 gives half its 200 µT. The usual mistake is to forget the factor of 2 between the two lines.",
6: "Idea: by Beer-Lambert, transmission at three times the concentration is the single transmission cubed. T = 0.9³ = 0.729, or 72.9 %. Check: exp(−3αcL) = (exp(−αcL))³. The usual mistake is to subtract three times 10 %, giving 70 %.",
}
S2[28] = {
1: "Idea: break-even = ΔNRE/Δ(unit cost). (2.5 − 0.5) million/(12 − 4) = 2,000,000/8 = 250,000 units. Check: at 250,000 units both cost 14 dollars per unit including NRE. The usual mistake is to divide by the sum of the unit costs.",
2: "Idea: NRE/N + unit cost at N = 100,000. FPGA: 2 + 25 = 27 dollars. Mature ASIC: 30 + 2 = 32 dollars. Advanced ASIC: 400 + 1.50 = 401.50 dollars. Check: 100,000 units lies below the 122,000-unit break-even, so the FPGA should still win, and it does. The usual mistake is to compare unit costs alone.",
3: "Idea: the respin adds to the ASIC's NRE and moves the break-even up. New NRE = 4.5 million; break-even = (4.5 − 0.2) million/(25 − 2) = 187,000 units. Check: 50 % more NRE moved the break-even about 54 % higher, because the FPGA's own NRE is subtracted. The usual mistake is to forget the respin entirely when planning, which is why the From the Bench note asks for margin.",
4: "Idea: analog and RF performance do not scale like logic. Analog precision, high-voltage devices, and low leakage are often better or cheaper in mature nodes, which offer thicker oxides and higher supply voltages; the NRE and mask cost are far lower; and the logic content of an analog chip is too small for an advanced node's density to pay. Any two of these answer the question.",
5: "Idea: the front end of the design flow is shared. The same hardware description and simulation produce an FPGA bitstream in hours, so the design can be tested in real time, with real interfaces and real software, before anyone pays for masks. An error found on the FPGA costs a rebuild; an error found in silicon costs a respin. The usual mistake is to assume FPGA timing and power will carry over to the ASIC unchanged; they do not.",
6: "Idea: total cost, not area, decides. The FPGA's twenty-fold area raises its unit cost, but it carries almost no NRE, no mask set, and no fab delay, and it can be changed after shipment. At low volume the NRE divided by the number of units dominates the ASIC's cost, so the FPGA is cheaper overall, as Worked Example 28.1 showed below about 122,000 units. The usual mistake is to compare silicon area or unit price alone.",
}
APPB_INTRO = "Every practice problem is worked in full below: the idea, the numbers, and a check or the usual mistake. Where a problem continues a worked example, the solution uses that example's declared values."
APPA = [
"Representative material constants for Part IX (gap, critical field, electron mobility, relative permittivity, saturation velocity, thermal conductivity): listed in Section 25.1. Orientation values, not design values.",
"SPICE nominal temperature TNOM: 27 °C by default, where VT = 25.85 mV. Hand work in this book keeps VT = 26 mV.",
"Teaching diode of Section 23.4: Is = 50 fA with N = 1, recombination current 0.5 nA with N = 2, high-injection knee 20 mA, Rs = 0.5 Ω.",
"Time of flight: 6.67 ns of round trip per meter of range, 66.7 ps per centimeter.",
"APD excess noise: F(M) = kM + (1 − k)(2 − 1/M); k ≈ 0.02 for silicon, 0.4 to 0.5 for InGaAs/InP, 0.9 for germanium.",
"Floating-diffusion conversion gain q/C: 160 µV per electron for 1 fF.",
"NV center in diamond: zero-field splitting 2.87 GHz; 28 GHz/T, or 28 kHz/µT, per resonance line.",
]
APPD = [
('Part VIII: From Datasheet to Model', 'Massobrio and Antognetti, Semiconductor Device Modeling with SPICE; the ngspice User\'s Manual; Box, "Science and Statistics" (Journal of the American Statistical Association, 1976), and "Robustness in the Strategy of Scientific Model Building" (in Launer and Wilkinson, editors, Robustness in Statistics, 1979); the onsemi data sheets for the 1N4148, 2N3904, and 2N7000; the Infineon data sheet for the IRFZ44N; manufacturer data sheets for the J310.'),
('Part IX: Materials, Light, Sensing, and the Chip', 'Tsao et al., "Ultrawide-Bandgap Semiconductors: Research Opportunities and Challenges" (Advanced Electronic Materials, 2018); Woo et al., "From Wide to Ultrawide-Bandgap Semiconductors for High Power and High Frequency Electronic Devices" (Journal of Physics: Materials, 2024); Coldren, Corzine, and Mašanović, Diode Lasers and Photonic Integrated Circuits; McIntyre, "Multiplication Noise in Uniform Avalanche Diodes" (IEEE Transactions on Electron Devices, 1966); Ohta, Smart CMOS Image Sensors and Applications; Gallego et al., "Event-Based Vision: A Survey" (IEEE Transactions on Pattern Analysis and Machine Intelligence, 2022); Shockley and Queisser, "Detailed Balance Limit of Efficiency of p-n Junction Solar Cells" (Journal of Applied Physics, 1961); Kaajakari, Practical MEMS; Popović, Hall Effect Devices; Schirhagl et al., "Nitrogen-Vacancy Centers in Diamond: Nanoscale Sensors for Physics and Biology" (Annual Review of Physical Chemistry, 2014); Weste and Harris (Part V) for the ASIC flow; the Tiny Tapeout project pages.'),
]
APPE_TITLE = 'Appendix E. Datasheet-to-SPICE Parameter Lists'
APPE_INTRO = "Each list names a model parameter and the data sheet line or measurement it comes from, for the devices of Chapters 23 and 24. Fitted values are valid over the range they were fitted in; record that range with the card."
APPE = [
('Diode (SPICE level 1)', [
 "Is, saturation current: from the straight part of the forward curve on a log axis, fitted together with N.",
 "N, emission coefficient: from the slope of that straight part, N = ΔV/(VT ln(I2/I1)).",
 "Rs, series resistance: from the bend of the forward curve at high current.",
 "Cjo, Vj, M: from the capacitance curve against reverse voltage; Cjo is the zero-bias value, often quoted as CT at 0 V and 1 MHz.",
 "Fc: where the forward-bias capacitance switches to a linear extrapolation; leave at 0.5.",
 "Tt, transit time: from trr in its stated test circuit, through ts ≈ Tt ln(1 + IF/IR).",
 "BV and Ibv: the breakdown voltage and the current that defines it, from the reverse curve or the Zener voltage specification.",
 "Eg and Xti: temperature scaling of Is, from forward curves at two temperatures; 1.11 eV for silicon junctions, the barrier height for Schottky diodes.",
 "Kf and Af: flicker-noise coefficient and exponent; rarely on a data sheet, zero unless measured."]),
('Bipolar transistor (Gummel-Poon)', [
 "Is, Bf, Nf: the collector current and the gain ceiling, from the Gummel plot.",
 "Ise, Ne: the non-ideal base current that lowers hFE at small IC.",
 "Ikf: the high-injection knee that lowers hFE at large IC.",
 "Vaf (and Var): the Early voltage, from the slope of the output curves.",
 "Br, Isc, Nc, Ikr: reverse-mode parameters; VCE(sat) checks them.",
 "Rb, Re, Rc: ohmic resistances, from VCE(sat) and VBE(sat) at high current.",
 "Cje, Vje, Mje and Cjc, Vjc, Mjc: junction capacitances, from Cibo and Cobo against voltage.",
 "Tf, Itf, Vtf, Xtf: forward transit time and its growth at high current, from fT against IC.",
 "Tr: reverse transit time, from the storage time in the switching test.",
 "Xtb, Xti, Eg: temperature scaling of β and Is."]),
('MOSFET (level 1 and the power subcircuit)', [
 "Vto: the square-law threshold; not the data sheet VGS(th), which is a gate voltage at a stated drain current.",
 "Kp with W and L: from gfs at its test current, K = gfs²/(2 ID).",
 "Lambda: from the slope of the output curves in saturation.",
 "Gamma and Phi: body effect; irrelevant for a discrete part with source tied to body.",
 "Rd and Rs: series resistances that close the gap to the measured RDS(on).",
 "Cgd, Cgs, Cds in a subcircuit: Cgd = Crss, Cgs = Ciss − Crss, Cds = Coss − Crss, each against VDS.",
 "Qgs, Qgd, Qg: checks on the capacitances, from the gate-charge curve.",
 "Body diode: a diode card fitted to the source-drain diode curve, trr, and Qrr.",
 "Thermal behavior: a Foster or Cauer network from Zth(t), and a temperature coefficient for RDS(on) from its curve against TJ.",
 "Safe operating area: not in the model; check against the data sheet curve."]),
('JFET', [
 "Vto: from VGS(off), the pinch-off voltage.",
 "Beta: IDSS/Vto².",
 "Lambda: from the slope of the output curves.",
 "Cgs, Cgd, Pb: from the capacitance data.",
 "Is: gate-junction leakage, from IGSS."]),
('Zener, LED, and Schottky diodes', [
 "Zener: BV and Ibv from VZ at IZT, the breakdown slope from rz, and a temperature coefficient from the Zener voltage drift.",
 "LED: Is and N from the forward curve, N often 2 or more; light output from a behavioral source proportional to current.",
 "Schottky: a large Is, N near 1.0 to 1.1, Tt near zero, and Eg set to the barrier height so that leakage rises correctly with temperature."]),
('Temperature, corners, and other devices', [
 "TNOM: the temperature at which the card was fitted, 27 °C by default.",
 "Foster network: Ri and τi pairs fitted to Zth(t); not extendable with a heat sink.",
 "Cauer network: a ladder whose nodes map to physical layers; extendable with a heat sink.",
 "Corners and Monte Carlo: corner cards built from the data sheet limits, or spreads measured on a batch of parts.",
 "Op-amps and comparators: macromodels, in Book 2, Circuits, Components, and Control, Sections 15.7, 15.8, and 16.8."]),
]
OL = 'https://openlibrary.org/search?q='; CR = 'https://search.crossref.org/?q='
def _q(s): import urllib.parse; return urllib.parse.quote_plus(s)
LINKS = [
('Semiconductor Device Modeling with SPICE', OL + _q('Semiconductor Device Modeling with SPICE Massobrio'), 'Massobrio and Antognetti'),
("ngspice User's Manual", 'https://ngspice.sourceforge.io/docs.html', 'Massobrio and Antognetti'),
('Science and Statistics', CR + _q('Science and Statistics Box 1976'), 'Massobrio and Antognetti'),
('Robustness in the Strategy of Scientific Model Building', CR + _q('Robustness in the Strategy of Scientific Model Building'), 'Massobrio and Antognetti'),
('Ultrawide-Bandgap Semiconductors: Research Opportunities and Challenges', CR + _q('Ultrawide-Bandgap Semiconductors: Research Opportunities and Challenges'), 'Tsao et al.'),
('From Wide to Ultrawide-Bandgap Semiconductors for High Power and High Frequency Electronic Devices', CR + _q('From wide to ultrawide-bandgap semiconductors for high power and high frequency electronic devices'), 'Tsao et al.'),
('Diode Lasers and Photonic Integrated Circuits', OL + _q('Diode Lasers and Photonic Integrated Circuits Coldren'), 'Tsao et al.'),
('Multiplication Noise in Uniform Avalanche Diodes', CR + _q('Multiplication Noise in Uniform Avalanche Diodes'), 'Tsao et al.'),
('Smart CMOS Image Sensors and Applications', OL + _q('Smart CMOS Image Sensors and Applications Ohta'), 'Tsao et al.'),
('Event-Based Vision: A Survey', CR + _q('Event-Based Vision: A Survey'), 'Tsao et al.'),
('Detailed Balance Limit of Efficiency of p-n Junction Solar Cells', CR + _q('Detailed Balance Limit of Efficiency of p-n Junction Solar Cells'), 'Tsao et al.'),
('Practical MEMS', OL + _q('Practical MEMS Kaajakari'), 'Tsao et al.'),
('Hall Effect Devices', OL + _q('Hall Effect Devices Popovic'), 'Tsao et al.'),
('Nitrogen-Vacancy Centers in Diamond: Nanoscale Sensors for Physics and Biology', CR + _q('Nitrogen-Vacancy Centers in Diamond: Nanoscale Sensors for Physics and Biology'), 'Tsao et al.'),
('Tiny Tapeout project pages', 'https://tinytapeout.com', 'Tsao et al.'),
('5 GHz Laterally-Excited Bulk-Wave Resonators (XBARs) Based on Thin Platelets of Lithium Niobate', CR + _q('5 GHz laterally-excited bulk-wave resonators (XBARs) based on thin platelets of lithium niobate'), 'Plummer, Deal, and Griffin'),
]
