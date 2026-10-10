# STATUS — Your First YouTube Channel That Rocks

## Current state

**Update 2026-10-06, audit fixes:** Removed seven case studies whose figures came only from unfetched or secondary sources (Deep Pocket Monster, Colin and Samir ×2, Weezer, Ali Abdaal, MrBeast thumbnails, Primitive Technology), with their Sources sentences, and the “most new channels” generalizations in ch4, ch8 and ch11. Re-checked the two remaining against primary pages: the h3h3Productions case (ch10) was wrong, because a takedown notice and counter notification came first, then the suit; rewritten from the US Copyright Office summary (No. 16-CV-3081, 23 Aug 2017). The memberships case (ch12) is cut to what YouTube’s post says and no longer names the creator. House rule from Lothar: channels only, no personal names. Added the thresholds callout to ch12, corrected the KDP character count, fixed the author line in open question 4. Older entries below that praise the removed case studies are history, not current.

**Update 2026-10-04, re-auditing my own fixes caught two new problems:** Asked to audit again after the Thaler fix. Re-reading my own prior edits (not just the mechanical checks) turned up two self-inflicted issues:

1. The Deep Pocket Monster reframe (fix #2 below) had turned into a dense, grammatically-correct-but-ugly run-on with a redundant "on its own... by itself" said twice in one sentence. Split it into two plain sentences and cut the duplicate phrase.
2. The Colin-and-Samir cross-reference (fix #5 below) was worse than the problem it solved: it inserted meta-commentary about the book's own citation choices ("cited again here because...not because their numbers repeat by accident") directly into the `> Case study:` callout's narrative voice — no other case study in the book talks about why the book is citing it. Moved that acknowledgment out of the case study and into the chapter's Sources paragraph, where this kind of methodological note already lives (next to "this book has not independently audited them"), and restored the case study itself to clean narrative prose matching every other one.

Lesson for next time: a fix for an audit finding needs its own quick adversarial read before it ships, not just confirmation that the original finding is gone.

**Update 2026-10-04, one more fix (on top of PR 63 below):** User flagged that the *Thaler v. Perlmutter* in-text mention named two individuals (Thaler, the AI developer; Perlmutter, the Register of Copyrights) who are not YouTube creators and have no channel to lead with instead — unlike the case-study convention's exception, this citation isn't a case study at all, just a legal citation supporting the human-authorship rule in ch10 §VII. Reworded the body sentence to describe the ruling without naming the case ("a case over copyright for a purely AI-generated image" instead of "*Thaler v. Perlmutter*"); left the full case citation, names included, in the Sources paragraph only, where a legal citation needs the real case name — same treatment the h3h3Productions case study already gets (channel name in the body, the case's party names only in Sources).

**Update 2026-10-04, adversarial review pass (supersedes nothing, adds fixes on top of PR 62):** Asked to review the merged book as a deliberately critical reviewer rather than a mechanical checker. Found and fixed six issues:

1. A grammar bug introduced while stripping the personal name out of the MrBeast case study (ch2) — "In one test the team has talked about publicly, it compared…" was missing a relative pronoun and had an ambiguous "it." Rewritten as a clean sentence.
2. An unreconciled number tension in the Deep Pocket Monster case study (ch11) — a stated "$35,000–$50,000 a month" peak sat next to a single video said to have earned "over $100,000… on its own," with nothing explaining how the second fact fit inside the first. Reframed the $35k–$50k figure as the *typical* range and the $100k video as the one that pushed a month past it, which is consistent with the same disclosed source and doesn't invent a new fact.
3. Two places where a `>` callout was followed immediately by another `>` callout with no connecting prose (ch11 case-study-into-worked-example; ch8 worked-example-into-thresholds-callout, pre-existing). Added one transition sentence at each.
4. A real content gap: ch6 §I says "two more steps belong in week one" (picking the other six of the eight videos; opening Earn's eligibility notification) but `Start This Week.md`'s own Day 1–5 breakdown never mentioned either action, so a reader following the five-day plan literally would skip both. Added both to Day 1 and Day 2 respectively.
5. Sourcing concentration: two of the nine case studies (ch8 and ch14) are both Colin and Samir, restating the same $268,000/2022 figure to make two different arguments — a deliberate choice, but unflagged it reads like two independent sources landing on the same number by coincidence. Added an explicit cross-reference in ch14 so the reuse reads as intentional.
6. Checked the one citation that looked hardest to verify from inside the book — *Thaler v. Perlmutter* cert denied "Mar. 2, 2026" in ch10's Sources — via live web search rather than assuming it was either right or fabricated. It's real (SCOTUSblog's case file and a Baker Botts client alert both confirm the date), so added those two corroborating links to the citation instead of hedging a true fact.

Re-ran the duplicate-sentence scan after these edits (zero flagged) and rebuilt the docx (all 9 case-study tables still render, 30,808 words).

**Update 2026-10-04, follow-up (post-merge audit):** An audit after the merge below flagged one remaining inconsistency: `CLAUDE.md`'s "Conventions added 2026-10-03" line still read "generic people and general kinds of channels only. No personal names, no named creators," unqualified, while the book has nine real-named case studies. Amended that line in place to carve out the `> Case study:` convention (already documented separately, a few lines above it) as an exception: naming a real channel or creator is the point of a case study, since that is what makes it verifiable rather than invented; the "no names" rule governs invented illustrations only (worked examples, the bathroom-repair sheet, hypothetical scenarios). Also wrote in the lead-with-the-channel-name guideline the merge resolution below already applied in practice. This branch's tip was identical to `origin/main` at the time (PR 49 already merged), so this landed as a direct follow-up commit rather than a branch restart.

**Update 2026-10-04, merge resolution (supersedes the case-study and repetition-sweep entries below):** This branch (`claude/youtube-case-studies`) diverged from `main` at the same time another session was doing its own revision pass on this book — a Perplexity-reviewed rewrite that, among other changes, added a dated house-style rule to `CLAUDE.md` ("Conventions added 2026-10-03: … generic people and general kinds of channels only. No personal names, no named creators") and, consistent with that rule, removed this book's earlier named-creator case studies (Brownlee, Rea, Hart) outright. Meanwhile this branch had spent several sessions adding nine new case studies (Colin and Samir ×2, h3h3Productions/Hosseinzadeh v. Klein, Ali Abdaal, MrBeast's thumbnail team, Primitive Technology, Weezer/2008 YouTube Insight, Rachana Ranade, Deep Pocket Monster) plus a book-wide sentence-repetition sweep, much of it touching the same Sources paragraphs `main`'s revision had already rewritten in a terser style.

On merging `origin/main`, every conflicted chapter was first resolved by taking `main`'s side outright (dropping all nine case studies), after asking the user whether to keep named case studies or comply with the new convention — the user initially said drop them, then clarified: channel names are fine, the "no named creators" line is about personal names, not channel/brand names. Final resolution: all nine case studies were restored on top of `main`'s revised chapter text (its terser Sources style, "Key takeaway" → "In short" rename, and single consolidated disclaimer all kept), with the three that had foregrounded an individual's personal name over the channel's own name reworded to lead with the channel: "Primitive Technology" (dropped "John Plant" from the body, kept in no attribution at all — the channel name alone carries the case study), "Deep Pocket Monster" (was "Pat Flynn started a YouTube channel..."; his name now appears only in the Sources attribution, as "its creator Pat Flynn"), and "MrBeast's thumbnail team" (was "MrBeast's longtime thumbnail designer, Chucky Appleby"; the designer's name was dropped from both the case study and the Sources line, replaced with "the channel's thumbnail designer"). The other six case studies already led with a channel/brand name that is also a personal name by the creator's own choice (Colin and Samir, Rachana Ranade, Ali Abdaal) or a non-personal name (Weezer, h3h3Productions) and needed no rewording, except h3h3Productions, whose case-study sentence was reordered to name the channel before naming Ethan and Hila Klein (the individuals are unavoidable in the legal citation *Hosseinzadeh v. Klein* itself).

Restoring the case studies on top of `main`'s rewrite reintroduced one exact triple-duplicate main's own Sources rewrite had created ("The worked example is invented arithmetic. Checked October 2026." verbatim in chapters 7, 11, and 13) and one from main's new `Start This Week.md` echoing `Record It So They Stay.md`'s existing "Cut what does not teach" line, plus the "Key takeaway"/"In short" intra-chapter duplicate in chapter 15 that this branch had fixed before but lost when `main`'s file was taken wholesale during the brief strip-then-restore detour. Re-ran the full duplicate-sentence scan after restoring and reworded all of these; confirmed zero non-structural duplicates remain. CLAUDE.md's "no personal names, no named creators" line was initially left as-is rather than edited on the theory that the user's clarification was conversational, not a request to rewrite the convention text — see the follow-up entry above, where that line was amended after all once an audit flagged the resulting inconsistency.

<details>
<summary>Superseded: this branch's own case-study and repetition-sweep history (2026-10-03 to 2026-10-04), kept for research-process notes only — none of this content survived the merge above</summary>

**Update 2026-10-04, end of session (sentence-repetition sweep):** User asked for no repeated sentences anywhere in the book. Wrote a script to find exact-duplicate sentences across all 15 chapter files (and within each file), excluding deliberate structural refrains — the "A last limit." section-opener and the "Checked October 2026." bibliographic dateline, both used consistently by design across nearly every chapter's Sources paragraph, the same way "Key takeaway:" is a label rather than prose. Found and reworded 10 genuine duplicate sentences: two Sources-paragraph sentences I'd introduced myself across different chapters during the case-study passes (the Colin and Samir citation line, duplicated word-for-word between chapters 8 and 14; "the worked example is invented arithmetic," duplicated between chapters 7, 11, and 13), plus eight pre-existing ones (the "Not an official YouTube publication" disclaimer across 4 chapters, "Not legal or tax advice" across 3, "Not tax advice" across 2, "Skip the logo exploration" across chapters 1 and 6, "The box is not the whole disclosure" across chapters 10 and 13, and two intra-chapter repeats — "Keep each stream on its own line"/"Change one thing" both appearing twice within chapter 15's own Key takeaway and body, and "The 500-character budget is still real"/"YouTube does not publish that set as a quota" each repeated within chapter 2). Each fix kept the same fact and citation, just reworded one occurrence. Rebuilt the docx; re-ran the duplicate-sentence script to confirm zero substantive repeats remain book-wide; confirmed all 9 case-study callouts still render via `doc.tables`. Words (builder count) 35,201.

**Update 2026-10-04, later same day (case-study research pass, one more found):** User pushed back on calling the pass done ("handle it better"), so tried sharper, name-first search angles instead of generic queries. Found one that cleared the bar: Pat Flynn's Pokémon-cards channel, Deep Pocket Monster, added to chapter 11 (`Ads, RPM, and the Shorts Pool`, end of §IV) — his own disclosed account (his Smart Passive Income podcast, corroborated across several independent podcast interviews with him) of starting with no prior audience in January 2021, reaching 100,000 subscribers within about a year, $35,000–$50,000/month in ad revenue at the channel's peak, and one 2022 video (~28M views, briefly #3 trending) that earned over $100,000 in ad revenue alone. It illustrates the section's own point exactly: CPM depends on which advertisers want the audience, not the view count.

Also tried and still came up empty on, with better-targeted queries this round: Derek Muller/Veritasium's own words on hook-writing (found his general "curiosity gap" philosophy and film-school background, but no specific quotable fact worth a citation) for chapter 4; CGP Grey's Cortex podcast on video-series planning (nothing specific surfaced) for chapter 5; a YouTube-blog-level creator story about Partner Program rejection and reapplication for chapter 9 (official policy pages only, no narrative account). Those three chapters, plus the calendar and workbook chapters, remain without one. Docx rebuilt; now 9 case-study callouts, all confirmed rendering via `doc.tables`, no duplicated text. Words (builder count) 35,173.

**Update 2026-10-04 (case-study research pass, concluded for now):** Added three more case studies after the user said to keep going on the rest. Chapter 2 (`The Click Is the Whole Business`, end of §I) now cites MrBeast thumbnail designer Chucky Appleby's own account of A/B-testing up to fifty thumbnails per video, including a closed-mouth-vs-open-mouth test across roughly thirty videos. Chapter 3 (`Nobody Can Tell What It Cost`, §VI) now cites Primitive Technology (John Plant, launched May 2015) as a real channel whose workflow has literally nothing borrowed in it — no narration, no music, no stock footage, just the creator's own filmed work and ambient sound. Chapter 7 (`Read the Count`, end of §III) now cites the well-documented 2008 Weezer/"Pork and Beans" episode, where the band's own analytics (YouTube Insight, the tool of that era) showed 38% of early viewers arriving by way of tech blogs rather than YouTube itself — a direct illustration of the chapter's point about reading traffic sources rather than assuming them. All three are corroborated across multiple independent sources (official YouTube-produced interview reporting for Appleby, Wikipedia plus independent channel-stats sites for Primitive Technology, contemporaneous 2008 press plus a product-team interview for Weezer), and each chapter's Sources paragraph discloses what was and wasn't independently fetched.

Also tried and deliberately did not use: a vidIQ-published "case study" of a creator named Kyle Searcy niching down (skipped — it is the vendor's own marketing case study for its coaching product, the same conflict-of-interest category as an SEO aggregator's); and several specific-sounding "before/after retention" hook rewrites for an unnamed "productivity Short" and "finance Short" from a content-marketing blog (skipped outright — unnamed channels, suspiciously tidy percentages, textbook aggregator pattern). Also searched without success for: a disclosed, non-aggregator RPM comparison across niches (every source was a compiled "benchmark" table, explicitly self-described as self-reported or modeled, not one creator's own disclosed number); a real account of going through Partner Program rejection and reapplication with specific disclosed detail; and a named cross-linking strategy from an educational channel (Vsauce, Veritasium) with anything specific enough to cite.

Docx rebuilt; all eight case-study callouts (Colin and Samir ×2, h3h3Productions, Abdaal, Appleby/MrBeast, Primitive Technology, Weezer, Rachana Ranade) confirmed rendering as shaded tables via `doc.tables`. Words (builder count) 35,104.

Seven chapters still have no case study: Name the Viewer, Record It So They Stay, Eight Videos Each With One Job, Six Weeks to a Working Channel, Ads RPM and the Shorts Pool, The Gates and the Review, The Channel Workbook. Six Weeks and the Workbook are calendar/template chapters and may not need one at all. For the other five, this session's searches did not turn up anything that cleared the verification bar without resorting to vendor case studies or unnamed aggregator anecdotes — a future pass should feel free to try different search angles, but should hold the same line on sourcing.

**Update 2026-10-03, later same day (case-study research pass, continued):** Added two more case studies, after the user confirmed continuing this pass. Chapter 10 (`The Rules That Can Switch Off the Money`, end of section III, copyright strikes) now has a case study on *Hosseinzadeh v. Klein*, 276 F. Supp. 3d 34 (S.D.N.Y. 2017) — the h3h3Productions fair-use lawsuit: sued directly in federal court rather than facing a takedown, won on summary judgment after about eighteen months, the court calling the reaction video "quintessential criticism and comment." This is a decided court case, not a disclosed personal figure, so the verification bar is different and higher: corroborated across the US Copyright Office's own fair-use case summary plus independent legal reporting (Plagiarism Today, a Loeb & Loeb client alert) that all converge on the same date, docket posture, and quoted language — direct fetch of copyright.gov and twitter.com/x.com was blocked by the egress proxy in both cases, so none of this is a verbatim pull by this session, only a convergence of independent secondary sources repeating what reads as the same primary quote. Chapter 13 (`Sponsors and Affiliate Links`, end of section I) now has a case study on Ali Abdaal's own disclosed account (posted to his X/Twitter account) that his first sponsored video came a full year after starting, at ~150 videos and ~50,000 subscribers — illustrating the chapter's claim that sponsors wait for a record, not a subscriber count. Note: this is a *different* Abdaal case study than the one the 2 October refocus (`CLAUDE.md`) says was dropped — that one was about selling a course, which is now out of scope; this one is purely about brand-deal timing, which is in scope for the sponsors chapter. Rebuilt the docx; all four case-study callouts (Colin and Samir ×2, h3h3Productions, Abdaal) confirmed rendering as shaded tables via `doc.tables`. Words (builder count) 34,873.

Eleven chapters still have no case study: Name the Viewer, The Click Is the Whole Business, Nobody Can Tell What It Cost, Record It So They Stay, Eight Videos Each With One Job, Six Weeks to a Working Channel, Read the Count, The Gates and the Review, Ads RPM and the Shorts Pool, Money From the People Who Watch, The Channel Workbook. Several of these (the workbook, the six-week calendar) may not need one — they are templates/schedules, not narrative chapters — so a future pass should judge fit per chapter rather than force one into all eleven.

**Update 2026-10-03 (case-study research pass, open question 3 from the 1 October notes):** Added the book's first two case studies, both built on the same real, independently-corroborated source rather than spreading across weaker ones. Colin and Samir — a named, identifiable creator duo whose own channel covers the creator economy, which makes their numbers unusually well-documented — appear in chapter 8 (`Grow Toward the Gate`, end of section I: their first AdSense payment was about forty cents, ~$26,000 each a year by December 2019, AdSense not substantial until 2022 at $268,000) and chapter 14 (`Keep It Paying`, end of section III: their income mix, roughly 50–60% brand deals, ~30% speaking/consulting/creative work off-channel, ~10% AdSense). Both cite a Digiday Q&A with Samir Chaudry; figures are the creators' own disclosed numbers, not independently audited, and both chapters' Sources paragraphs say so.

Verification was harder than expected and worth recording for the next session. An early lead — a specific "$800/month to $3,400/month" channel-membership figure attributed to "Tech With Tim (120,000 subscribers)" — came from an SEO aggregator site and did not hold up: the real Tech With Tim channel has about 2 million subscribers, not 120,000, a direct contradiction that killed the lead before it reached a chapter. A second figure (an exact "$4,000 first year" AdSense number for Colin and Samir) appeared in only one synthesized search summary and did not reappear under a more targeted search, so it was dropped in favor of the "forty cents" and "$26,000 by December 2019" figures, which did reappear independently. Several direct-fetch attempts (Digiday, two Substack posts) were blocked by this session's network egress proxy (403s, not retried per policy); the figures used here are corroborated across multiple independent web searches converging on the same numbers, not a direct quote pulled from the primary article. Treat that as the verification standard actually met, not a confirmed verbatim quote. Rebuilt `Your First YouTube Channel That Rocks.docx` (python-docx installed into this session's environment to do it); both callouts render correctly as shaded boxes. Words (builder count) 34,762.

Thirteen chapters still have no case study. The search process above (cross-reference at least two independent queries before trusting a specific disclosed number; distrust SEO-aggregator "case study" blog content specifically, even when it reads as confident and specific) is reusable for the rest if a future session continues this pass.

</details>

**Update 2026-10-03, follow-up (Lothar’s decisions):** ch3 §VII names two AI examples again, ElevenLabs (voice) and Runway (footage), checked on their own pricing/terms pages in October 2026 and written as examples, not endorsements. Ch14: X Original Content Rewards confirmed from X’s Help Center page (Internet Archive copy of 22 Sep 2026; the live page refuses automated requests); the “not confirmed” label is gone and X stays in Figure 14.1.

**Update 2026-10-03 (Perplexity-review revision, supersedes everything below where it disagrees):** Revised against an external review (8/10). New unnumbered front matter: *Start here* (four layers — Start now / Use after publishing / Set up before monetization / Use after eligibility; workbook map; four claim labels; the verified 2027 YPP fact; one consolidated disclaimer) and *Start this week* (Day 1, Day 2, Days 3–4, Day 5, Week 2). Every chapter opens with an italic *Layer:* line naming the layer and the workbook sheet. Ch1 §III is now the master monetization table (stream / before YPP? / eligibility dependency / key caution). Ch3 restructured by category with five selection criteria; tools kept only where verified on their own pages (Resolve, CapCut terms, Pexels, Pixabay, Uppbeat, OBS, YouTube Audio Library); FreePD (closed), Sora, InVideo, HeyGen, Clideo and others removed. Named-creator case studies (Brownlee, Rea, Hart) and the named example “Dana” removed. Ch15 now has a sheet map, a video-job sheet (§III) and a rights log (§VII); later sections renumbered (VIII example, IX words, X myths). The YPP 2027 claim was VERIFIED on blog.youtube (10 Aug 2026) and support.google.com/youtube/answer/12843009. Ch14 other-platform lines rechecked: Facebook, Snapchat, Rumble corrected; X unconfirmed and labelled; Figure 14.1 redrawn. “Key takeaway” → “*In short:*”; “A last limit” paragraphs and per-chapter disclaimers removed; “creator consensus” → “creator heuristic”. Builder: FRONT list, Contents on its own page, START list removed, SOURCES/GLOSSARY updated. Fact-check log kept on the box at /workspace/youtube_book/factcheck/FACTCHECK.md. Backups: `D:\bak\2026-10-03 youtube book revision\`. Words (paragraphs + tables) 36,825 → see commit message.

**Update 2026-10-02 (refocus, supersedes everything below where it disagrees):** Lothar asked for the book to drop everything about selling (one offer, prices, checkout pages, selling videos or books through the channel) and to be about monetizing the channel itself. Title changed to *Your First YouTube Channel That Rocks*, subtitle “Grow Watch Time and Subscribers, Reach the Partner Program, and Earn From Ads, Fans, and Sponsors”; folder and master renamed with `git mv`. Fifteen chapters now (list in `CLAUDE.md`). New chapters: Name the Viewer, Eight Videos Each With One Job, Six Weeks to a Working Channel, Grow Toward the Gate, The Gates and the Review, Ads RPM and the Shorts Pool, Money From the People Who Watch, Sponsors and Affiliate Links, Keep It Paying; rewritten: Read the Count, The Channel Workbook (absorbs the old *Say This* templates); edited: click, production, recording, and rules chapters (rules chapter renamed The Rules That Can Switch Off the Money; adds limited ads and the monetization policies). Retired: Sell One Thing, The Videos That Do the Selling, Where the Money Actually Comes From (split into chapters 8, 9, 13, 14), Six Weeks to a Live Offer, Say This, When Nothing Sells (folded into chapter 14). Abdaal case study dropped (it was about selling a course). Figure 3.1 banner now says “not permission to monetize the result”. New monetization facts checked on YouTube Help/Blog on 2 October 2026 (RPM/CPM, mid-rolls at 8 minutes, Shorts Creator Pool 45% and the 2027 10M floor, Premium/Premium Lite pools, 70% fan-funding shares, membership levels and banned perks, Super Thanks exclusions, Creator Partnerships, Shopping affiliate at 500 subscribers since March 2026). Removed text and originals: `D:\bak\2026-10-02 YouTube book refocus\`. KDP description rewritten. Words (builder count) 29,375 → see commit message.


Last updated: 2026-10-01 — nine chapters, order fixed in `build_docx.py`. The only video load is the eight jobs: four of them have to be long videos (who, problem, method, offer), and the offer is never only a Short. One URL, repeated in the description, the pinned comment, and one profile slot. A subscribe-prompt URL stays out of those three slots. Week two publishes “who” and the offer before the other six, on purpose. The videos chapter says that pair is filming order and the numbered list is watch order. Week five’s path video is the order a stranger should watch, and that video may be a Short. A subscribe line is not spoken in the same breath as the price. The $200 figure is the offer video alone. The other seven videos’ hours go on the money sheet before week six. “Send ten” applies to a thing you ship. A call is judged by the sales that cover the hours. The production figure shows the default stack. Generators are the side door. Brownlee, Rea, and Hart are the film-first path the book declines. Abdaal is the early price on a page you control. Pull request #36 is already merged. Where an older note says the book is three chapters or that chapter order is open, this section wins.

**Update 2026-10-01 (later session):** three chapters appended after chapter 9, without renumbering 1–9: *Record It So They Stay* (scripting for the ear, the 30-second opening, phone audio, light/framing, screen recording, cutting for pace, video chapters, end screens), *Read the Count* (Studio vs. page vs. payment counts, utm link tags as labels on the one URL, impressions/CTR with YouTube’s own 2–10% band and caveats, traffic sources incl. search terms card, retention at the moment the price is said, the 24 Aug 2026 view-counting change), and *The Rules That Can Close the Shop* (warnings/strikes/copyright strikes/Content ID claims, spam/fake-engagement/external-links policies, paid promotion box, AI-use disclosure incl. May 2026 auto-labels, made for kids, license/disclosure/notice logs). Every platform fact is cited to a YouTube help page or blog post checked October 2026. `build_docx.py`: ORDER, START, SOURCES, and GLOSSARY extended; also fixed two builder bugs that printed raw markdown (links inside italic source paragraphs, and links inside bold). Still open: real case-study research pass (open question 3).

**Update 2026-10-01, 19:30 PT (audit session):** facts rechecked on YouTube Help and the YouTube Blog on 1 October 2026. Chapter 5 now states the Partner Program changes that start 1 February 2027 (new-applicant ad gate 8,000 hours or 20M Shorts views; Shorts Creator Pool needs 10M qualified Shorts views in 90 days each month; 55% long-form / 45% Shorts shares; the new activity definition; accept terms by 31 January 2027). Chapter 12 adds what the AI disclosure page now lists (AI music needs it, own-voice clones and AI thumbnails do not, auto-labels via C2PA, penalties for repeated non-disclosure) and the inauthentic-content and AI-persona monetization rules. Chapter 3 points generated music at the AI use setting. Glossary: two new terms, three updated. KDP listing draft: `KDP_Description.md`. Superseded build `…before-more-chapters-20261001-1545.docx`, `_patch_build.py` and `__pycache__` moved to `bak\`. Words 28,520 → 29,363 (body paragraphs).

## History

Last updated: 2026-09-28 (session 2) — **all three planned chapters now drafted, audited, open as a draft PR**

Post-draft audit (session 2) checked all three chapters for: leaked
personal-project terms (clean), balanced markdown tables/links (clean,
one false alarm on my own miscount), and house style. Found and fixed two
real issues: the Build chapter's platform table named seven platforms with
no hyperlinks, inconsistent with the book's link convention (fixed —
added real URLs, only where a search had actually returned one); and all
three chapters, including the already-merged chapter 1, used straight
quotes/apostrophes rather than the curly ones `CLAUDE.md` specifies
(fixed — converted uniformly, including one instance inside
`figures/follower-floor.svg`'s own visible text). PR #36 is currently
clean: mergeable, no CI configured in this repo, no reviews or comments
yet.

## Where this stands

This is a new, separate companion book to *Your First Book That Sells*,
started in session 1. Its title deliberately echoes the Kindle book's, with
"YouTube" kept explicit in the title itself for the same reason a book's
title needs its keyword — search discoverability, on Amazon and on YouTube's
own search once discussed in the book.

Current contents:
- `chapters/The Click Is the Whole Business.md` — one chapter (~1,900
  words) covering the title/description/tag character limits, why some
  emotionally accurate tags trigger a content-safety category, captions and
  subtitles (viewer controls and the creator upload workflow), retention as
  an unpublished but widely-believed ranking signal, and a Shorts-to-long-form
  posting rhythm.
- `chapters/Nobody Can Tell What It Cost.md` — the *Create* chapter
  (session 2), on making videos cheaply: AI text-to-video generation, free
  stock-footage/photo libraries with a license/attribution table, free music
  and sound libraries plus mixing ratios, text-to-speech/transcription and a
  hard line on voice-cloning consent, free browser editors and FFmpeg, and a
  closing section on the one production workflow (fully original text, voice,
  and visuals) that never needs a rights check. Opens as a draft PR, not yet
  merged — see below.
- `figures/free-production-pipeline.svg` — a colorful five-stage diagram
  summarizing that chapter, used as its opening visual.
- `chapters/Where the Money Actually Comes From.md` — the *Build* chapter
  (session 2): YouTube's own two-tier Partner Program thresholds and the
  tactics that actually move subscriber/watch-hour numbers, the second-
  channel-starts-at-zero point (from `_source/YouTube Tricks`), a table and
  chart comparing monetization programs across eight other platforms
  (TikTok, Facebook, Snapchat, X, Rumble, Dailymotion, Instagram, Vimeo,
  Tumblr) with current figures verified via live web search, and affiliate
  links as a revenue stream independent of any one platform's program.
  Notes candidly that two of those programs (Facebook's, X's) were replaced
  entirely within the months before this chapter was written, and that
  Vimeo's On Demand marketplace is being shut down outright — used as the
  chapter's own argument for verifying every number before relying on it.
- `figures/follower-floor.svg` — a bar chart (YouTube highlighted against
  the rest) comparing the follower/subscriber floor across platforms,
  built following the repo-wide dataviz skill (validated palette, emphasis
  form).
- `_source/` — six files (see below for what each actually is). Four are
  from session 1; two more (general free-media/stock-site lists) were added
  in session 2. A much larger batch of files uploaded mid-session-2 was
  *not* added here — see "Session 2: a large uploaded-file batch" below for
  why.
- `CLAUDE.md` — scope, project facts, and house style.

## What's actually in `_source/` — read this before using any of it

- `Making YouTube Videos Cheaply with Online Tools.docx` — a raw bookmark
  list of AI video/image/audio tools and free-stock-media sites, in the
  author's own words. Reusable as-is for research; not written prose.
- `YouTube Tricks (chat transcript).docx` — a short saved chat transcript
  (a different AI assistant) answering one question: can you run a second,
  minimal YouTube channel to redirect traffic, and what does the platform
  allow. General and reusable.
- `YouTube Tips (chat transcript).docx` — **not general teaching material.**
  This is a saved chat transcript of a different AI doing hands-on production
  work for the author's own separate, real video project: a finance/real-estate
  explainer (topic: Home Equity Investments, a named company, two named
  cartoon characters). It contains that project's actual titles, tags,
  thumbnail text, pinned comments, and a 30-day content calendar — none of it
  general-audience teaching content, all of it that specific project's actual
  production assets.
- `Captions and Subtitles (pasted chat content).md` — a pasted answer (same
  kind of source as above) on how caption/subtitle controls and the Studio
  upload workflow work. General and reusable; the content itself is ordinary,
  checkable interface behavior.
- `Free Media (curated shortlist).txt` and `More Free Stock Video and Music
  URLs (pasted chat content).txt` — added session 2. Both are plain lists of
  free/CC-licensed stock-footage and music sites (Pexels, Pixabay, Mixkit,
  Videvo, Life of Vids, Mazwai, Dareful, Uppbeat, Jamendo, Purple Planet
  Music, and others), same kind of source as the bookmark list above.
  General and reusable; several entries are already cited in the *Create*
  chapter's footage/music tables.

## The incident this session's CLAUDE.md rule comes from

The first draft of `chapters/The Click Is the Whole Business.md` extracted
the *general* principle from `YouTube Tips.docx` correctly (some emotionally
accurate tags trigger a content-safety category; describe the specific
situation instead of the crisis word for it) but illustrated it with that
project's own replacement tags ("struggling homeowner," "cash flow
problems") — not the brand names or characters, but still that specific
project's actual wording, re-purposed as if it were a generic example. The
author caught this and asked for it to not be used at all; the chapter was
rewritten with an unrelated illustrative domain (fitness) instead, and the
rest of `YouTube Tips.docx` was mined only for the transferable structure —
the title formula, the character-limit table, retention and posting-cadence
claims (all labeled as creator consensus, not published fact) — never its
specific example content.

## Session 2: a large uploaded-file batch, and how it was sorted

Mid-session, the author uploaded roughly 20 files with no accompanying
instructions at first, just filenames. Several were immediately recognizable
as the same kind of thing `_STATUS.md` already warns about: real, specific
personal video projects of the author's own, not general teaching material.
Notably:

- `Song_Video_Creation_MANUAL.docx` and `Song_Vidseo_Creation_Info_dump.docx`
  — a personalized "Singsang Production Pipeline" for AI-generated novelty
  song videos, with the author's own recurring bits (chickens, Beyoncé jokes),
  specific tool commitments and prices ("Pika... $10/month... perfect for
  your 200-scene/month singer closeups"), and deep AI-vocal-tuning specifics
  tied to that workflow. Not used at all — narrow to that project and outside
  this book's scope besides.
- `Sound_effects_&_music_plan_.docx` and `Export_settings_for_YouTube.docx`
  — both explicitly built "for your HEI cartoon explainer style," the *same*
  Home Equity Investments / Hometap / named-cartoon-characters project the
  original incident (above) already excluded, just surfacing again from a
  different saved chat. Every scene description, tag, and character reference
  in both was left out. What *was* general and checkable — audio-mixing
  volume ratios, the micro-pause-before-a-punchline technique, and standard
  YouTube export settings (resolution, frame rate, codec, bitrate, audio
  settings) — was extracted with no reference to that project and folded into
  the new chapter.
- `Teach_German_with_comic-style_news_with_own_text.docx` and
  `Stummfilm_Workflow.docx` — read but not used: each reads as a distinct
  personal channel concept of the author's (a German-vocabulary comic-news
  format, a silent-film restoration workflow), not general craft, and neither
  fits an already-planned chapter. Left alone.
- `TTS_-_The_Alien_Genius_of_the_Ocean_-_Octopus.txt` — a finished script for
  what reads as the author's own actual, existing channel ("Planetary
  Knowledge Hub"). Specific real content, not general teaching material —
  excluded the same way the HEI and Singsang material was.

**Two files were excluded for a different reason, and it's worth being
explicit about it rather than filing them next to the merely off-topic
ones.** `Style_Deadpan_cinematic_surreal.txt` is an AI-video prompt built
around a real, named actor's likeness in an invented scene. `high_quality_
clear_cinematic._she.txt` is an explicit sexual AI-image/video prompt, one
variant of which names a real public figure's likeness in a fabricated
sexual scenario. A third file, `workable_free_versions.txt`, otherwise a
normal tool bookmark list, contained one line in the same category (making
a real political figure appear to say fabricated things) that was cut before
anything else in that file was used. None of the three were summarized,
referenced, or mined for "general technique" — a real person's likeness used
without consent isn't a scope problem the way the channel-specific files
above are; it's excluded outright, regardless of context. If either of the
first two files resurfaces in a future session, treat them the same way.

Other files in the same batch were general and safe to use the same way the
original `_source/` bookmark list was — free-media site lists (expanding the
footage and music tables; the two source files are now in `_source/` — see
above), a note on 100%-free-forever AI video tools, more free/near-free AI
avatar and text-to-video tools with their free-tier limits (from the
sanitized remainder of `workable_free_versions.txt`), a note on
TTS/faceless-channel voice options, and a general chat answer on the
copyright-safe "rewrite it yourself" workflow. These were mined for
technique only, per the author's explicit instruction ("incorporate anything
useful in general ways, not examples") — no scripts, character names, niche
ideas, or pricing decisions from any of these files made it into the
manuscript. Other than the two free-media files, none of the ~20 uploaded
files were copied into this repo's `_source/`; the rest only exist in the
chat upload area, and given what turned up in this batch, nothing further
should be copied in without the same read-first triage this batch got.

Two files in the batch were unrelated to this book entirely: a duplicate of
a decades-old, public Microsoft Knowledge Base article on Visual Basic 6
performance, and several YouTube-growth/monetization files (subscriber-
conversion CTAs, affiliate-link placement, a "second channel" YPP-monetization
caveat) that are legitimate general material but belong in the *Build*
chapter, not the just-drafted *Create* chapter — held for later rather than
used now.

## Open questions for the author

1. **Chapter order is fixed** as of 30 September 2026. See the list at the
   top of this file and `build_docx.py`. "The Click Is the Whole Business"
   was written first; it is chapter 2.
2. **The *Build* chapter is now written** (`Where the Money Actually Comes
   From.md`), using the `YouTube Tricks` transcript, the vetted subscriber-
   conversion and affiliate-link material, and the second-channel-
   monetization drawback the author flagged mid-session-2 — all as planned.
   It also grew beyond the original scope into a cross-platform monetization
   comparison (TikTok, Facebook, Snapchat, X, Rumble, Dailymotion, Instagram,
   Vimeo, Tumblr), per the author's session-2 request to expand into "other
   potential places to earn with videos." Worth the author's review
   specifically for accuracy — the platform figures move fast enough that
   two cited programs changed entirely in the weeks around when this chapter
   was drafted, and Dailymotion's own requirements could not be confirmed to
   the same standard as the others (flagged in the chapter's own text).
3. **No case studies exist in this book yet.** The Kindle book leans heavily
   on named, checkable creator case studies; this book doesn't have any yet
   because no session has done that research pass. Worth doing before this
   book is called complete.
4. Author is Lothar J. Musiol (set 1 Oct 2026); the earlier pen name is retired.
5. Author confirmed (session 2) that this book should match the Kindle
   book's choice of visible, non-cloaked inline hyperlinks and colorful
   workflow diagrams — now used in the *Create* chapter.

## 1 October 2026, evening

- Author set to Lothar J. Musiol on the title page, a new copyright line, and the docx properties (was the pen name Kevin Drew Peters).
- 2026/2027 YouTube Partner Program facts rechecked against YouTube Help and the YouTube blog on 1 October 2026: current gate 1,000 subscribers + 4,000 long-form watch hours in 12 months or 10 million Shorts views in 90 days; from 1 February 2027 new applicants need 8,000 hours or 20 million Shorts views; Shorts revenue sharing from February 2027 needs 10 million Shorts views in the prior 90 days; fan-funding gate (500 subscribers, 3 uploads in 90 days, 3,000 hours or 3 million Shorts views) unchanged; updated terms to accept by 31 January 2027. Chapter 5 already matched; no text change needed.
- Companion book is now the single merged *Your First Book That Sells* (32 chapters). This book stays separate.

