"""Assemble the 31 Evolution chapter .docx files into one Kindle-ready manuscript
with a title page, a copyright page, a hyperlinked Word Contents page (bookmarks + internal
hyperlinks; the reader clicks straight to the chapter, no Update Field needed),
and Further Reading and About the Author back-matter sections.

Heading scheme (Kindle-friendly): in each chapter file the "Chapter N" label uses the
ChapterLabel style (no outline level), the chapter title is Heading 1, and section headings
are Heading 2. Part titles and "Contents" use PartTitle (no outline level), so the Kindle /
Word navigation pane lists chapters (plus Further Reading and About the Author) only.
Output is .docx only.

Usage: python scripts/_build_manuscript.py
"""
import glob
import html
import os
import re
import zipfile

# Book-root layout: this script lives in scripts\, chapter files in chapters\,
# and the master manuscript is written to the book root.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FOLDER = os.path.join(ROOT, 'chapters')
TEMPLATE = os.path.join(FOLDER, '27 - Can a Mind Be Built - Evolution and AI - Funny.docx')
OUT = os.path.join(ROOT, 'Life - Evolution - Full Manuscript.docx')

AUTHOR = 'Lothar J. Musiol'
SERIES = 'Physics, Actually'
COPYRIGHT = [
    'Copyright \u00a9 2026 Lothar J. Musiol',
    'All rights reserved.',
    'Series: ' + SERIES,
    'No part of this book may be reproduced, stored, or transmitted in any form or by any means without written permission from the author, except for brief quotations in reviews.',
    'This book is a work of popular science. It reflects the scientific understanding at the time of writing; some details will change as research moves on.',
    'First edition, 2026',
]
# Back-matter author page. Facts only from Lothar's About the Author pages in his other books
# (Science Books/The Quantum Conversation back matter, Science Books/Physics/about_author_real.txt).
ABOUT_AUTHOR = [
    'Lothar J. Musiol is a graduate of Munich University of Applied Sciences. He spent more than forty years in the semiconductor industry, first at the largest company in the field Germany had to offer, then at a string of American start-ups.',
    'He studied physics alongside all of it, seriously enough to know exactly how much he is simplifying in his books, and how much he is not. He writes to make complex ideas clearer and more engaging than most treatments manage, without ever pretending they are simpler than they actually are.',
    'Dual citizenship lets him split his time between San Clemente, California, and Passau, Bavaria, where Austria begins at the garden fence. The household includes one married daughter, one grumpy Teacup Pomeranian, and eleven chickens.',
]
# (author(s), title, year) -- books discussed in the text; titles are italicized
FURTHER_READING = [
    ('Charles Lyell', 'Principles of Geology', '1830\u20131833'),
    ('Charles Darwin', 'On the Origin of Species', '1859'),
    ('Erwin Schr\u00f6dinger', 'What Is Life?', '1944'),
    ('Richard Dawkins', 'The Selfish Gene', '1976'),
    ('Douglas R. Hofstadter', 'G\u00f6del, Escher, Bach', '1979'),
    ('Douglas R. Hofstadter and Daniel C. Dennett, eds.', "The Mind's I", '1981'),
    ('Richard Dawkins', 'The Extended Phenotype', '1982'),
    ('Robert Axelrod', 'The Evolution of Cooperation', '1984'),
    ('Douglas R. Hofstadter', 'Metamagical Themas', '1985'),
    ('Marvin Minsky', 'The Society of Mind', '1986'),
    ('Daniel C. Dennett', 'The Intentional Stance', '1987'),
    ('Hans Moravec', 'Mind Children', '1988'),
    ('Stephen Jay Gould', 'Wonderful Life', '1989'),
    ('Daniel C. Dennett', 'Consciousness Explained', '1991'),
    ('Jonathan Weiner', 'The Beak of the Finch', '1994'),
    ('Douglas R. Hofstadter', 'Fluid Concepts and Creative Analogies', '1995'),
    ('Daniel C. Dennett', "Darwin's Dangerous Idea", '1995'),
    ('Simon Conway Morris', "Life's Solution", '2003'),
    ('Andrew Parker', 'In the Blink of an Eye', '2003'),
    ('Sean B. Carroll', 'Endless Forms Most Beautiful', '2005'),
    ('Douglas R. Hofstadter', 'I Am a Strange Loop', '2007'),
    ('Douglas R. Hofstadter and Emmanuel Sander', 'Surfaces and Essences', '2013'),
    ('Johnjoe McFadden and Jim Al-Khalili', 'Life on the Edge', '2014'),
    ('Nick Lane', 'The Vital Question', '2015'),
    ('David Reich', 'Who We Are and How We Got Here', '2018'),
]

PARTS = [
    ('Part I: What Life Is and How It Began', ['01', '02', '03', '04', '05']),
    ('Part II: Darwin\u2019s Machine', ['06', '07', '08', '09', '10', '11', '12']),
    ('Part III: The Big Transitions', ['13', '14', '15', '16', '17', '18', '19']),
    ('Part IV: Us', ['20', '21', '22']),
    ('Part V: Minds, Loops and Machines', ['23', '24', '25', '26', '27', '28', '29', '30']),
    ('Part VI: Elsewhere', ['31']),
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
    """Read the chapter title (the first Heading1 paragraph) straight from the file."""
    z = zipfile.ZipFile(find_file(num))
    doc = z.read('word/document.xml').decode('utf-8')
    heads = re.findall(r'<w:pStyle w:val="Heading1"/>.*?</w:p>', doc)
    # "Chapter N" is a ChapterLabel paragraph; the first Heading1 is the title
    if not heads:
        raise SystemExit(f'chapter {num}: no Heading1 title found')
    return html.unescape(''.join(re.findall(r'<w:t[^>]*>(.*?)</w:t>', heads[0])))


def chapter_body_xml(num, bookmark_id, bookmark_name):
    z = zipfile.ZipFile(find_file(num))
    doc = z.read('word/document.xml').decode('utf-8')
    body = doc[doc.index('<w:body>') + len('<w:body>'):doc.index('<w:sectPr')]
    paras = re.findall(r'<w:p>.*?</w:p>', body, re.S)
    # paras[0] = Title "Life: Evolution" -> drop
    # paras[1] = "Chapter N" (ChapterLabel) -> add page break + bookmark here
    # paras[2] = chapter title -> part of chapter, no break
    # paras[3:] = body
    assert len(paras) >= 3, f'chapter {num}: too few paragraphs'
    p_chapnum, p_title, rest = paras[1], paras[2], paras[3:]
    p_chapnum = p_chapnum.replace(
        '<w:pPr>', '<w:pPr><w:pageBreakBefore/>', 1
    ).replace(
        '<w:pStyle w:val="ChapterLabel"/>',
        '<w:pStyle w:val="ChapterLabel"/><w:bookmarkStart w:id="%d" w:name="%s"/>' % (bookmark_id, bookmark_name),
        1,
    )
    # close the bookmark right after the run content, before </w:p>
    assert 'bookmarkStart' in p_chapnum, f'chapter {num}: ChapterLabel paragraph not found'
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


def reading_para(author, title, year):
    return (
        '<w:p><w:pPr><w:ind w:left="0" w:right="0" w:firstLine="0"/><w:jc w:val="center"/></w:pPr>'
        '<w:r><w:t xml:space="preserve">%s, </w:t></w:r>'
        '<w:r><w:rPr><w:i/></w:rPr><w:t>%s</w:t></w:r>'
        '<w:r><w:t xml:space="preserve"> (%s)</w:t></w:r></w:p>' % (esc(author), esc(title), esc(year))
    )


def bookmarked_heading(text, bookmark_id, bookmark_name):
    p = plain_para(text, style='Heading1', page_break=True)
    p = p.replace('<w:pStyle w:val="Heading1"/>',
                  '<w:pStyle w:val="Heading1"/><w:bookmarkStart w:id="%d" w:name="%s"/>' % (bookmark_id, bookmark_name), 1)
    return p[:-len('</w:p>')] + '<w:bookmarkEnd w:id="%d"/></w:p>' % bookmark_id


def build():
    zin = zipfile.ZipFile(TEMPLATE)
    doc = zin.read('word/document.xml').decode('utf-8')
    head = doc[:doc.index('<w:body>') + len('<w:body>')]
    sect = doc[doc.index('<w:sectPr'):]

    xml = []
    xml.append(plain_para(SERIES, headline=True))
    xml.append(plain_para('Life: Evolution', style='Title'))
    xml.append(plain_para('A Popular Science Book on Evolution', style='Subtitle'))
    xml.append(plain_para(AUTHOR, bold=True))

    # copyright page
    for i, line in enumerate(COPYRIGHT):
        xml.append(plain_para(line, page_break=(i == 0)))

    xml.append(plain_para('Contents', style='PartTitle', page_break=True))
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
    xml.append(plain_para('Back Matter', headline=True))
    xml.append(hyperlink_para('Further Reading', 'further_reading'))
    xml.append(hyperlink_para('About the Author', 'about_author'))

    for part_title, nums in PARTS:
        xml.append(plain_para(part_title, style='PartTitle', page_break=True))
        for num in nums:
            bm_id += 1
            xml.append(chapter_body_xml(num, bm_id, anchors[num]))

    # back matter
    xml.append(bookmarked_heading('Further Reading', 900, 'further_reading'))
    xml.append(plain_para('These are the books discussed in this one, plus a few that go further, '
                          'in order of publication. Each is a good next step for a reader who wants more.'))
    for author, title, year in FURTHER_READING:
        xml.append(reading_para(author, title, year))

    xml.append(bookmarked_heading('About the Author', 901, 'about_author'))
    for line in ABOUT_AUTHOR:
        xml.append(plain_para(line))

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
