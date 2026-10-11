"""REV15 typography pass, run after tools/kindle_links.py: curly apostrophes, prime marks, true minus signs.
Every spaced hyphen left in this book sits in an equation, so " - " becomes " \u2212 "."""
import sys, re, docx
from docx.oxml.ns import qn
d = docx.Document(sys.argv[1]); n = [0, 0, 0]
for t in d.element.body.iter(qn('w:t')):
    s = t.text or ''; o = s
    s, k = re.subn(r"(?<=[A-Za-z\u00C0-\u024F])'(?=[A-Za-z])", '\u2019', s); n[0] += k
    s, k = re.subn(r"(?<=[\u0370-\u03FF])'", '\u2032', s); n[1] += k
    s, k = re.subn(r'(?:(?<=\S)|^) - (?=\S)', ' \u2212 ', s); n[2] += k
    s, k = re.subn(r'(?<=\S) - $', ' \u2212 ', s); n[2] += k
    s, k = re.subn(r'"(RNA world)"', '\u201c\\1\u201d', s); n[0] += k
    if s != o: t.text = s
d.save(sys.argv[2]); print('apostrophes %d, primes %d, minus signs %d' % tuple(n))
