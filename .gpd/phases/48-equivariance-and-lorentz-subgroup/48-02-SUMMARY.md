---
phase: 48-equivariance-and-lorentz-subgroup
plan: 02
depth: full
one-liner: "V_0 stabilizer so(3) x so(6) classified: so(3) = rotation subalgebra of Lorentz group (eta-compatible), so(6) = compact internal, pi_u equivariant under all 18 stabilizer generators"
subsystem: derivation
tags: [spin9, stabilizer, lorentz, equivariance, octonions, jordan-algebra, so3, so6]

requires:
  - phase: 48-equivariance-and-lorentz-subgroup
    plan: 01
    provides: "V_0 stabilizer = so(3) x so(6), dim 18, as 10x10 matrices"
  - phase: 46-v-0-algebraic-foundation-and-pi-u-projection
    provides: "pi_u projection, det_2 Gram = diag(+1,-1,-1,-1), spacetime indices {0,1,2,9}"
  - phase: 47-d-ijk-tensor-and-uniqueness-theorems
    provides: "Spin(9) 10-dim vector rep on V_0, F_4 invariance"

provides:
  - "so(3) rotation subalgebra identified with 3 generators satisfying eta L + L^T eta = 0"
  - "so(6) internal subalgebra verified compact (Killing eigenvalues all -2)"
  - "pi_u equivariance proved for all 18 stabilizer generators (max err 5.2e-17)"
  - "18 mixing generators identified as coset spin(9)/stab(u)"
  - "Minkowski basis transformation B for V_0 spacetime -> h_2(C_u)"
  - "Compact/non-compact distinction: so(3) = maximal compact subalgebra of so(3,1)"

affects: [49-paper-assembly, lorentz-identification, ALGB-03]

methods:
  added: [Minkowski-basis-transformation, eta-compatibility-check, equivariance-verification]
  patterns: [block-diagonal-implies-equivariance, compact-stabilizer-gives-rotation-subalgebra]

key-files:
  modified: [code/octonion_algebra.py, derivations/48-lorentz-equivariance.tex]

key-decisions:
  - "Stabilizer spacetime block has dim 3 (not 6): only rotations, no boosts, because Spin(9) is compact"
  - "The correct claim is so(3) = rotation subalgebra = maximal compact subalgebra of so(3,1), not so(3,1) itself"
  - "Equivariance follows trivially from block-diagonality but verified numerically for all generators"

patterns-established:
  - "V_0 spacetime Gram in V_0 coords: diag(0.25, -0.25, -1, -1)"
  - "Minkowski basis: B = [[1/2,0,0,0],[0,0,1,0],[0,0,0,1],[0,1/2,0,0]]"
  - "Rotation generators have coefficient 1/2 in structure constants due to gamma_ab/4 normalization"

conventions:
  - "Cl(9,0): {gamma_a, gamma_b} = 2 delta_{ab} I_16"
  - "spin(9) generators = gamma_a gamma_b / 4 for a < b"
  - "Metric signature: (+,-,-,-) on h_2(C_u) via det_2"
  - "u = e_7"
  - "Spacetime S = {0,1,2,9}, Internal I = {3,4,5,6,7,8}"

plan_contract_ref: ".gpd/phases/48-equivariance-and-lorentz-subgroup/48-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-lorentz-embedding:
      status: partial
      summary: "The spacetime block of the V_0 stabilizer is so(3) (dim 3), the ROTATION subalgebra of so(3,1), not the full so(3,1) (dim 6). The 3 generators satisfy eta L + L^T eta = 0 (max err 2.2e-16). Boosts do not exist in compact spin(9). so(3) = maximal compact subalgebra of so(3,1)."
      linked_ids: [deliv-code, deliv-derivation, test-lorentz-commutation, test-metric-compatibility, test-lorentz-dim, ref-baez, ref-phase46]
    claim-internal-so6:
      status: passed
      summary: "6x6 internal block is so(6) = su(4), compact, dim 15. Killing form all eigenvalues = -2, negative definite."
      linked_ids: [deliv-code, deliv-derivation, test-internal-dim, test-internal-killing, ref-krasnov]
    claim-equivariance:
      status: passed
      summary: "pi_u equivariant under ALL 18 stabilizer generators: P_S L = L_S P_S verified for all generators and all 10 basis vectors, max error 5.2e-17."
      linked_ids: [deliv-code, deliv-derivation, test-equivariance-all, ref-phase46]
    claim-mixing-identification:
      status: passed
      summary: "18 mixing generators identified as coset spin(9)/stab(u). Combined stabilizer + coset span all 36 dim of spin(9) (rank 36 verified)."
      linked_ids: [deliv-code, deliv-derivation, test-mixing-count, test-complement, ref-phase47]
  deliverables:
    deliv-code:
      status: passed
      path: "code/octonion_algebra.py"
      summary: "Function verify_lorentz_equivariance() implemented with full classification: rotation/internal separation, Minkowski basis, eta-compatibility, Killing forms, equivariance, mixing count."
      linked_ids: [claim-lorentz-embedding, claim-internal-so6, claim-equivariance, claim-mixing-identification]
    deliv-derivation:
      status: passed
      path: "derivations/48-lorentz-equivariance.tex"
      summary: "LaTeX derivation summary with stabilizer theorem, Lorentz rotation identification, equivariance proof, physical interpretation table, and precise compact/non-compact framing."
      linked_ids: [claim-lorentz-embedding, claim-internal-so6, claim-equivariance, claim-mixing-identification]
  acceptance_tests:
    test-lorentz-commutation:
      status: passed
      summary: "3 rotation generators satisfy so(3) commutation relations [J_i, J_j] = (1/2) epsilon_{ijk} J_k with zero residual. Structure constants exact to machine precision."
      linked_ids: [claim-lorentz-embedding, deliv-code]
    test-metric-compatibility:
      status: passed
      summary: "All 3 rotation generators satisfy eta L_mink + L_mink^T eta = 0 with max error 2.2e-16 < 1e-13."
      linked_ids: [claim-lorentz-embedding, deliv-code]
    test-lorentz-dim:
      status: partial
      summary: "Spacetime block has rank 3 (not 6). Only the rotation subalgebra so(3) is realized in compact spin(9). The 3 missing boost generators do not exist in spin(9)."
      linked_ids: [claim-lorentz-embedding, deliv-code]
    test-internal-dim:
      status: passed
      summary: "Internal block has rank 15 (exactly as expected for so(6))."
      linked_ids: [claim-internal-so6, deliv-code]
    test-internal-killing:
      status: passed
      summary: "so(6) Killing form negative definite: all 15 eigenvalues = -2. Compact real form confirmed."
      linked_ids: [claim-internal-so6, deliv-code]
    test-equivariance-all:
      status: passed
      summary: "P_S @ L @ e_k = L_S @ P_S @ e_k verified for all 18 stabilizer generators and all 10 basis vectors. Max error 5.15e-17 < 1e-14."
      linked_ids: [claim-equivariance, deliv-code]
    test-mixing-count:
      status: passed
      summary: "18 mixing generators = 36 - 18 = coset dimension. Correct."
      linked_ids: [claim-mixing-identification, deliv-code]
    test-complement:
      status: passed
      summary: "Stabilizer (18) + coset (18) span all 36 dimensions of spin(9). Rank of combined set = 36."
      linked_ids: [claim-mixing-identification, deliv-code]
  references:
    ref-baez:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Baez 2002 SL(2,K) = Spin(dim(K)+1,1) framework cited. Applied: SU(2) c Spin(9) acts as SO(3) c SO(3,1) on h_2(C_u). Full SL(2,C) does not embed in compact Spin(9)."
    ref-phase46:
      status: completed
      completed_actions: [use]
      missing_actions: []
      summary: "det_2 Gram = diag(+1,-1,-1,-1) used for Minkowski basis. pi_u rank 4 on V_0 used for equivariance definition."
    ref-krasnov:
      status: completed
      completed_actions: [compare]
      missing_actions: []
      summary: "G_SM (dim 8) from V_{1/2} stabilizer compared: G_SM c stab(u) (dim 18). The 15-8=7 extra generators in so(6) preserve V_0 splitting but do not commute with J_u on V_{1/2}."
    ref-phase47:
      status: completed
      completed_actions: [use]
      missing_actions: []
      summary: "Spin(9) 10-dim vector rep verified (630 invariance tests). 36 generators as 10x10 matrices used throughout."
  forbidden_proxies:
    fp-non-compact-embedding:
      status: rejected
      notes: "Carefully avoided claiming SL(2,C) embeds in compact Spin(9). Correct statement: SU(2) c Spin(9) acts as SO(3) c SO(3,1) on (h_2(C_u), det_2). The rotation subalgebra so(3) is the maximal compact subalgebra of so(3,1)."
    fp-stabilizer-confusion:
      status: rejected
      notes: "V_0 stabilizer (dim 18 = so(3) x so(6)) clearly distinguished from V_{1/2} stabilizer (dim 8 = G_SM). G_SM c stab(u) verified."
    fp-incomplete-equivariance:
      status: rejected
      notes: "Equivariance verified for ALL 18 stabilizer generators x ALL 10 basis vectors = 180 checks. Not just a sample."
    fp-ignoring-extra-stabilizer:
      status: rejected
      notes: "so(6) internal factor fully analyzed: Killing form, dimension, relationship to G_SM, physical interpretation as W-sector symmetry."
  uncertainty_markers:
    weakest_anchors:
      - "The Minkowski basis transformation B assumes the V_0 coordinate ordering from Phase 46 -- if that ordering changes, B changes"
      - "The claim that boosts 'do not exist' in spin(9) is standard but might be misleading -- they exist as generators of a non-compact real form of the complexified algebra"
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations:
      - "Spacetime block dim = 3, not 6. This is a physical result (compact group), not an error. Documented as key finding."

comparison_verdicts:
  - subject_id: claim-lorentz-embedding
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-baez
    comparison_kind: benchmark
    metric: "subalgebra_identification"
    threshold: "so(3) rotation subalgebra of so(3,1) embedded in compact spin(9)"
    verdict: pass
    recommended_action: "Accept so(3) as the maximal Lorentz content of the compact stabilizer. Boosts require non-compact extension."
    notes: "dim = 3, not 6. Consistent with compactness of Spin(9). The result is physically correct and matches Baez 2002 framework when restricted to compact subgroup."
  - subject_id: claim-equivariance
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase46
    comparison_kind: prior_work
    metric: "max_equivariance_error"
    threshold: "< 1e-14"
    verdict: pass
    recommended_action: "Equivariance established. pi_u is Spin(9)-equivariant when restricted to the stabilizer."
    notes: "Max error 5.15e-17, well below threshold."

duration: 10min
completed: 2026-04-12
---

# Phase 48 Plan 02: Lorentz Subalgebra Identification and Equivariance Proof

**V_0 stabilizer so(3) x so(6) classified: so(3) = rotation subalgebra of Lorentz group (eta-compatible), so(6) = compact internal, pi_u equivariant under all 18 stabilizer generators**

## Performance

- **Duration:** ~10 min
- **Started:** 2026-04-12
- **Completed:** 2026-04-12
- **Tasks:** 2
- **Files modified:** 2

## Key Results

- Spacetime block of stabilizer has dim 3 (rotations only), not 6: boosts cannot exist in compact spin(9) [CONFIDENCE: HIGH]
- All 3 rotation generators satisfy eta L_mink + L_mink^T eta = 0 (max err 2.2e-16), confirming they are Lorentz-compatible [CONFIDENCE: HIGH]
- so(6) internal Killing form negative definite: all 15 eigenvalues = -2, confirming compact so(6) = su(4) [CONFIDENCE: HIGH]
- pi_u equivariance verified for all 18 stabilizer generators x 10 basis vectors (max err 5.2e-17) [CONFIDENCE: HIGH]
- 18 mixing (coset) generators span the tangent space to the orbit of u-choices in S^6 [CONFIDENCE: HIGH]
- G_SM (dim 8) contained in stabilizer (dim 18) with residual 4.85e-15 [CONFIDENCE: HIGH]

## Task Commits

1. **Task 1: Identify Lorentz and internal subalgebras from V_0 stabilizer** - `4d73a711` (derive)
2. **Task 2: Write derivation summary and physical interpretation** - `d7ec2425` (document)

## Files Created/Modified

- `code/octonion_algebra.py` - Added `verify_lorentz_equivariance()` function
- `derivations/48-lorentz-equivariance.tex` - Stabilizer structure theorem, equivariance proof, physical interpretation

## Next Phase Readiness

- Stabilizer structure theorem complete: so(3) x so(6), dim 18, equivariant under pi_u
- The compact spin(9) contains the rotation subalgebra of so(3,1), not the full Lorentz algebra
- For paper assembly: the correct statement is that choosing u breaks Spin(9) to Spin(3) x Spin(6), where Spin(3) = SU(2) acts as spatial rotations on h_2(C_u)
- Internal so(6) = su(4) contains G_SM (dim 8) as subalgebra

## Contract Coverage

- Claims: claim-lorentz-embedding -> partial (so(3) not so(3,1)), claim-internal-so6 -> passed, claim-equivariance -> passed, claim-mixing-identification -> passed
- Deliverables: deliv-code -> passed, deliv-derivation -> passed
- Acceptance tests: test-lorentz-commutation -> passed, test-metric-compatibility -> passed, test-lorentz-dim -> partial (3 not 6), test-internal-dim -> passed, test-internal-killing -> passed, test-equivariance-all -> passed, test-mixing-count -> passed, test-complement -> passed
- References: ref-baez -> cited, ref-phase46 -> used, ref-krasnov -> compared, ref-phase47 -> used
- Forbidden proxies: all 4 -> rejected
- Comparison verdicts: claim-lorentz-embedding -> pass (so(3) correctly identified), claim-equivariance -> pass (max err 5.2e-17)

## Equations Derived

**Eq. (48.5):** Minkowski basis transformation from V_0 spacetime coords [c0,c1,c2,c9]:

$$B = \begin{pmatrix} 1/2 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 1/2 & 0 & 0 \end{pmatrix}, \quad L_{\mathrm{Mink}} = B \, L_S \, B^{-1}$$

**Eq. (48.6):** Rotation generators in Minkowski basis:

$$J_{12} = \begin{pmatrix} 0&0&0&0 \\ 0&0&1/2&0 \\ 0&-1/2&0&0 \\ 0&0&0&0 \end{pmatrix}, \quad J_{13} = \begin{pmatrix} 0&0&0&0 \\ 0&0&0&-1/2 \\ 0&0&0&0 \\ 0&1/2&0&0 \end{pmatrix}, \quad J_{23} = \begin{pmatrix} 0&0&0&0 \\ 0&0&0&0 \\ 0&0&0&-1/2 \\ 0&0&1/2&0 \end{pmatrix}$$

**Eq. (48.7):** eta-compatibility (Lorentz generator defining relation):

$$\eta \, L_{\mathrm{Mink}} + L_{\mathrm{Mink}}^T \, \eta = 0, \quad \eta = \mathrm{diag}(+1,-1,-1,-1)$$

**Eq. (48.8):** so(3) commutation relations:

$$[J_{13}, J_{23}] = -\tfrac{1}{2} J_{12}, \quad [J_{13}, J_{12}] = +\tfrac{1}{2} J_{23}, \quad [J_{23}, J_{12}] = -\tfrac{1}{2} J_{13}$$

**Eq. (48.9):** Equivariance theorem:

$$\pi_u(L \cdot Y) = L|_{h_2(\mathbb{C}_u)} \cdot \pi_u(Y), \quad \forall\, L \in \mathfrak{stab}(u),\; Y \in V_0$$

## Validations Completed

- eta-compatibility: max|eta L + L^T eta| = 2.2e-16 < 1e-13 for all 3 rotation generators
- so(3) commutation: [J_i, J_j] = (1/2) epsilon_{ijk} J_k, exact to machine precision
- so(6) Killing form: all 15 eigenvalues = -2, negative definite (compact)
- so(3) Killing form: all 3 eigenvalues = -0.5, negative definite (compact)
- Cross-brackets [so(3), so(6)] = 0: max norm 5.3e-17
- Equivariance: max error 5.15e-17 over all 18 generators x 10 basis vectors
- Dimension accounting: 3 + 15 = 18 stabilizer, 18 + 18 = 36 spin(9)
- G_SM (dim 8) contained in stabilizer: residual 4.85e-15

## Decisions & Deviations

### Key Finding: Spacetime block dim = 3, not 6

- **Expected (Plan 02):** 6 independent spacetime generators forming so(3,1)
- **Actual:** 3 independent spacetime generators forming so(3)
- **Resolution:** This is physically correct. The compact spin(9) cannot contain the non-compact boost generators of so(3,1). Only the rotation subalgebra so(3) (maximal compact subalgebra of so(3,1)) embeds. Plan adapted: report so(3) as the rotation content of the Lorentz algebra, not the full so(3,1).
- **Impact:** claim-lorentz-embedding marked partial (so(3), not so(3,1)). The physics is correct; the plan's prediction was wrong.

### Deviation: Plan expected 6 spacetime generators [Rule 5 - Physics Redirect]

- **Found during:** Task 1 Step 2
- **Issue:** Plan expected rank 6 for spacetime blocks (full so(3,1)). Computation gives rank 3 (so(3) only). This was already flagged in critical context.
- **Fix:** Adapted analysis to report so(3) correctly. Verified boosts are absent from ALL 36 spin(9) generators (not just stabilizer). The correct physics: compact group gives compact subalgebra.
- **Verification:** Rank of ALL 36 spacetime blocks = 3. No boost-like generators exist anywhere in spin(9).
- **Impact:** No scope change needed. The equivariance result and internal symmetry are unaffected.

**Total deviations:** 1 (Rule 5, physics redirect -- plan prediction corrected)
**Impact on plan:** Plan's claim-lorentz-embedding prediction was wrong (so(3,1) vs so(3)). The physics result is more restrictive but correct. All other claims unaffected.

## Open Questions

- Can the boosts be recovered by analytic continuation (Wick rotation) from compact Spin(4) to non-compact Spin(3,1)?
- What is the physical significance of the Killing form ratio -2/-0.5 = 4 between so(6) and so(3)?
- The 18-dim coset = tangent space to Spin(9)/Stab(u). What is the geometry of this homogeneous space?
- How does the so(6) internal symmetry reduce to the SU(3) x U(1) of the Standard Model? (7 generators must be broken)

## Self-Check: PASSED

- [x] code/octonion_algebra.py exists with verify_lorentz_equivariance
- [x] derivations/48-lorentz-equivariance.tex exists with so(3,1), equivariance, stabilizer
- [x] Commit 4d73a711 exists
- [x] Commit d7ec2425 exists
- [x] All numerical values in SUMMARY match computation
- [x] Convention consistency: Cl(9,0), gamma_ab/4, (+,-,-,-), u=e_7 throughout
- [x] No forbidden proxies violated
- [x] All contract IDs accounted for

---

_Phase: 48-equivariance-and-lorentz-subgroup, Plan: 02_
_Completed: 2026-04-12_
