# EO-native QEC: native parity measurements and encoded flags

This folder hosts our **exchange-only (EO) stabilizer extraction and flag-qubit research**. It was migrated from a draft branch of `GitGuanjie/Nuclear-high-spin-VPC` into this dedicated **EO** repository.

**Read:** [English working paper](PAPER.md) · [Paper PDF](PAPER.pdf) · [Evidence and limitations](EVIDENCE_LEDGER.md) · [Pulse sequences](sequences/) · [Figures](figures/).

## Main model results

| Construction | Strict positive exchange pulses | Evidence |
| --- | ---: | --- |
| Four-logical-EO ZZZZ | 92P / 44D | Nominal encoded-instrument simulation |
| Rotated four-logical-EO X-tilde check | 92P / 44D | Nominal encoded-instrument simulation |
| Fixed-frame XXXX | 100P / 45D | Nominal encoded-instrument simulation |
| Flagged rotated four-body check | 140P / 60D | Selected fault-channel tests |
| Three-check X-Z-X without / with flag | 276P / 324P | Limited correlated-gain simulations |

In one fixed-codeword, fixed-gauge numerical setting, 50 paired samples yielded conditional encoded logical errors of **0.06682%** without flag versus **0.03744%** with flag, while acceptance fell from 88.70% to 86.24%. These are **not experimental measurements, fault-tolerance thresholds, or a complete distance-3 QEC validation**.

## Folder layout

- `PAPER.md`, `PAPER.pdf` — research-style English manuscript
- `EVIDENCE_LEDGER.md` — explicit model assumptions, verification and gaps
- `BUILD_PDF.md` — PDF build guidance
- `sequences/` — physical positive-exchange CSV words and 18-spin geometry
- `figures/` — SVG geometry and result visualization
- `SOURCE_PROVENANCE.md` — migration reference

The full raw numerical evidence JSON and original archived research ZIPs have **not** yet been mirrored to GitHub; see the downloadable research archive in the source ChatGPT conversation. Please do not interpret the included pulse CSVs alone as an independently reproduced complete QEC proof.

The pre-existing [`research/eo-qec-2026`](../eo-qec-2026/) folder has been preserved without modification.
