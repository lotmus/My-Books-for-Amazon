import re
from model16 import text, style
from engine import W
FIX = [(r'(?i)\b(\w*?)(quanti|polymeri|authori|civili|compartmentali|extremi|immuni|minerali|oxidi|pasteuri|personali|randomi|sterili|sensiti|synchroni|symmetri|axiomati|formali|diagonali|regulari|parameteri|factori|speciali|encephali|fertili|coloni|ideali|locali|renormali|Renormali|magneti|polari|circulari|thermali|catalogi|parametri|crystalli|neutrali|standardi|minimi|maximi|stabili|organi|reali|recogni|ioni)s(e|ed|es|ing|ation|ations|er|ers)\b', r'\1\2z\3'), (r'\bcenterd\b', 'centered'), (r'\blitres\b', 'liters'), (r'\b(f|F)ibre', r'\1iber'), (r'\b(dis)?favour', r'\1favor'.replace('\\1','\\1')), (r'\b(c|C)olour', r'\1olor'), (r'\b(b|B)ehaviour', r'\1ehavior'), (r'\b(n|N)eighbour', r'\1eighbor'), (r'\b(h|H)onour', r'\1onor'), (r'\b(r|R)umour', r'\1umor'), (r'\b(v|V)apour', r'\1apor'), (r'\b(l|L)abour', r'\1abor'), (r'\b(h|H)arbour', r'\1arbor'), (r'\btumour', 'tumor'), (r'(p|P)alaeo', r'\1aleo'), (r'\b(d|D)efence', r'\1efense'), (r'(k|K)ilotonnes', r'\1ilotons'), (r'(m|M)egatonnes', r'\1egatons'), (r'(d|D)iarrhoea', r'\1iarrhea'), (r'(p|P)aralys(ed|ing)', r'\1aralyz\2'), (r'\boestrogen', 'estrogen'), (r'\bOestrogen', 'Estrogen'), (r'(h|H)aemo', r'\1emo'), (r'(a|A)naemi', r'\1nemi'), (r'\boedema', 'edema'), (r'\b(m|M)ollusc(s?)\b', r'\1ollusk\2'), (r'(s|S)ulph', r'\1ulf'), (r'(c|C)olonis', r'\1oloniz'), (r'desensitis', 'desensitiz'), (r'(c|C)entred', r'\1entered'), (r'(c|C)entre', r'\1enter'), (r'(i|I)metre', r'\1meter'), (r'(o|O)metre', r'\1meter'), (r'\bmetres?\b', lambda m: m.group(0).replace('metre','meter')), (r'\b(c|C)atalys(e|ed|es|ing)\b', r'\1ataly z\2'.replace(' ','')), (r'\bparalysed\b', 'paralyzed'), (r'\b(f|F)lavour', r'\1lavor'), (r'\b(t|T)unnelling', r'\1unneling'), (r'\bfunnelled', 'funneled'), (r'\bspiralling', 'spiraling'), (r'\banalogue', 'analog'), (r'\banalys(e|ed|ing)\b', r'analyz\1'), (r'\bAnalys(e|ed|ing)\b', r'Analyz\1'), (r'\blitre\b', 'liter'), (r'\bfor ever\b', 'forever'), (r'\bReionisation\b', 'Reionization'), (r'\bquantisation\b', 'quantization'),
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
