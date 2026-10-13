# Series Cover and KDP Draft Audit

**Audit date:** 13 October 2026  
**Scope:** Current cover JPEGs in `covers/`, cover-generation source, and nine `notes/KDP_Book*.md` listing drafts.

## Findings

- All nine books have a front and back cover JPEG. Each asset is 1600 × 2560 pixels; the covers use a consistent navy, gold, and technical-line-art series design.
- A contact sheet of all 18 covers was visually reviewed. Front-cover titles and book numbers are consistent across the series. Back covers contain a reserved white barcode area. This is a visual draft review, not approval of final print wraps or marketplace thumbnails.
- All nine KDP description drafts include a reader-level statement. The description sections were initially estimated at 1,856 to 3,579 characters; a current source-based recount including HTML tags is recorded below. Per the existing drafts: Books 1 and 8 recommend ages 16+, Book 2 17+, and Books 3–7 and 9 18+; these are suitability recommendations, not formal age restrictions.
- The cover files and descriptions remain drafts. No image or copy change was justified by this pass. Recheck all claims, counts, title metadata, and cover assets against frozen release editions and KDP’s current upload requirements before publication.

## Evidence and Limits

The cover contact sheet was generated in the system temporary directory for inspection; it is not a release asset. The covers were reviewed together for series consistency, not individually at full-size print resolution. This audit does not confirm KDP category availability, metadata acceptance, print-wrap dimensions, barcode placement, or final Kindle thumbnail appearance.


## Initial KDP description validation (13 Oct 2026; later refresh below)

At the time of this first recount, the HTML description source in all nine `notes/KDP_Book*.md` files, including tags, was below KDP's 4,000-character limit. The current lengths after the reader-age revisions are listed below. Parsed each description and confirmed balanced tags; the tags used (`p`, `b`, `i`, `ul`, `li`) are supported by KDP's current [book-description guidance](https://kdp.amazon.com/en_US/help/topic/G201189630?lang=en). A UTF-8 scan found no replacement characters or common mojibake sequences. This is a local source check; the descriptions have not been entered into or approved by KDP.


Current-manuscript count reconciliation (13 Oct 2026): compared the nine KDP draft claims with current DOCX chapter headings and extracted mirror counts. Chapter counts match: 38, 28, 28, 52, 25, 22, 29, 26, and 38. Figure counts match the listing claims: Books 1-9 contain 56, 59, 33, 54, 34, 27, 35, 54, and 50 embedded images respectively; Book 1's count includes one reader-lab figure in front matter plus 55 chapter figures. Where listings state worked-example counts, the mirrors show 74 for Book 1 (supporting 'more than 70'), 109 for Book 2, 72 for Book 8, and 111 for Book 9. The all-nine answer-coverage audit confirms listed problem totals 156, 215, 319, 256, 208, and 234 for Books 1, 2, 4, 5, 8, and 9. Book 8 has 84 distinct numbered listing captions and 87 source files. No count correction was needed. Counts confirm source alignment only; they do not establish the marketing copy's qualitative claims or final live KDP acceptance.

## Reader-age guidance revision (13 October 2026)

Revised all nine description reader-level paragraphs to present ages as recommendations rather than hard cutoffs and state the preparation that actually predicts fit. The current recommendations are Book 1: 16+ (algebra/trigonometry); Book 2: 17+ (those foundations plus Book 1 circuit analysis); Book 3: 18+ (circuit analysis, complex numbers, introductory calculus); Books 4 and 5: 18+ (phasors/complex numbers, with probability and basic signals for Book 5); Books 6 and 7: 18+ (circuit/feedback or electronics/circuit/measurement experience); Book 8: 16+ (basic electronics and programming, with adult supervision for younger readers' selected projects); Book 9: 18+ (basic circuit knowledge and properly supervised lab practice). Books 6 and 9 now say age is not a safety qualification.

Revalidated the description HTML: allowed tags balance, no disallowed tags were found, and all descriptions remain below 4,000 characters including markup. Current lengths are 2,768; 3,127; 2,997; 3,475; 2,877; 1,787; 1,719; 2,273; and 2,280 characters for Books 1-9. These are editorial suitability recommendations, not formal age restrictions or a substitute for prerequisite knowledge and safe practice.


Final KDP HTML/age check (13 Oct 2026): re-parsed all nine current Description sections. Every draft contains its reader-level statement, uses balanced allowed tags only, and remains below 4,000 characters (2,767; 3,126; 2,996; 3,474; 2,876; 1,786; 1,718; 2,272; 2,279). This verifies local draft structure and length, not live KDP acceptance or listing suitability.


## Book 6 design-scope wording follow-up (13 October 2026)

A buyer-facing read found that "build linear regulators ... converters" could imply a sequence of hands-on construction projects. Book 6 presents design calculations and worked analysis across the converter families, with high-voltage and pulsed-power validation explicitly bounded; it is not framed as a set of step-by-step hardware builds. Changed the KDP draft to say "design and analyze" while retaining its component-selection and topic coverage. The updated description is 1,802 characters including markup, remains below the 4,000-character limit, and the edit leaves its age/prerequisite paragraph intact. This is a purchase-expectation clarification; live KDP approval, final marketplace rendering, and the listed independent/hardware gates remain open. No readiness score is raised.
