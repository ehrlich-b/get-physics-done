# Research Summary

**Project:** Experiential Measure on Structure Space -- v3.0 GR Extension
**Domain:** Quantum foundations / Quantum gravity / Thermodynamic gravity / Entanglement-gravity correspondence
**Researched:** 2026-03-21
**Confidence:** MEDIUM

## Unified Notation

| Symbol | Quantity | Units/Dimensions | Convention Notes |
|--------|---------|-----------------|-----------------|
| g_ab | Spacetime metric | dimensionless | Abstract index notation, signature (-,+,+,+) following Wald |
| G_ab | Einstein tensor | [length]^{-2} | G_ab = R_ab - (1/2) R g_ab |
| R_ab | Ricci tensor | [length]^{-2} | Follows from metric connection |
| T_ab | Stress-energy tensor | [mass][length]^{-3} | Source term in Einstein equations |
| S_EE | Entanglement entropy | dimensionless (natural units) | von Neumann: S_EE = -Tr(rho_A ln rho_A); distinguished from S_BH |
| S_BH | Bekenstein-Hawking entropy | dimensionless | S_BH = A/(4G) in natural units |
| I(A:B) | Mutual information | dimensionless | I(A:B) = S(A) + S(B) - S(AB) |
| K | Modular Hamiltonian | dimensionless | K = -ln(rho_A); generates modular flow |
| A_x | Local algebra at site x | -- | A_x = M_n(C), full matrix algebra |
| M_n(C)^sa | Self-adjoint part of n x n matrices | -- | The Jordan algebra from Paper 5 |
| theta | Expansion of null congruence | [length]^{-1} | Raychaudhuri variable |
| sigma_ab | Shear of null congruence | [length]^{-1} | Traceless part of expansion tensor |
| k^a | Null normal to horizon | [length]^{-1} | Affinely parametrized null generator |
| chi^a | Boost Killing vector | dimensionless | Approximate, at local Rindler horizon |
| v_LR | Lieb-Robinson velocity | [length]/[time] | Effective speed of information propagation |
| eta | Entropy density | [length]^{-2} | S = eta * A; eta = 1/(4G) |
| Delta | Spectral gap | [energy] | E_1 - E_0 for ground state |
| xi | Correlation length | [length] | Exponential decay scale of correlations |

**Unit system:** Natural units (hbar = c = k_B = 1) for all derivations. Restore factors only in final expressions.

**Metric signature:** (-,+,+,+) throughout, following Wald and Jacobson (2016). Note: Jacobson (1995) uses (+,-,-,-); signs in the Raychaudhuri equation must be adjusted when comparing.

**Convention conflicts resolved:**

1. Jacobson 1995 uses (+,-,-,-) while Jacobson 2016 and standard GR texts use (-,+,+,+). We adopt (-,+,+,+). The Raychaudhuri equation changes sign on the R_ab k^a k^b term: in our convention, d(theta)/d(lambda) = -(1/(D-2)) theta^2 - sigma^2 - R_ab k^a k^b (for geodesic, twist-free congruence).

2. "Entropy" appears in three senses: S_EE (entanglement), S_BH (Bekenstein-Hawking thermodynamic), and S_thermo (Clausius relation). Jacobson (2012, 2016) argues S_EE = S_BH for horizons; this identification is an input assumption, not a derived result.

3. "Area law" in condensed matter (S_EE proportional to boundary area of spatial region) vs. "area law" in black hole physics (S_BH proportional to horizon area). Same mathematical statement, different physical context. We unify: both are instances of entanglement entropy scaling with boundary area.

## Executive Summary

The v3.0 milestone aims to derive Einstein's field equations from the locality of self-modeling, extending the v2.0 result (self-modeling forces M_n(C)^sa) to gravity. The proposed derivation chain is: local self-modeling on a lattice of M_n(C)^sa systems produces area-law entanglement entropy; Jacobson's thermodynamic argument (1995/2016) converts area-law entropy into the Einstein field equations. The literature strongly supports the individual links: area laws for gapped local Hamiltonians are rigorously established in 1D (Hastings 2007) and for frustration-free 2D systems (Anshu-Arad-Gosset 2022), while Jacobson's thermodynamic derivation is widely accepted and has been refined over 30 years. The critical gap -- and the project's novel contribution -- is the bridge from self-modeling locality to the conditions that imply area-law entanglement. No prior work has connected a QM reconstruction program to emergent gravity.

The recommended approach is: (1) formalize self-modeling locality using the standard quantum lattice system framework (Bratteli-Robinson), (2) prove area-law entanglement via a channel capacity / mutual information bound that bypasses the need for a spectral gap, (3) apply Jacobson's 2016 "entanglement equilibrium" formulation (which uses entanglement entropy directly, avoiding the need for explicit Rindler horizons or Unruh temperature on the lattice), and (4) construct emergent spatial geometry from mutual information using the Cao-Carroll-Michalakis framework as a consistency check. The Jacobson 2016 formulation is strongly preferred over the 1995 version because it is more compatible with a lattice/discrete setting.

The principal risks are: (a) the self-modeling fixed point may not be a state with area-law entanglement (the "which state?" problem), (b) background dependence circularity (the lattice topology is an input, so "emergent geometry" means emergent metric, not emergent topology), and (c) Jacobson's argument requires a smooth manifold, but the self-modeling system is a finite lattice -- a continuum limit is needed but is an open problem in quantum gravity. These risks are manageable: (a) is addressed by the information-theoretic channel capacity route, (b) is mitigated by honest framing, and (c) is handled by adopting the standard Wilsonian perspective (lattice = UV, Einstein equations = IR effective description).

## Key Findings

### Prior Work Landscape

Three distinct programs derive gravity from entanglement, and their relative strengths determine the recommended approach:

**Program 1: Jacobson's Thermodynamic Gravity (1995, 2012, 2016).** Derives the full nonlinear Einstein equations from area-law entropy + Clausius relation + Unruh effect. Does NOT require AdS/CFT. Works in any spacetime dimension. This is the recommended terminus of the derivation chain because it produces the strongest result (full nonlinear equations) with the fewest framework assumptions. [CONFIDENCE: HIGH]

**Program 2: AdS/CFT Entanglement Gravity (FLM, LMVR, Van Raamsdonk).** Derives linearized Einstein equations from the entanglement first law within holographic CFTs. Requires the full AdS/CFT apparatus. Not suitable as the primary route because self-modeling systems are not CFTs with holographic duals. However, the conceptual insight -- that entanglement constraints determine gravitational dynamics -- transfers directly. [CONFIDENCE: HIGH for the results within AdS/CFT; NOT APPLICABLE to this project as primary method]

**Program 3: Emergent Geometry (Cao-Carroll-Michalakis 2017).** Constructs spatial geometry from entanglement structure of a quantum state in finite-dimensional Hilbert space. Produces a spatial analog of Einstein's equation from entanglement perturbations. Most directly compatible with the lattice framework. Gives spatial geometry only, not full spacetime dynamics. [CONFIDENCE: MEDIUM]

**No direct precedent exists** for deriving GR from self-modeling, self-reference, or similar operational premises. The novelty is genuine: no published work chains QM reconstruction to emergent gravity. Each individual link (self-modeling to M_n(C)^sa, area laws from locality, Jacobson's derivation) has strong precedent, but the complete chain is new.

**Must reproduce (benchmarks):**

- Jacobson's derivation: G_ab + Lambda g_ab = (8 pi G) T_ab from area-law entropy, in the continuum limit
- Area-law scaling: S(A) ~ |boundary(A)| for the relevant lattice state, not volume-law
- Lieb-Robinson bounds: finite propagation speed from local interactions

**Novel contributions:**

- Self-modeling locality forces area-law entanglement (the bridge argument)
- Complete chain from a single operational premise (self-modeling) to GR via QM
- Identification of which self-modeling state satisfies area-law conditions

### Methods and Tools

The v3.0 methods work ABOVE the C*-algebra level established in v2.0: we now HAVE M_n(C)^sa at each site and must derive consequences of assembling many such sites into a lattice with local interactions. Seven methods are identified, with a clear critical path.

**Critical path (sequential):**

1. **Quantum lattice system formalization** (Bratteli-Robinson framework) -- define the lattice with A_x = M_n(C) at each site, nearest-neighbor interactions encoding self-modeling coupling. [CONFIDENCE: HIGH, standard framework]
2. **Lieb-Robinson bounds** -- establish finite propagation speed and effective causal structure from local interactions. [CONFIDENCE: HIGH, rigorous theorems since 1972]
3. **Area-law entanglement** via channel capacity / mutual information bound -- the CRITICAL STEP. Four routes available, ranked by promise: (3D) channel capacity bound (most promising, requires pure global state), (3A) WVCH mutual information bound (requires thermal state identification), (3C) Brandao-Horodecki correlation decay (1D only), (3B) Hastings gapped ground state (1D only, requires gap). [CONFIDENCE: MEDIUM for applicability to self-modeling]
4. **Entanglement first law** -- delta S = delta <K> connects area-law perturbations to modular energy, bridging to Jacobson. [CONFIDENCE: MEDIUM-HIGH]
5. **Jacobson 2016 entanglement equilibrium** -- MVEH (vacuum maximizes entanglement entropy in small geodesic balls) implies Einstein's equations. Preferred over 1995 because it uses entanglement entropy directly. [CONFIDENCE: HIGH for the continuum result; MEDIUM for lattice adaptation]

**Supporting track (parallel):**

6. **Cao-Carroll-Michalakis emergent geometry** -- construct spatial geometry from mutual information matrix via MDS. Consistency check, not on the critical path. [CONFIDENCE: MEDIUM]
7. **MERA / holographic geometry** -- conceptual support showing area-law states can produce geometry. Not used as proof strategy. [CONFIDENCE: MEDIUM as conceptual framework]

**Rate-limiting step:** Method 3 (area-law entanglement from self-modeling locality). The bridge between self-modeling locality and the information-theoretic conditions for area-law scaling is the single most important methodological question.

### Computational Approaches

The v3.0 milestone is primarily proof work, not heavy numerics. Computation serves verification and illustration: small-scale numerical checks that area-law scaling holds for self-modeling lattices and that intermediate steps (entanglement first law) are numerically satisfied.

**Core approach:**

- Exact diagonalization (NumPy/SciPy) for lattices up to ~20 qubits / 10 M_2(C)^sa sites
- QuTiP for partial trace and entanglement entropy extraction
- Linear regression to distinguish area-law vs volume-law scaling

**Feasibility:** All computation is local laptop-scale. Sweet spots: 1D chain N=16-20 qubits and 2D 4x4 lattice (1 MB state vector, seconds to minutes). Total new code: ~300-400 lines of Python.

**Critical dependency:** All numerical computation is blocked until Phase 1 defines the self-modeling interaction Hamiltonian. Benchmark computations (Heisenberg chain, transverse Ising) can validate infrastructure in parallel.

### Critical Pitfalls

13 pitfalls identified, 8 critical and 5 moderate. The top 5:

1. **The "Which State?" Problem (P1)** -- Area laws hold for ground states of gapped local Hamiltonians, not generic states. **Avoid by:** using the information-theoretic channel capacity route (Route 3D), which does not require a Hamiltonian or spectral gap, only that the global state is pure and information flow is local.

2. **Background Dependence Circularity (P2)** -- The lattice connectivity is an input, so "emergent geometry" risks being tautological. **Avoid by:** separating claims: topology is input, metric is derived.

3. **Jacobson Requires Smooth Manifold (P3)** -- Rindler horizons, Raychaudhuri equation, and Unruh temperature do not exist on a finite lattice. **Avoid by:** using Jacobson 2016 (entanglement equilibrium) and the Wilsonian perspective (lattice = UV, continuum = IR).

4. **Spectral Gap Not Guaranteed (P4)** -- The gap is unproven for self-modeling and potentially undecidable (Cubitt-Perez-Garcia-Wolf 2015). **Avoid by:** using gap-free routes to area law.

5. **Continuum Limit is an Open Problem (P6)** -- No known rigorous route from finite lattice to smooth manifold. **Avoid by:** framing as leading-order effective description, analogous to lattice QCD.

## Approximation Landscape

| Method | Valid Regime | Breaks Down When | Controlled? | Complements |
|--------|------------|------------------|-------------|-------------|
| Hastings area law | 1D, gapped, local H | Gapless (log corrections); D > 1 (unproven) | Yes (expansion in 1/Delta) | Brandao-Horodecki (no gap needed) |
| Brandao-Horodecki | 1D, exponential correlation decay | Algebraic decay; D > 1 | Yes (expansion in xi) | Mutual info bound (works in all D) |
| WVCH mutual info bound | Any D, thermal states of local H | Not thermal; not local H | Yes (bound: beta * boundary * h) | Channel capacity (no H needed) |
| Channel capacity bound | Any D, pure global state, local info flow | Mixed global state; long-range channels | Yes (capacity = 2 log n per bond) | WVCH (handles thermal states) |
| Jacobson 1995 | Smooth manifold, local equilibrium | Non-equilibrium (gives f(R) gravity); lattice | No (assumes equilibrium exactly) | Jacobson 2016 |
| Jacobson 2016 | Conformal fields, first-order perturbations | Non-conformal (needs conjecture); higher order | Partially (first order) | CCM spatial Einstein analog |
| CCM emergent geometry | Finite-dim Hilbert space, area-law states | Non-area-law states; distance inconsistency | No (constructive) | Jacobson for dynamics |
| Exact diagonalization | N <= ~24 qubits | Memory overflow N > ~28 qubits | Yes (exact to machine precision) | DMRG for larger 1D |

**Coverage gap:** No controlled method for proving area-law entanglement in D > 1 for general gapped Hamiltonians. The channel capacity argument is dimension-independent but requires the pure-state condition.

## Theoretical Connections

### Entanglement First Law as Universal Bridge [ESTABLISHED]

The entanglement first law delta S = delta <K> is the common thread linking all three programs. In Jacobson: it is the Clausius relation rewritten in entanglement language. In FLM/LMVR: it gives linearized Einstein equations via Ryu-Takayanagi. On a lattice: it is an exact quantum information identity for first-order perturbations of any state. The lattice formulation is mathematically identical to the continuum -- only the interpretation of K changes.

### Modular Hamiltonian as Discrete Boost Generator [CONJECTURED]

In continuum QFT, the modular Hamiltonian of the vacuum restricted to a Rindler wedge IS the boost generator (Bisognano-Wichmann). On a lattice, K = -ln(rho_A) is well-defined but has no a priori geometric interpretation. The conjecture: for area-law states on lattices, K is approximately local (concentrated at the boundary of A), and in the continuum limit, K approaches the boost generator. This establishes the Unruh temperature through the modular Hamiltonian rather than through Lorentz invariance.

### Self-Modeling Locality as Information-Theoretic Locality [SPECULATIVE]

The deepest connection: the self-modeling constraint (model probes body through boundary) IS information-theoretic locality (mutual information bounded by channel capacity of intermediate bonds). If this identification holds, the area law follows immediately. This is the project's core hypothesis and its novel contribution.

### Area-Law Universality [ESTABLISHED]

Area-law entanglement appears across: condensed matter ground states, black hole horizons, Ryu-Takayanagi surfaces, tensor network states. The universality strongly suggests it is a fundamental constraint. The self-modeling project would add another instance from an operational/algebraic premise.

### Cross-Validation Matrix

|                      | Jacobson 2016 | CCM Geometry | Exact Diag. | Known Limits |
|:---------------------|:---:|:---:|:---:|:---:|
| Channel capacity (3D) | Area-law input | MI provides distances | S(A) scaling check | Flat: S = const/bond |
| Jacobson 2016        | -- | Compatible curvature | Equil. check | Flat: T=0, R=0 |
| CCM Geometry         | Spatial curvature | -- | MDS dim check | 1D chain -> 1D |

**High-risk gap:** The channel capacity argument has no independent cross-validation. If it fails, fallback to WVCH (thermal) or Brandao-Horodecki (1D only).

## Implications for Research Plan

### Phase 1: Locality Formalization

**Rationale:** Everything depends on precisely defining "local self-modeling" on a lattice. Must establish the lattice structure, interaction Hamiltonian, and mapping from self-modeling locality to Hamiltonian/information-theoretic locality.
**Delivers:** Formal lattice definition; interaction Hamiltonian H; locality axiom; Lieb-Robinson velocity.
**Methods:** Quantum lattice formalization, Lieb-Robinson bounds.
**Builds on:** Paper 5 (M_n(C)^sa, local tomography, composite structure).
**Avoids:** P2 (circularity), P9 (locality conflation).
**Risk:** MEDIUM.

### Phase 2: Area-Law Derivation

**Rationale:** The area law is the critical link. Must be established before Jacobson applies. This is the rate-limiting step and the novel contribution.
**Delivers:** Proof or strong argument that S(A) ~ |boundary(A)| for self-modeling lattice state.
**Methods:** Channel capacity (Route 3D) primary, WVCH (Route 3A) backup.
**Builds on:** Phase 1 (lattice, locality axiom).
**Avoids:** P1 (which state?), P4 (spectral gap), P11 (higher-D conjecture).
**Risk:** HIGH.

### Phase 3: Jacobson Application

**Rationale:** Once area-law entanglement is established, Jacobson 2016 converts it to Einstein's equations. Continuum limit argued physically, not proved rigorously.
**Delivers:** G_ab + Lambda g_ab = (8 pi G) T_ab from entanglement equilibrium; G = 1/(4 eta).
**Methods:** Jacobson 2016 entanglement equilibrium, entanglement first law.
**Builds on:** Phase 2 (area law), Phase 1 (causal structure).
**Avoids:** P3 (smooth manifold), P5 (equilibrium), P6 (continuum limit), P8 (Unruh temperature).
**Risk:** HIGH.

### Phase 4: Numerical Verification

**Rationale:** Small-scale numerics validate Phases 2-3. Benchmarks on standard models validate infrastructure; self-modeling lattice checks require Phase 1 Hamiltonian.
**Delivers:** Area-law scaling data; entanglement first law verification; entanglement equilibrium check.
**Methods:** Exact diagonalization (SciPy), QuTiP.
**Builds on:** Phase 1 (Hamiltonian).
**Risk:** LOW.

### Phase 5: Emergent Geometry and Paper Assembly

**Rationale:** CCM emergent geometry provides consistency check. Paper 6 assembles the full chain with honest framing.
**Delivers:** Emergent spatial geometry; Paper 6 "Spacetime from Self-Modeling."
**Methods:** CCM emergent geometry, MDS embedding.
**Builds on:** All prior phases.
**Avoids:** P7 (dimension not determined), P12 (classical only), P13 (factorization).
**Risk:** MEDIUM.

### Phase Ordering Rationale

- Phase 1 before Phase 2: cannot prove area law without defining the lattice
- Phase 2 before Phase 3: area-law entanglement is input to Jacobson
- Phase 4 partially parallel to Phases 2-3: benchmarks can begin immediately
- Phase 5 after Phases 1-4: paper assembly requires all results

### Phases Requiring Deep Investigation

- **Phase 2 (Area-Law Derivation):** Novel theoretical work; no existing theorem directly applies. Must construct the bridge argument.
- **Phase 3 (Jacobson Application):** No published discrete lattice version of Jacobson exists. Original work required.

Phases with established methodology:

- **Phase 1 (Locality Formalization):** Standard quantum lattice framework (Bratteli-Robinson, 40+ years).
- **Phase 4 (Numerical Verification):** Well-established exact diagonalization and entanglement entropy methods.

## Confidence Assessment

| Area | Confidence | Notes |
|------|-----------|-------|
| Prior Work | HIGH | Jacobson's thermodynamic gravity well-established (30 years). Area-law literature mature. |
| Methods | MEDIUM | Individual methods well-established; application to self-modeling is novel. Critical gap at bridge step. |
| Computational Approaches | MEDIUM-HIGH | Standard, validated techniques. Blocked until Hamiltonian defined. |
| Pitfalls | MEDIUM | Known issues well-cataloged; self-modeling-specific pitfalls inferred from structural analysis. |

**Overall confidence:** MEDIUM

### Gaps to Address

- **Self-modeling state identification:** Which state has area-law entanglement? Must resolve in Phase 2.
- **Pure state condition:** Channel capacity route requires pure global state. Does self-modeling have a pure fixed point?
- **Continuum limit:** Cannot solve this open problem; must frame correctly as leading-order IR effective description.
- **Higher-D area law:** Rigorous only in 1D and 2D frustration-free. Must prove 1D rigorously, argue physically for higher D.
- **Spectral gap:** Unknown and potentially undecidable. Recommended approach deliberately bypasses this.

### Critical Claim Verification

| # | Claim | Source | Verification | Result |
|---|-------|--------|--------------|--------|
| 1 | Jacobson 2016: delta S_EE = 0 iff Einstein eqs (conformal, 1st order) | PRIOR-WORK.md | web_search: arXiv:1505.04753, PRL 116, 201101 | CONFIRMED |
| 2 | Hastings area law: rigorous only in 1D; higher-D open | PITFALLS.md | web_search: general D>1 still open as of 2025 | CONFIRMED |
| 3 | Anshu-Arad-Gosset: 2D frustration-free area law | PRIOR-WORK.md | web_search: arXiv:2103.02492, STOC 2022 | CONFIRMED |
| 4 | WVCH: mutual info area law for thermal states | METHODS.md | web_search: PRL 100, 070502 (2008) | CONFIRMED |
| 5 | CCM: emergent geometry from mutual information | METHODS.md | web_search: PRD 95, 024031 (2017) | CONFIRMED |
| 6 | No prior GR-from-self-modeling work exists | PRIOR-WORK.md | Researcher survey; no contradicting evidence | UNVERIFIED (consistent with absence) |

## Open Questions

1. **Does self-modeling locality map onto information-theoretic locality?** [HIGH, blocks Phase 2]
2. **Is the self-modeling fixed point a pure global state?** [HIGH, blocks Route 3D]
3. **What Hamiltonian encodes self-modeling locality?** [HIGH, blocks Phase 4]
4. **Can Jacobson's entanglement equilibrium work on a finite lattice?** [MEDIUM, blocks Phase 3]
5. **How does the continuum limit emerge?** [MEDIUM, blocks rigorous Phase 3]
6. **Does the self-modeling lattice have a spectral gap?** [MEDIUM, non-blocking]
7. **Does self-modeling determine spatial dimension D?** [LOW, out of scope]

## Sources

### Primary (HIGH)

- Jacobson (1995), "Thermodynamics of Spacetime," PRL 75, 1260, [arXiv:gr-qc/9504004](https://arxiv.org/abs/gr-qc/9504004)
- Jacobson (2016), "Entanglement Equilibrium and the Einstein Equation," PRL 116, 201101, [arXiv:1505.04753](https://arxiv.org/abs/1505.04753)
- Jacobson (2012), "Gravitation and Vacuum Entanglement Entropy," [arXiv:1204.6349](https://arxiv.org/abs/1204.6349)
- Hastings (2007), "An Area Law for One Dimensional Quantum Systems," JSTAT P08024, [arXiv:0705.2024](https://arxiv.org/abs/0705.2024)
- Eisert, Cramer, Plenio (2010), "Area Laws for the Entanglement Entropy," RMP 82, 277, [arXiv:0808.3773](https://arxiv.org/abs/0808.3773)
- Wolf, Verstraete, Cirac, Hastings (2008), "Area Laws: Mutual Information and Correlations," PRL 100, 070502, [arXiv:0704.3906](https://arxiv.org/abs/0704.3906)
- Lieb, Robinson (1972), "The Finite Group Velocity of Quantum Spin Systems," Commun. Math. Phys. 28, 251
- Bratteli, Robinson (1979/1981), "Operator Algebras and Quantum Statistical Mechanics," Springer
- Bisognano, Wichmann (1975/1976), J. Math. Phys. 16, 985; 17, 303

### Secondary (MEDIUM)

- Cao, Carroll, Michalakis (2017), "Space from Hilbert Space," PRD 95, 024031, [arXiv:1606.08444](https://arxiv.org/abs/1606.08444)
- Faulkner, Lewkowycz, Maldacena (2014), JHEP 1403, 051, [arXiv:1312.7856](https://arxiv.org/abs/1312.7856)
- Lashkari, McDermott, Van Raamsdonk (2014), JHEP 1404, 195, [arXiv:1308.3716](https://arxiv.org/abs/1308.3716)
- Van Raamsdonk (2010), GRG 42, 2323, [arXiv:1005.3035](https://arxiv.org/abs/1005.3035)
- Brandao, Horodecki (2013/2015), Nature Physics 9, 721, [arXiv:1206.2947](https://arxiv.org/abs/1206.2947)
- Anshu, Arad, Gosset (2022), [arXiv:2103.02492](https://arxiv.org/abs/2103.02492)
- Swingle (2012), PRD 86, 065007, [arXiv:1209.3304](https://arxiv.org/abs/1209.3304)
- Casini, Huerta, Myers (2011), JHEP 1105, 036, [arXiv:1102.0440](https://arxiv.org/abs/1102.0440)
- Nachtergaele, Sims (2006/2019), [arXiv:1810.02428](https://arxiv.org/abs/1810.02428)
- Bravyi, Hastings, Verstraete (2006), PRL 97, 050401, [arXiv:quant-ph/0603121](https://arxiv.org/abs/quant-ph/0603121)

### Tertiary (LOW)

- Verlinde (2011), [arXiv:1001.0785](https://arxiv.org/abs/1001.0785) -- tangential
- Padmanabhan (2010), [arXiv:0911.5004](https://arxiv.org/abs/0911.5004) -- broader program
- Chirco, Liberati (2010), [arXiv:0909.4194](https://arxiv.org/abs/0909.4194) -- non-equilibrium
- Cubitt, Perez-Garcia, Wolf (2015), [arXiv:1502.04573](https://arxiv.org/abs/1502.04573) -- undecidability

---

_Research analysis completed: 2026-03-21_
_Ready for research plan: yes_

```yaml
# --- ROADMAP INPUT (machine-readable, consumed by gpd-roadmapper) ---
synthesis_meta:
  project_title: "Experiential Measure on Structure Space -- v3.0 GR Extension"
  synthesis_date: "2026-03-21"
  input_files: [METHODS.md, PRIOR-WORK.md, COMPUTATIONAL.md, PITFALLS.md]
  input_quality: {METHODS: good, PRIOR-WORK: good, COMPUTATIONAL: good, PITFALLS: good}

conventions:
  unit_system: "natural"
  metric_signature: "mostly_plus"
  fourier_convention: "physics"
  coupling_convention: "G = 1/(4*eta) where eta is entanglement entropy density"
  renormalization_scheme: "N/A"

methods_ranked:
  - name: "Channel capacity / mutual information area law (Route 3D)"
    regime: "Any D, pure global state, local information flow"
    confidence: MEDIUM
    cost: "Analytical proof; numerical check O(d^N) for N-site ED"
    complements: "WVCH mutual info bound (handles thermal states)"
  - name: "Jacobson 2016 entanglement equilibrium"
    regime: "Conformal fields, first-order perturbations, smooth manifold (continuum limit)"
    confidence: HIGH
    cost: "Analytical derivation; numerical check O(d^N) for entanglement equilibrium"
    complements: "CCM emergent geometry (spatial consistency check)"
  - name: "Quantum lattice formalization (Bratteli-Robinson)"
    regime: "Any finite-dimensional local algebra, any graph"
    confidence: HIGH
    cost: "Analytical framework setup, 3-5 days"
    complements: "Lieb-Robinson bounds (establishes causal structure)"
  - name: "Lieb-Robinson bounds"
    regime: "Finite-range interactions, bounded local dimension"
    confidence: HIGH
    cost: "Invoke known results, 1-2 days"
    complements: "Lattice formalization (provides input structure)"
  - name: "WVCH mutual information bound (Route 3A)"
    regime: "Any D, thermal states of local Hamiltonians"
    confidence: MEDIUM
    cost: "Analytical; requires identifying self-modeling thermal state"
    complements: "Channel capacity (handles pure states)"
  - name: "CCM emergent geometry"
    regime: "Finite-dim Hilbert space, area-law states"
    confidence: MEDIUM
    cost: "O(N^2 * d^N) for mutual info + O(N^3) for MDS"
    complements: "Jacobson (provides dynamics; CCM gives only spatial geometry)"
  - name: "Exact diagonalization + entanglement entropy"
    regime: "N <= 24 qubits (d^N manageable)"
    confidence: HIGH
    cost: "O(d^{2N}) per ground state; minutes on laptop for N<=20"
    complements: "DMRG (extends to N~100 in 1D)"

phase_suggestions:
  - name: "Locality Formalization"
    goal: "Define self-modeling lattice with precise locality axiom and effective causal structure"
    methods: ["Quantum lattice formalization (Bratteli-Robinson)", "Lieb-Robinson bounds"]
    depends_on: []
    needs_research: false
    risk: MEDIUM
    pitfalls: ["P2-background-dependence", "P9-locality-conflation"]
  - name: "Area-Law Derivation"
    goal: "Prove or strongly argue that local self-modeling implies area-law entanglement"
    methods: ["Channel capacity / mutual information area law (Route 3D)", "WVCH mutual information bound (Route 3A)"]
    depends_on: ["Locality Formalization"]
    needs_research: true
    risk: HIGH
    pitfalls: ["P1-which-state", "P4-spectral-gap", "P11-higher-D-conjecture"]
  - name: "Jacobson Application"
    goal: "Derive Einstein field equations from entanglement equilibrium in continuum limit"
    methods: ["Jacobson 2016 entanglement equilibrium", "CCM emergent geometry"]
    depends_on: ["Area-Law Derivation"]
    needs_research: true
    risk: HIGH
    pitfalls: ["P3-smooth-manifold", "P5-local-equilibrium", "P6-continuum-limit", "P8-unruh-temperature"]
  - name: "Numerical Verification"
    goal: "Validate area-law scaling and entanglement equilibrium on small lattices"
    methods: ["Exact diagonalization + entanglement entropy"]
    depends_on: ["Locality Formalization"]
    needs_research: false
    risk: LOW
    pitfalls: ["finite-size-effects"]
  - name: "Paper Assembly"
    goal: "Assemble Paper 6 with complete chain, precise gap identification, and honest framing"
    methods: ["CCM emergent geometry"]
    depends_on: ["Locality Formalization", "Area-Law Derivation", "Jacobson Application", "Numerical Verification"]
    needs_research: false
    risk: MEDIUM
    pitfalls: ["P7-dimension-problem", "P12-classical-only", "P13-factorization"]

critical_benchmarks:
  - quantity: "Area-law scaling for 1D gapped local Hamiltonian"
    value: "S(A) = O(1) for half-chain (constant, independent of system size)"
    source: "Hastings (2007), arXiv:0705.2024"
    confidence: HIGH
  - quantity: "Critical 1D CFT entanglement (negative control)"
    value: "S(A) = (c/6) ln(L) with c = 1/2 for transverse-field Ising at criticality"
    source: "Calabrese-Cardy (2004), arXiv:hep-th/0405152"
    confidence: HIGH
  - quantity: "Jacobson Einstein equation from entanglement equilibrium"
    value: "G_ab + Lambda g_ab = (8 pi G) T_ab for conformal fields at first order"
    source: "Jacobson (2016), PRL 116, 201101"
    confidence: HIGH
  - quantity: "Mutual information area law for thermal states"
    value: "I(A:B) <= beta * |boundary(A)| * ||h||"
    source: "Wolf-Verstraete-Cirac-Hastings (2008), PRL 100, 070502"
    confidence: HIGH

open_questions:
  - question: "Does self-modeling locality map onto information-theoretic channel capacity locality?"
    priority: HIGH
    blocks_phase: "Area-Law Derivation"
  - question: "Is the self-modeling fixed point a pure global state?"
    priority: HIGH
    blocks_phase: "Area-Law Derivation"
  - question: "What Hamiltonian encodes self-modeling locality?"
    priority: HIGH
    blocks_phase: "Numerical Verification"
  - question: "Can Jacobson's entanglement equilibrium be formulated on a finite lattice?"
    priority: MEDIUM
    blocks_phase: "Jacobson Application"
  - question: "How does the continuum limit emerge from the self-modeling lattice?"
    priority: MEDIUM
    blocks_phase: "Jacobson Application"
  - question: "Does the self-modeling lattice have a spectral gap?"
    priority: MEDIUM
    blocks_phase: "none"
  - question: "Does self-modeling determine the spatial dimension D?"
    priority: LOW
    blocks_phase: "none"

contradictions_unresolved:
  - claim_a: "Hastings area law provides the route to S(A) ~ |boundary(A)| (requires spectral gap)"
    claim_b: "Channel capacity argument provides the route (requires pure global state, no gap needed)"
    source_a: "METHODS.md Route 3B, PITFALLS.md P4"
    source_b: "METHODS.md Route 3D"
    investigation_needed: "Determine whether the self-modeling fixed point is a gapped ground state (favoring Hastings) or a pure state accessible via channel capacity (favoring Route 3D). Both routes are viable; the choice depends on properties of the self-modeling dynamics that are currently unknown."
```
