# Known Pitfalls Research

**Domain:** Quantum foundations / quantum gravity / thermodynamic gravity -- deriving Einstein's field equations from self-modeling locality via area-law entanglement and Jacobson's thermodynamic argument
**Researched:** 2026-03-21
**Confidence:** MEDIUM (Jacobson's argument is well-established; area-law literature is mature; the novel pitfalls specific to the self-modeling extension are inferred from structural analysis and require validation)

## Critical Pitfalls

### Pitfall 1: The "Which State?" Problem -- Area Laws Hold for Ground States, Not Generic States

**What goes wrong:**
Area-law theorems (Hastings 2007; Eisert, Cramer, Plenio 2010) prove that the entanglement entropy of a region A scales as |boundary(A)| for *ground states of gapped local Hamiltonians*. A generic state in the Hilbert space of a lattice system has *volume-law* entanglement -- S(A) ~ |A|, not |boundary(A)|. The self-modeling lattice must be in a specific state (or class of states) for the area law to hold. If the self-modeling dynamics do not select a state with area-law scaling, the entire chain to Jacobson breaks at step one.

**Why it happens:**
The lattice of M_n(C)^sa self-modeling systems has a Hilbert space of dimension n^N (N sites). The vast majority of states in this space satisfy volume-law entanglement (Page's theorem: a random state in a large Hilbert space has near-maximal entanglement for any subsystem). Area-law states are a measure-zero subset. The self-modeling constraint must pick out this subset, but it is not obvious that it does. The self-modeling fixed point (where M accurately tracks B at each site) is a constraint on the *local* state at each site, not a global constraint that directly controls entanglement scaling.

**How to avoid:**
Identify the specific state of the self-modeling lattice to which area-law arguments apply. The candidates are:
1. **The self-modeling fixed point as a ground state:** Argue that the self-modeling constraint defines an effective Hamiltonian whose ground state is the self-modeling fixed point. Then invoke Hastings if this Hamiltonian is gapped and local. This requires showing (a) the effective Hamiltonian exists, (b) it is local, (c) it is gapped.
2. **Information-theoretic area law:** Bypass Hamiltonian assumptions entirely. Argue from the structure of the self-modeling constraint that mutual information between distant sites decays exponentially (because information must propagate through intermediaries), and use mutual information decay to bound entanglement entropy. This is the approach of Brandao and Horodecki (2013, arXiv:1206.2947).
3. **Thermal state argument:** If the self-modeling fixed point is better characterized as a thermal state (Gibbs state) of a local Hamiltonian, area laws for thermal states are known (Wolf et al. 2008) with S(A) <= beta * |boundary(A)| * ||h||, where h is the boundary interaction strength. But this gives extensive mutual information, not the refined structure Jacobson needs.

The honest assessment: option 2 is the most promising for the self-modeling framework because it does not require constructing an explicit Hamiltonian. But it requires proving exponential correlation decay from the self-modeling constraint, which is nontrivial.

**Warning signs:**
- Invoking "area law" without specifying which state has the area law
- Citing Hastings (2007) without verifying the spectral gap and locality conditions
- Assuming the self-modeling fixed point IS a ground state without constructing the Hamiltonian
- Any argument that works equally well for volume-law states (proves nothing)

**Phase to address:** Locality formalization / Area-law derivation (the phase that proves S(A) ~ |boundary(A)|)

---

### Pitfall 2: Background Dependence Circularity -- Assuming Geometry to Derive Geometry

**What goes wrong:**
The project assumes a lattice of self-modeling systems with nearest-neighbor interactions. "Nearest neighbor" presupposes a spatial structure -- you need to know which sites are adjacent before you can define local interactions. But the goal is to *derive* spatial geometry from entanglement. If the lattice connectivity defines the geometry and the entanglement follows from the connectivity, you have not derived geometry from entanglement; you have read it back from the input.

This is the central criticism of all "emergent geometry from entanglement" programs, including Cao-Carroll-Michalakis (2017). As Ney (2018) noted: if the entangled objects are not located in a pre-defined spacetime, it is unclear why the entanglement structure should have exactly the structure compatible with three-dimensional space.

**Why it happens:**
There are two distinct claims being conflated:
(a) "Entanglement structure determines geometric structure" -- given a quantum state, you can read off a geometry from its entanglement pattern (Ryu-Takayanagi, Van Raamsdonk). This is TRUE within AdS/CFT.
(b) "Entanglement structure produces geometric structure without prior spatial input" -- the geometry was not assumed anywhere in the setup. This is a MUCH stronger claim, and it requires that the lattice connectivity itself emerges from something non-spatial.

The self-modeling project is in danger of proving (a) while claiming (b). The lattice structure is put in by hand.

**How to avoid:**
Be honest about what is and is not derived. Two options:
1. **Accept the lattice as input, derive the metric.** The lattice defines topology (which sites are connected) but not geometry (distances, curvature). Argue that the self-modeling constraint determines the entanglement structure, which determines the metric on the pre-existing topological lattice. This is a weaker but defensible claim: "self-modeling determines the geometry of spacetime given its topology."
2. **Derive the lattice from self-modeling.** Argue that the self-modeling constraint itself selects which degrees of freedom interact with which others. A self-modeling system can only model its immediate environment (because modeling distant systems requires information to propagate through intermediaries), so locality *is* the self-modeling constraint, not an additional input. This is the stronger claim and is the project's stated approach.

For option 2: the key step is showing that the lattice emerges from the algebra. The Hilbert space of N copies of M_n(C) has many possible tensor factorizations (Zanardi et al. 2004, quant-ph/0308043; Cotler et al. 2019, arXiv:1801.10168). The self-modeling constraint must select a *preferred* factorization. If it does, that factorization defines the lattice. If it does not, the lattice is an assumption and the claim of emergent geometry is overstated.

**Warning signs:**
- The lattice connectivity appears as an assumption in the premises
- "Nearest-neighbor interactions" invoked without explaining why self-modeling forces this structure
- The final geometry reproduces the input lattice structure exactly (tautology)
- No discussion of the Hilbert space factorization problem (Donnelly 2012, arXiv:1202.5334)

**Phase to address:** Locality formalization (first phase -- must establish what "local self-modeling" means without circular spatial assumptions)

---

### Pitfall 3: Jacobson's Argument Assumes a Background Smooth Manifold

**What goes wrong:**
Jacobson's 1995 derivation operates within the framework of a smooth pseudo-Riemannian manifold. It uses:
- Local Rindler horizons (requires smooth causal structure)
- Unruh temperature T = hbar * a / (2*pi*c*k_B) (requires Lorentz-invariant vacuum at short distances)
- Raychaudhuri equation for null congruences (requires differentiable geometry)
- Energy flux as boost energy of matter crossing the horizon (requires a stress-energy tensor Tab defined on the manifold)

None of these structures exist on a finite lattice of M_n(C)^sa systems. Jacobson works at the continuum level; the self-modeling lattice is discrete. Applying Jacobson to a discrete system requires either:
(a) Taking a continuum limit of the lattice, or
(b) Finding a discrete analog of Jacobson's argument

Both are highly nontrivial, and (b) does not currently exist in the literature.

**Why it happens:**
Jacobson's argument is seductively clean -- just three inputs (area-law entropy, Clausius relation, Unruh temperature) give Einstein's equations. But the argument is not a stand-alone derivation of GR; it is a *rewriting* of GR in thermodynamic language, conditional on the spacetime manifold already existing. The Raychaudhuri equation (which connects the area change of a null congruence to Ricci curvature) IS the Einstein equation in disguise. Jacobson's contribution is to identify the thermodynamic interpretation, not to derive geometry from non-geometric inputs.

This is the "reverse engineering" criticism: Jacobson does not derive GR from thermodynamics. He shows that if GR holds, its field equations can be interpreted as a thermodynamic equation of state. The derivation goes the other direction -- from the assumption that delta-Q = T*delta-S holds at every point for every Rindler horizon -- but this assumption already encodes the full Einstein equation, as Jacobson himself showed.

**How to avoid:**
The project must be clear about what Jacobson's argument provides and what it does not:
- Jacobson shows: area-law entropy + Clausius + Unruh + smooth manifold => Einstein's equations
- The project needs: self-modeling lattice => area-law entropy => ??? => Einstein's equations

The gap is the "???": how does a lattice produce a smooth manifold on which Jacobson's argument operates? This is the continuum limit problem (see Pitfall 6). The project should:
1. Establish the area law from self-modeling (independent of Jacobson)
2. Argue that the area law implies the system behaves *as if* it has a smooth manifold structure at long wavelengths (emergent continuum)
3. Apply Jacobson at the continuum level, acknowledging that the smooth manifold is emergent

This is the Wilsonian approach: the lattice defines the UV completion, the continuum arises as the IR effective description, and Jacobson's argument applies in the IR.

**Warning signs:**
- Using Jacobson's formula directly on a finite lattice
- Defining "Rindler horizon" or "Unruh temperature" on a discrete system without careful limiting arguments
- Claiming to derive Einstein's equations without a continuum limit
- Ignoring the fact that Raychaudhuri requires a differentiable manifold

**Phase to address:** Jacobson application (must establish the continuum limit before applying Jacobson)

---

### Pitfall 4: The Spectral Gap Problem -- Self-Modeling Does Not Guarantee a Gap

**What goes wrong:**
Hastings' area law (the most rigorous route to S(A) ~ |boundary(A)|) requires a spectral gap above the ground state: Delta = E_1 - E_0 > 0 for the lattice Hamiltonian. Without a gap, the area law can fail:
- Gapless systems in 1D have S ~ (c/3) * log(L), where c is the central charge (Calabrese-Cardy 2004)
- Critical systems (gapless, at phase transitions) violate the area law with logarithmic or even algebraic corrections
- In higher dimensions, gapless systems can have worse violations

The self-modeling constraint does not obviously produce a gapped system. The "effective Hamiltonian" (if one exists) whose ground state is the self-modeling fixed point might be gapless, in which case Hastings does not apply.

Furthermore, Cubitt, Perez-Garcia, and Wolf (2015, arXiv:1502.04573) proved that the spectral gap is *undecidable* for general local Hamiltonians on 2D lattices. This means there is no algorithm that, given a Hamiltonian, can determine whether it is gapped. If the self-modeling "Hamiltonian" is in this undecidable regime, proving a gap may be impossible in principle.

**Why it happens:**
The gap condition is the standard sufficient condition for area-law behavior, but it is very specific. Self-modeling is a logical/operational constraint (the model tracks the body), not a Hamiltonian one. Translating from the self-modeling constraint to a gapped Hamiltonian requires several non-obvious steps, each of which could fail.

**How to avoid:**
Consider routes to the area law that do not require a spectral gap:
1. **Exponential correlation decay:** Brandao and Horodecki (2013, arXiv:1206.2947) showed that exponential decay of correlations implies an area law in 1D, without assuming a spectral gap. If the self-modeling constraint forces exponential correlation decay (because information about distant sites is attenuated by intermediate modelings), this bypasses the gap requirement.
2. **Finite correlation length from locality:** If the self-modeling lattice has a finite correlation length xi (mutual information between sites i and j decays as exp(-|i-j|/xi)), this implies area-law entanglement by the result of Brandao-Horodecki. The self-modeling constraint might naturally produce finite xi because each site's model is limited by its local information.
3. **Assume a gap as a physical hypothesis:** State "we assume the self-modeling effective dynamics are gapped" and flag it as an open question whether this follows from the self-modeling constraint. This is honest but weakens the derivation.
4. **Use thermal state area laws:** Wolf et al. (2008) proved area laws for thermal (Gibbs) states of local Hamiltonians without a gap condition. If the self-modeling fixed point is better modeled as a thermal state, this route avoids the gap issue.

**Warning signs:**
- Citing Hastings without establishing the gap
- Assuming "local Hamiltonian implies gapped" (false -- many local Hamiltonians are gapless)
- Confusing "local interactions" with "gapped ground state"
- No discussion of what happens if the system is gapless

**Phase to address:** Area-law derivation (must either prove a gap, prove correlation decay, or use gap-free area-law results)

---

### Pitfall 5: Jacobson's Local Equilibrium Assumption Is Extremely Strong

**What goes wrong:**
Jacobson's 1995 argument requires that the expansion and shear of the null congruence vanish at the point where the Clausius relation is applied. This is the "local equilibrium" condition: the horizon is instantaneously stationary. Physically, this means the entropy is in equilibrium -- no entropy production from shear or expansion.

For a finite lattice of self-modeling systems, "local equilibrium" is not a geometric condition (there is no null congruence). It must be translated into an algebraic/information-theoretic condition. What does it mean for the self-modeling lattice to be in "local thermal equilibrium"? If the self-modeling dynamics are not in equilibrium (e.g., if the model is still updating, still converging), the Clausius relation delta-Q = T*delta-S does not hold. Instead, you get irreversible entropy production: delta-S >= delta-Q / T (Clausius inequality), which gives an inequality, not Einstein's equations.

Chirco and Liberati (2010, arXiv:0909.4194) showed that relaxing the equilibrium assumption gives f(R) gravity or other modified gravity theories, not standard GR. If the self-modeling lattice is not exactly at equilibrium, you derive *modified* gravity, which may or may not be the intended result.

**Why it happens:**
Jacobson himself acknowledged (1995 paper, final paragraph) that non-equilibrium conditions would lead to modifications of Einstein's equations. He revisited this in his 2016 "entanglement equilibrium" paper (arXiv:1505.04753), where he showed that the Einstein equation follows from the condition that vacuum entanglement entropy is *maximal* at fixed volume -- the "entanglement equilibrium" condition. This is a different (and arguably more fundamental) way to state the equilibrium requirement.

**How to avoid:**
Use Jacobson's 2016 formulation instead of the 1995 one. The 2016 version:
- Does not require Rindler horizons explicitly
- Replaces the Clausius relation with an entanglement extremality condition
- Is more naturally compatible with a lattice approach (entanglement entropy is well-defined on lattices)
- Still requires the assumption that the vacuum entanglement is maximal at fixed volume (which must be verified for the self-modeling state)

The entanglement equilibrium condition is: the entanglement entropy of a small geodesic ball is at a local maximum when the geometry varies over spacetimes with the same volume element at the center. For the self-modeling lattice, this translates to: the entanglement entropy of a lattice region is maximal (at fixed local dimension) when the self-modeling constraint is exactly satisfied. This is a testable condition.

**Warning signs:**
- Using the 1995 Clausius relation without establishing equilibrium
- Ignoring the distinction between Clausius equality and Clausius inequality
- Not discussing what happens out of equilibrium (modified gravity vs GR)
- Treating "self-modeling converged" as "thermodynamic equilibrium" without justification

**Phase to address:** Jacobson application (must establish either equilibrium or use the 2016 entanglement equilibrium formulation)

---

### Pitfall 6: The Continuum Limit Problem -- No Known Route from Finite Lattice to Smooth Manifold

**What goes wrong:**
Einstein's field equations are PDEs on a smooth 4-dimensional Lorentzian manifold: G_mu_nu + Lambda * g_mu_nu = 8*pi*G * T_mu_nu. The self-modeling system lives on a finite lattice with N sites, each carrying M_n(C)^sa. The continuum limit N -> infinity requires:
1. A notion of "lattice spacing" a that goes to zero
2. A metric g_mu_nu that emerges from the lattice data in this limit
3. Curvature (second derivatives of g) that remains finite as a -> 0
4. Diffeomorphism invariance that emerges in the limit

None of these are automatic. In lattice gauge theory (the best-understood lattice -> continuum transition), the continuum limit requires a second-order phase transition where the correlation length xi diverges as xi ~ a * (a/a_c)^(-nu). Without such a phase transition, the lattice theory does not have a continuum limit -- it remains inherently discrete.

Regge calculus (simplicial gravity) has its own problems with the continuum limit: the Einstein equations are recovered only for smooth triangulations, and lattice artifacts persist for generic triangulations (Loll 2019). Causal dynamical triangulations (CDT) recover a 4D spacetime only for specific choices of bare couplings, and even then the evidence is numerical, not analytic.

**Why it happens:**
The continuum limit is a UV completion problem. The self-modeling lattice is a UV description; GR is an IR effective theory. Connecting them requires understanding the RG flow from lattice to continuum, which is an open problem in quantum gravity. The project cannot solve this problem -- it is one of the central unsolved problems in physics.

**How to avoid:**
Accept that the continuum limit is an open problem and frame the result accordingly:
1. **Derive Einstein's equations as the leading-order effective description** of the lattice at large scales, without claiming to fully control the continuum limit. This is analogous to how lattice QCD derives the meson spectrum without proving the continuum limit rigorously.
2. **Use the Wilsonian perspective:** the lattice defines the UV, and the IR is described by whatever relevant operators survive RG flow. If the area law holds, Jacobson's argument (applied in the emergent continuum) gives Einstein's equations as the unique consistent IR dynamics.
3. **Identify the dimension D** from the lattice structure. This is Pitfall 7 below.

The honest framing is: "Given that the self-modeling lattice produces area-law entanglement and a smooth emergent spacetime (which we argue for but do not rigorously prove), Jacobson's argument gives Einstein's equations." The conditional is important.

**Warning signs:**
- Claiming to derive the continuum limit without a phase transition analysis
- Using continuum notation (integrals, derivatives, metrics) on a finite lattice
- Ignoring lattice artifacts (discretization errors that vanish only in the continuum limit)
- Not acknowledging that the continuum limit of lattice gravity is an open problem

**Phase to address:** Paper assembly (must frame the result honestly, with the continuum limit as an explicitly stated assumption or gap)

---

### Pitfall 7: The Dimension Problem -- Where Does D=4 (or Any D) Come From?

**What goes wrong:**
Jacobson's argument works in any spacetime dimension D: the Einstein equations in D dimensions follow from area-law entropy scaling as |boundary(A)| (which is a D-2 dimensional surface in a D-1 dimensional spatial slice). But the argument does not select D. The lattice of self-modeling systems also does not obviously select a dimension. A lattice with connectivity k (each site connected to k neighbors) can embed in any dimension D >= 1. The coordination number k and the spatial dimension D are independent parameters.

The project states that D=3+1 is "out of scope." This is honest. But there is a subtler problem: the area-law scaling S(A) ~ |boundary(A)| must be in the *correct* dimension for Jacobson to produce the right Einstein equations. If the lattice has D_eff = 2 (a planar graph), Jacobson gives 2+1 dimensional Einstein equations (which have no propagating gravitons). If D_eff = 4, you get 3+1 GR. The dimension enters through the Raychaudhuri equation and the relationship between Ricci tensor and Einstein tensor, both of which are dimension-dependent.

**Why it happens:**
The self-modeling constraint is algebraic, not geometric. It does not contain information about spatial dimension. The lattice connectivity (graph structure) determines the effective dimension, but the self-modeling constraint operates at each site independently. Compositionality (from Paper 5) constrains how sites interact, but not the topology of the interaction graph.

**How to avoid:**
Separate the claims:
1. "Self-modeling locality produces area-law entanglement" -- this is dimension-independent and should be stated without reference to D
2. "Area-law entanglement on a D-dimensional lattice gives D-dimensional Einstein equations via Jacobson" -- this depends on D but is a standard result once Jacobson applies
3. "The value of D is not determined by self-modeling" -- this is an honest gap

The project should note that D enters as an environmental parameter (the topology of the lattice), not as a derived quantity. This is comparable to how the Standard Model does not derive D=3+1 -- it works in D=3+1 and makes predictions there, but D is an input.

**Warning signs:**
- Claiming to derive D=3+1 from self-modeling
- Writing D=4 formulas without noting that D is an input
- Confusing "area law in D dimensions" with "area law in 3+1 dimensions" -- the scaling is different
- Not noting that Jacobson's argument gives trivial gravity (no propagating degrees of freedom) in D=2+1

**Phase to address:** Paper assembly (must state clearly that D is an input, not a prediction)

---

### Pitfall 8: The Unruh Temperature Does Not Exist on a Finite Lattice

**What goes wrong:**
Jacobson's argument requires the Unruh temperature T = hbar * a / (2*pi*c*k_B) seen by an accelerated observer near a Rindler horizon. The Unruh effect is a consequence of:
1. Lorentz invariance of the vacuum
2. The existence of the Minkowski vacuum state |0>
3. The Bisognano-Wichmann theorem (the Minkowski vacuum restricted to a Rindler wedge is a thermal state at the Unruh temperature)

None of these hold on a finite lattice:
- Lorentz invariance is broken by the lattice (it has a preferred frame)
- There is no "Minkowski vacuum" on a finite-dimensional Hilbert space -- the vacuum is a property of QFT on a continuum, not of finite-dimensional QM
- The Bisognano-Wichmann theorem applies to Haag-Kastler nets of observables (algebraic QFT), not to finite lattice systems
- The Stone-von Neumann theorem prevents canonical commutation relations on a finite-dimensional Hilbert space

The Unruh temperature is intrinsically a continuum concept. On a lattice, there is no well-defined analogue.

**Why it happens:**
The Unruh effect depends on the infinite-dimensional structure of QFT: the Minkowski vacuum is an entangled state of the left and right Rindler wedge modes, with infinitely many modes contributing. On a lattice with finite n per site, there are only finitely many modes, and the thermal nature of the reduced state is only approximate.

**How to avoid:**
This pitfall reinforces the need for a continuum limit (Pitfall 6). In addition:
1. **Use the modular Hamiltonian approach.** The Unruh temperature is related to the modular Hamiltonian K = -log(rho_A) of the reduced state. On a lattice, rho_A is well-defined (just trace out the complement), and K is well-defined (just take the matrix logarithm). The modular Hamiltonian gives a "local temperature" even on a finite lattice. Jacobson's 2016 paper uses this approach, connecting the Einstein equation to modular flow rather than to the Unruh effect directly.
2. **Show that the Unruh temperature emerges in the continuum limit.** As the lattice spacing a -> 0 with the accelerated observer's trajectory fixed, the Unruh temperature should emerge from the modular Hamiltonian. This is a well-studied problem in lattice QFT.
3. **Bypass the Unruh temperature entirely.** Jacobson's 2016 formulation (entanglement equilibrium) does not explicitly require the Unruh temperature -- it uses the entanglement entropy of small balls and the modular Hamiltonian instead. This may be a better fit for the self-modeling framework.

**Warning signs:**
- Defining "Unruh temperature" on a finite lattice without qualification
- Using T = hbar * a / (2*pi*c*k_B) for a lattice system
- Invoking the Bisognano-Wichmann theorem without checking its hypotheses (algebraic QFT axioms)
- Not discussing what replaces the Unruh effect on a lattice

**Phase to address:** Jacobson application (must either establish the continuum limit first or use the modular Hamiltonian formulation)

## Moderate Pitfalls

### Pitfall 9: Conflating Self-Modeling Locality with Hamiltonian Locality

**What goes wrong:**
Self-modeling locality means: "the model probes the body through the boundary, not telepathically through the bulk." Hamiltonian locality means: "the Hamiltonian is a sum of terms, each acting on a bounded number of nearby sites, with interaction strength decaying with distance." These are different concepts. Area-law theorems assume Hamiltonian locality (local H with bounded interaction range). Self-modeling locality is an information-processing constraint. Mapping from one to the other requires identifying:
- What is the "Hamiltonian" of the self-modeling system?
- In what sense are the interactions "local"?
- What is the interaction strength, and does it decay with distance?

If self-modeling locality does not map onto Hamiltonian locality, Hastings-type area-law theorems do not apply directly.

**How to avoid:**
The mapping requires formalizing the self-modeling constraint as a local Hamiltonian. One route: define the self-modeling "cost function" as H = sum_i h_i, where h_i measures how well site i's model tracks its body. If the model only has access to information from neighboring sites, h_i depends only on site i and its neighbors -- making H a local Hamiltonian. But this requires:
- The cost function to be a valid Hamiltonian (Hermitian, bounded below)
- The ground state of this Hamiltonian to correspond to perfect self-modeling
- The interactions to have bounded strength

Alternatively, use the information-theoretic route: self-modeling locality implies that mutual information between distant sites decays (because information propagates through intermediaries), which implies area-law entanglement via Brandao-Horodecki. This bypasses the Hamiltonian entirely.

**Warning signs:**
- Using "local" interchangeably for self-modeling and Hamiltonian senses
- Invoking Hastings without constructing the Hamiltonian
- Assuming "self-modeling is local, therefore the Hamiltonian is local"

**Phase to address:** Locality formalization (must establish the precise relationship between the two notions of locality)

---

### Pitfall 10: The Proportionality Constant Problem -- S = A/(4*G) Is Not Derived

**What goes wrong:**
Jacobson's argument derives Einstein's equations from delta-Q = T*delta-S, where S is assumed proportional to horizon area: S = eta * A, where eta is a constant. The specific value eta = 1/(4*G) (Bekenstein-Hawking) is what gives Einstein's equations with the correct Newton's constant. If eta is different, you get Einstein's equations with a different G, or a different theory entirely.

The self-modeling framework must produce the correct proportionality between entanglement entropy and area. The entanglement entropy of a lattice region is S(A) = alpha * |boundary(A)| + subleading, where alpha depends on the lattice cutoff, the local dimension n, and the interaction details. This alpha is UV-sensitive (it diverges as the lattice spacing goes to zero in QFT). The relationship between alpha and Newton's constant G is not determined by the self-modeling constraint -- it is a dynamical question about the specific Hamiltonian.

**Why it happens:**
The Bekenstein-Hawking formula S = A/(4*G*hbar) relates the UV-complete entanglement entropy to the IR gravitational coupling. This is a statement about how degrees of freedom reorganize across scales -- it connects the lattice-scale (UV) degrees of freedom to the gravitational (IR) effective description. The self-modeling framework provides the UV description but does not (and in scope, should not) determine G.

**How to avoid:**
Accept that the proportionality constant is not determined. Frame the result as:
- "Self-modeling locality produces area-law entanglement" (the scaling, not the coefficient)
- "Area-law scaling, via Jacobson, gives Einstein's equations" (with G appearing as an undetermined constant)
- "The value of G is an environmental parameter, like D" (not derivable from self-modeling)

This is explicitly stated in the project scope: "deriving the specific value of G (Newton's constant)" is out of scope.

**Warning signs:**
- Attempting to calculate G from the lattice parameters
- Setting eta = 1/(4*G) without discussing where G comes from
- Treating the proportionality constant as unimportant (it determines the strength of gravity)

**Phase to address:** Jacobson application and Paper assembly (frame the result correctly)

---

### Pitfall 11: Higher-Dimensional Area-Law Theorems Are Not as Strong as 1D

**What goes wrong:**
Hastings' rigorous area-law theorem (2007) applies only in 1D. In D > 1 spatial dimensions, the situation is:
- D=2: Area law proved only for frustration-free gapped Hamiltonians (Anshu, Arad, Gosset 2021, arXiv:2103.02492). Frustrated 2D systems remain open.
- D=3: No rigorous proof exists. There is strong numerical evidence and physical arguments, but no theorem.
- General D: The area law is a conjecture for gapped local Hamiltonians, supported by extensive numerical evidence but not proved.

If the self-modeling lattice is naturally D-dimensional with D > 1, the area-law argument rests on a conjecture, not a theorem. This weakens the chain considerably.

**How to avoid:**
Options:
1. **Work in 1D first** as a proof of concept. Show that a 1D chain of self-modeling systems has area-law entanglement (constant entropy, since boundary in 1D is zero-dimensional). Then argue by physical continuity that the result extends to higher D. This is not rigorous but is standard practice.
2. **Use the exponential correlation decay route.** Brandao-Horodecki proved the area law in 1D from exponential correlation decay, but their result has been extended to imply area-law-like bounds in higher D under stronger assumptions on correlation structure.
3. **Accept the conjecture.** State "we assume the area law conjecture holds in D dimensions" and note that this is a standard assumption in the field, believed by essentially all practitioners.

**Warning signs:**
- Citing Hastings (2007) as if it proves the area law in all dimensions
- Not distinguishing between rigorous theorems (1D) and conjectures (higher D)
- Claiming a rigorous derivation when the area law is assumed as a conjecture

**Phase to address:** Area-law derivation (must be clear about which dimension the argument is rigorous in)

---

### Pitfall 12: Jacobson Gives the Einstein Equation, Not the Full Theory

**What goes wrong:**
Jacobson's argument derives G_mu_nu + Lambda * g_mu_nu = 8*pi*G * T_mu_nu -- the classical Einstein field equation. It does NOT derive:
- Quantum corrections to gravity (graviton loops)
- Higher-curvature corrections (R^2, R_mu_nu*R^mu_nu terms)
- The path integral over geometries
- Black hole information paradox resolution
- Cosmological dynamics (Friedmann equations follow from Einstein's equations, but the cosmological constant Lambda is not determined)

The self-modeling program derives QM (Paper 5) and GR (Paper 6) at the classical/semiclassical level. It does not produce a theory of quantum gravity. Overclaiming would be to suggest that the self-modeling framework resolves deep quantum gravity puzzles.

However, Jacobson's 2016 entanglement equilibrium paper notes that departures from entanglement equilibrium (i.e., non-maximal entanglement) would give corrections to Einstein's equations. These corrections might correspond to higher-curvature terms or quantum gravity effects. This is an interesting avenue but is speculative and beyond the current scope.

**How to avoid:**
Frame Paper 6 as deriving the *classical* Einstein equation from self-modeling, at leading order in the continuum limit. Note that:
- Quantum gravity corrections are expected at the Planck scale (where the lattice structure is visible)
- Higher-curvature corrections might arise from sub-leading terms in the entanglement entropy
- The self-modeling framework provides a UV completion in principle, but extracting its predictions requires solving the continuum limit problem

**Warning signs:**
- Claiming to solve quantum gravity
- Claiming to derive the cosmological constant
- Not qualifying "Einstein's equations" with "classical" or "leading order"
- Suggesting the framework resolves the black hole information paradox

**Phase to address:** Paper assembly (appropriate framing and scope)

---

### Pitfall 13: The Hilbert Space Factorization Problem

**What goes wrong:**
Defining entanglement entropy requires a tensor product decomposition of the Hilbert space: H = H_A tensor H_B, so you can trace over B to get rho_A = Tr_B(|psi><psi|). But in gauge theories and gravitational theories, the Hilbert space does NOT factorize due to gauge constraints (Donnelly 2012, arXiv:1202.5334; Casini, Huerta, Rosabal 2014, arXiv:1312.1183).

For the self-modeling lattice, the Hilbert space is H = (C^n)^{tensor N}, which DOES factorize by construction. So the factorization problem does not arise at the lattice level. But at the continuum level (after taking the continuum limit to get something resembling QFT or quantum gravity), gauge constraints will prevent factorization, and the naive lattice entanglement entropy will not match the continuum entanglement entropy.

**Why it happens:**
The lattice regularization introduces a UV cutoff that allows factorization. In the continuum, gauge-invariant states cannot be factorized across a boundary because gauge transformations act on both sides simultaneously (Gauss's law constraint). The lattice breaks gauge invariance at the boundary, allowing factorization but introducing edge modes (Donnelly and Wall 2015, arXiv:1412.1895). These edge modes contribute to the entanglement entropy and are responsible for the UV divergence of entanglement entropy in QFT.

**How to avoid:**
For the purposes of Paper 6, this is not a blocking issue because the project works at the lattice level, where factorization holds. But the paper should:
1. Note that factorization is a feature of the lattice description
2. Acknowledge that the continuum limit will introduce gauge constraints and the factorization problem
3. Note that the edge mode / extended Hilbert space formalism (Donnelly-Wall) provides a consistent framework for entanglement entropy in gauge theories, if needed

**Warning signs:**
- Not mentioning that lattice factorization is a simplification
- Claiming that entanglement entropy is well-defined in the continuum without discussing gauge constraints
- Ignoring the extended Hilbert space / edge mode literature

**Phase to address:** Paper assembly (discussion section, limitations)

## Approximation Shortcuts

| Shortcut | Immediate Benefit | Long-term Cost | When Acceptable |
| -------- | ----------------- | -------------- | --------------- |
| Assume the self-modeling fixed point IS a ground state of some local Hamiltonian | Allows direct application of Hastings area-law theorems | May not be true; the self-modeling fixed point might be a thermal state, excited state, or not an eigenstate at all | For the initial argument (strong physical argument level), if flagged as an assumption |
| Assume 1D for area-law proofs, generalize by assertion | Use rigorous Hastings theorem instead of conjectured higher-D area law | Higher-D case is not proved; dimensional dependence of corrections unknown | Acceptable for proof-of-concept; must be flagged |
| Use Jacobson 1995 (Clausius relation) instead of 2016 (entanglement equilibrium) | Simpler argument, more widely known | Requires Rindler horizons, Unruh temperature, smooth manifold -- all problematic on a lattice | Never -- use 2016 formulation instead; it is more compatible with the lattice framework |
| Assume the lattice spacing provides a natural UV cutoff for entanglement entropy | Avoids the UV divergence of continuum entanglement entropy | The proportionality constant alpha depends on the cutoff, linking lattice parameters to G | Acceptable and probably necessary; just be explicit about it |
| Treat lattice connectivity as a proxy for spatial dimension | Avoids deriving dimensionality | The dimension D is an input, not a prediction | Acceptable (and honestly required, given scope) |
| Assume exponential correlation decay without proof | Enables Brandao-Horodecki area-law route | May not follow from self-modeling; if correlation decay is algebraic, area law may fail | Only if backed by a physical argument for why self-modeling produces short-range correlations |

## Convention Traps

| Convention Issue | Common Mistake | Correct Approach |
| ---------------- | -------------- | ---------------- |
| Entropy units: k_B vs natural units | Mixing S in k_B units with T in natural units, producing factors of k_B in wrong places | In natural units (hbar = c = k_B = 1): T_Unruh = a/(2*pi), S = A/(4*G). State this at the start and use consistently. |
| Metric signature for Jacobson's argument | Jacobson uses (-,+,+,+) for the Rindler metric. If the project uses (+,-,-,-), the Raychaudhuri equation has sign differences that affect the derivation. | Pin to Jacobson's convention (-,+,+,+) for the GR portions. Paper 5 algebraic portions are signature-independent. |
| Entanglement entropy vs thermodynamic entropy | Conflating von Neumann entropy S_vN = -Tr(rho * log(rho)) with Bekenstein-Hawking entropy S_BH = A/(4*G). These are conceptually different (entanglement vs thermal) though numerically equal for horizons. | Use S_ent for entanglement entropy, S_BH for Bekenstein-Hawking. State clearly when and why they are equated. |
| Area vs boundary area | In D spatial dimensions, "area" of the boundary of a region A means the (D-1)-dimensional measure of the boundary. In D=1 (a chain), the "area" is the number of boundary points (0 or 2). | Always specify the spatial dimension when writing |boundary(A)|. |
| Newton's constant G in D dimensions | G_D has different dimensions for different D: [G_D] = [length]^{D-2} in natural units. Jacobson's formula has dimension-dependent factors. | Use the D-dimensional formula explicitly. Do not copy 3+1 formulas for general D. |

## Numerical Traps

| Trap | Symptoms | Prevention | When It Breaks |
| ---- | -------- | ---------- | -------------- |
| Computing entanglement entropy for large lattices by exact diagonalization | Memory overflow for N > ~20 qubits; impossible for realistic lattice sizes | Use tensor network methods (MPS/DMRG for 1D, PEPS for 2D) for verification calculations | Beyond ~40 qubits for exact methods; beyond ~100 sites for DMRG in 1D |
| Extracting the area-law coefficient from finite-size data | Finite-size corrections mask the leading scaling; subleading log corrections can dominate for small systems | Use at least 3-4 system sizes and fit S(L) = alpha * L^{d-1} + beta * log(L) + gamma. Check stability of alpha as L increases. | When the subleading correction is comparable to the leading term (small systems, near criticality) |
| Verifying entanglement scaling for self-modeling lattice numerically | Requires defining and solving the self-modeling constraint for each lattice configuration -- may be computationally expensive | Start with n=2 (qubits) and small lattices (N=4-8). Check scaling before going larger. | Self-modeling constraint may not have a unique solution, producing ambiguity |
| Computing mutual information between distant sites to check correlation decay | Mutual information I(A:B) = S(A) + S(B) - S(AB) involves computing three entropies, each requiring a partial trace over a different partition | Use exact methods for small systems; for larger systems, use tensor network representations that directly give reduced density matrices | When the mutual information is very small (close to machine precision), numerical errors in the three entropy terms cancel poorly |

## Interpretation Mistakes

| Mistake | Risk | Prevention |
| ------- | ---- | ---------- |
| "Area law proved, therefore GR derived" | Skips the continuum limit, Jacobson application, and the entire chain from lattice entropy to field equations | Area law is step 1 of 3. The chain is: area law -> continuum limit -> Jacobson -> Einstein. Each step requires separate justification. |
| "Jacobson derives GR from thermodynamics" | Overstates what Jacobson showed. He showed the Einstein equation is equivalent to a thermodynamic identity, not that thermodynamics produces GR from non-gravitational inputs. | Frame correctly: "Jacobson showed that area-law entropy + Clausius + Unruh + smooth manifold = Einstein equation. We provide the area-law entropy from self-modeling; the remaining inputs come from the emergent continuum structure." |
| "Emergent geometry means we derived spacetime" | Conflates emergent metric (distances between pre-existing points) with emergent topology and dimensionality | Be precise: "emergent geometry" means the metric and curvature emerge from entanglement. The topology (lattice graph) and dimensionality are inputs. |
| "Self-modeling gives both QM and GR from one premise, so self-modeling is a theory of everything" | Overclaiming. Self-modeling does not give the Standard Model, does not determine the value of G or the cosmological constant, does not solve quantum gravity, does not explain why D=3+1. | Frame as: "Self-modeling, given the lattice topology and dimension, derives the algebraic structure (M_n(C)^sa), entanglement scaling (area law), and dynamics (Einstein equations) from a single operational premise." |

## Publication Pitfalls

| Pitfall | Impact | Better Approach |
| ------- | ------ | --------------- |
| Claiming GR derived without a continuum limit | Referees will immediately reject; the gap between lattice and continuum is well-known | Present as "strong physical argument" with the continuum limit as an explicit gap to be closed in future work |
| Not engaging with the background dependence criticism | Referees working on emergent geometry will ask this immediately | Address explicitly: "The lattice topology is an input; the metric is derived" |
| Ignoring the "which state?" problem | The most technically serious objection to the area-law step | Identify the state, justify why it has area-law entanglement, and discuss sensitivity to state choice |
| Not distinguishing the project from Van Raamsdonk / ER=EPR / Swingle | Referees will ask "how is this different from existing emergent gravity programs?" | The novel contribution is the self-modeling premise: locality is derived from the operational constraint, not postulated. Other programs assume locality / AdS structure. |
| Claiming the Unruh effect holds on a lattice | Well-known to be problematic (Stone-von Neumann, no Lorentz invariance on lattice) | Use the modular Hamiltonian approach, which is well-defined on lattices |

## "Looks Correct But Is Not" Checklist

- [ ] **Area-law claim:** Often missing the hypothesis that the state must be a ground state (or thermal state) of a gapped (or local) Hamiltonian -- verify the state is identified and the conditions are checked
- [ ] **Jacobson application:** Often missing the smooth manifold assumption -- verify that either a continuum limit is taken or the argument is adapted to a lattice
- [ ] **Unruh temperature on lattice:** Often stated as T = a/(2*pi) without checking whether the Unruh effect holds in the discrete setting -- verify using modular Hamiltonian instead
- [ ] **"Locality implies area law":** Often missing the gap condition -- verify either a spectral gap or exponential correlation decay is established
- [ ] **Entanglement entropy proportional to area:** Often missing the UV sensitivity -- verify the proportionality constant is treated correctly (not set to 1/(4G) without justification)
- [ ] **Emergent geometry from entanglement:** Often circular (geometry put in through lattice connectivity, read out through entanglement) -- verify the argument adds something beyond the input
- [ ] **D-dimensional formulas:** Often copied from D=3+1 without checking D-dependence -- verify all dimension-dependent factors are correct for general D

## Recovery Strategies

| Pitfall | Recovery Cost | Recovery Steps |
| ------- | ------------- | -------------- |
| "Which state?" problem -- area law fails for the self-modeling state (Pitfall 1) | HIGH | Must either (a) identify a different state (thermal, ground, or other) to which the area law applies, or (b) find a different route to Jacobson that does not require area-law entanglement. Option (b) is the Jacobson 2016 entanglement equilibrium approach, which requires entanglement maximality rather than area-law scaling. |
| Background dependence circularity (Pitfall 2) | MEDIUM | Weaken the claim from "emergent geometry" to "emergent metric on a pre-existing lattice topology." This is still a meaningful result. |
| Jacobson requires smooth manifold (Pitfall 3) | MEDIUM-HIGH | Develop a discrete version of Jacobson's argument, or frame the result as "in the continuum limit, Jacobson applies." The 2016 entanglement equilibrium formulation may be more adaptable. |
| Spectral gap not established (Pitfall 4) | MEDIUM | Use the Brandao-Horodecki route (exponential correlation decay implies area law). This shifts the burden from proving a gap to proving correlation decay. |
| Equilibrium assumption fails (Pitfall 5) | MEDIUM | Switch to Jacobson 2016 formulation. The entanglement equilibrium condition may be more naturally satisfied by the self-modeling fixed point than the thermodynamic equilibrium of the 1995 argument. |
| Continuum limit not controlled (Pitfall 6) | HIGH | This is an open problem in quantum gravity. Frame the result as conditional: "given that a smooth spacetime emerges in the continuum limit..." |
| D not determined (Pitfall 7) | LOW | Accept D as an input. This is not a weakness -- it is an honest scope boundary. |
| Unruh temperature undefined on lattice (Pitfall 8) | MEDIUM | Use modular Hamiltonian / entanglement equilibrium. Well-defined on lattices. |

## Pitfall-to-Phase Mapping

| Pitfall | Prevention Phase | Verification |
| ------- | ---------------- | ------------ |
| P1: "Which state?" problem | Area-law derivation | Specific state identified; area-law scaling verified for that state |
| P2: Background dependence circularity | Locality formalization | Lattice structure derived from self-modeling or honestly acknowledged as input |
| P3: Jacobson requires smooth manifold | Jacobson application | Continuum limit discussed; Jacobson applied at continuum level |
| P4: Spectral gap not guaranteed | Area-law derivation | Gap established, or gap-free area-law route used (Brandao-Horodecki) |
| P5: Local equilibrium too strong | Jacobson application | Equilibrium established, or 2016 entanglement equilibrium used |
| P6: Continuum limit open problem | Paper assembly | Framed as explicit gap/assumption, not glossed over |
| P7: D not determined | Paper assembly | D stated as input, not prediction |
| P8: Unruh temperature on lattice | Jacobson application | Modular Hamiltonian used instead of Unruh temperature |
| P9: Self-modeling locality vs Hamiltonian locality | Locality formalization | Mapping between the two established or information-theoretic route used |
| P10: Proportionality constant undetermined | Jacobson application + Paper assembly | G appears as undetermined constant; flagged as out of scope |
| P11: Higher-D area law is conjecture | Area-law derivation | Dimension of rigorous result stated; higher-D treated as physical argument |
| P12: Classical Einstein only | Paper assembly | Framed as "classical leading order" derivation |
| P13: Hilbert space factorization | Paper assembly | Noted as lattice simplification; continuum issues acknowledged |

## Sources

- Jacobson (1995), "Thermodynamics of Spacetime: The Einstein Equation of State," PRL 75, 1260, arXiv:gr-qc/9504004 -- original thermodynamic derivation
- Jacobson (2016), "Entanglement Equilibrium and the Einstein Equation," PRL 116, 201101, arXiv:1505.04753 -- improved derivation using entanglement equilibrium, more compatible with lattice approaches
- Hastings (2007), "An area law for one-dimensional quantum systems," JSTAT P08024, arXiv:0705.2024 -- rigorous 1D area law
- Eisert, Cramer, Plenio (2010), "Colloquium: Area laws for the entanglement entropy," Rev. Mod. Phys. 82, 277, arXiv:0808.3773 -- comprehensive review of area laws
- Brandao and Horodecki (2013), "An area law for entanglement from exponential decay of correlations," Nature Physics 9, 721, arXiv:1206.2947 -- area law from correlation decay (no gap needed)
- Calabrese and Cardy (2004), "Entanglement entropy and quantum field theory," JSTAT P06002, arXiv:hep-th/0405152 -- logarithmic violations of area law in critical 1D systems
- Cao, Carroll, Michalakis (2017), "Space from Hilbert Space: Recovering Geometry from Bulk Entanglement," PRD 95, 024031, arXiv:1606.08444 -- emergent geometry from entanglement
- Carroll and Singh (2019), "Towards Space from Hilbert Space: Finding Lattice Structure in Finite-Dimensional Quantum Systems," arXiv:1801.10168 -- lattice structure from finite-dimensional QM
- Chirco and Liberati (2010), "Non-equilibrium thermodynamics of spacetime: The role of gravitational dissipation," PRD 81, 024016, arXiv:0909.4194 -- non-equilibrium Jacobson
- Van Raamsdonk (2010), "Building up spacetime with quantum entanglement," GRG 42, 2323, arXiv:1005.3035 -- entanglement and geometry
- Lashkari, McDermott, Van Raamsdonk (2014), "Gravitational dynamics from entanglement thermodynamics," JHEP 04, 195, arXiv:1308.3716 -- linearized Einstein from entanglement
- Donnelly (2012), "Decomposition of entanglement entropy in lattice gauge theory," PRD 85, 085004, arXiv:1109.0036 -- Hilbert space factorization in gauge theory
- Donnelly and Wall (2015), "Entanglement entropy of electromagnetic edge modes," PRL 114, 111603, arXiv:1412.1895 -- edge modes and factorization
- Cubitt, Perez-Garcia, Wolf (2015), "Undecidability of the Spectral Gap," Nature 528, 207, arXiv:1502.04573 -- undecidability of spectral gap
- Wolf, Verstraete, Hastings, Cirac (2008), "Area Laws in Quantum Systems: Mutual Information and Correlations," PRL 100, 070502, arXiv:0704.3906 -- thermal state area laws
- Anshu, Arad, Gosset (2021), "An area law for 2D frustration-free spin systems," arXiv:2103.02492 -- 2D area law (frustration-free case)
- Zanardi, Lidar, Lloyd (2004), "Quantum Tensor Product Structures are Observable-Induced," PRL 92, 060402, arXiv:quant-ph/0308043 -- non-uniqueness of tensor product structure

---

_Known pitfalls research for: GR from self-modeling locality via area-law entanglement and Jacobson's thermodynamic argument_
_Researched: 2026-03-21_
