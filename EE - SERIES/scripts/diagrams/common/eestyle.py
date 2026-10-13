"""Shared figure style for the Electrical Engineering Series (all seven books)."""
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
BLUE='#2f6db0'; RED='#c0392b'; GREEN='#2e8b57'; GRAY='#666666'; ORANGE='#d9822b'; INK='#111111'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.edgecolor':INK,'axes.linewidth':1.0,
  'axes.spines.top':False,'axes.spines.right':False,'axes.grid':True,'grid.color':'#dddddd','grid.linewidth':0.6,
  'axes.titlesize':12,'axes.labelsize':11,'legend.frameon':False,'savefig.dpi':100})
def fig(w=8,h=4.5): return plt.subplots(figsize=(w,h),dpi=100)
def save(f,path):
    f.tight_layout(); f.savefig(path,dpi=100); plt.close(f)
    from PIL import Image
    im=Image.open(path).convert('P',palette=Image.ADAPTIVE,colors=64); im.save(path,optimize=True)
def schem(path, build, unit=2.5, fontsize=12, width_px=800, pad=3.0):
    import schemdraw
    schemdraw.use('matplotlib')
    d=schemdraw.Drawing(show=False)
    d.config(unit=unit,fontsize=fontsize,font='DejaVu Sans',lw=1.6)
    build(d)
    f=d.draw(show=False).fig
    ax=f.axes[0]; x0,x1=ax.get_xlim(); y0,y1=ax.get_ylim(); ax.set_xlim(x0-pad,x1+pad); ax.set_ylim(y0-pad,y1+pad)
    for t in ax.texts: t.set_clip_on(False)
    f.savefig(path,dpi=200,bbox_inches='tight',pad_inches=0.15,facecolor='white')
    plt.close(f)
    from PIL import Image
    im=Image.open(path).convert('RGB')
    from PIL import ImageOps
    bb=ImageOps.invert(im).getbbox(); m=30
    im=im.crop((max(0,bb[0]-m),max(0,bb[1]-m),min(im.width,bb[2]+m),min(im.height,bb[3]+m))); im=im.resize((width_px,round(im.height*width_px/im.width)),Image.LANCZOS); im=im.convert('P',palette=Image.ADAPTIVE,colors=32); im.save(path,optimize=True)
