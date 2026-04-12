# Paper 7: Spectral Triple from Self-Modeling

## Research Question

Does the self-modeling composite naturally carry the structure of a real
spectral triple of KO-dimension 6? Specifically: given the concrete
candidate construction below, does it satisfy all axioms required for
Connes' classification to give A_F = C + H + M_3(C)?

If yes: the spectral action gives the full Standard Model + Einstein-
Hilbert gravity. GR is free. No separate Paper 6 derivation needed.

## What we already have (from Papers 5-6, proved)

1. Self-modeling forces V = M_n(C)^sa with Luders sequential product
   a . b = sqrt(a) b sqrt(a)
2. The involution J: X -> X^dagger is DERIVED (conjugate transpose)
3. J^2 = +1 (involution)
4. The sequential product is temporally asymmetric: a . b != b . a
5. The self-modeling composite V_BM = V_B tensor V_M has diagonal U(n)
   invariance, forcing H = J*SWAP (Heisenberg model) via Schur-Weyl
6. The SWAP operator P decomposes C^n tensor C^n into Sym^2(C^n) (P=+1)
   and wedge^2(C^n) (P=-1)

## The concrete candidate construction

### Hilbert space (doubled)

  H = (C^n tensor C^n)_particle  direct-sum  (C^n tensor C^n)_antiparticle

Elements are pairs (psi, chi) with psi in the "particle" sector (B is
body, M is model) and chi in the "antiparticle" sector (M is body, B is
model). The doubling is natural: the self-modeling composite has two
subsystems, and either can play the "observer" role. This parallels
Connes' particle/antiparticle doubling.

dim(H) = 2n^2 per site (total: 2 * n^2).

### J (real structure / charge conjugation)

  J(psi, chi) = (PC chi-bar, PC psi-bar)

where P is the SWAP operator P|i>|j> = |j>|i>, C is complex conjugation
in the computational basis (psi-bar), and the composition PC swaps
tensor factors and conjugates. J is antilinear.

Properties:
- J^2 = 1 (verified: (PC)^2 = P^2 C^2 = I since PC = CP)
- J maps the particle sector to the antiparticle sector (swaps body/model)

Physical meaning: J swaps which subsystem is the observer and which is
the observed. This is charge conjugation (particle <-> antiparticle).

### gamma (chirality / Z/2 grading)

  gamma(psi, chi) = (P psi, -P chi)

where P is the SWAP operator (same P as in J and in the Hamiltonian).

Properties:
- gamma^2 = 1 (verified: P^2 = I, (-1)^2 = 1)
- gamma is self-adjoint (P is self-adjoint)
- Eigenvalues: +1 on Sym^2-particle and wedge^2-antiparticle,
               -1 on wedge^2-particle and Sym^2-antiparticle

### VERIFIED: J gamma = -gamma J

Computation:
  J gamma (psi, chi)  = J(P psi, -P chi)
                       = (PC(-P chi-bar), PC(P psi-bar))
                       = (-PCP chi-bar, PCP psi-bar)
                       = (-C chi-bar, C psi-bar)
  [using PCP = C since PC = CP and P^2 = I, so PCP = P(CP) = P(PC) = P^2 C = C]

  gamma J (psi, chi)  = gamma(PC chi-bar, PC psi-bar)
                       = (P PC chi-bar, -P PC psi-bar)
                       = (P^2 C chi-bar, -P^2 C psi-bar)
                       = (C chi-bar, -C psi-bar)

  Therefore: J gamma = -gamma J.  QED.

### Eigenvalue pattern matches Connes exactly

| Sector             | P eigenvalue | Matter sign | gamma | Connes SM analog           |
|--------------------|-------------|-------------|-------|----------------------------|
| wedge^2-particle   | -1          | +1          | -1    | H_L (left-handed particle) |
| Sym^2-particle     | +1          | +1          | +1    | H_R (right-handed particle)|
| wedge^2-antipart.  | -1          | -1          | +1    | H_L^c (left-handed anti.)  |
| Sym^2-antipart.    | +1          | -1          | -1    | H_R^c (right-handed anti.) |

This is the EXACT eigenvalue pattern of Connes' gamma_F in the Standard
Model spectral triple (cf. Boeijink-van den Dungen arXiv:1605.03231,
Eq. 3.30; Chamseddine-Connes arXiv:0706.3688).

### Physical interpretation

- P (SWAP) distinguishes exchange-symmetric (bosonic, Sym^2) from
  exchange-antisymmetric (fermionic, wedge^2) states. This is the
  "chirality" of the self-modeling composite: fermionic states are
  sensitive to the temporal ordering of the sequential product,
  bosonic states are not.

- The sign flip between particle/antiparticle sectors: when you swap
  which subsystem is the observer (J), the "directed chirality" — how
  exchange symmetry relates to the observer's perspective — reverses.
  "Forward" for B-as-observer is "backward" for M-as-observer.

- gamma = P * (matter sign) correlates exchange symmetry type with the
  observer assignment. J flips the observer assignment, flipping gamma.
  This is exactly how charge conjugation maps left-handed particles to
  right-handed antiparticles in the Standard Model.

## What must be proved (4 phases)

### Phase 1: Axiom verification for the spectral triple

Given (A, H, D, J, gamma) with A = M_n(C) acting on the doubled H above,
verify ALL axioms of a real spectral triple of KO-dimension 6.

**KO-dimension 6 sign relations:**
- J^2 = +1 (epsilon = +1)  — VERIFIED above
- JD = +DJ (epsilon' = +1) — DEPENDS ON D (Phase 2)
- J gamma = -gamma J (epsilon'' = -1) — VERIFIED above

**Order zero condition:** [a, Jb*J^{-1}] = 0 for all a, b in A.

This says: the left action of A commutes with the J-conjugated right
action. Compute Jb*J^{-1} explicitly for our J and check commutativity.

The algebra A = M_n(C) acts on H by:
  pi(a)(psi, chi) = ((a tensor 1)psi, (a tensor 1)chi)

The opposite algebra action is:
  pi_o(b) = Jb*J^{-1}

Compute this explicitly and verify [pi(a), pi_o(b)] = 0.

**Tasks:**
1. Compute pi_o(b) = Jb*J^{-1} explicitly for our J
2. Verify the order zero condition
3. If it fails: diagnose why and determine if the algebra action needs
   modification (e.g., A acts differently on particle vs antiparticle
   sectors, as in Connes' framework)

### Phase 2: Construct D with D gamma = -gamma D

The Dirac operator D must satisfy:
1. D is self-adjoint on H
2. D gamma = -gamma D (D anticommutes with chirality)
3. JD = DJ (D commutes with J, for KO-dim 6)
4. [D, a] is bounded for all a in A (first-order differential operator)

The condition D gamma = -gamma D means D maps between chirality sectors:
- D: Sym^2 <-> wedge^2 (within each matter sector)
- D: maps exchange-symmetric states to exchange-antisymmetric states

The Hamiltonian H = J*SWAP COMMUTES with P (it is diagonal in the SWAP
eigenbasis), so H is NOT D. D must be an operator that breaks the SWAP
symmetry — the self-modeling analog of Yukawa couplings.

**Candidate construction for D:**

Consider what operators on C^n tensor C^n map between Sym^2 and wedge^2.
Any operator that is NOT diagonal in the SWAP eigenbasis will do this.
The question is which one is natural from self-modeling.

Key observation: the sequential product a . b = sqrt(a) b sqrt(a), when
viewed as a linear map L_a: b -> a . b, is NOT symmetric under SWAP
(because a . b != b . a). The difference L_a - R_a (where R_a: b -> b . a)
maps between the symmetric and antisymmetric parts of the product. This
antisymmetric part of the sequential product is a natural candidate for D.

More specifically: on V_BM = V_B tensor V_M, define for a fixed reference
state omega:

  D_omega = sum_a [L_{a tensor 1} - R_{a tensor 1}]

or some natural contraction of the sequential product's asymmetry.

**Tasks:**
1. Identify the most natural self-modeling operator that maps Sym^2 <-> wedge^2
2. Check D gamma = -gamma D
3. Check JD = DJ
4. Check [D, a] is bounded (automatic in finite dims)
5. If no natural candidate works, determine what additional structure
   from self-modeling constrains D

### Phase 3: First-order condition and subalgebra

The first-order condition: [[D, a], Jb*J^{-1}] = 0 for all a, b in A.

In Connes' SM, this condition is what forces the subalgebra. Starting
from the "initial" algebra M_a(H) + M_{2a}(C), the first-order condition
on D restricts to A_F = C + H + M_3(C) for a = 2.

**Tasks:**
1. With D from Phase 2, compute [D, a] for general a in A
2. Check the first-order condition [[D, a], Jb*J^{-1}] = 0
3. If it fails for general a: determine the subalgebra A_F subset A
   for which it holds
4. Compare A_F to the SM algebra C + H + M_3(C)
5. Determine what value of n is required (conjecture: n = 4, since
   the SM spectral triple has H_F = C^{16} per generation = C^{4^2})

### Phase 4: Classification and spectral action

If Phases 1-3 succeed:
1. Verify ALL axioms of a real spectral triple (KO-dim 6) are satisfied
2. Invoke the Chamseddine-Connes classification theorem
3. Identify A_F and compare to C + H + M_3(C)
4. State the spectral action consequences:
   - Einstein-Hilbert term (from Lambda^2 coefficient in heat kernel)
   - Yang-Mills for U(1) x SU(2) x SU(3)
   - Higgs potential
   - Yukawa couplings
5. List what is forced vs what remains as input (cosmological constant,
   coupling constants, masses)

## Success criteria

**STRONG SUCCESS (Paper 7 complete):**
All 4 phases succeed. The self-modeling composite carries a natural real
spectral triple of KO-dimension 6. The classification gives A_F = C + H + M_3(C).
GR + SM from spectral action. Paper 6 becomes supporting UV evidence.

**MEDIUM SUCCESS (partial result, still publishable):**
Phases 1-2 succeed but Phase 3 gives a different A_F, or the first-order
condition requires additional input. Still proves self-modeling gives a
KO-dim 6 spectral triple. The specific subalgebra depends on D.

**INFORMATIVE FAILURE:**
Phase 1 fails (order zero condition violated). This means the algebra
action needs modification. Diagnose: what algebra action IS compatible?
This constrains the framework.

Phase 2 fails (no natural D with D gamma = -gamma D and JD = DJ). This
means the construction gives KO-dim 6 signs for J and gamma but no
compatible Dirac operator. Diagnose: what constraints on D emerge?

**DEFINITIVE FAILURE:**
The construction is inconsistent (gamma^2 != 1 or J gamma != -gamma J in
some regime we missed). This would kill the approach. But the algebraic
verification above makes this unlikely.

## Deliverables

For each phase:
1. A proof document (derivations/07-{phase-name}.md)
2. SymPy verification code where applicable (code/spectral_triple_verification.py)
3. Clear statement of what is proved, what is assumed, what fails

## Key references

- Connes 1995, "Noncommutative geometry and reality" (axioms)
- Chamseddine-Connes 2008, "Why the Standard Model" (arXiv:0706.3688)
- Connes 2006, "NCG and the SM with neutrino mixing" (arXiv:hep-th/0608226)
- Boeijink-van den Dungen 2016 (arXiv:1605.03231, explicit gamma_F)
- van Suijlekom 2024, "NCG and Particle Physics" 2nd ed (textbook)
- van de Wetering 2019 (sequential products -> Jordan algebras)
- Paper 5: QM from self-modeling (the source of J, sequential product)
- Paper 6: spacetime from self-modeling (SWAP, Schur-Weyl, lattice)

## What this prompt supersedes

This replaces paper7-chirality-prompt.md. The old prompt had the right
target (J gamma = -gamma J) but lacked a concrete construction. This
prompt provides the explicit (H, J, gamma) with the anticommutation
already verified, and focuses GPD on the remaining gaps: the algebra
action (order zero), D (the Dirac operator), and the first-order
condition that forces the subalgebra.
