# Book 2 Regenerative-Braking Resistor Review

**Date:** 13 October 2026  
**Scope:** Worked Example 24.4 in the current `Circuits_Components_and_Control_Book2.docx`, its Appendix E source list, tagged mirrors, arithmetic, and selected page render.

## Finding and correction

The original solution set the brake-chopper turn-on near 28 V, then sized its resistor at the 30 V ceiling (30^2/95 = 9.5 ohm). That resistor dissipates only 82.5 W at 28 V, below the example's 95 W peak regenerative power. It therefore does not clamp at the stated turn-on; the bus can continue rising toward or beyond the 30 V limit. The 9.5 ohm value also leaves essentially no component-tolerance or control-overshoot margin.

The corrected solution sizes against the actual turn-on threshold: 28^2/95 = 8.25 ohm maximum for immediate absorption of the modeled peak. It gives a 7.5 ohm, +/-5% illustration: at 28 V and the high resistance limit (7.875 ohm), dissipation is 99.6 W; at 30 V and the low resistance limit (7.125 ohm), dissipation can reach 126 W and current 4.21 A. The answer calls for pulse-energy, repetitive average-power, switch voltage/current, drive-specific resistance, and bus-overshoot checks. It explicitly says this is not a brake-resistor design approval.

## Independent calculation

Using the example's motor values (J = 1.0e-4 kg m^2, Kt = Ke = 0.05, R = 1 ohm), 5 A braking current, 480 rad/s start speed, 24 V bus, and 470 uF capacitor:

- Initial kinetic energy: 0.5 J omega^2 = 11.52 J.
- Deceleration: Kt I/J = 2500 rad/s^2; stop time = 0.192 s.
- Winding loss over the stop: I^2 R t = 4.80 J; net energy added to the bus = 6.72 J.
- Unprotected bus voltage = sqrt(24^2 + 2(6.72)/470 uF) = 170.8 V. Capacitance alone for a 30 V ceiling = 41.48 mF.
- Peak regenerative power = I(Ke omega - I R) = 5(24 - 5) = 95 W.
- Net bus energy (6.72 J) is not the same as the positive regenerative pulse integral. Under the stated constant-current/constant-deceleration model, bus power is positive until speed reaches I R/Ke = 100 rad/s, about 0.152 s into the stop; its positive integral is 7.22 J. The final 0.5 J of winding loss is supplied from the bus.

## Source and limits

Rockwell Automation's [PowerFlex Dynamic Brake Resistor Calculator, PFLEX-AT001M-EN-P (2022)](https://literature.rockwellautomation.com/idc/groups/literature/documents/at/pflex-at001_-en-p.pdf) separately checks peak and average regenerative power and uses drive-family resistance, pulse, and thermal limits. It is cited as a vendor-specific reference, not a universal brake-chopper design standard. The example still needs the selected drive's manual, resistor transient-energy data, braking repetition rate, switch ratings, and measured bus overshoot before it could guide a real build.

## Verification

Updated the authoritative Book 2 DOCX solution and Appendix E citation, regenerated `chapters/Book2`, passed DOCX schema validation, and visually inspected the 183-page LibreOffice PDF on page 126. The revised solution and adjacent section remain legible on the same page. This is one worked example and selected-page evidence, not a complete Book 2 fact-read, hardware test, or full Kindle visual review. No score increase is claimed.

Book 2 final reader-file conversion follow-up (13 Oct 2026): after the Chapter 24 brake-chopper correction, Book 2 passed DOCX validation, its 90 extracted files matched the mirror byte-for-byte, and page 126 was visually inspected. The subsequent final all-nine current-master Kindle batch also reports Book 2 Success with zero errors/issues. The KPF quality report is not a visual review or a validated brake-chopper build; external drive/resistor validation remains open.
