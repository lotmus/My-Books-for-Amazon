# PART FOUR — Finding Maxwell Again

---

## 12. Where Did the Fields Go?

Where did **E** and **B** go? Eleven chapters of phase and potential, and the fields with the diagrams and the right-hand rules have barely appeared.

Nowhere. They have simply moved one step downstream. Start with the scalar and vector potentials, *φ* and **A**, exactly as before. From them, construct

*E = −∇φ − ∂A/∂t*

and

*B = ∇×A*.

These relationships define how the potentials and the familiar fields relate to one another, and nothing about the last eleven chapters asks you to give them up. What changes is not the mathematics but the interpretation of which side of the equation gets to be the starting point. Instead of treating **E** and **B** as the primary ingredients of electromagnetism, with the potentials introduced afterward as a convenient shortcut, this book has been treating the potentials as the primary objects and **E** and **B** as the gauge-invariant, locally measurable quantities you build from them.

This reordering pays off the moment you notice how naturally it lines up with the rest of physics. Quantum mechanics is most naturally expressed in terms of phase and potentials — that has been the entire argument since Chapter 1. Classical electromagnetism is most naturally expressed in terms of fields — that is how the subject is normally taught, and for good reason, since fields are what you measure with a voltmeter or a compass needle. The potential is what lets these two natural languages talk to each other without either one pretending to be a mere approximation of the other.

The bridge becomes especially elegant once relativity enters the picture properly. Rather than treating the scalar potential and the three components of the vector potential as four separate, unrelated functions, they combine into a single relativistic object, the four-potential. The electric and magnetic fields can then be packaged together into one corresponding object, the electromagnetic field tensor — and this is where a fact usually taught as a curiosity turns out to be structurally central. Electricity and magnetism turn out to be two aspects of one electromagnetic structure rather than two fundamentally separate forces that happen to share a name, and which aspect you see depends on how you, the observer, happen to be moving.

A magnetic field measured in one reference frame can appear partly as an electric field in another frame moving relative to the first. The split between "electric" and "magnetic" phenomena is, in this precise sense, partly a fact about the observer rather than a fact about the field alone. The four-potential is what makes that unity visible without any extra work.

A single moving charge makes the point concretely. Sit at rest next to an electron, and you measure a purely electric field radiating outward from it in every direction, with no magnetic field anywhere to speak of — nothing is moving relative to you, so there is nothing for a magnetic field to be "made of" in the usual textbook sense. Now let a second observer run past that same electron at high speed. From that observer's point of view, the electron itself is moving, which means it constitutes a current, and a moving charge produces a magnetic field.

Both observers are correctly describing the very same electron, at the very same instant, using the very same laws of physics — they simply disagree about how much of the electron's influence to call "electric" and how much to call "magnetic." What neither observer can disagree about is the field tensor built from the four-potential, which every observer, moving at whatever speed, correctly reconstructs into the identical electric and magnetic split once their own velocity is accounted for. The split is real and useful, but only feels fundamental from inside a single, stationary laboratory.

Quantum mechanics then adds the layer that has been this book's whole argument so far: the four-potential couples directly to charged quantum matter, entering the phase of every amplitude a charged particle carries. Classical fields are what falls out of that coupling once you stop tracking individual phases and look only at the aggregate. That gives us a single thread running through everything covered in Parts One through Three — quantum phase, connected to the four-potential, connected to the electromagnetic field — and the rest of this book is, in large part, an extended investigation of how far that thread can be followed before it frays.

---

## 13. Maxwell Appears

There is a persistent, slightly misleading image of how Maxwell's equations came to be: James Clerk Maxwell at a blackboard one afternoon, writing down four tidy equations, after which the universe agreed to obey them. The real history was much messier. Maxwell was synthesizing decades of experimental discoveries and mathematical groundwork laid by Coulomb, Ampère, Faraday, and others; the compact four-equation form familiar today was assembled, and partly reformulated, by people who came after him. Maxwell's own original presentation, in 1865, ran to some twenty equations, thick with components written out one at a time in the style of the day.

It was Oliver Heaviside (the same Heaviside from Chapter 2, tidying the equations down to the potential-stripped, field-only form that became standard) who compressed all twenty into the compact four now printed on undergraduate T-shirts. That messiness disappears from the final result, which is remarkably economical: four equations relating electric and magnetic fields to charge, to current, and to each other.

In modern notation, they read

> **Equation (2).** Maxwell's equations:
> *∇·E = ρ/ε₀*,
> *∇·B = 0*,
> *∇×E = −∂B/∂t*,
> *∇×B = μ₀J + μ₀ε₀∂E/∂t*.

The first time you meet these, they look like four independent rules that simply have to be memorized. The potential formulation from the last chapter exposes two of them as consequences of definitions already made, not independent assumptions at all. Recall that *B* = ∇×*A*. Take the divergence of both sides:

*∇·B = ∇·(∇×A) = 0*.

The second of Maxwell's four equations has appeared automatically — it isn't a separate physical law so much as a direct consequence of *B* being built from a potential in the first place, since the divergence of a curl is identically zero for any vector field whatsoever. Now take *E* = −∇*φ* − ∂*A*/∂*t* and apply a curl to both sides. Since the curl of a gradient vanishes identically, only the second term survives, and using ∇×*A* = *B* again gives

*∇×E = −∂B/∂t*,

the third of Maxwell's equations, appearing just as automatically as the second.

This is more than an algebraic curiosity. It tells us that two of the four famous equations turn out to be built into the very definition of the potentials, not independent physical content at all, true for purely geometric reasons, the way "a circle has no corners" is true by definition rather than by observation. The remaining two — Gauss's law, ∇·**E** = ρ/ε₀, and the Ampère–Maxwell law, ∇×**B** = μ₀**J** + μ₀ε₀∂**E**/∂*t* — do not fall out of the definitions the same automatic way.

They have to be imposed from outside, as genuine dynamical content connecting the potentials to whatever charges and currents happen to be present, and they are the two equations that determine what the potentials themselves are, given a particular arrangement of matter. That is the real physics: not four independent commandments, but two definitions and two laws telling those definitions how to respond to the world.

![Figure 4. The potentials come first: the fields are built from them, and Maxwell's equations describe how those fields — and their sources — are allowed to behave.](fig04_maxwell_flow.png)

So the four equations everyone memorizes split into two unequal tiers rather than standing side by side as four equally fundamental laws. In the potential formulation used here, two of them — the homogeneous pair, ∇·B = 0 and Faraday's law — follow identically from how the fields are defined in terms of potentials in the first place; they are consequences of that definition, not separate physical assumptions being smuggled in. The other two — the inhomogeneous pair, Gauss's law and the Ampère–Maxwell law — carry the genuine dynamical content, describing how the electromagnetic system behaves given real sources.

That distinction is nearly invisible when Maxwell's equations are handed to you as a finished list of four, and it gives us a clean conceptual hierarchy to work with going forward: potentials provide a compact description; fields are derived from them; Maxwell's equations describe how those fields, and their sources, are allowed to behave; and quantum mechanics tells us how charged matter couples to the potential underneath it all. Maxwell's equations lose nothing in this book's approach; they now sit inside a larger structure, showing up as a consequence rather than as a starting axiom.

---

## 14. The Classical World Is a Limit, Not a Different Universe

A persistent misconception treats the quantum world and the classical world as two separate universes, each running on its own rulebook, with some mysterious switch flipped at a certain size or energy where the quantum rules get turned off and the classical ones take over. Nature has no such switch. Classical physics emerges from quantum physics under the right conditions — but "emerges" is doing real work in that sentence, and it does not mean "becomes irrelevant" or "stops actually being quantum mechanics underneath."

Consider a laser beam. Quantum electrodynamics describes electromagnetic radiation fundamentally in terms of quantum states of the field. And yet a sufficiently intense, sufficiently coherent beam is described extraordinarily well by ordinary classical electromagnetic wave equations: the classical electric and magnetic fields function as effective variables capturing the large-scale behavior of an underlying quantum state, without the everyday user of a laser pointer ever needing to think about photons at all. Something structurally similar happens with matter.

A baseball has a genuine quantum state, complete with a well-defined quantum wavelength (the de Broglie wavelength, set by dividing Planck's constant by the ball's momentum) that comes out to something like 10⁻³⁴ meters for an ordinary fastball, a distance so far beneath anything measurable that no experiment ever built or conceivable could resolve the ball's wave nature directly.

Under ordinary conditions, its center-of-mass motion is described superbly by Newtonian mechanics anyway, not because quantum mechanics quietly excuses itself for objects that large, but because the phases associated with wildly different possible trajectories interfere destructively with each other, and constant interaction with the surrounding environment suppresses any observable coherence between macroscopically distinct possibilities before it could ever become visible. The classical world, in other words, is an extremely well-organized regime of quantum mechanics, not a rejection of it.

This matters here because Mead's work draws attention to a particularly interesting variety of that classical limit — one that doesn't work the way intuition suggests. The obvious guess is that a collective quantum system becomes classical by each of its microscopic constituents individually becoming classical, the way a crowd might be imagined to "become classical" if every person in it separately started behaving predictably. A coherent quantum system does it differently: it can remain thoroughly, unambiguously quantum mechanical at the microscopic level while its collective variables behave in a way that looks entirely classical from the outside.

A superconducting circuit makes the point vividly. Its collective phase is a quantum mechanical object. Its enclosed flux is quantized, in discrete units of *h*/2*e*, as Chapter 3 derived. Its current depends directly on how that phase varies. And yet the whole system can be described, for engineering purposes, using the ordinary vocabulary of classical electrical circuits — voltages, currents, inductances — without anyone needing to reference a wavefunction. Quantum mechanics, rather than receding from this picture as the system got larger and more practical, organized itself into a macroscopic form and kept right on being quantum mechanics the entire time.

That is a different idea from the more familiar hand-wave: "there are so many particles that quantum effects simply average out." Sometimes that's what happens. But sometimes — and this is the more interesting case, the one this book keeps returning to — coherence survives *because* an enormous number of particles are acting collectively rather than independently, and the classical-looking behavior that results is a direct consequence of that coherence rather than a symptom of its absence.

Coherence, the mechanism doing all of that work, is one of the great hidden organizing principles running underneath this entire book.

Picture two speakers playing the same musical tone. If they are perfectly synchronized, their sound waves combine in a highly organized way: reinforcing sharply in some locations, canceling sharply in others, producing a distinctive pattern you can walk around and map out. If they are not synchronized, the same two waves still combine, but the resulting pattern is far less organized, closer to an unremarkable blur. A laser and an ordinary light bulb make the identical contrast with light itself.

Both convert electrical energy into photons, often in comparable total quantities, but a light bulb's atoms emit independently of one another, each on its own schedule, producing a beam that spreads out in every direction and washes out any interference pattern almost immediately.

A laser's atoms are coaxed into emitting in lockstep, sharing one phase across an enormous number of photons at once; that shared phase is what stimulated emission needs to work at all, and the cavity of mirrors bouncing light back and forth is what then shapes it into a tight, directional beam, so a laser pointer stays coherent and narrow across a lecture hall while a flashlight bulb of similar power, with no such cavity and no shared phase, floods the whole room within a few feet. The energy budget can be nearly the same.

The organization is not, and the organization is the whole difference. Now scale the picture up. With thousands of independently fluctuating sources, contributions mostly average together in a fairly ordinary way: nothing dramatic happens, because there is no shared phase relationship for the contributions to reinforce around. With thousands of *coherent* sources, all sharing a definite phase relationship, the combined effect can become enormous, in a very specific mathematical sense already introduced in Chapter 6: the difference between contributions adding as *N* and combining as *N²*.

That earlier discussion was about particles contributing to a scattering process. The same underlying mathematics runs the whole show here too. Quantum systems can exploit this same structure, and the distinction between coherent and incoherent addition is often the distinction between an effect that scales like *N* and one that scales like *N²* — which is also, not coincidentally, why coherence is capable of surprising anyone whose intuition was built entirely on independent, uncoordinated particles.

A superconductor remains the most dramatic illustration available. Its collective state is described by a single macroscopic phase, and its electromagnetic response depends on how that phase varies across the material. The resulting current is a collective property of the coherent state as a whole, not just "a great many electrons each independently doing their own small thing, added up" — a different kind of object from a sum of independent contributions, in the same way a synchronized round of applause is a different *kind* of sound from an unsynchronized one, not simply a louder version of it.

This is another reason to take phase as seriously as this book has been insisting all along. The phase is no longer confined to the microscopic description, invisible and irrelevant at any scale you could observe. It governs a macroscopic, measurable response. And that inverts the usual order in which electromagnetism gets taught. The traditional route runs: first there is a field, and then the field acts on matter. The route this book has been building runs the other way: there is coherent quantum matter; its phase is coupled to the electromagnetic potential; the resulting collective dynamics produce the electromagnetic behavior we go on to observe and call "the field."

These need not be treated as rival descriptions fighting over which one is real. They emphasize different layers of one underlying structure, and each earns its keep for different purposes.

That said, one of the deepest questions in this entire subject is now sitting in plain view, and it would be evasive to keep walking past it. If the electromagnetic interaction can be described through relationships between charges, and if the potential enters directly into the phase of matter without needing a separate mediator to carry it — do we actually need to treat the electromagnetic field as an independent physical entity at all, with its own degrees of freedom, sitting between the charges as a substance in its own right?

This is precisely the question Richard Feynman took up, a few years before quantum electrodynamics became his more famous legacy, in an unusual collaboration with John Wheeler. The next part keeps that question in its place. The list of what the quantum theory actually adds is Chapter 19.
