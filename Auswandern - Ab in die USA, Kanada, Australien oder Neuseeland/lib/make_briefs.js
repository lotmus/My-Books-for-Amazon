"use strict";
// Generates _Konzept/briefs/K<nn>.md: a short per-chapter brief (the chapter's
// entry from 01_Gliederung.md + a one-line index of all chapters for cross-
// references). Writers read this instead of the whole outline (saves tokens).
//   node lib/make_briefs.js
const fs = require("fs");
const path = require("path");
const root = path.join(__dirname, "..");
const text = fs.readFileSync(path.join(root, "_Konzept", "01_Gliederung.md"), "utf-8").replace(/\r\n?/g, "\n");
const lines = text.split("\n");

const entries = {};   // n -> {title, file, words, sheets, body}
let part = "";
for (let i = 0; i < lines.length; i++) {
  const pm = lines[i].match(/^## (TEIL .*)$/);
  if (pm) part = pm[1];
  const m = lines[i].match(/^\*\*K(\d+) · (.+?)\*\* — `(.+?)` — ([\d.]+) W — (.*)$/);
  if (!m) continue;
  const body = [lines[i]];
  for (let j = i + 1; j < lines.length && lines[j].trim() !== ""; j++) body.push(lines[j]);
  entries[+m[1]] = { title: m[2], file: m[3], words: m[4], sheets: m[5], body: body.join("\n"), part };
}

const index = Object.keys(entries).map(Number).sort((a, b) => a - b)
  .map((n) => `- Kapitel ${n}: ${entries[n].title}`).join("\n");

let hints = {};
try { hints = JSON.parse(fs.readFileSync(path.join(__dirname, "hints.json"), "utf-8")); } catch (e) { /* optional */ }
const outDir = path.join(root, "_Konzept", "briefs");
fs.mkdirSync(outDir, { recursive: true });
Object.keys(entries).forEach((k) => {
  const e = entries[k];
  const nn = String(k).padStart(2, "0");
  const content = [
    `# KAPITELBRIEF — Kapitel ${k}: ${e.title}`,
    ``,
    `Teil: ${e.part}`,
    `Datei: \`manuscript\\${e.file}\` · Wortziel: ${e.words} (±15 %) · Faktenblätter: ${e.sheets}`,
    ``,
    `## Vorgabe aus der Gliederung (verbindlich)`,
    e.body,
    ``,
    ...(hints[k] ? [`## Besondere Hinweise des Buchleiters (verbindlich)`, hints[k], ``] : []),
    `## Alle Kapitel (Nummern sind fest; nutze sie für „siehe Kapitel N“)`,
    index,
    ``,
    `Alle Kapitel und Teile stehen ausführlich in \`_Konzept\\01_Gliederung.md\` — lies dort nur bei Bedarf einzelne Einträge angrenzender Kapitel (Abgrenzung!).`,
    ``,
  ].join("\n");
  fs.writeFileSync(path.join(outDir, `K${nn}.md`), content, "utf-8");
});
console.log("wrote " + Object.keys(entries).length + " briefs to _Konzept/briefs/");
