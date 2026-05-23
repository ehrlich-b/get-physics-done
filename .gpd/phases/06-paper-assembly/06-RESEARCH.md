# Phase 6: Paper Assembly - Research

**Researched:** 2026-03-21
**Domain:** Quantum foundations / QM reconstruction / Mathematical physics writing
**Confidence:** HIGH

## Summary

Phase 6 assembles the complete derivation chain (self-modeling -> complex QM) into a publication-ready manuscript. The technical content is complete: Phase 4 proved S1-S7 (186 SymPy tests), Phase 5 proved local tomography, excluded non-complex types, and promoted to C*-algebra (658+ SymPy tests, 6/6 contract targets verified). The task is expository and structural, not mathematical.

The central challenge is presenting a genuinely novel result -- deriving QM from a single operational premise -- in a way that (a) the logical chain is airtight and self-contained, (b) the novelty claims are calibrated (neither overclaiming nor underselling), (c) the load-bearing assumptions are honestly flagged, and (d) the paper positions itself clearly against the existing reconstruction landscape.

**Primary recommendation:** Structure the paper as a linear logical chain (premise -> construction -> theorem invocation -> conclusion) with a detailed comparison table showing this work uses one premise where competitors use 3-6. Target the journal Quantum (quantum-journal.org), which has published most major reconstruction papers since 2017 and has a strong foundations readership.

## User Constraints

See phase CONTEXT.md for locked decisions and user constraints that apply to this phase.

Key constraints affecting this research:
- Paper type is FULL CHAIN (one premise -> QM). Not conditional.
- Logical chain is locked: Steps 1-8 as specified in CONTEXT.md.
- Load-bearing assumptions must be honestly stated: finite-dimensional spectral OUS, faithful self-modeling, minimality of composite, simple EJA.
- Unique selling point is locked: "Self-modeling is the single operational premise from which complex quantum mechanics -- including the complex field, the involution, and local tomography -- is derived, not assumed."

Discretion areas (recommendations needed):
- Target venue selection
- Notation and presentation style
- Proof detail level vs. proof sketches with references
- Discussion section structure
- Whether to include appendices for SymPy verifications

Deferred (OUT OF SCOPE):
- Infinite-dimensional generalization
- Non-Markovian self-models
- Detailed comparison with other reconstruction programs (save for future paper)
- Blog series writeup

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| --- | --- | --- | --- | --- |
| ref-vdw2018 (arXiv:1803.11139) | method + benchmark | Theorem 1 (S1-S7 -> EJA) and Theorem 3 (SP + LT -> C*) are the two central published theorems invoked | cite with explicit theorem numbers | Introduction, Theorem statements, References |
| ref-gudder-greechie (2002) | method | Original sequential product definition; historical anchor | cite for context | Introduction, Definition section |
| ref-barnum2023 (arXiv:2306.00362) | method | Composites of EJAs; supports composite construction | cite | Composite section |
| ref-barandes (2025) | prior art | Stochastic-quantum bijection; downstream application of QM structure | cite if Barandes chain invoked | Discussion (optional) |
| ref-motzkin-taussky (1955) | prior art | Generic non-commutativity; downstream result | cite if NC chain invoked | Discussion (optional) |
| ref-hanche-olsen (1985) | benchmark | JB-algebra + tensor product -> C*-algebra; the Jordan-to-C* promotion | cite with theorem statement | C*-promotion section |
| ref-barnum-wilce (arXiv:1202.4513) | benchmark | EJA + LT + qubit -> M_n(C)^sa; type exclusion | cite with theorem statement | Type exclusion section |
| Phase 4 derivations | prior artifact | All S1-S7 proofs, corrected product formula | incorporate results | Main body |
| Phase 5 derivations | prior artifact | LT proof, type exclusion, C*-promotion, involution | incorporate results | Main body |

**Missing or weak anchors:** None. All required anchors have been verified in prior phases. The Barandes and Motzkin-Taussky anchors are optional for the paper (they concern the downstream NC -> matrix algebra -> QM chain, which is established but tangential to the main contribution).

## Conventions

| Choice | Convention | Alternatives | Source |
| --- | --- | --- | --- |
| Sequential product notation | a . b (dot) or a & b | Various | van de Wetering (arXiv:1803.11139) |
| Jordan product | a o b = (1/2)(a . b + b . a) | Different factor conventions | Standard |
| Effect space | [0,1]_V | E(V) | van de Wetering |
| Order unit | 1 (bold or plain) | u, e | van de Wetering |
| Metric signature | N/A (algebraic, no spacetime) | -- | -- |
| Units | Dimensionless algebraic quantities | -- | -- |
| EJA types | JVW classification: R, C, H, spin, Albert | -- | Jordan-von Neumann-Wigner (1934) |
| Involution | X* = X^dagger (conjugate transpose) | -- | Standard |
| Axiom source | arXiv:1803.11139 Definition 2 EXCLUSIVELY | Gudder-Greechie (different S4) | CRITICAL: do not mix axiom versions |

**CRITICAL: All equations and results below use these conventions. The paper must use a single consistent notation throughout. Recommend a . b for the sequential product (matching vdW's published notation) and reserving & for internal derivation files only.**

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in This Phase |
| --- | --- | --- | --- |
| a . b (S1-S7 axioms) | Sequential product axioms | vdW Def. 2 | Central definition |
| a o b = (1/2)(a . b + b . a) | Jordan product from SP | vdW | Derived structure |
| Corrected SP: sum_i lambda_i C_{p_i}(b) + sum_{i<j} sqrt(lambda_i lambda_j) P_{ij}(b) | Self-modeling product formula | Phase 4 (Eq. 04-06.4) | Novel construction |
| B(a,b) = tau(a * phi^{-1}(b)) | Correlation bilinear form | Phase 5 (Eq. 05-01.4) | Bridges tracking -> LT |
| dim(V_BM) = dim(V_B) * dim(V_M) | Local tomography condition | Phase 5 (Eq. 05-01.5) | Key result |
| (n-1)^2 = 0 | Type exclusion algebraic condition | Phase 5 (Eq. 05-02.2) | Excludes R, H |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --- | --- | --- | --- |
| Theorem invocation with hypothesis verification | Apply published results by verifying all premises | Every theorem application | Standard mathematical practice |
| LaTeX manuscript preparation | Typeset the paper | Entire phase | -- |
| Comparison table construction | Position against competitors | Discussion section | Mueller (2021) review |

### Approximation Schemes

Not applicable. This phase is expository, not computational. All results are exact (algebraic, not numerical).

## Standard Approaches

### Approach 1: Linear Logical Chain Presentation (RECOMMENDED)

**What:** Present the derivation as a single linear chain: premise -> definition -> lemma -> theorem -> corollary, with each step building on the previous one. No forward references. A reader can verify correctness by reading front-to-back.

**Why standard:** This is how all successful reconstruction papers are structured: Hardy (2001), Chiribella et al. (2011), Dakic-Brukner (2011), Masanes-Mueller (2013), Barnum-Mueller-Ududec (2014). The linear structure makes the logical dependencies explicit and the premise count verifiable.

**Track record:** Every major reconstruction paper follows this pattern. The field rewards clarity and verifiability above technical virtuosity.

**Key steps:**

1. State the premise (self-modeling) precisely with all standing assumptions
2. Construct the sequential product from self-modeling operations (novel step 1)
3. Verify S1-S7 axiom-by-axiom (novel step 2 -- proof sketches with key ideas, full proofs in appendix or supplementary)
4. Invoke vdW Theorem 1 to get EJA structure (theorem citation)
5. Construct the composite and prove local tomography (novel step 3)
6. Exclude non-complex types via dimension counting + BGW (theorem citations + novel argument)
7. Promote to C*-algebra via vdW Theorem 3 / Hanche-Olsen (theorem citation)
8. Exhibit the involution as conjugate transpose (concluding observation)
9. Discussion: comparison with other programs, load-bearing assumptions, future directions

**Known difficulties at each step:**

- Step 1: Defining "self-modeling" precisely without importing Hilbert space structure. Must use only OUS primitives.
- Step 3: S4 is the hardest axiom. The paper must convey why it is non-trivial without burying the reader in Peirce decomposition details.
- Step 5: The gap between independent accessibility and local tomography is subtle. Must explain why minimality is needed.
- Step 9: Calibrating claims. Must not overclaim ("we derive all of QM from one axiom") or undersell ("we derive the involution under several assumptions").

### Approach 2: Theorem-First / Abstract-First Presentation (FALLBACK)

**What:** State the main theorem first ("A finite-dimensional system that faithfully self-models is governed by complex quantum mechanics"), then prove it in stages.

**When to switch:** If the linear chain is too long for the target venue's page limits.

**Tradeoffs:** More immediately impactful (reader sees the result on page 1) but harder to verify (reader must hold the whole argument in mind while reading proofs).

### Anti-Patterns to Avoid

- **Overclaiming scope:** "We derive QM from one axiom" is misleading without flagging the standing assumptions (finite-dim, faithful, minimal composite, simple EJA). The correct claim is: "We derive complex QM for finite-dimensional systems from a single operational premise (self-modeling), given a faithful self-model and the standard GPT composite construction."
- **Burying the novel content:** The novel contributions are (a) the self-modeling sequential product construction, (b) the S4 proof via Peirce feedback, (c) the local tomography argument via correlation form non-degeneracy. These must be prominent, not lost in a sea of theorem citations.
- **Notation inconsistency:** The derivation files use both a & b and a . b. Pick one for the paper and stick to it.
- **Ignoring the circularity question:** Referees WILL ask "isn't the sqrt in your product formula importing Hilbert space structure?" The circularity audit must be referenced or summarized in the paper.

## Existing Results to Leverage

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
| --- | --- | --- | --- |
| vdW Theorem 1 | S1-S7 on finite-dim OUS => EJA | J. Math. Phys. 60, 062201 (2019) | Invoke after verifying S1-S7 |
| vdW Theorem 3 | SP space + LT composite => C*-algebra | J. Math. Phys. 60, 062201 (2019) | Invoke after proving LT |
| Hanche-Olsen | JB-algebra + tensor product => C*-algebra | LNM 1132 (1985) | Consistency check on vdW Thm 3 |
| Barnum-Wilce | EJA + LT + qubit => M_n(C)^sa | Found. Phys. 44, 192-212 (2014) | Type identification |
| BGW | No non-signaling composite with Albert summand | Quantum 4, 359 (2020) | Albert exclusion |
| JVW classification | 5 simple EJA types | Ann. Math. 35, 29-64 (1934) | Classification enumeration |
| Westerbaan-Westerbaan-vdW | Associative normal SEA => commutative | Quantum 4, 378 (2020) | Sanity check (cite only) |

**Key insight:** The paper's novelty is NOT in the downstream theorems (vdW, Hanche-Olsen, Barnum-Wilce) -- those are established. The novelty is in the upstream construction: showing that self-modeling produces a sequential product satisfying S1-S7, and that faithful tracking implies local tomography. Re-deriving the downstream theorems would waste pages and obscure the contribution.

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
| --- | --- | --- | --- |
| Corrected SP formula (Eq. 04-06.4) | Explicit product on M_n(C)^sa | Phase 4 | Self-modeling with faithful phi |
| Correlation form non-degeneracy | Bridge from tracking to LT | Phase 5 | Simple EJA, faithful phi |
| Dimension mismatch (n-1)^2 = 0 | Clean exclusion of R, H types | Phase 5 | n >= 2 |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| --- | --- | --- | --- | --- |
| "Quantum Theory From Five Reasonable Axioms" | Hardy | 2001 | First GPT reconstruction; 5 axioms | Comparison: 5 axioms vs our 1 premise |
| "Informational derivation of quantum theory" | Chiribella, D'Ariano, Perinotti | 2011 | 6 axioms (5 + purification) | Comparison: purification as extra axiom |
| "Quantum Theory and Beyond" | Dakic, Brukner | 2009/2011 | 4 axioms (incl. local tomography) | Comparison: LT assumed, we derive it |
| "Existence of an information unit" | Masanes, Mueller, Augusiak, Perez-Garcia | 2013 | 3 postulates | Comparison: closest in parsimony |
| "Higher-order interference..." | Barnum, Mueller, Ududec | 2014 | 4 postulates, single-system | Comparison: different approach to complex selection |
| "Reconstructing QT from diagrammatic postulates" | Selby, Scandolo, Coecke | 2021 | Categorical reconstruction | Comparison: different mathematical framework |
| "An effect-theoretic reconstruction" | van de Wetering | 2019 | Effectus theory reconstruction | Comparison: same author, different route |
| "Probabilistic Theories and Reconstructions" | Mueller | 2021 | Review of reconstruction landscape | Use for positioning and comparison framing |
| "Defending the quantum reconstruction program" | Various | 2024 | Addresses common objections | Anticipate referee concerns |
| "Self-Simulation Hypothesis" | Irwin, Amaral, Chester | 2020 | Self-simulation in QM | Tangential; different meaning of "self-modeling" |

## Competing Reconstruction Programs: Premise Comparison

This table is the core positioning tool for the paper.

| Program | Authors | Year | Premises/Axioms | Key Axioms | Derives | Complex Selection |
| --- | --- | --- | --- | --- | --- | --- |
| Hardy | Hardy | 2001 | 5 | Subspaces, composite, continuity, simplicity, complementarity | Complex QM (via Simplicity) | Simplicity axiom |
| CDP | Chiribella, D'Ariano, Perinotti | 2011 | 6 | Causality, distinguishability, compression, local distinguishability, pure conditioning + Purification | Complex QM | Purification |
| Dakic-Brukner | Dakic, Brukner | 2011 | 4 | Information capacity, subspace, local tomography, reversibility | Complex QM | Local tomography (assumed) |
| Masanes-Mueller | Masanes, Mueller et al. | 2013 | 3 | Tomographic locality, continuous reversibility, subspace axiom | Complex QM | Tomographic locality (assumed) |
| Barnum-Mueller-Ududec | Barnum, Mueller, Ududec | 2014 | 4 | No higher-order interference, classical decomposability, strong symmetry, energy observability | Complex QM | Energy observability |
| Selby-Scandolo-Coecke | Selby, Scandolo, Coecke | 2021 | ~6 | Diagrammatic/categorical postulates + symmetric purification | Complex QM | Symmetric purification |
| van de Wetering | van de Wetering | 2019 | ~5 | Effectus theory axioms | Embeds into C*-algebras | Effectus axioms |
| Alfsen-Shultz | Alfsen, Shultz | 2001-2003 | Geometric | State space geometry + orientation | C*-algebra characterization | Orientation |
| **This work** | **[authors]** | **2026** | **1** | **Self-modeling (faithful self-model of finite-dim system)** | **Complex QM** | **Derived (LT from faithful tracking)** |

**Critical distinction:** Every other program either (a) assumes local tomography / tomographic locality as an axiom, (b) assumes purification, (c) assumes continuous reversibility, or (d) assumes multiple independent operational principles. This work derives local tomography from the self-modeling structure and does not assume it. The complex field is output, never input.

**Honest caveat:** The standing assumptions (finite-dim, faithful, minimal composite, simple EJA) are not "axioms" in the same sense as Hardy's or CDP's, but they are structural assumptions that constrain the scope. The paper must be transparent about this: the claim is "one operational premise plus standard structural assumptions," not "one axiom with no assumptions."

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
| --- | --- | --- | --- |
| LaTeX | Standard (pdflatex or lualatex) | Manuscript typesetting | Universal for physics papers |
| BibTeX / BibLaTeX | Standard | Reference management | Universal |
| SymPy verification code | Python 3 + SymPy | Appendix material; verification evidence | Already built in Phases 4-5 |

### Supporting Tools

| Tool | Purpose | When to Use |
| --- | --- | --- |
| matplotlib | Figures (if any -- e.g., derivation chain diagram) | Optional: visual summary of logical chain |
| tikz / tikz-cd | LaTeX diagrams | If including commutative diagrams or chain diagrams |

### Computational Feasibility

No new computation required. All computational work was completed in Phases 4-5. The paper may reference the 186 + 658 = 844+ SymPy tests as supplementary verification evidence.

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| --- | --- | --- | --- |
| Circularity audit | No Hilbert space imports before conclusion | Trace every definition/lemma for QM presuppositions | Zero imports; complex numbers appear only at Barnum-Wilce conclusion |
| Premise count | Exactly one operational premise | List all assumptions; classify as premise vs. structural | One premise (self-modeling) + 4 structural assumptions |
| Citation accuracy | All theorem invocations correct | Verify theorem numbers, hypothesis lists | All match published sources |
| Notation consistency | Single notation system | Global search for notation variants | No conflicts |
| Logical completeness | No gaps in the chain | Verify each step's output feeds the next step's input | Complete chain from self-modeling to M_n(C) |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| --- | --- | --- | --- |
| Classical limit | All effects diagonal (commuting) | Pointwise multiplication; classical probability | Phase 4 verification |
| Qubit case (n=2) | 2-dimensional system | M_2(C) with Luders product | Phase 4 (V_3 identification) |
| Real QM | K = R | LT fails (dim mismatch: 9 != 10) | Phase 5 negative check |
| Quaternionic QM | K = H | LT fails (dim mismatch: 36 != 28) | Phase 5 negative check |

### Red Flags During Manuscript Preparation

- If the logical chain has a step that requires citing an unpublished result (other than the present work), something is wrong.
- If the circularity audit fails at any step, the paper cannot be submitted.
- If the premise count exceeds one, the USP is lost and the framing must change.
- If a referee can identify a hidden assumption not listed in the assumptions section, credibility is damaged.

## Common Pitfalls

### Pitfall 1: Overclaiming Scope

**What goes wrong:** Claiming "we derive QM from one axiom" without qualifying the standing assumptions.
**Why it happens:** Natural enthusiasm; the result is genuinely impressive with one operational premise.
**How to avoid:** Always state "one operational premise" not "one axiom." List all four structural assumptions prominently. Frame as: "the operational content reduces to a single premise; the structural framework is standard GPT."
**Warning signs:** If a colleague reads the abstract and says "but you assumed finite dimensions," the framing is wrong.
**Recovery:** Rewrite abstract and introduction to foreground structural assumptions alongside the premise.

### Pitfall 2: Underselling the Novelty

**What goes wrong:** Presenting the work as "just" applying known theorems (vdW, Hanche-Olsen, Barnum-Wilce).
**Why it happens:** The downstream theorems are established; the upstream construction is where the novelty lives.
**How to avoid:** Emphasize three novel contributions: (a) self-modeling SP construction, (b) S4 proof via Peirce feedback, (c) LT from correlation form non-degeneracy. These are not applications of known theorems -- they are new physics arguments.
**Warning signs:** If the Introduction reads like a literature review with a new example appended.
**Recovery:** Restructure to lead with "what's new" before "what we invoke."

### Pitfall 3: Mixing Axiom Versions

**What goes wrong:** Citing Gudder-Greechie S4 when the proof uses van de Wetering S4 (they differ).
**Why it happens:** Both sources define "sequential product axioms" but with different S4 formulations.
**How to avoid:** Pin ALL axiom references to arXiv:1803.11139 Definition 2. Cite Gudder-Greechie for historical context only, with explicit note that axiom numbering differs.
**Warning signs:** Any axiom reference that cites Gudder-Greechie as the operative definition.
**Recovery:** Global search-and-replace of axiom citations.

### Pitfall 4: Failing to Address the sqrt Circularity Question

**What goes wrong:** A referee asks "doesn't the sqrt in your product formula presuppose the spectral theorem, which presupposes Hilbert space?"
**Why it happens:** The corrected product formula uses sqrt(lambda_i * lambda_j), which looks like it imports QM structure.
**How to avoid:** Include a circularity audit section (or remark) explaining: the sqrt is applied to REAL NUMBERS (eigenvalues of a spectral OUS element), not to operators. Spectral decomposition in an OUS is a lattice-theoretic operation, not a Hilbert space operation. The Luders rule sqrt(a)*b*sqrt(a) is the CONSEQUENCE, not the definition.
**Warning signs:** If the derivation section doesn't address this point at all.
**Recovery:** Add a "Remark on circularity" after the corrected product formula.

### Pitfall 5: Page Budget Misallocation

**What goes wrong:** Spending too many pages on standard theorem citations (vdW, Hanche-Olsen) and too few on the novel constructions.
**Why it happens:** Theorem statements are easy to write; novel proofs are harder to present clearly.
**How to avoid:** Budget roughly: 2 pages for introduction/setup, 3-4 pages for novel SP construction and S1-S7, 2 pages for composite and LT, 1 page for type exclusion and C*-promotion, 2 pages for discussion. Published theorems get 1-2 sentence summaries, not full re-statements.
**Warning signs:** If the novel S4 proof gets less space than the statement of vdW Theorem 1.
**Recovery:** Compress theorem citations; expand novel arguments.

## Venue Analysis and Recommendation

### Venue Comparison

| Venue | Impact | Scope | Turnaround | Prior Reconstruction Papers | Fit |
| --- | --- | --- | --- | --- | --- |
| **Quantum** (quantum-journal.org) | IF ~5.7, Q1 | Quantum science broadly | ~3-6 months | vdW (Quantum 4, 2020), BGW (Quantum 4, 2020), Selby-Scandolo-Coecke (Quantum 5, 2021) | EXCELLENT -- primary venue for modern reconstruction papers |
| Physical Review A | IF ~2.9 | Atomic, molecular, optical, quantum info | ~3-6 months | CDP (PRA 84, 2011) | GOOD -- prestigious, broad QM audience |
| Foundations of Physics | IF ~1.5 | Foundations specifically | ~6-12 months | Many historical papers | GOOD -- targeted audience but slower, lower impact |
| Journal of Mathematical Physics | IF ~1.3 | Mathematical physics | ~6-12 months | vdW (JMP 60, 2019) | MODERATE -- mathematical audience, less foundations focus |
| New Journal of Physics | IF ~2.8 | All physics | ~3-6 months | Barnum-Mueller-Ududec (NJP 16, 2014) | MODERATE -- broad scope, less targeted |
| PNAS | IF ~11 | All sciences | Fast-track possible | Masanes-Mueller (PNAS 110, 2013) | HIGH IMPACT but hard to get in; need a member to communicate |
| Communications in Mathematical Physics | IF ~2.2 | Mathematical physics | ~6-12 months | Alfsen-Shultz related | MODERATE -- very mathematical audience |

### Recommendation: Quantum (quantum-journal.org)

**Why:**
1. It is now the primary venue for quantum reconstruction papers (vdW, BGW, Selby-Scandolo-Coecke all published there)
2. Open access with low APC (450 EUR) -- accessible to independent researchers
3. Strong foundations reviewer pool (the editors know this subfield)
4. Good impact factor (5.7) and growing prestige
5. arXiv overlay model matches existing workflow

**Backup:** Physical Review A if a broader physics audience is desired, or Foundations of Physics if a more philosophical framing is preferred.

## Paper Structure Best Practices

Based on analysis of successful reconstruction papers (Hardy 2001, CDP 2011, Dakic-Brukner 2011, Masanes-Mueller 2013, vdW 2019):

### Standard Structure for Reconstruction Papers

1. **Abstract** (~150 words): State the result ("we derive X from Y"), the method ("using Z framework"), and the key novelty ("this is the first single-premise reconstruction")
2. **Introduction** (2-3 pages): Motivate the problem (why reconstruct QM?), survey existing approaches (comparison table), state the main result informally, outline the paper structure
3. **Preliminaries** (1-2 pages): Define the framework (OUS, effect algebras, sequential products). Keep minimal -- cite references for standard material.
4. **The Self-Modeling Construction** (2-3 pages): THIS IS THE NOVEL CONTENT. Define self-modeling precisely. Construct the sequential product. State and prove the corrected formula.
5. **Axiom Verification** (2-3 pages): Verify S1-S7. S4 gets the most space (it's the hard one). Others can be sketched.
6. **From Jordan Algebra to C*-Algebra** (2-3 pages): Composite construction, local tomography proof, type exclusion, C*-promotion. Mix of novel arguments and theorem citations.
7. **Discussion** (1-2 pages): Comparison with other programs, load-bearing assumptions, relation to operational QM, future directions (infinite-dim, non-Markovian, etc.)
8. **Appendix** (optional): Full S1-S7 proofs if main text gives sketches; SymPy verification details.

### What Makes a Reconstruction Paper Impactful

Based on the success of Hardy, CDP, Dakic-Brukner, and Masanes-Mueller:

1. **Parsimony:** Fewer axioms = more impactful. This work has the fewest (1 premise).
2. **Physicality:** Axioms should have clear physical meaning, not be abstract mathematical conditions. "Self-modeling" is highly physical and intuitive.
3. **Completeness:** Must derive the full structure (complex numbers, involution, Born rule context) not just part of it.
4. **Transparency about assumptions:** Hidden assumptions destroy credibility. Flagging them builds trust.
5. **Clean comparison table:** Readers want to see at a glance how this work compares.

## Potential Reviewer Objections and Responses

### Objection 1: "The standing assumptions are doing the work, not the single premise"

**Anticipated form:** "You claim one premise, but finite-dimensionality, faithfulness, minimality, and simplicity are each non-trivial assumptions."

**Response strategy:** Distinguish between (a) the operational premise (self-modeling -- this is the physics content, the thing that selects QM over classical or other theories) and (b) structural assumptions (finite-dim, etc. -- these define the framework, analogous to how Hardy assumes finite-dim GPT). Every reconstruction program makes structural assumptions. The relevant comparison is: how many OPERATIONAL premises distinguish QM from the alternatives? We have one; Hardy has five; CDP has six.

### Objection 2: "What does 'self-modeling' mean physically?"

**Anticipated form:** "The premise is not as operationally clear as 'purification' or 'local tomography.' What physical setup corresponds to a self-model?"

**Response strategy:** A self-model is a subsystem M of a system B such that the evolution of M tracks the state of B. This is operationally definable: it means there exists a measurement protocol on M whose statistics reproduce those of any measurement on B. Concrete examples: a quantum system with a pointer basis, a measurement apparatus that faithfully registers the system's state. The self-modeling constraint is that this tracking is achieved by the system itself (M is part of B), not by an external observer.

### Objection 3: "The minimality assumption for the composite is doing non-trivial work"

**Anticipated form:** "You define V_BM as the minimal OUS satisfying your axioms. But the choice of minimal vs. maximal composite is a substantive physical assumption."

**Response strategy:** Acknowledge this honestly. Note that for complex QM, minimal = maximal (this is a theorem), so the assumption is vacuous for the derived theory. The assumption matters only in excluding non-complex alternatives, where minimal != maximal. This is analogous to how CDP's purification axiom excludes classical theory -- it is a meaningful physical choice, not a mathematical triviality. Frame the minimality assumption as: "the composite contains exactly the structure forced by the axioms and no more" -- a parsimony principle.

### Objection 4: "How does this relate to the Alfsen-Shultz program?"

**Anticipated form:** "Alfsen and Shultz characterized C*-algebra state spaces geometrically. How does your work differ?"

**Response strategy:** Alfsen-Shultz characterize WHICH state spaces are C*-algebraic (a mathematical classification). This work asks WHY a physical system should have a C*-algebraic state space (a physical derivation). The answer is: because it self-models. Alfsen-Shultz's results are part of the mathematical infrastructure (via Hanche-Olsen), but the physical content is different.

### Objection 5: "S4 proof relies on faithful self-modeling -- isn't this just assuming QM in disguise?"

**Anticipated form:** "Faithful self-modeling means phi is an isomorphism. But in quantum mechanics, isomorphisms are unitary maps. So aren't you assuming QM?"

**Response strategy:** phi is an OUS isomorphism (order-preserving, unit-preserving, bijective), not a unitary map. OUS isomorphisms exist in classical probability theory too (any permutation of outcomes). The QM-specific structure (unitarity, Hilbert space) EMERGES from the downstream theorems (vdW, Hanche-Olsen) -- it is not presupposed by phi. The circularity audit in the paper verifies this explicitly.

## Level of Rigor

**Required for this phase:** Publication-quality mathematical exposition. Proof sketches in the main text for non-trivial arguments; full proofs available (in appendix or supplementary material). All theorem invocations must verify every hypothesis explicitly.

**Justification:** This is a foundations paper making a strong claim (one-premise reconstruction). The standard of proof must be high enough that a referee specializing in quantum reconstruction cannot find logical gaps. However, full proofs of every step would make the paper too long; the standard practice (Hardy, CDP, Masanes-Mueller) is proof sketches in the main text with detailed arguments available.

**What this means concretely:**

- S4 proof: include the key idea (Peirce feedback + faithful tracking => orthogonality symmetry) with enough detail that a knowledgeable reader can verify it. Full computation in appendix.
- vdW Theorem 1 invocation: state the theorem, list the 7 verified axioms with one-line justifications, cite the theorem.
- LT proof: include the correlation form construction and non-degeneracy argument. The entangled-sector treatment can be condensed to a paragraph citing the full derivation.
- Type exclusion: the (n-1)^2 = 0 argument is clean enough to include in full. BGW citation for Albert.

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| --- | --- | --- | --- |
| Gudder-Greechie S4 | Van de Wetering S4 | 2018 (arXiv:1803.11139) | Different axiom formulation; must use vdW exclusively |
| Many-axiom reconstructions (5-6) | Fewer-axiom reconstructions (3-4) | 2011-2013 | Trend toward parsimony; this work continues the trend to 1 |
| Assuming local tomography | Deriving local tomography | 2014+ (Barnum-Mueller-Ududec, this work) | More powerful but harder |
| Jordan algebra program (pure math) | Jordan algebra + operational foundations | 2018+ (vdW) | Bridge between algebraic and operational approaches |

**Superseded approaches to avoid:**

- Hardy's Simplicity axiom: replaced by other mechanisms in all subsequent work.
- Gudder-Greechie axiom numbering: replaced by vdW's cleaner formulation.
- Treating the involution as a separate axiom: the whole point of this work is that it is derived.

## Open Questions

1. **How much proof detail in the main text vs. appendix?**
   - What we know: Reconstruction papers vary widely (Hardy gives full proofs; Masanes-Mueller gives sketches).
   - What's unclear: The optimal balance for this specific paper depends on venue page limits.
   - Impact on this phase: Determines the paper length (estimated 12-20 pages).
   - Recommendation: Main text gives proof sketches for all novel arguments. Full proofs for S4 and LT in an appendix. SymPy verification as supplementary material.

2. **Should the Barandes / Motzkin-Taussky downstream chain be included?**
   - What we know: The full chain goes L4 -> C*-algebra -> NC -> Artin-Wedderburn -> Skolem-Noether -> Barandes -> Born rule -> QM. But the C*-algebra result already gives QM (by the spectral theorem for C*-algebras).
   - What's unclear: Whether including the full downstream chain adds value or dilutes the main contribution.
   - Impact on this phase: Adds 1-2 pages if included.
   - Recommendation: Mention briefly in the Discussion section. The main theorem should stop at "C*-algebra with involution," which IS quantum mechanics. The downstream chain (automorphisms, Born rule) is well-established and doesn't need our help.

3. **Should figures be included?**
   - What we know: Some reconstruction papers include diagrams of the logical chain; most do not.
   - What's unclear: Whether a chain diagram adds clarity.
   - Impact on this phase: Minor (one figure).
   - Recommendation: Include one figure: a diagram of the derivation chain with the novel steps highlighted and the published theorem invocations labeled. This is useful for talks and for readers who want the big picture.

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| --- | --- | --- | --- |
| Quantum journal submission | Rejected by referees | Physical Review A or Foundations of Physics | ~1-2 weeks to reformat |
| Linear chain presentation | Paper too long (>20 pages) | Compress to theorem-first style; move proofs to appendix | ~1 week restructuring |
| One-premise framing | Referees reject premise count | Reframe as "minimal-assumption" reconstruction (still fewer than all competitors) | Cosmetic changes only |

**Decision criteria:** If three independent referee objections cite the same issue, address it substantively rather than arguing.

## Sources

### Primary (HIGH confidence)

- van de Wetering, "Sequential product spaces are Jordan algebras," J. Math. Phys. 60, 062201 (2019), arXiv:1803.11139 -- Central published theorems (Thm 1, Thm 3)
- Barnum and Wilce, "Local tomography and the Jordan structure of quantum theory," Found. Phys. 44, 192-212 (2014), arXiv:1202.4513 -- Type identification theorem
- Hanche-Olsen, "JB-algebras with tensor products are C*-algebras," LNM 1132, Springer (1985) -- Jordan-to-C* promotion
- Barnum, Graydon, Wilce, "Composites and categories of Euclidean Jordan algebras," Quantum 4, 359 (2020) -- Albert exclusion
- Hardy, "Quantum Theory From Five Reasonable Axioms," arXiv:quant-ph/0101012 (2001) -- First reconstruction; comparison baseline
- Chiribella, D'Ariano, Perinotti, "Informational derivation of quantum theory," Phys. Rev. A 84, 012311 (2011) -- CDP reconstruction; comparison
- Masanes, Mueller et al., "Existence of an information unit as a postulate of quantum theory," PNAS 110, 16373 (2013) -- Closest competitor in parsimony (3 axioms)

### Secondary (MEDIUM confidence)

- Mueller, "Probabilistic Theories and Reconstructions of Quantum Theory," SciPost Phys. Lect. Notes 28 (2021), arXiv:2011.01286 -- Review of reconstruction landscape
- Plavala, "General probabilistic theories: An introduction," Physics Reports 1033, 1-64 (2023), arXiv:2103.07469 -- GPT review; composite framework
- Dakic, Brukner, "Quantum Theory and Beyond: Is Entanglement Special?" arXiv:0911.0695 (2009) -- 4-axiom reconstruction; comparison
- Barnum, Mueller, Ududec, "Higher-order interference and single-system postulates characterizing quantum theory," NJP 16, 123029 (2014), arXiv:1403.4147 -- Single-system reconstruction; comparison
- Selby, Scandolo, Coecke, "Reconstructing quantum theory from diagrammatic postulates," Quantum 5, 445 (2021), arXiv:1802.00367 -- Categorical reconstruction; comparison
- van de Wetering, "An effect-theoretic reconstruction of quantum theory," Compositionality 1, 1 (2019), arXiv:1801.05798 -- Effectus theory reconstruction
- Defending the quantum reconstruction program, Eur. J. Phil. Sci. (2024), arXiv:2410.21152 -- Common objections and responses

### Tertiary (LOW confidence -- useful for context only)

- Irwin, Amaral, Chester, "The Self-Simulation Hypothesis," Entropy 22, 247 (2020) -- Different meaning of "self-modeling"; cite only to disambiguate
- Barandes, "The Stochastic-Quantum Correspondence," Phil. of Phys. 3(1) (2025), arXiv:2302.10778 -- Downstream application (optional citation)
- Alfsen, Shultz, "Geometry of State Spaces of Operator Algebras," Birkhauser (2003) -- Mathematical infrastructure

## Metadata

**Confidence breakdown:**

- Paper structure and presentation: HIGH -- well-established conventions in reconstruction papers
- Venue recommendation: HIGH -- clear fit with Quantum journal based on publication history
- Comparison with competitors: HIGH -- all major programs surveyed with axiom counts verified
- Anticipated reviewer objections: MEDIUM -- objections are based on general patterns; specific referees may raise unexpected issues
- Proof detail recommendations: MEDIUM -- depends on venue page limits and editorial preferences

**Research date:** 2026-03-21
**Valid until:** Indefinitely for the comparison landscape (reconstruction programs are stable); venue recommendations may shift with journal policy changes.

## Caveats and Self-Critique

1. **What assumption might be wrong?** The classification of "one premise" is the strongest claim and the most vulnerable. A skeptical referee might argue that "faithful self-modeling" is really two assumptions (self-modeling + faithfulness) or that the structural assumptions (finite-dim, simple EJA) are too constraining to be "standard framework." The paper must be prepared for this debate.

2. **What alternative approach did I dismiss too quickly?** The theorem-first presentation (Approach 2) might actually be better for high-impact venues like PNAS, where the abstract and first paragraph determine readership. For Quantum journal, the linear chain is standard, but it's worth reconsidering if PNAS is targeted.

3. **What limitation am I understating?** The finite-dimensional restriction. All the downstream theorems (vdW, Hanche-Olsen, Barnum-Wilce) are finite-dimensional. The extension to infinite dimensions (JB-algebras, von Neumann algebras) is non-trivial and the paper should acknowledge this as the most significant open extension.

4. **Is there a simpler method I overlooked?** No -- the method IS the result. The paper's contribution is the construction and verification, not an alternative proof technique.

5. **Would a specialist disagree?** A GPT specialist might object to the minimality assumption for composites (some prefer the maximal tensor product). A Jordan algebra specialist might want more detail on the Peirce decomposition arguments. An operational foundations person might want a more detailed physical interpretation of "self-modeling." These are addressable in revision.
