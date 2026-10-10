// Checks the built book for repeated sentences (Lothar's rule, 2026-10-04: no sentence appears twice anywhere in
// the book). Run after a build, from anywhere: node scripts/check_repeats.js [folder-of-docx]
// It reads chapters/*.docx and reports, outside the deliberate devices listed in ALLOWED:
//   1. exact duplicate sentences of three or more words,
//   2. runs of seven or more words shared by two places,
//   3. near-duplicate sentences (word-order similarity of 0.7 or more, eight or more words each),
//   4. in Notes and Sources, entries that are identical (its citation tails legitimately repeat imprints).
// Exit code 1 means something was flagged. "jszip" comes with the docx package.
const fs = require("fs");
const path = require("path");
process.chdir(path.join(__dirname, ".."));
const JSZip = require("jszip");

const DIR = process.argv[2] || "chapters";
const SKIP_FILES = [/^Also by/];            // a list of titles
const NOTES_FILE = /^Notes and Sources/;    // citations: entry-level check only
const RUN = 7;                              // words in a shared run
const NEAR = 0.7;                           // similarity for near-duplicates
const MIN_NEAR_WORDS = 8;

// Deliberate devices, normalized (lowercase, letters and digits only). A finding is dropped when it is one of these.
const ALLOWED = [
  "professor click click whoosh in the margin",             // lead-in for the Professor's margin notes
  "from the minutes of the society on the question of",     // label for the Society-minutes scenes
  "that all men are created equal",                         // Jefferson's phrase, echoed on purpose
];
const ALLOWED_EXACT = [
  "50 000 years",                                           // Timeline label shared by two events
];

const ABBR = /\b(Mr|Mrs|Ms|Dr|St|Jr|Sr|vs|etc|No|Fig|Vol|Ch|ed|eds|cf|ca|approx|Mt|Gen|Col|Lt|Capt|Sgt|Rev|Prof|U\.S|U\.K|e\.g|i\.e)\./g;
const key = s => s.normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase()
  .replace(/[^a-z0-9 ]/g, " ").replace(/\s+/g, " ").trim();
const words = k => (k ? k.split(" ") : []);
const decode = s => s.replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&quot;/g, '"').replace(/&apos;/g, "'")
  .replace(/&#(\d+);/g, (_, n) => String.fromCharCode(+n)).replace(/&amp;/g, "&");

function sentences(text) {
  const t = text.replace(ABBR, "$1\u0001").replace(/\b([A-Z])\.(?=\s*[A-Z])/g, "$1\u0001").replace(/(\d)\.(\d)/g, "$1\u0001$2");
  return t.split(/(?<=[.!?])["”’')\]]*\s+(?=["“‘'(]?[A-Z0-9])/)
    .map(s => s.replace(/\u0001/g, ".").trim()).filter(Boolean);
}

async function paragraphs(file) {
  const zip = await JSZip.loadAsync(fs.readFileSync(file));
  const xml = await zip.file("word/document.xml").async("string");
  return xml.split("</w:p>").map(p =>
    decode([...p.matchAll(/<w:t(?:\s[^>]*)?>([^<]*)<\/w:t>/g)].map(m => m[1]).join(""))).filter(Boolean);
}

const allowed = k => ALLOWED.some(a => k.includes(a));
function lcsRatio(a, b) {
  let prev = new Array(b.length + 1).fill(0);
  for (let i = 1; i <= a.length; i++) {
    const cur = [0];
    for (let j = 1; j <= b.length; j++) cur[j] = a[i - 1] === b[j - 1] ? prev[j - 1] + 1 : Math.max(prev[j], cur[j - 1]);
    prev = cur;
  }
  return (2 * prev[b.length]) / (a.length + b.length);
}

(async () => {
  const files = fs.readdirSync(DIR).filter(f => f.endsWith(".docx") && !SKIP_FILES.some(r => r.test(f))).sort();
  const rows = [];      // {loc, text, k, w}
  const notes = [];     // {loc, k}
  for (const f of files) {
    const label = /^\d\d - /.test(f) ? f.slice(0, 2) : f.slice(0, 14).trim();
    const paras = await paragraphs(path.join(DIR, f));
    paras.forEach((p, i) => {
      if (i === 0) return;   // the chapter heading
      if (NOTES_FILE.test(f)) { notes.push({ loc: `${label}:${i}`, k: key(p), text: p }); return; }
      for (const s of sentences(p)) rows.push({ loc: `${label}:${i}`, text: s, k: key(s), w: words(key(s)) });
    });
  }
  console.log(`${files.length} files, ${rows.length} sentences scanned (plus ${notes.length} notes entries)`);
  let flagged = 0;

  // 1. exact duplicates
  const by = new Map();
  for (const r of rows) if (r.w.length >= 3) (by.get(r.k) || by.set(r.k, []).get(r.k)).push(r);
  for (const [k, v] of by) {
    if (v.length < 2 || ALLOWED_EXACT.includes(k) || allowed(k)) continue;
    flagged++; console.log(`EXACT   ${v.map(r => r.loc).join(" | ")}\n        ${v[0].text.slice(0, 200)}`);
  }

  // 2. runs of RUN or more words in two or more places
  const grams = new Map();
  for (const r of rows) for (let i = 0; i + RUN <= r.w.length; i++) {
    const g = r.w.slice(i, i + RUN).join(" ");
    (grams.get(g) || grams.set(g, new Set()).get(g)).add(r.loc);
  }
  const reps = [...grams].filter(([, locs]) => locs.size > 1).map(([g, locs]) => ({ g, locs: [...locs].sort() }));
  const merged = [];   // overlapping runs in the same places become one phrase
  for (const { g, locs } of reps) {
    const last = merged[merged.length - 1];
    if (last && last.locs.join() === locs.join() && last.tail === g.split(" ").slice(0, -1).join(" ")) {
      last.g += " " + g.split(" ").pop(); last.tail = g.split(" ").slice(1).join(" ");
    } else merged.push({ g, locs, tail: g.split(" ").slice(1).join(" ") });
  }
  for (const { g, locs } of merged) {
    if (ALLOWED.some(a => a.includes(g) || g.includes(a))) continue;
    flagged++; console.log(`RUN     ${locs.join(" | ")}\n        ...${g}...`);
  }

  // 3. near-duplicate sentences
  const cand = rows.filter(r => r.w.length >= MIN_NEAR_WORDS);
  const sets = cand.map(r => new Set(r.w));
  for (let a = 0; a < cand.length; a++) for (let b = a + 1; b < cand.length; b++) {
    const A = cand[a], B = cand[b];
    if (A.k === B.k) continue;   // exact duplicates are reported above
    if (Math.min(A.w.length, B.w.length) / Math.max(A.w.length, B.w.length) < 0.6) continue;
    let inter = 0; for (const x of sets[a]) if (sets[b].has(x)) inter++;
    if (inter / (sets[a].size + sets[b].size - inter) < 0.45) continue;
    const r = lcsRatio(A.w, B.w);
    if (r < NEAR || (allowed(A.k) && allowed(B.k))) continue;
    flagged++; console.log(`NEAR    ${r.toFixed(2)}  ${A.loc} <-> ${B.loc}\n        A: ${A.text.slice(0, 200)}\n        B: ${B.text.slice(0, 200)}`);
  }

  // 4. identical notes entries
  const nb = new Map();
  for (const n of notes) (nb.get(n.k) || nb.set(n.k, []).get(n.k)).push(n);
  for (const [, v] of nb) if (v.length > 1) { flagged++; console.log(`NOTES   ${v.map(n => n.loc).join(" | ")}\n        ${v[0].text.slice(0, 200)}`); }

  console.log(flagged ? `\n${flagged} finding(s). Rewrite one side of each, or add a deliberate device to ALLOWED.` : "\nNo repeated sentences found.");
  process.exit(flagged ? 1 : 0);
})();
