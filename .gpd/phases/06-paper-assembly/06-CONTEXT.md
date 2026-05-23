# Phase 6 Context: Paper Assembly

## Decisions (LOCKED)

### Paper Type: Full Chain (One Premise)
The derivation chain is complete. Phase 4 (S1-S7 all proved) and Phase 5 (local tomography, type exclusion, C*-promotion) both succeeded. Paper 5 presents the full chain: L4 (self-modeling) -> QM.

### Logical Chain
1. Self-modeling (the one premise) -> sequential product "test, update, test"
2. Sequential product -> S1-S7 verified (Phase 4, all proved, 186 SymPy tests)
3. S1-S7 -> Euclidean Jordan algebra (van de Wetering Theorem 1)
4. EJA + faithful tracking -> local tomography (Phase 5 Plan 01, trace form non-degeneracy + minimality)
5. EJA + local tomography -> exclude real, quaternionic, spin factors, Albert (Phase 5 Plan 02, dimension counting + BGW)
6. EJA + LT + qubit -> V = M_n(C)^sa (Barnum-Wilce theorem)
7. SP space + LT composite -> C*-algebra (vdW Theorem 3 + Hanche-Olsen)
8. M_n(C)^sa -> involution exhibited (conjugate transpose, C* identity verified)

### Key Novelty Claims
- Complex numbers are OUTPUT, never input. Circularity audit passes: no Hilbert spaces, no complex linearity, no density matrices before Step 6.
- Self-modeling feedback (phi) is proved necessary (Phase 4, Peirce 1-space gap). Without phi, S3 fails.
- One premise (self-modeling) derives everything: Jordan product, complex field, involution, local tomography.
- Every other reconstruction program either assumes the complex field, assumes C*-algebraic structure, has multiple operational axioms (5+), or doesn't derive the involution.

### Load-Bearing Assumptions (must be honestly stated)
1. Finite-dimensional spectral OUS (infinite-dimensional needs separate treatment)
2. Faithful self-modeling (phi is an isomorphism; approximate/partial self-models might give weaker structure)
3. Minimality of composite (Plan 01's upper bound uses MINIMAL composite; for complex QM, minimal = maximal, but the choice is a design decision)
4. Simple EJA (trace form non-degeneracy needs simplicity; direct sums are handled but simplicity should be flagged)

### Paper Structure
1. Premise: Finite-dimensional system that faithfully self-models
2. Construction: Sequential product from self-modeling operations
3. Result 1: S1-S7 -> EJA (Phase 4)
4. Result 2: Faithful tracking -> local tomography (Phase 5 Plan 01)
5. Result 3: LT -> complex type only (Phase 5 Plan 02)
6. Conclusion: Self-modeling implies complex quantum mechanics

### Unique Selling Point
"Self-modeling is the single operational premise from which complex quantum mechanics -- including the complex field, the involution, and local tomography -- is derived, not assumed."

### Verification Strength
- Three independent theorem chains (vdW, Barnum-Wilce, Hanche-Olsen) all converge on M_n(C)
- Negative checks work: real (9 != 10) and quaternionic (36 != 28) correctly excluded
- 186 SymPy tests (Phase 4) + 658 composite tests (Phase 5) pass

## Agent's Discretion

- Target venue selection (Foundations of Physics / PRA / NJP / other)
- Notation and presentation style choices
- Level of detail in proofs vs. proof sketches with references to Phase 4-5 derivation files
- Discussion section structure and comparison depth with other programs
- Whether to include appendices for detailed SymPy verifications

## Deferred Ideas

- Infinite-dimensional generalization
- Non-Markovian self-models
- Connection to other reconstruction programs (save for future paper)
- Blog series writeup
