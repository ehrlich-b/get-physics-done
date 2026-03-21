---
phase: 04-sequential-product-formalization
plan: 04
depth: full
one-liner: "S4 (orthogonality symmetry) proved for all phi choices via Alfsen-Shultz facial orthogonality -- with S1-S7 complete, vdW Theorem 1 gives EJA classification (spin factor V_3 for qubits)"
subsystem: [formalism, derivation]
tags: [sequential-product, axiom-verification, order-unit-space, facial-orthogonality, EJA, spin-factor]

requires:
  - phase: 04-sequential-product-formalization
    plan: 01
    provides: compression-based SP for sharp effects
  - phase: 04-sequential-product-formalization
    plan: 06
    provides: corrected product formula Eq. 04-06.4
  - phase: 04-sequential-product-formalization
    plan: 02
    provides: non-associativity verified, kill gate passed
  - phase: 04-sequential-product-formalization
    plan: 03
    provides: S1-S3, S5-S7 all proved and verified

provides:
  - Formal proof of S4 (compatibility of orthogonal effects) for the self-modeling sequential product
  - S4 is phi-INDEPENDENT (holds for all f with f(0, x) = 0, not just f = sqrt)
  - Two-case proof structure: full-rank (forces b = 0) and rank-deficient (facial absorption via A5)
  - With S1-S7 complete, vdW Theorem 1 applies: OUS is order-isomorphic to a Euclidean Jordan algebra
  - EJA identification for qubits: spin factor V_3 (= M_2(C)^sa)
  - 186 SymPy tests on M_2(C)^sa including general-position effects and multiple phi choices
  - Circularity audit passed: proof uses only OUS primitives (no Hilbert space imports)
  - Plan 05 (S4 failure characterization) SKIPPED because S4 passed

affects: [05-phase-completion]

methods:
  added: [Alfsen-Shultz facial orthogonality (Prop. 7.43), Peirce decomposition direct-sum argument, spectral case analysis]
  patterns: [facial absorption -- C_p(b) = 0 and b >= 0 implies b in face(p^perp), complementary faces have zero compression overlap]

key-files:
  created:
    - derivations/04-axiom-S4.md
  modified:
    - code/sp_verification.py

key-decisions:
  - "S4 proof uses facial absorption (A5 = Alfsen-Shultz Prop. 7.43) as the linchpin -- this is construction-specific"
  - "Two-case structure: full-rank a forces b = 0 via Peirce completeness; rank-deficient a uses facial absorption"
  - "Phi-independence follows from f(0, x) = 0, which any reasonable mixing function satisfies"
  - "EJA classification invokes vdW Theorem 1 without re-derivation"

patterns-established:
  - "Facial absorption (A5): C_p(b) = 0 with b >= 0 forces b into face(p^perp)"
  - "Complementary face orthogonality: q_j in face(sum p_k) and a in face(sum p_i) with sum p_i + sum p_k = 1 gives C_{q_j}(a) = 0"
  - "Peirce 1-space vanishing for effects in complementary faces"

conventions:
  - "sequential product: a & b (non-commutative)"
  - "orthogonality: a perp b iff a & b = 0"
  - "complement: a^perp = 1 - a"
  - "axiom source: arXiv:1803.11139 Definition 2 EXCLUSIVELY"
  - "compression: C_p (Alfsen-Shultz P-projection for face(p))"
  - "dimensionless algebraic quantities"

plan_contract_ref: ".gpd/phases/04-sequential-product-formalization/04-04-PLAN.md#/contract"
contract_results:
  claims:
    claim-s4:
      status: passed
      summary: "S4 (compatibility of orthogonal effects) PROVED for the self-modeling sequential product on all finite-dimensional spectral OUS. Two-case proof: (A) full-rank a forces b = 0 via Peirce completeness; (B) rank-deficient a triggers facial absorption (Alfsen-Shultz Prop. 7.43) forcing b into the complementary face, then reverse product vanishes by complementary-face orthogonality. S4 is phi-INDEPENDENT: holds for all mixing functions f with f(0,x) = 0."
      linked_ids: [deliv-s4-proof, test-s4-qubit, test-s4-general, test-s4-phi-dependence, ref-vdw2018, ref-vdw2018b]
    claim-eja-classification:
      status: passed
      summary: "With S1-S7 all proved, vdW Theorem 1 (arXiv:1803.11139) applies: any finite-dimensional spectral OUS with the self-modeling sequential product is order-isomorphic to a Euclidean Jordan algebra. For M_2(C)^sa, the EJA is the spin factor V_3."
      linked_ids: [deliv-s4-proof, test-eja-invoke, ref-vdw2018]
  deliverables:
    deliv-s4-proof:
      status: passed
      path: "derivations/04-axiom-S4.md"
      summary: "Complete formal proof of S4 (489 lines) with: verbatim S4 statement from arXiv:1803.11139 Def. 2, two-case proof, facial orthogonality lemma, phi-dependence analysis, EJA classification, circularity audit, proof-length red flag check."
      linked_ids: [claim-s4, claim-eja-classification, test-s4-qubit, test-s4-general, test-s4-phi-dependence, test-eja-invoke]
  acceptance_tests:
    test-s4-qubit:
      status: passed
      summary: "186 SymPy tests on M_2(C)^sa: 10 sharp orthogonal projections, 12 general effects, 54 general-position (rotated Bloch vectors), 4 full-rank (vacuous), 52 parametric search, 30 scaled projections, 13 coarse-graining phi, 5 trivial phi, 6 Luders positive control. All pass."
      linked_ids: [claim-s4, deliv-s4-proof, ref-vdw2018]
    test-s4-general:
      status: passed
      summary: "General proof completed for arbitrary finite-dimensional spectral OUS. Proof is 92 lines (vs 19 for S1-S3 combined), references facial absorption (A5) as construction-specific property, handles both sharp and general effects via spectral extension. Red flag check passed."
      linked_ids: [claim-s4, deliv-s4-proof, ref-vdw2018]
    test-s4-phi-dependence:
      status: passed
      summary: "S4 is phi-INDEPENDENT. Holds for all mixing functions f with f(0,x) = 0. Tested: phi = faithful (f = sqrt), phi = coarse-graining (f = (1/2)sqrt, (1/3)sqrt, (3/4)sqrt), phi = trivial (f = 0). All pass. The proof depends only on OUS facial structure and f(0,x) = 0, not on f for positive arguments."
      linked_ids: [claim-s4, deliv-s4-proof]
    test-eja-invoke:
      status: passed
      summary: "vdW Theorem 1 invoked with all seven axiom premises verified (S1-S3 from Plan 03, S4 from this plan, S5-S7 from Plan 03). EJA type for M_2(C)^sa identified as spin factor V_3 via Jordan-von Neumann-Wigner classification."
      linked_ids: [claim-eja-classification, deliv-s4-proof, ref-vdw2018]
  references:
    ref-vdw2018:
      status: completed
      completed_actions: [read, use, cite]
      missing_actions: []
      summary: "S4 definition quoted verbatim from Def. 2. Theorem 1 invoked for EJA classification. Prop. 28-29 consulted for alternative S4 proof routes."
    ref-vdw2018b:
      status: completed
      completed_actions: [read, use]
      missing_actions: []
      summary: "Three characterizations of sequential product consulted. Inner product symmetry route considered but facial orthogonality route proved more direct."
  forbidden_proxies:
    fp-s4-assumed:
      status: rejected
      notes: "S4 has a complete 92-line formal proof via facial orthogonality, not assumed."
    fp-quantum-s4:
      status: rejected
      notes: "Proof uses only OUS primitives (compressions, faces, Peirce decomposition). Luders product used only as positive control, not as the proof mechanism. Circularity audit passed."
    fp-short-proof:
      status: rejected
      notes: "S4 proof body is 92 lines vs 19 lines for S1-S3 combined. Red flag check passed. Additional length comes from case analysis, facial orthogonality lemma, and phi-dependence analysis."
    fp-symmetric-examples:
      status: rejected
      notes: "54 general-position tests (rotated Bloch vectors, non-basis-aligned effects) included in the 186-test suite. Effects in general position satisfy S4 equally well."
  uncertainty_markers:
    weakest_anchors:
      - "The Peirce 1-space vanishing argument for general n-projector case (n > 2) relies on facial structure of complementary faces extending to mixed Peirce components. Verified for n = 2 (M_2(C)^sa); general n relies on Alfsen-Shultz Theorem 9.37."
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations: []

comparison_verdicts:
  - subject_id: claim-s4
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-vdw2018
    comparison_kind: benchmark
    metric: axiom_satisfaction
    threshold: "S4 holds for the self-modeling sequential product"
    verdict: pass
    recommended_action: "S1-S7 complete. Invoke Theorem 1 for EJA classification. Plan 05 skipped. Phase 5 unblocked."
    notes: "S4 proved via Alfsen-Shultz facial orthogonality (Prop. 7.43). Phi-independent. 186 SymPy tests all pass."
  - subject_id: claim-eja-classification
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-vdw2018
    comparison_kind: benchmark
    metric: theorem_premises
    threshold: "all seven axioms S1-S7 satisfied"
    verdict: pass
    recommended_action: "EJA classification established. Proceed to Phase 5."
    notes: "vdW Theorem 1 premises fully verified. EJA type for M_2(C)^sa: spin factor V_3."

duration: 15min
completed: 2026-03-21
---

# Plan 04: S4 Decisive Test -- Summary

**S4 (orthogonality symmetry) proved for all phi choices via Alfsen-Shultz facial orthogonality -- with S1-S7 complete, vdW Theorem 1 gives EJA classification (spin factor V_3 for qubits).**

## Performance

- **Duration:** ~15 min
- **Started:** 2026-03-21T02:28:00Z
- **Completed:** 2026-03-21T02:43:00Z
- **Tasks:** 3 (2 auto + 1 checkpoint, APPROVED)
- **Files modified:** 2

## Key Results

- **S4 PROVED** for the self-modeling sequential product on all finite-dimensional spectral OUS. The proof uses Alfsen-Shultz facial orthogonality (Prop. 7.43) as the linchpin. [CONFIDENCE: HIGH]
- **Two-case proof:** (A) Full-rank a: Peirce completeness forces b = 0. (B) Rank-deficient a: facial absorption (A5) forces b into the complementary face, then reverse product vanishes by complementary-face orthogonality. [CONFIDENCE: HIGH]
- **S4 is phi-INDEPENDENT:** Holds for ALL mixing functions f with f(0, x) = 0, including faithful (sqrt), coarse-graining, and trivial (f = 0). [CONFIDENCE: HIGH]
- **186 SymPy tests on M_2(C)^sa:** Sharp, general, general-position, full-rank, parametric, scaled, multiple phi, and Luders positive control. All pass. [CONFIDENCE: HIGH]
- **EJA classification established:** With S1-S7 all proved, vdW Theorem 1 applies. For M_2(C)^sa, the EJA is the spin factor V_3. [CONFIDENCE: HIGH]
- **Circularity audit PASSED:** S4 proof uses only OUS primitives (no Hilbert space imports). [CONFIDENCE: HIGH]
- **Plan 05 (S4 failure characterization) SKIPPED** because S4 passed.

## Task Commits

1. **Task 1: Exhaustive SymPy S4 testing on M_2(C)^sa** -- `6585dae` (compute)
2. **Task 2: General S4 proof** -- `e9ffcf4` (derive)
3. **Task 3: S4 result checkpoint** -- APPROVED by researcher

## Files Created/Modified

- `derivations/04-axiom-S4.md` -- Complete S4 proof: two-case structure, facial orthogonality lemma, phi-dependence analysis, EJA classification, circularity audit, proof-length red flag check
- `code/sp_verification.py` -- S4 test suite: 186 tests across sharp/general/general-position effects, multiple phi choices, Luders positive control

## Next Phase Readiness

**Phase 4 is essentially complete.** All seven axioms S1-S7 are proved for the self-modeling sequential product:

| Axiom | Status | Proved in | Key Argument |
|-------|--------|-----------|--------------|
| S1 (additivity) | PASS | Plan 03 | Linearity of compressions and Peirce projections |
| S2 (continuity) | PASS | Plan 03 | Continuity of spectral decomposition in finite dim |
| S3 (unitality) | PASS | Plan 06 | C_1 = id |
| S4 (orthogonality symmetry) | PASS | Plan 04 | Facial orthogonality (Alfsen-Shultz Prop. 7.43) |
| S5 (compatible associativity) | PASS | Plan 03 | Compression composition + spectral factorization |
| S6 (compatible additivity) | PASS | Plan 03 | a & 1 = a + simultaneous diagonalizability |
| S7 (compatible multiplicativity) | PASS | Plan 03 | Functional calculus commutativity |

vdW Theorem 1 gives EJA classification. Plan 05 is skipped. Phase 5 is unblocked.

## Contract Coverage

- claim-s4 -> **passed**: S4 proved via facial orthogonality, phi-independent
- claim-eja-classification -> **passed**: vdW Theorem 1 invoked, spin factor V_3 for qubits
- deliv-s4-proof -> **passed**: derivations/04-axiom-S4.md (489 lines)
- test-s4-qubit -> **passed**: 186 SymPy tests all pass
- test-s4-general -> **passed**: general proof for arbitrary finite-dim spectral OUS
- test-s4-phi-dependence -> **passed**: phi-independent (all f with f(0,x) = 0)
- test-eja-invoke -> **passed**: Theorem 1 premises verified, EJA type identified
- ref-vdw2018 -> **completed** [read, use, cite]
- ref-vdw2018b -> **completed** [read, use]
- fp-s4-assumed -> **rejected**: complete formal proof provided
- fp-quantum-s4 -> **rejected**: OUS-only proof, circularity audit passed
- fp-short-proof -> **rejected**: 92 lines vs 19 for S1-S3 combined
- fp-symmetric-examples -> **rejected**: 54 general-position tests included

## Equations Derived

No new equations derived. The proof uses the corrected product formula Eq. (04-06.4) from Plan 06.

**Key structural results established:**

**Eq. (04-04.1):** Facial absorption lemma (the linchpin):
$$C_p(b) = 0 \text{ and } b \geq 0 \implies b \in \text{face}(p^\perp) \quad \text{(Alfsen-Shultz Prop. 7.43)}$$

**Eq. (04-04.2):** S4 theorem statement:
$$a \mathbin{\&} b = 0 \implies b \mathbin{\&} a = 0 \quad \text{for all effects } a, b \in [0, 1]_V$$

**Eq. (04-04.3):** EJA classification (vdW Theorem 1):
$$\text{S1-S7 hold} \implies (V, \leq, 1) \cong \text{Euclidean Jordan algebra}$$

## Validations Completed

- S4 on sharp orthogonal projections: 10 tests, all pass (trivial case) [CONFIDENCE: HIGH]
- S4 on general effects: 12 tests, all pass [CONFIDENCE: HIGH]
- S4 on general-position effects (rotated Bloch vectors): 54 tests, all pass [CONFIDENCE: HIGH]
- S4 on full-rank effects: 4 tests, vacuously true (only b = 0 satisfies a & b = 0) [CONFIDENCE: HIGH]
- S4 parametric search (13 directions x 4 scales): 52 tests, all pass [CONFIDENCE: HIGH]
- S4 scaled projections: 30 tests, all pass [CONFIDENCE: HIGH]
- S4 coarse-graining phi (3 choices): 13 tests, all pass [CONFIDENCE: HIGH]
- S4 trivial phi (f = 0): 5 tests, all pass [CONFIDENCE: HIGH]
- Luders positive control: 6 tests, all pass [CONFIDENCE: HIGH]
- Circularity audit: no Hilbert space imports in proof [CONFIDENCE: HIGH]
- Proof-length red flag: 92 lines S4 vs 19 lines S1-S3 combined -- PASSED [CONFIDENCE: HIGH]

## Decisions & Deviations

### Decisions

1. **Proof route:** Facial orthogonality (Route C from PLAN) proved most direct. The inner product symmetry route (Route B) was considered but required constructing an inner product from OUS primitives, which is more involved. Route C uses existing Alfsen-Shultz machinery.

2. **Case structure:** Two cases (full-rank vs rank-deficient) plus the trivial a = 0 case. The full-rank case is simple (Peirce completeness). The rank-deficient case carries all the technical weight via facial absorption.

3. **Phi-independence characterization:** S4 holds for all f with f(0, x) = 0. This is stronger than expected -- the plan anticipated possible phi-dependence. The proof shows S4 is a property of OUS facial geometry, not the product's coherence level.

### Deviations

None -- plan executed as specified.

## Open Questions

- Does the EJA classification extend to infinite-dimensional spectral OUS? (vdW Theorem 1 is stated for finite dimensions)
- Can the facial orthogonality proof be adapted for non-spectral OUS?
- What is the physical interpretation of the spin factor V_3 structure beyond the Bloch ball isomorphism?

## Self-Check: PASSED

- [x] derivations/04-axiom-S4.md exists (489 lines)
- [x] code/sp_verification.py updated with S4 test suite
- [x] Commit 6585dae verified in git log
- [x] Commit e9ffcf4 verified in git log
- [x] All 186 SymPy tests pass
- [x] Luders positive control passes
- [x] No Hilbert space imports in S4 proof (circularity audit)
- [x] Proof length 92 lines > S1-S3 combined 19 lines (red flag check)
- [x] All axiom statements from arXiv:1803.11139 Definition 2
- [x] Researcher checkpoint APPROVED

---

_Phase: 04-sequential-product-formalization, Plan: 04_
_Completed: 2026-03-21_
