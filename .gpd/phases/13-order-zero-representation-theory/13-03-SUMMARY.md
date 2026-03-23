---
phase: 13-order-zero-representation-theory
plan: 03
depth: full
one-liner: "Bimodule decomposition H = 2 x C^{n^2} with Krajewski diagram; dimension counting resolved: per-sector n^2 = k^2 with k = n, giving k=4 (SM) at n=4"
subsystem: [derivation, formalism]
tags: [bimodule, krajewski-diagram, noncommutative-geometry, spectral-triple, representation-theory, standard-model]

requires:
  - phase: "13-01"
    provides: "pi(a) = diag(a tensor I, a tensor I), pi_o(b) = diag(I tensor b^T, I tensor b^T), order zero [pi(a), pi_o(b)] = 0"
  - phase: "13-02"
    provides: "Numerical verification at n=2,3,4; gamma = diag(P, -P); [gamma, pi(a)] = 0 failure; commutant dim = 4n^2"
provides:
  - "H = 2 copies of unique irreducible M_n(C)-M_n(C)^o bimodule C^{n^2}"
  - "Krajewski diagram: single vertex (n,n) with multiplicity 2, gamma decoration, J-connection"
  - "Barrett isomorphism: C^n tensor C^n = M_n(C) via v tensor w -> v w^T"
  - "Per-sector dimension n^2 = k^2 with k = n; n=4 gives k=4 (SM value)"
  - "Gamma-refined decomposition: Sym^2_p(+1) + wedge^2_p(-1) + wedge^2_{ap}(+1) + Sym^2_{ap}(-1)"
  - "Even condition failure does not invalidate bimodule decomposition"
affects: [14-dirac-operator, 15-first-order-condition, 16-spectral-action]

methods:
  added: [bimodule-decomposition, krajewski-diagram-construction, barrett-matrix-geometry]
  patterns: [per-sector-dimension-comparison, simple-algebra-unique-bimodule]

key-files:
  created: [derivations/07-bimodule-krajewski.md]

key-decisions:
  - "Per-sector n^2 = k^2 is the correct CCM comparison (not naive 2n^2 = k^2)"
  - "Barrett spinor space V = C^2 (two sectors: particle + antiparticle)"
  - "A_F identification deferred to Phase 15 (first-order condition)"

patterns-established:
  - "Simple algebra M_n(C) has unique irreducible bimodule C^{n^2}; multiplicity in H counts sectors"
  - "Krajewski diagram for simple algebra: single vertex, multiplicity = number of bimodule copies"
  - "Barrett isomorphism v tensor w -> v w^T converts tensor product to matrix multiplication"

conventions:
  - "[A,B] = AB - BA"
  - "inner product linear in second argument"
  - "pi_o(b) = J pi(b*) J^{-1}"
  - "gamma = diag(P, -P)"

plan_contract_ref: ".gpd/phases/13-order-zero-representation-theory/13-03-PLAN.md#/contract"
contract_results:
  claims:
    claim-bimodule-decomposition:
      status: passed
      summary: "H = C^{2n^2} decomposes as 2 copies of the unique irreducible M_n(C)-M_n(C)^o bimodule C^{n^2}, with left action a tensor I matching pi(a) and right action I tensor b^T matching pi_o(b)"
      linked_ids: [deliv-bimodule-derivation, test-bimodule-multiplicity, test-bimodule-actions, ref-van-suijlekom2024, ref-paper5, ref-paper6]
    claim-krajewski-diagram:
      status: passed
      summary: "Krajewski diagram has single vertex type (M_n(C) simple, one irrep C^n), multiplicity 2, gamma decoration distinguishing Sym^2/wedge^2 eigenspaces, J-connection swapping sectors; sigma_1 sigma_3 = -sigma_3 sigma_1 verified"
      linked_ids: [deliv-bimodule-derivation, test-krajewski-structure, ref-krajewski1997, ref-van-suijlekom2024, ref-paper6]
    claim-dimension-resolution:
      status: passed
      summary: "Per-sector dim = n^2 matches CCM k^2 with k = n; n=4 gives k=4 (SM value), dim(H) = 32 (SM per-generation); full comparison deferred to Phase 15 when A_F identified"
      linked_ids: [deliv-bimodule-derivation, test-dimension-mapping, ref-chamseddine-connes2008, ref-barrett2015]
  deliverables:
    deliv-bimodule-derivation:
      status: passed
      path: "derivations/07-bimodule-krajewski.md"
      summary: "Complete derivation with bimodule decomposition, gamma-refined 4-sector structure, Krajewski diagram, Barrett isomorphism, dimension counting resolution, and established-vs-deferred scope boundary"
      linked_ids: [claim-bimodule-decomposition, claim-krajewski-diagram, claim-dimension-resolution, test-bimodule-multiplicity, test-bimodule-actions, test-krajewski-structure, test-dimension-mapping]
  acceptance_tests:
    test-bimodule-multiplicity:
      status: passed
      summary: "H decomposes as exactly 2 copies of the unique irreducible bimodule C^{n^2}, proved by M_n(C) tensor M_n(C)^{op} = M_{n^2}(C) simplicity (unique irreducible module)"
      linked_ids: [claim-bimodule-decomposition, deliv-bimodule-derivation, ref-van-suijlekom2024]
    test-bimodule-actions:
      status: passed
      summary: "Left action a tensor I matches pi(a) from Plan 01; right action I tensor b^T matches pi_o(b) from Plan 01; verified under Barrett isomorphism as left/right matrix multiplication"
      linked_ids: [claim-bimodule-decomposition, deliv-bimodule-derivation]
    test-krajewski-structure:
      status: passed
      summary: "Single vertex type (simple algebra), multiplicity 2, gamma eigenvalue decoration (Sym^2/wedge^2 per sector), J-connection between sectors; multiplicity space acts as 2x2 with J = sigma_1, gamma = sigma_3 satisfying anticommutation"
      linked_ids: [claim-krajewski-diagram, deliv-bimodule-derivation, ref-krajewski1997]
    test-dimension-mapping:
      status: passed
      summary: "Per-sector n^2 = k^2 with k = n verified at n=1,2,3,4,5; n=4 gives k=4 (SM), dim(H) = 32; factor of 2 is J-doubling (particle+antiparticle); no naive 2n^2 = k^2 used"
      linked_ids: [claim-dimension-resolution, deliv-bimodule-derivation, ref-chamseddine-connes2008, ref-barrett2015]
  references:
    ref-van-suijlekom2024:
      status: completed
      completed_actions: [use, cite]
      missing_actions: []
      summary: "Bimodule decomposition method and Krajewski diagram formalism from Ch. 3-4 used throughout"
    ref-krajewski1997:
      status: completed
      completed_actions: [use, cite]
      missing_actions: []
      summary: "Krajewski diagram vertex/multiplicity/grading formalism applied to construct diagram for simple algebra"
    ref-chamseddine-connes2008:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "CCM k^2 classification compared with our per-sector n^2; correct mapping k = n identified; conditions (C1)-(C4) referenced"
    ref-barrett2015:
      status: completed
      completed_actions: [compare, cite]
      missing_actions: []
      summary: "Barrett matrix geometry H = V tensor M_n(C) matched with our V = C^2; isomorphism v tensor w -> v w^T explicitly verified"
    ref-paper5:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "M_n(C)^sa algebra cited as source of A = M_n(C)"
    ref-paper6:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "H = C^{2n^2}, J, gamma definitions cited as inputs to bimodule analysis"
  forbidden_proxies:
    fp-assumed-bimodule:
      status: rejected
      notes: "Bimodule decomposition explicitly connected to verified pi and pi_o from Plans 01-02; left action = a tensor I matches pi(a), right action = I tensor b^T matches pi_o(b)"
    fp-naive-dimension:
      status: rejected
      notes: "Per-sector comparison n^2 = k^2 used (giving k = n); naive 2n^2 = k^2 explicitly identified as incorrect comparison and explained why"
    fp-ko-dim-assumed:
      status: rejected
      notes: "KO-dim 6 signs J^2 = +1 and J gamma = -gamma J verified simultaneously in Plan 13-02 (pytest); gamma^2 = I also verified"
  uncertainty_markers:
    weakest_anchors:
      - "CCM dimension counting interpretation: per-sector n^2 = k^2 is the most natural mapping but the full CCM conditions (C1)-(C4) involve more than just dimension"
      - "Whether our factor of 2 (J-doubling) maps to the same structure as CCM's particle-antiparticle handling requires Phase 15 analysis"
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations: []

comparison_verdicts:
  - subject_id: claim-dimension-resolution
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-chamseddine-connes2008
    comparison_kind: benchmark
    metric: per_sector_dimension_match
    threshold: "n^2 = k^2 with k = n"
    verdict: pass
    recommended_action: "Proceed to Phase 14 (Dirac operator) and Phase 15 (first-order condition to identify A_F)"
    notes: "n=4 gives k=4 (SM value); dim(H) = 32 matches SM per-generation; full CCM conditions deferred to Phase 15"
  - subject_id: claim-bimodule-decomposition
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-van-suijlekom2024
    comparison_kind: benchmark
    metric: bimodule_multiplicity
    threshold: "multiplicity = 2"
    verdict: pass
    recommended_action: "Use bimodule structure to constrain Dirac operator in Phase 14"
    notes: "M_n(C) tensor M_n(C)^{op} = M_{n^2}(C) simple, unique irreducible module, H = 2 copies"

duration: 10min
completed: 2026-03-23
---

# Plan 13-03: Bimodule Decomposition and Krajewski Diagram Summary

**Bimodule decomposition H = 2 x C^{n^2} with Krajewski diagram; dimension counting resolved: per-sector n^2 = k^2 with k = n, giving k=4 (SM) at n=4**

## Performance

- **Duration:** 10 min
- **Started:** 2026-03-23T02:03:04Z
- **Completed:** 2026-03-23T02:13:00Z
- **Tasks:** 2
- **Files modified:** 1

## Key Results

- H = 2 copies of unique irreducible M_n(C)-M_n(C)^o bimodule C^{n^2}; left = a tensor I, right = I tensor b^T [CONFIDENCE: HIGH]
- Krajewski diagram: single vertex (n,n) with multiplicity 2, gamma = sigma_3 and J = sigma_1 on multiplicity space [CONFIDENCE: HIGH]
- Barrett isomorphism: C^n tensor C^n = M_n(C) via v tensor w -> v w^T; pi(a) = left multiplication, pi_o(b) = right multiplication [CONFIDENCE: HIGH]
- Per-sector n^2 = k^2 with k = n; n=4 gives k=4 (SM value), dim(H) = 32 [CONFIDENCE: HIGH]
- Gamma-refined decomposition: Sym^2_p(+1) + wedge^2_p(-1) + wedge^2_{ap}(+1) + Sym^2_{ap}(-1), dim = 2n^2 [CONFIDENCE: HIGH]
- Even condition failure does NOT invalidate bimodule decomposition (bimodule structure independent of gamma compatibility) [CONFIDENCE: HIGH]

## Task Commits

1. **Task 1: Bimodule decomposition and Krajewski diagram** - `12f6c72` (derive)
2. **Task 2: Resolve dimension counting 2n^2 vs CCM k^2** - `5bb912a` (derive)

## Files Created/Modified

- `derivations/07-bimodule-krajewski.md` - Complete bimodule decomposition, Krajewski diagram, Barrett isomorphism, and dimension counting resolution

## Next Phase Readiness

- Bimodule structure H = 2 x C^{n^2} ready for Phase 14 (Dirac operator construction): D maps between bimodule summands, first-order condition constrains D to be an intertwiner
- n = 4 identified as SM candidate: per-sector k = 4 matches CCM classification
- Open: even condition failure must be resolved (different gamma, different action, or odd spectral triple) before Phase 14 can construct a fully consistent even spectral triple
- Phase 15 required: first-order condition to identify A_F as subalgebra of M_n(C) and verify A_F = C + H + M_3(C) at n = 4

## Contract Coverage

- Claim IDs advanced: claim-bimodule-decomposition -> passed, claim-krajewski-diagram -> passed, claim-dimension-resolution -> passed
- Deliverable IDs produced: deliv-bimodule-derivation -> derivations/07-bimodule-krajewski.md (passed)
- Acceptance test IDs run: test-bimodule-multiplicity -> passed, test-bimodule-actions -> passed, test-krajewski-structure -> passed, test-dimension-mapping -> passed
- Reference IDs surfaced: ref-van-suijlekom2024 -> use+cite, ref-krajewski1997 -> use+cite, ref-chamseddine-connes2008 -> read+compare+cite, ref-barrett2015 -> compare+cite, ref-paper5 -> cite, ref-paper6 -> cite
- Forbidden proxies rejected: fp-assumed-bimodule -> rejected, fp-naive-dimension -> rejected, fp-ko-dim-assumed -> rejected
- Decisive comparison verdicts: claim-dimension-resolution -> pass (n^2 = k^2, k=n), claim-bimodule-decomposition -> pass (multiplicity 2)

## Equations Derived

**Eq. (13-03.1) -- Bimodule decomposition:**

$$H = C^{n^2}_p \oplus C^{n^2}_{ap} = 2 \times (C^n \otimes (C^n)^*)$$

as M_n(C)-M_n(C)^o bimodules. Multiplicity m = 2.

**Eq. (13-03.2) -- Gamma-refined decomposition:**

$$H = \text{Sym}^2_p(+1) \oplus \wedge^2_p(-1) \oplus \wedge^2_{ap}(+1) \oplus \text{Sym}^2_{ap}(-1)$$

Dimensions: n(n+1)/2 + n(n-1)/2 + n(n-1)/2 + n(n+1)/2 = 2n^2.

**Eq. (13-03.3) -- Barrett isomorphism:**

$$C^n \otimes C^n \xrightarrow{\sim} M_n(\mathbb{C}), \quad v \otimes w \mapsto v \cdot w^T$$

Under this map: pi(a) = left multiplication X -> aX, pi_o(b) = right multiplication X -> Xb.

**Eq. (13-03.4) -- Per-sector dimension counting:**

$$n^2 = k^2 \quad \Rightarrow \quad k = n, \quad n = 4 \Rightarrow k = 4 \text{ (SM)}$$

## Validations Completed

- Total dimension 2n^2 verified for n = 1,2,3,4,5
- Gamma eigenspace dimensions n^2 + n^2 = 2n^2 (equal split)
- Left/right bimodule actions match verified pi and pi_o from Plans 01-02
- Barrett isomorphism consistency: left/right multiplication under v tensor w -> v w^T
- Krajewski diagram: single vertex for simple algebra, multiplicity 2
- J, gamma on multiplicity space: sigma_1, sigma_3 anticommute
- Per-sector n^2 = k^2 with k = n at all tested values
- n = 4 gives dim(H) = 32 = SM per-generation dimension

## Decisions & Deviations

**Decisions:**
- Per-sector n^2 (not total 2n^2) is the correct comparand for CCM k^2, because the factor of 2 is J-doubling
- Barrett spinor space V = C^2 (two sectors), matching the simplest non-trivial matrix geometry
- A_F identification deferred to Phase 15 (no premature SM claims)

**Deviations:** None -- plan executed exactly as written.

## Open Questions

- Does the first-order condition (Phase 15) produce A_F = C + H + M_3(C) as a subalgebra of M_4(C)?
- How is the even condition failure resolved? Three paths identified in Plan 13-02: different algebra action, different gamma, or odd spectral triple
- Does the bimodule refinement under A_F match the full CCM counting (not just dimension but structure)?

## Self-Check: PASSED

- [x] derivations/07-bimodule-krajewski.md exists
- [x] Commit 12f6c72 exists (Task 1)
- [x] Commit 5bb912a exists (Task 2)
- [x] Bimodule decomposition computed at general n with multiplicity 2
- [x] Krajewski diagram drawn with gamma decoration and J-connections
- [x] 2n^2 vs k^2 dimension counting resolved (per-sector k = n)
- [x] Even condition failure implications documented
- [x] Barrett isomorphism identified and verified
- [x] All forbidden proxies rejected
- [x] All acceptance tests passed
- [x] All references surfaced
- [x] No premature SM claims (A_F deferred to Phase 15)

---

_Phase: 13-order-zero-representation-theory_
_Plan: 03_
_Completed: 2026-03-23_
