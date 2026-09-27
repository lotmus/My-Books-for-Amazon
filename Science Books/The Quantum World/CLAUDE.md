# The Quantum World — working instructions

## Scope: stay in this folder

This folder is its own book: *The Quantum World*, canonically at
https://github.com/lotmus/My-Books-for-Amazon/tree/main/Science%20Books/The%20Quantum%20World

**Do not leave this folder.** Don't read, edit, or comment on any other book,
folder, or repo in this account (the almanac *Lothar's Holistic Brain Farts*,
other Science Books, the History or Math Tower projects, other PRs, etc.)
while working on Quantum World, even if a fix elsewhere looks related or an
error here also appears to exist there. If something outside this folder
seems worth touching, say so and wait to be asked — don't go do it.

## Project facts

- **The deliverable is `The_Quantum_World__FINAL.docx`.** It has been through
  many editorial passes (fact-check, style, accessibility, hyperlink fixes);
  treat it as mature, not a draft needing a rewrite.
- `backup/` holds prior drafts, editorial feedback (ChatGPT/Grok/Gemini/
  Copilot), and old KINDLE/TEST builds. Read for context; don't restyle or
  clean it up unasked.
- `kdp_description_QW.txt` is the live KDP listing copy — treat claims in it
  (illustration count, simulator links, companion-volume framing) as things
  the manuscript should stay consistent with.
- Before editing the `.docx` directly (it's a zip), verify round-trip
  integrity: `testzip()` clean, entry list unchanged, `word/document.xml`
  still parses, and check `word/_rels/document.xml.rels` against a working
  backup copy before assuming a relationship is broken — this book has at
  least one hyperlink (`rId12`, the Schrödinger's-cat image) whose correct
  form looks broken to a naive check but isn't.
