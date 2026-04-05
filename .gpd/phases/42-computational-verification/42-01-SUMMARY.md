---
phase: 42-computational-verification
plan: 01
depth: full
one-liner: "Verified sqrt(T_a) T_b sqrt(T_a) = (i/2)*T_b for all 72 anticommuting Cl(9,0) pairs via SymPy exact proof and NumPy numerical check -- GO for sequential product route"
subsystem: [validation, numerics]
tags: [clifford-algebra, sequential-product, complexification, matrix-sqrt, sympy-exact]

requires:
  - phase: 29
    provides: "9 uniformly-normalized Cl(9,0) generators T_a in M_16(R) via get_traceless_generators()"
provides:
  - "GO verdict: sequential product exits M_16(R) into M_16(C) for all 72 anticommuting pairs"
  - "Diagonal control: sqrt(T_a) T_a sqrt(T_a) = (1/4)*I_16 for all 9 pairs"
  - "Effect algebra control: E_a E_b E_a = (1/2)*E_a stays real for all 72 pairs"
  - "Self-contained verification script code/verify_sequential_product.py"
affects: [43-axiom-derivation, 44-formal-proof, gap-c-closure]

methods:
  added: [closed-form-matrix-sqrt, sympy-exact-rational-verification, exhaustive-pair-enumeration]
  patterns: [numpy-sympy-dual-verification, frobenius-norm-tolerance-checking]

key-files:
  created:
    - code/verify_sequential_product.py

key-decisions:
  - "Used closed-form sqrt(T_a) = ((1+i)I + (1-i)2T_a)/(2*sqrt(2)) instead of eigendecomposition or sqrtm"
  - "Used SymPy Rational conversion (not Float) for exact algebraic proof"
  - "Principal branch convention: Re(sqrt(z)) >= 0"

patterns-established:
  - "Dual NumPy+SymPy verification pattern for algebraic identities on small matrices"
  - "Exhaustive pair enumeration with per-pair error tracking and aggregate statistics"

conventions:
  - "Cl(9,0): {T_a, T_b} = (1/2)*delta_{ab}*I_16"
  - "Sequential product: a & b = sqrt(a) b sqrt(a)"
  - "Effect: E_a = (I + 2*T_a)/2"
  - "Sqrt branch: principal, Re(sqrt(z)) >= 0"
  - "Units: dimensionless (pure algebra)"

plan_contract_ref: ".gpd/phases/42-computational-verification/42-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-offdiag-identity:
      status: passed
      summary: "sqrt(T_a) T_b sqrt(T_a) = (i/2)*T_b verified for all 72 anticommuting pairs: NumPy max error 2.23e-16, SymPy exact zero for all 72"
      linked_ids: [deliv-script, test-offdiag-numpy, test-offdiag-sympy, test-imag-nonzero, ref-T-matrices, ref-sqrt-formula, ref-gudder-greechie]
      evidence:
        - verifier: self
          method: "NumPy Frobenius norm + SymPy exact algebraic verification"
          confidence: high
          claim_id: claim-offdiag-identity
          deliverable_id: deliv-script
          acceptance_test_id: test-offdiag-numpy
    claim-diag-identity:
      status: passed
      summary: "sqrt(T_a) T_a sqrt(T_a) = (1/4)*I_16 verified for all 9 diagonal pairs: NumPy max error 2.23e-16, SymPy exact zero"
      linked_ids: [deliv-script, test-diag, ref-T-matrices, ref-sqrt-formula]
    claim-effect-real:
      status: passed
      summary: "E_a E_b E_a = (1/2)*E_a for all 72 off-diagonal pairs, max error 0.00e+00, imaginary norm 0.00e+00 exactly"
      linked_ids: [deliv-script, test-effect-identity, test-effect-real, ref-T-matrices]
    claim-exit-real:
      status: passed
      summary: "Im(sqrt(T_a) T_b sqrt(T_a)) nonzero for all 72 pairs: min ||Im||_F = 1.000000, max ||Re||_F = 2.24e-17"
      linked_ids: [deliv-script, test-imag-nonzero, ref-T-matrices, ref-sqrt-formula]
  deliverables:
    deliv-script:
      status: passed
      path: "code/verify_sequential_product.py"
      summary: "Self-contained Python script with all 6 sections, dual NumPy+SymPy verification for all 153 pairs"
      linked_ids: [claim-offdiag-identity, claim-diag-identity, claim-effect-real, claim-exit-real]
  acceptance_tests:
    test-precondition:
      status: passed
      summary: "81/81 anticommutation pairs: max Frobenius error 0.00e+00 (exact zeros)"
      linked_ids: [ref-T-matrices, ref-clifford-anticomm]
    test-sqrt-sanity:
      status: passed
      summary: "9/9 sqrt(T_a)^2 = T_a: max error 4.46e-16"
      linked_ids: [ref-sqrt-formula]
    test-offdiag-numpy:
      status: passed
      summary: "72/72 off-diagonal pairs: max Frobenius error 2.23e-16"
      linked_ids: [claim-offdiag-identity, deliv-script]
    test-offdiag-sympy:
      status: passed
      summary: "72/72 off-diagonal pairs: SymPy simplify yields exact zero matrix for all"
      linked_ids: [claim-offdiag-identity, deliv-script]
    test-imag-nonzero:
      status: passed
      summary: "72/72 pairs: min ||Im||_F = 1.000000 (well above 0.5 threshold)"
      linked_ids: [claim-exit-real, deliv-script]
    test-diag:
      status: passed
      summary: "9/9 diagonal pairs: max Frobenius error 2.23e-16"
      linked_ids: [claim-diag-identity]
    test-effect-identity:
      status: passed
      summary: "72/72 effect pairs: max Frobenius error 0.00e+00 (exact)"
      linked_ids: [claim-effect-real]
    test-effect-real:
      status: passed
      summary: "72/72 effect pairs: max imaginary Frobenius norm 0.00e+00 (exactly real)"
      linked_ids: [claim-effect-real]
  references:
    ref-T-matrices:
      status: completed
      completed_actions: [read]
      missing_actions: []
      summary: "Loaded 9 generators via get_traceless_generators(); all entries exactly +/-1/2 or 0"
    ref-sqrt-formula:
      status: completed
      completed_actions: [compare]
      missing_actions: []
      summary: "Closed-form sqrt verified via sqrt^2=T_a (NumPy 4.46e-16, SymPy exact)"
    ref-gudder-greechie:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Sequential product definition a & b = sqrt(a) b sqrt(a) from Gudder-Greechie 2002"
    ref-clifford-anticomm:
      status: completed
      completed_actions: [compare]
      missing_actions: []
      summary: "Anticommutation {T_a,T_b}=(1/2)*delta_{ab}*I_16 verified for all 81 pairs, max error 0.00e+00"
  forbidden_proxies:
    fp-partial:
      status: rejected
      notes: "All 72 anticommuting pairs checked exhaustively, not a subset"
    fp-spotcheck:
      status: rejected
      notes: "All 9 generators used, all 72 off-diagonal pairs enumerated systematically"
    fp-numpy-only:
      status: rejected
      notes: "SymPy exact verification included alongside NumPy numerical checks"
    fp-wrong-sqrt:
      status: rejected
      notes: "Used closed-form formula exclusively; no fisher_metric._matrix_sqrt or scipy.linalg.sqrtm"
  uncertainty_markers:
    weakest_anchors:
      - "Branch choice for sqrt(T_a): principal branch gives +i. Opposite branch gives -i. EXISTENCE of imaginary part is branch-independent."
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations: []

comparison_verdicts:
  - subject_id: claim-offdiag-identity
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-sqrt-formula
    comparison_kind: benchmark
    metric: frobenius_norm
    threshold: "< 1e-14"
    verdict: pass
    recommended_action: "Proceed to Phase 43"
    notes: "NumPy max error 2.23e-16, SymPy exact zero. Well within tolerance."
  - subject_id: claim-exit-real
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-T-matrices
    comparison_kind: benchmark
    metric: imaginary_frobenius_norm
    threshold: "> 0.5"
    verdict: pass
    recommended_action: "Complexification confirmed for all 72 pairs"
    notes: "min ||Im||_F = 1.000000, confirming explicit exit from M_16(R)"

duration: 2min
completed: 2026-04-05
---

# Phase 42, Plan 01: Sequential Product Verification Summary

**Verified sqrt(T_a) T_b sqrt(T_a) = (i/2)*T_b for all 72 anticommuting Cl(9,0) pairs via SymPy exact proof and NumPy numerical check -- GO for sequential product route**

## Performance

- **Duration:** 2 min
- **Started:** 2026-04-05T01:33:55Z
- **Completed:** 2026-04-05T01:36:04Z
- **Tasks:** 2
- **Files created:** 1

## Key Results

- **GO verdict**: Sequential product exits M_16(R) into M_16(C) for all 72 anticommuting Cl(9,0) generator pairs [CONFIDENCE: HIGH]
- sqrt(T_a) T_b sqrt(T_a) = (i/2)*T_b: NumPy max error 2.23e-16, SymPy exact zero for all 72 pairs [CONFIDENCE: HIGH]
- sqrt(T_a) T_a sqrt(T_a) = (1/4)*I_16: NumPy max error 2.23e-16, SymPy exact zero for all 9 diagonal pairs [CONFIDENCE: HIGH]
- Effect algebra E_a E_b E_a = (1/2)*E_a: max error 0.00e+00, imaginary part 0.00e+00 (exactly real) for all 72 pairs [CONFIDENCE: HIGH]

## Task Commits

1. **Task 1: Write exhaustive verification script** - `f36c788` (implement)
2. **Task 2: Execute verification and confirm GO/NO-GO** - no file changes (validation only, results above)

## Files Created/Modified

- `code/verify_sequential_product.py` - Self-contained verification of all 153 Cl(9,0) sequential product pairs (72 off-diagonal + 9 diagonal + 72 effect)

## Next Phase Readiness

- GO verdict confirmed: proceed to Phase 43 (Axiom Derivation)
- Verification script available for re-execution at any time
- All 4 roadmap success criteria met

## Contract Coverage

- Claim IDs advanced: claim-offdiag-identity -> passed, claim-diag-identity -> passed, claim-effect-real -> passed, claim-exit-real -> passed
- Deliverable IDs produced: deliv-script -> code/verify_sequential_product.py (passed)
- Acceptance test IDs run: test-precondition -> passed, test-sqrt-sanity -> passed, test-offdiag-numpy -> passed, test-offdiag-sympy -> passed, test-imag-nonzero -> passed, test-diag -> passed, test-effect-identity -> passed, test-effect-real -> passed
- Reference IDs surfaced: ref-T-matrices -> read, ref-sqrt-formula -> compare, ref-gudder-greechie -> cite, ref-clifford-anticomm -> compare
- Forbidden proxies rejected: fp-partial, fp-spotcheck, fp-numpy-only, fp-wrong-sqrt (all rejected)
- Decisive comparison verdicts: claim-offdiag-identity -> pass (2.23e-16 < 1e-14), claim-exit-real -> pass (1.0 > 0.5)

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
| --- | --- | --- | --- | --- | --- |
| Off-diagonal identity max error | err_offdiag | 2.23e-16 | exact (SymPy zero) | NumPy float64 | All 72 pairs |
| Diagonal identity max error | err_diag | 2.23e-16 | exact (SymPy zero) | NumPy float64 | All 9 pairs |
| Min imaginary Frobenius norm | min_Im_F | 1.000000 | exact | NumPy float64 | All 72 pairs |
| Max real Frobenius norm (off-diag) | max_Re_F | 2.24e-17 | machine epsilon | NumPy float64 | All 72 pairs |
| Effect algebra max error | err_effect | 0.00e+00 | exact (0.0) | NumPy float64 | All 72 pairs |
| Effect algebra max imaginary norm | max_Im_effect | 0.00e+00 | exact (0.0) | NumPy float64 | All 72 pairs |
| Anticommutation precondition error | err_precond | 0.00e+00 | exact (0.0) | NumPy float64 | All 81 pairs |
| Sqrt sanity max error | err_sqrt | 4.46e-16 | machine epsilon | NumPy float64 | All 9 generators |

## Validations Completed

- Precondition: {T_a, T_b} = (1/2)*delta_{ab}*I_16 for all 81 pairs (max error 0.00e+00)
- Sqrt sanity: sqrt(T_a)^2 = T_a for all 9 generators (max error 4.46e-16)
- Off-diagonal identity: 72/72 pairs to 2.23e-16 (NumPy) and exact zero (SymPy)
- Diagonal identity: 9/9 pairs to 2.23e-16 (NumPy) and exact zero (SymPy)
- Effect algebra: 72/72 pairs to 0.00e+00 (exact)
- Imaginary exit: min ||Im||_F = 1.000000 across all 72 off-diagonal pairs
- Real part vanishing: max ||Re||_F = 2.24e-17 across all 72 off-diagonal pairs
- Cross-method agreement: SymPy algebraic proof confirms NumPy numerical result for all 81 sequential product pairs
- Exhaustiveness: 72 + 9 + 72 = 153 total pairs checked, zero exceptions

## Decisions Made

- Used closed-form sqrt formula (not eigendecomposition) -- simpler, exact, and avoids branch ambiguity
- Used SymPy Rational conversion for exact verification -- proof-level certainty
- Principal branch convention for sqrt -- consistent with standard complex analysis

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

None.

## Self-Check: PASSED

- [x] code/verify_sequential_product.py exists and runs
- [x] Commit f36c788 exists
- [x] Exit code 0 on successful run
- [x] All 153 pairs verified (72 + 9 + 72)
- [x] Convention consistency: Cl(9,0) normalization used throughout
- [x] All 4 contract claims passed
- [x] All 8 acceptance tests passed
- [x] All 4 references surfaced
- [x] All 4 forbidden proxies rejected

---

_Phase: 42-computational-verification, Plan: 01_
_Completed: 2026-04-05_
