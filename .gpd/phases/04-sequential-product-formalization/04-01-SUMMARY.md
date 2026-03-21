---
phase: 04-sequential-product-formalization
plan: 01
depth: full
one-liner: "Compression-based sequential product defined on E(B), framing resolved, but naive spectral extension fails S3 on non-commutative OUS due to Peirce 1-space annihilation"
subsystem: [formalism, derivation]
tags: [sequential-product, order-unit-space, compression, Peirce-decomposition, effect-algebra, Jordan-algebra]

requires:
  - phase: v1.0 (archived)
    provides: classical composite process framework, experiential density functional
provides:
  - Formal definition of compression-based sequential product for sharp effects (p & q = C_p(q))
  - E(B) vs E(B x M) framing resolution (E(B) selected, three failure modes exhibited for E(B x M))
  - Classical limit verification (pointwise product on simplices for n=2,3)
  - Circularity audit (zero Hilbert space imports)
  - CRITICAL FINDING -- naive spectral extension (sum lambda_i C_{p_i}(b)) fails S3 on non-commutative OUS
  - SymPy verification harness with positive/negative controls
affects: [04-02, 04-03, 04-04, 04-05]

methods:
  added: [Alfsen-Shultz compression theory, spectral decomposition in OUS, Peirce decomposition analysis]
  patterns: [compression product for sharp effects, spectral extension from sharp to general, positive/negative control testing]

key-files:
  created:
    - derivations/04-sequential-product-definition.md
    - code/sp_verification.py

key-decisions:
  - "E(B) framing selected over E(B x M) -- three failure modes exhibited for composite framing"
  - "Sequential product phi-independent at algebraic level -- tracking map is physical interpretation only"
  - "Naive spectral extension fails S3 -- Peirce 1-space annihilation discovered via SymPy verification"

patterns-established:
  - "Compression product C_p(b) = p*b*p agrees with Luders on sharp effects but decoheres general effects"
  - "Classical limit works because Peirce 1-space is trivial on simplices"

conventions:
  - "sequential product: a & b (non-commutative)"
  - "Jordan product: a * b = (1/2)(a & b + b & a)"
  - "axiom source: arXiv:1803.11139 Definition 2 exclusively"
  - "compression: C_p (Alfsen-Shultz P-projection)"
  - "dimensionless algebraic quantities"
  - "entropy base: nats"

plan_contract_ref: ".gpd/phases/04-sequential-product-formalization/04-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-sp-definition:
      status: partial
      summary: "Sequential product defined for sharp effects via compressions (p & q = C_p(q)). Well-defined and bilinear in second argument. HOWEVER, the bilinear extension to general effects via spectral decomposition fails S3 (unitality) on non-commutative OUS because the sum of compressions for a resolution of unity is the pinching map, not the identity. The Peirce 1-space (off-diagonal components) is annihilated."
      linked_ids: [deliv-sp-derivation, deliv-sp-code, test-bilinearity, test-well-defined, ref-vdw2018, ref-alfsen-shultz]
    claim-framing:
      status: passed
      summary: "E(B) framing selected. E(B x M) framing rejected with three failure modes: (1) treats B and M symmetrically, contradicting asymmetric self-modeling constraint; (2) characterizes composite B x M, not body B; (3) no natural way to encode 'test B, update M, test B' asymmetry."
      linked_ids: [deliv-sp-derivation, test-framing-resolution]
  deliverables:
    deliv-sp-derivation:
      status: partial
      path: "derivations/04-sequential-product-definition.md"
      summary: "Formal derivation document with product definition (sharp effects only), framing resolution, classical limit, circularity audit, and critical Peirce decomposition finding. Bilinearity proof for general effects is invalid due to S3 failure."
      linked_ids: [claim-sp-definition, claim-framing, test-bilinearity, test-classical-limit]
    deliv-sp-code:
      status: passed
      path: "code/sp_verification.py"
      summary: "SymPy harness with positive control (Luders, all S1-S7 pass), negative control (matrix mult, correctly fails), classical limit (n=2,3 pass), and self-model product demonstrating the Peirce decomposition failure."
      linked_ids: [claim-sp-definition, test-bilinearity, test-classical-limit, test-well-defined]
  acceptance_tests:
    test-bilinearity:
      status: failed
      summary: "Bilinearity in second argument passes (compressions are linear). Bilinearity in first argument fails when the spectral decomposition basis differs from the standard basis: (1/2)*C_{P+}(b) + (1/2)*C_{P-}(b) != C_{I/2}(b) because the decomposition into P+/P- compressions produces different diagonal blocks than the decomposition into P0/P1. Root cause: sum of compressions over a resolution of unity is basis-dependent pinching, not the identity."
      linked_ids: [claim-sp-definition, deliv-sp-code]
    test-classical-limit:
      status: passed
      summary: "Compression product equals pointwise multiplication on n=2 and n=3 simplices (all pairs tested). Matches Gudder-Greechie uniqueness: pointwise product is unique SP on simplices."
      linked_ids: [claim-sp-definition, deliv-sp-code, ref-gudder-greechie]
    test-well-defined:
      status: partial
      summary: "Effect range 0 <= a & b <= 1 passes for all 49 tested pairs on M_2(C)^sa. Unit test (1 & a = a) fails for effects with off-diagonal components (S3 failure). a & 0 = 0 passes. p & p^perp = 0 passes for all projections tested."
      linked_ids: [claim-sp-definition, deliv-sp-code]
    test-framing-resolution:
      status: passed
      summary: "E(B) framing produces well-defined product matching vdW single-system framework. E(B x M) framing exhibits three failure modes documented in derivation."
      linked_ids: [claim-framing, deliv-sp-derivation]
  references:
    ref-vdw2018:
      status: completed
      completed_actions: [read, use, cite]
      missing_actions: []
      summary: "Definition 2 (S1-S7) quoted verbatim. Corollary 7 (spectral decomposition) used for extension attempt. Theorem 1 referenced as downstream payoff."
    ref-gudder-greechie:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "Classical uniqueness result (pointwise product on simplices) verified by SymPy harness for n=2,3."
    ref-alfsen-shultz:
      status: completed
      completed_actions: [read, use]
      missing_actions: []
      summary: "Compression (P-projection) theory used as foundation. Peirce decomposition analysis revealed V_1 annihilation as root cause of S3 failure."
  forbidden_proxies:
    fp-hilbert-import:
      status: rejected
      notes: "Circularity audit passed. No sqrt, trace, inner product, density matrices, or Luders rule in the formal construction. Hilbert space structure used ONLY in the SymPy harness for concrete M_2(C)^sa examples."
    fp-quantum-check:
      status: rejected
      notes: "Self-model product explicitly distinguished from Luders product. Test harness verifies both independently. Luders is positive control only."
    fp-framing-assumption:
      status: rejected
      notes: "Both E(B) and E(B x M) framings explored. E(B) selected with documented justification. E(B x M) rejected with three exhibited failure modes."
  uncertainty_markers:
    weakest_anchors:
      - "Bilinear extension from sharp to general effects via spectral decomposition -- CONFIRMED WEAK: fails S3 due to Peirce 1-space annihilation"
    unvalidated_assumptions: []
    competing_explanations:
      - "The correct extension to general effects may require the quadratic representation U_a (which gives Luders in B(H)^sa), but this imports Jordan algebra structure"
      - "The self-modeling feedback loop may provide a natural Peirce 1-space contribution that the naive compression sum misses"
    disconfirming_observations:
      - "S3 fails: I & P+ = (1/2)I != P+ on M_2(C)^sa"
      - "Bilinearity fails: (1/2)*C_{P+}(b) + (1/2)*C_{P-}(b) != (1/2)I & b for general b"

comparison_verdicts:
  - subject_id: claim-sp-definition
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-gudder-greechie
    comparison_kind: benchmark
    metric: exact_equality
    threshold: "exact match"
    verdict: pass
    recommended_action: "Classical limit confirmed. Continue to non-commutative extension."
    notes: "Compression product equals pointwise multiplication on simplices for n=2,3."
  - subject_id: claim-sp-definition
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-vdw2018
    comparison_kind: benchmark
    metric: axiom_satisfaction
    threshold: "S3 holds"
    verdict: fail
    recommended_action: "Revise spectral extension to preserve Peirce 1-space. Explore alternatives: quadratic representation, self-modeling feedback contribution, or modified compression formula."
    notes: "Naive spectral extension sum lambda_i C_{p_i}(b) annihilates Peirce 1-space, failing S3."

duration: 30min
completed: 2026-03-21
---

# Plan 01: Sequential Product Definition -- Summary

**Compression-based sequential product defined for sharp effects on E(B); naive bilinear extension to general effects fails S3 on non-commutative OUS due to Peirce 1-space annihilation by the compression sum.**

## Performance

- **Duration:** ~30 min
- **Started:** 2026-03-21T01:27:39Z
- **Completed:** 2026-03-21T01:57:00Z
- **Tasks:** 2
- **Files modified:** 2

## Key Results

- **FRAMING RESOLVED:** E(B) framing is correct for the sequential product. E(B x M) rejected with three exhibited failure modes (symmetry, scope, operational mismatch).
- **SHARP EFFECT PRODUCT WORKS:** p & q = C_p(q) is well-defined, maps effects to effects, agrees with Luders on projections, and recovers pointwise multiplication on simplices.
- **CRITICAL FINDING:** The naive spectral extension a & b = sum lambda_i C_{p_i}(b) FAILS S3 (unitality) on non-commutative OUS. Root cause: sum of compressions for a resolution of unity is the pinching map (Peirce 2+0 projection), not the identity. The Peirce 1-space (off-diagonal/non-commutative structure) is annihilated.
- **CLASSICAL LIMIT PASSES:** On simplices (commutative OUS), the Peirce 1-space is trivial, so the compression sum IS the identity, and the product correctly gives pointwise multiplication for n=2,3.
- **CIRCULARITY AUDIT PASSED:** Zero Hilbert space imports in the formal construction.

## Task Commits

1. **Task 1: Define compression-based SP and resolve framing** -- `a2d4361` (derive)
2. **Task 2: SymPy verification harness with Peirce analysis** -- `c727d65` (compute)

## Files Created/Modified

- `derivations/04-sequential-product-definition.md` -- Formal definition, framing resolution, bilinearity analysis, classical limit, circularity audit, and Peirce decomposition addendum
- `code/sp_verification.py` -- SymPy harness: positive control (Luders), negative control (matrix mult), classical limit (n=2,3), self-model product, Peirce decomposition analysis

## Next Phase Readiness

**Plans 02-04 need re-scoping.** The naive "compression = sequential product" identification works for sharp effects but fails for general effects. Before verifying S1-S7, the extension from sharp to general effects must be revised. Three options to explore:

1. **Modified compression with Peirce 1-space contribution:** The self-modeling feedback loop B -> M -> B may naturally produce a Peirce 1-space term. The tracking map phi, which was found to be algebraically irrelevant in the naive construction, may become algebraically essential in a corrected extension.

2. **Quadratic representation:** In Jordan algebra theory, the quadratic map U_a(b) is the natural extension. In B(H)^sa, this gives Luders: U_a(b) = aba. But defining U_a requires Jordan algebra structure, which is what we are trying to derive. Check whether a subset of the quadratic representation axioms can be motivated from OUS primitives.

3. **Conditional expectation approach:** Niestegge's conditional probability mu(f|e) = mu_hat(U_e f)/mu(e) might provide a product formula that naturally preserves Peirce 1-space contributions.

## Contract Coverage

- claim-sp-definition -> **partial**: sharp effects OK, general extension fails S3
- claim-framing -> **passed**: E(B) selected with justified rejection of E(B x M)
- deliv-sp-derivation -> **partial**: document complete but bilinearity proof invalid for general effects
- deliv-sp-code -> **passed**: harness runs correctly, documents both successes and failures
- test-bilinearity -> **failed**: Peirce 1-space annihilation breaks first-argument linearity
- test-classical-limit -> **passed**: pointwise product on simplices for n=2,3
- test-well-defined -> **partial**: effect range passes, S3 fails
- test-framing-resolution -> **passed**: both framings explored, documented
- ref-vdw2018, ref-gudder-greechie, ref-alfsen-shultz -> **completed**
- fp-hilbert-import, fp-quantum-check, fp-framing-assumption -> **rejected**

## Equations Derived

**Eq. (04-01.1):** Sequential product for sharp effects

$$
p \mathbin{\&} q = C_p(q) \quad \text{(sharp effects } p, q \in \text{Proj}(B)\text{)}
$$

where C_p is the Alfsen-Shultz compression (P-projection) for face(p).

**Eq. (04-01.2):** Naive spectral extension (FAILS S3 on non-commutative OUS)

$$
a \mathbin{\&} b = \sum_i \lambda_i C_{p_i}(b) \quad \text{where } a = \sum_i \lambda_i p_i
$$

**Eq. (04-01.3):** Peirce decomposition identity showing the failure

$$
\sum_i C_{p_i}(b) = \text{pinch}_{p_1, \ldots, p_n}(b) \neq b \quad \text{(non-commutative case)}
$$

**Eq. (04-01.4):** Classical limit (PASSES)

$$
a \mathbin{\&} b = (a_1 b_1, \ldots, a_n b_n) \quad \text{(simplex case)}
$$

## Validations Completed

- Classical limit: pointwise product on n=2 and n=3 simplices (exact, all pairs) [CONFIDENCE: HIGH]
- Circularity audit: zero Hilbert space imports in formal construction [CONFIDENCE: HIGH]
- Positive control: Luders product passes all S1-S7 in SymPy harness [CONFIDENCE: HIGH]
- Negative control: matrix multiplication correctly detected as non-SP [CONFIDENCE: HIGH]
- Peirce analysis: S3 failure exhibited with explicit computation I & P+ = I/2 != P+ [CONFIDENCE: HIGH]
- Sharp effect agreement: self-model product = Luders product on all projections tested [CONFIDENCE: HIGH]

## Decisions & Deviations

### Decisions

1. **E(B) framing selected** -- vdW single-system framework matches; E(B x M) has three failure modes.
2. **phi found algebraically irrelevant** -- The sequential product C_p(q) depends only on B's compression structure. phi provides physical interpretation but does not enter the product formula.
3. **Peirce decomposition failure documented as critical finding** -- Rather than treating as a bug, this is documented as a structural insight that reshapes downstream plans.

### Deviations

**1. [Rule 5 - Physics Redirect] S3 failure of naive spectral extension**

- **Found during:** Task 2 (SymPy verification)
- **Issue:** 1 & P+ = (1/2)I != P+ on M_2(C)^sa. The naive spectral extension kills Peirce 1-space.
- **Action:** Documented the failure, analyzed root cause (Peirce decomposition), updated derivation with addendum, revised test harness to correctly report known failures.
- **Impact:** Plans 02-04 need re-scoping to address the extension problem before axiom verification.
- **Committed in:** c727d65

**Total deviations:** 1 physics redirect (Rule 5)
**Impact on plan:** Significant -- the bilinear extension from sharp to general effects must be revised. The framing resolution, classical limit, circularity audit, and sharp-effect product are all valid. Only the general-effect extension is affected.

## Open Questions

- What OUS primitive correctly extends the compression product from sharp to general effects while preserving S3?
- Does the self-modeling feedback loop (tracking map phi) provide the missing Peirce 1-space contribution, making phi algebraically essential (not just interpretive)?
- Can the quadratic representation U_a(b) be motivated from OUS primitives alone, without importing Jordan algebra structure?
- Is there a compression-based formula that preserves off-diagonal structure while remaining non-circular?

## Issues Encountered

- SymPy 1.14.0 eigenvects() returns eigenvectors in standard basis order, which is fine for this analysis but could affect numerical stability for near-degenerate eigenvalues. No issue for exact symbolic computation.

---

_Phase: 04-sequential-product-formalization_
_Completed: 2026-03-21_
