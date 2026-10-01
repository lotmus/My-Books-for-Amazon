# -*- coding: utf-8 -*-
import re
import zipfile
from pathlib import Path

def text_of(path: Path) -> str:
    xml = zipfile.ZipFile(path).read("word/document.xml").decode("utf-8", "replace")
    text = re.sub(r"</w:p>", "\n", xml)
    text = re.sub(r"<[^>]+>", "", text)
    return text

p = Path(r"D:\Book Backups\Cosmology\A Permit Is Not a City - Manuscript\A Permit Is Not a City - Kindle.docx")
text = text_of(p)
body = text[starts[-1]:] if (starts := [m.start() for m in re.finditer(r"(?m)^1\. The Airlock Still Sticks\s*$", text)]) else text
print("body words", len(re.findall(r"\S+", body)))
for needle in ["A Suit Is a Spacecraft", "Two Weeks of Night", "Crews That Do Not Sleep", "Her Hands Still Age", "APPENDIX", "Appendix"]:
    print(needle, body.find(needle))
print("--- HEADS ---")
for line in body.splitlines():
    s = line.strip()
    if re.match(r"^(\d+\.\s+[A-Z]|PART |Appendix|APPENDIX)", s) and len(s) < 100:
        print(s)
