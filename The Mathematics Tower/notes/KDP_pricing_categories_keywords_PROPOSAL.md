# The Mathematics Tower — KDP pricing, categories and keywords (PROPOSAL)

**Status: draft for Lothar to approve. Nothing has been entered in KDP and nothing is published.**
Written 1 Oct 2026 (PT). Author: Lothar J. Musiol. Sources: `KDP_Description.md`, `notes/CLAUDE.md`,
`notes/Tower - Series Reference.md`, the four master `.docx` files, and KDP's own help pages (checked 1 Oct 2026).

## 1. What is being priced

| Volume | Title (from `KDP_Description.md`) | Floors / rooms | Body words (1 Oct notation sweep) | Word pages in the master (US Letter) | Est. paperback pages at 7 × 10 in |
|---|---|---|---|---|---|
| 1 | The Lower Floors — Floors 1–12: From Arithmetic to Calculus | 12 / 109 | 169,228 | 525 | ≈ 656 |
| 2 | The Middle Floors — Floors 13–25: From Multivariable Calculus to Set Theory & Logic | 13 / 118 | 182,245 | 608 | ≈ 760 |
| 3 | The Upper Floors — Floors 26–37: From Differential Equations to Abstract Algebra | 12 / 108 | 192,678 | 581 | ≈ 726 |
| 4 | The Penthouse — Floors 38–50: From Category Theory to the Frontier | 13 / 117 | 176,600 | 563 | ≈ 704 |

- The masters are Kindle files laid out on US Letter (8.5 × 11 in, 1.1 in side margins). No print layout exists yet.
- The 7 × 10 page counts are estimates. They scale the Letter text area (6.3 × 9.0 in) to a 7 × 10 text area of about 5.4 × 8.4 in, a factor of about 1.25. Rebuild a 7 × 10 print docx before trusting them.
- The Word page counts (525 / 608 / 581 / 563) are the last recount in the series reference. The `docProps` page counters in V3 and V4 are stale.
- **Omnibus:** a single-volume paperback is not possible. All four together are about 2,280 Letter pages, and KDP's paperback maximum is 828 pages (white paper; 776 on cream). A complete edition can only be an **ebook**. The old complete build in `bak\READY (2026-09-26)` is out of date, so it would have to be rebuilt from the current four masters.
- Paper: use **white**. V2 at about 760 pages is close to the 776-page cream limit, and white suits diagrams.

## 2. KDP rules this is based on (Amazon.com, checked 1 Oct 2026)

- **Paperback royalty:** 60% of list price minus printing cost, at a list price of $9.99 or more (50% below $9.99). Expanded Distribution pays 40% minus printing.
- **Printing cost, black ink, white or cream paper:** fixed $1.00 + per-page charge. Regular trim (up to 6.12 × 9 in): $0.012/page. **Large trim (7 × 10 and 8.5 × 11 are both large): $0.017/page.** Books of 24–110 pages pay a flat fee instead.
- **Kindle 70% band:** **since 7 July 2026 it is $2.99–$12.99 on Amazon.com** (it was $2.99–$9.99 before). Royalty = 70% × (list price − delivery cost). Delivery cost is $0.15 per MB of the converted file. Above $12.99 the rate is 35%, with no delivery cost.
- **Categories:** 3 per format, chosen from Amazon's own category tree. KDP no longer asks for BISAC codes. Amazon maps the chosen shelf to a BISAC code itself. The BISAC codes below are listed to show the intended subject. The KDP picker is what matters.
- **Keywords:** 7 fields per format, up to 50 characters each. Do not repeat words already in the title, subtitle or series name.

## 3. Comparable books (US store)

| Book | Format / length | Price seen |
|---|---|---|
| Ivan Savov, *No bullshit guide to math and physics* (indie, Minireference) | paperback, 528 pages | $23.31 on Amazon; $31.35 list elsewhere |
| Richard Hammack, *Book of Proof* (open text, print on demand) | paperback | $24.27–$37.45 |
| David Austin, *Understanding Linear Algebra* (open text) | paperback / hardcover | $28 / $36 |
| APEX Calculus (open text, split into volumes) | B&W paperback per volume | $15 (subsidized: the PDF is free) |
| Barron's AP Calculus Premium 2026 | paperback | $29.99 list |
| Indie Kindle calculus workbooks in the Mathematics bestseller list | Kindle | $0.99–$9.99 |
| Traditional university textbooks (Springer UTM, Pearson, OUP) | paperback / hardcover | $40–$150+ |

The Tower volumes are each 650–760 pages with answers and full solutions. That is more than the indie comparisons and close to a university text. A price between the indie books and the publisher textbooks fits: about $35–$40 in paperback, and at the top of the 70% band for Kindle.

## 4. Proposed prices and royalty per sale (US)

### Paperback — 7 × 10 in, black ink, white paper (recommended trim)

| Volume | List price | Est. pages | Printing cost | Royalty per sale (60%) | Expanded Distribution (40%) | KDP minimum list price |
|---|---|---|---|---|---|---|
| 1 | **$34.99** | ≈ 656 | $12.15 | **$8.84** | $1.84 | $20.25 |
| 2 | **$39.99** | ≈ 760 | $13.92 | **$10.07** | $2.08 | $23.20 |
| 3 | **$39.99** | ≈ 726 | $13.34 | **$10.65** | $2.65 | $22.24 |
| 4 | **$39.99** | ≈ 704 | $12.97 | **$11.03** | $3.03 | $21.61 |
| Paperback box set | not possible on KDP | — | — | — | — | — |

Volume 1 is $5 cheaper because it is the entry point, and the readers it targets (adults coming back to maths) are the most price-sensitive. Expanded Distribution earns $2–3 a copy at these prices. Turn it on only if library and bookstore reach matters more than margin.

**Alternative: 8.5 × 11 in.** This trim is also "large", so it costs the same per page, but it needs about 20% fewer pages because the masters are already laid out on Letter. Printing would be $9.93 / $11.34 / $10.88 / $10.57. At the same list prices the royalties would be **$11.07 / $12.66 / $13.12 / $13.42**. The cost is a bulkier, workbook-like book. 7 × 10 is the usual textbook trim and is easier to hold.

### Kindle ebook — 70% band

Delivery costs below use the master `.docx` size as the file-size estimate (5.2 / 6.7 / 6.8 / 8.0 MB). KDP shows the real figure after upload.

| Volume | List price | Est. delivery cost | Royalty per sale (70%) |
|---|---|---|---|
| 1 | **$9.99** | $0.78 | **$6.45** |
| 2 | **$12.99** | $1.00 | **$8.39** |
| 3 | **$12.99** | $1.02 | **$8.38** |
| 4 | **$12.99** | $1.20 | **$8.25** |
| Complete edition (all four, ebook only, ≈ 26.7 MB) | **$34.99** at 35% | none at 35% | **$12.25** |

- Volume 1 at $9.99 is the entry price. It is also the old 70% ceiling, and $12.99 is the new one. If Lothar would rather price every volume the same, V1 at $12.99 earns $8.55.
- At **$12.99 and 70%**, the complete edition would earn only $6.29, because about 26.7 MB costs about $4.00 to deliver. At **$34.99 and 35%** it earns $12.25 with no delivery cost. Bought separately, the four volumes cost $48.96, so $34.99 is about 29% off and still earns more per sale than any single volume.
- A paperback "set" can only be the four paperbacks linked on the series page. Set the KDP series field to *The Mathematics Tower*, with volume numbers 1–4.
- KDP Select / Kindle Unlimited is a separate decision. It requires 90-day ebook exclusivity, and its page reads would count heavily on 650-page books.

## 5. Categories (3 per volume, per format; same three for ebook and paperback)

Shelf names follow the current Amazon.com Mathematics browse tree (Applied, Chaos & Systems, Geometry & Topology, Mathematical Analysis, Matrices, Popular & Elementary, Pure Mathematics › Algebra / Calculus / Set Theory / Logic …, Reference, Study & Teaching, Trigonometry). Check each name in the KDP picker, because Amazon renames shelves.

| Volume | 1 | 2 | 3 |
|---|---|---|---|
| 1 Lower Floors | Science & Math › Mathematics › Pure Mathematics › Calculus (BISAC MAT005000 Calculus) | Science & Math › Mathematics › Popular & Elementary (BISAC MAT023000 Pre-Calculus) | Science & Math › Mathematics › Study & Teaching (BISAC MAT030000 Study & Teaching) |
| 2 Middle Floors | Science & Math › Mathematics › Matrices / Pure Mathematics › Algebra › Linear (BISAC MAT002050 Algebra / Linear) | Science & Math › Mathematics › Pure Mathematics › Calculus (BISAC MAT005000 Calculus — multivariable and vector calculus) | Science & Math › Mathematics › Mathematical Analysis (BISAC MAT034000 Mathematical Analysis — Fourier, Laplace, complex analysis) |
| 3 Upper Floors | Science & Math › Mathematics › Applied › Differential Equations (BISAC MAT007000 Differential Equations / General) | Science & Math › Mathematics › Geometry & Topology (BISAC MAT038000 Topology) | Science & Math › Mathematics › Pure Mathematics › Algebra › Abstract (BISAC MAT002010 Algebra / Abstract) |
| 4 Penthouse | Science & Math › Mathematics › Applied › Probability & Statistics (BISAC MAT029000 Probability & Statistics / General) | Science & Math › Mathematics › Chaos & Systems (BISAC SCI012000 Science / Chaotic Behavior in Systems) | Science & Math › Mathematics › Applied › Game Theory (BISAC MAT011000 Game Theory) |
| Complete edition (ebook) | Science & Math › Mathematics › Study & Teaching (MAT030000) | Science & Math › Mathematics › Pure Mathematics › Calculus (MAT005000) | Science & Math › Mathematics › Reference (MAT026000 Reference) |

The Kindle store has a parallel tree (Kindle eBooks › Science & Math › Mathematics › …). Pick the same shelves there.

## 6. Keywords (7 per volume, each under 50 characters, no title or subtitle words)

Words already in the titles, and therefore left out: *mathematics, tower, volume, floors, lower / middle / upper, penthouse, from, arithmetic, calculus (V1, V2), multivariable, set, theory (V2, V4), logic, differential, equations, abstract, algebra (V3), category, frontier.*

**Volume 1 — The Lower Floors**
1. algebra for adults self study (29)
2. precalculus workbook with solutions (35)
3. trigonometry and geometry for beginners (39)
4. learn math from scratch as an adult (35)
5. limits derivatives and integrals explained (42)
6. math refresher for college students (35)
7. high school math review with answer key (39)

**Volume 2 — The Middle Floors**
1. linear algebra self study with solutions (40)
2. vector analysis divergence curl and stokes (42)
3. fourier transform and fft for engineers (39)
4. laplace transform worked examples (33)
5. complex analysis for beginners (30)
6. eigenvalues and singular value decomposition (44)
7. partial derivatives and multiple integrals (42)

**Volume 3 — The Upper Floors**
1. ode and pde textbook for self study (35)
2. numerical methods for engineers (31)
3. topology and manifolds introduction (35)
4. measure theory and functional analysis (38)
5. group theory and galois theory primer (37)
6. calculus of variations and optimization (39)
7. tensor analysis for physics students (36)

**Volume 4 — The Penthouse**
1. probability and statistics self study (37)
2. information entropy and coding for beginners (44)
3. wavelets and signal processing (30)
4. game strategy and decision analysis (35)
5. control systems and feedback design (35)
6. chaos and nonlinear dynamics introduction (41)
7. math methods for physics and engineering (40)

**Complete edition (ebook)** — check these against its final title before use
1. undergraduate math curriculum self study (40)
2. math from counting to research level (36)
3. algebra calculus and linear algebra in one (42)
4. university math for adult learners (34)
5. math textbook with worked solutions (35)
6. engineering math reference (26)
7. learn higher math on your own (29)

These phrases are the subject names and "self study / for beginners / worked examples / with solutions" patterns that readers type into Amazon search. Check them in the Amazon search bar's autocomplete before entering them. Drop any phrase that autocomplete never suggests.

## 7. Decisions for Lothar

1. Trim: 7 × 10 (recommended) or 8.5 × 11 (cheaper to print, bulkier book). A print-layout docx (page numbers, mirror margins, gutter) has to be built either way. The current masters are Kindle files.
2. Prices: paperback $34.99 / $39.99 / $39.99 / $39.99; Kindle $9.99 / $12.99 / $12.99 / $12.99; complete ebook $34.99.
3. Whether to build the complete ebook edition now, from the current masters.
4. Expanded Distribution (on or off) and KDP Select (in or out).
5. Approve or replace the categories and keywords above.
