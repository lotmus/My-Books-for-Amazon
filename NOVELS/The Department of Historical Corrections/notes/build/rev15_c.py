P='../../The Department of Historical Corrections - REV15.md'
b=open(P,encoding='utf-8').read()
def rep(a,c):
    global b
    assert b.count(a)==1,(b.count(a),a[:70]); b=b.replace(a,c)
rep("It was the first honest notice the shop had displayed all week.","It was the most accurate sign the shop had ever carried.")
rep("The room smelled of damp coats and of the municipal polish used on every room in which people are made to wait.","Wet coats hung steaming on the radiator, and the polish was the municipal kind used on every room in which people are made to wait.")
rep("Perrott sat for a quarter of an hour without moving.","Perrott sat without moving until the pie went cold.")
open(P,'w',encoding='utf-8',newline='\n').write(b)
