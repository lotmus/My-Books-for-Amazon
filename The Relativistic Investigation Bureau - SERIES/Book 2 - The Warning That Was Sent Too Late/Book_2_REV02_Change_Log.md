# Book Two REV02 change log (2026-10-09)

Base: `The_Warning_That_Was_Sent_Too_Late_BOOK_2_REV01.docx` (REV01 = the DRAFT master plus the REV01 fixes). DRAFT and REV01 are unchanged. Backup of the whole Book 2 folder before this pass: `D:\bak\2026-10-09 RIB2 integrate\` (19 files, SHA-256 verified).

`The_Warning_That_Was_Sent_Too_Late_BOOK_2_REV02.md` is a plain-text working copy of the docx. The docx is the master.

## Integrated from "In Love with Murder, Actually" material

- **Chapter 2, "A Clock Set Wrong".** Weinstein's night-train anecdote: the Sud Expresso between Hendaye and Lisbon, the summer he was twenty (1992), standing in the night at Vilar Formoso, where the Portuguese clocks said an hour less than the Spanish ones. That autumn Portugal joined Spain's time, in 1996 it went back, and the train and the sun noticed none of it. It makes Penny's "it's a label" concrete: a ministry can move every clock an hour with a signature, but it cannot make one tick slower. His existing line "A clock set wrong is not a clock running slow" is folded into the same speech. Source: the night train / Hendaye sleeper leftovers. Facts checked: the service stopped on 17 March 2020 and has not resumed, it crossed the border at Vilar Formoso, and mainland Portugal used Central European Time from 27 September 1992 to 1996 (Decree-Laws 124/92 and 17/96). It also pays off his Chapter 11 line about being "lied to by railways in four countries".
- **Chapter 20, "Acting Station Master".** Four lines adapted from the ILWM archive scene ("It exists in the book. This is different from not existing." / "That distinction has kept philosophers employed for centuries." / "And railway clerks."), given to Mr Pendleton about form PL/9: "It exists on the form... That is different from not existing." / "And Facilities."

## Continuity fixes

- **Chapter 1:** Sophie's clock was "in drawer three under a closed file" at 10:05, but the 1047 folder was still on the desk then. Now it is just "in drawer three".
- **Chapter 1:** REV01's added folder paragraph was out of place. It interrupted Trevor's text and "Nobody asked him to explain". It had Mrs Marsh carry the folder "downstairs to drawer three", but drawer three is in the outer room (Ch13, Ch21). It also said "The sheet stayed on Derek's desk", but the sheet was in his pocket. The beat now happens during Mrs Marsh's 10:05 visit. She passes the drawer key across the outer doorway without crossing it, which keeps the "she never came in" gag, Penny files the folder, and the sheet stays in Derek's pocket.
- **Chapter 13:** "a key Derek had not known she possessed" is now "the key she had kept since the morning", to match the Prologue and Chapter 1.
- **Coming Next:** this page quoted Derek as saying "Not yet", but that line was narration. It now refers to the file's own NO RING / LEFT BLANK entry. The status line names the Sunday slip.

## Back matter

- **Also by:** the Quanta, Actually entries are replaced with *Quantum, Actually, Volume 1: Questions and Answers from the Double Slit to the Superconducting Wire* and *Quantum, Actually, Volume 2: A QED Course*, matching the branch master.

## Checked

- 48 bookmarks and 33 internal links, all resolved. The book renders to 122 Letter pages in LibreOffice.
- No Trump references.
- The byline is unchanged: "Lothar J. Musiol writing as Spezala Genara Relavi (S.G.R.)".

---

# REV02 pass 2 (2026-10-09, Lothar's decisions)

REV02 is the master. Before this pass, the integration-pass REV02 docx was backed up to `D:\bak\2026-10-09 RIB2 integrate\REV02_before_pass2\`.

## Retired files

Moved, with SHA-256 checked, to `D:\bak\2026-10-09 RIB2 integrate\retired\`:

- `The_Warning_That_Was_Sent_Too_Late_BOOK_2_DRAFT.docx`
- `The_Warning_That_Was_Sent_Too_Late_BOOK_2_REV01.docx`
- `scripts/manuscript_text.txt`. This was an old export: compared with the docx, it holds nothing the docx lacks, only the earlier wording and one duplicated text message that the docx had already removed. Note that `scripts/build_book2_docx.py` reads this file, so that script is now obsolete. The docx is edited directly.

The move is recorded in git on `book-2-lectures-after-qed` (6dfcb48) and on `main` (8f186e3).

## Line edit (whole book, with chapters 5-12 first)

201 sentence-level edits, each replacing one exact phrase. There are no plot changes. Rates are per 10,000 words of story, before → after:

| Phrase | Before | After |
|---|---|---|
| "the way" | 72 (14.8) | 23 (4.7) |
| "which was" | 53 (10.9) | 22 (4.5) |
| "very" | 66 (13.5) | 23 (4.7) |
| "looked at" | 123 (25.2) | 71 (14.6) |
| "of a man who" | 19 | 5 |
| "the expression of" | 8 | 1 |

Kept on purpose:
- "nobody" (95). Most uses are the book's theme: the sender is nobody, and nobody boarded.
- The Ch2/Ch20 callback "at the speed of a man who has never once been sure he is in the right building".
- "Herbert did not look at it. He looked at the table." (Ch18).

Story words: 48,807 → 48,516.

## Front matter

- **How to Read This Book** (new, Heading 1, with a TOC link) goes before the Prologue, in the same pattern as Book 1. It includes the reading note that **Lesson 6 is the capstone**: Lessons 1-5 cover the Prologue and Chapters 1-9, and from Chapter 10 to the Epilogue every link points to Lesson 6 on purpose. Lesson 6 was not split.
- **Author's Note** (new, Heading 2, inside How to Read, as in Book 1). It sets out what is real and what is invented, and gives the Sud Expresso facts: it ran overnight from Hendaye/Irún across Spain to Lisbon, entered Portugal at Vilar Formoso, and was suspended on 17 March 2020. Portugal was on Spain's time from September 1992 to 1996.

## Checked

- 50 bookmarks and 52 internal links, all resolved, with no duplicate IDs.
- The book renders to 124 Letter pages.
- Total words: 52,935.
- The byline is unchanged. No Trump references.

## New notes

- `notes/Book 3 seeds.md`: the doors, the horn and the night-train stop, with their sources and the series rules each would have to obey.
- `KDP.md`: description, 7 keywords, categories and the fields still open.

---

# REV02 follow-ups (2026-10-09, 22:35 PT request)

- **Also by:** removed this book's own entry from its Also-by list. Book 1 is still listed.
- **Pace pass, chapters 5-11 (the Paddington stretch):** 21 cuts of repeated beats, with no plot, clue or scene removed. The stretch went from 12,322 to 12,030 words.
  - **Penny's argument:** her "if we strike her now, the fear wrote it" case appeared twice (Ch9 at the tea shelf and again on the chairs). It is now made once.
  - **Repeated habits:** Sophie's "too big to look at directly" habit was described twice (Ch8 and Ch9). It is kept once, in Ch9, from Derek's side.
  - **Pigeon jokes:** two of them are gone.
  - **Repeat descriptions:** Sherlock's mackerel accounting (already given a sentence earlier), the board's city list (it comes again later in the chapter), Tabitha's "where London is" (already said), the doubled school-phone logistics, and several padded clauses.
  - **Size:** the docx is now 52,629 words and 123 Letter pages. All 52 internal links resolve.
- **`SERIES_SEAM.md`** (series notes) now names REV02 as Book 2's master and records that DRAFT, REV01 and the old `manuscript_text.txt` export were retired. The worktree copy was identical to `origin/main`, so there were no uncommitted changes from another agent.

## 10 Oct 2026, strict rescore: 8.4 before the day's fixes, 8.7 after

Sampled reread (front matter, Prologue, Chapters 1 and 12, the course and back matter). Prose 8.8, plot 8.4, characters 8.8, humour 8.6, pacing 8.3, facts 9.2, formatting/KDP 9.0. Cover not scored: none yet, by decision.

- Typography: every straight quote is now curly (1,312 paragraphs, 2,856 double and 1,219 single marks), matching Book 1; three nested single quotes checked by eye. The "->" lesson arrows and " - " in the Contents stay, as in Book 1.
- Link rule: the seven Bibliography books and the three Further Reading books now carry their titles as keyword links to Open Library (each checked to resolve); the two papers already had DOI links. No visible URLs.
- The Also-by page already leaves this book out; KDP.md no longer says otherwise.
- `The_Warning_That_Was_Sent_Too_Late_BOOK_2_REV02.md` regenerated from the docx (`scripts/docx_to_md.py`); it had fallen behind by the lesson lines in the Contents and the review line. The docx stays the master.
- Script: `scripts/rescore_2026-10-10.py`. Old docx and md in `bak/2026-10-10 pre-rescore/`.

Still open: covers (none yet, by decision; Lothar decides), release date and price.


## 11 Oct 2026 (PT), full read-through: 38 fixes

The whole book was read: front matter, Prologue to Epilogue, Coming Next, the course and the back matter, and it was checked against Book 1 (`FINAL_REV11`), the series notes and the two passages taken from *In Love with Murder, Actually* (Weinstein's Sud Expresso anecdote in Ch2 and Pendleton's "It exists on the form" lines in Ch20, both consistent). The docx is edited in place by `scripts/readthrough_2026-10-11.py`; every edit replaces one exact phrase and has to match exactly once. The old docx and md are in `bak/2026-10-11 pre-readthrough/`. The lessons' exercises (Quick tests) are untouched.

Plot logic and clue fairness (the Ch22 solution has to match what the reader saw):
- **Ch22:** the printout's heading read STATUS OF CASE; the Prologue sheet reads CASE STATUS. Now identical.
- **Ch12:** the form's grey note read "THE PREVIOUS WARNING ARRIVED AFTER THE ACT", but Ch22 says the back of the sheet *is* that note, and the back reads "The previous warning was sent too late". The note now reads PLEASE NOTE. THE PREVIOUS WARNING WAS SENT TOO LATE.
- **Ch12:** Penny deletes a recipient line the reader had never been shown. The line (RECIPIENT: SOPHIE, typed by Trevor at lunch) is now on screen before she deletes it.
- **Ch22:** the carrier route said the sheet arrived "between 09:58:12 and the opening of the door"; 09:58:12 is the door photograph, not the sheet. Now: under the 1047 folder, before the door opened, time unknown.
- **Ch22:** on Monday Derek stood on the yellow line inside his own office; he never crossed the sill. The recap now says so, and the explanatory paragraph about paces and widths (it read like a note) is replaced by two sentences: from the slabs he can reach the first seat; reaching is not boarding.
- **Ch22:** Penny is four minutes out of the door, so she answers from a bus stop, not her kitchen; and the British Rail form is in the basement, so the call no longer has Derek reading it aloud.
- **Epilogue:** Sophie used the Bureau's private phrase "the nearest name", which she cannot know and which brushes against the promise not to tell her about the board. Replaced with "It's the true one." / "Mr Okafor says the true ones usually are."

Continuity:
- **Prologue:** "He lifted Penny's mug off it": the mug on the folder was Derek's. Now "the mug".
- **Ch1:** a kettle Penny boiled before ten "clicked off" at 10:22. It now ticks as it cools, and the poured mugs go cold.
- **Ch1:** Book 1 has device 3 revoked at SUN 01:33, the second one. Was "half past one".
- **Ch1:** Tabitha, a solicitor, is at home on a Monday: "where she had a brief to read and was not reading it".
- **Ch4:** "what Penny had taught him on the stairs at ten o'clock": the order was dictated onto Trevor's envelope at 10:22, in the office. "She's said she won't write it down": her text said she had not opened or fetched it. "Twice in a morning" at 13:15 is now "twice in one day".
- **Ch5:** the Sunday-morning photograph cannot have lived in Penny's bag "since the old Tuesday"; clause removed.
- **Ch6:** Herbert said Weinstein was staying "to be polite for a week", but he leaves on the Monday. Now "until Monday ... three days together".
- **Ch9:** Sophie put Julian's hangers "in the hall"; Tuppence and Ch14 have them in her room. Now "in my wardrobe".
- **Ch12:** Trevor "went to the kitchen" for the kettle that is in the office corner.
- **Ch13:** Mrs Marsh's kettle is in the lodge (Book 1), not "the kitchen downstairs".
- **Ch14:** Tuppence rings Derek on Tuesday evening (Epilogue), so "In the daytime" is gone from her plan.
- **Ch15:** Penny came in at seven and gets up at about ten: "nearly three hours", not two and a half.
- **Ch16:** Sherlock's "No." came at Paddington in the afternoon, not "at lunch".
- **Ch17:** Weinstein does the sum "in ink" after getting out his phone; now his pen.
- **Ch21:** Mrs Marsh says she locks drawer three at half past six but collects the paper at 18:35; now "a quarter to seven". Penny's guidebook appears for the first time and is now "her guidebook to Greece".
- **Epilogue:** Trevor had gone to move the Mini, so he drives home round the park rather than walking through it.

Facts (every figure in the story and course was recomputed or checked):
- **Ch1:** 17 minutes of light is 306 million km; added "That's past the far side of the Sun", which sets up Ch10's "the sum about the other side of the Sun".
- **Ch15:** Hafele and Keating published two short papers (Science 177, 166-170), not "two pages".
- **Lesson 5:** Hawking's chronology protection is a conjecture, so it "proposes", not "says", that physics forbids closed timelike curves.
- **Lessons 1, 2 and 4:** at the opening the sheet was in Derek's hand, not yet in his pocket.
- Checked and unchanged: 1/1200 rate limit (12,000 km/s by time dilation, 250 km/s by Doppler), the flight sums (4.3 ns/h gained at 11 km, 1.25 ns/h lost at 250 m/s, London 290 m/s and Athens 365 m/s of rotation, the x3), Hafele-Keating (-59 +/- 10 and +273 +/- 7 ns observed, -40 and +275 predicted), the laser's 6 ns for 896 mm, 41.2 m = 45 yd, 07:40 to 13:05 local = 3 h 25, the two one o'clocks on the night UK clocks go back, Munich one hour ahead, DCF77 at Mainflingen for the PTB, the caesium second (1967) and the ephemeris second (1956/1960), the Sud Expresso dates and Portugal's 1992-1996 clocks, PL/9's "fifty-two years" since 1974, thirty-two hours of ageing, and every Bibliography and Further Reading citation.

Also checked: British spelling throughout; no leftover notes or brackets except the cabinet label in About the Author; no Trump references; no Word tables; 54 bookmarks, 75 links, 0 dead anchors, 0 visible URLs; Also-by matches the canonical list in Book 1 and lists Book 1, not this book; the review line still sits before About the Author; byline "Lothar J. Musiol writing as Spezala Genara Relavi (S.G.R.)"; bio is the Colin Frissell / Gucci version.


## 11 Oct 2026 (PT), covers, KDP and strict rescore: 8.7 to 8.9

- **Covers:** `Kindle Front Cover.jpg` (1600 x 2560) and `Kindle Back Cover.jpg` (1600 x 2560), drawn by `scripts/make_covers.py` in Book 1's trade dress: night-blue sky with a dusk-orange horizon over generic London rooftops, the title in cream and gold Coustard Black, the gold Cinzel series line (RELATIVISTIC INVESTIGATION BUREAU / BOOK 2) with the RIB monogram, and the byline "Lothar J. Musiol / writing as Spezala Genara Relavi (S.G.R.)". The picture is the office door open onto the platform: the YESTERDAY board in amber dots, the lit train with its open door and first seat, the yellow line, the bench, the lamp and the station clock, Trevor's tape across the sill, and the warning (heading, instruction, NOT YET, tea ring with its bite) pinned beside the door. The back cover is one navy colour, text only: the hook, the blurb (as in KDP.md), the line about the physics, and a short Colin/Gucci bio line taken from About the Author. No photographs, no real people, no third-party art; fonts are Google Fonts (SIL Open Font License). No MediaSearcher or stock art was needed.
- **KDP.md:** the description was checked against the read-through and still holds. Keywords replaced (no category or title words, no "time travel", none copied from Book 1). Categories now match Book 1's revised set: Hard Science Fiction; Mystery > Private Investigators; Science Fiction > Humorous. Time Travel dropped: nobody travels in time and Derek does not board.
- **Checks on the master:** 0 Word tables, no visible URLs, 75 hyperlinks (linked Contents and course links), review line directly before About the Author, Also-by leaves this book out, 0.16 MB.
- **Strict rescore (whole book read):** prose 8.9, plot and clue fairness 8.9, characters 8.9, humour 8.7, pacing 8.4 (the Tuesday chapters still sag a little), facts 9.4, formatting/KDP 9.3, covers 8.8. Overall 8.9. Status ready.

