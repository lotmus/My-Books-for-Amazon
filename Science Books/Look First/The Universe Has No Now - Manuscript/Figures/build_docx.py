# Builds the Kindle-ready Word manuscript for "The Universe Has No Now"
# from the Markdown part files. One figure per chapter (Fig 0 + Fig 1-45), per 00_Figure_Plan.md.
# Photos: if figs/figNN.jpg exists it is used; otherwise figs/figNN_slot.png (framed placeholder).
import io, os, re, glob, sys
from PIL import Image, ImageDraw, ImageFont
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.dirname(HERE)  # was hardcoded to D:\...; now follows wherever this script actually lives
FIGS = os.path.join(HERE, "figs")
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "The Universe Has No Now - Kindle.docx")

TITLE = "The Universe Has No Now"
SUBTITLE = "Time, Origins, and Whether We Can Get Somewhere Else"
AUTHOR = "Lothar J. Musiol"
HEADLINE_FONT = "Amazon Ember"
# Deep navy, still blue, and not the pure #0000FF that reads as a hyperlink.
HEADLINE_BLUE = RGBColor(0x0C, 0x2D, 0x5A)
BODY_FONT = "Georgia"

# ---------------- figure table: number -> (kind, caption, credit-when-real) ----------------
FIG = {
 0: ("photo", "A kitchen clock on a bright wall. It is an excellent local tool; it says nothing about what is happening on Andromeda.", ""),
 1: ("photo", "One kitchen. Put two people in it, one walking and one standing still: they agree on the casserole; they do not share Andromeda’s now.", ""),
 2: ("diagram", "One event: a happening with four numbers, x, y, z and t. An event is not a rock.", ""),
 3: ("photo", "The Sun. Its light is eight minutes old by the time it reaches your eye.", "Credit: NASA/SDO"),
 4: ("photo", "The Andromeda Galaxy, cropped to its bright disk. Whatever is happening there now is two and a half million years from your yard.", "Credit: NASA/ESA"),
 5: ("diagram", "Two worldlines meet, split and meet again. The twin who travelled is younger: mileage through spacetime, not a trick.", ""),
 6: ("diagram", "The block: a loaf of all events. One thick thread is you. Past and future are directions on the loaf, not a moving edge.", ""),
 7: ("diagram", "A grid of dots that grows. Every dot sees the others recede; no dot is the center.", ""),
 8: ("photo", "A handful of distant galaxies, each still sharp. Almost every one is receding.", "Credit: NASA/ESA/STScI"),
 9: ("photo", "The microwave sky as a grayscale oval, warmer and cooler patches. This is a measurement, not a snapshot from a camera.", "Credit: ESA/Planck Collaboration"),
 10: ("diagram", "Four ticks on one line: one second, three minutes, 380,000 years, now. The temperature under each tick falls as the stretch grows.", ""),
 11: ("diagram", "A cubic meter of smoothed universe holds about one atom. Almost nothing, almost everywhere.", ""),
 12: ("diagram", "The last-scattering sky. Patches A and B on opposite sides never met in the plain hot bang, yet they match.", ""),
 13: ("diagram", "One curve: a steep burst, then a gentler slope. Inflation is the burst; everything else is after.", ""),
 14: ("photo", "A nearby spiral galaxy, NGC 4414, filling the frame. A quantum twitch, stretched and pulled for thirteen billion years.", "Credit: NASA/ESA/Hubble Heritage Team (STScI/AURA)"),
 15: ("diagram", "Three bubbles in a field that keeps stretching. A picture of a possibility, not a photograph.", ""),
 16: ("photo", "The whole sky as a map of a million galaxies from the 2MASS survey. The band across the middle is our own Milky Way blocking the view; the clumps and filaments everywhere else are the web grown from twitches. The small labels name nearby clusters and can be ignored.", "Credit: NASA/JPL-Caltech/IPAC (2MASS)"),
 17: ("photo", "The Bullet Cluster as one composite: hot gas piled in the middle; mass, mapped by lensing, on either side. The pull did not stay with the gas.", "Credit: NASA/CXC/CfA/M. Markevitch et al.; NASA/STScI; ESO WFI"),
 18: ("photo", "A supernova remnant, the Crab Nebula. Explosions of a related kind, seen much farther off, taught us the stretch is speeding up.", "Credit: NASA/ESA/J. Hester and A. Loll (Arizona State University)"),
 19: ("diagram", "Three futures for the size of the universe: recollapse, coast, accelerate. The curve marked data is the accelerating one.", ""),
 20: ("photo", "The ring and dark center of M87*. The shadow of a one-way surface.", "Credit: EHT Collaboration"),
 21: ("diagram", "Two clocks, one lower in a gravity well. The lower face runs slow.", ""),
 22: ("diagram", "The Kruskal map as four rooms: two outsides, a black hole, a white hole. We live in one of the outsides.", ""),
 23: ("diagram", "A sphere with hash marks on the skin only. A black hole’s entropy counts area, not volume.", ""),
 24: ("photo", "The bright host galaxy M87, with a jet thrown out from its center. A real black hole lives there. It is still not a door.", "Credit: NASA/Hubble Heritage Team (STScI/AURA)"),
 25: ("photo", "The rover Perseverance, large in frame, on dusty ground; the small helicopter behind it is Ingenuity. Dirt, delay, no magic.", "Credit: NASA/JPL-Caltech/MSSS"),
 26: ("diagram", "Two horizons on a simple spacetime wedge: the particle horizon is what we can see; the event horizon is what can still reach us.", ""),
 27: ("diagram", "A star, a planet crossing it, and a light curve with a square bite. The planet is the bite, not a painting.", ""),
 28: ("diagram", "A hatched band around a star where liquid water can last. Earth is in the band; Mars sits on the rim.", ""),
 29: ("photo", "Europa’s ice, cracks readable in gray. A windshield that heals because a sea kneads it from below.", "Credit: NASA/JPL-Caltech/SETI Institute"),
 30: ("diagram", "Two trunks: Earth’s tree of life solid, a second trunk dotted. Sample size: one.", ""),
 31: ("photo", "A tractor working a field, with no one you can see in the seat. Patience is the picture. The crew that can wait is that patience, off the Earth, with a spare for every bit the rays flip.", ""),
 32: ("photo", "A vault door in snow. A library is a physical object.", ""),
 33: ("diagram", "Two large circles joined by a short, fat handle: here and there. A wormhole would be a handle on the block, not a subway.", ""),
 34: ("photo", "A radio dish with ground in the frame. A signal is light, and light is late.", ""),
 35: ("diagram", "A worldline that meets itself. Same events, not a rewrite.", ""),
 36: ("diagram", "A loaf in slices. No one walks between the slices.", ""),
 37: ("diagram", "Four kinds of elsewhere in a two-by-two: more space, other bubbles, other branches, other math.", ""),
 38: ("diagram", "Identical rooms receding. A picture of a possibility, not a photograph of copies.", ""),
 39: ("diagram", "Three bubbles, three different icons. Other rooms, other rules, unphotographed.", ""),
 40: ("diagram", "One line splits into two that never rejoin. Every allowed outcome, one worldline each.", ""),
 41: ("photo", "Earth, bright against a dead horizon. A temperate world is where observers find themselves.", "Credit: NASA"),
 42: ("photo", "One Galápagos finch on a light ground, beak readable. A filter can look like a craftsman.", ""),
 43: ("diagram", "Five rows, one word each: Freeze, Rip, Crunch, Decay, Bounce.", ""),
 44: ("diagram", "A clock face dissolving into marks. A clock is a habit of events, not a river.", ""),
 45: ("photo", "Rover tracks toward a near horizon. Meaning is local, on one worldline.", "Credit: NASA/JPL-Caltech"),
}

def fig_path(n):
    kind = FIG[n][0]
    if kind == "photo":
        for ext in ("jpg", "jpeg", "png"):
            p = os.path.join(FIGS, f"fig{n:02d}.{ext}")
            if os.path.exists(p): return p, True
        return os.path.join(FIGS, f"fig{n:02d}_slot.png"), False
    p = os.path.join(FIGS, f"fig{n:02d}.png")
    return p, os.path.exists(p)

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
    """RGB JPEG/PNG bytes. Word often shows 8-bit grayscale (mode L) PNGs as missing."""
    im = Image.open(path)
    suffix = os.path.splitext(path)[1].lower()
    if im.mode == "RGB" and suffix in (".jpg", ".jpeg"):
        with open(path, "rb") as f:
            return io.BytesIO(f.read()), "jpg"
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
    files = ["00_Front_Matter.md"] + sorted(os.path.basename(f) for f in glob.glob(os.path.join(SRC, "0[1-9]_*.md")) + glob.glob(os.path.join(SRC, "10_*.md"))) + ["11_Appendix.md"]
    blocks = []
    chapter = None          # current popular chapter number (0 for prologue)
    chapter_has_fig = {}
    in_appendix = False
    for fname in files:
        front = fname.startswith("00_")
        in_appendix = fname.startswith("11_")
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
                blocks.append(("hr",)); i += 1; continue
            if line.startswith("# "):
                t = line[2:].strip()
                blocks.append(("h1", t, "appendix" if in_appendix else "part")); i += 1; continue
            if line.startswith("## "):
                t = line[3:].strip()
                m = re.match(r"(\d+)\.\s", t)
                if front:
                    if t.lower().startswith("prologue"):
                        chapter = 0; chapter_has_fig[0] = False
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
            # paragraph: gather until blank line (markdown two-space line breaks are kept as breaks)
            para = [line]
            i += 1
            while i < len(lines) and lines[i].strip() and not re.match(r"^(#|!\[|\||---|%%)", lines[i]):
                para.append(lines[i].rstrip("\n")); i += 1
            blocks.append(("p", para))
    # chapters with no inline figure ref (e.g. 14): add the plan figure at chapter end
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


SUP_DIGITS = str.maketrans("0123456789+-", "\u2070\u00b9\u00b2\u00b3\u2074\u2075\u2076\u2077\u2078\u2079\u207a\u207b")
def to_sup(t):
    return t.translate(SUP_DIGITS)
SUP_NEST = re.compile(r"\^\{(\d+)\^\{([\d+\-]+)\}\}")      # 10^{10^{86}} -> 10^{10⁸⁶}
ITAL_SUB_STAR = re.compile(r"\*([A-Za-z])_\*\*?")
SUB_STAR = re.compile(r"(?<=[A-Za-z])_\*")               # g_* outside italics -> g with subscript *

def add_runs(par, text, bold=False, italic=False, sup=False, sub=False, size=None):
    text = text.replace("M87*", "M87")
    text = text.replace("Sgr A*", "Sgr A").replace("Sagittarius A*", "Sagittarius A")
    text = SUP_NEST.sub(lambda m: "^{" + m.group(1) + to_sup(m.group(2)) + "}", text)
    text = ITAL_SUB_STAR.sub(lambda m: "*" + m.group(1) + "*\uE003", text)   # *z_** or *z_* -> italic z, subscript *
    text = SUB_STAR.sub("\uE003", text)
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

def _emit(par, s, bold, italic, sup, sub, size):
    if not s: return
    r = par.add_run(s.replace("", "*"))
    r.bold = bold or None
    r.italic = italic or None
    if sup: r.font.superscript = True
    if sub: r.font.subscript = True
    if size: r.font.size = Pt(size)
    return r

def _run(par, s, bold, italic, sup, sub, size):
    if not s: return
    if not XREF_ANCHORS or not XREF_RE.search(s):
        _emit(par, s, bold, italic, sup, sub, size)
        return
    pos = 0
    for m in XREF_RE.finditer(s):
        if m.start() > pos:
            _emit(par, s[pos:m.start()], bold, italic, sup, sub, size)
        if m.group(2):
            key, label = m.group(2), m.group(1) + m.group(2)
        elif m.group(4):
            key, label = m.group(4), m.group(3) + m.group(4)
        elif m.group(6):
            key, label = m.group(6), m.group(5) + m.group(6)
        else:
            key, label = m.group(8), m.group(8)
        anchor = XREF_ANCHORS.get(key)
        if anchor:
            add_internal_link(par, label, anchor, bold=bold, size=size)
        else:
            _emit(par, label, bold, italic, sup, sub, size)
        pos = m.end()
    if pos < len(s):
        _emit(par, s[pos:], bold, italic, sup, sub, size)

def plain_text(t):
    """Heading text without markdown emphasis markers (for TOC links and bookmarks)."""
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
    color = OxmlElement("w:color"); color.set(qn("w:val"), "0563C1"); rpr.append(color)
    u = OxmlElement("w:u"); u.set(qn("w:val"), "single"); rpr.append(u)
    r.append(rpr)
    t = OxmlElement("w:t"); t.text = text; t.set(qn("xml:space"), "preserve"); r.append(t)
    h.append(r); par._p.append(h)

# Filled in build() from heading bookmarks. Keys: "31", "A31".
XREF_ANCHORS = {}
XREF_RE = re.compile(r"(Chapter\s+)(\d+)|(\bAppendix\s+)(A\d+)|(\bCh\.\s*)(\d+)|(\b)(A\d+)(?=\b)")

def page_break(doc):
    p = doc.add_paragraph(); p.add_run().add_break(WD_BREAK.PAGE)
    p.paragraph_format.space_after = Pt(0)

def set_style_font(style, name=BODY_FONT, size=11, bold=None, italic=None):
    style.font.name = name; style.font.size = Pt(size)
    if bold is not None: style.font.bold = bold
    if italic is not None: style.font.italic = italic
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
    n.font.color.rgb = None
    h1 = doc.styles["Heading 1"]; set_style_font(h1, name=HEADLINE_FONT, size=20, bold=True)
    h1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER; h1.paragraph_format.space_before = Pt(60); h1.paragraph_format.space_after = Pt(24)
    h1.paragraph_format.first_line_indent = Inches(0); h1.paragraph_format.keep_with_next = True
    h2 = doc.styles["Heading 2"]; set_style_font(h2, name=HEADLINE_FONT, size=18, bold=True)
    h2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER; h2.paragraph_format.space_before = Pt(30); h2.paragraph_format.space_after = Pt(14)
    h2.paragraph_format.first_line_indent = Inches(0); h2.paragraph_format.keep_with_next = True
    for s in (h1, h2):
        # Headlines, big (Part) or small (Chapter): the author's reference blue.
        s.font.color.rgb = HEADLINE_BLUE
        rpr = s.element.get_or_add_rPr()
        c = rpr.find(qn("w:color"))
        if c is None:
            c = OxmlElement("w:color"); rpr.append(c)
        c.set(qn("w:val"), "%02X%02X%02X" % (HEADLINE_BLUE[0], HEADLINE_BLUE[1], HEADLINE_BLUE[2]))
    from docx.enum.style import WD_STYLE_TYPE
    def mk(name, base="Normal"):
        try: st = doc.styles[name]
        except KeyError: st = doc.styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
        st.base_style = doc.styles[base]; return st
    fp = mk("First Paragraph"); fp.paragraph_format.first_line_indent = Inches(0)
    ni = mk("No Indent"); ni.paragraph_format.first_line_indent = Inches(0); ni.paragraph_format.space_after = Pt(6)
    eq = mk("Equation"); eq.paragraph_format.first_line_indent = Inches(0); eq.paragraph_format.left_indent = Inches(0.3)
    eq.paragraph_format.space_before = Pt(6); eq.paragraph_format.space_after = Pt(6)
    cap = mk("Figure Caption"); set_style_font(cap, size=9.5, italic=True)
    cap.paragraph_format.first_line_indent = Inches(0); cap.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cap.paragraph_format.space_before = Pt(4); cap.paragraph_format.space_after = Pt(14)
    cr = mk("Figure Credit"); set_style_font(cr, size=8.5, italic=False)
    cr.paragraph_format.first_line_indent = Inches(0); cr.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER; cr.paragraph_format.space_after = Pt(14)
    tp = mk("Title Page"); set_style_font(tp, size=28, bold=True); tp.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
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
    kind, caption, credit = FIG[n]
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
    c.add_run(f"Figure {n}. ").italic = False
    c.runs[0].bold = True
    add_runs(c, caption)
    # Credits live in the Amazon product description only — not under figures.
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
    # collect headings for the TOC
    heads = []
    for b in blocks:
        if b[0] == "h1": heads.append(("part", b[1]))
        elif b[0] == "h2": heads.append(("chapter", b[1]))
    anchors = {}; k = 0
    XREF_ANCHORS.clear()
    for kind, t in heads:
        k += 1
        name = f"bm_{k:03d}"
        anchors[(kind, t)] = name
        pt = plain_text(t)
        m = re.match(r"(\d+)\.\s", pt)
        if m:
            XREF_ANCHORS[m.group(1)] = name
        m = re.match(r"(A\d+)\.", pt)
        if m:
            XREF_ANCHORS[m.group(1)] = name
    # title page
    titlelines = [b[1] for b in blocks if b[0] == "titleline"]
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
            page_break(doc)
            h = doc.add_paragraph("Contents", style="Heading 1"); add_bookmark(h, "toc")
            for hk, t in heads:
                if hk == "part":
                    p = doc.add_paragraph(style="TOC Part"); add_internal_link(p, plain_text(t), anchors[(hk, t)], bold=True)
                else:
                    p = doc.add_paragraph(style="TOC Chapter"); add_internal_link(p, plain_text(t), anchors[(hk, t)])
            prev = "toc"; continue
        if kind == "hr":
            continue
        if kind == "h1":
            page_break(doc)
            h = doc.add_paragraph(style="Heading 1"); add_runs(h, b[1]); add_bookmark(h, anchors[("part", b[1])])
            prev = "head"; continue
        if kind == "h2":
            # Bug fixed 26 Sep 2026: this used to only break before b[2]=="chapter"
            # (the 45 numbered popular chapters), silently skipping every appendix
            # note (b[2]=="appendix": A0-A45) and every other H2 (b[2]=="other":
            # How to Read These Notes, Equations at a Glance, Further Reading,
            # Glossary) -- 51 headings in total ran on with no page break.
            if b[2] in ("chapter", "appendix", "other"): page_break(doc)
            h = doc.add_paragraph(style="Heading 2"); add_runs(h, b[1]); add_bookmark(h, anchors[("chapter", b[1])])
            prev = "head"; continue
        if kind == "fig":
            if add_figure(doc, b[1]): missing_photos.append(b[1])
            prev = "fig"; continue
        if kind == "table":
            add_table(doc, b[1]); prev = "table"; continue
        if kind == "list":
            for it in b[1]:
                p = doc.add_paragraph(style="List Item"); p.add_run("•  "); add_runs(p, it)
            prev = "list"; continue
        if kind == "p":
            text = " ".join(l.strip() for l in b[1]) if not any(l.endswith("  ") for l in b[1]) else None
            if text is None:
                # markdown hard line breaks: keep them
                p = doc.add_paragraph(style="First Paragraph" if prev != "p" else "Normal")
                for j, l in enumerate(b[1]):
                    add_runs(p, l.strip())
                    if j < len(b[1]) - 1: p.add_run().add_break(WD_BREAK.LINE)
                prev = "p"; continue
            if re.match(r"^\*\*\(\d+\)\*\*", text):
                style = "Equation"
            elif text.startswith("**") or text.startswith("*(") or text.lower().startswith("*where"):
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
