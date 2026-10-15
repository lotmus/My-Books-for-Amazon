import os,zipfile,re
from lxml import etree
src=os.path.join(r'D:\My Books for Amazon','HOW TO  Series','How to Publish Your First Kindle Book','bak','Your First Book That Sells_REV04_2026-10-05.docx')
out=os.path.join(r'C:\Users\lomus\.codex\worktrees\kindle-rev04-kdp-format\My Books for Amazon','How to Publish Your First Kindle Book','How to Publish Your First Kindle Book_REV44_2026-10-15.docx')
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}; W='{%s}'%ns['w']; BLUE='0070C0'
with zipfile.ZipFile(src) as z: infos=z.infolist(); data={i.filename:z.read(i.filename) for i in infos}
parser=etree.XMLParser(remove_blank_text=False,resolve_entities=False); root=etree.fromstring(data['word/document.xml'],parser)
paras=root.xpath('.//w:body//w:p',namespaces=ns); centered=0; blue=0; pagebreaks=0; chapters=[]
chapter_re=re.compile(r'^Chapter\s+\d+\s*:')
def txt(p): return ''.join(p.xpath('.//w:t/text()',namespaces=ns))
def style(p):
 x=p.find('w:pPr/w:pStyle',namespaces=ns); return x.get(W+'val','') if x is not None else ''
for p in paras:
 sid=style(p)
 if sid in ('Title','Subtitle','Heading1','Heading2','Heading3'):
  ppr=p.find('w:pPr',namespaces=ns)
  if ppr is None: ppr=etree.Element(W+'pPr'); p.insert(0,ppr)
  jc=ppr.find('w:jc',namespaces=ns)
  if jc is None: jc=etree.SubElement(ppr,W+'jc')
  jc.set(W+'val','center'); centered+=1
 if sid in ('Heading1','Heading2'):
  for r in p.xpath('.//w:r',namespaces=ns):
   rpr=r.find('w:rPr',namespaces=ns)
   if rpr is None: rpr=etree.Element(W+'rPr'); r.insert(0,rpr)
   c=rpr.find('w:color',namespaces=ns)
   if c is None: c=etree.SubElement(rpr,W+'color')
   c.set(W+'val',BLUE)
   for key in ('themeColor','themeTint','themeShade'): c.attrib.pop(W+key,None)
  blue+=1
 if sid in ('Heading1','Heading2') and chapter_re.match(txt(p).strip()):
  ppr=p.find('w:pPr',namespaces=ns)
  if ppr is None: ppr=etree.Element(W+'pPr'); p.insert(0,ppr)
  pb=ppr.find('w:pageBreakBefore',namespaces=ns)
  if pb is None: pb=etree.SubElement(ppr,W+'pageBreakBefore')
  chapters.append(txt(p).strip()); pagebreaks+=1
data['word/document.xml']=etree.tostring(root,xml_declaration=True,encoding='UTF-8',standalone=True)
os.makedirs(os.path.dirname(out),exist_ok=True)
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
 for i in infos: z.writestr(i,data[i.filename])
with zipfile.ZipFile(out) as z:
 assert z.testzip() is None
 assert z.namelist()==[i.filename for i in infos]
 assert z.read('word/_rels/document.xml.rels')==data['word/_rels/document.xml.rels']
 etree.fromstring(z.read('word/document.xml'),parser)
# Exact manuscript text unchanged from input
with zipfile.ZipFile(src) as z: old=etree.fromstring(z.read('word/document.xml'))
oldtxt=[''.join(p.xpath('.//w:t/text()',namespaces=ns)) for p in old.xpath('.//w:body//w:p',namespaces=ns)]
newtxt=[''.join(p.xpath('.//w:t/text()',namespaces=ns)) for p in root.xpath('.//w:body//w:p',namespaces=ns)]
assert oldtxt==newtxt
assert len(chapters)==33,(len(chapters),chapters)
print('created',out,os.path.getsize(out),'bytes')
print('centered',centered,'Heading1/2 colored',blue,'chapter page-breaks',pagebreaks)
print('text identical; ZIP clean; members and relationships preserved.')
