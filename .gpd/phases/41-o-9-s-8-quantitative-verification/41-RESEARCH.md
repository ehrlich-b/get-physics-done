# Phase 41: O(9)/S^8 Quantitative Verification - Research

**Researched:** 2026-03-30
**Domain:** Condensed matter / nonlinear sigma models / spin-wave theory / entanglement Hamiltonians
**Confidence:** HIGH

## Summary

Phase 41 is a quantitative patch: replace all Heisenberg S=1/2 carry-forward numbers in derivation chain links (i)-(l) with O(9)/S^8-specific values. The v10.0 chain (Phase 40) flagged five model-specific quantities that do not carry forward from v9.0: spin-wave velocity c_s, Lieb-Robinson velocity v_LR, the ratio v_LR/c_s, the Spectral Recovery Fraction (SRF) for lattice-BW, and the Fisher metric numerical prefactors. All of these can be computed analytically from the O(9) model parameters already established in Phases 38-39: rho_s = J/8, chi_perp = 1/(2Jz), 2-site spectrum with ||H_ij|| = 9J/4, and 8 Type-A Goldstone modes with linear dispersion.

The key results are: (1) c_s is obtainable analytically from the hydrodynamic relation c_s = sqrt(rho_s / chi_perp), using the known rho_s = J/8 and chi_perp computable from classical spin-wave theory for the O(9) model; (2) v_LR follows from the Nachtergaele-Sims bound applied to H_eff with interaction norm ||h_ij|| determined by the 2-site spectrum; (3) SRF is structurally model-independent (the lattice-BW ansatz depends only on Lorentz invariance of the low-energy theory, not on the specific sigma model), so the SRF argument carries over with only c_s replaced; (4) the Fisher metric structure (CORR-03 theorem) is model-independent, with the O(9) model having 8 massless modes producing the same r^{-(d-2)} decay as O(3) but with modified numerical prefactors proportional to 1/rho_s.

No QMC data exists for O(9) lattice models. All computations are analytical (spin-wave theory + known lattice integrals). This is appropriate because the goal is replacing Heisenberg-specific numbers, not achieving QMC-level precision.

**Primary recommendation:** Compute c_s analytically from c_s^2 = rho_s/chi_perp with classical spin-wave formulas for O(N=9), then update all downstream quantities (v_LR, emergent metric, lattice-BW prefactor) by substitution. State the lattice-BW SRF universality argument explicitly rather than recomputing SRF numerically.

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| --- | --- | --- | --- | --- |
| derivations/40-derivation-chain.md | prior artifact | Contains the carry-forward caveat at links (i)-(l) that this phase resolves | Update links (i)-(l) with O(9) numbers | plan, execution, verification |
| derivations/39-sigma-model.md | prior artifact | Provides rho_s = J/8, g^2 = 8T/J, sigma model action | Read and cite | plan, execution |
| derivations/39-goldstone-modes.md | prior artifact | 8 Type-A Goldstones, rho_ab = 0, c_s = c_s|k| dispersion | Read and cite | plan, execution |
| derivations/38-lattice-and-symmetry.md | prior artifact | 2-site spectrum E/J = {-7/4,...,9/4}, Spin(9) symmetry, H_eff form | Read for interaction norm | plan, execution |
| derivations/34-velocity-hierarchy-and-causal-structure.md | method template | Structure of the velocity hierarchy argument for Heisenberg; replicate for O(9) | Follow same argument structure | plan, execution |
| derivations/35-bw-axioms-and-lattice-bw.md | method template | Lattice-BW ansatz structure and SRF definition; replicate for O(9) | Follow same structure, substitute c_s | plan, execution |
| derivations/33-fisher-smoothness-algebraic-decay.md | method template | CORR-03 conditional theorem structure; verify it applies to O(9) | Verify hypotheses H1-H4 for O(9) | plan, execution |
| Giudici et al., PRB 98, 134403 (2018) | benchmark | Lattice-BW validated across universality classes (Ising, Potts, XXZ, LL) | Cite as evidence for model-independence of BW ansatz | execution, verification |
| arXiv:2511.00950 | benchmark | LBW ansatz works beyond Lorentz-invariant cases; universality validated in 2D QMC | Cite as additional evidence | execution |
| Nachtergaele-Sims, CMP 265, 119 (2006) | method | Lieb-Robinson bound with explicit velocity formula | Apply to H_eff | execution |
| Sandvik, arXiv:2601.20189 (2025) | benchmark | QMC values for Heisenberg (to be replaced, not carried forward) | Reference for comparison only | execution |

**Missing or weak anchors:** No QMC data exists for O(9) lattice models. The spin-wave velocity c_s will be computed analytically only, without the QMC calibration available for O(3). This is an honest limitation. The classical spin-wave result should be accurate at leading order but lacks the 1/S quantum corrections that shift the Heisenberg value from the classical prediction (2.0 Ja for O(3) on Z^2) to the QMC value 1.659 Ja -- quantum fluctuations reduce rho_s from J/2 to 0.181J and chi_perp from 1/(8J) to 0.0657/J, with the net effect on c_s being a ~17% reduction.

## Conventions

| Choice | Convention | Alternatives | Source |
| --- | --- | --- | --- |
| Unit system | Natural: hbar = 1, k_B = 1, a = 1 | SI | Project convention lock |
| Clifford algebra | Cl(9,0), {T_a, T_b} = (1/2) delta_{ab} I_{16} | Cl(0,9) | Phase 38 |
| Coupling sign | J > 0; H_eff = J sum T_a^(i) T_a^(j) | J < 0 | Phase 38 convention |
| Metric signature | (-,+,+,+) for emergent Lorentzian | (+,-,-,-) | Project convention lock |
| Sigma model normalization | S = (rho_s/2) int (d_mu n)^2 | S = (1/2g^2) int g_ij d_mu phi^i d_mu phi^j | Phase 39 |
| Lattice-BW ansatz | H_ent = (2pi/c_s) sum x_perp h_x | -- | Phase 35, Giudici et al. 2018 |
| Modular Hamiltonian | K_A = -ln(rho_A) (positive operator) | K_A = +ln(rho_A) | Project convention |

**CRITICAL: All equations and results below use these conventions. The O(9) model has an effective FERROMAGNETIC ground state (aligned T_a vectors), but the Hamiltonian convention uses J > 0 with the minus sign in H = -J sum n_i . n_j absorbed. The sigma model is written with the standard positive-definite action.**

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in This Phase |
| --- | --- | --- | --- |
| c_s^2 = rho_s / chi_perp | Hydrodynamic spin-wave velocity | Standard; Chaikin-Lubensky Ch. 6 | PRIMARY: compute c_s for O(9) |
| rho_s = J/(N-1) = J/8 | Classical O(N) spin stiffness | Phase 39, Section 2.4 | INPUT: known from Phase 39 |
| chi_perp = 1/(2Jz) for classical O(N) at T=0 | Transverse susceptibility (mean-field/classical) | Standard spin-wave theory | INPUT: derive for O(9) on Z^d |
| v_LR = 2e ||h|| z / mu | Nachtergaele-Sims LR bound | CMP 265, 119 (2006) | Compute v_LR for H_eff |
| H_ent = (2pi/c_s) sum_x x_perp h_x | Lattice-BW ansatz | Giudici et al. 2018 | Substitute O(9) c_s |
| ds^2 = -c_s^2 dt^2 + g_ij dx^i dx^j | Emergent spacetime metric | Phase 34, Eq. (34.9) | Substitute O(9) c_s |
| g_F(x) = O(m_s^2) > 0 | Fisher metric smoothness (CORR-03) | Phase 33, Eq. (33.19) | Verify H1-H4 for O(9) |
| C(r) ~ Gamma(d/2-1)/(4pi^{d/2} rho_s r^{d-2}) | Goldstone propagator correlation | Standard sigma model | O(9) with rho_s = J/8 |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --- | --- | --- | --- |
| Classical spin-wave expansion for O(N) | Determines chi_perp from the quadratic fluctuation spectrum around ordered state | Computing c_s | Chaikin-Lubensky; Altland-Simons Ch. 2 |
| Nachtergaele-Sims LR bound | Gives rigorous upper bound on information propagation velocity | Computing v_LR | CMP 265, 119 (2006); arXiv:math-ph/0603064 |
| Universality class argument for lattice-BW | Shows SRF is determined by Lorentz invariance, not specific sigma model | SRF for O(9) | Giudici et al. PRB 98, 134403 (2018) |
| CORR-03 conditional theorem | Maps sigma model correlations to Fisher metric positivity | Fisher metric for O(9) | Phase 33 derivation |

### Approximation Schemes

| Approximation | Small Parameter | Regime of Validity | Error Estimate | Alternatives if Invalid |
| --- | --- | --- | --- | --- |
| Classical spin-wave theory | 1/S (quantum corrections) | Large S or leading-order estimate | O(1/S); for S_eff = 1/2 corrections are O(1) | No QMC exists; this is the best available |
| Leading-order sigma model | g^2 = 8T/J (coupling) | Low T, d >= 2 (ordered phase) | O(g^4) from next Friedan loop | Standard; well-controlled |
| Nachtergaele-Sims LR bound | None (rigorous bound) | Always valid | Bound is not tight; v_LR overestimates true propagation speed | Tighter bounds exist (arXiv:1908.03997) but require model-specific analysis |

## Standard Approaches

### Approach 1: Analytical Spin-Wave Theory + LR Bound (RECOMMENDED)

**What:** Compute all five model-specific quantities analytically from known O(9) model parameters (rho_s, spectrum, lattice structure) without numerical simulation.

**Why standard:** This is the standard approach for any O(N) sigma model on a lattice where the coupling and spectrum are known. The hydrodynamic relation c_s^2 = rho_s/chi_perp is a textbook result. The LR bound is a rigorous mathematical result.

**Track record:** Used universally in condensed matter for magnon velocity; LR bounds used in mathematical physics since 1972.

**Key steps:**

1. **Compute chi_perp for O(9) on Z^d (d=3).** The transverse susceptibility of the classical O(N) model at T=0 is chi_perp = S^2/(2JSz) for spin S on a z-coordinated lattice. For the classical model (S -> infinity limit), chi_perp = 1/(2Jz). For z = 2d = 6 (cubic lattice): chi_perp = 1/(12J). The key subtlety: the "effective spin" in the O(9) model is S_eff = 1/2 (from the 2-site ground state being in the vector representation, dim 9). However, for the CLASSICAL spin-wave velocity, use the classical formula with the unit-vector constraint |n| = 1 (no quantum corrections).

2. **Compute c_s from c_s^2 = rho_s / chi_perp.** With rho_s = J/8 and chi_perp for O(9): c_s = sqrt(J/8 / chi_perp). For the classical O(N) model on Z^d, this gives c_s = J * sqrt(2z/(N-1)). For N=9, d=3 (z=6): c_s = J * sqrt(12/8) = J * sqrt(3/2) = 1.225 Ja. For d=2 (z=4): c_s = J * sqrt(8/8) = J. Cross-check: for O(3) (N=3) on Z^2 (z=4): c_s = J * sqrt(8/2) = 2J, matching the known classical value.

3. **Compute v_LR from Nachtergaele-Sims bound.** For nearest-neighbor interactions with interaction norm ||h_ij||, the LR velocity is v_LR = 2e * ||h_ij|| * z / mu for optimal mu. The interaction norm for H_eff is ||h_ij|| = max eigenvalue of H_{2-site} = 9J/4. Then v_LR scales as O(eJz).

4. **Compute v_LR/c_s ratio.**

5. **State lattice-BW SRF universality argument.** The lattice-BW entanglement Hamiltonian H_ent = (2pi/c_s) sum x_perp h_x is structurally model-independent: it depends only on the Lorentz invariance of the low-energy theory (Giudici et al. 2018 validated it across Ising, Potts, XXZ, Luttinger liquid universality classes). For the O(9) model, the low-energy theory is the O(9) NL sigma model, which IS Lorentz invariant (Phase 39). Therefore the BW ansatz applies with c_s replaced by the O(9) value. The SRF measures the fraction of K_A's weight in nearest-neighbor terms; this is determined by the ratio of lattice corrections to the BW leading term, which scales as O((a/L)^2) universally.

6. **State Fisher metric for O(9).** CORR-03 conditional theorem applies to any sigma model with LRO. For O(9) with 8 massless Goldstones: C(r) ~ Gamma(d/2-1) * (N-2) / (4 pi^{d/2} rho_s r^{d-2}), where the (N-2) = 7 factor counts the number of independent transverse fluctuation channels. The Fisher metric g_F = O(m_s^2) > 0 conditional on H1-H4.

7. **Assemble emergent metric.** ds^2 = -c_s^2 dt^2 + g_ij dx^i dx^j with O(9) c_s.

**Known difficulties at each step:**

- Step 1: The classical chi_perp for the O(9) model needs careful derivation. The formula chi_perp = 1/(2Jz) applies to the classical O(N) model with unit vectors. For the quantum model with S_eff = 1/2, quantum corrections are O(1). Since no QMC exists, we must use the classical value and state the limitation honestly.
- Step 3: The LR bound is not tight. v_LR overestimates the true group velocity by a factor that depends on model details. For the Heisenberg model, v_LR/c_s = 7.63; for O(9), a similar or larger ratio is expected (more degrees of freedom per site means the LR bound is looser relative to the physical velocity).

### Approach 2: Direct Spin-Wave Dispersion (ALTERNATIVE for c_s)

**What:** Compute the magnon dispersion omega(k) by linearizing the equations of motion around the ordered ground state of the O(9) lattice model. Read off c_s from omega = c_s |k| at small k.

**When to switch:** If the hydrodynamic formula gives ambiguous results or if the quantum corrections to chi_perp need better control.

**Tradeoffs:** More detailed but gives the same result at leading order. Requires explicit construction of the fluctuation matrix around the ordered state, which is a 8x8 matrix for 8 Goldstone modes.

### Anti-Patterns to Avoid

- **Carrying forward Heisenberg numbers:** c_s = 1.659 Ja, rho_s = 0.181 J, chi_perp = 0.0657/J are all specific to the S=1/2 Heisenberg model with O(3) symmetry. The O(9) model has DIFFERENT values. The entire point of this phase is the replacement.
- **Claiming QMC precision without QMC:** No QMC data exists for O(9). State that c_s is computed at leading spin-wave order (classical approximation) and give the classical value, not a QMC-calibrated value.
- **Confusing classical and quantum spin-wave velocities:** For O(3) on Z^2, the classical (unit-vector) spin-wave theory gives c_s,classical = 2.0 Ja (from rho_s = J/2, chi_perp = 1/(8J)), while the QMC value for S=1/2 is c_s = 1.659 Ja -- quantum corrections reduce c_s by ~17%. For O(9) on Z^3, the classical formula gives c_s = sqrt(3/2) Ja = 1.225 Ja; the unknown quantum corrections may shift this by a comparable fraction. Report the classical value and flag this limitation honestly.
- **Recomputing SRF numerically for O(9):** Unnecessary. The SRF is a measure of how well the lattice-BW ansatz reproduces K_A. Giudici et al. showed this works across universality classes. State the universality argument instead.

## Existing Results to Leverage

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
| --- | --- | --- | --- |
| rho_s = J/8 for O(9) | rho_s = J/(N-1), N=9 | Phase 39, Section 2.4 | Direct input to c_s computation |
| 2-site spectrum | E/J = {-7/4, -3/4, 1/4, 5/4, 9/4}, mult = {9, 84, 126, 36, 1} | Phase 38 | ||h_ij|| = 9J/4 for LR bound |
| 8 Type-A Goldstones | n_A = 8, n_B = 0, omega = c_s|k| | Phase 39 | Goldstone count and dispersion type |
| Spin(9) -> Spin(8) SSB | Coset S^8, dim 8 | Phase 39 | Sigma model target, N=9 in O(N) formulas |
| Friedan beta function | mu dg^2/dmu = -(d-2)g^2 + (7/2pi)g^4 | Phase 39, Eq. 39.8 | AF verified; no need to recompute |
| Lattice-BW universality | BW ansatz validated for Ising, Potts, XXZ, Luttinger liquid classes | Giudici et al. PRB 98, 134403 (2018) | Universality argument for O(9) |
| CORR-03 conditional theorem | g_F(x) = O(m_s^2) > 0, conditional on H1-H4 | Phase 33, Eq. (33.19) | Apply to O(9) sigma model |
| Emergent Lorentz structure | Four independent arguments from Phase 34 | Phase 34 derivation | Same arguments apply to O(9) with c_s replaced |

**Key insight:** The Phases 32-35 results have a structural component (theorem statements, argument structure) that is model-independent, and a quantitative component (specific numbers) that is model-specific. Phase 41 replaces only the quantitative component while confirming the structural component carries over.

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
| --- | --- | --- | --- |
| chi_perp = 1/(2Jz) for classical O(N) | Transverse susceptibility at T=0 | Standard spin-wave theory (Chaikin-Lubensky) | Classical limit; quantum corrections at O(1/S) |
| v_LR = C * ||h|| * z for NN interactions | LR velocity upper bound | Nachtergaele-Sims 2006 | Always valid; bound is not tight |
| Watson integral I_3 = (6 - pi^2/3)/(2pi^2) | Lattice sum for Z^3 infrared bound | DLS 1978 | Universal for Z^3 |
| C(r) ~ 1/(rho_s * r^{d-2}) at large r | Goldstone correlator decay | Standard sigma model | Ordered phase, T=0 |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| --- | --- | --- | --- | --- |
| Giudici et al., PRB 98, 134403 | Giudici, Giudice, Valli, Pollet, Dalmonte | 2018 | Lattice-BW validated across universality classes | SRF universality argument |
| arXiv:2511.00950 | (LBW beyond Lorentz invariance) | 2025 | LBW works even beyond Lorentz-invariant cases | Strengthens universality argument |
| Nachtergaele-Sims, CMP 265, 119 | Nachtergaele, Sims | 2006 | LR bound explicit formula | v_LR computation |
| arXiv:1004.2086 | Nachtergaele, Sims, Young | 2010 | LR bounds review | Explicit bound formulas for general lattices |
| Sandvik, arXiv:2601.20189 | Sandvik | 2025 | QMC precision for O(3) S=1/2 | Comparison only; these numbers are REPLACED |
| Hasenbusch & Vicari, JSTAT | Hasenbusch, Vicari | 2011 | O(N) critical exponents, cubic anisotropy | UC3 verification for O(9) |
| Chakravarty-Halperin-Nelson, PRB 39, 2344 | Chakravarty, Halperin, Nelson | 1989 | O(3) quantum NL sigma model renormalization | Structure of quantum corrections to c_s |

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
| --- | --- | --- | --- |
| Python 3 + NumPy | numpy >= 2.4 | Numerical computation of c_s, v_LR | Already in project |
| SciPy | scipy >= 1.17 | Sparse eigensolvers if needed | Already in project |
| Existing code: effective_hamiltonian.py | Phase 38 | T_a generators, 2-site spectrum | Provides ||h_ij|| directly |
| Existing code: octonion_algebra.py | Phase 28+ | Octonion and Clifford algebra infrastructure | Foundation for T_a operators |

### Supporting Tools

| Tool | Purpose | When to Use |
| --- | --- | --- |
| SymPy | Symbolic verification of spin-wave dispersion | Cross-check analytical formulas |
| matplotlib | Plotting dispersion relation if needed | Optional visualization |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
| --- | --- | --- |
| Analytical c_s (classical) | QMC for O(9) | QMC would give quantum-corrected value but no O(9) QMC code exists; would be a multi-month project |
| Nachtergaele-Sims LR bound | Tighter model-specific bounds (arXiv:1908.03997) | Tighter bounds require detailed analysis of the O(9) Hamiltonian structure; NS bound is sufficient for the velocity hierarchy argument |

### Computational Feasibility

| Computation | Estimated Cost | Bottleneck | Mitigation |
| --- | --- | --- | --- |
| Analytical c_s from spin-wave theory | Minutes (pen and paper) | None | Straightforward calculation |
| v_LR from NS bound | Minutes (pen and paper + verification script) | None | Apply standard formula |
| Fisher metric argument | Minutes (verify CORR-03 hypotheses) | None | Structural argument, no numerics |
| Updated derivation chain text | ~1 hour writing | Clear documentation | Follow Phase 34-35 template |

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| --- | --- | --- | --- |
| Dimensional analysis of c_s | Units correct | [c_s] = [sqrt(rho_s/chi_perp)] = [sqrt(J * J)] = [J] = [velocity] (a=1) | c_s has units Ja |
| v_LR > c_s | Velocity hierarchy | Compare numerical values | Ratio O(1)-O(10), must be > 1 |
| c_s(O(9),classical) is O(1) Ja | Reasonable magnitude | c_s(O(9)) on Z^3 vs O(3) on Z^2 | Classical c_s(O(9),d=3) = 1.225 Ja; classical c_s(O(3),d=2) = 2.0 Ja; both O(1) Ja as expected |
| N=3 recovery | O(3) limit | Set N=3 in O(N) formulas, compare with known Heisenberg CLASSICAL spin-wave velocity | Should match classical O(3) prediction (before quantum corrections) |
| Emergent metric positive-definite spatial part | Physical metric | g_ij = delta_ij in homogeneous case | Positive-definite for any c_s > 0 |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| --- | --- | --- | --- |
| O(3) classical spin-wave velocity on Z^2 | N=3, d=2 | c_s,classical = Ja * sqrt(2) * S * sqrt(d) ~ 1.0 Ja for S=1/2 | Standard; cf. QMC value 1.659 Ja |
| Large-N limit of O(N) | N -> infinity | c_s -> 0 as 1/sqrt(N) | rho_s ~ 1/N, chi_perp ~ const, so c_s ~ 1/sqrt(N) |
| rho_s = J/(N-1) | Classical O(N) | rho_s(O(9)) = J/8 = 0.125 J | Phase 39 |
| LR bound for Heisenberg | O(3), S=1/2, Z^1 | v_LR = 8eJ/(e-1) = 12.66 J | Phase 34, Eq. (34.2) |

### Numerical Validation

| Test | Method | Tolerance | Reference Value |
| --- | --- | --- | --- |
| 2-site spectrum check | Diagonalize H_2 with effective_hamiltonian.py | Exact | E/J = {-7/4, -3/4, 1/4, 5/4, 9/4} |
| Spin-wave dispersion at small k | Analytical: omega(k) = c_s |k| + O(k^3) | Exact at leading order | c_s from hydrodynamic formula |
| O(3) recovery of classical c_s | Set N=3 in formulas | Within 5% of known classical value | c_s,classical(O(3)) from spin-wave theory |

### Red Flags During Computation

- If c_s(O(9)) is not O(1) Ja: **SUSPICIOUS.** Both O(3) and O(9) have c_s = O(Ja) in the classical limit. If c_s << 0.1 Ja or c_s >> 10 Ja, recheck the formula.
- If v_LR < c_s: **PHYSICS ERROR.** The LR bound is a rigorous upper bound on ALL propagation, including the spin-wave velocity. v_LR >= c_s is a theorem.
- If chi_perp is negative: **ERROR.** Transverse susceptibility is positive-definite for a stable ordered phase.
- If c_s is imaginary: **ERROR.** Would indicate instability of the ordered state (negative chi_perp or negative rho_s), which contradicts the SSB proof from Phase 39.

## Common Pitfalls

### Pitfall 1: Confusing Classical and Quantum Spin-Wave Velocities

**What goes wrong:** For the S=1/2 Heisenberg AFM, the classical spin-wave value c_s,classical ~ 1.0 Ja differs from the QMC value c_s = 1.659 Ja by ~66%. Quantum corrections (1/S corrections in spin-wave theory) are large for small spin. Presenting the classical O(9) value as "the" c_s without flagging the quantum correction issue would be dishonest.

**Why it happens:** No QMC exists for O(9), so we have no quantum-corrected value.

**How to avoid:** Compute the classical value, state it clearly as the "classical spin-wave approximation," note the Heisenberg analogy where quantum corrections reduce c_s by ~17% (from 2.0 Ja classical to 1.659 Ja QMC for O(3) on Z^2), and acknowledge that the true O(9) quantum value is unknown.

**Warning signs:** Claiming a specific number as "the exact c_s for O(9)" without qualification.

**Recovery:** If the quantum correction is needed, one approach is the 1/S expansion, but for S_eff = 1/2 this is not controlled. The honest statement is: "c_s(O(9)) = c_s,classical * (1 + O(1) quantum corrections)."

### Pitfall 2: Wrong Interaction Norm for LR Bound

**What goes wrong:** The Nachtergaele-Sims bound uses ||h_ij|| = operator norm of the 2-site interaction. For H_eff = J sum T_a^(i) T_a^(j), the 2-site Hamiltonian H_2 = J sum_a T_a x T_a has spectrum E/J = {-7/4, -3/4, 1/4, 5/4, 9/4}. The operator norm is ||H_2|| = max(|E|) = 9J/4 (the largest absolute value eigenvalue). Using the wrong norm (e.g., the Frobenius norm, or missing the factor of J, or using the wrong eigenvalue) gives a wrong v_LR.

**Why it happens:** Multiple definitions of "norm" exist. LR bounds require operator norm = spectral radius.

**How to avoid:** Compute ||H_2|| = spectral radius = max |E_i| = 9J/4 from the known 2-site spectrum. Verify: the spectrum is {-7/4, -3/4, 1/4, 5/4, 9/4} * J, so the maximum absolute value is 9J/4.

**Warning signs:** v_LR that is orders of magnitude different from the O(3) value (they should be O(1) different since both are set by J and z).

**Recovery:** Re-check the 2-site spectrum and operator norm definition.

### Pitfall 3: Claiming SRF = 0.9993 for O(9)

**What goes wrong:** SRF = 0.9993 was computed numerically for the S=1/2 Heisenberg model on a specific lattice size. This number is model-specific and cannot be claimed for O(9) without computation. However, the STRUCTURAL argument (that SRF is close to 1 for any model whose low-energy theory is Lorentz invariant) DOES carry over.

**Why it happens:** Conflating the structural universality argument with the specific numerical value.

**How to avoid:** State: "The lattice-BW ansatz applies to the O(9) model because its low-energy theory (O(9) NL sigma model) is Lorentz invariant. Giudici et al. (2018) validated the ansatz across multiple universality classes. The SRF for O(9) has not been computed numerically, but the universality argument predicts SRF close to 1, with lattice corrections at O((a/L)^2)." Do NOT state SRF = 0.9993 for O(9).

**Warning signs:** Using the number 0.9993 in any context other than the Heisenberg model.

**Recovery:** Replace numerical claim with universality argument.

### Pitfall 4: Conflating Explicit and Spontaneous Breaking in c_s

**What goes wrong:** The full symmetry breaking is F_4 -> Spin(9) -> Spin(8). The sigma model describes only the SPONTANEOUS part: Spin(9) -> Spin(8) on S^8 with 8 Goldstone modes. The speed c_s is the velocity of these 8 modes, not of the 16 gapped modes from explicit F_4 -> Spin(9) breaking. Using the wrong mode count or the wrong coupling constant for the gapped modes would give the wrong c_s.

**Why it happens:** The derivation chain has two breaking stages that can be confused.

**How to avoid:** Always use N=9 (the order of the O(N) model on S^8), not N=17 (the total number of broken generators). The sigma model is O(9)/S^8, not F_4/Spin(9).

**Warning signs:** Using N=17 or dim(OP^2) = 16 anywhere in the sigma model computation.

**Recovery:** Recheck the SSB pattern from Phase 39.

## Level of Rigor

**Required for this phase:** Controlled approximation (analytical spin-wave theory) + rigorous bounds (LR velocity) + structural universality arguments (lattice-BW, Fisher metric)

**Justification:** This phase replaces specific numerical values in an established chain. The structural arguments were already derived in Phases 32-35 and validated by the Phase 40 assembly. The goal is accurate numbers, not new proofs. Classical spin-wave theory is appropriate for leading-order estimates when QMC is unavailable.

**What this means concretely:**

- c_s is computed at classical spin-wave order and flagged as such. No claim of QMC-level precision.
- v_LR is a rigorous upper bound (no approximation involved).
- SRF is stated as a universality argument with supporting evidence from Giudici et al., not as a computed number.
- Fisher metric is conditional on H1-H4 (same as in Phase 33); the conditionality is inherited, not new.
- All formulas include explicit dimensional analysis verification.

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| --- | --- | --- | --- |
| Heisenberg-specific numbers (v9.0) | Model-specific O(9) numbers (this phase) | This phase | Removes all carry-forward numbers |
| Single universality class validation of lattice-BW (Giudici 2018) | Multi-class validation + beyond-Lorentz extension (arXiv:2511.00950) | 2025 | Strengthens the SRF universality argument |

**Superseded approaches to avoid:**

- Using v9.0 Heisenberg numbers (c_s = 1.659 Ja, rho_s = 0.181 J) for O(9) -- this is the entire motivation for Phase 41
- Computing c_s from QMC for O(3) and calling it O(9) -- different universality class

## Open Questions

1. **Quantum corrections to c_s for O(9)**
   - What we know: Classical spin-wave theory gives c_s,classical. For O(3) S=1/2 on Z^2, quantum corrections reduce c_s by ~17% (from 2.0 Ja to 1.659 Ja).
   - What's unclear: The magnitude of quantum corrections for O(9) with S_eff = 1/2. The 1/S expansion is not controlled at S=1/2.
   - Impact on this phase: The classical c_s will be an approximation. The ratio v_LR/c_s will use this approximate c_s.
   - Recommendation: Compute the classical value, state it as a leading-order result, and note the quantum correction caveat. This is the best available without QMC.

2. **Lattice-BW SRF for O(9)**
   - What we know: SRF is close to 1 for all universality classes tested (Ising, Potts, XXZ, LL) by Giudici et al. The 2025 paper (arXiv:2511.00950) extends this beyond Lorentz-invariant cases.
   - What's unclear: The exact SRF for O(9). No one has computed it.
   - Impact on this phase: Cannot give a numerical SRF value.
   - Recommendation: State the universality argument, cite Giudici et al. and arXiv:2511.00950, and avoid claiming a specific SRF number.

3. **Tighter LR bound for H_eff**
   - What we know: The Nachtergaele-Sims bound is not tight. Improved bounds exist (arXiv:1908.03997) but require model-specific analysis.
   - What's unclear: How much tighter the bound can be made for the O(9) model.
   - Impact on this phase: v_LR may overestimate the true propagation speed. The velocity hierarchy v_LR > c_s still holds.
   - Recommendation: Use the NS bound (standard, rigorous, sufficient). Mention the possibility of tighter bounds as future work.

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| --- | --- | --- | --- |
| Classical chi_perp formula | Formula doesn't apply to quantum O(9) | Direct spin-wave dispersion calculation (diagonalize fluctuation matrix around ordered state) | Low: analytical computation on 8x8 matrix |
| NS LR bound gives unreasonable v_LR | Bound too loose for this model | Model-specific LR analysis using commutator growth | Medium: requires careful operator algebra |
| Universality argument for SRF | Referee objects to lack of numerical evidence | ED computation of entanglement Hamiltonian for small O(9) chain | High: requires implementing 16-dim-per-site ED for entanglement spectrum |

**Decision criteria:** The primary approach (analytical spin-wave + NS bound + universality argument) should succeed for all five quantities. Fallback is needed only if a reviewer demands numerical SRF evidence, which would require a separate computational phase.

## Detailed Formulas for Phase 41 Computations

### A. Spin-Wave Velocity c_s

For the classical O(N) model on Z^d with nearest-neighbor coupling J and lattice spacing a=1:

**Spin stiffness:**
rho_s = J/(N-1) = J/8 [Phase 39, established]

**Transverse susceptibility at T=0:**
For the classical O(N) model with ordered state n_0 = (1,0,...,0), the transverse susceptibility is the response to an infinitesimal uniform field h_perp in a transverse direction:

chi_perp = (d/dh_perp) <n_perp> |_{h=0}

For the nearest-neighbor O(N) model H = -J sum n_i . n_j on Z^d:
chi_perp = 1/(2Jz) at T=0 in the classical approximation

where z = 2d is the coordination number (z=6 for Z^3).

**Alternative derivation of chi_perp:** From the sum rule for the uniform transverse susceptibility and the spin-wave dispersion omega(k) = c_s |k|:
chi_perp = 1/V * sum_k 1/(2 * omega(k) * rho_s * k^2) * (integrated form gives chi_perp = S/(2Jz) for spin S)

For the CLASSICAL model (S -> inf limit normalized with |n|=1), chi_perp = 1/(2Jz).

**Hydrodynamic formula:**
c_s^2 = rho_s / chi_perp = (J/8) / (1/(2Jz)) = (J/8) * (2Jz) = J^2 * z / 4

For d=3 (z=6): c_s^2 = 6J^2/4 = 3J^2/2
c_s = J * sqrt(3/2) = J * 1.2247

For d=2 (z=4): c_s^2 = 4J^2/4 = J^2
c_s = J * 1.000

**Cross-check with O(N) spin-wave dispersion:** The spin-wave dispersion for the classical O(N) model on Z^d is:
omega(k) = 2JS * sqrt( (N-1)^{-1} * sum_mu (1-cos(k_mu)) * sum_nu (1-cos(k_nu)) ) ... [need the explicit form]

Actually, the simplest route: for O(N) model with H = -J sum n_i . n_j, the spin-wave Lagrangian for fluctuations pi_a (a=1,...,N-1) transverse to the ordered direction is:
L = (chi_perp/2) (d pi_a/dt)^2 - (rho_s/2) (nabla pi_a)^2

This gives dispersion omega^2 = (rho_s/chi_perp) |k|^2, confirming c_s^2 = rho_s/chi_perp.

**O(3) cross-check:**
For O(3) (N=3, the Heisenberg model) on Z^2 (z=4):
rho_s = J/(3-1) = J/2 [CLASSICAL value]
chi_perp = 1/(2*J*4) = 1/(8J)
c_s,classical = sqrt((J/2)/(1/(8J))) = sqrt(4J^2) = 2J [in units of a=1]

Wait, this gives c_s = 2J for classical O(3) on Z^2. The QMC value for quantum S=1/2 Heisenberg is c_s = 1.659 J. But the CLASSICAL spin stiffness rho_s = J/2 is MUCH larger than the quantum rho_s = 0.181 J. This is because quantum fluctuations strongly reduce rho_s (by factor ~3.6 for S=1/2).

So the formula rho_s = J/(N-1) is the CLASSICAL (T=0, S -> infinity normalized) value. For the quantum model, rho_s is renormalized. Phase 39 used rho_s = J/8 which is the CLASSICAL O(9) value. This is consistent.

**Important clarification:** The chi_perp = 1/(2Jz) is also the classical value. Both rho_s and chi_perp are classical. Their ratio gives the classical c_s. For the quantum model, both are renormalized, but the ratio may change differently. For O(3) S=1/2:
- rho_s goes from J/2 (classical) to 0.181J (quantum) -- factor 2.76 reduction
- chi_perp goes from 1/(8J) = 0.125/J (classical) to 0.0657/J (quantum) -- factor 1.90 reduction
- c_s goes from 2J (classical) to 1.659J (quantum) -- factor 1.21 reduction

So the classical c_s overestimates the quantum c_s by ~20% for O(3) S=1/2. For O(9), a similar overestimate is expected.

### B. Lieb-Robinson Velocity v_LR

The Nachtergaele-Sims bound for nearest-neighbor interactions (math-ph/0603064, Theorem 2.1):

||[A(t), B(0)]|| <= C * ||A|| * ||B|| * min(|X|,|Y|) * exp(-mu * (d(X,Y) - v_LR |t|))

where v_LR = 2 * ||Phi|| * z / mu for NN interactions, with ||Phi|| = max over bonds ||h_ij||, z = coordination number, and mu is optimized.

For the optimal mu (which gives the tightest bound), the LR velocity for NN interactions on Z^d is:
v_LR = 2e * ||h_ij|| * z (with numerical prefactors from the optimization)

For H_eff on Z^d: ||h_ij|| = spectral radius of the 2-site Hamiltonian = max(|E_i|).
From Phase 38: E/J = {-7/4, -3/4, 1/4, 5/4, 9/4}.
||h_ij|| = 9J/4 (the maximum absolute eigenvalue).

Alternatively, note that for the Heisenberg S=1/2 model: H_2 = J S_1.S_2 with spectrum {-3J/4, J/4}, so ||h_ij|| = 3J/4. And v_LR = 8eJ/(e-1) = 12.66 J (from code/lieb_robinson_benchmark.py).

v_LR(Heisenberg) = 8eJ/(e-1). With ||h_ij|| = 3J/4 and z=2 (1D chain used in Phase 34):
v_LR = 2e * (3J/4) * 2 = 3eJ = 8.15J ... This doesn't match 8eJ/(e-1) = 12.66J.

The exact formula depends on the specific form of the NS bound used. The Phase 8/34 computation used the specific NS formula for 1D NN interactions. For the general case, we need to use the same formula structure but with the O(9) interaction norm.

The key insight: v_LR scales linearly with ||h_ij|| for fixed lattice structure. Since both models live on Z^d with NN interactions, the ratio is:
v_LR(O(9)) / v_LR(Heis) = ||h_ij||(O(9)) / ||h_ij||(Heis) = (9J/4) / (3J/4) = 3

So v_LR(O(9)) = 3 * v_LR(Heis) for the same lattice.

For Z^1: v_LR(O(9)) = 3 * 12.66 J = 37.98 J
For Z^3: needs the z-dependence from the NS formula.

### C. Lattice-BW Structural Argument

The lattice-BW entanglement Hamiltonian H_ent = (2pi/c_s) sum_x x_perp h_x depends on:
1. The emergent Lorentz invariance of the low-energy theory (established for O(9) NL sigma model, Phase 39)
2. The spin-wave velocity c_s (to be computed in this phase)
3. The local Hamiltonian density h_x (known: h_x = J sum_a T_a^(i) T_a^(j) for the bond at x)

The SRF universality argument: Giudici et al. (2018) showed the BW ansatz works for Ising (Z_2), Potts (Z_q), XXZ (U(1)), and Luttinger liquid (CFT) universality classes -- a diverse set covering discrete and continuous symmetries, gapped and gapless phases. The O(9) model with continuous Spin(9) symmetry and gapless Goldstone modes falls squarely within this framework. The 2025 paper (arXiv:2511.00950) further extends the validity beyond Lorentz-invariant cases.

## Sources

### Primary (HIGH confidence)

- Nachtergaele, Sims, CMP 265, 119 (2006); arXiv:math-ph/0603064 -- Lieb-Robinson bounds with explicit formulas
- Giudici, Giudice, Valli, Pollet, Dalmonte, PRB 98, 134403 (2018); arXiv:1807.01322 -- Lattice-BW across universality classes
- Chaikin & Lubensky, "Principles of Condensed Matter Physics," Ch. 6 -- Spin-wave theory, hydrodynamic relation c_s^2 = rho_s/chi_perp
- Altland & Simons, "Condensed Matter Field Theory," Ch. 2 -- O(N) sigma model, spin waves
- Phase 38 derivation (derivations/38-lattice-and-symmetry.md) -- 2-site spectrum
- Phase 39 derivation (derivations/39-sigma-model.md) -- rho_s = J/8, sigma model
- Phase 39 derivation (derivations/39-goldstone-modes.md) -- 8 Type-A Goldstones
- Phase 34 derivation (derivations/34-velocity-hierarchy-and-causal-structure.md) -- Velocity hierarchy structure
- Phase 35 derivation (derivations/35-bw-axioms-and-lattice-bw.md) -- Lattice-BW structure

### Secondary (MEDIUM confidence)

- arXiv:2511.00950 -- LBW ansatz beyond Lorentz invariance (2025, QMC study)
- arXiv:1908.03997 -- Tighter LR bounds
- arXiv:1004.2086 -- LR bounds review (Nachtergaele, Sims, Young)
- Chakravarty, Halperin, Nelson, PRB 39, 2344 (1989) -- Quantum NL sigma model for O(3) Heisenberg

### Tertiary (LOW confidence)

- Classical spin-wave formula chi_perp = 1/(2Jz) -- standard textbook result but needs verification for the specific O(9) model construction used here (Cl(9,0) spinors, not abstract O(9) vectors)
- Quantum correction estimate "~66% for O(3)" -- extrapolated from comparing classical vs QMC for Heisenberg; not directly applicable to O(9)

## Metadata

**Confidence breakdown:**

- Mathematical framework: HIGH - The hydrodynamic relation, LR bounds, and lattice-BW are all well-established
- Standard approaches: HIGH - Spin-wave theory for O(N) models is textbook material
- Computational tools: HIGH - All tools are already in the project and no new packages needed
- Validation strategies: HIGH - Multiple cross-checks available (O(3) recovery, dimensional analysis, v_LR > c_s)

**Research date:** 2026-03-30
**Valid until:** Indefinitely for the analytical framework; would need updating only if QMC data for O(9) becomes available

## Caveats and Alternatives

### Self-Critique

1. **Assumption that may be wrong:** The chi_perp = 1/(2Jz) formula assumes the classical O(N) model at T=0 on Z^d. The actual O(9) model uses Cl(9,0) spinors in R^16 per site, not abstract O(9) vectors. The relationship between the lattice model H_eff = J sum T_a T_a and the classical O(N) model needs verification: specifically, whether the spin-wave expansion around the ordered state gives the same chi_perp as the abstract O(N) formula. Phase 39 established rho_s = J/8 = J/(N-1) for N=9, confirming the mapping at the level of spin stiffness. The same mapping should give chi_perp = 1/(2Jz), but this should be verified by direct calculation.

2. **Alternative approach dismissed:** One could compute c_s by direct spin-wave expansion: expand H_eff around the classical ground state (all spins aligned), compute the fluctuation matrix, and read off the dispersion. This would give the same result as the hydrodynamic formula at leading order but would provide a more direct connection to the microscopic Hamiltonian. Dismissed because it's more work for the same result, but it would be a good cross-check.

3. **Limitation understated:** The quantum corrections to c_s are genuinely unknown for O(9). For O(3) S=1/2 on Z^2, the classical c_s = 2.0 Ja overestimates the QMC value 1.659 Ja by ~20%. For O(9) with S_eff = 1/2, quantum corrections of similar or larger magnitude are expected but cannot be computed without QMC or a controlled 1/S expansion.

4. **Simpler method overlooked?** No. The hydrodynamic relation is already the simplest method for computing c_s given rho_s and chi_perp.

5. **Would a specialist disagree?** A condensed matter theorist might insist on QMC verification of c_s, which is standard practice for quantum magnets. We cannot provide this for O(9). A mathematical physicist might object to using the LR bound for a system where the bound is known to be loose. Both objections are valid but do not have solutions within the scope of Phase 41.
