import sys, os, re, json, concurrent.futures as cf
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gen

B = os.path.dirname(HERE)
STORY_DIR = os.path.join(B, "Step_Stories_Texts")
STORY = os.path.join(STORY_DIR, sorted(f for f in os.listdir(STORY_DIR) if f.endswith(".txt"))[-1])
REF = os.path.join(B, "Step_Stories_Pics_Final", "reference_cast_sheet_b3.jpg")
REF0 = os.path.join(B, "Step_Stories_Pics_Final", "reference_cast_sheet.jpg")
PLAN = os.path.join(B, "build", "b3_plan.json")
STEP = 150

STYLE = ("Rich, highly detailed oil-painting style classic fantasy storybook illustration, textured brushwork, warm natural light with a little adventure, never gloomy, "
         "any sign, bottle label or slate is left blank or shows only meaningless scribbles, never real words. Illustrate exactly the action and the place described in the passage, indoors if the passage is indoors, in the village, at the mill, on a snowy pond or in a cave as the text says. "
         "COMPOSITION: ONE single candid dynamic moment caught mid-action, a varied camera angle, figures at different heights and distances, nobody looking at the viewer, "
         "never lined up or posed in a row, not a group portrait. ")
LEGEND = {
    "Hal": "Hal (tousled brown hair, freckles, patched blue jacket, a slate)",
    "Titch": "Titch (dark hair, red knitted cap pulled down over her ears so no ears show, yellow scarf, green coat)",
    "Tabitha": "Tabitha (curly black hair in a bun with a rust band, dark skin, gray coat)",
    "Pip": "Pip (small seven-year-old boy, dark hair, plain red knitted cap pulled down snugly over his ears so no ears show at all, small brown boots)",
    "Wen": "Wen (thin nine-year-old boy of East Asian heritage, straight black hair, dark blue wool coat, tool roll on his belt)",
    "Hopsi": "Hopsi (elf girl, long wavy light-brown hair with a hops wreath, pointed ears, green dress, purple scarf)",
    "Scally": "Scally (little devil, messy brown hair with a leaf, big pointed ears, mossy olive-brown hooded tunic, big old brown boots)",
    "Gucci": "Gucci (young gray wolf as big as a large dog, not a small puppy, blue eyes, one floppy ear)",
    "Dr. Liang": "Dr Liang (small brisk East Asian woman, black hair in a bun, long blue coat, black doctor's bag)",
    "Mrs. Crumb": "Mrs Crumb the baker (big floury cheerful woman of European heritage)",
    "Mayor": "Mayor Pomfrey (round pink European man, big mustache, waistcoat, gold chain of office)",
    "Hal's mother": "Hal's mother (warm weathered European woman in a kerchief)",
    "Hal's father": "Hal's father (stocky European man with a limp and a cane)",
    "Titch's mother": "Titch's mother (small freckled European woman, very round with a baby coming)",
    "Titch's father": "Titch's father (large quiet European man with soot on his hands)",
    "Fourpence": "Fourpence (a small plain brown bird)",
}
ALL_KIDS = ["Hal", "Titch", "Tabitha", "Pip", "Wen", "Scally", "Hopsi"]
EARS = "EAR RULE: only Scally and Hopsi have pointed ears; every other person has small round human ears. "


def cast_for(text):
    t = text.replace("’", "'")
    names = []
    for k in LEGEND:
        if k in ("Hal", "Titch"):
            if re.search(r"\b" + k + r"\b(?!'s (mother|father))", t):
                names.append(k)
        elif k == "Mayor":
            if re.search(r"\bMayor\b|Pomfrey", t):
                names.append(k)
        elif k == "Dr. Liang":
            if "Dr. Liang" in t or "Dr Liang" in t:
                names.append(k)
        elif k in t:
            names.append(k)
    if re.search(r"\bchildren\b", t):
        for k in ALL_KIDS:
            if k not in names:
                names.append(k)
    if re.search(r"\b(his|Hal's) mother\b", t) and "Hal's mother" not in names and "Titch's mother" not in names:
        names.append("Hal's mother")
    if re.search(r"\b(his|Hal's) father\b", t) and "Hal's father" not in names:
        names.append("Hal's father")
    if re.search(r"\bhis mother\b", t) and "Titch's mother" in names and "Titch" in names:
        pass
    return names


def paragraphs():
    raw = open(STORY, encoding="utf-8").read()
    body = raw[raw.index("Chapter 1."):]
    cut = "\nHal’s Slate: What We Found Out"
    if cut in body:
        body = body[:body.index(cut)]
    return [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]


def make_plan():
    paras = paragraphs()
    plan, since, chap = [], 0, 0
    for i, p in enumerate(paras):
        if p.startswith("Chapter "):
            chap += 1
            since = STEP
            continue
        if p == "---" or p == "The End":
            continue
        w = len(p.split())
        since += w
        if since >= STEP and w >= 20 and not p.isupper():
            prev = paras[i - 1] if i and not paras[i - 1].startswith("Chapter ") and paras[i - 1] != "---" else ""
            n = 45
            while sum(1 for q in paras if q.startswith(p[:n])) > 1 and n < len(p):
                n += 10
            plan.append({"n": len(plan) + 1, "chap": chap, "key": p[:n], "prev": " ".join(prev.split()[:60]), "text": " ".join(p.split()[:110])})
            since = 0
    json.dump(plan, open(PLAN, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return plan


def prompt(e):
    txt = (e["prev"] + " " if e["prev"] else "") + e["text"]
    names = cast_for(e["text"])
    if not names:
        names = cast_for(e["prev"])
    if names:
        people = [n for n in names if n != "Gucci" and n != "Fourpence"]
        extra = [n for n in names if n in ("Gucci", "Fourpence")]
        count = "Exactly %d %s in the picture" % (len(people), "person" if len(people) == 1 else "people")
        if "Gucci" in extra:
            count += " and one wolf"
        if "Fourpence" in extra:
            count += " and one small bird"
        who = (count + ", and absolutely nobody else (do not draw any other character from the reference painting, no extra children, no extra adults): "
               + "; ".join(LEGEND[n] for n in names) + ". Use the reference painting only for how these characters look. ")
    else:
        who = "Show only the place and objects described, with no people in the picture. "
    return STYLE + who + EARS + "Passage to illustrate: " + txt


def run(e):
    from PIL import Image
    name = "p%03d_ch%02d" % (e["n"], e["chap"])
    out = os.path.join(gen.OUT, name + ".jpg")
    if os.path.exists(out):
        try:
            Image.open(out).verify()
            return name + " exists"
        except Exception:
            os.remove(out)
    for attempt in range(4):
        try:
            ref = REF if re.search(r"Wen|Dr\. Liang|Dr Liang", e["text"] + e["prev"]) else REF0
            if gen.edit_with(name, ref, prompt(e), "3:2"):
                Image.open(out).verify()
                return name + " ok"
        except Exception as ex:
            print(name, "retry", attempt, type(ex).__name__, flush=True)
            if os.path.exists(out):
                os.remove(out)
    return name + " FAILED"


if __name__ == "__main__":
    if sys.argv[1:2] == ["plan"]:
        pl = make_plan()
        print(len(pl), "pictures planned")
        sys.exit()
    plan = json.load(open(PLAN, encoding="utf-8"))
    sel = plan
    if len(sys.argv) > 2:
        a, b = int(sys.argv[1]), int(sys.argv[2])
        sel = [e for e in plan if a <= e["n"] <= b]
    with cf.ThreadPoolExecutor(4) as ex:
        for r in ex.map(run, sel):
            print(r, flush=True)
