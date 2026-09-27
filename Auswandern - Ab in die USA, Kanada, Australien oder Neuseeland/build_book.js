"use strict";
// Builds build/Auswandern - Ab in die USA, Kanada, Australien oder Neuseeland.docx from manuscript/*.md
//   node build_book.js [--dir manuscript] [--out build/Auswandern - Ab in die USA, Kanada, Australien oder Neuseeland.docx]
// Page: 6x9in trim, 0.75in margins (KDP-safe up to 500 pages).
// The table of contents is a real Word TOC field; run finalize_docx.ps1 to
// update it (and export a PDF) through Word.
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, Footer, PageNumber,
  Table, TableRow, TableCell, WidthType, BorderStyle, ShadingType, TableOfContents,
  LevelFormat, Bookmark, InternalHyperlink, ExternalHyperlink, VerticalAlignSection, TableLayoutType, TabStopType, LineRuleType,
} = require("docx");
const P = require("./lib/parse");

// ------------------------------------------------------------------ args
const args = process.argv.slice(2);
const argVal = (name, def) => { const i = args.indexOf(name); return i >= 0 && args[i + 1] ? args[i + 1] : def; };
const ROOT = __dirname;
const MS_DIR = path.resolve(ROOT, argVal("--dir", "manuscript"));
const OUT = path.resolve(ROOT, argVal("--out", "build/Auswandern - Ab in die USA, Kanada, Australien oder Neuseeland.docx"));
const BOOK = JSON.parse(fs.readFileSync(path.join(ROOT, "book.json"), "utf-8"));

// ------------------------------------------------------------------ layout
const PAGE = { width: 8640, height: 12960 };            // 6x9in in DXA
const MARGIN = { top: 1080, bottom: 1100, left: 1080, right: 1080 };
const TEXT_W = PAGE.width - MARGIN.left - MARGIN.right; // 6480 DXA = 4.5in
const FONT = "Cambria";
const HEADING_BLUE = "0000FF"; // pixel-sampled from the user's reference swatch
const HEADING_FONT = "Amazon Ember";
const HEADING_SIZE = 36; // 18pt (docx sizes are in half-points)
const BODY = 22;   // 11pt
const SMALL = 20;  // 10pt (boxes)
const TBL = 18;    // 9pt (tables)
const LINE = 288;  // 1.2 line spacing

const BOX = {
  "Kurz gesagt":    { label: "KURZ GESAGT",              color: "1F3A5F", fill: "ECF1F7" },
  "Achtung":        { label: "ACHTUNG",                  color: "9B2C2C", fill: "FAEEEE" },
  "Spartipp":       { label: "SPARTIPP",                 color: "2F6B3B", fill: "EDF6EF" },
  "Merke":          { label: "MERKE",                    color: "8A6212", fill: "FBF5E4" },
  "Praxisbeispiel": { label: "PRAXISBEISPIEL · FIKTIV",  color: "4A5568", fill: "F0F2F5" },
  "Checkliste":     { label: "CHECKLISTE",               color: "1F6F78", fill: "EBF5F6" },
  "Stand":          { label: "STAND",                    color: "6B7280", fill: "F2F3F5" },
  "Kein Rechtsrat": { label: "KEIN RECHTSRAT",           color: "6B7280", fill: "F2F3F5" },
};
const NONE = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const NO_BORDERS = { top: NONE, bottom: NONE, left: NONE, right: NONE, insideHorizontal: NONE, insideVertical: NONE };

// ------------------------------------------------------------------ pass 1: read + collect bookmarks
const files = P.listManuscriptFiles(MS_DIR);
if (!files.length) { console.error("No .md files in " + MS_DIR); process.exit(1); }

const docs = files.map((f) => ({ file: path.basename(f), blocks: P.parseMarkdown(fs.readFileSync(path.join(MS_DIR, f), "utf-8")) }));

const bookmarks = new Set();
let bmCounter = 0;
docs.forEach((d) => d.blocks.forEach((b) => {
  if (b.type === "h2") { b.bookmark = P.bookmarkFor(b.text, d.file, ++bmCounter); bookmarks.add(b.bookmark); }
}));

// ------------------------------------------------------------------ inline -> docx runs
function anchorFor(kind, key) { return kind === "k" ? "k" + key : "anhang_" + key.toLowerCase(); }

function xrefChildren(text, style) {
  const out = [];
  const re = new RegExp(P.XREF_RE.source, "g");
  let cursor = 0, m;
  const plain = (t) => t && out.push(new TextRun({ text: t, ...style }));
  while ((m = re.exec(text))) {
    plain(text.slice(cursor, m.index));
    if (m[1]) {
      out.push(new TextRun({ text: m[1] + P.NBSP, ...style }));
      // link each number in the group individually
      const parts = m[2].split(/(\d{1,2})/);
      parts.forEach((part) => {
        if (/^\d{1,2}$/.test(part) && bookmarks.has(anchorFor("k", part))) {
          out.push(new InternalHyperlink({ anchor: anchorFor("k", part), children: [new TextRun({ text: part, ...style })] }));
        } else plain(part);
      });
    } else {
      out.push(new TextRun({ text: m[3] + P.NBSP, ...style }));
      const a = anchorFor("a", m[4]);
      if (bookmarks.has(a)) out.push(new InternalHyperlink({ anchor: a, children: [new TextRun({ text: m[4], ...style })] }));
      else plain(m[4]);
    }
    cursor = m.index + m[0].length;
  }
  plain(text.slice(cursor));
  return out;
}

function runs(text, base = {}) {
  const size = base.size || BODY;
  const out = [];
  P.parseInline(P.typo(text)).forEach((r) => {
    if (r.br) { out.push(new TextRun({ break: 1, size })); return; }
    const style = {
      font: FONT, size,
      bold: !!(r.b || base.bold), italics: !!(r.i || base.italics),
      ...(base.color ? { color: base.color } : {}),
    };
    if (r.link) {
      const linkStyle = { ...style, color: "0563C1", underline: { type: "single" } };
      const child = new TextRun({ text: r.t, ...linkStyle });
      if (r.link.startsWith("#")) {
        const anchor = r.link.slice(1);
        if (bookmarks.has(anchor)) out.push(new InternalHyperlink({ anchor, children: [child] }));
        else out.push(new TextRun({ text: r.t, ...style })); // unresolved anchor: plain text, caught by lint
      } else {
        out.push(new ExternalHyperlink({ link: r.link, children: [child] }));
      }
      return;
    }
    out.push(...xrefChildren(r.t, style));
  });
  return out;
}

// ------------------------------------------------------------------ block renderers
function spacer(twips) {
  return new Paragraph({ spacing: { before: 0, after: 0, line: twips, lineRule: LineRuleType.EXACT }, children: [new TextRun({ text: "", size: 2 })] });
}
let olInstance = 0;

function para(text, opts = {}) {
  return new Paragraph({
    alignment: opts.align || AlignmentType.LEFT,
    spacing: { after: opts.after ?? 140, before: opts.before ?? 0, line: opts.line ?? LINE },
    keepNext: !!opts.keepNext, keepLines: !!opts.keepLines,
    indent: opts.indent,
    children: runs(text, opts),
  });
}

function listParas(block, opts = {}) {
  const size = opts.size || BODY;
  const out = [];
  let prevTopKind = null; // kind of the last top-level item; a new numbered run restarts at 1
  block.items.forEach((it) => {
    if (it.kind === "ol" && it.level === 0 && prevTopKind !== "ol") olInstance++;
    if (it.level === 0) prevTopKind = it.kind;
    const spacing = { after: opts.after ?? 60, line: opts.line ?? LINE };
    if (it.check !== null) {
      const left = it.level ? 720 : 400;
      out.push(new Paragraph({
        spacing, indent: { left, hanging: 330 },
        tabStops: [{ type: TabStopType.LEFT, position: left }],
        children: [
          new TextRun({ text: it.check === "x" ? "☑" : "☐", font: "Segoe UI Symbol", size }),
          new TextRun({ text: "\t", size }),
          ...runs(it.text, { size, color: opts.color }),
        ],
      }));
    } else if (it.kind === "ul") {
      out.push(new Paragraph({ spacing, numbering: { reference: "bullets", level: it.level }, children: runs(it.text, { size, color: opts.color }) }));
    } else {
      out.push(new Paragraph({ spacing, numbering: { reference: "nums", level: it.level, instance: olInstance }, children: runs(it.text, { size, color: opts.color }) }));
    }
  });
  return out;
}

function colWidths(header, rows) {
  const n = header.length;
  const weights = [];
  // Longest unbreakable token (no spaces/slashes) per column, in DXA, so a
  // single long compound word never gets forced to break mid-word instead
  // of wrapping at a word boundary (~100 twips/char at table font size,
  // plus cell padding).
  const CHAR_W = 130, PAD = 250;
  const floors = [];
  for (let j = 0; j < n; j++) {
    const cells = [header[j], ...rows.map((r) => r[j] || "")];
    const lens = cells.map((c) => P.stripInline(c).length);
    const avg = lens.reduce((a, b) => a + b, 0) / lens.length;
    const max = Math.max(...lens);
    weights.push(Math.max(9, Math.min(46, avg * 0.7 + max * 0.3)));
    let longestToken = 0;
    for (const c of cells) for (const tok of P.stripInline(c).split(/[\s/]+/)) longestToken = Math.max(longestToken, tok.length);
    floors.push(Math.max(950, longestToken * CHAR_W + PAD));
  }
  const sum = weights.reduce((a, b) => a + b, 0);
  const floorSum = floors.reduce((a, b) => a + b, 0);
  let w;
  if (floorSum <= TEXT_W) {
    // Every column can have its floor plus a content-weighted share of
    // what's left over.
    const remaining = TEXT_W - floorSum;
    w = floors.map((f, j) => f + Math.round(remaining * (weights[j] / sum)));
  } else {
    // Floors alone don't fit (several long compound words spread across
    // different columns of the same table) -- there's no way to satisfy
    // every column, so give each a share proportional to how much it
    // needs rather than shrinking all of them by the same amount.
    w = floors.map((f) => Math.max(750, Math.round((f / floorSum) * TEXT_W)));
  }
  const diff = TEXT_W - w.reduce((a, b) => a + b, 0);
  w[w.indexOf(Math.max(...w))] += diff;
  return w;
}

function tableBlock(block) {
  const n = block.header.length;
  const widths = colWidths(block.header, block.rows);
  const border = { style: BorderStyle.SINGLE, size: 4, color: "B8BEC7" };
  const borders = { top: border, bottom: border, left: border, right: border };
  const mk = (cells, isHead) => new TableRow({
    cantSplit: true, tableHeader: isHead,
    children: Array.from({ length: n }, (_, j) => new TableCell({
      width: { size: widths[j], type: WidthType.DXA },
      borders,
      shading: isHead ? { type: ShadingType.CLEAR, fill: "DDE3EA", color: "auto" } : undefined,
      margins: { top: 50, bottom: 50, left: 80, right: 80 },
      children: [new Paragraph({ spacing: { after: 0, line: 250 }, children: runs(cells[j] || "", { size: TBL, bold: isHead }) })],
    })),
  });
  return [
    new Table({
      width: { size: TEXT_W, type: WidthType.DXA }, columnWidths: widths, layout: TableLayoutType.FIXED,
      rows: [mk(block.header, true), ...block.rows.map((r) => mk(r, false))],
    }),
    spacer(180),
  ];
}

function boxBlock(block) {
  const cfg = BOX[block.label] || { label: block.label.toUpperCase(), color: "6B7280", fill: "F2F3F5" };
  const kids = [new Paragraph({
    spacing: { after: 70, line: 240 }, keepNext: true,
    children: [new TextRun({ text: cfg.label, font: FONT, size: 16, bold: true, color: cfg.color, characterSpacing: 24 })],
  })];
  block.blocks.forEach((b) => {
    if (b.type === "p") kids.push(para(b.text, { size: SMALL, after: 80, line: 264 }));
    else if (b.type === "list") kids.push(...listParas(b, { size: SMALL, after: 50, line: 264 }));
    else if (b.type === "table") kids.push(...tableBlock(b));
  });
  const totalChars = block.blocks.map(P.blockText).join(" ").length;
  const left = { style: BorderStyle.SINGLE, size: 24, color: cfg.color };
  return [
    new Table({
      width: { size: TEXT_W, type: WidthType.DXA }, columnWidths: [TEXT_W], layout: TableLayoutType.FIXED, borders: NO_BORDERS,
      rows: [new TableRow({
        cantSplit: totalChars < 1100,
        children: [new TableCell({
          width: { size: TEXT_W, type: WidthType.DXA },
          shading: { type: ShadingType.CLEAR, fill: cfg.fill, color: "auto" },
          borders: { top: NONE, bottom: NONE, right: NONE, left },
          margins: { top: 110, bottom: 80, left: 200, right: 160 },
          children: kids,
        })],
      })],
    }),
    spacer(220),
  ];
}

function quoteBlock(block) {
  const out = [];
  block.blocks.forEach((b) => { if (b.type === "p") out.push(para(b.text, { italics: true, indent: { left: 400 } })); });
  return out;
}

// ------------------------------------------------------------------ sections
const pageProps = { page: { size: PAGE, margin: MARGIN } };
const footerNum = new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 18 })] })] });
const footerNone = new Footer({ children: [new Paragraph({ children: [] })] });
const sections = [];
let cur = [];
function flush(o = {}) {
  if (!cur.length) return;
  sections.push({
    properties: { ...pageProps, ...(o.center ? { verticalAlign: VerticalAlignSection.CENTER } : {}), ...(o.bottom ? { verticalAlign: VerticalAlignSection.BOTTOM } : {}) },
    footers: { default: o.noFooter ? footerNone : footerNum },
    children: cur,
  });
  cur = [];
}

function titlePage() {
  const kids = [
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 240 }, children: [new TextRun({ text: BOOK.title, font: HEADING_FONT, size: 52, bold: true, color: HEADING_BLUE })] }),
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 360 }, children: [new TextRun({ text: BOOK.subtitle, font: HEADING_FONT, size: 32, bold: true, color: HEADING_BLUE })] }),
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 720, line: 300 }, children: [new TextRun({ text: P.typo(BOOK.tagline), font: FONT, size: 22 })] }),
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 120 }, children: [new TextRun({ text: BOOK.author, font: FONT, size: 30, bold: true })] }),
    new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: "Stand: " + BOOK.stand, font: FONT, size: 20, color: "666666" })] }),
  ];
  return kids;
}

function tocBlock() {
  return [
    new Paragraph({ pageBreakBefore: true, alignment: AlignmentType.CENTER, spacing: { after: 360 }, children: [new TextRun({ text: "Inhaltsverzeichnis", font: HEADING_FONT, size: 34, bold: true, color: HEADING_BLUE })] }),
    new TableOfContents("Inhaltsverzeichnis", { hyperlink: true, headingStyleRange: "1-2" }),
  ];
}

let smallMode = false;
const stats = [];
docs.forEach((d) => {
  const blocks = d.blocks;
  for (let i = 0; i < blocks.length; i++) {
    const b = blocks[i];
    switch (b.type) {
      case "directive":
        if (b.name === "TITLEPAGE") { flush(); cur.push(...titlePage()); }
        else if (b.name === "PAGEBREAK") cur.push(new Paragraph({ pageBreakBefore: true, children: [] }));
        else if (b.name === "TOC") cur.push(...tocBlock());
        else if (b.name === "SMALL") { cur.push(spacer(360)); smallMode = true; }
        else if (b.name === "NORMAL") { flush({ noFooter: true }); smallMode = false; }
        break;
      case "h1": {
        flush();
        cur.push(new Paragraph({ heading: HeadingLevel.HEADING_1, alignment: AlignmentType.CENTER, spacing: { after: 360, line: 340 }, children: [new TextRun({ text: P.typo(b.text), font: HEADING_FONT, bold: true, color: HEADING_BLUE })] }));
        while (i + 1 < blocks.length && blocks[i + 1].type === "p") {
          i++;
          cur.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 160, line: 300 }, indent: { left: 400, right: 400 }, children: runs(blocks[i].text, { italics: true, size: 24 }) }));
        }
        flush({ center: true, noFooter: true });
        break;
      }
      case "h2":
        cur.push(new Paragraph({
          heading: HeadingLevel.HEADING_2, pageBreakBefore: true, keepNext: true, alignment: AlignmentType.CENTER,
          spacing: { before: 0, after: 300, line: 340 },
          children: [new Bookmark({ id: b.bookmark, children: [new TextRun({ text: P.typo(b.text), font: HEADING_FONT, size: HEADING_SIZE, bold: true, color: HEADING_BLUE })] })],
        }));
        break;
      case "h3": cur.push(new Paragraph({ heading: HeadingLevel.HEADING_3, keepNext: true, alignment: AlignmentType.CENTER, spacing: { before: 280, after: 100, line: 340 }, children: [new TextRun({ text: P.typo(b.text), font: HEADING_FONT, size: HEADING_SIZE, bold: true, color: HEADING_BLUE })] })); break;
      case "h4": cur.push(new Paragraph({ heading: HeadingLevel.HEADING_4, keepNext: true, alignment: AlignmentType.CENTER, spacing: { before: 200, after: 80, line: 340 }, children: [new TextRun({ text: P.typo(b.text), font: HEADING_FONT, size: HEADING_SIZE, bold: true, color: HEADING_BLUE })] })); break;
      case "p":
        if (smallMode) cur.push(para(b.text, { size: 17, color: "444444", after: 90, line: 260 }));
        else cur.push(para(b.text));
        break;
      case "list": cur.push(...listParas(b), spacer(120)); break;
      case "table": cur.push(...tableBlock(b)); break;
      case "box": cur.push(...boxBlock(b)); break;
      case "quote": cur.push(...quoteBlock(b)); break;
    }
  }
  stats.push({ file: d.file, words: P.countWords(blocks) });
});
flush();

// ------------------------------------------------------------------ document
const numbering = {
  config: [
    { reference: "bullets", levels: [
      { level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 360, hanging: 240 } } } },
      { level: 1, format: LevelFormat.BULLET, text: "–", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 720, hanging: 240 } } } },
    ] },
    { reference: "nums", levels: [
      { level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 420, hanging: 330 } } } },
      { level: 1, format: LevelFormat.LOWER_LETTER, text: "%2)", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 800, hanging: 330 } } } },
    ] },
  ],
};

const styles = {
  default: { document: { run: { font: FONT, size: BODY, language: { value: BOOK.language } }, paragraph: { spacing: { line: LINE } } } },
  paragraphStyles: [
    { id: "Title", name: "Title", basedOn: "Normal", next: "Normal", run: { font: FONT, size: 60, bold: true }, paragraph: { alignment: AlignmentType.CENTER, spacing: { after: 300 } } },
    { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true, run: { font: FONT, size: 48, bold: true, color: "1F3A5F" }, paragraph: { spacing: { before: 0, after: 360 }, outlineLevel: 0 } },
    { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true, run: { font: FONT, size: 34, bold: true, color: "1F3A5F" }, paragraph: { spacing: { before: 0, after: 300 }, outlineLevel: 1 } },
    { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true, run: { font: FONT, size: 26, bold: true, color: "1F3A5F" }, paragraph: { spacing: { before: 280, after: 100 }, outlineLevel: 2 } },
    { id: "Heading4", name: "Heading 4", basedOn: "Normal", next: "Normal", quickFormat: true, run: { font: FONT, size: 22, bold: true, italics: true }, paragraph: { spacing: { before: 200, after: 80 }, outlineLevel: 3 } },
    { id: "TOC1", name: "toc 1", basedOn: "Normal", next: "Normal", run: { font: FONT, size: 22, bold: true }, paragraph: { spacing: { before: 200, after: 60 } } },
    { id: "TOC2", name: "toc 2", basedOn: "Normal", next: "Normal", run: { font: FONT, size: 20 }, paragraph: { spacing: { after: 30 }, indent: { left: 240 } } },
  ],
};

const doc = new Document({
  creator: BOOK.author, lastModifiedBy: BOOK.author,
  title: BOOK.title + " – " + BOOK.subtitle, subject: BOOK.tagline, description: BOOK.tagline,
  features: { updateFields: true },
  styles, numbering, sections,
});

fs.mkdirSync(path.dirname(OUT), { recursive: true });
Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(OUT, buf);
  const total = stats.reduce((a, s) => a + s.words, 0);
  console.log("wrote " + path.relative(ROOT, OUT) + "  (" + files.length + " files, ~" + total.toLocaleString("de-DE") + " words)");
});
