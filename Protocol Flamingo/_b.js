const fs = require("fs");
const JSZip = require("jszip");
(async () => {
  const zip = await JSZip.loadAsync(fs.readFileSync("Protocol_Flamingo_Rev2.docx"));
  const xml = await zip.file("word/document.xml").async("string");
  const end = xml.indexOf("</w:document>");
  console.log("doc len", xml.length, "end", end, "after", xml.length - end);
  console.log(xml.slice(end, end + 80));
  const tail = xml.slice(end);
  const paras = tail.split(/<w:p[ >]/).length - 1;
  console.log("paras after document", paras);
  console.log("TAIL END", xml.slice(-300));
})();
