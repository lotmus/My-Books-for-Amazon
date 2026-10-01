from docx import Document

path = r"C:\Users\lomus\OneDrive\My Books for Amazon\Your First Book That Sells\First_Review_Kindle_Edition\Your_First_Book_That_Sells_Updated.docx"
doc = Document(path)
rows = [(p.style.name, p.text.strip()) for p in doc.paragraphs if p.text.strip()]
# contents window
for i, (style, text) in enumerate(rows):
    if text.startswith("12 Copy"):
        for style2, text2 in rows[i:i+6]:
            print(f"TOC {style2} | {text2}")
        break
print("--- CHAPTER ---")
start = max(i for i, (s, t) in enumerate(rows) if t == "15 Write one kind of book")
for style, text in rows[start:start+20]:
    print(f"{style} | {text[:220]}")
print("--- POINTER COUNT ---")
blob = "\n".join(t for _, t in rows)
print(blob.count("chapter 15"))
print(blob.count("If the manuscript is not written yet"))
