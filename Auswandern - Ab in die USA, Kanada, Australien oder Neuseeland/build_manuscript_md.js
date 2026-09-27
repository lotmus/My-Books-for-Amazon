// Combines manuscript/*.md into a single build/<title>.manuscript.md for easy reading/editing.
//   node build_manuscript_md.js [--dir manuscript] [--out build/<title>.manuscript.md]
"use strict";

const fs = require("fs");
const path = require("path");
const P = require("./lib/parse");

const ROOT = __dirname;

function argVal(flag, def) {
  const i = process.argv.indexOf(flag);
  return i !== -1 && process.argv[i + 1] ? process.argv[i + 1] : def;
}

const MS_DIR = path.resolve(ROOT, argVal("--dir", "manuscript"));
const book = JSON.parse(fs.readFileSync(path.join(ROOT, "book.json"), "utf8"));
const defaultOut = path.join("build", `${book.title} - ${book.subtitle}`.replace(/[\\/:*?"<>|]/g, "") + ".manuscript.md");
const OUT = path.resolve(ROOT, argVal("--out", defaultOut));

const files = P.listManuscriptFiles(MS_DIR);

const parts = [
  `# ${book.title} – ${book.subtitle}`,
  ``,
  `_Stand: ${book.stand} · Autor: ${book.author}_`,
  ``,
  `> Automatisch aus \`manuscript/*.md\` zusammengeführt (${files.length} Dateien). Nicht direkt als Bauquelle verwenden — Änderungen bitte in den Einzeldateien unter \`manuscript/\` vornehmen und dieses Dokument neu erzeugen mit \`node build_manuscript_md.js\`.`,
  ``,
  `---`,
];

for (const file of files) {
  const content = fs.readFileSync(path.join(MS_DIR, file), "utf8").trimEnd();
  parts.push(``, `<!-- Datei: ${file} -->`, ``, content, ``, `---`);
}

fs.mkdirSync(path.dirname(OUT), { recursive: true });
fs.writeFileSync(OUT, parts.join("\n") + "\n", "utf8");

console.log(`Geschrieben: ${path.relative(ROOT, OUT)} (${files.length} Kapiteldateien)`);
