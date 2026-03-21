# Research Summary

**Project:** Experiential Measure on Structure Space (v2.0 -- QM from Algebraic Genericity)
**Domain:** Quantum foundations / Algebraic quantum theory / QM reconstruction
**Researched:** 2026-03-20
**Confidence:** MEDIUM

## Unified Notation

All downstream work uses these conventions. Where research files differed, reconciliation is noted.

| Symbol | Quantity | Convention | Notes |
|--------|---------|-----------|-------|
| a . b | Sequential product | van de Wetering (arXiv:1803.11139) | Non-commutative; "test a then test b" |
| a o b | Jordan product | a o b = (1/2)(a . b + b . a) | Commutative; the symmetrized sequential product. NOTE: factor of 1/2 is easy to drop (Pitfall P6 checklist) |
| [0,1]\_V | Effect space | {a in V : 0 <= a <= 1} | Effects on order unit space V with unit 1 |
| 1 | Order unit | Identity effect / trivial test | Standard |
| Omega(V) | State space | Compact convex set of normalized positive functionals on V | Matches van de Wetering |
| a perp b | Orthogonality | a . b = 0 | Defined via sequential product, not algebraic complement |
| a\* | Involution / adjoint | C\*-algebra involution (goal of derivation) | Does NOT exist until Phase 2 succeeds |
| S1--S7 | Sequential product axioms | Van de Wetering (arXiv:1803.11139) formulation exclusively | NOT Gudder-Greechie original axioms (different S4). See Pitfall P8. |
| E(B), E(M) | Effect algebras of body, model | To be determined: E(B) vs E(B x M) is Phase 1 research question | See Pitfall P2 |
| EJA | Euclidean Jordan algebra | Finite-dimensional formally real Jordan algebra | JVW classification: 5 simple types |
| M\_n(K)\_sa | Self-adjoint n x n matrices over K | K in {R, C, H}; plus spin factors V\_n and Albert algebra M\_3(O)\_sa | Standard Jordan algebra notation |

**Unit system:** Natural (dimensionless algebraic quantities throughout).
**Metric/signature:** Not applicable (no spacetime structure; this is algebraic quantum foundations).
**Standing assumption:** All systems finite-dimensional.

**Convention conflict resolved:** METHODS.md sometimes uses a & b for the sequential product while PRIOR-WORK.md uses a . b. Both follow van de Wetering. We adopt a . b (dot notation) as standard, matching the published journal version (J. Math. Phys. 60, 062201). COMPUTATIONAL.md uses `seq(a,b)` in code, which is the programmatic representation.

## Executive Summary

This project aims to derive the C\*-algebra involution -- the last missing piece in the L4 --> QM chain -- from the sequential product structure of self-modeling systems. The route is: (1) show that the "test-update-test" operation on a self-modeling system satisfies van de Wetering's axioms S1--S7, which forces the algebra of effects to be a Euclidean Jordan algebra; (2) show that body-model compositionality implies local tomography, which via Hanche-Olsen's theorem promotes the Jordan algebra to a C\*-algebra. Both steps rest on established published theorems. The novelty and risk are entirely in verifying that the self-modeling construction satisfies the axiom inputs.

The critical bottleneck is axiom S4 (symmetry of orthogonality): if testing a then b gives zero, does testing b then a also give zero? For the standard quantum sequential product (Luders rule), this follows from spectral arguments. For the self-modeling product, the model-update step introduces an asymmetry that could break S4. No prior work has verified S4 for any construction beyond B(H). This is simultaneously the project's main novelty and its main risk. If S4 fails, a backup route exists via D'Ariano's faithful-state construction, and a conditional result (L4 + C\* ==> QM) is still publishable.

The computational work is lightweight proof-support: symbolic axiom checking on 2x2 and 3x3 matrix models using SymPy, with NumPy for numerical cross-checks. No HPC or specialized software is needed. The main computational deliverable is a test harness that verifies S1--S7 against known positive controls (Luders product), negative controls (asymmetric product violating S4), and the novel self-modeling product once formalized.

## Key Findings

### Methods

The project employs a sequence of established analytical methods, connected by published theorems, with one genuinely novel verification step.

- **Sequential product axiom verification (S1--S7):** Direct axiom-by-axiom checking against the self-modeling construction in the order unit space framework. S1--S3 are essentially free (linearity, continuity in finite dim, unit). S5--S7 are moderate algebraic consequences. S4 is the decisive test. [CONFIDENCE: HIGH for the method; MEDIUM for whether S4 holds]
- **Koecher-Vinberg pathway:** Once S1--S7 hold, van de Wetering Theorem 1 gives EJA structure automatically. This is a published theorem application, not novel work. [CONFIDENCE: HIGH]
- **Hanche-Olsen tensor product criterion:** Promotes Jordan --> C\* via local tomography. Also a published theorem. [CONFIDENCE: HIGH]
- **Local tomography from B-M independence:** The gap between "independent accessibility" and "local tomography" must be bridged. This is the second novel argument needed. Three techniques available: GPT dimension counting, information-theoretic argument, or categorical (Barnum-Wilce). [CONFIDENCE: MEDIUM]
- **D'Ariano faithful-state backup:** If S4 fails, construct the involution from a symmetric faithful state. Requires the B-M correlation state to be faithful and symmetric -- non-trivial but plausible. [CONFIDENCE: MEDIUM]

### Prior Work Landscape

The sequential product --> Jordan algebra --> C\* pipeline is well-established.

**Must reproduce (critical benchmarks):**
- Van de Wetering's Theorem 1: S1--S7 on finite-dim order unit space ==> EJA (this is invoked, not re-derived)
- Van de Wetering's Theorem 3 / Hanche-Olsen: EJA + locally tomographic composite ==> C\*-algebra (invoked)
- Westerbaan-Westerbaan-van de Wetering: associative sequential product ==> commutative (must verify self-modeling product is non-associative as a sanity check)
- Barnum-Graydon-Wilce: compositionality excludes Albert algebra (must verify B-M composite satisfies their conditions)

**Novel contributions (what this project adds):**
- First verification of S1--S7 for a physically motivated construction beyond B(H)
- Derivation of C\*-involution from a single operational premise (if S4 holds + local tomography proved)
- If S4 fails: precise characterization of which axiom the self-modeling product violates, and what additional assumption bridges the gap

**Critical observation from PRIOR-WORK.md:** Every existing QM reconstruction program smuggles in the involution via some axiom (purification, local tomography, continuous reversibility, faithful state). If v2.0 succeeds, it would be the first to derive the involution purely from operational measurement structure.

### Computational Approaches

All computation is proof-support, not simulation. The stack is SymPy (symbolic identity verification) + NumPy/SciPy (numerical cross-checks). No dedicated software exists for sequential product axiom verification -- a lightweight Python test harness must be built from scratch.

**Key computational elements:**
1. **Positive control:** Luders product on M\_2(C) must pass all S1--S7 checks (validates tooling)
2. **Negative control:** Plain matrix multiplication must fail S4 (validates S4 detection)
3. **Target:** Self-modeling sequential product (pending Phase 1 formalization)
4. **Spin factor models:** V\_n for n > 3 provide non-quantum EJAs that still satisfy S1--S7, useful for catching dimension-specific bugs

Resource requirements are negligible: matrices are at most 4x4 (8x8 for composites), all computation runs on a single CPU in under 10 minutes.

### Pitfalls

The 7 critical pitfalls, ranked by severity and likelihood.

1. **Circularity in the update map (P6):** If the self-modeling update rule uses Luders' rule, sqrt, inner product, or any Hilbert space structure, quantum mechanics is assumed, not derived. The update map must use ONLY order unit space primitives + the self-modeling constraint. Prevention: every step in Phase 1 must be audited for Hilbert space imports.
2. **S4 assumed rather than proved (P3):** S4 is the hardest axiom. It must be the longest, most detailed proof. If the proof is short, something is wrong. Prevention: dedicated S4 analysis with multiple techniques (spectral decomposition, inner product symmetry, faithfulness reduction, contrapositive search).
3. **Wrong effect algebra carrier (P2):** Effects on B vs effects on B x M give different sequential products. The correct framing is a RESULT of Phase 1, not a premise. Prevention: explore both framings in parallel.
4. **Conflating local tomography with independent accessibility (P4):** Independent accessibility means you CAN measure each subsystem. Local tomography means product measurements SUFFICE to determine the joint state. The gap is the entangled sector. Prevention: Phase 2 must explicitly address which EJA type emerges and prove local tomography for that type.
5. **Associativity kills non-commutativity (P9):** If the self-modeling sequential product is associative, the algebra is necessarily commutative (classical). This is a fatal obstruction. Prevention: verify non-associativity early in Phase 1 as a sanity check.
6. **Axiom version mismatch (P8):** Gudder-Greechie S4 != van de Wetering S4. Pin all references to arXiv:1803.11139 exclusively.
7. **Checking standard QM instead of the self-model (P1):** The false-progress trap. If any proof step invokes Hilbert space structure or works identically for any sequential product, it proves nothing about the self-modeling case.

## Approximation Landscape

| Method | Valid Regime | Breaks Down When | Controlled? | Complements |
|--------|-------------|-----------------|-------------|-------------|
| Sequential product axiom verification | Finite-dim order unit spaces with continuous sequential product | Infinite dimensions (need JB-algebra theory) | Yes (each axiom is a checkable identity) | D'Ariano backup if S4 fails |
| Koecher-Vinberg (S1-S7 --> EJA) | Finite-dim, homogeneous self-dual cones | Infinite-dim or non-self-dual cones | Yes (theorem with explicit conditions) | Direct Jordan algebra construction |
| Hanche-Olsen (EJA + tensor --> C\*) | JB-algebras admitting tensor products | Exceptional Jordan algebras (Albert algebra) | Yes (proven theorem) | Alfsen-Shultz orientation approach |
| Local tomography argument | Complex matrix algebras | Real, quaternionic, or spin factor algebras (local tomography fails for these) | Partially (depends on formalization of "independence") | Purification axiom (Hardy) |
| D'Ariano faithful-state route | Algebras with symmetric faithful states | Algebras without faithful states; or when composition-preservation fails | No (composition-preservation is postulated, not derived) | Sequential product route |

**Coverage gap:** The regime where S4 fails AND no faithful state exists is not covered by any method. In that case, the C\*-involution cannot be derived from self-modeling alone, and the result is the conditional statement: L4 + C\* ==> QM (still publishable, still novel).

## Theoretical Connections

### Established Connections

1. **Sequential products <--> Jordan algebras (van de Wetering 2018):** S1--S7 force EJA structure via Koecher-Vinberg. The Jordan product is the symmetrized sequential product: a o b = (1/2)(a . b + b . a). [ESTABLISHED]

2. **Jordan algebras + local tomography <--> C\*-algebras (Hanche-Olsen 1985, Barnum-Wilce 2014):** Among EJAs, only the complex matrix algebras M\_n(C)\_sa survive the local tomography constraint. The involution emerges because the self-adjoint part of a C\*-algebra inherits the \*-operation. [ESTABLISHED]

3. **Compositionality <--> exclusion of exceptional types (Barnum-Graydon-Wilce 2016/2020):** Having well-defined composites kills the Albert algebra, spin factors (n >= 4), and forces complex type -- independently of local tomography. This provides a second route to the same conclusion. [ESTABLISHED]

4. **Associativity <--> commutativity in SEAs (Westerbaan-Westerbaan-van de Wetering 2020):** Associative normal SEAs are commutative (classical). Quantum non-commutativity requires non-associativity of the sequential product. [ESTABLISHED]

### Conjectured Connections (to be proved/disproved by this project)

5. **Self-modeling "test-update-test" <--> sequential product satisfying S1--S7:** The central conjecture. If the self-modeling update map preserves enough structure, the operational "test-update-test" satisfies the sequential product axioms. [CONJECTURED -- this IS the project]

6. **B-M independent accessibility <--> local tomography:** If the self-model can probe B and M independently, and M faithfully tracks B, then product measurements suffice to determine the joint state. [CONJECTURED -- Phase 2]

7. **Model faithfulness <--> S4 symmetry of orthogonality:** If M is a faithful model of B (injective embedding of state spaces), the model update is isometric, and isometries preserve orthogonality symmetrically. This is the most physically motivated route to S4. [CONJECTURED -- Phase 1]

### Cross-Validation Opportunities

| | Koecher-Vinberg | Hanche-Olsen | Barnum-Graydon-Wilce | D'Ariano backup |
|---|:---:|:---:|:---:|:---:|
| **S1--S7 verification** | Produces EJA; check classification | -- | -- | -- |
| **Koecher-Vinberg** | -- | Promotes EJA to C\* | BGW compositionality independently excludes exceptional types | Both should give same C\* structure |
| **Hanche-Olsen** | -- | -- | Both select complex type from Jordan classification | Both derive involution (different routes) |

**High-risk node:** S4 verification has NO independent cross-check. If S4 holds, there is no second method to confirm it besides the direct proof. If S4 fails, the counterexample serves as confirmation. This is the single-point-of-failure in the methodology.

## Critical Claim Verification

| # | Claim | Source | Verification | Result |
|---|-------|--------|--------------|--------|
| 1 | S1-S7 on finite-dim order unit space ==> EJA (van de Wetering Thm 1) | METHODS.md, PRIOR-WORK.md | web\_search: van de Wetering sequential product Jordan algebras | CONFIRMED -- published J. Math. Phys. 60, 062201 (2019) |
| 2 | JB-algebra with tensor product ==> C\*-algebra (Hanche-Olsen) | METHODS.md, PRIOR-WORK.md | web\_search: Hanche-Olsen JB-algebras tensor products C\*-algebras | CONFIRMED -- LNM 1132 (1985), cited extensively |
| 3 | Associativity of normal SEA ==> commutativity | PITFALLS.md | web\_search: Westerbaan van de Wetering associativity commutativity | CONFIRMED -- Quantum 4, 378 (2020) |
| 4 | Compositionality excludes Albert algebra from composites | PRIOR-WORK.md | web\_search: Barnum Graydon Wilce composites exceptional Jordan | CONFIRMED -- Quantum 4, 359 (2020) |
| 5 | D'Ariano involution from faithful state + composition-preserving extension | METHODS.md | web\_search: D'Ariano operational axioms faithful state involution | CONFIRMED -- arXiv:quant-ph/0611094 (2006); key: composition-preservation is postulated (Postulate 5) |
| 6 | No prior verification of S1-S7 for any construction beyond B(H) | PRIOR-WORK.md | Inference from literature survey (no counterexample found in search) | UNVERIFIED -- plausible but cannot confirm a negative |
| 7 | Local tomography fails for real and quaternionic QM | PITFALLS.md | Known result from Barnum-Wilce (2014) arXiv:1202.4513 | CONFIRMED -- established in multiple sources |

## Implications for Roadmap

### Suggested Phase Structure

### Phase 1: Sequential Product Formalization and S1-S7 Verification

**Rationale:** Everything downstream depends on whether S1--S7 hold. The formal definition of the self-modeling sequential product is the foundational step -- without it, no axiom can be checked. S4 is the critical gate.

**Delivers:** (a) Formal definition of the self-modeling sequential product in the order unit space framework, with explicit effect algebra framing chosen (B vs B x M). (b) Proof or disproof of each axiom S1--S7. (c) If S1--S7 hold: the EJA classification of the resulting algebra. (d) Sanity checks: non-associativity, non-commutativity.

**Methods:** Direct axiom verification (Method 1), dedicated S4 analysis (Method 2), Koecher-Vinberg invocation (Method 3).

**Validates:** Self-modeling sequential product satisfies S1--S7; Jordan algebra classification; non-associativity confirmed.

**Avoids:** Pitfalls P1 (circular use of QM), P2 (wrong effect algebra), P3 (S4 assumed), P6 (circular update map), P8 (axiom version mismatch), P9 (associativity trap).

**Needs research:** YES -- this is genuinely novel territory; no prior work on S1--S7 for non-B(H) constructions.

**Risk:** HIGH -- S4 may fail.

### Phase 2: Local Tomography from B-M Compositionality

**Rationale:** Depends on Phase 1 succeeding (EJA structure established). Must bridge the gap from "independent accessibility" to "local tomography" to invoke Hanche-Olsen/Barnum-Wilce for Jordan --> C\* promotion.

**Delivers:** (a) Proof that B-M compositionality implies local tomography (or identification of the additional assumption needed). (b) C\*-algebra structure via Hanche-Olsen. (c) Explicit exclusion of non-complex EJA types (real, quaternionic, spin factor, Albert).

**Methods:** GPT compositional analysis (Method 5), Hanche-Olsen criterion (Method 4).

**Builds on:** Phase 1 (EJA structure), Barnum-Wilce (arXiv:1202.4513), Barnum-Graydon-Wilce (arXiv:1606.09331).

**Avoids:** Pitfalls P4 (conflating accessibility with tomography), P5 (Albert algebra obstruction), P7 (norm completion trap).

**Needs research:** YES -- the formalization of "independent accessibility implies local tomography" is novel.

**Risk:** MEDIUM -- the mathematical framework is established; the question is whether the self-modeling context provides the right operational assumptions.

### Phase 3: Paper Assembly (Paper 5)

**Rationale:** Depends on Phases 1--2. Assembles the complete L4 --> QM chain (if both phases succeed) or the conditional chain L4 + C\* --> QM (if either phase produces a partial result).

**Delivers:** Paper 5 with the full or conditional derivation.

**Methods:** Standard mathematical writing. The published theorems (van de Wetering, Hanche-Olsen, Barnum-Wilce) are cited; the novel content is the self-modeling --> S1--S7 verification and the local tomography argument.

**Needs research:** NO -- this is assembly of established results plus Phase 1--2 outputs.

**Risk:** LOW (assuming Phases 1--2 complete).

### Phase 4: D'Ariano Backup (Contingency)

**Rationale:** Triggered ONLY if Phase 1 fails at S4. Constructs the involution from D'Ariano's faithful-state method instead of the sequential product route.

**Delivers:** Involution from the B-M correlation state, if it is faithful and symmetric.

**Methods:** D'Ariano faithful-state construction (Method 6).

**Avoids:** Pitfall P10 (faithful state existence is non-trivial).

**Needs research:** YES (if triggered) -- must prove faithfulness and symmetry of the B-M correlation state.

**Risk:** MEDIUM-HIGH -- composition-preservation (D'Ariano's Postulate 5) may need to be postulated rather than derived, which weakens the "one premise" claim.

### Phase Ordering Rationale

- Phase 1 before Phase 2: Phase 2 assumes EJA structure, which Phase 1 establishes.
- Phase 2 before Phase 3: Paper requires complete chain.
- Phase 4 is conditional: only triggered by Phase 1 failure at S4.
- Phases 1 and 2 are strictly sequential (no parallelism).
- Within Phase 1: S1--S3 in parallel, then S4 (the gate), then S5--S7 only if S4 passes.

### Phases Requiring Deep Investigation

- **Phase 1 (S4 verification):** No literature precedent for this specific verification. Multiple proof techniques available but none guaranteed to work.
- **Phase 2 (local tomography argument):** The formalization of "independent accessibility implies local tomography" is novel. Standard GPT framework provides tools but the specific argument is new.

Phases with established methodology:
- **Phase 3 (paper assembly):** Straightforward once results are in hand.
- **Phase 1 (S1--S3, S5--S7):** These axioms follow established patterns; the difficulty is concentrated in S4.

### Input Quality --> Roadmap Impact

| Input File | Quality | Affected Recommendations | Impact if Wrong |
|------------|---------|------------------------|-----------------|
| METHODS.md | Good | Method selection, phase ordering, S4 proof techniques | Phases 1-2 may need different proof strategies |
| PRIOR-WORK.md | Good | Benchmark theorems, chain of published results | Unlikely wrong (published theorems); would invalidate the entire approach |
| COMPUTATIONAL.md | Good | Tool selection, test harness design | Low impact (computational work is proof-support, not the main argument) |
| PITFALLS.md | Good | Risk mitigation across all phases | Blind spots in Phase 1 formalization are the main danger |

## Confidence Assessment

| Area | Confidence | Notes |
|------|-----------|-------|
| Methods | MEDIUM | Methods themselves are sound (published theorems). Confidence is MEDIUM because the novel step (S4 verification) has unknown difficulty. |
| Prior Work | HIGH | All key theorems are published and peer-reviewed. The logical chain from sequential products to C\*-algebras is well-established. |
| Computational Approaches | MEDIUM | Adequate for proof-support. The key limitation is that computation cannot prove S4 in general -- it can only find counterexamples or build confidence. |
| Pitfalls | HIGH | Comprehensive identification of failure modes. The pitfall-to-phase mapping is complete. |

**Overall confidence:** MEDIUM. The downstream mathematics is solid; the uncertainty is concentrated in the novel steps (S4 verification and local tomography formalization).

### Gaps to Address

- **S4 proof technique:** No single technique is guaranteed. The "model faithfulness implies S4" route (Technique 2d in METHODS.md) is the most promising but requires formalizing "faithful model" in the order unit space setting.
- **Effect algebra framing:** E(B) vs E(B x M) must be resolved in Phase 1. Both framings should be explored in parallel.
- **Qubit existence:** Barnum-Wilce requires at least one qubit-like system. Must verify that the self-modeling framework admits a 2-dimensional subsystem.
- **D'Ariano backup feasibility:** If needed, the faithfulness and symmetry of the B-M correlation state are non-trivial claims requiring independent proofs.

## Open Questions

1. **Does the self-modeling sequential product satisfy S4?** [PRIORITY: HIGH, blocks Phase 1] -- The decisive question of the entire project. If yes, Jordan algebra structure follows. If no, the sequential product route fails.

2. **Which effect algebra framing is correct -- E(B) or E(B x M)?** [PRIORITY: HIGH, blocks Phase 1] -- The two framings give different sequential products. One may satisfy S4 while the other does not.

3. **Does B-M independent accessibility imply local tomography?** [PRIORITY: HIGH, blocks Phase 2] -- The gap between "can measure independently" and "product measurements suffice" must be bridged.

4. **Does the self-modeling framework admit a qubit-like system?** [PRIORITY: MEDIUM, blocks Phase 2] -- Barnum-Wilce requires at least one 2-dimensional system.

5. **Is the self-modeling sequential product non-associative?** [PRIORITY: MEDIUM, blocks Phase 1 early] -- If associative, the algebra is necessarily commutative (classical). Quick sanity check.

6. **If S4 fails, is the B-M correlation state faithful?** [PRIORITY: LOW until Phase 1 fails, then HIGH] -- Needed for D'Ariano backup route.

## Sources

### Primary (HIGH confidence)

- van de Wetering, "Sequential product spaces are Jordan algebras," [J. Math. Phys. 60, 062201 (2019)](https://arxiv.org/abs/1803.11139) -- S1-S7, Theorem 1 (S1-S7 => EJA), Theorem 3 (EJA + local tomography => C\*)
- van de Wetering, "Three characterisations of the sequential product," [J. Math. Phys. 59, 082202 (2018)](https://arxiv.org/abs/1803.08453) -- Uniqueness of Luders product; inner product symmetry characterization
- Gudder and Greechie, "Sequential products on effect algebras," Rep. Math. Phys. 49, 87-111 (2002) -- Original sequential effect algebra definition
- Westerbaan, Westerbaan, van de Wetering, "The three types of normal sequential effect algebras," [Quantum 4, 378 (2020)](https://arxiv.org/abs/2004.12749) -- Classification; associativity => commutativity
- Barnum and Wilce, "Local tomography and the Jordan structure of quantum theory," [Found. Phys. 44, 192-212 (2014)](https://arxiv.org/abs/1202.4513) -- Jordan + local tomography + qubit => complex QM
- Barnum, Graydon, Wilce, "Composites and categories of Euclidean Jordan algebras," [Quantum 4, 359 (2020)](https://arxiv.org/abs/1606.09331) -- Compositionality excludes exceptional types
- Hanche-Olsen, "JB-algebras with tensor products are C\*-algebras," [LNM 1132, Springer (1985)](https://link.springer.com/content/pdf/10.1007/BFb0074886) -- THE Jordan-to-C\* promotion theorem
- Jordan, von Neumann, Wigner, "On an algebraic generalization of the quantum mechanical formalism," Ann. Math. 35, 29-64 (1934) -- Classification of formally real Jordan algebras

### Secondary (MEDIUM confidence)

- D'Ariano, "Operational axioms for quantum mechanics," [arXiv:quant-ph/0611094 (2006)](https://arxiv.org/abs/quant-ph/0611094) -- Faithful state construction of involution (backup route)
- Barnum, Ududec, van de Wetering, "Self-duality from homogeneity and pure transitivity," [arXiv:2306.00362 (2023)](https://arxiv.org/abs/2306.00362) -- Reduces geometric assumptions for Koecher-Vinberg (preprint)
- Plavala, "General probabilistic theories: An introduction," [Physics Reports 1033, 1-64 (2023)](https://arxiv.org/abs/2103.07469) -- GPT review covering effect algebras in GPT context

### Tertiary (LOW confidence -- useful for context only)

- Gudder, "Open problems for sequential effect algebras," Int. J. Theor. Phys. 44, 755-772 (2005) -- Historical open problems
- Stuckey et al. (2024), "Completing QRP via relativity" -- Tangential; different philosophical framework

---

_Research synthesis completed: 2026-03-20_
_Ready for research plan: yes_

```yaml
# --- ROADMAP INPUT (machine-readable, consumed by gpd-roadmapper) ---
synthesis_meta:
  project_title: "Experiential Measure on Structure Space (v2.0)"
  synthesis_date: "2026-03-20"
  input_files: [METHODS.md, PRIOR-WORK.md, COMPUTATIONAL.md, PITFALLS.md]
  input_quality: {METHODS: good, PRIOR-WORK: good, COMPUTATIONAL: good, PITFALLS: good}

conventions:
  unit_system: "natural"
  metric_signature: "N/A"
  fourier_convention: "N/A"
  coupling_convention: "N/A"
  renormalization_scheme: "N/A"

methods_ranked:
  - name: "Sequential product axiom verification (S1-S7)"
    regime: "Finite-dim order unit spaces"
    confidence: MEDIUM
    cost: "Analytical proof work; computational support O(n^3) per matrix multiply, n <= 8"
    complements: "D'Ariano faithful-state backup"
  - name: "Koecher-Vinberg pathway (S1-S7 => EJA)"
    regime: "Finite-dim homogeneous self-dual cones"
    confidence: HIGH
    cost: "Theorem citation (near zero)"
    complements: "Direct Jordan algebra construction"
  - name: "Hanche-Olsen tensor product criterion (EJA => C*)"
    regime: "JB-algebras admitting tensor products"
    confidence: HIGH
    cost: "Theorem citation (near zero)"
    complements: "Alfsen-Shultz orientation approach"
  - name: "Local tomography from B-M independence"
    regime: "GPT composites of EJAs"
    confidence: MEDIUM
    cost: "Analytical proof work"
    complements: "Hardy purification axiom"
  - name: "D'Ariano faithful-state backup"
    regime: "Algebras with symmetric faithful states"
    confidence: MEDIUM
    cost: "Analytical proof work (2-3 weeks)"
    complements: "Sequential product route (primary)"

phase_suggestions:
  - name: "Sequential Product Formalization and S1-S7 Verification"
    goal: "Prove or disprove that self-modeling sequential product satisfies S1-S7, yielding EJA structure"
    methods: ["Sequential product axiom verification (S1-S7)", "Koecher-Vinberg pathway (S1-S7 => EJA)"]
    depends_on: []
    needs_research: true
    risk: HIGH
    pitfalls: ["P1-circular-verification", "P2-wrong-effect-algebra", "P3-S4-assumed", "P6-circular-update-map", "P8-axiom-version-mismatch", "P9-associativity-trap"]
  - name: "Local Tomography from B-M Compositionality"
    goal: "Prove B-M independent accessibility implies local tomography, promoting Jordan algebra to C*-algebra"
    methods: ["Local tomography from B-M independence", "Hanche-Olsen tensor product criterion (EJA => C*)"]
    depends_on: ["Sequential Product Formalization and S1-S7 Verification"]
    needs_research: true
    risk: MEDIUM
    pitfalls: ["P4-local-tomo-conflation", "P5-Albert-algebra", "P7-norm-completion"]
  - name: "Paper Assembly (Paper 5)"
    goal: "Assemble complete L4 => QM chain (or conditional L4 + C* => QM) into publishable paper"
    methods: []
    depends_on: ["Local Tomography from B-M Compositionality"]
    needs_research: false
    risk: LOW
    pitfalls: ["publication-overclaiming"]
  - name: "D'Ariano Backup (Contingency)"
    goal: "Construct involution from faithful B-M correlation state if S4 fails"
    methods: ["D'Ariano faithful-state backup"]
    depends_on: ["Sequential Product Formalization and S1-S7 Verification"]
    needs_research: true
    risk: HIGH
    pitfalls: ["P10-faithful-state-existence"]

critical_benchmarks:
  - quantity: "Van de Wetering Theorem 1 (S1-S7 => EJA)"
    value: "Published theorem -- must be correctly invoked"
    source: "van de Wetering, J. Math. Phys. 60, 062201 (2019)"
    confidence: HIGH
  - quantity: "Hanche-Olsen criterion (EJA + tensor => C*)"
    value: "Published theorem -- must be correctly invoked"
    source: "Hanche-Olsen, LNM 1132 (1985)"
    confidence: HIGH
  - quantity: "Associativity => commutativity for normal SEAs"
    value: "Published theorem -- sanity check (product must be non-associative)"
    source: "Westerbaan-Westerbaan-van de Wetering, Quantum 4, 378 (2020)"
    confidence: HIGH
  - quantity: "Compositionality excludes Albert algebra"
    value: "Published theorem -- B-M composite must satisfy BGW conditions"
    source: "Barnum-Graydon-Wilce, Quantum 4, 359 (2020)"
    confidence: HIGH

open_questions:
  - question: "Does the self-modeling sequential product satisfy S4 (symmetry of orthogonality)?"
    priority: HIGH
    blocks_phase: "Sequential Product Formalization and S1-S7 Verification"
  - question: "Which effect algebra framing is correct -- E(B) or E(B x M)?"
    priority: HIGH
    blocks_phase: "Sequential Product Formalization and S1-S7 Verification"
  - question: "Does B-M independent accessibility imply local tomography?"
    priority: HIGH
    blocks_phase: "Local Tomography from B-M Compositionality"
  - question: "Does the self-modeling framework admit a qubit-like (2-dimensional) system?"
    priority: MEDIUM
    blocks_phase: "Local Tomography from B-M Compositionality"
  - question: "Is the self-modeling sequential product non-associative?"
    priority: MEDIUM
    blocks_phase: "Sequential Product Formalization and S1-S7 Verification"

contradictions_unresolved: []
```
