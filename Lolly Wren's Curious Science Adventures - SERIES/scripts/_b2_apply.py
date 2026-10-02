# -*- coding: utf-8 -*-
import re, shutil, zipfile
from pathlib import Path
import xml.etree.ElementTree as ET

root = Path(r"C:\Users\lomus\OneDrive\My Books for Amazon") / (
    "Lolly Wren" + chr(39) + "s Curious Science Adventures - SERIES"
)
book = root / "Book 2 - The Permitted Options"
src = book / "The_Permitted_Options_BOOK_2_DRAFT.docx"
bak = book / "The_Permitted_Options_BOOK_2_DRAFT.before-critical-review.docx"
if not bak.exists():
    shutil.copy2(src, bak)

xml = zipfile.ZipFile(src).read("word/document.xml").decode("utf-8")
bm0 = xml.count("<w:bookmarkStart")

def split_paras(doc):
    parts = []
    pos = 0
    token = re.compile(r"<w:p[ >]")
    while True:
        m = token.search(doc, pos)
        if not m:
            if doc[pos:]:
                parts.append(doc[pos:])
            break
        a = m.start()
        if a > pos:
            parts.append(doc[pos:a])
        b = doc.find("</w:p>", a)
        if b < 0:
            raise SystemExit("unclosed")
        b += 6
        parts.append(doc[a:b])
        pos = b
    return parts

def plain(p):
    return "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p))

def norm(s):
    return s.replace("\u2019", "'").replace("\u2018", "'")

def style_of(p):
    m = re.search(r'<w:pStyle w:val="([^"]+)"', p)
    return m.group(1) if m else ""

def replace_plain(p, old, new):
    if p.count(old) == 1:
        return p.replace(old, new, 1)
    pieces = []
    for m in re.finditer(r"(<w:t[^>]*>)([^<]*)(</w:t>)", p):
        pieces.append([m.start(), m.end(), m.group(1), m.group(2), m.group(3)])
    joined = "".join(x[3] for x in pieces)
    if joined.count(old) != 1:
        raise SystemExit("count %s" % old[:60])
    at = joined.find(old)
    end = at + len(old)
    cursor = 0
    first = True
    for x in pieces:
        t = x[3]
        lo, hi = cursor, cursor + len(t)
        cursor = hi
        if hi <= at or lo >= end:
            continue
        cut_lo = max(0, at - lo)
        cut_hi = min(len(t), end - lo)
        if first:
            x[3] = t[:cut_lo] + new + t[cut_hi:]
            first = False
        else:
            x[3] = t[:cut_lo] + t[cut_hi:]
    out = p
    for start, endpos, a, t, b in reversed(pieces):
        out = out[:start] + a + t + b + out[endpos:]
    return out

parts = split_paras(xml)

def iter_p():
    for i, p in enumerate(parts):
        if p.startswith("<w:p"):
            yield i

subs = [
    ("spent two chapters measuring", "spent the year measuring"),
    ("spent fifteen chapters asking", "spent the case asking"),
    ("for two chapters and filed", "in that mineshaft and filed"),
    ("G\u00f6del-sentence motion", "motion we had refused to call a theorem"),
    ("for a hundred and nine years, pending", "since 1916, pending"),
    ("We did not open it for 109 years.", "We did not open it."),
    ("had waited a hundred and nine years for someone", "had waited since 1916 for someone"),
    ("put the chapter in the file", "put the matter in the file"),
    ("write the chapter up as a chapter rather than a minute", "write the afternoon up as an argument rather than a minute"),
    ("most important twenty minutes in the chapter.", "most important twenty minutes of the afternoon."),
    ("Lolly laughed, for the first time since the Annex, out loud, in the office, which several people noted and none commented on.", "Lolly laughed."),
    ("She crossed the room. She put her forehead, briefly, against the shoulder that always met the racks first. He held the bag clear with the competence of long practice, and said, into her hair,",
     "She stayed on her side of the doorway. He held the bag clear, and said,"),
    ("He has never asked me to call either of those things by a larger name. I am going to, here, where only the notebook can be embarrassed. He is how I know a day is real.",
     "He has not asked me to call either of those things by a larger name."),
    ("who said almost nothing throughout and whom Lolly never saw again", "who had said almost nothing throughout"),
    ("Going deeper (skip freely)", "Going deeper"),
    ("holding a throat open behind Mr Eilstein for eleven thousand years", "holding a throat open in the geometry behind Mr Eilstein"),
    ("for the first time in eleven thousand years, a calibrated apparatus", "for the first time, a calibrated apparatus"),
    ("arXiv:1207.3123. arXiv:1207.3123", "arXiv:1207.3123"),
]
log = []
for old, new in subs:
    hits = []
    for i in iter_p():
        np = norm(plain(parts[i]))
        if norm(old) in np:
            hits.append(i)
    if not hits:
        log.append("MISS " + old[:70])
        continue
    for i in hits:
        np = norm(plain(parts[i]))
        at = np.find(norm(old))
        actual = plain(parts[i])[at:at + len(old)]
        parts[i] = replace_plain(parts[i], actual, new)
        log.append("OK " + old[:50])

# shorten Drill's morning if the long version is still there
for i in list(iter_p()):
    t = plain(parts[i])
    if t.startswith("It took the whole morning, and Lolly gave up"):
        if "bookmarkStart" in parts[i] or "hyperlink" in parts[i]:
            log.append("SKIP drill link")
            break
        short = ("It took the whole morning. He would reach the end of a proposition, say that it was too strong, and take a piece back. "
                 "By eleven Lolly had stopped trying to take him down verbatim.")
        parts[i] = replace_plain(parts[i], t, short)
        log.append("OK drill")
        break

drop_prefix = (
    "In one breath.",
    "Where the popular version goes wrong.",
    "What this chapter was actually showing you.",
    "Book Two opens on quantum tunnelling",
    "Why it is the right opening idea.",
    "Classically, a particle without enough energy to climb a barrier simply cannot cross it.",
    "Quantum mechanically the particle is a wave, and a wave",
    "If the barrier ends before the amplitude reaches zero",
    "That chance falls off exponentially with barrier width",
    "None of this needs to know why the barrier is there.",
)
for i in list(iter_p()):
    t = plain(parts[i])
    if any(t.startswith(p) for p in drop_prefix):
        if "bookmarkStart" in parts[i] or "hyperlink" in parts[i]:
            raise SystemExit("refuse delete " + t[:50])
        parts[i] = ""
        log.append("DEL " + t[:40])

def find_one(pred, label):
    hits = [i for i in iter_p() if pred(plain(parts[i]))]
    if len(hits) != 1:
        raise SystemExit("find %s %s" % (label, len(hits)))
    return hits[0]

def body_p(text):
    return ('<w:p><w:pPr><w:pStyle w:val="BodyText"/></w:pPr>'
            '<w:r><w:t xml:space="preserve">%s</w:t></w:r></w:p>' % text)

i = find_one(lambda t: t.startswith("Singularity Asset 4C."), "4c")
if 'w:anchor="ch00"' in parts[i]:
    parts[i] = parts[i].replace('w:anchor="ch00"', 'w:anchor="ch06"', 1)
    log.append("OK 4c link")
else:
    log.append("4c anchor left as is")

i = find_one(lambda t: t.startswith("The ninth of February arrived"), "feb")
ellen = [
    "On the Sunday before that Monday, Lolly rang the number on Ellen Prosper\u2019s card. The office in Peterhead said the vessel was at sea and the set was not answering. She rang the partner in Sligo at six. The woman said Ellen had not come off the boat since the case began, and had not taken the shop in Newcastle, and that if anyone was going to speak to her it would not be through a form.",
    "Lolly did not alter the trace. She wrote nothing on the cover that was not already there. Mrs Chain had asked for the page if the word came back. There was no page to send.",
]
parts[i:i+1] = [body_p(t) for t in ellen] + [parts[i]]
log.append("OK ellen")

i = find_one(lambda t: "God, no" in t, "god")
parts[i+1:i+1] = [body_p(
    "Okonkwo-Barrett wrote that answer in a book the size of a postcard and set the book on the schedule. She took her coat. She did not ask a second question."
)]

marks = (
    "The observatory liaison",
    "The letter had been in the department",
    "The letter came in on the general tray",
    "Jack Nashville came in",
    "Viktor Eugenius did not write",
    "Three items had been left",
    "The paper arrived from the Office",
    "Lolly told Miss Pike about Column B",
    "5 May 1906.",
    "The physics of the ledger",
    "The Concordance, and the way out",
    "The Fermi paper arrived",
    "The nine sent no letter this time",
    "The letter did not come from the nine",
    "On the Sunday before that Monday",
    "The ninth of February arrived",
)
mark = body_p("* * *")
for needle in marks:
    hits = [i for i in iter_p() if plain(parts[i]).startswith(needle)]
    if len(hits) != 1:
        log.append("MARK skip %s %s" % (needle[:30], len(hits)))
        continue
    i = hits[0]
    prev = ""
    j = i - 1
    while j >= 0:
        if parts[j].startswith("<w:p") and plain(parts[j]).strip():
            prev = style_of(parts[j])
            if plain(parts[j]).strip() == "* * *":
                prev = "HAVE"
            break
        j -= 1
    if prev.startswith("Heading") or prev == "HAVE":
        continue
    parts[i:i] = [mark]
    log.append("MARK " + needle[:30])

i = find_one(lambda t: t.startswith("Kruskal, M. D. (1960)."), "kruskal")
old_k = " Szekeres, G. (1960). On the singularities of a Riemannian manifold. Publicationes Mathematicae Debrecen 7, 285\u2013301."
if old_k not in plain(parts[i]):
    log.append("MISS szekeres split")
else:
    parts[i] = replace_plain(parts[i], old_k, "")
    parts[i+1:i+1] = [body_p(
        "Szekeres, G. (1960). On the singularities of a Riemannian manifold. Publicationes Mathematicae Debrecen 7, 285\u2013301."
    )]
    log.append("OK szekeres")

i = find_one(lambda t: t.startswith("Zurek, W. H."), "zurek")
extra = [
    "Coleman, S., and De Luccia, F. (1980). Gravitational effects on and of vacuum decay. Physical Review D 21, 3305\u20133315. doi:10.1103/PhysRevD.21.3305",
    "Esaki, L. (1958). New phenomenon in narrow germanium p-n junctions. Physical Review 109, 603\u2013604. doi:10.1103/PhysRev.109.603",
    "Nash, J. (1951). Non-cooperative games. Annals of Mathematics 54, 286\u2013295.",
]
parts[i+1:i+1] = [body_p(t) for t in extra]

doc = "".join(parts)
if doc.count("<w:bookmarkStart") != bm0:
    raise SystemExit("bookmarks %s %s" % (bm0, doc.count("<w:bookmarkStart")))
ET.fromstring(doc.encode("utf-8"))

check = split_paras(doc)
bad = []
seen_lectures = False
for p in check:
    if not p.startswith("<w:p"):
        continue
    t = plain(p)
    if t.strip() == "The Lectures":
        seen_lectures = True
    if seen_lectures or style_of(p).startswith("Heading"):
        continue
    if re.search(r"\bchapters\b", t, re.I) or re.search(r"Chapter\s+[A-Z0-9]", t):
        bad.append(t[:180])
plain_all = "\n".join(plain(p) for p in check if p.startswith("<w:p"))
need = ["not be through a form", "There was no page to send", "Coleman, S.", "Esaki, L.", "Nash, J.",
        "What the reader learns", "The Permitted Options ends here", "Q.E.D.", "The plates moved",
        "Okonkwo-Barrett wrote that answer"]
missing = [s for s in need if s not in plain_all]
(root / "_b2_apply_log.txt").write_text(
    "\n".join(log + ["BAD"] + bad + ["MISSING"] + missing), encoding="utf-8")
if bad or missing:
    raise SystemExit("refuse bad %s missing %s" % (len(bad), missing))
for s in ["In one breath.", "Where the popular version goes wrong.", "Going deeper (skip freely)",
          "for the first time since the Annex", "into her hair", "He is how I know a day is real",
          "G\u00f6del-sentence"]:
    if s in plain_all:
        raise SystemExit("remains " + s)

out = src.with_suffix(".tmp.docx")
zin = zipfile.ZipFile(src, "r")
with zipfile.ZipFile(out, "w") as zout:
    for item in zin.infolist():
        data = doc.encode("utf-8") if item.filename == "word/document.xml" else zin.read(item.filename)
        zout.writestr(item, data)
zin.close()
out.replace(src)
idx = []
n = 0
for p in check:
    if not p.startswith("<w:p"):
        continue
    if style_of(p) == "Heading2":
        idx.append("%d %s" % (n, plain(p).strip()[:70]))
    n += 1
(root / "_b2_apply_idx.txt").write_text("paras %d\n%s" % (n, "\n".join(idx)), encoding="utf-8")
print("saved", n)
