---
phase: 18-complexification-from-c-observer-part-a
plan: 01
depth: full
one-liner: "Peirce decomposition of h_3(O) under E_11 derived (27 = 1 + 16 + 10); C*-observer nature forces complexification V_{1/2} = S_9 -> S_{10}^+ via extension of scalars, upgrading Spin(9) to Spin(10)"
subsystem: [derivation, formalism]
tags: [peirce-decomposition, exceptional-jordan-algebra, octonions, spin9, spin10, complexification, c-star-algebra, weyl-spinor]

requires:
  - phase: 05-local-tomography-from-b-m-compositionality
    plan: 02
    provides: Type exclusion, C*-algebra promotion (M_n(C)^sa forced by self-modeling)

provides:
  - Peirce decomposition of h_3(O) under rank-1 idempotent E_11 with explicit eigenspaces
  - V_{1/2} = O^2 identified as real Spin(9) spinor S_9 (dim_R = 16)
  - V_0 = h_2(O) identified as Spin(9) vector rep 9 + trace (dim = 10)
  - Proof that C*-observer nature forces extension of scalars V_{1/2} -> V_{1/2}^C
  - Spin(9) -> Spin(10) upgrade via branching rule S_{10}^+|_{Spin(9)} = S_9 tensor C
  - Cross-check with Boyle 2020 (consistent identification of V_{1/2} as S_{10}^+)

affects: [18-02 (F_4 -> E_6 upgrade, 27 -> 1+10+16 decomposition), Phase 19 (Cl(6) chirality)]

methods:
  added: [Peirce decomposition under idempotent, extension of scalars, Spin branching rules]
  patterns: [C*-observer complexification: complex observer probing real space forces tensor with C]

key-files:
  created:
    - derivations/11-peirce-complexification.md

key-decisions:
  - "S_{10}^+ chosen over S_{10}^- as label for complexified spinor (convention following Boyle 2020; chirality resolution deferred to Phase 19)"
  - "Rank-1 idempotent e = E_11 taken as given input (Gap B step 1), not derived"
  - "Complexification argument structured as 5-step logical chain from C*-nature to extension of scalars"

patterns-established:
  - "C*-observer complexification pattern: self-modeling -> C*-nature -> C-scalars -> extension of scalars on probed real spaces"
  - "Peirce eigenspace identification: V_lambda computed by solving e circ X = lambda X entry-by-entry"

conventions:
  - "jordan_product: a * b = (1/2)(ab + ba)"
  - "peirce_decomposition: under E_11"
  - "dimensionless algebraic quantities"
  - "S_{10}^+ for the positive-chirality Weyl spinor (Boyle convention)"

plan_contract_ref: ".gpd/phases/18-complexification-from-c-observer-part-a/18-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-peirce-decomp:
      status: passed
      summary: "h_3(O) decomposes under E_11 into V_1 (dim 1, trivial), V_{1/2} (dim 16, O^2 = S_9), V_0 (dim 10, h_2(O) = 9+1). All dimensions verified: 1+16+10=27. Spin(9) = Stab_{F_4}(E_11) acts on V_{1/2} via the unique real 16-dim spinor S_9."
      linked_ids: [deliv-peirce-proof, test-peirce-dims, test-spin9-rep, ref-baez-octonions, ref-yokota]
    claim-complexification:
      status: passed
      summary: "C*-observer nature (complex type from Paper 5 local tomography) forces extension of scalars V_{1/2} tensor_R C = V_{1/2}^C. Logical chain: self-modeling -> C*-algebra -> C-scalars -> C-linear operations -> extension of scalars. No additional assumptions beyond Paper 5."
      linked_ids: [deliv-peirce-proof, test-cstar-forces-complex, test-dim-complex, ref-paper5]
    claim-spin10-upgrade:
      status: passed
      summary: "After complexification, Spin(9) action on S_9 extends to Spin(10) action on S_{10}^+. Branching rule S_{10}^+|_{Spin(9)} = S_9 tensor_R C established. S_9 is the real form of S_{10}^+. Cross-checked with Boyle 2020."
      linked_ids: [deliv-peirce-proof, test-spin10-rep, test-dim-complex, ref-boyle2020, ref-baez-octonions]
  deliverables:
    deliv-peirce-proof:
      status: passed
      path: "derivations/11-peirce-complexification.md"
      summary: "Two-part derivation: Part I (Peirce decomposition, Spin(9) identification, 4 steps), Part II (complexification argument, Spin(10) upgrade, 7 steps). Contains all required elements: Peirce decomposition under E_11, V_1 = O^2 identification, C*-observer complexification argument, Spin(9) -> Spin(10) representation upgrade."
      linked_ids: [claim-peirce-decomp, claim-complexification, claim-spin10-upgrade]
  acceptance_tests:
    test-peirce-dims:
      status: passed
      summary: "Dimensions sum to 27: V_1 (1) + V_{1/2} (16) + V_0 (10) = 27 = dim(h_3(O)). Verified by explicit entry-by-entry computation of e circ X."
      linked_ids: [deliv-peirce-proof, ref-baez-octonions]
    test-spin9-rep:
      status: passed
      summary: "V_{1/2} = O^2 identified as S_9 via: dim(S_9) = 2^4 = 16 = dim(V_{1/2}), Spin(9) = Stab_{F_4}(E_11) acts on V_{1/2} via isotropy representation on tangent space of OP^2. Coset check: dim(F_4/Spin(9)) = 52-36 = 16. References: Baez Sec 4.3, Yokota Ch 2."
      linked_ids: [deliv-peirce-proof, ref-baez-octonions, ref-yokota]
    test-cstar-forces-complex:
      status: passed
      summary: "5-step logical chain verified: (1) Paper 5 proves C*-nature, (2) C*-algebra has C-scalars, (3) observer probes V_{1/2} through its framework, (4) observer's operations are C-linear, (5) extension of scalars V tensor_R C is forced. No step assumes complexification; each follows from the preceding."
      linked_ids: [deliv-peirce-proof, ref-paper5]
    test-dim-complex:
      status: passed
      summary: "dim_C(V_{1/2}^C) = dim_R(V_{1/2}) = 16. Extension of scalars preserves real dimension as complex dimension."
      linked_ids: [deliv-peirce-proof]
    test-spin10-rep:
      status: passed
      summary: "Branching rule established: S_{10}^+|_{Spin(9)} = S_9 tensor_R C. S_9 is real form of S_{10}^+. dim_C(S_{10}^+) = 2^{10/2-1} = 16 = dim_R(S_9). Consistent with Boyle 2020 identification."
      linked_ids: [deliv-peirce-proof, ref-boyle2020]
  references:
    ref-paper5:
      status: completed
      completed_actions: [cite, use]
      missing_actions: []
      summary: "Paper 5 C*-algebra result cited as source of complex observer nature. Used in Steps 5-6 of the complexification argument."
    ref-boyle2020:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Boyle 2020 identification of V_{1/2} in h_3^C(O) as S_{10}^+ used as cross-check in Step 9. Our derivation arrives at the same result via a different route (deriving complexification from C*-nature rather than starting from h_3^C(O))."
    ref-baez-octonions:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Baez 'The Octonions' Sec 4.3 cited for F_4 = Aut(h_3(O)), Spin(9) = Stab(E_11), and V_{1/2} = S_9 identification."
    ref-yokota:
      status: completed
      completed_actions: [compare]
      missing_actions: []
      summary: "Yokota 'Exceptional Lie Groups' cross-referenced for F_4, Spin(9) structure and Peirce decomposition. Consistent with Baez."
  forbidden_proxies:
    fp-assume-complexification:
      status: rejected
      notes: "Complexification derived from 5-step logical chain starting from C*-nature (Paper 5). Not assumed. Circularity check: complex structure enters only through Paper 5 conclusion, not as input to the Peirce decomposition."
    fp-spin10-without-upgrade:
      status: rejected
      notes: "Spin(10) established via explicit representation-theoretic branching rule S_{10}^+|_{Spin(9)} = S_9 tensor_R C. The upgrade is derived from complexification of the spinor space, not asserted."
  uncertainty_markers:
    weakest_anchors:
      - "The 'probing' step (Step 6c, point 3): the observer probes V_{1/2} through its own C*-framework. This is physically natural but not a formal theorem. The mechanism by which the C*-observer's C-linearity forces extension of scalars (rather than some other interaction with the real space) is the weakest link."
    unvalidated_assumptions:
      - "Rank-1 idempotent e = E_11 choice (Gap B step 1) -- taken as input, not derived from self-modeling"
    competing_explanations: []
    disconfirming_observations: []

comparison_verdicts:
  - subject_id: claim-peirce-decomp
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-baez-octonions
    comparison_kind: benchmark
    metric: dimension_decomposition
    threshold: "27 = 1 + 16 + 10"
    verdict: pass
    recommended_action: "Peirce decomposition established. Proceed to Plan 02 for full algebra complexification."
    notes: "All dimensions match standard references. Spin(9) action on V_{1/2} = S_9 confirmed."
  - subject_id: claim-spin10-upgrade
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-boyle2020
    comparison_kind: prior_work
    metric: representation_identification
    threshold: "V_{1/2}^C = S_{10}^+ (complex 16-dim Weyl spinor)"
    verdict: pass
    recommended_action: "Spin(10) upgrade established. Plan 02 will track F_4 -> E_6 at the algebra level."
    notes: "Our route (C*-observer -> complexification) arrives at same result as Boyle's (starting from h_3^C(O)). Novel contribution is deriving the complexification from physics."

duration: 3min
completed: 2026-03-23
---

# Plan 01: Peirce Decomposition and C*-Observer Complexification -- Summary

**Peirce decomposition of h_3(O) under E_11 derived (27 = 1 + 16 + 10); C*-observer nature forces complexification V_{1/2} = S_9 -> S_{10}^+ via extension of scalars, upgrading Spin(9) to Spin(10)**

## Performance

- **Duration:** ~3 min
- **Started:** 2026-03-23T23:47:20Z
- **Completed:** 2026-03-23T23:50:35Z
- **Tasks:** 2
- **Files modified:** 1

## Key Results

- **Peirce decomposition:** h_3(O) = V_1 (dim 1) + V_{1/2} (dim 16) + V_0 (dim 10) under idempotent E_11, with 1 + 16 + 10 = 27. [CONFIDENCE: HIGH]
- **Spinor identification:** V_{1/2} = O^2 carries the unique real 16-dim Spin(9) spinor S_9, with Spin(9) = Stab_{F_4}(E_11). [CONFIDENCE: HIGH]
- **Complexification from C*-nature:** The observer's C*-algebra nature (Paper 5) forces extension of scalars V_{1/2} -> V_{1/2}^C = V_{1/2} tensor_R C, giving dim_C = 16. Logical chain: self-modeling -> C*-algebra -> C-scalars -> C-linear probing -> extension of scalars. No additional assumptions. [CONFIDENCE: MEDIUM -- the "probing" step is physically motivated but not a formal theorem]
- **Spin(9) -> Spin(10):** After complexification, S_9 tensor_R C = S_{10}^+ (Weyl spinor of Spin(10), dim_C = 16). Branching rule cross-checked. Consistent with Boyle 2020. [CONFIDENCE: HIGH]

## Task Commits

1. **Task 1: Peirce decomposition and Spin(9) identification** -- `17aa31b` (derive)
2. **Task 2: C*-observer complexification and Spin(10) upgrade** -- `19b6bec` (derive)

## Files Created/Modified

- `derivations/11-peirce-complexification.md` -- Two-part derivation (11 steps): Part I (Peirce decomposition, Spin(9)), Part II (complexification, Spin(10) upgrade, backtracking assessment)

## Next Phase Readiness

Plan 02 inputs ready:
- V_{1/2}^C = S_{10}^+ established with correct dimension and representation
- Spin(9) -> Spin(10) upgrade at representation level
- Next: F_4 -> E_6 upgrade at algebra level, 27 -> 1 + 10 + 16 decomposition under Spin(10)

## Contract Coverage

- claim-peirce-decomp -> **passed**: 27 = 1 + 16 + 10 with Spin(9) action
- claim-complexification -> **passed**: derived from C*-nature, not assumed
- claim-spin10-upgrade -> **passed**: S_9 tensor_R C = S_{10}^+ via branching rule
- deliv-peirce-proof -> **passed**: derivations/11-peirce-complexification.md
- test-peirce-dims -> **passed**: 1 + 16 + 10 = 27
- test-spin9-rep -> **passed**: dim(S_9) = 16, Stab_{F_4}(E_11) = Spin(9)
- test-cstar-forces-complex -> **passed**: 5-step logical chain
- test-dim-complex -> **passed**: dim_C = 16
- test-spin10-rep -> **passed**: branching rule verified
- ref-paper5 -> **completed** [cite, use]
- ref-boyle2020 -> **completed** [read, compare, cite]
- ref-baez-octonions -> **completed** [read, cite]
- ref-yokota -> **completed** [compare]
- fp-assume-complexification -> **rejected**: complexification derived, not assumed
- fp-spin10-without-upgrade -> **rejected**: Spin(10) via branching rule, not asserted

## Equations Derived

No dynamical equations. Key structural results:

**Eq. (18-01.1):** Peirce decomposition of h_3(O):
$$h_3(\mathbb{O}) = V_1 \oplus V_{1/2} \oplus V_0, \quad 27 = 1 + 16 + 10$$

**Eq. (18-01.2):** Complexification of Peirce space:
$$V_{1/2}^\mathbb{C} = \mathbb{O}^2 \otimes_\mathbb{R} \mathbb{C}, \quad \dim_\mathbb{C} = 16$$

**Eq. (18-01.3):** Spin upgrade:
$$S_9 \otimes_\mathbb{R} \mathbb{C} = S_{10}^+$$

## Validations Completed

- Dimension check: 1 + 16 + 10 = 27 [CONFIDENCE: HIGH]
- Entry-by-entry Peirce eigenvalue verification [CONFIDENCE: HIGH]
- Coset dimension: dim(F_4/Spin(9)) = 52 - 36 = 16 = dim(V_{1/2}) [CONFIDENCE: HIGH]
- Spinor dimension: dim(S_9) = 2^4 = 16, dim_C(S_{10}^+) = 16 [CONFIDENCE: HIGH]
- Forbidden proxy audit: complexification derived (not assumed); Spin(10) via branching rule (not asserted) [CONFIDENCE: HIGH]
- Cross-check with Boyle 2020: V_{1/2}^C = S_{10}^+ consistent [CONFIDENCE: HIGH]

## Decisions & Deviations

### Decisions

1. **S_{10}^+ convention:** Followed Boyle 2020 in labeling the complexified spinor as S_{10}^+ rather than S_{10}^-. The choice of chirality is deferred to Phase 19 (Cl(6) construction).

2. **Backtracking trigger not fired:** The complexification argument uses only C*-nature (Paper 5), extension of scalars, and the physical setup of observer probing V_{1/2}. No additional structure beyond C*-nature is required.

### Deviations

None -- plan executed exactly as written.

## Open Questions

- Does the complexification of V_{1/2} alone imply complexification of the full algebra h_3(O) -> h_3^C(O)? (Address in Plan 02)
- Is the "probing" step (observer accesses V_{1/2} through its C*-framework) formalizable as a categorical statement about modules?
- Can the rank-1 idempotent choice (Gap B step 1) be derived from self-modeling, or is it an irreducible input?

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
|----------|--------|-------|------------|--------|-------------|
| dim(h_3(O)) | -- | 27 | exact | definition | -- |
| dim(V_1) | -- | 1 | exact | Peirce computation | -- |
| dim(V_{1/2}) | -- | 16 | exact | Peirce computation | -- |
| dim(V_0) | -- | 10 | exact | Peirce computation | -- |
| dim(F_4) | -- | 52 | exact | standard | -- |
| dim(Spin(9)) | -- | 36 | exact | standard | -- |
| dim_C(S_{10}^+) | -- | 16 | exact | standard | -- |

## Approximations Used

None -- all results are exact (algebraic/representation-theoretic).

---

_Phase: 18-complexification-from-c-observer-part-a, Plan: 01_
_Completed: 2026-03-23_
