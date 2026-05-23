# Phase 8: Locality Formalization - Research

**Researched:** 2026-03-21
**Domain:** Quantum lattice systems / Operator algebras / Lieb-Robinson bounds / Self-modeling locality
**Confidence:** MEDIUM-HIGH

## Summary

Phase 8 must translate the abstract notion of "self-modeling locality" -- that a model subsystem (M) can probe its body (B) only through a shared boundary, not through the bulk -- into a precise quantum lattice system in the Bratteli-Robinson framework. The output is a concrete Hamiltonian H on a graph with M_n(C) local algebras and a computed Lieb-Robinson velocity v_LR.

The mathematical framework is well-established (40+ years of quantum lattice systems), and the Lieb-Robinson bound computation is standard for finite-range interactions. The novel and challenging part is the **mapping step**: translating the self-modeling B-M boundary coupling from the OUS/EJA framework of Paper 5 into an interaction Hamiltonian h_{xy} on the lattice. This mapping is the phase's core intellectual contribution and its primary risk.

**Primary recommendation:** Define the lattice in the standard Bratteli-Robinson framework with A_x = M_n(C) at each site, nearest-neighbor interactions h_{xy} constructed from the Paper 5 composite sequential product acting across shared B-M boundaries, and compute v_LR using the Nachtergaele-Sims bound v_LR = 2||Phi||_a C_a / a. The interaction Hamiltonian should be constrained by requiring that the two-site reduced dynamics reproduce the Paper 5 composite OUS structure (a tensor b) & (c tensor d) = (a & c) tensor (b & d).

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| --- | --- | --- | --- | --- |
| ref-paper5 (Paper 5, v2.0) | prior artifact | Provides M_n(C)^sa per site, local tomography dim(V_BM) = dim(V_B) * dim(V_M), composite OUS with product-form SP, Luders product | read, use, cite | plan, execution, verification |
| Bratteli-Robinson (1979/1981) | method | Standard framework for quantum lattice systems: quasi-local algebra, local Hamiltonians, infinite-volume limit | read, cite | plan, execution |
| Lieb-Robinson (1972) | benchmark | Original finite group velocity result; template for v_LR computation | cite | execution, verification |
| Nachtergaele-Sims (2006, 2019) | method | Modern formulation of LR bounds with explicit constants; exponential clustering theorem | read, cite | execution, verification |
| Bravyi-Hastings-Verstraete (2006) | method | Entanglement generation rate scales as boundary area; connects LR bounds to area-law intuition | cite | execution |
| Barnum-Wilce (2012), arXiv:1202.4513 | method | Local tomography forces M_n(C)^sa; provides the composite dimension counting used in Paper 5 | cite | execution |

**Missing or weak anchors:** No published work maps self-modeling B-M boundary coupling to a specific Hamiltonian interaction. This mapping is novel and has no external anchor. The phase must construct it from first principles, constrained by the Paper 5 composite OUS axioms (C1-C4) and the product-form sequential product.

## Conventions

| Choice | Convention | Alternatives | Source |
| --- | --- | --- | --- |
| Unit system | Natural (hbar = c = k_B = 1) | SI, lattice units | Project SUMMARY.md |
| Metric signature | (-,+,+,+) | (+,-,-,-) | Project SUMMARY.md, following Wald |
| Sequential product notation | a & b (non-commutative) | a . b, a o b | Project conventions (vdW arXiv:1803.11139 Def. 2) |
| Jordan product | a * b = (1/2)(a & b + b & a) | a circ b | Project conventions |
| Composite product | (a tensor b) & (c tensor d) = (a & c) tensor (b & d) | -- | Paper 5, Eq. 05-01.1 |
| Local algebra | A_x = M_n(C) (full matrix algebra) | A_x^sa = M_n(C)^sa (self-adjoint part) | Bratteli-Robinson (A_x is the full algebra; Paper 5 works with the self-adjoint part) |
| Lattice graph | G = (V, E) abstract, unspecified topology | Z^d, finite subset of Z^d | Phase 8 input; topology not derived |
| Hamiltonian sign | H = sum_{<x,y>} h_{xy}, ground state minimizes energy | H = -sum... (opposite sign) | Standard condensed matter convention |
| Energy scale | Set ||h_{xy}|| = J (coupling constant) | Dimensionless, arbitrary | Natural choice for LR velocity computation |
| Entropy base | Nats (ln) | Bits (log_2) | Project CONVENTIONS.md |

**CRITICAL: All equations and results below use these conventions. The local algebra A_x = M_n(C) is the FULL matrix algebra; the self-adjoint part A_x^sa = M_n(C)^sa is the OUS/EJA from Paper 5. The Hamiltonian is self-adjoint (h_{xy} in A_{xy}^sa) but lives in the full tensor product algebra A_{xy} = A_x tensor A_y = M_n(C) tensor M_n(C) = M_{n^2}(C).**

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in This Phase |
| --- | --- | --- | --- |
| A_x = M_n(C), A_R = bigotimes_{x in R} A_x | Local and regional algebra | Bratteli-Robinson Ch. 6.2 | Foundation: defines the algebraic structure at each site |
| H = sum_{<x,y> in E} h_{xy}, h_{xy} in A_{xy}^sa | Nearest-neighbor Hamiltonian | Standard | The interaction to be constructed from self-modeling coupling |
| (a tensor b) & (c tensor d) = (a & c) tensor (b & d) | Product-form sequential product | Paper 5, composite-lt.tex Eq. (5.2) | Constrains the form of h_{xy}: two-site dynamics must reproduce this product structure |
| a & b = sum_i lambda_i C_{p_i}(b) + sum_{i<j} sqrt(lambda_i lambda_j) P_{ij}(b) | Corrected SP with Peirce 1-space | Phase 4 derivation 04-peirce-feedback-extension | The single-site sequential product that h_{xy} must encode |
| \|\|[A(t), B]\|\| <= 2\|\|A\|\| \|\|B\|\| g_a(t) sum_{x in X, y in Y} F_a(d(x,y)) | Lieb-Robinson bound | Nachtergaele-Sims (2019), Theorem 3.4 equivalent | The bound to be computed with explicit constants for the self-modeling Hamiltonian |
| v_LR = 2\|\|Phi\|\|_a C_a / a | Lieb-Robinson velocity | Nachtergaele-Sims; see also arXiv:1011.4540 Corollary 3.5 | The velocity to be computed explicitly |
| dS(R)/dt <= c * \|boundary(R)\| | Entanglement generation rate | Bravyi-Hastings-Verstraete (2006), PRL 97, 050401 | Connects LR bounds to area-law intuition; not directly used but motivates Phase 9 |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --- | --- | --- | --- |
| Bratteli-Robinson lattice construction | Assigns local algebras to vertices, defines quasi-local algebra as norm closure of union of regional algebras | Defining the lattice formally | Bratteli-Robinson vols. 1-2 |
| Interaction Phi as a map from finite subsets to local observables | Encodes the Hamiltonian as Phi(X) in A_X for each finite subset X; ||Phi|| controls LR velocity | Defining the interaction and computing v_LR | Nachtergaele-Sims (2019) |
| Spectral decomposition of M_n(C)^sa elements | Writes effects as a = sum_i lambda_i p_i with spectral projections; needed for the corrected SP formula | Constructing h_{xy} from the sequential product | Alfsen-Shultz, Geometry of State Spaces |
| Partial trace / reduced state | Traces out subsystems to get local density matrices; needed to verify consistency of h_{xy} with Paper 5 composite | Verification that lattice reproduces Paper 5 structure | Standard quantum information |
| F-function and convolution constant computation | Defines the decay function F_a(r) = e^{-ar}/(1+r)^{nu+epsilon} on the lattice; C_a = sup_x sum_y F_a(d(x,y)) is the convolution constant | Computing v_LR explicitly | Nachtergaele-Sims (2019) |

### Approximation Schemes

| Approximation | Small Parameter | Regime of Validity | Error Estimate | Alternatives if Invalid |
| --- | --- | --- | --- | --- |
| Nearest-neighbor truncation | Interaction range / system size | Exact if self-modeling coupling is strictly nearest-neighbor | No error (exact) | Include next-nearest-neighbor terms; LR bounds still apply |
| Finite lattice (N sites) | 1/N | Exact for finite N; infinite-volume properties require limit | Finite-size corrections ~ 1/N or exponentially small | Take thermodynamic limit via Bratteli-Robinson infinite-volume construction |
| n = 2 (qubits) | 1/n | Simplest case; captures all essential physics | Missing higher-spin effects | General n; results should be stated for general n, computed for n = 2 |

## Standard Approaches

### Approach 1: Bratteli-Robinson Lattice + Constrained Hamiltonian (RECOMMENDED)

**What:** Construct the lattice in the standard Bratteli-Robinson framework. The self-modeling constraint determines the form of h_{xy} by requiring that the two-site dynamics reproduce the Paper 5 composite OUS.

**Why standard:** The Bratteli-Robinson framework is the universal language for quantum lattice systems. Every result on area laws, Lieb-Robinson bounds, and quantum lattice dynamics is formulated in this language. Using it ensures compatibility with all downstream references (Hastings, WVCH, Brandao-Horodecki, Jacobson).

**Track record:** Used in every mathematical result on quantum spin systems since the 1970s. The framework handles arbitrary finite-dimensional local algebras (M_n(C) is the paradigmatic case), arbitrary lattice graphs, and arbitrary finite-range interactions.

**Key steps:**

1. **Define the lattice graph G = (V, E).** V is the set of sites (self-modeling systems). E encodes which pairs of sites share a B-M boundary. For now, G is abstract (topology is input, not derived -- acknowledged as Pitfall 2 in PITFALLS.md). State results for general G; compute examples for G = Z^1 (chain) and G = Z^2 (square lattice).

2. **Assign local algebras.** A_x = M_n(C) at each site x in V. The self-adjoint part A_x^sa = M_n(C)^sa is the EJA from Paper 5. For two adjacent sites {x,y} in E, the two-site algebra is A_{xy} = M_n(C) tensor M_n(C) = M_{n^2}(C).

3. **Construct h_{xy} from the self-modeling coupling.** This is the novel step. The self-modeling constraint says that neighboring sites interact through their shared B-M boundary via the product-form sequential product. The interaction Hamiltonian h_{xy} must be the self-adjoint element of A_{xy} that generates (in the Heisenberg picture) the dynamics consistent with the composite sequential product. Concretely: the sequential product a & b on a single site involves the Luders/compression map C_a(b) = a^{1/2} b a^{1/2} (in the M_n(C)^sa representation). The two-site coupling h_{xy} should encode the "measurement-like" interaction where site x's effect a acts on site y's state via the compression. This means h_{xy} encodes the Luders channel of the boundary interaction.

4. **Verify consistency with Paper 5.** Check that the two-site reduced dynamics under H reproduce the composite OUS axioms (C1-C4) and the product-form SP: (a tensor b) & (c tensor d) = (a & c) tensor (b & d). This is a non-trivial consistency check.

5. **Compute the Lieb-Robinson velocity.** Given ||h_{xy}|| = J (the coupling strength), use the Nachtergaele-Sims formula: choose the F-function F_a(r) = e^{-ar} for the lattice, compute the convolution constant C_a = sup_x sum_{y: d(x,y)>=1} e^{-a*d(x,y)}, and obtain v_LR = 2J * C_a / a. Optimize over a to get the tightest bound.

6. **Verify dimensional consistency.** H has dimensions of energy. h_{xy} has dimensions of energy. J = ||h_{xy}|| has dimensions of energy. v_LR = 2J * C_a / a has dimensions of energy * (lattice spacing) / (decay rate) = [E][L] if we restore lattice spacing. In natural units with lattice spacing a_lat = 1, v_LR has units of energy = 1/time, consistent with a velocity (in natural units with lattice spacing = 1).

**Known difficulties at each step:**

- Step 1: The lattice graph is input, creating background dependence (Pitfall P2). This is acknowledged and deferred -- topology is not derived.
- Step 3: **The critical difficulty.** The mapping from the abstract sequential product to a concrete Hamiltonian is not unique. The sequential product a & b is a bilinear map on M_n(C)^sa, but many Hamiltonians can generate the same effective dynamics at short times. The phase must identify the constraints that pin down h_{xy} (or characterize the family of compatible Hamiltonians).
- Step 4: The verification requires comparing an algebraic structure (OUS with SP) to a dynamical one (Heisenberg evolution under H). The correspondence may hold exactly only at short times or in a specific limit.
- Step 5: The LR velocity is an upper bound, not a tight bound. The actual propagation speed may be slower.

### Approach 2: Direct Information-Theoretic Lattice (FALLBACK)

**What:** Skip the Hamiltonian and define locality purely in information-theoretic terms: site x has mutual information only with its neighbors; all correlations decay with graph distance.

**When to switch:** If the mapping from self-modeling coupling to a Hamiltonian proves impossible (the self-modeling dynamics cannot be captured by a time-independent Hamiltonian) or if the Hamiltonian is not unique and uniqueness is needed for Phase 9.

**Tradeoffs:** Gains simplicity and avoids the Hamiltonian construction problem. Loses the ability to compute v_LR (no Hamiltonian means no Heisenberg evolution), making success criterion 3 (explicit v_LR) unachievable. Also loses compatibility with Hastings' area-law theorem (which requires a gapped Hamiltonian). The channel capacity route (Route 3D from METHODS.md) remains available.

### Anti-Patterns to Avoid

- **Writing down a Hamiltonian by analogy without justification:** Do not say "h_{xy} looks like a Heisenberg interaction" because the self-modeling coupling is not a spin-spin interaction. The form of h_{xy} must be derived from the Paper 5 composite structure.
  - _Example:_ Writing h_{xy} = J * (sigma_x dot sigma_y) without explaining why the self-modeling constraint produces this specific form would be unjustified false progress.

- **Conflating self-modeling locality with Hamiltonian locality without proof:** The two notions are structurally different (one is operational/information-theoretic, the other is algebraic). The mapping is the core of this phase, not an assumption.
  - _Example:_ Stating "self-modeling is local, therefore H has nearest-neighbor interactions" skips the proof.

- **Citing Lieb-Robinson bounds without computing v_LR:** The contract explicitly forbids this as a false progress proxy. v_LR must be computed from the specific interaction.

## Existing Results to Leverage

**This section is MANDATORY.** The following results should be CITED rather than re-derived.

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
| --- | --- | --- | --- |
| Paper 5: Self-modeling forces M_n(C)^sa | V is an EJA; local tomography excludes R, H, O types; only M_n(C)^sa survives | Paper 5 (v2.0), derivations 05-type-exclusion-and-cstar.md | Input: each site's algebra is fixed. No need to re-argue this. |
| Paper 5: Composite OUS axioms (C1-C4) | V_BM contains V_B tensor V_M, with order unit 1_BM = 1_B tensor 1_M, product states, non-signaling | Paper 5, composite-lt.tex Def. 5.1 | Input: constrains the two-site structure. |
| Paper 5: Product-form SP inherits S1-S7 | If factor SPs satisfy S1-S7, composite SP satisfies S1-S7 | Paper 5, composite-lt.tex Prop. 5.2 | Input: the composite is again an EJA. |
| Lieb-Robinson bound (general form) | \|\|[A(t), B]\|\| <= 2\|\|A\|\| \|\|B\|\| min[1, C_a^{-1}(e^{2\|\|Phi\|\|_a C_a \|t\|} - 1) sum_{x,y} F_a(d(x,y))] | Nachtergaele-Sims, arXiv:1810.02428 | Invoke with specific Phi; do not re-derive the bound itself. |
| LR velocity formula | v_LR = 2\|\|Phi\|\|_a C_a / a | Nachtergaele-Sims; arXiv:1011.4540 Cor. 3.5 | Plug in specific interaction norm and lattice convolution constant. |
| Bratteli-Robinson quasi-local algebra | A = norm-closure of union of A_R for finite R; UHF algebra for M_n(C) sites | Bratteli-Robinson vol. 2, Ch. 6.2 | Cite the framework; do not re-construct the C*-algebra theory. |
| Entanglement generation rate | dS(R)/dt <= c * \|boundary(R)\| for local Hamiltonians | Bravyi-Hastings-Verstraete (2006), PRL 97, 050401 | Cite as motivation for area-law; do not re-derive. |
| Exponential clustering for gapped ground states | \|<A B> - <A><B>\| <= C \|\|A\|\| \|\|B\|\| e^{-d(A,B)/xi} with xi ~ v_LR/Delta | Nachtergaele-Sims (2006), CMP 265, 119 | Invoke if gap is established; do not re-derive. |

**Key insight:** The Lieb-Robinson bound and exponential clustering theorem are deep results with multi-page proofs. This phase should invoke them as black boxes with the specific interaction parameters plugged in. The novel work is constructing the interaction, not re-proving the bounds.

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
| --- | --- | --- | --- |
| Luders product in M_n(C)^sa | a & b = a^{1/2} b a^{1/2} (the concrete form of the SP in the C*-algebra representation) | Alfsen-Shultz; also Phase 4 derivation 04-sequential-product-definition.md | Valid for M_n(C)^sa; this IS the sequential product after type exclusion |
| Corrected SP with Peirce feedback | a & b = sum_i lambda_i C_{p_i}(b) + sum_{i<j} sqrt(lambda_i lambda_j) P_{ij}(b) | Phase 4, derivation 04-peirce-feedback-extension.md | General form on EJA; reduces to Luders product on M_n(C)^sa |
| Two-site algebra structure | M_n(C) tensor M_n(C) = M_{n^2}(C) | Standard algebra | The two-site algebra is again a full matrix algebra |
| F-function on Z^d | F_a(r) = e^{-ar}/(1+r)^{d+epsilon}, C_a = sup_x sum_{y != x} F_a(d(x,y)) | Nachtergaele-Sims (2019) | For Z^d lattice; C_a is finite for all a > 0 |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| --- | --- | --- | --- | --- |
| Operator Algebras and QSM (vols. 1-2) | Bratteli, Robinson | 1979/1981 | Definitive reference for quantum lattice systems | Framework: local algebras, interactions, dynamics |
| Quasi-Locality Bounds Part I | Nachtergaele, Sims, Young | 2019 | Modern unified treatment of LR bounds | Explicit bound formula, F-function framework, velocity computation |
| Lieb-Robinson Bounds and Exponential Clustering | Nachtergaele, Sims | 2006 | Gap implies exponential clustering via LR bounds | Theorem statement for downstream use in Phase 9 |
| LR Bounds and Generation of Correlations | Bravyi, Hastings, Verstraete | 2006 | Entanglement rate scales with boundary | Area-law rate result, motivation |
| Local Tomography and Jordan Structure | Barnum, Wilce | 2012 | Local tomography forces complex quantum theory | Composite dimension counting, type exclusion |
| Tightening the LR Bound | Wang, Hazzard | 2019 | Improved v_LR that grows slower with local dimension | Tighter velocity bound: v_LR improved by factor ~1/log(d) for large local dim d |

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
| --- | --- | --- | --- |
| NumPy | numpy.linalg | Matrix operations, spectral decomposition of h_{xy} | Universal numerical linear algebra |
| SciPy | scipy.linalg, scipy.sparse.linalg | Sparse Hamiltonian construction, ground state via Lanczos | Standard for exact diagonalization |
| SymPy | sympy.matrices, sympy.physics.quantum | Symbolic construction of h_{xy} from the sequential product | Symbolic algebra for verifying consistency |

### Supporting Tools

| Tool | Purpose | When to Use |
| --- | --- | --- |
| matplotlib | Visualize LR light cone, lattice structure | Illustration of v_LR cone; lattice diagrams for paper |
| QuTiP | Partial trace, tensor products | If needed for entanglement verification of two-site states |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
| --- | --- | --- |
| NumPy (dense) | SciPy sparse | Sparse only needed for N > 10 sites; for two-site consistency checks, dense is simpler |
| SymPy (symbolic h_{xy}) | Manual algebra | SymPy prevents algebraic errors in composing the SP; worth the setup cost |

### Computational Feasibility

| Computation | Estimated Cost | Bottleneck | Mitigation |
| --- | --- | --- | --- |
| Two-site Hamiltonian construction (n=2) | 4x4 matrix algebra, milliseconds | None | Trivial |
| Two-site Hamiltonian construction (general n) | n^2 x n^2 matrix algebra, seconds | None for n <= 10 | Use SymPy for symbolic |
| Verification: two-site dynamics vs. composite SP | Matrix exponential of 4x4 (n=2), seconds | None | NumPy expm |
| v_LR computation for Z^d lattice | Sum over lattice sites (convergent series), seconds | None | Analytical formula for Z^d |

**Installation / Setup:**
```bash
# Standard scientific Python -- likely already installed
pip install numpy scipy sympy matplotlib
# Optional, only if entanglement entropy checks needed:
pip install qutip
```

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| --- | --- | --- | --- |
| Two-site SP reproduction | h_{xy} generates the correct composite sequential product | Compute e^{iHt} (a tensor b) e^{-iHt} at short times; compare to (a & c) tensor (b & d) structure | Agreement to O(t^2) at minimum |
| Self-adjointness of h_{xy} | Hamiltonian is Hermitian | Check h_{xy} = h_{xy}^dagger | Exact |
| Dimensional analysis of v_LR | v_LR has correct units | v_LR = 2J * C_a / a; [J] = energy, [C_a] = dimensionless, [a] = 1/length; [v_LR] = energy * length = velocity (natural units) | Correct dimensions |
| Locality: h_{xy} supported on sites {x,y} only | Interaction is truly nearest-neighbor | Verify h_{xy} in A_{xy} = M_n(C) tensor M_n(C), not in larger algebra | Exact |
| Paper 5 composite axioms (C1-C4) | Lattice two-site structure matches Paper 5 | Verify product states, non-signaling, order unit, for the lattice two-site system | Must match exactly |
| Trace preservation | Two-site dynamics preserves normalization | Tr(e^{-iHt} rho e^{iHt}) = 1 | Exact (unitary evolution) |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| --- | --- | --- | --- |
| Single site (no interactions, J = 0) | H = 0 | v_LR = 0; no propagation; each site independent | Trivial |
| Two sites only (N = 2) | Exact two-body problem | Full dynamics analytically solvable; LR bound trivially saturated | Standard QM |
| Heisenberg model benchmark | h_{xy} = J (sigma_x dot sigma_y) on Z^1 | v_LR = 2eJ for d=1 with F(r) = e^{-r}; known area-law ground state | Lieb-Robinson (1972); standard benchmark |
| Large n limit | n -> infinity, fixed J | v_LR may grow with n (Wang-Hazzard: improved bound grows as O(sqrt(n))) | Wang-Hazzard (2019), arXiv:1908.03997 |
| Product state (no entanglement) | t = 0, initial product state | S(A) = 0 for any A; entanglement grows linearly in time at rate <= c * |boundary(A)| | Bravyi-Hastings-Verstraete (2006) |

### Numerical Validation

| Test | Method | Tolerance | Reference Value |
| --- | --- | --- | --- |
| Heisenberg chain v_LR | Compute from formula; compare to known | Exact match to formula | v_LR = 2eJ for nearest-neighbor on Z^1 with exponential F-function |
| Two-site dynamics | Time-evolve under h_{xy}; compare to SP | Relative error < 1e-10 | Exact agreement at t=0; O(t^2) corrections at finite t |
| Ground state entanglement (benchmark) | ED of Heisenberg chain N=16, compute S(L/2) | Match known S ~ 0.69 (= ln 2) for half-chain | Laflorencie (2016), Phys. Rep. 646, 1 |

### Red Flags During Computation

- If h_{xy} is not self-adjoint, the Hamiltonian is not Hermitian -- unitarity is broken; the construction is wrong.
- If v_LR diverges, the interaction norm ||Phi|| is infinite -- the interaction is not bounded or the F-function was chosen incorrectly.
- If the two-site dynamics under h_{xy} violate non-signaling (measuring at site x changes the reduced state at site y instantaneously), the interaction is non-local -- contradicts the self-modeling locality premise.
- If h_{xy} = 0 (the only compatible Hamiltonian is trivial), self-modeling does not actually produce any interaction -- the lattice is a product state with no entanglement, and the chain to GR collapses.
- If the family of compatible Hamiltonians is parametrically large (many free parameters), the construction is underdetermined -- must then check whether area-law results are robust across the family (backtracking trigger from the contract).

## Common Pitfalls

### Pitfall 1: Conflating Self-Modeling Locality with Hamiltonian Locality

**What goes wrong:** Assuming that "self-modeling is local" automatically means "the Hamiltonian has nearest-neighbor interactions" without proving the correspondence. These are structurally different claims: self-modeling locality is an operational/information-theoretic statement about what a model can access; Hamiltonian locality is an algebraic statement about the support of interaction terms.

**Why it happens:** The words "local" and "locality" are used in both contexts, creating a false sense of equivalence. In self-modeling, "local" means "the model probes only the boundary." In the Hamiltonian framework, "local" means "interaction terms are supported on bounded subsets."

**How to avoid:** Prove the mapping explicitly. Show that the information-theoretic constraint (model accesses body only through boundary) implies that the interaction terms h_{xy} are supported only on pairs of adjacent sites. The proof should go: self-modeling constraint -> channel capacity between non-adjacent sites bounded by boundary capacity -> interactions effectively nearest-neighbor.

**Warning signs:** Any statement of the form "clearly, self-modeling locality implies..." without a proof step.

**Recovery:** If the mapping cannot be proved, this is a backtracking trigger. Identify whether the two notions are structurally compatible. If not, return to user for scope decision.

### Pitfall 2: Background Dependence Circularity

**What goes wrong:** The lattice graph G = (V, E) is an input, which defines which sites are "neighbors." But the goal of the overall project is to derive spatial geometry. If the lattice connectivity defines the geometry, the geometry is not derived -- it is assumed.

**Why it happens:** Defining nearest-neighbor interactions requires knowing the graph, which encodes topology. Topology is a geometric concept.

**How to avoid:** Be explicit: Phase 8 assumes the lattice topology as input. The claim is that self-modeling determines the METRIC (distances, curvature) on a given topology, not the topology itself. Frame this honestly in the lattice definition: "Given a graph G (input), we define..."

**Warning signs:** Any claim that the lattice "emerges" from self-modeling without proof.

**Recovery:** This pitfall is deferred to LOCL-03 (follow-up requirement). Phase 8 proceeds with honest framing.

### Pitfall 3: Non-Unique Hamiltonian

**What goes wrong:** The self-modeling constraint may not uniquely determine h_{xy}. Many Hamiltonians could be compatible with the same composite sequential product structure, especially because the SP constrains the algebra (products of effects) but the Hamiltonian generates continuous-time dynamics.

**Why it happens:** The sequential product is a static algebraic structure (a & b is defined without reference to time evolution). A Hamiltonian generates dynamics. Mapping from a static structure to a dynamic one typically introduces ambiguity.

**How to avoid:** (a) Characterize the full family of compatible Hamiltonians. (b) Check whether area-law results (Phase 9) and Lieb-Robinson bounds are robust across the family. If v_LR and area-law scaling are independent of the choice within the family, non-uniqueness is harmless. (c) If uniqueness is needed and fails, identify the additional physical constraint that would fix it (e.g., energy minimization, symmetry requirement).

**Warning signs:** Choosing a specific h_{xy} by fiat without checking alternatives.

**Recovery:** Per the contract backtracking trigger: "identify the family of compatible Hamiltonians and whether area-law results are robust across the family."

### Pitfall 4: Dimension Mismatch Between OUS and Hilbert Space

**What goes wrong:** Paper 5 works with M_n(C)^sa (the self-adjoint part, a real vector space of dimension n^2). The Hamiltonian framework works with M_n(C) (the full algebra) or equivalently with C^n (the Hilbert space). Confusing the dimensions: M_n(C)^sa has real dimension n^2, but the Hilbert space has complex dimension n. An effect a in M_n(C)^sa is an n x n self-adjoint matrix, but a state vector is an n-component complex vector.

**Why it happens:** The OUS framework (Paper 5) and the Hilbert space framework (Bratteli-Robinson) use different mathematical objects as primitives. Converting between them requires care.

**How to avoid:** Always be explicit about which mathematical object you are working with: OUS element (self-adjoint matrix), Hilbert space vector (state vector), or density matrix (positive trace-one operator). The Hamiltonian h_{xy} is a self-adjoint element of M_n(C) tensor M_n(C) = M_{n^2}(C). Its spectral decomposition gives eigenvalues and eigenvectors in C^{n^2}.

**Warning signs:** Conflating dim(M_n(C)^sa) = n^2 with dim(C^n) = n.

## Level of Rigor

**Required for this phase:** Physicist's proof for the mapping (self-modeling to Hamiltonian), formal proof for the Lieb-Robinson bound computation.

**Justification:** The Lieb-Robinson bound is a rigorous mathematical result and must be applied rigorously (correct statement, correct hypotheses, correct constants). The mapping from self-modeling to the Hamiltonian is novel theoretical work where a physicist's proof (logically sound, standard manipulations assumed) is appropriate for the first pass. A formal proof may be required for Paper 6 but is not needed for the planning stage.

**What this means concretely:**

- The lattice definition (graph, local algebras, interaction terms) must be mathematically precise -- no ambiguity in what the objects are.
- The Lieb-Robinson velocity v_LR must be computed with explicit constants from the Nachtergaele-Sims framework, not estimated or "expected to be finite."
- The mapping from self-modeling coupling to h_{xy} should be argued from the structure of the composite sequential product, with the key steps identified even if full details are deferred.
- Dimensional analysis must be verified at every step.

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| --- | --- | --- | --- |
| Original LR bound (1972): loose constants | Nachtergaele-Sims (2006, 2019): tight bounds, unified framework | 2006 | Use modern bounds; much tighter v_LR |
| LR velocity growing as O(d) with local dimension d | Wang-Hazzard (2019): improved to O(sqrt(d)) or O(d/log d) | 2019 | For M_n(C) with large n, the improved bound matters |
| Only gap-based area laws (Hastings 2007) | Multiple gap-free routes: WVCH (thermal), Brandao-Horodecki (correlation decay), channel capacity | 2008-2015 | Phase 9 benefits; Phase 8 does not directly need area laws but should set up the Hamiltonian to be compatible with all routes |
| 2D area law: open for general gapped systems | Anshu-Arad-Gosset (2022): proved for 2D frustration-free | 2022 | If the self-modeling Hamiltonian is frustration-free, 2D area law follows |

**Superseded approaches to avoid:**

- **Original Lieb-Robinson (1972) constants:** The original paper gives correct but very loose bounds. Use the Nachtergaele-Sims modernization for tighter constants.
- **Ad hoc lattice models without operator-algebraic foundation:** Some entanglement-gravity papers (e.g., toy MERA models) define lattices without the full Bratteli-Robinson structure. Our construction must be mathematically precise to support rigorous LR bounds.

## Open Questions

1. **Does the self-modeling sequential product uniquely determine h_{xy}?**
   - What we know: The product-form SP (a tensor b) & (c tensor d) = (a & c) tensor (b & d) constrains the two-site algebra, and the single-site SP a & b = a^{1/2} b a^{1/2} (Luders product) constrains the single-site dynamics. Together, these may or may not uniquely fix h_{xy}.
   - What's unclear: Whether the algebraic constraint (SP structure) translates to a unique dynamical generator (Hamiltonian). The SP is "timeless" -- it describes the result of a sequential measurement, not time evolution. Connecting to a Hamiltonian requires interpreting the SP as generating a one-parameter group.
   - Impact on this phase: HIGH. If non-unique, must characterize the family and check robustness.
   - Recommendation: Identify the constraints that h_{xy} must satisfy. Enumerate the degrees of freedom in h_{xy} (as an element of M_{n^2}(C)^sa, it has n^4 real parameters). The SP constraints are equations that reduce this parameter space. For n = 2, h_{xy} has 16 real parameters; count how many are fixed by the SP structure.

2. **Is the self-modeling Hamiltonian frustration-free?**
   - What we know: A Hamiltonian H = sum h_{xy} is frustration-free if the ground state of H also minimizes each h_{xy} individually. Frustration-free systems have stronger area-law results (Anshu-Arad-Gosset 2022 for 2D).
   - What's unclear: Whether the self-modeling constraint produces a frustration-free Hamiltonian. The product-form SP is "factorized" in some sense, which hints at frustration-freeness, but this is speculative.
   - Impact on this phase: LOW (directly). Affects Phase 9 route selection.
   - Recommendation: Check frustration-freeness as a bonus after constructing h_{xy}. Do not require it.

3. **What is the effective lattice dimension?**
   - What we know: The lattice graph G is input. In physical spacetime, d = 3 spatial dimensions.
   - What's unclear: Whether the self-modeling constraint selects a preferred dimension. This is LOCL-03 (follow-up, not in scope for Phase 8).
   - Impact on this phase: LOW. State results for general G; compute for Z^1 and Z^2.
   - Recommendation: Defer dimension selection. Phase 8 works for any G.

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| --- | --- | --- | --- |
| Hamiltonian construction from SP | SP does not uniquely determine h_{xy}; family too large | Information-theoretic lattice (no Hamiltonian); define locality via channel capacity constraints | Moderate: lose explicit v_LR computation; gain simplicity. Phase 9 must use channel capacity route exclusively. |
| Hamiltonian construction from SP | Self-modeling dynamics not captured by time-independent H | Time-dependent or stochastic interaction; Lindbladian framework | High: requires re-developing LR bounds for open systems (Poulin 2010, PRL 104, 190401). Well-studied but more complex. |
| Nearest-neighbor interaction | Self-modeling coupling produces next-nearest-neighbor or longer-range terms | Finite-range (not strictly NN) interaction; LR bounds still apply for any finite range | Low: Nachtergaele-Sims framework handles any finite-range interaction. v_LR formula changes but procedure is identical. |
| Consistency with Paper 5 composite | Two-site dynamics do not exactly reproduce product-form SP | Approximate reproduction: SP structure holds to leading order in coupling J | Moderate: must quantify the approximation error and verify it does not invalidate Phase 9 arguments. |

**Decision criteria:** Abandon the Hamiltonian approach if: (a) the SP constraints leave h_{xy} entirely unconstrained (no equations reduce the parameter space), or (b) the only compatible h_{xy} is h_{xy} = 0 (no interaction). In case (a), switch to information-theoretic lattice. In case (b), the self-modeling premise does not generate an interaction, and the entire v3.0 chain is blocked -- return to user.

## Sources

### Primary (HIGH confidence)

- Bratteli, Robinson, "Operator Algebras and Quantum Statistical Mechanics," vols. 1-2, Springer (1979, 1981) -- Definitive reference for quantum lattice systems
- Lieb, Robinson, "The Finite Group Velocity of Quantum Spin Systems," Commun. Math. Phys. 28, 251 (1972) -- Original LR bound
- Nachtergaele, Sims, "Lieb-Robinson Bounds and the Exponential Clustering Theorem," Commun. Math. Phys. 265, 119 (2006), [arXiv:math-ph/0506030](https://arxiv.org/abs/math-ph/0506030) -- Exponential clustering from gap + LR bounds
- Nachtergaele, Sims, Young, "Quasi-Locality Bounds for Quantum Lattice Systems. Part I," J. Math. Phys. 60, 061101 (2019), [arXiv:1810.02428](https://arxiv.org/abs/1810.02428) -- Modern unified LR bound framework with explicit constants
- Bravyi, Hastings, Verstraete, "Lieb-Robinson Bounds and the Generation of Correlations and Topological Quantum Order," PRL 97, 050401 (2006), [arXiv:quant-ph/0603121](https://arxiv.org/abs/quant-ph/0603121) -- Entanglement generation rate scales with boundary
- Paper 5 (v2.0) -- composite-lt.tex, derivations/05-local-tomography.md, derivations/05-type-exclusion-and-cstar.md -- M_n(C)^sa, composite OUS, local tomography, product-form SP

### Secondary (MEDIUM confidence)

- Barnum, Wilce, "Local Tomography and the Jordan Structure of Quantum Theory," Found. Phys. 44, 192 (2014), [arXiv:1202.4513](https://arxiv.org/abs/1202.4513) -- Local tomography forces complex quantum theory
- Wang, Hazzard, "Tightening the Lieb-Robinson Bound in Locally-Interacting Systems," PRX Quantum 1, 010303 (2020), [arXiv:1908.03997](https://arxiv.org/abs/1908.03997) -- Improved LR velocity for large local dimension
- Nachtergaele, Sims, "Quasi-Locality Bounds for Quantum Lattice Systems. Part II," [arXiv:2010.15337](https://arxiv.org/abs/2010.15337) -- Stability of gapped phases under perturbations
- Eisert, Cramer, Plenio, "Area Laws for the Entanglement Entropy," RMP 82, 277 (2010), [arXiv:0808.3773](https://arxiv.org/abs/0808.3773) -- Comprehensive area-law review
- Hastings, "An Area Law for One Dimensional Quantum Systems," JSTAT P08024 (2007), [arXiv:0705.2024](https://arxiv.org/abs/0705.2024) -- 1D area law for gapped systems

### Tertiary (LOW confidence)

- Nachtergaele, Raz, Schlein, Sims, "Lieb-Robinson Bounds for Harmonic and Anharmonic Lattice Systems," Commun. Math. Phys. 286, 1073 (2009) -- Extension to infinite-dimensional local Hilbert spaces (not needed here)
- Poulin, "Lieb-Robinson Bound and Locality for General Markovian Quantum Dynamics," PRL 104, 190401 (2010) -- LR bounds for open systems (fallback if Lindbladian needed)

## Metadata

**Confidence breakdown:**

- Mathematical framework: HIGH -- Bratteli-Robinson and LR bounds are textbook material with 40+ years of development
- Standard approaches: MEDIUM-HIGH -- The framework application is standard; the novel mapping step (SP to Hamiltonian) has no precedent
- Computational tools: HIGH -- Standard scientific Python; no exotic tools needed
- Validation strategies: MEDIUM-HIGH -- Internal consistency checks are well-defined; validation of the mapping itself is harder (no external benchmark for the novel step)

**Research date:** 2026-03-21
**Valid until:** Indefinite for the mathematical framework (Bratteli-Robinson, LR bounds). The novel mapping step has no expiration but may be superseded if someone publishes a self-modeling-to-Hamiltonian construction.

## Caveats and Alternatives (Pre-Submission Self-Critique)

1. **What assumption am I making that might be wrong?** I assume the sequential product can be meaningfully connected to a Hamiltonian generator. The SP a & b describes a single "sequential measurement" operation, not continuous-time evolution. It is possible that the self-modeling dynamics are fundamentally discrete (measurement-like) and cannot be captured by a Hamiltonian at all. If so, the Lindbladian/open-system fallback is needed.

2. **What alternative approach did I dismiss too quickly?** The information-theoretic lattice (no Hamiltonian) is simpler and avoids the SP-to-Hamiltonian mapping entirely. I prioritized the Hamiltonian approach because it gives v_LR (a contract requirement) and compatibility with more area-law results. But if the mapping proves difficult, the information-theoretic approach may be more productive.

3. **What limitation of my recommended method am I understating?** The non-uniqueness of h_{xy} could be severe. For n = 2, h_{xy} has 16 real parameters; the SP constraints may only fix a few of them, leaving a large family. I have not estimated how many constraints the SP structure provides. This should be the first task in Phase 8 execution.

4. **Is there a simpler method I overlooked?** One could define h_{xy} = -J * (boundary projector) where the "boundary projector" is the projection onto the subspace where sites x and y have compatible self-models. This is a simpler ansatz than deriving h_{xy} from the full SP structure. It may suffice for LR bounds and area-law arguments. The risk is that it does not faithfully represent the self-modeling coupling.

5. **Would a specialist disagree with my recommendation?** An operator algebraist might argue that the Hamiltonian is unnecessary -- the quasi-local algebra structure plus a state (via the GNS construction) is sufficient. An information theorist might argue that mutual information constraints are the correct formalization of self-modeling locality, not Hamiltonian interactions. Both perspectives have merit and correspond to the fallback approach.
