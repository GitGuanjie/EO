# Exchange-only spin-qubit control and native QEC measurements

**Current PRX-style paper rewrite:** [Measurement-Aware EO Compilation](prx-manuscript/README.md) (new research manuscript, with REVTeX LaTeX source, supplementary material, figures and editorial audit). The older MANUSCRIPT.md is preserved as historical R138–R154 context.

**Computational research synthesis, R138–R154 (working draft, November 2026).**

This folder collects the analysis previously staged in a draft PR in `Nuclear-high-spin-VPC`. It now lives in the dedicated **EO** repository.

## Start here

- [Paper-style manuscript](MANUSCRIPT.md) — six-spin simultaneous exchange, first-order gain errors, encoded leakage, nine-spin stabilizer extraction, and five-EO four-body references.
- [Results ledger](RESULTS_LEDGER.md) — what was reproduced, improved, disproved within a tested class, or remains open.
- [Reproducibility and source evidence](REPRODUCIBILITY.md) — conventions, audit checklist, original run archives.
- [Read the paper as PDF](EO_QEC_Research_Synthesis_Readable.pdf) — text-focused PDF rendering of the working manuscript (no embedded plots); [build instructions](BUILD_PDF.md).
- [Full-precision 48-control ZZ-check sequence](selected_sequences/ZZ_48C_P1R0.csv).
- [Full-precision 30-control exact CZ sequence](selected_sequences/CZ30C_R143_STATIC_OPT.csv).
- [Six-layer dual-static-gain three-spin sequence](selected_sequences/THREE_SPIN_6L_DUAL_GAIN.csv).

## Verified headline results

| Topic | Numerical result | Qualification |
|---|---|---|
| Six-spin exact CZ | 30 controls, ASAP depth 19, static per-bond harm `Hpb = 32.011918` | No first-order J34 cancellation |
| Three-spin simultaneous robust SWAP | 6 layers/12 positive controls; static gain infidelity scales quartically | Only isolated three-spin encoded operation, **not** robust two-EO CZ |
| Nine-spin ZZ syndrome instrument | Reduced 50C/29D to **48C/27D** | Exact Kraus operator up to outcome phases |
| Noisy syndrome extraction | Average wrong-syndrome probability 1.1036% → 1.0045% (750 paired trials) | Simulated static gain 1.5%, IID jitter 0.06%; not hardware data |
| Five-EO ZZZZ/XXXX references | 92C and 116C sequences, coherent 15-spin validation | Requires **hypothetical star connections**, not strict linear geometry |

**Status:** numerical research only. No validated fault-tolerance threshold, repeated logical error suppression, physical hardware demonstration, or first-order error-free encoded two-EO CZ is claimed.

**PDF provenance:** the PDF committed here is an easy-to-open, text-focused rendering of the manuscript. The original figure-rich, typeset nine-page PDF and the frozen research-code ZIP archives remain available through the originating ChatGPT conversation; they have **not** been copied to this GitHub folder. The Markdown is the canonical editable manuscript in GitHub.

## Publication caution

Before publication, rerun the full independent validators, confirm exact physical geometry and noise calibration against the cited experimental reference, and complete literature/new-result novelty review.
