---
phase: 50-weinberg-verification-spin2-universal-coupling
plan: 01
depth: full
one-liner: "SO(3,1) irrep decomposition gives 10 = 9 (spin-2) + 1 (spin-0); det_3 quadratic expansion yields M_{ab} = det_2 (kinetic, not Fierz-Pauli) -- graviton is massless"
subsystem: [derivation, validation]
tags: [spin-2, massless-graviton, weinberg-theorem, fierz-pauli, jordan-algebra, det3-expansion]

requires:
  - phase: 46
    provides: [det_2 Gram = diag(+1,-1,-1,-1) on h_2(C_u), pi_u projection, spacetime/internal V_0 split]
  - phase: 47
    provides: [det_3 formula, d_{IJK} tensor, Peirce basis ordering]
provides:
  - SO(3,1) irrep decomposition of det_2 perturbation (10 = 9 spin-2 + 1 spin-0)
  - det_3 quadratic expansion around E_{11} gives M_{ab} = det_2 (massless)
  - Weinberg hypotheses 2 (spin-2) and 3 (massless) confirmed
  - Functions so31_irrep_decomposition_50() and det3_quadratic_expansion_50()
affects: [50-02 (universal coupling), 51 (synthesis)]

methods:
  added: [adjugate/sharp map X#, polarized sharp cross(X,Y), SO(3,1) traceless projector]
  patterns: [det_3 expansion around rank-1 idempotent, F_4-invariant quadratic decomposition]

key-files:
  created: [derivations/50-spin2-and-masslessness.tex]
  modified: [code/octonion_algebra.py]

key-decisions:
  - "M_{ab} = det_2 Gram identified as kinetic-type (case b), not Fierz-Pauli mass"
  - "Masslessness confirmed by two independent routes: direct det_3 expansion and F_4-invariant decomposition"

patterns-established:
  - "X# formula: X^2 - Tr(X)*X + (1/2)(Tr^2 - Tr(X^2))*I"
  - "Polarized sharp: cross(X,Y) = (1/2)((X+Y)# - X# - Y#)"
  - "For rank-1 E with E#=0: det_3(E+eps*delta) = eps^2*det_2(delta) on V_0"

conventions:
  - "metric = (+,-,-,-) from det_2 on h_2(C_u)"
  - "jordan_product = (1/2)(ab+ba)"
  - "det3_normalization: d(X,X,X) = 6*det_3(X)"
  - "spacetime V_0 local indices: {0,1,2,9}"
  - "internal V_0 local indices: {3,4,5,6,7,8}"

plan_contract_ref: ".gpd/phases/50-weinberg-verification-spin2-universal-coupling/50-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-spin2:
      status: passed
      summary: "Symmetric bilinear perturbation h_{ab} on h_2(C_u) = R^{3,1} decomposes as 10 = 9 (spin-2, traceless symmetric, (1,1) of SL(2,C)) + 1 (spin-0, trace). Traceless projector verified idempotent with rank 9."
      linked_ids: [deliv-derivation, deliv-code, test-irrep-decomposition, test-component-count, ref-weinberg-1964, ref-phase46]
    claim-massless:
      status: passed
      summary: "det_3(E_{11} + eps*delta) = eps^2*det_2(delta) for all V_0 perturbations. The O(eps^2) coefficient is the metric norm-squared (kinetic-type), NOT Fierz-Pauli mass. No mass term exists. Graviton is massless."
      linked_ids: [deliv-derivation, deliv-code, test-quadratic-expansion, test-no-fierz-pauli, ref-fierz-pauli, ref-boulware-deser, ref-phase47]
  deliverables:
    deliv-derivation:
      status: passed
      path: "derivations/50-spin2-and-masslessness.tex"
      summary: "LaTeX derivation with Propositions 1 (spin-2) and 2 (massless), full proofs, F_4 cross-check"
      linked_ids: [claim-spin2, claim-massless]
    deliv-code:
      status: passed
      path: "code/octonion_algebra.py"
      summary: "Functions so31_irrep_decomposition_50() and det3_quadratic_expansion_50() with _compute_sharp() and _polarized_sharp() helpers"
      linked_ids: [claim-spin2, claim-massless]
  acceptance_tests:
    test-irrep-decomposition:
      status: passed
      summary: "Traceless projector P_TL: idempotent (err 0), rank 9. Trace projector: idempotent (err 0), rank 1. Orthogonal and complete: P_TL + P_trace = I. 9 + 1 = 10."
      linked_ids: [claim-spin2, deliv-code, ref-phase46]
    test-component-count:
      status: passed
      summary: "Full V_0 (dim 10): det_2 Gram has signature (1,9). After pi_u: spacetime 4x4 = diag(+1,-1,-1,-1), internal 6x6 = 0. Cross terms = 0. 6 internal directions killed by pi_u."
      linked_ids: [deliv-code, ref-phase46]
    test-quadratic-expansion:
      status: passed
      summary: "M_{ab} computed by analytical (polarized sharp) and numerical (finite difference, eps=1e-4) methods agree to 1.65e-16. M_{ab} = det_2 Gram exactly (max err 0). NOT Fierz-Pauli form."
      linked_ids: [claim-massless, deliv-code, deliv-derivation, ref-phase47]
    test-no-fierz-pauli:
      status: passed
      summary: "M_{ab} = det_2 bilinear = -(1/2)*Tr(X^2) + (1/2)*(TrX)^2. This is the metric norm-squared (kinetic), not m^2(h_ab h^ab - h^2) (Fierz-Pauli). Boulware-Deser argument: any non-FP mass introduces ghost. Since M is kinetic, no mass term exists."
      linked_ids: [claim-massless, deliv-derivation, ref-fierz-pauli, ref-boulware-deser]
  references:
    ref-weinberg-1964:
      status: completed
      completed_actions: [cite, compare]
      missing_actions: []
      summary: "Weinberg hypotheses 2 (spin-2) and 3 (massless) verified against the algebraic structure. Cited in derivation."
    ref-fierz-pauli:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Fierz-Pauli mass form cited as the benchmark against which M_{ab} was compared. M_{ab} is NOT of FP form."
    ref-boulware-deser:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Boulware-Deser ghost argument cited: any non-FP spin-2 mass is inconsistent. Since M is kinetic (not mass), this reinforces masslessness."
    ref-phase46:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Phase 46 det_2 Gram = diag(+1,-1,-1,-1) and pi_u projection used as foundation for both propositions."
    ref-phase47:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Phase 47 det_3 formula and d_{IJK} tensor used for quadratic expansion computation."
  forbidden_proxies:
    fp-circular-R2:
      status: rejected
      notes: "Did not use -R/2 (Einstein-Hilbert) to conclude masslessness. Derived from det_3 expansion algebra."
    fp-symmetric-not-spin2:
      status: rejected
      notes: "Performed explicit SO(3,1) irrep decomposition with traceless projector. Did not assume symmetric = spin-2."
    fp-massless-by-assertion:
      status: rejected
      notes: "Computed det_3(E+eps*delta) quadratic expansion explicitly. Found M_{ab} = det_2 (kinetic), not mass."
    fp-proceed-on-failure:
      status: not_applicable
      notes: "No mass term found. HARD GATE passed cleanly."
  uncertainty_markers:
    weakest_anchors:
      - "E_{11} rank-1 with E#=0 verified numerically (not symbolically), but exact to machine precision"
      - "Boulware-Deser ghost argument is perturbative; non-perturbative massive gravity remains logically possible but irrelevant at tree level"
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations: []

comparison_verdicts:
  - subject_id: claim-massless
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-fierz-pauli
    comparison_kind: benchmark
    metric: exact_match
    threshold: "M_{ab} != Fierz-Pauli form"
    verdict: pass
    recommended_action: "Proceed to Plan 02 (universal coupling)"
    notes: "M_{ab} = det_2 Gram (kinetic type), confirmed by two independent methods"

duration: 12min
completed: 2026-04-12
---

# Phase 50 Plan 01: Spin-2 + Masslessness from det_3 on h_3(O)

**SO(3,1) irrep decomposition gives 10 = 9 (spin-2) + 1 (spin-0); det_3 quadratic expansion yields M_{ab} = det_2 (kinetic, not Fierz-Pauli) -- graviton is massless**

## Performance

- **Duration:** ~12 min
- **Started:** 2026-04-12T21:43:51Z
- **Completed:** 2026-04-12T21:56:00Z
- **Tasks:** 2
- **Files modified:** 2

## Key Results

- Symmetric perturbation h_{ab} on h_2(C_u) = R^{3,1} decomposes as 10 = 9 (spin-2, traceless) + 1 (spin-0, trace) [CONFIDENCE: HIGH]
- det_3(E_{11} + eps*delta) = eps^2 * det_2(delta) for V_0 perturbations: O(eps^2) coefficient equals det_2 Gram exactly [CONFIDENCE: HIGH]
- M_{ab} is kinetic-type (metric norm-squared), NOT Fierz-Pauli mass: graviton is massless [CONFIDENCE: HIGH]
- F_4-invariant decomposition: M = -(1/2)*Tr(X^2) + (1/2)*(TrX)^2 = det_2 (independent confirmation) [CONFIDENCE: HIGH]

## Task Commits

1. **Task 1: SO(3,1) irrep decomposition** - `c018b7a2` (derive)
2. **Task 2: Quadratic expansion and mass analysis** - `47040407` (derive)

## Files Created/Modified

- `derivations/50-spin2-and-masslessness.tex` - Propositions 1 (spin-2) and 2 (massless) with proofs
- `code/octonion_algebra.py` - so31_irrep_decomposition_50(), det3_quadratic_expansion_50(), _compute_sharp(), _polarized_sharp()

## Next Phase Readiness

- Weinberg hypotheses 2 (spin-2) and 3 (massless) confirmed
- Ready for Plan 02: universal coupling (Weinberg hypothesis 4)
- The identity Tr(delta# circ E) = det_2(delta) is the key algebraic mechanism

## Contract Coverage

- claim-spin2 -> passed (SO(3,1) decomposition: 10 = 9 + 1)
- claim-massless -> passed (M_{ab} = det_2, kinetic, not Fierz-Pauli)
- deliv-derivation -> passed (derivations/50-spin2-and-masslessness.tex)
- deliv-code -> passed (code/octonion_algebra.py)
- test-irrep-decomposition -> passed (P_TL rank 9, idempotent, verified)
- test-component-count -> passed (spacetime 4d, internal 6d killed by pi_u)
- test-quadratic-expansion -> passed (analytical = numerical to 1.65e-16)
- test-no-fierz-pauli -> passed (M = det_2, not m^2(h^2 - trace^2))
- ref-weinberg-1964 -> completed (cited, compared)
- ref-fierz-pauli -> completed (cited)
- ref-boulware-deser -> completed (cited)
- ref-phase46 -> completed (cited)
- ref-phase47 -> completed (cited)
- fp-circular-R2 -> rejected
- fp-symmetric-not-spin2 -> rejected
- fp-massless-by-assertion -> rejected
- fp-proceed-on-failure -> not_applicable (no mass found)
- Decisive comparison: claim-massless vs ref-fierz-pauli -> pass

## Equations Derived

**Eq. (50.1):** Normalized spacetime basis

$$e_\mu = \{2b_0,\; b_2,\; b_9,\; 2b_1\}, \quad \mu = 0,1,2,3$$

**Eq. (50.2):** SO(3,1) decomposition

$$10 = 9\;(\text{spin-2, traceless symmetric}) + 1\;(\text{spin-0, trace})$$

**Eq. (50.3):** Traceless projection

$$h_{ab}^{\text{TL}} = h_{ab} - \tfrac{1}{4}\,\eta_{ab}\,h$$

**Eq. (50.5):** det_3 expansion around rank-1 idempotent E_{11}

$$\det_3(E + \varepsilon\delta) = \varepsilon^2\,\text{Tr}(\delta^\# \circ E) + \varepsilon^3\,\det_3(\delta)$$

**Eq. (50.6):** Key identity

$$\text{Tr}(\delta^\# \circ E) = \det_2(\delta)$$

**Eq. (50.8):** F_4-invariant decomposition

$$M_{ab} = -\tfrac{1}{2}\,\text{Tr}(e_a \circ e_b) + \tfrac{1}{2}\,\text{Tr}(e_a)\,\text{Tr}(e_b) = \det_2(\cdot)$$

## Validations Completed

- Traceless projector: idempotent (err 0), rank 9, orthogonal to trace projector
- Minkowski metric: diag(+1,-1,-1,-1) on normalized spacetime basis (err 0)
- Internal V_0: 6 directions killed by pi_u (norm 0 after projection)
- E_{11}: det_3 = 0, E# = 0 (rank-1 verified to machine precision)
- M_{ab}: analytical (polarized sharp) = numerical (finite differences) to 1.65e-16
- M_{ab} = det_2 Gram: exact (max err 0)
- det_3(delta) = 0 for all 10 V_0 basis elements (structural zero)
- F_4 cross-check: M = -(1/2)*Tr(X^2) + (1/2)*(TrX)^2 (reconstruction err 0)

## Decisions & Deviations

None - plan executed exactly as written.

## Open Questions

- The identity Tr(delta# circ E) = det_2(delta) should generalize to other rank-1 idempotents by E_{6(-26)} covariance -- verify if needed for universality argument in Plan 02

---

_Phase: 50-weinberg-verification-spin2-universal-coupling_
_Completed: 2026-04-12_
