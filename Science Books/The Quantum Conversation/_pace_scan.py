import pathlib
import re

root = pathlib.Path(r"C:\Users\lomus\OneDrive\My Books for Amazon\Science Books\The Quantum Conversation")
skip = {"00_Chapter_Outline.md", "Editorial_Review_2026-09-24.md"}

ABBREV = {
    "dr", "mr", "mrs", "ms", "prof", "jr", "sr", "st", "fig", "eq", "ch",
    "vs", "etc", "al", "e.g", "i.e", "u.s", "u.k", "ph.d", "no",
}

def word_count(s):
    return len(re.findall(r"[A-Za-z0-9']+", s))

def split_sentences(text):
    """Return sentence strings, including their ending punctuation."""
    marks = []
    i = 0
    n = len(text)
    while i < n:
        ch = text[i]
        if ch in ".!?":
            j = i + 1
            # footnote markers and closing markdown before the space
            while j < n and text[j] in ")*_\"'0123456789^":
                # stop if we run into the next sentence's capital without a space
                j += 1
            if j < n and text[j].isspace():
                k = j
                while k < n and text[k].isspace():
                    k += 1
                if k < n and (text[k].isupper() or text[k] in "\"'*"):
                    token = re.findall(r"[A-Za-z.]+", text[max(0, i - 8):i])
                    prev = token[-1].lower().rstrip(".") if token else ""
                    if prev not in ABBREV and not re.fullmatch(r"[A-Z]", prev):
                        marks.append(k)
                        i = k
                        continue
        i += 1
    if not marks:
        return [text]
    out = []
    start = 0
    for m in marks:
        out.append(text[start:m].strip())
        start = m
    tail = text[start:].strip()
    if tail:
        out.append(tail)
    return [s for s in out if s]

def pack(sentences, target=95, ceiling=130):
    chunks = []
    cur = ""
    for s in sentences:
        if not cur:
            cur = s
            continue
        if word_count(cur) >= target or word_count(cur) + word_count(s) > ceiling:
            chunks.append(cur)
            cur = s
        else:
            cur = cur + " " + s
    if cur:
        chunks.append(cur)
    return chunks

# Preview one known wall before writing anything.
sample = (root / "07_Part_Seven_Geometry_Symmetry_Vacuum.md").read_text(encoding="utf-8")
sample = sample.replace("\r\n", "\n")
block = next(b for b in sample.split("\n\n") if "slower than a snail" in b)
print("--- SAMPLE", word_count(block), "words", len(split_sentences(block.strip())), "sentences ---")
for i, c in enumerate(pack(split_sentences(block.strip())), 1):
    print(f"\n[{i} | {word_count(c)}]")
    print(c[:220])
print("--- END SAMPLE ---\n")
raise SystemExit(0)

changed_files = 0
split_count = 0
for f in sorted(root.glob("*.md")):
    if f.name in skip or f.name.startswith("_"):
        continue
    text = f.read_text(encoding="utf-8")
    blocks = text.split("\n\n")
    new_blocks = []
    file_changed = False
    for block in blocks:
        head = block.lstrip()
        if (
            word_count(block) < 170
            or head.startswith("#")
            or head.startswith(">")
            or head.startswith("![")
            or head.startswith("%%")
            or head.startswith("|")
        ):
            new_blocks.append(block)
            continue
        sentences = split_sentences(block.strip("\n"))
        if len(sentences) < 2:
            new_blocks.append(block)
            continue
        chunks = pack(sentences)
        if len(chunks) < 2:
            new_blocks.append(block)
            continue
        # preserve leading/trailing blank that split already removed; keep original indent none
        new_blocks.append("\n\n".join(chunks))
        file_changed = True
        split_count += 1
    if file_changed:
        f.write_text("\n\n".join(new_blocks), encoding="utf-8")
        changed_files += 1
        print("split", f.name)

print("files", changed_files, "paragraphs", split_count)
