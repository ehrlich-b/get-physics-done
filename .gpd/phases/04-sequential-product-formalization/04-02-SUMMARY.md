---
phase: 04-sequential-product-formalization
plan: 02
depth: full
one-liner: "Self-modeling sequential product is non-associative: explicit witness Delta = [[39/224 - 3sqrt(3)/32, sqrt(3)/112], [sqrt(3)/112, -11/224 + sqrt(3)/32]] != 0, kill gate passed"
subsystem: [formalism, derivation]
tags: [sequential-product, non-associativity, Luders, Westerbaan-vdW, kill-gate, order-unit-space]

requires:
  - phase: 04-sequential-product-formalization
    plan: 01
    provides: compression-based SP for sharp effects, SymPy verification harness
  - phase: 04-sequential-product-formalization
    plan: 06
    provides: corrected product formula (Eq. 04-06.4) with Peirce 1-space feedback, corrected_sp() function

provides:
  - Explicit non-associativity witness (a, b, c) with exact symbolic computation
  - Proof that Delta[0,0] = 39/224 - 3*sqrt(3)/32 is irrational, hence nonzero
  - Confirmation that corrected product Delta == Luders Delta (consistency)
  - Kill gate PASSED -- sequential product route survives
  - 20/20 random triples non-associative -- non-associativity is generic

affects: [04-03, 04-04, 04-05]

methods:
  added: [non-associativity witness construction, irrationality argument for nonzero verification]
  patterns: [corrected product = Luders on M_2(C)^sa, so non-associativity test applies to both simultaneously]

key-files:
  created:
    - derivations/04-non-associativity.md
  modified:
    - code/sp_verification.py

key-decisions:
  - "Witness triple: a=diag(3/4,1/4), b=(I+sigma_x/2)/2, c=P0 -- chosen because a and b don't commute, c is sharp"
  - "Irrationality argument for exact nonzero proof: 39/224 = 3*sqrt(3)/32 would require sqrt(3) = 13/7, but (13/7)^2 = 169/49 != 3"
  - "Kill gate passed: non-associativity necessary by WWvdW for non-commutative algebra"

patterns-established:
  - "Non-associativity is generic (20/20 random triples), not a special-case artifact"
  - "Corrected product = Luders on M_2(C)^sa, so one non-associativity test covers both"

conventions:
  - "sequential product: a & b (non-commutative)"
  - "axiom source: arXiv:1803.11139 Definition 2 exclusively"
  - "compression: C_p (Alfsen-Shultz P-projection for face(p))"
  - "dimensionless algebraic quantities"

plan_contract_ref: ".gpd/phases/04-sequential-product-formalization/04-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-non-assoc:
      status: passed
      summary: "The self-modeling sequential product is non-associative. Explicit witness: a=diag(3/4,1/4), b=(I+sigma_x/2)/2, c=P0 gives Delta[0,0] = 39/224 - 3*sqrt(3)/32 != 0 (proved by irrationality of sqrt(3)). Verified with exact SymPy arithmetic. 20/20 random triples also non-associative."
      linked_ids: [deliv-non-assoc, test-non-assoc-witness, ref-vdw2018, ref-wwvdw2020]
  deliverables:
    deliv-non-assoc:
      status: passed
      path: "derivations/04-non-associativity.md"
      summary: "Complete derivation with explicit triple, step-by-step exact computation of both (a&b)&c and a&(b&c), irrationality proof of nonzero, positive controls, and WWvdW implication statement."
      linked_ids: [claim-non-assoc, test-non-assoc-witness]
  acceptance_tests:
    test-non-assoc-witness:
      status: passed
      summary: "Exhibited triple (a,b,c) with exact symbolic Delta != 0 (SymPy Rational + sqrt). Delta[0,0] = 39/224 - 3*sqrt(3)/32, Delta[0,1] = sqrt(3)/112 -- both symbolically verified nonzero. Positive controls: Luders also non-associative (same Delta), matrix mult associative (Delta = 0)."
      linked_ids: [claim-non-assoc, deliv-non-assoc, ref-vdw2018, ref-wwvdw2020]
  references:
    ref-vdw2018:
      status: completed
      completed_actions: [use, cite]
      missing_actions: []
      summary: "Product definition (Eq. 04-06.4) from vdW axioms used throughout. Non-associativity computed for this specific product."
    ref-wwvdw2020:
      status: completed
      completed_actions: [cite]
      missing_actions: [read]
      summary: "Theorem cited: associativity implies commutativity in normal sequential effect algebras. Contrapositive applied: non-commutative M_2(C)^sa requires non-associativity. Kill gate interpretation stated."
  forbidden_proxies:
    fp-assoc-claim:
      status: rejected
      notes: "Non-associativity is verified for the SELF-MODELING product (corrected_sp), not just claimed from Luders being non-associative. The fact that corrected = Luders on M_2(C)^sa is a consistency check, not the proof method."
    fp-numerical-only:
      status: rejected
      notes: "All computation uses SymPy exact arithmetic (Rational, sqrt). Nonzero proof uses irrationality of sqrt(3), not floating-point comparison. Numerical values shown only for illustration."
  uncertainty_markers:
    weakest_anchors:
      - "WWvdW theorem is cited, not re-derived. Its hypothesis ('normal sequential effect algebra') must be verified to match our construction."
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations: []

comparison_verdicts:
  - subject_id: claim-non-assoc
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-wwvdw2020
    comparison_kind: benchmark
    metric: associativity_test
    threshold: "Delta != 0"
    verdict: pass
    recommended_action: "Kill gate passed. Proceed to S4-S7 verification (Plans 03-05)."
    notes: "Delta = [[39/224 - 3sqrt(3)/32, sqrt(3)/112], [sqrt(3)/112, -11/224 + sqrt(3)/32]], symbolically nonzero. Consistent with WWvdW: non-associativity is necessary for non-commutative algebra."

duration: 10min
completed: 2026-03-21
---

# Plan 02: Non-Associativity Verification -- Summary

**Self-modeling sequential product is non-associative: explicit witness Delta != 0 verified with exact symbolic arithmetic, kill gate passed, program continues.**

## Performance

- **Duration:** ~10 min
- **Started:** 2026-03-21T02:06:49Z
- **Completed:** 2026-03-21T02:17:00Z
- **Tasks:** 2
- **Files modified:** 2

## Key Results

- **NON-ASSOCIATIVITY WITNESS (Eq. 04-02.5):** For a=diag(3/4,1/4), b=(I+sigma_x/2)/2, c=P0: Delta = (a&b)&c - a&(b&c) = [[39/224 - 3sqrt(3)/32, sqrt(3)/112], [sqrt(3)/112, -11/224 + sqrt(3)/32]] != 0. [CONFIDENCE: HIGH]
- **EXACT NONZERO PROOF:** Delta[0,0] = 39/224 - 3sqrt(3)/32 != 0 because sqrt(3) is irrational (if 39/224 = 3sqrt(3)/32 then sqrt(3) = 13/7, but (13/7)^2 = 169/49 != 3). [CONFIDENCE: HIGH]
- **POSITIVE CONTROLS PASS:** Luders product gives identical Delta (consistency); matrix multiplication gives Delta = 0 (associativity correctly detected). [CONFIDENCE: HIGH]
- **GENERIC NON-ASSOCIATIVITY:** 20/20 random rational Bloch-parameterized triples are non-associative. Non-associativity is the generic case, not a special artifact. [CONFIDENCE: HIGH]
- **KILL GATE PASSED:** By Westerbaan-Westerbaan-vdW (Quantum 4, 378, 2020), associativity would force commutativity. The product is non-associative, so the algebra is not forced to be commutative. The sequential product route survives. [CONFIDENCE: HIGH]

## Task Commits

1. **Task 1: Construct and verify non-associativity witness** -- `4c2ccd8` (derive)
2. **Task 2: SymPy exact verification** -- `3b48ccb` (compute)

## Files Created/Modified

- `derivations/04-non-associativity.md` -- Formal derivation: witness triple, step-by-step computation, irrationality proof, positive controls, WWvdW implication
- `code/sp_verification.py` -- Updated harness: test_non_associativity(), test_corrected_non_associativity() (witness + controls), test_non_associativity_random_search() (20 random triples), all pass

## Next Phase Readiness

**Plans 03-05 remain unblocked.** The non-associativity result is a prerequisite confirmation, not a blocker. Specifically:

- **Plan 03 (S4-S5):** Orthogonality symmetry and compatible associativity. Non-associativity is for GENERAL triples; S5 requires associativity only for COMPATIBLE effects (which commute under the product). These are different claims.
- **Plan 04 (S6-S7):** Compatibility additivity and multiplicativity. Independent of non-associativity.
- **Plan 05 (EJA classification):** If S1-S7 all hold, vdW Theorem 1 forces EJA structure. Non-associativity is consistent with this (EJAs have non-associative Jordan products in general).

## Contract Coverage

- claim-non-assoc -> **passed**: explicit witness with exact symbolic verification
- deliv-non-assoc -> **passed**: derivations/04-non-associativity.md
- test-non-assoc-witness -> **passed**: SymPy exact arithmetic, positive controls, random search
- ref-vdw2018 -> **completed** [use, cite]
- ref-wwvdw2020 -> **completed** [cite] (read action not performed; theorem statement cited from training data)
- fp-assoc-claim -> **rejected**: self-modeling product tested directly, not inferred from Luders
- fp-numerical-only -> **rejected**: all computation uses SymPy Rational + sqrt, nonzero proof by irrationality

## Equations Derived

**Eq. (04-02.1):** Sequential product of witness effects:
$$a \mathbin{\&} b = \begin{pmatrix} 3/8 & \sqrt{3}/16 \\ \sqrt{3}/16 & 1/8 \end{pmatrix}$$

**Eq. (04-02.2):** Left-associated triple product:
$$(a \mathbin{\&} b) \mathbin{\&} c = \begin{pmatrix} 81/224 & 9\sqrt{3}/224 \\ 9\sqrt{3}/224 & 3/224 \end{pmatrix}$$

**Eq. (04-02.3):** Inner product:
$$b \mathbin{\&} c = \begin{pmatrix} \sqrt{3}/8 + 1/4 & 1/8 \\ 1/8 & 1/4 - \sqrt{3}/8 \end{pmatrix}$$

**Eq. (04-02.4):** Right-associated triple product:
$$a \mathbin{\&} (b \mathbin{\&} c) = \begin{pmatrix} 3\sqrt{3}/32 + 3/16 & \sqrt{3}/32 \\ \sqrt{3}/32 & 1/16 - \sqrt{3}/32 \end{pmatrix}$$

**Eq. (04-02.5):** Non-associativity witness:
$$\Delta = (a \mathbin{\&} b) \mathbin{\&} c - a \mathbin{\&} (b \mathbin{\&} c) = \begin{pmatrix} 39/224 - 3\sqrt{3}/32 & \sqrt{3}/112 \\ \sqrt{3}/112 & -11/224 + \sqrt{3}/32 \end{pmatrix} \neq 0$$

## Validations Completed

- Non-associativity witness: Delta[0,0] = 39/224 - 3*sqrt(3)/32 != 0 (irrationality proof) [CONFIDENCE: HIGH]
- Positive control: Luders product gives identical Delta (corrected = Luders on M_2(C)^sa) [CONFIDENCE: HIGH]
- Positive control: matrix multiplication gives Delta = 0 (test framework correctly distinguishes) [CONFIDENCE: HIGH]
- Random search: 20/20 triples non-associative (non-associativity is generic) [CONFIDENCE: HIGH]
- All effects in witness are valid: eigenvalues in [0,1] [CONFIDENCE: HIGH]

## Decisions & Deviations

### Decisions

1. **Witness selection:** First attempt (a=diag(3/4,1/4), b=(I+sigma_x/2)/2, c=(I+sigma_y/2)/2) gave Delta = 0 because all three effects have the same eigenvalue spectrum {3/4, 1/4}. Switching c to P0 (eigenvalues {1, 0}) broke the symmetry and produced nonzero Delta.

2. **Irrationality argument for nonzero proof:** Rather than relying on numerical evaluation (forbidden by contract), proved Delta[0,0] != 0 by assuming equality and deriving that sqrt(3) = 13/7, which contradicts (13/7)^2 = 169/49 != 3.

### Deviations

None -- plan executed as specified. The initial symmetric triple giving zero was handled within the plan's "choose candidate effects" step, not a deviation.

## Open Questions

- Is the WWvdW theorem's hypothesis ("normal sequential effect algebra") satisfied by our construction? This needs to be checked in Plans 03-05.
- What is the structure of the non-associativity? Does the "associator" (a,b,c) := (a&b)&c - a&(b&c) satisfy any identities (e.g., alternative law, Jordan identity)?

## Issues Encountered

None.

---

_Phase: 04-sequential-product-formalization, Plan: 02_
_Completed: 2026-03-21_
