import io,sys,json
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
kept=json.load(open('pool.json',encoding='utf-8'))
for s in kept:
    for t in s['paras']:
        if 'Topics in this chapter' in t: print(s['id'],s['title'],'|',t[:200]); break
print()
import re
n=0
for s in kept:
    for t in s['paras']:
        if re.fullmatch(r'\*\*[^*]+\*\*',t.strip()): n+=1; print(s['id'],s['title'],'|',t[:80])
