"""REV18: insert new H3 sections into the thinner chapters, just before each chapter's 'Questions to Keep Asking' block.
Usage (from scripts/rev17):  python expand18.py ../../The_Universe_Actually__REV18.docx"""
import sys, os, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rev16'))
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
sys.path.insert(0, HERE)
import docx
from docx.oxml.ns import qn
from engine import newpara
EXP = {}
for mod in ('expand_a', 'expand_b'):
    EXP.update(__import__(mod).EXP)
W = lambda t: qn('w:' + t)
path = sys.argv[1]
d = docx.Document(path); body = d.element.body
text = lambda p: ''.join(t.text or '' for t in p.iter(W('t')))
def style(p):
    s = p.find(W('pPr')); s = s.find(W('pStyle')) if s is not None else None
    return s.get(W('val')) if s is not None else ''
kids = [e for e in body.iterchildren() if e.tag == W('p')]
tpl = next(p for p in kids if style(p) == '' and len(text(p)) > 150)
h3tpl = next(p for p in kids if style(p) == 'Heading3')
chap = {}
for e in kids:
    if style(e) == 'Heading2':
        m = re.match(r'(\d+)\. ', text(e))
        if m: chap[int(m.group(1))] = e
total = 0
for n, secs in EXP.items():
    e = chap[n].getnext()
    while e is not None and text(e).strip() != 'Questions to Keep Asking':
        assert style(e) != 'Heading2', ('no questions block in chapter', n)
        e = e.getnext()
    assert e is not None, n
    for head, paras in secs:
        e.addprevious(newpara(h3tpl, head))
        for t in paras:
            e.addprevious(newpara(tpl, t)); total += len(t.split())
print('sections added to chapters', sorted(EXP), 'words', total)
d.save(path)
