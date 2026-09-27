from __future__ import annotations

import re
import zipfile
from pathlib import Path

DOCX = Path(r"D:\My Books for Amazon\Schrodingers_Paperwork\Schrodingers_Paperwork_BOOK_1_2.docx")

with zipfile.ZipFile(DOCX) as z:
    xml = z.read("word/document.xml").decode("utf-8")

bookmarks = set(re.findall(r'<w:bookmarkStart[^>]*w:name="([^"]+)"', xml))
print("bookmarks", len(bookmarks))
print(sorted(bookmarks)[:40])

anchors = re.findall(r'<w:hyperlink[^>]*w:anchor="([^"]+)"', xml)
print("toc_anchors", len(anchors), "unique", len(set(anchors)))
missing = [a for a in dict.fromkeys(anchors) if a not in bookmarks]
print("missing_anchors", missing)

print("oMath", xml.count("<m:oMath"))
print("w:drawing in eq?", False)
print("lang", re.findall(r'<w:lang [^/]+/>', xml)[:3])
print("numPr in TOC-ish", xml.count("<w:numPr"))

# sample hyperlink
m = re.search(r"<w:hyperlink[^>]*>.*?</w:hyperlink>", xml, re.DOTALL)
print("sample_hyper", (m.group(0)[:400] if m else None))
