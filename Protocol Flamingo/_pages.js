const fs = require("fs");
const JSZip = require("jszip");
(async () => {
  const zip = await JSZip.loadAsync(fs.readFileSync("Protocol_Flamingo_Rev2.docx"));
  const xml = await zip.file("word/document.xml").async("string");
  const end = xml.indexOf("</w:document>");
  let words = 0;
  let i = 0;
  while (i < end) {
    const a = xml.indexOf("<w:p ", i);
    const b = xml.indexOf("<w:p>", i);
    const start = a < 0 ? b : b < 0 ? a : Math.min(a, b);
    if (start < 0 || start > end) break;
    const e = xml.indexOf("</w:p>", start);
    const p = xml.slice(start, e);
    const t = [...p.matchAll(/<w:t[^>]*>([^<]*)<\/w:t>/g)].map((m) => m[1]).join(" ");
    words += t.split(/\s+/).filter(Boolean).length;
    i = e + 6;
  }
  const sect = xml.slice(xml.indexOf("<w:sectPr"), xml.indexOf("</w:sectPr>") + 10);
  console.log("words", words);
  console.log(sect.replace(/></g, ">\n<"));
})();
