from pathlib import Path
import zipfile
import re
from collections import Counter

docx = Path(r"D:\My Books for Amazon\Schrodingers_Paperwork\Schrodingers_Paperwork_BOOK_1_2.docx")
out = Path(r"D:\My Books for Amazon\Schrodingers_Paperwork\English\_phys_fmt.txt")

with zipfile.ZipFile(docx) as z:
    xml = z.read("word/document.xml").decode("utf-8")
    styles = z.read("word/styles.xml").decode("utf-8")

parts = []
for sid in ("Heading1", "Heading2", "Normal"):
    m = re.search(rf'<w:style[^>]*w:styleId="{sid}".*?</w:style>', styles, re.DOTALL)
    parts.append(f"=== STYLE {sid} ===")
    parts.append(m.group(0) if m else "MISSING")

# sample a novel chapter heading + first body para, and a physics notes heading + first body
def para_text(p):
    return "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p))

paras = re.findall(r"<w:p\b[^>]*>.*?</w:p>", xml, re.DOTALL)
parts.append("\n=== SAMPLE PARAS ===")
want = [
    "Chapter 1: The Form That Would Not Resolve",
    "There are, in the management",
    "Chapter 1: Physics Notes: Superposition",
    "In one breath",
    "Appendix: The Physics Lecture",
    "Further Reading",
    "Glossary",
]
for p in paras:
    t = para_text(p)
    for w in want:
        if t.startswith(w):
            ppr = re.search(r"<w:pPr>.*?</w:pPr>", p, re.DOTALL)
            rpr = re.search(r"<w:rPr>.*?</w:rPr>", p, re.DOTALL)
            parts.append(f"\n--- {t[:70]} ---")
            parts.append("PPR " + (ppr.group(0) if ppr else "none"))
            parts.append("RPR " + (rpr.group(0)[:400] if rpr else "none"))
            parts.append("hard_break " + str('w:type="page"' in p))
            parts.append("style " + (re.search(r'w:pStyle w:val="([^"]+)"', p).group(1) if re.search(r'w:pStyle w:val="([^"]+)"', p) else "none"))

# heading2 count and whether they have pbb
h2 = [p for p in paras if 'w:val="Heading2"' in p]
parts.append(f"\nHeading2 count={len(h2)}")
for p in h2:
    t = para_text(p)
    parts.append(f"H2 pbb={'pageBreakBefore' in p} hard={'w:type=\"page\"' in p} | {t[:80]}")

out.write_text("\n".join(parts), encoding="utf-8")
print("wrote", out)
