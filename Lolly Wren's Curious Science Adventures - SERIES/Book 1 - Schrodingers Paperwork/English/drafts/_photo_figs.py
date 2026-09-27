"""Kindle-safe photo scenes + typeset labels, then re-embed."""

from __future__ import annotations

import importlib.util
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFont, ImageOps

ROOT = Path(r"D:\My Books for Amazon\Schrodingers_Paperwork")
PHOTO = Path(r"C:\Users\lomus\.cursor\projects\d-My-Books-for-Amazon-Schrodingers-Paperwork\assets")
ASSETS = ROOT / "English" / "_fig_out"
DOCX = ROOT / "Schrodingers_Paperwork_BOOK_1_2.docx"

INK = (17, 17, 17)
MUTED = (70, 70, 70)
PAPER = (255, 255, 255)

spec = importlib.util.spec_from_file_location("redraw", ROOT / "English" / "_redraw_figs.py")
redraw = importlib.util.module_from_spec(spec)
sys.modules["redraw"] = redraw
spec.loader.exec_module(redraw)


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    path = Path(redraw.__file__).resolve()
    # matplotlib ships DejaVu
    import matplotlib

    return ImageFont.truetype(str(Path(matplotlib.get_data_path()) / "fonts" / "ttf" / name), size)


def kindle(im: Image.Image) -> Image.Image:
    im = im.convert("L")
    im = ImageOps.autocontrast(im, cutoff=1)
    im = ImageEnhance.Contrast(im).enhance(1.12)
    return im.convert("RGB")


def load(name: str, width: int) -> Image.Image:
    im = kindle(Image.open(PHOTO / name))
    h = int(im.height * (width / im.width))
    return im.resize((width, h), Image.Resampling.LANCZOS)


def boxed(draw: ImageDraw.ImageDraw, xy, text, fnt, fill=INK, bg=PAPER, pad=7, anchor="mm"):
    bbox = draw.multiline_textbbox(xy, text, font=fnt, anchor=anchor, align="center", spacing=4)
    draw.rectangle((bbox[0] - pad, bbox[1] - pad, bbox[2] + pad, bbox[3] + pad), fill=bg)
    draw.multiline_text(xy, text, font=fnt, fill=fill, anchor=anchor, align="center", spacing=4)


def frame(photo: Image.Image, title: str, caption: str, labels=()) -> Image.Image:
    """White title/caption bands so type never sits on the photo."""
    w = 1400
    if photo.width != w:
        photo = photo.resize((w, int(photo.height * (w / photo.width))), Image.Resampling.LANCZOS)
    top, bot = 92, 86
    canvas = Image.new("RGB", (w, photo.height + top + bot), PAPER)
    canvas.paste(photo, (0, top))
    draw = ImageDraw.Draw(canvas)
    tf, cf, lf = font(30, True), font(22), font(22)
    draw.multiline_text((w // 2, top // 2), title, font=tf, fill=INK, anchor="mm", align="center")
    draw.multiline_text((w // 2, top + photo.height + bot // 2), caption, font=cf, fill=MUTED, anchor="mm", align="center")
    for x, y, text, anchor in labels:
        boxed(draw, (int(x * w), top + int(y * photo.height)), text, lf, anchor=anchor)
    return canvas


def save(im: Image.Image, dest: Path) -> tuple[int, int]:
    dest.parent.mkdir(parents=True, exist_ok=True)
    im = im.convert("L").convert("RGB")
    if dest.suffix.lower() in {".jpg", ".jpeg"}:
        im.save(dest, "JPEG", quality=88, optimize=True)
    else:
        im.save(dest, "PNG", optimize=True)
    return im.size


def side_by_side(a: Image.Image, b: Image.Image, gap: int = 28) -> Image.Image:
    h = min(a.height, b.height)
    a = a.resize((int(a.width * h / a.height), h), Image.Resampling.LANCZOS)
    b = b.resize((int(b.width * h / b.height), h), Image.Resampling.LANCZOS)
    out = Image.new("RGB", (a.width + b.width + gap, h), PAPER)
    out.paste(a, (0, 0))
    out.paste(b, (a.width + gap, 0))
    return out


def stack(a: Image.Image, b: Image.Image, gap: int = 22) -> Image.Image:
    w = min(a.width, b.width)
    a = a.resize((w, int(a.height * w / a.width)), Image.Resampling.LANCZOS)
    b = b.resize((w, int(b.height * w / b.width)), Image.Resampling.LANCZOS)
    out = Image.new("RGB", (w, a.height + b.height + gap), PAPER)
    out.paste(a, (0, 0))
    out.paste(b, (0, a.height + gap))
    return out


def fig1(path: Path):
    photo = load("kfig01_slits.png", 1400)
    return save(frame(photo,
        "Superposition: both paths, until one is asked",
        "Both paths contribute. The stripes are the evidence.",
        [(0.18, 0.90, "source", "mm"), (0.47, 0.90, "two slits", "mm"), (0.78, 0.90, "screen", "mm")],
    ), path)


def fig2(path: Path):
    photo = load("kfig02_bases.png", 1400)
    return save(frame(photo,
        "Measurement basis: the apparatus decides which question is asked",
        "Same particle. Different magnet. Different question.",
        [(0.08, 0.62, "incoming", "mm"), (0.28, 0.08, "Basis A", "mm"), (0.72, 0.08, "Basis B", "mm")],
    ), path)


def fig3(path: Path):
    a = load("kfig03a_interfere.png", 1400)
    b = load("kfig03b_whichpath.png", 1400)
    da, db = ImageDraw.Draw(a), ImageDraw.Draw(b)
    lf = font(24)
    boxed(da, (a.width // 2, 36), "Interference: both slits used", lf, anchor="mm")
    boxed(db, (b.width // 2, 36), "One clump: the stripes are gone", lf, anchor="mm")
    boxed(db, (int(0.42 * b.width), int(0.18 * b.height)), "which-path detector", lf, anchor="mm")
    return save(frame(stack(a, b),
        "Ask which path, and the pattern that needed both is gone",
        "Look, then look again. The stripes do not survive the question.",
    ), path)


def fig4(path: Path):
    photo = load("kfig04_zeno.png", 1400)
    return save(frame(photo,
        "Quantum Zeno effect: checked often enough, it barely moves",
        "Each check measures again, and resets the drift.",
        [(0.86, 0.28, "if left alone", "mm"), (0.86, 0.52, "confirmed\nstate", "mm")],
    ), path)


def fig7(path: Path):
    photo = load("kfig07_entangle.png", 1400)
    return save(frame(photo,
        "Entanglement: a shared fact, not a message",
        "No signal travels this way.",
        [(0.18, 0.82, "Station A", "mm"), (0.82, 0.82, "Station B", "mm"), (0.50, 0.28, "shared origin", "mm")],
    ), path)


def fig8(path: Path):
    a = load("kfig08a_copier.png", 700)
    b = load("kfig08b_pattern.png", 700)
    da, db = ImageDraw.Draw(a), ImageDraw.Draw(b)
    lf = font(22)
    boxed(da, (a.width // 2, 28), "Unknown state", lf, anchor="mm")
    boxed(db, (b.width // 2, 28), "Distributed pattern", lf, anchor="mm")
    boxed(da, (a.width // 2, a.height - 36), "no perfect copy", lf, anchor="mm")
    boxed(db, (b.width // 2, b.height - 36), "one damaged node —\nthe pattern still holds", lf, anchor="mm")
    return save(frame(side_by_side(a, b),
        "No perfect copy. A spread-out pattern can still be repaired.",
        "You cannot copy the unknown. You can repair a pattern.",
    ), path)


def fig10(path: Path):
    a = load("kfig10a_isolated.png", 680)
    b = load("kfig10b_moon.png", 680)
    da, db = ImageDraw.Draw(a), ImageDraw.Draw(b)
    lf = font(22)
    boxed(da, (a.width // 2, 32), "Isolated, in principle", lf, anchor="mm")
    boxed(db, (b.width // 2, 32), "The moon, in contact with the sky", lf, anchor="mm")
    boxed(da, (a.width // 2, a.height - 48), "Few records nearby.\nInterference can survive.", lf, anchor="mm")
    boxed(db, (b.width // 2, b.height - 48), "Air, light and warmth\nnotice it constantly.", lf, anchor="mm")
    return save(frame(side_by_side(a, b),
        "Decoherence: the world is already looking, on nobody's authority",
        "No rota required.",
    ), path)


def fig11(path: Path):
    photo = load("kfig11_wigner.png", 1400)
    return save(frame(photo,
        "Wigner's friend: definite inside, still open from outside",
        "There is no view from nowhere.",
        [(0.14, 0.88, "Wigner, outside", "mm"), (0.62, 0.88, "Friend has a record", "mm")],
    ), path)


def fig12(path: Path):
    photo = load("kfig12_pilot.png", 1400)
    return save(frame(photo,
        "Pilot-wave theory: one path taken, guided by all the others",
        "The empty paths do not cross the one that is taken.",
        [(0.12, 0.88, "source", "mm"), (0.50, 0.08, "actual path (solid)", "mm"),
         (0.50, 0.88, "empty path (dashed)", "mm"), (0.88, 0.88, "screen", "mm")],
    ), path)


def fig14(path: Path):
    photo = load("kfig14_mtheory.png", 1100)
    return save(frame(photo,
        "Five theories, seen from five sides",
        "Same structure. Five limited views.",
        [(0.50, 0.93, "M-theory", "mm"), (0.50, 0.04, "Type I", "mm"),
         (0.08, 0.28, "Type IIA", "mm"), (0.08, 0.78, "Type IIB", "mm"),
         (0.92, 0.28, "Heterotic\nE8 x E8", "mm"), (0.92, 0.78, "Heterotic\nSO(32)", "mm")],
    ), path)


def fig15(path: Path):
    photo = load("kfig15_holo.png", 1100)
    return save(frame(photo,
        "Holography: the boundary carries the account",
        "The account is kept on the surface, not lost inside.",
        [(0.50, 0.90, "volume (the interior)", "mm"), (0.88, 0.10, "readable\non this edge", "mm")],
    ), path)


FIGURES = [
    ("image1.png", fig1),
    ("image2.jpeg", fig2),
    ("image3.png", fig3),
    ("image4.jpeg", fig4),
    ("image5.jpeg", redraw.fig5),
    ("image6.png", redraw.fig6),
    ("image7.jpeg", fig7),
    ("image8.jpeg", fig8),
    ("image9.jpeg", redraw.fig9),
    ("image10.jpeg", fig10),
    ("image11.jpeg", fig11),
    ("image12.png", fig12),
    ("image13.png", redraw.fig13),
    ("image14.png", fig14),
    ("image15.png", fig15),
    ("image16.png", redraw.fig16),
    ("image17.png", redraw.fig17),
]


def main() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    sizes = {}
    for name, fn in FIGURES:
        dest = ASSETS / name
        w, h = fn(dest)
        sizes[name] = (w, h)
        print(f"built {name:14s} {w}x{h}")

    source = DOCX if DOCX.exists() else None
    for fallback in (DOCX.with_suffix(".docx.next"), DOCX.with_suffix(".docx.repack")):
        if source is None and fallback.exists():
            source = fallback
    if source is None:
        raise SystemExit(f"No book file found at {DOCX}")

    tmp = Path(tempfile.mkdtemp(prefix="sp_photo_"))
    with zipfile.ZipFile(source) as z:
        z.extractall(tmp)
    media = tmp / "word" / "media"
    for name in sizes:
        shutil.copyfile(ASSETS / name, media / name)
    xml_path = tmp / "word" / "document.xml"
    xml_path.write_text(redraw.update_extents(xml_path.read_text(encoding="utf-8"), sizes), encoding="utf-8")
    packed = DOCX.with_name(DOCX.stem + "_kindle.docx")
    if packed.exists():
        packed.unlink()
    with zipfile.ZipFile(packed, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for path in sorted(tmp.rglob("*")):
            if path.is_file():
                z.write(path, path.relative_to(tmp).as_posix())
    shutil.rmtree(tmp, ignore_errors=True)
    try:
        if DOCX.exists():
            DOCX.unlink()
        shutil.copyfile(packed, DOCX)
        print("updated", DOCX, "mb", round(DOCX.stat().st_size / 1e6, 2))
    except PermissionError as e:
        print("Word has the live file open. Updated copy saved as", packed)
        print(e)


if __name__ == "__main__":
    main()
