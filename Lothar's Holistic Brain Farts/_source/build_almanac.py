# -*- coding: utf-8 -*-
"""Assemble The Universe Keeps the Books from the condensed markdown fragments.

Usage: python build_almanac.py [output.docx]
The table of contents is written directly into the file as hyperlinked entries
(Heading 1-3, bookmarks + internal links, no Word automation needed).
"""
import copy
import os
import re
import sys
import docx
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt, Inches, RGBColor
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

BASE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_OUT = os.path.join(BASE, "build", "almanac_build.docx")

BODY_FONT = "Georgia"
HEADLINE_FONT = "Amazon Ember"
HEADLINE_COLOR = RGBColor(0x00, 0x00, 0xFF)  # sampled from the user's reference image
BRIDGE = 'BRIDGE'
TOC_MAX_LEVEL = 3

PARTS = [
    ("Part I — Physics, Cosmology & the Quantum World",
     "In which the universe is examined closely enough to notice it's making rather a mess of "
     "‘now’ — and everything else in this book, from self-copying chemistry to the "
     "circuits on the next shelf, keeps turning up again, unmistakably, in what follows.",
     ["05_physics.md",
      (BRIDGE, "Physics laid out the rules at human scale. Cosmology is what those same rules "
               "do when you run them for thirteen billion years, at the scale of everything "
               "there is."),
      "02_cosmology.md",
      (BRIDGE, "Zoom back down from the largest scale to the smallest, and the same rules get "
               "considerably stranger rather than simpler."),
      "04b_qworld_prose.md",
      (BRIDGE, "The Quantum World lays out what quantum mechanics actually found. The Quantum "
               "Conversation is a second, deeper pass over the same territory, told through one "
               "physicist's insistence on explaining it a different way — and arriving, "
               "reassuringly, in the same place."),
      "04c_qconv_prose.md"]),
    ("Part II — Life, Evolution & Genetics",
     "In which life insists on copying itself badly enough to become interesting. If Part I "
     "described the stage, this is the first thing that climbed onto it and refused to leave.",
     ["03_evolution.md",
      (BRIDGE, "Evolution is the four-billion-year argument. Genetics is the fine print it was "
               "written in."),
      "04a_genetics_prose.md"]),
    ("Part III — Mathematics",
     "In which numbers behave themselves rather better than anything else in this book. Every "
     "equation quietly stripped out of Parts I and II is hiding in here somewhere, fully "
     "dressed and considerably less embarrassed.",
     ["06_math_tower.md"]),
    ("Part IV — Electrical Engineering & QED",
     "In which electrons are persuaded to do useful things, mostly by asking nicely. This is "
     "Part III's mathematics, put to work paying rent.",
     ["01_ee_qed.md"]),
    ("Part V — History",
     "As narrated, with some justified smugness, by dolphins. Everything upstream of this part "
     "— the physics, the biology, the mathematics, the circuitry — is what a species "
     "with hands and no particular wisdom did with several million spare years.",
     ["09_history.md"]),
    ("Part VI — Science Smuggled Into the Novels",
     "Where the plot pauses so someone can explain relativity. Consider it proof that a fair "
     "chunk of Part I can survive being smuggled into a joke.",
     ["10_novel_appendices.md",
      (BRIDGE, "The lectures just above are the course. What follows keeps only the scenes "
               "that are not that course a second time."),
      "11_novel_narrative_science.md"]),
]

# Text inserted (italic) right after the first heading of a fragment file.
NOTES = {
    "02_cosmology.md": "Three related books share this file, loosely bound by the theme of time "
                       "and distance rather than by subject: cosmic time (this one), bodily time "
                       "(“The Body Keeps Its Own Clock,” on aging and medicine), and the "
                       "distance to everywhere else (“A Permit Is Not a City,” on leaving "
                       "Earth). Each stands on its own; read them as three short books back to "
                       "back, not one long one.",
}

HEADING_RENAMES = {}   # heading text replaced at render time (fragment files stay untouched)
LABEL_DASH_RE = re.compile(r'^(Prologue|Epilogue|Appendix(?: [A-Z0-9]+)?) — (.+)$')


def normalize_heading(text):
    """'Prologue — X' -> 'Prologue: X' (unless X already contains a colon)."""
    m = LABEL_DASH_RE.match(text)
    if m and ':' not in m.group(2):
        return '%s: %s' % (m.group(1), m.group(2))
    return text

MISSING_NOTE = "(Pending — this section's source has not been produced yet.)"
TOKEN_RE = re.compile(r'(\*\*.+?\*\*|\*[^*\n]+?\*)')

HEADINGS = []          # (level, plain text, bookmark name) for the table of contents
_bookmark_counter = [0]

# ---------- cross-reference auto-linking ----------
# Populated as the document is built, then used in a final pass (after every bookmark
# exists) to turn existing in-text references into real hyperlinks: "Part III", exact
# book titles ("The Quantum World"), and "Chapter N"/"Storey N"/"Lesson N" callbacks.
GLOBAL_TITLE_LINKS = {}   # exact heading text (Part titles, book titles) -> bookmark name
BODY_PARAGRAPHS = []      # (paragraph, local_numeric_dict) scanned in the final linking pass
PART_ROMAN_RE = re.compile(r'^Part (I|II|III|IV|V|VI)\b')
NUM_HEADING_RE = re.compile(r'^(\d+)\.\s')
LABEL_NUM_RE = re.compile(r'^(?:Chapter|Storey|Lesson)\s+(\d+)\b')
LABEL_RANGE_RE = re.compile(r'^(?:Chapters|Lessons)\s+(\d+)\s*[–-]\s*(\d+)\b')
CHAPTER_NUM_RE = re.compile(r'\b(?:Chapter|Storey|Lesson) \d+\b')


# ---------- styling helpers ----------
def set_style_font(style, name, size=None, bold=None, italic=None, color=None):
    style.font.name = name
    rpr = style.element.get_or_add_rPr()
    rfonts = rpr.find(qn('w:rFonts'))
    if rfonts is None:
        rfonts = OxmlElement('w:rFonts')
        rpr.append(rfonts)
    for a in ('w:ascii', 'w:hAnsi', 'w:eastAsia', 'w:cs'):
        rfonts.set(qn(a), name)
    for a in ('w:asciiTheme', 'w:hAnsiTheme', 'w:eastAsiaTheme', 'w:cstheme'):
        if rfonts.get(qn(a)) is not None:
            del rfonts.attrib[qn(a)]
    if size is not None:
        style.font.size = Pt(size)
    if bold is not None:
        style.font.bold = bold
    if italic is not None:
        style.font.italic = italic
    if color is not None:
        style.font.color.rgb = color


def setup_styles(doc):
    black = RGBColor(0, 0, 0)
    normal = doc.styles['Normal']
    set_style_font(normal, BODY_FONT, 11)
    pf = normal.paragraph_format
    pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    pf.first_line_indent = Inches(0.3)
    pf.space_before = Pt(0)
    pf.space_after = Pt(0)
    pf.line_spacing = 1.3
    pf.widow_control = True

    h1 = doc.styles['Heading 1']
    set_style_font(h1, HEADLINE_FONT, 18, bold=True, italic=False, color=HEADLINE_COLOR)
    h1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    h1.paragraph_format.first_line_indent = Inches(0)
    h1.paragraph_format.page_break_before = True
    h1.paragraph_format.space_before = Pt(120)
    h1.paragraph_format.space_after = Pt(18)
    h1.paragraph_format.keep_with_next = True

    h2 = doc.styles['Heading 2']
    set_style_font(h2, HEADLINE_FONT, 18, bold=True, italic=False, color=HEADLINE_COLOR)
    h2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    h2.paragraph_format.first_line_indent = Inches(0)
    h2.paragraph_format.page_break_before = True
    h2.paragraph_format.space_before = Pt(36)
    h2.paragraph_format.space_after = Pt(18)
    h2.paragraph_format.keep_with_next = True

    h3 = doc.styles['Heading 3']
    set_style_font(h3, HEADLINE_FONT, 18, bold=True, italic=False, color=HEADLINE_COLOR)
    h3.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    h3.paragraph_format.first_line_indent = Inches(0)
    h3.paragraph_format.space_before = Pt(22)
    h3.paragraph_format.space_after = Pt(8)
    h3.paragraph_format.keep_with_next = True

    h4 = doc.styles['Heading 4']
    set_style_font(h4, HEADLINE_FONT, 18, bold=True, italic=False, color=HEADLINE_COLOR)
    h4.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    h4.paragraph_format.first_line_indent = Inches(0)
    h4.paragraph_format.space_before = Pt(14)
    h4.paragraph_format.space_after = Pt(6)
    h4.paragraph_format.keep_with_next = True

    for lvl, (indent, size, bold, before) in enumerate(
            [(0.0, 11, True, 9), (0.25, 10.5, False, 1), (0.5, 10, False, 0)], start=1):
        st = doc.styles.add_style('toc %d' % lvl, WD_STYLE_TYPE.PARAGRAPH)
        st.base_style = normal
        set_style_font(st, BODY_FONT, size, bold=bold, italic=False)
        st.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        st.paragraph_format.first_line_indent = Inches(0)
        st.paragraph_format.left_indent = Inches(indent)
        st.paragraph_format.space_before = Pt(before)
        st.paragraph_format.space_after = Pt(0)
        st.paragraph_format.line_spacing = 1.1

    sec = doc.sections[0]
    sec.left_margin = sec.right_margin = Inches(1.1)
    sec.top_margin = sec.bottom_margin = Inches(1.0)


# ---------- content helpers ----------
def plain(text):
    return text.replace('**', '').replace('*', '')


def add_runs_from_markdown(paragraph, text):
    """Split text on **bold** / *italic* markdown tokens and add properly formatted runs."""
    for part in TOKEN_RE.split(text):
        if not part:
            continue
        if part.startswith('**') and part.endswith('**') and len(part) > 4:
            paragraph.add_run(part[2:-2]).bold = True
        elif part.startswith('*') and part.endswith('*') and len(part) > 2:
            paragraph.add_run(part[1:-1]).italic = True
        else:
            paragraph.add_run(part)


def flush_left(p, space_before=0, space_after=0, italic=False, align=None, text=None, size=None):
    pf = p.paragraph_format
    pf.first_line_indent = Inches(0)
    pf.space_before = Pt(space_before)
    pf.space_after = Pt(space_after)
    if align is not None:
        p.alignment = align
    if text is not None:
        r = p.add_run(text)
        r.italic = italic
        if size:
            r.font.size = Pt(size)
    return p


TITLE_LINK_STOPLIST = {'Prologue', 'Epilogue', 'Foreword', 'Afterword', 'Contents',
                       'About the Author', 'Appendix'}


def register_heading(p, level, text):
    """Wrap the heading in a bookmark and remember it for the table of contents."""
    if level > TOC_MAX_LEVEL:
        return None
    _bookmark_counter[0] += 1
    bid = _bookmark_counter[0]
    name = "_Toc%06d" % (900000 + bid)
    start = OxmlElement('w:bookmarkStart')
    start.set(qn('w:id'), str(bid))
    start.set(qn('w:name'), name)
    end = OxmlElement('w:bookmarkEnd')
    end.set(qn('w:id'), str(bid))
    ppr = p._p.find(qn('w:pPr'))
    if ppr is not None:
        ppr.addnext(start)
    else:
        p._p.insert(0, start)
    p._p.append(end)
    clean = plain(text)
    HEADINGS.append((level, clean, name))
    # Index distinctive, multi-word titles (Part titles, book titles) for auto-linking.
    # Skip numbered chapter/storey/lesson headings (linked separately, by number) and
    # generic front-matter labels that are just ordinary English words elsewhere.
    if (clean not in TITLE_LINK_STOPLIST and len(clean.split()) >= 3
            and not NUM_HEADING_RE.match(clean) and not LABEL_NUM_RE.match(clean)
            and not LABEL_RANGE_RE.match(clean)):
        GLOBAL_TITLE_LINKS.setdefault(clean, name)
    part_m = PART_ROMAN_RE.match(clean)
    if part_m:
        GLOBAL_TITLE_LINKS.setdefault('Part %s' % part_m.group(1), name)
    return name


def heading(doc, level, text):
    p = doc.add_paragraph(style='Heading %d' % level)
    add_runs_from_markdown(p, text)
    return register_heading(p, level, text)


def add_link_paragraph(before_paragraph, level, text, anchor):
    p = before_paragraph.insert_paragraph_before(style='toc %d' % level)
    h = OxmlElement('w:hyperlink')
    h.set(qn('w:anchor'), anchor)
    h.set(qn('w:history'), '1')
    r = OxmlElement('w:r')
    t = OxmlElement('w:t')
    t.set(qn('xml:space'), 'preserve')
    t.text = text
    r.append(t)
    h.append(r)
    p._p.append(h)
    return p


def render_markdown(doc, path, heading_offset=0, flat=False, note=None):
    """heading_offset: levels to push '#'-headings down. flat: '#'->H1, everything deeper->H4.

    Tracks a per-book "segment" dict (number -> bookmark) for Chapter/Storey/Lesson
    cross-references, reset whenever a new book title ('#' line) appears, so files that
    bundle several books (e.g. cosmology's three) don't cross-link one book's Chapter 6
    to another's.
    """
    segment = {}
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()
    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            continue
        hashes = len(line) - len(line.lstrip('#'))
        if hashes and line[hashes:hashes + 1] == ' ':
            text = HEADING_RENAMES.get(line[hashes:].strip(), line[hashes:].strip())
            text = normalize_heading(text)
            level = (1 if hashes == 1 else 4) if flat else min(hashes + heading_offset, 4)
            if hashes == 1:
                segment = {}
            bookmark = heading(doc, level, text)
            m = NUM_HEADING_RE.match(text) or LABEL_NUM_RE.match(text)
            if m and bookmark:
                segment[int(m.group(1))] = bookmark
            r = LABEL_RANGE_RE.match(text)
            if r and bookmark:
                for n in range(int(r.group(1)), int(r.group(2)) + 1):
                    segment.setdefault(n, bookmark)
            if note:
                flush_left(doc.add_paragraph(), space_before=0, space_after=10, italic=True, text=note)
                note = None
        elif line.lstrip().startswith(('- ', '* ')):
            p = doc.add_paragraph(style='List Bullet')
            add_runs_from_markdown(p, line.lstrip()[2:].strip())
            BODY_PARAGRAPHS.append((p, segment))
        else:
            p = doc.add_paragraph()
            add_runs_from_markdown(p, line)
            BODY_PARAGRAPHS.append((p, segment))


def _make_text_run(text, base_rpr):
    r = OxmlElement('w:r')
    if base_rpr is not None:
        r.append(copy.deepcopy(base_rpr))
    t = OxmlElement('w:t')
    t.set(qn('xml:space'), 'preserve')
    t.text = text
    r.append(t)
    return r


def _make_link_run(text, base_rpr, bookmark):
    h = OxmlElement('w:hyperlink')
    h.set(qn('w:anchor'), bookmark)
    h.set(qn('w:history'), '1')
    r = OxmlElement('w:r')
    rpr = OxmlElement('w:rPr')
    if base_rpr is not None:
        rpr.append(copy.deepcopy(base_rpr))
    color = OxmlElement('w:color')
    color.set(qn('w:val'), '0000FF')
    u = OxmlElement('w:u')
    u.set(qn('w:val'), 'single')
    rpr.append(color)
    rpr.append(u)
    r.append(rpr)
    t = OxmlElement('w:t')
    t.set(qn('xml:space'), 'preserve')
    t.text = text
    r.append(t)
    h.append(r)
    return h


def linkify_document():
    """Final pass: turn 'Part III', exact book titles, and 'Chapter N'/'Storey N'/'Lesson N'
    mentions in body text into real hyperlinks, now that every bookmark exists. Only rewrites
    a run when it actually contains a resolvable reference; everything else is untouched.
    """
    title_keys = sorted(GLOBAL_TITLE_LINKS.keys(), key=len, reverse=True)
    title_pattern = '|'.join(re.escape(k) for k in title_keys)
    parts = [p for p in (title_pattern, CHAPTER_NUM_RE.pattern) if p]
    if not parts:
        return 0
    scan_re = re.compile('(?:' + '|'.join(parts) + ')')
    link_count = 0
    for paragraph, segment in BODY_PARAGRAPHS:
        for run in list(paragraph.runs):
            text = run.text
            if not text or not scan_re.search(text):
                continue
            pieces = []
            pos = 0
            found_any = False
            for m in scan_re.finditer(text):
                token = m.group(0)
                bookmark = GLOBAL_TITLE_LINKS.get(token)
                if bookmark is None and CHAPTER_NUM_RE.match(token):
                    bookmark = segment.get(int(token.rsplit(' ', 1)[1]))
                if bookmark is None:
                    continue
                s, e = m.span()
                if s > pos:
                    pieces.append((text[pos:s], None))
                pieces.append((token, bookmark))
                pos = e
                found_any = True
            if not found_any:
                continue
            if pos < len(text):
                pieces.append((text[pos:], None))
            r = run._r
            parent = r.getparent()
            idx = list(parent).index(r)
            base_rpr = r.find(qn('w:rPr'))
            parent.remove(r)
            for piece_text, bm in pieces:
                if not piece_text:
                    continue
                node = _make_link_run(piece_text, base_rpr, bm) if bm else _make_text_run(piece_text, base_rpr)
                parent.insert(idx, node)
                idx += 1
                if bm:
                    link_count += 1
    return link_count


def build(out_path):
    doc = docx.Document()
    setup_styles(doc)
    doc.core_properties.title = "The Universe Keeps the Books"
    doc.core_properties.author = "Lothar J. Musiol"
    doc.core_properties.comments = "An almanac of highlights compiled from the author's non-fiction catalog."

    # Title page
    flush_left(doc.add_paragraph(), space_before=170, align=WD_ALIGN_PARAGRAPH.CENTER)
    t = doc.paragraphs[-1].add_run("The Universe Keeps the Books")
    t.bold = True
    t.font.size = Pt(34)
    t.font.name = HEADLINE_FONT
    t.font.color.rgb = HEADLINE_COLOR
    flush_left(doc.add_paragraph(), space_before=24, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER,
               text="Physics, life, mathematics, and history.\n"
                    "The same few rules, told in highlights.", size=15)
    flush_left(doc.add_paragraph(), space_before=90, align=WD_ALIGN_PARAGRAPH.CENTER,
               text="Lothar J. Musiol", size=14)
    doc.add_page_break()

    # Copyright page
    flush_left(doc.add_paragraph(), space_before=300, align=WD_ALIGN_PARAGRAPH.CENTER,
               text="Copyright © 2026 Lothar J. Musiol.", size=10)
    flush_left(doc.add_paragraph(), space_before=4, align=WD_ALIGN_PARAGRAPH.CENTER,
               text="All rights reserved.", size=10)
    flush_left(doc.add_paragraph(), space_before=10, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER,
               text="This volume condenses material from the author's own published and "
                    "in-progress works. Full editions of each title are available separately.",
               size=9)

    # Foreword
    heading(doc, 1, "Foreword")
    BODY_PARAGRAPHS.append((doc.add_paragraph(
        "This is not a book. It is what happens when several dozen non-fiction "
        "manuscripts — on physics, cosmology, evolution, genetics, mathematics, "
        "electrical engineering, and human history as narrated by dolphins — are "
        "put through a blender set to ‘highlights’. Nothing here is exhaustive; "
        "everything here is, as far as forty-odd condensation passes can promise, true. "
        "Full editions of every title below exist and are considerably longer — "
        "consult them if a paragraph here leaves you wanting the other eleven thousand words."
    ), {}))
    BODY_PARAGRAPHS.append((doc.add_paragraph(
        "The six parts aren't a ladder so much as six windows facing the same view: a "
        "small number of underlying regularities keeps turning up, recognizably, in each "
        "one. Part I lays out the physical rules the universe runs on, from the smallest "
        "particle to the largest structure. Part II is what those rules produce, "
        "unsupervised, given four billion years and a wet rock: life that copies itself, "
        "imperfectly, on purpose. Part III writes those same rules out in plain sentences, "
        "stripped of the equations they usually hide behind. Part IV puts that same "
        "fluency to work: electrons doing something useful because a sufficiently fluent "
        "species figured out how to ask nicely. Part V is what happens when that species "
        "organizes itself into groups large enough to make simultaneous use — and misuse — "
        "of everything in the parts above, audited this time by an observer with no "
        "particular stake in how flattering the results sound. And Part VI is proof that "
        "none of the above has to be boring: the same physics, still doing its job, hiding "
        "inside a murder mystery."
    ), {}))
    BODY_PARAGRAPHS.append((doc.add_paragraph(
        "None of that is a reading order between Parts, though. Every Part is written to "
        "stand on its own two feet, and none of them depends on having read another first. "
        "Skip straight to whichever Part you're curious about, read them out of order, or "
        "read only one — the book will not mind, and neither will the author. Three "
        "sections inside the Parts are courses rather than highlights, and those do want "
        "reading front to back: the Mathematics Tower, the Complete QED Course, and the "
        "Quantum Lectures. Each lesson there spends the one before it."
    ), {}))
    BODY_PARAGRAPHS.append((doc.add_paragraph(
        "A few appendices smuggled in from the novels are here too, on the "
        "reasoning that a good physics explainer doesn't stop being one just because "
        "someone was recently murdered nearby."
    ), {}))

    # About the Author (file has its own '# About the Author'; language subheads become H4)
    render_markdown(doc, os.path.join(BASE, '00_about_author.md'), flat=True)

    # Contents: a styled paragraph (not a heading, so it doesn't list itself) + placeholder
    p = doc.add_paragraph()
    p.paragraph_format.page_break_before = True
    flush_left(p, space_before=60, space_after=18, align=WD_ALIGN_PARAGRAPH.CENTER)
    r = p.add_run("Contents")
    r.bold = True
    r.font.size = Pt(26)
    r.font.name = HEADLINE_FONT
    r.font.color.rgb = HEADLINE_COLOR
    toc_placeholder = doc.add_paragraph()

    # Parts
    for part_title, blurb, files in PARTS:
        heading(doc, 1, part_title)
        BODY_PARAGRAPHS.append((flush_left(doc.add_paragraph(), space_before=6, space_after=24, italic=True,
                   align=WD_ALIGN_PARAGRAPH.CENTER, text=blurb), {}))
        for item in files:
            if isinstance(item, tuple) and item[0] == BRIDGE:
                BODY_PARAGRAPHS.append((flush_left(doc.add_paragraph(), space_before=14, space_after=14, italic=True,
                           text=item[1]), {}))
                continue
            fpath = os.path.join(BASE, item)
            if os.path.exists(fpath):
                render_markdown(doc, fpath, heading_offset=1, note=NOTES.get(item))
            else:
                heading(doc, 2, item)
                flush_left(doc.add_paragraph(), italic=True, text=MISSING_NOTE)

    # Afterword
    heading(doc, 1, "Afterword")
    BODY_PARAGRAPHS.append((doc.add_paragraph(
        "Where an idea was explained once and then explained again with a different picture, "
        "the second copy is gone. The long books are still the long books."
    ), {}))

    # Auto-link 'Part N', book titles, and 'Chapter/Storey/Lesson N' cross-references
    # now that every bookmark in the book exists.
    link_count = linkify_document()

    # Fill in the table of contents, then drop the placeholder
    for level, text, anchor in HEADINGS:
        add_link_paragraph(toc_placeholder, level, text, anchor)
    toc_placeholder._p.getparent().remove(toc_placeholder._p)

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    doc.save(out_path)
    print("Saved:", out_path)
    print("Words (rough):", sum(len(p.text.split()) for p in doc.paragraphs))
    print("TOC entries:", len(HEADINGS))
    print("Cross-reference links added:", link_count)


if __name__ == '__main__':
    build(sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUT)
