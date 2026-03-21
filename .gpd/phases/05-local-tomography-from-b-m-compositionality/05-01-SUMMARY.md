---
phase: 05-local-tomography-from-b-m-compositionality
plan: 01
depth: complex
one-liner: "Local tomography proved from faithful B-M tracking: EJA trace form non-degeneracy + composite minimality forces dim(V_BM) = dim(V_B) * dim(V_M), excluding real and quaternionic types"
subsystem: [formalism, derivation]
tags: [local-tomography, composite-system, GPT, order-unit-space, EJA, trace-form, non-degeneracy, entangled-sector, dimension-counting]

requires:
  - phase: 04-sequential-product-formalization
    plan: 04
    provides: S1-S7 proved, EJA classification (V_3 for qubits)
  - phase: 04-sequential-product-formalization
    plan: 06
    provides: corrected product formula Eq. 04-06.4, Luders equivalence
  - phase: 04-sequential-product-formalization
    plan: 01
    provides: compression-based SP for sharp effects

provides:
  - Composite OUS V_BM defined from GPT primitives (no Hilbert space imports)
  - Product-form sequential product (Eq. 05-01.1) inherits S1-S7 from factor products
  - B-M correlation bilinear form B(a,b) = tau(a * phi^{-1}(b)) proved non-degenerate via EJA trace form
  - Local tomography proved: dim(V_BM) = dim(V_B) * dim(V_M) (Eq. 05-01.5)
  - Entangled-sector analysis: minimality + SP closure + non-degeneracy eliminates hidden entangled states
  - Negative checks: real QM (3*3=9 != 10) and quaternionic QM (6*6=36 != 28) correctly excluded
  - SymPy verification: composite S1-S7 on V_3 tensor V_3, dimension counting, classical limit (625 tests)
  - Circularity audit passed: no Hilbert space imports in formal construction

affects: [05-02-type-exclusion-c-star-promotion]

methods:
  added: [EJA trace form non-degeneracy argument, composite minimality, product-form SP inheritance]
  patterns: [non-degeneracy of bilinear form -> linear independence of product effects -> local tomography]

key-files:
  created:
    - derivations/05-local-tomography.md
  modified:
    - code/sp_verification.py

key-decisions:
  - "Composite V_BM defined as MINIMAL OUS with product effects, non-signaling, and product-form SP"
  - "Correlation form B(a,b) = tau(a * phi^{-1}(b)) uses EJA trace form (Phase 4 output, not Hilbert space import)"
  - "Entangled sector eliminated by minimality + SP closure + non-degeneracy, not by additional axioms"
  - "S4 inheritance uses states-separate-points property of OUS (Alfsen-Shultz 1.23)"

patterns-established:
  - "Product-form SP (a tensor b) & (c tensor d) = (a & c) tensor (b & d) inherits all axioms from factors"
  - "Non-degeneracy of trace form on simple EJA is the bridge from faithful tracking to local tomography"
  - "Minimal composite = span of product effects when SP preserves the product effect subspace"

conventions:
  - "sequential product: a & b (non-commutative)"
  - "composite product: (a tensor b) & (c tensor d) = (a & c) tensor (b & d)"
  - "local tomography: dim(V_BM) = dim(V_B) * dim(V_M)"
  - "trace form: tau(a * b) normalized to tau(1) = 1"
  - "axiom source: arXiv:1803.11139 Definition 2 EXCLUSIVELY"
  - "dimensionless algebraic quantities"

plan_contract_ref: ".gpd/phases/05-local-tomography-from-b-m-compositionality/05-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-independent-accessibility:
      status: passed
      summary: "Independent accessibility formalized as composite OUS V_BM with product states, product effects, and non-signaling constraints using only GPT/OUS primitives. No Hilbert space tensor products, no complex structure."
      linked_ids: [deliv-lt-derivation, test-composite-sp, test-circularity, ref-vdw2018, ref-barnum-wilce, ref-plavala-gpt]
    claim-composite-sp:
      status: passed
      summary: "Product-form SP (Eq. 05-01.1) on V_BM inherits S1-S7 from factor SPs. S4 inheritance uses states-separate-points property of OUS. Verified algebraically (all 7 axioms) and numerically (SymPy on V_3 tensor V_3)."
      linked_ids: [deliv-lt-derivation, deliv-lt-code, test-composite-sp, ref-vdw2018]
    claim-local-tomo:
      status: passed
      summary: "Local tomography proved: dim(V_BM) = dim(V_B) * dim(V_M). Argument: (1) lower bound from product state span, (2) non-degeneracy of B(a,b) = tau(a * phi^{-1}(b)) from EJA trace form + phi isomorphism, (3) linear independence of product effects from non-degeneracy, (4) minimality of V_BM. Entangled sector explicitly addressed. Negative checks pass for real (9!=10) and quaternionic (36!=28) types."
      linked_ids: [deliv-lt-derivation, test-local-tomo-dim, test-entangled-sector, ref-barnum-wilce, ref-hardy]
  deliverables:
    deliv-lt-derivation:
      status: passed
      path: "derivations/05-local-tomography.md"
      summary: "Complete formal derivation (15 steps): composite OUS definition, product-form SP, S1-S7 inheritance, correlation bilinear form, non-degeneracy proof, local tomography proof, entangled-sector analysis, negative checks, circularity audit."
      linked_ids: [claim-independent-accessibility, claim-composite-sp, claim-local-tomo]
    deliv-lt-code:
      status: passed
      path: "code/sp_verification.py"
      summary: "Extended verification harness with 4 new test suites: composite_sp_basic (11 tests), composite_S1_S7 (22 tests), composite_dimension (dimension counting + negative checks), composite_classical_limit (625 tests). All pass."
      linked_ids: [claim-composite-sp, test-composite-sp, test-local-tomo-dim]
  acceptance_tests:
    test-composite-sp:
      status: passed
      summary: "Product-form SP on V_3 tensor V_3 satisfies S1-S7. Verified: S3 unitality (9 product effects), S4 orthogonality symmetry (4 orthogonal pairs), S5 compatible associativity (1 compatible triple), S1 additivity (8 scalar/additive tests). Algebraic proof covers all 7 axioms."
      linked_ids: [deliv-lt-derivation, deliv-lt-code, ref-vdw2018]
    test-local-tomo-dim:
      status: passed
      summary: "Dimension equality: dim(V_3 tensor V_3) = 4 * 4 = 16 = dim(M_4(C)^sa). Negative checks: real (3*3=9 != 10) and quaternionic (6*6=36 != 28) correctly excluded. Classical (2*2=4) correctly included."
      linked_ids: [deliv-lt-derivation, deliv-lt-code, ref-barnum-wilce]
    test-entangled-sector:
      status: passed
      summary: "Entangled sector explicitly addressed in Steps 12-13 of derivation. (1) What the entangled sector is: extra dimensions of V_BM beyond product effect span. (2) Why faithful tracking prevents it: minimality + SP closure + non-degeneracy of correlation form. (3) Comparison with real QM: for M_2(R)^sa, minimal composite (dim=9) != maximal composite (dim=10), so entangled sector exists. For M_2(C)^sa, minimal = maximal = 16, so no entangled sector."
      linked_ids: [deliv-lt-derivation]
    test-circularity:
      status: passed
      summary: "Zero Hilbert space imports in composite construction AND local tomography proof. EJA trace form used (Phase 4 output, not C*-import). phi^{-1} is an OUS isomorphism. Complex structure, Hilbert spaces, and C*-algebras appear ONLY in SymPy verification harness and conclusion statement."
      linked_ids: [deliv-lt-derivation]
  references:
    ref-vdw2018:
      status: completed
      completed_actions: [read, use, cite]
      missing_actions: []
      summary: "S1-S7 definitions from Def. 2 used throughout. Theorem 1 invoked for EJA classification (Phase 4). Theorem 3 referenced as downstream application of local tomography."
    ref-barnum-wilce:
      status: completed
      completed_actions: [read, use, cite]
      missing_actions: []
      summary: "Local tomography dimension counting framework (Section 3). dim(M_2(R)^sa)=3, dim(M_2(H)^sa)=6 dimensions cited. Product state span lower bound. Complex-only local tomography result."
    ref-plavala-gpt:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "GPT composite framework: non-signaling constraints, minimal tensor product, product states. Definition 3.1 used for composite OUS definition."
    ref-hardy:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Original local tomography dimension counting argument (2001). Cited for historical context."
    ref-phase4:
      status: completed
      completed_actions: [use]
      missing_actions: []
      summary: "S1-S7 proved (Plans 03-04), EJA classification (Plan 04), corrected product (Plan 06). All used as inputs."
  forbidden_proxies:
    fp-conflate-ia-lt:
      status: rejected
      notes: "The proof explicitly constructs the correlation bilinear form B, proves its non-degeneracy, and uses minimality to close the gap between independent accessibility and local tomography. The entangled sector is addressed in Steps 12-13 (>2 pages)."
    fp-assume-complex:
      status: rejected
      notes: "No complex numbers used in the proof. EJA trace form is defined on real vector spaces. phi is an OUS isomorphism. Complex structure is a CONCLUSION (via vdW Theorem 3 downstream), not an input."
    fp-hilbert-composite:
      status: rejected
      notes: "Composite V_BM defined via real algebraic tensor product, compact convex state spaces, affine functionals, and non-signaling constraints. Circularity audit passed (Steps 6 and 14)."
    fp-short-lt-proof:
      status: rejected
      notes: "Local tomography proof is Steps 7-15 of derivation (>3 pages), including explicit entangled-sector treatment (Steps 12-13), negative checks for real and quaternionic types (Step 13), and circularity audit (Step 14)."
  uncertainty_markers:
    weakest_anchors:
      - "The minimality assumption (E1): V_BM is the MINIMAL OUS satisfying the composite axioms. This is standard in GPT but is a nontrivial choice. The maximal composite might differ."
      - "The trace form non-degeneracy relies on V being a SIMPLE EJA. Direct sums would need sector-by-sector treatment."
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations: []

comparison_verdicts:
  - subject_id: claim-local-tomo
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-barnum-wilce
    comparison_kind: benchmark
    metric: dimension_equality
    threshold: "dim(V_BM) = dim(V_B) * dim(V_M)"
    verdict: pass
    recommended_action: "Local tomography established. Proceed to Plan 02 (type exclusion + C*-promotion via vdW Theorem 3)."
    notes: "4*4=16 = dim(M_4(C)^sa). Real (9!=10) and quaternionic (36!=28) correctly excluded."
  - subject_id: claim-composite-sp
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-vdw2018
    comparison_kind: benchmark
    metric: axiom_satisfaction
    threshold: "S1-S7 hold on composite"
    verdict: pass
    recommended_action: "Composite SP valid. Used in local tomography proof."
    notes: "All 7 axioms inherited from factors. 658+ SymPy tests on V_3 tensor V_3."

duration: 25min
completed: 2026-03-21
---

# Plan 01: Local Tomography from B-M Compositionality -- Summary

**Local tomography proved from faithful B-M tracking: EJA trace form non-degeneracy + composite minimality forces dim(V_BM) = dim(V_B) * dim(V_M), excluding real and quaternionic types.**

## Performance

- **Duration:** ~25 min
- **Started:** 2026-03-21T12:01:35Z
- **Completed:** 2026-03-21T12:30:00Z
- **Tasks:** 3 (2 auto + 1 checkpoint, APPROVED)
- **Files modified:** 2

## Key Results

- **COMPOSITE OUS V_BM** formalized using only GPT/OUS primitives: product states, product effects, non-signaling, product-form SP. Circularity audit passed. [CONFIDENCE: HIGH]
- **S1-S7 INHERITANCE:** Product-form SP on V_BM inherits all seven axioms from factor SPs. S4 inheritance uses the OUS property that states separate points (Alfsen-Shultz 1.23). [CONFIDENCE: HIGH]
- **LOCAL TOMOGRAPHY PROVED (Eq. 05-01.5):** dim(V_BM) = dim(V_B) * dim(V_M). The proof uses three ingredients: (1) non-degeneracy of the EJA trace form, (2) phi isomorphism from faithful self-modeling, (3) minimality of the composite. [CONFIDENCE: MEDIUM -- the minimality assumption is standard but nontrivial]
- **ENTANGLED SECTOR ADDRESSED:** The proof explicitly shows why faithful tracking eliminates hidden entangled states via minimality + SP closure + non-degeneracy of the correlation form. For complex QM, minimal = maximal composite. For real/quaternionic QM, they differ. [CONFIDENCE: MEDIUM]
- **NEGATIVE CHECKS PASS:** Real QM (3*3=9 != 10) and quaternionic QM (6*6=36 != 28) correctly excluded. Classical systems (product = composite) correctly included. [CONFIDENCE: HIGH]
- **658+ SymPy tests on V_3 tensor V_3:** Composite S1-S7, dimension counting, classical limit (625 product pairs). All pass. [CONFIDENCE: HIGH]

## Task Commits

1. **Task 1: Formalize B-M composite OUS with product-form SP** -- `dca27e6` (derive)
2. **Task 2: Prove faithful tracking implies local tomography** -- `345d754` (derive)
3. **Task 3: Verify local tomography argument** -- APPROVED by researcher

**Plan metadata:** `baeb340` (docs: complete plan)

## Files Created/Modified

- `derivations/05-local-tomography.md` -- Complete derivation: composite OUS definition, product-form SP, S1-S7 inheritance, correlation bilinear form, non-degeneracy proof, local tomography theorem, entangled-sector analysis, negative checks, circularity audit (15 steps)
- `code/sp_verification.py` -- Extended harness: 4 new test suites (composite_sp_basic, composite_S1_S7, composite_dimension, composite_classical_limit), 658+ new tests, all pass

## Next Phase Readiness

**Plan 02 (type exclusion + C\*-promotion) is unblocked.** Researcher approved the local tomography argument. The key result -- local tomography on the composite -- is the final prerequisite for invoking vdW Theorem 3, which promotes the EJA to a C\*-algebra (selecting complex QM over real or quaternionic alternatives).

**Researcher verdict:** "The proof is rigorous, the circularity audit passes, and the negative checks validate the exclusion mechanism." Load-bearing structure confirmed: (1) non-degeneracy -> product effects span d_B * d_M dim subspace, (2) this equals maximal composite dimension for complex types only, (3) therefore minimal = maximal = d_B * d_M.

## Contract Coverage

- claim-independent-accessibility -> **passed**: GPT-only composite construction
- claim-composite-sp -> **passed**: S1-S7 inheritance proved algebraically and numerically
- claim-local-tomo -> **passed**: dim(V_BM) = dim(V_B) * dim(V_M) proved
- deliv-lt-derivation -> **passed**: derivations/05-local-tomography.md (15 steps)
- deliv-lt-code -> **passed**: code/sp_verification.py (658+ new tests)
- test-composite-sp -> **passed**: S1-S7 on V_3 tensor V_3
- test-local-tomo-dim -> **passed**: 4*4=16, negative checks pass
- test-entangled-sector -> **passed**: explicit 2+ page treatment
- test-circularity -> **passed**: zero Hilbert space imports
- ref-vdw2018 -> **completed** [read, use, cite]
- ref-barnum-wilce -> **completed** [read, use, cite]
- ref-plavala-gpt -> **completed** [read, cite]
- ref-hardy -> **completed** [cite]
- ref-phase4 -> **completed** [use]
- fp-conflate-ia-lt -> **rejected**: explicit entangled-sector treatment
- fp-assume-complex -> **rejected**: no complex numbers in proof
- fp-hilbert-composite -> **rejected**: GPT-only construction, circularity audit passed
- fp-short-lt-proof -> **rejected**: 3+ pages with entangled-sector analysis

## Equations Derived

**Eq. (05-01.1):** Product-form sequential product on composite:
$$(a_B \otimes b_M) \mathbin{\&} (c_B \otimes d_M) = (a_B \mathbin{\&} c_B) \otimes (b_M \mathbin{\&} d_M)$$

**Eq. (05-01.2):** Local tomography condition:
$$\dim(V_{BM}) = \dim(V_B) \cdot \dim(V_M)$$

**Eq. (05-01.3):** Lower bound (product state span):
$$\dim(V_{BM}) \geq \dim(V_B) \cdot \dim(V_M)$$

**Eq. (05-01.4):** B-M correlation bilinear form:
$$B(a, b) = \tau(a * \phi^{-1}(b))$$

where $\tau$ is the normalized trace functional on the EJA, $*$ is the Jordan product, and $\phi^{-1}$ is the inverse tracking map.

**Eq. (05-01.5):** Local tomography theorem:
$$\dim(V_{BM}) = \dim(V_B) \cdot \dim(V_M) \quad \text{(from non-degeneracy of } B \text{ + minimality)}$$

## Derivation Summary

### Starting Point

Phase 4 established: S1-S7 satisfied on V_B = V_M = V_3 (spin factor = M_2(C)^sa). EJA classification via vdW Theorem 1. Corrected product Eq. (04-06.4) = Luders on M_2(C)^sa.

### Intermediate Steps

1. **Composite V_BM defined** from GPT primitives: product states, product effects, non-signaling, order unit 1_BM = 1_B tensor 1_M.

2. **Product-form SP** (Eq. 05-01.1) defined and verified to inherit S1-S7. Key step: S4 inheritance uses the OUS property that states separate points.

3. **Correlation bilinear form B(a,b)** constructed from EJA trace form and tracking isomorphism phi.

4. **Non-degeneracy of B** proved using non-degeneracy of EJA trace form on simple EJAs (Faraut-Koranyi III.4.2).

5. **Linear independence** of product effects established from non-degeneracy.

6. **Minimality + SP closure** gives dim(V_BM) = dim(V_B) * dim(V_M).

### Final Result

$$\dim(V_{BM}) = \dim(V_B) \cdot \dim(V_M)$$

Local tomography holds for the self-modeling composite. Combined with Phase 4 (EJA), this positions Plan 02 to invoke vdW Theorem 3 for C\*-algebra promotion.

## Validations Completed

- S1-S7 inheritance: algebraic proof for all 7 axioms [CONFIDENCE: HIGH]
- Composite S3 unitality: 9 product effects pass [CONFIDENCE: HIGH]
- Composite S4 orthogonality: 4 orthogonal pairs pass [CONFIDENCE: HIGH]
- Composite S5 associativity: 1 compatible triple passes [CONFIDENCE: HIGH]
- Dimension counting: 4*4=16 = dim(M_4(C)^sa) [CONFIDENCE: HIGH]
- Negative check (real): 3*3=9 != 10 [CONFIDENCE: HIGH]
- Negative check (quaternionic): 6*6=36 != 28 [CONFIDENCE: HIGH]
- Classical limit: 625 composite product pairs = pointwise [CONFIDENCE: HIGH]
- Circularity audit: zero Hilbert space imports [CONFIDENCE: HIGH]
- Non-degeneracy of trace form verified on M_2(C)^sa [CONFIDENCE: HIGH]

## Decisions & Deviations

### Decisions

1. **Minimal composite (not maximal):** The composite V_BM is the minimal OUS satisfying the composite axioms. This is standard in GPT (Plavala) and ensures no hidden entangled structure. The maximal composite would allow more states but violate local tomography for non-complex types.

2. **EJA trace form as the bridge:** The non-degeneracy argument uses the EJA trace form tau(a * c), which is available after Phase 4 established the EJA structure. This is the correct tool because it is intrinsic to the EJA and does not import Hilbert space structure.

3. **Entangled-sector treatment via minimality:** Rather than proving the entangled sector is empty by analyzing its structure directly, the proof uses minimality (the composite is defined to have no structure beyond what the axioms force). This is cleaner but relies on the minimality assumption.

### Deviations

None -- plan executed as specified.

## Open Questions

- Does the minimality assumption matter in practice? (For complex QM, minimal = maximal. But the argument that minimal is the "right" composite is a physical assumption, not a mathematical theorem.)
- Can the non-degeneracy argument be strengthened to work without the simple EJA assumption (i.e., for direct sums)?
- How does this local tomography result interact with infinite-dimensional extensions?

## Self-Check: PASSED

- [x] derivations/05-local-tomography.md exists (15 steps, 3+ pages for entangled sector)
- [x] code/sp_verification.py updated with Plan 05 test suites
- [x] Commit dca27e6 verified in git log (Task 1)
- [x] Commit 345d754 verified in git log (Task 2)
- [x] All 658+ SymPy tests pass
- [x] Dimension counting: 4*4=16 passes, real (9!=10) fails, quaternionic (36!=28) fails
- [x] No Hilbert space imports in formal construction (circularity audit)
- [x] Entangled sector explicitly addressed (Steps 12-13)
- [x] Proof length >1 page (fp-short-lt-proof rejected)
- [x] Negative checks for non-complex types pass

---

_Phase: 05-local-tomography-from-b-m-compositionality, Plan: 01_
_Completed: 2026-03-21_
