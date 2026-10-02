import math, numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os; OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'fig')+os.sep
plt.rcParams.update({'font.size':9,'font.family':'DejaVu Sans','axes.grid':True,'grid.alpha':0.3})
def save(fig,name): fig.tight_layout(); fig.savefig(OUT+name,dpi=200); plt.close(fig)
W,H=6.0,2.9
# 24.1
G=np.logspace(0,3,200); fig,ax=plt.subplots(figsize=(W,H))
for t,c in [(0.01,'r'),(0.001,'b'),(0.0001,'g')]:
    ax.semilogx(G,20*np.log10(G*2/(4*t)),c,lw=1.5,label=f'{t*100:g}% resistors')
ax.plot(100,20*np.log10(100*500),'ko',ms=4); ax.annotate('WE 24.3: 94 dB',(100,94),textcoords='offset points',xytext=(-70,8))
ax.set_xlabel('Front-end gain G₁'); ax.set_ylabel('Total CMRR (dB)'); ax.legend(fontsize=8,loc='upper left'); ax.set_ylim(40,140)
save(fig,'fig24_1.png')
# 25.1
fig,ax=plt.subplots(figsize=(W,H)); dt=1e-4; t=np.arange(0,1.2,dt)
for z,c in [(0.4,'r'),(0.7,'b'),(1.0,'g')]:
    x=v=0; ys=[]
    for _ in t:
        a=100*(1-x)-2*z*10*v; v+=a*dt; x+=v*dt; ys.append(x)
    ax.plot(t,ys,c,lw=1.5,label=f'ζ = {z}')
ax.axhline(1,color='gray',ls='--',lw=1); ax.set_xlabel('Time (s)'); ax.set_ylabel('Position / step size'); ax.legend(fontsize=8)
save(fig,'fig25_1.png')
# 26.1
f=np.logspace(5,9,300); fig,ax=plt.subplots(figsize=(W,H))
for s,c in [(0.1e-12,'g'),(1e-12,'b'),(10e-12,'r')]:
    ax.semilogx(f,-20*np.log10(2*np.pi*f*s),c,lw=1.5,label=f'σ = {s*1e12:g} ps')
for N in [12,14,16]:
    v=6.02*N+1.76; ax.axhline(v,color='gray',ls=':',lw=1); ax.text(1.2e5,v+1,f'{N}-bit ideal {v:.0f} dB',fontsize=7,color='gray')
ax.set_xlabel('Input frequency (Hz)'); ax.set_ylabel('Jitter-limited SNR (dB)'); ax.set_ylim(40,130); ax.legend(fontsize=8,loc='lower left')
save(fig,'fig26_1.png')
# 27.1
k=1.380649e-23;q=1.602176634e-19; T=np.linspace(233.15,398.15,200)
vbe=0.65-2e-3*(T-300)+1.5e-8*-(T-300)**2*0  # linear model used in text
Kg=2e-3/(k/q*math.log(8)); ptat=Kg*k*T/q*math.log(8)
# add small curvature to VBE to show parabola
vbe_c=0.65-2e-3*(T-300)-4e-7*(T-300)**2
fig,ax=plt.subplots(figsize=(W,H)); Tc=T-273.15
ax.plot(Tc,vbe_c,'r',lw=1.5,label='V_BE (CTAT)'); ax.plot(Tc,ptat,'b',lw=1.5,label='K·ΔV_BE (PTAT)'); ax.plot(Tc,vbe_c+ptat,'k',lw=1.8,label='V_REF = sum')
ax.set_xlabel('Temperature (°C)'); ax.set_ylabel('Voltage (V)'); ax.set_ylim(0.3,1.4); ax.legend(fontsize=8,loc='center left',bbox_to_anchor=(0.02,0.72))
save(fig,'fig27_1.png')
# 28.1
D=np.linspace(0,1,300); Vs,L,fs=24,1e-3,20e3; fig,ax=plt.subplots(figsize=(W,H))
ax.plot(D,2*Vs*D*(1-D)/(L*fs),'r',lw=1.5,label='Bipolar'); ax.plot(D,Vs*D*(1-D)/(L*fs),'b',lw=1.5,label='Sign-magnitude')
ax.plot(0.5,0.6,'ro',ms=5); ax.annotate('bipolar 0 V point: 0.6 A',(0.5,0.6),textcoords='offset points',xytext=(-150,4))
ax.plot(0,0,'bo',ms=5); ax.annotate('sign-magnitude 0 V point',(0,0),textcoords='offset points',xytext=(8,14))
ax.set_xlabel('Duty cycle D'); ax.set_ylabel('Ripple Δi (A pk-pk)'); ax.set_ylim(0,0.7); ax.legend(fontsize=8,loc='lower center')
save(fig,'fig28_1.png')
