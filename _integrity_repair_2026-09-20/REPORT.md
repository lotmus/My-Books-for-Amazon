# Integrity repair report - 2026-09-20

Scope: every file under `C:\Users\lomus\OneDrive\My Books for Amazon` (about 3,500 files). Nothing was deleted.
Every file I changed had its damaged original copied first to `_integrity_repair_2026-09-20\originals_before_repair\` (same relative path).

## How the damage looks
Small blocks (usually 4 bytes) inside files were overwritten or dropped, sometimes with fragments of nearby text.
Windows logged "IO operation was retried" (event 153) on Disk 1 and Disk 2, the two JMicron external drives, and volume E: reports "Warning".
D: is one of them. The damage predates the move to OneDrive (some files were last saved 14-16 August).

## Repaired, each fix verified
| File | Fix | Source of the good data |
|---|---|---|
| QED Course: Complete docx + lesson 14, 15, 21 sources | rebuilt / 3 bytes-runs fixed | original base file + lesson sources, diffed against a pre-move snapshot (0 differences) |
| The Quantum World\backup\Draft\ch20.png | 3 damaged blocks | working copy + committed copy combined; PNG checksums pass |
| The Quantum World\backup\Draft\cropped\19.jpg | 2 blocks | committed copy (decodes cleanly) |
| Physics\Volume 1\drafts\Vol 1 Back Cover.png (really a JPEG) | 2 blocks | committed copy |
| Bureau series: Chinese and Hebrew TTS .xml | 3 + 5 spots | older committed copy and Hebrew manuscript |
| Schrodingers_Paperwork SSML .xml: German, Arabic, Chinese (x2), Czech, Greek, Hebrew, Portuguese | 1-3 spots each | manuscripts / sibling versions; three tag fixes follow each file's own repeating pattern |
| Schrodingers_Paperwork\_tmp_appendix_extract.txt | "S1935dinger" -> "Schrodinger" | manuscript text |
| Schrodingers_Paperwork\English\drafts\backup\...before_repetition_completeness_fixes.epub | 2 damaged members replaced, garbled header rewritten | byte-identical members from another EPUB (name, size and CRC match) |
| Science Books\Cosmology\The Body Keeps Its Own Clock - Manuscript\Figures\build_book.py | `paragraph_lignat` -> `paragraph_format` | committed line |

Also fixed by OneDrive itself (I did not modify them; they now pass all checks): the Spanish Kindle cover PNG and the two Audible-cover JPEGs.

## Still damaged
- `Science Books\The Quantum World\backup\Draft\Physics Vol 2 - cover.png`: the deflate stream is broken about 40% of the way in. Both the working copy and the committed copy are damaged and no other copy exists in the tree. Try OneDrive web > Version history, or restore from any earlier backup.

## Not damage
- Five `~$*.docx` files (162 bytes): Word lock-file leftovers. Safe to delete.
- `node_modules` files: vendor code, identical in two places.
- `Vol 1 Back Cover.png` is a JPEG with a .png extension. It decodes fine; my scanner just flags the extension.
- `QED Course\_build\corrupt\` holds the three damaged Complete-docx files, kept for reference.

## Limits
Damage is only detectable when a file has a checksum, a parser, or a reference copy. Silent damage inside plain English text or JPEG data with no reference cannot be found by any tool.

## Other things to know
- 201 files of `The Relativistic Investigation Bureau - SERIES\WORD` are still only on D:. They were never moved to OneDrive.
- `_integrity_repair_2026-09-20` is untracked by git; delete it after you have checked the results.
- Recommended: run `chkdsk` on D: and E:, try another USB port/cable for the JMicron drives, and stop using D: as a working drive. Commit and push the git repo regularly; its history saved most of these repairs.
