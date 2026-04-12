---
phase: 47-d-ijk-tensor-and-uniqueness-theorems
plan: 01
depth: full
one-liner: "Computed d_{IJK} tensor on h_3(O) by polarization of det_3; exhaustive Peirce classification yields exactly two nonzero blocks (V_1,V_0,V_0) and (V_{1/2},V_{1/2},V_0)"
subsystem: [formalism, validation]
tags: [octonion, jordan-algebra, cubic-norm, peirce-decomposition, d-tensor, E6-invariant]

requires:
  - phase: 46-v-0-algebraic-foundation-and-pi-u-projection
    provides: H3O class, jordan_product, Peirce projections, V0_basis_elements, Vhalf_basis_vectors, proj_u, pi_u, det_2
provides:
  - det_3 cubic norm function on h_3(O) with left-to-right association Re((x1*x2)*x3)
  - polarize_d symmetric trilinear form via inclusion-exclusion (d(X,X,X)=6*N(X))
  - peirce_basis_27 function (27-element Peirce-adapted basis, I=0 V_1, I=1..16 V_{1/2}, I=17..26 V_0)
  - d_ijk_tensor function (exhaustive computation, 106 nonzero entries)
  - classify_peirce_blocks function (sector classification)
  - Two-block theorem verified: exactly (V_1,V_0,V_0) and (V_{1/2},V_{1/2},V_0) nonzero
  - (V_1,V_0,V_0) block = det_2 bilinear form (exact match)
affects: [47-02-uniqueness-theorems, 49-gst-matching]

methods:
  added: [det_3 cubic norm, inclusion-exclusion polarization, exhaustive basis triple evaluation]
  patterns: [Peirce block classification by sector triple, det_2 bilinear cross-check]

key-files:
  modified: [code/octonion_algebra.py]

key-decisions:
  - "No new decisions required -- followed plan exactly using locked conventions"

patterns-established:
  - "det_3(X) = alpha*beta*gamma - alpha*|x1|^2 - beta*|x2|^2 - gamma*|x3|^2 + 2*Re((x1*x2)*x3)"
  - "d(X,Y,Z) via inclusion-exclusion: N(X+Y+Z) - N(X+Y) - N(X+Z) - N(Y+Z) + N(X) + N(Y) + N(Z)"
  - "Peirce index convention: I=0 (V_1), I=1..16 (V_{1/2}), I=17..26 (V_0)"
  - "(V_1,V_0,V_0) block is diagonal: diag(+0.5, -0.5, -2, -2, -2, -2, -2, -2, -2, -2)"
  - "d_{IJK} is 97% sparse: 106/3654 nonzero distinct triples"

conventions:
  - "u = e_7 (complex structure)"
  - "jordan_product = (1/2)(AB + BA)"
  - "det_3 association: left-to-right Re((x1*x2)*x3)"
  - "d_{IJK} normalization: d(X,X,X) = 6*N(X) via inclusion-exclusion"
  - "Fano: e_1 e_2 = e_4"
  - "Peirce idempotent: E_{11}"

plan_contract_ref: ".gpd/phases/47-d-ijk-tensor-and-uniqueness-theorems/47-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-det3:
      status: passed
      summary: "det_3(X) implemented with correct Re((x1*x2)*x3) left-to-right association; passes all 7 benchmark categories including I_3, idempotents, diagonal, homogeneity, C_u restriction"
      linked_ids: [deliv-code, test-det3-benchmarks, test-det3-homogeneity, ref-baez]
      evidence:
        - verifier: gpd-executor
          method: 7-category benchmark suite (exact values, random tests, C_u restriction)
          confidence: high
          claim_id: claim-det3
          deliverable_id: deliv-code
          acceptance_test_id: test-det3-benchmarks
          reference_id: ref-baez
    claim-dijk:
      status: passed
      summary: "d_{IJK} computed by polarization on all 3654 distinct triples of the 27-element Peirce basis; d(X,X,X) = 6*N(X) verified to float64 precision"
      linked_ids: [deliv-code, test-dijk-symmetry, test-dijk-polarization, ref-baez]
      evidence:
        - verifier: gpd-executor
          method: exhaustive basis triple evaluation + symmetry spot-check + polarization identity
          confidence: high
          claim_id: claim-dijk
          deliverable_id: deliv-code
          acceptance_test_id: test-dijk-symmetry
          reference_id: ref-baez
    claim-two-blocks:
      status: passed
      summary: "Exactly two nonzero Peirce block types: (V_1,V_0,V_0) with 10 entries and (V_{1/2},V_{1/2},V_0) with 96 entries; all other blocks identically zero (max |d| = 0 to machine precision)"
      linked_ids: [deliv-code, test-block-structure, test-d000-zero, ref-slansky, ref-baez]
      evidence:
        - verifier: gpd-executor
          method: exhaustive evaluation of all 3654 distinct triples with sector classification
          confidence: high
          claim_id: claim-two-blocks
          deliverable_id: deliv-code
          acceptance_test_id: test-block-structure
          reference_id: ref-slansky
    claim-v1v0v0-is-det2:
      status: passed
      summary: "(V_1,V_0,V_0) block d(E_{11},e_a,e_b) exactly matches det_2 bilinear form B(e_a,e_b) = det_2(e_a+e_b) - det_2(e_a) - det_2(e_b) for all 55 V_0 basis pairs"
      linked_ids: [deliv-code, test-v1v0v0-det2, ref-baez]
      evidence:
        - verifier: gpd-executor
          method: exhaustive 55-pair comparison with det_2 bilinear form
          confidence: high
          claim_id: claim-v1v0v0-is-det2
          deliverable_id: deliv-code
          acceptance_test_id: test-v1v0v0-det2
          reference_id: ref-baez
  deliverables:
    deliv-code:
      status: passed
      path: "code/octonion_algebra.py"
      summary: "Extended with det_3, polarize_d, peirce_basis_27, peirce_sector, d_ijk_tensor, classify_peirce_blocks"
      linked_ids: [claim-det3, claim-dijk, claim-two-blocks, claim-v1v0v0-is-det2]
  acceptance_tests:
    test-det3-benchmarks:
      status: passed
      summary: "det_3(I_3)=1 (exact), det_3(E_{ii})=0 for all i (exact), det_3(diag(a,b,c))=abc for 5 random triples (rel err 0), h_3(C_u) restriction matches complex det (rel err 2.9e-16)"
      linked_ids: [claim-det3, deliv-code, ref-baez]
    test-det3-homogeneity:
      status: passed
      summary: "det_3(lam*X) = lam^3 * det_3(X) for 10 random X x 5 lambda values; max rel err 9.2e-15"
      linked_ids: [claim-det3, deliv-code]
    test-dijk-symmetry:
      status: passed
      summary: "d(e_I,e_J,e_K) invariant under all 6 permutations for 50 random triples; max error 0 (exact to machine precision)"
      linked_ids: [claim-dijk, deliv-code]
    test-dijk-polarization:
      status: passed
      summary: "d(X,X,X) = 6*N(X) for 20 random X; max rel err 1.4e-13 (float64 noise from 7 det_3 evaluations, absolute error 6e-14)"
      linked_ids: [claim-dijk, deliv-code]
    test-block-structure:
      status: passed
      summary: "Exhaustive classification of all 3654 distinct triples: exactly (V_1,V_0,V_0) and (V_{1/2},V_{1/2},V_0) nonzero. All forbidden blocks exactly zero: pure V_0 (220 triples), V_1^2 x V_0 (10), V_1 x V_{1/2}^2 (136), V_{1/2}^3 (816), V_1 x V_{1/2} x V_0 (160)"
      linked_ids: [claim-two-blocks, deliv-code, ref-slansky]
    test-d000-zero:
      status: passed
      summary: "d_{0,0,0} = 6*N(E_{11}) = 0 exactly; all 220 pure V_0 triples exactly zero"
      linked_ids: [claim-two-blocks, deliv-code]
    test-v1v0v0-det2:
      status: passed
      summary: "All 55 V_0 basis pairs: d(E_{11},e_a,e_b) = B(e_a,e_b) with zero error (exact match)"
      linked_ids: [claim-v1v0v0-is-det2, deliv-code, ref-baez]
  references:
    ref-baez:
      status: completed
      completed_actions: [cite, compare]
      missing_actions: []
      summary: "Baez 2002 Sec 3.4: cubic norm formula N(X) on h_3(O). Confirmed: det_3 reproduces all benchmarks. Peirce decomposition 27=1+16+10 confirmed by basis construction."
    ref-slansky:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Slansky 1981: E_6 branching 27 -> 1_2 + 10_{-1} + 16_1. Two-block structure confirmed by exhaustive computation matching the charge-balance prediction."
  forbidden_proxies:
    fp-sampling:
      status: rejected
      notes: "All 3654 distinct triples evaluated exhaustively. No sampling used."
    fp-wrong-association:
      status: rejected
      notes: "det_3 uses left-to-right (x1*x2)*x3 throughout. Verified by C_u restriction matching standard complex determinant."
    fp-normalization-mismatch:
      status: rejected
      notes: "d(X,X,X) = 6*N(X) verified for 20 random X. Factor of 6 from inclusion-exclusion is consistent with N(X) = (1/6)*d_{IJK}*X^I*X^J*X^K."
  uncertainty_markers:
    weakest_anchors: []
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations: []

comparison_verdicts:
  - subject_id: claim-det3
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-baez
    comparison_kind: benchmark
    metric: exact_value_match
    threshold: "< 1e-14"
    verdict: pass
    recommended_action: "Proceed to Plan 02 (uniqueness theorems)"
    notes: "det_3(I_3)=1, det_3(E_{ii})=0, det_3(diag)=abc all exact"
  - subject_id: claim-two-blocks
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-slansky
    comparison_kind: benchmark
    metric: block_type_count
    threshold: "exactly 2 nonzero block types"
    verdict: pass
    recommended_action: "Proceed to Plan 02 and Phase 49"
    notes: "(V_1,V_0,V_0) and (V_{1/2},V_{1/2},V_0) only; all forbidden blocks identically zero"
  - subject_id: claim-v1v0v0-is-det2
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-baez
    comparison_kind: cross_method
    metric: max_absolute_error
    threshold: "< 1e-14"
    verdict: pass
    recommended_action: "Use det_2 bilinear form as proxy for (V_1,V_0,V_0) block in downstream phases"
    notes: "Exact match between d(E_{11},e_a,e_b) and det_2 bilinear form B(e_a,e_b)"

duration: 8min
completed: 2026-04-12
---

# Phase 47, Plan 01: d_{IJK} Tensor Computation and Peirce Block Decomposition -- Summary

**Computed d_{IJK} tensor on h_3(O) by polarization of det_3; exhaustive Peirce classification yields exactly two nonzero blocks (V_1,V_0,V_0) and (V_{1/2},V_{1/2},V_0)**

## Performance

- **Duration:** 8 min
- **Started:** 2026-04-12T12:43:38Z
- **Completed:** 2026-04-12T12:51:38Z
- **Tasks:** 2
- **Files modified:** 1

## Key Results

- det_3(X) = alpha*beta*gamma - alpha*|x1|^2 - beta*|x2|^2 - gamma*|x3|^2 + 2*Re((x1*x2)*x3) implemented with correct left-to-right association; all 7 benchmark categories pass [CONFIDENCE: HIGH]
- d_{IJK} tensor has exactly 106 nonzero entries out of 3654 distinct triples (97% sparse); fully symmetric to machine precision [CONFIDENCE: HIGH]
- Exactly two nonzero Peirce block types: (V_1,V_0,V_0) with 10 entries and (V_{1/2},V_{1/2},V_0) with 96 entries; all forbidden blocks identically zero [CONFIDENCE: HIGH]
- (V_1,V_0,V_0) block = det_2 bilinear form with zero error, confirming N(X) contains the term alpha*det_2(X_0) [CONFIDENCE: HIGH]

## Task Commits

1. **Task 1: Implement det_3 and polarization, verify on benchmarks** - `2660aec2` (implement)
2. **Task 2: Compute full d_{IJK} tensor and classify Peirce blocks** - `30b46afc` (validate)

## Files Created/Modified

- `code/octonion_algebra.py` - Added det_3, polarize_d, peirce_basis_27, peirce_sector, d_ijk_tensor, classify_peirce_blocks; verification comment blocks

## Next Phase Readiness

- d_{IJK} tensor available for Plan 02 (uniqueness theorems via F_4 invariance)
- Two-block structure ready for Phase 49 (GST matching: d_{IJK} = C_{IJK} prepotential tensor)
- (V_1,V_0,V_0) block identified with det_2: the singlet-gravity coupling
- (V_{1/2},V_{1/2},V_0) block encodes matter-matter-gravity couplings (96 entries)
- peirce_basis_27() provides the canonical 27-element basis for all subsequent tensor computations

## Contract Coverage

- Claim IDs advanced: claim-det3 -> passed, claim-dijk -> passed, claim-two-blocks -> passed, claim-v1v0v0-is-det2 -> passed
- Deliverable IDs produced: deliv-code -> code/octonion_algebra.py (passed)
- Acceptance test IDs run: test-det3-benchmarks -> passed, test-det3-homogeneity -> passed, test-dijk-symmetry -> passed, test-dijk-polarization -> passed, test-block-structure -> passed, test-d000-zero -> passed, test-v1v0v0-det2 -> passed
- Reference IDs surfaced: ref-baez -> cite+compare, ref-slansky -> cite
- Forbidden proxies rejected: fp-sampling -> rejected, fp-wrong-association -> rejected, fp-normalization-mismatch -> rejected
- Decisive comparison verdicts: claim-det3 -> pass (Baez), claim-two-blocks -> pass (Slansky), claim-v1v0v0-is-det2 -> pass (det_2 cross-check)

## Equations Derived

**Eq. (47.1):** Cubic norm on h_3(O)

$$
N(X) = \alpha\beta\gamma - \alpha|x_1|^2 - \beta|x_2|^2 - \gamma|x_3|^2 + 2\,\mathrm{Re}((x_1 x_2)x_3)
$$

**Eq. (47.2):** Polarization identity (inclusion-exclusion)

$$
d(X,Y,Z) = N(X{+}Y{+}Z) - N(X{+}Y) - N(X{+}Z) - N(Y{+}Z) + N(X) + N(Y) + N(Z)
$$

**Eq. (47.3):** Normalization

$$
d(X,X,X) = 6\,N(X), \quad N(X) = \tfrac{1}{6}\,d_{IJK}\,X^I X^J X^K
$$

**Eq. (47.4):** (V_1,V_0,V_0) block

$$
d(E_{11}, e_a, e_b) = B(e_a, e_b) = \mathrm{det}_2(e_a + e_b) - \mathrm{det}_2(e_a) - \mathrm{det}_2(e_b)
$$

with Gram matrix $\mathrm{diag}(+\tfrac{1}{2}, -\tfrac{1}{2}, -2, -2, -2, -2, -2, -2, -2, -2)$ in the V_0 basis.

## Validations Completed

- det_3(I_3) = 1.0 (exact) -- Baez 2002 anchor
- det_3(E_{ii}) = 0 for all i (exact) -- rank-1 idempotent check
- det_3(diag(a,b,c)) = abc for 5 random triples (zero error)
- Cubic homogeneity: max rel err 9.2e-15 over 50 test cases
- Polarization symmetry: max |d(perm) - d| = 6.8e-14 over 100 permutation checks
- d(X,X,X) = 6*N(X): max rel err 1.4e-13 (float64 noise; abs err 6e-14)
- h_3(C_u) restriction: matches standard complex 3x3 det to 2.9e-16
- Two-block structure: exhaustive over all 3654 distinct triples
- All forbidden blocks: max |d| = 0 (not just small -- exactly zero)
- (V_1,V_0,V_0) = det_2 bilinear: zero error on all 55 pairs
- d_{IJK} symmetry: zero error on 50 random spot-checks

## Decisions & Deviations

None -- followed plan exactly as specified.

## Open Questions

- The (V_{1/2},V_{1/2},V_0) block has 96 nonzero entries with a specific pattern: 16 couplings each for the trace (b[0]) and traceless diagonal (b[1]) V_0 basis elements, and 8 couplings each for the 8 off-diagonal V_0 basis elements. This pattern likely reflects the Spin(9) representation structure on V_{1/2} = R^{16}. Plan 02 will use this to establish uniqueness.

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
| --- | --- | --- | --- | --- | --- |
| Nonzero d_{IJK} entries | count | 106 | exact | exhaustive evaluation | all I <= J <= K |
| (V_1,V_0,V_0) entries | count | 10 | exact | exhaustive | I=0, J,K in 17..26 |
| (V_{1/2},V_{1/2},V_0) entries | count | 96 | exact | exhaustive | I,J in 1..16, K in 17..26 |
| det_3(I_3) | N(I_3) | 1.0 | exact (float64) | det_3 evaluation | identity element |
| Homogeneity max error | rel err | 9.2e-15 | N/A | 50 random test cases | random H3O elements |
| Polarization max error | rel err | 1.4e-13 | N/A | 20 random X | random H3O elements |
| Forbidden block max | max |d| | 0.0 | exact (float64) | all 1342 forbidden triples |

## Approximations Used

None -- all computations are exact (finite-dimensional linear algebra over rationals embedded in float64).

## Issues Encountered

None.

## Self-Check: PASSED

- [x] code/octonion_algebra.py exists with det_3, polarize_d, peirce_basis_27, d_ijk_tensor, classify_peirce_blocks
- [x] Commit 2660aec2 exists (Task 1)
- [x] Commit 30b46afc exists (Task 2)
- [x] All numerical results reproducible (deterministic + explicit seeds 42/137/999/314/271)
- [x] Convention consistency: u=e_7, Jordan 1/2 factor, left-to-right association, Fano e1*e2=e4
- [x] All 3654 distinct triples evaluated (fp-sampling rejected)
- [x] Left-to-right association used throughout (fp-wrong-association rejected)
- [x] d(X,X,X) = 6*N(X) normalization verified (fp-normalization-mismatch rejected)

---

_Phase: 47-d-ijk-tensor-and-uniqueness-theorems_
_Completed: 2026-04-12_
