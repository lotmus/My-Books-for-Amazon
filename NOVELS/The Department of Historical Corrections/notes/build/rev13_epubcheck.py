import sys,zipfile,re
from xml.dom import minidom
z=zipfile.ZipFile(sys.argv[1]); print('testzip',z.testzip())
names=z.namelist(); print(len(names),[n for n in names if n.endswith(('.png','.jpg','.jpeg'))])
bad=0
for n in names:
    if n.endswith(('.xhtml','.xml','.opf','.ncx')):
        try: minidom.parseString(z.read(n))
        except Exception as e: bad+=1; print('XMLERR',n,e)
print('xml errors',bad)
nav=z.read('EPUB/nav.xhtml').decode('utf8'); items=re.findall(r'<a href="([^"]+)"[^>]*>(.*?)</a>',nav); print('nav items',len(items)); print(items[:3],items[-6:])
tx=''.join(z.read(n).decode('utf8') for n in names if n.startswith('EPUB/text/') and n.endswith('.xhtml'))
print('tables',tx.count('<table'),'h2',tx.count('<h2'),'h1',tx.count('<h1'),'scene',tx.count('class="scene"'),'imgs',tx.count('<img'))
print('missing alt',len(re.findall(r'<img(?![^>]*alt=)',tx)))
print('Bell' ,tx.count('Bell'))
print([n for n in names if n.startswith('EPUB/text/')][:5], len([n for n in names if n.startswith('EPUB/text/')]))
last=sorted(n for n in names if n.startswith('EPUB/text/') and n.endswith('.xhtml'))[-1]; print(last, z.read(last).decode('utf8')[-400:])
