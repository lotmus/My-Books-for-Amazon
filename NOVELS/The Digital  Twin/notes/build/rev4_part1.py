import glob, io, os, sys
CH = r"C:\Users\lomus\wt-dt4\NOVELS\The Digital  Twin\chapters"

def path(prefix):
    m = glob.glob(os.path.join(CH, prefix + "_*.md"))
    assert len(m) == 1, (prefix, m)
    return m[0]

def rep(prefix, old, new):
    p = path(prefix)
    with io.open(p, "r", encoding="utf-8", newline="") as f:
        t = f.read()
    nl = "\r\n" if "\r\n" in t else "\n"
    o = old.replace("\n", nl)
    n = new.replace("\n", nl)
    c = t.count(o)
    if c != 1:
        print("FAIL", prefix, c, old[:70])
        sys.exit(1)
    t = t.replace(o, n)
    with io.open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t)
    print("ok", prefix, old[:50].replace("\n", " "))