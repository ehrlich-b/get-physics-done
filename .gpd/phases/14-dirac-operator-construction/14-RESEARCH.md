# Phase 14: Dirac Operator Construction - Research

**Researched:** 2026-03-22
**Domain:** Finite noncommutative geometry / Dirac operator moduli spaces / matrix geometry spectral triples
**Confidence:** HIGH

## Summary

Phase 14 parameterizes all self-adjoint Dirac operators D on H = C^{2n^2} satisfying D gamma = -gamma D and JD = DJ, then tests whether the sequential product asymmetry operator (L_a - R_a) lies in this moduli space. The mathematical framework is completely standard: Barrett (2015) gives the general form of D for matrix geometries as sums of left and right multiplication operators tensored with gamma matrices, while Cacic (2009) provides the abstract moduli space theory. All constraints are linear in D, so the moduli space is a real vector space whose dimension is computed by null space analysis of the constraint matrix.

The key technical subtlety is the even condition failure from Phase 13: [gamma, pi(a)] != 0 for non-scalar a. This means the spectral triple is NOT even with the current (pi, gamma) pair. For Phase 14, this does NOT block Dirac operator construction -- we can still parameterize all D satisfying D* = D, D gamma = -gamma D, and JD = DJ independently of whether [gamma, pi(a)] = 0. The even condition affects interpretation (whether D is an "even" Dirac operator in the NCG sense) but not the constraint-solving algebra. The resolution of the even condition failure is an independent question that can be addressed in parallel or deferred.

The sequential product asymmetry candidate D_a: X -> sqrt(a) X sqrt(a) - sqrt(X) a sqrt(X) is problematic as stated because it is nonlinear in X. The correct linearization is: for fixed a in M_n(C)^sa, define D_a(X) = L_{sqrt(a)} X L_{sqrt(a)} - R_{sqrt(a)} X R_{sqrt(a)} where L_K(X) = KX and R_K(X) = XK. This gives D_a(X) = sqrt(a) X sqrt(a) - X (when contracted appropriately). The actual operator to test is the commutator [L_{sqrt(a)}, R_{sqrt(a)}] or equivalently L_a - R_a (left minus right multiplication by a), which IS linear and maps Sym^2 to wedge^2. Whether any natural contraction of this lies in the D moduli space is the core open question.

**Primary recommendation:** Parameterize D in block form with respect to gamma eigenspaces H_+ and H_-, impose JD = DJ as a linear constraint on the off-diagonal block M: H_+ -> H_-, count the dimension of the resulting moduli space, then test the candidate D_a(X) = aX - Xa = [a, X] (or the SWAP-odd part of L_a - R_a) against the constraints. Verify at n=2, n=3, n=4 with SymPy/NumPy.

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| --- | --- | --- | --- | --- |
| Barrett 2015 (arXiv:1502.05383) | method | General form of D for M_n(C) matrix geometries: D = sum (K_I m + epsilon' m K_I*) tensor gamma_I | use as primary D parameterization | plan, execution, verification |
| van Suijlekom 2024 (Ch. 3-4) | anchor | Textbook treatment of D constraints and block structure for finite spectral triples | use as reference for constraint derivation | plan, execution |
| Cacic 2009 (arXiv:0902.2068) | method | Moduli space theory for Dirac operators; generalized framework allowing orientability failure | use for moduli space dimension counting | plan, verification |
| Paper 5 (own) | prior artifact | Sequential product sp(a,b) = sqrt(a) b sqrt(a); source of L_a - R_a candidate | read; L_a - R_a definition | plan, execution |
| Phase 13 results | prior artifact | H = 2 x C^{n^2}, pi(a) = diag(a tensor I, a tensor I), pi_o(b) = diag(I tensor b^T, I tensor b^T), gamma = diag(P, -P), J(psi,chi) = (PC conj(chi), PC conj(psi)), even condition failure | read; all definitions are inputs | plan, execution, verification |
| Chamseddine-Connes 2008 (arXiv:0706.3688) | benchmark | Classification requires non-trivial D; moduli space dimension > 0 is necessary for SM | compare dimension count | verification |

**Missing or weak anchors:** The sequential product asymmetry as a Dirac operator candidate has NO literature precedent. This is entirely novel to this project. Confidence for the candidate itself is LOW; confidence for the parameterization method is HIGH.

## Conventions

| Choice | Convention | Alternatives | Source |
| --- | --- | --- | --- |
| Inner product | Linear in second argument | Linear in first | Physics convention; Paper 5 |
| J definition | J(psi,chi) = (PC conj(chi), PC conj(psi)) | Various | Paper 6, Phase 13 |
| P (SWAP) | P(v tensor w) = w tensor v | -- | Paper 6 |
| gamma (grading) | gamma = diag(P, -P) | -- | Phase 13 |
| KO-dimension signs | (epsilon, epsilon', epsilon'') = (+1, +1, -1) | -- | Connes 1995; Phase 13 verified J^2=+1, J gamma=-gamma J |
| Barrett D form | D(v tensor m) = sum_I (K_I m + epsilon' m K_I*) tensor gamma_I v | -- | Barrett 2015, Eq. in Prop. 3.1 |
| epsilon' for KO-dim 6 | epsilon' = +1 (JD = +DJ) | -- | KO-dim 6 sign table |
| Left multiplication | L_K(X) = KX on M_n(C) | -- | Standard |
| Right multiplication | R_K(X) = XK on M_n(C) | -- | Standard |
| Barrett isomorphism | C^n tensor C^n = M_n(C) via v tensor w -> v w^T | -- | Phase 13, Step 6 |

**CRITICAL: All equations and results below use these conventions. Under the Barrett isomorphism, pi(a) = L_a (left multiplication by a) and pi_o(b) = R_b (right multiplication by b). The SWAP operator P corresponds to the transpose: P(X) = X^T under the Barrett isomorphism.**

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in This Phase |
| --- | --- | --- | --- |
| D* = D | Self-adjointness | Spectral triple axiom | Constraint 1 on D |
| D gamma = -gamma D | D anticommutes with grading | Even spectral triple axiom | Constraint 2: forces D off-diagonal in gamma eigenspaces |
| JD = DJ | D commutes with real structure | KO-dim 6 sign epsilon' = +1 | Constraint 3: relates particle/antiparticle blocks of D |
| gamma = diag(P, -P) | Grading in sector form | Phase 13 | Determines H_+ and H_- |
| H_+ = Sym^2_p + wedge^2_{ap} | gamma = +1 eigenspace | Phase 13 | Target/source of D blocks |
| H_- = wedge^2_p + Sym^2_{ap} | gamma = -1 eigenspace | Phase 13 | Target/source of D blocks |
| D = [[0, M*], [M, 0]] | Off-diagonal block form | D gamma = -gamma D | M: H_+ -> H_- is the free data |
| sp(a,b) = sqrt(a) b sqrt(a) | Sequential product | Paper 5 (vdW arXiv:1803.11139 Def. 2) | Source of candidate D |
| L_a(X) = aX, R_a(X) = Xa | Left/right multiplication | Standard | Building blocks for candidate D |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --- | --- | --- | --- |
| Block decomposition of D | Write D as 2x2 block matrix in gamma eigenspaces | Imposing D gamma = -gamma D | van Suijlekom Ch. 3 |
| J constraint as linear system | JD = DJ becomes a system of linear equations on the entries of M | Reducing the parameter space of D | Barrett 2015; Cacic 2009 |
| Null space computation | Find the kernel of the constraint matrix to get the moduli space | Computing moduli space dimension | Standard linear algebra |
| Barrett isomorphism | Convert C^n tensor C^n to M_n(C) for cleaner operator expressions | Writing D in terms of left/right multiplication | Phase 13, Step 6 |
| SymPy symbolic constraint solving | Solve constraint equations symbolically at general n or specific n | Verification at n=2,3,4 | Project infrastructure |

### Approximation Schemes

No approximations needed. All computations are exact finite-dimensional linear algebra. The moduli space parameterization is exact (not approximate).

## Standard Approaches

### Approach 1: Block Decomposition + Linear Constraint Solving (RECOMMENDED)

**What:** Write D in block form with respect to gamma eigenspaces, impose D* = D and JD = DJ as linear constraints on the block entries, compute the null space to get the moduli space.

**Why standard:** This is exactly Method 4 from METHODS.md (D parameterization). Barrett (2015) and Cacic (2009) both use this approach. Van Suijlekom (2024) Ch. 3 provides the textbook treatment.

**Track record:** Used in every finite spectral triple classification since Krajewski (1997). The SM spectral triple's 31-parameter Dirac operator was found this way.

**Key steps:**

1. **Identify gamma eigenspaces.** From Phase 13:
   - H_+ (gamma = +1): Sym^2_p (dim n(n+1)/2) + wedge^2_{ap} (dim n(n-1)/2), total dim n^2
   - H_- (gamma = -1): wedge^2_p (dim n(n-1)/2) + Sym^2_{ap} (dim n(n+1)/2), total dim n^2
   - D gamma = -gamma D forces D = [[0, M^dagger], [M, 0]] where M: H_+ -> H_-

2. **Write M in sub-block form.** M maps from H_+ = Sym^2_p + wedge^2_{ap} to H_- = wedge^2_p + Sym^2_{ap}, so:
   ```
   M = | M_{wp,Sp}   M_{wp,wap}  |
       | M_{Sap,Sp}  M_{Sap,wap} |
   ```
   where M_{wp,Sp}: Sym^2_p -> wedge^2_p has size n(n-1)/2 x n(n+1)/2, etc.

3. **Impose self-adjointness.** D = D* requires M^dagger M = M M^dagger (automatic from the 2x2 block structure: D* = [[0, M^dagger], [M, 0]] = D when M^dagger is in the upper-right block). So D = D* is already built into the block form. The free data is any complex matrix M: H_+ -> H_-, which has 2 * n^2 * n^2 = 2n^4 real parameters.

   **Correction:** D = [[0, M^dagger], [M, 0]] is automatically self-adjoint for ANY M. So self-adjointness does not constrain M at all. The space of self-adjoint D anticommuting with gamma is parameterized by arbitrary complex n^2 x n^2 matrices M, giving 2n^4 real parameters before JD = DJ.

4. **Impose JD = DJ.** Write J in the gamma-eigenspace basis. Since J swaps particle and antiparticle sectors AND anticommutes with gamma, J maps H_+ to H_- and H_- to H_+. The condition JD = DJ becomes a constraint relating M to J M^dagger J^{-1}. Specifically, JD = DJ with D = [[0, M^dagger], [M, 0]] gives:
   ```
   J [[0, M^dagger], [M, 0]] = [[0, M^dagger], [M, 0]] J
   ```
   Since J maps between gamma eigenspaces (because J gamma = -gamma J), write J = [[0, J_-], [J_+, 0]] where J_+: H_+ -> H_- and J_- = J_+^{-1} (since J^2 = 1). Then JD = DJ becomes:
   ```
   J_- M = M^dagger J_-  and  J_+ M^dagger = M J_+
   ```
   These are conjugate conditions. The surviving M form a real vector subspace of the space of all n^2 x n^2 complex matrices.

5. **Compute null space dimension.** The constraint J_- M = M^dagger J_- is a real-linear constraint on M. Vectorize M as a 2n^4-dimensional real vector, express the constraint as a matrix equation, find the kernel dimension. This is the moduli space dimension.

6. **Verify at n=2,3,4.** Build explicit matrices for J_+, J_- using Phase 13's J definition, solve the constraint system, count free parameters.

**Known difficulties at each step:**

- Step 1: The gamma eigenspaces mix particle and antiparticle sectors in a non-obvious way. The Sym^2_p and wedge^2_{ap} are in H_+, while wedge^2_p and Sym^2_{ap} are in H_-. Must carefully track the basis ordering.
- Step 4: J is antilinear, so J M J^{-1} involves complex conjugation. The constraint JD = DJ for antilinear J becomes: J D J^{-1} = D (since JD = DJ and J^2 = 1). In matrix form with J antilinear: J D J^{-1} acts as J_matrix conj(D) J_matrix^{-1} = D, where J_matrix is the linear part. This makes the constraint real-linear (not complex-linear) on M.
- Step 5: For n=4, M is 16x16 complex, giving a 512-dimensional real vector space before JD = DJ. The constraint matrix is large but sparse and tractable with SymPy/NumPy.

### Approach 2: Barrett's Matrix Geometry Form (COMPLEMENTARY)

**What:** Use Barrett's (2015) formula: on H = V tensor M_n(C), the Dirac operator takes the form D(v tensor m) = sum_I (K_I m + epsilon' m K_I*) tensor gamma_I v, where K_I are free matrix parameters and gamma_I are products of gamma matrices acting on V.

**When to use:** As a cross-check on Approach 1. Barrett's parameterization directly gives D in terms of left/right multiplication operators, making it easy to compare with the sequential product candidate.

**Key insight for our case:** Our V = C^2 (two sectors: particle/antiparticle). The gamma matrices on V = C^2 are just the Pauli matrices (up to convention). For KO-dimension 6, epsilon' = +1, so the Barrett form becomes:

D(v tensor X) = sum_I (K_I X + X K_I*) tensor sigma_I v

where X in M_n(C) (under Barrett isomorphism), K_I are n x n matrices (free parameters), and sigma_I are products of Pauli matrices acting on V = C^2.

For V = C^2 with one gamma matrix gamma_1, there are two terms (I = empty and I = {1}):
```
D(v tensor X) = (K_0 X + X K_0*) tensor v + (K_1 X + X K_1*) tensor gamma_1 v
```
where K_0 is Hermitian (K_0 = K_0*) and K_1 is skew-Hermitian (K_1 = -K_1*) or vice versa depending on the signature convention.

**Tradeoffs:** Barrett's form gives the answer in terms of left/right multiplication operators on M_n(C), making the connection to the sequential product candidate transparent. However, it assumes the Barrett isomorphism and the V tensor M_n(C) structure, while Approach 1 works directly on C^{2n^2}.

### Anti-Patterns to Avoid

- **Testing only the sequential product candidate without first parameterizing the full moduli space (FORBIDDEN PROXY P4):** Must enumerate all allowed D before testing specific candidates. If the moduli space is empty, no candidate can work. If it has dimension d, the candidate must lie in a d-dimensional space.
  - _Example:_ Jumping straight to "does L_a - R_a satisfy JD = DJ?" without knowing what the space of solutions looks like.

- **Constructing ad hoc D without self-modeling motivation (FORBIDDEN PROXY):** The contract explicitly forbids this. Any D must be motivated from self-modeling structure.
  - _Example:_ Picking a random Hermitian matrix as D because it satisfies the constraints.

- **Confusing the antilinearity of J with linearity:** J is antilinear. JD = DJ with antilinear J means J_matrix conj(D) J_matrix^{-1} = D, NOT J_matrix D J_matrix^{-1} = D. Getting this wrong gives incorrect constraints.
  - _Example:_ Writing JDJ^{-1} = D and treating J as a matrix, ignoring the complex conjugation on D.

- **Ignoring the even condition failure:** [gamma, pi(a)] != 0 means the spectral triple is not even. This affects the first-order condition (Phase 15) but NOT the D parameterization. Do not let this block the D construction.

## Existing Results to Leverage

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
| --- | --- | --- | --- |
| Barrett D form for matrix geometry | D(v tensor m) = sum_I (K_I m + epsilon' m K_I*) tensor gamma_I v | Barrett 2015 (arXiv:1502.05383), Proposition 3.1 | Starting point for D parameterization |
| H = 2 x C^{n^2} bimodule decomposition | H = C^{n^2}_p + C^{n^2}_{ap}, unique irreducible M_n(C)-bimodule | Phase 13 (verified) | Input structure |
| pi(a) = diag(a tensor I, a tensor I) | Algebra action on H | Phase 13-01 (verified) | Used in [D, pi(a)] computation |
| pi_o(b) = diag(I tensor b^T, I tensor b^T) | Opposite algebra action | Phase 13-01 (verified) | Used in first-order condition (Phase 15) |
| J^2 = +1, J gamma = -gamma J | KO-dim 6 signs | Phase 13-02 (verified, 52 pytest tests) | J structure input |
| Barrett isomorphism: C^n tensor C^n = M_n(C) | v tensor w -> v w^T | Phase 13 Step 6 (verified) | Converts tensor product to matrix space |
| P(X) = X^T under Barrett isomorphism | SWAP = transpose | Direct from v tensor w -> v w^T | gamma eigenspaces = Sym/Skew matrices |
| Gamma eigenspaces | Sym^2_p(+1) + wedge^2_p(-1) + wedge^2_{ap}(+1) + Sym^2_{ap}(-1) | Phase 13 Step 3 (verified) | Block structure of D |
| Sym^2(C^n) = symmetric matrices | dim = n(n+1)/2, under Barrett iso | Standard | Gamma eigenspace dimensions |
| wedge^2(C^n) = skew-symmetric matrices | dim = n(n-1)/2, under Barrett iso | Standard | Gamma eigenspace dimensions |
| Even condition [gamma, pi(a)] = 0 FAILS | For all non-scalar a | Phase 13-02 (verified) | Known issue; does not block D parameterization |

**Key insight:** Under the Barrett isomorphism, the SWAP operator P becomes the transpose. So Sym^2(C^n) corresponds to symmetric n x n matrices and wedge^2(C^n) corresponds to skew-symmetric n x n matrices. D must map between these subspaces. Left multiplication L_a(X) = aX and right multiplication R_a(X) = Xa both map symmetric matrices to general matrices (not necessarily preserving symmetry). The antisymmetric combination L_a - R_a maps symmetric to skew-symmetric and vice versa (since (aX - Xa)^T = X^T a^T - a^T X^T = -(a^T X^T - X^T a^T); for a = a^T symmetric, this gives -(aX^T - X^T a) = -(L_a - R_a)(X^T)). This is the origin of the D gamma = -gamma D property for the sequential product candidate.

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
| --- | --- | --- | --- |
| J on Barrett space | Under Barrett iso, J(X_p, X_{ap}) = (conj(X_{ap})^T, conj(X_p)^T) = (overline{X_{ap}}^T, overline{X_p}^T) | Compute from J(psi,chi) = (PC conj(chi), PC conj(psi)) | Need to verify at n=2 |
| D gamma = -gamma D in Barrett language | D maps symmetric matrices to skew-symmetric and vice versa (within each sector) | Phase 13 gamma eigenspace analysis | Central constraint |
| dim(H_+) = dim(H_-) = n^2 | Equal-dimensional gamma eigenspaces | Phase 13 Step 3 | M is square (n^2 x n^2) |
| M_n(C) = Sym_n + Skew_n | Symmetric + skew-symmetric decomposition | Standard linear algebra | Barrett isomorphism converts gamma eigenspaces |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| --- | --- | --- | --- | --- |
| "Matrix geometries and fuzzy spaces" | Barrett | 2015 | General D form for A = M_n(C) | Proposition 3.1: D parameterization; examples at small n |
| "Moduli spaces of Dirac operators" | Cacic | 2009 | Abstract moduli space theory | Definition of D_0(A,H,P); generalized axioms without orientability |
| "Why the Standard Model" | Chamseddine, Connes | 2008 | SM has 31-parameter D | Benchmark: moduli space should be non-trivial |
| "NCG and Particle Physics" 2nd ed. | van Suijlekom | 2024 | Textbook D construction | Ch. 3: finite spectral triple D; Ch. 11: SM D parameterization |
| "Computing spectral action for fuzzy geometries" | Barrett, Glaser | 2016 | Explicit D computation at small n | arXiv:1912.13288; computational techniques for Barrett D form |
| "Bootstrapping NCG with Dirac ensembles" | Hessam, Khalkhali, Pagliaroli | 2025 | Recent D parameterization | arXiv:2512.08694; explicit Barrett D formula with gamma matrices |
| Paper 5 (own) | -- | -- | Sequential product definition | sp(a,b) = sqrt(a) b sqrt(a); asymmetry L_a - R_a |

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
| --- | --- | --- | --- |
| SymPy | >= 1.13, `sympy.matrices` | Symbolic constraint solving at n=2 (8x8 D); parameterize moduli space | Project infrastructure; exact arithmetic |
| NumPy | >= 1.26 | Explicit numerical matrices at n=2,3,4; null space computation via SVD | Project infrastructure; 32x32 matrices trivial |

### Supporting Tools

| Tool | Purpose | When to Use |
| --- | --- | --- |
| `numpy.linalg.svd` | Null space computation for JD = DJ constraint | Dimension counting at specific n |
| `numpy.kron` | Kronecker product for building pi(a), pi_o(b) | Constructing operators on H = C^{2n^2} |
| `sympy.physics.quantum.TensorProduct` | Symbolic tensor product | General-n derivations |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
| --- | --- | --- |
| SymPy symbolic at general n | NumPy at specific n only | SymPy gives exact formulas but may struggle with large symbolic matrices; NumPy gives dimensions but not parameterization |
| Null space via SVD | Null space via QR or Gaussian elimination | SVD is more numerically stable; for exact work, SymPy's `nullspace()` is better |

### Computational Feasibility

| Computation | Estimated Cost | Bottleneck | Mitigation |
| --- | --- | --- | --- |
| D moduli space at n=2 (M is 4x4 complex) | < 1 second | None | Trivial |
| D moduli space at n=3 (M is 9x9 complex) | < 5 seconds | None | Trivial |
| D moduli space at n=4 (M is 16x16 complex) | < 30 seconds | Constraint matrix is 512 x 512 real | SVD of 512x512 is fast |
| Sequential product candidate check at n=2 | < 1 second | None | Trivial |
| General-n symbolic parameterization | 1-5 minutes | SymPy simplification | Work in Barrett form to reduce expression size |

**Installation / Setup:**
```bash
# Already available in project environment
pip install numpy scipy sympy
```

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| --- | --- | --- | --- |
| D* = D | Self-adjointness of constructed D | Compute D - D^dagger; check Frobenius norm = 0 | Exactly zero |
| D gamma + gamma D = 0 | Anticommutation with grading | Compute {D, gamma}; check = 0 | Exactly zero |
| JD - DJ = 0 | Commutation with real structure (epsilon' = +1) | Compute JDJ^{-1} - D (using antilinear J); check = 0 | Exactly zero |
| Moduli space dim at n=1 | Trivial case | H = C^2, all operators are 2x2 | Should give known result (trivially 0 or small) |
| Moduli space dim monotonicity | Dimension should be well-behaved in n | Compute at n=1,2,3,4 | Non-decreasing (generally) |
| D = 0 is always a solution | Zero operator satisfies all constraints | Verify D=0 in moduli space | Always true |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| --- | --- | --- | --- |
| n = 1 (trivial algebra) | A = C, H = C^2 | D moduli space is 1-dimensional (D = [[0, d*], [d, 0]] with d in C, but JD = DJ constrains to d in R) | Direct computation |
| SM spectral triple | Different algebra (A_F = C + H + M_3(C)) | D has 31 real parameters (Yukawa couplings + Majorana mass) | Chamseddine-Connes 2008 |
| Barrett fuzzy sphere | A = M_n(C), V = C^4 (4 gamma matrices) | D parameterized by 3 skew-Hermitian matrices (angular momentum generators) | Barrett 2015 |

### Numerical Validation

| Test | Method | Tolerance | Reference Value |
| --- | --- | --- | --- |
| Constraint rank at n=2 | SVD of constraint matrix | Singular values < 1e-12 are zero | Cross-check with SymPy exact null space |
| Moduli space dimension at n=2 | dim(kernel) | Must be integer | Independent Barrett form computation |
| Sequential product candidate in moduli space | Project candidate onto moduli space; check residual | Frobenius norm < 1e-12 | Either zero (candidate works) or nonzero (identify violated constraint) |

### Red Flags During Computation

- **Moduli space dimension = 0:** This means only D = 0 satisfies all constraints. The spectral triple has no non-trivial Dirac operator. This triggers a backtracking condition (reconsider gamma or J definitions). Check: is this because of the gamma choice? The even condition failure may be related.
- **Moduli space dimension is odd:** This is unusual for real moduli spaces arising from JD = DJ with J^2 = +1. If J acts as complex conjugation in some basis, the moduli space should be a real vector space. An odd dimension is possible but warrants double-checking.
- **Sequential product candidate has imaginary entries:** Under the Barrett isomorphism, L_a - R_a for real a acts on M_n(C). If the candidate D has entries incompatible with self-adjointness, the formulation is wrong.
- **J constraint eliminates ALL within-sector D blocks:** If JD = DJ forces D to have no particle-to-particle or antiparticle-to-antiparticle blocks within the off-diagonal (gamma) structure, this may be physically meaningful (D only mixes sectors through J) but must be checked.

## Common Pitfalls

### Pitfall 1: Antilinearity of J in the JD = DJ constraint

**What goes wrong:** Treating J as a linear operator when computing JD = DJ. Since J is antilinear, J D J^{-1} involves complex conjugation of D's matrix entries: J_matrix conj(D_matrix) J_matrix^{-1} = D_matrix.

**Why it happens:** In the C^{2n^2} representation, J is implemented as J_matrix * complex_conjugation. Forgetting the conjugation gives a linear constraint instead of an antilinear one, typically doubling the moduli space dimension (allowing complex parameters where only real ones are permitted).

**How to avoid:** Always decompose JDJ^{-1} = J_matrix conj(D_matrix) J_matrix^{-1}. In code: `J_matrix @ np.conj(D_matrix) @ np.linalg.inv(J_matrix)`. Alternatively, split D = D_real + i D_imag and impose J_matrix D_real J_matrix^{-1} = D_real and J_matrix D_imag J_matrix^{-1} = -D_imag.

**Warning signs:** Moduli space dimension is twice what Barrett's formula predicts.

**Recovery:** Re-derive the constraint with explicit complex conjugation; recompute the null space.

### Pitfall 2: Basis ordering confusion between gamma eigenspaces and particle/antiparticle sectors

**What goes wrong:** The gamma eigenspaces (H_+, H_-) do NOT align with the particle/antiparticle sectors. H_+ = Sym^2_p + wedge^2_{ap} mixes particle and antiparticle. Getting the basis ordering wrong in the block decomposition gives incorrect sub-blocks of M.

**Why it happens:** The natural basis for H = C^{2n^2} is (particle sector, antiparticle sector). But D gamma = -gamma D requires working in the (H_+, H_-) basis. The change of basis is a permutation matrix that rearranges the particle Sym^2 and wedge^2 components with the antiparticle ones.

**How to avoid:** Explicitly construct the change-of-basis matrix from the (particle, antiparticle) basis to the (H_+, H_-) basis. Verify by checking that gamma is diagonal in the new basis.

**Warning signs:** D gamma + gamma D != 0 after imposing the off-diagonal block structure.

**Recovery:** Recompute the change-of-basis matrix; verify gamma is diag(I, -I) in the new basis.

### Pitfall 3: The sequential product candidate is nonlinear

**What goes wrong:** The sequential product sp(a,b) = sqrt(a) b sqrt(a) defines a map b -> sp(a,b) = sqrt(a) b sqrt(a) that IS linear in b (for fixed a). But the "asymmetry" sp(a,b) - sp(b,a) is NOT linear in either argument because sp(b,a) = sqrt(b) a sqrt(b) involves sqrt(b), which is nonlinear in b.

**Why it happens:** The asymmetry L_a - R_a where L_a(b) = sp(a,b) = sqrt(a) b sqrt(a) and R_a(b) = sp(b,a) = sqrt(b) a sqrt(b) has L_a linear in b but R_a nonlinear in b.

**How to avoid:** The correct linearization is: for a FIXED reference state a in M_n(C)^sa, define D_a(X) = sqrt(a) X sqrt(a) - X (or similar). Alternatively, consider the commutator [a, X] = aX - Xa as the simplest SWAP-odd operator derived from the algebra action. Or consider the "infinitesimal" version: for a near the identity, sp(1+epsilon*h, X) - sp(X, 1+epsilon*h) to first order in epsilon gives a linear operator on X.

**Warning signs:** Attempting to check "D_a in the moduli space" where D_a is a function of both a and X makes no sense as a linear operator on H.

**Recovery:** Fix a specific a (e.g., a = diag(lambda_1, ..., lambda_n)) and compute D_a as a linear map X -> sqrt(a) X sqrt(a). This IS a legitimate linear operator on M_n(C) and can be checked against the moduli space. But note: this gives a FAMILY of D operators (one per a), not a single canonical D. The question is whether any member of this family, or some natural average/contraction, lies in the moduli space.

### Pitfall 4: Confusing within-sector D with cross-sector D

**What goes wrong:** D gamma = -gamma D forces D to be off-diagonal in H_+/H_- basis. But within each gamma eigenspace, there are sub-blocks connecting particle and antiparticle components (e.g., Sym^2_p to wedge^2_{ap} are both in H_+, so M has a block connecting them). JD = DJ provides the constraint relating these sub-blocks.

**Why it happens:** The gamma and sector decompositions are not aligned. The interplay between the two decompositions creates a 4x4 sub-block structure in D.

**How to avoid:** Work with the full 4-component decomposition (Sym^2_p, wedge^2_p, wedge^2_{ap}, Sym^2_{ap}) from the start. Write D as a 4x4 block matrix, then impose gamma (which makes it 2x2 in gamma blocks) and J (which constrains sub-blocks).

## Level of Rigor

**Required for this phase:** Controlled computation with exact verification.

**Justification:** The moduli space parameterization is exact linear algebra. No approximations, no perturbation theory, no truncations. The computation is finite-dimensional and deterministic. The only risk is algebraic error in tracking indices and bases, which is mitigated by SymPy/NumPy verification at n=2,3,4.

**What this means concretely:**

- All constraint equations must be derived symbolically, not just verified numerically
- Moduli space dimension must be exact (integer), not approximate
- The sequential product candidate must be checked exactly (lies in the space or does not; no "approximately in the space")
- Numerical verification at n=2,3,4 must use exact arithmetic (SymPy Rational or integer matrices) where possible; floating-point only as cross-check

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| --- | --- | --- | --- |
| KO-dimension 0 (pre-Barrett) | KO-dimension 6 (post-Barrett 2006) | 2006 (Connes, hep-th/0608226) | Resolves fermion doubling; changes gamma and D constraints |
| Orientability required | Orientability dropped (Cacic 2009) | 2009 | Allows KO-dim 6 finite triples where orientability fails |
| Ad hoc D construction | Systematic moduli space parameterization | Krajewski 1997, Cacic 2009 | All D enumerated, not just specific candidates |
| Pen-and-paper only | Computational verification (Barrett-Glaser, Hessam et al.) | 2016-2025 | Explicit numerical checks at small n; random matrix ensembles |

**Superseded approaches to avoid:**

- **KO-dimension 0 framework:** Gives fermion doubling. Use KO-dimension 6 exclusively.
- **Guessing D without parameterizing moduli space:** This is the anti-pattern the contract explicitly forbids (P4). Always parameterize first.

## Open Questions

1. **Does the even condition failure affect the D moduli space?**
   - What we know: [gamma, pi(a)] != 0 means the spectral triple is not even. D gamma = -gamma D is a condition on D alone (no algebra involved). JD = DJ is a condition on D and J (no algebra involved). So the even condition failure does NOT directly affect the D parameterization.
   - What's unclear: Whether the non-evenness means the moduli space is "too large" (because the algebra does not further constrain D through the even condition) or has the "wrong" structure for the SM.
   - Impact on this phase: Minimal. Parameterize D regardless. The even condition affects Phase 15 (first-order condition) more than Phase 14.
   - Recommendation: Proceed with D parameterization. Note even condition failure in the output. Defer resolution to Phase 15 or a dedicated sub-phase.

2. **What is the correct linearization of L_a - R_a?**
   - What we know: L_a(X) = sqrt(a) X sqrt(a) is linear in X. R_a(X) = sqrt(X) a sqrt(X) is NOT linear in X. The "asymmetry" as written in paper7-spectral-triple-prompt.md is nonlinear.
   - What's unclear: What is the "natural contraction" mentioned in the prompt? Several candidates:
     (a) Fix a, use D_a(X) = sqrt(a) X sqrt(a) as a family of operators parameterized by a
     (b) Use the commutator [a, X] = aX - Xa (simplest SWAP-odd operator from the algebra)
     (c) Use the infinitesimal asymmetry: d/dt|_{t=0} sp(e^{tH}, X) - sp(X, e^{tH}) for some generator H
     (d) Use the "Dirac-type" combination D(X) = sum_i (H_i X + X H_i) for appropriate H_i (Barrett form)
   - Impact on this phase: Critical. The specific form of the candidate determines whether it lies in the moduli space.
   - Recommendation: Test ALL of the above candidates. Start with (b) [a, X] as the simplest. Then test (a) with a = diag(1,0,...,0) and other rank-1 projectors. Then test (d) using Barrett's form.

3. **What is the moduli space dimension at general n?**
   - What we know: For the SM spectral triple (different algebra), D has 31 parameters. For Barrett fuzzy sphere (different V), D has 3 parameters. For our case (A = M_n(C), V = C^2, KO-dim 6), the dimension is unknown.
   - What's unclear: Whether there's a closed-form formula dim(moduli) = f(n).
   - Impact on this phase: The dimension tells us how constrained D is. If dim = 0, the phase fails. If dim is very large, D is underdetermined and the sequential product candidate has more room.
   - Recommendation: Compute at n=2,3,4 first, then look for a pattern. Attempt a general-n formula only if the pattern is clear.

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| --- | --- | --- | --- |
| Moduli space is empty (dim = 0) | gamma or J definition incompatible with any non-trivial D | (a) Try alternative gamma (e.g., gamma = diag(I, -I) sector-swap without P); (b) Try odd spectral triple (drop gamma requirement entirely) | Medium: recompute J constraints with new gamma; redo Phase 13 gamma analysis |
| Sequential product candidate not in moduli space | JD != DJ for the candidate | (a) Identify which constraint fails; (b) Try modified candidate (e.g., symmetrized version, different contraction); (c) Find the D in moduli space closest to the candidate; (d) Find the most naturally motivated D from self-modeling | Low: moduli space already parameterized; just pick a different element |
| Moduli space is trivially large (dim ~ n^4) | J constraint is too weak | The D moduli space is large but the first-order condition (Phase 15) will drastically reduce it; proceed to Phase 15 | None: large moduli space is not a failure, just underdetermined |
| Barrett form incompatible with our J | Our J is non-standard (includes SWAP) | Use Approach 1 (direct block decomposition) exclusively | None: Approach 1 is primary; Barrett is cross-check |

**Decision criteria:** Moduli space emptiness is detected immediately at n=2. If empty at n=2, try alternative gamma before proceeding to n=3,4.

## Sources

### Primary (HIGH confidence)

- [Barrett 2015: "Matrix geometries and fuzzy spaces as finite spectral triples," arXiv:1502.05383](https://arxiv.org/abs/1502.05383) -- General D form for M_n(C) spectral triples; Proposition 3.1 (D parameterization)
- [van Suijlekom 2024: "Noncommutative Geometry and Particle Physics," 2nd ed., Ch. 3-4](http://www.waltervansuijlekom.nl/wp-content/uploads/2024/02/ncgphysics2nd.pdf) -- Finite spectral triple D construction; block decomposition method
- [Cacic 2009: "Moduli spaces of Dirac operators for finite spectral triples," arXiv:0902.2068](https://arxiv.org/abs/0902.2068) -- Moduli space theory; generalized axioms without orientability
- [Chamseddine-Connes 2008: "Why the Standard Model," arXiv:0706.3688](https://arxiv.org/abs/0706.3688) -- SM D has 31 parameters; classification theorem
- [Phase 13 results: derivations/07-order-zero-condition.md, derivations/07-bimodule-krajewski.md, tests/test_order_zero.py](.) -- Bimodule structure, J/gamma definitions, Barrett isomorphism (all verified)

### Secondary (MEDIUM confidence)

- [Hessam, Khalkhali, Pagliaroli 2025: "Bootstrapping NCG with Dirac Ensembles," arXiv:2512.08694](https://arxiv.org/html/2512.08694) -- Explicit Barrett D formula; computational techniques
- [Barrett-Glaser 2016/2019: "Computing the spectral action for fuzzy geometries," arXiv:1912.13288](https://arxiv.org/abs/1912.13288) -- Explicit D computation; random matrix applications
- [Krajewski 1997: "Classification of finite spectral triples," arXiv:hep-th/9701081](https://arxiv.org/abs/hep-th/9701081) -- Krajewski diagram D rules

### Tertiary (LOW confidence)

- Paper 7 prompt (paper7-spectral-triple-prompt.md) -- Sequential product asymmetry candidate (novel, no literature validation)

## Metadata

**Confidence breakdown:**

- Mathematical framework: HIGH -- Block decomposition of D and linear constraint solving are standard textbook methods (van Suijlekom Ch. 3, Barrett 2015)
- Standard approaches: HIGH -- Approach 1 (block + null space) is exactly how every finite spectral triple D is parameterized in the literature
- Computational tools: HIGH -- SymPy/NumPy are well-tested for this project; matrix sizes are trivial (32x32 max)
- Validation strategies: HIGH -- Multiple cross-checks available (n=1 limit, Barrett form comparison, SymPy vs NumPy)
- Sequential product candidate: LOW -- Novel construction with no literature precedent; the correct linearization is ambiguous; multiple candidate forms exist

**Research date:** 2026-03-22
**Valid until:** Indefinite for the mathematical framework; the sequential product candidate analysis is specific to this project

## Caveats and Alternatives (Self-Critique)

1. **Assumption that might be wrong:** I assume the D moduli space is non-trivial (dim > 0) for our specific (J, gamma) pair. Given the even condition failure, it is possible that the constraints are over-determined and no non-trivial D exists. This is not a theoretical impossibility -- it would mean our gamma choice is incompatible with a non-trivial Dirac operator. The safest approach is to compute the dimension at n=2 first and immediately flag if dim = 0.

2. **Alternative approach I may have dismissed too quickly:** Twisted spectral triples (where JD = epsilon' D J is replaced by a twisted condition J D = epsilon' sigma(D) J for some automorphism sigma) could resolve the even condition failure while preserving a non-trivial D moduli space. However, this adds significant complexity and moves away from the standard NCG framework, so I recommend exploring it only if the standard framework fails.

3. **Limitation I may be understating:** The "correct linearization of L_a - R_a" problem is more serious than it appears. The paper7-spectral-triple-prompt.md describes L_a - R_a as if it were a single operator, but it is actually a family parameterized by a. There is no canonical way to contract this family into a single D without additional structure (e.g., a trace, an integral over a, or a specific choice of a). The phase may need to explore multiple contraction schemes.

4. **Simpler method I might have overlooked:** The commutator [a, -] = L_a - R_a (without square roots) is the simplest SWAP-odd operator from the algebra. Under the Barrett isomorphism, [a, X] = aX - Xa is manifestly odd under transpose (since [a, X]^T = X^T a^T - a^T X^T = -[a^T, X^T]). For a = a^T (symmetric), this gives [a, X]^T = -[a, X^T], so it maps Sym -> Skew and Skew -> Sym. This is the simplest possible candidate and should be tested FIRST.

5. **Potential expert disagreement:** An NCG specialist might insist that the even condition failure must be resolved BEFORE constructing D, since the spectral triple framework requires [gamma, pi(a)] = 0 as an axiom of even spectral triples. The counter-argument is that D can be parameterized independently of the algebra action's evenness, and the even condition is a separate constraint that affects the physical interpretation but not the mathematical parameterization.
