from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import json, hashlib

BOOK = Path(__file__).resolve().parents[1]
SRC = BOOK / 'The_Permitted_Options_BOOK_2_DRAFT.docx'
NS = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
with ZipFile(SRC) as z:
    root = etree.fromstring(z.read('word/document.xml'))
paras = root.xpath('//w:body//w:p', namespaces=NS)
lines = []
for i,p in enumerate(paras):
    t = ''.join(p.xpath('.//w:t/text()', namespaces=NS))
    style = p.xpath('./w:pPr/w:pStyle/@w:val', namespaces=NS)
    lines.append(f'[{i}] [{style[0] if style else "default"}] {t}')
out = BOOK / 'bak' / 'review-20261005'
out.mkdir(exist_ok=True)
(out / 'manuscript.txt').write_text('\n'.join(lines), encoding='utf-8')
print(json.dumps({'paragraphs':len(paras), 'words':sum(len(x.split()) for x in root.xpath('//w:t/text()',namespaces=NS)), 'sha256':hashlib.sha256(SRC.read_bytes()).hexdigest(), 'extraction':str(out/'manuscript.txt')}, indent=2))
