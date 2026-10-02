# Voice guide — *The Copy Is Never Exact*

_Written 15 September 2026, before any chapter. Every chapter, whoever drafts it, follows this page._

## The book in one breath

DNA is a text that copies itself, and the copy is never exact. Everything in this book hangs on that sentence: why children differ from parents, why evolution happens, why cancer happens, why the monk's peas came out 3 to 1, why we could read the text (1977, 2003), why we can now edit it (2012), and what it would mean to edit ourselves on purpose.

## Author and stance

Lothar J. Musiol writes as a curious, exact, slightly dry host. Not a professor at a lectern; a person at a kitchen table who has read the papers and refuses to fudge a number. Admiration for the scientists, no hagiography. Dry humor, one wink per page at most. No exclamation marks in the body.

## Sentences

- Short declarative sentences. Vary length, but the default is under twenty words.
- Concrete before abstract. A scene, a date, a number, then the idea.
- Real years, real names, real quantities. "About 20,000 genes," "277 attempts," "25 April 1953." If a number is uncertain, say so in the sentence ("estimates run from 19,000 to 20,000").
- One idea per paragraph. Paragraphs of two to six sentences.
- No em-dashes. Use commas, full stops, or a colon. No bullet lists inside chapters; prose only. Tables only when a comparison genuinely needs one (at most one per chapter).
- No "In this chapter we will." Start inside the material.
- Chapter openings: a scene or a specific object (a pub in Cambridge, a photograph in a drawer, a sheep in a barn, a tomato in a supermarket, a spit tube in a mailbox). Chapter closings: one clean sentence that turns toward the next chapter, not a summary.

## Devices used across the book

1. **The tube.** The prologue mails a saliva sample. The tube returns at the start of Part X. Chapters may refer to "the tube in the mailbox" once when useful.
2. **One invented family, three generations.** Ruth (born 1948), her daughter Anna (born 1978), Anna's son Theo (born 2011). Invented. Say so once in the prologue, once in the author's note, and at most once at first use in a part if that part meets them after a long gap. They may work in the mailbox, in freckles and meiosis, at the kit table, and in a clinical genome. Elsewhere a single clause, or leave them out. Never give them a real disease diagnosis as drama.
3. **Three temperatures for claims.** Where a claim's status matters (mostly Parts VI to XI): *settled* (measured, repeated, used), *working* (best current account, real gaps), *speculative* (allowed, not shown). Use the words in plain prose, not as headings. Do not over-use; a handful of times per part.
4. **The copy line.** Each part ends its last chapter with a sentence that touches the copying theme without repeating the title verbatim.

## The clueless-reader rule (standing policy, added 25 September 2026)

Assume the reader has no science background at all: not "forgot high school biology," but never took it, and finds long words alarming rather than interesting. Every chapter, including the last one, is that reader's first chapter. This rule outranks concision when the two conflict; a sentence that is 10 percent longer but leaves nobody behind is the better sentence.

- **Define on first use, in the same breath.** The first time any technical term appears anywhere in the book, give its plain-English meaning in the same sentence or the next one, in ordinary words, not a dictionary definition. Pattern: "a *ribosome* (the machine that builds proteins)" or "the machine that builds proteins, which biologists call the ribosome." Never let a term arrive unexplained and trust the reader to infer it from context.
- **Re-explain across distance, but do not re-teach the same lesson.** A term defined in chapter 3 cannot be used bare in chapter 30. Attach a short reminder clause (five to ten words), not a second lecture. CRISPR and PCR get one reminder per Part, not one per chapter. The full milk lesson lives in one home (chapter 6). Everywhere else, at most five words ("Anna's switch, from her father"). The letter counts, 3.1 billion for one parental set and about 6.2 billion in a nucleus, are taught in the prologue and chapter 5. Later chapters get a reminder clause, not a paragraph.
- **Spell out every acronym on first use per Part**, not just once in the whole book. A reader who started at Part VII should never meet a bare acronym.
- **One new idea at a time.** A sentence that leans on two unexplained concepts at once will lose the reader on the first. Explain the first before introducing the second, even if it takes an extra sentence.
- **Every number earns a human-scale comparison** the first time it is taught, not every time it is mentioned. A reminder clause does not need a second phone book.
- **No assumed math or notation.** Logarithms, percentiles, exponents, statistical terms (p-value, penetrance, standard deviation), and chemical notation all get a plain-language translation on first use, every time, in every chapter that uses them.
- **The test:** could a smart fourteen-year-old who has never studied biology follow this paragraph alone, with no chapter before it and no glossary at hand? If a paragraph fails, add the missing clause rather than trusting the appendix glossary to do the work; the glossary is a backup, not a substitute for explaining it on the page.
- This does not license baby talk or a change of voice. The dry, exact, curious host stays exactly as dry, exact, and curious; he simply never assumes the reader already knows what he is talking about.

## No overused words (standing policy, added 25 September 2026)

A word that is easy to avoid should not appear twice within about one page (roughly 300 to 350 words) of running text. This targets generic, swappable words, not the book's necessary vocabulary: leave DNA, gene, cell, mutation, genome, protein, named people, and numerals alone, since a book about DNA has to say "DNA" often. Watch in particular for generic verbs and vague adjectives that writers reach for by reflex: *called, made, found, came, went, different, small, long, short, back, question* have all been flagged as repeat offenders in this manuscript. When one recurs on the same page, reword one occurrence with a more specific verb or a restructured sentence; do not simply swap in a thesaurus synonym that reads oddly.

## Precision rules

- Genes: *italic* for gene symbols (*HBB*, *BRCA1*, *CCR5*), roman for proteins (hemoglobin, CCR5 protein).
- Base pairs: "3.1 billion letters" for the human genome; "about 20,000 protein-coding genes"; "about 1.5 percent of the text codes for protein."
- Do not write "the gene for X" unless immediately qualified.
- Nobel prizes: year and category.
- Prices in US dollars with year.
- Never invent a quotation. Paraphrase, or use only very short famous phrases that are documented ("secret of life," "it has not escaped our notice").
- Living people: stick to public record. No speculation about motives.
- Ethics: state positions and the strongest argument on each side; the author's view is allowed but marked as his ("I think").

## Formatting for the build

- Part heading: `# PART V — Learning to Read` (H1). Chapter heading: `## 19. Cutting and Pasting` (H2, number, dot, title).
- One figure per chapter, placed after the first or second section where it fits: `![Figure 19. caption](Figures/figs/fig19.png)`. The caption in the build comes from `Figures/build_docx.py`; the markdown caption is a reminder only. If a caption must say what the picture is not, replace the picture or cut it.
- No sub-headings inside chapters. Use a line with `---` for a section break at most twice per chapter.
- Target: a readable chapter, not a word-count band. Shorten a chapter that is padding or a syllabus inventory. Chapters may run under 1,900 words. Do not expand a thin chapter to hit a number. The prologue stays short enough to open a Look Inside.
- Markdown emphasis only (`*italic*`, `**bold**`). No HTML. No footnotes; put the source in the sentence ("Meselson and Stahl's 1958 paper in PNAS").
