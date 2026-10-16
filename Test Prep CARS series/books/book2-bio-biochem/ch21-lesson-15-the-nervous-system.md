# Lesson 15: The Nervous System

**What you will be able to do**

- Explain how ion gradients, selective permeability and the Nernst and Goldman-Hodgkin-Katz (GHK) ideas set the resting membrane potential.
- Describe the phases of an action potential in terms of voltage-gated channel behavior, and predict the effect of channel blockers and ion changes.
- Explain how myelin and saltatory conduction speed up signals, and what happens when myelin is damaged.
- Trace events at a chemical synapse, compare common neurotransmitters and receptors, and apply temporal and spatial summation.
- Divide the nervous system into central, peripheral, somatic and autonomic parts, and match brain regions to functions.
- Follow a reflex arc and describe in outline how sensory receptors turn stimuli into electrical signals.

**Why it matters for the exam**

This lesson covers category 3A, the nervous system, and it is one of the most reliable sources of passage-based questions in the section. Almost everything here is applied physical chemistry. The membrane is a capacitor and a set of resistors (Book 1, Lesson 5), ion gradients are concentration cells (Book 1, Lesson 17, the Nernst equation), and the speed of a signal depends on resistance and insulation. The ion pumps and channels were introduced in [Lesson 12](chapter:17), and the receptor logic (GPCRs, second messengers, ligand-gated channels) is the same logic reused here. The outputs of this system, including muscle control, connect to [Lesson 16](chapter:22) on hormones and to the organ-systems lessons that follow. The behavior side of the nervous system (perception, learning, memory, emotion and the psychology of the brain) is covered in Book 3, and this lesson stays with the cellular and anatomical biology. Where a topic continues there, the text says so in plain words.

Praxis Tip: In any neuron question, ask which ion is moving, in which direction, and what that does to the membrane potential. Then decide whether the cell is moving toward threshold or away from it.

**Concept Review**

**The neuron.** The neuron is the signaling cell of the nervous system. Its **dendrites** receive input and its **cell body (soma)** integrates it and contains the nucleus and most of the protein synthesis. The **axon** carries the output, starting at the **axon hillock** (the axon initial segment), which has a high density of voltage-gated sodium channels and is generally where the action potential begins. The axon ends in **terminal boutons**, which release neurotransmitter. **Glial cells** support neurons and outnumber them in most regions. **Astrocytes** regulate the chemical environment, take up neurotransmitters and form part of the blood-brain barrier. **Oligodendrocytes** make myelin in the central nervous system, while **Schwann cells** do so in the peripheral nervous system. **Microglia** are the resident immune cells of the brain. **Ependymal cells** line the ventricles and help make cerebrospinal fluid.

**The resting membrane potential.** At rest, a neuron's interior is about −70 mV relative to the outside (the value varies by cell type [VERIFY]). Three facts combine to produce this.

1. The **Na⁺/K⁺-ATPase** ([Lesson 12](chapter:17)) maintains a high K⁺ and low Na⁺ concentration inside. Typical values are roughly 140 mM K⁺ inside and 5 mM outside, and roughly 10 mM Na⁺ inside and 145 mM outside.
2. The membrane has open "leak" K⁺ channels, so at rest it is far more permeable to K⁺ than to Na⁺.
3. K⁺ leaves down its concentration gradient, leaving unbalanced negative charge (mostly trapped anionic proteins and phosphates) behind, until the electrical force balances the chemical force.

For a single ion, the equilibrium is given by the **Nernst equation**: E = (61.5 mV / z) log₁₀([out] / [in]) at 37 °C. With the values above, E(K) is about −89 mV and E(Na) is about +71 mV. The real resting potential is not at either value. It lies between them, close to E(K), because the membrane is mostly permeable to K⁺ with a small Na⁺ leak. The **GHK equation** captures this idea: the membrane potential is a permeability-weighted average of the Nernst potentials, so the ion with the highest permeability dominates. In symbols for K⁺ and Na⁺ only:

Vm = 61.5 log₁₀( (PK[K]out + PNa[Na]out) / (PK[K]in + PNa[Na]in) )

You do not need to memorize the full form for the exam, but you should be able to reason: raise the permeability of an ion and Vm moves toward that ion's Nernst potential. The pump matters over the long run because it prevents the gradients from running down, but its direct electrical contribution to Vm is small ([Lesson 12](chapter:17)).

Because the potential depends on the gradients, changing the extracellular K⁺ matters. A higher extracellular K⁺ makes E(K) less negative and depolarizes the cell. This is why a high blood potassium level is dangerous for the heart and nerves.

Terms to keep straight: **depolarization** means Vm becomes less negative (toward zero or positive); **hyperpolarization** means more negative; **repolarization** is the return toward rest. **Driving force** for an ion is Vm − E(ion); the ion flows in the direction that moves Vm toward its E, and the size of the current also depends on how many channels are open.

**The action potential.** A neuron is **excitable**: when depolarization reaches a **threshold** (about −55 mV [VERIFY]), it fires an action potential, an all-or-none event of fixed size. The sequence follows the behavior of voltage-gated channels.

1. **Depolarization to threshold.** Input opens enough voltage-gated Na⁺ channels to start a positive feedback loop: more depolarization opens more Na⁺ channels, which depolarizes the membrane further.
2. **Rising phase.** Na⁺ rushes in (the driving force is large and inward), and Vm swings toward E(Na), reaching about +30 to +40 mV, not all the way to E(Na), because the Na⁺ channels inactivate and K⁺ channels begin to open.
3. **Falling phase.** The Na⁺ channels **inactivate** (an inactivation gate closes within about a millisecond), and the slower **voltage-gated K⁺ channels** open, so K⁺ leaves and Vm repolarizes.
4. **Undershoot (afterhyperpolarization).** K⁺ channels stay open briefly after repolarization, so Vm dips close to E(K), below rest.
5. **Return to rest.** K⁺ channels close, and Vm settles back at rest. The Na⁺/K⁺ pump restores the small ion shifts over a longer time; each action potential moves only a tiny fraction of the ions.

The action potential is **all-or-none**: a stronger stimulus does not make a bigger spike; it makes more spikes per second. Intensity is therefore encoded in the **firing frequency**, and the identity of the stimulus is encoded by which neurons fire.

The **refractory period** limits firing. In the **absolute refractory period**, the Na⁺ channels are inactivated and no stimulus, however strong, can trigger another spike. In the **relative refractory period**, some Na⁺ channels have recovered but K⁺ channels are still open and Vm is hyperpolarized, so a stronger-than-normal stimulus is needed. The refractory period is also why the impulse travels in one direction along an axon: the region behind the spike is inactivated.

The effects of drugs and toxins follow from these steps. Tetrodotoxin (from pufferfish) blocks the voltage-gated Na⁺ channel, so no action potentials fire. Local anesthetics such as lidocaine also block Na⁺ channels. Blocking voltage-gated K⁺ channels (for example with tetraethylammonium in the lab) prolongs the action potential because repolarization is slowed.

Praxis Tip: Learn the action potential as a story of two gates. Sodium channels open fast and then close themselves; potassium channels open slowly and stay open. Almost every question on the topic is that sentence applied to a drug or a mutation.

**Propagation, myelin and saltatory conduction.** An action potential regenerates itself along the axon: Na⁺ entering at one point spreads depolarizing current to the neighboring membrane, which brings it to threshold. Two properties set the speed. A **larger axon diameter** lowers the internal resistance, so current spreads farther and faster (the giant axon of the squid is a classic example). **Myelin**, a stack of insulating membrane wrapped around the axon, raises the membrane resistance and lowers its capacitance, so current spreads much farther along the axon before leaking out. The myelin sheath has gaps called **nodes of Ranvier**, which have a very high density of voltage-gated Na⁺ channels. The action potential is regenerated at the nodes only, and the signal appears to jump from node to node: **saltatory conduction** (from the Latin for leaping). This increases speed and saves energy, because fewer ions cross the membrane (so the pump has less work to do). In **demyelinating diseases** such as multiple sclerosis (an autoimmune attack on CNS myelin) or Guillain-Barré syndrome (a peripheral nerve disorder), conduction slows or fails because current leaks out of the bare axon and no longer reaches the next node. Unmyelinated axons conduct slowly (on the order of 1 m/s [VERIFY]), while large myelinated axons can conduct at tens of meters per second.

**The synapse.** A **synapse** is a junction where one neuron signals another cell. A few electrical synapses use gap junctions ([Lesson 12](chapter:17)), but most synapses are chemical. The steps at a chemical synapse are:

1. An action potential arrives at the presynaptic terminal and opens **voltage-gated Ca²⁺ channels**.
2. Ca²⁺ enters (the gradient strongly favors entry), and triggers **fusion of synaptic vesicles** (exocytosis, with SNARE proteins) with the membrane.
3. The neurotransmitter diffuses across the **synaptic cleft** (a few tens of nanometers), a quick process.
4. It binds **postsynaptic receptors**, which are either ligand-gated ion channels (**ionotropic**, fast, direct) or GPCRs (**metabotropic**, slower, and acting through second messengers).
5. The signal is terminated by **reuptake** into the terminal or into astrocytes, by **enzymatic degradation** in the cleft, or by diffusion away.

Calcium is the essential presynaptic signal. Removing external Ca²⁺ or blocking its channels stops transmitter release, though the action potential still reaches the terminal. Botulinum toxin cleaves SNARE proteins and prevents release of acetylcholine at the neuromuscular junction, causing paralysis.

A neurotransmitter is not by itself excitatory or inhibitory. The effect depends on the receptor and the ion it controls. An **excitatory postsynaptic potential (EPSP)** is a small depolarization, for instance from opening channels that pass Na⁺ (and K⁺). An **inhibitory postsynaptic potential (IPSP)** is usually a hyperpolarization or a stabilization of the potential, from opening K⁺ channels or Cl⁻ channels. Postsynaptic potentials are **graded** (their size depends on the amount of transmitter) and **decay with distance**, unlike action potentials.

| Transmitter | Main receptor action | Notes |
|---|---|---|
| Glutamate | Excitatory | Main fast excitatory CNS transmitter |
| GABA | Inhibitory (Cl⁻ in) | Main fast inhibitory brain transmitter |
| Glycine | Inhibitory | Mainly spinal cord and brainstem |
| Acetylcholine | Nicotinic or muscarinic | Neuromuscular junction, autonomic |
| Norepinephrine | Adrenergic GPCRs | Sympathetic; alertness |
| Dopamine | GPCRs | Movement, reward |
| Serotonin | Mostly GPCRs | Mood, sleep, gut motility |

Acetylcholine is a good example of one transmitter with two receptor families. At the skeletal neuromuscular junction it binds **nicotinic** receptors, which are ligand-gated cation channels, and causes fast depolarization of muscle. In the heart, it binds **muscarinic** receptors (GPCRs), which slow the heart rate. The enzyme **acetylcholinesterase** breaks acetylcholine down in the cleft, and inhibitors of this enzyme (certain nerve agents and pesticides) cause acetylcholine to accumulate and overstimulate. Many drugs act at synapses: some block receptors, some block reuptake (this raises transmitter levels in the cleft), and some inhibit degradation. The psychology of these drugs is Book 3 material.

**Summation.** One EPSP is usually too small to trigger an action potential. The postsynaptic neuron adds its inputs at the axon hillock. **Temporal summation** adds EPSPs that arrive from the same synapse in rapid succession, before the earlier one has decayed. **Spatial summation** adds inputs that arrive at different synapses at the same time. IPSPs subtract. If the sum at the hillock reaches threshold, the neuron fires. Synapses close to the soma or hillock count more than those far out on the dendrites, because of decay with distance. Over longer times, synapses change strength with activity (synaptic plasticity), which is the cellular basis for learning, discussed further in Book 3.

**Organization of the nervous system.** The **central nervous system (CNS)** consists of the brain and spinal cord. The **peripheral nervous system (PNS)** consists of nerves and ganglia outside them. The PNS divides by function:

- The **sensory (afferent)** division carries information toward the CNS.
- The **motor (efferent)** division carries commands away, and has two parts: the **somatic** system, which controls skeletal muscle (voluntary, though reflexes are included), and the **autonomic** system, which controls smooth muscle, cardiac muscle and glands (generally involuntary).

The **autonomic nervous system** has two opposing divisions. Autonomic pathways use two neurons in sequence: a **preganglionic** neuron whose cell body is in the CNS, and a **postganglionic** neuron whose cell body is in a ganglion.

| Feature | Sympathetic | Parasympathetic |
|---|---|---|
| Overall effect | Fight or flight | Rest and digest |
| Preganglionic transmitter | Acetylcholine | Acetylcholine |
| Postganglionic transmitter | Norepinephrine (mostly) | Acetylcholine |
| Ganglia | Near the spinal cord | Near or in the target |

Generally, the sympathetic system raises heart rate and blood pressure, dilates the airways and pupils, mobilizes glucose and decreases digestion; the parasympathetic system (the **vagus nerve** is its main route) slows the heart, constricts the pupils, and stimulates digestion. Most organs receive both, and the net effect reflects the balance. A notable exception is the adrenal medulla, which acts like a modified sympathetic ganglion and releases epinephrine into the blood ([Lesson 16](chapter:22)). The **enteric nervous system** in the gut wall can also operate on its own.

Praxis Tip: Preganglionic neurons in both autonomic divisions release acetylcholine onto nicotinic receptors. Only the postganglionic ending separates the two (norepinephrine for sympathetic, acetylcholine for parasympathetic). That one fact answers many drug questions.

**Brain regions.** The brain is organized in a few large divisions.

| Region | Main functions |
|---|---|
| Cerebral cortex | Perception, thought, voluntary movement, language |
| Basal ganglia | Movement initiation and selection |
| Thalamus | Relay of sensory input to cortex |
| Hypothalamus | Homeostasis; controls pituitary |
| Hippocampus, amygdala | Memory formation; emotion and fear |
| Cerebellum | Coordination, balance, motor learning |
| Brainstem | Breathing, heart rate, arousal, reflexes |

The cerebral cortex is divided into lobes: **frontal** (planning, judgment, voluntary motor control, speech production), **parietal** (somatosensory processing and spatial awareness), **temporal** (hearing, language comprehension, some memory), and **occipital** (vision). The primary motor and sensory cortices are arranged as maps of the body. Each cerebral hemisphere generally receives sensory input from and controls movement of the opposite side of the body. The **thalamus** relays most sensory information to the cortex (smell is a notable exception [VERIFY]). The **hypothalamus** controls temperature, hunger, thirst, circadian rhythms and the pituitary ([Lesson 16](chapter:22)). The **cerebellum** refines movement and balance; damage causes clumsy, poorly coordinated movement. The **basal ganglia** are involved in starting movements, and loss of dopamine-producing neurons in this circuit occurs in Parkinson disease. The **brainstem** (midbrain, pons, medulla) controls vital functions such as breathing and heart rate; the medulla in particular contains cardiovascular and respiratory centers. The **spinal cord** carries sensory fibers in through the **dorsal root** and motor fibers out through the **ventral root** (the Bell-Magendie law). The brain and spinal cord have gray matter (cell bodies and synapses) and white matter (myelinated axons), and are protected by the meninges, cerebrospinal fluid and the blood-brain barrier. For how these regions give rise to behavior, see Book 3.

**Reflex arcs.** A **reflex** is a rapid, stereotyped response to a stimulus that does not require conscious thought. A reflex arc has five parts: a receptor, a sensory (afferent) neuron, an integration center in the CNS, a motor (efferent) neuron, and an effector (muscle or gland). The **monosynaptic stretch reflex** (the knee-jerk) has only one synapse in the CNS, between the sensory and motor neurons, and the muscle contracts. Most reflexes also involve interneurons: in the **withdrawal reflex**, a painful stimulus excites flexor motor neurons by way of interneurons and inhibits the opposing extensor muscles at the same time (reciprocal inhibition). Because the integration center is the spinal cord, the response occurs before the brain is aware of the stimulus.

**Sensory transduction.** A sensory receptor converts a stimulus into a **receptor potential**, a graded change in membrane potential, which then sets the rate of action potentials in the sensory neuron. The mechanisms differ with the modality. **Mechanoreceptors** (touch, hearing, balance) have mechanically gated channels. **Photoreceptors** in the retina use a GPCR cascade: in the dark, rods and cones are depolarized by a steady current, and light activates a G protein, lowers cyclic GMP, closes channels, and **hyperpolarizes** the cell (an unusual case of light reducing, not increasing, transmitter release). **Chemoreceptors** (taste and smell) use GPCRs (and channels for some tastes) and second messengers. **Thermoreceptors** and **nociceptors** use temperature- and chemical-sensitive channels. Receptors **adapt**: with a constant stimulus, firing falls. Rapidly adapting receptors report changes, and slowly adapting receptors report sustained levels. The eye and the ear in more detail, and the perception built from them, are covered in Book 3.

**Worked Example 1: Nernst potential and driving force (skill: gradients)**

A neuron has [Na⁺] of 12 mM inside and 145 mM outside at 37 °C. Find E(Na), and then the driving force on Na⁺ at a membrane potential of −70 mV. With E(K) = −89 mV, compare the driving force on K⁺.

E(Na) = 61.5 log(145 / 12) = 61.5 × 1.082 = about +67 mV. Driving force = Vm − E = −70 − 67 = −137 mV. The negative value means a strong inward drive for Na⁺: the electrical and chemical forces both pull it in. For K⁺, Vm − E(K) = −70 − (−89) = +19 mV, a small outward drive, because Vm is close to E(K). This is why opening Na⁺ channels causes a large current and why the resting membrane is nearly at equilibrium for K⁺.

**Worked Example 2: Permeability and the GHK idea (skill: reasoning)**

Use Vm = 61.5 log( (PK[K]out + PNa[Na]out) / (PK[K]in + PNa[Na]in) ), with [K]out = 5, [K]in = 140, [Na]out = 145, [Na]in = 10 mM. Compare PNa/PK = 0.04 (rest) with PNa/PK = 5 (peak of the action potential).

At rest: numerator = 5 + 0.04 × 145 = 10.8; denominator = 140 + 0.04 × 10 = 140.4; ratio 0.0769; Vm = 61.5 × (−1.114) = about −69 mV. At the peak: numerator = 5 + 5 × 145 = 730; denominator = 140 + 5 × 10 = 190; ratio 3.84; Vm = 61.5 × 0.585 = about +36 mV. The membrane potential moves toward the Nernst potential of whichever ion dominates the permeability. The model contains only two ions, and the real values depend on the cell type, but the logic is the exam-level point.

**Worked Example 3: Channel blockers (skill: experimental reasoning)**

In a patch of axon, the stimulus depolarizes the membrane from −70 mV to −40 mV. Predict the voltage trace after (a) tetrodotoxin, and (b) a K⁺ channel blocker given at a dose that does not affect Na⁺ channels.

(a) With the Na⁺ channels blocked, there is no regenerative inward current. The membrane depolarizes only as far as the stimulus pushes it, and then returns to rest through leak K⁺ current, so there is no action potential. (b) With K⁺ channels blocked, the rising phase is normal, but repolarization is slow and incomplete, so the action potential is widened (prolonged) and has little or no undershoot. The tracing is a longer spike, not a taller one, because the peak is limited by Na⁺ channel inactivation, not by K⁺ channels.

**Worked Example 4: Summation (skill: quantitative reasoning)**

A neuron has a resting potential of −70 mV and a threshold of −55 mV. Each EPSP depolarizes the hillock by 6 mV when it arrives alone, and each IPSP hyperpolarizes by 4 mV. Does the neuron fire if (a) three excitatory synapses fire simultaneously, (b) the same three fire together with one inhibitory synapse?

(a) The change is +18 mV, giving −52 mV, which is above threshold (less negative than −55), so the neuron fires. (b) Net change is 18 − 4 = +14 mV, giving −56 mV, which is just below threshold, so no action potential occurs. A single inhibitory input can veto a group of excitatory ones when the sum is close to threshold. The simple additive model ignores decay with distance, which would shrink distant inputs.

**Worked Example 5: Myelin and conduction time (skill: scaling)**

A motor axon 1.0 m long conducts at 1 m/s when unmyelinated and at 50 m/s when myelinated. Compare the travel times, and explain what a nerve with failing myelin would do to the delay.

Unmyelinated: t = 1.0 m / 1 m/s = 1 s. Myelinated: t = 1.0 / 50 = 0.02 s, or 20 ms. Myelin shortens the delay by a factor of 50 in this example. With damaged myelin, the current leaks and spreads less far, so conduction slows (the delay lengthens) and may fail entirely when the signal does not reach the next node above threshold. This produces weakness or sensory loss, as in multiple sclerosis.

**Worked Example 6: Following a drug through a synapse (skill: mechanism)**

A drug inhibits acetylcholinesterase. Predict the effects at (a) the skeletal neuromuscular junction, and (b) the heart.

Acetylcholine stays in the cleft and keeps acting on its receptors. (a) At the neuromuscular junction, nicotinic receptors are overstimulated, which causes persistent depolarization of the muscle end plate. Initially there may be twitching, and then weakness, because depolarized Na⁺ channels inactivate and the muscle cannot fire again. (b) In the heart, the excess acetylcholine acts on muscarinic receptors and slows the heart rate. The same molecular change gives different outcomes because the receptor types differ.

**More Praxis Tips**

Praxis Tip: Direction rules. Cation channels opening move Vm toward their positive Nernst potential (depolarization); K⁺ channels opening move Vm toward −89 mV or so (hyperpolarization); Cl⁻ channels opening hold Vm near E(Cl), which is close to rest (stabilization).

Praxis Tip: All-or-none refers to the action potential only. Synaptic potentials and receptor potentials are graded. If a graph shows a response that grows smoothly with stimulus size, it is not an action potential.

Praxis Tip: Myelin is not a pump or a channel. It is insulation, and its effect is on the spread of current. Remove the insulation and the cable leaks.

Praxis Tip: Calcium is the trigger for vesicle fusion. If a passage says transmitter release is lost but the action potential reaches the terminal normally, look for a calcium channel or SNARE problem.

Praxis Tip: For the autonomic system, ask where the ganglion lies and what the postganglionic transmitter is. Short preganglionic fibers in the sympathetic chain, long ones in the parasympathetic. The pattern is a useful anchor, though you will rarely need more than the transmitter.

Praxis Tip: When a passage describes a lesion, work out the side and level. Brain lesions mostly affect the opposite side of the body, spinal cord lesions affect the same side below the lesion for motor loss. [VERIFY] Do not spend long on this unless the passage supplies the anatomy.

Praxis Tip: Frequency, not size, encodes stimulus strength. A question showing a stronger stimulus will show more spikes, never taller ones.

**Common Mistakes**

- Saying that the Na⁺/K⁺ pump is what produces the resting potential directly; the leak K⁺ channels and the gradients do most of the work.
- Thinking that an action potential changes the ion concentrations significantly. It moves only a tiny fraction of the ions.
- Describing voltage-gated Na⁺ channels as simply "closing" at the peak, when they are inactivated; this is why the absolute refractory period exists.
- Treating a neurotransmitter as excitatory or inhibitory in itself, instead of looking at the receptor and the ion.
- Treating myelin as continuous: the action potential is regenerated at the nodes of Ranvier, not under the myelin.
- Mixing up afferent (toward the CNS) with efferent (away), and sympathetic with parasympathetic transmitters.
- Reading an IPSP as always a hyperpolarization (it may be a stabilization with little voltage change).
- Describing light as depolarizing a vertebrate photoreceptor, when it hyperpolarizes it.

**Checkpoint Questions**

1. A researcher raises the extracellular K⁺ concentration of a bathing solution from 5 mM to 15 mM, leaving everything else the same. What is the most likely immediate effect on the resting neuron?
   A. Hyperpolarization, because K⁺ now enters the cell
   B. No change, because the Na⁺/K⁺ pump sets the potential
   C. Depolarization, because E(K) becomes less negative
   D. Hyperpolarization, because E(Na) becomes more positive

2. During the falling phase of an action potential, the principal event is
   A. opening of voltage-gated K⁺ channels together with inactivation of Na⁺ channels
   B. opening of voltage-gated Ca²⁺ channels at the axon hillock
   C. closing of the leak K⁺ channels
   D. reversal of the Na⁺/K⁺ pump

3. A toxin binds to voltage-gated Na⁺ channels and keeps them from inactivating. Compared with a normal action potential, the spike will most likely be
   A. shorter, because depolarization ends sooner
   B. unchanged, because K⁺ channels set the duration
   C. smaller in amplitude, because fewer channels open
   D. prolonged, because inward Na⁺ current continues

4. Which sequence correctly orders events at a chemical synapse?
   A. Transmitter release, Ca²⁺ entry, vesicle fusion, receptor binding
   B. Ca²⁺ entry, vesicle fusion, receptor binding, postsynaptic potential
   C. Receptor binding, Ca²⁺ entry, vesicle fusion, postsynaptic potential
   D. Vesicle fusion, receptor binding, Ca²⁺ entry, transmitter release

5. A drug that blocks reuptake of a neurotransmitter into the presynaptic terminal would most likely
   A. decrease the amount of transmitter in the cleft
   B. block the voltage-gated Ca²⁺ channels
   C. increase and prolong the transmitter's action on postsynaptic receptors
   D. destroy the postsynaptic receptors

6. Which of the following correctly describes the autonomic nervous system?
   A. Preganglionic sympathetic neurons release norepinephrine
   B. Parasympathetic neurons release norepinephrine from their postganglionic endings
   C. Sympathetic activation slows the heart and stimulates digestion
   D. Both divisions release acetylcholine from their preganglionic neurons

7. A patient has a stroke that damages the cerebellum. The most likely deficit is
   A. clumsy, poorly coordinated movement with intact comprehension
   B. loss of vision in both eyes
   C. failure of breathing at rest
   D. inability to form any new memory

---

**Stop here.** Answer every question on scratch paper before you read the reasons.

**Answers and reasons**

1. **C.** Raising [K]out from 5 to 15 mM shrinks the gradient favoring K⁺ exit, so E(K) moves from about −89 mV to about −60 mV (61.5 × log(15/140)), and the resting potential, which follows E(K) closely, depolarizes. (A the gradient still favors K⁺ exit, only less so, which depolarizes rather than hyperpolarizes; B the pump maintains gradients over the long term but does not set the potential instantly; D E(Na) does not change here.)
2. **A.** The Na⁺ channels inactivate and the slower voltage-gated K⁺ channels open, so K⁺ efflux repolarizes the cell. (B Ca²⁺ channels are important at the terminal, not for the falling phase at the hillock; C closing leak channels would depolarize the cell; D the pump works slowly and does not reverse.)
3. **D.** If Na⁺ channels fail to inactivate, inward current continues and repolarization is delayed. (A would be true if channels closed sooner; B K⁺ channels open but cannot offset continuing Na⁺ entry; C the number of channels opening at the start is unchanged.)
4. **B.** The action potential opens Ca²⁺ channels, Ca²⁺ triggers vesicle fusion, the transmitter then binds receptors, and a postsynaptic potential follows. (A, C and D place release or binding before calcium entry, which would require the transmitter to be released without its trigger.)
5. **C.** Reuptake clears transmitter from the cleft, and blocking it leaves more transmitter for longer. (A is the opposite effect; B reuptake transporters are not calcium channels; D the drug does not act on receptors.)
6. **D.** Preganglionic neurons of both divisions release acetylcholine. (A the preganglionic sympathetic transmitter is acetylcholine; B parasympathetic postganglionic endings release acetylcholine; C describes parasympathetic effects.)
7. **A.** The cerebellum coordinates movement and balance, and its damage produces ataxia without loss of understanding. (B vision is processed in the occipital lobe; C breathing centers are in the brainstem; D new memories depend on the hippocampus.)

Praxis Tip: After the checkpoint questions, sort every miss into one of four types: wrong ion, wrong direction, wrong location, or wrong switch. Repeating the same type tells you what to review.

**Teach-Back and Spaced Review**

*Say this aloud in one breath:* "A neuron keeps K⁺ high inside and Na⁺ high outside with a pump, and its resting potential sits near the K⁺ Nernst potential because K⁺ channels are open; depolarization to threshold opens fast sodium channels, which then inactivate while slower potassium channels repolarize, producing an all-or-none spike, which jumps between the nodes of Ranvier in myelinated axons; at the terminal, calcium triggers vesicle release, and the transmitter's effect depends on the postsynaptic receptor and is added up with other inputs at the hillock; the brain and cord make up the CNS, the autonomic system balances sympathetic against parasympathetic, and reflexes loop through the cord."

*Review schedule:* revisit this lesson after 1 day (redo Worked Examples 1 and 4 without looking), after 3 days (checkpoint questions from a blank page), after 7 days (a mixed set including [Lesson 12](chapter:17) transport and Book 1, Lesson 17), and after 21 days (draw an action potential and label the channel states from memory, and then draw a synapse).

*Interleave:* alternate a nervous-system problem with a hormone problem ([Lesson 16](chapter:22)) and a membrane transport problem. Book 3 continues with the perception, behavior and cognition built on this biology.

Praxis Tip: End each study session by sketching one voltage trace and labeling, at each stage, which channels are open. If you can do that without notes, you can answer most of the questions on this topic.

---

**Author verification note (remove before publishing)**

- All examples and questions are original. Verified in Python: E(Na) with 12 and 145 mM = +66.6 mV (rounded to +67); E(K) = -89 mV; GHK values -68.5 mV and +36.0 mV; E(K) at 15 mM outside = -59.7 mV (text says about -60). Summation -52 and -56 mV; conduction times 1 s and 0.02 s.
- Answer key positions: C, A, D, B, C, D, A.
- Verify with a neuroscience reviewer: resting potential (-70 mV) and threshold (-55 mV) typical values; olfaction bypassing the thalamus; unmyelinated conduction speeds; the statement about spinal cord lesion laterality; photoreceptor hyperpolarization; the 61.5 mV constant at 37 degrees C.
- Category 3A topics covered: neurons and glia, resting and action potentials, myelin, synapses, neurotransmitters, receptors, summation, CNS/PNS, autonomic system, brain regions, reflexes and sensory transduction.
