# Methods Research

**Domain:** Information geometry on quantum lattice states / Continuum limit from finite-dimensional observer
**Researched:** 2026-03-29
**Confidence:** MEDIUM

### Scope Boundary

METHODS.md covers analytical and numerical PHYSICS methods for v9.0: closing Paper 6 gaps via information-geometric continuum limit. It does NOT cover software tools (see COMPUTATIONAL.md) or the theoretical landscape (see PRIOR-WORK.md).

**What is NEW vs v8.0:** v8.0 addressed Gap C (algebraic complexification forcing). v9.0 addresses the remaining Paper 6 gaps: (1) continuum limit, (2) exponential decay/spectral gap in d>=2, (3) Fisher information geometry on lattice states, (4) Lorentzian signature emergence, (5) connection to Wightman axioms. The existing ED infrastructure (N=8-20, code/ed_entanglement.py) and Lieb-Robinson bounds are inputs, not deliverables.

---

## Recommended Methods

### Analytical Methods

| Method | Purpose | Why Recommended |
|--------|---------|-----------------|
| Quantum Fisher information metric on reduced density matrices | Extract Riemannian geometry from lattice ground states parametrized by subsystem position | Directly addresses Gap 1: provides the geometric object (metric tensor) that must converge in the continuum limit |
| Nachtergaele-Sims exponential clustering theorem | Prove spectral gap implies exponential decay of correlations for Heisenberg AFM | Standard rigorous method; already cited in Paper 6; extends the Lieb-Robinson framework already in the project |
| Reflection positivity + infrared bounds (Dyson-Lieb-Simon / Kennedy-Lieb-Shastry) | Prove Neel order / long-range order for d>=2 Heisenberg AFM | The ONLY rigorous method for establishing symmetry breaking in quantum spin systems; needed to close the d>=2 gap |
| Osterwalder-Schrader reconstruction | Convert Euclidean lattice correlators to Lorentzian Wightman functions | Standard path from lattice to QFT axioms; well-developed for constructive field theory |
| Modular flow / Connes-Rovelli thermal time | Extract Lorentzian causal structure from the Fisher-Riemannian geometry | Already used in Paper 6 for MVEH identification; extends naturally to the Lorentzian signature question |

### Numerical Methods

| Method | Purpose | Convergence | Cost Scaling | Implementation |
|--------|---------|-------------|-------------|----------------|
| Exact diagonalization + QFI extraction | Compute Fisher metric components on N=8-20 lattice | Finite-size scaling ~ O(1/N) corrections | O(2^N) per state, O(d^3) per QFIM entry | Extend existing code/ed_entanglement.py |
| Symmetric logarithmic derivative (SLD) method | Compute quantum Fisher information matrix for mixed states | Exact for given density matrix | O(d^3) where d = dim(rho_A) | From scratch (straightforward linear algebra) |
| DMRG with Uhlmann gauge | Extend Fisher metric computation to N~100-1000 | Exponential in bond dimension chi | O(N chi^3 d^2) | Requires ITensor or TeNPy + custom gauge layer |
| Finite-difference position derivative of rho_A | Numerically estimate d(rho_A)/dx for Fisher metric | O(h^2) for central differences | O(2^N) per shift | Trivial extension of ED |
| Finite-size scaling extrapolation | Extract continuum-limit Fisher metric from sequence of lattice sizes | Power-law in 1/N | Negligible (post-processing) | Standard curve fitting |

### Computational Tools

| Tool | Version | Purpose | Why |
|------|---------|---------|-----|
| NumPy/SciPy | >=1.20/>=1.10 | ED infrastructure, eigensolvers, linear algebra | Already in project; Lanczos eigsh for sparse Hamiltonians |
| SymPy | latest | Symbolic verification of Fisher metric identities | Already in project |
| ITensor (Julia) or TeNPy (Python) | ITensor v0.6+ / TeNPy 1.0+ | DMRG for N>20 | Standard tensor network libraries for 1D spin chains |

---

## Method Details

### Method 1: Quantum Fisher Information Metric on Reduced Density Matrices

**What:** For a lattice ground state |psi>, define the family of reduced density matrices rho_A(x) parametrized by the position x of subsystem A on the lattice. The quantum Fisher information metric (QFIM) g_{mu nu}(x) on this parameter space defines a Riemannian metric that encodes the information-geometric structure of the ground state. In the continuum limit, this metric must reproduce (or relate to) the emergent spacetime metric.

**Mathematical basis:**

The quantum Fisher information for a parametrized family rho(theta) is:

    g_{mu nu}(theta) = (1/2) Tr[ rho(theta) {L_mu, L_nu} ]

where L_mu is the symmetric logarithmic derivative (SLD) defined by:

    d(rho)/d(theta^mu) = (1/2) (rho L_mu + L_mu rho)

This is a Lyapunov equation for L_mu. For a density matrix with spectral decomposition rho = sum_k p_k |k><k|, the SLD matrix elements are:

    <m| L_mu |n> = 2 <m| d(rho)/d(theta^mu) |n> / (p_m + p_n)    [when p_m + p_n > 0]

The QFIM equals 4 times the Bures metric: g_{mu nu} = 4 * g^{Bures}_{mu nu}.

For the lattice application, the parameter theta^mu = x^mu labels the lattice position of the subsystem A. On a d-dimensional lattice with spacing a, the derivative d(rho_A)/d(x^mu) is approximated by the finite difference:

    d(rho_A)/d(x^mu) ~ [rho_A(x + a e_mu) - rho_A(x - a e_mu)] / (2a)

where e_mu is the unit vector in direction mu. Each shifted rho_A comes from tracing out the complement of a spatially shifted subsystem in the same global ground state.

**Convergence:** The SLD computation is exact for a given rho_A. The finite-difference derivative has O(a^2) discretization error. The leading finite-size correction to the Fisher metric on a 1D chain scales as O(1/N) from Calabrese-Cardy type corrections. In d>=2, finite-size corrections depend on whether the system is gapped (exponential convergence) or gapless (power-law).

**Known failure modes:**
- Rank changes in rho_A: When eigenvalues of rho_A cross zero as x varies, the QFIM diverges (Seveso et al., PRA 95, 052320, 2017). On a gapped system this should not happen for small shifts, but near quantum phase transitions the Fisher metric can diverge.
- Translation invariance on PBC: With periodic boundary conditions and a translation-invariant ground state, rho_A(x) is x-independent and the Fisher metric is identically zero. Must use OBC or break translation invariance (e.g., by choosing a fixed reference region and varying a probe region).
- SLD ill-conditioning: When p_m + p_n is very small, the SLD matrix element (2 <m|drho|n>)/(p_m + p_n) is numerically unstable. Regularize by setting elements to zero when p_m + p_n < epsilon (typically 1e-12).

**Benchmarks:** The Fisher metric for the transverse-field Ising model at criticality has been computed and shown to diverge at the critical point (Zanardi et al., PRA 76, 032311, 2007). For 1D CFTs, the Fisher metric on reduced states should reproduce the Zamolodchikov metric on the conformal manifold, providing a benchmark.

**Implementation notes:**

```python
def compute_qfi_metric(rho_A_list, directions, spacing):
    """
    Compute QFIM g_{mu nu} from a list of rho_A at shifted positions.

    rho_A_list: dict mapping direction -> (rho_plus, rho_minus)
    directions: list of spatial direction indices
    spacing: lattice spacing a

    Returns: g_{mu nu} as a dxd array
    """
    # 1. Compute drho/dx^mu via central difference
    # 2. Diagonalize rho_A at central position: rho = sum p_k |k><k|
    # 3. For each mu, solve Lyapunov eqn for L_mu
    # 4. g_{mu nu} = (1/2) Tr[rho {L_mu, L_nu}]
    # Regularize: skip matrix elements with p_m + p_n < eps
```

**Cost:** For N-site lattice: O(2^N) for ground state, O(2^|A|)^3 for SLD per direction. For |A|=4 on N=16, the SLD step is negligible (16x16 matrices). For |A|=8 on N=20, SLD is 256x256 -- still fast. The bottleneck is ground state computation.

**Confidence:** MEDIUM-HIGH for the method itself; MEDIUM for whether it converges to a smooth metric in the continuum limit.

**Key references:**
- Zanardi, Giorda, Cozzini, "Information-theoretic differential geometry of quantum phase transitions," PRL 99, 100603 (2007), arXiv:quant-ph/0701061
- Matsueda, "Emergent General Relativity from Fisher Information Metric," arXiv:1310.1831 (2013)
- Liu, Peng, Yuan, "Quantum Fisher information matrix and multiparameter estimation," J. Phys. A 53, 023001 (2020), arXiv:1907.08037

---

### Method 2: Exponential Clustering via Nachtergaele-Sims Framework

**What:** Prove that for the Heisenberg AFM in d>=2, a nonvanishing spectral gap above the ground state implies exponential decay of connected correlation functions. Combined with known or conjectured results on the spectral gap, this establishes the exponential clustering needed for a smooth continuum limit.

**Mathematical basis:**

The Nachtergaele-Sims theorem (CMP 265, 119, 2006) states:

**Theorem:** Let H be a local Hamiltonian on a lattice with Lieb-Robinson velocity v_LR and spectral gap Delta > 0 above the ground state. Then for any local observables A, B supported on regions X, Y:

    |<psi_0| A B |psi_0> - <psi_0|A|psi_0> <psi_0|B|psi_0>|
        <= C ||A|| ||B|| min(|X|, |Y|) exp(-mu * dist(X,Y))

where mu = Delta / (2 v_LR) and C is a constant depending on the lattice geometry.

The key chain of logic for d>=2 Heisenberg AFM:

1. **Neel order exists** (Dyson-Lieb-Simon 1978 for S>=1 d>=3; Kennedy-Lieb-Shastry 1988 for S=1/2 d=3, partial for d=2 S>=3/2): The ground state breaks SU(2) symmetry spontaneously in d>=2 (rigorously proved for S>=3/2 in d=2).

2. **Spectral gap above Neel ground state:** The broken-symmetry ground state is separated from the magnon excitations by a gap. For the anisotropic (easy-axis) Heisenberg model in d>=2, the gap is rigorously established. For the isotropic SU(2) model, there are gapless Goldstone modes (spin waves) in the infinite-volume limit, but the finite-lattice ground state has a gap that scales as ~ 1/N^{1/d} (tower of states).

3. **SU(2) complication for n=2:** The isotropic spin-1/2 Heisenberg AFM in d=2 is the critical case. Neel order is believed to exist based on QMC evidence (Sandvik, PRL 104, 137201, 2010) and spin-wave theory, but a rigorous proof for S=1/2 in d=2 remains open. Kennedy-Lieb-Shastry provided sufficient conditions (infrared bounds) but did not fully close the proof.

**The honest status for d=2, n=2 (SU(2)):**
- Neel order: STRONG numerical evidence, no rigorous proof for S=1/2
- Spectral gap: NO in the thermodynamic limit (Goldstone modes), YES on any finite lattice
- Exponential clustering: YES on any finite lattice (finite gap -> exponential decay), but the clustering length diverges as system size -> infinity
- For the continuum limit argument: need clustering on length scales a << xi << L where xi is the correlation length and L is the system size. This is satisfied as long as Neel order exists, because xi remains finite even though the true gap vanishes

**What can be rigorously proved:**
- For n>=3 (SU(n>=3)): Haldane gap exists in d=1, strict area law, exponential clustering. In d>=2, stronger results available.
- For n=2 in d>=2: On any finite lattice, exponential clustering holds with clustering length ~ v_LR / gap ~ N^{1/d}. In the thermodynamic limit, algebraic decay replaces exponential for the transverse correlations (Goldstone modes), but the longitudinal correlations remain short-ranged.
- For n=2 in d>=3: Full Neel order is rigorously proved (KLS 1988). Combined with the broken-symmetry gap (above Goldstone modes), exponential clustering holds for connected correlations of order-parameter-aligned observables.

**Recommended approach:** Proceed in two tiers:
1. **Rigorous tier:** State the result for n>=3 (gapped, exponential clustering, textbook). For n=2 d>=3, state KLS + Nachtergaele-Sims.
2. **Physical-argument tier:** For n=2 d=2, state the numerical evidence for Neel order (QMC, series expansions, DMRG) and argue that exponential clustering of connected correlations follows from the staggered magnetization being nonzero, even though the exact gap vanishes. This is standard condensed matter reasoning but not rigorous.

**Cost:** No computation needed -- this is a literature assembly problem. Time: 5-10 hours to write the rigorous statements carefully.

**Confidence:** HIGH for n>=3 and n=2 d>=3 (textbook/proved). MEDIUM for n=2 d=2 (strong numerical evidence, no proof).

**Key references:**
- Nachtergaele & Sims, "Lieb-Robinson bounds and the exponential clustering theorem," CMP 265, 119 (2006), arXiv:math-ph/0506030
- Hastings, "Spectral gap and exponential decay of correlations," CMP 265, 781 (2006), arXiv:math-ph/0604015
- Kennedy, Lieb & Shastry, "Existence of Neel order in some spin-1/2 Heisenberg antiferromagnets," J. Stat. Phys. 53, 1019 (1988)
- Dyson, Lieb & Simon, "Phase transitions in quantum spin systems with isotropic and nonisotropic interactions," J. Stat. Phys. 18, 335 (1978)
- Affleck, Kennedy, Lieb & Tasaki, "Valence bond ground states in isotropic quantum antiferromagnets," CMP 115, 477 (1988)

---

### Method 3: Smoothness of Reduced States as a Function of Position

**What:** Establish that rho_A(x) depends smoothly on the lattice position x (after embedding the lattice in R^d), so that the Fisher information metric is well-defined and smooth.

**Mathematical basis:**

On a translation-invariant lattice with OBC or in the bulk of a PBC lattice, smoothness of rho_A(x) follows from exponential clustering:

**Lemma (smoothness from exponential clustering):** Let |psi> be the ground state of a gapped local Hamiltonian on a lattice of spacing a. Let A(x) denote a subsystem of fixed shape centered at position x. Then:

    || rho_A(x + delta) - rho_A(x) || <= C |delta|/a * exp(-dist(boundary shift) / xi)

where xi is the correlation length and || . || is the trace norm. The bound follows because shifting A by delta changes which boundary bonds are cut, and the sensitivity to distant bonds is exponentially suppressed by clustering.

More precisely, for a gapped Hamiltonian with exponential clustering at rate mu:
1. rho_A(x) as a function of discrete lattice position x is well-defined
2. Finite differences Delta rho_A / Delta x^mu are bounded by C * exp(-mu * dist_min) where dist_min is the minimum distance from the changed boundary to the nearest site
3. After embedding the lattice in R^d and interpolating (or working with the discrete Fisher metric), the resulting g_{mu nu} is a positive semidefinite matrix at each lattice point

**For gapless systems (n=2, d=1):** The 1D Heisenberg chain is gapless with algebraic correlations. The reduced state still varies smoothly with position -- the correlation functions are C^infty as functions of position even for algebraic decay -- but the Fisher metric will have different scaling properties (logarithmic corrections from the CFT). The Calabrese-Cardy formula provides the explicit form.

**For gapless systems (n=2, d=2):** If Neel order exists, the transverse correlations decay algebraically (Goldstone modes) while the longitudinal correlations are short-ranged. The reduced state rho_A(x) still varies smoothly with x because the algebraic decay is still infinitely differentiable as a function of distance. The Fisher metric components will be finite because the variation of rho_A with position is controlled by the boundary correlations, which are finite even when the bulk correlations are algebraic.

**Numerical check protocol:**
1. Compute rho_A(x) for x = 0, 1, 2, ..., N-|A| on a 1D chain
2. Compute || rho_A(x+1) - rho_A(x) ||_trace for each x
3. Fit to exponential decay vs x near boundaries, constant in bulk
4. Compute second differences || rho_A(x+1) - 2 rho_A(x) + rho_A(x-1) ||_trace
5. Verify these are O(a^2) times the first differences (smoothness check)

**Cost:** Negligible beyond existing ED computation. Each rho_A is already available from the ground state.

**Confidence:** HIGH for gapped systems (rigorous exponential clustering -> smoothness). MEDIUM for n=2 d=1 (gapless but CFT controls everything). MEDIUM for n=2 d=2 (conditional on Neel order).

**Key references:**
- Hastings & Koma, "Spectral gap and exponential decay of correlations," CMP 265, 781 (2006)
- Calabrese & Cardy, "Entanglement entropy and quantum field theory," J. Stat. Mech. P06002 (2004), arXiv:hep-th/0405152

---

### Method 4: From Fisher-Riemannian to Lorentzian Structure

**What:** The Fisher information metric is inherently Riemannian (positive definite). To connect to spacetime physics, we need Lorentzian signature. This method establishes the connection.

**Mathematical basis:**

There are three complementary approaches, in order of rigor:

**Approach A: Modular flow defines the time direction (recommended)**

The Connes-Rovelli thermal time hypothesis (already used in Paper 6 for MVEH) identifies physical time with the modular flow of the equilibrium state. The modular Hamiltonian K_A = -ln(rho_A) generates a one-parameter automorphism group sigma_t that acts as "time evolution" relative to the subsystem A.

The key insight: the Fisher metric g_{mu nu} gives the SPATIAL part of the emergent metric. The TIME direction is identified with the modular flow. The resulting spacetime metric has the form:

    ds^2 = -N^2 dt^2 + g_{mu nu} dx^mu dx^nu

where N is the lapse function determined by the modular Hamiltonian normalization, and dt is the modular time parameter. This naturally produces Lorentzian signature because the time direction is DISTINGUISHED by the modular flow, not derived from the Fisher metric.

This is the approach Paper 6 already uses implicitly. Making it explicit with the Fisher metric fills the gap.

**Approach B: Wick rotation of Euclidean correlators**

If lattice correlators satisfy reflection positivity (Osterwalder-Schrader axiom), they can be analytically continued to Lorentzian signature via Wick rotation t -> -i*tau. The reconstructed Wightman functions define the Lorentzian theory.

For the Heisenberg model: the transfer matrix formalism provides Euclidean time correlators. Reflection positivity holds for the Heisenberg model on a bipartite lattice (the interaction is antiferromagnetic, and the Hamiltonian is reflection-positive after a spin-flip transformation on one sublattice).

**Approach C: Emergent Lorentzian signature from noncommutative geometry**

Recent work (arXiv:2512.15450, 2024) shows that extending a spectral triple with almost-commutative structure induces emergence of pseudo-Riemannian (Lorentzian) signature from a Riemannian background. This connects to the Connes approach and provides a mathematical framework for signature emergence.

Also relevant: Baldazzi et al. (PRD 87, 065020, 2013) show that Lorentzian signature can emerge as a dynamical property from a fundamentally Euclidean system, with the signature determined by the dynamics rather than put in by hand.

**Recommended approach:** Use Approach A (modular flow) as the primary method because it is already consistent with Paper 6's framework. Use Approach B (OS reconstruction) as the rigorous verification path. Approach C is the most mathematically sophisticated but requires noncommutative geometry machinery not yet in the project.

**What must be shown:**
1. The Fisher metric g_{mu nu}(x) on the lattice converges to a smooth Riemannian metric in the continuum limit (Method 1 + Method 3)
2. The modular flow sigma_t defines a timelike direction that is everywhere transverse to the spatial Fisher geometry
3. The combined (modular time, Fisher space) metric has Lorentzian signature
4. The resulting spacetime satisfies Einstein's equations (Paper 6 already does this, given the metric)

**Cost:** Approach A is conceptual/derivation work, not computational. Time: 10-20 hours. Approach B requires verifying reflection positivity numerically for the self-modeling Hamiltonian, then computing Euclidean correlators and analytically continuing. Time: 20-40 hours. Approach C is a literature study. Time: 5-10 hours.

**Confidence:** MEDIUM for Approach A (conceptually clear but new formal work needed). MEDIUM-HIGH for Approach B (standard constructive QFT, but tedious). LOW for Approach C (frontier mathematics).

**Key references:**
- Connes & Rovelli, "Von Neumann algebra automorphisms and time-thermodynamics relation in general covariant quantum theories," CMP 8, 1 (1994), arXiv:gr-qc/9406019
- Jacobson, "Entanglement equilibrium and the Einstein equation," PRL 116, 201101 (2016), arXiv:1505.04753
- Matsueda, "Emergent General Relativity from Fisher Information Metric," arXiv:1310.1831 (2013)
- Osterwalder & Schrader, "Axioms for Euclidean Green's functions," CMP 31, 83 (1973); CMP 42, 281 (1975)

---

### Method 5: Verification of Wightman Axioms for the Effective Theory

**What:** Check whether the effective QFT emerging from the lattice continuum limit satisfies the Wightman axioms (or the equivalent Osterwalder-Schrader axioms in Euclidean signature). This is the gold standard for a well-defined QFT.

**Mathematical basis:**

The Wightman axioms require:
- W0: Relativistic quantum theory (Hilbert space, Poincare covariance)
- W1: Spectral condition (energy-momentum in forward light cone)
- W2: Existence of a unique Poincare-invariant vacuum
- W3: Domain and continuity of field operators
- W4: Local commutativity (spacelike separated fields commute/anticommute)
- W5: Completeness (fields generate the full Hilbert space from the vacuum)

The Osterwalder-Schrader (OS) approach is more tractable from the lattice:
- OS0: Temperedness of Schwinger functions
- OS1: Euclidean covariance
- OS2: Reflection positivity
- OS3: Permutation symmetry
- OS4: Cluster property

**Strategy for the self-modeling lattice:**

1. **OS2 (Reflection positivity):** This is the key axiom. For the Heisenberg model on a bipartite lattice, the transfer matrix T = exp(-a H) is a positive operator. After the sublattice spin-flip trick (Dyson-Lieb-Simon), the model has a reflection-positive transfer matrix. This gives OS2.

2. **OS4 (Cluster property):** This follows from exponential clustering (Method 2) or from a mass gap.

3. **OS1 (Euclidean covariance):** This requires rotational invariance, which the lattice breaks. In the continuum limit, the lattice artifacts must be irrelevant. For the Heisenberg model in d=1, the WZW CFT has full conformal covariance, so OS1 holds in the continuum limit. For d>=2, the Neel-ordered phase has a mass gap (above Goldstone modes) and the IR effective theory is a nonlinear sigma model, which is Euclidean-covariant.

4. **OS reconstruction:** If OS0-OS4 hold, the Osterwalder-Schrader reconstruction theorem gives a Wightman QFT.

**Honest assessment:** Full verification of the OS axioms for the d>=2 Heisenberg model continuum limit is an OPEN PROBLEM in constructive field theory. The d=1 case (WZW CFT) is under much better control. For d>=2, the effective theory is the O(3) nonlinear sigma model, and constructing this as a rigorous QFT in d=2+1 is one of the open Clay Millennium problems (Yang-Mills mass gap is related but different).

**What IS achievable for this project:**
- Verify reflection positivity numerically for the self-modeling Hamiltonian on small lattices
- Verify the cluster property from exponential clustering
- State the continuum limit conjecture precisely and identify the effective theory
- Verify Wightman axioms for the FREE field limit (non-interacting approximation)
- Provide numerical evidence for convergence of lattice correlators to continuum form

**Cost:** Numerical verification of OS2 and OS4: 5-10 hours. Statement of the continuum limit conjecture: 5-10 hours. Full OS verification: INTRACTABLE (open problem in mathematical physics).

**Confidence:** HIGH for the lattice OS checks (finite lattice, computable). LOW for the full continuum limit OS verification (open problem).

**Key references:**
- Osterwalder & Schrader, CMP 31, 83 (1973); CMP 42, 281 (1975)
- Glimm & Jaffe, "Quantum Physics: A Functional Integral Point of View," Springer (1987)
- Rivasseau, "From Perturbative to Constructive Renormalization," Princeton (1991)

---

### Method 6: Numerical Computation of Fisher Metric on Small Lattices

**What:** Concrete numerical protocol to compute the quantum Fisher information metric g_{mu nu} on N=8-20 lattice ground states, extending the existing ED infrastructure.

**Mathematical basis:**

Given the ground state |psi> of the Heisenberg AFM on a d-dimensional lattice:

Step 1: Fix a subsystem shape (e.g., contiguous block of |A| sites in 1D, or square region in 2D).

Step 2: For each lattice position x of the subsystem, compute:
    rho_A(x) = Tr_{complement(A(x))} |psi><psi|

Step 3: For each spatial direction mu, compute the derivative via central differences:
    delta_mu rho_A(x) = [rho_A(x + e_mu) - rho_A(x - e_mu)] / (2a)

Step 4: Solve the SLD equation at the central position:
    delta_mu rho = (1/2)(rho L_mu + L_mu rho)

In the eigenbasis rho = sum_k p_k |k><k|:
    <m|L_mu|n> = 2 <m|delta_mu rho|n> / (p_m + p_n)  [for p_m + p_n > epsilon]
    <m|L_mu|n> = 0  [for p_m + p_n < epsilon]

Step 5: Compute the metric:
    g_{mu nu}(x) = (1/2) Tr[rho {L_mu, L_nu}]
    = sum_{m,n} (p_m * <m|L_mu|n> * <n|L_nu|m> + p_m * <m|L_nu|n> * <n|L_mu|m>) / 2
    = Re[ sum_{m,n} p_m <m|L_mu|n> <n|L_nu|m> ]  [using Hermiticity of L]

Step 6: Repeat for all positions x in the bulk (away from boundaries).

Step 7: Extract:
- Spatial profile g_{mu nu}(x) -- should be approximately constant in the bulk
- Finite-size dependence g_{mu nu}(N) -- should converge as N -> infinity
- Isotropy check: g_{xx} = g_{yy} in 2D (Heisenberg SU(2) symmetry implies rotational invariance)

**Implementation plan:**

```python
def fisher_metric_1d(N, J, A_size, boundary='OBC'):
    """
    Compute Fisher metric on 1D Heisenberg chain.

    Returns g(x) for each valid position x of subsystem A.
    In 1D there is only one spatial direction, so g is a scalar.
    """
    # 1. Build Hamiltonian and find ground state
    H = build_heisenberg_1d(N, J, boundary)
    E0, psi0 = eigsh(H, k=1, which='SA')

    # 2. For each position x (with x-1, x, x+1 valid):
    for x in range(1, N - A_size):
        rho_center = partial_trace(psi0, sites=range(x, x+A_size))
        rho_plus   = partial_trace(psi0, sites=range(x+1, x+1+A_size))
        rho_minus  = partial_trace(psi0, sites=range(x-1, x-1+A_size))
        drho = (rho_plus - rho_minus) / 2.0  # a=1 lattice units

        # 3. Diagonalize rho_center
        p, U = eigh(rho_center)

        # 4. Compute SLD in eigenbasis
        drho_eig = U.T.conj() @ drho @ U
        L_eig = np.zeros_like(drho_eig)
        for m in range(len(p)):
            for n in range(len(p)):
                denom = p[m] + p[n]
                if denom > 1e-12:
                    L_eig[m, n] = 2 * drho_eig[m, n] / denom
        L = U @ L_eig @ U.T.conj()

        # 5. Fisher metric: g = (1/2) Tr[rho {L, L}] = Tr[rho L^2]
        g_xx = np.real(np.trace(rho_center @ L @ L))
        # Store g_xx for position x

def fisher_metric_2d(Lx, Ly, J, A_shape, boundary='PBC'):
    """
    Compute Fisher metric tensor on 2D Heisenberg lattice.

    Returns g_{mu nu}(x,y) for each valid position.
    g is a 2x2 matrix at each point.
    """
    # Similar to 1D but with two shift directions.
    # For 4x4 lattice: 2^16 = 65536 states -- feasible.
    # For 6x6 lattice: 2^36 -- infeasible with full ED.
    # Use symmetry sectors (total S_z = 0) to reduce.
```

**Expected results:**
- 1D gapless (n=2): g(x) ~ constant in bulk, with O(1/N) corrections and logarithmic boundary effects
- 2D gapped (n=2, if Neel ordered): g_{mu nu}(x) ~ eta * delta_{mu nu} in bulk (isotropic), converging exponentially fast in N
- The proportionality constant eta encodes the entanglement entropy density and should relate to 1/(4 G_N) as in Paper 6

**Critical numerical checks:**
1. g_{mu nu} is positive semidefinite at every point (physicality)
2. g_{xx}(x) is approximately translation-invariant in the bulk (homogeneity)
3. g_{xx} ~ g_{yy} in 2D (isotropy from SU(2) symmetry)
4. g(N) converges as N increases (continuum limit evidence)
5. The continuum-limit value of g matches the entanglement entropy density eta from Paper 6

**Cost per lattice:**
- N=12 1D PBC: ~1 sec (already computed in existing code)
- N=16 1D PBC: ~5 sec
- N=20 1D PBC: ~2 min
- 4x4 2D PBC: ~30 min (with S_z sector restriction)
- 5x5 2D PBC: infeasible with full ED

Total for the Fisher metric study: ~2-4 hours of computation.

**Confidence:** HIGH for the computation itself. MEDIUM for whether the results will show clear convergence to a smooth metric (finite-size effects may be large at N=16-20).

---

## Alternatives Considered

| Recommended | Alternative | When to Use Alternative |
|-------------|-------------|------------------------|
| SLD-based QFI metric | Bures distance d_B(rho, sigma) computed directly | Only for very small systems (|A|<=3) where d_B is cheaper than SLD; for larger systems SLD is more numerically stable |
| Central finite differences for drho/dx | Forward differences | Never -- central differences have O(a^2) vs O(a) error for negligible extra cost |
| Modular flow for time direction (Approach A) | Full OS reconstruction (Approach B) | When rigorous axiomatic QFT verification is the goal, not just establishing Lorentzian metric |
| Nachtergaele-Sims for exponential clustering | Hastings' independent proof | Either works; NS has tighter constants and connects more directly to Lieb-Robinson already in the project |
| ED for N<=20 | DMRG for N<=1000 | When finite-size effects at N=20 are too large to extrapolate; DMRG requires additional library setup |

## What NOT to Use

| Avoid | Why | Use Instead |
|-------|-----|-------------|
| Classical Fisher information (on measurement outcomes) | We need the QUANTUM Fisher information on density matrices, not the classical version on probability distributions; the quantum version captures coherence information that classical misses | Quantum Fisher information via SLD |
| Fubini-Study metric on pure states | The full lattice state |psi> is pure, but the relevant geometric object is the metric on REDUCED states rho_A(x) which are mixed; Fubini-Study applies only to pure states | Bures/SLD metric on mixed states |
| Perturbative QFT for Wightman axiom verification | The lattice theory is strongly coupled (Heisenberg model is not weakly interacting); perturbation theory gives the wrong effective theory | Constructive/non-perturbative methods (OS reconstruction, ED verification) |
| Monte Carlo for Fisher metric | QMC has a sign problem for frustrated systems and cannot directly compute off-diagonal density matrix elements needed for SLD | ED for small systems, DMRG for larger 1D systems |
| Numerical analytic continuation for Lorentzian correlators | Notorious ill-conditioning; Bayesian methods (MaxEnt) have uncontrolled systematic errors | Direct OS reconstruction or modular flow identification |

---

## Validation Strategy by Method

| Method | Validation Approach | Key Benchmarks |
|--------|---------------------|----------------|
| Fisher metric (Method 1) | Check g_{mu nu} >= 0, isotropy g_{xx}=g_{yy}, translation invariance in bulk | TFI at criticality: g diverges at h/J=1 (Zanardi et al. 2007) |
| Exponential clustering (Method 2) | Compute correlation functions and fit decay rate; compare mu with Delta/(2 v_LR) | Heisenberg chain n=2: algebraic decay at rate from WZW CFT (c=1). Gapped TFI: exponential decay |
| Smoothness (Method 3) | Second-difference test: ||Delta^2 rho|| / ||Delta rho|| = O(a) | Constant ratio in the bulk for gapped systems; logarithmic corrections for gapless |
| Lorentzian (Method 4) | Modular Hamiltonian locality (already checked in Paper 6: SRF=0.9993) | Bisognano-Wichmann: modular Hamiltonian = boost generator in Rindler wedge |
| Wightman axioms (Method 5) | Reflection positivity of transfer matrix; cluster property from exponential decay | phi^4_2 constructive QFT results (Glimm-Jaffe): known to satisfy all OS axioms |
| Numerical Fisher metric (Method 6) | Cross-check: g from SLD vs g from Bures distance for small |A| | Both must agree to machine precision (they differ only at singular points where rank changes) |

### Critical Cross-Check

The Fisher metric g_{mu nu} derived from Method 1/6 must be consistent with the entanglement entropy eta from Paper 6. Specifically:

    g_{mu nu} ~ eta * delta_{mu nu} / a^{d-1}

where eta = S(A) / |partial A| is the entanglement entropy per unit boundary area and a is the lattice spacing. Since Paper 6 identifies eta = 1/(4 G_N), the Fisher metric provides an independent path to Newton's constant. These two determinations MUST agree; disagreement would indicate an error in the framework.

---

## Installation / Setup

```bash
# Core computational environment (already in project)
pip install numpy scipy sympy matplotlib

# For DMRG extension (N>20, optional, requires user approval):
# pip install physics-tenpy  # TeNPy for Python DMRG
# OR
# Julia + ITensors.jl for Julia DMRG

# No additional software needed for ED-based Fisher metric computation.
# All methods build on existing code/ed_entanglement.py infrastructure.
```

---

## Sources

- Zanardi, Giorda & Cozzini, "Information-theoretic differential geometry of quantum phase transitions," PRL 99, 100603 (2007), [arXiv:quant-ph/0701061](https://arxiv.org/abs/quant-ph/0701061) -- Fisher metric and quantum phase transitions
- Liu, Peng & Yuan, "Quantum Fisher information matrix and multiparameter estimation," J. Phys. A 53, 023001 (2020), [arXiv:1907.08037](https://arxiv.org/abs/1907.08037) -- Comprehensive review of QFIM computation methods
- Matsueda, "Emergent General Relativity from Fisher Information Metric," [arXiv:1310.1831](https://arxiv.org/abs/1310.1831) (2013) -- Fisher metric -> Einstein tensor on lattice states
- Nachtergaele & Sims, "Lieb-Robinson bounds and the exponential clustering theorem," CMP 265, 119 (2006), [arXiv:math-ph/0506030](https://arxiv.org/abs/math-ph/0506030) -- Spectral gap implies exponential clustering
- Hastings, "Spectral gap and exponential decay of correlations," CMP 265, 781 (2006), [arXiv:math-ph/0604015](https://arxiv.org/abs/math-ph/0604015) -- Independent proof of exponential clustering
- Kennedy, Lieb & Shastry, "Existence of Neel order in some spin-1/2 Heisenberg antiferromagnets," J. Stat. Phys. 53, 1019 (1988) -- Rigorous Neel order for spin-1/2 in d>=3
- Dyson, Lieb & Simon, "Phase transitions in quantum spin systems with isotropic and nonisotropic interactions," J. Stat. Phys. 18, 335 (1978) -- Foundation for infrared bounds and long-range order
- Calabrese & Cardy, "Entanglement entropy and quantum field theory," J. Stat. Mech. P06002 (2004), [arXiv:hep-th/0405152](https://arxiv.org/abs/hep-th/0405152) -- CFT entanglement entropy formula
- Connes & Rovelli, "Von Neumann algebra automorphisms and time-thermodynamics relation," CMP 8, 1 (1994), [arXiv:gr-qc/9406019](https://arxiv.org/abs/gr-qc/9406019) -- Thermal time hypothesis
- Osterwalder & Schrader, "Axioms for Euclidean Green's functions," CMP 31, 83 (1973); CMP 42, 281 (1975) -- OS axioms for Euclidean QFT
- Glimm & Jaffe, "Quantum Physics: A Functional Integral Point of View," Springer (1987) -- Constructive QFT textbook
- Seveso, Albarelli, Genoni & Paris, "Discontinuities of the quantum Fisher information and the Bures metric," PRA 95, 052320 (2017), [arXiv:1612.04581](https://arxiv.org/abs/1612.04581) -- QFI discontinuities at rank changes
- Zhou & Jiang, "An exact correspondence between the quantum Fisher information and the Bures metric," [arXiv:1910.08473](https://arxiv.org/abs/1910.08473) (2019) -- QFI = 4 * Bures metric
- Uhlmann gauge + DMRG: "Quantum Information Geometry Meets DMRG," [arXiv:2505.11514](https://arxiv.org/abs/2505.11514) (2025) -- DMRG with Bures metric gauge for spin chains
- Affleck, Kennedy, Lieb & Tasaki, "Valence bond ground states in isotropic quantum antiferromagnets," CMP 115, 477 (1988) -- AKLT model, exact gap, exponential clustering
- Nachtergaele, Sims & Young, "Quasi-locality bounds for quantum lattice systems. Part I," [arXiv:1810.02428](https://arxiv.org/abs/1810.02428) (2019) -- Modern comprehensive treatment of Lieb-Robinson bounds

---

_Methods research for: v9.0 Information-Geometric Continuum Limit from Finite-Dimensional Observer_
_Researched: 2026-03-29_
