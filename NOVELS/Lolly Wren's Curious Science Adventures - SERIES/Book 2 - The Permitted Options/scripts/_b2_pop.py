# -*- coding: utf-8 -*-
import html
import re, zipfile
from pathlib import Path
import xml.etree.ElementTree as ET

root = Path(r"D:\My Books for Amazon") / (
    "Lolly Wren" + chr(39) + "s Curious Science Adventures - SERIES"
)
book = root / "Book 2 - The Permitted Options"
src = book / "The_Permitted_Options_BOOK_2_DRAFT.docx"
bak = book / "bak" / "The_Permitted_Options_BOOK_2_DRAFT.before-critical-review.docx"

def paras(path):
    xml = zipfile.ZipFile(path).read("word/document.xml").decode("utf-8")
    out = []
    pos = 0
    token = re.compile(r"<w:p[ >]")
    while True:
        m = token.search(xml, pos)
        if not m:
            break
        a = m.start()
        b = xml.find("</w:p>", a)
        if b < 0:
            break
        b += 6
        raw = "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", xml[a:b]))
        t = " ".join(html.unescape(raw).split())
        out.append(t)
        pos = b
    return out

label = "Where the popular version goes wrong. "
sents = []
for t in paras(bak):
    if t.startswith(label):
        rest = t[len(label):]
        dot = rest.find(". ")
        sent = rest[:dot + 1] if dot > 0 else rest
        sents.append(sent)
print("sents", len(sents))
if len(sents) != 16:
    raise SystemExit("sent count")

xml = zipfile.ZipFile(src).read("word/document.xml").decode("utf-8")
bm0 = xml.count("<w:bookmarkStart")
parts = []
pos = 0
token = re.compile(r"<w:p[ >]")
while True:
    m = token.search(xml, pos)
    if not m:
        if xml[pos:]:
            parts.append(xml[pos:])
        break
    a = m.start()
    if a > pos:
        parts.append(xml[pos:a])
    b = xml.find("</w:p>", a)
    b += 6
    parts.append(xml[a:b])
    pos = b

def plain(p):
    return "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p))

def body_p(text):
    text = (text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
    return ('<w:p><w:pPr><w:pStyle w:val="BodyText"/></w:pPr>'
            '<w:r><w:t xml:space="preserve">%s</w:t></w:r></w:p>' % text)

def style_of(p):
    m = re.search(r'<w:pStyle w:val="([^"]+)"', p)
    return m.group(1) if m else ""

idxs = [i for i, p in enumerate(parts) if p.startswith("<w:p") and style_of(p) == "Heading3" and plain(p).strip() == "Going deeper"]
if len(idxs) != 16:
    raise SystemExit("deeper %s" % len(idxs))
for n, i in reversed(list(enumerate(idxs))):
    parts[i:i] = [body_p(sents[n])]

doc = "".join(parts)
if doc.count("<w:bookmarkStart") != bm0:
    raise SystemExit("bookmarks")
ET.fromstring(doc.encode("utf-8"))
if doc.count("Where the popular version goes wrong.") != 0:
    raise SystemExit("label back")
out = src.with_suffix(".tmp.docx")
zin = zipfile.ZipFile(src, "r")
with zipfile.ZipFile(out, "w") as zout:
    for item in zin.infolist():
        data = doc.encode("utf-8") if item.filename == "word/document.xml" else zin.read(item.filename)
        zout.writestr(item, data)
zin.close()
out.replace(src)
print("popular sentences", len(idxs))
