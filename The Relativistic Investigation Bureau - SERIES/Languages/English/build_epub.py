# -*- coding: utf-8 -*-
import docx
from ebooklib import epub
from html import escape

SRC = "The_Murder_That_Hadnt_Happened_Yet_PUBLISHING.docx"
COVER = "unpacked/word/media/image1.png"
OUT = "The_Murder_That_Hadnt_Happened_Yet.epub"

d = docx.Document(SRC)
paras = d.paragraphs

def para_text(p):
    return p.text

def is_center(p):
    try:
        return p.alignment is not None and int(p.alignment) == 1
    except Exception:
        return False

def runs_html(p):
    parts = []
    for r in p.runs:
        t = escape(r.text or "")
        if not t:
            continue
        t = t.replace("\n", "<br/>")
        if r.bold:
            t = f"<b>{t}</b>"
        if r.italic:
            t = f"<i>{t}</i>"
        parts.append(t)
    return "".join(parts)

start_idx = 0
for i, p in enumerate(paras):
    if p.style.name == 'Heading 1':
        start_idx = i
        break

front_paras = []
for p in paras[:start_idx]:
    if p.text.strip() == 'Contents':
        break
    front_paras.append(p)

sections = []
current = None
for p in paras[start_idx:]:
    if p.style.name == 'Heading 1':
        if current is not None:
            sections.append(current)
        current = (p.text.strip(), [])
    else:
        if current is not None:
            current[1].append(p)
if current is not None:
    sections.append(current)

# Build a richer nav title for numbered chapters: "Chapter N — Subtitle",
# pulled from the first non-empty body paragraph (the centered subtitle line).
def nav_title_for(heading, body):
    if heading.startswith('Chapter ') or heading in ('Prologue', 'Epilogue'):
        for p in body:
            t = p.text.strip()
            if t:
                return f"{heading} — {t}"
    return heading

nav_titles = [nav_title_for(h, b) for h, b in sections]

print(f"Found {len(sections)} top-level sections:")
for (title, _), nav in zip(sections, nav_titles):
    print(" -", nav)

book = epub.EpubBook()
book.set_identifier('sgr-murder-that-hadnt-happened-yet-v2')
book.set_title("The Murder That Hadn’t Happened Yet")
book.set_language('en')
book.add_author('Spezala Genara Relavi')

with open(COVER, 'rb') as f:
    cover_bytes = f.read()
book.set_cover('cover.jpg', cover_bytes)

CSS = """
body { font-family: Georgia, 'Palatino Linotype', serif; line-height: 1.5; }
h1 { text-align: center; margin-top: 2em; margin-bottom: 0.3em; font-size: 1.6em; page-break-before: always; }
h2 { text-align: center; margin-top: 1.6em; margin-bottom: 0.6em; font-size: 1.25em; }
p { margin: 0 0 0.8em 0; text-indent: 1.2em; }
p.center { text-align: center; text-indent: 0; }
p.subtitle { text-align: center; text-indent: 0; font-style: italic; margin-bottom: 1.2em; }
.titlepage p { text-indent: 0; text-align: center; }
"""
css_item = epub.EpubItem(uid="style", file_name="style/style.css", media_type="text/css", content=CSS)
book.add_item(css_item)

chapters = []

tp_html = ['<div class="titlepage">']
for p in front_paras:
    t = runs_html(p) or escape(p.text)
    if not t.strip():
        continue
    style = p.style.name
    if style == 'Title':
        tp_html.append(f'<h1>{t}</h1>')
    elif style == 'Subtitle':
        tp_html.append(f'<p class="subtitle">{t}</p>')
    else:
        tp_html.append(f'<p class="center">{t}</p>')
tp_html.append('</div>')
c_title = epub.EpubHtml(title='Title Page', file_name='titlepage.xhtml', lang='en')
c_title.content = "<html><head><link rel='stylesheet' href='style/style.css'/></head><body>" + "\n".join(tp_html) + "</body></html>"
c_title.add_item(css_item)
book.add_item(c_title)
chapters.append(c_title)

for si, (heading, body) in enumerate(sections):
    fname = f"sec{si:02d}.xhtml"
    html = [f'<h1>{escape(heading)}</h1>']
    for p in body:
        text_html = runs_html(p)
        if not text_html.strip():
            continue
        style = p.style.name
        if style == 'Heading 2':
            html.append(f'<h2>{escape(p.text)}</h2>')
        elif is_center(p):
            html.append(f'<p class="center">{text_html}</p>')
        else:
            html.append(f'<p>{text_html}</p>')
    c = epub.EpubHtml(title=nav_titles[si], file_name=fname, lang='en')
    c.content = "<html><head><link rel='stylesheet' href='style/style.css'/></head><body>" + "\n".join(html) + "</body></html>"
    c.add_item(css_item)
    book.add_item(c)
    chapters.append(c)

book.toc = tuple(chapters[1:])
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())
book.spine = ['cover', 'nav'] + chapters

epub.write_epub(OUT, book, {})
print(f"\nEPUB written: {OUT}")

import os
print("size:", os.path.getsize(OUT), "bytes")
