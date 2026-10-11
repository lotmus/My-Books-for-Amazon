import io,sys,re,collections,zipfile
from lxml import etree
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
z=zipfile.ZipFile('../The_Universe_Actually__REV11.docx')
root=etree.fromstring(z.read('word/document.xml'))
body=root.find(W+'body')
sig=collections.Counter(); ex={}
for k,p in enumerate(body):
    if p.tag!=W+'p': print('NONPARA',p.tag,k); continue
    ppr=p.find(W+'pPr'); pp=etree.tostring(ppr).decode() if ppr is not None else ''
    pp=re.sub(r' xmlns:\w+="[^"]+"','',pp)
    runs=p.findall('.//'+W+'r')
    rs=[]
    for r in runs:
        rpr=r.find(W+'rPr'); s=re.sub(r' xmlns:\w+="[^"]+"','',etree.tostring(rpr).decode()) if rpr is not None else ''
        rs.append(s)
    key=(pp,tuple(dict.fromkeys(rs)))
    sig[key]+=1; ex.setdefault(key,(k,''.join(t.text or '' for t in p.iter(W+'t'))[:60]))
for key,c in sig.most_common(40):
    print(c,ex[key]); print('  P:',key[0][:260]); 
    for r in key[1][:3]: print('  R:',r[:300])
