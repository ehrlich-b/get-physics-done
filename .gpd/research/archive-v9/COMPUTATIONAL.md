# Computational Approaches: v13.0 Paper 6 Closure Extensions

**Surveyed:** 2026-04-12
**Domain:** Exceptional Jordan algebra / KKT conformal algebra / Very special real geometry / E_{6(-26)} invariants
**Confidence:** HIGH (all algorithms are exact algebraic operations on finite-dimensional spaces <= 27; existing codebase covers ~70% of what's needed)

## Recommended Stack

Extend `code/octonion_algebra.py` with five computational blocks, each building on existing infrastructure:

1. **OD1-OD4 verification** -- Uses existing `jordan_product()`, `V0_basis_elements()`, `peirce_V0()`, `compute_T_b_matrices()`. New: systematic faithfulness check (10x10 matrix rank), Peirce multiplication table verification against McCrimmon axioms.

2. **KKT structure constants for h_2(C_u)** -- Uses existing `h2cu_basis()` (4 elements), `jordan_product_h2o()`. New: 15 generators of KKT(h_2(C_u)) as explicit matrices, commutation relation verification against so(4,2).

3. **Observer independence via second idempotent** -- Uses existing Peirce projection functions, `jordan_product()`. New: E_{22} idempotent, second Peirce decomposition, isomorphism map between decompositions.

4. **Very special real metric a_{IJ}** -- Uses existing `det_3()`, `peirce_basis_27()`, `peirce_coords()`, `d_ijk_tensor()`. New: constrained Hessian computation on det=1 hypersurface, positive definiteness check.

5. **E_{6(-26)}-invariant two-derivative enumeration** -- Uses existing `d_ijk_tensor()`, `_compute_sharp()`, Spin(9) generators. New: E_{6(-26)} generator construction, invariant tensor classification, derivative term enumeration.

No new Python dependencies needed. NumPy for numerics, SymPy only if exact rational verification is desired (optional). All matrices are at most 27x27, all computations complete in seconds on a laptop.

---

## Numerical Algorithms

### Algorithm 1: OD1-OD4 Verification (Faithful V_0 Action + Peirce Multiplication)

| Algorithm | Problem | Convergence | Cost per Step | Memory | Key Reference |
|-----------|---------|-------------|---------------|--------|---------------|
| Matrix rank of T_b representation | OD1: V_0 acts faithfully on V_{1/2} | Exact (SVD) | O(16^2 * 10) = O(2560) | 10 matrices 16x16 | McCrimmon 2004 Ch. 17 |
| Peirce product table comparison | OD2-OD4: multiplication rules | Exact (polynomial) | O(10^2 * 27) = O(2700) | 10x10 table of 27-vectors | Alfsen-Shultz 2001 Ch. 8 |

**What exists:** `compute_T_b_matrices()` returns 10 matrices (16x16) representing V_0 action on V_{1/2}. `V0_basis_elements()` provides the V_0 basis. `jordan_product()` and `jordan_product_h2o()` compute products.

**What's new:**

OD1 (Faithful action): Verify that the map b -> T_b from V_0 to End(V_{1/2}) is injective. Stack the 10 flattened 16x16 matrices as columns of a 256x10 matrix; check rank = 10.

```python
def verify_OD1_faithful_action():
    """OD1: V_0 acts faithfully on V_{1/2} via Peirce operators T_b.
    
    Faithfulness means ker(b -> T_b) = {0}, equivalently rank = 10.
    
    Uses: compute_T_b_matrices() [existing], V0_basis_elements() [existing]
    Returns: dict with rank, singular values, is_faithful bool
    """
    T_mats = compute_T_b_matrices()  # 10 matrices, 16x16
    T_flat = np.array([T.flatten() for T in T_mats]).T  # 256 x 10
    rank = np.linalg.matrix_rank(T_flat, tol=1e-10)
    sv = np.linalg.svd(T_flat, compute_uv=False)
    return {
        'rank': rank,
        'is_faithful': rank == 10,
        'singular_values': sv,
        'sv_min': sv[min(9, len(sv)-1)],
        'sv_gap': sv[9] if len(sv) > 9 else sv[-1],
    }
```

OD2-OD3 (Peirce multiplication verification): Verify the three Peirce multiplication rules hold with exact zero error:
- V_1 . V_0 = 0
- V_{1/2} . V_{1/2} subset V_1 + V_0  (no V_{1/2} component)
- V_0 . V_0 subset V_0

These are already partially verified in Phase 46-01 Task 2 (V_0 closure), Phase 46-02 Task 2 (V_{1/2} x V_{1/2} Peirce rule), and Phase 47-01 Task 2 (d_{IJK} forbidden blocks = 0). The new function consolidates all checks.

```python
def verify_OD2_OD3_peirce_rules():
    """OD2-OD3: Systematic Peirce multiplication rule verification.
    
    Checks all sector pairs (V_1,V_0), (V_1,V_{1/2}), (V_0,V_0),
    (V_{1/2},V_{1/2}), (V_{1/2},V_0) and verifies landing sectors.
    
    Uses: jordan_product() [existing], peirce_V0/V1/Vhalf [existing],
          peirce_basis_27() [existing]
    """
    basis = peirce_basis_27()  # 27 elements
    # For each pair, compute jordan_product and check Peirce projections
    # V_1 . V_0 = 0: basis[0] . basis[17..26] -> check norm = 0
    # etc.
    # Returns: dict with max_error per rule, all_passed bool
```

OD4 (Associativity of Peirce product on V_0): The intrinsic Jordan product on V_0 = h_2(O) satisfies the Jordan identity (a . b) . a^2 = a . (b . a^2). Already verified in Phase 46-01 Task 2 (intrinsic vs inherited agreement). New: explicit Jordan identity check on random V_0 elements.

```python
def verify_OD4_jordan_identity_V0(n_random=20, seed=42):
    """OD4: Jordan identity on V_0.
    
    (a . b) . a^2 = a . (b . a^2) for random a, b in V_0.
    
    Uses: jordan_product_h2o() [existing], V0_basis_elements() [existing]
    """
    rng = np.random.default_rng(seed)
    # Generate random V_0 elements as linear combos of basis
    # Check Jordan identity with machine-precision tolerance
    # Returns: dict with max_error, n_tests, all_passed bool
```

**Convergence criterion:** All errors < 1e-14 (float64 machine precision).

**Operation count:** OD1: 1 SVD of 256x10 matrix. OD2-OD3: 27*27 = 729 Jordan products (each ~50 octonion multiplications). OD4: 20 random tests, 4 Jordan products each. Total: < 0.5 seconds.


### Algorithm 2: KKT Structure Constants for h_2(C_u) and so(4,2) Isomorphism

| Algorithm | Problem | Convergence | Cost per Step | Memory | Key Reference |
|-----------|---------|-------------|---------------|--------|---------------|
| TKK Lie algebra construction | KKT(h_2(C_u)) generators | Exact (structure constants) | O(4^3) = O(64) per bracket | 15 matrices, each 10x10 | Tits 1962, Koecher 1967, McCrimmon 2004 |
| Killing form eigenvalue check | so(4,2) isomorphism | Exact (eigenvalues) | O(15^3) = O(3375) | 15x15 Killing form | Conformal algebra: Fradkin-Palchik 1998 |

**What exists:** `h2cu_basis()` returns 4 basis elements of h_2(C_u). `jordan_product_h2o()` computes the Jordan product. `det_2()` provides the quadratic form.

**What's new:** The Kantor-Koecher-Tits (TKK/KKT) construction builds a Lie algebra from a Jordan algebra J:

```
KKT(J) = J^- + Der(J) + J^+
```

where J^+ and J^- are two copies of J (translations and special conformal), and Der(J) is the derivation algebra. For J = h_2(C) (= R^{3,1} as Jordan algebra with det_2):
- dim(J) = 4
- Der(h_2(C)) = so(3,1), dim = 6 (derivations of 2x2 Hermitian complex matrices)
- A dilatation generator, dim = 1
- Total: 4 + 6 + 1 + 4 = 15 = dim(so(4,2))

The 15 generators decompose as: 4 translations P_mu, 4 special conformal K_mu, 6 Lorentz M_munu, 1 dilatation D.

**Implementation strategy:** Represent the TKK algebra on J + R + J (dimension 4+1+4 = 9) or equivalently on the 10-dimensional V_0 (which already contains h_2(C_u) as a 4-dim subspace). Use the existing V_0 coordinate system.

Step 1: Construct derivation algebra of h_2(C_u). A derivation D satisfies D(a . b) = D(a) . b + a . D(b). For h_2(C_u), this is so(3,1) acting on the 4-dim space. Build the 6 derivation generators as 4x4 matrices satisfying the Leibniz rule on the Jordan product.

Step 2: Construct translation and special conformal generators. For a in J, the translation T_a acts as T_a(x) = a (constant map). The special conformal transformation S_a acts as S_a(x) = {x, a, x} (quadratic map via the triple product). In the linearized (Lie algebra) formulation on J + R + J, these become:

```python
def build_kkt_generators_h2cu():
    """Build 15 generators of KKT(h_2(C_u)) = so(4,2).
    
    Representation on 10-dim space: [x in J, lambda in R, y in J]
    where J = h_2(C_u), dim(J) = 4.
    Representation dimension: 4 + 1 + 4 + 1(extra for conformal weight) = 10.
    
    Actually: use 6x6 matrix representation.
    Embed h_2(C_u) = R^{3,1} in R^{4,2} via conformal embedding.
    The so(4,2) generators are then 6x6 antisymmetric matrices 
    (with respect to eta_{4,2} = diag(+,+,+,+,-,-) or (+,-,-,-,+,-)).
    
    Uses: h2cu_basis() [existing], det_2() [existing for metric]
    Returns: dict with 15 generators (6x6 or 10x10), 
             commutation relations, Killing form, isomorphism proof
    """
    # Step 1: Get Minkowski metric on h_2(C_u) from det_2
    basis = h2cu_basis()  # 4 elements
    eta = np.zeros((4, 4))
    for i in range(4):
        for j in range(4):
            # Polarization of det_2
            ApB = basis[i] + basis[j]  # need to handle H3O addition in V_0
            eta[i, j] = 0.5 * (det_2(ApB) - det_2(basis[i]) - det_2(basis[j]))
    # eta should be diag(+1/4, -1/4, -1, -1) in unnormalized basis
    # Normalize to get eta = diag(+1, -1, -1, -1)
    
    # Step 2: Build so(4,2) generators in 6x6 representation
    # Metric: eta_42 = diag(+1,-1,-1,-1,+1,-1) on R^{4,2}
    # 15 generators M_{AB} for A < B in {0,1,2,3,4,5}
    # (M_{AB})^C_D = eta_{AC} delta_{BD} - eta_{BC} delta_{AD}
    
    # Step 3: Identify P_mu, K_mu, M_munu, D in conformal decomposition
    # P_mu = M_{mu,4} + M_{mu,5}  (4 translations)
    # K_mu = M_{mu,4} - M_{mu,5}  (4 special conformal)
    # M_munu = M_{mu,nu}          (6 Lorentz)
    # D = M_{45}                  (1 dilatation)
    
    # Step 4: Verify commutation relations match so(4,2)
    # [M_{AB}, M_{CD}] = eta_{BC} M_{AD} - eta_{AC} M_{BD} 
    #                   + eta_{AD} M_{BC} - eta_{BD} M_{AC}
```

Step 3: Verify the Killing form. For so(4,2), the Killing form has signature (6, 9) (6 positive from the compact so(4) x so(2) subalgebra, 9 negative from the noncompact directions). Alternatively: Killing(M_AB, M_CD) = 8 * (eta_AC eta_BD - eta_AD eta_BC).

Step 4: Verify commutation relations. All 15*14/2 = 105 brackets must match so(4,2) structure constants exactly.

**Convergence criterion:** All structure constants exact to 1e-14. Killing form eigenvalue spectrum matches so(4,2) prediction.

**Operation count:** 15^2 = 225 matrix commutators (each 6x6). Killing form: 15x15 matrix (225 traces). Total: < 0.1 seconds.

**Connection to existing code:** The 6 Lorentz generators can be cross-checked against the so(3) x so(6) stabilizer from `compute_v0_stabilizer()`. The so(3) factor (3 generators) should match 3 of the 6 Lorentz generators (the rotation subgroup M_{12}, M_{13}, M_{23}). The 3 boost generators M_{0i} will be NEW -- they do not appear in the compact Spin(9) stabilizer because boosts are noncompact. This is the key v13.0 result: the KKT construction PRODUCES the missing boosts that Spin(9) could not provide.


### Algorithm 3: Second Idempotent and Observer Independence

| Algorithm | Problem | Convergence | Cost per Step | Memory | Key Reference |
|-----------|---------|-------------|---------------|--------|---------------|
| Peirce decomposition under E_{22} | Second observer's Peirce sectors | Exact (eigenvalue) | O(27^2) = O(729) products | 27x27 + 3 projection matrices | McCrimmon 2004 Ch. 17 |
| Isomorphism construction | Map between decompositions | Exact (linear) | O(27^2) = O(729) | 27x27 change-of-basis | Alfsen-Shultz 2001 |

**What exists:** Full Peirce decomposition under E_{11}: `peirce_V1()`, `peirce_Vhalf()`, `peirce_V0()`, `L_E11()`, `L_E11_matrix_on_Vhalf()`, all 27-dim basis functions.

**What's new:** Construct the Peirce decomposition under E_{22} = diag(0,1,0) and verify it produces isomorphic structure.

E_{22} is a rank-1 idempotent (E_{22}^2 = E_{22}, Tr(E_{22}) = 1). Its Peirce decomposition gives:
- V_1(E_{22}) = R * E_{22}: the 1-dim eigenspace with eigenvalue 1
- V_{1/2}(E_{22}): the 16-dim eigenspace with eigenvalue 1/2 -- spanned by the (1,2) and (2,3) off-diagonal octonionic entries (x3 and x1)
- V_0(E_{22}): the 10-dim eigenspace with eigenvalue 0 -- the h_2(O) complementary to the (2,2) position, consisting of (alpha, gamma, x2)

```python
def peirce_decomposition_E22():
    """Peirce decomposition of h_3(O) under E_{22} = diag(0,1,0).
    
    L_{E_{22}}(X) = E_{22} . X has eigenvalues 0, 1/2, 1.
    
    V_1(E_{22}) = R * E_{22}
    V_{1/2}(E_{22}) = {X : alpha=0, beta=0, gamma=0, x2=0}
                     = span{x1 components, x3 components} = O^2
    V_0(E_{22}) = {X : beta=0, x1=0, x3=0}
                 = h_2(O) in (alpha, gamma, x2) coordinates
    
    Uses: jordan_product() [existing], H3O [existing]
    Returns: dict with projection functions, basis elements, 
             L_{E22} matrix on 27-dim space
    """
    E22 = H3O(beta=1.0)  # diag(0,1,0)
    
    # Verify idempotent
    E22_sq = jordan_product(E22, E22)
    # E22_sq should equal E22
    
    # Build L_{E22} matrix on full 27-dim basis
    basis = peirce_basis_27()
    L_mat = np.zeros((27, 27))
    for j in range(27):
        prod = jordan_product(E22, basis[j])
        coords = peirce_coords(prod, basis)
        L_mat[:, j] = coords
    
    # Eigenvalues should be {0 (x10), 1/2 (x16), 1 (x1)}
    evals = np.linalg.eigvalsh(L_mat)
    
    # Projection functions for the new decomposition
    def peirce_V1_E22(X):
        return H3O(beta=X.beta)
    
    def peirce_Vhalf_E22(X):
        return H3O(x1=Octonion(X.x1.c.copy()), 
                   x3=Octonion(X.x3.c.copy()))
    
    def peirce_V0_E22(X):
        return H3O(alpha=X.alpha, gamma=X.gamma, 
                   x2=Octonion(X.x2.c.copy()))
```

Step 2: Build the isomorphism between the two Peirce decompositions. There exists an F_4 automorphism sigma that maps E_{11} -> E_{22}. Under this automorphism:
- V_1(E_{11}) -> V_1(E_{22})
- V_{1/2}(E_{11}) -> V_{1/2}(E_{22})  
- V_0(E_{11}) -> V_0(E_{22})

The automorphism sigma is conjugation by the permutation matrix that swaps rows/columns 1 and 2 in the 3x3 representation. On h_3(O) coordinates:

```python
def permute_12(X):
    """F_4 automorphism swapping positions 1 and 2 in h_3(O).
    
    Swaps E_{11} <-> E_{22}, mapping:
      alpha <-> beta
      x1 -> conj(x3), x2 -> conj(x2), x3 -> conj(x1)
    
    This is the existing _permute_h3o with perm=(1,0,2).
    Uses: _permute_h3o() [existing]
    """
    return _permute_h3o(X, (1, 0, 2))
```

Step 3: Verify that after permutation, all structures match:
- det_3 is preserved: det_3(sigma(X)) = det_3(X)
- d_{IJK} tensor is preserved (in permuted basis)
- V_0 projection pi_u in the new decomposition gives the same Minkowski metric
- T_b operators on the new V_{1/2} give isomorphic Clifford algebra

```python
def verify_observer_independence(n_random=20, seed=42):
    """Verify E_{11} and E_{22} Peirce decompositions are F_4-isomorphic.
    
    Checks:
    1. sigma(E_{11}) = E_{22} and sigma(E_{22}) = E_{11}
    2. det_3 preserved: det_3(sigma(X)) = det_3(X) for random X
    3. V_0 structures isomorphic (det_2 metric same signature)
    4. V_{1/2} Clifford structures isomorphic (same Cl(9,0))
    5. pi_u in new decomposition gives same Minkowski structure
    
    Uses: _permute_h3o() [existing], det_3() [existing], 
          det_2() [existing], verify_f4_invariance_det3() [existing]
    Returns: dict with all verification results
    """
```

**Convergence criterion:** All errors < 1e-14. det_3 preservation exact.

**Operation count:** 27x27 = 729 Jordan products for L_{E22} matrix. 20 random det_3 checks. Permutation map: O(1) per element. Total: < 1 second.

**Why this matters for v13.0:** Observer independence (any rank-1 idempotent gives the same physics) strengthens the claim that V_0 = spacetime is not an artifact of choosing E_{11}. All three diagonal idempotents E_{11}, E_{22}, E_{33} should give isomorphic Peirce decompositions with isomorphic spacetime. This is guaranteed by the S_3 subgroup of F_4 acting on h_3(O) by permuting diagonal positions.


### Algorithm 4: Very Special Real Metric a_{IJ}

| Algorithm | Problem | Convergence | Cost per Step | Memory | Key Reference |
|-----------|---------|-------------|---------------|--------|---------------|
| Constrained Hessian of log det | a_{IJ} on det=1 surface | Exact (closed form) | O(27^3) = O(20000) d_IJK lookups | 27x27 matrix | GST 1984, de Wit-Van Proeyen 1992 |
| Eigenvalue check | Positive definiteness | Exact | O(27^3) eigenvalue | 27x27 matrix | Cecotti-Ferrara-Girardello 1989 |

**What exists:** `det_3()`, `d_ijk_tensor()` (106 nonzero entries), `peirce_basis_27()`, `peirce_coords()`, `prepotential_F()`.

**What's new:** The very special real (VSR) metric on the scalar manifold of 5d N=2 MESGT is:

```
a_{IJ} = -(1/2) * (d_I d_J log N(h))|_{N(h)=1}
```

where N(h) = (1/6) d_{IJK} h^I h^J h^K is the cubic norm and d_I = d/dh^I. On the constraint surface N(h) = 1, this reduces to:

```
a_{IJ} = -(1/2) * [ (d_{IJK} h^K) / N - (3/2) * (d_{IKL} h^K h^L)(d_{JMN} h^M h^N) / N^2 ]
```

evaluated at N = 1. With d(X,X,X) = 6*N(X), using our convention d_{IJK} h^I h^J h^K = 6*det_3(X), we have N(h) = det_3(X). Then:

```python
def vsr_metric_aIJ(h_coords, d_tensor=None):
    """Compute the very special real metric a_{IJ}.
    
    a_{IJ} = -(1/2) d_I d_J log(N)|_{N=1}
    
    where N = det_3 expressed in Peirce coordinates,
    d_{IJK} is the totally symmetric tensor from d_ijk_tensor().
    
    The formula on N=1:
      a_{IJ} = -(1/2) * [N_{IJ}/N - (3/2)(N_I N_J)/N^2]
    where N_I = d_{IJK} h^J h^K, N_{IJ} = d_{IJK} h^K.
    
    Parameters:
        h_coords: np.ndarray shape (27,), coordinates with det_3 = 1
        d_tensor: dict from d_ijk_tensor() (default: computed)
    
    Uses: d_ijk_tensor() [existing]
    Returns: dict with a_IJ (27x27), eigenvalues, signature, 
             is_positive_definite, restricted metrics on Peirce sectors
    """
    if d_tensor is None:
        d_tensor = d_ijk_tensor()
    
    # Step 1: Compute N_I = sum_{JK} d_{IJK} h^J h^K for each I
    N_I = np.zeros(27)
    for I in range(27):
        for (A, B, C), val in d_tensor.items():
            # d is stored with A<=B<=C; sum over all permutations
            indices = [A, B, C]
            for perm in _unique_perms(indices):
                if perm[0] == I:
                    N_I[I] += val * h_coords[perm[1]] * h_coords[perm[2]]
    
    # Step 2: Compute N_{IJ} = sum_K d_{IJK} h^K for each (I,J)
    N_IJ = np.zeros((27, 27))
    for (A, B, C), val in d_tensor.items():
        for perm in _unique_perms([A, B, C]):
            N_IJ[perm[0], perm[1]] += val * h_coords[perm[2]]
    
    # Step 3: Compute N = det_3(X) for normalization
    N = 0.0
    for (A, B, C), val in d_tensor.items():
        mult = _multiplicity(A, B, C)
        N += mult * val * h_coords[A] * h_coords[B] * h_coords[C]
    N /= 6.0  # d(X,X,X) = 6*det_3
    
    # Step 4: a_{IJ} = -(1/2) * [N_{IJ}/N - (3/2)(N_I N_J)/N^2]
    a = np.zeros((27, 27))
    for I in range(27):
        for J in range(27):
            a[I, J] = -0.5 * (N_IJ[I, J] / N 
                              - 1.5 * N_I[I] * N_I[J] / N**2)
    
    # Step 5: Check positive definiteness
    # CRITICAL: a_{IJ} is 27x27 but the physical metric lives on the
    # 26-dim submanifold N=1 (remove one direction). The normal to
    # N=1 is n_I = N_I/|N_I|. Project out this direction:
    # a_perp = a - (a.n)(n.a) / (n.a.n)
    
    evals = np.linalg.eigvalsh(a)
    evals_sorted = np.sort(evals)
    
    return {
        'a_IJ': a,
        'eigenvalues': evals_sorted,
        'n_positive': int(np.sum(evals > 1e-10)),
        'n_negative': int(np.sum(evals < -1e-10)),
        'n_zero': int(np.sum(np.abs(evals) <= 1e-10)),
        'is_positive_definite_full': bool(np.all(evals > -1e-10)),
        'N_I': N_I,
        'N_IJ': N_IJ,
        'N_value': N,
    }
```

**Evaluation point:** Use h = peirce_coords(I_3) where I_3 = diag(1,1,1) is the identity (det_3(I_3) = 1). This is the maximally symmetric point on the N=1 surface.

**Alternative evaluation:** Use h = peirce_coords(E_{11} + E_{22} + E_{33}) which is the same as I_3. Can also check at a generic point on N=1 by scaling any X with det_3(X) > 0 to det_3 = 1 via h -> h / det_3(h)^{1/3}.

**Expected result:** The 27x27 metric a_{IJ} has rank 26 (one null direction along the N=1 normal). The projected metric on the 26-dim tangent space should have signature (26, 0) -- positive definite -- because the scalar manifold of the octonionic magic MESGT is E_{6(-26)} / F_4, which is a COMPACT symmetric space of RANK 2, dimension 26. Positive definiteness of a_{IJ} on the constraint surface is equivalent to stating that the 5d kinetic terms for the 26 vector multiplet scalars are positive (no ghosts).

**Cross-check:** At the identity point I_3, the F_4 symmetry forces a_{IJ} to be proportional to the Peirce Gram matrix (since F_4 acts transitively on the N=1 surface near I_3). This means a_{IJ} should be diagonal in the Peirce basis with entries proportional to 1/G_{II} where G_{II} = Tr(e_I . e_I).

**Convergence criterion:** Rank of a_{IJ} = 26 exactly. All 26 nonzero eigenvalues positive. Null eigenvector proportional to N_I.

**Operation count:** d_tensor has 106 entries. N_I: 27 * 106 * 6 permutations ~ 17000 operations. N_IJ: 27^2 * 106 ~ 77000 operations. Total: < 0.5 seconds.


### Algorithm 5: E_{6(-26)}-Invariant Two-Derivative Terms

| Algorithm | Problem | Convergence | Cost per Step | Memory | Key Reference |
|-----------|---------|-------------|---------------|--------|---------------|
| E_6 generator construction | 78 generators of e_{6(-26)} on R^{27} | Exact (Lie bracket) | O(27^2 * 78) per closure | 78 matrices 27x27 | Yokota 2009, Barton-Sudbery 2003 |
| Invariant tensor enumeration | E_6-invariant symmetric tensors | Exact (kernel computation) | O(78 * 27^4) | Tensor spaces | GST 1984, Cecotti et al. 1989 |

**What exists:** `verify_f4_invariance_det3()` builds F_4 generators (52-dim) acting on h_3(O). `compute_spin9_v0_rep()` builds Spin(9) generators. `_g2_derivation_matrix()` builds G_2 derivations.

**What's new:** E_{6(-26)} is the structure group of the cubic form det_3 on h_3(O). It has dimension 78 = 52 (F_4) + 26 (coset). The 26 coset generators are the "boosts" that do NOT preserve the identity I_3 but DO preserve det_3. The coset is E_{6(-26)}/F_4 = OP^2 (octonionic projective plane), dimension 26.

E_{6(-26)} = Aut(det_3), the determinant-preserving linear transformations on h_3(O). An infinitesimal generator D satisfies:

```
d/dt det_3(e^{tD} X)|_{t=0} = 0  for all X
```

which linearizes to:

```
d_3(DX, X, X) = 0  for all X
```

where d_3 is the polarized trilinear form.

**Step 1:** Build F_4 generators (already available in `verify_f4_invariance_det3()`). These are 52 matrices acting on R^{27}.

**Step 2:** Build the 26 coset generators. These are traceless endomorphisms of h_3(O) preserving det_3 but NOT preserving the Jordan product. Concretely, for each a in h_3(O) with Tr(a) = 0, the map:

```
D_a(X) = a . X - (1/3) Tr(a . X) * I
```

is a generator of E_{6(-26)} if a is in the 26-dim traceless subspace. Verify: d_3(D_a X, X, X) = 0.

**Step 3:** Check closure. The 78 generators should close under Lie bracket.

**Step 4:** Enumerate E_{6(-26)}-invariant two-derivative terms. A two-derivative term in a 5d Lagrangian has the form:

```
L_2 = g_{IJ}(h) * (d_mu h^I)(d^mu h^J)
```

where g_{IJ}(h) is a metric on the scalar manifold. E_{6(-26)} invariance requires g_{IJ}(h) to be invariant under the E_{6(-26)} action on h^I. Since E_{6(-26)} acts transitively on N=1 with stabilizer F_4, the only E_{6(-26)}-invariant metric on N=1 is the coset metric (up to scale). This coset metric IS the VSR metric a_{IJ}.

For the gauge kinetic terms, the two-derivative term is:

```
L_gauge = a_{IJ}(h) * F^I_{mu nu} * F^{J mu nu}
```

where a_{IJ} is again the VSR metric. E_{6(-26)} invariance uniquely determines the gauge kinetic matrix to be a_{IJ} (up to scale).

```python
def enumerate_e6_invariant_terms():
    """Enumerate and verify E_{6(-26)}-invariant two-derivative terms.
    
    Result: exactly TWO independent E_{6(-26)}-invariant two-derivative 
    structures exist:
    1. a_{IJ} dh^I dh^J  (scalar kinetic)
    2. a_{IJ} F^I F^J    (gauge kinetic)
    Both use the SAME metric a_{IJ} from Algorithm 4.
    
    Proof strategy: 
    - E_{6(-26)} acts on the 27 with one invariant: det_3 (cubic)
    - Two-index invariant tensors: only the metric on the orbit space
    - By Schur's lemma applied to the IRREDUCIBLE 27 of E_6: the only
      E_6-invariant symmetric 2-tensor on the 27 is the one derived 
      from det_3 (since 27 is irreducible, Sym^2(27) contains exactly 
      one singlet under E_6, which is the metric induced by det_3).
    
    Verification: For each E_6 generator D_alpha (78 total), check:
      D_alpha^I_K a_{IJ} + D_alpha^J_K a_{IK} = 0
    (Lie derivative of a_{IJ} under the E_6 action vanishes)
    
    Uses: verify_f4_invariance_det3() [existing for F_4 part],
          vsr_metric_aIJ() [new, Algorithm 4]
    Returns: dict with n_invariant_2tensors, verification errors,
             scalar_kinetic_unique (bool), gauge_kinetic_unique (bool)
    """
```

**The key uniqueness result:** The decomposition Sym^2(27) under E_6 is:

```
Sym^2(27) = 27 + 351
```

where 27 appears exactly ONCE. The invariant (singlet) under E_{6(-26)} in Sym^2(27) does NOT appear directly, but on the N=1 constraint surface, the induced metric from the cubic form provides the unique E_6-invariant metric. This is because E_6 acts transitively on N=1 with isotropy F_4, so E_6-invariant metrics on N=1 correspond to F_4-invariant metrics on T_{p}(N=1), and F_4 acts irreducibly on the 26-dim tangent space, giving a UNIQUE invariant metric by Schur's lemma.

**Convergence criterion:** All 78 Lie derivative checks zero to 1e-14.

**Operation count:** 78 generators x 27^2 entries x 27 contractions ~ 1.5M multiplications. Total: < 5 seconds.


---

## Software Ecosystem

### Primary Tools

| Tool | Version | Purpose | License | Maturity |
|------|---------|---------|---------|----------|
| Python | 3.14.2 | Core language | PSF | stable |
| NumPy | 2.4.2 | Float64 matrix operations | BSD | stable |

### Supporting Tools

| Tool | Version | Purpose | When Needed |
|------|---------|---------|-------------|
| SymPy | latest | Exact rational verification of structure constants | Optional cross-check for KKT commutation relations |
| SageMath | 10.x | Lie algebra classification, branching rules | Optional cross-check for E_6 representation theory |

No additional installations needed. The existing environment already has NumPy.


## Data Flow

```
Existing v12.0 infrastructure
  |
  +--> OD1-OD4 verification (Algorithm 1)
  |     Input: T_b matrices (existing), basis functions (existing)
  |     Output: faithfulness proof, Peirce rule verification
  |
  +--> KKT(h_2(C_u)) construction (Algorithm 2)
  |     Input: h2cu_basis() (existing), det_2() (existing), 
  |            compute_v0_stabilizer() (existing for Lorentz cross-check)
  |     Output: 15 generators, so(4,2) isomorphism proof, commutation table
  |
  +--> Second idempotent (Algorithm 3)
  |     Input: jordan_product() (existing), _permute_h3o() (existing)
  |     Output: E_{22} Peirce decomposition, isomorphism verification
  |
  +--> VSR metric a_{IJ} (Algorithm 4)
  |     Input: d_ijk_tensor() (existing, 106 entries), det_3() (existing)
  |     Output: 27x27 metric, positive definiteness on N=1, eigenvalues
  |
  +--> E_{6(-26)} invariants (Algorithm 5)
        Input: F_4 generators (existing), a_{IJ} (from Alg 4),
               d_ijk_tensor() (existing)
        Output: 78 E_6 generators, uniqueness proof for 2-derivative terms
```


## Computation Order and Dependencies

| Step | Depends On | Produces | Can Parallelize? |
|------|-----------|----------|-----------------|
| Algorithm 1 (OD1-OD4) | v12.0 code only | Faithfulness + Peirce rules | Yes (independent) |
| Algorithm 2 (KKT) | v12.0 code only | so(4,2) generators + isomorphism | Yes (independent) |
| Algorithm 3 (2nd idempotent) | v12.0 code only | Observer independence proof | Yes (independent) |
| Algorithm 4 (VSR metric) | v12.0 code (d_ijk_tensor) | a_{IJ}, positive definiteness | Yes (independent) |
| Algorithm 5 (E_6 invariants) | Algorithm 4 (a_{IJ}) | Uniqueness of 2-derivative Lagrangian | After Algorithm 4 |

Algorithms 1-4 are fully independent and can execute in parallel. Algorithm 5 depends on Algorithm 4's a_{IJ} output for the invariance verification.


## Resource Estimates

| Computation | Time (estimate) | Memory | Storage | Hardware |
|-------------|-----------------|--------|---------|----------|
| Algorithm 1 (OD1-OD4) | < 1 sec | < 10 MB | negligible | CPU (laptop) |
| Algorithm 2 (KKT) | < 1 sec | < 10 MB | negligible | CPU (laptop) |
| Algorithm 3 (2nd idempotent) | < 2 sec | < 10 MB | negligible | CPU (laptop) |
| Algorithm 4 (VSR metric) | < 1 sec | < 10 MB | negligible | CPU (laptop) |
| Algorithm 5 (E_6 invariants) | < 10 sec | < 50 MB | negligible | CPU (laptop) |
| **Total** | **< 15 sec** | **< 50 MB** | **negligible** | **Single-core laptop** |


## Integration with Existing Code

All new functions extend `code/octonion_algebra.py`. No new files needed.

### Existing Functions Used by Each Algorithm

**Algorithm 1 (OD1-OD4):**
- `compute_T_b_matrices()` -- returns 10 matrices, 16x16 (Phase 28)
- `V0_basis_elements()` -- returns 10 H3O elements (Phase 28)
- `jordan_product()` -- h_3(O) Jordan product (Phase 28)
- `jordan_product_h2o()` -- intrinsic V_0 product (Phase 46)
- `peirce_V0()`, `peirce_Vhalf()`, `peirce_V1()` -- projections (Phase 28)
- `peirce_basis_27()` -- full 27-element basis (Phase 47)

**Algorithm 2 (KKT):**
- `h2cu_basis()` -- 4 basis elements of h_2(C_u) (Phase 46)
- `det_2()` -- Minkowski quadratic form (Phase 46)
- `jordan_product_h2o()` -- for derivation construction (Phase 46)
- `compute_v0_stabilizer()` -- for so(3) cross-check (Phase 48)

**Algorithm 3 (2nd idempotent):**
- `jordan_product()` -- (Phase 28)
- `_permute_h3o()` -- S_3 permutation automorphisms (Phase 47)
- `det_3()` -- for invariance check (Phase 47)
- `peirce_coords()` -- coordinate extraction (Phase 49)

**Algorithm 4 (VSR metric):**
- `d_ijk_tensor()` -- 106 nonzero entries of d_{IJK} (Phase 47)
- `det_3()` -- cubic norm (Phase 47)
- `peirce_basis_27()` -- basis (Phase 47)
- `peirce_coords()` -- coordinate extraction (Phase 49)

**Algorithm 5 (E_6 invariants):**
- `verify_f4_invariance_det3()` -- F_4 generators on R^27 (Phase 47)
- `d_ijk_tensor()` -- for invariance verification (Phase 47)
- `_g2_derivation_matrix()` -- G_2 derivations (Phase 47)
- Algorithm 4 output: a_{IJ} metric

### Interface Points

- **Input format:** All functions take H3O objects or numpy arrays (same as existing code)
- **Output format:** All return dicts with numpy arrays and scalar diagnostics (same as existing code)
- **Naming convention:** Follow existing `verify_*()` and `compute_*()` pattern
- **Error reporting:** Return max_error fields in dict for automated checking


## Open Questions

| Question | Why Open | Impact on Project | Approaches Being Tried |
|----------|---------|-------------------|----------------------|
| Does the KKT construction for h_2(C_u) produce boosts as well as rotations? | Boosts are noncompact, h_2(C_u) is a rank-2 Jordan algebra | Critical: if KKT only gives the compact part, need alternative argument for full Lorentz | KKT by construction gives all conformal generators including boosts; verify numerically |
| Is a_{IJ} positive definite at generic points on N=1, not just at I_3? | Positive definiteness could break at boundary of moduli space | Medium: affects physical interpretation of scalar kinetic terms | Check at multiple points; F_4 transitivity on N=1 guarantees uniformity near I_3 |
| Which real form of E_6 appears? | E_6 has 5 real forms; need E_{6(-26)} specifically | Critical: wrong real form gives wrong signature | Check Killing form signature: E_{6(-26)} has maximal compact F_4, so Killing signature is (52, 26) |


## Anti-Approaches

| Anti-Approach | Why Avoid | What to Do Instead |
|---------------|-----------|-------------------|
| Building E_6 generators from scratch via root system | Overcomplicated, error-prone for exceptional groups | Use the known embedding E_6 superset F_4, build coset generators from Jordan algebra operations |
| Numerical optimization for N=1 constraint | Not needed, analytical formula exists | Use closed-form a_{IJ} from d_{IJK} contraction |
| Generic Lie algebra software (GAP, LiE) for commutation relations | Overkill for 15-dim so(4,2) | Direct 6x6 matrix construction, verify commutators explicitly |
| Computing E_6 invariants via character theory | Abstract, doesn't connect to the physical metric | Use infinitesimal invariance (Lie derivative = 0) directly |
| SymPy for all computations | Too slow for 27x27 symbolic matrices | Use NumPy float64 with SymPy only for exact verification of critical structure constants |


## Logical Dependencies

```
det_3 (existing, Phase 47) -> d_{IJK} tensor (existing, Phase 47)
                                |
                                +--> a_{IJ} VSR metric (Algorithm 4)
                                |     |
                                |     +--> E_6 invariant verification (Algorithm 5)
                                |
                                +--> Peirce block structure (existing, Phase 47)
                                      |
                                      +--> OD1-OD4 verification (Algorithm 1)

h2cu_basis (existing, Phase 46) -> KKT construction (Algorithm 2)
                                    |
                                    +--> so(4,2) isomorphism (Algorithm 2)

jordan_product (existing, Phase 28) -> E_{22} decomposition (Algorithm 3)
                                       |
                                       +--> Observer independence (Algorithm 3)

compute_v0_stabilizer (existing, Phase 48) --> Cross-check for Algorithm 2
                                               (so(3) in stabilizer = rotation 
                                                subgroup of so(3,1) in KKT)
```


## Recommended Investigation Scope

Prioritize:
1. **Algorithm 2 (KKT -> so(4,2)):** This is the most novel result. If KKT(h_2(C_u)) = so(4,2), it proves the conformal spacetime symmetry algebraically, providing OD5-OD7 plus boosts. This directly addresses gap G4 (V_0 = spacetime).
2. **Algorithm 4 (VSR metric):** Computing a_{IJ} and proving positive definiteness establishes the kinetic term structure. Combined with E_6 invariance (Algorithm 5), this proves the Lagrangian is uniquely determined, addressing the N=2 SUSY gap.
3. **Algorithm 1 (OD1-OD4):** Systematic consolidation of Peirce structure verification. Many pieces already verified in Phases 46-47; this assembles them into a single coherent check.

Defer:
- Algorithm 3 (observer independence): Important for completeness but follows trivially from F_4 symmetry already established in Phase 47. Can be executed after the core results.
- Algorithm 5 (E_6 invariants): Depends on Algorithm 4. Can run after Algorithm 4 but before paper assembly.


## Validation Strategy

| Result | Validation Method | Benchmark | Source |
|--------|------------------|-----------|--------|
| OD1 faithfulness | Rank of T_b map = 10 | Exact integer | McCrimmon 2004 |
| KKT(h_2(C_u)) = so(4,2) | Killing form signature (6,9) | Exact | Conformal algebra theory |
| KKT commutation | [M_AB, M_CD] structure constants | Exact match to so(4,2) | Standard Lie theory |
| so(3) embedding | KKT rotations match v12.0 stabilizer | < 1e-14 | Phase 48 cross-check |
| E_{22} idempotent | E_{22}^2 = E_{22}, Tr = 1 | Exact | Jordan algebra axiom |
| Observer independence | det_3(sigma(X)) = det_3(X) | < 1e-14 | F_4 invariance (Phase 47) |
| a_{IJ} rank | rank = 26 on R^{27}, 26 positive eigenvalues | Exact integer | GST 1984 |
| a_{IJ} at I_3 | Proportional to Peirce Gram inverse | < 1e-12 | F_4 isotropy argument |
| a_{IJ} positive definite | All 26 nonzero eigenvalues > 0 | > 1e-10 | de Wit-Van Proeyen 1992 |
| E_6 invariance of a_{IJ} | Lie derivative = 0 for all 78 generators | < 1e-14 | Schur's lemma |
| 2-derivative uniqueness | Exactly 1 singlet in Sym^2(27)|_{N=1} | Exact integer | E_6 representation theory |


## Key References

- **GST 1984:** Gunaydin, Sierra, Townsend, "The geometry of N=2 Maxwell-Einstein supergravity and Jordan algebras," Nucl. Phys. B 242 (1984) 244-268. Primary reference for magic MESGT, Jordan algebra structure.
- **de Wit, Van Proeyen 1992:** "Special geometry, cubic polynomials and homogeneous quaternionic spaces," Commun. Math. Phys. 149 (1992) 307-333 (hep-th/9112027). VSR geometry, a_{IJ} metric, dimensional reduction chain.
- **Tits 1962:** "Une classe d'algebres de Lie en relation avec les algebres de Jordan," Indag. Math. 24 (1962) 530-535. KKT construction.
- **McCrimmon 2004:** "A Taste of Jordan Algebras," Springer. Peirce decomposition, multiplication rules, derivation algebra.
- **Alfsen-Shultz 2001:** "State Spaces of Operator Algebras," Springer. Jordan algebra structure theory.
- **Yokota 2009:** "Exceptional Lie Groups," arXiv:0902.0431. E_6 generators, real forms.
- **Barton-Sudbery 2003:** "Magic squares and matrix models of Lie algebras," Adv. Math. 180 (2003) 596-647 (math/0203010). F_4 and E_6 from 3x3 matrices.
- **Baez 2002:** "The Octonions," Bull. AMS 39 (2002) 145-205 (math/0105155). h_2(K) = R^{dim(K)+1,1}, KKT for Jordan algebras.
- **Springer 1962:** "Characterization of a class of cubic forms," Indag. Math. 24 (1962) 259-265. Uniqueness of det_3.
- **Weinberg 1964:** Phys. Rev. 135 (1964) B1049. Low-energy uniqueness of spin-2 theory.


## Sources

- GST 1984 (Nucl. Phys. B 242, 244) -- prepotential structure, field content, C_{IJK}
- de Wit, Van Proeyen 1992 (hep-th/9112027) -- VSR metric definition and properties
- McCrimmon 2004 (Springer) -- Peirce rules, Jordan identity, derivation algebra
- Baez 2002 (math/0105155) -- KKT construction, h_2(K) spacetime structure
- Phase 46-50 verification headers in `code/octonion_algebra.py` -- existing benchmarks
