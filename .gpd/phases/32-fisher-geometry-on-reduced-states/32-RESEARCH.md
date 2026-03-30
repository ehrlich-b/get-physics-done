# Phase 32: Fisher Geometry on Reduced States - Research

**Researched:** 2026-03-29
**Domain:** Quantum information geometry / Riemannian geometry on state manifolds / Quantum lattice systems
**Confidence:** MEDIUM-HIGH

## Summary

Phase 32 establishes the foundational geometric object for the entire v9.0 milestone: the quantum Fisher information metric on the manifold of reduced density matrices {rho_Lambda(x)} parametrized by lattice position x on an OBC lattice. The phase must deliver three results: (FISH-01) smoothness of rho_Lambda(x) as a function of x when correlations decay sufficiently fast, (FISH-02) positive-definiteness of the SLD quantum Fisher metric g_ij(x) for non-degenerate ground states with full-rank reduced states, and (FISH-03) asymptotic recovery of lattice distance from Fisher geodesic distance at separations large compared to the correlation length xi.

The mathematical framework is well-established: the SLD Fisher metric is defined via the symmetric logarithmic derivative (Braunstein-Caves 1994), computed numerically via eigendecomposition of the density matrix (Liu-Peng-Yuan 2020), and is known to equal 4x the Bures metric at full-rank points (Safranek 2017). The smoothness argument chains through exponential clustering (Hastings-Koma 2006): spectral gap implies exponential decay of correlations, which implies that shifting the subsystem by one lattice site changes rho_Lambda by an amount exponentially suppressed in the distance from the boundary change to the rest of the system. The distance recovery result requires showing that the Fisher metric in the bulk is approximately constant (reflecting the approximate translation invariance), so that geodesic distance is proportional to lattice distance.

**Primary recommendation:** Use the eigendecomposition-based SLD formula for Fisher metric computation on the existing ED infrastructure (code/ed_entanglement.py), OBC lattices N=8-20 for numerics, and chain the analytical argument through Hastings-Koma exponential clustering for the smoothness theorem. Handle rank-deficient states via Bures fallback per Safranek 2017. Cross-validate SLD metric against fidelity-based Bures metric (must agree to factor of 4).

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| --- | --- | --- | --- | --- |
| ref-braunstein-caves1994 (PRL 72, 3439) | Method definition | Defines the SLD Fisher metric; proves it is the maximal monotone metric; establishes operational meaning via Cramer-Rao | Use as the defining reference for g_ij | Plan, execution, verification |
| ref-zanardi2007 (PRL 99, 100603) | Benchmark | Fisher metric singularities at QPTs; TFI benchmark for metric computation | Use TFI critical point as computational benchmark | Plan (benchmark task), execution |
| Provost-Vallee 1980 (CMP 76, 289) | Foundation | Riemannian structure on manifold of quantum states; establishes that the metric pullback to pure states gives Fubini-Study | Cite for pure-state limit check; verify g_F reduces to 4*g_FS on pure states | Execution, verification |
| ref-paper5 (v2.0) | Prior artifact | M_n(C)^sa finite-dimensional observer = UV cutoff; determines that |Lambda| <= n^2 - 1 | Reference for subsystem dimension constraint | Plan, execution |
| ref-paper6 (v3.0) | Prior artifact | SWAP lattice definition; OBC requirement; ED data from Phase 11 (N=8-20) | Use as lattice definition and prior numerical infrastructure | Plan, execution |
| Hastings-Koma 2006 (CMP 265, 781) | Backbone theorem | Spectral gap => exponential clustering; provides the smoothness argument backbone | Cite and apply for FISH-01 smoothness proof | Plan, execution, verification |
| Safranek 2017 (PRA 95, 052320) | Method caveat | QFI is discontinuous at rank-changing points; Bures metric is the continuous extension | Use for rank-deficient fallback strategy | Plan (backtracking trigger), execution |

**Missing or weak anchors:** None for Phase 32. All required anchors are well-established published results with high confidence. The smoothness argument for algebraic (non-exponential) correlation decay is not anchored in a single reference but follows from standard analysis (power-law decay functions are C^infinity); this gap is acceptable for Phase 32 since the full algebraic-decay analysis is deferred to Phase 33 (CORR-03).

## Conventions

| Choice | Convention | Alternatives | Source |
| --- | --- | --- | --- |
| Metric definition | g_ij = (1/2) Tr[rho {L_i, L_j}] (SLD Fisher) | Bures: g^B = g^F/4; Wigner-Yanase; Kubo-Mori | Braunstein-Caves 1994 |
| Metric normalization | g_F = 4 * g_Bures (the "quantum Fisher information metric") | Some refs use g_Bures as primary | Project convention (SUMMARY.md) |
| Units | Natural (hbar=1, k_B=1), lattice spacing a=1 | SI | Project convention |
| Metric dimensions | [length]^{-2} in lattice units | dimensionless if a is factored out | Project convention |
| Eigenvalue threshold | 1e-14 for zero eigenvalue cutoff in SLD formula | 1e-12 (more conservative) | ed_entanglement.py existing convention |
| Boundary conditions | OBC for physics; PBC for symmetry checks | PBC only (gives g=0, useless) | Project requirement (FISH-01) |
| Fourier convention | e^{-ikx} forward | e^{+ikx} | Project convention |
| Coupling | J > 0 antiferromagnetic | J < 0 ferromagnetic | Project convention |

**CRITICAL: All equations and results below use these conventions. The SLD Fisher metric g_ij is 4x the Bures metric. Some references (especially Zanardi et al.) use "fidelity susceptibility" chi_F = g_Bures/N, which is g_F/(4N). Always verify normalization when comparing.**

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in This Phase |
| --- | --- | --- | --- |
| g_ij(x) = (1/2) Tr[rho(x) {L_i(x), L_j(x)}] | SLD Fisher metric definition | Braunstein-Caves 1994 | Central definition of the geometric object |
| (rho L_i + L_i rho)/2 = d_i rho | SLD equation (Lyapunov) | Standard | Defines L_i implicitly; solve via eigendecomposition |
| <m\|L_i\|n> = 2<m\|d_i rho\|n>/(p_m + p_n) | SLD matrix elements in eigenbasis | Liu-Peng-Yuan 2020 | Computational formula; numerator from finite differences |
| g_ij = sum_{m,n: p_m+p_n>0} 2\|<m\|d_i rho\|n>\|^2 / (p_m + p_n) | Closed-form QFIM | Braunstein-Caves 1994 | Primary computational algorithm |
| d_i rho ~ [rho(x+ae_i) - rho(x-ae_i)] / (2a) | Central finite difference | Standard numerical analysis | O(a^2) approximation of the parameter derivative |
| g_F = 4 g_Bures; g_Bures = 2(1 - sqrt(F))/epsilon^2 | Fisher-Bures relation | Safranek 2017 | Cross-validation identity |
| F(rho,sigma) = [Tr sqrt(sqrt(rho) sigma sqrt(rho))]^2 | Quantum fidelity (Uhlmann) | Uhlmann 1976; Jozsa 1994 | Used in Bures cross-validation |
| \|\|rho_A(x+delta) - rho_A(x)\|\| <= C\|delta\|/a * exp(-d_boundary/xi) | Smoothness from clustering | Hastings-Koma 2006 (derived) | Core of FISH-01 proof |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --- | --- | --- | --- |
| Eigendecomposition of rho | Produces {p_m, \|m>} for SLD formula | Every QFIM computation | Standard linear algebra |
| Central finite differences | Approximates d_i rho from shifted partial traces | Parameter derivatives on lattice | Standard numerical analysis |
| Partial trace via tensor reshape | Produces rho_Lambda(x) from ground state | Subsystem extraction at each position x | ed_entanglement.py (existing) |
| Lanczos eigensolver | Finds ground state of sparse Hamiltonian | Ground state computation | scipy.sparse.linalg.eigsh |
| Dijkstra shortest path | Computes geodesic distance on metric graph | Distance recovery test (FISH-03) | Standard graph algorithm |
| Exponential clustering theorem | Bounds correlation decay from spectral gap | Smoothness proof (FISH-01) | Hastings-Koma 2006 |

### Tensor Covariance of g_ij

**Requirement FISH-04 (success criterion 4):** g_ij must transform as a rank-2 covariant tensor under lattice diffeomorphisms. This is automatic from the construction:

The Fisher metric g_ij is defined as the pullback of the Bures/SLD metric on the space of density matrices to the parameter manifold (lattice positions). Pullback metrics inherit covariant tensor transformation properties by construction. Concretely, if we reparametrize lattice positions x -> y(x) with Jacobian J^i_j = dx^i/dy^j, then:

    g'_ij(y) = J^a_i J^b_j g_ab(x(y))

This follows from the chain rule applied to d_i rho: under reparametrization, d/dy^i = (dx^a/dy^i) d/dx^a, which transforms the SLD operators and hence the metric as a rank-2 covariant tensor.

**Verification:** On the discrete lattice, "diffeomorphisms" are limited to relabeling sites. The covariance check reduces to verifying that g_ij computed in two different coordinate systems (e.g., left-to-right vs right-to-left labeling on a 1D chain) are related by the appropriate Jacobian (which for a reflection is just the parity transformation). This is a simple numerical check: compute g in both orderings and verify g'(y) = J^T g(x) J.

**Dimensional check:** g_ij has dimensions [length]^{-2} = [lattice site]^{-2} (dimensionless when a=1). Under rescaling x -> lambda*x, g -> g/lambda^2, consistent with a rank-2 covariant tensor with [length]^{-2} dimensions.

### Approximation Schemes

| Approximation | Small Parameter | Regime of Validity | Error Estimate | Alternatives if Invalid |
| --- | --- | --- | --- | --- |
| Central finite difference for d_i rho | a (lattice spacing) | Always valid on discrete lattice; exact for lattice position parametrization | O(a^2) systematic error in derivative | Higher-order finite differences (4th order) |
| Eigenvalue threshold cutoff | epsilon_thresh = 1e-14 | Full-rank or near-full-rank rho | Negligible for p_m >> 1e-14; drops contributions from numerically zero eigenvalues | Bures metric (continuous at rank changes) |
| Bulk approximation (ignore boundary effects) | 1/N (boundary fraction) | Interior of OBC lattice, x >> xi and N-x >> xi | O(exp(-x/xi)) boundary corrections | Explicit boundary treatment; finite-size scaling |
| Exponential clustering for smoothness | exp(-R/xi) where R = subsystem radius | Gapped systems with gap gamma > 0 | Controlled: xi = O(v_LR/gamma) | For gapless systems: algebraic smoothness argument (Phase 33) |

## Standard Approaches

### Approach 1: Eigendecomposition SLD Formula (RECOMMENDED)

**What:** Compute g_ij(x) at each lattice position x by: (1) construct ground state via Lanczos, (2) extract rho_Lambda(x) via partial trace at each position, (3) eigendecompose rho_Lambda(x), (4) compute d_i rho via central finite differences of neighboring partial traces, (5) assemble g_ij using the closed-form SLD eigendecomposition formula.

**Why standard:** This is the most numerically stable and conceptually transparent method for computing the quantum Fisher information metric. It avoids matrix logarithm derivatives (which fail catastrophically for rank-deficient states), directly handles the zero-eigenvalue regularization, and produces the SLD operators L_i as a byproduct.

**Track record:** Used in Liu-Peng-Yuan 2020 (comprehensive review), Zanardi et al. 2007 (QPT detection), and is the standard algorithm in all QFIM implementations.

**Key steps:**

1. **Ground state computation:** Construct SWAP Hamiltonian (existing code), find ground state via Lanczos. Use OBC for physics, PBC for symmetry cross-check.
2. **Subsystem extraction:** For each lattice position x = 0, 1, ..., N-|Lambda|, compute rho_Lambda(x) = Tr_{complement}(|psi><psi|) where Lambda = {x, x+1, ..., x+|Lambda|-1}. Use existing `partial_trace` function.
3. **Eigendecomposition:** At each x, diagonalize rho_Lambda(x) = sum_m p_m |m><m|. Record eigenvalues and eigenvectors. Discard eigenvalues below threshold (1e-14).
4. **Finite differences:** For each direction i, compute d_i rho = [rho(x+e_i) - rho(x-e_i)] / 2 using neighboring partial traces (already computed in step 2).
5. **SLD assembly:** Compute g_ij(x) = sum_{m,n} 2|<m|d_i rho|n>|^2 / (p_m + p_n) where sum runs over pairs with p_m + p_n > threshold.
6. **Positive-definiteness check:** Verify all eigenvalues of g(x) are positive at interior points.
7. **Distance recovery:** Build weighted graph with edge weights sqrt(g_ii(x)) * a, run Dijkstra, compare geodesic to lattice distance.

**Known difficulties at each step:**

- Step 1: For Heisenberg AFM, ground state is in the Sz=0 sector. Use symmetry to reduce Hilbert space if N > 18.
- Step 2: On OBC, rho_Lambda(x) genuinely varies with x. On PBC, rho_Lambda(x) is x-independent (symmetry check: g should be zero or constant).
- Step 3: Near-degenerate eigenvalues can cause numerical instability in eigenvectors. Use `np.linalg.eigh` (not eigvalsh) to get vectors.
- Step 4: At boundaries (x=0 or x=N-|Lambda|), one-sided differences must be used.
- Step 5: When p_m + p_n is very small but nonzero, the ratio amplifies noise. Use threshold on the sum (1e-10), not just individual eigenvalues.
- Step 6: Near boundaries, g(x) may be rank-deficient or have small eigenvalues due to boundary effects. Report bulk values separately.
- Step 7: In 1D, geodesic is trivially along the chain. Non-trivial test requires 2D lattice or comparison of geodesic distance scaling with lattice distance.

### Approach 2: Fidelity-Based Bures Metric (CROSS-VALIDATION)

**What:** Compute g_Bures_ij from the quantum fidelity F(rho(x), rho(x+epsilon*e_i)) and use the identity g_F = 4 * g_Bures.

**When to switch:** Use as cross-validation for Approach 1 at every point. If they disagree by more than machine precision (relative error > 1e-10), there is a bug.

**Tradeoffs:** Slightly less numerically stable than the eigendecomposition approach (involves square roots of matrices), but provides an independent check and automatically handles rank-deficient states (Bures metric is continuous at rank changes, unlike SLD which diverges).

### Approach 3: Direct Bures Distance (QUICK SANITY CHECK for FISH-03)

**What:** Skip the metric tensor entirely. Compute d_Bures(rho(x), rho(y)) = sqrt(2(1 - sqrt(F(rho(x), rho(y))))) directly for all pairs (x,y). Plot d_Bures vs d_lattice = |x-y|.

**When to use:** As a fast first check of distance recovery before computing the full metric tensor. If d_Bures is approximately linear in d_lattice in the bulk, FISH-03 is likely true.

**Tradeoffs:** Does not give the tensorial metric g_ij (needed downstream for spatial geometry), but confirms distance recovery with zero numerical differentiation. Complements the metric-based approach.

### Anti-Patterns to Avoid

- **Matrix logarithm approach:** Computing g_ij via Tr[d_i(log rho) d_j(rho)] fails catastrophically for rank-deficient states because log(rho) has -infinity eigenvalues. Never use `scipy.linalg.logm`. Recovery: use eigendecomposition SLD formula.
- **PBC for Fisher metric:** On periodic lattices with exact translation symmetry, rho_Lambda(x) is x-independent and g = 0 identically. This is correct (flat geometry from perfect symmetry) but useless. Always use OBC for the physics. Recovery: switch to OBC.
- **Full state Fisher metric:** Computing the Fisher metric on the full pure state |psi> gives the Fubini-Study metric on projective Hilbert space, not the reduced-state Fisher metric. The reduced-state metric captures the physical (lattice position) geometry; the full-state metric captures the abstract parameter geometry. Recovery: always partial-trace first.
- **Subsystem too large:** If |Lambda| > N/3, the reduced state approaches purity and the metric degenerates. Recovery: keep |Lambda| = 2 to 4 for N = 8-20.
- **Ignoring sublattice alternation in Neel phase:** For antiferromagnets, rho_Lambda at even vs odd sites can differ significantly (alternating sublattice magnetization). The Fisher metric may show large even/odd oscillations. Recovery: coarse-grain over unit cells (average over pairs of adjacent sites), or restrict analysis to same-sublattice comparisons.

## Existing Results to Leverage

**This section is MANDATORY.** The following results should be CITED and USED, not re-derived.

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
| --- | --- | --- | --- |
| SLD Fisher metric = 4 x Bures metric (full rank) | g_F^{SLD}_{ij} = 4 g^{Bures}_{ij} when rho is full-rank | Braunstein-Caves 1994; Safranek 2017 | Cross-validation identity |
| Morozova-Cencov-Petz classification | SLD Fisher metric is the LARGEST monotone metric on density matrix space | Petz 1996 (LAA 244, 81) | Justifies using SLD over other metrics |
| Hastings-Koma exponential clustering | gamma > 0 => \|<AB> - <A><B>\| <= C exp(-d/xi), xi = O(v_LR/gamma) | Hastings-Koma CMP 265 (2006) | Core of FISH-01 smoothness argument |
| Safranek discontinuity theorem | QFI (SLD) is discontinuous at rank-changing points; Bures metric is the continuous extension | Safranek PRA 95 (2017) | Backtracking trigger: if rho_Lambda(x) is rank-deficient at generic points, switch to Bures |
| Provost-Vallee pure state limit | For pure rho = \|psi><psi\|, g_F = 4(Re<d_i psi\|d_j psi> - <d_i psi\|psi><psi\|d_j psi>) = 4 g_{FS} | Provost-Vallee CMP 76 (1980) | Limiting case check: when |Lambda| -> N, rho -> pure state, g_F -> 4 g_{FS} |
| LR velocity for SWAP on Z^1 | v_LR = 8eJ/(e-1) ~ 21.7 J | Nachtergaele-Sims; v3.0 Phase 11 | Input for xi = v_LR/gamma bound |
| PBC gives g = 0 | On periodic lattice with translation-invariant ground state, rho_Lambda(x) is x-independent | Trivial by symmetry | Sanity check: must use OBC |
| Pullback metric is a rank-2 covariant tensor | g_ij(x) transforms as g'_ij(y) = J^a_i J^b_j g_ab(x(y)) under reparametrization | Standard differential geometry | Tensor covariance check (FISH-04) is automatic from construction |

**Key insight:** The SLD eigendecomposition formula, the Hastings-Koma theorem, and the Bures-Fisher relation are all textbook results. None should be re-derived. The new content is (a) applying these to the specific SWAP lattice with OBC, (b) proving positive-definiteness for the SWAP ground state, and (c) establishing the distance recovery claim.

### Full-Rank Property of Reduced States (Strategy for FISH-02)

The positive-definiteness of g_ij requires rho_Lambda(x) to be full-rank (all eigenvalues > 0) at interior lattice points. The strategy to establish this:

**Analytical argument:** For a non-degenerate ground state |psi> of a local Hamiltonian on an OBC lattice, the reduced density matrix rho_Lambda(x) for a subsystem Lambda in the interior is generically full-rank. This follows from:

1. The ground state |psi> is entangled across the cut between Lambda and its complement (for any non-trivial Hamiltonian with interactions crossing the boundary).
2. Full rank of rho_Lambda is equivalent to the ground state having nonzero weight on all product states in the Schmidt decomposition across the Lambda/complement cut.
3. For the Heisenberg/SWAP Hamiltonian, SU(2) symmetry constrains the ground state to the Sz=0 sector but does not force zero eigenvalues in the entanglement spectrum for small subsystems.
4. Rank deficiency at a generic interior point would require a fine-tuned cancellation that is not expected for the SWAP Hamiltonian.

**Numerical verification (definitive for finite N):** Compute min eigenvalue of rho_Lambda(x) at every interior point for N=8,12,16,20 with |Lambda|=2,3,4. If min_eigenvalue > 0 (practically, > 1e-10) at all interior points, full-rank is established numerically. If any interior point has min_eigenvalue < 1e-10, document which point and switch to Bures metric there.

**What could go wrong:** At boundary sites (x near 0 or N-|Lambda|), rho may become nearly rank-deficient because the subsystem is near the edge and has fewer entangling bonds. This is expected and handled by restricting "interior" to x in [|Lambda|, N-2|Lambda|] or similar.

### Asymptotic Distance Recovery: Analytical Scaffolding for FISH-03

The claim d_Fisher(x,y) / d_lattice(x,y) -> const > 0 as |x-y| >> xi needs an explicit analytical framework:

**Bulk constancy argument:** In the interior of an OBC lattice (x >> xi and N-x >> xi), rho_Lambda(x) depends on x primarily through boundary effects. For a gapped system, the sensitivity of rho_Lambda to the boundary decays exponentially: rho_Lambda(x) = rho_Lambda^{bulk} + O(exp(-x/xi)) + O(exp(-(N-x-|Lambda|)/xi)). Therefore:
- d_i rho at interior points is dominated by the variation due to shifting the subsystem cut, not boundary effects
- This variation is approximately x-independent in the bulk, giving g_ij(x) ~ g_ij^{bulk} + O(exp(-min(x, N-x)/xi))
- The Fisher geodesic distance between two interior points is then d_Fisher(x,y) ~ sqrt(g_bulk) * |x-y| * a

**The asymptotic constant:** For a 1D chain with |Lambda|=l, the bulk Fisher metric scalar g_bulk is:

    g_bulk = sum_{m,n} 2|<m|[rho(x+1) - rho(x-1)]|n>|^2 / (2(p_m + p_n))

This depends on (i) the Hamiltonian parameters (J, subsystem size l), (ii) the correlation structure (xi), and (iii) the specific ground state. The constant in d_Fisher/d_lattice -> const is:

    const = sqrt(g_bulk) * a = sqrt(g_bulk) [dimensionless when a=1]

**Numerical extraction:** Compute g(x) for x in the bulk of N=8,12,16,20 chains. Fit g_bulk as the plateau value. Extrapolate g_bulk(N) -> g_bulk(infinity) via finite-size scaling. Express the result as a function of J, l, and xi.

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
| --- | --- | --- | --- |
| Liu-Peng-Yuan QFIM formula for arbitrary rank | Explicit formula for g_ij that handles rank deficiency | arXiv:1312.6910; J. Phys. A 53 (2020) | General density matrices |
| Zanardi QPT benchmark on TFI | Fisher metric scalar curvature diverges at h/J = 1 for transverse-field Ising | Zanardi et al. PRL 99 (2007) | Use as independent algorithm validation |
| Calabrese-Cardy 1D CFT entropy | S(L) = (c/3) ln(L/a) + const with c=1 for SU(2)_1 WZW | Calabrese-Cardy JSTAT P06002 (2004) | Provides scaling context for 1D Fisher metric |
| Phase 11 ED data | Ground states and entropy for N=8-20 on SWAP lattice | Project v3.0 Phase 11 | Direct input; reuse existing computed ground states |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| --- | --- | --- | --- | --- |
| Statistical distance and geometry of quantum states | Braunstein, Caves | 1994 | Defines the Fisher metric; proves positive-semidefiniteness; operational meaning | Definition, key theorem (Theorem 1), Cramer-Rao connection |
| Riemannian structure on manifolds of quantum states | Provost, Vallee | 1980 | Pure state metric = Fubini-Study; foundational Riemannian geometry on state manifolds | Pure-state limiting case; formula for g_{FS} |
| Information-theoretic differential geometry of QPTs | Zanardi, Giorda, Cozzini | 2007 | Fisher metric on parameter manifolds diverges at QPTs | Benchmark (TFI model); conceptual framework |
| Discontinuities of QFI and Bures metric | Safranek | 2017 | QFI discontinuous at rank changes; Bures is continuous extension | Rank-deficiency handling; explicit formulas |
| QFI matrix and multiparameter estimation (review) | Liu, Peng, Yuan | 2020 | Comprehensive review of QFIM computation | Algorithm details; arbitrary-rank formula |
| Space from Hilbert Space | Cao, Carroll, Michalakis | 2017 | Mutual information defines graph distance; geometry from entanglement | Conceptual parallel (different method, same goal); benchmark for distance recovery |
| Spectral gap and exponential decay | Hastings, Koma | 2006 | Gap => clustering => smoothness of reduced states | Core theorem for FISH-01 |
| Nachtergaele-Sims LR bounds | Nachtergaele, Sims | 2006 | LR velocity and quasi-locality framework | Infrastructure for clustering argument |
| Bures geodesics and quantum metrology | Arnaud et al. | 2023/2025 | Bures geodesics correspond to physical evolutions; optimal precision in single-parameter estimation | Confirms operational meaning of geodesic distance; validates use of Bures/Fisher geodesics |
| Efficient computation of subsystem Bures distance in TFI | arXiv:2508.09417 | 2025 | Subsystem Bures distance scales linearly with subsystem size in TFI | Validates d_Bures proportional to d_lattice for spin chains |

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
| --- | --- | --- | --- |
| NumPy | >= 2.0 | Dense matrix eigendecomposition (eigh), partial trace via tensor reshape, metric assembly | Already in project; optimal for small matrices (d <= 256) |
| SciPy | >= 1.10 | Sparse Hamiltonian construction, Lanczos ground state (eigsh) | Already in project; Lanczos is the standard for large sparse matrices |
| code/ed_entanglement.py | Existing | Ground state, partial trace, entropy | Project infrastructure from Phase 11 |

### Supporting Tools

| Tool | Purpose | When to Use |
| --- | --- | --- |
| matplotlib | Visualization of g_ij(x) profiles, eigenvalue spectra, distance ratios | Plotting results for verification and presentation |
| networkx (or manual Dijkstra) | Graph shortest path for geodesic distance | FISH-03 distance recovery test |
| pytest | Test framework | Algorithm validation against known cases |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
| --- | --- | --- |
| Eigendecomposition SLD | QuanEstimation library | Heavy dependency for a 50-line calculation; Python/Julia hybrid adds complexity |
| Manual Dijkstra | scipy.sparse.csgraph.dijkstra | Already available in scipy; no new dependency needed |
| Central finite differences | JAX automatic differentiation | Over-engineering; finite differences are exact to O(a^2) which is sufficient |

### Computational Feasibility

| Computation | Estimated Cost | Bottleneck | Mitigation |
| --- | --- | --- | --- |
| Ground state N=16 OBC | ~5 sec, 500 MB | Lanczos convergence | Use Sz=0 symmetry sector |
| Ground state N=20 OBC | ~5 min, 8 GB | Memory for state vector | Sz=0 sector halves dimension |
| All rho_Lambda(x) for N=16, \|Lambda\|=2 | < 1 sec, < 10 MB | Trivial | N/A |
| All g_ij(x) for N=16, \|Lambda\|=2 | < 1 sec, < 1 MB | Trivial | N/A |
| Cross-validation SLD vs Bures | < 1 sec per point | Fidelity computation (matrix sqrt) | Use eigh-based sqrt |
| Full pipeline N=20 (1D) | ~5-10 min total | Ground state computation | One-time cost |
| Full pipeline 4x4 (2D) | ~1 min total | Ground state | N/A |

**Installation / Setup:**
```bash
# No new packages needed. Existing numpy/scipy stack suffices.
# If networkx is needed for Dijkstra:
pip install networkx  # or: uv add networkx
```

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| --- | --- | --- | --- |
| SLD = 4 * Bures at full-rank points | Algorithm correctness | Compute both independently, compare | Agreement to machine precision (relative error < 1e-10) |
| g_ij = g_ji (symmetry) | Metric is symmetric | Check g - g^T at each point | \|\|g - g^T\|\| < 1e-12 |
| g_ij positive semidefinite | Metric is a valid Riemannian metric | Compute eigenvalues of g at each point | All eigenvalues >= 0 |
| PBC gives g = 0 | Translation symmetry correctly handled | Compute g on PBC lattice | g = 0 identically (to machine precision) |
| Trace preservation | rho_Lambda is a valid density matrix | Check Tr(rho) = 1 and rho >= 0 at every x | Tr = 1 +/- 1e-14; all eigenvalues >= 0 |
| Hermiticity of rho | Density matrix is Hermitian | Check rho - rho^dagger at every x | \|\|rho - rho^dagger\|\| < 1e-14 |
| Tensor covariance under site relabeling | g_ij transforms as rank-2 covariant tensor | Compute g in left-to-right and right-to-left orderings; verify g'(y) = J^T g(x) J | Agreement to machine precision |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| --- | --- | --- | --- |
| Pure state limit | \|Lambda\| -> N (entire system) | g_F -> 4 * g_{Fubini-Study} = 0 (single state, no manifold) | Provost-Vallee 1980 |
| Product state limit | Uncorrelated ground state (e.g., strong field) | g_ij = sum of single-site Fisher metrics | Standard |
| TFI critical point | Transverse-field Ising at h/J = 1 | Fisher metric curvature diverges | Zanardi et al. 2007 |
| Two-site exact | N=4, \|Lambda\|=2, Heisenberg OBC | Analytically computable | Direct calculation |
| Translation-invariant PBC | Any PBC lattice | g = 0 identically | Symmetry argument |

### Numerical Validation

| Test | Method | Tolerance | Reference Value |
| --- | --- | --- | --- |
| SLD vs Bures agreement | Compare at every lattice point | Relative error < 1e-10 | g_F = 4 g_B exactly |
| Metric symmetry | g_ij - g_ji | < 1e-12 | 0 |
| Positive eigenvalues (bulk) | np.linalg.eigvalsh(g) > 0 | lambda_min > 0 at interior points | Positive (value depends on system) |
| Distance ratio constancy | std(d_Fisher/d_lattice) / mean | < 0.1 for N >= 16 | Approximately constant in bulk |
| Finite-size scaling | g(N) extrapolation N=8,12,16,20 | Monotone convergence | g_bulk(N) -> g_bulk(infinity) |

### Red Flags During Computation

- **g_ij has negative eigenvalues in the bulk:** Indicates a bug in the SLD computation or eigenvalue threshold is too aggressive. The SLD Fisher metric is positive semidefinite by construction.
- **SLD and Bures disagree at full-rank points:** Algorithm bug. They must agree to factor of 4 at full-rank points.
- **g_ij is identically zero on OBC:** Possible bug: may be accidentally using translation-invariant state, or subsystem extraction is wrong.
- **Eigenvalues of rho are negative:** Partial trace implementation error. rho must be positive semidefinite by construction.
- **d_Fisher/d_lattice ratio varies wildly in the bulk:** Finite-size effects too large, or subsystem size |Lambda| is too large relative to N.
- **Metric blows up at specific sites:** Rank change in rho_Lambda(x); switch to Bures metric at that point.

## Common Pitfalls

### Pitfall 1: PBC Translation Invariance Kills the Metric

**What goes wrong:** On a periodic lattice with translation-invariant ground state, rho_Lambda(x) is the same for all x, so d_i rho = 0 and g_ij = 0 everywhere. The geometry is trivially flat.

**Why it happens:** PBC enforces exact discrete translation symmetry. The ground state is an eigenstate of the translation operator. All reduced density matrices are related by the same unitary permutation.

**How to avoid:** Use OBC exclusively for the physics. PBC only as a sanity check (expect g = 0).

**Warning signs:** g_ij = 0 or very small compared to expectations.

**Recovery:** Switch to OBC. This is already the project requirement.

### Pitfall 2: Rank-Deficiency at Generic Points

**What goes wrong:** If rho_Lambda(x) drops rank as x varies (some eigenvalue crosses zero), the SLD Fisher metric diverges at that point. The metric "blows up" and cannot be evaluated.

**Why it happens:** For small subsystems in strongly correlated states, the rank of rho can change with position. In Neel-ordered phases, sublattice magnetization can make rho nearly rank-1 on one sublattice.

**How to avoid:** (1) Verify rho is full-rank at every interior point before computing g. (2) If rank-deficient, use Bures metric (which is continuous through rank changes per Safranek 2017). (3) Coarse-grain over unit cells to average out sublattice effects.

**Warning signs:** Very large g_ij values (orders of magnitude above typical); very small eigenvalues of rho (< 1e-6).

**Recovery:** Switch to Bures metric at affected points. Report which points are rank-deficient and why.

### Pitfall 3: Sublattice Alternation in Neel Phase

**What goes wrong:** For antiferromagnets with Neel order, rho_Lambda at even sites differs systematically from odd sites (different sublattice magnetization). The Fisher metric shows large even/odd oscillations that obscure the smooth geometric signal.

**Why it happens:** Neel order breaks the translation-by-one symmetry while preserving translation-by-two. The physics alternates on the scale of one lattice site.

**How to avoid:** (1) Coarse-grain: define the metric on the unit cell (two sites) rather than individual sites. (2) Separate analysis: compute g on even sublattice and odd sublattice independently, then compare. (3) For distance recovery: use same-sublattice distances.

**Warning signs:** g_ij(x) alternates between two very different values at consecutive sites.

**Recovery:** Coarse-grain over unit cells. This is a physical effect (the "lattice spacing" for the metric should be the unit cell, not the bare site spacing).

### Pitfall 4: Subsystem Size Too Large or Too Small

**What goes wrong:** If |Lambda| is too large (> N/3), rho approaches a pure state and g degenerates. If |Lambda| is too small (= 1), the metric may not capture spatial structure.

**Why it happens:** For |Lambda| approaching N, the partial trace removes very little; the reduced state is nearly pure. For |Lambda| = 1, the single-site reduced state has limited information about the spatial correlations.

**How to avoid:** Use |Lambda| = 2 to 4 for N = 8-20. The sweet spot is |Lambda| = 2 (4x4 density matrices: cheap, structurally rich enough for 1D) or |Lambda| = 4 (16x16: captures more spatial structure, still cheap).

**Warning signs:** g eigenvalues approaching zero at all points (subsystem too large); g too uniform (subsystem too small, missing structure).

**Recovery:** Systematic scan of |Lambda| = 2, 3, 4 to find optimal subsystem size. Report results for multiple sizes.

### Pitfall 5: Confusing Parameter-Space vs Position-Space Fisher Metric

**What goes wrong:** The Zanardi et al. 2007 work computes the Fisher metric on the space of coupling constants (parameter manifold). Phase 32 needs the Fisher metric on the space of lattice positions (physical space). These are different manifolds with different metrics.

**Why it happens:** Both use "Fisher metric on quantum states" but parametrize the state family differently. Parameter-space: vary H(lambda), track ground state. Position-space: fix H, vary which subsystem is traced out.

**How to avoid:** Always be explicit about the parametrization. The Phase 32 metric is parametrized by lattice position x, not by Hamiltonian parameters.

**Warning signs:** Using parameter derivatives dH/dlambda instead of subsystem shifts.

**Recovery:** Verify the parametrization is lattice position, not coupling constants.

## Level of Rigor

**Required for this phase:** Physicist's proof for the analytical results; exact numerical computation for the computational checks.

**Justification:** The smoothness theorem (FISH-01) follows from the established Hastings-Koma theorem applied to a standard lattice system -- this is a "plug and play" application of a rigorous result, so the argument itself is rigorous given the theorem's assumptions. The positive-definiteness proof (FISH-02) requires showing that the SWAP ground state with OBC produces full-rank reduced density matrices -- this can be established analytically for generic cases and verified numerically for specific cases. The distance recovery (FISH-03) is an asymptotic statement that can be proved by showing the bulk Fisher metric is approximately constant, with corrections controlled by finite-size scaling.

**What this means concretely:**

- Smoothness theorem: state the Hastings-Koma theorem precisely, verify its hypotheses for the SWAP Hamiltonian, and derive the smoothness bound as a corollary. This is rigorous.
- Positive-definiteness: prove for generic non-degenerate ground states; verify numerically for SWAP. If analytical proof is difficult, state as a numerical observation with finite-size scaling evidence.
- Distance recovery: prove the bulk-constancy of g analytically (from translation invariance away from boundaries), compute the constant numerically, and verify d_Fisher/d_lattice -> const with increasing system size.
- All numerical results: exact to machine precision (the only approximation is Lanczos convergence, already validated at 1e-12).

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| --- | --- | --- | --- |
| Classical Fisher information on measurement outcomes | Quantum (SLD) Fisher information on density matrices | Braunstein-Caves 1994 | SLD Fisher metric is the correct quantum generalization; maximizes over all measurements |
| Fubini-Study metric on pure states | SLD/Bures metric on mixed states | Petz 1996; Braunstein-Caves 1994 | Mixed state metric is essential for reduced states (our case) |
| Parameter-space Fisher metric (coupling constants) | Position-space Fisher metric (lattice position) | Cao-Carroll-Michalakis 2017 (conceptual); this project (specific implementation) | Position parametrization directly gives spatial geometry |
| Matrix logarithm computation of QFI | Eigendecomposition SLD formula | Always (numerical best practice) | Avoids catastrophic failure at rank-deficient points |

**Superseded approaches to avoid:**

- **Matrix logarithm approach to QFI:** Never use scipy.linalg.logm for Fisher metric computation. The eigendecomposition formula is strictly superior in all cases. People still sometimes use it because some textbooks present QFI in terms of log(rho), but this is numerically disastrous.
- **Wigner-Yanase information as Fisher metric substitute:** Wigner-Yanase skew information I_WY(rho, A) = -(1/2)Tr[sqrt(rho), A]^2 is related but NOT equal to the SLD Fisher metric. It is a monotone metric but not the maximal one. Using it instead of SLD gives a different (smaller) metric. Avoid unless specifically needed.

## Open Questions

1. **Is rho_Lambda(x) full-rank at all interior lattice points for the SWAP ground state on OBC?**
   - What we know: For generic Hamiltonians with non-degenerate ground state, rho_Lambda should be full-rank if |Lambda| is small enough and the system has sufficient entanglement. Numerically verified for small systems in prior work.
   - What's unclear: Whether this holds for all system sizes and all interior positions. Edge effects may cause rank deficiency near boundaries.
   - Impact on this phase: If rho is rank-deficient at generic interior points, FISH-02 must pivot to Bures metric (backtracking trigger).
   - Recommendation: Verify numerically for N=8,12,16,20. If full-rank at all interior points, proceed with SLD. If not, document where rank drops and use Bures there.

2. **How does the Neel sublattice alternation affect the Fisher metric in d >= 2?**
   - What we know: Neel order causes rho to alternate between sublattices. In 1D this is manageable (coarse-grain over pairs). In 2D the pattern is more complex.
   - What's unclear: Whether coarse-graining over unit cells produces a smooth, positive-definite metric in 2D.
   - Impact on this phase: Affects FISH-02 (positive-definiteness may require coarse-graining) and FISH-03 (distance recovery on which sublattice?).
   - Recommendation: First analyze 1D (simpler), then extend to 2D 4x4. Coarse-grain over unit cells if alternation is large.

3. **What is the asymptotic constant in d_Fisher ~ const * d_lattice?**
   - What we know: The constant should depend on the Hamiltonian parameters (J, subsystem size |Lambda|) and the correlation length xi. In the bulk of a gapped system, g_ij(x) approaches a constant g_bulk, and the asymptotic ratio is const = sqrt(g_bulk).
   - What's unclear: Exact analytical expression for g_bulk in terms of J, |Lambda|, and xi. Whether the constant has a universal form or depends on microscopic details.
   - Impact on this phase: FISH-03 requires the constant to be positive (nonzero) and expressible in terms of Hamiltonian parameters. The exact value is a deliverable.
   - Recommendation: Extract numerically from finite-size scaling. Derive analytically if possible from the bulk Fisher metric value. At minimum, verify positivity and monotone convergence with N.

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| --- | --- | --- | --- |
| SLD Fisher metric at all points | Rank-deficiency at generic interior points | Bures metric throughout (continuous at rank changes) | LOW -- Bures computation is already implemented as cross-validation |
| OBC Fisher metric positive-definite | Boundary effects contaminate too many sites | Larger systems (N=20+) or symmetry sector reduction | MEDIUM -- need to optimize for larger N |
| Distance recovery in 1D | 1D metric is scalar (trivially proportional to lattice distance) | Test on 2D lattice (4x4) where metric is 2x2 tensor | MEDIUM -- 2D adds complexity but no new algorithms |
| Eigendecomposition approach | Numerical instability for near-degenerate eigenvalues | Regularized Bures metric (Safranek continuous formula) | LOW -- already implemented |
| Smoothness from exponential clustering | System is gapless (Heisenberg AFM in d >= 2) | Algebraic smoothness argument (power-law decay is still C^infinity) | MEDIUM -- Phase 33 handles this; Phase 32 can state the result conditionally |

**Decision criteria:** If SLD Fisher metric fails to be positive-definite at > 20% of interior lattice points (due to rank deficiency), abandon SLD and switch entirely to Bures metric. The Bures metric is always well-defined and continuous.

## Sources

### Primary (HIGH confidence)

- [Braunstein-Caves, PRL 72, 3439 (1994)](https://link.aps.org/doi/10.1103/PhysRevLett.72.3439) - SLD Fisher metric definition, operational meaning, positive semidefiniteness
- [Hastings-Koma, CMP 265, 781 (2006), arXiv:math-ph/0507008](https://arxiv.org/abs/math-ph/0507008) - Spectral gap implies exponential clustering; backbone of smoothness argument
- [Nachtergaele-Sims, CMP 265, 119 (2006), arXiv:math-ph/0506030](https://arxiv.org/abs/math-ph/0506030) - LR bounds and exponential clustering theorem
- [Safranek, PRA 95, 052320 (2017), arXiv:1612.04581](https://arxiv.org/abs/1612.04581) - QFI discontinuities at rank changes; Bures as continuous extension
- [Petz, LAA 244, 81 (1996)](https://doi.org/10.1016/0024-3795(94)00211-8) - Classification of quantum monotone metrics; SLD is maximal
- [Provost-Vallee, CMP 76, 289 (1980)](https://link.springer.com/article/10.1007/BF02193559) - Riemannian structure on manifold of quantum states

### Secondary (MEDIUM confidence)

- [Zanardi-Giorda-Cozzini, PRL 99, 100603 (2007), arXiv:quant-ph/0701061](https://arxiv.org/abs/quant-ph/0701061) - Fisher metric and QPTs; benchmark for TFI
- [Liu-Peng-Yuan, J. Phys. A 53, 023001 (2020), arXiv:1907.08037](https://arxiv.org/abs/1907.08037) - QFIM computation review; arbitrary-rank formula
- [Liu et al., arXiv:1312.6910](https://arxiv.org/abs/1312.6910) - QFI for density matrices with arbitrary ranks
- [Cao-Carroll-Michalakis, PRD 95, 024031 (2017), arXiv:1606.08444](https://arxiv.org/abs/1606.08444) - Space from Hilbert space; conceptual parallel for distance recovery
- [Calabrese-Cardy, JSTAT P06002 (2004)](https://arxiv.org/abs/hep-th/0405152) - Entanglement entropy in 1D CFT; scaling context
- [Arnaud et al., arXiv:2308.08706 (2023)](https://arxiv.org/abs/2308.08706) - Bures geodesics and quantum metrology; operational meaning of geodesic distance

### Tertiary (LOW confidence)

- [Matsueda, arXiv:1310.1831 (2013)](https://arxiv.org/abs/1310.1831) - Emergent GR from Fisher metric (suggestive but not rigorous; useful for conceptual motivation only)
- [arXiv:2508.09417 (2025)](https://arxiv.org/abs/2508.09417) - Efficient computation of subsystem Bures distance in TFI chain (recent, single source; validates distance-lattice proportionality)

## Metadata

**Confidence breakdown:**

- Mathematical framework: HIGH - SLD Fisher metric, eigendecomposition algorithm, Hastings-Koma theorem are all textbook-level established results
- Standard approaches: HIGH - Eigendecomposition SLD is the universally recommended algorithm; implementation is straightforward with existing infrastructure
- Computational tools: HIGH - NumPy/SciPy with existing ed_entanglement.py; no new dependencies needed; compute budget is modest (minutes on laptop)
- Validation strategies: HIGH - Multiple independent cross-checks (SLD vs Bures, PBC symmetry, pure state limit, TFI benchmark); well-defined success/failure criteria

**Research date:** 2026-03-29
**Valid until:** Indefinite for mathematical results; tool versions may change but algorithms are stable

## Caveats and Alternatives

**Self-critique:**

1. **Assumption that might be wrong:** I assume the SWAP ground state on OBC produces full-rank reduced density matrices at all interior points. This is physically reasonable (entanglement spreads eigenvalues across the reduced state spectrum) but has not been proved for the specific SWAP Hamiltonian. If the ground state has unusual symmetry properties that force eigenvalue degeneracies or zero eigenvalues, the SLD approach needs modification. Mitigation: numerical verification at N=8,12,16 is cheap and should be done first.

2. **Alternative dismissed perhaps too quickly:** The Wigner-Yanase information metric is an alternative monotone metric that is always well-defined (no rank issues) and may have simpler analytical properties. I dismissed it because the SLD Fisher metric is the standard (maximal monotone metric, operational meaning via Cramer-Rao). However, if rank-deficiency turns out to be widespread, Wigner-Yanase might be simpler than the Bures fallback. Counter-argument: Bures is already implemented as cross-validation, so the switching cost is zero.

3. **Limitation I may be understating:** The distance recovery claim (FISH-03) is only meaningful in the bulk, far from boundaries. For N=16 with |Lambda|=2, the "bulk" is only about 10 sites (after excluding boundary regions of width ~xi on each side). If xi is large (comparable to N), there is no bulk, and FISH-03 cannot be tested. For the Heisenberg chain in 1D (gapless, xi = infinity formally), this is a real concern. Mitigation: FISH-03 requires |x-y| >> xi, so it is automatically restricted to gapped systems in Phase 32; the gapless case is Phase 33 territory.

4. **Simpler method overlooked?** For 1D systems, the Bures distance d_B(rho(x), rho(y)) could be computed directly without constructing the full metric tensor -- just compute fidelity between all pairs. This avoids the finite-difference derivative and gives the distance directly. I chose the metric tensor approach because (a) it generalizes to 2D, (b) it gives the full tensorial structure needed downstream, and (c) it is the standard approach in the literature. But for a quick sanity check of distance recovery, direct Bures distance is simpler. This is now documented as Approach 3.

5. **Would a specialist disagree?** A quantum information theorist might argue that the SLD Fisher metric is only one of infinitely many monotone metrics (Petz classification), and the choice of metric is not physically motivated by the lattice geometry alone -- it is motivated by estimation theory. The operational meaning (Cramer-Rao bound) is about parameter estimation, not about spatial geometry per se. The identification of the SLD metric with "the" spatial metric is a physical assumption, not a theorem. This is fair -- and it is exactly what Phase 32 is testing: does this specific metric produce a sensible spatial geometry?
