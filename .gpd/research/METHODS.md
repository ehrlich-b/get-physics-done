# Methods Research

**Domain:** Quantum foundations / Operational quantum theory / Jordan algebras / Effect algebras
**Researched:** 2026-03-20
**Confidence:** MEDIUM

### Scope Boundary

METHODS.md covers analytical PHYSICS methods for verifying sequential product axioms, proving local tomography, and promoting Jordan algebras to C*-algebras. It does NOT cover software tools or libraries -- those belong in COMPUTATIONAL.md.

**Critical distinction:** All methods here work BELOW the C*-algebra level (in effect algebras, order unit spaces, Jordan algebras, GPTs). Methods that presuppose C*-algebra structure are irrelevant -- we are trying to DERIVE that structure.

---

## Recommended Methods

### Analytical Methods

| Method | Purpose | Why Recommended |
|--------|---------|-----------------|
| Order unit space axiom checking | Verify S1-S7 for self-modeling sequential product | Direct method: check each axiom against the construction one by one |
| Koecher-Vinberg pathway | Obtain Jordan algebra from homogeneity + self-duality | Van de Wetering's Theorem 1 uses this as the bridge from S1-S7 to EJA |
| Hanche-Olsen tensor product criterion | Promote Jordan algebra to C*-algebra | The standard (and essentially unique) method for Jordan -> C* promotion |
| GPT compositional analysis | Prove local tomography from B-M independence | Barnum-Wilce framework for when composites force complex quantum theory |
| D'Ariano faithful-state construction | Backup route: construct involution from symmetric faithful state | Alternative if sequential product route fails at S4 |

### Method Selection by Problem Type

**If verifying S1-S7 for a specific construction:**
- Use direct axiom-by-axiom verification in order unit space framework
- Because this is a finite-dimensional algebraic problem with concrete axioms to check

**If S4 fails and you need a workaround:**
- Use D'Ariano's faithful-state method (arXiv:quant-ph/0611094) as backup
- Because it constructs the involution from a different operational assumption (symmetric faithful state) rather than from sequential product symmetry

**If proving local tomography from compositionality:**
- Use GPT framework with Barnum-Wilce theorem (arXiv:1202.4513)
- Because this is the standard result connecting Jordan algebras + local tomography -> C*-algebras

---

## Method Details

### Method 1: Sequential Product Axiom Verification (S1-S7)

**What:** Systematic verification that a concrete sequential product construction satisfies the Gudder-Greechie axioms as formulated by van de Wetering.

**Mathematical basis:**

Let (V, e) be a finite-dimensional order unit space with positive cone V+ and order unit e. A sequential product is a bilinear map (a,b) -> a & b from [0,e] x [0,e] -> [0,e] satisfying:

- **S1 (Additivity in 2nd argument):** a & (b + c) = a & b + a & c when b + c <= e. This says "testing a, then testing the mixture b+c" equals "testing a then b" plus "testing a then c." For the self-model: if effects b,c on B are orthogonal, updating M after testing a and then testing b+c decomposes. This is LINEAR in the second argument because sequential measurement of a disjoint alternative decomposes.

- **S2 (Continuity in 1st argument):** The map a -> a & b is continuous for each fixed b. For the self-model: small perturbations of the first test produce small changes in the sequential outcome. This is a TOPOLOGICAL condition and holds for any construction on a finite-dimensional space (all linear maps on finite-dimensional spaces are continuous).

- **S3 (Unit acts trivially):** e & a = a for all a in [0,e]. "Performing the trivial test (always pass) first changes nothing." For the self-model: if the first test is the identity (do nothing to B), the model update is trivial, and the second test proceeds unchanged.

- **S4 (Symmetry of orthogonality):** If a & b = 0 then b & a = 0. "If testing a first makes b impossible, then testing b first makes a impossible." THIS IS THE HARD ONE. For the self-model: if "test a on B, update M, test b on B" always gives zero, then "test b on B, update M, test a on B" must also give zero. This is nontrivial because the model update step M could break the symmetry.

- **S5 (Compatibility):** If a & b = b & a then a & (e - b) = (e - b) & a. "If a and b commute sequentially, then a and the complement of b also commute." For the self-model: this is an algebraic consistency condition on compatible pairs.

- **S6 (Sequential product preserves sharp elements):** If a and b are sharp (projections), then a & b is sharp. For the self-model: sequential measurement of two sharp effects produces a sharp effect.

- **S7 (Multiplicativity on compatible effects):** If a & b = b & a then a & b coincides with the Jordan product. For compatible (commuting) effects, the sequential product reduces to the algebraic product.

**Proof strategy for each axiom:**

| Axiom | Strategy | Difficulty | Key technique |
|-------|----------|------------|---------------|
| S1 | Show bilinearity of "test a, update, test b" in b | Easy | Linearity of effect evaluation |
| S2 | Invoke finite-dimensionality | Trivial | All maps on finite-dim spaces are continuous |
| S3 | Show identity test produces trivial update | Easy | Definition of the sequential product |
| S4 | **Show orthogonality is symmetric despite model update** | **HARD** | See dedicated section below |
| S5 | Algebraic computation for compatible pairs | Moderate | Commutativity implies complement-commutativity |
| S6 | Show idempotent effects compose to idempotent | Moderate | Spectral analysis of the product |
| S7 | Reduce to Jordan product for commuting elements | Moderate | Direct computation |

**Confidence:** MEDIUM. The axiom list is well-established (Gudder-Greechie 2002, van de Wetering 2018). The difficulty is in the concrete application to the self-modeling construction, especially S4.

**Key references:**
- Gudder & Greechie, "Sequential products on effect algebras," Reports on Math. Physics 49, 87-111 (2002)
- van de Wetering, "Sequential product spaces are Jordan algebras," J. Math. Phys. 60, 062201 (2019), arXiv:1803.11139
- Gudder, "Open problems for sequential effect algebras," Int. J. Theor. Phys. 44, 2199-2206 (2005)


### Method 2: S4 Verification -- Dedicated Analysis

**What:** Techniques specifically for proving or disproving S4 (symmetry of orthogonality) for the self-modeling sequential product.

**Why this deserves its own section:** S4 is the decisive axiom. S1-S3 are essentially free. S5-S7 are algebraic consequences once the product is defined. S4 is the one that can fail, and if it fails, the entire sequential product route collapses.

**The problem in concrete terms:** The self-model's sequential product is:
```
(a & b)(rho) = Prob(b | state after "test a on B, update M based on outcome")
```

S4 requires: if this is zero for all states, then swapping a and b also gives zero for all states. The model update step is the asymmetry -- testing a first triggers a different model update than testing b first.

**Technique 2a: Direct algebraic proof via spectral decomposition**

If the effect algebra on B is finite-dimensional, decompose the sequential product using the spectral theory of the order unit space. Write:
```
a & b = sqrt(a) . b . sqrt(a)    (Luders product form)
```
where sqrt and multiplication are in the order unit space sense. Then:
- a & b = 0 iff sqrt(a) . b . sqrt(a) = 0 iff b . a . b = 0 (by positivity) iff sqrt(b) . a . sqrt(b) = 0 iff b & a = 0.

This works IF the sequential product has Luders form. The question is whether the self-modeling construction actually produces a Luders-form product.

**Applicability:** Works when the sequential product can be shown to coincide with the Luders product. This is the STANDARD sequential product on C*-algebras and EJAs. Van de Wetering (arXiv:1803.08453) showed that the Luders product is characterized by three properties: invariance under order isomorphisms, symmetry w.r.t. a specific inner product, and preservation of invertibility.

**Technique 2b: Inner product symmetry argument**

Van de Wetering's second characterization: the Luders product is the UNIQUE sequential product satisfying <a & b, c> = <b, a & c> for the canonical inner product on the EJA (the trace inner product <a,b> = tr(a . b) in the Jordan algebra sense).

Strategy: define the natural inner product on the self-model's effect space, then check whether the self-modeling sequential product satisfies this symmetry. If yes, S4 follows automatically (because inner product symmetry implies: a & b = 0 iff <a & b, c> = 0 for all c iff <b, a & c> = 0 for all c, plus positivity arguments give b & a = 0).

**Applicability:** Requires identifying a natural inner product on the state space. For finite-dimensional systems, the trace form on the state space provides this.

**Technique 2c: Contrapositive / counterexample search**

If S4 is suspected to fail, construct an explicit counterexample:
1. Choose specific finite-dimensional system (e.g., B = qubit, M = qubit)
2. Define explicit effects a, b on B
3. Define explicit model update rule
4. Compute a & b and b & a
5. Find a,b with a & b = 0 but b & a != 0

**Applicability:** Always applicable. If you can find a counterexample, S4 fails. The difficulty is that the construction must be the SPECIFIC self-modeling one, not an arbitrary sequential product.

**Technique 2d: Reduction to faithfulness condition**

If the model M faithfully represents the state of B (injective embedding of B's state space into M's), then the model update is an isometric map. Isometric maps preserve orthogonality in both directions. Therefore:
- a perp b in B implies (model-updated-a) perp (model-updated-b)
- This symmetry of the isometry forces S4

This is the most promising route because the "self-model is faithful" assumption is physically natural (a model that loses information is a bad model).

**Confidence:** MEDIUM-LOW. The specific technique depends heavily on what exactly the "model update" does. Technique 2d is the most physically motivated but requires the faithfulness assumption to be formalized and proved.

**Key references:**
- van de Wetering, "Three characterisations of the sequential product," J. Math. Phys. 59, 082202 (2018), arXiv:1803.08453
- Westerbaan, Westerbaan & van de Wetering, "The three types of normal sequential effect algebras," Quantum 4, 378 (2020), arXiv:2004.12749


### Method 3: Koecher-Vinberg Pathway (S1-S7 -> Jordan Algebra)

**What:** Once S1-S7 are verified, invoke the Koecher-Vinberg theorem through van de Wetering's Theorem 1 to obtain Euclidean Jordan algebra structure.

**Mathematical basis:**

Van de Wetering's Theorem 1 (arXiv:1803.11139): A finite-dimensional order unit space with a continuous sequential product satisfying S1-S7 is homogeneous and self-dual. By the Koecher-Vinberg theorem, it is therefore a Euclidean Jordan algebra (EJA).

The Koecher-Vinberg theorem (Koecher 1957, Vinberg 1961): There is a one-to-one correspondence between finite-dimensional formally real Jordan algebras and symmetric cones (open, regular, homogeneous, self-dual convex cones).

**Proof technique in van de Wetering's theorem:**
1. S1-S4 + continuity -> the sequential product induces a spectral decomposition
2. Spectral decomposition -> the cone of positive elements is homogeneous (any interior point can be mapped to any other by a positive map)
3. S4 (symmetry of orthogonality) -> self-duality of the cone (the cone equals its dual)
4. Homogeneous + self-dual -> Koecher-Vinberg -> formally real Jordan algebra
5. S5-S7 -> the Jordan product is the symmetrized sequential product

**What this gives us:** The EJA classification. Every finite-dimensional EJA is a direct sum of simple EJAs, and the simple ones are:
- Real symmetric matrices: M_n(R)_sa (self-adjoint part)
- Complex Hermitian matrices: M_n(C)_sa
- Quaternionic Hermitian matrices: M_n(H)_sa
- Spin factors: V_n
- Exceptional Albert algebra: M_3(O)_sa (the 3x3 Hermitian octonionic matrices)

**What this does NOT give us:** The C*-algebra. The Jordan algebra is the self-adjoint part of a C*-algebra, but the Jordan product a . b = (1/2)(ab + ba) does not determine the full associative product ab. For that, we need the local tomography step (Method 5).

**Confidence:** HIGH. The Koecher-Vinberg theorem and van de Wetering's extension are well-established published results.

**Key references:**
- Koecher, "Positivitatsbereiche im R^n," Amer. J. Math. 79, 575-596 (1957)
- Vinberg, "Homogeneous cones," Doklady 141, 270-273 (1961)
- van de Wetering, arXiv:1803.11139


### Method 4: Hanche-Olsen Tensor Product Criterion (Jordan -> C*-Algebra)

**What:** Promote a Euclidean Jordan algebra to a C*-algebra by showing its tensor product with another EJA is again an EJA (i.e., it admits a locally tomographic composite).

**Mathematical basis:**

Hanche-Olsen's theorem (1985): A JB-algebra whose vector space tensor product with any other JB-algebra carries a JB-algebra structure (compatible with the factor structures) must be a JC-algebra -- i.e., it embeds in a C*-algebra as the self-adjoint part.

More precisely: if A is an EJA such that A tensor B carries an EJA structure for any EJA B, with the tensor product respecting the factor Jordan products, then A is (a direct sum of) self-adjoint parts of matrix algebras over R, C, or H. The exceptional Albert algebra M_3(O) is EXCLUDED because it does not admit a locally tomographic tensor product.

**This is van de Wetering's Theorem 3:** Sequential product space + local tomographic composite = C*-algebra (self-adjoint part).

**Proof technique:**
1. Start with EJA A from Method 3
2. Consider the composite system A tensor B where B is another EJA (in our case: B's effect algebra and M's effect algebra)
3. Local tomography requires: states on A tensor B are determined by product measurements
4. This forces the tensor product to be the "maximal" tensor product of operator systems
5. Hanche-Olsen: this maximal tensor product exists as an EJA iff A has no exceptional (octonionic) direct summand
6. Without the exceptional part: A = direct sum of M_n(K)_sa for K in {R, C, H}
7. Each such summand embeds in M_n(C) as the self-adjoint part -> C*-algebra

**What eliminates the remaining ambiguity (R vs C vs H):**
- Local tomography specifically selects the COMPLEX case
- Real and quaternionic quantum mechanics fail local tomography for composites
- This is the content of Barnum-Wilce (arXiv:1202.4513): Jordan algebra + local tomography + one qubit-like system -> complex QM

**Confidence:** HIGH. Hanche-Olsen's result is a proven theorem (1985). The application to quantum foundations is well-established through Barnum-Wilce and van de Wetering.

**Key references:**
- Hanche-Olsen, "JB-algebras with tensor products are C*-algebras," in Operator Algebras and their Connections with Topology and Ergodic Theory, LNM 1132, Springer (1985)
- Hanche-Olsen & Stormer, "Jordan Operator Algebras," Pitman Monographs (1984)
- Barnum, Mueller & Ududec, "Composites and categories of Euclidean Jordan algebras," Quantum 4, 359 (2020), arXiv:1606.09331
- van de Wetering, arXiv:1803.11139, Theorem 3


### Method 5: Local Tomography from B-M Compositionality

**What:** Prove that the composite system (body B) tensor (model M) satisfies local tomography, using the operational constraint that B and M are independently accessible to the self-model.

**Mathematical basis:**

Local tomography (definition): A composite state rho_BM on B tensor M is locally tomographic if it is uniquely determined by the set of all product probabilities {p(a_B, b_M) = Tr((a_B tensor b_M) rho_BM)} for effects a_B on B and b_M on M.

Equivalently: the state space of the composite equals the tensor product of the individual state spaces: S(BM) = S(B) tensor S(M). No "entangled-only" degrees of freedom.

**Proof strategy:**

The argument must proceed in the PRE-algebraic setting (order unit spaces / GPT framework), not assuming C*-algebra structure.

**Technique 5a: Dimension counting in GPT framework**

In a general probabilistic theory (GPT), a system is described by:
- State space: a compact convex set Omega
- Effect space: [0,u] in the dual order unit space
- Composite: some tensor product Omega_A tensor_? Omega_B between minimal and maximal tensor products

Local tomography holds iff the composite state space has dimension dim(Omega_A) * dim(Omega_B).

For the self-model: if B has state space dimension d_B and M has state space dimension d_M, local tomography holds iff the joint state space has dimension d_B * d_M. The argument: if the self-model can independently probe B and M, and M is a faithful model of B, then the joint state is determined by the independent probes.

**Technique 5b: Information-theoretic argument**

If the self-model can:
(i) prepare any state of B independently of M, and
(ii) prepare any state of M independently of B, and
(iii) the self-model's information about BM consists ONLY of what it can learn by probing B and M separately,

then by definition the joint state is determined by local measurements, which IS local tomography.

The key assumption is (iii): the self-model has no "non-local oracle" for the composite system. This is physically motivated by the operational setup -- the self-model interacts with B and M through local measurements.

**Technique 5c: Barnum-Wilce categorical argument**

Barnum and Wilce (arXiv:1202.4513) proved: if individual systems form EJAs, composites are locally tomographic, and at least one system is a qubit (2-dimensional), then the theory IS complex quantum mechanics.

Strategy:
1. From Method 3, we have EJA structure on B (and on M if M is also an EJA)
2. From the operational setup, argue local tomography (via 5a or 5b)
3. Invoke Barnum-Wilce: EJA + local tomography + qubit -> complex QM

The "qubit" condition is mild -- it just requires one system in the theory to be the simplest non-trivial quantum system. For the self-model: if B can be as simple as a two-level system, this is satisfied.

**Known limitation:** Local tomography fails for real and quaternionic quantum mechanics. If the Jordan algebra turns out to be real-type or quaternion-type, local tomography is the assumption that SELECTS the complex case. This is a feature, not a bug -- it is precisely the role local tomography plays in the reconstruction.

**Confidence:** MEDIUM. The mathematical framework is solid. The gap is in formalizing exactly what "independent accessibility of B and M" means in the order unit space framework and proving it implies local tomography.

**Key references:**
- Barnum & Wilce, "Local tomography and the Jordan structure of quantum theory," Found. Phys. 44, 192-212 (2014), arXiv:1202.4513
- Barnum, Mueller & Ududec, "Composites and categories of Euclidean Jordan algebras," Quantum 4, 359 (2020), arXiv:1606.09331
- Hardy, "Reformulating and reconstructing quantum theory," arXiv:1104.2066


### Method 6: D'Ariano Faithful-State Backup Route

**What:** If the sequential product route fails (S4 does not hold), construct the involution directly from the existence of a symmetric faithful state, following D'Ariano's operational axiomatics.

**Mathematical basis:**

D'Ariano's Postulate 5 (arXiv:quant-ph/0611094): There exists a "faithful state" omega such that:
- omega(a) = 0 implies a = 0 (faithfulness: the state separates effects)
- The bilinear form <a, b>_omega = omega(a . b) is symmetric (symmetry: the state defines a real inner product on effects)

From such a state, D'Ariano constructs:
1. An inner product on the effect algebra: <a, b> = omega(a . b)
2. A conjugation map (involution) on effects: a -> a* defined via <a* . b, omega> = <b . a, omega>
3. The adjoint extends to transformations: T -> T* via <T*(a), b>_omega = <a, T(b)>_omega

If the conjugation is composition-preserving (i.e., (T . S)* = S* . T*), this gives a *-algebra structure, hence C*-algebra in finite dimensions.

**When to use:** ONLY if Method 1 (S4 verification) fails. This is a backup that uses a DIFFERENT operational assumption (faithful state exists) instead of sequential product structure.

**For the self-model:** The faithful state would be the "maximally uncertain" state of the self-model -- the state where the model has maximum uncertainty about B. This is operationally natural (the model starts with no information about B). The symmetry condition <a, b>_omega = <b, a>_omega then becomes a condition on this maximum-uncertainty state.

**Limitation:** This method requires proving that the maximum-uncertainty state IS symmetric and faithful, which is a separate (potentially hard) verification.

**Confidence:** MEDIUM. D'Ariano's method is published and well-understood. The question is whether the self-model provides the necessary faithful state.

**Key references:**
- D'Ariano, "Operational axioms for quantum mechanics," arXiv:quant-ph/0611094 (2006)
- D'Ariano, Chiribella & Perinotti, "Informational derivation of quantum theory," Phys. Rev. A 84, 012311 (2011), arXiv:1011.6451


---

## Alternatives Considered

| Recommended | Alternative | When to Use Alternative |
|-------------|------------|------------------------|
| Sequential product axiom verification (Methods 1-2) | Algebraic QFT (Haag-Kastler) approach | Never for this project -- presupposes C*-algebra structure, which is what we are trying to derive |
| Koecher-Vinberg (Method 3) | Direct Jordan algebra construction from scratch | If the order unit space is already known to be a Jordan algebra by other means -- unnecessary here because van de Wetering's theorem gives it from the sequential product |
| Hanche-Olsen (Method 4) | Alfsen-Shultz orientation approach | When you have geometric (orientation) data on the state space but not a tensor product; more complex than Hanche-Olsen but equivalent in finite dim |
| Local tomography (Method 5) | Hardy's purification axiom | If you cannot establish local tomography directly; purification is an alternative route to complex QM but requires additional operational assumptions |
| D'Ariano backup (Method 6) | Barandes stochastic-quantum bijection | If you want to go directly from stochastic dynamics to QM without algebraic intermediaries; different philosophy but valid |

## What NOT to Use

| Avoid | Why | Use Instead |
|-------|-----|-------------|
| C*-algebra spectral theory | Circular -- presupposes the structure we are deriving | Order unit space spectral theory (Alfsen-Shultz) |
| Hilbert space methods (bra-ket, density matrices) | Circular -- presupposes complex QM | GPT framework (effect algebras, state spaces) |
| von Neumann algebra techniques | Too heavy, presupposes separable Hilbert space | Finite-dimensional Jordan algebra techniques |
| Categorical quantum mechanics (Abramsky-Coecke) | Presupposes dagger-compact category structure, which includes the involution | Work in the weaker setting of order unit spaces |
| GNS construction from states | Presupposes *-algebra structure (the involution) to define the inner product | D'Ariano's faithful state method (does NOT presuppose the *) |

---

## Validation Strategy by Method

| Method | Validation Approach | Key Benchmarks |
|--------|-------------------|----------------|
| S1-S7 verification | Check each axiom against known quantum case (M_n(C)_sa with Luders product) -- all must hold | Standard quantum mechanics must satisfy S1-S7 (it does, by construction) |
| S4 specifically | Verify on qubit (n=2) first, then general n | For M_2(C): a & b = sqrt(a) b sqrt(a), orthogonality IS symmetric |
| Koecher-Vinberg | Check classification: result must be one of the five types of simple EJA | If you get something not in the classification, an axiom was wrong |
| Hanche-Olsen | Check that octonionic case is excluded by local tomography | M_3(O)_sa must fail the tensor product condition |
| Local tomography | Dimension count: dim(S_BM) must equal dim(S_B) * dim(S_M) | For qubits: dim = 3*3 = 9 (not 15, which would be non-local-tomographic) |
| D'Ariano backup | Faithful state must separate effects and be symmetric | For the maximally mixed state on M_n(C): omega(a) = tr(a)/n satisfies both conditions |

---

## Logical Dependency Chain

```
S1-S3 verification (easy, mostly free)
    |
    v
S4 verification (hard, decisive) --[if fails]--> D'Ariano backup (Method 6)
    |                                                    |
    v                                                    v
S5-S7 verification                              Faithful state construction
    |                                                    |
    v                                                    v
Van de Wetering Thm 1: EJA structure           *-algebra from faithful state
    |                                                    |
    v                                                    |
Local tomography proof (Method 5) <---------------------|
    |
    v
Hanche-Olsen / Barnum-Wilce: C*-algebra
    |
    v
Complex quantum mechanics (involution derived)
```

The critical path runs through S4. Everything else is either straightforward (S1-S3), algebraic consequence (S5-S7), well-established theorem application (Koecher-Vinberg, Hanche-Olsen), or a separate but tractable argument (local tomography).

---

## Cost and Difficulty Assessment

| Method | Analytical Difficulty | Time Estimate | Risk |
|--------|----------------------|---------------|------|
| S1-S3 verification | Low | 1-2 days | Low: these are essentially definitions |
| S4 verification | **High** | 1-3 weeks | **High**: may fail, and failure mode matters |
| S5-S7 verification | Moderate | 3-5 days | Low: follow from algebraic properties once product is defined |
| Koecher-Vinberg invocation | Low (theorem citation) | 1 day | None: just apply published theorem |
| Local tomography proof | Moderate | 1-2 weeks | Medium: formalization of "independent accessibility" is the hard part |
| Hanche-Olsen invocation | Low (theorem citation) | 1 day | None: just apply published theorem |
| D'Ariano backup | Moderate-High | 2-3 weeks | Medium: existence and symmetry of faithful state must be proved |

---

## Sources

- van de Wetering, "Sequential product spaces are Jordan algebras," J. Math. Phys. 60, 062201 (2019). [arXiv:1803.11139](https://arxiv.org/abs/1803.11139)
- van de Wetering, "Three characterisations of the sequential product," J. Math. Phys. 59, 082202 (2018). [arXiv:1803.08453](https://arxiv.org/abs/1803.08453)
- Westerbaan, Westerbaan & van de Wetering, "The three types of normal sequential effect algebras," Quantum 4, 378 (2020). [arXiv:2004.12749](https://arxiv.org/abs/2004.12749)
- Gudder & Greechie, "Sequential products on effect algebras," Rep. Math. Phys. 49, 87-111 (2002). [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0034487702800076)
- Gudder, "Open problems for sequential effect algebras," Int. J. Theor. Phys. 44, 2199-2206 (2005). [Springer](https://link.springer.com/content/pdf/10.1007/s10773-005-8015-1.pdf)
- Barnum & Wilce, "Local tomography and the Jordan structure of quantum theory," Found. Phys. 44, 192-212 (2014). [arXiv:1202.4513](https://arxiv.org/abs/1202.4513)
- Barnum, Mueller & Ududec, "Composites and categories of Euclidean Jordan algebras," Quantum 4, 359 (2020). [arXiv:1606.09331](https://arxiv.org/abs/1606.09331)
- Barnum, Ududec & van de Wetering, "Self-duality and Jordan structure of quantum theory follow from homogeneity and pure transitivity," Compositionality 5 (2023). [arXiv:2306.00362](https://arxiv.org/abs/2306.00362)
- Hanche-Olsen, "JB-algebras with tensor products are C*-algebras," LNM 1132, Springer (1985)
- Hanche-Olsen & Stormer, "Jordan Operator Algebras," Pitman (1984)
- Alfsen & Shultz, "Geometry of State Spaces of Operator Algebras," Birkhauser (2003). [Springer](https://link.springer.com/book/10.1007/978-1-4612-0019-2)
- D'Ariano, "Operational axioms for quantum mechanics," [arXiv:quant-ph/0611094](https://arxiv.org/abs/quant-ph/0611094) (2006)
- D'Ariano, Chiribella & Perinotti, "Informational derivation of quantum theory," Phys. Rev. A 84, 012311 (2011). [arXiv:1011.6451](https://arxiv.org/abs/1011.6451)
- Koecher-Vinberg theorem: [Wikipedia](https://en.wikipedia.org/wiki/Koecher%E2%80%93Vinberg_theorem)
- Plavala, "General probabilistic theories: An introduction," [arXiv:2103.07469](https://arxiv.org/pdf/2103.07469) (2021)

---

_Methods research for: Sequential product axioms / Jordan-to-C* promotion / Local tomography_
_Researched: 2026-03-20_
