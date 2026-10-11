# -*- coding: utf-8 -*-
OPS = [
# ---- ch9
('delsec', 1915),
('delsec', 1921),
('sub', 676, "The equality has been tested to better than one part in \\( 10^{13} \\). Torsion-balance experiments, lunar laser ranging, and satellite measurements all confirm it. In general relativity the equality is elevated to a principle: the local effects of gravity are indistinguishable from the effects of acceleration. The principle is the foundation of the geometric description of gravity.", "The equality has been tested to a few parts in \\( 10^{15} \\) with torsion balances, lunar laser ranging and the MICROSCOPE satellite. General relativity promotes it to a principle, described in the next section."),
('sub', 814, "It remains the conceptual foundation of the geometric theory of gravity.", "It remains the conceptual foundation of the geometric theory of gravity, and it demands that every form of energy gravitate, binding energy included."),
('sub', 828, "the straightest possible path in curved spacetime. The geodesic equation is", "the straightest possible path in curved spacetime, and the path of extremal proper time between two events. The geodesic equation is"),
('sub', 2393, "The Einstein equation relates the curvature to the stress-energy tensor. The equation is non-linear.", "The Einstein equation relates the curvature to the stress-energy tensor, and because gravity carries energy of its own the theory interacts with itself."),
('sub', 2393, "Quantum corrections are expected near the Planck scale. No observational evidence of those corrections exists.", "No observational trace of the quantum corrections it implies has yet been found."),
('sub', 491, "None has been confirmed.", "No candidate has yet been confirmed by experiment."),
# ---- ch10
('sub', 1067, "Without a correction the positioning error would grow by more than 10 km each day. ", "Left alone, the drift would ruin navigation within minutes. "),
('replace', 1091, [
 "Example 1. If the relativistic offset were left uncorrected, how large a ranging error would accumulate in one hour?",
 "38.4 µs per day is 1.6 µs per hour. Light travels \\( 3\\times 10^{8}\\,\\mathrm{m\\,s^{-1}} \\times 1.6\\times 10^{-6}\\,\\mathrm{s} \\approx 480 \\) m in that time, so the position error would grow by nearly half a kilometre every hour.",
 "Example 2. A satellite orbits with eccentricity 0.02. What is the maximum additional relativistic clock correction?",
 "The eccentricity term has amplitude \\( 2\\sqrt{GMa}\\,e/c^2 \\approx 2.3\\times 10^{-6}\\,\\mathrm{s}\\times e \\). For \\( e = 0.02 \\) that is about 46 ns, which corresponds to a range error of roughly 14 m if it is not applied.",
 "Example 3. After 10 years of continuous operation, by how much would an uncorrected satellite clock have drifted relative to ground time?",
 "38.4 µs day\\(^{-1}\\) × 365.25 × 10 ≈ 0.140 s. Corresponding range error ≈ 42 000 km, larger than the GPS constellation itself.",
 "The numerical values are those used in the actual GPS interface specifications. The system would be unusable without them.",
]),
# ---- ch11
('set', 1970, "The first detection, GW150914", "The first detection, GW150914, was a binary black-hole merger roughly 400 megaparsecs away, in which about three solar masses were radiated away as gravitational waves in a fraction of a second. Later events include black-hole pairs far heavier than expected and binary neutron stars. The catalogue now holds many dozens of events, and the masses, spins and local expansion rate are measured from them. The gravitational-wave window is independent of electromagnetic radiation."),
]
