# R143 — Exact native-grid EO parity-extraction module and two-round noise experiment

Date: 29 October 2026. Status: **numerically certified physical unitary + exact ideal encoded measurement branches; model-only noise/measurement simulation**. This is *not* a claim of hardware QEC, first-order gain cancellation, or a published-literature novelty priority.

## Executive result

A 47-pulse, 25-layer **strict serial, positive-exchange** nine-spin circuit performs an encoded stabilizer **Z_A Z_C** parity write onto the central EO ancilla B, using a pair of physically mapped 22P linear CZ sequences and two-pulse ancilla-basis rotations. This is a nontrivial operation useful for a *small EO parity-check primitive*, unlike previously examined two-CZ identities or a toy ancilla-Rx Kraus counterexample. Every pulse lies on the 12-edge 3x3 grid. The full 512x64 spin-level physical unitary is gauge-independent and leakage-free at nominal control angles (full leakage norm <4e-15). With B initialized in |0> and then measured in the ideal encoded 0/1 basis, the **two conditional 32x32 gauge-inclusive Kraus operators** equal Pi_even and exp(i phi) Pi_odd to ~3e-15 Frobenius norm, where Pi_even/odd=(I +/- Z_A Z_C)/2 on the data.

### Key construction: a matching native ancilla axis

Use the Fong–Wandzura-derived previously archived 22P nearest-neighbor six-spin CZ circuit. Map its five active sites into the native grid as follows:

- A–B gate: original ordered six sites (1,2,3,4,5,6) -> physical (5,4,1,2,3,6). The mapped word uses grid bonds (4,5), (1,4), (1,2), (2,3). Its encoded logical operation is I - 2 |1_A><1_A| ⊗ P_B.
- B–C gate: original sites -> (2,3,6,9,8,7). The mapped word uses (2,3), (3,6), (6,9), (8,9). Its operation is I - 2 P_B ⊗ |1_C><1_C|.
- Both share exactly the same ancilla Bloch-axis projector, P_B = [[3/4,-sqrt(3)/4],[-sqrt(3)/4,1/4]]. The alternate A–B routing (1,4,5,6,3,2) instead uses |1_B><1_B|, so it **fails** to share the B axis with the B–C gate. Choosing the correct physical triple role assignment is essential.

Because the two *encoded* controlled reflections commute, their product writes parity to the common ancilla basis. A legal two-pulse B-local preparation uses, chronologically, X_23(1.8067882851772408), X_36(1.4505587284454933); its physical inverse is X_36(0.5494412715545067), X_23(0.19321171482275923). A single adjacent J36 merge reduces the 48-pulse naive implementation to **47P/25D**. All areas are between 0.1932117 and 1.8067883; see `sequences/EO_PARITY_AB_BC_47P.csv`.

### Physical sequence benchmarks

| Variant (two gate orders) | Pulses | Depth | Total area | Hpb | Hiid | max eig(Q) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| AB then BC | 47 | 25 | 44 | 100.349204 | 110.429027 | 28.226911 |
| BC then AB | 47 | 25 | 42 | 97.513192 | 100.559423 | 37.091500 |

The second order requires reducing one merged J36 angle modulo 2 after physical adjacency (the resulting **physical** single pulse is a=0.4505587), not retaining an unphysical area >2. This changes actual static gain sensitivity and is included when computing Q. The two sequences are the *same initialized-ancilla parity instrument* up to known syndrome-dependent phases, although the full logical unitary on arbitrary B inputs can differ. Neither cancels all static per-bond errors.

A second, complementary two-pulse ancilla-preparation branch with areas (0.1932117, 0.5494413) yields two more 47P parity instruments. The order/branch pairs reproduce the same two harm levels. These alternatives are included under `sequences/EO_PARITY_LOW_*.csv`. The 47P choice is not a new record against **every** published parity-check circuit; this study establishes a clean baseline for future instrument-level optimization.

## Full-code and derivative verification

`code/reconstruct_r143.py` rebuilds both native-grid subwords and the legal 47P merged sequences from the supplied FW-derived 22P source. `code/verify_r143.py` independently applies **genuine 512x512 sparse spin-permutation matrices** to all 64 encoded columns, compares with an independently programmed rectangular propagation engine, verifies the common target and both 32x32 conditional operators, and checks all 7 bond first derivatives by central differences. Analytic and finite-difference per-bond Q entries differ by <=1.1e-8; a +0.01 perturbation deliberately fails the exact-target contract. Clean extraction reproduces.

## One round — 3,000 paired full-spin Monte Carlo draws

Noise: 7 independently Gaussian *physical bond* gain errors with sigma=0.015, held fixed for the **entire 47P round**; fresh IID fractional gain sigma=0.0006 on each pulse. Identical bond draws are paired between both realizations; the same raw per-pulse IID draw index was used as a variance-matched paired-sampling coupling. Per shot, propagate all 32 initialized-ancilla data×gauge basis vectors through the full 512D physical Hilbert space. Finally project onto the ideal code and ancilla readout; leakage is treated as separately detected loss *by assumption*.

| Metric (physical model; not experimental rates) | AB then BC | BC then AB | Paired difference BC–AB, 95% half-width |
| --- | ---: | ---: | ---: |
| Code leakage / ideal detector loss | 0.77357% | 0.85282% | +0.07924 +/- 0.00615 percentage points |
| Wrong encoded ancilla report | 0.71377% | 0.70237% | -0.01140 +/- 0.01065 percentage points |
| Data computational-label change | 0.39767% | 0.39848% | +0.00081 +/- 0.00180 percentage points |
| One minus normalized branch-overlap score | 2.02158% | 2.08885% | +0.06727 +/- 0.01551 percentage points |

**Important counterexample to a wrong optimization proxy:** BC→AB has **lower Hpb and IID**, but it has significantly **higher physically computed leakage**, and it fares worse in the exact-measurement branch-overlap score. A single gate-only harmonic coefficient does *not* determine the optimal QEC instrument. Wrong-record rates are very similar; the narrow paired interval should not be overinterpreted against unknown hardware SPAM/context errors. All raw coupled shot metrics are retained.

## Two rounds — 3,000 paired persistent-gain realizations

For both rounds, the exact physical 47P word and ideal B readout/reset are repeated. For each sampled static gain vector, it is **held fixed in both rounds**; IID draws are renewed between rounds. After round one, the gauge-inclusive 32×32 Kraus state of the data is retained for each measured branch. For round two, compute K_(n,2) K_(m,1), not merely classical independent Bernoulli events. Code-space leakage is treated as detected **loss and discarded** after each round. This idealized leakage detection is *not* an implemented HRL LRU model.

| Metric | AB then BC | BC then AB |
| --- | ---: | ---: |
| Two-round accepted (equal syndromes AND no leakage) | **97.02335%** | 96.87532% |
| Wrong-but-agree unconditional | 0.19958% | 0.20038% |
| Wrong among accepted | **0.20804%** | 0.20964% |
| Disagreeing records with no leakage | 1.46421% | 1.45474% |
| Detected leakage / loss over two rounds | **1.51244%** | 1.66994% |

Paired difference BC–AB in acceptance: -0.14802 percentage points ±0.02371 (95% interval half-width). The difference in wrong-given-acceptance is +0.00160 percentage points ±0.00168, *not statistically resolved*. Compared with a single-round wrong record ~0.714%, two-round conditional wrong-agreement ~0.208% is a ~71% reduction **for this specific parity-record task with postselection**, but at **94 exchange pulses plus two measurements/resets** per attempted two-round run and ~3% rejection. That is not a measured logical QEC threshold or decoded logical failure rate. The data can be damaged or dephased despite a correct parity report.

## Connection to experimental EO QEC and limitations

HRL, *Nature* **655**, 1154 (2026), performed repetition-code and [[4,2,2]] syndrome operations with real SPAM, idling NZ1 and 21/24-pulse leakage-reduction sequences. Our device-level model is not a reproduction of HRL's layout or gates. A physical singlet/triplet readout of B alone does not distinguish all leaked states from encoded logical |1>; the **perfect leakage flag**, projective encoded measurement and reset used here are optimistic abstractions. Measurement latency, reset failure, readout assignment errors, idle exchange/magnetic noise, context-dependent calibration, correlated data faults, and physical LRU placement were not included. Do not compare these percentages to HRL's reported logical error rates. The model noise sigmas were selected from the project's prior HRL-motivated fit, not extracted or re-fitted in this round.

**What is proved or numerically certified:** same ancilla logical projector on two native legal physical subgraphs; exact ideal 47P parity instrument; exact branch correctness on all data and gauge states; noise metric conflict; full 3,000-shot per-round and two-round model calculations. **What remains open:** any physically implemented LRU/readout/reset model, a genuine lower decoded logical failure rate at fixed total hardware time, and any new first-order-cancelled individual physical gain channel.

## Supplementary exact circuit compiler check

A 43P exact CCNOT, followed by local encoded SWAP89 and the same 43P CCNOT, is a meaningful but *unnecessarily compiled* CZ_AB × local-Z_C operation. Literal 512x64 encoded outputs match up to a global phase at 7.55e-14 Frobenius norm. Direct 27P CZ_AB plus 1P local SWAP yields the same target: 87P/46D and Hpb=388.563 become 28P/17D and Hpb=39.445. This is a **standard logical Clifford conjugation identity** and is included as an audit of circuit-level simplification, **not** as a novel native CCNOT synthesis or fair published benchmark.

## Reproduce

See `README_RUN.md`. Run under `OPENBLAS_NUM_THREADS=1` to constrain RAM and avoid unnecessary thread overhead. Supporting files: `sequences/`, `code/`, `evidence/`, `runs/`. Independent verification is fast; the 3,000-shot datasets are bundled and the exact ensemble scripts may be rerun with the settings shown.