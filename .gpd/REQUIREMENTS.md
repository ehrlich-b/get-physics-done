# Requirements: Spectral Triple from Self-Modeling

**Defined:** 2026-03-22
**Core Research Question:** Does the self-modeling composite carry a real spectral triple of KO-dimension 6, giving A_F = C + H + M_3(C) (Standard Model)?

## Primary Requirements

### Axiom Verification

- [ ] **AXVM-01**: Compute pi_o(b) = Jb*J^{-1} explicitly for general n and verify order zero condition [pi(a), pi_o(b)] = 0 for all a, b in M_n(C), with SymPy verification at n=2,3,4
- [ ] **AXVM-02**: Check orientability condition (gamma = pi(c) J pi(c') J^{-1} for some Hochschild cycle); document expected failure per Barrett 2007 / Stephan 2006 precedent
- [ ] **AXVM-03**: Verify Poincare duality (intersection form non-degenerate) for the candidate spectral triple
- [ ] **AXVM-04**: Resolve dimension counting: how does dim(H) = 2n^2 map to the CCM classification's k^2 per generation; determine which n (if any) is compatible with SM particle content

### Dirac Operator Construction

- [ ] **DIRC-01**: Parameterize all self-adjoint D satisfying D gamma = -gamma D and JD = DJ on the doubled Hilbert space H = C^{2n^2} (the D moduli space)
- [ ] **DIRC-02**: Construct the sequential product asymmetry operator (L_a - R_a or natural contraction thereof) and determine whether it lies in the D moduli space
- [ ] **DIRC-03**: If sequential product candidate fails JD = DJ or D gamma = -gamma D, identify which D in the moduli space is most naturally motivated from self-modeling structure

### First-Order Condition and Subalgebra

- [ ] **FRST-01**: Compute [[D, a], Jb*J^{-1}] for general a, b in A = M_n(C) and identify the maximal subalgebra A_F where it vanishes, for the D from Phase 2
- [ ] **FRST-02**: Evaluate A_F at n=2, 3, 4 and compare to C + H + M_3(C) (Standard Model algebra)
- [ ] **FRST-03**: If A_F differs from SM algebra, characterize the resulting gauge group (Pati-Salam fallback per Chamseddine-Connes-van Suijlekom 2013)

### Computational Verification

- [ ] **COMP-01**: SymPy verification pipeline at n=2 (8x8 matrices): order zero, D moduli space, first-order condition
- [ ] **COMP-02**: Extend SymPy verification to n=3 (18x18) and n=4 (32x32)

### Paper Assembly

- [ ] **PAPR-01**: Paper 7 "Spectral Triple from Self-Modeling" with complete derivation chain, honest gap identification, and tiered success statement (strong/medium/informative failure)

## Follow-up Requirements

### Extended Analysis

- **EXTN-01**: Investigate Boyle-Farnsworth Jordan geometry (arXiv:1910.11888, 2206.07039) as alternative framework if C*-algebraic route encounters obstruction
- **EXTN-02**: Full spectral action computation (coupling constants, Higgs potential, Yukawa terms) if spectral triple is established
- **EXTN-03**: Connection between Paper 6 (Jacobson/Lovelock GR) and Paper 7 (spectral action GR) -- are they consistent?

## Out of Scope

| Topic | Reason |
| ----- | ------ |
| Full spectral action computation | Requires established spectral triple first; separate paper |
| Phenomenological predictions (masses, mixing angles) | Requires spectral action; well beyond current scope |
| Lorentzian spectral triples | Active research area; Euclidean signature sufficient for classification |
| Infinite-dimensional spectral triples | Paper 5 restriction to finite dimensions carries forward |
| Generations (why 3 families) | Separate question from algebra identification |

## Accuracy and Validation Criteria

| Requirement | Accuracy Target | Validation Method |
| ----------- | --------------- | ----------------- |
| AXVM-01 | Exact algebraic proof | SymPy verification at n=2,3,4 |
| AXVM-02 | Exact (pass/fail) | Explicit Hochschild cycle search or proof of non-existence |
| AXVM-04 | Exact dimension match | Compare 2n^2 to CCM classification tables |
| DIRC-01 | Complete parameterization | Dimension count of moduli space matches independent calculation |
| DIRC-02 | Exact (in moduli space or not) | SymPy check of all three conditions |
| FRST-01 | Exact subalgebra identification | SymPy null space computation at specific n |
| FRST-02 | Exact algebra comparison | Isomorphism check against C + H + M_3(C) |
| COMP-01 | Zero tolerance (exact algebra) | All commutator/anticommutator identities vanish exactly |

## Contract Coverage

| Requirement | Decisive Output | Anchor / Reference | Prior Inputs | False Progress To Reject |
| ----------- | --------------- | ------------------ | ------------ | ------------------------ |
| AXVM-01 | Proof + SymPy verification that [pi(a), pi_o(b)] = 0 | Connes 1995 axioms; van Suijlekom 2024 Ch. 3 | J from Paper 5, SWAP from Paper 6 | Checking only for specific a,b instead of all |
| AXVM-04 | Explicit mapping of 2n^2 to CCM counting | Chamseddine-Connes 2008 classification | Paper 5 dim counting | Ignoring generation structure |
| DIRC-02 | Sequential product asymmetry operator tested against all 3 conditions | Barrett 2015 matrix geometries | Sequential product from Paper 5 | Constructing ad hoc D without self-modeling motivation |
| FRST-01 | Identified subalgebra A_F with proof | CCM 2008 first-order condition | D from Phase 2, pi_o from Phase 1 | Assuming A_F without computing first-order condition |
| FRST-02 | Comparison A_F vs C + H + M_3(C) | Standard Model algebra | A_F from FRST-01 | Claiming SM match without checking all factors |
| PAPR-01 | Paper 7 with honest gaps | Papers 5-6, CCM classification | All prior phases | Overclaiming (SM "derived") when conditions assumed |

## Traceability

| Requirement | Phase | Status |
| ----------- | ----- | ------ |
| AXVM-01 | -- | Pending |
| AXVM-02 | -- | Pending |
| AXVM-03 | -- | Pending |
| AXVM-04 | -- | Pending |
| DIRC-01 | -- | Pending |
| DIRC-02 | -- | Pending |
| DIRC-03 | -- | Pending |
| FRST-01 | -- | Pending |
| FRST-02 | -- | Pending |
| FRST-03 | -- | Pending |
| COMP-01 | -- | Pending |
| COMP-02 | -- | Pending |
| PAPR-01 | -- | Pending |

**Coverage:**

- Primary requirements: 13 total
- Mapped to phases: 0 (pending roadmap)
- Unmapped: 13

---

_Requirements defined: 2026-03-22_
_Last updated: 2026-03-22 after initial definition_
