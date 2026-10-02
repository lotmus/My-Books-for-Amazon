"""Write book/chapters/12_Back_Matter.md: Epilogue, Core Ideas, Glossary, Further Reading,
Bibliography, Photo Credits and Index, in the Physics, Actually back-matter order."""
import os,re,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from normalize import americanize, smart_quotes
H=os.path.dirname(os.path.abspath(__file__)); B=os.path.join(H,'back')
APP=open(os.path.join(H,'..','src','z','chapters','12_Appendix.md'),encoding='utf-8').read()
def section(name):
    m=re.search(r'^## '+re.escape(name)+r'\n(.*?)(?=^## |\Z)',APP,re.M|re.S); return m.group(1).strip()
REFS={'AAV':73,'Allele':43,'Base':35,'Base editing':56,'Base pair':33,'Cas9':55,'Clone':60,'CRISPR':55,'Chromatin':35,
 'Chromosome':35,'Codon':38,'Diploid':41,'Dominant':43,'Enhancer':39,'Epigenetics':44,'Eugenics':49,'Event':63,'Exon':39,
 'Franklin, Rosalind':32,'Gene-edited':63,'Genome-wide association study (GWAS)':68,'Genotyping':69,'Germline':74,'Guide RNA':55,
 'Haplogroup':42,'Heritability':43,'Intron':39,'Manhattan plot':68,'Meiosis':41,'Messenger RNA (mRNA)':38,'Mitochondrial DNA':42,
 'Mutation':40,'Nanopore sequencing':54,'Pangenome':67,'Penetrance':70,'Photo 51':32,'Point mutation':40,'Plasmid':50,
 'Polygenic score':71,'Polymerase chain reaction (PCR)':52,'Preimplantation genetic testing (PGT)':74,'Prime editing':56,
 'Recessive':43,'Recombination':41,'Restriction enzyme':50,'Ribosome':38,'Semiconservative replication':33,'Splicing':39,
 'Stacked trait':65,'Tautomer':40,'Telomere':37,'Transcription':38,'Transfer RNA (tRNA)':38,'Translation':38,'Transgenic':63,'Transposon':39}
entries={}
for line in section('A Spit-Kit Glossary').splitlines():
    m=re.match(r'\*\*(.+?)\*\* — (.*)',line.strip())
    if m:
        t,d=m.groups(); d=d.rstrip()
        if t in REFS: d+=f' See Chapter {REFS[t]}.'
        entries[t]=d
for line in open(os.path.join(B,'extra_glossary.txt'),encoding='utf-8'):
    if ' — ' in line: t,d=line.strip().split(' — ',1); entries[t]=d
gl=['## Glossary','','Terms are explained where they first appear. This list is a reminder, with the chapter where each term is developed.','']
for t in sorted(entries,key=lambda s:s.lower().lstrip('(')):
    gl+=[f'**{t}** — {entries[t]}','']
FR='''## Further Reading

These are the books discussed in this one, plus a few that go further, grouped by the Parts they extend. Each is a good next step for a reader who wants more.

### Origins and Evolution (Parts I to IV)

Principles of Geology, by Charles Lyell (John Murray, 1830–1833) — the book Darwin took on the Beagle, and the source of the deep time his theory needed. See Chapter 6.

On the Origin of Species, by Charles Darwin (John Murray, 1859) — still readable, still the best single argument for natural selection. See Chapters 6 and 7.

What Is Life?, by Erwin Schrödinger (Cambridge University Press, 1944) — the physicist's question behind Chapter 1, and behind the whole book.

The Selfish Gene, by Richard Dawkins (Oxford University Press, 1976) — evolution from the gene's point of view, the subject of Chapter 9.

The Extended Phenotype, by Richard Dawkins (Oxford University Press, 1982) — the more technical sequel, for readers who want to go further into Chapter 9.

The Evolution of Cooperation, by Robert Axelrod (Basic Books, 1984) — the computer tournaments behind Chapter 11.

Wonderful Life, by Stephen Jay Gould (W. W. Norton, 1989) — the Burgess Shale and the case for contingency, one side of the argument in Chapter 17.

The Beak of the Finch, by Jonathan Weiner (Alfred A. Knopf, 1994) — evolution watched in real time on the Galápagos, expanding on Chapter 20.

Life's Solution, by Simon Conway Morris (Cambridge University Press, 2003) — the case for convergence, the other side of Chapter 17.

In the Blink of an Eye, by Andrew Parker (Free Press, 2003) — one bold explanation for the Cambrian explosion of Chapter 14.

Endless Forms Most Beautiful, by Sean B. Carroll (W. W. Norton, 2005) — the genes that build bodies, the subject of Chapter 15.

Life on the Edge, by Johnjoe McFadden and Jim Al-Khalili (Bantam Press, 2014) — quantum biology at book length, going further into Chapter 5.

The Vital Question, by Nick Lane (Profile Books, 2015) — energy, vents and the origin of complex cells, behind Chapters 3, 4 and 12.

Who We Are and How We Got Here, by David Reich (Pantheon, 2018) — ancient DNA and the human story of Chapters 19 and 58.

### Minds and Machines (Part V)

Gödel, Escher, Bach, by Douglas R. Hofstadter (Basic Books, 1979) — the original strange loop, the source of Chapter 22.

The Mind's I, edited by Douglas R. Hofstadter and Daniel C. Dennett (Basic Books, 1981) — the anthology behind Chapter 25.

Metamagical Themas, by Douglas R. Hofstadter (Basic Books, 1985) — essays on patterns, self-reference and analogy.

The Society of Mind, by Marvin Minsky (Simon & Schuster, 1986) — a mind built from many mindless parts.

The Intentional Stance, by Daniel C. Dennett (MIT Press, 1987) — how we attribute beliefs and desires, and why it works.

Mind Children, by Hans Moravec (Harvard University Press, 1988) — the robot future of Chapter 29, in its author's words.

Consciousness Explained, by Daniel C. Dennett (Little, Brown, 1991) — the multiple-drafts model of Chapters 24 and 27.

Fluid Concepts and Creative Analogies, by Douglas R. Hofstadter and the Fluid Analogies Research Group (Basic Books, 1995) — analogy as the core of thought, behind Chapter 23.

Darwin's Dangerous Idea, by Daniel C. Dennett (Simon & Schuster, 1995) — natural selection as a universal acid, the subject of Chapter 24.

I Am a Strange Loop, by Douglas R. Hofstadter (Basic Books, 2007) — the self as a pattern, returning to Chapter 22.

Surfaces and Essences, by Douglas R. Hofstadter and Emmanuel Sander (Basic Books, 2013) — analogy at full length.

### The Molecule and the Edit (Parts VI to X)

The Eighth Day of Creation, by Horace Freeland Judson (Simon & Schuster, 1979) — the long history of how the molecule was worked out, from the phage group through the code. The one to open if Part VI felt too short.

In the Name of Eugenics, by Daniel J. Kevles (Alfred A. Knopf, 1985) — the history behind Chapter 49, and the right next book if that chapter is the one that stays.

Rosalind Franklin: The Dark Lady of DNA, by Brenda Maddox (HarperCollins, 2002) — the biography; Chapter 32 is a sketch beside it.

Life's Greatest Secret, by Matthew Cobb (Profile Books, 2015) — the race to crack the genetic code, at the length that story deserves.

The Gene: An Intimate History, by Siddhartha Mukherjee (Scribner, 2016) — much of the same ground as Parts VI to X in a different voice. Read it as another account, not as a correction of the dates and counts given here.

The Code Breaker, by Walter Isaacson (Simon & Schuster, 2021) — Jennifer Doudna and the CRISPR story of Chapters 55 and 56.

### Life Elsewhere (Part XI)

Rare Earth, by Peter D. Ward and Donald Brownlee (Copernicus, 2000) — the argument that complex life is rare, one answer to Chapter 83.

The Eerie Silence, by Paul Davies (Allen Lane, 2010) — SETI, the shadow biosphere and what the silence means, behind Chapters 82 and 84.

Five Billion Years of Solitude, by Lee Billings (Current, 2013) — the people and telescopes behind the search for other Earths of Chapters 78 and 81.

The Zoologist's Guide to the Galaxy, by Arik Kershenbaum (Penguin Press, 2021) — what evolution suggests alien life might be like, if it exists.
'''
BIB=open(os.path.join(B,'bibliography.txt'),encoding='utf-8').read().strip().splitlines()
bib=['## Bibliography','','This is the formal reference list behind the book: the original papers its account of life rests on, for readers who want to trace an idea back to its source. Entries with a full date rather than volume and page numbers are recent papers cited as first published.','']
for l in sorted([l for l in BIB if l.strip()], key=lambda s: re.sub(r'[^a-z]','',s.lower())):
    bib+=[l,'']
cred=section('Photo Credits')
def renum(m): return f'Figure {int(m.group(1))+1}.'
cred=re.sub(r'^Figure (\d+)\.',renum,cred,flags=re.M).replace('the one chapter 39 names','the one Chapter 69 names').replace('The diagrams are original.','The diagrams are original. Figures 48 to 50 were drawn for this book.')
pc=['## Photo Credits','',cred,'']
pre=[open(os.path.join(B,'epilogue.md'),encoding='utf-8').read().strip(),'',open(os.path.join(B,'core.md'),encoding='utf-8').read().strip(),'']+gl+[FR.strip(),'']
post=pc+['## Index','','References are to chapter numbers; each is a link.','','%%INDEX%%','']
text=smart_quotes(americanize('\n'.join(pre)))+'\n'+smart_quotes('\n'.join(bib))+'\n'+smart_quotes(americanize('\n'.join(post)))
dst=sys.argv[1] if len(sys.argv)>1 else os.path.join(H,'..','book','chapters','12_Back_Matter.md')
open(dst,'w',encoding='utf-8').write(text); print('wrote',dst,len(text.split()),'words; glossary',len(entries),'bib',len(bib)//2-2)
