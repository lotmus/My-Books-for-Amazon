# -*- coding: utf-8 -*-
import json, importlib
from build_map import load_map, resolve
def build_model():
    pool = json.load(open('pool.json', encoding='utf-8'))
    parts = load_map(); problems, un = resolve(parts, pool)
    assert not problems, problems
    front = json.load(open('frontback.json', encoding='utf-8'))
    import edits; importlib.reload(edits)
    log = edits.apply(parts, front)
    return parts, front, log
def all_sections(parts):
    n = 0
    for pi, p in enumerate(parts):
        for c in p['chapters']:
            n += 1
            if c['leadsec']: yield n, c['title'], c['leadsec'], True
            for s in c['secs']: yield n, c['title'], s, False
