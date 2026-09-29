"""Book 3 quality pass: exact-duplicate removal + mechanical fragment cleanup."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
PARTS = [
    "01_Part_One_Many_Clocks.md",
    "02_Part_Two_The_Organ_You_Already_Use.md",
    "03_Part_Three_Not_A_Straight_Line.md",
    "04_Part_Four_The_Honest_Body.md",
]

# Ultra-short mechanical closers from thicken passes — delete whole --- blocks that are only these
KILL_FRAGMENTS = {
    "Keep the log.",
    "Keep the log. Four words clear the bar when brands sell capacity they do not have.",
    "Local heat. Cold coat. Done.",
    "Tin closed. Body counted. Sale sized.",
    "Inventory first. Seal second. Helium never. That is the tin.",
    "Keep the stair. Leave the costume.",
    "Middles are temporary. Cash them as middles.",
    "Eight more words for the wall: name it or you bought a ray. Middles are temporary. Cash them as middles.",
}


def norm(s: str) -> str:
    s = re.sub(r"\s+", " ", s.strip().lower())
    s = s.replace("—", "-").replace("–", "-")
    return s


def collapse_exact_duplicate_paragraphs(text: str) -> tuple[str, int]:
    """Remove a paragraph if the previous non-empty paragraph has the same normalized text."""
    parts = re.split(r"(\n\n+)", text)
    out = []
    removed = 0
    last_para_norm = None
    for i, chunk in enumerate(parts):
        if re.fullmatch(r"\n\n+", chunk or ""):
            out.append(chunk)
            continue
        # chunk may contain multiple lines that form one paragraph block
        para = chunk.strip()
        if not para:
            out.append(chunk)
            continue
        # skip headings / figures / hr for dedupe identity of "last"
        if para.startswith("#") or para.startswith("![") or para == "---":
            out.append(chunk)
            last_para_norm = None
            continue
        n = norm(para)
        if last_para_norm and n == last_para_norm and len(n) > 40:
            removed += 1
            # drop this paragraph; also drop preceding separator if present
            if out and re.fullmatch(r"\n\n+", out[-1] or ""):
                out.pop()
            continue
        out.append(chunk)
        last_para_norm = n
    return "".join(out), removed


def remove_kill_blocks(text: str) -> tuple[str, int]:
    """Remove --- blocks whose body (excluding hr) is only a kill fragment."""
    removed = 0
    # Split keeping --- separators
    chunks = re.split(r"(?m)^(---)\s*$", text)
    # re.split with capture: [pre, ---, post, ---, post, ...]
    if len(chunks) == 1:
        return text, 0
    rebuilt = [chunks[0]]
    i = 1
    while i < len(chunks):
        sep = chunks[i]  # '---'
        body = chunks[i + 1] if i + 1 < len(chunks) else ""
        # body runs until next ---; but split already separated
        # For kill check: take text until next heading or Appendix line or next natural end
        # Actually each 'body' is everything between this --- and next ---
        body_stripped = body.strip()
        # Only kill if the ENTIRE inter-hr region (before next ## or Appendix) is a short fragment
        # Safer: if first paragraph equals a kill fragment and the block is short (< 120 words)
        first_para = body_stripped.split("\n\n")[0].strip() if body_stripped else ""
        words = len(re.findall(r"[A-Za-z0-9']+", body_stripped))
        if first_para in KILL_FRAGMENTS and words < 80:
            removed += 1
            # skip this --- and its body
            i += 2
            continue
        rebuilt.append("\n---\n")
        rebuilt.append(body)
        i += 2
    return "".join(rebuilt), removed


def remove_duplicate_hr_blocks(text: str) -> tuple[str, int]:
    """If two --- blocks have near-identical first 200 normalized chars, drop the later one."""
    chunks = re.split(r"(?m)^(---)\s*$", text)
    if len(chunks) == 1:
        return text, 0
    seen = []
    rebuilt = [chunks[0]]
    removed = 0
    i = 1
    while i < len(chunks):
        body = chunks[i + 1] if i + 1 < len(chunks) else ""
        # fingerprint: first paragraph of body
        paras = [p.strip() for p in re.split(r"\n\n+", body.strip()) if p.strip() and p.strip() != "---"]
        fp = norm(paras[0])[:220] if paras else ""
        # skip if fingerprint matches a previous block fingerprint closely
        drop = False
        if fp and len(fp) > 60:
            for prev in seen:
                # exact or high overlap
                if fp == prev or (fp in prev) or (prev in fp):
                    drop = True
                    break
                # shared long prefix
                common = 0
                for a, b in zip(fp, prev):
                    if a == b:
                        common += 1
                    else:
                        break
                if common > 100:
                    drop = True
                    break
        if drop:
            removed += 1
            i += 2
            continue
        if fp:
            seen.append(fp)
        rebuilt.append("\n---\n")
        rebuilt.append(body)
        i += 2
    return "".join(rebuilt), removed


def tidy_blank_lines(text: str) -> str:
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    text = re.sub(r"(?m)^---\s*\n---\s*$", "---", text)
    return text.strip() + "\n"


def main():
    total_dup = total_kill = total_hr = 0
    for name in PARTS:
        p = ROOT / name
        t = p.read_text(encoding="utf-8")
        t, n1 = collapse_exact_duplicate_paragraphs(t)
        t, n2 = remove_kill_blocks(t)
        t, n3 = remove_duplicate_hr_blocks(t)
        t = tidy_blank_lines(t)
        p.write_text(t, encoding="utf-8", newline="\n")
        print(f"{name}: dup_paras={n1} kill_blocks={n2} dup_hr={n3}")
        total_dup += n1
        total_kill += n2
        total_hr += n3
    print(f"TOTAL removed: paras={total_dup} kill={total_kill} hr={total_hr}")


if __name__ == "__main__":
    main()
