from __future__ import annotations

import re
import zipfile
from pathlib import Path

DOCX = Path(r"D:\My Books for Amazon\Schrodingers_Paperwork\Schrodingers_Paperwork_BOOK_1_2.docx")


def para_text(p: str) -> str:
    return "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p))


def style_of(p: str) -> str:
    m = re.search(r'<w:pStyle w:val="([^"]+)"', p)
    return m.group(1) if m else "Normal"


with zipfile.ZipFile(DOCX) as z:
    xml = z.read("word/document.xml").decode("utf-8")
    rels = z.read("word/_rels/document.xml.rels").decode("utf-8")
    print("hyperlink rels", len(re.findall(r"hyperlink", rels)))
    print(rels[:1500])

paras = re.findall(r"<w:p\b[^>]*>.*?</w:p>", xml, flags=re.DOTALL)
print("\n=== FIRST 80 PARAS ===")
for i, p in enumerate(paras[:80]):
    t = para_text(p).strip()
    if not t and style_of(p) == "Normal" and "<w:drawing" not in p:
        continue
    extra = []
    if "<w:hyperlink" in p:
        extra.append("HYPER")
    if "<w:drawing" in p:
        extra.append("IMG")
    if style_of(p) != "Normal":
        extra.append(style_of(p))
    print(f"{i:4d} {' '.join(extra):12s} {t[:100]}")

print("\n=== HEADING3 ===")
for i, p in enumerate(paras):
    if style_of(p) == "Heading3":
        print(i, para_text(p)[:120])

print("\n=== CONTENTS BLOCK ===")
for i, p in enumerate(paras):
    if 28 <= i <= 57:
        print(f"{i:4d} {style_of(p):12s} hyper={('<w:hyperlink' in p)} {para_text(p)[:90]}")
