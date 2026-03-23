---
phase: 18-complexification-from-c-observer-part-a
plan: 02
depth: full
one-liner: "F_4 -> E_6 upgrade tracked through Peirce decomposition under complexification; 27 -> 1 + 10 + 16 under Spin(10) with each summand identified as a complexified Peirce subspace"
subsystem: [derivation, formalism]
tags: [exceptional-jordan-algebra, E6, F4, spin10, complexification, peirce-decomposition, representation-theory, 27-dimensional]

requires:
  - phase: 18-complexification-from-c-observer-part-a
    plan: 01
    provides: Peirce decomposition (27=1+16+10), V_{1/2}^C = S_{10}^+, Spin(9)->Spin(10), C*-complexification argument

provides:
  - h_3^C(O) = h_3(O) tensor_R C defined as complexified Jordan algebra (dim_C = 27)
  - F_4 -> E_6 upgrade as Aut -> Str_0 under complexification, tracked through Peirce decomposition
  - Spin(9) -> Spin(10) x U(1) stabilizer upgrade with orbit dimension check (78-46=32)
  - 27 -> 1 + 10 + 16 decomposition under Spin(10) with Peirce identification
  - V_1^C = 1 (singlet), V_0^C = 10 (vector), V_{1/2}^C = 16 (Weyl spinor S_{10}^+)
  - V_0^C representation check via branching 10|_{Spin(9)} = 9 + 1
  - Phase 18 synthesis (CMPL-01 + CMPL-02 complete)

affects: [Phase 19 (Cl(6) chirality from complex structure on Im(O)), Phase 20 (SM gauge group)]

methods:
  added: [extension of scalars at full algebra level, structure group identification, stabilizer orbit analysis, E_6 branching rules]
  patterns: [Peirce tracking through complexification: follow each eigenspace from real to complex and identify representation upgrade]

key-files:
  modified:
    - derivations/11-peirce-complexification.md

key-decisions:
  - "Step numbering continues from Plan 01 (Steps 12-17) to avoid collision with existing Steps 9-11"
  - "U(1) charges (-4, 2, -1) recorded but not analyzed -- deferred to Phase 19-20"
  - "Local-to-global complexification noted as consistent algebraic completion, not formally proven as necessary"

patterns-established:
  - "Full Peirce tracking pattern: derive real decomposition, complexify each eigenspace, verify representation upgrade via branching rules, cross-check dimensions at every stage"

conventions:
  - "jordan_product: a * b = (1/2)(ab + ba)"
  - "peirce_decomposition: under E_11"
  - "dimensionless algebraic quantities"
  - "S_{10}^+ for positive-chirality Weyl spinor (Boyle convention)"
  - "E_6 = compact form E_6^{-78} (structure group of h_3^C(O))"

plan_contract_ref: ".gpd/phases/18-complexification-from-c-observer-part-a/18-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-f4-e6:
      status: passed
      summary: "F_4 = Aut(h_3(O)) upgrades to E_6 = Str_0(h_3^C(O)) under complexification. F_4 embeds in E_6 as the subgroup preserving the real form. dim(F_4)=52, dim(E_6)=78, difference=26. Tracked through Peirce decomposition: each subspace followed from real to complex."
      linked_ids: [deliv-f4-e6-proof, test-f4-e6-dims, test-f4-subset-e6, ref-boyle2020, ref-baez-octonions, ref-yokota]
    claim-spin10-stabilizer:
      status: passed
      summary: "Stab_{F_4}(E_11) = Spin(9) (dim 36) upgrades to Stab_{E_6}(E_11) = Spin(10) x U(1) (dim 46) under complexification. Orbit dimension: 78-46=32 (complexified Cayley plane). Consistent with V_{1/2}^C = S_{10}^+ from Plan 01."
      linked_ids: [deliv-f4-e6-proof, test-spin10-stabilizer, ref-boyle2020, ref-yokota]
    claim-27-decomp:
      status: passed
      summary: "27 -> 1 + 10 + 16 under Spin(10), with 1 = V_1^C (singlet/idempotent), 10 = V_0^C (vector rep, h_2(O)^C), 16 = V_{1/2}^C (Weyl spinor S_{10}^+). Each summand identified with its Peirce subspace. Cross-checked with Boyle 2020."
      linked_ids: [deliv-f4-e6-proof, test-27-decomp, test-peirce-match, ref-boyle2020, ref-baez-octonions]
  deliverables:
    deliv-f4-e6-proof:
      status: passed
      path: "derivations/11-peirce-complexification.md"
      summary: "Part III (Steps 12-17) added: h_3^C(O) definition, F_4->E_6 upgrade, Spin(10)xU(1) stabilizer, 27->1+10+16 decomposition with Peirce identification, V_0^C representation check, Phase 18 synthesis."
      linked_ids: [claim-f4-e6, claim-spin10-stabilizer, claim-27-decomp]
  acceptance_tests:
    test-f4-e6-dims:
      status: passed
      summary: "dim(F_4)=52, dim(E_6)=78, 78-52=26. F_4 subset E_6 as real-form-preserving subgroup. Verified in Step 13."
      linked_ids: [deliv-f4-e6-proof, ref-baez-octonions]
    test-f4-subset-e6:
      status: passed
      summary: "F_4 = {g in E_6 : g(h_3(O)) = h_3(O)} -- subgroup preserving real form inside structure group of complexified algebra. Equivalently, fixed-point set of complex conjugation automorphism on E_6. Described in Step 13."
      linked_ids: [deliv-f4-e6-proof, ref-yokota]
    test-spin10-stabilizer:
      status: passed
      summary: "Spin(10) x U(1) = Stab_{E_6}(E_11), dim = 45+1 = 46. Orbit: E_6/(Spin(10)xU(1)), dim = 78-46 = 32 = dim_R((OP^2)^C). Spin(10) acts on V_{1/2}^C via Weyl spinor, consistent with Part II. Step 14."
      linked_ids: [deliv-f4-e6-proof, ref-boyle2020, ref-yokota]
    test-27-decomp:
      status: passed
      summary: "1 + 10 + 16 = 27. Each summand dimension matches its Spin(10) representation: trivial (1), vector (10), Weyl spinor (16). Step 15."
      linked_ids: [deliv-f4-e6-proof, ref-boyle2020]
    test-peirce-match:
      status: passed
      summary: "1 = V_1^C (C*E_11, singlet), 10 = V_0^C (h_2(O)^C, vector; verified via 10|_{Spin(9)} = 9+1 branching in Step 16), 16 = V_{1/2}^C (S_{10}^+, Weyl spinor; from Plan 01 Step 8). All three Peirce subspaces correctly identified."
      linked_ids: [deliv-f4-e6-proof, ref-boyle2020, ref-plan18-01]
  references:
    ref-boyle2020:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Boyle 2020 decomposition 27->1+10+16 used as benchmark throughout. Our results match at every level. Novel contribution: deriving complexification from C*-observer nature."
    ref-baez-octonions:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Baez Sec 4.3 cited for F_4 = Aut(h_3(O)), foundation for F_4->E_6 upgrade discussion."
    ref-yokota:
      status: completed
      completed_actions: [compare]
      missing_actions: []
      summary: "Yokota cross-referenced for Stab_{E_6}(E_11) = Spin(10) x U(1), F_4 embedding in E_6."
    ref-plan18-01:
      status: completed
      completed_actions: [use]
      missing_actions: []
      summary: "Plan 01 results used as foundation: Peirce decomposition, V_{1/2} = S_9, C*-complexification, Spin(9)->Spin(10)."
  forbidden_proxies:
    fp-f4-e6-assertion:
      status: rejected
      notes: "F_4 -> E_6 tracked through Peirce decomposition (Steps 13-14), not just stated as a group theory fact. Each Peirce subspace followed through complexification with representation upgrades verified."
    fp-27-without-peirce:
      status: rejected
      notes: "Every summand in 27 -> 1+10+16 identified with its Peirce subspace and representation (Step 15). The V_0^C = 10 identification independently verified via branching rule (Step 16)."
  uncertainty_markers:
    weakest_anchors:
      - "Str_0(h_3^C(O)) = E_6 identification invoked from literature (Baez, Yokota, Boyle), not re-derived."
      - "Stab_{E_6}(E_11) = Spin(10) x U(1) cited from literature. The U(1) factor and its physical significance (B-L) not analyzed in this phase."
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations:
      - "If 27 under Spin(10) did not decompose as 1+10+16 matching Peirce spaces, the framework would need revision. This did not occur -- decomposition matches exactly."

comparison_verdicts:
  - subject_id: claim-f4-e6
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-baez-octonions
    comparison_kind: benchmark
    metric: group_dimensions_and_embedding
    threshold: "dim(F_4)=52, dim(E_6)=78, F_4 subset E_6"
    verdict: pass
    recommended_action: "F_4->E_6 upgrade established. Phase 18 CMPL-02 complete."
    notes: "All dimensions match. Embedding characterized as real-form-preserving subgroup."
  - subject_id: claim-27-decomp
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-boyle2020
    comparison_kind: prior_work
    metric: representation_decomposition
    threshold: "27 = 1 + 10 + 16 with Peirce identification"
    verdict: pass
    recommended_action: "Proceed to Phase 19 for Cl(6) chirality construction."
    notes: "Decomposition matches Boyle 2020 exactly. Novel element: derivation route via C*-observer complexification."
  - subject_id: claim-spin10-stabilizer
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-yokota
    comparison_kind: benchmark
    metric: stabilizer_identification
    threshold: "Stab_{E_6}(E_11) = Spin(10) x U(1), dim = 46"
    verdict: pass
    recommended_action: "Stabilizer upgrade confirmed. U(1) analysis deferred to Phase 19-20."
    notes: "Orbit dimension 32 = 2 * dim(OP^2) consistent with complexified Cayley plane."

duration: 4min
completed: 2026-03-23
---

# Plan 02: F_4 -> E_6 Upgrade and 27-dim Decomposition -- Summary

**F_4 -> E_6 upgrade tracked through Peirce decomposition under complexification; 27 -> 1 + 10 + 16 under Spin(10) with each summand identified as a complexified Peirce subspace**

## Performance

- **Duration:** ~4 min
- **Started:** 2026-03-23T23:54:28Z
- **Completed:** 2026-03-23T23:58:09Z
- **Tasks:** 2
- **Files modified:** 1

## Key Results

- **F_4 -> E_6 upgrade:** Aut(h_3(O)) -> Str_0(h_3^C(O)), dim 52 -> 78, with F_4 embedded as real-form-preserving subgroup. [CONFIDENCE: HIGH]
- **Stabilizer upgrade:** Spin(9) -> Spin(10) x U(1), dim 36 -> 46. Orbit 78-46 = 32 = complexified Cayley plane. [CONFIDENCE: HIGH]
- **27 -> 1 + 10 + 16:** Each summand matched to Peirce subspace: 1 = V_1^C (singlet), 10 = V_0^C (vector), 16 = V_{1/2}^C = S_{10}^+ (Weyl spinor). Cross-checked with Boyle 2020. [CONFIDENCE: HIGH]
- **V_0^C representation:** Independently verified as Spin(10) vector via branching 10|_{Spin(9)} = 9 + 1. [CONFIDENCE: HIGH]
- **Phase 18 synthesis:** CMPL-01 (complexification from C*-observer) + CMPL-02 (F_4->E_6 with Peirce tracking) both complete. Ready for Phase 19. [CONFIDENCE: HIGH]

## Task Commits

1. **Task 1: Complexification h_3(O)->h_3^C(O) and F_4->E_6 upgrade** -- `3c3dfe6` (derive)
2. **Task 2: 27-dim decomposition and Phase 18 synthesis** -- `6ba778b` (derive)

## Files Created/Modified

- `derivations/11-peirce-complexification.md` -- Part III added (Steps 12-17): full algebra complexification, F_4->E_6, stabilizer upgrade, 27->1+10+16, V_0^C check, synthesis

## Next Phase Readiness

Phase 19 inputs ready:
- V_{1/2}^C = S_{10}^+ established (Weyl spinor, dim_C = 16)
- Spin(10) x U(1) stabilizer established
- 27 = 1 + 10 + 16 decomposition matched to Peirce
- Next: choosing complex structure on Im(O) (u in S^6) gives O = C + C^3, inducing Cl(6) -> Cl(10), whose volume form selects chirality

## Contract Coverage

- claim-f4-e6 -> **passed**: Aut -> Str_0, dim 52 -> 78, Peirce tracked
- claim-spin10-stabilizer -> **passed**: Spin(9) -> Spin(10) x U(1), dim 36 -> 46, orbit 32
- claim-27-decomp -> **passed**: 27 = 1+10+16, each summand = Peirce subspace
- deliv-f4-e6-proof -> **passed**: derivations/11-peirce-complexification.md Part III
- test-f4-e6-dims -> **passed**: 52, 78, 26
- test-f4-subset-e6 -> **passed**: real-form-preserving characterization
- test-spin10-stabilizer -> **passed**: dim 46, orbit 32
- test-27-decomp -> **passed**: 1+10+16=27
- test-peirce-match -> **passed**: all three subspaces identified
- ref-boyle2020 -> **completed** [read, compare, cite]
- ref-baez-octonions -> **completed** [read, cite]
- ref-yokota -> **completed** [compare]
- ref-plan18-01 -> **completed** [use]
- fp-f4-e6-assertion -> **rejected**: tracked through Peirce, not just stated
- fp-27-without-peirce -> **rejected**: every summand connected to Peirce subspace

## Equations Derived

No dynamical equations. Key structural results:

**Eq. (18-02.1):** Full algebra complexification:
$$h_3^\mathbb{C}(\mathbb{O}) = h_3(\mathbb{O}) \otimes_\mathbb{R} \mathbb{C}, \quad \dim_\mathbb{C} = 27$$

**Eq. (18-02.2):** Structure group upgrade:
$$F_4 = \mathrm{Aut}(h_3(\mathbb{O})) \xrightarrow{\text{complexification}} E_6 = \mathrm{Str}_0(h_3^\mathbb{C}(\mathbb{O}))$$

**Eq. (18-02.3):** Stabilizer upgrade:
$$\mathrm{Spin}(9) \to \mathrm{Spin}(10) \times \mathrm{U}(1), \quad \dim: 36 \to 46$$

**Eq. (18-02.4):** 27-dim decomposition:
$$\mathbf{27} \to \mathbf{1} \oplus \mathbf{10} \oplus \mathbf{16} \quad \text{under } \mathrm{Spin}(10)$$

## Validations Completed

- dim(F_4)=52, dim(E_6)=78, diff=26 [CONFIDENCE: HIGH]
- dim(Spin(9))=36, dim(Spin(10))=45, Spin(10)xU(1) dim=46 [CONFIDENCE: HIGH]
- Orbit: 78-46=32 = 2*dim(OP^2) (complexified Cayley plane) [CONFIDENCE: HIGH]
- 1+10+16=27 dimension sum [CONFIDENCE: HIGH]
- V_0^C = 10 via branching 10|_{Spin(9)} = 9+1 [CONFIDENCE: HIGH]
- Cross-check Boyle 2020: decomposition matches [CONFIDENCE: HIGH]
- Forbidden proxy audit: F_4->E_6 tracked (not just stated), 27 decomposition connected to Peirce (not just cited) [CONFIDENCE: HIGH]

## Decisions & Deviations

### Decisions

1. **Step numbering:** Continued from Plan 01 as Steps 12-17 (Plan 01 used Steps 1-11) to maintain sequential numbering in the derivation document.

2. **U(1) charges recorded but not analyzed:** The charges (-4, 2, -1) in the E_6 branching rule are standard but their physical significance (B-L) is deferred to Phase 19-20.

3. **Local-to-global complexification:** Noted as consistent algebraic completion, not formally proven as necessary consequence of local V_{1/2} complexification. This is an honest gap.

### Deviations

None -- plan executed exactly as written.

## Open Questions

- Can the local complexification of V_{1/2} (Part II) be shown to necessitate complexification of the full algebra h_3(O) -> h_3^C(O) (Part III)?
- Physical interpretation of U(1) factor in Spin(10) x U(1) as B-L (Boyle) -- to be analyzed in Phase 19-20
- Can Gap B step 1 (rank-1 idempotent choice) be derived from self-modeling?

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
|----------|--------|-------|------------|--------|-------------|
| dim(h_3^C(O)) | -- | 27 | exact | definition | -- |
| dim(F_4) | -- | 52 | exact | standard | -- |
| dim(E_6) | -- | 78 | exact | standard | -- |
| dim(Spin(10)) | -- | 45 | exact | standard | -- |
| dim(Spin(10)xU(1)) | -- | 46 | exact | standard | -- |
| Orbit dim E_6/Stab | -- | 32 | exact | 78-46 | -- |
| dim(V_0^C) | -- | 10 | exact | Peirce computation | -- |

## Approximations Used

None -- all results are exact (algebraic/representation-theoretic).

---

_Phase: 18-complexification-from-c-observer-part-a, Plan: 02_
_Completed: 2026-03-23_
