import math, numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
import os; OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'fig')+os.sep
plt.rcParams.update({'font.size':9,'font.family':'DejaVu Sans','axes.grid':True,'grid.alpha':0.3})
def save(fig,name): fig.tight_layout(); fig.savefig(OUT+name,dpi=200); plt.close(fig)
W,H=6.0,2.9
# 11.1 block diagram
fig,ax=plt.subplots(figsize=(W,2.4)); ax.axis('off'); ax.set_xlim(0,10); ax.set_ylim(0,4)
ax.add_patch(Circle((2.2,2.8),0.35,fill=False,lw=1.5)); ax.text(2.2,2.8,'Σ',ha='center',va='center',fontsize=12)
ax.add_patch(FancyBboxPatch((4,2.3),2,1,boxstyle='round,pad=0.05',fill=False,lw=1.5)); ax.text(5,2.8,'A',ha='center',va='center',fontsize=13)
ax.add_patch(FancyBboxPatch((4,0.4),2,1,boxstyle='round,pad=0.05',fill=False,lw=1.5)); ax.text(5,0.9,'β',ha='center',va='center',fontsize=13)
kw=dict(arrowstyle='->',lw=1.3)
ax.annotate('',xy=(1.85,2.8),xytext=(0.3,2.8),arrowprops=kw); ax.text(0.4,3.05,'Vᵢₙ')
ax.annotate('',xy=(4,2.8),xytext=(2.55,2.8),arrowprops=kw); ax.text(2.9,3.05,'error')
ax.annotate('',xy=(9.6,2.8),xytext=(6.05,2.8),arrowprops=kw); ax.text(8.8,3.05,'Vₒᵤₜ')
ax.plot([7.5,7.5],[2.8,0.9],'k',lw=1.3); ax.annotate('',xy=(6.05,0.9),xytext=(7.5,0.9),arrowprops=kw)
ax.plot([4,2.2],[0.9,0.9],'k',lw=1.3); ax.annotate('',xy=(2.2,2.45),xytext=(2.2,0.9),arrowprops=kw)
ax.text(1.6,2.25,'−',fontsize=13); ax.text(1.5,3.1,'+',fontsize=11); ax.text(2.4,1.3,'βVₒᵤₜ')
save(fig,'fig11_1.png')
# 12.1 PM vs CL
def pm(CL,ro=50,gbw=1e6):
    fp=1/(2*math.pi*ro*CL); lo,hi=1,1e8
    for _ in range(200):
        m=math.sqrt(lo*hi); mag=gbw/m/math.sqrt(1+(m/fp)**2)
        lo,hi=(m,hi) if mag>1 else (lo,m)
    return 90-math.degrees(math.atan(m/fp))
CL=np.logspace(-11,-7,200); fig,ax=plt.subplots(figsize=(W,H))
ax.semilogx(CL*1e9,[pm(c) for c in CL],'b',lw=1.6); ax.axhline(45,color='gray',ls='--',lw=1); ax.axhline(30,color='r',ls=':',lw=1)
ax.text(0.012,47,'45°',color='gray'); ax.text(0.012,32,'30° rings',color='r')
for c in [1e-9,10e-9]: ax.plot(c*1e9,pm(c),'ko',ms=4); ax.annotate(f'{c*1e9:.0f} nF: {pm(c):.0f}°',(c*1e9,pm(c)),textcoords='offset points',xytext=(5,5))
ax.set_xlabel('Load capacitance (nF)'); ax.set_ylabel('Phase margin (degrees)'); ax.set_ylim(0,95)
save(fig,'fig12_1.png')
# 13.1 Bode
f=np.logspace(0,7,500); A=1e5/np.sqrt(1+(f/10)**2); fig,ax=plt.subplots(figsize=(W,H))
ax.semilogx(f,20*np.log10(A),'k',lw=1.6,label='Open loop A(f)')
for ng,c in [(1,'g'),(10,'b'),(100,'r')]:
    G=ng/np.sqrt(1+(f/(1e6/ng))**2); ax.semilogx(f,20*np.log10(G),c,lw=1.3,label=f'NG = {ng}: f_cl = {1e6/ng/1e3:g} kHz')
ax.set_xlabel('Frequency (Hz)'); ax.set_ylabel('Gain (dB)'); ax.set_ylim(-20,110); ax.legend(fontsize=7.5,loc='upper right')
save(fig,'fig13_1.png')
# 14.1 noise density
f=np.logspace(-1,5,400); e=10*np.sqrt(1+100/f); fig,ax=plt.subplots(figsize=(W,H))
ax.loglog(f,e,'b',lw=1.6); ax.axvline(100,color='gray',ls='--',lw=1); ax.text(110,150,'f_c = 100 Hz',color='gray')
ax.axhline(10,color='gray',ls=':',lw=1); ax.set_xlabel('Frequency (Hz)'); ax.set_ylabel('e_n (nV/√Hz)'); ax.set_ylim(5,500)
save(fig,'fig14_1.png')
# 15.1 bar chart
fig,ax=plt.subplots(figsize=(W,H)); labels=['Offset,\nuntrimmed','Bias current,\nuncompensated','Bias current,\ncompensated','Offset drift,\n25→75 °C']
vals=[202,80,20,50.5]; ax.bar(labels,vals,color=['#c44','#c84','#4a4','#48c']); 
for i,v in enumerate(vals): ax.text(i,v+4,f'{v:g} mV',ha='center')
ax.set_ylabel('Output error (mV)'); ax.set_ylim(0,230); ax.grid(axis='x')
save(fig,'fig15_1.png')
# 16.1 Schmitt
t=np.linspace(0,1,4000); rng=np.random.default_rng(3); vin=2.5+1.0*np.sin(2*np.pi*1.5*t-1.2)+np.convolve(0.25*rng.standard_normal(t.size+4),np.ones(5)/5,mode='valid'); hi,lo=2.727,2.273; out=[];state=5
for v in vin:
    if state==5 and v>hi: state=0
    elif state==0 and v<lo: state=5
    out.append(state)
single=np.where(vin>2.5,0,5)
fig,(a1,a2)=plt.subplots(2,1,figsize=(W,3.6),sharex=True)
a1.plot(t,vin,'k',lw=0.8); a1.axhline(hi,color='r',ls='--',lw=1); a1.axhline(lo,color='b',ls='--',lw=1)
a1.set_ylabel('Input (V)'); a1.text(0.005,hi+0.07,'2.727 V',color='r',fontsize=7); a1.text(0.005,lo-0.25,'2.273 V',color='b',fontsize=7)
a2.plot(t,single+0.15,color='0.6',lw=0.8,label='single threshold'); a2.plot(t,out,'b',lw=1.4,label='Schmitt trigger')
a2.set_ylabel('Output (V)'); a2.set_xlabel('Time (arbitrary units)'); a2.legend(fontsize=7,loc='center right')
save(fig,'fig16_1.png')
# 17.1 P control steps
t=np.linspace(0,0.15,600); fig,ax=plt.subplots(figsize=(W,H))
for Kp,c in [(1,'r'),(5,'b'),(20,'g')]:
    L=Kp*2; y=10*L/(1+L)*(1-np.exp(-t*(1+L)/0.1)); ax.plot(t*1e3,y,c,lw=1.5,label=f'K_p = {Kp}: final {10*L/(1+L):.2f} rad/s')
ax.axhline(10,color='k',ls='--',lw=1); ax.set_xlabel('Time (ms)'); ax.set_ylabel('Speed (rad/s)'); ax.legend(fontsize=7.5,loc='lower right')
save(fig,'fig17_1.png')
# 18.1 lead phase
w=np.logspace(0,3.5,500); fig,ax=plt.subplots(figsize=(W,H))
for a,c in [(4,'b'),(10,'r')]:
    wz=50/math.sqrt(a); wp=50*math.sqrt(a); ph=np.degrees(np.arctan(w/wz)-np.arctan(w/wp)); ax.semilogx(w,ph,c,lw=1.5,label=f'α = {a}: max {math.degrees(math.asin((a-1)/(a+1))):.1f}°')
ax.axvline(50,color='gray',ls='--',lw=1); ax.set_xlabel('Angular frequency (rad/s)'); ax.set_ylabel('Phase lead (degrees)'); ax.legend(fontsize=8)
save(fig,'fig18_1.png')
# 19.1 sampled
def sim(T,delay,cont=False,tend=0.12,ref=10,Kp=5,Ki=50):
    K=2;tau=0.1;dt=1e-5;y=0;integ=0;out=[];ts=[];t=0;nextS=0;ua=0;un=0
    while t<tend:
        if cont or t>=nextS-1e-12:
            e=ref-y; step=dt if cont else T; integ+=e*step; u=Kp*e+Ki*integ
            if delay: ua=un; un=u
            else: ua=u
            nextS+=T
        y+=dt*(K*ua-y)/tau; out.append(y); ts.append(t); t+=dt
    return np.array(ts),np.array(out)
fig,ax=plt.subplots(figsize=(W,H))
for args,lab,c in [(dict(T=1e-5,delay=False,cont=True),'continuous','k'),(dict(T=1e-3,delay=True),'sampled 1 kHz, 1-period delay','b'),(dict(T=5e-3,delay=True),'sampled 200 Hz, 1-period delay','r')]:
    ts,y=sim(**args); ax.plot(ts*1e3,y,c,lw=1.4,label=lab)
ax.axhline(10,color='gray',ls='--',lw=1); ax.set_xlabel('Time (ms)'); ax.set_ylabel('Speed (rad/s)'); ax.legend(fontsize=7.5,loc='lower right')
save(fig,'fig19_1.png')
# 20.1 L vs I
I=np.linspace(0,4,400); hard=10/(1+(I/3.2)**12)**0.5; soft=10/(1+(I/2.6)**2)**0.6
fig,ax=plt.subplots(figsize=(W,H)); ax.plot(I,hard,'b',lw=1.5,label='gapped ferrite (hard)'); ax.plot(I,soft,'r',lw=1.5,label='metal composite (soft)')
ax.axhline(8,color='gray',ls=':',lw=1); ax.text(0.05,7.6,'−20%',color='gray',fontsize=8)
ax.set_xlabel('DC current (A)'); ax.set_ylabel('Inductance (µH)'); ax.set_ylim(0,11); ax.legend(fontsize=8)
save(fig,'fig20_1.png')
# 21.1 filters
f=np.logspace(-1,1,500); fig,ax=plt.subplots(figsize=(W,H))
for Q,lab,c in [(0.5773,'Bessel Q = 0.577','g'),(0.7071,'Butterworth Q = 0.707','b'),(0.9565,'Chebyshev 1 dB Q = 0.957','r')]:
    s=1j*f; Hh=1/(s**2+s/Q+1); ax.semilogx(f,20*np.log10(abs(Hh)),c,lw=1.4,label=lab)
ax.set_xlabel('Frequency / f₀'); ax.set_ylabel('Gain (dB)'); ax.set_ylim(-40,5); ax.legend(fontsize=8)
save(fig,'fig21_1.png')
# 22.1 derating
T=np.array([-55,70,155]); P=np.array([100,100,0]); fig,ax=plt.subplots(figsize=(W,H))
ax.plot(T,P,'b',lw=1.6); ax.plot(100,64.7,'ro'); ax.annotate('100 °C: 65 mW',(100,64.7),textcoords='offset points',xytext=(8,5))
ax.set_xlabel('Ambient temperature (°C)'); ax.set_ylabel('Allowed power (mW)'); ax.set_ylim(0,115)
save(fig,'fig22_1.png')
# 23.1 impedance
f=np.logspace(5,9,800)
def Z(f,C,L,R): w=2*np.pi*f; return R+1j*(w*L-1/(w*C))
Za=Z(f,10e-6,1e-9,5e-3); Zb=Z(f,100e-9,0.5e-9,20e-3); Zp=1/(1/Za+1/Zb)
fig,ax=plt.subplots(figsize=(W,H)); ax.loglog(f,abs(Za),'b',lw=1.2,label='10 µF'); ax.loglog(f,abs(Zb),'g',lw=1.2,label='100 nF'); ax.loglog(f,abs(Zp),'r',lw=1.8,label='parallel')
ax.axhline(0.015,color='gray',ls='--',lw=1); ax.text(1.2e5,0.018,'15 mΩ target',color='gray',fontsize=8)
ax.set_xlabel('Frequency (Hz)'); ax.set_ylabel('|Z| (Ω)'); ax.legend(fontsize=8)
save(fig,'fig23_1.png')
print('done')
