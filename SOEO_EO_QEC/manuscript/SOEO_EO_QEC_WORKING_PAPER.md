---
title: "Exchange-Only Singlet-Sector Detection and Symmetry-Based Noise Suppression for Hybrid SOEO–EO Quantum Error Correction"
subtitle: "A consolidated theoretical and numerical working paper"
date: "1 November 2026"
lang: en
geometry: margin=0.86in
fontsize: 10pt
numbersections: true
colorlinks: true
linkcolor: MidnightBlue
urlcolor: MidnightBlue
header-includes:
  - '\usepackage{amsmath,amssymb,booktabs,longtable,microtype}'
  - '\usepackage{float}'
  - '\usepackage{fancyhdr}'
  - '\pagestyle{fancy}\fancyhf{}\fancyhead[L]{SOEO--EO QEC | Working Draft}\fancyhead[R]{\thepage}'
  - '\renewcommand{\headrulewidth}{0.35pt}'
  - '\setlength{\headheight}{14pt}'
  - '\usepackage{caption}'
  - '\captionsetup{font=small,labelfont=bf}'
abstract: |
  This technical working paper consolidates an exchange-only research sequence on low-level total-spin detection of four-spin singlet-only exchange-only (SOEO) qubits, hybridization with three-spin exchange-only (EO) ancillas, and symmetry-based mitigation of correlated pulse-area errors. An ideal four-link simultaneous-exchange probe admits an analytic singlet-return Kraus map and cancels the first-order response to four independent quasi-static bond-gain errors on encoded inputs, but is incompatible with strict one-bond-at-a-time control. A numerically constructed 11-pulse strictly serial detector, embedded into a nearest-neighbor 3x3 grid with two routing SWAPs (13 pulses total), reproduces the required nominal SOEO code identity and produces nontrivial spin-sector detection. Klein-four bond reassignment yields four equivalent physical detectors; cycling through them reduces accepted-branch logical error under persistent bond gain in a restricted simulated model. A one-parameter family of exact 13-pulse words offers a modest further reduction in conditional logical infidelity but worsens acceptance. The work does not demonstrate fault-tolerant quantum error correction, physical hardware performance, or a decoded logical error threshold. Exact algebraic statements, numerically certified ideal circuits, and noise-model estimates are explicitly distinguished throughout.
---

> **Research status and attribution.** This is an **unreviewed working draft**, prepared from project research reports dated 30--31 October 2026. It is not a journal publication, an independently replicated hardware experiment, or evidence of literature priority. Authors, affiliations, acknowledgements, permission to release, and detailed hardware comparisons must be confirmed before public dissemination. Source datasets and scripts are included separately in this package. Unless explicitly stated, all numbers refer to an idealized theoretical or Monte Carlo model.

# Introduction and research question

Exchange-only (EO) spin qubits encode a logical two-level system in the spin-$1/2$ multiplicity of three physical electron spins. Their appeal is that encoded control can be achieved using isotropic Heisenberg exchange, with physical singlet preparation and singlet--triplet (S/T) measurement as additional resources. A four-spin singlet-only exchange-only (SOEO) qubit instead uses the two-dimensional $S_D=0$ sector. This avoids dependence on a three-spin $m=\pm1/2$ gauge label, but it does not make every encoded logical error detectable.

Heinz, Sharma, and Kattemölle [1] proposed low-level error detection in a **hybrid SOEO + single-spin Loss--DiVincenzo (LD)** device using physical-spin $XXXX$ and $ZZZZ$ stabilizer checks and flag qubits. The requisite physical single-spin LD rotations are **not** present in a strict exchange-only model. The present working project therefore asks a different question:

> Can a native, strictly serial, positive-Heisenberg-exchange circuit transfer evidence of SOEO total-spin leakage into an EO singlet/triplet ancilla; and can correlated exchange-gain errors be suppressed without adding pulses?

This low-level measurement targets data total spin $S_D=0$ versus $S_D>0$. It is **not** the high-level encoded check $X_A X_B X_C X_D$ on four separate EO or SOEO logical qubits. A complete QEC architecture would require both kinds of operations, a recovery model and a decoder.

The project stages summarized here are the simultaneous-star analytic baseline; the native 11P/13P detector; the Klein-four (K4) equivalent-instrument family and multi-round echo; and a numerical exact-identity parameter manifold with an explicitly limited no-zero result for the original finite primitive pool.

![Schematic distinction between local SOEO error detection and high-level EO parity processing.](figures/architecture.png){width=92%}

# Physical model and notation

The physical control is

$$
H(t)=\sum_{\langle i,j\rangle}J_{ij}(t)\,\mathbf S_i\cdot\mathbf S_j,\qquad J_{ij}(t)\ge0.
$$

The strict serial class permits only one active bond per step. Using the project's exchange pulse convention,

$$
X_{ij}(a)=\exp\!\left(i\pi a P_{ij}^{(s)}\right),\qquad
P_{ij}^{(s)}=\tfrac14 I-\mathbf S_i\cdot\mathbf S_j,\quad 0<a<2.
$$

A pulse with $a=1$ implements SWAP up to a global phase. Static per-physical-bond gain errors and pulse-to-pulse errors are respectively

$$
J_{b,k}^{\rm actual}=J_{b,k}\big(1+\delta_b+\eta_{b,k}\big),\quad
\delta_b\sim\mathcal N(0,\sigma_{\rm pb}^2),\quad
\eta_{b,k}\sim\mathcal N(0,\sigma_{\rm iid}^2).
$$

In the key correlation-sensitive simulations, $\sigma_{\rm pb}=0.015$ persists across a full sequence of measurement rounds while $\sigma_{\rm iid}=0.0006$ is renewed per pulse. These are **project benchmark parameters informed by previous HRL-focused modeling**, not a new extraction of measured bond-by-bond error rates from the HRL device [2]. The model omits realistic magnetic noise, context-dependent exchange calibration, readout confusion, finite reset times and NZ1 idle schedules.

We label a result as **ANALYTIC** when derived from the defined ideal Hamiltonian, **NUMERICALLY VERIFIED** when checked by full-spin or representation-sector computations, **MODEL-ONLY** when based on simulated noise, and **OPEN** when a required physical or systems-level validation is missing. These categories are deliberately not interchangeable.

# Four-bond star: analytically solvable reference

## Ideal spin-sector measurement

Take four data spins $D=(1,2,3,4)$, initially supported in the two-dimensional singlet code $S_D=0$, and an auxiliary pair $(a,b)$ prepared in the physical spin singlet $|S_{ab}\rangle$. The ideal reference Hamiltonian temporarily turns on **four simultaneous, equal** positive couplings:

$$
H_\star=J\sum_{i=1}^{4}\mathbf S_i\cdot\mathbf S_a
=J\mathbf S_D\cdot\mathbf S_a,\qquad T=2\pi/J.
$$

The second ancillary spin $b$ is inert during the interaction. Since $\mathbf S_D|\psi_{S_D=0}\rangle=0$, the unitary acts as identity on every correctly encoded SOEO state. After evolution, a physical S/T measurement on $(a,b)$ gives a singlet-return Kraus operator

$$
K_s(T)=\sum_{S=0}^{2}A_S(T)P_S,\qquad
A_S(T)=\frac{(S+1)e^{-iJST/2}+S e^{iJ(S+1)T/2}}{2S+1}.
$$

At the selected revival time,

$$
\boxed{K_s=P_0-\tfrac13P_1+\tfrac15P_2,\quad
E_t=\tfrac89P_1+\tfrac{24}{25}P_2.}
$$

The triplet outcome therefore detects an already-existing data $S_D=1$ error with probability $8/9$, and an $S_D=2$ input with probability $24/25$. This is an **imperfect filter**, not a projective one-shot $P_0$ measurement. Ideal repeated acceptance has miss probability $(1/9)^n$ on an $S=1$ sector state only when each ancillary pair is freshly prepared and no new faults intervene.

## Full first-order cancellation for quasi-static star gains

Let the four star bonds carry independent static deviations $\delta_i$:

$$
H=H_\star+V,\qquad
V=J\sum_{i=1}^{4}\delta_i\mathbf S_i\cdot\mathbf S_a.
$$

Acting once on a data singlet, the vector $\mathbf S_i$ can only reach $S_D=1$. The isotropic scalar product also preserves $F=S_D+S_a$; hence the only first-order intermediate sector is $S_D=1,F=1/2$, with energy $-J$, relative to the encoded initial energy $0$. Therefore

$$
\left.\frac{\partial U(T)}{\partial\delta_i}\right|_{\boldsymbol\delta=0}P_0
=-iJ\int_0^T e^{+iJ(T-t)}dt\,(\mathbf S_i\cdot\mathbf S_a)P_0
=0\qquad (JT=2\pi).
$$

This is cancellation of the **full first-order error amplitude on the encoded initial subspace**, not merely cancellation of an averaged fidelity. Thus, for small quasi-static offsets and a single probe, $1-F=O(\|\boldsymbol\delta\|^4)$. For perfectly common gains $\delta_i=\delta$, $V=\delta H_\star$ and the data code is undisturbed to all orders.

The second-order residual has an encoded logical component,

$$
H_{\mathrm{eff}}^{(2)}=\frac J4P_0\left(\sum_i\delta_i\mathbf S_i\right)^2P_0
=h_0I+\frac{\sqrt3J}{8}(B-C)X_L+\frac J8(-2A+B+C)Z_L,
$$

where $A=\delta_1\delta_2+\delta_3\delta_4$, $B=\delta_1\delta_3+\delta_2\delta_4$, and $C=\delta_1\delta_4+\delta_2\delta_3$ in the stated logical convention. Under gain offsets persistent across cycles, this coherent $O(\delta^2)$ logical rotation can accumulate as approximately $n^2\sigma^4$ in accepted-state infidelity before saturation.

The original project report verified this analytic construction by six-spin 64-dimensional propagation. At $\sigma_{\rm pb}=1.5\%$, a 500-draw static-gain ensemble gave a mean conditional accepted logical infidelity of $4.53\times10^{-7}$ for the specified six-state input set. Over 100 **persistent-gain** accepted-probe opportunities, a separate 240-draw ensemble gave approximately $4.88\times10^{-3}$ conditional infidelity despite near-unit acceptance. These Monte Carlo figures are illustrative rather than experimental performance.

**Hardware limit.** Four simultaneous equal star couplings violate the historical strict serial constraint. The star result is an analytical control target, not a valid one-bond-at-a-time pulse schedule.

# Native 3x3-grid detector: 11P core plus routing

## Physical layout, pulse convention and resource accounting

A subsequent numerical search in SU(2)-reduced spin multiplicity representations produced an **11-pulse serial positive-exchange** detection core. Add two full-SWAP routing pulses to embed it in a nearest-neighbor 3x3 grid (row-major sites 1--9): four SOEO data spin states initially on sites $(4,2,6,9)$, EO ancillary triple on $(5,8,7)$, with ancillary singlet initially on $(5,8)$ and gauge spectator 7. A SWAP on $J_{89}$ moves the ancillary singlet partner to site 9 and the data spin to site 8; the central site 5 then has radial access to four data states via $J_{45},J_{25},J_{56},J_{58}$. A final $J_{89}$ SWAP restores the locations before the $J_{58}$ S/T readout.

The full chronological 13P word is supplied in `../data/GRID_13P_SOEO_SPIN0_DETECTOR.csv`. Its eleven central bond-area pairs are:

| Step | Physical bond | Positive area $a$ |
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

These are numerical pulse-area solutions, not closed-form algebraic angles or a globally proven pulse minimum. Physical initialization, S/T assignment, reset and any additional data-pair routing are **not included** in the 13P resource count.

## Ideal quantum action and fault-detection contrast

The target code action is

$$
U_{13}\big(|\psi_{S_D=0}\rangle|S_{ab}\rangle|m_g\rangle\big)
=e^{i\phi}|\psi_{S_D=0}\rangle|S_{ab}\rangle|m_g\rangle,
$$

for arbitrary SOEO logical superpositions and both EO ancilla gauge orientations. The project report records full seven-spin $128\times128$ propagation with a nominal residual of $2.19\times10^{-15}$ on the initialized code/gauge inputs. The auxiliary triplet probability for a uniformly sampled $S_D=1$ multiplicity state is $0.54803$, and for $S_D=2$ it is $0.82108$. Over the four physical SOEO data sites, single-site Pauli errors gave average detection rates between approximately $0.509$ and $0.584$ for the tested logical input ensemble. The smallest **state-dependent** detection value in that tested one-fault class was only $0.3086$; the average must not be advertised as a worst-case guarantee.

The serial word **does not** retain the star's static-gain first-order cancellation: at the five physical bonds $(45,25,56,58,89)$ the single-round tangent Gram matrix has $\operatorname{tr}Q=33.5447>0$, with all five reported eigenvalues positive. At $\sigma_{\rm pb}=1.5\%$, a 1,200-draw ideal-readout model reported an accepted-state conditional error of $0.08446\%$, a false-triplet rate of $0.67194\%$, and full-state error of $0.75544\%$. Consequently this is a **nominally exact** strict-serial detector, not a first-order gain-robust physical detector.

# Klein-four equivalent instruments and multicycle control

## Symmetry derivation

The two-dimensional four-spin singlet code carries the $[2,2]$ representation of the permutation group $S_4$. The Klein-four subgroup

$$
V_4=\{e,(12)(34),(13)(24),(14)(23)\}
$$

acts trivially on the whole code. If the eleven-pulse core $U$ fixes the SOEO code and the ancillary singlet up to a scalar phase, then $U_g=W_gUW_g^\dagger$ does so for all $g\in V_4$. There is no need to physically insert $W_g$: the exchange identity

$$
W_gX_{ia}(a)W_g^\dagger=X_{g(i)a}(a)
$$

allows one to **reassign the existing radial physical bond** for each pulse, preserving the pulse count and positivity. Four forward detectors $F_0,\ldots,F_3$ and four reverse positive-area detectors $I_0,\ldots,I_3$ were checked against full seven-spin propagation in the source computational reports.

For input data spin-1 multiplicity, the original single-cycle triplet detection effect $E=I-K^\dagger K$ has eigenvalues $(0.30862,0.38170,0.95376)$. The uniform mixture over the four $V_4$ relabelings instead yields $(0.41698,0.41698,0.81014)$. Hence random assignment raises the worst-case **expected** one-cycle detection from $30.86\%$ to $41.70\%$, without asserting that every individual shot has this detection probability. In ideal noiseless repeated measurements, four deterministic $F_0,F_1,F_2,F_3$ cycles raise the worst-case spin-1 cumulative detection from $77.15\%$ (one word repeated four times) to $95.28\%$.

## Persistent-gain Monte Carlo

Under $\sigma_{\rm pb}=0.015$ held constant over all cycles, independent $\sigma_{\rm iid}=0.0006$ per pulse, ideal S/T measurement and reset, the original project reports the following **conditional accepted-state** results. Data are based on 1,000 noise realizations and average over a set of logical input eigenstates, rather than real hardware measurements.

| Schedule | Exchange pulses | All-accepted probability | Conditional logical-state infidelity |
|:--|--:|--:|--:|
| Fixed 13P $\times4$ | 52 | 97.43% | 1.298% |
| Four K4 forward variants | 52 | 97.46% | **0.02768%** |
| Fixed 13P $\times12$ | 156 | 92.63% | 10.175% |
| Twelve K4 forward variants | 156 | 92.69% | 0.24361% |
| K4 with 8 forward + 4 inverse | 156 | 91.63% | **0.04186%** |

![Four-cycle comparison: models with the same 52-pulse count. R146 t=0.12 data are from a different 3,000-paired-draw ensemble, so fine cross-study differences are not paired.](figures/four_cycle_comparison.png){width=89%}

The physical importance of the K4 schedule is **not** the exact decimal factor but that symmetry-balanced relabeling suppresses **persistent coherent** accepted-logical error while costing no extra exchange pulses within a fixed four-cycle protocol. Four readouts, four ancilla preparations and resets are still required and are excluded from the pulse count.

For 12 cycles, the accepted-state first-order gain sensitivity trace dropped from $536.28$ (fixed) to $8.72$ (K4 forward) and $0.02855$ (K4 8F/4I), in the report's tangent normalization. The last is small, **not zero**; it is neither an all-channel physical derivative cancellation nor proof that the full measurement instrument is $O(\sigma^4)$.

Correlation stress was decisive. Replacing a fraction of the across-cycle gain by fresh per-cycle fluctuations yields the reported conditional logical infidelities:

| Persistent fraction $\rho$ | Fixed F$\times12$ | K4 forward$\times12$ | K4 8F+4I |
|---:|---:|---:|---:|
| 0 | 0.859% | 1.015% | 1.001% |
| 0.5 | 5.234% | 0.576% | 0.471% |
| 0.9 | 10.053% | 0.329% | 0.141% |
| 1 | 10.921% | 0.250% | 0.0409% |

![Model-only accepted-state performance under varying gain correlation.](figures/correlation_stress.png){width=89%}

At $\rho=0$ the symmetry schedule can be worse than the fixed schedule. The proposed sequence is thus a **correlation-matched control design**, not a universally preferred detector.

# Restricted obstruction and exact parameter manifold

## Fixed primitive pool does not allow complete accepted-logical first-order cancellation

For the eight fixed-angle 13P words $F_g,I_g$, the first-order traceless logical derivative of a product of nominally identity accepted Kraus operators is the sum of the individual derivatives. A finite computational search over all four-word multisets (330 combinations) produced $H_{\rm accepted}=0.9692788$ for the four distinct forwards, the smallest value in that pool for exactly four cycles. Optimizing arbitrary nonnegative normalized weights over the **same eight fixed derivatives** gave a strictly positive minimum $1.01532\times10^{-4}$ and an infeasible exact-zero linear program. These results exclude *zero within that derivative cone*, up to numerical solver accuracy. They do **not** constitute a universal no-go theorem for arbitrary exchange sequences or altered angles.

## Numerical identity-preserving 13P manifold

The eleven central areas were varied subject to the exact initialized-code identity constraint

$$
U(\mathbf a)B=e^{i\phi(\mathbf a)}B,
$$

where $B$ is the two-column $S_D=0\otimes$singlet isometry in the six-spin total-spin-zero multiplicity sector. The numerical Jacobian at the source word has rank 10 of 11, revealing a **local one-dimensional solution family**. Projected continuation gives new 13P detector words with nominal full seven-spin residuals around $10^{-15}$--$10^{-14}$, keeping all exchange areas positive and the same grid routing.

| Continuation parameter $t$ | Four-cycle $H_{\rm accepted}$ | Worst-case ideal 4-cycle spin-1 detection | 13P total area |
|---:|---:|---:|---:|
| 0 | 0.969279 | 95.2817% | 11.9165 |
| 0.08 | 0.827620 | 95.4383% | 12.1023 |
| 0.12 | 0.791431 | 95.3342% | 12.1902 |
| 0.16 | 0.770600 | 95.1037% | 12.2744 |
| 0.26 | 0.755549 | 93.8734% | 12.4660 |

![A numerically exact pulse-angle manifold yields a nontrivial detection/noise trade-off.](figures/manifold_tradeoff.png){width=89%}

A separate paired 3,000-realization persistent-gain + IID study reported:

| 52P detector family | Four-cycle acceptance | Accepted-state conditional infidelity |
|---|---:|---:|
| Source, $t=0$ | **97.4132%** | 0.027260% |
| Reoptimized, $t=0.12$ | 96.9962% | **0.024265%** |
| Low-$H$ candidate, $t=0.26$ | 96.4587% | 0.024736% |

The $t=0.12$ candidate improved conditional infidelity by approximately $11\%$ *relative* to the source in that paired model, but reduced acceptance by $0.417$ percentage points. It therefore is **not a Pareto-dominating improvement** in system throughput or experimental time. The best analytical tangent score at $t=0.26$ did not yield the smallest finite-noise error. Further work must evaluate the complete POVM, readout confusion, state recovery and hardware duration.

# Hybrid EO--SOEO operation and high-level code integration

A four-spin SOEO singlet may be written as a three-spin EO logical degree of freedom with its gauge entangled with a fourth reference spin:

$$
|\widetilde\ell\rangle=\frac{1}{\sqrt2}
\left(|\ell,+\rangle_{123}|\downarrow\rangle_4
-|\ell,-\rangle_{123}|\uparrow\rangle_4\right),\quad \ell=0,1.
$$

Consequently, a three-spin encoded gate exactly equal to $U_L\otimes I_g$ on both EO gauge sectors can be lifted to the four-spin SOEO code by leaving the reference spin untouched. This is an algebraic criterion, **not** a guarantee for a device using a specific sequence. A gauge-dependent gate or a sequence that leaks mid-operation and does not return correctly is not covered by an unrestricted claim.

In earlier project reports (R143/R144), a 47P/25D gauge-inclusive nine-spin $Z_AZ_C$ measurement instrument was reported on a 3x3 exchange grid. The current working data suggest a possible two-SOEO-data + one EO-ancilla 11-spin hybrid $ZZ$ measurement using the same nine active spins plus two reference spectators. But the complete chronological 47P physical CSV and its **independent 11-spin hybrid rerun are not part of this working-paper evidence bundle**. This remains an OPEN integration milestone. Similarly, an encoded $XXXX$ check on four SOEO data blocks requires 4$\times$4 + 3 = **19 physical spins**, even if only 15 are active in the lifted logic; an extra three-spin EO flag would increase the physical count to 22. The low-level SOEO $S_D=0$ detector does not substitute for these high-level encoded stabilizer measurements.

An independent toy seven-spin gap-mediated SOEO--EO entangler produced an $O(g^2/\Delta)$ effective $Z_AZ_B$ term, but severe sensitivity to independent intra-SOEO gain offsets. In that report, a nominal $99.78\%$ theoretical gate fell near $49\%$ average fidelity when the idealized all-to-all inner-bond model was stressed with independent 1.5% static gains. This negative result argues *against* prioritizing a long always-on-gap entangler without a separate calibrated hardware model. It does **not** rule out the SAGE architecture [3], which uses different control assumptions.

# Scope of fault tolerance, limitations and research priorities

Under isotropic exchange, total six-spin angular momentum is conserved. Starting with data $S_D=0$ and an ancillary singlet, an ideal singlet-accepted branch leaves the data in $S_D=0$, even with arbitrary exchange-area gain offsets, because the total initial spin is zero. This is **all-order spin-sector closure** for that ideal model. It does not eliminate logical rotations within the $S_D=0$ code. The detector has finite probability to miss an actual single-spin fault within a fixed number of cycles; consequently an $O(p)$ unflagged component can remain. The proposed protocol is thus **heralded low-level error detection**, not proven single-fault-tolerant QEC.

A rigorous experimental or systems-level claim requires the following additional tests:

1. Reconstruct the full logical and physical instrument for all detector outcomes, with gauge, leakage and **physical** S/T measurement POVMs; include realistic ancilla reset and preparation failure.
2. Implement a native high-level mixed SOEO--EO $ZZ/XX$ check and eventually $XXXX/ZZZZ$, including all reference spins, accessible graph edges, hook-error propagation, idle operations and native pulse time.
3. Measure or fit the gain correlation time and include the same bond errors throughout repeated full QEC cycles; benchmark against IID pulses, crosstalk/context errors and nuclear-spin fluctuations.
4. Evaluate **decoded logical error per unit wall-clock time**, acceptance/rejection throughput and code distance, not only the accepted-state six-state fidelity.
5. Verify full pulse sequences from independently loaded CSVs and independent physical representations, including derivatives and worst-case fault detection. A rigorous finite-family impossibility claim requires interval/validated arithmetic, not only float-based LP infeasibility.
6. Conduct a targeted prior-art comparison before making novelty or publication-priority claims. Full-permutation EO dynamical decoupling predates these working reports [4].

# Conclusion

A short strictly serial and nearest-neighbor native-exchange SOEO singlet-sector detector is numerically available, and Klein-four relabeling offers a no-extra-pulse method to control **persistent** accepted-branch coherent errors in an idealized measurement model. The simultaneous-star analytic revival offers a distinct and stronger first-order cancellation principle but requires hardware controls outside the serial class. The numerical exact-identity manifold supplies a modest further finite-noise optimization with an explicit acceptance trade-off. The most important next research step is **not pulse padding**: it is to marry native low-level SOEO heralding to a physically verified higher-level EO/SOEO parity instrument and a decoder, with truthful hardware-time and readout costs.

# References and provenance

1. I. Heinz, M. Sharma, and J. Kattemölle, *Exchange-only qubit stabilized by a single-spin qubit*, arXiv:2608.14214v1 (2026). <https://arxiv.org/abs/2608.14214>. **External paper: hybrid LD/SOEO control, not the native 13P construction.**
2. Members of the HRL Quantum Team and Collaborators, *A digitally controlled silicon quantum processing unit*, *Nature* **655**, 1154--1159 (2026). <https://doi.org/10.1038/s41586-026-10754-7>. **Experimental reference; the project noise simulation is not an HRL device measurement.**
3. N. L. Foulk *et al.*, *Singlet-Only Always-On Gapless Exchange Qubits with Baseband Control*, *Physical Review Letters* **135**, 106202 (2025). <https://doi.org/10.1103/j1hn-k5m8>. **Different always-on physical architecture.**
4. B. Sun *et al.*, *Full-Permutation Dynamical Decoupling in Triple-Quantum-Dot Spin Qubits*, *PRX Quantum* **5**, 020356 (2024). <https://doi.org/10.1103/PRXQuantum.5.020356>. **Prior art on permutation-based exchange decoupling.**
5. Internal computational reports (unpublished working materials): *Star SOEO Revival Recheck* (30 Oct 2026), *SOEO--EO Hybrid* (30 Oct), *Native-Grid QED* (30 Oct), *K4 Echo R145* (31 Oct), and *R146 Pareto/No-Go* (31 Oct). Full source report text and selected reproducibility scripts and pulse files accompany this paper; numbers in this manuscript attributed to the project are transcriptions or derived comparisons from those reports, **not independently remeasured in the present document-generation step**.

---

*Prepared as a private review draft. Public release, scientific authorship, novelty claims and submission venue are undecided.*