# Exchange-only spin-qubit control and native QEC measurements

**Computational research synthesis, R138–R154 (working draft, November 2026).**

This folder collects the analysis previously staged in a draft PR in `Nuclear-high-spin-VPC`. It now lives in the dedicated **EO** repository.

## Start here

- [Paper-style manuscript](MANUSCRIPT.md) — six-spin simultaneous exchange, first-order gain errors, encoded leakage, nine-spin stabilizer extraction, and five-EO four-body references.
- [Results ledger](RESULTS_LEDGER.md) — what was reproduced, improved, disproved within a tested class, or remains open.
- [Reproducibility and source evidence](REPRODUCIBILITY.md) — conventions, audit checklist, original run archives.
- [Build the paper](BUILD_PDF.md) — PDF instructions.
- [Full-precision 48-control ZZ-check sequence](selected_sequences/ZZ_48C_P1R0.csv).

## Verified headline results

| Topic | Numerical result | Qualification |
|---|---|---|
| Six-spin exact CZ | 30 controls, ASAP depth 19, static per-bond harm `Hpb = 32.011918` | No first-order J34 cancellation |
| Three-spin simultaneous robust SWAP | 6 layers/12 positive controls; static gain infidelity scales quartically | Only isolated three-spin encoded operation, **not** robust two-EO CZ |
| Nine-spin ZZ syndrome instrument | Reduced 50C/29D to **48C/27D** | Exact Kraus operator up to outcome phases |
| Noisy syndrome extraction | Average wrong-syndrome probability 1.1036% → 1.0045% (750 paired trials) | Simulated static gain 1.5%, IID jitter 0.06%; not hardware data |
| Five-EO ZZZZ/XXXX references | 92C and 116C sequences, coherent 15-spin validation | Requires **hypothetical star connections**, not strict linear geometry |

**Status:** numerical research only. No validated fault-tolerance threshold, repeated logical error suppression, physical hardware demonstration, or first-order error-free encoded two-EO CZ is claimed.

The paper-style PDF and frozen round-by-round ZIP archives were also produced in ChatGPT. See the conversation attachment links for the original binary downloads; if binaries are not present in this repository, the Markdown text is the canonical browsable version here.

## Publication caution

Before publication, rerun the full independent validators, confirm exact physical geometry and noise calibration against the cited experimental reference, and complete literature/new-result novelty review.
