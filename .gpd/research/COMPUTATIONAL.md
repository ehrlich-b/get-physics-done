# Computational Approaches: Spectral Triple Verification for Standard Model Extension

**Surveyed:** 2026-03-22
**Domain:** Noncommutative geometry / Finite spectral triples / Algebraic quantum field theory
**Confidence:** MEDIUM-HIGH

### Scope Boundary

COMPUTATIONAL.md covers computational TOOLS, libraries, algorithms, and infrastructure for verifying spectral triple axioms and constructing finite spectral triples on doubled Hilbert spaces H = C^{2n^2}. It does NOT cover the physics/mathematics of why these axioms matter (PRIOR-WORK.md) or the analytical proof strategies (METHODS.md).

**Relationship to existing codebase:** The project already has a working Python/SymPy + NumPy/SciPy computational framework with 658+ tensor product tests and exact diagonalization up to N=20 spin chains. This document covers EXTENSIONS needed: symbolic commutator computation on doubled spaces, systematic axiom checking, and matrix representations of J/gamma/D operators.

## Recommended Stack

Use Python/SymPy for all symbolic spectral triple verification, with NumPy for explicit numerical checks at specific n. No dedicated noncommutative geometry software package exists in the Python ecosystem -- the field has no mature computational library. The correct approach is to build targeted verification routines on top of SymPy's symbolic matrix algebra and NumPy's dense linear algebra, which the project already uses.

The key insight: for finite spectral triples on H = C^{2n^2}, every operator (D, J, gamma, pi(a), J pi(b*) J^{-1}) is an explicit matrix. The "axiom verification" problem reduces to matrix algebra: computing commutators of explicit matrices and checking they vanish. This is straightforward dense linear algebra, not a research-level computational challenge. The hard part is organizing the computation systematically, not the computation itself.

**Primary approach:** SymPy symbolic matrices for general-n proofs (parametric verification), NumPy explicit matrices for n=2,3,4 spot-checks. The project's existing SymPy patterns (Peirce decomposition, spectral extension) transfer directly.

## Numerical Algorithms

### 1. Zero-Order Condition Verification: [pi(a), J pi(b*) J^{-1}] = 0

| Algorithm | Problem | Convergence | Cost per Step | Memory | Key Reference |
|-----------|---------|-------------|---------------|--------|---------------|
| Explicit commutator sweep | Check [pi(a), J pi(b*) J^{-1}] = 0 for all a,b in A | Exact (finite-dim) | O(dim(A)^2 * dim(H)^3) | O(dim(H)^2) | van Suijlekom, Ch. 3 |
| Basis reduction | Check on basis elements {E_ij} only (linearity) | Exact | O(n^4 * (2n^2)^3) for A = M_n(C) | O((2n^2)^2) | Standard linear algebra |

#### Algorithm: Zero-Order Condition Check

```
INPUT:  Algebra A = M_n(C) represented on H = C^{2n^2}
        Representation pi: A -> End(H)
        Real structure J: H -> H (antilinear isometry)
OUTPUT: Boolean (zero-order condition satisfied or not)

1. Choose basis {E_ij}_{i,j=1}^n for M_n(C)
   - E_ij has 1 in position (i,j), 0 elsewhere

2. Construct opposite representation:
   - pi_o(b) := J pi(b*) J^{-1} for each basis element b = E_ij
   - b* = E_ji (adjoint = transpose for matrix units)
   - Compute pi_o(E_ij) = J pi(E_ji) J^{-1} as explicit 2n^2 x 2n^2 matrix

3. For each pair (i,j), (k,l) with 1 <= i,j,k,l <= n:
   - Compute comm = pi(E_ij) @ pi_o(E_kl) - pi_o(E_kl) @ pi(E_ij)
   - Check ||comm||_F < epsilon (Frobenius norm)
   - If any pair fails: RETURN False, report failing pair

4. RETURN True

COMPLEXITY: n^4 commutator checks, each O((2n^2)^3) matrix multiply
            Total: O(n^4 * n^6) = O(n^{10})
            For n=2: ~1024 multiplies of 8x8 matrices -> microseconds
            For n=3: ~6561 multiplies of 18x18 matrices -> milliseconds
            For n=4: ~65536 multiplies of 32x32 matrices -> seconds
```

#### Convergence Properties

- **Exact for explicit matrices:** No convergence issue. The commutator is computed exactly (symbolic) or to machine precision (numerical).
- **Basis sufficiency:** Because the commutator is bilinear, checking on all pairs of basis elements E_ij suffices. If [pi(E_ij), pi_o(E_kl)] = 0 for all i,j,k,l, then [pi(a), pi_o(b)] = 0 for all a,b by linearity.
- **Known failure mode:** None for the computation itself. The mathematical question is whether a given J satisfies this condition for a given representation pi.

### 2. First-Order Condition Verification: [[D, pi(a)], J pi(b*) J^{-1}] = 0

| Algorithm | Problem | Convergence | Cost per Step | Memory | Key Reference |
|-----------|---------|-------------|---------------|--------|---------------|
| Double commutator sweep | Check [[D,a], Jb*J^{-1}] = 0 for all a,b | Exact | O(n^4 * (2n^2)^3) | O((2n^2)^2) | Cacic arXiv:0902.2068 |
| Parametric D construction | Find D satisfying first-order condition | Linear system solve | O(dim(D-space)^2 * n^4) | O(dim(D-space) * (2n^2)^2) | Cacic arXiv:0902.2068 |

#### Algorithm: First-Order Condition as Linear Constraints on D

```
INPUT:  Algebra A = M_n(C), representation pi on H = C^{2n^2}
        Real structure J, grading gamma
        D is UNKNOWN: self-adjoint operator on H with D*gamma = -gamma*D, J*D = D*J
OUTPUT: The vector space of Dirac operators satisfying first-order condition

1. Parametrize D:
   - D is a self-adjoint 2n^2 x 2n^2 matrix: D = D^dagger
   - Constraint D*gamma = -gamma*D: D is off-diagonal in the gamma eigenspaces
   - Constraint J*D*J^{-1} = epsilon'*D (epsilon' from KO-dimension table)
   - These are linear constraints reducing dim(D-space) from (2n^2)^2 to
     a much smaller parameter space

2. Write D = sum_alpha c_alpha * B_alpha where {B_alpha} is a basis
   for the constrained space (self-adjoint, anti-commutes with gamma,
   commutes or anti-commutes with J as required)

3. For each basis element E_ij of A and each E_kl of A:
   - Compute [D, pi(E_ij)] = sum_alpha c_alpha * [B_alpha, pi(E_ij)]
   - Compute [[D, pi(E_ij)], pi_o(E_kl)]
     = sum_alpha c_alpha * [[B_alpha, pi(E_ij)], pi_o(E_kl)]
   - Set equal to zero: this gives linear equations in {c_alpha}

4. Collect all equations from step 3 into a matrix equation M * c = 0
   where c = (c_1, ..., c_dim) is the parameter vector

5. Solve: null space of M gives the moduli space of allowed Dirac operators
   - Use SVD: M = U S V^T, null space = columns of V with singular value < epsilon
   - Dimension of null space = number of free parameters in D

COMPLEXITY: Step 3 generates n^4 constraints (one per pair E_ij, E_kl),
            each involving dim(D-space) parameters
            Matrix M has n^4 * (2n^2)^2 rows, dim(D-space) columns
            SVD: O(min(rows, cols)^2 * max(rows, cols))
```

**This is the core algorithm.** Cacic (arXiv:0902.2068) calls the output space D_0(A, H, P) -- the moduli space of Dirac operators for the finite spectral triple. Computing it is a finite-dimensional linear algebra problem.

### 3. First-Order Condition Subalgebra

| Algorithm | Problem | Convergence | Cost per Step | Memory | Key Reference |
|-----------|---------|-------------|---------------|--------|---------------|
| Subalgebra extraction | Given D, find largest A_F subset A with [[D,a], Jb*J^{-1}] = 0 | Exact | O(n^6 * (2n^2)^3) | O(n^2 * (2n^2)^2) | Chamseddine-Connes arXiv:0706.3688 |

#### Algorithm: First-Order Condition Subalgebra

```
INPUT:  Fixed Dirac operator D on H = C^{2n^2}
        Algebra A = M_n(C), representation pi, real structure J
OUTPUT: Maximal subalgebra A_F of A satisfying first-order condition

1. For each basis element E_ij of A:
   - Compute [D, pi(E_ij)] as a 2n^2 x 2n^2 matrix
   - Store as matrix M_ij

2. For each pair (E_ij, E_kl):
   - Compute [M_ij, pi_o(E_kl)] = [M_ij, J pi(E_lk) J^{-1}]
   - If nonzero: record that the pair (E_ij, E_kl) violates first-order

3. Build violation graph:
   - Vertices = basis elements {E_ij}
   - Edge (E_ij, E_kl) if the double commutator [[D, E_ij], J E_kl* J^{-1}] != 0

4. Find maximal subalgebra:
   - A_F must be closed under multiplication and adjoint
   - A_F = span of {E_ij : for ALL E_kl in A_F, [[D, E_ij], J E_kl* J^{-1}] = 0
                     AND for ALL E_kl in A_F, [[D, E_kl], J E_ij* J^{-1}] = 0}
   - Start with A_F = A. Remove any generator that violates.
     Iterate until stable. (Shrinking iteration always terminates for finite dim.)

5. Identify structure of A_F:
   - Compute its center, check if it decomposes as direct sum of matrix blocks
   - For Standard Model: expect A_F = C + H + M_3(C) [Chamseddine-Connes]

COMPLEXITY: Step 2 is O(n^4) double commutators of (2n^2)x(2n^2) matrices
            Step 4 is iterative but terminates in at most n^2 steps
```

**Physical significance:** The first-order condition subalgebra is what selects the Standard Model gauge group from the "input" algebra. Chamseddine-Connes showed that starting from A = M_2(H) + M_4(C) (or similar), the first-order condition on D forces the subalgebra to be C + H + M_3(C), which gives U(1) x SU(2) x SU(3) after unimodularity.

### 4. Grading and Real Structure Construction

| Algorithm | Problem | Convergence | Cost per Step | Memory | Key Reference |
|-----------|---------|-------------|---------------|--------|---------------|
| Grading enumeration | Find all gamma with gamma^2 = 1, gamma pi(a) = pi(a) gamma | Exact | O(n^2 * (2n^2)^3) | O((2n^2)^2) | van Suijlekom Ch. 3 |
| J construction | Find antilinear J with J^2 = epsilon, JD = epsilon'DJ, J gamma = epsilon'' gamma J | Exact | O((2n^2)^3) per candidate | O((2n^2)^2) | Connes, Barrett |

#### Algorithm: Constructing J (Real Structure)

```
INPUT:  H = C^{2n^2}, representation pi: A -> End(H)
        KO-dimension k (determines signs epsilon, epsilon', epsilon'')
OUTPUT: Antilinear isometry J satisfying J^2 = epsilon * id,
        J gamma = epsilon'' gamma J (if even),
        and zero-order condition [pi(a), J pi(b*) J^{-1}] = 0

KO-dimension sign table (mod 8):
  k:  0    1    2    3    4    5    6    7
  e:  1    1   -1   -1   -1   -1    1    1
  e': 1   -1    1    1    1   -1    1    1
  e'': 1       -1         1        -1

(e = epsilon = J^2, e' = epsilon' = JD vs DJ, e'' = epsilon'' = J*gamma vs gamma*J)

1. Represent J as J = C * K where C is a unitary matrix and K is
   complex conjugation (K v = v* componentwise in chosen basis)
   - J antilinear: J(alpha v) = alpha* J(v)
   - J isometry: <Jv, Jw> = <w, v>
   - Then C must be unitary: C^dagger C = I

2. Constraint J^2 = epsilon:
   - J^2 v = C K C K v = C C* v (since K C K = C*)
   - So C C* = epsilon * I
   - For epsilon = +1: C is symmetric unitary (C = C^T)
   - For epsilon = -1: C is antisymmetric unitary (C = -C^T)

3. Zero-order condition [pi(a), J pi(b*) J^{-1}] = 0:
   - J pi(b*) J^{-1} v = C (pi(b*))* C^{-1} v  (using J = CK)
   - So pi_o(b) = C (overline{pi(b*)}) C^{-1}
   - Zero-order: pi(a) commutes with C overline{pi(b*)} C^{-1} for all a,b

4. Strategy: write C in the pi-adapted basis. If pi decomposes
   H into irreducible components, C must intertwine them.
   For A = M_n(C) on H = C^{2n^2}: pi is generically the sum of
   the fundamental and its conjugate (or two copies of the fundamental),
   and C swaps them.

5. Solve the linear system for the entries of C subject to all constraints.
   This is finite-dimensional linear algebra.
```

## Software Ecosystem

### Primary Tools

| Tool | Version | Purpose | License | Maturity |
|------|---------|---------|---------|----------|
| NumPy | >= 1.26 | Explicit matrix construction and commutator computation for n=2,3,4 | BSD | Stable |
| SciPy | >= 1.12 | SVD for null space computation (moduli space of D), sparse methods if needed | BSD | Stable |
| SymPy | >= 1.13 | Symbolic/parametric verification at general n; commutator algebra; matrix symbols | BSD | Stable |

### Supporting Tools

| Tool | Version | Purpose | When Needed |
|------|---------|---------|-------------|
| Matplotlib | >= 3.8 | Visualization of moduli space dimensions, constraint counts | For paper figures |
| pytest | >= 8.0 | Test framework for axiom verification suite | Always (CI) |

### Why NOT Other Tools

| Tool | Why Skip | What To Do Instead |
|------|----------|-------------------|
| Mathematica NCAlgebra | Noncommutative Groebner bases; overkill for explicit finite matrix commutators. Not Python-native. | Direct matrix computation in NumPy/SymPy |
| SageMath g_algebra | Good for abstract noncommutative polynomial rings but our problem is EXPLICIT matrices, not abstract algebra | NumPy dense matrix arithmetic |
| GAP | Strong for finite groups and Lie algebras, not for explicit matrix operator verification | NumPy for matrices; GAP irrelevant here |
| No "NCG Python package" exists | Confirmed by search: no mature Python/SymPy/SageMath package for spectral triple computation exists as of 2026 | Build targeted routines (200-400 lines) |

**Key finding from literature survey:** There is NO dedicated computational package for finite spectral triple verification in any language. The NCG community works with hand-constructed examples and pen-and-paper proofs. The closest computational work is:
- Barrett (arXiv:2403.18428, 2024): fermion integrals for finite spectral triples -- computational but focused on path integrals, not axiom verification
- Cacic (arXiv:0902.2068, 2009): moduli spaces of Dirac operators -- systematic framework but no published code
- van Suijlekom textbook (2nd ed., 2024): explicit constructions but no accompanying software

This means we build our own verification suite. The advantage: finite spectral triples on H = C^{2n^2} are small enough (8x8 for n=2, 18x18 for n=3, 32x32 for n=4) that brute-force matrix computation is fast and exact.

### SymPy Features Directly Applicable

| Feature | Module | Use Case |
|---------|--------|----------|
| `Matrix` | `sympy.matrices` | Symbolic matrices with exact arithmetic for general-n patterns |
| `MatrixSymbol` | `sympy.matrices.expressions` | Parametric matrix expressions without specifying entries |
| `commutative=False` symbols | `sympy.core` | Noncommutative symbolic algebra for abstract identities |
| `Commutator` | `sympy.physics.quantum` | Formal commutator objects with algebraic expansion rules |
| `TensorProduct` | `sympy.physics.quantum` | Tensor product of operators on composite Hilbert spaces |
| `kronecker_product` | `sympy.matrices` | Explicit Kronecker product of matrices (numerical tensor product) |
| `tensorproduct` | `sympy.tensor.array` | Array-level tensor products |

**SymPy approach for general-n:** Use `sympy.Matrix` with symbolic entries to construct pi(E_ij), J, gamma, D at general n. The commutator [pi(a), J pi(b*) J^{-1}] is then a symbolic matrix whose entries must all vanish. SymPy can verify this symbolically for small n (n=2,3) and likely for general n if the representation structure is clean.

**NumPy approach for specific n:** At n=2, all matrices are 8x8. At n=3, 18x18. At n=4, 32x32. Construct everything explicitly and compute commutators numerically. This provides independent verification of symbolic results.

## Data Flow

```
Define algebra A = M_n(C), Hilbert space H = C^{2n^2}
  Parameters: n (matrix algebra dimension), KO-dimension k
  -> Construct representation pi: M_n(C) -> End(H)
     (fundamental + conjugate, or left regular + right regular, etc.)
  -> Construct grading gamma (diagonal in eigenspace decomposition)
  -> Construct real structure J = C * K (complex conjugation + unitary)
  -> Verify zero-order condition: [pi(a), J pi(b*) J^{-1}] = 0
     for all basis pairs (E_ij, E_kl)

  -> Parametrize Dirac operator D:
     - Self-adjoint: D = D^dagger
     - Anti-commutes with gamma: D gamma + gamma D = 0
     - Commutation with J: J D J^{-1} = epsilon' D
     -> Write D = sum c_alpha B_alpha (constrained basis)

  -> First-order condition: [[D, pi(a)], J pi(b*) J^{-1}] = 0
     -> Generates linear equations in {c_alpha}
     -> Null space of constraint matrix = moduli space of D
     -> Dimension = number of free parameters

  -> If starting from general A (e.g., M_2(H) + M_4(C)):
     -> Find subalgebra A_F satisfying first-order for given D
     -> Identify gauge group from A_F
```

## Computation Order and Dependencies

| Step | Depends On | Produces | Can Parallelize? |
|------|-----------|----------|-----------------|
| 1. Choose representation of A on H | Algebra structure (input) | pi: A -> End(H) as explicit matrices | No |
| 2. Construct gamma (grading) | Step 1 | gamma as diagonal matrix | No |
| 3. Construct J (real structure) | Step 1, KO-dimension choice | J = C * K as explicit unitary C | No |
| 4. Verify zero-order condition | Steps 1, 3 | Boolean + violation report | Yes (pairs independent) |
| 5. Parametrize D (constrained space) | Steps 2, 3 | Basis {B_alpha} for allowed D | No |
| 6. First-order condition constraints | Steps 1, 3, 5 | Constraint matrix M | Yes (pairs independent) |
| 7. Solve null space of M | Step 6 | Moduli space D_0(A,H,P), dimension | No |
| 8. Subalgebra extraction (if needed) | Steps 1, 3, specific D from Step 7 | A_F and its structure | No |

**Critical path:** Steps 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
Steps 4 and 6 are the computationally intensive parts but trivial in practice for n <= 4.

## Resource Estimates

| Computation | Time (estimate) | Memory | Storage | Hardware |
|-------------|-----------------|--------|---------|----------|
| Zero-order check, n=2 (8x8 matrices) | < 1 ms | < 1 MB | Negligible | Local CPU |
| Zero-order check, n=3 (18x18 matrices) | < 10 ms | < 1 MB | Negligible | Local CPU |
| Zero-order check, n=4 (32x32 matrices) | < 100 ms | < 1 MB | Negligible | Local CPU |
| Parametrize D space, n=2 | < 1 s | < 10 MB | Negligible | Local CPU |
| Parametrize D space, n=3 | < 10 s | < 100 MB | Negligible | Local CPU |
| Parametrize D space, n=4 | < 1 min | < 1 GB | Negligible | Local CPU |
| First-order constraint matrix + SVD, n=2 | < 1 s | < 10 MB | Negligible | Local CPU |
| First-order constraint matrix + SVD, n=3 | < 30 s | < 100 MB | Negligible | Local CPU |
| First-order constraint matrix + SVD, n=4 | < 5 min | < 1 GB | Negligible | Local CPU |
| Symbolic verification, general n (SymPy) | 1-30 min depending on pattern | < 4 GB | Negligible | Local CPU |
| Full axiom suite, n=2 through n=4 | < 10 min total | < 1 GB peak | < 1 MB output | Local CPU |

**Everything is laptop-scale.** No HPC, no GPU, no cluster needed. The bottleneck is human time organizing the computation, not compute time.

## Integration with Existing Code

The project already has:
- **Python/SymPy framework** for algebraic verification (test_spectral_extension.py: Peirce decomposition, Luders product, functional equations)
- **NumPy/SciPy** for exact diagonalization and eigendecomposition
- **Test patterns** using random matrix construction, sweep over parameters, error threshold checking

**Input formats:** Existing code uses `np.ndarray` for matrices and `np.linalg.eigh` for eigendecomposition. New spectral triple code uses the same.

**Output formats:** Existing tests produce pass/fail with max error reports. New axiom checks follow the same pattern.

**Interface points:**
1. The Peirce decomposition code (`peirce_product`, `peirce_product_general_s`) from test_spectral_extension.py operates on the SAME M_n(C)^sa algebras. The spectral triple verification acts on the DOUBLED space where these algebras are represented.
2. The `random_effect` and `random_effect_real` helper functions generalize directly to constructing test elements of M_n(C) for axiom checking.
3. The test infrastructure (pytest, assertion patterns, error reporting) carries over unchanged.

**New code estimate:** ~400-600 lines of Python:
- ~100 lines: representation construction (pi, pi_o, J, gamma for given n and KO-dim)
- ~100 lines: zero-order condition checker
- ~150 lines: D parametrization and first-order constraint matrix builder
- ~100 lines: subalgebra extraction
- ~50-100 lines: test harness and validation

## Open Questions

Questions without consensus answers relevant to the computational approach.

| Question | Why Open | Impact on Project | Approaches Being Tried |
|----------|---------|-------------------|----------------------|
| Which representation of M_n(C) on C^{2n^2} matches the self-modeling construction? | The doubling (H = C^n tensor C^n with L/R action, doubled by gamma) vs. the bimodule doubling (H = A tensor A^o) give different operator structures | Determines pi, hence all downstream computation | Try both; the self-modeling representation should be determined by the sequential product structure from Paper 5 |
| What KO-dimension for the internal finite geometry? | Physical SM uses KO-dim 6 (mod 8) for the finite part. Self-modeling may prefer a different KO-dim. | Fixes epsilon, epsilon', epsilon'' signs, hence J^2 and JD relation | Start with KO-dim 6 (SM standard); verify which KO-dims are compatible with M_n(C) |
| Does the first-order condition subalgebra depend continuously on D? | For a generic D, the subalgebra might jump discontinuously as parameters vary | Affects whether "the" subalgebra is well-defined or depends on fine-tuning | Compute subalgebra dimension as function of D parameters; look for stability |

## Anti-Approaches

Approaches to explicitly NOT pursue.

| Anti-Approach | Why Avoid | What to Do Instead |
|---------------|-----------|-------------------|
| Abstract noncommutative algebra packages (NCAlgebra, SageMath g_algebra) | Our problem is EXPLICIT finite matrices (8x8 to 32x32), not abstract polynomial manipulation. These tools solve a different problem. | Direct NumPy matrix arithmetic + SymPy symbolic matrices |
| Krajewski diagram enumeration for general classification | Krajewski diagrams classify ALL possible finite spectral triples. We need to verify ONE specific triple (the self-modeling one). Classification is useful background but not our computational task. | Construct the specific triple from the self-modeling representation and verify it directly |
| Infinite-dimensional spectral triple methods | Spectral truncations, Dirac operator spectral theory on manifolds -- all for continuous geometries. Our triple is finite-dimensional by construction. | Finite matrix algebra only |
| GPU acceleration | Maximum matrix size is 32x32 (n=4). GPU overhead exceeds computation time. | CPU-only computation |
| Sparse matrix methods | Maximum matrix size is 32x32. Dense is faster than sparse at this scale. | Dense numpy arrays |

## Logical Dependencies

```
Self-modeling sequential product (Paper 5)
  -> M_n(C)^sa at each site (established)
  -> Doubled Hilbert space H = C^{2n^2} (bimodule structure)
     -> Representation pi of M_n(C) on H
        -> Zero-order condition check (J)
        -> First-order condition (D)
           -> Moduli space of D
           -> Subalgebra A_F
              -> Gauge group identification

Convention: Peirce decomposition (Paper 5 S1-S7)
  -> Compression maps C_{p_i} on M_n(C)^sa
  -> These become building blocks for pi(a) on the doubled space

KO-dimension choice (mod 8)
  -> Signs epsilon, epsilon', epsilon''
     -> Constraints on J and J-D relation
        -> Constraints on D parametrization
```

## Recommended Investigation Scope

Prioritize:
1. **n=2 complete axiom verification** -- smallest nontrivial case, 8x8 matrices, all computations instantaneous. Establish the full pipeline: construct pi, J, gamma, parametrize D, compute moduli space, extract subalgebra. This is the proof-of-concept that validates the computational approach before scaling to n=3,4.
2. **n=3 verification** -- 18x18 matrices, still fast. Physically relevant because M_3(C) is the color algebra of QCD.
3. **General-n symbolic computation** -- use SymPy to verify whether patterns from n=2,3 extend to arbitrary n. This is the hardest computational step but the most valuable for the paper.

Defer:
- **n >= 5:** Only needed if general-n pattern is not clear from n=2,3,4. Resource cost grows as n^{10} for brute-force, though structured computation should be much faster.
- **Product algebras (e.g., M_2(H) + M_4(C)):** This is the SM-specific algebra choice. Only pursue after single-algebra verification is complete.
- **Spectral action computation:** Computing Tr(f(D/Lambda)) for the finite spectral triple. Interesting but not needed for axiom verification.

## Validation Strategy

| Result | Validation Method | Benchmark | Source |
|--------|------------------|-----------|--------|
| Zero-order condition for standard SM triple | Reconstruct known SM result | Must hold for A = C + H + M_3(C) with standard J | van Suijlekom Ch. 11-13 |
| First-order condition selects SM subalgebra | Start from M_2(H) + M_4(C), verify A_F = C + H + M_3(C) | Dimension of A_F = 1 + 4 + 9 = 14 | Chamseddine-Connes arXiv:0706.3688 |
| Moduli space dimension for SM Dirac operator | Count free parameters in D | Should give SM Yukawa coupling count (Dirac masses + mixing matrices) | van Suijlekom Thm 13.12 |
| n=2 M_2(C) self-adjoint part | Verify sequential product from Paper 5 embeds correctly | Peirce formula must reproduce Luders product on embedded effects | test_spectral_extension.py (existing) |
| J^2 = epsilon, J gamma = epsilon'' gamma J | Direct matrix verification | Exact for any valid J, gamma | Axiom definition |
| D self-adjoint, D gamma + gamma D = 0 | Direct matrix verification | Exact for any valid D | Axiom definition |

## Key References

- van Suijlekom, W.D. "Noncommutative Geometry and Particle Physics" 2nd ed. (2024), Springer. Chapters 2-4 (finite spectral triples), 11-13 (Standard Model). The primary textbook reference for explicit finite spectral triple construction. [DOI: 10.1007/978-3-031-59120-4](https://link.springer.com/book/10.1007/978-3-031-59120-4)
- Cacic, B. "Moduli spaces of Dirac operators for finite spectral triples" (2009). [arXiv:0902.2068](https://arxiv.org/abs/0902.2068). Systematic framework for parametrizing the space of allowed Dirac operators; defines D_0(A,H,P) and works out the linear algebra structure.
- Krajewski, T. "Classification of finite spectral triples" (1998). [arXiv:hep-th/9701081](https://arxiv.org/abs/hep-th/9701081). Krajewski diagrams for systematic enumeration of finite spectral triples. Background classification, not directly computational for our purposes.
- Chamseddine, A.H. and Connes, A. "Why the Standard Model" (2007). [arXiv:0706.3688](https://arxiv.org/abs/0706.3688). The first-order condition subalgebra derivation that selects the Standard Model gauge group.
- Barrett, J.W. "Fermion integrals for finite spectral triples" (2024). [arXiv:2403.18428](https://arxiv.org/abs/2403.18428). Recent computational work on finite spectral triples; confirms the field is still done by hand/pen-and-paper.
- Paschke, M. and Sitarz, A. "Discrete spectral triples and their symmetries" (1998). [arXiv:q-alg/9612029](https://arxiv.org/abs/q-alg/9612029). Early structure theory for finite spectral triples.
- Stephan, C.A. "Krajewski diagrams and the Standard Model" (2009). [arXiv:0809.5137](https://arxiv.org/abs/0809.5137). Application of Krajewski classification to the SM.
- SymPy documentation: Matrix Expressions module, Quantum Commutator module. [https://docs.sympy.org/latest/modules/matrices/expressions.html](https://docs.sympy.org/latest/modules/matrices/expressions.html)

## Sources

- van Suijlekom (2024) -- primary reference for finite spectral triple construction algorithms and SM application
- Cacic (2009) -- moduli space of Dirac operators framework
- Barrett (2024) -- confirms no existing computational software in the field
- Chamseddine-Connes (2007) -- first-order condition subalgebra derivation
- SymPy 1.14 documentation -- verified current capabilities for noncommutative symbolic computation
- NCAlgebra GitHub repository -- confirmed focus on abstract noncommutative algebra, not finite matrix spectral triples
- SageMath documentation -- confirmed noncommutative algebra support but not spectral-triple-specific
- GAP documentation -- confirmed focus on discrete algebra/group theory, not operator verification
