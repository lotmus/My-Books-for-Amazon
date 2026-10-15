# -*- coding: utf-8 -*-
# Hooks (engagement) and three inquiry prompts (How do we know? / What would change our mind? / Try it yourself) for chapters 1-38.
CH = {}
def add(n, hook, how, change, tryit): CH[n] = dict(hook=hook, how=how, change=change, tryit=tryit)

add(1, "A skater pulls in her arms and spins faster. A satellite circles for decades without fuel. A pendulum clock keeps time through a recession. Behind these three ordinary facts stand the ideas that carry the rest of this book: motion needs no push to continue, forces change motion, and energy keeps its books to the last decimal.",
 "How do we know that heavy and light objects fall together? Think of what Galileo could measure with a ramp and a water clock, and of the astronaut who dropped a hammer and a feather on the Moon in 1971.",
 "What observation would show that energy is not conserved? When beta decay seemed to break the rule, physicists proposed a new particle instead of abandoning it. Why was that a reasonable bet?",
 "Drop a coin and a sheet of paper together, then drop the paper crumpled into a ball. What changed, and what did not?")
add(2, "A cup of coffee cools, and never warms itself from the air around it. Nothing in the laws of motion forbids that, yet no one has ever seen it happen. The reason, which took the nineteenth century to find, is the most statistical law in physics.",
 "How do we know that heat is the motion of molecules? Brownian jiggling of pollen grains and Joule’s paddle wheel, which turned falling weights into warmth in water, both point to it.",
 "What would a genuine violation of the second law look like, and why do physicists still bet heavily against it?",
 "Put a drop of food coloring in a glass of cold water and another in a glass of warm water. Time how long each takes to spread evenly, and ask what the difference says about molecular motion.")
add(3, "You can hear a conversation around a corner without seeing the speakers. Sound bends around obstacles and light mostly does not. The difference is wavelength, and it is the first clue to what a wave is.",
 "How do we know that light is a wave? In 1801 Thomas Young showed that light from two narrow slits makes bright and dark bands, a result that only waves can produce.",
 "What would it mean if light showed no diffraction at any scale? Why does the size of an obstacle, compared with the wavelength, decide whether you see bending?",
 "Look at a bright lamp through the narrow gap between two fingers held almost touching, or through the fine barbs of a feather. The dark lines you see are interference.")
add(4, "Rub a balloon on your hair and it clings to the wall. A compass needle swings near a wire carrying current. In 1865 four equations tied these curiosities to one another and to light itself, and predicted radio before anyone had built a transmitter.",
 "How do we know that light is an electromagnetic wave? Maxwell calculated its speed from electrical and magnetic constants, and the answer matched the measured speed of light.",
 "Magnetic monopoles would change one of Maxwell’s four equations. Searches have found none. What would a single detection mean for the theory?",
 "Hold a compass beside a wire and touch the wire briefly across the ends of a flashlight battery (only for a moment, since the wire heats). Reverse the battery. What does the needle do?")
add(5, "A glowing stove coil, an LED, and a lump of metal cooled until it carries current forever are all quantum facts you can see or build without a laboratory. This chapter and the next four lay out the rules behind them.",
 "How do we know that energy comes in quanta? Black-body spectra, the threshold frequencies of the photoelectric effect, and the sharp lines of atomic spectra all point the same way.",
 "What would you expect to see if energy were not quantized? Compare the dashed classical curve in the figure with the glow of a hot object.",
 "Look at a compact fluorescent bulb or an LED through a compact disc held at an angle. You will see separate colored lines, not a smooth rainbow. What do the lines tell you about the atoms inside?")
add(6, "Ask ten physicists what happens when a quantum measurement is made and you will hear several answers, all agreeing on every experiment ever done. This chapter sets out the answers and why choosing among them is hard.",
 "How do we know that superpositions are real and not just ignorance? Interference experiments with large molecules, built from hundreds of atoms, show wave behavior that a mere lack of knowledge could not produce.",
 "Collapse models predict a tiny extra heating of matter. What result from a sensitive experiment would favor one of them over the others?",
 "Hold two polarizing lenses, such as a pair of sunglass lenses, so that they block the light when crossed. Slide a third between them at 45 degrees. Why does light reappear?")
add(7, "In 2022 the Nobel Prize in Physics went to three experimenters who showed that nature breaks a rule Einstein thought it had to obey, the rule that what happens here depends only on what is here. No signal travels faster than light, and yet the rule fails.",
 "How do we know that the loopholes are closed? Experiments in 2015 set the detectors far enough apart, and chose settings fast enough, that no signal could connect them.",
 "If the CHSH combination were found never to exceed 2 in a carefully closed experiment, what would that say about quantum mechanics?",
 "Try to invent a strategy for a two-player game in which each player sees one private bit and must give an answer without talking. You will find that you cannot win more than 75 percent of rounds on average, while entangled players can reach about 85 percent.")
add(8, "A message sent as quantum states reveals eavesdroppers by the disturbance they cause, and a machine with enough perfect qubits could factor numbers that stump every classical computer. Neither idea is science fiction. Both are held back by noise.",
 "How do we know that a quantum computer has done something a classical one cannot? Look at how such claims are checked, and how some have been matched later by cleverer classical algorithms.",
 "What size of error-corrected machine, and what task, would make you conclude that a useful quantum advantage has arrived?",
 "Two bits have four possible states, and ten qubits are described by 1,024 amplitudes. Roughly how many amplitudes describe 300 qubits, and how does that compare with the number of atoms in the observable universe?")
add(9, "The electron’s magnetism has been measured to about twelve digits, and quantum electrodynamics predicts the same number. Measure the distance from New York to San Francisco as precisely and you would be right to within a few millionths of a meter.",
 "How do we know that renormalization is not just a trick to hide infinities? It makes predictions that experiments check to many digits, and effective-field-theory ideas explain why it works.",
 "A long-running disagreement over the muon’s magnetic moment was settled largely in the Standard Model’s favor by better calculations. What kind of disagreement would be harder to explain away?",
 "Draw the simplest Feynman diagram in which two electrons repel each other. Label the lines and say which one is virtual.")
add(10, "Every ordinary thing is built from three kinds of particle: up quarks, down quarks and electrons. The Standard Model needs seventeen to account for everything accelerators have produced, and no experiment has shown it to be wrong within its domain.",
 "How do we know that quarks exist if none has ever been seen alone? Scattering experiments, jets of particles in collisions and the pattern of known particles all require them.",
 "Proton decay or a new particle at the Large Hadron Collider would each demand more than the Standard Model. Which one would you expect to see first, and why?",
 "Count the quarks and electrons in one water molecule. (Answer: 28 up quarks, 26 down quarks and 10 electrons.)")
add(11, "The Standard Model cannot say what most matter is, why there is any matter at all, or why neutrinos weigh anything. This chapter is a list of those holes and of the best ideas for filling them.",
 "How do we know that new physics is needed? Neutrino masses, dark matter and the excess of matter over antimatter are each firmly observed and absent from the model.",
 "Many arguments of naturalness predicted new particles that the Large Hadron Collider did not find. Does that weaken the arguments, or only the particular models?",
 "Naturalness predicted the charm quark correctly and failed for the cosmological constant. Find one other case in this book where an elegance argument succeeded or failed.")
add(12, "A teaspoon of neutron-star material would weigh billions of tonnes, and nothing like it can be made on Earth. What the stuff is made of is being answered with gravitational waves and X-ray telescopes.",
 "How do we know the size of a neutron star? Pulsar X-ray timing and the deformation of merging stars in gravitational waves each give radii of about 11 to 13 kilometers.",
 "What would a neutron star heavier than about 2.3 solar masses tell us about the matter inside it?",
 "Atomic nuclei have a density of about 2 × 10¹⁷ kilograms per cubic meter. Estimate the radius of a ball of such matter with the Sun’s mass. (Answer: about 13 km.)")
add(13, "A kilogram of uranium-235, completely fissioned, would release as much energy as about three thousand tonnes of coal. A kilogram of hydrogen fused to helium releases roughly eight times more again. The gulf between a chemical fire and a nuclear one is a factor of millions, and it comes from one curve.",
 "How do we know that the Sun runs on fusion? Neutrinos from the Sun’s core, including those from the carbon–nitrogen–oxygen cycle, have been detected in underground experiments.",
 "If solar neutrinos had come out at a tenth of the predicted rate and no oscillation had been found, what would that have said about the Sun’s core?",
 "Use E = mc² to find how much mass the Sun converts to radiation every second, given its power of 3.8 × 10²⁶ watts. (Answer: about four million tonnes.)")
add(14, "Right now about sixty billion neutrinos from the Sun pass through your thumbnail every second, and almost none interact. That they exist at all was proposed in desperation, to rescue the conservation of energy.",
 "How do we know that neutrinos have mass? A neutrino produced as one flavor is found later as another, and that can happen only if the flavors are mixtures of states with different masses.",
 "The absolute mass scale is still unknown. What measurement of tritium decay or of the cosmic microwave background would surprise current expectations?",
 "If 65 billion solar neutrinos cross each square centimeter every second, roughly how many cross your body, about 0.7 square meters in cross-section, each second? (Answer: about 5 × 10¹⁴.)")
add(15, "Mendeleev left gaps in his table of 1869 and predicted what would fill them. Within two decades gallium, scandium and germanium turned up with nearly the properties he had foretold. A chart built from chemistry turned out to be a map of electron shells.",
 "How do we know that atoms are mostly empty space? Rutherford’s students fired alpha particles at gold foil, and nearly all passed straight through, with a few bouncing back from a tiny, dense nucleus.",
 "What would change if a new element beyond the current table were found to sit in the wrong column, with chemistry that breaks the pattern?",
 "An element has 2 electrons in its first shell, 8 in its second and 1 in its third. What is it? (Answer: sodium.)")
add(16, "Why does iron rust, bread rise, vinegar sting and a battery run down? Each is a rearrangement of electrons, shared, transferred or promoted, and the rules for it fit on a page.",
 "How do we know that a chemical bond is a sharing of electrons? X-ray diffraction maps the distribution of electron density in molecules and shows it piled between bonded atoms.",
 "What measurement would show that a reaction is faster because of a catalyst and not merely because of heating?",
 "Stir baking soda into vinegar in a cup and feel the cup. The reaction absorbs heat. How does the temperature change relate to the bubbling?")
add(17, "A silicon chip holds tens of billions of switches, each a few dozen atoms across. A soap film, a rubber band and a lightning bolt belong to the same chapter. What unites them is that large numbers of particles do things no single one can.",
 "How do we know a material’s band gap? Light of lower energy than the gap passes through, and light above it is absorbed, so the color and the onset of absorption reveal it.",
 "A new material is claimed to be a superconductor at room temperature. What measurements would you demand before accepting it?",
 "The gap in electron-volts is about 1240 divided by the longest wavelength in nanometers that the material absorbs or emits. What gap does a 620 nm red LED have? (Answer: about 2 eV.)")
add(18, "Light leaves a flashlight at the same speed whether you stand still or chase it. That single fact, believed before it was understood, bends time and length, and the muons raining down from the upper atmosphere show that it does.",
 "How do we know that time dilation is real? Cosmic-ray muons live far longer in our frame than at rest, atomic clocks on aircraft lose time, and particle accelerators rely on it every day.",
 "What would a variation of the speed of light with direction or with the speed of the source mean for special relativity?",
 "A muon lives 2.2 microseconds at rest. How far does it travel at nearly the speed of light without time dilation, and with a Lorentz factor of 15.8? (Answer: about 660 m and about 10 km.)")
add(19, "Stand on a scale in a falling elevator and it reads zero. You are weightless, though gravity has not gone anywhere. That was Einstein’s happiest thought: gravity and acceleration are one thing, and what we call the force of gravity is the shape of spacetime.",
 "How do we know that spacetime is curved? Starlight bent around the Sun in 1919, the precession of Mercury’s orbit, time delays of radar signals and the waves from merging black holes all fit.",
 "The equivalence principle has been tested to a few parts in a quadrillion. What kind of deviation would point to new physics?",
 "Drop a pen and a coin side by side. In the falling frame, is there any local experiment that tells you apart from floating in empty space?")
add(20, "Your phone knows where you stand to within a few meters because it can tell time to a few billionths of a second. The clocks that do it would drift by tens of microseconds a day if relativity were ignored. Navigation is the most widely used test of Einstein’s theories ever made.",
 "How do we know the corrections are right? Satellite clocks are tuned before launch to allow for them, and the system’s accuracy shows that the rates match prediction.",
 "What would the positioning error look like if only the special-relativistic correction had been applied?",
 "Light travels 300 meters in a microsecond. If an uncorrected clock gains 38 microseconds in a day, how far off would a position fix be after one day? (Answer: about 11 km.)")
add(21, "On 14 September 2015 two mirrors four kilometers apart moved by less than a thousandth of the width of a proton. The movement came from two black holes that had collided 1.3 billion light-years away. It took a century of theory and fifty years of instrument-building to hear it.",
 "How do we know the signal was not noise? Two detectors a continent apart saw the same waveform within ten milliseconds, and the chance of a false alarm was about once in two hundred thousand years.",
 "A detection that appeared in only one detector, or with a delay longer than the light-travel time between them, would be viewed with suspicion. Why?",
 "The two LIGO sites are about 3,000 km apart. What is the largest delay a gravitational wave traveling at light speed can show between them? (Answer: about 10 ms.)")
add(22, "Squeeze the Sun to a ball six kilometers across and light could no longer escape it. We now photograph the shadows of such objects, hear them collide, and watch stars orbit one at the center of our own galaxy. What happens inside is the least tested part of general relativity.",
 "How do we know that black holes exist? Stars at the Milky Way’s center orbit a dark, compact mass of four million Suns, and gravitational waves match the merger of horizons.",
 "A confirmed deviation in the shape of a black hole’s shadow or in its ringdown would point to physics beyond general relativity. What precision is needed?",
 "Find the Schwarzschild radius of the Earth from 2GM/c². (Answer: about 9 mm.) What does it say about the density of a black hole’s contents?")
add(23, "Black holes are black because nothing escapes them, and yet in 1974 Stephen Hawking showed that they should glow faintly and slowly shrink. The glow has never been seen, and the argument for it ties together gravity, quantum theory and heat.",
 "How do we know the radiation exists if no one has seen it? We do not. Laboratory analogues, such as sound-wave horizons in cold gases, show the mechanism, and the thermodynamics of black holes requires it.",
 "Seeing the evaporation of a tiny primordial black hole would confirm Hawking. What would its final burst look like?",
 "A solar-mass black hole has a temperature of about 60 nanokelvin. The cosmic background is 2.7 kelvin. In which direction does heat flow between them today?")
add(24, "Burn a book and its information survives, in principle, in the smoke and ash. Throw it into a black hole that later evaporates and, Hawking argued, it might be gone for good. A fifty-year argument over that claim has produced holography.",
 "How do we know that quantum evolution must preserve information? The equations of quantum mechanics are reversible, and every other known process obeys them.",
 "What would convince you that information really is lost when a black hole evaporates, and what else in physics would have to give?",
 "Write down two reasons a physicist might be willing to give up the conservation of quantum information, and two reasons she might not.")
add(25, "The Solar System is a record of a single afternoon, cosmically speaking. A cloud of gas and dust collapsed about 4.57 billion years ago, and the craters of the Moon and the rings of Saturn are leftovers of what happened next.",
 "How do we know the Solar System’s age? Uranium and lead in the oldest meteorites give 4.567 billion years, and the Moon rocks and Earth’s oldest minerals agree within the expected delays.",
 "A meteorite found to be much older than the rest would contradict a single, shared formation. What would that suggest?",
 "Find Jupiter with the naked eye, then with binoculars look for up to four small points of light beside it. Watch them over two nights and sketch how they move.")
add(26, "Tens of thousands of tonnes of cosmic dust fall on Earth every year, and now and then something much larger arrives. Small bodies hold the oldest surviving material in the Solar System, and one day one of them will have to be moved.",
 "How do we know that meteorites come from asteroids? Fireball tracks have been traced to the asteroid belt, spectra match, and returned samples from Ryugu and Bennu are like the meteorites.",
 "If an asteroid’s orbit were found to give it a 1-in-100 chance of impact, what would you want to know before acting?",
 "Watch the sky on a dark night for an hour and count meteors. Repeat during a meteor shower. What changes, and why?")
add(27, "Thirty years ago nobody knew whether other stars had planets. Now more than six thousand are known, and the most common kind, between Earth and Neptune in size, does not exist in our own Solar System.",
 "How do we know that a dip in starlight is a planet? The dip repeats on a fixed period, the star’s velocity often confirms it, and statistics rule out most look-alikes.",
 "What observation of an Earth-size planet’s atmosphere would suggest life, and what would show that a gas had a lifeless source?",
 "A Jupiter-size planet blocks about 1 percent of a Sun-like star’s light. By what fraction does an Earth-size planet dim it? (Answer: about 0.008 percent, or 84 parts per million.)")
add(28, "A star is a ball of gas in a standoff: gravity squeezes inward, heat from fusion pushes outward, and the stalemate lasts for millions to trillions of years until the fuel runs out. Almost everything heavier than helium in your body was made in such a standoff.",
 "How do we know what is inside a star? The Sun’s vibrations map its interior, neutrinos come straight from its core, and the spectra of other stars show the products of burning.",
 "A star of known mass found to be far older than its mass allows would be a puzzle. What would you check first?",
 "Estimate the Sun’s main-sequence lifetime: it can burn about a tenth of its mass at 0.7 percent efficiency, at a power of 3.8 × 10²⁶ watts. (Answer: about ten billion years.)")
add(29, "In 2007 astronomers combing archived data found a flash of radio waves lasting a thousandth of a second that had crossed billions of light-years. Since then bursts have been traced to magnetized neutron stars, and a cosmic ray carrying about as much energy as a pitched baseball has been caught.",
 "How do we know that fast radio bursts come from outside our galaxy? The longer a burst has traveled through gas, the more its low frequencies are delayed, and the delays are too large for local sources. Several have been traced to distant host galaxies.",
 "A repeating burst found to come from an ordinary star in our own galaxy would change the picture. Which would you give up, the magnetar idea or the cosmological distances?",
 "Why do cosmic rays arrive from all directions, while neutrinos and light from the same source point back to it?")
add(30, "Our galaxy holds a few hundred billion stars and is one of perhaps a trillion in the observable universe. Their arrangement into filaments and voids is the oldest message in the cosmos, written in tiny fluctuations before any star existed.",
 "How do we know that Andromeda and other galaxies lie outside our own? In 1923 Edwin Hubble found Cepheid variable stars in Andromeda, whose faintness placed it far beyond the Milky Way.",
 "Simulations that include dark matter reproduce the cosmic web. What pattern of galaxies would they fail to reproduce?",
 "On a clear autumn night, find the faint smudge of the Andromeda galaxy with the naked eye. The light you see left it about 2.5 million years ago.")
add(31, "In 1929 Edwin Hubble found that distant galaxies recede faster the farther away they are. The universe has no center from which they flee. Space itself is stretching, and the farther two points lie apart, the faster the stretching carries them away.",
 "How do we know the expansion is real? The light curves of distant supernovae are stretched in time, the background radiation was hotter in the past, and the pattern fits one expansion history.",
 "A disagreement between the Hubble constant measured nearby and from the early universe has persisted for years. What would settle it as new physics or as an error?",
 "Draw dots on a balloon and measure the distances between three of them before and after inflating it. Which dot seems to be the center of the expansion?")
add(32, "The oldest light in the universe reaches us from every direction as a faint microwave glow at 2.7 kelvin. A small part of the static on an old analog television was this light, set free 380,000 years after the Big Bang when the universe cooled enough for atoms to form.",
 "How do we know there was a Big Bang? The expansion, the background radiation, the abundances of hydrogen and helium and the way galaxies have evolved all fit one hot, dense beginning.",
 "A star older than the universe, or a helium fraction far from 25 percent in the oldest gas, would contradict the picture. How are those two quantities measured?",
 "The universe has expanded by a factor of about 1,100 since the light of the background was released, and its temperature today is 2.7 K. What was its temperature then? (Answer: about 3,000 K.)")
add(33, "Stars and gas make up barely a tenth of the matter in a galaxy. The rest, and an even stranger something that speeds up the expansion, has never been seen in any laboratory. Seventy percent of the cosmos is described by a number, not a substance.",
 "How do we know dark matter is not just modified gravity? The Bullet Cluster, the pattern of the microwave background and the growth of structure all fit invisible mass better than a change to the law.",
 "A particle found in an underground detector or a collider would settle the question one way. What result would favor modified gravity instead?",
 "A galaxy’s stars orbit at nearly constant speed far from its center. Sketch the mass you would need as a function of radius to make that happen.")
add(34, "General relativity and quantum theory each pass every test we can give them, and they contradict each other at the smallest scales. A theory that joins them needs energies a million billion times beyond our accelerators, so ideas must be judged by consistency until nature offers more.",
 "How do we know that string theory is physics and not mathematics? Today we do not: it has made no confirmed prediction. Its test is whether it can.",
 "What result in cosmology, particle physics or black-hole physics would count against the whole string programme?",
 "List three requirements any theory of quantum gravity must meet, and judge which of them each programme in this chapter meets.")
add(35, "Film a cup falling and shattering, run it backward, and everyone knows which film is real. Yet the equations of motion cannot tell the two apart. The difference lies not in the laws but in the state of the early universe.",
 "How do we know that entropy increases? Every large system observed obeys it, and laboratory experiments on tiny systems show the rare, brief violations that statistics allows.",
 "A process that regularly turned heat into work with no waste would break the second law. What would you check before believing a report of one?",
 "How likely is a freshly shuffled deck of cards to be in the original order? (Answer: 1 in about 8 × 10⁶⁷.)")
add(36, "Clocks tick at different rates for people who move or sit at different heights, no “now” is shared by everyone, and the equations for the whole universe may not contain time at all. The thing we feel most surely is the thing physics understands least.",
 "How do we know that there is no universal “now”? Experiments with fast-moving clocks and the structure of signals show that events simultaneous for one observer are not for another.",
 "What experiment could detect a preferred frame in which time is absolute?",
 "Imagine two lightning strikes at either end of a moving train, seen as simultaneous by someone on the platform. Why does a passenger in the middle disagree?")
add(37, "Life appeared on Earth within a few hundred million years of the planet becoming habitable, and no one has watched it start. What chemistry did in that window is the largest question between cosmology and biology.",
 "How do we know when life began? Carbon isotopes in ancient rocks and layered mats of microbes called stromatolites show living processes by about 3.5 billion years ago, with hints earlier.",
 "A fully lifeless explanation of every early trace would not prove life absent. What would settle it?",
 "List three things a protocell must do, and name a place on the early Earth that could supply each.")
add(38, "Every cell in your body descends, by an unbroken line of divisions, from the first cells almost four billion years ago. The cell is the smallest thing we call alive, and it is a city.",
 "How do we know that mitochondria were once bacteria? They have their own circular DNA and ribosomes and a double membrane, and their genes are closest to those of free-living bacteria.",
 "What would you conclude if a modern eukaryote were found with no trace of either endosymbiosis?",
 "Look at a drop of pond water or yogurt under a magnifier or a phone with a macro lens. What moves, and what stays still?")
add(39, "Darwin knew nothing of genes. He needed variation, inheritance and differences in survival, and he had the evidence for all three. The molecular century then supplied the machinery, and the pattern written in DNA matches the tree he drew from bones and beaks.",
 "How do we know that species share common ancestors? Genes and broken genes are shared in a nested pattern, as are inserted viral fragments, in exactly the places an ancestry tree predicts.",
 "A rabbit fossil in rock a billion years old would overturn evolutionary history. Why has nothing like it ever been found?",
 "Draw the arm bones of a human, the wing of a bat and the flipper of a whale side by side, and match them bone by bone.")
