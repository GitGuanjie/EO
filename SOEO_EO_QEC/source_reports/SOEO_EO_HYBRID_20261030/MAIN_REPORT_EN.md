# Research advance: SOEO–EO hybrid control and fault-aware coupling
**Date:** 30 October 2026. **Status:** new analytical derivations plus independently executed complete-spin simulations. Not hardware experiments, nor claims of literature priority. Builds on arXiv:2608.14214v1 and the established R143/R144 EO parity-instrument contracts.

## Executive decision
**Do not replace the short, strict-serial EO compiler with a long gapped SOEO–EO perturbative gate under the existing static-per-bond model.** Instead, treat a four-spin SOEO as a three-spin EO logical subsystem whose gauge is purified by a spectator spin. Test whether the existing, independently certified six-/nine-spin gauge-independent EO–EO gate and parity instrument can be *lifted* to SOEO data blocks while keeping the extra spin completely idle. Use the new SOEO spin-0 detection only as a separate low-level leakage/erasure interface, if its four-arm simultaneous exchange can be physically provided or an exact shorter replacement is found.

### Definitions and hardware controls
- `SOEO-A = spins (1,2,3,4)` uses four physical spin-1/2 electrons and code S_A=0 (two logical dimensions).
- `EO-B = spins (5,6,7)` uses three physical spins and code S_B=1/2 (two logical dimensions times two gauge sectors).
- Positive Heisenberg exchange only. No physical single-spin X/H/Z. Singlet preparation and singlet/triplet readout as primitive measurement resources when explicitly stated.
- Distinguish **1-J strict serial** (one physical bond active per step), **2-J simultaneous**, and **multi-J always-on gap**. Results from the latter categories cannot be claimed as valid 1-J circuits.

## A. Exact encoding compatibility (PROVED; 4-spin and 7-spin tests PASS)
In a three-spin EO basis `|ell,+>` and `|ell,->` with gauge m=+/-1/2, the SOEO code can be written exactly as

```
|tilde ell>_(1234) = (|ell,+>_123 |down>_4 - |ell,->_123 |up>_4)/sqrt(2).
```

In the published SOEO logical basis defined by singlet12 singlet34 and triplet-pair singlet, the recoupled states satisfy `|tilde 0> = |0>_paper`, `|tilde 1> = -|1>_paper`. Thus the known frame transformation is Z. A three-spin exchange-only unitary that implements `U_logic tensor I_gauge` on spins123 acts on SOEO as `Z U_logic Z` in the paper frame, with the fourth spin entirely idle. A physically checked native 3-pulse `H_L` on EO lifts exactly to SOEO with the expected Z frame, nominal code leakage < 1e-15 (code/lifted_h_test.py).

**Critical two-block condition:** A known 6-spin EO–EO pulse word may be lifted to one 4-spin SOEO + one 3-spin EO by parking the SOEO fourth reference spin *only if* its physical 6-spin contract is `U_logical tensor I_(gaugeA,gaugeB)` on all logical/gauge inputs, with zero final leakage. A sequence correct only for one gauge sector, or with conditional joint-gauge phases, is not automatically liftable. A Choi/reference-system argument proves this necessity: acting on half of the maximally entangled SOEO gauge-reference singlet must leave that singlet unchanged. Gauge-independent, ideal 47P R143/R144 parity is a good candidate to lift, but its physical CSV was not available to this turn for independent 11-spin verification. Do NOT label that verification completed.

Resource accounting: an SOEO+EO gate is **7 physical spins** with 6 active and 1 spectator. Two SOEO data blocks + 1 EO ancilla are **11 physical spins**, with 9 active and 2 spectators; this is the natural lift of an existing 9-spin 47P parity instrument. Four SOEO data blocks + an EO ancilla are **19 physical spins**, with 15 active and 4 spectators.

## B. Exact single-cross-bond obstruction for gapless isolated exchange (PROVED; 128x128 check PASS)
For one exchange `U(theta) = exp(i theta P_singlet_(i,j))` between any SOEO physical spin i and EO physical spin j, use `P_A S_i P_A=0`. On the encoded SOEO×EO space,

```
P U(theta) P = [(3 + exp(i theta))/4] * P
p_escape = (3/4)*sin^2(theta/2).
```

Therefore this **single isolated physical cross pulse** cannot implement an encoded entangling unitary. Except for theta=0 modulo 2pi it causes leakage; at full 2pi return it is the identity. This is not a no-go for a composite exchange word or for interblock exchange while intra-SOEO interactions remain on. The published SAGE always-on proposal is an explicit example of the latter scenario.

## C. Explicit second-order hybrid entangler with two cross links and a spin-gap (PROVED to O(g²/Delta); 128D exact check)
Toy H0=(Delta/2) S_A^2, with gaps to S_A=1 and 2 of Delta and 3Delta. Can be represented, up to scalar, by equal all-to-all positive intra-SOEO couplings on **six physical bonds**. This is a NON-STRICT, multiple-always-on-bonds hardware class. Cross coupling:

```
V = g ( S_1.S_5 + S_2.S_6 ), g << Delta.
P V P = 0.
Heff(2) = -(g^2/Delta) [5/12 I + ZA/12 + ZB/12 + (ZA ZB)/6].
```

Derivation: V takes spin-zero data into spin-one at energy Delta. On an SOEO singlet, `P_A S_i^mu S_k^nu P_A = delta_mu,nu P_A(S_i.S_k)P_A/3`. The cross terms yield `-(2g²/(3Delta)) (P_A S1.S2 P_A)(P_B S5.S6 P_B)`, with each pair product `-I/4-Z/2`. Code/hybrid_7spin.py checks the cross term and all Pauli coefficients to ~1e-16, gauge independent.

At second order the ZZ coefficient is `-g²/(6Delta)`. An ideal maximally entangling controlled-phase equivalent takes `T ≃ 3 pi Delta/(2g²)`, after local Z corrections. At g/Delta≈0.136800829 and TDelta≈210.900173, a full 7-spin **noise-free** square-pulse simulation gives 99.7769% trace-compatible average gate fidelity after fixed local-Z frame calibration and ~99.789% code survival. This is a tuned theoretical pulse with six always-on intra-links and two simultaneous cross-links; it is not a valid isolated 1-J gate. The fidelity counts final leakage but not ramp, control, readout or idle errors.

### D. Noise stress is strongly negative for independent intra-block gain offsets
Use eight physical bonds: six intra with unit nominal J0=Delta plus two cross with g. Apply independent static Gaussian delta_b on requested bond groups, fixed for the full TDelta~211 evolution; compare once-calibrated gate to an exactly maximally entangling diagonal target. Full 7-spin Sz=+1/2 (35D) simulation suffices by SU(2) symmetry. Fixed 120 Monte Carlo realizations per configuration.

- Nominal: Favg=0.997769, code survival 0.997890.
- Only cross gains sigma=0.015: Favg≈0.9970 (small effect).
- Only six independent intra gains sigma=0.0015: Favg≈0.90.
- All eight independent gains sigma=0.015: Favg≈0.48–0.49 (MC sampling variation).
- Six intra gains perfectly common mode sigma=0.015 (cross ideal): Favg≈0.981.

The underlying reason is that asymmetry of all-to-all J0 within SOEO induces directly projected `O(sigma*J0) (hX XA + hZ ZA)`, whereas the desired entangler is O(g²/J0). Over long gate times the first-order internal error overwhelms the controlled interaction. This stress test extends the *form* of a HRL-inspired sigma=1.5% static per-physical-bond gain model to a hypothetical all-to-all SOEO processor. It is **not** an experimental noise calibration of SAGE or a direct result from HRL hardware.

## E. Synchronized logical-Y echo: partial noise cancellation, not enough
An exact numerical positive-exchange 5-pulse logical Y rotation on a 3-spin EO, and likewise SOEO through its triple, has (chronological 12,13,12,13,12) exchange areas:

```
[0.9544871677751868, 1.1098198558456085, 1.4918977454286901,
 1.5884811018233003, 0.2329176621974702]
```

Modulo overall phase, code-space Y error is <1e-12; no nominal SOEO leakage. Simultaneous logical `R=YA YB` inverts local XA/ZA and XB/ZB terms but preserves ZA ZB. The abstract echo `R exp(-i HT/2) R exp(-i HT/2)` cancels the first average-Hamiltonian moment of local quasistatic logical errors; commutators with ZZ and finite-gap leakage are not zero. FULL 7-spin ideal-INSTANTANEOUS echo insertion numerical stress:

- nominal Favg≈0.98072 (lower than no echo)
- 1.5% independent six intra gains: Favg≈0.758
- 1.5% independent eight gains: Favg≈0.774
- Repeat 3 such echo pairs (60 added logical 1-J exchange pulses) gives approximately Favg≈0.877 with 1.5% intra gains in another common-seed sample (nominal≈0.979).

The native physical pulses would themselves have the same gain errors and nonzero time; these optimistic figures are NOT ready-to-run gate benchmarks. Echo helps but does not rescue the basic gap design in HRL-like per-bond gain.

## F. EO ancilla as a SOEO leakage probe (PROVED, 7-spin exact gauge test)
An ordinary three-spin EO ancilla in `|0_L>` has an initialized singlet on its physical pair (5,6) and a spectator gauge spin 7. Use spin 5 to contact the four SOEO data spins by simultaneous four-link star `H=J sum_(i=1..4) S_i.S5` for JT=2pi. Then singlet/triplet readout of pair (5,6) is exactly the two-spin ancilla probe from the previous SOEO 6-spin report, with EO gauge spin7 completely inert. Code/eo_ancilla_star_probe.py verifies both EO gauge inputs:

- original SOEO S=0 => P_singlet=1 (no false flag);
- a single physical Z error on SOEO => P_singlet=1/9, triplet flag=8/9.

This is a SOEO–EO **measurement interface**, not an encoded SOEO–EO logical gate. The EO ancilla logical state is consumed by its physical S/T readout; its gauge is spectator. The 4-J star still violates strict 1-J requirements and may need genuine hardware or a more clever exact serial synthesis.

## G. Probabilistic EO -> SOEO conversion by singlet-sector filtering (ANALYTICAL; full 4-spin rho verified)
Start with unknown EO logical state rho_L, maximally mixed EO gauge I/2 and an additional uncorrelated reference spin I/2. The 4-spin total spin support is S=0 with weight 1/4 and S=1 with weight 3/4. Each ideal star singlet-accepted branch acts as `K_s=P_0-P_1/3`. After n fresh-ancilla acceptances,

```
P_accept(n) = 1/4 + (3/4) 9^(-n)
F_SOEO|accepted(n) = 1/(1+3*9^(-n)).
```

Rounds: 1 (accept .333333, purity .75), 2 (.259259,.964286), 3 (.251029,.995902), 4 (.250114,.999543). This works for all tested logical Pauli eigenstates and is linear for arbitrary unknown logical inputs. It is NOT deterministic encoding transfer; only useful when one-time conversion is worth 75% discard and multiple 4-J/readout rounds. SOEO->EO by tracing out spectator simply yields the logical EO state with mixed gauge, but does not itself make a gauge-pure EO state.

## H. Specific system recommendation, grounded in R143/R144
1. **Priority 1: lift an already exact and gauge-blind EO parity instrument to mixed SOEO(data)+EO(ancilla)**, by adding inert reference spins to data blocks. The R143/R144 47P/25D physical 9-spin instrument is an appealing candidate for 2 SOEO data + 1 EO ancilla, i.e. 11 physical spins, 9 active. R144 reports Kraus branches proportional to `Pi_even/odd tensor I_8` over data gauges, so this is promising; acquire its exact CSV and independently propagate all gauge-embedded 11-spin states. Also test XX via native 3P H on each EO triple with the known SOEO Z-frame correction.
2. **Priority 2: build real SOEO leakage/erasure measurement** separately. Four-J star with EO singlet-pair ancilla is a clean theoretical interface, but needs 4-J geometry or an exact short serial analogue; test physical S/T readout and repeated rounds. Do not equate heralded fidelity with decoded code performance.
3. **Priority 3: full hybrid stabilizer measurement** 4 SOEO data + EO ancilla = 19 spins, 15 of them active. Compare to all-EO 15-spin instrument. In all cases count reference spins, gauge sectors, idle and measurement overhead, leakage and number of real control lines. Don't use dense 2^19 unitaries; propagate code columns in reduced SU(2) representations.
4. **Exploratory only:** always-on-gapped interblock exchange, SAGE-inspired. Instead of simple noise-vulnerable all-to-all gap, investigate symmetric noise sweet spots, adiabatic pulse shaping, robust DCG and symmetry matched co-toggling; require improvement at sigma_pb=1.5% and sigma_iid=0.0006 without prohibitively long gate time.

## I. Prior art / novelty boundary
- Heinz, Sharma, Kattemölle, 'Exchange-only qubit stabilized by a single-spin qubit,' arXiv:2608.14214v1 (2026): hybrid EO+LD gauge transfer and SOEO physical-spin XXXX/ZZZZ QED. LD side has separate single-spin control.
- Foulk, Hoffman, Laubscher, Das Sarma, 'Singlet-only Always-on Gapless Exchange Qubits with Baseband Control,' PRL 135 (2025), arXiv:2501.18589: already proposes always-on spin-0 encodings and entangling gates using a single interqubit exchange with leakage suppression. Its physical model is NOT our isolated single-cross-pulse case; do not claim a broad single-cross no-go that conflicts with SAGE.
- Foulk et al., 'Singlet-only always-on gapless exchange (SAGE) spin qubits: Charge noise effects and two-qubit gates,' arXiv:2604.15419 (2026): explicitly studies charge noise, refocusing and pulse ramps. Our simple gap-mediated model does not establish literature novelty, nor does it fairly benchmark those more carefully designed SAGE pulses.
- R143/R144 user research reports: full 9-spin R144 47P/25D instrument has gauge-inclusive exact Kraus parity factorization; under static sigma=.015 and pulse IID .0006 it still has nontrivial leakage and wrong-syndrome error, so lifted ideal validity is not evidence of superior decoded-QEC performance.

## Validation notes
Run with `OPENBLAS_NUM_THREADS=1 python code/<script>.py`. The scripts are self-contained except some load the top section of `hybrid_7spin.py` for reusable spin operators. Use the generated evidence tables for reproducibility and compare each proposed target to full physical gauge and leakage behavior. Pulse files in this package are only analytical logical gate primitives, **not** unverified full 19-spin XXXX CSV sequences.