# Phase 5: Local Tomography from B-M Compositionality - Research

**Researched:** 2026-03-21
**Domain:** Quantum foundations / Jordan algebras / Generalized probabilistic theories / Compositionality
**Confidence:** MEDIUM

## Summary

Phase 5 must bridge the gap between "independently accessible body B and model M" and "local tomography on B tensor M," then invoke Hanche-Olsen's theorem to promote the Euclidean Jordan algebra established in Phase 4 to a C\*-algebra. This is the second genuinely novel argument in the project (after the S4 proof in Phase 4). The mathematical framework is well-established: three published theorems (van de Wetering Theorem 3, Hanche-Olsen 1985, Barnum-Wilce 2014) collectively say "EJA + locally tomographic composite + qubit = C\*-algebra = complex QM." The novelty is entirely in Step 1: proving that the self-modeling B-M structure provides a locally tomographic composite.

The core difficulty is that "independent accessibility" (the self-model can probe B and M separately) is logically weaker than "local tomography" (product measurements on B and M suffice to determine the joint state). The gap is the entangled sector: there might exist joint states of B tensor M that are invisible to product measurements. For complex quantum mechanics, local tomography holds automatically (dim(M_n(C)^sa tensor M_m(C)^sa) = n^2 * m^2 as real vector spaces, matching the product of dimensions). For real QM, quaternionic QM, spin factors V_n with n >= 4, and the Albert algebra, local tomography fails. The self-modeling constraint must provide the additional structure that closes this gap -- specifically, that M's role as a faithful model of B forces the composite state space to have the right dimension.

Phase 5 inherits from Phase 4: S1-S7 all proved for the self-modeling sequential product (S4 via facial orthogonality, phi-independent); the OUS is order-isomorphic to an EJA (van de Wetering Theorem 1); for M_2(C)^sa the EJA is the spin factor V_3; the corrected product formula (Eq. 04-06.4) with f = sqrt for faithful self-modeling.

**Primary recommendation:** Formalize "independently accessible" in the GPT / order unit space framework as a non-signaling composite with product-form sequential product on B tensor M. Prove that B-M self-modeling faithfulness forces the composite to satisfy van de Wetering's Theorem 3 conditions (locally tomographic composite). Then invoke Barnum-Wilce + Hanche-Olsen to exclude non-complex types. The qubit condition is satisfied because Phase 4 established V_3 = M_2(C)^sa for the qubit self-model.

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| --- | --- | --- | --- | --- |
| ref-barnum2023: Barnum-Ududec-van de Wetering (2023) arXiv:2306.00362 | method | Compositionality constraints on Jordan algebras; may simplify geometric assumptions | read, cite | plan, execution, writing |
| ref-vdw2018: van de Wetering arXiv:1803.11139 | benchmark / chain endpoint | Theorem 3: SP space + locally tomographic composite = C\*-algebra | read, use, cite | plan, execution, verification, writing |
| Hanche-Olsen (1985): LNM 1132 | method | JB-algebra with tensor products are C\*-algebras -- THE promotion theorem | read, use, cite | plan, execution, verification, writing |
| Barnum-Wilce arXiv:1202.4513 | method | EJA + local tomography + qubit = complex QM | read, use, cite | plan, execution, verification, writing |
| Barnum-Graydon-Wilce arXiv:1606.09331 | method | Composites of EJAs exclude Albert algebra; compositionality constraints | read, use, cite | plan, execution, verification |
| Niestegge arXiv:2001.11421 | supporting | Local tomography in quantum logical setting; spin factor subtleties | read, cite | execution, writing |
| Phase 4 results (S1-S7 proofs, EJA classification) | prior artifact | S1-S7 proved, EJA = V_3 for qubits, corrected product formula | use | plan, execution, verification |

**Missing or weak anchors:**
- No prior work formalizes "independent accessibility" in the OUS/GPT framework as a compositionality constraint that implies local tomography. This is novel territory. The closest references are Barnum-Wilce (who assume local tomography) and Hardy (who derives it from other axioms). The gap between "independent accessibility" and "local tomography" is the central open question of this phase.
- The Hanche-Olsen paper (1985) is in a Springer LNM volume that is not freely accessible. The theorem statement is well-documented in secondary sources (Barnum-Wilce 2014, van de Wetering 2019), but the precise technical conditions should be verified against the original.

## Conventions

| Choice | Convention | Alternatives | Source |
| --- | --- | --- | --- |
| Sequential product | a & b (non-commutative) | a . b | arXiv:1803.11139 Def. 2 (Phase 4 convention) |
| Jordan product | a * b = (1/2)(a & b + b & a) | a o b | arXiv:1803.11139 (Phase 4 convention) |
| Effects | [0,1]\_V = {a in V : 0 <= a <= 1} | E(V) | arXiv:1803.11139 |
| Local tomography | dim(S(A tensor B)) = dim(S(A)) * dim(S(B)) | "product measurements determine joint state" | Barnum-Wilce (2014) |
| Composite sequential product | (a1 tensor b1) & (a2 tensor b2) = (a1 & a2) tensor (b1 & b2) | non-product composites | vdW Theorem 3 |
| Units | Natural (dimensionless algebraic quantities) | -- | project convention |
| EJA types | M\_n(K)^sa for K in {R, C, H}; V\_n; M\_3(O)^sa | -- | JVW classification |

**CRITICAL: All equations and results below use these conventions. The key distinction: "local tomography" is a condition on the COMPOSITE system's state space dimension. "Independent accessibility" is a condition on the OPERATIONAL capabilities of the self-model. These are NOT equivalent.**

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in This Phase |
| --- | --- | --- | --- |
| dim(S(A tensor B)) = dim(S(A)) * dim(S(B)) | Local tomography condition | Barnum-Wilce (2014) | The condition to prove |
| (a1 tensor b1) & (a2 tensor b2) = (a1 & a2) tensor (b1 & b2) | Product-form sequential product on composite | vdW Theorem 3 | Structural condition for C\*-algebra promotion |
| V is EJA and V tensor V is SP space => V is C\*-algebra | Van de Wetering Theorem 3 | arXiv:1803.11139, p.19 | The payoff theorem |
| JB-algebra + tensor product = C\*-algebra | Hanche-Olsen's theorem | LNM 1132 (1985) | The Jordan-to-C\* promotion |
| EJA + local tomo + qubit = complex QM | Barnum-Wilce theorem | arXiv:1202.4513 | Selects complex type from JVW classification |
| a & b = sum\_i lambda\_i C\_{p\_i}(b) + sum\_{i<j} sqrt(lambda\_i lambda\_j) P\_{ij}(b) | Corrected sequential product (Phase 4) | Eq. 04-06.4 | The concrete product formula that must extend to composites |
| dim(M\_n(R)^sa) = n(n+1)/2 | Real self-adjoint matrix dimension | standard | Dimension counting for local tomography failure |
| dim(M\_n(C)^sa) = n^2 | Complex Hermitian matrix dimension | standard | Dimension counting for local tomography success |
| dim(M\_n(H)^sa) = n(2n-1) | Quaternionic Hermitian matrix dimension | standard | Dimension counting for local tomography failure |
| dim(V\_n) = n + 1 | Spin factor dimension | standard | V\_3 = 4 = dim(M\_2(C)^sa) confirms qubit identification |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --- | --- | --- | --- |
| GPT composite construction | Defines the composite state space S(A tensor B) in the GPT framework | Formalizing B-M composite structure | Plavala (2023) arXiv:2103.07469 |
| Non-signaling constraint | Restricts composites to those where marginals are well-defined | Constraining admissible composites | Barnum-Wilce (2014) |
| Dimension counting | Compares dim(S(A tensor B)) with dim(S(A)) * dim(S(B)) | Checking local tomography | Hardy (2001), Barnum-Wilce (2014) |
| Hanche-Olsen tensor product criterion | Tests whether EJA admits a well-behaved tensor product | Promoting EJA to C\*-algebra | Hanche-Olsen (1985) |
| Type exclusion by dimension | Shows non-complex EJA types fail local tomography by dimension mismatch | Excluding R, H, spin, Albert types | Barnum-Wilce (2014), BGW (2020) |
| Product-form SP extension | Extends sequential product to composite: (a tensor b) & (c tensor d) = (a & c) tensor (b & d) | Verifying vdW Theorem 3 conditions | arXiv:1803.11139 Theorem 3 |

### Approximation Schemes

| Approximation | Small Parameter | Regime of Validity | Error Estimate | Alternatives if Invalid |
| --- | --- | --- | --- | --- |
| Finite-dimensional restriction | dim(V) < infinity | All finite-dim OUS | Exact | JB-algebra theory for infinite dim |
| Simple EJA assumption | -- | When EJA has no superselection sectors | Exact (reduces to simpler analysis) | Handle direct sums explicitly |
| Qubit (n=2) as base case | n = dim(Hilbert space) = 2 | V\_3 = M\_2(C)^sa | Exact | General n needed for full result |

## Standard Approaches

### Approach 1: Dimension-Counting Route via Product SP Extension (RECOMMENDED)

**What:** Construct the composite B tensor M as an order unit space with a product-form sequential product, show the composite state space dimension matches the local tomography requirement, then invoke van de Wetering Theorem 3 and Barnum-Wilce.

**Why standard:** This follows the logical structure of vdW Theorem 3 directly. The key insight: if V is a sequential product space (established in Phase 4), and V tensor V with the product-form sequential product is also a sequential product space, then V is a C\*-algebra. The self-modeling structure provides the composite: B and M are both modeled by the same EJA (Phase 4), and the B-M composite is the natural product system.

**Track record:** Van de Wetering uses this in Theorem 3 of arXiv:1803.11139. Barnum-Wilce (2014) use the same framework. Barnum-Graydon-Wilce (2020) provide the most detailed analysis of composites of EJAs.

**Key steps:**

1. **Formalize "independently accessible B and M" in the OUS framework:** Define the composite order unit space V\_BM with effects E(V\_BM) containing product effects a\_B tensor b\_M. "Independent accessibility" means: for every effect a on B and every effect b on M, the product effect a tensor b is a valid effect on BM, and measuring a tensor b gives marginal probabilities consistent with measuring a on B alone and b on M alone (non-signaling).

2. **Define the product-form sequential product on V\_BM:** For product effects, (a\_B tensor b\_M) & (c\_B tensor d\_M) = (a\_B & c\_B) tensor (b\_M & d\_M). Extend bilinearly. This uses the Phase 4 sequential product on each factor.

3. **Verify S1-S7 for the composite:** S1-S3 extend trivially from the factors. S4 (symmetry of orthogonality) on the composite requires: if (a tensor b) & (c tensor d) = 0, then (c tensor d) & (a tensor b) = 0. Since (a tensor b) & (c tensor d) = (a & c) tensor (b & d), this is zero iff a & c = 0 or b & d = 0. By Phase 4's S4 on each factor, this symmetry is inherited. S5-S7 similarly extend.

4. **Check local tomography (the hard step):** Show that the state space of V\_BM has dimension dim(S(V\_B)) * dim(S(V\_M)). This is where the self-modeling constraint enters: because M faithfully tracks B, the B-M correlation state has full rank on the product state space, which forces the composite to be locally tomographic.

   **The argument structure:**
   - The self-model M tracks B faithfully (established in Phase 4: phi is an isomorphism for faithful self-modeling, selecting f = sqrt).
   - Faithful tracking means the B-M state rho\_BM separates product effects: if Tr(rho\_BM (a tensor b)) = 0 for all product effects a tensor b, then rho\_BM = 0.
   - This separability of the B-M state forces dim(S(V\_BM)) <= dim(S(V\_B)) * dim(S(V\_M)).
   - The non-signaling constraint gives dim(S(V\_BM)) >= dim(S(V\_B)) * dim(S(V\_M)) (product states exist).
   - Together: dim(S(V\_BM)) = dim(S(V\_B)) * dim(S(V\_M)). This IS local tomography.

5. **Invoke van de Wetering Theorem 3:** V is an SP space, V tensor V with product SP is also an SP space, therefore V embeds in a C\*-algebra.

6. **Invoke Barnum-Wilce:** Since V\_3 = M\_2(C)^sa (Phase 4 established this for qubits), at least one system has qubit structure. By Barnum-Wilce: EJA + local tomography + qubit = complex QM. This excludes M\_n(R)^sa, M\_n(H)^sa, V\_n for n >= 4, and M\_3(O)^sa.

7. **Exhibit the C\*-algebra involution:** The C\*-algebra A satisfying A^sa = V is determined. The involution \* on A is the unique anti-linear involution whose fixed-point set is V. On M\_n(C), this is just the conjugate transpose: (a + ib)\* = a - ib for a, b in M\_n(C)^sa. Exhibit this explicitly.

**Known difficulties at each step:**

- Step 1: "Independent accessibility" must be formalized precisely. The definition must be strong enough to imply local tomography but weak enough to follow from the self-modeling setup. The gap is non-trivial.
- Step 4: This is the central novel argument. The claim that faithful tracking forces local tomography needs careful proof. The argument must explicitly address entangled-sector states -- states of BM that are not determined by product measurements.
- Step 6: The qubit condition requires that the self-modeling framework admits a 2-dimensional subsystem. This is satisfied because Phase 4 worked with M\_2(C)^sa, but the general argument needs to show that any self-modeling system with dim >= 2 contains a qubit-like subsystem.
- Step 7: Exhibiting the involution requires identifying the embedding of V = A^sa in the C\*-algebra A. For M\_n(C)^sa, A = M\_n(C) and the involution is conjugate transpose. Must verify this is the ONLY possibility.

### Approach 2: Barnum-Graydon-Wilce Compositionality Route (ALTERNATIVE)

**What:** Instead of proving local tomography directly, use the BGW result that compositionality constraints alone (well-defined non-signaling composites exist) already exclude the Albert algebra and heavily constrain the EJA type.

**When to use:** If the dimension-counting argument for local tomography (Step 4 of Approach 1) cannot be completed -- i.e., if faithful tracking does not imply local tomography in full generality. BGW provides a weaker but still useful constraint.

**What it gives:** BGW (arXiv:1606.09331, Quantum 4, 359, 2020) shows:
- No non-signaling composite has M\_3(O)^sa (Albert algebra) as a direct summand.
- If one factor has an exceptional summand, no composite exists (unless the other factor is purely classical).
- Composites of simple non-exceptional EJAs are direct summands of the universal tensor product.

**What it does NOT give:** BGW alone does NOT select complex over real or quaternionic. For that, local tomography or an additional assumption is needed.

**Tradeoffs:** Weaker conclusion (excludes Albert but not R or H types) but requires weaker assumptions (just "composites exist" rather than "composites are locally tomographic"). If local tomography cannot be proved, this gives a partial result.

### Approach 3: Information-Theoretic Argument (BACKUP)

**What:** Argue that the self-model's information about BM consists ONLY of what it can learn by probing B and M separately, because the self-model interacts with B and M through local measurements. This is local tomography by construction.

**When to use:** If the dimension-counting argument is too technical or requires assumptions beyond faithful tracking.

**Tradeoffs:** More physically intuitive but less mathematically rigorous. Might be accused of assuming the conclusion. The critical distinction: "the self-model can ONLY probe B and M separately" is stronger than "the self-model CAN probe B and M separately." The stronger statement might be justified by the operational setup but needs careful argument.

### Anti-Patterns to Avoid

- **Assuming complex field without proof:** The whole point is to DERIVE that the algebra is over C, not assume it. Any step that uses complex linearity, complex inner products, or complex conjugation before Hanche-Olsen/Barnum-Wilce is circular.
  - _Example:_ Writing "the state space of n qubits has dimension 4^n - 1" assumes complex QM.

- **Conflating independent accessibility with local tomography:** These are logically distinct (Pitfall P4 from project-level research). Independent accessibility says you CAN measure B and M separately. Local tomography says product measurements SUFFICE. The gap is the entangled sector.
  - _Example:_ "Since B and M are independently accessible, states on BM are determined by product measurements" -- this skips the crucial step.

- **Hand-waving the Albert algebra exclusion:** The Albert algebra M\_3(O)^sa must be explicitly excluded. It is a valid EJA (27-dimensional) that satisfies S1-S7 but admits no locally tomographic composite. Simply saying "the exceptional case doesn't arise" is insufficient.
  - _Example:_ Invoking Hanche-Olsen without checking that the Albert algebra is excluded from the composite.

- **Importing C\*-structure to define the composite:** The composite B tensor M must be defined using OUS/GPT primitives, not assuming a Hilbert space tensor product.
  - _Example:_ Writing "rho\_BM in B(H\_B tensor H\_M)" assumes the conclusion.

## Existing Results to Leverage

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
| --- | --- | --- | --- |
| vdW Theorem 1 | Finite-dim SP space => EJA | arXiv:1803.11139, p.15 | Already invoked in Phase 4. CITE. |
| vdW Theorem 3 | SP space + locally tomo composite = C\*-algebra | arXiv:1803.11139, p.19 | INVOKE once local tomography is proved. |
| Hanche-Olsen | JB-algebra + tensor product = C\*-algebra | LNM 1132 (1985) | The Jordan-to-C\* promotion. CITE. |
| Barnum-Wilce | EJA + local tomo + qubit = complex QM | arXiv:1202.4513, Found. Phys. 44, 192-212 (2014) | INVOKE to select complex type. |
| BGW Albert exclusion | No non-signaling composite has Albert summand | arXiv:1606.09331, Quantum 4, 359 (2020) | CITE for Albert exclusion. |
| S1-S7 for self-modeling product | All seven axioms proved (Phase 4) | Phase 4 proofs (Plans 03, 04, 06) | CITE as established. Do not re-verify. |
| EJA = V\_3 for qubits | spin factor V\_3 = M\_2(C)^sa | Phase 4 Plan 04 | Provides the qubit for Barnum-Wilce. |
| Corrected product formula | a & b = sum lambda\_i C\_{p\_i}(b) + sum sqrt(lambda\_i lambda\_j) P\_{ij}(b) | Phase 4 Eq. 04-06.4 | Starting point for composite product construction. |
| S4 phi-independent | S4 holds for all mixing functions f with f(0,x)=0 | Phase 4 Plan 04 | Means composite S4 inherits freely. |
| Associativity => commutativity | For normal SEAs | Quantum 4, 378 (2020) | Sanity check: composite product must be non-associative. |
| dim(M\_n(C)^sa) = n^2 | Standard | Linear algebra | Local tomography dimension check. |
| dim(M\_n(R)^sa) = n(n+1)/2 | Standard | Linear algebra | Local tomography failure for real type. |
| dim(M\_n(H)^sa) = n(2n-1) | Standard | Linear algebra | Local tomography failure for quaternionic type. |
| dim(V\_n) = n + 1 | Standard | Jordan algebra classification | Spin factor dimensions. |

**Key insight:** The entire downstream machinery is published and peer-reviewed. The ONLY novel work in this phase is: (1) formalizing independent accessibility, (2) proving it implies local tomography, and (3) explicitly excluding each non-complex EJA type. Everything else is theorem invocation.

### Don't Re-Derive

- The Koecher-Vinberg theorem
- Van de Wetering's Theorems 1 and 3
- Hanche-Olsen's theorem
- The Barnum-Wilce result
- The BGW compositionality constraints
- Any of the S1-S7 axiom proofs from Phase 4
- The Jordan-von Neumann-Wigner classification

**These are CITED, not proved.**

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
| --- | --- | --- | --- |
| Non-signaling composites of EJAs | Structure theory for admissible composites | BGW (2020) | Non-signaling, well-defined marginals |
| Dimension formula: local tomography | dim(S(A tensor B)) = dim(S(A)) * dim(S(B)) iff K = C | Hardy (2001), Barnum-Wilce (2014) | For M\_n(K)^sa systems |
| Spin factor V\_3 = M\_2(C)^sa | Qubit exists in the framework | JVW classification | Always (V\_3 is the 3+1 = 4 dim spin factor) |
| Self-duality from S4 | S4 + homogeneity => self-dual cone | vdW Prop. 30 | Already established in Phase 4 |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| --- | --- | --- | --- | --- |
| Local tomography and Jordan structure | Barnum, Wilce | 2014 | THE theorem connecting local tomo + EJA + qubit to complex QM | Main theorem statement and conditions |
| Composites of EJAs | Barnum, Graydon, Wilce | 2020 | Albert exclusion, compositionality constraints | Theorem: no composite has Albert summand |
| Sequential product spaces are Jordan algebras | van de Wetering | 2019 | Theorem 3 (locally tomo composite -> C\*) | Precise conditions for Theorem 3 |
| Local tomography and complex numbers | Niestegge | 2020 | Spin factor subtleties in local tomography | Quantum logical definition vs standard |
| Self-duality from homogeneity | Barnum, Ududec, vdW | 2023 | Reduces geometric assumptions | May simplify composite construction |
| GPT introduction | Plavala | 2023 | GPT framework for composites | Formal definitions of composites, non-signaling |

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
| --- | --- | --- | --- |
| SymPy | >= 1.12 | Symbolic verification of composite product properties | Continues Phase 4 tooling |
| NumPy | >= 1.24 | Numerical dimension checks, concrete composite examples | Cross-checking symbolic results |

### Supporting Tools

| Tool | Purpose | When to Use |
| --- | --- | --- |
| Phase 4 sp\_verification.py | Existing test harness for sequential product | Extend to composite products |
| SageMath (optional) | Jordan algebra tensor product structure | If EJA classification of composites is needed |

### Computational Feasibility

| Computation | Estimated Cost | Bottleneck | Mitigation |
| --- | --- | --- | --- |
| Verify product SP satisfies S1-S7 on V\_3 tensor V\_3 | < 1 minute (4x4 tensor = 16x16 symbolic matrices, but most checks reduce to factor checks) | Symbolic simplification | Factor-by-factor verification |
| Dimension check for composite state space | Trivial (arithmetic) | None | Direct computation |
| Explicit involution exhibition on M\_2(C) | Trivial | None | Conjugate transpose |
| Verify exclusion of R, H, spin, Albert | Moderate (case analysis) | Conceptual, not computational | Follow Barnum-Wilce structure |

**Installation / Setup:**
```bash
# Same as Phase 4 -- no additional packages needed
pip install numpy scipy sympy
```

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| --- | --- | --- | --- |
| Dimension count for V\_3 tensor V\_3 | Local tomography for qubit-qubit composite | dim(V\_3) = 4; dim(V\_3 tensor V\_3) should = 16 | 4 * 4 = 16 (matches M\_2(C)^sa tensor M\_2(C)^sa = M\_4(C)^sa restricted) |
| Product SP satisfies S4 on composite | Composite inherits S4 from factors | (a tensor b) & (c tensor d) = 0 => (c tensor d) & (a tensor b) = 0 | Follows from factor S4 |
| Classical limit: composite of simplices | Simplex tensor simplex = simplex | Product of diagonal matrices | Pointwise multiplication on product space |
| EJA type after local tomography | Only complex type survives | Check dimension formula for R, C, H types | Only C gives dim(A tensor B) = dim(A) * dim(B) |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| --- | --- | --- | --- |
| Complex QM (n=2) | M\_2(C)^sa tensor M\_2(C)^sa | Local tomography holds; dim = 4 * 4 = 16 | Standard QM |
| Real QM (n=2) | M\_2(R)^sa tensor M\_2(R)^sa | Local tomography FAILS; dim(S) = 3, composite dim = 6 but dim(S) * dim(S) = 9 | Barnum-Wilce |
| Classical (simplex) | n-simplex tensor m-simplex | Local tomography holds (classical probability) | Standard |
| Albert algebra | M\_3(O)^sa | No composite exists at all | BGW (2020) |
| Spin factor V\_4 | V\_4 tensor V\_4 | No locally tomographic composite | Barnum-Wilce |

### Numerical Validation

| Test | Method | Tolerance | Reference Value |
| --- | --- | --- | --- |
| dim(M\_n(C)^sa tensor M\_m(C)^sa) = n^2 * m^2 | Direct computation | Exact | Matches n^2 * m^2 |
| dim(M\_n(R)^sa tensor M\_m(R)^sa) != (n(n+1)/2) * (m(m+1)/2) | Direct computation | Exact | Mismatch confirms local tomo fails for R |
| Composite product on V\_3 tensor V\_3 | SymPy verification | Exact | Must satisfy S1-S7 |
| Involution on M\_2(C) | Exhibit (a+ib)\* = a-ib | Exact | (A^sa)\* = A^sa, i\* = -i |

### Red Flags During Computation

- If the composite state space dimension exceeds dim(S\_B) * dim(S\_M), local tomography fails -- check whether the self-modeling constraint was correctly formalized.
- If the product-form sequential product on the composite fails S4, re-examine whether S4 truly inherits from factors (it should by the product structure).
- If the dimension argument works for quaternionic type as well as complex, something is wrong -- quaternionic QM violates local tomography. Check whether dim(M\_n(H)^sa) was computed correctly (should be n(2n-1), not n^2).
- If the involution is not unique, there may be a superselection sector issue.

## Common Pitfalls

### Pitfall 1: Conflating Independent Accessibility with Local Tomography (P4)

**What goes wrong:** Claiming "since B and M are independently accessible, product measurements determine the joint state" without addressing the entangled sector.

**Why it happens:** In complex QM, these coincide. But in real or quaternionic QM, independent accessibility holds but local tomography fails. The entangled sector contains states invisible to product measurements.

**How to avoid:** The argument must explicitly identify what property of the self-modeling construction closes the gap. The candidate: faithful tracking (phi is an isomorphism) forces the B-M state to span the product state space, eliminating any hidden entangled sector.

**Warning signs:** The local tomography proof is very short (< 1 page). It should involve careful treatment of the entangled sector.

**Recovery:** If local tomography cannot be proved, fall back to the BGW compositionality route (Approach 2), which gives a weaker but still useful result (excludes Albert but not R/H types).

### Pitfall 2: Albert Algebra Obstruction (P5)

**What goes wrong:** Invoking Hanche-Olsen without first excluding the Albert algebra M\_3(O)^sa from the classification.

**Why it happens:** The Albert algebra is a valid EJA satisfying S1-S7 but admitting NO well-behaved tensor product. It is an isolated exceptional point in the JVW classification.

**How to avoid:** Two routes:
1. BGW (2020) shows compositionality itself excludes Albert -- the B-M composite CANNOT have an Albert summand.
2. The Albert algebra is 27-dimensional. If the self-modeling system has dimension < 27, it cannot be Albert. For qubits (dim = 4 = V\_3), this is automatic.

**Warning signs:** No explicit argument about why the Albert algebra does not arise.

**Recovery:** Low cost -- the BGW result gives the exclusion for free once compositionality is established.

### Pitfall 3: Assuming Complex Linearity Before Proving It

**What goes wrong:** Using complex structure (complex inner products, complex eigenvalues, complex conjugation) before Hanche-Olsen/Barnum-Wilce has selected the complex type.

**Why it happens:** Natural for physicists trained in complex QM. The entire Phase 5 argument works in the REAL vector space framework of order unit spaces and EJAs. Complex structure EMERGES as the conclusion.

**How to avoid:** All intermediate steps must use real vector space operations only. The EJA V is a real vector space. The Jordan product is a real bilinear operation. The involution maps V to itself (it is a real-linear map).

**Warning signs:** Appearance of "i" or "complex conjugate" before the final identification step.

**Recovery:** Rewrite offending steps in real terms. Usually straightforward.

### Pitfall 4: Norm Completion Trap (P7)

**What goes wrong:** Claiming the C\*-norm is "free" in finite dimensions before establishing the C\*-identity ||a\*a|| = ||a||^2.

**Why it happens:** In finite dimensions, all norms are equivalent. But the C\*-identity is a SPECIFIC relationship between norm and involution, not just "any norm works."

**How to avoid:** The C\*-norm on A = M\_n(C) is the operator norm ||a|| = max eigenvalue of (a\*a)^{1/2}. This is determined by the involution. Once the involution is exhibited, the C\*-norm follows. Track the dependency explicitly.

**Warning signs:** Invoking the C\*-identity before exhibiting the involution.

**Recovery:** Reorder the argument: involution first, then norm.

### Pitfall 5: Circularity -- Importing C\*-Structure to Define the Composite

**What goes wrong:** Defining B tensor M using the Hilbert space tensor product (H\_B tensor H\_M), which presupposes complex QM.

**Why it happens:** The Hilbert space tensor product is the most familiar composite construction. But it assumes complex structure, which is what Phase 5 derives.

**How to avoid:** Define the composite in the GPT framework: the state space S(BM) is a compact convex set containing all product states rho\_B tensor rho\_M, satisfying the non-signaling constraint, and (for local tomography) having dimension dim(S\_B) * dim(S\_M).

**Warning signs:** Any mention of "Hilbert space" in the composite construction.

**Recovery:** Rewrite using GPT primitives. This may require more careful formalization but avoids circularity.

## Level of Rigor

**Required for this phase:** Physicist's proof with careful attention to logical dependencies and explicit case analysis for EJA type exclusion.

**Justification:** The key theorems (vdW Theorem 3, Hanche-Olsen, Barnum-Wilce) are published and peer-reviewed. The novel argument (independent accessibility -> local tomography) needs to be careful but not formally axiomatic. The case analysis (excluding R, H, spin, Albert) should be explicit but can reference published dimension formulas.

**What this means concretely:**
- The formalization of "independent accessibility" must have a precise mathematical definition, not just a verbal description.
- The proof that independent accessibility implies local tomography must explicitly address the entangled sector.
- Each non-complex EJA type must be individually excluded with a specific argument (dimension mismatch or compositionality obstruction).
- Theorem invocations must cite the exact theorem, verify all hypotheses, and state the conclusion.
- The involution must be exhibited as a specific operation, not just claimed to exist.

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| --- | --- | --- | --- |
| Assume local tomography axiomatically | Derive from compositionality constraints | Barnum-Wilce (2014), BGW (2020) | Local tomography is now a CONSEQUENCE of compositionality + Jordan structure, not an independent axiom |
| Hanche-Olsen (JB -> JC) only | vdW Theorem 3 (SP + composite -> C\*) | van de Wetering (2019) | More direct route from sequential products to C\* |
| Albert exclusion ad hoc | BGW systematic exclusion | 2020 | Compositionality alone kills exceptional type |
| Assume qubit exists | Derive qubit from Phase 4 (V\_3 for minimal self-model) | This project | Qubit assumption is NOT independent -- it follows from the self-modeling framework |

**Superseded approaches to avoid:**
- Assuming local tomography as an axiom without justification (pre-2014 approach). Must derive it or state it as an explicit assumption.
- Using only Hanche-Olsen without Barnum-Wilce (misses the R/H type exclusion).

## Open Questions

1. **Does independent accessibility imply local tomography for self-modeling systems?**
   - What we know: Independent accessibility is weaker than local tomography in general. For complex QM, they coincide. For real/quaternionic QM, independent accessibility holds but local tomography fails. The self-modeling constraint (faithful tracking) provides additional structure that may close the gap.
   - What's unclear: Whether faithful tracking alone is sufficient, or whether an additional property of the self-model is needed (e.g., the model being "complete" or "sufficient" in some information-theoretic sense).
   - Impact on this phase: This is THE central question. If yes, Phase 5 succeeds. If no, the additional assumption must be identified and stated.
   - Recommendation: Attempt the dimension-counting argument first (Approach 1, Step 4). If it fails, identify the minimal additional assumption.

2. **Does the self-modeling framework admit arbitrary-dimensional subsystems?**
   - What we know: Phase 4 established V\_3 = M\_2(C)^sa for the qubit case. Barnum-Wilce requires at least one qubit.
   - What's unclear: Whether the self-modeling construction naturally produces systems of all dimensions, or only specific dimensions.
   - Impact on this phase: The qubit condition is already satisfied for the qubit model (Phase 4). For the general result, need to show that a qubit-like subsystem always exists.
   - Recommendation: Use Phase 4's V\_3 result to satisfy the qubit condition. For generality, argue that any self-modeling system with dim >= 2 contains a 2-dimensional face, which is a qubit subsystem.

3. **How does the involution act on the sequential product?**
   - What we know: Once V is identified as M\_n(C)^sa, the C\*-algebra is M\_n(C), and the involution is conjugate transpose.
   - What's unclear: How the involution relates to the self-modeling sequential product operationally. The involution (a+ib)\* = a-ib has no obvious interpretation in terms of "test-update-test."
   - Impact on this phase: The involution must be EXHIBITED as an operation, not just claimed to exist. Its operational meaning is important for the paper but not for the proof.
   - Recommendation: Exhibit the involution algebraically, defer operational interpretation to paper writing (Phase 6).

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| --- | --- | --- | --- |
| Dimension-counting argument for local tomography | Faithful tracking insufficient to close entangled-sector gap | Information-theoretic argument (Approach 3) | LOW -- different framing of same argument |
| Information-theoretic argument | Too hand-wavy for rigorous proof | BGW compositionality route (Approach 2) | MEDIUM -- weaker conclusion (no R/H exclusion) |
| BGW route | Cannot form the composite at all | Identify minimal additional assumption for local tomography; state as conditional result | MEDIUM -- publishable as "L4 + local tomography => C\*" |
| All approaches | Local tomography genuinely does not follow from self-modeling | Conditional paper: "Self-modeling + S1-S7 give EJA. If additionally locally tomographic, then C\*-algebra." | LOW -- still novel (S1-S7 verification is the main result) |

**Decision criteria:** If after 3 different argument strategies the gap between independent accessibility and local tomography remains unbridged, pivot to the conditional result. This is still publishable and novel -- the Phase 4 results (S1-S7 from self-modeling) are the main contribution.

## Dimension Counting Reference Table

The following table is essential for the type-exclusion arguments. It shows why only complex QM admits local tomography.

For two copies of an n-dimensional simple EJA of type K:

| Type K | dim(M\_n(K)^sa) | dim(A) * dim(A) | dim(S(A tensor A)\_min) | Local Tomo? |
| --- | --- | --- | --- | --- |
| R (real) | n(n+1)/2 | [n(n+1)/2]^2 | > [n(n+1)/2]^2 for n >= 2 | NO |
| C (complex) | n^2 | n^4 | n^4 | YES |
| H (quaternionic) | n(2n-1) | [n(2n-1)]^2 | < [n(2n-1)]^2 for n >= 2 | NO |
| Spin V\_n (n>=4) | n+1 | (n+1)^2 | > (n+1)^2 | NO |
| Albert M\_3(O)^sa | 27 | 729 | NO COMPOSITE EXISTS | NO |

**For n=2 specifically:**

| Type | dim | dim^2 | Local tomo composite? |
| --- | --- | --- | --- |
| M\_2(R)^sa | 3 | 9 | NO (composite state space has dim > 9) |
| M\_2(C)^sa = V\_3 | 4 | 16 | YES (composite state space has dim = 16) |
| M\_2(H)^sa = V\_5 | 6 | 36 | NO (composite state space has dim != 36) |
| V\_4 | 5 | 25 | NO (no locally tomo composite for V\_n, n>=4) |

**Why the asymmetry between R and H:** For real QM, the composite state space is TOO BIG (extra entangled states invisible to product measurements). For quaternionic QM, the composite state space is TOO SMALL (fewer separable states than expected). Only complex QM has the Goldilocks dimension.

## Sources

### Primary (HIGH confidence)

- van de Wetering, "Sequential product spaces are Jordan algebras," J. Math. Phys. 60, 062201 (2019), [arXiv:1803.11139](https://arxiv.org/abs/1803.11139) -- Theorem 1 (S1-S7 => EJA), Theorem 3 (SP + locally tomo composite => C\*)
- Barnum and Wilce, "Local tomography and the Jordan structure of quantum theory," Found. Phys. 44, 192-212 (2014), [arXiv:1202.4513](https://arxiv.org/abs/1202.4513) -- EJA + local tomo + qubit = complex QM
- Barnum, Graydon, and Wilce, "Composites and categories of Euclidean Jordan algebras," Quantum 4, 359 (2020), [arXiv:1606.09331](https://arxiv.org/abs/1606.09331) -- Compositionality constraints, Albert exclusion
- Hanche-Olsen, "JB-algebras with tensor products are C\*-algebras," LNM 1132, Springer (1985), [SpringerLink](https://link.springer.com/content/pdf/10.1007/BFb0074886) -- THE Jordan-to-C\* promotion theorem
- Hanche-Olsen and Stormer, "Jordan Operator Algebras," Pitman (1984) -- Standard reference on JB-algebras

### Secondary (MEDIUM confidence)

- Niestegge, "Local tomography and the role of the complex numbers in quantum mechanics," (2020), [arXiv:2001.11421](https://arxiv.org/abs/2001.11421) -- Quantum logical definition of local tomography, spin factor subtleties
- Barnum, Ududec, and van de Wetering, "Self-duality from homogeneity and pure transitivity," Compositionality 5 (2023), [arXiv:2306.00362](https://arxiv.org/abs/2306.00362) -- Reduces geometric assumptions
- Plavala, "General probabilistic theories: An introduction," Physics Reports 1033, 1-64 (2023), [arXiv:2103.07469](https://arxiv.org/abs/2103.07469) -- GPT framework for composites and local tomography
- Hardy, "Quantum theory from five reasonable axioms," [arXiv:quant-ph/0101012](https://arxiv.org/abs/quant-ph/0101012) (2001) -- Original local tomography dimension counting

### Tertiary (LOW confidence)

- Phase 4 results (S1-S7 proofs, EJA classification) -- project-internal artifacts, fully verified but not yet peer-reviewed

## Metadata

**Confidence breakdown:**

- Mathematical framework: HIGH -- the theorems (vdW Thm 3, Hanche-Olsen, Barnum-Wilce) are published and well-established
- Standard approaches: MEDIUM -- the approach is clear but the novel step (independent accessibility -> local tomography) has no literature precedent
- Computational tools: HIGH -- lightweight proof-support computation; same tools as Phase 4
- Validation strategies: HIGH -- known dimension formulas and limiting cases provide clear benchmarks

**Research date:** 2026-03-21
**Valid until:** Indefinitely for the mathematical results. The novel step (independent accessibility -> local tomography) is where the research risk lies.

## Caveats and Alternatives

### Self-Critique

1. **What assumption am I making that might be wrong?** That faithful tracking (phi is an isomorphism) is sufficient to force local tomography. This is plausible but unproven. The gap between "independent accessibility" and "local tomography" might require additional structure beyond faithfulness -- e.g., that the self-model can prepare arbitrary product states, not just measure them.

2. **What alternative approach did I dismiss too quickly?** The categorical (dagger-monoidal) approach via Barnum-Wilce's second characterization (Theorem 2 in arXiv:1202.4513). This characterizes finite-dim QM among dagger-monoidal categories, which might provide a more natural framework for the self-modeling composite. Dismissed because it requires establishing dagger-monoidal structure, which is itself non-trivial. But if the GPT route stalls, this is worth revisiting.

3. **What limitation of my recommended method am I understating?** The dimension-counting argument (Approach 1, Step 4) relies on "the B-M state has full rank on the product state space." This is a strong claim about the B-M correlation state. For a faithful self-model, the state should indeed have full rank on product effects, but proving this rigorously requires a careful analysis of what "faithful tracking" means for joint states (not just marginals).

4. **Is there a simpler method I overlooked?** Possibly: if one could show that the self-modeling sequential product is UNIQUELY the Luders product (using vdW's three characterizations from arXiv:1803.08453), then one immediately gets M\_n(C)^sa with no need for separate local tomography argument. Phase 4 showed the product coincides with Luders on M\_2(C)^sa, but this was a CHECK, not a DERIVATION of complex structure. Still, this shortcut is worth investigating.

5. **Would a specialist disagree with my recommendation?** A GPT specialist might argue that "independent accessibility" should be formalized as a CATEGORY-THEORETIC property (existence of a monoidal product) rather than a set-theoretic one (dimension of state space). The categorical approach is more natural in the GPT community. However, for this project, the dimension-counting approach is more concrete and easier to connect to the self-modeling framework.

---

_Phase research for: Local Tomography from B-M Compositionality_
_Researched: 2026-03-21_
