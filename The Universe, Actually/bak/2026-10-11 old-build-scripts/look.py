import io,sys
import docx
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
ps=docx.Document('../The_Universe_Actually__REV11.docx').paragraphs
a,b=int(sys.argv[1]),int(sys.argv[2]); n=int(sys.argv[3]) if len(sys.argv)>3 else 400
for i in range(a,b): print(i,ps[i].text[:n]); 
