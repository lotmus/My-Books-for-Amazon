# Lesson 11: Evolution and Diversity

**What you will be able to do**

- Define fitness and natural selection, and predict how directional, stabilizing, disruptive and balancing selection change a population.
- Distinguish selection from genetic drift, gene flow and mutation as forces that change allele frequencies, and apply the Hardy-Weinberg framework to selection and migration.
- Describe species concepts, isolating barriers and the main modes of speciation.
- Read a phylogenetic tree (cladogram): find sister groups and common ancestors, and decide whether a group is monophyletic.
- Use molecular data, a molecular clock, and anatomical and fossil evidence to reason about relatedness.
- Contrast adaptive radiation, divergent evolution and convergent evolution, and place organisms in the three domains of life.

**Why it matters for the exam**

This lesson belongs to category 1C, the transmission of heritable information and the evolution of populations. Evolution questions are usually passage-based: a scenario about a lizard, a bacterium or a flowering plant, with a table of allele frequencies or a tree, and a question asking you to apply a principle rather than recall a definition. The calculations are light. The reasoning is the point: what is the mechanism that changed this population, and what would it predict next? The math builds directly on [Lesson 10](chapter:14), where you learned Hardy-Weinberg equilibrium, and the molecular evidence leans on [Lesson 7](chapter:11) (mutation and replication) and [Lesson 3](chapter:6) (nucleic acid structure). The three domains connect forward to [Lesson 14](chapter:19) on prokaryotes.

Praxis Tip: Before you answer any evolution question, name the force. Selection, drift, gene flow, mutation and non-random mating are the only ways allele frequencies change. Most wrong answers come from choosing a force that does not fit the scenario.

**Concept Review**

**Evolution and the conditions for natural selection.** Evolution, at the population level, is a change in allele frequencies from one generation to the next. Natural selection is one cause of it, and it requires four conditions: (1) individuals vary in a trait, (2) the variation is at least partly heritable, (3) more offspring are produced than can survive, and (4) the variants differ in how many offspring they leave. Whenever all four hold, the heritable traits associated with higher reproductive output become more common. Selection acts on phenotypes, but only the heritable part of that variation responds. A tan acquired by sunbathing, or a muscle built by training, is not passed on, and selection on it changes nothing in the next generation.

**Fitness.** In evolutionary biology, **fitness** is reproductive success: the number of fertile offspring that survive to reproduce, usually expressed relative to others. It is not strength, speed or health in itself; those matter only if they raise reproductive output. **Relative fitness (w)** scales fitness so the most successful genotype is 1.0. The **selection coefficient (s)** is the reduction in fitness: if a genotype has w = 0.8, then s = 0.2. **Inclusive fitness** adds the effect of helping relatives, whose genes overlap with your own, and explains much altruistic behavior (kin selection). **Sexual selection** is selection for traits that improve mating success, even at some cost to survival, such as elaborate plumage; it arises through competition among members of one sex (often males) and choice by the other.

**Types of selection.** Selection is described by what it does to a distribution of phenotypes.

| Type | Favors | Effect on variation |
|---|---|---|
| Directional | One extreme | Mean shifts; variation may fall |
| Stabilizing | The average | Variation decreases |
| Disruptive | Both extremes | Variation increases; may split the population |
| Balancing | Multiple alleles kept | Variation maintained |

Examples. **Directional:** bacteria exposed to an antibiotic, where resistant cells leave more descendants and the population shifts toward resistance. **Stabilizing:** human birth weight, where very small and very large babies have lower survival than medium ones. **Disruptive:** a bird species in which birds with very small or very large beaks feed efficiently on the two seed types available, but medium beaks cope poorly with either. **Balancing selection** keeps two or more alleles in the population. Two classic routes are **heterozygote advantage** (the heterozygote has the highest fitness, as in the sickle cell allele, where carriers are generally better protected against severe malaria than non-carriers, while homozygotes for the sickle allele suffer sickle cell disease) [VERIFY] and **negative frequency-dependent selection** (a phenotype does better when rare, so it cannot take over).

Praxis Tip: Draw the bell curve before and after. If the peak moved, it is directional. If the peak got taller and narrower, stabilizing. If it flattened or grew two humps, disruptive. This takes five seconds and removes the guesswork.

**Selection and Hardy-Weinberg.** Recall that Hardy-Weinberg equilibrium (p² + 2pq + q² = 1, with p + q = 1) describes a population in which allele frequencies do not change. It requires: no selection, no mutation, no migration (gene flow), a very large population (no drift) and random mating. **Violating any one of these is a way evolution can occur.** Selection can be modeled by weighting each genotype frequency by its relative fitness. The mean fitness is wbar = p²·w(AA) + 2pq·w(Aa) + q²·w(aa), and the new frequency of a is q′ = (pq·w(Aa) + q²·w(aa)) / wbar. Selection against a recessive allele is slow once the allele is rare, because most copies are hidden in heterozygotes, where selection cannot see them.

**Genetic drift.** Drift is random change in allele frequencies caused by sampling error in finite populations. It is strongest in small populations and is not directed toward better adaptation. Over time drift tends to **reduce genetic variation within a population** and to **fix** or **lose** alleles. For a new neutral allele, the probability that it eventually becomes fixed equals its starting frequency. Two well-known special cases:

- **Bottleneck effect:** a sudden, severe reduction in population size (a disease, a natural disaster, hunting). The survivors' allele frequencies may differ from the original population by chance, and variation is lost even after the population recovers.
- **Founder effect:** a few individuals colonize a new area, and the new population carries only a sample of the source population's alleles.

In a diploid population of effective size N, heterozygosity is lost at a rate of about 1/(2N) per generation: H(t) = H(0)·(1 − 1/(2N))^t. A rare allele that happens to be common among the founders can reach high frequency in the new population (a pattern seen in some isolated human communities), without any selective advantage.

**Gene flow.** Gene flow (migration) is the movement of alleles between populations when individuals or gametes (pollen, for instance) move and breed. It tends to make populations **more similar to each other** and, within a recipient population, **adds variation**. For a population receiving a fraction m of its gene pool from migrants each generation, p′ = (1 − m)·p + m·p(migrants). Gene flow works against divergence and speciation; reducing it is a first step toward both.

**Mutation.** Mutation is the ultimate source of new alleles ([Lesson 7](chapter:11)). Per-gene rates are low, so mutation alone changes allele frequencies slowly, but without it selection would have no new variants to act on. Most mutations that affect function are neutral or deleterious; a few are beneficial. Gene duplication, recombination in meiosis and horizontal gene transfer (in prokaryotes) rearrange or add genetic material. Mutations in somatic cells are not passed to offspring; only changes in the germ line count for evolution. Mutations occur regardless of whether they would be useful; the environment does not direct them, it only sorts them.

**Non-random mating.** Inbreeding and assortative mating change genotype frequencies (more homozygotes), but by themselves they do not change allele frequencies.

Praxis Tip: When a question says allele frequencies changed, think of the five forces. When it says genotype frequencies changed but allele frequencies did not, think non-random mating.

**Species and speciation.** The **biological species concept** defines a species as a group of populations that can interbreed in nature and produce viable, fertile offspring, and are reproductively isolated from other such groups. It does not work well for asexual organisms, fossils or groups that hybridize, so other concepts (morphological, ecological, phylogenetic) are used too. A reproductive barrier that exists before fertilization is **prezygotic**; one that acts after the zygote forms is **postzygotic**.

| Barrier | Type | Example |
|---|---|---|
| Habitat isolation | Prezygotic | Two insects live on different host plants |
| Temporal isolation | Prezygotic | Species breed in different seasons |
| Behavioral isolation | Prezygotic | Mating songs differ |
| Mechanical isolation | Prezygotic | Genitalia or flower shapes do not fit |
| Gametic isolation | Prezygotic | Sperm cannot fertilize egg |
| Hybrid inviability or sterility | Postzygotic | Mule is sterile |

A hybrid that develops but is infertile, such as a mule, is the standard example of postzygotic isolation. Hybrid breakdown, in which the first-generation hybrids are fertile but later generations are weak or sterile, is another postzygotic case.

**Modes of speciation.**

- **Allopatric speciation:** a geographic barrier (a mountain range, a river, an island separation) splits a population. Gene flow stops, and the separated populations diverge through mutation, drift and different selection pressures until they cannot interbreed. This is the most widely accepted and best-documented mode.
- **Sympatric speciation:** new species arise within the same geographic area, without a physical barrier, for instance through disruptive selection together with assortative mating, or by polyploidy. **Polyploidy** is common in plants: an error in meiosis produces unreduced gametes, and a tetraploid plant can be reproductively isolated from its diploid parents in a single generation, because the triploid offspring of a cross between them are generally sterile.
- **Parapatric speciation:** populations on adjacent ranges diverge while still exchanging some genes across a narrow contact zone.

Where two diverging populations meet again, **reinforcement** may strengthen prezygotic barriers if hybrids have low fitness; or the populations may merge (fusion), or form a stable **hybrid zone**. Speciation can be gradual or follow a pattern of long stability interrupted by rapid change (punctuated equilibrium); the fossil record supports both modes in different lineages.

**Adaptive radiation, divergent and convergent evolution.** **Adaptive radiation** is the rapid diversification of a lineage into many forms that exploit different ecological niches, usually after colonizing a new environment with few competitors or after a mass extinction (Darwin's finches on islands and the diversification of mammals after the extinction of the non-avian dinosaurs are classic cases). **Divergent evolution** is the general pattern in which related populations become different over time. **Convergent evolution** is the independent evolution of similar traits in unrelated lineages under similar selection pressures: the streamlined bodies of sharks (fish) and dolphins (mammals), or the wings of birds and insects. Convergence produces **analogous** structures (similar function, different evolutionary origin). **Homologous** structures share an evolutionary origin even if their functions differ, such as the forelimb bones of humans, bats and whales. **Vestigial** structures are reduced remnants of structures that were functional in ancestors. **Coevolution** is reciprocal evolutionary change in interacting species, such as flowers and their pollinators or hosts and parasites.

Praxis Tip: Similarity because of shared ancestry is homology; similarity because of shared environment is analogy. When a question shows two similar structures in distant lineages, ask which explanation fits the tree.

**Phylogenetic trees.** A **phylogenetic tree** is a hypothesis about evolutionary relationships. A **cladogram** shows branching order only; in many other trees, branch lengths represent amounts of change or time.

How to read one:

- Tips (the ends of the branches) are the groups being compared; **nodes** (branch points) are inferred common ancestors; the root is the oldest ancestor.
- Relatedness is judged by **how recently two lineages share a common ancestor**, not by how close their tips sit on the page. Trees can be rotated at any node without changing the relationships.
- **Sister groups** are two lineages that share an immediate common ancestor not shared by any other group in the tree.
- A **monophyletic group (clade)** includes an ancestor and **all** of its descendants. A **paraphyletic group** includes an ancestor but not all descendants (traditional "reptiles", if birds are left out). A **polyphyletic group** includes members from different lineages but not their most recent common ancestor (for example, "flying animals").
- **Shared derived characters** (synapomorphies) are traits that arose in a common ancestor and are inherited by its descendants; they define clades. Ancestral traits shared by older groups (like having a backbone, within vertebrates) do not distinguish subgroups.
- **Parsimony** prefers the tree that requires the fewest evolutionary changes. An **outgroup** is a lineage known to be outside the group of interest; it helps determine which character states are ancestral.

A tree can be written in text with parentheses. For example, ((A, B), (C, D)) means A and B are sister taxa, C and D are sister taxa, and the pairs share a more distant common ancestor.

**Molecular evidence and molecular clocks.** DNA and protein sequences are now the main source of phylogenetic data. Closely related species have more similar sequences. Because changes accumulate with time, the number of differences between two sequences can be used as a **molecular clock**: if neutral substitutions accumulate at a roughly constant rate r per site per year in each lineage, the divergence between two species is d = 2rt, where t is the time since they split (two lineages have each been changing). The clock must be calibrated with fossils or known geological events, and it is rougher than it sounds: rates vary between genes, lineages and generation times. Regions under less selective constraint, such as synonymous sites and noncoding sequences, generally give the cleanest clocks. Highly conserved genes, such as rRNA genes, are used to compare distantly related organisms.

**Evidence for evolution.** (1) **Fossil record:** transitional forms and the order of appearance of groups in rock layers. (2) **Comparative anatomy:** homologous structures and vestiges. (3) **Embryology:** similar early developmental stages across vertebrates. (4) **Biogeography:** the distribution of species, including island species related to those of the nearest mainland. (5) **Molecular biology:** a nearly universal genetic code, shared genes (the same conserved regulatory genes in flies and mammals), pseudogenes, and sequence similarity that matches the anatomical tree. (6) **Direct observation:** antibiotic resistance, pesticide resistance and changes in beak size in island birds during droughts. Hardy-Weinberg equilibrium serves as the null model against which such changes are detected. (The origin of life itself is a separate question from evolution, which explains change among living things.)

**The three domains.** Most modern classification divides cellular life into three **domains**, based largely on ribosomal RNA sequences: **Bacteria**, **Archaea** and **Eukarya**.

| Feature | Bacteria | Archaea | Eukarya |
|---|---|---|---|
| Nucleus | No | No | Yes |
| Membrane-bound organelles | No | No | Yes |
| Cell wall | Peptidoglycan | No peptidoglycan | Varies (cellulose, chitin, none) |
| Membrane lipid linkage | Ester | Ether (generally) [VERIFY] | Ester |

Bacteria and archaea are both prokaryotes, but archaea are, in several ways (the machinery for transcription and some features of translation), more similar to eukaryotes than to bacteria, and phylogenies generally place eukaryotes closer to archaea. Many archaea live in extreme environments (high salt, high temperature, high acidity) although they are also common in ordinary soil and oceans. The eukaryotic organelles **mitochondria** and **chloroplasts** arose through **endosymbiosis**, as described in the endosymbiotic theory: an ancestral cell engulfed a bacterium that became permanently resident. Evidence includes their double membranes, their own circular DNA, bacterial-like (70S) ribosomes, division by a process like binary fission, and sequence similarity to specific bacterial groups (mitochondria to alpha-proteobacteria, chloroplasts to cyanobacteria). Viruses are generally not placed in the tree of life, because they are acellular and cannot carry out metabolism on their own.

**Worked Example 1: Selection against a recessive genotype (skill: Hardy-Weinberg with fitness)**

In a large population, the frequency of allele a is q = 0.30. Genotypes AA and Aa have relative fitness 1.0, while aa has relative fitness 0.8. Assuming random mating before selection, what is q in the next generation?

Genotype frequencies before selection: p = 0.70, so AA = 0.49, Aa = 2(0.7)(0.3) = 0.42, aa = 0.09. Mean fitness: wbar = 0.49(1) + 0.42(1) + 0.09(0.8) = 0.49 + 0.42 + 0.072 = 0.982. After selection, the frequency of a is (heterozygote half + aa) divided by wbar: q′ = (0.21 + 0.072) / 0.982 = 0.282 / 0.982 = about 0.287. The allele frequency dropped from 0.300 to 0.287 in one generation: selection against a recessive is real but slow, because most copies of a are in heterozygotes, which are not penalized.

**Worked Example 2: Drift in a small population (skill: heterozygosity decline)**

A newly isolated population has an effective size of N = 50 diploid breeding individuals. Starting heterozygosity is 0.50. What heterozygosity is expected after 20 generations, if drift is the only force acting?

H(t) = H(0)·(1 − 1/(2N))^t = 0.50 × (1 − 1/100)^20 = 0.50 × (0.99)^20 = 0.50 × 0.818 = about 0.41. Roughly 18 percent of the heterozygosity has been lost. In a population ten times larger, the same calculation (0.995^20 is about 0.90) would give a much smaller loss: the smaller the population, the faster drift erodes variation.

**Worked Example 3: Gene flow (skill: migration equation)**

On an island, the frequency of allele B is 0.20. Each generation, 10 percent of the breeding adults are migrants from the mainland, where the frequency of B is 0.80. What is the frequency of B on the island in the next generation, and what happens with continued migration?

p′ = (1 − m)p + m·p(mainland) = 0.9(0.20) + 0.1(0.80) = 0.18 + 0.08 = 0.26. With continued migration and no other force, the island frequency moves toward the mainland value of 0.80, so the populations become more alike. Gene flow opposes divergence.

**Worked Example 4: A molecular clock (skill: divergence time)**

The noncoding region of a gene differs at 6 percent of sites between two species. In related lineages with fossil calibration, neutral sites accumulate substitutions at about 1.5 × 10⁻⁹ per site per year per lineage. Estimate the time since the two species diverged.

Differences accumulate along both lineages, so d = 2rt. Then t = d / (2r) = 0.06 / (2 × 1.5 × 10⁻⁹) = 0.06 / (3.0 × 10⁻⁹) = 2.0 × 10⁷ years, about 20 million years. If someone forgot the factor of two and used d = rt, they would get 40 million years, double the correct answer. The numbers here are illustrative, not real measurements.

**Worked Example 5: Reading a tree (skill: sister groups and clades)**

A tree is written (lamprey, (shark, (frog, (lizard, mouse)))), with lamprey as the outgroup. (a) Which two taxa are sister taxa? (b) Is the group {frog, lizard} monophyletic? (c) Is shark more closely related to mouse or to lamprey?

(a) Lizard and mouse are sister taxa within the tree as drawn, since they share an immediate common ancestor not shared by frog. (b) No. The most recent common ancestor of frog and lizard also gave rise to mouse, so a group containing frog and lizard but not mouse leaves out a descendant: it is paraphyletic (and only a clade if mouse is included). (c) Shark is more closely related to mouse. The common ancestor of shark and mouse is more recent than the one shared with lamprey. A tip drawn next to another tip is not evidence of closeness; the nodes are.

**Worked Example 6: Naming the barrier and the mode (skill: speciation)**

Two populations of a fish are separated when a river changes course. Over many generations, they differ in mating coloration, and when later reunited, females of each population refuse to mate with males of the other. Name the mode of speciation and the barrier.

The physical separation makes this **allopatric** speciation. The refusal to mate is a **prezygotic, behavioral** barrier. If instead the two populations had mated and produced sterile offspring, the barrier would be **postzygotic** (hybrid sterility). Ask two questions in order: how did gene flow stop, and at what stage does the barrier act?

**More Praxis Tips**

Praxis Tip: Fitness is counted in offspring, not in victories. A tiny, unimpressive animal that leaves six surviving offspring is fitter than a magnificent one that leaves two.

Praxis Tip: Drift is the answer when the change is random, the population is small, and nothing about the new allele explains why it prospered. Selection is the answer when the change is consistent and tied to an environmental pressure.

Praxis Tip: In molecular clock questions, check the factor of two: divergence accumulates along both branches. Then check units (per site per year).

Praxis Tip: To find sister taxa on a tree, trace each tip back to its first node. Two tips whose first node is the same are sisters. Do not read across the page.

Praxis Tip: Natural selection acts on individuals, but populations evolve. An individual does not change its genes in order to cope; if a question says an organism "adapted by developing" a trait during its lifetime, be suspicious.

Praxis Tip: When a passage describes an experiment on evolution (for example, bacteria grown for hundreds of generations), identify the control population and what has been held constant. See [Strategy: Reading Biology Experiments](chapter:3).

**Common Mistakes**

- Treating evolution as progress toward a goal, or as something individuals do within their lifetimes.
- Saying fitness means strength or longevity rather than reproductive success.
- Confusing a bottleneck (a collapse in numbers) with a founder effect (a small colonizing group).
- Calling convergent traits homologous, or homologous traits analogous.
- Forgetting that mutation produces variation but does not aim at a need.
- Reading closeness from tip positions on a tree rather than from shared nodes.
- Omitting the factor of two in the molecular clock.
- Describing the three domains as plants, animals and fungi.

**Checkpoint Questions**

1. A population of beetles shows a bell-shaped distribution of body size. After several generations, the mean body size has not changed, but the variance has decreased, because beetles of intermediate size survive best. This is an example of
   A. directional selection
   B. disruptive selection
   C. stabilizing selection
   D. genetic drift

2. A hurricane kills most of the individuals on a small island, and the few survivors by chance carry a rare allele at much higher frequency than before. After the population recovers, that allele is common. The best explanation is
   A. a bottleneck followed by genetic drift
   B. gene flow from the mainland
   C. directional selection for the allele
   D. mutation of the allele to a higher rate

3. Two species of cichlid fish live in the same lake and look identical, but females of each species respond only to the courtship coloration of males of their own species. This is best classified as
   A. a postzygotic barrier of hybrid sterility
   B. a prezygotic behavioral barrier
   C. a geographic barrier
   D. a barrier of gametic isolation

4. On a phylogenetic tree written as (X, (Y, (Z, W))), which statement is correct?
   A. X and Y are sister taxa
   B. Y is more closely related to X than to W
   C. The group {X, Z} is monophyletic
   D. Z and W share a more recent common ancestor with each other than either does with Y

5. Two unrelated groups of desert plants have independently evolved thick, water-storing stems with spines instead of leaves. This pattern is best described as
   A. divergent evolution, producing homologous structures
   B. adaptive radiation from a recent common ancestor
   C. convergent evolution, producing analogous structures
   D. genetic drift

6. The noncoding regions of two species differ at 3 percent of sites. Neutral substitutions accumulate at 1.0 × 10⁻⁹ per site per year in each lineage. About how long ago did the species diverge?
   A. 1.5 × 10⁷ years
   B. 3.0 × 10⁷ years
   C. 6.0 × 10⁷ years
   D. 1.5 × 10⁶ years

7. Which observation provides the strongest evidence that mitochondria arose from a free-living bacterium?
   A. Mitochondria produce ATP
   B. Mitochondria are found in nearly all eukaryotic cells
   C. Mitochondria are smaller than the nucleus
   D. Mitochondria contain circular DNA and ribosomes resembling those of bacteria

---

**Stop here.** Answer every question on scratch paper before you read the reasons.

**Answers and reasons**

1. **C.** Selection favoring the average phenotype narrows the distribution while leaving the mean unchanged. (A would move the mean toward one extreme; B would increase the variance by favoring both extremes; D is random and not tied to survival of intermediate size.)
2. **A.** A sudden, random reduction in population size changes allele frequencies by sampling error, not by differences in fitness. (B requires migrants arriving, which the scenario does not describe; C assumes the allele was advantageous, though survival was by chance; D mutation rates do not change a frequency this quickly.)
3. **B.** Mate choice based on courtship signals acts before fertilization and is therefore a behavioral prezygotic barrier. (A no hybrids are produced in this scenario; C both species live in the same lake; D the barrier acts through female choice, not through failure of sperm and egg to fuse.)
4. **D.** Relatedness is read from the nodes: Z and W join first, then Y joins them, then X. (A Y's closest relatives on the tree are Z and W; B Y and W share a node that excludes X; C it excludes W, which descends from the same ancestor as Z.)
5. **C.** Similar solutions that evolved independently under similar pressures are convergent, and the structures are analogous. (A would require the traits to arise from a shared ancestral structure and diverge; B the plants are described as unrelated; D the shared pattern across lineages points to a common selection pressure, not random change.)
6. **A.** t = d / (2r) = 0.03 / (2 × 1.0 × 10⁻⁹) = 1.5 × 10⁷ years, since both lineages accumulate changes. (B omits the factor of two for two lineages; C multiplies by two instead of dividing; D has an error of a factor of ten in the exponent.)
7. **D.** Their own circular genome, bacterial-type ribosomes and double membranes fit an ancestral engulfed bacterium. (A chemical function alone does not show a bacterial origin; B being widespread does not indicate where they came from; C size alone says nothing about ancestry.)

Praxis Tip: After the checkpoint questions, label each wrong choice with the force or concept it actually describes (drift, gene flow, analogy, and so on). Log the pattern in your error log; the same confusions tend to repeat.

**Teach-Back and Spaced Review**

*Say this aloud in one breath:* "Populations evolve when allele frequencies change, through selection, drift, gene flow, mutation or non-random mating; selection needs heritable variation that affects reproductive success and can be directional, stabilizing, disruptive or balancing; speciation requires that gene flow stops and reproductive barriers arise, usually after geographic isolation; trees show ancestry by shared nodes, and clades contain an ancestor and all its descendants; and life divides into three domains, with mitochondria and chloroplasts descended from endosymbiotic bacteria."

*Review schedule:* revisit this lesson after 1 day (redo Worked Examples 1 and 4 without looking), after 3 days (checkpoint questions from a blank page), after 7 days (a mixed set including [Lesson 10](chapter:14) Hardy-Weinberg problems), and after 21 days (draw a tree and explain it aloud).

*Interleave:* alternate an evolution question with a genetics question and a molecular technique question ([Lesson 9](chapter:13)). Then take the [Genes and Evolution Set](chapter:16).

Praxis Tip: End each study session by listing the five forces that change allele frequencies and giving a one-line example of each. If you can do it in under a minute, you are ready.

---

**Author verification note (remove before publishing)**

- All examples and questions are original. Verified in Python: q′ = 0.287 after selection (wbar = 0.982); H after 20 generations = 0.41 (0.99^20 = 0.818); island p′ = 0.26; molecular clock t = 2.0 × 10⁷ years; the factor-of-two error gives 4.0 × 10⁷.
- Answer key positions: C, A, B, D, C, A, D.
- Verify with a biology reviewer: wording on heterozygote advantage and sickle cell and malaria; the claim that archaea cluster with eukaryotes and ether-linked membrane lipids being general rather than universal; the endosymbiosis evidence list; rRNA as a distant-relationship marker; the synonymous-site clock statement; the placement of viruses; the polyploidy sympatric speciation example.
- Category 1C topics covered: natural selection, fitness, types of selection, genetic drift, gene flow, mutation, speciation and isolating barriers, phylogenetic trees, molecular clocks, evidence, adaptive radiation, convergent and divergent evolution, and the three domains.
