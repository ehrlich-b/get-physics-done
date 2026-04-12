---
phase: 48-equivariance-and-lorentz-subgroup
plan: 01
depth: full
one-liner: "V_0 stabilizer under spin(9) is so(3) x so(6) (dim 18): so(3) on spacetime, so(6) on internal, G_SM contained"
subsystem: computation
tags: [spin9, stabilizer, lie-algebra, octonions, jordan-algebra, lorentz]

requires:
  - phase: 47-d-ijk-tensor-and-uniqueness-theorems
    provides: "F_4 invariance verified, spin(9) action on V_0 via commutator [gamma_ab/4, T_c]"
  - phase: 46-v-0-algebraic-foundation-and-pi-u-projection
    provides: "pi_u rank 4 on V_0, spacetime indices {0,1,2,9}, internal {3..8}"

provides:
  - "36 spin(9) generators as 10x10 matrices on V_0 (compute_spin9_v0_rep)"
  - "V_0 stabilizer = so(3) x so(6), dim 18, classified Killing form"
  - "G_SM (dim 8) contained in stabilizer (residual < 5e-15)"
  - "Orthonormal basis transformation D = diag(1,1,2,...,2) for V_0"

affects: [48-02-PLAN, lorentz-identification, equivariance-proof]

methods:
  added: [SVD-nullspace-for-stabilizer, Killing-form-classification]
  patterns: [commutator-action-to-matrix-rep, orthonormalization-of-T-basis]

key-files:
  modified: [code/octonion_algebra.py]

key-decisions:
  - "Stabilizer dim = 18 (not expected 21): correct because so(3,1) noncompact, only so(3) embeds in compact so(9)"
  - "V_0 rep is 1 + 9 decomposition: T_0 trivial, T_1..T_9 vector rep of so(9)"

patterns-established:
  - "V_0 orthonormal basis: D = diag(1,1,2,...,2) from G_{ab} = Tr(T_a T_b) = diag(1,1,4,...,4)"
  - "Stabilizer via SVD of off-diagonal constraint: 48 x 36 matrix, nullspace = stabilizer"

conventions:
  - "Cl(9,0): {gamma_a, gamma_b} = 2*delta_{ab}*I_16"
  - "spin(9) generators = gamma_a gamma_b / 4 for a < b"
  - "V_0 coords: [c0=beta+gamma, c1=beta-gamma, x1.c[0..7]]"
  - "Spacetime S = {0,1,2,9}, Internal I = {3,4,5,6,7,8}"

plan_contract_ref: ".gpd/phases/48-equivariance-and-lorentz-subgroup/48-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-10x10-rep:
      status: passed
      summary: "All 36 spin(9) generators correctly represented as 10x10 matrices on V_0. Antisymmetric in G-metric (max err 4.4e-16), antisymmetric in orthonormal basis (max err 2.2e-16), traceless (exact), closed Lie algebra (residual 0)."
      linked_ids: [deliv-code, test-antisymmetry, test-closure, ref-phase47]
    claim-stabilizer-dim:
      status: passed
      summary: "V_0 stabilizer has exact integer dimension 18 (SVD gap 0.71, clear separation). Decomposition: 18 + 18 = 36."
      linked_ids: [deliv-code, test-stabilizer-dim, test-stabilizer-closure, ref-phase46]
    claim-stabilizer-structure:
      status: passed
      summary: "Stabilizer = so(3) x so(6). Killing form negative definite, eigenvalues -2 (x15, so(6)) and -0.5 (x3, so(3)). Center dim = 0. so(3) acts on 4-dim spacetime block, so(6) acts on 6-dim internal block, cross-brackets zero."
      linked_ids: [deliv-code, test-killing-form, test-center, ref-baez]
  deliverables:
    deliv-code:
      status: passed
      path: "code/octonion_algebra.py"
      summary: "Functions compute_spin9_v0_rep() and compute_v0_stabilizer() implemented with full classification."
      linked_ids: [claim-10x10-rep, claim-stabilizer-dim, claim-stabilizer-structure]
  acceptance_tests:
    test-antisymmetry:
      status: passed
      summary: "All 36 generators antisymmetric in orthonormal basis: max|M + M^T| = 2.2e-16 < 1e-14. Also verified M^T G + G M = 0 in natural basis (4.4e-16)."
      linked_ids: [claim-10x10-rep, deliv-code]
    test-closure:
      status: passed
      summary: "100 random brackets of spin(9) generators all expressible in span with residual = 0 (exact to machine precision)."
      linked_ids: [claim-10x10-rep, deliv-code]
    test-stabilizer-dim:
      status: passed
      summary: "SVD of 48x36 off-diagonal constraint matrix gives 18 null singular values (all < 1e-17) and 18 nonzero (min 0.71). Clear gap > 1e-8."
      linked_ids: [claim-stabilizer-dim, deliv-code]
    test-stabilizer-closure:
      status: passed
      summary: "All 153 brackets of 18 stabilizer generators in span with max residual 5.3e-17 < 1e-12."
      linked_ids: [claim-stabilizer-dim, deliv-code]
    test-killing-form:
      status: passed
      summary: "Killing form is 18x18 real symmetric (max|K-K^T| = 0), negative definite. Eigenvalues: -2 (x15) and -0.5 (x3). Rank = 18 = full. Signature identifies so(3) x so(6)."
      linked_ids: [claim-stabilizer-structure, deliv-code]
    test-center:
      status: passed
      summary: "Center dimension = 0 (all adjoint representation norms > threshold). Algebra is semisimple."
      linked_ids: [claim-stabilizer-structure, deliv-code]
  references:
    ref-phase47:
      status: completed
      completed_actions: [use]
      missing_actions: []
      summary: "Spin(9) commutator action [gamma_ab/4, T_c] extracted from verify_f4_invariance_det3 (lines 2601-2618) and made reusable in compute_spin9_v0_rep."
    ref-phase46:
      status: completed
      completed_actions: [use]
      missing_actions: []
      summary: "4+6 splitting S={0,1,2,9}, I={3..8} from Phase 46 pi_u rank-4 result used to define stabilizer constraint."
    ref-baez:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Baez 2002 SL(2,K)=Spin(dim(K)+1,1) framework cited for theoretical context. The compact stabilizer so(3) x so(6) is consistent with Lorentz = noncompact extension."
  forbidden_proxies:
    fp-spin9-so9:
      status: rejected
      notes: "Carefully distinguished: spin(9) Lie algebra = so(9) Lie algebra, but Spin(9) != SO(9) as groups. All computations at Lie algebra level where they coincide."
    fp-approximate-dim:
      status: rejected
      notes: "Stabilizer dimension 18 determined exactly from SVD with gap 0.71 >> 1e-8. No approximation."
    fp-abstract-branching:
      status: rejected
      notes: "All results from explicit matrix computation and SVD, not from abstract Dynkin diagram arguments."
  uncertainty_markers:
    weakest_anchors:
      - "The 4+6 split indices {0,1,2,9} vs {3..8} inherited from Phase 46 -- if those are wrong, the stabilizer is wrong"
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations:
      - "Stabilizer dim = 18, not expected 21. Explained: so(3,1) is noncompact, only so(3) embeds in compact so(9). The 3 boosts are in the coset, not the stabilizer."

comparison_verdicts:
  - subject_id: claim-stabilizer-dim
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase46
    comparison_kind: prior_work
    metric: dimension_match
    threshold: "exact integer"
    verdict: pass
    recommended_action: "Proceed to Plan 02 for Lorentz identification"
    notes: "dim = 18 = 3 + 15 = so(3) + so(6), physically correct"

duration: 8min
completed: 2026-04-12
---

# Phase 48 Plan 01: Spin(9) V_0 Representation and Stabilizer Classification

**V_0 stabilizer under spin(9) is so(3) x so(6) (dim 18): so(3) on spacetime, so(6) on internal, G_SM (dim 8) contained**

## Performance

- **Duration:** ~8 min
- **Started:** 2026-04-12T13:46:35Z
- **Completed:** 2026-04-12T13:54:00Z
- **Tasks:** 2
- **Files modified:** 1

## Key Results

- 36 spin(9) generators built as 10x10 matrices on V_0, verified antisymmetric (2.2e-16), traceless, closed (residual 0) [CONFIDENCE: HIGH]
- V_0 stabilizer = so(3) x so(6), dimension 18 (not 21), SVD gap 0.71 [CONFIDENCE: HIGH]
- so(3) (dim 3) acts on spacetime block {0,1,2,9}; so(6) (dim 15) acts on internal block {3..8}; cross-brackets exactly zero [CONFIDENCE: HIGH]
- Killing form negative definite: eigenvalues -2 (x15) and -0.5 (x3), center dim = 0 [CONFIDENCE: HIGH]
- G_SM (dim 8) is a subalgebra of the stabilizer (max residual 4.85e-15) [CONFIDENCE: HIGH]

## Task Commits

1. **Task 1: Build 36 spin(9) generators as 10x10 matrices on V_0** - `a167c0c8` (derive)
2. **Task 2: Find V_0 stabilizer and classify its Lie algebra structure** - `b5e8baf2` (validate)

## Files Created/Modified

- `code/octonion_algebra.py` - Added `compute_spin9_v0_rep()` and `compute_v0_stabilizer()` functions

## Next Phase Readiness

- Stabilizer so(3) x so(6) ready for Plan 02: Lorentz subgroup identification
- so(3) on spacetime = compact rotation subgroup; the 3 boosts live in the coset (18 mixing generators)
- Key question for Plan 02: can the 3 boosts be identified among the 18 coset generators to reconstruct so(3,1)?

## Contract Coverage

- Claims: claim-10x10-rep -> passed, claim-stabilizer-dim -> passed, claim-stabilizer-structure -> passed
- Deliverables: deliv-code -> passed (code/octonion_algebra.py)
- Acceptance tests: all 6 -> passed
- References: ref-phase47 -> used, ref-phase46 -> used, ref-baez -> cited
- Forbidden proxies: all 3 -> rejected
- Comparison verdicts: claim-stabilizer-dim -> pass (dim=18 exact integer)

## Equations Derived

**Eq. (48.1):** Commutator action defining 10x10 representation:

$$[gamma_{ab}/4, \; T_c] = \sum_d M^{(ab)}_{dc} \, T_d$$

where $M^{(ab)}$ is the 10x10 matrix of the spin(9) generator labeled by $(a,b)$ with $0 \le a < b \le 8$.

**Eq. (48.2):** V_0 inner product (Gram matrix):

$$G_{ab} = \text{Tr}(T_a \, T_b) = \text{diag}(1, 1, 4, 4, 4, 4, 4, 4, 4, 4)$$

Orthonormal basis: $D = \text{diag}(1, 1, 2, \ldots, 2)$, $v_{\text{ortho}} = D \, v_{\text{natural}}$.

**Eq. (48.3):** Stabilizer decomposition:

$$\text{Stab}_{so(9)}(S \oplus I) = so(3) \oplus so(6), \quad \dim = 3 + 15 = 18$$

where $S = \{0,1,2,9\}$ (spacetime) and $I = \{3,4,5,6,7,8\}$ (internal).

**Eq. (48.4):** Killing form eigenvalue structure:

$$\text{spec}(K) = \{-2^{(\times 15)}, -0.5^{(\times 3)}\}$$

identifying the so(6) and so(3) simple factors respectively.

## Validations Completed

- Antisymmetry in orthonormal basis: max|M + M^T| = 2.2e-16 < 1e-14
- G-antisymmetry in natural basis: max|M^T G + G M| = 4.4e-16 < 1e-14
- Tracelessness: max|Tr(M)| = 0 (exact)
- Lie algebra closure: 100 random brackets, max residual = 0 (exact)
- Cross-check against verify_f4_invariance_det3 inline code: 3 generators x 2 vectors, max err = 0
- SVD gap 0.71 >> 1e-8 (clear integer dimension)
- Stabilizer closure: 153 brackets, max residual 5.3e-17
- Off-diagonal blocks all < 5.2e-17
- Killing form symmetric (exact), nondegenerate (rank 18)
- so(3) acts only on spacetime block (internal block exactly zero)
- so(6) acts only on internal block (spacetime block exactly zero)
- Cross-brackets [so(3), so(6)] = 0 (max 5.3e-17)
- Dimension accounting: 18 + 18 = 36
- G_SM (dim 8) contained in stabilizer: residual 4.85e-15

## Decisions & Deviations

### Deviation: V_0 basis is not orthonormal [Rule 4 - Missing Component]

- **Found during:** Task 1 verification
- **Issue:** Plan's antisymmetry test assumes M + M^T = 0 (orthonormal basis), but V_0 natural basis has G = diag(1,1,4,...,4)
- **Fix:** Added orthonormalization via D = diag(1,1,2,...,2). Returned both natural-basis and orthonormal-basis generators.
- **Files modified:** code/octonion_algebra.py
- **Verification:** M_ortho + M_ortho^T max err 2.2e-16; M^T G + G M max err 4.4e-16

### Key Finding: Stabilizer dim = 18, not expected 21

- **Expected:** 21 (anticipating so(3,1) + so(6) = 6 + 15)
- **Actual:** 18 = so(3) + so(6) = 3 + 15
- **Explanation:** so(3,1) is noncompact. Within the compact so(9), only the rotation subalgebra so(3) preserves the splitting. The 3 Lorentz boosts mix spacetime and internal indices and live in the 18-dim coset.
- **Impact on downstream:** Plan 02 needs to find the 3 boosts among the 18 coset generators. The Lorentz algebra so(3,1) is NOT a subalgebra of so(9); it requires going beyond the compact stabilizer.

**Total deviations:** 1 auto-fixed (Rule 4, missing normalization component)
**Impact on plan:** Necessary for correctness. No scope change.

## Open Questions

- Can the 3 Lorentz boosts be identified among the 18 coset generators by algebraic criteria?
- Does the so(6) internal factor relate to SU(4) ~ Spin(6) Pati-Salam symmetry?
- The Killing form ratio -2/-0.5 = 4: is this ratio universal or depends on the embedding?

---

_Phase: 48-equivariance-and-lorentz-subgroup, Plan: 01_
_Completed: 2026-04-12_
