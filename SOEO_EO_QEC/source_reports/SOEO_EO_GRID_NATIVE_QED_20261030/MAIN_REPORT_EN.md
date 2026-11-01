# Research advance: native-grid strict-serial SOEO singlet-sector detection using an EO ancilla
Date: 2026-10-30. Status: **numerically exact ideal instrument, verified at the full 7-spin level; model-only per-bond noise results; NOT fault-tolerant or experimentally demonstrated.**

## Executive finding
We found a genuinely strict one-bond-at-a-time **11-pulse, all-positive Heisenberg-exchange sequence** that acts as a global phase on both four-spin SOEO logical states when the auxiliary pair is initialized in a singlet, yet changes the singlet/triplet outcome statistics for input data spin-1 or spin-2 sectors. No physical single-spin H, X, Z control and **no simultaneous exchange couplings** are used. It requires a four-neighbor star during the detection phase, but **two additional full SWAPs** embed it in a static **3×3 square-grid nearest-neighbor** connectivity, giving a concrete **13P** detector with a three-spin EO ancilla (one singlet pair plus inert gauge spin). An analogous **12P** candidate exists with weaker detection contrast.

This is an improvement over the earlier four-simultaneous-coupling 4-J star proposal in **control class and geometry**, not in gain robustness: independent static per-bond gain at 1.5% produces significant O(sigma²) errors in these strict-serial words. The previous 4-J star has O(sigma⁴) in the ideal simultaneous model; **we did not preserve that cancellation**. This is not a high-level multi-EO XXXX or ZZZZ measurement; it is a native **low-level SOEO S_D=0 vs S_D>0 heralded detector**, to be coupled later with existing gauge-independent EO high-level parity instruments.

## 1. Exact physical setup and available primitives
A four-spin SOEO data block with logical code `S_D=0`, two auxiliary spins `a,b` initialized as `|singlet_ab>`, plus a third inert spin `g` so that `(a,b,g)` is a 3-spin EO ancilla in logical `|0>` (singlet pair plus arbitrary gauge). All controls are strictly one bond at a time, positive pulse areas `a_k` in the convention `X_ij(a)=exp(i*pi*a*P_ij^singlet)`. Initialization of the EO ancilla and physical singlet-triplet readout are extra resources, not counted as exchange pulses. None of the pulse words below are an isolated logical EO–EO entangler; the ancillary EO logical measurement is consumed by S/T readout.

### 3x3 grid coordinates (row, col), row-major site labels
1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), **5:(1,1)**, 6:(1,2), 7:(2,0), **8:(2,1)**, 9:(2,2).

- Before operation: data SOEO site states `(4,2,6,9)`; auxiliary EO `(5,8,7)` with singlet on `(5,8)` and gauge spectator `7`.
- Exchange sites `(8,9)` by full `SWAP` area `1`: data state D4 moves from site9 to site8; ancilla-b singlet partner moves from site8 to site9. This is an actual **spin-state SWAP**, not literal dot translation.
- Execute all 11 serial exchange pulses from site5 to the four data states at sites `(4,2,6,8)`; physically used four bonds are (4,5), (2,5), (5,6), (5,8).
- Full `SWAP(8,9)` again restores data D4 to site9 and the ancilla singlet partner to site8.
- Measure pair singlet/triplet on nearest-neighbor bond `(5,8)`. Gauge 7 is a spectator.

This geometry is static nearest-neighbor and contains five physical bonds. Depth = pulse count 13 when sequential; sum of positive areas is 11.9165 (in π units). A 12P alternate uses total area 10.2556.

### Exact chronological 13P word
`(8,9;1)` + these central a=site5 steps:

| Step (inside star) | Bond | Area a |
|---|---|---:|
|1|45|0.5192386333595181|
|2|56|1.5839512377735476|
|3|58|1.3682386550761760|
|4|56|1.5839512377735474|
|5|25|1.3905039171274718|
|6|45|1.4579153626294534|
|7|25|0.1730184425355885|
|8|56|0.3682386550761670|
|9|58|0.5839512377735380|
|10|56|0.3682386550761673|
|11|25|0.5192386333595033|

then `(8,9;1)`. Use `sequences/GRID_13P_SOEO_SPIN0_DETECTOR.csv` for authoritative full exact numeric values. **Angles are numerically optimized to ~1e-15 residual and are not a closed-form proof of pulse values.** No claim of global pulse-count minimality.

**Scope of geometry verification:** The 13P CSV is a valid *detection-core* routing on the 3×3 graph; preparing two SOEO singlet pairs on the selected four data sites may require extra shuttling or routing, because only one of the needed data-pair connections is directly adjacent. The ancillary singlet preparation, physical S/T readout, reset, and re-embedding into a multi-block QEC processor are not included in the 13P resource count.

## 2. Representation theory and independent physical verification
A six-spin system decomposes into total-spin sectors `S_all=0,1,2,3`, with spin-multiplicity dimensions `5,9,5,1`. Since exchange preserves total spin and its z-component, all searches may run in the 20-dimensional `S_z=0` computational subspace, separately projected onto `5,9,5` sectors. The data-SOEO code plus pair singlet occupies a 2D subspace of `S_all=0`. On this code×ancilla subspace the optimized 11P central unitary satisfies

`U_11 ( |psi_SOEO> |singlet_ab> ) = exp(i phi) |psi_SOEO> |singlet_ab>`

for both SOEO logical states and arbitrary superpositions, with `phi=arg(0.341573658792486 - 0.939855007764024i)`. Independent full 128D (7-spin) spin-permutation propagation of the 13P routed circuit, with both gauge states, shows norm residual `2.19e-15`, ideal false-flag probability `<1e-29`. Code-phase identity in the fixed-gauge 5D rep is separately checked. All five physical exchange bonds are valid nearest-neighbor edges in the chosen 3x3 grid.

**For the input data spin sectors** `S_D=1` and `S_D=2`, the single-round ancilla-singlet return depends on multiplicity and logical state. Averaged uniformly over spin multiplicities, the 11P central word gives `S=1` singlet return `0.4519692671` (triplet detection `0.5480307329`), `S=2` return `0.1789178648` (triplet detection `0.8210821352`). The 12P alternate gives `S=1` detection `0.2871470`, `S=2` detection `0.6318440`.

For single physical X/Y/Z faults on any data site, **averaged over the two SOEO logical states and two auxiliary gauge states**, the 13P detection probabilities are by physical data site `[4,2,6,9]` = `[0.509477,0.514350,0.584148,0.584148]`. All X/Y/Z axes give identical values due to SU(2) invariance. For an arbitrary logical superposition the min/max detection eigenspectra vary: worst over tested single-site Pauli errors is `0.308625`, best `0.795055`. Do NOT call 50–58% a state-independent guaranteed rate; the guaranteed single-fault minimum is at most the above 30.86% for this class of inputs.

### Repeated *ideal* detection: no protected dark sector
The singlet-acceptance Kraus operator `K_S` in the three-dimensional spin-1 multiplicity space has singular values `[0.83148968,0.78631777,0.21502810]` and eigenvalue magnitudes `[0.83148968,0.78623219,0.21505151]`. All are strictly below 1. In the one-dimensional spin-2 multiplicity, `|K_2|=0.42298684`. Thus repeated ideal (noise-free, freshly reset ancillary singlet) tests exponentially eliminate every S>0 component, though the rate depends on initial state. Average detection on the uniformly mixed S=1 multiplicity subspace improves from `54.803%` after one round to `91.725%` after five and `98.897%` after ten; S=2 reaches `99.982%` after five. This is **not** the old 4-J star formula `(1/9)^n`: the strict-serial K_S is generally non-scalar on the spin-1 multiplicity space.

### An exact symmetry statement survives *all orders* of isotropic exchange-gain noise
Total six-spin SU(2) angular momentum is conserved by any pulse sequence made only of isotropic Heisenberg exchange, even with arbitrary pulse-area gain errors. Initially correct SOEO S_D=0 + ancillary singlet S_ab=0 implies total S_all=0. If the final ancillary pair is measured as singlet (S_ab=0), the surviving data must have S_D=0. Hence **accepted trajectories cannot leak outside the SOEO S=0 sector** under this ideal isotropic exchange-and-perfect-ST-readout model. Accepted logical X/Z rotations are still possible and significant. This does not cover local magnetic noise, spin-orbit anisotropy, incorrect ST assignment or destructive leakage during data reset.

## 3. Static per-bond gain noise: negative but quantified
Apply one Gaussian static fractional offset per physical bond, independent between five bonds, drawn once and held over the full 13P attempt: `delta_b~Normal(0,sigma²)`. For 12 states (six SOEO logical Pauli eigenstates × two EO gauge states), full 128D unitary propagation, 1,200 draws per sigma, perfect S/T detector:

| sigma | word | Triplet false-alarm (correct SOEO input) | Accepted conditional state error | Full-state error |
|---|---|---:|---:|---:|
| 0.003 | 13P | 0.02692% | 0.00332% | 0.03023% |
| 0.015 | 13P | 0.67194% | 0.08446% | 0.75544% |
| 0.003 | 12P | 0.01293% | 0.00389% | 0.01682% |
| 0.015 | 12P | 0.31773% | 0.09930% | 0.41655% |

These are model estimates with finite Monte Carlo variability; they are not HRL experimental rates. IID per pulse, idle/nuclear noise, calibration drift within pulse, context effects, SPAM and physical reset are NOT included. QEC performance requires measuring actual decoded logical error, not just low-level acceptance or false alarm.

For the physical 13P word, finite-difference first-order per-bond gain derivatives produce 5x5 real Gram Q, with physical bond order `J45,J25,J56,J58,J89`. `tr Q = 33.54473845`, `sum(Q)=15.66511718`, and eigenvalues `[1.627986,2.516192,6.806138,7.086760,15.507662]`; thus **no first-order per-bond gain direction is cancelled** by this word. For the portion causing false triplet reports `tr Q_flag = 29.82055800`; the remaining accepted logical error quadratic coefficient is ~`3.72418045`. Under sigma=.015, the leading full infidelity predicted by `sigma² tr Q` is 0.7548%, agreeing with MC 0.7554%. In particular **this is not the sigma^4 revival mechanism** from the 4J simultaneous star.

The two routing swaps add one persistent-noise bond J89; they raise full error relative to the bare 11P scheme. Nevertheless they solve the static 3x3 nearest-neighbor connectivity problem, under ideal exchange-only ST prep/readout.

## 4. Why this is not yet QEC, and next step
- With a single physical data-spin Pauli error, detection probability is strictly less than one; hence postselected harmful error still has an O(p) contribution at fixed finite number of rounds. This is NOT a fault-tolerant QED gadget in the strict single-fault-detectability sense.
- With sigma_pb=1.5% held over many test rounds, accepted logical errors accumulate coherently. 11P un-routed single-round conditional error ~0.08%; at 10 repeated noise-affected accepts the model can reach ~7% conditional error (independent 800-draw test). Repeating this long noisy detector blindly is counterproductive.
- 13P detector is intended only for *local SOEO total-spin-sector* checks; it is not the high-level `X_A X_B X_C X_D` or `Z_A Z_B Z_C Z_D` parity instrument. A high-level gauge-independent R143/R144 47P EO parity word could in principle be lifted onto SOEO data spectator-encoded triples, but the original 47P chronological physical CSV was NOT present for a full 11-spin rerun in this turn. The 3x3 physical layout here is different from the earlier R144 layout; integrating the two requires new routing design.
- The best next optimization is to search in the **same 5x5,9x9,5x5 representation sectors**, with simultaneous hard constraints: nominal exact `U P_code = exp(i phi) P_code`, required minimum detection for all single-spin Pauli faults, `K_S` spectral radius less than one, and **minimize** leading first-order static error Gram `tr Q` and accepted-branch Gram. Optimize real routed geometry and 1-J pulse budget. Then add pulse IID, physical non-projective singlet/triplet readout, singlet reset time and HRL-inspired idling.

### Related existing work, novelty boundary
- Heinz, Sharma & Kattemölle, arXiv:2608.14214v1: hybrid SOEO + LD physical `XXXX/ZZZZ` with true single-spin control in LD zone, not a strict 1-J SOEO spin-sector detector.
- HRL, *A digitally controlled silicon quantum processing unit*, Nature 655, 1154–1159 (2026): implemented EO repetition codes and LRU with physical SPAM; readout leakage ambiguity is a key caveat.
- HRL/Petta group, *Demonstration of an always-on exchange-only spin qubit*, Nature Communications 17, 4794 (2026), and *Leakage-Protected Idle Operation of a Triangular Exchange-Only Spin Qubit*, PRX Quantum 7, 020324 (2026): realistic 2-J controls and leakage protected idle, but not a demonstration of this 13P scheme.
- No literature priority claim has been established for the exact 11P/13P numerical word; do a targeted literature search before asserting novelty in a paper.