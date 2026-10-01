# PART EIGHT — Following an Electron

---

## 28. The Equation Behind the Conversation

Here is the equation the book has been walking toward. If a symbol is new, keep the sentence in front of it. The matrices can stay unread. This part is heading for one coupling, and that coupling shows up again in a wire.

The central object in modern quantum field theory is called the Lagrangian density, and for quantum electrodynamics it can be written as

*L_QED = ψ̄(iħc·γᵘD_u − mc²)ψ − (1/4μ₀)F_uvF^uv*.

That looks like a machine built specifically to intimidate beginners. Take it apart, though, and there are really only two major pieces here. (The bar over *ψ* and the *γᵘ* matrices are bookkeeping this book won't otherwise need — they exist because the electron is relativistic and carries spin, which makes *ψ* here a richer object than the plain amplitude-and-phase *Ψ* from Chapter 5, though it plays the same conceptual role.) The first term describes the electron field on its own. The last term describes the electromagnetic field on its own.

And sitting between them, doing essentially all of the conceptual work this book cares about, is a single small modification hidden inside the symbol *D_u* — the *covariant derivative*:

> **Equation (6).** The covariant derivative:
> *D_u = ∂_u − (iq/(ħc))A_u*

That one substitution is where the entire electromagnetic interaction lives. Rather than taking an ordinary derivative of the electron field — a plain statement of how the field changes as you move through spacetime — the theory uses a derivative that already has the electromagnetic potential baked into it. That potential enters directly into the operation of comparing the electron field at one point with the field at a neighboring point, rather than getting appended afterward as a correction. This is the field-theoretic version of the phase story told since Chapter 1, now written in the actual language professional physicists use.

Sit for a moment with what actually makes a derivative "covariant." An ordinary derivative asks how a quantity changes as you move. A covariant derivative asks how a quantity changes as you move, *once you've accounted for the fact that comparing it at two different points already requires a gauge connection to make the comparison meaningful in the first place* — precisely the connection introduced geometrically in Chapter 21. Suppose an electron's quantum state carries a certain phase at one location. Move to a neighboring location and ask how that phase compares.

In ordinary mathematics, you'd simply subtract. In a gauge theory, the comparison has to respect local phase symmetry, and the electromagnetic potential is the object that supplies the necessary correction. The covariant derivative therefore contains both an ordinary rate of change and an electromagnetic phase connection, folded into one operation — which is why gauge theory is so much more than a fancy way of rewriting Maxwell's equations. It says that electromagnetism is built into the very grammar of comparing charged quantum states from point to point, not pasted onto quantum mechanics as an afterthought.

Expand that covariant derivative inside the Lagrangian, and an interaction term falls straight out. Substitute the definition of *D_u* back into the electron term: the ordinary-derivative piece reproduces the free electron equation you'd have without any field at all, and the piece proportional to *A_u* is left over. That leftover piece is new — it's the interaction term:

*L_int = qψ̄γᵘA_uψ = j·A*,

*where j is the electromagnetic current, q times the same combination of electron fields.*

The *c* in Equation (6)'s denominator is what lets that substitution come out even, with no leftover factor of *c*. The phase formulas in the rest of this book are the same coupling written in units where the speed of light equals 1. Set *c* = 1 in Equation (6) and the potential term is *(iq/ħ)A_u*. The flux quantum, the Wilson loop, and the central bridge *J ∝ ħ∇θ − qA* are that reduced form: multiply the connection by *ħ* and the electromagnetic piece is *qA*, standing beside the phase gradient exactly as Equation (8) writes it. One coupling, two conventions.

There it is — the same relationship Chapter 24 already introduced: current, coupled to potential, producing an interaction. Because the action comes from integrating this Lagrangian over all of spacetime, this interaction term contributes directly to the action; because the action determines quantum phase, it contributes directly to phase. The entire conceptual chain built across the last few chapters compresses into one line of actual formalism: *j·A* feeds the action *S*, and *S* feeds the phase factor *exp(iS/ħ)* that determines how every possible history interferes with every other.

This is the interaction term of QED, in a form where the algebra can be checked. The field term beside it, −(1/4μ₀)*F_uvF^uv*, is the standard SI density for the free electromagnetic field. This book does not expand *F* into **E** and **B**. The indices are summed in the usual way, one up and one down. What the substitution checks is the interaction. Every earlier chapter's talk of phase and potentials was pointing directly at this equation's central structure the entire time — not gesturing at quantum field theory from a respectful distance.

The Lagrangian splits cleanly into a matter sector, an electromagnetic sector, and the interaction connecting them (*matter + electromagnetism + interaction*), and that three-part organization is what makes the whole framework so powerful: it lets you calculate electron scattering, photon emission and absorption, corrections to the electron's magnetic moment, vacuum polarization, and a vast range of other experimentally testable phenomena, all from the same handful of terms. What's philosophically striking is that the interaction shows up here as a term in the action, not a classical force sitting between two otherwise separate sectors: the action reshapes the quantum amplitude, the amplitude interferes with other amplitudes, and observable probabilities emerge only at the end of that chain.

The old force picture survives this encounter, just not intact — call it *absorbed*, a useful word to hold onto, since absorbed is not the same thing as discarded. The classical force remains exactly where it always was, as a limiting description; the quantum theory tells you, for the first time, what's actually sitting underneath it.

---

## 29. Feynman's Diagrams Become Less Mysterious

With the interaction term from the last chapter in hand, Feynman diagrams finally have somewhere real to live. A diagram works as a graphical bookkeeping system for the terms that appear when you expand a quantum amplitude in powers of the electromagnetic coupling, never as a literal picture of the universe going about its business: start from the interaction term, expand, and each resulting term corresponds to some particular combination of interactions, which can then be drawn. The diagrams track which particles enter and leave, which interactions occur, how momentum moves through the process, and which mathematical factor belongs to each piece of the calculation.

A wavy line conventionally represents an electromagnetic propagator; a straight line, a fermion propagator; a vertex, a single factor of the interaction. But the whole diagram remains, from beginning to end, a piece of an amplitude calculation — not a microscopic movie of what physically happened, frame by frame.

That distinction may be the single most important thing any popular account of QED can convey: a Feynman diagram reads closer to a sentence in a specialized mathematical language than to a photograph, and Feynman's own path-integral intuition sits directly underneath it: the theory is fundamentally about amplitudes, diagrams organize the contributions to them, and the classical-sounding story of particles trading forces back and forth emerges only after the calculation is finished and reinterpreted in the appropriate limit.

Take the simplest possible case to see this concretely: two electrons approaching each other and scattering. Nothing about the setup looks exotic — two particles in, two particles out, a detector recording where they ended up — and yet explaining it properly drags nearly everything this book has covered onto the same stage at once: quantum phase, the electromagnetic potential, the field, photons, interference, relativity, the distinction between real and virtual photons, and the classical Coulomb force waiting patiently at the very end of the calculation. At lowest order in the electromagnetic coupling, the two electrons exchange a single internal electromagnetic propagator, conventionally drawn as a photon line connecting two vertices.

The warning from Chapter 9 bears repeating here, because this is the picture that tempts people to forget: that internal line is an internal element of the amplitude, representing the electromagnetic propagator connecting two interaction events mathematically — not a small photon flying from one electron to the other.

![Figure 6. Two electrons scattering, drawn as a Feynman diagram: each vertical line is one electron, and the wavy line connecting them is the internal photon line — a term in the calculation, not a detectable particle in flight.](fig06_feynman_scattering.png)

This is where the direct-action perspective from Part Five becomes useful again, not just provocative. Instead of picturing an independent messenger leaving particle A, traveling through space, and arriving at particle B, you can think in terms of the mathematical relationship connecting the two interaction events — precisely what a propagator is. In a field formulation, the field is an explicit dynamical degree of freedom carrying that relationship; in a direct-action formulation, the same kind of relationship can be organized more directly between the two currents involved, without an intervening field required to carry it.

The mathematics can be rearranged this way. But the caution from Part Five still applies with full force: the fact that an interaction *can* be represented through a propagator does not license the jump to "therefore the electromagnetic field is definitely not real." That conclusion simply does not follow from the premise. A propagator tells you how a disturbance at one event contributes to another (a mathematical answer to the question *if something happens here, how does that possibility contribute there?*) without requiring you to imagine a little object physically flying between the two endpoints.

Whether the corresponding field degrees of freedom are ontologically fundamental remains a separate, harder question, kept honestly open here rather than quietly resolved for the sake of a tidier ending.

---

## 30. The Classical Coulomb Force Emerges

Now take the two-electron scattering process from the last chapter and slow it down: two charges, moving slowly, separated by a distance large compared with their quantum wavelengths. The full relativistic QED calculation for this process is complicated. But in this low-energy limit, the dominant piece of the interaction reduces to something reassuringly familiar — the Coulomb potential energy, from which the ordinary Coulomb force follows in the usual way, *F = −∇V*:

> **Equation (7).** The Coulomb potential energy and force:
> *V(r) = q₁q₂/4πε₀r*,
> *F = (q₁q₂/4πε₀r²)r̂*.

There is the old friend, sitting exactly where every introductory physics course leaves it. What's changed is not the formula but the chain of reasoning that now sits underneath it: quantum fields, an interaction term, a scattering amplitude, a low-energy limit, an effective potential, and only then the classical force, in that order. The classical law wasn't wrong so much as incomplete — an important distinction, because "incomplete" doesn't mean "approximately true only by luck."

A classical force is not literally the average of many tiny quantum forces computed one particle at a time; rather, in the appropriate semiclassical regime, observable motion is governed by an effective action derived from the full underlying quantum theory, and that effective action's equations of motion reproduce ordinary classical dynamics exactly. The general pattern (*quantum theory → effective action → classical equations*) is the same conceptual hierarchy this book keeps finding everywhere it looks, and it means the everyday electrostatic potential energy taught in every introductory course was never fundamental in the same sense as the underlying QED interaction.

It is a remarkably, almost suspiciously accurate effective description — accurate enough that an engineer can design a working circuit, or an astronomer model a plasma, without ever calculating a single photon.

But the phase chased since Chapter 1 has not quietly left the building just because the final answer looks like a classical force. The full scattering amplitude computed by QED is complex-valued, carrying both size and phase, and different quantum contributions to that amplitude can carry different phases that interfere with each other before anyone squares the result to get a measurable probability. A force only ever tells you how a single classical trajectory bends. A quantum amplitude tells you how every alternative history combines — and the electromagnetic interaction's real job, underneath the whole calculation, is reshaping that phase structure among the alternatives.

The word "feels" smuggles in more classical imagery than the physics supports: an electron does not experience a small arrow of force in any literal sense. Its quantum state evolves according to the electromagnetic interaction, and only when that state is sufficiently localized, in the regime where a classical description becomes an excellent approximation, does its expected motion end up looking like the Lorentz force acting on a definite trajectory. A more honest replacement for "the electron feels a force" might be: *the electromagnetic interaction reshapes the electron's quantum amplitude, and the force law is the classical shadow that reshaping casts.*

A shadow is a useful word here — real, measurable, usable, and yet never containing the full three-dimensional information of the object casting it. Classical mechanics is that kind of shadow, cast by quantum dynamics onto the regime where a trajectory becomes a good approximation, and the reason the classical equations look so much simpler than the full QED calculation underneath them is interference itself: when phases vary wildly between very different possible histories, most of those histories cancel each other out, and a narrow, structured, classical-looking subset survives to dominate the observable result.

Send that same electron through a magnetic field instead of merely toward another charge, and a subtlety that's been lurking since Chapter 7 finally has to be confronted head-on. Classically, the magnetic part of the Lorentz force bends the electron's path without changing its speed, as Chapter 26 described. Quantum mechanically, the vector potential enters directly into the relationship between phase gradient and momentum, and the *canonical* momentum associated with the wave function's phase turns out not to be, on its own, the same thing as the *mechanical* momentum of the moving charge. The two differ by exactly the electromagnetic contribution already introduced in Chapter 7:

*p_mechanical = p_canonical − qA*.

That difference is essential to how quantum mechanics works in the presence of electromagnetism, not a bookkeeping nuisance to be tolerated and then forgotten. The canonical momentum is the quantity naturally associated with translations in the mathematical description of the system; the mechanical momentum is what corresponds to the electron's actual physical motion; and the vector potential is the bridge connecting the two. This is one more reason the potential earns the central role Mead insists on giving it: the potential enters directly into the canonical structure of the quantum theory itself, not merely as a quantity you differentiate to recover *E* and *B* after the fact.

Because momentum is tied to the gradient of phase, phase once again sits at the very center of the relationship.

With this distinction properly in hand, the Aharonov–Bohm effect can finally be given the treatment every earlier mention of it has been promising. Picture the classic setup again: an electron beam split into two paths that pass on opposite sides of a shielded solenoid, then recombined on a screen. An electron's phase carries a contribution from the electromagnetic potential integrated along its path, and for two different paths reaching the same destination, the phase *difference* between them reduces, via Stokes' theorem as in Chapter 3, to the magnetic flux enclosed between the two paths — so the interference pattern where they recombine shifts with that enclosed flux, regardless of whether the magnetic field is actually zero everywhere the electron travels.

Nothing about this requires imagining the electron being pushed by a force in a region where no force exists. The quantum amplitude simply remembers the electromagnetic connection it was transported along, in the strict mathematical sense of Chapter 21. It is tempting to describe this by saying the electron somehow "knows" the flux enclosed by its path, as though it were carrying a tiny map — but it isn't. The amplitude evolves according to strictly local laws involving the potential at each point; only when two amplitudes, having taken different routes, are finally compared does the integrated phase difference reveal information about the flux enclosed between them.

Nothing has to communicate instantaneously across the loop for this to happen — global information here emerges from purely local dynamics plus the topology of the two paths, fully compatible with relativity, since no controllable signal ever needs to cross the loop faster than light for the interference pattern to shift.

All of this sharpens a distinction: a force changes momentum; a phase changes interference; these are not the same concept, even though they become closely related in the classical limit. The electromagnetic interaction contributes to the action, the action shapes the phase, and only in the semiclassical limit — where a stationary-phase condition picks out one dominant family of histories, as Chapter 25 described — do the resulting equations of motion take the form of a force at all. The force turns out to be what the deeper phase dynamics looks like once you insist on viewing it through classical variables, not the fundamental quantum object underneath electromagnetism.

---

## 31. Now Add Many Electrons

The single-electron story from the last three chapters is only the opening act. Put a great many electrons together, and the quantum state now lives in a configuration space whose size multiplies out of all proportion to the number of particles involved, which sounds, at first, like it should make any hope of a simple phase-based picture completely hopeless. Instead, something remarkable tends to happen under the right conditions: interactions can organize the system, the electrons can settle into a collective state, and new effective variables emerge that were nowhere to be found in the description of any single electron on its own.

Superconductivity, once again, is the clearest laboratory for this. The microscopic quantum complexity hasn't gone anywhere (every electron is still there, still obeying the full machinery this Part has just spent three chapters building), but the relevant low-energy behavior can be captured almost entirely by one collective phase. This is where the book's two central strands finally meet in the most direct way available: Feynman supplies the microscopic quantum framework in full technical detail, and Mead asks what happens once quantum coherence becomes collective and macroscopic.

The answer has less to do with "the microscopic theory switching off" than with the microscopic theory organizing itself into new effective degrees of freedom, without abandoning a single one of its underlying principles.

Here is the conceptual pivot that makes this precise. For one quantum particle, phase belongs to that particle's individual wave function. For a coherent many-body state, phase becomes a *field* in its own right — a quantity defined smoothly across the whole material, as Chapter 5 introduced with *Ψ(r) = √n(r)e^iθ(r)*. Once that transition happens, something genuinely new has entered the picture: a quantum phase that used to be a private property of one microscopic amplitude has become a spatially extended, macroscopic, dynamical variable — its gradients corresponding to currents, its time evolution corresponding to voltage, its winding around a loop capable of producing quantized flux.

And the combination that governs this collective dynamics is never the bare phase gradient alone; it is the gauge-invariant combination already familiar from Chapter 7 and Chapter 30, now describing a macroscopic supercurrent rather than one electron's momentum:

*J ∝ ħ∇θ − qA*.

This is the macroscopic version of the minimal-coupling structure from the covariant derivative that opened this Part, written in the units where the speed of light is 1. The collective phase and the electromagnetic potential cannot be fully understood in isolation from each other: the potential is what directly enters the phase dynamics, and the ordinary electric and magnetic fields are simply what you recover from that potential afterward, as in the microscopic theory. Integrate this relation around a closed superconducting loop, demand that the phase return to an equivalent value after the full circuit, and, using Stokes' theorem as in Chapter 3 and Chapter 21, a quantization condition for the enclosed magnetic flux falls out directly.

A macroscopic magnetic phenomenon, trapped inside a loop of wire you could hold in your hand, turns out to be controlled entirely by a microscopic quantum requirement: the phase simply has to close consistently on itself.

The word "collective" needs a precise meaning here, since it gets used loosely elsewhere. A collective variable is a variable describing an *organized pattern* among a great many microscopic degrees of freedom, not the outcome of summing many individual variables together the way a total weight sums individual weights. A phase field in a superconductor is collective because it captures the coherent order of the entire many-body state, in the same way a fluid's velocity field is collective because it captures the organized motion of an enormous number of molecules, and much as a classical electromagnetic field can be collective because it captures the organized state of the underlying electromagnetic degrees of freedom.

This is why emergence, throughout this book, has meant organization, not mere averaging — and organization is what makes new physical laws possible.

---

## 32. The Book's Central Bridge

One relationship, both ends of the story. A single electron in the full theory, and a supercurrent in a wire, are the same combination of phase gradient and potential:

> **Equation (8).** The book's central bridge:
> *J ∝ ħ∇θ − qA*

In the units of Chapter 28, where the speed of light is set to 1, this is the combination inside the covariant derivative of the full QED Lagrangian at the microscopic scale, and inside the supercurrent of a coherent quantum condensate at the macroscopic scale.

This is the book's central *bridge*, not a claim that electromagnetism has a single master equation. A particle physicist would reach for the covariant derivative or the QED Lagrangian. A circuit physicist would reach for this. In those units, they are looking at the same coupling.

![Figure 7. With the speed of light set to 1, the combination ħ∇θ − qA is the coupling inside one electron's covariant derivative and inside a coherent supercurrent — the book's central bridge, at both ends of the story.](fig07_two_scales.png)

One branch of this equation runs downward: charged matter, quantum fields, the covariant derivative, the interaction term, Feynman diagrams, the low-energy Coulomb limit, the classical force. The other branch runs upward: coherent many-body matter, collective phase, the gauge-invariant combination of phase gradient and potential, flux quantization, a macroscopic electromagnetic device sitting on a laboratory bench. The two branches meet in exactly the same expression, and that meeting is the merger this entire book has been assembling piece by piece. Not because Mead and Feynman secretly wrote down the same theory under different names.

Not because the electromagnetic field turns out to be a polite fiction. Not because everything reduces, in the end, to nothing but phase. But because phase, potential, field, photon, and collective coherence are genuinely connected levels of one electromagnetic story — connected specifically through this equation, which is the closest thing this book has to offer as its single organizing claim.

Now that the equation is finally on the page, one direct question follows: why doesn't the everyday world behave like a quantum interference experiment, if all of this machinery is really running underneath it? The answer is coherence, and its fragility. A macroscopic system is constantly interacting with its environment: thermal motion, scattering, vibration, electromagnetic noise, and those interactions rapidly entangle the system with everything around it, destroying the delicate phase relationships that large-scale quantum interference requires. That process, decoherence, is why an ordinary circuit behaves classically.

But coherence can survive when a system is sufficiently isolated and carefully controlled: superconductors, trapped ions, cold atomic gases, an entire modern industry of quantum technology built essentially on the art of protecting the coherence that ordinary environments destroy. The classical world is classical because the relevant quantum information is usually inaccessible, scrambled, or averaged into irrelevance — quantum mechanics never switches off inside it — and the moment that information is deliberately protected, the quantum world reappears, fully intact, exactly where the central bridge says it should.

The classical electromagnetic field is not being demoted to an illusion here. Emergent quantities can be entirely real: a vortex in a superfluid is real, a sound wave is real, temperature and pressure are real, and a classical electromagnetic field is real in the fullest operational sense available to physics: it predicts measurable forces, energy transfers, radiation pressure, and interference, all correctly. What changes is only the field's relationship to the deeper theory underneath it.

The choice was never between "the field is a literal substance" and "the field is imaginary"; there was always a third option, the one this book has been building toward the entire time: the field is a physically meaningful degree of freedom within its own effective regime, whose deeper description is supplied by quantum theory — a theory in which, in its standard formulation, the electromagnetic field remains fully and irreducibly quantized.

Mead pushes further than this, questioning whether independent field degrees of freedom deserve to be called fundamental at all, at least for coherent systems, a stronger claim, and one treated here with real caution rather than adopted wholesale, since standard QED's independent electromagnetic degrees of freedom have consequences no collective reformulation gets to simply wave away: photons are not optional, radiative corrections are not optional, vacuum polarization is not optional. The honest way to hold both truths at once is to recognize that the merger being offered here isn't symmetric.

Feynman's QED supplies the microscopic relativistic framework nothing else can replace; Mead supplies a radically phase-centered way of seeing collective electrodynamics that QED's own formalism tends to leave invisible; gauge theory explains why the two connect at all. Flattening any of them into one equation pretending to be the whole truth would misrepresent all three — except, perhaps, for the one this chapter has finally written down, which claims no more than to be the clearest evidence available that a single continuous thread really does run from one electron's phase to the current in a wire, not the final word on what electromagnetism is.

A theory, in the end, is as much a choice about which variables deserve to be treated as the important ones as it is a collection of equations — Newton chose positions and momenta, Maxwell chose fields, Einstein chose spacetime geometry, quantum mechanics chose amplitudes, Feynman chose histories and phase, gauge theory chose connections and symmetry, and Mead chose collective quantum phase and the electromagnetic potential. Each choice changes what becomes obvious and what stays hidden. The universe does not arrive labeled with instructions about which variable is secretly the fundamental one.

Useful variables get discovered by finding descriptions that compress the physics without losing what matters — and sometimes the deepest available insight is not a new equation at all, but the recognition that the old question was being asked in the wrong variables all along. That recognition is a great deal of what doing physics consists of, far more than a footnote to it.
