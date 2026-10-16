import sys
from docx import Document
d=Document(sys.argv[1]); ps=d.paragraphs
for i,pp in enumerate(ps):
    if not pp.text.strip() and not pp._p.xpath('.//w:drawing'):
        print(i,pp.style.name,'| prev:',ps[i-1].text[:40],'| next:',ps[i+1].text[:40])
