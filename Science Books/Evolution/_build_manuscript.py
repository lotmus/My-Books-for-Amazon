"""Assemble the 31 Evolution chapter .docx files into one Kindle-ready manuscript
with a title page and a hyperlinked Word Contents page (bookmarks + internal
hyperlinks; the reader clicks straight to the chapter, no Update Field needed).

Usage: python build_manuscript.py
"""
import glob
import html
import os
import re
import zipfile

FOLDER = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(FOLDER, '27 - Can a Mind Be Built - Evolution and AI - Funny.docx')
OUT = os.path.join(FOLDER, 'Life - Science for Everyone - Full Manuscript.docx')

PARTS = [
    ('Part I: What Life Is and How It Began', ['01', '02', '03', '04', '05']),
    ('Part II: Darwin\u2019s Machine', ['06', '07', '08', '09', '10', '11', '12']),
    ('Part III: The Big Transitions', ['13', '14', '15', '16', '17', '18', '19']),
    ('Part IV: Us', ['20', '21', '22']),
    ('Part V: Minds, Loops and Machines', ['23', '24', '25', '26', '27', '27a', '28', '29']),
    ('Part VI: Elsewhere', ['30']),
]


def esc(s):
    return html.escape(s, quote=False)


def find_file(num):
    matches = [f for f in glob.glob(os.path.join(FOLDER, num + ' - *.docx'))
               if re.match(r'^' + re.escape(num) + r' - ', os.path.basename(f))]
    if len(matches) != 1:
        raise SystemExit(f'chapter {num}: expected 1 file, found {len(matches)}: {matches}')
    return matches[0]


def chapter_title(num):
    """Read the 'Chapter N' and title Heading1 paragraphs straight from the file."""
    z = zipfile.ZipFile(find_file(num))
    doc = z.read('word/document.xml').decode('utf-8')
    heads = re.findall(r'<w:pStyle w:val="Heading1"/>.*?</w:p>', doc)
    # first Heading1 = "Chapter N", second Heading1 = the title
    texts = []
    for h in heads[:2]:
        t = ''.join(re.findall(r'<w:t[^>]*>(.*?)</w:t>', h))
        texts.append(html.unescape(t))
    return texts[1] if len(texts) > 1 else texts[0]


def chapter_body_xml(num, bookmark_id, bookmark_name):
    z = zipfile.ZipFile(find_file(num))
    doc = z.read('word/document.xml').decode('utf-8')
    body = doc[doc.index('<w:body>') + len('<w:body>'):doc.index('<w:sectPr')]
    paras = re.findall(r'<w:p>.*?</w:p>', body, re.S)
    # paras[0] = Title "Life: Science for Everyone" -> drop
    # paras[1] = "Chapter N" -> add page break + bookmark here
    # paras[2] = chapter title -> part of chapter, no break
    # paras[3:] = body
    assert len(paras) >= 3, f'chapter {num}: too few paragraphs'
    p_chapnum, p_title, rest = paras[1], paras[2], paras[3:]
    p_chapnum = p_chapnum.replace(
        '<w:pPr>', '<w:pPr><w:pageBreakBefore/>', 1
    ).replace(
        '<w:pStyle w:val="Heading1"/>',
        '<w:pStyle w:val="Heading1"/><w:bookmarkStart w:id="%d" w:name="%s"/>' % (bookmark_id, bookmark_name),
        1,
    )
    # close the bookmark right after the run content, before </w:p>
    p_chapnum = p_chapnum[:-len('</w:p>')] + '<w:bookmarkEnd w:id="%d"/></w:p>' % bookmark_id
    return p_chapnum + p_title + ''.join(rest)


def hyperlink_para(text, anchor):
    return (
        '<w:p><w:pPr><w:ind w:left="0" w:right="0" w:firstLine="0"/><w:jc w:val="center"/></w:pPr>'
        '<w:hyperlink w:anchor="%s" w:history="1">'
        '<w:r><w:rPr><w:color w:val="0563C1"/><w:u w:val="single"/></w:rPr><w:t>%s</w:t></w:r>'
        '</w:hyperlink></w:p>' % (anchor, esc(text))
    )


def plain_para(text, style=None, bold=False, page_break=False, headline=False):
    ppr = '<w:pPr>'
    if page_break:
        ppr += '<w:pageBreakBefore/>'
    if style:
        ppr += '<w:pStyle w:val="%s"/>' % style
    ppr += '<w:ind w:left="0" w:right="0" w:firstLine="0"/><w:jc w:val="center"/></w:pPr>'
    if headline:
        # matches the Amazon Ember / bold / blue 0000FF headline styling used
        # throughout the book (Title and Heading1 in every chapter's styles.xml);
        # this is for the Contents page's Part labels, which are plain bold runs,
        # not a paragraph style, so they need the same formatting spelled out here.
        rpr = ('<w:rPr><w:rFonts w:ascii="Amazon Ember" w:hAnsi="Amazon Ember" w:cs="Amazon Ember"/>'
               '<w:b/><w:color w:val="0000FF"/></w:rPr>')
    elif bold:
        rpr = '<w:rPr><w:b/></w:rPr>'
    else:
        rpr = ''
    return '<w:p>%s<w:r>%s<w:t>%s</w:t></w:r></w:p>' % (ppr, rpr, esc(text))


def build():
    zin = zipfile.ZipFile(TEMPLATE)
    doc = zin.read('word/document.xml').decode('utf-8')
    head = doc[:doc.index('<w:body>') + len('<w:body>')]
    sect = doc[doc.index('<w:sectPr'):]

    xml = []
    xml.append(plain_para('Life: Science for Everyone', style='Title'))
    xml.append(plain_para('A Popular Science Book on Evolution', style='Subtitle'))

    xml.append(plain_para('Contents', style='Heading1', page_break=True))
    titles = {}
    bm_id = 100
    anchors = {}
    for part_title, nums in PARTS:
        for num in nums:
            titles[num] = chapter_title(num)
            anchors[num] = 'chap%s' % num
    def display_num(num):
        m = re.match(r'(\d+)([a-z]?)', num)
        return str(int(m.group(1))) + m.group(2)

    for part_title, nums in PARTS:
        xml.append(plain_para(part_title, headline=True))
        for num in nums:
            label = 'Chapter %s \u2014 %s' % (display_num(num), titles[num])
            xml.append(hyperlink_para(label, anchors[num]))

    for part_title, nums in PARTS:
        xml.append(plain_para(part_title, style='Heading1', page_break=True))
        for num in nums:
            bm_id += 1
            xml.append(chapter_body_xml(num, bm_id, anchors[num]))

    newdoc = head + ''.join(xml) + sect
    tmp = OUT + '.tmp'
    with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == 'word/document.xml':
                data = newdoc.encode('utf-8')
            zout.writestr(item, data)
    zin.close()
    os.replace(tmp, OUT)
    print('built', OUT)


if __name__ == '__main__':
    build()
