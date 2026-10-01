from docx import Document

path = r"C:\Users\lomus\OneDrive\My Books for Amazon\Your First Book That Sells\First_Review_Kindle_Edition\Your_First_Book_That_Sells_Updated.docx"
doc = Document(path)
capture = False
n = 0
for para in doc.paragraphs:
    text = para.text.strip()
    style = para.style.name if para.style else ""
    if text.startswith("1 Define"):
        capture = True
    if text.startswith("2 Make"):
        break
    if capture and text:
        n += 1
        print(style, "|", text)
        print()
print("COUNT", n)
