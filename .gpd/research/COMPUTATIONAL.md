# Computational Approaches: GR from det(X) on h_3(O)

**Surveyed:** 2026-04-11
**Domain:** Exceptional Jordan algebra / Magic supergravity / Peirce decomposition / Very special real geometry
**Confidence:** HIGH (all algorithms are exact algebraic operations on small-dimensional spaces; existing codebase covers ~60% of what's needed)

## Recommended Stack

Extend the existing `code/octonion_algebra.py` infrastructure with five new modules: (1) h_2(O) data structures and the projection pi_u: h_2(O) -> h_2(C_u), (2) determinant computations on h_3(O) and h_2(O), (3) cubic form d_IJK decomposition under Peirce, (4) group representation machinery for equivariance checks, and (5) KK reduction field content bookkeeping. All computations involve matrices of dimension at most 27x27 (or 16x16 for group actions on V_{1/2}). The existing Python/NumPy/SymPy stack suffices with no new dependencies. SageMath is available as an optional cross-check tool for branching rules but is not required for the core computation pipeline.

The key insight is that h_2(O) = V_0 already has a complete 10-element basis implementation (`V0_basis_elements()`) and Peirce projection (`peirce_V0()`). The new work is primarily: (a) implementing det(X) on h_3(O) and h_2(O) as explicit polynomial functions, (b) constructing pi_u as a concrete linear map, and (c) decomposing the 27-dimensional C_IJK tensor into Peirce blocks. These are all finite-dimensional linear algebra problems, not iterative numerical computations.

---

## Numerical Algorithms

### Algorithm 1: det(X) on h_3(O) -- the Cubic Form

| Algorithm | Problem | Convergence | Cost per Step | Memory | Key Reference |
|-----------|---------|-------------|---------------|--------|---------------|
| Direct formula evaluation | det: h_3(O) -> R | Exact (polynomial) | O(1) per octonion multiply (8x8 table lookup) | O(1) | Baez, Bull. AMS 39 (2002); Faraut-Koranyi (1994) |

**Formula:** For X = (alpha, beta, gamma, x1, x2, x3) in h_3(O):

```
det(X) = alpha * beta * gamma
       - alpha * |x1|^2
       - beta  * |x2|^2
       - gamma * |x3|^2
       + 2 * Re(x1 * (x2 * x3))
```

where |x|^2 = x * conj(x) (octonion norm squared) and Re() extracts the real (e_0) component. The triple product term x1 * (x2 * x3) is NOT associative, but this specific expression is well-defined because we evaluate right-to-left: first compute x2 * x3, then multiply x1 on the left.

**Convergence criterion:** Exact. Verify: det(E_{11}) = 0 (rank-1 idempotent), det(I) = 1 (identity), det(lambda * X) = lambda^3 * det(X).

**Known failure modes:** The triple product Re(x1 * (x2 * x3)) is sensitive to parenthesization because O is non-associative. The formula uses the SPECIFIC ordering x1 * (x2 * x3). Using (x1 * x2) * x3 gives a different answer in general, though for HERMITIAN matrices Re(x1 * (x2 * x3)) = Re((x1 * x2) * x3) by the Moufang identity. This should be verified numerically but is expected to hold exactly.

**Implementation:**
```python
def det_h3o(X):
    """Determinant of X in h_3(O).
    
    det(X) = alpha*beta*gamma - alpha*|x1|^2 - beta*|x2|^2
             - gamma*|x3|^2 + 2*Re(x1*(x2*x3))
    """
    triple = X.x1 * (X.x2 * X.x3)
    return (X.alpha * X.beta * X.gamma
            - X.alpha * X.x1.norm_sq()
            - X.beta * X.x2.norm_sq()
            - X.gamma * X.x3.norm_sq()
            + 2.0 * triple.real_part())
```

### Algorithm 2: det on h_2(O) -- the 10d Quadratic Form

| Algorithm | Problem | Convergence | Cost per Step | Memory | Key Reference |
|-----------|---------|-------------|---------------|--------|---------------|
| Direct formula | det: h_2(O) -> R | Exact | O(1) | O(1) | Standard |

**Formula:** For Y = (beta, gamma, x1) in V_0 = h_2(O) (alpha = x2 = x3 = 0):

```
det_2(Y) = beta * gamma - |x1|^2
```

This is a quadratic form of signature (1,9) on R^{10}: writing beta = (s+t)/2, gamma = (s-t)/2, we get det_2 = (s^2 - t^2)/4 - |x1|^2. Alternatively, writing the 10 coordinates as (beta, gamma, x1[0..7]), the associated bilinear form is the spin factor inner product.

**Relationship to h_3(O) determinant:** When restricted to V_0 (alpha = x2 = x3 = 0), the h_3(O) determinant reduces to: det(X)|_{V_0} = 0 (all three terms involving alpha vanish, and the triple product x1*(0*0) = 0). This is correct because V_0 elements have rank at most 2 in h_3(O), so det = 0 trivially. The h_2(O) determinant is NOT the restriction of det_{h_3(O)} but rather the intrinsic Jordan algebra determinant of the rank-2 algebra h_2(O).

**Implementation:**
```python
def det_h2o(Y):
    """Determinant of Y in h_2(O), the Peirce complement V_0.
    
    Y has beta, gamma (diagonal) and x1 (off-diagonal octonionic entry).
    det = beta*gamma - |x1|^2
    """
    return Y.beta * Y.gamma - Y.x1.norm_sq()
```

### Algorithm 3: Projection pi_u: h_2(O) -> h_2(C_u)

| Algorithm | Problem | Convergence | Cost per Step | Memory | Key Reference |
|-----------|---------|-------------|---------------|--------|---------------|
| Orthogonal projection on octonion space | pi_u: h_2(O) -> h_2(C_u) | Exact (linear) | O(1) | O(1) | Project-specific construction |

**Formula:** For u in S^6 (unit imaginary octonion, e.g., u = e_7):

```
proj_u: O -> C_u = span_R{1, u}
proj_u(x) = Re(x) + <Im(x), u> * u
```

where Im(x) = (x[1], ..., x[7]) and <,> is the R^7 inner product. Then:

```
pi_u: h_2(O) -> h_2(C_u)
pi_u(beta, gamma, x1) = (beta, gamma, proj_u(x1))
```

The diagonal entries (beta, gamma) are real and pass through unchanged. The off-diagonal entry x1 is projected from O to C_u.

**Output dimension:** h_2(C_u) is 4-dimensional: 2 real diagonal + 2 real components of proj_u(x1) = a + b*u. This is isomorphic to h_2(C) = R^{3,1} with det = Minkowski metric.

**Kernel:** ker(pi_u) = {(0, 0, x1) : x1 in u^perp cap Im(O)} has dimension 6. These are the "internal" directions.

**Implementation:**
```python
def proj_u(x, u_index=7):
    """Project octonion x onto C_u = span{1, e_u}.
    
    proj_u(x) = x[0]*e_0 + x[u]*e_u  (for basis unit u = e_{u_index})
    """
    result = np.zeros(8, dtype=np.float64)
    result[0] = x.c[0]          # real part preserved
    result[u_index] = x.c[u_index]  # u-component preserved
    return Octonion(result)

def pi_u(Y, u_index=7):
    """Project h_2(O) element Y to h_2(C_u).
    
    Preserves diagonal (beta, gamma), projects x1 to C_u.
    """
    return H3O(beta=Y.beta, gamma=Y.gamma,
               x1=proj_u(Y.x1, u_index))
```

For general u (not a basis vector), the projection becomes:
```python
def proj_u_general(x, u_vec):
    """Project octonion x onto C_u for general unit imaginary u.
    
    u_vec: 7-component unit vector (imaginary part of u).
    proj(x) = Re(x)*1 + <Im(x), u_vec>*u
    """
    im_x = x.c[1:]  # 7 components
    coeff = np.dot(im_x, u_vec)
    result = np.zeros(8, dtype=np.float64)
    result[0] = x.c[0]
    result[1:] = coeff * u_vec
    return Octonion(result)
```

### Algorithm 4: Cubic Form d_IJK in Peirce Basis

| Algorithm | Problem | Convergence | Cost per Step | Memory | Key Reference |
|-----------|---------|-------------|---------------|--------|---------------|
| Third-order partial derivatives of det(X) | d_IJK = (d^3/dh^I dh^J dh^K) det(X) | Exact (polynomial) | O(27^3) evaluations | O(27^3) = O(20000) floats | GST (1983); de Wit-Van Proeyen (1992) |

**Method:** The cubic form d_IJK encodes det(X) via:

```
det(X) = (1/6) d_IJK h^I h^J h^K
```

where h^I are the 27 coordinates of X in some basis. Compute d_IJK by taking third derivatives (or equivalently, by polarization: d_IJK = det(e_I, e_J, e_K) where det is extended to a symmetric trilinear form).

**Polarization identity:** The symmetric trilinear form associated to det is:

```
det(A, B, C) = (1/6)[det(A+B+C) - det(A+B) - det(A+C) - det(B+C)
                      + det(A) + det(B) + det(C)]
```

Then d_IJK = det(e_I, e_J, e_K) for the 27 standard basis vectors e_I of h_3(O).

**Peirce block structure:** In the Peirce basis {e_1 (V_1), e_2...e_{17} (V_{1/2}), e_{18}...e_{27} (V_0)}, the tensor d_IJK has block structure forced by degree counting:
- d_{111} = 0 (V_1 is 1-dim, contributes at most linearly to det)
- d_{1,half,half} nonzero (these give the V_{1/2} x V_{1/2} -> V_0 bilinear form seen by V_1)
- d_{half,half,0} nonzero (these are the core SM-gravity coupling terms)
- d_{0,0,0} = 0 (V_0 is h_2(O) with rank 2, so its intrinsic det is quadratic, not cubic)

The nonvanishing blocks and their physical interpretation are the central computation of Phase 2.

**Implementation:**
```python
def compute_dIJK(basis_27=None):
    """Compute the full 27x27x27 tensor d_IJK = det(e_I, e_J, e_K).
    
    Uses the polarization identity for the symmetric trilinear form
    associated to the cubic det: h_3(O) -> R.
    
    Returns: (27, 27, 27) numpy array, fully symmetric in all indices.
    """
    if basis_27 is None:
        basis_27 = [H3O.from_vector(np.eye(27)[i]) for i in range(27)]
    
    d = np.zeros((27, 27, 27), dtype=np.float64)
    for I in range(27):
        for J in range(I, 27):
            for K in range(J, 27):
                # Polarization: det(A,B,C) from det evaluations
                eI, eJ, eK = basis_27[I], basis_27[J], basis_27[K]
                val = _trilinear_det(eI, eJ, eK)
                # Symmetrize
                for perm in [(I,J,K),(I,K,J),(J,I,K),(J,K,I),(K,I,J),(K,J,I)]:
                    d[perm] = val
    return d

def _trilinear_det(A, B, C):
    """Polarization of det to symmetric trilinear form."""
    ABC = A + B + C
    AB = A + B
    AC = A + C
    BC = B + C
    return (det_h3o(ABC) - det_h3o(AB) - det_h3o(AC) - det_h3o(BC)
            + det_h3o(A) + det_h3o(B) + det_h3o(C)) / 6.0
```

### Algorithm 5: Equivariance Verification -- Group Actions

| Algorithm | Problem | Convergence | Cost per Step | Memory | Key Reference |
|-----------|---------|-------------|---------------|--------|---------------|
| Explicit matrix construction + conjugation check | Verify G-equivariance of pi_u | Exact | O(n^3) per group element | O(n^2) | Standard representation theory |

**Spin(9) on V_0 = h_2(O):** Already available. The 10 T_b operators generate the Spin(9) action on V_{1/2}, and the induced action on V_0 is via:

```
g . Y = Pi_0( sum_IJ g_IJ T_{b_I}(T_{b_J}(Y_half)) )  -- NOT correct

Actually: Spin(9) acts on h_2(O) = V_0 directly as the spin factor automorphism group.
The action on the 10-dim space is the VECTOR representation of SO(9).
```

The existing T_b matrices encode the Spin(9) action on V_{1/2} via Clifford generators. The action on V_0 is the 10-dim representation: 9 (vector) + 1 (trace). The trace (beta+gamma)/2 is invariant; the 9 traceless directions transform as the SO(9) vector.

**SL(2,C_u) on h_2(C_u):** For the standard choice u = e_7, SL(2,C) acts on h_2(C) by X -> gXg*. Represent g as a 2x2 complex matrix, convert to a 4x4 real matrix acting on (beta, gamma, Re(x1), Im_u(x1)). This is the defining representation of SO_0(3,1).

**Stabilizer computation:** The stabilizer of u in Spin(9) is the subgroup that preserves the splitting O = C_u + C_u^perp. For u = e_7, this is generated by Clifford elements that commute with left-e_7-multiplication. Use the existing gamma matrices to find which grade-2 Clifford elements stabilize u.

**Implementation approach:** Use the existing `compute_commutator_algebra()` infrastructure. Compute [gamma_a, gamma_b] for all pairs and filter those that commute with J_u (the left-e_7 multiplication operator). The stabilizer Lie algebra is spin(7) (dim 21) inside spin(9) (dim 36).

### Algorithm 6: 5d -> 4d KK Reduction Bookkeeping

| Algorithm | Problem | Convergence | Cost per Step | Memory | Key Reference |
|-----------|---------|-------------|---------------|--------|---------------|
| Field content decomposition | Track how 5d fields decompose under KK reduction | Exact (algebraic counting) | Negligible | Negligible | de Wit-Van Proeyen (1992); GST (1984) |

**Method:** This is primarily a bookkeeping exercise, not a numerical computation. The 5d N=2 MESGT has:
- Graviton (5d metric g_{mu nu}): 5 d.o.f. -> 4d metric (2) + graviphoton (2) + dilaton (1)
- 27 vector fields A^I_mu: 27 x 3 d.o.f. -> 27 4d vectors (27x2) + 27 scalars (27x1)
- 26 scalars phi^x: 26 d.o.f. -> 26 4d scalars

Total 4d bosonic content: 1 metric + 28 vectors + 53 scalars (on coset E_{7(-25)}/(E_6 x U(1)) after dualization).

**Implementation:** A Python dict tracking field multiplicities and representations. No heavy numerics needed.

```python
def kk_field_content_5d_to_4d():
    """Return the 5d -> 4d KK reduction field content.
    
    5d N=2 MESGT with n_V = 26 vector multiplets (exceptional magic case).
    """
    return {
        '5d_graviton': {'5d_dof': 5, '4d_metric': 1, '4d_graviphoton': 1, '4d_dilaton': 1},
        '5d_vectors': {'count': 27, '4d_vectors': 27, '4d_scalars_from_vectors': 27},
        '5d_scalars': {'count': 26, '4d_scalars': 26},
        '4d_total': {
            'metric': 1,
            'vectors': 28,  # 27 + 1 graviphoton
            'scalars': 53,  # 26 + 27 from vectors
            'scalar_manifold': 'E7(-25)/(E6 x U(1))',
            'scalar_manifold_dim_real': 54,  # dim_R(E7(-25)) - dim_R(E6 x U(1))
        }
    }
```

---

## Software Ecosystem

### Primary Tools

| Tool | Version | Purpose | License | Maturity |
|------|---------|---------|---------|----------|
| Python | 3.14.2 | Runtime | PSF | Stable |
| NumPy | 2.4.2 | Matrix operations, linear algebra, 27x27 tensor computations | BSD | Stable |
| SymPy | 1.14.0 | Symbolic verification of det formula, F_4 invariance check | BSD | Stable |

### Supporting Tools

| Tool | Version | Purpose | When Needed |
|------|---------|---------|-------------|
| SageMath | >=10.x | Branching rules Spin(9)->Spin(7), exceptional Jordan algebra cross-checks | Optional: for verifying stabilizer computations and representation decompositions |
| Matplotlib | >=3.8 | Visualization of scalar manifold geometry | Plotting only |

**No new dependencies required.** All core computations use existing NumPy + SymPy. SageMath is listed as optional because it has a built-in exceptional Jordan algebra implementation (h_3(O) as self-adjoint 3x3 octonionic matrices, with determinant and F_4 automorphism group) that could serve as an independent cross-check, but it is not needed for the computation pipeline.

### SageMath Exceptional Jordan Algebra (Optional Cross-Check)

SageMath's `sage.algebras.jordan_algebra` module implements the exceptional 27-dimensional Jordan algebra as self-adjoint 3x3 matrices over an octonion algebra. The module provides:
- Basis computation and Jordan multiplication
- Derivation algebra computation (returns F_4)
- Operations over commutative rings with characteristic not 2

This could independently verify our `det_h3o()` and `_trilinear_det()` implementations. However, SageMath operates symbolically (slow) while our NumPy pipeline operates numerically (fast). Use SageMath for spot-checking, not bulk computation.

---

## Data Flow

```
Existing infrastructure (code/octonion_algebra.py)
  - H3O class, Octonion class, Jordan product, Peirce projections
  - V0_basis_elements() (10 basis vectors of h_2(O))
  - Vhalf_basis_vectors() (16 basis vectors of V_{1/2})
  - T_b matrices, Clifford generators, J_u

Phase 1: pi_u projection
  -> Implement proj_u: O -> C_u (single octonion projection)
  -> Implement pi_u: h_2(O) -> h_2(C_u) (apply proj_u to x1 entry)
  -> Verify: det on h_2(C_u) = Minkowski metric on R^{3,1}
  -> Compute kernel of pi_u: 6-dim subspace of h_2(O)
  -> Verify: det on h_2(O) splits as det_4 + quadratic_on_kernel

Phase 2: det(X) and d_IJK
  -> Implement det_h3o: h_3(O) -> R (cubic form)
  -> Validate: det(E_11) = 0, det(I) = 1, det(lambda*X) = lambda^3 det(X)
  -> Implement trilinear polarization _trilinear_det
  -> Compute full d_IJK tensor (27^3 entries, symmetric => 27*28*29/6 = 3654 independent)
  -> Decompose d_IJK into Peirce blocks: (V_1, V_{1/2}, V_0) indexing
  -> Identify nonzero blocks and their physical meaning

Phase 3: Equivariance
  -> Compute stabilizer of u in Spin(9): intersect spin(9) with commutant of J_u
  -> Verify stabilizer contains SL(2,C_u) acting on h_2(C_u)
  -> Decompose 10 of Spin(9) under stabilizer: expect 4 + 6

Phase 4: KK reduction
  -> Bookkeeping: 5d -> 4d field content
  -> Verify scalar manifold dimension matches E_{7(-25)}/(E_6 x U(1))
  -> Identify 4d Einstein equations from reduced Lagrangian
```

## Computation Order and Dependencies

| Step | Depends On | Produces | Can Parallelize? |
|------|-----------|----------|-----------------|
| 1. Implement det_h3o() | H3O class (Phase 28) | det: h_3(O) -> R | N/A (entry point) |
| 2. Validate det_h3o() | Step 1 | Boolean pass/fail + known values | Sequential after Step 1 |
| 3. Implement proj_u, pi_u | Octonion class (Phase 28) | pi_u: h_2(O) -> h_2(C_u) | Parallel with Steps 1-2 |
| 4. Verify det on h_2(C_u) = Minkowski | Steps 1, 3 | Metric signature check | Sequential after 1,3 |
| 5. Compute d_IJK tensor | Step 1 | 27x27x27 symmetric tensor | Sequential after Step 2 |
| 6. Decompose d_IJK into Peirce blocks | Step 5, Peirce projections (Phase 28) | Block structure of d_IJK | Sequential after Step 5 |
| 7. Compute stabilizer of u in Spin(9) | Clifford generators (Phase 29), J_u (Phase 28) | Lie algebra of stabilizer | Parallel with Steps 1-6 |
| 8. Verify Lorentz subgroup in stabilizer | Steps 3, 7 | SL(2,C) embedding check | Sequential after 3,7 |
| 9. KK reduction field count | Steps 5, 6 | 4d field content table | Sequential after Step 6 |

---

## Resource Estimates

| Computation | Time (estimate) | Memory | Storage | Hardware |
|-------------|-----------------|--------|---------|----------|
| det_h3o for single X | < 0.01 ms | < 1 KB | negligible | Any CPU |
| Full d_IJK tensor (3654 independent entries) | < 1 second | ~160 KB (27^3 doubles) | negligible | Any CPU |
| Peirce block decomposition of d_IJK | < 10 ms | ~160 KB | negligible | Any CPU |
| Stabilizer Lie algebra computation | < 100 ms | < 10 KB | negligible | Any CPU |
| Full pipeline (all phases) | < 5 seconds | < 5 MB | negligible | Any CPU |

All computations are trivially small. The bottleneck is algebraic understanding, not computational resources.

---

## Integration with Existing Code

### Input Formats
- `H3O` class from `octonion_algebra.py`: stores (alpha, beta, gamma, x1, x2, x3) with `to_vector()` / `from_vector()` for R^27 <-> H3O conversion
- `V0_basis_elements()`: returns 10 H3O elements spanning V_0 = h_2(O)
- `Vhalf_basis_vectors()`: returns 16 H3O elements spanning V_{1/2}
- `peirce_V0(X)`, `peirce_Vhalf(X)`, `peirce_V1(X)`: projection operators
- `compute_T_b_matrices()`: 10 real 16x16 matrices (Spin(9) generators on V_{1/2})
- `rescale_to_clifford_generators(T_matrices)`: 9 Cl(9,0) generators with {gamma_i, gamma_j} = 2*delta*I
- `krasnov_J_u_matrix()`: 16x16 matrix for left-e_7-multiplication on V_{1/2}

### Output Formats
- `det_h3o(X)`: float (the cubic determinant)
- `det_h2o(Y)`: float (the quadratic determinant on V_0)
- `pi_u(Y, u_index)`: H3O element in h_2(C_u) (alpha=x2=x3=0, beta,gamma preserved, x1 projected)
- `compute_dIJK()`: (27, 27, 27) numpy array
- `dIJK_peirce_blocks()`: dict mapping block labels to sub-tensors

### Interface Points

**Entry point:** `code/octonion_algebra.py` -- all new functions added to this file, extending the existing module.

**New functions needed:**
- `det_h3o(X)` -- cubic determinant on h_3(O)
- `det_h2o(Y)` -- quadratic determinant on h_2(O) = V_0
- `proj_u(x, u_index)` -- project octonion to C_u
- `proj_u_general(x, u_vec)` -- project octonion to C_u for general u
- `pi_u(Y, u_index)` -- project h_2(O) to h_2(C_u)
- `minkowski_metric_h2c(Y1, Y2, u_index)` -- inner product on h_2(C_u) induced by det
- `compute_dIJK(basis_27)` -- full 27x27x27 cubic form tensor
- `_trilinear_det(A, B, C)` -- polarized trilinear form of det
- `dIJK_peirce_blocks(d_tensor)` -- decompose d_IJK into Peirce block structure
- `stabilizer_u_in_spin9(gammas, J_u)` -- find Lie algebra of stabilizer of u in Spin(9)
- `verify_lorentz_in_stabilizer(stab_basis, pi_u_matrix)` -- check SL(2,C) embedding

**Existing functions reusable without modification:**
- All Octonion arithmetic (multiplication, conjugation, norm)
- H3O class (storage, arithmetic, to_vector/from_vector)
- jordan_product(A, B)
- All Peirce projections (peirce_V0, peirce_Vhalf, peirce_V1)
- V0_basis_elements(), Vhalf_basis_vectors()
- compute_T_b_matrices(), rescale_to_clifford_generators()
- krasnov_J_u_matrix(), compute_commutator_algebra()

### H3O.from_vector Basis Convention

The `H3O.from_vector(v)` maps R^27 -> h_3(O) as:
- v[0] = alpha (V_1 coordinate)
- v[1] = beta, v[2] = gamma, v[3:11] = x1 components (V_0 coordinates, indices 1-10)
- v[11:19] = x2 components, v[19:27] = x3 components (V_{1/2} coordinates, indices 11-26)

For d_IJK decomposition, the index ranges are:
- I = 0: V_1 block
- I = 1..10: V_0 block (beta, gamma, x1[0..7])
- I = 11..26: V_{1/2} block (x2[0..7], x3[0..7])

This means the Peirce block (V_1, V_{1/2}, V_{1/2}) of d_IJK corresponds to d[0, 11:27, 11:27].

---

## Open Questions

| Question | Why Open | Impact on Project | Approaches Being Tried |
|----------|---------|-------------------|----------------------|
| Does Re(x1*(x2*x3)) = Re((x1*x2)*x3) for all octonions x1,x2,x3? | Alternative expressions: by Artin's theorem this holds when any two of x1,x2,x3 are equal, but the general case follows from the trace form Re(abc) being alternating on Im(O). Must verify this identity numerically. | If this fails, det_h3o must use a specific parenthesization consistently. | Numerical verification for 1000 random triples + appeal to Moufang identity |
| Is the stabilizer of u in Spin(9) exactly Spin(7), or Spin(7) x something? | The isotropy group of a unit vector in S^8 under Spin(9) is Spin(8), but u is in S^6 subset Im(O), not S^8. The isotropy in G_2 subset Spin(7) of u in S^6 is SU(3). Need to track how this lifts to Spin(9). | Determines the structure group on the 6d kernel of pi_u and whether it matches SU(3) for gauge symmetry. | Explicit computation using Clifford algebra commutant |
| What is the precise relationship between d_{half,half,0} and the fermion bilinear -> spacetime vector coupling? | The Peirce product V_{1/2} x V_{1/2} -> V_0 maps spinor bilinears to h_2(O). After pi_u projection, does this give the standard Dirac current j^mu = psi_bar gamma^mu psi? | If yes, the GST cubic coupling directly encodes SM matter-gravity interaction. | Explicit computation of d_IJK for V_{1/2} x V_{1/2} x V_0 block |

## Anti-Approaches

| Anti-Approach | Why Avoid | What to Do Instead |
|---------------|-----------|-------------------|
| Using SymPy symbolic computation for the full d_IJK tensor | 27^3 = 19683 symbolic evaluations each requiring symbolic octonion multiplication. Painfully slow (hours). | Use NumPy floats throughout; verify specific entries symbolically if needed |
| Implementing h_2(O) as a separate class | h_2(O) = V_0 of h_3(O), already stored as H3O with alpha=x2=x3=0. A separate class would duplicate logic and create interface friction. | Use existing H3O class with peirce_V0 projection; add det_h2o as a standalone function |
| Building explicit 27x27 matrices for the E_6 action | E_6 is 78-dimensional; constructing all generators as 27x27 matrices is a large computation not needed for this milestone. | Work with the F_4 subgroup (which preserves det) and the Spin(9) subgroup (which we already have via Clifford generators) |
| Attempting to implement the full GST Lagrangian numerically | The Lagrangian involves spacetime derivatives, gauge covariant derivatives, and Chern-Simons forms -- these are field-theoretic objects, not finite-dimensional matrices. | Focus on the algebraic/group-theoretic content: d_IJK tensor, field content decomposition, representation matching. The Lagrangian is a formula to be VERIFIED algebraically, not simulated numerically. |
| Using general-purpose symmetric space computation packages | The specific coset E_{6(-26)}/F_4 has dimension 26 and is well-characterized analytically. Generic algorithms add overhead without insight. | Use the explicit Jordan algebra structure: the 26-dim tangent space is the traceless part of h_3(O), with metric from the Jordan trace form |

---

## Logical Dependencies

```
Octonion arithmetic + H3O class (Phase 28, existing)
  -> det_h3o (new: cubic polynomial on 27 coordinates)
    -> _trilinear_det (new: polarization)
      -> compute_dIJK (new: full 27x27x27 tensor)
        -> dIJK_peirce_blocks (new: block decomposition)
          -> Physical interpretation: which C_IJK encode which SM couplings

Peirce projections (Phase 28, existing)
  -> pi_u = proj_u composed with peirce_V0 (new: linear map)
    -> det on h_2(C_u) = Minkowski metric (new: verification)
    -> 10 = 4 + 6 splitting under pi_u (new: kernel computation)

Clifford generators gamma_i (Phase 29, existing)
  -> spin(9) Lie algebra = span{[gamma_i, gamma_j]} (existing from Phase 30)
  -> stabilizer of u = {M in spin(9) : [M, J_u] = 0} (new: commutant)
    -> verify Lorentz subgroup in stabilizer (new: representation check)
    -> verify SU(3) structure group on kernel (new: branching rule)

det_h3o validated + pi_u constructed + stabilizer computed
  -> GST Lagrangian algebraic content verified
    -> KK reduction field counting
      -> 4d field content matches SM + GR expectation
```

---

## Recommended Investigation Scope

Prioritize:
1. **det_h3o + validation** -- the cubic determinant is the foundation of everything else. Validate against det(E_{11}) = 0, det(I) = 1, the F_4-invariance property det(g.X) = det(X) for g in Aut(h_3(O)), and consistency with the existing Jordan product: det(X) = (1/3)Tr(X . (X . X)) - (1/6)(Tr X)^3 + (1/2)(Tr X)(Tr(X.X)) - (1/3)Tr(X.(X.X)).
2. **pi_u and Minkowski metric** -- the projection must produce the correct (1,3) signature on h_2(C_u). This is the "gravity lives here" claim.
3. **d_IJK Peirce block decomposition** -- this tells us which cubic couplings in the GST Lagrangian correspond to which SM interactions.

Defer:
- **Full KK reduction Lagrangian:** The 5d -> 4d reduction is a standard calculation (de Wit-Van Proeyen 1992) that does not require new computational infrastructure. It should be done analytically with numerical spot-checks, not as a full numerical computation.
- **E_{7(-25)} scalar manifold geometry:** Only needed if Phases 1-2 succeed and Phase 3 proceeds. The 54-dimensional quaternionic manifold is well-characterized in the literature.

---

## Validation Strategy

| Result | Validation Method | Benchmark | Source |
|--------|------------------|-----------|--------|
| det(E_{11}) = 0 | Direct computation | Exact zero | Rank-1 idempotent has det = 0 |
| det(I_{3x3}) = 1 | Direct computation | Exact 1.0 | Identity matrix det = 1 |
| det(lambda*X) = lambda^3 * det(X) | 50 random X, 10 random lambda | Rel error < 1e-14 | Cubic homogeneity |
| det is F_4-invariant: det(g.X) = det(X) | Apply Jordan automorphisms and check | Rel error < 1e-12 | F_4 = Aut(h_3(O)) preserves det |
| det from trace formula: det = (1/3)Tr(X^3) - (1/2)Tr(X)Tr(X^2) + (1/6)(Tr X)^3 | Compare two formulas for 100 random X | Diff < 1e-12 | Cayley-Hamilton for rank-3 Jordan algebras |
| det on h_2(C_u) has signature (1,3) | Compute metric matrix g_{ab} = d^2(det)/dY_a dY_b for h_2(C_u) basis | Eigenvalues: one positive, three negative | h_2(C) = R^{3,1} is classical |
| pi_u is a Jordan algebra homomorphism for h_2 | pi_u(A.B) = pi_u(A).pi_u(B) for A,B in h_2(O)? | This should FAIL in general (pi_u is NOT a homomorphism) | Expectation from non-associativity |
| d_IJK is fully symmetric | Check d[I,J,K] = d[sigma(I,J,K)] for all permutations | Exact within machine precision | Definition of polarized form |
| d_IJK with all V_0 indices vanishes | d[1:11, 1:11, 1:11] = 0 | Exact zero | V_0 = h_2(O) is rank-2; cubic invariant of rank-2 algebra is zero |
| Stabilizer dimension | Count independent generators | dim = 21 (if Spin(7)) or 28 (if Spin(7) x U(1)) | Representation theory |
| 10 = 4 + 6 under stabilizer | Decompose V_0 restricted to stabilizer | Two irreducible pieces of dim 4 and 6 | Branching rule |

---

## Sources

- Baez, J.C., "The Octonions," Bull. AMS 39 (2002) 145-205, [math/0105155](https://arxiv.org/abs/math/0105155) -- h_3(O) structure, det formula, F_4 automorphism group
- Gunaydin, M., Sierra, G., and Townsend, P.K., [Phys. Lett. B 133 (1983) 72](https://www.sciencedirect.com/science/article/abs/pii/0370269383901089) -- original magic supergravity paper, cubic prepotential from det(X)
- Gunaydin, M., Sierra, G., and Townsend, P.K., Nucl. Phys. B 242 (1984) 244 -- detailed GST Lagrangian and field content
- de Wit, B. and Van Proeyen, A., "Special geometry, cubic polynomials and homogeneous quaternionic spaces," [hep-th/9112027](https://arxiv.org/abs/hep-th/9112027) -- classification of very special real manifolds, c-map, r-map
- Faraut, J. and Koranyi, A., *Analysis on Symmetric Cones* (1994) -- Jordan algebra determinant formulas, symmetric cones, trace forms
- Springer, T.A., "Characterization of a class of cubic forms," Indag. Math. 24 (1962) 259 -- uniqueness of cubic invariant on h_3(O)
- Farnsworth, S., "The n-point Exceptional Universe," [arXiv:2503.10744](https://arxiv.org/abs/2503.10744) -- exceptional spectral geometry from Jordan algebras, F_4 x F_4 gauge theory
- Todorov, I. and Drenska, S., "Octonions, Exceptional Jordan Algebra and the role of the group F_4 in particle physics," [arXiv:1805.06739](https://arxiv.org/abs/1805.06739) -- SM from F_4, decomposition under subgroups
- Boyle, L., "The Standard Model, The Exceptional Jordan Algebra, and Triality," [arXiv:2006.16265](https://arxiv.org/abs/2006.16265) -- Peirce decomposition, Spin(10) upgrade, triality
- [SageMath Jordan algebra documentation](https://doc.sagemath.org/html/en/reference/algebras/sage/algebras/jordan_algebra.html) -- optional cross-check tool for exceptional Jordan algebra computations
- [SageMath branching rules](https://doc.sagemath.org/html/en/thematic_tutorials/lie/branching_rules.html) -- optional tool for representation decomposition verification
- Parisi, M. and Marrani, A., "The role of Spin(9) in Octonionic Geometry," [Preprints 2018](https://www.preprints.org/manuscript/201809.0430/v1/download) -- Spin(9) representation theory on octonionic spaces
- Okubo, S., "The exceptional Jordan eigenvalue problem," [arXiv:math-ph/9910004](https://arxiv.org/pdf/math-ph/9910004) -- eigenvalue computation for h_3(O), computational aspects
