# Phase 11: Numerical Verification - Research

**Researched:** 2026-03-22
**Domain:** Computational condensed matter / Exact diagonalization / Entanglement entropy / Quantum lattice systems
**Confidence:** HIGH

## Summary

Phase 11 provides numerical evidence for (or against) the theoretical results of Phases 8-10: area-law entanglement scaling on the self-modeling lattice, modular Hamiltonian locality, and a qualitative MVEH check. The self-modeling Hamiltonian H = sum JF_{xy} is identical to the isotropic Heisenberg model for n=2 (Phase 8 result), so benchmarking against known Heisenberg chain results is a direct test of numerical infrastructure -- NOT a separate model. The transverse-field Ising model provides a genuinely independent benchmark with known exact entanglement entropy values at and away from criticality.

The computational methods are entirely standard: exact diagonalization via sparse Lanczos (scipy.sparse.linalg.eigsh) for ground states of chains up to N=20-24 qubits, partial trace via tensor reshaping for reduced density matrices, and von Neumann entropy from eigenvalue spectra. Memory is the binding constraint: 2^N complex doubles for the state vector, so N=20 requires 8 MB (trivial), N=24 requires 128 MB (easy), and 2D 4x4 = 16 qubits requires 1 MB (trivial). No HPC is needed.

The key subtlety is the area-law vs volume-law regression methodology for small systems. In 1D, area law means S(A) = const for interior cuts (|boundary| = 2 always), while volume law means S(A) ~ |A|. So the test is whether S(L) saturates or grows linearly with subsystem size L. For the AFM Heisenberg chain (J>0), the ground state is critical with S ~ (1/3)ln(L) (c=1 CFT), which is neither strict area law nor volume law -- this is a known result, not a failure. The gapped transverse-field Ising model (h >> J) provides the clean area-law benchmark.

**Primary recommendation:** Build a single self-contained Python script using only numpy/scipy that: (1) benchmarks against known transverse-field Ising and Heisenberg chain entanglement entropies, (2) computes S(A) vs |A| and |boundary(A)| for the self-modeling lattice in 1D and 2D, (3) performs area-law vs volume-law linear regression with R^2 statistics, (4) computes the modular Hamiltonian K_A = -ln(rho_A) and checks locality of its matrix elements, and (5) performs a qualitative MVEH check via local perturbations. Use QuSpin only if symmetry exploitation is needed for larger systems; for the target sizes (N <= 20), raw scipy is sufficient and avoids a dependency.

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| --- | --- | --- | --- | --- |
| Phase 8: H = sum JF (SWAP), v_LR = 8eJ/(e-1) | prior artifact | Defines the Hamiltonian to diagonalize; self-modeling IS Heisenberg for n=2 | use as input | plan, execution, verification |
| Phase 9: three area-law perspectives (WVCH, channel capacity, delta S) | prior artifact | Defines what numerical targets to check; Eqs. 09-03.1, 09-03.2, 09-03.6 | compare numerical results against bounds | plan, verification |
| Phase 10: numerical targets H.1-H.3 | prior artifact | Specifies exactly what Phase 11 must compute: area-law scaling, MVEH, K locality | implement all three checks | plan, execution |
| Calabrese-Cardy (hep-th/0405152) | benchmark | S = (c/3)ln(L) + const for critical 1D; c=1/2 for Ising, c=1 for Heisenberg | compare | verification |
| Laflorencie (arXiv:1512.03388) | review | Comprehensive review of entanglement in condensed matter; benchmark values | cite, compare | verification |
| Eisert-Cramer-Plenio (arXiv:0808.3773) | review | Area laws review; methodology for distinguishing area vs volume law | cite | plan, verification |
| code/self_modeling_lr_velocity.py | prior artifact | Existing code with construct_swap(), construct_h_xy(), Pauli matrices, expm | extend, reuse utilities | execution |
| code/self_modeling_hamiltonian.py | prior artifact | Existing code with construct_h_xy() for n=2 Heisenberg interaction | extend, reuse | execution |
| Wolf-Verstraete-Cirac-Hastings (arXiv:0704.3906) | benchmark | I(A:B) <= 2*beta*|boundary|*|J| for thermal states | verify numerically | verification |

**Missing or weak anchors:** No prior numerical computation of modular Hamiltonian locality for interacting spin chains in this project. The matrix-element decay check (H.3 from Phase 10) has no established benchmark values -- it is a qualitative test. Peschel's results (arXiv:0906.1663) provide the free-fermion case but the interacting Heisenberg case requires numerical computation. The MVEH check is qualitative only; no quantitative benchmark exists.

## Conventions

| Choice | Convention | Alternatives | Source |
| --- | --- | --- | --- |
| Unit system | Natural (hbar = c = k_B = 1) | SI, lattice units | Project conventions |
| Metric signature | (-,+,+,+) | (+,-,-,-) | Project SUMMARY.md |
| Entropy base | Nats (ln) | Bits (log_2) | Project conventions |
| Hamiltonian sign | H = sum h_xy, ground state minimizes E | H = -sum | Phase 8 convention |
| Lattice spacing | a_lat = 1 | Physical units | Phase 8 convention |
| Interaction form | h_xy = JF (SWAP); for n=2, h_xy = (J/2)(sigma.sigma) | -- | Phase 8 Eq. (08.1) |
| Entanglement entropy | S(A) = -Tr(rho_A ln rho_A) | Renyi S_alpha | Standard von Neumann |
| Mutual information | I(A:B) = S(A) + S(B) - S(AB) | -- | Standard |
| Eigenvalue threshold | lambda > 1e-14 for entropy sums | 1e-12, 1e-16 | Numerical stability |

**CRITICAL: All equations and results below use these conventions. The entropy is in nats (natural logarithm). The Hamiltonian is H = sum JF_{xy} with F the SWAP operator. For n=2, this is the isotropic Heisenberg model h_{xy} = (J/2)(sigma_x sigma_x + sigma_y sigma_y + sigma_z sigma_z).**

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in This Phase |
| --- | --- | --- | --- |
| H = sum_{<x,y>} JF_{xy} | Self-modeling Hamiltonian | Phase 8, Eq. (08.1) | The Hamiltonian to diagonalize |
| F\|v,w> = \|w,v> | SWAP operator definition | Phase 8 | Construct H matrix |
| S(A) = -sum_i lambda_i ln(lambda_i) | von Neumann entropy | Standard | Compute entanglement entropy from eigenvalues of rho_A |
| rho_A = Tr_B(\|psi><psi\|) | Reduced density matrix | Standard | Partial trace of ground state |
| I(A:B) = S(A) + S(B) - S(AB) | Mutual information | Standard | Compute MI for WVCH check |
| S = (c/3) ln(L/a) + c_1 | Calabrese-Cardy (periodic BC) | hep-th/0405152, Eq. (11) | Benchmark for critical chains |
| S = (c/6) ln(L/a) + c_1' | Calabrese-Cardy (open BC) | hep-th/0405152, Eq. (12) | Benchmark for open chains |
| I(A:B) <= 2*beta*\|boundary\|*\|J\| | WVCH bound | PRL 100, 070502 | Thermal state area-law check |
| K_A = -ln(rho_A) | Modular Hamiltonian | Standard | Compute and check locality |
| H_TFI = -J sum sigma_z^i sigma_z^{i+1} - h sum sigma_x^i | Transverse-field Ising | Standard | Benchmark model |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --- | --- | --- | --- |
| Sparse Lanczos (ARPACK) | Finds ground state of sparse H | Ground state computation | scipy.sparse.linalg.eigsh |
| Tensor reshaping partial trace | Computes rho_A from \|psi> | Every S(A) computation | COMPUTATIONAL.md algorithm |
| Symmetric eigendecomposition | Extracts lambda_i from rho_A | S(A) from eigenvalues | numpy.linalg.eigh |
| Linear regression | Fits S vs \|boundary\| and S vs \|volume\| | Area vs volume law discrimination | scipy.stats.linregress or numpy.polyfit |
| Matrix logarithm | Computes K_A = -ln(rho_A) from eigendecomposition | Modular Hamiltonian check | Direct: K = -V diag(ln lambda) V^T |
| Sparse matrix construction | Builds H as CSR matrix | All ED computations | scipy.sparse |

### Approximation Schemes

| Approximation | Small Parameter | Regime of Validity | Error Estimate | Alternatives if Invalid |
| --- | --- | --- | --- | --- |
| Exact diagonalization (finite size) | 1/N | N >> 1 for bulk behavior | O(1/N) finite-size corrections to S | DMRG for larger 1D |
| Eigenvalue threshold lambda > eps | eps = 1e-14 | Eigenvalues well-separated from 0 | Error ~ eps * \|ln(eps)\| ~ 5e-13 | Lower threshold, check convergence |
| Calabrese-Cardy fit | 1/L, lattice effects | L >> a_lat (many sites in subsystem) | Subleading O(1/L) oscillatory corrections | Use exact finite-size CC formula with chord length |

## Standard Approaches

### Approach 1: Sparse ED + Partial Trace + Regression (RECOMMENDED)

**What:** Construct the full many-body Hamiltonian as a sparse matrix, find the ground state via Lanczos, compute reduced density matrices via tensor reshaping, extract entanglement entropy, and perform linear regression to distinguish area-law from volume-law scaling.

**Why standard:** This is the textbook approach for entanglement entropy computation on small lattices. Used in hundreds of papers (see Laflorencie 2016 review, arXiv:1512.03388). No approximations beyond finite system size and machine precision.

**Track record:** Gold standard for N <= 24 qubits (spin-1/2). Exact to machine precision. Universally used for benchmarking.

**Key steps:**

1. **Construct H as sparse matrix.** For each bond (x,y), construct h_{xy} = JF and embed in full Hilbert space using tensor products. Use scipy.sparse.kron for the tensor product and scipy.sparse.csr_matrix for storage. For N sites: dimension = 2^N, number of nonzeros per row = O(N) for nearest-neighbor H.

2. **Find ground state via Lanczos.** Call scipy.sparse.linalg.eigsh(H, k=1, which='SA') to get the lowest eigenvalue and eigenvector. For N=20: dim = 2^20 = 1M, sparse H has ~20M nonzeros, eigsh takes seconds. For N=24: dim = 16M, takes minutes.

3. **Compute S(A) for varying subsystem sizes.** For each |A| = 1, 2, ..., N/2: reshape |psi> into a (2^|A|, 2^{N-|A|}) matrix, compute rho_A = psi_matrix @ psi_matrix.conj().T, eigendecompose rho_A, compute S = -sum lambda_i ln(lambda_i). This is the bottleneck: rho_A is dense with dimension 2^|A|, so |A| should not exceed ~14.

4. **Regression: area law vs volume law.** For 1D: plot S(L) vs L (subsystem size). Area law: S = const. Volume law: S ~ L. Log correction (critical): S ~ (c/3)ln(L). Fit all three models and compare R^2.

5. **For 2D (4x4 lattice, 16 qubits):** Vary the shape of region A. For rectangular subregions of varying size, the boundary size |boundary(A)| and volume |A| differ. Regress S against |boundary| and |volume| independently. R^2 > 0.9 for boundary fit and R^2 < 0.5 for volume fit constitutes evidence for area law.

**Known difficulties at each step:**

- Step 1: Constructing the sparse Hamiltonian for 2D lattice requires careful bookkeeping of bond indices. Pre-existing code (self_modeling_lr_velocity.py) has utility functions for SWAP construction that should be reused.
- Step 2: eigsh can fail for degenerate ground states (returns linear combination). For the AFM Heisenberg chain with periodic BC, the ground state is unique in the S_z=0 sector. For open BC, it is unique overall for even N.
- Step 3: For the Heisenberg model, the ground state lives in the S_z=0 sector only for even N with periodic BC. Symmetry exploitation (constructing H in the S_z=0 sector) reduces dimension by factor ~sqrt(pi N/2) and speeds computation significantly.
- Step 4: With only O(10) data points for 1D (L = 1 to N/2), the R^2 statistic has large variance. The contract threshold R^2 > 0.9 is achievable for true area-law systems but borderline for systems with small corrections. Use adjusted R^2 for small samples.
- Step 5: 2D subregion enumeration is non-trivial. Use rectangular subregions (easier to enumerate) rather than arbitrary connected subregions.

### Approach 2: QuSpin (FALLBACK)

**What:** Use the QuSpin library for Hamiltonian construction, symmetry exploitation, and dynamics. QuSpin handles symmetry sectors (translation, parity, S_z conservation) automatically and has built-in entanglement entropy routines.

**When to switch:** If N > 20 qubits are needed for convincing statistics, or if symmetry exploitation is critical for the 2D case. QuSpin can handle N ~ 32 for the Heisenberg chain with all symmetries.

**Tradeoffs:** Adds a dependency (pip install quspin). QuSpin's API has changed between versions; the entanglement entropy moved from Hamiltonian objects to basis objects in newer versions. For N <= 20, raw scipy is simpler and avoids the dependency.

### Anti-Patterns to Avoid

- **Using full (dense) diagonalization for N > 16.** Dense diagonalization stores the full d x d matrix and costs O(d^3). For d = 2^20 = 10^6, this requires 10^{12} bytes = 1 TB and O(10^{18}) operations. Always use sparse Lanczos for N > 16.
- **Ignoring symmetry sectors.** The Heisenberg Hamiltonian conserves total S_z. The ground state for even N and J > 0 is in the S_z = 0 sector. Working in this sector reduces dimension from 2^N to C(N, N/2) ~ 2^N / sqrt(pi N/2). For N=20: from 1M to ~185k.
- **Using open boundary conditions without accounting for boundary effects.** Calabrese-Cardy predicts S = (c/6)ln(L) for open chains (half the periodic coefficient). Benchmark comparisons must use the correct formula for the correct boundary condition.
- **Computing rho_A by forming the full density matrix |psi><psi| first.** This is a 2^N x 2^N matrix. Instead, reshape |psi> as a (d_A, d_B) matrix and compute rho_A = psi_matrix @ psi_matrix.conj().T directly. Memory: O(d_A^2) instead of O(d^2).
- **Regressing S(L) against L in 1D and calling it "area law test."** In 1D, |boundary(A)| = 2 (constant) for any interior cut. The area-law test in 1D is whether S(L) saturates (constant) or grows. A linear regression of S against |boundary| in 1D is meaningless because |boundary| does not vary. The correct 1D test is: fit S(L) = a (constant), S(L) = bL (linear), and S(L) = (c/6)ln(L) + d (log), then compare fits.

## Existing Results to Leverage

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
| --- | --- | --- | --- |
| CC formula (periodic) | S(L, N) = (c/3) ln[(N/pi) sin(pi L/N)] + c_1 | Calabrese-Cardy 2004, Eq. (11) | Benchmark critical chains |
| CC formula (open) | S(L, N) = (c/6) ln[(2N/pi) sin(pi L/N)] + c_1' | Calabrese-Cardy 2004, Eq. (12) | Benchmark open chains |
| c = 1/2 for Ising | Central charge of transverse-field Ising at criticality | Exact CFT result | Verify numerical c extraction |
| c = 1 for Heisenberg | Central charge of SU(2)_1 WZW CFT (AFM Heisenberg) | Bethe ansatz + CFT | Verify numerical c extraction |
| Heisenberg ground state energy | E_0/N = 1/4 - ln(2) = -0.443147... (1D, J=1, PBC, thermo limit) | Hulthen 1938, Bethe ansatz | Cross-check ground state |
| TFI critical point | h_c/J = 1 (transition between ordered and paramagnetic) | Exact duality | Set benchmark parameters |
| TFI gapped S(L) | S(L) -> const for h >> J or h << J (both gapped phases) | Exact, area law | Positive control for area law |
| WVCH bound | I(A:B) <= 2*beta*\|bd(A)\|*\|J\| | PRL 100, 070502 | Upper bound check for thermal state MI |
| Page value | S_random ~ (N/2)ln(2) - 1/2 for random pure states | Page 1993 | Negative control: typical state has volume law |

**Key insight:** The self-modeling Heisenberg model (J > 0) in 1D is a gapless critical system with c = 1, so it exhibits log corrections to area law: S ~ (1/3)ln(L). This is NOT a failure -- it is the known result. The contract criteria (R^2 > 0.9 for area-law fit) apply to the gapped case or to 2D. For 1D AFM Heisenberg, the correct expectation is logarithmic scaling. The contract requirement must be interpreted carefully: the area-law test with R^2 criteria is meaningful for (a) gapped 1D benchmarks (TFI away from criticality), (b) 2D lattice, and (c) thermal states at finite T.

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
| --- | --- | --- | --- |
| S_z conservation in Heisenberg | Block-diagonalize H into S_z sectors | Phase 8 | Reduces Hilbert space dimension |
| SWAP eigenvalues | F has eigenvalues +1 (d(d+1)/2 symm) and -1 (d(d-1)/2 antisymm) | Phase 8, code | Verify Hamiltonian construction |
| Heisenberg = SWAP for n=2 | h_xy = (J/2)(sigma.sigma) = J(F - I/2) up to constant | Phase 8, Eq. (08.2) | Use interchangeably |
| Peschel: K is local for free fermions | K_A is a single-particle operator with hopping decaying from boundary | arXiv:0906.1663 | Benchmark for K locality check (free case) |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| --- | --- | --- | --- | --- |
| arXiv:hep-th/0405152 | Calabrese, Cardy | 2004 | Exact CC entanglement entropy formulas for 1D critical systems | Eqs. (11)-(12) for benchmarking |
| arXiv:0808.3773 | Eisert, Cramer, Plenio | 2010 | Comprehensive area-law review | Methodology, known results, caveats |
| arXiv:1512.03388 | Laflorencie | 2016 | Entanglement in condensed matter review | Benchmark values, numerical methods |
| arXiv:0906.1663 | Peschel | 2009 | Free-fermion entanglement Hamiltonian: K is local | Benchmark for K locality test |
| arXiv:1703.08126 | Eisler, Peschel | 2017 | Analytical K for free-fermion chains | Quantitative benchmark for K locality |
| PRL 100, 070502 | Wolf et al. | 2008 | WVCH thermal MI area-law bound | Bound to verify numerically |
| arXiv:1610.03042 | Weinberg, Bukov | 2017 | QuSpin: Python ED package | Fallback tool if needed |

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
| --- | --- | --- | --- |
| NumPy | numpy (>=1.20) | Array operations, eigendecomposition, tensor reshaping | Foundation of all scientific Python |
| SciPy | scipy.sparse, scipy.sparse.linalg | Sparse matrix construction (csr_matrix, kron), Lanczos eigensolver (eigsh) | Standard sparse LA |
| scipy.stats | scipy.stats.linregress | Linear regression for R^2 computation | Standard statistics |

### Supporting Tools

| Tool | Purpose | When to Use |
| --- | --- | --- |
| matplotlib | Plotting S(A) vs L, |boundary|, |volume|; K locality decay plots | Visualization of all results |
| QuSpin | Symmetry-exploited ED for larger systems | Only if N > 20 needed |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
| --- | --- | --- |
| scipy.sparse.linalg.eigsh | numpy.linalg.eigh (dense) | Dense is simpler but limited to N <= 16 |
| Raw scipy sparse construction | QuSpin Hamiltonian builder | QuSpin adds dependency but handles symmetries automatically |
| Von Neumann entropy | Renyi-2 entropy (swap trick) | Renyi-2 avoids full eigendecomposition but is a different quantity |

### Computational Feasibility

| Computation | Estimated Cost | Bottleneck | Mitigation |
| --- | --- | --- | --- |
| 1D chain N=20 ground state | ~5 seconds | eigsh on 1M-dim sparse matrix | Standard on any laptop |
| 1D chain N=20 all S(A) | ~30 seconds | Partial trace for L=1..10 | Parallelize over L |
| 2D 4x4 ground state | ~1 second | eigsh on 65k-dim sparse matrix | Trivial |
| 2D 4x4 all S(A) subregions | ~5 minutes | Enumerating rectangular subregions | Pre-enumerate subregions |
| 1D chain N=24 ground state (S_z=0 sector) | ~30 seconds | eigsh on ~2.7M-dim sparse matrix | S_z conservation |
| Thermal state computation (T = 1/beta) | ~10 minutes for N=16 | Full diag to get all eigenvalues for exp(-beta H)/Z | Only needed for WVCH check |
| Modular Hamiltonian K_A | ~1 second per subsystem | Eigendecompose rho_A (small matrix) | Trivial for |A| <= 6 |

**Installation / Setup:**
```bash
# Core dependencies (likely already installed)
pip install numpy scipy matplotlib
# Optional (only if larger systems needed)
pip install quspin
```

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| --- | --- | --- | --- |
| S(A) = S(B) for pure state | Partial trace correctness | Compute S(A) and S(N-A), verify equal | Exact equality to machine precision |
| S(empty) = 0, S(full) = 0 | Entropy bounds | Compute S for trivial subsystems | Zero to machine precision |
| 0 <= S(A) <= min(|A|, |B|) * ln(2) | Entropy bounds | Check all computed S values | All within bounds |
| Tr(rho_A) = 1 | Normalization | Check trace of every rho_A | 1 to machine precision |
| rho_A hermitian, positive semidefinite | Physical density matrix | Check rho_A = rho_A^dag, all eigenvalues >= -1e-14 | Pass |
| Ground state energy vs known | Hamiltonian correctness | Compare E_0/N to Hulthen value for Heisenberg (PBC, large N) | E_0/N -> 1/4 - ln(2) = -0.443... |
| Strong subadditivity | Quantum information consistency | S(ABC) + S(B) <= S(AB) + S(BC) | Holds for all tripartitions |
| I(A:B) >= 0 | MI non-negativity | Check for all bipartitions | Non-negative to machine precision |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| --- | --- | --- | --- |
| Gapped TFI (h/J = 3) | Deep paramagnetic phase | S(L) = O(1) saturating, area law | Exact |
| Critical TFI (h/J = 1) | Quantum critical point | S(L) ~ (1/12) ln(L) + const (OBC) or (1/6) ln(L) (PBC), c = 1/2 | Calabrese-Cardy |
| AFM Heisenberg (J > 0, PBC) | Critical, c = 1 | S(L, N) = (1/3) ln[(N/pi) sin(pi L/N)] + c_1 | Calabrese-Cardy |
| FM Heisenberg (J < 0) | Fully polarized ground state | S(A) = 0 for all A | Exact (product state) |
| High-T thermal state | beta -> 0 | rho -> I/d, S(A) = |A| ln(2) (volume law) | Page's theorem limit |
| Random pure state | Haar random | S(A) ~ |A| ln(2) - 1/2 | Page 1993 |
| Two-site Heisenberg (J > 0) | N = 2 | S(1) = ln(2) (maximally entangled singlet) | Exact |

### Numerical Validation

| Test | Method | Tolerance | Reference Value |
| --- | --- | --- | --- |
| TFI c = 1/2 extraction | Fit S(L) = (c/6) ln(L) + const to OBC data | |c - 0.5| < 0.05 | Calabrese-Cardy |
| Heisenberg c = 1 extraction | Fit S(L) = (c/3) ln[(N/pi) sin(pi L/N)] + c_1 to PBC data | |c - 1| < 0.1 | Calabrese-Cardy |
| Heisenberg E_0(N=16, PBC) | Compare to Bethe ansatz / reference ED | |delta E/E| < 1e-10 | Exact Bethe ansatz |
| TFI E_0(N=16, h=1, OBC) | Compare to transfer matrix / Jordan-Wigner | |delta E/E| < 1e-10 | Exact free-fermion |
| WVCH bound saturation | I(A:B) / [2*beta*|bd|*|J|] | <= 1 for all beta, A | WVCH theorem |

### Red Flags During Computation

- If S(A) > |A| * ln(2), the partial trace or eigendecomposition has a bug (eigenvalues outside [0,1]).
- If S(A) != S(B) for a pure state bipartition A, B, the partial trace code is wrong.
- If E_0 for the benchmark models deviates from known values by more than 1e-8, the Hamiltonian construction is wrong.
- If eigsh fails to converge for a system that should be straightforward (N <= 20, gapped), the sparse matrix may have been constructed incorrectly (not Hermitian, wrong dimension).
- If R^2 for the area-law fit is high AND R^2 for the volume-law fit is also high, the data does not discriminate between the two models (insufficient dynamic range). This happens in 1D when S(L) varies slowly. Increase N or use 2D.
- If modular Hamiltonian matrix elements do NOT decay from the boundary for the free-fermion case (TFI at h >> J, which is free via Jordan-Wigner), the K computation has a bug -- Peschel proved locality in this case.

## Common Pitfalls

### Pitfall 1: Confusing the Self-Modeling Lattice with a New Model

**What goes wrong:** Treating the n=2 self-modeling lattice as something different from the isotropic Heisenberg model and expecting new physics at the numerical level.
**Why it happens:** The theoretical framework wraps the Heisenberg model in self-modeling language, but H = sum JF_{xy} IS the Heisenberg model for n=2. Phase 8 proved this.
**How to avoid:** For n=2, the self-modeling lattice benchmark IS the Heisenberg chain benchmark. They are the same Hamiltonian. The novel content is the interpretation, not the numerics. If the Heisenberg chain shows area law, so does the self-modeling lattice with the same parameters.
**Warning signs:** Getting different numerical results for "self-modeling" and "Heisenberg" with the same J and N. This means a coding bug, not new physics.
**Recovery:** Verify that construct_h_xy(J) from Phase 8 code produces the same matrix as the standard Heisenberg construction (J/2)(sigma.sigma).

### Pitfall 2: Expecting Strict Area Law from the AFM Heisenberg Chain

**What goes wrong:** Setting J > 0 and expecting S(L) = const in 1D, then declaring failure when S ~ (1/3)ln(L).
**Why it happens:** The AFM Heisenberg chain is gapless (Bethe ansatz), so it has log corrections to area law. This is a known, well-understood result, NOT a contradiction of the project.
**How to avoid:** The contract criteria (R^2 > 0.9 for area-law fit) should be applied to the gapped case. For AFM Heisenberg 1D, the correct test is whether S matches the CC prediction with c=1. Include the log model in the regression and report which model fits best.
**Warning signs:** Reporting R^2 for area-law fit on AFM Heisenberg 1D as a "failure" of the area-law argument.
**Recovery:** Report the result correctly: "The AFM Heisenberg chain shows S ~ (1/3)ln(L) consistent with c=1 CFT, as expected for this gapless system. The gapped TFI benchmark shows strict area law."

### Pitfall 3: Insufficient Dynamic Range in 1D Regression

**What goes wrong:** The R^2 statistic fails to discriminate area law from volume law because S(L) varies by only a small amount across the available L range (especially for gapped systems where S saturates quickly).
**Why it happens:** In 1D with N=20, L ranges from 1 to 10. For a gapped system, S saturates after L ~ xi (correlation length, often 2-5 sites). The regression has only 10 points with most having S ~ const. The R^2 for volume law can be moderate because a line with small slope fits nearly-constant data reasonably.
**How to avoid:** (a) Use 2D where |boundary| and |volume| genuinely vary independently. (b) In 1D, supplement R^2 with the fitted slope: area law predicts slope ~0, volume law predicts slope ~ ln(2). Report both R^2 and the slope magnitude. (c) Use multiple system sizes N = 8, 12, 16, 20 and check finite-size scaling.
**Warning signs:** R^2 > 0.5 for BOTH area-law and volume-law fits in 1D.
**Recovery:** Add 2D computation (4x4 lattice) where |boundary| and |volume| are genuinely independent. This is the definitive test.

### Pitfall 4: Sign of J Ambiguity

**What goes wrong:** Computing with one sign of J and drawing conclusions about the wrong phase.
**Why it happens:** Phase 8 established that the sign of J is NOT determined by self-modeling (SP) constraints. J > 0 (AFM) and J < 0 (FM) give qualitatively different physics.
**How to avoid:** Compute for BOTH signs. Report results for both. Note that J < 0 gives a trivial product ground state with S=0 (useless for gravity). J > 0 gives the physically relevant case.
**Warning signs:** Only reporting one sign without mentioning the other.
**Recovery:** Run both signs. It costs essentially nothing -- just negate J.

### Pitfall 5: Numerical Instability in Modular Hamiltonian Computation

**What goes wrong:** K_A = -ln(rho_A) is numerically unstable when rho_A has eigenvalues very close to zero.
**Why it happens:** ln(0) = -infinity. Eigenvalues of rho_A can be as small as 1e-15, producing K_A matrix elements of order 35 (in nats). These dominate the matrix and obscure the locality structure.
**How to avoid:** (a) Threshold eigenvalues: set lambda < 1e-14 to zero and exclude from the log. (b) Work in the support of rho_A: project onto the subspace with lambda > threshold before taking the log. (c) Report K_A matrix elements relative to the largest eigenvalue, or restrict to the "bulk" of the spectrum.
**Warning signs:** K_A has matrix elements spanning 30+ orders of magnitude. Decay plots dominated by numerical noise.
**Recovery:** Project rho_A onto its support (eigenvalues > 1e-12) before computing ln. Report the condition number of rho_A.

## Level of Rigor

**Required for this phase:** Numerical evidence

**Justification:** Phase 11 is verification, not derivation. The theoretical arguments are in Phases 8-10. This phase provides computational confirmation (or falsification) of those arguments on small systems. The standard of evidence is: do the numbers match the theoretical predictions within finite-size effects?

**What this means concretely:**

- All ground state energies must match known exact values to 10 significant digits (limited only by machine precision and Lanczos convergence).
- Entanglement entropy values must be converged (insensitive to Lanczos tolerance below 1e-12).
- Area-law vs volume-law discrimination must include R^2 values, fitted slopes with error bars, and comparison to the CC prediction for critical systems.
- Finite-size effects must be estimated by computing at multiple system sizes (N = 8, 12, 16, 20).
- The MVEH check is qualitative: does delta S have the right sign? No quantitative threshold.
- The K locality check is qualitative: do matrix elements decay from boundary? Plot with error bars.

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| --- | --- | --- | --- |
| Full dense diagonalization | Sparse Lanczos (ARPACK) | ~2000 | Extends reach from N~14 to N~24 |
| No symmetry exploitation | Symmetry-adapted basis (QuSpin) | 2017 | Extends reach to N~36 for Heisenberg |
| Manual Hamiltonian construction | Library construction (QuSpin, TeNPy) | 2017 | Reduces coding effort; fewer bugs |
| Von Neumann entropy only | Full entanglement spectrum | ~2008 (Li-Haldane) | Richer information about entanglement structure |

**Superseded approaches to avoid:**

- **Full dense diagonalization for N > 16:** Use sparse Lanczos. Dense diag costs O(d^3) vs O(d * nnz * n_iter) for Lanczos.
- **Using Renyi entropy as substitute for von Neumann:** The contract specifies von Neumann entropy. Renyi-2 is easier to compute but gives different values. Compute von Neumann directly.

## Open Questions

1. **What value of J to use?**
   - What we know: J > 0 (AFM) gives nontrivial entanglement relevant for gravity. J < 0 (FM) gives trivial S=0. Phase 8 says sign undetermined by SP.
   - What's unclear: Whether a specific J magnitude matters, or whether only the sign is physically relevant.
   - Impact on this phase: Must compute for both signs. J = +1 (AFM) is the primary case; J = -1 (FM) is the trivial control.
   - Recommendation: Use J = +1 as the primary coupling, J = -1 as control. The magnitude only sets the energy scale (S is dimensionless and does not depend on |J|, only on sign).

2. **Can modular Hamiltonian locality be quantified for the interacting Heisenberg chain?**
   - What we know: For free fermions (TFI in the gapped phase), K_A is provably local (Peschel). For the interacting Heisenberg model, no analytical result exists.
   - What's unclear: What decay rate to expect. Exponential? Power-law?
   - Impact on this phase: The A3 check (modular K locality) is qualitative. If K shows clear boundary-locality, A3 is supported. If not, A3 is weakened.
   - Recommendation: Compute K_A numerically for both TFI (free-fermion benchmark where locality is known) and Heisenberg (interacting case). Compare decay profiles.

3. **Is 2D (4x4 lattice) sufficient for area-law regression?**
   - What we know: 4x4 = 16 qubits is feasible. But there are limited distinct rectangular subregions for regression.
   - What's unclear: Whether the statistical power (number of distinct (|boundary|, S) pairs) is sufficient for R^2 > 0.9.
   - Impact on this phase: If 4x4 has too few data points, the 2D area-law claim is weak.
   - Recommendation: Enumerate all rectangular subregions of a 4x4 lattice. There are O(50) distinct rectangles with varying |boundary| and |volume|. This should be sufficient.

4. **How to handle the MVEH check given that it is a continuum concept?**
   - What we know: MVEH (vacuum maximizes entanglement entropy) is a statement about the continuum vacuum. On a lattice, the "vacuum" is the ground state.
   - What's unclear: Whether delta S < 0 for all local perturbations of the ground state is the correct lattice analog.
   - Impact on this phase: The MVEH check is the most speculative part of Phase 11.
   - Recommendation: Apply random local unitaries to the ground state and check whether S(A) decreases for small regions A. This is a qualitative sanity check, not a proof. Report as "consistent with MVEH" or "inconsistent with MVEH."

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| --- | --- | --- | --- |
| scipy.sparse.linalg.eigsh | Non-convergence for large N | QuSpin with symmetries | ~2 hours to rewrite Hamiltonian construction |
| Raw sparse construction | Bug-prone for 2D lattice | QuSpin lattice builder | ~1 hour |
| 1D regression R^2 insufficient | Log corrections from criticality | Switch to gapped models (TFI h=3) or 2D | Minimal; just change parameters |
| 2D 4x4 insufficient data | Too few subregions | 2D 4x5 (20 qubits, 8 MB) or 3x4 with d=4 | ~10 minutes extra computation |
| K locality computation | Numerical instability from small eigenvalues | Restrict to Renyi-2 entanglement Hamiltonian or use SVD-based approach | ~30 minutes to rewrite |

**Decision criteria:** If the primary scipy approach produces correct benchmark results (TFI, Heisenberg) and meaningful area-law statistics within the contract thresholds, it is sufficient. Switch to QuSpin only if (a) larger system sizes are needed for statistical significance, or (b) the 2D Hamiltonian construction proves too error-prone by hand.

## Sources

### Primary (HIGH confidence)

- Calabrese, Cardy (2004), "Entanglement Entropy and Quantum Field Theory," JSTAT P06002, [arXiv:hep-th/0405152](https://arxiv.org/abs/hep-th/0405152) - Exact CC formulas for 1D critical entanglement entropy
- Calabrese, Cardy (2009), "Entanglement Entropy and Conformal Field Theory," J. Phys. A 42, 504005, [arXiv:0905.4013](https://arxiv.org/abs/0905.4013) - Extended CC results, finite-size formulas
- Eisert, Cramer, Plenio (2010), "Area Laws for the Entanglement Entropy," RMP 82, 277, [arXiv:0808.3773](https://arxiv.org/abs/0808.3773) - Comprehensive area-law review
- Wolf, Verstraete, Cirac, Hastings (2008), "Area Laws in Quantum Systems: Mutual Information and Correlations," PRL 100, 070502, [arXiv:0704.3906](https://arxiv.org/abs/0704.3906) - WVCH thermal MI bound
- SciPy documentation, scipy.sparse.linalg.eigsh - Lanczos eigensolver specification

### Secondary (MEDIUM confidence)

- Laflorencie (2016), "Quantum Entanglement in Condensed Matter Systems," Phys. Rep. 646, 1, [arXiv:1512.03388](https://arxiv.org/abs/1512.03388) - Review with numerical benchmarks
- Peschel (2009), "Reduced Density Matrices and Entanglement Entropy in Free Lattice Models," [arXiv:0906.1663](https://arxiv.org/abs/0906.1663) - Free-fermion entanglement Hamiltonian locality
- Eisler, Peschel (2017), "Analytical Results for the Entanglement Hamiltonian of a Free-Fermion Chain," [arXiv:1703.08126](https://arxiv.org/abs/1703.08126) - Quantitative K locality for free fermions
- Weinberg, Bukov (2017), "QuSpin: a Python Package for Dynamics and Exact Diagonalisation," SciPost Phys. 2, 003, [arXiv:1610.03042](https://arxiv.org/abs/1610.03042) - QuSpin package
- Phase 8-10 derivation files and summaries (this project) - Prior results to verify

### Tertiary (LOW confidence)

- Phase 10 MVEH numerical targets (H.2) - Qualitative check with no established benchmark
- K locality for interacting systems - No analytical benchmark exists for Heisenberg

## Caveats and Alternatives

**Self-critique:**

1. *What assumption am I making that might be wrong?* I assume that N=16-20 is sufficient for area-law scaling to be visible and for finite-size effects to be small. For the gapless Heisenberg chain, finite-size effects are logarithmic and persistent. The CC formula partially accounts for this, but subleading oscillatory corrections (Affleck-Ludwig boundary entropy, parity effects) can be significant for N ~ 20.

2. *What alternative approach did I dismiss too quickly?* DMRG (via TeNPy or ITensor) could access N ~ 100 sites in 1D, giving much better scaling statistics. I dismissed it because the contract specifies exact diagonalization and the target sizes (N=16-20) are within ED reach. But if the area-law regression is inconclusive at N=20, DMRG would be the natural next step.

3. *What limitation of my recommended method am I understating?* The 2D area-law regression on a 4x4 lattice has limited statistical power. With only O(50) rectangular subregions, and many having the same |boundary| value, the regression may not clearly distinguish area from volume law. A 5x4 lattice (20 qubits, still feasible) would be better but doubles the effort.

4. *Is there a simpler method I overlooked?* For the area-law test, one could simply plot S(L) vs L and visually inspect whether it saturates (area law) or grows linearly (volume law), without formal regression. This is what most papers do. The R^2 requirement is the contract's quantitative criterion; visual inspection is the physicist's method.

5. *Would a specialist disagree?* A computational condensed matter physicist would note that for the Heisenberg chain, the gold-standard entanglement computation uses DMRG, not ED. ED at N=20 has significant finite-size effects for the Heisenberg chain. However, ED is exact (no bond-dimension truncation errors), and the contract specifies ED. The specialist would also insist on exploiting S_z conservation, which reduces the Hilbert space by ~sqrt(N) and is straightforward to implement.

## Metadata

**Confidence breakdown:**

- Mathematical framework: HIGH - All methods are standard textbook ED plus standard entanglement entropy computation
- Standard approaches: HIGH - Sparse Lanczos + partial trace is the universal approach for small-system entanglement
- Computational tools: HIGH - NumPy/SciPy are mature, well-documented, widely used
- Validation strategies: HIGH - Known exact results (CC formula, Bethe ansatz) provide rigorous benchmarks
- Modular Hamiltonian check: MEDIUM - Method is clear but no interacting-system benchmark exists
- MVEH check: LOW - Qualitative check with no established benchmark; lattice analog of continuum concept

**Research date:** 2026-03-22
**Valid until:** Indefinite for physics content; tool versions may change (numpy/scipy API stable)
