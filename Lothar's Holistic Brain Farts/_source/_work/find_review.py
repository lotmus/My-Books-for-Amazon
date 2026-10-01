import json, re
T = r"C:\Users\lomus\.cursor\projects\c-Users-lomus-OneDrive-My-Books-for-Amazon-Lothar-s-Holistic-Brain-Farts\agent-transcripts\907f6ad0-ffad-4b9d-b9c5-19c81ea63ad5\907f6ad0-ffad-4b9d-b9c5-19c81ea63ad5.jsonl"
lines = open(T, encoding='utf-8').read().splitlines()
for i, l in enumerate(lines, 1):
    if i < 130:
        continue
    try:
        o = json.loads(l)
    except Exception:
        continue
    if o.get('role') != 'assistant':
        continue
    texts = [c.get('text', '') for c in o['message']['content'] if c.get('type') == 'text']
    t = '\n'.join(texts)
    if 'monetiz' in t.lower() or 'glossary' in t.lower() and len(t) > 3000:
        print('=== line', i, len(t))
        print(t[:12000])
        break
