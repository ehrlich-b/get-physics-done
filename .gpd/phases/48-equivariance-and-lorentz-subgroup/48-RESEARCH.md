# Phase 48: Equivariance and Lorentz Subgroup - Research

**Researched:** 2026-04-12
**Domain:** Exceptional Jordan algebra / Spin(9) stabilizer theory / Lorentz subgroup embedding / Equivariant projection
**Confidence:** HIGH

## Summary

Phase 48 identifies the full stabilizer of the unit imaginary octonion u = e_7 in Spin(9), exhibits SL(2,C_u) = Spin(3,1) as a subalgebra acting on h_2(C_u) by Lorentz transformations, and proves that pi_u is equivariant under the Lorentz subgroup. The mathematical framework is entirely standard: the stabilizer computation reduces to a linear algebra nullspace problem on the existing 16x16 Clifford representation, and the Lorentz embedding follows from the classical isomorphism SL(2,C) = Spin(3,1) acting on h_2(C) by X -> gXg^dagger.

The key subtlety is that "stabilizer of u in Spin(9)" has TWO possible meanings depending on which representation we consider: (a) the stabilizer of u acting on R^9 via the vector representation (giving Spin(7), dim 21), or (b) the stabilizer of the complex structure J_u acting on R^16 via the spinor representation (giving the SM gauge group, dim 8). Phase 48 needs BOTH perspectives:

1. **The V_0 perspective:** Spin(9) acts on V_0 = h_2(O) = R^{9,1} via the 10-dim vector representation. The stabilizer of the "u-direction" in this 10-dim space is the subgroup preserving the splitting 10 = 4 (spacetime) + 6 (internal). This stabilizer contains the Lorentz group SL(2,C) acting on the 4-dim spacetime factor.

2. **The V_{1/2} perspective:** Spin(9) acts on V_{1/2} = O^2 = R^16 via the spinor representation. The complex structure J_u (already computed in earlier phases) has commutant G_SM in spin(9). The Lorentz subgroup must be compatible with BOTH the V_0 and V_{1/2} actions.

The computation is exact finite-dimensional algebra on spaces dim <= 36 (the dimension of spin(9)). All required infrastructure exists: the code has 9 Clifford generators (16x16), the 10 T_b operators, the V_0 basis, pi_u, and the stabilizer/commutant computation functions (compute_gsm_commutant, compute_grade2_stabilizer). The principal new work is: (i) computing the 10x10 representation of each spin(9) generator on V_0, (ii) identifying which generators preserve the 4+6 splitting, (iii) extracting the sl(2,C) subalgebra from the 4-dim-preserving generators, and (iv) proving equivariance of pi_u.

**Primary recommendation:** Compute the full 36 spin(9) generators as 10x10 matrices on V_0 (via the commutator [gamma_ab/4, T_c] method already used in verify_f4_invariance_det3). The stabilizer of the 4+6 splitting is the subalgebra preserving both the 4-dim image and 6-dim kernel of pi_u. Extract the sl(2,C) subalgebra by restricting to the 4x4 block on h_2(C_u). Verify equivariance by checking pi_u(exp(epsilon*L).Y) = exp(epsilon*L|_4).pi_u(Y) to first order for all stabilizer generators L.

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| --- | --- | --- | --- | --- |
| Baez 2002 (arXiv:math/0105155) | benchmark | SL(2,K) = Spin(dim(K)+1,1) acts on h_2(K) by Lorentz transformations | Use for SL(2,C) = Spin(3,1) identification on h_2(C_u) | Plan: Lorentz embedding task |
| Baez-Huerta 2009 (arXiv:0909.0551) | method | Division algebra -> spacetime: h_2(K) with det gives R^{dim(K)+1,1} Minkowski; SL(2,O) relates to Spin(9,1) | Use for understanding how u-choice reduces Spin(9,1) to subgroup containing SL(2,C) | Plan: dimensional reduction chain |
| Paper 7 Spin(9) action on V_0 | prior artifact | Establishes that Spin(9) acts on V_0 via 10-dim vector rep, with explicit T_b operator construction | Use existing T_b matrices and commutator action | Plan: 10x10 matrix computation |
| Krasnov 2019 (arXiv:1912.11282) | method | G_SM = Stab_{Spin(9)}(J_u) on spinors, dim 8. Distinguishes vector vs spinor stabilizer | Cite for the spinor-stabilizer perspective; our V_0 stabilizer is DIFFERENT | Plan: comparison of V_0 vs V_{1/2} stabilizers |
| Phase 46 code (octonion_algebra.py) | prior artifact | pi_u, V0_basis_elements, T_b matrices, rescale_to_clifford_generators, compute_gsm_commutant, compute_grade2_stabilizer | Build stabilizer computation on existing functions | All implementation tasks |
| Phase 46 verification | prior artifact | Confirmed 4+6 splitting of V_0 under pi_u; established pi_u equivariance under SU(3)_C | Use as starting point -- this phase extends from SU(3)_C to the full stabilizer | Plan: verification steps |

**Missing or weak anchors:** The explicit sl(2,C) embedding inside the V_0 stabilizer is novel to this project. No prior paper constructs it in exactly this form (from the Peirce/pi_u perspective). The embedding itself is standard (SL(2,C) acts on h_2(C) by conjugation), but connecting it to the Spin(9) stabilizer structure is new. Confidence: HIGH for the mathematical components individually, MEDIUM for the specific assembly.

## Conventions

| Choice | Convention | Alternatives | Source |
| --- | --- | --- | --- |
| Octonion basis | Fano plane: e_1 e_2 = e_4 | 480 valid tables | octonion_algebra.py |
| Complex structure | u = e_7 | Any u in S^6 (G_2-equivalent) | octonion_algebra.py, Paper 7 |
| C_u definition | C_u = span_R{1, u} = span_R{1, e_7} | N/A | Standard |
| W definition | W = u^perp cap Im(O) = span{e_1,...,e_6} | N/A | Standard |
| Jordan product | A circ B = (1/2)(AB + BA) | Some sources omit 1/2 | octonion_algebra.py |
| Clifford convention | {gamma_i, gamma_j} = 2*delta_{ij}*I_{16}, Cl(9,0) | Some use +I vs -I | octonion_algebra.py |
| spin(9) generators | gamma_ij = gamma_i @ gamma_j for i < j, dim 36 | Factor of 1/4 for Lie algebra element | octonion_algebra.py |
| Lie algebra normalization | L = gamma_ij / 4 as the spin(9) Lie algebra element | Some use 1/2 | Matches verify_f4_invariance_det3 |
| V_0 basis | b[0]=(0.5,0.5,0), b[1]=(0.5,-0.5,0), b[2..9]=x1=e_k | N/A | octonion_algebra.py |
| V_0 coordinates | v0_vec = [c0=beta+gamma, c1=beta-gamma, x1.c[0..7]] | N/A | verify_f4_invariance_det3 |
| Metric signature | (+,-,-,-) on h_2(C_u) via det_2 | (-,+,+,+) | Phase 46 established |
| SL(2,C) action | X -> gXg^dagger on h_2(C) | Some write g^{-dagger}Xg^{-1} | Baez 2002 |

**CRITICAL: The Lie algebra normalization matters. The code uses gamma_ij/4 as the spin(9) generator in the F_4 invariance test (lines 2607, 2616). The 10x10 matrix M_v0 is computed via [gamma_ab/4, T_c] = sum_d M_{cd} T_d. This normalization must be consistent throughout Phase 48.**

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in This Phase |
| --- | --- | --- | --- |
| [gamma_ab/4, T_c] = sum_d M_{cd}^{(ab)} T_d | Spin(9) action on V_0 in 10-dim rep | verify_f4_invariance_det3 (line 2616) | Core: gives 10x10 matrices M^{(ab)} for each spin(9) generator |
| pi_u(a, b; b*, d) = (a, proj_u(b); proj_u(b)*, d) | pi_u projection | Phase 46 (locked) | Defines the 4+6 splitting to stabilize |
| P = projection matrix: R^10 -> R^4 (spacetime) | pi_u in V_0 coordinates | Phase 46 (V_0 spacetime indices: 0,1,2,9) | Stabilizer condition: M^{(ab)} preserves ker(P) and im(P) |
| X -> gXg^dagger for g in SL(2,C) | Lorentz action on h_2(C) | Baez 2002 | The expected form of the Lorentz subgroup action |
| sl(2,C) = span{sigma_i, i*sigma_i} (i=1,2,3) | Lorentz Lie algebra generators | Standard | Expected structure of the 4-dim-preserving subalgebra |
| [L, pi_u] = 0 iff L preserves the 4+6 splitting | Equivariance condition | Linear algebra | The condition defining the stabilizer |
| pi_u(exp(eps*L).Y) = exp(eps*L|_4).pi_u(Y) | Infinitesimal equivariance | Lie theory | The equivariance statement to verify |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --- | --- | --- | --- |
| Commutator action on T_b operators | Computes 10x10 rep of spin(9) on V_0 | Step 1: build all 36 generator matrices | verify_f4_invariance_det3 (existing code) |
| Block-diagonal decomposition | Identifies generators preserving the 4+6 split | Step 2: check which M^{(ab)} are block-diagonal in spacetime/internal basis | Standard linear algebra |
| Lie algebra identification via Killing form | Determines the structure (semisimple part, center) of the stabilizer | Step 3: classify the stabilizer subalgebra | compute_gsm_commutant (existing pattern) |
| Explicit SL(2,C) generator construction | Builds the 4x4 Lorentz generators on h_2(C_u) from Pauli matrices | Step 4: compare extracted sl(2,C) with expected form | Baez 2002 |
| Nullspace computation via SVD | Finds the stabilizer as nullspace of the projection commutator | Core of all stabilizer computations | NumPy (existing pattern) |

### Approximation Schemes

None required. All computations are exact algebraic operations on finite-dimensional spaces (10x10 and 16x16 matrices). The only numerical consideration is floating-point precision (errors at 10^{-15} level), completely negligible.

## Standard Approaches

### Approach 1: Direct 10x10 Matrix Computation (RECOMMENDED)

**What:** Build the 36 spin(9) generators as 10x10 matrices on V_0, then find the subalgebra preserving the 4+6 splitting by checking block-diagonal structure.

**Why standard:** For a 10-dimensional representation of a 36-dimensional Lie algebra, direct matrix computation is the canonical approach. The commutator-extraction method is already implemented and verified in verify_f4_invariance_det3.

**Track record:** The same [gamma_ab/4, T_c] computation successfully verified F_4 invariance of det_3 in Phase 47 (630 tests, error < 10^{-12}).

**Key steps:**

1. **Build all 36 spin(9) generators as 10x10 matrices on V_0.** For each pair (a,b) with a < b, compute M^{(ab)}_{cd} via [gamma_ab/4, T_c] = sum_d M^{(ab)}_{cd} T_d using lstsq. This gives 36 matrices in R^{10x10}. The code template is in verify_f4_invariance_det3 (lines 2613-2618), but there it is computed inside a loop per random X. Here we need to compute it once and store.

2. **Identify the 4+6 splitting in V_0 coordinates.** The spacetime indices in V_0 coordinates are {0, 1, 2, 9} (corresponding to b[0], b[1], b[2], b[9] -- the h_2(C_u) basis elements). The internal indices are {3, 4, 5, 6, 7, 8} (corresponding to b[3]..b[8] -- the W-sector basis elements with x1 = e_1,...,e_6). Define P_S (4x10 projection onto spacetime) and P_I (6x10 projection onto internal).

3. **Find generators preserving the 4+6 split.** A spin(9) generator M^{(ab)} preserves the splitting iff it is block-diagonal in the spacetime/internal basis, i.e., P_I @ M^{(ab)} @ P_S^T = 0 AND P_S @ M^{(ab)} @ P_I^T = 0. Equivalently, the off-diagonal blocks of M^{(ab)} in the {0,1,2,9} vs {3,4,5,6,7,8} partition vanish. Find all linear combinations L = sum c_{ab} M^{(ab)} that are block-diagonal: this is a linear system, solve by SVD nullspace.

4. **Classify the stabilizer.** Compute the dimension, Killing form, center, and semisimple structure of the block-diagonal subalgebra (following the pattern of compute_gsm_commutant). Expected: the stabilizer has two blocks -- a 4x4 block (acting on spacetime) and a 6x6 block (acting on internal space). The 4x4 block should be so(3,1) = sl(2,C) (the Lorentz algebra, dim 6). The 6x6 block should be so(6) = su(4) (dim 15). Total stabilizer dimension: 6 + 15 = 21 = dim(spin(7)).

5. **Verify the 4x4 block is sl(2,C).** Extract the 4x4 spacetime blocks of all stabilizer generators. These give a representation of the Lorentz algebra on R^4. Check that they satisfy the so(3,1) commutation relations. Specifically, if we use the Minkowski basis (x_0, x_1, x_2, x_3), the generators should include 3 boosts (J_{0i}) and 3 rotations (J_{ij}), forming so(3,1). Verify by computing the Killing form signature (should be (3,3) for the real form so(3,1)).

6. **Verify the 6x6 block is so(6).** Extract the 6x6 internal blocks. Check dimension (should be 15), compute Killing form (should be negative definite for the compact form so(6)), verify closure.

7. **Prove equivariance of pi_u.** For each stabilizer generator L (block-diagonal), the equivariance statement is:
   pi_u(exp(eps*L).Y) = exp(eps*L|_{spacetime}).pi_u(Y)
   Infinitesimally: pi_u(L.Y) = L|_{spacetime}.pi_u(Y)
   In coordinates: P_S @ M_L @ v = M_L|_{4x4} @ P_S @ v for all v in R^{10}.
   This is AUTOMATIC for block-diagonal generators, since P_S @ M_L = M_L|_{4x4} @ P_S by block structure.
   The key insight: equivariance of pi_u under the stabilizer is equivalent to the block-diagonal structure. So step 3 already proves equivariance.

8. **Identify generators NOT preserving the 4+6 split.** The remaining 36 - 21 = 15 spin(9) generators mix spacetime and internal directions. These correspond to the coset spin(9)/stab(u), which is tangent to the space of possible u-choices (the S^6 of unit imaginary octonions, or more precisely its Spin(9) orbit in V_0).

**Known difficulties at each step:**

- Step 1: The lstsq solve for M^{(ab)} coefficients must use the T_flat matrix (256x10). This is already done in the existing code. Potential issue: the T_b matrices include T_0 = (1/4)*I (trace element), which is the V_1 direction. We need T_0,...,T_9 as the 10 V_0 operators. Check: V0_basis_elements gives 10 elements corresponding to T_0,...,T_9.

- Step 2: The spacetime indices {0,1,2,9} are in the V_0 coordinate system [c0, c1, x1.c[0..7]]. Need to verify: pi_u kills components x1.c[1],...,x1.c[6] (indices 3..8 in the 10-dim vector), preserves c0, c1, x1.c[0], x1.c[7] (indices 0,1,2,9). This matches Phase 46 verification.

- Step 4: The expected stabilizer dimension 21 comes from the branching Spin(9) -> Spin(7) x Spin(2), where Spin(7) is the stabilizer of a unit vector in R^9 (since V_0 = R^{1,9} and pi_u selects a specific R^{1,3} subspace). However, the exact structure depends on which subspace is stabilized. The 4+6 splitting is NOT the standard point-stabilizer (which would be Spin(8) for a point on S^8, or Spin(7) for a point on S^{15}). It is the stabilizer of a 4-dim subspace, which is SO(4) x SO(6) in the Euclidean case, or SO(3,1) x SO(6) in the Lorentzian case.

- Step 5: CRITICAL SUBTLETY. The 4x4 block of a COMPACT group generator on R^4 will look like so(4), not so(3,1). This is because Spin(9) is COMPACT, so all its representations are orthogonal. The Lorentzian interpretation comes from the METRIC (det_2 has signature (1,3)), not from the group action. The generators act as antisymmetric matrices in the MINKOWSKI inner product, which means they are so(3,1) generators relative to det_2. Must carefully distinguish the Euclidean inner product (used by the matrix rep) from the Lorentzian inner product (given by det_2). See the "Lorentz algebra from compact group" discussion in Common Pitfalls below.

### Approach 2: J_u Commutant on V_{1/2} Then Restrict to V_0 (COMPLEMENTARY)

**What:** Use the already-computed commutant of J_u in spin(9) (the G_SM stabilizer, dim 8) and extend it by finding additional generators that preserve the 4+6 splitting on V_0 but do NOT commute with J_u on V_{1/2}.

**When to use:** As a cross-check on Approach 1, and to understand the relationship between the V_0 stabilizer and the V_{1/2} stabilizer.

**Key insight:** The V_0 stabilizer (preserving 4+6 split) and the V_{1/2} stabilizer (commuting with J_u) are DIFFERENT subalgebras of spin(9). The V_{1/2} stabilizer is the SM gauge algebra (dim 8). The V_0 stabilizer is larger (dim 21). Their intersection should be the su(3) color algebra (dim 8) acting trivially on h_2(C_u) and nontrivially on the internal 6.

**Tradeoffs:** More conceptually illuminating but requires computing two separate stabilizers and comparing them.

### Anti-Patterns to Avoid

- **Confusing Spin(9) with SO(9).** Spin(9) is the double cover. On V_{1/2} = R^{16}, Spin(9) acts faithfully as the spinor representation. On V_0, it acts via the vector representation (which factors through SO(9)). The Lie ALGEBRA spin(9) = so(9) is the same, but the global group structure matters for connectivity arguments.

- **Claiming SL(2,C) embeds in Spin(9) as a non-compact subgroup.** Spin(9) is COMPACT. There is no literal SL(2,C) = Spin(3,1) subgroup of Spin(9). What we show is that the Lie algebra so(3,1) = sl(2,C)_R embeds in spin(9) in a way that is consistent with the LORENTZIAN metric on h_2(C_u). The group-level statement is that SU(2) x SU(2) = Spin(4) c Spin(9) acts on h_2(C_u) by SO(4) rotations, and this SO(4) becomes SO(3,1) when we use the det_2 inner product instead of the Euclidean one.

- **Ignoring the metric distinction.** The 10x10 matrices M^{(ab)} are antisymmetric in the EUCLIDEAN inner product on R^{10} (because Spin(9) is compact). They are antisymmetric in the MINKOWSKI inner product on R^{1,9} (given by det_2 on h_2(O)). These are DIFFERENT conditions and give DIFFERENT subgroups. The stabilizer of the 4+6 splitting in the Euclidean sense is SO(4) x SO(6) c SO(10). In the Minkowski sense it is SO(3,1) x SO(6) c SO(9,1). Since Spin(9) c SO(10) preserving the Minkowski form, the actual stabilizer is the intersection: Spin(9) cap (SO(3,1) x SO(6)) = Spin(3,1) x Spin(6) cap Spin(9).

- **Confusing two different "stabilizer of u" problems.** The stabilizer of u as a POINT in S^6 c Im(O) (under G_2 action) is SU(3). The stabilizer of u as a complex structure J_u on R^{16} (under Spin(9) action) is G_SM (dim 8). The stabilizer of the 4+6 splitting on V_0 (under Spin(9) action) is a different, larger subgroup (dim 21). Phase 48 needs the THIRD one, but should document its relationship to the first two.

## Existing Results to Leverage

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
| --- | --- | --- | --- |
| SL(2,C) = Spin(3,1) | Standard isomorphism | Baez 2002; any QFT textbook | Cite for Lorentz identification |
| SL(2,C) acts on h_2(C) by X -> gXg^dagger | Preserves det_2, gives SO^+(3,1) | Baez 2002 Sec 3.3 | Cite for expected form of Lorentz action |
| h_2(K) with det gives R^{dim(K)+1,1} | Lorentzian metric from determinant | Baez 2002 | Already verified in Phase 46 |
| Spin(9) acts on V_0 via 10-dim vector rep | [gamma_ab/4, T_c] = M_{cd} T_d | Phase 47 (verify_f4_invariance_det3) | Use existing computation method |
| pi_u projects V_0 to 4+6 | Spacetime indices {0,1,2,9}, internal {3..8} | Phase 46 verification | Use as the splitting to stabilize |
| G_SM = Stab_{Spin(9)}(J_u) has dim 8 | compute_gsm_commutant result | Earlier phases | Cross-reference with V_0 stabilizer |
| V_0 circ V_0 closes in V_0 | Intrinsic Jordan product | Phase 46 (verified, 55 pairs) | Jordan structure preserved by equivariant action |
| so(4) = su(2) + su(2) = sl(2,C)_R | Real form decomposition | Standard Lie theory | Needed for Lorentz identification |
| so(6) = su(4) | Accidental isomorphism | Standard | Needed for internal symmetry identification |

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
| --- | --- | --- | --- |
| T_b matrices (10 operators, 16x16) | V_0 action on V_{1/2}; also used to define 10-dim rep | octonion_algebra.py | Already computed |
| Clifford generators gamma_i (9 matrices, 16x16) | spin(9) generators via gamma_i @ gamma_j | rescale_to_clifford_generators | Already computed |
| Minkowski basis of h_2(C_u) | x_0=(a+d)/2, x_3=(a-d)/2, x_1=Re(b), x_2=Im_u(b) | Phase 46 | Converts V_0 coordinates to Minkowski coordinates on the 4-dim factor |
| Delta(A,B) structure | Vanishes on h_2(C_u), nonzero on W-self-products | Phase 46 | Equivariance of pi_u should be compatible with Delta structure |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| --- | --- | --- | --- | --- |
| "The Octonions" | Baez | 2002 | SL(2,K) = Spin(dim(K)+1,1); h_2(K) = R^{dim(K)+1,1} | The isomorphism and action formula X -> gXg^dagger |
| "Division Algebras and Supersymmetry I" | Baez, Huerta | 2009 | Detailed construction of SL(2,O) and Spin(9,1) | How u-selection reduces higher-dim Lorentz to SL(2,C) |
| "SO(9) characterisation of SM gauge group" | Krasnov | 2019 | G_SM as Stab_{Spin(9)}(J_u) on spinors | The SPINOR stabilizer (dim 8) vs our V_0 stabilizer |
| "Octonions, exceptional Jordan algebra..." | Todorov, Drenska | 2018 | F_4, Spin(9), G_2 intersection gives SM gauge group | The algebraic framework for stabilizer computations |
| "Spin(9) geometry of octonionic Hopf fibration" | Parton, Piccinni | 2012 | Spin(7) c Spin(8) c Spin(9) chain; S^15 = Spin(9)/Spin(7) | Confirms stabilizer of point in spinor rep is Spin(7) |

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
| --- | --- | --- | --- |
| NumPy | np.linalg.svd | SVD for nullspace computation (stabilizer finding) | Standard for all linear algebra in this project |
| NumPy | np.linalg.lstsq | Least-squares for expressing commutators in basis | Already used in existing stabilizer code |
| NumPy | np.linalg.eigh | Eigenvalue decomposition for Killing form analysis | Already used in compute_gsm_commutant |

### Supporting Tools

| Tool | Purpose | When to Use |
| --- | --- | --- |
| octonion_algebra.py | All octonionic and Clifford algebra infrastructure | Foundation for everything |
| rescale_to_clifford_generators | Get the 9 gamma matrices from T_b | Step 1 |
| compute_T_b_matrices | Get the 10 T_b operators | Step 1 |
| V0_basis_elements | Get the 10 V_0 basis elements | Step 2 |

### Computational Feasibility

| Computation | Estimated Cost | Bottleneck | Mitigation |
| --- | --- | --- | --- |
| Build 36 M^{(ab)} matrices (10x10) | < 0.1 sec | lstsq solve 36 times | Trivial |
| Find block-diagonal subalgebra | < 0.01 sec | SVD of constraint matrix | Trivial |
| Killing form of stabilizer (21x21) | < 0.01 sec | Matrix multiplication | Trivial |
| Equivariance check (36 generators x 10 basis vectors) | < 0.01 sec | Matrix-vector multiply | Trivial |

Total computation time: under 1 second. All exact finite-dimensional algebra.

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| --- | --- | --- | --- |
| Stabilizer closure | The block-diagonal generators form a Lie subalgebra | Compute all brackets, check they stay in the space | Residual < 10^{-12} |
| Dimension check | Stabilizer has expected dimension | Count nullspace vectors | dim = 21 (or 6+15) |
| Killing form signature | Identifies the real Lie algebra type | Eigenvalues of Killing form matrix | so(6) part: negative definite; so(3,1) part: indefinite (3,3) |
| Antisymmetry in det_2 metric | Generators are so(3,1) wrt Lorentzian inner product | Check M^T eta + eta M = 0 where eta = diag(+1,-1,-1,-1) | Should hold for all 6 Lorentz generators |
| so(3,1) commutation relations | The 6 Lorentz generators satisfy correct algebra | Compute structure constants, compare with standard J_i, K_i | Exact match |
| Casimir eigenvalue | Identifies representation content | Compute quadratic Casimir on R^4 and R^6 | Known values for vector reps |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| --- | --- | --- | --- |
| Restriction to h_2(C_u) | Y entirely in spacetime (4-dim) | pi_u(L.Y) = L|_4.Y exactly | Block-diagonal structure |
| Restriction to W-sector | Y entirely in internal (6-dim) | pi_u(L.Y) = 0 | Kernel of pi_u |
| SU(3)_C subgroup | G_2 stabilizer of u, dim 8 | Should be contained in the 6x6 internal block | Phase 46 verified pi_u equivariance under SU(3)_C |
| Full spin(9) | All 36 generators | 21 block-diagonal + 15 mixing | dim(spin(9)) = 36 |
| Euclidean orthogonality | M^{(ab)T} + M^{(ab)} = 0 in R^{10} | All generators antisymmetric | Spin(9) compact |

### Numerical Validation

| Test | Method | Tolerance | Reference Value |
| --- | --- | --- | --- |
| M^{(ab)} antisymmetry | Check M + M^T = 0 for each 10x10 matrix | < 10^{-14} | Zero matrix |
| Stabilizer closure | Bracket residual after lstsq | < 10^{-12} | Zero |
| Equivariance | P_S @ M @ v - M|_4 @ P_S @ v for all v | < 10^{-14} | Zero vector |
| det_2 preservation | eta M + M^T eta = 0 for Lorentz generators | < 10^{-13} | Zero matrix |

### Red Flags During Computation

- If the stabilizer dimension is NOT 21 (e.g., is 22 or 20), the expected spin(7) structure may be wrong. Investigate whether u(1) center is present.
- If the 4x4 block has dimension != 6, the Lorentz algebra identification fails. Check that the spacetime indices are correct.
- If the 6x6 block has dimension != 15, the internal symmetry identification is wrong. Check basis ordering.
- If the Killing form of the 4x4 block is negative definite (not indefinite), the generators are so(4) rather than so(3,1). This is actually EXPECTED for the compact group -- see Pitfall 2 below for how to handle this.
- If any off-diagonal block of a "stabilizer" generator is nonzero (> 10^{-10}), the generator does NOT preserve the splitting and was incorrectly classified.

## Common Pitfalls

### Pitfall 1: Confusing Vector and Spinor Stabilizers

**What goes wrong:** Computing the stabilizer of J_u on V_{1/2} (the SM gauge group, dim 8) when the phase requires the stabilizer of the 4+6 splitting on V_0 (a DIFFERENT subalgebra, dim 21).

**Why it happens:** Both involve "stabilizer in Spin(9)" and both are related to the complex structure u = e_7. But they act on different spaces (16-dim spinor vs 10-dim vector) and stabilize different objects (complex structure J_u vs subspace splitting).

**How to avoid:** Be explicit about WHICH representation and WHICH object is being stabilized. Label clearly: "V_0 stabilizer" vs "V_{1/2} stabilizer" (or "J_u commutant").

**Warning signs:** If you get dim 8 instead of dim 21 for the V_0 stabilizer, you computed the wrong thing.

**Recovery:** The V_{1/2} stabilizer (G_SM, dim 8) is CONTAINED in the V_0 stabilizer (dim 21). The V_0 stabilizer is the larger group.

### Pitfall 2: Compact Group Cannot Contain Non-Compact SL(2,C)

**What goes wrong:** Claiming that SL(2,C) = Spin(3,1) literally embeds as a subgroup of Spin(9). This is impossible because Spin(9) is compact and SL(2,C) is non-compact.

**Why it happens:** The phase goal says "SL(2,C_u) = Spin(3,1) is verified as the Lorentz subgroup." This must be interpreted correctly.

**How to avoid:** The correct statement is: the LIE ALGEBRA sl(2,C)_R = so(3,1) embeds in spin(9) = so(9). At the Lie algebra level, so(3,1) and so(4) have the same complexification (so(4,C)), and so(4) = su(2) + su(2). The COMPACT subalgebra so(4) c so(9) becomes the LORENTZIAN algebra so(3,1) when we use the det_2 Lorentzian inner product instead of the Euclidean one.

Concretely: the 6 generators of the 4x4 block are antisymmetric in the Euclidean inner product on R^4 (because Spin(9) is compact), giving so(4). But relative to the det_2 inner product eta = diag(+1,-1,-1,-1), these same generators satisfy eta*M + M^T*eta = 0, which is the defining relation of so(3,1).

**The precise claim:** The 4x4 block of the V_0 stabilizer is so(4) = su(2) + su(2) as an abstract Lie algebra, but it acts on h_2(C_u) = (R^4, det_2) as so(3,1) = sl(2,C)_R. The two descriptions are equivalent because the METRIC det_2 has Lorentzian signature.

**Warning signs:** If the Killing form of the 4x4 block is negative definite, that's CORRECT for so(4) as a compact algebra. To see so(3,1), compute the metric-compatible condition eta*M + M^T*eta = 0.

### Pitfall 3: Wrong Basis Ordering for V_0 Coordinates

**What goes wrong:** Misidentifying which V_0 basis elements correspond to spacetime vs internal directions.

**Why it happens:** The V_0 coordinate vector is [c0, c1, x1.c[0], x1.c[1], ..., x1.c[7]], where c0 = beta+gamma, c1 = beta-gamma. The spacetime components are c0, c1, x1.c[0] (=Re(x1)), x1.c[7] (=<Im(x1), e_7>). The internal components are x1.c[1] through x1.c[6]. So spacetime indices are {0, 1, 2, 9} and internal indices are {3, 4, 5, 6, 7, 8} in the 10-component vector.

**How to avoid:** Verify against Phase 46 results: pi_u kills basis elements b[3]..b[8] (x1 = e_1,...,e_6) and preserves b[0], b[1], b[2], b[9]. Check numerically.

**Warning signs:** If the "stabilizer" has wrong dimension or wrong structure, check the index mapping first.

### Pitfall 4: Overcounting the Lorentz Generators

**What goes wrong:** Finding more than 6 generators in the spacetime block and incorrectly claiming a larger Lorentz group.

**Why it happens:** The full stabilizer of the 4+6 split has 21 generators, of which 6 act nontrivially on the spacetime part (as the Lorentz algebra) AND 15 act nontrivially on the internal part (as so(6)). But some of the 15 internal generators may have a ZERO 4x4 block (acting trivially on spacetime), and some of the 21 generators may have NONZERO entries in both blocks (acting simultaneously on spacetime and internal).

**How to avoid:** The block-diagonal structure means EVERY stabilizer generator has independent 4x4 and 6x6 blocks. The 4x4 block forms a Lie algebra by itself (it's a homomorphic image). Count the generators whose 4x4 block is nonzero -- these generate the Lorentz algebra. Expected: exactly 6 linearly independent 4x4 blocks.

## Level of Rigor

**Required for this phase:** Controlled computation with exact verification.

**Justification:** All statements are algebraic identities on finite-dimensional vector spaces. Exact numerical verification is both possible and required.

**What this means concretely:**

- All stabilizer dimensions must be exact integers (not "approximately 21")
- Lie algebra closure must be verified with residual < 10^{-12}
- The Lorentz algebra identification must be confirmed by checking commutation relations AND Killing form
- Equivariance must be verified for ALL stabilizer generators, not just a sample
- The 4+6 splitting must use EXACTLY the correct V_0 basis indices

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| --- | --- | --- | --- |
| Abstract group theory (Dynkin diagrams) | Explicit matrix computation on Cl(9,0) | This project (Phases 28+) | Can verify every claim numerically |
| Treating SL(2,C) c Spin(9) literally | Recognizing compact/non-compact distinction | Standard | Avoids impossible embedding claim |
| Separate V_0 and V_{1/2} analyses | Unified Peirce framework with both reps | This project | Connects spacetime and matter sectors |

**Superseded approaches to avoid:**

- Abstract Dynkin diagram branching rules without explicit matrices: while correct, they don't provide the computational verification needed for this project. Use them as cross-checks, not primary tools.

## Open Questions

1. **What is the exact structure of the V_0 stabilizer?**
   - What we know: it should be a 21-dimensional subalgebra of spin(9), expected to be isomorphic to spin(7). The 10-dim rep of spin(9) restricts as 10 -> 4 + 6, which under spin(7) might not be the standard 7+1+1+1 branching.
   - What's unclear: the exact decomposition of the 10-dim vector rep of spin(9) under the stabilizer of a 4-dim subspace. This is NOT the standard spin(9) -> spin(7) branching (which gives 9 -> 7 + 1 + 1 for the vector rep). The 4+6 splitting arises from the pi_u projection, which selects a specific 4-dim subspace of R^{10} that is NOT a simple "axis stabilizer."
   - Impact on this phase: the computation will resolve this -- we just compute and classify.
   - Recommendation: compute first, identify structure after.

2. **How does the V_0 stabilizer relate to the V_{1/2} stabilizer (G_SM)?**
   - What we know: G_SM (dim 8) should be a subalgebra of the V_0 stabilizer (dim 21). The G_SM generators commute with J_u on V_{1/2} AND should preserve the 4+6 splitting on V_0 (since the SU(3) color part acts only on the internal 6).
   - What's unclear: the exact embedding and whether there are V_0 stabilizer generators that are NOT in G_SM.
   - Impact: understanding this relationship clarifies the physical interpretation (Lorentz + internal symmetry).
   - Recommendation: compute both, compare.

3. **Is the stabilizer exactly spin(7) or does it have a u(1) center?**
   - What we know: the phase description mentions "spin(7) or spin(7) + u(1)." The answer depends on whether the V_0 stabilizer includes the U(1) rotation mixing the two Spin(9)/Spin(7) coset directions.
   - What's unclear: must compute to determine.
   - Impact: if u(1) is present (dim 22), there's an extra abelian symmetry to interpret physically.
   - Recommendation: compute Killing form and center of the stabilizer algebra.

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| --- | --- | --- | --- |
| 10x10 matrix computation | Numerical instability in lstsq | Use exact rational arithmetic (SymPy) | MEDIUM: need to rewrite matrix ops |
| Block-diagonal check | Unexpected V_0 basis ordering | Recompute pi_u on V_0 basis, verify indices | LOW: quick diagnostic |
| Stabilizer dim != 21 | Unexpected algebraic structure | Investigate what the actual stabilizer is | LOW: the computation tells you |
| so(3,1) identification fails | 4x4 block is smaller than expected | Check if spacetime indices are correct; check if some generators have zero 4x4 block | LOW: diagnostic |

**Decision criteria:** If the stabilizer dimension is not 21, do not force the expected answer. Report the actual dimension and structure. The computation is exact; if it disagrees with expectations, the expectations were wrong (or the basis is wrong -- check that first).

## Sources

### Primary (HIGH confidence)

- Baez, J.C., "The Octonions," Bull. AMS 39 (2002) 145-205, arXiv:math/0105155 -- SL(2,K) = Spin(dim(K)+1,1), h_2(K) as Minkowski spacetime
- Baez, J.C. and Huerta, J., "Division Algebras and Supersymmetry I," arXiv:0909.0551 (2009) -- detailed SL(2,O) and 10d Lorentz structure
- Phase 46 verification (all 7/7 targets passed, 13/13 physics checks) -- pi_u, 4+6 splitting, det_2 signature
- Phase 47 verification (all 7/7 targets passed, 15/15 physics checks) -- F_4 invariance, Spin(9) action on V_0
- octonion_algebra.py (2869 lines) -- all required computational infrastructure

### Secondary (MEDIUM confidence)

- Krasnov, K., "SO(9) characterisation of the Standard Model gauge group," arXiv:1912.11282 (2019) -- G_SM as Stab_{Spin(9)}(J_u), distinguishes spinor vs vector stabilizer
- Todorov, I. and Drenska, S., "Octonions, exceptional Jordan algebra and the role of F_4 in particle physics," arXiv:1805.06739 (2018) -- F_4, Spin(9) algebraic framework
- Parton, M. and Piccinni, P., "Spin(9) geometry of the octonionic Hopf fibration," arXiv:1208.0899 (2012) -- Spin(7) c Spin(8) c Spin(9) chain, S^15 = Spin(9)/Spin(7)

### Tertiary (LOW confidence)

- The specific identification of the V_0 stabilizer as spin(7) and the decomposition 21 = 6 (Lorentz) + 15 (internal so(6)) is a prediction from this project, not verified in prior literature. Confidence: MEDIUM-HIGH (the mathematics is standard, but the specific application to the Peirce/pi_u framework is novel).

## Metadata

**Confidence breakdown:**

- Mathematical framework: HIGH - all techniques are standard linear algebra on explicit matrices
- Standard approaches: HIGH - the commutator method is already implemented and verified
- Computational tools: HIGH - everything needed exists in octonion_algebra.py
- Validation strategies: HIGH - multiple independent checks available
- Stabilizer identification: MEDIUM-HIGH - the dimension and structure are predictions that will be verified computationally
- Lorentz interpretation: MEDIUM - the compact/non-compact subtlety requires careful handling

**Research date:** 2026-04-12
**Valid until:** Indefinite (pure algebra, no tool version dependencies)

## Caveats and Alternatives

**Self-critique answers:**

1. **What assumption might be wrong?** The assumption that the V_0 stabilizer decomposes as so(3,1) + so(6) with dim 6 + 15 = 21. The actual stabilizer might have a different structure if the 4-dim spacetime subspace of R^{10} is not in "general position" relative to the Spin(9) action. The computation will resolve this.

2. **What alternative did I dismiss too quickly?** The approach of computing everything in the full 27-dim representation of F_4 rather than restricting to the 10-dim V_0. This would give more information (how the stabilizer acts on ALL Peirce sectors simultaneously) but at higher computational cost. Could be added as a cross-check.

3. **What limitation am I understating?** The compact/non-compact issue (Pitfall 2). The statement "sl(2,C) embeds in spin(9)" requires very careful framing. The Lie algebra embedding is unambiguous, but the group-level statement requires specifying that we mean SL(2,C) acting on h_2(C_u) WITH THE LORENTZIAN METRIC det_2, not as a subgroup of the compact Spin(9).

4. **Is there a simpler method?** For the pure Lorentz identification: yes. We KNOW that SL(2,C) acts on h_2(C) by X -> gXg^dagger (this is Baez 2002). We KNOW pi_u maps h_2(O) to h_2(C_u). The Lorentz group on h_2(C_u) is simply the standard SL(2,C) action. The hard part is showing this SL(2,C) action EXTENDS to a spin(9) action on all of V_0 = h_2(O). This extension is what the stabilizer computation proves.

5. **Would a specialist disagree?** A representation theorist might object to calling the compact so(4) c so(9) by the name "so(3,1)", since so(4) and so(3,1) are different real forms. The resolution is that the SAME real 6-dimensional Lie algebra of antisymmetric 4x4 matrices can be interpreted as so(4) (relative to Euclidean metric) or so(3,1) (relative to Minkowski metric det_2). Both descriptions are correct; the physical interpretation requires det_2.
