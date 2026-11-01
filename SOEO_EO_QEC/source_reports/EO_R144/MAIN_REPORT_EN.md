# R144 — Instrument-equivalent native EO parity compilation and realistic-readout sensitivity

**Date:** 29 October 2026. **Status:** exact encoded instrument construction (NUM-CERTIFIED), first-order sensitivity analysis, 3,000 paired full-nine-spin stochastic runs for single-, two-, and three-round instruments (MODEL-ONLY), and a restricted one-pulse obstruction (PROVED). **No per-bond first-order cancellation or demonstrated complete QEC-code logical improvement.**

## Executive finding

The R143 47P/25D native 3×3-grid two-data/one-ancilla EO parity instrument has an underused exact **measurement-instrument equivalence manifold**. The ancillary local basis change needs only to place `|0_B>` on the equator of the shared physical CZ projector `P_B`, rather than reproduce one preselected two-pulse local unitary. Therefore many two-pulse rotations lead to the *same Kraus parity projectors* (up to scalar outcome-dependent phases), despite differing full physical static and IID gain sensitivities.

The **R144 conservative candidate** keeps **47P/25D**, reduces total exchange area from 44 to **42**, improves minimum area from 0.1932 to **0.226**, and reduces `H_pb: 100.349204 -> 90.600186` and `H_iid: 110.429027 -> 100.379860` (9.72% and 9.10%). Its full nine-spin 3,000-shot **wrong syndrome per attempted round** decreases from **0.697015% to 0.541849%** (22.26% relative; paired absolute delta `-0.155166 ± 0.009882` percentage points, 95% CI). Leakage `0.764564% -> 0.764846%` has a paired difference `+0.000282 ± 0.000760` percentage points (95% CI crosses zero). Branch-overlap loss `2.000287% -> 1.804261%` (9.80% relative improvement). Computational-basis data-label change increases slightly, `0.390607% -> 0.392355%` (`+0.001748 ±0.000835` percentage points), and worst-case gain Gram eigenvalue increases `28.2269 -> 30.4006`; this candidate is **not** an all-metric Pareto improvement.

An **aggressive alternative** on the same manifold (still 47P/25D) yields `H_pb=86.239314`, `H_iid=99.923823`, and wrong syndrome **0.494951%** (28.99% relative reduction), but leakage rises from **0.764564% to 0.768139%**, an identified small yet statistically significant cost (`+0.003575 ± 0.000945` percentage points). It improves the leading Gram largest eigenvalue `28.2269 -> 26.3584` and sum area to 42. There is a genuine instrument-level error trade-off, not full first-order cancellation.

Both candidates preserve literal **exact** same `Z_A Z_C` parity syndrome measurement instrument on all 32 AC-data×gauge basis inputs, with branch Frobenius residual ~1e-15 and final full 512×64 code leakage <4e-15. They do not implement CCNOT, CZ, or a fully error-corrected repetition code.

## Strict setup

- 9 spins, *native* 3×3 grid with 12 bonds: `12,23,45,56,78,89,14,25,36,47,58,69`.
- Blocks A=(4,5,1), B=(3,6,2), C=(8,9,7). Exactly one bond active per pulse; all areas `0.15<=a<2`, with no adjacent repeated bond.
- Independent per-physical-bond static fractional gain `delta_b ~ N(0,0.015^2)` **held fixed across the complete multiround experiment**. Pulse IID `eta_k ~ N(0,0.0006^2)` redrawn for every physical pulse and round. No magnetic noise. Full 512×32 physical wave propagation for the initialized-ancilla instrument, full 512×64 nominal factorization and gauge/leakage verification. Seven physical bonds appear in the sequence.
- All headline finite-noise comparisons are paired with identical physical bond samples and paired *indexed* IID draws, 3,000 realizations. Different scenarios use separately seeded 3,000-draw ensembles; do not compare nonpaired digits as physical measurements.

## Exact construction

Keep R143's 22P AB and 22P BC controlled reflections of the same ancilla projector `P_B`, and write the local B preparation as chronological `X23(a), X36(b)`, followed by the two 22P entanglers and inverse `X36(2-b), X23(2-a)`. A boundary J36 merge leaves 47 positive physical pulses. The exact initialized-ancilla contract holds whenever

`<0|R_B(a,b)^dag [I-2 P_B] R_B(a,b)|0> = 0`, with `P_B = [[3,-sqrt(3)],[-sqrt(3),1]]/4` and `R_B=X36(b)X23(a)`.

This **one real scalar condition on two angles** leaves a continuous one-dimensional physical compilation manifold; the 32×32 conditional Kraus maps remain `exp(i phi_s) Pi_s ⊗ I_8` for `s=0/1`. They differ only by a scalar phase per measurement outcome, not by data action. Rebuilding the sequences requires no nonlinear full-nine-spin gate optimizer.

- R144 conservative: `a=0.226`, `b=0.3662511940447638`.
- R144 aggressive: `a=0.3200008`, `b=0.2506941462749272`.

Both are **new numerical witnesses relative to this R143 source family**, not claims of novelty over published EO parity-check techniques. The original 22P CZ sources and complete 47P chronologically ordered CSVs are retained.

## Same-target physical cost and gain coefficients

| Sequence | P / D | Total area | Min area | H_pb | H_iid | largest eig(Q) |
|---|---:|---:|---:|---:|---:|---:|
| R143 AB→BC source | 47 / 25 | 44 | 0.193212 | 100.349204 | 110.429027 | 28.226911 |
| **R144 conservative** | **47 / 25** | **42** | **0.226000** | **90.600186** | **100.379860** | 30.400635 |
| R144 lower-record-error | 47 / 25 | 42 | 0.250694 | **86.239314** | **99.923823** | **26.358387** |

The full real symmetric **7×7 Gram matrices**, eigenvalue spectra, and per-bond analytic response are in `evidence/Q_AND_SPECTRA.json`. `H_common = sum Q` is not the same as `H_pb=tr Q`; no individual static-bond error has been certified as exactly cancelled.

## Single-round finite noise (N=3,000, paired)

| Metric | R143 reference | R144 conservative | R144 aggressive |
|---|---:|---:|---:|
| Code leakage (perfect loss flag, model only) | 0.764564% | 0.764846% | 0.768139% |
| Wrong ancilla syndrome / attempt | 0.697015% | **0.541849%** | **0.494951%** |
| Data computational label change | 0.390607% | 0.392355% | 0.392194% |
| One-minus branch overlap | 2.000287% | **1.804261%** | **1.710969%** |

Confidence intervals from `evidence/R144_PARETO_MC_3000.json` and `evidence/R144_MC_3000.json`. These are **model probabilities derived from quantum propagation averaged over code/gauge inputs**, not raw frequency estimates from 3,000 physical device measurements. Statistical uncertainty is from sampled gain realizations.

## Repeated measurement: what improves and what doesn't

For R143 vs R144 conservative, static gains persist across rounds, pulse jitter is renewed; actual conditional 32×32 gauge-inclusive Kraus products are propagated. Each run uses 2×47 or 3×47 pulses, ideal ancilla projective measurement, ideal unconditional reset, and **perfect leakage detection / discard**. No injected independent logical data noise beyond physical exchange-control faults.

**Two-round equal-syndrome postselection (3,000 paired static-gain draws)**:

| Metric | R143 | R144 conservative |
|---|---:|---:|
| Accepted (equal syndrome and no leak) | 97.056075% | **97.370173%** |
| Wrong among accepted | 0.205575% | 0.206412% |
| Disagree, without loss | 1.456696% | **1.139984%** |
| Loss | 1.487229% | 1.489843% |

Acceptance improves by `+0.314098 ± 0.020091` percentage points (95% paired interval half-width). **The conditional wrong probability does not improve significantly**: `+0.000837 ± 0.001448` percentage points. The extra acceptance is the real two-round resource-normalized gain at fixed pulse/readout counts, not a gain in a full decoded logical error rate.

**Three-round majority outcome (3,000 paired draws)**:

| Metric | R143 | R144 conservative |
|---|---:|---:|
| Survival (no perfect leakage flag activated) | 97.773313% | 97.770959% |
| Wrong majority outcome among surviving attempts, relative to *initial* data parity | 0.705297% | 0.703179% |

Three-round majority voting with persistent coherent gain and data disturbance **does not** show a material reduction of the parity-label error. This is an important negative result, not a demonstration that three-round QEC in a properly specified code never works. A majority decoder over a *single repeated check* cannot identify arbitrary data faults or distinguish first-round data transitions from measurement flips.

## Readout-assignment stress test (not HRL-fitted)

Assume symmetric independent classical outcome flip probability `r` *after* each ideal B measurement, with perfect unconditional reset and a separate, perfect leakage flag. This is an analytically applied classical confusion matrix on the physically propagated branch probabilities; it does not pretend to be a calibrated singlet/triplet POVM.

| Assumed r | One-round wrong record: R143 | R144 conservative | Relative reduction |
|---:|---:|---:|---:|
| 0 | 0.6970% | 0.5418% | 22.3% |
| 0.2% | 0.8927% | 0.7382% | 17.3% |
| 0.5% | 1.1862% | 1.0326% | 13.0% |
| 1% | 1.6754% | 1.5234% | 9.1% |
| 2% | 2.6538% | 2.5049% | 5.6% |

For **two rounds** with an assumed `r=0.5%`, acceptance becomes **96.1049% vs 96.4127%** and wrong-conditional-on-acceptance **0.2157% vs 0.2148%** (the latter improvement is not statistically resolved). For 3 rounds with `r=0.5%`, majority wrong given survival is **0.7273% vs 0.7205%**, not a decisive QEC advantage. All readout error rates above are *sensitivity parameters*, **not published HRL values**.

**Missing hardware model:** a physical B singlet/triplet detector does not generally separate every leakage state from the logical measurement outcomes; our perfect loss flag is optimistic. Reset failure, context gain, NZ1 idling, LRU/RIL implementation, measurement latency and detector asymmetry are not included. Therefore these results cannot be converted to experimental logical failure or throughput in seconds.

## Restricted one-pulse obstruction (PROVED)

In this exact ancilla projector convention, the two physically allowed B-local bonds are `J23` and `J36`. On the logical B code:

- `P_23 = I - P_B`: its pulse commutes with `Z'_B=I-2P_B`, so it cannot change `<Z'_B>` from the input `|0_B>` value `-1/2`.
- `P_36 = |0_B><0_B|`: its pulse only adds a phase to the input `|0_B>` and likewise cannot change `<Z'_B>` from `-1/2`.

Hence **neither legal single-bond B-local pulse can create the equatorial ancilla state required for this two-22P parity construction**. A mathematical J26 exchange could achieve this in one pulse, but bond 26 is **not** in the 3×3 native grid. This is a scoped minimality result for the isolated local preparation step only, **not** a 47-pulse global parity-instrument lower bound.

## Source comparison / novelty boundary

The HRL Quantum Team, *A digitally controlled silicon quantum processing unit*, Nature 655, 1154–1159 (2026), https://doi.org/10.1038/s41586-026-10754-7, demonstrates real repeated EO syndrome extraction in [3,1,3], [5,1,5], and [[4,2,2]] experiments, with NZ1 idling and 21/24-pulse RIL/LRU elements and nonideal measurement. In its [5,1,5] configuration, 200 rounds use 335,422 exchange pulses, 805 measurements and 1,805 initializations; the physical setup and exact check circuits differ from this small idealized grid. Our single-parity-check result is **not** an original implementation of error correction and must not be compared directly with HRL's reported logical failure. Also see Sun et al., PRX Quantum 5, 020356 (2024) and the earlier exchange-only DCG literature before claiming a new control principle.

## Decision

**Keep R144 conservative as the first improved native-grid parity-check candidate and R144 aggressive as an error-record-minimizing alternate.** This is a measurable *instrument-level* optimization at unchanged 47P/25D that could matter when calibration or detector overhead dominates. The true next step is to incorporate physically specified nonunitary singlet/triplet measurement and leakage-reduction operations, then test a genuine 3-data-plus-ancilla code with a decoder and injected data faults. The present three-round majority result specifically warns against mistaking syndrome-record improvements for decoded logical improvement.