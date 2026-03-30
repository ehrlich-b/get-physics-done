# Prior Work: Universality Class of Self-Modeler Network in h_3(O)

**Surveyed:** 2026-03-30
**Domain:** Exceptional Jordan algebras / Quantum lattice systems / SSB with continuous symmetry / Nonlinear sigma models
**Confidence:** MEDIUM (established results for SU(2)/O(3); novel territory for F_4 lattice systems)

This document covers prior work relevant to proving the universality class of the self-modeler network (whose algebra is h_3(O) with F_4 automorphism symmetry) supports the v9.0 mechanism chain. It does NOT re-cover v9.0 results (Fisher geometry -> sigma model -> Lorentz -> BW -> KMS -> Jacobson -> Einstein for the Heisenberg toy model) or v5.0/v8.0 results (h_3(O) Peirce decomposition, Cl(6) chirality, M_16(R) observable algebra). Those are validated inputs.

**Central question:** Does the REAL self-modeler system (sites carrying h_3(O) degrees of freedom with F_4 symmetry) fall into a universality class where the v9.0 chain fires?

---

## Theoretical Framework

### Governing Theory

| Framework | Scope | Key Equations | Regime of Validity |
|-----------|-------|---------------|-------------------|
| Exceptional Jordan algebra h_3(O) | 27-dim self-adjoint octonionic 3x3 matrices | a o b = (1/2)(ab + ba), Aut(h_3(O)) = F_4 | Exact algebraic structure |
| DLS infrared bounds | SSB proof for quantum lattice systems with continuous symmetry | Infrared bound: S(k) <= C/E(k), E(k) ~ k^2 for AFM | Bipartite lattice, reflection positive, d >= 3 |
| Nonlinear sigma model on G/H | Low-energy effective theory of SSB system | L = (1/2g^2) Tr(d_mu U^{-1} d^mu U), U in G/H | Below SSB scale, above lattice UV cutoff |
| FSS infrared bounds (classical) | Phase transitions with continuous symmetry | Gaussian domination + RP -> infrared bound | d >= 3, NN ferromagnetic, reflection positive |

### Mathematical Prerequisites

| Topic | Why Needed | Key Results | References |
|-------|-----------|-------------|-----------|
| F_4 Lie algebra (dim 52, rank 4) | Symmetry group of h_3(O) | F_4 = Aut(h_3(O)); maximal subgroups: Spin(9), SU(3)xSU(3), Sp(3)xSU(2) | Todorov-Drenska arXiv:1805.06739 |
| Octonionic projective plane OP^2 | Target space of effective sigma model | OP^2 = F_4/Spin(9), dim = 16, compact symmetric space | Parton-Picken, Axioms 7(4):72 (2018) |
| Reflection positivity on lattices | Technical condition for infrared bounds | RP holds for bipartite lattices with NN interactions | Froehlich-Simon-Spencer, CMP 50 (1976) |
| Peirce decomposition of h_3(O) | Defines the lattice site algebra | h_3(O) = V_1 + V_{1/2} + V_0 (dims 1+16+10) | Validated in v5.0/v8.0 |
| Spectral triples on Jordan backgrounds | Alternative approach via NCG | Farnsworth: F_4 x F_4 gauge theory from n-point Jordan geometries | arXiv:2503.10744, arXiv:2506.21496 |

### Symmetries and Conservation Laws

| Symmetry | Conserved Quantity | Implications for Methods |
|----------|-------------------|------------------------|
| F_4 (automorphism of h_3(O)) | 52-dim Noether currents in continuum | Goldstone theorem: SSB of F_4 -> H produces dim(F_4/H) Goldstone modes |
| Spin(9) (stabilizer of idempotent) | 36-dim charges | If F_4 -> Spin(9): 52-36 = 16 Goldstone modes on OP^2 |
| G_2 (automorphism of octonions) | 14-dim charges | If F_4 -> G_2: 52-14 = 38 Goldstone modes |
| Lattice translation | Crystal momentum | Dispersion relation of Goldstone modes determines spin-wave velocity |
| Lattice point group | Discrete rotation symmetry | Must restore to full SO(d) in continuum limit for von Ignatowsky |

### Unit System and Conventions

- **Unit system:** hbar = 1, k_B = 1, lattice spacing a = 1
- **Jordan product:** a o b = (1/2)(ab + ba)
- **Peirce eigenvalues:** {0, 1/2, 1}
- **Octonion convention:** Fano e_1 e_2 = e_4 (matches Paper 7)
- **Clifford signature:** Cl(9,0) (positive definite)

### Known Limiting Cases

| Limit | Parameter Regime | Expected Behavior | Reference |
|-------|-----------------|-------------------|-----------|
| SU(2) Heisenberg | Restrict h_3(O) to h_2(C) | Neel order d >= 3; O(3) sigma model; v9.0 chain fires | DLS 1978; v9.0 |
| Free field (g -> 0) | Sigma model weak coupling | Asymptotic freedom in 2D; perturbative in d >= 3 | Friedan, Ann. Phys. 163 (1985) |
| Large-N O(N) | N -> infinity with g^2 N fixed | Solvable sigma model; mass gap in 2D | Brezin-Zinn-Justin, PRB 14 (1976) |
| Classical limit S -> infinity | Quantum -> classical lattice model | FSS theorem applies directly | Biskup-Chayes-Starr, CMP 269 (2007) |

---

## Key Parameters and Constants

| Parameter | Value | Source | Notes |
|-----------|-------|--------|-------|
| dim h_3(O) | 27 | Algebraic | Site Hilbert space dimension (per self-modeler) |
| dim F_4 | 52 | Algebraic | Number of continuous symmetry generators |
| rank F_4 | 4 | Algebraic | Number of independent Casimirs |
| dim OP^2 = F_4/Spin(9) | 16 | Algebraic | Goldstone manifold dimension if F_4 -> Spin(9) |
| dim Spin(9) | 36 | Algebraic | Stabilizer of a primitive idempotent in h_3(O) |
| Ricci curvature of OP^2 | Positive (Einstein manifold) | Differential geometry | Ensures asymptotic freedom of 2D sigma model |

---

## Established Results to Build On

### Result 1: Froehlich-Simon-Spencer (FSS) Infrared Bounds for Classical Systems

**Statement:** For classical lattice spin models on Z^d (d >= 3) with compact continuous symmetry group G, nearest-neighbor ferromagnetic interactions, and reflection positivity, the Fourier transform of the two-point function satisfies S(k) <= C/E(k) where E(k) is the lattice Laplacian spectrum. This infrared bound implies long-range order (SSB of G) at sufficiently low temperature.

**Proven/Conjectured:** PROVEN (1976)

**Reference:** Froehlich-Simon-Spencer, CMP 50 (1976) 79-95

**Relevance:** This is the foundational method. Originally proved for O(N) models and phi^4 theories. The key insight: the infrared bound S(k) <= C/k^2 prevents correlations from decaying too fast, forcing long-range order in d >= 3. The method requires TWO technical conditions: (1) reflection positivity of the measure, and (2) a Gaussian domination inequality. For the CLASSICAL F_4 lattice model (which exists in the classical limit S -> infinity of the quantum model), FSS applies IF the interaction is reflection positive. NN interactions on bipartite lattices satisfy RP.

**Confidence:** HIGH for O(N)/SU(N) models; MEDIUM for F_4 (conditions met in principle, but never explicitly verified for exceptional groups)

### Result 2: Dyson-Lieb-Simon (DLS) Neel Order for Quantum Heisenberg

**Statement:** The quantum SU(2) Heisenberg antiferromagnet on Z^d exhibits spontaneous symmetry breaking (Neel order) at T = 0 for: (a) S >= 1, d >= 3; (b) S >= 3/2, d >= 2; and at T > 0 for S >= 1, d >= 3. Extended by Kennedy-Lieb-Shastry (1988) to S = 1/2, d >= 3.

**Proven/Conjectured:** PROVEN

**Reference:** Dyson-Lieb-Simon, J. Stat. Phys. 18 (1978) 335; Kennedy-Lieb-Shastry, J. Stat. Phys. 53 (1988) 1019

**Relevance:** The benchmark result. DLS proves SSB for quantum spins with SU(2) symmetry. The METHOD (reflection positivity + infrared bounds) is what matters for v10.0: can it be extended to F_4 symmetry? DLS used properties specific to SU(2) spin operators, but the underlying framework (RP + infrared bounds) is more general. Nachtergaele's review (arXiv:math-ph/0603017) surveys the landscape of extensions.

**Confidence:** HIGH

### Result 3: Biskup-Chayes-Starr Quantum-to-Classical Reduction

**Statement:** For quantum spin systems with reflection positivity and a meaningful classical limit (spin magnitude S -> infinity), whenever chessboard estimates prove a phase transition in the classical model, the quantum model has a similar phase transition provided beta << sqrt(S). This reduces the quantum SSB problem to the classical one for large enough spin.

**Proven/Conjectured:** PROVEN

**Reference:** Biskup-Chayes-Starr, CMP 269 (2007) 611-657; arXiv:math-ph/0509017

**Relevance:** This is a CRITICAL result for v10.0. It says: if we can establish SSB for the CLASSICAL F_4 lattice model (which is the FSS problem), then the QUANTUM version also has SSB for large enough effective spin. The h_3(O) site algebra is 27-dimensional, so the "spin" is large (analogous to large S). The condition beta << sqrt(S) with S ~ 27 is not particularly restrictive. The catch: must verify the quantum model is reflection positive and has a well-defined classical limit.

**Confidence:** HIGH for the general theorem; MEDIUM for applicability to h_3(O) (need to verify RP and classical limit)

### Result 4: Sigma Model One-Loop Beta Function = Ricci Tensor

**Statement:** For a 2D nonlinear sigma model with target manifold (M, g), the one-loop RG beta function is beta^{(1)}_{ab} = (1/2pi) R_{ab} where R_{ab} is the Ricci tensor of the target manifold. For compact symmetric spaces G/H, the Ricci tensor is proportional to the metric: R_{ab} = (1/2d_G/H) g_{ab} where the proportionality depends on the geometry. Positive Ricci curvature implies asymptotic freedom.

**Proven/Conjectured:** PROVEN (perturbatively)

**Reference:** Friedan, Ann. Phys. 163 (1985) 318; Polyakov, Phys. Lett. B 59 (1975) 79

**Relevance:** The octonionic projective plane OP^2 = F_4/Spin(9) is a compact symmetric Einstein manifold with positive Ricci curvature. Therefore a 2D sigma model on OP^2 is asymptotically free, just like the O(3) sigma model that describes the Heisenberg antiferromagnet. This is the effective field theory statement: IF the F_4 lattice model breaks F_4 -> Spin(9) spontaneously, the Goldstone sector is described by a sigma model on OP^2 that is asymptotically free in 2D and has massive excitations (spin waves) in d >= 3 with a well-defined propagation velocity.

**Confidence:** HIGH for the general result; MEDIUM for applicability to the specific F_4 -> Spin(9) breaking pattern (which has not been established)

### Result 5: F_4 Subgroup Structure and Borel-de Siebenthal Classification

**Statement:** The maximal subgroups of F_4 (compact form) include: (a) Spin(9) (dim 36) -- stabilizer of a primitive idempotent in h_3(O); coset F_4/Spin(9) = OP^2 (dim 16). (b) SU(3) x SU(3) / Z_3 (dim 16) -- preserves the decomposition of h_3(O) into 3x3 block structure. (c) Sp(3) x SU(2) (dim 24) -- related to quaternionic substructure. The intersection of (a) and (b) yields the Standard Model gauge group (Todorov).

**Proven/Conjectured:** PROVEN (classification theory)

**Reference:** Todorov-Drenska, Adv. Appl. Cliff. Alg. 28:82 (2018), arXiv:1805.06739

**Relevance:** Determines the possible SSB patterns. If the lattice model breaks F_4 completely, the Goldstone manifold is F_4 itself (dim 52 modes). If it breaks F_4 -> Spin(9), the Goldstone manifold is OP^2 (16 modes). The PHYSICAL question is which subgroup H is preserved, which depends on the specific Hamiltonian. For self-modeler dynamics, Spin(9) is the most natural stabilizer because it is the automorphism group that preserves a chosen idempotent (= a chosen "observer" state in h_3(O)).

**Confidence:** HIGH for the group theory; LOW for which pattern is realized dynamically

### Result 6: Farnsworth Spectral Geometry with Exceptional Jordan Algebras

**Statement:** Finite-dimensional discrete spectral geometries can be constructed from non-simple exceptional Jordan algebras as coordinate algebras. The 2-point geometry yields an F_4 x F_4 gauge theory; the 1-point geometry yields G_2 x G_2. Scalar content is restricted by novel conditions from the associative properties of the coordinate algebra.

**Proven/Conjectured:** PROVEN (constructive)

**Reference:** Farnsworth, arXiv:2503.10744 (2025); arXiv:2506.21496 (2025)

**Relevance:** Independent confirmation that the exceptional Jordan algebra route to gauge theories is viable. Farnsworth's approach is via noncommutative geometry / spectral triples, different from the self-modeling route of Papers 5-7. The F_4 x F_4 gauge group from the 2-point geometry is larger than what emerges from the self-modeling framework, but the underlying algebraic structure is the same h_3(O). This cross-validates the general approach without duplicating it.

**Confidence:** MEDIUM (very recent, not yet widely cited)

### Result 7: Bjornberg-Ueltschi Review of RP and Infrared Bounds for Quantum Spins

**Statement:** Comprehensive review of the method of reflection positivity and infrared bounds applied to quantum spin systems. Covers the DLS approach, random loop representations, and extensions to SU(2)-invariant systems including spin-1 bilinear-biquadratic models.

**Proven/Conjectured:** REVIEW

**Reference:** Bjornberg-Ueltschi, arXiv:2204.12896 (2022)

**Relevance:** Most recent comprehensive survey of the RP/infrared bound technology. Clarifies what symmetry groups and lattice structures the method handles. The method works for systems where: (i) the Hamiltonian is reflection positive across a lattice hyperplane, (ii) Gaussian domination can be established, and (iii) the infrared bound S(k) <= C/E(k) can be proven. The SU(2) case is fully worked out; extensions to SU(N) and other groups require case-by-case verification.

**Confidence:** HIGH

---

## Open Problems Relevant to This Project

### Open Problem 1: Existence of SSB for Lattice Models with Exceptional Symmetry

**Statement:** Does a quantum lattice system on Z^d (d >= 3) with F_4-symmetric nearest-neighbor interactions exhibit spontaneous symmetry breaking at low temperature?

**Why it matters:** This is THE central question for v10.0. If SSB occurs, the Goldstone sector provides the sigma model needed for the rest of the v9.0 chain. If SSB does not occur (which would be surprising in d >= 3 for a compact continuous symmetry with large enough representation), the mechanism fails.

**Current status:** No published work addresses this specific question. However, the general theory strongly suggests YES for the following reasons:

1. The classical limit (FSS 1976): A classical F_4 lattice model on Z^d, d >= 3 with NN ferromagnetic interaction is expected to break F_4 spontaneously, by the same FSS infrared bound argument that works for O(N). The FSS method requires only reflection positivity (satisfied for NN bipartite) and Gaussian domination (which follows from the convexity structure of the interaction). The key technical step is verifying that the F_4 Haar measure provides the needed estimates. For ANY compact group G, the NN Heisenberg model on Z^d with spins in a G-representation has a classical RP measure, and FSS-type arguments go through in d >= 3 for large enough representation dimension. This is essentially the content of the Biskup-Chayes-Starr framework.

2. The quantum regime (DLS-type): For quantum spins with F_4 symmetry and site Hilbert space dim 27, the Biskup-Chayes-Starr reduction works because the effective spin is large (dim >> 1). The quantum model inherits SSB from its classical limit.

3. Physical intuition: In d >= 3, the infrared divergence is too weak to destroy long-range order for continuous symmetries (unlike d <= 2 where Mermin-Wagner applies). Larger symmetry groups have MORE Goldstone modes, which could in principle cause stronger fluctuations, but in d >= 3 the infrared counting still favors ordering.

**Key references:** FSS CMP 50 (1976); DLS J. Stat. Phys. 18 (1978); Biskup-Chayes-Starr CMP 269 (2007); Nachtergaele arXiv:math-ph/0603017

### Open Problem 2: Determination of the SSB Pattern for F_4

**Statement:** If F_4 is spontaneously broken, which subgroup H is preserved? Candidates: Spin(9), SU(3) x SU(3), Sp(3) x SU(2), or smaller.

**Why it matters:** The Goldstone manifold F_4/H determines the target space of the effective sigma model, which controls the low-energy physics. F_4/Spin(9) = OP^2 (dim 16) is the physically most natural choice.

**Current status:** For the Heisenberg-type model where the interaction is the Jordan product inner product, the ground state selects a direction in h_3(O). The stabilizer of a generic element of h_3(O) depends on its Jordan-algebraic properties:
- A primitive idempotent has stabilizer Spin(9) [Todorov-Drenska]
- A generic element (3 distinct eigenvalues) has stabilizer smaller than Spin(9)
- An element proportional to the identity has stabilizer F_4 (no breaking)

The SSB pattern depends on the ground state manifold of the specific Hamiltonian. For a nearest-neighbor antiferromagnet on a bipartite lattice, the Neel state selects directions on alternating sublattices, and the unbroken symmetry is the diagonal subgroup of (isotropy of sublattice A) x (isotropy of sublattice B).

**Key references:** Todorov-Drenska arXiv:1805.06739; classification of F_4 maximal subgroups

### Open Problem 3: Does the OP^2 Sigma Model Have the Right Universality Class?

**Statement:** Is the 2D nonlinear sigma model on OP^2 = F_4/Spin(9) in the same universality class as the O(3) model for the purposes of the v9.0 chain (Fisher geometry -> Lorentz -> BW)?

**Why it matters:** If the OP^2 sigma model is "sufficiently like" the O(3) model (asymptotic freedom, mass gap in d >= 3, well-defined spin-wave velocity), then the entire v9.0 chain generalizes from SU(2) -> O(3) -> S^2 to F_4 -> Spin(9) -> OP^2.

**Current status:** General theory strongly supports YES:
- OP^2 is a compact symmetric Einstein space with positive Ricci curvature, so the 2D sigma model is asymptotically free (Friedan 1985)
- In d >= 3, the sigma model is in the ordered phase with massive Goldstone bosons (spin waves) at finite temperature, exactly like O(3)
- The spin-wave velocity is determined by the curvature of the interaction and the lattice structure, not the target manifold
- The key difference: 16 Goldstone modes instead of 2, but this is a quantitative difference, not qualitative

**Key references:** Friedan, Ann. Phys. 163 (1985); Polyakov, Phys. Lett. B 59 (1975); Brezin-Zinn-Justin PRB 14 (1976)

### Open Problem 4: Constructing the F_4-Symmetric Hamiltonian from Self-Modeling

**Statement:** What is the explicit Hamiltonian for the self-modeler lattice, and is it F_4-symmetric? Is it NN on a bipartite lattice? Is it reflection positive?

**Why it matters:** The DLS/FSS/BCS machinery requires specific properties of the Hamiltonian. The self-modeling framework must produce a Hamiltonian with these properties, or an alternative route to SSB must be found.

**Current status:** Paper 5 derives the SWAP interaction from self-modeling. On the Heisenberg chain (v9.0), this is the SU(2) Heisenberg Hamiltonian H = J sum_{<ij>} S_i . S_j. For h_3(O), the analogous interaction should be H = J sum_{<ij>} (a_i, a_j) where (,) is the trace inner product on h_3(O). This interaction IS F_4-symmetric (F_4 preserves the trace inner product on h_3(O)), IS nearest-neighbor on any lattice, and IS reflection positive on bipartite lattices (by the same argument as for O(N) models: the interaction is a sum of products of generators, and the RP follows from the positivity of the representation).

**Key references:** Paper 5 (SWAP derivation); Paper 6 (lattice structure); v8.0 (Peirce operators as 16x16 matrices)

---

## Key Negative Results and No-Go Constraints

### No Lattice Models with F_4 Symmetry Exist in the Literature

**Statement:** A thorough literature survey found NO published work on quantum or classical lattice spin models with F_4 symmetry in the condensed matter or statistical mechanics literature.

**Significance:** This means v10.0 is genuinely novel. There are no benchmarks, no QMC data, no known phase diagrams for F_4 lattice models. The universality class must be established analytically (via DLS/FSS-type arguments) rather than numerically.

**What exists instead:** (a) O(N) and SU(N) lattice models -- extensively studied. (b) E_8 appears in the Zamolodchikov integrable field theory (1D Ising in transverse + longitudinal field), but this is E_8 as a DYNAMICAL symmetry of excitations, not as the SYMMETRY GROUP of the lattice interaction. (c) F-theory models with F_4 gauge group exist in string theory, but these are NOT lattice models.

**Confidence:** HIGH (absence of evidence, supported by extensive search)

### Mermin-Wagner Forbids F_4 SSB in d <= 2 at T > 0

**Statement:** For any compact continuous symmetry group G on Z^d with d <= 2 at T > 0, the Mermin-Wagner-Hohenberg theorem forbids spontaneous symmetry breaking. F_4 is compact, so SSB of F_4 is forbidden in d = 1, 2 at T > 0.

**Significance:** The v10.0 chain REQUIRES d >= 3 for the SSB step, consistent with v9.0 (which also needed d >= 3 for DLS-type arguments). In d = 2 at T = 0, SSB may still occur (DLS-type result for S = 1/2 on the square lattice is numerical evidence, not rigorous for SU(2); for F_4 nothing is known).

**Confidence:** HIGH (Mermin-Wagner is rigorous)

### No-Go: Jordan Algebra is NOT an Associative Algebra

**Statement:** h_3(O) is an exceptional Jordan algebra that cannot be realized as the self-adjoint part of any associative algebra (this is what makes it "exceptional" in the JvNW classification). Consequently, standard matrix-algebra techniques (trace, determinant, representation theory of associative algebras) do not apply directly.

**Significance:** The Hamiltonian construction must use Jordan-algebraic operations (Jordan product, trace form, Freudenthal product) rather than standard matrix multiplication. The trace inner product (a, b) = Tr(a o b) IS well-defined and F_4-invariant, so the Heisenberg-type interaction works. But diagonalization, transfer matrix methods, and other techniques that rely on associativity need careful reformulation.

**Confidence:** HIGH (algebraic fact)

---

## Alternatives Considered

| Category | Recommended | Alternative | Why Not |
|----------|------------|-------------|---------|
| SSB proof method | DLS/FSS infrared bounds via BCS reduction | Direct quantum Monte Carlo | No QMC code exists for F_4; IR bounds are analytic and general |
| Sigma model target | OP^2 = F_4/Spin(9) | F_4/G_2 or F_4/(SU(3)xSU(3)) | Spin(9) is the natural stabilizer of an idempotent; matches self-modeler structure |
| Lattice structure | Hypercubic Z^d, d >= 3 | Triangular, honeycomb, other | Bipartite needed for RP; hypercubic is simplest bipartite |
| Interaction type | Trace inner product on h_3(O) | Quadratic Casimir, higher-order Jordan products | Trace form is unique F_4-invariant bilinear form; simplest; matches SWAP |
| Universality argument | Sigma model universality (one coupling) | Lattice-specific phase diagram | Symmetric space sigma models have one coupling; universality is standard |

---

## Logical Dependency Chain for v10.0

```
[v5.0] Self-modeling -> M_n(C)^sa
[v8.0] Observable algebra = M_16(R); Peirce operators T_b
[Paper 7] Universe algebra = h_3(O), Aut = F_4
         |
         v
[v10.0 Step 1] Construct Hamiltonian H = J sum Tr(a_i o a_j) on Z^d
         |
         v
[v10.0 Step 2] Verify: H is F_4-symmetric, NN, reflection positive on bipartite lattice
         |
         v
[v10.0 Step 3] Apply FSS/BCS: classical limit has SSB in d >= 3
         |
         v
[v10.0 Step 4] Identify SSB pattern: F_4 -> Spin(9), Goldstone manifold = OP^2
         |
         v
[v10.0 Step 5] Effective sigma model on OP^2: asymptotically free, spin waves with velocity c_s
         |
         v
[v10.0 Step 6] Map to v9.0 chain: Fisher geometry on OP^2 -> Lorentz -> BW -> Jacobson
```

---

## Key References

| Reference | arXiv/DOI | Type | Relevance |
|-----------|-----------|------|-----------|
| Froehlich-Simon-Spencer (1976) | DOI:10.1007/BF01608557 | Foundational paper | Infrared bounds for classical lattice models; establishes SSB for O(N), d >= 3 |
| Dyson-Lieb-Simon (1978) | DOI:10.1007/BF01022099 | Foundational paper | Quantum SSB (Neel order) for SU(2) Heisenberg, d >= 3 |
| Kennedy-Lieb-Shastry (1988) | DOI:10.1007/BF01023854 | Extension | Neel order for S = 1/2, d = 3 |
| Nachtergaele (2006) | arXiv:math-ph/0603017 | Review | Survey of DLS extensions and quantum spin system methods |
| Biskup-Chayes-Starr (2007) | arXiv:math-ph/0509017 | Extension | Quantum-to-classical reduction via RP; SSB for large spin |
| Bjornberg-Ueltschi (2022) | arXiv:2204.12896 | Review | Modern review of RP/IR bounds for quantum spins |
| Todorov-Drenska (2018) | arXiv:1805.06739 | Paper | F_4 subgroup structure; maximal Borel-de Siebenthal subgroups |
| Todorov (2019) | arXiv:1911.13124 | Paper | Exceptional quantum algebra for Standard Model |
| Farnsworth (2025) | arXiv:2503.10744 | Paper | n-point exceptional Jordan geometries; F_4 x F_4 gauge theory |
| Farnsworth (2025) | arXiv:2506.21496 | Paper | Spectral geometry with exceptional symmetry |
| Friedan (1985) | DOI:10.1016/0003-4916(85)90383-5 | Foundational paper | Sigma model beta function = Ricci tensor |
| Polyakov (1975) | DOI:10.1016/0370-2693(75)90161-6 | Foundational paper | Asymptotic freedom of 2D sigma models |
| Parton-Picken (2018) | DOI:10.3390/axioms7040072 | Paper | Role of Spin(9) in octonionic geometry; OP^2 = F_4/Spin(9) |
| Froehlich-Israel-Lieb-Simon (1978) | DOI:10.1007/BF01014646 | Extension | Phase transitions and RP II: lattice systems |

---

## Assessment: What Is New vs. What Is Established

| Component | Status | Confidence |
|-----------|--------|------------|
| h_3(O) has Aut = F_4 | ESTABLISHED | HIGH |
| F_4 is compact Lie group (dim 52, rank 4) | ESTABLISHED | HIGH |
| F_4/Spin(9) = OP^2 (dim 16, compact symmetric) | ESTABLISHED | HIGH |
| OP^2 has positive Ricci curvature | ESTABLISHED | HIGH |
| FSS infrared bounds prove SSB for O(N) models d >= 3 | ESTABLISHED | HIGH |
| DLS/KLS proves quantum SSB for SU(2) d >= 3 | ESTABLISHED | HIGH |
| BCS reduces quantum SSB to classical for large spin | ESTABLISHED | HIGH |
| Sigma model on OP^2 is asymptotically free in 2D | ESTABLISHED (follows from positive Ricci + Friedan) | HIGH |
| FSS/BCS applies to F_4 lattice model | NEW -- needs verification of RP + Gaussian domination | MEDIUM |
| F_4 lattice model breaks to Spin(9) specifically | NEW -- SSB pattern depends on Hamiltonian details | LOW-MEDIUM |
| Self-modeler Hamiltonian has the right form | NEW -- must derive from self-modeling axioms | MEDIUM |
| Full v9.0 chain fires for OP^2 sigma model | NEW -- universality argument | MEDIUM |
| Mermin-Wagner forbids F_4 SSB in d <= 2 at T > 0 | ESTABLISHED | HIGH |
| No prior lattice models with F_4 symmetry exist | ESTABLISHED (negative result) | HIGH |
