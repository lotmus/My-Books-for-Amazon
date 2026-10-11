import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='DejaVu Serif'
# 1 two ladders
fig,ax=plt.subplots(figsize=(8,4.6),dpi=100)
ax.set_xlim(-19,28); ax.set_ylim(-0.2,2.4); ax.axis('off')
def ladder(y,items,col,title):
    ax.annotate('',xy=(27.5,y),xytext=(-18.5,y),arrowprops=dict(arrowstyle='->',lw=1.6,color='#333'))
    ax.text(-18.5,y+0.42,title,fontsize=11,weight='bold',color=col,ha='left')
    for i,(x,lab) in enumerate(items):
        ax.plot([x],[y],'o',color=col,ms=7)
        ax.text(x,y+(0.12 if i%2==0 else -0.2),lab,ha='center',va='bottom' if i%2==0 else 'top',fontsize=8.2)
ladder(1.7,[(-18,'quark\n(<10⁻¹⁸ m)'),(-15,'proton\n10⁻¹⁵ m'),(-10,'atom\n10⁻¹⁰ m'),(-7,'molecule'),(0,'you\n1 m'),(7,'Earth\n10⁷ m'),(13,'Solar System\n10¹³ m'),(21,'galaxy\n10²¹ m'),(27,'observable\nuniverse 10²⁷ m')],'#1f4e9c','First arc (Parts I–VI): the physical world, small to large')
ladder(0.45,[(-9,'DNA\n2 nm wide'),(-6,'cell\n10⁻⁶–10⁻⁴ m'),(-1,'brain\n0.15 m'),(0.2,'body\n1.7 m'),(4,'forest,\nreef'),(7,'living planet\n10⁷ m'),(11,'technology reaching\nother worlds')],'#2e7d32','Second arc (Parts VII–XI): life, from the first cell to civilization')
ax.text(4.5,-0.15,'size in meters on a powers-of-ten scale; each tick is a factor of 1 000',ha='center',fontsize=8,style='italic',color='#555')
for x in range(-18,28,3): ax.plot([x,x],[1.66,1.74],color='#999',lw=0.8); ax.plot([x,x],[0.41,0.49],color='#999',lw=0.8)
plt.tight_layout(); plt.savefig('figures/fig1_two_arcs.png',dpi=100); plt.close()
# 2 cosmic timeline
import numpy as np
fig,(ax,bx)=plt.subplots(2,1,figsize=(8,5.6),dpi=100)
ev=[(5.4e-44,'Planck time:\nknown physics ends'),(1e-34,'inflation\n(if it happened)'),(1e-12,'electroweak\nforce splits'),(1e-5,'quarks bind into\nprotons, neutrons'),(180,'light nuclei form\n(first minutes)'),(1.6e12,'matter outweighs\nradiation')]
ax.set_xlim(-46,14); ax.set_ylim(-1.3,1.3); ax.axhline(0,color='#333',lw=1.5)
for i,(t,l) in enumerate(ev):
    xx=np.log10(t); up=1 if i%2==0 else -1
    ax.plot([xx,xx],[0,0.35*up],color='#b5651d',lw=1); ax.plot([xx],[0],'o',color='#b5651d',ms=6)
    ax.text(xx,0.4*up,l,ha='center',va='bottom' if up>0 else 'top',fontsize=8)
ax.set_yticks([]); ax.set_xticks(range(-45,15,5)); ax.set_xticklabels([f'10$^{{{v}}}$' for v in range(-45,15,5)],fontsize=8)
ax.set_xlabel('the first 50 000 years: seconds after the Big Bang (logarithmic scale)',fontsize=9)
for sp in ['top','right','left']: ax.spines[sp].set_visible(False)
ax.set_title('A timeline of the universe',fontsize=11,weight='bold')
ev2=[(0.00038,'atoms form; microwave\nbackground released'),(0.2,'first stars'),(1.0,'reionization\ncomplete'),(3.5,'cosmic star\nformation peaks'),(7.8,'expansion starts\nto accelerate'),(9.2,'Sun and Earth\nform'),(13.8,'today')]
bx.set_xlim(-3.2,14.8); bx.set_ylim(-1.3,1.3); bx.axhline(0,color='#333',lw=1.5)
for i,(t,l) in enumerate(ev2):
    up=1 if i%2==0 else -1
    bx.plot([t,t],[0,0.35*up],color='#1f4e9c',lw=1); bx.plot([t],[0],'o',color='#1f4e9c',ms=6)
    ha={0:'right',2:'left'}.get(i,'center')
    bx.text(t+(0.15 if i==0 else (-0.1 if i==2 else 0)),0.4*up,l,ha=ha,va='bottom' if up>0 else 'top',fontsize=8)
bx.set_yticks([]); bx.set_xticks(range(0,15,2)); bx.tick_params(labelsize=8)
bx.set_xlabel('the rest of the story: billions of years after the Big Bang (linear scale)',fontsize=9)
for sp in ['top','right','left']: bx.spines[sp].set_visible(False)
plt.tight_layout(); plt.savefig('figures/fig2_cosmic_timeline.png',dpi=100); plt.close()
# 3 Standard Model chart
fig,ax=plt.subplots(figsize=(8,5.2),dpi=100); ax.set_xlim(0,8); ax.set_ylim(0,5.2); ax.axis('off')
cells=[('u','up','2.2 MeV',0,3,'#f3c99a'),('c','charm','1.27 GeV',1,3,'#f3c99a'),('t','top','173 GeV',2,3,'#f3c99a'),
('d','down','4.7 MeV',0,2,'#f3c99a'),('s','strange','93 MeV',1,2,'#f3c99a'),('b','bottom','4.18 GeV',2,2,'#f3c99a'),
('e','electron','0.511 MeV',0,1,'#b9d7f0'),('μ','muon','106 MeV',1,1,'#b9d7f0'),('τ','tau','1.78 GeV',2,1,'#b9d7f0'),
('νₑ','e-neutrino','< 0.45 eV',0,0,'#b9d7f0'),('ν_μ','μ-neutrino','< 0.45 eV',1,0,'#b9d7f0'),('ν_τ','τ-neutrino','< 0.45 eV',2,0,'#b9d7f0'),
('g','gluon','0',3.3,3,'#c8e6c0'),('γ','photon','0',3.3,2,'#c8e6c0'),('Z','Z boson','91.2 GeV',3.3,1,'#c8e6c0'),('W','W boson','80.4 GeV',3.3,0,'#c8e6c0'),('H','Higgs','125 GeV',4.6,1.5,'#f0e08a')]
for sym,name,m,cx,cy,col in cells:
    X=0.3+cx*1.2; Y=0.3+cy*1.1
    ax.add_patch(plt.Rectangle((X,Y),1.1,1.0,fc=col,ec='#555'))
    ax.text(X+0.55,Y+0.55,sym.replace('ν_μ','ν$_μ$').replace('ν_τ','ν$_τ$'),ha='center',va='center',fontsize=17,weight='bold')
    ax.text(X+0.55,Y+0.2,name,ha='center',fontsize=7.5); ax.text(X+0.55,Y+0.82,m,ha='center',fontsize=7)
ax.text(0.3+0.55,4.85,'I',ha='center',fontsize=10,weight='bold'); ax.text(1.5+0.55,4.85,'II',ha='center',fontsize=10,weight='bold'); ax.text(2.7+0.55,4.85,'III',ha='center',fontsize=10,weight='bold')
ax.text(1.95,5.05,'three generations of matter (fermions)',ha='center',fontsize=9)
ax.text(4.86,5.05,'force carriers',ha='center',fontsize=9); ax.text(6.4,3.35,'Higgs boson',ha='center',fontsize=9)
ax.text(0.15,3.5,'quarks',color='#a0522d',fontsize=9,rotation=90,ha='center',va='center'); ax.text(0.15,1.4,'leptons',color='#1f4e9c',fontsize=9,rotation=90,ha='center',va='center')
ax.text(5.9,0.5,'masses: particle-data values, rounded;\nneutrino limit from direct measurement',fontsize=7,style='italic')
plt.tight_layout(); plt.savefig('figures/fig3_standard_model.png',dpi=100); plt.close()
