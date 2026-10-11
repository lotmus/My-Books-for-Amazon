# -*- coding: utf-8 -*-
# Edit layer applied on top of the REV11 pool. Each op addresses a section by its original id (heading paragraph index in REV11).
# ('sub', sid, old, new)  replace substring in one paragraph (must occur exactly once)
# ('del', sid, startswith) delete paragraph(s) starting with text
# ('ins', sid, after_startswith, text)  insert paragraph after
# ('add', sid, text)  append paragraph
# ('set', sid, startswith, text)  replace whole paragraph
# ('retitle', sid, newtitle)
# ('front', key, startswith, newtext) / ('fsub', key, old, new): front-matter dict edits
OPS = []
import glob, importlib.util, os
for f in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ops', '*.py'))):
    spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    OPS.extend(m.OPS)

def apply(parts, front):
    log = []
    secs = {}
    for p in parts:
        for c in p['chapters']:
            if c['leadsec']: secs[c['leadsec']['id']] = c['leadsec']
            for s in c['secs']: secs[s['id']] = s
    # make paragraph lists mutable copies
    for s in secs.values(): s['paras'] = list(s['paras'])
    for op in OPS:
        k = op[0]
        if k == 'fset':
            front[op[1]]['paras'] = list(op[2]); continue
        if k == 'fadd':
            front[op[1]]['paras'].extend(op[2]) if isinstance(op[2], list) else front[op[1]]['paras'].append(op[2]); continue
        if k in ('fsub', 'front'):
            d = front[op[1]]
            lst = d['paras'] if 'paras' in d else None
            if k == 'fsub':
                hit = [i for i, t in enumerate(lst) if op[2] in t]
                if len(hit) != 1: log.append('FSUB FAIL %s %r (%d hits)' % (op[1], op[2][:50], len(hit))); continue
                lst[hit[0]] = lst[hit[0]].replace(op[2], op[3])
            else:
                hit = [i for i, t in enumerate(lst) if t.startswith(op[2])]
                if len(hit) != 1: log.append('FRONT FAIL %s %r (%d hits)' % (op[1], op[2][:50], len(hit))); continue
                lst[hit[0]] = op[3]
            continue
        if k == 'delsec':
            done = False
            for p in parts:
                for c in p['chapters']:
                    n = len(c['secs']); c['secs'] = [s for s in c['secs'] if s['id'] != op[1]]
                    if len(c['secs']) != n: done = True
            if not done: log.append('DELSEC FAIL %s' % (op[1],))
            continue
        if k == 'newsec':
            done = False
            for p in parts:
                for c in p['chapters']:
                    for ix, s in enumerate(c['secs']):
                        if s['id'] == op[1]:
                            ns = {'id': op[2], 'title': op[3], 'paras': list(op[4]), 'origin': 'new'}
                            c['secs'].insert(ix + 1, ns); secs[op[2]] = ns; done = True; break
                    if done: break
                if done: break
            if not done: log.append('NEWSEC FAIL after %s' % (op[1],))
            continue
        s = secs.get(op[1])
        if s is None: log.append('NO SECTION %s' % (op[1],)); continue
        if k == 'replace':
            s['paras'] = list(op[2]); 
            if len(op) > 3: s['title'] = op[3]
            continue
        ps = s['paras']
        if k == 'sub':
            hit = [i for i, t in enumerate(ps) if op[2] in t]
            if len(hit) != 1: log.append('SUB FAIL %s %r (%d hits)' % (op[1], op[2][:50], len(hit))); continue
            ps[hit[0]] = ps[hit[0]].replace(op[2], op[3])
        elif k == 'del':
            n = len(ps); ps[:] = [t for t in ps if not t.startswith(op[2])]
            if len(ps) == n: log.append('DEL FAIL %s %r' % (op[1], op[2][:50]))
        elif k == 'ins':
            hit = [i for i, t in enumerate(ps) if t.startswith(op[2])]
            if len(hit) != 1: log.append('INS FAIL %s %r (%d hits)' % (op[1], op[2][:50], len(hit))); continue
            ps.insert(hit[0] + 1, op[3])
        elif k == 'add':
            ps.append(op[2])
        elif k == 'set':
            hit = [i for i, t in enumerate(ps) if t.startswith(op[2])]
            if len(hit) != 1: log.append('SET FAIL %s %r (%d hits)' % (op[1], op[2][:50], len(hit))); continue
            ps[hit[0]] = op[3]
        elif k == 'retitle':
            s['title'] = op[2]
    return log
