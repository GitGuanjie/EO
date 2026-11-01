# Scientific and editorial assessment: PRX / PRX Quantum style

**Status: author-review working draft, not a submission-ready PRX research article.**

This manuscript has been rewritten in the American Physical Society's REVTeX 4.2 two-column style; it follows the research-article progression Abstract → Introduction → Physical model → Exact result → Numerical evidence → Discussion → Data and author disclosures → References, plus separate Supplemental Material. The official [PRX instructions](https://journals.aps.org/prx/authors) and [PRX Quantum instructions](https://journals.aps.org/prxquantum/authors) were checked in November 2026.

## Why this version is more defensible

The former document was a chronological catalogue of R138–R154 experiments. The new manuscript makes one principal scientific claim: **compiling an exchange-only parity instrument with preparation/readout promises allows exact removal of two exchange pulses without weakening the full gauge-resolved Kraus maps**, and selection among the remaining state-preparation paths reduces a physically specified model of wrong-syndrome errors. The 30-control CZ and 15-spin weight-four constructions are supporting evidence and scope checks, not unrelated headline claims. We separate logical gate infidelity, syndrome error and leakage, and show a two-check coarse-graining counterexample.

## Gaps relative to a persuasive PRX paper

1. **Scope of novelty.** The boundary-pulse elimination is mathematically exact but is a special case of instrument equivalence/stabilizer-state preparation simplification. An exhaustive comparison with existing ancilla-aware and measurement-based compilation literature is still needed. A 2-control, 2-layer saving and ~9% model-dependent wrong-syndrome decrease alone may be insufficient for Physical Review X's broad-impact editorial criterion.
2. **Hardware performance.** No experimental shots, calibrated context-coupling noise, exchange-axis calibration or pulse-duration model underpin the numerical improvement. The 1.5% per-bond and 0.06% IID assumptions are *assumed* representative values, not precise published device calibrations.
3. **QEC relevance.** There are no repeated syndrome rounds, leakage-reduction units, measurement assignment errors, decoder simulations, logical error suppression or threshold results. A weight-four star reference is not a physical strict-linear implementation.
4. **Main open computational result.** A genuine **native nonfactorized** 9-spin parity-instrument pulse sequence shorter than 48 controls, with lower syndrome error at controlled leakage and duration, would strengthen the central claim substantially.
5. **Authorship/funding/reproducibility.** Author list, affiliation, grants, provenance of all numerical optimization runs and a permanent code/data DOI require confirmation. The package contains the original frozen source archives, but the Github source tree need not be fully self-contained until those archives are uploaded to a permanent repository.
6. **Independent audit.** The 9-spin smoke test is rerun here; full 15-spin verification and all 750 Monte Carlo draws have not been rerun in this editorial round. They are carefully identified as previously archived numerical results.
7. **References.** The 2011 Fong–Wandzura, 2013 Hickman et al., 2025 Heinz et al., 2025 Mądzik et al. and 2026 HRL papers have been checked against publisher pages, but the literature review must be broadened before submission. PRX requires **article titles** in the reference list; this version supplies them.
8. **AI disclosure.** APS requires author responsibility and appropriate disclosure of substantive AI assistance; final wording should be verified against institutional and APS policies.

**Journal fit:** The current result is closest to a focused theoretical/numerical PRX Quantum or Physical Review Research submission, not an established PRX-level broad conceptual breakthrough. The requested PRX **format** is implemented; journal-level **originality and impact** are not certified by typography.

## Deliverables

- `main.tex`, `main.pdf` — official REVTeX 4.2-style main article, two-column.
- `supplement.tex`, `supplement.pdf` — derivations, gauge checks, and numerical-method details.
- `references.bib` — source records; references are additionally embedded in `main.tex` for portable compilation without a BibTeX binary.
- `figures/` — vector-PDF and PNG figures created from confirmed archived summary values or explicitly assumed topology.
- `data/` — exact pulse schedule CSV files.
- `source_evidence/R154_NATIVE_PARITY_RESULTS.zip`, `source_evidence/R143_RESULTS.zip` — frozen original source archives.
- `POPULAR_SUMMARY.txt` — nontechnical summary, <150 words.
- `MAIN_ARTICLE.md`, `SUPPLEMENTARY.md` — editable Markdown convenience exports; LaTeX/PDF are the authoritative formatted versions.

Compiled using `pdflatex` and visually reviewed with rendered pages. No copyright-protected figure from another publication was reused.