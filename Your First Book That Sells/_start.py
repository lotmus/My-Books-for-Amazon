from docx import Document

path = r"C:\Users\lomus\OneDrive\My Books for Amazon\Your First Book That Sells\First_Review_Kindle_Edition\Your_First_Book_That_Sells_Updated.docx"
doc = Document(path)
seen_heading = False
for para in doc.paragraphs:
    style = para.style.name if para.style else ""
    text = para.text.strip()
    if style == "Heading 1" and text == "Start here":
        seen_heading = True
        print("H1", text)
        continue
    if seen_heading and style == "Heading 1":
        break
    if seen_heading and text:
        print(text)
        print()
