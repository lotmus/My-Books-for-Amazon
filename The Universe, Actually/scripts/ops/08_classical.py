# -*- coding: utf-8 -*-
OPS = [
# ---- ch18 motion
('sub', 641, " In the path-integral formulation of quantum mechanics the same action appears in the phase of each path. The classical path is the one about which the phase varies least; neighboring paths interfere constructively. The principle is therefore the classical limit of the quantum sum over histories.", ""),
('sub', 685, "The principle remains valid in relativity and in quantum mechanics. In the latter the action appears as the phase of each path in the path integral. The classical path is recovered as the path of stationary phase. Everyday motion", "Everyday motion"),
('delsec', 1958),
('sub', 671, "The conservation laws follow from symmetries of the underlying action. Time-translation invariance yields energy conservation. Spatial-translation invariance yields momentum conservation. Rotational invariance yields angular-momentum conservation. The connection is Noether’s theorem.", "The conservation laws follow from symmetries of the underlying action, as Noether’s theorem shows."),
('sub', 2974, "The cosmic microwave background is uniform to one part in \\( 10^{5} \\).", "Across the whole sky the microwave background varies by only about one part in \\( 10^{5} \\)."),
# ---- ch19 heat
('set', 698, "The first law of thermodynamics states", "In quantitative form the first law says that the change in internal energy of a system equals the heat added minus the work done by the system. Taken together with the second law, it forbids perpetual-motion machines of both the first and the second kind."),
('replace', 1946, [
 "Example. One mole of a monatomic ideal gas is heated at constant volume from 300 K to 400 K. How much heat is absorbed, and how much work is done?",
 "No work is done at constant volume, so \\( Q = \\Delta U = \\frac{3}{2}R\\,\\Delta T = 1.5 \\times 8.314 \\times 100 \\approx 1\\,250 \\) J.",
 "Example. A Carnot engine operates between 400 K and 300 K. Find its efficiency and the work produced per kilojoule of heat absorbed from the hot reservoir.",
 "\\( \\eta = 1 - T_C/T_H = 0.25 \\). Work = 250 J per kilojoule absorbed.",
 "The results follow directly from the first law and from the definition of the Carnot efficiency. They are the upper bounds realised by no real engine.",
]),
('delsec', 1610),
('replace', 2015, [
 "A chaotic system has at least one positive Lyapunov exponent, and the exponents obey a bookkeeping rule: their sum equals the average rate at which phase-space volume contracts. In a dissipative system that sum is negative, so the attractor has zero volume and a non-integer dimension.",
 "Chaos needs nonlinearity and, for continuous-time systems, at least three dynamical degrees of freedom. It appears in low-dimensional systems such as the logistic map at parameter value 4, the Lorenz equations, double pendulums and driven oscillators, and also in high-dimensional ones such as turbulence, climate and neural networks. The limit on prediction is practical, not fundamental. Statistical properties such as invariant measures and correlation functions remain well defined, and forecasts succeed inside the predictability horizon.",
], "Lyapunov Exponents and Predictability"),
# ---- ch20 waves and light
('sub', 160, "Light is an electromagnetic wave. It does not need a medium.", "Light turns out to be an electromagnetic wave, and it does not need a medium."),
('sub', 160, "The wave and particle descriptions are complementary. Neither is complete alone. Quantum mechanics is the framework that contains both.", "The wave and particle pictures live together in the single framework of quantum mechanics."),
]
