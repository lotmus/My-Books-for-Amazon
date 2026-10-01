const fs = require("fs");
const JSZip = require("jszip");
(async () => {
  const zip = await JSZip.loadAsync(fs.readFileSync("Protocol_Flamingo_Rev2.docx"));
  const xml = await zip.file("word/document.xml").async("string");
  const settings = await zip.file("word/settings.xml").async("string");
  const rels = await zip.file("word/_rels/document.xml.rels").async("string");
  const end = xml.indexOf("</w:document>");
  console.log("after document", xml.length - end - "</w:document>".length);
  console.log("height", (xml.match(/w:h="\d+"/g) || []).join(","));
  console.log("gutter", (xml.match(/w:gutter="\d+"/g) || []).join(","));
  console.log("roman", xml.includes("lowerRoman"), "decimal", xml.includes('w:fmt="decimal"'));
  console.log("mirror", settings.includes("mirrorMargins"));
  console.log("nature doi", rels.includes("10.1038/186670a0"));
  console.log("sciencedirect", rels.includes("sciencedirect"));
  const paras = [];
  let i = 0;
  while (i < xml.length) {
    const a = xml.indexOf("<w:p ", i);
    const b = xml.indexOf("<w:p>", i);
    let start = a < 0 ? b : b < 0 ? a : Math.min(a, b);
    if (start < 0 || start > end) break;
    const e = xml.indexOf("</w:p>", start);
    const p = xml.slice(start, e + 6);
    const t = [...p.matchAll(/<w:t[^>]*>([^<]*)<\/w:t>/g)].map(m => m[1]).join("")
      .replace(/&amp;/g, "&").replace(/&lt;/g, "<");
    if (t.trim()) paras.push(t);
    i = e + 6;
  }
  const heads = paras.filter(t => /^(THE INVASION|PROTOCOL|A NOTE|THE PEOPLE|CONTENTS|BOOK |TWO PEOPLE|The |Brussels|Starfall|GLOSSARY|APPENDIX|BIBLIOGRAPHY|ALSO BY|ABOUT THE|I\.|XI\.|XII\.|A Note|Glossary|Appendix|Bibliography|Also by|About the)/.test(t));
  console.log("---HEADS---");
  paras.forEach((t, n) => {
    if (/Heading/.test("")) return;
  });
  const want = ["THE INVASION STORYBOOKS", "CONTENTS", "BOOK ONE", "The Best Man Speech", "The Pretzel Corridor", "A NOTE TO THE READER", "THE PEOPLE WHO LOOKED UP", "A NOTE ON THE COUSINS", "GLOSSARY", "APPENDIX: THE SCIENCE THIS BOOK", "BIBLIOGRAPHY", "ALSO BY GEORGE HERBERT FONTAINE", "ABOUT THE AUTHOR"];
  for (const w of want) {
    const at = paras.findIndex(t => t.startsWith(w));
    console.log(String(at).padStart(4), w);
  }
  const book = paras.findIndex(t => t === "BOOK ONE");
  const note = paras.findIndex(t => t === "A NOTE TO THE READER");
  console.log("book before note", book < note, book, note);
  const bad = ["A STORYBOOK OF NO SERIES AT ALL", "XI. Biology", "the same lesson Feld had spent an hour", "He was built the way work builds a person", "Halo Systems sold the world orbital internet from a campus"];
  for (const b of bad) console.log("BAD", paras.some(t => t.includes(b)), b.slice(0, 40));
  const good = ["You don\u2019t get to spend him", "Nobody had asked her", "the hours had been taken", "Steve smells the same marker", "The retellings are still to come", "Get me Kade", "a louder way of not asking", "Not as your file"];
  for (const g of good) console.log("GOOD", paras.some(t => t.includes(g)), g.slice(0, 40));
  // print the joins
  function around(needle) {
    const n = paras.findIndex(t => t.includes(needle));
    console.log("\n==", needle, n);
    for (let k = Math.max(0, n - 1); k <= n + 1 && k < paras.length; k++) {
      console.log("---", paras[k].slice(0, 280));
    }
  }
  around("face suggested a great deal");
  around("The gift shop sold");
  around("get to spend him");
  around("Nobody had asked her");
  around("hours had been taken");
  around("She said his name");
  around("Nature 186");
})();
