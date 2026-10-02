# -*- coding: utf-8 -*-
import re, zipfile
from pathlib import Path
root = Path(r"C:\Users\lomus\OneDrive\My Books for Amazon") / (
    "Lolly Wren" + chr(39) + "s Curious Science Adventures - SERIES"
)
src = root / "Book 2 - The Permitted Options" / "The_Permitted_Options_BOOK_2_DRAFT.docx"
xml = zipfile.ZipFile(src).read("word/document.xml").decode("utf-8")
pos = 0
token = re.compile(r"<w:p[ >]")
paras = []
while True:
    m = token.search(xml, pos)
    if not m:
        break
    a = m.start()
    b = xml.find("</w:p>", a)
    if b < 0:
        break
    b += 6
    t = "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", xml[a:b]))
    paras.append(" ".join(t.split()))
    pos = b
needles = ["plates moved", "attometre", "travell", "nucleus", "Chapter ", "chapters",
           "del-sentence", "Sunday before", "not through a form", "Coleman", "Nash, J",
           "Esaki, L", "Szekeres", "In one breath", "What this chapter", "Where the popular",
           "forehead", "how I know a day", "laughed", "God, no", "ninth of February",
           "Peterhead", "postcard"]
lines = ["paras %d" % len(paras)]
for n in needles:
    hits = [(i, t) for i, t in enumerate(paras) if n.lower() in t.lower()]
    lines.append("== %s %d" % (n, len(hits)))
    for i, t in hits[:6]:
        j = t.lower().find(n.lower())
        lines.append("%d %s" % (i, t[max(0, j-90):j+140]))
out = root / "Book 2 - The Permitted Options" / "bak" / "_b2_probe2.txt"
out.write_text("\n".join(lines), encoding="utf-8")
print("wrote", len(lines))
