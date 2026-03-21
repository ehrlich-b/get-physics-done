# Computational Approaches: GR from Self-Modeling Locality

**Surveyed:** 2026-03-21
**Domain:** Quantum foundations / quantum gravity / entanglement entropy / thermodynamic gravity
**Confidence:** MEDIUM

### Scope Boundary

COMPUTATIONAL.md covers computational TOOLS, libraries, and infrastructure for the v3.0 GR extension. It does NOT cover physics methods (METHODS.md) or the theoretical landscape (PRIOR-WORK.md). Focus: what software, algorithms, and numerical checks support the proof-driven derivation of GR from self-modeling locality.

## Recommended Stack

The v3.0 milestone is primarily proof work, not heavy numerics. The computational role is **verification and illustration**: small-scale numerical checks that confirm (or falsify) the area-law entanglement scaling for self-modeling lattices, and that validate intermediate steps in the Jacobson argument. The recommended stack extends v2.0's Python/SymPy base with targeted additions for entanglement entropy computation on small lattices.

**Primary approach:** Exact diagonalization of small lattice systems (up to ~16 qubits / 8 sites of M_2(C)^sa) using NumPy/SciPy, with QuTiP for entanglement entropy and partial trace convenience functions. Tensor network methods (TeNPy/DMRG) are available as a reach tool for larger 1D systems but are unlikely to be needed given the proof-driven nature of the work.

**Architecture:** Build a lightweight Python module that constructs a lattice of M_n(C)^sa systems with nearest-neighbor coupling, computes ground states via exact diagonalization, and extracts entanglement entropy for subregions of varying size to check area vs. volume scaling.

## Numerical Algorithms

### 1. Entanglement Entropy via Exact Diagonalization

| Algorithm | Problem | Convergence | Cost per Step | Memory | Key Reference |
|-----------|---------|-------------|---------------|--------|---------------|
| Full ED + partial trace | S(A) for subregion A of lattice | Exact | O(d^{2N}) for N sites, local dim d | O(d^N) for state vector | Laflorencie, Phys. Rep. 646, 1 (2016) |
| Lanczos + partial trace | Ground state S(A) only | O(1/k) for k Lanczos steps | O(k * d^N) | O(d^N) for state + k Lanczos vectors | Lehoucq et al., ARPACK Users' Guide |
| Swap trick (Renyi-2) | S_2(A) = -ln Tr(rho_A^2) | Exact for given state | O(d^N) | O(d^N) | Hastings et al., PRL 104, 157201 (2010) |

#### Algorithm: Computing S(A) for a Subregion

```
INPUT:  Hamiltonian H on lattice of N sites, each with local dim d
        Subregion A (subset of sites)
OUTPUT: von Neumann entropy S(A)

1. Find ground state |psi> of H
   - If N*log2(d) <= 16: full diagonalization via numpy.linalg.eigh
   - If N*log2(d) <= 24: Lanczos via scipy.sparse.linalg.eigsh
   - If N*log2(d) > 24: tensor network (TeNPy DMRG) or out of scope

2. Form density matrix rho = |psi><psi|
   - For pure state: store |psi> as vector, compute rho_A directly

3. Compute reduced density matrix rho_A = Tr_Abar(rho)
   - Reshape |psi> as tensor with shape (d_A, d_Abar)
     where d_A = d^|A|, d_Abar = d^(N-|A|)
   - rho_A = sum_j <j_Abar|psi><psi|j_Abar> (partial trace)
   - Efficient: rho_A = psi_reshaped @ psi_reshaped.conj().T

4. Compute S(A) = -Tr(rho_A ln rho_A)
   - Eigendecompose rho_A: eigenvalues {lambda_i}
   - S(A) = -sum_i lambda_i * ln(lambda_i) for lambda_i > 0
   - Use threshold lambda_i > 1e-14 to avoid log(0)
```

#### Convergence Properties

- **Full ED:** Exact to machine precision. No convergence issue. Limited by memory: d^N doubles of storage for state vector. For M_2(C)^sa (d=2 per site), N=16 sites requires 2^16 = 65536 complex numbers = 1 MB. N=20 requires 2^20 = ~8 MB. N=24 requires ~128 MB. N=28 is borderline at ~2 GB.
- **Lanczos:** Converges to ground state exponentially fast in number of iterations when gap is O(1). Typically 50-200 iterations suffice. Convergence criterion: |E_k - E_{k-1}|/|E_k| < 1e-12. Fails when gap is exponentially small.
- **Partial trace:** Exact reshaping operation. No numerical error beyond machine precision.
- **Entropy from eigenvalues:** Numerically stable if eigenvalues are computed via symmetric eigendecomposition (which is backward stable). Catastrophic cancellation possible if rho_A has eigenvalues very close to 0 or 1; mitigated by the threshold cutoff.

### 2. Area-Law Scaling Verification

| Algorithm | Problem | Convergence | Cost per Step | Memory | Key Reference |
|-----------|---------|-------------|---------------|--------|---------------|
| Systematic subregion sweep | S(A) vs |boundary(A)| and |A| | N/A (data analysis) | Per subregion: O(d^N) | O(d^N) | Eisert et al., RMP 82, 277 (2010) |
| Linear regression | Fit S = alpha * |boundary| + beta vs S = gamma * |volume| + delta | Standard R^2 | O(number of data points) | Negligible | Standard statistics |

#### Algorithm: Area vs. Volume Law Check

```
INPUT:  Lattice of N sites in d_spatial dimensions with local dim d
        Hamiltonian H with nearest-neighbor interactions
OUTPUT: Scaling coefficient and R^2 for area-law and volume-law fits

1. Compute ground state |psi> of H (as above)

2. For each connected subregion A of size |A| = 1, 2, ..., N/2:
   a. Compute S(A) via partial trace + eigendecomposition
   b. Record |A| (volume), |boundary(A)| (number of boundary links)

3. Fit two models:
   - Area law:   S(A) = alpha * |boundary(A)| + c_area
   - Volume law: S(A) = gamma * |A| + c_vol

4. Compare R^2 values. Area law should win for gapped ground states.

5. For 1D chains: |boundary(A)| = 2 (constant for interior cuts)
   -> Area law predicts S(A) = const, independent of |A|
   -> Volume law predicts S(A) ~ |A|
   This is the clearest test.
```

#### Feasible Lattice Sizes

| Geometry | Sites N | Local dim d | Hilbert space dim | Memory (state) | Feasibility |
|----------|---------|-------------|-------------------|----------------|-------------|
| 1D chain | 16 | 2 (qubit) | 65,536 | 1 MB | Easy |
| 1D chain | 20 | 2 | 1,048,576 | 8 MB | Easy |
| 1D chain | 24 | 2 | 16,777,216 | 128 MB | Moderate |
| 2D square | 4x4 | 2 | 65,536 | 1 MB | Easy |
| 2D square | 4x5 | 2 | 1,048,576 | 8 MB | Easy |
| 2D square | 5x5 | 2 | 33,554,432 | 256 MB | Moderate |
| 1D chain | 8 | 4 (M_2(C)^sa) | 65,536 | 1 MB | Easy |
| 1D chain | 10 | 4 | 1,048,576 | 8 MB | Easy |
| 1D chain | 12 | 4 | 16,777,216 | 128 MB | Moderate |
| 2D square | 3x3 | 4 | 262,144 | 2 MB | Easy |
| 2D square | 4x3 | 4 | 16,777,216 | 128 MB | Moderate |

**Recommendation:** Use d=2 (qubit) systems for initial area-law verification (simpler Hamiltonian, same scaling physics). Then d=4 for M_2(C)^sa-specific checks. The 1D chain with N=16-20 qubits and the 2D 4x4 lattice are the sweet spots: large enough to see scaling, small enough for exact diagonalization on a laptop.

### 3. Fisher Information Metric on Lattice

| Algorithm | Problem | Convergence | Cost per Step | Memory | Key Reference |
|-----------|---------|-------------|---------------|--------|---------------|
| Numerical differentiation of state | g_ij = Re Tr(d_i rho * d_j ln rho) | O(epsilon^2) for step epsilon | O(d^{2N} * p^2) for p parameters | O(d^N) | Paris, Int. J. Quant. Inf. 7, 125 (2009) |
| SLD Fisher info | g_ij via symmetric logarithmic derivative | Exact (solve Lyapunov eq) | O(d^{3N}) per matrix equation | O(d^{2N}) | Braunstein & Caves, PRL 72, 3439 (1994) |

#### Algorithm: Fisher Information Metric from Parameterized States

```
INPUT:  Family of states rho(theta) parameterized by theta = (theta_1, ..., theta_p)
        (e.g., theta_i = coupling strength at site i)
OUTPUT: Fisher information matrix g_ij(theta)

1. For each parameter theta_i:
   a. Compute rho(theta + epsilon * e_i) and rho(theta - epsilon * e_i)
   b. d_i(rho) = (rho(theta + eps*e_i) - rho(theta - eps*e_i)) / (2*epsilon)

2. For each pair (i,j):
   a. Solve the SLD equation: d_i(rho) = (L_i * rho + rho * L_i) / 2
      - This is a Lyapunov equation; solve via vectorization:
        (I tensor rho + rho tensor I) vec(L_i) = 2 * vec(d_i(rho))
   b. g_ij = (1/2) * Tr(rho * (L_i * L_j + L_j * L_i))

Alternative (simpler, for pure states rho = |psi><psi|):
   g_ij = 4 * Re(<d_i psi | d_j psi> - <d_i psi|psi><psi|d_j psi>)
   (Fubini-Study metric on projective Hilbert space)
```

**Relevance to emergent geometry:** The Fisher information metric on the parameter space of local coupling constants defines a Riemannian geometry. If the parameters are identified with spatial coordinates, this metric IS the emergent spatial metric. Cao-Carroll-Michalakis (2017) use mutual information instead, but the Fisher metric approach is more directly geometric.

**Practical note:** For the v3.0 project, the Fisher metric computation is a bonus (Step 4 in GR_EXTENSION.md). Prioritize entanglement entropy calculations first.

### 4. Mutual Information as Emergent Distance (Cao-Carroll-Michalakis approach)

| Algorithm | Problem | Convergence | Cost per Step | Memory | Key Reference |
|-----------|---------|-------------|---------------|--------|---------------|
| Pairwise mutual information | I(i:j) = S(i) + S(j) - S(i,j) for all site pairs | Exact (given state) | O(N^2 * d^N) for N site pairs | O(d^N) | Cao, Carroll, Michalakis, PRD 95, 024031 (2017) |
| Classical MDS | Embed distance matrix into R^k | Exact for given dimension k | O(N^3) for eigendecomposition | O(N^2) | Borg & Groenen, Modern MDS (2005) |

#### Algorithm: Emergent Geometry from Entanglement

```
INPUT:  Ground state |psi> on lattice of N sites
OUTPUT: Emergent spatial geometry (distance matrix + embedding dimension)

1. For each pair of sites (i,j):
   a. Compute S(i) = -Tr(rho_i ln rho_i)
   b. Compute S(j) = -Tr(rho_j ln rho_j)
   c. Compute S(i,j) = -Tr(rho_{ij} ln rho_{ij})
   d. I(i:j) = S(i) + S(j) - S(i,j)

2. Define distance: d(i,j) = f(I(i:j))
   - Cao-Carroll-Michalakis use d(i,j) ~ 1/I(i:j)
   - Must verify triangle inequality

3. Classical multidimensional scaling on distance matrix:
   a. Double-center the squared distance matrix
   b. Eigendecompose: largest eigenvalues give embedding coordinates
   c. Number of significant eigenvalues = emergent spatial dimension

4. Compare emergent geometry to input lattice geometry
```

**This is the key numerical check for Step 4 (emergent geometry).** For a 1D chain with local interactions, the mutual information should decay exponentially with lattice distance, and MDS should recover a 1D embedding. For a 2D lattice, MDS should recover 2D. This is a powerful consistency check.

## Software Ecosystem

### Primary Tools

| Tool | Version | Purpose | License | Maturity |
|------|---------|---------|---------|----------|
| NumPy | >= 1.26 | Dense linear algebra, state vectors, eigendecomposition | BSD | Stable |
| SciPy | >= 1.12 | Sparse eigensolvers (Lanczos), matrix functions | BSD | Stable |
| SymPy | >= 1.13 | Symbolic verification of algebraic identities (carries from v2.0) | BSD | Stable |
| QuTiP | >= 5.0 | Partial trace, entropy functions, tensor product states | BSD | Stable |

### Supporting Tools

| Tool | Version | Purpose | When Needed |
|------|---------|---------|-------------|
| TeNPy | >= 1.0 | DMRG for 1D systems beyond ED reach (N > 24 qubits) | Only if 1D area-law check needs larger systems |
| QuSpin | >= 1.0 | ED with symmetry sectors for spin chains | If symmetry-exploiting ED needed for larger lattices |
| scikit-learn | >= 1.4 | Classical MDS for emergent geometry embedding | For Step 4 (emergent geometry) only |
| Matplotlib | >= 3.8 | Plotting S(A) vs |boundary(A)|, emergent geometry visualization | For figures in paper |

### Why These Tools

**QuTiP over hand-rolled partial trace:** QuTiP's `Qobj.ptrace()` handles arbitrary tensor product structures correctly, including non-contiguous subsystems. Hand-rolling partial traces on general subsystem decompositions is error-prone. QuTiP also provides `entropy_vn()`, `entropy_mutual()`, and `concurrence()` as validated black-box functions. The v3.0 work involves many partial trace operations on different subregions; QuTiP's convenience functions save development time and reduce bugs.

**NumPy/SciPy over QuTiP for the Hamiltonian:** QuTiP's Hamiltonian construction is oriented toward open quantum systems dynamics (Lindblad, Monte Carlo). For static ground-state problems on lattices, constructing the Hamiltonian directly as a sparse SciPy matrix and using `scipy.sparse.linalg.eigsh` (ARPACK-based Lanczos) is more direct and efficient. Use QuTiP only for the entanglement entropy extraction step.

**TeNPy as reach tool, not primary:** TeNPy's DMRG is the standard tool for 1D entanglement entropy in large systems. But our lattice sizes (N <= 20 qubits for ED) are sufficient to demonstrate area-law scaling in 1D. DMRG would be needed only if we want to push to N=100+ sites for a convincing scaling plot, which is a nice-to-have, not essential for a proof-driven paper.

**QuSpin as alternative ED:** QuSpin handles symmetry-reduced exact diagonalization efficiently for spin chains (translation, parity, spin-flip symmetries). If the self-modeling Hamiltonian has symmetries that reduce the Hilbert space, QuSpin can push ED to larger systems. But the self-modeling interaction structure may not have standard symmetries, making QuSpin's advantage marginal.

### Why NOT Other Tools

| Tool | Why Skip |
|------|----------|
| ITensor (C++/Julia) | Excellent for production tensor network calculations, but requires Julia or C++. Project is Python-native. TeNPy covers the same ground in Python. |
| Qiskit / Cirq | Quantum circuit simulators. Our problem is static ground-state computation, not circuit simulation. Wrong abstraction. |
| DMRG++ (C++) | High-performance DMRG code. Overkill for our small-lattice verification needs. |
| PETSc/SLEPc | Industrial sparse eigensolvers. SciPy's ARPACK wrapper is sufficient for d^N <= 10^7. |
| Mathematica | Stronger symbolic engine than SymPy but not Python-native. v2.0 established SymPy as adequate. |

## Data Flow

```
Define self-modeling lattice Hamiltonian
  Parameters: n (local algebra dim), N (lattice size), J (coupling), geometry (1D/2D)
  -> Construct H as sparse matrix (scipy.sparse)
  -> Exact diagonalization: ground state |psi> (scipy.sparse.linalg.eigsh)
  -> For each subregion A of size |A| = 1, ..., N/2:
     -> Partial trace: rho_A = Tr_Abar(|psi><psi|) (QuTiP ptrace or manual reshape)
     -> Von Neumann entropy: S(A) = -Tr(rho_A ln rho_A) (QuTiP entropy_vn)
     -> Record (|A|, |boundary(A)|, S(A))
  -> Fit S(A) vs |boundary(A)| (area law) and S(A) vs |A| (volume law)
  -> Report R^2 values, scaling coefficients

Bonus: Emergent geometry
  -> Compute pairwise mutual information I(i:j) for all site pairs
  -> Classical MDS on 1/I distance matrix (scikit-learn MDS)
  -> Report embedding dimension, compare to lattice geometry
```

## Computation Order and Dependencies

| Step | Depends On | Produces | Can Parallelize? |
|------|-----------|----------|-----------------|
| 1. Define self-modeling Hamiltonian | Locality formalization (Phase 1 proof work) | H as sparse matrix | No (needs math first) |
| 2. Benchmark on standard models (Heisenberg, transverse Ising) | Nothing | Verified area-law checker | Yes (known results) |
| 3. Ground state computation | Step 1 (or 2 for benchmarks) | Ground state vector |psi> | Yes per model |
| 4. Subregion entropy sweep | Step 3 | S(A) vs |A| and |boundary(A)| data | Yes (subregions independent given |psi>) |
| 5. Area vs volume law fit | Step 4 | Scaling exponent, R^2 | No (needs all data) |
| 6. Pairwise mutual information | Step 3 | I(i:j) matrix | Yes (site pairs independent) |
| 7. MDS embedding | Step 6 | Emergent geometry | No (needs full I matrix) |
| 8. Fisher information metric | Step 3 + parameterized family | g_ij metric tensor | Yes per parameter pair |

**Critical path:** Steps 1 -> 3 -> 4 -> 5. This is the area-law check.
**Bonus path:** Steps 3 -> 6 -> 7 (emergent geometry) and Steps 3 -> 8 (Fisher metric).

## Resource Estimates

| Computation | Time (estimate) | Memory | Storage | Hardware |
|-------------|-----------------|--------|---------|----------|
| ED ground state, 16-qubit 1D chain | < 1 second | 1 MB | Negligible | Local CPU |
| ED ground state, 20-qubit 1D chain | < 10 seconds | 8 MB | Negligible | Local CPU |
| ED ground state, 24-qubit 1D chain | 1-10 minutes | 128 MB | Negligible | Local CPU |
| ED ground state, 4x4 qubit lattice (2D) | < 1 second | 1 MB | Negligible | Local CPU |
| ED ground state, 5x5 qubit lattice (2D) | ~30 minutes | 256 MB | Negligible | Local CPU |
| Subregion entropy sweep (all cuts, 16 sites) | < 1 minute | 1 MB | Negligible | Local CPU |
| Subregion entropy sweep (all cuts, 20 sites) | < 10 minutes | 8 MB | Negligible | Local CPU |
| Pairwise mutual info (16 sites) | < 5 minutes | 1 MB | Negligible | Local CPU |
| Fisher info metric (8 sites, 8 params) | < 30 minutes | 1 MB | Negligible | Local CPU |
| DMRG 1D chain (100 sites, chi=64) | < 5 minutes | 100 MB | Negligible | Local CPU |

All computation is local laptop-scale. No HPC, no GPU, no cluster needed.

## Integration with Existing Code

### v2.0 Codebase

The v2.0 computational work was algebraic structure verification (sequential product axioms, Jordan algebra checks) using SymPy. The v3.0 work is numerically different: ground-state physics and entanglement entropy on lattices. There is no code reuse from v2.0 beyond the Python environment.

**However:** The M_n(C)^sa algebra construction from v2.0 provides the local algebra at each lattice site. The self-modeling sequential product (Luders product sqrt(a) b sqrt(a)) from v2.0 may inform the interaction Hamiltonian construction.

### Interface Points

- **Input from v2.0:** M_n(C)^sa structure at each site (n=2 gives qubits). Local tomography result determines tensor product structure.
- **Input from Phase 1 (v3.0):** Formal definition of "local self-modeling interaction" determines the Hamiltonian. This is the critical dependency -- no computation can start until the Hamiltonian is defined.
- **Output to Phase 2 (v3.0):** Area-law scaling data {S(A), |A|, |boundary(A)|} to support or refute the area-law argument.
- **Output to Phase 3 (v3.0):** Emergent geometry data (mutual information matrix, MDS embedding) to support the Jacobson application.

### What Must Be Built

1. **Lattice Hamiltonian constructor:** Takes lattice geometry (1D chain, 2D square, etc.), local dimension n, and coupling type. Outputs sparse Hamiltonian matrix. ~100 lines of Python.
2. **Entanglement entropy scanner:** Takes ground state and subregion specification. Outputs S(A). Wraps QuTiP's ptrace and entropy_vn. ~50 lines.
3. **Area-law checker:** Takes entropy data, fits area and volume models, reports R^2. ~30 lines.
4. **Mutual information computer:** Takes ground state, computes I(i:j) for all pairs. ~40 lines.
5. **Benchmark suite:** Verifies area-law checker against known results (Heisenberg chain, transverse Ising at and away from criticality). ~100 lines.

Total new code: ~300-400 lines of Python. This is a weekend of work, not a software project.

## Discretizing Jacobson's Argument

### State of the Art

No published discrete lattice version of Jacobson's full thermodynamic argument exists. Jacobson's original 1995 derivation and his 2016 "Entanglement Equilibrium" reformulation both operate in the continuum, requiring:

1. **Rindler horizons:** Local causal horizons through each spacetime point. On a lattice, there is no continuous notion of "local causal horizon." The nearest analogue is a bipartition boundary -- but this lacks the boost Killing vector structure.

2. **Boost Killing vector:** The generator of Lorentz boosts that preserves the Rindler horizon. On a lattice, there is no continuous symmetry group. Possible discrete analogues: modular Hamiltonian K = -ln(rho_A) generates "modular flow" (Tomita-Takesaki theory), which is the algebraic analogue of geometric boosts.

3. **Raychaudhuri equation:** Governs focusing of null geodesic congruences. No lattice analogue exists. The Raychaudhuri equation is intrinsically a continuum differential geometry statement.

4. **Unruh temperature:** T = a/(2pi) for acceleration a. On a lattice with finite degrees of freedom, the Unruh effect requires a continuum limit or an analogue construction.

### What Can Be Computed

The Cao-Carroll-Michalakis approach (PRD 95, 024031, 2017) bypasses these continuum structures entirely. Their route:
- Start with a finite-dimensional Hilbert space (no continuum needed)
- Define geometry from entanglement (mutual information as distance)
- Show that entanglement perturbations obey a spatial analogue of Einstein's equation
- The "spatial Einstein equation" emerges from entanglement first law: delta S = delta <K>

This is more natural for our lattice setting than trying to discretize Jacobson's continuum argument directly.

Jacobson's 2016 "Entanglement Equilibrium" paper (PRL 116, 201101) provides a bridge: Einstein's equations follow from the hypothesis that entanglement entropy in small geodesic balls is maximized in vacuum. This is closer to a lattice-friendly formulation because it's about entropy of subregions, which we can compute directly.

### Computational Checks

| Check | What to Compute | Expected Result | Feasibility |
|-------|----------------|-----------------|-------------|
| Entanglement first law | delta S(A) vs delta <K_A> for small perturbations | delta S = delta <K> | Feasible: exact for small lattices |
| Modular Hamiltonian | K_A = -ln(rho_A) | Should generate "modular flow" | Feasible: direct computation from rho_A |
| Entanglement equilibrium | Is vacuum S(A) maximal at fixed |A|? | Yes for area-law states | Feasible: compare S(A) across state families |

## Open Questions

| Question | Why Open | Impact on Project | Approaches Being Tried |
|----------|---------|-------------------|----------------------|
| What Hamiltonian encodes self-modeling locality? | Self-modeling is an operational/algebraic concept; translating to a Hamiltonian is nontrivial | Blocks all numerical computation until resolved | Phase 1 formalization; may need to define the Hamiltonian axiomatically |
| Does the self-modeling ground state have a spectral gap? | Hastings' area law requires a gap; without it, area law is not guaranteed | Could invalidate the Hastings route to area law | Check numerically for small lattices; may need information-theoretic argument instead |
| Can Jacobson's argument work on a lattice without continuum limit? | Rindler horizons, boost Killing vectors, Raychaudhuri equation are continuum structures | If no: need continuum limit argument; if yes: direct lattice derivation | Cao-Carroll-Michalakis approach bypasses continuum structures |
| What is the right coupling for M_n(C)^sa neighbors? | Many possible nearest-neighbor interactions; self-modeling constrains but may not determine uniquely | Different couplings give different ground states and possibly different entropy scaling | Derive from self-modeling update map; test several candidates numerically |

## Anti-Approaches

| Anti-Approach | Why Avoid | What to Do Instead |
|---------------|-----------|-------------------|
| Large-scale tensor network simulation | This is a proof project, not a condensed matter simulation. Spending weeks optimizing DMRG for large lattices adds nothing to the theoretical argument. | Exact diagonalization on small lattices (N <= 20 qubits). The point is to CHECK the area law, not to compute it with maximum precision. |
| Discretizing the Raychaudhuri equation | No clean lattice analogue exists. Attempting to define null geodesic focusing on a graph is a research program, not a verification step. | Use the Cao-Carroll-Michalakis or Jacobson entanglement equilibrium formulations that work with subregion entropies directly. |
| Quantum circuit simulation | The problem is static ground-state entanglement, not quantum dynamics or quantum computing. Qiskit/Cirq are wrong tools. | SciPy sparse eigensolvers for ground states. |
| Monte Carlo for entanglement entropy | QMC methods for Renyi entropy (replica trick) are powerful but complex to implement and require careful thermalization. | Exact diagonalization is sufficient at our lattice sizes and gives von Neumann entropy directly. |
| Trying to derive Newton's constant G | Out of scope per PROJECT.md. The thermodynamic argument gives Einstein's equations with G as an undetermined proportionality constant (G = 1/(4*eta) where eta is the entropy-area proportionality). | Accept G as a free parameter. The derivation's value is the FORM of the equations, not the constant. |

## Logical Dependencies

```
Paper 5 results (M_n(C)^sa, local tomography, Luders product)
  -> Lattice site algebra (each site is M_n(C)^sa)
  -> Tensor product structure for multi-site system (from local tomography)

Phase 1: Locality formalization
  -> Self-modeling interaction Hamiltonian H
  -> Blocks: all numerical ground-state computations

Phase 2: Area-law argument
  -> Numerical check: S(A) vs |boundary(A)| for self-modeling lattice
  -> Requires: ground state of H from Phase 1

Phase 3: Jacobson application
  -> Numerical check: entanglement first law delta S = delta <K>
  -> Numerical check: entanglement equilibrium (S maximized in vacuum)
  -> Requires: area-law confirmation from Phase 2

Phase 4 (bonus): Emergent geometry
  -> Numerical check: MDS embedding recovers lattice dimension
  -> Requires: ground state from Phase 1
  -> Independent of Phases 2-3 (can parallelize)

Benchmark computations (Heisenberg chain, transverse Ising)
  -> Validates computational infrastructure
  -> Independent of all phases (do first)
```

## Recommended Investigation Scope

Prioritize:
1. **Benchmark area-law checker on known models** -- Heisenberg chain (gapped: S = const) and critical transverse Ising (S ~ (c/3) ln L) as positive and negative controls. This validates infrastructure before applying to the novel self-modeling Hamiltonian.
2. **Compute S(A) for self-modeling lattice** -- Once Phase 1 provides the Hamiltonian. Check area vs. volume scaling for 1D chains (N=8-20) and 2D lattices (4x4, 3x4) with M_2(C)^sa local algebras.
3. **Entanglement first law check** -- Verify delta S(A) = delta <K_A> for small perturbations of the ground state. This is the key input to the Jacobson/entanglement-equilibrium argument.

Defer:
- **Emergent geometry via MDS:** Nice result but not on the critical path for the area-law -> Einstein equation chain. Do after the core argument is established.
- **Fisher information metric:** Requires a parameterized family of states and is the most computationally expensive calculation. Only relevant for Step 4 (bonus).
- **Large-scale DMRG computations:** Only if small-lattice ED results are inconclusive about scaling behavior.

## Validation Strategy

| Result | Validation Method | Benchmark | Source |
|--------|------------------|-----------|--------|
| Area-law checker correctness | Heisenberg chain (gapped, Delta > 1) | S(A) = const for interior bipartitions | Hastings (2007), arXiv:0705.2024 |
| Area-law checker correctness | Critical transverse Ising chain (gapless) | S(A) ~ (c/6) ln L with c=1/2 | Calabrese & Cardy, JSTAT P06002 (2004) |
| Volume-law detection | Random state entropy | S(A) ~ |A| * ln(d) - 1/2 | Page, PRL 71, 1291 (1993) |
| Partial trace implementation | Bell state rho_A | S(A) = ln(2) for maximally entangled pair | Textbook |
| Mutual information | Product state | I(i:j) = 0 for all pairs | Definition |
| Mutual information | GHZ state | I(i:j) > 0 for all pairs, equal by symmetry | Known result |
| Entanglement first law | Perturbed ground state | delta S = delta <K> to O(delta^2) | Blanco et al., JHEP 01, 130 (2013) |

## Installation / Setup

```bash
# Core stack (extends v2.0 environment)
pip install numpy scipy sympy matplotlib

# Entanglement entropy computation (NEW for v3.0)
pip install qutip

# Optional: larger-scale tensor networks (only if needed)
pip install physics-tenpy

# Optional: symmetry-exploiting ED (only if needed)
pip install quspin

# Optional: MDS for emergent geometry (only if needed)
pip install scikit-learn
```

**Note:** QuTiP v5 (current) requires Python >= 3.10. TeNPy v1 requires Python >= 3.9. Both are compatible with the existing v2.0 environment.

**Do NOT install** without user confirmation per shared-protocols.md.

## Concrete Implementation Sketch

### Benchmark: Heisenberg Chain Area Law

```python
import numpy as np
from scipy.sparse import kron, eye
from scipy.sparse.linalg import eigsh

def heisenberg_chain(N):
    """Construct Heisenberg XXX Hamiltonian on N-site chain."""
    d = 2  # qubit
    # Pauli matrices
    sx = np.array([[0, 1], [1, 0]], dtype=complex) / 2
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex) / 2
    sz = np.array([[1, 0], [0, -1]], dtype=complex) / 2
    I2 = eye(2, format='csr')

    H = None
    for i in range(N - 1):
        # S_i . S_{i+1} = sx_i sx_{i+1} + sy_i sy_{i+1} + sz_i sz_{i+1}
        for S in [sx, sy, sz]:
            term = eye(1, format='csr')
            for j in range(N):
                if j == i:
                    term = kron(term, S, format='csr')
                elif j == i + 1:
                    term = kron(term, S, format='csr')
                else:
                    term = kron(term, I2, format='csr')
            H = term if H is None else H + term
    return H

def entanglement_entropy(psi, N, subsys_size):
    """Compute von Neumann entropy S(A) for first subsys_size sites."""
    d = 2
    d_A = d ** subsys_size
    d_B = d ** (N - subsys_size)
    psi_matrix = psi.reshape(d_A, d_B)
    rho_A = psi_matrix @ psi_matrix.conj().T
    eigenvalues = np.linalg.eigvalsh(rho_A)
    eigenvalues = eigenvalues[eigenvalues > 1e-14]
    return -np.sum(eigenvalues * np.log(eigenvalues))

# Example: N=12 Heisenberg chain
N = 12
H = heisenberg_chain(N)
E, psi = eigsh(H, k=1, which='SA')
psi = psi[:, 0]

# Sweep subregion size
for L in range(1, N // 2 + 1):
    S = entanglement_entropy(psi, N, L)
    print(f"|A|={L}, S(A)={S:.4f}")
# Expected: S(A) roughly constant for L >= 2 (area law in 1D)
```

This benchmark should be the FIRST computation run, before any self-modeling-specific work. It validates the entire toolchain.

## Key References

- Eisert, Cramer, Plenio (2010), "Colloquium: Area laws for the entanglement entropy," RMP 82, 277, arXiv:0808.3773 -- Comprehensive review of area laws; Section III covers numerical methods
- Hastings (2007), "An area law for one-dimensional quantum systems," JSTAT P08024, arXiv:0705.2024 -- Rigorous 1D area law proof; states conditions (gapped, local, finite-range)
- Calabrese, Cardy (2004), "Entanglement entropy and quantum field theory," JSTAT P06002, arXiv:hep-th/0405152 -- CFT formula S ~ (c/3) ln L for critical 1D systems; benchmark for gapless case
- Cao, Carroll, Michalakis (2017), "Space from Hilbert space," PRD 95, 024031, arXiv:1606.08444 -- Emergent geometry from entanglement in finite Hilbert spaces; closest existing framework
- Jacobson (1995), "Thermodynamics of Spacetime," PRL 75, 1260, arXiv:gr-qc/9504004 -- Original thermodynamic derivation of Einstein equations
- Jacobson (2016), "Entanglement Equilibrium and the Einstein Equation," PRL 116, 201101, arXiv:1505.04753 -- Reformulation via entanglement equilibrium in causal diamonds
- Blanco, Casini, Hung, Myers (2013), "Relative entropy and holography," JHEP 01, 130, arXiv:1305.3182 -- Entanglement first law: delta S = delta <K>
- Laflorencie (2016), "Quantum entanglement in condensed matter systems," Phys. Rep. 646, 1, arXiv:1512.03388 -- Review of numerical methods for entanglement entropy
- Page (1993), "Average entropy of a subsystem," PRL 71, 1291 -- Random state entropy: S ~ |A| ln(d) - d_A/(2 d_B); benchmark for volume law
- QuTiP documentation: https://qutip.org/docs/latest/ -- entropy_vn, ptrace, tensor operations
- TeNPy documentation: https://tenpy.readthedocs.io/en/latest/ -- DMRG, MPS, entanglement entropy
- QuSpin documentation: https://quspin.github.io/QuSpin/ -- ED with symmetries for spin chains

## Sources

- Eisert et al. (2010): [arXiv:0808.3773](https://arxiv.org/abs/0808.3773) -- Area law review with numerical methods survey
- Hastings (2007): [arXiv:0705.2024](https://arxiv.org/abs/0705.2024) -- 1D area law theorem conditions
- Cao, Carroll, Michalakis (2017): [arXiv:1606.08444](https://arxiv.org/abs/1606.08444) -- Emergent geometry algorithm (MDS from mutual information)
- Jacobson (2016): [arXiv:1505.04753](https://arxiv.org/abs/1505.04753) -- Entanglement equilibrium formulation
- TeNPy v1 paper: [arXiv:2408.02010](https://arxiv.org/abs/2408.02010) -- TeNPy version 1, August 2024
- QuTiP entropy module: [qutip.org](https://qutip.org/docs/4.0.2/modules/qutip/entropy.html) -- Verified 2026-03-21
- QuSpin: [SciPost Phys. 2, 003 (2017)](https://scipost.org/SciPostPhys.2.1.003) -- ED with symmetries
- Entanglement entropy bounds (2025): [Comm. Math. Phys.](https://link.springer.com/article/10.1007/s00220-025-05324-3) -- Recent area law conditional proofs for rapid decorrelation
- Bipartite reweight-annealing QMC (2025): [Nature Communications](https://www.nature.com/articles/s41467-025-61084-7) -- Large-scale Renyi entropy extraction
