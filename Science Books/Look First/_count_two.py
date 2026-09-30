import os, re
root = os.path.dirname(os.path.abspath(__file__))
books = [
    "A Trip Is Not a Settlement - Manuscript",
    "A Longer Life Is Not a New Body - Manuscript",
]

def words(t):
    t = re.sub(r"!\[.*?\]\(.*?\)", " ", t)
    return len(re.findall(r"[A-Za-z0-9']+", t))

for b in books:
    p = os.path.join(root, b)
    print("==", b)
    total = 0
    for fn in sorted(os.listdir(p)):
        if not fn.endswith(".md"):
            continue
        if not (fn[:2].isdigit() or fn.startswith("00_Front") or fn.startswith("11_")):
            continue
        text = open(os.path.join(p, fn), encoding="utf-8").read()
        print(f"  {fn}: {words(text)}")
        if re.match(r"0[1-9]_|10_", fn):
            for part in re.split(r"\n(?=## )", text):
                m = re.match(r"## (.+)", part)
                if m:
                    print(f"    {m.group(1)[:72]}: {words(part)}")
        total += words(text)
    print("  TOTAL", total)
