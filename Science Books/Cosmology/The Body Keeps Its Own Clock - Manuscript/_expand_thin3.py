from pathlib import Path
import re, os, subprocess, sys

ROOT = Path(__file__).resolve().parent

BLOCKS = {
9: ("03_Part_Three_Not_A_Straight_Line.md", r"Appendix A9 writes",
"""Real stairs, named once without a costume: childhood death became rare enough to forget in lucky kitchens — which is how it becomes possible again. A genome draft that cost a billion became a clinic invoice. Packets made delay rude and clear. Compute outran a basement and then spent the savings on a hall that drinks a river. None of that is myth. None of it is a method for year 12,000. The walls — energy, materials, attention, war — were always in the house. Keep the stair. Refuse the ruler."""),
10: ("03_Part_Three_Not_A_Straight_Line.md", r"Appendix A10 writes",
"""The steep photograph is a middle. Middles are temporary. Sequencing dollars collapsed while the act — this letter, this tissue, this trial — kept invoices. Moore’s middle was a factory calendar and a voltage that behaved; when the voltage stopped, the sermon did not apologize. Parallelism is a new S, not the old ray in a hat. Ask for the wall. Keep the S."""),
11: ("03_Part_Three_Not_A_Straight_Line.md", r"Appendix A11 writes",
"""Arithmetic abuse feels like forecasting because surprise feels like slope. Fifty years of real stairs do not multiply into a 10,000-year catalog. Rearview ratios fail the moment a wall appears. No pharmacy cashes year 12,000. Cross out the sum. Keep the invoices that will still be due: energy, coordination, a body that ages, a meeting that can fail."""),
12: ("03_Part_Three_Not_A_Straight_Line.md", r"Appendix A12 writes",
"""Institutions are a failure mode with fluorescent lights. A trial is a meeting that can store a method or lose it. War deletes both. Ledgers decide who gets a local fix this year while a transistor that made the fix possible sits outside the room. Progress is not a law that fires if we wait. Keep the table. Part IV is the body’s own invoices."""),
13: ("04_Part_Four_The_Honest_Body.md", r"^## 14\. Adjusting",
"""Staff is an S-curve you cannot download. Someone runs the apheresis, watches the liver number, teaches not-eligible without lying. Inequality is a clock. Phase 4 is the messy kitchen after the press release. Keep the receipt. The local fix is the last line — and only for the addresses that can open the door."""),
14: ("04_Part_Four_The_Honest_Body.md", r"^## 15\. Copies",
"""Rerouting costs watts, frustration, a therapist, sleep that must actually happen. Diminishing returns live in skulls too. A skill you thicken can eat the mornings you would have spent elsewhere. Overtime is the method when brands promised spare capacity. Keep the log."""),
15: ("04_Part_Four_The_Honest_Body.md", r"^## 16\. The Honest Body",
"""A photocopy of a letter does not move the sender. Forever-mind stories fuse death’s off-switch, a spare tank, and a catalog into one coat. Hang them apart. Take the restoration if Tuesday votes for it. Put the forever-mind down. Omega-ish required last minds stay cold."""),
16: ("04_Part_Four_The_Honest_Body.md", r"^Do not wait for helium\.\s*$",
"""Cash the recognitions again without helium: lifespan is not healthspan; aging is many clocks; gene fixes are local; the ten-percent sentence is false; plasticity is expensive overtime; the last fifty years were stairs not a ruler; S-curves have walls; ten thousand is not times two hundred; meetings and wars can delete methods; eligible is three words at once; a file is not a worldline. Want mornings you would vote to repeat. The radio will be late. Light does not care. You do not have to care about helium — only about the Tuesday, and about the Tuesday in the kitchen that did not get the capsule."""),
}

for n, (fn, pat, block) in BLOCKS.items():
    p = ROOT / fn
    t = p.read_text(encoding="utf-8")
    key = block.strip()[:40]
    if key in t:
        print("skip", n)
        continue
    m = re.search(pat, t, re.M)
    if not m:
        print("no", n, pat)
        continue
    t = t[: m.start()] + "---\n\n" + block.strip() + "\n\n" + t[m.start() :]
    p.write_text(t, encoding="utf-8", newline="\n")
    print("ins", n)


def wc(text):
    body = re.sub(r"!\[.*?\]\(.*?\)", " ", text)
    body = re.sub(r"^#+\s+.*$", " ", body, flags=re.M)
    return len(re.findall(r"[A-Za-z0-9\u2019']+", body))


def sizes(text):
    out = []
    for sec in re.split(r"(?=^##\s+)", text, flags=re.M):
        m = re.match(r"^##\s+(\d+)\.\s+", sec, re.M)
        if not m:
            continue
        n = int(m.group(1))
        body = re.sub(r"!\[.*?\]\(.*?\)", " ", sec)
        body = re.sub(r"^#+\s+.*$", " ", body, flags=re.M)
        out.append((n, len(re.findall(r"[A-Za-z0-9\u2019']+", body))))
    return out


parts = [
    f for f in sorted(os.listdir(ROOT))
    if re.match(r"^\d{2}_", f) and f.endswith(".md")
    and f not in ("00_Chapter_Outline.md", "00_Figure_Plan.md", "00_Status.md")
]
big = "\n\n".join((ROOT / p).read_text(encoding="utf-8") for p in parts)
total = wc(big)
print("TOTAL", total)
thin = []
for n, w in sizes(big):
    print(f"Ch {n:02d} {w:5d}{' THIN' if w < 1500 else ''}")
    if w < 1500:
        thin.append((n, w))
print("thin", thin)
st = (ROOT / "00_Status.md").read_text(encoding="utf-8")
st = re.sub(r"\*\*[\d,]+ words\*\*", f"**{total:,} words**", st)
st = re.sub(r"Thin leftovers \(if any\):.*", f"Thin leftovers (if any): {thin or 'none'}.", st)
(ROOT / "00_Status.md").write_text(st, encoding="utf-8", newline="\n")
r = subprocess.run([sys.executable, str(ROOT / "Figures" / "build_book.py"), "body"], capture_output=True, text=True)
print(r.stdout)
print("exit", r.returncode)
