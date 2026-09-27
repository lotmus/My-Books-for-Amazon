"use strict";
// Style/structure linter for manuscript chapters (contract: _Konzept/00_Buchbibel.md).
//   node lint_book.js [file-substring ...]     e.g.  node lint_book.js K05 K06
// Exit code 1 if any ERROR is found (warnings do not fail).
const fs = require("fs");
const path = require("path");
const P = require("./lib/parse");

const MS = path.join(__dirname, "manuscript");
const TARGET = { 1: 3600, 2: 3400, 3: 3200, 4: 2400, 5: 3800, 6: 3800, 7: 2800, 8: 3400, 9: 3600, 10: 3000, 11: 2800, 12: 4200, 13: 3000, 14: 4200, 15: 2400, 16: 2800, 17: 3600, 18: 2600, 19: 2600, 20: 2800, 21: 3300, 22: 2200, 23: 2400, 24: 2600, 25: 3000, 26: 3600, 27: 2800, 28: 3600, 29: 3400, 30: 3000, 31: 4000, 32: 3200, 33: 2600, 34: 2400, 35: 2600, 36: 3400, 37: 2800, 38: 3200, 39: 3000, 40: 2800, 41: 2800, 42: 2600 };
const VALID_BOX = new Set(["Kurz gesagt", "Achtung", "Spartipp", "Merke", "Praxisbeispiel", "Checkliste", "Stand", "Kein Rechtsrat"]);
const SLANG = /\b(krass|mega|geil|Hammer|Mörder|abgefahren|Bock auf|checkst|Leute!|Hey\b|Alter\b)/i;
const EMOJI = /(?![©®™↔])\p{Extended_Pictographic}/u; // © ® ™ ↔ are legitimate (technical symbols, not emoji)
const filters = process.argv.slice(2);

const allFiles = P.listManuscriptFiles(MS);
const files = allFiles.filter((f) => !filters.length || filters.some((x) => f.includes(x)));

// Global anchor set for internal-link validation, built from ALL files
// (not just the filtered subset), mirroring build_book.js's bookmark pass.
const allAnchors = new Set();
allFiles.forEach((f) => {
  const blocks = P.parseMarkdown(fs.readFileSync(path.join(MS, f), "utf-8"));
  let idx = 0;
  blocks.forEach((b) => { if (b.type === "h2") allAnchors.add(P.bookmarkFor(b.text, path.basename(f), ++idx)); });
});

function walk(blocks, fn) { blocks.forEach((b) => { fn(b); if (b.blocks) walk(b.blocks, fn); }); }
let errorFiles = 0, totalWords = 0;
const rows = [];

files.forEach((f) => {
  const raw = fs.readFileSync(path.join(MS, f), "utf-8");
  const blocks = P.parseMarkdown(raw);
  const errs = [], warns = [];
  const words = P.countWords(blocks);
  totalWords += words;
  const base = path.basename(f);
  const km = base.match(/_K(\d\d)_/);
  const NEW_PART = { TAU: "Australien", TKA: "Kanada", TNZ: "Neuseeland", T00: "Universal" };
  const newKm = base.match(/^(TAU|TKA|TNZ|T00)_K\d\d_/);
  const isChapter = !!km;
  const num = km && !newKm ? parseInt(km[1], 10) : null;

  // ---- universal checks (all files)
  const plain = blocks.map(P.blockText).join("\n");
  const straight = (raw.match(/["']/g) || []).length;
  if (straight) warns.push(`${straight}× gerade Anführungszeichen (werden automatisch typografisch korrigiert)`);
  if (/!\[.*?\]\(.*?\)/.test(raw)) errs.push("Bild-Markdown gefunden");
  {
    const linkRe = /\[([^\]]+)\]\(([^)]+)\)/g;
    let lm;
    while ((lm = linkRe.exec(raw))) {
      const url = lm[2];
      if (url.startsWith("#")) {
        const anchor = url.slice(1);
        if (!allAnchors.has(anchor)) errs.push(`interner Link „${lm[1]}“ zeigt auf unbekannten Anker #${anchor}`);
      } else if (!/^https:\/\//.test(url)) {
        errs.push(`externer Link „${lm[1]}“ ohne https://-Prefix: ${url}`);
      }
    }
  }
  if (/<(?!br\s*\/?>)[a-zA-Z][^>]*>/.test(raw)) errs.push("HTML-Tag außer <br> gefunden");
  if (EMOJI.test(raw)) errs.push("Emoji gefunden");
  if (/^---+\s*$/m.test(raw)) errs.push("Trennlinie --- im Text");
  if (SLANG.test(plain)) warns.push("möglicher Slang: " + (plain.match(SLANG) || [""])[0]);
  const formal = plain.match(/[a-zäöüß,;:] (Sie|Ihnen|Ihre[mnrs]?|Ihr)\b/g);
  if (formal) errs.push(`Sie-Form (${formal.length}×, z. B. „${formal[0]}“) — Buch nutzt „du“`);
  if (/\$\s?\d|\b\d{1,3},\d{3}\b(?!\s*[%])/.test(plain)) warns.push("US-Zahlenformat? ($1,000 bzw. 1,000) → deutsches Format 1.000 $");
  const excl = (plain.match(/!/g) || []).length;
  if (excl > 4) warns.push(`${excl}× Ausrufezeichen`);
  walk(blocks, (b) => {
    if (b.type === "box" && !VALID_BOX.has(b.label)) errs.push(`unbekanntes Box-Label „${b.label}“`);
    if (b.type === "table" && b.header.length > 4) warns.push(`Tabelle mit ${b.header.length} Spalten (max. 4)`);
    if (b.type === "table") b.rows.forEach((r) => { if (r.length !== b.header.length) errs.push("Tabellenzeile mit falscher Spaltenzahl"); });
    if ((b.type === "h1") && isChapter) errs.push("Ebene-1-Überschrift in Kapitel");
  });
  // cross-references
  const re = new RegExp(P.XREF_RE.source, "g");
  let m;
  while ((m = re.exec(plain))) {
    if (m[2]) (m[2].match(/\d+/g) || []).forEach((n) => { if (+n < 1 || +n > 42) errs.push(`Querverweis auf nicht existierendes Kapitel ${n}`); });
  }

  // ---- chapter checks
  if (isChapter) {
    const h2 = blocks.filter((b) => b.type === "h2");
    if (h2.length !== 1) errs.push(`${h2.length} Kapitelüberschriften (## …) statt genau 1`);
    else if (newKm) {
      const teil = NEW_PART[newKm[1]];
      const okTeil = new RegExp(`^${teil}:\\s+\\S`).test(h2[0].text);
      const okKapitel = /^Kapitel\s+\d+:\s+\S/.test(h2[0].text);
      if (!okTeil && !okKapitel) errs.push(`Kapitelüberschrift nicht im Format „## ${teil}: Titel“ oder „## Kapitel N: Titel“`);
      if (blocks[0].type !== "h2") errs.push("Datei beginnt nicht mit der Kapitelüberschrift");
    } else {
      const hm = h2[0].text.match(/^Kapitel\s+(\d+):\s+\S/);
      if (!hm) errs.push("Kapitelüberschrift nicht im Format „## Kapitel N: Titel“");
      else if (+hm[1] !== num) errs.push(`Kapitelnummer ${hm[1]} passt nicht zum Dateinamen (K${num})`);
      if (blocks[0].type !== "h2") errs.push("Datei beginnt nicht mit der Kapitelüberschrift");
    }
    const boxes = blocks.filter((b) => b.type === "box");
    const count = (l) => boxes.filter((b) => b.label === l).length;
    if (count("Kurz gesagt") !== 1) errs.push(`„Kurz gesagt“-Box ${count("Kurz gesagt")}× (Pflicht: genau 1)`);
    if (count("Checkliste") < 1) errs.push("keine Checkliste");
    else if (!boxes.find((b) => b.label === "Checkliste").blocks.some((x) => x.type === "list" && x.items.some((i) => i.check !== null))) errs.push("Checkliste ohne - [ ]-Punkte");
    if (count("Stand") !== 1) errs.push(`„Stand“-Box ${count("Stand")}× (Pflicht: genau 1)`);
    const last = blocks[blocks.length - 1];
    if (!(last && last.type === "box" && last.label === "Stand")) warns.push("Kapitel endet nicht mit der Stand-Box");
    if (!blocks.some((b) => b.type === "h3" && /^Quellen/.test(b.text))) errs.push("keine Überschrift „### Quellen und weiterführende Links“");
    if (count("Achtung") < 1) warns.push("keine Achtung-Box");
    if (blocks.filter((b) => b.type === "h3").length < 3) warns.push("weniger als 3 Zwischenüberschriften");
    if (count("Praxisbeispiel") > 2) warns.push("mehr als 2 Praxisbeispiele");
    const t = TARGET[num];
    if (t) {
      const ratio = words / t;
      if (ratio < 0.7) errs.push(`zu kurz: ${words} Wörter (Ziel ${t}, ≥ 70 % nötig)`);
      else if (ratio < 0.85) warns.push(`etwas kurz: ${words} Wörter (Ziel ${t})`);
      else if (ratio > 1.4) warns.push(`deutlich zu lang: ${words} Wörter (Ziel ${t})`);
      else if (ratio > 1.15) warns.push(`etwas lang: ${words} Wörter (Ziel ${t})`);
    }
  }
  if (errs.length) errorFiles++;
  rows.push({ f, words, target: isChapter ? TARGET[num] : "", errs, warns });
});

rows.forEach((r) => {
  const status = r.errs.length ? "FEHLER" : r.warns.length ? "warn  " : "ok    ";
  console.log(`${status} ${r.f.padEnd(62)} ${String(r.words).padStart(6)} W${r.target ? " / " + r.target : ""}`);
  r.errs.forEach((e) => console.log("       ✗ " + e));
  r.warns.forEach((w) => console.log("       · " + w));
});
console.log(`\n${rows.length} Dateien, ~${totalWords.toLocaleString("de-DE")} Wörter, ${errorFiles} Datei(en) mit Fehlern.`);
process.exit(errorFiles ? 1 : 0);
