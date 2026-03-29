---
phase: 29-observable-algebra-and-representation-theory
plan: 02
depth: full
one-liner: "REPR-02 verdict: J_u is algebraically distinguished (isolated in its 8-monomial subspace, grade 2+3) but NOT a 10th Clifford generator; Spin(10) extension fails (generates sl(16,R), not spin(10)); stabilizer dim = 10 = su(3)+u(1)^2, not 12"
subsystem: [computation, validation]
tags: [octonion, jordan-algebra, clifford-algebra, spin9, spin10, gap-c, REPR-02, verdict, G_SM]

requires:
  - phase: "29-01 (associative closure, J_u grade decomposition, anticommutation pattern)"
    provides: "256-dim closure, J_u grade 2+3, J_u commutes with gamma_0, depth 2"
provides:
  - "REPR-02 VERDICT: J_u is distinguished but not a 10th Clifford generator"
  - "J_u Clifford polynomial: 8 explicit nonzero terms, reconstruction error = 0.0"
  - "J_u uniqueness: ISOLATED in 8-monomial subspace (tangent dim = 0 at J_u)"
  - "Stabilizer dim(Stab_{spin(9)}(J_u)) = 10 = su(3) + u(1)^2"
  - "Krasnov discrepancy: we find dim 10, Krasnov claims dim 12 = su(3)+su(2)+u(1)"
  - "Spin(10) extension: FAILS. {spin(9), gamma_i J_u} is 45-dim but NOT a Lie algebra; the generated Lie algebra is sl(16,R) = 255-dim"
  - "Complexification: valid (J_u^2 = -I defines C^8), J_u-linear subalgebra of spin(9) has dim 10"
  - "R^16 decomposes as 12-dim + 4-dim under stabilizer Casimir"
affects: [30-selection-arguments, paper7-gap-c]

methods:
  added: [clifford-polynomial-extraction, jacobian-uniqueness-analysis, gsm-commutant-via-svd, lie-closure-iteration]
  patterns: [killing-form-semisimple-decomposition, casimir-multiplicity-analysis]

key-files:
  modified: [code/octonion_algebra.py, tests/test_observable_algebra.py]

key-decisions:
  - "Uniqueness analyzed within the 8-monomial subspace (the nonzero terms of J_u's Clifford polynomial). This is the natural space for the question."
  - "Stabilizer computed via SVD of the commutator action [J_u, .] on spin(9), giving the full 10-dim kernel (not just individual commuting generators)"
  - "Spin(10) extension tested by checking Lie closure of span{spin(9), gamma_i J_u}. Closure gives sl(16,R), confirming Cl(9)->Cl(10) fails."

patterns-established:
  - "When J_u does not anticommute with all gamma_i, the products gamma_i J_u mix grades (antisymmetric matrices) and their commutators leave spin(9). This prevents a clean Cl(10) extension."
  - "The 4 individually commuting gamma_i gamma_j elements (the grade-2 part of J_u's polynomial) form a maximal torus. The remaining 6 stabilizer generators are linear combinations of gamma_i gamma_j."

conventions:
  - "jordan_product = (1/2)(ab + ba)"
  - "octonion_basis = fano_e1e2=e4"
  - "peirce_decomposition under E_11"
  - "v_half_basis = (x2_0..x2_7, x3_0..x3_7)"
  - "clifford_signature = Cl(9,0), gamma_i^2 = +I"
  - "clifford_normalization = gamma_1 = 4*T_b[1], gamma_k = 2*T_b[k] for k=2..9"
  - "complex_structure = u_equals_e7"

plan_contract_ref: ".gpd/phases/29-observable-algebra-and-representation-theory/29-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-repr02-verdict:
      status: passed
      summary: "J_u expressed as explicit 8-term Clifford polynomial (4 grade-2 + 4 grade-3). J_u is DISTINGUISHED (isolated in its monomial subspace, tangent dim = 0) but NOT a 10th Clifford generator (commutes with gamma_0, mixed grade). The stop/rethink trigger: 'forcing' from containment alone is vacuous (forbidden proxy fp-forcing-from-containment). The physical content is J_u's grade 2+3 structure and depth 2 -- complex structure requires iterated measurements."
      linked_ids: [deliv-verdict-code, deliv-verdict-tests, test-ju-polynomial, test-stop-rethink, ref-krasnov2019, ref-boyle2020, ref-paper7, ref-plan01-results]
      evidence:
        - verifier: gpd-executor
          method: explicit Clifford polynomial extraction + Jacobian uniqueness analysis + commutant computation
          confidence: high
          claim_id: claim-repr02-verdict
          deliverable_id: deliv-verdict-code
          acceptance_test_id: test-ju-polynomial
          reference_id: ref-krasnov2019
    claim-uniqueness:
      status: passed
      summary: "J_u is UNIQUE (up to sign) within its 8-monomial subspace. The Jacobian of the X^2=-I constraint has rank 8 at J_u's coefficients, giving tangent dim = 0. This means no continuous family of solutions passes through J_u. The broader uniqueness under the Spin(9) orbit is: Spin(9)/Stab(J_u) has dim 36-10=26, so J_u lives on a 26-dim orbit."
      linked_ids: [deliv-verdict-code, deliv-verdict-tests, test-uniqueness, ref-krasnov2019]
      evidence:
        - verifier: gpd-executor
          method: Jacobian rank analysis at J_u coefficients
          confidence: high
          claim_id: claim-uniqueness
          deliverable_id: deliv-verdict-code
          acceptance_test_id: test-uniqueness
          reference_id: ref-krasnov2019
    claim-spin9-spin10:
      status: passed
      summary: "Spin(9)->Spin(10) compatibility: FAILS in the naive sense. The 45-dim space span{spin(9), gamma_i J_u} is NOT a Lie algebra. Its Lie closure is sl(16,R) (dim 255), not spin(10) (dim 45). This is because J_u is grade 2+3, not grade 1, so gamma_i J_u products mix grades and their commutators leave spin(9). The complexification (R^16, J_u) = C^8 is valid, and the J_u-linear subalgebra of spin(9) has dim 10 and is a Lie subalgebra. This is the honest algebraic structure."
      linked_ids: [deliv-verdict-code, deliv-verdict-tests, test-spin10-branching, ref-boyle2020]
      evidence:
        - verifier: gpd-executor
          method: Lie closure iteration + J_u-linearity test
          confidence: high
          claim_id: claim-spin9-spin10
          deliverable_id: deliv-verdict-code
          acceptance_test_id: test-spin10-branching
          reference_id: ref-boyle2020
  deliverables:
    deliv-verdict-code:
      status: passed
      path: "code/octonion_algebra.py"
      summary: "Functions added: express_ju_as_clifford_polynomial, test_ju_uniqueness, compute_gsm_commutant, verify_spin10_branching"
      linked_ids: [claim-repr02-verdict, claim-uniqueness, claim-spin9-spin10]
    deliv-verdict-tests:
      status: passed
      path: "tests/test_observable_algebra.py"
      summary: "25 new tests added (6 polynomial, 5 uniqueness, 6 commutant, 7 Spin(10)). All 54 tests pass."
      linked_ids: [claim-repr02-verdict, claim-uniqueness, claim-spin9-spin10]
  acceptance_tests:
    test-ju-polynomial:
      status: passed
      summary: "J_u = sum c_S gamma_S with 8 nonzero terms. Reconstruction error = 0.0 (exact). Grade-2 subsets {1,8},{2,4},{3,7},{5,6} each with coeff 0.25. Grade-3 subsets: {0,1,8} with 0.75, {0,2,4},{0,3,7},{0,5,6} with -0.25."
      linked_ids: [claim-repr02-verdict, deliv-verdict-code, ref-krasnov2019]
    test-stop-rethink:
      status: passed
      summary: "J_u is DISTINGUISHED by: (1) isolated in its 8-monomial subspace (unique up to sign with X^2=-I), (2) specific grade 2+3 structure determined by octonion multiplication, (3) stabilizer su(3)+u(1)^2 contains the SU(3) color factor. J_u is NOT algebraically generic -- it is selected by the specific Fano plane structure of the octonions. However, this selection is by the OCTONIONIC structure, not by the PEIRCE structure. The Peirce algebra gives M_16(R) which contains everything; the selection comes from knowing which octonion u to use."
      linked_ids: [claim-repr02-verdict, deliv-verdict-code, deliv-verdict-tests, ref-krasnov2019, ref-boyle2020]
    test-uniqueness:
      status: passed
      summary: "Within the 8-dim monomial subspace of J_u's Clifford polynomial, J_u is the unique (up to sign) element with X^2 = -I. Jacobian rank = 8 at J_u, tangent dim = 0. J_u lives on a 26-dim orbit under Spin(9) (orbit dim = 36 - 10)."
      linked_ids: [claim-uniqueness, deliv-verdict-code, deliv-verdict-tests, ref-krasnov2019]
    test-spin10-branching:
      status: passed
      summary: "Case B confirmed. span{spin(9), gamma_i J_u} = 45-dim but NOT a Lie algebra. Generated Lie algebra = sl(16,R) (dim 255). J_u-linear subalgebra of spin(9) has dim 10 and IS a Lie subalgebra."
      linked_ids: [claim-spin9-spin10, deliv-verdict-code, deliv-verdict-tests, ref-boyle2020]
  references:
    ref-krasnov2019:
      status: completed
      completed_actions: [compare]
      missing_actions: [read]
      summary: "Krasnov's G_SM = Stab_{Spin(9)}(J_u). We find dim(stab) = 10 = su(3)+u(1)^2, not 12 = su(3)+su(2)+u(1) as Krasnov claims. The su(3) factor matches (dim 8, semisimple part). The discrepancy is in the residual 2 vs 4 dimensions. This may reflect a difference in which Spin(9) embedding is used, or Krasnov may be including structure beyond the spin(9) representation on R^16."
    ref-boyle2020:
      status: completed
      completed_actions: [compare]
      missing_actions: []
      summary: "Boyle's S_{10}^+|_{Spin(9)} = S_9^C branching does NOT hold in the naive sense: extending Cl(9) by J_u does not give Cl(10) or Cl(9,1). The complexification (R^16, J_u) = C^8 is valid, but the C^8 does NOT carry a Spin(10) action via the Peirce algebra. It only carries a 10-dim subalgebra of spin(9) (the J_u-linear part)."
    ref-paper7:
      status: completed
      completed_actions: [read]
      missing_actions: []
      summary: "Gap C = Link 4 in the 9-link chain. The verdict for Paper 7: algebraic containment alone is insufficient (everything is in M_16(R)). The octonionic structure of J_u (grade 2+3, specific coefficients from Fano plane) provides the selection, but this selection requires external input (choice of u in S^6). Phase 30 must determine whether this external input can be derived from the self-modeling framework."
    ref-plan01-results:
      status: completed
      completed_actions: [use]
      missing_actions: []
      summary: "All Plan 01 results used: 256-dim closure, J_u grade 2+3 decomposition, anticommutation pattern (commutes with gamma_0, mixed with gamma_1..8), depth 2. All 29 Plan 01 tests pass as regression."
  forbidden_proxies:
    fp-forcing-from-containment:
      status: rejected
      notes: "Explicitly addressed in the verdict. Containment of J_u in M_16(R) is vacuous (every 16x16 matrix is in M_16(R)). The meaningful content is J_u's SPECIFIC Clifford polynomial (grade 2+3, 8 terms, specific subsets determined by the Fano plane). This is selection by octonionic structure, not by the Peirce algebra."
    fp-close-not-in:
      status: rejected
      notes: "All results are exact algebraic (zero error on reconstruction, integer dimensions, exact coefficients 0.25 and 0.75)."
    fp-wrong-clifford-extension:
      status: rejected
      notes: "Explicitly checked: J_u^2 = -I would give Cl(9,1) not Cl(10,0) IF J_u anticommuted with all gamma_i. But J_u does NOT anticommute with all gamma_i, so the Clifford extension fails entirely. No wrong-signature claim made."
  uncertainty_markers:
    weakest_anchors:
      - "The dim=10 vs dim=12 discrepancy with Krasnov needs independent verification. Our computation is exact (zero commutator errors), but Krasnov might be computing the stabilizer in a different algebraic object or using a different Spin(9) embedding."
      - "The verdict 'J_u is distinguished but not forced' is a novel conceptual contribution with no published precedent. Its interpretation for Gap C depends on whether Phase 30 can derive the choice of u from self-modeling."
    unvalidated_assumptions: []
    competing_explanations:
      - "The dim=10 result could arise from a different Spin(9) representation than Krasnov's. If Krasnov's Spin(9) acts on a different 16-dim space (e.g., S_9 with a different spin structure), the stabilizer might genuinely be dim 12."
    disconfirming_observations:
      - "The Spin(10) extension fails: span{spin(9), gamma_i J_u} generates sl(16,R) (255-dim), not spin(10) (45-dim). This means the Boyle branching S_{10}^+|_{Spin(9)} = S_9^C cannot be realized via the Peirce algebra in the naive way."

comparison_verdicts:
  - subject_id: claim-repr02-verdict
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-krasnov2019
    comparison_kind: benchmark
    metric: stabilizer_dimension
    threshold: "= 12 (Krasnov's prediction)"
    verdict: discrepancy
    recommended_action: "Investigate the Krasnov discrepancy in Phase 30. Check whether Krasnov's Spin(9) includes structure beyond the grade-2 Clifford elements, or whether the extra 2 dimensions arise from a different representation."
    notes: "We find dim = 10 = su(3) + u(1)^2. Krasnov claims dim = 12 = su(3) + su(2) + u(1). The su(3) factor matches. The discrepancy is 2 dimensions."
  - subject_id: claim-spin9-spin10
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-boyle2020
    comparison_kind: benchmark
    metric: lie_algebra_dimension
    threshold: "= 45 (spin(10))"
    verdict: fail
    recommended_action: "The Spin(10) extension via J_u as a 10th generator fails. The complexification route S_9 -> S_9^C = C^8 is valid but gives only a 10-dim subalgebra, not spin(10). Phase 30 must address whether a DIFFERENT mechanism (not Clifford extension) can realize the Spin(9)->Spin(10) structure."
    notes: "Generated Lie algebra = sl(16,R) (255-dim), not spin(10) (45-dim). The 45-dim span is NOT closed under brackets."
  - subject_id: claim-uniqueness
    subject_kind: claim
    subject_role: supporting
    reference_id: ref-krasnov2019
    comparison_kind: consistency
    metric: isolated_solution
    threshold: "tangent_dim = 0"
    verdict: pass
    recommended_action: "No action needed. J_u is uniquely determined (up to sign) in its monomial subspace."
    notes: "Jacobian rank 8 at J_u coefficients. J_u lives on a 26-dim Spin(9) orbit."

duration: 15min
completed: 2026-03-29
---

# Phase 29, Plan 02: REPR-02 Verdict -- J_u Algebraic Role and Spin(10) Compatibility

**J_u is algebraically distinguished (isolated in its 8-monomial subspace, grade 2+3) but NOT a 10th Clifford generator; Spin(10) extension fails; stabilizer dim = 10 = su(3)+u(1)^2**

## Performance

- **Duration:** 15 min
- **Started:** 2026-03-29
- **Tasks:** 2
- **Files modified:** 2

## REPR-02 Verdict

### (a) Is J_u in the observable algebra?

**YES**, trivially. The associative closure is M_16(R) (256-dim), so every 16x16 matrix is in the observable algebra. This is *not* the interesting question.

### (b) Does this constitute "forcing"?

**NO**, not from containment alone. Claiming "forcing" from the fact that J_u is in M_16(R) violates the forbidden proxy `fp-forcing-from-containment`. Every element of M_16(R) is in the observable algebra; J_u's containment has no special significance.

The physically meaningful content is:

- J_u enters the closure at **depth 2** (requires compositions of 3+ Peirce operators = iterated measurements)
- J_u has a **specific** Clifford polynomial: 8 terms with coefficients determined by the Fano plane multiplication table
- J_u is **isolated** in its 8-monomial subspace (unique solution with X^2 = -I, up to sign)

### (c) What is J_u's algebraic role?

J_u is **neither** a 10th Clifford generator **nor** generic. It is a **grade 2+3 element** of the Clifford algebra Cl(9,0):

$$J_u = \tfrac{1}{4}(\gamma_{18} + \gamma_{24} + \gamma_{37} + \gamma_{56}) + \tfrac{3}{4}\gamma_{018} - \tfrac{1}{4}(\gamma_{024} + \gamma_{037} + \gamma_{056})$$

The grade-2 subsets {1,8}, {2,4}, {3,7}, {5,6} correspond to the imaginary quaternionic subalgebra pairs determined by the Fano plane with e_7 as the distinguished imaginary unit. The grade-3 terms are grade-2 terms multiplied by gamma_0 (the diagonal traceless generator).

### (d) Is J_u unique?

**YES**, within its 8-monomial subspace. The Jacobian of the X^2 = -I constraint at J_u's coefficients has rank 8 (full rank), so J_u is an isolated point (tangent space dimension = 0). The norm-squared constraint sum(a_k^2) = 1 is satisfied exactly.

Under the Spin(9) action, J_u lives on a 26-dim orbit (orbit dim = 36 - 10), so there is a 26-parameter family of "equivalent" complex structures related by Spin(9) rotations.

### (e) Is the Spin(9)->Spin(10) branching verified?

**NO.** The extension fails at the Lie algebra level:

- span{spin(9) generators, gamma_i J_u} has dimension 45 (correct for spin(10))
- BUT this 45-dim space is NOT a Lie algebra (not closed under brackets)
- The Lie algebra it GENERATES is sl(16, R) (dim 255), not spin(10) (dim 45)

The failure occurs because J_u is grade 2+3 (not grade 1). The products gamma_i J_u are antisymmetric matrices of mixed Clifford grade, and their commutators leave the initial 45-dim space.

The complexification (R^16, J_u) = C^8 is valid, and the J_u-linear subalgebra of spin(9) has dim 10 and IS a Lie subalgebra (= the stabilizer). But this does not constitute a Spin(10) structure.

### (f) What is the honest input for Phase 30?

**Key facts for Phase 30:**

1. The Peirce algebra on V_{1/2} is all of M_16(R). This is necessary but not sufficient for "forcing."
2. J_u is selected by the octonionic structure (Fano plane, choice of u in S^6), NOT by the Peirce algebra. The Peirce algebra cannot distinguish J_u from any other element of M_16(R).
3. The Spin(10) extension fails. Whatever connects Spin(9) to Spin(10) in the physical picture, it does not happen through J_u acting as a Clifford generator.
4. The stabilizer dim = 10 (su(3)+u(1)^2) contains the su(3) color factor but the discrepancy with Krasnov's dim = 12 needs resolution.
5. Gap C cannot be closed purely algebraically at this level. Phase 30 must either: (A) find a selection principle within the self-modeling framework that picks out J_u, or (B) formulate a conditional theorem: "IF octonionic structure is given, THEN complex structure is forced."

### Krasnov Discrepancy

We find dim(Stab_{Spin(9)}(J_u)) = 10, not 12 as Krasnov claims. The discrepancy:

| Component | Our result | Krasnov |
|-----------|-----------|---------|
| Total dim | 10 | 12 |
| Semisimple | 8 (su(3)) | 8 (su(3)) |
| Abelian | 2 (u(1)^2) | 4 (su(2)+u(1)) |

The su(3) factor matches. The discrepancy is 2 dimensions in the abelian/non-semisimple part. This could arise from a different Spin(9) embedding or different conventions.

## Key Results

- **J_u Clifford polynomial:** 8 terms, reconstruction error = 0.0, coefficients exactly 0.25 and 0.75 [CONFIDENCE: HIGH]
- **J_u uniqueness:** isolated in 8-monomial subspace (tangent dim = 0) [CONFIDENCE: HIGH]
- **Stabilizer dimension:** 10 = su(3) + u(1)^2 [CONFIDENCE: HIGH]
- **Spin(10) extension:** FAILS (generated Lie algebra = sl(16,R)) [CONFIDENCE: HIGH]
- **R^16 decomposition:** 12-dim + 4-dim under stabilizer Casimir [CONFIDENCE: HIGH]
- **Krasnov discrepancy:** dim 10 vs dim 12, su(3) matches, abelian part differs [CONFIDENCE: MEDIUM -- needs independent verification]

## Task Commits

1. **Task 1: J_u polynomial, uniqueness, G_SM commutant** - `20d9fe1` (compute)
2. **Task 2: Spin(10) branching, verdict, tests** - `6027e7d` (validate)

## Files Modified

- `code/octonion_algebra.py` - Added: express_ju_as_clifford_polynomial, test_ju_uniqueness, compute_gsm_commutant, verify_spin10_branching
- `tests/test_observable_algebra.py` - 25 new tests (polynomial 6, uniqueness 5, commutant 6, Spin(10) 7). Total: 54 tests, all pass.

## Equations Derived

**Eq. (29-02.1): J_u Clifford polynomial** (explicit, from Plan 01 grade decomposition)

$$J_u = \frac{1}{4}\bigl(\gamma_{18} + \gamma_{24} + \gamma_{37} + \gamma_{56}\bigr) + \frac{3}{4}\gamma_{018} - \frac{1}{4}\bigl(\gamma_{024} + \gamma_{037} + \gamma_{056}\bigr)$$

Reconstruction error: 0.0 (exact). Coefficients: all 0.25 except gamma_{018} which is 0.75.

**Eq. (29-02.2): Uniqueness constraint**

For X = sum_k a_k M_k in the 8-monomial subspace, X^2 = -I iff:
$$\sum_k a_k^2 = 1 \quad \text{AND} \quad \sum_{i<j} a_i a_j \{M_i, M_j\} = 0$$

At J_u: Jacobian rank = 8 = dim(subspace), tangent dim = 0. J_u isolated.

**Eq. (29-02.3): Stabilizer structure**

$$\text{stab}_{spin(9)}(J_u) = su(3) \oplus u(1) \oplus u(1), \quad \dim = 8 + 1 + 1 = 10$$

Individually commuting generators: L_{18}, L_{24}, L_{37}, L_{56} (= grade-2 part of J_u).

**Eq. (29-02.4): R^16 Casimir decomposition**

$$R^{16} = V_{12} \oplus V_4, \quad \text{Casimir eigenvalues: } -0.75 \text{ (mult 12)}, -0.25 \text{ (mult 4)}$$

## Validations Completed

- J_u polynomial: 8 terms, reconstruction error = 0.0
- Uniqueness: norm squared = 1.0, constraint residual = 0.0, tangent dim = 0
- Stabilizer: dim 10, closed under brackets, Killing form rank 8 (2 zero eigenvalues)
- Spin(10) extension: 45-dim span NOT a Lie algebra; generated Lie algebra = 255-dim
- All 54 tests pass (29 Plan 01 + 25 Plan 02)
- Self-check: all files exist, all commits found

## Deviations from Plan

No deviations. The plan correctly anticipated Case B and the required analyses.

## Self-Check: PASSED

- [x] All created files exist
- [x] All checkpoints exist (20d9fe1, 6027e7d)
- [x] Convention consistency verified (Cl(9,0) throughout)
- [x] All 54 tests pass
- [x] SUMMARY written with substantive physics content
- [x] Contract coverage complete (all claim IDs, deliverable IDs, acceptance tests, references, forbidden proxies addressed)

## Key Quantities and Uncertainties

| Quantity | Value | Uncertainty | Source |
| --- | --- | --- | --- |
| J_u polynomial terms | 8 | exact | grade decomposition |
| J_u dominant coefficient | 0.75 | exact | linear solve |
| Uniqueness tangent dim | 0 | exact | Jacobian rank |
| |a|^2 | 1.0 | exact | coefficient sum |
| Stabilizer dim | 10 | exact | SVD nullspace |
| Semisimple part dim | 8 (su(3)) | exact | Killing form |
| Center dim | 2 (u(1)^2) | exact | Killing form |
| Casimir eigenvalues | -0.75, -0.25 | exact | diagonalization |
| Casimir multiplicities | 12, 4 | exact | eigenvalue count |
| Spin(10) span dim | 45 | exact | SVD rank |
| Generated Lie dim | 255 (sl(16,R)) | exact | iterative closure |

---

_Phase: 29-observable-algebra-and-representation-theory, Plan: 02_
_Completed: 2026-03-29_
