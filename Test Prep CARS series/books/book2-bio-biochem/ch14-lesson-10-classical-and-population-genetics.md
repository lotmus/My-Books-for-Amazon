# Lesson 10: Classical and Population Genetics

**What you will be able to do**

- Predict offspring genotypes and phenotypes for monohybrid and dihybrid crosses, testcrosses and crosses with sex-linked genes.
- Recognize incomplete dominance, codominance, multiple alleles, lethal alleles, epistasis and other departures from simple Mendelian ratios.
- Calculate recombination frequencies, build a simple genetic map, and recognize linked genes from offspring counts.
- Read pedigrees and decide among autosomal recessive, autosomal dominant, X-linked and mitochondrial inheritance.
- Use the product, sum, conditional and binomial rules, and the Hardy-Weinberg equations, with correct arithmetic.
- Explain how nondisjunction produces aneuploidy and what common chromosomal abnormalities look like.

**Why it matters for the exam**

This lesson serves category 1C (transmission of heritable information and evolution) and uses a skill that does not depend on memory at all: careful, patient counting. Genetics questions reward a few clean habits (write genotypes, set up the cross, use fractions) and punish guessing. Passages often give offspring counts or a pedigree and ask you to deduce the mode of inheritance, a map distance or a probability. The lesson builds on meiosis ([Lesson 13](chapter:18) covers it in detail) and DNA mutations ([Lesson 7](chapter:11)), and it leads directly into [Lesson 11](chapter:15), where Hardy-Weinberg becomes the baseline for evolution.

Praxis Tip: In every genetics problem, write down the genotypes before you do anything else. Candidates who work from phenotype words ("the tall ones") lose the information the cross depends on.

**Concept Review**

**1. Mendel's rules.** A **gene** occupies a **locus** on a chromosome and comes in versions called **alleles**. An individual with two identical alleles is **homozygous**; with two different alleles, **heterozygous**. The **genotype** is the allele combination, and the **phenotype** is the observable trait. Mendel's findings, in modern terms:

- **Segregation:** the two alleles of a gene separate into different gametes in meiosis, so each gamete carries one allele (anaphase I of meiosis separates homologs).
- **Independent assortment:** alleles of genes on different chromosomes (or far apart on the same chromosome) are distributed into gametes independently of each other.
- **Dominance:** in a heterozygote, the **dominant** allele's phenotype is observed and the **recessive** allele's phenotype is hidden, in simple cases.

Standard results to know:

- Monohybrid cross Aa × Aa: genotypes 1 AA : 2 Aa : 1 aa; phenotypes 3 dominant : 1 recessive.
- Dihybrid cross AaBb × AaBb (independent genes): phenotypes 9 A_B_ : 3 A_bb : 3 aaB_ : 1 aabb (the underscore stands for either allele).
- **Testcross:** cross an individual of unknown genotype with a homozygous recessive. If every offspring shows the dominant phenotype, the unknown is probably AA; a 1 : 1 ratio shows Aa.

**2. The probability toolkit.** Most genetics is probability.

- **Product rule:** the probability that two independent events both occur is the product: P(A and B) = P(A) × P(B). Use it for "and" across genes, children or gametes.
- **Sum rule:** for mutually exclusive outcomes, P(A or B) = P(A) + P(B).
- **Conditional probability:** if you know something, shrink the possibilities and recompute. A phenotypically unaffected child of two Aa parents is AA with probability 1/3 and Aa with 2/3, because the aa possibility (1/4) is removed, leaving 3/4 of outcomes, of which 1/4 are AA and 2/4 Aa.
- **Independence:** each child is an independent event; a couple with three sons has the same chance of a son next time (1/2).
- **Binomial:** the probability of exactly k of a certain kind among n trials, each with probability p, is [n! ÷ (k!(n − k)!)] × pᵏ × (1 − p)ⁿ⁻ᵏ. For two carrier parents with four children, the chance that exactly one is affected by an autosomal recessive disorder is 4 × (1/4) × (3/4)³ = 27/64.

Praxis Tip: Keep probabilities as fractions until the end. 9/64 is easier to check than 0.140625, and the denominators tell you how many independent 1/2 or 1/4 events were multiplied.

**3. Patterns of dominance and gene action.**

- **Incomplete dominance:** the heterozygote is intermediate (red × white gives pink flowers). F₂ phenotype ratio 1 : 2 : 1, equal to the genotype ratio.
- **Codominance:** both alleles are fully expressed in the heterozygote. ABO blood types: alleles Iᴬ and Iᴮ are codominant and both are dominant over *i*. Genotypes ↔ phenotypes: Iᴬ_ or Iᴬi = type A; Iᴮ_ or Iᴮi = B; IᴬIᴮ = AB; *ii* = O. A type A (Iᴬ*i*) × type B (Iᴮ*i*) cross can give A, B, AB or O, each with probability 1/4.
- **Multiple alleles:** more than two alleles exist in the population, although each individual carries only two.
- **Lethal alleles:** a homozygous lethal combination removes one genotype, changing a 3 : 1 ratio to 2 : 1 among survivors for a recessive lethal.
- **Penetrance and expressivity:** *penetrance* is the fraction of people with the genotype who show any phenotype; *expressivity* is how strongly it shows. Incomplete penetrance makes a dominant disorder appear to skip a generation.
- **Pleiotropy:** one gene affects several traits. **Polygenic traits:** many genes (plus environment) shape one trait, giving a continuous bell-shaped range, such as height.
- **Environment** can alter expression of a genotype, so identical genotypes can have different phenotypes.

**4. Sex-linkage and other non-autosomal patterns.** Humans have 22 pairs of autosomes and one pair of sex chromosomes (XX in females, XY in males). Genes on the X chromosome without a counterpart on the Y are **X-linked**, and males are **hemizygous** for them (one copy).

- **X-linked recessive** (for example, red-green color blindness, hemophilia A): affected individuals are mostly male; an affected male passes the allele to all his daughters (who are carriers) and none of his sons; a carrier mother passes it to half her sons (affected) and half her daughters (carriers). Affected father × unaffected non-carrier mother: no affected children, all daughters carriers. **No male-to-male transmission.**
- **X-linked dominant:** an affected father has all daughters affected and no sons affected; affected females pass the trait to half of their children of either sex.
- **Y-linked:** father to all sons only.
- **X inactivation:** in each cell of a female, one X is generally silenced and condenses into a **Barr body**, at random early in development. Heterozygous females are therefore mosaics (calico cats are the classic example), so a female carrier can show mild signs.
- **Mitochondrial inheritance:** mitochondrial DNA is inherited from the egg (maternal inheritance). All offspring of an affected mother may be affected (to varying degrees, because cells hold a mix of normal and mutant mitochondria), and an affected father generally transmits to none.
- **Genomic imprinting:** a few genes are expressed according to which parent they came from, so that a trait depends on the parent of origin even though the sequence is the same ([Lesson 8](chapter:12), epigenetics).

**5. Linkage and recombination.** Genes close together on the same chromosome tend to be inherited together. In prophase I, **crossing over** between non-sister chromatids of homologs can swap segments and make **recombinant** gametes with new allele combinations. For a **testcross** of a double heterozygote (AaBb × aabb):

- The **parental** types are the most common classes (they match the original chromosomes).
- The **recombinant** types are the less common classes.
- **Recombination frequency (RF)** = recombinants ÷ total offspring × 100 percent. One percent recombination is defined as one **map unit**, or **centimorgan (cM)**.

Facts to know:

- RF is at most **50 percent**. At 50 percent the genes behave as if unlinked, whether they are on different chromosomes or far apart on the same one.
- A smaller RF means genes are closer together.
- **Phase matters.** In the *cis* (coupling) arrangement, AB/ab, the parental gametes are AB and ab. In the *trans* (repulsion) arrangement, Ab/aB, the parental gametes are Ab and aB. Always identify the parentals from the **majority** classes.
- **Three-point mapping:** the two genes that are farthest apart have the largest RF, and the gene between them has the other two distances adding up to the large one (approximately). For example, if A–B = 14, A–C = 6 and B–C = 20, then A is in the middle (14 + 6 = 20).
- Map distances are approximate for long distances, because **double crossovers** restore the parental arrangement and are not counted, so large distances are underestimated.

**6. Pedigrees.** A pedigree is a family tree: squares represent males, circles females, shaded symbols affected individuals, a horizontal line a mating, and vertical lines the offspring, with Roman numerals for generations. Reasoning rules (use each with care; look for the clue that decides):

- **Autosomal recessive:** two unaffected parents can have an affected child (of either sex); it often skips generations; affected individuals' parents are carriers; consanguinity makes it more likely.
- **Autosomal dominant:** every affected person has an affected parent (barring a new mutation or incomplete penetrance); it appears in every generation; affected × unaffected gives about half affected.
- **X-linked recessive:** many more affected males than females; passes through carrier females; no father-to-son transmission.
- **X-linked dominant:** affected fathers have affected daughters but unaffected sons; females are affected at least as often as males.
- **Mitochondrial:** passes only through females to all offspring.

Strategy: first, look for two unaffected parents with an affected child (recessive). Then ask whether the sex of the affected children is mixed, and whether any father-to-son transmission occurs. Do not stop at the first fit; check each possibility against every family.

**7. Hardy-Weinberg equilibrium.** For a gene with two alleles at frequencies p (dominant, A) and q (recessive, a):

p + q = 1
p² + 2pq + q² = 1

where p² is the frequency of AA, 2pq of Aa, and q² of aa. Equilibrium holds if the population is large, mating is random, and there is no selection, mutation, migration or genetic drift. Standard workflow for a recessive trait:

1. Convert the proportion of affected individuals to q² (frequency of the homozygous recessive).
2. Take the square root to find q.
3. Find p = 1 − q.
4. Compute the carrier frequency 2pq and the dominant homozygotes p².

For **X-linked** recessive traits, the frequency of affected males equals q, and the frequency of affected females equals q². Two cautions: the equations give genotype frequencies, not "how many carriers there are among those with the dominant phenotype" (that is 2pq ÷ (p² + 2pq), a conditional probability), and the equations describe a baseline: a deviation (for example, an excess of homozygotes) suggests nonrandom mating, selection or another force acting ([Lesson 11](chapter:15)). For rare recessive alleles, q is small, so p ≈ 1 and the carrier frequency 2pq ≈ 2q.

**8. Chromosomal abnormalities.** **Nondisjunction** is failure of chromosomes to separate properly. It gives gametes with an extra or a missing chromosome and, after fertilization, **aneuploidy** (an abnormal number of one chromosome).

- **Meiosis I nondisjunction:** homologous chromosomes fail to separate. All four gametes are abnormal (two with an extra chromosome, two with none).
- **Meiosis II nondisjunction:** sister chromatids fail to separate. Two gametes are normal, one has an extra chromosome and one has none.
- **Mitotic nondisjunction** after fertilization gives **mosaicism**.
- **Trisomy** (3 copies) and **monosomy** (1 copy): most autosomal monosomies and many trisomies are generally lethal in embryos. Viable examples: **trisomy 21 (Down syndrome, 47,XX or XY,+21)**, trisomy 18 and trisomy 13 (severe, usually short-lived); **Turner syndrome (45,X)**; **Klinefelter syndrome (47,XXY)**; **47,XXX** and **47,XYY**. The risk of trisomy increases with maternal age. [VERIFY wording of "generally" claims]
- **Which parent and which division?** Using genetic markers on the extra chromosome in the child: if the child carries **both** of one parent's different homologs (heterozygous near the centromere), the error was in meiosis I; if the child carries **two identical copies** from one parent, the error was in meiosis II (ignoring crossing over).
- **Structural changes:** deletion, duplication, inversion and translocation. In a **balanced translocation** no genetic material is lost, so the carrier is generally healthy, but gametes can be unbalanced, causing infertility or miscarriage or an affected child (a Robertsonian translocation involving chromosome 21 is a reason for familial Down syndrome). **Polyploidy** (whole extra sets) is common in plants and generally lethal in humans.
- **Extra X or Y.** Only one X per cell is active, which is why extra X chromosomes tend to be better tolerated than extra autosomes.

**9. Gene interactions.** When two genes affect the same trait, the dihybrid 9 : 3 : 3 : 1 ratio changes. The 16 combinations are still present, but some phenotypes are merged. **Epistasis** is when one gene's genotype masks the expression of another.

| Interaction | F₂ ratio | Idea |
|---|---|---|
| None (independent) | 9:3:3:1 | Four phenotypes |
| Recessive epistasis | 9:3:4 | aa masks B locus |
| Complementary genes | 9:7 | Both needed |
| Dominant epistasis | 12:3:1 | One dominant masks |

A reliable method: any ratio that adds to 16 is a dihybrid cross with merged classes. Add up the classes of the combined phenotypes: 9 + 3 + 4 = 16 means a 9:3:4 ratio and thus one gene masks the other in its recessive form; 9 + 7 = 16 means both genes must contribute a dominant allele (a pathway with two steps, where a block at either step stops the product).

Example of recessive epistasis: in Labrador retrievers, coat color depends on gene B (black B_ or brown bb) and gene E (pigment deposited, E_, or not, ee). An *ee* dog is yellow no matter what its B genotype is: BbEe × BbEe gives 9 black : 3 brown : 4 yellow.

**Worked Example 1: Dihybrid and trihybrid probability (skill: product rule)**

(a) In a cross AaBb × AaBb with independent genes, what fraction of the offspring are aaB_? (b) In AaBbCc × AaBbCc, what is the probability of an offspring with the dominant phenotype for A and B but the recessive phenotype for C?

(a) P(aa) = 1/4 and P(B_) = 3/4, so P(aaB_) = 1/4 × 3/4 = **3/16**, which matches one of the "3" classes in 9 : 3 : 3 : 1. (b) P(A_) = 3/4, P(B_) = 3/4, P(cc) = 1/4, so P = 3/4 × 3/4 × 1/4 = **9/64**. A Punnett square for three genes would need 64 boxes; the product rule needs one line. In a trihybrid cross, the chance of the all-dominant phenotype is (3/4)³ = 27/64, and of the all-recessive phenotype is (1/4)³ = 1/64.

**Worked Example 2: Linkage and map distance (skill: recombination frequency)**

A plant AaBb in the *cis* arrangement is testcrossed with aabb. The offspring are: 420 AaBb, 380 aabb, 110 Aabb and 90 aaBb. Are the genes linked, and how far apart are they?

If A and B assorted independently, the four classes would be about equal (about 250 each). They are not: two classes are far more common, so the genes are linked. The parental types (matching the original chromosomes AB and ab) are the majority classes: 420 + 380 = 800. The recombinants are 110 + 90 = 200. Total = 1,000.

RF = 200 ÷ 1,000 × 100 = **20 percent**, so the genes are about 20 map units (20 cM) apart. A third gene C that is 8 cM from A and 12 cM from B would have to lie between them if A and B are 20 cM apart (8 + 12 = 20). Note that the two recombinant classes are about equal to each other, as are the two parentals; this is expected, since each crossover creates one of each.

**Worked Example 3: Pedigree plus Hardy-Weinberg (skill: combining conditional probability and allele frequency)**

An autosomal recessive disorder affects 1 in 2,500 people in a population at equilibrium. A healthy woman has a sister with the disorder (their parents are healthy). She plans a child with a healthy man from the general population. What is the probability that the child is affected?

Step 1, her carrier probability. Her parents are both Aa (they had an affected child). She is unaffected, so she is AA (1/3) or Aa (2/3). P(Aa) = 2/3.

Step 2, his carrier probability. q² = 1/2,500, so q = 1/50 = 0.02 and p = 0.98. Carrier frequency among all people: 2pq = 2 × 0.98 × 0.02 = 0.0392. A healthy man is one of the AA or Aa people, so strictly his carrier probability is 0.0392 ÷ (0.9604 + 0.0392) ≈ 0.0392, nearly unchanged, since affected people are so rare.

Step 3, the child. The child is affected only if both are carriers (2/3 × 0.0392) and both pass the recessive allele (1/4):

P = 2/3 × 0.0392 × 1/4 ≈ **0.0065**, about 1 in 150.

**Worked Example 4: An X-linked cross (skill: sex-linked inheritance)**

Red-green color blindness is X-linked recessive. A woman with normal vision whose father was color-blind marries a man with normal vision. What fractions of their sons, daughters and all children are expected to be color-blind?

Her father (XᶜY) must have given her his Xᶜ, and she has normal vision, so she is a carrier, XᶜX. The father is XY. Cross: XᶜX × XY gives XᶜX (carrier daughter), XX (normal daughter), XᶜY (affected son), XY (normal son), each 1/4. Daughters: none color-blind (0), half are carriers. Sons: **1/2** color-blind. All children: **1/4** color-blind. The probability that the next child is an affected son is 1/4; if you already know the child is a son, it is 1/2. The condition makes the difference.

**Worked Example 5: Nondisjunction (skill: which division failed)**

A child with trisomy 21 is tested at a DNA marker near the centromere of chromosome 21. The mother has alleles M1/M2, the father has M3/M3. The child has alleles M1, M2 and M3. Which parent and which meiotic division is at fault?

The child carries two different maternal alleles (M1 and M2), so both of the mother's homologs were passed to the egg: the homologs failed to separate, which is **nondisjunction in maternal meiosis I**. Had the child carried M1, M1 and M3 (two identical maternal copies), the error would have been in meiosis II, where the sister chromatids fail to separate. The father's M3 shows he contributed one chromosome, as normal. A related prediction: if a mother with 46,XX has nondisjunction of the X in meiosis I and the egg is fertilized by a Y-bearing sperm, the zygote is 47,XXY (Klinefelter syndrome); by an X-bearing sperm, 47,XXX; and an egg with no X fertilized by an X sperm gives 45,X (Turner syndrome). The combination YO (no X) is not viable.

**More Praxis Tips**

Praxis Tip: For a ratio problem, add up the numbers. If they add to 16, think two genes; if they add to 4, think one. Then ask which classes have merged.

Praxis Tip: In a testcross, the parental classes are the two most common phenotypes and the recombinants are the two least common. Always compute RF from the less common classes, and never exceed 50 percent.

Praxis Tip: For "what is the probability the next child is..." problems, separate two questions: is the parent a carrier (conditional probability), and does the carrier pass the allele (the Mendelian fraction)? Multiply them, and watch for the word "given".

Praxis Tip: For pedigrees, test each model against the most informative family first: two unaffected parents with an affected child eliminates all dominant models; an affected father with an unaffected daughter eliminates X-linked dominant; father-to-son transmission eliminates X-linked models.

Praxis Tip: In Hardy-Weinberg, the only number you can read straight from the problem is usually q² (the affected fraction). Square-root it first, then write p. The carrier frequency 2pq is almost always the answer being asked for, and it is much larger than q².

Praxis Tip: A mnemonic for nondisjunction: meiosis I fails, you keep different homologs; meiosis II fails, you keep identical twins (sister chromatids).

Praxis Tip: When you meet an unfamiliar ratio such as 9 : 7, do not panic. Total it, compare with 16, and ask which phenotype classes merged. The unfamiliarity is usually a name, not a concept.

Praxis Tip: Check your numerical work for "reasonableness": probabilities must be between 0 and 1, genotype frequencies must sum to 1, and map distances cannot exceed 50 percent in a single testcross. An answer outside these limits needs no further discussion; it is wrong.

**Common Mistakes**

- Using the Hardy-Weinberg equations when the population is clearly not in equilibrium (selection, small size, non-random mating), or taking q² as q.
- Giving the carrier frequency as q instead of 2pq.
- Counting phenotype ratios from a testcross as "parental" and "recombinant" without checking which classes are the majority.
- Assuming that a recessive disorder must show in every generation.
- Treating a father-to-son transmission as compatible with X-linkage.
- Confusing "probability the child is an affected boy" (1/4) with "probability a boy is affected" (1/2).
- Saying a recombination frequency of 60 percent is possible.
- Forgetting to condition on an unaffected phenotype (the 2/3 versus 1/2 error).
- Mixing up meiosis I and II nondisjunction.

**Checkpoint Questions**

1. In a cross AaBbCc × AaBbCc with all three genes assorting independently, what fraction of offspring are expected to show the recessive phenotype for A and the dominant phenotype for both B and C?
   A. 27/64
   B. 3/64
   C. 1/64
   D. 9/64

2. Recombination frequencies between three linked genes are: A–B 14 percent, A–C 6 percent and B–C 20 percent. Which gene lies between the other two?
   A. Gene B
   B. Gene A
   C. Gene C
   D. The order cannot be determined from these distances

3. In a population at Hardy-Weinberg equilibrium, an autosomal recessive disorder affects 1 person in 1,600. The carrier frequency is closest to
   A. 1 in 20
   B. 1 in 40
   C. 1 in 800
   D. 1 in 1,600

4. Two unaffected parents have an affected daughter. Which mode of inheritance is most consistent?
   A. X-linked recessive
   B. Autosomal dominant with full penetrance
   C. Autosomal recessive
   D. X-linked dominant

5. Which event could produce a son with the karyotype 47,XXY from a normal X-bearing egg?
   A. Fertilization by a sperm with no sex chromosome
   B. Fertilization by a sperm carrying both X and Y after nondisjunction in paternal meiosis I
   C. Fertilization by a sperm carrying two Y chromosomes after nondisjunction in meiosis II
   D. Fertilization by an ordinary Y-bearing sperm

6. Two pure-breeding white-flowered plant lines are crossed. The F₁ plants are all purple, and the F₂ is 9 purple : 7 white. This ratio is best explained by
   A. incomplete dominance at a single gene
   B. two independent genes each with simple dominance
   C. complementary gene action, in which a dominant allele at each of two genes is required for purple
   D. recessive epistasis giving a 9 : 3 : 4 ratio

7. A woman is a carrier of an X-linked recessive disorder and her partner is unaffected. What is the probability that their next child is an affected son?
   A. 1/4
   B. 1/2
   C. 0
   D. 1/8

---

**Stop here.** Answer every question on scratch paper before you read the reasons.

**Answers and reasons**

1. **D.** P(aa) × P(B_) × P(C_) = 1/4 × 3/4 × 3/4 = 9/64. (A is the fraction that are dominant for all three traits; B is the fraction recessive for A and B and dominant for C; C is the fraction recessive for all three traits.)
2. **B.** The two outer genes have the largest distance; here 14 + 6 = 20, so the order is B–A–C. (A it has the largest distance to C, so it lies at one end; C it has the largest distance to B, so it lies at one end; D the largest distance equals the sum of the two others, which fixes the middle gene.)
3. **A.** q² = 1/1,600 gives q = 1/40 = 0.025. Carriers are 2pq = 2 × 0.975 × 0.025 ≈ 0.049, about 1 in 20. (B is the frequency of the recessive allele q, not of carriers; C is half of the disease frequency, which has no meaning here; D is the frequency of affected people, not carriers.)
4. **C.** Two carrier parents can have an affected child of either sex; the other modes cannot explain an affected daughter of two unaffected parents. (A an affected daughter would require an affected father, who would not be unaffected; B the affected child would need an affected parent; D the unaffected parents would lack the dominant allele, so the daughter could not be affected.)
5. **B.** An egg with one X plus a sperm with X and Y gives XXY; the sperm has both sex chromosomes only if the X and Y failed to separate in meiosis I. (A would give a 45,X zygote; C would give 47,XYY; D would give a normal 46,XY zygote.)
6. **C.** A 9 : 7 ratio adds to 16 with three of the four classes merged, which is the signature of two genes that both need a dominant allele. (A would give a 1 : 2 : 1 ratio; B would give a 9 : 3 : 3 : 1 ratio with four phenotypes; D would produce three phenotypes, not two.)
7. **A.** P(son) = 1/2 and P(son receives the recessive X) = 1/2, so 1/2 × 1/2 = 1/4. (B is the chance that a son is affected, given that the child is a son; C is the chance that a daughter is affected; D includes an extra factor of 1/2 that does not apply.)

Praxis Tip: After the checkpoint questions, label each wrong choice with its slip (product rule misapplied, wrong mode of inheritance, q instead of 2pq, wrong division of meiosis) and log it in your error log (see Book 1, Strategy: The Question Method).

**Teach-Back and Spaced Review**

*Say this aloud in one breath:* "Alleles segregate and genes on different chromosomes assort independently, so crosses obey the product rule; departures from the 9:3:3:1 and 3:1 ratios signal incomplete dominance, codominance, epistasis, lethal alleles or linkage, and linked genes give mostly parental offspring with a recombination frequency of at most 50 percent that serves as map distance; X-linked traits pass from carrier mothers to half their sons, pedigrees are read by testing each model against the most informative family, Hardy-Weinberg turns the affected fraction into q, then p and 2pq, and nondisjunction in meiosis I or II makes aneuploidies such as trisomy 21, Turner and Klinefelter syndromes."

*Review schedule:* revisit this lesson after 1 day (redo Worked Examples 2 and 3 without looking), after 3 days (checkpoint questions from a blank page), after 7 days (a mixed set that includes [Lesson 9](chapter:13) techniques and [Lesson 8](chapter:12) gene regulation), and after 21 days (explain the lesson aloud).

*Interleave:* alternate a probability problem, a pedigree problem and a population problem, then do the [Genes and Evolution Set](chapter:16), which uses these skills in data passages.

Praxis Tip: End each study session by writing, from memory, the Hardy-Weinberg equations, the cases of epistasis with their ratios, and the list of common aneuploidies with their karyotypes.

---

**Author verification note (remove before publishing)**

- All examples and questions are original. Computed and checked: 3/16; 9/64 and 27/64; linkage RF = 200/1,000 = 20 percent; q = 0.02, 2pq = 0.0392, 2/3 × 0.0392 × 1/4 = 0.00653; (not used in the text, spare values: q = 0.4 gives p² = 0.36, 2pq = 0.48; X-linked q = 0.08 gives affected females 0.0064, carrier females 0.1472); 1 in 1,600 gives q = 0.025 and 2pq = 0.04875 (about 1 in 20).
- Answer key positions: D, B, A, C, B, C, A.
- Verify with a genetics reviewer: statements on penetrance and mitochondrial inheritance wording; X inactivation "generally" wording; the viability statements for trisomies and monosomies; epistasis ratios (standard); the 47,XXX and 47,XYY entries; the Robertsonian translocation example.
- Category 1C topics covered: Mendelian concepts (phenotype and genotype, gene, locus, allele, homozygosity and heterozygosity, wild type, recessiveness, complete dominance, codominance, incomplete dominance, penetrance and expressivity, hybridization and monohybrid and dihybrid crosses, test crosses, Punnett squares, gene interactions, sex-linked inheritance, pedigrees, linkage, recombination), meiosis and genetic variability (nondisjunction, aneuploidy), and Hardy-Weinberg.
