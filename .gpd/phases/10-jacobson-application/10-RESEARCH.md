# Phase 10: Jacobson Application - Research

**Researched:** 2026-03-22
**Domain:** Entanglement thermodynamics / Semiclassical gravity / Emergent spacetime
**Confidence:** MEDIUM

## Summary

Phase 10 must verify Jacobson's 2016 entanglement equilibrium condition for the self-modeling lattice and derive Einstein's field equations G_ab + Lambda g_ab = (8 pi G) T_ab as the leading-order IR effective description of the continuum limit. The phase receives three critical inputs from Phases 8-9: (1) the self-modeling Hamiltonian h_xy = JF with Lieb-Robinson velocity v_LR = 8eJ/(e-1) (Phase 8), (2) area-law entanglement structure via the three-perspective synthesis theorem (Phase 9), and (3) the entanglement first law delta S = delta <K_A> as an exact QI identity (Phase 9, Eq. 09-03.3).

The central challenge is the Maximal Vacuum Entanglement Hypothesis (MVEH), identified in Phase 9 as the main open gap. MVEH states that vacuum entanglement entropy in small geodesic balls is maximized at fixed volume. For conformal fields, Jacobson showed: MVEH holds if and only if the Einstein equation holds. The self-modeling lattice is NOT a conformal field theory, so MVEH cannot be derived from Jacobson's original conformal argument. Phase 10 must either (a) derive MVEH from self-modeling properties, (b) assume MVEH and derive Einstein's equations conditional on it, or (c) motivate MVEH as the natural equilibrium condition for the self-modeling state and clearly state the gap.

The recommended strategy is option (c): frame MVEH as the lattice-to-continuum analog of MaxEnt (the maximum entropy principle) applied to the self-modeling fixed point, derive Einstein's equations conditional on it, and clearly identify what self-modeling property would establish it. The derivation itself follows Jacobson 2016 closely: decompose delta S = delta S_UV + delta S_mat, use the entanglement first law for delta S_mat, identify the geometric entropy variation delta S_UV with area change via the Raychaudhuri equation, and impose delta S = 0 (entanglement equilibrium) to obtain the Einstein equation. The key identification is G = 1/(4 eta) where eta is the entanglement entropy density per unit area.

**Primary recommendation:** Follow Jacobson 2016 (arXiv:1505.04753) with the self-modeling lattice as UV completion. Decompose delta S into geometric (UV) and matter (IR) contributions. Use the entanglement first law (Phase 9, Eq. 09-03.3) for the matter part. Use the Raychaudhuri equation for the geometric part. Impose delta S = 0 (MVEH) to obtain G_ab + Lambda g_ab = (8 pi G) T_ab. Frame as Wilsonian: lattice = UV, Einstein = IR at scales >> lattice spacing. State MVEH's status honestly.

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| --- | --- | --- | --- | --- |
| ref-jacobson2016 (arXiv:1505.04753, PRL 116, 201101) | method/benchmark | THE derivation template. Entanglement equilibrium implies Einstein equations for conformal fields | read, reproduce steps, adapt to lattice | plan, execution, verification |
| ref-jacobson1995 (arXiv:gr-qc/9504004, PRL 75, 1260) | method | Original thermodynamic derivation. Provides context but 2016 version preferred | read, cite, compare | plan, discussion |
| ref-lmvr2014 (arXiv:1308.3716, JHEP 1404:195) | benchmark | Entanglement first law => linearized Einstein in holographic CFT. Validates approach | read, cite | execution, verification |
| ref-ccm2017 (arXiv:1606.08444, PRD 95, 024031) | consistency check | Emergent spatial geometry from entanglement. Spatial Einstein analog | cite, compare | verification |
| Phase 9 Synthesis Theorem (Eqs. 09-03.7a-c) | prior artifact | Area-law inputs: MI, S, delta S bounds. Direct input to Jacobson | use as starting point | plan, execution |
| Phase 9 Entanglement First Law (Eq. 09-03.3) | prior artifact | delta S = delta <K_A>, exact identity. Core equation in derivation | use directly | execution |
| Phase 8 v_LR = 8eJ/(e-1) (Eq. 08-03.3) | prior artifact | Emergent speed of light, sets causal structure | use for continuum limit | execution |
| Phase 9 Assumption Register (A1-A4) | prior artifact | Tracks which assumptions carry into Phase 10 | inherit, extend | plan, gap statement |

**Missing or weak anchors:**
- No prior work derives MVEH from a lattice quantum system. This is genuinely novel territory for the MVEH verification step.
- Jacobson 2016 works with conformal fields; extension to non-conformal fields requires a conjecture (Speranza 2016, arXiv:1602.01380 examines this). The self-modeling lattice is not conformal.
- No lattice analog of the Raychaudhuri equation exists in the literature. The geometric entropy variation must be argued through the continuum limit, not derived on the lattice.

## Conventions

| Choice | Convention | Alternatives | Source |
| --- | --- | --- | --- |
| Metric signature | (-,+,+,+) | (+,-,-,-) | Project SUMMARY.md, Wald, Jacobson 2016 |
| Units | Natural (hbar = c = k_B = 1) | SI | Project conventions |
| Entropy | S = -Tr(rho ln rho) in nats | bits (log_2) | Phase 9 conventions |
| Modular Hamiltonian | K_A = -ln(rho_A) | K = +ln(rho) (opposite sign) | Phase 9, Eq. 09-03.3 |
| Hamiltonian | H = sum h_xy (no 1/2) | H = (1/2) sum (double-counting) | Phase 8 convention |
| Einstein tensor | G_ab = R_ab - (1/2) R g_ab | -- | Wald, MTW |
| Newton's constant | G = 1/(4 eta) | G = l_P^2 | Jacobson 2012 |
| Cosmological constant | Lambda appears as integration constant | Lambda = 0 | Jacobson 2016 |
| Lattice spacing | a (to be taken small, a << L) | a_lat = 1 (Phase 8 convention) | Continuum limit |

**CRITICAL: Phase 8 used a_lat = 1. The continuum limit requires restoring a as a dimensionful parameter. The mapping is: lattice results at a_lat = 1 correspond to the continuum at scale a, with physical quantities obtained by inserting factors of a. Specifically: S_lattice = eta * A_lattice where A_lattice = |boundary| (count of boundary bonds) maps to S_continuum = eta * A_physical / a^{d-1} in the continuum.**

**Convention conflict note:** Jacobson 1995 uses (+,-,-,-) metric. Jacobson 2016 and this project use (-,+,+,+). The Raychaudhuri equation sign is affected: in our convention d(theta)/d(lambda) = -(1/(D-2)) theta^2 - sigma_{ab} sigma^{ab} - R_{ab} k^a k^b for affinely parametrized, twist-free null geodesic congruence.

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in This Phase |
| --- | --- | --- | --- |
| delta S = delta <K_A>, K_A = -ln(rho_A) | Entanglement first law | Phase 9, Eq. 09-03.3 (exact QI identity) | Core equation: relates entropy change to modular energy change |
| delta S(A) ~ O(\|boundary\|) for local perturbations | delta S boundary scaling | Phase 9, Eq. 09-03.6 (under A3) | Input: establishes area-law character of entropy variations |
| S = eta * A | Entropy-area proportionality | Jacobson 2012 (arXiv:1204.6349) | Assumption: entanglement entropy proportional to area with density eta |
| delta S = delta S_UV + delta S_mat | Entropy decomposition | Jacobson 2016 | Key decomposition: split entropy into geometric and matter parts |
| delta S_UV = -eta * delta A | Geometric entropy variation | Jacobson 2016 via Raychaudhuri | UV part: area change from geometry perturbation |
| delta S_mat = delta <K> = 2*pi integral T_ab chi^a d*Sigma^b | Matter entropy variation | Jacobson 2016 + Casini-Huerta-Myers 2011 | IR part: modular energy for ball in CFT vacuum |
| d(theta)/d(lambda) = ... - R_ab k^a k^b | Raychaudhuri equation | Wald Ch. 9; MTW | Connects area change to Ricci curvature |
| G_ab + Lambda g_ab = (8 pi G) T_ab | Einstein field equations | Target equation | The output: derived from delta S = 0 |
| G = 1/(4 eta) | Newton's constant identification | Jacobson 2012, 2016 | Maps entropy density to gravitational coupling |
| v_LR = 8eJ/(e-1) | Lieb-Robinson velocity | Phase 8, Eq. 08-03.3 | Emergent speed of light for causal structure |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --- | --- | --- | --- |
| Entanglement first law | Relates delta S to delta <K> | Matter entropy variation | Blanco-Casini-Hung-Myers 2013 (arXiv:1305.3182) |
| Raychaudhuri equation | Relates area change to R_ab k^a k^b | Geometric entropy variation | Wald, Ch. 9.2; Poisson, Ch. 2 |
| Conformal Killing vector for causal diamond | Provides chi^a for modular Hamiltonian of ball | Modular Hamiltonian identification | Casini-Huerta-Myers 2011 (arXiv:1102.0440) |
| Wilsonian effective field theory framing | Justifies lattice -> continuum passage | Continuum limit argument | Peskin-Schroeder Ch. 12; Wilson-Kogut 1974 |
| MaxEnt principle | Motivates MVEH from information theory | MVEH motivation | Jaynes 1957; Jacobson 2012 |
| Differential geometry of null congruences | Expansion, shear, twist of null geodesics | Raychaudhuri calculation | Wald Ch. 9; Poisson Ch. 2 |

### Approximation Schemes

| Approximation | Small Parameter | Regime of Validity | Error Estimate | Alternatives if Invalid |
| --- | --- | --- | --- | --- |
| First-order perturbation of vacuum | delta g_ab, delta phi | Small deviations from MSS | O(delta^2) -- Jacobson's argument is first-order only | Second-order analysis (Bueno-Myers-Witczak-Krempa 2015) gives corrections |
| Continuum limit (a -> 0) | a/L (lattice spacing / region size) | L >> a (many lattice sites in region) | O(a/L) lattice corrections | Keep lattice results, do not take continuum limit |
| Conformal field approximation | mass / UV cutoff | Massless or near-massless fields | Corrections ~ (m*R)^{2*Delta} per Speranza 2016 | Use Jacobson's conjecture for nonconformal fields |
| Small geodesic ball (R -> 0) | R * (curvature)^{1/2} | Ball small compared to curvature scale | O(R^2 * R_abcd) corrections | Finite-size corrections from higher curvature terms |

## Standard Approaches

### Approach 1: Jacobson 2016 Entanglement Equilibrium (RECOMMENDED)

**What:** Apply Jacobson's 2016 argument (arXiv:1505.04753) to the self-modeling lattice, treating the lattice as the UV completion and Einstein's equations as the leading-order IR effective description.

**Why standard:** This IS the standard modern route from entanglement to Einstein's equations without AdS/CFT. 30 years of development from Jacobson 1995 to 2016. Published in PRL with >500 citations.

**Track record:** Reproduces full nonlinear Einstein equations (not just linearized) from entanglement equilibrium for conformal fields. Extended to f(R) gravity (Chirco-Liberati), higher-derivative gravity (Bueno-Myers), and de Sitter (Jacobson-Speranza 2019).

**Key steps:**

1. **Establish the setting.** Consider a small geodesic ball B of radius R in the emergent spacetime, centered at a point p. The causal diamond D(B) has a conformal Killing vector chi^a that vanishes on the boundary of B and at the tips of the diamond.

2. **Decompose the entropy.** Write the total entanglement entropy as S = S_UV + S_mat, where S_UV = eta * A(boundary of B) is the UV-divergent geometric contribution (proportional to area) and S_mat is the finite matter contribution (state-dependent). Under a perturbation away from the locally maximally symmetric vacuum:

   delta S = delta S_UV + delta S_mat

3. **Compute delta S_UV (geometric contribution).** The area of the boundary of the ball changes due to the metric perturbation. Using the Raychaudhuri equation for a congruence of null geodesics generating the past light cone of the causal diamond:

   delta A = -(Omega_d / d(d-1)) * R^{d+2} * R_ab n^a n^b + ...

   where n^a is the unit timelike vector at p, Omega_d is the area of unit (d-1)-sphere, and R_ab is the Ricci tensor. Therefore:

   delta S_UV = -eta * delta A = eta * (Omega_d / d(d-1)) * R^{d+2} * (R_ab - R/(2d) g_ab) n^a n^b + ...

   (The trace part R/(2d) enters because the variation is at fixed volume.)

4. **Compute delta S_mat (matter contribution).** Using the entanglement first law (Phase 9, Eq. 09-03.3):

   delta S_mat = delta <K>

   For the vacuum state of a CFT restricted to a ball of radius R, the modular Hamiltonian is (Casini-Huerta-Myers 2011):

   K = 2*pi * integral_B d^{d-1}x * (R^2 - r^2)/(2R) * T_00(x)

   where r is the distance from the center. In the small-ball limit:

   delta S_mat = delta <K> = (Omega_d * R^{d+2}) / (d(d+1)) * 2*pi * T_ab n^a n^b + ...

5. **Impose entanglement equilibrium (MVEH).** The MVEH states delta S = 0 for the vacuum. Therefore:

   delta S_UV + delta S_mat = 0

   eta * (Omega_d / d(d-1)) * (R_ab - R/(2d) g_ab) n^a n^b + (Omega_d / d(d+1)) * 2*pi * T_ab n^a n^b = 0

6. **Extract Einstein's equation.** Since this must hold for all n^a (all observers at p) and all p (all points), the tensor equation follows:

   R_ab - R/(2d) g_ab = -(2*pi / (eta * (d-1)/(d+1))) * T_ab

   Rewrite using G_ab = R_ab - (1/2) R g_ab and absorbing the trace into a cosmological constant Lambda:

   G_ab + Lambda g_ab = (8*pi*G) * T_ab

   with G = 1/(4*eta) and Lambda an undetermined integration constant (from the trace freedom).

**Known difficulties at each step:**

- Step 1: The "geodesic ball" and "causal diamond" do not exist on the lattice. This step requires the continuum limit to be taken first, or argued to emerge at long wavelengths.
- Step 2: The UV/IR decomposition is conceptually clean in the continuum but on the lattice, S_EE is finite and there is no clean separation. The decomposition must be argued to emerge in the continuum limit.
- Step 3: The Raychaudhuri equation requires a differentiable manifold. On the lattice, the geometric entropy variation must be argued to take this form in the continuum limit.
- Step 4: The modular Hamiltonian K for a ball in the LATTICE vacuum is NOT known in closed form. The Casini-Huerta-Myers formula applies to CFT vacuum only. Assumption A3 (modular Hamiltonian locality) from Phase 9 provides the physical motivation, but the exact form K = 2*pi * integral T_00 * (R^2-r^2)/(2R) is a continuum CFT result.
- Step 5: MVEH is the main open gap. Why should the self-modeling state maximize entanglement?
- Step 6: This step is algebraic and robust once steps 1-5 are established.

### Approach 2: Jacobson 1995 Thermodynamic Derivation (FALLBACK)

**What:** Use the original 1995 argument: delta Q = T dS at local Rindler horizons, where T is the Unruh temperature and dS = eta * dA.

**When to switch:** Only if the 2016 approach encounters a fundamental obstacle that the 1995 approach avoids (unlikely -- the 2016 version is strictly better for lattice systems).

**Tradeoffs:** The 1995 version requires explicit Rindler horizons and Unruh temperature, which do NOT exist on the lattice (Pitfall 8). The 2016 version replaces these with entanglement entropy and modular Hamiltonian, which DO exist on the lattice. The 1995 version is therefore WORSE for our purposes.

### Anti-Patterns to Avoid

- **Applying Jacobson directly to the finite lattice:** The Raychaudhuri equation, geodesic balls, and causal diamonds do not exist on a finite lattice. The derivation must go through the continuum limit. Do NOT write lattice analogs of the Raychaudhuri equation.
  - _Example:_ Writing "the lattice Raychaudhuri equation is..." is a red flag. There is no such thing.

- **Claiming MVEH is proven:** Phase 9 identified MVEH as an OPEN GAP. Do not claim it is established. Clearly state it as an assumption (possibly motivated by MaxEnt) and identify what self-modeling property would establish it.
  - _Example:_ "Since self-modeling states are special, they maximize entanglement" is hand-waving, not a derivation.

- **Confusing the entanglement first law with MVEH:** The entanglement first law delta S = delta <K> is an EXACT identity (Phase 9). MVEH is an ADDITIONAL assumption that delta S = 0 for the vacuum. These are logically independent.
  - _Example:_ "The entanglement first law gives delta S = 0" is wrong. It gives delta S = delta <K>, not delta S = 0.

- **Ignoring the conformal field restriction:** Jacobson 2016 proves the result rigorously ONLY for conformal fields. For nonconformal fields (which the lattice produces in the IR), a conjecture about the entropy variation is needed (Speranza 2016). State this honestly.

## Existing Results to Leverage

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
| --- | --- | --- | --- |
| Entanglement first law | delta S = delta <K_A>, K_A = -ln(rho_A) | Phase 9, Eq. 09-03.3 | Use directly. CITE Phase 9. Do not re-derive. |
| Area-law bounds | I <= 2*beta*\|bd\|*\|J\|, S <= log(n)*\|bd\|, delta S ~ O(\|bd\|) | Phase 9, Eqs. 09-03.7a-c | Use as inputs to Jacobson. CITE Phase 9. |
| Lieb-Robinson velocity | v_LR = 8eJ/(e-1) on Z^1 | Phase 8, Eq. 08-03.3 | Use as emergent speed of light. CITE Phase 8. |
| Self-modeling Hamiltonian | h_xy = JF (SWAP) | Phase 8 | Use as the UV Hamiltonian. Do not re-derive. |
| Jacobson 2016 derivation | G_ab + Lambda g_ab = (8 pi G) T_ab from delta S = 0 for conformal fields | PRL 116, 201101 | Reproduce the derivation steps adapted to self-modeling context. CITE Jacobson. |
| Casini-Huerta-Myers modular Hamiltonian | K = 2*pi * integral (R^2-r^2)/(2R) * T_00 for ball in CFT vacuum | JHEP 1105:036, arXiv:1102.0440 | Use for the matter entropy variation. CITE CHM. |
| Raychaudhuri equation | d(theta)/d(lambda) = -(theta^2)/(D-2) - sigma^2 - R_ab k^a k^b | Wald Ch. 9, MTW | Use for geometric entropy variation. CITE Wald. |
| Bekenstein-Hawking entropy | S_BH = A/(4G) | Bekenstein 1973, Hawking 1975 | Identifies eta = 1/(4G). CITE standard reference. |

**Key insight:** The Jacobson derivation itself is established and well-tested. The novel work in Phase 10 is NOT re-deriving the Einstein equation from entanglement -- it is verifying/arguing that the self-modeling lattice satisfies the INPUT CONDITIONS for Jacobson's argument (MVEH, area law, entanglement first law, continuum limit).

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
| --- | --- | --- | --- |
| Phase 9 Assumption A3 (modular Hamiltonian locality) | K_A concentrated near boundary | Phase 9, Eq. 09-03.4 | Physically motivated, not proven for self-modeling |
| Bisognano-Wichmann theorem | K = 2*pi * boost generator for Rindler wedge | BW 1975/76 | Exact for QFT vacuum restricted to half-space |
| Lattice Bisognano-Wichmann ansatz | Approximate entanglement Hamiltonian for lattice systems | Giudici et al. 2018; Dalmonte et al. 2022 | Approximate; becomes exact in continuum limit |
| WVCH thermal area law | I(A:B) <= 2*beta*\|bd\|*\|J\| | Wolf et al. 2008 | Thermal states of local Hamiltonians |
| Jacobson 2012 entropy = entanglement entropy argument | S_BH = S_EE (horizon entropy IS entanglement entropy) | arXiv:1204.6349 | UV physics renders S_EE finite; G = 1/(4*eta) |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| --- | --- | --- | --- | --- |
| Entanglement Equilibrium and the Einstein Equation | Jacobson | 2016 | PRIMARY: the derivation template | Full derivation structure, MVEH statement, conformal restriction |
| Thermodynamics of Spacetime | Jacobson | 1995 | Historical context; original thermodynamic route | Clausius relation approach (contrast with 2016 version) |
| Gravitation and Vacuum Entanglement Entropy | Jacobson | 2012 | G = 1/(4*eta) identification; UV/IR decomposition rationale | Entropy density eta, UV divergence argument |
| Gravitational Dynamics from Entanglement Thermodynamics | Lashkari, McDermott, Van Raamsdonk | 2014 | Validates entanglement first law => Einstein in holographic context | Independent confirmation of the approach |
| Towards a Derivation of Holographic Entanglement Entropy | Casini, Huerta, Myers | 2011 | Modular Hamiltonian for ball in CFT | Exact K formula used in step 4 |
| Comments on Jacobson's Entanglement Equilibrium | Casini, Huerta, Myers | 2016 | Critique/refinement of Jacobson 2016 | Potential issues with nonconformal fields |
| Entanglement Entropy of Excited States in CPT | Speranza | 2016 | Nonconformal field corrections to delta S | R^{2*Delta} corrections for relevant deformations |
| Space from Hilbert Space | Cao, Carroll, Michalakis | 2017 | Emergent geometry from entanglement, spatial Einstein analog | Consistency check for emergent curvature |

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
| --- | --- | --- | --- |
| SymPy | sympy.diffgeom | Symbolic tensor algebra, Christoffel symbols, Riemann tensor | Standard CAS with differential geometry module |
| NumPy/SciPy | numpy, scipy.linalg | Exact diagonalization for small lattice checks | Standard numerical library |

### Supporting Tools

| Tool | Purpose | When to Use |
| --- | --- | --- |
| matplotlib | Visualization of entropy scaling | If numerical verification of area law in small causal diamond analog |
| QuTiP | Partial trace, entanglement entropy | If computing entanglement on small lattice to verify entanglement equilibrium numerically |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
| --- | --- | --- |
| SymPy diffgeom | xAct (Mathematica) | xAct is more powerful for GR tensor calculations but requires Mathematica license |
| Hand derivation | Cadabra | Cadabra handles index notation natively but adds tool dependency |

### Computational Feasibility

| Computation | Estimated Cost | Bottleneck | Mitigation |
| --- | --- | --- | --- |
| Reproduce Jacobson derivation symbolically | ~1 hour human time | Tensor algebra bookkeeping | Use SymPy or hand-derive with careful index tracking |
| Small lattice entanglement equilibrium check | ~minutes (N <= 12 sites) | Hilbert space dimension 2^N | Use sparse matrices; restrict to N <= 16 |
| Modular Hamiltonian locality check | ~minutes (N <= 10 sites) | Computing K = -ln(rho_A) requires full diag | Restrict to small subsystems |

**Installation / Setup:**
```bash
# All tools already available from Phases 8-9. No new packages needed.
# pip install numpy scipy sympy matplotlib qutip  (if not already installed)
```

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| --- | --- | --- | --- |
| Dimensional analysis of G = 1/(4*eta) | Newton's constant has correct dimensions | [G] = [length]^{d-1} in natural units; [eta] = [length]^{-(d-1)} since S = eta * A | [G * eta] = dimensionless = 1/4. Consistent. |
| Trace of Einstein equation gives Lambda | Lambda is integration constant, not independently derived | Take g^{ab} of G_ab + Lambda g_ab = 8*pi*G T_ab | -R + d*Lambda = 8*pi*G T, giving Lambda in terms of R and T |
| Flat space limit | R_ab = 0, T_ab = 0 => vacuum solution | Set perturbations to zero | delta S_UV = 0 and delta S_mat = 0 independently. Consistent. |
| Sign check: positive mass -> attractive gravity | G > 0 with correct sign in Einstein equation | Verify eta > 0 (entropy density positive) => G = 1/(4*eta) > 0 | Positive Newton's constant. Correct. |
| Phase 9 entanglement first law recovery | delta S_mat = delta <K> reproduces known thermal first law | Set K = beta*H (thermal case) | delta S = beta * delta <H>. Standard thermodynamic first law. |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| --- | --- | --- | --- |
| Flat spacetime | R_abcd = 0 | G_ab = 0, T_ab = 0, Lambda = 0 consistent | Jacobson 2016 |
| Conformal field theory | Massless fields, d dimensions | Jacobson 2016 gives exact result | PRL 116, 201101 |
| Weak field (linearized gravity) | h_ab << 1 | Linearized Einstein: Box h_ab = -16*pi*G T_ab | Standard GR; LMVR 2014 |
| Spherical symmetry (Schwarzschild) | Static, vacuum, spherically symmetric | R_ab = 0 (Ricci flat) | Wald Ch. 6 |
| de Sitter | T_ab = 0, Lambda > 0 | G_ab + Lambda g_ab = 0 | Jacobson-Speranza 2019 |

### Numerical Validation

| Test | Method | Tolerance | Reference Value |
| --- | --- | --- | --- |
| Entanglement equilibrium on small lattice | Compute S(A) for lattice state perturbed away from self-modeling equilibrium; check delta S < 0 (maximum) | Qualitative: S decreases under perturbation | No literature value; novel check |
| Modular Hamiltonian locality (A3 verification) | Compute K_A = -ln(rho_A) for self-modeling ground state on N=8 chain; check matrix elements decay with distance from boundary | Exponential decay with distance | Peschel 2003 (free fermions); qualitative for interacting |
| Area-law coefficient | Compare S(A) for increasing A in self-modeling lattice | S(A) / \|boundary\| approximately constant | Phase 9 bounds as upper limits |

### Red Flags During Computation

- If delta S > 0 for perturbations of the self-modeling state away from equilibrium, MVEH fails for the self-modeling lattice. This does NOT kill the derivation -- it means MVEH is an additional assumption.
- If the modular Hamiltonian K_A has significant support far from the boundary (volume-extensive contributions), assumption A3 fails and delta S does not scale with boundary area. Backtrack to WVCH thermal route.
- If the continuum limit produces R^2 corrections comparable to the Einstein term at the lattice scale, the Wilsonian argument requires more careful treatment (higher-derivative gravity corrections).
- If the derived G_ab + Lambda g_ab = 8*pi*G T_ab has wrong signs (e.g., repulsive gravity), there is a sign error in the Raychaudhuri equation application (check metric convention).

## Common Pitfalls

### Pitfall 1: Conflating Lattice and Continuum

**What goes wrong:** Writing continuum equations (Raychaudhuri, geodesic balls, conformal Killing vectors) as if they apply on the finite lattice.
**Why it happens:** The Jacobson derivation is so clean in the continuum that it is tempting to apply it directly. But the lattice has no geodesics, no curvature, no diffeomorphisms.
**How to avoid:** Always state explicitly: "In the continuum limit, which we argue emerges at scales >> lattice spacing a, the following structure appears..." Never write lattice analogs of continuum geometric quantities.
**Warning signs:** "The lattice Ricci tensor" or "lattice Raychaudhuri equation."
**Recovery:** Rewrite in Wilsonian language: lattice is UV, continuum is IR, Jacobson operates in the IR.

### Pitfall 2: Claiming MVEH Is Derived Rather Than Assumed

**What goes wrong:** Asserting that the self-modeling lattice satisfies MVEH without proof.
**Why it happens:** Phase 9 established area-law entropy and the entanglement first law. It is tempting to conclude MVEH from these, but MVEH is a SEPARATE condition: it says the vacuum MAXIMIZES entanglement, not just that entanglement obeys an area law.
**How to avoid:** Clearly distinguish three logical levels: (1) S obeys area law (Phase 9), (2) delta S = delta <K> (Phase 9, exact), (3) delta S = 0 for vacuum (MVEH, NOT established). Present MVEH as assumption A5 and state what self-modeling property would establish it.
**Warning signs:** "Since the area law holds, MVEH follows" -- this is a non-sequitur.
**Recovery:** Reframe as conditional: "Given MVEH (or given that the self-modeling equilibrium state maximizes entanglement at fixed volume), Einstein's equations follow."

### Pitfall 3: Ignoring the Conformal Field Restriction

**What goes wrong:** Applying Jacobson 2016 as if it works for arbitrary quantum fields, when it rigorously holds only for conformal fields.
**Why it happens:** The self-modeling lattice produces an interacting (nonconformal) theory in the IR. Jacobson's rigorous result requires conformal invariance for the exact form of the modular Hamiltonian.
**How to avoid:** State the conformal restriction explicitly. Note Jacobson's conjecture that the result extends to nonconformal fields. Cite Speranza 2016 for corrections. Frame the self-modeling result as "following Jacobson's conjecture for nonconformal fields" or argue that the leading-order IR physics is approximately conformal at scales >> lattice spacing.
**Warning signs:** Using the CHM modular Hamiltonian formula without noting it applies only to CFT vacuum.
**Recovery:** Add a paragraph stating that the CHM formula is valid for conformal fields, and that extension to the self-modeling lattice requires either (a) the lattice producing an approximately conformal IR theory, or (b) Jacobson's conjecture for nonconformal fields.

### Pitfall 4: Sign Error in Raychaudhuri Equation

**What goes wrong:** Getting the wrong sign relation between area change and Ricci curvature, leading to repulsive gravity.
**Why it happens:** The Raychaudhuri equation has different sign conventions depending on whether theta is expansion or contraction, whether the metric is (+,-,-,-) or (-,+,+,+), and whether the congruence is past-directed or future-directed.
**How to avoid:** Use our convention (-,+,+,+) consistently. Check: positive mass (R_ab k^a k^b > 0 via NEC) causes focusing (d(theta)/d(lambda) < 0), which DECREASES the area (delta A < 0). Since S_UV = eta * A, this gives delta S_UV < 0. The matter contribution delta S_mat > 0 (positive energy increases modular energy). The equilibrium delta S = 0 then gives the correct sign in Einstein's equation.
**Warning signs:** Attractive matter producing negative curvature (should be positive). G < 0.
**Recovery:** Trace the sign through each step, comparing with Wald's treatment.

### Pitfall 5: Treating Lambda as Determined

**What goes wrong:** Claiming that the cosmological constant Lambda is predicted by the derivation.
**Why it happens:** In Jacobson's derivation, Lambda appears as an integration constant when converting from the traceless equation (R_ab - R/(2d) g_ab = ... T_ab) to the full Einstein equation (G_ab + Lambda g_ab = ...). Lambda is NOT determined.
**How to avoid:** State clearly that Lambda is an undetermined integration constant, analogous to how the cosmological constant problem is not solved by Jacobson's approach. The derivation determines the DYNAMICS (how curvature responds to matter) but not the VACUUM ENERGY.
**Warning signs:** "We derive Lambda = ..." or "The self-modeling lattice predicts Lambda."
**Recovery:** Restate that Lambda is free and represents the vacuum energy, which is not determined by this derivation.

## Level of Rigor

**Required for this phase:** Physicist's proof with clearly stated assumptions.

**Justification:** Jacobson's argument itself is at the physicist's proof level -- it uses the Raychaudhuri equation, entanglement first law, and MVEH as inputs without formal mathematical proof of each step's applicability. The novel contribution of Phase 10 is NOT a formal theorem but a physical argument connecting the self-modeling lattice to the conditions of Jacobson's derivation. The key requirement is that every assumption is EXPLICITLY STATED with its status (proven, motivated, or open gap).

**What this means concretely:**

- The Jacobson derivation steps should be followed carefully with sign checks and dimensional analysis at each step
- MVEH should be stated as an assumption (A5) with physical motivation, not claimed as proven
- The continuum limit should be framed as a Wilsonian argument, not rigorously constructed
- Each Jacobson input ((J1) area law, (J2) first law, (J3) MVEH) should have its status explicitly tracked (Phase 9 delivered (J1) and (J2); (J3) is the gap)
- The assumption register from Phase 9 (A1-A4) should be extended with any new assumptions

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| --- | --- | --- | --- |
| Jacobson 1995 (Clausius relation at Rindler horizons) | Jacobson 2016 (entanglement equilibrium, MVEH) | 2016 | Removes need for explicit Rindler horizons and Unruh temperature; uses entanglement entropy directly |
| Holographic entanglement gravity (FLM, LMVR) | Non-holographic entanglement gravity (Jacobson 2016) | 2016 | Does not require AdS/CFT; works in any dimension |
| Thermodynamic entropy S_BH = A/(4G) | Entanglement entropy S_EE = eta * A | ~2012 (Jacobson) | Identifies horizon entropy as entanglement entropy; removes need for classical horizon thermodynamics |
| Gap-based area law (Hastings 2007) | Gap-free area law routes (WVCH 2008, channel capacity) | 2008 | Area laws available without spectral gap |

**Superseded approaches to avoid:**

- **Jacobson 1995 directly on lattice:** The 1995 version requires Rindler horizons and Unruh temperature, which do not exist on a lattice. Jacobson 2016 is strictly superior for lattice applications because it uses entanglement entropy (well-defined on lattices) instead of thermodynamic entropy (requires a thermal state and horizon).
- **Deriving linearized Einstein from holographic entanglement first law (LMVR):** This requires AdS/CFT, which the self-modeling lattice does not provide. Jacobson 2016 achieves the FULL nonlinear equations without AdS/CFT.

## Open Questions

1. **Can MVEH be derived from self-modeling properties?**
   - What we know: MVEH is Jacobson's key hypothesis. For CFT, it is equivalent to Einstein's equation (i.e., it is as strong as the conclusion). For the self-modeling lattice, no derivation exists.
   - What's unclear: What property of self-modeling would force the entanglement entropy to be maximal? One candidate: the self-modeling fixed point IS the MaxEnt state (maximum entropy consistent with the self-modeling constraint), and MaxEnt states maximize entanglement by construction. But this needs verification.
   - Impact on this phase: If MVEH cannot be derived, Phase 10 presents a conditional result: "IF MVEH holds for the self-modeling state, THEN Einstein's equations follow." This is still a strong result but has an open assumption.
   - Recommendation: Present MVEH as assumption A5, motivate it via MaxEnt reasoning, and clearly state what would establish it. Identify this as the main gap for Paper 6.

2. **Is the self-modeling IR theory approximately conformal?**
   - What we know: The Heisenberg model (h_xy = JF for n=2) at the AFM critical point is described by SU(2)_1 WZW CFT in 1D. In higher dimensions, the IR theory is not conformal (Neel order / spontaneous symmetry breaking).
   - What's unclear: Whether Jacobson's conjecture for nonconformal fields (that the derivation goes through with corrections) applies.
   - Impact on this phase: If the IR theory is not conformal, the CHM modular Hamiltonian formula is approximate, and corrections of order (mass*R)^{2*Delta} appear.
   - Recommendation: State the conformal restriction. Argue that at scales >> lattice spacing but << curvature scale, the theory is approximately conformal (standard Wilsonian argument). Cite Speranza 2016 for correction estimates.

3. **How exactly does the lattice spacing map to Newton's constant?**
   - What we know: G = 1/(4*eta), and on the lattice S = eta * |boundary| with |boundary| counting boundary bonds. In the continuum, A_physical = |boundary| * a^{d-1} so eta_continuum = eta_lattice / a^{d-1}.
   - What's unclear: The precise numerical coefficient in G = a^{d-1} / (4 * eta_lattice). For the channel capacity route, eta_lattice <= log(n), giving G >= a^{d-1} / (4 log n).
   - Impact on this phase: This determines the scale at which gravity becomes strong (the Planck scale l_P ~ a * (eta_lattice)^{-1/(d-1)}).
   - Recommendation: Present the dimensional analysis mapping. Note that the lattice spacing a plays the role of the Planck length (up to factors of eta_lattice). Do not attempt to predict the numerical value of G.

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| --- | --- | --- | --- |
| Jacobson 2016 (MVEH cannot be motivated) | MVEH has no connection to self-modeling | Present MVEH as external assumption; focus on verifying (J1) and (J2) | Low: derivation still goes through, just with one more assumption |
| Conformal modular Hamiltonian (non-conformal IR) | Lattice produces massive excitations | Use Jacobson's conjecture for nonconformal fields; cite Speranza corrections | Low: add a paragraph on corrections |
| Continuum limit argument | No argument for smooth manifold at large scales | Use CCM emergent geometry as supporting evidence for smooth geometry | Medium: need to invoke Phase 12 results |
| Full Einstein equation (only linearized accessible) | Cannot go beyond first order | Present linearized result G_ab^{(1)} = 8*pi*G T_ab^{(1)} as main result | Low: linearized is already significant |

**Decision criteria:** If MVEH cannot be motivated from self-modeling, DO NOT abandon Phase 10. Instead, present the result as "Einstein's equations from area-law entanglement + MVEH" with the gap clearly identified. This is already a strong result: it shows the BRIDGE from self-modeling to GR, with MVEH as the single remaining gap. Jacobson himself treats MVEH as a hypothesis, not a theorem.

## Sources

### Primary (HIGH confidence)

- Jacobson (2016), "Entanglement Equilibrium and the Einstein Equation," PRL 116, 201101, [arXiv:1505.04753](https://arxiv.org/abs/1505.04753) -- THE primary derivation template
- Jacobson (1995), "Thermodynamics of Spacetime: The Einstein Equation of State," PRL 75, 1260, [arXiv:gr-qc/9504004](https://arxiv.org/abs/gr-qc/9504004) -- historical context, original argument
- Jacobson (2012), "Gravitation and Vacuum Entanglement Entropy," IJMPD 21, 1242006, [arXiv:1204.6349](https://arxiv.org/abs/1204.6349) -- G = 1/(4*eta), UV/IR decomposition
- Casini, Huerta, Myers (2011), "Towards a Derivation of Holographic Entanglement Entropy," JHEP 1105:036, [arXiv:1102.0440](https://arxiv.org/abs/1102.0440) -- exact modular Hamiltonian for ball in CFT
- Lashkari, McDermott, Van Raamsdonk (2014), "Gravitational Dynamics from Entanglement Thermodynamics," JHEP 1404:195, [arXiv:1308.3716](https://arxiv.org/abs/1308.3716) -- entanglement first law => linearized Einstein
- Wald (1984), "General Relativity," University of Chicago Press, Ch. 9 -- Raychaudhuri equation, null congruences
- Phase 9, this project, derivations/09-area-law-synthesis.md -- area-law synthesis, entanglement first law, assumption register
- Phase 8, this project, derivations/08-lr-self-modeling.md -- v_LR, self-modeling Hamiltonian, lattice definition

### Secondary (MEDIUM confidence)

- Casini, Huerta, Myers (2016), "Comments on Jacobson's Entanglement Equilibrium," JHEP 1603:194, [arXiv:1601.00528](https://arxiv.org/abs/1601.00528) -- critique/refinement of Jacobson 2016
- Speranza (2016), "Entanglement Entropy of Excited States in CPT and the Einstein Equation," JHEP 1604:105, [arXiv:1602.01380](https://arxiv.org/abs/1602.01380) -- nonconformal field corrections
- Cao, Carroll, Michalakis (2017), "Space from Hilbert Space," PRD 95, 024031, [arXiv:1606.08444](https://arxiv.org/abs/1606.08444) -- emergent geometry consistency check
- Bisognano, Wichmann (1975/1976), J. Math. Phys. 16, 985 and 17, 303 -- modular Hamiltonian = boost generator
- Blanco, Casini, Hung, Myers (2013), "Relative Entropy and Holography," JHEP 1308:060, [arXiv:1305.3182](https://arxiv.org/abs/1305.3182) -- entanglement first law in holographic context

### Tertiary (LOW confidence)

- Giudici et al. (2018), lattice Bisognano-Wichmann ansatz -- approximate entanglement Hamiltonian on lattice, needs validation
- Chirco, Liberati (2010), "Non-equilibrium Thermodynamics of Spacetime," [arXiv:0909.4194](https://arxiv.org/abs/0909.4194) -- f(R) gravity from non-equilibrium

## Caveats and Alternatives (Self-Critique)

**1. What assumption am I making that might be wrong?**
The biggest assumption is that the self-modeling lattice produces a smooth emergent spacetime in the continuum limit. This is the standard assumption in ALL lattice approaches to quantum gravity (lattice QCD, CDT, Regge calculus), but it has never been rigorously established for any approach, including ours. If the continuum limit does not exist or produces a non-Riemannian geometry, the Jacobson argument does not apply.

**2. What alternative approach did I dismiss too quickly?**
The CCM emergent geometry approach (Cao-Carroll-Michalakis 2017) derives a SPATIAL analog of Einstein's equation without requiring MVEH or the conformal field restriction. It could potentially replace the Jacobson route entirely for the spatial component. I dismissed it because it gives only spatial Einstein's equation (constraint equation), not the full spacetime dynamics. But for a first paper, the spatial constraint plus a physical argument for the dynamical equation might be sufficient.

**3. What limitation of my recommended method am I understating?**
The conformal field restriction is more serious than I initially present. The self-modeling Heisenberg lattice is NOT a conformal field theory (except at critical points in 1D). Jacobson's conjecture that the result extends to nonconformal fields is just that -- a conjecture. Speranza (2016) shows corrections of order R^{2*Delta} which could be significant. I recommend stating this limitation prominently rather than as a footnote.

**4. Is there a simpler method I overlooked?**
One could argue more directly: the entanglement first law + area-law delta S + identification of modular Hamiltonian with boost generator (in the continuum limit) directly gives the Clausius relation delta Q = T dS, which is Jacobson 1995's starting point. This avoids the MVEH entirely but requires the Unruh temperature, which has its own lattice problems (Pitfall 8). The MVEH route (Jacobson 2016) is cleaner for a lattice approach, but the 1995 route might be simpler if one is willing to assume the Unruh effect emerges in the continuum limit.

**5. Would a specialist disagree with my recommendation?**
A specialist in algebraic QFT might object that the Bisognano-Wichmann theorem (which underpins the modular Hamiltonian identification) applies to von Neumann algebras of type III, while finite lattice algebras are type I (matrix algebras). The type transition happens in the continuum limit, and one should be careful about which results survive. However, the lattice BW ansatz (Giudici et al.) suggests the leading behavior is captured correctly, so this is likely a subleading correction.

## Metadata

**Confidence breakdown:**

- Mathematical framework: HIGH -- Jacobson's derivation is well-established (30 years, PRL publication, >1000 citations across 1995+2016)
- Standard approaches: HIGH -- the approach (Jacobson 2016) is the standard modern route
- MVEH verification: LOW -- no prior work connects MVEH to lattice quantum systems; this is genuinely novel territory
- Computational tools: HIGH -- standard tools sufficient, minimal computation needed
- Validation strategies: MEDIUM -- known limits available for the continuum part; lattice validation of MVEH is novel
- Continuum limit: MEDIUM -- standard Wilsonian argument, but no rigorous proof

**Research date:** 2026-03-22
**Valid until:** Indefinite for the mathematical framework; Jacobson's result is well-established. Tool versions may change.
