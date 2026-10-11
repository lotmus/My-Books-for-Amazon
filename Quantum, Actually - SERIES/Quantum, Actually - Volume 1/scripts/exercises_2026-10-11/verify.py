import sys, zipfile, re
from lxml import etree
src='/workspace/qa1x/src/Quantum, Actually - Volume 1_REV02_2026-10-05.docx'
new=sys.argv[1]
a=zipfile.ZipFile(src); b=zipfile.ZipFile(new)
print('testzip', b.testzip())
sa=set(a.namelist()); sb=set(b.namelist())
print('entries missing', sa-sb, 'added', sb-sa)
for n in ['word/_rels/document.xml.rels']:
    print(n, 'identical' if a.read(n)==b.read(n) else 'DIFFERENT')
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
d=etree.fromstring(b.read('word/document.xml'))
txt=''.join(t.text or '' for t in d.iter(W+'t'))
print('tables', len(list(d.iter(W+'tbl'))))
print('hyperlinks', len(list(d.iter(W+'hyperlink'))), 'orig', len(list(etree.fromstring(a.read('word/document.xml')).iter(W+'hyperlink'))))
print('visible URLs', re.findall(r'(?:https?://|www\.)\S+', txt)[:5])
import os; print('size MB', round(os.path.getsize(new)/1e6,2))
print('words', len(txt.split()))
