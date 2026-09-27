# -*- coding: utf-8 -*-
from docx import Document
import re, json, os

path = r'D:\My Books for Amazon\Schrodingers_Paperwork\Schrodingers_Paperwork_BOOK_1.docx'
out_dir = r'D:\My Books for Amazon\Schrodingers_Paperwork\_tmp_audit_10'
os.makedirs(out_dir, exist_ok=True)

doc = Document(path)
paras = [(i, (p.style.name if p.style else ''), p.text or '') for i, p in enumerate(doc.paragraphs)]

h1 = [(i, t) for i, s, t in paras if s == 'Heading 1']
print('ALL H1:')
for i, t in h1:
    print(f'{i:4d} | {t}')

want = []
for i, t in h1:
    tl = t.lower()
    if t.strip().startswith('Physics'):
        continue
    if any(k in tl for k in ['how to read', 'prologue', 'chapter ', 'epilogue']):
        if 'appendix' in tl:
            continue
        want.append((i, t))

print('\nWANT:')
for i, t in want:
    print(f'{i:4d} | {t}')

narrative_end = len(paras)
for i, s, t in paras:
    if s == 'Heading 1' and (
        'Physics Prologue' in t or t == 'Cast of Characters' or t.startswith('Appendix')
    ):
        narrative_end = i
        break

sections = []
for idx, (start, title) in enumerate(want):
    end = want[idx + 1][0] if idx + 1 < len(want) else narrative_end
    # Clamp Epilogue etc. to narrative_end
    if end > narrative_end and start < narrative_end:
        end = narrative_end
    sections.append((start, end, title))

meta = []
for start, end, title in sections:
    body = []
    empty_runs = []
    empty_streak = 0
    for i in range(start, end):
        _, s, t = paras[i]
        body.append((i, s, t))
        if not t.strip():
            empty_streak += 1
        else:
            if empty_streak >= 2:
                empty_runs.append((i - empty_streak, empty_streak))
            empty_streak = 0
    words = sum(len(t.split()) for _, _, t in body)
    rules = []
    for i, s, t in body:
        ts = t.strip()
        if re.search(r'^Rules for\b', ts, re.I) or re.match(r'^Rules\b', ts):
            rules.append((i, ts[:120]))
        # also capture short rule-list intros
        if re.search(r'\bRules for [A-Za-z]', ts) and len(ts) < 80:
            if (i, ts[:120]) not in rules:
                rules.append((i, ts[:120]))
    phys = []
    for i, s, t in body:
        ts = t.strip()
        if re.search(r'Physics Notes|see.*Physics|Appendix.*Lecture|the Physics Notes', ts, re.I):
            phys.append((i, ts[:180]))
    opening = []
    for i, s, t in body:
        if i == start:
            continue
        if t.strip():
            opening.append((i, t.strip()))
            if len(opening) >= 4:
                break
    closing = []
    for i, s, t in reversed(body):
        if t.strip() and i != start:
            closing.append((i, t.strip()))
            if len(closing) >= 5:
                break
    closing = list(reversed(closing))

    safe = re.sub(r'[^\w\-]+', '_', title)[:90]
    with open(os.path.join(out_dir, f'{safe}.txt'), 'w', encoding='utf-8') as f:
        for i, s, t in body:
            f.write(f'{i}|{s}|{t}\n')

    meta.append({
        'title': title,
        'start': start,
        'end': end,
        'words': words,
        'rules': rules,
        'phys_ptrs': phys[:10],
        'opening': opening,
        'closing': closing,
        'empty_clusters': empty_runs,
        'para_count': end - start,
        'file': safe + '.txt',
    })

with open(os.path.join(out_dir, '_meta.json'), 'w', encoding='utf-8') as f:
    json.dump(meta, f, ensure_ascii=False, indent=2)

print('\nMETA:')
for m in meta:
    print(
        f"{m['words']:5d}w | rules={len(m['rules'])} | "
        f"empty={len(m['empty_clusters'])} | {m['start']}-{m['end']} | {m['title']}"
    )
