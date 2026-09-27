from pathlib import Path
import zipfile
import re

docx = Path(
    r"D:\My Books for Amazon\Schrodingers_Paperwork\English"
    r"\Schrodingers_Paperwork_BOOK_1_2_BEFORE_FIGURE_FIX_BACKUP.docx"
)
out = Path(r"D:\My Books for Amazon\Schrodingers_Paperwork\English\_breaks.txt")

NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
}

with zipfile.ZipFile(docx) as z:
    xml = z.read("word/document.xml").decode("utf-8")
    styles = z.read("word/styles.xml").decode("utf-8")

parts = []
# Heading1 style definition
m = re.search(r'<w:style[^>]*w:styleId="Heading1".*?</w:style>', styles, re.DOTALL)
parts.append("=== Heading1 style ===")
parts.append(m.group(0)[:2500] if m else "NOT FOUND")

# all Heading1 paragraphs: style + pageBreakBefore + text
heads = re.findall(
    r"<w:p\b[^>]*>.*?</w:p>",
    xml,
    re.DOTALL,
)
parts.append("\n=== Heading-styled paragraphs ===")
count_h1 = 0
count_pbb = 0
count_hard = xml.count('w:type="page"')
for p in heads:
    if 'w:val="Heading1"' not in p and 'w:val="Heading2"' not in p:
        continue
    texts = re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p)
    title = "".join(texts)[:80]
    style = "H1" if 'w:val="Heading1"' in p else "H2"
    pbb = "pageBreakBefore" in p
    hard = 'w:type="page"' in p
    if style == "H1":
        count_h1 += 1
        if pbb:
            count_pbb += 1
    parts.append(f"{style} pbb={pbb} hard={hard} | {title}")

parts.append(f"\nHeading1 count={count_h1}")
parts.append(f"Heading1 with pageBreakBefore={count_pbb}")
parts.append(f"hard page-break runs in document={count_hard}")
parts.append(f"pageBreakBefore total occurrences={xml.count('pageBreakBefore')}")

# first few chapter-like titles that are NOT heading
parts.append("\n=== lines that look like chapters but may not be Heading1 ===")
for p in heads:
    texts = re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p)
    title = "".join(texts)
    if re.match(r"^(Chapter |Prologue|Epilogue|Appendix|How to Read|Physics Prologue|Cast of)", title):
        is_h = 'w:val="Heading1"' in p or 'w:val="Heading2"' in p
        pbb = "pageBreakBefore" in p
        if not is_h:
            parts.append(f"NOT HEADING pbb={pbb} | {title[:90]}")

out.write_text("\n".join(parts), encoding="utf-8")
print("wrote", out)
