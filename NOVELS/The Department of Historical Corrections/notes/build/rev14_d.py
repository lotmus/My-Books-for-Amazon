P='../../The Department of Historical Corrections - REV14.md'
b=open(P,encoding='utf-8').read()
def rep(a,c):
    global b
    assert b.count(a)==1,(b.count(a),a[:60]); b=b.replace(a,c)
def cut(s):
    global b
    assert b.count(s)==1,(b.count(s),s[:60]); i=b.index(s); j=b.index('\n\n',i)+2; b=b[:i]+b[j:]
cut("She thought of Arthur’s future, with its clean air")
cut("Mr Gant had quarrelled with Hester over a paper delivery")
rep("They printed forty copies. Hester sent ten to other printers, ten to booksellers, ten to men who enjoyed embarrassing private committees and ten to addresses likely to retain unusual correspondence. She kept no single master list with them. If Cresswell took one bundle, he would not find the rest through it.","They printed forty copies. Hester sent them out in four bundles of ten, to printers, booksellers, men who enjoyed embarrassing private committees and addresses likely to keep unusual correspondence, and kept no master list. If Cresswell took one bundle, he would not find the rest through it.")
rep("Towards four, Daniel fell asleep in a chair. Hester covered him with a coat and went outside. London was beginning another day. A baker carried trays through an open door. Somewhere a bell rang. The victory celebrations had left paper and broken glass in the gutters, and women were already sweeping both away.","Towards four, Daniel fell asleep in a chair. Hester covered him with a coat and went outside. A baker carried trays through an open door, and women were already sweeping the victory’s paper and broken glass out of the gutters.")
rep("She did not include the door in time. Not because it was untrue, but because it would allow every other fact to be dismissed as madness. Instead she described Arthur as a clerk who had witnessed the seizure and whose full account was retained separately.","She did not include the door in time, not because it was untrue but because it would let every other fact be dismissed as madness. Arthur appeared as a clerk who had witnessed the seizure, whose full account was held separately.")
open(P,'w',encoding='utf-8',newline='\n').write(b)
