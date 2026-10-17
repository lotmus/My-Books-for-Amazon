# Lesson 14: Prokaryotes and Viruses

**What you will be able to do**

- Describe bacterial structure and contrast it with eukaryotic cells, and use the Gram stain to infer cell-wall structure.
- Read a bacterial growth curve and calculate population size and doubling time.
- Classify bacteria by their relationship to oxygen and by how they obtain energy and carbon.
- Explain binary fission and the three routes of gene transfer (transformation, transduction and conjugation), and the role of plasmids.
- Describe viral structure, the lytic and lysogenic cycles, and the special features of retroviruses.
- Explain how antibiotics work, why they do not work on viruses, and how resistance arises and spreads.
- Give a brief account of prions.

**Why it matters for the exam**

This lesson is category 2B, prokaryotes and viruses. It rewards three kinds of reasoning: quantitative (exponential growth and doubling time), experimental (which gene-transfer mechanism explains a result, and what a control would show), and mechanistic (which step of a viral life cycle or which bacterial structure does a drug hit). The topic connects to many others: bacterial replication and operons ([Lesson 7](chapter:11) and [Lesson 8](chapter:12)), the evolution of resistance by natural selection ([Lesson 11](chapter:15)), membranes and cell structure ([Lesson 12](chapter:17)), tumor viruses ([Lesson 13](chapter:18)), and immunity and vaccination ([Lesson 21](chapter:28)). Cloning and selection techniques that use plasmids appear in [Lesson 9](chapter:13).

Praxis Tip: When a passage describes an experiment on bacteria or viruses, identify at the start what is being measured (cell count, colony count, turbidity, plaques, or gene transfer) and what the control is. Most questions then follow in a line.

**Concept Review**

**Prokaryotic cell structure.** Bacteria (and archaea) are prokaryotes: they have no nucleus and no membrane-bound organelles.

- **Chromosome:** typically a single, circular DNA molecule in the **nucleoid** region, without a nuclear envelope. Because there is no nucleus, transcription and translation are coupled: ribosomes begin translating an mRNA while it is still being made. Bacterial genes are often grouped in **operons** ([Lesson 8](chapter:12)).
- **Plasmids:** small, circular, extra-chromosomal DNA molecules that replicate independently and often carry genes that are useful but not essential, such as antibiotic resistance.
- **Ribosomes:** bacterial ribosomes are 70S (a 30S small subunit and a 50S large subunit), while eukaryotic cytosolic ribosomes are 80S (40S and 60S). This difference is the basis for several antibiotics.
- **Plasma membrane:** a phospholipid bilayer that, in bacteria, also carries the electron transport chain and ATP synthase, because there are no mitochondria. The proton gradient is built across the plasma membrane ([Lesson 5](chapter:8)).
- **Cell wall:** a rigid layer of **peptidoglycan** (sugar chains cross-linked by short peptides) outside the plasma membrane that resists osmotic lysis. Archaeal cell walls generally lack peptidoglycan. Eukaryotic animal cells have no cell wall.
- **Other structures:** a **capsule** (a sticky polysaccharide layer that helps avoid phagocytosis), **pili** or **fimbriae** (for attachment, and the **sex pilus** for conjugation), and **flagella** (a rotating protein filament driven by the proton gradient, unlike the whip-like motion of a eukaryotic flagellum). Some Gram-positive bacteria form **endospores**, dormant structures that survive heat, drying and many disinfectants.
- **Shapes:** cocci (spheres), bacilli (rods) and spirilla (spirals).

The endosymbiotic theory proposes that mitochondria and chloroplasts descend from engulfed bacteria, which fits their circular DNA and 70S-type ribosomes ([Lesson 12](chapter:17)).

**Gram stain.** The Gram stain divides bacteria into two groups on the basis of their cell envelopes. Cells are stained with crystal violet, treated with iodine, washed with alcohol, then counterstained with safranin.

| Feature | Gram-positive | Gram-negative |
|---|---|---|
| Peptidoglycan | Thick layer | Thin layer |
| Outer membrane | Absent | Present (contains LPS) |
| Color after stain | Purple | Pink or red |

In Gram-positive cells, the thick peptidoglycan holds the crystal violet-iodine complex despite the alcohol wash. In Gram-negative cells the thin wall and outer membrane lose the dye during the alcohol wash, and the cells take up the pink counterstain. The outer membrane of Gram-negative bacteria contains **lipopolysaccharide (LPS)**, also called endotoxin, which can trigger a strong immune response, and it acts as a barrier that makes many Gram-negative bacteria less susceptible to some antibiotics. Between the plasma membrane and outer membrane is the periplasmic space. The Gram stain is an indicator of wall structure, not a classification by evolutionary relatedness.

**Bacterial growth.** Bacteria reproduce by **binary fission**: the circular chromosome replicates from a single origin ([Lesson 7](chapter:11)), the two copies segregate, and the cell divides in two. Daughter cells are genetically identical except for mutation. In ideal conditions, the number of cells doubles every **generation time** (also called doubling time, td), which ranges from minutes in fast-growing species to many hours or days in slow ones.

Exponential growth is described by:

N = N0 × 2^(t/td)

where N0 is the starting number, t is the elapsed time, and t/td is the number of doublings (generations). Rearranging, the number of doublings is n = log2(N/N0), and td = t / n. If you use base-10 logarithms, n = (log10 N − log10 N0)/0.301. The continuous growth rate constant is k = ln 2 / td, about 0.693/td.

**The growth curve.** A batch culture in a closed flask passes through four phases when plotted as the logarithm of the cell count against time.

- **Lag phase:** cells adjust to the medium, synthesize enzymes, and do not yet divide at the maximum rate.
- **Exponential (log) phase:** growth is at its fastest and the plot of log N versus time is a straight line, whose slope gives the growth rate.
- **Stationary phase:** growth slows because nutrients run out, waste products accumulate, or space is limited, so that the rate of division is approximately equal to the rate of death and the count levels off. Endospores may form.
- **Death (decline) phase:** deaths exceed new cells.

Measurement matters. **Turbidity** (optical density) reports total cell mass, living and dead. A **plate count** reports only **viable** cells that can form colonies (colony-forming units, CFU), calculated as CFU/mL = colonies / (volume plated in mL × dilution factor), where the dilution factor is the fraction remaining (for example, 10⁻⁶). In a diluted sample the plate with 30 to 300 colonies is generally the most reliable.

Praxis Tip: If a growth plot is on a logarithmic axis, exponential growth is a straight line, and each fixed vertical distance on a log2 axis is one doubling. Do not interpret the straight line as "linear growth" in cell number.

**Metabolism of bacteria.** Bacteria are grouped by their relationship with oxygen.

| Type | Oxygen relationship | Energy strategy |
|---|---|---|
| Obligate aerobe | Requires O2 | Aerobic respiration |
| Obligate anaerobe | Harmed or killed by O2 | Fermentation or anaerobic respiration |
| Facultative anaerobe | Grows with or without O2 | Uses O2 if present, otherwise ferments |
| Aerotolerant anaerobe | Tolerates O2 but does not use it | Fermentation |

Anaerobic respiration uses an electron acceptor other than oxygen (such as nitrate), and fermentation regenerates NAD⁺ without an electron transport chain ([Lesson 4](chapter:7)). Bacteria are also classified by their sources of energy and carbon: **phototrophs** use light and **chemotrophs** use chemical energy; **autotrophs** build organic molecules from CO₂ and **heterotrophs** use organic carbon. Cyanobacteria are photoautotrophs. Most human pathogens are chemoheterotrophs.

**Genetic variation in bacteria.** Bacteria reproduce asexually, but they are far from genetically static. Variation arises by **mutation**, which, combined with huge population sizes and short generation times, is rapidly amplified by selection. Bacteria also acquire genes from other cells by **horizontal gene transfer**, as opposed to the vertical transmission from parent to daughter cells. DNA that arrives is useful only if it is incorporated: by recombination into the chromosome, or as a plasmid that can replicate on its own.

- **Transformation:** a **competent** cell takes up **naked DNA** from the environment (for example, from lysed cells) and may incorporate it by recombination. Griffith's experiment with a harmless and a virulent strain of *Streptococcus pneumoniae* showed that something from dead virulent cells could transform harmless cells, and later work identified the transforming substance as DNA. The process is sensitive to DNase, an enzyme that digests DNA, and does not require cell contact.
- **Transduction:** a **bacteriophage** carries bacterial DNA from one cell to another. In **generalized transduction**, an error in packaging places a random fragment of host DNA into a phage head during the lytic cycle. In **specialized transduction**, a prophage excises imprecisely from the chromosome and carries nearby bacterial genes into the next cell. Transduction is DNase-resistant because the DNA is protected inside the capsid, and it needs a phage.
- **Conjugation:** direct transfer of DNA between two cells through a **sex pilus** and a cell-to-cell connection. The **F plasmid** (fertility factor) carries the genes for the pilus and for transfer. A donor (F⁺) transfers a copy of the plasmid to a recipient (F⁻), which becomes F⁺. If the F plasmid has integrated into the chromosome (an **Hfr** cell), chromosomal genes can be transferred, but the recipient generally remains F⁻ because the entire plasmid is rarely transferred. Conjugation requires cell contact, and the transferred DNA is generally a single strand that is copied in the recipient.

Plasmids that carry resistance genes (R plasmids) can move between cells and even between species, and **transposons** (mobile DNA elements; [Lesson 7](chapter:11)) can hop between plasmid and chromosome. This makes horizontal transfer a central route by which resistance spreads.

Praxis Tip: Pick the gene-transfer mechanism by asking three questions in order: Is cell-to-cell contact needed (conjugation)? Does a virus carry the DNA (transduction)? Is DNase destructive to it (transformation)? An experiment with a fine filter or a U-tube answers the first, and DNase answers the third.

**Viruses.** Viruses are not cells. They have no cytoplasm, metabolism or ribosomes, and they replicate only by taking over a host cell: they are **obligate intracellular parasites**.

- **Genome:** DNA or RNA, single-stranded or double-stranded, in one or several segments.
- **Capsid:** a protein shell made of repeating subunits (capsomeres) that protects the genome.
- **Envelope:** some viruses are surrounded by a lipid membrane taken from the host cell as the virus buds, studded with viral glycoproteins. Enveloped viruses generally enter by fusing with the host membrane, are more sensitive to detergents and drying, and are released by budding. Naked (non-enveloped) viruses are often released by lysis.
- **Specificity:** attachment proteins recognize specific host receptors, which determines which species and tissues a virus can infect (**tropism**).
- **Bacteriophages** are viruses of bacteria. Many have an icosahedral head and a tail, and attach to the bacterial surface, then inject their DNA, leaving the empty capsid outside.

RNA viruses that have a **positive-sense (+) single-stranded RNA genome** can have that genome read directly as mRNA by host ribosomes. **Negative-sense (−)** RNA viruses carry an **RNA-dependent RNA polymerase** in the virion to make mRNA from their genome. Because RNA-dependent polymerases generally lack proofreading, RNA viruses mutate rapidly, which helps explain the frequent need for new influenza vaccines. Viruses with segmented genomes, such as influenza, can also swap segments when two strains infect the same cell.

**The lytic cycle.** A **virulent** phage always uses the lytic cycle:

1. **Attachment** to a specific receptor.
2. **Penetration** (entry of the genome).
3. **Biosynthesis:** the host's machinery is used to replicate the viral genome and make viral proteins, and the host DNA is usually degraded.
4. **Assembly** (maturation) of new virions.
5. **Release** by lysis, which kills the host.

**The lysogenic cycle.** A **temperate** phage can instead integrate its DNA into the bacterial chromosome as a **prophage**. It is then copied along with the host DNA at every division, and may stay silent for many generations because a viral repressor blocks the lytic genes. Stress such as DNA damage or ultraviolet light can lead to **induction**: the prophage excises and enters the lytic cycle. A prophage can also alter the host: some bacteria carry toxin genes of viral origin (for example, in diphtheria and cholera). [VERIFY]

**Animal viruses and retroviruses.** Animal viruses enter by receptor-mediated endocytosis or membrane fusion and uncoat. DNA viruses often replicate in the nucleus; most RNA viruses replicate in the cytoplasm. Some DNA viruses can integrate into host DNA, and certain tumor viruses contribute to cancer by inactivating host tumor suppressors such as p53 and Rb (human papillomavirus is an example) [VERIFY]; [Lesson 13](chapter:18).

**Retroviruses** (such as HIV) have an RNA genome and defy the simplest reading of the central dogma. The virion carries **reverse transcriptase**, an RNA-dependent DNA polymerase that copies the single-stranded RNA genome into a DNA copy (ultimately a double-stranded DNA); an **integrase** inserts that DNA into the host chromosome as a **provirus**, which is then transcribed by host RNA polymerase to produce new viral RNA (both genome and mRNA). Host ribosomes make viral proteins, which includes a **protease** that cuts large precursor proteins into functional pieces, and the virion buds from the cell. HIV infects cells that display the CD4 receptor, mainly helper T cells, so loss of those cells weakens adaptive immunity ([Lesson 21](chapter:28)). Reverse transcriptase has no proofreading, so retroviruses mutate quickly. Reverse transcriptase is also used in the laboratory to make cDNA from mRNA ([Lesson 9](chapter:13)).

Viruses with RNA genomes versus the flow of information:

| Virus type | Key enzyme | Template to product |
|---|---|---|
| (+) RNA virus | RNA-dependent RNA polymerase | RNA to RNA |
| (−) RNA virus | RNA-dependent RNA polymerase | RNA to RNA |
| Retrovirus | Reverse transcriptase | RNA to DNA |
| DNA virus | DNA polymerase (host or viral) | DNA to DNA |

**Prions (a brief note).** Prions are infectious agents made only of protein, with no nucleic acid. The normal prion protein (PrP^C) has a high α-helix content. A misfolded form (PrP^Sc) is rich in β-sheet and induces normal copies to misfold, spreading as a chain reaction. Prions cause neurodegenerative diseases such as Creutzfeldt-Jakob disease and bovine spongiform encephalopathy. They are unusually resistant to heat, UV light and nucleases, which would destroy a conventional infectious agent, and they have no vaccine. The point to remember: misfolding of protein ([Lesson 1](chapter:4)) can be transmitted.

**Antibiotics.** Antibiotics exploit differences between bacterial and human cells (**selective toxicity**). A **bactericidal** drug kills bacteria; a **bacteriostatic** drug stops their growth and relies on the immune system for clearance.

| Target | Example class | Effect |
|---|---|---|
| Cell wall synthesis | Penicillins, vancomycin | Wall weakens, cell lyses |
| 30S ribosome | Tetracyclines, aminoglycosides | Blocks or distorts translation |
| 50S ribosome | Macrolides, chloramphenicol | Blocks translation |
| DNA gyrase, folate, RNA polymerase | Quinolones, sulfonamides, rifampin | Blocks DNA, folate or RNA synthesis |

[VERIFY all drug mechanisms in the table; the exam will generally supply the mechanism in the passage.] Cell wall drugs act on **growing** cells, which are synthesizing new peptidoglycan; in a hypotonic environment the weakened wall cannot resist the osmotic pressure, and the cell lyses. Human cells have no peptidoglycan, which makes the target selective. Antibiotics are **useless against viruses**, which have no wall, no 70S ribosomes and no metabolism of their own. Antiviral drugs instead target viral enzymes or steps (for example, reverse transcriptase, viral proteases, and genome polymerases) [VERIFY], and vaccines work by priming the immune system.

**Antibiotic resistance.** Resistance arises through mutation or the acquisition of resistance genes, and common mechanisms include: an enzyme that destroys the drug (a **β-lactamase** cleaves the β-lactam ring of penicillins), a **modified target** (an altered penicillin-binding protein or ribosome), an **efflux pump** that exports the drug, or reduced permeability. The key logic is **selection**, not intention: within a large population, a few cells already carry resistance (by mutation or by a plasmid). The drug kills the susceptible majority, the resistant survivors multiply in the space that opens up, and the population becomes largely resistant. The antibiotic is the selective pressure, and it is not generally required to cause the resistance mutation. Misuse (unnecessary prescriptions, stopping a course early, using antibiotics for viral infections) increases selection, and horizontal transfer then moves resistance genes between species ([Lesson 11](chapter:15)).

Praxis Tip: Describe resistance as "selection of pre-existing resistant cells", never as "bacteria becoming resistant because they needed to". The first is the answer a test writer wants. The second is Lamarck in a lab coat.

**Worked Example 1: Reading the Gram stain (skill: inferring structure)**

A bacterial culture is processed through the Gram stain. Under the microscope, the cells are pink. Is the cell wall thick or thin, is there an outer membrane, and what does the result suggest about susceptibility to a drug that must cross an outer membrane?

Pink cells are Gram-negative. They have a thin peptidoglycan layer, lose the crystal violet during the alcohol wash, and have an outer membrane containing LPS. A drug that must cross the outer membrane may be less effective, because the outer membrane is a permeability barrier. A larger, more polar drug would be especially excluded. Gram-positive bacteria, with a thick wall and no outer membrane, hold the purple dye.

**Worked Example 2: Growth calculations (skill: exponential growth)**

(a) A culture starts with 5.0 × 10⁴ cells/mL and has a doubling time of 20 minutes. What is the density after 2 hours of exponential growth? (b) The log10 of the cell density rises from 5.0 to 7.4 over 4 hours of exponential growth. What is the doubling time?

(a) 2 hours = 120 minutes, so n = 120/20 = 6 doublings. N = 5.0 × 10⁴ × 2⁶ = 5.0 × 10⁴ × 64 = **3.2 × 10⁶ cells/mL**. (b) The increase in log10 N is 2.4, so n = 2.4/0.301 = 7.97, or about 8 doublings. td = 240 min / 8 = **30 minutes**. Check: 10^2.4 is about 250, and 2⁸ = 256.

**Worked Example 3: Plate counts (skill: viable counts and dilutions)**

A sample is diluted 10⁻⁶ and 0.10 mL is spread on an agar plate. After incubation, 85 colonies appear. What is the concentration of viable cells in the original sample? Would an optical density reading give the same number?

CFU/mL = 85 / (0.10 mL × 10⁻⁶) = 85 / 10⁻⁷ = **8.5 × 10⁸ CFU/mL**. An optical density reading measures turbidity from all cells, living and dead, so it can overestimate the viable count, especially in the death phase. A plate count includes only cells that can form colonies.

**Worked Example 4: Which gene-transfer mechanism? (skill: experimental logic)**

A researcher mixes strain 1 (requires leucine, resistant to drug X) with strain 2 (makes its own leucine, sensitive to drug X). Cells that grow on medium lacking leucine and containing drug X (that is, cells that now have both traits) are recovered at a low frequency. The result is the same when DNase is added. When the two strains are grown in two arms of a U-tube separated by a filter whose pores are large enough to pass phages and free DNA but not bacteria, no such cells are recovered. Which mechanism is supported, and which are excluded?

The transfer needs direct contact: when the two strains are separated by the filter, transfer fails. Free DNA could cross the filter, so **transformation** is excluded (and DNase had no effect, which also argues against it). Phages could cross the filter, so **transduction** is excluded. **Conjugation** is consistent with all observations. (Note: this logic does not rule out other results with other conditions, and the recovered cells should also be shown to carry the transferred gene.)

**Worked Example 5: Virus life cycles and information flow (skill: sequencing steps)**

(a) A culture infected with a phage shows no lysis for many generations, but lyses within an hour after ultraviolet exposure. What cycle explains this? (b) List, in order, the nucleic acids that appear during the replication of a retrovirus after it enters the cell.

(a) The phage is temperate and was present as a **prophage** (lysogenic cycle). UV-induced DNA damage triggered induction, switching the phage to the lytic cycle. (b) Viral **single-stranded RNA** (genome) → **DNA** copy made by reverse transcriptase (first a DNA-RNA hybrid, then double-stranded DNA) → **integrated provirus** in the host chromosome → **viral RNA** transcribed by host RNA polymerase (used as new genomes and as mRNA). An inhibitor of reverse transcriptase would block the second step and prevent integration.

**Worked Example 6: Frequency of resistance (skill: selection)**

A population of 4.0 × 10⁹ bacteria is plated on agar containing an antibiotic, and 12 colonies grow. What is the frequency of resistant cells? What does the result suggest about the origin of resistance?

Frequency = 12 / (4.0 × 10⁹) = **3.0 × 10⁻⁹**. A very low frequency is consistent with rare spontaneous mutations that occurred in the population. The antibiotic selected the few resistant cells, rather than inducing them.

**More Praxis Tips**

Praxis Tip: Learn bacterial and eukaryotic structures as a contrast table of eight lines (chromosome, ribosome, membrane organelles, cell wall, division, transcription site, respiration site, size). Questions on 2B are very often "which structure explains why drug X is selective?"

Praxis Tip: Gram-positive is thick wall and purple. Gram-negative is thin wall with an extra outer membrane and pink. If you cannot recall which is which, remember that "negative" has more, because it has the outer membrane (and the outer membrane is the reason it stains negative).

Praxis Tip: In a doubling-time problem, convert units before anything else. Time in minutes and doubling time in hours has ruined more answers than any amount of arithmetic.

Praxis Tip: Plasmids are in the exam for a reason: they are the vehicle of both antibiotic resistance and of laboratory cloning. When you see "plasmid", ask what gene it carries and how it is transferred.

Praxis Tip: For viruses, never say "alive" or "dead" in your reasoning: say "infectious" or "inactivated". Viruses are not cells, so questions that treat them as cells (cell wall, binary fission, ribosomes) are usually distractors.

Praxis Tip: To keep the three transfer mechanisms apart, try the one-line stories. Transformation: DNA is picked up from the floor. Transduction: a virus delivers the DNA by mistake. Conjugation: two cells hold hands.

Praxis Tip: A retrovirus is the only common exception to the usual order of the central dogma. Questions about it nearly always hinge on reverse transcriptase, integration, or the lack of proofreading.

Praxis Tip: If an answer says an antibiotic "causes" resistance, check whether it means "selects for". The first is usually wrong, the second usually right.

**Common Mistakes**

- Reversing the Gram colors, or forgetting that Gram-negative bacteria have an outer membrane and a thin wall.
- Treating exponential growth as linear, or forgetting that a doubling time of 30 minutes means 2^(t/30) with t in minutes.
- Using optical density as if it counted only living cells.
- Confusing transformation (naked DNA), transduction (phage) and conjugation (contact and a pilus).
- Saying that viruses divide by binary fission, or that antibiotics treat viral infections.
- Forgetting that the lysogenic cycle does not kill the host immediately, and that the prophage is replicated with the host DNA.
- Describing antibiotic resistance as bacteria "adapting" in an individual, instead of selection acting on a population.
- Claiming that prions contain DNA or RNA.

**Checkpoint Questions**

1. A bacterial smear is stained with crystal violet, treated with iodine, washed with alcohol and counterstained with safranin. The cells appear purple. This most likely means the cells
   A. have a thin peptidoglycan wall with an outer membrane containing LPS
   B. lack a cell wall entirely
   C. are eukaryotic cells with a nuclear envelope
   D. have a thick peptidoglycan wall and no outer membrane

2. A culture contains 2.0 × 10⁴ cells/mL in early exponential growth and has a doubling time of 40 minutes. Assuming the exponential phase continues, what is the density after 4 hours?
   A. 1.2 × 10⁵ cells/mL
   B. 3.2 × 10⁵ cells/mL
   C. 1.28 × 10⁶ cells/mL
   D. 2.56 × 10⁶ cells/mL

3. Two auxotrophic strains are grown in the two arms of a U-tube separated by a filter that blocks bacteria but passes free DNA and bacteriophages. No recombinant cells appear, but they do appear when the strains are mixed directly. The best explanation is
   A. conjugation, which requires direct cell-to-cell contact
   B. transformation, because naked DNA must pass between the strains
   C. transduction, because phages carry DNA between cells
   D. binary fission, because it exchanges DNA between strains

4. Bacteria infected with a phage grow normally for many generations. After brief ultraviolet irradiation, the culture lyses and releases phage. Which statement best explains the observation?
   A. The phage was in the lytic cycle all along, and UV started the cycle
   B. The phage was integrated as a prophage, and UV damage induced it to enter the lytic cycle
   C. The UV exposure caused bacterial conjugation, which lysed the cells
   D. The bacteria acquired antibiotic resistance genes from the phage

5. An inhibitor of reverse transcriptase is added to cells infected with a retrovirus. Which step is most directly blocked?
   A. translation of viral proteins on host ribosomes
   B. assembly of the capsid proteins
   C. synthesis of a DNA copy of the viral RNA genome
   D. transcription of host genes by host RNA polymerase

6. A hospital isolates a bacterial strain that is resistant to an antibiotic. Which statement is most consistent with the principles of selection?
   A. Exposure to the drug caused each cell to develop resistance because it needed it
   B. Resistant cells were present at low frequency, and exposure to the drug killed susceptible cells and allowed the resistant ones to multiply
   C. Resistance arises only if the antibiotic passes into the nucleus of the bacteria
   D. Antibiotics are effective against viruses, so resistance must be viral

7. Penicillin-like drugs block cross-linking of peptidoglycan. When such a drug is added to a growing culture of bacteria in a dilute medium, the most likely result is
   A. lysis of dividing cells, which cannot build a wall that resists osmotic pressure
   B. shrinkage of the cells because the drug draws water out
   C. equal killing of growing and of nongrowing cells
   D. immediate blockage of DNA replication

---

**Stop here.** Answer every question on scratch paper before you read the reasons.

**Answers and reasons**

1. **D.** Purple cells retained the crystal violet-iodine complex, as expected of a thick peptidoglycan layer. (A describes Gram-negative cells, which lose the crystal violet at the alcohol wash and appear pink; B would not retain the stain through the alcohol wash; C is wrong because the stain describes bacterial wall structure and gives no information about a nucleus.)
2. **C.** Four hours is 240 minutes, which is 6 doublings, so N = 2.0 × 10⁴ × 2⁶ = 1.28 × 10⁶. (A multiplies by the number of 40-minute periods, which treats growth as linear; B uses 4 doublings by treating the 4 hours as 4 generations; D counts 7 doublings, one more than 240/40 = 6.)
3. **A.** Transfer that fails when cells are kept apart, even though DNA and phages can cross, points to contact-dependent conjugation. (B predicts recombinants in the U-tube, since free DNA crosses the filter; C predicts recombinants in the U-tube, since phages cross the filter; D produces identical daughter cells and does not transfer DNA between strains.)
4. **B.** Silent propagation with the host DNA, followed by stress-induced lysis, is the signature of lysogeny and induction. (A is contradicted by many generations of normal growth, since lytic phage would have lysed the cells; C does not account for the release of phage, and conjugation does not lyse cells; D is irrelevant to lysis and phage release.)
5. **C.** Reverse transcriptase copies the RNA genome into DNA, and the DNA copy is needed for integration. (A does not involve reverse transcriptase, since it uses mRNA and ribosomes; B is a later step, which does not need reverse transcriptase; D is performed by a host enzyme, not by reverse transcriptase.)
6. **B.** Pre-existing variation plus selective pressure explains resistance, and the drug acts as the filter, not the cause. (A describes a directed response, whereas resistance mutations arise independently of the drug; C is wrong because bacteria have no nucleus; D is wrong because antibiotics do not act on viruses and viral infection is not the source of bacterial resistance.)
7. **A.** A weakened wall cannot withstand the water entering a cell in dilute medium, so growing cells burst. (B is the opposite of what happens, since a weakened wall in a dilute medium leads to swelling; C is wrong because cell wall drugs mostly affect cells that are synthesizing new wall; D is not the primary mechanism, because the drug acts on the cell wall.)

Praxis Tip: After the checkpoint questions, name the slip behind every wrong choice (colors reversed, linear instead of exponential, wrong gene-transfer mechanism, or induction mistaken for mutation). Log it in your error log (see Book 1, Strategy: The Question Method).

**Teach-Back and Spaced Review**

*Say this aloud in one breath:* "Bacteria are prokaryotes with a circular chromosome, 70S ribosomes and a peptidoglycan wall, divided by the Gram stain into thick-walled purple Gram-positive cells and thin-walled pink Gram-negative cells with an outer membrane; they grow exponentially by binary fission as N = N0 times 2 to the t over td, and they swap genes by transformation, transduction and conjugation, with plasmids often carrying resistance; viruses are noncellular parasites that use the lytic or lysogenic cycle, retroviruses use reverse transcriptase and integrase, antibiotics target bacterial structures and are selected for by their use, and prions are infectious proteins."

*Review schedule:* revisit this lesson after 1 day (redo Worked Examples 2 and 4 without looking), after 3 days (checkpoint questions from a blank page), after 7 days (a mixed set that includes [Lesson 8](chapter:12) operons and [Lesson 13](chapter:18) cell division), and after 21 days (explain the lesson aloud).

*Interleave:* alternate a growth-calculation problem with a gene-transfer problem and a viral life cycle problem. Then take the [Cell Biology and Microbiology Set](chapter:20).

Praxis Tip: End each study session by drawing, from memory, the growth curve with its four phases, the lytic and lysogenic cycles side by side, and a three-column table of the gene-transfer mechanisms.

---

**Author verification note (remove before publishing)**

- All examples and questions are original. Verified by calculation: 5.0 × 10⁴ × 2⁶ = 3.2 × 10⁶; (7.4 − 5.0)/0.301 = 7.97, about 8 doublings; 85/(0.10 × 10⁻⁶) = 8.5 × 10⁸; 12/(4.0 × 10⁹) = 3.0 × 10⁻⁹; checkpoint 2: 2.0 × 10⁴ × 2⁶ = 1.28 × 10⁶.
- Answer key positions: D, C, A, B, C, B, A.
- Verify with a microbiology reviewer: the antibiotic mechanism table and example classes; the statement about Gram-positive endospore formers; the F plasmid and Hfr details; the toxin-gene examples (diphtheria and cholera); the human papillomavirus statement; lack of proofreading in RNA-dependent polymerases (stated as a general rule); the prion description; and the claim about Archaea cell walls.
- Category 2B topics covered: bacterial structure and function, Gram stain, growth, metabolism types, binary fission, gene transfer and plasmids, viral structure and life cycles, retroviruses, antibiotics and resistance, and a note on prions.
