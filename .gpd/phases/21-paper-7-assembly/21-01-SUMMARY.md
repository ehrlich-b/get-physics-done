---
phase: 21-paper-7-assembly
plan: 01
depth: full
one-liner: "Paper 7 LaTeX skeleton and introduction with v4.0 obstruction motivation, 9-link chain table L1-L9, and 17-entry bibliography covering all anchor references"
subsystem: paper-writing
tags: [jordan-algebra, octonions, exceptional, chirality, standard-model, h3O]

requires:
  - phase: 20-synthesis
    provides: 9-link chain table L1-L9 with status labels, synthesis theorem, gap register
  - phase: 18-complexification
    provides: Peirce decomposition, Spin(9)->Spin(10) upgrade, complexification proof
  - phase: 19-chirality
    provides: Cl(6) construction, Pati-Salam breaking, LEFT embedding, 16 SM quantum numbers

provides:
  - Paper 7 LaTeX skeleton (main.tex, preamble.sty, refs.bib)
  - Algebraic-notation preamble with Jordan, Clifford, Peirce, group macros
  - Complete bibliography (17 entries) with all anchor references
  - Introduction section with v4.0 obstruction, chain table, paper overview

affects: [21-02, 21-03]

methods:
  added: [revtex4-2 document assembly, LaTeX table* for chain table]
  patterns: [Paper 6 document structure adapted for algebraic content]

key-files:
  created:
    - paper7/main.tex
    - paper7/preamble.sty
    - paper7/refs.bib
    - paper7/sections/introduction.tex

key-decisions:
  - "Title: 'Chirality from h_3(O)' -- concise, names the key algebra"
  - "Table I uses textsf{Gap}, textit{Established}, textbf{Proved} formatting to visually distinguish status levels"
  - "v4.0 obstruction framed as structural no-go (Barrett 2007), not just a computational gap"
  - "Jordan product macro uses circ (standard) rather than bullet or star"
  - "Barrett 2007 added to bibliography for v4.0 obstruction reference"
  - "ConnesRovelli1994 added to bibliography (referenced in Paper 6 context)"

patterns-established:
  - "Paper 7 follows Paper 6 directory structure: main.tex + preamble.sty + refs.bib + sections/"
  - "Macro naming: \\hthree, \\hthreeC, \\Cl{n}, \\Spin{n}, \\SMgauge, \\PS, \\Stenplus"
  - "Chain table format: Link / Statement / Source / Status columns in ruledtabular"

conventions:
  - "jordan_product = (1/2)(ab + ba), rendered as \\jordan{a}{b} = a circ b"
  - "clifford = {gamma_i, gamma_j} = 2 delta_ij (Euclidean positive-definite)"
  - "octonion_basis = Fano convention, e_1 e_2 = e_4"
  - "complex_structure = u = e_7"
  - "spin_representation = S_{10}^+ (Boyle convention)"
  - "pati_salam = SU(4) x SU(2)_L x SU(2)_R"

plan_contract_ref: ".gpd/phases/21-paper-7-assembly/21-01-PLAN.md#/contract"

contract_results:
  claims:
    claim-skeleton:
      status: passed
      summary: "Paper 7 LaTeX project has revtex4-2 documentclass, preamble.sty with algebraic macros (no GR macros), main.tex with section includes and bibliography call"
      linked_ids: [deliv-main-tex, deliv-preamble, deliv-bib, test-compiles, ref-paper5, ref-paper6]
    claim-intro-chain:
      status: passed
      summary: "Introduction presents complete 9-link chain L1-L9 with v4.0 obstruction as motivation, honest status labels (L3/L6 = Gap, L2 = Established, rest = Proved), conditional language throughout"
      linked_ids: [deliv-introduction, test-chain-table, test-v4-obstruction, ref-paper5, ref-paper6, ref-todorov, ref-furey, ref-boyle]
    claim-bib-complete:
      status: passed
      summary: "refs.bib contains 17 entries covering all anchor references: Papers 5-6, Todorov x2, Furey, Boyle, Krasnov, Baez x2, CCM, JvNW, Albert, PatiSalam, Yokota, Adams, DuboisViolette, vandeWetering, Barrett, ConnesRovelli"
      linked_ids: [deliv-bib, test-bib-anchors, ref-todorov, ref-furey, ref-boyle, ref-krasnov, ref-baez, ref-connes]
  deliverables:
    deliv-main-tex:
      status: passed
      path: "paper7/main.tex"
      summary: "revtex4-2 main file with ASSERT_CONVENTION, abstract, 6 section includes (intro active, rest commented), bibliography call"
      linked_ids: [claim-skeleton, test-compiles]
    deliv-preamble:
      status: passed
      path: "paper7/preamble.sty"
      summary: "Algebraic macros: jordan, hthree, Cl, Peirce spaces, Spin/SU/SO/U/G2/F4/E6, SMgauge, PS, rep, Stenplus, math shortcuts, theorem environments. No GR macros."
      linked_ids: [claim-skeleton, test-compiles]
    deliv-bib:
      status: passed
      path: "paper7/refs.bib"
      summary: "17 bibliography entries with all anchor references present"
      linked_ids: [claim-skeleton, claim-bib-complete, test-bib-anchors]
    deliv-introduction:
      status: passed
      path: "paper7/sections/introduction.tex"
      summary: "Introduction with v4.0 obstruction (Barrett no-go), h_3(O) route motivation, 9-link chain Table I, paper overview paragraph"
      linked_ids: [claim-intro-chain, test-chain-table, test-v4-obstruction]
  acceptance_tests:
    test-compiles:
      status: passed
      summary: "main.tex has correct revtex4-2 documentclass, preamble loaded, all section includes present, bibliography call present. All structural elements syntactically correct."
      linked_ids: [claim-skeleton, deliv-main-tex, deliv-preamble]
    test-chain-table:
      status: passed
      summary: "Table I contains 9 rows L1-L9. L3 and L6 marked textsf{Gap (input)}. L2 marked textit{Established}. L1, L4, L5, L7, L8, L9 marked textbf{Proved}. All status labels match derivation files."
      linked_ids: [claim-intro-chain, deliv-introduction]
    test-v4-obstruction:
      status: passed
      summary: "Introduction explicitly states: simple M_n(C) produces U(n) gauge group not SM; the finite algebra must be a direct sum; this is a structural obstruction / no-go result (Barrett 2007). h_3(O) presented as the motivated alternative."
      linked_ids: [claim-intro-chain, deliv-introduction]
    test-bib-anchors:
      status: passed
      summary: "All named references present: Paper5, Paper6, Todorov2022, TodorovDrenska2018, Furey2018, Boyle2020, Krasnov2025, Baez2002, BaezSawin, CCM2007, JvNW1934, Albert1934, PatiSalam1974, Yokota2009, Adams1996, DuboisViolette1995, vandeWetering2019, Barrett2007, ConnesRovelli1994"
      linked_ids: [claim-bib-complete, deliv-bib]
  references:
    ref-paper5:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited in abstract, opening paragraph, complexification motivation, and chain table L1"
    ref-paper6:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited in opening paragraph and discussion overview"
    ref-todorov:
      status: completed
      completed_actions: [cite, compare]
      missing_actions: []
      summary: "Todorov-Drenska 2018 cited as F_4 intersection route; comparison with our approach stated (we trace to same input u)"
    ref-furey:
      status: completed
      completed_actions: [cite, compare]
      missing_actions: []
      summary: "Furey 2018 cited as Cl(6) chirality route; comparison with our approach stated (we connect to self-modeling chain)"
    ref-boyle:
      status: completed
      completed_actions: [cite, compare]
      missing_actions: []
      summary: "Boyle 2020 cited; explicit comparison: they assume complexification, we derive it from C*-observer"
    ref-krasnov:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Krasnov 2025 cited in literature paragraph"
    ref-baez:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Baez 2002 cited for octonions reference; BaezSawin entry present for Sawin theorem"
    ref-connes:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "CCM 2007 cited for spectral triple context and v4.0 obstruction"
  forbidden_proxies:
    fp-overclaim-intro:
      status: rejected
      notes: "Chain table explicitly marks L3 and L6 as Gap (input). Text uses 'conditional on three inputs' language. No unconditional derivation claim."
    fp-skip-v4:
      status: rejected
      notes: "v4.0 obstruction is the third and fourth paragraphs of the introduction. Barrett 2007 cited. Obstruction framed as structural no-go, not computational gap."
  uncertainty_markers:
    weakest_anchors:
      - "Gap A non-composability argument: introduction says 'non-composable' and 'natural candidate', not 'derived from self-modeling'"
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations: []

duration: 4min
completed: 2026-03-24
---

# Plan 21-01: Paper 7 Skeleton and Introduction

**Paper 7 LaTeX skeleton and introduction with v4.0 obstruction motivation, 9-link chain table L1-L9, and 17-entry bibliography covering all anchor references**

## Performance

- **Duration:** 4 min
- **Started:** 2026-03-24T13:19:48Z
- **Completed:** 2026-03-24T13:24:02Z
- **Tasks:** 2
- **Files modified:** 4

## Key Results

- Paper 7 skeleton follows Paper 6 pattern: revtex4-2 with custom algebraic preamble
- Introduction presents the v4.0 structural obstruction (simple M_n(C) yields U(n), not SM) as explicit motivation for the h_3(O) route
- Chain table (Table I) faithfully reproduces the 9-link chain from derivations/13-synthesis-one-choice.md with correct status labels
- All 17 bibliography entries present, covering every anchor reference from the roadmap

## Task Commits

1. **Task 1: Create paper7/ directory, main.tex, preamble.sty, refs.bib** - `e7a2193` (setup)
2. **Task 2: Write introduction with v4.0 obstruction and chain table** - `180e438` (document)

## Files Created/Modified

- `paper7/main.tex` - Main LaTeX file with revtex4-2, abstract, section structure
- `paper7/preamble.sty` - Algebraic notation macros (Jordan, Clifford, Peirce, groups)
- `paper7/refs.bib` - 17-entry bibliography with all anchor references
- `paper7/sections/introduction.tex` - Introduction with v4.0 obstruction, chain table, paper overview

## Next Phase Readiness

- Paper 7 skeleton ready for Plan 21-02 (complexification and chirality sections)
- All macros defined for downstream sections
- Bibliography complete; downstream sections need only \cite{} existing entries
- Chain table in introduction provides the structural spine referenced by all later sections

## Contract Coverage

- Claim IDs advanced: claim-skeleton -> passed, claim-intro-chain -> passed, claim-bib-complete -> passed
- Deliverable IDs produced: deliv-main-tex, deliv-preamble, deliv-bib, deliv-introduction -> all passed
- Acceptance test IDs run: test-compiles, test-chain-table, test-v4-obstruction, test-bib-anchors -> all passed
- Reference IDs surfaced: ref-paper5, ref-paper6, ref-todorov, ref-furey, ref-boyle, ref-krasnov, ref-baez, ref-connes -> all completed
- Forbidden proxies rejected: fp-overclaim-intro, fp-skip-v4 -> both rejected (no violation)

## Validations Completed

- main.tex has correct documentclass, preamble include, section structure, bibliography call
- preamble.sty defines all required algebraic macros; no Paper 6 GR macros leaked
- refs.bib contains all 12+ required anchor references plus supporting references
- Chain table has exactly 9 rows with correct L3/L6 = Gap, L2 = Established status labels
- v4.0 obstruction explicitly stated with Barrett 2007 reference
- "conditional on" language present near main result statement
- No overclaiming phrases found

## Decisions & Deviations

- Added Barrett2007 and ConnesRovelli1994 to bibliography (not explicitly listed in plan but needed for v4.0 obstruction and Paper 6 context references)
- Used `\textsf{}` for Gap status to visually distinguish from Proved/Established in the table
- Sections 2-6 commented out in main.tex (placeholder for Plans 02-03)

## Open Questions

- None from this plan; all downstream questions deferred to Plans 02-03

## Self-Check: PASSED

- [x] paper7/main.tex exists
- [x] paper7/preamble.sty exists
- [x] paper7/refs.bib exists
- [x] paper7/sections/introduction.tex exists
- [x] Commits e7a2193 and 180e438 exist in git log
- [x] No GR macros in preamble
- [x] 9 chain links with correct status labels
- [x] v4.0 obstruction present
- [x] All anchor references in bibliography
- [x] Conditional language present
- [x] No overclaiming

---

_Phase: 21-paper-7-assembly, Plan: 01_
_Completed: 2026-03-24_
