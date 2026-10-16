import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, Circle, Ellipse
import sys, os
OUT=sys.argv[1]
W=3.0; DPI=267   # 801 px wide, 3.0 in
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":8,"font.weight":"bold","axes.linewidth":1.2,"text.color":"black","axes.labelweight":"bold","mathtext.default":"bf"})
BL="#000000"; BLUE="#0b3d91"; RED="#b00020"; GREY="#555555"
def fig(h):
    f=plt.figure(figsize=(W,h),dpi=DPI); f.patch.set_facecolor("white"); return f
def save(f,name):
    f.savefig(os.path.join(OUT,name),dpi=DPI,facecolor="white"); plt.close(f)

# Fig 1: two clocks, 0.6c out and back
f=fig(2.9); ax=f.add_axes([0.14,0.16,0.80,0.80])
ax.plot([0,0],[0,10],color=BL,lw=3.2,solid_capstyle="butt")
ax.plot([0,3,0],[0,5,10],color=RED,lw=3.2)
ax.plot([-0.0,3.9],[0,3.9],color=GREY,lw=1,ls=":"); 
ax.text(4.3,3.3,"light",color=GREY,fontsize=7,rotation=0,ha="left",va="center")
ax.set_xlim(-0.8,6.2); ax.set_ylim(-0.8,11.2)
ax.set_xlabel("distance from home (light-years)",fontsize=8); ax.set_ylabel("home calendar (years)",fontsize=8)
ax.set_xticks([0,1,2,3]); ax.set_yticks([0,5,10]); ax.tick_params(width=1.2,labelsize=8)
ax.text(-0.15,10.6,"Stay-at-home clock: 10 years",color=BL,fontsize=8,ha="left")
ax.text(3.3,5.0,"turns round\nat 3 light-years",color=RED,fontsize=7.5,va="center",ha="left")
ax.text(3.3,8.3,"Traveller at 0.6c:\nown clock 8 years\n(10 \u00d7 0.8)",color=RED,fontsize=7.5,ha="left",va="center")
ax.annotate("",xy=(0.0,10),xytext=(0.0,9.99))
for s in ("top","right"): ax.spines[s].set_visible(False)
save(f,"fig1_two_clocks.png")

# Fig 2
f=fig(2.9); ax=f.add_axes([0,0,1,1]); ax.set_xlim(0,10); ax.set_ylim(0,10); ax.axis("off")
f_=[(3*n+4)%10 for n in range(10)]
xs=np.linspace(0.9,9.1,10)
ax.text(5,9.6,"Digit N arrives from the future",ha="center",fontsize=8)
for n in range(10):
    ax.text(xs[n],8.4,str(n),ha="center",va="center",fontsize=11,bbox=dict(boxstyle="round,pad=0.25",fc="white",ec=BL,lw=1.4))
    ax.text(xs[n],3.2,str(n),ha="center",va="center",fontsize=11,bbox=dict(boxstyle="round,pad=0.25",fc="white",ec=BL,lw=1.4))
for n in range(10):
    if f_[n]==n: continue
    ax.annotate("",xy=(xs[f_[n]],3.95),xytext=(xs[n],7.65),arrowprops=dict(arrowstyle="-|>",lw=0.9,color="#8a8a8a",shrinkA=0,shrinkB=0,mutation_scale=6))
for n in range(10):
    if f_[n]==n:
        ax.annotate("",xy=(xs[n],3.95),xytext=(xs[n],7.65),arrowprops=dict(arrowstyle="-|>",lw=4,color=BLUE,shrinkA=0,shrinkB=0,mutation_scale=12))
ax.text(5,2.1,"Digit you send back = last digit of 3N + 4",ha="center",fontsize=8)
ax.text(5,1.15,"Only 3 and 8 come back as themselves (blue).",ha="center",fontsize=7.5,color=BLUE)
ax.text(5,0.45,"The other eight cannot exist.",ha="center",fontsize=7.5,color=BL)
save(f,"fig2_consistent_loop.png")

# Fig 3: looking at an electron
f=fig(3.0); ax=f.add_axes([0,0,1,1]); ax.set_xlim(0,10); ax.set_ylim(0,10); ax.axis("off")
def photon(ax,x0,x1,y,wl,amp=0.35,col=BLUE):
    x=np.linspace(x0,x1,400); ax.plot(x,y+amp*np.sin(2*np.pi*(x-x0)/wl),color=col,lw=1.8)
    ax.annotate("",xy=(x1+0.25,y),xytext=(x1,y),arrowprops=dict(arrowstyle="-|>",color=col,lw=1.8))
# top: short wavelength
ax.text(5,9.3,"Short wavelength (about 1 nm)",ha="center",fontsize=8)
photon(ax,0.4,4.3,7.7,0.55)
ax.add_patch(Circle((5.1,7.7),0.28,fc=BL,ec=BL))
ax.add_patch(Circle((5.1,7.7),0.55,fc="none",ec=BL,lw=1,ls=":"))
ax.annotate("",xy=(9.3,7.7),xytext=(5.6,7.7),arrowprops=dict(arrowstyle="-|>",color=RED,lw=3.4,mutation_scale=12))
ax.text(7.45,8.45,"hard kick",color=RED,ha="center",fontsize=8)
ax.text(5.1,6.55,"sharp position",ha="center",fontsize=7.5)
ax.plot([0.3,9.7],[5.4,5.4],color="#999999",lw=1)
# bottom: long wavelength
ax.text(5,4.7,"Long wavelength (about 500 nm)",ha="center",fontsize=8)
photon(ax,0.4,3.4,2.6,2.2)
ax.add_patch(Ellipse((5.1,2.6),2.4,1.7,fc="#d9d9d9",ec=BL,lw=1,ls=":"))
ax.add_patch(Circle((5.1,2.6),0.28,fc=BL,ec=BL))
ax.annotate("",xy=(6.9,2.6),xytext=(6.45,2.6),arrowprops=dict(arrowstyle="-|>",color=RED,lw=1.4,mutation_scale=8))
ax.text(8.2,2.6,"gentle kick",color=RED,ha="center",va="center",fontsize=8)
ax.text(5.1,1.1,"blurred position (about one wavelength)",ha="center",fontsize=7.5)
ax.text(5,0.25,"not to scale",ha="center",fontsize=6.5,color=GREY,fontweight="normal")
save(f,"fig3_looking_at_electron.png")

# Fig 4
f=fig(3.5)
ax=f.add_axes([0,0.50,1,0.50]); ax.set_xlim(0,10); ax.set_ylim(0,6); ax.axis("off")
ax.add_patch(Circle((5,4.2),0.5,fc="white",ec=BL,lw=1.8)); ax.text(5,4.2,"S",ha="center",va="center",fontsize=9)
ax.text(5,5.3,"pair made together",ha="center",fontsize=7.5)
ax.annotate("",xy=(2.45,4.2),xytext=(4.4,4.2),arrowprops=dict(arrowstyle="-|>",lw=1.6,color=BL))
ax.annotate("",xy=(7.55,4.2),xytext=(5.6,4.2),arrowprops=dict(arrowstyle="-|>",lw=1.6,color=BL))
for x,nm,ang in ((1.35,"Alice",r"axis $\theta_A$"),(8.65,"Bob",r"axis $\theta_B$")):
    ax.add_patch(Rectangle((x-1.2,3.35,),2.4,1.7,fc="white",ec=BL,lw=1.8))
    ax.text(x,4.6,nm,ha="center",va="center",fontsize=8); ax.text(x,3.8,ang,ha="center",va="center",fontsize=7.5)
ax.text(1.4,2.5,"her list alone:\na coin toss",ha="center",va="center",fontsize=7,color=BL)
ax.text(8.6,2.5,"his list alone:\na coin toss",ha="center",va="center",fontsize=7,color=BL)
ax.text(5,0.6,"No message passes between them.",ha="center",fontsize=7.5,color=RED)
ax2=f.add_axes([0.22,0.17,0.72,0.27])
t=np.linspace(0,180,361)
ax2.plot(t,np.cos(np.radians(t)/2)**2,color=BLUE,lw=2.6)
for a_ in (0,60,90,180):
    ax2.plot([a_],[np.cos(np.radians(a_)/2)**2],"o",color=RED,ms=5)
ax2.set_xticks([0,60,90,180]); ax2.set_yticks([0,0.5,1]); ax2.set_ylim(-0.08,1.15); ax2.set_xlim(-6,186)
ax2.set_xlabel(r"angle between the two axes (degrees)",fontsize=7.5)
ax2.set_ylabel("share opposite",fontsize=7.5); ax2.tick_params(labelsize=7.5,width=1.2)
ax2.text(63,0.82,"60\u00b0: 0.75",fontsize=7,color=RED)
ax2.text(100,0.56,"90\u00b0: 0.5",fontsize=7,color=RED)
for s_ in ("top","right"): ax2.spines[s_].set_visible(False)
save(f,"fig4_correlated_tokens.png")

# Fig 5: tunnelling, exact rectangular barrier, E<V
hbar=1.0; m=1.0; E=1.0; V=2.0
k=np.sqrt(2*m*E)/hbar; kap=np.sqrt(2*m*(V-E))/hbar; L=2.0
# unknowns A(refl),B,C,F with incident 1: x<0: e^{ikx}+R e^{-ikx}; 0<x<L: B e^{kap x}+C e^{-kap x}; x>L: T e^{ikx}
M=np.array([[-1,1,1,0],[-1j*k,-kap,kap,0],[0,np.exp(kap*L),np.exp(-kap*L),-np.exp(1j*k*L)],[0,kap*np.exp(kap*L),-kap*np.exp(-kap*L),-1j*k*np.exp(1j*k*L)]],dtype=complex)
rhs=np.array([1,-1j*k,0,0],dtype=complex)
R,B,C,T=np.linalg.solve(M,rhs)
x1=np.linspace(-6,0,500); x2=np.linspace(0,L,200); x3=np.linspace(L,L+6,500)
p1=np.exp(1j*k*x1)+R*np.exp(-1j*k*x1); p2=B*np.exp(kap*x2)+C*np.exp(-kap*x2); p3=T*np.exp(1j*k*x3)
prob=abs(T)**2
f=fig(2.6); ax=f.add_axes([0.04,0.20,0.92,0.72]); 
ax.add_patch(Rectangle((0,-2.7),L,5.3,fc="#d0d0d0",ec=BL,lw=1.6,zorder=0))
ax.plot(x1,p1.real,color=BLUE,lw=2.2); ax.plot(x2,p2.real,color=RED,lw=2.4); ax.plot(x3,p3.real,color=BLUE,lw=2.2)
ax.set_xlim(-6,L+6); ax.set_ylim(-2.9,3.5); ax.axis("off")
ax.text(L/2,2.95,"barrier",ha="center",fontsize=8)
ax.text(-3,2.45,"wave arrives",ha="center",fontsize=7.5,color=BLUE)
ax.text(L/2,-2.25,"dies away\nsteeply inside",ha="center",fontsize=7,color=RED)
ax.text(L+2.9,1.5,"small wave beyond:\nthe chance of\nfinding it here",ha="center",va="center",fontsize=7,color=BLUE)
ax.annotate("",xy=(L+6,-2.55),xytext=(-6,-2.55),arrowprops=dict(arrowstyle="-",lw=0))
f.text(0.5,0.04,"position  \u2192      (wave height shown, not to scale)",ha="center",fontsize=7,fontweight="normal",color=GREY)
save(f,"fig5_tunnelling.png")
print("T^2 prob",prob)
