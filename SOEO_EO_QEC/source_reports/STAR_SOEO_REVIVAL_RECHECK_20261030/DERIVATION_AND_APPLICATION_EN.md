# Four-data SOEO spin-sector detection by exchange-only singlet-pair probe
## Independent analytic and numerical recheck, 30 October 2026

**Status:** mathematically derived and verified with a full 64-dimensional, six-spin representation. **Not demonstrated in hardware, not a known native strict-serial pulse sequence, and not claimed to appear in arXiv:2608.14214v1**. The cited paper (Heinz, Sharma, Kattemölle) investigates a *different* three-coupling EO gauge transfer at Jt=pi and LD+SOEO error detection. Literature novelty of this particular four-coupling extension has not been established.

### Physical system
Four spin-1/2 data spins D=(1,2,3,4), restricted initially to the two-dimensional total-data-spin S_D=0 singlet-only exchange-only (SOEO) code; two ancillas a,b initialized in a two-spin singlet. During the probe, b is decoupled. All four strictly positive equal couplings J_{ia}=J must run **simultaneously**:

```
H0 = J * (S1+S2+S3+S4).Sa = J S_D.Sa
U0 = exp(-i H0 T),  T = 2*pi/J, hbar=1.
```
Then measure singlet/triplet (S/T) on a,b. No physical single-spin H, X, Z pulses are required, but physical preparation and S/T readout remain prerequisites. The 4-star hardware geometry does not fit the user's historical strict one-bond-at-a-time control model.

### Exactly solved ideal measurement
On data total-spin sector S=0,1,2, write its projector P_S. Singlet survival Kraus operator K_s = <S_ab|U0|S_ab>. Clebsch-Gordan decomposition gives

```
A_S(T)= [(S+1)*exp(-i*J*S*T/2) + S*exp(i*J*(S+1)*T/2)]/(2*S+1)
K_s(T)=sum_S A_S(T) P_S.
```
For JT=2*pi, A0=1, A1=-1/3, A2=+1/5, so

```
K_s = P0 - P1/3 + P2/5;
E_s = K_s^dag K_s = P0 + P1/9 + P2/25;
E_t = I-E_s = (8/9)P1 + (24/25)P2.
```
Single physical Pauli error on data S=0 is entirely mapped into data S=1, hence one ideal probe detects it with probability 8/9, not 100%. n ideal independent repeated probes miss such an error with probability (1/9)^n; this is still O(p) for fixed n, not formally single-fault tolerant. The ideal filter is not a deterministic projective P0 measurement, despite excellent heralding.

### Strong first-order cancellation for four independent quasi-static gains
Set J_ia=J(1+delta_i) fixed throughout one pulse. V = J sum_i delta_i S_i.Sa. Since (i) any local data spin operator sends S_D=0 into S_D=1, (ii) total F=S_D+Sa is conserved for each isotropic scalar Si.Sa, only Q=(S_D=1,F=1/2,E=-J) is reachable at first order, while the code energy is 0. In Dyson expansion,

```
dU/d(delta_i)|0 P0 = -i J int_0^T exp(i J (T-t)) dt * (Si.Sa) P0
                       = -(exp(i JT)-1) (Si.Sa) P0 = 0 for JT=2*pi.
```
The derivative zero is for the **full unitary acting on the code input**, not only an average fidelity or conditional measurement. For simultaneous small gain biases, U(T)P0=P0+O(||delta||^2), so single-operation pure-state infidelity is O(||delta||^4). If all delta_i are the same, V=delta H0 and the code is completely unaffected to all orders. Time-dependent jitter, off-target JT, non-Heisenberg gradients and extra spectator couplings generally destroy the argument. For a sole bond gain delta at arbitrary JT, the leading infidelity is `(3/4)*sin^2(JT/2)*delta^2` (plus higher orders): the zero of the quadratic error coefficient at JT=2*pi is a genuine revival.

### The remaining second-order logical Hamiltonian
Let D = sum_i delta_i S_i and P0 the data spin-zero projector. The second-order effective code Hamiltonian is

```
H_eff^(2) = (J/4) P0 D^2 P0
          = h0 I + (sqrt(3)J/8)(B-C) X_L + (J/8)(-2A+B+C) Z_L,
A = delta1*delta2 + delta3*delta4,
B = delta1*delta3 + delta2*delta4,
C = delta1*delta4 + delta2*delta3.
```
Thus nonuniform gains leave O(delta^2) *coherent logical rotations*. Single-round infidelity is O(delta^4), but holding the *same* gain vector over n accepted cycles can accumulate logical error approximately as n^2 sigma^4 before saturation, even when the ancilla rarely flags. This detector does **not** correct coherent exchange overrotations acting entirely within the SOEO code, since [S_D^2, Si.Sj]=0 for data-only isotropic exchange.

### All-order code-sector closure of singlet-accepted branch
Total spin of all six physical spins S_all=S_D+Sa+Sb is 0 initially (data spin0 times ancilla singlet). Arbitrary SU(2)-invariant exchange evolution preserves S_all=0. Postselecting the two ancillas onto S_ab=0 forces the remaining four data spins to be S_D=0. Hence the accepted Kraus branch cannot end with DATA total-spin leakage, **to all orders in arbitrary Heisenberg exchange-gain errors**, assuming correct initial state, ideal ancilla singlet preparation/readout, and no anisotropic/local-magnetic errors. Nevertheless, within-code logical X_L/Z_L rotations can still occur. A triplet ancilla result in this initial situation certifies the data are outside the S=0 code after the interaction.

### Reproduced numerical baselines
Full 64x64 exact diagonalization, six logical Pauli eigenstates where relevant:

Single-bond fractional gain delta | full six-spin infidelity
- 0.04 | 4.812884269e-6
- 0.02 | 2.987496774e-7
- 0.01 | 1.859337336e-8
- 0.005 | 1.159414231e-9

Independent Gaussian gains, sigma=0.015, 500 shots, seed 20261030:
- mean full-state infidelity 1.20e-6;
- mean ancilla triplet flag 7.47e-7;
- mean conditional accepted logical infidelity 4.53e-7.

Independent Gaussian gains, sigma=0.015, 240 shots, seed 42, **one static vector per 100-cycle trajectory**:

|n accepted-probe opportunities| mean probability all ancilla results singlet | mean conditional logical infidelity|
|---:|---:|---:|
|1|0.999999245|4.99e-7|
|5|0.999996224|1.25e-5|
|10|0.999992448|4.99e-5|
|20|0.999984896|1.99e-4|
|50|0.999962243|1.24e-3|
|100|0.999924494|4.88e-3|

These are **only exchange-gain and ideal-measurement toy-model** outcomes, not a logical QEC error rate. Real multi-round errors from correlated noise could be substantially worse or different.

### Actual QEC application / missing milestones
A test protocol is: prepare SOEO code; prepare fresh singlet pair; apply the four-bond star for T=2*pi/J; measure S/T; if triplet, raise a **probabilistic erasure/leakage flag** to a higher-level decoder or abort/reprepare; if singlet, retain the block without projecting its logical superposition. Repeat n times if lower miss probability is required, considering extra readout time. The resulting filter is **not** the encoded high-level `X_A X_B X_C X_D` measurement: those X_A represent four separate EO blocks and need a different logical ancilla instrument.

To validate a usable architecture: design a real four-way equal-J coupling and S/T readout, or discover an exact positive-J strict-serial composite with the same first-derivative and heralding properties; include readout, idle, magnetic gradients, same-gain-across-cycles and context effects; compare accepted fidelity and yield, unflagged error, leakage, gate duration and decoded high-level error. No such verified strict-serial implementation is supplied here.