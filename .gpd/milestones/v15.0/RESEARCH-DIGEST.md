# Research Digest: v15.0 The P5 ↔ Basin Restriction Lemma

Generated: 2026-05-24
Milestone: v15.0
Phases: 60-63

## Narrative Arc

This milestone attacked the **spine** of the Radical Relativity program — the single load-bearing
join between Paper 5 ("self-modeling → QM": the observer is forced **complex** because it *has* a
well-behaved internal composite, Def 1 clause (iii)) and Paper 7 ("QM lives in h_3(O)": the basin is
forced **octonionic** precisely because the Albert algebra is **non-composable**). These two facts pull
in opposite directions, and the lemma reconciling them — observer = a complex C*-subsystem reading the
non-composable whole through a Peirce bottleneck (access by projection, **not** tensor factorization) —
had never been proved. If it failed, the observer's **C** and the basin's **O** would be two unconnected
posits and the through-line an illusion.

The attack was four strictly-sequential phases. **Phase 60** earned the *two-composites distinction*
non-circularly: the observer's clause-(iii) body-model composite V_BM (an OUS-level object) and h_3(O)'s
BGW Jordan-monoidal non-composability (an FRJA-monoidal-bifunctor property) are **type-distinct, logically
independent** statements about different objects — so the claim does not collapse into circularity at
step 1; and rem:converse was grounded against BGW 2020 (CONFIRMED-WITH-CAVEAT). **Phase 61** verified that
the C*-bottleneck slice A = h_3(C_u) ≅ M_3(C)^sa satisfies **all four** Paper 5 Def 1 clauses as a
self-modeler *in its own right*, with clause (iii) checked **as stated** (not redefined) and exact-symbolic
SymPy backing. **Phase 62** — the hard part — asked the decisive question on the **actual non-associative
h_3(O)**: does the bottleneck conditional expectation E transport the self-modeling sequential product
a&b = √a·b·√a coherently from the ambient? The exact computation returned the ambient transport residual
**R ≠ 0** (‖R‖² = 38593/72; decisive-triple associator 524/9 load-bearing on the same X,Y), i.e. an
**ambient-transport obstruction (O)**: E is the access/projection map, **not** a Jordan/SP morphism on the
ambient.

The pivotal interpretive move (Bryan, 2026-05-24): the prompt **over-specified** RESTRICTION. The
through-line needs only **coexistence-as-island** — the observer self-certifies its M_3(C)^sa QM on the
slice (Phase 61) and the slice *sits inside* h_3(O) as the range of E. Coherent ambient transport is a
**stronger, not-required** property. So the obstruction **refines** the through-line rather than refuting
it. **Phase 63** assembled this into RESULT.md, then a separate-wave adversarial fresh-eyes review confirmed
all three reward-hacking guards PASS against the real artifacts (review committed *before* finalization),
and the verdict was finalized: **CHARACTERIZED OBSTRUCTION refining RESTRICTION to coexistence-as-island —
the "self-modeling → QM → h_3(O)" through-line SURVIVES** (as the island through-line; NOT independent
posits, NOT a program collapse). A clean, honestly-reported obstruction was the contract-sanctioned
outcome (NEGATIVE-RESULT-IS-SUCCESS).

## Key Results

| Phase | Result | Equation / Value | Validity Range | Confidence |
| ----- | ------ | ---------------- | -------------- | ---------- |
| 60 | Two composites are type-distinct, logically independent | V_BM (OUS composite) ≠ BGW bifunctor on h_3(O); non-composability of h_3(O) ⇏ non-existence of V_BM | Categorical/structural (all n) | HIGH |
| 60 | rem:converse grounded vs BGW 2020 (CONFIRMED-WITH-CAVEAT) | M_n(C)^sa minimal composite M_{n²}(C)^sa satisfies clause (iii); minimal ≠ maximal (maximal = M_{n²}(C)^sa ⊕ M_{n²}(C)^sa, extra classical bit, BGW Thm 4.15/Cor 4.16) | M_n(C)^sa, all n | HIGH (BGW primary source) |
| 61 | Slice A = h_3(C_u) ≅ M_3(C)^sa satisfies all four Def 1 clauses intrinsically | (i) Jordan rank 3, three orthogonal projective units → I_3; (iv) simple (center = C·I_3); (ii)/(iii) via corrected direct-summand rem:converse | M_3(C)^sa | HIGH (exact SymPy, 21 tests) |
| 61 | Product-form sequential product factorizes on associative M_9(C)^sa | √a·b·√a = (a_B&b_B)⊗(a_M&b_M); composite real-dim 81 = 9·9 (maximal 162 ≠ 81) | M_9(C)^sa (associative slice) | HIGH (full 9×9, not assumed-from-Lüders) |
| 62 | **Ambient E-transport obstruction (O)** — DECISIVE | R = E(√X·Y·√X) − √(EX)·(EY)·√(EX) ≠ 0 (exact); ‖R‖² = 38593/72; R_11 = −2 | Generic ambient X (PSD), Y ∈ h_3(O) | HIGH (exact SymPy, 2 routes agree) |
| 62 | Non-associativity is load-bearing on the same triple | associator ‖(√X·Y)√X − √X(Y·√X)‖² = 524/9 ≠ 0; E not a Jordan morphism on ambient (‖E(X∘X)−(EX)∘(EX)‖² = 3797527/34560000) | same X,Y | HIGH |
| 62 | Defect partitions exactly across E_11 Peirce grades | 4 + 1033/18 + 3797/8 = 38593/72 (LCD-72: 288 + 4132 + 34173 = 38593) | C_u defect (e0,e7) | HIGH (independent Peirce route) |
| 62 | Slice-internal control is trivial (non-rigged test) | a,b ∈ A: leakage 0, associator 0, R = 0 — proves the test CAN yield (P) | closed associative slice | HIGH |
| 63 | Milestone verdict FINALIZED | CHARACTERIZED OBSTRUCTION refining RESTRICTION to coexistence-as-island; through-line SURVIVES | whole program | HIGH (verifier 4/4, consistency CONSISTENT, human-approved) |

Source: phase SUMMARY.md `key-results` + `derivations/p5-basin-restriction/RESULT.md`. (state.json `intermediate_results` for v15.0 are the deliverable files, not numeric entries.)

## Methods Employed

- **Phase 60:** category-separation independence argument (pure-math); type-consistency audit as the dimensional-analysis analog; literature-grounding of a prompt-inline result against an exact cited primary source (BGW 2020).
- **Phase 61:** clause-by-clause Def-1 verification with intrinsic (direct) vs relational (rem:converse) split; exact n×n positive matrix square root via SymPy spectral decomposition + Gram-Schmidt; exact-symbolic commutant computation via `linsolve` for center/simplicity.
- **Phase 62:** explicit entrywise C_u-projection conditional expectation on h_3(O); Jordan-morphism-on-ambient diagnostic E(X∘X) vs (EX)∘(EX); ambient-transport residual R as the decisive SP-coherence object; exact-square trick X = C² for exact ambient √X; exact-SymPy octonion arithmetic (Fano e1e2=e4) ported from float64 octonion_algebra.py; non-associative 3×3 octonionic matrix triple product by independent left/right association; independent positional-Peirce/grade cross-check route.
- **Phase 63:** milestone verdict assembly from a settled verified computation (restate-verbatim, no re-derivation); fresh-eyes adversarial guard review against named real artifacts in a separate wave; backtracking-trigger finalization gate (review-precedes-finalization ordering); stale-requirement-text reconciliation against a corrected governing authority (negated/marked-superseded quotation only).

## Convention Evolution

The milestone is pure algebra; the numerical/field conventions are inherited and stable. The two
*semantic* convention changes that matter downstream:

| Date / Phase | Convention | Description | Status |
| ------------ | ---------- | ----------- | ------ |
| Phase 60-02 | rem:converse statement | CORRECTED from "minimal = maximal composites COINCIDE" to **"minimal ≠ maximal; minimality SELECTS the standard direct summand"** (BGW Thm 4.15/Cor 4.16, extra classical bit) | Active (supersedes pre-Phase-60 phrasing) |
| Phase 62-03 | RESTRICTION semantics | Embedding clause weakened to **coexistence-as-island**; clause (iii) itself UNCHANGED (verbatim). Ambient E-transport = stronger, not-required property; its failure REFINES (does not refute) RESTRICTION | Active (supersedes prompt over-specification) |
| (stable) | Slice | A = h_3(C_u) ≅ M_3(C)^sa (maximal C*-target inside h_3(O); single F_4-orbit) | Active |
| (stable) | E | entrywise C_u-projection, u = e_7 (any u ∈ S^6 equivalent under G_2) | Active |
| (stable) | Sequential product | a&b = √a·b·√a (Lüders / self-modeling, temporally asymmetric) | Active |
| (stable) | Octonion | Fano e_1 e_2 = e_4 (matches Paper 7); Cl(9,0) positive-definite | Active |

Full catalog: `.gpd/CONVENTIONS.md`. No convention was introduced that conflicts with prior milestones.

## Figures and Data Registry

No plots (pure-algebra milestone). Computational artifacts and derivation documents:

| File | Phase | Description | Paper-ready? |
| ---- | ----- | ----------- | ------------ |
| `code/slice_clause_iii_verification.py` | 61 | Exact-symbolic M_3(C)^sa: rank 3, orthogonal projective units, simplicity, composite dim 81 vs 162, product-form SP factorization | Yes (verification appendix) |
| `tests/test_slice_clause_iii.py` | 61 | 21 assert-based tests for VALD-61-01 (runtime <1s) | Yes |
| `code/embedding_under_E_verification.py` | 62 | Exact-SymPy octonion h_3(O) arithmetic; E construction; ambient transport residual R; associator; Peirce-grade partition | Yes (decisive computation) |
| `tests/test_embedding_under_E.py` | 62 | Assert-based harness (no pytest): exit 0, verdict (O), is_zero_exact=[False,False], anti-loophole assertions | Yes |
| `derivations/p5-basin-restriction/RESULT.md` | 63 | FINALIZED verdict (CHARACTERIZED OBSTRUCTION, coexistence-as-island) + program consequence + §7 minimal-extra-input | Yes (the deliverable) |
| `derivations/p5-basin-restriction/claim.md` | 60-62 | RESTRICTION restated; reward-hacking guards; corrected coexistence-as-island framing (provenance preserved) | Reference |
| `derivations/p5-basin-restriction/two-composites.md` | 60 | The type-distinct V_BM vs BGW-composite distinction | Reference |
| `derivations/p5-basin-restriction/rem-converse-bgw.md` | 60 | rem:converse grounded vs BGW 2020 (direct-summand correction) | Reference |
| `derivations/p5-basin-restriction/slice-clause-iii.md` | 61 | Clause-by-clause Def-1 verification for M_3(C)^sa | Reference |
| `derivations/p5-basin-restriction/embedding-under-E.md` | 62 | §1-§5: E setup → decisive computation → verdict (O) → coexistence-as-island | Reference (the core argument) |
| `derivations/p5-basin-restriction/attempt-01..05.md` | 60-63 | Contiguous attempt log (DERV-00-01), coverage-audited | Reference |
| `derivations/p5-basin-restriction/STATE.md` | 60-63 | Derivation-tree state (FINALIZED) | Reference |

## Open Questions

1. **Hanche-Olsen induced-vs-imported "minimal extra input"** (RESULT.md §7): the precise extra structure the *stronger* ambient-transport property would require. The least-certain part; stated as precisely as the evidence allows, flagged, NOT inflating the claim. **Coexistence-as-island does not require it.** Carried to future work, not a blocker.
2. **Downstream paper integration:** whether/how to fold the coexistence-as-island through-line into Paper 5 / Paper 7 (rem:converse remark + the island framing). Note: FUTR-01 (ready-to-insert Paper 7 LaTeX for a *positive* RESTRICTION lemma) was NOT triggered — the outcome was an obstruction, not a clean positive theorem.
3. **FUTR-02** (parked): forced-vs-selected complexification (is the observer's u ∈ S^6 forced or selected?) — downstream of this lemma.
4. **Deferred to v16.0+:** gap G6 (so(6) → G_SM, Todorov–Drenska F_4–Spin(9) intersection); gap G7 (3 generations, Boyle triality); Λ ≠ 0 mechanism (ungauged MESGT gives Λ=0 classically).
5. **v14.0 (PAUSED):** Paper 5 JMP revision (JMP26-AR-00922) — resumes on referee report or explicit restart; see `.gpd/V14-CLOSEOUT.md`. Independent track.

## Dependency Graph

The chain is strictly linear — a single load-bearing argument, not independent work streams.

    Phase 60 "Two-Composites Distinction"
      provides: V_BM ≠ BGW-composite (type-distinct, independent); rem:converse grounded (direct-summand); claim.md + STATE.md
      requires: Paper 5 Def 1; BGW 2020; Hanche-Olsen
    → Phase 61 "Slice Satisfies Clause (iii)"
      provides: A = M_3(C)^sa satisfies all four Def 1 clauses intrinsically (clause iii verbatim); SymPy (rank 3, simple, dim 81 vs 162); SP factorizes on associative M_9(C)^sa
      requires: Phase 60 distinction + grounded rem:converse
    → Phase 62 "Coherent Embedding under E (the hard part)"
      provides: VERDICT (O) ambient-transport obstruction — exact R ≠ 0 (‖R‖²=38593/72), associator 524/9 load-bearing; E = access/projection map not a morphism; coexistence-as-island reframe
      requires: Phase 61 (slice is a self-modeler)
    → Phase 63 "Verdict"
      provides: FINALIZED milestone verdict — CHARACTERIZED OBSTRUCTION refining RESTRICTION to coexistence-as-island (through-line survives); 3/3 guards PASS; attempt-01..05 complete
      requires: Phase 62 (O) verdict + decisive harness

## Mapping to Original Objectives

| Requirement | Status | Fulfilled by | Key Result |
| ----------- | ------ | ------------ | ---------- |
| DERV-60-01..04 (two-composites distinction + workspace) | Complete | Phase 60 | V_BM ≠ BGW-composite earned non-circularly; claim.md + STATE.md initialized |
| DERV-60-03 (rem:converse vs BGW) | Complete (corrected) | Phase 60-02 | CONFIRMED-WITH-CAVEAT: minimal ≠ maximal (direct summand), not "coincide" |
| DERV-61-01..03, VALD-61-01 (slice clauses + SymPy) | Complete | Phase 61 | All four Def 1 clauses for M_3(C)^sa intrinsically; 21 exact tests |
| DERV-62-01..03, VALD-62-01 (coherent embedding) | Complete | Phase 62 | OBSTRUCTION (O) demonstrated on real h_3(O): R ≠ 0, associator 524/9 load-bearing |
| DERV-63-01..02 (verdict + adversarial review) | Complete | Phase 63 | RESULT.md FINALIZED; 3/3 reward-hacking guards PASS; honest-negative |
| DERV-00-01 (attempt log) | Complete | Phases 60-63 | attempt-01..05 contiguous, coverage-audited |
| DERV-00-02 (verdict line) | Complete | Phase 63 | CHARACTERIZED OBSTRUCTION refining RESTRICTION to coexistence-as-island; through-line SURVIVES |

**Core research question** — "Is 'self-modeling → QM → h_3(O)' a genuine through-line, or are the
observer's complex C* structure and the basin's octonionic structure independent posits?" —
**ANSWERED: a genuine through-line, in the coexistence-as-island form.** The observer is a self-contained
C* island self-certifying its M_3(C)^sa QM on the slice A = h_3(C_u), which sits inside the non-composable
h_3(O) as the range of the projection E. The ambient-transport obstruction (E is not a Jordan/SP morphism
on the non-associative whole) **refines** this through-line; it does **not** establish independent posits.

---

_Generated at v15.0 milestone completion. Primary handoff artifact for any downstream paper integration
(see Open Questions #2; FUTR-01 not triggered — outcome was an obstruction, not a clean positive theorem)._
