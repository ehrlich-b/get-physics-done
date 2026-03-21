# Methods Research

**Domain:** Quantum gravity / Entanglement & area laws / Thermodynamic gravity / Emergent geometry
**Researched:** 2026-03-21
**Confidence:** MEDIUM

### Scope Boundary

METHODS.md covers analytical and conceptual PHYSICS methods for the v3.0 GR extension: formalizing lattice locality, proving area-law entanglement, applying Jacobson's thermodynamic argument, and constructing emergent geometry. It does NOT cover software tools or libraries -- those belong in COMPUTATIONAL.md.

**Critical distinction from v2.0:** The v2.0 methods worked BELOW C\*-algebra level (in order unit spaces, effect algebras, Jordan algebras). The v3.0 methods work ABOVE it: we now HAVE M\_n(C)^sa at each site (from Paper 5) and must derive consequences of assembling many such sites into a lattice with local interactions. The algebraic framework is established; what is new is the spatial/geometric structure.

---

## Recommended Methods

### Analytical Methods

| Method | Purpose | Why Recommended |
|--------|---------|-----------------|
| Quantum lattice system formalization | Define locality for M\_n(C)^sa lattice | Standard framework: assigns local algebras to sites, locality = tensor product + nearest-neighbor interactions |
| Mutual information area law (Wolf-Verstraete-Cirac-Hastings) | Prove area-law scaling without gapped Hamiltonian assumption | Works for ANY state with finite correlation length; avoids needing a spectral gap |
| Lieb-Robinson bounds | Establish finite propagation speed from local interactions | Connects lattice locality to correlation decay; standard tool for all area-law arguments |
| Jacobson's thermodynamic derivation (1995 + 2016 update) | Convert area-law S + Clausius + Unruh into Einstein's equations | The target theorem; well-established (30 years) |
| Cao-Carroll-Michalakis emergent geometry | Construct spatial geometry from entanglement structure | Closest existing framework to our lattice approach; uses mutual information as distance |

### Method Selection by Problem Type

**If formalizing locality for the M\_n(C)^sa lattice:**
- Use the standard quantum lattice system framework (Bratteli-Robinson)
- Because it naturally handles finite-dimensional local algebras with tensor product composites, and our M\_n(C)^sa sites are precisely the self-adjoint parts of the local matrix algebras

**If proving area-law entanglement from self-modeling locality:**
- Use the mutual information area law (Wolf et al. 2008) as the primary route
- Because it requires ONLY a finite correlation length (which follows from Lieb-Robinson bounds + local interactions), not a spectral gap
- Use Brandao-Horodecki (2013) as the secondary/strengthening route for 1D
- Because it gives the strongest bound: exponential decay of correlations implies area law

**If applying Jacobson's argument to the discrete lattice:**
- Use Jacobson 2016 ("Entanglement Equilibrium") over Jacobson 1995
- Because the 2016 version uses entanglement entropy directly (not thermodynamic entropy), which is what our lattice produces, and replaces the Clausius relation with a maximal entanglement hypothesis

**If constructing emergent geometry:**
- Use Cao-Carroll-Michalakis (2017) mutual information distance
- Because it works in finite-dimensional Hilbert spaces (our setting), does not require AdS/CFT, and naturally produces spatial dimensionality from entanglement structure

---

## Method Details

### Method 1: Quantum Lattice System Formalization

**What:** Define a lattice Lambda (graph with vertices V and edges E) where each vertex x carries a local algebra A\_x = M\_n(C). The total algebra for any region R is A\_R = tensor product of A\_x for x in R. Locality means interactions couple only neighboring sites.

**Mathematical basis:**

The quasi-local algebra framework (Bratteli-Robinson, "Operator Algebras and Quantum Statistical Mechanics"):
- Lattice: Lambda = (V, E) a graph (typically Z^d or finite subset)
- Local algebra at site x: A\_x = M\_n(C) (a full matrix algebra)
- Regional algebra: A\_R = bigotimes\_{x in R} A\_x for finite R subset V
- Quasi-local algebra: A = norm-closure of union of all A\_R
- Local Hamiltonian: H = sum of interaction terms Phi(X) where each Phi(X) is supported on a subset X of V with |X| bounded, and Phi(X) in A\_X

For the self-modeling lattice:
- Each site x is a self-modeling system; Paper 5 gives A\_x^sa = M\_n(C)^sa
- The self-adjoint part of the local algebra IS the effect algebra from Paper 5
- Nearest-neighbor interactions: Phi({x,y}) for {x,y} in E encode the body-model coupling between adjacent self-modeling systems
- "Self-modeling is local" translates to: information about site x can only reach site z by propagating through intermediate sites

**What this formalizes:**
1. Sites = self-modeling systems from Paper 5
2. Edges = body-model boundary couplings between adjacent sites
3. Locality = interactions are nearest-neighbor (or finite-range)
4. The global state is determined by local interactions propagating through the lattice

**Known results in this framework:**
- Lieb-Robinson bounds hold automatically for finite-range interactions on any lattice
- Ground states of gapped local Hamiltonians obey area laws (in 1D rigorously; in higher D with additional assumptions)
- The quasi-local algebra is a UHF (uniformly hyperfinite) algebra, which is a simple C\*-algebra

**Regime of validity:** Works for any finite-dimensional local algebra (our M\_n(C) qualifies). The lattice can be any graph. No restriction on spatial dimension.

**Confidence:** HIGH. This is the standard framework for quantum lattice systems, used universally in condensed matter and mathematical physics. Bratteli-Robinson is the definitive reference (>40 years).

**Key references:**
- Bratteli & Robinson, "Operator Algebras and Quantum Statistical Mechanics" vols 1-2, Springer (1979, 1981)
- Nachtergaele & Sims, "Quasi-Locality Bounds for Quantum Lattice Systems. Part I," J. Math. Phys. 60, 061101 (2019). [arXiv:1810.02428](https://arxiv.org/abs/1810.02428)
- Nachtergaele & Sims, "Lieb-Robinson Bounds and the Exponential Clustering Theorem," Commun. Math. Phys. 265, 119-130 (2006)


### Method 2: Lieb-Robinson Bounds for Locality

**What:** Prove that local interactions on the M\_n(C)^sa lattice produce a finite speed of information propagation, giving an effective light cone. This is the mathematical backbone connecting "local interactions" to "finite correlation length," which is the input for area-law arguments.

**Mathematical basis:**

For a local Hamiltonian H = sum\_X Phi(X) with finite-range interactions on a lattice, the Lieb-Robinson bound states:

||[A(t), B]|| <= C ||A|| ||B|| min(|supp(A)|, |supp(B)|) exp(-a(d(A,B) - v|t|))

where:
- A(t) = e^{iHt} A e^{-iHt} is the Heisenberg-evolved observable
- d(A,B) is the distance between the supports of A and B
- v is the Lieb-Robinson velocity (depends on interaction strength and lattice geometry)
- a is a decay constant
- C is a constant

**What this gives us:**
1. An effective causal structure on the lattice (even though the underlying theory is non-relativistic)
2. Exponential clustering: for gapped ground states, correlations decay exponentially with distance
3. Input for area-law arguments: bounded entanglement generation rate implies area-law scaling

**For the self-modeling lattice:**
- The nearest-neighbor body-model coupling defines the interaction terms Phi({x,y})
- The Lieb-Robinson velocity v is determined by the coupling strength
- The emergent "speed of light" is this Lieb-Robinson velocity
- This is the FIRST place where a causal/geometric structure appears from the algebraic setup

**Key result (Bravyi-Hastings-Verstraete 2006):** The rate at which entanglement entropy can be generated in a block of spins scales like the boundary area of that block. Specifically, for a region R evolving under a local Hamiltonian starting from a product state:

dS(R)/dt <= c * |boundary(R)|

This is an area-law RATE, which already points toward area-law entropy for equilibrium states.

**Regime of validity:** Exact for finite-range interactions. Generalizes to power-law interactions (Lieb-Robinson velocity then depends on distance). Requires bounded local Hilbert space dimension (satisfied: each site is M\_n(C)).

**Confidence:** HIGH. Lieb-Robinson bounds are rigorous mathematical results, proven since 1972, extensively generalized.

**Key references:**
- Lieb & Robinson, "The finite group velocity of quantum spin systems," Commun. Math. Phys. 28, 251-257 (1972)
- Bravyi, Hastings & Verstraete, "Lieb-Robinson Bounds and the Generation of Correlations and Topological Quantum Order," PRL 97, 050401 (2006). [arXiv:quant-ph/0603121](https://arxiv.org/abs/quant-ph/0603121)
- Nachtergaele, Sims & Young, "Quasi-Locality Bounds for Quantum Lattice Systems," J. Math. Phys. 60, 061101 (2019). [arXiv:1810.02428](https://arxiv.org/abs/1810.02428)


### Method 3: Area-Law Entanglement from Locality -- Primary Route

**What:** Prove that the entanglement entropy S(A) of a region A in the lattice scales as |boundary(A)|, not |A|. This is the critical link between self-modeling locality and gravity.

**Three available routes, in order of recommendation:**

#### Route 3A: Mutual Information Area Law (PRIMARY -- RECOMMENDED)

**Why primary:** This route does NOT require a Hamiltonian or spectral gap. It works for ANY state with bounded mutual information between subsystems, which follows from locality of correlations.

**Mathematical basis (Wolf-Verstraete-Cirac-Hastings 2008):**

For a quantum state rho on a lattice, define the mutual information:
I(A:B) = S(A) + S(B) - S(AB)

Theorem (WVCH 2008): For a thermal state at inverse temperature beta of a local Hamiltonian H on a lattice:
I(A:B) <= beta * |boundary(A)| * ||h||

where ||h|| is the local interaction strength and |boundary(A)| is the number of boundary terms connecting A to its complement B.

Since I(A:B) = S(A) + S(B) - S(AB), and for a pure global state S(A) = S(B), this directly gives an area law for mutual information. For thermal states, S(A) obeys an area law up to a volume-law thermal contribution.

**Why this works for self-modeling:**
- Self-modeling locality means interactions are local (nearest-neighbor body-model couplings)
- Local interactions produce bounded mutual information across any cut
- The mutual information is bounded by the number of interactions crossing the cut = |boundary(A)|
- This is an INFORMATION-THEORETIC argument, not a Hamiltonian ground-state argument

**Known limitation:** The WVCH bound applies to thermal states, not arbitrary pure states. For pure ground states, one needs either a gap assumption (Hastings) or correlation decay (Brandao-Horodecki). The mutual information bound is the most general.

**Confidence:** HIGH for the mutual information bound itself. MEDIUM for applying it to the self-modeling context (need to identify what plays the role of "thermal state" or "equilibrium state" in the self-modeling framework).

**Key references:**
- Wolf, Verstraete, Cirac & Hastings, "Area Laws in Quantum Systems: Mutual Information and Correlations," PRL 100, 070502 (2008). [arXiv:0704.3906](https://arxiv.org/abs/0704.3906)


#### Route 3B: Hastings' Area Law for 1D Gapped Systems

**What:** For ground states of 1D gapped local Hamiltonians, the entanglement entropy across any cut is bounded by a constant (independent of system size).

**Exact assumptions:**
1. 1D lattice (chain of sites)
2. Local Hamiltonian (finite-range interactions)
3. Unique ground state
4. Spectral gap Delta > 0 between ground state and first excited state

**Key result (Hastings 2007):** S(A) <= c * exp(c' / Delta) for a half-chain A, where c, c' are constants depending on the local Hilbert space dimension and interaction range.

**Proof technique:** Coarse-grain the frustrated system into an approximately frustration-free system; use Lieb-Robinson bounds to show that the ground state can be well-approximated by a state with bounded entanglement; the approximation error decays exponentially with the bond dimension of a matrix product state.

**What this gives vs. what it lacks:**
- GIVES: Rigorous area law in 1D, with explicit (but loose) bound on entropy
- LACKS: Extension to D > 1 (open problem for general gapped systems; proved only for frustration-free 2D by Anshu-Arad-Gosset 2022)
- LACKS: Applicability without a spectral gap assumption

**For the self-modeling lattice:** The spectral gap assumption is the bottleneck. We need to either (a) show the self-modeling lattice has a gapped ground state, or (b) bypass the gap requirement entirely (use Route 3A or 3C instead).

**Confidence:** HIGH for the theorem itself. LOW for direct applicability to self-modeling (gap condition unverified).

**Key references:**
- Hastings, "An Area Law for One Dimensional Quantum Systems," JSTAT P08024 (2007). [arXiv:0705.2024](https://arxiv.org/abs/0705.2024)
- Anshu, Arad & Gosset, "An area law for 2D frustration-free spin systems," arXiv:2103.02492 (2021), STOC 2022


#### Route 3C: Brandao-Horodecki Correlation Decay Route

**What:** For 1D states with exponentially decaying correlations, entanglement entropy obeys an area law. Does NOT require a Hamiltonian or spectral gap -- only correlation decay.

**Exact assumptions:**
1. 1D lattice
2. State with correlation length xi: |<A\_x B\_y> - <A\_x><B\_y>| <= C exp(-|x-y|/xi)
3. No Hamiltonian or gap assumption needed

**Key result (Brandao-Horodecki 2013, 2015):** If a 1D state has correlation length xi, then the entanglement entropy across any cut satisfies S <= exp(O(xi)).

**Why this matters:** The bound is exponential in the correlation length (worse than Hastings' bound, which is polynomial in 1/Delta), but the ASSUMPTION is weaker -- only correlation decay, not a spectral gap.

**For the self-modeling lattice:** Lieb-Robinson bounds + local interactions guarantee that correlations decay at least exponentially beyond the Lieb-Robinson cone. If the self-modeling state is a ground state or thermal state of the local interaction, exponential correlation decay follows from the gap (if gapped) or from the locality structure (if in thermal equilibrium). This route is the best fallback if the gap condition is hard to establish.

**Known limitation:** The entropy bound is exponential in xi, which is loose. Also only proved in 1D. The 2D generalization remains open.

**Confidence:** HIGH for the theorem. MEDIUM for applicability (need to establish correlation decay for self-modeling states).

**Key references:**
- Brandao & Horodecki, "An area law for entanglement from exponential decay of correlations," Nature Physics 9, 721 (2013). [arXiv:1309.3789](https://arxiv.org/abs/1309.3789)
- Brandao & Horodecki, "Exponential Decay of Correlations Implies Area Law," Commun. Math. Phys. 333, 761 (2015). [arXiv:1206.2947](https://arxiv.org/abs/1206.2947)


#### Route 3D: Direct Information-Theoretic Bound (MOST PROMISING FOR THIS PROJECT)

**What:** Bypass Hamiltonians entirely. Argue that locality of self-modeling DIRECTLY constrains the entanglement structure, producing area-law scaling from information-theoretic considerations alone.

**Mathematical basis:**

The key insight is that self-modeling locality is a constraint on the INFORMATION FLOW, not on a Hamiltonian's spectrum. The argument:

1. Self-modeling is local: site x learns about site y only through the chain of intermediaries x-x1-x2-...-y
2. The mutual information between non-adjacent sites is bounded by the channel capacity of the intermediary chain
3. For a region A, all information about its complement B must pass through the boundary sites
4. Therefore I(A:B) <= sum over boundary bonds of (channel capacity per bond)
5. Each bond has finite channel capacity (local dimension is n, so capacity <= 2 log n)
6. Therefore I(A:B) <= 2 log(n) * |boundary(A)|

This is a CHANNEL CAPACITY argument. It does not require a Hamiltonian, a spectral gap, or a specific state. It follows purely from the locality of information flow.

**Subtlety:** This argument gives an area law for MUTUAL INFORMATION, not for von Neumann entropy. For a pure global state, S(A) = S(B) and I(A:B) = 2S(A), so the area law for I translates to an area law for S. For a mixed global state, S(A) can have a volume-law thermal contribution even with area-law mutual information.

**For the self-modeling lattice:** The global state of the lattice (the fixed point of the self-modeling dynamics) is the relevant state. If the self-modeling dynamics has a PURE fixed point (a pure state that is consistent with all local self-models), then I(A:B) = 2S(A) and the mutual information area law immediately gives an entropy area law. If the fixed point is mixed, additional argument is needed.

**Key question:** Does the self-modeling lattice have a pure global state? This connects to the question of whether the lattice describes a "universe" (pure state) or a "subsystem" (mixed state). For the derivation of GR, we want the pure-state case (the universe is in a pure state, and subsystem entanglement obeys an area law).

**Confidence:** MEDIUM. The channel capacity argument is sound information theory. The gap is in establishing that the self-modeling fixed point is a pure global state. This is the MAIN BRIDGE to be constructed in the project.

**Key references:**
- Wolf, Verstraete, Cirac & Hastings (2008) for the connection between mutual information and area laws
- Eisert, Cramer & Plenio, "Colloquium: Area laws for the entanglement entropy," Rev. Mod. Phys. 82, 277 (2010). [arXiv:0808.3773](https://arxiv.org/abs/0808.3773)


### Method 4: Jacobson's Thermodynamic Argument -- Two Versions

#### Method 4A: Jacobson 1995 (Classical Thermodynamics Route)

**What:** Derive Einstein's field equations from the assumption that entropy is proportional to horizon area, plus the Clausius relation delta\_Q = T dS at local Rindler horizons.

**Three inputs:**
1. **Area-law entropy:** S = eta * A, where A is the area of a local Rindler horizon and eta = 1/(4 l\_P^2) in Planck units
2. **Clausius relation:** delta\_Q = T dS for quasi-static processes at the horizon
3. **Unruh temperature:** T = a/(2 pi), where a is the acceleration of the Rindler observer (in natural units hbar = c = k\_B = 1)

**Derivation sketch:**
1. At any spacetime point p, consider a local Rindler horizon (the causal boundary of an accelerated observer)
2. Matter-energy crossing the horizon carries heat flux delta\_Q = T\_ab k^a k^b (integrated Raychaudhuri focusing)
3. The Unruh temperature seen by the accelerated observer is T = a/(2 pi)
4. The horizon area change is delta\_A = R\_ab k^a k^b * (geometric expansion)
5. Applying delta\_Q = T dS = T * eta * delta\_A and demanding this hold for ALL local Rindler horizons at ALL points
6. This forces: G\_ab + Lambda g\_ab = (8 pi G) T\_ab (Einstein's equations with cosmological constant)

**What Jacobson's argument requires from us:**
- The lattice must produce states whose entanglement entropy is proportional to boundary area (area law)
- There must be a sensible notion of "local Rindler horizon" on the lattice (or in the continuum limit)
- The Unruh temperature must emerge from the lattice dynamics
- The Clausius relation (delta\_Q = T dS) must hold for perturbations of the lattice state

**Key subtlety for discrete/lattice systems:** Jacobson's argument is formulated in the continuum. To apply it on a lattice:
- "Horizon area" becomes the number of boundary bonds (discrete analog)
- "Unruh temperature" requires a notion of acceleration, which requires an emergent causal structure (from Lieb-Robinson bounds)
- The Clausius relation becomes a statement about entanglement first law: delta\_S = delta\_<H\_mod> where H\_mod is the modular Hamiltonian

**Confidence:** HIGH for the continuum argument (published 1995, widely accepted). MEDIUM for the discrete/lattice adaptation (active research area; see Jacobson 2016 for improvements).

**Key references:**
- Jacobson, "Thermodynamics of Spacetime: The Einstein Equation of State," PRL 75, 1260 (1995). [arXiv:gr-qc/9504004](https://arxiv.org/abs/gr-qc/9504004)


#### Method 4B: Jacobson 2016 (Entanglement Equilibrium -- RECOMMENDED)

**What:** Replace the thermodynamic inputs (Clausius relation, thermal entropy) with a single entanglement hypothesis: the vacuum state MAXIMIZES entanglement entropy in small geodesic balls at fixed volume.

**Maximal Vacuum Entanglement Hypothesis (MVEH):**

The vacuum entanglement entropy S\_EE in a small geodesic ball is maximal when:
1. The geometry is locally maximally symmetric (flat space / maximally symmetric vacuum)
2. The quantum fields are in the vacuum state

Perturbations away from the vacuum satisfy: delta\_S\_EE = 0 (first-order stationarity).

**Key result (Jacobson 2016):** For first-order perturbations of conformal quantum fields around the vacuum state on a locally maximally symmetric background:

delta\_S\_EE = 0 for all small balls <==> Einstein's equations hold

**Why this is better than 1995 for our project:**
1. Uses ENTANGLEMENT entropy directly (not thermodynamic entropy) -- our lattice naturally produces entanglement entropy
2. Replaces the Clausius relation with a stationarity condition (delta\_S = 0) -- easier to check
3. Does not require explicit Unruh temperature -- the modular Hamiltonian plays this role
4. Connects directly to the entanglement first law: delta\_S = delta\_<H\_mod>

**The entanglement first law:**
For a state rho perturbed to rho + delta\_rho, and the modular Hamiltonian H\_mod = -log(rho\_0) of the reference state rho\_0:

delta\_S = delta\_<H\_mod>     (exact for first-order perturbations)

This is the quantum information version of delta\_Q = T dS. The modular Hamiltonian H\_mod plays the role of the inverse temperature times the energy, and the entanglement entropy S plays the role of the thermal entropy.

**For the self-modeling lattice:**
- The "vacuum" is the ground state / fixed point of the self-modeling dynamics
- The "small geodesic ball" is a connected subregion of the lattice
- The stationarity condition delta\_S = 0 becomes: the self-modeling fixed point maximizes entanglement entropy at fixed local constraints
- This is plausible because self-modeling dynamics tends to maximize mutual information between body and model (the model needs to be as faithful as possible)

**Confidence:** MEDIUM. The Jacobson 2016 result is published and well-established for conformal fields. The application to finite-dimensional lattice systems requires:
1. Identifying the modular Hamiltonian of the self-modeling fixed point
2. Showing the fixed point satisfies the stationarity condition
3. Taking a continuum/large-lattice limit to recover smooth geometry

**Key references:**
- Jacobson, "Entanglement Equilibrium and the Einstein Equation," PRL 116, 201101 (2016). [arXiv:1505.04753](https://arxiv.org/abs/1505.04753)
- Chirco, Haggard, Riello & Rovelli, "Spacetime thermodynamics without hidden degrees of freedom," PRD 90, 044044 (2014). [arXiv:1401.5262](https://arxiv.org/abs/1401.5262)


### Method 5: Entanglement First Law and Linearized Einstein Equations

**What:** Use the entanglement first law (delta\_S = delta\_<H\_mod>) to derive linearized Einstein equations from perturbations of entanglement entropy. This is the bridge between the lattice area law and Jacobson's argument.

**Mathematical basis (Lashkari-McDermott-Van Raamsdonk 2014):**

In a conformal field theory:
- For ball-shaped regions, the modular Hamiltonian is known explicitly (Bisognano-Wichmann theorem generalization)
- The entanglement first law delta\_S = delta\_<H\_mod> holds exactly for first-order perturbations
- For holographic CFTs (with gravity duals), this implies the linearized Einstein equations in the bulk

**Key insight for our project:**
- We do NOT need AdS/CFT. The entanglement first law is a GENERAL result of quantum information theory
- delta\_S = delta\_<H\_mod> holds for ANY state rho\_0 and first-order perturbation delta\_rho
- The modular Hamiltonian H\_mod = -log(rho\_0) is defined for any state with full-rank density matrix
- For a lattice with local interactions, H\_mod for a region A is approximately local (Araki's result generalized to lattices by various authors)

**Lattice adaptation:**
1. Start with the self-modeling fixed point rho\_0 on the full lattice
2. For a region A, compute the reduced state rho\_A = tr\_B(rho\_0)
3. The modular Hamiltonian is H\_mod = -log(rho\_A)
4. For perturbations delta\_rho, the entanglement first law gives delta\_S(A) = tr(delta\_rho\_A * H\_mod)
5. If H\_mod is approximately local (supported near boundary(A)), this connects to an area-law perturbation
6. Demanding delta\_S(A) = delta\_<H\_mod> for ALL regions A constrains the geometry that can emerge

**Why "modular Hamiltonian is approximately local" matters:** If H\_mod for a region A has support concentrated on the boundary of A (as happens for Rindler wedges in continuum QFT, where H\_mod is the boost generator), then perturbations of the entropy are controlled by boundary physics, which is exactly the area-law structure needed for Jacobson's argument.

**Known limitation:** For general lattice states, H\_mod = -log(rho\_A) is not necessarily local. It is a sum over ALL operators on A, not just boundary operators. The approximate locality of H\_mod requires the state to have specific properties (short-range correlations, area-law entanglement). There is a potential circularity: we need area-law entanglement to make H\_mod local, and we need local H\_mod for Jacobson's argument. This is not vicious: the area law comes from Method 3, and the locality of H\_mod is a consequence (not a premise).

**Confidence:** MEDIUM-HIGH for the entanglement first law itself (rigorous QI result). MEDIUM for the locality of H\_mod on lattices (active research). LOW for the full chain from lattice to linearized Einstein (requires continuum limit).

**Key references:**
- Lashkari, McDermott & Van Raamsdonk, "Gravitational Dynamics From Entanglement 'Thermodynamics'," JHEP 04, 195 (2014). [arXiv:1308.3716](https://arxiv.org/abs/1308.3716)
- Faulkner, Guica, Hartman, Myers & Van Raamsdonk, "Gravitation from entanglement in holographic CFTs," JHEP 03, 051 (2014). [arXiv:1312.7856](https://arxiv.org/abs/1312.7856)
- Casini, Huerta & Myers, "Towards a derivation of holographic entanglement entropy," JHEP 1105, 036 (2011). [arXiv:1102.0440](https://arxiv.org/abs/1102.0440)


### Method 6: Emergent Geometry from Entanglement (Cao-Carroll-Michalakis)

**What:** Construct a spatial geometry (metric, dimensionality, curvature) from the entanglement structure of a quantum state on a finite-dimensional Hilbert space, without assuming AdS/CFT.

**Mathematical basis:**

Given a quantum state rho on a tensor product Hilbert space H = bigotimes\_x H\_x:

1. **Define distance from mutual information:**
   d(x,y) ~ 1 / I(x:y)
   where I(x:y) = S(x) + S(y) - S(xy) is the mutual information between sites x and y.
   Large mutual information = nearby; zero mutual information = far apart.

2. **Extract dimensionality via multidimensional scaling (MDS):**
   Given the distance matrix d(x,y), use classical MDS to find the best-fit embedding in R^D.
   The optimal D is the emergent spatial dimension.

3. **Read off geometry:**
   The embedding coordinates give the emergent spatial geometry.
   Curvature corresponds to deviations from flat-space entanglement patterns.

4. **Perturbations give Einstein's equations:**
   Cao-Carroll-Michalakis show that entanglement perturbations on emergent geometries naturally give rise to local modifications of spatial curvature which obey a spatial analog of Einstein's equation.

**Inputs required:**
- A quantum state on a tensor product of finite-dimensional Hilbert spaces
- A way to identify which degrees of freedom are "spatial" (the tensor product structure)
- Mutual information between all pairs of subsystems

**Outputs:**
- Emergent spatial dimension D
- Emergent spatial geometry (metric)
- Spatial curvature from entanglement perturbations
- A spatial analog of Einstein's equations

**For the self-modeling lattice:**
- The tensor product structure is given by the lattice: each site is an M\_n(C) factor
- The self-modeling fixed point determines the mutual information matrix I(x,y)
- The emergent geometry is read off from this matrix
- Self-modeling dynamics (which preserves the fixed point) corresponds to time evolution
- Perturbations of the fixed point give curvature perturbations

**Known limitations:**
1. Gives spatial geometry only, not full spacetime. Time must come from elsewhere (dynamics).
2. The mutual information distance is not necessarily a proper metric (triangle inequality can fail).
3. The MDS embedding is approximate -- the emergent geometry has a "resolution" limited by the number of lattice sites.
4. The "Einstein equation" obtained is a spatial constraint equation, not the full dynamical equation. Need Jacobson-type argument for the full Einstein equations.
5. Requires the mutual information matrix to have a structure consistent with a smooth geometry (not all lattice states give sensible geometry).

**Confidence:** MEDIUM. Published in PRD, well-cited, conceptually clean. The limitations are real but identified. The approach is a constructive existence proof, not a complete derivation.

**Key references:**
- Cao, Carroll & Michalakis, "Space from Hilbert Space: Recovering Geometry from Bulk Entanglement," PRD 95, 024031 (2017). [arXiv:1606.08444](https://arxiv.org/abs/1606.08444)
- Cao & Carroll, "Bulk Entanglement Gravity without a Boundary: Towards finding Einstein's equation in Hilbert space," PRD 97, 086003 (2018). [arXiv:1712.02803](https://arxiv.org/abs/1712.02803)
- Van Raamsdonk, "Building up spacetime with quantum entanglement," GRG 42, 2323 (2010). [arXiv:1005.3035](https://arxiv.org/abs/1005.3035)


### Method 7: MERA and Holographic Geometry (Supporting/Conceptual)

**What:** The Multi-scale Entanglement Renormalization Ansatz (MERA) tensor network naturally produces area-law entanglement AND has a geometric structure resembling AdS spacetime. This provides a CONSTRUCTIVE example of how area-law states give rise to geometry.

**How it works:**
- MERA is a specific tensor network architecture with layers of disentanglers and isometries
- The disentanglers remove short-range entanglement at each scale
- The isometries coarse-grain the lattice by combining sites
- The resulting tree-like structure has a depth (scale) direction that maps to the radial (holographic) direction of AdS

**Why it matters for this project:**
- MERA PRODUCES area-law entanglement by construction (each layer adds entanglement only at boundaries)
- The depth direction of MERA is an EMERGENT dimension (not in the original lattice)
- Swingle (2012) showed: MERA network structure = discretized AdS geometry
- This is the clearest existing example of "entanglement builds geometry"

**Why NOT to use MERA as the primary method:**
- MERA is a specific ansatz, not a proof. It shows that SOME area-law states have geometric interpretations, not that ALL do.
- The connection to Einstein's equations through MERA requires additional steps (Swingle's argument is suggestive, not rigorous).
- For our project, MERA is conceptual support, not the proof strategy.

**Confidence:** MEDIUM as conceptual framework. The MERA-AdS connection is well-established. It does NOT constitute a proof of our claims.

**Key references:**
- Swingle, "Entanglement Renormalization and Holography," PRD 86, 065007 (2012). [arXiv:1209.3304](https://arxiv.org/abs/1209.3304)
- Vidal, "Entanglement Renormalization," PRL 99, 220405 (2007). [arXiv:cond-mat/0512165](https://arxiv.org/abs/cond-mat/0512165)

---

## Logical Dependency Chain for v3.0

```
Paper 5 result: M_n(C)^sa at each site
    |
    v
Method 1: Quantum lattice formalization
    - Define lattice Lambda with A_x = M_n(C) at each site
    - Self-modeling locality = nearest-neighbor interactions
    |
    v
Method 2: Lieb-Robinson bounds
    - Local interactions => finite propagation speed v_LR
    - Emergent causal structure on the lattice
    - Exponential clustering of correlations (if gapped)
    |
    v
Method 3: Area-law entanglement  <-- CRITICAL STEP
    - Route 3A (mutual info): I(A:B) <= c * |boundary(A)|
    - Route 3D (channel capacity): I(A:B) <= 2 log(n) * |boundary(A)|
    - For pure global state: S(A) = I(A:B)/2 <= log(n) * |boundary(A)|
    |
    v
Method 5: Entanglement first law
    - delta_S(A) = delta_<H_mod> for perturbations
    - H_mod approximately local for area-law states
    |
    v
Method 4B: Jacobson 2016 (Entanglement Equilibrium)
    - MVEH: vacuum maximizes S_EE in small balls
    - delta_S_EE = 0 for all balls <==> Einstein's equations
    |
    v
Einstein's field equations (in continuum limit)
```

**Parallel supporting track:**
```
Method 6: Cao-Carroll-Michalakis
    - Construct emergent geometry from I(x,y) matrix
    - Verify consistency with the geometry implied by Einstein's equations

Method 7: MERA (conceptual support)
    - Constructive example that area-law states produce AdS-like geometry
```

---

## Alternatives Considered

| Recommended | Alternative | When to Use Alternative |
|-------------|------------|------------------------|
| Mutual information area law (Method 3A/3D) | Hastings gapped area law (Method 3B) | When a spectral gap can be rigorously established for the self-modeling lattice Hamiltonian |
| Jacobson 2016 entanglement equilibrium (Method 4B) | Jacobson 1995 thermodynamic (Method 4A) | When explicit Unruh temperature can be derived from the lattice dynamics (requires emergent Lorentz invariance) |
| Cao-Carroll-Michalakis (Method 6) | Full AdS/CFT (Ryu-Takayanagi) | Never for this project -- requires conformal field theory + holographic duality, which are not available on a generic lattice |
| Channel capacity argument (Route 3D) | Brandao-Horodecki (Route 3C) | When correlation decay can be established rigorously in 1D |

## What NOT to Use

| Avoid | Why | Use Instead |
|-------|-----|-------------|
| Full AdS/CFT machinery | Requires conformal field theory with large-N holographic dual; our lattice is not a CFT | Jacobson 2016 (works without holography) + CCM emergent geometry |
| Ryu-Takayanagi formula | Assumes AdS/CFT; our lattice has no "boundary" in the holographic sense | Direct entanglement entropy computation on the lattice |
| Loop quantum gravity / spin foam methods | Different program; assumes background independence from the start; incompatible with our lattice-first approach | Emergent geometry from entanglement (CCM framework) |
| String theory / compactification | Completely different framework; requires extra dimensions, supersymmetry | Our approach is self-contained: lattice -> area law -> Einstein |
| Verlinde's entropic gravity | Treats gravity as entropic force, which is a different (and debated) interpretation of Jacobson | Jacobson's original thermodynamic/entanglement equilibrium argument |

---

## Validation Strategy by Method

| Method | Validation Approach | Key Benchmarks |
|--------|-------------------|----------------|
| Lattice formalization (Method 1) | Check that the construction reproduces standard quantum lattice model properties | For M\_2(C) sites (qubits) on a chain: must reproduce Heisenberg model, transverse-field Ising, etc. |
| Lieb-Robinson (Method 2) | Verify v\_LR for specific coupling strengths; compare with known results | For nearest-neighbor coupling J: v\_LR should scale as O(J); check against exact results for XX model |
| Area law (Method 3) | Compute S(A) for small lattice numerically; verify scaling | For N-site chain with local coupling: S(half-chain) should saturate at O(1) for gapped case |
| Jacobson (Method 4) | Check that the argument reproduces GR in known limits | In continuum limit with Lorentz invariance: must recover G\_ab = 8piG T\_ab |
| Entanglement first law (Method 5) | Verify delta\_S = delta\_<H\_mod> numerically for small lattices | For 4-8 site lattice: compute both sides of the first law for random perturbations |
| Emergent geometry (Method 6) | Apply CCM to known states (e.g., ground state of Heisenberg chain); verify geometry makes sense | For 1D chain: emergent geometry should be 1D; for 2D lattice: emergent geometry should be 2D |

---

## Cost and Difficulty Assessment

| Method | Analytical Difficulty | Time Estimate | Risk |
|--------|----------------------|---------------|------|
| Lattice formalization (Method 1) | Low | 3-5 days | Low: standard framework, just instantiate with M\_n(C) |
| Lieb-Robinson bounds (Method 2) | Low (invoke known results) | 1-2 days | None: well-established theorems |
| Area law -- mutual info route (3A/3D) | **Moderate** | 1-2 weeks | **Medium**: need to identify self-modeling "equilibrium state" |
| Area law -- channel capacity (3D) | **Moderate-High** | 2-3 weeks | **Medium-High**: information-theoretic argument; need pure-state condition |
| Jacobson 2016 adaptation (4B) | **High** | 2-4 weeks | **High**: continuum-to-lattice adaptation is the hardest step |
| Entanglement first law (5) | Moderate | 1-2 weeks | Medium: well-understood QI result, but lattice H\_mod locality unclear |
| Emergent geometry (6) | Moderate | 1-2 weeks | Medium: constructive but may not produce sensible geometry |
| MERA conceptual (7) | Low (literature review) | 2-3 days | None: supporting argument only |

**Critical path:** Method 1 -> Method 2 -> Method 3 (area law) -> Method 5 (entanglement first law) -> Method 4B (Jacobson). The rate-limiting step is the area law (Method 3), specifically the bridge between self-modeling locality and the information-theoretic conditions that imply area-law scaling.

---

## The Critical Gap: Self-Modeling Locality to Area Law

This is the SINGLE MOST IMPORTANT methodological question for v3.0. The gap can be stated precisely:

**Known:** Self-modeling is local (information propagates through body-model boundaries, not telepathically).

**Need to show:** This locality implies that the entanglement entropy of any region scales as its boundary area.

**What bridges the gap (four candidates, in order of promise):**

1. **Channel capacity bound (Route 3D):** If information about region A's complement can only reach A through boundary bonds, and each bond has finite capacity, then I(A:B) <= c * |boundary(A)|. This is the cleanest argument, but requires establishing that the self-modeling fixed point is a pure state (so I(A:B) = 2 S(A)).

2. **Mutual information bound (Route 3A):** If the self-modeling fixed point is a thermal state of a local Hamiltonian, then I(A:B) <= beta * |boundary(A)| * ||h|| (WVCH 2008). Requires identifying an effective Hamiltonian for the self-modeling dynamics.

3. **Correlation decay (Route 3C):** If the self-modeling state has finite correlation length (which follows from local interactions + Lieb-Robinson), then Brandao-Horodecki gives an area law (in 1D). Requires establishing correlation decay without assuming a spectral gap.

4. **Spectral gap (Route 3B):** If the self-modeling dynamics has a unique gapped ground state, Hastings gives an area law (in 1D). Requires proving the gap exists -- the hardest of the four conditions.

**Recommendation:** Pursue Route 3D (channel capacity) as primary, with Route 3A (mutual information / WVCH) as backup. Avoid Routes 3B and 3C initially because they are restricted to 1D and require additional assumptions (gap or correlation decay) that are harder to establish than the channel capacity bound.

---

## Sources

- Jacobson, "Thermodynamics of Spacetime: The Einstein Equation of State," PRL 75, 1260 (1995). [arXiv:gr-qc/9504004](https://arxiv.org/abs/gr-qc/9504004)
- Jacobson, "Entanglement Equilibrium and the Einstein Equation," PRL 116, 201101 (2016). [arXiv:1505.04753](https://arxiv.org/abs/1505.04753)
- Hastings, "An Area Law for One Dimensional Quantum Systems," JSTAT P08024 (2007). [arXiv:0705.2024](https://arxiv.org/abs/0705.2024)
- Brandao & Horodecki, "An area law for entanglement from exponential decay of correlations," Nature Physics 9, 721 (2013). [arXiv:1309.3789](https://arxiv.org/abs/1309.3789)
- Brandao & Horodecki, "Exponential Decay of Correlations Implies Area Law," Commun. Math. Phys. 333, 761 (2015). [arXiv:1206.2947](https://arxiv.org/abs/1206.2947)
- Wolf, Verstraete, Cirac & Hastings, "Area Laws in Quantum Systems: Mutual Information and Correlations," PRL 100, 070502 (2008). [arXiv:0704.3906](https://arxiv.org/abs/0704.3906)
- Eisert, Cramer & Plenio, "Colloquium: Area laws for the entanglement entropy," Rev. Mod. Phys. 82, 277 (2010). [arXiv:0808.3773](https://arxiv.org/abs/0808.3773)
- Cao, Carroll & Michalakis, "Space from Hilbert Space: Recovering Geometry from Bulk Entanglement," PRD 95, 024031 (2017). [arXiv:1606.08444](https://arxiv.org/abs/1606.08444)
- Cao & Carroll, "Bulk Entanglement Gravity without a Boundary," PRD 97, 086003 (2018). [arXiv:1712.02803](https://arxiv.org/abs/1712.02803)
- Lashkari, McDermott & Van Raamsdonk, "Gravitational Dynamics From Entanglement 'Thermodynamics'," JHEP 04, 195 (2014). [arXiv:1308.3716](https://arxiv.org/abs/1308.3716)
- Faulkner, Guica, Hartman, Myers & Van Raamsdonk, "Gravitation from entanglement in holographic CFTs," JHEP 03, 051 (2014). [arXiv:1312.7856](https://arxiv.org/abs/1312.7856)
- Van Raamsdonk, "Building up spacetime with quantum entanglement," GRG 42, 2323 (2010). [arXiv:1005.3035](https://arxiv.org/abs/1005.3035)
- Swingle, "Entanglement Renormalization and Holography," PRD 86, 065007 (2012). [arXiv:1209.3304](https://arxiv.org/abs/1209.3304)
- Lieb & Robinson, "The finite group velocity of quantum spin systems," Commun. Math. Phys. 28, 251 (1972)
- Bravyi, Hastings & Verstraete, "Lieb-Robinson Bounds and the Generation of Correlations and Topological Quantum Order," PRL 97, 050401 (2006). [arXiv:quant-ph/0603121](https://arxiv.org/abs/quant-ph/0603121)
- Nachtergaele, Sims & Young, "Quasi-Locality Bounds for Quantum Lattice Systems," J. Math. Phys. 60, 061101 (2019). [arXiv:1810.02428](https://arxiv.org/abs/1810.02428)
- Bratteli & Robinson, "Operator Algebras and Quantum Statistical Mechanics," vols 1-2, Springer (1979, 1981)
- Anshu, Arad & Gosset, "An area law for 2D frustration-free spin systems," arXiv:2103.02492 (2021)
- Chirco, Haggard, Riello & Rovelli, "Spacetime thermodynamics without hidden degrees of freedom," PRD 90, 044044 (2014). [arXiv:1401.5262](https://arxiv.org/abs/1401.5262)
- Casini, Huerta & Myers, "Towards a derivation of holographic entanglement entropy," JHEP 1105, 036 (2011). [arXiv:1102.0440](https://arxiv.org/abs/1102.0440)

---

_Methods research for: GR from self-modeling locality -- lattice formalization, area laws, Jacobson's argument, emergent geometry_
_Researched: 2026-03-21_
