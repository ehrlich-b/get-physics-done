# Prior Work: Spectral Triples from Self-Modeling and the Noncommutative Standard Model

**Surveyed:** 2026-03-22
**Domain:** Noncommutative geometry / Spectral triples / Particle physics from NCG / Jordan algebras
**Confidence:** MEDIUM-HIGH

This document covers prior work relevant to determining whether the self-modeling composite carries a real spectral triple of KO-dimension 6 and whether Connes' classification gives the Standard Model algebra A_F = C + H + M_3(C). It does NOT re-cover the v2.0 results (self-modeling -> M_n(C)^sa) or v3.0 results (locality -> Einstein's equations), which are validated and complete.

---

## Key Results

| Result | Expression / Value | Conditions | Source | Year | Confidence |
|--------|-------------------|------------|--------|------|------------|
| KO-dim 6 sign relations | J^2 = +1, JD = +DJ, J gamma = -gamma J | Real spectral triple, even, KO-dimension 6 mod 8 | Connes, J. Math. Phys. 36, 6194 | 1995 | HIGH |
| Classification of irreducible finite KO-dim 6 geometries | dim(H_F) = k^2 per generation; quaternion linearity singles out k=4 giving A_F = C + H + M_3(C) | Irreducible, KO-dim 6, first-order condition, massless graviton constraint, Poincare duality | Chamseddine-Connes-Marcolli, arXiv:0706.3688 | 2007 | HIGH |
| Spectral action gives SM + gravity | Tr(chi(D/Lambda)) + (psi, D psi) = Einstein-Hilbert + Yang-Mills + Higgs + fermion terms | Almost-commutative geometry M x F, A_F = C + H + M_3(C), asymptotic expansion | Chamseddine-Connes, hep-th/9606001 | 1996 | HIGH |
| Finite space resolves fermion doubling | Changing grading on antiparticle sector (KO-dim 6 not 0) eliminates fermion doubling | Metric dimension 0, KO-dimension 6 for F | Connes, hep-th/0608226 | 2006 | HIGH |
| First-order condition can be relaxed | Inner fluctuations acquire quadratic term; leads to Pati-Salam SU(2)_R x SU(2)_L x SU(4) | Spectral triple without first-order condition | Chamseddine-Connes-van Suijlekom, arXiv:1304.7583 | 2013 | HIGH |
| Krajewski diagram classification | Finite real spectral triples classified by decorated graphs (Krajewski diagrams) | Finite-dimensional algebra, even spectral triple | Krajewski, hep-th/9701081 | 1997 | HIGH |
| Jordan geometry reproduces SM | Jordan algebra approach: coordinate algebra is Jordan, not associative; gauge fields automatically unimodular | Replaces associative algebra axiom with Jordan algebra | Boyle-Farnsworth, arXiv:1910.11888 | 2019 | MEDIUM |
| Exceptional Jordan algebra and SM gauge group | Aut(H_3(O)) = F_4; intersection Spin(9) cap subgroup of F_4 = G_SM | Exceptional Jordan algebra H_3(O), 27-dimensional | Dubois-Violette-Todorov, arXiv:1805.06739 | 2018 | MEDIUM |
| Jordan algebras define spectral triples | Spectral triples built from special Jordan backgrounds; gauge-invariant bosonic configuration spaces | Jordan coordinate algebras, not C*-algebras | Farnsworth, arXiv:2206.07039 | 2022 | MEDIUM |
| Matrix geometries as finite spectral triples | General form of Dirac operator for finite spectral triples with A = M_n(C) | Finite-dimensional Hilbert space, real spectral triple | Barrett, arXiv:1502.05383 | 2015 | HIGH |
| Operator systems generalize spectral triples | Spectral truncations use operator systems (Jordan-like) in place of C*-algebras | Truncated spectral triples | Connes-van Suijlekom, arXiv:2004.14115 | 2020 | MEDIUM |

---

## Foundational Work

### Connes (1995) - Noncommutative Geometry and Reality

**Key contribution:** Defined the axioms of a real spectral triple and classified them by KO-dimension mod 8 using the signs (epsilon, epsilon', epsilon'') of the relations J^2 = epsilon, JD = epsilon' DJ, J gamma = epsilon'' gamma J.

**The KO-dimension sign table** (established, textbook-level, HIGH confidence):

| KO-dim | epsilon (J^2) | epsilon' (JD) | epsilon'' (J gamma) |
|--------|--------------|---------------|-------------------|
| 0 | +1 | +1 | +1 |
| 1 | +1 | -1 | -- |
| 2 | -1 | +1 | +1 |
| 3 | -1 | +1 | -- |
| 4 | -1 | +1 | -1 |
| 5 | -1 | -1 | -- |
| 6 | +1 | +1 | -1 |
| 7 | +1 | -1 | -- |

(Odd KO-dimensions have no grading operator gamma, so epsilon'' is not applicable.)

**For KO-dimension 6:** J^2 = +1, JD = +DJ, J gamma = -gamma J. This is precisely what the self-modeling construction gives with the candidate J(psi,chi) = (PC chi-bar, PC psi-bar) and gamma(psi,chi) = (P psi, -P chi).

**The axioms of a real spectral triple** (A, H, D, J, gamma) are:
1. A is a *-algebra represented on a Hilbert space H
2. D is a self-adjoint (unbounded) operator on H with compact resolvent (for infinite-dimensional H)
3. [a, JbJ^{-1}] = 0 for all a, b in A (order zero condition / zeroth-order condition)
4. [[D, a], JbJ^{-1}] = 0 for all a, b in A (first-order condition)
5. J, gamma satisfy the KO-dimension sign relations
6. D gamma = -gamma D (even case)
7. Orientability (Hochschild cycle condition)
8. Poincare duality (intersection form is non-degenerate)

For finite-dimensional spectral triples (our case), conditions 2 and 7-8 simplify: D is just a self-adjoint matrix, compact resolvent is automatic, orientability becomes a condition on the representation, and Poincare duality becomes a condition on the K-theory pairing.

**Limitations:** The axioms were formulated for Riemannian (Euclidean) signature. Lorentzian versions require Krein spaces (see below).

**Relevance:** This is the foundation. The self-modeling construction must satisfy these axioms. J^2 = +1 and J gamma = -gamma J are already verified. The remaining checks are: order zero condition, first-order condition, and existence of D with D gamma = -gamma D and JD = DJ.

### Chamseddine-Connes-Marcolli (2007) - Why the Standard Model

**Key contribution:** Classified all irreducible finite noncommutative geometries of KO-dimension 6 mod 8 and showed that under specific additional conditions, the Standard Model algebra is the unique solution.

**Precise classification theorem statement:**

*Theorem (CCM 2007):* Consider irreducible finite real spectral triples (A_F, H_F, D_F, J_F, gamma_F) of KO-dimension 6 mod 8. Then:

1. The Hilbert space dimension per generation satisfies dim(H_F) = k^2 for some positive integer k.
2. The algebra A_F is a direct sum of matrix algebras over R, C, or H (quaternions).

Under the additional conditions:
- (C1) The representation of A_F on H_F satisfies the first-order condition
- (C2) The constraint on the subalgebra imposed by the massless graviton condition (A_F contains the field of rationals, ensuring the algebra is "big enough")
- (C3) Quaternion linearity (the algebra contains H as a summand, acting on H_F from the left)
- (C4) Unimodularity (SU(A_F) rather than U(A_F))

the unique solution is k = 4, giving:

**A_F = M_2(H) + M_4(C)** (the "input" algebra)

with the subalgebra surviving the first-order condition being:

**A_F^{(1)} = C + H + M_3(C)** (the Standard Model algebra)

The gauge group is then U(A_F^{(1)}) / center = U(1) x SU(2) x SU(3), which is the Standard Model gauge group.

**Critical subtlety for this project:** The "input" algebra in CCM is M_2(H) + M_4(C), not C + H + M_3(C). The SM algebra emerges as the SUBALGEBRA consistent with the first-order condition [[D, a], Jb*J^{-1}] = 0. This is a constraint FROM D, not on D. The first-order condition acts as a filter: given the full algebra and Hilbert space, only a subalgebra is compatible with any given Dirac operator satisfying the first-order condition.

**What the classification does NOT determine:** The Dirac operator D_F is not uniquely determined by the axioms -- it lives in a moduli space parameterized by fermion masses and mixing matrices. The spectral action then determines the dynamics.

**Relevance to this project:** If the self-modeling composite gives an irreducible finite spectral triple of KO-dimension 6, this theorem constrains the algebra. The key question is whether the self-modeling composite's Hilbert space (dim = 2n^2) gives k^2 = 2n^2 for some integer k, and whether the additional conditions (C1)-(C4) hold. For n=4: dim(H) = 32, giving k^2 = 32, which is NOT a perfect square. This is a potential obstruction -- see PITFALLS.md. However, the theorem applies per generation; with the correct counting (particle/antiparticle doubling already in H), the effective dimension may differ.

### Connes (2006) - NCG and the Standard Model with Neutrino Mixing

**Key contribution:** Resolved the fermion doubling problem by recognizing that the finite noncommutative geometry F should have KO-dimension 6 (not 0), with metric dimension 0. This key insight allows the metric dimension and KO-dimension to be independent.

**Method:** Changed the grading on the antiparticle sector to its opposite. In the old model (KO-dim 0), the finite space had gamma_F = +1 on particles and +1 on antiparticles. In the new model (KO-dim 6), gamma_F = +1 on right-handed particles and left-handed antiparticles, and gamma_F = -1 on left-handed particles and right-handed antiparticles. This eliminates the unphysical doubling of fermion degrees of freedom and naturally incorporates the see-saw mechanism for neutrino masses.

**The eigenvalue pattern** of gamma_F in the KO-dim 6 model is:

| Sector | gamma_F eigenvalue |
|--------|-------------------|
| nu_R, e_R, u_R, d_R (right-handed particles) | +1 |
| nu_L, e_L, u_L, d_L (left-handed particles) | -1 |
| (nu_R)^c, (e_R)^c, (u_R)^c, (d_R)^c (right-handed antiparticles) | -1 |
| (nu_L)^c, (e_L)^c, (u_L)^c, (d_L)^c (left-handed antiparticles) | +1 |

**Relevance to this project:** This eigenvalue pattern is EXACTLY what the self-modeling gamma(psi,chi) = (P psi, -P chi) produces (as documented in paper7-spectral-triple-prompt.md). The correspondence is:
- wedge^2-particle (P=-1, matter-sign=+1, gamma=-1) <-> left-handed particles
- Sym^2-particle (P=+1, matter-sign=+1, gamma=+1) <-> right-handed particles
- wedge^2-antiparticle (P=-1, matter-sign=-1, gamma=+1) <-> left-handed antiparticles
- Sym^2-antiparticle (P=+1, matter-sign=-1, gamma=-1) <-> right-handed antiparticles

### Chamseddine-Connes (1996) - The Spectral Action Principle

**Key contribution:** Proposed that the entire bosonic Lagrangian (Einstein-Hilbert + Yang-Mills + Higgs) is given by a single trace formula: Tr(chi(D/Lambda)), where chi is a smooth approximation to a cutoff function, D is the full Dirac operator, and Lambda is a cutoff scale.

**The spectral action formula:**

S = Tr(chi(D/Lambda)) + (1/2) <J psi, D psi>

The first term gives the bosonic action (gravity + gauge + Higgs). The second term gives the fermionic action. The asymptotic expansion of the trace in powers of Lambda gives:

Tr(chi(D/Lambda)) ~ sum_{n >= 0} f_n a_n(D^2)

where f_n are moments of chi and a_n are the Seeley-DeWitt coefficients. For an almost-commutative geometry M x F:
- a_0 gives the cosmological constant
- a_2 gives the Einstein-Hilbert action + Higgs mass term
- a_4 gives the Yang-Mills action + Higgs quartic coupling + topological terms

**Relevance:** If the self-modeling spectral triple is established, the spectral action automatically gives the physical Lagrangian. This is the payoff: all of the Standard Model + gravity from a single spectral action principle applied to the self-modeling spectral triple.

### Krajewski (1997) - Classification of Finite Spectral Triples

**Key contribution:** Developed a diagrammatic method (Krajewski diagrams) for classifying all finite real spectral triples. Each irreducible representation of the algebra corresponds to a vertex; Dirac operator matrix elements correspond to edges; and the constraints (order zero, first-order condition, J-reality, gamma-grading) translate to selection rules on the diagram.

**Method:** A finite spectral triple has A = direct_sum M_{n_i}(F_i) where F_i in {R, C, H}. The Hilbert space H = direct_sum H_{ij} where each H_{ij} carries a left action of M_{n_i} and a right action of M_{n_j}. The Krajewski diagram has vertices labeled by (i, n_i, F_i) and edges connecting vertices where the Dirac operator has non-zero matrix elements.

**Selection rules from the axioms:**
- Order zero condition: the right action of A commutes with the left action, so H_{ij} = C^{n_i} tensor (C^{n_j})* (bimodule structure)
- First-order condition: D can only connect H_{ij} to H_{kl} if i=k or j=l (at most one index changes)
- J maps H_{ij} to H_{ji} (swaps left and right)
- gamma gives eigenvalue +1 or -1 on each H_{ij}

**Relevance:** This provides the explicit technology for checking whether the self-modeling Hilbert space decomposition admits a valid Krajewski diagram for the SM algebra.

### Boyle-Farnsworth (2014, 2018, 2019) - Non-Associative/Jordan Geometry and the Standard Model

**Key contributions (three papers):**

**Paper 1 (arXiv:1401.5083, 2014):** Reformulated Connes' NCG axioms. Key insight: many axioms can be unified into one. Generalized from non-commutative to non-associative geometry. Resolved the problem of 7 unwanted terms in the NCG action that previously required a non-geometric assumption to remove.

**Paper 2 (arXiv:1604.00847, 2018, JHEP):** Introduced a "new algebraic structure" in the SM. Found that the internal algebra of the NCG Standard Model naturally carries additional structure -- specifically, the algebra A_F = C + H + M_3(C) can be understood as the complexification of a particular real Jordan algebra.

**Paper 3 (arXiv:1910.11888, 2019):** Proposed "Jordan geometry" as a replacement for NCG. Instead of replacing commutative coordinates by a noncommutative algebra, replace them by a Jordan algebra. The Standard Model and Pati-Salam model both arise naturally. Jordan geometry gives:
- Automatically unimodular gauge fields (no ad hoc unimodularity constraint)
- Natural accommodation of the SM algebra
- Extension to include three right-handed sterile neutrinos and a complex scalar

**Relevance to this project:** This is the most directly relevant prior work. The self-modeling construction produces Jordan algebras (M_n(C)^sa with Jordan product a o b = (ab + ba)/2) as the natural algebraic structure. Boyle-Farnsworth show that Jordan algebras can replace C*-algebras in the spectral triple framework. This could provide the bridge: self-modeling -> Jordan algebra -> Jordan spectral triple -> SM.

**Critical assessment:** The Boyle-Farnsworth program is promising but incomplete. The Jordan geometry framework does not yet have a full analog of the spectral action principle or a complete classification theorem analogous to CCM. The program is better developed for the SM algebra identification than for the dynamical content.

### Farnsworth (2022) - Particle Models from Special Jordan Backgrounds and Spectral Triples

**Key contribution:** Defined spectral triples with Jordan coordinate algebras (not associative algebras). Constructed natural and gauge-invariant bosonic configuration spaces of fluctuated Dirac operators. The resulting theory is NOT equivalent to standard associative NCG -- it gives different physical content.

**Key result:** In the Jordan case, gauge fields are ALWAYS unimodular. This resolves a long-standing problem in NCG where the unimodularity condition U(1) -> SU(1) x ... had to be imposed by hand.

**Method:** Replace the associative *-algebra A in (A, H, D, J, gamma) with a special Jordan algebra. The order zero condition [a, Jb*J^{-1}] = 0 and first-order condition [[D, a], Jb*J^{-1}] = 0 are reformulated for Jordan algebras using the Jordan product a o b = (ab + ba)/2 instead of associative multiplication.

**Relevance:** Direct relevance. The self-modeling construction gives M_n(C)^sa, which is a special Jordan algebra (it is the self-adjoint part of a C*-algebra). This paper shows how to build spectral triples from exactly this type of algebraic object.

### Dubois-Violette-Todorov (2018, 2019) - Exceptional Jordan Algebra and the Standard Model

**Key contribution:** Showed that the automorphism group F_4 of the exceptional Jordan algebra H_3(O) (3x3 Hermitian octonionic matrices) contains the Standard Model gauge group G_SM = [SU(3) x SU(2) x U(1)] / Z_6 as a specific intersection of subgroups.

**Precise result:** F_4 has two maximal Borel-de Siebenthal subgroups: Spin(9) and SU(3) x SU(3)/Z_3. Their intersection in F_4 is precisely G_SM.

**Related work by Todorov (arXiv:1911.13124):** Extended to show H_3(O) "appears designed for" three generations of fundamental fermions: the 27-dimensional representation decomposes under G_SM into exactly the quantum numbers of one generation of quarks and leptons.

**Relevance:** This is an alternative to the Connes program that uses Jordan algebras directly. The self-modeling construction gives M_n(C)^sa, which for n=3 gives a special Jordan algebra. The exceptional Jordan algebra H_3(O) is NOT a special Jordan algebra (it is not the self-adjoint part of any associative algebra), so the connection to self-modeling is indirect. However, the result shows that Jordan algebraic structures can encode the SM gauge group, supporting the broader program.

**Boyle (arXiv:2006.16265, 2020):** Connected the exceptional Jordan algebra to the SM via triality. Showed that the complexified exceptional Jordan algebra organizes the fundamental fermions, with three generations related to SO(8) triality.

### Barrett (2015) - Matrix Geometries and Fuzzy Spaces as Finite Spectral Triples

**Key contribution:** Defined and investigated finite spectral triples with algebra A = M_n(C) and determined the general form of the Dirac operator. Provided concrete examples including fuzzy spheres.

**Key result for this project:** For A = M_n(C), the Hilbert space of a finite spectral triple is H = M_n(C) tensor C^k (the algebra acting on itself tensored with a "spinor" space). The Dirac operator is of the form D = sum_i L_{e_i} tensor gamma^i + sum_j R_{f_j} tensor delta^j, where L and R are left and right multiplication, and gamma^i, delta^j are matrices on the spinor space.

**Relevance:** This provides the technology for constructing explicit Dirac operators on M_n(C) spectral triples. The self-modeling algebra is M_n(C)^sa, and the natural Hilbert space is C^n tensor C^n = M_n(C) (viewing the tensor product as the space of n x n matrices). Barrett's results constrain what D can look like.

### Connes-van Suijlekom (2020) - Spectral Truncations and Operator Systems

**Key contribution:** Extended NCG to spectral truncations, where operator systems (self-adjoint unital subspaces of C*-algebras) replace the C*-algebra. Operator systems are closely related to Jordan algebras: an operator system is a Jordan algebra under the product a o b = (ab + ba)/2.

**Relevance:** This provides a mathematical framework for treating the self-adjoint part M_n(C)^sa as a coordinate space in NCG. In the Connes-van Suijlekom framework, M_n(C)^sa is an operator system and can serve as the "algebra" of a spectral triple. This is a more natural fit for the self-modeling construction than the standard C*-algebraic framework.

### Chamseddine-Connes-van Suijlekom (2013) - Inner Fluctuations without the First-Order Condition

**Key contribution:** Extended the theory of inner fluctuations to spectral triples that do NOT satisfy the first-order condition [[D, a], Jb*J^{-1}] = 0. The inner fluctuations acquire a quadratic term in addition to the usual linear term.

**Main result:** Without the first-order condition, the spectral action leads to Pati-Salam unification SU(2)_R x SU(2)_L x SU(4). The SM is recovered as a spontaneously broken phase.

**Relevance:** This is important for this project because the first-order condition may not hold for the self-modeling Dirac operator. If it fails, the construction is NOT dead -- it leads to a Pati-Salam model instead, which is a phenomenologically viable GUT. This provides a graceful fallback.

---

## Recent Developments

| Paper | Authors | Year | Advance | Impact on Our Work |
|-------|---------|------|---------|--------------------|
| Twisted spectral triples | Devastato-Lizzi-Martinetti | 2018 | Lorentzian signature via twisted spectral triples on Krein spaces | May be needed for Lorentzian extension |
| Spectral geometry, the spectral standpoint | Connes | 2019 (arXiv:1910.10407) | Review of current state of NCG program | Confirms KO-dim 6 as standard; discusses open problems |
| Fundamental fermions as internal forms | Dabrowski-Dossena | 2017 | Reinterpretation of SM fermions as differential forms on the internal space | Alternative perspective on the Hilbert space |
| Spectral action for Robertson-Walker metrics | Chamseddine-Connes | 2014 | Explicit spectral action for cosmological metrics | Relevant if extending to cosmology |
| Eckstein-Iochum textbook | Eckstein-Iochum | 2019 (arXiv:1902.05306) | Comprehensive treatment of spectral action computation | Reference for spectral action calculations |

---

## Known Limiting Cases

| Limit | Known Result | Source | Verified By |
|-------|-------------|--------|------------|
| Commutative A | Connes reconstruction theorem: recovers Riemannian geometry | Connes (2008, arXiv:0810.2088) | Multiple authors |
| A_F = C | Trivial internal space; no gauge fields | Direct | Standard |
| A_F = M_n(C) | U(n) gauge theory | Barrett (2015) | Multiple |
| A_F = C + H + M_3(C) | Full Standard Model | CCM (2007) | Multiple independent verifications |
| First-order condition relaxed | Pati-Salam SU(2)_R x SU(2)_L x SU(4) | CCSvS (2013) | Independent |
| n=1 (single state) | Trivial: M_1(C) = C, no internal structure | Direct | Trivial |
| n=2 | H_F = C^4 doubled = C^8; Sym^2 = C^3, wedge^2 = C^1; k^2 = 8 not perfect square | Direct calculation | Should be checked computationally |

---

## Open Questions

1. **Order zero condition for the self-modeling algebra action** -- Does [a, Jb*J^{-1}] = 0 hold for the natural action pi(a)(psi,chi) = (a tensor 1)(psi), (a tensor 1)(chi)? The answer depends on the precise definition of the algebra action and J. This is the first critical check. If it fails for the naive action, a modified action must be found.

2. **Natural Dirac operator from temporal asymmetry** -- The sequential product a.b = sqrt(a) b sqrt(a) is temporally asymmetric. Does the "asymmetry operator" D_asym, defined by some natural construction from sp(a,b) - sp(b,a), satisfy D gamma = -gamma D and JD = DJ? No prior work derives D from sequential product asymmetry; this would be new.

3. **Which n gives the SM?** -- The CCM classification gives k=4 (dim H_F = 16 per generation, 32 with particle/antiparticle doubling). The self-modeling construction gives dim(H) = 2n^2. Matching 2n^2 = 32 gives n = 4. But the counting may not be this simple due to the distinction between the CCM "generation" counting and the self-modeling Hilbert space structure.

4. **Is the Jordan route better than the C*-algebraic route?** -- Boyle-Farnsworth suggest replacing NCG with Jordan geometry. The self-modeling construction gives Jordan algebras naturally (M_n(C)^sa). Should we attempt to satisfy Connes' axioms (which require an associative algebra) or Boyle-Farnsworth's Jordan axioms (which are more natural for our construction but less developed)? Recommendation: try Connes first (more mature, clearer classification), with Jordan as fallback.

5. **What happens if the first-order condition fails?** -- If [[D, a], Jb*J^{-1}] != 0 for the natural D, we get Pati-Salam instead of SM. This is not a failure -- Pati-Salam is a viable GUT. But the SM would then emerge only after spontaneous symmetry breaking, which adds a step to the derivation chain.

---

## Notation Conventions in the Literature

| Quantity | Standard Symbol(s) | Variations | Our Choice | Reason |
|----------|-------------------|------------|-----------|--------|
| Real structure | J | J, J_F (finite part) | J | Matches Paper 5's involution |
| Chirality grading | gamma, gamma_5, gamma_F | chi (some authors) | gamma | Standard in Connes |
| KO-dimension signs | (epsilon, epsilon', epsilon'') | (e, e', e''); some authors use n mod 8 directly | (epsilon, epsilon', epsilon'') | Standard in CCM |
| Finite algebra | A_F | A_int, A_discrete | A_F | Standard |
| Order zero condition | [a, Jb*J^{-1}] = 0 | [a, b^o] = 0 where b^o = Jb*J^{-1} | [a, Jb*J^{-1}] = 0 | Explicit J |
| First-order condition | [[D, a], Jb*J^{-1}] = 0 | [[D, a], b^o] = 0 | [[D, a], Jb*J^{-1}] = 0 | Explicit J |
| Spectral action | Tr(chi(D/Lambda)) | S_b, S_bos | Tr(chi(D/Lambda)) | Standard |
| Sequential product | sp(a,b) = sqrt(a) b sqrt(a) | a . b, a * b, L_a(b) | sp(a,b) | Matches Paper 5 |

---

## Theoretical Framework

### Governing Theory

| Framework | Scope | Key Equations | Regime of Validity |
|-----------|-------|--------------|-------------------|
| Noncommutative geometry (Connes) | Spectral characterization of geometry; unification of gravity and gauge theory | Spectral action: S = Tr(chi(D/Lambda)) + (1/2)<J psi, D psi> | Almost-commutative geometries; compact Riemannian manifolds; finite-dimensional internal spaces |
| Self-modeling framework (Papers 5-6) | Forces QM (M_n(C)^sa) and GR (Einstein's equations) from self-modeling | Sequential product: sp(a,b) = sqrt(a) b sqrt(a); Hamiltonian: H ~ J*SWAP | Finite-dimensional systems; discrete lattice with thermodynamic/continuum limit |

### Mathematical Prerequisites

| Topic | Why Needed | Key Results | References |
|-------|-----------|-------------|-----------|
| KO-theory / Real K-theory | Classifies real structures on spectral triples; determines sign table | KO-dimension mod 8 classification; Bott periodicity | Connes (1995); Gracia-Bondia-Varilly-Figueroa textbook |
| Krajewski diagram theory | Classifies finite spectral triples; constrains Dirac operator | Selection rules from order zero and first-order conditions | Krajewski, hep-th/9701081 |
| Jordan algebras | M_n(C)^sa is a special Jordan algebra; alternative to C*-algebraic framework | JvNW classification (1934); Boyle-Farnsworth reformulation | McCrimmon textbook; Boyle-Farnsworth (2019) |
| Representation theory of finite-dimensional algebras | Decomposes H_F into irreducible bimodules | Wedderburn-Artin theorem; bimodule decomposition | Any algebra textbook |
| Clifford algebras | Control the KO-dimension and real structure | Cl(p,q) classification; periodicity mod 8 | Lawson-Michelsohn; Gracia-Bondia et al. |

### Symmetries and Conservation Laws

| Symmetry | Conserved Quantity | Implications for Methods |
|----------|-------------------|------------------------|
| Diagonal U(n) covariance (Paper 6) | Gauge invariance of self-modeling Hamiltonian | Forces SWAP Hamiltonian; constrains algebra action |
| SWAP symmetry (P^2 = 1) | Z/2 grading (chirality gamma) | Decomposes H into Sym^2 + wedge^2 |
| CPT (if applicable) | Combined charge-parity-time | J gamma = -gamma J (KO-dim 6 relation) |
| Gauge group G_SM | Charges (hypercharge, weak isospin, color) | Determined by first-order condition on A_F |

### Unit System and Conventions

- **Unit system:** Natural units (hbar = c = k_B = 1) for dynamical content; dimensionless for algebraic structure
- **Metric signature:** Not directly applicable (finite NCG is algebraic); (+,-,-,-) when connecting to continuous spacetime
- **Hilbert space convention:** Inner product linear in second argument (physics convention, <psi|phi> = psi^dagger phi)
- **J convention:** Antilinear isometry; J(alpha psi) = alpha-bar J(psi)
- **Grading convention:** gamma = +1 on "right-handed" (Sym^2-particle, wedge^2-antiparticle); gamma = -1 on "left-handed" (wedge^2-particle, Sym^2-antiparticle)

---

## Alternatives Considered

| Category | Recommended | Alternative | Why Not |
|----------|------------|-------------|---------|
| Algebraic framework | Connes' real spectral triple (associative algebra) | Boyle-Farnsworth Jordan geometry | Jordan framework less mature; no classification theorem yet; try associative first |
| Algebra action | Left action pi(a) = a tensor 1 | Two-sided action pi(a) = a tensor a* | Two-sided action violates linearity of the representation |
| Hilbert space | Doubled H = (C^n tensor C^n) + (C^n tensor C^n) | Single copy C^n tensor C^n | Must double for particle/antiparticle to get J gamma = -gamma J |
| KO-dimension | 6 | 0, 2, or 4 | Sign relations J^2 = +1, J gamma = -gamma J force KO-dim = 6 (the only even KO-dim with these signs) |
| Dirac operator source | Sequential product asymmetry | Postulated D matching Connes | Must derive D from self-modeling, not postulate it |
| Classification approach | CCM (2007) top-down classification | Bottom-up: construct A_F directly | CCM gives the cleanest identification conditions |

---

## Sources

- Connes, "Noncommutative geometry and reality," J. Math. Phys. 36, 6194 (1995) -- foundational axioms and KO-dimension classification
- Chamseddine-Connes, "The spectral action principle," arXiv:hep-th/9606001 -- spectral action formula
- Chamseddine-Connes-Marcolli, "Why the Standard Model," arXiv:0706.3688 -- classification theorem
- Connes, "NCG and the SM with neutrino mixing," arXiv:hep-th/0608226 -- KO-dim 6 resolution of fermion doubling
- Krajewski, "Classification of finite spectral triples," arXiv:hep-th/9701081 -- Krajewski diagrams
- Barrett, "Matrix geometries and fuzzy spaces as finite spectral triples," arXiv:1502.05383 -- Dirac operators on M_n(C)
- Boyle-Farnsworth, "Non-commutative geometry, non-associative geometry and the SM," arXiv:1401.5083 -- axiom reformulation
- Boyle-Farnsworth, "A new algebraic structure in the SM," arXiv:1604.00847 -- algebraic structure identification
- Boyle-Farnsworth, "The SM, the Pati-Salam model, and Jordan geometry," arXiv:1910.11888 -- Jordan geometry program
- Farnsworth, "Particle models from special Jordan backgrounds," arXiv:2206.07039 -- Jordan spectral triples
- Boyle, "The SM, the exceptional Jordan algebra, and triality," arXiv:2006.16265 -- octonionic connection
- Dubois-Violette-Todorov, "Octonions, exceptional Jordan algebra, and F_4 in particle physics," arXiv:1805.06739 -- F_4 and SM gauge group
- Todorov, "Exceptional quantum algebra for the SM," arXiv:1911.13124 -- H_3(O) and three generations
- Chamseddine-Connes-van Suijlekom, "Inner fluctuations without first-order condition," arXiv:1304.7583 -- Pati-Salam from relaxed axioms
- Chamseddine-Connes, "Beyond the spectral SM: Pati-Salam unification," arXiv:1304.8050 -- Pati-Salam emergence
- Connes-van Suijlekom, "Spectral truncations and operator systems," arXiv:2004.14115 -- operator systems in NCG
- van Suijlekom, "NCG and Particle Physics," 2nd ed. (2024) -- definitive textbook
- Eckstein-Iochum, "Spectral Action in NCG," arXiv:1902.05306 -- comprehensive spectral action reference
- Cacic, "Moduli spaces of Dirac operators for finite spectral triples," arXiv:0902.2068 -- moduli space structure
- Connes, "NCG, the spectral standpoint," arXiv:1910.10407 -- 2019 review of the full program
