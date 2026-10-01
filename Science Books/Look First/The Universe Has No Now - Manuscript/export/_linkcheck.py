import zipfile
from xml.etree import ElementTree as ET
from pathlib import Path

docx = Path(r"export\The_Universe_Has_No_Now.docx")
ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
with zipfile.ZipFile(docx) as z:
    root = ET.fromstring(z.read("word/document.xml"))
bookmarks = {b.get("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}name") for b in root.iter("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}bookmarkStart")}
anchors = []
for h in root.iter("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}hyperlink"):
    a = h.get("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}anchor")
    if a:
        anchors.append(a)
missing = sorted({a for a in anchors if a not in bookmarks})
pg = root.find(".//w:sectPr/w:pgSz", ns)
out = Path(r"export\_linkcheck.txt")
lines = [
    f"hyperlinks {len(anchors)}",
    f"unique_anchors {len(set(anchors))}",
    f"bookmarks {len(bookmarks)}",
    f"missing {len(missing)}",
    f"missing_list {missing[:20]}",
    f"pgSz {pg.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}w') if pg is not None else None} x {pg.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}h') if pg is not None else None}",
]
out.write_text("\n".join(lines), encoding="utf-8")
