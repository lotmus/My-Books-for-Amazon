# STATUS — Protocol Flamingo

Last updated: 2026-10-01. The live book is the expanded manuscript, not the generator.

## Live file

`Protocol_Flamingo_Rev2.docx` is the book. 26,647 words of body text (counted 1 Oct 2026; the earlier "about 28,700" was stale). Pen name on the title page and in the file properties: George Herbert Fontaine. Story year is “this year” (2026). Series line on the title page: The Invasion Storybooks.

The paperback trim in the file is 5.5 by 8.5 inches, with a half-inch gutter and mirrored margins. Front matter is numbered in roman numerals. Page 1 is the start of the story. `KDP_LISTING.md` holds the description, keywords, categories, and price. `Protocol_Flamingo_cover_front.jpg` is a front cover at that trim, not a full paperback wrap.

`build_docx.js` builds the earlier, shorter draft and writes `Protocol_Flamingo_script_draft.docx`. Running it must not replace Rev2.

`Protocol_Flamingo_Rev1.docx` (older) now sits in `bak/superseded/`. `bak/` holds snapshots and scratch scripts; none of it is the live book. `bak/` is gitignored.

## Session of 1 Oct 2026 (owner: the single session that also has RIB Book 1 and the Tower)

That session does no git; Lothar syncs separately. The pre-edit file is backed up at `C:\Users\lomus\OneDrive\My Books for Amazon - session backups\2026-10-01 RIB-Flamingo-Tower\Protocol Flamingo\`. 26,460 → 26,647 words. What changed:

- Chapter IV is now in story order. Cobb is introduced once, in the lot, with her file briefing. Then Huff in the lot, one arrival at the Reyes house (there were two), the alpaca and Steve loaded, the pickup chase, Huff's bunker, the Dipstick. "Warren had talked once in the first hour."
- Chapter V diner: the setting comes first. It is the time pencilled on the flyer (an old line said Nora picked it, which broke canon). The sign "UN T" has one dead letter. Order: Jesse arrives, banter, they stand to leave, then the man in the lot.
- Brussels: one line names the services (Duval, French; Berthold, German; Whitcombe, British; Cole, American). The dangling "before Duval got that far" is gone.
- Chapter VII: Kade is introduced before "did not give tours".
- Aboard: the doubled PA line is cut. The three crewmen (oldest, heavyset, youngest) are introduced before the lunge, which now names them.
- Place slips: "a diner in Nevada" became the break room under the dead mall. The motel "outside Reno" became "outside Tonopah".
- Starfall is a daytime total solar eclipse throughout (afternoon heat, game day, "cleaner than the day"; the glossary agrees). The sails fly outside the Moon's shadow, so the ring sits a hand's width from the Sun. The light-time to the Boat now matches canon: Trojans are about 4.2–6.2 AU from Earth, so a round trip takes much under an hour and a half. The doubled trailer paragraph is split so the setting comes before the authorization.
- Trims: Mabs's second physical description is cut, and Colonel Buchanan gets an introduction at first mention.
- Appendix and bibliography: the Hein link text now matches the cited JBIS 2012 paper. Biosphere 2: nobody died; oxygen fell from 21% to about 14.5% and was topped up from outside. "Looking for Lurkers" is James Benford's 2019 proposal, not a search, and Gertz is no longer credited. Page ranges use en dashes. Checked and left as written: Starlink (over 11,000 working satellites) and Rubin's forecast Trojan count (about 109,000, several times today's catalogue).
- Verified: zip is clean, 376 paragraphs, all 18 hyperlinks, section properties intact.

For Lothar: no real total solar eclipse crosses Texas in late 2026. The real 2026 eclipse is 12 August (Greenland, Iceland, Spain). The book says "this year", so either keep the eclipse as invented, or move the story year.

## Light pass, 1 Oct 2026 evening (tidy + audit session)

Pre-edit copies: `bak/2026-10-01 pre-lightpass backup/`. Word count unchanged, 26,647.

- Tidy: `Protocol_Flamingo_Rev1.docx` moved to `bak/superseded/`; the scratch scripts `_gap.js` and `_pages.js` moved to `bak/scratch 2026-10-01/`. Nothing deleted. `build_docx.js` and `node_modules/` stay (the script still builds the earlier draft only; it must not replace Rev2).
- Fix: "pencilled" became "penciled" (Chapter V diner; American spelling). Edited in `word/document.xml` only; zip, paragraph count (376) and links unchanged.
- Checked and left: front matter, series line, Also by page and About the Author agree with `KDP_LISTING.md` (The Invasion Storybooks, Book 1, George Herbert Fontaine). The KDP description matches the book (six people drop phones, eleven seconds, eighty seconds of the water tower, "the committee has been meeting since 1947", Starfall two weeks out). Spell check found no other typos.
- Still open for Lothar: the late-2026 Texas total eclipse is invented (see above). The listing calls the book a novella (26,647 words is novella length); decide whether to sell it as a novel.

## Polish pass, 3 Oct 2026 (single session, no git)

Pre-edit copy: `bak/2026-10-03 pre-polish backup/`. The counts above are stale: the live Rev2 measured 2,428 paragraphs and about 77,000 words (three Books, 23 chapters) on 3 Oct, up from 376 paragraphs and 26,647 words.

- Fix: "neighbours" became "neighbors" (Book Two, the Trojan-swarm dot paragraph). The Also by page had a straight apostrophe in "Hadn't"; now curly. Edited in `word/document.xml` only; every other zip entry byte-identical, paragraph count, word count, 18 links and section properties unchanged.
- Checked and left: the title payoff (Gladys names it, Warren pencils it, the glossary explains the pink), Whitcombe's margin note in "Logistics", the closed ending, the Starfall chapters. Sweeps for Texas, Jupiter's shadow, Reno, "intern named Carl", straight quotes, double spaces and British spellings found nothing else ("burnt coffee" is fine as an American adjective).
- Not touched: `build_docx.js` still builds only the earlier draft.

## No-repeated-sentences pass, 4 Oct 2026 (single session)

Lothar's rule: no sentence may recur within the same book. Pre-edit copy: `bak/2026-10-04 pre-dedupe backup/`. 170 paragraphs changed; 76,990 → 76,908 words; paragraph count (2,428), links (18) and section properties unchanged; edited in `word/document.xml` only, every other zip entry byte-identical.

- Scan before: 93 repeated-sentence groups (3+ words) and 8 near-duplicates. After: none left except chapter titles that also sit in the contents list ("Eighty-Four Seconds", "The Company That Owns the Sky"), the bibliography titles that the appendix also names, and the bare interjection "I don't know,".
- Callbacks were reworded rather than copied: Rosa's rule ("he gets told, and he decides") now appears once verbatim (Rosa's own speech) and in varied form elsewhere; "That's the deal" is kept for Dominic and Nora's exchange at the end; the pen/pencil line, "an ask, and a yes", "for the other one", "sitting next to", the authorization text read twice, and gesture beats ("He looked at her", "Nora looked at him", "He did not move") were varied. Glossary entries that copied story sentences were reworded.
- Long shared phrases (8+ words) were checked too; the ones that were near-copies of a sentence were varied. Deliberate motifs were left (the grain of rice, "the way a man knocks wood" once, the hallway simile once).
- Also: the straight apostrophe in "The Dolphins' View of History" (Also by page) is now curly.
- To re-scan after any edit: split the book's text into sentences, normalize case and punctuation, and look for equal sentences of 3+ words outside headings, the contents list and the bibliography.

## Git

Parent repository is `My Books for Amazon`, remote `https://github.com/lotmus/My-Books-for-Amazon.git`.

Other folders in that repository belong to other books and other agents. They are often dirty. Commit and push only paths under `Protocol Flamingo/`. Do not `git add` the repository root. Do not force-push. Do not commit scratch files. This status file starts with an underscore on purpose. Do not delete every file whose name starts with an underscore.

As of 1 Oct 2026 the checkout and `origin/main` were the same commit, `e2b2cb1`, on the branch name `book-2-lectures-after-qed`. The manuscript’s last dedicated save in that history was `aab2e25`. Later sentences in the working copy (the thirty-three-year wait, and the producer killing Dominic’s name before the broadcast) may be newer than that commit. Confirm `git status` for this folder before pushing.

## How to edit

Edit `word/document.xml` inside Rev2. Phrases are often split across runs. Do not pretty-print the XML. If an anchor sentence is missing, stop and do not write the file. New story paragraphs are body text. Do not give them a Heading style, or they will show up as blank or extra entries in a contents list.

The bibliography must stay inside `w:body`, before the final `w:sectPr`. Do not append paragraphs after `</w:document>`.

Curly apostrophes and curly quotes. American spelling. The British lean is voice, not spelling.

## Canon — do not reopen

- The intern is Evan. Dr. Carl Daniels is the only Carl.
- Saturday wedding. Sunday post. Tuesday the video comes down. Tuesday night Mabs calls, then the flyer. Nora does not meet Jesse that night. Thanksgiving is two days later.
- The first meeting with Jesse is the diner in Chapter V, because she finally uses the time on the flyer.
- The man in the parking lot leaves once. Jesse then puts the recorder away.
- Mabs calls the morning the cars will not leave the block. The diner refers to that call.
- Confetti is eleven thousand pieces. The stadium seats eighty thousand. “Several thousand people quietly like him” means hybrids in that stadium, not the crowd.
- “Four days later” is correct twice: Dana’s scene after the wedding, and the alpaca visit after Gladys’s notes.
- The Boat is a dark hull a few kilometers across, in the Trojan swarm sixty degrees ahead of Jupiter. It is not in Jupiter’s shadow and it is not moon-sized. They noticed Earth’s noise in 1947 and waited thirty-three years. Forty-six years before this story, they came closer and took samples.
- The eleven missing hours are a sedated rendezvous with a shore boat already in high orbit. There is no faster-than-light trip. Nora did not agree to the sedative. She tells Dana the hours were taken. The Boat stays at the Trojans, about three-quarters of an hour away at the speed of light.
- Starfall’s reply comes from the shore boat, which is close enough to answer in seconds. The Boat hears the outcome later.
- The Dipstick reads one marker. Crew bodies make it in bulk. A hybrid leaks it. Steve smells the same marker. Gladys names the pink FLAMINGO. That is the title.
- Marin and Beluffi (2018) found that a crew of 98 can last about 6,300 years under strict rules. This ship has been sealed for forty thousand years. Its request is consented passage and consented samples. Children born on Earth to hybrid parents do not deliver genes to the Boat.
- The implant is neural-dust scale (Seo and colleagues, Neuron, 2016). It talks to a nearby hull, not to Jupiter. Bracewell’s 1960 Nature paper is the citation for the patient probe.
- The ending is closed. Curtis calls back. The Manitoba file closes. The Escort is alive on the shore boat. Nowak was a clerk in that office, and Dana stops looking. The badges work again on Wednesday. Halvorsen refuses Contingent Illumination. Whitcombe’s line stays in the file. Dominic goes home. Mabs keeps the napkin and the photograph of the plate, and she tells Nora to bring back the man who carved the turkey, not a file. Milo’s school note is on the refrigerator. He is not told the rest.
- Jesse sends a producer a voice memo that names Dominic. Nora does not forgive it that morning. The producer posts a cold open with no surname: Lissome, and eleven seconds. Mabs hears her town before Nora can warn her. At the stadium Jesse does not say the town again. Nora does not thank him.
- Kade tells Dana the hull, the swarm, the thirty-three-year wait, and the date. He does not explain the children. The escort does, on the ship.
- The second aircraft costs one Starfall sail. The ring in Texas is short that sail. Kade does not explain the gap.
- A Starfall flyer is on Nora’s windshield the night of the wedding. The Tuesday on it is wrong. The town is not.
- Dominic, the week after Thanksgiving, finds the napkin and asks for seats that face the screen.
- Curtis is answered after Starfall, from the garage in Fort Wayne.
- Three Handbook epigraphs remain: weddings, evidence, and fraternization. The cast list is gone. The glossary stays.
- Chapter XI is The Pretzel Corridor.
- The note to the reader and the cast list sit in the back, beside the cousins. The nine cousins are films, not books on sale. The series name a shopper can follow is The Invasion Storybooks.

## Still true, and not a defect

Mabs hears “he was a little drunk” and knows it is wrong. That is the scene. The Handbook is fiction and says so. The appendix and the bibliography are the citations. Handbook epigraphs stay. The book does not add a second paragraph that explains Mabs’s line.
