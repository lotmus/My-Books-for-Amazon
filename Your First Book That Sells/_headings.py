from docx import Document

path = r"C:\Users\lomus\OneDrive\My Books for Amazon\Your First Book That Sells\First_Review_Kindle_Edition\Your_First_Book_That_Sells_Updated.docx"
doc = Document(path)
for para in doc.paragraphs:
    name = para.style.name if para.style is not None else ""
    if name in ("Title", "Subtitle") or name.startswith("Heading"):
        text = " ".join(para.text.split())
        if text:
            print(f"{name} | {text[:160]}")
