import os as _os
HERE = _os.path.dirname(_os.path.abspath(__file__))
ROOT = _os.path.dirname(HERE)
import sys
from docx import Document

path = _os.path.join(ROOT, "Complete QED Course.docx")
doc = Document(path)
out = []
for p in doc.paragraphs:
    style = p.style.name if p.style is not None else ""
    if style.startswith("Heading") or style in ("Title",):
        t = p.text.strip()
        if t:
            out.append(f"{style}: {t}")
dest = _os.path.join(HERE, "_headings.txt")
open(dest, "w", encoding="utf-8").write("\n".join(out))
print("headings", len(out))
