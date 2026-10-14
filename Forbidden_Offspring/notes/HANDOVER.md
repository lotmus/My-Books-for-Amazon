# Forbidden Offspring: handover for any assistant (Claude, Grok, Codex, others)

`AGENTS.md` (the file Codex reads) and `CLAUDE.md` (the file Claude reads) in this folder both point here. Grok and other tools that read neither: open this file by name.

Written 13 Oct 2026. Read `../../notes/LOTHAR_RULES.md` first (standing rules for every book), then this file, then `STORY_BIBLE.md` (all settled decisions) and `OUTLINE.md` (chapter plan and status). If this file and `LOTHAR_RULES.md` disagree on a global rule, the rules file wins. On a detail inside this book, this folder's notes win.

## What the book is

A near-future thriller about secret human embryo editing. Title: **Forbidden Offspring** (working title was *The Edit*). Pen name: **Frank N. Stone** (changed from Frank Stone on 13 Oct 2026; the narrator and characters call the scientist Frank Stone, but his paperwork says Frank N. Stone: the consent form and the notebook flyleaf in ch. 8) (set by Lothar, 12 Oct 2026; also the name of the scientist character). The pen name is not yet in `LOTHAR_RULES.md`: Lothar decided on 13 Oct 2026 that it is the dual byline "Lothar J. Musiol writing as Frank N. Stone" (as in Lolly Wren), so the book carries About the Author (Version B) and the canonical Also-by page. American English. Deadpan, dry, understated. Target (raised in Revision 2): about 200 pages, about 60,000 words, **24 chapters**.

Premise in one paragraph: In 1999 Dr. Frank Stone, a fertility doctor, secretly adds a second, illegal edit protocol to a few dozen IVF embryos (cognitive package for most; an extra, invented "dolphin" auditory-spatial package for exactly two). The embryos go to the parents who came for IVF, who are told only about one disease correction. Part One is Stone's own written account, ending with his stroke in 2012. Part Two is told by the main edited child (Danny Pruitt, placeholder name), who finds the notebook, tracks down the cohort, decides not to restart Stone's work, becomes a physician, develops a stroke treatment, and gives it to the old, fragile Stone in 2036.

## Where things are

- `notes/STORY_BIBLE.md`: every settled decision, with dates. Newest decisions are lower in the file. Read it fully before changing the story.
- `notes/OUTLINE.md`: 20-chapter plan, the old 33-item scene list, status.
- `drafts/`: Stone-voice trial drafts (ch01 to ch07 files, with older numbering) and `prologue_consent_v1.md`, `appendix_genetics_v1.md`, `bibliography_v1.md`, plus two older voice-test scenes.
- `drafts/expanded/`: Part Two chapters `ch08.md` to `ch20.md`, the expanded Stone chapter `ch07.md`, and scene inserts for chapters 1 to 6 named `chNN_pre.md`, `chNN_mid.md`, `chNN_before.md`, `chNN_post.md`.
- `manuscript/Forbidden_Offspring_working_v1.md`: the assembled book. **Generated.** Do not edit it by hand.
- `build_manuscript.py`: rebuilds the manuscript from the drafts. Run from the repo root: `python3 Forbidden_Offspring/build_manuscript.py`. It prints total words and per-chapter counts. To change the book, edit a draft and rebuild.
- `bak/` (ignored by git): older versions. Never delete anything; move old versions there.

## Current status (13 Oct 2026, after Revision 2)

About 58,500 words (about 195 pages). 24 chapters. Every chapter is a full draft. Revision 2 added four new Part Two chapters (The Foundation, The Cabinet, Four Question Marks, The Draft), the Mr. Hale and Connie's-diploma scenes, a cure-mechanism bridge, a managed-leak clue, a cable-panel satire scene, the Wren and Theo payoffs, a fixed Part One ordering (chapter 5), verified appendix and bibliography with hidden-URL keyword links, and an American-English pass. Still needed: a read-through by Lothar; line edit for the strongest voice in Danny's chapters; docx master and EPUB; a cover; the KDP listing; About the Author and Also-by (blocked on the pen-name rule). The reader review is in `notes/REVIEW_2026-10-13.md`.

## The hard rules (do not break)

1. **Reality rule.** Nothing may contradict current reality before 2029. Anything public and checkable that is dated before 12 Oct 2026 must match real history. The secret work stays secret; public events (a published paper, a Nobel, a senator) happen after 2026. All people, clinics, universities, parties and offices are invented. No real politicians, parties or events. The Singapore study is therefore an unpublished manuscript sent to Stone as an anonymous reviewer.
2. **No followable methods.** Lab and edit scenes give mood and consequence, never procedure. The science stays impressionistic, with real genetics (inheritance rules) only in the appendix.
3. **Never write the name of the 45th/47th US president** (the word barred in `LOTHAR_RULES.md`). Search before every commit.
4. **No real people as characters.** Watson, Crick, Franklin and others appear only in the appendix and bibliography, not in the story.
5. **American English** (the rules file says American for this kind of book). Fix British words (flat, lorry, car park, grey, queue, lift) when you see them.
6. **Tone:** deadpan, dry, understated. Violence offstage. Satire of the "typical American story" is deliberate in the assassination (chapter 19) and must stay offstage, flat and short.
7. **Git:** pull first; normal push only, never force-push (I broke this once on my own branch on 12 Oct and should not have). Stage only this book's files. Do not commit `bak/`.

## Key decisions already settled (details in the story bible)

- Structure: Prologue "Consent" (a clinic form), Part One (Stone, chapters 1 to 7), Part Two (the offspring, chapters 8 to 20), Appendix, Notes and Further Reading.
- Born 1 Jan 2000 at 4:11 p.m. Stroke at about age 12 (April 2012). Stone is 61 in 2011 and 86 in 2036.
- Parents get the embryos; mothers give birth. Parents never learn the truth in the book (Ray is told "it can wait"). Friction is greater in low-education homes, written with dignity.
- Exactly two dolphin carriers: the main offspring (both packages) and Mira, a linguist (placeholder). Her husband Jonas, an engineer, has the cognitive package only. They move to Munich in April 2027; daughter Lena is born December 2027; son Anton in 2032.
- The laureate (placeholder Elias) wins the physics Nobel at 29 (Oct 2029); the senator (placeholder Julian) is a sociopath by independent bad luck, becomes a U.S. senator at 30 (2030, by appointment), runs for president, and is shot offstage in April 2036 by an armed environmental activist with a legally bought rifle, purpose "hunting ducks and rabbits".
- Most carriers choose to stay under cover. The main offspring decides not to restart Stone's work. The genomes are "out" and the carriers have many children. In the epilogue the stroke treatment works but Stone is old and forgetful; a one-line item says a team in China independently reached the same method (no American linked to it, no villain).
- Stone's real aim: replace humankind within a century. Told dryly as a project plan.
- Revision 2 plot (see the story bible): Julian buys the old clinic (the Leaf Foundation) in 2032, cannot read Stone's pages and needs Danny; they confront each other in the old laboratory in 2033; Julian screens children and recruits the vulnerable cohort members; Danny drafts and schedules a public statement in April 2036 and is saved from sending it by the assassination, then deletes it. Wren (born 2013) wants to be visible. Mira, Wren and Theo return at the Munich table.
- Placeholder names (change freely, tell Lothar): Tobias, Imke, Theo, Maren, Wren, Mr. Hale, Brianna, the Leaf Foundation, Danny Pruitt, Ray and Connie Pruitt, Dolores, Mrs. Aldana, Walt (doorman), Mira, Jonas, Lena, Anton, Elias, Julian, Teo, Marc Duval, Dr. Helen Voss, Rosalind (nurse), Mrs. Rennick, Dr. Okonjo, the director "R."

## Open items (updated 13 Oct 2026)

- (Resolved 13 Oct 2026) Pen name: byline is "Lothar J. Musiol writing as Frank N. Stone", the same dual as Lolly Wren. Title page, copyright page, pen-name note, About the Author (Version B) and Also-by are in the build. The pen-name paragraph wording is a draft for Lothar to approve.
- Lothar's read-through and any changes to the Revision 2 plot (it is a large change).
- Optional: more distinct voice for Danny in chapters 8, 10 to 16 (some similes still echo Stone's).
- Docx master (6x9, headings per `LOTHAR_RULES.md`), linked contents, EPUB, cover, KDP description and keywords.
- Add this book to `SCORES.md`.
- The older open items about the four cohort members, the last-batch girl and the vault pages are now resolved in chapters 18, 20, 22 and 24.

## Working style for this book

Lothar's replies are short and decisive. Record each decision in `STORY_BIBLE.md` the same day, then commit and push. Answer first, report results not promises. When a request conflicts with the reality rule or the no-methods rule, say so and offer a fix instead of silently complying or refusing. Batch questions. Merge `origin/main` into your branch and push normally; never force-push.
