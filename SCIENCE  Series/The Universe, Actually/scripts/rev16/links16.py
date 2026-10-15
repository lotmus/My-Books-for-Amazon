import re, copy
from urllib.parse import quote_plus
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from model16 import text, style
from engine import W, runs_of, base_rpr, mkrun
OL = lambda q: 'https://openlibrary.org/search?q=' + quote_plus(q)
WP = 'https://en.wikipedia.org/wiki/'
BIB = [  # (entry prefix, title as printed, url, in-text keys)
 ('Anthony, David W.', 'The Horse, the Wheel, and Language', WP+'The_Horse,_the_Wheel,_and_Language', ['The Horse, the Wheel, and Language']),
 ('Asimov, Isaac. A Short History of Biology', 'A Short History of Biology', OL('A Short History of Biology Asimov'), []),
 ('Asimov, Isaac. A Short History of Chemistry', 'A Short History of Chemistry', OL('A Short History of Chemistry Asimov'), []),
 ('Asimov, Isaac. Asimov’s New Guide', 'Asimov’s New Guide to Science', WP+'Asimov%27s_Guide_to_Science', []),
 ('Asimov, Isaac. The Human Brain', 'The Human Brain', OL('The Human Brain Asimov 1964'), []),
 ('Asimov, Isaac. Understanding Physics', 'Understanding Physics', WP+'Understanding_Physics', []),
 ('Axelrod', 'The Evolution of Cooperation', WP+'The_Evolution_of_Cooperation', ['The Evolution of Cooperation']),
 ('Barbour', 'The End of Time', WP+'The_End_of_Time_(book)', ['The End of Time']),
 ('Barrow, John D. The Origin', 'The Origin of the Universe', OL('The Origin of the Universe Barrow'), []),
 ('Barrow, John D., and Frank', 'The Anthropic Cosmological Principle', WP+'The_Anthropic_Cosmological_Principle', ['The Anthropic Cosmological Principle']),
 ('Carroll, Sean. Something', 'Something Deeply Hidden', WP+'Something_Deeply_Hidden', ['Something Deeply Hidden']),
 ('Carroll, Sean. The Big Picture', 'The Big Picture', WP+'The_Big_Picture_(Carroll_book)', ['The Big Picture']),
 ('Dawkins', 'The Blind Watchmaker', WP+'The_Blind_Watchmaker', ['The Blind Watchmaker']),
 ('Epstein', 'Relativity Visualized', OL('Relativity Visualized Epstein'), ['Relativity Visualized']),
 ('Everett', None, None, []),
 ('Feynman, Richard P. QED', 'QED: The Strange Theory of Light and Matter', WP+'QED:_The_Strange_Theory_of_Light_and_Matter', ['QED: The Strange Theory of Light and Matter']),
 ('Feynman, Richard P. Quantum Electrodynamics', 'Quantum Electrodynamics', OL('Quantum Electrodynamics Feynman 1961'), []),
 ('Feynman, Richard P., Robert', 'The Feynman Lectures on Physics', WP+'The_Feynman_Lectures_on_Physics', ['Feynman Lectures']),
 ('Graeber', 'The Dawn of Everything', WP+'The_Dawn_of_Everything', ['The Dawn of Everything']),
 ('Greene, Brian. The Fabric', 'The Fabric of the Cosmos', WP+'The_Fabric_of_the_Cosmos', ['The Fabric of the Cosmos']),
 ('Greene, Brian. Until', 'Until the End of Time', WP+'Until_the_End_of_Time_(book)', ['Until the End of Time']),
 ('Harari', 'Sapiens: A Brief History of Humankind', WP+'Sapiens:_A_Brief_History_of_Humankind', ['Sapiens']),
 ('Hawking, Stephen W. A Brief', 'A Brief History of Time', WP+'A_Brief_History_of_Time', ['A Brief History of Time']),
 ('Hawking, Stephen W., and Roger', 'The Nature of Space and Time', WP+'The_Nature_of_Space_and_Time', ['The Nature of Space and Time']),
 ('Hofstadter, Douglas R. Gödel', 'Gödel, Escher, Bach: An Eternal Golden Braid', WP+'G%C3%B6del,_Escher,_Bach', ['Gödel, Escher, Bach']),
 ('Hofstadter, Douglas R. I Am', 'I Am a Strange Loop', WP+'I_Am_a_Strange_Loop', ['I Am a Strange Loop']),
 ('Hofstadter, Douglas R. Metamagical', 'Metamagical Themas', WP+'Metamagical_Themas', ['Metamagical Themas']),
 ('Hofstadter, Douglas R., and Daniel', 'The Mind’s I', WP+'The_Mind%27s_I', ['The Mind’s I']),
 ('Hofstadter, Douglas R., and Emmanuel', 'Surfaces and Essences: Analogy as the Fuel and Fire of Thinking', OL('Surfaces and Essences Hofstadter Sander'), ['Surfaces and Essences']),
 ('Lewis-Williams', 'The Mind in the Cave', WP+'The_Mind_in_the_Cave', ['The Mind in the Cave']),
 ('McFadden, Johnjoe, and Jim', 'Life on the Edge: The Coming of Age of Quantum Biology', OL('Life on the Edge McFadden Al-Khalili'), ['Life on the Edge']),
 ('McFadden, Johnjoe. Quantum', 'Quantum Evolution', OL('Quantum Evolution McFadden'), []),
 ('Mead', 'Collective Electrodynamics: Quantum Foundations of Electromagnetism', OL('Collective Electrodynamics Mead'), ['Collective Electrodynamics']),
 ('Mithen', 'After the Ice: A Global Human History, 20,000–5000 BC', OL('After the Ice Mithen'), ['After the Ice']),
 ('Musiol, Lothar J. Foundations', 'Foundations of Electronics', 'https://www.amazon.com/s?k=' + quote_plus('Lothar J. Musiol Foundations of Electronics'), []),
 ('Musiol, Lothar J. Physics', 'Physics, Actually', 'https://www.amazon.com/s?k=' + quote_plus('Lothar J. Musiol Physics, Actually'), []),
 ('Musiol, Lothar J. Quantum', 'Quantum, Actually', 'https://www.amazon.com/s?k=' + quote_plus('Lothar J. Musiol Quantum, Actually'), []),
 ('Musiol, Lothar J. Science', 'Science Sparks', 'https://www.amazon.com/s?k=' + quote_plus('Lothar J. Musiol Science Sparks'), []),
 ('Penrose', 'Cycles of Time', WP+'Cycles_of_Time', ['Cycles of Time']),
 ('Sagan', 'Cosmos', WP+'Cosmos_(Sagan_book)', ['Cosmos']),
 ('Scarre', 'The Human Past: World Prehistory and the Development of Human Societies', OL('The Human Past Scarre'), ['The Human Past']),
 ('Schiller', 'Motion Mountain: The Adventure of Physics', None, ['Motion Mountain']),
 ('Tattersall', 'Masters of the Planet: The Search for Our Human Origins', OL('Masters of the Planet Tattersall'), ['Masters of the Planet']),
 ('Tipler', 'The Physics of Immortality', WP+'The_Physics_of_Immortality', ['The Physics of Immortality']),
 ('Tyson', 'Origins: Fourteen Billion Years of Cosmic Evolution', OL('Origins Fourteen Billion Years of Cosmic Evolution'), []),
 ('Watson, James D. The Double', 'The Double Helix', WP+'The_Double_Helix', []),
 ('Watson, James D., and Francis', None, None, []),
 ('Weinberg', 'The First Three Minutes', WP+'The_First_Three_Minutes', []),
 ('Wheeler, John Archibald, and Kenneth', 'Geons, Black Holes, and Quantum Foam', OL('Geons Black Holes and Quantum Foam Wheeler'), ['Geons, Black Holes, and Quantum Foam']),
 ('Wheeler, John Archibald. “Information', 'Complexity, Entropy and the Physics of Information', OL('Complexity Entropy and the Physics of Information Zurek'), []),
 ('Wragg Sykes', 'Kindred: Neanderthal Life, Love, Death and Art', WP+'Kindred:_Neanderthal_Life,_Love,_Death_and_Art', ['Kindred']),
 ('Particle Data Group', None, None, []),
]
def hyperlink(d, url=None, anchor=None, label='', rpr=None, italic=False):
    h = OxmlElement('w:hyperlink')
    if url: h.set(qn('r:id'), d.part.relate_to(url, RT.HYPERLINK, is_external=True))
    else: h.set(W('anchor'), anchor)
    rp = copy.deepcopy(rpr) if rpr is not None else OxmlElement('w:rPr')
    st = OxmlElement('w:rStyle'); st.set(W('val'), 'Hyperlink')
    rp.insert(0, st)
    for x in rp.findall(W('color')) + rp.findall(W('u')): rp.remove(x)
    c = OxmlElement('w:color'); c.set(W('val'), '0563C1'); rp.append(c)
    u = OxmlElement('w:u'); u.set(W('val'), 'single'); rp.append(u)
    h.append(mkrun(label, rp, it=italic)); return h
def wrap(d, p, sub_text, url=None, anchor=None, italic=None):
    """turn the first occurrence of sub_text (within one run) into a hyperlink"""
    for r in runs_of(p):
        if r.getparent().tag == W('hyperlink'): continue
        t = ''.join(x.text or '' for x in r.iter(W('t')))
        i = t.find(sub_text)
        if i < 0: continue
        rp = r.find(W('rPr')); isit = rp is not None and rp.find(W('i')) is not None
        rpr = base_rpr(r)
        before, after = t[:i], t[i+len(sub_text):]
        ts = list(r.iter(W('t'))); ts[0].text = before; [setattr(x, 'text', '') for x in ts[1:]]
        ts[0].set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
        h = hyperlink(d, url, anchor, sub_text, rpr, italic if italic is not None else isit)
        r.addnext(h)
        if after:
            r2 = copy.deepcopy(r); t2 = list(r2.iter(W('t'))); t2[0].text = after; [setattr(x, 'text', '') for x in t2[1:]]
            h.addnext(r2)
        return True
    return False
def bookmark(p, name, bid):
    s = OxmlElement('w:bookmarkStart'); s.set(W('id'), str(bid)); s.set(W('name'), name)
    e = OxmlElement('w:bookmarkEnd'); e.set(W('id'), str(bid))
    pPr = p.find(W('pPr'))
    if pPr is not None: pPr.addnext(s)
    else: p.insert(0, s)
    p.append(e)
def run(d, body):
    ps = [e for e in body.iterchildren() if e.tag == W('p')]
    H = lambda t: next(i for i, p in enumerate(ps) if style(p) == 'Heading1' and text(p) == t)
    b0, r0, a0 = H('Bibliography'), H('External Resources'), H('About the Author')
    bib = [p for p in ps[b0+1:r0] if text(p).strip()]
    keys = {}
    for k, (pre, title, url, intext) in enumerate(BIB):
        p = next(p for p in bib if text(p).startswith(pre))
        bookmark(p, 'bib_%d' % (k+1), 9500 + k)
        if title and url:
            assert wrap(d, p, title, url=url, italic=True), title
        elif title:   # title present, link elsewhere already (Motion Mountain): italicize only via link to site
            wrap(d, p, title, url='https://www.motionmountain.net/', italic=True)
        for key in intext: keys[key] = 'bib_%d' % (k+1)
    print('bibliography entries linked', len(bib))
    # in-text citations: first mention per chapter -> bibliography entry
    intro = H('Introduction: Why Any of This Matters'); epi = H('Epilogue: Actually')
    seen = set(); chap = 'intro'; nlinks = 0
    for p in ps[intro:epi]:
        if style(p) == 'Heading2': chap = text(p); continue
        if style(p).startswith('Heading'): continue
        t = text(p)
        for key, bm in sorted(keys.items(), key=lambda x: -len(x[0])):
            if (chap, key) in seen or key not in t: continue
            if key == 'Cosmos' and '*' not in t and 'television' not in t and 'Sagan' not in t: continue
            if key in ('Sapiens', 'The End of Time', 'The Big Picture', 'After the Ice', 'Kindred', 'Life on the Edge', 'The Human Past'):
                # only italic (title) uses
                ok = False
                for r in runs_of(p):
                    rp = r.find(W('rPr'))
                    if rp is not None and rp.find(W('i')) is not None and key in ''.join(x.text or '' for x in r.iter(W('t'))): ok = True
                if not ok and not (key == 'The End of Time' and 'Barbour' in t): continue
            if wrap(d, p, key, anchor=bm): seen.add((chap, key)); nlinks += 1
    print('in-text citation links', nlinks)
    # External Resources: dedupe and regroup by part
    res = [p for p in ps[r0+1:a0]]
    rels = d.part.rels
    links = {}
    for p in res:
        for h in p.iter(W('hyperlink')):
            rid = h.get(qn('r:id'))
            if rid: links.setdefault(rels[rid].target_ref, text(h))
    FIXURL = {'https://solarsystem.nasa.gov/': 'https://science.nasa.gov/solar-system/', 'https://exoplanets.nasa.gov/': 'https://science.nasa.gov/exoplanets/', 'https://qiskit.org/': 'https://www.ibm.com/quantum/qiskit'}
    def lab(u):
        l = links[u]
        if l == 'Wikipedia':
            l = u.rsplit('/', 1)[1].replace('_', ' ').replace('%27', '’').replace('%C3%B6', 'ö')
        l = l.replace('Wikipedia: ', '').replace("'", '’')
        return l[0].upper() + l[1:]
    WPu = lambda s: 'https://en.wikipedia.org/wiki/' + s
    GROUPS = [
     ('Part I · Motion and Energy', [WPu('Newton%27s_laws_of_motion'), WPu('Principle_of_least_action'), WPu('Laws_of_thermodynamics'), WPu('Statistical_mechanics'), WPu('Entropy'), WPu('Chaos_theory'), WPu('Maxwell%27s_equations'), WPu('Optics')]),
     ('Part II · The Quantum World', [WPu('Quantum_mechanics'), 'https://www.youtube.com/watch?v=2h1E3YJMKfA', 'https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2013/', WPu('Superconductivity'), WPu('Topological_insulator'), WPu('Quantum_information'), WPu('Quantum_computing'), 'https://www.youtube.com/watch?v=QuR969uMICM', 'https://qiskit.org/']),
     ('Part III · Particles, Nuclei and Atoms', [WPu('Standard_Model'), 'https://home.cern/science/physics/standard-model', WPu('Higgs_boson'), 'https://home.cern/science/physics/higgs-boson', WPu('Neutrino_oscillation'), WPu('Nuclear_physics'), WPu('Nuclear_fusion'), WPu('Periodic_table'), WPu('Chemical_bond'), WPu('Materials_science')]),
     ('Part IV · Space, Time and Gravity', [WPu('Special_relativity'), WPu('General_relativity'), 'https://www.einstein-online.info/en/', WPu('Gravitational_wave'), 'https://www.ligo.caltech.edu/', WPu('Black_hole'), WPu('Black_hole_information_paradox')]),
     ('Part V · Planets, Stars and Galaxies', [WPu('Solar_System'), 'https://solarsystem.nasa.gov/', WPu('Exoplanet'), 'https://exoplanets.nasa.gov/', WPu('Stellar_evolution'), WPu('Galaxy')]),
     ('Part VI · The Universe as a Whole', [WPu('Big_Bang'), 'https://science.nasa.gov/universe/overview/', WPu('Inflation_(cosmology)'), WPu('Arrow_of_time')]),
     ('Part VII · Life', [WPu('Evolution'), 'https://evolution.berkeley.edu/', WPu('DNA'), WPu('CRISPR'), WPu('Great_Oxidation_Event'), WPu('Cambrian_explosion'), WPu('Extinction_event'), WPu('Astrobiology'), 'https://astrobiology.nasa.gov/', WPu('Habitable_zone'), WPu('Human_evolution')]),
     ('Part VIII · The Human Body and Mind', [WPu('Human_microbiome'), WPu('Neuroscience'), WPu('Consciousness'), WPu('Hard_problem_of_consciousness')]),
     ('Part IX · Earth, the Living Planet', [WPu('Climate_change'), 'https://www.ipcc.ch/', WPu('Ecology')]),
     ('Part X · Technology', [WPu('Information_theory'), WPu('Machine_learning'), 'https://www.youtube.com/watch?v=aircAruvnKk']),
     ('Part XI · How We Know', [WPu('G%C3%B6del%27s_incompleteness_theorems')]),
    ]
    used = [u for g in GROUPS for u in g[1]]
    missing = set(links) - set(used); assert not missing, missing
    intro_p = res[0]; tpl = next(p for p in res[1:] if p.find(W('hyperlink')) is not None)
    review = next(p for p in res if text(p).startswith('If this book gave you something'))
    ts = list(intro_p.iter(W('t'))); ts[0].text = 'The links below point to reliable outside material for the main subjects of each part. They are starting points, not endorsements of every claim on the pages they lead to. Entries marked with a source name lead to that organization; the others lead to the Wikipedia article of that name.'; [setattr(x, 'text', '') for x in ts[1:]]
    rpr0 = base_rpr(runs_of(tpl)[0])
    for p in res:
        if p is not intro_p and p is not review: body.remove(p)
    for gname, urls in GROUPS:
        p = copy.deepcopy(tpl)
        for ch in list(p):
            if ch.tag != W('pPr'): p.remove(ch)
        b = copy.deepcopy(rpr0); b.append(OxmlElement('w:b'))
        p.append(mkrun(gname + ': ', b))
        for i, u in enumerate(urls):
            if i: p.append(mkrun(' · ', rpr0))
            p.append(hyperlink(d, FIXURL.get(u, u), None, lab(u), rpr0))
        review.addprevious(p)
    print('external resources', len(used), 'links in', len(GROUPS), 'groups')
