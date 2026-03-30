# Research Summary

**Project:** Continuum Limit from Finite-Dimensional Observer (v9.0)
**Domain:** Quantum information geometry / Quantum lattice systems / Emergent spacetime
**Researched:** 2026-03-29
**Confidence:** MEDIUM

## Unified Notation

| Symbol | Quantity | Units/Dimensions | Convention Notes |
|--------|---------|-----------------|-----------------|
| g_F^{ij}(x) | Quantum Fisher information metric (SLD) on reduced states | [length]^{-2} in lattice units | g_F = 4 g_Bures; use SLD convention throughout |
| rho_Lambda(x) | Reduced density matrix of subsystem Lambda at lattice position x | dimensionless (trace 1) | Mixed state; obtained by partial trace of ground state |
| L_mu | Symmetric logarithmic derivative in direction mu | dimensionless | Defined by d_mu rho = (rho L_mu + L_mu rho)/2 |
| gamma | Spectral gap above ground state | [energy] = J | Hastings-Koma convention; NOT the Euler-Mascheroni constant |
| v_LR | Lieb-Robinson velocity | [lattice sites]/[time] | Rigorous upper bound on signal speed; v_LR >= c_s (spin-wave velocity) |
| c_s | Spin-wave velocity | [lattice sites]/[time] | Physical propagation speed in Neel-ordered phase; c_s <= v_LR |
| xi | Correlation length | [lattice sites] | xi = O(v_LR / gamma) for gapped systems |
| a | Lattice spacing | [length] | Consistent with Paper 6 |
| K_A | Modular Hamiltonian | dimensionless | K_A = -ln(rho_A); consistent with Paper 6 |
| S(A) | Entanglement entropy | dimensionless | S(A) = -Tr(rho_A ln rho_A); consistent with Paper 6 |
| F(rho, sigma) | Quantum fidelity | dimensionless | F = [Tr sqrt(sqrt(rho) sigma sqrt(rho))]^2 |
| g_{ij} | Spatial Fisher metric (Riemannian, d-dimensional) | [length]^{-2} | Indices i,j = 1..d for spatial directions ONLY |
| g_{mu nu} | Spacetime metric (Lorentzian) | [length]^{-2} | Indices mu,nu = 0..d; signature (-,+,...,+); assembled from g_ij + modular flow |

**Conventions:** Natural units (hbar = 1, k_B = 1). Lattice spacing a = 1 unless taking continuum limit. Fourier convention: e^{-ikx} forward. Coupling J > 0 for antiferromagnetic SWAP Hamiltonian. SLD Fisher metric (largest monotone metric) is the default; all statements about "the Fisher metric" refer to SLD unless otherwise noted.

**Notation conflicts resolved:** (1) g_{ij} is SPATIAL Riemannian Fisher metric; g_{mu nu} is SPACETIME Lorentzian metric. Never conflate. (2) gamma is spectral gap (Hastings-Koma), not Euler constant or Lorentz factor. (3) "Fisher metric" always means quantum (SLD) Fisher metric on density matrices, never classical Fisher information on measurement outcomes. (4) v_LR (rigorous bound) is distinct from c_s (physical spin-wave velocity); the emergent speed of light is identified with c_s, not v_LR.

## Executive Summary

The v9.0 milestone aims to close all four Paper 6 gaps by establishing the derivation chain: finite-dimensional C*-observer + SWAP lattice + correlation decay -> smooth Fisher manifold -> emergent Lorentz invariance -> Bisognano-Wichmann -> Jacobson -> Einstein equations. The research survey reveals that each link in this chain rests on well-established mathematical physics, but the connections between links contain genuine gaps that require careful treatment. The overall approach is sound and the recommended path is clear, but the honest confidence level is MEDIUM because the hardest step -- establishing smooth Fisher geometry for the gapless Neel-ordered phase in d >= 2 -- lacks rigorous proof.

The recommended theoretical approach combines five analytical methods (QFI metric extraction, Nachtergaele-Sims clustering, reflection positivity, modular flow for Lorentzian signature, Osterwalder-Schrader reconstruction) with exact diagonalization on N = 8-20 lattices for numerical verification. The Fisher information metric on reduced density matrices {rho_Lambda(x)} parametrized by lattice position is the central geometric object. The SLD Fisher metric is the correct choice (largest monotone metric, operational meaning via Cramer-Rao, agrees with all others on pure states). The computational cost is modest -- the full pipeline runs on a laptop in under an hour for the primary 1D systems, and 2D 4x4 lattices are feasible.

The principal risks are: (1) the Heisenberg AFM in d >= 2 is gapless due to Goldstone modes, so Hastings-Koma exponential clustering does not apply directly -- the Fisher geometry must work with algebraic correlation decay or route through the nonlinear sigma model effective theory; (2) von Ignatowsky requires continuous spatial isotropy, but the lattice has only discrete rotational symmetry -- emergent isotropy must be established before the theorem can be invoked; (3) the BW theorem requires Lorentz invariance as input, creating a sequential dependency that must be respected (not circular, but each step must be independently established). These risks are all manageable with the two-tier strategy (rigorous results for tractable cases, physical arguments for the general case) recommended by the methods survey.

## Key Findings

### Computational Approaches

The computational infrastructure extends the existing ED framework (code/ed_entanglement.py) with a new ~400-line module for Fisher metric computation. The algorithm is the eigendecomposition-based SLD formula, which is numerically stable, handles rank-deficient states naturally (by dropping zero eigenvalues), and avoids the catastrophic failure of matrix logarithm approaches. [CONFIDENCE: HIGH]

**Core approach:**

- **Eigendecomposition QFIM** (Algorithm 1): Central algorithm computing g_{ij} = sum_{m,n} 2|<m|d_mu rho|n>|^2 / (p_m + p_n) -- exact given eigensystem, O(d^3) per point, cross-validated against Bures fidelity metric
- **Subsystem sliding window**: Parametrize reduced states by lattice position x; central finite differences for d_mu rho with O(a^2) accuracy
- **Correlation function extraction**: Direct two-point correlators from ground state for exponential/power-law decay fitting
- **Geodesic distance via Dijkstra**: Weighted graph shortest path on Fisher metric to test distance recovery claim

**Critical computational finding:** On PBC lattices with exact translation symmetry, rho_Lambda(x) is x-independent and the Fisher metric is identically zero. Must use OBC or break translation invariance. This is not a bug -- it is a consequence of the geometry being trivial (flat) when the lattice has perfect symmetry. The nontrivial geometry emerges from boundary effects or symmetry breaking, which is the physically relevant regime.

### Prior Work Landscape

The derivation chain rests on a sequence of established results, each HIGH confidence individually, connected by new arguments that are MEDIUM confidence. [OVERALL CONFIDENCE: MEDIUM]

**Must reproduce (benchmarks):**

- Hastings-Koma: spectral gap gamma > 0 implies |<AB> - <A><B>| <= C exp(-d/xi) with xi = O(v_LR/gamma) -- the bridge from gap to smooth Fisher manifold [HIGH]
- Zanardi-Giorda-Cozzini (2007): Fisher metric scalar curvature diverges at quantum phase transitions -- benchmark for Fisher metric computation on TFI model [HIGH]
- Lattice BW (Giudici et al. 2018): entanglement Hamiltonian H_ent ~ sum_x x_perp h_x accurate to few percent when low-energy theory is Lorentz-invariant -- consistency check for Phase D [HIGH]
- Calabrese-Cardy: S(L) = (c/3) ln(L/a) for 1D CFT with c = 1 for SU(2)_1 WZW -- controls the d=1 Fisher geometry [HIGH]

**Novel predictions (contributions):**

- Fisher metric g_F on {rho_Lambda(x)} is smooth, positive-definite, and recovers lattice distance in the bulk
- Modular flow + spatial Fisher metric assembles into Lorentzian spacetime metric ds^2 = -N^2 dt^2 + g_{ij} dx^i dx^j
- Complete chain from finite-dim observer to Einstein equations with all steps explicit

**Defer (future work):**

- General n > 2 results (SU(n) Heisenberg phase diagram is an active research area; n = 2 is the tractable case)
- Full Osterwalder-Schrader verification for d >= 2 effective theory (open problem in constructive QFT, related to Clay Millennium)
- DMRG extension to N > 100 (requires ITensor/TeNPy setup; not needed for proof-of-concept)

### Methods and Tools

Six analytical/numerical methods form the toolkit, ordered by centrality to the argument. The Fisher metric extraction (Method 1) and exponential clustering analysis (Method 2) are the core. The Lorentzian signature construction (Method 4) via modular flow is the conceptual bridge. OS reconstruction (Method 5) and numerical Fisher computation (Method 6) provide verification. [CONFIDENCE: HIGH for individual methods, MEDIUM for the chain]

**Major components:**

1. **QFI metric on reduced density matrices** -- the central geometric object; parametrized by lattice position x
2. **Nachtergaele-Sims exponential clustering** -- proves gap -> smooth Fisher manifold; the rigorous backbone
3. **Modular flow for Lorentzian signature** -- Fisher = spatial metric, modular flow = time; assembles into spacetime
4. **von Ignatowsky + emergent isotropy** -- LR finite speed + continuum-limit isotropy -> Lorentz group
5. **Osterwalder-Schrader reconstruction** -- rigorous path from Euclidean lattice to Lorentzian Wightman QFT
6. **Numerical ED pipeline** -- N=8-20 1D, 4x4 2D; Fisher metric, correlations, geodesics, BW check

### Critical Pitfalls

The pitfalls survey identified 10 pitfalls (7 critical, 3 moderate), of which 3 require structural attention and 4 are avoidable with careful framing. [CONFIDENCE: HIGH -- pitfalls are well-grounded in theorems and counterexamples]

1. **Signature problem (P1)** -- Fisher metric is Riemannian by construction (positive-definite, theorem of Braunstein-Caves). It CANNOT be Lorentzian. Avoid by: Fisher = spatial metric; Lorentzian signature assembled via modular flow + LR causal structure + von Ignatowsky. Recovery cost: LOW (correct approach already planned).

2. **Discrete isotropy gap (P2)** -- von Ignatowsky requires continuous SO(d) isotropy; lattice has only O_h (order 48 in 3D). Lattice artifacts break isotropy at O(a^4) (fourth moment). Avoid by: establish emergent isotropy in continuum limit via universality, compute v_LR anisotropy numerically. Recovery cost: MEDIUM.

3. **Gapless Goldstone modes (P3)** -- THE hardest pitfall. Heisenberg AFM in d >= 2 has Neel order -> gapless magnons -> algebraic (not exponential) correlation decay. Hastings-Koma does not apply. Avoid by: two-tier strategy (rigorous for gapped cases n >= 3 or easy-axis; physical argument for isotropic n = 2 via nonlinear sigma model). Recovery cost: HIGH.

4. **BW circularity (P4)** -- BW requires Lorentz as input. Avoid by: strict phase ordering (Lorentz established in Phase C BEFORE BW applied in Phase D). Recovery cost: LOW.

5. **QFI rank singularities (P5)** -- SLD Fisher metric diverges at rank-changing points. In Neel phase, sublattice rho is nearly rank-1, creating large Fisher distances between sublattices. Avoid by: verify full-rank property of reduced states, coarse-grain over unit cells, or switch to Bures metric at singular points. Recovery cost: MEDIUM.

## Approximation Landscape

| Method | Valid Regime | Breaks Down When | Controlled? | Complements |
|--------|-------------|-----------------|-------------|-------------|
| Hastings-Koma clustering | gamma > 0 (gapped systems) | Gapless: Goldstone modes, critical points | Yes (xi = v_LR/gamma) | NL sigma model for gapless |
| Spin-wave theory (NL sigma model) | Neel-ordered, d >= 2, T << J | T ~ T_N or quantum melting | Yes (1/S expansion) | Hastings-Koma for gapped phases |
| ED (N = 8-20) | Small systems, any coupling | N > 22 (memory); finite-size effects | Yes (exact for given N) | DMRG for N > 20 in 1D |
| Fisher metric (SLD) | Full-rank rho | Rank changes (p_m + p_n -> 0) | Yes (Bures as fallback) | Bures metric at singular points |
| von Ignatowsky | Continuous isotropy + finite v_max | Discrete lattice symmetry; v_max = infinity (Galilean) | No (requires additional isotropy input) | Universality argument for emergent isotropy |
| Modular flow (Connes-Rovelli) | Faithful state on type III algebra | Lattice algebras are type I (finite dim) | Partially (physical argument) | OS reconstruction for rigorous path |
| OS reconstruction | Reflection-positive lattice theory | Non-reflection-positive Hamiltonians | Yes (standard constructive QFT) | Modular flow for physical insight |

**Coverage gap:** The regime d = 2, n = 2 (isotropic SU(2) Heisenberg AFM at T = 0) has NO fully rigorous method establishing smooth Fisher geometry. Neel order is proved only for S >= 3/2 (DLS 1978), and even with Neel order, Goldstone modes prevent exponential clustering. This is the critical gap. The nonlinear sigma model effective theory provides a physical argument but not a rigorous proof. For the 1D case (gapless WZW CFT), the Fisher metric is controlled by conformal symmetry and is well-defined despite algebraic correlations.

## Theoretical Connections

### Structural Parallels

1. **Fisher metric <-> Fubini-Study metric** [ESTABLISHED]: On pure states, g_F reduces to 4 x g_FS. On mixed states (our regime), g_F is the natural extension. The manifold {rho_Lambda(x)} is a submanifold of the space of density matrices, and g_F is the pullback of the Bures geometry to this submanifold.

2. **Lieb-Robinson <-> speed of light** [ESTABLISHED → CONJECTURED bridge]: v_LR provides a rigorous finite maximum signal speed. The emergent speed of light is c_s (spin-wave velocity), which satisfies c_s <= v_LR. The identification requires showing that the continuum limit selects c_s (not v_LR) as the invariant speed. This is physically clear (v_LR is a loose bound; c_s is the physical dispersion) but not rigorously established.

3. **Modular flow <-> time direction** [CONJECTURED]: The Connes-Rovelli thermal time hypothesis identifies physical time with modular flow. In the BW context, modular flow = Lorentz boost. This connection assembles the full Lorentzian metric from spatial Fisher geometry + modular time. Already used in Paper 6; v9.0 makes it explicit.

4. **Fisher singularities <-> quantum phase transitions** [ESTABLISHED]: Zanardi et al. (2007) proved that Fisher metric curvature diverges at QPTs. This means the Fisher geometry naturally encodes the phase structure of the lattice system. For v9.0, this is both a feature (the geometry is physically meaningful) and a constraint (must avoid QPT points where the metric is singular).

5. **Nonlinear sigma model <-> emergent Lorentz** [ESTABLISHED in condensed matter]: The Neel-ordered Heisenberg AFM's low-energy theory is an O(3) NL sigma model with Lorentz-invariant dispersion omega = c_s |k|. This provides a concrete mechanism for emergent Lorentz invariance that does NOT require the full von Ignatowsky argument -- the NL sigma model IS Lorentz-invariant by construction. This is arguably the strongest route to Lorentz for the d >= 2 case.

### Cross-Validation Opportunities

| | Bures/Fidelity | Correlation Functions | Lattice BW | Entanglement Entropy |
|---|:---:|:---:|:---:|:---:|
| **Fisher metric (SLD)** | Must agree (factor 4) at full-rank points | Fisher metric scale ~ 1/xi^2 | BW accuracy confirms Lorentz | g_F ~ eta/a^{d-1} where eta = S/|dA| |
| **Correlation functions** | -- | -- | BW predicts linear-weighted H_ent | Calabrese-Cardy benchmark |
| **Lattice BW** | -- | -- | -- | Entanglement spectrum from BW must match exact |

### Critical Claim Verification

| # | Claim | Source | Verification | Result |
|---|-------|--------|-------------|--------|
| 1 | Spectral gap implies exponential clustering | METHODS.md, PRIOR-WORK.md | web_search: Hastings-Koma 2006 CMP 265 | CONFIRMED -- published Springer, 700+ citations |
| 2 | von Ignatowsky: isotropy + finite speed -> Lorentz or Galilean | PRIOR-WORK.md, METHODS.md | web_search: Ignatowsky theorem derivation | CONFIRMED -- requires continuous isotropy (caveat noted: lattice has only discrete) |
| 3 | Frustration-free systems have z >= 2 | PITFALLS.md (P9) | web_search: PRX 15, 041050 (2025) | CONFIRMED -- SWAP/Heisenberg AFM is NOT frustration-free, so bound does not apply |
| 4 | Lattice BW accurate only when low-energy theory is Lorentz-invariant | PITFALLS.md (P4), PRIOR-WORK.md | web_search: Giudici et al. 2018 PRB 98 | CONFIRMED -- accuracy degrades for non-relativistic systems |
| 5 | QFI is discontinuous at rank-changing points | PITFALLS.md (P5), COMPUTATIONAL.md | web_search: Safranek 2017 PRA 95 | CONFIRMED -- Bures metric provides continuous extension |
| 6 | Heisenberg AFM d >= 2 has Neel order and gapless Goldstone modes | PITFALLS.md (P3), PRIOR-WORK.md | Dyson-Lieb-Simon 1978 (textbook result) | CONFIRMED -- standard condensed matter; prevents exponential clustering |

## Implications for Research Plan

Based on the analysis, the derivation chain has a natural five-phase structure determined by logical dependencies. The ordering is dictated by the physics: spatial geometry must precede Lorentzian structure, which must precede BW, which must precede Jacobson.

### Phase A: Fisher Geometry on Reduced States

**Rationale:** The Fisher metric g_F on {rho_Lambda(x)} is the foundational geometric object. Everything downstream depends on it being well-defined, smooth, and positive-definite. Must be established first.
**Delivers:** Numerical Fisher metric on N = 8-20 lattices (1D OBC and 2D 4x4); positive-definiteness verification; smoothness check (discrete second derivatives); geodesic distance recovery; cross-validation SLD vs Bures.
**Validates:** Zanardi et al. (2007) Fisher metric at TFI critical point (benchmark). PBC translation-invariance check (g = 0, expected). Full-rank property of reduced density matrices.
**Avoids:** P5 (QFI singularities -- verify rank), P10 (sublattice Fisher distance -- check Neel-ordered states explicitly), PBC pitfall (use OBC).
**Methods:** Fisher metric extraction (Method 1), numerical computation (Method 6), smoothness verification (Method 3).
**Cost:** 2-4 hours computation, 10-15 hours derivation/writeup.

### Phase B: Correlation Decay and Spectral Analysis

**Rationale:** The correlation decay law determines whether the Fisher manifold is smooth in the thermodynamic limit. This is the hardest link -- must honestly confront the gapless Goldstone problem in d >= 2.
**Delivers:** Rigorous statement of exponential clustering for gapped cases (AKLT, easy-axis, n >= 3); physical argument for n = 2 d >= 2 via NL sigma model; numerical correlation functions on ED lattices; two-tier confidence assessment.
**Uses:** Nachtergaele-Sims framework (Method 2), ED correlation computation (Algorithm 4).
**Builds on:** Phase A (Fisher metric must be computed to check how it responds to algebraic vs exponential decay).
**Avoids:** P3 (gapless Goldstone -- two-tier strategy), P8 (general n -- restrict rigorous claims to n = 2, flag n > 2 as conjecture).
**Risk:** HIGH -- if the Fisher geometry does not survive algebraic decay, the d >= 2 argument fails.

### Phase C: Emergent Lorentz Invariance

**Rationale:** Lorentz invariance must be established independently of BW (to avoid circularity P4). Two routes: (i) von Ignatowsky on the effective continuum theory after establishing emergent isotropy, (ii) direct identification of NL sigma model as Lorentz-invariant effective theory.
**Delivers:** Argument for emergent continuous isotropy from lattice universality class; von Ignatowsky application to effective theory; identification of c_s as invariant speed; numerical v_LR anisotropy computation showing convergence toward isotropy.
**Builds on:** Phase B (NL sigma model identification requires knowing the correlation structure).
**Avoids:** P2 (discrete isotropy -- establish emergent isotropy first), P9 (frustration-free bound -- state that SWAP is frustrated, cite PRX 2025).
**Risk:** MEDIUM -- the NL sigma model route is well-established in condensed matter; the von Ignatowsky route requires more care.

### Phase D: BW and Entanglement Equilibrium

**Rationale:** With Lorentz invariance from Phase C, BW theorem identifies modular Hamiltonian with boost generator. This gives the thermal/Unruh structure needed for Jacobson.
**Delivers:** Statement of BW for the effective Lorentz-invariant theory; numerical lattice BW check (compare entanglement Hamiltonian eigenvalues to linearly-weighted local Hamiltonian); modular Hamiltonian identification.
**Uses:** Modular flow (Method 4), OS reconstruction check (Method 5).
**Builds on:** Phase C (Lorentz invariance required BEFORE BW).
**Avoids:** P4 (circularity -- BW comes AFTER Lorentz, not before).
**Risk:** LOW -- BW is a theorem once Lorentz is established; lattice BW is well-tested numerically.

### Phase E: Assembly and Gap Closure

**Rationale:** Assemble the full chain and score each Paper 6 gap individually (CLOSED, NARROWED, OPEN).
**Delivers:** Complete derivation chain with explicit assumptions at each step; individual gap assessments; honest calibration of "effective smoothness" vs "continuum limit"; list of all remaining assumptions.
**Builds on:** All prior phases.
**Avoids:** P6 (observer-cutoff overclaim -- distinguish effective smoothness from continuum limit), P7 (all-four-gaps overclaim -- score each gap independently).
**Risk:** MEDIUM -- the risk is overclaiming, not technical failure. Honest assessment is the mitigation.

### Phase Ordering Rationale

- A before B: Fisher metric computation needed to numerically test correlation decay effects on geometry
- B before C: correlation structure determines the effective theory (NL sigma model vs CFT), which determines the Lorentz argument
- C before D: Lorentz invariance is a prerequisite for BW (not circular, sequential)
- D before E: BW + Jacobson argument cannot be stated until modular Hamiltonian is identified
- A and the first part of B can partially overlap (Fisher metric computation and correlation function computation are independent at the numerical level)

### Phases Requiring Deep Investigation

Phases likely needing additional theoretical or computational exploration:

- **Phase B:** Hardest link. The gapless Goldstone problem in d >= 2 has no clean resolution in the literature. The NL sigma model argument is physical, not rigorous. May need to restrict strong claims to gapped phases and frame d >= 2 isotropic SU(2) as conditional.
- **Phase C:** The discrete-to-continuous isotropy transition requires care. Lattice universality arguments are standard in condensed matter but not usually stated in the form needed for von Ignatowsky.

Phases with established methodology (straightforward execution):

- **Phase A:** Fisher metric computation is standard quantum information geometry. Algorithms are well-documented. Primary risk is numerical (finite-size effects), not conceptual.
- **Phase D:** BW on lattice is extensively studied (Giudici 2018, arXiv:2511.00950). Once Lorentz is established, this phase follows known procedures.

## Confidence Assessment

| Area | Confidence | Notes |
|------|-----------|-------|
| Computational Approaches | HIGH | Eigendecomposition QFIM is standard, well-validated, cheap. ED infrastructure exists. |
| Prior Work | HIGH | All foundational results are textbook-level or well-cited published papers. |
| Methods | MEDIUM-HIGH | Individual methods are solid. The chain connecting them (especially correlation decay -> smooth Fisher manifold in gapless regime) is the weak link. |
| Pitfalls | HIGH | Well-grounded in theorems and counterexamples. Recovery strategies identified for each. |

**Overall confidence:** MEDIUM

### Gaps to Address

- **Gapless Fisher geometry (critical):** Does the Fisher metric on reduced states remain smooth and positive-definite when correlations decay algebraically (Goldstone modes, d >= 2)? No rigorous answer exists. Must resolve in Phase B or restrict claims to gapped systems.
- **Emergent isotropy quantification:** How fast does lattice anisotropy vanish with increasing scale? Needs numerical measurement of v_LR directional dependence. Must resolve in Phase C.
- **Sublattice Fisher distance:** In the Neel phase, rho alternates between sublattices. Does coarse-graining over unit cells produce a smooth Fisher metric? Must resolve in Phase A.
- **Modular flow on lattice:** Connes-Rovelli thermal time applies to type III algebras; lattice algebras are type I (finite-dimensional). The physical argument is that the effective continuum theory is type III, but this is the continuum limit assumption. Must handle carefully in Phase D/E.
- **Gap 2 (conformal approximation) resolution:** The Heisenberg AFM in d >= 2 is NOT conformal (Neel order breaks symmetry). Route A (conformal modular Hamiltonian) may not apply. Route B (Lovelock tensoriality) avoids this but requires separate argument. Must choose route in Phase E.

## Open Questions

1. **Is the Fisher metric smooth for the gapless Neel-ordered Heisenberg AFM in d >= 2?** Priority: HIGH. Blocks Phase B and conditionally all downstream phases for the d >= 2 case.

2. **Does coarse-graining over unit cells resolve the sublattice alternation in the Fisher metric?** Priority: HIGH. Blocks Phase A interpretation for Neel-ordered systems.

3. **How does the lattice anisotropy of v_LR scale with system size?** Priority: MEDIUM. Needed for Phase C quantitative argument but not a conceptual blocker.

4. **Which Paper 6 gap-closing route (A: conformal, B: Lovelock) is compatible with Neel order?** Priority: MEDIUM. Needed for Phase E but can be deferred until Phase C establishes the effective theory.

5. **Can the BW-like modular structure be derived without assuming Lorentz invariance?** Priority: LOW for v9.0 (we derive Lorentz first). Would strengthen the argument if achievable.

## Sources

### Primary (HIGH)

- Hastings-Koma, CMP 265 (2006) 781, arXiv:math-ph/0507008 -- Spectral gap implies exponential clustering
- Nachtergaele-Sims, CMP 265 (2006) 119, arXiv:math-ph/0506030 -- LR bounds and exponential clustering
- Nachtergaele-Sims-Young, JMP 60 (2019) 061101, arXiv:1810.02428 -- Comprehensive quasi-locality bounds
- Bisognano-Wichmann, JMP 16 (1975) 985; JMP 17 (1976) 303 -- Modular Hamiltonian = boost generator
- Jacobson, PRL 116 (2016) 201101, arXiv:1505.04753 -- Entanglement equilibrium and Einstein equation
- Dyson-Lieb-Simon, J. Stat. Phys. 18 (1978) 335 -- Neel order in Heisenberg AFM
- Zanardi-Giorda-Cozzini, PRL 99 (2007) 100603, arXiv:quant-ph/0701061 -- Fisher metric and QPTs
- Petz, LAA 244 (1996) 81 -- Classification of quantum monotone metrics
- Braunstein-Caves, PRL 72 (1994) 3439 -- Quantum Fisher information metric
- Ignatowsky, Phys. Z. 11 (1910) 972; Levy-Leblond, Am. J. Phys. 44 (1976) 271 -- Lorentz from isotropy
- Connes-Rovelli, CQG 11 (1994) 2899 -- Thermal time hypothesis
- Osterwalder-Schrader, CMP 31 (1973) 83; CMP 42 (1975) 281 -- Euclidean QFT axioms
- Calabrese-Cardy, JSTAT P06002 (2004) -- Entanglement entropy in CFT

### Secondary (MEDIUM)

- Giudici et al., PRB 98 (2018) 134403, arXiv:1807.01322 -- Lattice BW entanglement Hamiltonians
- Cao-Carroll-Michalakis, PRD 95 (2017) 024031, arXiv:1606.08444 -- Space from Hilbert space
- Safranek, PRA 95 (2017) 052320, arXiv:1612.04581 -- QFI discontinuities at rank changes
- Liu-Peng-Yuan, J. Phys. A 53 (2020) 023001, arXiv:1907.08037 -- QFIM computation review
- Kennedy-Lieb-Shastry, J. Stat. Phys. 53 (1988) 1019 -- Neel order for S = 1/2 in d >= 3
- PRX 15, 041050 (2025), arXiv:2406.06415 -- z >= 2 for frustration-free systems
- arXiv:2511.00950 -- QMC study of lattice BW limits

### Tertiary (LOW)

- Matsueda, arXiv:1310.1831 (2013) -- Emergent GR from Fisher metric (suggestive, not rigorous)
- arXiv:2512.15450 -- Lorentzian signature emergence from spectral triples (frontier mathematics)

---

_Research analysis completed: 2026-03-29_
_Ready for research plan: yes_

```yaml
# --- ROADMAP INPUT (machine-readable, consumed by gpd-roadmapper) ---
synthesis_meta:
  project_title: "Continuum Limit from Finite-Dimensional Observer (v9.0)"
  synthesis_date: "2026-03-29"
  input_files: [METHODS.md, PRIOR-WORK.md, COMPUTATIONAL.md, PITFALLS.md]
  input_quality: {METHODS: good, PRIOR-WORK: good, COMPUTATIONAL: good, PITFALLS: good}

conventions:
  unit_system: "natural"
  metric_signature: "mostly_plus"
  fourier_convention: "physics"
  coupling_convention: "J > 0 antiferromagnetic; SWAP = Heisenberg + const"
  renormalization_scheme: "N/A"

methods_ranked:
  - name: "QFI metric on reduced density matrices (SLD eigendecomposition)"
    regime: "Full-rank rho_Lambda, any lattice size N <= 20 (ED), any d"
    confidence: HIGH
    cost: "O(2^N) for ground state + O(d^3) per QFIM entry where d = 2^|Lambda|"
    complements: "Bures fidelity metric (cross-validation at rank-deficient points)"
  - name: "Nachtergaele-Sims exponential clustering"
    regime: "Gapped systems (gamma > 0); n >= 3 in d = 1, n = 2 d >= 3 with anisotropy"
    confidence: HIGH
    cost: "Literature assembly, no computation"
    complements: "NL sigma model for gapless d >= 2"
  - name: "Nonlinear sigma model effective theory"
    regime: "Neel-ordered phase, d >= 2, T << J"
    confidence: MEDIUM
    cost: "Analytical derivation, ~10-20 hours"
    complements: "Hastings-Koma for gapped phases"
  - name: "Modular flow (Connes-Rovelli thermal time)"
    regime: "Effective continuum theory with faithful state"
    confidence: MEDIUM
    cost: "Conceptual/derivation work, ~10-20 hours"
    complements: "OS reconstruction for rigorous verification"
  - name: "von Ignatowsky + emergent isotropy"
    regime: "Effective continuum theory with emergent SO(d) symmetry"
    confidence: MEDIUM
    cost: "Analytical + numerical (v_LR anisotropy), ~15-25 hours"
    complements: "NL sigma model Lorentz invariance (direct route)"
  - name: "Exact diagonalization (N = 8-20)"
    regime: "N <= 20 (1D), N <= 16 (2D 4x4)"
    confidence: HIGH
    cost: "< 1 hour total compute for full pipeline"
    complements: "DMRG for N > 20 (deferred)"

phase_suggestions:
  - name: "Phase A: Fisher Geometry"
    goal: "Establish that Fisher metric on reduced states is smooth, positive-definite, and recovers lattice distance"
    methods: ["QFI metric on reduced density matrices (SLD eigendecomposition)", "Exact diagonalization (N = 8-20)"]
    depends_on: []
    needs_research: false
    risk: MEDIUM
    pitfalls: ["P5-qfi-rank-singularities", "P10-fisher-lattice-distance"]
  - name: "Phase B: Correlation Decay"
    goal: "Prove exponential clustering for gapped cases; physical argument for gapless d >= 2 via NL sigma model"
    methods: ["Nachtergaele-Sims exponential clustering", "Nonlinear sigma model effective theory", "Exact diagonalization (N = 8-20)"]
    depends_on: ["Phase A: Fisher Geometry"]
    needs_research: true
    risk: HIGH
    pitfalls: ["P3-gapless-goldstone", "P8-general-n-harder"]
  - name: "Phase C: Emergent Lorentz"
    goal: "Establish emergent Lorentz invariance from isotropy + LR finite speed or NL sigma model"
    methods: ["von Ignatowsky + emergent isotropy", "Nonlinear sigma model effective theory", "Exact diagonalization (N = 8-20)"]
    depends_on: ["Phase B: Correlation Decay"]
    needs_research: true
    risk: MEDIUM
    pitfalls: ["P2-discrete-isotropy", "P9-frustration-free-bound"]
  - name: "Phase D: BW and Equilibrium"
    goal: "Apply BW theorem to effective Lorentz-invariant theory; verify lattice BW numerically"
    methods: ["Modular flow (Connes-Rovelli thermal time)", "Exact diagonalization (N = 8-20)"]
    depends_on: ["Phase C: Emergent Lorentz"]
    needs_research: false
    risk: LOW
    pitfalls: ["P4-bw-circularity"]
  - name: "Phase E: Assembly and Gap Closure"
    goal: "Assemble full chain; score each Paper 6 gap; write rigorous derivation"
    methods: ["Modular flow (Connes-Rovelli thermal time)"]
    depends_on: ["Phase D: BW and Equilibrium"]
    needs_research: false
    risk: MEDIUM
    pitfalls: ["P6-observer-cutoff-overclaim", "P7-all-four-gaps-overclaim"]

critical_benchmarks:
  - quantity: "Hastings-Koma clustering bound"
    value: "|<AB> - <A><B>| <= C exp(-d/xi), xi = O(v_LR/gamma)"
    source: "Hastings-Koma CMP 265 (2006)"
    confidence: HIGH
  - quantity: "TFI Fisher metric divergence at criticality"
    value: "Scalar curvature of g_F diverges at h/J = 1"
    source: "Zanardi et al. PRL 99 (2007)"
    confidence: HIGH
  - quantity: "SU(2)_1 WZW entanglement entropy"
    value: "S(L) = (1/3) ln(L/a) + const (c = 1)"
    source: "Calabrese-Cardy JSTAT P06002 (2004)"
    confidence: HIGH
  - quantity: "Lattice BW accuracy"
    value: "Few-percent agreement when low-energy theory is Lorentz-invariant"
    source: "Giudici et al. PRB 98 (2018)"
    confidence: HIGH
  - quantity: "QFI = 4 x Bures (full-rank)"
    value: "g_F^{SLD} = 4 g^{Bures} for full-rank rho"
    source: "Braunstein-Caves PRL 72 (1994); Zhou-Jiang arXiv:1910.08473"
    confidence: HIGH

open_questions:
  - question: "Is the Fisher metric on reduced states smooth for the gapless Neel-ordered Heisenberg AFM in d >= 2?"
    priority: HIGH
    blocks_phase: "Phase B: Correlation Decay"
  - question: "Does coarse-graining over unit cells resolve sublattice alternation in Fisher metric?"
    priority: HIGH
    blocks_phase: "Phase A: Fisher Geometry"
  - question: "How does lattice anisotropy of v_LR scale with system size?"
    priority: MEDIUM
    blocks_phase: "Phase C: Emergent Lorentz"
  - question: "Which Paper 6 route (A: conformal, B: Lovelock) works for Neel-ordered systems?"
    priority: MEDIUM
    blocks_phase: "Phase E: Assembly and Gap Closure"

contradictions_unresolved:
  - claim_a: "v9.0 scoping contract says 'exponential decay proved rigorously for n=2'"
    claim_b: "Heisenberg AFM (n=2) in d >= 2 has algebraic (not exponential) correlation decay due to Goldstone modes"
    source_a: "PROJECT.md scoping contract"
    source_b: "Dyson-Lieb-Simon 1978; Goldstone theorem; PITFALLS.md P3"
    investigation_needed: "Clarify which correlators and which dimensions. Exponential holds for gapped cases only. For d >= 2 isotropic, must work with algebraic decay or restrict to connected longitudinal correlations."
```
