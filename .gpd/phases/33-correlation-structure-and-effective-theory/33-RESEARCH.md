# Phase 33: Correlation Structure and Effective Theory - Research

**Researched:** 2026-03-29
**Domain:** Quantum magnetism / Nonlinear sigma model / Information geometry on quantum lattice states
**Confidence:** MEDIUM

## Summary

Phase 33 must deliver three results: (CORR-01) rigorous characterization of correlation decay in the SWAP/Heisenberg ground state for d>=2, distinguishing gapped (exponential) from gapless Neel (algebraic) regimes; (CORR-02) derivation of the O(3) nonlinear sigma model as the low-energy effective theory for the d>=2 Neel phase with an explicit spin-wave velocity c_s determined by lattice parameters; and (CORR-03) proof or conditional argument that Fisher geometry remains smooth in the sigma model regime where correlations are algebraic rather than exponential.

The mathematical situation is well-understood at the textbook level but contains one genuine gap: there is no rigorous theorem establishing Fisher metric smoothness for gapless systems with algebraic correlations. For the gapped regime, Hastings-Koma gives everything needed (already validated in Phase 32). For the gapless Neel regime, the argument must chain through: (i) Dyson-Lieb-Simon / Kennedy-Lieb-Shastry prove Neel order exists; (ii) Goldstone theorem gives gapless magnons with linear dispersion omega ~ c_s |k|; (iii) the NL sigma model provides the effective theory with explicit parameters; (iv) within the NL sigma model, transverse correlations decay as 1/r^{d-1} while longitudinal correlations approach the order parameter value. The Fisher metric on reduced states in this regime is controlled by these power-law tails plus the non-vanishing staggered magnetization that breaks translation invariance on the sublattice scale.

**Primary recommendation:** Use the two-tier strategy: rigorous Hastings-Koma for gapped systems (AKLT, easy-axis), and NL sigma model effective theory for the n=2 d>=2 Neel phase. The SWAP Hamiltonian is equivalent to Heisenberg up to a constant, so the entire standard Heisenberg literature applies directly. For CORR-03, the key insight is that Neel long-range order provides a non-vanishing sublattice magnetization m_s > 0, which gives rho_Lambda(x) genuine x-dependence (sublattice alternation) that survives the thermodynamic limit -- unlike the 1D case where FISH-03 failed because g_bulk -> 0.

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| --- | --- | --- | --- | --- |
| ref-hastings2004 (Hastings-Koma, CMP 265, 2006) | Backbone theorem | Gap => exponential clustering; handles gapped tier completely | Cite for gapped regime; state inapplicability for gapless Neel | Plan, execution, verification |
| Dyson-Lieb-Simon 1978 (JSP 18, 335) | Rigorous result | Proves Neel order for S>=1 d>=3; extended by KLS to S=1/2 d=3 | Cite for Neel order existence; note limitations for S=1/2 d=2 | Plan, execution |
| Kennedy-Lieb-Shastry 1988 (JSP 53, 1019) | Extension of DLS | Extends to S=1/2 d=3; provides inequalities used with QMC for d=2 | Cite for S=1/2 results; QMC completion for d=2 | Plan, execution |
| Nachtergaele-Sims 2006 (CMP 265, 119) | LR bounds | Provides v_LR bound; underlies clustering theorems | Cite for v_LR; c_s <= v_LR consistency check | Plan, execution |
| Haldane 1983 (PLA 93, 464; PRL 50, 1153) | NL sigma model origin | Maps Heisenberg AFM to O(3) NL sigma model via coherent states | Foundation for CORR-02 derivation | Plan, execution |
| Chakravarty-Halperin-Nelson 1989 (PRB 39, 2344) | NL sigma model analysis | Low-T analysis of 2D quantum Heisenberg via NL sigma model | Provides framework for spin-wave velocity, stiffness | Plan, execution |
| ref-paper6 (SWAP lattice, ED data) | Prior artifact | SWAP lattice definition; H_SWAP = H_Heis + const | Verify equivalence carries through to effective theory | Plan, execution |
| Phase 32 results (FISH-01/02/03) | Prior artifact | FISH-01/02 proved; FISH-03 fails in 1D; motivates d>=2 | Build CORR-03 argument on FISH-01/02; explain why d>=2 rescues FISH-03 | Plan, execution, verification |
| Sandvik 2025 (arXiv:2601.20189) | Benchmark | High-precision QMC values: m_s=0.307447, rho_s=0.180752, c=1.65880 | Use as numerical benchmarks for NL sigma model parameters | Plan, execution, verification |

**Missing or weak anchors:** The Fisher metric smoothness for algebraic correlations (CORR-03) has no single anchoring reference. This is novel territory -- the argument must be constructed from the NL sigma model structure plus standard analysis of power-law decay integrands. Confidence for CORR-03 is LOW-MEDIUM.

## Conventions

| Choice | Convention | Alternatives | Source |
| --- | --- | --- | --- |
| Metric signature | (-,+,+,...,+) for Lorentzian; (+,+,...,+) for Riemannian Fisher | (+,-,-,-) | Project convention (SUMMARY.md) |
| Units | Natural (hbar=1, k_B=1), lattice spacing a=1 unless taking continuum limit | SI, Gaussian | Project convention |
| Fisher metric | SLD, g_F = 4*g_Bures | Wigner-Yanase, Kubo-Mori | Phase 32 convention |
| Coupling | J > 0 antiferromagnetic | J < 0 ferromagnetic | Project convention |
| SWAP-Heisenberg relation | H_SWAP = J*sum P_{ij} = J*sum (2 S_i.S_j + (1/2)I) | P_{ij} = (1+sigma_i.sigma_j)/2 | Paper 6 |
| Staggered magnetization | m_s = (1/N) sum (-1)^i <S_i^z> (sublattice-alternating) | Various normalizations | Manousakis 1991 convention |
| NL sigma model field | n(x,tau): unit vector field on S^2, n^2 = 1 | CP^1 representation z | Haldane 1983 |
| Spin-wave velocity units | c_s in units of Ja (energy * lattice spacing) | c_s/J dimensionless (assumes a=1) | Standard condensed matter |

**CRITICAL: All equations and results below use these conventions. The SWAP Hamiltonian ground state is identical to the Heisenberg ground state; only the energy eigenvalue differs by N_bonds * J/2. The NL sigma model literature uses both n-field and CP^1 representations; we use the n-field (O(3)) representation following Haldane.**

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in This Phase |
| --- | --- | --- | --- |
| H = J sum S_i . S_j (J>0, nn) | Heisenberg AFM Hamiltonian | Standard | Starting Hamiltonian (equivalent to SWAP up to constant) |
| P_{ij} = 2 S_i . S_j + (1/2) I | SWAP-Heisenberg identity (spin-1/2) | Paper 6 | Confirms SWAP = Heisenberg + const for all CORR derivations |
| <S_i^a S_j^b>_c ~ (-1)^{i-j} m_s^2 delta_{ab}/3 + C_{ab}(r)/r^{d-1+eta} | Two-point correlation in Neel phase | Spin wave theory | CORR-01 target: decompose into LRO + power-law transverse |
| S_eff = (1/2g) int d^d x d tau [(d_tau n)^2/c_s^2 + (nabla n)^2] | O(3) NL sigma model action | Haldane 1983; CHN 1989 | CORR-02 target: derive this from lattice with explicit g, c_s |
| g = d*c_s / (2*rho_s) (d=2) or equivalently c_s = 2*rho_s / (d*chi_perp)^{1/2} | Coupling-stiffness-velocity relation | CHN 1989 | Maps lattice parameters to sigma model coupling |
| c_s = sqrt(rho_s / chi_perp) | Spin-wave velocity from stiffness and susceptibility | Standard spin wave theory | CORR-02 deliverable: explicit c_s formula |
| g_F(x) = sum_{m,n} 2|<m|d_x rho|n>|^2 / (p_m + p_n) | SLD Fisher metric (from Phase 32) | Phase 32, Eq. (32.4) | CORR-03: evaluate in NL sigma model regime |
| ||rho(x+1) - rho(x)||_1 <= C * exp(-R(x)/xi) | Smoothness from Hastings-Koma (gapped) | Phase 32, Eq. (32.8) | CORR-03 gapped tier |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --- | --- | --- | --- |
| Holstein-Primakoff transformation | Maps spin operators to bosonic operators (magnons) | NL sigma model derivation step 1 | Auerbach Ch. 11 |
| Coherent state path integral | Converts spin partition function to continuum action | NL sigma model derivation step 2 | Auerbach Ch. 12; Haldane 1983 |
| Sublattice decomposition | Separates lattice into A/B sublattices for staggered order | Neel order analysis; correlation decomposition | Standard for bipartite lattices |
| Linear spin-wave theory | Quadratic magnon Hamiltonian; dispersion omega_k = c_s |k| | Spin-wave velocity extraction; correlation exponents | Auerbach Ch. 11; Anderson 1952 |
| Reflection positivity / infrared bounds | Prove long-range order via Fourier-space bounds | Neel order proof (DLS method) | DLS 1978; Nachtergaele review |
| Partial trace + sublattice alternation analysis | Compute rho_Lambda(x) in Neel phase; detect sublattice structure | CORR-03 Fisher metric argument | Extension of Phase 32 methods |

### Approximation Schemes

| Approximation | Small Parameter | Regime of Validity | Error Estimate | Alternatives if Invalid |
| --- | --- | --- | --- | --- |
| Linear spin-wave theory (LSWT) | 1/S (quantum fluctuations) | S >= 1 or large coordination z; moderate for S=1/2 | O(1/S^2); LSWT overestimates m_s by ~8% for S=1/2 | 1/S expansion to next order; QMC |
| NL sigma model (continuum limit) | a/xi_corr (lattice spacing / correlation length) | Long wavelengths k << pi/a | O((ka)^2) lattice corrections | Stay on lattice; use ED/QMC |
| Hastings-Koma exponential clustering | exp(-r/xi) with xi = v_LR/gamma | Gapped systems only (gamma > 0) | Tight for gapped phases | Inapplicable for gapless; use sigma model |
| Neel mean field + fluctuations | 1/z (inverse coordination number) | z >= 4 (square lattice z=4 is borderline) | O(1/z^2) corrections significant for z=4 | Full QMC; series expansions |

## Standard Approaches

### Approach 1: Two-Tier Correlation Characterization (RECOMMENDED for CORR-01)

**What:** Separately characterize correlation decay for (a) gapped systems via Hastings-Koma, and (b) gapless Neel phase via spin-wave theory + NL sigma model.

**Why standard:** This is exactly how the condensed matter community handles these systems. No single method covers both regimes. The gapped case is rigorous; the gapless case requires the standard (but not fully rigorous) spin-wave / sigma model machinery.

**Track record:** Used in every textbook treatment (Auerbach, Sachdev, Fradkin). The spin-wave theory predictions match QMC to within a few percent.

**Key steps:**

1. **Gapped tier (AKLT, easy-axis, n>=3 candidates):**
   - State Hastings-Koma theorem with hypotheses
   - Verify spectral gap exists (cite AKLT gap proof, or easy-axis gap from anisotropy)
   - Conclude: |<S_i.S_j>_connected| <= C exp(-|i-j|/xi), xi = O(v_LR/gamma)
   - Fisher metric smoothness follows from Phase 32 FISH-01 argument

2. **Gapless Neel tier (n=2, d>=2):**
   - Establish Neel order: cite DLS 1978 for S>=1 d>=3, KLS 1988 for S=1/2 d=3, QMC evidence for S=1/2 d=2 (Reger-Young 1988, Sandvik 2025: m_s = 0.3074)
   - Identify Goldstone modes: SU(2) -> U(1) breaking gives 2 gapless magnon branches
   - Compute correlation decomposition:
     * Longitudinal: <S_i^z S_j^z> -> m_s^2 (-1)^{i-j} + O(1/r^{d+1}) (approaches LRO value)
     * Transverse: <S_i^+ S_j^-> ~ 1/r^{d-1} (Goldstone mode contribution)
     * Connected: <S_i.S_j>_c ~ 1/r^{d-1} from magnon propagator
   - For d=2: transverse correlations decay as 1/r (marginal), connected correlations decay as 1/r

3. **State the result precisely:** For n=2 d>=2, the correlation structure is NOT purely exponential NOR purely algebraic. It is: LRO (non-decaying staggered component) + algebraic correction (from Goldstone modes).

**Known difficulties at each step:**
- Step 2: DLS does NOT prove Neel order for S=1/2 d=2 rigorously. The proof requires S>=1 in d>=2, or S=1/2 in d>=3. For S=1/2 d=2, we rely on QMC evidence (which is overwhelming but not a mathematical proof). State this honestly.
- Step 2: The exponent d-1 for transverse correlations is the leading spin-wave result. Higher-order corrections are O(1/S) and modify the exponent by logarithmic factors in d=2 (anomalous dimension eta ~ 0 for Heisenberg, but log corrections present).

### Approach 2: NL Sigma Model Derivation (RECOMMENDED for CORR-02)

**What:** Derive the O(3) NL sigma model as the effective low-energy theory for the Neel-ordered phase of the Heisenberg AFM on a d-dimensional bipartite lattice.

**Why standard:** This is THE textbook derivation (Haldane 1983, Auerbach Ch. 12-13, Sachdev Ch. 13). The mapping is well-established and verified numerically to high precision.

**Key steps:**

1. **Sublattice decomposition:** Write S_i = S * n_i where n_i is a unit vector. On sublattice A, n_i ~ +n(x); on sublattice B, n_i ~ -n(x) (staggered field).
2. **Introduce smooth fields:** Define staggered (n) and uniform (l) fields: S_i = S[(-1)^i n(x_i) + l(x_i)/S] with constraints n^2 = 1, n.l = 0.
3. **Coherent state path integral:** Convert the lattice partition function to a path integral over (n, l).
4. **Integrate out l (uniform fluctuations):** This is Gaussian; produces kinetic term for n.
5. **Resulting action:** S_eff = (1/(2g)) int d^d x dtau [(d_tau n)^2/c_s^2 + (nabla n)^2] + i*theta*Q[n] (in d=1)
   - Coupling constant: g = d*c_s/(2*rho_s) in d spatial dimensions
   - Spin-wave velocity: c_s = 2*sqrt(d)*J*S*a for classical (large-S) limit
   - For S=1/2 d=2 (square lattice): quantum-renormalized c_s = 1.65880(6) Ja (Sandvik 2025)
   - Topological term: theta = 2*pi*S per unit cell. For integer S, theta = 0 mod 2pi (Haldane gap in d=1). For half-integer S, theta = pi (gapless in d=1). In d>=2, the topological term is absent (no pi_2 for O(3) in d>=2+1).

6. **Verify c_s from lattice parameters:** The spin-wave velocity satisfies c_s = sqrt(rho_s / chi_perp) where:
   - rho_s = spin stiffness (response to boundary twist)
   - chi_perp = transverse uniform susceptibility
   - QMC values (Sandvik 2025): rho_s = 0.180752(6) J, chi_perp = 0.065690(5) /J, c_s = sqrt(0.180752/0.065690) = 1.6588 Ja. Confirmed.

7. **Dimensional analysis check:** [S_eff] = dimensionless. [g] = dimensionless (d=2). [c_s] = [length/time] = Ja/hbar. [rho_s] = [energy] = J. Consistent.

**Known difficulties:**
- Step 2: The smooth field approximation breaks down at lattice scale. The derivation is valid only for k << pi/a.
- Step 5: In d=2+1, g is dimensionless and the sigma model is classically scale-invariant. The ordered (Neel) phase corresponds to g < g_c (weak coupling).
- Step 5: For S=1/2, the "large-S" derivation is formally uncontrolled (S is not large). However, QMC confirms the NL sigma model description works quantitatively.

### Approach 3: Fisher Smoothness in Algebraic Decay Regime (RECOMMENDED for CORR-03)

**What:** Argue that the Fisher metric g_F(x) on reduced states remains smooth (FISH-01-like) and non-vanishing in the bulk (unlike 1D) when correlations are algebraic with Neel LRO.

**Why this is the hard part:** Phase 32 proved FISH-01 (smoothness) for gapped systems via Hastings-Koma. For gapless systems, Hastings-Koma does not apply. The question is whether algebraic decay 1/r^alpha with alpha > 0 gives a well-defined, smooth Fisher metric.

**Key argument (CORR-03):**

The Fisher metric g_F(x) involves d_x rho_Lambda. In the Neel-ordered phase:

1. **rho_Lambda(x) has genuine x-dependence from sublattice alternation.** Unlike the 1D gapless case where translation symmetry is restored in the thermodynamic limit (causing g_bulk -> 0), in d>=2 with Neel order, rho_Lambda centered on an A-sublattice site differs from rho_Lambda centered on a B-sublattice site by an amount proportional to m_s > 0. This sublattice alternation persists in the thermodynamic limit.

2. **d_x rho is bounded and non-vanishing.** The shift x -> x+1 takes an A-site-centered subsystem to a B-site-centered one. The trace-norm difference ||rho(x+1) - rho(x)||_1 is proportional to m_s^2 in the Neel phase. This is O(1), not O(1/N).

3. **Smoothness of the slowly-varying part.** Beyond the sublattice alternation, rho_Lambda(x) varies smoothly on the scale of the correlation length. The corrections to the staggered pattern decay as power laws (1/r^{d-1} from Goldstone modes). For d >= 2, the integral sum_{r > R} 1/r^{d-1} * r^{d-1} d_r converges logarithmically for d=2 and absolutely for d>2, giving bounded corrections to rho.

4. **Formal argument:** Write rho_Lambda(x) = rho_A^{Neel}(x) + delta_rho(x) where rho_A^{Neel} encodes the staggered mean-field state and delta_rho captures Goldstone fluctuations. The Fisher metric decomposes as:
   - g_F^{Neel}(x): contribution from the Neel order -- O(m_s^2), non-vanishing, well-defined
   - g_F^{Goldstone}(x): contribution from the transverse fluctuations -- bounded if the integral int d^d r / r^{2(d-1)} converges
   - Cross terms: bounded
   - For d=2: the Goldstone integral int d^2 r / r^{2} = int dr/r is logarithmically divergent. This suggests the Fisher metric may have logarithmic corrections but remains finite at any finite lattice size. In the thermodynamic limit, this gives log(L) corrections where L is the system size.
   - For d>=3: the integral converges absolutely. Fisher metric is well-defined.

5. **Conditional conclusion:** For d=2, the Fisher metric is smooth at finite L with possible log(L) corrections. For d>=3, the Fisher metric is smooth in the thermodynamic limit. Both cases give a non-vanishing bulk metric (unlike 1D), rescuing FISH-03.

**This argument is NOT rigorous.** It is a controlled physical argument at the level of the NL sigma model. The conditions under which it holds should be stated explicitly.

### Anti-Patterns to Avoid

- **Claiming exponential decay for gapless Neel phase:** Explicitly forbidden by the contract. Hastings-Koma requires a gap. The Neel phase is gapless.
- **Using a generic sigma model without SWAP-specific c_s:** The contract requires c_s determined by the lattice Hamiltonian parameters. Must give the explicit formula and numerical value.
- **Assuming spectral gap without proof for n=2 d>=2:** The Heisenberg AFM on the square lattice is NOT gapped. Do not cite Hastings-Koma for this regime.
- **Treating 1D and d>=2 as the same:** The 1D case is fundamentally different (no LRO, Mermin-Wagner). The d>=2 case has LRO which qualitatively changes the Fisher geometry.
- **Ignoring the sublattice structure:** The Neel order means rho_Lambda alternates between A and B sublattice character. The Fisher metric must account for this alternation.
- **Claiming Fisher smoothness without argument:** For algebraic correlations, smoothness requires explicit justification, not just citing Hastings-Koma (which does not apply).

## Existing Results to Leverage

**This section is MANDATORY.** The following results should be CITED and USED, not re-derived.

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form / Value | Source | How to Use |
| --- | --- | --- | --- |
| SWAP = Heisenberg + constant | P_{ij} = 2 S_i.S_j + (1/2)I for spin-1/2 | Paper 6; standard identity | Ground state is identical; all Heisenberg results apply directly |
| Neel order existence (S>=1, d>=3) | <(-1)^i S_i^z> != 0 in thermodynamic limit | DLS 1978, JSP 18, 335 | Cite for gapped tier; state regime of validity |
| Neel order existence (S=1/2, d=2) | m_s = 0.307447(2) | KLS 1988 (inequalities) + QMC (Reger-Young 1988; Sandvik arXiv:2601.20189) | Use QMC value as benchmark; note not fully rigorous |
| Heisenberg AFM ground state energy (S=1/2, d=2) | e_0 = -0.669441857(7) J per bond | Sandvik arXiv:2601.20189 | Benchmark for any numerical checks |
| Spin-wave velocity (S=1/2, d=2) | c_s = 1.65880(6) Ja | Sandvik arXiv:2601.20189; c_s = sqrt(rho_s/chi_perp) | CORR-02 deliverable: explicit c_s for SWAP lattice |
| Spin stiffness (S=1/2, d=2) | rho_s = 0.180752(6) J | Sandvik arXiv:2601.20189 | NL sigma model coupling; validate against spin-wave theory |
| Transverse susceptibility (S=1/2, d=2) | chi_perp = 0.065690(5) /J | Sandvik arXiv:2601.20189 | c_s = sqrt(rho_s/chi_perp) verification |
| Hastings-Koma theorem | Gap gamma => xi = O(v_LR/gamma); exponential clustering | CMP 265, 781 (2006) | Gapped tier ONLY; do NOT apply to Neel phase |
| FISH-01 (smoothness, Phase 32) | ||rho(x+1)-rho(x)||_1 <= C exp(-R(x)/xi) for gapped systems | Phase 32, Eq. (32.8) | Gapped tier of CORR-03 |
| FISH-02 (positive-definiteness, Phase 32) | g(x) > 0 at interior full-rank points | Phase 32, Theorem 2 | Carries forward to both tiers |
| FISH-03 failure in 1D | g_bulk ~ N^{-2.75} -> 0 as N -> inf for 1D Heisenberg | Phase 32, Eq. (32.12) | Motivates d>=2; explains why Neel order is needed |
| AKLT gap (spin-1 chain) | gamma > 0 (proven rigorously) | AKLT, CMP 115 (1988) | Example for gapped tier |
| Z_c renormalization factor | Z_c = 1.1765 +/- 0.0002 for S=1/2 square lattice | Canali-Girvin-Wallin, PRB 45, 10131 (1992) | Quantum correction to classical c_s |
| Classical spin-wave velocity | c_s^{classical} = 2*sqrt(d)*J*S*a = sqrt(2)*J*a for S=1/2, d=2 | Linear spin-wave theory | Starting point for quantum-corrected c_s |
| Spin-wave velocity renormalization | c_s^{quantum} = Z_c * c_s^{classical} = 1.1765 * sqrt(2) * J * a = 1.664 Ja | LSWT + 1/S correction | Cross-check: 1.664 vs QMC 1.659 (0.3% agreement) |

**Key insight:** The SWAP Hamiltonian equivalence means we can use the entire 50+ year literature on the Heisenberg antiferromagnet without any new derivation. The only "new" step is connecting NL sigma model parameters to the Fisher metric.

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| --- | --- | --- | --- | --- |
| Phase transitions in quantum spin systems | Dyson, Lieb, Simon | 1978 | Neel order proof | Reflection positivity method; infrared bounds; conditions (S, d) |
| Neel order in S=1/2 AFMs | Kennedy, Lieb, Shastry | 1988 | Extension to S=1/2 | Inequalities; combined with QMC for d=2 |
| Continuum dynamics of 1D Heisenberg AFM | Haldane | 1983 | NL sigma model origin | O(3) sigma model mapping; theta term; coupling constant |
| 2D quantum Heisenberg AFM at low T | Chakravarty, Halperin, Nelson | 1989 | NL sigma model analysis in d=2 | Renormalization; T-dependence; universality class |
| S=1/2 Heisenberg on square lattice (review) | Manousakis | 1991 | Comprehensive review | Spin-wave theory parameters; NL sigma model; comparison methods |
| High-precision ground state parameters | Sandvik | 2025 | State-of-the-art QMC values | m_s, rho_s, chi_perp, c_s to 5-6 significant figures |
| Spectral gap and exponential decay | Hastings, Koma | 2006 | Gapped regime | Exponential clustering theorem; xi = v_LR/gamma |
| Quantum NL sigma model for arbitrary spin | Berera, Horgan, et al. | 2005 | General derivation | arXiv:cond-mat/0509628; spin-S sigma model parameters |

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
| --- | --- | --- | --- |
| NumPy/SciPy | >=1.20/>=1.10 | ED infrastructure, eigensolvers | Already in project; Lanczos eigsh |
| code/ed_entanglement.py | Phase 11 | Hamiltonian construction, partial trace, ground state | Already includes construct_heisenberg_1d, construct_heisenberg_2d (PBC) |
| code/fisher_metric.py | Phase 32 | Fisher metric computation, reduced state sweeps | Already has SLD formula, Bures cross-validation |

### Supporting Tools

| Tool | Purpose | When to Use |
| --- | --- | --- |
| SymPy | Symbolic algebra for NL sigma model derivation steps | Verify coupling constant relations |
| matplotlib | Visualization of correlation decay, Fisher metric profiles | Plotting correlation functions vs distance |
| scipy.optimize.curve_fit | Power-law fitting of correlation decay | CORR-01: fit C(r) ~ A/r^alpha to extract alpha |

### Computational Feasibility

| Computation | Estimated Cost | Bottleneck | Mitigation |
| --- | --- | --- | --- |
| 2D Heisenberg ED (4x4 = 16 sites, S^z=0 sector) | ~30 sec, ~1 GB RAM | Hilbert space dim ~12870 | Use symmetry sector; already feasible |
| 2D Heisenberg ED (4x6 = 24 sites) | ~hours, ~50 GB RAM | Hilbert space dim ~2.7M | May be infeasible; use 4x4 with finite-size scaling |
| Correlation function extraction (4x4) | ~1 sec after ground state | Trivial after ED | Already in infrastructure |
| Fisher metric on 2D lattice (4x4 OBC) | ~minutes | Need 2D reduced state sweep | Extend fisher_metric.py to 2D |
| NL sigma model derivation | Analytical (symbolic) | Algebra, not computation | Pencil-and-paper + SymPy verification |

**Installation / Setup:**
```bash
# No additional packages needed beyond what Phase 32 already uses.
# All computations use NumPy, SciPy, existing ED infrastructure.
```

### 2D Lattice Extension Needed

The existing `construct_heisenberg_2d` in ed_entanglement.py constructs the 2D Hamiltonian with PBC. For CORR-03, need OBC version. The `fisher_metric.py` `reduced_states_sweep` currently works for 1D. Must extend to 2D: the subsystem Lambda is now a plaquette (e.g., 2x2 block), and the position parameter x = (x1, x2) is 2D.

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| --- | --- | --- | --- |
| c_s = sqrt(rho_s/chi_perp) | NL sigma model relation | Compute rho_s and chi_perp independently from ED; check ratio | Should agree with c_s from dispersion |
| Z_c * c_s^{classical} = c_s^{QMC} | Spin-wave renormalization | 1.1765 * sqrt(2) * J * a = 1.664 Ja vs 1.659 Ja | 0.3% agreement |
| m_s(L) -> m_s(inf) extrapolation | Neel order persistence | Finite-size scaling of staggered magnetization from ED | Should approach 0.307 for large L (4x4 will be crude) |
| Correlation decay exponent | CORR-01 characterization | Fit <S_i.S_j>_connected vs |i-j| to power law | Exponent alpha ~ d-1 = 1 for d=2 |
| Fisher metric g_F > 0 in 2D bulk | CORR-03 non-vanishing | Compute g_F on 2D OBC lattice; check interior | g_F should be O(m_s^2), not O(1/N) |
| Sublattice alternation in rho | Neel order signature | Compare rho_Lambda at A-site vs B-site center | Trace distance ~ m_s |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| --- | --- | --- | --- |
| S -> infinity (classical) | Large spin | c_s = 2*sqrt(d)*JSa; m_s = S | Linear spin-wave theory |
| d -> infinity | Large coordination | Mean-field exact | Sublattice magnetization = S |
| T -> 0, d=2 | Zero temperature | Neel order; c_s finite | QMC; spin-wave theory |
| gamma -> 0 (gapless) | Neel phase | Hastings-Koma NOT applicable | Explicit statement needed |
| gamma > 0 (gapped) | AKLT, easy-axis | Exponential clustering | Hastings-Koma |
| 1D limit | d=1 | No Neel order (Mermin-Wagner); g_bulk -> 0 | Phase 32 FISH-03 |

### Red Flags During Computation

- If the 2D staggered magnetization on 4x4 lattice is zero or negative, there is likely a symmetry sector issue (ground state may be in singlet sector with zero net magnetization -- must compute <S_i.S_j>(-1)^{i-j} as a correlation, not expectation value)
- If the Fisher metric in 2D is O(1/N) like 1D, the Neel order argument is failing -- check that OBC is correctly breaking translation invariance
- If c_s from dispersion disagrees with sqrt(rho_s/chi_perp) by more than 5%, there is a convention or normalization error
- If correlation decay appears exponential rather than algebraic in d=2, the system may be too small for the power-law regime to be visible (correlation length exceeds system size)

## Common Pitfalls

### Pitfall 1: Confusing Neel Order with Exponential Decay

**What goes wrong:** Assuming that because Neel order is "well-behaved," correlations must decay exponentially. In fact, Neel order produces ALGEBRAIC decay of transverse correlations due to Goldstone modes.
**Why it happens:** Conflation of "ordered phase" with "gapped phase." Ordered phases with continuous symmetry breaking are gapless (Goldstone theorem).
**How to avoid:** Always distinguish longitudinal (approaches m_s^2) from transverse (power-law 1/r^{d-1}) correlations. State which correlator you are discussing.
**Warning signs:** Writing "<S_i.S_j> ~ exp(-|i-j|/xi)" for the Neel phase.
**Recovery:** Replace with the correct decomposition: staggered LRO + algebraic transverse corrections.

### Pitfall 2: Applying Hastings-Koma to Gapless Systems

**What goes wrong:** Citing Hastings-Koma for the Heisenberg AFM in d>=2 without noting it requires a spectral gap.
**Why it happens:** Hastings-Koma is the "go-to" clustering theorem, and it is tempting to apply it universally.
**How to avoid:** Always check: does the system have a gap? For Neel phase: NO. For AKLT: YES. State the gap condition explicitly.
**Warning signs:** "By Hastings-Koma, correlations in the Neel phase decay exponentially."
**Recovery:** Use the two-tier approach. Hastings-Koma for gapped tier only; sigma model for Neel tier.

### Pitfall 3: Wrong Spin-Wave Velocity Formula

**What goes wrong:** Using c_s = 2*sqrt(2)*J*S*a (classical value for S=1/2 d=2) without the quantum renormalization factor Z_c.
**Why it happens:** The classical formula appears in many derivations as the "result" without noting it needs correction.
**How to avoid:** Always quote the quantum-renormalized value: c_s = Z_c * c_s^{classical} = 1.1765 * sqrt(2) * J * a = 1.659 Ja. Or better, cite the QMC value c_s = 1.65880(6) Ja directly.
**Warning signs:** Getting c_s = sqrt(2) * J * a = 1.414 Ja (missing Z_c).
**Recovery:** Multiply by Z_c = 1.1765, or use c_s = sqrt(rho_s/chi_perp) with QMC values.

### Pitfall 4: Finite-Size Effects Masking Neel Order in ED

**What goes wrong:** On a finite lattice with SU(2) symmetry, the ground state is a singlet (total S=0) and has zero staggered magnetization.
**Why it happens:** Spontaneous symmetry breaking requires the thermodynamic limit. Finite systems have symmetric ground states.
**How to avoid:** Compute the staggered structure factor S(pi,pi) = (1/N^2) sum_{i,j} (-1)^{i-j} <S_i.S_j>. If this remains O(1) as N grows, Neel order exists. Alternatively, apply a small staggered field to break symmetry.
**Warning signs:** <S_i^z> = 0 on all sites; concluding "no Neel order."
**Recovery:** Use the staggered structure factor, not the local magnetization.

### Pitfall 5: Assuming Fisher Smoothness Without Argument

**What goes wrong:** Assuming CORR-03 follows trivially from FISH-01 (Phase 32). But FISH-01 was proved using Hastings-Koma (gapped), which does not apply here.
**Why it happens:** Temptation to shortcut the hard part (algebraic decay Fisher analysis).
**How to avoid:** Construct an explicit argument for the algebraic decay regime. The argument in Approach 3 above is the recommended path.
**Warning signs:** "By FISH-01, the Fisher metric is smooth in the Neel phase."
**Recovery:** State FISH-01 applies only to gapped systems. Provide the separate argument for the Neel phase based on sublattice alternation + bounded Goldstone corrections.

## Level of Rigor

**Required for this phase:** Controlled approximation for CORR-01/02, conditional argument for CORR-03.

**Justification:** CORR-01 (correlation characterization) can be stated rigorously for the gapped tier (Hastings-Koma is a theorem) and at the level of controlled spin-wave theory for the Neel tier. CORR-02 (NL sigma model) is inherently a physicist's derivation (coherent-state path integral mapping) validated by numerical agreement. CORR-03 (Fisher smoothness for algebraic decay) requires a novel argument that cannot be fully rigorous because no existing theorem covers it -- a conditional argument with explicit assumptions is the honest approach.

**What this means concretely:**
- Gapped tier: rigorous theorem statements with cited proofs
- Neel tier: spin-wave theory results with QMC verification to validate approximations
- NL sigma model: physicist's derivation with all steps explicit, verified against QMC benchmarks
- Fisher smoothness (CORR-03): conditional statement -- "IF the Neel order persists and correlations decay as 1/r^{d-1}, THEN the Fisher metric is smooth with the following bound..."
- Numerical evidence from 4x4 2D lattice ED to support (but not prove) the analytical arguments

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| --- | --- | --- | --- |
| Neel order only for S>=1 (DLS 1978) | S=1/2 d=2 established by QMC + KLS inequalities | 1988-1991 | Opens S=1/2 square lattice to sigma model treatment |
| Classical spin-wave velocity | Quantum-renormalized c_s with Z_c correction | 1992 (Canali et al.) | 17% correction to classical value |
| Low-precision QMC (3-4 digits) | 6-digit precision (Sandvik 2025) | 2025 | Definitive benchmark for all sigma model parameters |
| Separate treatments of gap/gapless | Two-tier strategy for Fisher geometry | This project | Connects Hastings-Koma and sigma model to information geometry |

**Superseded approaches to avoid:**
- Anderson spin-wave theory without quantum corrections: gives c_s = sqrt(2) Ja instead of 1.659 Ja. Off by 17%.
- Mean-field Neel state: misses all Goldstone physics. Do not use for correlation structure.
- Schwinger boson mean-field: useful for qualitative phase diagrams but less precise than QMC for quantitative parameters.

## Open Questions

1. **Fisher metric smoothness for d=2 algebraic correlations**
   - What we know: FISH-01 works for gapped; Neel order gives non-vanishing sublattice alternation; Goldstone corrections are 1/r.
   - What's unclear: Whether the 1/r decay in d=2 gives log(L) divergences in the Fisher metric components, or whether they cancel in the full expression.
   - Impact on this phase: If log(L) divergences appear, CORR-03 must state the result as conditional (Fisher metric diverges logarithmically with system size but is smooth at any finite L).
   - Recommendation: Proceed with the conditional argument. Check numerically on 4x4 lattice. If log(L) divergences appear, document them and note they are milder than the 1D power-law failure.

2. **S=1/2 d=2 Neel order: rigorous or QMC-based?**
   - What we know: DLS proves Neel order for S>=1 d>=3 and some S=1/2 cases. QMC gives m_s = 0.3074 for S=1/2 d=2.
   - What's unclear: No rigorous proof of Neel order for S=1/2 on the square lattice (d=2) exists.
   - Impact on this phase: The entire CORR-01/02/03 chain for n=2, d=2 rests on Neel order. If we cannot prove it rigorously, the results are conditional.
   - Recommendation: State the QMC evidence (overwhelmingly strong, 0.3074 is not controversial) and note the gap in the rigorous proof. This is standard practice in condensed matter physics.

3. **Does 2D OBC lattice give g_bulk > 0 for S=1/2 Heisenberg?**
   - What we know: In 1D, g_bulk -> 0 as N^{-2.75}. In d>=2 with Neel order, we argue g_bulk ~ O(m_s^2) > 0.
   - What's unclear: No numerical confirmation yet (Phase 32 was 1D only).
   - Impact on this phase: This is the key prediction of CORR-03. Must verify on 4x4 OBC lattice.
   - Recommendation: Include a 2D Fisher metric computation task in the plan, even if only 4x4.

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| --- | --- | --- | --- |
| NL sigma model for S=1/2 | Quantum corrections too large; sigma model invalid | Direct QMC correlation functions (cite literature) | LOW -- QMC data already exists |
| 4x4 ED for 2D | Finite-size effects too large; can't see Neel regime | Use published QMC data (Sandvik 2025) for benchmarks | LOW -- literature values sufficient |
| Fisher smoothness argument | Log divergences in d=2 worse than expected | Conditional argument: "For d>=3, smooth. For d=2, smooth at finite L with log corrections" | LOW -- statement becomes weaker but still useful |
| Neel order for S=1/2 d=2 | Cannot establish rigorously | State as strong numerical evidence + conditional theorem | LOW -- this is standard in the field |
| CORR-03 completely | Fisher metric provably fails with algebraic decay | Report as stop/rethink trigger. d>=2 chain becomes conditional. | HIGH -- fundamentally changes the v9.0 structure |

**Decision criteria:** If the 4x4 2D Fisher metric shows g_bulk ~ O(1/N) scaling (like 1D), abandon the Neel order rescue and report the d>=2 chain as conditional. If g_bulk ~ O(1) (constant or slowly varying), the approach is validated.

## Sources

### Primary (HIGH confidence)

- Dyson, Lieb, Simon, "Phase transitions in quantum spin systems with isotropic and nonisotropic interactions," J. Stat. Phys. 18 (1978) 335-383 -- Neel order proof
- Kennedy, Lieb, Shastry, "Existence of Neel order in some spin-1/2 Heisenberg antiferromagnets," J. Stat. Phys. 53 (1988) 1019-1030 -- Extension to S=1/2
- Hastings, Koma, "Spectral gap and exponential decay of correlations," CMP 265 (2006) 781-804, arXiv:math-ph/0507008 -- Exponential clustering theorem
- Nachtergaele, Sims, "Lieb-Robinson bounds and the exponential clustering theorem," CMP 265 (2006) 119-130, arXiv:math-ph/0506030 -- LR bounds
- Haldane, "Continuum dynamics of the 1-D Heisenberg antiferromagnet: Identification with the O(3) nonlinear sigma model," Phys. Lett. A 93 (1983) 464 -- NL sigma model mapping
- Haldane, "Nonlinear field theory of large-spin Heisenberg antiferromagnets," PRL 50 (1983) 1153 -- Sigma model + topological term
- Chakravarty, Halperin, Nelson, "Two-dimensional quantum Heisenberg antiferromagnet at low temperatures," PRB 39 (1989) 2344 -- NL sigma model in d=2
- Manousakis, "The spin-1/2 Heisenberg antiferromagnet on a square lattice," Rev. Mod. Phys. 63 (1991) 1-62 -- Comprehensive review
- Auerbach, "Interacting Electrons and Quantum Magnetism," Springer (1994) -- Textbook: Ch. 11-14 for spin waves and sigma model
- Braunstein, Caves, "Statistical distance and the geometry of quantum states," PRL 72 (1994) 3439 -- Fisher metric definition

### Secondary (MEDIUM confidence)

- Sandvik, "High-precision ground state parameters of the 2D spin-1/2 Heisenberg model on the square lattice," arXiv:2601.20189 (2025) -- State-of-the-art QMC benchmarks
- Canali, Girvin, Wallin, "Spin-wave velocity renormalization in the 2D Heisenberg AFM at zero temperature," PRB 45 (1992) 10131 -- Z_c renormalization factor
- Reger, Young, "Monte Carlo simulations of the spin-1/2 Heisenberg antiferromagnet on a square lattice," PRB 37 (1988) 5978 -- Early QMC confirmation of Neel order for S=1/2 d=2
- Affleck, Kennedy, Lieb, Tasaki, "Rigorous results on valence-bond ground states in antiferromagnets," CMP 115 (1988) 477 -- AKLT gap proof
- Nachtergaele, "Quantum spin systems after DLS 1978," arXiv:math-ph/0603017 -- Review of post-DLS developments

### Tertiary (LOW confidence)

- Phase 32 FISH-01/02/03 results (project-internal) -- Validated against Hastings-Koma; FISH-03 failure is definitive for 1D
- The CORR-03 argument for Fisher smoothness with algebraic decay (constructed in this research) -- Novel argument, not found in literature

## Metadata

**Confidence breakdown:**
- Mathematical framework: HIGH -- Heisenberg model and NL sigma model are textbook material
- Standard approaches (CORR-01, CORR-02): HIGH -- Two-tier strategy and sigma model derivation are well-established
- Computational tools: HIGH -- Existing ED infrastructure covers most needs; 2D extension is straightforward
- Validation strategies: HIGH -- QMC benchmarks exist at 6-digit precision
- CORR-03 (Fisher smoothness for algebraic decay): LOW-MEDIUM -- Novel argument; no existing theorem; conditional conclusion

**Research date:** 2026-03-29
**Valid until:** Indefinite for physics results (Neel order, sigma model, spin-wave theory). QMC benchmarks stable (Sandvik 2025 is state-of-the-art). Tool versions may change.

## Caveats and Alternatives

### Self-Critique

1. **What assumption am I making that might be wrong?** The CORR-03 argument assumes that Neel order sublattice alternation dominates the Fisher metric at d=2, with Goldstone corrections bounded. This could fail if the Goldstone contributions to the reduced density matrix are larger than the mean-field Neel contribution at small subsystem sizes. For |Lambda| = 1 (single site), the reduced state in the singlet ground state is rho = I/2 regardless of position -- no sublattice alternation visible. Need |Lambda| >= 2 to see Neel structure.

2. **What alternative approach did I dismiss too quickly?** Schwinger boson mean-field theory provides an alternative to the Holstein-Primakoff route for the sigma model derivation. It handles S=1/2 more naturally (no unphysical states). Dismissed because it is less transparent for extracting c_s explicitly, but it could serve as a cross-check.

3. **What limitation of my recommended method am I understating?** The 4x4 lattice is very small for seeing asymptotic Neel physics. Finite-size effects are significant. The staggered magnetization at L=4 will be substantially different from the thermodynamic limit value. The Fisher metric numerical check on 4x4 is indicative but not conclusive.

4. **Is there a simpler method I overlooked?** For CORR-01, one could simply cite the Sandvik 2025 QMC paper (which computes all relevant ground state parameters to high precision) rather than deriving anything. The analytical derivation (sigma model) is needed for CORR-02 specifically, but CORR-01 could be handled almost entirely by literature citation.

5. **Would a specialist disagree with my recommendation?** A mathematical physicist might object that the sigma model derivation is not rigorous (it involves the coherent state path integral, which is formally ill-defined for finite S). A condensed matter physicist would consider this standard and uncontroversial. The level of rigor matches what is expected in the project (physicist's proof, not constructive QFT).
