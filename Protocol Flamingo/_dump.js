const fs = require("fs");
const JSZip = require("jszip");
const path = "C:\\Users\\lomus\\OneDrive\\My Books for Amazon\\Protocol Flamingo\\Protocol_Flamingo_Rev2.docx";
(async () => {
  const zip = await JSZip.loadAsync(fs.readFileSync(path));
  const xml = await zip.file("word/document.xml").async("string");
  const paras = xml.split(/<w:p[ >]/).slice(1);
  const out = [];
  paras.forEach((p, i) => {
    const style = (p.match(/<w:pStyle w:val="([^"]+)"/) || [])[1] || "";
    const texts = [...p.matchAll(/<w:t[^>]*>([^<]*)<\/w:t>/g)].map(m => m[1]);
    const t = texts.join("").replace(/&amp;/g, "&").replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&quot;/g, '"');
    if (!t.trim() && !style) return;
    out.push(String(i).padStart(4, "0") + "\t" + style + "\t" + t);
  });
  const sect = xml.match(/<w:sectPr[\s\S]*?<\/w:sectPr>/);
  fs.writeFileSync("_dump.txt", out.join("\n") + "\n\nSECT\n" + (sect ? sect[0] : "NONE"), "utf8");
  console.log("paras", paras.length, "kept", out.length);
})();
