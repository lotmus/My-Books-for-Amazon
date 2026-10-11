import zipfile, re, sys
z = zipfile.ZipFile(sys.argv[1])
x = z.read('word/document.xml').decode('utf-8')
anchors = re.findall(r'w:anchor="([^"]+)"', x)
names = re.findall(r'<w:bookmarkStart w:id="(\d+)" w:name="([^"]+)"', x)
ids = [i for i, _ in names]; nm = [n for _, n in names]
print('links', len(anchors), 'bookmarks', len(nm), 'unique ids', len(set(ids)) == len(ids), 'unique names', len(set(nm)) == len(nm))
print('dead links', [a for a in anchors if a not in nm])
