"use strict";
// Pre-digests the 42 finished chapters into compact source files for the
// appendix writers, so they don't each have to read 42 full chapters.
//   node lib/extract_digests.js
const fs = require("fs");
const path = require("path");
const P = require("./parse");
const MS = path.join(__dirname, "..", "manuscript");
const OUT = path.join(__dirname, "..", "_Konzept", "digests");
fs.mkdirSync(OUT, { recursive: true });

const files = fs.readdirSync(MS).filter((f) => /_K\d+_/.test(f)).sort((a, b) => {
  const na = +a.match(/_K(\d+)_/)[1], nb = +b.match(/_K(\d+)_/)[1];
  return na - nb;
});

const chapters = files.map((f) => {
  const raw = fs.readFileSync(path.join(MS, f), "utf-8");
  const blocks = P.parseMarkdown(raw);
  const h2 = blocks.find((b) => b.type === "h2");
  const m = h2.text.match(/^Kapitel\s+(\d+):\s+(.*)$/);
  return { num: +m[1], title: m[2], file: f, blocks, raw };
});

// ---------------------------------------------------------------- A: Checklisten
{
  const out = [];
  chapters.forEach((c) => {
    const walk = (bs) => bs.forEach((b) => {
      if (b.type === "box" && b.label === "Checkliste") {
        out.push(`### Kapitel ${c.num}: ${c.title}`);
        b.blocks.forEach((x) => { if (x.type === "list") x.items.forEach((it) => out.push("- [ ] " + P.stripInline(it.text))); });
        out.push("");
      }
      if (b.blocks) walk(b.blocks);
    });
    walk(c.blocks);
  });
  fs.writeFileSync(path.join(OUT, "checklisten_alle.md"), "# Alle Checklisten-Punkte, nach Kapitel\n\n" + out.join("\n"), "utf-8");
}

// ---------------------------------------------------------------- F: Quellen
{
  const out = [];
  chapters.forEach((c) => {
    const idx = c.blocks.findIndex((b) => b.type === "h3" && /^Quellen/.test(b.text));
    if (idx < 0) return;
    out.push(`### Kapitel ${c.num}: ${c.title}`);
    for (let i = idx + 1; i < c.blocks.length; i++) {
      const b = c.blocks[i];
      if (b.type === "h3" || b.type === "box") break;
      if (b.type === "list") b.items.forEach((it) => out.push("- " + P.stripInline(it.text)));
    }
    out.push("");
  });
  fs.writeFileSync(path.join(OUT, "quellen_alle.md"), "# Alle Quellenangaben, nach Kapitel\n\n" + out.join("\n"), "utf-8");
}

// ---------------------------------------------------------------- D: Formulare/Abkürzungen
{
  const formRe = /\b(I-\d{3}[A-Z]?|N-\d{3}|DS-\d{3}|SS-5|W-[47]|W-2|1040(?:-NR)?|8843|8938|8621|3520|SS-5|G-1055|EAD|ITIN|SSN|LCA|PERM|I-9|I-90|I-94|I-864|I-797|I-140|I-129|I-485|I-526E|I-829|I-407|8-K|AR-11)\b/g;
  const abbrevRe = /\b([A-ZÄÖÜ]{2,6}(?:-[A-ZÄÖÜ]{2,6})?)\b/g;
  const forms = new Map();
  chapters.forEach((c) => {
    const text = c.raw;
    let m;
    const re = new RegExp(formRe.source, "g");
    while ((m = re.exec(text))) {
      const key = m[1];
      if (!forms.has(key)) forms.set(key, new Set());
      forms.get(key).add(c.num);
    }
  });
  const out = ["# Formularnummern und Abkürzungen: Fundstellen (aus den Kapiteln extrahiert)", "", "Formular/Kürzel | Kapitel", "---|---"];
  [...forms.entries()].sort((a, b) => a[0].localeCompare(b[0])).forEach(([k, v]) => {
    out.push(`${k} | ${[...v].sort((a, b) => a - b).join(", ")}`);
  });
  fs.writeFileSync(path.join(OUT, "formulare_fundstellen.md"), out.join("\n"), "utf-8");
}

// ---------------------------------------------------------------- B: Glossar-Kandidaten (kursive Begriffe mit Erklärung)
{
  // Pattern in the manuscript: "*Begriff* (deutsche Erklärung)" or "*Begriff*, die/der/das deutsche Erklärung"
  const re = /\*([A-Za-zÀ-ž0-9 .\/&'’-]{2,40}?)\*\s*[,(]\s*([^).\n]{3,140})[).]/g;
  const terms = new Map();
  chapters.forEach((c) => {
    let m;
    const rre = new RegExp(re.source, "g");
    while ((m = rre.exec(c.raw))) {
      const term = m[1].trim();
      const gloss = m[2].trim();
      if (term.length < 2 || /^\d+$/.test(term)) continue;
      if (!terms.has(term)) terms.set(term, { gloss, chapters: new Set() });
      terms.get(term).chapters.add(c.num);
    }
  });
  const out = ["# Glossar-Kandidaten (automatisch aus *kursiv* + Erklärung extrahiert; Rohmaterial, muss redigiert werden)", "", "Begriff | Erklärung (Rohtext) | Kapitel", "---|---|---"];
  [...terms.entries()].sort((a, b) => a[0].localeCompare(b[0])).forEach(([k, v]) => {
    out.push(`${k} | ${v.gloss.replace(/\|/g, "/")} | ${[...v.chapters].sort((a, b) => a - b).join(",")}`);
  });
  fs.writeFileSync(path.join(OUT, "glossar_kandidaten.md"), out.join("\n"), "utf-8");
  console.log("Glossar-Kandidaten (roh):", terms.size);
}

// ---------------------------------------------------------------- G: Kapitelübersicht (Titel + Kurz-gesagt) für den Schnellfinder
{
  const out = [];
  chapters.forEach((c) => {
    out.push(`### Kapitel ${c.num}: ${c.title}`);
    const box = c.blocks.find((b) => b.type === "box" && b.label === "Kurz gesagt");
    if (box) box.blocks.forEach((x) => { if (x.type === "list") x.items.forEach((it) => out.push("- " + P.stripInline(it.text))); });
    out.push("");
  });
  fs.writeFileSync(path.join(OUT, "kapitel_kurzfassungen.md"), "# Kapitel-Kurzfassungen (Titel + Kurz-gesagt-Box)\n\n" + out.join("\n"), "utf-8");
}

console.log("Digests geschrieben nach " + path.relative(process.cwd(), OUT));
console.log(chapters.length + " Kapitel verarbeitet.");
