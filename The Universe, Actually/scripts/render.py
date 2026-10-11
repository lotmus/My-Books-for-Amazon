# -*- coding: utf-8 -*-
# XML renderer for the manuscript (direct formatting, matching REV11's look).
import re
from xml.sax.saxutils import escape
import tex

GEORGIA = '<w:rFonts w:ascii="Georgia" w:cs="Georgia" w:eastAsia="Georgia" w:hAnsi="Georgia"/>'
LIB = '<w:rFonts w:ascii="Liberation Serif" w:cs="Liberation Serif" w:eastAsia="Liberation Serif" w:hAnsi="Liberation Serif"/>'

def rpr(font=GEORGIA, b=False, i=False, color=None, sz=22, u=False, va=None):
    s = font
    if b: s += '<w:b/><w:bCs/>'
    if i: s += '<w:i/><w:iCs/>'
    if color: s += '<w:color w:val="%s"/>' % color
    s += '<w:sz w:val="%d"/><w:szCs w:val="%d"/>' % (sz, sz)
    if u: s += '<w:u w:val="single"/>'
    if va: s += '<w:vertAlign w:val="%s"/>' % ('superscript' if va == 'sup' else 'subscript')
    return '<w:rPr>%s</w:rPr>' % s

def run(text, **kw):
    if not text: return ''
    return '<w:r>%s<w:t xml:space="preserve">%s</w:t></w:r>' % (rpr(**kw), escape(text))

MATH = re.compile(r'\\\((.+?)\\\)|\\\[(.+?)\\\]', re.S)
TOK = re.compile(r'\*\*(.+?)\*\*|\\\((.+?)\\\)|\\\[(.+?)\\\]|(?<![\w*])\*([^*\s][^*]*?)\*(?![\w*])', re.S)

def inline_runs(text, **kw):
    """text with **bold** and \\( math \\) -> run xml"""
    text = text.replace('\\ldots', '…')
    out = []; pos = 0
    for m in TOK.finditer(text):
        if m.start() > pos: out.append(run(text[pos:m.start()], **kw))
        if m.group(1) is not None:
            k = dict(kw); k['b'] = True
            # bold span may itself hold math
            out.append(inline_runs(m.group(1), **k) if '\\(' in m.group(1) else run(m.group(1), **k))
        elif m.group(4) is not None:
            k = dict(kw); k['i'] = True
            out.append(run(m.group(4), **k))
        else:
            for t, kind in tex.parse(m.group(2) or m.group(3)):
                k = dict(kw)
                if kind: k['va'] = kind
                out.append(run(t, **k))
        pos = m.end()
    if pos < len(text): out.append(run(text[pos:], **kw))
    return ''.join(out)

def para(text, ppr='<w:spacing w:after="120" w:line="276"/>', **kw):
    return '<w:p><w:pPr>%s</w:pPr>%s</w:p>' % (ppr, inline_runs(text, **kw))

_bm = [100]
def bookmark_wrap(name, inner):
    _bm[0] += 1; i = _bm[0]
    return '<w:bookmarkStart w:id="%d" w:name="%s"/>%s<w:bookmarkEnd w:id="%d"/>' % (i, name, inner, i)

def h1(text, bm=None, center=False, before=200, after=240, sz=36):
    jc = '<w:jc w:val="center"/>' if center else ''
    inner = run(text, font=LIB, b=True, color='2E5A88', sz=sz)
    if bm: inner = bookmark_wrap(bm, inner)
    return '<w:p><w:pPr><w:pStyle w:val="Heading1"/><w:pageBreakBefore/><w:spacing w:after="%d" w:before="%d"/>%s</w:pPr>%s</w:p>' % (after, before, jc, inner)

def part_title(text, bm):
    return h1(text, bm, center=True, before=360, after=200, sz=40)

def tagline(text):
    return '<w:p><w:pPr><w:spacing w:after="360"/><w:jc w:val="center"/></w:pPr>%s</w:p>' % run(text, font=LIB, i=True, color='5C6B73', sz=22)

def h2(text, bm, pagebreak=True):
    inner = bookmark_wrap(bm, run(text, b=True, color='1F4E79', sz=28))
    pb = '<w:pageBreakBefore/>' if pagebreak else ''
    return '<w:p><w:pPr><w:pStyle w:val="Heading2"/>'+pb+'<w:spacing w:after="160" w:before="200"/><w:jc w:val="center"/></w:pPr>%s</w:p>' % inner

def h3(text, bm=None):
    inner = run(text, b=True, color='1F4E79', sz=24)
    if bm: inner = bookmark_wrap(bm, inner)
    return '<w:p><w:pPr><w:pStyle w:val="Heading3"/><w:keepNext/><w:spacing w:after="100" w:before="320"/></w:pPr>%s</w:p>' % inner

def body(text):
    return para(text)

def lead_italic(text):
    return para(text, ppr='<w:spacing w:after="200" w:line="276"/>', i=True, color='5C6B73')

def toc_part(text, anchor):
    r = '<w:hyperlink w:history="1" w:anchor="%s">%s</w:hyperlink>' % (anchor, run(text, b=True, color='1F4E79', sz=26, u=False))
    return '<w:p><w:pPr><w:keepNext/><w:spacing w:after="60" w:before="280"/></w:pPr>%s</w:p>' % r

def toc_chapter(text, anchor):
    r = '<w:hyperlink w:history="1" w:anchor="%s">%s</w:hyperlink>' % (anchor, run(text, color='1F4E79', sz=22, u=True))
    return '<w:p><w:pPr><w:spacing w:after="50"/><w:ind w:left="360"/></w:pPr>%s</w:p>' % r

def toc_plain(text, anchor):
    r = '<w:hyperlink w:history="1" w:anchor="%s">%s</w:hyperlink>' % (anchor, run(text, b=True, color='1F4E79', sz=24))
    return '<w:p><w:pPr><w:spacing w:after="60" w:before="200"/></w:pPr>%s</w:p>' % r

def small_heading(text):
    return '<w:p><w:pPr><w:keepNext/><w:spacing w:after="100" w:before="240"/></w:pPr>%s</w:p>' % run(text, b=True, color='1F4E79', sz=28)

def centered_h1_plain(text, bm=None):
    return h1(text, bm, center=True, before=200, after=280, sz=32)
