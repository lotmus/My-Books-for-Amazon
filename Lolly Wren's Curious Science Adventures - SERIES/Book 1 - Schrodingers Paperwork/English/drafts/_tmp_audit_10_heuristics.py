# -*- coding: utf-8 -*-
"""Per-chapter quality heuristics for editorial punch list."""
from docx import Document
import json, os, re
from collections import Counter

path = r'D:\My Books for Amazon\Schrodingers_Paperwork\Schrodingers_Paperwork_BOOK_1.docx'
out_dir = r'D:\My Books for Amazon\Schrodingers_Paperwork\_tmp_audit_10'
doc = Document(path)
paras = [(i, (p.style.name if p.style else ''), p.text or '') for i, p in enumerate(doc.paragraphs)]

with open(os.path.join(out_dir, '_meta.json'), encoding='utf-8') as f:
    meta = json.load(f)

# Find long dialogue stretches / long paragraphs / soft openers
out = []
for m in meta:
    start, end = m['start'], m['end']
    body = [(i, t.strip()) for i, _, t in paras[start:end] if t.strip() and i != start]
    # dialogue ratio
    dial = sum(1 for _, t in body if t.startswith('"') or t.startswith('“'))
    narr = len(body) - dial
    long_paras = [(i, len(t.split()), t[:160]) for i, t in body if len(t.split()) >= 90]
    # consecutive dialogue runs
    runs = []
    run_start = None
    run_len = 0
    for i, t in body:
        is_d = t.startswith('"') or t.startswith('“')
        if is_d:
            if run_start is None:
                run_start = i
                run_len = 1
            else:
                run_len += 1
        else:
            if run_len >= 8:
                runs.append((run_start, run_len))
            run_start = None
            run_len = 0
    if run_len >= 8:
        runs.append((run_start, run_len))

    # soft/hedge density
    hedges = 0
    hedge_words = re.compile(
        r'\b(rather|quite|somewhat|perhaps|almost|seemed|appeared|a little|sort of|kind of|in a way)\b',
        re.I,
    )
    for _, t in body:
        hedges += len(hedge_words.findall(t))

    # repeated sentence openers
    openers = Counter()
    for _, t in body:
        w = t.split()[:3]
        if w:
            openers[' '.join(w).lower()] += 1
    top_openers = [(o, c) for o, c in openers.most_common(8) if c >= 3]

    # em-dash density
    em = sum(t.count('—') + t.count('–') for _, t in body)

    # find "obviously/allegedly/apparently" stacking
    stack_words = []
    for i, t in body:
        hits = re.findall(r'\b(Obviously|Allegedly|Apparently|Probably)\b', t)
        if hits:
            stack_words.append((i, hits, t[:120]))

    out.append(f"\n### {m['title']} ({m['words']}w, {len(body)} paras)")
    out.append(f"  dialogue≈{dial} narr≈{narr} dial%={100*dial/max(1,len(body)):.0f}% hedges={hedges} emdashes={em}")
    out.append(f"  long_paras(>=90w)={len(long_paras)} dial_runs(>=8)={runs}")
    if top_openers:
        out.append(f"  repeated openers: {top_openers}")
    for i, wc, snip in long_paras[:5]:
        out.append(f"  LONG p{i} ({wc}w): {snip}")
    for i, hits, snip in stack_words[:6]:
        out.append(f"  STACK p{i} {hits}: {snip}")

# Search specific problem phrases user mentioned
problems = [
    r'eighth week',
    r'Tuesday afternoon',
    r'Tegn[eé]r',
    r'\bPeck\b',
    r'\bVoss\b',
    r'von Wittenberg',  # ok as character
    r'the the\b',
    r'\b(\w{4,})\s+\1\b',
    r'had been waiting',
    r'without turning',
    r'particular patience',
    r'expression of a woman',
    r'air of',
    r'in a professional sense',
    r'which only served',
    r'for the first time',
    r'not identical but',
    r'Once more than',
]
out.append('\n\n=== TARGETED PHRASE LOCS ===')
for rx in problems:
    cre = re.compile(rx, re.I)
    hits = []
    for i, s, t in paras:
        if i >= 2104:
            break
        if cre.search(t):
            hits.append((i, cre.search(t).group(0), t[:140]))
    out.append(f'\n{rx}: {len(hits)}')
    for i, g, snip in hits[:15]:
        out.append(f'  p{i}: {snip}')

# Check Ch15 for week references
out.append('\n\n=== WEEK / TIMELINE REFS Ch14-17 ===')
for i, s, t in paras:
    if 1797 <= i < 2026:
        if re.search(r'\b(week|Monday|Tuesday|Thursday|Sunday|eleven|seven|month)\b', t, re.I):
            if re.search(r'week|Monday|Tuesday|Sunday|Thursday|eleven week|seven week', t, re.I):
                out.append(f'p{i}: {t[:200]}')

path_out = os.path.join(out_dir, '_heuristics.txt')
with open(path_out, 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))
print('wrote', path_out)
