import re
from model16 import text, style
from engine import W
FIX = [(r'(?i)\b(\w*?)(quanti|polymeri|authori|civili|compartmentali|extremi|immuni|minerali|oxidi|pasteuri|personali|randomi|sterili|sensiti|synchroni|symmetri|axiomati|formali|diagonali|regulari|parameteri|factori|speciali|encephali|fertili|coloni|ideali|locali|renormali|Renormali|magneti|polari|circulari|thermali|catalogi|parametri|crystalli|neutrali|standardi|minimi|maximi|stabili|organi|reali|recogni|ioni)s(e|ed|es|ing|ation|ations|er|ers)\b', r'\1\2z\3'), (r'\bcenterd\b', 'centered'), (r'\blitres\b', 'liters'), (r'\b(c|C)atalys(e|ed|es|ing)\b', r'\1ataly z\2'.replace(' ','')), (r'\bparalysed\b', 'paralyzed'), (r'\b(f|F)lavour', r'\1lavor'), (r'\b(t|T)unnelling', r'\1unneling'), (r'\bfunnelled', 'funneled'), (r'\bspiralling', 'spiraling'), (r'\banalogue', 'analog'), (r'\banalys(e|ed|ing)\b', r'analyz\1'), (r'\bAnalys(e|ed|ing)\b', r'Analyz\1'), (r'\blitre\b', 'liter'), (r'\bfor ever\b', 'forever'), (r'\bReionisation\b', 'Reionization'), (r'\bquantisation\b', 'quantization'),
       (r'\bcircularisation\b', 'circularization'), (r'\blocalisation\b', 'localization'), (r'\bmagnetised\b', 'magnetized'), (r'\bTravelled\b', 'Traveled'), (r'\btravelled\b', 'traveled'),
       (r'\bDefence\b', 'Defense'), (r'\bSignalling\b', 'Signaling'), (r'\bsignalling\b', 'signaling')]
def run(d, body):
    ps = [e for e in body.iterchildren() if e.tag == W('p')]
    stop = next(i for i, p in enumerate(ps) if style(p) == 'Heading1' and text(p) == 'Bibliography')
    n = 0
    for p in ps[:stop]:
        for t in p.iter(W('t')):
            s = t.text or ''; o = s
            for a, b in FIX: s = re.sub(a, b, s)
            if s != o: t.text = s; n += 1
    print('typo runs', n)
    ps = [e for e in body.iterchildren() if e.tag == W('p')]
    a = next(i for i, p in enumerate(ps) if style(p) == 'Heading1' and text(p).startswith('Introduction'))
    b = next(i for i, p in enumerate(ps) if style(p) == 'Heading1' and text(p).startswith('Epilogue'))
    k = 0
    for p in ps[a:b]:
        if not text(p).strip() and not p.findall('.//'+W('drawing')) and not p.findall('.//'+W('bookmarkStart')) and not p.findall('.//'+W('br')) and not p.findall('.//'+W('pageBreakBefore')):
            body.remove(p); k += 1
    print('empty paras removed', k)
    import links16; links16.run(d, body)
