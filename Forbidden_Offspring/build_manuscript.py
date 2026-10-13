"""Rebuild manuscript/Forbidden_Offspring_working_v1.md from drafts/. Run from the repo root: python3 Forbidden_Offspring/build_manuscript.py
Chapters 7-20 use drafts/expanded/chNN.md when present, else the short draft."""
import re,io
D="Forbidden_Offspring/drafts/"
def rd(f): return open(D+f,encoding="utf-8").read()
def body(text):
    lines=text.split("\n")
    i=0
    while i<len(lines):
        l=lines[i].strip()
        if l=="" or l.startswith("#") or l.startswith("*Trial draft") or l.startswith("*Short draft") or l=="---":
            i+=1; continue
        break
    out=[]
    for l in lines[i:]:
        out.append("* * *" if l.strip()=="---" else l)
    return "\n".join(out).strip()
p=D+'ch07_to_20_short_v1.md'
s=open(p,encoding='utf-8').read()
parts=re.split(r"\n(?=## \d+\. )",s)
short={}
for part in parts:
    m=re.match(r"## (\d+)\. (.+)",part)
    if m: short[int(m.group(1))]=(m.group(2).strip(),body(part))
import os
for n in list(short):
    f=D+'expanded/ch%02d.md'%n
    if os.path.exists(f): short[n]=(short[n][0],body(open(f,encoding='utf-8').read()))
def join(*fs): return "\n\n* * *\n\n".join(body(rd(f)) for f in fs)
out=[]
out.append("# Forbidden Offspring\n\n*A novel*\n")
out.append("---\n\n# Consent\n\n"+body(rd("prologue_consent_v1.md")).replace("* * *","---")+"\n")
out.append("\n# PART ONE: STONE\n")
P1=[(1,"Four Minutes",["ch01_four_minutes_Stone_v1.md","ch02_the_transfer_Stone_v1.md"]),
(2,"Test Time",["ch03_test_time_Stone_v1.md"]),
(3,"The Ledger",["ch06_the_ledger_Stone_v1.md","ch07_the_cohort_Stone_v1.md"]),
(4,"The Second Listener",["ch04_the_second_listener_Stone_v1.md","ch05_the_singapore_paper_Stone_v2.md"]),
(5,"The Apartment",["ch05_the_apartment_Stone_v1.md"]),
(6,"The Bargain",["ch06_the_bargain_Stone_v1.md"])]
def extra(n,kind):
    f=D+'expanded/ch%02d_%s.md'%(n,kind)
    return body(open(f,encoding='utf-8').read()) if os.path.exists(f) else ''
NL=chr(10)
SEP=NL+NL+"* * *"+NL+NL
for n,t,fs in P1:
    text=join(*fs)
    bef=extra(n,'before')
    if bef:
        k=text.rfind(SEP)
        text=text[:k]+SEP+bef+text[k:]
    mid=extra(n,'mid')
    if mid:
        k=text.find(SEP)
        text=text[:k]+SEP+mid+text[k:]
    pre=extra(n,'pre'); post=extra(n,'post')
    if pre: text=pre+SEP+text
    if post: text=text+SEP+post
    out.append(NL+"## "+str(n)+". "+t+NL+NL+text+NL)
out.append(f"\n## 7. {short[7][0]}\n\n"+short[7][1]+"\n")
out.append("\n# PART TWO: THE OFFSPRING\n")
for n in range(8,21):
    out.append(f"\n## {n}. {short[n][0]}\n\n"+short[n][1]+"\n")
out.append("\n---\n\n# Appendix: The Science Behind the Story\n\n"+body(rd("appendix_genetics_v1.md"))+"\n")
out.append("\n---\n\n# Notes and Further Reading\n\n"+body(rd("bibliography_v1.md"))+"\n")
txt="\n".join(out)
open("Forbidden_Offspring/manuscript/Forbidden_Offspring_working_v1.md","w",encoding="utf-8").write(txt)
words=len(re.findall(r"\w+",txt))
print("words",words,"pages@300",round(words/300))
for n in range(7,21): print(n,short[n][0],len(re.findall(r"\w+",short[n][1])))
