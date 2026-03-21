# Phase 4: Sequential Product Formalization - Context

**Gathered:** 2026-03-20
**Status:** Ready for planning

<domain>
## Phase Boundary

Prove or disprove that the self-modeling "test-update-test" cycle defines a sequential product on a finite-dimensional order unit space satisfying van de Wetering's axioms S1-S7, and classify the resulting algebraic structure. The sequential product is defined via Alfsen-Shultz compressions, parametrized by a tracking map phi.

Requirements: SPFM-01, SPFM-02, SPFM-03, SPFM-04, SPFM-05

</domain>

<contract_coverage>
## Contract Coverage

- **Sequential product definition:** Compression-based bilinear map a . b = C_a(b) on the effect space of a finite-dimensional OUS, with the self-modeling constraint formalized as "B's compressions induce corresponding compressions on M via phi"
- **Acceptance signal:** Each of S1-S7 individually proved or disproved with formal argument pinned to arXiv:1803.11139 definitions verbatim; non-associativity exhibited with explicit triple
- **False progress to reject:** Axiom checks that paraphrase vdW definitions or substitute Gudder-Greechie axioms; proofs that import Hilbert space structure; checking axioms for quantum sequential products instead of the self-modeling construction

</contract_coverage>

<user_guidance>
## User Guidance To Preserve

- **User-stated observables:** Whether each of S1-S7 holds for the self-modeling sequential product; which effect algebra framing is correct; whether S4 requires phi to preserve orthogonality or holds unconditionally
- **User-stated deliverables:** Formal definition of the compression-based sequential product parametrized by phi; proof/disproof of each axiom; non-associativity verification; EJA classification (if S1-S7 hold)
- **Must-have references / prior outputs:** van de Wetering arXiv:1803.11139 (Theorems 1 and 3 -- axiom definitions AND C*-promotion result); Gudder-Greechie (2002) for comparison only; v1.0 composite process framework (classical limit check); ~/repos/blog/research/quantum-extension/draft.md
- **Stop / rethink conditions:**
  - Bilinearity fails (extending compressions to bilinear product on general effects): STOP immediately, redesign construction
  - S4 fails for isometric phi (dim M >= dim B): STOP immediately, discuss D'Ariano backup or construction rethink
  - S4 holds even under coarse-graining (dim M < dim B): FLAG as suspicious -- try more diverse examples before escalating; check for circularity
  - Non-associativity fails (product is associative): STOP, sequential product route is dead

</user_guidance>

<decisions>
## Methodological Decisions

### Update Map Construction

- **Compression-based:** The sequential product is a . b = C_a(b) where C_a is the Alfsen-Shultz compression (P-projection) for face(a). This is the native OUS primitive for measurement update -- exists for any finite-dimensional order unit space without Hilbert space imports.
- **Self-modeling constraint:** B's compressions induce corresponding compressions on M. Formally: there exists a positive unital compression-preserving map phi: E(B) -> E(M) such that testing effect a on B triggers compression C_{phi(a)} on M.
- **Parametrize by phi:** The sequential product is defined for a class of valid tracking maps phi. Do NOT try to pin phi down uniquely. Let the axiom verification reveal what phi needs to be. Three possible outcomes:
  - S1-S7 hold for ALL valid phi: self-modeling alone suffices
  - S1-S7 hold only for phi satisfying additional constraint (e.g., orthogonality preservation): that constraint becomes part of the assumption, needs physical justification
  - S1-S7 fail for ALL valid phi: clean negative result
- **Sharp effects first:** Compressions for sharp effects (projective units/faces) are guaranteed. Extension to fuzzy effects via spectral decomposition comes later.
- **Bilinearity is the first gate:** If extending C_a(b) to a bilinear map on the full effect space fails, the approach is fundamentally wrong. Check this BEFORE any axiom verification.

### Classical Recovery

- **Hard constraint, not sanity check:** When B is a simplex (classical system), the compression-based sequential product MUST reduce to pointwise multiplication a . b = a * b. This is the unique sequential product satisfying S1-S7 on a simplex (Gudder-Greechie).
- **Verification sequence:** Define the construction, verify classical recovery on simplices, THEN extend to non-classical state spaces.
- **Constrains phi:** In the classical case, phi is a coarse-graining of B's state space. Induced compressions on M must be consistent with classical conditional probabilities.

### Axiom Source

- **arXiv:1803.11139 EXCLUSIVELY** for all axiom definitions. Fetch the paper and quote definitions verbatim before any verification. No working from memory or paraphrase. No Gudder-Greechie substitution (their axioms are on effect algebras specifically; vdW works on order unit spaces more generally).
- **Both Theorems 1 and 3 in view:** Theorem 1 (S1-S7 -> Jordan algebra) defines the immediate target. Theorem 3 (Jordan + local tomography -> C*-algebra) defines the downstream target. S4 verification must not introduce assumptions that conflict with the local tomography step.

### Agent's Discretion

- Specific form of the bilinear extension from sharp to general effects (spectral theorem approach vs other methods)
- Whether to work in Schrodinger (state) or Heisenberg (effect) picture for intermediate calculations, as long as compressions are the foundational object
- Level of detail in documenting intermediate algebra
- Whether to use symbolic computation (SymPy) or pen-and-paper style for the low-dimensional examples

</decisions>

<assumptions>
## Physical Assumptions

- Compressions are the correct OUS analogue of measurement update: Justified by Alfsen-Shultz theory; compressions act on effects natively (Heisenberg picture), matching vdW's framework | Breaks if the self-modeling update has structure that compressions cannot capture (e.g., requires non-idempotent maps)
- The self-modeling feedback loop B -> M -> B is invariant under automorphisms of M: Justified as gauge freedom (relabeling M's internal structure) | Breaks if the sequential product on B depends on the internal structure of M beyond its compression action
- Finite-dimensional order unit spaces have sufficient face structure for the construction: Justified by Alfsen-Shultz structure theory in finite dimensions | Would break in infinite dimensions where face structure is more subtle

</assumptions>

<limiting_cases>
## Expected Limiting Behaviors

- When B is a simplex (classical): a . b must reduce to pointwise multiplication a * b
- When phi is the identity (M copies B exactly): S4 should hold (user's primary prediction)
- When phi is a coarse-graining (dim M < dim B): S4 may fail -- this is the decisive test distinguishing "bare tracking" from "faithful tracking"
- When alpha -> infinity in the original framework (short-range limit): should be consistent with standard BKT-type sequential product structure (not directly applicable but consistency required)

</limiting_cases>

<anchor_registry>
## Active Anchor Registry

- **ref-vdw2018:** van de Wetering, arXiv:1803.11139 -- Sequential product spaces are Jordan algebras
  - Why it matters: Theorems 1 and 3 are the axiom source and the chain endpoint; definitions must be quoted verbatim
  - Carry forward: planning, execution, verification, writing
  - Required action: read (fetch paper), use, cite

- **ref-gudder-greechie:** Gudder, Greechie (2002) -- Sequential products on effect algebras
  - Why it matters: Classical uniqueness result (pointwise multiplication is the unique SP on simplices); comparison reference only, NOT axiom source
  - Carry forward: planning, execution, writing
  - Required action: read, cite (for classical uniqueness)

- **ref-alfsen-shultz:** Alfsen, Shultz -- Geometry of State Spaces of Operator Algebras
  - Why it matters: Compression (P-projection) theory is the foundation of the construction
  - Carry forward: planning, execution
  - Required action: read, use

- **v1.0 composite process framework**
  - Why it matters: Classical limit consistency check; the compression-based construction must reduce to v1.0's factorization condition on simplices
  - Carry forward: verification
  - Required action: compare (classical limit only)

- **~/repos/blog/research/quantum-extension/draft.md**
  - Why it matters: Contains the algebraic genericity chain and motivates the sequential product route; the "gap" this phase closes
  - Carry forward: planning, writing
  - Required action: read

</anchor_registry>

<skeptical_review>
## Skeptical Review

- **Weakest anchor:** The assumption that compressions extend to a bilinear product on general (fuzzy) effects. Sharp effects have guaranteed compressions, but bilinear extension to the full effect space is the untested step.
- **Unvalidated assumptions:** (1) That the self-modeling feedback loop B -> M -> B has enough structure to force S4 when phi is isometric; (2) That the compression-based product is the "right" formalization of test-update-test, rather than some other OUS primitive
- **Competing explanation:** The involution might genuinely require an independent physical postulate (C*-axiom) that cannot be derived from self-modeling. Many reconstruction programs assume it.
- **Disconfirming check:** S4 fails for isometric phi in the qubit case (2x2 matrices, phi = identity). This is checkable exhaustively for all sharp effect pairs and would kill the approach decisively.
- **False progress to reject:** S4 "holding" because the example is too symmetric (e.g., only testing effects aligned with a preferred basis); axiom checks that use Hilbert space trace or inner product structure disguised as OUS operations

</skeptical_review>

<deferred>
## Deferred Ideas

None -- discussion stayed within phase scope

</deferred>

---

_Phase: 04-sequential-product-formalization_
_Context gathered: 2026-03-20_
