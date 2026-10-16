import io, re
B = r"C:\Users\lomus\wt-dt4\NOVELS\The Digital  Twin"
R = r"C:\Users\lomus\wt-dt4"
def rd(p): return io.open(p, encoding="utf-8", newline="").read()
def wr(p, t): io.open(p, "w", encoding="utf-8", newline="").write(t)
def nl(t): return "\r\n" if "\r\n" in t else "\n"

# ---------- REVIEW ----------
review = """# The Digital Twin: REVIEW REV4 (15 Oct 2026)

Scope: REV3 (109,469 words) to REV4 (113,073 words, 35 chapters). Brief: pacing, comic types, officials' registers, narrator tics; a humour pass; twists with plants and payoffs. Scored from four angles (reader, critic, genre expert, market). Strict; no area is a 10, and the reasons are stated.

## Scores

| Area | REV3 | REV4 | What stops a 10 |
|---|---:|---:|---|
| Plot / structure | 9.0 | 9.2 | The twists now turn the courtroom (zero is a person, Pettifer's double game). The climax is still decided by a document in a hall, which is tidy by genre convention. |
| Characters | 9.0 | 9.2 | Pettifer now has a secret and a peppermint, Pym a safety-card register, Lessing the passive voice, Gareth a conscience, Kevin a confession. They are still comic types first; none changes as much as Daniel or Sophie. |
| Prose / voice | 8.7 | 8.8 | "a man who" 47 and "a woman who" 25 (REV3 about 70), "like a" 149 (155), "as though" 23. The cadence is still recognisably one narrator. Needs a human line editor. |
| Pacing | 8.8 | 9.0 | Ch 22 now has a clock and an interruption (Securishred), Ch 30 a clearance deadline, Ch 31 a reveal. Ch 31 is still the quietest of the late chapters by design. |
| Continuity | 9.1 | 9.1 | Scripted scans clean and one real clash caught and fixed (the blank date field in Ch 4 against the photographed register line in Ch 32). No fresh human front-to-back read of 113k words, which caps this. |
| Dialogue | 9.0 | 9.2 | Officials now sound different from each other. Some dry one-liners still land with the same rhythm (statement, pause, understatement). |
| Humour | n/a | 9.0 | Running jokes with payoffs (peppermint, interested-parties list, Hydrate responsibly, oven door, PENDING, nulls, Argument Pack, "He's allowed"). Reader-tested only by me. |
| Kindle formatting | 8.9 | 8.9 | To spec by script and in file checks (3.6 x 4.8 in, 0.3 in margins, 39 Heading 1 on new pages, 41 internal links, no tables, one inline image). Not opened in Kindle Previewer or on a device. |
| Front / back matter | 9.0 | 9.0 | Unchanged. Generic review line, no outside blurbs. |
| Cover / KDP listing | 8.4 | 8.4 | Unchanged; script-drawn cover, not approved by Lothar. KDP_Description not touched. |
| **Overall (manuscript)** | 8.9 | **9.1** | No outside reader, no line editor, no Previewer. |
| **Sellability** | 8.4 | **8.6** | Stronger middle and ending hook for reviews; still no reviews, generic cover versus genre leaders. |

## Twists
Used (3 big, plus smaller):
1. BIG. DP-0000000 is a person: Daniel-A's "legacy" ancestor record, DP-0000000/A, registered 2 March 1999 (Ch 32). Plants: Ch 4 (the zero line deleted as a fault), Ch 18 (Gareth photographs everything), Ch 23 (luggage label "REG. NO. 0 (LEGACY)"), Ch 28/29 hints. Reveal changes what Daniel-A wants (he is "a suffix", wants Ned's consent) and what Ned wants ("Can I keep you?", then "He's allowed").
2. BIG. Pettifer and Calder are Imogen and Marguerite; he has corresponded with her since winter 2019 on a standing instruction and was never on a side (Ch 31). Plants: Ch 4 (instructed in advance, peppermint), Ch 15 (peppermint tin), Ch 16/22/24 (hen, lanyard), Ch 27. Changes what Pettifer wants (to bill for it) and what Daniel wants (to keep Pettifer).
3. BIG. Kevin's minutes are the cause of the canteen attendance and the Settled/Unsettled fiasco (Ch 8 plant, Ch 16 plant, Ch 27 reveal: "nine people and a dentist in Walsall").
Smaller: the decoy box and the true certificate (Ch 22); Barry's eleven fifty-one (Ch 30); Dorothy disagrees with the winning argument (Ch 35); PENDING becomes ADOPTED (Ch 35); Pettifer refunds the retainer (Ch 35).
Dropped: (a) Lessing as Marguerite's old friend (too many reveals for one chapter); (b) Giles as the registrant of record (would undo Ch 24); (c) Sophie as a Mercier relative (belongs to Book 2).

## Before / after sample
Before (Ch 24, REV3): Lessing announced the seizure in the same brisk, slightly aggrieved register as every other official.
After (REV4): "It has been noted," said Mr Lessing, "that a file has been noted." The passive is his whole personality; nobody in the book, including Pym, speaks that way.

## What is not done
No cold read by a person; no Kindle Previewer; Lothar has not read REV4 or approved the cover; the new scenes (Ch 22 Securishred, Ch 31 reveal, Ch 32 DP-0000000/A) are the first thing a human should check for tone.
"""
wr(B + r"\notes\REVIEW_REV4_2026-10-15.md", review)

# ---------- STATUS ----------
p = B + r"\notes\_STATUS.md"; t = rd(p); n = nl(t)
head = """# The Digital Twin: status (15 Oct 2026, REV4)

**Master:** `The Digital Twin - REV4.docx` (Kindle page 3.6 x 4.8 in, 0.3 in margins, Heading 1 per chapter on a new page, linked contents, no tables, cover on page 1; about 113,100 words in the 35 chapters). REV3 is in `bak\\2026-10-15 REV3\\`, REV2 and REV1 in their own bak folders. Full four-angle scores and the twist log: `notes/REVIEW_REV4_2026-10-15.md`.

Scores (REV4, strict, no 10s): plot 9.2, characters 9.2, prose 8.8, pacing 9.0, continuity 9.1, dialogue 9.2, humour 9.0, Kindle formatting 8.9, front/back matter 9.0, cover/KDP 8.4. Overall 9.1, sellability 8.6.
Open items: Lothar read-through; outside readers; Kindle Previewer; cover approval.

(REV3 status follows for reference.)

""".replace("\n", n)
wr(p, head + t.split(n, 1)[1])

# ---------- HANDOVER ----------
p = B + r"\notes\HANDOVER.md"; t = rd(p); n = nl(t)
add = """

## REV4 (15 Oct 2026)
- Master is now `The Digital Twin - REV4.docx`; REV3 moved to `bak\\2026-10-15 REV3\\` (on the D: copy). Branch `dt-rev4-20261015`.
- Edits are scripted in `notes/build/rev4_a.py` to `rev4_e.py` (helper `rev4_part1.py`), run on the REV3 chapters. Rebuild with `notes/build/build_docx.py` (needs the two canonical files copied next to the chapters).
- New scenes: Ch 22 Securishred (decoy box, hen against policy, true certificate); Ch 31 Pettifer/Calder reveal; Ch 32 DP-0000000/A reveal; Ch 27 Kevin's confession; Ch 35 Argument Pack disagreement, PENDING to ADOPTED, retainer refund.
- Running gags to keep consistent in Book 2: Pettifer's peppermints, the interested-parties list, "Hydrate responsibly", the oven door, nulls end up on the news, "He's allowed".
- Twists used: DP-0000000/A; Pettifer and Calder (Imogen/Marguerite); Kevin's minutes. Dropped: Lessing as Marguerite's friend; Giles as registrant; Sophie as a Mercier relative (Book 2).
- Known fact: the Ch 4 register date field is blank; the date 2 March 1999 comes from page one of the Register (Ch 32).
- Book 2 hook unchanged: Ch 35 S2 MERCIER and Sophie's phone dark on the cloth.
- Banned-name rule: manuscript, notes and docx grepped clean. Do not touch the Historical Corrections folder.
""".replace("\n", n)
wr(p, t.rstrip() + n + add)

# ---------- CONTINUITY ----------
p = B + r"\notes\book1_continuity.md"; t = rd(p); n = nl(t)
add = """

## REV4 changes
- DP-0000000 (Ch 4) is a legacy record, DP-0000000/A is Daniel-A's linked record, date field blank, registered 2 March 1999 per page one of the Register; Schedule Four para 9 consent of the antecedent registrant (Edmund Calder, "Ned").
- Pettifer = Imogen; Calder = Marguerite; correspondence since winter 2019; standing instruction GBP 40 a month, file marked "Hypothetical". Lanyard borrowed from Gareth; no friend in Records.
- Securishred (Ch 22): technician Gavin, arrives 8:22, gone before half past eight; decoy box; certificate.
- Kevin: attended the canteen via the phone; list of nine people and a dentist in Walsall.
- Barry: unit 114 cleared at noon (Ch 30), eleven fifty-one.
""".replace("\n", n)
wr(p, t.rstrip() + n + add)

# ---------- SCORES.md ----------
p = R + r"\SCORES.md"; t = rd(p)
old = "| REV1 docx + cover + KDP description; REV2 line edit, Act III loss, Sophie beats, countdown; REV3 set pieces, endings, tic and simile cuts, KDP refresh, Also-by and Identity |"
assert t.count("REV3 set pieces, endings, tic and simile cuts, KDP refresh, Also-by and Identity |") == 1
t = t.replace("REV3 set pieces, endings, tic and simile cuts, KDP refresh, Also-by and Identity |", "REV3 set pieces, endings, tic and simile cuts, KDP refresh, Also-by and Identity; REV4 humour pass, three twists with plants, pacing scenes (Ch 22, 30, 31), officials' registers |")
o2 = "8.9 manuscript, sellability 8.4 (15 Oct 2026, REV3; strict, no 10s, see notes/_STATUS.md for what blocks each; plot 9.0, characters 9.0, prose 8.7, pacing 8.8, continuity 9.1, dialogue 9.0, Kindle formatting 8.9, front/back matter 9.0, cover/KDP 8.4)"
assert t.count(o2) == 1
t = t.replace(o2, "9.1 manuscript, sellability 8.6 (15 Oct 2026, REV4; strict, no 10s, see notes/REVIEW_REV4_2026-10-15.md; plot 9.2, characters 9.2, prose 8.8, pacing 9.0, continuity 9.1, dialogue 9.2, humour 9.0, Kindle formatting 8.9, front/back matter 9.0, cover/KDP 8.4)")
wr(p, t)
print("done")