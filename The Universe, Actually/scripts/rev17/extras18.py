"""REV18 extras, applied in place to the docx built by rev17.py:
 - a 'Further Reading' paragraph at the end of each of the eleven Parts
 - new bibliography entries for the books named there
 - a photograph-credits paragraph in 'A Note on Sources'
Usage (from scripts/rev17):  python extras18.py ../../The_Universe_Actually__REV18.docx"""
import sys, os, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rev16'))
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
import docx
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from engine import newpara, runs_of, base_rpr, mkrun
W = lambda t: qn('w:' + t)
path = sys.argv[1]
d = docx.Document(path); body = d.element.body
text = lambda p: ''.join(t.text or '' for t in p.iter(W('t')))
def style(p):
    s = p.find(W('pPr')); s = s.find(W('pStyle')) if s is not None else None
    return s.get(W('val')) if s is not None else ''
kids = [e for e in body.iterchildren() if e.tag == W('p')]
tpl = next(p for p in kids if style(p) == '' and len(text(p)) > 150)
rpr0 = base_rpr(runs_of(tpl)[0])

FR = {
 'I': "*The Feynman Lectures on Physics*, Volume I, is free online and is the natural next step; read the chapters on energy and on the kinetic theory of gases first. Schiller’s *Motion Mountain* covers the same ground with a modern eye, and Asimov’s *Understanding Physics* tells how the ideas were found.",
 'II': "Feynman’s *QED* is four short lectures on how light and electrons really behave, written for anyone. Carroll’s *Something Deeply Hidden* argues for the many-worlds reading of quantum mechanics, and Everett’s original 1957 paper is short enough to read. Mead’s *Collective Electrodynamics* rebuilds electromagnetism from quantum ideas.",
 'III': "Weinberg’s *The First Three Minutes* is the classic account of how the lightest nuclei were made. The Particle Data Group’s *Review of Particle Physics* is where the numbers in this Part are kept, and Asimov’s *A Short History of Chemistry* shows how the periodic table was assembled.",
 'IV': "Epstein’s *Relativity Visualized* teaches special and general relativity with pictures and almost no mathematics. Hawking’s *A Brief History of Time* is the popular classic on black holes, and Hawking and Penrose’s *The Nature of Space and Time* puts their two views side by side. Wheeler and Ford’s *Geons, Black Holes, and Quantum Foam* is a memoir of the field by one of its builders.",
 'V': "Sagan’s *Cosmos* remains the best invitation to the sky. Tyson and Goldsmith’s *Origins* tells the story from the Big Bang to the first planets, and Asimov’s *New Guide to Science* is a patient tour of the facts.",
 'VI': "Weinberg’s *The First Three Minutes* and Barrow’s *The Origin of the Universe* give the standard picture in short books. Greene’s *The Fabric of the Cosmos* takes on space, time and the arrow of time, Penrose’s *Cycles of Time* proposes a stranger answer, and Barbour’s *The End of Time* denies that time exists at all. Carroll’s *The Big Picture* ties these questions to everything else.",
 'VII': "Dawkins’s *The Blind Watchmaker* explains natural selection as clearly as anyone has, and Watson’s *The Double Helix* is a candid memoir of the discovery of DNA’s shape. Lane’s *The Vital Question* asks why complex cells evolved only once, and McFadden and Al-Khalili’s *Life on the Edge* covers quantum effects in living things. For human origins, read Tattersall’s *Masters of the Planet*, Wragg Sykes’s *Kindred*, Mithen’s *After the Ice*, and the articles in Scarre’s *The Human Past*. Harari’s *Sapiens* and Graeber and Wengrow’s *The Dawn of Everything* disagree usefully about what came next, Anthony’s *The Horse, the Wheel, and Language* follows the steppe herders, and Lewis-Williams’s *The Mind in the Cave* asks about the first art.",
 'VIII': "Hofstadter’s *I Am a Strange Loop* and the collection he edited with Dennett, *The Mind’s I*, are the best places to start thinking about what a self is. Asimov’s *The Human Brain* is old but well organized, and Seth’s *Being You* argues that consciousness is controlled hallucination.",
 'IX': "Weart’s *The Discovery of Global Warming* follows the science from the 1800s to now. Ritchie’s *Not the End of the World* weighs the major environmental problems with data, and Carroll’s *The Big Picture* reminds us that a living planet is a physical phenomenon too.",
 'X': "Shannon and Weaver’s *The Mathematical Theory of Communication* is where information theory began. Singh’s *The Code Book* tells the history of secret writing, Russell’s *Human Compatible* asks what it means to build machines whose goals match ours, and Hofstadter’s *Gödel, Escher, Bach* is the great playful book about minds, machines and meaning.",
 'XI': "Kuhn’s *The Structure of Scientific Revolutions* and Popper’s *The Logic of Scientific Discovery* are the two classic arguments about how science changes. Hofstadter’s *Metamagical Themas* and *Surfaces and Essences* show how analogy drives thinking, Axelrod’s *The Evolution of Cooperation* is a model of testing an idea by simulation, and Greene’s *Until the End of Time* places the whole story in cosmic time.",
}
NEWBIB = [
 'Kuhn, Thomas S. The Structure of Scientific Revolutions. University of Chicago Press, 1962.',
 'Lane, Nick. The Vital Question: Energy, Evolution, and the Origins of Complex Life. W. W. Norton, 2015.',
 'Popper, Karl R. The Logic of Scientific Discovery. Hutchinson, 1959.',
 'Ritchie, Hannah. Not the End of the World: How We Can Be the First Generation to Build a Sustainable Planet. Chatto & Windus, 2024.',
 'Russell, Stuart. Human Compatible: Artificial Intelligence and the Problem of Control. Viking, 2019.',
 'Seth, Anil. Being You: A New Science of Consciousness. Faber & Faber, 2021.',
 'Shannon, Claude E., and Warren Weaver. The Mathematical Theory of Communication. University of Illinois Press, 1949.',
 'Singh, Simon. The Code Book: The Science of Secrecy from Ancient Egypt to Quantum Cryptography. Fourth Estate, 1999.',
 'Weart, Spencer R. The Discovery of Global Warming. Harvard University Press, 2003.',
]
CREDITS = ("Photographs. The photographs in this book come from NASA and its partner agencies’ public image libraries (the NASA Image and Video Library at images.nasa.gov and the Planetary Photojournal), and are in the public domain. Each caption names the mission and the team that made the image. "
           "Where an image is shown in false color or enhanced color, or combined from several exposures, the caption says so. The diagrams are the author’s own, drawn from the equations and values in the text.")

def mk(txt, bold_lead=None):
    p = newpara(tpl, txt)
    if bold_lead:
        first = [c for c in p if c.tag == W('r')][0]
        r = mkrun(bold_lead + ' ', rpr0); r.find(W('rPr')).insert(0, OxmlElement('w:b')); first.addprevious(r)
    return p

h1s = [e for e in kids if style(e) == 'Heading1']
parts = [(re.match(r'Part ([IVX]+):', text(h)).group(1), h) for h in h1s if re.match(r'Part [IVX]+:', text(h))]
assert len(parts) == 11, len(parts)
nxt = {id(h1s[i]): h1s[i + 1] for i in range(len(h1s) - 1)}
for num, h in parts:
    end = nxt[id(h)]
    end.addprevious(mk(FR[num], 'Further reading for Part ' + num + '.'))
# bibliography
bib = next(h for h in h1s if text(h).startswith('Bibliography'))
ent = []; e = bib.getnext()
while e is not None and style(e) != 'Heading1':
    if e.tag == W('p') and text(e).strip(): ent.append(e)
    e = e.getnext()
def key(t): return re.sub(r'[^a-z]', '', t.lower())
for line in NEWBIB:
    if any(line.split('.')[0] in text(x) and line.split('. ')[1][:20] in text(x) for x in ent): continue
    new = newpara(ent[0], line)
    nk = key(line)
    for x in ent:
        if key(text(x)) > nk: x.addprevious(new); ent.insert(ent.index(x), new); break
    else: ent[-1].addnext(new); ent.append(new)
# photo credits in Note on Sources
note = next(h for h in h1s if text(h).startswith('A Note on Sources'))
last = note; e = note.getnext()
while e is not None and style(e) != 'Heading1': last = e; e = e.getnext()
last.addnext(mk(CREDITS))
d.save(path); print('extras applied to', path)
