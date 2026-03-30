# Methods Research: SSB and Universality Class for F_4-Symmetric Lattice Models

**Domain:** Rigorous statistical mechanics / Spontaneous symmetry breaking / Exceptional Lie groups
**Researched:** 2026-03-30
**Confidence:** MEDIUM

### Scope Boundary

METHODS.md covers analytical and numerical PHYSICS methods for v10.0: proving SSB for the self-modeler network with F_4 symmetry, counting Goldstone modes, constructing the effective sigma model, and determining the universality class. It does NOT cover software tools (see COMPUTATIONAL.md) or the established v9.0 results (Hastings-Koma, Nachtergaele-Sims LR bounds, O(3) sigma model, BW theorem) which are INPUTS.

**What is NEW vs v9.0:** v9.0 used the Heisenberg toy model with O(3) symmetry. v10.0 must handle the REAL symmetry group F_4 = Aut(h_3(O)), which is an exceptional Lie group of rank 4 and dimension 52. The on-site Hilbert space is now the exceptional Jordan algebra h_3(O) (dim 27), not C^2. The order parameter space is the coset F_4/H where H is the stabilizer of a frame (set of 3 orthogonal primitive idempotents). The SSB proof must use infrared bounds adapted to this setting.

---

## Recommended Methods

### Analytical Methods

| Method | Purpose | Why Recommended |
|--------|---------|-----------------|
| DLS infrared bounds via reflection positivity | Prove SSB (Neel-type order) for F_4-symmetric lattice model in d >= 3 | The ONLY rigorous method for SSB in continuous-symmetry quantum spin systems; extends to general compact G under specific conditions |
| Watanabe-Murayama Goldstone counting | Count Type-A and Type-B Nambu-Goldstone modes for F_4 -> H breaking | The definitive counting rule for non-Lorentzian SSB; determines the low-energy spectrum |
| NL sigma model on F_4/H | Effective field theory for long-wavelength Goldstone dynamics | Standard approach to universality class; replaces the O(3) sigma model from v9.0 |
| Peirce decomposition -> bipartite structure | Derive lattice Hamiltonian from Jordan product structure | Natural route from the algebraic structure of h_3(O) to a nearest-neighbor Hamiltonian on bipartite lattice |

### Numerical Methods

| Method | Purpose | Convergence | Cost Scaling | Implementation |
|--------|---------|-------------|-------------|----------------|
| Exact diagonalization of F_4 lattice model | Verify SSB numerically on small lattices | Finite-size scaling ~ O(1/N^{2/d}) | O(27^N) per state | From scratch; 27-dim on-site space |
| QMC with F_4-symmetric updates | Verify Neel order parameter for d=2,3 | Standard QMC scaling | O(beta N) per sweep | Requires sign-problem analysis |
| Root system / weight space computation | Compute F_4 representation theory data needed for infrared bound | Exact | O(1) (finite computation) | SageMath or LiE |

### Computational Tools

| Tool | Version | Purpose | Why |
|------|---------|---------|-----|
| SageMath | >=10.0 | F_4 root system, Weyl group, branching rules | Standard for exceptional Lie algebra computation |
| NumPy/SciPy | >=1.20/>=1.10 | ED for small F_4 lattice systems | Already in project |
| SymPy | latest | Symbolic verification of sigma model Lagrangians | Already in project |

---

## Method Details

### Method 1: DLS Infrared Bounds for F_4

**What:** The Dyson-Lieb-Simon (1978) / Froehlich-Simon-Spencer (1976) method uses reflection positivity (RP) of the lattice measure to derive an infrared bound on the Fourier transform of the two-point function: G_hat(k) <= C/|k|^2. Combined with a sum rule, this forces long-range order (LRO) in d >= 3 for sufficiently large spin or sufficiently low temperature.

**Mathematical basis:**

The method requires FIVE conditions. Here they are stated precisely, with the F_4 status of each:

**(RP1) Lattice with reflection symmetry.** The lattice Lambda must admit a reflection theta through a hyperplane that maps Lambda to itself. The standard choice is the hypercubic lattice Z^d with reflection through a plane bisecting bonds (not sites). The Peirce-decomposition bipartite structure of h_3(O) naturally maps to a bipartite lattice (diagonal sites connected through off-diagonal sites), which embeds into Z^d for d >= 2.

**F_4 status: SATISFIED.** The self-modeler network on Z^d inherits the reflection symmetry of the lattice. The bipartite structure (diagonal/off-diagonal Peirce components) is compatible with the checkerboard reflection used in DLS.

**(RP2) On-site space is a compact symmetric space or its tangent space.** In the classical case (FSS 1976), the spin at each site takes values in S^{n-1} (the O(n) model). In the quantum case (DLS 1978), the on-site Hilbert space carries a representation of the symmetry group G. The key requirement is that the two-point function G(x,y) = <phi_x . phi_y> can be decomposed into irreducible representations of G, and the infrared bound applies to each irreducible channel.

**F_4 status: SATISFIED.** The on-site space is the 26-dimensional traceless part of h_3(O), which is the fundamental representation of F_4. The F_4 action on this space is by automorphisms, preserving the Jordan product. The two-point function decomposes into F_4 irreps.

**(RP3) Nearest-neighbor interaction respecting G-symmetry.** The Hamiltonian must be of the form H = -J sum_{<xy>} phi_x . phi_y (ferromagnetic, J > 0) or H = J sum_{<xy>} phi_x . phi_y on a bipartite lattice with staggered order parameter (antiferromagnetic, J > 0). The interaction must be G-invariant.

**F_4 status: SATISFIED.** The natural Hamiltonian from the Jordan product is H = -J sum_{<xy>} Tr(A_x . A_y) where A_x in h_3(O) and the Jordan product gives a natural F_4-invariant inner product. On a bipartite lattice, the antiferromagnetic version gives a staggered order parameter.

**(RP4) Reflection positivity of the Gibbs measure.** The partition function Z = Tr exp(-beta H) must satisfy the RP inequality: for any observable A supported on one side of the reflection plane, <A theta(A)*> >= 0 where theta is the lattice reflection. This holds automatically for nearest-neighbor interactions of the form H = sum_{<xy>} h(phi_x, phi_y) when h depends only on phi_x . phi_y AND the lattice reflection theta bisects bonds (not sites).

**F_4 status: SATISFIED** for the natural inner-product Hamiltonian on Z^d. The proof follows the standard DLS argument: the interaction h(A_x, A_y) = Tr(A_x . A_y) depends only on the F_4-invariant inner product, and reflection through bond-bisecting planes preserves this structure.

**CRITICAL SUBTLETY:** RP holds for the ANTIFERROMAGNET on a BIPARTITE lattice (with the staggered transformation phi_x -> (-1)^x phi_x absorbing the sign), but FAILS for the quantum Heisenberg FERROMAGNET (Speer, 1985; see PITFALLS.md). The self-modeler Hamiltonian must be verified to be in the antiferromagnetic class after mapping to the standard form.

**(RP5) Infrared bound and sum rule.** The RP inequality implies the Gaussian domination bound:

    G_hat(k) <= 1/(2 beta J sum_mu (1 - cos k_mu))

where G_hat(k) is the Fourier transform of the two-point function. Combined with the sum rule (1/|Lambda|) sum_k G_hat(k) = <phi_x^2>, this forces:

    <phi_x^2> >= integral dk / (2 beta J sum_mu (1 - cos k_mu))

The integral diverges for d <= 2 (Mermin-Wagner), but for d >= 3 it converges to a finite constant I_d. Therefore, for beta J > <phi_x^2> / I_d, the long-range order parameter m^2 = lim_{|x-y|->inf} <phi_x . phi_y> > 0.

**F_4 status: SATISFIED IN PRINCIPLE.** The on-site "spin length" <phi_x^2> = Tr(A_x^2) is determined by the representation theory of F_4. For the 26-dimensional fundamental representation, this is a computable constant. The lattice integral I_d is the same as for any model on Z^d (it depends only on dimension, not on the symmetry group). The conclusion: SSB is proved for d >= 3 at sufficiently low temperature (or in the ground state for sufficiently large "spin" S).

**Known failure modes:**
- d = 1, 2: Mermin-Wagner theorem prevents SSB for continuous symmetry at T > 0 (and for d = 1 even at T = 0 for the Heisenberg model). For d = 2, T = 0: no rigorous proof of LRO exists for S = 1/2, but QMC evidence is overwhelming.
- Ferromagnetic sign: RP fails for quantum ferromagnets (Speer 1985). Must use antiferromagnetic sign or staggered order parameter.
- Non-bipartite lattice: RP requires the reflection to map each sublattice to itself, which constrains the lattice geometry. Triangular lattice does NOT have RP for the antiferromagnet (frustration).

**Key references:**
- Froehlich, Simon, Spencer, CMP 50 (1976) 79-95. Original infrared bound for classical models.
- Dyson, Lieb, Simon, JSP 18 (1978) 335-383. Extension to quantum antiferromagnets.
- Kennedy, Lieb, Shastry, JSP 53 (1988) 1019-1044. S = 1/2 in d >= 3.
- Froehlich, Israel, Lieb, Simon, CMP 62 (1978) 1-34. General RP framework.
- Biskup, arXiv:math-ph/0610025 (2006). Modern review of RP methods.
- Bjornberg, Ueltschi, arXiv:2204.12896 (2022). Recent review of RP for quantum spins.

**Confidence:** HIGH for conditions (RP1)-(RP5) being sufficient. MEDIUM for F_4 satisfying all conditions -- the gap is in (RP3), specifically: must verify that the self-modeler Hamiltonian naturally takes the required inner-product form. If the Jordan product Tr(A_x . A_y) is the interaction, this is standard. If the interaction has a more complex form (e.g., involving the cubic trace form det(A)), additional analysis is needed.

---

### Method 2: Watanabe-Murayama Goldstone Counting for F_4 -> H

**What:** When a continuous symmetry G is spontaneously broken to a subgroup H in a non-relativistic (lattice) system, the number of Nambu-Goldstone bosons (NGBs) is NOT necessarily equal to dim(G/H). The Watanabe-Murayama theorem gives the precise count.

**Mathematical basis:**

Define the Watanabe-Brauner (WB) matrix:

    rho_ab = lim_{Omega -> inf} (-i / Omega) <0| [Q_a, Q_b] |0>

where Q_a are the broken generators (a = 1, ..., n_BG with n_BG = dim(G/H)) and Omega is the system volume.

The counting rule is:

    n_A = n_BG - rank(rho)     [Type-A NGBs: linear dispersion omega ~ k]
    n_B = (1/2) rank(rho)      [Type-B NGBs: quadratic dispersion omega ~ k^2]
    n_NGB = n_A + n_B = n_BG - (1/2) rank(rho)

**Application to F_4 breaking:**

The self-modeler chooses a frame: a set of 3 mutually orthogonal primitive idempotents {e_1, e_2, e_3} in h_3(O) with e_1 + e_2 + e_3 = I. The stabilizer H of a frame in F_4 must be determined.

There are TWO symmetric spaces of F_4 (Cartan classification):

| Cartan label | Space | Dimension | Rank | Description |
|---|---|---|---|---|
| FI | F_4 / [Sp(3) . SU(2)] | 28 | 4 | Symmetric subspaces of OP^2 isomorphic to HP^2 |
| FII | F_4 / Spin(9) | 16 | 1 | Cayley projective plane OP^2 |

**Which breaking pattern applies?**

The stabilizer of a SINGLE primitive idempotent e_1 in F_4 is Spin(9). This is because F_4 acts transitively on the set of primitive idempotents (which form the Cayley plane OP^2 = F_4/Spin(9)), and Spin(9) is the stabilizer. The coset has dimension 52 - 36 = 16.

The stabilizer of a FRAME {e_1, e_2, e_3} is a SMALLER subgroup. Since fixing e_1 gives Spin(9), and then Spin(9) acts on the remaining idempotents {e_2, e_3} (which are constrained by e_2 + e_3 = I - e_1), the stabilizer of the full frame is the intersection of three copies of Spin(9). This stabilizer is:

    H_frame = Spin(8) [the stabilizer of a complete frame in F_4]

The reasoning: Spin(9) acting on the 16-dimensional Cayley plane has an isotropy subgroup Spin(8) (by the Spin(9)/Spin(8) = S^8 fibration structure). More precisely, fixing the full orthogonal frame {e_1, e_2, e_3} leaves the subgroup that preserves all three Peirce eigenspaces simultaneously. This is Spin(8), the triality group acting on the three 8-dimensional off-diagonal Peirce components V_{1/2}(e_i, e_j) for i != j.

**CAUTION:** This identification H_frame = Spin(8) needs verification. The literature on F_4 frame stabilizers is specialized. An alternative possibility is that the frame stabilizer is (SU(2))^3 or G_2 x something. The Spin(8) identification follows from triality: the three Peirce off-diagonal spaces V_{12}, V_{23}, V_{13} are each 8-dimensional and are permuted/mixed by triality, so the stabilizer that preserves all three is the fixed-point subgroup of the triality automorphism, which is G_2 (the automorphism group of the octonions). But G_2 has dimension 14, and dim(F_4/G_2) = 52 - 14 = 38, which would give 38 broken generators.

**REVISED ANALYSIS:** The frame stabilizer depends on whether we fix the frame up to permutation or including ordering. For a complete ordered frame {e_1, e_2, e_3}:

- Fixing e_1: stabilizer = Spin(9), dimension 36
- Additionally fixing e_2 (within the Spin(9) action on the 16-dim OP^2): stabilizer reduces further
- The group preserving ALL three Peirce subspaces V_0(e_i), V_{1/2}(e_i, e_j), V_1(e_i) simultaneously

The correct answer depends on the precise action. For the self-modeler, the relevant breaking is:

    F_4 -> H_frame, where n_BG = 52 - dim(H_frame)

**For the Goldstone counting:**

In a quantum antiferromagnet on a lattice (non-relativistic), the ground state expectation values <[Q_a, Q_b]> are generically ZERO for internal symmetry generators because the ground state is an eigenstate of the total spin (or the lattice analog). This means rho_ab = 0, rank(rho) = 0, and:

    n_A = n_BG, n_B = 0, n_NGB = n_BG

ALL Goldstone modes are Type-A (linear dispersion, like magnons in the Heisenberg antiferromagnet). This is the analog of the v9.0 result where the O(3) Heisenberg AFM has 2 magnon branches (= dim O(3)/O(2) = 2 broken generators).

**CONTRAST with ferromagnets:** In a ferromagnet, <[S^+, S^-]> = 2<S^z> != 0, so rank(rho) = 2 per broken pair, giving Type-B (quadratic) magnons. The self-modeler is antiferromagnetic, so we expect Type-A.

For F_4 -> Spin(8) (if frame stabilizer is Spin(8)):
- n_BG = 52 - 28 = 24
- rho_ab = 0 (antiferromagnet)
- n_NGB = 24 Type-A Goldstone modes with linear dispersion

For F_4 -> G_2 (if frame stabilizer is G_2):
- n_BG = 52 - 14 = 38
- n_NGB = 38 Type-A Goldstone modes

**This is a KEY number that determines the universality class.** The sigma model target space dimension equals n_BG.

**References:**
- Watanabe, Murayama, PRL 108 (2012) 251602, arXiv:1203.0609. The counting theorem.
- Watanabe, Ann. Rev. Cond. Mat. Phys. 11 (2020) 169, arXiv:1904.00569. Review.
- Brauner, Symmetry 2 (2010) 609-657. Earlier partial result.
- Nielsen, Chadha, Nucl. Phys. B105 (1976) 445. Original Type-I/II classification.

**Confidence:** HIGH for the counting formula itself. MEDIUM for the identification of H_frame. The frame stabilizer in F_4 is the critical group-theoretic input that must be pinned down before proceeding.

---

### Method 3: NL Sigma Model on F_4/H

**What:** The long-wavelength effective theory for Goldstone modes in the broken phase is a nonlinear sigma model (NLsM) with target space G/H. For v9.0, this was the O(3)/O(2) = S^2 sigma model (the standard O(3) NLsM). For v10.0, it is the F_4/H sigma model.

**Mathematical basis:**

The NLsM Lagrangian on a symmetric space G/H is:

    L = (f^2 / 2) g_{ab}(phi) partial_mu phi^a partial^mu phi^b

where:
- phi^a are coordinates on G/H (the Goldstone fields)
- g_{ab}(phi) is the G-invariant metric on G/H (unique up to overall scale for irreducible symmetric spaces)
- f is the "pion decay constant" (the stiffness, determined by the microscopic coupling J)

For a SYMMETRIC space (where [m, m] subset h, with g = h + m the Cartan decomposition), the metric g_{ab} is the restriction of the Killing form of g to m. The sigma model is then the standard G/H coset NLsM with:

    L = (f^2 / 2) Tr(partial_mu U^{-1} partial^mu U)

where U(x) in G/H is the coset-valued field.

**The two candidate target spaces:**

1. **FII: F_4/Spin(9) = OP^2** (Cayley plane, dim 16, rank 1)
   - This is the order parameter space if the order parameter is a single idempotent.
   - The NLsM on OP^2 is well-studied in the mathematical physics literature.
   - The Cayley plane is a rank-1 symmetric space, so the metric is uniquely determined.
   - The sigma model on OP^2 has 16 Goldstone modes.
   - RG properties: The NLsM on OP^2 is asymptotically free in d = 2 (like all compact symmetric space sigma models). In d = 3, it describes a second-order phase transition.

2. **FI: F_4/[Sp(3).SU(2)]** (dim 28, rank 4)
   - This would be the target if the stabilizer is Sp(3) x SU(2).
   - Rank 4 means the moduli space of vacua has a 4-parameter family of inequivalent ground states.

3. **F_4/Spin(8)** or **F_4/G_2** (if the frame stabilizer is one of these)
   - These are NOT standard Cartan symmetric spaces of F_4.
   - The quotient F_4/Spin(8) has dimension 24. It is a homogeneous space but may not be symmetric.
   - The quotient F_4/G_2 has dimension 38. Also a homogeneous space.
   - For non-symmetric homogeneous spaces, the NLsM is still well-defined but the metric is not uniquely determined by G-invariance (there may be a multi-parameter family of G-invariant metrics).

**The physical question is: what does the self-modeler actually break F_4 to?**

If frame-choosing breaks F_4 -> Spin(9) (single idempotent): target = OP^2, dim 16.
If frame-choosing breaks F_4 -> Spin(8) (full frame, triality-preserving): target = F_4/Spin(8), dim 24.
If frame-choosing breaks F_4 -> G_2 (full frame, octonionic-automorphism): target = F_4/G_2, dim 38.

**Recommendation:** Start with the simplest case: F_4 -> Spin(9) on OP^2. This corresponds to choosing a SINGLE preferred idempotent (one "direction" in the Jordan algebra). This is the analog of the O(3) -> O(2) breaking in v9.0 where a single Neel direction is chosen. The full frame-locking may involve further symmetry breaking within the Spin(9) stabilizer, giving a multi-stage SSB pattern:

    F_4 -> Spin(9) -> ... -> H_frame

This multi-stage picture is actually more natural from the RG perspective: different stages break at different energy scales.

**Universality class determination:**

The universality class of the quantum phase transition (if any) is determined by:
1. The target manifold dimension n = dim(G/H)
2. The spatial dimension d
3. The topology of the target (homotopy groups, which determine topological terms)

For the OP^2 sigma model:
- pi_1(OP^2) = 0 (simply connected, no topological theta-term in 2D)
- pi_2(OP^2) = Z (allows WZW-type terms in 3D)
- The universality class is a NEW one, not equivalent to O(n) for any n

This is a genuinely novel universality class that does not reduce to standard O(n) or CP^n models.

**References:**
- Friedan, PRL 45 (1980) 1057. RG flow of NLsM on general target manifolds.
- Brezin, Zinn-Justin, Le Guillou, PRB 14 (1976) 4976. Epsilon expansion for O(n) NLsM.
- Eichenherr, Forger, Nucl. Phys. B155 (1979) 381. NLsM on symmetric spaces, integrability.
- Abdalla, Abdalla, Rothe, "Non-Perturbative Methods in 2-Dimensional Quantum Field Theory" (World Scientific, 1991). Comprehensive treatment of G/H sigma models.

**Confidence:** HIGH for the sigma model construction. MEDIUM for determining which G/H is the correct target. LOW for the universality class being novel (needs explicit RG computation).

---

### Method 4: Deriving the Lattice Hamiltonian from Jordan Product Structure

**What:** The exceptional Jordan algebra h_3(O) has a natural product structure (the Jordan product a o b = (1/2)(ab + ba)) that gives rise to nearest-neighbor interactions on the lattice. The Peirce decomposition relative to a frame provides a natural bipartite structure.

**Mathematical basis:**

For a chosen frame {e_1, e_2, e_3} of orthogonal primitive idempotents, h_3(O) decomposes as:

    h_3(O) = V_1(e_1) + V_1(e_2) + V_1(e_3) + V_{1/2}(e_1,e_2) + V_{1/2}(e_2,e_3) + V_{1/2}(e_1,e_3)

where:
- V_1(e_i) = R.e_i (1-dimensional, the diagonal entries)
- V_{1/2}(e_i,e_j) = O (8-dimensional, the off-diagonal entries parametrized by octonions)

Total: 3 + 3(8) = 27 dimensions.

The natural lattice Hamiltonian is:

    H = -J sum_{<xy>} <A_x, A_y> = -J sum_{<xy>} Tr(A_x . A_y)

where Tr is the trace form on h_3(O) and the sum is over nearest-neighbor pairs on Z^d. This is F_4-invariant because F_4 preserves both the Jordan product and the trace form.

**The bipartite structure:** The Peirce decomposition gives a natural graph structure:
- Diagonal sites (the e_i components) are connected to off-diagonal sites (the V_{1/2} components)
- Off-diagonal sites are connected to each other through the Jordan product
- This is a bipartite-LIKE structure but may not map cleanly to a checkerboard

**For DLS compatibility**, the lattice model should be placed on Z^d with the entire Jordan algebra element at each site. The bipartite decomposition for DLS purposes is the checkerboard sublattice decomposition of Z^d, NOT the Peirce decomposition. The Peirce decomposition is internal (on-site) structure, while the DLS bipartite requirement is about the lattice geometry.

**The effective Hamiltonian has the form:**

    H_eff = J_1 sum_{<xy>} Tr(A_x . A_y) + J_2 sum_{<xy>} det(A_x + A_y) + ...

where J_1 is the quadratic coupling and J_2 involves the cubic invariant det (the determinant on 3x3 matrices, which is an F_4-invariant). The cubic term is relevant in the RG sense for d < 6 and can change the universality class.

**CRITICAL DECISION:** Whether to include only the quadratic term (standard Heisenberg-type) or also the cubic invariant (which is unique to the Albert algebra and has no analog in the O(3) case). The cubic invariant is the fundamental new ingredient of the exceptional Jordan algebra.

**Recommendation:** Start with J_2 = 0 (quadratic coupling only). This gives a standard Heisenberg-type model with F_4 symmetry acting on the 26-dimensional traceless part of h_3(O). The DLS infrared bound method applies directly. Add the cubic term later as a perturbation to study whether it is RG-relevant and changes the universality class.

**No standard approach exists** for deriving effective Hamiltonians from Jordan product structure. This is genuinely new territory. The closest analog is the SU(N) Heisenberg model (the standard Heisenberg model with SU(N) symmetry acting on the fundamental representation), which has been studied extensively for N = 2, 3, 4 and in the large-N limit. The F_4 model is a specific case of a "generalized Heisenberg model" with compact Lie group symmetry G and on-site representation V.

**References:**
- McCrimmon, "A Taste of Jordan Algebras" (Springer, 2004). Standard reference for Jordan algebra structure.
- Baez, "The Octonions," Bull. AMS 39 (2002) 145-205, arXiv:math/0105155. F_4 as Aut(h_3(O)).
- Yokota, "Exceptional Lie Groups" (2009). Detailed F_4 subgroup structure.
- Read, Sachdev, NPB 316 (1989) 609. SU(N) Heisenberg models, large-N limit.

**Confidence:** HIGH for the quadratic Hamiltonian construction. MEDIUM for the relevance of the cubic invariant. LOW for whether any existing literature treats F_4-symmetric lattice models.

---

### Method 5: Reflection Positivity on General Lattices

**What:** The DLS method requires reflection positivity, which constrains the lattice geometry. We need to verify RP for the specific lattice structure arising from the self-modeler network.

**Precise conditions for RP (Froehlich-Israel-Lieb-Simon 1978; Biskup 2006):**

**Condition 1: Lattice with reflection plane.** Lambda subset Z^d with a hyperplane Pi that:
- Reflects Lambda to itself: theta(Lambda) = Lambda
- Bisects bonds (the plane passes between sites, not through them)
- The lattice splits as Lambda = Lambda_+ union Lambda_- union Lambda_0 where Lambda_0 = Lambda_+ intersect Lambda_- = empty (bond-bisecting case)

**Condition 2: Interaction decomposition.** The Hamiltonian decomposes as:

    H = H_+ + H_- + H_int

where H_+ (H_-) involves only sites in Lambda_+ (Lambda_-), and H_int couples sites across the reflection plane. The coupling H_int must have the form:

    H_int = -sum_alpha A_alpha tensor theta(A_alpha)

where A_alpha are operators on Lambda_+ and theta(A_alpha) are their reflections. For nearest-neighbor interactions of the form -J phi_x . theta(phi_x) across the plane, this is automatic.

**Condition 3: On-site measure/state.** For classical spins, the single-site measure must be invariant under the symmetry group G. For quantum spins, the on-site Hilbert space carries a unitary representation of G, and the trace is used.

**Condition 4 (quantum case): Antiferromagnetic sign on bipartite lattice.** For quantum spin systems, RP requires the antiferromagnetic sign convention on a bipartite lattice (DLS 1978). The ferromagnetic quantum Heisenberg model does NOT have RP (Speer 1985, Toth 1993). The key identity that makes the antiferromagnet work:

    exp(-beta H_AFM) = exp(-beta J sum phi_x . phi_y) [bipartite lattice]

After the staggered transformation phi_x -> (-1)^x phi_x on one sublattice, this becomes effectively ferromagnetic with a minus sign absorbed, and RP holds.

**Beyond hypercubic lattices:** RP holds for any lattice that admits a bond-bisecting reflection. This includes:
- Hypercubic Z^d (the standard case)
- Body-centered cubic (BCC) lattice
- Face-centered cubic (FCC) lattice (with appropriate reflections)
- Any bipartite lattice with a reflection symmetry

RP does NOT hold for:
- Triangular lattice with antiferromagnetic coupling (frustrated, no staggered transformation)
- Kagome lattice (frustrated)
- Any lattice where the antiferromagnet is geometrically frustrated

**For the self-modeler network:** The key question is whether the self-modeler network maps to a bipartite lattice with bond-bisecting reflections. If the network is placed on Z^d (which it naturally is, from the SWAP lattice construction of Paper 6), then RP is automatic for the antiferromagnetic sign.

**References:**
- Froehlich, Israel, Lieb, Simon, CMP 62 (1978) 1-34. Part I: General theory.
- Froehlich, Israel, Lieb, Simon, JSP 22 (1980) 297-347. Part II: Short-range and Coulomb.
- Biskup, arXiv:math-ph/0610025 (2006). Modern review.
- Speer, Lett. Math. Phys. 10 (1985) 41-47. RP failure for quantum ferromagnet.
- Toth, Lett. Math. Phys. 28 (1993) 75-84. RP conditions for quantum systems.

**Confidence:** HIGH for RP on Z^d with the natural Hamiltonian. The self-modeler network on Z^d inherits RP from the lattice.

---

## Alternatives Considered

| Category | Recommended | Alternative | Why Not |
|----------|-------------|-------------|---------|
| SSB proof method | DLS infrared bounds | Peierls argument | Peierls works for discrete symmetry breaking but NOT for continuous symmetry. F_4 is continuous. |
| SSB proof method | DLS infrared bounds | Bogoliubov inequality / Mermin-Wagner approach | Mermin-Wagner PREVENTS SSB in d <= 2. For d >= 3, it gives weaker results than DLS. |
| Goldstone counting | Watanabe-Murayama | Naive dim(G/H) counting | Naive counting is wrong for non-Lorentzian systems (Type-B modes pair up). Correct for AFM (all Type-A) but using WM is the rigorous approach. |
| Effective theory | NLsM on G/H | Spin-wave theory (linear approximation) | Spin-wave theory captures the Goldstone modes perturbatively but misses topological terms and non-perturbative effects. NLsM is the systematic EFT. |
| Lattice structure | Z^d with h_3(O) at each site | Bipartite network from Peirce | The Peirce bipartite structure is internal algebra, not a lattice geometry. Must use Z^d for DLS. |
| Cubic invariant | Start with J_2 = 0 | Include det(A) from the start | The cubic invariant complicates the analysis enormously. Standard approach: prove SSB with quadratic coupling first, then study cubic as perturbation. |

## What NOT to Use

| Avoid | Why | Use Instead |
|-------|-----|-------------|
| Mean-field theory for SSB | Mean-field gives qualitatively correct phase diagram but WRONG critical exponents and cannot prove SSB rigorously | DLS infrared bounds for proof; sigma model for universality |
| Large-N limit with N = 52 | dim(F_4) = 52 is not the same as SU(N) with N = 52. The large-N expansion for SU(N) models is well-understood but does not apply to exceptional groups. | Direct F_4 representation theory; no large-N shortcut exists |
| Quantum Monte Carlo without sign-problem analysis | F_4 lattice models may have a sign problem depending on the representation | First analyze sign problem; if present, use alternative methods (tensor networks, variational) |
| Conformal bootstrap for F_4 | The conformal bootstrap for exotic symmetry groups is in its infancy; no existing results for F_4 | Direct NLsM computation |

## Method Selection by Problem Type

**If proving SSB rigorously for F_4-symmetric model in d >= 3:**
- Use DLS infrared bounds with reflection positivity
- Because: only method that gives rigorous proof; all conditions satisfied for Z^d

**If counting Goldstone modes and determining their dispersion:**
- Use Watanabe-Murayama formula with F_4 representation theory
- Because: definitive counting rule; need to compute WB matrix rho_ab

**If determining universality class:**
- Use NLsM on the target space F_4/H with epsilon expansion or functional RG
- Because: standard approach to universality; sigma model on exceptional coset is genuinely new

**If verifying SSB numerically:**
- Use exact diagonalization on small lattices (N = 2-4 sites) with 27-dim on-site space
- Because: Hilbert space dimension 27^N grows fast; N = 2 gives 729-dim, manageable; N = 4 gives ~500K-dim, at the limit

**If the cubic det(A) interaction matters:**
- Use RG analysis of the NLsM + cubic perturbation
- Because: the cubic term is the only NEW ingredient relative to standard Heisenberg models; its RG relevance determines whether F_4 gives a genuinely new universality class or reduces to O(26) at long wavelengths

## Validation Strategy

| Check | Expected Result | Tolerance | Reference |
|-------|----------------|-----------|-----------|
| F_4 Casimir on 26-rep | Specific numerical value from rep theory | Exact | Standard tables |
| Goldstone mode count | n_BG = 52 - dim(H) | Exact | Watanabe-Murayama |
| Spin-wave velocity | c_s^2 = (J/chi_perp) where chi_perp is perpendicular susceptibility | Compare to ED or QMC | Analogy with O(3) result |
| Infrared bound integral I_d | I_3 = (6 - pi^2/3)/(2 pi^2) (standard Z^3 integral) | Exact | DLS 1978 |
| NLsM beta function at 1 loop | beta = -(dim G/H)/(2 pi) epsilon + O(epsilon^2) in d = 2 + epsilon | Compare to standard result | Friedan 1980 |
| Mermin-Wagner in d = 2 | No SSB at T > 0 | Exact | MW theorem |
| Staggered order parameter vanishes at high T | m_s -> 0 as T -> inf | Monotone decrease | Thermodynamics |

## Open Questions Requiring Phase-Specific Research

1. **What is the frame stabilizer H_frame in F_4?** This is the single most important group-theoretic input. Must distinguish: stabilizer of one idempotent (= Spin(9)) vs. stabilizer of a complete frame (= Spin(8)? G_2? something else?).

2. **Is the cubic invariant det(A) RG-relevant?** If so, the F_4 universality class is genuinely new and cannot be reduced to O(n) for any n. If irrelevant, the long-wavelength physics reduces to an O(26) model.

3. **Does the F_4 lattice model have a QMC sign problem?** This determines whether numerical verification via QMC is feasible. The answer depends on the representation-theoretic details of the 26-dimensional representation.

4. **What are the homotopy groups of F_4/H?** Specifically pi_2, which determines whether topological (theta) terms or WZW terms appear in the sigma model. For OP^2: pi_2(OP^2) = Z.

5. **Is there a staggered-to-ferromagnetic map?** The DLS method for the AFM works via a staggered transformation. For O(3), this is S_i -> (-1)^i S_i. For F_4 acting on the 26-rep, the staggered transformation must be an F_4-equivariant sign flip on the on-site space. This exists if and only if the 26-rep is real (i.e., equivalent to its conjugate), which it is since F_4 has only real representations.

## Sources

- Froehlich, Simon, Spencer, "Infrared bounds, phase transitions and continuous symmetry breaking," CMP 50 (1976) 79-95
- Dyson, Lieb, Simon, "Phase transitions in quantum spin systems with isotropic and nonisotropic interactions," JSP 18 (1978) 335-383
- Kennedy, Lieb, Shastry, "Existence of Neel order in some spin-1/2 Heisenberg antiferromagnets," JSP 53 (1988) 1019-1044
- Froehlich, Israel, Lieb, Simon, "Phase transitions and reflection positivity. I," CMP 62 (1978) 1-34
- Watanabe, Murayama, "Unified Description of Nambu-Goldstone Bosons without Lorentz Invariance," PRL 108 (2012) 251602, arXiv:1203.0609
- Watanabe, "Counting Rules of Nambu-Goldstone Modes," Ann. Rev. Cond. Mat. Phys. 11 (2020) 169, arXiv:1904.00569
- Biskup, "Reflection positivity and phase transitions in lattice spin models," arXiv:math-ph/0610025 (2006)
- Bjornberg, Ueltschi, "Reflection positivity and infrared bounds for quantum spin systems," arXiv:2204.12896 (2022)
- Friedan, "Nonlinear models in 2+epsilon dimensions," PRL 45 (1980) 1057
- McCrimmon, "A Taste of Jordan Algebras" (Springer, 2004)
- Baez, "The Octonions," Bull. AMS 39 (2002) 145-205, arXiv:math/0105155
- Yokota, "Exceptional Lie Groups" (2009)
- Helgason, "Differential Geometry, Lie Groups, and Symmetric Spaces" (AMS, 2001). Cartan classification of symmetric spaces.

---

_Methods research for: F_4-symmetric lattice models, SSB and universality class_
_Researched: 2026-03-30_
