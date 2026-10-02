# PART FIVE — The Field That May Not Be a Thing

---

## 15. What If the Field Isn't Independent?

Physics has a dangerous habit. Someone invents a useful mathematical object. It works. People calculate with it. Other people learn to calculate with it. Textbooks get written about it. And somewhere along the way, everyone forgets that the object was invented at all — it starts to feel like a piece of furniture that was simply sitting in the universe, waiting to be discovered rather than constructed.

Fields are unusually susceptible to this treatment, and the electromagnetic field most of all. It is so deeply embedded in how physics gets taught and practiced that asking whether it's an independent piece of physical furniture, rather than a useful description, can sound almost heretical. But physics has taught this lesson to itself repeatedly, in other contexts, without much controversy. Temperature is real, measurably real, and yet there is no tiny substance called temperature that flows from a hot object into a cold one; temperature is a statistical property of a huge number of molecular motions, not itself one more ingredient added to the mix.

Pressure is real as a macroscopic description of a gas, but there is no separate microscopic material called "pressure" occupying the spaces between molecules. A center of mass is real and enormously useful for solving mechanics problems, but there is no additional particle actually sitting at that point in space.

Dressed up to sound profound, *is the field real?* is still the wrong question here. The sharper one: does the electromagnetic field require independent degrees of freedom of its own, separate from the charged matter it interacts with, or is talking about "the field" more like talking about temperature: an extremely useful description of something that, underneath, is really just charged matter and its relationships?

The standard formulation of quantum electrodynamics gives an unambiguous answer: yes, independent degrees of freedom. The electromagnetic field is quantized in its own right; its excitations are photons; the theory contains electromagnetic degrees of freedom in addition to, not instead of, the degrees of freedom belonging to charged matter. This framework is spectacularly successful, tested to the same absurd precision Chapter 9 already flagged, and nothing in this book is arguing otherwise.

But there is another possible way to organize the same physics, and dismissing it on reflex would be premature. Perhaps electromagnetic interactions can instead be formulated directly as relationships between charged particles — full stop, no separate mediating substance required — with the field appearing only as a convenient effective intermediary rather than as an independently existing dynamical entity. This is the radical direction pursued by John Wheeler and Richard Feynman, well before the Feynman diagrams of ordinary QED made him famous for something else entirely.

Their motive going in was simplification, not mystification: they wanted to know whether an entire independent substance, complete with its own energy, momentum, and dynamics, was really necessary, or whether it was scaffolding that had outlived its usefulness.

---

## 16. Wheeler and Feynman: The Universe Talks Back

Classical electrodynamics has always carried an uncomfortable, easy-to-overlook feature. A charged particle produces an electromagnetic field. That field then acts back on the very particle that produced it. Fine so far — except, what is the mechanism by which a particle acts on itself? An accelerating electron radiates; the radiation carries energy and momentum away from it; the electron correspondingly experiences a recoil, a "radiation reaction" force resisting its own acceleration — the same effect, on a much smaller scale, that makes a radio transmitter's antenna require more driving power to broadcast at higher power, since some of that power has to cover the antenna's own resistance to accelerating the charges it's pushing back and forth.

Press for a purely mechanical account of what's happening at the level of a single electron, though, and the questions multiply quickly. How does a particle exert a force on itself without becoming a logical tangle? Does the field possess its own independent energy and momentum, held apart from the particle's? And if so, where exactly did those additional degrees of freedom come from in the first place?

Where this idea actually came from matters, because it did not arrive as an armchair speculation. John Wheeler was, at the time, a young Princeton professor; Richard Feynman was his graduate student, working through this radiation-reaction puzzle with him starting in the early 1940s, alongside the path-integral work that became his actual doctoral thesis^4; the absorber-theory papers followed a few years later^5, not long before quantum electrodynamics proper made him a household name in physics.

The absorber theory was, quite literally, where Feynman learned to distrust an explanation that merely sounded plausible until he had pushed the mathematics hard enough to see whether it held together, a habit of mind that shows up constantly in the rest of this book. Wheeler and Feynman explored a strikingly different formulation in response. Rather than treating the electromagnetic field as an autonomous entity with its own life, they considered electrodynamics as a direct interaction between charges — full stop — in which the response of the rest of the universe plays an essential, load-bearing role in producing both radiation and the reaction force associated with it.

Concretely: in this time-symmetric formulation, every accelerating charge's contribution is represented as a combination of two solutions to the same equations — one retarded, propagating forward in time in the ordinary way, and one advanced, propagating backward in time — not two physical waves a charge literally sends out, but two mathematical pieces of one description. Sum the responses of every other charged particle in the universe that will ever go on to absorb that radiation, and the advanced pieces cancel one another almost perfectly, leaving exactly the forward-traveling radiation and the recoil force observed.

This approach, known as absorber theory, is subtle, has a specific technical domain of validity, and has a history far more nuanced than a slogan can capture. It should not get flattened into "fields don't really exist": that would be both too simple and, worse, scientifically misleading about what the theory actually claims.

There's a different lesson here, and a more general one. A theory can sometimes be reformulated so that what looks, in one description, like an independent mediator carrying influence from place to place, becomes instead a direct relationship among sources and their responses in another description — with no mediator required at all. That is a profound possibility, and it resonates unmistakably with a claim closely associated with the Wheeler–Feynman program: there need not be a separate field, carrying its own independent degrees of freedom, sitting between two charges as an additional physical substance in its own right.

That viewpoint becomes especially provocative once set beside the quantum-phase picture built so far. The electromagnetic potential already enters directly into the phase of charged matter. The familiar fields can be derived from that potential. The potential itself can, in turn, be related to its sources through Green's functions, as Chapter 8 described. And the direct-interaction formulation asks whether the electromagnetic degrees of freedom, at bottom, might be nothing more than relationships between charged systems, expressed in a particularly compact language. Seen this way, Mead's approach is one more voice in a much older conversation about the most economical way to describe how charges talk to each other — not an isolated eccentricity within condensed matter physics.

![Figure 14. Retarded and advanced are two pieces of one solution, drawn here as arrows in time. Sum the response of every charge that will absorb the radiation, and the backward pieces cancel. What remains is the forward radiation and the recoil a detector actually sees.](fig14_absorber.png)

Sound needs air. Take the air away and the conversation stops, because a sound wave is a disturbance of a material. Light does not work that way. It crosses a vacuum, and the standard description of that fact is the quantized electromagnetic field. This part is not reviving the nineteenth-century ether, the invisible mechanical medium that was discarded for good reason.

The useful question is which description makes which physics easy to see. High-energy scattering belongs to QED. A coherent superconductor belongs to the collective phase. Radiation reaction is where the direct-action account earns its keep. None of the three is obliged to do the other two jobs. Chapter 17 is where that limit shows up in the laboratory: a beam of light carries energy and momentum whether or not anyone has decided the field is a substance. Absorber theory, as this chapter has it, cannot reproduce QED's radiative corrections, vacuum polarization, or particle creation. If the circuit is the destination, Chapter 19 is next.

---

## 17. Radiation Is Where Things Get Serious

A beam of light carries energy and momentum. It can push a solar sail. It knocks electrons out of a metal one photon at a time. The last two chapters made an independent field sound optional: charges interact, phases shift, familiar fields emerge downstream, coherence makes phase visible. The beam is where that idea gets expensive.

There are, in fact, several different questions tangled together inside the single word *radiation*, and keeping them apart matters. One is a classical question: how does an accelerating charge come to produce electromagnetic radiation in the first place? A second is a quantum question: how does matter emit and absorb individual photons? A third is a foundational question, and the hardest of the three: does the mere existence of radiation require the electromagnetic field to possess independent degrees of freedom of its own? These questions are related, but they are not the same question wearing three hats.

The first is answered by Maxwell's equations. The second requires the full machinery of quantum electrodynamics. The third is a question about how the underlying theory ought to be formulated — and keeping it separate from the other two prevents a common and tempting mistake: assuming that because a particular mathematical description is enormously useful, its individual ingredients must automatically be the fundamental furniture of the universe. It equally guards against the opposite mistake — assuming that because some alternative formulation is philosophically appealing, it has therefore already reproduced everything ordinary QED accomplishes.

It hasn't, not automatically, and radiation is where that gap becomes impossible to paper over.

Start with the classical picture, which is illuminating on its own terms. A charged particle moving at constant velocity carries its electromagnetic configuration along with it, unchanging. Accelerate the particle, though, and the surrounding electromagnetic disturbance cannot rearrange itself everywhere instantaneously — information about the changed motion propagates outward at a finite speed, the speed of light. Far enough from the accelerating charge, that changing disturbance separates cleanly from the near-field structure clinging to the particle and propagates outward on its own, as radiation, indefinitely, whether or not anything is left nearby to absorb it.

This is the classical theory's way of insisting that radiation is not simply "the electric field of a moving charge, viewed from a distance" — no minor technical footnote, but a genuinely independent propagating disturbance, carrying its own energy and its own momentum, which is why classical electromagnetism assigns the field an energy density of its own, and an energy flux (the rate at which energy flows from place to place) given by the Poynting vector:

> **Equation (3).** Electromagnetic energy density and flux:
> *u = ½(ε₀E² + B²/μ₀)*,
> *S = (1/μ₀)E×B*.

These equations trace directly back to the conservation of energy and momentum in classical electrodynamics rather than to any arbitrary convention, and any formulation that wants to do without an independent field has real, non-negotiable work ahead of it: it has to reproduce this same energy-and-momentum accounting some other way, not declare the question closed by fiat.

This is why Mead's treatment counts as a provocative physical claim, not just a poetic one. If the field is not an independent dynamical entity, then whatever we conventionally call "field energy" has to be understood, in full, as a property of the interacting matter and its collective dynamics — a much stronger claim than the earlier, gentler observation that potentials are useful. It is a specific claim about where the physical bookkeeping lives.

And it demands a distinction this book intends to hold onto carefully for the rest of its argument: there is a real difference between saying *the field formulation stores energy in the field*, which is a precise statement about how one particular formulation is organized, and saying *the energy literally belongs to an independent substance called the field*, which is an ontological claim about what ultimately exists. The first is uncontroversial. The second is the question this Part is trying to take seriously rather than assume.

---

## 18. Where Is the Energy?

Energy remains one of the best available tests of any physical picture, if only because it has to be conserved no matter how you tell the story. Suppose two like charges repel each other and drift apart, gaining kinetic energy as they go. Where did that additional kinetic energy actually come from?

In the standard classical account, the electromagnetic field participates directly in the energy bookkeeping. The system carries electromagnetic potential energy, and as the charges move apart, energy transfers back and forth between the mechanical sector and the electromagnetic sector. More generally, energy can flow from place to place through the field itself, governed by the Poynting theorem introduced in the last chapter, which in its local form reads

*∂u/∂t + ∇·S = −J·E*.

In full, that equation says: energy stored in the electromagnetic configuration can change over time; energy can flow continuously from one region of space to another, carried by nothing but the field itself; and matter can gain energy precisely as the electromagnetic system loses it, or vice versa, all tracked locally and consistently. It is a remarkably coherent and successful picture.

So what happens if you refuse, on principle, to treat the field as an independent repository of energy at all? You need another complete account — one that attributes all of that energy to the interacting charged particles directly, with the apparent "field energy" of the standard picture emerging somehow from the structure of their mutual interaction rather than being stored independently in the space between them.

That reformulation is conceptually possible in certain restricted settings, but it isn't a free relabeling that costs nothing — it changes how you have to think about what is physically happening in the empty space between two charges, and this is the point in the argument where this book has to resist the temptation to make things sound tidier than they actually are. A beautiful idea is not automatically a complete theory.

Claiming that all electromagnetic energy ultimately belongs to matter and its interactions carries an obligation to show, in detail, how that reformulated theory reproduces energy conservation, momentum conservation, radiation, propagation at the speed of light, interference, electromagnetic waves, photon emission, photon absorption, and the experimentally verified quantum corrections that QED gets right to the same one-part-in-a-billion precision noted back in Chapter 9. That is a formidable list. Direct-action thinking illuminates real pieces of it beautifully. Ordinary QED remains powerful because it handles the entire list at once, inside one relativistic quantum framework, without needing to reformulate anything on a case-by-case basis.

What changes from one formulation to another is where the description places the degrees of freedom. A different bookkeeping can assign the same total energy to the interaction of the charges rather than to a field sitting between them. Energy conservation survives that rewrite. Momentum conservation survives it. Radiation survives it. The rewrite is never permission to stop conserving energy, and it is not, by itself, a replacement for QED.

There is a further reason to hold this discussion to a high standard, and it's the same reason Chapter 9 raised in passing: a real photon is more than an accounting entry in someone's calculation. It can be detected, arriving at a detector with a definite, measurable energy and momentum:

> **Equation (4).** Photon energy and momentum:
> *E = ħω*,
> *p = ħω/c*.

Light, in other words, comes in discrete quantum packets that behave, on arrival, like particles with sharp, well-defined properties — and that fact has direct consequences for the phase-centered picture this book has been developing since Chapter 1. It means phase alone is not the whole story. Phase governs interference and the evolution of amplitudes beautifully, but the electromagnetic field additionally has quantized excitations, and those excitations carry energy and momentum in their own right. Any complete theory has to account for that fact, not just the phase relationships riding on top of it.

Quantum electrodynamics is the theory that can count those photons. The classical electromagnetic potential becomes an operator-valued quantum field, capable of existing in states containing zero photons, one photon, a vast number of photons, or elaborate superpositions of all of the above — and the quantum state of light itself turns out to carry its own phase structure, on top of everything already said about the phase of charged matter.

Coherent states of the field provide the bridge back to the everyday classical world: a classical-looking electromagnetic wave corresponds to a quantum state in which the photon number is not sharply fixed at all, but the field nonetheless has a well-defined coherent amplitude, meaning the classical wave isn't so much a rival to the photon picture as what an enormous, highly coherent population of photons looks like once you stop being able to count them individually. The same bridge, built from the same material, connects a single click in a photon detector to a beam bright enough to read by.

Here is a point that links directly back to Part Two. This book has now encountered coherence in two apparently separate settings. Matter can be coherent: that was the whole subject of superconductivity, an enormous number of charged constituents sharing one macroscopic quantum phase. Light can be coherent too: that is what a laser is, an enormous number of photons occupying one highly organized quantum state. These two situations are not identical. But the same underlying mathematical idea, phase coherence, links them, and that link turns out to be one of the most fruitful available routes for connecting Mead's world to Feynman's.

In a sufficiently coherent regime — inside a superconducting circuit, say, or a microwave cavity tuned to trap a single electromagnetic mode — the electromagnetic interaction itself can become a macroscopic relationship between two collective phases: the phase of the coherent matter and the phase of the coherent light, exchanging excitations back and forth in an orderly, trackable way.

At that point, "matter" and "field" stop naming two different substances and start naming two sets of degrees of freedom coexisting within one quantum system. That is one of the most useful lessons available from this entire debate: the better question is less the flat *is the field real?* than *which degrees of freedom are the natural ones for describing the physical regime in front of you right now?* Sometimes the honest answer is individual particles. Sometimes it's collective matter. Sometimes it's electromagnetic modes. Sometimes it's phases and potentials, stripped of everything else.

The art of physics, as much as anywhere in this book, lies in knowing when to change language without imagining that you've changed the underlying physics along with it — and in resisting the temptation, once photons enter the story, to turn any of these ideas back into a cartoon of tiny bullets passing between billiard balls. The real picture, threading phase, potential, field, and photon together, is stranger than that cartoon. It is also far more elegant. The next Part puts it to the harder test: setting this whole phase-and-potential framework directly against the full machinery of quantum electrodynamics, to see how much of it survives contact.
