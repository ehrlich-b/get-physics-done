---
phase: 15-first-order-condition-algebra-identification
plan: 01
depth: full
one-liner: "First-order condition [[D_K, L_a], R_b] = 0 is automatically satisfied for ALL a, b in M_n(C) with Barrett-form D: A_F = M_n(C) (full algebra), gauge group U(n), not SM"
subsystem: derivation
tags: [first-order-condition, spectral-triple, noncommutative-geometry, gauge-group, barrett-form]

requires:
  - phase: "14-dirac-operator-construction"
    provides: "Barrett-form D_K(X) = KX + XK with K in M_n(R)^sym, dim n(n+1)/2 subspace"
  - phase: "13-order-zero-representation-theory"
    provides: "pi(a) = L_a, pi_o(b) = R_b, J, gamma, Barrett iso, order zero [L_a, R_b] = 0"
provides:
  - "[[D_K, L_a], R_b] = 0 for all a, b in M_n(C), all K in M_n(R)^sym"
  - "[D_1, L_a] = L_{[K,a]} (first commutator is a pure left multiplication)"
  - "A_F = M_n(C) (full algebra, no restriction from first-order condition)"
  - "Gauge group = U(n); at n=4, U(4) not U(1) x SU(2) x SU(3)"
  - "CCM comparison: simple vs direct sum algebra is the structural difference"
affects: [15-02-general-D, 16-spectral-action, paper-writing]

methods:
  added: [first-order-condition-computation, constraint-matrix-null-space]
  patterns: [left-right-commutativity-kills-double-commutator, associativity-is-order-zero-and-first-order]

key-files:
  created:
    - derivations/09-first-order-condition.md
    - tests/test_first_order.py

key-decisions:
  - "A_F = M_n(C) (full algebra): first-order condition places no restriction on a for Barrett-form D"
  - "The proof reduces to [L_C, R_b] = 0 (associativity), same identity as order zero"
  - "CCM comparison: difference is structural -- simple algebra M_n(C) vs direct sum M_2(H) + M_4(C)"

patterns-established:
  - "[D_1, L_a] = L_{[K,a]}: the first commutator with Barrett D is always a pure left multiplication"
  - "Left-right commutativity kills the double commutator: [L_C, R_b] = 0 is both order zero and first order"

conventions:
  - "[A,B] = AB - BA"
  - "pi(a) = L_a, pi_o(b) = R_b (Barrett iso)"
  - "D_K(X_p, X_ap) = (KX_ap + X_ap K, KX_p + X_p K)"
  - "K in M_n(R)^sym (real symmetric)"
  - "KO-dim 6: (epsilon, epsilon', epsilon'') = (+1, +1, -1)"
  - "Jordan product K * X = (1/2)(KX + XK)"

plan_contract_ref: ".gpd/phases/15-first-order-condition-algebra-identification/15-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-barrett-first-order-trivial:
      status: passed
      summary: "[[D_K, L_a], R_b] = 0 for ALL a, b in M_n(C) and ALL K in M_n(R)^sym. Proof: [D_1, L_a] = L_{[K,a]} (pure left mult), then [L_C, R_b] = 0 (associativity). A_F = M_n(C). Verified numerically at n=2,3,4 with 3 K choices each (diag, identity, random symmetric). Constraint matrix null space dim = n^2 at all n."
      linked_ids: [deliv-first-order-derivation, deliv-first-order-tests, test-double-comm-zero, test-af-full-algebra, test-subalgebra-closure, ref-phase14, ref-phase13, ref-ccm2008, ref-van-suijlekom2024]
      evidence:
        - verifier: pytest
          method: exhaustive basis-element double commutator + constraint matrix SVD
          confidence: high
          claim_id: claim-barrett-first-order-trivial
          deliverable_id: deliv-first-order-tests
          acceptance_test_id: test-double-comm-zero
    claim-gauge-group-un:
      status: passed
      summary: "A_F = M_n(C) gives gauge group U(n). At n=4: U(4), not U(1) x SU(2) x SU(3). This follows directly from A_F being the full algebra."
      linked_ids: [deliv-first-order-derivation, test-af-full-algebra, ref-ccm2008, ref-barrett2015]
    claim-ccm-comparison:
      status: passed
      summary: "CCM uses direct sum A = M_2(H) + M_4(C); cross-terms between summands create non-trivial constraints forcing A_F = C + H + M_3(C). For simple M_n(C), no cross-terms exist, and [D_K, L_a] = L_{[K,a]} is always a pure left multiplication."
      linked_ids: [deliv-first-order-derivation, test-af-full-algebra, ref-ccm2008, ref-ccsv2013]
  deliverables:
    deliv-first-order-derivation:
      status: passed
      path: "derivations/09-first-order-condition.md"
      summary: "7-step derivation: [D_1,L_a] = L_{[K,a]}, [[D_1,L_a],R_b] = 0, doubled-space verification, A_F = M_n(C), gauge U(n), CCM comparison, limiting cases, Pati-Salam context."
      linked_ids: [claim-barrett-first-order-trivial, claim-gauge-group-un, claim-ccm-comparison]
    deliv-first-order-tests:
      status: passed
      path: "tests/test_first_order.py"
      summary: "34-test pytest suite: 9 double-commutator-zero tests (3 K types x 3 n values), 9 null-space-dimension tests, 6 subalgebra closure tests, 1 K-independence test (10 random K at n=2), 4 limiting case tests, 3 intermediate-result tests, 3 axiom cross-checks."
      linked_ids: [claim-barrett-first-order-trivial, test-double-comm-zero, test-af-full-algebra, test-subalgebra-closure]
  acceptance_tests:
    test-double-comm-zero:
      status: passed
      summary: "For K = diag(1,0,...,0), K = I, K = random symmetric at n=2,3,4: all n^4 basis-element pairs (a,b) give ||[[D_K, L_a], R_b]|| < 1e-12. Total: 9 parametrized tests, each checking all n^4 pairs."
      linked_ids: [claim-barrett-first-order-trivial, deliv-first-order-tests]
    test-af-full-algebra:
      status: passed
      summary: "Constraint matrix null space dimension = n^2 at n=2 (4), n=3 (9), n=4 (16) for all 3 K choices. SVD threshold 1e-10. Confirms A_F = M_n(C) = full algebra."
      linked_ids: [claim-barrett-first-order-trivial, deliv-first-order-tests]
    test-subalgebra-closure:
      status: passed
      summary: "For 3 random a, b at each n=2,3,4: ab satisfies [[D,L_{ab}],R_c] = 0 and a^dag satisfies [[D,L_{a^dag}],R_c] = 0 for random c. A_F closed under multiplication and adjoint."
      linked_ids: [claim-barrett-first-order-trivial, deliv-first-order-tests]
  references:
    ref-phase14:
      status: completed
      completed_actions: [read, use]
      missing_actions: []
      summary: "Barrett-form D_K(X) = KX + XK with K in M_n(R)^sym from Phase 14-02. Used as direct input for first-order condition computation."
    ref-phase13:
      status: completed
      completed_actions: [read, use]
      missing_actions: []
      summary: "pi(a) = L_a, pi_o(b) = R_b, order zero [L_a, R_b] = 0 from Phase 13. Same algebraic identity (associativity) powers both order zero and first-order condition."
    ref-ccm2008:
      status: completed
      completed_actions: [compare, cite]
      missing_actions: []
      summary: "CCM classification compared: A_F = C + H + M_3(C) for direct sum M_2(H) + M_4(C). Structural difference (simple vs direct sum) documented in Step 5."
    ref-van-suijlekom2024:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Textbook treatment of first-order condition as linear algebra cited as method reference."
    ref-barrett2015:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Barrett matrix geometries framework cited. Simple algebra gives full unitary gauge group, consistent with our finding."
    ref-ccsv2013:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "CCSV Pati-Salam from relaxed first-order condition cited for context. Our case is distinct: condition is trivially satisfied, not dropped."
  forbidden_proxies:
    fp-assume-sm:
      status: rejected
      notes: "Did not assume CCM result A_F = C + H + M_3(C). Computed first-order condition from scratch for our algebra M_n(C), found A_F = M_n(C) (different result, as expected for simple algebra)."
    fp-spot-check:
      status: rejected
      notes: "Checked ALL n^4 basis-element pairs at each n, not a subset. Constraint matrix null space captures all a satisfying the condition."
    fp-skip-doubled:
      status: rejected
      notes: "Step 3 of derivation explicitly verifies on full doubled space H = M_n(C)_p + M_n(C)_ap. Sector-swap verified to not affect result."
  uncertainty_markers:
    weakest_anchors:
      - "Barrett-form D is a special subspace (dim n(n+1)/2) of the full moduli space (dim n^2(n^2+1)). A_F = M_n(C) may not hold for general D -- tested in Plan 15-02."
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations: []

comparison_verdicts:
  - subject_id: claim-barrett-first-order-trivial
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase14
    comparison_kind: benchmark
    metric: double_commutator_norm
    threshold: "< 1e-12"
    verdict: pass
    recommended_action: "Proceed to Plan 15-02 to test general D (full moduli space)"
    notes: "All 9 parametrized tests (3 K types x 3 n values) pass. Each test checks all n^4 basis pairs."
  - subject_id: claim-barrett-first-order-trivial
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-ccm2008
    comparison_kind: prior_work
    metric: structural_comparison
    threshold: "A_F identified and compared"
    verdict: pass
    recommended_action: "Document structural difference (simple vs direct sum) in paper"
    notes: "CCM: A_F = C + H + M_3(C) for direct sum. Us: A_F = M_n(C) for simple algebra. Difference is structural, not an error."

duration: 4min
completed: 2026-03-23
---

# Plan 15-01: First-Order Condition for Barrett-Form D Summary

**First-order condition [[D_K, L_a], R_b] = 0 is automatically satisfied for ALL a, b in M_n(C) with Barrett-form D: A_F = M_n(C) (full algebra), gauge group U(n), not SM**

## Performance

- **Duration:** 4 min
- **Started:** 2026-03-23T14:00:05Z
- **Completed:** 2026-03-23T14:04:13Z
- **Tasks:** 2
- **Files modified:** 2

## Key Results

- [[D_K, L_a], R_b] = 0 for ALL a, b in M_n(C), ALL K in M_n(R)^sym. The proof is 3 lines: [D_1, L_a] = L_{[K,a]}, then [L_C, R_b] = 0 (associativity). [CONFIDENCE: HIGH]
- A_F = M_n(C) (full algebra). The first-order condition places NO restriction on a. [CONFIDENCE: HIGH]
- Gauge group = U(n). At n=4: U(4), NOT U(1) x SU(2) x SU(3). [CONFIDENCE: HIGH]
- CCM comparison: difference is structural -- simple M_n(C) has no cross-terms, direct sum M_2(H) + M_4(C) does. [CONFIDENCE: HIGH]
- 34/34 pytest tests pass at n=2,3,4: double commutator zero, null space dim = n^2, subalgebra closure, K-independence, limiting cases. [CONFIDENCE: HIGH]

## Task Commits

1. **Task 1: Derive first-order condition triviality for Barrett-form D** - `9c025d8` (derive)
2. **Task 2: Numerical verification at n=2,3,4** - `9455872` (validate)

## Files Created/Modified

- `derivations/09-first-order-condition.md` - 7-step derivation of [[D_K, L_a], R_b] = 0, A_F = M_n(C), gauge U(n), CCM comparison
- `tests/test_first_order.py` - 34-test pytest suite verifying all claims numerically

## Next Phase Readiness

- A_F = M_n(C) for Barrett-form D is established. Plan 15-02 tests the first-order condition for GENERAL D in the full n^2(n^2+1)-dim moduli space, which may give a proper subalgebra.
- The key physical conclusion: Barrett-form D alone does not reproduce the SM gauge group. Either (a) general D gives SM-compatible A_F, (b) additional constraints beyond Barrett-form are needed, or (c) the SM gauge group does not emerge from M_n(C) spectral triples.
- The derivation machinery ([D, pi(a)], constraint matrix, null space) is reusable for Plan 15-02.

## Contract Coverage

- Claim IDs advanced: claim-barrett-first-order-trivial -> passed, claim-gauge-group-un -> passed, claim-ccm-comparison -> passed
- Deliverable IDs produced: deliv-first-order-derivation -> derivations/09-first-order-condition.md (passed), deliv-first-order-tests -> tests/test_first_order.py (passed)
- Acceptance test IDs run: test-double-comm-zero -> passed, test-af-full-algebra -> passed, test-subalgebra-closure -> passed
- Reference IDs surfaced: ref-phase14 -> read+use, ref-phase13 -> read+use, ref-ccm2008 -> compare+cite, ref-van-suijlekom2024 -> cite, ref-barrett2015 -> cite, ref-ccsv2013 -> cite
- Forbidden proxies rejected: fp-assume-sm -> rejected, fp-spot-check -> rejected, fp-skip-doubled -> rejected
- Decisive comparison verdicts: claim-barrett-first-order-trivial -> pass (double commutator norm < 1e-12), claim-barrett-first-order-trivial -> pass (CCM structural comparison)

## Equations Derived

**Eq. (15-01.1) -- First-order condition:**

$$[[D, \pi(a)], \pi_o(b)] = 0 \quad \forall\, a \in A_F,\; b \in A$$

**Eq. (15-01.2) -- First commutator:**

$$[D_1, L_a] = L_{[K,a]}$$

The commutator of Barrett-form D_1 = L_K + R_K with left multiplication L_a is a pure left multiplication by [K, a]. The R_K part cancels because [R_K, L_a] = 0 (associativity).

**Eq. (15-01.3) -- Double commutator vanishes:**

$$[[D_1, L_a], R_b] = [L_{[K,a]}, R_b] = 0$$

Any left multiplication commutes with any right multiplication (associativity).

**Eq. (15-01.4) -- Doubled space first commutator:**

$$[D, \pi(a)](X_p, X_{ap}) = ([K,a]X_{ap}, [K,a]X_p) = \sigma_1 \otimes L_{[K,a]}$$

**Eq. (15-01.5) -- Doubled space double commutator:**

$$[[D, \pi(a)], \pi_o(b)](X_p, X_{ap}) = (0, 0)$$

**Eq. (15-01.6) -- Universal result:**

$$[[D_K, \pi(a)], \pi_o(b)] = 0 \quad \forall\, a, b \in M_n(\mathbb{C}),\; \forall\, K \in M_n(\mathbb{R})^{\text{sym}}$$

**Eq. (15-01.7) -- Maximal subalgebra:**

$$A_F = M_n(\mathbb{C}) \quad \text{(full algebra)}$$

**Eq. (15-01.8) -- Gauge group:**

$$\text{Gauge group} = U(n)$$

## Validations Completed

- [D_1, L_a] = L_{[K,a]} verified numerically at n=2,3,4 for random symmetric K (3 tests)
- [[D_K, L_a], R_b] = 0 for all n^4 basis pairs at n=2,3,4, for K = diag(1,0,...,0), I, random symmetric (9 tests)
- Constraint matrix null space dim = n^2 at n=2 (4), n=3 (9), n=4 (16) for 3 K types (9 tests)
- Subalgebra closure: product and adjoint verified numerically (6 tests)
- K-independence: dim(A_F) = 4 for 10 random K at n=2 (1 test)
- Limiting cases: K=0 (D=0, vacuous), K=I ([K,a]=0), K generic (4 tests)
- Barrett-form D cross-check: all 3 axioms pass at n=2,3,4 (3 tests)
- 34/34 tests pass

## Decisions & Deviations

**Decisions:** None -- plan executed exactly as written.

**Deviations:** None.

## Open Questions

- Does the full moduli space (general D, not just Barrett-form) give a PROPER subalgebra A_F? This is Plan 15-02.
- Can additional physical constraints (beyond the spectral triple axioms) reduce U(n) to U(1) x SU(2) x SU(3)?
- Is the Barrett-form subspace dim n(n+1)/2 the ONLY subspace giving A_F = M_n(C), or does the full moduli also give A_F = M_n(C)?

## Self-Check: PASSED

- [x] derivations/09-first-order-condition.md exists
- [x] tests/test_first_order.py exists with 34 tests
- [x] Commit 9c025d8 exists (Task 1)
- [x] Commit 9455872 exists (Task 2)
- [x] 34/34 tests pass (pytest exit code 0)
- [x] [[D_K, L_a], R_b] = 0 verified at n=2,3,4 for 3 K types
- [x] dim(A_F) = n^2 verified at n=2,3,4
- [x] Subalgebra closure verified
- [x] K-independence verified (10 random K)
- [x] Limiting cases K=0, K=I pass
- [x] CCM comparison documented
- [x] All forbidden proxies rejected
- [x] All acceptance tests passed
- [x] All references surfaced
- [x] Convention consistency: all files use same Barrett iso, L_a, R_b, [A,B] = AB-BA

---

_Phase: 15-first-order-condition-algebra-identification_
_Plan: 01_
_Completed: 2026-03-23_
