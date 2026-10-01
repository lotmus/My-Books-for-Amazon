const fs = require("fs");
const JSZip = require("jszip");
(async () => {
  const zip = await JSZip.loadAsync(fs.readFileSync("Protocol_Flamingo_Rev2.docx"));
  const xml = await zip.file("word/document.xml").async("string");
  const end = xml.indexOf("</w:document>");
  const paras = [];
  let i = 0;
  while (i < end) {
    const a = xml.indexOf("<w:p ", i);
    const b = xml.indexOf("<w:p>", i);
    const start = a < 0 ? b : b < 0 ? a : Math.min(a, b);
    if (start < 0 || start > end) break;
    const e = xml.indexOf("</w:p>", start);
    const t = [...xml.slice(start, e).matchAll(/<w:t[^>]*>([^<]*)<\/w:t>/g)].map(m => m[1]).join("").replace(/&amp;/g, "&");
    paras.push(t);
    i = e + 6;
  }
  const keys = ["drugstore", "thumb found the napkin", "tickets came", "cold open", "What they grew", "infants bound", "They grew", "orange", "STARFALL", "sail", "Fort Wayne"];
  paras.forEach((t, n) => {
    if (keys.some(k => t.includes(k))) console.log("\n" + n + " " + t.slice(0, 400));
  });
  console.log("\nPARAS", paras.length, "WORDS", paras.join(" ").split(/\s+/).filter(Boolean).length);
})();
