# R145 — Zero-extra-pulse Klein-four symmetrization and forward/inverse coherent-gain echoes for native SOEO–EO syndrome extraction

**Date:** 31 October 2026. **Research status:** NUMERICALLY CERTIFIED nominal exchange-only operations and physical seven-spin maps; MODEL-ONLY multi-round correlated-gain improvement. Not a hardware experiment, complete QEC code, or exact first-order cancellation. Input baseline: `SOEO_EO_GRID_NATIVE_QED_20261030`, 13P nearest-neighbor 3×3 SOEO-spin-0 detector.

## 1. Executive results

The original 13P strict-one-bond serial SOEO-EO detector works on four-spin `S_D=0` data plus an EO ancilla (singlet pair and inactive gauge). It uses 2 identical route SWAPs on grid J89 and an 11P central star around J45,J25,J56,J58, followed by the physical singlet/triplet readout on J58. The original word is numerically exact on the logical SOEO code and two EO ancilla gauge states with residual ~2.3e-15.

**New result 1: no-extra-pulse symmetry-family construction.** The four double-transpositions of the Klein four group `V4={e,(12)(34),(13)(24),(14)(23)}` act trivially on the two-dimensional `S_D=0` singlet code (the [2,2] representation of S4). Consequently, relabeling which of the four *existing* central-ancilla bonds receives each pulse gives **four physical 13P detectors** with the same exact ideal code action and no additional gates or routing. We independently checked all four and their positive-exchange inverse pulse words in the full 128-dimensional seven-spin Hilbert space, residuals `<2.4e-15`.

**New result 2: more uniform physical fault detection.** For a *single* physical Pauli error on any of four SOEO data spins, randomizing uniformly over these four 13P variants increases the worst-case (over site, X/Y/Z axis, and arbitrary encoded logical state) **expected** triplet detection rate from 30.8625% for one fixed pattern to **41.6976%**. Average detection stays 54.8031%. This is an expectation over the randomized choice of pulse pattern, not a per-shot deterministic promise. Within the four-pattern class, uniform probabilities maximize the worst-case one-shot detection by symmetry and concavity of the minimum eigenvalue. No single-spin rotations, shuttling, simultaneous exchange, or physical insertion of a double-SWAP is needed: the double-transpositions justify relabeling *which of the four existing radial bonds is addressed*.

**New result 3: deterministic four-pattern cycling reduces undetected coherent errors in repeated tests.** Each cycle includes a fresh singlet ancilla preparation, one of the 13P words, singlet/triplet readout, and ideal reset if another cycle is attempted. On 3x3 physical bonds, the same independently sampled Gaussian 1.5% static gain on each physical bond is held fixed for *all* cycles, with fresh 0.06% Gaussian IID pulse gain. The model conditions on all-singlet outcomes. The following quantities are *not* high-level decoded error rates:

| Schedule | Physical exchange pulses | Accepted probability | Mean conditional SOEO-state infidelity among accepted attempts |
|--|--:|--:|--:|
| Original fixed 13P ×4 | 52 | 97.43% | **1.298%** |
| Four different V4 pattern 13P ×4 | 52 | 97.46% | **0.02768%** |
| Original fixed 13P ×12 | 156 | 92.63% | **10.175%** |
| Three cycles of four V4 13P patterns | 156 | 92.69% | **0.24361%** |
| V4 patterns, 8 forward plus 4 inverse | 156 | 91.63% | **0.04186%** |

Reproduced by the portable `code/simulate.py`, 1000 independently sampled static vectors, seed 10012027, `sigma_static=.015`, `sigma_iid=.0006`. Different seeds and ensembles yield somewhat different means; independent paired 1000-shot runs produce four-round 1.247% vs 0.0297%, and 12-round 9.71% vs 0.261% vs 0.0457% respectively. Both ensembles support the mechanism, but percentages are Monte Carlo estimates under idealized readout and no idle noise. The 12-round mixed inverse schedule requires ~6.06% greater integrated exchange area (151.666π versus 142.998π, in the pulse-area convention) even though pulse **count** is the same.

**New result 4: coherent-error tangent rank collapses with V4 cycling.** For the initialized-ancilla accepted SOEO logical instrument of the entire 12-cycle sequence, differentiate with respect to the five physical-bond gain offsets held constant throughout all 12 cycles, project out an irrelevant state phase, and average over the six Pauli logical input eigenstates. The resulting 5×5 first-order accepted logical Gram matrix has traces:

| Twelve-round sequence | Leading conditional logical gain `tr Q` | Nonzero eigenvalues of Q |
|--|--:|--|
| One fixed 13P word ×12 | 536.28184 | 497.84331, 38.41820, 0.02032 |
| V4-balanced, 12 forward | 8.72351 | 8.72351 |
| V4-balanced, 8 forward + 4 inverse | **0.02855** | 0.02855 |

Numerical zero eigenvalues are ~1e-13. This is strong *projected error suppression after a sequence of accepted outcomes*, NOT cancellation of all gain tangents of the physical 7-spin unitary and not `O(sigma^4)` for the whole noisy instrument. In particular the mixed pattern retains a small but nonzero first-order accepted logical derivative. At the relatively large 1.5% sigma, higher-order terms dominate its ~0.04–0.05% finite-noise infidelity; multiplying Q by sigma² markedly underestimates the actual finite-noise score.

## 2. Exact symmetry derivation

The singlet code of four spin-1/2 particles realizes the two-dimensional `[2,2]` representation of the permutation group `S4`. Its kernel contains all even double-transpositions:

`G = { identity, (12)(34), (13)(24), (14)(23) }`.

For each `g in G`, `P_code W_g P_code=P_code` and `W_g P_code=P_code`. Let `U` be the original 11P central detector, which obeys `U |psi_SOEO,S_ab> = e^{i phi}|psi_SOEO,S_ab>` on the entire 2D SOEO code. Its group-conjugate `U_g=W_g U W_g^dag` acts on the same code identically. The physical conjugating `W_g` gates do not need to be run: for a radial exchange pulse `X_{ia}(alpha)`, `W_g X_{ia}(alpha) W_g^dag = X_{g(i),a}(alpha)`. Thus construct `U_g` by reassigning each original radial pulse to the permuted physical bond, without changing pulse count, pulse areas or 3x3 grid layout. The two J89 routing SWAPs remain unchanged.

The same construction holds for the exact inverse `U_g^dag`: reverse the 11 internal pulses and replace each exchange area `alpha` by its positive equivalent `2-alpha`, while keeping the two J89 route SWAP pulses. Both forward and inverse candidates remain strict serial and positive exchange with 13 pulses.

## 3. Detection proof and quantitative results

Fix data total spin `S_D=1` and the freshly prepared singlet ancillary pair. Its multiplicity space is 3D in the 6-spin total-spin-1 sector. For each detector `g` let `K_g` denote its ancilla-singlet Kraus operator on that multiplicity space. The single-shot detection effect is `E_g=I-K_g^dag K_g`. For the original detector:

`eig(E_original)=[0.30862492, 0.38170437, 0.95376291]`.

For the uniformly randomized family:

`eig((E_0+E_1+E_2+E_3)/4)=[0.41697628,0.41697628,0.81013964]`.

Thus the minimum detection expectation increases from 0.30862492 to 0.41697628. The `S_D=2` detector remains at 0.82108214 per shot. Independent full seven-spin Pauli-fault calculations agree for all twelve physical fault classes (4 sites × X/Y/Z) and both EO ancilla gauges. The mean remains 0.54803073.

For a known sequence of accepted measurements the actual Kraus matrices must be multiplied, not their single-shot probabilities. With four successive forward patterns `g=0,1,2,3`, the worst-case `S_D=1` detection increases from 0.77151647 for four repetitions of the same detector to **0.95281665** for the balanced four. For twelve repeats, the minimum `S_D=1` cumulative detection increases from **0.98807208** for fixed to **0.99997456** for V4-balanced forward. Mixed 8F/4I yields **0.99991615** in the ideal zero-gain-noise scenario. These ideal probabilities assume no additional faults arise during subsequent detection cycles.

## 4. Static-gain cancellation mechanism; precise limit

Write the small-δ accepted SOEO Kraus operator in a logical Pauli basis (ignoring scalar gain-dependent phase) as

`K_g^F(δ) ~ e^{iφF} [ I + i Σ_b δ_b v^F_{g^{-1}(b)} · σ + O(δ²)]`,

and likewise for the positive-area inverse pattern `I`. Over a complete four-element V4 cycle, every physical radial bond is sampled in all four symmetry-equivalent roles. Hence the first-order *traceless* logical generator is identical for all four physical radial-bond gain directions: residual response is proportional to their **sum**. Physical route bond J89 has no first-order accepted logical response (though it still causes false alarm/leakage). Thus Q on accepted logical outputs becomes rank one.

For one pattern averaged over the four variants, the central-bond traceless logical derivative vectors (numerical Pauli-coordinate convention) are approximately

`v_F = (-0.004385, +0.055605, +0.140023)`

`v_I = (+0.019728, -0.091580, -0.267248)`.

Their signs are almost opposed, but not perfectly so. With 8F/4I cycles, the relevant coefficient becomes `2 v_F + v_I ≈ (0.010958,0.019629,0.012798)`, far smaller than `3 v_F`. The corresponding 12-round Q trace falls to 0.02855. The cancellation is **partial**. For different exact 11P angle families one could seek full cancellation, but this is not established here. A small 1D constrained manifold search in the baseline 11P word did not find a valid exact gain-zero point; this is not a no-go theorem.

## 5. Correlation-stress results, important negative finding

For static-gain correlation fraction rho between rounds, model `δ_b(r)=sqrt(rho) δ_b^(persistent)+sqrt(1-rho) ξ_b(r)` with both components carrying the same marginal 1.5% standard deviation. IID pulse gain is separately 0.06%. Across 350 samples per rho, for 12 rounds:

| rho | Fixed F12 conditional error | V4 F12 | V4 F8I4 |
|--:|--:|--:|--:|
| 0 (fully renewed gain per round) | 0.859% | 1.015% | 1.001% |
| 0.5 | 5.234% | 0.576% | 0.471% |
| 0.9 | 10.053% | 0.329% | 0.141% |
| 1.0 (fully persistent) | 10.921% | 0.250% | 0.0409% |

The symmetry cycling is highly valuable specifically for *persistent correlated gains*—the current project’s main physical error model. At rho=0 it is not helpful; it can be worse than repeatedly using one fixed word. Thus the temporal noise spectrum/correlation time must be measured or calibrated before recommending this protocol experimentally.

## 6. Important practical caveats

1. The raw QEC benefit is conditional on ideal singlet/triplet assignment, lossless ancillary initialization/reset, and detected branches discarded. These are **heralded error-detection experiments**, not decoded high-level QEC logical error per cycle.
2. Extra detection rounds cost extra readouts, resets and pulse time. At 12 rounds the 8F/4I option gives ~91.6% acceptance, i.e. roughly 8.4% discarded/flagged trajectories *even on correct nominal SOEO input* subjected only to gain noise. Readout assignment errors will compound.
3. No nuclear-spin/Overhauser noise, pulse-dependent context noise, actual HRL NZ1 idle, leakage-reduction action or data recovery was included. Exchange-only SU(2) symmetry protects singlet-accepted data *against spin-sector leakage* but not logical X/Z overrotation.
4. The physical 3x3 grid has 7 occupied sites; preparing two initial SOEO singlet pairs on nonadjacent data locations, measuring and resetting the ancillary pair, and embedding a large high-level EO QEC lattice require additional layout work.
5. A detector of local `S_D=0` is not a high-level encoded `XXXX/ZZZZ` stabilizer readout. Lifting R143/R144 gauge-independent encoded parity words to SOEO is a separate potential workstream that still requires the original source CSV and physical 11-spin verification.
6. The original 13P has `H_pb=33.5447` for **one physical cycle**, of which `H_flag=29.8206` and `H_accepted=3.7242`; neither the V4 variants nor their inverse is a perfect first-order-cancelled *physical* detector. Our 12-round Q is a different quantity, measuring **accepted logical error accumulation** for persistent physical-gain perturbations.
7. Pulse counts for 4/12 repeated detectors do not include singlet-state preparation, S/T measurement, reset and their duration or error rates. Full QEC resource comparison must include them, and should compare against *no local detector*, standard EO LRU/RIL, and direct high-level parity readout under identical time budgets.
8. Literature novelty is not established. HRL’s full-permutation exchange-only dynamical decoupling was experimentally demonstrated in Sun et al., *PRX Quantum* 5, 020356 (2024); this construction targets SOEO spin-sector measurement Kraus operators and persistent-gain measurement errors, but a proper overlap and priority audit is required.

## 7. Reproducibility and next decision

`sequences/` contains all 8 physically mapped chronological 13P words (F0..3 and I0..3) plus a 12-round readout/reset schedule. `code/sector_rep.py` constructs the 20D Mz=0 six-spin basis and the total S=0,1,2 blocks. `code/native_variants.py` implements exactly the physical 5-bond per-physical-bond correlated gain model and physical routing to the auxiliary singlet. `code/reproduce.py` recomputes exact ideal instruments, detection spectra, and projected Gram matrices; `code/full_spin_independent.py` independently verifies all eight words in full 128D physics using Pauli spin matrices; `code/simulate.py` reruns 4/12-round static+IID Monte Carlo with configurable correlation rho. `evidence/` holds executed output captures and copies of independent exploratory paired/correlation results.

**Research decision:** Keep the zero-overhead V4 four-round protocol as the near-term experimental candidate. Keep the 8F/4I 12-round pattern as a mechanism proof of partially cancelling persistent *accepted logical* exchange-gain error, not as an immediately practical QEC design. Next do full measurement POVM + idle/readout/reset and leakage-aware high-level decoder, and search for a genuinely short block (≤4 rounds) with exact first-order accepted-logical cancellation and acceptable single-spin detection. Restrict new novelty claims until prior permutation-DD literature is audited.