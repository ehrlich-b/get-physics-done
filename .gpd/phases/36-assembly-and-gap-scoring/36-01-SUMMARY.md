---
phase: 36-assembly-and-gap-scoring
plan: 01
depth: full
one-liner: "Assembled six-link derivation chain (finite-dim observer to Einstein equations) with equation-level citations from Phases 32-35, J1-J8 Jacobson input mapping, dimension-dependent assessment, and cumulative assumption register"
subsystem: [derivation, analysis]
tags: [derivation-chain, entanglement-equilibrium, jacobson, einstein-equations, fisher-geometry, sigma-model, bisognano-wichmann]

requires:
  - phase: 32-fisher-geometry-on-reduced-states
    provides: FISH-01 (smoothness Eq. 32.8), FISH-02 (positive-def), FISH-03 (1D failure Eq. 32.12)
  - phase: 33-correlation-structure-and-effective-theory
    provides: CORR-01 (decay Eq. 33.1), CORR-02 (sigma model Eq. 33.11), CORR-03 (conditional smoothness Eq. 33.19)
  - phase: 34-emergent-lorentz-invariance
    provides: LRNZ-01/02 (isotropy, Lorentz Eq. 34.16), velocity hierarchy (c_s=1.659Ja), metric assembly (Eq. 34.9)
  - phase: 35-bw-theorem-and-local-equilibrium
    provides: BWEQ-01 (lattice-BW Eq. 35.1), BWEQ-02 (KMS, J1-J3), theta=sigma=0 (Eqs. 35.19/35.21)
provides:
  - Complete six-link derivation chain document (derivations/36-derivation-chain.md)
  - Jacobson input mapping J1-J8 with status at each input
  - Dimension comparison table (d=1/d=2/d>=3)
  - Cumulative assumption register (6 categories)
  - Cumulative chain status by dimension
affects: [36-02-gap-scoring, paper-revision]

methods:
  added: [derivation-chain-assembly, rigor-classification-taxonomy]
  patterns: [cite-by-equation-number, dimension-dependent-assessment]

key-files:
  created: [derivations/36-derivation-chain.md]

key-decisions:
  - "Integrated J1-J8 table, dimension table, and assumption register into chain document (not separate files)"
  - "Used four-level rigor taxonomy: RIGOROUS / CONDITIONAL / PHYSICAL ARGUMENT / ASSUMED"
  - "MVEH classified as 'structural identification' not 'proof' (honest framing)"
  - "Route A vs Route B presented as complementary (not competing)"

patterns-established:
  - "cite-by-equation: Every physics claim cites (derivation file, equation number) pair"
  - "dimension-columns: Assessment tables always split d=1 / d=2 / d>=3"
  - "rigor-taxonomy: {RIGOROUS, CONDITIONAL, PHYSICAL ARGUMENT, ASSUMED} for every link"

conventions:
  - "hbar = 1, k_B = 1, a = 1 (natural units)"
  - "Metric: (-,+,...,+) Lorentzian for emergent spacetime; (+,...,+) Riemannian for Fisher spatial"
  - "Fisher metric: SLD, g_F = 4 g_Bures, SPATIAL ONLY"
  - "Emergent speed: c = c_s = 1.659 Ja (NOT v_LR)"
  - "Coupling: J > 0 antiferromagnetic"

plan_contract_ref: ".gpd/phases/36-assembly-and-gap-scoring/36-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-chain-complete:
      status: passed
      summary: "Six-link derivation chain assembled with equation-level citations from Phases 32-35, rigor classification at each link, no re-derivations"
      linked_ids: [deliv-chain-doc, test-six-links, test-rigor-classification, test-no-rederivation, test-convention-consistency]
    claim-jacobson-inputs:
      status: passed
      summary: "All 8 Jacobson inputs (J1-J8) mapped to chain sources with status; Route A and Route B distinguished"
      linked_ids: [deliv-chain-doc, test-jacobson-mapping, test-route-ab]
    claim-dimension-dependent:
      status: passed
      summary: "Dimension comparison table covers all 6 links at d=1/d=2/d>=3; d=1 failure and trivial Einstein honestly stated"
      linked_ids: [deliv-chain-doc, test-dimension-columns]
  deliverables:
    deliv-chain-doc:
      status: passed
      path: "derivations/36-derivation-chain.md"
      summary: "Self-contained derivation chain document with all required sections: ASSERT_CONVENTION, link status table, six links (a)-(f), J1-J8 mapping, dimension table, assumption register, cumulative status, verification summary"
      linked_ids: [claim-chain-complete, claim-jacobson-inputs, claim-dimension-dependent]
  acceptance_tests:
    test-six-links:
      status: passed
      summary: "All six links (a)-(f) present with explicit sections; each cites specific equations from Phases 32-35 or Papers 5-6"
      linked_ids: [claim-chain-complete, deliv-chain-doc]
    test-rigor-classification:
      status: passed
      summary: "Every link classified using {RIGOROUS, CONDITIONAL, PHYSICAL ARGUMENT, ASSUMED}; no overclaiming"
      linked_ids: [claim-chain-complete, deliv-chain-doc]
    test-no-rederivation:
      status: passed
      summary: "Zero new derivations; every result cited by (Phase, Equation) pair; no tag{36.x} equations"
      linked_ids: [claim-chain-complete, deliv-chain-doc]
    test-convention-consistency:
      status: passed
      summary: "Natural units, SLD Fisher, J>0 AFM, c=c_s throughout; Fisher always qualified as spatial/Riemannian; Lorentzian only for full spacetime"
      linked_ids: [claim-chain-complete, deliv-chain-doc]
    test-jacobson-mapping:
      status: passed
      summary: "J1-J8 all mapped with source equation and status; J7 RIGOROUS, J6/J8 ASSUMED, rest CONDITIONAL or RIGOROUS-once-BW-accepted"
      linked_ids: [claim-jacobson-inputs, deliv-chain-doc]
    test-route-ab:
      status: passed
      summary: "Route A (requires Gap B conformal) and Route B (requires Gap C tensoriality) clearly distinguished with complementarity table"
      linked_ids: [claim-jacobson-inputs, deliv-chain-doc]
    test-dimension-columns:
      status: passed
      summary: "d=1: FISH-03 failure + G_ab=0 trivially; d=2: log corrections + Neel QMC only; d>=3: Goldstone convergent + Neel rigorous (S>=1)"
      linked_ids: [claim-dimension-dependent, deliv-chain-doc]
  references:
    ref-paper5:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited as chain origin Link (a): finite-dimensional observer, C*-algebraic setting"
    ref-paper6:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited for SWAP lattice (Link b), area law (Links L1-L5), gap definitions, Route A/B structure"
    ref-jacobson2016:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited as framework for Link (f); entanglement equilibrium (NOT Jacobson 1995 Clausius approach)"
    ref-phase32:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "FISH-01 Eq. 32.8, FISH-02 Theorem 2, FISH-03 Eq. 32.12 all cited in Link (c)"
    ref-phase33:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "CORR-01 Eq. 33.1, CORR-02 Eqs. 33.11/33.14, CORR-03 Eqs. 33.18/33.19 all cited in Link (c)"
    ref-phase34:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "LRNZ-01 Eqs. 34.6-34.9, LRNZ-02 Eqs. 34.15/34.16/34.30, velocity hierarchy Eqs. 34.2-34.8, metric Eqs. 34.9-34.11 cited in Link (d)"
    ref-phase35:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "BWEQ-01 Eq. 35.1, BWEQ-02 Eqs. 35.0a/35.3/35.9/35.19/35.21 cited in Link (e); J1-J3 mapped"
    ref-lovelock:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Lovelock uniqueness theorem cited for Route B in Link (f)"
    ref-chm2011:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Casini-Huerta-Myers conformal modular Hamiltonian cited for Route A in Link (f)"
  forbidden_proxies:
    fp-rederivation:
      status: rejected
      notes: "Zero new derivations; all results cited by equation number"
    fp-universal-claim:
      status: rejected
      notes: "Dimension comparison table and cumulative status always specify d=1/d=2/d>=3 separately"
    fp-constructive-continuum:
      status: rejected
      notes: "Explicitly stated: 'effective smoothness at finite N, NOT constructive limit' in J4 and assumption register"
    fp-jacobson1995:
      status: rejected
      notes: "Jacobson 2016 framework used throughout; 1995 cited only for conceptual lineage in RESEARCH.md"
  uncertainty_markers:
    weakest_anchors:
      - "Sigma model description of SWAP lattice continuum limit (physical universality argument, not proved)"
      - "Lattice-BW entanglement Hamiltonian (numerical SRF=0.9993, not theorem)"
      - "Neel order for S=1/2 d=2 (QMC evidence only, not rigorous)"
    unvalidated_assumptions:
      - "MVEH (structural identification, not proof)"
      - "Tensoriality J8 (Route B, assumed)"
      - "Wilsonian regime J6 (assumed)"
    competing_explanations: []
    disconfirming_observations:
      - "FISH-03 1D failure is a genuine negative result that blocks d=1 route"

duration: 7min
completed: 2026-03-30
---

# Phase 36, Plan 01: Chain Assembly Summary

**Assembled six-link derivation chain from finite-dimensional observer to Einstein equations with equation-level citations, J1-J8 Jacobson mapping, dimension-dependent assessment, and cumulative assumption register**

## Performance

- **Duration:** 7 min
- **Started:** 2026-03-30T14:36:50Z
- **Completed:** 2026-03-30T14:43:02Z
- **Tasks:** 2
- **Files modified:** 1

## Key Results

- Six-link chain assembled: (a) finite-dim observer -> (b) SWAP lattice -> (c) Fisher manifold -> (d) emergent Lorentz -> (e) BW + equilibrium -> (f) Jacobson -> Einstein. Every link cites specific equations from Phases 32-35.
- Chain status by dimension: d>=3 CONDITIONAL (each link at least PHYSICAL ARGUMENT); d=2 CONDITIONAL with caveats (Neel QMC only, log corrections); d=1 FAILS (FISH-03 collapses Fisher geometry, Einstein tensor vanishes)
- J1-J8 Jacobson inputs fully mapped: J1 (Eq. 35.0a, CONDITIONAL), J2 (Eqs. 35.19/35.21, RIGOROUS), J3 (Eq. 35.3, RIGOROUS once BW accepted), J4 (CONDITIONAL), J5 (CONDITIONAL), J6 (ASSUMED), J7 (RIGOROUS), J8 (ASSUMED, Route B only)
- Route A (conformal, Gap B required) vs Route B (Lovelock, Gap C required) clearly distinguished as complementary

## Task Commits

1. **Task 1: Assemble six-link chain with equation-level citations** - `87a7967` (derive)
2. **Task 2: Verify J1-J8 mapping, dimension table, assumption register** - `6570f81` (validate)

## Files Created/Modified

- `derivations/36-derivation-chain.md` -- Self-contained derivation chain document (490 lines)

## Next Phase Readiness

- Chain document ready for Plan 02 (gap scoring): gap scorecards can cite the chain's rigor classifications and dimension table
- J1-J8 mapping provides the input status for Jacobson argument assessment
- Assumption register provides the basis for honest gap scoring

## Equations Derived

No new equations derived (assembly plan). All equations cited from Phases 32-35 by number.

## Validations Completed

- All six links (a)-(f) present with equation-level citations
- Rigor classification at every link (no overclaiming)
- Zero re-derivations (all cite prior derivation files)
- Convention consistency verified: c=c_s, Fisher=spatial only, natural units, Jacobson 2016 framework
- FISH-03 failure honestly stated in dimension table and cumulative status
- Route A/B complementarity noted

## Decisions & Deviations

### Deviation

**[Rule 4 - Missing Component] Integrated Task 2 content into Task 1 deliverable**

- **Found during:** Task 1 (chain assembly)
- **Issue:** The plan separated "chain assembly" (Task 1) from "J1-J8 table, dimension table, assumption register" (Task 2), but the logical structure of the chain document required all sections to be written together for coherence
- **Fix:** Integrated all sections into a single document during Task 1; Task 2 became a verification pass confirming completeness
- **Impact:** No scope creep; all acceptance tests pass; both tasks committed individually

## Open Questions

- Does the sigma model universality argument for the SWAP lattice have a tighter justification than "standard universality class"?
- Can the lattice-BW SRF = 0.9993 be improved to a theorem (even a conditional one)?
- Is there a route to rigorous Neel order for S=1/2, d=2 that would upgrade CORR-03?

---

_Phase: 36-assembly-and-gap-scoring, Plan 01_
_Completed: 2026-03-30_
