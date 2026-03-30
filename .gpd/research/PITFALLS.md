# Known Pitfalls Research

**Domain:** Information-geometric continuum limit from finite-dimensional observer; Fisher metric as spacetime; emergent Lorentz invariance; Bisognano-Wichmann in effective theories
**Researched:** 2026-03-29
**Confidence:** HIGH (pitfalls grounded in established theorems, published counterexamples, and concrete obstructions from information geometry and lattice QFT)

## Critical Pitfalls

### Pitfall 1: The Signature Problem -- Fisher Metric Is Riemannian, Not Lorentzian

**What goes wrong:**
The quantum Fisher information metric on a manifold of density matrices is positive semi-definite by construction. When positive-definite, it defines a Riemannian metric -- signature (+,+,...,+). Spacetime requires a Lorentzian metric -- signature (-,+,+,+). There is no mechanism within standard information geometry to produce a negative eigenvalue in the Fisher metric. Claiming that the Fisher metric "becomes" a spacetime metric requires an explicit construction producing Lorentzian signature, which is a non-trivial step that most information-geometry-to-gravity proposals gloss over or handle by fiat.

The Fisher information matrix g_{ij}(theta) = E[d_i log p * d_j log p] is manifestly a sum of squares (expectation of a product of real quantities), so every eigenvalue is non-negative. This is a theorem, not an approximation. The quantum Fisher metric (Bures metric) inherits this property.

**Why it happens:**
Information geometry naturally produces Riemannian geometry because distinguishability between probability distributions is non-negative. The analogy "Fisher metric ~ spacetime metric" works for the spatial part but has no mechanism for the temporal part. Many papers in the "gravity from entanglement" literature silently assume Lorentzian signature will emerge from some additional ingredient (causal structure, modular flow, Wick rotation) without deriving it.

**How to avoid:**
The v9.0 approach uses von Ignatowsky to obtain Lorentz structure, not the Fisher metric directly. The Fisher metric provides spatial geometry (Riemannian); the causal structure (Lorentzian signature) comes separately from LR bounds and isotropy. This is the correct strategy -- but it means the Fisher metric does NOT "become" a spacetime metric. It becomes the SPATIAL metric, and the full spacetime metric is assembled from:
- Spatial: Fisher metric g_{ij}(x)
- Temporal: modular flow (BW/Connes-Rovelli)
- Causal: LR bound providing finite speed c_LR
- Assembly: von Ignatowsky combining isotropy + finite speed -> Lorentz

Each step must be verified independently. The Fisher metric alone gives Riemannian geometry, period.

**Warning signs:**
- Any claim that the Fisher metric has Lorentzian signature
- Equations where g_{mu nu} (Lorentzian, 4D) is equated directly with the Fisher metric g_{ij} (Riemannian, 3D or parameter-space)
- Missing construction of how temporal direction enters
- Wick rotation invoked without justification from the lattice physics

**Phase to address:** Phase A (Fisher geometry) must establish the Riemannian spatial metric. Phase C (emergent Lorentz) must produce the causal/temporal structure. The assembly into a full Lorentzian metric should be Phase E, and it must explicitly construct the metric as ds^2 = -c^2 dt^2 + g_{ij} dx^i dx^j (or equivalent), not claim the Fisher metric is Lorentzian.

**References:**
- Braunstein-Caves (1994), PRL 72, 3439 -- Fisher metric is positive-definite
- Cencov (1982) -- Chentsov's theorem: Fisher metric is the unique (up to scale) monotone Riemannian metric on statistical manifolds
- arXiv:2108.05976 -- Singularities of the quantum Fisher information

---

### Pitfall 2: Discrete Lattice Symmetry vs Continuous Isotropy -- von Ignatowsky's Premises Fail on a Lattice

**What goes wrong:**
Von Ignatowsky's theorem (1911) derives Lorentz transformations from: (1) relativity principle, (2) linearity of transformations, (3) spatial isotropy (continuous rotational invariance), (4) existence of a finite maximum speed. A cubic lattice Z^d has discrete rotational symmetry (the octahedral group O_h, order 48 in d=3), NOT continuous SO(3) isotropy. The theorem's proof uses rotational invariance to constrain the transformation to depend on speed only (not direction), which fails with only discrete symmetry. On a hypercubic lattice, the LR velocity v_LR is generically direction-dependent -- faster along lattice axes than along diagonals.

Moment isotropy analysis shows that a cubic lattice achieves isotropy of tensor moments only up to second order (the quadratic form sum x_i^2 is invariant under O_h). Fourth-order tensors break isotropy: sum x_i^4 is NOT the same as (sum x_i^2)^2/3 under O_h. This means the LR velocity, which depends on the lattice structure through higher-order terms, is anisotropic at finite lattice spacing.

**Why it happens:**
The continuum limit is supposed to restore full rotational symmetry, but von Ignatowsky's theorem is being invoked BEFORE taking the continuum limit (to DERIVE Lorentz invariance that would make the continuum limit Lorentzian). This is logically problematic: you need continuous isotropy to invoke the theorem, but you only get continuous isotropy after taking the continuum limit, which requires Lorentz invariance to be Lorentzian.

**How to avoid:**
The argument must be structured carefully:
1. First establish that the lattice effective theory at long wavelengths has emergent continuous rotational symmetry (this is the universality argument -- cubic lattice systems in the appropriate universality class have SO(d) emergent symmetry).
2. Then invoke von Ignatowsky on the emergent long-wavelength theory.
3. This means Lorentz invariance is emergent at long wavelengths, not exact at all scales.

The honest statement is: "On a regular lattice, the effective long-wavelength theory inherits continuous rotational symmetry from the universality class, and von Ignatowsky then gives Lorentz invariance." But this requires proving that the SWAP Hamiltonian's effective theory is in a universality class with emergent SO(d) symmetry -- which is precisely the continuum limit problem.

Quantify the anisotropy: compute v_LR along different lattice directions and show it converges to an isotropic value as a -> 0. The correction should scale as O(a^2/L^2) for a cubic lattice.

**Warning signs:**
- Invoking von Ignatowsky on the lattice without discussing emergent isotropy
- Claiming "the lattice is isotropic" without specifying the sense (it is NOT continuously isotropic)
- Missing the direction-dependence of v_LR
- Circular logic: using Lorentz invariance to justify the continuum limit that is needed to get the isotropy that is needed for von Ignatowsky

**Phase to address:** Phase C (emergent Lorentz). Must explicitly address the gap between discrete and continuous isotropy. Compute v_LR anisotropy on small lattices as a function of direction and show convergence toward isotropy with increasing scale.

**References:**
- von Ignatowsky (1911), Archiv der Mathematik und Physik 17
- Mattingly (2005), Living Rev. Rel. 8, 5 -- Modern tests of Lorentz invariance
- arXiv:0709.1464 -- Discrete rotational symmetry, moment isotropy, and lattice Boltzmann models
- Visser (2011), arXiv:1112.1466 -- Inertial frames without the relativity principle (discusses evasions of von Ignatowsky)

---

### Pitfall 3: Heisenberg AFM in d >= 2 Has Neel Order and Gapless Goldstone Modes -- NOT a Gapped or Conformal Theory

**What goes wrong:**
The v9.0 derivation chain requires: (a) exponential decay of correlations (from spectral gap), and (b) emergent Lorentz invariance. But the Heisenberg antiferromagnet on a bipartite lattice in d >= 2 spontaneously breaks SU(n) symmetry to produce Neel order. This generates gapless Goldstone modes (magnons with linear dispersion omega ~ |k|). The system is therefore:
- NOT gapped (magnons are gapless)
- NOT conformal (Neel order breaks the symmetry)
- Correlation functions decay as POWER LAWS, not exponentially (algebraic decay from Goldstone modes)

This means Hastings' theorem (spectral gap -> exponential decay) does not apply because there IS no spectral gap. The correlation decay is algebraic (power-law), and the effective theory is a nonlinear sigma model, not a CFT.

For n=2 specifically (the SU(2) Heisenberg AFM):
- d=1: No Neel order (Mermin-Wagner). Gapless, critical, described by SU(2)_1 WZW CFT with central charge c=1. Algebraic correlations.
- d=2: Neel order at T=0 (proved by Dyson-Lieb-Simon for S>=1; strong numerical evidence for S=1/2). Gapless magnons. Power-law correlations.
- d=3: Neel order with magnon gap set by anisotropy or quantum corrections. Still gapless in the isotropic case.

**Why it happens:**
The project description says "exponential decay proved rigorously for n=2" but the SU(2) Heisenberg AFM on bipartite lattices in d >= 2 has ALGEBRAIC, not exponential, correlation decay due to Goldstone modes. Exponential decay occurs only in GAPPED systems (Hastings 2006). The Heisenberg AFM in d >= 2 is GAPLESS.

Possible resolutions: (a) The claim might refer specifically to d=1, where the spin-1 chain (Haldane gap) has exponential decay. (b) The SWAP Hamiltonian for general n might differ from SU(2) Heisenberg in important ways. (c) Exponential decay of connected correlations transverse to the order parameter might hold despite the Goldstone modes. None of these can be assumed without proof.

**How to avoid:**
1. Precisely state which correlations decay exponentially and in which regime. Distinguish longitudinal (along Neel order) from transverse (Goldstone) correlations.
2. For d >= 2: accept that full exponential decay does not hold, and determine whether the Fisher geometry construction works with algebraic decay + Neel order.
3. For d=1 with n=2: the system is critical (SU(2)_1 WZW), correlations decay as power law |x|^{-1}. This is well-understood but NOT exponential.
4. Consider whether the relevant object is the CONNECTED correlation function (which might decay faster) or the full correlation function.

The derivation chain may need restructuring: instead of gap -> exponential decay -> smooth Fisher manifold, it might be: Neel order -> nonlinear sigma model -> effective Lorentz-invariant low-energy theory -> Fisher manifold construction on the effective theory. But this is a different argument.

**Warning signs:**
- Claiming exponential decay for the Heisenberg AFM in d >= 2 without specifying which correlators
- Citing Hastings (2006) for a gapless system
- Ignoring Goldstone modes entirely
- Confusing d=1 (critical, algebraic) with d >= 2 (ordered, algebraic but for different reason)

**Phase to address:** Phase B (exponential decay). This is the most fragile link in the chain. Must honestly confront the gapless nature of the Heisenberg AFM in d >= 2 and determine whether the Fisher geometry construction survives with algebraic decay.

**References:**
- Hastings (2006), CMP 265, 781 -- Spectral gap implies exponential decay (applies ONLY to gapped systems)
- Dyson-Lieb-Simon (1978), JStatPhys 18, 335 -- Phase transitions in quantum Heisenberg models
- Nachtergaele-Sims (2006), CMP 265, 119 -- LR bounds (apply regardless of gap)
- Goldstone, Salam, Weinberg (1962) -- Broken symmetry implies gapless modes

---

### Pitfall 4: BW Theorem Requires Lorentz Invariance -- Circular if Lorentz Is What You Are Deriving

**What goes wrong:**
The Bisognano-Wichmann theorem states that the modular operator of a wedge-region algebra in a Wightman QFT equals the boost generator. Its proof requires:
1. Wightman axioms (or Haag-Kastler axioms)
2. Poincare covariance (including Lorentz invariance)
3. Spectrum condition (positive energy)
4. Existence of a vacuum state

The v9.0 chain attempts: Fisher geometry -> Lorentz -> BW -> Jacobson -> Einstein. But BW REQUIRES Lorentz invariance as an INPUT. If you are using BW to establish the modular Hamiltonian that feeds into Jacobson's argument, you need Lorentz invariance first. But if you are also trying to DERIVE Lorentz invariance in the same chain, the logic is:

Derive Lorentz (Phase C) -> Assume BW (needs Lorentz from Phase C) -> Get modular Hamiltonian -> Jacobson -> Einstein

This is not circular IF Phase C's Lorentz derivation is independent of BW. But it means BW cannot be used to SUPPORT the Lorentz derivation. The chain is sequential, not circular, but each link must be independently established.

The real danger: BW on lattice. Numerical studies (Giudici et al. 2018, arXiv:1807.01322; Mendes-Santos et al. 2020, SciPost Phys. Core 2, 007) show that the lattice Bisognano-Wichmann ansatz works well ONLY when the low-energy theory is Lorentz-invariant. For non-relativistic systems, BW breaks down. This means BW on the lattice is a DIAGNOSTIC of emergent Lorentz invariance, not an independent ingredient.

**Why it happens:**
The gravity-from-entanglement program typically ASSUMES a continuum Lorentz-invariant QFT and then uses BW to connect modular flow to geometric flow. The v9.0 program tries to DERIVE the continuum Lorentz-invariant theory from the lattice. Using BW in this context requires careful separation of what is derived vs what is assumed.

**How to avoid:**
Structure the argument as:
1. Phase A: Fisher metric gives spatial Riemannian geometry (no BW needed)
2. Phase B: Correlation decay characterizes the ground state (no BW needed)
3. Phase C: Emergent Lorentz invariance from isotropy + LR finite speed (no BW needed)
4. Phase D: GIVEN Lorentz invariance from Phase C, BW theorem applies to the effective theory, identifying modular Hamiltonian with boost generator
5. Phase E: Jacobson's argument using BW output from Phase D

BW enters AFTER Lorentz is established. Do not use BW to support any step in the Lorentz derivation. The numerical BW verification on the lattice (Phase D) is a CONSISTENCY CHECK, not a derivation step.

**Warning signs:**
- Using BW to argue for Lorentz invariance
- Claiming BW holds on the lattice without checking that the effective theory is Lorentz-invariant
- Citing the lattice BW ansatz accuracy as evidence for the approach, when the ansatz ASSUMES the thing being proved
- Conflating "BW is approximately satisfied on the lattice" with "the effective theory satisfies Wightman axioms"

**Phase to address:** Phase D (BW/equilibrium). Must clearly state that BW is applied to the EFFECTIVE theory after Lorentz invariance is established, not to the bare lattice theory.

**References:**
- Bisognano-Wichmann (1976), JMP 17, 303 -- Original theorem
- Giudici et al. (2018), PRB 98, 134403 (arXiv:1807.01322) -- BW on lattice: works when low-energy theory is Lorentz-invariant
- Mendes-Santos et al. (2020), SciPost Phys. Core 2, 007 -- BW modular Hamiltonian in critical spin chains
- arXiv:2511.00950 -- QMC study of lattice-BW limits

---

### Pitfall 5: Quantum Fisher Information Metric Is Singular at Rank-Changing Points

**What goes wrong:**
The quantum Fisher information matrix (QFIM) is discontinuous at points where the rank of the density matrix changes. Specifically, when an eigenvalue of rho_Lambda(x) passes through zero as x varies across the lattice, the QFIM jumps discontinuously. This means the Fisher metric on the manifold of reduced states rho_Lambda(x) is NOT smooth at such points -- it can have singularities, discontinuities, or degeneracies.

For the SWAP lattice ground state, the reduced density matrix rho_Lambda(x) at site x is obtained by tracing out all other sites. As x varies, the eigenvalue spectrum of rho_Lambda(x) changes. If any eigenvalue reaches zero at some x (the boundary of the state space), the QFIM is undefined or discontinuous there.

The Bures metric (the continuous extension of the QFIM through rank-deficient points) exists and is well-defined, but it may differ from the QFIM at the singular points. The Fisher manifold M = {rho_Lambda(x) : x in lattice} is smooth ONLY if all rho_Lambda(x) have the same rank for all x.

**Why it happens:**
The QFIM involves terms of the form |<i|d_mu rho|j>|^2 / (p_i + p_j) where p_i, p_j are eigenvalues. When p_i -> 0, these terms can diverge or jump. The standard SLD (symmetric logarithmic derivative) Fisher information has this singularity. Alternative quantum Fisher metrics (Wigner-Yanase, Kubo-Mori) have different singular behavior but are all problematic at rank-changing points.

**How to avoid:**
1. Prove that rho_Lambda(x) has FULL RANK for all x in the lattice. For a thermal state at finite temperature, rho is always full-rank. For a ground state, reduced density matrices are typically full-rank if the ground state is entangled, but this must be verified.
2. If full rank cannot be guaranteed, use the Bures metric (which extends continuously through rank-deficient points) rather than the raw QFIM. State explicitly that you are using Bures, not SLD Fisher.
3. For the SWAP lattice ground state: by translation invariance on a regular lattice, all rho_Lambda(x) have the same spectrum (up to boundary effects). If one is full-rank, all are. So the key check is: does the SWAP ground state's single-site reduced density matrix have full rank?
4. For the Heisenberg AFM ground state on a bipartite lattice: in the Neel-ordered phase, the single-site reduced density matrix is approximately |up><up| on one sublattice and |down><down| on the other. This has rank 1, NOT full rank. The QFIM between neighboring sites (different sublattice) would be singular.

Resolution: if correlation decay generates a small mixing away from pure Neel, rho_Lambda(x) is full rank but nearly pure. The Fisher distance between sublattice A and B sites is then large but finite. This needs quantification.

**Warning signs:**
- Claiming the Fisher manifold is smooth without checking rank of reduced density matrices
- Using the SLD Fisher metric without verifying full rank
- Ignoring sublattice structure in Neel-ordered phases
- Conflating Bures metric with SLD Fisher metric at singular points

**Phase to address:** Phase A (Fisher geometry). Must prove full-rank property of single-site reduced density matrices in the SWAP ground state, or explain how to handle rank-deficient cases.

**References:**
- arXiv:2108.05976 -- Taming singularities of the quantum Fisher information
- Safranek (2017), PRA 95, 052320 -- Discontinuities of the quantum Fisher information and the Bures metric
- Braunstein-Caves (1994), PRL 72, 3439 -- Fisher metric definition

---

### Pitfall 6: "Observer as UV Cutoff" Does Not Solve the Continuum Limit Problem

**What goes wrong:**
The v9.0 argument claims that the finite-dimensional C*-observer (M_n(C)^sa from Paper 5) provides a natural UV cutoff, and therefore the continuum limit problem is "dissolved" rather than solved. The idea: since the observer has finite resolution (n^2 real parameters), it cannot resolve physics below the lattice scale, so the effective geometry it sees is automatically smooth.

This is physically intuitive but mathematically insufficient. The continuum limit problem is not "can the observer see sub-lattice structure?" -- it is "does the lattice theory have a well-defined limit as a -> 0?" These are different questions:

(a) Observer resolution: The observer's finite dimension limits what it can measure. Agreed. But this does not make the lattice theory's correlation functions converge to continuum ones. It makes the observer's coarse-grained description well-defined, which is a weaker statement.

(b) Effective smoothness: A coarse-grained description can appear smooth even if the underlying lattice theory has lattice artifacts (anisotropy, umklapp, Brillouin zone effects). Smoothness of the coarse-grained theory does not imply the lattice theory has a continuum limit.

(c) Universality: The real mechanism for continuum limits is universality -- irrelevant operators in the RG flow are suppressed at long wavelengths. This requires the system to be at or near a critical point (for CFT) or to have a well-defined low-energy effective theory (for gapped or ordered phases). The observer's finite dimension does not provide this.

(d) The analogy to experimental physics: In lattice QCD, the lattice provides a UV cutoff. But the continuum limit exists because the lattice theory is in the same universality class as continuum QCD -- this is a property of the THEORY, not of the observer. Calling the observer a "UV cutoff" does not prove universality.

**Why it happens:**
Confusing two meanings of "cutoff":
- Physical cutoff: the theory is defined on a lattice, so momenta above pi/a do not exist. This is automatic for any lattice theory.
- Observer cutoff: the observer cannot distinguish states that differ only at sub-lattice scales. This is a property of the measurement apparatus.

The continuum limit requires showing that physics is INDEPENDENT of the cutoff as it is removed (a -> 0). An observer-cutoff argument shows that the observer cannot tell whether a -> 0 or not. These are very different claims. The former is a statement about the theory; the latter is a statement about the observer's limitations.

**How to avoid:**
1. Distinguish clearly between "the observer sees smooth effective geometry" (a statement about coarse-graining, likely true) and "the lattice theory has a continuum limit" (a statement about universality, needs proof).
2. If the claim is the weaker one (observer sees smooth geometry), state it as such and acknowledge that the continuum limit problem is sidestepped, not solved.
3. If the claim is the stronger one (continuum limit exists), provide the universality argument: identify the universality class, the relevant and irrelevant operators, and the RG flow.
4. The honest framing: "The finite-dimensional observer provides a physical justification for coarse-graining. The coarse-grained description is smooth. Whether this coarse-grained description corresponds to a well-defined continuum QFT is a separate question that we address via [specific argument]."

**Warning signs:**
- Claiming the continuum limit is "dissolved" without providing a universality argument
- Equating observer resolution with continuum limit
- Asserting that finite observer dimension automatically gives smooth effective geometry without checking lattice artifacts
- Missing the distinction between "the lattice theory HAS a continuum limit" and "the observer CANNOT TELL the difference"

**Phase to address:** Phase E (assembly). The framing of the continuum limit claim must be calibrated. If the honest claim is "effective smoothness from coarse-graining," say that. If the claim is "continuum limit exists," prove it.

**References:**
- Wilson-Kogut (1974), Phys. Rep. 12, 75 -- Renormalization group and continuum limits
- Luscher (2010), arXiv:1002.4232 -- Computational strategies for lattice QCD (continuum extrapolation)
- Cao-Carroll-Michalakis (2017), PRD 95, 024031 -- Gravity from entanglement (assumes smooth geometry)

---

### Pitfall 7: Claiming All Four Paper 6 Gaps Close Via One Mechanism When They Have Different Mathematical Content

**What goes wrong:**
Paper 6 identified four gaps with distinct mathematical content:

1. **Continuum limit** (Gap 1): Does the lattice theory produce a smooth Riemannian manifold at long wavelengths? This is an RG/universality question.
2. **Conformal approximation** (Gap 2, Route A only): Is the modular Hamiltonian well-approximated by the conformal one? This is a question about conformal symmetry in the effective theory.
3. **Tensoriality** (Gap 3, Route B only): Is the entanglement-geometry equation a symmetric 2-tensor equation with at most second derivatives? This is a question about the form of the effective field equations.
4. **MVEH** (not numbered as gap, but "structural identification"): Is the lattice ground state the maximum-entanglement state? This is a vacuum selection question.

The v9.0 claim is that the Fisher geometry + observer-as-cutoff mechanism closes ALL FOUR simultaneously. This is suspicious because:

- Gap 1 is about universality/RG flow
- Gap 2 is about conformal symmetry (which the Heisenberg AFM in d >= 2 BREAKS via Neel order)
- Gap 3 is about the derivative expansion of the effective theory
- MVEH is about vacuum selection

These are logically independent questions. A single mechanism that closes all four would need to address universality, conformal symmetry, derivative expansion, and vacuum selection simultaneously. This is possible in principle (if the mechanism is sufficiently powerful) but raises the prior probability of overclaiming.

**Why it happens:**
The appeal of a unified mechanism is strong -- it would be elegant if one idea closed all four gaps. But elegance is not a substitute for proof. Each gap was identified for a specific mathematical reason, and each requires a specific mathematical resolution.

**How to avoid:**
Address each gap independently and explicitly:

1. **Continuum limit:** State the universality argument. What universality class? What are the irrelevant operators? How do lattice artifacts scale to zero?
2. **Conformal approximation:** Either (a) show the effective theory IS conformal (unlikely for Neel-ordered d >= 2), (b) bound the non-conformal corrections and show they are small, or (c) use Route B (Lovelock) which avoids this gap entirely.
3. **Tensoriality:** Derive the form of the effective equations from the lattice, or argue that the derivative expansion truncates at second order for the coarse-grained theory.
4. **MVEH:** The thermal-time argument from Paper 6 may be sufficient. State whether the Fisher geometry adds anything new.

Score each gap as: CLOSED (proved), NARROWED (reduced to a weaker assumption), or OPEN (not addressed). Do not claim "closed" unless the mathematical argument is complete.

**Warning signs:**
- Single paragraph claiming all four gaps close, without separate arguments
- Using the phrase "the observer-as-cutoff mechanism closes..." for all gaps
- Not distinguishing Route A (needs conformal) from Route B (needs tensoriality)
- Declaring gaps "dissolved" rather than "closed" (this is rhetoric, not mathematics)

**Phase to address:** Phase E (assembly). Each gap must have its own subsection with its own argument and its own honest assessment.

---

## Moderate Pitfalls

### Pitfall 8: Exponential Decay for General n Is Substantially Harder Than for n=2

**What goes wrong:**
The SWAP Hamiltonian H = sum J * SWAP is equivalent to the Heisenberg model for n=2 (SU(2) spin-1/2), but for general n it is the SU(n) Heisenberg model. The ground state properties depend dramatically on n:
- n=2: Neel order in d >= 2, critical (WZW) in d=1. Well-studied.
- n=3: SU(3) model, possibly with different ordered phases. Less well-studied.
- n >= 4: SU(n) models can have qualitatively different behavior (dimerized, topological, or other exotic ground states).

Claiming results for general n based on the n=2 case is not justified. The SU(n) Heisenberg model's phase diagram is an active research area.

**Prevention:** Prove results for n=2 first, flag general n as conjecture. The scoping contract already does this ("prove n=2, flag n > 2"). Follow through -- do not slip into claiming general n results.

### Pitfall 9: Frustration-Free Systems Cannot Host Emergent Lorentz Invariance

**What goes wrong:**
A 2025 result (Phys. Rev. X 15, 041050) rigorously proves that frustration-free quantum many-body systems with power-law decaying ground-state correlations have dynamical exponent z >= 2. Lorentz invariance requires z = 1 (linear dispersion). Therefore frustration-free systems CANNOT have emergent Lorentz invariance.

The Heisenberg antiferromagnet on a bipartite lattice is NOT frustration-free (the ground state does not simultaneously minimize each local term). So this result does not directly kill the v9.0 approach. However, it is important to verify:
1. The SWAP Hamiltonian for general n on the target lattice is NOT frustration-free.
2. Any approximate or variational ground state construction does not accidentally impose frustration-freeness.
3. The distinction is stated explicitly to preempt reviewer objections.

**Prevention:** State early that the Heisenberg/SWAP Hamiltonian on a bipartite lattice with J > 0 (AFM) is NOT frustration-free, and cite the z >= 2 bound as a constraint that does NOT apply to this system.

### Pitfall 10: Fisher Metric Recovers Lattice Distance Only Under Specific Conditions

**What goes wrong:**
The claim that the Fisher metric on reduced states recovers the lattice distance requires that:
(a) rho_Lambda(x) varies smoothly with x (requires smoothness of ground state correlations),
(b) the variation is dominated by nearest-neighbor effects (requires locality of correlations),
(c) the Fisher distance d_F(x, x+a) is proportional to a (the lattice spacing) to leading order.

Condition (c) is NOT automatic. The Fisher distance depends on the overlap between neighboring reduced density matrices, which depends on the ground state's entanglement structure. For a product state (no entanglement), rho_Lambda(x) is the same for all x, and d_F = 0. For a maximally entangled state, rho_Lambda(x) = I/n for all x, and again d_F = 0 (all reduced states identical). The Fisher distance is maximized for intermediate entanglement.

For the Heisenberg AFM with Neel order: on sublattice A, rho ~ |up><up|; on sublattice B, rho ~ |down><down|. The Fisher distance alternates between large (A to B) and zero (A to A), giving a saw-tooth pattern, NOT a smooth metric.

**Prevention:** Compute the Fisher metric explicitly for small lattices in the SWAP ground state. Verify that it gives something proportional to lattice distance, not a sublattice-dependent pattern. The sublattice issue may be resolved by coarse-graining over unit cells (averaging A and B sublattices), but this must be done explicitly.

---

## Approximation Shortcuts

| Shortcut | Immediate Benefit | Long-term Cost | When Acceptable |
| --- | --- | --- | --- |
| Treating Fisher metric as Lorentzian | Directly identifies spacetime metric | Violates positive-definiteness theorem; invalidates all downstream results | Never -- must construct Lorentzian metric separately from Riemannian Fisher metric |
| Assuming exponential decay for d >= 2 Heisenberg AFM | Enables clean Hastings-based argument | Contradicted by Goldstone theorem; magnons give algebraic decay | Never for isotropic AFM -- must either work with algebraic decay or add explicit gap mechanism |
| Using BW before establishing Lorentz | Simplifies argument ordering | Creates logical circularity | Only as a heuristic/motivation; formal argument must have Lorentz before BW |
| Claiming "observer as UV cutoff" closes continuum limit | Avoids the hardest problem | Does not address universality; reviewer will reject | Acceptable as physical motivation, not as mathematical proof |
| Ignoring sublattice structure in Fisher metric | Smoother-looking results | Misses the alternating pattern from Neel order | Never for d >= 2 -- sublattice structure is the dominant feature |
| Assuming continuous isotropy on the lattice | Enables direct von Ignatowsky application | Incorrect -- lattice has only discrete rotational symmetry | Only at long wavelengths after establishing emergent isotropy |

## Convention Traps

| Convention Issue | Common Mistake | Correct Approach |
| --- | --- | --- |
| Fisher information: classical vs quantum | Using classical Fisher formula for quantum states | Use SLD (symmetric logarithmic derivative) Fisher information for density matrices: g_{ij} = (1/2) Tr[rho {L_i, L_j}] where rho dL/dtheta = (L rho + rho L)/2 |
| Bures metric vs SLD Fisher metric | Treating them as identical | They agree on full-rank states but differ at rank-deficient points. Bures is always well-defined; SLD Fisher can diverge. State which one you use. |
| "Distance" on a lattice | Confusing graph distance (integer, discrete) with Fisher distance (continuous, geometric) | Graph distance d(x,y) counts edges. Fisher distance d_F(x,y) integrates the metric. The claim is d_F ~ d(x,y) * a at leading order. |
| Metric signature notation | Using g_{mu nu} for both spatial Fisher metric (Riemannian) and spacetime metric (Lorentzian) | Use g_{ij} for spatial Fisher metric (i,j = 1..d) and g_{mu nu} for spacetime (mu,nu = 0..d). Never conflate indices. |
| LR velocity units | Mixing lattice units (v_LR in sites/time) with continuum units (c in m/s) | v_LR has units of [lattice spacing]/[time]. In natural units with a=1, it is dimensionless. The identification with c requires specifying the unit conversion: c = v_LR * a / tau where tau is the lattice time scale. |

## Numerical Traps

| Trap | Symptoms | Prevention | When It Breaks |
| --- | --- | --- | --- |
| Fisher metric from finite-difference derivatives of rho(x) | Noisy or divergent metric components | Use analytic derivatives where possible; for numerical derivatives, use central differences with step size << correlation length | When rho(x) is nearly singular (eigenvalue ~ 0) or when step size is comparable to lattice spacing |
| ED on small lattices showing "smooth" Fisher metric | Appears to confirm smoothness | Finite-size effects dominate for N <= 20; boundary effects and finite-size gaps mask the true thermodynamic behavior | When N is smaller than twice the correlation length |
| SLD Fisher information diverges near pure states | Numerical overflow or artificially large metric | Regularize: add small epsilon to eigenvalues of rho, or use Bures metric which is continuous | When ground state has nearly pure reduced density matrices (weak entanglement) |
| v_LR computation on small lattices | Apparent isotropy due to finite-size quantization | Compute v_LR on lattices large enough to resolve directional dependence; use elongated lattices along different directions | When lattice is smaller than ~10 sites in each direction |
| Neel order detection conflated with correlation decay | Power-law correlations mistaken for exponential with large correlation length on small lattices | Fit both power-law and exponential; distinguish via chi^2 or Bayesian model comparison | For N <= 20, both fits may look acceptable |

## Interpretation Mistakes

| Mistake | Risk | Prevention |
| --- | --- | --- |
| Interpreting "observer sees smooth geometry" as "continuum limit exists" | Conflating observer-dependent coarse-graining with objective property of the theory | State explicitly: "smooth effective geometry" is a coarse-grained description, not a claim about the continuum limit of the lattice theory |
| Claiming "Fisher metric = spacetime metric" without the temporal direction | Missing that spacetime has one more dimension (time) than the Fisher manifold (spatial) | The Fisher metric provides the spatial part. Temporal direction comes from modular flow/LR causal structure. State both. |
| Taking numerical BW agreement on small lattices as proof of Wightman axioms | BW can be approximately satisfied without full Wightman axioms | BW on lattice is a necessary condition for the effective theory being Lorentz-invariant, not sufficient. Quantify deviations. |
| Interpreting algebraic (power-law) correlation decay as "almost exponential" | Mischaracterizes the physics; Goldstone modes are not "almost gapped" | State that correlations are algebraic due to Goldstone modes, and explain why the argument works (or doesn't) with algebraic decay |
| Assuming "closing all four gaps" means the derivation is complete | Other assumptions remain (lattice topology, J > 0, dimension d) | List ALL remaining assumptions explicitly after "closing" the gaps. The derivation chain has more inputs than just these four gaps. |

## Publication Pitfalls

| Pitfall | Impact | Better Approach |
| --- | --- | --- |
| Claiming "continuum limit derived" when only "effective smoothness established" | Reviewer will reject; overclaiming relative to what is proved | Use precise language: "effective smooth geometry from coarse-graining" or "continuum limit established in the universality sense" |
| Claiming all four gaps "closed" when some are only "narrowed" | Loss of credibility; the gaps were identified by Paper 6 precisely because they are hard | Score each gap honestly: CLOSED, NARROWED, or STILL OPEN. "Three narrowed, one closed" is better than "all four closed" if that is the truth. |
| Not citing the z >= 2 frustration-free result (PRX 2025) | Reviewer familiar with this result will ask why it does not apply | Cite it and explain: the SWAP/Heisenberg AFM is NOT frustration-free, so the bound does not apply |
| Presenting the Fisher geometry as entirely novel | There is extensive prior work (Zanardi, Provost-Vallee, Braunstein-Caves) | Cite prior work prominently. State what is new: the specific application to the self-modeling lattice ground state. |

## "Looks Correct But Is Not" Checklist

- [ ] **"Fisher metric is smooth":** VERIFY: rho_Lambda(x) must have constant rank for all x. Check rank of single-site reduced density matrix in the SWAP ground state. If Neel-ordered, rank may alternate between sublattices.
- [ ] **"Exponential decay proved for n=2":** VERIFY: In which dimension? d=1 has algebraic decay (critical WZW). d >= 2 has algebraic decay (Goldstone modes). Only specific gapped chains (spin-1, Haldane) have exponential decay. Which regime is being claimed?
- [ ] **"von Ignatowsky gives Lorentz":** VERIFY: Does the lattice have continuous isotropy? No. Does the effective theory have emergent isotropy? Must be proved, not assumed.
- [ ] **"BW holds in the effective theory":** VERIFY: Does the effective theory satisfy Wightman axioms? This requires Lorentz invariance (from Phase C), spectral condition, and existence of vacuum. Each must be checked.
- [ ] **"Observer provides UV cutoff":** VERIFY: This is true (finite dimension limits resolution) but does it imply smooth effective geometry? Only with additional input (universality, coarse-graining prescription). Not automatic.
- [ ] **"All four Paper 6 gaps close via one mechanism":** VERIFY: Are separate arguments given for each gap? Does each argument address the specific mathematical content of that gap? Or is there a single hand-wave covering all four?

## Recovery Strategies

| Pitfall | Recovery Cost | Recovery Steps |
| --- | --- | --- |
| Signature problem (P1) | LOW | The v9.0 approach already handles this correctly (Fisher = spatial, LR = causal, von Ignatowsky = Lorentz). Just make the separation explicit. |
| Discrete isotropy (P2) | MEDIUM | Compute lattice anisotropy of v_LR; show it vanishes as a/L -> 0; invoke universality for emergent continuous isotropy. Quantify the rate. |
| No gap / Goldstone modes (P3) | HIGH | This is the hardest pitfall to recover from. Options: (a) work with algebraic decay (requires new Fisher geometry argument), (b) show that the relevant correlations (not the order parameter correlations) still decay fast enough, (c) restructure the argument through the nonlinear sigma model effective theory. |
| BW circularity (P4) | LOW | Restructure: establish Lorentz (Phase C) independently, THEN apply BW (Phase D). This is likely already the intended structure; just make the logical ordering explicit. |
| QFI singularities (P5) | MEDIUM | Prove full-rank of reduced density matrices, or switch to Bures metric, or regularize. May need sublattice coarse-graining for Neel-ordered phase. |
| Observer-cutoff overclaim (P6) | LOW | Reframe as "effective smoothness" rather than "continuum limit." Acknowledge the distinction. |
| All-four-gaps overclaim (P7) | MEDIUM | Score each gap independently. If some cannot be closed, state honestly which are closed, which narrowed, which open. |

## Pitfall-to-Phase Mapping

| Pitfall | Prevention Phase | Verification |
| --- | --- | --- |
| Signature problem (P1) | Phase A (Fisher geometry) | Check: does the Fisher metric have (+,...,+) signature? If yes, it is Riemannian. Do NOT claim Lorentzian. |
| Discrete isotropy (P2) | Phase C (emergent Lorentz) | Check: is von Ignatowsky invoked on the lattice or on the effective theory? Compute v_LR anisotropy. |
| No gap / Goldstone (P3) | Phase B (correlation decay) | Check: what is the correlation decay law? Exponential or algebraic? For which correlators? |
| BW circularity (P4) | Phase D (BW/equilibrium) | Check: is Lorentz invariance established BEFORE BW is used? Is BW used to support the Lorentz claim? |
| QFI singularities (P5) | Phase A (Fisher geometry) | Check: rank of rho_Lambda(x) for all x. If not constant rank, smoothness fails. |
| Observer-cutoff overclaim (P6) | Phase E (assembly) | Check: is the claim "smooth effective geometry" or "continuum limit exists"? Are they distinguished? |
| All-four-gaps overclaim (P7) | Phase E (assembly) | Check: separate argument for each gap with separate assessment. |
| General n vs n=2 (P8) | Phase B (correlation decay) | Check: are general n results proved or conjectured? Is the distinction stated? |
| Frustration-free bound (P9) | Phase C (emergent Lorentz) | Check: is the z >= 2 bound cited? Is the SWAP Hamiltonian's frustrated nature stated? |
| Fisher lattice distance (P10) | Phase A (Fisher geometry) | Check: does d_F(x,y) scale linearly with graph distance? Compute numerically. |

## Sources

- Braunstein, Caves (1994), PRL 72, 3439 -- Fisher metric on quantum states
- Chentsov (1982), "Statistical Decision Rules and Optimal Inference" -- Uniqueness of Fisher metric
- arXiv:2108.05976 -- Taming singularities of quantum Fisher information
- Safranek (2017), PRA 95, 052320 -- Discontinuities of QFI and Bures metric
- Hastings (2006), CMP 265, 781 -- Spectral gap implies exponential decay
- Nachtergaele-Sims (2006), CMP 265, 119 -- Lieb-Robinson bounds
- Dyson-Lieb-Simon (1978), JStatPhys 18, 335 -- Phase transitions in Heisenberg models
- von Ignatowsky (1911), Archiv der Mathematik und Physik 17 -- Lorentz from isotropy + finite speed
- Visser (2011), arXiv:1112.1466 -- Inertial frames without the relativity principle
- Bisognano-Wichmann (1976), JMP 17, 303 -- Modular theory and wedge algebras
- Giudici et al. (2018), PRB 98, 134403 (arXiv:1807.01322) -- Lattice BW entanglement Hamiltonians
- Mendes-Santos et al. (2020), SciPost Phys. Core 2, 007 -- BW modular Hamiltonian in critical spin chains
- arXiv:2511.00950 -- QMC study of lattice-BW breakdown limits
- Phys. Rev. X 15, 041050 (2025) (arXiv:2406.06415) -- z >= 2 bound in frustration-free systems
- Zanardi et al. (2007), PRA 76 -- Information geometry of quantum phase transitions
- Provost-Vallee (1980), CMP 76 -- Riemannian structure on manifolds of quantum states
- Hamma et al. (2009), PRL 102, 017204 -- Lieb-Robinson and speed of light
- Wilson-Kogut (1974), Phys. Rep. 12, 75 -- Renormalization group and continuum limits
- arXiv:0709.1464 -- Discrete rotational symmetry and moment isotropy
- Mattingly (2005), Living Rev. Rel. 8, 5 -- Modern tests of Lorentz invariance

---

_Known pitfalls research for: Information-geometric continuum limit from finite-dimensional observer_
_Researched: 2026-03-29_
