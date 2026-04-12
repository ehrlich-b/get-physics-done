---
phase: 46-v-0-algebraic-foundation-and-pi-u-projection
plan: 01
depth: full
one-liner: "Constructed pi_u: h_2(O) -> h_2(C_u) with verified Minkowski signature (1,3) and exact V_0 Peirce closure"
subsystem: [formalism, validation]
tags: [octonion, jordan-algebra, peirce-decomposition, minkowski-signature, projection]

requires:
  - phase: 28-peirce-verification-and-v-0-channel-exploration
    provides: Octonion class, H3O, jordan_product, peirce_V0/Vhalf/V1, V0_basis_elements
provides:
  - proj_u function (Octonion -> C_u projection, u = e_7)
  - pi_u function (h_2(O) -> h_2(C_u) projection)
  - det_2 quadratic form with signature (1,3) on h_2(C_u)
  - jordan_product_h2o (intrinsic h_2(O) Jordan product)
  - V_0 Peirce closure verified (intrinsic == inherited, zero leakage)
affects: [47-hamiltonian-and-equations-of-motion, 48-einstein-equation-derivation]

methods:
  added: [pi_u projection via C_u = span(1, e_7), det_2 quadratic form, intrinsic 2x2 Jordan product]
  patterns: [Gram matrix signature verification via polarization identity]

key-files:
  modified: [code/octonion_algebra.py]

key-decisions:
  - "No new decisions required -- followed plan exactly using locked conventions"

patterns-established:
  - "h_2(C_u) parametrization: x_0=(beta+gamma)/2, x_3=(beta-gamma)/2, x_1=Re(x1), x_2=x1.c[7]"
  - "det_2 = x_0^2 - x_1^2 - x_2^2 - x_3^2 (Minkowski norm via quadratic form)"

conventions:
  - "u = e_7 (complex structure)"
  - "jordan_product = (1/2)(AB + BA)"
  - "det_2 signature = (+,-,-,-) on h_2(C_u)"
  - "Fano: e_1 e_2 = e_4"

plan_contract_ref: ".gpd/phases/46-v-0-algebraic-foundation-and-pi-u-projection/46-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-signature:
      status: passed
      summary: "det_2 on pi_u(h_2(O)) = h_2(C_u) has Lorentzian signature (1,3); Gram matrix eigenvalues exactly {+1,-1,-1,-1}"
      linked_ids: [deliv-code, test-signature-gram, test-benchmarks, ref-baez]
      evidence:
        - verifier: gpd-executor
          method: Gram matrix eigenvalue computation
          confidence: high
          claim_id: claim-signature
          deliverable_id: deliv-code
          acceptance_test_id: test-signature-gram
          reference_id: ref-baez
    claim-peirce-closure:
      status: passed
      summary: "Intrinsic h_2(O) Jordan product closes exactly in V_0 for all 55 basis pairs; inherited h_3(O) product also closes with zero V_{1/2} leakage"
      linked_ids: [deliv-code, test-intrinsic-closure, test-inherited-comparison, ref-mccrimmon]
      evidence:
        - verifier: gpd-executor
          method: exhaustive basis pair computation
          confidence: high
          claim_id: claim-peirce-closure
          deliverable_id: deliv-code
          acceptance_test_id: test-intrinsic-closure
          reference_id: ref-mccrimmon
    claim-projection-properties:
      status: passed
      summary: "pi_u is idempotent (error 0) with 4-dimensional image h_2(C_u)"
      linked_ids: [deliv-code, test-idempotent, test-image-dim, ref-baez]
      evidence:
        - verifier: gpd-executor
          method: random element testing (10 elements) + basis rank computation
          confidence: high
          claim_id: claim-projection-properties
          deliverable_id: deliv-code
          acceptance_test_id: test-idempotent
          reference_id: ref-baez
  deliverables:
    deliv-code:
      status: passed
      path: "code/octonion_algebra.py"
      summary: "Extended with proj_u, pi_u, det_2, jordan_product_h2o -- all verified"
      linked_ids: [claim-signature, claim-peirce-closure, claim-projection-properties]
  acceptance_tests:
    test-signature-gram:
      status: passed
      summary: "Gram matrix G = diag(+1,-1,-1,-1) exactly; eigenvalues {+1,-1,-1,-1}; signature (1,3)"
      linked_ids: [claim-signature, deliv-code, ref-baez]
    test-benchmarks:
      status: passed
      summary: "det_2(E_{22})=0, det_2(I_2)=1, det_2(off-diag e_7)=-1 -- all exact"
      linked_ids: [claim-signature, deliv-code]
    test-idempotent:
      status: passed
      summary: "pi_u(pi_u(Y)) = pi_u(Y) for 10 random V_0 elements; max error 0"
      linked_ids: [claim-projection-properties, deliv-code]
    test-image-dim:
      status: passed
      summary: "10x4 coordinate matrix of pi_u applied to V_0 basis has rank 4"
      linked_ids: [claim-projection-properties, deliv-code]
    test-intrinsic-closure:
      status: passed
      summary: "All 55 intrinsic products have alpha=0, x2=0, x3=0 exactly"
      linked_ids: [claim-peirce-closure, deliv-code, ref-mccrimmon]
    test-inherited-comparison:
      status: passed
      summary: "Intrinsic and inherited products agree exactly on all 55 pairs; zero V_{1/2} leakage from inherited"
      linked_ids: [claim-peirce-closure, deliv-code, ref-mccrimmon, ref-paper7]
  references:
    ref-baez:
      status: completed
      completed_actions: [cite, compare]
      missing_actions: []
      summary: "Baez 2002 Sec 3.3: h_2(K) = R^{dim(K)+1,1} predicts signature (1,3) for K=C. Confirmed by Gram matrix computation."
    ref-mccrimmon:
      status: completed
      completed_actions: [cite, compare]
      missing_actions: []
      summary: "McCrimmon Ch. 17 Peirce multiplication rule V_0 o V_0 c V_0 confirmed for h_3(O) under E_{11}."
    ref-paper7:
      status: completed
      completed_actions: [use]
      missing_actions: []
      summary: "27=1+16+10 decomposition used; V_0 basis elements from Paper 7 conventions."
    ref-octonion-code:
      status: completed
      completed_actions: [use]
      missing_actions: []
      summary: "Existing Octonion, H3O, jordan_product, peirce projections reused as base."
  forbidden_proxies:
    fp-signature-without-piu:
      status: rejected
      notes: "Signature computed explicitly on pi_u(h_2(O)), not on h_2(O) directly."
    fp-closure-without-checking:
      status: rejected
      notes: "All 55 basis pairs computed explicitly; no assumption of closure."
  uncertainty_markers:
    weakest_anchors: []
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations: []

comparison_verdicts:
  - subject_id: claim-signature
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-baez
    comparison_kind: benchmark
    metric: eigenvalue_match
    threshold: "eigenvalues = {+1,-1,-1,-1}"
    verdict: pass
    recommended_action: "Proceed to Phase 47 (Hamiltonian construction)"
    notes: "Gram matrix diagonal -- eigenvalue check trivially exact"

duration: 4min
completed: 2026-04-12
---

# Phase 46, Plan 01: V_0 Algebraic Foundation and pi_u Projection -- Summary

**Constructed pi_u: h_2(O) -> h_2(C_u) with verified Minkowski signature (1,3) and exact V_0 Peirce closure**

## Performance

- **Duration:** 4 min
- **Started:** 2026-04-12T11:31:10Z
- **Completed:** 2026-04-12T11:34:55Z
- **Tasks:** 2
- **Files modified:** 1

## Key Results

- det_2 on h_2(C_u) has Gram matrix diag(+1,-1,-1,-1): Minkowski signature (1,3) [CONFIDENCE: HIGH]
- pi_u is idempotent with 4-dimensional image, projecting h_2(O) -> h_2(C_u) via u = e_7 [CONFIDENCE: HIGH]
- Intrinsic h_2(O) Jordan product closes exactly in V_0, with exact agreement to inherited h_3(O) Peirce product and zero V_{1/2} leakage [CONFIDENCE: HIGH]

## Task Commits

1. **Task 1: Implement proj_u, pi_u, det_2 and verify Minkowski signature** - `8bd46749` (implement)
2. **Task 2: Verify Peirce closure and intrinsic vs inherited comparison** - `b5b5713c` (validate)

## Files Created/Modified

- `code/octonion_algebra.py` - Added proj_u, pi_u, det_2, jordan_product_h2o; verification comment blocks

## Next Phase Readiness

- pi_u and det_2 ready for Phase 47 (Hamiltonian construction on h_2(C_u))
- jordan_product_h2o available for constructing the V_0 dynamics
- Zero V_{1/2} leakage simplifies downstream: can use either intrinsic or inherited product interchangeably on V_0

## Contract Coverage

- Claim IDs advanced: claim-signature -> passed, claim-peirce-closure -> passed, claim-projection-properties -> passed
- Deliverable IDs produced: deliv-code -> code/octonion_algebra.py (passed)
- Acceptance test IDs run: test-signature-gram -> passed, test-benchmarks -> passed, test-idempotent -> passed, test-image-dim -> passed, test-intrinsic-closure -> passed, test-inherited-comparison -> passed
- Reference IDs surfaced: ref-baez -> cite+compare, ref-mccrimmon -> cite+compare, ref-paper7 -> use, ref-octonion-code -> use
- Forbidden proxies rejected: fp-signature-without-piu -> rejected, fp-closure-without-checking -> rejected
- Decisive comparison verdicts: claim-signature -> pass (eigenvalues match Baez 2002)

## Equations Derived

**Eq. (46.1):** Projection to C_u

$$
\mathrm{proj}_u(b) = b_0 \cdot 1 + b_7 \cdot e_7 \quad (u = e_7)
$$

**Eq. (46.2):** pi_u on V_0

$$
\pi_u(\beta, \gamma, x_1) = (\beta, \gamma, \mathrm{proj}_u(x_1))
$$

**Eq. (46.3):** det_2 quadratic form

$$
\mathrm{det}_2(X) = \beta\gamma - |x_1|^2
$$

**Eq. (46.4):** Minkowski parametrization

$$
\mathrm{det}_2 = x_0^2 - x_1^2 - x_2^2 - x_3^2, \quad G = \mathrm{diag}(+1, -1, -1, -1)
$$

where $x_0 = (\beta+\gamma)/2$, $x_3 = (\beta-\gamma)/2$, $x_1 = \mathrm{Re}(x_1)$, $x_2 = \langle\mathrm{Im}(x_1), u\rangle$.

## Validations Completed

- Gram matrix eigenvalues = {+1, -1, -1, -1} (Baez 2002 anchor)
- det_2(E_{22}) = 0, det_2(I_2) = 1, det_2(off-diag e_7) = -1 (benchmark values)
- pi_u idempotent: pi_u^2 = pi_u with zero error on 10 random elements
- Image dimension: rank of 10x4 coordinate matrix = 4
- Intrinsic V_0 closure: all 55 pairs, zero leakage
- Intrinsic == inherited: exact agreement on all 55 pairs
- h_2(C_u) limiting case: both products close, exact agreement

## Decisions & Deviations

None -- followed plan exactly as specified.

## Open Questions

- The exact agreement between intrinsic and inherited products (zero V_{1/2} leakage) resolves the uncertainty marker from the plan. The Peirce rule holds exactly for h_3(O), consistent with McCrimmon. This is a stronger result than the plan anticipated.

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
| --- | --- | --- | --- | --- | --- |
| Gram matrix eigenvalues | spec(G) | {+1,-1,-1,-1} | exact | Gram matrix computation | h_2(C_u) basis |
| V_{1/2} leakage | max leak | 0 | exact (floating point) | 55 basis pair enumeration | all V_0 x V_0 |
| pi_u idempotency error | max err | 0 | exact (floating point) | 10 random elements, seed 42 | all V_0 |
| Image dimension | rank | 4 | exact | SVD rank computation | all V_0 basis |

## Approximations Used

None -- all computations are exact (finite-dimensional linear algebra over rationals embedded in float64).

## Issues Encountered

None.

## Self-Check: PASSED

- [x] code/octonion_algebra.py exists with proj_u, pi_u, det_2, jordan_product_h2o
- [x] Commit 8bd46749 exists
- [x] Commit b5b5713c exists
- [x] All numerical results reproducible (deterministic + seed 42/137/999)
- [x] Convention consistency: u=e_7 throughout, Jordan 1/2 factor, (+,-,-,-) metric

---

_Phase: 46-v-0-algebraic-foundation-and-pi-u-projection_
_Completed: 2026-04-12_
