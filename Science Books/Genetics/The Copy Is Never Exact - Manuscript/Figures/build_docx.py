# Builds the Kindle-ready Word manuscript for "The Copy Is Never Exact"
# from the Markdown part files. One figure per chapter (Fig 0 + Fig 1-46).
import io, os, re, glob, sys
from PIL import Image, ImageDraw, ImageFont
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.dirname(HERE)
FIGS = os.path.join(HERE, "figs")
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "The Copy Is Never Exact - Kindle.docx")

TITLE = "The Copy Is Never Exact"
SUBTITLE = "DNA, Inheritance, and the Coming Edit of Ourselves"
AUTHOR = "Lothar J. Musiol"
BODY_FONT = "Georgia"
HEAD_FONT = "Amazon Ember"
HEAD_COLOR = RGBColor(0x00, 0x00, 0xFF)

# ---------------- figure table: number -> (kind, caption) ----------------
FIG = {
 0: ("photo", "A saliva collection tube."),
 1: ("photo", "The Eagle, Bene't Street, Cambridge."),
 2: ("diagram", "The X-shaped diffraction pattern of a helix."),
 3: ("diagram", "The ladder: A with T, G with C."),
 4: ("photo", "Colonies of bacteria on a plate."),
 5: ("diagram", "A nucleotide, and the four bases."),
 6: ("diagram", "A chain of amino acids folds into a working shape."),
 7: ("diagram", "A replication fork."),
 8: ("diagram", "The codon table."),
 9: ("diagram", "The genome's budget: coding, introns, repeats, regulatory, other."),
 10: ("diagram", "A proton hopping across a hydrogen bond: ordinary pair, tautomeric pair."),
 11: ("diagram", "Meiosis, with one crossover between a maternal and a paternal chromosome."),
 12: ("diagram", "A pedigree of an X-linked recessive trait across four generations."),
 13: ("diagram", "A Punnett square for one gene beside the bell curve that thousands of genes produce."),
 14: ("photo", "A bare field in winter."),
 15: ("photo", "Pea plants in flower and in pod."),
 16: ("diagram", "5,474 round seeds to 1,850 wrinkled: about 3 to 1."),
 17: ("photo", "Brno, where Mendel's abbey stands."),
 18: ("photo", "A fruit fly, Drosophila melanogaster."),
 19: ("photo", "Archive cabinets."),
 20: ("diagram", "A plasmid cut open by a restriction enzyme, with a foreign gene pasted into the gap."),
 21: ("diagram", "A Sanger sequencing gel: four lanes, read from the bottom upward."),
 22: ("diagram", "The doubling cascade of the polymerase chain reaction."),
 23: ("diagram", "Short tandem repeat profiles from two samples."),
 24: ("diagram", "Cost per human genome, 2001 to 2025, on a logarithmic axis."),
 25: ("diagram", "Cas9 guided to a target by RNA."),
 26: ("photo", "Samples prepared in a laboratory."),
 27: ("diagram", "A designed protein next to its sequence."),
 28: ("photo", "A cave mouth in limestone."),
 29: ("photo", "A ewe with her lamb in a barn."),
 30: ("photo", "Two dogs of the same litter."),
 31: ("photo", "A research laboratory."),
 32: ("photo", "Ears of corn."),
 33: ("photo", "Tomatoes on a market stall."),
 34: ("photo", "A modern broiler house."),
 35: ("photo", "The entrance of the Svalbard Global Seed Vault."),
 36: ("photo", "A genetics research laboratory."),
 37: ("diagram", "A chromosome ideogram with the regions finished after 2003 marked."),
 38: ("diagram", "A Manhattan plot, sketched."),
 39: ("photo", "A saliva collection kit, boxed."),
 40: ("diagram", "Risk against penetrance."),
 41: ("diagram", "Two overlapping bell curves."),
 42: ("photo", "A server room."),
 43: ("diagram", "Ex vivo and in vivo editing routes."),
 44: ("diagram", "An embryo-selection decision tree."),
 45: ("photo", "A racing whippet at full stretch."),
 46: ("photo", "A newborn's hand."),
}

PARTS = [
    "00_Front_Matter.md",
    "01_Part_One_Shape.md",
    "02_Part_Two_Molecule.md",
    "03_Part_Three_Inheritance.md",
    "04_Part_Four_Monk.md",
    "05_Part_Five_Reading.md",
    "06_Part_Six_Now.md",
    "07_Part_Seven_Copies.md",
    "08_Part_Eight_Dinner.md",
    "09_Part_Nine_Whole_Book.md",
    "10_Part_Ten_Your_Own.md",
    "11_Part_Eleven_Correcting.md",
    "12_Appendix.md",
]

def fig_path(n):
    kind = FIG[n][0]
    if kind == "photo":
        for ext in ("jpg", "jpeg", "png"):
            p = os.path.join(FIGS, f"fig{n:02d}.{ext}")
            if os.path.exists(p): return p, True
        return os.path.join(FIGS, f"fig{n:02d}_slot.png"), False
    for ext in ("png", "jpg", "jpeg"):
        p = os.path.join(FIGS, f"fig{n:02d}.{ext}")
        if os.path.exists(p): return p, True
    return os.path.join(FIGS, f"fig{n:02d}_slot.png"), False

def make_slot_png(n, caption=""):
    """Framed RGB placeholder so Word always has a real picture to embed."""
    os.makedirs(FIGS, exist_ok=True)
    path = os.path.join(FIGS, f"fig{n:02d}_slot.png")
    W, H = 1800, 1350
    im = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(im)
    d.rectangle([40, 40, W - 40, H - 40], outline=(0, 0, 0), width=8)
    d.rectangle([120, 120, W - 120, H - 120], outline=(120, 120, 120), width=4)
    try:
        f_big = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 150)
        f_mid = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 100)
        f_sm = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 56)
    except OSError:
        f_big = f_mid = f_sm = ImageFont.load_default()
    d.text((900, 520), "PHOTO", font=f_big, fill=(110, 110, 110), anchor="mm")
    d.text((900, 690), f"Figure {n}", font=f_mid, fill=(110, 110, 110), anchor="mm")
    note = (caption or "image file not on disk")[:70]
    d.text((900, 860), note, font=f_sm, fill=(90, 90, 90), anchor="mm")
    im.save(path, "PNG")
    return path

def word_picture_stream(path):
    """RGB JPEG/PNG bytes, always re-encoded through Pillow. Some source JPEGs
    (e.g. progressive with an embedded ICC profile right after SOI) parse fine
    in Pillow but trip python-docx's minimal header sniffer if passed through
    raw, and Word shows 8-bit grayscale (mode L) PNGs as missing, so every
    image is normalised here rather than passed through unmodified."""
    im = Image.open(path)
    im.load()
    suffix = os.path.splitext(path)[1].lower()
    if im.mode == "RGBA":
        bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[-1])
        im = bg
    elif im.mode != "RGB":
        im = im.convert("RGB")
    buf = io.BytesIO()
    if suffix in (".jpg", ".jpeg"):
        im.save(buf, format="JPEG", quality=90)
        buf.seek(0)
        return buf, "jpg"
    im.save(buf, format="PNG")
    buf.seek(0)
    return buf, "png"

# ---------------- parse markdown into blocks ----------------
def parse_all():
    files = PARTS
    blocks = []
    chapter = None          # current chapter number (0 for prologue)
    chapter_has_fig = {}
    in_appendix = False
    for fname in files:
        front = fname.startswith("00_")
        in_appendix = fname.startswith("12_")
        lines = open(os.path.join(SRC, fname), encoding="utf-8").read().splitlines()
        i = 0
        while i < len(lines):
            line = lines[i].rstrip()
            if not line.strip():
                i += 1; continue
            if front and line.startswith("# ") and not blocks:
                blocks.append(("title", line[2:].strip())); i += 1; continue
            if front and line.startswith("*") and line.endswith("*") and all(b[0] in ("title", "titleline") for b in blocks):
                blocks.append(("titleline", line.strip("*").strip())); i += 1; continue
            if line.strip() == "%%TOC%%":
                blocks.append(("toc",)); i += 1; continue
            if line.startswith("---"):
                blocks.append(("hr", front)); i += 1; continue
            if line.startswith("# "):
                t = line[2:].strip()
                blocks.append(("h1", t, "appendix" if in_appendix else "part"))
                i += 1; continue
            if line.startswith("## "):
                t = line[3:].strip()
                m = re.match(r"(\d+)\.\s", t)
                if front:
                    if t.lower().startswith("prologue"):
                        chapter = 0; chapter_has_fig[0] = False
                        blocks.append(("h2", t, "chapter", 0))
                    else:
                        blocks.append(("h1", t, "front"))
                elif in_appendix:
                    blocks.append(("h2", t, "appendix"))
                elif m:
                    chapter = int(m.group(1)); chapter_has_fig[chapter] = False
                    blocks.append(("h2", t, "chapter", chapter))
                else:
                    blocks.append(("h2", t, "other"))
                i += 1; continue
            if line.startswith("!["):
                if chapter is not None and chapter in FIG and not chapter_has_fig.get(chapter):
                    blocks.append(("fig", chapter)); chapter_has_fig[chapter] = True
                i += 1; continue
            if line.startswith("|"):
                rows = []
                while i < len(lines) and lines[i].startswith("|"):
                    r = lines[i].strip()
                    if not re.match(r"^\|\s*-", r):
                        rows.append([c.strip() for c in r.strip("|").split("|")])
                    i += 1
                blocks.append(("table", rows)); continue
            if re.match(r"^\s*[-*]\s+", line):
                items = []
                while i < len(lines) and re.match(r"^\s*[-*]\s+", lines[i]):
                    items.append(re.sub(r"^\s*[-*]\s+", "", lines[i]).strip()); i += 1
                blocks.append(("list", items)); continue
            # paragraph: gather until blank line
            para = [line]
            i += 1
            while i < len(lines) and lines[i].strip() and not re.match(r"^(#|!\[|\||---|%%)", lines[i]):
                para.append(lines[i].rstrip("\n")); i += 1
            blocks.append(("p", para))
    # chapters with no inline figure ref: add the plan figure at chapter end
    out = []
    cur = None
    for b in blocks:
        if b[0] in ("h1", "h2") and cur is not None and not chapter_has_fig.get(cur, True):
            out.append(("fig", cur)); chapter_has_fig[cur] = True
        if b[0] == "h2" and b[2] == "chapter":
            cur = b[3]
        elif b[0] in ("h1", "h2"):
            cur = None
        out.append(b)
    return out

# ---------------- inline formatting ----------------
TOKEN = re.compile(
    r"(\uE003"
    r"|\*\*.+?\*\*"
    r"|\*[^*\n]+?\*"
    r"|\^\{[^}]*\}"
    r"|\^[^\s\^_*(){}]+"
    r"|(?<=[A-Za-zα-ωΑ-Ωħℓ★₀-₉∫Σ])_\{[^}]*\}"
    r"|(?<=[A-Za-zα-ωΑ-Ωħℓ★∫Σ])_[A-Za-z0-9μνΛ★]+)"
)

def add_runs(par, text, bold=False, italic=False, sup=False, sub=False, size=None):
    pos = 0
    for m in TOKEN.finditer(text):
        if m.start() > pos:
            _run(par, text[pos:m.start()], bold, italic, sup, sub, size)
        tok = m.group(0)
        if tok.startswith("**"):
            add_runs(par, tok[2:-2], True, italic, sup, sub, size)
        elif tok.startswith("*"):
            add_runs(par, tok[1:-1], bold, True, sup, sub, size)
        elif tok.startswith("^"):
            inner = tok[2:-1] if tok.startswith("^{") else tok[1:]
            add_runs(par, inner, bold, italic, True, False, size)
        elif tok == "\uE003":
            _run(par, "*", bold, italic, False, True, size)
        elif tok.startswith("_"):
            inner = tok[2:-1] if tok.startswith("_{") else tok[1:]
            add_runs(par, inner, bold, italic, False, True, size)
        pos = m.end()
    if pos < len(text):
        _run(par, text[pos:], bold, italic, sup, sub, size)

def _run(par, s, bold, italic, sup, sub, size):
    if not s: return
    r = par.add_run(s)
    r.bold = bold or None
    r.italic = italic or None
    if sup: r.font.superscript = True
    if sub: r.font.subscript = True
    if size: r.font.size = Pt(size)
    return r

def plain_text(t):
    t = re.sub(r"\*\*(.+?)\*\*", r"\1", t)
    t = re.sub(r"(?<!\w)\*([^*\n]+?)\*(?!\w)", r"\1", t)
    return t

# ---------------- document helpers ----------------
_bm_id = [100]
def add_bookmark(par, name):
    _bm_id[0] += 1
    start = OxmlElement("w:bookmarkStart"); start.set(qn("w:id"), str(_bm_id[0])); start.set(qn("w:name"), name)
    end = OxmlElement("w:bookmarkEnd"); end.set(qn("w:id"), str(_bm_id[0]))
    par._p.insert(0, start); par._p.append(end)

def add_internal_link(par, text, anchor, bold=False, size=None):
    h = OxmlElement("w:hyperlink"); h.set(qn("w:anchor"), anchor); h.set(qn("w:history"), "1")
    r = OxmlElement("w:r"); rpr = OxmlElement("w:rPr")
    if bold:
        b = OxmlElement("w:b"); rpr.append(b)
    if size:
        sz = OxmlElement("w:sz"); sz.set(qn("w:val"), str(int(size*2))); rpr.append(sz)
    r.append(rpr)
    t = OxmlElement("w:t"); t.text = text; t.set(qn("xml:space"), "preserve"); r.append(t)
    h.append(r); par._p.append(h)

def page_break(doc):
    p = doc.add_paragraph(); p.add_run().add_break(WD_BREAK.PAGE)
    p.paragraph_format.space_after = Pt(0)

def set_style_font(style, name=BODY_FONT, size=11, bold=None, italic=None, color=None):
    style.font.name = name; style.font.size = Pt(size)
    if bold is not None: style.font.bold = bold
    if italic is not None: style.font.italic = italic
    if color is not None: style.font.color.rgb = color
    rpr = style.element.get_or_add_rPr()
    rf = rpr.find(qn("w:rFonts"))
    if rf is None:
        rf = OxmlElement("w:rFonts"); rpr.append(rf)
    for a in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
        rf.set(qn(a), name)
    for a in ("w:asciiTheme", "w:hAnsiTheme", "w:eastAsiaTheme", "w:cstheme"):
        if rf.get(qn(a)) is not None: del rf.attrib[qn(a)]

def setup_styles(doc):
    n = doc.styles["Normal"]; set_style_font(n, size=11)
    pf = n.paragraph_format; pf.first_line_indent = Inches(0.3); pf.space_after = Pt(0); pf.space_before = Pt(0); pf.line_spacing = 1.15
    h1 = doc.styles["Heading 1"]; set_style_font(h1, name=HEAD_FONT, size=18, bold=True, color=HEAD_COLOR)
    h1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER; h1.paragraph_format.space_before = Pt(60); h1.paragraph_format.space_after = Pt(24)
    h1.paragraph_format.first_line_indent = Inches(0); h1.paragraph_format.keep_with_next = True
    h2 = doc.styles["Heading 2"]; set_style_font(h2, name=HEAD_FONT, size=18, bold=True, color=HEAD_COLOR)
    h2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER; h2.paragraph_format.space_before = Pt(30); h2.paragraph_format.space_after = Pt(14)
    h2.paragraph_format.first_line_indent = Inches(0); h2.paragraph_format.keep_with_next = True
    from docx.enum.style import WD_STYLE_TYPE
    def mk(name, base="Normal"):
        try: st = doc.styles[name]
        except KeyError: st = doc.styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
        st.base_style = doc.styles[base]; return st
    fp = mk("First Paragraph"); fp.paragraph_format.first_line_indent = Inches(0)
    orn = mk("Ornament"); orn.paragraph_format.first_line_indent = Inches(0); orn.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    orn.paragraph_format.space_before = Pt(14); orn.paragraph_format.space_after = Pt(14); orn.paragraph_format.keep_with_next = True
    ni = mk("No Indent"); ni.paragraph_format.first_line_indent = Inches(0); ni.paragraph_format.space_after = Pt(6)
    cap = mk("Figure Caption"); set_style_font(cap, size=9.5, italic=True)
    cap.paragraph_format.first_line_indent = Inches(0); cap.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cap.paragraph_format.space_before = Pt(4); cap.paragraph_format.space_after = Pt(14)
    tp = mk("Title Page"); set_style_font(tp, name=HEAD_FONT, size=28, bold=True, color=HEAD_COLOR); tp.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    tp.paragraph_format.first_line_indent = Inches(0); tp.paragraph_format.space_before = Pt(140); tp.paragraph_format.space_after = Pt(18)
    ts = mk("Title Sub"); set_style_font(ts, size=14, italic=True); ts.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    ts.paragraph_format.first_line_indent = Inches(0); ts.paragraph_format.space_after = Pt(60)
    ta = mk("Title Author"); set_style_font(ta, size=13); ta.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER; ta.paragraph_format.first_line_indent = Inches(0)
    cp = mk("Copyright"); set_style_font(cp, size=9.5); cp.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cp.paragraph_format.first_line_indent = Inches(0); cp.paragraph_format.space_after = Pt(8)
    t1 = mk("TOC Part"); set_style_font(t1, size=11, bold=True); t1.paragraph_format.first_line_indent = Inches(0); t1.paragraph_format.space_before = Pt(8); t1.paragraph_format.space_after = Pt(2)
    t2 = mk("TOC Chapter"); set_style_font(t2, size=10.5); t2.paragraph_format.first_line_indent = Inches(0); t2.paragraph_format.left_indent = Inches(0.3); t2.paragraph_format.space_after = Pt(1)
    li = mk("List Item"); li.paragraph_format.first_line_indent = Inches(-0.2); li.paragraph_format.left_indent = Inches(0.4); li.paragraph_format.space_after = Pt(3)

def add_figure(doc, n):
    kind, caption = FIG[n]
    path, real = fig_path(n)
    if not path or not os.path.exists(path):
        path = make_slot_png(n, caption)
        real = False
    stream, ext = word_picture_stream(path)
    stream.name = f"figure_{n:02d}.{ext}"
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.first_line_indent = Inches(0); p.paragraph_format.space_before = Pt(10); p.paragraph_format.keep_with_next = True
    r = p.add_run(); shape = r.add_picture(stream, width=Inches(4.5))
    alt = f"Figure {n}. {caption}"[:120]
    shape._inline.docPr.set("descr", alt); shape._inline.docPr.set("title", f"Figure {n}")
    c = doc.add_paragraph(style="Figure Caption")
    c.add_run(f"Figure {n}. ").bold = True
    add_runs(c, caption)
    return not real

def add_table(doc, rows):
    if not rows: return
    ncol = max(len(r) for r in rows)
    t = doc.add_table(rows=len(rows), cols=ncol); t.style = "Table Grid"; t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for ri, row in enumerate(rows):
        for ci in range(ncol):
            cell = t.cell(ri, ci); cell.text = ""
            par = cell.paragraphs[0]; par.paragraph_format.first_line_indent = Inches(0); par.paragraph_format.line_spacing = 1.0
            add_runs(par, row[ci] if ci < len(row) else "", bold=(ri == 0), size=9)
    doc.add_paragraph(style="No Indent")

def build():
    blocks = parse_all()
    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Inches(6), Inches(9)
    for m in ("left_margin", "right_margin", "top_margin", "bottom_margin"): setattr(sec, m, Inches(0.75))
    setup_styles(doc)
    heads = []
    for b in blocks:
        if b[0] == "h1": heads.append(("part", b[1]))
        elif b[0] == "h2" and len(b) > 2 and b[2] in ("chapter", "appendix"): heads.append(("chapter", b[1]))
    anchors = {}; k = 0
    for kind, t in heads:
        k += 1; anchors[(kind, t)] = f"bm_{k:03d}"
    doc.add_paragraph(TITLE, style="Title Page")
    doc.add_paragraph(SUBTITLE, style="Title Sub")
    doc.add_paragraph(AUTHOR, style="Title Author")
    page_break(doc)
    missing_photos = []
    prev = "start"
    for b in blocks:
        kind = b[0]
        if kind in ("title", "titleline"): continue
        if kind == "toc":
            h = doc.add_paragraph("Contents", style="Heading 1"); add_bookmark(h, "toc")
            for hk, t in heads:
                if hk == "part":
                    p = doc.add_paragraph(style="TOC Part"); add_internal_link(p, plain_text(t), anchors[(hk, t)], bold=True)
                else:
                    p = doc.add_paragraph(style="TOC Chapter"); add_internal_link(p, plain_text(t), anchors[(hk, t)])
            prev = "toc"; continue
        if kind == "hr":
            if not b[1]:
                p = doc.add_paragraph(style="Ornament"); p.add_run("*   *   *")
                prev = "hr"
            continue
        if kind == "h1":
            page_break(doc)
            h = doc.add_paragraph(style="Heading 1"); add_runs(h, b[1]); add_bookmark(h, anchors[("part", b[1])])
            prev = "head"; continue
        if kind == "h2":
            is_chapterlike = len(b) > 2 and b[2] in ("chapter", "appendix")
            if is_chapterlike: page_break(doc)
            h = doc.add_paragraph(style="Heading 2"); add_runs(h, b[1])
            if is_chapterlike:
                add_bookmark(h, anchors[("chapter", b[1])])
            prev = "head"; continue
        if kind == "fig":
            if add_figure(doc, b[1]): missing_photos.append(b[1])
            prev = "fig"; continue
        if kind == "table":
            add_table(doc, b[1]); prev = "table"; continue
        if kind == "list":
            for it in b[1]:
                p = doc.add_paragraph(style="List Item"); p.add_run("-  "); add_runs(p, it)
            prev = "list"; continue
        if kind == "p":
            text = " ".join(l.strip() for l in b[1]) if not any(l.endswith("  ") for l in b[1]) else None
            if text is None:
                p = doc.add_paragraph(style="First Paragraph" if prev != "p" else "Normal")
                for j, l in enumerate(b[1]):
                    add_runs(p, l.strip())
                    if j < len(b[1]) - 1: p.add_run().add_break(WD_BREAK.LINE)
                prev = "p"; continue
            if text.startswith("**"):
                style = "No Indent"
            else:
                style = "First Paragraph" if prev != "p" else "Normal"
            p = doc.add_paragraph(style=style); add_runs(p, text)
            prev = "p"; continue
    doc.core_properties.title = TITLE; doc.core_properties.author = AUTHOR; doc.core_properties.subject = SUBTITLE
    doc.save(OUT)
    print("saved", OUT)
    print("figures:", len([b for b in blocks if b[0] == "fig"]), "photo slots still placeholders:", missing_photos)
    return OUT

if __name__ == "__main__":
    build()
