# -*- coding: utf-8 -*-
"""Pull concrete facts for the critical review. Writes UTF-8."""
from docx import Document
from docx.oxml.ns import qn

path = r"C:\Users\lomus\OneDrive\My Books for Amazon\Science Books\QED Course\Complete QED Course.docx"
doc = Document(path)
paras = doc.paragraphs
lines = []
lines.append("PARAS %d TABLES %d SECTIONS %d" % (len(paras), len(doc.tables), len(doc.sections)))
sec = doc.sections[0]
lines.append("PAGE %s x %s" % (sec.page_width, sec.page_height))
lines.append("MARGINS L%s R%s T%s B%s" % (sec.left_margin, sec.right_margin, sec.top_margin, sec.bottom_margin))

# first 40 non-empty paras
n = 0
lines.append("--- OPENING ---")
for p in paras:
    t = p.text.strip()
    if not t:
        continue
    lines.append("[%s] %s" % (p.style.name, t[:220]))
    n += 1
    if n >= 25:
        break

# hyperlinks
body = doc.element.body
links = body.findall(".//" + qn("w:hyperlink"))
lines.append("HYPERLINKS %d" % len(links))

# lesson 68 sample
lines.append("--- LESSON 68 ---")
grab = False
count = 0
for p in paras:
    t = p.text.strip()
    if t.startswith("Lesson 68 "):
        grab = True
    if grab:
        if t:
            lines.append(t[:300])
            count += 1
        if count >= 18:
            break

lines.append("--- CAPSTONE ---")
grab = False
count = 0
for p in paras:
    t = p.text.strip()
    if t == "Course capstone":
        grab = True
    if grab:
        if t:
            lines.append(t[:400])
            count += 1
        if count >= 8:
            break

# words
words = 0
for p in paras:
    words += len(p.text.split())
lines.append("WORDS %d" % words)

# style histogram for headings
from collections import Counter
c = Counter(p.style.name for p in paras)
lines.append("--- STYLES ---")
for name, k in c.most_common(15):
    lines.append("%s %d" % (name, k))

dest = r"C:\Users\lomus\OneDrive\My Books for Amazon\Science Books\QED Course\_build\_review_facts.txt"
open(dest, "w", encoding="utf-8").write("\n".join(lines))
print("wrote", dest)
