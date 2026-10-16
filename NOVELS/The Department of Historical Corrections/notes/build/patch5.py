b=open('rev13_epub.py',encoding='utf-8').read()
def rep(a,c):
    global b
    assert b.count(a)==1,a[:50]; b=b.replace(a,c)
rep("'<p class=\"scene\">* * *</p>'","r'<p class=\"scene\">\\* \\* \\*</p>'")
rep("<p class=\"booktitle\">The Department of Historical Corrections</p>\\n\\n","")
rep("h1{font-size:1.4em;page-break-before:always}","h1{font-size:1.6em;page-break-before:auto}")
open('rev13_epub.py','w',encoding='utf-8').write(b)
