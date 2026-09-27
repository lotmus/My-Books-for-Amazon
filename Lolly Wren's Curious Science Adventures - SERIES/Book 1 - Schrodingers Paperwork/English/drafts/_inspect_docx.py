from pathlib import Path
import zipfile
import re

docx = Path(r"D:\My Books for Amazon\Schrodingers_Paperwork\Schrodingers_Paperwork_BOOK_1_2.docx")
out = Path(r"D:\My Books for Amazon\Schrodingers_Paperwork\English\_xml_snips.txt")

with zipfile.ZipFile(docx) as z:
    xml = z.read("word/document.xml").decode("utf-8")
    rels = z.read("word/_rels/document.xml.rels").decode("utf-8")
    ctypes = z.read("[Content_Types].xml").decode("utf-8")

parts = ["RELS:", rels, "\nCONTENT TYPES:\n", ctypes]
for needle in [
    "String Theory and M-Theory",
    "The injunction itself was granted",
    "They got eleven weeks",
]:
    i = xml.find(needle)
    parts.append(f"\n==== {needle} @ {i} ====")
    if i >= 0:
        parts.append(xml[max(0, i - 400) : i + 500])

idx = xml.rfind("<w:drawing")
parts.append(f"\n==== last drawing @ {idx} ====")
if idx >= 0:
    parts.append(xml[idx : idx + 3500])
parts.append(f"\ndrawing count={xml.count('<w:drawing')}")
descs = re.findall(r'descr="([^"]*)"', xml)
parts.append("ALTS:")
parts.extend(" - " + d for d in descs)
out.write_text("\n".join(parts), encoding="utf-8")
print("wrote", out, "xml_len", len(xml))
