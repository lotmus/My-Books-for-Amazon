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
        if l=="" or l.startswith("#") or l.startswith("*Trial draft") or l.startswith("*Short draft") or l.startswith("*Expansion scene") or l.startswith("*Expanded draft") or l.startswith("*v2,") or l.startswith("*Revision 2 chapter") or l=="---":
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
BYLINE="Lothar J. Musiol writing as Frank N. Stone"
out.append("# Forbidden Offspring\n\n*A novel*\n\n"+BYLINE+"\n\n"
"Copyright © 2026 Lothar J. Musiol. All rights reserved. No part of this publication may be reproduced, distributed, or transmitted in any form or by any means, including photocopying, recording, or other electronic or mechanical methods, without the prior written permission of the author, except in the case of brief quotations embodied in critical reviews and certain other non-commercial uses permitted by copyright law.\n\n"
"This is a work of fiction. All people, clinics, universities, companies, parties and offices in the story are invented, and any resemblance to real ones is coincidence. The Appendix and the Notes and Further Reading refer to real science and real publications.\n")
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
    fullf=D+'expanded/ch%02d_full.md'%n
    text=body(open(fullf,encoding='utf-8').read()) if os.path.exists(fullf) else join(*fs)
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
PART2=["ch08.md","ch09.md","ch10.md","ch11.md","ch12.md","ch13.md","ch14.md","ch15.md","ch16.md","ch17a_foundation.md","ch17b_cabinet.md","ch17.md","ch19b_question_marks.md","ch18.md","ch22_draft.md","ch19.md","ch20.md"]
chap_words=[]
for k,fn in enumerate(PART2):
    n=8+k
    raw=open(D+'expanded/'+fn,encoding='utf-8').read()
    title=re.search(r"^## \d+[a-z]?\. (.+)$",raw,flags=re.M).group(1).strip()
    b=body(raw)
    chap_words.append((n,title,len(re.findall(r"\w+",b))))
    out.append(NL+"## "+str(n)+". "+title+NL+NL+b+NL)
out.append("\n---\n\n# Appendix: The Science Behind the Story\n\n"+body(rd("appendix_genetics_v2.md"))+"\n")
out.append("\n---\n\n# Notes and Further Reading\n\n"+body(rd("bibliography_v2.md"))+"\n")
# back matter: pen-name note + About the Author (Version B, American-English book) + Also by (canonical list)
ab=open("notes/ABOUT_THE_AUTHOR - canonical.md",encoding="utf-8").read()
vb=ab.split("## Version B",1)[1].split("Plain-text copies",1)[0].strip()
pen="Frank N. Stone is a pseudonym. It is also the name on the fertility doctor's paperwork in this book, a coincidence the author has chosen not to annotate, in keeping with the doctor's own methods."
out.append("\n---\n\n# About the Author\n\n"+pen+"\n\n"+vb+"\n")
al=open("notes/ALSO_BY - canonical list.md",encoding="utf-8").read()
al=al.split("## Also by Lothar J. Musiol",1)[1].split("## Also by Kevin",1)[0].strip()
al="\n".join(l for l in al.split("\n") if not l.startswith("- Forbidden Offspring"))  # leave out the book itself
out.append("\n---\n\n# Also by Lothar J. Musiol\n\n"+al+"\n")
txt="\n".join(out)
# reader copy: strip internal verification notes and the working status section
txt=re.sub(r"\s*\*\((?:Verify|Cite from)[^)]*\)\*","",txt)
txt=re.sub(r"\n\*\*Facts to re-check before publication:\*\*[^\n]*\n","\n",txt)
txt=re.sub(r"\n\*\(Ideas only; nothing is borrowed in text\.\)\*\n","\n",txt)
txt=re.sub(r"\n\* \* \*\n\n## Status\n.*\Z","\n",txt,flags=re.S)
open("Forbidden_Offspring/manuscript/Forbidden_Offspring_working_v1.md","w",encoding="utf-8").write(txt)
words=len(re.findall(r"\w+",txt))
print("words",words,"pages@300",round(words/300))
print(7,short[7][0],len(re.findall(r"\w+",short[7][1])))
for n,t,w in chap_words: print(n,t,w)
