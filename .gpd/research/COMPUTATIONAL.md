# Computational Methods: H_eff from h_3(O) Peirce Structure and SSB Verification

**Physics Domain:** Exceptional Jordan algebras / Lattice models with F_4 symmetry / Nonlinear sigma models on F_4/Spin(9)
**Researched:** 2026-03-30
**Confidence:** MEDIUM (novel territory -- no existing lattice F_4 codes; algebraic part HIGH)

### Scope Boundary

COMPUTATIONAL.md covers computational TOOLS, libraries, algorithms, and infrastructure for: (1) constructing H_eff from the Jordan product on h_3(O), (2) numerical verification of SSB on small lattices with 27-dimensional on-site Hilbert space, (3) computing the spin stiffness analog for F_4/Spin(9) sigma models, (4) constructing the NL sigma model Lagrangian on F_4/Spin(9). It does NOT cover physics derivations (METHODS.md) or the research landscape (PRIOR-WORK.md).

**Relationship to existing codebase:** The project has:
- `code/octonion_algebra.py`: Full octonion arithmetic, h_3(O) Jordan product, Peirce projections under E_{11}, all 10 V_0 Peirce operators T_b as 16x16 matrices, Clifford algebra Cl(9,0) generators, Krasnov J_u matrix, associative closure verification (M_16(R)). This is the ALGEBRAIC FOUNDATION.
- `code/ed_entanglement.py`: Sparse Hamiltonian construction for spin-1/2 chains/lattices, Lanczos ground state solver (scipy eigsh), partial trace, von Neumann entropy.
- `code/fisher_metric.py`: QFIM via eigendecomposition, Bures metric.
- `code/correlation_2d.py`: 2D Heisenberg AFM on 4x4 lattice, correlation functions.
- `peirce_coupling.py` / `peirce_coupling_v2.py`: Jordan product coupling hierarchy for all four division algebras.

The new milestone extends the algebraic infrastructure to build a lattice Hamiltonian and study its ground-state properties.

---

## Dimensions and Hilbert Space Analysis

### On-site Hilbert space: h_3(O)^sa

The self-adjoint part of h_3(O) (the exceptional Jordan algebra, also called the Albert algebra) is a 27-dimensional REAL vector space. The Peirce decomposition under E_{11} gives:

| Subspace | Description | Real dimension |
|----------|-------------|----------------|
| V_1 | span{E_{11}} | 1 |
| V_{1/2} | x_2, x_3 in O (off-diagonal to E_{11}) | 16 |
| V_0 | h_2(O) (lower-right 2x2 block) | 10 |
| **Total** | **h_3(O)** | **27** |

For a lattice model with N sites, each site carries a 27-dimensional on-site space. The full Hilbert space dimension for a CLASSICAL lattice model (no quantum superposition) is 27^N. For a QUANTUM lattice model where the on-site algebra is promoted to a quantum Hilbert space, the situation depends on the representation chosen.

### Key dimension: 27 is large but manageable for small lattices

| N sites | Classical dim (27^N) | Quantum dim (if d=27) | Feasibility |
|---------|---------------------|-----------------------|-------------|
| 1 | 27 | 27 | Trivial |
| 2 | 729 | 729 | Trivial |
| 3 | 19,683 | 19,683 | Easy ED |
| 4 | 531,441 | 531,441 | Tight ED (dense ~2 GB) |
| 5 | 14,348,907 | 14,348,907 | Infeasible for dense ED |
| 6 | ~3.9 x 10^8 | ~3.9 x 10^8 | Infeasible |

**Verdict:** ED is feasible up to N=4 sites (531k dim) on a local workstation with ~32 GB RAM. With sparse matrices and Lanczos, N=4 is comfortable; N=5 requires aggressive symmetry reduction.

### Comparison with v9.0 lattice sizes

The v9.0 work used spin-1/2 models (d=2 per site). A 4x4 2D lattice with d=2 gives 2^16 = 65,536 -- comfortably within ED. For d=27, the analog is:

- **2-site chain:** 27^2 = 729. Trivial.
- **3-site chain:** 27^3 = 19,683. Straightforward Lanczos.
- **4-site chain:** 27^4 = 531,441. Sparse Lanczos with ~4-8 GB, feasible.
- **2x2 plaquette:** 27^4 = 531,441. Same as 4-site chain.
- **2x3 rectangle:** 27^6 ~ 3.9 x 10^8. Infeasible without symmetry reduction.

**Recommendation:** Use 2-4 site chains and the 2x2 plaquette for ED. The 2x2 plaquette is the minimal 2D system for detecting SSB signatures. This parallels the v9.0 approach (4x4 for spin-1/2 = 16 sites, d=2) but scaled to the larger on-site dimension.

---

## Open Questions

| Question | Why Open | Impact on Project | Approaches Being Tried |
|----------|---------|-------------------|----------------------|
| What is the correct quantum Hilbert space for an h_3(O) lattice site? | Jordan algebras are not associative; standard tensor product construction requires a C*-envelope or alternative formulation | Determines the Hamiltonian construction method | Use the associative envelope M_16(R) acting on V_{1/2}, or treat the 27-dim space as a classical target manifold |
| Does SSB survive finite-size effects on a 2x2 lattice? | SSB is a thermodynamic limit phenomenon; small lattices only show precursors | Limits what can be "verified" numerically | Look for order parameter scaling, not true SSB; use finite-size scaling analysis |
| Is the Jordan product H_eff gapped or gapless? | No prior lattice simulation of Jordan algebra Hamiltonians exists | Determines whether Hastings-Koma applies for correlation decay | Compute spectrum for small systems, look for gap scaling |

## Anti-Approaches

| Anti-Approach | Why Avoid | What to Do Instead |
|---------------|-----------|-------------------|
| Treat 27-dim h_3(O) as a quantum d=27 spin | The Jordan algebra is not a spin representation; imposing SU(27) symmetry is wrong | Construct H from the Jordan product structure, preserving F_4 symmetry |
| Full ED on N > 4 sites | 27^5 ~ 14M is beyond dense diagonalization; 27^6 ~ 387M is beyond Lanczos | Use 2-4 site ED for spectra; use classical Monte Carlo on larger lattices for the NL sigma model |
| DMRG for F_4 lattice | Large on-site d=27 makes each MPS tensor 27 x chi x chi; bond dim chi~100 already costs 27 x 100^2 = 270k per tensor; no F_4-symmetric DMRG code exists | ED for small systems; classical MC for sigma model on larger lattices |
| Importing heavy external packages (QuTiP, ITensor) | The Jordan product structure is non-standard; no existing package handles h_3(O) natively; the existing codebase is self-contained Python/NumPy | Extend `code/octonion_algebra.py` with lattice infrastructure; use SciPy sparse for ED |

---

## Recommended Computational Stack

### Task 1: H_eff from Jordan Product

**Algorithm:** Direct algebraic construction using existing T_b operators.

The effective Hamiltonian on a lattice acts on tensor products of on-site spaces. There are two formulations:

**Formulation A: V_{1/2} representation (RECOMMENDED)**

Each site carries V_{1/2} = R^16 (the Peirce half-space). The nearest-neighbor interaction is built from the Jordan product structure:

```
H_eff = J * sum_{<i,j>} sum_{a in V_0_basis} T_a^(i) T_a^(j)
```

where T_a^(i) is the Peirce operator T_a acting on site i. This is a bilinear coupling mediated by the V_0 basis elements. The on-site dimension is 16, giving:

| N sites | Hilbert dim (16^N) | Feasibility |
|---------|-------------------|-------------|
| 2 | 256 | Trivial |
| 3 | 4,096 | Easy |
| 4 | 65,536 | Standard ED (same as v9.0 2D 4x4 spin-1/2) |
| 5 | 1,048,576 | Lanczos feasible |
| 6 | 16,777,216 | Tight Lanczos (~134 MB per vector, need ~5-10 vectors) |

This is MUCH more tractable than the 27-dim formulation because dim(V_{1/2}) = 16, not 27.

**Formulation B: Full h_3(O) representation**

Each site carries the full 27-dim h_3(O). The interaction is the Jordan product itself:

```
H = J * sum_{<i,j>} (a_i o a_j)_{projected}
```

This is more natural but computationally more expensive. Use only for 2-3 site systems.

**Implementation plan:** Extend `code/octonion_algebra.py`:

1. Use the existing 10 T_b matrices (16x16 real) as building blocks.
2. Construct the 2-site Hamiltonian H_2 = sum_a (T_a tensor T_a) as a 256x256 sparse matrix.
3. Verify: H_2 must commute with the diagonal action of Spin(9) on V_{1/2}^{tensor 2}.
4. Extend to N-site chain: standard nearest-neighbor construction.
5. Compute ground state via `scipy.sparse.linalg.eigsh` (Lanczos).

**Cost estimate for Formulation A:**
- 2 sites: 256x256 matrix, < 1 second on any machine.
- 4 sites: 65,536 x 65,536 sparse matrix. The Hamiltonian has ~10 nonzero terms per bond, each a Kronecker product of 16x16 matrices. Lanczos with scipy eigsh: ~10-30 seconds for ground state.
- 6 sites: 16M x 16M sparse. Lanczos feasible but slow: ~10-60 minutes for ground state, ~1 GB RAM for vectors.

**The 10 T_b operators and their Clifford structure:**

From v8.0 Phase 28-02:
- T_{b_1} = (1/4)*I_16 (trace element, trivially couples)
- T_{b_2}: diagonal, eigenvalues {-1/4, +1/4} (diagonal V_0)
- T_{b_3} through T_{b_10}: off-diagonal, eigenvalues {-1/2, +1/2} (octonionic V_0)
- Traceless T_b satisfy Clifford anticommutation: {T_a, T_b} = (1/2) delta_{ab} I_16
- All T_b are SYMMETRIC (real eigenvalues)

The Hamiltonian H = sum_a T_a^(i) T_a^(j) has F_4-derived structure because the T_b span the V_0 subspace of the Peirce decomposition, which inherits F_4 symmetry from h_3(O).

### Task 2: SSB Verification

**Method:** Finite-size analysis of order parameter and level crossings.

True SSB cannot occur on finite lattices (no symmetry breaking in a finite Hilbert space with compact symmetry group). What CAN be detected:

1. **Tower of states (Anderson tower):** In the low-energy spectrum, the system develops a "tower" of quasi-degenerate states that collapses to the ground state as N -> infinity. The spacing scales as 1/N (for magnons in a Heisenberg AFM) or more generally as 1/V (volume). Detect this by computing the low-lying spectrum for N=2,3,4 and checking the gap scaling.

2. **Order parameter:** Define a staggered order parameter (analog of m_s for Neel order) adapted to the F_4/Spin(9) coset. The coset F_4/Spin(9) = OP^2 (octonionic projective plane) is 16-dimensional. The order parameter lives in the tangent space of OP^2 at the "ordered" point.

3. **Correlation function:** Compute the 2-point correlator of the order parameter field. If SSB occurs, the correlator has a non-decaying component (long-range order).

**Feasible lattice sizes for SSB detection:**

| Method | Max sites (d=16) | Max sites (d=27) | What it detects |
|--------|-----------------|-----------------|-----------------|
| Full spectrum (dense) | 4 | 3 | Anderson tower, all level crossings |
| Low-energy spectrum (Lanczos) | 6 | 4 | Gap scaling, lowest ~20 states |
| Ground state only (Lanczos) | 7-8 | 5 | Order parameter, correlations |

**Implementation:** Extend `code/ed_entanglement.py` with a new constructor `construct_jordan_hamiltonian(N, bc='obc')` that builds the Hamiltonian from T_b Kronecker products. The existing Lanczos infrastructure (eigsh wrapper) applies directly.

### Task 3: Spin Stiffness (rho_s analog)

**Method:** Twisted boundary conditions.

The spin stiffness (helicity modulus) rho_s measures the energy cost of imposing a twist in the order parameter across the system. For a lattice Hamiltonian with continuous symmetry G broken to H:

```
rho_s = (1/V) * d^2 E_0 / d phi^2 |_{phi=0}
```

where phi is a twist angle in the G/H coset space imposed via boundary conditions.

For the F_4/Spin(9) model:
- G = F_4 (automorphism group of h_3(O))
- H = Spin(9) (stabilizer of E_{11})
- Coset = OP^2, dim = 52 - 36 = 16
- The twist is an element of the Lie algebra of F_4 modulo the Lie algebra of Spin(9)

**Implementation:**

1. Construct the twisted Hamiltonian H(phi) by modifying the bond across the boundary to include a F_4 rotation by angle phi.
2. Use the existing Lanczos solver to compute E_0(phi) for several phi values.
3. Fit a parabola to extract d^2 E_0 / d phi^2.

**Challenge:** The F_4 Lie algebra has dimension 52. Implementing F_4 rotations on V_{1/2} = R^16 requires the explicit action of F_4 on R^16 (the spinor representation S_9, viewed as a real representation). The existing codebase has the Spin(9) action (36-dim, Phase 28-02) and the full Cl(9,0) structure. The remaining 16 generators of F_4 (beyond spin(9)) act as transformations of the V_0 Peirce operators. These are NOT yet implemented.

**Feasibility:** On a 4-site chain (d=16 per site, 65k Hilbert space), computing E_0(phi) for 5-10 phi values costs 5-10 Lanczos runs, each ~10-30 seconds. Total: a few minutes. The hard part is constructing the correct twisted Hamiltonian, which requires explicit F_4 generators -- a primarily ALGEBRAIC task, not a computational bottleneck.

### Task 4: NL Sigma Model on F_4/Spin(9)

**Method:** Classical Monte Carlo on OP^2 = F_4/Spin(9) with lattice regularization.

The nonlinear sigma model on the target manifold M = F_4/Spin(9) = OP^2 has the standard form:

```
S[n] = (rho_s / 2) * integral d^d x * g_{AB}(n) * partial_mu n^A * partial_mu n^B
```

where n(x) in OP^2, g_{AB} is the round metric on OP^2 (Fubini-Study type for the octonionic projective plane), and rho_s is the stiffness constant.

**Lattice regularization:** Discretize onto a square lattice. Each site carries a field n_i in OP^2. The lattice action is:

```
S_lat = -beta * sum_{<i,j>} cos(d(n_i, n_j))
```

where d(n_i, n_j) is the geodesic distance on OP^2 and beta = rho_s * a^{d-2}. Alternatively, parametrize by rank-1 idempotents P in h_3(O) (which ARE the points of OP^2) and use:

```
S_lat = -beta * sum_{<i,j>} Tr(P_i * P_j)
```

where the trace inner product on h_3(O) provides a natural distance.

**Implementation:**

1. Parametrize OP^2 points as rank-1 projectors P in h_3(O): P = v * v^T / (v^T * v) for v in the "octonionic line" (normalized octonionic 3-vectors). The constraint is: P^2 = P (idempotent), Tr(P) = 1, and P in h_3(O).
2. Monte Carlo updates: Propose a new P' at site i by applying a random F_4 rotation to P_i (or more practically, by perturbing the octonionic 3-vector v and reprojecting).
3. Metropolis accept/reject with the lattice action.
4. Measure correlations <Tr(P_i P_j)> to extract correlation length.

**Feasibility:** Classical MC on OP^2 is the MOST tractable large-lattice computation. Each site carries a rank-1 projector (a 27-dim real vector satisfying constraints, effectively parametrized by 16 real degrees of freedom). The computational cost per MC sweep is O(N * d_target) = O(N * 16). For a 32x32 lattice (N=1024), one MC sweep takes microseconds.

**Software:** Pure Python/NumPy. The existing `peirce_coupling.py` H3Matrix class provides the Jordan product and trace inner product. Extend with:
- `sample_random_OP2_point()`: Random rank-1 idempotent in h_3(O)
- `propose_OP2_update(P, step_size)`: Local MC update
- `op2_action(P_list, beta, lattice)`: Compute lattice action

**Warning:** The non-associativity of the octonions means that the standard Lie group update algorithms (used for O(N) or SU(N) models) need modification. One cannot simply exponentiate a Lie algebra element and multiply. Use the explicit parametrization via octonionic 3-vectors instead.

---

## Logical Dependencies

```
v8.0 T_b operators (16x16, code/octonion_algebra.py)
  -> H_eff construction (Task 1: bilinear T_a^(i) T_a^(j))
    -> ED ground state (Task 2: Lanczos on sparse H)
      -> Order parameter & correlation functions
      -> Anderson tower analysis (spectrum)
    -> Twisted BC Hamiltonian (Task 3: requires F_4 generators)
      -> Spin stiffness rho_s extraction

v8.0 Peirce projectors + Jordan product
  -> OP^2 parametrization (rank-1 idempotents)
    -> Classical MC on OP^2 (Task 4)
      -> Correlation length, phase diagram
      -> Comparison with quantum rho_s from Task 3

Task 1 output -> Task 2 input (H_eff needed for ED)
Task 2 output -> Task 3 input (ground state needed for rho_s baseline)
Task 4 is INDEPENDENT of Tasks 1-3 (classical sigma model, separate code path)
```

---

## Software and Library Versions

| Tool | Version | Purpose | Status |
|------|---------|---------|--------|
| Python | 3.14.2 | Runtime | Already in project |
| NumPy | 2.4.2 | Array operations, linear algebra | Already in project |
| SciPy | >= 1.17 | Sparse matrices, eigsh (Lanczos) | Already in project |
| SymPy | >= 1.13 | Symbolic verification of algebraic identities | Already in project |
| Matplotlib | >= 3.8 | Plotting spectra, correlation functions | Already in project |

**No new dependencies required.** The entire computational pipeline runs on the existing Python/NumPy/SciPy stack.

---

## Recommended Investigation Scope

Prioritize:
1. **H_eff construction from T_b (Formulation A, V_{1/2} representation):** This is the core algebraic-to-numerical bridge. Build the 2-site Hamiltonian first, verify F_4-derived symmetries, then extend to 3-4 sites.
2. **Ground state spectrum for 2-4 site chains:** Extract the Anderson tower structure, gap scaling, and order parameter. This is the minimal SSB diagnostic.
3. **Classical MC on OP^2:** The most tractable path to large-lattice behavior and sigma model verification.

Defer:
- **Spin stiffness via twisted BC:** Requires F_4 generators beyond spin(9), which is primarily an algebraic construction task. Do after H_eff is validated.
- **Full 27-dim formulation (Formulation B):** Only needed if Formulation A misses physics that lives outside V_{1/2}. Start with Formulation A.
- **DMRG or tensor network methods:** Not justified given the feasibility of ED for these system sizes and the absence of F_4-symmetric tensor network codes.

---

## Feasibility Summary

| Task | Feasible? | Limiting Factor | Estimated Wall Time |
|------|-----------|-----------------|---------------------|
| H_eff construction (2-site) | YES | Algebraic, not computational | < 1 minute |
| H_eff construction (4-site) | YES | Sparse matrix construction | < 5 minutes |
| ED ground state (4 sites, d=16) | YES | Lanczos on 65k x 65k sparse | 10-30 seconds |
| ED ground state (6 sites, d=16) | MARGINAL | 16M x 16M sparse, ~1 GB/vector | 10-60 minutes |
| Full spectrum (4 sites, d=16) | YES | Dense diag of 65k x 65k | 5-15 minutes |
| Classical MC on OP^2 (32x32) | YES | CPU-bound, no memory issue | Minutes per 10^5 sweeps |
| Spin stiffness (4 sites) | YES, after F_4 generators | 5-10 Lanczos runs | A few minutes |
| SSB finite-size scaling | YES (3-4 data points) | Only 3-4 feasible system sizes | Combined: ~1 hour |

**Overall verdict:** All proposed calculations are feasible on a local workstation. The main bottleneck is ALGEBRAIC (constructing the correct H_eff and F_4 generators), not computational.

---

## Key References

- Baez, J.C., "The Octonions," Bull. AMS 39 (2002) 145-205, [math/0105155](https://arxiv.org/abs/math/0105155) -- Standard reference for h_3(O), F_4, OP^2 structure
- Boyle, L., "The Standard Model, The Exceptional Jordan Algebra, and Triality," [arXiv:2006.16265](https://arxiv.org/abs/2006.16265) -- Complexification of h_3(O) and SM connection; Spin(9)->Spin(10)
- Bernardoni et al., "Mapping the geometry of the F_4 group," J. Math. Phys. 49 (2008), [arXiv:0705.3978](https://arxiv.org/abs/0705.3978) -- Explicit F_4 parametrization via Spin(9) fibration, Euler angles for F_4
- Krasnov, K., "Spin(11,3), particles, and octonions," J. Math. Phys. 62 (2021), [arXiv:1912.11282](https://arxiv.org/abs/1912.11282) -- J_u complex structure, G_SM stabilizer
- Braunstein, S.L. and Caves, C.M., PRL 72, 3439 (1994) -- SLD Fisher metric definition (used in existing code)
- Sandvik, A.W., [arXiv:2601.20189](https://arxiv.org/abs/2601.20189) (2025) -- High-precision QMC for Heisenberg AFM (SSB benchmark)
- Lhuillier, C., "Exact diagonalization study of the antiferromagnetic spin-1/2 Heisenberg model on the square lattice," [arXiv:0812.3420](https://arxiv.org/abs/0812.3420) -- Spin stiffness via ED methodology

---

## Detailed Algorithm: H_eff Construction from T_b Operators

### Step 1: Load existing T_b matrices

```python
# In code/octonion_algebra.py, the T_b matrices are already computed.
# T_b[k] for k=0,...,9 are 16x16 real numpy arrays.
# T_b[0] = (1/4)*I_16  (trace element)
# T_b[1]: diagonal, eigenvalues {-1/4, +1/4}
# T_b[2..9]: off-diagonal Clifford generators (rescaled)
```

### Step 2: Build 2-site Hamiltonian

The nearest-neighbor interaction coupling sites i and j through V_0 mediators:

```python
# H_bond = sum_{a=0}^{9} T_a (x) T_a
# where (x) denotes Kronecker product
import numpy as np
from scipy import sparse

def build_jordan_bond(T_b_list):
    """Build the 2-site bond Hamiltonian from Peirce T_b operators.

    H_bond = sum_a T_a (x) T_a, acting on V_{1/2}^{(i)} (x) V_{1/2}^{(j)}.
    Dimension: 16^2 = 256.
    """
    d = T_b_list[0].shape[0]  # = 16
    H = np.zeros((d*d, d*d))
    for T in T_b_list:
        H += np.kron(T, T)
    return H
```

### Step 3: Verify symmetry

```python
# The Hamiltonian must commute with diagonal Spin(9) action:
# [H, g (x) g] = 0 for all g in Spin(9).
# Spin(9) generators are the 36 commutators [T_a, T_b] (from Phase 28-02).
# Verification: compute [H, L (x) I + I (x) L] for each L in spin(9).
```

### Step 4: Extend to N sites

```python
def build_jordan_chain(N, T_b_list, bc='obc'):
    """Build N-site chain Hamiltonian.

    H = J * sum_{<i,j>} sum_a T_a^(i) T_a^(j)

    Uses sparse Kronecker products for scalability.
    """
    d = T_b_list[0].shape[0]  # = 16
    dim = d ** N
    H = sparse.csr_matrix((dim, dim))
    bonds = [(i, i+1) for i in range(N-1)]
    if bc == 'pbc' and N > 2:
        bonds.append((N-1, 0))
    for (site_i, site_j) in bonds:
        for T in T_b_list:
            # Build I (x) ... (x) T (x) ... (x) T (x) ... (x) I
            ops = [sparse.eye(d)] * N
            ops[site_i] = sparse.csr_matrix(T)
            ops[site_j] = sparse.csr_matrix(T)
            term = ops[0]
            for k in range(1, N):
                term = sparse.kron(term, ops[k])
            H = H + term
    return H
```

### Step 5: Ground state and observables

```python
from scipy.sparse.linalg import eigsh

def ground_state_and_gap(H, k=10):
    """Compute lowest k eigenvalues and ground state."""
    vals, vecs = eigsh(H, k=k, which='SA')
    idx = np.argsort(vals)
    return vals[idx], vecs[:, idx]
```

---

## Detailed Algorithm: Classical MC on OP^2

### OP^2 point representation

A point in OP^2 = F_4/Spin(9) is a rank-1 idempotent in h_3(O):

```
P = v v^dagger / Tr(v v^dagger)
```

where v is an "octonionic 3-vector" (column of h_3(O)) with Tr(P) = 1, P^2 = P (under Jordan product: P o P = P).

In practice, represent P by its 27 real components subject to the idempotency and trace constraints. The constraint surface has dim = 27 - 11 = 16 (matching dim(OP^2) = 16).

### Lattice action

```python
def op2_lattice_action(projectors, bonds, beta):
    """Compute S = -beta * sum_{<i,j>} Tr(P_i . P_j).

    Tr(P_i . P_j) = frobenius_inner_product of their h_3(O) matrices.
    """
    S = 0.0
    for (i, j) in bonds:
        S -= beta * np.sum(projectors[i] * projectors[j])  # Frobenius
    return S
```

### Update proposal

```python
def propose_op2_update(P, step_size, rng):
    """Propose a new rank-1 idempotent near P.

    Strategy: Perturb P in a tangent direction and reproject.
    Tangent space at P is T_P(OP^2) = V_{1/2}(P) in h_3(O).
    """
    # 1. Generate random tangent vector in V_{1/2}(P)
    delta = rng.normal(0, step_size, size=27)
    # Project delta to V_{1/2}(P): delta_h = Pi_{1/2}(delta)
    delta_h = peirce_half_projection(P, delta)
    # 2. Move along geodesic (or retract): P' = exp_P(delta_h)
    # For small step_size, retraction suffices:
    P_new = P + delta_h
    # 3. Reproject to rank-1 idempotent
    P_new = project_to_rank1_idempotent(P_new)
    return P_new
```

### Measurement

```python
def measure_correlator(projectors, i, j):
    """Compute Tr(P_i . P_j) - 1/3.

    For uncorrelated random projectors, <Tr(P_i P_j)> = 1/3 (OP^2 average).
    Connected correlator: C(r) = <Tr(P_i P_j)> - 1/3.
    """
    return np.sum(projectors[i] * projectors[j]) - 1.0/3.0
```

---

## Resource Estimates for Local Workstation

Assuming: M1/M2 Mac, 16-32 GB RAM, single-threaded Python, NumPy with Accelerate BLAS.

| Calculation | RAM | Wall Time | Notes |
|-------------|-----|-----------|-------|
| T_b loading + 2-site H_eff | < 10 MB | < 1 s | Dense 256x256 |
| 4-site H_eff construction | ~50 MB | ~5 min | Sparse 65k x 65k, ~10 Kronecker products per bond |
| Lanczos ground state (N=4) | ~100 MB | ~30 s | eigsh with k=10 |
| Dense full spectrum (N=4) | ~32 GB | ~15 min | numpy.linalg.eigh on 65k x 65k dense |
| Lanczos ground state (N=6) | ~2 GB | ~30-60 min | 16M x 16M sparse |
| Classical MC (32x32, 10^6 sweeps) | ~100 MB | ~30 min | CPU-bound, no memory issue |
| Spin stiffness (N=4, 10 phi values) | ~100 MB | ~5 min | 10 Lanczos runs |

**Critical path:** The 4-site full spectrum (dense) is the most memory-intensive calculation at ~32 GB. If RAM is limited to 16 GB, use Lanczos for the lowest ~50-100 eigenvalues instead, which gives the Anderson tower without needing the full spectrum. Cost: ~2-5 minutes.

---

## Validation Strategy

| Check | Expected Result | Tolerance | Source |
|-------|----------------|-----------|--------|
| H_eff commutes with spin(9) generators | [H, L^(diag)] = 0 | Machine precision | F_4 symmetry |
| 2-site ground state energy | Analytic from Jordan product | Exact | Direct computation |
| Tr(H_eff) | sum_a Tr(T_a)^2 * N_bonds | Exact | Trace identity |
| Classical MC at beta -> infinity | Ordered configuration (single P) | Visible | Trivial limit |
| Classical MC at beta -> 0 | Uniform on OP^2, <Tr(P_i P_j)> -> 1/3 | ~1/sqrt(N_samples) | Disordered limit |
| Spin stiffness at large beta | rho_s > 0 (ordered) | 10% from fit | SSB criterion |
| Gap scaling 1/N | Anderson tower | Factor of 2 | Finite-size theory |

---

## Sources

- Baez, J.C., "The Octonions," Bull. AMS 39 (2002) 145-205, [math/0105155](https://arxiv.org/abs/math/0105155)
- Boyle, L., [arXiv:2006.16265](https://arxiv.org/abs/2006.16265) (2020)
- Bernardoni et al., [arXiv:0705.3978](https://arxiv.org/abs/0705.3978) (2007)
- Krasnov, K., [arXiv:1912.11282](https://arxiv.org/abs/1912.11282) (2019)
- SciPy sparse documentation, https://docs.scipy.org/doc/scipy/reference/sparse.linalg.html (2026)
- XDiag library for ED: [arXiv:2505.02901](https://arxiv.org/abs/2505.02901) (2025) -- recent ED library, not needed here but confirms state of the art
- Sandvik, A.W., [arXiv:2601.20189](https://arxiv.org/abs/2601.20189) (2025) -- QMC spin stiffness methodology
