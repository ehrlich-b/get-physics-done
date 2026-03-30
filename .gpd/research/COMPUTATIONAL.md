# Computational Approaches: Fisher Information Geometry on SWAP Lattice Reduced States

**Surveyed:** 2026-03-29
**Domain:** Quantum information geometry / Exact diagonalization / Riemannian geometry on state manifolds
**Confidence:** HIGH

### Scope Boundary

COMPUTATIONAL.md covers computational TOOLS, libraries, algorithms, and infrastructure for computing the Fisher information metric on reduced density matrices of the SWAP Hamiltonian ground state, verifying smoothness and positive-definiteness, computing geodesics, and checking lattice distance recovery. It does NOT cover the physics motivation (PRIOR-WORK.md) or the analytical proof strategy (METHODS.md).

**Relationship to existing codebase:** The project has a working Python/NumPy/SciPy exact diagonalization framework in `code/ed_entanglement.py` (Phase 11) with sparse Hamiltonian construction (Heisenberg 1D/2D, self-modeling/SWAP, TFI), Lanczos ground state solver, partial trace, and von Neumann entropy. The `code/area_law_verification.py` extends this to area-law fits. This document covers the NEW computational layer needed: Fisher metric tensor extraction from families of reduced density matrices parametrized by lattice position, numerical differentiation and regularization for rank-deficient states, positive-definiteness verification, geodesic computation, and lattice distance comparison.

## Recommended Stack

Extend the existing `code/ed_entanglement.py` framework with a new module (~400 lines) implementing Fisher metric computation on reduced density matrices. Use the eigendecomposition-based formula for the quantum Fisher information metric (QFIM), which avoids matrix logarithm derivatives entirely and handles rank-deficient states naturally. Do not use external quantum metrology packages.

The reasons:

1. **The eigendecomposition formula is the standard.** For a parametrized family of density matrices rho(theta), the QFIM components are computed from eigenvalues and eigenvectors of rho directly. The formula has explicit handling of zero eigenvalues (those matrix elements are dropped). This is numerically stable and well-understood.

2. **The computation is small.** For N=8 lattice sites (n=2), Hilbert space dimension is 2^8 = 256. Reduced density matrices on Lambda sites with |Lambda| = 2-4 have dimension 4-16. Eigendecomposition of a 16x16 matrix is microsecond-scale. Even N=20 gives 2^20 ~ 10^6 dimensional Hilbert space, manageable for Lanczos, and reduced density matrices remain small.

3. **Integration with existing code is seamless.** The existing `partial_trace` function already produces reduced density matrices. The new code adds Fisher metric computation as a downstream consumer of those matrices.

4. **External packages add complexity without value.** QuanEstimation (Python/Julia hybrid, focused on parameter estimation optimization) and qutip (general-purpose quantum toolbox) could compute QFIM but introduce heavy dependencies for what amounts to a 50-line eigendecomposition calculation. The project pattern is self-contained numerical verification.

**Primary stack:** NumPy + SciPy (already in project). No new dependencies needed.

## Numerical Algorithms

### 1. Quantum Fisher Information Metric via Eigendecomposition

| Algorithm | Problem | Convergence | Cost per Step | Memory | Key Reference |
|-----------|---------|-------------|---------------|--------|---------------|
| Eigendecomposition QFIM | g_ij(x) from rho(x) family | Exact (given eigensystem) | O(d^3) for d x d rho | O(d^2) | Braunstein-Caves PRL 72 (1994) |

This is the CENTRAL algorithm. The quantum Fisher information metric (also called the Bures metric or fidelity susceptibility) on a manifold of density matrices parametrized by theta = (theta^1, ..., theta^k) is:

```
g_{ij}(theta) = (1/2) Tr[rho(theta) {L_i, L_j}]
```

where L_i is the symmetric logarithmic derivative (SLD) satisfying:

```
d rho / d theta^i = (1/2)(rho L_i + L_i rho)
```

#### Algorithm: QFIM via Eigendecomposition

```
INPUT:  Family of density matrices rho(theta) with theta in R^k
        Point theta_0 at which to evaluate the metric
        Finite difference step size epsilon
OUTPUT: k x k metric tensor g_{ij}(theta_0)

STEP 1: Eigendecompose rho_0 = rho(theta_0)
  rho_0 = sum_m lambda_m |m><m|
  Discard eigenvalues lambda_m < threshold (e.g., 1e-14)
  Record: eigenvalues {lambda_m}, eigenvectors {|m>}, active set S = {m : lambda_m > threshold}

STEP 2: For each parameter direction i = 1, ..., k:
  Compute d_rho_i = d rho / d theta^i via finite differences:
    d_rho_i = (rho(theta_0 + epsilon * e_i) - rho(theta_0 - epsilon * e_i)) / (2 * epsilon)
  where e_i is the i-th unit vector.

  CRITICAL: Each rho(theta_0 +/- epsilon * e_i) must be computed from a SEPARATE
  partial trace of the ground state. For lattice position parametrization, this means
  shifting which sites form the subsystem.

STEP 3: Compute metric components using the closed-form SLD formula:
  g_{ij} = sum_{m,n in S} (2 / (lambda_m + lambda_n)) * Re[<m|d_rho_i|n> * <n|d_rho_j|m>]

  where the sum runs over pairs (m,n) with lambda_m + lambda_n > 0.

  DERIVATION: The SLD equation rho L + L rho = 2 d_rho has matrix elements
    (lambda_m + lambda_n) <m|L|n> = 2 <m|d_rho|n>
  so <m|L_i|n> = 2 <m|d_rho_i|n> / (lambda_m + lambda_n) when the denominator is nonzero.
  Then g_{ij} = (1/2) Tr[rho {L_i, L_j}] = sum_{m,n} [lambda_m * <m|L_i|n><n|L_j|m>]
  which simplifies to the formula above.

STEP 4: Verify g is a real symmetric matrix (to machine precision).
  Check: g_{ij} = g_{ji} to tolerance 1e-12.
  Check: all eigenvalues of g are non-negative (positive semi-definite).

COMPLEXITY:
  - Eigendecomposition: O(d^3) where d = dim(rho) = 2^|Lambda|
  - Finite differences: 2k ground state computations (if varying Hamiltonian parameters)
    OR 2k partial traces (if varying subsystem position, ground state fixed)
  - Metric assembly: O(d^2 * k^2) per point
  - For |Lambda| = 2 (d=4), k = lattice dimension (1D: k=1, 2D: k=2): trivial
  - For |Lambda| = 4 (d=16), k = 2: still trivial
```

#### Convergence Properties

- **Finite difference convergence:** Central differences give O(epsilon^2) error in d_rho. Optimal epsilon ~ sqrt(machine_epsilon) * scale ~ 1e-8 for double precision when the parameter is a lattice position measured in lattice spacings.
- **Eigenvalue threshold:** Setting threshold = 1e-14 excludes numerically zero eigenvalues without introducing bias. This is the same threshold used in `ed_entanglement.py` for von Neumann entropy.
- **Known failure mode:** When two eigenvalues lambda_m, lambda_n are both very small but nonzero, the ratio 2/(lambda_m + lambda_n) amplifies noise in <m|d_rho|n>. Mitigation: use threshold on lambda_m + lambda_n directly (e.g., 1e-10), not just on individual eigenvalues.

#### Why NOT matrix logarithm derivatives

The naive approach -- compute g_{ij} = Tr[d_i(log rho) d_j(rho)] -- requires the matrix logarithm and its derivatives. This fails catastrophically for rank-deficient states because log(rho) has -infinity eigenvalues at zero eigenvalues of rho. The eigendecomposition formula above avoids this entirely by working in the eigenbasis and explicitly excluding zero eigenvalues.

Do NOT use `scipy.linalg.logm` for Fisher metric computation. It uses the Al-Mohy/Higham (2012) algorithm which is designed for well-conditioned invertible matrices and will produce garbage for near-singular density matrices.

### 2. Parametrization of Reduced Density Matrices by Lattice Position

| Algorithm | Problem | Convergence | Cost per Step | Memory | Key Reference |
|-----------|---------|-------------|---------------|--------|---------------|
| Subsystem sliding window | rho_Lambda(x) for varying x | N/A (exact) | O(2^N * 2^{2|Lambda|}) | O(2^{2|Lambda|}) | Standard partial trace |

For the SWAP lattice, the natural parametrization of reduced density matrices is by lattice position: fix a subsystem shape Lambda (e.g., a block of 2 or 4 adjacent sites), and vary its position x on the lattice. The family {rho_Lambda(x)} parametrizes a manifold whose Fisher metric we want to compute.

#### Algorithm: Lattice Position Parametrization

```
INPUT:  Ground state |psi> of SWAP Hamiltonian on N sites
        Subsystem shape Lambda (e.g., {0, 1} for two adjacent sites)
        Lattice translation vector e_mu (e.g., e_1 = (1,0) in 2D)
OUTPUT: Family rho_Lambda(x) for x = 0, 1, 2, ..., L-1

For 1D PBC lattice with N sites:
  rho_Lambda(x) = Tr_{complement of {x, x+1, ..., x+|Lambda|-1 mod N}} |psi><psi|

CRITICAL SUBTLETY (PBC): On a periodic lattice, translation symmetry means
all rho_Lambda(x) are related by a unitary permutation of sites. The Fisher
metric should be the SAME at every x (by symmetry). The test is whether the
metric is constant along the lattice -- non-constant metric on a PBC lattice
signals a bug.

For 1D OBC lattice:
  rho_Lambda(x) varies nontrivially with x due to boundary effects.
  The Fisher metric SHOULD vary near boundaries and be approximately constant
  in the bulk. Use OBC for the actual physics (boundary-to-bulk transition
  reveals the emergent geometry).

For 2D lattice (Lx x Ly):
  rho_Lambda(x,y) with x,y the position of the subsystem's corner.
  Metric tensor is 2x2 (or dxd in d dimensions).
```

### 3. Alternative: Fidelity-Based Fisher Metric (Bures Metric)

| Algorithm | Problem | Convergence | Cost per Step | Memory | Key Reference |
|-----------|---------|-------------|---------------|--------|---------------|
| Fidelity susceptibility | g_ij from F(rho(x), rho(x+dx)) | O(epsilon^2) | O(d^3) for fidelity | O(d^2) | Zanardi et al. PRA 76 (2007) |

The Bures metric is equivalent to the quantum Fisher metric (up to a factor of 4). It can be computed from the quantum fidelity:

```
F(rho, sigma) = [Tr sqrt(sqrt(rho) sigma sqrt(rho))]^2

ds^2_Bures = 2(1 - sqrt(F(rho(x), rho(x+dx))))

g_{ij}^{Bures} = -(1/2) d^2 F / d theta^i d theta^j |_{theta=theta_0}
               = (1/4) g_{ij}^{Fisher}
```

#### Algorithm: Fidelity-Based Metric

```
INPUT:  rho_0 = rho(theta_0), rho_{+i} = rho(theta_0 + epsilon * e_i) for each i
OUTPUT: g_{ij}^{Bures}

STEP 1: For each pair (i, j):
  If i == j:
    g_{ii} = (2/epsilon^2)(1 - sqrt(F(rho_0, rho_{+i})))
  If i != j:
    Use the polarization identity:
    g_{ij} = (1/2)[g(e_i+e_j, e_i+e_j) - g(e_i, e_i) - g(e_j, e_j)]
    This requires computing F(rho_0, rho_{+i+j}) where theta_{+i+j} = theta_0 + epsilon*(e_i + e_j).

STEP 2: Compute fidelity via eigendecomposition:
  F(rho, sigma) = [Tr sqrt(sqrt(rho) sigma sqrt(rho))]^2
  = [sum_k sqrt(mu_k)]^2 where mu_k are eigenvalues of sqrt(rho) sigma sqrt(rho).

  OR equivalently: F(rho, sigma) = ||sqrt(rho) sqrt(sigma)||_1^2
  where ||A||_1 = Tr sqrt(A^dagger A) is the trace norm.

  Numerically: compute sqrt(rho) via eigendecomposition, form M = sqrt(rho) sigma sqrt(rho),
  eigendecompose M, take sqrt of eigenvalues, sum and square.

RECOMMENDATION: Use fidelity-based metric as CROSS-VALIDATION of the SLD eigendecomposition
method. They must agree to machine precision (up to the factor of 4). The SLD method is
preferred as primary because it gives the SLD operators L_i directly, which are useful for
other checks.
```

### 4. Correlation Function Computation

| Algorithm | Problem | Convergence | Cost per Step | Memory | Key Reference |
|-----------|---------|-------------|---------------|--------|---------------|
| Two-point correlator from ground state | <sigma_i^a sigma_j^b> | Exact (given |psi>) | O(2^N * N) for all pairs | O(2^N) | Standard quantum mechanics |

#### Algorithm: Two-Point Correlation Functions

```
INPUT:  Ground state |psi> of SWAP Hamiltonian on N sites
        Operator O_i at site i (e.g., sigma_z)
OUTPUT: C(r) = <psi|O_i O_{i+r}|psi> - <psi|O_i|psi><psi|O_{i+r}|psi>

STEP 1: For each pair of sites (i, j) with j = i + r:
  Compute <O_i O_j> = <psi| (O_i tensor O_j tensor I_{rest}) |psi>

  EFFICIENT METHOD: Build the sparse operator O_i tensor O_j acting on full 2^N space.
  For sigma_z^i sigma_z^j, this is diagonal:
    (sigma_z^i sigma_z^j)|s> = spin(s,i) * spin(s,j) |s>
  So <sigma_z^i sigma_z^j> = sum_s |psi_s|^2 * spin(s,i) * spin(s,j)
  This is O(2^N) per pair, no matrix multiplication needed.

  For sigma_+^i sigma_-^j (needed for full correlator):
    This flips spins at sites i,j: only contributes when i is up and j is down.
    <psi| sigma_+^i sigma_-^j |psi> = sum_{s: i down, j up} conj(psi_{s with i up, j down}) * psi_s

STEP 2: Average over translates (for PBC) to reduce noise:
  C(r) = (1/N) sum_{i=0}^{N-1} [<O_i O_{i+r}> - <O_i><O_{i+r}>]

STEP 3: Fit exponential decay:
  |C(r)| ~ A * exp(-r/xi)
  where xi is the correlation length.

  Fit via least-squares on log|C(r)| vs r (linear regression in log space).
  Exclude r = 0 (self-correlation) and r close to N/2 (PBC finite-size effects).

CONVERGENCE: Exact for given |psi>. The only approximation is Lanczos convergence
for the ground state itself (already validated in Phase 11 at 1e-12 accuracy).

KNOWN ISSUE (1D AFM Heisenberg, n=2): The spin-1/2 Heisenberg chain is GAPLESS
(Bethe ansatz exact solution). Correlations decay as a POWER LAW, not exponentially:
  C(r) ~ (-1)^r / r^eta  with eta = 1
This is critical: the 1D case does NOT give exponential decay. Must use d >= 2
(where the Heisenberg AFM has long-range Neel order and a magnon gap in d=3)
or use n > 2 (where the SWAP Hamiltonian may have a gap even in 1D).
```

### 5. Positive-Definiteness and Smoothness Verification

| Algorithm | Problem | Convergence | Cost per Step | Memory | Key Reference |
|-----------|---------|-------------|---------------|--------|---------------|
| Eigenvalue check | g > 0 at each point | Exact | O(k^3) for k x k metric | O(k^2) | Standard linear algebra |
| Numerical gradient | smoothness of g_{ij}(x) | O(h^2) finite diff | O(k^2) per point | O(k^2 * N_points) | Standard numerical analysis |

#### Algorithm: Positive-Definiteness Check

```
INPUT:  Metric tensor g_{ij}(x) at lattice points x = 0, 1, ..., L-1
OUTPUT: Boolean: is g positive-definite at all interior points?
        Minimum eigenvalue across all points
        Condition number at each point

STEP 1: At each lattice point x:
  Compute eigenvalues of g(x): lambda_1 >= lambda_2 >= ... >= lambda_k
  Record lambda_min(x) = lambda_k
  Record condition number kappa(x) = lambda_1 / lambda_k

STEP 2: Check:
  - lambda_min(x) > 0 for all x in the bulk (away from boundaries if OBC)
  - kappa(x) is bounded (not growing with system size)
  - lambda_min(x) is bounded away from zero by a margin that grows (or at least
    does not shrink) with system size

POSITIVE-DEFINITENESS FAILURE MODES:
  - If rho_Lambda(x) has the same spectrum for all x (e.g., PBC with exact
    translation symmetry), then d_rho = 0 and g = 0. This happens on PBC lattices
    where rho(x) is truly translation-invariant. SOLUTION: use OBC, or parametrize
    by subsystem size rather than position, or add a weak boundary/impurity.
  - If Lambda is too large relative to N, the reduced state becomes nearly pure
    (rho ~ |psi><psi|), and the metric degenerates. Keep |Lambda| < N/3.
```

#### Algorithm: Smoothness Verification

```
INPUT:  g_{ij}(x) sampled at all integer lattice points x = 0, 1, ..., L-1
OUTPUT: Smoothness measure (discrete second derivative bound)

STEP 1: Compute discrete second derivative at each interior point:
  Delta^2 g_{ij}(x) = g_{ij}(x+1) - 2*g_{ij}(x) + g_{ij}(x-1)

STEP 2: Check:
  max_x |Delta^2 g_{ij}(x)| / max_x |g_{ij}(x)| << 1
  This ratio being small means g varies slowly on the lattice scale.

STEP 3: Fit g_{ij}(x) to a smooth function (polynomial or constant for bulk).
  For PBC: g should be exactly constant (symmetry). Deviation is a bug.
  For OBC: g should be approximately constant in the bulk, varying near boundaries.
  Fit residual should decrease with system size (finite-size effects shrinking).
```

### 6. Geodesic Distance Computation

| Algorithm | Problem | Convergence | Cost per Step | Memory | Key Reference |
|-----------|---------|-------------|---------------|--------|---------------|
| Discrete geodesic via Dijkstra | Shortest path on metric graph | Exact (on graph) | O(N^2 log N) | O(N^2) | Standard graph algorithm |
| ODE integration | Geodesic equation on manifold | O(h^4) RK4 | O(k^3) per step | O(k) | Standard Riemannian geometry |

#### Algorithm: Discrete Geodesic on Lattice

```
INPUT:  Metric tensor g_{ij}(x) at each lattice point x
        Start point x_A, end point x_B
OUTPUT: Geodesic distance d_g(x_A, x_B) on the Fisher manifold

METHOD 1: Weighted graph shortest path (RECOMMENDED for lattice)
  Build graph: nodes = lattice sites, edges = nearest-neighbor bonds.
  Edge weight w(x, x+e_mu) = sqrt(g_{mu mu}(x)) * (lattice spacing)
  (For diagonal metric; for full metric: w = sqrt(e_mu^T g(x) e_mu).)
  Run Dijkstra from x_A to x_B.

  This is the natural discrete geodesic for a lattice system.

METHOD 2: Geodesic ODE integration (for smooth interpolation)
  The geodesic equation is:
    d^2 x^mu / dt^2 + Gamma^mu_{alpha beta} (dx^alpha/dt)(dx^beta/dt) = 0
  where Gamma^mu_{alpha beta} = (1/2) g^{mu nu}(partial_alpha g_{nu beta}
    + partial_beta g_{nu alpha} - partial_nu g_{alpha beta})
  are the Christoffel symbols.

  For our lattice: Christoffel symbols from finite differences of g_{ij}(x).
  Integrate with RK4 or scipy.integrate.solve_ivp.

  WHEN TO USE: Only if smooth interpolation between lattice points is needed.
  For lattice distance comparison, Method 1 is sufficient.

COMPARISON WITH LATTICE DISTANCE:
  The key test: does d_g(x_A, x_B) ~ c * d_lattice(x_A, x_B) for a constant c?

  Compute:
    ratio(x_A, x_B) = d_g(x_A, x_B) / d_lattice(x_A, x_B)

  If ratio is approximately constant (within finite-size corrections), the Fisher
  metric recovers the lattice geometry. Report:
    - mean(ratio), std(ratio) over all pairs
    - max deviation from mean
    - scaling with system size (does std shrink?)
```

### 7. Ground State Computation (Existing, Extended)

| Algorithm | Problem | Convergence | Cost per Step | Memory | Key Reference |
|-----------|---------|-------------|---------------|--------|---------------|
| Lanczos (scipy eigsh) | Ground state of H | Exponential in Krylov dim | O(nnz * k) per iter | O(2^N * k) | Lanczos 1950, scipy docs |

The existing `code/ed_entanglement.py` provides `ground_state(H, k=1)` using `scipy.sparse.linalg.eigsh` with `which='SA'` (smallest algebraic). No modification needed for N=8-16. For N=20 (2^20 ~ 10^6 dimensional Hilbert space), Lanczos converges in O(100) iterations for gapped systems. Memory requirement: O(2^N * k) complex doubles = O(8 MB * k) for N=20.

**Extension needed:** For 2D lattices at N=16 (4x4), the Hilbert space is 2^16 = 65536, which is manageable. For N=20 in 2D (e.g., 4x5 or 5x4), 2^20 ~ 10^6, still feasible with sparse methods. The existing `construct_heisenberg_2d` handles this.

## Software Ecosystem

### Primary Tools

| Tool | Version | Purpose | License | Maturity |
|------|---------|---------|---------|----------|
| NumPy | >= 2.0 | Dense matrix operations, eigendecomposition, partial trace | BSD | Stable |
| SciPy | >= 1.10 | Sparse Hamiltonian construction, Lanczos (eigsh), matrix functions | BSD | Stable |
| Python | >= 3.11 | Runtime | PSF | Stable |
| pytest | >= 9.0 | Test framework (existing project pattern) | MIT | Stable |
| matplotlib | >= 3.0 | Visualization of Fisher metric, correlation functions, geodesics | BSD | Stable |

### Supporting Tools

| Tool | Version | Purpose | When Needed |
|------|---------|---------|-------------|
| SymPy | >= 1.13 | Symbolic verification of small-case Fisher metric formulas | Only for N=4 (2-site) analytic checks |
| networkx | >= 3.0 | Graph shortest path for geodesic computation | Only if Dijkstra needed on non-trivial graph topologies |

### Tools NOT to Use

| Tool | Why Not | What Instead |
|------|---------|-------------|
| QuanEstimation | Python/Julia hybrid; heavy dependency for a 50-line calculation; focused on parameter optimization, not metric extraction | Direct eigendecomposition formula |
| qutip | General-purpose quantum toolbox; adds large dependency tree; Fisher metric not a primary feature | Direct NumPy computation |
| scipy.linalg.logm | Catastrophically fails for rank-deficient density matrices (log of zero eigenvalue); completely wrong approach | Eigendecomposition-based SLD formula |
| jax / autograd | Automatic differentiation could compute d_rho exactly, but adds complexity for a problem where finite differences suffice at our precision needs | Central finite differences on partial traces |
| pennylane / cirq | Quantum computing frameworks; designed for circuit simulation, not lattice Hamiltonian ground states | Existing ED framework |

## Data Flow

```
SWAP Hamiltonian H (from construct_self_modeling_1d / construct_heisenberg_2d)
  -> Lanczos ground state |psi> (from ground_state)
  -> For each lattice position x:
       -> partial_trace(psi, N, sites_Lambda(x)) -> rho_Lambda(x)
  -> For each pair of nearby positions (x, x+dx):
       -> Eigendecompose rho_Lambda(x) and rho_Lambda(x+dx)
       -> Compute d_rho via finite differences
       -> Compute QFIM g_{ij}(x) via SLD eigendecomposition formula
  -> Collect g_{ij}(x) at all lattice points
  -> Check positive-definiteness (eigenvalues of g)
  -> Check smoothness (discrete second derivatives)
  -> Compute geodesic distances (Dijkstra on weighted graph)
  -> Compare to lattice distances (ratio analysis)
  -> Cross-validate with fidelity-based Bures metric

PARALLEL BRANCH (correlation functions):
  -> For each pair of sites (i, j):
       -> Compute <O_i O_j> directly from |psi>
  -> Average over translates (PBC) or position (OBC)
  -> Fit exponential decay: C(r) ~ exp(-r/xi)
  -> Extract correlation length xi
  -> Compare xi to Fisher metric scale
```

## Computation Order and Dependencies

| Step | Depends On | Produces | Can Parallelize? |
|------|-----------|----------|-----------------|
| 1. Construct SWAP Hamiltonian | Existing ed_entanglement.py | Sparse H | Yes (across N values) |
| 2. Compute ground state | Step 1 | |psi> | No (one Lanczos per N) |
| 3. Compute all rho_Lambda(x) | Step 2 | Family of density matrices | Yes (across x) |
| 4. Compute two-point correlators | Step 2 | C(r) for all r | Yes (across pairs) |
| 5. Eigendecompose each rho_Lambda(x) | Step 3 | Eigenvalues, eigenvectors | Yes (across x) |
| 6. Compute d_rho via finite differences | Steps 3, 5 | Derivative matrices | Yes (across x, i) |
| 7. Assemble QFIM g_{ij}(x) | Steps 5, 6 | Metric tensor at each x | Yes (across x) |
| 8. Cross-validate with fidelity metric | Step 3 | Bures metric (must match Step 7) | Yes (parallel to Step 7) |
| 9. Positive-definiteness check | Step 7 | Pass/fail + eigenvalue report | No (needs all g) |
| 10. Smoothness check | Step 7 | Second derivative bounds | No (needs all g) |
| 11. Geodesic distances | Step 7 | d_g(x_A, x_B) for all pairs | No (needs all g) |
| 12. Lattice distance comparison | Step 11 | Ratio analysis | No (needs Step 11) |
| 13. Correlation length extraction | Step 4 | xi from exponential fit | No (needs all C(r)) |

## Resource Estimates

| Computation | Time (estimate) | Memory | Storage | Hardware |
|-------------|-----------------|--------|---------|----------|
| Ground state N=8 (1D, PBC) | < 1 sec | < 10 MB | Negligible | Laptop CPU |
| Ground state N=12 (1D, PBC) | < 1 sec | < 50 MB | Negligible | Laptop CPU |
| Ground state N=16 (1D, PBC) | ~ 5 sec | ~ 500 MB | Negligible | Laptop CPU |
| Ground state N=20 (1D, PBC) | ~ 1-5 min | ~ 8 GB | Negligible | Laptop CPU |
| Ground state 4x4 2D (PBC) | ~ 5 sec | ~ 500 MB | Negligible | Laptop CPU |
| All rho_Lambda(x) for N=16 | < 1 sec | < 10 MB | Negligible | Laptop CPU |
| All QFIM g_{ij}(x) for N=16 | < 1 sec | < 1 MB | Negligible | Laptop CPU |
| Correlation functions N=16 | < 1 sec | < 10 MB | Negligible | Laptop CPU |
| Full pipeline N=20 (1D) | ~ 5-10 min | ~ 8 GB | < 100 MB JSON | Laptop CPU, 16 GB RAM |
| Full pipeline 4x4 (2D) | ~ 1 min | ~ 500 MB | < 100 MB JSON | Laptop CPU |

The bottleneck is Lanczos for the ground state at N=20. Everything downstream (partial traces, eigendecomposition of small reduced density matrices, metric computation) is trivially fast.

**Hard limit:** N=22 requires 2^22 ~ 4 x 10^6 dimensional Hilbert space, needing ~32 GB for the state vector alone. N=24 is ~256 GB, impractical on a laptop. For N > 20, use symmetry sectors (total S_z conservation halves the space) to reach N=22-24.

### System Size Requirements for Reliable Fisher Metric Estimates

| System Size (N) | Hilbert Dim | Subsystem |Lambda| | rho Dim | Finite-Size Quality | Use Case |
|-----------------|-------------|----------------------|---------|---------------------|----------|
| 8 | 256 | 2 | 4 | Heavy finite-size effects | Algorithm validation only |
| 12 | 4096 | 2-3 | 4-8 | Moderate finite-size effects | Preliminary checks |
| 16 | 65536 | 2-4 | 4-16 | Acceptable for bulk metrics | Primary workhorse for 1D |
| 20 | 1048576 | 2-4 | 4-16 | Good (bulk well-separated from boundaries) | Best 1D case without symmetries |
| 4x4 (16) | 65536 | 2x2 (4 sites) | 16 | Acceptable for 2D | Primary workhorse for 2D |

**Recommendation:** Use N=16 as the primary test case for algorithm development and validation. Use N=20 for final quantitative results. Use N=8 only for debugging. Report all three sizes to demonstrate finite-size scaling.

**Subsystem size guidance:** |Lambda| = 2 sites gives a 4x4 reduced density matrix (cheap, but may miss spatial structure). |Lambda| = 4 sites gives 16x16 (captures more structure, still cheap). Do NOT use |Lambda| > N/3: the reduced state becomes nearly pure and the Fisher metric degenerates.

## Integration with Existing Code

- **Input formats:** The existing `ed_entanglement.py` produces the ground state as a complex NumPy array of shape (2^N,). Hamiltonian is a `scipy.sparse.csr_matrix`. These are the inputs to the new Fisher metric code.
- **Output formats:** Metric tensor g_{ij}(x) as a NumPy array of shape (N_points, k, k). Correlation functions C(r) as a 1D NumPy array. Results serialized as JSON with metadata (matching the existing `area_law_verification.py` output pattern).
- **Interface points:**
  - `ground_state(H)` from `ed_entanglement.py` -- unchanged, used as-is
  - `partial_trace(psi, N, sites_A)` from `ed_entanglement.py` -- unchanged, used as-is
  - NEW: `fisher_metric(psi, N, Lambda_sites, direction, epsilon)` -- computes one component of g
  - NEW: `fisher_metric_tensor(psi, N, Lambda_shape, x)` -- computes full g_{ij} at position x
  - NEW: `correlation_function(psi, N, operator, r_max)` -- computes C(r) for given operator
  - NEW: `geodesic_distance(g_tensor, x_A, x_B)` -- shortest path on metric graph
- **Convention bridge:** The existing code uses `coupling_convention=H_sum_hxy` for the Heisenberg model. The SWAP Hamiltonian is H_SWAP = H_Heisenberg + constant (same ground state). Fisher metric depends only on the ground state, so the constant shift is irrelevant.

## Open Questions

| Question | Why Open | Impact on Project | Approaches Being Tried |
|----------|---------|-------------------|----------------------|
| Does PBC translation symmetry make g = 0? | On PBC lattice, rho_Lambda(x) is x-independent by symmetry | If yes, must use OBC or alternative parametrization | Use OBC; alternative: parametrize by subsystem size instead of position |
| What is the optimal subsystem size |Lambda| for Fisher metric extraction? | Too small: insufficient spatial resolution; too large: rho nearly pure | Determines phase structure (what |Lambda| to test) | Systematic scan |Lambda| = 2, 3, 4 for N = 16, 20 |
| Does the n=2 (Heisenberg) SWAP lattice have exponential decay in d >= 2? | Critical for the chain: exponential decay needed for well-defined correlation length | If power-law in d=2, Fisher metric analysis still works but Lorentz argument weakens | d=3 Heisenberg AFM is gapped (Neel ordered); d=2 is marginal (ordered at T=0 but with algebraic corrections) |
| How do finite-size effects in the Fisher metric scale with N? | Need g(N) -> g(infinity) reliably | Determines whether N=16-20 suffices | Compute g at N=8, 12, 16, 20 and extrapolate |

## Anti-Approaches

| Anti-Approach | Why Avoid | What to Do Instead |
|---------------|-----------|-------------------|
| Using scipy.linalg.logm for Fisher metric | Fails for rank-deficient rho; produces -inf eigenvalues; numerically catastrophic | Eigendecomposition-based SLD formula (Algorithm 1) |
| Automatic differentiation of rho(theta) | Over-engineering for a problem where theta is a discrete lattice index and finite differences are exact to O(epsilon^2) | Central finite differences on partial traces |
| Monte Carlo sampling for correlations | ED gives exact correlators; MC introduces statistical noise for no benefit at N <= 20 | Direct computation from |psi> |
| Computing Fisher metric on FULL state rho (not reduced) | Full state is pure (|psi><psi|), so its Fisher metric is the Fubini-Study metric on projective Hilbert space -- not what we want. We need the REDUCED state metric. | Always work with partial-traced rho_Lambda |
| Using very large |Lambda| (|Lambda| > N/2) | Reduced state approaches purity; Fisher metric degenerates; purification has trivial geometry | Keep |Lambda| <= N/3; primary analysis at |Lambda| = 2-4 |
| Ignoring the PBC/OBC distinction | PBC gives trivially constant metric (by translation symmetry); OBC boundary effects contaminate small systems | Use OBC for physics, PBC as a symmetry check; report both |

## Logical Dependencies

```
Existing ED infrastructure (ed_entanglement.py)
  -> Ground state |psi> of SWAP/Heisenberg Hamiltonian
  -> partial_trace -> family of reduced density matrices rho_Lambda(x)

rho_Lambda(x) family -> eigendecomposition -> {lambda_m, |m>} at each x
  -> finite differences of rho -> d_rho_i
  -> SLD formula -> QFIM g_{ij}(x) at each x

g_{ij}(x) at all lattice points
  -> eigenvalue check -> positive-definiteness verification
  -> discrete second derivatives -> smoothness verification
  -> Dijkstra on weighted graph -> geodesic distances
  -> comparison with lattice distances -> distance recovery test

Ground state |psi> -> two-point correlators -> C(r)
  -> exponential fit -> correlation length xi
  -> comparison with Fisher metric length scale

CROSS-VALIDATION:
  SLD-based g_{ij} must equal (4x) fidelity-based Bures metric g_{ij}^B
  This is an internal consistency check with no approximation.
```

## Recommended Investigation Scope

Prioritize:
1. **Fisher metric computation module** (Algorithm 1 + integration with existing ED code) -- this is the core deliverable enabling all downstream analyses
2. **Correlation function computation** (Algorithm 4) -- needed independently for exponential decay verification
3. **Positive-definiteness and distance recovery** (Algorithms 5, 6) -- the two key claims to validate numerically

Defer:
- **2D geodesics:** First establish the method in 1D. 2D adds complexity (2x2 metric, Christoffel symbols) without new algorithmic challenges.
- **N=20 runs:** Develop and validate at N=8-16 first. N=20 is a final confirmation, not a development platform.
- **Smooth interpolation of g between lattice points:** Not needed unless the lattice-distance comparison fails at leading order.

## Validation Strategy

| Result | Validation Method | Benchmark | Source |
|--------|------------------|-----------|--------|
| QFIM eigendecomposition formula | Compare with fidelity-based Bures metric | g^{SLD} = 4 * g^{Bures} to machine precision | Braunstein-Caves (1994), Zanardi et al. (2007) |
| QFIM on pure state | Reduce to Fubini-Study metric | For pure rho = |psi><psi|, g_{ij} = 4(Re<d_i psi|d_j psi> - <d_i psi|psi><psi|d_j psi>) | Provost-Vallee CMP 76 (1980) |
| PBC translation invariance | g_{ij}(x) constant for all x on PBC lattice | std(g) / mean(g) < 1e-10 | Translation symmetry |
| Two-site (N=4) analytic check | Compute Fisher metric analytically for 2-site Heisenberg, compare to numerics | Exact agreement to machine precision | Direct calculation |
| Correlation function (1D Heisenberg) | Compare C(r) to Bethe ansatz exact results for N -> infinity | Power-law C(r) ~ (-1)^r / r (no exponential) | Bethe ansatz, Korepin et al. |
| Geodesic distance proportional to lattice distance | ratio = d_g / d_lattice approximately constant in bulk | std(ratio)/mean(ratio) < 0.1 for N >= 16 | This is the CLAIM to verify |
| Positive-definiteness | All eigenvalues of g > 0 in bulk | lambda_min > 0 by a margin independent of N | This is the CLAIM to verify |

## Sources

- Braunstein and Caves, "Statistical Distance and the Geometry of Quantum States," PRL 72, 3439 (1994) -- Foundation for quantum Fisher metric on state manifolds
- Zanardi, Giorda, Cozzini, "Information-Theoretic Differential Geometry of Quantum Phase Transitions," PRL 99, 100603 (2007). arXiv:quant-ph/0701061 -- Fisher/Bures metric on Hamiltonian parameter manifolds; fidelity susceptibility at QPTs
- Zanardi, Campos Venuti, Giorda, "Bures metric over thermal state manifolds and quantum criticality," PRA 76, 062318 (2007) -- Bures metric tensor for thermal states; analytical results for quantum Ising model
- Provost and Vallee, "Riemannian Structure on Manifolds of Quantum States," CMP 76, 289 (1980) -- Original definition of the quantum metric tensor (real part = Provost-Vallee metric)
- Liu, Jing, Yuan, "Quantum Fisher information matrix and multiparameter estimation," J. Phys. A 53, 023001 (2020). arXiv:1907.08037 -- Comprehensive review of QFIM computation methods including eigendecomposition, Lyapunov equation, and connections to fidelity
- Gu, "Fidelity approach to quantum phase transitions," Int. J. Mod. Phys. B 24, 4371 (2010). arXiv:0811.3127 -- Review of fidelity susceptibility as a probe of quantum phase transitions with numerical methods
- Albuquerque et al., "Quantum critical scaling of fidelity susceptibility," PRB 81, 064418 (2010). arXiv:0912.2689 -- Finite-size scaling of fidelity susceptibility in lattice models with QMC
- Zhang et al., "QuanEstimation: An open-source toolkit for quantum parameter estimation," Phys. Rev. Research 4, 043057 (2022). arXiv:2205.15588 -- Reference implementation of QFIM computation (Python/Julia); useful for cross-validation if needed
- Al-Mohy and Higham, "Improved Inverse Scaling and Squaring Algorithms for the Matrix Logarithm," SIAM J. Sci. Comput. 34, C153 (2012) -- Algorithm behind scipy.linalg.logm (explains why it fails for singular matrices)
- Existing project code: `code/ed_entanglement.py` (Hamiltonian construction, Lanczos, partial trace, entropy)
- Existing project code: `code/area_law_verification.py` (area-law fits, 1D/2D, output format)
- Existing project code: `code/self_modeling_hamiltonian.py` (SWAP operator construction, verification)
