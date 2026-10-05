# -*- coding: utf-8 -*-
# generic: python apply_edits.py <docx> <edits_module> <list_name> <label> [--write]   (env EXPECT_SIZE / EXPECT_MTIME required)
import io, os, sys, shutil, time, zipfile, datetime, importlib
import xml.dom.minidom
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
LIVE, modname, listname, label = sys.argv[1:5]
WRITE = '--write' in sys.argv
E = getattr(importlib.import_module(modname), listname)
st = os.stat(LIVE)
mt = datetime.datetime.fromtimestamp(st.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
print('live size', st.st_size, 'mtime', mt)
if st.st_size != int(os.environ['EXPECT_SIZE']) or mt != os.environ['EXPECT_MTIME']:
    print('ABORT: file changed since read'); sys.exit(2)
zin = zipfile.ZipFile(LIVE)
xml = zin.read('word/document.xml').decode('utf-8'); orig = xml; bad = 0
for n, (old, new, occ) in enumerate(E, 1):
    cnt = xml.count(old)
    if occ is None:
        if cnt != 1:
            print('E%02d: expected 1 hit, got %d | %s' % (n, cnt, old[:100])); bad += 1; continue
        xml = xml.replace(old, new)
    else:
        if cnt <= max(occ):
            print('E%02d: too few hits %d | %s' % (n, cnt, old[:100])); bad += 1; continue
        pos = []; i = -1
        while True:
            i = xml.find(old, i + 1)
            if i < 0: break
            pos.append(i)
        for k in sorted(occ, reverse=True): xml = xml[:pos[k]] + new + xml[pos[k] + len(old):]
print('edits', len(E), 'problems', bad, 'xml delta', len(xml) - len(orig))
if bad: sys.exit(3)
xml.__class__
xml.dom if False else None
import xml.dom.minidom as md
md.parseString(xml.encode('utf-8')); print('well-formed OK')
if not WRITE: print('dry run only'); sys.exit(0)
root = os.path.dirname(LIVE); base = os.path.splitext(os.path.basename(LIVE))[0]
bak = os.path.join(root, 'bak', '%s.before-%s-%s.docx' % (base, label, time.strftime('%Y%m%d-%H%M%S')))
assert not os.path.exists(bak)
shutil.copy2(LIVE, bak); print('backup', bak, os.path.getsize(bak))
tmp = LIVE + '.tmp'
with zipfile.ZipFile(tmp, 'w') as zout:
    for info in zin.infolist():
        data = zin.read(info.filename)
        if info.filename == 'word/document.xml': data = xml.encode('utf-8')
        zi = zipfile.ZipInfo(info.filename, info.date_time); zi.compress_type = info.compress_type; zi.external_attr = info.external_attr
        zout.writestr(zi, data)
zin.close()
st2 = os.stat(LIVE)
assert st2.st_size == st.st_size and st2.st_mtime == st.st_mtime, 'live file changed during run'
os.replace(tmp, LIVE); print('WROTE', LIVE, os.path.getsize(LIVE))
