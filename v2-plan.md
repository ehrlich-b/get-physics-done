# v2.0: QM from Algebraic Genericity (Sequential Product Route)

## Research Question

Does the sequential product structure of self-modeling systems satisfy
van de Wetering's axioms, thereby deriving quantum mechanics from a
single operational premise ("self-models test and update")?

## Background

The v1.0 milestone (Papers 2-4) formalized the experiential measure on
structure space. The algebraic genericity chain (L4 -> NC -> Artin-
Wedderburn -> Skolem-Noether -> Barandes -> QM) was validated across
six rounds of LLM research and two rounds of adversarial review
(research/quantum-extension/ and research/qm-genericity-review/ in
the blog repo).

The chain is airtight from Step 3 onward. The single remaining gap is
between Steps 2 and 3: why should a self-modeling system's algebra be
a C*-algebra? The C* assumption decomposes into five components:

| Component | Status |
|-----------|--------|
| Algebra (closure under +, x) | JUSTIFIED (observables compose) |
| Linearity (vector space) | JUSTIFIED (convex mixtures, Dutch books) |
| Complex field | CLOSEABLE (compositionality kills H, phase kills R) |
| **Involution (*-operation)** | **THE GAP** |
| Norm | FREE (automatic in finite dims) |

The involution is the irreducible residual. Without it, automorphisms
are GL(n,C) not U(n), and everything quantum disappears.

## The Sequential Product Route (2026-03-18 breakthrough)

Van de Wetering (2018, arXiv:1803.11139) proved:
- Theorem 1: Sequential product spaces satisfying axioms S1-S7 are
  Euclidean Jordan algebras
- Theorem 3: Jordan algebra + local tomography -> C*-algebra

A self-model does "test effect a on body, update model, test effect b."
This IS a sequential product. If this construction satisfies S1-S7, the
involution is DERIVED (emerges in the Jordan-to-C* promotion step).

## Phases

### Phase 1: Sequential Product Formalization

**Conjecture:** Self-modeling sequential products satisfy van de
Wetering's axioms S1-S7, producing a Jordan algebra.

**Tasks:**
1. Formally define a "self-modeling sequential product" on a finite-
   dimensional order unit space. The self-model has body B and model M.
   The sequential product is: "test effect a on B, update M, test b on B."
2. Verify axioms S1-S7 hold for this construction:
   - S1: Additivity in second argument (testing respects mixtures) - FREE
   - S2: Continuity in first argument (small changes, small effects) - FREE
   - S3: 1 & a = a (trivial test changes nothing) - FREE
   - S4: Symmetry of orthogonality ("a then b impossible" = "b then a
     impossible") - THIS IS THE ONE THAT MIGHT FAIL
   - S5-S7: Compatible effects compose standardly - FREE
3. If S1-S7 hold: invoke van de Wetering Theorem 1 to get Jordan algebra.
   Write up as a lemma with proof.
4. If any axiom fails: characterize exactly which axiom fails and why.
   This is a valuable negative result.

**Key references:**
- van de Wetering (2018), arXiv:1803.11139 (Theorems 1 and 3)
- Gudder-Greechie (2002), "Sequential products on effect algebras"
- Barnum-Ududec-van de Wetering (2023), arXiv:2306.00362

**Decisive output:** Proof or disproof that the self-modeling sequential
product satisfies S1-S7. If S4 fails, characterize exactly how and why.

### Phase 2: Local Tomography from B-M Compositionality

**Conjecture:** A self-model with independently accessible body B and
model M satisfies local tomography on B tensor M.

**Tasks:**
1. Formalize "independently accessible": the self-model can perform
   measurements on B alone and M alone.
2. Check whether independent accessibility implies that the joint state
   rho_BM is determined by the set of all products {Tr((a_B tensor b_M)
   rho_BM)} for effects a_B on B and b_M on M.
3. If yes: local tomography holds, invoke van de Wetering Theorem 3 to
   get C*-algebra. Write up as theorem.
4. If no: characterize what additional assumption is needed.

**Decisive output:** Proof or disproof that B-M compositionality implies
local tomography.

### Phase 3: Full Chain Paper Assembly

**Task:** Assemble the complete chain into Paper 5.

If Phases 1-2 succeed:
- L4 (premise) -> self-models test and update (operational) -> sequential
  product (van de Wetering) -> Jordan algebra (theorem) -> local
  tomography (from B-M compositionality) -> C*-algebra (theorem) -> NC
  generic (Motzkin-Taussky) -> matrix algebras (Artin-Wedderburn) ->
  unitary automorphisms (Skolem-Noether) -> quantum indivisibility
  (Barandes) -> Born rule (Gleason) -> QM.
- ONE premise (L4). Everything else is theorems or operational definitions.

If Phase 1 or 2 fails:
- Ship conditional version: L4 + C* as premises.
- Include the sequential product route as "promising but gap at [specific
  axiom]" in discussion.
- Still publishable, still novel, still fewer premises than competitors.

### Phase 4 (optional): D'Ariano Backup Route

**Conjecture:** The B-M correlation state satisfies D'Ariano's Postulate
5 (symmetric faithful state), allowing explicit involution construction.

Only run this if Phase 1 fails.

**Reference:** D'Ariano (2006), arXiv:quant-ph/0611094

## Success Criteria

- **Minimal:** Phase 1 produces a clear positive or negative result on
  S1-S7. Either closes the gap or precisely characterizes the failure.
- **Target:** Phases 1-2 succeed. Paper 5 has ONE premise.
- **Fallback:** Phase 1 or 2 fails cleanly. Ship conditional Paper 5
  (L4 + C*). Still fewer premises than all competing reconstruction
  programs.

## Key Anchors

- van de Wetering (2018), arXiv:1803.11139
- Gudder-Greechie (2002), sequential products on effect algebras
- Barnum-Ududec-van de Wetering (2023), arXiv:2306.00362
- D'Ariano (2006), arXiv:quant-ph/0611094
- Barandes (2025), stochastic-quantum bijection
- Motzkin-Taussky (1955), generic non-commutativity
- Gleason (1957), Born rule uniqueness

## What's NOT In Scope

- Standard Model derivation (Level 4+)
- Self-modeling constants experiment (Level 6)
- Experiential measure extensions (v1.0 is complete)
- The blog series (separate project)
