# -*- coding: utf-8 -*-
OPS = [
# ---- ch24 nuclei
('sub', 1035, "The mass is small. It is not zero.", "The mass is small but real."),
('sub', 992, "The energy release is approximately 200 MeV per fission of uranium-235 or plutonium-239.", "Each fission of uranium-235 or plutonium-239 releases roughly 200 MeV, tens of millions of times the energy of a chemical bond."),
# ---- ch25 neutrinos
('delsec', 1566),
('sub', 2078, " Direct evidence for the heavy right-handed states is absent.", ""),
# ---- ch26 quantum world
('delsec', 1852),
('sub', 318, "Magnetic flux through a superconducting ring is quantized in units of \\( h/2e \\). The quantization is observed.", "Magnetic flux through a superconducting ring is quantized in units of \\( h/2e \\), the factor of 2 reflecting that the carriers are pairs. The quantization is observed."),
('replace', 2024, [
 "The Hong–Ou–Mandel effect is the interference of two identical photons at a beam splitter. When the photons arrive simultaneously they exit together in the same output port. The coincidence rate drops to zero. The dip is a direct signature of bosonic exchange symmetry. It is used to characterise single-photon sources and to implement linear-optical quantum gates.",
 "Light comes in kinds that differ in their photon statistics. A coherent state from a laser has Poissonian photon counts. A single-photon Fock state has exactly one photon. Squeezed vacuum emits photons in correlated pairs. Photon counting and homodyne detection tell them apart, and each kind has its use, from quantum cryptography to the quantum-noise reduction in gravitational-wave detectors mentioned above.",
]),
# ---- ch27 measurement
('sub', 2315, "The Schrödinger equation is linear and deterministic. It does not by itself select one outcome.", "The Schrödinger equation is linear and deterministic, so it never picks a single result on its own."),
('sub', 581, "Interference between macroscopically distinct positions becomes unobservable.", "Interference between macroscopically distinct positions becomes unobservable. The basis in which interference disappears, the pointer basis, is selected by the form of the interaction, and for macroscopic objects it is approximately the position basis. The resulting diagonal density matrix looks like ignorance about which outcome occurred, but it is an improper mixture, not a definite result."),
('delsec', 2318),
('set', 2342, "The quantum-to-classical transition is", "The quantum-to-classical transition is the emergence of classical behaviour from quantum mechanics. Treating the decohered state as a classical mixture is adequate for prediction and incomplete for ontology."),
('replace', 2321, [
 "As an answer to the measurement problem, many-worlds says that nothing needs answering. The universal wave function never collapses; apparent collapse is the branching of the wave function into components that no longer interfere, and observers are branched along with everything else.",
 "The full account, with its difficulty over the origin of probabilities, appears in the discussion of the multiverse. What matters here is the comparison with the other options. This interpretation adds no postulates and no new dynamics, it is not experimentally distinguishable from collapse models in which the collapse is irreversible and the branches do not interfere, and its price is ontological: the reality of every unobserved branch.",
]),
# ---- ch28 Bell
('delsec', 2345),
('sub', 1208, "It shows only that the correlations are stronger than those permitted by local pre-existing values.", "It shows only that the correlations are stronger than those permitted by local pre-existing values, and it excludes the completions that satisfy its assumptions, not every conceivable completion."),
('sub', 1614, "Bell inequalities bound the correlations permitted by local hidden-variable theories. Quantum mechanics exceeds those bounds. Experiments with photons, atoms and superconducting circuits have violated the inequalities under conditions that close the principal loopholes. The violations demonstrate that nature does not admit a local realist description of the sort assumed by the inequalities.", "Bell inequalities bound the correlations permitted by local hidden-variable theories, and quantum mechanics exceeds those bounds, as the experiments described above show."),
('sub', 1198, "The result violates the Bell inequality that any local hidden-variable theory must satisfy.", "Combined at suitable angles, correlations of this form violate the Bell inequality that any local hidden-variable theory must satisfy."),
]
