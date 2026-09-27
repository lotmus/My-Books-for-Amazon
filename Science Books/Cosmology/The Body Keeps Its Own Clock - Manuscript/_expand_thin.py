"""Book 3: real teaching inserts for thin chapters (no clone padding)."""
from pathlib import Path
import re, os, subprocess, sys
from collections import defaultdict

ROOT = Path(r"D:\My Books for Amazon\Science Books\Cosmology\The Body Keeps Its Own Clock - Manuscript")

# Unique teaching blocks sized to clear shortfalls with margin
MORE = {
2: """Healthspan is the product you thought you bought when the wall clock lost. A pulse that lasts is not a Tuesday you would vote to repeat. Demographers already split the pots; marketers glue them. Ask for HALE, or for the morning test, before you pay for a calendar. The 122-year fence is a tail, not a ship date. Averages rose mostly by sparing the young. That leap is mostly finished where pipes already run.""",
4: """A class-of-edit is paperwork with scissors: consent, a vector, an off-target worry, sometimes a marrow wipe that can kill on the way to a save. The win is this lineage of cells keeping the correction. It is not a downtown for the organism. Delivery is half the invoice. Headline CRISPR is incense. Print local again before the next slide.""",
5: """Cancer is plural doors. Vessels are arithmetic with blood. Brains are overlapping messes without a single SKU. Aging is not one lock. Triage and local repair stay hot because they land at addresses. A skeleton key stays cold because it has nowhere to ship. Chapter 4 opened one honest door. This chapter refuses to sell the house as unlocked.""",
7: """Enhancement that is warm has a scar and a schedule: sleep that consolidates, a hearing aid that returns a room, a stimulant with a crash, a stimulator that quiets a tremor. Enhancement that is cold promises a spare loft. Tools are not confessions. They are overtime with hardware. The false ten-percent sentence keeps trying to rent the loft. Keep the toolbox. Evict the loft.""",
9: """Stairs have landings where methods survive. Vaccines, genomes, packets, and cheaper compute climbed real flights. Energy, materials, attention, institutions, and war are walls and rest spots, not optional footnotes. Uneven gains are still gains. A ruler painted to year 12,000 skips both the landing and the wall. Keep the stair underfoot. Leave the rocket costume on the sales floor. History is flights with rest, not a continuous ray sold by the yard.""",
10: """Drunk middles photograph like destiny. Walls do not. Sequencing got cheap; clinics did not get two hundred times cheaper in the same breath. Compute bent when watts stopped being polite. Logistic curves are rude to founders who need a ray. When someone shows the steep bit, ask for the wall’s address: cost, energy, regulation, attention, war. Keep the S. Cash the middle only as a middle.""",
11: """Felt is surprise, not slope. The last fifty years felt larger than a lifetime because the kitchen changed underfoot. Name a sport — vaccines, compute, sequencing — and the ratio fails when walls appear. There is no catalog for year 12,000 that a body can cash. Extrapolation without a wall is a costume. Invoices only.""",
12: """Meetings store methods: trials, ledgers, not shooting the technician when the result is ugly. When meetings fail, knowledge dies in public. War is a delete key. Germline talk is a front among ledgers, not a download. The transistor that made a win possible is often missing from the budget slide that claims the win. Coordination is the limit more often than the enzyme.""",
13: """Eligible is biological, geographic, and insurance at once. A wall of wins sits beside letters that say not eligible in a neutral font. Boring wins — blood pressure, vaccines, affordable surgeons — stay hot because they land. Helium stays cold. Delivery of payment is this chapter’s truck. Delivery of molecule was Chapter 4’s. A molecule without a route is a press release.""",
14: """Plasticity is overtime, not a loft. Twelve wrong tries, then a right one. Sleep consolidates. Stroke recovery costs years of ugly work. A child’s site reroutes cheaper than an adult office. Brands sell spare capacity; clinics log overtime. The notebook is the spare that keeps showing up. Water still has to melt.""",
15: """Three colds share a coat because the coat photographs well: death’s off-switch, a spare mind, a catalog to year 12,000. Hang them apart and each must earn a temperature. Restorations stay local and warm. A copy is not travel. Required last minds stay cold. Bodies end. Keep the coat off the repair bench.""",
16: """Last inventory before the seal: capsule late, label optimistic, joint a two not an eight, Tuesday worth voting for, no spare mind, notebook yes, file-that-is-her no, year 12,000 no. That count is the honest body — not small, the only size reliably for sale. Do not wait for helium seals the jar. It does not replace the count.""",
}

NEEDLES = {
2: ("01_Part_One_Many_Clocks.md", r"Appendix A2 writes"),
4: ("01_Part_One_Many_Clocks.md", r"Appendix A4 writes"),
5: ("01_Part_One_Many_Clocks.md", r"Appendix A5 writes"),
7: ("02_Part_Two_The_Organ_You_Already_Use.md", r"Appendix A7 writes"),
9: ("03_Part_Three_Not_A_Straight_Line.md", r"Appendix A9 writes"),
10: ("03_Part_Three_Not_A_Straight_Line.md", r"Appendix A10 writes"),
11: ("03_Part_Three_Not_A_Straight_Line.md", r"Appendix A11 writes"),
12: ("03_Part_Three_Not_A_Straight_Line.md", r"Appendix A12 writes"),
13: ("04_Part_Four_The_Honest_Body.md", r"Appendix A13 writes"),
14: ("04_Part_Four_The_Honest_Body.md", r"Appendix A14 writes"),
15: ("04_Part_Four_The_Honest_Body.md", r"Appendix A15 writes"),
16: ("04_Part_Four_The_Honest_Body.md", r"^Do not wait for helium\.\s*$"),
}

by = defaultdict(list)
for n, (fn, ndl) in NEEDLES.items():
    by[fn].append((n, ndl, MORE[n]))

for fn, items in by.items():
    p = ROOT / fn
    t = p.read_text(encoding="utf-8")
    plans = []
    for n, ndl, block in items:
        m = re.search(ndl, t, re.M)
        if not m:
            print("no", n)
            continue
        # skip if this exact block already present
        if block.strip()[:60] in t:
            print("skip", n)
            continue
        plans.append((m.start(), n, block))
    plans.sort(reverse=True)
    for pos, n, block in plans:
        t = t[:pos] + "---\n\n" + block.strip() + "\n\n" + t[pos:]
        print("ins", n)
    p.write_text(t, encoding="utf-8", newline="\n")


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
    f
    for f in sorted(os.listdir(ROOT))
    if re.match(r"^\d{2}_", f)
    and f.endswith(".md")
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
if "Thin leftovers" in st:
    st = re.sub(r"Thin leftovers \(if any\):.*", f"Thin leftovers (if any): {thin or 'none'}.", st)
else:
    st += f"\n\nThin leftovers (if any): {thin or 'none'}.\n"
(ROOT / "00_Status.md").write_text(st, encoding="utf-8", newline="\n")
r = subprocess.run(
    [sys.executable, str(ROOT / "Figures" / "build_book.py"), "body"],
    capture_output=True,
    text=True,
)
print(r.stdout)
print("exit", r.returncode)
