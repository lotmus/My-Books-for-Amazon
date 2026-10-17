# Book 3: Scally and the Hill with the Hanging Socks

The Step Stories, Book 3, by Anneliese Tauber. Docx is the working master, the EPUB is the upload file; file names carry the version.

- Story: `Step_Stories_Texts/Book3_Story_v10.txt` (11 chapters plus Hal's Slate, American English).
- Built files: `Scally_and_the_Hill_with_the_Hanging_Socks_Book3_v10.docx` and `.epub` (119 story pictures plus cover).
- Outline and notes: `Book3_Outline_v1.md`. Store listing: `KDP_Description.md`.
- Pictures: `Step_Stories_Pics_Final/` (`p001_ch01.jpg` and so on, one per planned anchor; `00_cover_art.jpg`; reference sheets).
- Build: run `python build/make_build_book3.py` (writes `build_book3.py` from the Book 2 script and the picture plan `b3_plan.json`), then `python build/build_book3.py`, then pandoc for the EPUB as in Book 2's README. Picture plan and generation: `build/b3_pics.py plan` then `build/b3_pics.py` (xAI Grok Imagine, reference `reference_cast_sheet_b3.jpg`). Covers: `build/b3_cover.py` and `build/make_covers_book3.py`.
- Convert new text to American spelling with `Scally_and_the_Sleepless_Stream/build/us_spelling.py`.
- Old versions and rejected pictures are in `bak/` (not committed).
