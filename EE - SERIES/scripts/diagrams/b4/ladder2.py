import numpy as np
Z0=50
def bvd(f,fs,C0,k2,Q):
    r=4/np.pi**2*k2; fp=fs/(1-r); Cm=C0*((fp/fs)**2-1); w=2*np.pi*f
    Lm=1/((2*np.pi*fs)**2*Cm); Rm=2*np.pi*fs*Lm/Q
    Zm=Rm+1j*w*Lm+1/(1j*w*Cm); Zc=1/(1j*w*C0); return Zm*Zc/(Zm+Zc)
def ladder(f,fse,fsh,Cs,Cp,k2,Q,Lg=0.0,n=4):
    A=np.ones_like(f,dtype=complex);B=0*A;C=0*A;D=A.copy()
    for i in range(2*n-1):
        if i%2==0: Z=bvd(f,fse,Cs,k2,Q); a,b,c,d=1,Z,0,1
        else: Z=bvd(f,fsh,Cp,k2,Q)+1j*2*np.pi*f*Lg; a,b,c,d=1,0,1/Z,1
        A,B,C,D=A*a+B*c,A*b+B*d,C*a+D*c,C*b+D*d
    s21=2/(A+B/Z0+C*Z0+D); s11=(A+B/Z0-C*Z0-D)/(A+B/Z0+C*Z0+D); return s21,s11
k2=0.09;Q=1500;r=4/np.pi**2*k2
fse=2.540e9; fsh=fse*(1-r); Cs=0.40e-12; Cp=2.0e-12
fb=np.linspace(2.5e9,2.57e9,141); fr=np.linspace(2.62e9,2.69e9,141)
if __name__=='__main__':
  print('r',r,'fp ser',fse/(1-r),'fsh',fsh, 'Xs',1/(2*np.pi*2.535e9*Cs),'Xp',1/(2*np.pi*2.535e9*Cp))
  for Lg in [0,0.1e-9,0.3e-9]:
    s,s11=ladder(fb,fse,fsh,Cs,Cp,k2,Q,Lg); sr,_=ladder(fr,fse,fsh,Cs,Cp,k2,Q,Lg)
    il=-20*np.log10(abs(s)); rj=-20*np.log10(abs(sr)); rl=-20*np.log10(abs(s11))
    print(Lg,'IL %.2f..%.2f RLmin %.1f rejmin %.1f @2620 %.1f'%(il.min(),il.max(),rl.min(),rj.min(),rj[0]))
