---
phase: 52-g4-spacetime-derivation-v-0-is-spacetime
plan: 01
depth: full
one-liner: "KKT(h_2(C_u)) = so(4,2) verified with 15 generators, Killing sig (8,7), boosts B_i=L_{sigma_i} in Str_0 with [B_i,B_j]=-epsilon J_k (G5 resolved), OD1-OD6 all passed"
subsystem: [derivation, formalism, validation]
tags: [kkt-algebra, conformal-algebra, so42, lorentz, boosts, jordan-algebra, octonion, spacetime, peirce, causal-structure]

requires:
  - phase: 46-v-0-algebraic-foundation-and-pi-u-projection
    provides: "pi_u, det_2 with Gram diag(+1,-1,-1,-1), V_0 Peirce closure, jordan_product_h2o"
  - phase: 48-equivariance-and-lorentz-subgroup
    provides: "V_0 stabilizer so(3) x so(6), rotation generators in Minkowski basis, Phase 48 Eq 48.5-48.8"
provides:
  - "KKT algebra g(h_2(C_u)) = so(4,2) with all 15 generators and 105 structure constants"
  - "Killing form signature (8, 7) confirming so(4,2)"
  - "Boost generators B_i = L_{sigma_i} in Str_0 with [B_i, B_j] = -epsilon_{ijk} J_k (non-compact)"
  - "Lorentz subalgebra {B_i, J_i} = so(3,1) with Killing signature (3,3)"
  - "det_2 invariance under boosts (max error 2.1e-14)"
  - "OD1-OD6 operational criteria all verified"
  - "G5 gap resolved: boosts live in Str_0, not Der, not Spin(9)"
  - "Hierarchy: Der(J) = so(3) c Str_0(J) = so(3,1)+R c g(J) = so(4,2)"
affects: [52-02-plan, 53-n2-lagrangian-uniqueness, paper-assembly]

methods:
  added: [kkt-construction, jordan-triple-product, adjoint-representation, killing-form-computation]
  patterns: [mccrimmon-bracket-convention, pauli-basis-for-h2cu, L-operator-as-4x4-matrix]

key-files:
  modified: [code/octonion_algebra.py, derivations/52-kkt-spacetime.tex]

key-decisions:
  - "L_{e_0} = I_4 (not 1/2 I) because jordan_product includes the 1/2 factor"
  - "Rotation generators from SVD of derivation space, normalized to [J_i,J_j] = epsilon_{ijk} J_k"
  - "McCrimmon convention for KKT bracket: [T_a, K_b] = L(e_a o e_b) + [L(e_a), L(e_b)]"

patterns-established:
  - "KKT generator ordering: T_0-T_3 (g+1), D,B_1-B_3,J_1-J_3 (g0), K_0-K_3 (g-1)"
  - "Boost-boost sign convention: [B_i, B_j] = -epsilon_{ijk} J_k (negative = non-compact)"
  - "Killing eigenvalues: +8 (x8) and -8 (x7) for so(4,2) in this normalization"

conventions:
  - "metric_signature = (+,-,-,-)"
  - "jordan_product = (1/2)(ab + ba)"
  - "kkt_bracket = McCrimmon convention"
  - "killing_form = B(X,Y) = Tr(ad_X ad_Y)"
  - "u = e_7"
  - "Fano: e_1 e_2 = e_4"

plan_contract_ref: ".gpd/phases/52-g4-spacetime-derivation-v-0-is-spacetime/52-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-kkt-so42:
      status: passed
      summary: "KKT(h_2(C_u)) = so(4,2) verified: dim 15, all 105 structure constants computed, Jacobi max 3.3e-16, Killing form signature (8,7), abelian grades exact"
      linked_ids: [deliv-code, deliv-derivation, test-dim-15, test-jacobi, test-killing-sig, test-abelian-grades, ref-gunaydin93, ref-koecher67, ref-tits62, ref-mccrimmon04]
      evidence:
        - verifier: gpd-executor
          method: "Full 15x15x15 structure constant tensor + adjoint representation + Killing form eigenvalue decomposition"
          confidence: high
          claim_id: claim-kkt-so42
          deliverable_id: deliv-code
          acceptance_test_id: test-killing-sig
          reference_id: ref-gunaydin93
    claim-boost-identification:
      status: passed
      summary: "3 boost generators B_i = L_{sigma_i} explicitly constructed in Str_0, [B_i, B_j] = -epsilon_{ijk} J_k (NEGATIVE sign = non-compact so(3,1)), det_2 invariant under boosts to 2.1e-14"
      linked_ids: [deliv-code, deliv-derivation, test-boost-rotation, test-boost-boost-sign, test-det2-invariance, ref-koecher67, ref-phase48]
      evidence:
        - verifier: gpd-executor
          method: "Explicit L_a operator construction + matrix commutator verification + expm det_2 invariance test"
          confidence: high
          claim_id: claim-boost-identification
          deliverable_id: deliv-code
          acceptance_test_id: test-boost-boost-sign
          reference_id: ref-koecher67
    claim-od1-od4:
      status: passed
      summary: "OD1 (Peirce disjointness), OD2 (det_2 sig (1,3)), OD3 (surjection rank 10), OD4 (JSpin(3) maximality) all verified"
      linked_ids: [deliv-code, deliv-derivation, test-od1-disjoint, test-od2-det2, test-od3-surj, test-od4-maximal, ref-phase46, ref-mccrimmon04]
      evidence:
        - verifier: gpd-executor
          method: "Direct computation for OD1-OD3, structural argument for OD4"
          confidence: high
          claim_id: claim-od1-od4
          deliverable_id: deliv-code
          acceptance_test_id: test-od2-det2
          reference_id: ref-phase46
    claim-causal-structure:
      status: passed
      summary: "det_2 classifies h_2(C_u) elements as timelike/null/spacelike (OD5), forward cone {det_2>0, Tr>0} convex (OD6, 100 pairs x 10 combinations), boosts preserve det_2"
      linked_ids: [deliv-code, deliv-derivation, test-causal-classify, test-cone-convex, test-det2-invariance, ref-phase46, ref-baez02]
      evidence:
        - verifier: gpd-executor
          method: "Basis element classification + 1000 random convex combination tests"
          confidence: high
          claim_id: claim-causal-structure
          deliverable_id: deliv-code
          acceptance_test_id: test-cone-convex
          reference_id: ref-baez02
  deliverables:
    deliv-code:
      status: passed
      path: "code/octonion_algebra.py"
      summary: "Extended with compute_kkt_algebra(), verify_kkt_so42(), identify_boosts(), verify_od_criteria() plus helpers (_h2cu_pauli_basis, _h2cu_to_coords, _h2cu_from_coords, _jordan_product_h2cu, _compute_L_operator)"
      linked_ids: [claim-kkt-so42, claim-boost-identification, claim-od1-od4, claim-causal-structure]
    deliv-derivation:
      status: passed
      path: "derivations/52-kkt-spacetime.tex"
      summary: "KKT algebra derivation with 3-grading, Str_0 decomposition, boost identification, G5 resolution hierarchy, OD1-OD6 table, all anchor citations"
      linked_ids: [claim-kkt-so42, claim-boost-identification, claim-od1-od4, claim-causal-structure]
  acceptance_tests:
    test-dim-15:
      status: passed
      summary: "dim(g) = 15 exactly (4 translations + 7 Str_0 + 4 special conformal)"
      linked_ids: [claim-kkt-so42, deliv-code]
    test-jacobi:
      status: passed
      summary: "Jacobi identity max |[[X,Y],Z] + cyclic| = 3.3e-16 < 1e-13 for all 455 triples"
      linked_ids: [claim-kkt-so42, deliv-code]
    test-killing-sig:
      status: passed
      summary: "Killing form eigenvalues: {+8} x 8, {-8} x 7. Signature (8,7). det != 0 (semisimple). Confirms so(4,2)."
      linked_ids: [claim-kkt-so42, deliv-code, ref-gunaydin93]
    test-abelian-grades:
      status: passed
      summary: "[g+1, g+1] = 0 and [g-1, g-1] = 0 exactly (all brackets vanish to machine precision)"
      linked_ids: [claim-kkt-so42, deliv-code]
    test-boost-rotation:
      status: passed
      summary: "[B_i, J_j] verified for all 9 pairs: boosts transform as 3-vector under rotations"
      linked_ids: [claim-boost-identification, deliv-code]
    test-boost-boost-sign:
      status: passed
      summary: "[B_1,B_2]=-J_1, [B_1,B_3]=-J_2, [B_2,B_3]=-J_3. NEGATIVE sign confirmed for all 3 pairs (non-compact so(3,1), not compact so(4))"
      linked_ids: [claim-boost-identification, deliv-code]
    test-det2-invariance:
      status: passed
      summary: "|det_2(exp(tB)X) - det_2(X)| < 2.1e-14 for t in {0.1, 0.5, 1.0, 2.0}, all 3 boosts, 10 random elements each"
      linked_ids: [claim-causal-structure, claim-boost-identification, deliv-code]
    test-od1-disjoint:
      status: passed
      summary: "V_0 basis elements have alpha=0, x2=0, x3=0 (Peirce eigenspaces disjoint)"
      linked_ids: [claim-od1-od4, deliv-code]
    test-od2-det2:
      status: passed
      summary: "det_2 Gram matrix eigenvalues exactly {+1,-1,-1,-1}, signature (1,3)"
      linked_ids: [claim-od1-od4, deliv-code, ref-phase46]
    test-od3-surj:
      status: passed
      summary: "V_{1/2} x V_{1/2} -> V_0 surjective with rank 10"
      linked_ids: [claim-od1-od4, deliv-code]
    test-od4-maximal:
      status: passed
      summary: "h_2(C_u) = JSpin(3), dim 4. Any extension to dim 5+ breaks spin factor structure (structural argument)."
      linked_ids: [claim-od1-od4, deliv-derivation]
    test-causal-classify:
      status: passed
      summary: "I_2: det_2=+1 (timelike), sigma_1: det_2=-1 (spacelike), sigma_2: det_2=-1 (spacelike), sigma_3: det_2=-1 (spacelike). Classification correct."
      linked_ids: [claim-causal-structure, deliv-code]
    test-cone-convex:
      status: passed
      summary: "100 random pairs in forward cone, 10 convex combinations each, all remain in forward cone (det_2 > 0, Tr > 0)"
      linked_ids: [claim-causal-structure, deliv-code]
  references:
    ref-gunaydin93:
      status: completed
      completed_actions: [compare, cite]
      missing_actions: []
      summary: "Gunaydin 1993 benchmark TKK(h_2(C)) = su(2,2) = so(4,2) dim 15 reproduced exactly. Killing signature (8,7) matches."
    ref-koecher67:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Koecher 1967 KKT construction method used throughout. Str_0 decomposition follows Koecher's structure algebra."
    ref-tits62:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Tits 1962 3-grading g = g_{-1} + g_0 + g_{+1} defines the KKT construction used throughout."
    ref-phase46:
      status: completed
      completed_actions: [read]
      missing_actions: []
      summary: "Phase 46 det_2, pi_u, Peirce closure results used as input data for OD verification. Gram diag(+1,-1,-1,-1) confirmed."
    ref-phase48:
      status: completed
      completed_actions: [read, compare]
      missing_actions: []
      summary: "Phase 48 so(3) rotation generators in Minkowski basis matched against KKT rotation generators. Residual 2.2e-16 (ratio of 2 from gamma_ab/4 normalization). Confirms compact Spin(9) contains only so(3), not so(3,1)."
    ref-mccrimmon04:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "McCrimmon ATJA Ch IV Sec 14.2 KKT bracket formula used for all structure constant computations."
    ref-baez02:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Baez 2002 division algebra spacetime table: SL(2,K) = Spin(dim(K)+1,1). Independent cross-check: K=C gives Spin(3,1) = SL(2,C), conformal algebra so(4,2)."
  forbidden_proxies:
    fp-so3-only:
      status: rejected
      notes: "All 15 KKT generators constructed including 3 explicit boosts B_i = L_{sigma_i} in Str_0. Not just so(3) rotations."
    fp-fisher-rao:
      status: rejected
      notes: "Spacetime metric is det_2 (algebraic, indefinite signature (1,3)). Fisher-Rao not used anywhere."
    fp-abstract-boosts:
      status: rejected
      notes: "Boost generators explicitly constructed as L_{sigma_i} 4x4 matrices, commutation relations verified numerically."
    fp-complexification-shortcut:
      status: rejected
      notes: "Boosts identified WHERE they live in the REAL algebraic structure (Str_0), not via complexification argument."
  uncertainty_markers:
    weakest_anchors:
      - "Minkowski basis transformation B from Phase 48 -- coordinate ordering propagated consistently"
      - "McCrimmon vs Kantor convention factor: McCrimmon used throughout, consistent with [T_a, K_b] = L(a o b) + [L_a, L_b]"
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations: []

comparison_verdicts:
  - subject_id: claim-kkt-so42
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-gunaydin93
    comparison_kind: benchmark
    metric: "killing_signature_match"
    threshold: "signature = (8,7)"
    verdict: pass
    recommended_action: "Proceed to Phase 52 Plan 02 (observer independence)"
    notes: "Exact match to Gunaydin 1993 benchmark. Eigenvalues {+8}x8, {-8}x7."
  - subject_id: claim-boost-identification
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase48
    comparison_kind: prior_work
    metric: "boost_boost_sign"
    threshold: "sign = negative (non-compact)"
    verdict: pass
    recommended_action: "G5 resolved. Boosts in Str_0, not Der."
    notes: "[B_i,B_j] = -epsilon_{ijk} J_k confirmed for all 3 pairs. Phase 48 so(3)-only result explained by compact Spin(9) limitation."
  - subject_id: claim-causal-structure
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-baez02
    comparison_kind: benchmark
    metric: "det2_invariance_under_boosts"
    threshold: "<= 1e-12"
    verdict: pass
    recommended_action: "Causal structure established. det_2 is the invariant quadratic form."
    notes: "Max error 2.1e-14. Consistent with Baez 2002 SL(2,C) acting on h_2(C) preserving det."

duration: 8min
completed: 2026-04-13
---

# Phase 52, Plan 01: KKT Algebra g(h_2(C_u)) = so(4,2) -- Summary

**KKT(h_2(C_u)) = so(4,2) verified with 15 generators, Killing sig (8,7), boosts B_i=L_{sigma_i} in Str_0 with [B_i,B_j]=-epsilon J_k (G5 resolved), OD1-OD6 all passed**

## Performance

- **Duration:** ~8 min
- **Started:** 2026-04-13T13:48:51Z
- **Completed:** 2026-04-13T13:57:00Z
- **Tasks:** 2
- **Files modified:** 2

## Key Results

- KKT(h_2(C_u)) = so(4,2) with dim 15, Killing form signature (8,7), Jacobi max error 3.3e-16 [CONFIDENCE: HIGH]
- Boost generators B_i = L_{sigma_i} in Str_0 with [B_i, B_j] = -epsilon_{ijk} J_k (non-compact so(3,1), resolving G5) [CONFIDENCE: HIGH]
- Lorentz subalgebra {B_i, J_i} has Killing signature (3,3), confirming so(3,1) [CONFIDENCE: HIGH]
- det_2 invariant under boosts: max |Delta det_2| = 2.1e-14 [CONFIDENCE: HIGH]
- OD1-OD6 all verified (Peirce disjointness, Lorentzian det_2, surjectivity, maximality, causal classification, cone convexity) [CONFIDENCE: HIGH]
- Hierarchy: Der(J) = so(3) c Str_0(J) = so(3,1)+R c g(J) = so(4,2) [CONFIDENCE: HIGH]
- Phase 48 rotation generators match KKT rotations (residual 2.2e-16) [CONFIDENCE: HIGH]

## Task Commits

1. **Task 1: Construct KKT algebra g(h_2(C_u)) and verify = so(4,2)** - `9f499c59` (derive)
2. **Task 2: Identify boosts in Str_0, verify OD1-OD6, write derivation** - `9e6fbea8` (derive)

## Files Created/Modified

- `code/octonion_algebra.py` - Added compute_kkt_algebra(), verify_kkt_so42(), identify_boosts(), verify_od_criteria() plus helpers
- `derivations/52-kkt-spacetime.tex` - KKT algebra derivation, boost identification, G5 resolution, OD1-OD6 verification table

## Next Phase Readiness

- so(4,2) conformal algebra established for V_0 = h_2(C_u) -- ready for Plan 02 (observer independence)
- Boost generators explicitly available for downstream Lorentz covariance checks
- G5 resolved: Phase 53 (N=2 Lagrangian uniqueness) can proceed knowing V_0 has full Lorentz symmetry
- OD1-OD6 verification complete -- spacetime operational criteria satisfied

## Contract Coverage

- Claim IDs: claim-kkt-so42 -> passed, claim-boost-identification -> passed, claim-od1-od4 -> passed, claim-causal-structure -> passed
- Deliverable IDs: deliv-code -> passed (code/octonion_algebra.py), deliv-derivation -> passed (derivations/52-kkt-spacetime.tex)
- Acceptance tests: test-dim-15 -> passed, test-jacobi -> passed, test-killing-sig -> passed, test-abelian-grades -> passed, test-boost-rotation -> passed, test-boost-boost-sign -> passed, test-det2-invariance -> passed, test-od1-disjoint -> passed, test-od2-det2 -> passed, test-od3-surj -> passed, test-od4-maximal -> passed, test-causal-classify -> passed, test-cone-convex -> passed
- References: ref-gunaydin93 -> compare+cite, ref-koecher67 -> cite, ref-tits62 -> cite, ref-phase46 -> read, ref-phase48 -> read+compare, ref-mccrimmon04 -> cite, ref-baez02 -> cite
- Forbidden proxies: fp-so3-only -> rejected, fp-fisher-rao -> rejected, fp-abstract-boosts -> rejected, fp-complexification-shortcut -> rejected
- Comparison verdicts: claim-kkt-so42 -> pass (Gunaydin93 benchmark), claim-boost-identification -> pass (Phase 48 comparison), claim-causal-structure -> pass (det_2 invariance)

## Equations Derived

**Eq. (52.1):** KKT 3-grading

$$\mathfrak{g}(\mathfrak{h}_2(\mathbb{C}_u)) = \mathfrak{g}_{-1} \oplus \mathfrak{g}_0 \oplus \mathfrak{g}_{+1} = J \oplus \mathrm{Str}_0(J) \oplus J$$

dim = 4 + 7 + 4 = 15.

**Eq. (52.2):** L operators on Pauli basis

$$L_{e_0} = I_4, \quad L_{\sigma_i} = \text{(symmetric, traceless, rank 2)}$$

**Eq. (52.3):** Str_0 decomposition

$$\mathrm{Str}_0(J) = \mathrm{Der}(J) \oplus \{L_a : a \text{ traceless}\} \oplus \mathbb{R} \cdot E = \mathfrak{so}(3) \oplus \mathbb{R}^3 \oplus \mathbb{R}$$

dim = 3 + 3 + 1 = 7.

**Eq. (52.4):** Boost-boost commutation (non-compact sign)

$$[B_i, B_j] = -\epsilon_{ijk} J_k$$

**Eq. (52.5):** Symmetry hierarchy (G5 resolution)

$$\mathrm{Der}(J) = \mathfrak{so}(3) \subset \mathrm{Str}_0(J) = \mathfrak{so}(3,1) \oplus \mathbb{R} \subset \mathfrak{g}(J) = \mathfrak{so}(4,2)$$

**Eq. (52.6):** Killing form signature

$$B(X,Y) = \mathrm{Tr}(\mathrm{ad}_X \, \mathrm{ad}_Y), \quad \text{eigenvalues } \{+8\} \times 8, \{-8\} \times 7, \quad \text{signature } (8,7)$$

## Validations Completed

- Killing form signature (8,7) matches Gunaydin 1993 benchmark for so(4,2)
- Jacobi identity: max residual 3.3e-16 < 1e-13 for all 455 triples of 15 generators
- Abelian grades: [g+1, g+1] = 0, [g-1, g-1] = 0 exactly
- Boost-boost sign: [B_i, B_j] = -epsilon J_k (NEGATIVE = non-compact so(3,1), not compact so(4))
- det_2 invariance under boosts: max error 2.1e-14 over 120 test cases
- Phase 48 cross-check: KKT rotation generators span same space as Phase 48 so(3) (residual 2.2e-16)
- Lorentz subalgebra Killing signature (3,3) = so(3,1)
- OD1-OD6: all 6 operational criteria verified

## Decisions & Deviations

None -- plan executed exactly as written. All code was already implemented and committed from prior execution; this run verified all results and created SUMMARY.

## Open Questions

- How does the conformal algebra so(4,2) constrain the dynamics on V_0? (Plan 02 addresses observer independence)
- Relationship between KKT dilatation D and physical scale transformations in the self-modeling framework
- Whether the full conformal group SO(4,2) is realized as a symmetry, or only the Poincare subgroup ISO(3,1) c SO(4,2)

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
| --- | --- | --- | --- | --- | --- |
| KKT algebra dimension | dim g | 15 | exact | Generator counting | h_2(C_u) |
| Killing form eigenvalues | spec(B) | {+8}x8, {-8}x7 | exact (float64) | Tr(ad_X ad_Y) computation | all 15 generators |
| Killing form signature | sig(B) | (8, 7) | exact | eigenvalue sign count | so(4,2) |
| Jacobi identity residual | max Jac | 3.3e-16 | machine precision | all 455 triples | all generators |
| Boost det_2 invariance | max err | 2.1e-14 | float64 accumulation | expm test, 120 cases | t in [0.1, 2.0] |
| Phase 48 cross-check | resid | 2.2e-16 | machine precision | lstsq projection | all 3 rotation gens |
| Lorentz Killing signature | sig(B_lor) | (3, 3) | exact | 6x6 Killing submatrix | so(3,1) subspace |
| Forward cone convexity | failures | 0 / 1000 | exact | 100 pairs x 10 t-values | seed 137 |

## Approximations Used

None -- all computations are exact (finite-dimensional linear algebra over rationals embedded in float64).

## Issues Encountered

None.

## Self-Check: PASSED

- [x] code/octonion_algebra.py exists with compute_kkt_algebra, verify_kkt_so42, identify_boosts, verify_od_criteria
- [x] derivations/52-kkt-spacetime.tex exists with so(4,2), L_{a,b}, Str_0, OD1, OD5
- [x] Commit 9f499c59 exists (Task 1)
- [x] Commit 9e6fbea8 exists (Task 2)
- [x] All numerical results reproducible (deterministic + seeds 42, 137)
- [x] Convention consistency: McCrimmon bracket, (+,-,-,-), u=e_7, Fano e_1 e_2 = e_4 throughout
- [x] All 4 forbidden proxies explicitly rejected
- [x] All 7 must_surface references surfaced with required actions completed
- [x] All 4 claims passed, all 13 acceptance tests passed, all 2 deliverables passed
- [x] 3 decisive comparison verdicts emitted (Gunaydin93, Phase48, Baez02)

---

_Phase: 52-g4-spacetime-derivation-v-0-is-spacetime, Plan: 01_
_Completed: 2026-04-13_
