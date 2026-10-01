import sys
from docx import Document

path = r"C:\Users\lomus\OneDrive\My Books for Amazon\Science Books\QED Course\Complete QED Course.docx"
doc = Document(path)
out = []
for p in doc.paragraphs:
    style = p.style.name if p.style is not None else ""
    if style.startswith("Heading") or style in ("Title",):
        t = p.text.strip()
        if t:
            out.append(f"{style}: {t}")
dest = r"C:\Users\lomus\OneDrive\My Books for Amazon\Science Books\QED Course\_build\_headings.txt"
open(dest, "w", encoding="utf-8").write("\n".join(out))
print("headings", len(out))
