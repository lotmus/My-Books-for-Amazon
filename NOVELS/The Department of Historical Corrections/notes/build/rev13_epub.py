import re,subprocess,sys,os,tempfile,shutil
MD,OUT,COVER,BACK=sys.argv[1:5]
base=os.path.dirname(os.path.abspath(MD))
t=open(MD,encoding='utf-8').read()
lines=t.split('\n')
assert lines[0].startswith('# ')
t='\n'.join(lines[1:]).lstrip('\n')
t=re.sub(r'^\* \* \*$',r'<p class="scene">\* \* \*</p>',t,flags=re.M)
t=re.sub(r'^\*(Figure [^\n]*)\*$',lambda m:'<p class="caption"><em>'+m.group(1)+'</em></p>',t,flags=re.M)
t=re.sub(r'\^\{([^}]*)\}',r'<sup>\1</sup>',t)
t=re.sub(r'_\{([^}]*)\}',r'<sub>\1</sub>',t)
front=('<div class="titlepage">\n\n<p class="subtitle"><em>A Novel</em></p>\n\n<p class="author"><strong>Lothar J. Musiol</strong></p>\n\n</div>\n\n'
 '<div class="copyright">\n\n<p>Copyright © 2026 Lothar J. Musiol. All rights reserved.</p>\n\n<p>This is a work of fiction. Historical settings are used imaginatively; the Department, its technology and its people are invented, and any resemblance to actual persons, living or dead, or to any department that has ever misplaced a country, is coincidental.</p>\n\n<p>No part of this book may be reproduced without written permission, except for brief quotations in reviews.</p>\n\n<p>First edition, 2026.</p>\n\n</div>\n\n')
alt='Back cover: the title, the tagline "Belgium has stopped existing. It is Monday.", a short blurb, three selling lines, a one-sentence author note and the Also-by series list.'
back='\n\n<div class="backcover">\n\n!['+alt+']('+BACK.replace('\\','/')+')\n\n</div>\n'
tmp=tempfile.mkdtemp()
src=os.path.join(tmp,'epub_src.md'); open(src,'w',encoding='utf-8').write(front+t+back)
css=os.path.join(tmp,'epub.css'); open(css,'w',encoding='utf-8').write('''
body{margin:0;padding:0;text-align:left;line-height:1.35}
p{margin:0 0 .7em 0;text-indent:0;text-align:left}
h1,h2,h3{text-align:center;color:#2A5CAA;font-weight:bold;page-break-after:avoid;margin-top:1.2em;margin-bottom:.8em}
h1{font-size:1.6em;page-break-before:auto}
h2{font-size:1.3em;page-break-before:always}
h3{font-size:1.1em;page-break-before:auto}
.scene{text-align:center;margin:1em 0}
.caption{text-align:center;font-size:.8em;margin:.2em 0 1em 0}
img{max-width:100%;height:auto}
.titlepage{text-align:center;margin-top:30%}
.booktitle{font-size:1.9em;font-weight:bold;color:#2A5CAA;text-align:center}
.subtitle{text-align:center;font-size:1.1em}
.author{text-align:center;margin-top:1.5em}
.copyright{page-break-before:always;font-size:.8em}
.backcover{page-break-before:always;text-align:center}
nav#toc ol{list-style:none;padding-left:0}
nav#toc a{text-decoration:none}
''')
meta=os.path.join(tmp,'meta.yaml'); open(meta,'w',encoding='utf-8').write('---\ntitle: "The Department of Historical Corrections"\nauthor: "Lothar J. Musiol"\nlang: en-GB\nrights: "Copyright 2026 Lothar J. Musiol"\n---\n')
cmd=['pandoc',src,'-f','markdown-implicit_figures-smart','-t','epub3','-o',OUT,'--metadata-file',meta,'--css',css,'--toc','--toc-depth=2','--split-level=2','--epub-cover-image',COVER,'--resource-path',base+os.pathsep+os.path.dirname(os.path.abspath(BACK)),'--epub-title-page=false','--standalone']
r=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8'); print(r.returncode,r.stderr[:1500])
print(os.path.getsize(OUT))
