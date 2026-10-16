import re
class Doc:
    def __init__(self,path):
        self.t=open(path,encoding='utf8').read()
        self.fail=[]
    def sub(self,old,new,count=1):
        n=self.t.count(old)
        if n<1 or (count and n!=count):
            self.fail.append((old[:70],n)); return
        self.t=self.t.replace(old,new)
    def after(self,anchor,new):
        # insert new paragraph(s) after paragraph that contains anchor
        paras=self.t.split('\n\n')
        idx=[i for i,p in enumerate(paras) if anchor in p]
        if len(idx)!=1: self.fail.append(('AFTER '+anchor[:60],len(idx))); return
        paras.insert(idx[0]+1,new.strip('\n')); self.t='\n\n'.join(paras)
    def before(self,anchor,new):
        paras=self.t.split('\n\n')
        idx=[i for i,p in enumerate(paras) if anchor in p]
        if len(idx)!=1: self.fail.append(('BEFORE '+anchor[:60],len(idx))); return
        paras.insert(idx[0],new.strip('\n')); self.t='\n\n'.join(paras)
    def cutp(self,start,new=None):
        paras=self.t.split('\n\n')
        idx=[i for i,p in enumerate(paras) if p.startswith(start)]
        if len(idx)!=1: self.fail.append(('CUTP '+start[:60],len(idx))); return
        if new is None: del paras[idx[0]]
        else: paras[idx[0]]=new
        self.t='\n\n'.join(paras)
    def cutrange(self,a,b,new=None):
        paras=self.t.split('\n\n')
        ia=[i for i,p in enumerate(paras) if p.startswith(a)]
        ib=[i for i,p in enumerate(paras) if p.startswith(b)]
        if len(ia)!=1 or len(ib)!=1 or ib[0]<=ia[0]: self.fail.append(('RANGE '+a[:40]+'|'+b[:40],(len(ia),len(ib)))); return
        rep=[] if new is None else [new]
        paras[ia[0]:ib[0]]=rep; self.t='\n\n'.join(paras)
    def save(self,path): open(path,'w',encoding='utf8').write(self.t)
