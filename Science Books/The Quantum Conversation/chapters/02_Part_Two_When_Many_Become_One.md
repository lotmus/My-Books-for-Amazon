# PART TWO — When Many Become One

---

## 5. One Electron Is Not a Superconductor

It is tempting to picture a superconductor as an ordinary collection of electrons that simply happens to behave unusually well — as if you'd taken normal, sluggish, resistance-generating electrons and, through some clever trick, gotten them all to cooperate. That picture misses the interesting part entirely. Here's why.

Take a million ordinary electrons and put them in a box. You do not get one giant electron. You get a million electrons, each with its own quantum state, scattering off impurities, bumping into the lattice, interacting with one another in complicated and largely incoherent ways. Their combined behavior is, in a real sense, still just a sum of a million separate stories, however hard those stories are to track individually.

Cool the same box down, far enough that thermal jostling stops scrambling everything, typically within a few degrees of absolute zero, though some materials manage the trick above the temperature of liquid nitrogen (still colder than anywhere on Earth's surface has ever naturally been, but warm enough to reach with a cooling method any lab can buy off the shelf), and something changes qualitatively, not just quantitatively. A *coherent* quantum system is a different kind of object altogether. It can develop collective degrees of freedom: new variables that describe the system as a whole and cannot be recovered by patiently following each constituent on its own.

This is not a specifically quantum idea; classical physics is full of the same trick. A sound wave moving through a room involves an astronomical number of air molecules, but nobody describes a sound wave by writing down the trajectory of every molecule: the pressure wave itself is the useful variable, and it exists at a level of description where individual molecules have already been left behind. An orchestra tuning up produces one recognizable pitch out of dozens of instruments doing slightly different things; the pitch is real, audible, and measurable, and it is not the story of any single violin.

Collective behavior generates its own vocabulary, and that vocabulary isn't so much a shorthand for ignorance as the most accurate description available.

Superconductivity takes this same idea and carries it into the quantum domain, where it becomes stranger still. The microscopic electrons are still there, still individually quantum mechanical, still subject to all the ordinary rules. But under the right conditions the system develops a collective quantum state characterized by a single, shared phase spread across the entire material. A useful schematic way to write this collective state is

*Ψ(r) = √n(r)e^iθ(r)*

*where n(r) is the local density of the coherent charge carriers and θ(r) is the phase.*

The phase is now a function that varies smoothly across the whole sample, not a private property buried inside one particle's wavefunction. Once it varies from point to point, it starts to carry real physical consequences. Where the phase changes rapidly, the coherent state carries momentum. Where the electromagnetic potential changes, the relationship between that phase gradient and the resulting momentum changes right along with it. And if we insist that the phase stay self-consistent going all the way around a closed loop (the same consistency requirement from Chapter 3), the allowed electromagnetic configurations become quantized.

The loop, in other words, has returned. But this time it is a loop of superconducting wire you could hold between two fingers, not a loop traced only in the abstract mathematics of one electron's wavefunction amplitude. That is the extraordinary part: a condition that sounds like pure quantum bookkeeping turns into a laboratory-scale electromagnetic fact, measurable with ordinary instruments, engineered into real devices.

It is also, not incidentally, engineered into a piece of hospital equipment: an MRI scanner's main magnet is a superconducting coil, cooled this way, sustaining a field of one and a half to three tesla — tens of thousands of times the strength of Earth's own magnetic field — with no ongoing power supply needed to maintain it, because a genuinely superconducting current, once started, simply does not decay. Scaled up this far, the quantum world hasn't receded at all — it has organized itself and grown right along with the hardware built to hold it.

That sentence would have sounded strange to a physicist in, say, 1900. Quantum effects were assumed, almost by definition, to be small: confined to individual atoms, washed out the instant enough of them were gathered together for a human hand to hold. A superconducting ring quietly violates that assumption. Nothing about the ring is microscopic. You can machine it, cool it in an ordinary laboratory cryostat, connect wires to it, and read a number off an instrument. And the number you read is set, ultimately, by the same consistency requirement that governs a single electron's wavefunction.

Scale, in this one respect, turned out not to be the boundary between the quantum and the classical after all. Coherence was.

But that word "phase" invites a misunderstanding. A superconductor is not, in any literal sense, one enormous particle standing in for a billion small ones. The microscopic state of the material remains ferociously complicated — every electron is still there, still obeying the full machinery of many-body quantum mechanics. What changes is that the system's *low-energy* collective behavior can be captured almost completely by a macroscopic complex order parameter with a single, well-defined phase. That phase is coherent across the entire sample. And coherence, once again, is doing all the work.

An analogy that gets the flavor right, if not the full subtlety: imagine a packed stadium. If everyone claps at a moment of their own choosing, the sound is a formless roar — loud, but statistically unremarkable, growing only in proportion to the number of people clapping. If the same crowd claps in unison, the result is qualitatively different: a sharp, powerful sound that can shake the building, growing far faster than the headcount alone would suggest. No individual clapper has changed. What changed is the relationship between them.

Quantum coherence is a more delicate phenomenon than synchronized applause, but the underlying lesson survives the analogy: when many contributions share a definite phase relationship, their combined effect can be wildly disproportionate to what you'd expect from simply adding up the individual pieces.

This is why coherent quantum systems make such a powerful laboratory for electromagnetic ideas. In a superconductor, quantum phase stops being an abstraction confined to a physicist's notebook and becomes something you can build circuits out of. You can construct devices whose behavior depends directly on phase differences between two points. You can measure interference between macroscopic quantum states, the way you'd measure interference between two beams of light. You can trap magnetic flux inside a superconducting ring and find that it only ever comes in the discrete amounts fixed by *Φ₀ = h/2e* — never a little more, never a little less.

You can build a system in which the quantum state of matter itself controls an electromagnetic response you can read off with a voltmeter on a lab bench.

One such device, the superconducting quantum interference device (everyone in the field simply calls it a SQUID), is already sitting in hospitals and geology labs around the world, built from nothing more exotic than a superconducting loop interrupted by one or two thin barriers. Its output current oscillates as the enclosed flux is tuned, tracing out an interference pattern the way two overlapping light beams trace out bright and dark fringes on a screen, except here the two "beams" are the same macroscopic quantum state interfering with itself around a loop of wire.

That interference pattern is sensitive enough to detect a change in magnetic field measured in single flux quanta, which is why SQUIDs are used to image the faint magnetic fields produced by electrical activity in the human brain, a signal about a billion times weaker than the Earth's own magnetic field. I spent forty years around circuits that only knew about **E** and **B**. The first time I understood what a sensor like this is counting, it was not a force on a needle. It was a shared phase slipping by one flux quantum. Getting here never required inventing new physics beyond what this chapter has already described — only noticing that the phase had always been more than a bookkeeping device.

Through all of this the system has simply become *collective* — quantum mechanics practiced at a scale that used to belong exclusively to classical engineering, with nothing about it any less quantum mechanical than before.

That raises a hard question, and it is the question that will occupy the rest of this Part. What happens to an electromagnetic interaction — to the whole apparatus of charges and fields and forces — when the charges involved are no longer acting as a loose crowd of independent particles, but as a single coherent whole? The intuitive answer is: probably not much, beyond a straightforward matter of scale. The actual answer is far more interesting, and it is one of Mead's most provocative contributions to this entire picture.

---

## 6. Coherence Changes the Rules

Suppose you have *N* charged particles, and you want to know how strongly they interact with an external field, or how much radiation they produce, or how large some collective response will be. The ordinary classical instinct says: work out what one particle contributes, then multiply by *N*. One particle, one unit of effect; a thousand particles, a thousand units. Often enough, that instinct is right — most contributions from most particles are effectively independent, and independent contributions add.

But coherent systems break that instinct in a specific, well-understood way. If *N* sources contribute an amplitude coherently (meaning all their phases line up), the total amplitude does not average out or partially cancel. It simply adds:

*A_total = Na*

*where a is the amplitude contributed by one source.*

The trouble, or the opportunity, shows up once you square that amplitude to get an intensity, an energy, or a rate — the kind of quantity you'd measure. Squaring a coherent sum gives

*|A_total|² = N²a²*,

compared with *Na²* for *N* independent, incoherent sources, whose contributions add as intensities directly rather than as amplitudes.

Why becomes clear once you notice the machinery for it was already built back in Chapter 1. When *N* sources are incoherent, their phases point every which way, like *N* arrows scattered at random angles instead of lined up. Random arrows mostly cancel — this is the same interference arithmetic from Chapter 1, just run with many more arrows than two — and the typical length of their sum grows only as the square root of *N*, the familiar "drunkard's walk" result for a random sum. Square that typical length to get an intensity, and the √N becomes a plain *N*.

Coherent sources skip the cancellation entirely: all *N* arrows point the same way, their lengths add to *Na*, and squaring that gives *N²a²* instead. The gap between the two cases is the gap between arrows that fight each other and arrows that don't.

The difference between *N* and *N²* is not a rounding error. For a billion coherent particles, it is the difference between a billion and a billion billion.

A radio engineer meets this fact constantly and gives it an unmysterious name: an antenna array. Feed the same signal, perfectly in phase, to a hundred individual antenna elements arranged in a grid, and the power radiated in the favored direction does not simply scale with the hundred elements doing the radiating — it scales with the hundred elements *squared*, ten thousand times the output of one element alone — concentrated into a narrower beam, not manufactured from nowhere, since the total power radiated in every direction combined is still set by what the array is fed — which is why phased-array radar and modern cell towers bother with many small antennas instead of one large one.

Break the phase relationship between the elements (let each one radiate on its own schedule instead of in lockstep), and the enhancement collapses back down to plain old proportionality with *N*. Nothing about the individual antennas changed in either case. Only whether they were coherent with each other did.

This is not a mysterious quantum effect dreamed up specially for superconductors — it is the same mathematics behind coherent radio antennas, laser light, and diffraction gratings. What makes it relevant here is Mead's observation that a coherent electrodynamic system's *collective* degrees of freedom can scale with the number of participating charges in a different way than the *mechanical* degrees of freedom of the same number of independent particles would. That distinction matters more than a technical footnote — it changes what you should expect the macroscopic equations of a coherent system to look like, and it is why a superconducting loop carrying an enormous number of charge carriers can behave, electromagnetically, like a single coherent object rather than like a crowd.

It is easy to overreach here, so one caveat needs stating plainly: not every physical quantity in a coherent system scales as *N²*. Different quantities depend on different combinations of amplitude, density, geometry, and the details of how the system is coupled to whatever you're measuring. The safe, general lesson is narrower than "everything gets bigger by a factor of *N*": coherence changes scaling laws, in ways that depend on what you're asking about — which is why the classical limit of a coherent quantum system can look nothing like the naive sum of many independent classical particles.

The broader moral generalizes well beyond superconductors. The number of constituents in a system is never, by itself, enough to predict its behavior — you also need to know how those constituents are organized. A crowd is more than a list of people. A fluid is more than a list of molecules. A superconductor is more than a list of electrons. And, as the next several chapters will start to suggest, a classical electromagnetic field may not be the most fundamental way to describe the underlying quantum relationships from which its large-scale behavior emerges.

---

## 7. Momentum in the Presence of a Potential

One of those underlying quantum relationships is momentum itself — and it turns out the electromagnetic potential gets folded into the definition of momentum in a way that's easy to overlook until a coherent system forces the issue. Momentum looks like one of the least controversial ideas in all of physics. Something moves; it has momentum. In classical mechanics the relationship is about as simple as physics gets:

*p = mv*.

Quantum mechanics complicates this picture in a specific and illuminating way. The momentum of a quantum particle is tied to how quickly its phase changes from point to point: schematically, *p ~ ħ∇θ*, momentum proportional to the spatial gradient of the phase. (*ħ*, pronounced "h-bar," is just Planck's constant *h*, the same *h* from the flux quantum in Chapter 3, divided by 2π; it is the form of Planck's constant that shows up naturally wherever a phase gradient is doing the work.) That much would already be true with no electromagnetism anywhere in sight.

Introduce an electromagnetic potential, though, and something has to give: the *mechanical* momentum (the quantity that shows up in *F = ma*) and the *canonical* momentum used in the formal machinery of the theory are no longer simply the same thing. The electromagnetic potential inserts itself directly into the relationship between them. In the standard "minimal coupling" form, it is the combination

*p − qA*

that plays the role of mechanical momentum, with the exact signs and factors depending on convention.

The split between canonical and mechanical momentum is not a quirk invented for electromagnetism specifically — it is built into the whole framework, going back to Hamilton, that quantum mechanics inherited from classical mechanics. The canonical momentum is whatever quantity pairs naturally with position in that formal machinery, the one that generates translations (that is, the quantity whose value governs how the system shifts when you nudge it from one point to a neighboring one) and that quantum mechanics expresses as a derivative of the wavefunction's phase.

It usually happens to coincide with the everyday, common-sense momentum *mv* — until an electromagnetic potential is switched on, at which point the two quietly split apart, and it is the mechanical combination, *p* − *qA*, that continues to correspond to the ordinary notion of "mass times velocity" a bathroom scale or a police radar gun would register. Get the two confused, and a calculation can look consistent right up until it disagrees with an experiment.

This is one of the places where the potential stops resembling a mathematical convenience and starts looking like a direct participant in the dynamics. The quantum phase determines momentum. The electromagnetic potential reshapes the relationship between phase and actual mechanical motion. Put those two facts together, and the electromagnetic interaction can be described as changing the way quantum phase translates into physical momentum — an unusually compact way of saying what electromagnetism *does*.

Set this new formulation directly against the old one. The traditional story runs: *charges produce fields, and fields exert forces.* The story this book has been building runs instead: *charged quantum matter carries phase, and electromagnetic potentials determine how that phase translates into momentum and accumulated action.* The two descriptions have to agree wherever they overlap, and they do. But the second one keeps the underlying quantum machinery visible the whole way through, instead of hiding it behind a force law.

And once a huge number of particles share a single collective phase — as in Chapters 5 and 6 — this exact relationship stops being a private fact about one electron's wavefunction and becomes something you can measure across an entire circuit. The electromagnetic behavior of the whole coherent system can be encoded in how its collective phase evolves in time and space. This is the doorway through which Mead's approach to electrodynamics enters the larger story this book is telling.

But a harder question is waiting just past that doorway. If the potential is this central to the phase of matter, where does the potential itself come from?

---

## 8. Where Does the Potential Come From?

The potential shapes the phase of charged matter. What produces the potential?

If an electron moves, the potential surrounding it changes. If a different electron moves somewhere else entirely, that potential changes too. It can start to feel as though we've simply relocated the original mystery rather than solved it. We began with a force, replaced the force with a field, replaced the field with a potential — and now we're asking what produces the potential. That's how physics usually works, not a failure of the approach: you solve one puzzle and discover it was resting on top of a deeper one.

The classical answer is straightforward enough to state. Charge and current act as sources of the electromagnetic field, and Maxwell's equations describe how those sources generate the potentials, and how the resulting fields propagate outward. In the language of potentials, this relationship between source and result is captured by a *Green's function*. If you have met a response function under another name, this is that object. The name is older than the jargon around it.

Suppose you want to know how a complicated system responds when you disturb it somewhere. Start with the simplest version of that question: what happens if the system is poked at exactly one point? The response to that single poke is the Green's function. Once you know the response to one elementary disturbance, the response to any complicated source is the sum of those responses, one for every point where the source has some charge or current.

A sound engineer uses this trick without necessarily calling it by name. Record how a concert hall responds to a single, sharp handclap — its "impulse response" — and you have, in effect, measured the room's Green's function for sound. From that one recording, a studio can predict, with real accuracy, how the same hall would color an entire symphony, by treating the symphony as an enormous number of tiny clap-like disturbances layered on top of each other and adding up the room's response to each. Nobody needs to re-record the orchestra inside the actual hall to know what it will sound like there. The single poke already contained the room's whole personality.

For electromagnetism, the Green's function tells you how a source at one point in spacetime contributes to the potential at another point in spacetime — and immediately, something important falls out of that statement. The potential at one event is tied to what happened at other events, elsewhere and, crucially, *earlier*. At bottom, electromagnetism weaves relationships through spacetime, connecting what happens here to what happened there, rather than narrating isolated objects that each carry a private, self-contained history. That observation is about to matter a great deal, because relativity has strong opinions about which "elsewhere" and "earlier" are allowed, and the next few paragraphs spell them out.

There's a tempting shortcut lurking in the picture just sketched. If the potential at one location depends on a charge sitting somewhere else, maybe that charge reaches across space and influences the potential instantaneously — a kind of electromagnetic action at a distance, no propagation required, no delay involved. It would be a tidy picture. Relativity will not permit it.

No physically usable signal can travel faster than light, and this single fact reshapes the entire structure of electromagnetic theory. The influence of a charge that changes its motion does not appear everywhere in space all at once. It propagates, outward, at a finite speed, carrying a definite causal structure with it. Flip a light switch, and every electron in the room does not respond instantaneously to the change in current at the switch — the update ripples outward across the room in a few dozen billionths of a second, far too fast for anyone to notice, but not actually zero.

On a solar-system scale the delay becomes personal: sunlight leaving the Sun takes a little over eight minutes to reach Earth, so a hypothetical observer watching the Sun through a telescope is always watching it as it was eight minutes ago, and if the Sun's own electromagnetic field somehow flickered right now, nobody here would know about it until that same eight minutes had passed. The Green's function just described is not a bare mathematical convenience — it *encodes* that causal structure directly. In fully relativistic language, the potential produced at a given event depends only on sources lying in that event's appropriate causal past, with the precise details fixed by which Green's function and boundary conditions the calculation uses.

This is where an old-fashioned instantaneous force becomes inadequate as a picture of what's happening. Something has to physically connect distant events in spacetime in a way that respects the speed-of-light limit, and the field formulation makes that connection almost visually obvious: you can picture a disturbance rippling outward from its source, like a stone dropped in a pond, arriving later and later at points farther and farther away.

But there is another way to think about the very same causal structure — one that doesn't require imagining an independent substance called "the field" physically carrying the message from one place to another. On this alternative view, the electromagnetic interaction establishes relationships between events in spacetime, relationships constrained by the same causal structure, without insisting that something material has to occupy the space in between to make the connection work. The distinction is subtle.

It also turns out to matter enormously, because it is the seed of an entire alternative tradition in electromagnetic theory — one associated with John Wheeler and Richard Feynman himself, which asks whether the electromagnetic field's independent degrees of freedom are strictly necessary at all, or whether the interaction between charged particles can be described directly, without ever positing a separate field to carry it.

That question is far more radical than anything raised so far, and a passing mention won't do it justice. Part Five keeps it in its place. First, though, standard quantum electrodynamics has to say what a photon is. Otherwise that question has nothing to be a question about.
