# Research Summary

**Project:** Universality Class of Self-Modeler Network and Full Gap Closure (v10.0)
**Domain:** Exceptional Jordan algebras / Quantum lattice systems / SSB with F_4 symmetry / Nonlinear sigma models
**Researched:** 2026-03-30
**Confidence:** MEDIUM

## Unified Notation

| Symbol | Quantity | Units/Dimensions | Convention Notes |
|--------|---------|-----------------|-----------------|
| h_3(O) | Exceptional Jordan algebra (Albert algebra) | 27-dim real vector space | Jordan product: a o b = (ab + ba)/2 |
| F_4 | Compact exceptional Lie group, Aut(h_3(O)) | dim 52, rank 4 | F_4 = F_4(-52), compact real form; NOT split form F_4(4) |
| Spin(9) | Stabilizer of primitive idempotent in F_4 | dim 36 | Peirce embedding: stabilizer of E_{11} |
| OP^2 | Octonionic projective plane = F_4/Spin(9) | dim 16, compact symmetric | Cayley plane; rank-1 symmetric space |
| V_1, V_{1/2}, V_0 | Peirce eigenspaces under idempotent E_{11} | dims 1, 16, 10 | Eigenvalues {1, 1/2, 0} of L_{E_{11}} |
| T_b | Peirce multiplication operators on V_{1/2} | 16x16 real matrices in M_16(R) | b = 1,...,10; traceless T_b satisfy Clifford {T_a,T_b} = (1/2)delta_{ab} I_{16} |
| H_eff | Lattice Hamiltonian | Energy (hbar=1, k_B=1, a=1) | H = J sum_{<ij>} sum_a T_a^(i) T_a^(j) (Formulation A) |
| n_BG | Number of broken generators | dimensionless | = dim(F_4) - dim(H) where H is residual symmetry |
| rho_s | Spin stiffness (helicity modulus) | Energy | = (1/V) d^2 E_0 / dphi^2 |
| c_s | Spin-wave velocity | velocity (lattice units) | Determined by microscopic coupling and target manifold curvature |
| G_hat(k) | Fourier transform of 2-point function | [length]^d | Infrared bound: G_hat(k) <= C/E(k) |

**Unit system:** Natural units hbar = 1, k_B = 1, lattice spacing a = 1.
**Octonion convention:** Fano plane with e_1 e_2 = e_4 (matching Paper 7).
**Clifford signature:** Cl(9,0) (positive definite).
**Metric signature:** Not applicable at lattice level; emergent Lorentz is a downstream prediction.

**Convention conflicts resolved (2):**
1. Peirce eigenvalue convention: locked to {0, 1/2, 1} with Jordan product a o b = (ab+ba)/2. Some sources use {0, 1, 2}; the difference is a factor of 2 in the Jordan product definition.
2. F_4 real form: locked to F_4(-52) (compact), the automorphism group of h_3(O) over the division octonions. Some string theory sources use the split form F_4(4) = Aut(h_3(O_s)).

## Executive Summary

The v10.0 milestone asks whether the self-modeler network -- whose on-site algebra is the exceptional Jordan algebra h_3(O) with F_4 automorphism symmetry -- falls into a universality class where the v9.0 mechanism chain (Fisher geometry -> sigma model -> Lorentz -> BW -> KMS -> Jacobson -> Einstein) fires. The research literature strongly supports that a lattice model with F_4-symmetric nearest-neighbor interactions on Z^d (d >= 3) undergoes spontaneous symmetry breaking, via the well-established Froehlich-Simon-Spencer / Dyson-Lieb-Simon / Biskup-Chayes-Starr framework of reflection positivity and infrared bounds. The resulting Goldstone sector is described by a nonlinear sigma model on a compact symmetric space (likely OP^2 = F_4/Spin(9)), which is asymptotically free and shares the qualitative properties needed for the v9.0 chain. No prior lattice models with F_4 symmetry exist in the literature, making this genuinely novel territory.

The critical obstacle is the lattice structure. The Peirce decomposition of h_3(O) gives a 3-site triangle graph (K_3), which is NOT bipartite -- this breaks the DLS reflection positivity requirement. The resolution demands clarifying that the Peirce K_3 is the on-site algebraic structure, not the lattice geometry: the physical lattice model lives on Z^d with h_3(O) at EACH SITE, and Z^d IS bipartite. Phase 38 must make this lattice construction explicit. A second major uncertainty is the SSB pattern: while F_4 -> Spin(9) (giving OP^2 as the Goldstone manifold) is the physically motivated guess, the actual pattern depends on the explicit Hamiltonian H_eff, which must be computed before the sigma model analysis can proceed. The non-associativity of the octonions is resolved by working in the associative envelope M_16(R) via the T_b operators already computed in v8.0.

Computationally, all proposed calculations are feasible on a local workstation. The V_{1/2} representation (d=16 per site) makes exact diagonalization tractable up to 5-6 sites (Hilbert space dim 16^N vs 27^N). Classical Monte Carlo on OP^2 is highly tractable for arbitrarily large lattices. The main bottleneck is algebraic (constructing H_eff correctly and implementing the 16 additional F_4 generators beyond spin(9) for twisted boundary conditions), not computational.

## Key Findings

### Computational Approaches

**Core approach:** Two-track strategy separating quantum lattice ED from classical sigma model MC.

- **Formulation A (V_{1/2} representation, RECOMMENDED):** Each site carries R^16 (Peirce half-space). H_eff = J sum T_a^(i) T_a^(j) using the 10 existing T_b operators as 16x16 real matrices. Hilbert space dimension 16^N: N=4 gives 65,536 (identical to the v9.0 4x4 Heisenberg at d=2), N=6 gives 16M (Lanczos feasible). [CONFIDENCE: HIGH]
- **Classical MC on OP^2:** Points parametrized as rank-1 idempotents in h_3(O) (16 effective degrees of freedom per site). Lattice action S = -beta sum Tr(P_i . P_j). Tractable on 32x32+ lattices. No quantum sign problem. Independent of ED track. [CONFIDENCE: HIGH]
- **Spin stiffness via twisted BC:** Requires explicit F_4 generators beyond spin(9) (16 additional generators). Algebraic construction task, then standard Lanczos. [CONFIDENCE: MEDIUM -- F_4 generator construction is the bottleneck]

**Anti-approaches:** DMRG (d=16 per site makes MPS tensors enormous, no F_4-symmetric code exists), QMC (sign problem unanalyzed for F_4), large-N expansion (F_4 is exceptional, not SU(N)).

### Prior Work Landscape

**Must reproduce (benchmarks):**

- DLS infrared bound structure: G_hat(k) <= C/|k|^2 leading to SSB for d >= 3 at low T. The integral I_3 = (6 - pi^2/3)/(2pi^2) for Z^3 is the standard value. [CONFIDENCE: HIGH]
- Mermin-Wagner prohibition of F_4 SSB in d <= 2 at T > 0. [CONFIDENCE: HIGH]
- F_4 subgroup structure: F_4/Spin(9) = OP^2 (dim 16), Spin(9) = stabilizer of primitive idempotent. [CONFIDENCE: HIGH -- independently verified]
- OP^2 homotopy: pi_k = 0 for k = 1,...,7; pi_8 = Z. No topological theta-term, no WZW term. [CONFIDENCE: HIGH -- independently verified]
- Sigma model on OP^2 is asymptotically free in 2D (follows from positive Ricci curvature + Friedan 1985). [CONFIDENCE: HIGH]

**Novel predictions (contributions):**

- SSB of F_4 on Z^d (d >= 3) with trace-inner-product interaction -- first proof for any lattice model with exceptional symmetry. [CONFIDENCE: MEDIUM]
- Identification of SSB pattern (F_4 -> Spin(9) vs F_4 -> Spin(8) vs F_4 -> G_2) from explicit H_eff. [CONFIDENCE: LOW-MEDIUM]
- Complete v9.0 mechanism chain firing on OP^2 sigma model (closing all four Paper 6 gaps unconditionally). [CONFIDENCE: MEDIUM]

**Defer (future work):**

- RG relevance of cubic det(A) invariant (unique to Albert algebra, no O(3) analog). Potentially changes universality class but can be treated as perturbation after quadratic-coupling SSB is established.
- Precise critical exponents of the F_4/Spin(9) sigma model (a genuinely new universality class, not reducible to O(N) for any N).

### Methods and Tools

The analytical core is the DLS/FSS/BCS triad: FSS proves SSB for the classical limit, BCS lifts it to the quantum model (valid when beta << sqrt(S), with effective S ~ 27 being large), and DLS-style infrared bounds provide the quantitative estimate. Watanabe-Murayama counting determines the Goldstone mode spectrum (all Type-A with linear dispersion for antiferromagnets, which is required for emergent Lorentz). The NLsM on F_4/H provides the effective field theory. All existing codebase infrastructure (octonion_algebra.py, ed_entanglement.py, fisher_metric.py) extends naturally to the new setting.

**Major components:**

1. **DLS infrared bounds with RP** -- prove SSB rigorously for F_4-symmetric Hamiltonian on Z^d, d >= 3
2. **Watanabe-Murayama Goldstone counting** -- determine Type-A vs Type-B modes and their dispersion
3. **NLsM on F_4/H** -- effective field theory for Goldstone sector; universality class determination
4. **ED on V_{1/2} representation** -- numerical verification of SSB signatures (Anderson tower, order parameter, gap scaling)
5. **Classical MC on OP^2** -- large-lattice sigma model verification

### Critical Pitfalls

1. **K_3 is NOT bipartite (CRITICAL)** -- The Peirce decomposition gives a triangle graph, which has an odd cycle. DLS reflection positivity REQUIRES bipartiteness. The resolution is that the Peirce K_3 is the on-site algebraic structure; the physical lattice lives on Z^d with h_3(O) at each site, and Z^d IS bipartite. Phase 38 must make this explicit and construct the correct lattice model. [Phase 38 must resolve]
2. **No SSB on finite systems** -- If the self-modeler network is literally K_3 (3 sites), there is no thermodynamic limit, no SSB, and the mechanism fails. The K_3 must be the unit cell or internal structure, not the full lattice. Must explicitly construct the infinite lattice extension. [Phase 38 must resolve]
3. **Non-associativity of octonions** -- h_3(O) is exceptional (not a C*-algebra). Transfer matrices, BCH, standard operator methods assume associativity. Resolution: work exclusively in the associative envelope M_16(R) via T_b operators. H_eff must be bilinear in T_b (safe); cubic or higher terms require explicit parenthesization. [Phase 38: verify H_eff is associative]
4. **SSB pattern is NOT determined a priori** -- F_4 -> Spin(9) is a guess. Alternatives: F_4 -> Spin(8), F_4 -> G_2, F_4 -> Sp(3)xSU(2), or no SSB (spin liquid). The sigma model, Goldstone counting, and universality class all depend on the actual pattern. Resolution: compute H_eff first, determine ground state, THEN identify SSB pattern. [Phases 38-39]
5. **Type-II Goldstone modes kill Lorentz emergence** -- If the breaking is ferromagnetic-type, modes have quadratic dispersion omega ~ k^2, which is incompatible with emergent Lorentz invariance. Resolution: need antiferromagnetic-type ordering where rho_ab = <[Q_a, Q_b]> = 0, giving all Type-A (linear) modes. Must verify from H_eff. [Phase 39]

## Approximation Landscape

| Method | Valid Regime | Breaks Down When | Controlled? | Complements |
|--------|-------------|-----------------|-------------|-------------|
| DLS infrared bounds | d >= 3, bipartite lattice, NN interaction, RP holds | d <= 2 (Mermin-Wagner); non-bipartite (frustrated); long-range interactions | Yes (rigorous bound) | BCS for quantum-classical lift |
| BCS quantum-classical reduction | beta << sqrt(S), S large (effective spin) | Small spin (S ~ 1/2), very low T where quantum effects dominate | Yes (controlled by 1/sqrt(S)) | DLS for the classical limit |
| NLsM on G/H | Below SSB scale, above lattice UV cutoff; weak coupling in d=2+epsilon | Near phase transition (strong coupling); d=2 at T>0 (disordered) | Yes (epsilon expansion in d=2+epsilon) | ED/MC for non-perturbative regime |
| ED (exact diagonalization) | N <= 5-6 sites (d=16 per site) | N > 6 (memory); thermodynamic limit extrapolation | Exact for finite system | Classical MC for large lattices |
| Classical MC on OP^2 | Any lattice size; finite T | T=0 (need quantum corrections); near critical point (critical slowing) | No systematic expansion | ED for quantum effects |

**Coverage gap:** No reliable non-perturbative method exists for the quantum F_4 lattice model on large lattices. ED is limited to ~6 sites, QMC sign problem is unanalyzed, DMRG is impractical for d=16. The classical MC covers the sigma model regime but misses quantum corrections. This gap is mitigated by the BCS reduction theorem, which says the quantum model inherits SSB from the classical limit for large effective spin.

## Theoretical Connections

### Cross-Subfield Connections

1. **DLS universality across symmetry groups (ESTABLISHED):** The FSS/DLS/BCS framework proves SSB for ANY compact continuous symmetry G on Z^d (d >= 3) with RP-compatible interactions and large enough representation dimension. Extension to F_4 is a new application of an established framework.

2. **Peirce decomposition <-> Lattice structure (CONJECTURED):** The Peirce decomposition of h_3(O) into V_1 + V_{1/2} + V_0 parallels the sublattice decomposition in condensed matter. The V_{1/2} space (dim 16) mediates interactions between "site" degrees of freedom. This structural parallel motivates Formulation A.

3. **Sigma model universality: OP^2 vs S^2 (CONJECTURED):** Both OP^2 and S^2 are compact rank-1 symmetric spaces with positive Ricci curvature. Their sigma models share: asymptotic freedom in 2D, ordered phase in d >= 3, massive spin waves with well-defined velocity. The v9.0 mechanism depends on these GENERIC properties. The main quantitative difference is 16 Goldstone modes vs 2.

4. **Farnsworth spectral geometry (ESTABLISHED, independent):** Farnsworth's 2025 construction of F_4 x F_4 gauge theory from exceptional Jordan geometries via NCG cross-validates the h_3(O) route to gauge theories from a completely different method.

5. **Non-associativity resolution via operator representation (ESTABLISHED):** The JvNW obstruction (h_3(O) is exceptional, not a matrix algebra) is resolved by passing to M_16(R). This is standard in the Jordan algebra literature and is already implemented via T_b operators in the codebase.

### Cross-Validation Matrix

|                    | DLS/BCS (analytical) | ED (numerical) | Classical MC | Sigma model EFT |
|--------------------|:---:|:---:|:---:|:---:|
| **DLS/BCS**        | -- | Anderson tower 1/N scaling | Ordered phase at low T | SSB -> sigma model derivation chain |
| **ED**             | Gap scaling | -- | rho_s comparison | c_s from ED vs sigma model |
| **Classical MC**   | Phase transition at T_c | Order parameter | -- | Correlation length xi |
| **Sigma model**    | Valid below SSB scale | c_s calibration | Phase boundary | -- |

**High-risk gap:** DLS has no independent numerical cross-check for F_4 specifically (no QMC exists).

### Critical Claim Verification

| # | Claim | Source | Verification | Result |
|---|-------|--------|--------------|--------|
| 1 | F_4/Spin(9) = OP^2, dim 16 | PRIOR-WORK.md | web_search: "F4 Spin(9) stabilizer primitive idempotent h3(O)" | CONFIRMED |
| 2 | DLS requires bipartite lattice for quantum AFM | PITFALLS.md | web_search: "Dyson Lieb Simon reflection positivity bipartite" | CONFIRMED |
| 3 | pi_k(OP^2) = 0 for k <= 7, pi_8 = Z | PITFALLS.md | web_search: "octonionic projective plane homotopy groups" | CONFIRMED |
| 4 | Watanabe-Murayama: AFM gives all Type-A Goldstone modes | METHODS.md | web_search: "Watanabe Murayama Goldstone counting type-A" | CONFIRMED |
| 5 | BCS: quantum inherits SSB from classical for beta << sqrt(S) | PRIOR-WORK.md | web_search: "Biskup Chayes Starr quantum classical reduction" | CONFIRMED |
| 6 | No prior lattice models with F_4 symmetry exist | PRIOR-WORK.md | web_search: multiple queries | CONFIRMED (absence) |
| 7 | K_3 (3-vertex complete graph) is NOT bipartite | PITFALLS.md | Graph theory: K_3 has 3-cycle | CONFIRMED |

## Implications for Roadmap

### Suggested Phase Structure

### Phase 37: Gap Dependency Theorem

**Rationale:** Establish the logical framework FIRST: prove that universality conditions (UC1)-(UC4) plus additional QFT assumptions (UC5)-(UC8) suffice to close all four Paper 6 gaps. Pure logic that depends only on v9.0 results.
**Delivers:** Theorem statement with all assumptions explicit; clear target for Phases 38-40.
**Validates:** Logical consistency of the v9.0 chain applied to general compact symmetric spaces.
**Avoids:** Pitfall 6 (hidden assumptions in BW -> Lovelock chain).

### Phase 38: H_eff from Peirce Structure

**Rationale:** The Hamiltonian construction is the algebraic foundation for everything downstream. Must resolve: (a) lattice structure (how the K_3 Peirce motif maps to Z^d), (b) H_eff construction from T_b operators, (c) F_4 symmetry and RP verification, (d) whether H_eff is AFM-type.
**Delivers:** Explicit H_eff as sparse matrix on V_{1/2}^{tensor N}; verified Spin(9) commutation; 2-site spectrum; lattice structure clarification.
**Uses:** Formulation A (T_b operators from code/octonion_algebra.py), SciPy sparse, existing ED infrastructure.
**Builds on:** v8.0 T_b operators, v5.0/v8.0 Peirce decomposition.
**Avoids:** Pitfall 1 (K_3 bipartiteness), Pitfall 3 (non-associativity), Pitfall 4 (finite-system SSB confusion).

### Phase 39: SSB Proof and Universality Class

**Rationale:** With H_eff in hand, prove SSB via DLS/BCS, determine SSB pattern, count Goldstone modes, construct sigma model.
**Delivers:** Rigorous SSB proof (or honest conditional statement); SSB pattern; Goldstone mode count and type; sigma model Lagrangian.
**Uses:** DLS infrared bounds, BCS reduction, Watanabe-Murayama, NLsM, ED, classical MC.
**Builds on:** Phase 38 (H_eff and lattice structure).
**Avoids:** Pitfall 2 (frustration), Pitfall 5 (OP^2 topology), Pitfall 7 (wrong SSB pattern), Pitfall 9 (Goldstone mode type).

### Phase 40: Assembly and Gap Closure

**Rationale:** Map v9.0 chain to F_4/H sigma model, verify each link fires, close all four gaps.
**Delivers:** Complete derivation chain from self-modeling to Einstein equations on h_3(O); gap scorecards; honest assessment.
**Uses:** NLsM analysis from Phase 39, gap dependency theorem from Phase 37.
**Builds on:** All previous phases.
**Avoids:** Pitfall 6 (hidden assumptions), Pitfall 10 (d=3 overclaiming).

### Phase Ordering Rationale

- Phases 37 and 38 can run in parallel (independent inputs: v9.0 chain logic vs algebraic construction).
- Phase 38 strictly before 39: H_eff determines the lattice structure, SSB pattern, and whether DLS applies.
- Phase 39 strictly before 40: sigma model, Goldstone modes, and SSB proof are inputs to gap closure.
- The critical path is 38 -> 39 -> 40. Phase 37 is off the critical path but must complete before 40.

### Phases Requiring Deep Investigation

- **Phase 38:** Novel territory -- lattice structure from Peirce decomposition has no literature precedent. Must determine how h_3(O) sites tile Z^d.
- **Phase 39:** Novel territory -- first F_4 lattice SSB proof. Frame stabilizer identification is unsettled in the literature.

Phases with established methodology:

- **Phase 37:** Logical analysis of v9.0 chain; well-defined scope.
- **Phase 40 (partially):** If Phases 38-39 deliver clean results, the mapping is systematic.

## Confidence Assessment

| Area | Confidence | Notes |
|------|-----------|-------|
| Computational Approaches | HIGH | Formulation A (d=16) is tractable; all code extends from v8.0/v9.0 |
| Prior Work | HIGH | F_4 algebraic structure well-established; DLS/FSS/BCS framework mature |
| Methods | MEDIUM | DLS method is rigorous and general but never applied to F_4; frame stabilizer uncertain |
| Pitfalls | HIGH | Comprehensive; K_3 bipartiteness correctly identified as critical obstacle |

**Overall confidence:** MEDIUM

### Gaps to Address

- **Lattice structure from Peirce decomposition:** How does the K_3 motif map onto a macroscopic Z^d lattice? Is the on-site Peirce structure internal or does it generate a frustrated lattice? Blocks Phase 38.
- **F_4 frame stabilizer:** Spin(9) vs Spin(8) vs G_2. Determines everything about the sigma model. Blocks Phase 39.
- **Constructive QFT for 3D sigma model:** Whether the F_4/Spin(9) sigma model in 3D defines a rigorous Wightman QFT. Affects BW theorem application and honesty of gap closure.
- **QMC sign problem for F_4:** If absent, enables independent SSB verification. If present, we are limited to ED + classical MC.
- **Cubic invariant RG relevance:** Could change the universality class. Deferred but noted.

## Sources

### Primary (HIGH)

- Froehlich-Simon-Spencer, CMP 50 (1976) 79-95 -- infrared bounds for classical lattice models
- Dyson-Lieb-Simon, JSP 18 (1978) 335-383 -- quantum SSB for SU(2) Heisenberg
- Kennedy-Lieb-Shastry, JSP 53 (1988) 1019-1044 -- Neel order for S=1/2, d >= 3
- [Biskup-Chayes-Starr, CMP 269 (2007)](https://arxiv.org/abs/math-ph/0509017) -- quantum-to-classical reduction via RP
- [Watanabe-Murayama, PRL 108 (2012) 251602](https://arxiv.org/abs/1203.0609) -- Goldstone counting for non-Lorentzian systems
- [Biskup, "RP and Phase Transitions" (2006)](https://arxiv.org/abs/math-ph/0610025) -- review of RP conditions
- [Bjornberg-Ueltschi (2022)](https://arxiv.org/abs/2204.12896) -- modern review of RP/IR bounds
- Friedan, Ann. Phys. 163 (1985) 318 -- sigma model beta function = Ricci tensor
- [Baez, Bull. AMS 39 (2002)](https://arxiv.org/abs/math/0105155) -- h_3(O), F_4, OP^2
- [Todorov-Drenska, arXiv:1805.06739](https://arxiv.org/abs/1805.06739) -- F_4 subgroup structure

### Secondary (MEDIUM)

- [Nachtergaele, arXiv:math-ph/0603017](https://arxiv.org/abs/math-ph/0603017) -- post-DLS developments
- [Farnsworth, arXiv:2503.10744](https://arxiv.org/abs/2503.10744) -- exceptional Jordan geometries, F_4 x F_4 gauge theory
- [Lackmann, arXiv:1909.07047](https://arxiv.org/abs/1909.07047) -- homotopy groups of OP^2
- Parton-Picken, Axioms 7(4):72 (2018) -- Spin(9) in octonionic geometry
- [Watanabe, Ann. Rev. Cond. Mat. Phys. 11 (2020)](https://arxiv.org/abs/1904.00569) -- Goldstone counting review
- [Bernardoni et al., arXiv:0705.3978](https://arxiv.org/abs/0705.3978) -- F_4 parametrization
- Sandvik, arXiv:2601.20189 (2025) -- QMC spin stiffness methodology

### Tertiary (LOW)

- Farnsworth, arXiv:2506.21496 (2025) -- spectral geometry with exceptional symmetry (very recent)
- McCrimmon, "A Taste of Jordan Algebras" (Springer, 2004)
- Yokota, "Exceptional Lie Groups" (2009)

---

_Research analysis completed: 2026-03-30_
_Ready for research plan: yes_

```yaml
# --- ROADMAP INPUT (machine-readable, consumed by gpd-roadmapper) ---
synthesis_meta:
  project_title: "Universality Class of Self-Modeler Network and Full Gap Closure (v10.0)"
  synthesis_date: "2026-03-30"
  input_files: [METHODS.md, PRIOR-WORK.md, COMPUTATIONAL.md, PITFALLS.md]
  input_quality: {METHODS: good, PRIOR-WORK: good, COMPUTATIONAL: good, PITFALLS: good}

conventions:
  unit_system: "natural"
  metric_signature: "N/A (lattice; emergent Lorentz is downstream prediction)"
  fourier_convention: "physics"
  coupling_convention: "H = J sum T_a^(i) T_a^(j), J > 0 for AFM"
  renormalization_scheme: "N/A (lattice model; sigma model uses epsilon expansion d=2+epsilon)"

methods_ranked:
  - name: "DLS infrared bounds (via BCS quantum-classical reduction)"
    regime: "d >= 3, bipartite lattice, NN interaction, RP holds, large effective spin S ~ 27"
    confidence: HIGH
    cost: "O(1) (analytical proof)"
    complements: "ED for finite-size verification; classical MC for sigma model regime"
  - name: "Exact diagonalization (V_{1/2} Formulation A)"
    regime: "N <= 5-6 sites, d=16 per site"
    confidence: HIGH
    cost: "O(16^N) memory; O(16^N * k) for Lanczos with k eigenvalues"
    complements: "DLS for thermodynamic limit; classical MC for large lattices"
  - name: "Watanabe-Murayama Goldstone counting"
    regime: "Any SSB pattern with compact G; requires knowledge of ground state"
    confidence: HIGH
    cost: "O(1) (algebraic computation)"
    complements: "NLsM for dynamics; ED for spectrum verification"
  - name: "NLsM on F_4/H"
    regime: "Below SSB scale, above lattice cutoff; perturbative in d=2+epsilon"
    confidence: MEDIUM
    cost: "Analytical"
    complements: "DLS for SSB existence; ED for spin-wave velocity"
  - name: "Classical MC on OP^2"
    regime: "Any lattice size; finite T; classical sigma model regime"
    confidence: HIGH
    cost: "O(N * 16) per sweep; minutes for 32x32 lattice"
    complements: "ED for quantum effects; DLS for rigorous SSB"

phase_suggestions:
  - name: "Gap Dependency Theorem"
    goal: "Prove (UC1)-(UC4) + (UC5)-(UC8) close all four Paper 6 gaps"
    methods: ["logical analysis of v9.0 chain"]
    depends_on: []
    needs_research: false
    risk: LOW
    pitfalls: ["pitfall-6-hidden-assumptions"]
  - name: "H_eff from Peirce Structure"
    goal: "Construct explicit Hamiltonian, determine lattice structure, verify RP"
    methods: ["Exact diagonalization (V_{1/2} Formulation A)"]
    depends_on: []
    needs_research: true
    risk: MEDIUM
    pitfalls: ["pitfall-1-K3-bipartiteness", "pitfall-3-nonassociativity", "pitfall-4-finite-system-SSB"]
  - name: "SSB Proof and Universality Class"
    goal: "Prove F_4 SSB on Z^d (d>=3), identify breaking pattern, count Goldstone modes, construct sigma model"
    methods: ["DLS infrared bounds (via BCS quantum-classical reduction)", "Watanabe-Murayama Goldstone counting", "NLsM on F_4/H", "Classical MC on OP^2"]
    depends_on: ["H_eff from Peirce Structure"]
    needs_research: true
    risk: HIGH
    pitfalls: ["pitfall-2-frustration", "pitfall-5-OP2-topology", "pitfall-7-SSB-pattern", "pitfall-9-goldstone-type"]
  - name: "Assembly and Gap Closure"
    goal: "Map v9.0 chain to F_4/H sigma model, close all four gaps, honest assessment"
    methods: ["NLsM on F_4/H", "Exact diagonalization (V_{1/2} Formulation A)"]
    depends_on: ["Gap Dependency Theorem", "SSB Proof and Universality Class"]
    needs_research: false
    risk: MEDIUM
    pitfalls: ["pitfall-6-hidden-assumptions", "pitfall-10-d3-overclaiming"]

critical_benchmarks:
  - quantity: "DLS infrared bound integral I_3 on Z^3"
    value: "(6 - pi^2/3)/(2 pi^2)"
    source: "DLS 1978"
    confidence: HIGH
  - quantity: "dim F_4/Spin(9) = dim OP^2"
    value: "16"
    source: "Baez 2002; Todorov-Drenska 2018"
    confidence: HIGH
  - quantity: "Homotopy pi_k(OP^2) for k = 1,...,7"
    value: "0 (trivial)"
    source: "Lackmann arXiv:1909.07047"
    confidence: HIGH
  - quantity: "pi_8(OP^2)"
    value: "Z"
    source: "Baez 2002"
    confidence: HIGH
  - quantity: "H_eff 2-site ground state energy"
    value: "To be computed from T_b Kronecker products"
    source: "This project"
    confidence: HIGH
  - quantity: "Mermin-Wagner: no F_4 SSB in d <= 2 at T > 0"
    value: "Forbidden"
    source: "Mermin-Wagner theorem"
    confidence: HIGH

open_questions:
  - question: "What is the macroscopic lattice structure? How does h_3(O) on-site algebra map to Z^d?"
    priority: HIGH
    blocks_phase: "H_eff from Peirce Structure"
  - question: "What is the SSB pattern (F_4 -> Spin(9) vs Spin(8) vs G_2 vs other)?"
    priority: HIGH
    blocks_phase: "SSB Proof and Universality Class"
  - question: "Does the F_4 lattice model have a QMC sign problem?"
    priority: MEDIUM
    blocks_phase: "none"
  - question: "Is the cubic det(A) invariant RG-relevant in d=3?"
    priority: MEDIUM
    blocks_phase: "none"
  - question: "Does the 3D F_4/Spin(9) sigma model satisfy Wightman axioms?"
    priority: LOW
    blocks_phase: "none"

contradictions_unresolved:
  - claim_a: "METHODS.md: Peirce decomposition gives bipartite-LIKE structure"
    claim_b: "PITFALLS.md: K_3 is definitively NOT bipartite"
    source_a: "METHODS.md, Method 4"
    source_b: "PITFALLS.md, Pitfall 1"
    investigation_needed: "Phase 38 must clarify: the Peirce K_3 is on-site algebraic structure, not lattice geometry. The lattice model on Z^d IS bipartite (checkerboard). METHODS.md conflates the two; PITFALLS.md correctly flags K_3 but the physical lattice is Z^d."
  - claim_a: "METHODS.md: frame stabilizer may be Spin(8) (dim 28, giving 24 broken generators)"
    claim_b: "METHODS.md: frame stabilizer may be G_2 (dim 14, giving 38 broken generators)"
    source_a: "METHODS.md, Method 2"
    source_b: "METHODS.md, Method 2"
    investigation_needed: "Frame stabilizer in F_4 is not settled. Phase 38 must compute H_eff to determine which stabilizer is realized. The sigma model target space, Goldstone count, and universality class all depend on this."
```
