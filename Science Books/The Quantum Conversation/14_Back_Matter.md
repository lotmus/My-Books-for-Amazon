## Appendix A: Equations at a Glance

The twelve equations below are the ones this book actually asks a reader to carry forward. Everything else in these pages is written in plain sentences on purpose, matching the book's own working rule that a formula earns a place on this list only when it clarifies something a paragraph alone could not. Chapter references point to where each one is first developed. Appendix E says what each letter is doing, and which formulas have set the speed of light to 1.

> **Equation (1).** The superconducting flux quantum (Chapter 3):
> *Φ_0 = h/2e*

In the idealized loop picture used throughout this book, the flux trapped by a superconducting loop comes only in whole multiples of this amount: the payoff of demanding that a quantum phase return to itself consistently around a closed path. Work the unit out and it comes to about 2.07×10⁻¹⁵ weber — a billionth of the flux an ordinary refrigerator magnet leaves through a square centimeter of air, which is why it took a superconductor, not a compass, to notice it was there at all. (The exact quantized quantity is the *fluxoid*, which folds in the loop's own current; it reduces to plain flux in the thick, well-screened loops this book pictures.)

> **Equation (2).** Maxwell's equations (Chapter 13):
> *∇·E = ρ/ε₀*
> *∇·B = 0*
> *∇×E = −∂B/∂t*
> *∇×B = μ₀J + μ₀ε₀∂E/∂t*

Two of these four — the homogeneous pair — follow automatically once the fields are built from potentials, a mathematical consequence of that construction. Only the other two carry independent dynamical content. For the patient, ground-up introduction to what each equation physically means, Daniel Fleisch's *A Student's Guide to Maxwell's Equations* remains the standard place to start.

> **Equation (3).** Electromagnetic energy density and flux (Chapters 18–19):
> *u = ½(ε₀E² + B²/μ₀)*
> *S = (1/μ₀)E×B*

The classical field's own energy bookkeeping: the non-negotiable accounting any alternative formulation has to reproduce, one way or another.

> **Equation (4).** Photon energy and momentum (Chapter 19):
> *E = ħω*
> *p = ħω/c*

What a photon delivers on arrival at a detector: a concrete, measurable amount of energy and momentum. Put in a frequency corresponding to green light and the answer comes out to about 2.3 electron-volts per photon — the same number, worked from the other direction, behind the solar-cell example in Chapter 9.

> **Equation (5).** The Lorentz force (Chapter 25):
> *F = q(E + v×B)*

The everyday force law survives as the classical limit of the deeper action-and-phase picture — the same equation, now understood as a special case of something larger.

> **Equation (6).** The covariant derivative (Chapter 28):
> *D_u = ∂_u − (iq/(ħc))A_u*

Where the electromagnetic interaction actually lives inside the machinery of QED — a single modification to an ordinary derivative, carrying the whole coupling between matter and field. The *c* in the denominator keeps the relativistic algebra of Chapter 28 honest. Set *c* = 1 and this is the same coupling as Equation (8).

> **Equation (7).** The Coulomb potential energy and force (Chapter 30):
> *V(r) = q₁q₂/4πε₀r*
> *F = (q₁q₂/4πε₀r²)r̂*

The oldest result in electromagnetism, rederived here as the low-energy limit of a full quantum scattering calculation.

> **Equation (8).** The book's central bridge (Chapter 32):
> *J ∝ ħ∇θ − qA*

With the speed of light set to 1, as Chapter 28 explains, this is the coupling inside the covariant derivative at the microscopic scale and inside a superconductor's supercurrent at the macroscopic scale, up to the carrier density and effective mass folded into the proportionality — the clearest single piece of evidence this book has to offer for its own argument.

> **Equation (9).** The Wilson loop (Chapter 35):
> *W(C) = exp((iq/ħ)∮_C A·dx)*

The formal, gauge-invariant descendant of every closed loop this book has followed since Chapter 3 — direct evidence that those loops were pointing at the geometry of gauge theory the whole time.

> **Equation (10).** The electron's anomalous magnetic moment (Chapter 37):
> *a_e = (g − 2)/2 = α/(2π) + ···*

The definition is the first equality. The prediction is the series, beginning with Schwinger's *α/(2π)*. The full calculation agrees with experiment to better than one part in a billion, through roughly ten significant digits of *a_e*: the fingerprint of virtual quantum processes stamped directly onto a measurable number.

> **Equation (11).** The fine-structure constant (Chapter 38):
> *α = e²/4πε₀ħc ≈ 1/137*

The familiar number that turns out not to be quite fixed after all — the low-energy face of a coupling that runs with scale. At everyday energies the measured value comes out to α ≈ 1/137.036, precise enough that the next few digits genuinely test QED itself.

> **Equation (12).** The Josephson relations (Chapter 40):
> *I = I_c sin(δ)*
> *U(δ) = −E_J cos(δ)*
> *V = (ħ/2e) dδ/dt*

The equations that turn a quantum phase difference into a measurable current, a controllable nonlinear energy, and — through the third relation — a literal voltmeter reading: together, the working heart of every superconducting circuit this book describes. Work out that third relation's constant and you get 2e/h ≈ 483.6 gigahertz per millivolt. Since 2019 the modern SI defines the volt from the fixed values of *e* and *h*, which makes this conversion exact; a Josephson junction is the laboratory realization of that definition.

## Appendix B: Notes on Sources

This book places a small numbered marker at the point where a specific dated result is used, rather than interrupting the prose with a citation. This section gathers what those markers point to. Where a paper has a digital object identifier, the link is given so the source can be opened directly.

**1.** The Aharonov–Bohm effect, discussed from Chapter 2 onward, was proposed by Yakir Aharonov and David Bohm in "Significance of Electromagnetic Potentials in the Quantum Theory" (*Physical Review* 115, 485, 1959), https://doi.org/10.1103/PhysRev.115.485, and confirmed with the magnetic field shielded from the electron wave by Akira Tonomura and colleagues (*Physical Review Letters* 56, 792, 1986), https://doi.org/10.1103/PhysRevLett.56.792.

**2.** The flux-quantization argument in Part One follows Carver Mead, *Collective Electrodynamics: Quantum Foundations of Electromagnetism* (MIT Press, 2000), the primary source for this book's phase-centered framework.

**3.** Einstein's explanation of the photoelectric effect — the work cited in his 1921 Nobel Prize, rather than relativity — is "Über einen die Erzeugung und Verwandlung des Lichtes betreffenden heuristischen Gesichtspunkt," "On a Heuristic Point of View Concerning the Production and Transformation of Light" (*Annalen der Physik*, 1905), https://doi.org/10.1002/andp.19053220607, from the same year as his papers on Brownian motion and special relativity.

**4.** Richard Feynman's path-integral formulation was developed in his 1942 doctoral thesis and published as "Space-Time Approach to Non-Relativistic Quantum Mechanics" (*Reviews of Modern Physics* 20, 367, 1948), https://doi.org/10.1103/RevModPhys.20.367.

**5.** Wheeler and Feynman's absorber theory, developed while Feynman was Wheeler's graduate student at Princeton, appeared as "Interaction with the Absorber as the Mechanism of Radiation" (*Reviews of Modern Physics* 17, 157, 1945), https://doi.org/10.1103/RevModPhys.17.157, and "Classical Electrodynamics in Terms of Direct Interparticle Action" (*Reviews of Modern Physics* 21, 425, 1949), https://doi.org/10.1103/RevModPhys.21.425.

**6.** The Lamb shift was measured by Willis Lamb and Robert Retherford in "Fine Structure of the Hydrogen Atom by a Microwave Method" (*Physical Review* 72, 241, 1947), https://doi.org/10.1103/PhysRev.72.241, using surplus wartime radar electronics; the result is widely credited as one of the experimental triggers for modern renormalized QED.

**7.** Emmy Noether's theorem connecting symmetries to conservation laws was published in 1918 as "Invariante Variationsprobleme" (*Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen*, 1918). An English translation by M. A. Tavel, "Invariant Variation Problems," appeared in *Transport Theory and Statistical Physics* 1, 186 (1971), https://doi.org/10.1080/00411457108231446.

**8.** The Casimir effect was predicted by Hendrik Casimir in "On the Attraction Between Two Perfectly Conducting Plates" (*Proceedings of the Koninklijke Nederlandse Akademie van Wetenschappen* B51, 793, 1948). The academy's scan of that paper is at https://dwc.knaw.nl/DL/publications/PU00018547.pdf. The journal predates DOIs, so none is attached here. The measurement is Steve Lamoreaux, "Demonstration of the Casimir Force in the 0.6 to 6 μm Range" (*Physical Review Letters* 78, 5, 1997), https://doi.org/10.1103/PhysRevLett.78.5.

**9.** The Abrikosov flux lattice was predicted by Alexei Abrikosov in "On the Magnetic Properties of Superconductors of the Second Group" (*Soviet Physics JETP* 5, 1174, 1957). The journal's English PDF is at https://jetp.ras.ru/cgi-bin/dn/e_005_06_1174.pdf. No DOI is attached. The lattice was later confirmed by direct imaging.

**10.** Paul Dirac's argument connecting magnetic monopoles to charge quantization, "Quantised Singularities in the Electromagnetic Field" (*Proceedings of the Royal Society A* 133, 60, 1931), https://doi.org/10.1098/rspa.1931.0130. No monopole has yet been detected.

**11.** The single-photon behavior in Chapter 33 draws on Grangier, Roger, and Aspect, "Experimental Evidence for a Photon Anticorrelation Effect on a Beam Splitter" (*Europhysics Letters* 1, 173, 1986), https://doi.org/10.1209/0295-5075/1/4/004.

**12.** The leading term in the electron's anomalous magnetic moment, *α/(2π)*, is Julian Schwinger, "On Quantum-Electrodynamics and the Magnetic Moment of the Electron" (*Physical Review* 73, 416, 1948), https://doi.org/10.1103/PhysRev.73.416. The measurement cited for the modern comparison is X. Fan, T. G. Myers, B. A. D. Sukra, and G. Gabrielse, "Measurement of the Electron Magnetic Moment" (*Physical Review Letters* 130, 071801, 2023), https://doi.org/10.1103/PhysRevLett.130.071801. That paper reports *g*/2 to 0.13 parts per trillion.

The comparison with the calculated series is limited by disagreement between independent measurements of the fine-structure constant, which the prediction depends on. "Better than one part in a billion," and "roughly ten significant digits" of *a_e*, are the conservative statements used in the text.

**13.** The Josephson effect was predicted by Brian Josephson in "Possible New Effects in Superconductive Tunnelling" (*Physics Letters* 1, 251, 1962), https://doi.org/10.1016/0031-9163(62)91369-0, when he was a twenty-two-year-old graduate student at Cambridge. He shared the 1973 Nobel Prize in Physics for the result.

**Further reading.** Organized by how much background they assume. Years are the editions this book has in mind.

**Accessible.** Richard Feynman, *QED: The Strange Theory of Light and Matter* (Princeton University Press, 1985). The source for this book's restraint about virtual photons and diagrams.

**Intermediate.** Carver Mead, *Collective Electrodynamics: Quantum Foundations of Electromagnetism* (MIT Press, 2000). The book this argument is built on, and much more demanding than Feynman's. David J. Griffiths, *Introduction to Electrodynamics*, 4th edition (Cambridge University Press, 2017), for the classical treatment this book arrives at backward. Daniel Fleisch, *A Student's Guide to Maxwell's Equations* (Cambridge University Press, 2008), the ground-up reading named under Equation (2). Michael Tinkham, *Introduction to Superconductivity*, 2nd edition (McGraw-Hill, 1996), for the physics behind Parts Two and Eleven.

**Advanced.** Michael E. Peskin and Daniel V. Schroeder, *An Introduction to Quantum Field Theory* (Westview Press, 1995), or Matthew D. Schwartz, *Quantum Field Theory and the Standard Model* (Cambridge University Press, 2014). The covariant derivative in Chapter 28 is one line from a subject either book spends several hundred pages on. For the circuit at the end of the wire, Alexandre Blais, Arne L. Grimsmo, S. M. Girvin, and Andreas Wallraff, "Circuit quantum electrodynamics" (*Reviews of Modern Physics* 93, 025005, 2021), https://doi.org/10.1103/RevModPhys.93.025005.

## Appendix C: Glossary

Short meanings, in the sense this book uses them. The chapter is where the term is first put to work. Letters, recurring numbers, and the distinctions that are easy to fuse live in Appendix E.

**Action.** A single number built from an entire history. Each history contributes a phase factor *exp(iS/ħ)*. Chapters 10 and 25.

**Aharonov–Bohm effect.** An interference shift set by magnetic flux in a region the electron never enters. Chapters 2, 3, and 30.

**Amplitude.** The complex number quantum mechanics assigns to one way a story might unfold. Its length, squared, is the probability. Its angle is the phase. Chapter 1.

**Anomalous magnetic moment.** *a_e = (g − 2)/2*. Dirac's theory gives *g = 2*. QED predicts *a_e* as a series in *α*, beginning with *α/(2π)*. Chapter 37.

**Coherence.** A shared phase, stable enough that contributions add instead of canceling at random. Chapters 5, 6, and 32.

**Connection.** The rule, supplied by the potential, for comparing phase at neighboring points. Chapter 21.

**Covariant derivative.** An ordinary derivative with the potential built into it. Equation (6). Set *c = 1* and it is the same coupling as Equation (8). Chapter 28.

**Curvature.** The failure of a phase comparison to come back independent of path. In this book, that failure is the electromagnetic field. Chapters 21 and 48.

**Decoherence.** Environmental entanglement that scrambles the phase relationships large-scale interference needs. Chapter 32.

**Effective theory.** A description that keeps the variables relevant at one scale and absorbs the rest into its parameters. Chapters 22 and 39.

**Feynman diagram.** A picture of one term in a perturbative amplitude. Not a photograph of a process. Chapter 29.

**Fine-structure constant.** *α = e²/(4πε₀ħc) ≈ 1/137.036* at everyday energies, and slightly different at others. Chapter 38.

**Flux quantum.** *Φ₀ = h/2e*, the flux step for a coherent pair of electrons in the thick-loop picture. Chapter 3.

**Fluxoid.** The closed-loop combination of enclosed flux and the loop's own current. It reduces to plain flux in the thick, well-screened loops this book uses. Chapter 3.

**Four-potential.** The scalar potential and the vector potential packaged as one relativistic object. Chapters 4 and 12.

**Gauge transformation.** A rewrite of the potentials that leaves the fields, and every measurement, unchanged. Chapter 4.

**Green's function.** The response at one event to a pointlike source at another. It carries the theory's causal structure. Chapter 8.

**Interference.** Addition of amplitudes. Routes whose phases agree reinforce; routes whose phases disagree cancel. Chapter 1.

**Josephson junction.** A thin barrier between two superconductors. The supercurrent depends on the phase difference across it. Chapter 40.

**Lagrangian.** The density that is integrated over spacetime to make the action. The QED expression in Chapter 28 keeps the interaction exact and the field term schematic. Chapter 28.

**Order parameter.** The collective variable that describes an organized many-body state. Here, the superconducting phase and its amplitude. Chapters 31 and 41.

**Path integral.** The sum over histories, each weighted by a phase built from the action. The classical path is where neighboring phases agree. Chapter 10.

**Phase.** The angle of an amplitude. Unobservable alone. Decisive when two routes to the same outcome are added. Chapters 1–3.

**Photon.** A quantum excitation of the electromagnetic field, carrying energy *ħω* and momentum *ħω/c*. Chapters 9 and 19.

**Potential.** The scalar potential *φ* and the vector potential **A**. They enter a charged particle's phase directly. The fields are built from them. Chapters 2–4 and 12.

**Propagator.** The contribution, inside an amplitude, of a disturbance at one event to another event. Chapters 8 and 29.

**Renormalization.** The bookkeeping that keeps measurable predictions unchanged when the resolution scale changes. Chapters 37–39.

**Running coupling.** The effective strength of the electromagnetic interaction as the energy of the probe changes. Chapters 37 and 38.

**Supercurrent.** The current of a coherent condensate, tied to *ħ∇θ − qA*. Chapters 31 and 32.

**Vacuum polarization.** The correction to one photon's propagation from a charged-particle loop. A different diagram from light scattering off light. Chapter 36.

**Virtual photon.** An internal line in a Feynman diagram: a term in a calculation, not a particle caught in a detector. Chapters 9 and 29.

**Bandgap.** The energy a photon must clear to free an electron inside a semiconductor. A metal's threshold is a work function instead. Chapter 9.

**Canonical momentum.** The momentum tied to the phase gradient. With a vector potential present it splits from the mechanical momentum, *p − qA*. Chapters 7 and 30.

**Compton scattering.** An X-ray photon bouncing off an electron and leaving with a longer wavelength. A straight-back bounce lengthens it by about five picometers. Chapter 20.

**Cooper pair.** Two electrons bound into one superconducting state, opposite spin and opposite momentum, charge *q* = 2*e*. In ordinary low-temperature superconductors the attraction is carried by lattice vibrations. The pair is why the flux step is *h*/2*e*. Chapters 3 and 40.

**Crossing.** Reading an outgoing positron as an incoming electron with time reversed on the diagram, so one calculation covers several related processes. Chapter 20.

**Entanglement.** One joint state of two systems that cannot be pulled apart into two independent states. Chapter 34.

**Lamb shift.** The splitting, about 1058 megahertz, between the hydrogen 2S and 2P levels. Chapter 20.

**Magnetic monopole.** An isolated magnetic charge. None has been detected. Dirac showed that one, anywhere, would force electric charge to come in steps. Chapter 27.

**Poynting vector.** *S* = (1/μ₀)*E*×*B*, the classical flow of electromagnetic energy. Equation (3). Chapters 18 and 19.

**Qubit.** Two unevenly spaced energy levels of a Josephson circuit, addressed like an artificial atom. Chapter 40.

**Wilson loop.** The phase factor from the potential integrated around a closed curve. Equation (9). Chapter 35.

## Appendix D: Index

Entries point to the chapter where the idea is developed, not to every mention. Page numbers belong to the typeset book. These are the chapters.

Abrikosov vortex lattice, 27
Action, 10, 25, 28
Aharonov–Bohm effect, 2, 3, 30
Amplitude and the Born rule, 1, 10
Anomalous magnetic moment, 20, 37
Antiparticle and pair production, 20
Aspect, Grangier, and Roger, 33
Bandgap and the photoelectric effect, 9
Canonical and mechanical momentum, 7, 30
Casimir effect, 26, 34
Cavity QED and circuit QED, 34, 40, 41
Central bridge, *J ∝ ħ∇θ − qA*, 31, 32
Charge conservation and Noether's theorem, 24
Coherence, of matter and of light, 5, 6, 14, 19, 32
Compton scattering, 20
Connection and curvature, 21, 48
Cooper pair, 3, 40
Coulomb force, 30
Covariant derivative, 28
Crossing, 20
Decoherence, 32
Dirac monopole, 27
Effective theory, 22, 38, 39
Einstein, magnet and conductor, 26
Entanglement, 34
Feynman, path integral and diagrams, 10, 16, 29
Feynman diagrams, 29, 37
Fine-structure constant, 38
Flux quantum and fluxoid, 3
Four-potential, 4, 12, 26
Gauge transformation, 4
Green's function and causality, 8
Interference, 1, 10
Josephson, 40
Josephson relations and the volt, 40
Lagrangian of QED, 28
Lamb and Retherford, 20
Lamb shift, 20
Lamoreaux, 26
Laser and coherence, 14
Lorentz force, 25, 26
Maxwell's equations, 12, 13
Mead's contribution, front matter, 42, 47
Noether, 24
Path integral, 1, 10, 16
Phase, 1–4
Photon, real and virtual, 9, 19, 29
Potential, scalar and vector, 2, 4, 7
Poynting theorem, 18, 19
Renormalization, 37–39
Running coupling, 37, 38
Schwinger's term, *α*/(2π), 37
Speed of light, from the unit ratio, 26
Superconducting circuit and qubit, 40, 41
Supercurrent, 31, 32
Tonomura, 2
Vacuum polarization and light-by-light, 36
Weber and Kohlrausch, 26
Wheeler–Feynman absorber theory, 15–19, 47
Wilson loop, 35

## Appendix E: Symbols, Numbers, and Distinctions

The formulas reuse a small alphabet. What follows is the meaning each letter keeps in this book, the handful of numbers the text actually computes, and the distinctions a fast reading can fuse.

**Phase.** *θ* is the phase of a coherent state, the angle of its amplitude. *δ* is the difference between two such phases across a Josephson junction. *χ* is the arbitrary smooth function in a gauge transformation. A potential is none of these three.

**Potentials and fields.** *φ* is the scalar potential. **A** is the vector potential. Packaged together they are the four-potential. The fields are built from them, as Chapter 2 writes: **B** = ∇×**A** and **E** = −∇*φ* − ∂**A**/∂*t*. A gauge transformation, Chapter 4, replaces **A** with **A** + ∇*χ* and *φ* with *φ* − ∂*χ*/∂*t*. The fields come out unchanged. ∇ measures how fast a quantity changes from point to point; ∇× measures how much it swirls.

**Charge.** *e* is the magnitude of one electron's charge. *q* is the charge that is actually coherent in the formula in front of you. This book writes a loop phase as *q*Φ/*ħ*, with *q* positive. For a Cooper pair, *q* = 2*e*, which is why Equation (1) is *h*/2*e* and why Equation (12) has 2*e* in the denominator. For a single electron the same rule uses *q* = *e*.

That last sentence has a checkable consequence. One superconducting flux quantum is Φ₀ = *h*/2*e*. The phase a charge *q* picks up around a loop enclosing flux Φ is *q*Φ/*ħ*, and *ħ* = *h*/2π. Put in a pair, *q* = 2*e*, and the phase around one Φ₀ is a full turn, 2π, which is why the flux changes in steps of Φ₀. Put in one electron, *q* = *e*, and the phase around that same Φ₀ is π. The flux that shifts a single electron's interference by a full turn is *h*/*e*, twice Φ₀. Equation (1) is the pair step. The Aharonov–Bohm pattern for electrons repeats on the larger step.

**The two writings of the same coupling.** Equation (6) keeps *c* in the denominator so that substituting the covariant derivative into the electron term produces *L_int* = *qψ̄γᵘA_uψ* with no leftover factor of *c*. The flux quantum, the Wilson loop, and *J* ∝ *ħ*∇*θ* − *q***A** are that same coupling with the speed of light set to 1. Restoring *c* there is a choice of units. It is the same interaction.

***h* and *ħ*.** *h* is Planck's constant. *ħ* is *h* divided by 2π. Equation (1) is written with *h* because a full turn of phase is 2π, and 2π × *ħ* is *h*. The phase factor *exp*(*iS*/*ħ*) and the Josephson voltage use *ħ*. Φ₀ = *h*/2*e* and Φ₀ = 2π*ħ*/2*e* are the same quantity.

**Numbers already worked in the text.** Φ₀ is about 2.07×10⁻¹⁵ weber, roughly two femtowebers. A green photon delivers about 2.3 electron-volts. An electron-positron pair requires at least 1.022 million electron-volts, and a lone photon in empty space cannot supply it; a third body, typically a nucleus, has to take the recoil. The Josephson conversion is 2*e*/*h* ≈ 483.6 gigahertz per millivolt, so five gigahertz is about ten microvolts. At everyday energies *α* ≈ 1/137.036. The series for the electron's anomalous magnetic moment agrees with experiment to better than one part in a billion.

The Lamb shift in hydrogen is about 1058 megahertz. A photon scattered straight back off an electron lengthens by about five picometers. Ideal Casimir plates a micrometer apart feel about a millipascal. Abrikosov vortices in a field of a tenth of a tesla sit roughly 150 nanometers apart. Weber and Kohlrausch's 1856 ratio matched the speed of light to about one percent.

**Distinctions the argument keeps apart.** A real photon is an excitation that can arrive at a detector, carrying energy *ħω* and momentum *ħω*/*c*. A virtual photon is an internal line in an amplitude. It is a term in a calculation.

Vacuum polarization corrects the propagation of one photon by a charged-particle loop. Light scattering off light uses that same kind of loop with two further photon legs. The second process has its own name, light-by-light scattering.

*a_e* = (*g* − 2)/2 is a definition. Dirac's theory gives *g* = 2, so *a_e* = 0. The prediction is the series that begins with Schwinger's *α*/(2π).

An ordinary inductor-capacitor circuit, once charge and phase are quantum variables, already has discrete energy levels, evenly spaced. The Josephson cosine makes that spacing uneven, which is what lets one transition be addressed on its own.

In that circuit, charge is conjugate to the phase. Voltage is how fast the phase changes.

Saying that a formulation stores energy in the field is a statement about how that formulation keeps its books. Saying that the energy belongs to an independent substance called the field is a different claim. Part Five is about the second. It does not replace QED.

The interaction term in Chapter 28 can be checked by the substitution just described. The electromagnetic-field term written beside it is still schematic.

## If This Book Worked for You

The wider map — entanglement, Bell tests, quantum fields, quantum gravity, interpretations, computing, and cryptography — is *The Quantum World*, elsewhere in this series. This book began there, as an interlude on collective electrodynamics that outgrew its chapter.

Feynman's *QED* and Mead's *Collective Electrodynamics*, and the other books named along the way, are listed with their editions at the end of Appendix B.

## Also by Lothar J. Musiol

A shelf, if you want the rest of it — from the same author, in whichever direction your curiosity runs next.

**Science for Everyone.** *The Quantum World* · *Physics Vol. 1 — Motion, Forces, Time, and Relativity* · *Physics Vol. 2 — Gravity, Cosmology, and the Limits of Spacetime* · *Physics Vol. 3 — The Standard Model, Chaos, and the Edge of Knowledge*

**Also nonfiction.** *The Mathematics Tower* · *Foundations of Electronics*

**Fiction.** *The Relativistic Investigation Bureau* · *Schrödinger's Paperwork*

## About the Author

The prologue's forty years around components that obey Maxwell's equations were spent in industry. Lothar J. Musiol is a graduate of Munich University of Applied Sciences who spent more than forty years in the semiconductor industry — first at the largest company in the field Germany had to offer, then at a string of American start-ups, where the insights arrived faster than the job security. He studied physics alongside all of it, seriously enough to know exactly how much of it he is simplifying in these pages, and how much he is not.

Dual citizenship, deployed to its most sensible possible use, now lets him split his time between San Clemente, California, and Passau, Bavaria, where Austria begins directly at the garden fence and the household includes one married daughter, one grumpy Teacup Pomeranian, and eleven chickens of various sizes and ages, listed here in order of seniority rather than of volume.

He writes to make complex ideas clearer and more engaging than most treatments manage, without ever pretending they are simpler than they actually are.

## A Small Request

If *The Quantum Conversation* gave you a new way of seeing something you thought you already understood, the single most useful thing you can do for it is to leave a review where you found it. Reviews are how books like this one — dense, particular, and not obviously commercial — find the handful of readers who were actually looking for them.

A sentence is enough.
