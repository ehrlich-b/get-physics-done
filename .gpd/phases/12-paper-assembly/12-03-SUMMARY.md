---
phase: 12-paper-assembly
plan: 03
depth: full
one-liner: "Wrote Section VI (numerical verification) with 4 publication figures from Phase 11 data, verified manuscript consistency: all cross-references resolve, conventions uniform, L1-L8 chain complete, all 10 anchors cited, no overclaiming"
subsystem: paper-writing
tags: [numerical-verification, exact-diagonalization, area-law, MVEH, figures, manuscript-assembly]

requires:
  - phase: 12-paper-assembly
    plan: 01
    provides: Paper 6 infrastructure, introduction, discussion, bibliography
  - phase: 12-paper-assembly
    plan: 02
    provides: Sections II-V (lattice, area law, equilibrium, Einstein)
  - phase: 11-numerical-verification
    provides: ED benchmarks, area-law data, K_A locality (SRF=0.9993), MVEH numerical support

provides:
  - Section VI (numerical.tex): complete numerical verification with ED benchmarks, area-law analysis (1D+2D), K_A locality, MVEH check
  - 4 publication-quality figures generated from Phase 11 JSON data
  - Figure generation script (paper6/figures/generate_figures.py)
  - Verified manuscript consistency across all 7 sections
  - graphicx package added to preamble.sty
  - vandeWetering citation key corrected in lattice.tex

affects: []

methods:
  added: [matplotlib figure generation from JSON data, cross-reference validation, convention sweep]
  patterns: [two-panel figure layout, honest numerical framing pattern]

key-files:
  created:
    - paper6/sections/numerical.tex
    - paper6/figures/generate_figures.py
    - paper6/figures/fig_cc_fit.pdf
    - paper6/figures/fig_2d_scatter.pdf
    - paper6/figures/fig_ka_locality.pdf
    - paper6/figures/fig_mveh_check.pdf
  modified:
    - paper6/preamble.sty
    - paper6/sections/lattice.tex

key-decisions:
  - "All numerical results framed as 'consistent with' and 'supporting evidence', never 'proves' or 'demonstrates'"
  - "2D R^2=0.885 shortfall honestly noted with PBC wrapping explanation and Spearman alternative"
  - "MVEH check includes perturbation method note explaining why Hamiltonian perturbation (not unitary) is needed"
  - "Summary table (Table II) lists all key results with benchmarks and pass/fail status"

patterns-established:
  - "Two-panel figure layout for paired analysis (data + control, or data + scaling)"
  - "Systematic cross-reference and convention verification before manuscript completion"

conventions:
  - "natural units (hbar=c=k_B=1)"
  - "metric = (-,+,+,+)"
  - "entropy = von Neumann, nats: S = -Tr(rho ln rho)"
  - "modular Hamiltonian: K = -ln(rho_A)"
  - "Einstein tensor: G_ab = R_ab - (1/2)Rg_ab"
  - "lattice Hamiltonian: H = sum J F_xy (SWAP)"

plan_contract_ref: ".gpd/phases/12-paper-assembly/12-03-PLAN.md#/contract"
contract_results:
  claims:
    claim-numerical-presentation:
      status: passed
      summary: "Section VI presents Phase 11 numerical results with honest framing ('consistent with', 'supporting evidence', 'do not constitute proof'). Finite-size caveats present. 2D R^2=0.885 shortfall noted with PBC explanation. All three benchmarks (TFI c=0.574, Heisenberg c=1.060, FM S=0) stated."
      linked_ids: [deliv-numerical, deliv-fig-cc, deliv-fig-2d, test-numerical-honest, test-figures-present, test-benchmarks-included, ref-calabresecardy2004]
    claim-manuscript-complete:
      status: passed
      summary: "Manuscript is complete and internally consistent: all cross-references resolve (0 unresolved), all 9 files have identical convention assertions, L1-L8 all present in corresponding sections, all 10 anchors cited, no overclaiming language, estimated 16-18 pages (within PRD 16-24 target). LaTeX compilation not verified (no pdflatex available)."
      linked_ids: [deliv-main-final, test-convention-sweep, test-chain-complete, test-anchor-coverage, ref-jacobson2016]
  deliverables:
    deliv-numerical:
      status: passed
      path: "paper6/sections/numerical.tex"
      summary: "Section VI with ED setup, benchmark validation (TFI+Heisenberg+FM), 1D area-law analysis, 2D boundary vs volume, K_A locality (SRF=0.9993), MVEH check (100% delta_S<0), summary table"
      linked_ids: [claim-numerical-presentation, test-numerical-honest, test-figures-present, test-benchmarks-included]
    deliv-fig-cc:
      status: passed
      path: "paper6/figures/fig_cc_fit.pdf"
      summary: "Two-panel figure: (a) S(L) vs CC scaling variable for N=8,12,16,20 with fit lines, (b) finite-size scaling of c converging to 1"
      linked_ids: [claim-numerical-presentation]
    deliv-fig-2d:
      status: passed
      path: "paper6/figures/fig_2d_scatter.pdf"
      summary: "Two-panel figure: (a) S vs boundary with R^2=0.885 regression, (b) S vs volume with R^2=0.491 regression"
      linked_ids: [claim-numerical-presentation]
    deliv-main-final:
      status: partial
      path: "paper6/main.tex"
      summary: "All sections populated, all cross-references resolve, conventions uniform, bibliography complete. Partial because pdflatex not available for compilation verification."
      linked_ids: [claim-manuscript-complete, test-compilation, test-convention-sweep, test-chain-complete, test-anchor-coverage]
  acceptance_tests:
    test-numerical-honest:
      status: passed
      summary: "Grep confirms: 'consistent with' (11 occurrences), 'supporting evidence' (1), 'do not constitute proof' (1). Zero occurrences of 'proves', 'demonstrates', 'confirms the'. Finite-size caveats in Sec 6.3.2 and 6.6. 2D R^2=0.885 shortfall noted with PBC explanation."
      linked_ids: [claim-numerical-presentation, deliv-numerical]
    test-figures-present:
      status: passed
      summary: "4 figures generated: fig_cc_fit.pdf, fig_2d_scatter.pdf, fig_ka_locality.pdf, fig_mveh_check.pdf. All referenced in text via \ref{fig:*}. All have captions with honest framing."
      linked_ids: [claim-numerical-presentation, deliv-fig-cc, deliv-fig-2d]
    test-benchmarks-included:
      status: passed
      summary: "Sec 6.2 presents all three benchmarks: TFI critical c=0.574 (exact 0.5), Heisenberg AFM c=1.060 (exact 1.0), FM S=0 (exact). Summary table (Table II) also lists all values."
      linked_ids: [claim-numerical-presentation, deliv-numerical]
    test-compilation:
      status: not_attempted
      summary: "pdflatex not available on system. Structural verification performed instead: all files exist, all cross-references resolve, all citation keys have bib entries, page count estimated at 16-18."
      linked_ids: [claim-manuscript-complete, deliv-main-final]
    test-convention-sweep:
      status: passed
      summary: "All 9 paper6 files have identical ASSERT_CONVENTION lines. No (+,-,-,-) metric, no log_2 entropy, no Assumption A5, K=-ln(rho_A) throughout."
      linked_ids: [claim-manuscript-complete, deliv-main-final]
    test-chain-complete:
      status: passed
      summary: "All 8 links verified: L1 (lattice.tex), L2 (lattice.tex), L3 (lattice.tex), L4 (arealaw.tex), L5 (arealaw.tex), L6 (equilibrium.tex), L7 (equilibrium.tex), L8 (einstein.tex). Table I in introduction lists all."
      linked_ids: [claim-manuscript-complete, deliv-main-final]
    test-anchor-coverage:
      status: passed
      summary: "All 10 anchors cited: Jacobson1995 (1), Jacobson2016 (20), ConnesRovelli1994 (8), Sorce2024 (3), Hastings2007 (3), VanRaamsdonk2010 (1), LMVR2014 (4), Faulkner2014 (3), CCM2017 (2), Paper5 (12)."
      linked_ids: [claim-manuscript-complete, deliv-main-final]
  references:
    ref-calabresecardy2004:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited in Sec VI benchmark validation (CC formulas for TFI and Heisenberg)"
    ref-jacobson2016:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited throughout manuscript (20 occurrences); no new citations added in this plan"
  forbidden_proxies:
    fp-numerical-as-proof:
      status: rejected
      notes: "Section VI explicitly states 'do not constitute proof' and uses 'consistent with' throughout. Summary table shows results as supporting evidence."
    fp-gap-glossing:
      status: rejected
      notes: "Discussion (Plan 01) identifies all gaps. Section VI notes 2D R^2 shortfall and finite-size limitations."
    fp-overclaim-scope:
      status: rejected
      notes: "Grep confirms no instances of 'prove MVEH', 'derive G', 'derive d=3+1', 'predict Lambda' in any section."
  uncertainty_markers:
    weakest_anchors:
      - "2D R^2(boundary) = 0.885 < 0.9 target -- PBC wrapping on 4x4 lattice"
      - "All ED results are N=8-20, far from thermodynamic or continuum limit"
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations:
      - "If larger-N simulations show volume-law scaling, the area-law claim weakens"
      - "If K_A locality breaks down at larger N, the perturbative delta S argument weakens"

duration: 6min
completed: 2026-03-22
---

# Phase 12, Plan 03: Numerical Verification Section and Final Assembly

**Wrote Section VI (numerical verification) with 4 publication figures from Phase 11 data, verified manuscript consistency: all cross-references resolve, conventions uniform, L1-L8 chain complete, all 10 anchors cited, no overclaiming**

## Performance

- **Duration:** 6 min
- **Started:** 2026-03-22T18:48:04Z
- **Completed:** 2026-03-22T18:53:45Z
- **Tasks:** 2
- **Files created:** 6
- **Files modified:** 2

## Key Results

- Section VI presents Phase 11 numerical results with honest framing across 6 subsections: ED setup, benchmarks, 1D area law, 2D area law, K_A locality, MVEH check [CONFIDENCE: HIGH]
- 4 publication-quality figures generated from Phase 11 JSON data via matplotlib [CONFIDENCE: HIGH]
- Manuscript consistency verified: 0 unresolved cross-references, uniform conventions across all 9 files, all 10 anchors cited [CONFIDENCE: HIGH]
- L1-L8 chain complete and traceable through corresponding sections [CONFIDENCE: HIGH]
- No overclaiming language found in any section [CONFIDENCE: HIGH]
- Estimated page count: 16-18 pages (within PRD 16-24 target) [CONFIDENCE: MEDIUM -- requires pdflatex for exact count]

## Task Commits

1. **Task 1: Section VI + figures** - `470c60c` (document)
2. **Task 2: Final assembly verification** - `04a2375` (fix)

## Files Created/Modified

- `paper6/sections/numerical.tex` - Sec VI: ED setup, benchmarks, 1D/2D area law, K_A locality, MVEH, summary table
- `paper6/figures/generate_figures.py` - matplotlib script generating all 4 figures from Phase 11 JSON
- `paper6/figures/fig_cc_fit.pdf` - 1D CC fit + finite-size scaling
- `paper6/figures/fig_2d_scatter.pdf` - 2D boundary vs volume scatter
- `paper6/figures/fig_ka_locality.pdf` - K_A Pauli coefficient decay + SRF bars
- `paper6/figures/fig_mveh_check.pdf` - MVEH delta_S distribution + quadratic scaling
- `paper6/preamble.sty` - Added graphicx package for figure inclusion
- `paper6/sections/lattice.tex` - Fixed vandeWetering citation key (2018->2019)

## Figures Produced

| Figure | File | Description | Key Feature |
| --- | --- | --- | --- |
| Fig. 1 | fig_cc_fit.pdf | 1D Calabrese-Cardy analysis | CC fits for N=8,12,16,20; c converges to 1 |
| Fig. 2 | fig_2d_scatter.pdf | 2D boundary vs volume | R^2(bd)=0.885 vs R^2(vol)=0.491 |
| Fig. 3 | fig_ka_locality.pdf | K_A locality | SRF=0.9993 for Heisenberg, decay profile |
| Fig. 4 | fig_mveh_check.pdf | MVEH check | 100% delta_S<0, quadratic scaling |

## Verification Results (Final Assembly)

| Check | Status | Details |
| --- | --- | --- |
| Cross-references | PASS | 0 unresolved \ref{} (all labels defined) |
| Convention sweep | PASS | 9/9 files identical ASSERT_CONVENTION |
| L1-L8 chain | PASS | All 8 links in corresponding sections |
| 10 anchors cited | PASS | All 10 cited at least once (total 67 citations) |
| Forbidden proxies | PASS | No overclaiming language found |
| MVEH not Assumption A5 | PASS | No "Assumption A5" in any section |
| Page count | PASS | ~16-18 estimated (target 16-24) |
| Compilation | NOT ATTEMPTED | No pdflatex available |

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 4 - Missing Component] graphicx package**

- **Found during:** Task 1 figure inclusion
- **Issue:** preamble.sty lacked \usepackage{graphicx} for \includegraphics
- **Fix:** Added graphicx to package list
- **Committed in:** 470c60c

**2. [Rule 1 - Code Bug] vandeWetering citation key**

- **Found during:** Task 2 cross-reference check
- **Issue:** lattice.tex cited vandeWetering2018 but bib entry is vandeWetering2019 (fix from Plan 02 was not staged)
- **Fix:** Committed the working copy which already has the correction
- **Committed in:** 04a2375

**3. [Rule 4 - Missing Component] LaTeX compiler unavailable**

- **Found during:** Task 2 compilation step
- **Issue:** No pdflatex on system
- **Fix:** Performed structural verification instead (cross-refs, citation keys, file existence, page estimate)
- **Impact:** Compilation deferred to environment with compiler

---

**Total deviations:** 3 auto-fixed (1 missing package, 1 citation key, 1 environment gate)
**Impact on plan:** None. All content correct; compilation is downstream.

## Open Questions

- LaTeX compilation not verified (no pdflatex) -- deferred to environment with compiler
- Equation numbering will be set at compile time; all \ref labels resolve structurally
- 6 bib entries (BennettWiesner1992, BisognanoWichmann1975, EisertCramerPlenio2010, HancheOlsen1985, Holevo1973, Unruh1976) are supporting references included for completeness but not cited in the current text

## Self-Check: PASSED

- [x] All 6 created files exist
- [x] Both commits (470c60c, 04a2375) exist in git log
- [x] Convention assertions in all .tex file headers (9/9 identical)
- [x] All 4 figures readable PDFs
- [x] Section VI uses honest framing throughout
- [x] 2D R^2=0.885 shortfall noted with explanation
- [x] All 3 benchmarks (TFI, Heisenberg, FM) present with values
- [x] K_A connects to Sec III modular Hamiltonian locality
- [x] MVEH connects to Sec IV definitional framing
- [x] Contract coverage complete: all claim/deliverable/test/reference/proxy IDs addressed

---

_Phase: 12-paper-assembly, Plan 03_
_Completed: 2026-03-22_
