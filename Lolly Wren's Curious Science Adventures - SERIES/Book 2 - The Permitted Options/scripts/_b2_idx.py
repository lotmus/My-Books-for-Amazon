# -*- coding: utf-8 -*-
import html, re, zipfile
from pathlib import Path

root = Path(r"D:\My Books for Amazon") / (
    "Lolly Wren" + chr(39) + "s Curious Science Adventures - SERIES"
)
src = root / "Book 2 - The Permitted Options" / "The_Permitted_Options_BOOK_2_DRAFT.docx"
xml = zipfile.ZipFile(src).read("word/document.xml").decode("utf-8")
token = re.compile(r"<w:p[ >]")
paras = []
pos = 0
while True:
    m = token.search(xml, pos)
    if not m:
        break
    a = m.start()
    b = xml.find("</w:p>", a)
    if b < 0:
        break
    b += 6
    chunk = xml[a:b]
    sm = re.search(r'<w:pStyle w:val="([^"]+)"', chunk)
    raw = "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", chunk))
    text = " ".join(html.unescape(raw).split())
    paras.append((sm.group(1) if sm else "", text, chunk))
    pos = b

print("paras", len(paras))
print("bookmarks", xml.count("<w:bookmarkStart"))
lectures = next(i for i, (_, t, _) in enumerate(paras) if t == "The Lectures")
story = paras[:lectures]
print("story chapters word", sum(1 for _, t, _ in story if "chapters" in t.lower()))
print("story Chapter capital", sum(1 for s, t, _ in story if s != "Heading2" and re.search(r"Chapter [A-Z]", t)))
need = [
    "not be through a form",
    "There was no page to send",
    "Coleman, S.",
    "Esaki, L.",
    "Nash, J.",
    "Szekeres, G.",
    "The plates moved",
    "Q.E.D.",
    "The Permitted Options ends here",
    "She stayed on her side of the doorway",
    "He has not asked me to call either of those things by a larger name",
    "who had said almost nothing throughout",
    "By eleven Lolly had stopped trying to take him down verbatim",
    "She did not ask a second question",
]
absent = [
    "In one breath.",
    "Where the popular version goes wrong.",
    "Going deeper (skip freely)",
    "What this chapter was actually showing you.",
    "into her hair",
    "He is how I know a day is real",
    "G\u00f6del-sentence",
    "for the first time since the Annex",
    "to within instrument error",
    "two places at once",
]
joined = "\n".join(t for _, t, _ in paras)
for s in need:
    print("NEED", s, joined.count(s))
for s in absent:
    print("ABSENT", s, joined.count(s))
print("--- headings ---")
for i, (s, t, _) in enumerate(paras):
    if s == "Heading2":
        print(i, t)
print("--- before going deeper ---")
for i, (s, t, _) in enumerate(paras):
    if s == "Heading3" and t == "Going deeper":
        prev = paras[i - 1][1]
        print(i, prev[:180])
