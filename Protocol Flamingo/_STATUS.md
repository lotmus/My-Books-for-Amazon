# STATUS — Protocol Flamingo

Last updated: 2026-09-30. The live book is the expanded manuscript, not the generator.

## Live file

`Protocol_Flamingo_Rev2.docx` is the book. About 28,700 words. Pen name on the title page and in the file properties: George Herbert Fontaine. Story year is “this year” (2026). Series line on the title page: The Invasion Storybooks.

The paperback trim in the file is 5.5 by 8.5 inches, with a half-inch gutter and mirrored margins. Front matter is numbered in roman numerals. Page 1 is the start of the story. `KDP_LISTING.md` holds the description, keywords, categories, and price. `Protocol_Flamingo_cover_front.jpg` is a front cover at that trim, not a full paperback wrap.

`build_docx.js` builds the earlier, shorter draft and writes `Protocol_Flamingo_script_draft.docx`. Running it must not replace Rev2.

`Protocol_Flamingo_Rev1.docx` is an older file. `bak/` is a snapshot. Neither is the live book.

## Git

Parent repository is `My Books for Amazon`, branch `main`, remote `https://github.com/lotmus/My-Books-for-Amazon.git`.

Other folders in that repository belong to other books and other agents. They are often dirty. Commit and push only paths under `Protocol Flamingo/`. Do not `git add` the repository root. Do not force-push.

The review fix is on `origin/main` as `b85edf5`. Later scenes (Mabs’s drawer, the pretzel corridor, Milo’s school note, Whitcombe’s margin line) and the fixes below are in the working copy. Confirm which commit is on `origin/main` before pushing. Do not push `book-2-lectures-after-qed` onto `main`.

## How to edit

Edit `word/document.xml` inside Rev2. Phrases are often split across runs. Do not pretty-print the XML. If an anchor sentence is missing, stop and do not write the file. New story paragraphs are body text. Do not give them a Heading style, or they will show up as blank or extra entries in a contents list.

The bibliography must stay inside `w:body`, before the final `w:sectPr`. A previous edit left it after `</w:document>`. That has been put back. Do not append paragraphs after the document is closed.

Curly apostrophes and curly quotes. American spelling. The British lean is voice, not spelling.

## Canon — do not reopen

- The intern is Evan. Dr. Carl Daniels is the only Carl.
- Saturday wedding. Sunday post. Tuesday the video comes down. Tuesday night Mabs calls, then the flyer. Nora does not meet Jesse that night. Thanksgiving is two days later.
- The first meeting with Jesse is the diner in Chapter V, because she finally uses the time on the flyer.
- The man in the parking lot leaves once. Jesse then puts the recorder away.
- Mabs calls the morning the cars will not leave the block. The diner refers to that call.
- Confetti is eleven thousand pieces. The stadium seats eighty thousand. “Several thousand people quietly like him” means hybrids in that stadium, not the crowd.
- “Four days later” is correct twice: Dana’s scene after the wedding, and the alpaca visit after Gladys’s notes.
- The Boat is a dark hull a few kilometers across, in the Trojan swarm sixty degrees ahead of Jupiter. It is not in Jupiter’s shadow and it is not moon-sized.
- The eleven missing hours are a sedated rendezvous with a shore boat already in high orbit. There is no faster-than-light trip. Nora did not agree to the sedative. She tells Dana the hours were taken. The Boat stays at the Trojans, about three-quarters of an hour away at the speed of light.
- Starfall’s reply comes from the shore boat, which is close enough to answer in seconds. The Boat hears the outcome later.
- The Dipstick reads one marker. Crew bodies make it in bulk. A hybrid leaks it. Steve smells the same marker. Gladys names the pink FLAMINGO. That is the title.
- Marin and Beluffi (2018) found that a crew of 98 can last about 6,300 years under strict rules. This ship has been sealed for forty thousand years. Its request is consented passage and consented samples. Children born on Earth to hybrid parents do not deliver genes to the Boat.
- The implant is neural-dust scale (Seo and colleagues, Neuron, 2016). It talks to a nearby hull, not to Jupiter. Bracewell’s 1960 Nature paper is the citation for the patient probe.
- The ending is closed. Curtis calls back. The Manitoba file closes. The Escort is alive on the shore boat. Nowak was a clerk in that office, and Dana stops looking. The badges work again on Wednesday. Halvorsen refuses Contingent Illumination. Whitcombe’s line stays in the file. Dominic goes home. Mabs keeps the napkin and the photograph of the plate, and she tells Nora to bring back the man who carved the turkey, not a file. Milo’s school note is on the refrigerator. He is not told the rest.
- Jesse sends a producer a voice memo that names Dominic. Nora does not forgive it that morning. She tells Mabs anyway.
- Chapter XI is The Pretzel Corridor.
- The note to the reader and the cast list sit in the back, beside the cousins. The nine cousins are films, not books on sale. The series name a shopper can follow is The Invasion Storybooks.

## Still true, and not a defect

Mabs hears “he was a little drunk” and knows it is wrong. That is the scene. The Handbook is fiction and says so. The appendix and the bibliography are the citations. Handbook epigraphs stay. The book does not add a second paragraph that explains Mabs’s line.
