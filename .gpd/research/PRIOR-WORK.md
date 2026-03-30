# Prior Work: Information-Geometric Continuum Limit from Finite-Dimensional Observer

**Surveyed:** 2026-03-29
**Domain:** Quantum information geometry / Quantum lattice systems / Emergent spacetime
**Confidence:** MEDIUM

This document covers prior work relevant to closing Paper 6 Gap 1 (continuum limit) via the chain: finite-dim observer + SWAP lattice + exponential decay -> smooth Fisher manifold -> emergent Lorentz -> BW + equilibrium -> Jacobson -> Einstein. It does NOT re-cover established results from Papers 5-6 (self-modeling forces M_n(C)^sa, SWAP lattice, area law, Jacobson route) or v3.0 (Nachtergaele-Sims LR bound, ED benchmarks). Those are treated as validated inputs.

---

## Key Results

| Result | Expression / Value | Conditions | Source | Year | Confidence |
|--------|-------------------|------------|--------|------|------------|
| Hastings-Koma exponential clustering | Spectral gap gamma > 0 implies \|<A B> - <A><B>\| <= C \|A\| \|B\| exp(-d(A,B)/xi), xi = O(v_LR/gamma) | Short-range interactions, any d, wide class of lattices | Hastings-Koma, arXiv:math-ph/0507008 | 2006 | HIGH |
| Nachtergaele-Sims LR bound (general) | \|[A(t),B]\| <= C min(\|A\|,\|B\|) exp(-a(d(X,Y) - v_LR\|t\|)) | Finite-range or exponentially decaying interactions | Nachtergaele-Sims, arXiv:math-ph/0506030 | 2006 | HIGH |
| QFI = 4 x Bures metric (regular case) | g_ij^F(theta) = 4 g_ij^Bures(theta) for full-rank rho(theta) | rho(theta) full rank; breaks at rank changes | Zhou-Jiang, arXiv:1910.08473; Safranek arXiv:1612.04581 | 2017-2019 | HIGH |
| Morozova-Cencov-Petz classification | Quantum monotone metrics form a family parametrized by operator monotone functions f; not unique unlike classical case | Finite-dim quantum systems, CPTP contractivity | Petz, J. Math. Phys. 37 (1996); Morozova-Cencov (1991) | 1991-1996 | HIGH |
| Zanardi-Giorda-Cozzini: Fisher metric singularities = QPTs | Scalar curvature of Fisher metric on coupling-constant manifold diverges at quantum phase transitions | Ground state fidelity, finite systems, parameter manifold | Zanardi et al., arXiv:quant-ph/0701061 | 2007 | HIGH |
| BW theorem: modular Hamiltonian = boost generator | Delta^{it} = exp(2 pi i K t) where K is the Lorentz boost generator for wedge region | Wightman axioms satisfied, vacuum state, wedge region | Bisognano-Wichmann, J. Math. Phys. 16 (1975), 17 (1976) | 1975-76 | HIGH |
| Lattice BW: quantitative accuracy for Lorentz-invariant continuum limits | H_ent ~ sum_x x_perp h_x reproduces lattice entanglement spectra to within a few percent | Low-energy description is Lorentz-invariant QFT | Giudici et al., arXiv:1807.01322 | 2018 | HIGH |
| DLS: Neel order for d >= 3, S >= 1 | Spontaneous SU(2) -> U(1) breaking in ground state | Hypercubic lattice, T = 0, spin S >= 1 in d >= 3 or S >= 3/2 in d = 2 | Dyson-Lieb-Simon, J. Stat. Phys. 18 (1978) | 1978 | HIGH |
| SU(N) square lattice: Neel to VBS transition at N_c ~ 4.57 | Direct continuous QPT between Neel and VBS | Square lattice, singlet projector QMC | Kawashima-Tanabe, arXiv:0803.1529; Beach et al. PRB 80 (2009) | 2009 | MEDIUM-HIGH |
| von Ignatowsky: relativity principle alone -> Galilean or Lorentzian | Homogeneity + isotropy + relativity principle => either v_max = infinity (Galilean) or finite v_max (Lorentzian) | No light postulate needed; need group structure of boosts | Ignatowsky (1910); modern: Pal, arXiv:physics/0302045; Levy-Leblond (1976) | 1910/1976 | HIGH |
| Cao-Carroll-Michalakis: geometry from entanglement | Mutual information defines graph distance; MDS extracts spatial dimension and metric | Redundancy-constrained states with area-law entropy | Cao-Carroll-Michalakis, arXiv:1606.08444 | 2016 | MEDIUM-HIGH |
| AKLT: rigorous gap for VBS ground states | Spectral gap proven for spin-1 chain; exponential decay of correlations | AKLT point of spin-1 Heisenberg, 1D | Affleck-Kennedy-Lieb-Tasaki, CMP 115 (1988) | 1988 | HIGH |
| Jacobson: entanglement equilibrium -> Einstein equation | delta S_UV + delta S_mat = 0 at MSS vacuum implies G_ab + Lambda g_ab = 8 pi G T_ab | Smooth geometry assumed, conformal modular Hamiltonian, small geodesic ball | Jacobson, arXiv:1505.04753 | 2016 | HIGH |
| Connes-Rovelli thermal time | Modular flow of a faithful state defines a preferred time flow on the algebra | Type III von Neumann algebra, faithful normal state | Connes-Rovelli, CQG 11 (1994) | 1994 | HIGH |

---

## Foundational Work

### Hastings-Koma (2006) - Spectral Gap and Exponential Decay of Correlations

**Key contribution:** Proved rigorously that a nonvanishing spectral gap above the ground state implies exponential decay of connected correlation functions for quantum spin and fermion systems on a wide class of lattices in arbitrary spatial dimension. The correlation length is bounded as xi = O(v_LR / gamma) where v_LR is the Lieb-Robinson velocity and gamma is the spectral gap.

**Method:** Combined Fourier analysis with Lieb-Robinson bounds to control the propagation of correlations. For observables that anticommute at large distance, the bare correlation decays exponentially. For commuting observables, the connected correlation decays exponentially. For vector observables under U(1) symmetry, the bare correlation decays on lattices with self-similarity in D < 2.

**Limitations:** (1) Requires a spectral gap to exist -- does not prove the gap, only consequences of it. The SU(n) Heisenberg antiferromagnet on Z^d for d >= 2 is NOT known to be gapped (it almost certainly is NOT gapped due to Neel order and Goldstone modes). (2) The bound xi = O(v_LR/gamma) may not be tight. (3) Does not apply to gapless systems like the d=1 Heisenberg chain (which is in the SU(2)_1 WZW universality class).

**Critical implication for v9.0:** This theorem is the bridge between "spectral gap" and "smooth Fisher manifold." IF the relevant lattice system has a spectral gap, then correlations of reduced density matrices decay exponentially, which gives the Fisher metric on the space of reduced states a well-defined, smooth structure in the thermodynamic limit. The catch: the Heisenberg AFM in d >= 2 breaks SU(n), producing Goldstone modes and closing the gap. The v9.0 chain must either (a) work in a gapped phase (AKLT-like deformation or disordered phase at finite T), (b) show the Fisher manifold is smooth despite gaplessness (the Goldstone modes produce power-law decay but may still give a well-defined Fisher metric), or (c) use a different route to smoothness.

**Reference:** Hastings-Koma, "Spectral Gap and Exponential Decay of Correlations," CMP 265 (2006) 781-804, arXiv:math-ph/0507008

### Nachtergaele-Sims-Young (2019) - Quasi-Locality Bounds for Quantum Lattice Systems

**Key contribution:** Comprehensive framework unifying Lieb-Robinson bounds, quasi-local maps, and spectral flow automorphisms for quantum lattice systems. Provides the most modern and general formulation of LR bounds applicable to the SWAP Hamiltonian.

**Method:** Developed quasi-locality properties of general classes of maps on the algebra of local observables. Extended LR bounds to lattice fermion systems via conditional expectations onto CAR subalgebras. Established stability of gapped ground state phases for frustration-free models with Local Topological Quantum Order.

**Limitations:** The stability results apply to frustration-free models (LTQO). The SU(n) Heisenberg model on general lattices is NOT frustration-free (the SWAP Hamiltonian is, but only for the ferromagnetic sign; the antiferromagnetic sign is frustrated on non-bipartite lattices).

**Critical implication for v9.0:** Provides the mathematical infrastructure (LR bounds, quasi-local maps) needed to rigorously control the continuum limit. The LR velocity v_LR sets the "emergent speed of light." The v3.0 validated result v_LR = 8eJ/(e-1) for SWAP on Z^1 fits into this framework.

**Reference:** Nachtergaele-Sims-Young, J. Math. Phys. 60 (2019) 061101, arXiv:1810.02428

### Zanardi-Giorda-Cozzini (2007) - Information-Geometric Approach to Quantum Phase Transitions

**Key contribution:** Established that the Riemannian metric induced by quantum state fidelity on the manifold of coupling constants (the "fidelity susceptibility" or "quantum geometric tensor") has singularities precisely at quantum phase transitions. This is the foundational result connecting Fisher information geometry to quantum lattice physics.

**Method:** For a family of Hamiltonians H(lambda) parametrized by coupling constants lambda, the ground state |psi(lambda)> traces out a manifold. The pullback of the Fubini-Study metric to the parameter space gives the quantum Fisher information metric g_ij(lambda) = Re[<d_i psi | (1 - |psi><psi|) | d_j psi>]. The scalar curvature of this metric diverges at QPTs.

**Limitations:** (1) Applies to pure states (ground states). Extension to thermal/mixed states requires the Bures/SLD Fisher metric, which is more complex. (2) For gapless systems, the fidelity susceptibility diverges as a power law, not a simple singularity -- the metric is still defined but its curvature diverges. (3) Does not directly address the reduced density matrix manifold for a subregion.

**Critical implication for v9.0:** This is the closest prior work to the v9.0 approach. The v9.0 chain needs the Fisher metric on the manifold of REDUCED density matrices rho_A(x) as the lattice site x varies, not on the full parameter manifold. The reduced-state Fisher metric inherits smoothness from the exponential clustering property. Zanardi et al. provide the conceptual framework; v9.0 must extend it from parameter space to physical (lattice-position) space.

**Reference:** Zanardi-Giorda-Cozzini, Phys. Rev. Lett. 99 (2007) 100603, arXiv:quant-ph/0701061

### Bisognano-Wichmann (1975-76) - Modular Hamiltonian and Lorentz Boosts

**Key contribution:** In Wightman-axiomatic QFT, the Tomita-Takesaki modular operator Delta of the vacuum state restricted to a wedge-shaped region equals the unitary group generated by the Lorentz boost preserving that wedge: Delta^{it} = exp(2 pi i K t), where K is the boost generator. Equivalently, the modular Hamiltonian H_mod = -ln(rho_wedge) is proportional to the boost generator.

**Method:** Applies Tomita-Takesaki modular theory to the von Neumann algebra associated with a Rindler wedge. Uses the PCT theorem and spectral condition to identify modular conjugation J with the CRT operator and the modular flow with Lorentz boosts.

**Limitations:** (1) Requires Wightman axioms (Lorentz invariance is an INPUT, not derived). (2) Exact only for the vacuum in a wedge region; for other regions (balls, half-spaces) the modular Hamiltonian is typically non-local. (3) Does not apply to lattice systems directly -- it is a continuum QFT result.

**Critical implication for v9.0:** The BW theorem is the bridge between "emergent Lorentz invariance" and the Jacobson argument. If the lattice Fisher manifold is smooth and the continuum limit is Lorentz-invariant, then BW identifies the modular Hamiltonian with the boost generator, giving the thermal/Unruh temperature T = 1/(2 pi) needed for Jacobson's thermodynamic derivation of Einstein equations. The key question is whether BW-like structure emerges from the lattice without assuming Lorentz invariance as input.

**Reference:** Bisognano-Wichmann, J. Math. Phys. 16 (1975) 985; J. Math. Phys. 17 (1976) 303

### Giudici-Mendes-Santos-Dalmonte (2018) - Lattice BW Entanglement Hamiltonians

**Key contribution:** Demonstrated numerically that the Bisognano-Wichmann form of the entanglement Hamiltonian (H_ent ~ sum_x x_perp h_x, linearly weighted by distance from entangling surface) provides a quantitatively accurate description of lattice entanglement Hamiltonians whenever the low-energy physics is captured by a Lorentz-invariant QFT.

**Method:** Computed exact lattice entanglement Hamiltonians using DMRG, ED, and QMC for Ising, Potts, and Luttinger liquid models in 1D and 2D. Compared eigenvalues, eigenvectors, and correlation functions with the BW prediction.

**Limitations:** (1) Accuracy degrades when Lorentz invariance is not a good description (massive phases far from criticality). (2) Edge effects and finite-size corrections can be significant. (3) Does not constitute a proof that BW emerges -- it is numerical evidence.

**Critical implication for v9.0:** Provides strong numerical evidence that BW structure can emerge on the lattice without being assumed. If the SWAP lattice's continuum limit is Lorentz-invariant (which v9.0 aims to show via Fisher geometry + von Ignatowsky), the lattice BW result would apply. The 2025 QMC study (arXiv:2511.00950) extends this to show BW accuracy even beyond strict Lorentz invariance in some cases.

**Reference:** Giudici et al., Phys. Rev. B 98 (2018) 134403, arXiv:1807.01322

### Ignatowsky (1910) / Levy-Leblond (1976) - Relativity Without Light

**Key contribution:** Demonstrated that the principle of relativity (equivalence of inertial frames) combined with spatial isotropy, homogeneity, and group structure of boosts uniquely determines the transformation law to be either Galilean (v_max = infinity) or Lorentzian (finite v_max). No postulate about light is needed. The invariant speed v_max is a free parameter that must be determined empirically or from additional physics.

**Method:** Assumes boosts form a one-parameter group, spatial isotropy, and reciprocity (if S' moves at v relative to S, then S moves at -v relative to S'). Derives that the composition law must be either additive (Galilean) or the Lorentz addition formula with an undetermined parameter 1/V^2 where V is the invariant speed.

**Limitations:** (1) Does not determine the VALUE of the invariant speed -- only that one exists. (2) Requires the transformation to be continuous and to form a group. (3) Does not address the microscopic origin of why boosts should form a group at all.

**Critical implication for v9.0:** This is the key theorem connecting "emergent finite signal speed" (from Lieb-Robinson) to "emergent Lorentz symmetry." The v9.0 argument is: (a) LR bounds give finite v_LR, (b) the continuum limit inherits a finite maximum signal speed, (c) if the continuum limit also has spatial isotropy and translational invariance (from lattice symmetries), then von Ignatowsky forces the symmetry group to be either Galilean or Lorentzian, (d) the Galilean option is excluded because v_max < infinity, (e) therefore Lorentz symmetry. The gap in this argument is step (c) -- spatial isotropy of the continuum limit is not guaranteed from a cubic lattice (which has only discrete rotational symmetry).

**References:**
- Ignatowsky, Phys. Z. 11 (1910) 972; Arch. Math. Phys. 17 (1911) 1
- Levy-Leblond, Am. J. Phys. 44 (1976) 271
- Pal, Eur. J. Phys. 24 (2003) 315, arXiv:physics/0302045
- Pelissetto-Testa, Am. J. Phys. 83 (2015) 338, arXiv:1504.02423

### Jacobson (2016) - Entanglement Equilibrium and the Einstein Equation

**Key contribution:** Showed that if the vacuum is a state of maximal entanglement entropy for small geodesic balls at fixed volume (the "maximal vacuum entanglement hypothesis" or MVEH), and the entanglement first law delta S = delta <K> holds, then the semiclassical Einstein equation G_ab + Lambda g_ab = 8 pi G T_ab follows.

**Method:** Decomposes entanglement entropy as S = S_UV + S_mat where S_UV = eta * Area is the area-proportional UV contribution. The MVEH condition delta S = 0 combined with the Raychaudhuri equation for delta Area and the entanglement first law for delta S_mat yields Einstein's equation. In the conformal case, the modular Hamiltonian is the Casini-Huerta-Myers conformal Hamiltonian, making the derivation explicit.

**Limitations:** (1) Assumes smooth geometry exists (this IS Gap 1). (2) Uses conformal modular Hamiltonian (Route A) or tensoriality assumption (Route B via Lovelock). (3) Does not derive MVEH -- treats it as a hypothesis (though Paper 6 reframes it via Connes-Rovelli thermal time).

**Critical implication for v9.0:** This is the ENDPOINT of the v9.0 chain. Everything upstream (Fisher manifold, Lorentz, BW) is aimed at establishing the preconditions for Jacobson's argument. Once smooth geometry + Lorentz invariance + BW are established, Jacobson's argument runs exactly as in Paper 6.

**Reference:** Jacobson, Phys. Rev. Lett. 116 (2016) 201101, arXiv:1505.04753

### Dyson-Lieb-Simon (1978) - Neel Order in Quantum Antiferromagnets

**Key contribution:** Proved rigorously that the SU(2) Heisenberg antiferromagnet exhibits spontaneous symmetry breaking (Neel order) for spin S >= 1 in d >= 3 and S >= 3/2 in d = 2 at zero temperature. Extended by subsequent work: S = 1/2 in d = 2 (Kennedy-Lieb-Shastry 1988, not rigorous but strong numerical evidence).

**Method:** Infrared bounds via reflection positivity. Bounded the two-point spin correlation function from below, showing it cannot decay fast enough to prevent long-range order.

**Limitations:** (1) Does not determine the spectrum above the Neel ground state (spectral gap vs. gapless Goldstone modes). (2) The existence of Neel order means the SU(n) symmetry is spontaneously broken, producing (n^2 - 1) Goldstone modes (for SU(n)), which are gapless. (3) The resulting low-energy theory is a nonlinear sigma model, not a CFT.

**Critical implication for v9.0:** This is the OBSTACLE. In d >= 2, the Heisenberg AFM breaks SU(n) spontaneously, producing Goldstone bosons and closing the spectral gap. The Hastings-Koma theorem (which requires a gap) does not directly apply. However: (a) the nonlinear sigma model has well-defined propagating modes with finite velocity (the spin-wave velocity c_s), (b) correlations decay as power laws (not exponentially) but the Fisher metric may still be well-defined (it encodes local geometric information, not long-range correlations), (c) at finite temperature, Mermin-Wagner prevents true long-range order in d = 2, restoring a finite correlation length.

**Reference:** Dyson-Lieb-Simon, J. Stat. Phys. 18 (1978) 335

### Cao-Carroll-Michalakis (2016) - Space from Hilbert Space

**Key contribution:** Showed how to reconstruct spatial geometry from the entanglement structure of a quantum state. Used mutual information I(A:B) between subsystems as a distance measure on a graph, then applied classical multidimensional scaling (MDS) to extract the emergent spatial dimension and metric.

**Method:** Factorize Hilbert space H = tensor product of H_i. Define graph distance d(i,j) from mutual information. Apply MDS to extract embedding dimension and coordinates. For "redundancy-constrained" states (area-law entanglement), this produces a well-defined Riemannian geometry.

**Limitations:** (1) Mutual information is NOT the same as the Fisher information metric -- MI measures total correlations, Fisher metric measures distinguishability. (2) The MDS procedure is a classical statistical technique with no guarantee of uniqueness. (3) Produces spatial geometry only, not spacetime. (4) Does not explain why the state should have area-law entanglement.

**Critical implication for v9.0:** The CCM approach uses mutual information; v9.0 proposes to use the Fisher information metric instead. The Fisher metric has the advantage of being a true Riemannian metric (by Cencov/Petz theory) with natural monotonicity properties, and it directly encodes the local distinguishability of reduced states. The v9.0 approach is conceptually cleaner: the Fisher metric on the space of reduced density matrices {rho_A(x)} as x varies over lattice sites IS the emergent spatial metric, without needing MDS or ad hoc distance definitions.

**Reference:** Cao-Carroll-Michalakis, Phys. Rev. D 95 (2017) 024031, arXiv:1606.08444

### Petz (1996) / Morozova-Cencov (1991) - Classification of Quantum Fisher Metrics

**Key contribution:** Classified all Riemannian metrics on quantum state space that are monotone under completely positive trace-preserving (CPTP) maps. Unlike the classical case (Cencov's theorem: the Fisher-Rao metric is unique up to a constant), the quantum case admits a one-parameter family of monotone metrics, each determined by an operator monotone function f: (0,infinity) -> (0,infinity) with f(t) = t f(1/t).

**Method:** Characterized monotone metrics via the formula g_f(A, B) = Tr(A c_f(L_rho, R_rho)^{-1}(B)) where c_f is the mean associated with f, and L_rho, R_rho are left and right multiplication superoperators. The SLD (symmetric logarithmic derivative) Fisher information corresponds to f(t) = (1+t)/2 and gives the largest monotone metric (= 4 x Bures metric). The RLD metric corresponds to f(t) = t and gives the smallest.

**Limitations:** (1) The non-uniqueness of the quantum Fisher metric means one must choose which metric to use. (2) The SLD Fisher metric has discontinuities when the rank of rho changes (Safranek 2017). (3) All metrics agree on pure states (reducing to the Fubini-Study metric) but differ on mixed states.

**Critical implication for v9.0:** Must specify WHICH quantum Fisher metric defines the emergent geometry. The SLD Fisher metric (= 4 x Bures) is the natural choice because: (a) it is the largest monotone metric, giving the most sensitive geometry, (b) it equals the Cramer-Rao bound for parameter estimation, giving it operational meaning, (c) for the reduced density matrices of interest (which are generically full-rank for thermal/ground states of lattice systems), all monotone metrics give qualitatively similar results. The choice must be stated explicitly and consistently.

**Reference:** Petz, Lin. Alg. Appl. 244 (1996) 81; Morozova-Cencov, "Markov invariant geometry on manifolds of states," J. Soviet Math. 56 (1991) 2648

---

## Recent Developments

| Paper | Authors | Year | Advance | Impact on Our Work |
|-------|---------|------|---------|-------------------|
| Emergent Spacetime in Quantum Lattice Models | Jahn et al. | 2022 | Showed how graphene-like lattice models produce emergent curved spacetime in continuum limit with identifiable lattice observables | Validates the general program of lattice -> continuum geometry; different mechanism than Fisher metric |
| Fisher Curvature Scaling at Critical Points | (recent arXiv) | 2025 | Exact information-geometric exponent for scalar curvature of Fisher metric at criticality with periodic BCs | Confirms Fisher metric geometry is singular at QPTs; relevant to understanding what happens at phase boundaries |
| QFI Density in Extended Ising Model | (EPJB 2025) | 2025 | QFI density from all two-qubit RDMs detects topological QPTs in 1D extended Ising | Demonstrates QFI from reduced density matrices detects phase structure; directly relevant technology |
| Lattice BW via QMC | (arXiv 2511.00950) | 2025 | Extended lattice BW entanglement Hamiltonian studies; BW accuracy even beyond strict Lorentz invariance | Strengthens the case that BW structure emerges robustly from lattice systems |
| Information Geometry of Quantum Stochastic Thermodynamics | (PRE 2025) | 2025 | Decomposed any QFI into metric-independent incoherent part + metric-dependent coherent contribution | Clarifies the structure of QFI decomposition; relevant to understanding which part of Fisher geometry carries geometric information |
| Stability of Gapped Phases (AKLT, decorated) | Nachtergaele-Sims-Young | 2023 | First rigorous proof of stable gapped phase for non-commuting 2D interaction (decorated AKLT) | Progress toward rigorous gap proofs in d >= 2, though not for undecorated Heisenberg |
| Farnsworth n-point Exceptional Universe | Farnsworth | 2025 | Spectral triples from non-simple exceptional Jordan algebras with F_4 x F_4 gauge theory | Different approach to exceptional geometry; cross-validates the Jordan algebra route of Papers 5-7 |

---

## Known Limiting Cases

| Limit | Known Result | Source | Verified By |
|-------|-------------|--------|-------------|
| d=1, SU(2), S=1/2 AFM | SU(2)_1 WZW CFT with c=1; Calabrese-Cardy S(L) = (c/3) ln(L/a) + const | Calabrese-Cardy, JSTAT P06002 (2004) | Paper 6 Section III; extensive DMRG literature |
| d=1, AKLT (S=1) | Gapped, VBS ground state, exponential decay xi ~ 1/ln(3), exact MPS with bond dim 2 | Affleck-Kennedy-Lieb-Tasaki, CMP 115 (1988) | Exact diagonalization, DMRG; Haldane gap confirmed numerically |
| d >= 3, SU(2), S >= 1 | Neel order (rigorous), Goldstone modes, NL sigma model description | Dyson-Lieb-Simon (1978) | QMC, spin-wave theory |
| d = 2, SU(2), S = 1/2 | Neel order (strong numerical evidence, not fully rigorous for S=1/2), spin-wave velocity c_s well-determined | Kennedy-Lieb-Shastry (1988); extensive QMC | QMC: Sandvik et al.; spin-wave: Zheng et al. |
| T > 0, d = 2, SU(2) | Mermin-Wagner: no long-range order, finite correlation length xi(T) ~ exp(2 pi rho_s / T) | Mermin-Wagner (1966); Hasenbusch-Nishimori (1990) | QMC |
| Bures metric, pure states | g_Bures = (1/4) g_FS (Fubini-Study metric) | Standard QI textbooks | Mathematical identity |
| Fisher metric, i.i.d. limit | QFI is additive: F(rho^{tensor n}) = n F(rho) | Petz (1996) | Standard result |

---

## Open Questions

1. **Does the SU(n) Heisenberg AFM in d >= 2 have a spectral gap for any n?** -- For the fundamental (spin-1/2 analog) representation, the answer is almost certainly NO due to Neel order and Goldstone modes. For higher representations or SU(n) with large n, the situation is more complex. The SU(N) model on the square lattice has a Neel-to-VBS transition at N_c ~ 4.57 (Beach et al. 2009); for N > N_c the VBS phase may be gapped. This is an open question in condensed matter theory.

2. **Is the Fisher metric on the manifold of reduced density matrices {rho_A(x)} smooth for gapless systems?** -- For gapped systems, exponential decay of correlations guarantees smoothness. For gapless systems with power-law correlations (Goldstone modes), the Fisher metric is still defined but may have power-law divergences or singularities. The d=1 CFT case is well-understood (the Fisher metric is smooth and conformally flat); the d >= 2 Neel-ordered case is not.

3. **Does the lattice BW structure emerge without assuming Lorentz invariance?** -- The numerical evidence (Giudici et al. 2018, arXiv:2511.00950) is encouraging but not a proof. A rigorous derivation of BW-like modular flow from lattice dynamics alone does not exist.

4. **Can the von Ignatowsky argument be made rigorous starting from lattice symmetries?** -- The argument requires continuous spatial isotropy, but a lattice has only discrete rotational symmetry (e.g., C_4v for a square lattice). In the continuum limit, one expects the full rotation group to be restored if the lattice spacing goes to zero, but making this rigorous requires control of lattice artifacts.

5. **What is the role of the spin-wave velocity c_s?** -- In the Neel-ordered phase, the spin-wave velocity c_s = Ja sqrt(2Zd) (in spin-wave theory) sets the ratio of spatial to temporal scales. This should become the emergent speed of light in the von Ignatowsky argument. The precise relationship between c_s and the LR velocity v_LR (which is typically larger, since v_LR is a rigorous upper bound) needs clarification.

---

## Notation Conventions in the Literature

| Quantity | Standard Symbol(s) | Variations | Our Choice | Reason |
|----------|-------------------|------------|------------|--------|
| Spectral gap | gamma, Delta | Gap, E_gap, Delta E | gamma | Consistent with Hastings-Koma |
| Lieb-Robinson velocity | v_LR, c_LR | v, c_s (NOT spin-wave velocity) | v_LR | Distinguish from spin-wave velocity c_s |
| Quantum Fisher information | F, H, I_F, g_F | QFI, J (Helstrom) | F or g_F | F for scalar, g_F for metric tensor |
| Bures metric | d_B, g_B | d_Bures, ds^2_B | g_B | Petz convention |
| Modular Hamiltonian | K, H_mod | K_A, H_E, h_ent | K_A | Consistent with Paper 6 |
| Correlation length | xi | l_c, lambda_c | xi | Standard condensed matter |
| Lattice spacing | a | epsilon, delta, l | a | Consistent with Paper 6 |
| Spin-wave velocity | c_s, c_sw | v_s, v_sw | c_s | Standard spin-wave theory |
| Entanglement entropy | S, S_E, S_vN | S_A, S_ent | S(A) | Consistent with Paper 6 |

---

## Alternatives Considered

| Category | Recommended | Alternative | Why Not |
|----------|-------------|-------------|---------|
| Distance metric for emergent geometry | Fisher/Bures metric on reduced states | Mutual information distance (CCM) | Fisher is a true Riemannian metric with monotonicity; MI requires ad hoc MDS; Fisher has operational meaning via Cramer-Rao |
| Route to Lorentz invariance | LR bound + von Ignatowsky | Assume Lorentz invariance as input | Defeats the purpose -- Gap 1 requires DERIVING smooth Lorentz-invariant geometry |
| Route to Lorentz invariance | LR bound + von Ignatowsky | Emergent Lorentz from RG fixed point | Requires showing the lattice model flows to a Lorentz-invariant fixed point, which is essentially the full continuum limit problem |
| Handling gaplessness in d >= 2 | Work with NL sigma model effective theory | Restrict to gapped AKLT-like models | The physical case (Heisenberg AFM) is gapless in d >= 2; AKLT is a special point that does not represent the generic physics |
| Which quantum Fisher metric | SLD (symmetric logarithmic derivative) | RLD, WYD, or other Petz-family metric | SLD = 4 x Bures is standard in quantum estimation theory, largest monotone metric, agrees with all others on pure states |
| Modular Hamiltonian identification | BW theorem (after establishing Lorentz) | Compute modular Hamiltonian directly on lattice | Direct computation is model-specific and does not give a universal argument; BW gives universal structure once Lorentz is established |

---

## Logical Dependency Chain for v9.0

```
Paper 5: Self-modeling -> M_n(C)^sa
    |
    v
Paper 6 L1-L5: SWAP lattice + area law + entanglement first law
    |
    v
[v9.0 NEW] Exponential/power-law decay of reduced-state correlations
    |
    v
[v9.0 NEW] Fisher metric g_F on {rho_A(x)} is smooth Riemannian manifold
    |
    v
[v9.0 NEW] Continuum limit of Fisher manifold = smooth (M, g)
    |
    v
[v9.0 NEW] LR velocity v_LR -> finite max signal speed
    |
    v
[v9.0 NEW] von Ignatowsky + lattice symmetries -> Lorentz(v_LR)
    |
    v
[v9.0 NEW] BW theorem gives K_A = boost generator (modular = geometric)
    |
    v
Paper 6 L6-L8: Jacobson entanglement equilibrium -> Einstein equations
```

Each arrow is a non-trivial step. The hardest steps are:
- Fisher metric smoothness for the gapless (Neel-ordered) case in d >= 2
- Spatial isotropy of the continuum limit from discrete lattice symmetry
- BW emergence without assuming Lorentz invariance as input

---

## Sources

- Hastings-Koma, CMP 265 (2006) 781, arXiv:math-ph/0507008 -- Spectral gap implies exponential clustering
- Nachtergaele-Sims-Young, JMP 60 (2019) 061101, arXiv:1810.02428 -- Comprehensive LR bounds and quasi-locality
- Nachtergaele-Sims, CMP 265 (2006) 119, arXiv:math-ph/0506030 -- LR bounds and exponential clustering theorem
- Zanardi-Giorda-Cozzini, PRL 99 (2007) 100603, arXiv:quant-ph/0701061 -- Fisher metric and QPTs
- Bisognano-Wichmann, JMP 16 (1975) 985; JMP 17 (1976) 303 -- Modular Hamiltonian = boost generator
- Giudici et al., PRB 98 (2018) 134403, arXiv:1807.01322 -- Lattice BW entanglement Hamiltonians
- Jacobson, PRL 116 (2016) 201101, arXiv:1505.04753 -- Entanglement equilibrium and Einstein equation
- Cao-Carroll-Michalakis, PRD 95 (2017) 024031, arXiv:1606.08444 -- Space from Hilbert space
- Petz, LAA 244 (1996) 81 -- Classification of quantum monotone metrics
- Morozova-Cencov, J. Soviet Math. 56 (1991) 2648 -- Markov invariant geometry on state manifolds
- Safranek, PRB 95 (2017) 245123, arXiv:1612.04581 -- Discontinuities of QFI and Bures metric
- Zhou-Jiang, arXiv:1910.08473 -- Exact correspondence QFI and Bures metric
- Dyson-Lieb-Simon, J. Stat. Phys. 18 (1978) 335 -- Neel order in quantum antiferromagnets
- Affleck-Kennedy-Lieb-Tasaki, CMP 115 (1988) 477 -- AKLT model, VBS ground states
- Ignatowsky, Phys. Z. 11 (1910) 972 -- Relativity without light
- Levy-Leblond, Am. J. Phys. 44 (1976) 271 -- One more derivation of the Lorentz transformation
- Connes-Rovelli, CQG 11 (1994) 2899 -- Thermal time hypothesis
- Calabrese-Cardy, JSTAT P06002 (2004) -- Entanglement entropy in 1+1 CFT
- Beach et al., PRB 80 (2009) 184401 -- SU(N) Heisenberg model on square lattice
- Mermin-Wagner, PRL 17 (1966) 1133 -- Absence of ordering in 1D and 2D
- Altland-Simons, "Condensed Matter Field Theory" (Cambridge, 2010) -- NL sigma model for antiferromagnets, Ch. 6
- Nachtergaele-Sims-Young, Ann. Henri Poincare 23 (2022) 393, arXiv:2106.02997 -- Stability of gapped ground state phases
