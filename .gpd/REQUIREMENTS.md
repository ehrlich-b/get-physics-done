# Requirements: The P5 <-> Basin Restriction Lemma (v15.0)

**Defined:** 2026-05-23
**Core Research Question:** Is "self-modeling -> QM -> h_3(O)" a genuine through-line, or are the observer's complex C* structure and the basin's octonionic structure independent posits? Concretely: prove or disprove RESTRICTION -- that the C*-bottleneck slice A = h_3(C_u) ~ M_3(C)^sa (reached by a positive unital conditional expectation E: h_3(O) -> A, lem:bottleneck / Effros-Stormer) satisfies Paper 5 Def 1 clause (iii), with the observer's body-model composite realized coherently as a sub-structure of the NON-composable h_3(O) induced by the Peirce/bottleneck restriction.

## Milestone Context

The whole Radical Relativity chain opens with two joins: "self-modeling -> QM" (Paper 5) and "QM lives in h_3(O)" (Paper 7). Paper 5 forces the observer COMPLEX via clause (iii), which needs a well-behaved composite to EXIST. Paper 7 selects the basin h_3(O) precisely because it is NON-composable (unique non-special simple FRJA; no Jordan-tensor composite in the BGW sense). The lemma reconciling these -- observer = a complex C*-subsystem reading the non-composable whole through a Peirce bottleneck (access by Peirce projection, NOT tensor factorization) -- has never been proved. This milestone proves or disproves it.

**A clean negative result (precisely-characterized structural obstruction) is a fully acceptable, valuable outcome.** Do NOT force a positive.

**Reward-hacking guard (central risk):** do NOT "prove" the claim by (1) redefining clause (iii) to be trivially satisfied; (2) conflating the observer's body-model composite with the BGW universe-tensoring; or (3) asserting the Peirce restriction preserves clause (iii) without demonstrating it on the actual non-associative h_3(O) structure. The two-composites distinction must be EARNED. Every phase's success criteria includes a circularity/conflation check.

**Pause condition:** the two composites collapse (claim circular), OR the coherent-embedding step needs structure NOT induced by E -> milestone pauses for human decision. A characterized obstruction is a deliverable, not a pause.

**Sources (LIVE, NOT the stale repo `papers/`):** Paper 5 Def 1 `~/repos/blog/landing/papers/qm-from-self-modeling/main.tex` (def:self-modeling-system line 342); lem:bottleneck + Peirce under E_11 `~/repos/blog/landing/papers/sm-from-self-modeling/sections/complexification.tex` (line 409). Inline definitions in `~/scratch/get-physics-done/p5-basin-restriction-prompt.md` are authoritative. rem:converse is prompt-inline; it is NOT yet a labeled remark in the live complexification.tex.

## Primary Requirements

### Phase 60 -- Two-Composites Distinction (rigorous, non-circular)

- [ ] **DERV-60-01**: State precisely, each in its own terms, the two composite notions: (a) the observer's clause-(iii) body-model composite V_BM (Paper 5 Def 1 -- minimal composite OUS carrying product states/effects, non-signaling, product-form sequential product); (b) the BGW Jordan-monoidal composite of the universe algebra h_3(O) with another system. Cite Paper 5 Def 1, BGW 2020, Hanche-Olsen.
- [ ] **DERV-60-02**: Prove that h_3(O)'s BGW non-composability does NOT entail non-existence of the observer's body-model composite V_BM -- the two are logically independent statements about different objects. Explicitly guard against the conflation; show the RESTRICTION claim does not become circular by assuming what it must prove.
- [ ] **DERV-60-03**: Confirm rem:converse against BGW: every M_n(C)^sa admits a faithful self-model (V_M = V_B = M_n(C)^sa, phi = id, composite M_{n^2}(C)^sa), and for complex matrix algebras the minimal and maximal composites COINCIDE, so clause (iii) is automatically satisfied. Verify the exact BGW statement that grounds "minimal = maximal for M_n(C)^sa"; flag that rem:converse is not yet in the live paper.
- [ ] **DERV-60-04**: Produce `derivations/p5-basin-restriction/claim.md` (RESTRICTION restated in the derivation's own notation, with allowed inputs and the three prohibited reward-hacking moves stated explicitly) and `derivations/p5-basin-restriction/STATE.md` (derivation-tree state).

### Phase 61 -- Slice Satisfies Clause (iii)

- [ ] **DERV-61-01**: Verify the slice A = h_3(C_u) ~ M_3(C)^sa satisfies Def 1 clause (i): finite-dimensional spectral order-unit space with at least two orthogonal nontrivial projective units.
- [ ] **DERV-61-02**: Verify clause (iv): A is simple -- no nontrivial direct-sum decomposition into order-unit subspaces.
- [ ] **DERV-61-03**: Instantiate rem:converse for M_3(C)^sa to supply clause (ii) (faithful tracking phi) and clause (iii) (minimal internal composite; minimal = maximal per BGW), confirming the product-form sequential product on A. Result: all four Def 1 clauses hold for A as a self-modeler in its own right.
- [ ] **VALD-61-01**: SymPy/matrix verification on M_3(C)^sa: rank 3, three mutually orthogonal rank-1 projective units summing to the unit, no nontrivial central idempotents (simplicity), and the composite dimension check dim(M_3(C)^sa (x) M_3(C)^sa) = dim(M_9(C)^sa) = 81.

### Phase 62 -- Coherent Embedding under E (the hard part -- where an obstruction would live)

- [ ] **DERV-62-01**: Set up the Peirce/bottleneck conditional expectation E: h_3(O) -> h_3(C_u) explicitly (Effros-Stormer): positive, unital, range = JB-subalgebra. State exactly what E preserves -- in particular whether it is coherent with the sequential product a&b = sqrt(a) b sqrt(a), not only the Jordan product.
- [ ] **DERV-62-02**: Determine whether the self-modeling data on A (its V_BM and its sequential product) is INDUCED by / consistent with the ambient h_3(O) Jordan structure under E -- demonstrated on the actual non-associative structure, NOT asserted. Treat the sequential product (CFC square roots in the non-associative ambient) explicitly.
- [ ] **DERV-62-03**: If preservation holds, state and prove the RESTRICTION embedding lemma. If it fails, characterize the obstruction precisely: name the exact structure clause (iii) needs that E cannot induce from the non-associative ambient, and what minimal extra input would be required.
- [ ] **VALD-62-01**: SymPy/matrix verification on h_3(O): construct E onto h_3(C_u) for a fixed u in S^6 (e.g. u = e_7), and test that sqrt(a) b sqrt(a) for a, b in the slice -- computed in the ambient h_3(O) -- lands back in the slice (preservation), or exhibit explicit leakage / a non-associativity obstruction.

### Phase 63 -- Verdict

- [ ] **DERV-63-01**: Assemble `derivations/p5-basin-restriction/RESULT.md`: either a clean RESTRICTION theorem (statement + proof, touching the actual non-associative structure) or a precisely-characterized obstruction, with the explicit consequence for the program (through-line real vs C and O independent posits) and what would have to change to close an obstruction.
- [ ] **DERV-63-02**: Adversarial fresh-eyes review of the verdict before RESULT.md finalizes, checking the three reward-hacking guards (no redefining clause iii; no conflating the two composites; no asserted preservation without demonstration on h_3(O)) and confirming a negative result was reported honestly rather than a positive forced.

### Milestone-Level Deliverables

- [ ] **DERV-00-01**: `derivations/p5-basin-restriction/attempt-NN.md` -- one per serious proof/obstruction attempt (numbered, most recent last); each states inputs used, the argument, and failure mode if any.
- [ ] **DERV-00-02**: Final verdict line in RESULT.md: RESTRICTION THEOREM (through-line) or CHARACTERIZED OBSTRUCTION (independent posits), with the one-sentence consequence for the Radical Relativity program.

## Follow-up Requirements

### Deferred (outcome-dependent or separate track)

- **FUTR-01**: If RESTRICTION proves TRUE -- draft ready-to-insert Paper 7 LaTeX (rem:converse remark + RESTRICTION lemma + proof) for `sm-from-self-modeling/sections/complexification.tex`. Outcome-dependent; out of scope this milestone.
- **FUTR-02**: Forced-vs-selected complexification (whether the observer's u in S^6 is forced or selected) -- downstream of this lemma; parked.
- **FUTR-03**: v14.0 Paper 5 JMP revision (paused pending referee report) -- separate track; resumes on referee report or explicit restart.
- **FUTR-04**: Carried from v13.0 -- close gap G6 (so(6) -> G_SM, Todorov-Drenska) and G7 (3 generations, Boyle triality).

## Out of Scope

| Topic | Reason |
| ----- | ------ |
| Anthropic "observer-grade" restriction | Conceded conditioning input (per milestone prompt) |
| Forced-vs-selected complexification | Downstream of THIS lemma; parked |
| Consciousness / Phi | Separate track |
| Ready-to-insert Paper 7 LaTeX integration | Verdict-only deliverable this milestone; outcome-dependent follow-up (FUTR-01) |
| Revisiting / re-deriving Paper 5 / Paper 6 / Paper 7 / v13.0 results | This milestone proves one new join; it does not re-open settled chain results |
| Redefining clause (iii), conflating the two composites, or asserting preservation without demonstration | Reward-hacking; the distinction and the embedding must be EARNED on the actual structure |
| Forcing a positive verdict | A clean obstruction is an acceptable, valuable outcome |
| Using the stale repo `papers/` copies | They predate the 2026-05-23 reframe; live sources in `~/repos/blog/landing/papers/` are authoritative |

## Accuracy and Validation Criteria

| Requirement | Accuracy Target | Validation Method |
| ----------- | --------------- | ----------------- |
| DERV-60-02 (two-composites) | Two notions defined distinctly; independence shown without circularity | Fresh-eyes check that non-composability of h_3(O) and existence of V_BM are independent facts about different objects |
| DERV-60-03 (rem:converse vs BGW) | Exact BGW statement located; "minimal = maximal for M_n(C)^sa" grounded | Cross-check against BGW 2020; flag rem:converse not-yet-in-paper |
| DERV-61-01..03 (slice clauses) | All four Def 1 clauses verified for M_3(C)^sa; no clause trivially redefined | Clause-by-clause check + VALD-61-01 SymPy |
| VALD-61-01 (slice SymPy) | rank 3, 3 orthogonal projective units, simple, composite dim 81 | `python` symbolic/numeric assertions; < 5 s runtime |
| DERV-62-02 (embedding) | Preservation demonstrated on actual non-associative h_3(O), or obstruction located -- never asserted | Sequential product computed in ambient h_3(O); VALD-62-01 |
| VALD-62-01 (embedding SymPy) | E onto h_3(C_u) constructed; sqrt(a) b sqrt(a) lands in slice (or leakage exhibited) | SymPy/NumPy on explicit octonion/h_3(O) matrices (reuse v8.0/v11.0 infra) |
| DERV-63-01 (verdict) | Decisive: theorem-with-proof OR precise obstruction + program consequence | Adversarial fresh-eyes review (DERV-63-02) |

## Contract Coverage

| Requirement | Decisive Output / Deliverable | Anchor / Benchmark / Reference | Prior Inputs / Baselines | False Progress To Reject |
| ----------- | ----------------------------- | ------------------------------ | ------------------------ | ------------------------ |
| DERV-60-02 | Non-circular two-composites distinction | BGW 2020; Paper 5 Def 1; Hanche-Olsen | Milestone prompt step 1 | "h_3(O) non-composable => observer has no composite" (conflation) |
| DERV-60-03 | rem:converse grounded in BGW | BGW 2020 (minimal=maximal for M_n(C)^sa) | Prompt rem:converse (inline) | Citing rem:converse as if already in the live paper |
| DERV-61-03 | Slice satisfies all 4 Def 1 clauses | Paper 5 Def 1; lem:bottleneck | rem:converse; M_3(C)^sa structure | Redefining clause (iii) to be trivially true |
| VALD-61-01 | SymPy slice verification | M_3(C)^sa standard structure | v8.0/v11.0 octonion infra | "Looks right" without explicit projective-unit/simplicity check |
| DERV-62-02 | Embedding demonstrated on h_3(O) | Effros-Stormer 1979; lem:bottleneck E | V_1 = R bottleneck (v6.0/v8.0); C*-observer SP closure (v11.0) | Asserting Peirce-restriction preserves clause (iii) without demonstrating on the non-associative ambient |
| DERV-62-03 | Preservation proof OR precise obstruction | Effros-Stormer; Hanche-Olsen | Sequential product sqrt(a) b sqrt(a) | Hand-waving "E preserves everything"; ignoring non-associativity |
| DERV-63-01 | RESULT.md verdict + consequence | Whole contract | All phase outputs | Forcing a positive; vague "mostly works" |

## Traceability

Which phases cover which requirements. Populated by roadmap.

| Requirement | Phase | Status |
| ----------- | ----- | ------ |
| DERV-60-01 | 60 | Pending |
| DERV-60-02 | 60 | Pending |
| DERV-60-03 | 60 | Pending |
| DERV-60-04 | 60 | Pending |
| DERV-61-01 | 61 | Pending |
| DERV-61-02 | 61 | Pending |
| DERV-61-03 | 61 | Pending |
| VALD-61-01 | 61 | Pending |
| DERV-62-01 | 62 | Pending |
| DERV-62-02 | 62 | Pending |
| DERV-62-03 | 62 | Pending (preservation OR obstruction) |
| VALD-62-01 | 62 | Pending |
| DERV-63-01 | 63 | Pending |
| DERV-63-02 | 63 | Pending |
| DERV-00-01 | 60-63 | Pending (attempt log) |
| DERV-00-02 | 63 | Pending (verdict line) |

**Coverage:**

- Primary requirements: 16 total
- Mapped to phases: 16 (Phase 60: 4, Phase 61: 4, Phase 62: 4, Phase 63: 2, Milestone-level: 2)
- Unmapped: 0

---

_Requirements defined: 2026-05-23_
_Last updated: 2026-05-23 after v15.0 milestone initialization_
