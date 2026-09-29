from pathlib import Path
import zipfile, re

docx = Path(r"D:\My Books for Amazon\Schrodingers_Paperwork\Schrodingers_Paperwork_BOOK_1_2.docx")
with zipfile.ZipFile(docx) as z:
    xml = z.read("word/document.xml").decode("utf-8")
paras = re.findall(r"<w:p\b[^>]*>.*?</w:p>", xml, re.DOTALL)
print("H1", sum(1 for p in paras if 'w:val="Heading1"' in p))
print("H2 leftover", sum(1 for p in paras if 'w:val="Heading2"' in p))
for p in paras:
    if 'w:val="Heading1"' in p and "Physics Notes" in p:
        t = "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p))
        print("ok", t[:60], "center", "center" in p, "hard", 'w:type="page"' in p)
        break
