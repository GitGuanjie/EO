# Symmetry-Balanced Exchange-Only Measurements of Four-Spin Singlet Qubits

**PRX-format working draft · 1 November 2026 · not peer reviewed**

**Author:** Guanjie He (institutional affiliation and collaborators to be confirmed).

## Abstract

Detecting errors in spin-encoded information without introducing new control channels is a central challenge for silicon quantum processors. We investigate a four-electron singlet-only exchange qubit coupled to an ancillary singlet–triplet probe under the strict restriction of one positive isotropic exchange interaction at a time. An analytically solvable four-coupling collective probe cancels the first-order response to independent static bond-gain errors, but requires simultaneous exchange. We construct an 11-exchange serial detector with two routing SWAPs (13 pulses on a nearest-neighbor grid) that preserves arbitrary encoded singlet states and produces nontrivial total-spin error flags. The representation-theoretic kernel of the four-spin singlet code yields four physically distinct, equal-cost detectors. Under persistent 1.5% bond-gain offsets and 0.06% independent pulse fluctuations with ideal readout, balanced four-cycle operation reduces conditional logical infidelity from 1.30% to 0.028% at a fixed 52-pulse budget; the ideal worst-case spin-one detection rises from 77.2% to 95.3%. We identify a restricted numerical obstruction to exact cancellation using the existing fixed-angle modules and an exact-identity pulse family with an acceptance–fidelity trade-off. The work concerns heralded spin-sector error detection, not established decoded QEC.

## I. Introduction

Exchange-only encoding implements logic using pairwise Heisenberg couplings, reducing dependence on local microwave control at the price of encoded leakage and longer composite pulse words. This approach originates in exchange-universal quantum computation and decoherence-free subsystems [1,2] and has been developed through exchange-only readout, exact encoded gates and leakage reduction [3,4]. In particular, full-permutation decoupling in triple-dot spin qubits has already been experimentally demonstrated [5]; permutation symmetrization as a general idea is not claimed as new here. A digitally controlled silicon exchange-only processor has implemented repeated syndrome extraction and a four-qubit error-detecting code [6], establishing the need for system-level measurement-aware control.

Four-spin singlet-only exchange-only (SOEO) coding has a two-dimensional total-spin-zero logical sector. Earlier work studies always-on singlet-only exchange qubits [7,8] and an EO/single-spin hybrid error-detection architecture [9]. Those approaches use distinct always-on, single-spin or simultaneous-control resources. We ask whether **strict serial positive exchange** can produce a nondemolition SOEO spin-sector flag, and whether symmetry can refocus accumulated backaction across several repetitions without increasing exchange count. This local check is not equivalent to a high-level encoded XXXX or ZZZZ stabilizer.

## II. Physical model and operational task

The Hamiltonian is

\[
H(t)=\sum_{(i,j)\in E}J_{ij}(t)\,\mathbf S_i\cdot\mathbf S_j,\qquad J_{ij}(t)\ge0,
\]

with only one active bond per step. We use the positive exchange-area convention

\[
X_{ij}(a)=e^{i\pi aP^{s}_{ij}},\qquad P^{s}_{ij}=\tfrac14 I-\mathbf S_i\cdot\mathbf S_j,\qquad 0<a<2 .
\]

A pulse with area 1 is a SWAP up to an overall phase. The four-spin data are encoded in the two-dimensional total-spin-zero sector \(P_0\); the probe is a singlet on ancillary spins \(a,b\). The target is stronger than low average leakage:

\[
U(P_0\otimes |s_{ab}\rangle\langle s_{ab}|)=e^{i\phi}(P_0\otimes |s_{ab}\rangle\langle s_{ab}|).
\]

Thus the ideal operation fixes **every** unknown SOEO logical state; its ancillary singlet-versus-triplet readout must respond to nonzero data spin. The static physical-bond fractional gains \(\delta_e\) remain unchanged throughout a multi-round run, while the pulse-specific fluctuation \(\eta_{e,k}\) is renewed:

\[
a^{\rm act}_{e,k}=a_{e,k}(1+\delta_e+\eta_{e,k}),\quad
\sigma_{\rm pb}=0.015,\quad \sigma_{\rm iid}=0.0006.
\]

These are project-model values, not a fresh device-by-device HRL calibration.

## III. Analytically protected but nonserial collective reference

With four simultaneous equal couplings to one ancillary spin,

\[
H_\star=J\sum_{i=1}^{4}\mathbf S_i\cdot\mathbf S_a=J\mathbf S_D\cdot\mathbf S_a,
\]

the data spin-zero code is unchanged. If the ancillary singlet is measured after \(JT=2\pi\), the accepted Kraus operator and triplet effect on the data are

\[
K_s=P_0-\tfrac13P_1+\tfrac15P_2,\qquad
E_t=\tfrac89P_1+\tfrac{24}{25}P_2.
\]

For four independent star-bond gains \(\delta_i\), a first-order spin-one virtual excursion acquires gap \(-J\); the Dyson integral is proportional to \(\int_0^{2\pi/J}e^{iJt}\,dt=0\). Every independent gain derivative of the full encoded input evolution therefore vanishes to first order. The resulting single-cycle infidelity starts at order \(\sigma^4\), while second-order encoded rotations can still accumulate coherently. This exactly solvable limit establishes a control principle, **not a physically allowed strict-serial pulse**.

## IV. Nearest-neighbor serial realization

The native grid has data spin states initially on sites 4, 2, 6 and 9 and a physical ancillary singlet on 5, 8. A third EO gauge spin is a spectator at site 7. Execute an initial SWAP on bond 89, the following eleven chronological radial exchanges, and a final SWAP on 89. The four moved data states then couple to central spin 5 on native grid edges:

| Step | Bond | Positive area |
|---:|:---:|---:|
| 1 | 45 | 0.5192386333595181 |
| 2 | 56 | 1.5839512377735476 |
| 3 | 58 | 1.3682386550761760 |
| 4 | 56 | 1.5839512377735474 |
| 5 | 25 | 1.3905039171274718 |
| 6 | 45 | 1.4579153626294534 |
| 7 | 25 | 0.1730184425355885 |
| 8 | 56 | 0.3682386550761670 |
| 9 | 58 | 0.5839512377735380 |
| 10 | 56 | 0.3682386550761673 |
| 11 | 25 | 0.5192386333595033 |

A separate complete seven-spin \(128\)-dimensional verification on both EO gauge orientations produces ideal code residual \(2.19\times10^{-15}\). The data-spin-one triplet-detection-effect spectrum is \((0.30862,0.38170,0.95376)\); the data-spin-two detection rate is 82.11%. The single-shot worst-case spin-one detection is only 30.86%. Under the 1.5% static gain model, the native 13P word also incurs a false-triplet rate of approximately 0.672% and an accepted-state conditional infidelity of 0.0845%. **Unlike the nonserial collective reference, this detector is not first-order physical-gain-robust.**

## V. Klein-four symmetry produces equal-cost measurement instruments

The four-spin singlet code realizes the \([2,2]\) irreducible representation of \(S_4\). The Klein-four subgroup

\[
V_4=\{e,(12)(34),(13)(24),(14)(23)\}
\]

acts trivially on the full singlet code. If \(U\) is a code-preserving detector, \(W_gUW_g^\dagger\) is also code-preserving. Crucially, the permutation need not be physically applied: for each radial pulse one simply relabels its target bond,

\[
W_gX_{ia}(a)W_g^\dagger=X_{g(i)a}(a).
\]

This creates four forward 13P words, all with identical ideal code action but with different effects on leaked states. The inverse words follow from reversed pulse order and the positive-area replacement \(a\mapsto2-a\).

For an isolated detector, the minimum triplet-effect eigenvalue is 0.30862. A uniform choice among the four K4-related words has a mean detection-effect spectrum \((0.41698,0.41698,0.81014)\); the minimum expected detection rises to 41.70%. With four scheduled ideal probes, the worst-case cumulative spin-one detection is 77.15% for repeated fixed words, versus **95.28%** for \(F_0F_1F_2F_3\). This requires multiplying the actual conditional Kraus matrices, not simply raising averaged detection probabilities to powers.

## VI. Persistent per-bond gain is refocused across rounds

The conditional logical Kraus map of each ideal word is a scalar multiple of \(I_L\). Therefore its first-order *traceless* logical derivatives add under products. Symmetrically rotating the four radial physical roles reduces the multiple independent gain-error directions to a common-mode residual. This suppresses **accepted-logical** coherent backaction, not every physical-unitary derivative or false flag.

A 1000-realization Monte Carlo with independent 1.5% physical-bond gains held constant for all four rounds, plus 0.06% IID pulse jitter, finds:

| Four-round schedule | Pulses | Acceptance | Conditional logical infidelity |
|---|---:|---:|---:|
| Fixed \(F_0^4\) | 52 | ~97.43% | 1.298% |
| Balanced \(F_0F_1F_2F_3\) | 52 | ~97.46% | **0.02768%** |

This is a roughly 47-fold reduction in a **postselected model metric**, not decoded logical error rate. Longer 12-round protocols show a stronger derivative-space mechanism: the first-order projected coefficient \(H=\operatorname{tr}Q\) decreases from 536.28 (fixed) to 8.72 (K4 forward) and 0.02855 (8 forward plus 4 inverse). The last value is nonzero, and the protocol costs 156 pulses and twelve ideal readouts and resets.

The advantage requires temporally persistent gain. In the mixed model \(\delta_{e,r}=\sqrt{\rho}\delta_e^{\rm persistent}+\sqrt{1-\rho}\xi_{e,r}\), a 12-round K4 sequence is less attractive when \(\rho=0\). In 350-draw source comparisons, the K4 8F/4I conditional error changes from 1.001% at \(\rho=0\) to 0.0409% at \(\rho=1\). It is therefore a **correlation-matched control strategy**, not noise-independent decoupling.

## VII. Restricted no-go and exact numerical pulse family

Exhaustive search over 330 unordered four-module multisets from the four fixed-angle forward and four inverse 13P detector modules finds the smallest four-round leading conditional logical coefficient \(H=0.969279\) when using all four forward K4 modules. A continuous nonnegative weight relaxation over exactly those eight existing derivatives has strictly positive minimum \(H=0.000101532\) per unit total weight; numerical linear feasibility finds no zero derivative. This only excludes perfect first-order accepted-logical cancellation **within the fixed finite primitive pool** and is not a global no-go theorem.

An independent continuous deformation of the eleven central pulse angles preserves the ideal code identity. The constraint Jacobian is numerically rank 10 of 11, producing a local one-dimensional exact-identity family. One representative (\(t=0.12\)) reduces four-round \(H\) from 0.9693 to 0.7914 and maintains ideal worst-case spin-one detection at 95.33%. A paired 3000-realization study reports baseline conditional error 0.027260% versus 0.024265% for \(t=0.12\), **but** acceptance decreases from 97.413% to 96.996%. The lower projected tangent metric is not a Pareto improvement in operational throughput.

## VIII. Distinguishing local SOEO detection from full quantum error correction

Isotropic exchange preserves six-spin total angular momentum. For an initial spin-zero data block and ancillary singlet, acceptance of the final ideal ancillary singlet therefore enforces data \(S_D=0\) at *all* exchange pulse-area error orders. It does **not** enforce preservation of the logical X/Z information within that sector. Finite-depth fault detection has a nonzero false-negative probability; intra-code exchange miscalibrations are in general invisible to a total-spin-only flag.

A separate encoding identity represents the SOEO singlet as a three-spin EO logical qubit with its gauge entangled with a fourth reference spin. Thus a full-gauge-independent EO gate \(U_L\otimes I_g\) can be lifted to SOEO by leaving the reference spin untouched. The existing nine-spin EO parity instrument motivates 11-spin two-SOEO-data/EO-ancilla parity extraction, but its full native 11-spin physical measurement and decoder have not been verified here. Four SOEO data blocks plus one EO ancilla would require 19 physical spins; the 13P local spin detector does not directly perform their encoded XXXX or ZZZZ stabilizer.

This work does not contain calibrated singlet-triplet measurement errors, nonideal reset, hardware gate-time-normalized performance, detailed leakage-recovery circuitry, or a complete repeated high-level code/decoder. It cannot claim fault tolerance, an error-correction threshold, or experimental performance.

## IX. Conclusion

The result is a strict-positive, short serial spin-sector measurement coupled to symmetry-based suppression of persistent accepted-branch backaction, not a universally robust quantum gate. The main contribution is showing how the **kernel of an encoded representation** supplies cost-preserving physical alternatives to the *same logical measurement instrument* whose sequencing matters under correlated errors. A next-stage system claim requires hardware-matched noise and readout, complete high-level EO–SOEO parity extraction and a decoder evaluated at equal physical time, not just an accepted-state fidelity plot.

## References

[1] D. P. DiVincenzo *et al.*, Nature **408**, 339 (2000). https://doi.org/10.1038/35042541

[2] D. Bacon *et al.*, Phys. Rev. Lett. **85**, 1758 (2000). https://doi.org/10.1103/PhysRevLett.85.1758

[3] J. Medford *et al.*, Nat. Nanotechnol. **8**, 654 (2013). https://doi.org/10.1038/nnano.2013.168

[4] B. H. Fong and S. M. Wandzura, Quantum Inf. Comput. **11**, 1003 (2011). https://doi.org/10.26421/qic11.11-12-9

[5] B. Sun *et al.*, PRX Quantum **5**, 020356 (2024). https://doi.org/10.1103/PRXQuantum.5.020356

[6] Members of the HRL Quantum Team and Collaborators, Nature **655**, 1154 (2026). https://doi.org/10.1038/s41586-026-10754-7

[7] N. L. Foulk *et al.*, Phys. Rev. Lett. **135**, 106202 (2025). https://doi.org/10.1103/j1hn-k5m8

[8] N. L. Foulk *et al.*, Phys. Rev. B accepted September 2026. https://doi.org/10.1103/8bzz-rw2j

[9] I. Heinz, M. Sharma, and J. Kattemölle, arXiv:2608.14214 (2026). https://arxiv.org/abs/2608.14214

[10] I. Heinz *et al.*, PRX Quantum **6**, 030353 (2025). https://doi.org/10.1103/njq3-fcdd

*Data and code*: prior results are archived in this repository's SOEO_EO_QEC folders. The present Markdown page is a revision-oriented companion; the full 7-page REVTeX typeset paper, 8-page mathematical supplement, 5 figures and complete source archive are supplied separately with this revision's downloadable bundle.