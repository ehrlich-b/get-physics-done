# Phase 34: Emergent Lorentz Invariance - Research

**Researched:** 2026-03-29
**Domain:** Emergent spacetime symmetry / Quantum magnetism / Lattice field theory
**Confidence:** MEDIUM

## Summary

Phase 34 must derive emergent Lorentz invariance from the lattice, using the O(3) NL sigma model effective theory established in Phase 33. The problem decomposes into three independent requirements: (LRNZ-01) establishing that continuous rotational symmetry (isotropy) is restored from discrete lattice symmetry at long wavelengths; (LRNZ-02) deriving Lorentz invariance from either the NL sigma model's built-in relativistic structure or via von Ignatowsky's theorem after isotropy is established; and (LRNZ-03) clarifying the relationship between the Lieb-Robinson velocity v_LR, the spin-wave velocity c_s, and the emergent speed of light c_eff.

The mathematical situation is favorable: the NL sigma model derived in Phase 33 already has a relativistic dispersion relation omega = c_s |k| built into its structure, which provides the primary (and most direct) route to Lorentz invariance. The NL sigma model action S_eff = (1/2g) int [(d_tau n)^2/c_s^2 + (nabla n)^2] is manifestly Lorentz-invariant in Euclidean signature after rescaling tau -> tau/c_s, which gives a standard O(d+1) symmetric sigma model. The von Ignatowsky route is secondary and more fragile (requiring emergent isotropy as a prerequisite). The key subtlety is quantifying how fast lattice anisotropy vanishes in the continuum limit.

**Primary recommendation:** Use the NL sigma model route as the primary derivation (LRNZ-02): the action is manifestly relativistic with c_s as the invariant speed. Use the von Ignatowsky route as a supporting/alternative argument. For LRNZ-01, cite the standard universality argument that cubic-lattice anisotropy corrections are irrelevant operators scaling as O(a^2/L^2) in the long-wavelength effective theory. For LRNZ-03, establish the hierarchy v_LR >= c_s = c_eff with explicit numerical values and physical justification for why c_s (not v_LR) is the emergent speed of light.

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| --- | --- | --- | --- | --- |
| ref-vonignatowsky1911 | Method | Isotropy + relativity principle + finite speed -> Lorentz or Galileo | Cite for secondary route; verify isotropy premise is satisfied | Plan, execution |
| ref-nachtergaele-sims2006 (CMP 265, 119; math-ph/0603064) | Backbone theorem | LR velocity provides rigorous upper bound on signal propagation | Cite for v_LR; use in LRNZ-03 causal structure analysis | Plan, execution, verification |
| Hamma et al. 2009 (PRL 102, 017204; arXiv:0808.2495) | Prior work | LR bounds and emergent speed of light from topological order on lattice | Cite as precedent; note differences (topological vs Neel order) | Plan, execution |
| Paper 6: v_LR = 8eJ/(e-1) | Prior artifact | SWAP lattice LR velocity = 12.66 J | Use in LRNZ-03; compare with c_s = 1.659 Ja | Plan, execution, verification |
| Phase 33 CORR-02: NL sigma model | Prior artifact | S_eff with c_s = 1.659 Ja, g = 9.18 | Foundation for LRNZ-02 derivation | Plan, execution |
| Davoudi-Savage 2012 (PRD 86, 054505; arXiv:1204.4146) | Method | Rotational symmetry restoration in lattice field theories: O(a^2) corrections | Cite for LRNZ-01 anisotropy scaling | Plan, execution |
| CHN 1989 (PRB 39, 2344) | Standard reference | NL sigma model analysis of 2D quantum Heisenberg AFM | Foundation for relativistic structure of effective theory | Plan, execution |
| Baccetti-Tate-Visser 2012 (JHEP; arXiv:1112.1466) | Analysis | Detailed analysis of von Ignatowsky's premises and evasions | Cite for precise statement of von Ignatowsky premises | Plan, execution |

**Missing or weak anchors:** There is no single paper that derives emergent Lorentz invariance specifically for the Heisenberg AFM / SWAP lattice from the NL sigma model. The argument must be assembled from standard components (NL sigma model structure + universality + LR bounds). This is standard condensed matter physics reasoning but not a single-reference result. Confidence: MEDIUM.

## Conventions

| Choice | Convention | Alternatives | Source |
| --- | --- | --- | --- |
| Metric signature | (-,+,+,...,+) for Lorentzian | (+,-,-,-) | Project convention (SUMMARY.md) |
| Units | Natural (hbar=1, k_B=1), lattice spacing a=1 unless continuum limit | SI, Gaussian | Project convention |
| Velocity units | [lattice sites]/[time] = Ja (with a=1) | Ja/hbar in non-natural units | Phase 33 convention |
| Euclidean time | tau = it, so Euclidean action has (+,+,...,+) signature | Minkowski time t | Standard for sigma model |
| Sigma model field | O(3) n-field, n^2 = 1 | CP^1 representation | Phase 33 convention |
| LR velocity | v_LR = 8eJ/(e-1) for SWAP on Z^1 | Dimension-dependent generalizations | Paper 6 |
| Fourier convention | e^{-ikx} forward | e^{+ikx} | Project convention |

**CRITICAL: All equations and results below use these conventions. The NL sigma model is written in Euclidean signature (imaginary time tau). Wick rotation to Minkowski signature gives the Lorentzian theory. The spin-wave velocity c_s has dimensions of Ja (energy times lattice spacing) when a=1. When a != 1, c_s = 1.659 Ja has dimensions of [length]/[time] = [velocity].**

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in This Phase |
| --- | --- | --- | --- |
| S_eff = (1/2g) int d^d x dtau [(d_tau n)^2/c_s^2 + (nabla n)^2] | O(3) NL sigma model (Euclidean) | Phase 33, Eq. (33.11) | Starting point for LRNZ-02 |
| omega_k = c_s \|k\| | Magnon dispersion (linear, isotropic at long wavelength) | LSWT; Phase 33 | Relativistic dispersion = Lorentz invariance |
| v_LR = 8eJ/(e-1) ~ 12.66 J | Lieb-Robinson velocity for SWAP on Z^1 | Paper 6, Phase 8 | Upper bound on signal speed for LRNZ-03 |
| c_s = sqrt(rho_s / chi_perp) = 1.659 Ja | Spin-wave velocity | Phase 33, Eq. (33.14) | Emergent speed of light candidate |
| omega_k = c_s sqrt(k_x^2 + k_y^2 + O((ka)^2 cos(4*phi))) | Lattice-corrected dispersion | LSWT on square lattice | Quantifies anisotropy for LRNZ-01 |
| Lorentz: ds^2 = -c_s^2 dtau_M^2 + dx^2 | Emergent Lorentzian metric (Minkowski) | Wick rotation of sigma model | Target metric for LRNZ-02 |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --- | --- | --- | --- |
| Rescaling to isotropic form | tau' = tau/c_s makes sigma model O(d+1) symmetric | LRNZ-02 derivation | Standard; Sachdev Ch. 13 |
| Wick rotation | Euclidean -> Minkowski: tau -> it gives Lorentzian signature | LRNZ-02 Lorentzian structure | Zinn-Justin Ch. 6 |
| Symanzik effective theory / irrelevant operators | Classify lattice corrections by dimension; anisotropy is irrelevant | LRNZ-01 anisotropy bounds | Symanzik 1983; Davoudi-Savage 2012 |
| Universality argument | Cubic lattice models in O(3) universality class share continuum limit | LRNZ-01 isotropy restoration | Sachdev; Zinn-Justin |
| LR bounds analysis | Rigorous upper bound on information propagation speed | LRNZ-03 causal structure | Nachtergaele-Sims 2006 |
| von Ignatowsky's theorem | Isotropy + relativity principle + homogeneity -> Lorentz/Galileo | LRNZ-02 alternative route | von Ignatowsky 1911; Baccetti-Tate-Visser 2012 |

### Approximation Schemes

| Approximation | Small Parameter | Regime of Validity | Error Estimate | Alternatives if Invalid |
| --- | --- | --- | --- | --- |
| NL sigma model continuum limit | ka << 1 (long wavelength) | Wavelengths >> lattice spacing | O((ka)^2) lattice corrections | Stay on lattice; use ED/QMC |
| Isotropic dispersion | (ka)^2 (anisotropy corrections) | k << pi/a | O((ka)^2) direction-dependent terms | Full lattice dispersion |
| Linear dispersion omega = c_s \|k\| | (ka)^2 (curvature of dispersion) | k << pi/a | O((ka)^2) cubic/quartic terms | Full dispersion relation |

## Standard Approaches

### Approach 1: NL Sigma Model Route (RECOMMENDED for LRNZ-02)

**What:** The O(3) NL sigma model action from Phase 33 is manifestly relativistic. After rescaling tau' = tau/c_s, the action becomes S_eff = (rho_s/(2c_s)) int d^d x dtau' [(d_{tau'} n)^2 + (nabla n)^2], which is an O(d+1) rotationally symmetric sigma model in (d+1)-dimensional Euclidean space. Wick rotation tau' -> it gives a Lorentzian field theory with speed c_s.

**Why standard:** This is how emergent Lorentz invariance is understood in the condensed matter community for antiferromagnets. The relativistic structure of the NL sigma model is a standard textbook result (Sachdev, "Quantum Phase Transitions", Ch. 13; Altland & Simons, "Condensed Matter Field Theory", Ch. 6). The connection between antiferromagnetic magnon dispersion omega = c_s|k| and emergent relativity is well-established.

**Track record:** The O(3) NL sigma model has been the standard effective theory for the S=1/2 Heisenberg AFM since Haldane (1983) and CHN (1989). Its predictions match QMC to sub-percent accuracy (Phase 33 demonstrated 0.3% for c_s).

**Key steps:**

1. Start from Phase 33 result: S_eff = (1/2g) int d^d x dtau [(d_tau n)^2/c_s^2 + (nabla n)^2]
2. Rescale Euclidean time: tau' = tau/c_s. This transforms the action to the isotropic form S_eff = (rho_s/(2c_s)) int d^d x dtau' [(d_{tau'} n)^2 + (nabla n)^2], which has manifest O(d+1) Euclidean symmetry (rotations mixing spatial and temporal directions)
3. Identify: the sigma model propagator in momentum space is G(k, omega_E) = 1/(k^2 + omega_E^2/c_s^2), which is the Euclidean version of the relativistic propagator with "speed of light" = c_s
4. Wick rotate: tau' -> it, giving the Lorentzian action with ds^2 = -c_s^2 dt^2 + dx^2, the emergent Minkowski metric with speed c_s
5. Identify c_s = 1.659 Ja as the emergent speed of light

**Known difficulties at each step:**

- Step 1: No difficulty; this is the Phase 33 deliverable
- Step 2: The rescaling is exact within the sigma model; lattice corrections break the O(d+1) symmetry at O((ka)^2)
- Step 3: The propagator is standard; must note it applies only at low energies (k << pi/a)
- Step 4: Wick rotation requires reflection positivity of the lattice theory (Osterwalder-Schrader). For the Heisenberg AFM on a bipartite lattice, reflection positivity holds (Dyson-Lieb-Simon 1978). This is a known result, not a new derivation.
- Step 5: The identification is physical: c_s is the speed at which information propagates in the low-energy effective theory. It is NOT the LR bound v_LR.

### Approach 2: von Ignatowsky Route (SUPPORTING)

**What:** Von Ignatowsky's theorem (1911) derives the Lorentz transformations from: (1) relativity principle (equivalence of inertial frames), (2) homogeneity of space and time, (3) isotropy of space, (4) linearity of transformations. The existence of a finite invariant speed is a CONSEQUENCE, not an assumption. Given that the emergent theory at long wavelengths has continuous isotropy (from universality) and a finite maximum propagation speed (from LR bounds), von Ignatowsky gives Lorentz invariance with the invariant speed determined by the dynamics.

**When to use:** As a supporting argument after LRNZ-01 (isotropy) is established. Also useful as a conceptual framework connecting the discrete lattice to the continuum.

**Key steps:**

1. Establish emergent isotropy (LRNZ-01): discrete lattice symmetry (octahedral group O_h) flows to continuous SO(d) at long wavelengths via universality
2. Identify the emergent relativity principle: the sigma model is the same effective theory regardless of the "frame" (lattice position / subsystem choice)
3. Apply von Ignatowsky: isotropy + homogeneity + linearity -> Lorentz group with some invariant speed c
4. Identify c = c_s from the sigma model dispersion relation

**Tradeoffs:** More conceptually illuminating but logically more complex than Approach 1. Requires LRNZ-01 as an independent prerequisite. The sigma model route gives Lorentz invariance directly without needing to establish isotropy first (isotropy is built into the sigma model action by construction for the square lattice).

### Anti-Patterns to Avoid

- **Assuming Lorentz invariance by fiat:** The entire point of this phase is to DERIVE it. Never write "the effective theory is Lorentz-invariant" without showing why.
  - _Example:_ "The sigma model is relativistic, so the theory is Lorentz-invariant" -- this is circular unless you explain WHY the sigma model has relativistic structure (it comes from the lattice symmetry + universality).

- **Conflating v_LR with the speed of light:** v_LR is a rigorous upper bound on ALL information propagation (including non-universal lattice-scale effects). c_s is the physical propagation speed of the low-energy excitations (magnons). v_LR >> c_s in general. The emergent speed of light is c_s, not v_LR.
  - _Example:_ Paper 6 gives v_LR = 8eJ/(e-1) ~ 12.66 J while c_s = 1.659 J. The ratio v_LR/c_s ~ 7.6. Calling v_LR "the speed of light" would overestimate the emergent speed by nearly an order of magnitude.

- **Conflating Fisher metric with causal structure:** The Fisher metric g_ij is SPATIAL and Riemannian (positive-definite). It does NOT provide the Lorentzian signature. Causal structure (light cones) comes from the LR bounds and sigma model propagation, not from the Fisher metric. The Fisher metric provides the spatial part of the emergent metric: ds^2 = -c_s^2 dt^2 + g_{ij} dx^i dx^j.
  - _Example:_ "The Fisher metric gives a Lorentzian spacetime" is wrong. The Fisher metric gives Riemannian spatial geometry; the temporal direction and Lorentzian signature come from modular flow / LR bounds / sigma model time.

- **Invoking von Ignatowsky without verifying isotropy:** The theorem requires continuous rotational invariance. A cubic lattice has only discrete O_h symmetry. Must establish that continuous isotropy emerges at long wavelengths before applying the theorem.

## Existing Results to Leverage

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
| --- | --- | --- | --- |
| NL sigma model action | S_eff = (1/2g) int [(d_tau n)^2/c_s^2 + (nabla n)^2] | Phase 33 CORR-02, Eq. (33.11) | Starting point; do not re-derive |
| Spin-wave velocity | c_s = 1.659 Ja (QMC: 1.65880(6)) | Phase 33, Eq. (33.14) | Use directly; do not re-derive |
| LR velocity for SWAP | v_LR = 8eJ/(e-1) ~ 12.66 J | Paper 6, Phase 8, Eq. (08-03.3) | Use in LRNZ-03 comparison |
| Reflection positivity for Heisenberg AFM | Holds on bipartite lattices | Dyson-Lieb-Simon 1978 | Justifies Wick rotation in Step 4 |
| O_h -> SO(3) isotropy restoration | Anisotropy corrections O(a^2) for cubic lattice | Symanzik; Davoudi-Savage 2012 | Cite for LRNZ-01 |
| von Ignatowsky's theorem | Isotropy + homogeneity + linearity -> Lorentz or Galileo | von Ignatowsky 1911; Gorini-Zecca | Cite for secondary route |

**Key insight:** The NL sigma model derivation in Phase 33 already did the hard work. Phase 34 is primarily about RECOGNIZING that the sigma model structure implies Lorentz invariance, and then carefully analyzing what "emergent" means (lattice corrections, anisotropy, velocity hierarchy). Do not re-derive the sigma model.

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
| --- | --- | --- | --- |
| Magnon dispersion on square lattice | omega_k = 2JSa sqrt(1 - gamma_k^2) where gamma_k = (cos k_x + cos k_y)/2 | LSWT, Auerbach Ch. 11 | Near k = (pi,pi): omega ~ c_s |k - Q| with c_s = 2sqrt(2) JSa |
| Lattice anisotropy of dispersion | omega_k ~ c_s|k|(1 + alpha (ka)^2 cos(4*phi_k) + ...) | LSWT expansion at small k | alpha = O(1) coefficient; quantifies LRNZ-01 |
| LR bounds in d dimensions | v_LR <= 2 sum_x |x| ||h(x)||_op * e^{mu|x|} / (e^{mu|x|} - 1) | Nachtergaele-Sims 2006 | Nearest-neighbor: v_LR proportional to zJ |
| Hamma et al. result | v_LR <= sqrt(2) * e * c_photon (in 2D toric code) | arXiv:0808.2495 | Precedent for v_LR > c_eff in lattice systems |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| --- | --- | --- | --- | --- |
| Haldane mapping | Haldane | 1983 | NL sigma model from Heisenberg AFM | Relativistic structure of the effective theory |
| CHN analysis | Chakravarty, Halperin, Nelson | 1989 | 2D quantum sigma model | c_s extraction, universality, phase diagram |
| LR bounds and speed of light | Hamma, Markopoulou, Premont-Schwarz, Severini | 2009 | v_LR vs emergent c on lattice | v_LR >= c_eff with explicit ratio |
| Inertial frames without relativity | Baccetti, Tate, Visser | 2012 | Precise statement of von Ignatowsky premises | What exactly is needed for the theorem |
| Rotational symmetry restoration | Davoudi, Savage | 2012 | O(a^2) anisotropy corrections on cubic lattice | Quantitative scaling of isotropy restoration |
| Restoring isotropy in 3D | Hasenbusch | 2021 | Ising universality class, cubic anisotropy corrections | Explicit scaling exponents; rho ~ 2 for O(N) |
| Emergent Lorentz, Lifshitz sigma model | Gomes, Nascimento, Petrov, da Silva | 2016 | Low-energy Lorentz in Lifshitz NL sigma models | RG flow toward Lorentz invariance in z=2 models |

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
| --- | --- | --- | --- |
| SymPy | latest | Symbolic manipulation of dispersion relation expansion, verification of anisotropy scaling | Already in project |
| NumPy/SciPy | >=1.20/>=1.10 | Numerical verification of velocity ratios, anisotropy coefficients | Already in project |

### Supporting Tools

| Tool | Purpose | When to Use |
| --- | --- | --- |
| matplotlib | Plot dispersion relation iso-frequency contours showing isotropy restoration | Visualization of LRNZ-01 if needed |
| Existing ED code (code/ed_entanglement.py) | Verify dispersion relation on small lattices | Cross-check if needed |

### Computational Feasibility

| Computation | Estimated Cost | Bottleneck | Mitigation |
| --- | --- | --- | --- |
| Symbolic dispersion expansion | < 1 min | None | Standard SymPy |
| Numerical anisotropy coefficient extraction | < 1 min | None | Standard numerics |
| Velocity ratio verification | < 1 sec | None | Arithmetic |

**No significant computation is needed for this phase.** The key results are analytical (recognizing Lorentz structure in the sigma model) and the numerical values (c_s, v_LR) are already established from Phases 8 and 33.

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| --- | --- | --- | --- |
| Dimensional analysis of c_s | Correct velocity dimensions | [c_s] = [Ja] = [energy * length] = [length/time] when hbar=1 | Consistent |
| v_LR > c_s | LR bound exceeds physical speed | 12.66 J > 1.659 Ja (with a=1: 12.66 J > 1.659 J) | v_LR/c_s ~ 7.6 |
| Anisotropy vanishes at k->0 | Long wavelength theory is isotropic | Expand LSWT dispersion at small k around AF ordering vector | Leading anisotropy ~ (ka)^2 cos(4phi) |
| Euclidean O(d+1) symmetry of rescaled action | Sigma model is isotropic after tau rescaling | Verify action depends only on (nabla' n)^2 with nabla' = (d/dtau', d/dx) | Yes by construction |
| Wick rotation consistency | Euclidean -> Minkowski gives correct signature | Check propagator poles: G^{-1} = k^2 + omega_E^2/c_s^2 -> k^2 - omega^2/c_s^2 | Correct Lorentzian propagator |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| --- | --- | --- | --- |
| Free magnon dispersion | g -> 0 (classical limit) | omega = c_s^{cl} |k| = sqrt(2) Ja |k| | LSWT |
| Isotropic limit | k -> 0 | omega = c_s |k| (direction-independent) | Universality |
| Classical limit (S -> inf) | 1/S -> 0 | c_s -> c_s^{cl} = sqrt(2) Ja | LSWT |
| 1D sigma model | d=1 | Lorentz-invariant O(3) sigma model with dynamical mass gap | Haldane 1983; well-studied |

### Numerical Validation

| Test | Method | Tolerance | Reference Value |
| --- | --- | --- | --- |
| c_s numerical value | Compare with QMC | < 1% | 1.65880(6) Ja (Sandvik 2025) |
| v_LR numerical value | Compare with Paper 6 | Exact | 8eJ/(e-1) ~ 12.66 J |
| Anisotropy coefficient | LSWT expansion at small k | Qualitative | O(1) coefficient times (ka)^2 |

### Red Flags During Computation

- If v_LR < c_s for any configuration, something is wrong (LR bound must always exceed physical speed)
- If the sigma model action is NOT O(d+1) symmetric after time rescaling, the derivation has an error
- If anisotropy corrections do NOT vanish as a -> 0, the universality argument fails (this would be extraordinary and indicate we are not in the O(3) universality class)
- If the Wick-rotated propagator has wrong-sign poles, the reflection positivity argument has failed

## Common Pitfalls

### Pitfall 1: Conflating v_LR with c_eff

**What goes wrong:** The Lieb-Robinson velocity v_LR is treated as the emergent speed of light. This is physically incorrect. v_LR is a rigorous upper bound on ALL signal propagation (including non-universal UV effects), while the emergent speed of light c_eff = c_s is the speed of the low-energy excitations (magnons/Goldstone modes).
**Why it happens:** Both are "speed of light"-like quantities. In some simplified discussions (Hamma et al. 2009), the ratio v_LR/c_photon is computed but the distinction is not always emphasized.
**How to avoid:** Always state: v_LR (rigorous bound) >= c_s (physical magnon speed) = c_eff (emergent speed of light). Quote both numbers: v_LR = 12.66 J, c_s = 1.659 Ja. The factor ~7.6 between them is physical and expected.
**Warning signs:** Any equation where v_LR appears in the emergent metric ds^2 = -v_LR^2 dt^2 + ...
**Recovery:** Replace v_LR with c_s and state the correct hierarchy.

### Pitfall 2: Circular Logic in the Isotropy Argument

**What goes wrong:** Using Lorentz invariance to justify the continuum limit that is needed to get the isotropy that is needed for von Ignatowsky.
**Why it happens:** The von Ignatowsky route requires continuous isotropy, which comes from the continuum limit, which one might think requires Lorentz invariance.
**How to avoid:** The isotropy restoration (LRNZ-01) must be established INDEPENDENTLY of Lorentz invariance, using the universality argument: lattice systems in the O(3) universality class have emergent SO(d) symmetry at long wavelengths regardless of the specific lattice geometry. This is a statement about RG flow, not about Lorentz invariance. Alternatively, use the NL sigma model route (Approach 1) which gives Lorentz invariance without needing isotropy as a separate input.
**Warning signs:** Any step that assumes what is being proved.
**Recovery:** Use the NL sigma model route, which avoids this issue entirely.

### Pitfall 3: Missing the Distinction Between Spatial and Spacetime Metrics

**What goes wrong:** The Fisher metric g_ij (Riemannian, spatial) is confused with the spacetime metric g_{mu nu} (Lorentzian, spacetime).
**Why it happens:** Both are called "metrics" and both come from the same physical system.
**How to avoid:** Always be explicit: Fisher metric g_ij has indices i,j = 1,...,d (spatial only). Spacetime metric g_{mu nu} has indices mu,nu = 0,...,d (including time). The assembly is: ds^2 = -c_s^2 dt^2 + g_{ij} dx^i dx^j. The Fisher metric provides ONLY the spatial part. The temporal part comes from modular flow / LR bounds / sigma model time, which is Phase 35-36 territory.
**Warning signs:** Fisher metric appearing with a time index; claims that Fisher metric is Lorentzian.
**Recovery:** Separate spatial and temporal components explicitly.

### Pitfall 4: Ignoring Lattice Corrections to Isotropy

**What goes wrong:** Claiming isotropy is "exact" rather than emergent. On a square lattice, the spin-wave dispersion is omega_k = 2JSa sqrt(1 - gamma_k^2) with gamma_k = (cos k_x + cos k_y)/2, which is NOT isotropic at finite k.
**Why it happens:** At k -> 0, the dispersion linearizes to omega ~ c_s|k|, which is isotropic. But at finite k, there are O((ka)^2) direction-dependent corrections.
**How to avoid:** Explicitly compute the leading anisotropy correction by expanding the lattice dispersion around the AF ordering vector Q = (pi, pi). Show that it scales as O((ka)^2) and is irrelevant in the RG sense. State that isotropy is emergent at long wavelengths, not exact.
**Warning signs:** Claims of exact isotropy on a lattice.
**Recovery:** Compute the anisotropy correction and show it is parametrically small.

## Level of Rigor

**Required for this phase:** Physicist's proof / controlled approximation

**Justification:** The NL sigma model route is built on the well-established effective field theory framework (Phase 33 already validated to 0.3% against QMC). The connection between the sigma model's relativistic structure and emergent Lorentz invariance is standard condensed matter physics. Formal proof (constructive QFT level) is not required and would be disproportionate to the contribution.

**What this means concretely:**

- The NL sigma model action is taken as established (from Phase 33)
- The rescaling tau' = tau/c_s -> O(d+1) symmetry is an algebraic identity (no approximation)
- The universality argument for isotropy restoration is stated with reference to RG theory (not proved from scratch)
- Lattice corrections are estimated by dimensional analysis and LSWT expansion (not computed to all orders)
- The velocity hierarchy v_LR >= c_s is verified numerically (12.66 J > 1.659 J)
- Reflection positivity is cited from Dyson-Lieb-Simon (not re-proved)

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| --- | --- | --- | --- |
| Assume Lorentz a priori | Derive from lattice universality | Haldane 1983; CHN 1989 | Lorentz emerges from AFM effective theory |
| v_LR as speed of light | c_s as speed of light, v_LR as upper bound | Hamma et al. 2009 | Correct physical identification |
| von Ignatowsky alone | Sigma model + von Ignatowsky (dual routes) | This work | More robust derivation |

**Superseded approaches to avoid:**

- **Assuming Lorentz by fiat in condensed matter effective theories:** Before Haldane/CHN, the relativistic structure of antiferromagnet effective theories was sometimes just assumed. Now it is derived from the lattice Hamiltonian. Do not revert to the old assumption.
- **Identifying v_LR = c (speed of light):** Early work on emergent spacetime from lattice models sometimes used this identification. Hamma et al. (2009) showed that v_LR exceeds the emergent speed by a factor of O(1) to O(10). Use c_s.

## Open Questions

1. **Exact anisotropy exponent for O(3) universality class**
   - What we know: Anisotropy corrections scale as O(a^rho) with rho ~ 2 for cubic lattices in the large-N approximation of O(N) models (Hasenbusch 2021; Davoudi-Savage 2012).
   - What's unclear: The exact value of rho for O(3) in d=2+1. Large-N gives rho ~ 2; the actual O(3) value might differ slightly.
   - Impact on this phase: Does not affect the qualitative argument (anisotropy vanishes in continuum limit) but affects the quantitative bound in LRNZ-01.
   - Recommendation: State rho >= 2 based on large-N and cite numerical evidence. The exact value is not needed for the derivation.

2. **v_LR in d >= 2 for the SWAP Hamiltonian**
   - What we know: Paper 6 computes v_LR = 8eJ/(e-1) for the 1D SWAP chain. In d dimensions, v_LR depends on the coordination number z and lattice geometry.
   - What's unclear: The exact v_LR for the SWAP Hamiltonian on a 2D square lattice or 3D cubic lattice.
   - Impact on this phase: Affects the quantitative v_LR/c_s ratio in d >= 2, but not the qualitative hierarchy v_LR > c_s.
   - Recommendation: Use the 1D result as the concrete example. Note that the d >= 2 v_LR is expected to be larger (more neighbors -> faster propagation), maintaining v_LR > c_s.

3. **Osterwalder-Schrader reconstruction for the d >= 2 sigma model**
   - What we know: The Wick rotation from Euclidean to Minkowski is rigorous when OS axioms hold. Reflection positivity for the Heisenberg AFM on bipartite lattices is proved (DLS 1978).
   - What's unclear: Whether the full OS reconstruction program gives a Wightman QFT for the d=2+1 sigma model (this is related to the Yang-Mills mass gap problem).
   - Impact on this phase: Does not block the physicist's-proof-level derivation. A rigorous constructive QFT proof would require solving an open millennium problem.
   - Recommendation: State that reflection positivity holds, Wick rotation is justified at the effective theory level, and note that full OS reconstruction is an open problem that goes beyond the scope of this work.

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| --- | --- | --- | --- |
| NL sigma model route | Sigma model not valid (e.g., strong coupling destroys low-energy Lorentz) | von Ignatowsky route (requires independent isotropy proof) | Medium: need LRNZ-01 independently |
| von Ignatowsky route | Emergent isotropy cannot be established (anisotropy persists) | NL sigma model route only (Lorentz from sigma model structure) | Low: sigma model route is primary anyway |
| Both routes fail | Neither sigma model is Lorentz-invariant nor is isotropy restored | Fall back to emergent diffeomorphism invariance only; flag Lorentz as additional assumption | High: fundamentally changes the claim structure |

**Decision criteria:** If the sigma model dispersion shows persistent anisotropy that does NOT scale as O(a^2), or if the sigma model coupling g is so large that the effective theory breaks down, the NL sigma model route fails. This would be extraordinary given the 0.3% QMC validation of Phase 33. If isotropy restoration fails, it would mean the square lattice Heisenberg AFM is NOT in the O(3) universality class, contradicting decades of numerical and theoretical work. Both failure modes are extremely unlikely.

## LRNZ-01 Specific: Emergent Isotropy

### The Argument

The square lattice has discrete D_4 symmetry (dihedral group of the square, order 8), not continuous SO(2). In d=3, the cubic lattice has O_h symmetry (octahedral group, order 48), not continuous SO(3). The question is: does continuous rotational symmetry emerge at long wavelengths?

**Standard answer (HIGH confidence):** Yes, for systems in the O(3) universality class. The argument:

1. **Lattice dispersion at small k:** Expand omega_k = 2JSa sqrt(1 - gamma_k^2) around the ordering vector Q = (pi, pi). At small q = k - Q:
   - omega_q ~ c_s |q| [1 + alpha_4 (qa)^2 cos(4 phi_q) + O((qa)^4)]
   - where phi_q is the angle of q in momentum space, and alpha_4 is an O(1) lattice-dependent coefficient

2. **RG classification:** The cos(4 phi_q) term corresponds to a rank-4 cubic anisotropy operator in the effective action. In the Symanzik effective theory, this operator has scaling dimension d_4 = d + 2 (naive) and is IRRELEVANT at the O(3) Wilson-Fisher fixed point (d_4 > d+1, the spacetime dimension). For the large-N limit, the anisotropy exponent is rho ~ 2, meaning anisotropy corrections vanish as (a/L)^rho with rho ~ 2.

3. **Conclusion:** At wavelengths L >> a, the effective theory is isotropic to accuracy O((a/L)^2) or better. In the continuum limit a -> 0, exact isotropy is restored.

### Quantitative Estimate

For the S=1/2 square lattice Heisenberg AFM:
- The lattice dispersion near Q = (pi, pi) is omega_q = c_s |q| sqrt(1 + (qa)^2 f(phi_q)/4 + ...)
- The anisotropy f(phi_q) contains cos(4 phi_q) terms from the lattice geometry
- At momentum q ~ 2pi/L (relevant for system size L): anisotropy ~ (a/L)^2
- For L/a = 100 (typical mesoscopic scale): anisotropy ~ 10^{-4}
- In the continuum limit L/a -> infinity: anisotropy -> 0

## LRNZ-02 Specific: Lorentz Invariance Derivation

### Primary Route (NL Sigma Model)

The detailed argument, step by step:

1. **Input:** S_eff = (1/2g) int d^d x dtau [(d_tau n)^2/c_s^2 + (nabla n)^2], from Phase 33

2. **Rescale time:** Define tau' = tau/c_s. Then d_tau = c_s d_{tau'}, and (d_tau n)^2/c_s^2 = (d_{tau'} n)^2. The action becomes:
   S_eff = (c_s/(2g)) int d^d x dtau' [(d_{tau'} n)^2 + (nabla n)^2]
   This is an O(d+1) rotationally symmetric sigma model in (d+1) Euclidean dimensions (x^1, ..., x^d, tau').

3. **Euclidean O(d+1) symmetry:** The rescaled action depends on spatial and temporal derivatives identically. Rotations in the (x^i, tau') plane are symmetries. This is the Euclidean version of Lorentz boosts.

4. **Wick rotation:** Replace tau' = it (Minkowski time). The Euclidean propagator G_E(k, omega_E) = 1/(k^2 + omega_E^2) becomes G_M(k, omega) = 1/(k^2 - omega^2), the standard relativistic propagator. In terms of original variables: G_M(k, omega) = 1/(k^2 - omega^2/c_s^2).

5. **Result:** The low-energy effective theory is Lorentz-invariant with speed of light c_s = 1.659 Ja.

### Secondary Route (von Ignatowsky)

1. **Input:** LRNZ-01 gives emergent isotropy at long wavelengths.

2. **Premises:** (a) Relativity principle: the sigma model effective theory is the same in all "inertial frames" (all lattice positions in the bulk give the same effective theory by translation invariance). (b) Homogeneity: translation invariance of the lattice -> spacetime homogeneity at long wavelengths. (c) Isotropy: from LRNZ-01. (d) Linearity: the effective theory's dispersion is linear (omega = c_s|k|), and the transformations between frames are linear at leading order.

3. **Application:** Von Ignatowsky's theorem then implies the spacetime symmetry group is either Lorentz (with finite invariant speed) or Galileo (with infinite invariant speed). Since the magnon dispersion has finite speed c_s, the Galilean option is excluded. Therefore: Lorentz with invariant speed c_s.

4. **Caveat:** The theorem applies to the long-wavelength effective theory, not to the bare lattice. Lattice corrections break Lorentz invariance at O((ka)^2). This is a feature, not a bug -- it means Lorentz invariance is emergent, not fundamental.

## LRNZ-03 Specific: Velocity Hierarchy and Causal Structure

### The Three Velocities

| Velocity | Symbol | Value (S=1/2, d=2 square) | Definition | Role |
| --- | --- | --- | --- | --- |
| Lieb-Robinson velocity | v_LR | 8eJ/(e-1) ~ 12.66 J (d=1) | Rigorous upper bound on information propagation | Light-cone bound (causal structure) |
| Spin-wave velocity | c_s | 1.659 Ja = 1.659 J (a=1) | Physical speed of magnon excitations | Emergent speed of light |
| Effective speed of light | c_eff | = c_s = 1.659 J (a=1) | Speed entering the emergent Lorentz metric | Metric ds^2 = -c_eff^2 dt^2 + g_ij dx^i dx^j |

### The Hierarchy

v_LR >= c_s = c_eff

**Why v_LR > c_s (strict inequality):**
- v_LR bounds ALL information propagation, including non-universal lattice-scale modes (optical magnons, multi-magnon continuum, lattice-scale excitations)
- c_s is the group velocity of the acoustic (Goldstone) magnons only
- The LR bound is not tight: it is an upper bound derived from operator norm estimates, not the actual maximum propagation speed
- For the 1D SWAP chain: v_LR/c_s ~ 12.66/1.659 ~ 7.6

**Why c_s = c_eff (identification):**
- c_s is the speed at which low-energy excitations propagate in the effective theory
- The NL sigma model propagator has poles at omega = c_s |k|, not at omega = v_LR |k|
- The emergent Lorentzian metric ds^2 = -c_s^2 dt^2 + dx^2 gives the correct dispersion relation
- This identification is physical (not just dimensional): c_s determines the light cone of the effective field theory
- All sub-light-speed excitations in the effective theory satisfy omega < c_s |k|

### Causal Structure

The Fisher metric g_ij (Phase 32-33) provides the spatial (Riemannian) part of the emergent geometry. The Lorentzian causal structure comes from:

1. **LR bounds:** Provide a rigorous light cone ||[A(t), B(0)]|| <= C exp(v_LR t - d(A,B)/xi). Information cannot propagate faster than v_LR.

2. **Sigma model propagation:** Within the effective theory, the physical light cone has speed c_s < v_LR. Excitations propagate at speed <= c_s.

3. **Assembly:** The emergent spacetime metric is:
   ds^2 = -c_s^2 dt^2 + g_{ij}(x) dx^i dx^j
   where g_{ij} is the Fisher metric from Phase 32-33 (spatial, Riemannian) and c_s provides the temporal/Lorentzian part.

This is NOT circular: the Fisher metric g_ij is independently established (Phase 32-33). The speed c_s is independently established (Phase 33 from the sigma model). The assembly is the new step.

## Sources

### Primary (HIGH confidence)

- [Haldane 1983, PLA 93, 464; PRL 50, 1153] - NL sigma model mapping from Heisenberg AFM; relativistic dispersion
- [Chakravarty-Halperin-Nelson 1989, PRB 39, 2344] - Definitive analysis of 2D quantum sigma model with spin-wave velocity
- [Nachtergaele-Sims 2006, CMP 265, 119; arXiv:math-ph/0603064] - Lieb-Robinson bounds for quantum lattice systems
- [Dyson-Lieb-Simon 1978, JSP 18, 335] - Reflection positivity and phase transitions in quantum Heisenberg models
- [Sachdev, "Quantum Phase Transitions", 2nd ed., Ch. 13] - Standard treatment of O(3) sigma model and emergent Lorentz invariance in antiferromagnets
- [Altland & Simons, "Condensed Matter Field Theory", Ch. 6] - Field-theoretic treatment of antiferromagnets and emergent relativistic structure

### Secondary (MEDIUM confidence)

- [Hamma et al. 2009, PRL 102, 017204; arXiv:0808.2495] - LR bounds and speed of light from topological order; v_LR > c_eff demonstrated
- [Baccetti-Tate-Visser 2012, JHEP; arXiv:1112.1466] - Precise analysis of von Ignatowsky premises and evasions
- [Davoudi-Savage 2012, PRD 86, 054505; arXiv:1204.4146] - Rotational symmetry restoration: O(a^2) corrections on cubic lattice
- [Hasenbusch 2021, PRB 104, 014426; arXiv:2105.09781] - Isotropy restoration in 3D Ising universality class
- [Sandvik 2025, arXiv:2601.20189] - QMC benchmarks for c_s, rho_s, chi_perp

### Tertiary (LOW confidence)

- [von Ignatowsky 1911, Arch. Math. Phys. 17] - Original theorem (difficult to access; use via Baccetti-Tate-Visser review)
- [Gorini-Zecca, "Isotropy of space"] - Modern re-derivation of von Ignatowsky result

## Metadata

**Confidence breakdown:**

- Mathematical framework: HIGH - NL sigma model structure is textbook; rescaling and Wick rotation are standard
- Standard approaches: HIGH - Both routes (sigma model and von Ignatowsky) are well-established individually
- Computational tools: HIGH - No significant computation needed; numerical values from prior phases
- Validation strategies: HIGH - Dimensional analysis, velocity hierarchy, QMC benchmarks all available
- Isotropy restoration argument: MEDIUM - Standard universality reasoning; exact exponent rho for O(3) in d=2+1 not rigorously determined
- v_LR in d >= 2: MEDIUM - Only 1D value computed explicitly (Paper 6); d >= 2 expected to maintain hierarchy but not computed
- Full OS reconstruction: LOW - Open problem in constructive QFT (related to millennium problem); not needed for physicist's proof

**Research date:** 2026-03-29
**Valid until:** Indefinite for the physics content. QMC benchmarks may be updated with higher precision.

## Caveats and Alternatives

### Self-Critique

1. **Assumption that might be wrong:** The NL sigma model being in its asymptotically free (renormalizable) regime in d=2+1. The coupling g = 9.18 is not small, so perturbative arguments about the sigma model require care. However, the 0.3% QMC match for c_s validates the sigma model description non-perturbatively.

2. **Alternative dismissed too quickly:** One could try to derive Lorentz invariance directly from LR bounds without going through the sigma model. Hamma et al. (2009) explored this for topological order. For Neel order, the LR-bounds-only approach gives v_LR as the speed, which is wrong. The sigma model route is necessary to get c_s.

3. **Limitation understated:** The von Ignatowsky route requires establishing a "relativity principle" for the emergent theory -- i.e., that the effective theory looks the same in all frames. On the lattice, there is a preferred frame (the lattice rest frame). The emergent relativity principle holds only at long wavelengths, which is the same regime where isotropy holds. This is not a separate weakness -- it is the same limitation as the isotropy restoration -- but it is an additional premise of the theorem.

4. **Simpler method overlooked?** No. The sigma model route IS the simplest method. Recognizing that the sigma model action is manifestly relativistic after time rescaling is the most direct path from lattice to Lorentz.

5. **Would a specialist disagree?** A condensed matter theorist would consider the sigma model route to Lorentz invariance completely standard and unremarkable. The main concern might be: "Why are you belaboring the obvious? The sigma model is relativistic by construction." The value of this phase is in making the argument EXPLICIT for the derivation chain, not in discovering anything new. A mathematical physicist might demand more rigor (OS reconstruction), which we acknowledge as an open problem.
