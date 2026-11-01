#!/usr/bin/env python3
"""Independent R146 verifier using copied original R145 sector rep and native word class.
No dependency on original /mnt/data location; includes full 128D spin-basis validation.
"""
from pathlib import Path
import numpy as np
from scipy.linalg import svdvals
import native_variants as nv
DIR=Path(__file__).resolve().parent.parent
m=np.load(DIR/'evidence'/'r146_manifold.npz')
c=np.load(DIR/'evidence'/'r146_certificate.npz')
orig=nv.BASE_AREAS.copy()
assert c['w'].shape==(8,)
print('convex optimum w:',c['w'],'one-round projected H_min', 2/3*np.linalg.norm(c['z'])**2)
assert 2/3*np.linalg.norm(c['z'])**2>1e-5
assert np.min(c['A'].T@c['z'])>1.4e-4
for t in [0.,0.08,0.12,0.16,0.26]:
 j=int(np.argmin(abs(m['t']-t)))
 nv.BASE_AREAS=m['angles'][j].copy()
 order=[(0,i) for i in range(4)]
 for i in range(4):
  K=nv.K(np.zeros(5),i)
  ph=np.trace(K)/2
  assert abs(abs(ph)-1)<1e-10
  assert np.linalg.norm(K-ph*np.eye(2))<1e-10
 det=1-svdvals(nv.cycle_product(np.zeros(5),order,spin_sector=1))[0]**2
 eps=1e-6
 ph=np.trace(nv.cycle_product(np.zeros(5),order))/2
 H=0
 for b in range(5):
  d=np.zeros(5);d[b]=eps
  D=(nv.cycle_product(d,order)-nv.cycle_product(-d,order))/(2*eps*ph)
  for v in nv.STATES.T:
   dv=D@v;H+=np.vdot(dv,dv).real-abs(np.vdot(v,dv))**2
 H/=6
 assert abs(H-m['H4'][j])<2e-6
 print('t',t,'H4',H,'worst S1 detection',det,'min area',nv.BASE_AREAS.min())
# independent full 128-dimensional native-physical verification of each forward K4 word
I=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],complex);Y=np.array([[0,-1j],[1j,0]],complex);Z=np.diag([1,-1]).astype(complex)
u=np.array([1,0],complex);d=np.array([0,1],complex)
s=(np.kron(u,d)-np.kron(d,u))/np.sqrt(2)
t0=(np.kron(u,d)+np.kron(d,u))/np.sqrt(2);tp=np.kron(u,u);tm=np.kron(d,d)
L=np.column_stack([np.kron(s,s),(np.kron(t0,t0)-np.kron(tp,tm)-np.kron(tm,tp))/np.sqrt(3)])
def on(p,i):
 A=np.array([[1]],complex)
 for j in range(7):A=np.kron(A,p if i==j else I)
 return A
PS={}
for a,b in ((3,5),(0,4),(1,4),(2,4),(3,4)):
 PS[(a,b)]=np.eye(128)/4-sum(on(q,a)@on(q,b) for q in (X,Y,Z))/4
inputs=np.column_stack([np.kron(np.kron(L[:,k],s),g) for k in range(2) for g in (u,d)])
SW=np.eye(128)-2*PS[(3,5)];B=SW@inputs
SITE={4:0,2:1,6:2,8:3,5:4,9:5}
for t in [0.08,0.12,0.26]:
 ix=int(np.argmin(abs(m['t']-t)));nv.BASE_AREAS=m['angles'][ix]
 for perm in range(4):
  z=B.copy()
  for _,x,y,area in nv.pulseword(perm,False):
   pq=PS[tuple(sorted((SITE[x],SITE[y])))]
   z=z+(np.exp(1j*np.pi*area)-1)*pq@z
  ph=np.trace(B.conj().T@z)/4
  err=np.linalg.norm(z-ph*B)
  assert err<1e-11,(t,perm,err)
 print('full 7spin check PASS t',t,'4 variants')
nv.BASE_AREAS=orig
print('R146 VERIFIED')