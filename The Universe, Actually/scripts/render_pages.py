import pymupdf, sys
doc = pymupdf.open(sys.argv[1])
want = [int(x) for x in sys.argv[3:]]
for n in want:
    pg = doc[n - 1]
    pix = pg.get_pixmap(matrix=pymupdf.Matrix(0.8, 0.8))
    pix.save('%s_p%d.png' % (sys.argv[2], n))
print(len(doc), 'pages')
# find pages containing text
import re
def find(s):
    return [i + 1 for i in range(len(doc)) if s in doc[i].get_text()][:5]
for s in ['Part I: The Universe', 'Cosmic Calendar', 'Feynman’s Ratchet', 'Table of Limits', 'A Puzzle in Meaningless']:
    print(s, find(s))
