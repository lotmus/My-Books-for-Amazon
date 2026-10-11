import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, numpy as np
from matplotlib.patches import FancyBboxPatch, Rectangle, Polygon, FancyArrowPatch
plt.rcParams['font.family']='DejaVu Serif'
# ---- EM spectrum
fig,ax=plt.subplots(figsize=(8,4.4),dpi=100); ax.set_xlim(-13,3.3); ax.set_ylim(-2.2,2.6); ax.axis('off')
bands=[(-13,-11,'gamma rays','#6a3d9a'),(-11,-8,'X-rays','#3f51b5'),(-8,np.log10(4e-7),'ultra-\nviolet','#7e57c2'),(np.log10(7e-7),-3,'infrared','#c62828'),(-3,-1,'micro-\nwaves','#ef6c00'),(-1,3.3,'radio','#8d6e63')]
for a,b,l,c in bands:
    ax.add_patch(Rectangle((a,0),b-a,0.8,color=c,alpha=0.85,lw=0)); ax.text((a+b)/2,0.4,l,ha='center',va='center',color='white',fontsize=8.5,weight='bold')
vis=np.linspace(np.log10(4e-7),np.log10(7e-7),40)
cm=plt.get_cmap('turbo')
for i in range(len(vis)-1): ax.add_patch(Rectangle((vis[i],0),vis[i+1]-vis[i],0.8,color=cm(0.12+0.8*i/len(vis)),lw=0))
ax.annotate('visible light\n400–700 nm',xy=(np.log10(5.5e-7),0.8),xytext=(np.log10(5.5e-7),1.9),ha='center',fontsize=8.5,arrowprops=dict(arrowstyle='->',lw=0.9))
for e in range(-12,4,3):
    ax.plot([e,e],[-0.05,-0.15],color='#333',lw=0.8); ax.text(e,-0.22,f'10$^{{{e}}}$ m',ha='center',va='top',fontsize=8)
    f=3e8/10**e; ax.text(e,1.0,f'{f:.0e} Hz'.replace('e+','×10^').replace('×10^0','×10^'),ha='center',fontsize=7,color='#444') if False else None
ax.text(-13,-0.62,'wavelength',fontsize=8.5,style='italic',color='#333')
for e in range(-12,4,3):
    f=3e8/10**e; ex=int(np.floor(np.log10(f)+1e-9)); m=f/10**ex
    ax.text(e,1.02,f'{m:.0f}×10$^{{{ex}}}$ Hz',ha='center',fontsize=7.2,color='#444')
ax.text(-13,1.3,'frequency',fontsize=8.5,style='italic',color='#333')
ex=[(-14.6+0.5,'nucleus'),(-10,'atom'),(-5,'cell'),(-2.5,'flea'),(0,'person'),(2,'building')]
ex=[(-10,'atom'),(-7,'virus'),(-5,'bacterium'),(-2.5,'grain of\nsand'),(0,'person'),(2.3,'stadium')]
for x,l in ex: ax.text(x,-1.05,l,ha='center',va='top',fontsize=7.8,color='#1b5e20')
ax.text(-13,-0.85,'about the size of:',fontsize=7.5,style='italic',color='#1b5e20')
notes=[(-11.5,'nuclear decay'),(-9.5,'medical X-rays'),(-7.0,'sunburn'),(-5.0,'heat cameras'),(np.log10(1.06e-3),'cosmic background\npeak ~1 mm'),(np.log10(0.125),'Wi-Fi, ovens\n~12 cm'),(1.3,'FM radio ~3 m;\nAM ~300 m')]
for x,l in notes: ax.text(x,-1.75,l,ha='center',va='top',fontsize=7.2,color='#333')
ax.text(-13,-1.55,'examples:',fontsize=7.5,style='italic')
ax.set_title('The electromagnetic spectrum: one kind of wave, many wavelengths',fontsize=10.5,weight='bold')
ax.text(-5,2.35,'← shorter wavelength: higher frequency, more energy per photon',ha='center',fontsize=8,color='#555')
plt.tight_layout(); plt.savefig('fig/fig4_em_spectrum.png',dpi=100); plt.close()

# ---- stellar life cycle
fig,ax=plt.subplots(figsize=(8,5.2),dpi=100); ax.set_xlim(0,10); ax.set_ylim(0,6.6); ax.axis('off')
def box(x,y,t,c,w=1.75,h=0.78):
    ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle='round,pad=0.03,rounding_size=0.12',fc=c,ec='#333',lw=0.9)); ax.text(x,y,t,ha='center',va='center',fontsize=8.2)
def arr(a,b,t=None,off=(0,0)):
    ax.annotate('',xy=b,xytext=a,arrowprops=dict(arrowstyle='->',lw=1.2,color='#333'))
    if t: ax.text((a[0]+b[0])/2+off[0],(a[1]+b[1])/2+off[1],t,fontsize=7.4,ha='center',color='#444',style='italic')
box(1.1,5.7,'cloud of gas\nand dust','#e0e0e0'); box(3.2,5.7,'protostar','#ffe0b2'); box(5.6,5.7,'main-sequence star\n(fuses hydrogen)','#fff59d',w=2.2)
arr((2.0,5.7),(2.3,5.7)); arr((4.1,5.7),(4.5,5.7))
box(8.6,5.7,'brown dwarf\n(never ignites)','#bcaaa4',w=1.9); ax.annotate('',xy=(7.65,5.95),xytext=(3.5,6.12),arrowprops=dict(arrowstyle='->',lw=1,color='#777',connectionstyle='arc3,rad=-0.25')); ax.text(5.6,6.5,'below 0.08 solar masses',fontsize=7.4,ha='center',style='italic',color='#444')
# low mass branch
box(2.4,3.6,'red giant','#ffab91'); box(2.4,2.1,'planetary nebula\n(outer layers lost)','#b3e5fc',w=2.0); box(2.4,0.6,'white dwarf\n(Earth-sized)','#eceff1',w=1.9)
arr((5.0,5.3),(2.9,4.0),'up to about 8\nsolar masses (the Sun)',(-0.6,0.15)); arr((2.4,3.2),(2.4,2.5)); arr((2.4,1.7),(2.4,1.0))
# high mass
box(7.4,3.6,'red supergiant\n(fuses up to iron)','#ef9a9a',w=2.1); box(7.4,2.1,'core-collapse\nsupernova','#ffcc80',w=1.9)
box(6.0,0.6,'neutron star\n(~25 km across)','#c5cae9',w=1.9); box(8.8,0.6,'black hole','#424242',w=1.6); ax.texts[-1].set_color('white')
arr((6.2,5.3),(7.1,4.0),'more than about\n8 solar masses',(0.75,0.15)); arr((7.4,3.2),(7.4,2.5)); arr((7.0,1.7),(6.3,1.0)); arr((7.8,1.7),(8.5,1.0))
ax.text(5.15,1.25,'lighter cores',fontsize=7.2,style='italic',color='#444'); ax.text(8.6,1.35,'heaviest cores',fontsize=7.2,style='italic',color='#444')
ax.annotate('',xy=(1.15,5.3),xytext=(6.4,1.95),arrowprops=dict(arrowstyle='->',lw=0.9,ls='--',color='#2e7d32',connectionstyle='arc3,rad=-0.35'))
ax.annotate('',xy=(0.9,5.3),xytext=(1.6,2.1),arrowprops=dict(arrowstyle='->',lw=0.9,ls='--',color='#2e7d32',connectionstyle='arc3,rad=0.3'))
ax.text(4.35,3.55,'ejected gas, enriched\nwith heavy elements,\nforms new stars and planets',fontsize=7.4,ha='center',color='#2e7d32',style='italic')
ax.set_title('The life cycle of a star depends mainly on its mass',fontsize=10.5,weight='bold')
plt.tight_layout(); plt.savefig('fig/fig6_stellar_life.png',dpi=100); plt.close()

# ---- tree of life
fig,ax=plt.subplots(figsize=(8,4.8),dpi=100); ax.set_xlim(0,10); ax.set_ylim(0,6); ax.axis('off')
L=dict(color='#333',lw=1.6)
ax.plot([5,5],[0.4,1.2],**L); ax.text(5,0.25,'LUCA, the last universal common ancestor\n(more than 3.5 billion years ago)',ha='center',va='top',fontsize=7.8)
ax.plot([2,7.2],[1.2,1.2],**L)
# bacteria
ax.plot([2,2],[1.2,2.6],**L); ax.plot([0.5,3.6],[2.6,2.6],**L)
bac=[(0.5,'cyano-\nbacteria'),(1.55,'alpha-\nproteo-\nbacteria'),(2.6,'E. coli and\nrelatives'),(3.6,'many\nother phyla')]
for x,l in bac: ax.plot([x,x],[2.6,4.9],color='#1565c0',lw=1.4); ax.text(x,5.0,l,ha='center',va='bottom',fontsize=7.2)
ax.text(2,2.2,'BACTERIA',ha='center',fontsize=9,weight='bold',color='#1565c0')
# archaea + eukarya
ax.plot([7.2,7.2],[1.2,2.0],**L); ax.plot([4.6,7.2],[2.0,2.0],**L)
for x,l in [(4.6,'methane\nmakers'),(5.6,'heat and\nsalt lovers')]: ax.plot([x,x],[2.0,4.9],color='#c62828',lw=1.4); ax.text(x,5.0,l,ha='center',va='bottom',fontsize=7.2)
ax.plot([7.2,7.2],[2.0,2.9],color='#c62828',lw=1.4); ax.plot([6.3,7.2],[2.9,2.9],color='#c62828',lw=1.4); ax.plot([6.3,6.3],[2.9,4.9],color='#c62828',lw=1.4); ax.text(6.3,5.0,'Asgard\narchaea',ha='center',va='bottom',fontsize=7.2)
ax.plot([7.2,7.2],[2.9,3.5],color='#2e7d32',lw=2); ax.plot([7.0,9.6],[3.5,3.5],color='#2e7d32',lw=2)
for x,l in [(7.0,'protists'),(7.85,'plants\nand algae'),(8.7,'fungi'),(9.6,'animals')]: ax.plot([x,x],[3.5,4.9],color='#2e7d32',lw=1.6); ax.text(x,5.0,l,ha='center',va='bottom',fontsize=7.2)
ax.text(5.6,1.65,'ARCHAEA',ha='center',fontsize=9,weight='bold',color='#c62828'); ax.text(8.6,3.15,'EUKARYOTES',ha='center',fontsize=9,weight='bold',color='#2e7d32')
ax.annotate('',xy=(7.25,3.3),xytext=(1.6,3.7),arrowprops=dict(arrowstyle='->',ls='--',lw=1.1,color='#6a1b9a',connectionstyle='arc3,rad=-0.25'))
ax.text(4.0,4.15,'became mitochondria',fontsize=7.4,color='#6a1b9a',style='italic',ha='center')
ax.annotate('',xy=(7.85,4.3),xytext=(0.55,4.3),arrowprops=dict(arrowstyle='->',ls='--',lw=1.1,color='#00838f',connectionstyle='arc3,rad=-0.28'))
ax.text(3.0,5.75,'became chloroplasts',fontsize=7.4,color='#00838f',style='italic',ha='center')
ax.set_title('The tree of life, simplified: two deep branches, with eukaryotes arising inside the archaea',fontsize=9.8,weight='bold')
plt.tight_layout(); plt.savefig('fig/fig7_tree_of_life.png',dpi=100); plt.close()

# ---- plate tectonics
fig,ax=plt.subplots(figsize=(8,4.4),dpi=100); ax.set_xlim(0,10); ax.set_ylim(0,5.4); ax.axis('off')
ax.add_patch(Rectangle((0,0),10,2.9,fc='#ffcc80',ec='none'))  # mantle
ax.add_patch(Rectangle((0,2.9),7.6,1.2,fc='#bbdefb',ec='none'))  # ocean
ax.add_patch(Polygon([(0,2.9),(2.7,2.9),(3.0,3.2),(3.3,2.9),(7.0,2.9),(9.8,1.0),(9.8,0.55),(7.0,2.45),(3.3,2.45),(3.0,2.75),(2.7,2.45),(0,2.45)],fc='#5d4037',ec='#333',lw=0.8))
ax.add_patch(Polygon([(7.2,2.9),(7.5,4.2),(8.3,4.2),(8.6,4.75),(8.9,4.2),(10,4.2),(10,2.2),(8.25,2.2)],fc='#a1887f',ec='#333',lw=0.8))
ax.plot([8.75,8.62],[1.72,4.6],color='#d32f2f',lw=1.2,ls=':')
ax.text(9.0,3.0,'melting\nfeeds\nvolcanoes',fontsize=7.2,color='white',ha='left')
ax.text(1.4,3.5,'ocean',fontsize=8,color='#0d47a1',style='italic')
ax.text(3.0,3.45,'mid-ocean ridge:\nnew crust forms',ha='center',fontsize=7.8)
ax.annotate('',xy=(1.3,2.67),xytext=(2.4,2.67),arrowprops=dict(arrowstyle='->',lw=1.4,color='white')); ax.annotate('',xy=(5.6,2.67),xytext=(4.0,2.67),arrowprops=dict(arrowstyle='->',lw=1.4,color='white'))
ax.text(5.0,2.1,'oceanic plate, 2–10 cm per year',fontsize=7.6,ha='center')
ax.text(6.9,3.25,'trench',fontsize=7.8,ha='center')
ax.text(8.6,4.9,'volcanic arc',fontsize=7.8,ha='center'); ax.text(8.1,3.6,'continent',fontsize=8,ha='center',color='white')
ax.text(8.0,0.75,'subduction:\nold crust sinks',fontsize=7.6,ha='center')
for cx,r in [(1.6,0.85),(5.1,0.85)]:
    th=np.linspace(0.2,2*np.pi-0.2,60); ax.plot(cx+1.35*np.cos(th),1.2+r*np.sin(th),color='#bf360c',lw=1.1,ls='--')
ax.annotate('',xy=(3.0,2.2),xytext=(3.0,1.0),arrowprops=dict(arrowstyle='->',lw=1.3,color='#bf360c'))
ax.text(3.2,0.6,'hot mantle rock rises',fontsize=7.6,color='#bf360c',ha='center')
ax.text(0.15,0.15,'mantle: solid rock that flows slowly over millions of years',fontsize=7.6,style='italic',color='#4e342e')
ax.text(0.15,2.0,'lithosphere\n(rigid plate)',fontsize=7.4,color='#3e2723')
ax.set_title('Plate tectonics: plates are made at ridges and destroyed at trenches',fontsize=10.5,weight='bold')
plt.tight_layout(); plt.savefig('fig/fig8_plates.png',dpi=100); plt.close()
print('ok')
