# Computational Approaches: h_3(O) Peirce Multiplication and Complexification Verification

**Surveyed:** 2026-03-29
**Domain:** Exceptional Jordan algebras / Octonion arithmetic / Spin(9)-Spin(10) representations
**Confidence:** HIGH

### Scope Boundary

COMPUTATIONAL.md covers computational TOOLS, libraries, algorithms, and infrastructure for verifying whether C*-observer Peirce multiplication maps force complexification of V_{1/2} = O^2 in h_3(O). It does NOT cover the physics motivation (PRIOR-WORK.md) or the analytical proof strategy (METHODS.md).

**Relationship to existing codebase:** The project has a working Python/SymPy + NumPy/SciPy framework with explicit 32x32 Cl(10)/Cl(6) matrices (test_cl6_sm.py, Phase 19) and first-order condition verification machinery (test_first_order.py, Phases 13-15). No octonion arithmetic or h_3(O) Jordan product code exists yet. This document covers the NEW computational layer needed: octonion multiplication, h_3(O) element representation, Jordan product computation, and Peirce multiplication operator extraction.

## Recommended Stack

Build a self-contained Python module (~300 lines) implementing octonion arithmetic and h_3(O) Jordan products from scratch using NumPy. Do not use external octonion libraries. The reasons are:

1. **No mature library exists.** The Python octonion ecosystem consists of toy packages (hypercomplex, pyoctonion, Cayley-Dickson scripts) that implement basic multiplication but lack h_3(O) matrix operations, Peirce decomposition, or Jordan products. None have been used in published research computations.

2. **The computation is small.** h_3(O) is 27-dimensional. Octonions are 8-dimensional. The Jordan product of two 3x3 octonionic Hermitian matrices involves ~54 octonion multiplications. This is microsecond-scale on a laptop.

3. **Correctness is critical.** The central question -- whether L_{u*E_11}(x) acts as multiplication by i on V_{1/2} -- depends on exact octonion multiplication. A hand-rolled implementation with Fano-plane-based multiplication table is verifiable line-by-line. An opaque external library is not.

4. **The existing Cl(10) code (test_cl6_sm.py) already follows this pattern.** It builds Clifford generators from scratch using Pauli tensor products rather than importing a library.

**Primary stack:** NumPy for all numerical computation. SymPy only if parametric proofs over symbolic octonion components are needed (unlikely -- the key checks are numerical with exact rational arithmetic or machine-precision floating point).

## Numerical Algorithms

### 1. Octonion Arithmetic

| Algorithm | Problem | Convergence | Cost per Step | Memory | Key Reference |
|-----------|---------|-------------|---------------|--------|---------------|
| Fano multiplication table | o1 * o2 for o1, o2 in O | Exact | O(64) flops (8x8 table) | 64 bytes (table) | Baez, Bull. AMS 39 (2002), Table 1 |
| Cayley-Dickson recursion | o1 * o2 via quaternion pairs | Exact | O(32) flops | Negligible | Dray-Manogue, "Geometry of the Octonions" (2015) |

**Recommendation:** Use the Fano multiplication table. It is explicit, verifiable, and matches the project's existing convention (fano_e1e2=e4 from test_cl6_sm.py ASSERT_CONVENTION).

#### Algorithm: Octonion Multiplication via Fano Table

```
INPUT:  a = (a0, a1, ..., a7), b = (b0, b1, ..., b7) in R^8
        Fano multiplication table FANO[i][j] = (sign, index) for e_i * e_j
OUTPUT: c = a * b in R^8

Convention: O = R*1 + R*e_1 + ... + R*e_7
  e_i * e_j = FANO[i][j] for i,j in {1,...,7}
  e_i * 1 = 1 * e_i = e_i
  1 * 1 = 1

Table (e_i * e_j -> +/- e_k, following Baez with e1*e2 = e4):
  e1*e2 = +e4    e2*e3 = +e5    e3*e4 = +e6    e4*e5 = +e7
  e5*e6 = +e1    e6*e7 = +e2    e7*e1 = +e3
  (plus cyclic shifts of each Fano line, plus antisymmetry e_j*e_i = -e_i*e_j)

1. c0 = a0*b0 - sum_{i=1}^{7} a_i*b_i     (real part: standard inner product)
2. For k = 1,...,7:
     c_k = a0*b_k + a_k*b0
           + sum over Fano triples (i,j,k) with e_i*e_j = +e_k: a_i*b_j - a_j*b_i
3. RETURN c

VERIFICATION:
  - e_i^2 = -1 for all i in {1,...,7}
  - ||a*b|| = ||a|| * ||b|| (norm-preserving: composition algebra)
  - NOT associative: check (e1*e2)*e3 != e1*(e2*e3) as a test
```

#### Convergence Properties

- **Exact for floating point:** No iteration, no convergence issue. Single-pass formula.
- **Known failure mode:** Sign errors in the Fano table. There are 480 valid octonion multiplication tables (corresponding to automorphisms of the Fano plane under G_2). The convention must be fixed once and checked against known identities.
- **Validation:** Verify all 7 Fano lines independently, check e_i^2 = -1, check norm-multiplicativity on 100 random pairs.

### 2. Octonion Conjugation and Norm

```
INPUT:  a = (a0, a1, ..., a7)
OUTPUT: a_bar = (a0, -a1, ..., -a7)        (conjugation)
        ||a||^2 = a0^2 + a1^2 + ... + a7^2  (squared norm)
        Re(a) = a0                           (real part)

Key identity: a * a_bar = a_bar * a = ||a||^2 * 1
```

### 3. h_3(O) Element Representation

| Algorithm | Problem | Convergence | Cost per Step | Memory | Key Reference |
|-----------|---------|-------------|---------------|--------|---------------|
| Component encoding | Represent X in h_3(O) as 27 real numbers | N/A | N/A | 27 floats | Albert (1934) |

#### Data Structure

```
An element X in h_3(O) is stored as:
  X = (alpha, beta, gamma, x1, x2, x3)
where:
  alpha, beta, gamma in R     (diagonal entries)
  x1, x2, x3 in R^8           (octonion off-diagonal entries)

Total: 3 + 3*8 = 27 real parameters

Matrix form:
  X = | alpha    x3_bar   x2    |
      | x3       beta     x1_bar|
      | x2_bar   x1       gamma |

Hermiticity: X_{ij} = X_{ji}_bar (octonion conjugate)
```

### 4. h_3(O) Jordan Product

| Algorithm | Problem | Convergence | Cost per Step | Memory | Key Reference |
|-----------|---------|-------------|---------------|--------|---------------|
| Explicit matrix multiply + symmetrize | A circ B = (1/2)(AB + BA) | Exact | O(3^3 * 64) ~ 1700 flops | 2 * 27 floats | Albert (1934), JvNW (1934) |

#### Algorithm: Jordan Product in h_3(O)

```
INPUT:  A, B in h_3(O) (each represented as 27 reals)
OUTPUT: C = A circ B = (1/2)(AB + BA) in h_3(O)

CRITICAL: The matrix product AB involves entries (AB)_{ij} = sum_k A_{ik} * B_{kj}
where * is OCTONION multiplication. For 3x3 matrices, each entry involves
3 octonion multiplications and 2 octonion additions.

SUBTLETY: Octonion multiplication is NOT associative, but the Jordan product
of 3x3 Hermitian matrices over O is well-defined because:
  - For Hermitian matrices, (AB)_{ij} = sum_k A_{ik} * B_{kj} involves
    products of the form x * y_bar where x, y are off-diagonal octonion entries
  - The sum AB + BA is always Hermitian when A, B are Hermitian
  - The Artin theorem guarantees: any subalgebra of O generated by 2 elements
    is associative. Each entry of AB involves sums of products of 2 octonion
    elements at a time, so parenthesization does not matter term-by-term.
  - For h_3(O) specifically: Jordan, von Neumann, and Wigner (1934) proved
    the Jordan identity (A circ B) circ A^2 = A circ (B circ A^2) holds.

STEPS:
1. Compute P = AB (formal 3x3 matrix product with octonion entries)
   - 9 entries, each = sum of 3 octonion products
   - P_{ij} = A_{i1}*B_{1j} + A_{i2}*B_{2j} + A_{i3}*B_{3j}

2. Compute Q = BA (same procedure)

3. C_{ij} = (1/2)(P_{ij} + Q_{ij}) for each entry

4. VERIFY: C is Hermitian (C_{ij} = C_{ji}_bar to machine precision)

COMPLEXITY: 54 octonion multiplications total (27 for AB, 27 for BA)
            Each octonion multiplication: ~64 real multiplications
            Total: ~3500 real multiplications -> microseconds
```

### 5. Peirce Multiplication Operator L_e

| Algorithm | Problem | Convergence | Cost per Step | Memory | Key Reference |
|-----------|---------|-------------|---------------|--------|---------------|
| Direct Jordan product | L_e(X) = e circ X for e = E_11 | Exact | Same as Jordan product | 27 floats | derivations/11-peirce-complexification.md |
| Shortcut formula | L_{E_11}(X) directly from components | Exact | O(16) flops | 27 floats | Phase 18-01, Step 2 |

#### Algorithm: Peirce Multiplication by E_11 (Shortcut)

```
INPUT:  X = (alpha, beta, gamma, x1, x2, x3) in h_3(O)
OUTPUT: L_{E_11}(X) = E_11 circ X

From Phase 18-01, the explicit formula is:
  E_11 circ X = (alpha, 0, 0, 0, x2/2, x3/2)

That is:
  - Diagonal: (alpha, 0, 0) -- eigenvalue 1 on alpha, eigenvalue 0 on beta, gamma
  - Off-diagonal: (0, x2/2, x3/2) -- eigenvalue 1/2 on x2, x3; eigenvalue 0 on x1

This confirms the Peirce decomposition:
  V_1 = {alpha * E_11} (eigenvalue 1, dim 1)
  V_{1/2} = {(0, 0, 0, 0, x2, x3)} (eigenvalue 1/2, dim 16)
  V_0 = {(0, beta, gamma, x1, 0, 0)} (eigenvalue 0, dim 10)

NO OCTONION MULTIPLICATION NEEDED for L_{E_11}. It is a linear projection.
```

### 6. KEY COMPUTATION: Peirce Multiplication by a in V_1

| Algorithm | Problem | Convergence | Cost per Step | Memory | Key Reference |
|-----------|---------|-------------|---------------|--------|---------------|
| General L_a on V_{1/2} | Compute L_a(x) for a in V_1, x in V_{1/2} | Exact | ~54 octonion mults | 27+27 floats | This investigation |

This is the CENTRAL computation. The question: for a = lambda * E_11 (the only elements of V_1, since V_1 = R * E_11), does L_a act on V_{1/2} in a way that could encode multiplication by i?

#### Algorithm: L_{lambda*E_11} on V_{1/2}

```
INPUT:  a = lambda * E_11 (element of V_1, lambda in R)
        x = (0, 0, 0, 0, x2, x3) (element of V_{1/2})
OUTPUT: L_a(x) = a circ x

COMPUTATION:
  a circ x = (lambda * E_11) circ x = lambda * (E_11 circ x) = lambda * (x/2)
           = (0, 0, 0, 0, lambda*x2/2, lambda*x3/2)

RESULT: L_a acts as SCALAR MULTIPLICATION by lambda/2 on V_{1/2}.

THIS IS THE V_1 = R BOTTLENECK identified in v6.0 Phase 22.
Since V_1 = R * E_11 is 1-dimensional, the only Peirce multiplication
operators from V_1 to V_{1/2} are real scalars. There is no room for
an imaginary unit i to appear through this mechanism.
```

### 7. EXTENDED COMPUTATION: Peirce Multiplication by Elements NOT in V_1

The v6.0 investigation exhausted the V_1 route. The new milestone must check whether elements from OUTSIDE V_1 -- specifically from h_3(O) itself or from the complexified algebra h_3^C(O) -- can produce an operator on V_{1/2} that acts as multiplication by i.

#### Algorithm: General Peirce-Type Action on V_{1/2}

```
INPUT:  a = arbitrary element of h_3(O) (27 real parameters)
        x = element of V_{1/2} (16 real parameters)
OUTPUT: Pi_{1/2}(a circ x) = projection of (a circ x) onto V_{1/2}

STEPS:
1. Compute c = a circ x using Algorithm 4 (Jordan product)
2. Extract V_{1/2} component of c:
   Pi_{1/2}(c) = (0, 0, 0, 0, c.x2, c.x3)
   (project out the V_1 and V_0 parts)
3. The operator T_a: V_{1/2} -> V_{1/2} defined by T_a(x) = Pi_{1/2}(a circ x)
   is a linear map on R^16.
4. Represent T_a as a 16x16 real matrix by evaluating on a basis of V_{1/2}.

QUESTION: Does there exist a in h_3(O) (or a in h_3^C(O)) such that
(T_a)^2 = -Id on R^16?

APPROACH:
- For each of the 27 basis elements e_k of h_3(O), compute the 16x16
  matrix (T_{e_k})
- Check if any real linear combination sum_k c_k * T_{e_k} squares to -Id
- This is a system of polynomial equations in 27 variables (the c_k)
  with 256 equations (entries of T^2 + Id = 0)
```

### 8. Spin(9) -> Spin(10) Representation Matrices

| Algorithm | Problem | Convergence | Cost per Step | Memory | Key Reference |
|-----------|---------|-------------|---------------|--------|---------------|
| Spin(9) from Cl(9) | Build 16x16 Spin(9) generators on V_{1/2} | Exact | O(16^3) per generator | 36 * 256 floats | Parton-Piccinni, arXiv:1810.06288 |
| Spin(10) embedding | Extend to 16x16 complex Spin(10) | Exact | O(16^3) per generator | 45 * 256 complex floats | Todorov, arXiv:2206.06912 |

#### Algorithm: Spin(9) on V_{1/2} = O^2 via Octonionic Matrices

```
INPUT:  Fano multiplication table for O
OUTPUT: 36 generators of spin(9) as 16x16 real matrices acting on V_{1/2}

APPROACH 1 (from Clifford algebra):
  Build Cl(9) on R^16 using the standard recursive tensor product construction:
  - 4 sigma_3/sigma_1/sigma_2/I2 tensor products give 8 generators of Cl(8)
    on R^16 = (R^2)^{tensor 4} [Cl(8) = R(16)]
  - The 9th generator: Gamma_9 = product of all 8 generators (volume element
    of Cl(8), which anti-commutes with all 8 in Cl(9))
  - spin(9) generators: (1/4)[Gamma_A, Gamma_B] for A < B, giving 36 generators

APPROACH 2 (octonionic model, Parton-Piccinni):
  The 9 Cl(9) generators I_1, ..., I_9 are 16x16 real symmetric matrices
  acting on R^16 = O^2. They are the octonionic analogues of Pauli matrices.
  Explicit formulas in terms of left multiplication by octonion units:
    I_k for k=1,...,7: related to L_{e_k} (left multiplication by e_k on O^2)
    I_8, I_9: involving the octonionic "Pauli matrices" sigma_1^O, sigma_3^O

  This approach directly uses the O^2 = V_{1/2} identification.

RECOMMENDATION: Use Approach 1 (tensor product) for NUMERICAL verification
because the existing test_cl6_sm.py code already implements this pattern.
Use Approach 2 for CROSS-VALIDATION to confirm the two constructions give
equivalent representations.

SPIN(10) EXTENSION:
  Complexify: R^16 -> C^16. The 9 real generators embed as Hermitian
  matrices in M_16(C). The 10th generator comes from i * Gamma_chirality
  (where Gamma_chirality = Gamma_1 * ... * Gamma_9 in Cl(9)).
  This extends spin(9) to spin(10) inside M_16(C).
  The 16-dim complex rep is S_{10}^+ (positive Weyl spinor of Spin(10)).
```

## Software Ecosystem

### Primary Tools

| Tool | Version | Purpose | License | Maturity |
|------|---------|---------|---------|----------|
| NumPy | 2.4.x | Dense matrix operations, octonion component storage | BSD | Stable |
| Python | 3.14.x | Runtime | PSF | Stable |
| pytest | 9.x | Test framework (existing project pattern) | MIT | Stable |

### Supporting Tools

| Tool | Version | Purpose | When Needed |
|------|---------|---------|-------------|
| SymPy | 1.13.x | Symbolic computation if parametric proofs needed | Only if numerical spot-checks suggest a general pattern worth proving symbolically |
| SciPy | 1.17.x | SVD, eigendecomposition for operator analysis | Analyzing spectrum of T_a operators |
| clifford (pygae) | 1.5.x | Cross-validation of Cl(9)/Cl(10) construction only | Optional: for verifying hand-built Clifford generators |

### Tools NOT to Use

| Tool | Why Not | What Instead |
|------|---------|-------------|
| hypercomplex (PyPI) | Toy library, Cayley-Dickson only, no matrix operations, no tests against Fano conventions | Hand-rolled octonion class |
| pyoctonion (PyPI) | Undocumented, no test suite, no maintenance | Hand-rolled octonion class |
| SplitOct | Split octonions != division octonions (different algebra) | Hand-rolled for division octonions |
| Mathematica | License cost, not in project stack, no automation | Python/NumPy |
| Magma | Proprietary CAS, not in project stack | Python/NumPy |
| galgebra | Symbolic GA, too slow for 16x16 numerical matrices, not designed for non-associative algebras | NumPy for numerical, SymPy for symbolic if needed |

## Data Flow

```
Fano multiplication table (7 triples, fixed convention)
  -> Octonion class (R^8, multiply, conjugate, norm)
  -> h_3(O) element class (3 reals + 3 octonions = 27 reals)
  -> Jordan product A circ B = (1/2)(AB + BA)
  -> Peirce decomposition: V_1, V_{1/2}, V_0 projections
  -> L_a operator: h_3(O) -> End(V_{1/2}) for any a in h_3(O)
  -> 16x16 matrix representation of L_a|_{V_{1/2}}
  -> Eigenvalue analysis: does L_a^2 = -Id for any a?
  -> Spin(9)/Spin(10) generators for cross-check
```

## Computation Order and Dependencies

| Step | Depends On | Produces | Can Parallelize? |
|------|-----------|----------|-----------------|
| 1. Octonion arithmetic module | Fano convention from ASSERT_CONVENTION | Octonion class with multiply/conjugate/norm | Yes (independent) |
| 2. h_3(O) element class | Step 1 | h_3(O) data structure with Jordan product | No (needs Step 1) |
| 3. Peirce projections | Step 2 | V_1, V_{1/2}, V_0 extractors | No (needs Step 2) |
| 4. L_a operator matrices | Steps 2, 3 | 16x16 real matrices for each basis element a | No (needs Steps 2-3) |
| 5. Complex structure search | Step 4 | YES/NO: existence of a with T_a^2 = -Id | No (needs Step 4) |
| 6. Cl(9) generators | None (tensor product construction) | 9 generators of Cl(9) on R^16 | Yes (independent of Steps 1-5) |
| 7. Spin(9) on V_{1/2} cross-check | Steps 4, 6 | Confirm T_a matrices lie in spin(9) image | No (needs Steps 4, 6) |
| 8. Spin(10) complexification | Steps 6, 7 | 10th generator, complex 16-dim rep | No (needs Steps 6-7) |

## Resource Estimates

| Computation | Time (estimate) | Memory | Storage | Hardware |
|-------------|-----------------|--------|---------|----------|
| Octonion module + tests | Minutes (coding) | < 1 MB | Negligible | Laptop CPU |
| h_3(O) Jordan products | Microseconds per product | < 1 MB | Negligible | Laptop CPU |
| All 27 T_a matrices (16x16) | Milliseconds total | < 1 MB | Negligible | Laptop CPU |
| Complex structure search (polynomial system) | Seconds to minutes | < 10 MB | Negligible | Laptop CPU |
| Cl(9)/Cl(10) on R^16/C^16 | Milliseconds | < 1 MB | Negligible | Laptop CPU |

This is a computationally trivial problem. The challenge is algebraic correctness, not computational cost.

## Integration with Existing Code

- **Input formats:** The existing test_cl6_sm.py uses 32x32 complex NumPy matrices for Cl(10) generators. The new code works at the 16x16 real (or complex after complexification) level, which is a subspace of the 32-dim Dirac spinor.
- **Output formats:** 16x16 real or complex matrices, consistent with NumPy ndarray format.
- **Interface points:** The Cl(9) generators from Approach 1 (tensor product) can be compared entry-by-entry with the first 9 of the 10 generators from test_cl6_sm.py restricted to the appropriate 16-dim subspace.
- **Convention bridge:** test_cl6_sm.py uses the convention fano_e1e2=e4 and complex_structure=u_equals_e7. The new octonion module must match this exactly.

## Open Questions

| Question | Why Open | Impact on Project | Approaches Being Tried |
|----------|---------|-------------------|----------------------|
| Can any element of h_3^C(O) (not just h_3(O)) produce T_a^2 = -Id on V_{1/2}? | Complexified algebra has 27 complex = 54 real parameters; larger search space | If YES: complexification mechanism found. If NO: confirms v6.0 negative. | Compute all T_a matrices, form the polynomial system, solve |
| Does the Spin(10) embedding naturally provide the complex structure on V_{1/2}? | The 10th generator of Cl(10) involves i, which may define the sought complex structure | Could bypass the Peirce route entirely | Build Cl(10), extract the 10th generator restricted to V_{1/2}, check if it squares to -Id on R^16 |
| Is the Peirce multiplication L_{V_0}: V_{1/2} -> V_{1/2} richer than L_{V_1}? | V_0 = h_2(O) is 10-dimensional, giving a 10-parameter family of operators | May provide complex structure that V_1 cannot | Compute all T_a for a in V_0 basis elements |

## Anti-Approaches

| Anti-Approach | Why Avoid | What to Do Instead |
|---------------|-----------|-------------------|
| Using external octonion libraries (hypercomplex, pyoctonion) | Untested against Fano conventions, no h_3(O) support, no correctness guarantees | Build from Fano table with project convention |
| Symbolic computation of general Jordan product in SymPy | Too slow for 3x3 octonion matrices (expressions explode combinatorially), non-associativity not natively supported | Numerical computation with exact rational arithmetic or high-precision floats |
| Searching for complex structure via optimization (gradient descent on ||T_a^2 + Id||) | Non-convex landscape, local minima, misses the algebraic structure | Direct algebraic approach: compute all T_a, check linear algebra conditions |
| Building Spin(9) from F_4 generators | F_4 is 52-dimensional and hard to represent explicitly; Spin(9) from Cl(9) is simpler | Tensor product construction for Cl(9), then extract spin(9) |

## Logical Dependencies

```
Fano convention -> Octonion multiplication -> h_3(O) Jordan product
h_3(O) Jordan product -> Peirce decomposition (V_1, V_{1/2}, V_0)
Peirce decomposition -> L_a operator extraction -> 16x16 matrices
16x16 matrices -> Complex structure search (T_a^2 = -Id?)
16x16 matrices -> Spin(9) identification (cross-check with Cl(9))
Cl(9) tensor product construction -> Spin(9) generators (independent path)
Spin(9) generators + complexification -> Spin(10) generators
Spin(10) 10th generator -> Alternative complex structure source
```

## Recommended Investigation Scope

Prioritize:
1. **Octonion module + h_3(O) Jordan product** (foundation for everything)
2. **All 27 T_a matrices on V_{1/2}** (the core computation answering the central question)
3. **Cl(9)/Cl(10) generators and cross-check** (independent verification path)

Defer:
- **Symbolic proofs over general parameters:** Only pursue if numerical results suggest a clean algebraic pattern.
- **F_4 orbit analysis:** Not needed for the computational verification; this is a representation-theoretic question.
- **Generation structure (3 generations):** Out of scope for this milestone.

## Validation Strategy

| Result | Validation Method | Benchmark | Source |
|--------|------------------|-----------|--------|
| Octonion multiplication | e_i^2 = -1 for all i; norm multiplicativity on random pairs | Exact identity | Baez (2002) Table 1 |
| Octonion non-associativity | (e1*e2)*e3 != e1*(e2*e3) but Artin theorem: (e_i*e_j)*e_j = e_i*(e_j*e_j) = -e_i | Exact comparison | Baez (2002), Sec. 2.1 |
| h_3(O) Jordan identity | (A circ B) circ A^2 = A circ (B circ A^2) on random A, B | Machine precision | Jordan-von Neumann-Wigner (1934) |
| Peirce eigenvalues | dim(V_1) = 1, dim(V_{1/2}) = 16, dim(V_0) = 10 | Exact dimensions | derivations/11-peirce-complexification.md |
| Peirce multiplication rules | V_1 circ V_{1/2} subset V_{1/2}, V_0 circ V_{1/2} subset V_{1/2}, V_1 circ V_0 = 0 | Exact (zero entries) | Standard Peirce theory |
| L_{E_11} on V_{1/2} | Acts as scalar 1/2 | Exact | Phase 18-01, Step 2 |
| Cl(9) Clifford relations | {Gamma_A, Gamma_B} = 2*delta_{AB}*I_16 for all A,B in 1..9 | Machine precision | Clifford algebra definition |
| Spin(9) on V_{1/2} | 36 generators of spin(9) match the 16x16 rep restricted from 32x32 Cl(10) | Matrix equality to machine precision | test_cl6_sm.py comparison |

## Sources

- Baez, "The Octonions," Bull. AMS 39 (2002), 145-205. arXiv:math/0105155 -- Octonion multiplication table, F_4 = Aut(h_3(O)), Spin(9) spinor rep
- Dray and Manogue, "The Geometry of the Octonions" (2015), World Scientific -- Octonionic eigenvalue problem, explicit matrix computations
- Dray and Manogue, "The Octonionic Eigenvalue Problem," Adv. Appl. Cliff. Alg. 8 (1998) 323-340. arXiv:math/9807126 -- Eigenvalues of 3x3 octonionic Hermitian matrices
- Todorov, "Octonion Internal Space Algebra for the Standard Model," Universe 9 (2023) 222. arXiv:2206.06912 -- Cl(10) from octonionic left multiplication, Pati-Salam from Cl(6)
- Parton and Piccinni, "The Role of Spin(9) in Octonionic Geometry," Axioms 7 (2018) 72. arXiv:1810.06288 -- Explicit Spin(9) matrices on R^16, canonical 8-form
- Jordan, von Neumann, Wigner, "On an Algebraic Generalization of the Quantum Mechanical Formalism," Ann. Math. 35 (1934) 29-64 -- Classification of formally real Jordan algebras
- Albert, "On a Certain Algebra of Quantum Mechanics," Ann. Math. 35 (1934) 65-73 -- Exceptional Jordan algebra h_3(O)
- Boyle, "The Standard Model, the Exceptional Jordan Algebra, and Triality," arXiv:2006.16265 -- V_{1/2} = S_{10}^+, 27 -> 1+10+16 decomposition
- Existing project code: tests/test_cl6_sm.py (32x32 Cl(10)/Cl(6) matrices, Witt operators, SM quantum numbers)
- Existing derivation: derivations/11-peirce-complexification.md (Peirce decomposition, complexification argument)
