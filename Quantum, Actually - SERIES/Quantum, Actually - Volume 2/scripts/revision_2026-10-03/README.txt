One-off tools of the 2026-10-03 revision (already applied to the txt sources; kept for the record).
merge_prologues.py  - merged old Prologues 6+7 -> 8 and 8+9 -> 9
content_patch.py    - passages adapted from "notes/Unused from merge for QED Course.docx" and the former Quantum Conversation (P3, P4, P6, Mead interlude)
boxes.py            - First-pass and Plain-language box texts
apply_revision.py   - figures into L45-79, boxes, Core/Extension/Challenge labels, try-first lines, mastery-check trim
Build order: make_figures_lessons.py, make_figures_prologues.py, _rebuild_range.py, _insert_opening.py, _write_tail.py, _finish_book.py, _patch_lesson01.py
