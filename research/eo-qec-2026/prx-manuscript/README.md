# PRX-format working manuscript: Measurement-Aware Exchange-Only Compilation

**This is a new research-article rewrite, not an edited chronology of search rounds.** It is an **APS REVTeX 4.2 / Physical Review X-style** numerical working draft. It has not been submitted or accepted, and its current contribution does **not** yet establish the scope or broad significance expected by PRX.

## Read the paper

- [Main article (GitHub Markdown)](MAIN_ARTICLE.md) — central theorem, physical model, numerical results, literature and limitations
- [REVTeX two-column source](main.tex) — authoritative typeset manuscript
- [Supplementary Material](SUPPLEMENTARY.md) and [LaTeX source](supplement.tex) — gauge- and leakage-aware mathematical detail
- [Vector figures](figures/) — view directly in GitHub as SVG
- [Figure generation Python](make_figures.py) — regenerates PDF/SVG/PNG figures
- [Full article reference database](references.bib)
- [Popular summary](POPULAR_SUMMARY.txt)
- [Editorial readiness assessment](EDITORIAL_READINESS.md) — gaps that remain before a credible PRX submission

The compiled **5-page two-column main PDF** and **3-page Supplementary PDF** are available as attachments in the originating ChatGPT conversation, together with a ZIP containing source, high-quality PDF figures and frozen R143/R154 research archives. Binary PDFs are **not** currently committed here.

## Build the actual two-column PDF

With a TeX Live installation containing `revtex4-2` and Python Matplotlib:

```bash
python make_figures.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error supplement.tex
pdflatex -interaction=nonstopmode -halt-on-error supplement.tex
```

No BibTeX binary is necessary: article-title references are embedded in `main.tex` for portable compilation. `references.bib` is provided for future editing.

## Verified main result and proper scientific scope

A nine-spin, two-data EO parity measurement uses an exact gauge-aware ancilla input/readout equivalence to eliminate two physical exchange controls (50 to **48** controls; 29 to **27** nominal ASAP layers). A separate ancilla preparation path reduces wrong-syndrome quadratic curvature **50.1050 to 46.0078** under a shot-static independent per-bond gain model. A frozen 750-pair simulation at static sigma=1.5%, IID sigma=0.06% estimates wrong-syndrome probability **1.1036% to 1.0045%**. The full nine-spin 48C ZZ Kraus test was independently rerun (residuals 1.58e-15 and 1.80e-15).

The paper also explains how the previously optimized [30-control CZ](../selected_sequences/CZ30C_R143_STATIC_OPT.csv) fits into this system-level discussion, and records CZ-factorized ZZZZ/XXXX reference instruments on a **hypothetical** 15-spin star graph.

**No** hardware-calibrated improvement, fault-tolerance threshold, repeated QEC, native non-CZ four-body primitive, or universal two-EO first-order gain cancellation is claimed. Author list, affiliation, funding and a permanent data DOI remain to be finalized.

Earlier [R138–R154 research synthesis](../MANUSCRIPT.md) remains as a historical document; this research-paper rewrite is the current editorial draft.
