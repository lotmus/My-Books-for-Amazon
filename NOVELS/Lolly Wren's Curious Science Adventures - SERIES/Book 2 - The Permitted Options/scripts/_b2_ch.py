# -*- coding: utf-8 -*-
import re, zipfile
from pathlib import Path
root = Path(r"D:\My Books for Amazon") / (
    "Lolly Wren" + chr(39) + "s Curious Science Adventures - SERIES"
)
src = root / "Book 2 - The Permitted Options" / "The_Permitted_Options_BOOK_2_DRAFT.docx"
xml = zipfile.ZipFile(src).read("word/document.xml").decode("utf-8")
pos = 0
token = re.compile(r"<w:p[ >]")
lines = []
i = 0
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
    style = ""
    sm = re.search(r'<w:pStyle w:val="([^"]+)"', chunk)
    if sm:
        style = sm.group(1)
    t = " ".join("".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", chunk)).split())
    if t.strip() == "The Lectures":
        break
    if not style.startswith("Heading"):
        if re.search(r"Chapter\s+[A-Z0-9]", t) or re.search(r"\bchapters\b", t, re.I):
            mm = re.search(r"Chapter\s+[A-Z0-9]|\bchapters\b", t, re.I)
            lines.append("%d %s" % (i, t[max(0, mm.start()-70):mm.end()+90]))
    i += 1
    pos = b
out = root / "Book 2 - The Permitted Options" / "bak" / "_b2_ch.txt"
out.write_text("\n".join(lines), encoding="utf-8")
print(len(lines))
