# Native exchange-only SOEO–EO error detection and symmetry-protected syndrome measurements

**Status:** internal working paper; **not peer-reviewed**, no hardware validation and no demonstrated decoded quantum-error-correction threshold.  
**Updated:** 2026-11-01.

This repository-ready research archive consolidates the SOEO/EO theory and simulated results developed across the star-revival, hybrid-interface, native-grid detector, K4 echo and exact-detector-manifold investigations (30–31 October 2026). It distinguishes **low-level SOEO total-spin detection** from **high-level logical $XXXX/ZZZZ$ stabilizer measurements**.

## Start here

- **[Readable working paper (Markdown)](manuscript/SOEO_EO_QEC_WORKING_PAPER.md)** — derivations, assumptions, benchmarks, negative results and remaining milestones.
- **[Typeset working paper (PDF)](manuscript/SOEO_EO_QEC_WORKING_PAPER.pdf)** — the same manuscript as a 10-page review draft.
- **[Raw model benchmarks](data/model_benchmarks.csv)** — named source round, pulse budget, acceptance and conditional error.
- **[Original 13P native-grid word](data/GRID_13P_SOEO_SPIN0_DETECTOR.csv)** and **[R146 t=0.12 word](data/R146_t12_K4_0_13P.csv)** — physical pulse areas in the convention $X_{ij}(a)=e^{i\pi aP^{(s)}_{ij}}$.
- **[Reproduction code and evidence](reproduction/)** — scripts and saved numerical outputs grouped by source round, with original chronology preserved.
- **[Original research reports](source_reports/)** — extended notes supporting the consolidated paper.

## Research findings at a glance

| Research claim | Evidence level | Important limitation |
|---|---|---|
| Four simultaneous exchange links yield an analytic spin-sector filter with $O(\sigma^4)$ single-probe infidelity on initially encoded states. | Analytic + six-spin simulation | Violates the strict one-bond serial hardware constraint; coherent second-order logical drift remains. |
| 11P serial spin-sector detector; 13P after 3x3 nearest-neighbor routing. | Full seven-spin nominal numerical verification | Nonzero first-order gain susceptibility, S/T preparation/readout not counted, not yet a fault-tolerant instrument. |
| Four K4-equivalent variants allow 52P four-cycle noise mitigation under persistent gains. | Correlated-gain + IID Monte Carlo | Conditional fidelity of accepted trajectories, not decoded QEC failure or throughput. |
| Forward/inverse 12-cycle echo further reduces correlated residual. | Model-only, 156P | Lower acceptance, 12 readout/reset operations; advantage can vanish for renewed gains. |
| Exact 11P core has a numerical local one-dimensional angle family. | Numerical constraint continuation and seven-spin verification | Better accepted-state error with reduced acceptance; no global optimality. |
| Existing gauge-independent EO parity instruments may lift to SOEO with inert reference spins. | Algebraic code mapping | Integrated 11/19-spin routed physical measurement **not yet independently verified** here. |

## Noise-model conventions

Default model in the source simulations: static physical bond offset $\delta_b\sim\mathcal N(0,0.015^2)$ held through all measurement cycles, and independent pulse jitter $\eta_{b,k}\sim\mathcal N(0,0.0006^2)$. Physical gates use isotropic Heisenberg exchange; ideal input state, perfect S/T measurement and reset are assumed unless noted. These are **project assumptions**, not measured performance of a specific QPU.

## Reproduce

Requires Python 3, NumPy and SciPy; memory usage depends on the script. Run from each round directory because some modules use sibling files:

```bash
cd reproduction/SOEO_EO_R146_PARETO_NO_GO_20261031/code
OPENBLAS_NUM_THREADS=1 python verify_r146.py
```

For a basic native-grid check:

```bash
cd reproduction/SOEO_EO_GRID_NATIVE_QED_20261030/code
OPENBLAS_NUM_THREADS=1 python grid13_verify.py
```

Original scripts and evidence are preserved but **not all Monte Carlo campaigns have been re-run during editorial assembly**. The SHA256SUMS file records each packaged file. Required R146 numerical `.npz` verification arrays are included in `reproduction/`; other large raw simulation files remain in the original source research archives.

## Literature and priority

The work is motivated by Heinz, Sharma and Kattemölle, [arXiv:2608.14214](https://arxiv.org/abs/2608.14214), but their hybrid LD single-spin-control and physical $XXXX/ZZZZ$ detector are **distinct** from this native-exchange SOEO total-spin probe. See also the [HRL QPU (2026)](https://doi.org/10.1038/s41586-026-10754-7), [SAGE PRL (2025)](https://doi.org/10.1103/j1hn-k5m8) and [full-permutation DD (2024)](https://doi.org/10.1103/PRXQuantum.5.020356). **No novelty or publication-priority claims are made without an independent systematic literature audit.**

## Publication / repository privacy

The material should remain private until the owner approves authorship, novelty review, intellectual-property clearance and release. Recommending a **private dedicated repository**, e.g. `SOEO-EO-exchange-QEC`, rather than placing unreviewed QEC data in an unrelated public repository.