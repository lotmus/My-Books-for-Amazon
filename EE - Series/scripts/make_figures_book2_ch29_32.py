import math, numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os; OUT=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'chapters','Book2','ch29_32','fig')+os.sep
plt.rcParams.update({'font.size':9,'font.family':'DejaVu Sans','axes.grid':True,'grid.alpha':0.3})
def save(fig,name): fig.tight_layout(); fig.savefig(OUT+name,dpi=200); plt.close(fig)
W,H=6.0,2.9
# 29.1 root locus
fig,ax=plt.subplots(figsize=(W,3.4))
Ks=np.concatenate([np.linspace(0,9.03,300),np.linspace(9.03,600,3000)])
pts=np.array([np.sort_complex(np.roots([1,12,20,K])) for K in Ks])
for i in range(3): ax.plot(pts[:,i].real,pts[:,i].imag,'b.',ms=1)
ax.plot([0,-2,-10],[0,0,0],'kx',ms=7,mew=1.5)
for a in (60,-60): ax.plot([-4,-4+8*math.cos(math.radians(a))],[0,8*math.sin(math.radians(a))],'g--',lw=0.8)
r=np.roots([1,12,20,28.7]); ax.plot(r.real,r.imag,'ro',ms=4); ax.annotate('K = 28.7 (ζ = 0.5)',(-0.83,1.44),textcoords='offset points',xytext=(-95,8),fontsize=7)
ax.plot([0,0],[4.47,-4.47],'ms',ms=4); ax.annotate('K = 240, ±j4.47',(0,4.47),textcoords='offset points',xytext=(5,-3),fontsize=7)
ax.annotate('breakaway −0.945',(-0.945,0),textcoords='offset points',xytext=(-20,-18),fontsize=7)
ax.axvline(0,color='k',lw=0.6); ax.axhline(0,color='k',lw=0.6)
ax.set_xlim(-14,3); ax.set_ylim(-7,7); ax.set_xlabel('Real part (1/s)'); ax.set_ylabel('Imaginary part (rad/s)')
save(fig,'fig29_1.png')
# 30.1 sensitivity
w=np.logspace(-2,2,4000); fig,ax=plt.subplots(figsize=(W,H))
for K,c in [(28.7,'g'),(60,'b'),(120,'r')]:
    S=abs(1/(1+K/(1j*w*(1j*w+2)*(1j*w+10)))); ax.loglog(w,S,c,lw=1.5,label=f'K = {K:g}, Mₛ = {S.max():.2f}')
ax.axhline(1,color='gray',ls='--',lw=1); ax.set_xlabel('Frequency (rad/s)'); ax.set_ylabel('|S(jω)|'); ax.legend(fontsize=8,loc='lower right'); ax.set_ylim(1e-3,10)
save(fig,'fig30_1.png')
# 31.1 relaxation
R,C,b,V=1e4,1e-7,0.5,1.0; tau=R*C; dt=1e-6; t=np.arange(0,6e-3,dt); vc=0.0; out=V; vs=[];os_=[]
for _ in t:
    vc+= (out-vc)/tau*dt
    if out>0 and vc>=b*V: out=-V
    elif out<0 and vc<=-b*V: out=V
    vs.append(vc); os_.append(out)
fig,ax=plt.subplots(figsize=(W,H)); ax.plot(t*1e3,os_,'b',lw=1.2,label='comparator output (±V)'); ax.plot(t*1e3,vs,'r',lw=1.5,label='capacitor voltage')
ax.axhline(b,color='gray',ls=':'); ax.axhline(-b,color='gray',ls=':'); ax.set_xlabel('Time (ms)'); ax.set_ylabel('Voltage / V'); ax.legend(fontsize=8,loc='lower right'); ax.set_ylim(-1.3,1.3)
save(fig,'fig31_1.png')
# 32.1 MTBF
tr=np.linspace(0.5e-9,5e-9,300); m=np.exp(tr/50e-12)/(1e-10*2e8*1e7)
fig,ax=plt.subplots(figsize=(W,H)); ax.semilogy(tr*1e9,m/3.156e7,'b',lw=1.5)
for x,l in [(1.0,'1.0 ns: 40 min'),(4.5,'4.5 ns: 1.9×10²⁶ yr')]:
    y=math.exp(x/0.05)/2e5/3.156e7; ax.plot(x,y,'ro',ms=4); ax.annotate(l,(x,y),textcoords='offset points',xytext=(-90 if x>3 else 8,-4),fontsize=7)
ax.axhline(1,color='gray',ls='--',lw=1); ax.text(0.55,1.5,'1 year',fontsize=7,color='gray')
ax.set_xlabel('Resolution time t_r (ns)'); ax.set_ylabel('MTBF (years)')
save(fig,'fig32_1.png')
