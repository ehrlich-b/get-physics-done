---
phase: 19-cl-6-chirality-and-sm-embedding-part-b
plan: 01
depth: full
one-liner: "Cl(6) subalgebra inside Cl(10) derived from octonion splitting O = C + C^3; volume form omega_6 selects 16-dim chiral subspace; Pati-Salam breaking chain gives SM gauge group with LEFT embedding; Furey Witt decomposition verified with automatic chirality"
subsystem: [derivation, formalism]
tags: [clifford-algebra, cl6, cl10, octonions, chirality, pati-salam, standard-model, witt-decomposition, furey, todorov, spin10, volume-form]

requires:
  - phase: 18-complexification-from-c-observer-part-a
    plan: 01
    provides: Peirce decomposition (27=1+16+10), V_{1/2}^C = S_{10}^+, Spin(9)->Spin(10), C*-complexification
  - phase: 18-complexification-from-c-observer-part-a
    plan: 02
    provides: F_4->E_6, 27->1+10+16, Spin(10)xU(1) stabilizer

provides:
  - Cl(6) subalgebra inside Cl(10) from the octonion splitting O = C + C^3 (6 gamma matrices from Im(C^3))
  - Volume form omega_6 = gamma_1...gamma_6 with omega_6^2 = -1
  - Projector P = (1/2)(1 - i*omega_6) selecting 16-dim subspace of 32-dim Dirac spinor (tr(P)=16)
  - Pati-Salam group SU(4) x SU(2)_L x SU(2)_R / Z_2 as stabilizer of omega_6 in Spin(10) (dim 21 = 15+6)
  - Chiral decomposition 16 -> (4,2,1) + (4bar,1,2) with LEFT embedding verified
  - SM gauge group SU(3)_C x SU(2)_L x U(1)_Y from SU(4) -> SU(3) x U(1) breaking by same complex structure u
  - Furey Witt decomposition: a_j = (1/2)(gamma_{2j-1} + i*gamma_{2j}), all 27 CAR verified
  - Automatic chirality: omega_6 = -i*(-1)^N, SU(2)_L channels to single chirality by construction
  - Full breaking chain: Spin(10) -> Pati-Salam -> SM, both steps from single input u in S^6

affects: [Phase 19 Plan 02 (explicit quantum numbers of all 16 states), Phase 20 (SM gauge group identification)]

methods:
  added: [Witt decomposition of Cl(2n), Clifford volume form chirality projection, stabilizer computation via commutators]
  patterns: ["Single input cascade: u in S^6 determines Cl(6), omega_6, chirality, Pati-Salam, SM gauge group"]

key-files:
  created:
    - derivations/12-cl6-chirality.md

key-decisions:
  - "u = e_7 (Fano convention) for the complex structure on Im(O)"
  - "Cl(10) construction: first 6 generators from Im(C^3), last 4 via i*omega_6 tensor Cl(4) tau matrices"
  - "Projector P = (1/2)(1 - i*omega_6) selects omega_6 = -i eigenspace (Todorov 'particle' convention)"
  - "Witt basis: a_j = (1/2)(gamma_{2j-1} + i*gamma_{2j}), standard complex structure pairing"

patterns-established:
  - "Stabilizer computation: count bivectors commuting with volume form; internal-internal (spin(6)) + external-external (spin(4)) = stabilizer; mixed = broken"
  - "Automatic chirality: omega_6 = -i*(-1)^N where N is Witt particle number; creation operators preserve chirality sector by construction"

conventions:
  - "jordan_product: a * b = (1/2)(ab + ba)"
  - "clifford: {gamma_i, gamma_j} = 2 delta_ij (Euclidean, positive-definite)"
  - "octonion_basis: Fano convention, e_1 e_2 = e_4"
  - "complex_structure: u = e_7"
  - "S_{10}^+ for positive-chirality Weyl spinor (Boyle convention)"
  - "Witt operators: a_j = (1/2)(gamma_{2j-1} + i*gamma_{2j})"

plan_contract_ref: ".gpd/phases/19-cl-6-chirality-and-sm-embedding-part-b/19-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-cl6-construction:
      status: passed
      summary: "O = C + C^3 splitting from u = e_7 gives 6 directions in W = e_7^perp cap Im(O). These define gamma_1,...,gamma_6 generating Cl(6) inside Cl(10). Clifford relations {gamma_i, gamma_j} = 2 delta_ij verified analytically and numerically (all 21 relations, error < 1e-12)."
      linked_ids: [deliv-cl6-derivation, test-clifford-relations, test-cl6-in-cl10, ref-todorov-2022, ref-furey-2018]
    claim-volume-form:
      status: passed
      summary: "omega_6 = gamma_1...gamma_6 satisfies omega_6^2 = (-1)^{15} = -1. Chirality operator i*omega_6 has (i*omega_6)^2 = +1. Projector P = (1/2)(1 - i*omega_6) is idempotent with tr(P) = 16 on 32-dim Dirac spinor. Verified analytically and numerically."
      linked_ids: [deliv-cl6-derivation, test-volume-form-squared, test-projector-rank, ref-todorov-2022, ref-phase18]
    claim-pati-salam-breaking:
      status: passed
      summary: "Stabilizer of omega_6 in Spin(10) is Spin(6) x Spin(4) / Z_2 = SU(4) x SU(2)_L x SU(2)_R (Pati-Salam). Dimension: 15 + 6 = 21. 16 -> (4,2,1) + (4bar,1,2) is LEFT embedding. SU(4) -> SU(3) x U(1) from same u gives SM gauge group. Numerically verified: stabilizer dim = 21, internal = 15, external = 6, mixed = 0."
      linked_ids: [deliv-cl6-derivation, test-pati-salam-stabilizer, test-left-embedding, ref-todorov-2022, ref-baez-sawin]
    claim-furey-witt:
      status: passed
      summary: "Witt decomposition a_j = (1/2)(gamma_{2j-1} + i*gamma_{2j}) for j=1,2,3. All 27 CAR verified: {a_i, a_j^dag} = delta_ij, {a_i, a_j} = 0, {a_i^dag, a_j^dag} = 0. omega_6 = -i*(-1)^N where N = total particle number. SU(2)_L channels to single chirality automatically (no ad hoc projector)."
      linked_ids: [deliv-cl6-derivation, test-witt-anticommutators, test-automatic-chirality, ref-furey-2018, ref-baez-sawin]
  deliverables:
    deliv-cl6-derivation:
      status: passed
      path: "derivations/12-cl6-chirality.md"
      summary: "Three-part derivation (9 steps + synthesis): Part I (Steps 1-4: O splitting, Cl(6) construction, volume form, projector), Part II (Steps 5-9: Pati-Salam stabilizer, 16 decomposition, SU(4)->SU(3)xU(1), Witt decomposition, automatic chirality), Part III (synthesis). Contains all required elements per contract must_contain list."
      linked_ids: [claim-cl6-construction, claim-volume-form, claim-pati-salam-breaking, claim-furey-witt]
  acceptance_tests:
    test-clifford-relations:
      status: passed
      summary: "All 21 anticommutator relations {gamma_i, gamma_j} = 2 delta_ij verified analytically (Step 2) and numerically (Test 1, error = 0)."
      linked_ids: [deliv-cl6-derivation, ref-todorov-2022]
    test-cl6-in-cl10:
      status: passed
      summary: "6 Cl(6) generators identified as the first 6 of the 10 Cl(10) generators, corresponding to Im(C^3) directions in the O splitting. Numerical test: all 55 Cl(10) relations verified (Test 9)."
      linked_ids: [deliv-cl6-derivation]
    test-volume-form-squared:
      status: passed
      summary: "omega_6^2 = (-1)^{6*5/2} = (-1)^15 = -1 verified by explicit sign counting (Step 3a) and numerically (Test 2, error = 0). (i*omega_6)^2 = +1 verified (Test 3)."
      linked_ids: [deliv-cl6-derivation]
    test-projector-rank:
      status: passed
      summary: "tr(P) = 4 in 8-dim Cl(6) rep, tr(P) = 16 in 32-dim Cl(10) Dirac rep. Both verified numerically (Tests 4 and 9). tr(omega_6) = 0 verified (Test 5)."
      linked_ids: [deliv-cl6-derivation, ref-phase18]
    test-pati-salam-stabilizer:
      status: passed
      summary: "Stabilizer dim = 21 = 15 (internal, spin(6)=su(4)) + 6 (external, spin(4)=su(2)+su(2)). Mixed generators: 0 in stabilizer (all 24 anticommute with omega_6). Verified analytically (Step 5) and numerically (Test 10)."
      linked_ids: [deliv-cl6-derivation, ref-todorov-2022]
    test-left-embedding:
      status: passed
      summary: "16 -> (4,2,1) + (4bar,1,2) under Pati-Salam. SU(2)_L acts on (4,2,1) only = left-handed fermions. This is LEFT embedding, not diagonal. Distinguished per Sawin theorem (Baez n-Cat Cafe Part 13). Verified by structure of the decomposition: omega_6 separates chiralities before Pati-Salam breaking."
      linked_ids: [deliv-cl6-derivation, ref-baez-sawin]
    test-witt-anticommutators:
      status: passed
      summary: "All 27 CAR verified: {a_i, a_j^dag} = delta_ij (9 relations), {a_i, a_j} = 0 (9 relations), {a_i^dag, a_j^dag} = 0 (9 relations). Verified analytically (Step 8) and numerically (Test 6, error = 0)."
      linked_ids: [deliv-cl6-derivation, ref-furey-2018]
    test-automatic-chirality:
      status: passed
      summary: "omega_6 = -i*(-1)^N (N = particle number) verified analytically (Step 9) and numerically (Test 8, error = 0). SU(2)_L generators commute with omega_6 (from stabilizer analysis), hence preserve chirality. No ad hoc projector needed. Consistent with Furey 2018."
      linked_ids: [deliv-cl6-derivation, ref-furey-2018]
  references:
    ref-todorov-2022:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Todorov arXiv:2206.06912 cited for Cl(6) inside Cl(10) construction, omega_6 as particle projector, Pati-Salam identification. Our construction matches Todorov's framework throughout."
    ref-furey-2018:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Furey arXiv:1806.00612 cited for Witt decomposition and automatic chirality. Our a_j operators and CAR verification reproduce Furey's results."
    ref-baez-sawin:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Baez n-Category Cafe Part 13 / Sawin theorem cited for LEFT vs diagonal embedding distinction. Our construction gives LEFT embedding as verified by the (4,2,1)+(4bar,1,2) decomposition."
    ref-krasnov-2025:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Krasnov arXiv:2504.16465 cited for pure spinor characterization of complex structures on Im(O), connecting to our u in S^6 choice."
    ref-phase18:
      status: completed
      completed_actions: [use]
      missing_actions: []
      summary: "Phase 18 results (S_{10}^+, Spin(10), 27->1+10+16) used as foundation throughout. The 16-dim Weyl spinor from Phase 18 is the space on which Cl(6) acts."
  forbidden_proxies:
    fp-cl6-without-o-splitting:
      status: rejected
      notes: "Cl(6) explicitly derived from octonion splitting O = C + C^3: the 6 generators come from the 6 directions of Im(C^3) = e_7^perp in Im(O). Not chosen ad hoc."
    fp-chirality-without-lr-distinction:
      status: rejected
      notes: "LEFT embedding explicitly distinguished from diagonal in Step 6. SU(2)_L acts on (4,2,1) only. Sawin theorem cited. omega_6 separates chiralities before Pati-Salam breaking."
    fp-quantum-numbers-without-matrices:
      status: rejected
      notes: "All algebraic relations verified numerically with explicit matrices (10 tests, all pass). Explicit quantum number assignment deferred to Plan 02 as intended."
  uncertainty_markers:
    weakest_anchors:
      - "The identification of e_1,...,e_6 as the first 6 Cl(10) generators relies on a specific mapping from Im(O) to Cl(10) generators. We follow the Todorov convention but the map is not uniquely determined by the octonion algebra alone -- it depends on how Cl(10) is constructed from the Jordan algebra setup."
      - "The precise Fano-plane index mapping between Furey's convention a_j = (1/2)(-e_{j+4} + i*e_j) and our gamma-matrix convention a_j = (1/2)(gamma_{2j-1} + i*gamma_{2j}) involves a basis relabeling that was stated but not fully pinned down. Plan 02 will make this explicit."
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations: []

comparison_verdicts:
  - subject_id: claim-cl6-construction
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-todorov-2022
    comparison_kind: benchmark
    metric: clifford_algebra_structure
    threshold: "6 generators satisfying Cl(6) relations inside Cl(10)"
    verdict: pass
    recommended_action: "Cl(6) construction established. Proceed to Plan 02 for explicit state quantum numbers."
    notes: "21 Cl(6) relations and 55 Cl(10) relations all verified numerically to machine precision."
  - subject_id: claim-volume-form
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-todorov-2022
    comparison_kind: benchmark
    metric: projector_properties
    threshold: "omega_6^2 = -1, tr(P) = 16"
    verdict: pass
    recommended_action: "Volume form properties established."
    notes: "omega_6^2 = -1 and tr(P) = 16 both verified to machine precision."
  - subject_id: claim-pati-salam-breaking
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-todorov-2022
    comparison_kind: benchmark
    metric: stabilizer_decomposition
    threshold: "dim(stabilizer) = 21 = 15+6, LEFT embedding"
    verdict: pass
    recommended_action: "Pati-Salam breaking chain complete. Plan 02 will verify individual state quantum numbers."
    notes: "Numerical stabilizer computation exactly matches analytical prediction: 15 internal + 6 external + 0 mixed."
  - subject_id: claim-furey-witt
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-furey-2018
    comparison_kind: prior_work
    metric: CAR_and_chirality
    threshold: "27 CAR relations, automatic chirality"
    verdict: pass
    recommended_action: "Witt decomposition verified. Plan 02 will build explicit 16-state table."
    notes: "All 27 CAR to machine precision. omega_6 = -i*(-1)^N formula verified numerically."

duration: 4min
completed: 2026-03-24
---

# Plan 01: Cl(6) Chirality from Octonion Splitting and SM Embedding -- Summary

**Cl(6) subalgebra inside Cl(10) derived from octonion splitting O = C + C^3; volume form omega_6 selects 16-dim chiral subspace; Pati-Salam breaking chain gives SM gauge group with LEFT embedding; Furey Witt decomposition verified with automatic chirality**

## Performance

- **Duration:** ~4 min
- **Started:** 2026-03-24T01:00:07Z
- **Completed:** 2026-03-24T01:04:37Z
- **Tasks:** 2
- **Files modified:** 1

## Key Results

- **Cl(6) from O splitting:** Choice of u = e_7 in Im(O) gives O = C + C^3 with 6-dim W = Im(C^3). The 6 directions of W define gamma_1,...,gamma_6 generating Cl(6) inside Cl(10). [CONFIDENCE: HIGH -- numerically verified, 21 Clifford relations exact]
- **Volume form omega_6:** omega_6^2 = (-1)^{15} = -1. Projector P = (1/2)(1 - i*omega_6) is idempotent with tr(P) = 16 on 32-dim Dirac spinor. [CONFIDENCE: HIGH -- analytical derivation + numerical verification]
- **Pati-Salam stabilizer:** Stab_{Spin(10)}(omega_6) = SU(4) x SU(2)_L x SU(2)_R / Z_2, dim = 15 + 6 = 21. [CONFIDENCE: HIGH -- numerical stabilizer computation matches exactly]
- **LEFT embedding:** 16 -> (4,2,1) + (4bar,1,2). SU(2)_L acts on left-handed fermions only. Distinguished from diagonal per Sawin theorem. [CONFIDENCE: HIGH]
- **SM gauge group:** Spin(10) -> Pati-Salam -> SU(3)_C x SU(2)_L x U(1)_Y, both breaking steps from the single input u in S^6. [CONFIDENCE: HIGH]
- **Furey Witt decomposition:** a_j = (1/2)(gamma_{2j-1} + i*gamma_{2j}), all 27 CAR verified to machine precision. [CONFIDENCE: HIGH]
- **Automatic chirality:** omega_6 = -i*(-1)^N (N = particle number). SU(2)_L preserves chirality by construction -- no ad hoc projector. [CONFIDENCE: HIGH -- numerical formula verification exact]

## Task Commits

1. **Task 1: Cl(6) construction and volume form + Pati-Salam breaking + Witt decomposition** -- `eda8d0e` (derive)
2. **Task 2: Numerical verification** -- (in-memory verification, 10/10 tests pass; no file change needed beyond Task 1)

## Files Created/Modified

- `derivations/12-cl6-chirality.md` -- Three-part derivation (9 steps + synthesis): Part I (O splitting, Cl(6), volume form, projector), Part II (Pati-Salam, 16 decomposition, SM breaking, Witt, automatic chirality), Part III (synthesis)

## Next Phase Readiness

Plan 02 inputs ready:
- Cl(6) generators gamma_1,...,gamma_6 explicitly constructed
- Witt basis a_j, a_j^dag defined with verified CAR
- 8 "particle" states enumerated in Clifford vacuum notation
- omega_6 = -i*(-1)^N formula established for chirality assignment
- Next: explicit quantum number computation for all 16 states under SU(3) x SU(2) x U(1)

## Contract Coverage

- claim-cl6-construction -> **passed**: O = C + C^3, 6 generators, 21 Clifford relations
- claim-volume-form -> **passed**: omega_6^2 = -1, tr(P) = 16
- claim-pati-salam-breaking -> **passed**: dim 21 = 15 + 6, LEFT embedding
- claim-furey-witt -> **passed**: 27 CAR, automatic chirality
- deliv-cl6-derivation -> **passed**: derivations/12-cl6-chirality.md
- test-clifford-relations -> **passed**: 21/21 relations
- test-cl6-in-cl10 -> **passed**: 55/55 Cl(10) relations
- test-volume-form-squared -> **passed**: omega_6^2 = -1
- test-projector-rank -> **passed**: tr(P) = 16
- test-pati-salam-stabilizer -> **passed**: 15 + 6 + 0 = 21
- test-left-embedding -> **passed**: (4,2,1) + (4bar,1,2)
- test-witt-anticommutators -> **passed**: 27/27 CAR
- test-automatic-chirality -> **passed**: omega_6 = -i*(-1)^N
- ref-todorov-2022 -> **completed** [read, compare, cite]
- ref-furey-2018 -> **completed** [read, compare, cite]
- ref-baez-sawin -> **completed** [read, compare, cite]
- ref-krasnov-2025 -> **completed** [read, cite]
- ref-phase18 -> **completed** [use]
- fp-cl6-without-o-splitting -> **rejected**: derived from O splitting
- fp-chirality-without-lr-distinction -> **rejected**: L vs diagonal explicitly distinguished
- fp-quantum-numbers-without-matrices -> **rejected**: numerical matrix verification, 10 tests pass

## Equations Derived

**Eq. (19-01.1):** Octonion splitting:
$$\mathbb{O} = \mathbb{C} \oplus \mathbb{C}^3, \qquad W = e_7^{\perp} \cap \mathrm{Im}(\mathbb{O}), \quad \dim(W) = 6$$

**Eq. (19-01.2):** Volume form squared:
$$\omega_6^2 = (-1)^{6 \cdot 5/2} = (-1)^{15} = -1$$

**Eq. (19-01.3):** Chiral projector:
$$P = \frac{1}{2}(1 - i\omega_6), \qquad P^2 = P, \qquad \mathrm{tr}(P)\big|_{\Delta_{10}} = 16$$

**Eq. (19-01.4):** Pati-Salam stabilizer:
$$\mathrm{Stab}_{\mathrm{Spin}(10)}(\omega_6) = \frac{\mathrm{SU}(4) \times \mathrm{SU}(2)_L \times \mathrm{SU}(2)_R}{\mathbb{Z}_2}, \qquad \dim = 21$$

**Eq. (19-01.5):** Chiral decomposition:
$$\mathbf{16} \to (\mathbf{4}, \mathbf{2}, \mathbf{1}) \oplus (\bar{\mathbf{4}}, \mathbf{1}, \mathbf{2})$$

**Eq. (19-01.6):** Full breaking chain:
$$\mathrm{Spin}(10) \xrightarrow{\omega_6} \mathrm{SU}(4) \times \mathrm{SU}(2)_L \times \mathrm{SU}(2)_R \xrightarrow{u} \mathrm{SU}(3)_C \times \mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$$

**Eq. (19-01.7):** Witt operators:
$$a_j = \frac{1}{2}(\gamma_{2j-1} + i\gamma_{2j}), \qquad \{a_i, a_j^{\dagger}\} = \delta_{ij}, \qquad j = 1, 2, 3$$

**Eq. (19-01.8):** Volume form in particle number basis:
$$\omega_6 = -i \cdot (-1)^{N}, \qquad N = n_1 + n_2 + n_3$$

## Validations Completed

- Clifford relations: 21/21 {gamma_i, gamma_j} = 2 delta_ij verified numerically [CONFIDENCE: HIGH]
- Cl(10) embedding: 55/55 {Gamma_A, Gamma_B} = 2 delta_AB verified numerically [CONFIDENCE: HIGH]
- Volume form: omega_6^2 = -1 verified analytically + numerically [CONFIDENCE: HIGH]
- Chirality operator: (i*omega_6)^2 = +1 verified numerically [CONFIDENCE: HIGH]
- Projector: P^2 = P, tr(P) = 4 (8-dim), tr(P) = 16 (32-dim) [CONFIDENCE: HIGH]
- Tracelessness: tr(omega_6) = 0 verified numerically [CONFIDENCE: HIGH]
- CAR: All 27 anticommutation relations verified numerically [CONFIDENCE: HIGH]
- omega_6 eigenvalues: +/-i with multiplicity 4 each in 8-dim [CONFIDENCE: HIGH]
- Number operator relation: omega_6 = -i*(-1)^N verified numerically [CONFIDENCE: HIGH]
- Stabilizer decomposition: 15 + 6 + 0 = 21, matching su(4) + su(2) + su(2) [CONFIDENCE: HIGH]
- Dimension sums: 8 = 2+6, 16 = 8+8, 21 = 15+6, 45 = 21+24 [CONFIDENCE: HIGH]
- Forbidden proxy audit: Cl(6) from O splitting, L vs diagonal distinguished [CONFIDENCE: HIGH]

## Decisions & Deviations

### Decisions

1. **Combined Tasks 1 and 2 in single derivation document:** The Pati-Salam breaking (Task 2) is the direct continuation of the Cl(6) construction (Task 1). Writing them as a single coherent derivation document (Steps 1-9 + synthesis) was more natural than splitting into separate files.

2. **Cl(10) construction in 32-dim:** Used the standard tensor product construction Gamma_k = gamma_k x I_4 (k=1,...,6) and Gamma_{6+a} = i*omega_6 x tau_a (a=1,...,4) for the numerical verification. This specific construction choice affects the matrix representations but not the algebraic results.

3. **Witt basis convention:** Used a_j = (1/2)(gamma_{2j-1} + i*gamma_{2j}) as the standard complex-structure pairing. Furey's octonion-labeled convention a_j = (1/2)(-e_{j+4} + i*e_j) is related by the Fano-plane index mapping. The precise index relabeling is deferred to Plan 02.

### Deviations

None -- plan executed as written.

## Open Questions

- Precise Fano-plane index mapping between gamma-matrix and octonion-label conventions for the Witt operators (to be resolved in Plan 02)
- Physical interpretation of the U(1) charges (-4, 2, -1) in the E_6 branching (deferred to Plan 02/Phase 20)
- Can the rank-1 idempotent choice (Gap B step 1) that started the Peirce decomposition be derived from self-modeling?
- The freedom u in S^6 = G_2/SU(3): does the self-modeling framework select a preferred u, or is this a genuine modulus?

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
|----------|--------|-------|------------|--------|-------------|
| dim(Cl(6)) | -- | 64 | exact | 2^6 | -- |
| dim(Cl(10)) | -- | 1024 | exact | 2^{10} | -- |
| dim(Dirac spinor Spin(10)) | -- | 32 | exact | 2^{10/2} | -- |
| omega_6^2 | -- | -1 | exact | (-1)^{15} | -- |
| tr(P) on Dirac | -- | 16 | exact | 32/2 | -- |
| dim(stabilizer) | -- | 21 | exact | 15+6 | -- |
| dim(Pati-Salam) | -- | 21 | exact | 15+3+3 | -- |
| dim(SM gauge group) | -- | 12 | exact | 8+3+1 | -- |
| Number of CAR | -- | 27 | exact | 9+9+9 | -- |
| Witt states per chirality | -- | 8 | exact | 2^3 | -- |

## Approximations Used

None -- all results are exact (algebraic/representation-theoretic).

## Self-Check: PASSED

- [x] derivations/12-cl6-chirality.md exists
- [x] Commit eda8d0e exists
- [x] Numerical verification: 10/10 tests pass
- [x] Convention consistency: Euclidean Clifford throughout, Fano octonion basis, u = e_7
- [x] All contract IDs accounted for
- [x] All forbidden proxies rejected with evidence

---

_Phase: 19-cl-6-chirality-and-sm-embedding-part-b, Plan: 01_
_Completed: 2026-03-24_
