---
phase: 29-observable-algebra-and-representation-theory
plan: 01
depth: full
one-liner: "Associative closure of Peirce operators is all of M_16(R) (256-dim); J_u is NOT a 10th Clifford generator (mixed grade 2+3, commutes with gamma_1); enters closure at depth 2"
subsystem: [computation, validation]
tags: [octonion, jordan-algebra, peirce-decomposition, albert-algebra, clifford-algebra, spin9, gap-c, ALGV-03, REPR-01]

requires:
  - phase: "28-peirce-verification-and-v-0-channel-exploration (Plan 02)"
    provides: "All 10 T_b matrices, Cl(9) anticommutation, J_u matrix, 46-dim Lie algebra"
provides:
  - "ALGV-03: Associative closure of {T_b} = M_16(R) (256-dim, full matrix algebra on V_{1/2})"
  - "Volume element omega = +I_{16} identifies the P_+ factor of Cl(9,0)"
  - "J_u does NOT anticommute with all gamma_i (commutes with gamma_1, mixed with rest)"
  - "J_u is mixed Clifford grade 2+3 (4 grade-2 + 4 grade-3 nonzero coefficients)"
  - "J_u enters associative closure at depth 2 (compositions of 3 Peirce operators)"
  - "Dimension growth: 10 -> 46 -> 130 -> 256"
  - "Clifford rescaling: gamma_1 = 4*T_b[1], gamma_k = 2*T_b[k] for k=2..9"
affects: [29-plan-02-repr02-verdict, 30-selection-arguments]

methods:
  added: [associative-closure-iterative, clifford-grade-decomposition, volume-element-computation, clifford-rescaling]
  patterns: [iterative-span-growth-via-SVD, omega-identification-for-grade-reduction]

key-files:
  modified: [code/octonion_algebra.py]
  created: [tests/test_observable_algebra.py]

key-decisions:
  - "Clifford rescaling: gamma_1 = 4*T_b[1] (factor 4, not 2), gamma_k = 2*T_b[k] for k=2..9 (verified from eigenvalue spectra)"
  - "Grade decomposition uses grades 0-4 only (256 independent monomials) since omega = +I identifies grades k and 9-k"
  - "Efficiency: associative closure multiplies only NEW basis vectors by generators at each depth"

patterns-established:
  - "omega = +I means Cl(9,0) projects to M_16(R) via P_+ = (1+omega)/2; only grades 0-4 are independent"
  - "J_u = grade 2+3 mix with equal-weight coefficients; physically this means J_u arises from iterated Peirce compositions, not from the linear span or Lie algebra"

conventions:
  - "jordan_product = (1/2)(ab + ba)"
  - "octonion_basis = fano_e1e2=e4"
  - "peirce_decomposition under E_11"
  - "v_half_basis = (x2_0..x2_7, x3_0..x3_7)"
  - "clifford_signature = Cl(9,0), gamma_i^2 = +I"
  - "clifford_normalization = gamma_1 = 4*T_b[1], gamma_k = 2*T_b[k] for k=2..9"
  - "complex_structure = u_equals_e7"

plan_contract_ref: ".gpd/phases/29-observable-algebra-and-representation-theory/29-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-algv03-closure:
      status: passed
      summary: "Associative closure of {T_b} is M_16(R) (256-dim). SVD rank converges 10 -> 46 -> 130 -> 256, with singular value gap > 1e-10. Confirms Cl(9,0) irrep surjects onto End(R^16)."
      linked_ids: [deliv-closure-code, deliv-closure-tests, test-closure-dim-256, test-closure-growth, ref-lawson-michelsohn, ref-phase28]
      evidence:
        - verifier: gpd-executor
          method: iterative associative closure via SVD rank computation
          confidence: high
          claim_id: claim-algv03-closure
          deliverable_id: deliv-closure-code
          acceptance_test_id: test-closure-dim-256
          reference_id: ref-lawson-michelsohn
    claim-repr01-clifford:
      status: passed
      summary: "9 rescaled T_b operators are Cl(9,0) generators. Volume element omega = gamma_1...gamma_9 = +I_{16} (all eigenvalues +1, zero error). This identifies the representation as using the P_+ factor of Cl(9,0) = M_16(R) + M_16(R)."
      linked_ids: [deliv-closure-code, deliv-closure-tests, test-volume-element, test-closure-dim-256, ref-lawson-michelsohn, ref-phase28]
      evidence:
        - verifier: gpd-executor
          method: direct computation of volume element and eigenvalue check
          confidence: high
          claim_id: claim-repr01-clifford
          deliverable_id: deliv-closure-code
          acceptance_test_id: test-volume-element
          reference_id: ref-lawson-michelsohn
    claim-ju-anticommutation:
      status: passed
      summary: "J_u does NOT anticommute with all 9 gamma_i. J_u COMMUTES with gamma_1 (diagonal traceless operator); has mixed (neither pure commutation nor anticommutation) relation with gamma_2..gamma_9. This means J_u is NOT a '10th Clifford generator'."
      linked_ids: [deliv-closure-code, deliv-closure-tests, test-ju-anticommutation, ref-krasnov2019, ref-boyle2020]
      evidence:
        - verifier: gpd-executor
          method: explicit anticommutator/commutator computation with Frobenius norms
          confidence: high
          claim_id: claim-ju-anticommutation
          deliverable_id: deliv-closure-code
          acceptance_test_id: test-ju-anticommutation
          reference_id: ref-krasnov2019
    claim-ju-grade:
      status: passed
      summary: "J_u is Clifford grade 2+3 mixed. Grade 2: 4 nonzero coefficients (all 0.25, subsets {1,8},{2,4},{3,7},{5,6}). Grade 3: 4 nonzero coefficients (one 0.75 and three -0.25, subsets {0,1,8},{0,2,4},{0,3,7},{0,5,6}). J_u first appears at depth 2 (residual drops from 3.46 to 6.99e-15)."
      linked_ids: [deliv-closure-code, deliv-closure-tests, test-ju-grade-decomp, test-ju-depth, ref-krasnov2019, ref-boyle2020]
      evidence:
        - verifier: gpd-executor
          method: Clifford grade decomposition via linear solve + depth tracking
          confidence: high
          claim_id: claim-ju-grade
          deliverable_id: deliv-closure-code
          acceptance_test_id: test-ju-grade-decomp
          reference_id: ref-krasnov2019
  deliverables:
    deliv-closure-code:
      status: passed
      path: "code/octonion_algebra.py"
      summary: "Functions added: rescale_to_clifford_generators, compute_associative_closure, compute_volume_element, compute_ju_anticommutation, compute_grade_decomposition, find_ju_depth"
      linked_ids: [claim-algv03-closure, claim-repr01-clifford, claim-ju-anticommutation, claim-ju-grade]
    deliv-closure-tests:
      status: passed
      path: "tests/test_observable_algebra.py"
      summary: "29 tests: closure (5), volume element (3), J_u anticommutation (4), grade decomposition (6), J_u depth (5), cross-validation (2), Phase 28 regression (4)"
      linked_ids: [claim-algv03-closure, claim-repr01-clifford, claim-ju-anticommutation, claim-ju-grade]
  acceptance_tests:
    test-closure-dim-256:
      status: passed
      summary: "SVD rank at convergence = 256. Singular value gap verified (rank is exact integer from SVD threshold 1e-10). Confirms Cl(9,0) irrep fills M_16(R)."
      linked_ids: [claim-algv03-closure, deliv-closure-code, deliv-closure-tests, ref-lawson-michelsohn]
    test-closure-growth:
      status: passed
      summary: "Dimension sequence 10 -> 46 -> 130 -> 256 -> 256 is monotonically non-decreasing, terminates at 256. Growth matches Clifford grading structure."
      linked_ids: [claim-algv03-closure, deliv-closure-code, deliv-closure-tests]
    test-volume-element:
      status: passed
      summary: "omega^2 - I = 0 (exact zero error). All 16 eigenvalues of omega are +1. Identifies P_+ factor of Cl(9,0) = M_16(R) + M_16(R)."
      linked_ids: [claim-repr01-clifford, deliv-closure-code, deliv-closure-tests, ref-lawson-michelsohn]
    test-ju-anticommutation:
      status: passed
      summary: "gamma_1: |{J_u,gamma}| = 8.0 (commutes). gamma_2..9: |{J_u,gamma}| in {4.0, 6.93} (neither commutes nor anticommutes). No ambiguous cases (all norms > 0.1 or < 1e-14)."
      linked_ids: [claim-ju-anticommutation, deliv-closure-code, deliv-closure-tests, ref-krasnov2019]
    test-ju-grade-decomp:
      status: passed
      summary: "Reconstruction error = 0.0 (exact). Nonzero grades: 2 (4 coefficients, norm 0.5) and 3 (4 coefficients, norm 0.866). J_u is grade 2+3 mixed."
      linked_ids: [claim-ju-grade, deliv-closure-code, deliv-closure-tests]
    test-ju-depth:
      status: passed
      summary: "J_u depth = 2. Residual at depth 1 = 3.46 (outside). Residual at depth 2 = 6.99e-15 (inside). Sharp transition confirmed."
      linked_ids: [claim-ju-grade, deliv-closure-code, deliv-closure-tests]
  references:
    ref-lawson-michelsohn:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cl(9,0) = M_16(R) + M_16(R) confirmed by computing dim(closure) = 256. Volume element omega = +I confirms irrep uses P_+ factor."
    ref-krasnov2019:
      status: completed
      completed_actions: [compare]
      missing_actions: [read]
      summary: "J_u from Krasnov's construction is NOT a 10th Clifford generator. It is a grade 2+3 element, first appearing at depth 2 in the associative closure."
    ref-boyle2020:
      status: completed
      completed_actions: [compare]
      missing_actions: []
      summary: "Boyle's S_{10}^+|_{Spin(9)} = S_9^C branching does NOT apply in the naive sense: J_u does not anticommute with all gamma_i, so it cannot serve as the 10th generator of Cl(10) restricted to the chiral spinor."
    ref-phase28:
      status: completed
      completed_actions: [use]
      missing_actions: []
      summary: "All 10 T_b matrices, Clifford anticommutation, J_u matrix, 46-dim Lie algebra used as input. 34 Phase 28 tests pass as regression."
  forbidden_proxies:
    fp-trivial-containment:
      status: rejected
      notes: "The algebra IS all of M_16(R), so J_u containment is trivially true. The meaningful content is the GRADE structure (2+3) and the DEPTH (2), not the binary answer."
    fp-wrong-signature:
      status: rejected
      notes: "Cl(9,0) with gamma_i^2 = +I used throughout. Verified numerically."
    fp-assumed-anticommutation:
      status: rejected
      notes: "J_u anticommutation computed explicitly. Result: J_u does NOT anticommute with all gamma_i. This was the single most important computation in the plan."
  uncertainty_markers:
    weakest_anchors:
      - "The interpretation of J_u's grade 2+3 structure in terms of Boyle/Krasnov physics (S_{10}^+ branching, SM gauge group) requires deeper analysis (Plan 02)."
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations:
      - "J_u does NOT anticommute with all gamma_i, contradicting the naive expectation from Boyle's 'S_{10}^+|_{Spin(9)} = S_9^C' picture where J_u would be a 10th Clifford generator."

comparison_verdicts:
  - subject_id: claim-algv03-closure
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-lawson-michelsohn
    comparison_kind: benchmark
    metric: dimension
    threshold: "= 256"
    verdict: pass
    recommended_action: "Proceed to Plan 02 for REPR-02 verdict."
    notes: "Exact match. Cl(9,0) = M_16(R) + M_16(R); irrep on R^16 fills M_16(R)."
  - subject_id: claim-ju-anticommutation
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-krasnov2019
    comparison_kind: benchmark
    metric: anticommutation_pattern
    threshold: "Each |{J_u, gamma_i}| either < 1e-14 or > 0.1"
    verdict: pass
    recommended_action: "Re-evaluate Boyle/Krasnov interpretation in light of mixed pattern."
    notes: "J_u commutes with gamma_1; mixed relation with gamma_2..9. NOT a 10th generator."

duration: 12min
completed: 2026-03-29
---

# Phase 29, Plan 01: Observable Algebra Characterization and J_u Clifford Structure

**Associative closure of Peirce operators is all of M_16(R) (256-dim); J_u is NOT a 10th Clifford generator (mixed grade 2+3, commutes with gamma_1); enters closure at depth 2**

## Performance

- **Duration:** 12 min
- **Started:** 2026-03-29T16:34:24Z
- **Completed:** 2026-03-29T16:46:00Z
- **Tasks:** 2
- **Files modified:** 2

## Key Results

- **ALGV-03 CONFIRMED:** Associative closure of {T_b} = M_16(R) (dim 256). Dimension growth: 10 -> 46 -> 130 -> 256. [CONFIDENCE: HIGH]
- **Volume element:** omega = gamma_1...gamma_9 = +I_{16} (all eigenvalues +1, zero error). Identifies P_+ factor of Cl(9,0). [CONFIDENCE: HIGH]
- **J_u is NOT a 10th Clifford generator:** J_u commutes with gamma_1, has mixed pattern with gamma_2..9. Does not anticommute with all gammas. [CONFIDENCE: HIGH]
- **J_u Clifford grade:** mixed grade 2+3. Grade 2: coefficient norm 0.5 (4 terms). Grade 3: coefficient norm 0.866 (4 terms, dominant). [CONFIDENCE: HIGH]
- **J_u depth:** enters associative closure at depth 2 (requires compositions of 3+ Peirce operators). [CONFIDENCE: HIGH]
- **J_u grade 2 subsets:** {1,8}, {2,4}, {3,7}, {5,6} (all coefficient 0.25). [CONFIDENCE: HIGH]
- **J_u grade 3 subsets:** {0,1,8} (coeff 0.75), {0,2,4}, {0,3,7}, {0,5,6} (all coeff -0.25). [CONFIDENCE: HIGH]

## Task Commits

1. **Task 1: Iterative associative closure, volume element, J_u diagnostics** - `0d28466` (compute)
2. **Task 2: Comprehensive test suite and cross-validation** - `9c578ca` (validate)

## Files Created/Modified

- `code/octonion_algebra.py` - Added: rescale_to_clifford_generators, compute_associative_closure, compute_volume_element, compute_ju_anticommutation, compute_grade_decomposition, find_ju_depth
- `tests/test_observable_algebra.py` - 29 tests: closure (5), volume element (3), J_u anticommutation (4), grade decomposition (6), J_u depth (5), cross-validation (2), Phase 28 regression (4)

## Next Phase Readiness

- ALGV-03 settled: the observable algebra is ALL of M_16(R). This is necessary but NOT sufficient for physical "forcing" of complex structure.
- J_u's grade 2+3 structure determines its position in the Clifford algebra. Plan 02 will evaluate what this means for REPR-02 (whether algebraic containment constitutes physical forcing).
- The key finding -- J_u does NOT anticommute with all gamma_i -- means the naive Boyle/Krasnov interpretation (J_u as 10th Clifford generator) does not apply directly. Plan 02 must address this.
- J_u depth = 2 means physical access to complex structure requires iterated measurements (compositions of 3+ Peirce operators), not single measurements.

## Contract Coverage

- Claim IDs advanced: claim-algv03-closure -> passed, claim-repr01-clifford -> passed, claim-ju-anticommutation -> passed, claim-ju-grade -> passed
- Deliverable IDs produced: deliv-closure-code -> code/octonion_algebra.py (passed), deliv-closure-tests -> tests/test_observable_algebra.py (passed)
- Acceptance test IDs run: test-closure-dim-256 -> passed, test-closure-growth -> passed, test-volume-element -> passed, test-ju-anticommutation -> passed, test-ju-grade-decomp -> passed, test-ju-depth -> passed
- Reference IDs surfaced: ref-lawson-michelsohn -> cite, ref-krasnov2019 -> compare, ref-boyle2020 -> compare, ref-phase28 -> use
- Forbidden proxies rejected: fp-trivial-containment, fp-wrong-signature, fp-assumed-anticommutation (all rejected)
- Decisive comparison verdicts: claim-algv03-closure vs ref-lawson-michelsohn -> pass; claim-ju-anticommutation vs ref-krasnov2019 -> pass

## Equations Derived

**Eq. (29-01.1): Clifford rescaling**

$$\gamma_1 = 4\,T_{b_1}, \quad \gamma_k = 2\,T_{b_k} \text{ for } k=2,\ldots,9 \quad \Rightarrow \quad \{\gamma_i, \gamma_j\} = 2\,\delta_{ij}\,I_{16}$$

**Eq. (29-01.2): Volume element**

$$\omega = \gamma_1 \gamma_2 \cdots \gamma_9 = +I_{16} \quad (\text{all eigenvalues } +1)$$

**Eq. (29-01.3): J_u Clifford decomposition**

$$J_u = \frac{1}{4}\bigl(\gamma_{28} + \gamma_{35} + \gamma_{48} + \gamma_{67}\bigr) + \frac{3}{4}\gamma_{129} - \frac{1}{4}\bigl(\gamma_{135} + \gamma_{148} + \gamma_{167}\bigr)$$

where $\gamma_{ij\cdots} = \gamma_i \gamma_j \cdots$ (ordered product) and indices are 1-based.

Note: using 0-based indexing as in the code, the grade-2 subsets are {1,8}, {2,4}, {3,7}, {5,6} and grade-3 subsets are {0,1,8}, {0,2,4}, {0,3,7}, {0,5,6}.

**Eq. (29-01.4): Associative closure dimension growth**

$$\dim(\text{Closure}_d) = 10, 46, 130, 256, 256, \ldots \quad (\text{converges at depth 3})$$

**Eq. (29-01.5): J_u depth**

$$J_u \in \text{Closure}_2 \setminus \text{Closure}_1 \quad (\text{first appears at depth 2})$$

## Validations Completed

- Associative closure dim = 256 (matches Lawson-Michelsohn Cl(9,0) = M_16(R) + M_16(R))
- Volume element omega^2 = I to zero error, all eigenvalues +1
- Volume element commutes with all gamma_i (verified: n=9 is odd)
- J_u anticommutation: no ambiguous norms (all < 1e-14 or > 0.1)
- Grade decomposition reconstruction: zero error for J_u, I, gammas, commutators
- Parseval relation: sum(c_S^2) = ||J_u||_F^2 / 16 verified to 1e-12
- Closure basis orthonormality: max |G - I| < 1e-10
- Phase 28 regression: all 34 tests pass

## Decisions Made

- Clifford rescaling gamma_1 = 4*T_b[1] determined from eigenvalue spectrum (T_b[1] eigenvalues +/-0.25, not +/-0.5 like T_b[2..9]). This resolves the indexing confusion in the plan's action text.
- Grade decomposition uses only grades 0-4 (256 independent monomials) since omega = +I identifies grade k with grade 9-k. The original implementation using all 512 monomials had a reconstruction error of 4.0 and was corrected.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Bug] Grade decomposition overcounting**

- **Found during:** Task 1, grade decomposition implementation
- **Issue:** Initial implementation summed over all 512 Clifford monomials, but omega = +I means grades k and 9-k are identified. This caused a reconstruction error of 4.0.
- **Fix:** Changed to use only 256 independent monomials (grades 0-4), solving a linear system instead of using the trace formula.
- **Files modified:** code/octonion_algebra.py
- **Verification:** Reconstruction error = 0.0 (exact)
- **Committed in:** 0d28466 (Task 1)

---

**Total deviations:** 1 auto-fixed (1 Rule 1 bug)
**Impact on plan:** Essential correctness fix. No scope creep.

## Issues Encountered

None beyond the auto-fixed deviation.

## Open Questions

- What does J_u's grade 2+3 structure mean physically? Grade-2 elements generate rotations (spin(9) subalgebra), grade-3 elements are beyond rotations.
- The grade-3 coefficients involve gamma_0 (= gamma_1 in 1-based indexing, the diagonal traceless operator). Since J_u commutes with gamma_1, the grade-3 part includes gamma_1 as a factor. Is this related to the block-diagonal structure of J_u?
- Does the depth-2 requirement (iterated Peirce compositions) have a physical interpretation as "measurement sequences" in the self-modeling framework?

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
| --- | --- | --- | --- | --- | --- |
| Closure dimension | dim(Cl) | 256 | exact | SVD rank | V_{1/2} |
| omega eigenvalues | - | all +1 | exact | eigvalsh | - |
| omega^2 error | - | 0.0 | exact | Frobenius norm | - |
| J_u depth | d | 2 | exact | lstsq residual | - |
| J_u residual at depth 1 | - | 3.46 | exact | lstsq | - |
| J_u residual at depth 2 | - | 6.99e-15 | exact | lstsq | - |
| Grade 2 norm | - | 0.500 | exact | linear solve | - |
| Grade 3 norm | - | 0.866 | exact | linear solve | - |

---

_Phase: 29-observable-algebra-and-representation-theory, Plan: 01_
_Completed: 2026-03-29_
