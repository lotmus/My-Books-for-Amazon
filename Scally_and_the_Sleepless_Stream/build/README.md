# Build scripts for The Wee Scallywag and the Gentle Elf

Run from this folder with Python 3 (needs Pillow and python-docx) and pandoc.

- `python build_docx.py` builds the Word master `../The_Wee_Scallywag_and_the_Gentle_Elf_Book1.docx` from `../Step_Stories_Texts/Book1_Story_v7.txt` and the pictures in `../Step_Stories_Pics_Final/`. Set the environment variable `OUTDOCX` to write somewhere else (for example when Word has the master open).
- Build the EPUB (the file uploaded to KDP) from the docx with pandoc: `pandoc <docx> -t epub3 -o ../The_Wee_Scallywag_and_the_Gentle_Elf_Book1.epub --lua-filter=drop_first_image.lua --epub-cover-image=../Step_Stories_Pics_Final/cover_1000x1600.jpg --css book.css --split-level=2 --epub-embed-font=fonts/ComicNeue-Regular.ttf` (and the Bold, Italic and BoldItalic files), with title "The Wee Scallywag and the Gentle Elf", author "Anneliese Tauber", language en-GB.
- `python make_covers.py` makes the 1600x2560 front and back covers.
- `gen.py`, `gen_more.py`, `plain_gen.py` generate pictures through xAI Grok Imagine. The key is read at run time from `D:\My_C#_Apps\MediaStar.GPT\config\asset_api.ini` (`xai_key`); no key is stored in these files. Lothar authorised that file for this book on 11 Oct 2026.
- `fonts/` holds Comic Neue (SIL Open Font License, OFL.txt included).
- Picture-to-paragraph anchors are the `place` table in `build_docx.py`; the script prints any anchor that does not match exactly one paragraph.
