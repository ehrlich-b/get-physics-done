# Phase 28: Peirce Verification and V_0 Channel Exploration - Research

**Researched:** 2026-03-29
**Domain:** Exceptional Jordan algebra h_3(O) / Peirce decomposition / Octonion arithmetic / Spin(9) representation theory
**Confidence:** HIGH

## Summary

Phase 28 is a computational verification phase with two objectives: (1) confirm the V_1 = R bottleneck by explicitly computing the 16x16 matrix for L_{E_{11}} on V_{1/2} = R^16, and (2) fully characterize the V_0 = h_2(O) channel by computing all 10 Peirce operators T_b: V_{1/2} -> V_{1/2} for b in V_0 and searching for J^2 = -Id in their span.

The mathematical framework is entirely standard Jordan algebra theory applied to the Albert algebra h_3(O). The Peirce decomposition h_3(O) = V_1(1) + V_{1/2}(16) + V_0(10) under the rank-1 idempotent E_{11} is textbook material (Baez 2002 Sec. 3.4, McCrimmon 2004 Ch. 17). The Peirce multiplication rules dictate V_0 . V_{1/2} subset V_{1/2} (standard), so each V_0 basis element defines a linear operator on V_{1/2} = R^16. The computation reduces to octonion arithmetic: the Jordan product of two 3x3 octonionic Hermitian matrices, projected onto V_{1/2}. All computations are exact (no approximations, no numerics beyond floating-point representation of exact algebraic quantities).

The V_1 verification (ALGV-01) is expected to confirm L_{E_{11}} = (1/2)Id on V_{1/2}, reproducing the v6.0 Phase 22 result. The V_0 channel exploration (ALGV-02) is genuinely novel: no prior computation in the literature or this project has systematically characterized the 10-parameter family of operators {T_b : b in V_0} on V_{1/2} or searched for J^2 = -Id in their span. The representation-theoretic expectation is that this search will fail (S_9 is real type, End_{Spin(9)}(S_9) = R), but the operators T_b are NOT in End_{Spin(9)}(S_9) -- they break Spin(9) equivariance -- so the search is not trivially excluded by representation theory.

**Primary recommendation:** Build octonion arithmetic and h_3(O) Jordan product from scratch in Python/NumPy (hand-rolled, ~300 lines). Compute L_{E_{11}} on V_{1/2} first (trivial, confirms bottleneck). Then compute all 10 T_b matrices for a basis of V_0, extract the 10-parameter operator family in M_{16}(R), and determine whether any real linear combination squares to -Id by eigenvalue analysis of T_b^2.

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| --- | --- | --- | --- | --- |
| ref-baez2002 Sec. 3.4 | method / benchmark | Peirce decomposition of h_3(O): dimensions 1+16+10, Spin(9) reps, multiplication rules | Use as primary reference for all Peirce formulas | Plan tasks, verification checks |
| ref-alfsen-shultz2001 Ch. 8-9 | method | Peirce theory for JB-algebras; module structure of V_{1/2} | Cite for Peirce product rules; confirm V_{1/2} . V_{1/2} subset V_1 + V_0 | Plan verification step |
| ref-effros-stormer1979 | context | Positive projections and Jordan structure; confirms Peirce projections are positive | Background context for why Peirce decomposition is meaningful | Plan context section |
| ref-paper5 | prior artifact | Observer is M_n(C)^sa -- the C*-nature is the motivation for searching for J on V_{1/2} | Read; motivates ALGV-02 search | Plan context, discussion of results |
| ref-yokota Sec. 3 | method | F_4, Spin(9) action on O^2; explicit octonionic description of the spinor representation | Use for cross-validation of T_b matrices against Spin(9) structure | Plan verification step |
| ref-boyle2020 | benchmark | S_{10}^+|_{Spin(9)} = S_9^C; the complexification result that Phase 28 is testing algebraically | Compare: if J found, verify it gives the Boyle complexification | Plan comparison step |
| v6.0 Phase 22 | prior artifact | All 4 algebraic routes failed; V_1 = R bottleneck confirmed analytically | Cross-check: Phase 28 ALGV-01 must reproduce this numerically | Plan ALGV-01 verification |
| derivations/11-peirce-complexification.md | prior artifact | Explicit Peirce decomposition calculation already done analytically | Use as template; verify numerical code matches analytical formulas | Plan code validation |
| tests/test_cl6_sm.py | prior artifact | Existing Cl(10) construction with 32x32 matrices; octonion convention fano_e1e2=e4 | Match convention; possible cross-validation of Spin(9) generators | Plan cross-check step |

**Missing or weak anchors:** No prior computation of V_0 Peirce operators on V_{1/2} exists anywhere (literature or project). This is genuinely novel territory for ALGV-02. The analytical expectation (from representation theory: S_9 is real type) suggests J^2 = -Id will not be found, but the T_b operators break Spin(9) equivariance, so this expectation is not a proof.

## Conventions

| Choice | Convention | Alternatives | Source |
| --- | --- | --- | --- |
| Jordan product | a . b = (1/2)(ab + ba) | Some sources omit the 1/2 | Standard; matches Paper 7, derivations/11 |
| Peirce eigenvalues | {0, 1/2, 1} | N/A (follows from Jordan product convention) | Standard |
| Octonion multiplication | Fano plane: e_1 e_2 = e_4 | 480 valid tables exist | Matches test_cl6_sm.py ASSERT_CONVENTION |
| Complex structure choice | u = e_7 (default, any u in S^6 equivalent under G_2) | Any imaginary unit | Matches test_cl6_sm.py: complex_structure=u_equals_e7 |
| V_{1/2} identification | O^2 = {(x_2, x_3) : x_2, x_3 in O} as (1,3) and (1,2) off-diagonal entries | Some sources use (2,3) and (1,3) | Matches derivations/11 |
| V_0 identification | h_2(O) = lower-right 2x2 block: {(beta, gamma, x_1)} | Consistent with E_{11} as rank-1 idempotent in (1,1) slot | Standard |
| Unit system | Dimensionless (algebraic structure, no dynamics) | N/A | N/A |
| V_{1/2} basis ordering | 16 reals: (x_2^0, x_2^1, ..., x_2^7, x_3^0, x_3^1, ..., x_3^7) | Could interleave | Choose and document in code |

**CRITICAL: All equations and results below use these conventions. The Fano convention (e_1 e_2 = e_4) must match test_cl6_sm.py exactly or cross-validation will fail.**

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in This Phase |
| --- | --- | --- | --- |
| L_e(X) = e . X = (1/2)(E_{11}X + XE_{11}) | Peirce multiplication by idempotent | Baez 2002 Sec. 3.4 | ALGV-01: verify L_{E_{11}} = (1/2)Id on V_{1/2} |
| V_1 . V_{1/2} subset V_{1/2} | Peirce rule | McCrimmon 2004 Ch. 17 | Confirms L_a maps V_{1/2} to itself for a in V_1 |
| V_0 . V_{1/2} subset V_{1/2} | Peirce rule | McCrimmon 2004 Ch. 17 | Foundation of ALGV-02: T_b maps V_{1/2} to itself for b in V_0 |
| V_{1/2} . V_{1/2} subset V_1 + V_0 | Peirce rule | McCrimmon 2004 Ch. 17 | Inner product structure on V_{1/2} |
| V_1 . V_0 = {0} | Peirce rule | McCrimmon 2004 Ch. 17 | V_1 and V_0 annihilate each other |
| (a . b) . a^2 = a . (b . a^2) | Jordan identity | JvNW 1934 | Verification check for all computed products |
| e_i e_j = +/- e_k (Fano) | Octonion multiplication | Baez 2002 Table 1 | Foundation of all octonion arithmetic |
| ||a * b|| = ||a|| * ||b|| | Norm multiplicativity | Composition algebra property | Octonion module validation |
| T_b(x) = Pi_{1/2}(b . x) | Projected Peirce operator | This phase (definition) | ALGV-02: the 16x16 matrix to compute |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --- | --- | --- | --- |
| Octonion multiplication via Fano table | Computes a * b for a, b in O | Every Jordan product computation | Baez 2002 Table 1 |
| 3x3 octonionic matrix multiplication | Computes AB with octonion entries | Jordan product a . b = (1/2)(AB + BA) | derivations/11-peirce-complexification.md |
| Peirce projection Pi_{1/2} | Extracts V_{1/2} component of h_3(O) element | Defining T_b operators | Standard linear algebra |
| Eigenvalue analysis of T_b^2 | Determines if T_b^2 = -Id (all eigenvalues -1) | ALGV-02 J^2 = -Id search | NumPy np.linalg.eigvals |
| Exhaustive search over 10-parameter family | Tests sum c_i T_{b_i} for J^2 = -Id | ALGV-02 exhaustive search | See approach below |

### Approximation Schemes

None required. All computations in this phase are exact algebraic calculations. The only "approximation" is machine-precision floating-point representation of exact rational/algebraic quantities, which introduces errors at the 10^{-15} level -- completely negligible for the qualitative questions being asked (eigenvalue = -1 vs not -1).

## Standard Approaches

### Approach 1: Direct Peirce Computation via Octonion Arithmetic (RECOMMENDED)

**What:** Build octonion multiplication from the Fano table. Represent h_3(O) elements as (alpha, beta, gamma, x_1, x_2, x_3) with 27 real parameters. Implement the Jordan product as (1/2)(AB + BA) using explicit 3x3 octonionic matrix multiplication. Extract the 16x16 matrix representation of each Peirce operator by evaluating on a basis of V_{1/2}.

**Why standard:** This is the only way to get explicit matrices. There is no shortcut for h_3(O) because it is exceptional -- no faithful matrix representation over R or C exists that respects the Jordan structure. The computation must go through the octonionic matrix product directly.

**Track record:** The project's derivations/11-peirce-complexification.md already performed the analytical version of this computation for E_{11}. The computational approach extends it to all basis elements.

**Key steps:**

1. Implement octonion class: 8-component real vectors with Fano multiplication table
2. Implement h_3(O) element class: 3 reals + 3 octonions = 27 reals
3. Implement Jordan product: (1/2)(AB + BA) via 3x3 octonionic matrix multiply
4. Validate: Jordan identity on random elements, dimension checks, known Peirce eigenvalues
5. For ALGV-01: compute L_{E_{11}}(e_k) for each of 16 basis vectors e_k of V_{1/2}; assemble 16x16 matrix; verify = (1/2)Id
6. For ALGV-02: choose 10 basis elements {b_1, ..., b_{10}} of V_0 = h_2(O); for each b_i, compute T_{b_i}(e_k) for all 16 basis vectors; assemble 10 matrices of size 16x16
7. Eigenvalue analysis: for each b_i, compute eigenvalues of T_{b_i}^2; search for T^2 = -Id
8. Exhaustive search: parameterize T(c) = sum c_i T_{b_i}; analyze T(c)^2 + Id = 0 as a polynomial system in 10 variables

**Known difficulties at each step:**

- Step 1: Sign errors in the Fano table are the #1 risk. Must verify e_i^2 = -1 for all i, norm multiplicativity on random pairs, and NON-associativity: (e_1 e_2)e_3 != e_1(e_2 e_3).
- Step 3: Octonion non-associativity does NOT cause problems for 3x3 Hermitian matrix products because each matrix entry involves sums of products of 2 octonion elements at a time (Artin's theorem guarantees associativity for any subalgebra generated by 2 elements). However, the code must never silently assume (ab)c = a(bc) for general octonions.
- Step 6: Choosing the right basis for V_0. A natural basis: {E_{22}, E_{33}, and the 8 matrices with x_1 = e_k for k=0,...,7}. That gives 2 + 8 = 10 basis elements, matching dim(V_0) = 10.
- Step 8: The polynomial system T(c)^2 + Id = 0 has 256 equations in 10 unknowns. This is overdetermined. If no solution exists, the system is inconsistent -- but proving inconsistency rigorously requires more than just failing to find a numerical solution. The approach should be: compute eigenvalues of T(c)^2 for a grid of c values plus random sampling, then use the algebraic structure (the operators generate a specific Lie algebra or associative algebra in M_{16}(R)) to prove impossibility.

### Approach 2: Clifford Algebra Cross-Validation (SUPPORTING)

**What:** Build the 9 generators of Cl(9) on R^16 using the tensor product construction (matching test_cl6_sm.py pattern). Verify that the spin(9) generators reproduce the Peirce operators from Approach 1 (specifically, the T_b for traceless b in V_0 should correspond to spin(9) generators restricted to the spinor representation). The 10th Cl(10) generator (complexification direction) identifies the J that would solve ALGV-02 if it existed in the span of the T_b.

**When to use:** After Approach 1 produces all 10 T_{b_i} matrices. This provides an independent check by comparing the operator algebra generated by the T_b with the known spin(9) algebra.

**Tradeoffs:** More work to set up, but provides independent validation and deeper structural insight into WHY J^2 = -Id fails (if it does).

### Anti-Patterns to Avoid

- **Using external octonion libraries:** None are mature enough, and convention mismatches will cause silent errors. Build from Fano table.
- **Symbolic computation with SymPy for full Jordan products:** Expressions explode combinatorially with non-associative multiplication. Numerical computation with exact-enough floating point is sufficient.
- **Searching for J via gradient descent on ||T(c)^2 + Id||:** Non-convex landscape with no guarantee of finding global minimum. Use algebraic analysis instead.
- **Testing with h_3(R) or h_3(C) as a proxy for h_3(O):** These are JC-algebras with fundamentally different properties. Results do NOT transfer to the exceptional case.
- **Assuming the T_b operators are in End_{Spin(9)}(V_{1/2}):** They are NOT. The T_b operators break Spin(9) equivariance (they depend on specific V_0 basis elements, not Spin(9)-invariant combinations). The Schur lemma argument (End_{Spin(9)}(S_9) = R) does not directly exclude J^2 = -Id in the span of T_b.

## Existing Results to Leverage

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
| --- | --- | --- | --- |
| Peirce decomposition dimensions | V_1(1) + V_{1/2}(16) + V_0(10) = 27 | Baez 2002 Sec. 3.4 | Dimension check on computed projections |
| L_{E_{11}} explicit formula | L_{E_{11}}(X) = (alpha, 0, 0, 0, x_2/2, x_3/2) | derivations/11, Step 2 | Direct check of ALGV-01 code output |
| V_1 = R * E_{11} | dim(V_1) = 1 | Baez 2002; derivations/11 | ALGV-01 reproduces this |
| V_0 = h_2(O) | Lower-right 2x2 Hermitian octonionic block | derivations/11, Steps 2-3 | Basis construction for ALGV-02 |
| V_{1/2} = O^2 | Off-diagonal (1,2) and (1,3) entries | derivations/11, Step 2 | V_{1/2} basis construction |
| Spin(9) representations: 27 = 1 + 16 + (9+1) | V_1 = trivial, V_{1/2} = S_9, V_0 = vector + scalar | Baez 2002 Sec. 4.3 | Structural interpretation of results |
| S_9 is real type (F-S = +1) | End_{Spin(9)}(S_9) = R; Cl^+(9,0) = M_{16}(R) | Lawson-Michelsohn 1989 Table I.4.3 | Expectation for ALGV-02 outcome (but not proof of impossibility for non-equivariant operators) |
| G_SM = Stab_{Spin(9)}(J_u) | J_u = left multiplication by u on each O factor of O^2 | Krasnov, arXiv:1912.11282 | If J found in T_b span, compare with J_u |
| Peirce multiplication rules | V_i . V_j containments | McCrimmon 2004 Ch. 17 | Validates that T_b(V_{1/2}) subset V_{1/2} |
| Jordan identity | (a . b) . a^2 = a . (b . a^2) | JvNW 1934 | Verification check |

**Key insight:** The L_{E_{11}} computation is a known result that serves as code validation. The T_b computation for b in V_0 is genuinely new and is the scientific content of this phase.

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
| --- | --- | --- | --- |
| Explicit Fano multiplication table | 7 triples defining O multiplication | Baez 2002 Table 1, test_cl6_sm.py convention | Convention: e_1 e_2 = e_4 |
| Octonion conjugation: a-bar = (a_0, -a_1, ..., -a_7) | Hermiticity of h_3(O) matrices | Standard | Always valid |
| Norm multiplicativity: ||ab|| = ||a|| ||b|| | Validation of octonion implementation | Composition algebra property | Always valid |
| Artin's theorem: subalgebra generated by 2 elements is associative | Parenthesization in 3x3 matrix entry OK | Standard (Baez 2002 Sec. 2.1) | 2 generators only |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| --- | --- | --- | --- | --- |
| The Octonions | Baez | 2002 | Peirce decomposition, Spin(9) action, Fano table | Sec. 3.4 for Peirce, Sec. 2.1 for octonion properties, Table 1 for multiplication |
| A Taste of Jordan Algebras | McCrimmon | 2004 | Peirce multiplication rules, Jordan identity proofs | Ch. 17 for Peirce theory, esp. Peirce bilinear products |
| SO(9) characterisation of G_SM | Krasnov | 2019 | J_u on O^2 is exactly what ALGV-02 searches for | Explicit formula for J_u = left-mult by u; comparison target |
| The Role of Spin(9) in Octonionic Geometry | Parton-Piccinni | 2018 | Explicit Spin(9) matrices on R^16 | arXiv:1810.06288; cross-validation of Cl(9) generators |
| The Exceptional Jordan Eigenvalue Problem | Dray-Manogue | 1999 | Explicit octonionic matrix computations | arXiv:math-ph/9910004; validates h_3(O) product implementation |
| Exceptional Lie Groups | Yokota | 2009 | F_4, Spin(9) on O^2 | arXiv:0902.0431; alternative octonionic Spin(9) construction |

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
| --- | --- | --- | --- |
| NumPy | 2.4.x | Dense 16x16 matrix operations, eigenvalue computation, octonion component storage | Universally standard for numerical linear algebra |
| Python | 3.14.x | Runtime | Project standard |
| pytest | 9.x | Test framework (matching existing test_cl6_sm.py pattern) | Project standard |

### Supporting Tools

| Tool | Purpose | When to Use |
| --- | --- | --- |
| SciPy (scipy.linalg) | SVD, eigendecomposition if finer spectral analysis needed | Analyzing rank and structure of operator algebra |
| matplotlib | Eigenvalue plots if visualizing T_b^2 spectrum | Optional, for understanding the 10-parameter family |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
| --- | --- | --- |
| Hand-rolled octonion class | hypercomplex/pyoctonion PyPI packages | Convention mismatch risk; no h_3(O) support; not maintained |
| NumPy floating point | SymPy exact symbolic | ~1000x slower; unnecessary since all structure questions are qualitative (eigenvalue = -1 or not) |
| Python | SageMath | Has built-in octonion support but different convention, heavy dependency |

### Computational Feasibility

| Computation | Estimated Cost | Bottleneck | Mitigation |
| --- | --- | --- | --- |
| One Jordan product of h_3(O) elements | ~3500 real multiplications, microseconds | None | Trivial |
| All 16 T_b evaluations for one b | 16 Jordan products + projections, milliseconds | None | Trivial |
| All 10 T_b matrices | 160 Jordan products, milliseconds total | None | Trivial |
| Eigenvalue analysis of T(c)^2 for grid search | ~10^4 eigendecompositions of 16x16, seconds | None | Trivial |
| Full exhaustive analysis of 10-parameter family | Algebraic structure analysis, minutes | Complexity of the polynomial system | Use operator algebra structure, not brute force |

**This is a computationally trivial problem. The challenge is algebraic correctness, not computational cost.**

**Installation / Setup:**
```bash
# All required packages are already in the project (NumPy, SciPy, pytest)
# No additional installation needed
```

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| --- | --- | --- | --- |
| e_i^2 = -1 for i=1,...,7 | Octonion multiplication table | Compute and assert | Exact equality |
| ||ab|| = ||a|| ||b|| | Composition algebra property | 100 random pairs | Machine precision (< 10^{-14}) |
| (e_1 e_2)e_3 != e_1(e_2 e_3) | Non-associativity | Compute both sides | Different (confirms non-associativity) |
| Jordan identity on random A, B | Jordan product implementation | (A.B).A^2 == A.(B.A^2) for 100 random pairs | Machine precision |
| dim(V_1) = 1, dim(V_{1/2}) = 16, dim(V_0) = 10 | Peirce projection implementation | Project random h_3(O) elements | Exact dimensions |
| L_{E_{11}} = (1/2)Id on V_{1/2} | ALGV-01 (code correctness) | Compute 16x16 matrix | Exact: diagonal = 0.5, off-diagonal = 0 |
| T_b(V_{1/2}) subset V_{1/2} | Peirce rule V_0.V_{1/2} subset V_{1/2} | Verify V_1 and V_0 components of b.x are zero when b in V_0, x in V_{1/2} | Exact: Pi_1(b.x) = 0, Pi_0(b.x) = 0... wait, Peirce rule says V_0.V_{1/2} subset V_{1/2}, so Pi_1 component is 0 but Pi_0 component need not be. Actually: the Peirce rules give V_0 . V_{1/2} subset V_{1/2}. So Pi_1 = 0 and Pi_0 = 0. |
| V_1 . V_0 = 0 | Peirce orthogonality | Compute E_{11} . b for b in V_0 | Exact zero |
| V_{1/2} . V_{1/2} subset V_1 + V_0 | Peirce rule | Compute x . y for x, y in V_{1/2}, check Pi_{1/2} = 0 | Machine precision zero |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| --- | --- | --- | --- |
| b = 0 (trivial V_0 element) | T_0 = 0 | Zero operator on V_{1/2} | Trivial |
| b = (1/2)(E_{22} + E_{33}) = 1 - E_{11} | T_b should give L_{1-e}|_{V_{1/2}} = (1/2)Id | (1/2)Id on V_{1/2} | Peirce: L_{1-e} has eigenvalue 1/2 on V_{1/2} |
| b = E_{22} or b = E_{33} (diagonal V_0) | These are idempotents in V_0 | T_b should be a projection-like operator | Peirce theory for sub-idempotents |
| Krasnov's J_u | J_u = left-mult by u on each O factor | J_u^2 = -Id, commutes with Spin(9) action | Krasnov arXiv:1912.11282 |

### Numerical Validation

| Test | Method | Tolerance | Reference Value |
| --- | --- | --- | --- |
| L_{E_{11}} matrix entries | Direct comparison | 10^{-14} | (1/2) * Id_{16} |
| T_b symmetry/antisymmetry | Check T_b^T vs T_b | 10^{-14} | Depends on b (see analysis below) |
| T_b eigenvalue spectrum | np.linalg.eigvals(T_b) | 10^{-12} | Must be real (T_b is real matrix) |
| T(c)^2 + Id spectrum | np.linalg.eigvals(T(c)^2 + Id) | 10^{-10} | If J exists: all zero. If not: nonzero eigenvalues. |
| Jordan identity residual | ||(A.B).A^2 - A.(B.A^2)|| | 10^{-12} | 0 |

### Red Flags During Computation

- **If dim(V_1) != 1:** Everything in the v8.0 framing is wrong. HALT per stop/rethink criterion.
- **If L_{E_{11}} != (1/2)Id on V_{1/2}:** Code bug in octonion multiplication or Jordan product. Do not proceed until fixed.
- **If T_b(x) has nonzero V_1 or V_0 components for b in V_0, x in V_{1/2}:** Violates Peirce multiplication rules. Code bug.
- **If Jordan identity fails on random elements:** Fundamental code error in Jordan product implementation.
- **If octonion norm is not multiplicative:** Fano table has sign error.
- **If T_b^2 has complex eigenvalues:** Cannot happen for a real matrix. Indicates numerical error.

## Common Pitfalls

### Pitfall 1: Fano Table Sign Errors

**What goes wrong:** There are 480 valid octonion multiplication tables (related by G_2 automorphisms). Using the wrong one does not produce incorrect Jordan products in general, but it DOES produce wrong explicit matrices that cannot be cross-validated against test_cl6_sm.py or Krasnov's J_u.

**Why it happens:** Copy-paste errors when transcribing the 7 Fano triples. Different sources use different conventions (Baez vs Yokota vs Conway-Smith).

**How to avoid:** Use the convention e_1 e_2 = e_4 (matching test_cl6_sm.py). Verify ALL 21 products e_i e_j (i < j) against the Fano table. Test: e_i^2 = -1, norm multiplicativity on 100+ random pairs, non-associativity witness.

**Warning signs:** Octonion norm not multiplicative. Cross-validation with test_cl6_sm.py Cl(10) generators fails.

**Recovery:** Re-derive from the 7 Fano triples. The triples for e_1 e_2 = e_4 convention are: (1,2,4), (2,3,5), (3,4,6), (4,5,7), (5,6,1), (6,7,2), (7,1,3).

### Pitfall 2: Confusing T_b with a Spin(9)-Equivariant Operator

**What goes wrong:** The representation-theoretic argument "End_{Spin(9)}(S_9) = R, so no J exists" is used to skip the ALGV-02 computation entirely. This is WRONG because the T_b operators are NOT Spin(9)-equivariant -- they depend on the choice of b in V_0, breaking Spin(9) symmetry.

**Why it happens:** Conflation of "no equivariant complex structure" with "no complex structure at all." The Krasnov J_u IS a complex structure on V_{1/2} -- it just doesn't commute with all of Spin(9), only with G_SM = Stab_{Spin(9)}(J_u).

**How to avoid:** Remember that the question is whether J^2 = -Id exists in the span of {T_b : b in V_0}, NOT whether J^2 = -Id exists in End_{Spin(9)}(V_{1/2}). The former is a 10-parameter search in M_{16}(R). The latter is trivially impossible (End_{Spin(9)}(S_9) = R contains no element squaring to -1).

**Warning signs:** Arguments that dismiss the ALGV-02 search without computing.

**Recovery:** Compute all T_b matrices. The computation is cheap (milliseconds).

### Pitfall 3: V_0 Basis Choice Ambiguity

**What goes wrong:** V_0 = h_2(O) is 10-dimensional. The choice of basis affects the explicit T_b matrices (though not the span). A poorly chosen basis makes it hard to interpret the operator algebra structure.

**Why it happens:** Multiple natural bases exist: {E_{22}, E_{33}, and 8 off-diagonal matrices with x_1 = e_k}, or {E_{22}, (1-E_{11}) (= E_{22}+E_{33}), and 8 off-diagonal matrices}, or {traceless diagonal, trace, off-diagonal}.

**How to avoid:** Use the Spin(9)-adapted basis: separate V_0 into the trace part (1-dimensional, spanned by (1/2)(E_{22}+E_{33})) and the traceless part (9-dimensional, carrying the vector representation of SO(9)). The traceless part decomposes as: 1 traceless diagonal matrix ((1/2)(E_{22}-E_{33})) and 8 off-diagonal matrices with x_1 = e_k for k=0,...,7. This makes the Spin(9) structure transparent.

**Warning signs:** Operators that should be related by Spin(9) rotations have different eigenvalue spectra.

**Recovery:** Change basis to the Spin(9)-adapted one.

### Pitfall 4: Octonion Non-Associativity in Jordan Product

**What goes wrong:** The Jordan product involves 3x3 matrix multiplication with octonion entries: (AB)_{ij} = sum_k A_{ik} B_{kj}. Each term A_{ik} B_{kj} is an octonion product. Summing over k gives sums of octonion products. The sum AB + BA involves terms like A_{ik}B_{kj} + B_{ik}A_{kj}. This is well-defined because each term is a product of 2 octonions (Artin's theorem applies). BUT if the code computes intermediate results that involve products of 3 or more octonions, associativity failure will cause bugs.

**Why it happens:** In standard matrix multiplication code, one might accumulate results using operations like result += A[i,m] * (B[m,k] * C[k,j]), which involves 3 octonion multiplications with implicit parenthesization.

**How to avoid:** The Jordan product A . B = (1/2)(AB + BA) only involves 2-octonion products (A_{ik} * B_{kj}). Never nest octonion multiplications in the Jordan product code. If computing A^2 = A . A, compute it as a single Jordan product, not as A * A using "matrix squaring" with triple products.

**Warning signs:** Jordan identity fails on random elements.

**Recovery:** Rewrite Jordan product to explicitly avoid nested octonion multiplications.

## Level of Rigor

**Required for this phase:** Computational verification with exact arithmetic (machine precision floating point for qualitative questions).

**Justification:** Phase 28 is a VERIFICATION phase. The theoretical framework (Peirce decomposition, Jordan products) is established. The goal is to produce explicit matrices and determine their properties computationally. The level of rigor is: compute exactly, verify against known results, report eigenvalue spectra.

**What this means concretely:**

- All octonion products must be exact to machine precision (< 10^{-14} error)
- The ALGV-01 result (L_{E_{11}} = (1/2)Id) must be verified to < 10^{-14}
- The ALGV-02 result (J^2 = -Id exists or not) must be established by eigenvalue analysis with clear separation from -1 (if no J exists, eigenvalues of T(c)^2 should be clearly != -1 for all c)
- Jordan identity verification on 100+ random element pairs

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| --- | --- | --- | --- |
| Analytical Peirce computation (v6.0 Phase 22) | Computational Peirce verification (Phase 28) | v8.0 | Numerical confirmation of analytical results; extension to V_0 channel |
| V_1 channel only (v6.0) | V_0 + V_1 channels (v8.0 Phase 28) | v8.0 | V_0 was never explored; 10-parameter operator family is genuinely new |

**Superseded approaches to avoid:**

- None for this phase. The computation is straightforward and no outdated methods are relevant.

## Open Questions

1. **Can any real linear combination of the 10 T_b operators satisfy J^2 = -Id?**
   - What we know: The Schur lemma argument excludes J in End_{Spin(9)}(S_9), but the T_b break Spin(9) equivariance. Krasnov's J_u (left-mult by u) IS a complex structure on O^2, but it arises from octonionic left multiplication, not from Peirce multiplication by V_0 elements. The question is whether J_u lies in the span of {T_b}.
   - What's unclear: The explicit relationship between Krasnov's J_u and the T_b operators. It is possible that J_u = T_b for some specific b in V_0, or that J_u requires elements outside V_0.
   - Impact on this phase: This IS the central question of ALGV-02.
   - Recommendation: Compute all 10 T_b matrices and directly check. Also explicitly compute Krasnov's J_u as a 16x16 matrix and check if it lies in span({T_b}).

2. **What Lie algebra do the T_b operators generate in M_{16}(R)?**
   - What we know: The 9 traceless T_b should generate a subalgebra related to so(9) or spin(9).
   - What's unclear: Whether the trace component adds anything new.
   - Impact on this phase: Identifies the structural reason for success/failure of ALGV-02.
   - Recommendation: Compute commutators [T_{b_i}, T_{b_j}] and identify the Lie algebra.

3. **Is Krasnov's J_u realizable as a Peirce operator T_b for some b?**
   - What we know: J_u acts on O^2 by left multiplication by u on each octonion factor. This is a well-defined 16x16 real matrix. The question is whether there exists b in h_2(O) such that T_b = J_u.
   - What's unclear: The explicit form of T_b in terms of octonion left multiplication.
   - Impact on this phase: If J_u = T_b for some b, then V_0 DOES contain the complex structure and ALGV-02 succeeds. If not, the V_0 channel fails to produce J.
   - Recommendation: This should be tested explicitly as part of ALGV-02.

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| --- | --- | --- | --- |
| Octonion arithmetic has bugs | Fano table errors | Verify against independent source (Dray-Manogue arXiv:math-ph/9910004 multiplication table) | Hours to cross-check |
| 16x16 matrix extraction gives wrong dimensions | V_{1/2} basis ordering issue | Re-examine basis choice, verify with dim counts | Minutes |
| ALGV-02 search inconclusive | Numerical ambiguity near J^2 = -Id | Switch to SymPy exact symbolic computation for the specific candidate | Hours |
| T_b span does not contain J_u | Structural: Krasnov J_u is not a Peirce operator | Characterize exactly what operator algebra the T_b generate; this IS a definitive negative result for the V_0 channel | Phase is complete (negative result is a valid and important outcome) |

**Decision criteria:** If ALGV-02 produces a definitive negative (no J^2 = -Id in the T_b span), this is a scientifically valuable result. It means the V_0 channel, like the V_1 channel, cannot transmit complex structure through Peirce multiplication. The phase succeeds either way -- the goal is to DETERMINE the answer, not to force a positive result.

## Detailed Computation Plan for ALGV-02

### V_0 Basis Construction

V_0 = h_2(O) consists of elements of h_3(O) with alpha = 0, x_2 = 0, x_3 = 0:

```
b = (0, beta, gamma, x_1, 0, 0) <-> matrix:  | 0    0        0    |
                                                | 0    beta     x1*  |
                                                | 0    x1       gamma|
```

Natural basis (10 elements):
- b_1 = E_{22}: beta=1, gamma=0, x_1=0
- b_2 = E_{33}: beta=0, gamma=1, x_1=0
- b_3 through b_{10}: x_1 = e_k for k=0,1,...,7 (with beta=gamma=0)

Spin(9)-adapted basis:
- Trace: (1/2)(E_{22} + E_{33})  [trivial rep of Spin(9)]
- Traceless diagonal: (1/2)(E_{22} - E_{33})  [part of vector rep]
- 8 off-diagonal: x_1 = e_k for k=0,...,7  [rest of vector rep]

### The T_b Computation

For each basis element b_i of V_0 and each basis element e_j of V_{1/2} (j = 1,...,16):

1. Compute c = b_i . e_j (Jordan product in h_3(O))
2. Extract T_{b_i,j} = Pi_{1/2}(c) (project onto V_{1/2})
3. Column j of the 16x16 matrix T_{b_i} is the coordinate vector of Pi_{1/2}(c) in the V_{1/2} basis

### The J^2 = -Id Search

Given 10 matrices T_{b_1}, ..., T_{b_{10}} in M_{16}(R):

**Step 1: Individual eigenvalue analysis.** For each T_{b_i}, compute eigenvalues of T_{b_i}^2. If any T_{b_i}^2 = -Id, we're done.

**Step 2: Pairwise analysis.** For T = c_1 T_{b_i} + c_2 T_{b_j} (2-parameter families), analyze T^2 = c_1^2 T_{b_i}^2 + c_1 c_2 (T_{b_i}T_{b_j} + T_{b_j}T_{b_i}) + c_2^2 T_{b_j}^2 = -Id. This is a quadratic system in (c_1, c_2) with known matrix coefficients.

**Step 3: Full 10-parameter analysis.** T(c)^2 = sum_{i,j} c_i c_j S_{ij} where S_{ij} = (1/2)(T_{b_i}T_{b_j} + T_{b_j}T_{b_i}). The condition T(c)^2 = -Id becomes sum_{i,j} c_i c_j S_{ij} = -Id_{16}. This is 256 quadratic equations in 10 unknowns. Analysis: extract the 16x16 matrices S_{ij} (there are 55 of them: 10 diagonal + 45 off-diagonal). The system sum c_i c_j S_{ij} = -Id is equivalent to: for each matrix entry (p,q), sum_{i,j} c_i c_j (S_{ij})_{pq} = -delta_{pq}. This is a quadratic form in c that must equal a specific value for each (p,q). The feasibility can be checked by linear algebra on the "flattened" system.

**Step 4: Compare with Krasnov's J_u.** Compute J_u as a 16x16 matrix (left multiplication by u = e_7 on each O factor of O^2). Check if J_u lies in span({T_{b_i}}). If yes, ALGV-02 succeeds. If no, the complex structure is not accessible through Peirce multiplication.

### Key Structural Question

The T_b operators for b in the traceless part of V_0 should be related to the Spin(9) generators on V_{1/2} = S_9. Specifically, the 9-dimensional vector representation of Spin(9) (= traceless V_0) should map to specific operators on S_9 via the Peirce product. If these operators are exactly the Cl(9) gamma matrices (or linear combinations thereof), then the Peirce V_0 channel reproduces the Clifford algebra Cl(9) on S_9, and the 10th direction (complexification, Krasnov's J) lies OUTSIDE V_0. This would be the definitive negative result.

Alternatively, the T_b operators might include additional structure from the Jordan identity that goes beyond Cl(9). The computation will determine which case holds.

## Caveats and Alternatives

**Self-critique:**

1. **Assumption that might be wrong:** I assume the T_b operators for traceless b in V_0 are closely related to Cl(9) generators. This is based on the representation theory (V_0 carries the 9+1 rep of Spin(9)). But the Peirce product is NOT the same as the Clifford product. The T_b could be something entirely different from gamma matrices.

2. **Alternative approach dismissed:** One could try to prove impossibility of J^2 = -Id algebraically (without computation) by analyzing the algebra generated by {T_b} in M_{16}(R). This was dismissed as harder than direct computation, but it would give a cleaner result. The planner should consider whether an algebraic proof should follow the computational search.

3. **Limitation understated:** The "exhaustive search" over the 10-parameter family is exhaustive only for the linear span of T_b operators evaluated at individual V_0 basis elements. It does NOT cover nonlinear combinations (compositions like T_{b_1} T_{b_2}) or products involving V_{1/2} . V_{1/2} -> V_0 followed by V_0 . V_{1/2} -> V_{1/2}. These second-order operations could produce operators outside the linear span of T_b. The planner should flag this gap.

4. **Simpler method overlooked?** For the specific question "is Krasnov's J_u a Peirce operator?", one could check directly by computing b . x and comparing to u * x (octonionic left multiplication) for a few test vectors x. This is simpler than computing all 10 T_b matrices. However, computing all 10 is cheap and gives the full picture, so the simpler check should be done FIRST as a quick test, then the full computation for completeness.

5. **Physicist disagreement:** A Jordan algebraist might argue that the Peirce product T_b is well-understood and cannot produce a complex structure because h_3(O) is formally real (every element squares to a sum of squares). This argument has force but is not a rigorous proof that J^2 = -Id is impossible in the T_b span -- formally real means no nilpotents, but J^2 = -Id is not a nilpotency condition.

## Sources

### Primary (HIGH confidence)

- Baez, "The Octonions," Bull. AMS 39 (2002), 145-205, [arXiv:math/0105155](https://arxiv.org/abs/math/0105155) - Peirce decomposition Sec. 3.4, Spin(9) action, Fano table
- McCrimmon, "A Taste of Jordan Algebras," Springer (2004), Ch. 17 - Peirce multiplication rules, Jordan identity proofs
- Lawson & Michelsohn, "Spin Geometry," Princeton (1989), Table I.4.3 - Clifford algebra classification, Cl(9,0) = M_{16}(R) + M_{16}(R)
- Jordan, von Neumann, Wigner, "On an Algebraic Generalization of the Quantum Mechanical Formalism," Ann. Math. 35 (1934) - Jordan identity, classification of formally real Jordan algebras
- derivations/11-peirce-complexification.md (project artifact) - Explicit Peirce decomposition calculation under E_{11}

### Secondary (MEDIUM confidence)

- [Krasnov, "SO(9) characterisation of the Standard Model gauge group," J. Math. Phys. 62 (2021) 021703](https://arxiv.org/abs/1912.11282) - J_u on O^2, G_SM characterization
- [Parton & Piccinni, "The Role of Spin(9) in Octonionic Geometry," Axioms 7 (2018) 72](https://arxiv.org/abs/1810.06288) - Explicit Spin(9) matrices on R^16
- [Dray & Manogue, "The Exceptional Jordan Eigenvalue Problem," Adv. Appl. Cliff. Alg. 8 (1998)](https://arxiv.org/abs/math-ph/9910004) - Explicit octonionic matrix computations
- Yokota, "Exceptional Lie Groups" (2009), [arXiv:0902.0431](https://arxiv.org/abs/0902.0431) - F_4, Spin(9) on O^2
- [Boyle, "The Standard Model, the Exceptional Jordan Algebra, and Triality"](https://arxiv.org/abs/2006.16265) - S_{10}^+|_{Spin(9)} = S_9^C branching
- tests/test_cl6_sm.py (project artifact) - Existing Cl(10) construction, fano_e1e2=e4 convention

### Tertiary (LOW confidence)

- None needed. All results for this phase are well-established.

## Metadata

**Confidence breakdown:**

- Mathematical framework: HIGH - Standard Peirce theory applied to a well-studied algebra. All formulas from textbooks.
- Standard approaches: HIGH - Direct computation is the only approach. No methodological uncertainty.
- Computational tools: HIGH - NumPy is standard. Computation is trivial in scale.
- Validation strategies: HIGH - Multiple independent checks available (Jordan identity, dimension counts, known Peirce eigenvalues, cross-validation with Cl(9) construction).

**Research date:** 2026-03-29
**Valid until:** Indefinitely (pure mathematics, no tool version sensitivity for the core computation)
