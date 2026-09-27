"""Rebuild a valid live BOOK_1_2.docx from photo figures."""

from __future__ import annotations

import importlib.util
import io
import shutil
import tempfile
import zipfile
from pathlib import Path

from PIL import Image

ROOT = Path(r"D:\My Books for Amazon\Schrodingers_Paperwork")
FIGS = ROOT / "English" / "_fig_out"
SRC = ROOT / "Schrodingers_Paperwork_BOOK_1_Photo_Edition.docx"
LIVE = ROOT / "Schrodingers_Paperwork_BOOK_1_2.docx"


def load_photo():
    spec = importlib.util.spec_from_file_location("photo", ROOT / "English" / "_photo_figs.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def save_clean(src: Path, dest: Path) -> None:
    im = Image.open(src)
    im.load()
    im = im.convert("RGB")
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.suffix.lower() in {".jpg", ".jpeg"}:
        im.save(dest, "JPEG", quality=88, optimize=True)
    else:
        im.save(dest, "PNG", optimize=True)


def main() -> None:
    photo = load_photo()
    dest3 = FIGS / "image3.png"
    print("rebuild fig3", photo.fig3(dest3))
    Image.open(dest3).load()
    print("image3 ok", dest3.stat().st_size)

    if not SRC.exists():
        raise SystemExit(f"missing source {SRC}")

    tmp = Path(tempfile.mkdtemp(prefix="sp_live_"))
    with zipfile.ZipFile(SRC) as z:
        z.extractall(tmp)
    media = tmp / "word" / "media"
    for p in sorted(FIGS.glob("image*")):
        save_clean(p, media / p.name)
        print("media", p.name, (media / p.name).stat().st_size)

    packed = ROOT / "_book_live_build.docx"
    if packed.exists():
        packed.unlink()
    with zipfile.ZipFile(packed, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for f in sorted(tmp.rglob("*")):
            if f.is_file():
                z.write(f, f.relative_to(tmp).as_posix())
    shutil.rmtree(tmp, ignore_errors=True)

    with zipfile.ZipFile(packed) as z:
        bad = z.testzip()
        names = z.namelist()
        print("testzip", bad, "media", len([n for n in names if n.startswith("word/media/")]))
        if bad is not None or "word/document.xml" not in names:
            raise SystemExit("packed docx failed validation")
        for n in names:
            if n.startswith("word/media/"):
                Image.open(io.BytesIO(z.read(n))).load()
        print("all media load ok")

    if LIVE.exists():
        LIVE.unlink()
    shutil.copyfile(packed, LIVE)
    shutil.copyfile(packed, SRC)
    packed.unlink()
    print("LIVE", LIVE, LIVE.stat().st_size)


if __name__ == "__main__":
    main()
