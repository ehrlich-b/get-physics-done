# Paper 7: Chirality from Self-Modeling (Jgamma = -gammaJ)

## What this paper must prove

The last missing NCG axiom: the real structure J and the chirality
operator gamma ANTICOMMUTE. If this holds, Connes' classification
gives A_F = C + H + M_3(C) uniquely, and the spectral action gives
the full Standard Model Lagrangian + Einstein-Hilbert gravity.

## What we already have

From Paper 5 (proved, deployed):
- Self-modeling forces M_n(C)^sa with Luders sequential product
- J (conjugate transpose involution) is DERIVED
- J^2 = +1 (FORCED by involution)
- JD = DJ (self-duality commutes with dynamics - FORCED)
- Sequential product is temporally asymmetric: a . b != b . a

From Paper 6 (manuscript complete, deployed):
- GR from locality of self-modeling
- Lorentz invariance as consequence

## The candidate argument (two routes)

### Route A (direct): Forward/backward grading

1. The sequential product a . b = sqrt(a) b sqrt(a) has a temporal
   order: test a BEFORE b. Result depends on order.

2. The composite V_BM has two channels:
   - Forward: M probes B (observer acts on observed)
   - Backward: B probes M (observed acts on observer)
   These are structurally distinct (self-modeling has a preferred
   direction: M is model, B is body).

3. Define Z/2 grading gamma:
   gamma = +1 on forward channel, gamma = -1 on backward channel

4. J swaps state/effect roles (body <-> model). This maps forward
   to backward and vice versa.

5. Therefore Jgamma = -gammaJ.

### Route B (CPT theorem)

1. Unitarity from Paper 5 (C*-algebra)
2. Lorentz invariance from Paper 6
3. Luders-Pauli CPT theorem applies
4. Self-modeling breaks T (a . b != b . a, forward != backward)
5. CPT preserved + T broken => CP correlated
6. C encoded by J, P encoded by gamma => Jgamma = -gammaJ

Route B is cleaner (uses published theorem). Route A gives the
physical interpretation.

## What must be formalized (5 gaps)

1. **Define gamma algebraically on V_BM.** The "forward/backward
   channel" needs a precise algebraic definition, not narrative.
   Candidates: gamma as the grading from the tensor product structure
   H_B tensor H_M, or gamma = sigma . J where sigma is the swap.

2. **Prove gamma^2 = 1.** Must be an involution. Should follow from
   the definition (two directions only).

3. **Prove Dgamma = -gammaD.** The Dirac operator (dynamics) must
   anticommute with the grading. This is the even spectral triple
   condition. Need to show dynamics couples the two channels
   antisymmetrically.

4. **Verify Luders-Pauli applies.** The CPT theorem requires
   Lorentz-invariant unitary QFT. We have unitarity (Paper 5) and
   local Lorentz symmetry (Paper 6). But: finite-dimensional
   C*-algebra, not infinite-dimensional QFT. Does CPT hold in our
   setting? Need to either prove this or find a finite-dim analog.

5. **Identify our gamma with Connes' chirality operator.** Connes'
   gamma is the chirality operator on the fermion Hilbert space. Our
   gamma is the forward/backward grading on the self-model composite.
   Must show these are the same object.

## Structure

Phase 1: Algebraic definition of gamma on V_BM
  - Define the forward/backward decomposition precisely
  - Prove gamma^2 = 1
  - Prove Jgamma = -gammaJ from the definition

Phase 2: Dgamma = -gammaD
  - Define D from self-modeling dynamics (the Hamiltonian from Paper 6?)
  - Show D maps forward states to backward states
  - Prove the anticommutation

Phase 3: CPT route (independent verification)
  - Verify Luders-Pauli applies (finite-dim analog if needed)
  - T-violation from sequential product asymmetry
  - Derive Jgamma = -gammaJ as consequence

Phase 4: Identification with Connes
  - Show our (A, H, D, J, gamma) satisfies the axioms of a real
    spectral triple of KO-dimension 6
  - Invoke Connes' classification => A_F = C + H + M_3(C)
  - State the consequence: spectral action => SM + gravity

## Key references

- Connes 1995, "Noncommutative geometry and reality" (the axioms)
- Chamseddine-Connes 2008, "Why the Standard Model" (classification)
- Luders 1954, Pauli 1955 (CPT theorem)
- van de Wetering 2019 (sequential products -> Jordan algebras)
- Paper 5 (QM from self-modeling)
- Paper 6 (GR from self-modeling)

## Honest assessment

This is categorically harder than Papers 5-6. The QM chain is a
typicality argument (NC algebras are generic). The GR chain assembles
known results (Jacobson + area law). Paper 7 requires CHARACTERIZING
the self-modeling fixed point and showing it matches specific NCG
axioms. Gap 3 (Dgamma = -gammaD) and Gap 5 (identification with
Connes' gamma) are the hardest. Gap 4 (finite-dim CPT) may not have
a clean answer.

The paper should be honest about which gaps are closed vs open. A
paper that formalizes Route A (Jgamma = -gammaJ from forward/backward
grading) and leaves Dgamma = -gammaD as a conjecture with supporting
argument would still be publishable and valuable.
