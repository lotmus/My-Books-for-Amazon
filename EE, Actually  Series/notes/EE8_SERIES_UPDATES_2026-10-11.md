# Book 8: shared files others should update (11 Oct 2026)

Book 8 was built without touching any shared file, Book 1-7 file, or SCORES.md while Books 1-7 were being revised. Book 8 has since been reviewed and rebuilt; see `notes/EE8_REVIEW_2026-10-12.md`. These shared-series edits remain open.

1. `D:\My Books for Amazon\SCORES.md`: the Book 8 editorial manuscript score of 8.5/10 is now recorded after Book 7. Score market fit after the cover and KDP listing are ready.
2. `notes\ALSO_BY - canonical list.md`: under **Electrical Engineering Series**, after "Packaging, Layout, EMC, and Test (Book 7)", add
   - Firmware and Software for Electronics (Book 8)
   Then regenerate the Also-by section of every book that prints the list (EE Books 1-7 and the other series), and add its Amazon link rule to each book's kindle_links json (Book 8's own json shows the pattern).
3. `notes\BOOK_LOCATIONS.md`: after item 7 add
   8. Book 8, Firmware and Software for Electronics (`EE - SERIES\Firmware_and_Software_for_Electronics_Book8.docx`). Sources are the master: `chapters\Book8\src` (build with `scripts\build_b8.py`); listings in `scripts\diagrams\b8\listings`.
   and change "seven" wording in the EE paragraph where it counts the books.
4. Other books' series lists: any front matter or How to Use This Book text that says "seven books" or lists Books 1-7 (search the EE sources for "seven" and "Book 7").
5. `scripts\make_ee_covers.py`: add entry 8, title lines ['FIRMWARE AND', 'SOFTWARE FOR', 'ELECTRONICS'] (or two lines if it fits), subtitle "Embedded C, Python, C#, and HDL at the Bench".
6. `scripts\ee_deploy.ps1`: header says "seven-book layout"; Book 8 builds from sources, so deploy is `python scripts\build_b8.py` then kindle_links.py, not the docx2src round trip.
7. Back cover and KDP series page: add Book 8 when the cover is made.
8. Optional: one line in Books 2, 5 and 7 pointing firmware readers to Book 8 (one-home rule, other direction).
