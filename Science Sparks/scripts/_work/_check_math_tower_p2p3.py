import os, re
d = r"C:\Users\lomus\OneDrive\My Books for Amazon\Science Sparks\scripts\_work"
bad = re.compile(r"honest|worth noting|worth stressing|worth repeating|a bit like|almanac|condens|highlights|this volume|full edition|Part [IVX]+\b", re.I)
for f in ["06_math_tower__part2.md", "06_math_tower__part3.md"]:
    a = open(os.path.join(d, f), encoding="utf-8").read()
    b = open(os.path.join(d, "orig", f), encoding="utf-8").read()
    ha = [l for l in a.splitlines() if l.startswith("#")]
    hb = [l for l in b.splitlines() if l.startswith("#")]
    paras = [p for p in a.split("\n\n") if p.strip()]
    print(f, "orig", len(b.split()), "now", len(a.split()), "headings identical:", ha == hb,
          "em", a.count("\u2014"), "/", b.count("\u2014"))
    for p in paras:
        n = len(p.split())
        if n > 200 or (p.startswith("**Worked") and not 100 <= n <= 180):
            print("  LEN", n, p[:50])
    for m in bad.finditer(a):
        print("  TIC", m.group(0))
    print("  examples", sum(p.startswith("**Worked example.**") for p in paras))
