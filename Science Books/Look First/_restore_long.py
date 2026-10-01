# -*- coding: utf-8 -*-
"""Replace the thin camp and body halves with the long Kindle texts."""
import html
import re
import zipfile
from pathlib import Path

ROOT = Path(r"C:\Users\lomus\OneDrive\My Books for Amazon\Science Books\Look First")
OUT = ROOT / "A Trip Is Not a New Life - Manuscript"
TRIP = Path(r"D:\Book Backups\Cosmology\A Permit Is Not a City - Manuscript\A Permit Is Not a City - Kindle.docx")
BODY = next(p for p in (ROOT / "A Longer Life Is Not a New Body - Manuscript").glob("*.docx") if "Invoice" in p.name)
APOS = "\u2019"


def docx_text(path: Path) -> str:
    xml = zipfile.ZipFile(path).read("word/document.xml").decode("utf-8", "replace")
    text = re.sub(r"</w:p>", "\n", xml)
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    text = text.replace("\u00a0", " ")
    return text


def words(text: str) -> int:
    return len(re.findall(r"\S+", text))


def after_last(text: str, marker: str) -> str:
    starts = [m.start() for m in re.finditer(re.escape(marker), text)]
    if not starts:
        raise SystemExit(f"missing marker {marker!r}")
    return text[starts[-1]:]


def to_markdown(chunk: str) -> str:
    lines = []
    for raw in chunk.splitlines():
        s = raw.strip()
        if not s:
            lines.append("")
            continue
        if re.match(r"^PART [IVX]+", s):
            lines.append(f"# {s}")
            lines.append("")
            continue
        if re.match(r"^\d+\.\s+\S", s) and len(s) < 90 and not re.match(r"^\d+\.\s+\d", s):
            lines.append(f"## {s}")
            lines.append("")
            continue
        lines.append(s)
    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def shift_invoice(text: str) -> str:
    text = re.sub(
        r"Chapter 12 of the other book.s three nouns",
        f"Chapter 12{APOS}s three nouns",
        text,
    )
    text = text.replace(
        "The slip is Chapter 3 of the destinations book, if you have it; you do not need it.",
        "The slip is Chapter 3; a moved year is a meeting, not a destiny.",
    )

    def heads(m: re.Match) -> str:
        n = int(m.group(1))
        if 1 <= n <= 20:
            return f"## {n + 26}. "
        return m.group(0)

    text = re.sub(r"^## (\d+)\. ", heads, text, flags=re.M)

    def ch(m: re.Match) -> str:
        n = int(m.group(1))
        if 1 <= n <= 20:
            return f"Chapter {n + 26}"
        return m.group(0)

    text = re.sub(r"Chapter (\d+)", ch, text)
    return text


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="\n")


def split_on_parts(md: str):
    parts = re.split(r"(?=^# PART )", md, flags=re.M)
    return [p for p in parts if p.strip()]


trip_raw = after_last(docx_text(TRIP), "1. The Airlock Still Sticks")
app_at = trip_raw.find("\nAPPENDIX")
if app_at < 0:
    raise SystemExit("trip appendix missing")
trip_main = to_markdown(trip_raw[:app_at])
trip_app = trip_raw[app_at:].strip() + "\n"
trip_parts = split_on_parts(trip_main)
if len(trip_parts) != 4:
    raise SystemExit(f"expected 4 trip parts, got {len(trip_parts)}")
names = [
    "01_Part_One_Dirt_Delay_Dates.md",
    "02_Part_Two_The_Moon_First.md",
    "03_Part_Three_Vehicle_Not_City.md",
    "04_Part_Four_Who_Stays.md",
]
# Point the old 'longer book' crew line at this book's Chapter 25.
for i, name in enumerate(names):
    text = trip_parts[i]
    text = text.replace(
        "Chapter 31 of the longer book already said a crew that does not sleep can wait. This book says a crew that does not sleep can also fetch a box",
        "Chapter 25 says a crew that does not sleep can wait. The same crew can also fetch a box",
    )
    text = text.replace(
        "The longer book already said a library is not a seed unless you look first.",
        "Chapter 26 says a library is not a seed unless you look first.",
    )
    text = text.replace(
        f"The longer book{APOS}s rule",
        f"Chapter 26{APOS}s rule",
    )
    text = text.replace("The longer book's rule", f"Chapter 26{APOS}s rule")
    text = text.replace(
        "That rule, in the longer book, meant",
        "That rule, in *The Universe Has No Now*, meant",
    )
    write(OUT / name, text)
    print(name, words(text))

body_all = docx_text(BODY)
hands = [m.start() for m in re.finditer(r"(?m)^1\. Her Hands Still Age\s*$", body_all)]
part_i = body_all.rfind("PART I", 0, hands[-1])
if part_i < 0:
    raise SystemExit("body PART I missing")
body_raw = body_all[part_i:]
bapp = body_raw.find("\nAPPENDIX")
if bapp < 0:
    bapp = body_raw.find("\nAppendix")
if bapp < 0:
    raise SystemExit("body appendix missing")
body_main = shift_invoice(to_markdown(body_raw[:bapp]))
body_app = body_raw[bapp:].strip() + "\n"
body_parts = split_on_parts(body_main)
print("body parts", len(body_parts), "words", words(body_main))
body_names = [
    "07_Part_Seven_Many_Clocks.md",
    "08_Part_Eight_The_Organ.md",
    "09_Part_Nine_Not_A_Straight_Line.md",
    "10_Part_Ten_The_Honest_Body.md",
]
if len(body_parts) != 4:
    for i, p in enumerate(body_parts):
        print("--- part", i, p.splitlines()[0] if p.strip() else "EMPTY")
    raise SystemExit("body part count")
# Renumber part titles to VII-X so they sit after the camp half.
renames = {
    "PART I": ("PART VII", "07_Part_Seven_Many_Clocks.md"),
    "PART II": ("PART VIII", "08_Part_Eight_The_Organ.md"),
    "PART III": ("PART IX", "09_Part_Nine_Not_A_Straight_Line.md"),
    "PART IV": ("PART X", "10_Part_Ten_The_Honest_Body.md"),
}
for part in body_parts:
    key = None
    for label in ("PART IV", "PART III", "PART II", "PART I"):
        if re.search(rf"\b{label}\b", part.splitlines()[0]):
            key = label
            break
    if key is None:
        raise SystemExit(part.splitlines()[0])
    new, name = renames[key]
    part = re.sub(rf"\b{key}\b", new, part, count=1)
    write(OUT / name, part)
    print(name, words(part))

# Appendix: long trip notes, then the body book's notes.
app = (
    "# APPENDIX\n\n"
    "The first block is the camp half. The second block is the body half. "
    "Chapter numbers in the body notes are the numbers in this book.\n\n"
    + trip_app
    + "\n\n"
    + shift_invoice(to_markdown(body_app))
)
write(OUT / "11_Appendix.md", app)
print("appendix", words(app))
print("trip main", words(trip_main), "trip app", words(trip_app))
