# -*- coding: utf-8 -*-
"""Deep excerpt dump for editorial evaluation."""
from docx import Document
import json, os, re

path = r'D:\My Books for Amazon\Schrodingers_Paperwork\Schrodingers_Paperwork_BOOK_1.docx'
out_dir = r'D:\My Books for Amazon\Schrodingers_Paperwork\_tmp_audit_10'
doc = Document(path)
paras = [(i, (p.style.name if p.style else ''), p.text or '') for i, p in enumerate(doc.paragraphs)]

with open(os.path.join(out_dir, '_meta.json'), encoding='utf-8') as f:
    meta = json.load(f)

lines = []
for m in meta:
    start, end = m['start'], m['end']
    body = [(i, s, t) for i, s, t in paras[start:end]]
    nonempty = [(i, s, t) for i, s, t in body if t.strip()]
    lines.append('=' * 80)
    lines.append(f"{m['title']} | {m['words']} words | paras {start}-{end} | nonempty={len(nonempty)}")
    lines.append('=' * 80)
    # first 8 nonempty
    lines.append('--- OPENING (first 8 nonempty) ---')
    for i, s, t in nonempty[:8]:
        lines.append(f'p{i}: {t}')
    # middle sample: 3 paras around 40% and 70%
    if len(nonempty) > 20:
        for frac in (0.35, 0.55, 0.75):
            idx = int(len(nonempty) * frac)
            lines.append(f'--- MID @{frac:.0%} (3 paras) ---')
            for i, s, t in nonempty[idx:idx+3]:
                lines.append(f'p{i}: {t}')
    # last 10 nonempty
    lines.append('--- CLOSING (last 10 nonempty) ---')
    for i, s, t in nonempty[-10:]:
        lines.append(f'p{i}: {t}')
    lines.append('')

# limp-phrase / repetition candidates across narrative
limp_rx = [
    (r'\bit was (?:not|only|simply|merely) ', 'it was not/only/simply'),
    (r'\bin the particular (?:way|manner|patience|tone)', 'in the particular X'),
    (r'\bwith the (?:air|expression|patience|settled) of', 'with the X of'),
    (r'\bwhich was itself ', 'which was itself'),
    (r'\bfor the first time ', 'for the first time'),
    (r'\bshe said\b', 'she said'),
    (r'\bhe said\b', 'he said'),
    (r'\bLolly said\b', 'Lolly said'),
    (r'\bquite\b', 'quite'),
    (r'\brather\b', 'rather'),
    (r'\bof course\b', 'of course'),
    (r'\bin fact\b', 'in fact'),
    (r'\bas if\b', 'as if'),
    (r'\ba kind of\b', 'a kind of'),
    (r'\bsomething (?:like|of|in)\b', 'something like/of/in'),
    (r'\bthe Ministry\b', 'the Ministry'),
    (r'\bSimplification Initiative\b', 'Simplification Initiative'),
    (r'\bTuesday afternoon\b', 'Tuesday afternoon'),
    (r'\bordinary rules\b', 'ordinary rules'),
    (r'\bvery still\b', 'very still'),
    (r'\bhad gone very\b', 'had gone very'),
    (r'\bnot the same as\b', 'not the same as'),
    (r'\brecoverable\b', 'recoverable'),
    (r'\bunharmed\b', 'unharmed'),
]

counts = {label: [] for _, label in limp_rx}
for i, s, t in paras:
    if i >= 2104:
        break
    if not t.strip():
        continue
    for rx, label in limp_rx:
        n = len(re.findall(rx, t, re.I))
        if n:
            counts[label].append((i, n, t[:100]))

lines.append('\n' + '=' * 80)
lines.append('PHRASE FREQUENCY (narrative)')
lines.append('=' * 80)
for label, hits in sorted(counts.items(), key=lambda x: -sum(h[1] for h in x[1])):
    total = sum(h[1] for h in hits)
    lines.append(f'{total:4d}  {label}')

# Find near-duplicate sentences (normalized)
norm_map = {}
dups = []
for i, s, t in paras:
    if i >= 2104:
        break
    ts = t.strip()
    if len(ts) < 60:
        continue
    key = re.sub(r'\s+', ' ', ts.lower())
    key = re.sub(r'[^a-z0-9 ]', '', key)[:160]
    if key in norm_map:
        dups.append((norm_map[key], i, ts[:160]))
    else:
        norm_map[key] = i

lines.append('\nNEAR-EXACT DUP PARAS:')
for a, b, snip in dups[:50]:
    lines.append(f'  p{a} ~ p{b}: {snip}')

# Check for empty paragraph clusters (including single empties between shorts)
empty_clusters = []
streak = 0
streak_start = 0
for i, s, t in paras:
    if i >= 2104:
        break
    if not t.strip():
        if streak == 0:
            streak_start = i
        streak += 1
    else:
        if streak >= 2:
            empty_clusters.append((streak_start, streak))
        streak = 0
lines.append(f'\nEMPTY CLUSTERS (>=2): {len(empty_clusters)}')
for st, n in empty_clusters[:30]:
    lines.append(f'  p{st} x{n}')

out = os.path.join(out_dir, '_excerpts.txt')
with open(out, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print('wrote', out, 'chars', sum(len(x) for x in lines))
print('dups', len(dups), 'empty clusters', len(empty_clusters))
