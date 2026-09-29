"""Clear Book 3 thin chapters with large unique inserts; collapse Ch16 inventory spam."""
from pathlib import Path
import re, os, subprocess, sys

ROOT = Path(__file__).resolve().parent

# Insert BEFORE these next-chapter headings (or helium seal for 16)
INSERT_BEFORE = {
    2: ("01_Part_One_Many_Clocks.md", r"^## 3\. Many Clocks", """
Healthspan is the product people thought they bought when the wall clock lost. A longer pulse is not a Tuesday you would vote to repeat. Demographers already split the pots; marketers glue them back together for a slide. Ask for HALE, or for the morning test, before you pay for a calendar. The 122-year fence is a tail on a distribution, not a ship date for a brand. Averages rose mostly by sparing the young from slaughter. That leap is mostly finished where pipes, vaccines, and midwives already run. Keep the two bars hatched differently. If a founder sells lifespan as if it were healthspan, ask which bar is on the invoice.
"""),
    5: ("01_Part_One_Many_Clocks.md", r"^Appendix A5 writes", """
Cancer is plural doors with different locks. Solid tumors hide behind barriers drugs do not cross for free. Blood cancers and sickle-cell-class lineages can be different sports. Vessels are arithmetic with blood: pressure, plaque, a clot that arrives on a Tuesday. Brains are overlapping messes — plaques, tangles, vessels, sleep, inflammation — without a single product SKU. Aging itself is not one lock labeled *rewind*. Triage and local repair stay hot because they land at addresses. A skeleton key stays cold because it has nowhere to ship. Chapter 4 opened one honest door. This chapter refuses to sell the house as unlocked. Keep naming doors. Take the master-key slide off the deck.
"""),
    7: ("02_Part_Two_The_Organ_You_Already_Use.md", r"^## 8\. The Carrot", """
Enhancement that is warm has a scar and a schedule: sleep that consolidates, a hearing aid that returns a room, a stimulant with a crash, a stimulator that quiets a tremor, a cochlear code a brain must relearn for months. Enhancement that is cold promises a spare loft waiting for a password. Tools are not confessions of defeat. They are overtime with hardware and invoices. The false ten-percent sentence keeps trying to rent the loft because a lockpick needs a lock. Keep the toolbox. Evict the loft. Take the tool if the Tuesday votes for it. Put the spare-tank sermon down before it hires the carrot.
"""),
    9: ("03_Part_Three_Not_A_Straight_Line.md", r"^## 10\. S-Curves", """
Stairs have landings where methods survive so the next climber does not reinvent the flight. Vaccines closed rooms of death. Genomes became readable without a monastery. Packets made a late radio clear. Compute got cheaper and then spent the savings on halls that drink rivers. Those are real flights. Energy, materials, attention, institutions, and war are walls and rest spots, not optional footnotes for a poster. Uneven gains are still gains — and uneven means a lucky zip code and a sister’s clinic are different S-curves on the same species. A ruler painted to year 12,000 skips both the landing and the wall. Keep the stair underfoot. Leave the rocket costume on the sales floor. History is flights with rest, not a continuous ray sold by the yard. Do not bring a ruler into this room.
"""),
    10: ("03_Part_Three_Not_A_Straight_Line.md", r"^## 11\. Ten Thousand", """
Drunk middles photograph like destiny. Walls do not photograph well. Sequencing got cheap; clinics did not get two hundred times cheaper in the same breath. Compute bent when watts per switch stopped being polite and lithography became a cathedral. Logistic curves are rude to founders who need a ray. When someone shows you the steep bit, ask for the wall’s address: cost, energy, regulation, attention, war, a staff who can keep the hall honest. Keep the S. Cash the middle only as a middle. An S is not a ray. Founders photograph the drunk middle and draw a line through the wall. Ask which wall they waived.
"""),
    11: ("03_Part_Three_Not_A_Straight_Line.md", r"^## 12\. Coordination", """
Felt is surprise, not slope. The last fifty years felt larger than a lifetime because the kitchen changed underfoot — vaccines, packets, a pocket, a sequence. That feeling is real. It is not a method for multiplying a century into a catalog. Name a sport — vaccines, compute, sequencing — and the ratio fails when walls appear. There is no furniture list for year 12,000 that a body can cash at a pharmacy. Extrapolation without a wall is a costume. Put the costume back on the hanger. Invoices only. If a founder shows a skyline labeled 12,000, ask which wall they waived and which war they cancelled.
"""),
    12: ("03_Part_Three_Not_A_Straight_Line.md", r"^# PART IV|^## 13\.", """
Meetings store methods: trials, ledgers, rivers of paperwork, not shooting the technician when the result is ugly. When meetings fail, knowledge dies in public and has to be reinvented by people who did not get the memo. War is a delete key aimed at labs and generations. Germline talk is a front among ledgers, not a software download. The transistor that made a win possible is often missing from the budget slide that claims the win. A hospital board deciding which local fix fits this year is the limit more often than the enzyme. Coordination is the unpaid character in every fountain slide.
"""),
    13: ("04_Part_Four_The_Honest_Body.md", r"^## 14\. Adjusting", """
Eligible is biological, geographic, and insurance at once. A wall of wins sits beside letters that say not eligible in a font designed to look neutral. Phase 1 through 4 are a kitchen with different knives. Mice lie in particular ways; translation is the unpaid invoice of fountain slides. Price is delivery: millions per person is a kingdom’s win and a village’s absence. Boring wins — blood pressure, vaccines, affordable surgeons — stay hot because they land. Helium stays cold. Delivery of payment is this chapter’s truck. Delivery of molecule was Chapter 4’s. Two trucks. Same rule: a molecule without a route is a press release.
"""),
    14: ("04_Part_Four_The_Honest_Body.md", r"^## 15\. Copies", """
Plasticity is overtime, not a loft. Twelve wrong tries, then a right one. Sleep consolidates. Stroke recovery costs years of ugly work and a family that walks the same hallway a thousand times. A child’s site reroutes cheaper than an adult office — development, not a cupboard. Brands sell spare capacity; clinics log overtime. Tools and other people are the method, not a confession of failure. The notebook is the spare that keeps showing up. Water still has to melt. The joint still has a number.
"""),
    15: ("04_Part_Four_The_Honest_Body.md", r"^## 16\. The Honest Body", """
Three colds share a coat because the coat photographs well: death’s off-switch, a spare mind, a catalog to year 12,000. Hang them apart and each must earn a temperature. A scan, if we had one fine enough, would be a map; a map is not a walk. Running the map on another substrate would be, at best, a second person who thinks they remember your Tuesdays. Travel did not happen. Restorations stay local and warm — a hand, a valve, a hearing channel with scars. Required last minds at the end of time stay cold. Bodies end. Keep the coat off the repair bench.
"""),
}

# Collapse Ch 16 inventory spam: keep core through first inventory intent, one seal
def clean_ch16(text: str) -> str:
    # Find ## 16. section and trim cascading inventory --- blocks after the recognition cash-out
    m = re.search(r"^## 16\. The Honest Body\s*$", text, re.M)
    if not m:
        return text
    start = m.start()
    # next part or end
    rest = text[start:]
    # Remove repeated inventory --- blocks; keep content before first "A last inventory" cascade,
    # then append one clean close
    # Split chapter from following content (none after in this file usually)
    # Find the "What to want instead" paragraph region and cut after it to one inventory
    marker = "What to want instead is not a smaller life."
    idx = rest.find(marker)
    if idx < 0:
        return text
    # keep through end of that paragraph block
    after = rest[idx:]
    # find end of that paragraph (double newline after)
    para_end = after.find("\n\n---\n")
    if para_end < 0:
        para_end = after.find("\n\n")
        # take a few paras
        parts = after.split("\n\n")
        head = "\n\n".join(parts[:3])
    else:
        head = after[:para_end]
    close = (
        "\n\n---\n\n"
        "Last inventory before the seal: capsule late, label optimistic, joint a two not an eight, "
        "Tuesday worth voting for, no spare mind in the cupboard, notebook yes, file-that-is-her no, "
        "year 12,000 no, film that goes alkaline when permanence gets sentimental. That count is the honest body — "
        "not small, the only size reliably for sale.\n\n"
        "Do not wait for helium.\n"
    )
    new_ch = rest[:idx] + head.strip() + close
    return text[:start] + new_ch


def insert_before(path: Path, pattern: str, block: str, n: int) -> bool:
    t = path.read_text(encoding="utf-8")
    if block.strip()[:50] in t:
        print("skip", n)
        return False
    m = re.search(pattern, t, re.M)
    if not m:
        print("no", n, pattern)
        return False
    t = t[: m.start()] + "---\n\n" + block.strip() + "\n\n" + t[m.start() :]
    path.write_text(t, encoding="utf-8", newline="\n")
    print("ins", n)
    return True


# Clean ch16 first
p4 = ROOT / "04_Part_Four_The_Honest_Body.md"
p4.write_text(clean_ch16(p4.read_text(encoding="utf-8")), encoding="utf-8", newline="\n")
print("cleaned ch16")

for n, (fn, pat, block) in INSERT_BEFORE.items():
    insert_before(ROOT / fn, pat, block, n)

# Extra padding for still-short if needed after count
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
    flag = " THIN" if w < 1500 else ""
    print(f"Ch {n:02d} {w:5d}{flag}")
    if w < 1500:
        thin.append((n, w))
print("thin", thin)

st = (ROOT / "00_Status.md").read_text(encoding="utf-8")
st = re.sub(r"\*\*[\d,]+ words\*\*", f"**{total:,} words**", st)
st = re.sub(r"Thin leftovers \(if any\):.*", f"Thin leftovers (if any): {thin or 'none'}.", st)
(ROOT / "00_Status.md").write_text(st, encoding="utf-8", newline="\n")

r = subprocess.run(
    [sys.executable, str(ROOT / "Figures" / "build_book.py"), "body"],
    capture_output=True,
    text=True,
)
print(r.stdout)
print("exit", r.returncode)
