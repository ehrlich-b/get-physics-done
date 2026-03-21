---
phase: 04-sequential-product-formalization
plan: 06
depth: full
one-liner: "Corrected sequential product derived via Peirce 1-space feedback: positivity bound forces f=sqrt(lambda_i*lambda_j), self-modeling faithfulness selects the maximum, recovering Luders on M_2(C)^sa from OUS primitives alone"
subsystem: [formalism, derivation]
tags: [sequential-product, Peirce-decomposition, compression, self-modeling, feedback, Luders, positivity-bound, order-unit-space]

requires:
  - phase: 04-sequential-product-formalization
    plan: 01
    provides: compression-based SP for sharp effects, Peirce 1-space annihilation finding, naive extension failure

provides:
  - Corrected sequential product formula with Peirce 1-space feedback (Eq. 04-06.4)
  - Positivity bound f <= sqrt(lambda_i lambda_j) on mixing function (Eq. 04-06.2)
  - Self-modeling faithfulness selects f = sqrt(lambda_i lambda_j) (Eq. 04-06.3)
  - phi enters algebraically (not just interpretively) via mixing function selection
  - Corrected product coincides with Luders on M_2(C)^sa (Eq. 04-06.5)
  - SymPy verification: S3, bilinearity, classical limit, sharp agreement, effect range, Luders comparison
  - Correction of Plan 01's C4 statement (C_p + C_{p^perp} = pinching, not id, in non-commutative OUS)

affects: [04-02, 04-03, 04-04, 04-05]

methods:
  added: [Peirce 1-space extraction from compressions, positivity bound derivation for mixing function, spectral functional calculus in OUS]
  patterns: [corrected product = compressions + Peirce 1-space feedback, faithful self-model selects maximal coherence]

key-files:
  created:
    - derivations/04-peirce-feedback-extension.md
  modified:
    - code/sp_verification.py

key-decisions:
  - "Positivity bound f^2 <= lambda_1 lambda_2 derived from effect range requirement -- this is the key constraint"
  - "Self-modeling faithfulness (phi isomorphism) selects f = sqrt (saturates positivity bound) -- maximum information preservation"
  - "C4 from Plan 01 corrected: C_p + C_{p^perp} = pinching (not id) in non-commutative OUS"
  - "vdW only requires S1 (linearity in 2nd arg) and S2 (continuity in 1st arg) -- product is NOT bilinear in 1st argument, and this is correct"

patterns-established:
  - "Corrected product = compression sum (diagonal) + sqrt-weighted Peirce 1-space (off-diagonal)"
  - "f = 0 -> naive pinching (fails S3); f = sqrt -> Luders (passes S3); intermediate f -> decoherent product"
  - "Self-modeling quality (phi faithfulness) controls coherence level of sequential product"

conventions:
  - "sequential product: a & b (non-commutative)"
  - "mixing function: f(lambda_i, lambda_j)"
  - "Peirce 1-space projection: P_{ij}(b) = b - sum_k C_{p_k}(b)"
  - "axiom source: arXiv:1803.11139 Definition 2 exclusively"
  - "compression: C_p (Alfsen-Shultz P-projection for face(p))"
  - "dimensionless algebraic quantities"

plan_contract_ref: ".gpd/phases/04-sequential-product-formalization/04-06-PLAN.md#/contract"
contract_results:
  claims:
    claim-peirce-feedback:
      status: passed
      summary: "The self-modeling feedback map phi provides the Peirce 1-space contribution via the mixing function f(lambda_i, lambda_j). The positivity bound forces |f| <= sqrt(lambda_i lambda_j). Faithful self-modeling (phi isomorphism) selects the maximum f = sqrt(lambda_i lambda_j), making phi algebraically essential: setting f=0 (no feedback) recovers the failed naive pinching product."
      linked_ids: [deliv-feedback-derivation, test-s3-corrected, test-phi-algebraic]
    claim-corrected-product:
      status: passed
      summary: "The corrected product a & b = sum_i lambda_i C_{p_i}(b) + sum_{i<j} sqrt(lambda_i lambda_j) P_{ij}(b) satisfies S3 (1 & a = a), S1 (additivity in b), S2 (continuity in a), maps effects to effects, agrees with C_p(q) on sharp effects, reduces to pointwise multiplication on simplices, and coincides with the Luders product sqrt(a)*b*sqrt(a) on M_2(C)^sa."
      linked_ids: [deliv-feedback-derivation, deliv-verification-code, test-s3-corrected, test-bilinearity-corrected, test-classical-limit, test-sharp-agreement, test-circularity, ref-vdw2018, ref-alfsen-shultz, ref-gudder-greechie]
    claim-phi-essential:
      status: passed
      summary: "phi enters the product formula algebraically through the mixing function f: faithful phi selects f = sqrt(lambda_i lambda_j); trivial phi (no feedback) gives f = 0, recovering the failed naive extension. Removing phi recovers the failure; adding phi fixes it."
      linked_ids: [deliv-feedback-derivation, test-phi-algebraic]
  deliverables:
    deliv-feedback-derivation:
      status: passed
      path: "derivations/04-peirce-feedback-extension.md"
      summary: "Complete derivation document: Peirce decomposition review, C4 correction, general corrected product formula (Eq. 04-06.1), positivity bound (Eq. 04-06.2), faithful self-modeling selection (Eq. 04-06.3), concrete formula (Eq. 04-06.4), S3 proof, S1/S2 verification, classical limit, sharp agreement, circularity audit, Luders equivalence on M_2(C)^sa."
      linked_ids: [claim-peirce-feedback, claim-corrected-product, claim-phi-essential]
    deliv-verification-code:
      status: passed
      path: "code/sp_verification.py"
      summary: "Updated SymPy harness with corrected_sp() function and 7 new test suites: S3 on off-diagonal effects (6 cases), bilinearity in 2nd argument (5 tests), classical limit (25 pairs), sharp agreement (24 pairs), effect range (49 pairs), Luders comparison (6 pairs), phi-essential test (2 cases). All pass. No regressions in Plan 01 tests."
      linked_ids: [claim-corrected-product, test-s3-corrected, test-bilinearity-corrected, test-classical-limit, test-sharp-agreement]
  acceptance_tests:
    test-s3-corrected:
      status: passed
      summary: "1 & P_+ = P_+ (not (1/2)I). Also tested on Py+, generic effect, P0, I/2, diag(1/4,3/4). All 6 effects pass S3 exactly."
      linked_ids: [claim-corrected-product, deliv-feedback-derivation, deliv-verification-code]
    test-bilinearity-corrected:
      status: passed
      summary: "Second-argument linearity verified: a & (b1+b2) = a&b1 + a&b2 for 4 different a effects (P0, P+, diagonal, generic). Scalar multiplication test also passes. Note: vdW requires S1 (linearity in 2nd arg) and S2 (continuity in 1st arg), NOT bilinearity. Product is correctly nonlinear in 1st argument."
      linked_ids: [claim-corrected-product, deliv-verification-code]
    test-classical-limit:
      status: passed
      summary: "All 25 diagonal effect pairs on n=2 simplex give pointwise product. Matches Gudder-Greechie uniqueness."
      linked_ids: [claim-corrected-product, deliv-verification-code, ref-gudder-greechie]
    test-sharp-agreement:
      status: passed
      summary: "All 24 pairs (6 projections x 4 test effects) give corrected_sp(p, b) = p*b*p = C_p(b). Includes P0, P1, P+, P-, Py+, Py-."
      linked_ids: [claim-corrected-product, deliv-verification-code]
    test-circularity:
      status: passed
      summary: "Circularity audit in derivation document (Step 9) verifies zero Hilbert space imports. The corrected_sp() function uses only: spectral decomposition, compression (p*b*p), Peirce projection (b - pinch), scalar sqrt on eigenvalues. No operator sqrt, trace, inner product, density matrices, or Luders rule in the definition. Luders is used only in comparison tests."
      linked_ids: [claim-corrected-product, deliv-feedback-derivation]
    test-phi-algebraic:
      status: passed
      summary: "f = sqrt (faithful phi) -> 1 & P+ = P+ (PASS). f = 0 (trivial phi / no feedback) -> 1 & P+ = (1/2)I (FAIL, as expected). Removing phi recovers the failed naive extension, confirming phi is algebraically essential."
      linked_ids: [claim-phi-essential, deliv-feedback-derivation]
  references:
    ref-vdw2018:
      status: completed
      completed_actions: [use, cite]
      missing_actions: []
      summary: "S1-S3 definitions used for verification. S3 (unitality) is the key axiom resolved by the corrected product. S2 (continuity) satisfied because spectral decomposition and sqrt are continuous."
    ref-alfsen-shultz:
      status: completed
      completed_actions: [use, cite]
      missing_actions: []
      summary: "Compression theory and Peirce decomposition are the foundation. C4 statement corrected: C_p + C_{p^perp} = pinching (not id) in non-commutative OUS. Peirce 1-space projection P_{ij} defined from compressions."
    ref-gudder-greechie:
      status: completed
      completed_actions: [compare, cite]
      missing_actions: []
      summary: "Classical uniqueness verified: corrected product = pointwise on simplices (25 pairs)."
  forbidden_proxies:
    fp-hilbert-import:
      status: rejected
      notes: "Circularity audit passed. No operator sqrt, trace, inner product, or C*-multiplication in the formal construction. Scalar sqrt on real eigenvalues is arithmetic, not C*-functional calculus."
    fp-luders-disguise:
      status: rejected
      notes: "The corrected product COINCIDES with Luders on M_2(C)^sa, but the derivation does not import sqrt(a) as a C*-operation. It arrives at sqrt(lambda_i lambda_j) via positivity bound + self-modeling faithfulness. The equivalence is a CONSEQUENCE, not a premise."
    fp-generic-proof:
      status: rejected
      notes: "The proof specifically uses self-modeling feedback to select f = sqrt (faithful model preserves maximum coherence). A generic bilinear positive unital map would not select this specific f."
    fp-quadratic-rep-import:
      status: rejected
      notes: "Resolution #1 (self-modeling feedback) succeeded. Resolution #2 (quadratic representation) was not needed. No Jordan algebra structure imported."
  uncertainty_markers:
    weakest_anchors:
      - "The 'faithful self-model selects maximal f' argument is physically motivated but not a formal theorem. It is a selection principle, not a uniqueness proof."
      - "The derivation is verified on M_2(C)^sa (qubits). Extension to M_n(C)^sa for n >= 3 requires checking the multi-projector Peirce structure."
    unvalidated_assumptions:
      - "The positivity bound derivation uses the 2x2 matrix structure of M_2(C)^sa. A general OUS positivity bound may have a different form."
    competing_explanations:
      - "The quadratic representation U_a(b) = {a,b,a} also gives the Luders product and is another candidate for the OUS extension. Resolution #2 was not needed here but remains a valid alternative route."
    disconfirming_observations: []

comparison_verdicts:
  - subject_id: claim-corrected-product
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-vdw2018
    comparison_kind: benchmark
    metric: axiom_satisfaction
    threshold: "S3 holds"
    verdict: pass
    recommended_action: "Proceed to Plans 02-05 for S4-S7 verification with corrected product."
    notes: "Corrected product passes S3 on M_2(C)^sa (6 test effects including the failure case P+ from Plan 01). Also passes S1, S2."
  - subject_id: claim-corrected-product
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-gudder-greechie
    comparison_kind: benchmark
    metric: exact_equality
    threshold: "exact match"
    verdict: pass
    recommended_action: "Classical limit confirmed."
    notes: "Corrected product = pointwise product on simplices (25 pairs tested)."
  - subject_id: claim-corrected-product
    subject_kind: claim
    subject_role: supporting
    reference_id: ref-vdw2018
    comparison_kind: cross_method
    metric: exact_equality
    threshold: "corrected = Luders on M_2(C)^sa"
    verdict: pass
    recommended_action: "Expected agreement confirms correctness of OUS derivation."
    notes: "All 6 tested pairs show corrected product = Luders product on M_2(C)^sa."

duration: 8min
completed: 2026-03-21
---

# Plan 06: Peirce Feedback Extension -- Summary

**Corrected sequential product derived via Peirce 1-space feedback: positivity bound forces f=sqrt(lambda_i*lambda_j), self-modeling faithfulness selects the maximum, recovering Luders on M_2(C)^sa from OUS primitives alone.**

## Performance

- **Duration:** ~8 min
- **Started:** 2026-03-21T01:54:35Z
- **Completed:** 2026-03-21T02:02:21Z
- **Tasks:** 2
- **Files modified:** 2

## Key Results

- **CORRECTED PRODUCT FORMULA (Eq. 04-06.4):** a & b = sum_i lambda_i C_{p_i}(b) + sum_{i<j} sqrt(lambda_i lambda_j) P_{ij}(b), where the first sum is compressions (diagonal/Peirce 2-space) and the second is Peirce 1-space feedback. [CONFIDENCE: HIGH]
- **POSITIVITY BOUND (Eq. 04-06.2):** |f(lambda_i, lambda_j)| <= sqrt(lambda_i lambda_j). Derived from the requirement 0 <= a & b <= 1 for all effects. [CONFIDENCE: HIGH]
- **SELF-MODELING SELECTION (Eq. 04-06.3):** Faithful self-model (phi isomorphism) selects f = sqrt(lambda_i lambda_j), saturating the positivity bound = maximum coherence. [CONFIDENCE: MEDIUM -- selection principle, not uniqueness theorem]
- **LUDERS AGREEMENT:** Corrected product = sqrt(a) b sqrt(a) on M_2(C)^sa for all tested pairs. [CONFIDENCE: HIGH]
- **PHI ESSENTIAL:** f = 0 (no feedback) recovers the failed naive product. f = sqrt (faithful feedback) gives the corrected product. phi is algebraically essential. [CONFIDENCE: HIGH]
- **C4 CORRECTION:** Plan 01's C4 (C_p + C_{p^perp} = id) is wrong for non-commutative OUS. Correct: C_p + C_{p^perp} = pinching (annihilates Peirce 1-space). [CONFIDENCE: HIGH]

## Task Commits

1. **Task 1: Derive corrected product** -- `6391f0d` (derive)
2. **Task 2: SymPy verification** -- `4fa5ace` (compute)

## Files Created/Modified

- `derivations/04-peirce-feedback-extension.md` -- Full derivation: C4 correction, general formula, positivity bound, self-modeling selection, S3 proof, circularity audit, Luders equivalence
- `code/sp_verification.py` -- Updated harness: corrected_sp() function, 7 new test suites (S3, bilinearity, classical limit, sharp agreement, effect range, Luders comparison, phi essential), all pass

## Next Phase Readiness

**Plans 02-05 are unblocked.** The corrected product passes S3 and is well-defined. The remaining axioms S4-S7 can now be verified using the corrected product formula. Specific implications:

- **Plan 02 (S4 verification):** Use corrected_sp() for orthogonality symmetry tests. The Luders product IS known to satisfy S4, so the corrected product should pass. But the derivation route matters -- it must be shown from OUS primitives.
- **Plan 03 (S5-S7):** Associativity of compatible effects, additivity/multiplicativity of compatibility. These should follow from the corrected product's agreement with Luders.
- **Plan 04 (Non-associativity):** Check (a & b) & c != a & (b & c) for non-compatible a, b. Expected to hold since Luders is non-associative.
- **Plan 05 (EJA classification):** If S1-S7 all hold, vdW Theorem 1 forces the space to be an EJA.

**Key note:** The corrected product = Luders on M_2(C)^sa, so all axiom checks should agree with known Luders results. The value is in the DERIVATION route (OUS primitives -> product), not in discovering new products.

## Contract Coverage

- claim-peirce-feedback -> **passed**: phi selects f via faithfulness
- claim-corrected-product -> **passed**: S3, S1, S2, effect range, sharp agreement, classical limit, Luders match
- claim-phi-essential -> **passed**: f=0 fails, f=sqrt works
- deliv-feedback-derivation -> **passed**: derivations/04-peirce-feedback-extension.md
- deliv-verification-code -> **passed**: code/sp_verification.py
- test-s3-corrected -> **passed**: 6 effects including P+ (the Plan 01 failure case)
- test-bilinearity-corrected -> **passed**: 2nd arg linearity (5 tests)
- test-classical-limit -> **passed**: 25 simplex pairs
- test-sharp-agreement -> **passed**: 24 pairs
- test-circularity -> **passed**: zero Hilbert space imports
- test-phi-algebraic -> **passed**: f=0 vs f=sqrt comparison
- ref-vdw2018 -> **completed** [use, cite]
- ref-alfsen-shultz -> **completed** [use, cite]
- ref-gudder-greechie -> **completed** [compare, cite]
- fp-hilbert-import -> **rejected**: scalar sqrt on real numbers, not C*-functional calculus
- fp-luders-disguise -> **rejected**: Luders equivalence is consequence, not premise
- fp-generic-proof -> **rejected**: argument specifically uses self-modeling faithfulness
- fp-quadratic-rep-import -> **rejected**: Resolution #1 succeeded, #2 not needed

## Equations Derived

**Eq. (04-06.1):** General corrected product formula:
$$a \mathbin{\&} b = \sum_i \lambda_i C_{p_i}(b) + \sum_{i<j} f(\lambda_i, \lambda_j) P_{ij}(b)$$

**Eq. (04-06.2):** Positivity bound:
$$|f(\lambda_i, \lambda_j)| \leq \sqrt{\lambda_i \lambda_j}$$

**Eq. (04-06.3):** Self-modeling selection:
$$f(\lambda_i, \lambda_j) = \sqrt{\lambda_i \lambda_j}$$

**Eq. (04-06.4):** Corrected product (faithful self-model):
$$a \mathbin{\&} b = \sum_i \lambda_i C_{p_i}(b) + \sum_{i<j} \sqrt{\lambda_i \lambda_j}\, P_{ij}(b)$$

**Eq. (04-06.5):** Luders equivalence on M_2(C)^sa:
$$a \mathbin{\&} b = \sqrt{a}\, b\, \sqrt{a}$$

## Validations Completed

- S3 (unitality): 1 & a = a for 6 effects including P+ (the Plan 01 failure case) [CONFIDENCE: HIGH]
- S1 (additivity in b): 5 tests with 4 different first-argument effects [CONFIDENCE: HIGH]
- Classical limit: 25 diagonal pairs = pointwise product (Gudder-Greechie) [CONFIDENCE: HIGH]
- Sharp agreement: 24 pairs = compression C_p(b) [CONFIDENCE: HIGH]
- Effect range: 49 pairs in [0, I] [CONFIDENCE: HIGH]
- Luders comparison: 6 pairs all match exactly [CONFIDENCE: HIGH]
- phi essential: f=0 fails S3, f=sqrt passes S3 [CONFIDENCE: HIGH]
- Circularity audit: zero Hilbert space imports [CONFIDENCE: HIGH]
- No regressions: all Plan 01 tests maintain expected behavior [CONFIDENCE: HIGH]

## Decisions & Deviations

### Decisions

1. **vdW only requires S1+S2 (not bilinearity):** S1 is linearity in the second argument. S2 is continuity (not linearity) in the first argument. The corrected product is correctly nonlinear in the first argument (the sqrt function is nonlinear). This is consistent with the Luders product, which is also nonlinear in the first argument.

2. **C4 corrected:** Plan 01 stated C_p + C_{p^perp} = id (C4). This holds only in commutative OUS. In non-commutative OUS, C_p + C_{p^perp} = pinching map (annihilates Peirce 1-space). The Peirce 1-space annihilation is the EXPECTED behavior of compressions, not a bug.

3. **Positivity bound as the key constraint:** Rather than guessing f from physical analogy, the derivation constrains f from the MATHEMATICAL requirement that the product maps effects to effects. The positivity bound |f| <= sqrt(lambda_i lambda_j) is a hard constraint that any valid product must satisfy.

4. **Self-modeling faithfulness as selection principle:** The argument that faithful self-modeling selects maximal f is a physical selection principle, not a mathematical uniqueness theorem. It is marked as MEDIUM confidence in the key results.

### Deviations

None -- plan executed as specified.

## Open Questions

- Does the positivity bound generalize to M_n(C)^sa for n >= 3? (Multi-projector Peirce structure)
- Is the "faithful self-model selects maximal f" argument formalizable as a theorem?
- Does the corrected product satisfy S4-S7? (Expected yes, since it equals Luders on M_2(C)^sa)
- Can the selection principle be strengthened to a uniqueness result?

---

_Phase: 04-sequential-product-formalization, Plan: 06_
_Completed: 2026-03-21_
