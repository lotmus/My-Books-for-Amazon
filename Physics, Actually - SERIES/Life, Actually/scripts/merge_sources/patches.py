import os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from figcaps import GEN_FIG_CAPTIONS, GEN_FIG_KIND
PARTS=[
 ('I','Chemistry That Learned to Copy','Origins',1,5),
 ('II',"Darwin’s Machine",'Darwins_Machine',6,11),
 ('III','The Big Transitions','Transitions',12,18),
 ('IV','Us','Us',19,21),
 ('V','Minds, Loops and Machines','Minds',22,29),
 ('VI','The Molecule','Molecule',30,40),
 ('VII','Inheritance','Inheritance',41,49),
 ('VIII','Reading and Writing the Text','Reading_Writing',50,61),
 ('IX','Dinner, and the Whole Genome','Dinner_Genome',62,68),
 ('X','Your Own Text, and the Edit to Come','Your_Own',69,76),
 ('XI','Life Elsewhere','Life_Elsewhere',77,84),
]
PART_INTROS={}
PATCHES={}
SECTION_REPLACE={}

MAP2 = """### The Sentence the Book Runs On

The Prologue promised that one sentence would carry the whole book, and this chapter has now earned it. Life is chemistry that copies itself, imperfectly, and lets the imperfections be judged. Every Part that follows is one view of that sentence: the chemistry in the rest of Part I, the judging in Parts II to IV, its strangest product in Part V, the copier itself and what we have done with it in Parts VI to X, and, in Part XI, the question of whether the same chemistry has started anywhere else.

The chapters ahead are short. The ideas inside them are not.
"""

MAP = """### A Map of the Book

Here is where this book is going, and the thread that ties it together. Life, in the working definition this chapter settles on, is chemistry that copies itself, imperfectly, and lets the imperfections be judged. Every part of the book is one view of that sentence.

Part I is the chemistry: which atoms matter, why carbon and water, how chemistry that merely happens might have become chemistry that copies, and the first cells, which stayed microscopic for about three billion years. Parts II and III are the judging: Darwin's machine, how selection, sex and cooperation work, and the great transitions, from the cell that swallowed an engine to the Cambrian explosion and the mass extinctions that reset the board. Part IV is us, a recent and unfinished branch. Part V follows evolution to its strangest product, a brain that builds a model of itself, and asks whether a mind could be built from anything else.

Then the book opens the copier itself. Parts VI and VII are the molecule, DNA, and how it passes from parent to child: the shape worked out in Cambridge in 1953, the letters, the copying machine and its mistakes, a friar's peas and a room full of flies. Parts VIII to X are what we have done with that knowledge in seventy years: learned to read the text, then to cut it, write it, clone it, put it on the dinner plate and read our own, and finally to ask whether we should edit it in our children.

Part XI leaves Earth. If life is chemistry that copies itself, there is no obvious reason it should have happened only once. The last chapters ask what life needs, where else those needs are met, how we are searching Mars, the buried oceans of the outer moons and the air of planets around other stars, and what a second, independent beginning would tell us about the first. The Epilogue gathers the thread.

The chapters ahead are short. The ideas inside them are not.
"""

BATTERY = """### The Battery Every Cell Runs On

Chapter 2 called the cell's energy currency ATP, the small molecule that pays for nearly everything a cell does. How a cell makes it is one of the strangest discoveries in biology. In the 1960s the British biochemist Peter Mitchell proposed that cells pump protons, the positively charged cores of hydrogen atoms, across a membrane, then let them flow back through a tiny turbine that builds ATP as it spins. The idea seemed so odd that it took about ten years to be accepted. Chapter 36 takes the turbine apart.

What matters here is how old the trick is. Bacteria run it across the skin of the cell. Plants run it inside their chloroplasts, the solar-powered factories in every leaf cell. You are running it right now, in the mitochondria of every one of your cells. Every branch of the tree of life uses it, so the last common ancestor very likely did too. It may be as old as life itself. That is one reason origin-of-life researchers pay so much attention to alkaline vents on the ocean floor.

Those vents produce natural proton gradients, just like the ones early cells learned to use.
"""

GARDEN = """### The Answer in a Monastery Garden

Gregor Mendel, an Augustinian friar in Brno, crossed garden peas for eight seasons, from 1856 to 1863, and counted the offspring. A cross of round-seeded and wrinkled-seeded plants gave only round seeds. The next generation brought wrinkled seeds back, about one for every three round. Three to one, again and again, for each of the seven traits he tracked.

The ratio meant that inheritance is not like mixing paint. It is like dealing marbles. Each plant carries two factors for every trait and passes one, at random, to each offspring. A hidden factor is not diluted. It waits, whole, and reappears when two of them meet in a grandchild. Jenkin's objection dissolves. A useful new trait is not a drop of ink that fades in the bucket. It is a marble, and marbles do not dilute.

Mendel published in 1866, and almost nobody read him. In 1900 three botanists found the ratio again, then found his paper. Within a decade the factors had a name, genes, and an address on the chromosomes, thanks to a room full of fruit flies at Columbia University. Part VII tells that whole story, from the garden in Brno to the fly room. This chapter needs only the result: heredity comes in particles.
"""

BONES = """### Reading Genes Instead of Bones

For most of the twentieth century, everything known about Neanderthals and other extinct relatives came from bones and the stone tools buried with them. Then, from the late 1990s, geneticists learned to read DNA out of the bones themselves. That is a hard trick, because DNA breaks down fast after death. Svante Pääbo, who pioneered the field, received the 2022 Nobel Prize in Physiology or Medicine for it.

The biggest surprise was that our ancestors and the Neanderthals had children together. If your ancestry lies mostly outside sub-Saharan Africa, about one to two percent of your DNA came from Neanderthals. Picture your genome as a hundred-page book: one or two of the pages, scattered through the text, were written by Neanderthals. A second group, the Denisovans, known for years only from a finger bone and a few teeth, left a few percent of the DNA of people in Papua New Guinea and Aboriginal Australians. The old picture, in which modern humans simply replaced everyone else without mixing, did not survive. Chapter 58 tells how the dead were read, and what else they said.

The real picture turned out to be messier, and more interesting, than that clean story.
"""

THINAIR = """### Borrowed Genes for Thin Air

A second case involves the Denisovans of Chapter 19. People on the Tibetan Plateau breathe air that holds much less oxygen than air at sea level. Lowlanders who move up often overreact, making far too many red blood cells, which thickens the blood. Many Tibetans carry a version of a gene called *EPAS1* that damps that overreaction. It did not arise as a new mutation. It came from the Denisovans, through ancient interbreeding, and selection then spread it in the one population that lived high enough to need it. Chapter 58 tells how the borrowing was traced.

Natural selection did not have to invent the adaptation. It only had to keep it.
"""

SYNTH = ("Chapter 8 told how Darwin's theory waited for two missing pieces. Mendel supplied the first: heredity comes in particles that do not blend. "
 "Mutation is the second, the source of genuinely new variants, and this chapter's chemistry is the mechanism Darwin lacked. "
 "Mutation supplies raw variation. Recombination, the shuffling of chromosome pieces between parents that Part VII explains, mixes it further. "
 "Selection, the bookkeeping of Chapter 7, changes which variants become common. Mutation without selection is just noise. "
 "Selection without mutation has nothing to select. Together they are the theory of evolution.")

SECTION_REPLACE = {
 1: [('A Map of the Book', MAP2)],
 4: [('The Battery Every Cell Runs On', BATTERY)],
 8: [('The Monk Who Counted', GARDEN), ('Particles, Not Paint', None), ('Found Three Times', None)],
 19: [('Reading Genes Instead of Bones', BONES), ('We Interbred With Them', None)],
 20: [('Borrowed Genes for Thin Air', THINAIR)],
}

PATCHES = {
 5: [("How much it drives mutation rates in living cells is still an open research question.",
      "How much it drives mutation rates in living cells is still an open research question. Chapter 40 returns to it, with the calculations that revived the idea in 2022.")],
 7: [("Chapter §E9§ will show just how accurate this copying usually is, and how it still isn't quite perfect.",
      "Chapters 37 and 40 show just how accurate this copying usually is, and how it still isn't quite perfect.")],
 8: [('__TITLE__', 'The Modern Synthesis: How Darwin Met Mendel')],
 15: [("Chapter §E9§ counted roughly twenty thousand protein-coding genes in the human genome.",
       "The human genome holds roughly twenty thousand protein-coding genes, a count Chapter 67 returns to.")],
 17: [("a question Chapter §E31§ will take up in full", "a question Part XI takes up in full")],
 20: [("which then drove genetic change in the population that adopted it.",
       "which then drove genetic change in the population that adopted it. Chapter 36 shows the switch itself, a stretch of DNA in a neighbouring gene that keeps lactase on.")],
 30: [("is the last argument of this book.", "is an argument for the end of Part X.")],
 40: [(r"re:Charles Darwin, in 1859, needed exactly one ingredient.*?Neither, alone, is the theory of evolution; together, they are\.", SYNTH),
      ("it is the one Lothar asked about directly", "it is the one readers ask about most often")],
 41: [("A garden of peas will show the same rule later, in Part IV, and the friar", "A garden of peas shows the same rule in Chapter 46, and the friar")],
 49: [("Part XI will pick them up", "Part X will pick them up")],
 54: [("A spit tube of the kind in the prologue", "A spit tube of the kind in Chapter 30")],
 61: [("is the argument of Part XI", "is the argument of Part X")],
 68: [("a tube posted in the prologue", "a tube posted in Chapter 30")],
 69: [("the prologue promised her", "Chapter 30 promised her")],
 73: [("since the Prologue", "since Chapter 30")],
 76: [("since Part VI,", "since Part VIII,"), ("forty-five chapters", "seventy-five chapters")],
 48: [("Chapter 40 already joined the pieces.", "Chapters 8 and 40 already joined the pieces.")],
}

PART_INTROS = {
 'I': "Before there was evolution there had to be something to evolve. This Part looks for the line between chemistry and life, and for the moment, about four billion years ago, when a molecule first made a copy of itself.",
 'II': "Once something copies itself with mistakes, a machine starts running that nobody built. Darwin found it. This Part explains how it works, why it needed particles of heredity, and why it produced sex and kindness as well as teeth.",
 'III': "For three billion years life was single cells. Then it learned to merge, to build bodies, and to survive the catastrophes that kept clearing the board. This Part follows those inventions.",
 'IV': "One branch of the tree is ours. It is recent, it was crowded with cousins, and selection is still editing it.",
 'V': "Evolution's most surprising product is a brain that models itself. This Part asks what a self is, whether one could be built from something other than neurons, and what our machines tell us about our own minds.",
 'VI': "So far the book has followed the copies. This Part opens the copier: the molecule whose shape was found in 1953, its four letters, the machine that copies them and the mistakes it makes. Three invented people, Ruth, her daughter Anna and Anna's son Theo, help carry the ideas from here to Part X.",
 'VII': "A child is a new shuffle of two old texts. This Part explains the shuffle, then goes back to the friar who first counted it, the flies that gave it an address, and the people who turned it into a programme of cruelty.",
 'VIII': "Within fifty years of the double helix we could read the text, cut it, copy it in a test tube and write it from scratch. This Part tells how, and what the tools have already done, from the first gene cures to a cloned sheep.",
 'IX': "Humans edited the text of other species for ten thousand years before anyone had heard of DNA. This Part follows that editing to the dinner plate, then turns to the reading of the whole human text, and of millions of people at once.",
 'X': "The text is now cheap to read, including yours. This Part asks what it can tell you, who else is reading it, and whether we should correct it, first in patients and then, perhaps, in children.",
 'XI': "If life is chemistry that copies itself, nothing in the chemistry says it had to happen only once. This Part leaves Earth to ask where else the copying could have started, how we would know, and what finding it would teach us about ourselves.",
}

# ---- coherence pass (one book): self-references written for the old Genetics volume
for _n,_old,_new in [
 (72,'What remains, for the last part of the book, is the question','What remains, for the rest of this Part, is the question'),
 (75,'The last chapter of this book is about what a hundred years of all this might look like','The next chapter is about what a hundred years of all this might look like'),
 (76,'using the three words this book has used since Part VIII,','using the three words this book has used since its Prologue,'),
 (46,'they are the moment the subject of this book stops being a matter of opinion','they are the moment heredity stops being a matter of opinion'),
]:
    PATCHES.setdefault(_n,[]).append((_old,_new))
