# -*- coding: utf-8 -*-
OPS = [
# ---- ch37 origin of life
('delsec', 1236),
('replace', 953, [
 "Carbon chemistry in water is the only known basis for life. Other possibilities have been examined. Silicon can form chains, but the bonds are weaker and the oxides are solid. The temperature range in which silicon chemistry remains fluid is narrow. Ammonia and methane can serve as solvents at lower temperatures. The reaction rates are slower. No self-replicating system based on either solvent has been demonstrated.",
 "Energy sources other than chemical redox or sunlight are conceivable. Tidal heating, radiolysis, and geothermal gradients already power ecosystems on Earth that do not rely on photosynthesis. The same sources could operate elsewhere. The requirement is a sustained free-energy flux and a mechanism of heredity. The particular molecules that satisfy the requirement may vary.",
 "Laboratory work has expanded the genetic alphabet with synthetic base pairs, which shows that other informational polymers are chemically possible. No living system built on them has been made, so alternative biochemistries remain possible but unsupported by observation.",
]),
# ---- ch38 cell
('delsec', 1924),
('sub', 123, "In eukaryotic cells, an internal skeleton of protein filaments gives shape and moves cargo.", "In eukaryotic cells, an internal skeleton of protein filaments gives shape and moves cargo. Energy is obtained by oxidising organic molecules or by photosynthesis, with ATP as the common currency, and information flows from DNA to RNA to protein."),
('delsec', 1860),
('replace', 1879, [
 "Culture-independent methods—16S rRNA sequencing and metagenomics—have revealed that the majority of microbial species have never been grown in the laboratory. The uncultured majority includes entire phyla. Their ecological roles are inferred from genomes and from environmental correlations. The inference is incomplete. It is already sufficient to show that microbial diversity and activity dominate the biosphere.",
 "Prokaryotic metabolism is more diverse than that of all eukaryotes combined, and microbes cycle carbon, nitrogen, sulphur and metals from hydrothermal vents to the human gut. Viruses, the most abundant biological entities, regulate microbial populations and mediate horizontal gene transfer. The microbial world is therefore both the metabolic foundation of the biosphere and a continuous source of genetic innovation.",
], "The Uncultured Majority"),
('delsec', 1876),
('sub', 411, "Amoebae are protists that move and feed by extending temporary projections of cytoplasm called pseudopods. The projections form by local changes in the cytoskeleton. The cell crawls toward food or away from harm. Some amoebae are free-living in soil and water. Others are parasitic.", "Amoebae, described in their own section, are protists that move and feed by extending pseudopods."),
# ---- ch39 genetics
('del', 198, "Gregor Mendel, working with pea plants"),
('del', 198, "The factors are genes. They are carried"),
('sub', 198, "The mechanism was missing.", "The mechanism was missing, and it arrived in stages: first Mendel’s factors and the chromosomes that carry them, described in the next sections, then mutation, and finally DNA itself."),
('sub', 198, "The genetic code maps triplets of bases to amino acids. The code is nearly universal. The universality is evidence of common ancestry.", "A triplet code of bases specifies amino acids, and its near-universality is evidence of common ancestry."),
('sub', 216, "Adenine pairs with thymine. Guanine pairs with cytosine. The pairing accounts for", "The pairing rules are adenine with thymine and guanine with cytosine, and they account for"),
('sub', 216, "Franklin and Gosling described the B form as helical, with a pitch of about 34 angstroms, about ten nucleotides per turn, and a diameter of about 20 angstroms. The phosphate groups lie on the outside.", "Franklin and Gosling described the B form as a helix with the phosphate groups on the outside."),
('sub', 216, "The complementary pairing is the copying rule.", "Complementarity is what makes the copying possible."),
('sub', 905, "Variation is measured by", "In large populations selection efficiently removes deleterious alleles, while in small populations drift lets them accumulate, and standing variation supplies the raw material for adaptation when the environment changes. Variation is measured by"),
('delsec', 1937),
# ---- ch40 evolution
('delsec', 2402),
('sub', 914, "Once gene flow stops, independent evolution proceeds.", "Once gene flow stops, independent evolution proceeds, and chromosomal rearrangements or cytoplasmic incompatibilities can speed the process."),
('delsec', 1934),
('sub', 926, "Drift fixes neutral alleles and can override weak selection.", "Drift fixes neutral alleles and can override weak selection; selection dominates only when the selection coefficient exceeds the reciprocal of the effective population size."),
('add', 926, "The framework accounts for the maintenance of polymorphism, the rate of molecular evolution and the genetic structure of subdivided populations, and it is the quantitative core of evolutionary genetics."),
('delsec', 1930),
('replace', 1107, [
 "Example 1. A recessive lethal allele has frequency 0.01. What fraction of the population dies from it each generation under random mating?",
 "Frequency of homozygotes = \\( q^2 = 10^{-4} \\). One in ten thousand individuals is affected.",
 "Example 2. A haploid allele with selective advantage \\( s = 0.01 \\) starts at frequency 0.001 in a large population. Approximately how many generations are required for it to reach frequency 0.5?",
 "The odds \\( p/(1-p) \\) grow by a factor \\( 1+s \\) each generation. The odds must rise from about 0.001 to 1, so the time is \\( \\ln(1000)/\\ln(1.01) \\approx 6.9/0.00995 \\approx 690 \\) generations.",
 "Example 3. In a population of effective size 10 000, what is the probability that a new neutral mutation eventually becomes fixed?",
 "The fixation probability of a neutral allele is \\( 1/(2N) = 5 \\times 10^{-5} \\).",
 "These elementary results are the starting point for every calculation of evolutionary rates and of the expected frequency of genetic disease.",
]),
]
