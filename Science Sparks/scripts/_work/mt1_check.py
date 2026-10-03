base = r"D:\My Books for Amazon\Science Sparks\scripts\_work"
name = "06_math_tower__part1.md"
o = open(base + "\\orig\\" + name, encoding="utf-8").read()
t = open(base + "\\" + name, encoding="utf-8").read()
print("words before", len(o.split()), "after", len(t.split()), "emdashes", t.count("\u2014"))
for para in t.split("\n\n"):
    n = len(para.split())
    if para.startswith("**Worked example.**"):
        print("example", n)
    elif n > 200:
        print("LONG", n, para[:50])
oh = [l for l in o.splitlines() if l.startswith("#")]
wh = [l for l in t.splitlines() if l.startswith("#")]
print("headings identical:", oh == wh, len(wh))
