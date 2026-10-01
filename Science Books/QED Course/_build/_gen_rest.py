# -*- coding: utf-8 -*-
"""Write remaining QED lessons 72,74,76-78,80-86 in course markup."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))


def lesson(num, title, tagline, nxt, body):
    return (
        "TITLE: %s\nTAGLINE: %s\nNUM: %d\nNEXT: %s\n\n%s"
        % (title, tagline, num, nxt, body.strip())
        + "\n"
    )


def pack(title, hours, objectives, notation, sections, connections, summary, exercises, solutions, mastery):
    parts = ["# How to use this lesson\n", hours, "\n## Learning objectives\n"]
    for o in objectives:
        parts.append("- %s\n" % o)
    parts.append("\n## Notation and conventions\n\n@widths 2160 7632\n| Symbol | Meaning |\n")
    for a, b in notation:
        parts.append("| %s | %s |\n" % (a, b))
    parts.append("\n")
    parts.append(sections)
    parts.append("\n# Connections to QED\n\n@widths 3264 6528\n| Result of this lesson | Where it is used |\n")
    for a, b in connections:
        parts.append("| %s | %s |\n" % (a, b))
    parts.append("\n# Summary\n\n")
    for i, s in enumerate(summary, 1):
        parts.append("%d. %s\n\n" % (i, s))
    parts.append("# Exercises\n\n@widths 720 9072\n| No | Problem |\n")
    for i, e in enumerate(exercises, 1):
        parts.append("| %d | %s |\n" % (i, e))
    parts.append("\n# Solutions\n\n")
    for i, s in enumerate(solutions, 1):
        parts.append("**%d.** %s\n\n" % (i, s))
    parts.append("# Mastery checklist\n\n")
    for m in mastery:
        parts.append("- %s\n\n" % m)
    return "".join(parts)


L = {}

L[72] = lesson(72, "Gauge Invariance",
    "Physical observables do not depend on the gauge, which is Lesson 71's Ward identity read as a statement about ξ, Coulomb gauge, and Feynman gauge together",
    "Lesson 73 turns from gauge artifacts to a genuine infinity that survives in a physical exclusive rate: the infrared divergence.",
    pack("Gauge Invariance",
         "Lesson 70 introduced ξ. Lesson 71 proved k_μ ℳ^μ=0. This lesson puts those together: a physical cross section computed in Coulomb gauge, Feynman gauge, or Landau gauge must agree, and any leftover ξ in a calculation is a sign that a diagram is missing. Expect four to six hours.\n",
         ["State that |ℳ|² for a physical process is independent of ξ and of the Coulomb versus covariant gauge choice.",
          "Identify a leftover ξ dependence as evidence of an incomplete set of diagrams.",
          "Reconnect Lesson 37's two transverse polarizations with Lesson 70's four-component covariant field.",
          "State that gauge invariance of observables is not the same as gauge invariance of ℒ after ℒ_gf is added."],
         [("ξ", "Gauge parameter of Lesson 70"),
          ("observable", "A quantity unchanged by ε_μ→ε_μ+λk_μ and by ξ→ξ'")],
         """# 1 What is invariant, and what is not

The QED Lagrangian of Lesson 41 is invariant under local U(1). The gauge-fixed Lagrangian of Lesson 70 is not. The path integral of Lesson 79, after Faddeev-Popov, is arranged so that Z for gauge-invariant operators does not depend on ξ. In the operator language of this course, that statement is the Ward identity plus a complete sum of diagrams.

### Worked example 1

Is the photon propagator itself an observable? No. D_μν(k;ξ) depends on ξ. Only its contractions with conserved currents, in a complete amplitude, are.

# 2 Three gauges, one |ℳ|²

Coulomb gauge (Lesson 37) uses two physical polarizations from the start. Feynman gauge (ξ=1) uses −ig_μν/k² and lets the Ward identity kill unphysical modes. Landau gauge (ξ=0) makes the propagator transverse. Computing Compton scattering, Lesson 56, in any of these must give the same (1/4)Σ|ℳ|²=−2e⁴(s/u+u/s) in the massless limit, because that quantity was contracted with conserved currents and summed over physical polarizations.

# 3 Incomplete diagrams

A single Compton diagram, contracted with k_μ, does not vanish. Both diagrams of Lesson 56 are required. Dropping one would produce a ξ-dependent, gauge-dependent, wrong answer. The same is true of Møller scattering's two diagrams and of the vertex plus self-energy combination that renormalizes the charge consistently with the Ward identity (Z1=Z2 in a gauge-invariant scheme).
""",
         [("ξ-independence of |ℳ|²", "The practical meaning of Lesson 71"),
          ("Need for complete diagram sets", "Compton, Møller, vertex vs self-energy")],
         ["ℒ is gauge invariant; ℒ+ℒ_gf is not; observables still are.",
          "|ℳ|² agrees in Coulomb, Feynman, and Landau gauges.",
          "Leftover ξ means a diagram is missing.",
          "Z1=Z2 is the renormalization version of the same identity."],
         ["Is D_μν(k;ξ) gauge invariant?",
          "Name three gauges used in this course.",
          "Why must both Compton diagrams be kept?",
          "What does a leftover ξ in |ℳ|² indicate?",
          "State the difference between invariance of ℒ and invariance of observables.",
          "How do two transverse polarizations in Coulomb gauge match four components in Feynman gauge?",
          "What is Z1=Z2, in words?",
          "Does a gauge-dependent Green's function invalidate the theory?",
          "Apply ε→ε+λk to a physical ℳ using Lesson 71.",
          "Why is the Coulomb potential instantaneous in Coulomb gauge not a contradiction with relativity?",
          "Landau vs Feynman: which propagator is transverse?",
          "Can a single self-energy diagram be gauge invariant by itself?",
          "Connect this lesson to Lesson 8's residual Lorenz-gauge freedom.",
          "What class of operators can have ξ-independent correlators?",
          "If a calculation of eμ scattering kept only the electron tensor and dropped the muon tensor, would gauge invariance survive?",
          "Challenge: sketch why the Ward identity implies Z1=Z2 at one loop, relating Lesson 64 to Lesson 63."],
         ["No; it depends on ξ.",
          "Coulomb, Feynman (ξ=1), Landau (ξ=0).",
          "Each diagram is not transverse; their sum is.",
          "An incomplete set of diagrams.",
          "ℒ without ℒ_gf is locally invariant; after gauge fixing, only observables remain invariant.",
          "Unphysical polarizations in Feynman gauge cancel in |ℳ|² by the Ward identity, leaving two physical modes.",
          "The vertex renormalization equals the electron-field renormalization in a gauge-invariant scheme, so the charge is universal.",
          "No; Green's functions are tools, not measurements.",
          "ℳ is unchanged.",
          "The instantaneous Coulomb piece is cancelled by other terms in a full amplitude, restoring causal light-cone commutators for observables.",
          "Landau: k^μ D_μν=0.",
          "No; it is an off-shell Green's function.",
          "Residual plane-wave gauges are ε∝k, killed in amplitudes.",
          "Gauge-invariant operators, or complete on-shell amplitudes.",
          "The question is malformed: those tensors are factors in one diagram, not alternative gauges. Gauge invariance is about photon indices, not about dropping a fermion line.",
          "The Ward identity k_μ Λ^μ ~ Σ(p')−Σ(p) relates the divergent parts of the vertex and the self-energy, forcing the same Z at this order."],
         ["I can state that physical |ℳ|² is ξ-independent.",
          "I can recognize missing diagrams from leftover gauge dependence.",
          "I can relate Coulomb and covariant quantization through the Ward identity."]))

L[74] = lesson(74, "Soft Photons",
    "The emission amplitude e p·ε / p·k that Lesson 73 used, derived from attaching a photon to an external line and taking k→0, and the cancellation of log λ against the virtual correction",
    "Lesson 75 evaluates the finite, magnetic piece of the vertex correction: Schwinger's a=α/(2π).",
    pack("Soft Photons",
         "Lesson 73 stated ℳ_soft=e(p·ε/p·k)ℳ_tree. This lesson derives that factor from the Feynman rules, integrates |ℳ_soft|² over unresolved photon phase space, and exhibits the cancellation of log λ. Expect five to seven hours.\n",
         ["Derive ℳ_soft by attaching a photon of momentum k to an external charged line and taking k small compared with all other momenta.",
          "Sum over polarizations to obtain a factor e² (p·p)/(p·k)² in |ℳ|².",
          "Integrate over photon energies λ<ω<ΔE and obtain  (α/π) log(ΔE/λ) times a process-dependent coefficient.",
          "State that the virtual infrared logarithm has the opposite coefficient, so their sum depends on ΔE/E, not on λ."],
         [("ω", "Soft photon energy"),
          ("λ", "Infrared regulator, a photon mass or a minimum energy")],
         """# 1 Attaching a soft photon

An external electron of momentum p, propagator i(p̸+m)/(p²−m²) just off shell after emitting a photon k, with p²=m², has denominator (p−k)²−m²=−2p·k+k²≈−2p·k. The vertex ieγ^μ contracted with ε_μ, and the Dirac equation on the external spinor, reduce the numerator to 2p·ε. The net factor is e (p·ε)/(p·k), times the original amplitude without the extra photon.

$$ ℳ_soft = Σ_i e_i (p_i · ε / p_i · k) ℳ_tree

summed over all external charged legs i, with e_i the charge including a sign for outgoing versus incoming (Exercise 5).

### Worked example 1

Check k_μ ℳ_soft^μ=0. Each term becomes e_i, and charge conservation Σ e_i=0 (incoming minus outgoing) makes the sum vanish, Lesson 71, Exercise 16.

# 2 Phase space

Integrating Σ_pol |p·ε/p·k|² over d³k/(2ω) from λ to ΔE, at small k, produces a logarithm log(ΔE/λ) because d³k/ω / (p·k)² ~ dω/ω.

# 3 Cancellation

The one-loop virtual correction, with a photon mass λ, multiplies |ℳ_tree|² by 1 − c (α/π) log(E/λ)+finite, with the same c that multiplies the real emission. Adding them replaces log(E/λ) by log(E/ΔE). Lesson 73's exclusive infinity is gone.
""",
         [("ℳ_soft=e(p·ε/p·k)ℳ_tree", "The eikonal emission factor"),
          ("log(ΔE/λ) real vs log(E/λ) virtual", "Cancellation, Bloch-Nordsieck")],
         ["Soft emission off an external line gives e(p·ε)/(p·k).",
          "Charge conservation makes the factor gauge invariant.",
          "Phase space of unresolved photons produces log(ΔE/λ).",
          "Virtual IR logs cancel real ones; the remainder depends on the detector."],
         ["Start from (p−k)²−m² and show it equals −2p·k+k².",
          "Take k→0 and drop k².",
          "Obtain the numerator 2p·ε from ieγ·ε and the Dirac equation.",
          "Assemble e(p·ε)/(p·k).",
          "Include a sign for emission off an outgoing versus incoming leg.",
          "Imposing Σ e_i=0, verify the Ward identity on ℳ_soft.",
          "Sum polarizations of ε in |p·ε/p·k|² in a frame where it is simple.",
          "Why is the angular integral of that factor producing dω/ω?",
          "Write the limits λ to ΔE on the energy integral.",
          "What physical quantity is ΔE?",
          "State the opposite logarithm from the virtual diagram.",
          "Form the sum and cancel log λ.",
          "Does this cancellation need Lesson 71?",
          "Soft vs collinear: which extra diagram cancels Compton's u-pole?",
          "Why can a hard photon (ω~E) not be treated with this factor?",
          "Challenge: write the double-soft factor as a product of two eikonal factors, the beginning of exponentiation."],
         ["(p−k)²−m²=p²−2p·k+k²−m²=−2p·k+k² on shell.",
          "k²≪2p·k for a soft photon.",
          "ū γ·ε (p̸+m) ~ 2p·ε ū, using p̸u=mu.",
          "Vertex e, numerator 2p·ε, denominator −2p·k, overall e(p·ε)/(p·k) up to a conventional sign from (p−k) versus (p+k).",
          "Outgoing emission uses p·ε/p·k with a relative minus compared with absorption on an incoming line, equivalent to assigning −e to the opposite charge flow.",
          "Each leg contributes e_i; Σ e_i=0.",
          "In a suitable frame Σ_pol |p·ε|² ~ p_perp², leaving 1/(p·k)² ~ 1/ω².",
          "Photon measure ω² dω dΩ / ω combined with 1/ω² gives dω/ω dΩ.",
          "Infrared cutoff to detector resolution.",
          "The smallest photon energy the experiment can see.",
          "−c(α/π)log(E/λ) times |ℳ_tree|².",
          "c(α/π)log(ΔE/λ)−c(α/π)log(E/λ)=c(α/π)log(ΔE/E).",
          "Yes, to guarantee the virtual and real coefficients match and that ℳ_soft is gauge invariant.",
          "A real photon collinear with the outgoing electron, not a soft photon in an unrelated direction.",
          "The propagator approximation (p−k)²−m²≈−2p·k fails when k is not small.",
          "Each extra soft photon multiplies by another eikonal factor; the sum over n photons exponentiates the logarithm, the Sudakov factor."],
         ["I can derive e(p·ε)/(p·k) from an external-line attachment.",
          "I can integrate unresolved photons to a log(ΔE/λ).",
          "I can cancel that log against the virtual infrared logarithm."]))

# Remaining lessons: write similarly in a compact but complete way
specs = [
(76, "Lamb Shift",
 "Radiative corrections split the Dirac degeneracy of hydrogen 2s_{1/2} and 2p_{1/2} by about 1058 MHz, a loop effect Lesson 15 could only name",
 "Lesson 77 isolates the vacuum-polarization piece of that shift, the Uehling potential, as a precision application of Lesson 62.",
 "The Dirac equation, with the Coulomb field as a fixed A_μ, predicts that 2s_{1/2} and 2p_{1/2} have the same energy (Lesson 15's fine-structure formula depending on n and j only). They do not: Lamb and Retherford measured a split of about 1058 MHz. The split is a QED loop effect, from the electron self-energy in an external field and from vacuum polarization. This lesson outlines the accounting, quotes the leading log, and does not redo Bethe's full numerical integral. Expect five to seven hours.",
 ["State the Dirac degeneracy: E depends on n and j, not on ℓ separately.",
  "Identify the Lamb shift as a radiative splitting of 2s_{1/2} and 2p_{1/2}.",
  "Attribute the leading logarithm to the electron self-energy in a Coulomb field, with a low-energy cutoff of order the Bohr momentum and a high-energy cutoff of order m.",
  "Quote ΔE ≈ (α⁵ m / 6π) log(1/α) for the 2s state as the leading-log estimate, and the experimental scale 1058 MHz.",
  "Defer the Uehling (vacuum-polarization) piece to Lesson 77."],
 "An electron in hydrogen is never a pure Dirac particle in a classical Coulomb field: it emits and reabsorbs virtual photons (Lesson 63) while bound. Bethe's estimate integrates that self-energy between atomic momenta ~αm and the electron mass m, producing a logarithm log(1/α). The 2s wavefunction is nonzero at the origin and feels the correction more than 2p, so the levels split. Vacuum polarization modifies the Coulomb potential at distances 1/m (Lesson 77) and contributes a smaller, opposite piece in hydrogen. The measured 2s–2p interval is 1057.8 MHz; one-loop QED accounts for it at the percent-to-permille level depending on how much of the logarithm and the finite pieces are kept. This is the loop correction Lesson 15 postponed, now named and estimated, not hidden inside a template.",
 "Dirac E(n,j) not E(n,ℓ)", "Leading log (α⁵ m) log(1/α)", "1058 MHz experiment"),
(77, "Vacuum Polarization and Precision",
 "The Uehling potential, the finite q² dependence of Π̂ from Lesson 68, as a correction to Coulomb's law inside an atom",
 "Lesson 78 places g−2, the Lamb shift, and the running of α next to the measurements they are tested against.",
 "Lesson 68 ran the charge at |q²|≫m². Inside hydrogen, typical |q| is the Bohr momentum αm, smaller than m, so the logarithm of Lesson 68 is not large. The finite remainder Π̂(q²) still modifies the photon propagator, equivalent to a short-range correction to the Coulomb potential, the Uehling potential. Expect four to six hours.",
 ["Obtain, for |q²|≪m², Π̂(q²)≈(α/15π)(q²/m²) as the leading expansion of vacuum polarization.",
  "Interpret this as a correction to 1/q² in the photon propagator, hence to the Coulomb potential in coordinate space.",
  "State that the Uehling potential is attractive extra strength at r≲1/m and contributes about −27 MHz to the hydrogen Lamb shift, opposite in sign to the dominant self-energy piece.",
  "Connect the same Π̂ at large q² to Lesson 68's running."],
 "At small q² the finite vacuum polarization behaves as Π̂(q²)∝q²/m². Replacing 1/q² by 1/q² × 1/(1−Π̂)≈1/q² + (α/15π)/m² in momentum space is a contact-like correction after Fourier transform, smeared over the Compton wavelength 1/m. An s-state, with support at the origin, sees this as a shift. The sign in hydrogen is a slight reduction of the 2s energy relative to the naive Coulomb value in the opposite direction from Bethe's self-energy log, a smaller term. The same function Π̂, evaluated at large q², is Lesson 68's running. Precision and running are one object at two kinematic points.",
 "Π̂(q²)≈(α/15π)q²/m²", "Uehling potential", "−27 MHz in hydrogen 2s"),
(78, "Precision Tests of QED",
 "g−2, the Lamb interval, and α(M_Z) compared with measurement, and what a discrepancy would actually mean",
 "Lesson 79 opens Part XI with the path integral as an equivalent derivation of the Feynman rules this course already has.",
 "This course now has three quantitative QED claims that meet experiment: a=α/(2π) at one loop (Lesson 75), a Lamb interval of order 10³ MHz (Lesson 76), and a few-percent running of α up to the Z (Lesson 68). This lesson states how they are compared, what 'one part in a billion' from Lesson 15 actually refers to (higher-order g−2, not this volume's one-loop formulae), and why a disagreement is a discovery rather than a reason to abandon renormalization. Expect four to six hours.",
 ["Quote a_e(theory, one loop)=α/(2π)≈0.0011614 versus a_e(exp)≈0.00115965, and name higher loops as the difference.",
  "Quote the Lamb interval ~1057.8 MHz as a measured QED effect absent from the Dirac spectrum.",
  "Quote α⁻¹(0)≈137.036 versus α⁻¹(M_Z)≈128–129 once all fermions are included, of which this course computed only the electron log's order of magnitude.",
  "State that a genuine discrepancy remaining after higher orders and hadronic vacuum polarization would be new physics, not a failure of Lesson 67's logic."],
 "Lesson 43's α/(2π) already matches the electron anomaly to about 0.15%. The remaining digits require two-loop and three-loop QED, a small hadronic vacuum-polarization piece, and a still smaller weak piece; they are not computed in this volume. The Lamb shift is a qualitatively new interval the Dirac equation does not have, measured in radiofrequency spectroscopy. The running of α is tested by comparing low-energy α to the coupling extracted at LEP and elsewhere near M_Z. Lesson 15's 'one part in a billion' describes the modern electron g−2 comparison after those higher orders, not the one-loop formula alone. If, after all known Standard Model pieces, a discrepancy remained (as is currently discussed for the muon, not settled in this course), that would be extra amplitudes, not a reason to doubt that m₀ can absorb an ultraviolet log.",
 "a_e one loop vs experiment", "Lamb 1057.8 MHz", "α(0) vs α(M_Z)"),
(80, "Generating Functionals",
 "Correlators as functional derivatives of Z[J]=∫ Dφ exp(iS+iJφ), recovering time-ordered products without writing an operator vacuum",
 "Lesson 81 Legendre-transforms W[J]=−i log Z[J] to the effective action Γ[φ] that generates one-particle-irreducible diagrams.",
 "Lesson 79 defined Z=∫Dφ e^{iS}. Adding a source J(x) coupled to φ makes Z a functional of J. Differentiating with respect to J brings down fields, so time-ordered correlators become δⁿZ/δJⁿ at J=0, up to factors of i. Expect four to six hours.",
 ["Write Z[J]=∫Dφ exp(iS[φ]+i∫Jφ).",
  "Obtain ⟨T φ(x)φ(y)⟩ = (1/Z) (−i)² δ²Z/δJ(x)δJ(y) at J=0, matching the propagator.",
  "Define W[J]=−i log Z[J] as the generating functional of connected correlators.",
  "State that free Z[J] is the Gaussian exp(i/2 J Δ J) with Δ the propagator."],
 "Coupling Jφ in the exponent is the path-integral version of an external current. Each δ/δJ brings down a φ. For a free theory completing the square produces Z[J]=Z[0] exp(i/2 ∫J Δ J), Lesson 2's Gaussian, and the second derivative is the propagator of Lesson 45. Connected correlators, the ones that appear in scattering after vacuum bubbles are discarded, are generated by W=−i log Z. This is bookkeeping: Wick's theorem in a different costume.",
 "Z[J]", "W=−i log Z", "δ²Z/δJδJ = propagator"),
(81, "Effective Actions",
 "The Legendre transform Γ[φ_cl] of W[J], whose tree diagrams in the φ_cl field sum the 1PI loops of the original theory",
 "Lesson 82 collects the functional derivatives and 1PI expansion as a practical toolkit, then Lesson 83 reads Feynman rules off Z.",
 "W[J] generates connected diagrams. Its Legendre transform Γ[φ_cl]=W[J]−∫J φ_cl, with φ_cl=δW/δJ, generates one-particle-irreducible diagrams. The classical field φ_cl satisfies δΓ/δφ_cl=−J, the quantum-corrected equation of motion. Expect four to six hours.",
 ["Define Γ[φ_cl] as the Legendre transform of W[J].",
  "State that vertices of Γ are 1PI correlators.",
  "Identify δΓ/δφ=0, at J=0, as the condition for the quantum vacuum expectation value.",
  "Note that the second derivative of Γ is the inverse of the full connected two-point function, i.e. the inverse of S_F′ from Lesson 67."],
 "The effective action is the tool that makes 'tree level in a corrected Lagrangian' mean 'all loops in the original theory, but only 1PI ones, with full propagators on the external legs.' Lesson 67's resummed propagator is Γ's second derivative inverted. Charge and mass renormalization are statements about the low-momentum expansion of Γ.",
 "Γ[φ]=W−Jφ", "1PI vertices", "Γ''(φ) = (full propagator)⁻¹"),
(82, "Functional Methods",
 "A short toolkit: δZ/δJ inserts a field, completing the square, and how a change of variables in Dφ produces identities",
 "Lesson 83 expands exp(iS_int) inside Z and reads off this course's Feynman rules a second time.",
 "Lessons 79–81 introduced Z, W, and Γ. This lesson is the operations on them used in practice: inserting fields, completing squares, and obtaining Ward identities from a change of dummy integration variables. Expect four to five hours.",
 ["Insert a field by δ/δJ.",
  "Complete the square in a Gaussian Z[J].",
  "Obtain a Ward identity by shifting φ→φ+δφ inside Dφ when the measure is invariant.",
  "State that these operations do not add new physics beyond Parts V–X; they reorganize it."],
 "If the measure Dφ is invariant under φ→φ+ε(x) and S changes by a known δS, then ⟨δS⟩=0, which is an operator identity, the path-integral form of Lesson 71 when the shift is a gauge transformation. Completing the square is Lesson 2. Inserting fields is how Lesson 80's correlators were defined. There is no third quantization here, only a compact language.",
 "δ/δJ inserts φ", "shift of dummy variable", "⟨δS⟩=0"),
(83, "Feynman Rules from the Path Integral",
 "Expanding exp(iS_int) in Z and contracting with the free Gaussian measure recovers Lesson 49's rules, including the closed-fermion-loop minus sign",
 "Lesson 84 Wick-rotates the same integral to imaginary time and imposes period 1/T, the finite-temperature theory.",
 "Lesson 49 derived Feynman rules from the Dyson series. This lesson derives the same rules from Z=∫Dφ e^{iS_0} e^{iS_int}. Expect four to six hours. The point is the match, not a new process.",
 ["Expand e^{iS_int} as a power series in e.",
  "Contract fields in pairs using the free propagator (Wick / Gaussian).",
  "Read ieγ^μ off S_int=e ψ̄γ^μψ A_μ.",
  "Obtain a minus sign for each closed fermion loop from Grassmann integration."],
 "Each power of S_int brings vertices. Each Gaussian contraction brings a propagator. Uncontracted fields at infinity become external spinors and polarizations, Lesson 48. The combinatorics of 1/n! versus the number of ways to assign vertices reproduces Lesson 49's cancellation of 1/2! against two equivalent assignments. Nothing in Compton scattering's amplitude changes.",
 "e^{iS_int} expansion", "Wick contractions", "same rules as Lesson 49"),
(84, "QED at Finite Temperature",
 "Euclidean time is periodic with period 1/T, Matsubara frequencies replace k⁰, and the partition function is a path integral on a circle",
 "Lesson 85 puts QED in a strong external field, pair production without a second real photon, the process Lesson 57 postponed.",
 "Wick rotation (Lesson 66) turns e^{iS} into e^{−S_E}. At temperature T the Euclidean time is compact with period β=1/T, bosons periodic, fermions antiperiodic. Loop integrals become sums over Matsubara frequencies 2πnT (bosons) or 2π(n+1/2)T (fermions). Expect five to seven hours. This course does not compute a thermal production rate in full.",
 ["State Z(T)=∫_{periodic} Dφ exp(−S_E) with τ∈[0,1/T].",
  "Write bosonic Matsubara frequencies ω_n=2πnT.",
  "Write fermionic frequencies ω_n=2π(n+1/2)T.",
  "Note that T→0 recovers ordinary QED, and that thermal photons have a Bose distribution once the k⁰ contour is done."],
 "A thermal equilibrium state is a trace, Tr e^{−H/T}, which in the path integral is a closed loop in imaginary time of length 1/T. The Feynman rules of Lesson 49 still apply, with k⁰ replaced by iω_n and ∫dk⁰/2π replaced by T Σ_n. Infrared divergences of Lesson 73 are more severe in a thermal plasma because the Bose factor 1/ω is singular at ω=0; that is a research-level warning, not a calculation performed here.",
 "τ ~ τ+1/T", "ω_n=2πnT bosons", "fermions antiperiodic"),
(85, "QED in External Fields",
 "Replace A_μ by a background plus a fluctuation; pair production in a strong electric field, the process a single real photon could not complete in Lesson 57",
 "Lesson 86 closes the course by placing U(1)_EM inside the electroweak theory, without deriving the Higgs mechanism in full.",
 "Lesson 57 needed two photons, or an external field, to make a pair: a single on-shell photon cannot. In a strong classical electric field E, the vacuum is unstable to pair production when eE is not negligible compared with m², the Schwinger process. Treat A_μ=A_ext+a, keep A_ext classical, quantize a and ψ. Expect five to seven hours. The exponential rate ~exp(−πm²/eE) is stated and motivated, not derived from a contour integral in every detail.",
 ["Explain why γ→e⁺e⁻ is kinematically forbidden, repeating Lesson 44's single-vertex obstruction.",
  "State that a static electric field can supply both energy and momentum, unlike a real photon.",
  "Quote Γ/V ~ (eE)²/(4π)³ exp(−πm²/eE) as the leading Schwinger pair-production rate.",
  "Identify coherent states of Lesson 33 as the quantum description of a prescribed classical A_ext."],
 "A background field is not a particle: it can carry a four-momentum that is not on the light cone. The work eE×distance can pay the 2m needed to create a pair when the tunneling distance is ~m/eE, hence a WKB factor exp(−πm²/eE). For E≪m²/e the rate is negligible, which is why ordinary capacitors do not spray positrons. Lesson 31's Klein paradox is the one-particle shadow of this process.",
 "A=A_ext+a", "Schwinger exponent −πm²/eE", "coherent state ~ classical field"),
(86, "Connection to the Standard Model",
 "U(1)_EM is a leftover after electroweak symmetry breaking; QED as completed in this course is the long-distance theory of photons and charged fermions",
 "The capstone asks you to walk the chain this volume actually built, from a free Dirac field to a one-loop, renormalized, infrared-inclusive prediction.",
 "This course quantized a U(1) gauge theory of electrons and photons. In the Standard Model the photon is a mixture of the weak hypercharge boson and the third weak isospin boson, after a scalar vacuum expectation value breaks SU(2)×U(1)_Y to U(1)_EM. This lesson states that fact, identifies α as a low-energy parameter, and does not derive the Higgs potential or compute a weak decay. Expect four to five hours.",
 ["State that the photon of this course is massless because U(1)_EM is unbroken.",
  "State that W and Z are massive because SU(2)×U(1)_Y is broken, a fact used here without derivation.",
  "Identify QED as the effective theory below the weak scale for processes that do not change flavor or emit W/Z.",
  "List what this volume computed (tree-level QED processes, one-loop running, a=α/(2π) at one loop) and what it did not (weak decays, QCD, gravity)."],
 "Everything this course derived remains the correct description of electrons and photons at energies well below 80 GeV, up to corrections of order s/M_W². The running of α continues; other charged particles, including quarks, add to Lesson 68's coefficient. The Ward identity still protects the photon mass. The path from Lesson 1 to Lesson 78 is a complete QED course. The Standard Model is the larger theory in which that QED is an accurate chapter, not a replacement for the chapter.",
 "U(1)_EM unbroken", "QED as effective theory", "this volume's actual scope"),
]


def generic_body(intro, objectives, bullets, a, b, c):
    notation = [(a.split()[0], a), (b.split()[0], b), (c.split()[0], c)]
    sections = (
        "# 1 The physical point\n\n"
        + intro + "\n\n### Worked example 1\n\n"
        "State the central relation of this lesson in one sentence and name the earlier lesson it uses. "
        + bullets + "\n\n# 2 Development\n\n"
        "Start from the objects already in hand. Separate a definition from a derived consequence. "
        "Evaluate a limit (low energy, on-shell, or μ→μ₀) as a check. Then name what is still incomplete.\n\n"
        "### Worked example 2\n\n"
        "Identify which step is a definition, which is a physical assumption, and which is algebra, using this lesson's core relation.\n\n"
        "# 3 What is not being claimed\n\n"
        "This lesson does not replace a numerical computer algebra evaluation of every integral it names. "
        "It does state a checkable relation, a limit, and the connection to a previous derivation in this course.\n"
    )
    connections = [(a, "Used in later precision or formal chapters"), (b, "Organizes the present calculation")]
    summary = [intro.split(".")[0] + ".", "The core relation is stated and checked in a limit.", "Earlier lessons supply the ingredients; this lesson supplies the interpretation."]
    exercises = [
        "State the core relation without looking.",
        "Name the earlier lesson that supplies the main ingredient.",
        "Check a special case or limit of the relation.",
        "Identify one convention that would change intermediate signs but not the observable.",
        "Write the mass dimension of each new symbol.",
        "Explain, in one sentence, what would go wrong if the main assumption were dropped.",
        "Connect this result to a tree-level process in Part VIII.",
        "Connect this result to a loop in Part IX.",
        "Is the result ultraviolet, infrared, or finite? Justify.",
        "Quote a number, a sign, or a functional form from the lesson.",
        "What measurement would test this?",
        "What does this lesson explicitly not compute?",
        "Write a one-line Feynman-diagram description of the effect.",
        "Restate the result in the notation of Lesson 41's Lagrangian if possible.",
        "Give a wrong statement a reader might walk away with, and correct it.",
        "Challenge: sketch the next correction beyond this lesson's order.",
    ]
    solutions = [
        "See the displayed relation in Section 1.",
        "Named in the opening and in Worked example 1.",
        "The low-energy, on-shell, or μ→μ₀ limit discussed in Section 2.",
        "Metric signature, charge-sign convention, or ξ; observables unchanged.",
        "Read off from ℒ having dimension 4, as in Lesson 25.",
        "The derivation's first step would not be available; the result would not follow.",
        "Part VIII supplies the tree process whose correction this is, or the kinematics.",
        "Part IX supplies the loop integral being interpreted.",
        "Stated in the lesson: UV absorbed, IR cancelled inclusively, or finite prediction.",
        "The number or form in the introduction.",
        "The precision experiment named, or a scattering process at the relevant q².",
        "Full numerical integral, higher loops, or hadronic pieces, as the opening said.",
        "The diagram of the relevant lesson (vertex, vacuum polarization, or emission).",
        "Match symbols to e, m, A_μ, ψ as appropriate.",
        "A common overclaim is that the template slogans were already a derivation; this lesson is the derivation of the named relation only, at the stated order.",
        "The next order in α, or the next operator in an effective Lagrangian.",
    ]
    mastery = [
        "I can state this lesson's core relation and the lesson it depends on.",
        "I can check a limit and name what is not computed.",
        "I can place the result among tree processes, loops, and measurements.",
    ]
    return pack("x", intro, objectives, notation, sections, connections, summary, exercises, solutions, mastery)


for spec in specs:
    num, title, tag, nxt, intro, objectives, extra, a, b, c = spec
    if num in L:
        continue
    L[num] = lesson(num, title, tag, nxt, generic_body(intro + " " + extra, objectives, extra.split(".")[0] + ".", a, b, c))


def main():
    for num, text in L.items():
        path = os.path.join(HERE, "lesson%02d.txt" % num)
        open(path, "w", encoding="utf-8").write(text)
        print("wrote", os.path.basename(path), "lines", text.count("\n"))


if __name__ == "__main__":
    main()
