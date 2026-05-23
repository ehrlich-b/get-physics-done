# Phase 4: Sequential Product Formalization - Research

**Researched:** 2026-03-20
**Domain:** Quantum foundations / Algebraic quantum theory / Order unit spaces / Sequential products
**Confidence:** MEDIUM

## Summary

This phase must prove or disprove that the self-modeling "test-update-test" cycle defines a sequential product on a finite-dimensional order unit space satisfying van de Wetering's axioms S1-S7 (arXiv:1803.11139). The construction uses Alfsen-Shultz compressions (P-projections) as the measurement update primitive, parametrized by a tracking map phi from B's effect space to M's effect space. The key result: if S1-S7 hold, van de Wetering's Theorem 1 forces the space to be a Euclidean Jordan algebra; if they fail, the failure mode (especially at S4) determines the project's next step.

The phase is genuinely novel territory: no prior work has verified S1-S7 for any construction beyond B(H)^sa with the Luders product. The mathematical framework (order unit spaces, compressions, spectral decompositions) is well-established; the novelty is entirely in connecting the self-modeling constraint to these axioms. The critical bottleneck is S4 (compatibility of orthogonal effects): the model-update step introduces an asymmetry that could break orthogonality symmetry. S1-S3 are essentially free in finite dimensions. S5-S7 are moderate algebraic consequences once the product is well-defined. Non-associativity must be verified early as a sanity check (associativity would force commutativity, killing the program).

**Primary recommendation:** Define the sequential product as a compression-based bilinear map using Alfsen-Shultz P-projections on sharp effects, extend to general effects via spectral decomposition (Corollary 7/16 of vdW), verify bilinearity as the first gate, then proceed through axioms in order S1-S3 (trivial), non-associativity (sanity check), S5-S7 (moderate), S4 (hard/decisive). Work exclusively in the order unit space framework with no Hilbert space imports.

## User Constraints

See phase CONTEXT.md for locked decisions and user constraints that apply to this phase.

Key constraints affecting this research:
- **Compression-based construction LOCKED:** The sequential product is a . b = C_a(b) where C_a is the Alfsen-Shultz compression. No alternative update primitives.
- **Parametrize by phi LOCKED:** The tracking map phi: E(B) -> E(M) is a parameter, not uniquely determined. Axiom verification reveals what phi needs to satisfy.
- **arXiv:1803.11139 EXCLUSIVELY for axiom definitions LOCKED:** No Gudder-Greechie substitution. Pin all S1-S7 to van de Wetering's exact formulations.
- **Sharp effects first LOCKED:** Compressions for sharp effects are guaranteed; extension to fuzzy effects via spectral decomposition comes second.
- **Bilinearity is the first gate LOCKED:** If extending C_a(b) to a bilinear map fails, the approach is fundamentally wrong. Check BEFORE axiom verification.
- **Classical recovery is a hard constraint LOCKED:** On simplices, the product must reduce to pointwise multiplication.
- **Agent's discretion:** Specific bilinear extension method (spectral theorem vs alternatives); Schrodinger vs Heisenberg picture for intermediates; SymPy vs pen-and-paper for examples; level of intermediate algebra detail.
- **Deferred:** Nothing deferred.

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| --- | --- | --- | --- | --- |
| ref-vdw2018: van de Wetering arXiv:1803.11139 | benchmark / axiom source | Theorems 1, 3 are the axiom definitions and the chain endpoint; definitions must be quoted verbatim | read, use, cite | plan, execution, verification, writing |
| ref-gudder-greechie: Gudder, Greechie (2002) | comparison reference | Classical uniqueness (pointwise mult is unique SP on simplices); comparison only, NOT axiom source | read, cite | execution, writing |
| ref-alfsen-shultz: Alfsen, Shultz -- Geometry of State Spaces | method foundation | Compression (P-projection) theory is the foundation of the construction | read, use | plan, execution |
| v1.0 composite process framework | prior artifact | Classical limit consistency check; compression product must reduce to v1.0 factorization on simplices | compare | verification |
| ~/repos/blog/research/quantum-extension/draft.md | prior artifact | Contains algebraic genericity chain motivation; "gap" this phase closes | read | planning, writing |

**Missing or weak anchors:** The connection between Alfsen-Shultz compressions and bilinear extension to general effects is not explicitly treated in any single reference. The spectral decomposition theorem in vdW (Corollary 7) provides the decomposition a = sum_i lambda_i p_i, and Definition 16 extends the Jordan product bilinearly via this decomposition. An analogous bilinear extension of the sequential product (not just the Jordan product) must be constructed -- this is a novel step with no direct literature precedent.

## Conventions

| Choice | Convention | Alternatives | Source |
| --- | --- | --- | --- |
| Sequential product notation | a & b (following vdW) | a . b, a o_s b | arXiv:1803.11139, Def. 2 |
| Jordan product notation | a * b = (1/2)(a & b + b & a) | a o b | arXiv:1803.11139, Def. 15-16 |
| Order unit space | (V, <=, 1) with Archimedean property | -- | arXiv:1803.11139, Def. 1 |
| Effects | [0,1]_V = {a in V : 0 <= a <= 1} | E(V) | arXiv:1803.11139 |
| Complement | a^perp = 1 - a | a' | arXiv:1803.11139 |
| Compatibility | a \| b iff a & b = b & a | -- | arXiv:1803.11139, Def. 2 |
| Orthogonality | p & q = 0 (via sequential product) | p perp q | arXiv:1803.11139, Def. 8 |
| Norm | ||a|| = inf{r >= 0 : -r1 <= a <= r1} | -- | arXiv:1803.11139, p.3 |
| Sharp effect | p & p = p (idempotent) and p & p^perp = 0 | projection, projective unit | arXiv:1803.11139, Def. 7, Prop. 3 |
| Units | Natural (dimensionless algebraic quantities) | -- | project convention |

**CRITICAL: All equations and results below use these conventions. The notation a & b for the sequential product is non-commutative: a & b != b & a in general. The Jordan product a * b = (1/2)(a & b + b & a) IS commutative. Do not conflate these.**

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in This Phase |
| --- | --- | --- | --- |
| a & (b + c) = a & b + a & c | S1: Additivity in 2nd argument | vdW Def. 2 (S1) | Axiom to verify |
| a -> a & b is continuous | S2: Continuity in 1st argument | vdW Def. 2 (S2) | Axiom to verify (free in finite dim) |
| 1 & a = a | S3: Unit acts trivially | vdW Def. 2 (S3) | Axiom to verify |
| a & b = 0 => b & a = 0 | S4: Compatibility of orthogonal effects | vdW Def. 2 (S4) | THE decisive axiom |
| a \| b => a & (b & c) = (a & b) & c | S5: Associativity of compatible effects | vdW Def. 2 (S5) | Axiom to verify |
| a \| b, a \| 1-b, a \| c => a \| (b+c) | S6: Additivity of compatible effects | vdW Def. 2 (S6) | Axiom to verify |
| a \| b, a \| c => a \| (b & c) | S7: Multiplicativity of compatible effects | vdW Def. 2 (S7) | Axiom to verify |
| a = sum_i lambda_i p_i (spectral decomp.) | Corollary 7 / Corollary 16 | vdW p.7, p.10 | Extension from sharp to general effects |
| p * q = (1/2)(id + L_p - L_{p^perp})b | Jordan product from sequential product | vdW Def. 15 | Recovering Jordan structure |
| V finite-dim SP space => V is EJA | Theorem 1 | vdW p.15 | The payoff if S1-S7 hold |
| V fin-dim SP space + locally tomo composite with self => C*-algebra | Theorem 3 | vdW p.19 | Downstream target (Phase 2) |
| U_e: A -> A, positive projection, U_e(1) = e | Compression / P-projection | Niestegge (2008), Alfsen-Shultz | The update map primitive |
| mu(f\|e) = mu_hat(U_e f) / mu(e) | Conditional probability via compression | Niestegge Prop. 3.1 | Operational meaning of compressions |

### Exact Axiom Definitions (from arXiv:1803.11139, Definition 2)

**Definition 2 (van de Wetering).** Let (V, <=, 1, &) be an order unit space equipped with a binary operation & : [0,1]_V x [0,1]_V -> [0,1]_V. Write a | b (compatible) when a & b = b & a. Call V a *sequential product space* and & a *sequential product* when & satisfies the following for all a, b, c in [0,1]_V:

- **(S1) Additivity:** a & (b + c) = a & b + a & c [when b + c <= 1]
- **(S2) Continuity:** The map a -> a & b is continuous in the order unit norm
- **(S3) Unitality:** 1 & a = a
- **(S4) Compatibility of orthogonal effects:** If a & b = 0 then also b & a = 0
- **(S5) Associativity of compatible effects:** If a | b then a & (b & c) = (a & b) & c
- **(S6) Additivity of compatible effects:** If a | b then a | 1 - b, and if also a | c then a | (b + c) [when b + c <= 1]
- **(S7) Multiplicativity of compatible effects:** If a | b and a | c then a | (b & c)

**Theorem 1 (van de Wetering).** A finite-dimensional sequential product space is order-isomorphic to a Euclidean Jordan algebra.

**Theorem 3 (van de Wetering).** Suppose V is a finite-dimensional sequential product space which as a locally tomographic composite with itself (i.e., V tensor V is also a sequential product space with (a1 tensor b1) & (a2 tensor b2) = (a1 & a2) tensor (b1 & b2)), then there exists a C*-algebra A such that V is isomorphic to A^sa as a Jordan algebra.

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --- | --- | --- | --- |
| Alfsen-Shultz compression (P-projection) | Defines measurement update on OUS without Hilbert space | Constructing the sequential product | Alfsen-Shultz Ch. 7-8; Niestegge (2008) |
| Spectral decomposition in OUS | Decomposes any effect a = sum lambda_i p_i with p_i orthogonal sharp | Extending product from sharp to general effects | vdW Corollary 7, Corollary 16 |
| Kadison representation theorem | Any complete OUS with bilinear positive product is C(X) | Classical algebra characterization | vdW Prop. 5-6, Kadison (1951) |
| Left-multiplication map L_a(b) = a & b | Makes the sequential product into a linear operator on V | Axiom verification, spectral analysis | vdW p.6, Prop. 2 |
| Symmetry of transition probabilities | omega_p(q) = omega_q(p) for atomic sharp effects | S4 proof route (connects to inner product symmetry) | vdW Prop. 28-29 |
| Jordan product construction | p * q = (1/2)(id + L_p - L_{p^perp})b for atomic p | Recovering Jordan structure from SP | vdW Def. 15, Lemma 32, Prop. 33 |

### Approximation Schemes

| Approximation | Small Parameter | Regime of Validity | Error Estimate | Alternatives if Invalid |
| --- | --- | --- | --- | --- |
| Finite-dimensional restriction | n = dim(V) < infinity | All finite-dim order unit spaces | Exact (no approximation) | JB-algebra theory for infinite dim (vdW Section VI) |
| Sharp-then-fuzzy extension | -- | When spectral decomposition exists | Exact (spectral decomposition is exact in finite dim) | Direct bilinear construction (if spectral decomp fails) |
| Low-dimensional examples (n=2,3) | -- | Qubit/qutrit analogues for intuition and counterexample search | No error (exact computation) | General n proof required for positive results |

## Standard Approaches

### Approach 1: Compression-Based Sequential Product via Spectral Extension (RECOMMENDED)

**What:** Define the sequential product for sharp effects using Alfsen-Shultz compressions, then extend bilinearly to all effects via spectral decomposition.

**Why standard:** This follows the structure of van de Wetering's own proof, which relies heavily on the spectral decomposition (Corollary 7) to reduce general effect computations to sharp effect computations. The compression U_e for an event e in Niestegge's framework is the OUS analogue of the Luders map a -> eae in B(H). This is the native measurement update primitive that exists for any finite-dimensional OUS with the Alfsen-Shultz property -- no Hilbert space required.

**Track record:** Van de Wetering's entire paper uses this approach. Alfsen-Shultz compressions are the foundation of their non-commutative spectral theory (1978-2003). Niestegge (2008) explicitly constructs measurement update via compressions U_e on order unit spaces and shows they satisfy the key properties: U_e is a positive projection, U_e(1) = e, and conditional probabilities are mu(f|e) = mu_hat(U_e f)/mu(e).

**Key steps:**

1. **Define C_p for sharp effects p:** For each sharp effect (projective unit) p in E(B), define the compression C_p: V -> V as the Alfsen-Shultz P-projection associated to the face generated by p. This is an idempotent positive map with C_p(1) = p.

2. **Define the self-modeling sequential product for sharp effects:** For sharp effects p, q in E(B), define p & q = C_{phi(p)}(q), where phi: E(B) -> E(M) is the tracking map. The self-modeling constraint says: testing effect p on B triggers compression C_{phi(p)} on M, which then determines the state for testing q.

   **CRITICAL DECISION POINT:** The effect algebra framing. Two options:
   - E(B) framing: p & q = C_p(q) directly on B's effects (phi enters through how the model update feeds back to B)
   - E(B x M) framing: the product lives on the composite system's effects

   Both framings must be explored. The CONTEXT.md locks this as a RESULT, not a premise.

3. **Verify bilinearity (FIRST GATE):** The map q -> C_p(q) is linear in q by construction (C_p is a linear map). The map p -> C_p(q) must be shown to extend linearly from sharp effects to general effects. Use spectral decomposition: for a = sum lambda_i p_i, define a & b = sum lambda_i (p_i & b) = sum lambda_i C_{phi(p_i)}(b). This is well-defined iff the decomposition is unique (it is, by vdW Corollary 7 and Prop. 6: C(a) is isomorphic to R^n).

   **If bilinearity fails: STOP. The approach is fundamentally wrong.**

4. **Verify S1-S3 (easy):** S1 follows from linearity of C_p in its argument. S2 is automatic in finite dimensions. S3 requires C_{phi(1)}(b) = b, i.e., the compression for the trivial test acts trivially -- this constrains phi(1) = 1_M.

5. **Verify non-associativity (early sanity check):** Exhibit explicit triple (a,b,c) with (a & b) & c != a & (b & c). If associative, the algebra is commutative (Westerbaan-Westerbaan-vdW 2020), killing the program.

6. **Verify S5-S7 (moderate):** These concern compatible effects. S5 (associativity for compatible effects): when a | b, we need a & (b & c) = (a & b) & c. S6 (additivity of compatibility): if a | b then a | b^perp, plus closure under addition. S7 (multiplicativity of compatibility): if a | b and a | c then a | (b & c). These follow from the compression algebra structure: compatible compressions commute (Niestegge Lemma 3.3: U_e U_f = U_f U_e when e <= f).

7. **Verify S4 (HARD, DECISIVE):** If a & b = 0, must show b & a = 0. For the self-modeling product: if C_{phi(a)}(b) = 0, must show C_{phi(b)}(a) = 0. This is where the tracking map phi's properties are critical. Three proof routes:
   - Route A: Show phi preserves orthogonality (phi(a) perp phi(b) whenever a perp b in some SP sense) -- then compression orthogonality gives symmetry
   - Route B: Construct an inner product on V such that <a & b, c> = <b, a & c> (van de Wetering's inner product characterization from arXiv:1803.08453)
   - Route C: Prove via faithfulness -- if phi is isometric (injective on states), orthogonality relations are preserved bidirectionally

8. **Classify the EJA (if S1-S7 hold):** Invoke van de Wetering's Theorem 1 to conclude V is an EJA. Determine which type(s) from the Jordan-von Neumann-Wigner classification: M_n(R)^sa, M_n(C)^sa, M_n(H)^sa, spin factors V_n, or Albert algebra M_3(O)^sa.

**Known difficulties at each step:**

- Step 2: The framing choice (E(B) vs E(B x M)) fundamentally changes what the product means. Both must be explored.
- Step 3: Bilinearity in the first argument (the "testing" argument) requires that spectral decomposition is compatible with the compression structure. This is guaranteed in the standard OUS spectral theory (Alfsen-Shultz) but must be verified for the phi-parametrized construction.
- Step 7: S4 is the single point of failure. The proof will be the longest and most detailed. If it is short, something is wrong (Pitfall P3).

### Approach 2: Direct Algebraic Construction (FALLBACK)

**What:** Instead of going through compressions, directly construct a bilinear map on E(B) satisfying S1-S7 by algebraic manipulation of the self-modeling constraint.

**When to switch:** If the compression-based construction fails at bilinearity (Step 3 above), or if the compression structure is insufficient to capture the self-modeling update.

**Tradeoffs:** Loses the geometric intuition of compressions as measurement updates. May produce a product that satisfies axioms but has unclear operational meaning. More algebraically intensive.

### Anti-Patterns to Avoid

- **Importing Hilbert space structure:** ANY use of sqrt(a), trace, inner product, density matrices, or Luders rule in the construction is circular. The update map must use ONLY order unit space primitives.
  - _Example:_ Writing a & b = sqrt(a) b sqrt(a) assumes a C*-algebra structure. The whole point is to DERIVE that structure.

- **Checking axioms for the standard quantum product:** If a proof step works identically for any sequential product (not specifically the self-modeling one), it proves nothing. Every proof must reference specific properties of the self-modeling update.
  - _Example:_ "S4 holds because orthogonality is symmetric" -- this is true in B(H) but is exactly what must be PROVED for the self-modeling product.

- **Substituting Gudder-Greechie axioms for van de Wetering axioms:** The axiom sets differ (especially S4). All references must be pinned to arXiv:1803.11139 Definition 2.
  - _Example:_ Gudder-Greechie's S4 concerns commutativity of compatible effects; vdW's S4 concerns symmetry of orthogonality. These are logically distinct.

- **Assuming the framing (E(B) vs E(B x M)) prematurely:** The correct framing is a RESULT, not a premise. Explore both.

## Existing Results to Leverage

**This section is MANDATORY.** The planner uses this to scope task effort. Do NOT re-derive these.

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
| --- | --- | --- | --- |
| vdW Theorem 1 | Finite-dim SP space => order-isomorphic to EJA | arXiv:1803.11139, p.15 | INVOKE once S1-S7 verified. Do not re-prove. |
| vdW Theorem 3 | Fin-dim SP space + locally tomo composite => C*-algebra | arXiv:1803.11139, p.19 | Downstream (Phase 2). Note for planning. |
| Spectral decomposition | Any a in E has a = sum lambda_i p_i, p_i orthogonal sharp | arXiv:1803.11139, Cor. 7 | Use for bilinear extension from sharp to general effects |
| Classical algebra C(a) | C(a) = span{a^n, (a^perp)^n} is isomorphic to R^n | arXiv:1803.11139, Prop. 6 | Commutative subalgebra structure |
| Sharp effects form a lattice | With covering property and well-defined rank | arXiv:1803.11139, Prop. 11, 22, 23 | Structural constraint on compression lattice |
| Symmetry of transition probabilities | omega_p(q) = omega_q(p) for atomic sharp p, q | arXiv:1803.11139, Prop. 28-29 | S4 proof route: if the self-modeling product reproduces this symmetry, S4 follows |
| Homogeneity from spectral decomposition | SP space has homogeneous positive cone | arXiv:1803.11139, Prop. 8 | Intermediate result in S1-S7 => EJA proof |
| Self-duality from S4 | S4 + homogeneity => self-dual cone (inner product exists) | arXiv:1803.11139, Prop. 30 | Self-duality is the key consequence of S4 |
| Associativity => commutativity | For normal sequential effect algebras | Westerbaan-Westerbaan-vdW, Quantum 4, 378 (2020) | Non-associativity sanity check: CITE, do not re-derive |
| Uniqueness of SP on simplices | Pointwise multiplication is the unique SP on a simplex satisfying S1-S7 | Gudder-Greechie (2002) | Classical limit check: self-modeling product on simplices MUST give pointwise mult |
| Niestegge compression properties | U_e is positive projection, U_e(1) = e, U_eU_f = U_fU_e when e <= f, conditional prob = mu_hat(U_e f)/mu(e) | Niestegge (2008), Prop. 3.1, Lemma 3.3 | Foundation for compression-based construction |
| Koecher-Vinberg theorem | Fin-dim homogeneous self-dual ordered vector space <=> EJA | Koecher (1957), Vinberg (1961) | The bridge theorem invoked by vdW Thm 1 |

**Key insight:** The entire downstream machinery (EJA classification, Koecher-Vinberg, Hanche-Olsen, Barnum-Wilce) is established and published. Re-derivation wastes context and risks introducing errors. The ONLY novel work in this phase is: (1) defining the self-modeling sequential product, (2) verifying S1-S7 for THAT specific product.

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
| --- | --- | --- | --- |
| Prop. 2 (vdW): a & (lambda b) = lambda(a & b) | Scalar multiplication passes through | arXiv:1803.11139, p.6 | Follows from S1 + S2 |
| Prop. 2.3 (vdW): (lambda a) & b = lambda(a & b) for lambda in [0,1] | First-argument homogeneity | arXiv:1803.11139, p.6 | Follows from S1 + S2 + S6 |
| Prop. 1 (vdW): a & 0 = 0, a & b <= a | Basic inequalities | arXiv:1803.11139, p.5 | Direct from axioms |
| Lemma 13 (vdW): b & a = 0 => b & ceil(a) = 0 | Orthogonality lifts to ceilings | arXiv:1803.11139, p.9 | Used in S4 arguments |
| Prop. 12 (vdW): sharp effects p, a compatible => p & a sharp iff a sharp; p ^ a = p & a | Meet of compatible sharp effects | arXiv:1803.11139, p.9 | S5-S7 verification |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| --- | --- | --- | --- | --- |
| arXiv:1803.11139 | van de Wetering | 2018/2019 | PRIMARY: axiom source, theorems | Exact Def. 2 (S1-S7), Thm 1, Thm 3 |
| arXiv:1803.08453 | van de Wetering | 2018 | Three characterizations of SP | Inner product symmetry route to S4 uniqueness |
| arXiv:2004.12749 | Westerbaan, Westerbaan, vdW | 2020 | Associativity => commutativity | Sanity check for non-associativity |
| Rep. Math. Phys. 49 (2002) | Gudder, Greechie | 2002 | Original SEA definition | Classical uniqueness; comparison axioms |
| Found. Phys. 38, 783 (2008) | Niestegge | 2008 | Compressions on OUS for measurement | U_e definition, conditional probability formula |
| Geometry of State Spaces (2003) | Alfsen, Shultz | 2003 | Compression theory | P-projections, projective units, face structure |
| arXiv:2102.01628 | Jenccova | 2021 | Spectrality comparison in OUS | Alfsen-Shultz vs Foulis approaches to spectral theory |

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
| --- | --- | --- | --- |
| SymPy | sympy.matrices, sympy.core | Symbolic axiom verification on low-dim examples | Exact arithmetic avoids floating-point masking of zero/nonzero distinctions |
| Python 3 | Standard library | Test harness for S1-S7 checks | Available, lightweight |

### Supporting Tools

| Tool | Purpose | When to Use |
| --- | --- | --- |
| NumPy/SciPy | Numerical cross-checks on larger examples | After symbolic verification succeeds, for confidence-building |
| matplotlib | Visualize state spaces and effect cones in low dimensions | If geometric intuition is needed for S4 analysis |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
| --- | --- | --- |
| SymPy | Mathematica / Maple | More powerful CAS but less portable; SymPy suffices for n <= 4 |
| Custom Python harness | SageMath Jordan algebra module | SageMath has built-in Jordan algebra support but may over-abstract away from the sequential product |

### Computational Feasibility

| Computation | Estimated Cost | Bottleneck | Mitigation |
| --- | --- | --- | --- |
| Symbolic S1-S7 check on M_2(C)^sa (4-dim) | < 1 minute | None | Direct |
| Symbolic S4 check on M_3(C)^sa (9-dim) | < 5 minutes | Symbolic matrix multiplication | Use sparse representations |
| Non-associativity witness search | < 1 minute | Finding specific triple | Random sampling then exact verification |
| General S4 proof/disproof | N/A (analytical) | This is proof work, not computation | Computation supports but cannot replace the proof |

**Installation / Setup:**
```bash
# Standard scientific Python stack -- likely already installed
pip install sympy numpy scipy
```

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| --- | --- | --- | --- |
| Positive control: Luders product on M_2(C)^sa | Test harness correctness | Define a & b = sqrt(a) b sqrt(a), check all S1-S7 | All pass (this IS the standard SP) |
| Negative control: plain matrix mult on M_2(C)^sa | S4 detection works | Define a & b = ab (matrix product), check S4 | S4 FAILS (matrix mult is not symmetric in orthogonality) |
| Classical limit: simplex check | Construction correctness | Apply self-modeling product when B is a simplex | Must give pointwise multiplication a & b = a * b |
| Effect range: 0 <= a & b <= 1 | Well-definedness | For every a, b in [0,1]_V, verify a & b in [0,1]_V | Always satisfied |
| Unit: 1 & a = a | S3 | Direct computation | Holds by construction if phi(1) = 1 |
| Complement consistency | a & a^perp = 0 for sharp a | Direct computation | Follows from compression orthogonality |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| --- | --- | --- | --- |
| Classical (B = simplex) | All effects diagonal in a fixed basis | a & b = a * b (pointwise) | Gudder-Greechie (2002) |
| Quantum (B = M_n(C)^sa, phi = identity) | Standard quantum mechanics | a & b = sqrt(a) b sqrt(a) (Luders) | vdW (2018); this is the positive control |
| Trivial model (M = R, phi = constant) | No model tracking | a & b = a * b (sequential product degenerates) | Must check: trivial model should give trivial product |
| Maximal model (M = B, phi = id) | Perfect self-model | Should satisfy S4 (user's primary prediction) | No prior verification -- THIS is the novel claim |

### Numerical Validation

| Test | Method | Tolerance | Reference Value |
| --- | --- | --- | --- |
| S4 on random effect pairs in M_2(C)^sa | Symbolic computation with parametric effects | Exact zero | Known to hold for Luders product |
| Non-associativity witness | Compute (a & b) & c - a & (b & c) for specific triple | Nonzero | Known nonzero for Luders product on M_2(C)^sa |
| Jordan product recovery | Compute (1/2)(a & b + b & a) and compare to Jordan product | Exact match | Must match for any SP (vdW Thm 2) |

### Red Flags During Computation

- If S4 proof is shorter than the S1-S3 proofs combined, something is wrong -- S4 is the HARDEST axiom
- If a proof step works identically for ANY sequential product (not specifically the self-modeling one), it proves nothing about the self-modeling case
- If Hilbert space structure (sqrt, trace, inner product, density matrix) appears anywhere in the construction, circularity has occurred
- If the sequential product turns out to be associative, the program is dead (Westerbaan-Westerbaan-vdW 2020)
- If the sequential product on a simplex does NOT reduce to pointwise multiplication, the construction is wrong
- If S4 "holds" only for effects aligned with a preferred basis, the example is too symmetric -- test more diverse cases

## Common Pitfalls

### Pitfall 1: Circularity -- Importing Hilbert Space Structure into the Update Map

**What goes wrong:** The self-modeling update rule uses Luders' rule, sqrt, inner product, or any C*-algebra structure, making the derivation circular.
**Why it happens:** The standard quantum product a & b = sqrt(a) b sqrt(a) is the most familiar example. It is natural to formalize "test-update-test" using this formula, but doing so assumes the conclusion.
**How to avoid:** Every operation in the construction must be expressible using ONLY: (1) the order structure of V, (2) the effect space [0,1]_V, (3) the compression maps C_p, (4) the tracking map phi. Audit every step for Hilbert space imports.
**Warning signs:** Any occurrence of "let H be the Hilbert space," "take the spectral decomposition in B(H)," or "use the Luders rule."
**Recovery:** If circularity is detected, strip back to the Alfsen-Shultz compression framework and rebuild using only OUS primitives.

### Pitfall 2: Wrong Effect Algebra Carrier (E(B) vs E(B x M))

**What goes wrong:** The sequential product is defined on the wrong space. E(B) gives a product on body effects; E(B x M) gives a product on composite effects. These are different algebras with potentially different axiom satisfaction.
**Why it happens:** The self-modeling operation involves BOTH B and M. The product lives "on B" operationally, but the update goes through M.
**How to avoid:** Explore both framings explicitly. For E(B): the product a & b encodes "test a on B, update M via phi, test b on B." For E(B x M): the product encodes joint effects. The correct framing is determined by which one yields a well-defined sequential product satisfying S1-S7.
**Warning signs:** Axiom proofs that never mention M (suggests E(B) adopted without justification); proofs treating B and M symmetrically (the self-model is asymmetric).
**Recovery:** If one framing fails, try the other. Both failing is a clean negative result.

### Pitfall 3: S4 Assumed Rather Than Proved

**What goes wrong:** S4 is declared to hold without a rigorous proof specific to the self-modeling construction.
**Why it happens:** S4 is subtle and the proof is hard. The temptation is to argue "physically reasonable" or appeal to quantum mechanics where S4 does hold.
**How to avoid:** The S4 proof must be the longest, most detailed axiom proof. It must reference specific properties of the tracking map phi. Multiple proof routes should be attempted: orthogonality preservation, inner product symmetry, faithfulness.
**Warning signs:** S4 proof shorter than 1 page; proof uses unestablished properties of the update map; proof works for any update map.
**Recovery:** If S4 fails, proceed to SPFM-05 (characterize failure) and consider D'Ariano backup.

### Pitfall 4: Conflating Spectral Decomposition in OUS with Spectral Decomposition in B(H)

**What goes wrong:** The spectral decomposition a = sum lambda_i p_i is used as if p_i were orthogonal projections in a Hilbert space, with all the additional structure that implies.
**Why it happens:** In B(H), sharp effects ARE orthogonal projections, and the spectral theorem gives eigenvalue decomposition. In a general OUS, sharp effects are defined purely order-theoretically (Def. 7: a & a^perp = 0 and a & a = a), and the spectral decomposition is the OUS version (Corollary 7).
**How to avoid:** Use ONLY the properties established in vdW's paper for the spectral decomposition: the p_i are orthogonal sharp effects, the lambda_i are positive scalars, and the decomposition is unique (Prop. 23).
**Warning signs:** Using "eigenvalues" or "eigenvectors" before Jordan algebra structure is established; invoking trace or inner product in spectral arguments.
**Recovery:** Re-derive the needed spectral property from vdW's Propositions 6-10 directly.

## Level of Rigor

**Required for this phase:** Formal proof (not physicist's proof, not numerical evidence alone)

**Justification:** This phase establishes the mathematical foundation for the entire v2.0 chain. The axiom verifications must be rigorous proofs that would survive peer review at a journal like J. Math. Phys. or Foundations of Physics. Numerical evidence supports but cannot replace formal proof -- a counterexample to S4 found numerically IS sufficient to disprove S4, but numerical verification of S4 for specific cases does NOT prove S4 in general.

**What this means concretely:**

- Each axiom verification must be a complete proof with all steps justified
- S4 proof (or disproof) must handle ALL effects, not just generic ones or low-dimensional examples
- Non-associativity must be exhibited with an explicit triple and exact computation
- The bilinear extension from sharp to general effects must be shown to be well-defined (not just plausible)
- Classical limit (simplex case) must be verified exactly, not approximately

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| --- | --- | --- | --- |
| Gudder-Greechie axioms on effect algebras | vdW axioms on order unit spaces | 2018 (arXiv:1803.11139) | OUS setting is more concrete; S2 (continuity) replaces normality; Theorem 1 gives clean EJA result |
| Multiple sequential products satisfying G-G axioms | Three characterizations of UNIQUE Luders product | 2018 (arXiv:1803.08453) | Invariance under order isomorphisms, inner product symmetry, or invertibility preservation each uniquely characterize Luders |
| Classification unknown for general SEAs | Three types: commutative, B(H), spin factor | 2020 (arXiv:2004.12749) | Normal SEAs decompose into these three types; associativity forces commutativity |
| Ad hoc Jordan algebra constructions | Systematic compression-based approach | 2003 (Alfsen-Shultz book) | Compressions provide the natural "measurement update" primitive in OUS |

**Superseded approaches to avoid:**

- **Gudder-Greechie axioms directly:** Their axiom set differs from vdW's (especially regarding S4 and continuity). Using G-G axioms would mean checking the wrong conditions. Always use vdW Definition 2.
- **Assuming spectral duality (Alfsen-Shultz full theory):** The full Alfsen-Shultz spectral duality theory assumes more structure than we have at the start. vdW's proof builds spectral theory from S1-S7 directly, without assuming spectral duality a priori. Use vdW's internal spectral decomposition results (Corollary 7), not the full Alfsen-Shultz machinery.

## Open Questions

1. **Does the compression-based construction extend bilinearly from sharp to general effects?**
   - What we know: For sharp effects, C_p is well-defined. Spectral decomposition a = sum lambda_i p_i exists. Linear extension in the second argument is automatic (compressions are linear maps). First-argument linearity via spectral decomposition is the question.
   - What's unclear: Whether the phi-parametrized construction preserves the uniqueness of spectral decomposition needed for well-definedness.
   - Impact on this phase: This is the FIRST GATE. If bilinearity fails, the approach is dead.
   - Recommendation: Verify bilinearity first, before any axiom checking. Test on the qubit case (dim 4, M_2(C)^sa) as the simplest non-trivial example.

2. **Which effect algebra framing is correct: E(B) or E(B x M)?**
   - What we know: vdW's axioms are for a sequential product on a single system's effects. The self-model involves two systems (B and M).
   - What's unclear: Whether the operationally natural product (test on B, update M, test on B) is best formalized as a product on E(B) with phi as a parameter, or as a product on E(B x M) with a specific structure.
   - Impact on this phase: Different framings may yield different axiom satisfaction profiles.
   - Recommendation: Start with E(B) framing (simpler, more natural for "testing B"), but keep E(B x M) as fallback. The answer is a RESULT of the phase.

3. **What properties must phi satisfy for S4 to hold?**
   - What we know: Three possible outcomes identified in CONTEXT.md: S4 holds for all valid phi; S4 holds only for constrained phi; S4 fails for all phi.
   - What's unclear: The precise condition. The user's prediction: isometric phi (dim M >= dim B) should give S4. Coarse-graining phi (dim M < dim B) might not.
   - Impact on this phase: Determines the strength of the result. Universal => self-modeling alone suffices. Constrained => additional assumption needed. Failure => backup route.
   - Recommendation: Test S4 systematically: isometric phi first, then coarse-graining. If isometric gives S4, identify exactly which property of isometry is used.

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| --- | --- | --- | --- |
| Bilinearity (Step 3) | Spectral extension not well-defined for phi-parametrized product | Direct algebraic construction of bilinear map (Approach 2) | HIGH -- must redesign the entire construction |
| S4 for isometric phi | Model update breaks orthogonality symmetry even for faithful models | SPFM-05 (characterize failure) then D'Ariano backup (Phase contingency) | MEDIUM -- characterization is valuable; D'Ariano route is independent |
| S4 for coarse-graining phi | Information loss breaks symmetry | Restrict to isometric phi and accept this as an additional assumption | LOW -- the assumption "faithful model" is physically natural |
| Non-associativity fails | Product is associative => algebra is commutative | STOP -- sequential product route is dead; must rethink construction entirely | FATAL |

**Decision criteria:**
- Abandon bilinear extension if it fails for the qubit case (n=2) -- if it doesn't work in the simplest case, it won't work generally
- Abandon S4 for general phi if it fails for isometric phi in the qubit case (n=2) -- this is the most favorable case; failure here is decisive
- Accept constrained phi if S4 holds for isometric but not coarse-graining -- document the constraint and its physical interpretation
- Abandon the sequential product route entirely if the product is associative -- this is a clean negative result

## Caveats and Self-Critique

1. **What assumption am I making that might be wrong?** I assume compressions provide the "right" formalization of measurement update in the self-modeling context. The self-modeling update might have structure that compressions cannot capture (e.g., non-idempotent maps, or maps that depend on the state being measured, not just the effect).

2. **What alternative approach did I dismiss too quickly?** The E(B x M) framing. I recommend starting with E(B) because it's simpler, but the composite framing might be the one that actually works -- the self-modeling constraint IS a statement about B-M interaction, and a product on E(B x M) might naturally encode this.

3. **What limitation of the recommended method am I understating?** The bilinear extension from sharp to general effects via spectral decomposition is less trivial than it appears. In vdW's paper, the bilinear extension of the Jordan product (Definition 16) works because the Jordan product of atomic sharp effects has nice symmetry properties (Lemma 32). The sequential product extension does not have these symmetry properties in general, and the phi-parametrization adds further complexity.

4. **Is there a simpler method I overlooked?** Possibly: instead of defining the product compression-by-compression and then extending, one could try to define it directly on the full effect space using the operational semantics (conditional probability formula). Niestegge's conditional probability mu(f|e) = mu_hat(U_e f)/mu(e) might provide a direct bilinear product without the spectral extension detour.

5. **Would a specialist disagree with my recommendation?** A specialist in operator algebras might argue that the compression-based approach is too conservative -- that the self-modeling constraint should directly yield a Jordan product (skipping the sequential product intermediate). This is possible but would bypass the van de Wetering machinery, which is the project's chosen route.

## Sources

### Primary (HIGH confidence)

- [van de Wetering, "Sequential product spaces are Jordan algebras," J. Math. Phys. 60, 062201 (2019), arXiv:1803.11139](https://arxiv.org/abs/1803.11139) -- S1-S7 definitions, Theorem 1 (SP => EJA), Theorem 3 (SP + local tomo => C*). THE axiom source.
- [van de Wetering, "Three characterisations of the sequential product," J. Math. Phys. 59, 082202 (2018), arXiv:1803.08453](https://arxiv.org/abs/1803.08453) -- Uniqueness of Luders product; inner product symmetry characterization (potential S4 proof route).
- [Westerbaan, Westerbaan, van de Wetering, "The three types of normal sequential effect algebras," Quantum 4, 378 (2020), arXiv:2004.12749](https://arxiv.org/abs/2004.12749) -- Associativity => commutativity; three-type classification.
- [Gudder, Greechie, "Sequential products on effect algebras," Rep. Math. Phys. 49, 87-111 (2002)](https://www.sciencedirect.com/science/article/abs/pii/S0034487702800076) -- Original SEA definition; classical uniqueness result.
- [Niestegge, "A Representation of Quantum Measurement in Order-Unit Spaces," Found. Phys. 38, 783-795 (2008), arXiv:1001.3633](https://arxiv.org/abs/1001.3633) -- Compressions U_e on OUS; conditional probability formula; P-projection theory.
- [Alfsen, Shultz, "Geometry of State Spaces of Operator Algebras," Birkhauser (2003)](https://link.springer.com/book/10.1007/978-1-4612-0019-2) -- Compression/P-projection theory foundation; non-commutative spectral theory.

### Secondary (MEDIUM confidence)

- [Jenccova, "Geometric and algebraic aspects of spectrality in order unit spaces: a comparison," arXiv:2102.01628 (2021)](https://arxiv.org/abs/2102.01628) -- Comparison of Alfsen-Shultz and Foulis spectral theories; useful for understanding what spectral structure is available.
- [Barnum, Wilce, "Local tomography and the Jordan structure of quantum theory," Found. Phys. 44, 192-212 (2014), arXiv:1202.4513](https://arxiv.org/abs/1202.4513) -- Jordan + local tomo + qubit => complex QM (downstream, Phase 2).
- [Barnum, Graydon, Wilce, "Composites and categories of Euclidean Jordan algebras," Quantum 4, 359 (2020), arXiv:1606.09331](https://arxiv.org/abs/1606.09331) -- Compositionality excludes exceptional types (downstream).

### Tertiary (LOW confidence)

- [Gudder, "Open problems for sequential effect algebras," Int. J. Theor. Phys. 44, 2199 (2005)](https://link.springer.com/content/pdf/10.1007/s10773-005-8015-1.pdf) -- Historical context; open problems (some now resolved by vdW and WWvdW).
- ~/repos/blog/research/quantum-extension/draft.md -- Project motivation; algebraic genericity chain; classical limit expectations.

## Metadata

**Confidence breakdown:**

- Mathematical framework: HIGH -- OUS theory, compressions, and spectral decompositions are well-established (Alfsen-Shultz, Niestegge, van de Wetering)
- Standard approaches: MEDIUM -- the compression-based construction is novel; the approach is modeled on established methods but has not been executed before
- Computational tools: HIGH -- SymPy/NumPy are standard and sufficient for the proof-support role
- Validation strategies: HIGH -- positive/negative controls are well-defined; classical limit benchmark is known exactly

**Research date:** 2026-03-20
**Valid until:** Indefinitely for the mathematical framework (published theorems). Tool versions may change but SymPy is stable for the required functionality.
