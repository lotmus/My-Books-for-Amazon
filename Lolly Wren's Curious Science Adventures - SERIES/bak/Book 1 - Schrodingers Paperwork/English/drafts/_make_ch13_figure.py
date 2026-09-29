"""Chapter 13 figure: Bell/CHSH as a photographed print, wording drawn in code."""

from __future__ import annotations

import shutil
import tempfile
import zipfile
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter

ASSETS = Path(
    r"C:\Users\lomus\.cursor\projects\d-My-Books-for-Amazon-Schrodingers-Paperwork"
    r"\assets\ch13-bell-chsh-ceiling.png"
)
DOCX = Path(r"D:\My Books for Amazon\Schrodingers_Paperwork\Schrodingers_Paperwork_BOOK_1.docx")

INK = "#1A1A1A"
MUTED = "#6A6A6A"
LINE = "#2E74B5"
LOCAL = "#8A8A8A"
QUANTUM = "#B5622E"
PAPER = "#F7F4EE"


def draw_figure(path: Path) -> None:
    fig_w, fig_h = 7.42, 4.18
    fig, ax = plt.subplots(figsize=(fig_w, fig_h), dpi=240)
    fig.patch.set_facecolor(PAPER)
    # equal data units so the stations stay circular
    ax.set_xlim(0, fig_w)
    ax.set_ylim(0, fig_h)
    ax.set_aspect("equal")
    ax.set_axis_off()
    ax.set_facecolor(PAPER)

    ax.text(
        fig_w / 2,
        3.90,
        "Bell / CHSH: measured correlation exceeded the local ceiling",
        ha="center",
        va="center",
        fontsize=11.4,
        color=INK,
        fontname="DejaVu Sans",
    )
    ax.text(
        1.85,
        3.28,
        "A number, not an interpretation",
        ha="center",
        va="center",
        fontsize=10.6,
        color=INK,
        fontname="DejaVu Sans",
    )
    ax.text(6.42, 3.28, "S", ha="center", va="center", fontsize=12.5, color=INK, fontname="DejaVu Sans")

    for cx, label in ((0.92, "a / a'"), (2.78, "b / b'")):
        ax.add_patch(plt.Circle((cx, 2.15), 0.42, fill=False, ec=INK, lw=1.4, zorder=4))
        ax.text(cx, 2.15, label, ha="center", va="center", fontsize=9.4, color=INK, fontname="DejaVu Sans")
        ax.text(
            cx,
            1.48,
            "setting chosen\nafter separation",
            ha="center",
            va="top",
            fontsize=8.3,
            color=MUTED,
            fontname="DejaVu Sans",
            linespacing=1.35,
        )

    ax.plot([1.34, 2.36], [2.15, 2.15], ls=(0, (2.4, 2.6)), color=LINE, lw=1.2, zorder=3)
    ax.plot(1.85, 2.15, marker="*", markersize=12, color=INK, zorder=5)

    ax.add_patch(plt.Rectangle((4.55, 0.92), 0.72, 1.18, facecolor=LOCAL, edgecolor="none", zorder=3))
    ax.add_patch(plt.Rectangle((5.85, 0.92), 0.72, 1.67, facecolor=QUANTUM, edgecolor="none", zorder=3))
    ax.plot([4.38, 6.74], [0.92, 0.92], color=INK, lw=1.1, zorder=4)
    ax.text(4.91, 2.16, "2", ha="center", va="bottom", fontsize=10.2, color=INK, fontname="DejaVu Sans")
    ax.text(6.21, 2.65, "2.83", ha="center", va="bottom", fontsize=10.2, color=INK, fontname="DejaVu Sans")
    ax.text(4.91, 0.58, "local limit", ha="center", va="center", fontsize=8.7, color=MUTED, fontname="DejaVu Sans")
    ax.text(6.21, 0.58, "quantum ceiling", ha="center", va="center", fontsize=8.7, color=MUTED, fontname="DejaVu Sans")

    fig.subplots_adjust(left=0.03, right=0.97, top=0.96, bottom=0.05)
    fig.savefig(path, dpi=240, facecolor=PAPER)
    plt.close(fig)


def photograph(path: Path) -> None:
    plate = Image.open(path).convert("RGB")
    w, h = plate.size
    rng = np.random.default_rng(13)
    grain = rng.normal(0, 4.2, (h, w, 3))
    arr = np.clip(np.array(plate, dtype=np.float32) + grain, 0, 255).astype(np.uint8)
    plate = Image.fromarray(arr)

    # vignette + left window light
    yy, xx = np.mgrid[0:h, 0:w]
    vig = 1.0 - 0.10 * (((xx / w - 0.5) ** 2) + ((yy / h - 0.48) ** 2))
    light = 1.0 + 0.045 * (1.0 - xx / w)
    lit = np.clip(np.array(plate, dtype=np.float32) * vig[..., None] * light[..., None], 0, 255)
    plate = Image.fromarray(lit.astype(np.uint8))

    pad = 38
    canvas = Image.new("RGB", (w + pad * 2, h + pad * 2), (214, 208, 198))
    shadow = Image.new("L", canvas.size, 0)
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle((pad + 10, pad + 14, pad + w + 10, pad + h + 16), radius=6, fill=90)
    shadow = shadow.filter(ImageFilter.GaussianBlur(16))
    canvas.paste((168, 160, 148), mask=shadow)
    canvas.paste(plate, (pad, pad))
    canvas = ImageEnhance.Contrast(canvas).enhance(1.04)
    canvas = ImageEnhance.Color(canvas).enhance(0.92)
    canvas.save(path, "PNG")


def embed(src: Path) -> None:
    tmp = Path(tempfile.mkdtemp(prefix="sp_ch13_"))
    with zipfile.ZipFile(DOCX, "r") as zin:
        zin.extractall(tmp)
    dest = tmp / "word" / "media" / "image13.png"
    shutil.copyfile(src, dest)
    xml_path = tmp / "word" / "document.xml"
    xml = xml_path.read_text(encoding="utf-8")
    old = (
        'descr="Diagram: a shared source sending particles to two distant '
        "detectors with independently chosen settings, next to a bar chart "
        'comparing the classical and quantum correlation limits."'
    )
    new = (
        'descr="Photograph of a Bell/CHSH figure: two stations with settings '
        "chosen after separation, and bars for the local limit of 2 and the "
        'quantum ceiling of 2.83. A number, not an interpretation."'
    )
    if old in xml:
        xml_path.write_text(xml.replace(old, new, 1), encoding="utf-8")
        print("alt text updated")
    out_tmp = DOCX.with_suffix(".docx.repack")
    if out_tmp.exists():
        out_tmp.unlink()
    with zipfile.ZipFile(out_tmp, "w", compression=zipfile.ZIP_DEFLATED) as zout:
        for path in sorted(tmp.rglob("*")):
            if path.is_file():
                zout.write(path, path.relative_to(tmp).as_posix())
    try:
        DOCX.unlink()
    except PermissionError:
        print("close the Word document and run again to embed")
        shutil.rmtree(tmp, ignore_errors=True)
        if out_tmp.exists():
            out_tmp.unlink()
        return False
    shutil.move(out_tmp, DOCX)
    shutil.rmtree(tmp, ignore_errors=True)
    return True


def main() -> None:
    ASSETS.parent.mkdir(parents=True, exist_ok=True)
    draw_figure(ASSETS)
    photograph(ASSETS)
    print("wrote", ASSETS, ASSETS.stat().st_size)
    if embed(ASSETS):
        print("updated", DOCX)
    else:
        print("figure ready; Word still has the manuscript open")


if __name__ == "__main__":
    main()
