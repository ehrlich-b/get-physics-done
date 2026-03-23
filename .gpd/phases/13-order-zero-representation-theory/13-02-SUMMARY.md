---
phase: 13-order-zero-representation-theory
plan: 02
depth: full
one-liner: "SymPy/NumPy verification confirms order zero [pi(a), pi_o(b)] = 0 for all 353 matrix unit pairs at n=2,3,4; identifies [gamma, pi(a)] != 0 as blocking issue for even spectral triple"
subsystem: [validation, computation]
tags: [order-zero, spectral-triple, noncommutative-geometry, representation-theory]

requires:
  - phase: paper7-spectral-triple-prompt.md
    provides: J, gamma, P definitions and KO-dim 6 sign relations
provides:
  - Order zero condition verified numerically at n=2,3,4 for naive action pi(a) = block_diag(a x I, a x I)
  - pi_o verified as *-representation of opposite algebra A^op
  - gamma eigenvalue pattern matches Connes SM analog (Sym^2/wedge^2 decomposition)
  - [gamma, pi(a)] = 0 failure documented -- only C*I satisfies even condition
  - Commutant of pi(M_n) has dimension 4n^2 = dim(M_2(C) x M_n(C))
affects: [13-03, phase-14]

methods:
  added: [exhaustive commutator verification, commutant dimension computation via SVD]
  patterns: [numpy integer-matrix verification for exact algebraic identities]

key-files:
  created:
    - tests/test_order_zero.py

key-decisions:
  - "pi_o multiplicativity is over A^op (reversed multiplication), not A -- this is correct NCG behavior"
  - "[gamma, pi(a)] = 0 failure for all non-scalar a is genuine, not a code bug -- P kron(a,I) P = kron(I,a) analytically"

patterns-established:
  - "Order zero test: build J_matrix, build_pi, build_pi_o, verify all n^4 commutators"
  - "Even condition test: [gamma, pi(a)] reduces to [P, kron(a, I_n)] in each sector"

conventions:
  - "J_matrix = [[0,P],[P,0]], P = SWAP"
  - "gamma = [[P,0],[0,-P]]"
  - "pi(a) = block_diag(kron(a,I), kron(a,I)) [naive action]"
  - "pi_o(b) = J_matrix @ conj(pi(b^dagger)) @ J_matrix [antilinear J]"
  - "[A,B] = AB - BA"

plan_contract_ref: ".gpd/phases/13-order-zero-representation-theory/13-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-sympy-order-zero:
      status: passed
      summary: "All 353 commutators [pi(E_ij), pi_o(E_kl)] = 0 verified at n=2 (16), n=3 (81), n=4 (256) with NumPy integer-matrix arithmetic (exact for 0/1 matrices)"
      linked_ids: [deliv-test-code, test-all-commutators-n2, test-all-commutators-n34, test-pi-o-rep-axioms]
      evidence:
        - verifier: pytest
          method: exhaustive commutator computation
          confidence: high
          claim_id: claim-sympy-order-zero
          deliverable_id: deliv-test-code
          acceptance_test_id: test-all-commutators-n2
    claim-j-consistency:
      status: passed
      summary: "J^2 = I, J gamma = -gamma J, gamma^2 = I, gamma = gamma^dagger all verified at n=2,3,4; [gamma, pi(a)] = 0 FAILS for all non-scalar a (only C*I commutes)"
      linked_ids: [deliv-test-code, test-j-properties, test-gamma-properties]
      evidence:
        - verifier: pytest
          method: direct matrix computation
          confidence: high
          claim_id: claim-j-consistency
          deliverable_id: deliv-test-code
          acceptance_test_id: test-j-properties
  deliverables:
    deliv-test-code:
      status: passed
      path: "tests/test_order_zero.py"
      summary: "52-test pytest suite verifying order zero, J/gamma properties, pi_o representation, sector decomposition, and commutant structure at n=2,3,4"
      linked_ids: [claim-sympy-order-zero, claim-j-consistency]
  acceptance_tests:
    test-all-commutators-n2:
      status: passed
      summary: "All 16 commutators [pi(E_ij), pi_o(E_kl)] exactly zero at n=2 (8x8 matrices)"
      linked_ids: [claim-sympy-order-zero, deliv-test-code]
    test-all-commutators-n34:
      status: passed
      summary: "All 81 commutators zero at n=3 (18x18) and all 256 zero at n=4 (32x32)"
      linked_ids: [claim-sympy-order-zero, deliv-test-code]
    test-pi-o-rep-axioms:
      status: passed
      summary: "pi_o is a *-representation of A^op: pi_o(a) pi_o(b) = pi_o(b*a) and pi_o(a^dagger) = pi_o(a)^dagger verified at n=2,3,4"
      linked_ids: [claim-sympy-order-zero, deliv-test-code]
    test-j-properties:
      status: passed
      summary: "J^2 = I verified at n=2,3,4; J_matrix is real binary (0/1 entries)"
      linked_ids: [claim-j-consistency, deliv-test-code]
    test-gamma-properties:
      status: passed
      summary: "gamma^2 = I, gamma = gamma^dagger, J gamma + gamma J = 0 at n=2,3,4; [gamma, pi(a)] = 0 fails for ALL n^2 matrix units (only identity commutes)"
      linked_ids: [claim-j-consistency, deliv-test-code]
  references:
    ref-connes1995:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Order zero condition [a, Jb*J^{-1}] = 0 verified as defined by Connes 1995"
    ref-paper6:
      status: completed
      completed_actions: [read, use]
      missing_actions: []
      summary: "J, P, gamma definitions from Paper 6 used to construct all operators"
  forbidden_proxies:
    fp-partial-basis:
      status: rejected
      notes: "ALL n^4 pairs tested at each n (16 + 81 + 256 = 353 total), not a subset"
    fp-numerical-only:
      status: rejected
      notes: "Matrix units are integer (0/1) matrices; all arithmetic is exact for integer matrices in NumPy float64 (no rounding). Frobenius norm threshold 1e-12 catches any deviation."
  uncertainty_markers:
    weakest_anchors: ["The even condition [gamma, pi(a)] = 0 fails for the naive action, meaning the spectral triple is NOT even with this (gamma, pi) pair"]
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations: ["[gamma, pi(a)] != 0 for all a != c*I means the naive algebra action is incompatible with even spectral triple structure using gamma = [[P,0],[0,-P]]"]

comparison_verdicts:
  - subject_id: claim-sympy-order-zero
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-connes1995
    comparison_kind: benchmark
    metric: commutator_frobenius_norm
    threshold: "< 1e-12"
    verdict: pass
    recommended_action: "Proceed to Dirac operator construction (Phase 14)"
    notes: "353/353 commutators exactly zero with integer arithmetic"

duration: 8min
completed: 2026-03-22
---

# Plan 02: SymPy/NumPy Order Zero Verification Summary

**SymPy/NumPy verification confirms order zero [pi(a), pi_o(b)] = 0 for all 353 matrix unit pairs at n=2,3,4; identifies [gamma, pi(a)] != 0 as blocking issue for even spectral triple**

## Performance

- **Duration:** 8 min
- **Started:** 2026-03-23T01:50:18Z
- **Completed:** 2026-03-23T01:58:28Z
- **Tasks:** 2
- **Files modified:** 1

## Key Results

- **Order zero condition PASSES** for the naive action pi(a) = block_diag(kron(a, I_n), kron(a, I_n)) at n=2,3,4: all 353 commutator pairs [pi(E_ij), pi_o(E_kl)] are exactly zero [CONFIDENCE: HIGH]
- **pi_o is a *-representation of the opposite algebra A^op**: pi_o(a) pi_o(b) = pi_o(b*a) and pi_o(a^dagger) = pi_o(a)^dagger verified at all n [CONFIDENCE: HIGH]
- **[gamma, pi(a)] = 0 FAILS** for ALL non-scalar matrix units: only the trivial subalgebra C*I commutes with gamma [CONFIDENCE: HIGH]
- **KO-dimension 6 sign relations verified**: J^2 = +1, J gamma = -gamma J at all n [CONFIDENCE: HIGH]
- **Gamma eigenvalue pattern matches Connes SM analog**: wedge^2-particle -> gamma = -1 (left-handed), Sym^2-particle -> gamma = +1 (right-handed), with reversed signs in antiparticle sector [CONFIDENCE: HIGH]
- **Commutant of pi(M_n(C)) has dimension 4n^2** = dim(M_2(C) tensor M_n(C)); pi_o generates an n^2-dimensional subalgebra within it [CONFIDENCE: HIGH]

## Task Commits

1. **Task 1: Build and verify order zero at n=2 with both algebra actions** - `cbd7401` (validate)
2. **Task 2: Extend verification to n=3,4 and run full consistency suite** - `a1083e8` (validate)

## Files Created/Modified

- `tests/test_order_zero.py` - 52-test pytest suite verifying all order zero and spectral triple consistency conditions at n=2,3,4

## Next Phase Readiness

- Order zero verified -- Plan 03 (analytical proof) can proceed with confidence that the algebraic identity holds
- The [gamma, pi(a)] = 0 failure is a genuine constraint: downstream phases must either modify the algebra action, modify gamma, or work with an odd spectral triple
- Three resolution paths identified: (a) algebra action respecting SWAP decomposition, (b) different chirality operator, (c) odd spectral triple without gamma

## Contract Coverage

- Claim IDs advanced: claim-sympy-order-zero -> passed, claim-j-consistency -> passed
- Deliverable IDs produced: deliv-test-code -> tests/test_order_zero.py (passed)
- Acceptance test IDs run: test-all-commutators-n2 -> passed, test-all-commutators-n34 -> passed, test-pi-o-rep-axioms -> passed, test-j-properties -> passed, test-gamma-properties -> passed
- Reference IDs surfaced: ref-connes1995 -> cited, ref-paper6 -> read, used
- Forbidden proxies rejected: fp-partial-basis -> rejected (all n^4 pairs tested), fp-numerical-only -> rejected (integer arithmetic is exact)
- Decisive comparison verdicts: claim-sympy-order-zero -> pass (353/353 commutators zero)

## Equations Derived

**Eq. (13-02.1): Opposite action formula**

$$
\pi_o(b) = J_{\text{matrix}} \cdot \overline{\pi(b^\dagger)} \cdot J_{\text{matrix}}
$$

where J is antilinear with real $J_{\text{matrix}}$ satisfying $J_{\text{matrix}}^2 = I$.

**Eq. (13-02.2): SWAP conjugation identity**

$$
P \cdot (a \otimes I_n) \cdot P = I_n \otimes a
$$

This identity is why $[\gamma, \pi(a)] \neq 0$ for $a \neq c \cdot I$: the SWAP conjugation maps $a \otimes I$ to $I \otimes a$, which is different.

**Eq. (13-02.3): Commutant dimension**

$$
\dim\left(\text{comm}(\pi(M_n(\mathbb{C})))\right) = 4n^2 = \dim\left(M_2(\mathbb{C}) \otimes M_n(\mathbb{C})\right)
$$

## Validations Completed

- Order zero: 353 total commutators verified exactly zero (16 at n=2, 81 at n=3, 256 at n=4)
- J^2 = I: verified at n=2,3,4 by direct matrix multiplication
- J gamma = -gamma J: verified at n=2,3,4 (anticommutator is exactly zero)
- gamma^2 = I: verified at n=2,3,4
- gamma = gamma^dagger: verified at n=2,3,4
- pi_o opposite multiplication: all n^4 pairs at each n confirm pi_o(a) pi_o(b) = pi_o(b*a)
- pi_o *-preservation: all n^2 basis elements at each n confirm pi_o(a^dagger) = pi_o(a)^dagger
- pi_o linear independence: rank = n^2 at each n (full rank)
- Sector dimensions: Sym^2 = n(n+1)/2, wedge^2 = n(n-1)/2 verified at each n
- [gamma, pi(a)] = 0 failure: confirmed analytically via P kron(a,I) P = kron(I,a)

## Decisions Made

- Used NumPy integer-matrix arithmetic instead of SymPy symbolic: matrix units are 0/1 matrices, so float64 arithmetic is exact (no rounding error for sums of products of 0s and 1s with magnitude < 2^52)
- Identified pi_o multiplication rule as opposite algebra (pi_o(a) pi_o(b) = pi_o(b*a)), consistent with Connes' framework where pi_o is a representation of A^op

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 4 - Missing Component] pi_o multiplicativity test needed opposite algebra convention**

- **Found during:** Task 1 (diagnostic report)
- **Issue:** Plan specified "pi_o(E_ij * E_kl) = pi_o(E_ij) * pi_o(E_kl)" but pi_o is actually a representation of A^op, so the correct condition is pi_o(a) pi_o(b) = pi_o(b*a)
- **Fix:** Changed test to verify opposite algebra multiplicativity pi_o(a) @ pi_o(b) = pi_o(b @ a)
- **Files modified:** tests/test_order_zero.py
- **Verification:** All n^4 pairs pass at n=2,3,4
- **Committed in:** cbd7401 (Task 1 commit)

---

**Total deviations:** 1 auto-fixed (1 missing component)
**Impact on plan:** Corrected the multiplicativity convention to match standard NCG. No scope creep.

## Issues Encountered

- [gamma, pi(a)] = 0 fails for ALL non-scalar matrix units, not just off-diagonal ones. This is because P kron(E_ii, I) P = kron(I, E_ii) != kron(E_ii, I) for any i when n > 1. The even condition is a genuine obstruction for the naive algebra action with SWAP-based chirality.

## Open Questions

- What algebra action on H = C^{n^2} + C^{n^2} commutes with gamma = [[P,0],[0,-P]]? The operators commuting with P on C^n x C^n are exactly the commutant of GL(n) diagonal = Span{I, P} (by Schur-Weyl for S_2). So the only operators of the form pi_sector(a) commuting with P are linear combinations of I and P, which form a 2-dimensional commutative algebra -- far smaller than M_n(C).
- Should the spectral triple be odd (no gamma)? The order zero condition passes without gamma; the issue is exclusively with the even structure.
- Can gamma be redefined to commute with the natural algebra action while preserving J gamma = -gamma J?

---

_Phase: 13-order-zero-representation-theory, Plan: 02_
_Completed: 2026-03-22_

## Self-Check: PASSED

- [x] tests/test_order_zero.py exists
- [x] Checkpoint cbd7401 exists
- [x] Checkpoint a1083e8 exists
- [x] All 52 tests pass (pytest exits 0)
- [x] Convention consistency: all operators use same J, gamma, P, pi definitions throughout
- [x] Contract coverage: all claim/deliverable/test/reference/proxy IDs present in contract_results
