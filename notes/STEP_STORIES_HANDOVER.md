# The Step Stories: handover for any assistant (Claude, Codex, Grok Bot)

Written 13 Oct 2026 by the Claude session that built Books 1 to 3. Read `notes/LOTHAR_RULES.md` and `notes/HANDOVER.md` first. If this file disagrees with a book's own README or KDP file, the book's file wins inside that book.

## What it is
Children's STEM-fantasy chapter books by **Anneliese Tauber** (pen name, the same as *Bavarian Cooking Made Simple*). Lothar's own name must never appear in these books or their listings. The series is **The Step Stories**; every title after Book 1 follows "Scally and the ...". Audience is mainly in the USA, ages 6 to 10.

| Book | Folder | Current files | Words | Pictures |
|---|---|---|---|---|
| 1. The Wee Scallywag and the Gentle Elf | `The_Wee_Scallywag_and_the_Gentle_Elf` | `..._Book1_v20.docx`, `.epub`, story `Step_Stories_Texts/Book1_Story_v20.txt` | about 11,200 | 65 + cover |
| 2. Scally and the Sleepless Stream | `Scally_and_the_Sleepless_Stream` | `..._Book2_v14.docx`, `.epub`, story `Book2_Story_v14.txt` | about 14,000 | 83 + cover |
| 3. Scally and the Hill with the Hanging Socks | `Scally_and_the_Hill_with_the_Hanging_Socks` | `..._Book3_v8.docx`, `.epub`, story `Book3_Story_v8.txt` | about 22,600 | 119 + cover |

The docx is the working master; the **EPUB is the upload file for KDP**. File names carry the version (`..._v20`). When you change a book, copy the story file to the next version, rebuild, move the old version to `bak\Story_previous_versions` (not committed), and update `KDP_Description.md` and `notes/BOOK_LOCATIONS.md`. Junk goes to `junk\`. No PDFs, no Word tables, no floating images. The name Trump must never appear.

## Standing content rules (from Lothar)
- **American edition.** American spelling and words (color, gray, candy, cookie, Mom, "Mr." with a period, dollars), EPUB language en-US, and nothing Bavarian-specific for US readers. Convert new text with `Scally_and_the_Sleepless_Stream/build/us_spelling.py`.
- **Scally always tries a scam, lie or cheat in every book, and something makes him reconsider.** Vary who stops him (Hopsi, a child, a consequence, his own conscience). From Book 3 he hums a warning rhyme before each scam: "Just a little, just a bit, who will ever notice it?"
- **Hopsi** (elf) only says what is true, says "I do not know" and "I think", and is sometimes wrong and says so. Hopsi and Scally have **no stated ages** and look almost the same book to book; the human children visibly grow: Hal 8 (Book 1), almost 9 (Book 2), 9 and a half (Book 3), about 10 and a bit (Book 4). Tabitha is 7 in Book 1. Pip, Titch's little brother, is 7 in Book 3.
- **Ears:** only Scally and Hopsi have pointed ears. Every other person has round ears.
- **Safety teaching is on purpose** (strangers and a code word, fire, water: reach or throw, storms, floods, ice, medicine, wild animals: never touch a bat, getting lost: stop and stay). Keep it in the action, never preachy.
- **Tone:** warm, funny, gentle but with real stakes. Original episodes in the spirit of Astrid Lindgren (Emil, The Children of Bullerby, Pippi Longstocking), Pumuckl and Dr. Seuss rhythm are welcome (Book 4 will lean on them heavily). Their works are in copyright: **never copy their scenes, characters or lines.**
- **No repeated sentences** inside one book; scan after each edit round. Hal's Slate / Hopsi's True Things at the back of each book: short fact and experiment notes; mark storybook machines as storybook.
- Pictures: painted oil style, only characters who are acting appear, nobody staged and looking into the camera, every picture tells part of the story so non-readers can follow.
- The author bio: Anneliese is a mother of four who read her children many fairy tales. No Bavaria claim.
- Cast notes: Hal (Halbert) Millersen; Scally (true name Sparefunk, used on special occasions); Hopsi (Elfie Didlhop); Titch Mitchel; Tabitha Smoke (Black girl); Pip; Gucci the wolf (named after Lothar's Pomeranian); Fourpence the bird; Old Walt and Dumpling the donkey (Book 2); Wen Liang (Asian boy, about 9) and his mother Dr. Liang the village doctor (Book 3); Mayor Pomfrey; Mrs. Crumb the baker.

## Where we are (13 Oct 2026)
- Books 1 and 2 are finished drafts with docx and EPUB, reviewed in several critic passes (parent, child, KDP editor). Kindle Previewer converts all three EPUBs with 0 errors and 0 quality issues.
- Book 3 (pregnancy book) has a complete first draft, built with 119 automatically generated pictures reviewed only on contact sheets, a cover (bats hanging like socks on a clothesline) and a KDP file.
- **Decided by Lothar, 13 Oct 2026:** the baby brother is **Beau** (nickname Biscuit, chosen by Pip) and the red-haired girl who arrives in Book 3's last line is **Dixie** (unnamed in Book 3; name her in Book 4). Southern-flavored names are welcome for new characters.
- **Still open for Lothar:** whether the Book 3 split "pregnancy book, then baby book (Book 4)" is confirmed; which parent drinks too much at the Book 4 feast (theme decided: a parent drinks too much and is unwell, the children learn they will never drink that much; handle gently, no preaching).
- **Book 4 plan:** the baby book (newborn weeks, sleepless nights, safe baby habits, a naming feast for Biscuit, the redhead arrives, heavy Lindgren and Pumuckl spirit). Hal's mother's baby is due in June (Book 3 story time).

## Still to do
1. Full-size review of the Book 3 pictures; redo the weak ones (tall red caps on Titch and Pip look gnome-like, Gucci's size varies). Redo recipe: `build/b3_pics.py <from> <to>` after deleting the bad files.
2. A read-through by a teacher, a doctor and a wildlife expert for the science and safety (bats, ultrasound, ice, hibernation) before upload; `Message_to_Reader.md` and `Teacher_Check.md` in Book 1 can be adapted.
3. KDP uploads (AI-illustration disclosure is required; price, categories and age range are Lothar's choice).
4. Add an "Also by Anneliese Tauber" page to the Bavarian Cooking docx listing Books 1 to 3 (that folder is owned by another session).
5. Update the "Next in the Series" page of Book 1 and the last page of Book 2 when Book 3 has a date.
6. Book 4 outline and the drinking-theme scene.

## How to build (Windows, Git Bash)
- Python 3 with `python-docx` and `Pillow`, and `pandoc` on the PATH. Kindle Previewer 3 is installed at `C:\Users\lomus\AppData\Local\Amazon\Kindle Previewer 3\` and can convert an EPUB from the command line: `"Kindle Previewer 3.exe" book.epub -convert -output <dir>` (read `Summary_Log.csv`: errors and quality issues must be 0).
- Book 1: `cd The_Wee_Scallywag_and_the_Gentle_Elf/build && python build_docx.py`. Book 2: `cd Scally_and_the_Sleepless_Stream/build && python build_book2.py`. Book 3: `cd Scally_and_the_Hill_with_the_Hanging_Socks/build && python make_build_book3.py && python build_book3.py` (the first script regenerates the build script and the picture anchors from `b3_plan.json`). Each build prints `ANCHOR PROBLEM` if a picture anchor does not match exactly one paragraph, and `UNLINKED` for science items without a link. Set `OUTDOCX` to build to another path if Word has the docx open.
- EPUB: `pandoc <docx> -t epub3 -o <epub> --lua-filter=drop_first_image.lua --epub-cover-image=../Step_Stories_Pics_Final/cover_1000x1600.jpg --css book.css --split-level=2 --metadata title="..." --metadata author="Anneliese Tauber" --metadata lang=en-US` plus `--epub-embed-font=fonts/ComicNeue-Regular.ttf` (and Bold, Italic, BoldItalic), run from the book's `build` folder.
- Pictures: the xAI Grok Imagine API (`grok-imagine-image-quality`, `/v1/images/edits`) with a reference cast sheet. The key is read at run time from `D:\My_C#_Apps\MediaStar.GPT\config\asset_api.ini` (`xai_key`; Lothar authorised that file for this). **Never print, copy or commit the key.** Scripts: `build/gen.py` (helper), Book 2 `b2_scenes.py` (hand-written scenes), Book 3 `b3_pics.py` (automatic prompts from story paragraphs; `plan` then run). Reference sheets: `reference_cast_sheet.jpg` (original six) and `reference_cast_sheet_b3.jpg` (adds Wen, Pip and Dr. Liang). Rejected pictures go to `bak\`.

## Git rules for this series
- Never reset or clean the shared checkout `D:\My Books for Amazon` (other sessions have uncommitted work). Work in a temporary git worktree under `C:\Users\lomus\git-dirs\` (the one used so far is `wt-scallywag`, on the branch `scallywag`).
- Always `git fetch` and merge `origin/main` first, commit only these three book folders and the notes you touched, then push normally (never force): `git push origin HEAD:main HEAD:scallywag HEAD:sleepless-stream`. If `main` has moved, merge it in and push again.
- Do not commit `bak\` or `junk\`. EPUBs are allowed in the repo.
- After a push, copy the new files to the matching folders under `D:\My Books for Amazon\` (the D: copies are what Lothar opens).

## Where to read more
Each book folder has a `README.md`, a `KDP_Description.md` (title, subtitle, description, keywords, categories, upload checklist) and `build\README.md` (Book 1). Book 3 also has `Book3_Outline_v1.md`.
