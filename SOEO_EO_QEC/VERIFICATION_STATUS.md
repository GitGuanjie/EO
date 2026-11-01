# Package verification log — 1 November 2026

- Working paper rendered with Pandoc/XeLaTeX, 10 letter-sized pages, visually inspected as a ten-page contact sheet; no obvious page clipping or overlap.
- `reproduction/SOEO_EO_GRID_NATIVE_QED_20261030/code/grid13_verify.py`: **PASS** in the repackaged tree with `OPENBLAS_NUM_THREADS=1`. Reproduces ideal seven-spin nominal residual ~`2.19e-15` and 1200-draw gain model (false triplet 0.67194%, accepted wrong 0.08446%, full state wrong 0.75544% at sigma=0.015).
- `reproduction/SOEO_EO_R146_PARETO_NO_GO_20261031/code/verify_r146.py`: **PASS** in the repackaged tree after restoring required numerical `.npz` evidence. Reproduces finite-family constraint value, angle-manifold harm values, and all twelve t>0 full seven-spin K4 checks.
- Original saved reports and many code/evidence artifacts are included without rewriting their historical conclusions; remaining campaigns were **not** independently re-executed in this editorial task.
- **NOT** physically measured QEC or independent peer review. Human scientific audit required before publication.