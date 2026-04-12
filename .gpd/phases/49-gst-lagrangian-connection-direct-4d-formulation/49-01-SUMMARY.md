---
phase: 49-gst-lagrangian-connection-direct-4d-formulation
plan: 01
depth: full
one-liner: "Identified 4d N=2 MESGT field content (1 gravity + 26 vector multiplets, 54 real scalars on E_{7(-25)}/(E_6(-78) x U(1))) and constructed prepotential F(X) = d_{IJK} X^I X^J X^K / (6 X^0) with normalization C_{IJK} = (1/6) d_{IJK}"
subsystem: [formalism, derivation]
tags: [supergravity, MESGT, special-kahler, prepotential, jordan-algebra, octonion, E7, E6, peirce-decomposition, field-content]

requires:
  - phase: 47-d-ijk-tensor-and-uniqueness-theorems
    provides: d_{IJK} tensor (106 nonzero entries), peirce_basis_27, det_3, two-block structure, uniqueness theorem, quantum_number_table_27
  - phase: 46-v-0-algebraic-foundation-and-pi-u-projection
    provides: pi_u, det_2 Gram = diag(+1,-1,-1,-1), V_0 = 4+6 split, h_2(C_u) Minkowski metric
  - phase: 48-lorentz-equivariance
    provides: so(3) x so(6) stabilizer, pi_u equivariance
provides:
  - 4d N=2 MESGT field content table (1 gravity + 26 vector multiplets)
  - Cubic prepotential F(X) = d_{IJK} X^I X^J X^K / (6 X^0)
  - Normalization C_{IJK} = (1/6) d_{IJK}
  - Peirce coordinate extraction (peirce_coords function)
  - field_content_table_49 function
  - prepotential_F function
  - Scalar manifold identification E_{7(-25)}/(E_6(-78) x U(1)), dim = 54
affects: [49-02-couplings-and-lagrangian, 50-paper-assembly]

methods:
  added: [Peirce-to-field-content identification, cubic prepotential construction, special Kahler formulation]
  patterns: [Peirce coordinate extraction via trace inner product, multiplicity-weighted d_{IJK} contraction]

key-files:
  modified: [code/octonion_algebra.py, derivations/49-field-content-and-prepotential.tex]

key-decisions:
  - "Direct 4d formulation via special Kahler geometry -- NO 5d or KK reduction"
  - "Normalization: C_{IJK} = (1/6) d_{IJK} from d(X,X,X) = 6 N(X) convention"
  - "Peirce coordinate extraction via orthogonal decomposition: X^I = tr(X o e_I) / tr(e_I o e_I)"

patterns-established:
  - "Prepotential: F(X) = d_{IJK} X^I X^J X^K / (6 X^0)"
  - "GST coupling: C_{IJK} = (1/6) d_{IJK}"
  - "Field count: 1 gravity + 26 vector = 27 vectors, 54 real scalars"
  - "Scalar manifold: E_{7(-25)}/(E_6(-78) x U(1)), dim = 133 - 78 - 1 = 54"

conventions:
  - "u = e_7 (complex structure)"
  - "jordan_product = (1/2)(AB + BA)"
  - "det_3 association: left-to-right Re((x1*x2)*x3)"
  - "Fano: e_1 e_2 = e_4"
  - "Peirce idempotent: E_{11}"
  - "Real forms: E_6(-26) (5d structure), E_7(-25) (4d U-duality)"
  - "Prepotential normalization: F(X) = d_{IJK} X^I X^J X^K / (6 X^0)"
  - "Peirce basis ordering: I=0 (V_1), I=1..16 (V_{1/2}), I=17..26 (V_0)"
  - "Metric signature: (+,-,-,-) from Phase 46 det_2 Gram"

plan_contract_ref: ".gpd/phases/49-gst-lagrangian-connection-direct-4d-formulation/49-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-field-content:
      status: passed
      summary: "27 = 1 (gravity, graviphoton) + 16 (V_{1/2} vector multiplets, SM fermion q.n.) + 10 (V_0 vector multiplets, 4 spacetime + 6 internal). n_V = 26, total vectors = 27, real scalars = 54 = dim E_{7(-25)}/(E_6(-78) x U(1))."
      linked_ids: [deliv-derivation, deliv-code, test-field-count, test-manifold-dim, ref-gst-1984, ref-dewit-vanproeyen]
      evidence:
        - verifier: gpd-executor
          method: field_content_table_49 function with dimension arithmetic
          confidence: high
          claim_id: claim-field-content
          deliverable_id: deliv-code
          acceptance_test_id: test-field-count
          reference_id: ref-gst-1984
    claim-prepotential:
      status: passed
      summary: "F(X) = d_{IJK} X^I X^J X^K / (6 X^0) homogeneous degree 2 (max rel err 6.3e-15 over 50 tests). Determines scalar manifold geometry, gauge kinetic matrix, and Chern-Simons couplings. Does NOT produce Einstein-Hilbert term."
      linked_ids: [deliv-derivation, deliv-code, test-homogeneity, ref-dewit-vanproeyen, ref-lauria-vanproeyen]
      evidence:
        - verifier: gpd-executor
          method: homogeneity test (10 random X, 5 lambda each), diagonal cross-checks, general element cross-checks
          confidence: high
          claim_id: claim-prepotential
          deliverable_id: deliv-code
          acceptance_test_id: test-homogeneity
          reference_id: ref-dewit-vanproeyen
    claim-normalization:
      status: passed
      summary: "C_{IJK} = (1/6) d_{IJK}. Verified: d_{IJK} X^I X^J X^K = 6 at I_3 (where det_3 = 1), so C_{IJK} X^I X^J X^K = 1 = det_3(I_3). lambda = 1/6 uniquely determined."
      linked_ids: [deliv-derivation, deliv-code, test-normalization, ref-gst-1984]
      evidence:
        - verifier: gpd-executor
          method: evaluation at I_3 and 5 random diagonal elements
          confidence: high
          claim_id: claim-normalization
          deliverable_id: deliv-code
          acceptance_test_id: test-normalization
          reference_id: ref-gst-1984
  deliverables:
    deliv-derivation:
      status: passed
      path: "derivations/49-field-content-and-prepotential.tex"
      summary: "Propositions 1 (field content), 2 (prepotential), 3 (normalization). Contains field content table, F(X) formula, C_{IJK} = (1/6) d_{IJK}, E_{7(-25)}/(E_6(-78) x U(1)) identification."
      linked_ids: [claim-field-content, claim-prepotential, claim-normalization]
    deliv-code:
      status: passed
      path: "code/octonion_algebra.py"
      summary: "Added field_content_table_49, prepotential_F, peirce_coords, _peirce_gram_diagonal functions."
      linked_ids: [claim-field-content, claim-prepotential, claim-normalization]
  acceptance_tests:
    test-field-count:
      status: passed
      summary: "n_V = 26, total vectors = 27, real scalars = 54. Gravity multiplet + 26 vector multiplets = 27 indices. All 27 Peirce indices accounted. V_0 spacetime {17,18,19,26} + internal {20,...,25} = 4 + 6 = 10."
      linked_ids: [claim-field-content, deliv-code, ref-gst-1984]
    test-manifold-dim:
      status: passed
      summary: "dim E_{7(-25)} = 133, dim E_{6(-78)} = 78, dim U(1) = 1. Coset dim = 133 - 78 - 1 = 54 = 2 * 27 = real scalar count."
      linked_ids: [claim-field-content, deliv-derivation]
    test-homogeneity:
      status: passed
      summary: "F(lambda X) = lambda^2 F(X) for 10 random X and 5 random lambda. Max relative error 6.3e-15 (float64 noise)."
      linked_ids: [claim-prepotential, deliv-code]
    test-normalization:
      status: passed
      summary: "At I_3: d_{IJK} X^I X^J X^K = 6.000000 (exact). C_{IJK} X^I X^J X^K = 1.000000 = det_3(I_3). F(I_3) = 1.000000. Diagonal diag(a,b,c): F = bc to machine precision (5 tests, max err < 1e-15)."
      linked_ids: [claim-normalization, deliv-code, deliv-derivation, ref-gst-1984]
  references:
    ref-gst-1984:
      status: completed
      completed_actions: [cite, compare]
      missing_actions: []
      summary: "GST 1984 Table 1: 1 graviton, 27 vectors, 27+1 scalars in 5d. Our 4d count matches after absorbing extra scalar into prepotential: n_V=26, 27 vectors, 54 real scalars."
    ref-dewit-vanproeyen:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "de Wit-Van Proeyen 1992: direct 4d special Kahler formulation from cubic polynomial. Method followed for prepotential construction."
    ref-lauria-vanproeyen:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Lauria-Van Proeyen 2020: modern N=2 MESGT conventions. Bosonic Lagrangian structure cited in derivation."
    ref-phase47:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Phase 47 d_{IJK} tensor (106 nonzero entries) used as algebraic input. d(X,X,X) = 6 N(X) normalization confirmed."
    ref-ferrara-gunaydin:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Ferrara-Gunaydin hep-th/0606108: E_{7(-25)} orbits and exceptional MESGT structure. Confirms scalar manifold identification."
  forbidden_proxies:
    fp-wrong-real-form:
      status: rejected
      notes: "E_7(-25) (magic N=2) used throughout. Not E_7(7) (split, N=8) or E_7(-133) (compact). Explicitly stated in derivation document."
    fp-5d-kk-reduction:
      status: rejected
      notes: "No 5d -> 4d reduction performed. Direct 4d formulation from d_{IJK} via special Kahler geometry. Derivation contains no '5d', 'compactification', or 'Kaluza-Klein' language."
    fp-27-vector-multiplets:
      status: rejected
      notes: "n_V = 26 (not 27). Graviphoton A^0 is part of gravity multiplet, explicitly stated in Proposition 1 and field content table."
    fp-h2o-as-4d:
      status: rejected
      notes: "V_0 = h_2(O) is 10-dimensional. 4d spacetime = h_2(C_u) (dim 4) after pi_u projection. 6 internal directions explicitly separated."
  uncertainty_markers:
    weakest_anchors:
      - "The normalization C_{IJK} = (1/6) d_{IJK} is convention-dependent (Phase 47 uses d(X,X,X) = 6 N(X)); alternative conventions exist in the literature"
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations: []

comparison_verdicts:
  - subject_id: claim-field-content
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-gst-1984
    comparison_kind: benchmark
    metric: field_count
    threshold: "n_V = 26, total vectors = 27, real scalars = 54"
    verdict: pass
    recommended_action: "Proceed to Plan 02 (couplings and Lagrangian)"
    notes: "Exact match with GST 1984 field content after 5d -> 4d recount"
  - subject_id: claim-prepotential
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-dewit-vanproeyen
    comparison_kind: benchmark
    metric: homogeneity_error
    threshold: "< 1e-13"
    verdict: pass
    recommended_action: "Use F(X) in Plan 02 for gauge kinetic matrix"
    notes: "Max rel err 6.3e-15 over 50 homogeneity tests"
  - subject_id: claim-normalization
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-gst-1984
    comparison_kind: benchmark
    metric: exact_value_match
    threshold: "< 1e-14"
    verdict: pass
    recommended_action: "Use C_{IJK} = (1/6) d_{IJK} in Plan 02"
    notes: "d*X^3 = 6 and C*X^3 = 1 = det_3(I_3) at identity, exact to float64"

duration: 6min
completed: 2026-04-12
---

# Phase 49, Plan 01: Field Content and Prepotential -- Summary

**Identified 4d N=2 MESGT field content (1 gravity + 26 vector multiplets, 54 real scalars on E_{7(-25)}/(E_6(-78) x U(1))) and constructed prepotential F(X) = d_{IJK} X^I X^J X^K / (6 X^0) with normalization C_{IJK} = (1/6) d_{IJK}**

## Performance

- **Duration:** 6 min
- **Started:** 2026-04-12T14:48:59Z
- **Completed:** 2026-04-12T14:55:18Z
- **Tasks:** 2
- **Files modified:** 2

## Key Results

- Field content: 1 gravity multiplet (graviton + graviphoton A^0) + 26 vector multiplets (16 from V_{1/2} + 10 from V_0), giving 27 vectors and 54 real scalars on E_{7(-25)}/(E_6(-78) x U(1)) [CONFIDENCE: HIGH]
- Prepotential: F(X) = d_{IJK} X^I X^J X^K / (6 X^0) is homogeneous degree 2, verified with max rel err 6.3e-15 over 50 test cases [CONFIDENCE: HIGH]
- Normalization: C_{IJK} = (1/6) d_{IJK} uniquely fixed by evaluating at I_3 where det_3 = 1 and d * X^3 = 6 [CONFIDENCE: HIGH]
- Scalar manifold: dim = 133 - 78 - 1 = 54 = 2 * 27, matching real scalar count exactly [CONFIDENCE: HIGH]
- Diagonal cross-check: F(diag(a,b,c)) = bc = abc/a to machine precision for all test cases [CONFIDENCE: HIGH]

## Task Commits

1. **Task 1: Field content identification from Peirce decomposition** - `c97c9729` (derive)
2. **Task 2: Prepotential construction and normalization** - `70ab70ab` (compute)

## Files Created/Modified

- `code/octonion_algebra.py` - Added field_content_table_49, prepotential_F, peirce_coords, _peirce_gram_diagonal
- `derivations/49-field-content-and-prepotential.tex` - Propositions 1-3: field content, prepotential, normalization

## Next Phase Readiness

- Prepotential F(X) ready for Plan 02: gauge kinetic matrix N_{IJ}, Kahler potential, C_{IJK} coupling decomposition
- C_{IJK} = (1/6) d_{IJK} normalization established for all downstream coupling computations
- Field content table provides the physical interpretation of all 27 Peirce indices
- peirce_coords function enables coordinate extraction for any h_3(O) element

## Contract Coverage

- Claim IDs advanced: claim-field-content -> passed, claim-prepotential -> passed, claim-normalization -> passed
- Deliverable IDs produced: deliv-derivation -> derivations/49-field-content-and-prepotential.tex (passed), deliv-code -> code/octonion_algebra.py (passed)
- Acceptance test IDs run: test-field-count -> passed, test-manifold-dim -> passed, test-homogeneity -> passed, test-normalization -> passed
- Reference IDs surfaced: ref-gst-1984 -> cite+compare, ref-dewit-vanproeyen -> cite, ref-lauria-vanproeyen -> cite, ref-phase47 -> cite, ref-ferrara-gunaydin -> cite
- Forbidden proxies rejected: fp-wrong-real-form -> rejected, fp-5d-kk-reduction -> rejected, fp-27-vector-multiplets -> rejected, fp-h2o-as-4d -> rejected
- Decisive comparison verdicts: claim-field-content -> pass (GST 1984), claim-prepotential -> pass (de Wit-Van Proeyen), claim-normalization -> pass (GST 1984)

## Equations Derived

**Eq. (49.0):** Peirce decomposition

$$
27 = \underbrace{1}_{V_1} + \underbrace{16}_{V_{1/2}} + \underbrace{10}_{V_0}
$$

**Eq. (49.1):** Scalar manifold

$$
\mathcal{M}_{\mathrm{scalar}} = \frac{E_{7(-25)}}{E_{6(-78)} \times U(1)}, \qquad \dim_{\mathbb{R}} = 133 - 78 - 1 = 54
$$

**Eq. (49.2):** Prepotential

$$
F(X) = \frac{d_{IJK}\, X^I X^J X^K}{6\, X^0}
$$

**Eq. (49.3):** Normalization

$$
C_{IJK} = \frac{1}{6}\, d_{IJK}, \qquad C_{IJK}\, X^I X^J X^K = \det_3(X)
$$

## Validations Completed

- Field count: n_V = 26, total vectors = 27, real scalars = 54 (exact integers)
- Scalar manifold: 133 - 78 - 1 = 54 = 2 * 27 (exact arithmetic)
- All 27 Peirce indices assigned to supergravity multiplets (0 unassigned)
- V_0 splitting: 4 spacetime + 6 internal = 10 (exact, from Phase 46 pi_u)
- SM quantum numbers: multiset match with Paper 7 for all 16 V_{1/2} states
- Homogeneity: F(lambda X) = lambda^2 F(X), max rel err 6.3e-15 over 50 tests
- Normalization at I_3: d * X^3 = 6, C * X^3 = 1 = det_3(I_3) (exact)
- Diagonal cross-check: F(diag(a,b,c)) = bc for 5 random triples (max err < 1e-15)
- General cross-check: |F - det_3/X^0| < 3.6e-14 for 10 random elements
- No KK reduction in derivation (no '5d -> 4d' or 'compactification' language)
- No claim that F(X) produces Einstein-Hilbert action (explicitly disclaimed)
- Real form: E_7(-25) stated (not E_7(7) or E_7(-133))

## Decisions & Deviations

None -- followed plan exactly as specified.

## Open Questions

- The gauge kinetic matrix N_{IJ} = dbar_F_{IJ} + i(Im F . X)_I(Im F . X)_J / (X . Im F . X) must be computed in Plan 02 to complete the bosonic Lagrangian
- The Kahler potential K = -ln(i(X^I bar{F}_I - bar{X}^I F_I)) determines the scalar metric; its evaluation requires the holomorphic section structure
- How do the two Peirce blocks of C_{IJK} ((V_1,V_0,V_0) gravitational self-coupling and (V_{1/2},V_{1/2},V_0) matter-matter-gravity) manifest in physical cross-sections?

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
| --- | --- | --- | --- | --- | --- |
| Vector multiplets | n_V | 26 | exact | Peirce decomposition | -- |
| Total vectors | n_V + 1 | 27 | exact | +1 graviphoton | -- |
| Real scalars | 2(n_V+1) | 54 | exact | special Kahler | -- |
| Coset dimension | dim M | 54 | exact | 133-78-1 | -- |
| Homogeneity max err | rel err | 6.3e-15 | N/A | 50 tests | random H3O |
| Normalization | lambda | 1/6 | exact | d(X,X,X) = 6 N(X) | -- |
| F(I_3) | F | 1.0 | exact (float64) | evaluation | identity |
| Diagonal max err | abs err | < 1e-15 | N/A | 5 random diag | diag elements |
| General max err | abs err | 3.6e-14 | N/A | 10 random | general H3O |

## Approximations Used

None -- all computations are exact (finite-dimensional linear algebra over rationals embedded in float64).

## Issues Encountered

None.

## Self-Check: PASSED

- [x] code/octonion_algebra.py exists with field_content_table_49, prepotential_F, peirce_coords
- [x] derivations/49-field-content-and-prepotential.tex exists with Propositions 1-3
- [x] Commit c97c9729 exists (Task 1)
- [x] Commit 70ab70ab exists (Task 2)
- [x] All numerical results reproducible (seeds 42 for random tests)
- [x] Convention consistency: u=e_7, Fano e1*e2=e4, left-to-right association, E_7(-25), Peirce ordering
- [x] No KK reduction in any file
- [x] Graviphoton in gravity multiplet (not vector multiplet)
- [x] n_V = 26 (not 27)
- [x] F(X) does not produce Einstein-Hilbert (explicitly disclaimed)
- [x] All contract claims, deliverables, acceptance tests, references, forbidden proxies accounted for

---

_Phase: 49-gst-lagrangian-connection-direct-4d-formulation_
_Completed: 2026-04-12_
