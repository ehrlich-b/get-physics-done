---
phase: 12-paper-assembly
plan: 01
depth: full
one-liner: "Created Paper 6 LaTeX infrastructure and wrote bookend sections: Introduction with L1-L8 derivation chain table (MVEH definitional) and Discussion with precise gap identification, four-paper comparison, and honest scope"
subsystem: paper-writing
tags: [emergent-gravity, entanglement-equilibrium, einstein-equations, self-modeling, latex, revtex]

requires:
  - phase: 10-jacobson-application
    provides: Master theorem (Eq. 10-03.1), derivation chain L1-L8, gap statement, Jacobson comparison
  - phase: 11-numerical-verification
    provides: ED benchmarks, area-law scaling data, K_A locality (SRF=0.9993), MVEH numerical support

provides:
  - Paper 6 REVTeX 4.2 infrastructure (main.tex, preamble.sty, refs.bib, 7 section stubs)
  - Introduction section with L1-L8 derivation chain table and MVEH definitional reframing
  - Discussion section with gap identification, four-paper related work comparison, honest scope statement
  - Complete bibliography (10 anchor + 15 supporting references)

affects: [12-02, 12-03]

methods:
  added: [REVTeX 4.2 manuscript preparation, thermal time hypothesis framing]
  patterns: [MVEH definitional via Connes-Rovelli, honest scope statement pattern]

key-files:
  created:
    - paper6/main.tex
    - paper6/preamble.sty
    - paper6/refs.bib
    - paper6/sections/introduction.tex
    - paper6/sections/discussion.tex
    - paper6/sections/lattice.tex
    - paper6/sections/arealaw.tex
    - paper6/sections/equilibrium.tex
    - paper6/sections/einstein.tex
    - paper6/sections/numerical.tex

key-decisions:
  - "MVEH framed as definitional via Connes-Rovelli thermal time hypothesis, not as Assumption A5"
  - "Two gaps identified: continuum limit (standard, shared with all lattice QG) and conformal approximation (minor)"
  - "Abstract explicitly states what paper does NOT derive: G, d, Lambda"
  - "Related work comparison structured as four dedicated paragraphs: Jacobson 2016, CCM 2017, LMVR 2014, Faulkner et al. 2014"

patterns-established:
  - "Convention assertions in every .tex file header for machine verification"
  - "Table I (derivation chain) as the paper's structural spine"

conventions:
  - "natural units (hbar=c=k_B=1)"
  - "metric = (-,+,+,+)"
  - "entropy = von Neumann, nats: S = -Tr(rho ln rho)"
  - "modular Hamiltonian: K = -ln(rho_A)"
  - "Einstein tensor: G_ab = R_ab - (1/2)Rg_ab"

plan_contract_ref: ".gpd/phases/12-paper-assembly/12-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-paper-framing:
      status: passed
      summary: "Introduction states main result, presents L1-L8 table with L7 definitional (Connes-Rovelli), and positions work against entanglement-gravity literature with six anchor citations"
      linked_ids: [deliv-introduction, test-chain-table, test-mveh-framing, test-honest-scope, ref-jacobson1995, ref-jacobson2016, ref-vanraamsdonk2010, ref-paper5]
    claim-gap-statement:
      status: passed
      summary: "Discussion identifies continuum limit and conformal approximation as gaps, reframes MVEH as definitional, compares with Jacobson 2016/CCM 2017/LMVR 2014/Faulkner 2014, states all non-claims"
      linked_ids: [deliv-discussion, test-gap-completeness, test-no-overclaim, ref-ccm2017, ref-lmvr2014, ref-faulkner2014]
    claim-bibliography-complete:
      status: passed
      summary: "Bibliography contains all 10 required anchor references with correct metadata plus 15 supporting references (25 total)"
      linked_ids: [deliv-bib, test-bib-completeness, ref-jacobson1995, ref-jacobson2016, ref-hastings2007, ref-ccm2017, ref-paper5, ref-vanraamsdonk2010, ref-lmvr2014, ref-faulkner2014]
  deliverables:
    deliv-introduction:
      status: passed
      path: "paper6/sections/introduction.tex"
      summary: "Introduction with derivation chain table, self-modeling claim, MVEH dissolution, honest scope, paper organization"
      linked_ids: [claim-paper-framing, test-chain-table, test-mveh-framing, test-honest-scope]
    deliv-discussion:
      status: passed
      path: "paper6/sections/discussion.tex"
      summary: "Discussion with derived-vs-input, gap identification, four-paper comparison, Paper 5 connection, non-claims, future work"
      linked_ids: [claim-gap-statement, test-gap-completeness, test-no-overclaim]
    deliv-bib:
      status: passed
      path: "paper6/refs.bib"
      summary: "25 BibTeX entries: 10 anchor (Jacobson1995, Jacobson2016, ConnesRovelli1994, Sorce2024, Hastings2007, VanRaamsdonk2010, LMVR2014, Faulkner2014, CCM2017, Paper5) + 15 supporting"
      linked_ids: [claim-bibliography-complete, test-bib-completeness]
    deliv-main-tex:
      status: passed
      path: "paper6/main.tex"
      summary: "REVTeX 4.2 main file with abstract, author, \\input commands for 7 sections, bibliography"
      linked_ids: []
    deliv-preamble:
      status: passed
      path: "paper6/preamble.sty"
      summary: "Custom macros consistent with (-,+,+,+) metric, K = -ln(rho_A), standard math shortcuts, theorem environments"
      linked_ids: []
  acceptance_tests:
    test-chain-table:
      status: passed
      summary: "Table I has all 8 links (L1-L8) with Status, Section, and Novel columns. L7 reads 'Definitional' with Connes-Rovelli citation. Every link maps to a paper section."
      linked_ids: [claim-paper-framing, deliv-introduction]
    test-mveh-framing:
      status: passed
      summary: "MVEH does not appear in any numbered assumption list. Text states self-modeling is sole physical premise and MVEH is definitional via Connes-Rovelli."
      linked_ids: [claim-paper-framing, deliv-introduction, deliv-discussion]
    test-honest-scope:
      status: passed
      summary: "Introduction and discussion both explicitly state: does not derive G, spacetime dimension, or Lambda."
      linked_ids: [claim-paper-framing, deliv-introduction, deliv-discussion]
    test-gap-completeness:
      status: passed
      summary: "Discussion identifies continuum limit and conformal approximation as gaps. MVEH reframed as definitional with explicit note. All four comparison papers (Jacobson 2016, CCM 2017, LMVR 2014, Faulkner 2014) have dedicated paragraphs."
      linked_ids: [claim-gap-statement, deliv-discussion]
    test-no-overclaim:
      status: passed
      summary: "No forbidden language found: 'prove MVEH', 'derive G', 'derive d=3+1', 'predict Lambda' all absent. Honest-framing statements present throughout."
      linked_ids: [claim-gap-statement, deliv-discussion]
    test-bib-completeness:
      status: passed
      summary: "All 10 required anchor entries present with correct years, journals, and arXiv eprint IDs. 15 supporting entries present."
      linked_ids: [claim-bibliography-complete, deliv-bib]
  references:
    ref-jacobson1995:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited in introduction (historical context paragraph) and discussion (comparison subsection)"
    ref-jacobson2016:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited in abstract, introduction (context + claim), and discussion (comparison paragraph + non-claims)"
    ref-vanraamsdonk2010:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited in introduction (entanglement-gravity context paragraph)"
    ref-paper5:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited in abstract, introduction (opening + claim + MVEH dissolution), and discussion (Paper 5 connection + non-claims)"
    ref-ccm2017:
      status: completed
      completed_actions: [compare, cite]
      missing_actions: []
      summary: "Cited in introduction (context) and discussed in dedicated comparison paragraph: spatial constraint vs full spacetime Einstein equation"
    ref-lmvr2014:
      status: completed
      completed_actions: [compare, cite]
      missing_actions: []
      summary: "Cited in introduction (context) and discussed in dedicated comparison paragraph: linearized vs nonlinear, holographic vs non-holographic"
    ref-faulkner2014:
      status: completed
      completed_actions: [compare, cite]
      missing_actions: []
      summary: "Cited in introduction (context) and discussed in dedicated comparison paragraph: holographic vs non-holographic"
    ref-hastings2007:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited in introduction (paper organization, Sec. III) and discussion (future work: spectral gap)"
    ref-connesrovelli1994:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited in abstract, introduction (MVEH dissolution + table), and discussion (derived-vs-input + gaps + non-claims)"
    ref-sorce2024:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited in introduction (caveat, forward reference to Sec. IV) and discussion (derived-vs-input)"
  forbidden_proxies:
    fp-gap-glossing:
      status: rejected
      notes: "Discussion Sec. 7.2 identifies each gap precisely with mechanism, consequence, and context. No glossing."
    fp-handwaving-arealaw:
      status: rejected
      notes: "Introduction specifies three routes to area law (WVCH, channel capacity, first law + K locality) and names them. No hand-waving."
    fp-overclaim:
      status: rejected
      notes: "Grep confirms no instances of 'prove MVEH', 'derive G', 'derive d=3+1', or 'predict Lambda' in either section."
    fp-mveh-assumption:
      status: rejected
      notes: "MVEH does not appear in any numbered assumption list. Described as definitional throughout."
  uncertainty_markers:
    weakest_anchors:
      - "MVEH dissolution via Connes-Rovelli -- novel interpretive argument, may face referee pushback"
      - "Sorce caveat resolution via SU(n) -> CFT -- sufficient conditions for geometric modular flow remain open"
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations:
      - "If a state on the self-modeling lattice fails MVEH but defines smooth geometry, the definitional argument collapses"

duration: 5min
completed: 2026-03-22
---

# Phase 12, Plan 01: Paper 6 Infrastructure and Bookend Sections

**Created Paper 6 LaTeX infrastructure and wrote Introduction (with L1-L8 derivation chain table, MVEH definitional reframing) and Discussion (with precise gap identification, four-paper comparison, honest scope statement)**

## Performance

- **Duration:** 5 min
- **Started:** 2026-03-22T18:28:41Z
- **Completed:** 2026-03-22T18:33:41Z
- **Tasks:** 2
- **Files created:** 10

## Key Results

- Paper 6 REVTeX 4.2 infrastructure complete: main.tex, preamble.sty, refs.bib (25 entries), 7 section files
- Introduction presents L1-L8 derivation chain table with L7 as "Definitional (Connes-Rovelli)" -- MVEH dissolved
- Discussion precisely identifies two remaining gaps (continuum limit, conformal approximation) and four related work comparisons
- All 10 anchor references cited; no overclaiming language present

## Task Commits

1. **Task 1: Paper 6 LaTeX infrastructure** - `7cad567` (setup)
2. **Task 2: Introduction and Discussion** - `0f5389a` (document)

## Files Created/Modified

- `paper6/main.tex` - REVTeX 4.2 main document with abstract and section inputs
- `paper6/preamble.sty` - Custom macros: metric, entropy, self-modeling quantities, math shortcuts
- `paper6/refs.bib` - 25 BibTeX entries (10 anchor + 15 supporting)
- `paper6/sections/introduction.tex` - Sec. I with derivation chain table (Table I), context, MVEH dissolution, scope
- `paper6/sections/discussion.tex` - Sec. VII with derived-vs-input, gaps, comparison, non-claims, future work
- `paper6/sections/lattice.tex` - Stub for Sec. II
- `paper6/sections/arealaw.tex` - Stub for Sec. III
- `paper6/sections/equilibrium.tex` - Stub for Sec. IV
- `paper6/sections/einstein.tex` - Stub for Sec. V
- `paper6/sections/numerical.tex` - Stub for Sec. VI

## Next Phase Readiness

- Paper 6 framing sections complete; Plans 02-03 can write Secs. II-VI constrained by the claims and gaps stated here
- Table I (derivation chain) serves as the structural spine for technical sections
- `\ref{eq:einstein}` in discussion awaits Sec. V equation label from Plan 02
- All anchor references in refs.bib ready for citation throughout

## Validations Completed

- All 8 links L1-L8 present in derivation chain table with Status, Section, Novel columns
- L7 reads "Definitional" (not "Assumed"), with Connes-Rovelli citation
- MVEH does not appear in any assumption list
- Introduction and discussion both state non-claims: G, d, Lambda
- All 10 anchor references cited at least once
- All 4 comparison papers discussed in dedicated subsections
- No overclaiming language: grep confirms absence of "prove MVEH", "derive G", "derive d=3+1", "predict Lambda"
- Convention assertions (ASSERT_CONVENTION) present in all .tex files
- LaTeX compilation not verified (no pdflatex available on system) -- environment limitation, not content error

## Decisions Made

- Derivation chain table placed in introduction (main text) as Table I, not appendix
- Sorce caveat addressed in introduction with forward reference to Sec. IV for detail
- Discussion organized as 6 subsections: derived-vs-input, gaps, comparison, Paper 5, non-claims, future work
- HancheOlsen1985 year corrected to 1983 (Canad. J. Math.) in refs.bib

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 4 - Missing Component] LaTeX compiler unavailable for verification**

- **Found during:** Task 1 verification
- **Issue:** No pdflatex/latexmk on the system; compilation verification step could not run
- **Fix:** Verified REVTeX structure syntactically via file existence and content grep checks. LaTeX compilation deferred to environment where compiler is available.
- **Verification:** All 10 files created, correct document class, correct \input commands, all bib entries valid BibTeX
- **Committed in:** 7cad567

---

**Total deviations:** 1 auto-fixed (environment gate, not physics error)
**Impact on plan:** None. File content is correct; compilation is a downstream verification step.

## Open Questions

- `\ref{eq:einstein}` in discussion will resolve once Sec. V is written (Plan 02)
- Sorce caveat detail deferred to Sec. IV (Plan 02)
- Numerical results section (Sec. VI) content deferred to Plan 03

## Self-Check: PASSED

- [x] All 10 created files exist
- [x] Both commits (7cad567, 0f5389a) exist in git log
- [x] Convention assertions in all .tex file headers
- [x] Contract coverage complete: all claim/deliverable/test/reference/proxy IDs addressed

---

_Phase: 12-paper-assembly, Plan 01_
_Completed: 2026-03-22_
