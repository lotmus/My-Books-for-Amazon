"""Add rubric pointers to notes/LOTHAR_RULES.md and CLAUDE.md in the working tree, and stage ONLY these two edits
(HEAD version + the pointer), so other sessions' uncommitted changes in those files are not swept into the commit."""
import subprocess, os, tempfile
ROOT = r'D:\My Books for Amazon'
def run(*a, **k): return subprocess.run(a, cwd=ROOT, capture_output=True, **k)
EDITS = [
    ('notes/LOTHAR_RULES.md',
     "- For science books the score areas are:",
     "- Rubric: `notes/SCIENCE_BOOK_RUBRIC.md` (ten criteria scored 1-4, 40-point scale, plus a weighted version) is available for every science or other nonfiction book. Apply it alongside the four-angle score, and record the result in the book's `SCORES.md` row or its notes.\n"),
    ('CLAUDE.md',
     "Also read `notes/ABOUT_THE_AUTHOR - canonical.md`,",
     None),
]
def insert_before(text, marker, line):
    i = text.index(marker); return text[:i] + line + text[i:]
for path, marker, line in EDITS:
    full = os.path.join(ROOT, path)
    cur = open(full, encoding='utf-8', newline='').read()
    head = run('git', 'show', 'HEAD:' + path).stdout.decode('utf-8')
    nl = '\r\n' if '\r\n' in cur else '\n'
    if path.startswith('notes/'):
        add = line.replace('\n', nl)
        if 'SCIENCE_BOOK_RUBRIC' not in cur: cur = insert_before(cur, marker, add)
        hnl = '\r\n' if '\r\n' in head else '\n'
        if 'SCIENCE_BOOK_RUBRIC' not in head: head = insert_before(head, marker, line.replace('\n', hnl))
    else:
        old = "and `SCORES.md`. Book-specific notes"
        new = "`SCORES.md`, and for science and other nonfiction books `notes/SCIENCE_BOOK_RUBRIC.md` (the scoring rubric). Book-specific notes"
        if 'SCIENCE_BOOK_RUBRIC' not in cur: cur = cur.replace(old, new)
        if 'SCIENCE_BOOK_RUBRIC' not in head: head = head.replace(old, new)
    open(full, 'w', encoding='utf-8', newline='').write(cur)
    with tempfile.NamedTemporaryFile('wb', delete=False) as t: t.write(head.encode('utf-8')); tn = t.name
    blob = run('git', 'hash-object', '-w', tn).stdout.decode().strip()
    r = run('git', 'update-index', '--cacheinfo', '100644,%s,%s' % (blob, path)); print(path, blob[:8], r.stderr.decode()[:100])
    os.unlink(tn)
r = run('git', 'add', 'notes/SCIENCE_BOOK_RUBRIC.md'); print(r.stderr.decode()[:100])
print(run('git', 'diff', '--cached', '--stat').stdout.decode())
