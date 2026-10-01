from pathlib import Path
import re, os
ROOT = Path(r"C:\Users\lomus\OneDrive\My Books for Amazon\Science Books\Look First\A Longer Life Is Not a New Body - Manuscript")
def wc(text):
    body=re.sub(r"!\[.*?\]\(.*?\)"," ",text); body=re.sub(r"^#+\s+.*$"," ",body,flags=re.M)
    return len(re.findall(r"[A-Za-z0-9\u2019']+",body))
def sizes(text):
    out=[]
    for sec in re.split(r"(?=^##\s+)", text, flags=re.M):
        m=re.match(r"^##\s+(\d+)\.\s+", sec, re.M)
        if not m: continue
        n=int(m.group(1)); body=re.sub(r"!\[.*?\]\(.*?\)"," ",sec); body=re.sub(r"^#+\s+.*$"," ",body,flags=re.M)
        out.append((n,len(re.findall(r"[A-Za-z0-9\u2019']+",body))))
    return out
parts=[f for f in sorted(os.listdir(ROOT)) if re.match(r"^\d{2}_",f) and f.endswith(".md") and f not in ("00_Chapter_Outline.md","00_Figure_Plan.md","00_Status.md")]
big="\n\n".join((ROOT/p).read_text(encoding="utf-8") for p in parts)
print("TOTAL", wc(big))
thin=[]
for n,w in sizes(big):
    print(f"Ch {n:02d} {w:5d}{' THIN' if w<1500 else ''}")
    if w<1500: thin.append((n,w))
print("thin", thin)
# find exact duplicate paragraphs bookwide
paras=[]
for p in parts:
    t=(ROOT/p).read_text(encoding="utf-8")
    for para in re.split(r"\n\n+", t):
        para=para.strip()
        if len(para)<80 or para.startswith("#") or para.startswith("![") or para=="---": continue
        paras.append(para)
from collections import Counter
c=Counter(paras)
dups=[(n,p[:100]) for p,n in c.items() if n>1]
print("exact_dup_paras", len(dups))
for n,p in sorted(dups, reverse=True)[:20]:
    print(n, p.replace("\n"," ")[:120])
