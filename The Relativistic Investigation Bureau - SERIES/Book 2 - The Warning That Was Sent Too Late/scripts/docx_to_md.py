"""Regenerate the plain-text working copy (.md) from the docx master. The docx is the master."""
import docx, sys
d = docx.Document(sys.argv[1]); out = []
for p in d.paragraphs:
    t = p.text.strip()
    if not t: continue
    s = p.style.name
    out.append(('# ' if s == 'Heading 1' else '## ' if s == 'Heading 2' else '') + t)
open(sys.argv[2], 'w', encoding='utf-8', newline='\n').write('\n\n'.join(out) + '\n')
