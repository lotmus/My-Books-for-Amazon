# -*- coding: utf-8 -*-
import re, zipfile
from pathlib import Path
root = Path(r"D:\My Books for Amazon") / (
    "Lolly Wren" + chr(39) + "s Curious Science Adventures - SERIES"
)
src = root / "Book 2 - The Permitted Options" / "The_Permitted_Options_BOOK_2_DRAFT.docx"
xml = zipfile.ZipFile(src).read("word/document.xml").decode("utf-8")
needles = [
    "Going deeper (skip freely)",
    "two places at once",
    "To within instrument error",
    "to within instrument error",
    "instrument error",
    "the reason is Chapter Nine",
    "God, no",
    "The ninth of February",
    "did not go as travell",
    "atomic nucleus",
    "In one breath.",
    "arXiv:1207.3123. arXiv",
    "for the first time since the Annex",
    "into her hair",
    "He carried the far end",
    "G\u00f6del-sentence",
    "Ellen Prosper",
]
text = "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", xml))
lines = ["size %d chars %d" % (src.stat().st_size, len(text))]
for n in needles:
    lines.append("%d %s" % (text.count(n), n))
Path(root / "Book 2 - The Permitted Options" / "bak" / "_b2_probe.txt").write_text("\n".join(lines), encoding="utf-8")
print("\n".join(lines))
