#!/usr/bin/env python3
"""Independent check of 4-spin SOEO star exchange + singlet-pair probe.
All frequencies are angular units J=1, hbar=1; 4 data + ancilla a + spectator b.
This is NOT a strict serial exchange-only physical sequence.
"""
import numpy as np
from scipy.linalg import eigh
from math import pi
np.set_printoptions(precision=9,suppress=True)
I=np.eye(2, dtype=complex)
X=np.array([[0,1],[1,0]],dtype=complex)
Y=np.array([[0,-1j],[1j,0]],dtype=complex)
Z=np.diag([1.,-1.]).astype(complex)
up=np.array([1.,0.]); dn=np.array([0.,1.])
def kron_all(x):
    out=np.array([1.], dtype=complex) if all(np.ndim(y)==1 for y in x) else np.array([[1.]], dtype=complex)
    for y in x: out=np.kron(out,y)
    return out

def op(q, site, n): return kron_all([q if k==site else I for k in range(n)])
def Sdot(i,j,n): return sum(op(p,i,n)@op(p,j,n)/4 for p in (X,Y,Z))
def unitary(H,t):
    eig,V=eigh(H)
    return (V*np.exp(-1j*t*eig))@V.conj().T
D=4; n=6
Hterms=[Sdot(i,4,n) for i in range(4)]
H0=sum(Hterms)
sing=(np.kron(up,dn)-np.kron(dn,up))/np.sqrt(2)
s0=np.kron(sing,sing)
t0=(np.kron(up,dn)+np.kron(dn,up))/np.sqrt(2)
tp=np.kron(up,up); tm=np.kron(dn,dn)
s1=(np.kron(t0,t0)-np.kron(tp,tm)-np.kron(tm,tp))/np.sqrt(3)
B=np.stack([s0,s1],axis=1)
assert np.linalg.norm(B.conj().T@B-np.eye(2))<1e-12
W=np.kron(np.eye(16),sing.reshape(4,1))
BC=W@B
assert np.linalg.norm(H0@BC)<1e-12
# data total spin Casimir
S2=sum((sum(op(q,i,4) for i in range(4)) @ sum(op(q,i,4) for i in range(4)))/4 for q in [X,Y,Z])
lambda_,V=eigh(S2)
print('Sector multiplicities:',[(s,int(sum(abs(lambda_-s*(s+1))<1e-9))) for s in [0,1,2]])
U0=unitary(H0,2*pi)
K0=W.conj().T@U0@W
print('ideal no-disturbance norm',np.linalg.norm(U0@BC-BC))
for s in [0,1,2]:
    idx=np.where(abs(lambda_-s*(s+1))<1e-9)[0]
    vv=V[:,idx]
    C=vv.conj().T@K0@vv
    amp=np.trace(C)/len(idx)
    e= [1.,-1/3,1/5][s]
    print(f'S={s}: amplitude={amp.real:+.12f} singlet_prob={abs(amp)**2:.12f}, analytical error={abs(amp-e):.2e}, non-scalar norm={np.linalg.norm(C-amp*np.eye(len(idx))):.2e}')

# Finite difference derivative on full 64-dimensional unitary's 2 encoded columns.
for k in range(4):
    ep=1e-3
    der=(unitary(H0+ep*Hterms[k],2*pi)@BC-unitary(H0-ep*Hterms[k],2*pi)@BC)/(2*ep)
    print('bond',k+1,'full gate derivative (central difference):',np.linalg.norm(der))

input_states=[B[:,0],B[:,1],(B[:,0]+B[:,1])/np.sqrt(2),(B[:,0]-B[:,1])/np.sqrt(2),(B[:,0]+1j*B[:,1])/np.sqrt(2),(B[:,0]-1j*B[:,1])/np.sqrt(2)]
inputs=W@np.column_stack(input_states)
ps=[]
def metrics(deltas):
    U=unitary(sum((1+dj)*H for dj,H in zip(deltas,Hterms)),2*pi)
    psi=U@inputs
    overlap=np.sum(np.conj(inputs)*psi,axis=0)
    fid=np.abs(overlap)**2
    kstates=W.conj().T@psi
    p_sing=np.sum(np.abs(kstates)**2,axis=0)
    cond_fid=fid/p_sing
    code_p=np.sum(np.abs(B.conj().T@kstates)**2,axis=0)
    return [np.mean(1-fid),np.mean(1-p_sing),np.mean(1-cond_fid),np.mean((p_sing-code_p)/p_sing)]
print('epsilon, full-state infidelity, false-flag rate, conditional-state infidelity, S>0 fraction within accepted')
for eps in [0.04,0.02,0.01,0.005]: print(eps, *['%.10g'%t for t in metrics([eps,0,0,0])])
print('common gain 5%, metrics=', metrics([.05]*4))
rng=np.random.default_rng(20261030)
for sigma in [0.005,0.015]:
    ar=np.array([metrics(rng.normal(0,sigma,4)) for i in range(500)])
    print('independent per-bond normal sigma',sigma,'means',ar.mean(axis=0),'se',ar.std(axis=0)/np.sqrt(len(ar)))

# Check second-order effective encoded Hamiltonian Q = 1/4 (sum_i delta_i S_i)^2
sample=np.array([.018,-.012,.008,-.003])
Dz=[sum(float(sample[i])*op(q,i,4)/2 for i in range(4)) for q in (X,Y,Z)]
DQ=sum(t@t for t in Dz)
H2=(B.conj().T@DQ@B)/4
U2=unitary(H2,2*pi)
U=unitary(sum((1+dj)*h for dj,h in zip(sample,Hterms)),2*pi)
KL=B.conj().T@W.conj().T@U@W@B
print('second-order H_eff /J =',H2)
print('actual logical singlet Kraus=',KL)
print('approx logical unitary=',U2)
print('Kraus-minus-approx norm',np.linalg.norm(KL-U2))