# Prior Work: Sequential Products, Jordan Algebras, and QM Reconstruction

**Surveyed:** 2026-03-20
**Domain:** Quantum foundations / Algebraic quantum theory / QM reconstruction
**Confidence:** MEDIUM-HIGH

This document covers prior work relevant to deriving the C\*-algebra involution from sequential product structure of self-modeling systems. It does NOT re-cover the v1.0 experiential measure framework or the algebraic genericity chain from Step 3 onward (NC generic -> matrix algebras -> unitary -> QM), which are validated and complete.

---

## Key Results

| Result | Expression / Value | Conditions | Source | Year | Confidence |
|--------|-------------------|------------|--------|------|------------|
| Sequential product spaces are Euclidean Jordan algebras | Koecher-Vinberg identification via homogeneous self-dual cone | Finite-dim order unit space + continuous seq. product (axioms S1-S7) | van de Wetering, arXiv:1803.11139 | 2018 | HIGH |
| Jordan + local tomography => C\*-algebra | Hanche-Olsen embedding | Simple Jordan factor + locally tomographic composite + qubit exists | van de Wetering Thm 3 (1803.11139); Barnum-Wilce (1202.4513) | 2018/2014 | HIGH |
| Three types of normal SEAs | E = E_b + E_c + E_ac (Boolean, convex, almost-convex) | Normal sequential effect algebra | Westerbaan-Westerbaan-van de Wetering, arXiv:2004.12749 | 2020 | HIGH |
| Self-duality from homogeneity + pure transitivity | Self-duality is not independent; it follows | Finite-dim, homogeneous cone, pure transitivity of normalized states | Barnum et al., arXiv:2306.00362 | 2023 | MEDIUM |
| Composites of EJAs exclude exceptional Jordan algebras | No composite has Albert algebra summand | Non-signaling composites of EJAs | Barnum-Graydon-Wilce, arXiv:1606.09331 | 2016/2020 | HIGH |
| Gudder-Greechie sequential product on B(H) | a . b = sqrt(a) b sqrt(a) | Effects on Hilbert space | Gudder-Greechie, Rep. Math. Phys. 49 (2002) 87-111 | 2002 | HIGH |
| Three characterisations of standard sequential product | Unital order isomorphism invariance, inner product symmetry, invertibility preservation | Each individually characterizes standard seq. product on von Neumann algebra or EJA | van de Wetering, arXiv:1803.08453 | 2018 | HIGH |
| Operational derivation of involution (D'Ariano) | Complex conjugation from faithful states | Finite-dim + faithful state + composition-preserving extension | D'Ariano, arXiv:quant-ph/0611094 | 2006 | MEDIUM |
| JVW classification of simple EJAs | 5 types: M_n(R)_sa, M_n(C)_sa, M_n(H)_sa, V_n (spin), M_3(O)_sa | Finite-dimensional, formally real | Jordan-von Neumann-Wigner, Ann. Math. 35 (1934) | 1934 | HIGH |

---

## Foundational Work

### Gudder-Greechie (2002) - Sequential Products on Effect Algebras

**Key contribution:** Defined the abstract sequential product on effect algebras. An effect algebra E with a binary operation . : E x E -> E is a sequential effect algebra (SEA) if the operation satisfies axioms encoding "measure a, then measure b." The standard model is a . b = sqrt(a) b sqrt(a) on the unit interval [0,I] of B(H).

**Original Gudder-Greechie axioms (for SEAs):**
- (S1) The map b -> a . b is additive: a . (b + c) = a . b + a . c when b + c is defined
- (S2) 1 . a = a
- (S3) If a . b = 0 then a . b = b . a (= 0)
- (S4) If a . b = b . a then a . b' = b' . a and a . (b . c) = (a . b) . c (where b' = 1 - b)
- (S5) If c . a = a . c and c . b = b . c then c . (a . b) = (a . b) . c and c . (a + b) = (a + b) . c (when a + b defined)

**Limitations:** These axioms are NOT sufficient to characterize the standard sequential product sqrt(a) b sqrt(a) on B(H). Multiple inequivalent sequential products exist satisfying these axioms. The axioms do not force Jordan algebra structure by themselves.

**Relevance:** This is the algebraic abstraction of "test a then test b." The self-modeling sequential product must satisfy at minimum these axioms for the approach to work.

### Van de Wetering (2018) - Sequential Product Spaces are Jordan Algebras [arXiv:1803.11139]

**Key contribution:** Proved that finite-dimensional order unit spaces with a continuous sequential product satisfying strengthened axioms are Euclidean Jordan algebras. This is THE key theorem for the v2.0 project.

**Van de Wetering's axioms for sequential product spaces (on an order unit space V with unit 1, effects [0,1]_V):**

A sequential product is a map . : [0,1]_V x V -> V satisfying:

- (S1) Bilinearity/additivity in the second argument: a . (lambda b + mu c) = lambda (a . b) + mu (a . c)
- (S2) Continuous in first argument (in the order-unit norm topology)
- (S3) 1 . b = b for all b (identity is trivial test)
- (S4) **Symmetry of orthogonality:** if a . b = 0 then b . a = 0
- (S5) If a . b = b . a then a . (b . c) = (a . b) . c (compatible effects associate)
- (S6) If a . b = b . a and a . c = c . a then a . (b + c) = (b + c) . a when b + c <= 1 (sums of compatible effects stay compatible)
- (S7) a . 1 = a for all a (measuring the trivial effect preserves the first measurement)

**CRITICAL DISTINCTION:** Van de Wetering works on order unit spaces (vector spaces with an Archimedean order unit), not bare effect algebras. This gives access to convexity and norm structure that Gudder-Greechie lacked. The key strengthening over Gudder-Greechie is:

- S1 is strengthened to linearity in the second argument (not just additivity)
- S4 (symmetry of orthogonality) replaces the Gudder-Greechie S3 (which only says a.b = 0 => a.b = b.a = 0, tautologically). Van de Wetering's S4 says: a.b = 0 => b.a = 0, which is a genuine constraint
- S7 (a . 1 = a) is added, not present in Gudder-Greechie

**Main theorem (Theorem 1):** A finite-dimensional order unit space with a sequential product satisfying S1-S7 is a Euclidean Jordan algebra (with Jordan product a o b = (1/2)(a . b + b . a)).

**Proof strategy:** Show the state space is homogeneous and self-dual, then invoke Koecher-Vinberg.

**Theorem 3:** If a sequential product space has a locally tomographic composite (i.e., the vector space tensor product is again a sequential product space satisfying S1-S7), then it is a C\*-algebra.

**Limitations:** Does not address which physical systems actually satisfy S1-S7. The axioms are shown sufficient; identifying concrete constructions that satisfy them (beyond the known B(H) case) is an open problem.

**Relevance:** This is the bridge from "sequential products" to "Jordan algebras." If the self-modeling construction satisfies S1-S7, we get the Jordan algebra for free, and then Theorem 3 plus local tomography gives the C\*-algebra.

### Van de Wetering (2018) - Three Characterisations of the Sequential Product [arXiv:1803.08453]

**Key contribution:** Showed that the Gudder-Greechie axioms are insufficient to pin down a . b = sqrt(a) b sqrt(a). Identified three independent properties, each of which (combined with the basic axioms) uniquely characterizes the standard sequential product:

1. **Invariance under unital order isomorphisms:** If phi is a unital order isomorphism, then phi(a . b) = phi(a) . phi(b)
2. **Symmetry w.r.t. a specific inner product:** The sequential product is symmetric with respect to the trace inner product <a,b> = tr(ab)
3. **Preservation of invertibility:** If b is an invertible effect (0 < b < 1 with b invertible), then a . b is invertible when a is invertible

**Relevance:** For the self-modeling construction, we need to check which of these additional properties holds. Property (2) -- inner product symmetry -- is the most physically transparent (it says "the probability of 'a then b' equals 'b then a' when one accounts for the effect of measurement on the state").

### Westerbaan-Westerbaan-van de Wetering (2020) - Three Types of Normal SEAs [arXiv:2004.12749]

**Key contribution:** Classified normal sequential effect algebras into three types via a direct sum decomposition: E = E_b (Boolean/classical) + E_c (convex/quantum) + E_ac (almost-convex/pathological). Proved a spectral theorem for normal SEAs. Showed that associativity forces normal SEAs satisfying their axioms to be commutative -- explaining why the quantum sequential product MUST be non-associative.

**Key finding for this project:** The almost-convex type E_ac is pathological and can be excluded by a simple additional axiom. Once excluded, the convex part E_c corresponds to the quantum/Jordan algebraic case. This classification confirms that the sequential product framework naturally splits into classical (Boolean) and quantum (Jordan) sectors.

**Relevance:** Provides theoretical support that the sequential product framework, with reasonable axioms, leads to exactly the classical+quantum dichotomy. No exotic third possibility survives reasonable assumptions.

### Barnum-Wilce (2014) - Local Tomography and the Jordan Structure of QT [arXiv:1202.4513]

**Key contribution:** Using Hanche-Olsen's result (1985), showed that among non-signaling probabilistic theories where individual systems are Euclidean Jordan algebras:
- Local tomography on composites
- Existence of at least one qubit-like system

together force the theory to be standard complex quantum mechanics (with possible superselection rules).

**The Hanche-Olsen result (1985):** A JB-algebra that admits a tensor product (in the sense of a JB-algebra composite satisfying local tomography) must be a JC-algebra (i.e., embeds into the self-adjoint part of a C\*-algebra). Concretely: among the five JVW types, only M_n(C)_sa survives the tensor product requirement. The spin factors V_n (for n >= 3), real quantum mechanics M_n(R)_sa, quaternionic quantum mechanics M_n(H)_sa, and the exceptional Albert algebra M_3(O)_sa are all ruled out.

**Why this matters:** This is the mechanism by which local tomography promotes Jordan -> C\*. The involution (*-operation) emerges because C\*-algebras have one but general Jordan algebras do not. The self-adjoint part of a C\*-algebra has an involution inherited from the ambient C\*-algebra; bare Jordan algebras lack this structure.

**Limitations:** Requires the existence of at least one qubit (2-dimensional system). This is natural for physical theories but must be justified in the self-modeling context.

### Barnum-Graydon-Wilce (2016/2020) - Composites and Categories of EJAs [arXiv:1606.09331]

**Key contribution:** Studied non-signaling composites of probabilistic models based on Euclidean Jordan algebras. Proved two critical no-go results:

1. No non-signaling composite can have the exceptional Jordan algebra M_3(O) as a direct summand
2. If one factor has an exceptional summand, no composite exists at all (unless the other factor is purely classical)

Moreover, composites of simple non-exceptional EJAs are direct summands of their universal tensor product.

**Relevance:** Independently confirms that compositionality (having well-defined composites) kills the exceptional and non-complex Jordan algebra types. This is the compositionality-based route to killing the same alternatives that local tomography kills.

### Barnum-Ududec-van de Wetering (2023) [arXiv:2306.00362]

**Key contribution:** Proved that self-duality of the state space cone follows from homogeneity and pure transitivity alone. Previously, homogeneity and self-duality were independent assumptions in the Koecher-Vinberg theorem. This result reduces the number of independent geometric assumptions needed.

**Significance for this project:** If the self-modeling state space is homogeneous (symmetry group acts transitively on the interior of the cone) and pure transitive (symmetry group acts transitively on pure states), then self-duality is automatic. This potentially simplifies verifying the conditions for the Koecher-Vinberg theorem.

**Status:** arXiv preprint (2023). Not yet published in a journal as of the survey date.

**Confidence:** MEDIUM -- single preprint, not yet peer-reviewed, but by established researchers in the field.

### D'Ariano (2006) - Operational Axioms for Quantum Mechanics [arXiv:quant-ph/0611094]

**Key contribution:** Derived the mathematical formulation of QM in terms of finite-dimensional Hilbert spaces from five operational postulates about "experimental accessibility and simplicity." The key novel element is the operational derivation of an involution (complex conjugation for effects) from the existence of a "faithful state" -- a state that is not annihilated by any non-zero effect.

**The involution construction:** Given a faithful state omega, one defines a bilinear form <a,b>_omega = omega(a . b) (where . is the sequential product / composition of effects). If this form is symmetric and non-degenerate (both guaranteed by the faithful state postulate), it induces a transpose/adjoint operation. The involution then comes from extending this transpose to transformations and showing the extension is composition-preserving.

**Critical assumption:** The involution construction requires a "faithful state" and that the extension of the transpose to transformations preserves composition. This composition-preservation is the non-trivial step -- it is postulated (D'Ariano's Postulate 5), not derived.

**Relevance to v2.0:** If the self-model's correlation state between body B and model M can be shown to be faithful, this provides an alternative route to the involution. However, this would require an additional postulate (composition-preservation of the extension) unless it can be derived from the self-modeling structure.

### D'Ariano (2007) - Operational Axioms for C\*-algebraic QM [arXiv:quant-ph/0701219]

**Key contribution:** Extended the 2006 work to the infinite-dimensional case, deriving a C\*-algebra representation via GNS construction from four of the five postulates.

**Relevance:** Confirms that the faithful-state route to involution generalizes beyond finite dimensions, which matters for eventual infinite-dimensional extensions.

---

## QM Reconstruction Programs: Comparison for This Project

| Program | Premises | Gets Involution? | How? | Key Limitation |
|---------|----------|-----------------|------|----------------|
| **Hardy (2001)** | 5 reasonable axioms | Indirectly (via Hilbert space) | Dimensional counting + continuity + compositionality | Assumes classical probability framework |
| **Chiribella-D'Ariano-Perinotti (2011)** | 5 informational axioms + purification | Yes (via purification) | Purification postulate forces C\*-structure | Purification is a strong assumption |
| **Masanes-Mueller (2011)** | 5 physical requirements | Yes (via local tomography) | Existence of information unit + continuous reversibility | Local tomography assumed, not derived |
| **D'Ariano (2006)** | 5 operational postulates | Yes (explicitly constructed) | Faithful state + composition-preserving extension | Extension preservation is postulated |
| **Van de Wetering (2018/2019)** | Sequential product S1-S7 + local tomography | Yes (via Jordan -> C\*) | Hanche-Olsen theorem | S1-S7 and local tomography assumed |
| **This project (v2.0)** | L4 (self-modeling) | **Goal: Yes** | Self-modeling -> sequential product -> Jordan -> local tomography -> C\* | Must verify S1-S7 and local tomography |

**Critical observation:** Every existing reconstruction program assumes something equivalent to the involution, either as an explicit axiom (D'Ariano's composition-preserving extension), or implicitly via postulates that force complex structure (purification, local tomography, continuous reversibility). NO existing program derives the involution purely from operational measurement structure without an additional postulate. The v2.0 project would be the first to do so IF the self-modeling construction satisfies S1-S7 and local tomography follows from B-M compositionality.

---

## Recent Developments

| Paper | Authors | Year | Advance | Impact on Our Work |
|-------|---------|------|---------|--------------------|
| Self-duality from homogeneity + pure transitivity | Barnum, Ududec, van de Wetering | 2023 | Reduces independent geometric assumptions for Koecher-Vinberg | May simplify verification of Jordan algebra conditions |
| Three types of normal SEAs | Westerbaan, Westerbaan, van de Wetering | 2020 | Classifies SEAs into Boolean + convex + almost-convex | Confirms no exotic alternatives; quantum = convex type |
| Effect-theoretic reconstruction | van de Wetering | 2019 | Derives QM from effectus theory axioms without GPT framework | Alternative reconstruction route; does not address involution gap |
| Composites and Categories of EJAs | Barnum, Graydon, Wilce | 2020 | Compositionality kills exceptional + non-complex EJAs | Confirms compositionality-based route to C\* is solid |
| Completing QRP via relativity | Stuckey et al. | 2024 | Links QM reconstruction to relativity principle | Tangential; different philosophical framework |

---

## Known Limiting Cases

| Limit | Known Result | Source | Verified By |
|-------|-------------|--------|-------------|
| Commutative sequential product | Boolean algebra (classical theory) | Westerbaan-Westerbaan-van de Wetering (2020) | Theorem in 2004.12749 |
| 2-dimensional system (qubit) | M_2(C)_sa (spin factor V_3 = M_2(C)_sa) | JVW classification + Barnum-Wilce (2014) | Multiple sources |
| Associative sequential product | Commutative (= classical) | Westerbaan-Westerbaan-van de Wetering (2020) | Theorem in 2004.12749 |
| No composite structure | Any simple EJA allowed (including exceptional) | Barnum-Graydon-Wilce (2016) | Theorem in 1606.09331 |
| With locally tomographic composite | C\*-algebra only | van de Wetering Thm 3 (2018); Hanche-Olsen (1985) | Barnum-Wilce (2014) |

---

## Open Questions

1. **S4 verification for non-B(H) constructions** -- No one has verified S4 (symmetry of orthogonality) for a sequential product arising from a physical construction other than the standard sqrt(a) b sqrt(a) on B(H). This is exactly the gap the v2.0 project must bridge for the self-modeling construction. S4 is the hardest axiom because it requires showing that "a then b = 0" implies "b then a = 0", which is a non-trivial symmetry condition that may or may not hold when the sequential product encodes model-updating.

2. **Local tomography from compositionality** -- Whether B-M (body-model) independent accessibility implies local tomography is an open question. Barnum-Wilce (2014) showed local tomography forces C\* among Jordan algebraic theories, but they assumed local tomography rather than deriving it from compositional structure. The v2.0 project needs: "independently accessible subsystems => states determined by product measurements." This is plausible but unproven in the self-modeling context.

3. **Whether faithful states exist in the self-modeling construction** -- D'Ariano's backup route requires a faithful state (one not annihilated by any non-zero effect). Whether the B-M correlation state in a self-model is faithful depends on the specifics of the self-modeling dynamics. This is Phase 4 territory if the sequential product route fails.

4. **Extension to infinite dimensions** -- Van de Wetering's Theorem 1 is stated for finite dimensions. The infinite-dimensional generalization (getting JB-algebras) requires additional technical conditions. The v2.0 project works in finite dimensions, so this is not an immediate concern, but eventual physical applications require it.

---

## Notation Conventions in the Literature

| Quantity | Standard Symbol(s) | Variations | Our Choice | Reason |
|----------|-------------------|------------|------------|--------|
| Sequential product | a . b, a o_s b | a ; b (Gudder), (a,b) -> a.b | a . b | Matches van de Wetering (2018) |
| Jordan product | a o b | a * b, {a,b}/2 | a o b = (1/2)(a . b + b . a) | Standard in Jordan algebra literature |
| Effect space | [0,1]_V, E(A) | E, [0,u] | [0,1]_V | Matches van de Wetering's order unit space notation |
| Order unit | 1, u, e | I, 1_A | 1 | Standard |
| State space | Omega(V), S(A), K | S, Omega | Omega(V) | Matches van de Wetering |
| Orthogonality | a perp b | a _|_ b | a . b = 0 | Defined via sequential product |
| Involution | a -> a* | a -> a^dag, a -> bar(a) | a -> a* | Standard C\*-algebra notation |

---

## The Logical Chain and Where Prior Work Fits

```
L4 (self-models test and update)
    |
    v
Self-modeling sequential product on effects of B
    |--- Must satisfy S1-S7 (van de Wetering 2018)
    |--- S1-S3, S5-S7 expected to be straightforward
    |--- S4 (symmetry of orthogonality) is THE critical test
    |
    v  [van de Wetering Theorem 1]
Euclidean Jordan Algebra
    |
    v  B-M compositionality
Local tomography on B tensor M
    |--- Must show independent accessibility => state determination
    |--- Barnum-Wilce (2014) + Hanche-Olsen (1985) then apply
    |
    v  [van de Wetering Theorem 3 / Hanche-Olsen]
C*-algebra (with involution DERIVED, not assumed)
    |
    v  [Validated chain from v1.0]
NC generic -> matrix algebras -> unitary -> QM
```

**What prior work gives us for free:** The bottom half of this chain (Jordan -> C\* via local tomography, and C\* -> QM via genericity) is entirely established mathematics. The project's contribution is the TOP of the chain: showing that self-modeling produces a sequential product satisfying the right axioms.

**What prior work does NOT give us:** No one has verified S1-S7 for ANY construction other than the standard B(H) model. The self-modeling sequential product would be the first non-trivial verification. This is simultaneously the novelty and the risk.

---

## Alternatives Considered

| Category | Recommended | Alternative | Why Not |
|----------|------------|------------|---------|
| Route to Jordan algebra | Sequential product (van de Wetering) | Homogeneity + self-duality (Koecher-Vinberg directly) | Sequential product is operationally motivated by self-modeling; Koecher-Vinberg requires proving geometric properties that are harder to connect to L4 |
| Route to involution | Local tomography (Hanche-Olsen) | Faithful state (D'Ariano) | Local tomography is derivable from B-M compositionality (conjectured); faithful state requires additional postulate (composition-preserving extension) |
| Sequential product axiom set | Van de Wetering S1-S7 | Gudder-Greechie original axioms | Gudder-Greechie axioms are too weak -- don't force Jordan structure. Van de Wetering's strengthened axioms are necessary |
| QM reconstruction framework | Van de Wetering effect-theoretic | Chiribella-D'Ariano-Perinotti informational | Effect-theoretic framework connects most directly to sequential measurement structure of self-models |

---

## Sources

- Gudder, Greechie (2002), "Sequential products on effect algebras," Rep. Math. Phys. 49, 87-111 -- Original definition of sequential effect algebras
- Van de Wetering (2018), arXiv:1803.11139, J. Math. Phys. 60, 062201 (2019) -- Sequential product spaces are Jordan algebras (THE key theorem)
- Van de Wetering (2018), arXiv:1803.08453, J. Math. Phys. 59, 082202 (2018) -- Three characterisations of the standard sequential product
- Westerbaan, Westerbaan, van de Wetering (2020), arXiv:2004.12749, Quantum 4, 378 -- Three types of normal sequential effect algebras
- Barnum, Wilce (2014), arXiv:1202.4513, Found. Phys. 44, 192-212 -- Local tomography and Jordan structure of QT
- Barnum, Graydon, Wilce (2016/2020), arXiv:1606.09331, Quantum 4, 359 -- Composites and categories of EJAs
- Barnum, Ududec, van de Wetering (2023), arXiv:2306.00362 -- Self-duality from homogeneity and pure transitivity
- D'Ariano (2006), arXiv:quant-ph/0611094 -- Operational axioms for QM (involution from faithful states)
- D'Ariano (2007), arXiv:quant-ph/0701219 -- Operational axioms for C\*-algebraic QM
- Jordan, von Neumann, Wigner (1934), Ann. Math. 35, 29-64 -- Classification of formally real Jordan algebras
- Hanche-Olsen (1985), "JB-algebras with tensor products are C\*-algebras," in Operator Algebras and their Connections with Topology and Ergodic Theory, Springer -- THE theorem linking Jordan composites to C\*
- Hanche-Olsen, Stormer (1984), Jordan Operator Algebras, Pitman -- Standard reference on JB-algebras
- Chiribella, D'Ariano, Perinotti (2011), arXiv:1011.6451, Phys. Rev. A 84, 012311 -- Informational derivation of QT
- Masanes, Mueller (2011), arXiv:1004.1483, New J. Phys. 13, 063001 -- Derivation of QT from physical requirements
- Hardy (2001), arXiv:quant-ph/0101012 -- Quantum theory from five reasonable axioms
- Gudder (2005), "Open problems for sequential effect algebras," Int. J. Theor. Phys. 44, 755-770 -- Lists open problems in SEA theory
- Van de Wetering (2019), arXiv:1801.05798, Compositionality 1 (2019) -- Effect-theoretic reconstruction of QT
