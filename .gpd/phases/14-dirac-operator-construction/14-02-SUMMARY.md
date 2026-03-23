---
phase: 14-dirac-operator-construction
plan: 02
depth: full
one-liner: "Sequential product asymmetry (commutator) fails JD=DJ, but Barrett-form D with real symmetric K passes all axioms -- this IS the linearized sequential product (Jordan product), giving n(n+1)/2-dim subspace of moduli"
subsystem: derivation
tags: [dirac-operator, sequential-product, jordan-product, barrett-form, spectral-triple, candidate-testing]

requires:
  - phase: "14-dirac-operator-construction"
    provides: "D moduli space dim = n^2(n^2+1), block form D = [[0,M^dag],[M,0]], involution M = J_+ M^T J_+"
  - phase: "13-order-zero-representation-theory"
    provides: "H = 2 x C^{n^2}, pi(a) = L_a, pi_o(b) = R_b, gamma = diag(P,-P), J antilinear, Barrett iso"
provides:
  - "Commutator [a,X] = L_a - R_a fails J constraint: JD = -DJ (epsilon'=-1), structural for all real symmetric a"
  - "SP operator sqrt(a)Xsqrt(a) is SWAP-even: commutes with gamma, not anticommutes"
  - "Barrett-form D with K = real symmetric passes ALL three axioms: n(n+1)/2-dim subspace of moduli"
  - "Jordan product connection: Barrett D_1(X) = KX + XK = 2(K*X) = linearized sequential product"
  - "KO-dim 6 (epsilon'=+1) selects symmetric combination L_K + R_K over antisymmetric L_K - R_K"
affects: [15-first-order-condition, 16-spectral-action]

methods:
  added: [barrett-form-analysis, jordan-product-linearization, candidate-constraint-testing]
  patterns: [epsilon-prime-sign-selection, swap-parity-diagnosis, j-constraint-via-transpose-reversal]

key-files:
  created:
    - derivations/08-dirac-candidates.md
  modified:
    - tests/test_dirac_moduli.py

key-decisions:
  - "Barrett J constraint requires K^T = K (symmetric), NOT K = scalar: the condition is [K^T - K, Y] = 0, not [K, Y] = 0"
  - "Jordan product a*X = (1/2)(aX+Xa) is the linearization of sp(a,X) = sqrt(a)Xsqrt(a) at identity"
  - "Barrett-form D encodes Jordan product action: D_1(X) = 2(K*X) for real symmetric K"
  - "Commutator/antisymmetric candidate pairs with epsilon'=-1; anticommutator/symmetric pairs with epsilon'=+1"

patterns-established:
  - "Epsilon' sign selects symmetric vs antisymmetric combination of L and R multiplication"
  - "Barrett-form subspace has dim n(n+1)/2: much smaller than full moduli n^2(n^2+1), expected to match first-order condition subspace"

conventions:
  - "[A,B] = AB - BA"
  - "inner product linear in second argument"
  - "J antilinear, J(X_p, X_{ap}) = (overline{X_{ap}}^T, overline{X_p}^T)"
  - "gamma = diag(P, -P), P = transpose under Barrett iso"
  - "KO-dim 6: (epsilon, epsilon', epsilon'') = (+1, +1, -1)"
  - "sp(a,b) = sqrt(a) b sqrt(a)"
  - "Jordan product a * b = (1/2)(ab + ba)"

plan_contract_ref: ".gpd/phases/14-dirac-operator-construction/14-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-candidate-tested:
      status: passed
      summary: "All three candidate types tested constraint-by-constraint at n=2,3,4. Commutator [a,X] passes D*=D and {D,gamma}=0 but fails JD=DJ (gets JD=-DJ). SP operator sqrt(a)Xsqrt(a) is SWAP-even (fails gamma). Barrett-form D with K=real symmetric passes all three constraints, forming an n(n+1)/2-dim subspace."
      linked_ids: [deliv-candidate-derivation, deliv-candidate-tests, test-commutator-candidate, test-sp-candidate, test-constraint-diagnosis, ref-paper5, ref-barrett2015, ref-plan14-01]
      evidence:
        - verifier: pytest
          method: constraint-by-constraint numerical verification
          confidence: high
          claim_id: claim-candidate-tested
          deliverable_id: deliv-candidate-tests
          acceptance_test_id: test-commutator-candidate
    claim-natural-d-identified:
      status: passed
      summary: "Barrett-form D with K in M_n(R)^sa identified as the most natural D from self-modeling: D_1(X) = KX + XK = 2(K*X) is twice the Jordan product, which is the linearization of the sequential product at the identity. This provides a direct self-modeling motivation."
      linked_ids: [deliv-candidate-derivation, test-natural-d-constraints, test-natural-d-motivation, ref-paper5, ref-barrett2015, ref-plan14-01]
  deliverables:
    deliv-candidate-derivation:
      status: passed
      path: "derivations/08-dirac-candidates.md"
      summary: "Complete constraint-by-constraint analysis of three candidate types under Barrett iso. Barrett-form with real symmetric K passes all axioms. Jordan product linearization identified."
      linked_ids: [claim-candidate-tested, claim-natural-d-identified, test-commutator-candidate, test-sp-candidate]
    deliv-candidate-tests:
      status: passed
      path: "tests/test_dirac_moduli.py"
      summary: "85-test pytest suite: 52 original moduli tests + 33 new candidate tests. Commutator JD=-DJ verified at n=2,3,4. SP SWAP-even verified. Barrett with real sym K passes all constraints at n=2,3,4. Non-symmetric K fails. Summary table at all n."
      linked_ids: [claim-candidate-tested, claim-natural-d-identified, test-commutator-candidate, test-sp-candidate, test-constraint-diagnosis]
  acceptance_tests:
    test-commutator-candidate:
      status: passed
      summary: "Commutator D_a^comm tested at n=2,3,4 with a=diag(1,0,...,0), E_{12}+E_{21}, diag(1,2). All pass D*=D and {D,gamma}=0. All fail JD=DJ with JD=-DJ (Frobenius of JDJ+D < 1e-12). Violation is structural (200% norm)."
      linked_ids: [claim-candidate-tested, deliv-candidate-tests, ref-plan14-01]
    test-sp-candidate:
      status: passed
      summary: "SP operator sqrt(a)Xsqrt(a) tested at n=2. Correctly identified as SWAP-even: [D,gamma]=0 (Frobenius < 1e-12) while {D,gamma} has Frobenius > 1. SWAP-odd extraction gives zero for real symmetric a."
      linked_ids: [claim-candidate-tested, deliv-candidate-tests, ref-paper5]
    test-constraint-diagnosis:
      status: passed
      summary: "Each failing candidate diagnosed: commutator has 100% moduli residual (projection onto moduli space = 0, since JDJ=-D means D is in the -1 eigenspace of the J involution). Barrett non-symmetric K fails J. Barrett real symmetric K has 0% residual."
      linked_ids: [claim-candidate-tested, deliv-candidate-tests, ref-plan14-01]
    test-natural-d-constraints:
      status: passed
      summary: "Barrett-form D with K=diag(1,0,...,0) (real symmetric, non-scalar) verified at n=2,3,4: all three constraints pass (Frobenius < 1e-12). Projects onto moduli with zero residual. Barrett scalar K=I also passes. Non-symmetric K fails."
      linked_ids: [claim-natural-d-identified, deliv-candidate-tests, ref-barrett2015]
    test-natural-d-motivation:
      status: passed
      summary: "Jordan product connection established analytically: Barrett D_1(X) = KX + XK = 2(K*X). The Jordan product K*X = (1/2)(KX+XK) is the linearization of the sequential product: d/deps (I+eps*A) & X |_0 = A*X. KO-dim 6 sign epsilon'=+1 selects the symmetric combination L_K+R_K over the antisymmetric L_K-R_K."
      linked_ids: [claim-natural-d-identified, deliv-candidate-derivation, ref-paper5, ref-paper6]
  references:
    ref-paper5:
      status: completed
      completed_actions: [read, use, cite]
      missing_actions: []
      summary: "Sequential product sp(a,b) = sqrt(a)bsqrt(a) from Paper 5 is the source of all candidate constructions. The linearization (Jordan product) gives the successful Barrett-form candidate."
    ref-barrett2015:
      status: completed
      completed_actions: [use, compare, cite]
      missing_actions: []
      summary: "Barrett's D form D_1(X) = KX + XK^* used as Candidate C. J constraint correctly derived: K must be real symmetric (K^T = K, overline{K} = K). n(n+1)/2-dim subspace identified."
    ref-plan14-01:
      status: completed
      completed_actions: [read, use]
      missing_actions: []
      summary: "Moduli space from Plan 14-01 used as target for projection tests. Barrett-form subspace is n(n+1)/2 within n^2(n^2+1) total. All moduli basis elements satisfy constraints."
    ref-paper6:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "SWAP operator and doubled Hilbert space from Paper 6 provide the framework. SWAP-odd vs SWAP-even distinction is key to candidate diagnosis."
  forbidden_proxies:
    fp-ad-hoc-d-construction:
      status: rejected
      notes: "Natural D identified through systematic candidate testing + Jordan product linearization, not ad hoc construction. The Barrett-form D has explicit self-modeling rationale."
    fp-assume-d-exists:
      status: rejected
      notes: "All three constraints verified independently for every candidate. Commutator diagnosed as failing JD=DJ with quantitative Frobenius norm. Barrett with non-symmetric K also tested and fails."
    fp-single-a-only:
      status: rejected
      notes: "Commutator tested with a=diag(1,0), E_{12}+E_{21}, diag(1,2) at n=2. All fail JD=DJ structurally. Barrett tested with K=diag(1,0), K=I, K=upper_triangular."
  uncertainty_markers:
    weakest_anchors:
      - "Jordan product connection is linearization at identity; the full nonlinear sequential product sp(a,b) = sqrt(a)bsqrt(a) does NOT give a valid D"
      - "Barrett-form subspace (n(n+1)/2 params) expected to coincide with first-order condition subspace, but this is not verified until Phase 15"
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations: []

comparison_verdicts:
  - subject_id: claim-candidate-tested
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-paper5
    comparison_kind: benchmark
    metric: constraint_satisfaction
    threshold: "all three constraints pass or specific failure identified"
    verdict: pass
    recommended_action: "Proceed to Phase 15 with Barrett-form D subspace as primary candidate"
    notes: "Commutator fails JD=DJ. SP fails gamma. Barrett real sym K passes all three. 85/85 tests pass."
  - subject_id: claim-natural-d-identified
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-barrett2015
    comparison_kind: cross_method
    metric: moduli_membership
    threshold: "Barrett D projects onto moduli with zero residual"
    verdict: pass
    recommended_action: "Phase 15: impose first-order condition on Barrett-form D to see if n(n+1)/2 reduces to SM-compatible parameter count"
    notes: "Barrett-form D with real sym K is an n(n+1)/2-dim subspace of the n^2(n^2+1)-dim moduli space"

duration: 15min
completed: 2026-03-23
---

# Plan 14-02: Sequential Product Candidate Testing Summary

**Sequential product asymmetry (commutator) fails JD=DJ, but Barrett-form D with real symmetric K passes all axioms -- this IS the linearized sequential product (Jordan product), giving n(n+1)/2-dim subspace of moduli**

## Performance

- **Duration:** 15 min
- **Started:** 2026-03-23T03:18:15Z
- **Completed:** 2026-03-23T03:34:14Z
- **Tasks:** 2
- **Files modified:** 2

## Key Results

- Commutator [a, X] = aX - Xa (the "asymmetry" L_a - R_a) FAILS JD = DJ: gets JD = -DJ instead. This is structural for all real symmetric a, with Frobenius violation = 200% of operator norm. [CONFIDENCE: HIGH]
- SP operator sqrt(a) X sqrt(a) is SWAP-even (commutes with P = transpose), failing the gamma anticommutation requirement. No natural SWAP-odd extraction works. [CONFIDENCE: HIGH]
- Barrett-form D with D_1(X) = KX + XK and K = real symmetric PASSES all three axioms, giving an n(n+1)/2-dimensional subspace of the moduli space. [CONFIDENCE: HIGH]
- The Barrett-form D_1(X) = KX + XK = 2(K * X) is twice the Jordan product. The Jordan product IS the linearization of the sequential product: d/deps (I + eps A) & X |_0 = A * X. [CONFIDENCE: HIGH]
- KO-dimension 6 (epsilon' = +1) selects the symmetric combination L_K + R_K (anticommutator) over the antisymmetric L_K - R_K (commutator). [CONFIDENCE: HIGH]

## Task Commits

1. **Task 1: Define and test sequential product asymmetry candidates** - `d8eef8d` (derive)
2. **Task 2: SymPy/NumPy verification at n=2,3,4** - `0af6ca0` (validate)

## Files Created/Modified

- `derivations/08-dirac-candidates.md` - Complete candidate analysis: commutator, SP, Barrett-form; Jordan product connection
- `tests/test_dirac_moduli.py` - Extended from 52 to 85 tests: candidate construction, constraint checking, moduli projection

## Next Phase Readiness

- Barrett-form D with K in M_n(R)^sa is the natural candidate for Phase 15 (first-order condition)
- n(n+1)/2 parameters at n=4 gives 10 parameters; first-order condition may further reduce
- The Jordan product connection provides a clear self-modeling interpretation for D
- Comparison with SM 31 parameters deferred to Phase 15 (requires full generation structure)

## Contract Coverage

- Claim IDs advanced: claim-candidate-tested -> passed, claim-natural-d-identified -> passed
- Deliverable IDs produced: deliv-candidate-derivation -> derivations/08-dirac-candidates.md (passed), deliv-candidate-tests -> tests/test_dirac_moduli.py (passed)
- Acceptance test IDs run: test-commutator-candidate -> passed, test-sp-candidate -> passed, test-constraint-diagnosis -> passed, test-natural-d-constraints -> passed, test-natural-d-motivation -> passed
- Reference IDs surfaced: ref-paper5 -> read+use+cite, ref-barrett2015 -> use+compare+cite, ref-plan14-01 -> read+use, ref-paper6 -> cite
- Forbidden proxies rejected: fp-ad-hoc-d-construction -> rejected, fp-assume-d-exists -> rejected, fp-single-a-only -> rejected
- Decisive comparison verdicts: claim-candidate-tested -> pass (constraint satisfaction), claim-natural-d-identified -> pass (moduli membership)

## Equations Derived

**Eq. (14-02.1) -- Commutator J anticommutation:**

$$J [a, -] J^{-1} = -[a, -] \quad \text{for all real symmetric } a$$

The commutator anticommutes with J (epsilon' = -1) instead of commuting (epsilon' = +1 required by KO-dim 6).

**Eq. (14-02.2) -- Barrett-form D (Jordan product):**

$$D_1(X) = KX + XK = 2(K \circ X), \quad K \in M_n(\mathbb{R})^{\text{sa}}$$

Barrett D with real symmetric K passes D* = D, D gamma = -gamma D, and JD = DJ.

**Eq. (14-02.3) -- Jordan product as linearized sequential product:**

$$\frac{d}{d\epsilon}\Big|_{\epsilon=0} (I + \epsilon A) \mathbin{\&} X = A \circ X = \frac{1}{2}(AX + XA)$$

The Jordan product is the first-order approximation to the sequential product near the identity.

**Eq. (14-02.4) -- Barrett subspace dimension:**

$$\dim(\text{Barrett subspace}) = \frac{n(n+1)}{2} \quad (n=2{:}3, \; n=3{:}6, \; n=4{:}10)$$

## Validations Completed

- Commutator JD = -DJ verified at n=2,3,4 for a = diag(1,0,...,0) (Frobenius < 1e-12)
- Commutator JD = -DJ verified for multiple a: diag(1,0), E_{12}+E_{21}, diag(1,2) at n=2
- SP operator SWAP-even verified: [D, gamma] = 0, {D, gamma} != 0 at n=2
- SP SWAP-odd extraction gives zero for real symmetric a (verified numerically)
- Barrett real symmetric K passes all 3 constraints at n=2,3,4 (Frobenius < 1e-12 each)
- Barrett scalar K = I passes all 3 constraints at n=2,3,4
- Barrett non-symmetric K fails J constraint at n=2,3
- Barrett-form D projects onto moduli space with zero residual at n=2,3,4
- Commutator D has 100% moduli residual (projection = 0)
- Barrett subspace dimension: 3, 6, 10 at n=2,3,4 (matches n(n+1)/2)
- 85/85 pytest tests pass

## Decisions & Deviations

**Decisions:**
- Barrett J constraint corrected from "K must be scalar" to "K must be real symmetric": the condition is [K^T - K, Y] = 0, not [K, Y] = 0. The analytical derivation initially had an algebraic error that was caught by numerical verification.
- Jordan product connection identified: Barrett D_1(X) = 2(K * X) is twice the Jordan product, which linearizes the sequential product.

**Deviations:**

### Auto-fixed Issues

**1. [Rule 1 - Code bug] Barrett J constraint analytical error corrected by numerical verification**

- **Found during:** Task 2 (numerical verification)
- **Issue:** Initial analytical derivation in Task 1 incorrectly concluded JD=DJ forces K = scalar (lambda * I). Numerical tests showed K = diag(1,0) passes all constraints.
- **Fix:** Re-derived: the J constraint gives [K^T - K, Y] = 0 for all Y, requiring K^T = K (symmetric), not K = scalar. Barrett-form with real symmetric K passes. Derivation and tests updated.
- **Files modified:** derivations/08-dirac-candidates.md, tests/test_dirac_moduli.py
- **Verification:** 85/85 tests pass including Barrett with non-scalar K
- **Committed in:** 0af6ca0 (Task 2 commit)

---

**Total deviations:** 1 auto-fixed (algebraic error caught by numerics)
**Impact on plan:** The correction STRENGTHENED the result: instead of "no candidate works, D must be ad hoc," we found that Barrett-form D with real symmetric K provides a natural self-modeling-motivated D via the Jordan product linearization.

## Open Questions

- Does the first-order condition [[D, pi(a)], pi_o(b)] = 0 restrict the Barrett-form D subspace further? (Phase 15)
- Does the Barrett-form subspace (n(n+1)/2 params) coincide exactly with the first-order condition subspace? (Phase 15)
- At n=4: Barrett gives 10 params, SM has 31. The discrepancy may involve generation structure and real/quaternionic subalgebras. (Phase 15+)
- Can the Jordan product connection be elevated from a linearization to an exact statement?

## Self-Check: PASSED

- [x] derivations/08-dirac-candidates.md exists
- [x] tests/test_dirac_moduli.py exists with 85 tests
- [x] Commit d8eef8d exists (Task 1)
- [x] Commit 0af6ca0 exists (Task 2)
- [x] 85 tests pass (pytest exit code 0)
- [x] Commutator JD = -DJ verified at n=2,3,4
- [x] SP SWAP-even verified at n=2
- [x] Barrett real sym K passes at n=2,3,4
- [x] Barrett non-sym K fails at n=2,3
- [x] Barrett scalar K passes at n=2,3,4
- [x] Summary table produced
- [x] Jordan product connection documented
- [x] All forbidden proxies rejected
- [x] All acceptance tests passed
- [x] All references surfaced
- [x] Convention consistency: all files use same J, gamma, P, Barrett iso

---

_Phase: 14-dirac-operator-construction_
_Plan: 02_
_Completed: 2026-03-23_
