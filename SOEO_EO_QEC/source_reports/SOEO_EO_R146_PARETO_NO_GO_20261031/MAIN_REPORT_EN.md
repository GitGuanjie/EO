# R146: Fixed-family first-order obstruction and exact 13P SOEO–EO detector manifold

**Date:** October 31, 2026. **Scope:** strict one-bond-at-a-time positive Heisenberg-exchange 3×3-grid, four-spin SOEO data, three-spin EO ancilla with singlet-triplet readout. This is a computational design study and not an experimental result, an error-corrected code cycle, or a proven publication-priority claim.

## 1. Reproduced source primitive

The inherited native 13P detector uses 4 radial 3×3 grid bonds (J45, J25, J56, J58) plus a route J89, with chronological route SWAP / 11 radial exchange pulses / inverse route SWAP. Under ideal control, data S_D=0 plus an ancillary singlet undergoes identity up to a scalar phase; other S_D sectors may be reported as triplet. Four Klein-four assignments of radial bonds act identically on the two-dimensional SOEO singlet code and form the four F_i variants. Four positive-area inverse words I_i complete the 8-primitive pool. This study independently reproduced nominal code action, S=1 detection spectrum and persistent-gain tangent coefficient.

## 2. Exhaustive first-order search: no zero within old eight-primitive class

For the accepted (ancilla-singlet) logical Kraus map K_i(δ) of each fixed 13P module i, expand at independent physical-bond persistent errors δ_b=0. At ideal δ=0, K_i=e^{iφ_i} I, so the *normalized traceless* derivative of a product equals the sum of module derivatives, independent of scheduling order. Represent each derivative as a real vector of coefficients of Pauli X_L, Y_L, Z_L, for each of the 5 physical bonds; discard the scalar complex phase/acceptance derivative when evaluating projective conditional logical fidelity. Its squared norm multiplied by 2/3 is the leading coefficient H of average six-state pure-state conditional infidelity.

Exhaustive multisets of four 13P primitives (330 choices) produced:

| Inverse primitives among four | Best H (fixed total 52P) |
|---:|---:|
| 0 | **0.9692787848** (each F0, F1, F2, F3 once) |
| 1 | 4.1357931765 |
| 2 | 1.5703903525 |
| 3 | 5.3620379856 |
| 4 | 3.4217684032 |

Thus the original K4 F4 is optimal *for leading accepted-logical persistent-gain harm within this particular fixed eight-word pool*. This is NOT a global optimality bound for arbitrary 52P exchange sequences. Reordering the same four patterns leaves H unchanged to first order but changes the worst-case accumulated detection probability for an S_D=1 data fault from 87.08% to 95.28%; the original F0,F1,F2,F3 ordering is among best detection orderings.

A second check relaxes primitive counts to nonnegative real weights w_i, with Σ_i w_i=1. Convex quadratic minimization gives an optimal orbit-balanced weight, with w_F=0.163195 each and w_I=0.086805 each, or forward:inverse ratio ≈1.880018:1. Nevertheless the minimal per-round normalized harm is **0.0001015321446 > 0**. A separating-hyperplane numerical witness has squared norm ≈0.00015229822, with inner product against all eight primitive derivative vectors ≥0.00015229759; the exact-zero LP reports infeasibility. The closest origin distance is ≈0.01234091637 in the adopted tangent-vector norm. Consequently, repeated combinations of these eight *fixed-angle* primitives cannot attain exact first-order accepted-logical gain cancellation, no matter how long the schedule, within the same persistent-gain model and projective-error definition. This is a finite-dimensional numerical certificate for a restricted class, not a theorem about all SOEO/EO circuits or the whole 7-spin physical map.

At 8 rounds, the lowest H among 6,435 multisets is 0.7558807155 (F0..F3 once and I0..I3 once), versus 3.8771151391 for F0..F3 twice. At 12 rounds, the lowest H among 50,388 multisets is 0.02855059734 (two of each forward and one of each inverse), reproducing R145. Long 12-round variants remain expensive (156 physical pulses and 12 readouts/resets).

## 3. New exact one-dimensional 11P core manifold

Instead of reordering existing words, vary the 11 central radial exchange areas. For the six participating spins, let B be the two-column isometry representing S_D=0 data ⊗ singlet_ab in the total-spin-zero 5D multiplicity sector. Set U(a)=X_{i11,a}(a11)...X_{i1,a}(a1). Enforce

    U(a) B = e^{iφ(a)} B .

The Jacobian of the code-preservation residual at the original exact point has singular-value rank 10 out of 11, hence a one-dimensional local exact solution manifold. Numerical continuation along its null direction, reprojected onto the exact code-preserving constraint, yields new 11P words with residual ~1e-15 to 1e-14. The four K4 pulse reassignment variants for any such word are still nominally exact because the Klein-four group acts trivially on the SOEO logical singlet sector.

The parameter `t` below is the signed displacement along a *normalized local tangent* to the existing 11P area vector, not physical time, a pulse angle or a unique global coordinate. All pulses remain positive and <2. The route remains two J89 full SWAPs, so each candidate is still strict serial 13P in the same grid.

| t | H, 4-cycle K4 | Best guaranteed 4-cycle S_D=1 detection | Sum areas per 13P |
|---:|---:|---:|---:|
| 0 (source) | 0.969279 | 95.2817% | 11.9165 |
| 0.08 | 0.827620 | **95.4383%** | 12.1023 |
| 0.12 | 0.791431 | 95.3342% | 12.1902 |
| 0.16 | 0.770600 | 95.1037% | 12.2744 |
| 0.26 | **0.755549** | 93.8734% | 12.4660 |

The t=0.26 point reduces leading accepted-logical persistent-gain harm by 22.05% relative to the original. But it also weakens worst-case fault detection and increases pulse area. The t=0.08 option reduces H by 14.61% while slightly improving the ideal worst-case S_D=1 detection. The t=0.12 option is a compromise (18.35% H reduction, similar fault detection). The precise complete 13P physical CSVs for all four Klein-four variants at t=0.08,0.12,0.26 are in `sequences/`. No additional physical single-spin drive or simultaneous exchange is introduced.

## 4. Multi-round model with static per-bond and IID pulse noise

For a paired 3,000-static-draw Monte Carlo, δ_b~N(0,0.015²) is held fixed across four cycles and η_{r,k}~N(0,0.0006²) is resampled every physical pulse. Four successive F0,F1,F2,F3 detectors each receive a fresh ideal singlet ancilla, ideal ST measurement, and ideal reset. Results averaged over six logical Pauli eigenstate inputs; conditional logical infidelity is the mean normalized pure-state output error among trajectories with every cycle accepted, not a decoded QEC error.

| Detector seed | All-four-singlet acceptance | Mean conditional logical infidelity | Paired improvement over source |
|---|---:|---:|---:|
| Original t=0 | 97.4132% | 0.027260% | — |
| t=0.12 | 96.9962% | **0.024265%** | 0.002995 ±0.000265 percentage points (95% half-width) |
| t=0.26 | 96.4587% | 0.024736% | 0.002523 ±0.000386 percentage points (95% half-width) |

The derived manifold therefore improves *conditional* coherent logical error, but sacrifices acceptance/throughput. At 1.5% gain noise, the leading coefficient H is not the whole finite-noise objective, and the t≈0.26 leading-H minimizer is not the best finite-noise candidate. In a separate paired 1,100-draw scan t≈0.12–0.16 gave the lowest conditional infidelity; sampling uncertainty and trial-seed selection limit this conclusion. Every nonzero t in the scanned positive branch reduced acceptance relative to the source at the tested σ. The total exchange area also increases, and IID effects plus more time/idle can further affect practical value. We do NOT claim a full physical QEC or Pareto-dominating improvement.

The conditional gain coefficient does not include physical false-triplet response or readout assignment errors. Actual worst-case detector performance needs explicit POVM, false positives, flag and reset modeled jointly. A major limitation of this native local spin-sector detector remains that it has finite probability to miss a genuine single-spin fault in a fixed number of rounds, leaving an O(p) unheralded component.

## 5. Independent physical verification and evidence limits

`code/verify_r146.py` independently reconstructs both SU(2)-reduced sector Kraus operators and full 128D seven-spin Pauli/swap propagation for all four K4 variants of t=0.08,0.12,0.26, and checks the 4-round first-order coefficient. All checked nominal code residuals are <1e-11 (actual observed values ~1e-15); corresponding verification stdout is in evidence.

The numerical no-go uses the fixed baseline derivative vectors as computed by central differences at 1e-6, and a numerically infeasible LP. A fully rigorous mathematical impossibility theorem would require exact algebraic derivative expressions and validated bounds on numerical error. It does not apply to non-identical pulse angles, as the manifold exploration directly illustrates.

## 6. Next recommendation

Do not continue random rearrangements of the eight old primitive sequences. Focus on (i) constrained optimization *along and beyond* the nominal identity manifold to reduce `H_accepted` **and** physical false-alarm tangent, at fixed min guaranteed physical-fault detection, (ii) accept-rate-aware realistic readout/idle/reset and erasure-assisted higher-code QEC simulations, and (iii) actual integration of the native 13P local detector with verified gauge-independent EO high-level parity extraction. The global 11-/19-spin physical layout, syndrome hook-error certification, error-decoder outputs, and total hardware-time-normalized metric remain unverified.

### Literature boundary

Full-permutation dynamical decoupling of EO qubits has been demonstrated by Sun et al., PRX Quantum 5, 020356 (2024). Exchange-only qubit stabilized by a single-spin qubit (Heinz et al., arXiv:2608.14214v1, 2026) uses a hybrid LD controlled single-spin scheme for low-level SOEO XXXX/ZZZZ detection. This R146 restricted measurement-instrument manifold and finite-family obstruction should not be claimed novel without a full literature review.