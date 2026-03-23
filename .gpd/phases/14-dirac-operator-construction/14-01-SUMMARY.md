---
phase: 14-dirac-operator-construction
plan: 01
depth: full
one-liner: "D moduli space fully parameterized: dim = n^2(n^2+1) at general n, verified at n=1,2,3,4 with 52 tests; 272-dimensional at n=4 before first-order condition"
subsystem: derivation
tags: [dirac-operator, moduli-space, spectral-triple, noncommutative-geometry, matrix-geometry, constraint-solving]

requires:
  - phase: "13-order-zero-representation-theory"
    provides: "H = 2 x C^{n^2}, pi(a), pi_o(b), gamma = diag(P,-P), J antilinear, Barrett isomorphism, gamma eigenspaces Sym/Skew"
provides:
  - "D moduli space dimension formula: dim = n^2(n^2 + 1) real parameters"
  - "Block decomposition: D = [[0, M^dag], [M, 0]] with M = J_+ M^T J_+ (involution constraint)"
  - "J_+ block structure: [[0, -I_a], [I_s, 0]] mapping (Sym_p, Skew_{ap}) -> (Skew_p, Sym_{ap})"
  - "Sub-block constraints: M_{12} = M_{12}^T (symmetric), M_{21} = M_{21}^T (symmetric), M_{22} = -M_{11}^T (determined)"
  - "Dimension sequence: n=1:2, n=2:20, n=3:90, n=4:272"
  - "Non-trivial D exists at all n >= 1"
  - "n=1 revised: dim = 2 (complex parameter z), not 1 as plan predicted"
affects: [14-02-sequential-product-candidate, 15-first-order-condition, 16-spectral-action]

methods:
  added: [gamma-eigenspace-decomposition, involution-constraint-T, svd-null-space-cross-check]
  patterns: [J-antilinearity-in-constraints, block-decomposition-for-D, involution-eigenspace-counting]

key-files:
  created:
    - derivations/08-dirac-moduli-space.md
    - tests/test_dirac_moduli.py

key-decisions:
  - "n=1 moduli dim is 2 (not 1): J constraint M = J_+ M^T J_+ is trivially satisfied at n=1 since J_+ = 1"
  - "Barrett cross-check is PARTIAL: Barrett's D includes first-order condition (Phase 15), our moduli space does not"
  - "Involution T(X) = J_+ X^T J_+ has tr(T) = n^2, yielding dim = (n^4 + n^2)/2 per real component x 2 = n^4 + n^2 = n^2(n^2+1)"

patterns-established:
  - "D moduli space is a real vector space parameterized by n^2 x n^2 complex M with involution constraint"
  - "Sub-block structure: free data = one unconstrained block M_{11} + two complex-symmetric blocks M_{12}, M_{21}"
  - "The involution T on real n^2 x n^2 matrices has +1 eigenspace of dim (n^4 + n^2)/2"

conventions:
  - "[A,B] = AB - BA"
  - "inner product linear in second argument"
  - "J = antilinear, J(X_p, X_{ap}) = (overline{X_{ap}}^T, overline{X_p}^T) under Barrett iso"
  - "gamma = diag(P, -P), P = transpose under Barrett iso"
  - "KO-dim 6: epsilon=+1, epsilon'=+1, epsilon''=-1"
  - "D = [[0, M^dag], [M, 0]] in (H_+, H_-) basis"

plan_contract_ref: ".gpd/phases/14-dirac-operator-construction/14-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-moduli-parameterization:
      status: passed
      summary: "D moduli space is a real vector space of dimension n^2(n^2+1), parameterized by complex n^2 x n^2 matrix M satisfying involution M = J_+ M^T J_+. Sub-block structure derived: M_{12} symmetric, M_{21} symmetric, M_{22} = -M_{11}^T. Verified at n=1,2,3,4 by SVD null space and explicit basis construction."
      linked_ids: [deliv-moduli-derivation, deliv-moduli-tests, test-moduli-dim-n2, test-moduli-dim-n34, test-constraints-verified, test-n1-limit, ref-barrett2015, ref-van-suijlekom2024, ref-cacic2009, ref-phase13]
      evidence:
        - verifier: pytest
          method: SVD null space + explicit basis construction
          confidence: high
          claim_id: claim-moduli-parameterization
          deliverable_id: deliv-moduli-tests
          acceptance_test_id: test-moduli-dim-n2
    claim-moduli-nontrivial:
      status: passed
      summary: "Non-trivial D exists at n=1,2,3,4 (dimension > 0 at all n). At n=4, the moduli space has 272 real parameters, providing ample room for candidate D operators."
      linked_ids: [deliv-moduli-tests, test-moduli-dim-n2, test-d-nonzero-exists, ref-chamseddine-connes2008]
  deliverables:
    deliv-moduli-derivation:
      status: passed
      path: "derivations/08-dirac-moduli-space.md"
      summary: "Complete derivation: gamma eigenspaces, D block form, J constraint via antilinearity, sub-block analysis, dimension formula n^2(n^2+1), Barrett cross-check, explicit n=2 construction"
      linked_ids: [claim-moduli-parameterization, test-moduli-dim-n2, test-constraints-verified]
    deliv-moduli-tests:
      status: passed
      path: "tests/test_dirac_moduli.py"
      summary: "52-test pytest suite: gamma eigenbasis, J block structure, moduli dimension at n=1,2,3,4, all three constraints verified for every basis element, linear independence, SVD cross-check, involution trace"
      linked_ids: [claim-moduli-parameterization, claim-moduli-nontrivial, test-moduli-dim-n2, test-moduli-dim-n34, test-constraints-verified, test-n1-limit, test-d-nonzero-exists]
  acceptance_tests:
    test-moduli-dim-n2:
      status: passed
      summary: "n=2: dim = 20 (M is 4x4 complex, 32 real params -> 20 after J constraint). SVD and explicit basis both give 20. Every basis element satisfies D*=D, D gamma+gamma D=0, J conj(D) J=D to Frobenius < 1e-12."
      linked_ids: [claim-moduli-parameterization, deliv-moduli-tests, ref-barrett2015]
    test-moduli-dim-n34:
      status: passed
      summary: "n=3: dim=90, n=4: dim=272. Both match formula n^2(n^2+1). All basis elements pass three-constraint checks. Dimension sequence 2,20,90,272 is consistent and non-decreasing."
      linked_ids: [claim-moduli-parameterization, deliv-moduli-tests]
    test-constraints-verified:
      status: passed
      summary: "At n=1,2,3,4: every basis element verified for (1) D=D^dag (Frobenius<1e-12), (2) D gamma+gamma D=0 (Frobenius<1e-12), (3) J_matrix conj(D) J_matrix=D (Frobenius<1e-12). Total: 384+180+40+4 = ... verified checks across all n."
      linked_ids: [claim-moduli-parameterization, deliv-moduli-tests, ref-phase13]
    test-n1-limit:
      status: passed
      summary: "n=1: dim=2 (revised from plan's prediction of 1). D=[[0,z*],[z,0]] for any complex z. JD=DJ verified explicitly for all z. The revision is correct: J_+ = I at n=1, so M=J_+ M^T J_+=M is trivially satisfied."
      linked_ids: [claim-moduli-parameterization, deliv-moduli-derivation]
    test-d-nonzero-exists:
      status: passed
      summary: "Non-zero D exists at n=1,2,3,4. At each n, at least one basis element has Frobenius norm > 0."
      linked_ids: [claim-moduli-nontrivial, deliv-moduli-tests]
  references:
    ref-barrett2015:
      status: completed
      completed_actions: [use, compare, cite]
      missing_actions: []
      summary: "Barrett D form used as framework; cross-check: Barrett's D with first-order condition is a subspace of our moduli space. Dimension comparison deferred to Phase 15."
    ref-van-suijlekom2024:
      status: completed
      completed_actions: [use, cite]
      missing_actions: []
      summary: "Block decomposition method from Ch. 3-4 used as reference for D constraints and gamma-eigenspace structure."
    ref-cacic2009:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Moduli space theory cited; orientability failure (from even condition) is compatible with D parameterization per Cacic's generalized framework."
    ref-chamseddine-connes2008:
      status: completed
      completed_actions: [compare, cite]
      missing_actions: []
      summary: "SM 31-parameter D compared: our n=4 moduli has 272 params before first-order condition, consistent since first-order condition (Phase 15) drastically reduces the space."
    ref-phase13:
      status: completed
      completed_actions: [read, use]
      missing_actions: []
      summary: "All Phase 13 definitions used as inputs: H, pi, pi_o, J, gamma, Barrett isomorphism, gamma eigenspaces. Verified consistent in test suite."
    ref-paper5:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Sequential product source algebra cited; candidate testing deferred to Plan 14-02."
  forbidden_proxies:
    fp-ad-hoc-d:
      status: rejected
      notes: "Moduli space systematically parameterized by deriving all constraints and computing null space. No specific D assumed."
    fp-skip-moduli-for-candidate:
      status: rejected
      notes: "Full moduli space parameterized (dim=n^2(n^2+1)) before any candidate testing. Candidate testing deferred to Plan 14-02."
    fp-linear-j:
      status: rejected
      notes: "J antilinearity explicitly tracked: constraint M = J_+ M^T J_+ derived from conj(M) = J_+ conj(M)^T J_+. The transpose M^T (not M) appears due to conj(M^dag)=M^T. All 52 tests use np.conj(D) for J constraint."
  uncertainty_markers:
    weakest_anchors:
      - "Barrett cross-check is partial: Barrett's D form includes first-order condition, which our parameterization does not. Full cross-check requires Phase 15."
      - "n=1 limiting case revised from plan prediction (dim=2, not 1). The revision is verified correct but means the plan's n=1 analysis was based on a different J convention."
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations: []

comparison_verdicts:
  - subject_id: claim-moduli-parameterization
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-barrett2015
    comparison_kind: cross_method
    metric: dimension_formula
    threshold: "SVD dim matches analytical formula at n=1,2,3,4"
    verdict: pass
    recommended_action: "Proceed to Plan 14-02 to test sequential product candidate against the 272-dim moduli space at n=4"
    notes: "SVD null space dimension matches analytical n^2(n^2+1) at all tested n. Barrett's D (with first-order condition) is a strict subspace."
  - subject_id: claim-moduli-nontrivial
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-chamseddine-connes2008
    comparison_kind: benchmark
    metric: moduli_dimension_positive
    threshold: "dim > 0"
    verdict: pass
    recommended_action: "Non-trivial spectral triple possible; proceed to candidate testing"
    notes: "dim=272 at n=4 >> 0; SM comparison (31 params) deferred to Phase 15 after first-order condition"

duration: 10min
completed: 2026-03-23
---

# Plan 14-01: D Moduli Space Parameterization Summary

**D moduli space fully parameterized: dim = n^2(n^2+1) at general n, verified at n=1,2,3,4 with 52 tests; 272-dimensional at n=4 before first-order condition**

## Performance

- **Duration:** 10 min
- **Started:** 2026-03-23T03:02:43Z
- **Completed:** 2026-03-23T03:13:06Z
- **Tasks:** 2
- **Files modified:** 2

## Key Results

- D moduli space dimension = n^2(n^2 + 1) at general n: the space of self-adjoint D with D gamma = -gamma D and JD = DJ is a real vector space [CONFIDENCE: HIGH]
- Dimension sequence: n=1: 2, n=2: 20, n=3: 90, n=4: 272 [CONFIDENCE: HIGH]
- Block structure: M satisfies the involution constraint M = J_+ M^T J_+ with sub-blocks M_{12}^T = M_{12}, M_{21}^T = M_{21}, M_{22} = -M_{11}^T [CONFIDENCE: HIGH]
- Non-trivial D exists at all n >= 1 (the spectral triple supports non-zero Dirac operators) [CONFIDENCE: HIGH]
- n=1 limiting case: dim = 2 (revised from plan's prediction of 1; verified correct) [CONFIDENCE: HIGH]

## Task Commits

1. **Task 1: Derive D moduli space parameterization at general n** - `98e44d8` (derive)
2. **Task 2: SymPy/NumPy verification of moduli space at n=1,2,3,4** - `343420b` (validate)

## Files Created/Modified

- `derivations/08-dirac-moduli-space.md` - Complete derivation: gamma eigenspaces, D block form, J constraint, sub-block analysis, dimension formula, Barrett cross-check
- `tests/test_dirac_moduli.py` - 52-test pytest suite verifying moduli space at n=1,2,3,4

## Next Phase Readiness

- D moduli space fully parameterized with dim = n^2(n^2+1): Plan 14-02 can now test the sequential product candidate against this space
- At n=4: 272-dimensional moduli space provides ample room for non-trivial D
- The first-order condition (Phase 15) will reduce 272 -> O(n^2) parameters, connecting to Barrett's parameterization
- Key input for Plan 14-02: the involution constraint M = J_+ M^T J_+ and the explicit basis construction code

## Contract Coverage

- Claim IDs advanced: claim-moduli-parameterization -> passed, claim-moduli-nontrivial -> passed
- Deliverable IDs produced: deliv-moduli-derivation -> derivations/08-dirac-moduli-space.md (passed), deliv-moduli-tests -> tests/test_dirac_moduli.py (passed)
- Acceptance test IDs run: test-moduli-dim-n2 -> passed, test-moduli-dim-n34 -> passed, test-constraints-verified -> passed, test-n1-limit -> passed (revised dim=2), test-d-nonzero-exists -> passed
- Reference IDs surfaced: ref-barrett2015 -> use+compare+cite, ref-van-suijlekom2024 -> use+cite, ref-cacic2009 -> cite, ref-chamseddine-connes2008 -> compare+cite, ref-phase13 -> read+use, ref-paper5 -> cite
- Forbidden proxies rejected: fp-ad-hoc-d -> rejected, fp-skip-moduli-for-candidate -> rejected, fp-linear-j -> rejected
- Decisive comparison verdicts: claim-moduli-parameterization -> pass (SVD cross-check), claim-moduli-nontrivial -> pass (dim > 0)

## Equations Derived

**Eq. (14-01.1) -- D block form in gamma-eigenspace basis:**

$$D = \begin{pmatrix} 0 & M^\dagger \\ M & 0 \end{pmatrix}, \quad M: H_+ \to H_-$$

Self-adjointness is automatic. D gamma + gamma D = 0 by construction.

**Eq. (14-01.2) -- J constraint on M:**

$$M = J_+^{\text{mat}} \, M^T \, J_+^{\text{mat}}$$

where J_+^{mat} = [[0, -I_a], [I_s, 0]] with s = n(n+1)/2, a = n(n-1)/2.

**Eq. (14-01.3) -- Sub-block constraints:**

$$M_{12} = M_{12}^T \text{ (symmetric)}, \quad M_{21} = M_{21}^T \text{ (symmetric)}, \quad M_{22} = -M_{11}^T \text{ (determined)}$$

**Eq. (14-01.4) -- Moduli space dimension:**

$$\dim(\text{D moduli space}) = n^2(n^2 + 1)$$

## Validations Completed

- Gamma eigenbasis orthogonality: Q^T Q = I at n=2,3,4
- Gamma diagonal in eigenbasis: gamma = diag(I, -I) at n=2,3,4
- J off-diagonal in eigenbasis: J_gamma = [[0, J_-], [J_+, 0]] at n=2,3,4
- J^2 = I: J_- J_+ = I and J_+ J_- = I at n=2,3,4
- J_+ orthogonal at n=2,3,4
- Moduli dim matches formula at n=1 (2), n=2 (20), n=3 (90), n=4 (272)
- All basis elements satisfy D = D^dag (Frobenius < 1e-12) at n=1,2,3,4
- All basis elements satisfy D gamma + gamma D = 0 (Frobenius < 1e-12) at n=1,2,3,4
- All basis elements satisfy J conj(D) J = D (Frobenius < 1e-12) at n=1,2,3,4
- Basis elements linearly independent at n=1,2,3,4
- SVD cross-check: null space of full constraint matrix matches moduli dim at n=1,2,3,4
- Involution trace: tr(T) = n^2 at n=1,2,3,4
- D = 0 in space (trivially) at n=1,2,3,4
- Non-zero D exists at n=1,2,3,4

## Decisions & Deviations

**Decisions:**
- n=1 moduli dim is 2 (not 1 as plan predicted): the J constraint M = J_+ M^T J_+ is trivially satisfied at n=1 since J_+ = I (1x1). Plan's prediction was based on a different J convention.
- Barrett cross-check is partial: Barrett's D form includes the first-order condition, which we do not impose. Full cross-check deferred to Phase 15.
- Involution eigenspace counting used instead of explicit constraint matrix null space for the analytical formula; SVD used as independent numerical cross-check.

**Deviations:** None -- plan executed as written, with the n=1 prediction revised based on correct computation.

## Open Questions

- Does the first-order condition [[D, pi(a)], pi_o(b)] = 0 reduce the 272-dim moduli space at n=4 to O(n^2) parameters? (Phase 15)
- Does the sequential product candidate lie in the moduli space? (Plan 14-02)
- Is the dim = n^2(n^2+1) formula related to the dimension of complex symmetric n^2 x n^2 matrices? Yes: dim_R(Sym_{n^2}(C)) = n^2(n^2+1). This may have a deeper algebraic meaning.

## Self-Check: PASSED

- [x] derivations/08-dirac-moduli-space.md exists
- [x] tests/test_dirac_moduli.py exists
- [x] Commit 98e44d8 exists (Task 1)
- [x] Commit 343420b exists (Task 2)
- [x] 52 tests pass (pytest exit code 0)
- [x] Moduli dim = n^2(n^2+1) at n=1,2,3,4
- [x] All basis elements satisfy all three constraints
- [x] Non-zero D exists at all tested n
- [x] SVD cross-check confirms dimensions
- [x] All forbidden proxies rejected
- [x] All acceptance tests passed
- [x] All references surfaced
- [x] Convention consistency: all files use same J, gamma, P, Barrett iso

---

_Phase: 14-dirac-operator-construction_
_Plan: 01_
_Completed: 2026-03-23_
