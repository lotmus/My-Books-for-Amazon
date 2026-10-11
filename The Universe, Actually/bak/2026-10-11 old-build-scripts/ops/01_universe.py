# -*- coding: utf-8 -*-
OPS = [
# ---- ch1
('sub', 2409, "They have been travelling ever since. They will continue after you stop reading.", "Their journey does not pause while you turn the page."),
# ---- ch2
('sub', 1050, "The constant of proportionality is the Hubble constant.", "The slope of that straight-line relation is the Hubble constant."),
('sub', 454, "That component is called dark energy. ", "Astronomers call that component dark energy. "),
('replace', 1927, [
 "Solving the Friedmann equations for a single dominant component gives three simple histories. When radiation dominates, the scale factor grows as the square root of time. When matter dominates it grows as time to the power two-thirds. When a cosmological constant dominates, it grows exponentially, with a doubling time set by the Hubble parameter.",
 "The real universe has passed through these regimes in that order. Radiation gave way to matter when the universe was some 50 000 years old, at a redshift near 3 400. Matter gave way to dark energy roughly ten billion years after the Big Bang, at a redshift near 0.3. We live early in the third era, and if the dark energy is a true constant, the exponential phase will last for ever.",
], "Radiation, Matter and Vacuum Eras"),
# ---- ch3
('sub', 1039, "The spectrum is that of a black body. The spectrum is perfect. No other known process", "The spectrum follows the black-body curve with extraordinary fidelity. No other known process"),
('replace', 1273, [
 "The Big Bang is the hot, dense, expanding phase from which the observable universe emerged. It is not an explosion in pre-existing space. It is the expansion of space itself, and every comoving observer sees the same recession of distant galaxies and the same cooling of the radiation field.",
 "Cosmologists divide the story into epochs, each tied to a temperature. Near \\( 10^{15} \\) K, within a trillionth of a second, the electromagnetic and weak forces were still one electroweak force. Within about ten microseconds the universe had cooled enough for quarks to bind into protons and neutrons. Within the first few minutes the light nuclei formed. Some 380 000 years later the first atoms appeared and the universe became transparent. Each transition is calculated within the Standard Model and leaves no relic that contradicts it.",
 "The frontier of the story is the very beginning. Extrapolating the classical equations backward reaches a singularity in finite time, a sign that the equations have been pushed past their domain. Quantum gravity is expected to intervene, and no completed theory yet replaces the singularity with a definite prior state. What is secure is everything from nucleosynthesis onward, confirmed by several independent observations.",
]),
('replace', 1231, [
 "To ask for the origin of the universe is to ask two different questions. One is how the hot, expanding phase began and what set its initial conditions. The other is whether anything came before it, or whether the question even has meaning. Observation reaches only the first, and only partly: the earliest direct evidence is the microwave background, and nothing earlier has been seen in light.",
 "Before nucleosynthesis the energies exceeded those accessible to accelerators. The electroweak transition, the confinement of quarks into hadrons, and any preceding inflationary phase lie in that regime. Inflation, if it occurred, would have stretched a microscopic region to macroscopic size, diluted curvature, and generated the nearly scale-invariant fluctuations later seen in the microwave background. No direct relic of inflation has been detected. The hypothesis remains the simplest account of the initial conditions required by the later evolution.",
 "The expansion itself has no centre and no edge within the observable volume. Run the Friedmann equation backward under the assumptions of classical general relativity and ordinary matter, and it reaches a singularity in finite time. That result marks the limit of the theory more than a moment of creation, and no controlled calculation yet replaces it with an earlier state.",
 "The origin of the low entropy that permits the thermodynamic arrow, the origin of the baryon asymmetry, and the nature of the dark-matter particles are likewise open. They are the questions a complete account of the beginning would have to answer.",
]),
('set', 607, "The same expansion that set the nuclear abundances", "The clock mattered. Free neutrons decay with a mean life of about fifteen minutes, so the neutron fraction was already sinking as the universe cooled toward the temperature at which deuterium could survive. Had the nuclear fires lit much later, less helium would have formed; had the weak interactions frozen out earlier, more. The observed quarter by mass is therefore a direct readout of the expansion rate in the first seconds."),
('sub', 851, "Virtually all remaining neutrons were incorporated into helium-4.", "Nearly every neutron that survived ended up inside a helium-4 nucleus."),
('sub', 1395, "Inflation solves the horizon problem: regions now widely separated were once in causal contact and could equalise their temperatures. It solves the flatness problem: any initial curvature is diluted to an unobservable level. Quantum fluctuations", "Both puzzles described in the previous section dissolve, because the whole observable universe descends from one small patch that was once in causal contact and was then stretched flat. Quantum fluctuations"),
('delsec', 774),
('sub', 2099, "They do not yet identify the microphysical model.", "They do not yet identify the microphysical model, and rival scenarios that mimic the same spectrum can be told apart only by better measurements of non-Gaussianity or of primordial gravitational waves."),
('sub', 1399, "The mechanism operates naturally within the seesaw framework.", "The mechanism fits naturally into the seesaw picture of neutrino mass."),
('sub', 1399, "None has been experimentally confirmed.", "Each remains a hypothesis awaiting experimental support."),
# ---- ch4
('retitle', 1470, "The Dark Sector at a Glance"),
('replace', 1470, [
 "Dark matter and dark energy are the two dominant components of the present universe. Neither emits, absorbs or scatters light, and both are detected solely through their gravitational effects.",
 "Dark matter makes up roughly a quarter of the cosmic energy budget and dark energy roughly two-thirds to seven-tenths. Ordinary atoms, everything that shines or can be built into a star, a planet or a person, supply the remaining five percent. The expansion history and the growth of structure are described accurately once all three are included.",
 "The two differ in character. Dark matter clumps: it gathers into halos, pulls galaxies together and shapes the cosmic web. Dark energy does not clump, and its density hardly changes as space expands. One slowed the expansion while structures formed; the other is speeding it up now. Neither has a known microphysical identity.",
]),
('sub', 464, "Quantum field theory predicts a far larger vacuum energy. The discrepancy is many orders of magnitude. No accepted resolution exists.", "A naive quantum-field-theory estimate of the vacuum energy comes out many orders of magnitude too large, a mismatch examined below."),
('replace', 1407, [
 "A true cosmological constant is only one way to make the universe accelerate. Quintessence replaces it with a slowly rolling scalar field whose energy density can change with time. Modified-gravity models alter the Einstein equation on large scales instead of adding a new substance. Each can be tuned to mimic a constant, which is why the choice is hard to make from the expansion history alone.",
 "The tests are the expansion history and the growth rate of cosmic structure. A pure constant fixes both with no free parameters, so any measured drift in the equation-of-state parameter \\( w \\), or any mismatch between how fast space expands and how fast structure grows, would point beyond it. Recent baryon-acoustic-oscillation maps, combined with supernova and microwave-background data, show a mild preference for dark energy that weakens with time. The significance depends on which supernova sample is used, and it has not been confirmed.",
 "A constant also fixes when acceleration began. Because its density does not dilute, it overtook the falling matter density only recently, and the switch from deceleration to acceleration happened at a redshift near 0.7.",
], "Beyond the Cosmological Constant"),
('replace', 2417, [
 "The cosmological constant is small, and it is not zero. Both halves of that sentence are measured. The explanation of either half is absent: no symmetry forces the value to vanish, and no mechanism is known that would relax it to the tiny number observed.",
 "The smallness is not a detail. A much larger value would have driven matter apart before galaxies could form, and there would be no stars, no chemistry and no observers. That observation has led to anthropic arguments. They may be correct, yet they explain only in a thin sense: they derive what observers will find from the fact that observers exist, not from a dynamical principle.",
 "The constant is therefore both the dominant component of the present universe and the least understood. Its smallness is the sharpest quantitative failure of present theory, and the failure is not hidden. It is written in the expansion rate of the universe and in the existence of the reader.",
]),
('replace', 2075, [
 "Annual modulation is a predicted signature. The Earth’s orbital motion causes the dark-matter flux to vary by a few percent over the year. One experiment has reported a modulation. Others have not confirmed it. The discrepancy remains unresolved. Directional detectors aim to measure the arrival direction of the recoiling nucleus. The direction would point opposite the solar motion through the galactic halo. No directional detector has yet reached the required sensitivity.",
 "Axion searches use resonant cavities in strong magnetic fields, where an axion would convert into a photon at a frequency set by its mass. The search is therefore a slow scan through frequencies, and nothing has turned up in the ranges covered so far. Much of the allowed mass range is still unexplored. Primordial black holes are constrained by microlensing, by dynamical effects on stars, and by the absence of evaporation signals. In most mass windows they can make up only a fraction of the dark matter.",
]),
]
