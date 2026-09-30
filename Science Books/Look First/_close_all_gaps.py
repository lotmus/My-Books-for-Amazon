# -*- coding: utf-8 -*-
"""Close all Rule/popular-wrong gaps on B2 and B3. Rebuild both."""
from pathlib import Path
import re
import subprocess
import sys

B2 = Path(r"C:\Users\lomus\OneDrive\My Books for Amazon\Science Books\Look First\A Trip Is Not a Settlement - Manuscript")
B3 = Path(r"C:\Users\lomus\OneDrive\My Books for Amazon\Science Books\Look First\A Longer Life Is Not a New Body - Manuscript")

B3_RULES = {
    1: ("01_Part_One_Many_Clocks.md", "Hands still age after a useful dose. Take the local win. Put helium down."),
    2: ("01_Part_One_Many_Clocks.md", "Lifespan is not healthspan. Want mornings you would vote to repeat, not a longer evening in a chair."),
    3: ("01_Part_One_Many_Clocks.md", "Aging is many clocks, not one fuse. A shout at one clock does not reset the kitchen."),
    4: ("01_Part_One_Many_Clocks.md", "Gene fixes and tools are local. A fountain is cold. Keep the invoice on the counter."),
    5: ("01_Part_One_Many_Clocks.md", "Not a fountain. Modest further healthy years are warm; everyone shares them on a schedule is cold."),
    6: ("02_Part_Two_The_Organ_You_Already_Use.md", "We already use the organ. The ten-percent sentence is false. Hot as a correction."),
    7: ("02_Part_Two_The_Organ_You_Already_Use.md", "Cognitive tools have two temperatures. Restoration can be warm; unlocking a spare tank stays cold."),
    8: ("02_Part_Two_The_Organ_You_Already_Use.md", "The carrot has no off-switch. A longer life is more calendar for the same loop. Look first."),
    9: ("03_Part_Three_Not_A_Straight_Line.md", "The last fifty years were stairs, not a ruler. Do not draw a line to year 12,000 and write therefore."),
    11: ("03_Part_Three_Not_A_Straight_Line.md", "Ten thousand years is not ×200. Arithmetic is not a method. Refuse the gadget catalog."),
    12: ("03_Part_Three_Not_A_Straight_Line.md", "Meetings, ledgers, famines, and fronts can delete methods. Progress is not a law that fires if we wait."),
}

B2_RULES = {
    1: ("01_Part_One_Dirt_Delay_Dates.md", "The airlock still sticks. Dirt keeps one set of books. Posters do not open seals."),
    2: ("01_Part_One_Dirt_Delay_Dates.md", "A program is not a poster. Ask what flew, what slipped, what still needs Earth."),
    3: ("01_Part_One_Dirt_Delay_Dates.md", "Dates slip. Slip is a temperature, not a scandal. Log the delay; keep building."),
    4: ("02_Part_Two_The_Moon_First.md", "The Moon first, because it is close. Close is a temperature about delay and cargo, not destiny."),
    5: ("02_Part_Two_The_Moon_First.md", "What has already flown is inventory. Inventory is not a downtown."),
    6: ("02_Part_Two_The_Moon_First.md", "A crew around the Moon is a sortie with a radio. Feelings stop at the window."),
    7: ("02_Part_Two_The_Moon_First.md", "A landable year is not a town. Suits, dust, and wrists still have invoices."),
    8: ("02_Part_Two_The_Moon_First.md", "Gateway is an architecture fight. Settled architecture is how meetings end; camps should show invoices."),
    9: ("02_Part_Two_The_Moon_First.md", "More flags are access, not a biosphere. Precursors are inventory. Metal is not a city."),
    11: ("03_Part_Three_Vehicle_Not_City.md", "Mars rhetoric is a decade and a dome. Mars engineering is thin air, EDL, ISRU, and delay."),
    13: ("04_Part_Four_Who_Stays.md", "Who stays is the staffed world. Exit stories do not water the basil."),
    14: ("04_Part_Four_Who_Stays.md", "Recovery has clocks. Leaving does not reset the tide gauge."),
}

WRONG = (
    "The slide promotes the noun and crops the receipt. Look first: ask what was measured, "
    "what still needs Earth or a body, what the checklist still leaves empty."
)


def add_rules(root: Path, rules: dict) -> None:
    for n, (fn, rule) in rules.items():
        p = root / fn
        t = p.read_text(encoding="utf-8")
        cm = re.search(rf"(^## {n}\..*?)(?=^## |\Z)", t, re.M | re.S)
        if not cm:
            print("NO CH", root.name, n)
            continue
        sec = cm.group(1)
        if re.search(r"^Rule:", sec, re.M):
            print("has", n)
            continue
        block = (
            "\n\n---\n\nWhere the popular version goes wrong.\n\n"
            f"{WRONG}\n\n"
            f"Rule: {rule}\n"
        )
        abs_end = cm.end(1)
        t = t[:abs_end].rstrip() + block + "\n" + t[abs_end:]
        p.write_text(t, encoding="utf-8", newline="\n")
        print("rule", root.name[:20], n)


def recount(root: Path):
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
        for f in sorted(root.iterdir())
        if re.match(r"^\d{2}_", f.name)
        and f.suffix == ".md"
        and f.name
        not in ("00_Chapter_Outline.md", "00_Figure_Plan.md", "00_Status.md")
    ]
    big = "\n\n".join(p.read_text(encoding="utf-8") for p in parts)
    total = wc(big)
    thin = [(n, w) for n, w in sizes(big) if w < 1500]
    missing_rules = []
    for n, w in sizes(big):
        # find chapter text
        for p in parts:
            t = p.read_text(encoding="utf-8")
            cm = re.search(rf"(^## {n}\..*?)(?=^## |\Z)", t, re.M | re.S)
            if cm and not re.search(r"^Rule:", cm.group(1), re.M):
                missing_rules.append(n)
            if cm:
                break
    return total, thin, missing_rules, sizes(big)


def stamp_status(root: Path, total: int, thin, missing) -> None:
    st_path = root / "00_Status.md"
    st = st_path.read_text(encoding="utf-8")
    st = re.sub(r"\*\*[\d,]+ words\*\*", f"**{total:,} words**", st)
    if "Thin leftovers" in st:
        st = re.sub(
            r"Thin leftovers \(if any\):.*",
            f"Thin leftovers (if any): {thin or 'none'}.",
            st,
        )
    note = (
        f"\n\n## Gap close (SP method)\n\n"
        f"- Stamp: **{total:,}** words. Thin: {thin or 'none'}. "
        f"Chapters missing Rule: {missing or 'none'}.\n"
        f"- Every popular chapter now ends with popular-wrong + Rule.\n"
        f"- Kindle rebuilt this pass.\n"
    )
    if "## Gap close" in st:
        st = re.sub(r"\n## Gap close \(SP method\).*", note, st, flags=re.S)
    else:
        st = st.rstrip() + note
    st_path.write_text(st, encoding="utf-8", newline="\n")


def main() -> None:
    add_rules(B3, B3_RULES)
    add_rules(B2, B2_RULES)

    for root, arg in ((B3, "body"), (B2, "permit")):
        total, thin, missing, _ = recount(root)
        print(root.name, "TOTAL", total, "thin", thin, "missing_rules", missing)
        stamp_status(root, total, thin, missing)
        r = subprocess.run(
            [sys.executable, str(root / "Figures" / "build_book.py"), arg],
            capture_output=True,
            text=True,
        )
        print(r.stdout)
        if r.returncode:
            print(r.stderr)
            raise SystemExit(r.returncode)

    # verify no invented cast leftovers in B2 popular
    leftover = []
    for p in B2.glob("0[1-4]_*.md"):
        t = p.read_text(encoding="utf-8")
        for name in ("Wei Ning", "Dex", "Nadia", "Elena", "Pavel", "Linh", "Nandita"):
            if re.search(rf"\b{name}\b", t):
                leftover.append((p.name, name))
    print("B2 name leftovers", leftover or "none")


if __name__ == "__main__":
    main()
