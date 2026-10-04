# Kindle-ready Word manuscript for "A Trip Is Not a New Life".
# 6x9 in, Georgia body, Amazon Ember headlines, one figure per chapter.
# Run: python Figures\build_docx.py
import io, os, re, glob, sys
from PIL import Image, ImageDraw, ImageFont
from docx import Document
from docx.shared import Pt, Inches, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.opc.constants import RELATIONSHIP_TYPE as RT

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.dirname(HERE)
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(SRC, "A Trip Is Not a New Life - Kindle.docx")

TITLE = "A Trip Is Not a New Life"
SUBTITLE = "Camps, the Body, and the Earth You Do Not Abandon"
AUTHOR = "Lothar J. Musiol"
HEADLINE_FONT = "Amazon Ember"
HEADLINE_BLUE = RGBColor(0x00, 0x00, 0xFF)
BODY_FONT = "Georgia"

# Real photographs. Everything else is a line diagram, so a .png wins when both exist.
PREFER_JPG = {13, 27}

FIG_LINE = re.compile(r"^Figure\s+(\d+)\.\s+(.+)$")
IMG_LINE = re.compile(r"^!\[Figure\s+(\d+)\.\s*(.*?)\]\(([^)]+)\)\s*$")
NOTE_LINE = re.compile(r"^(A\d+(?:\s*/\s*A\d+)?\.\s+.+)$")
APPENDIX_HEADS = (
    "How to Read These Notes",
    "How to Read the Body Notes",
    "APPENDIX — The Scientific Detail",
    "APPENDIX — The Body Notes",
    "Equations at a Glance",
    "Equations at a Glance, Continued",
    "Further Reading (tiered)",
    "Glossary",
)
CH_ANCHORS = {}
NOTE_ANCHORS = {}
NOTE_LINK = re.compile(
    r"Appendix\s+A(\d+)|[Ss]ee\s+A(\d+)|\(A(\d+)\)|(?<!Book 1 )Chapter\s+(\d+)"
    r"|\[\^([\w-]+)\]|(?<![\w.])Figure\s+(\d+[a-z]?)\b(?!\.\s)"
)
MARKER = re.compile(r"\[\^([\w-]+)\]")
NOTE_TEXT = {}
NOTE_NUM = {}
REF_PLACED = set()
FIG_ANCHORS = {}


def font(name, size):
    path = os.path.join("C:/Windows/Fonts", name)
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default()


def new_canvas():
    im = Image.new("RGB", (1800, 1200), (255, 255, 255))
    return im, ImageDraw.Draw(im)


def save_fig(im, n):
    path = os.path.join(HERE, f"fig{n:02d}.png")
    im.save(path, "PNG")
    return path


def punch(d, text, f):
    d.text((900, 1100), text, font=f, fill=(0, 0, 0), anchor="mm")


def draw_long_ticket():
    """Figures 25 and 26 were photographs of Earth standing in for the mechanism."""
    f_lab = font("arial.ttf", 36)
    f_sm = font("arial.ttf", 28)
    f_big = font("arialbd.ttf", 40)
    lw = 8
    if not os.path.isfile(os.path.join(HERE, "fig25.png")):
        im, d = new_canvas()
        d.line([(180, 700), (980, 540), (980, 760), (180, 760), (180, 700)], fill=(0, 0, 0), width=lw)
        d.text((560, 680), "craft", font=f_lab, fill=(0, 0, 0), anchor="mm")
        d.line([(1040, 180), (900, 540)], fill=(0, 0, 0), width=6)
        d.ellipse([1000, 120, 1120, 240], outline=(0, 0, 0), width=lw)
        d.text((1060, 90), "dust", font=f_sm, fill=(0, 0, 0), anchor="mm")
        d.rectangle([1180, 460, 1620, 860], outline=(0, 0, 0), width=lw)
        d.text((1400, 660), "library", font=f_lab, fill=(0, 0, 0), anchor="mm")
        punch(d, "a machine can wait", f_big)
        save_fig(im, 25)
    if not os.path.isfile(os.path.join(HERE, "fig26.png")):
        im, d = new_canvas()
        d.rectangle([160, 340, 520, 920], outline=(0, 0, 0), width=lw)
        d.line([(160, 340), (240, 250), (600, 250), (520, 340)], fill=(0, 0, 0), width=lw)
        d.line([(600, 250), (600, 830), (520, 920)], fill=(0, 0, 0), width=lw)
        d.text((340, 640), "sequence", font=f_sm, fill=(0, 0, 0), anchor="mm")
        d.rectangle([740, 460, 1240, 1020], outline=(0, 0, 0), width=lw)
        d.text((990, 740), "wet lab", font=f_lab, fill=(0, 0, 0), anchor="mm")
        d.ellipse([1360, 260, 1680, 580], outline=(0, 0, 0), width=lw)
        d.line([(1360, 420), (1680, 420)], fill=(0, 0, 0), width=lw)
        d.text((1520, 500), "sea", font=f_lab, fill=(0, 0, 0), anchor="mm")
        d.text((1520, 660), "shut", font=f_sm, fill=(0, 0, 0), anchor="mm")
        punch(d, "look first", f_big)
        save_fig(im, 26)


def draw_missing():
    """Classroom diagrams 17-24 and closing diagrams 43-46 were never on disk."""
    draw_long_ticket()
    f_lab = font("arial.ttf", 36)
    f_sm = font("arial.ttf", 28)
    f_big = font("arialbd.ttf", 40)
    lw = 8

    def need(n):
        return resolve_fig(n) is None

    if need(17):
        im, d = new_canvas()
        d.rounded_rectangle([180, 180, 780, 980], radius=80, outline=(0, 0, 0), width=lw)
        d.polygon([(420, 180), (500, 80), (620, 180)], outline=(0, 0, 0))
        d.line([(500, 80), (620, 180)], fill=(0, 0, 0), width=lw)
        d.text((480, 900), "glove", font=f_lab, fill=(0, 0, 0), anchor="mm")
        d.line([(700, 560), (860, 560)], fill=(0, 0, 0), width=4)
        d.text((780, 520), "seam", font=f_sm, fill=(0, 0, 0), anchor="mm")
        d.polygon([(1100, 280), (1280, 700), (980, 640)], outline=(0, 0, 0))
        d.line([(1100, 280), (1280, 700), (980, 640), (1100, 280)], fill=(0, 0, 0), width=lw)
        d.text((1140, 780), "grain, larger than the seam", font=f_lab, fill=(0, 0, 0), anchor="mm")
        punch(d, "the workplace is the glove", f_big)
        save_fig(im, 17)

    if need(18):
        im, d = new_canvas()
        d.line([(80, 700), (1720, 700)], fill=(0, 0, 0), width=lw)
        d.pieslice([1180, 520, 1500, 840], 180, 360, outline=(0, 0, 0), width=lw)
        d.text((1340, 900), "sun, set", font=f_lab, fill=(0, 0, 0), anchor="mm")
        d.rectangle([260, 360, 620, 700], outline=(0, 0, 0), width=lw)
        d.ellipse([400, 460, 480, 540], outline=(0, 0, 0), width=lw)
        d.text((440, 280), "tin", font=f_lab, fill=(0, 0, 0), anchor="mm")
        d.text((440, 620), "lamp", font=f_sm, fill=(0, 0, 0), anchor="mm")
        punch(d, "the night is a cargo problem", f_big)
        save_fig(im, 18)

    if need(19):
        im, d = new_canvas()
        d.ellipse([80, 280, 700, 900], outline=(0, 0, 0), width=lw)
        d.text((390, 200), "crater", font=f_lab, fill=(0, 0, 0), anchor="mm")
        d.rectangle([300, 520, 340, 780], outline=(0, 0, 0), width=lw)
        d.polygon([(280, 520), (360, 520), (320, 440)], outline=(0, 0, 0))
        d.line([(280, 520), (320, 440), (360, 520)], fill=(0, 0, 0), width=lw)
        d.text((320, 860), "drill", font=f_sm, fill=(0, 0, 0), anchor="mm")
        d.rectangle([1100, 480, 1500, 820], outline=(0, 0, 0), width=lw)
        d.ellipse([1220, 400, 1380, 520], outline=(0, 0, 0), width=lw)
        d.text((1300, 900), "tank", font=f_lab, fill=(0, 0, 0), anchor="mm")
        d.line([(400, 480), (1080, 620)], fill=(0, 0, 0), width=4)
        d.polygon([(1080, 620), (1000, 590), (1020, 670)], fill=(0, 0, 0))
        d.text((740, 500), "smaller than the drill", font=f_sm, fill=(0, 0, 0), anchor="mm")
        punch(d, "the ratio", f_big)
        save_fig(im, 19)

    if need(20):
        im, d = new_canvas()
        d.ellipse([180, 280, 700, 900], outline=(0, 0, 0), width=lw)
        for y in (420, 540, 660):
            d.line([(280, y), (600, y)], fill=(0, 0, 0), width=4)
        d.text((440, 200), "boot print, still sharp", font=f_lab, fill=(0, 0, 0), anchor="mm")
        d.ellipse([1050, 340, 1550, 840], outline=(0, 0, 0), width=lw)
        d.ellipse([1260, 550, 1340, 630], fill=(0, 0, 0))
        d.text((1300, 200), "seal", font=f_lab, fill=(0, 0, 0), anchor="mm")
        d.text((1300, 920), "a grain in it", font=f_sm, fill=(0, 0, 0), anchor="mm")
        punch(d, "no wind, no wash", f_big)
        save_fig(im, 20)

    if need(21):
        im, d = new_canvas()
        d.rectangle([200, 520, 780, 980], outline=(0, 0, 0), width=lw)
        d.polygon([(200, 520), (280, 280), (490, 180), (700, 300), (780, 520)], outline=(0, 0, 0))
        d.line([(200, 520), (280, 280), (490, 180), (700, 300), (780, 520)], fill=(0, 0, 0), width=lw)
        d.text((490, 400), "hat of dirt", font=f_lab, fill=(0, 0, 0), anchor="mm")
        d.text((490, 760), "tin", font=f_lab, fill=(0, 0, 0), anchor="mm")
        d.ellipse([1200, 160, 1520, 480], outline=(0, 0, 0), width=lw)
        for ang in ((1100, 300, 1180, 340), (1360, 80, 1360, 140), (1560, 220, 1660, 180), (1560, 420, 1680, 460)):
            d.line([ang[:2], ang[2:]], fill=(0, 0, 0), width=4)
        d.text((1360, 560), "sun, as a shower", font=f_lab, fill=(0, 0, 0), anchor="mm")
        punch(d, "the hat is mass", f_big)
        save_fig(im, 21)

    if need(22):
        im, d = new_canvas()
        d.ellipse([80, 420, 360, 700], outline=(0, 0, 0), width=lw)
        d.text((220, 560), "Earth", font=f_lab, fill=(0, 0, 0), anchor="mm")
        d.ellipse([1280, 180, 1480, 380], outline=(0, 0, 0), width=lw)
        d.text((1380, 280), "Moon", font=f_sm, fill=(0, 0, 0), anchor="mm")
        d.arc([200, 200, 1400, 900], 200, 340, fill=(0, 0, 0), width=lw)
        d.text((700, 240), "free return", font=f_lab, fill=(0, 0, 0), anchor="mm")
        d.arc([360, 480, 1600, 1100], 300, 80, fill=(0, 0, 0), width=6)
        d.text((1500, 780), "does not return", font=f_sm, fill=(0, 0, 0), anchor="mm")
        punch(d, "kindness is a burn you can skip", f_big)
        save_fig(im, 22)

    if need(23):
        im, d = new_canvas()
        d.ellipse([350, 160, 1450, 980], outline=(0, 0, 0), width=lw)
        d.text((900, 100), "crater", font=f_lab, fill=(0, 0, 0), anchor="mm")
        for x, y in ((620, 420), (900, 360), (1100, 520), (780, 680), (1040, 740)):
            d.line([(x - 24, y - 24), (x + 24, y + 24)], fill=(0, 0, 0), width=6)
            d.line([(x - 24, y + 24), (x + 24, y - 24)], fill=(0, 0, 0), width=6)
        d.text((900, 900), "marks, and no fence", font=f_lab, fill=(0, 0, 0), anchor="mm")
        punch(d, "use is not title", f_big)
        save_fig(im, 23)

    if need(24):
        im, d = new_canvas()
        def coins(x, n, label):
            for i in range(n):
                y = 860 - i * 36
                d.ellipse([x, y, x + 220, y + 50], outline=(0, 0, 0), width=6)
            d.text((x + 110, 960), label, font=f_lab, fill=(0, 0, 0), anchor="mm")
        coins(120, 3, "program")
        coins(560, 6, "city")
        coins(1100, 14, "the staffed world")
        punch(d, "do not swap the piles", f_big)
        save_fig(im, 24)

    if need(30):
        im, d = new_canvas()
        # mouse climbs fast, human at midlife, mole rat flat, shark barely rises
        curves = [
            ("mouse", [(160, 900), (280, 820), (400, 500), (520, 180)]),
            ("human", [(560, 900), (720, 860), (880, 700), (1040, 280)]),
            ("mole rat", [(1080, 900), (1240, 860), (1400, 840), (1560, 820)]),
            ("shark", [(160, 980), (560, 960), (1000, 940), (1560, 920)]),
        ]
        d.line([(120, 160), (120, 980), (1700, 980)], fill=(0, 0, 0), width=lw)
        d.text((80, 140), "hazard", font=f_sm, fill=(0, 0, 0), anchor="lm")
        colors_y = [200, 280, 860, 860]
        for (name, pts), _ in zip(curves[:3], colors_y):
            d.line(pts, fill=(0, 0, 0), width=lw)
        d.line(curves[3][1], fill=(0, 0, 0), width=5)
        d.text((400, 140), "mouse", font=f_lab, fill=(0, 0, 0), anchor="mm")
        d.text((900, 240), "human", font=f_lab, fill=(0, 0, 0), anchor="mm")
        d.text((1400, 760), "mole rat", font=f_lab, fill=(0, 0, 0), anchor="mm")
        d.text((520, 860), "shark", font=f_sm, fill=(0, 0, 0), anchor="mm")
        punch(d, "none of them touch zero", f_big)
        save_fig(im, 30)

    if need(32):
        im, d = new_canvas()
        d.ellipse([180, 220, 780, 820], outline=(0, 0, 0), width=lw)
        d.line([(480, 520), (620, 340)], fill=(0, 0, 0), width=lw)
        d.polygon([(620, 340), (560, 360), (600, 420)], fill=(0, 0, 0))
        d.text((480, 900), "pushed back, then stopped", font=f_sm, fill=(0, 0, 0), anchor="mm")
        d.line([(980, 180), (980, 980)], fill=(0, 0, 0), width=lw)
        for y in range(180, 981, 40):
            d.line([(980, y), (1040, y + 20)], fill=(0, 0, 0), width=4)
        d.text((1100, 560), "fence", font=f_lab, fill=(0, 0, 0), anchor="lm")
        d.rectangle([1320, 360, 1680, 900], outline=(0, 0, 0), width=lw)
        d.text((1500, 600), "identity", font=f_lab, fill=(0, 0, 0), anchor="mm")
        d.text((1500, 660), "lost", font=f_lab, fill=(0, 0, 0), anchor="mm")
        punch(d, "past the fence, the door has no name you want", f_big)
        save_fig(im, 32)

    if need(40):
        im, d = new_canvas()
        d.line([(200, 160), (200, 1000)], fill=(0, 0, 0), width=lw)
        d.polygon([(200, 160), (170, 220), (230, 220)], fill=(0, 0, 0))
        d.text((200, 110), "time", font=f_lab, fill=(0, 0, 0), anchor="mm")
        d.ellipse([160, 860, 240, 940], fill=(0, 0, 0))
        d.ellipse([160, 240, 240, 320], fill=(0, 0, 0))
        d.line([(200, 900), (200, 280)], fill=(0, 0, 0), width=lw)
        d.text((360, 560), "stays", font=f_lab, fill=(0, 0, 0), anchor="lm")
        d.text((360, 620), "clock reads most", font=f_sm, fill=(0, 0, 0), anchor="lm")
        d.line([(200, 900), (900, 700), (1400, 500), (200, 280)], fill=(0, 0, 0), width=6)
        d.text((1100, 760), "turned around", font=f_lab, fill=(0, 0, 0), anchor="mm")
        d.text((1100, 820), "reads less", font=f_sm, fill=(0, 0, 0), anchor="mm")
        punch(d, "the straight path is the one that stays", f_big)
        save_fig(im, 40)

    if need(41):
        im, d = new_canvas()
        d.ellipse([200, 180, 700, 680], outline=(0, 0, 0), width=lw)
        d.ellipse([400, 380, 500, 480], fill=(0, 0, 0))
        d.line([(450, 430), (620, 280)], fill=(0, 0, 0), width=lw)
        d.text((260, 300), "on", font=f_lab, fill=(0, 0, 0), anchor="mm")
        d.text((620, 560), "low", font=f_lab, fill=(0, 0, 0), anchor="mm")
        d.text((450, 760), "furnace", font=f_lab, fill=(0, 0, 0), anchor="mm")
        def glass(x, label, sand_top):
            d.polygon([(x, 200), (x + 220, 200), (x + 140, 480), (x + 80, 480)], outline=(0, 0, 0))
            d.line([(x, 200), (x + 220, 200), (x + 140, 480), (x + 80, 480), (x, 200)], fill=(0, 0, 0), width=lw)
            d.polygon([(x + 80, 520), (x + 140, 520), (x + 220, 800), (x, 800)], outline=(0, 0, 0))
            d.line([(x + 80, 520), (x + 140, 520), (x + 220, 800), (x, 800), (x + 80, 520)], fill=(0, 0, 0), width=lw)
            d.text((x + 110, 880), label, font=f_sm, fill=(0, 0, 0), anchor="mm")
        glass(980, "drains", True)
        glass(1360, "drains slower", False)
        d.polygon([(1020, 240), (1160, 240), (1100, 400)], fill=(0, 0, 0))
        d.polygon([(1400, 620), (1560, 760), (1380, 760)], fill=(180, 180, 180))
        punch(d, "neither one stopped", f_big)
        save_fig(im, 41)

    if need(43):
        im, d = new_canvas()
        d.rectangle([480, 80, 1320, 1000], outline=(0, 0, 0), width=lw)
        d.text((900, 160), "receipt", font=f_big, fill=(0, 0, 0), anchor="mm")
        for i, line in enumerate(("trial", "harm", "zip code")):
            y = 300 + i * 140
            d.text((620, y), line, font=f_lab, fill=(0, 0, 0), anchor="lm")
            d.line([(620, y + 56), (1180, y + 56)], fill=(0, 0, 0), width=3)
        d.text((620, 760), "local fix", font=f_big, fill=(0, 0, 0), anchor="lm")
        d.line([(620, 820), (1180, 820)], fill=(0, 0, 0), width=8)
        punch(d, "the local fix is on the last line, not the first", f_big)
        save_fig(im, 43)

    if need(44):
        im, d = new_canvas()
        d.rectangle([200, 420, 1500, 520], outline=(0, 0, 0), width=lw)
        d.text((850, 340), "table", font=f_lab, fill=(0, 0, 0), anchor="mm")
        xs = [280, 560, 840, 1120]
        for i, x in enumerate(xs):
            if i == 2:
                d.rectangle([x, 620, x + 160, 900], outline=(160, 160, 160), width=4)
                d.line([(x, 620), (x + 160, 900)], fill=(160, 160, 160), width=4)
                d.text((x + 80, 960), "empty", font=f_sm, fill=(0, 0, 0), anchor="mm")
            else:
                d.rectangle([x, 620, x + 160, 900], outline=(0, 0, 0), width=lw)
                d.ellipse([x + 40, 680, x + 120, 760], outline=(0, 0, 0), width=4)
        d.line([(440, 780), (560, 780)], fill=(0, 0, 0), width=4)
        d.polygon([(560, 780), (520, 760), (520, 800)], fill=(0, 0, 0))
        d.line([(1000, 780), (1120, 780)], fill=(0, 0, 0), width=4)
        d.polygon([(1120, 780), (1080, 760), (1080, 800)], fill=(0, 0, 0))
        punch(d, "overtime, not a hidden room", f_big)
        save_fig(im, 44)

    if need(45):
        im, d = new_canvas()
        pts = [(420, 160)]
        y = 160
        x = 420
        for i in range(12):
            x = 520 if i % 2 == 0 else 320
            y += 70
            pts.append((x, y))
        d.line(pts, fill=(0, 0, 0), width=lw)
        d.text((420, 1040), "thread", font=f_lab, fill=(0, 0, 0), anchor="mm")
        d.rectangle([980, 280, 1500, 860], outline=(0, 0, 0), width=lw)
        d.text((1240, 560), "file", font=f_big, fill=(0, 0, 0), anchor="mm")
        punch(d, "the box is not the thread", f_big)
        save_fig(im, 45)

    if need(46):
        im, d = new_canvas()
        d.ellipse([120, 360, 420, 720], outline=(0, 0, 0), width=lw)
        d.ellipse([360, 300, 700, 780], outline=(0, 0, 0), width=lw)
        d.text((400, 220), "hands", font=f_lab, fill=(0, 0, 0), anchor="mm")
        d.ellipse([520, 480, 580, 540], outline=(0, 0, 0), width=4)
        d.text((640, 500), "blister", font=f_sm, fill=(0, 0, 0), anchor="lm")
        d.rectangle([860, 400, 1280, 820], outline=(0, 0, 0), width=lw)
        for yy in (500, 580, 660, 740):
            d.line([(920, yy), (1220, yy)], fill=(0, 0, 0), width=3)
        d.text((1070, 320), "basil tray", font=f_lab, fill=(0, 0, 0), anchor="mm")
        d.rectangle([1360, 400, 1680, 820], outline=(0, 0, 0), width=lw)
        d.text((1520, 600), "pH", font=f_big, fill=(0, 0, 0), anchor="mm")
        d.text((1520, 680), "log", font=f_lab, fill=(0, 0, 0), anchor="mm")
        punch(d, "do not wait for helium", f_big)
        save_fig(im, 46)


def resolve_fig(n):
    order = ("jpg", "jpeg", "png") if n in PREFER_JPG else ("png", "jpg", "jpeg")
    for ext in order:
        path = os.path.join(HERE, f"fig{n:02d}.{ext}")
        if os.path.isfile(path):
            return path
    return None


def word_picture_stream(path):
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


_anchor = [0]


def new_anchor():
    _anchor[0] += 1
    return f"bm_{_anchor[0]:03d}"


def parse_all():
    files = (
        ["00_Front_Matter.md"]
        + sorted(os.path.basename(f) for f in glob.glob(os.path.join(SRC, "0[1-9]_*.md")) + glob.glob(os.path.join(SRC, "10_*.md")))
        + ["11_Appendix.md"]
        + [f for f in ("12_Notes.md", "13_Also_By.md") if os.path.isfile(os.path.join(SRC, f))]
    )
    blocks = []
    for fname in files:
        front = fname.startswith("00_")
        in_appendix = fname.startswith("11_")
        in_notes = fname.startswith("12_")
        in_also = fname.startswith("13_")
        lines = open(os.path.join(SRC, fname), encoding="utf-8").read().splitlines()
        i = 0
        while i < len(lines):
            line = lines[i].rstrip()
            if not line.strip():
                i += 1
                continue
            if front and line.startswith("# ") and not blocks:
                blocks.append(("title", line[2:].strip()))
                i += 1
                continue
            if front and line.startswith("*") and line.endswith("*") and all(b[0] in ("title", "titleline") for b in blocks):
                blocks.append(("titleline", line.strip("*").strip()))
                i += 1
                continue
            if line.strip() == "%%TOC%%":
                blocks.append(("toc",))
                i += 1
                continue
            if line.startswith("---"):
                i += 1
                continue
            mnote = re.match(r"^\[\^([\w-]+)\]:\s*(.+)$", line) if in_notes else None
            if mnote:
                blocks.append(("note", mnote.group(1), mnote.group(2).strip()))
                i += 1
                continue
            if in_also and not line.startswith("# "):
                blocks.append(("plain", line.strip()))
                i += 1
                continue
            if line.startswith("# "):
                kind = "appendix" if in_appendix else ("notes" if in_notes else "part")
                blocks.append(("h1", line[2:].strip(), kind, new_anchor()))
                i += 1
                continue
            if line.startswith("## "):
                t = line[3:].strip()
                m = re.match(r"(\d+)\.\s", t)
                if front:
                    blocks.append(("h1", t, "front", new_anchor()))
                elif in_appendix:
                    blocks.append(("h2", t, "appendix", new_anchor()))
                elif m:
                    blocks.append(("h2", t, "chapter", int(m.group(1)), new_anchor()))
                else:
                    blocks.append(("h2", t, "other", new_anchor()))
                i += 1
                continue
            img = IMG_LINE.match(line.strip())
            fig = FIG_LINE.match(line.strip())
            if img or fig:
                n = int((img or fig).group(1))
                cap = (img or fig).group(2).strip()
                blocks.append(("fig", n, cap))
                i += 1
                continue
            if in_appendix and (NOTE_LINE.match(line.strip()) or line.strip() in APPENDIX_HEADS):
                if line.strip().startswith("APPENDIX"):
                    blocks.append(("h1", line.strip(), "appendix", new_anchor()))
                else:
                    blocks.append(("h2", line.strip(), "appendix", new_anchor()))
                i += 1
                continue
            if line.startswith("|"):
                rows = []
                while i < len(lines) and lines[i].startswith("|"):
                    r = lines[i].strip()
                    if not re.match(r"^\|\s*-", r):
                        rows.append([c.strip() for c in r.strip("|").split("|")])
                    i += 1
                blocks.append(("table", rows))
                continue
            if re.match(r"^\s*(?:[-*]|\u2022)\s+", line):
                items = []
                while i < len(lines) and re.match(r"^\s*(?:[-*]|\u2022)\s+", lines[i]):
                    items.append(re.sub(r"^\s*(?:[-*]|\u2022)\s+", "", lines[i]).strip())
                    i += 1
                blocks.append(("list", items))
                continue
            para = [line]
            i += 1
            while para[-1].endswith("  ") and i < len(lines) and lines[i].strip() and not re.match(r"^(#|!\[|Figure\s+\d+\.\s|\||---|%%|A\d)", lines[i]) and lines[i].strip() not in APPENDIX_HEADS:
                para.append(lines[i].rstrip("\n"))
                i += 1
            blocks.append(("p", para))
    return blocks


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


SUP_NEST = re.compile(r"\^\{(\d+)\^\{([\d+\-]+)\}\}")
ITAL_SUB_STAR = re.compile(r"\*([A-Za-z])_\*\*?")
SUB_STAR = re.compile(r"(?<=[A-Za-z])_\*")


def add_runs(par, text, bold=False, italic=False, sup=False, sub=False, size=None):
    text = text.replace("M87*", "M87").replace("Sgr A*", "Sgr A").replace("Sagittarius A*", "Sagittarius A")
    text = SUP_NEST.sub(lambda m: "^{" + m.group(1) + to_sup(m.group(2)) + "}", text)
    text = ITAL_SUB_STAR.sub(lambda m: "*" + m.group(1) + "*\uE003", text)
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


def _run(par, s, bold, italic, sup, sub, size):
    if not s:
        return
    r = par.add_run(s.replace("", "*"))
    r.bold = bold or None
    r.italic = italic or None
    if sup:
        r.font.superscript = True
    if sub:
        r.font.subscript = True
    if size:
        r.font.size = Pt(size)
    r.font.name = BODY_FONT
    return r


def plain_text(t):
    t = re.sub(r"\*\*(.+?)\*\*", r"\1", t)
    t = re.sub(r"(?<!\w)\*([^*\n]+?)\*(?!\w)", r"\1", t)
    return t


_bm_id = [100]


def add_bookmark(par, name):
    _bm_id[0] += 1
    start = OxmlElement("w:bookmarkStart")
    start.set(qn("w:id"), str(_bm_id[0]))
    start.set(qn("w:name"), name)
    end = OxmlElement("w:bookmarkEnd")
    end.set(qn("w:id"), str(_bm_id[0]))
    par._p.insert(0, start)
    par._p.append(end)


def add_runs_linked(par, text, bold=False, italic=False, size=None, table=False):
    pos = 0
    for m in NOTE_LINK.finditer(text):
        if m.start() > pos:
            add_runs(par, text[pos:m.start()], bold=bold, italic=italic, size=size)
        if m.group(5) is not None:
            key = m.group(5)
            num = NOTE_NUM.get(key)
            if num is None:
                print("UNKNOWN NOTE KEY", key)
            else:
                if num not in REF_PLACED:
                    REF_PLACED.add(num)
                    add_bookmark(par, f"ref_{num}")
                if table:
                    if m.start() > 0 and text[m.start() - 1] not in " (":
                        add_runs(par, " ", size=size)
                    add_internal_link(par, f"Note {num}", f"note_{num}", size=size or 11)
                else:
                    add_internal_link(par, str(num), f"note_{num}", size=size or 11, sup=True)
            pos = m.end()
            continue
        if m.group(6) is not None:
            anchor = FIG_ANCHORS.get(m.group(6))
            if anchor:
                add_internal_link(par, m.group(0), anchor, bold=bold, size=size or 11)
            else:
                add_runs(par, m.group(0), bold=bold, italic=italic, size=size)
            pos = m.end()
            continue
        note = m.group(1) or m.group(2) or m.group(3)
        ch = m.group(4)
        anchor = None
        if note is not None:
            anchor = NOTE_ANCHORS.get(int(note))
        elif ch is not None:
            n = int(ch)
            if 1 <= n <= 46:
                anchor = CH_ANCHORS.get(n)
        if anchor:
            add_internal_link(par, m.group(0), anchor, bold=bold, size=size or 11)
        else:
            add_runs(par, m.group(0), bold=bold, italic=italic, size=size)
        pos = m.end()
    if pos < len(text):
        add_runs(par, text[pos:], bold=bold, italic=italic, size=size)


def _link_run(text, bold=False, size=None, sup=False):
    r = OxmlElement("w:r")
    rpr = OxmlElement("w:rPr")
    rf = OxmlElement("w:rFonts")
    for a in ("w:ascii", "w:hAnsi", "w:cs"):
        rf.set(qn(a), BODY_FONT)
    rpr.append(rf)
    if bold:
        rpr.append(OxmlElement("w:b"))
    col = OxmlElement("w:color")
    col.set(qn("w:val"), "0563C1")
    rpr.append(col)
    sz = OxmlElement("w:sz")
    sz.set(qn("w:val"), str(int((size or 11) * 2)))
    rpr.append(sz)
    u = OxmlElement("w:u")
    u.set(qn("w:val"), "single")
    rpr.append(u)
    if sup:
        va = OxmlElement("w:vertAlign")
        va.set(qn("w:val"), "superscript")
        rpr.append(va)
    r.append(rpr)
    t = OxmlElement("w:t")
    t.text = text
    t.set(qn("xml:space"), "preserve")
    r.append(t)
    return r


def add_external_link(par, url, text=None, size=None):
    rid = par.part.relate_to(url, RT.HYPERLINK, is_external=True)
    h = OxmlElement("w:hyperlink")
    h.set(qn("r:id"), rid)
    h.set(qn("w:history"), "1")
    h.append(_link_run(text or url, size=size))
    par._p.append(h)


def add_internal_link(par, text, anchor, bold=False, size=None, sup=False):
    if sup:
        h = OxmlElement("w:hyperlink")
        h.set(qn("w:anchor"), anchor)
        h.set(qn("w:history"), "1")
        h.append(_link_run(text, bold=bold, size=size, sup=True))
        par._p.append(h)
        return
    h = OxmlElement("w:hyperlink")
    h.set(qn("w:anchor"), anchor)
    h.set(qn("w:history"), "1")
    r = OxmlElement("w:r")
    rpr = OxmlElement("w:rPr")
    if bold:
        rpr.append(OxmlElement("w:b"))
    sz = OxmlElement("w:sz")
    sz.set(qn("w:val"), str(int((size or 11) * 2)))
    rpr.append(sz)
    rf = OxmlElement("w:rFonts")
    for a in ("w:ascii", "w:hAnsi", "w:cs"):
        rf.set(qn(a), BODY_FONT)
    rpr.append(rf)
    r.append(rpr)
    t = OxmlElement("w:t")
    t.text = text
    t.set(qn("xml:space"), "preserve")
    r.append(t)
    h.append(r)
    par._p.append(h)


def page_break(doc):
    p = doc.add_paragraph()
    p.add_run().add_break(WD_BREAK.PAGE)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.space_before = Pt(0)


def set_style_font(style, name=BODY_FONT, size=11, bold=None, italic=None):
    style.font.name = name
    style.font.size = Pt(size)
    if bold is not None:
        style.font.bold = bold
    if italic is not None:
        style.font.italic = italic
    rpr = style.element.get_or_add_rPr()
    rf = rpr.find(qn("w:rFonts"))
    if rf is None:
        rf = OxmlElement("w:rFonts")
        rpr.append(rf)
    for a in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
        rf.set(qn(a), name)
    for a in ("w:asciiTheme", "w:hAnsiTheme", "w:eastAsiaTheme", "w:cstheme"):
        if rf.get(qn(a)) is not None:
            del rf.attrib[qn(a)]


def setup_styles(doc):
    n = doc.styles["Normal"]
    set_style_font(n, size=11)
    pf = n.paragraph_format
    pf.first_line_indent = Inches(0.3)
    pf.space_after = Pt(0)
    pf.space_before = Pt(0)
    pf.line_spacing = 1.15
    h1 = doc.styles["Heading 1"]
    set_style_font(h1, name=HEADLINE_FONT, size=20, bold=True)
    h1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    h1.paragraph_format.space_before = Pt(36)
    h1.paragraph_format.space_after = Pt(18)
    h1.paragraph_format.first_line_indent = Inches(0)
    h1.paragraph_format.keep_with_next = True
    h2 = doc.styles["Heading 2"]
    set_style_font(h2, name=HEADLINE_FONT, size=18, bold=True)
    h2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    h2.paragraph_format.space_before = Pt(24)
    h2.paragraph_format.space_after = Pt(12)
    h2.paragraph_format.first_line_indent = Inches(0)
    h2.paragraph_format.keep_with_next = True
    for s in (h1, h2):
        s.font.color.rgb = HEADLINE_BLUE
        rpr = s.element.get_or_add_rPr()
        c = rpr.find(qn("w:color"))
        if c is None:
            c = OxmlElement("w:color")
            rpr.append(c)
        c.set(qn("w:val"), "0000FF")
    from docx.enum.style import WD_STYLE_TYPE

    def mk(name, base="Normal"):
        try:
            st = doc.styles[name]
        except KeyError:
            st = doc.styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
        st.base_style = doc.styles[base]
        return st

    fp = mk("First Paragraph")
    fp.paragraph_format.first_line_indent = Inches(0)
    ni = mk("No Indent")
    ni.paragraph_format.first_line_indent = Inches(0)
    ni.paragraph_format.space_after = Pt(6)
    eq = mk("Equation")
    eq.paragraph_format.first_line_indent = Inches(0)
    eq.paragraph_format.left_indent = Inches(0.3)
    eq.paragraph_format.space_before = Pt(6)
    eq.paragraph_format.space_after = Pt(6)
    cap = mk("Figure Caption")
    set_style_font(cap, size=9.5, italic=True)
    cap.paragraph_format.first_line_indent = Inches(0)
    cap.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cap.paragraph_format.space_before = Pt(4)
    cap.paragraph_format.space_after = Pt(14)
    tp = mk("Title Page")
    set_style_font(tp, size=26, bold=True)
    tp.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    tp.paragraph_format.first_line_indent = Inches(0)
    tp.paragraph_format.space_before = Pt(120)
    tp.paragraph_format.space_after = Pt(16)
    ts = mk("Title Sub")
    set_style_font(ts, size=13, italic=True)
    ts.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    ts.paragraph_format.first_line_indent = Inches(0)
    ts.paragraph_format.space_after = Pt(48)
    ta = mk("Title Author")
    set_style_font(ta, size=13)
    ta.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    ta.paragraph_format.first_line_indent = Inches(0)
    cp = mk("Copyright")
    set_style_font(cp, size=9.5)
    cp.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cp.paragraph_format.first_line_indent = Inches(0)
    cp.paragraph_format.space_after = Pt(8)
    t1 = mk("TOC Part")
    set_style_font(t1, size=11, bold=True)
    t1.paragraph_format.first_line_indent = Inches(0)
    t1.paragraph_format.space_before = Pt(8)
    t1.paragraph_format.space_after = Pt(2)
    t2 = mk("TOC Chapter")
    set_style_font(t2, size=10.5)
    t2.paragraph_format.first_line_indent = Inches(0)
    t2.paragraph_format.left_indent = Inches(0.25)
    t2.paragraph_format.space_after = Pt(1)
    ne = mk("Note Entry")
    set_style_font(ne, size=10)
    ne.paragraph_format.first_line_indent = Inches(0)
    ne.paragraph_format.space_after = Pt(5)
    ix = mk("Index Entry")
    set_style_font(ix, size=10.5)
    ix.paragraph_format.first_line_indent = Inches(-0.25)
    ix.paragraph_format.left_indent = Inches(0.25)
    ix.paragraph_format.space_after = Pt(3)
    rh = mk("Run-in Head")
    rh.paragraph_format.first_line_indent = Inches(0)
    rh.paragraph_format.space_before = Pt(10)
    rh.paragraph_format.space_after = Pt(2)
    rh.paragraph_format.keep_with_next = True
    li = mk("List Item")
    li.paragraph_format.first_line_indent = Inches(-0.2)
    li.paragraph_format.left_indent = Inches(0.4)
    li.paragraph_format.space_after = Pt(3)


def add_figure(doc, n, caption):
    path = resolve_fig(n)
    if not path:
        raise FileNotFoundError(f"missing figure {n}")
    stream, ext = word_picture_stream(path)
    stream.name = f"figure_{n:02d}.{ext}"
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.first_line_indent = Inches(0)
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.keep_with_next = True
    shape = p.add_run().add_picture(stream, width=Inches(4.5))
    add_bookmark(p, f"fig_{n}")
    alt = f"Figure {n}. {caption}"[:120]
    shape._inline.docPr.set("descr", alt)
    shape._inline.docPr.set("title", f"Figure {n}")
    c = doc.add_paragraph(style="Figure Caption")
    lead = c.add_run(f"Figure {n}. ")
    lead.italic = False
    lead.bold = True
    lead.font.name = BODY_FONT
    add_runs_linked(c, caption)


def add_table(doc, rows):
    if not rows:
        return
    ncol = max(len(r) for r in rows)
    t = doc.add_table(rows=len(rows), cols=ncol)
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for ri, row in enumerate(rows):
        for ci in range(ncol):
            cell = t.cell(ri, ci)
            cell.text = ""
            par = cell.paragraphs[0]
            par.paragraph_format.first_line_indent = Inches(0)
            par.paragraph_format.line_spacing = 1.0
            add_runs_linked(par, row[ci] if ci < len(row) else "", bold=(ri == 0), size=9 if ncol < 6 else 8.5, table=True)
    if ncol >= 5:
        tr = t.rows[0]._tr
        trpr = tr.get_or_add_trPr()
        th = OxmlElement("w:tblHeader")
        th.set(qn("w:val"), "true")
        trpr.append(th)
    doc.add_paragraph(style="No Indent")


def heading_anchor(block):
    if block[0] == "h1":
        return block[3]
    if block[0] == "h2" and block[2] == "chapter":
        return block[4]
    if block[0] == "h2":
        return block[3]
    return None


INDEX_TERMS = [
    ("Access and delivery (who gets the fix)", r"zip code|\bwho pays\b|\baccess\b"),
    ("Alzheimer’s antibody drugs", r"lecanemab|donanemab"),
    ("Artemis program", r"Artemis"),
    ("Artemis Accords and the Outer Space Treaty", r"Artemis Accords|Outer Space Treaty"),
    ("Basil and the pH log", r"\bbasil\b|pH log|logs the pH"),
    ("Biosphere 2", r"Biosphere 2"),
    ("Carrot (the seek loop with no off-switch)", r"\b[Cc]arrot\b"),
    ("Claims Guide", r"Claims Guide"),
    ("Clocks of aging (many clocks, not one fuse)", r"many clocks|epigenetic clock"),
    ("Contested (fourth tag)", r"\b[Cc]ontested\b"),
    ("Continuity view of personal identity", r"continuity view|psychological continuity|Parfit"),
    ("Cut-cable test", r"[Cc]ut-cable"),
    ("Expected value (long-range forecasts)", r"expected value"),
    ("Gateway (lunar station)", r"\bGateway\b"),
    ("Healthspan versus lifespan", r"healthspan"),
    ("Helium (this book’s word for a cold claim sold as ready)", r"\bhelium\b"),
    ("Hot, warm, cold (the three temperatures)", r"[Hh]ot, warm,? (and )?cold|three temperatures|temperature hygiene"),
    ("Inequality as a clock", r"[Ii]nequality"),
    ("ISRU (making supplies on site)", r"\bISRU\b"),
    ("Kessler cascade", r"Kessler"),
    ("Light-time and delay", r"[Ll]ight-time"),
    ("Local fix (this gene, this tissue, this bill)", r"[Ll]ocal fix"),
    ("Mara’s habitat", r"\bMara\b"),
    ("MOXIE (oxygen from Mars air)", r"MOXIE"),
    ("Naked mole-rat", r"mole-rat"),
    ("Negligible senescence", r"[Nn]egligible senescence"),
    ("Plasticity", r"[Pp]lasticity"),
    ("Priya’s clinic", r"\bPriya\b"),
    ("Proper time and worldlines", r"[Pp]roper time|worldline"),
    ("Reprogramming (partial, cellular)", r"[Rr]eprogramming"),
    ("Rohan", r"\bRohan\b"),
    ("S-curves", r"S-curve"),
    ("Seven loops (air, water, food, power, medicine, spares, law)", r"seven (loops|rows)|seven-loop|seven-row"),
    ("Sickle-cell gene edits", r"[Ss]ickle-cell"),
    ("Sortie, outpost, settlement", r"[Ss]ortie"),
    ("Technology readiness levels", r"readiness level|\bTRL\b"),
    ("Ten-percent brain myth", r"ten-percent|10% brain"),
    ("Time dilation (moving and low clocks)", r"atomic clocks|Hafele|muons?\b|time dilation"),
    ("Torpor and hibernation", r"[Tt]orpor|hibernat"),
    ("Trials and their phases", r"Phase [123]\b|\btrials?\b"),
    ("Uploading and copies of a mind", r"\bupload"),
]


def block_texts(b):
    if b[0] == "p":
        return [" ".join(b[1])]
    if b[0] in ("list",):
        return list(b[1])
    if b[0] == "table":
        return [c for r in b[1] for c in r]
    if b[0] == "fig":
        return [b[2]]
    return []


def build_index(blocks):
    entries = []
    sections = []
    cur = None
    for b in blocks:
        if b[0] == "h1" and b[2] in ("notes", "gen"):
            break
        if b[0] == "h1" and b[2] == "front":
            cur = (plain_text(b[1]), b[3])
        elif b[0] == "h1" and b[2] == "part":
            cur = (plain_text(b[1]).split(":")[0], b[3])
        elif b[0] == "h2" and b[2] == "chapter":
            cur = (f"Ch {b[3]}", b[4])
        elif b[0] == "h2":
            m = re.match(r"(A\d+)", b[1])
            cur = (m.group(1) if m else plain_text(b[1]), b[3])
        elif cur:
            sections.append((cur, " ".join(block_texts(b))))
    for term, rx in INDEX_TERMS:
        r = re.compile(rx)
        locs = []
        for sec, txt in sections:
            if sec not in locs and r.search(txt):
                locs.append(sec)
        if locs:
            entries.append((term, locs[:10]))
    return entries


def build():
    draw_missing()
    blocks = parse_all()
    gen = [("h1", "List of Figures", "gen", "figlist"), ("genfigs",),
           ("h1", "Index of Key Concepts", "gen", "index"), ("genindex",)]
    pos = next((k for k, b in enumerate(blocks) if b[0] == "h1" and b[1].startswith("Also by")), len(blocks))
    blocks[pos:pos] = gen
    NOTE_TEXT.clear(); NOTE_NUM.clear(); REF_PLACED.clear(); FIG_ANCHORS.clear()
    fig_list = []
    for b in blocks:
        if b[0] == "note":
            NOTE_TEXT[b[1]] = b[2]
        elif b[0] == "fig":
            FIG_ANCHORS[str(b[1])] = f"fig_{b[1]}"
            fig_list.append((str(b[1]), b[2]))
        elif b[0] == "p":
            m = re.match(r"^Figure\s+(\d+[a-z])\.\s+(.+)$", b[1][0].strip())
            if m:
                FIG_ANCHORS[m.group(1)] = f"fig_{m.group(1)}"
                fig_list.append((m.group(1), m.group(2)))
    for tables in (False, True):
        for b in blocks:
            if (b[0] == "table") != tables:
                continue
            for txt in block_texts(b):
                for k in MARKER.findall(txt):
                    if k not in NOTE_NUM:
                        NOTE_NUM[k] = len(NOTE_NUM) + 1
    print("NOTES used", len(NOTE_NUM), "unknown", [k for k in NOTE_NUM if k not in NOTE_TEXT],
          "unused", [k for k in NOTE_TEXT if k not in NOTE_NUM])
    index_entries = build_index(blocks)
    chapters = [b for b in blocks if b[0] == "h2" and b[2] == "chapter"]
    figs = [b[1] for b in blocks if b[0] == "fig"]
    missing_ch = [b[3] for b in chapters if b[3] not in figs]
    if missing_ch or sorted(figs) != list(range(1, 47)):
        print("FIGURE CHECK chapters", [b[3] for b in chapters])
        print("FIGURE CHECK figs", figs)
        print("FIGURE CHECK missing from chapters", missing_ch)
    CH_ANCHORS.clear()
    NOTE_ANCHORS.clear()
    for b in blocks:
        if b[0] == "h2" and b[2] == "chapter":
            CH_ANCHORS[b[3]] = heading_anchor(b)
        elif b[0] == "h2" and b[2] == "appendix":
            for m in re.finditer(r"A(\d+)", b[1]):
                NOTE_ANCHORS[int(m.group(1))] = heading_anchor(b)
    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Inches(6), Inches(9)
    for m in ("left_margin", "right_margin", "top_margin", "bottom_margin"):
        setattr(sec, m, Inches(0.7))
    setup_styles(doc)
    heads = []
    for b in blocks:
        if b[0] in ("h1", "h2"):
            kind = "part" if b[0] == "h1" else "chapter"
            heads.append((kind, plain_text(b[1]), heading_anchor(b)))
    doc.add_paragraph(TITLE, style="Title Page")
    doc.add_paragraph(SUBTITLE, style="Title Sub")
    doc.add_paragraph(AUTHOR, style="Title Author")
    page_break(doc)
    for line in (
        f"{TITLE}: {SUBTITLE}",
        f"Copyright © 2026 {AUTHOR}. All rights reserved.",
        "Look First, Volume 2.",
        "Photograph credits for agency and Creative Commons stills appear in the Amazon product description for this edition, not under the figures.",
    ):
        doc.add_paragraph(line, style="Copyright")
    prev = "start"
    notes_done = False
    for bi, b in enumerate(blocks):
        kind = b[0]
        if kind == "note":
            if notes_done:
                continue
            notes_done = True
            for key, num in sorted(NOTE_NUM.items(), key=lambda kv: kv[1]):
                txt = NOTE_TEXT.get(key)
                if txt is None:
                    continue
                p = doc.add_paragraph(style="Note Entry")
                add_bookmark(p, f"note_{num}")
                lead = p.add_run(f"{num}. ")
                lead.bold = True
                lead.font.name = BODY_FONT
                q = 0
                for um in re.finditer(r"https?://\S+", txt):
                    if um.start() > q:
                        add_runs(p, txt[q:um.start()], size=10)
                    add_external_link(p, um.group(0), size=10)
                    q = um.end()
                if q < len(txt):
                    add_runs(p, txt[q:], size=10)
                p.add_run(" ")
                add_internal_link(p, "Back to text", f"ref_{num}", size=10)
            prev = "note"
            continue
        if kind == "plain":
            p = doc.add_paragraph(style="No Indent")
            add_runs(p, b[1])
            prev = "plain"
            continue
        if kind == "genfigs":
            for n, cap in fig_list:
                p = doc.add_paragraph(style="TOC Chapter")
                first = re.split(r"(?<=[.!?])\s", plain_text(MARKER.sub("", cap)), maxsplit=1)[0]
                add_internal_link(p, f"Figure {n}. {first}", f"fig_{n}", size=10.5)
            prev = "gen"
            continue
        if kind == "genindex":
            p = doc.add_paragraph(style="No Indent")
            add_runs(p, "Each entry links to the chapters (Ch) and appendix notes (A) where the idea is developed; the first link is usually the place it is introduced.", italic=True, size=10)
            for term, locs in index_entries:
                p = doc.add_paragraph(style="Index Entry")
                r = p.add_run(term + ": ")
                r.bold = True
                r.font.name = BODY_FONT
                for j, (label, anchor) in enumerate(locs):
                    if j:
                        p.add_run(", ").font.name = BODY_FONT
                    add_internal_link(p, label, anchor, size=10.5)
            prev = "gen"
            continue
        if kind in ("title", "titleline"):
            continue
        if kind == "toc":
            page_break(doc)
            h = doc.add_paragraph("Contents", style="Heading 1")
            add_bookmark(h, "toc")
            for hk, t, anchor in heads:
                if hk == "part":
                    p = doc.add_paragraph(style="TOC Part")
                    add_internal_link(p, t, anchor, bold=True, size=11)
                else:
                    p = doc.add_paragraph(style="TOC Chapter")
                    add_internal_link(p, t, anchor, size=10.5)
            prev = "toc"
            continue
        if kind == "h1":
            page_break(doc)
            h = doc.add_paragraph(style="Heading 1")
            add_runs(h, b[1])
            add_bookmark(h, b[3])
            for run in h.runs:
                run.font.color.rgb = HEADLINE_BLUE
                run.font.name = HEADLINE_FONT
                run.bold = True
            prev = "head"
            continue
        if kind == "h2":
            page_break(doc)
            h = doc.add_paragraph(style="Heading 2")
            add_runs(h, b[1])
            add_bookmark(h, heading_anchor(b))
            for run in h.runs:
                run.font.color.rgb = HEADLINE_BLUE
                run.font.name = HEADLINE_FONT
                run.bold = True
            prev = "head"
            continue
        if kind == "fig":
            add_figure(doc, b[1], b[2])
            prev = "fig"
            continue
        if kind == "table":
            add_table(doc, b[1])
            prev = "table"
            continue
        if kind == "list":
            for it in b[1]:
                p = doc.add_paragraph(style="List Item")
                p.add_run("•  ")
                add_runs_linked(p, it)
            prev = "list"
            continue
        if kind == "p":
            if any(l.endswith("  ") for l in b[1]):
                p = doc.add_paragraph(style="First Paragraph" if prev != "p" else "Normal")
                for j, l in enumerate(b[1]):
                    add_runs_linked(p, l.strip())
                    if j < len(b[1]) - 1:
                        p.add_run().add_break(WD_BREAK.LINE)
                prev = "p"
                continue
            text = " ".join(l.strip() for l in b[1])
            mcap = re.match(r"^Figure\s+(\d+[a-z])\.\s+(.+)$", text)
            if mcap:
                c = doc.add_paragraph(style="Figure Caption")
                c.paragraph_format.keep_with_next = True
                add_bookmark(c, f"fig_{mcap.group(1)}")
                lead = c.add_run(f"Figure {mcap.group(1)}. ")
                lead.italic = False
                lead.bold = True
                lead.font.name = BODY_FONT
                add_runs_linked(c, mcap.group(2))
                prev = "fig"
                continue
            nxt = blocks[bi + 1] if bi + 1 < len(blocks) else None
            is_head = (
                len(b[1]) == 1 and len(text) <= 70 and re.search(r"[.:?]$", text)
                and not re.search(r"[.!?]\s", text[:-1]) and not text.startswith(("(", "*", "Rule"))
                and "[^" not in text and prev != "head"
                and (text.endswith((":", "?")) or not re.search(r"\b(is|are|was|were|ended|does|do|did|has|have|had|can|will|would)\b", text))
                and nxt is not None and nxt[0] == "p" and len(" ".join(nxt[1])) > 150
            )
            if is_head:
                p = doc.add_paragraph(style="Run-in Head")
                add_runs_linked(p, text, bold=True)
                prev = "head"
                continue
            if re.match(r"^\**\(\d+\)\**", text):
                style = "Equation"
            elif text.startswith("**") or text.startswith("*(") or text.lower().startswith("*where") or text.lower().startswith("where "):
                style = "No Indent"
            else:
                style = "First Paragraph" if prev != "p" else "Normal"
            p = doc.add_paragraph(style=style)
            add_runs_linked(p, text)
            prev = "p"
    doc.core_properties.title = TITLE
    doc.core_properties.author = AUTHOR
    doc.core_properties.subject = SUBTITLE
    doc.core_properties.category = "Look First, Volume 2"
    doc.save(OUT)
    print("saved", OUT)
    print("chapters", len(chapters), "figures", len(figs))
    return OUT


if __name__ == "__main__":
    build()
