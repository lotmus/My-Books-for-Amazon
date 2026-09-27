"use strict";
// Builds build/Auswandern - Ab in die USA, Kanada, Australien oder Neuseeland.epub (Kindle/e-reader edition) via pandoc.
//   node build_epub.js [--dir manuscript] [--out build/Auswandern - Ab in die USA, Kanada, Australien oder Neuseeland.epub]
// Preprocesses the book's Markdown subset into pandoc Markdown: labeled
// blockquotes become styled <div>s, checklist items become plain paragraphs
// with a box glyph, front-matter directives are dropped.
const fs = require("fs");
const path = require("path");
const { spawnSync } = require("child_process");
const P = require("./lib/parse");

const args = process.argv.slice(2);
const argVal = (n, d) => { const i = args.indexOf(n); return i >= 0 && args[i + 1] ? args[i + 1] : d; };
const ROOT = __dirname;
const MS_DIR = path.resolve(ROOT, argVal("--dir", "manuscript"));
const OUT = path.resolve(ROOT, argVal("--out", "build/Auswandern - Ab in die USA, Kanada, Australien oder Neuseeland.epub"));
const BOOK = JSON.parse(fs.readFileSync(path.join(ROOT, "book.json"), "utf-8"));
const BUILD = path.join(ROOT, "build");
fs.mkdirSync(BUILD, { recursive: true });

const slug = (s) => s.toLowerCase().replace(/[^a-zäöüß]+/g, "-").replace(/-+$/g, "");

function transform(text) {
  const lines = text.replace(/^﻿/, "").replace(/\r\n?/g, "\n").split("\n");
  const out = [];
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const t = line.trim();
    if (/^%%[A-Z]+%%$/.test(t)) continue;                  // directives
    if (t.startsWith(">")) {                                 // blockquote / box
      const group = [];
      while (i < lines.length && lines[i].trim().startsWith(">")) { group.push(lines[i].replace(/^\s*>\s?/, "")); i++; }
      i--;
      const first = group.findIndex((l) => l.trim() !== "");
      const m = first >= 0 ? group[first].trim().match(/^\*\*(.+?):\*\*\s*(.*)$/) : null;
      out.push("");
      if (m) {
        group[first] = m[2];
        out.push(`::: {.box .box-${slug(m[1])}}`, "", `**${m[1].toUpperCase()}**`, "");
      } else out.push("::: {.quote}", "");
      // checklist items -> paragraphs with a box glyph; other lines pass through
      group.forEach((l) => {
        const cm = l.match(/^(\s*)[-*]\s+\[( |x|X)\]\s+(.*)$/);
        if (cm) { out.push("", (cm[2] === " " ? "☐ " : "☑ ") + cm[3], ""); } else out.push(l);
      });
      out.push("", ":::", "");
      continue;
    }
    const cm = line.match(/^(\s*)[-*]\s+\[( |x|X)\]\s+(.*)$/);
    if (cm) { out.push("", (cm[2] === " " ? "☐ " : "☑ ") + cm[3], ""); continue; }
    out.push(line);
  }
  return P.typo(out.join("\n"));
}

const files = fs.readdirSync(MS_DIR).filter((f) => f.endsWith(".md") && !f.startsWith("_")).sort();
const body = files.map((f) => transform(fs.readFileSync(path.join(MS_DIR, f), "utf-8"))).join("\n\n");
const src = path.join(BUILD, "epub_src.md");
fs.writeFileSync(src, body, "utf-8");

const css = `
body { font-family: serif; line-height: 1.4; }
h1 { text-align: center; margin: 3em 0 1em; }
h2 { margin-top: 1.5em; }
h3 { margin-top: 1.4em; }
p { margin: 0.6em 0; }
table { width: 100%; border-collapse: collapse; font-size: 0.9em; margin: 1em 0; }
th, td { border: 1px solid #b8bec7; padding: 0.3em 0.5em; vertical-align: top; text-align: left; }
th { background: #dde3ea; }
.box { border-left: 0.35em solid #6b7280; background: #f2f3f5; padding: 0.4em 0.8em; margin: 1em 0; font-size: 0.95em; }
.box > p:first-child { font-size: 0.75em; letter-spacing: 0.15em; margin-bottom: 0.2em; }
.box-kurz-gesagt { border-color: #1f3a5f; background: #ecf1f7; }
.box-achtung { border-color: #9b2c2c; background: #faeeee; }
.box-spartipp { border-color: #2f6b3b; background: #edf6ef; }
.box-merke { border-color: #8a6212; background: #fbf5e4; }
.box-praxisbeispiel { border-color: #4a5568; background: #f0f2f5; }
.box-checkliste { border-color: #1f6f78; background: #ebf5f6; }
`;
fs.writeFileSync(path.join(BUILD, "epub.css"), css, "utf-8");

const meta = [
  "---",
  `title: "${BOOK.title} – ${BOOK.subtitle}"`,
  `author: "${BOOK.author}"`,
  `lang: ${BOOK.language}`,
  `date: "${BOOK.year}"`,
  `rights: "© ${BOOK.year} ${BOOK.author}"`,
  `description: "${BOOK.tagline.replace(/"/g, "'")}"`,
  "---", "",
].join("\n");
fs.writeFileSync(src, meta + body, "utf-8");

const r = spawnSync("pandoc", [
  src, "-o", OUT, "-f", "markdown+pipe_tables+fenced_divs-smart", "-t", "epub3",
  "--toc", "--toc-depth=2", "--split-level=2", "--css", path.join(BUILD, "epub.css"),
], { stdio: "inherit" });
if (r.status !== 0) { console.error("pandoc failed"); process.exit(1); }
console.log("wrote " + path.relative(ROOT, OUT));
