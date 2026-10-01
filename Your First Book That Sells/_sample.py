from docx import Document

path = r"C:\Users\lomus\OneDrive\My Books for Amazon\Your First Book That Sells\First_Review_Kindle_Edition\Your_First_Book_That_Sells_Updated.docx"
doc = Document(path)
words = 0
paras = []
for para in doc.paragraphs:
    text = para.text.strip()
    if text:
        words += len(text.split())
        paras.append((para.style.name if para.style else "", text))
print("WORDS", words)
print("PARAS", len(paras))
print("--- START ---")
for style, text in paras[2:18]:
    print(style, "|", text[:400])
    print()
print("--- END ---")
for style, text in paras[-12:]:
    print(style, "|", text[:400])
    print()
