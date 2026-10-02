import os, sys
import pymupdf
import win32com.client

W = os.path.dirname(os.path.abspath(__file__))
docx_path = os.path.join(W, sys.argv[1] if len(sys.argv) > 1 else 'trial_print.docx')
pdf = os.path.join(W, 'qa.pdf')
out = os.path.join(W, 'qa')
os.makedirs(out, exist_ok=True)

if not os.path.exists(pdf) or os.path.getmtime(pdf) < os.path.getmtime(docx_path):
    word = win32com.client.DispatchEx('Word.Application')
    word.Visible = False
    word.DisplayAlerts = 0
    try:
        d = word.Documents.Open(docx_path, ReadOnly=True)
        d.ExportAsFixedFormat(pdf, 17)
        d.Close(False)
    finally:
        word.Quit()

doc = pymupdf.open(pdf)
print('pdf pages', doc.page_count)
targets = [
    ('contents', 'Contents'),
    ('before', 'Before You Start'),
    ('preface', 'How an Engineer Decides What to Trust'),
    ('part1', 'Part I'),
    ('physics4', 'Why Does Time Have a Direction?'),
    ('lecture8', "Bell's ceiling"),
    ('qed1', 'Lesson 1'),
    ('storey11', 'Worked example.'),
    ('history', "We are the dolphins"),
    ('afterword', 'The Same Few Rules'),
    ('glossary', 'Each entry names the place'),
    ('index', 'Index'),
    ('alsoby', 'Also by the Author'),
]
found = {}
for name, needle in targets:
    start = 2 if name != 'contents' else 1
    for pno in range(start, doc.page_count):
        page = doc[pno]
        if needle in page.get_text():
            if name in ('index', 'alsoby', 'glossary', 'afterword'):
                # last occurrence = the back-matter page
                found[name] = pno
                continue
            found[name] = pno
            break
for name, pno in found.items():
    pix = doc[pno].get_pixmap(dpi=70)
    p = os.path.join(out, '%s_p%d.png' % (name, pno + 1))
    pix.save(p)
    print(name, pno + 1, p)
