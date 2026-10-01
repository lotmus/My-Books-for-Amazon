// Converts the manuscript's markdown Part-files into a real .docx,
// with true italic/superscript/subscript math formatting instead of
// markdown text approximations.
//
// Reconstructed 2026-09-12: the original build lived in a session scratchpad
// that got garbage-collected after a multi-week gap. This version was
// rebuilt by reverse-engineering the exact OOXML of the last known-good
// delivered .docx (fonts, sizes, spacing, keepNext chaining, hyperlink
// styling, etc. were all read back out of word/document.xml rather than
// guessed from memory), so the output should be byte-for-byte equivalent
// in every visible respect. It now lives here, next to the manuscript
// files it builds, instead of in an ephemeral scratchpad.
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  Header, Footer, PageNumber, VerticalAlignSection, ImageRun,
  PositionalTab, PositionalTabAlignment, PositionalTabLeader, PositionalTabRelativeTo,
  Bookmark, InternalHyperlink, ExternalHyperlink,
} = require("docx");

// Straight ' and " -> typographic curly quotes, by local context. Applied to
// every raw line (and to TOC_ENTRIES titles, below) before any other markdown
// parsing touches it, so downstream code never has to know straight quotes
// existed. "Opening" is triggered by start-of-string or a preceding
// whitespace/opening-bracket/dash/other-opening-quote character; everything
// else -- including every contraction and possessive apostrophe -- closes.
function smartenQuotes(text) {
  let out = "";
  for (let i = 0; i < text.length; i++) {
    const ch = text[i];
    if (ch !== "'" && ch !== '"') { out += ch; continue; }
    const prev = i > 0 ? text[i - 1] : "";
    const isOpen = prev === "" || /[\s([{\-—“‘]/.test(prev);
    if (ch === '"') out += isOpen ? "“" : "”";
    else out += isOpen ? "‘" : "’";
  }
  return out;
}

// The TOC's page numbers are filled in from toc_pages.json, produced by a
// separate Word-COM lookup pass after a first generation (see
// resolve_toc_pages.ps1). Entries print in this exact order; "front"/"back"
// and "part" render bold, "chapter" renders indented under the part
// immediately above it.
const TOC_ENTRIES = [
  { type: "front", title: "Prologue: A Different Way of Thinking" },
  { type: "front", title: "What's Mead, What's Feynman, What's New Here" },
  { type: "part", title: "PART ONE — Phase, Not Force" },
  { type: "chapter", title: "1. The Invisible Interaction" },
  { type: "chapter", title: "2. The Phase of a Charged Particle" },
  { type: "chapter", title: "3. The Loop" },
  { type: "chapter", title: "4. Not Just Bookkeeping" },
  { type: "part", title: "PART TWO — When Many Become One" },
  { type: "chapter", title: "5. One Electron Is Not a Superconductor" },
  { type: "chapter", title: "6. Coherence Changes the Rules" },
  { type: "chapter", title: "7. Momentum in the Presence of a Potential" },
  { type: "chapter", title: "8. Where Does the Potential Come From?" },
  { type: "part", title: "PART THREE — The Photon and the Path" },
  { type: "chapter", title: "9. The Photon" },
  { type: "chapter", title: "10. The Path Is Not a Track" },
  { type: "chapter", title: "11. From Individual Histories to Collective Phase" },
  { type: "part", title: "PART FOUR — Finding Maxwell Again" },
  { type: "chapter", title: "12. Where Did the Fields Go?" },
  { type: "chapter", title: "13. Maxwell Appears" },
  { type: "chapter", title: "14. The Classical World Is a Limit, Not a Different Universe" },
  { type: "part", title: "PART FIVE — The Field That May Not Be a Thing" },
  { type: "chapter", title: "15. What If the Field Isn't Independent?" },
  { type: "chapter", title: "16. Wheeler and Feynman: The Universe Talks Back" },
  { type: "chapter", title: "17. A Field or a Relationship?" },
  { type: "chapter", title: "18. Radiation Is Where Things Get Serious" },
  { type: "chapter", title: "19. Where Is the Energy?" },
  { type: "part", title: "PART SIX — What Survives the Merger" },
  { type: "chapter", title: "20. What QED Adds" },
  { type: "chapter", title: "21. The Geometry of the Potential" },
  { type: "chapter", title: "22. The Art of Forgetting" },
  { type: "chapter", title: "23. The Meaning of \"Fundamental\"" },
  { type: "part", title: "PART SEVEN — Geometry, Symmetry, Vacuum" },
  { type: "chapter", title: "24. Charge Is the Price of Changing Phase Locally" },
  { type: "chapter", title: "25. Why the Classical Path Wins" },
  { type: "chapter", title: "26. Magnetism, Light, and Empty Space" },
  { type: "chapter", title: "27. The Phase Can Wind" },
  { type: "part", title: "PART EIGHT — Following an Electron" },
  { type: "chapter", title: "28. The Equation Behind the Conversation" },
  { type: "chapter", title: "29. Feynman's Diagrams Become Less Mysterious" },
  { type: "chapter", title: "30. The Classical Coulomb Force Emerges" },
  { type: "chapter", title: "31. Now Add Many Electrons" },
  { type: "chapter", title: "32. The Book's Central Bridge" },
  { type: "part", title: "PART NINE — Light Meets Matter" },
  { type: "chapter", title: "33. The Photon Is Not the Opposite of the Phase" },
  { type: "chapter", title: "34. When Matter Meets Light" },
  { type: "chapter", title: "35. The Loop, Formalized" },
  { type: "part", title: "PART TEN — Renormalization, Done Once, Done Right" },
  { type: "chapter", title: "36. Vacuum Polarization: The Electron Is Not Quite Alone" },
  { type: "chapter", title: "37. The Terrible Reputation of Renormalization" },
  { type: "chapter", title: "38. A Resolution Dial" },
  { type: "chapter", title: "39. Renormalization Is a Translation System" },
  { type: "part", title: "PART ELEVEN — The World at the End of the Wire" },
  { type: "chapter", title: "40. From QED to a Superconducting Circuit" },
  { type: "chapter", title: "41. One System, Several Descriptions" },
  { type: "chapter", title: "42. The Same Wire Contains All Four Worlds" },
  { type: "part", title: "PART TWELVE — What the Electron Knows" },
  { type: "chapter", title: "43. A Tiny Charge With a Huge Story" },
  { type: "chapter", title: "44. The Electron in a Superconductor" },
  { type: "chapter", title: "45. Is the Field Real?" },
  { type: "part", title: "PART THIRTEEN — The Honest Ending" },
  { type: "chapter", title: "46. The Ladder of Descriptions: Electron to Eye" },
  { type: "chapter", title: "47. What We Have Learned, and What We Have Not Proven" },
  { type: "chapter", title: "48. Epilogue: The Law Becomes Visible" },
  { type: "back", title: "Appendix A: Equations at a Glance" },
  { type: "back", title: "Appendix B: Notes on Sources" },
  { type: "back", title: "Appendix C: Glossary" },
  { type: "back", title: "Appendix D: Index of Chapters" },
  { type: "back", title: "Appendix E: Symbols, Numbers, and Distinctions" },
  { type: "back", title: "If This Book Worked for You" },
  { type: "back", title: "Also by Lothar J. Musiol" },
  { type: "back", title: "About the Author" },
  { type: "back", title: "A Small Request" },
];

// Curly-quote every title in place, once, so the TOC page (which renders
// these strings directly) matches the curly quotes the matching "## "/"# "
// heading in the body will render -- and so a literal Word Find for one of
// these titles (resolve/verify_toc_pages.ps1) still locates its heading.
TOC_ENTRIES.forEach((e) => { e.title = smartenQuotes(e.title); });

// Every heading (front/chapter via "## ", part/back via non-first "# ") gets a
// bookmark id of "toc<N>" assigned in the exact order TOC_ENTRIES lists them --
// see ctx.nextTocId() in parseFile. These two maps let in-text "Chapter 12" /
// "Part Six" mentions resolve to the right bookmark for auto cross-linking.
const CHAPTER_TOC_INDEX = {};
const PART_TOC_INDEX = {};
TOC_ENTRIES.forEach((e, idx) => {
  if (e.type === "chapter") {
    const m = e.title.match(/^(\d+)\./);
    if (m) CHAPTER_TOC_INDEX[m[1]] = idx;
  } else if (e.type === "part") {
    const m = e.title.match(/^PART (\w+)/);
    if (m) PART_TOC_INDEX[m[1].toUpperCase()] = idx;
  }
});

// Subtle, book-appropriate link styling: a muted slate blue (not web-link
// bright blue) plus a thin underline, so a link reads clearly even in print.
const LINK_STYLE = { color: "44546A", underline: { type: "single" } };

const BODY_FONT = "Cambria";
const MATH_FONT = "Cambria Math";
const BODY_SIZE = 24; // half-points -> 12pt
const PARA_SPACING_AFTER = 260;
const LINE_SPACING = { line: 360, lineRule: "auto" };

// Headline style for every heading level (main title, Part-title pages, and
// "## " chapter/section headings), plus the Table of Contents heading itself:
// Amazon Ember, 18pt bold, centered, in the book's accent blue.
const HEADLINE_FONT = "Amazon Ember";
const HEADLINE_SIZE = 36; // half-points -> 18pt
const HEADLINE_COLOR = "0000FF";
const FIGURES_DIR = path.join(__dirname, "Figures");

let TOC_PAGES = {};
try {
  TOC_PAGES = JSON.parse(fs.readFileSync(path.join(__dirname, "toc_pages.json"), "utf-8"));
} catch (e) { /* pass 1: no page numbers yet -- entries render with a blank leader target */ }

// Matches "Chapter N", "Chapters N-N" (an en-dash range), and "Part <WORD>".
// Only the number/name itself gets hyperlinked; "Chapter "/"Part " stays
// plain text. A reference to something not in the TOC index (typo, or a
// generic "this Part") is left as ordinary plain text rather than forced.
const CROSSREF_RE = /\b(Chapters?)\s+(\d+)(?:–(\d+))?\b|\bPart\s+([A-Za-z]+)\b/g;

function linkifyChapterRefs(text, opts) {
  const { font, size, italics } = opts;
  const runs = [];
  let cursor = 0;
  const re = new RegExp(CROSSREF_RE.source, "g");
  let m;
  while ((m = re.exec(text))) {
    const [full, chWord, num1, num2, partName] = m;
    const plain = () => runs.push(new TextRun({ text: full, font, size, italics }));

    if (chWord) {
      const idx1 = CHAPTER_TOC_INDEX[num1];
      if (idx1 === undefined) { if (m.index > cursor) runs.push(new TextRun({ text: text.slice(cursor, m.index), font, size, italics })); plain(); cursor = m.index + full.length; continue; }
      if (m.index > cursor) runs.push(new TextRun({ text: text.slice(cursor, m.index), font, size, italics }));
      runs.push(new TextRun({ text: chWord + " ", font, size, italics }));
      runs.push(new InternalHyperlink({ anchor: "toc" + idx1, children: [new TextRun({ text: num1, font, size, italics, ...LINK_STYLE })] }));
      if (num2) {
        runs.push(new TextRun({ text: "–", font, size, italics }));
        const idx2 = CHAPTER_TOC_INDEX[num2];
        if (idx2 !== undefined) {
          runs.push(new InternalHyperlink({ anchor: "toc" + idx2, children: [new TextRun({ text: num2, font, size, italics, ...LINK_STYLE })] }));
        } else {
          runs.push(new TextRun({ text: num2, font, size, italics }));
        }
      }
    } else if (partName) {
      const idx = PART_TOC_INDEX[partName.toUpperCase()];
      if (idx === undefined) { if (m.index > cursor) runs.push(new TextRun({ text: text.slice(cursor, m.index), font, size, italics })); plain(); cursor = m.index + full.length; continue; }
      if (m.index > cursor) runs.push(new TextRun({ text: text.slice(cursor, m.index), font, size, italics }));
      runs.push(new TextRun({ text: "Part ", font, size, italics }));
      runs.push(new InternalHyperlink({ anchor: "toc" + idx, children: [new TextRun({ text: partName, font, size, italics, ...LINK_STYLE })] }));
    }
    cursor = m.index + full.length;
  }
  if (cursor < text.length) {
    runs.push(new TextRun({ text: text.slice(cursor), font, size, italics }));
  }
  return runs;
}

// Splits a math/italic span on bare ^token / _token markers (superscript /
// subscript), e.g. "e^iθ" or "p_mechanical", rendering the token in the same
// font/italics as its surroundings but raised or lowered.
const TOKEN_RE = /([\^_])([A-Za-z0-9Ͱ-Ͽ]+)/g;

function styledRuns(text, font, italics) {
  const runs = [];
  let cursor = 0;
  const re = new RegExp(TOKEN_RE.source, "g");
  let m;
  while ((m = re.exec(text))) {
    if (m.index > cursor) {
      runs.push(new TextRun({ text: text.slice(cursor, m.index), font, size: BODY_SIZE, italics }));
    }
    runs.push(new TextRun({
      text: m[2], font, size: BODY_SIZE, italics,
      ...(m[1] === "^" ? { superScript: true } : { subScript: true }),
    }));
    cursor = re.lastIndex;
  }
  if (cursor < text.length) {
    runs.push(new TextRun({ text: text.slice(cursor), font, size: BODY_SIZE, italics }));
  }
  return runs;
}

// Turns bare https://... sequences into external hyperlinks, then hands the
// leftover text to the chapter/part cross-ref linker.
function linkifyUrls(text, opts) {
  const runs = [];
  const re = /https?:\/\/[^\s),]+/g;
  let cursor = 0;
  let m;
  while ((m = re.exec(text))) {
    if (m.index > cursor) {
      runs.push(...linkifyChapterRefs(text.slice(cursor, m.index), opts));
    }
    runs.push(new ExternalHyperlink({
      link: m[0],
      children: [new TextRun({ text: m[0], font: opts.font, size: opts.size, italics: opts.italics, ...LINK_STYLE })],
    }));
    cursor = re.lastIndex;
  }
  if (cursor < text.length) {
    runs.push(...linkifyChapterRefs(text.slice(cursor), opts));
  }
  return runs;
}

// Plain-body-text counterpart to styledRuns: handles bare ^N endnote markers
// in ordinary prose (not inside a *math* span). A numeric marker jumps to
// the matching note in Appendix B. Surrounding text is URL-linked, then
// chapter-linked.
function plainRunsWithSuperscript(text, opts) {
  const runs = [];
  let cursor = 0;
  const re = /\^([A-Za-z0-9]+)/g;
  let m;
  while ((m = re.exec(text))) {
    if (m.index > cursor) {
      runs.push(...linkifyUrls(text.slice(cursor, m.index), opts));
    }
    const marker = new TextRun({ text: m[1], font: opts.font, size: opts.size, italics: opts.italics, superScript: true, ...(/^\d+$/.test(m[1]) ? LINK_STYLE : {}) });
    if (/^\d+$/.test(m[1])) {
      runs.push(new InternalHyperlink({ anchor: "note" + m[1], children: [marker] }));
    } else {
      runs.push(marker);
    }
    cursor = re.lastIndex;
  }
  if (cursor < text.length) {
    runs.push(...linkifyUrls(text.slice(cursor), opts));
  }
  return runs;
}

// Splits a full line on **bold** and *italic/math* spans, running whatever's
// left over through plainRunsWithSuperscript (endnote markers + cross-refs).
function inlineRuns(line) {
  const runs = [];
  const re = /\*\*(.+?)\*\*|\*(.+?)\*/g;
  let cursor = 0;
  let m;
  while ((m = re.exec(line))) {
    if (m.index > cursor) {
      runs.push(...plainRunsWithSuperscript(line.slice(cursor, m.index), { font: BODY_FONT, size: BODY_SIZE, italics: false }));
    }
    if (m[1] !== undefined) {
      runs.push(new TextRun({ text: m[1], font: BODY_FONT, size: BODY_SIZE, bold: true }));
    } else {
      runs.push(...styledRuns(m[2], MATH_FONT, true));
    }
    cursor = re.lastIndex;
  }
  if (cursor < line.length) {
    runs.push(...plainRunsWithSuperscript(line.slice(cursor), { font: BODY_FONT, size: BODY_SIZE, italics: false }));
  }
  return runs;
}

function isMathOnlyLine(line) {
  const t = line.trim();
  // Real math/definition lines in this manuscript top out around 110 chars
  // (the longest is a "where ... " gloss line). A long single-*-wrapped
  // paragraph -- e.g. a full-paragraph italic aside -- is prose, not a
  // centered equation, and must not be swept up by this heuristic.
  return t.startsWith("*") && t.length > 1 && t.length <= 150 && !t.startsWith("**") && t.lastIndexOf("*") > 0;
}

function pngDimensions(buffer) {
  // PNG signature (8 bytes) + chunk length (4) + "IHDR" (4) = 16, then
  // width and height each as a big-endian uint32.
  return { width: buffer.readUInt32BE(16), height: buffer.readUInt32BE(20) };
}

function imageParagraphs(caption, filename) {
  const buffer = fs.readFileSync(path.join(FIGURES_DIR, filename));
  const { width, height } = pngDimensions(buffer);
  const targetWidth = 420;
  const targetHeight = Math.round(height * (targetWidth / width));
  return [
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 120, ...LINE_SPACING },
      children: [new ImageRun({ data: buffer, type: "png", transformation: { width: targetWidth, height: targetHeight } })],
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: PARA_SPACING_AFTER, ...LINE_SPACING },
      children: [new TextRun({ text: caption, font: BODY_FONT, size: 20, italics: true })],
    }),
  ];
}

function tocLine(title, page, style, idx) {
  const bold = style === "part" || style === "back";
  const indent = style === "chapter" ? { left: 360 } : undefined;
  return new Paragraph({
    spacing: style === "part" ? { before: 240, after: 60 } : { after: 60 },
    indent,
    children: [
      new InternalHyperlink({
        anchor: "toc" + idx,
        children: [new TextRun({ text: title, font: BODY_FONT, size: bold ? 24 : 22, bold, ...LINK_STYLE })],
      }),
      new TextRun({
        children: [
          new PositionalTab({
            alignment: PositionalTabAlignment.RIGHT,
            relativeTo: PositionalTabRelativeTo.MARGIN,
            leader: PositionalTabLeader.DOT,
          }),
        ],
        font: BODY_FONT, size: bold ? 24 : 22, bold,
      }),
      new TextRun({ text: page != null ? String(page) : "", font: BODY_FONT, size: bold ? 24 : 22, bold }),
    ],
  });
}

function buildTOCParagraphs() {
  const paras = [
    new Paragraph({
      pageBreakBefore: true,
      pStyle: undefined,
      heading: HeadingLevel.HEADING_2,
      alignment: AlignmentType.CENTER,
      spacing: { before: 0, after: 400 },
      children: [new TextRun({ text: "Table of Contents", font: HEADLINE_FONT, size: HEADLINE_SIZE, bold: true, color: HEADLINE_COLOR })],
    }),
  ];
  TOC_ENTRIES.forEach((e, idx) => {
    paras.push(tocLine(e.title, TOC_PAGES[String(idx)], e.type, idx));
  });
  return paras;
}

function parseFile(mdPath, ctx) {
  const raw = smartenQuotes(fs.readFileSync(mdPath, "utf-8"));
  const lines = raw.split(/\r?\n/);
  let i = 0;
  while (i < lines.length) {
    const line = lines[i];
    if (line.trim() === "") { i++; continue; }
    if (line.trim() === "---") { i++; continue; }

    if (line.startsWith("# ")) {
      const isVeryFirst = !ctx.sawTitle;
      if (isVeryFirst) {
        ctx.sawTitle = true;
        ctx.pushPara(new Paragraph({
          heading: HeadingLevel.TITLE,
          alignment: AlignmentType.CENTER,
          spacing: { after: 300 },
          children: [new TextRun({
            text: line.slice(2).trim(),
            font: HEADLINE_FONT, size: HEADLINE_SIZE, bold: true, color: HEADLINE_COLOR,
          })],
        }));
      } else {
        // Part-title divider page: its own section, vertically centered,
        // containing nothing but the title -- then a fresh top-aligned
        // section starts for the chapter that follows.
        const titlePara = new Paragraph({
          heading: HeadingLevel.HEADING_1,
          alignment: AlignmentType.CENTER,
          children: [new Bookmark({
            id: ctx.nextTocId(),
            children: [new TextRun({
              text: line.slice(2).trim(),
              font: HEADLINE_FONT, size: HEADLINE_SIZE, bold: true, color: HEADLINE_COLOR,
            })],
          })],
        });
        ctx.startCenteredPartPage(titlePara);
      }
      i++; continue;
    }
    if (line.trim() === "%%TOC%%") {
      buildTOCParagraphs().forEach((p) => ctx.pushPara(p));
      i++; continue;
    }
    if (line.startsWith("## ")) {
      ctx.pushPara(new Paragraph({
        heading: HeadingLevel.HEADING_2,
        pageBreakBefore: true,
        alignment: AlignmentType.CENTER,
        spacing: { before: 0, after: 240 },
        children: [new Bookmark({
          id: ctx.nextTocId(),
          children: [new TextRun({ text: line.slice(3).trim(), font: HEADLINE_FONT, size: HEADLINE_SIZE, bold: true, color: HEADLINE_COLOR })],
        })],
      }));
      i++; continue;
    }
    // Image: "![Figure N. Caption text.](filename.png)"
    const imgMatch = line.match(/^!\[(.*)\]\((.*)\)$/);
    if (imgMatch) {
      imageParagraphs(imgMatch[1], imgMatch[2]).forEach((p) => ctx.pushPara(p));
      i++; continue;
    }

    // Equation block: "> **Equation (N).** label" then "> $math$"
    if (line.startsWith("> ") && /\*\*Equation \(\d+\)\.\*\*/.test(line)) {
      const capMatch = line.match(/^> \*\*Equation \((\d+)\)\.\*\*\s*(.*)$/);
      const num = capMatch[1];
      const label = capMatch[2];
      ctx.pushPara(new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 360, after: 120, ...LINE_SPACING },
        keepNext: true,
        keepLines: true,
        children: [new TextRun({ text: `Equation (${num})`, font: BODY_FONT, size: 20, italics: true, bold: true }),
                   ...(label ? linkifyChapterRefs(`  —  ${label}`, { font: BODY_FONT, size: 20, italics: true }) : [])],
      }));
      i++;
      // one or more subsequent blockquote lines hold the formula(s), e.g. "> *Φ_0 = h/2e*"
      // the (N) tag goes on the last line of the group only. keepNext chains every line
      // in the block to the next (label -> line1 -> ... -> last line) so Word never
      // splits an equation block across a page boundary.
      const formulaLines = [];
      while (i < lines.length && isMathOnlyLine(lines[i].replace(/^>\s*/, ""))) {
        formulaLines.push(lines[i].replace(/^>\s*/, "").trim());
        i++;
      }
      formulaLines.forEach((t, idx) => {
        const closeIdx = t.lastIndexOf("*");
        const mathContent = t.slice(1, closeIdx);
        const trailing = t.slice(closeIdx + 1);
        const children = styledRuns(mathContent, MATH_FONT, true);
        if (trailing) children.push(new TextRun({ text: trailing, font: BODY_FONT, size: BODY_SIZE }));
        const isLast = idx === formulaLines.length - 1;
        if (isLast) children.push(new TextRun({ text: `    (${num})`, font: BODY_FONT, size: BODY_SIZE }));
        ctx.pushPara(new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { before: idx === 0 ? 120 : 60, after: isLast ? 300 : 60, ...LINE_SPACING },
          keepNext: !isLast,
          keepLines: true,
          children,
        }));
      });
      continue;
    }

    // regular paragraph
    const centered = isMathOnlyLine(line);
    let children;
    if (centered) {
      const t = line.trim();
      const closeIdx = t.lastIndexOf("*");
      const mathContent = t.slice(1, closeIdx);
      const trailing = t.slice(closeIdx + 1);
      children = styledRuns(mathContent, MATH_FONT, true);
      if (trailing) children.push(new TextRun({ text: trailing, font: BODY_FONT, size: BODY_SIZE }));
    } else {
      children = inlineRuns(line);
    }
    ctx.pushPara(new Paragraph({
      alignment: centered ? AlignmentType.CENTER : AlignmentType.LEFT,
      spacing: { after: PARA_SPACING_AFTER, ...LINE_SPACING },
      children,
    }));
    i++;
  }
}

const PAGE_SETUP = {
  // 6"x9" trade-book trim (standard nonfiction size), DXA units (1440/inch)
  size: { width: 8640, height: 12960 },
  margin: { top: 1080, bottom: 1080, left: 1080, right: 1080 },
};
const FOOTERS = {
  default: new Footer({
    children: [new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [new TextRun({ children: [PageNumber.CURRENT], font: BODY_FONT, size: 20 })],
    })],
  }),
};

// Builds up a list of Word *sections* (not just paragraphs), because
// vertically centering a Part-title page is a per-section page property in
// OOXML -- it can't be applied to one paragraph in the middle of a section.
const sections = [];
let currentChildren = [];
let tocIdCounter = 0;
const ctx = {
  sawTitle: false,
  nextTocId() { return "toc" + (tocIdCounter++); },
  pushPara(para) { currentChildren.push(para); },
  flush(verticalAlign) {
    sections.push({
      properties: {
        page: PAGE_SETUP,
        ...(verticalAlign ? { verticalAlign } : {}),
      },
      footers: FOOTERS,
      children: currentChildren,
    });
    currentChildren = [];
  },
  startCenteredPartPage(titlePara) {
    this.flush(); // close out everything before this Part title, top-aligned
    currentChildren.push(titlePara);
    this.flush(VerticalAlignSection.CENTER); // isolate the title on its own centered page
  },
};

const files = process.argv.slice(2);
files.forEach((f) => parseFile(f, ctx));
ctx.flush(); // whatever's left after the last file

const doc = new Document({
  creator: "Lothar J. Musiol",
  lastModifiedBy: "Lothar J. Musiol",
  title: "The Quantum Conversation",
  subject: "Phase, Light, and the Hidden Architecture of Electromagnetism",
  description: "Phase, Light, and the Hidden Architecture of Electromagnetism",
  sections,
});

Packer.toBuffer(doc).then((buffer) => {
  fs.writeFileSync(path.join(__dirname, "manuscript_draft.docx"), buffer);
  console.log("wrote manuscript_draft.docx");
});
