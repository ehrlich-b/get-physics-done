---
phase: 60-two-composites-distinction
plan: 01
depth: full
one-liner: "Proved non-circularly that the observer's clause-(iii) body-model composite V_BM (an OUS-level object) and h_3(O)'s BGW Jordan-monoidal non-composability (an FRJA-monoidal-bifunctor property) are type-distinct, logically independent objects — RESTRICTION does not collapse into circularity; distinction EARNED, no PAUSE"
subsystem: [formalism, derivation]
tags: [jordan-algebra, formally-real-jordan-algebra, order-unit-space, h3O, BGW-composability, self-modeling, local-tomography, non-circularity, type-consistency]

requires:
  - phase: "Paper 5 (qm-from-self-modeling)"
    provides: "Def 1 (self-modeling system), clause (iii) sms:minimal, composable/non-composable scoping remark"
  - phase: "Paper 7 (sm-from-self-modeling)"
    provides: "lem:bottleneck (C*-bottleneck universality: A = h_3(C_u) ~ M_3(C)^sa inside h_3(O))"
provides:
  - "Type-distinct definitions of V_BM (OUS internal composite) and the BGW composite of h_3(O) (bifunctor on FRJA-Sys)"
  - "Non-circular proof that P_BGW (h_3(O) non-composable) does NOT entail not-exists(V_BM)"
  - "Initialized p5-basin-restriction derivation workspace (claim.md, STATE.md, attempt-01.md)"
  - "Categories ledger (type-consistency analog of dimensional analysis) for downstream phases"
affects: ["Phase 61 (slice satisfies clause iii)", "Phase 62 (coherent embedding under E)", "Phase 63 (verdict)", "plan 60-02 (confirm rem:converse against BGW)"]

methods:
  added: ["category-separation independence argument (pure-math)", "type-consistency audit as dimensional-analysis analog"]
  patterns: ["every named object tagged OUS | FRJA | monoidal-composite | conditional-expectation; no inference equates objects of different categories"]

key-files:
  created:
    - derivations/p5-basin-restriction/two-composites.md
    - derivations/p5-basin-restriction/claim.md
    - derivations/p5-basin-restriction/STATE.md
    - derivations/p5-basin-restriction/attempt-01.md
  modified: []

key-decisions:
  - "Independence established from category separation + Paper 5's own composable/non-composable scoping remark, NEVER from RESTRICTION/embedding/slice-clause-(iii)-satisfaction (non-circular by construction)"
  - "Existence direction (M_n(C)^sa has its own V_BM; M_3(C)^sa sits inside h_3(O)) stated PRINCIPLE-ONLY; does NOT assert the slice satisfies clause (iii) — that is deferred to Phase 61/62"
  - "rem:converse treated as prompt-inline authoritative ONLY (grep of live complexification.tex: 0 matches); BGW confirmation deferred to plan 60-02"
  - "Clause (iii) reproduced verbatim with all four carried data + minimality; not weakened"

patterns-established:
  - "Categories ledger: type-consistency is the pure-math analog of dimensional analysis for this milestone"
  - "Honest-negative branch wired into every distinction claim: collapse -> DECISIVE NEGATIVE -> PAUSE"

conventions:
  - "pure algebra; no field theory / no numerics this plan"
  - "Jordan product a o b = (1/2)(ab+ba); sequential product a&b = sqrt(a) b sqrt(a) (Luders, temporally asymmetric)"
  - "Peirce eigenvalues {0, 1/2, 1}; complex structure u in S^6 (u=e_7 default, G_2-equivalent)"
  - "LIVE papers only (~/repos/blog/landing/papers/), NOT stale repo papers/"

plan_contract_ref: ".gpd/phases/60-two-composites-distinction/60-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-two-composites:
      status: partial
      summary: "Proved V_BM (OUS internal composite) and h_3(O)'s BGW non-composability (FRJA-monoidal bifunctor property) are type-distinct, logically independent objects: P_BGW does NOT entail not-exists(V_BM). Argument is non-circular (category separation + Paper 5 scoping remark; RESTRICTION/E/slice-satisfaction used nowhere as premise). Self-audited PASS. Marked partial because the decisive gate test-two-composites is human_review (fresh-eyes), pending."
      linked_ids: [deliv-two-composites, test-two-composites, test-type-consistency, ref-paper5-def1, ref-bgw, ref-hanche-olsen]
      evidence:
        - verifier: gpd-executor
          method: type-consistency audit + non-circularity grep-audit
          confidence: high
          claim_id: claim-two-composites
          deliverable_id: deliv-two-composites
          acceptance_test_id: test-type-consistency
          reference_id: ref-paper5-def1
          evidence_path: "derivations/p5-basin-restriction/two-composites.md"
  deliverables:
    deliv-two-composites:
      status: passed
      path: derivations/p5-basin-restriction/
      summary: "Workspace initialized with all four required files. two-composites.md: two type-distinct definition blocks (V_BM in its own terms; BGW composite in its own terms) + Categories ledger + Independence argument. claim.md, STATE.md, attempt-01.md present. All must_contain items satisfied."
      linked_ids: [claim-two-composites, test-two-composites, test-type-consistency]
  acceptance_tests:
    test-two-composites:
      status: partial
      summary: "Executor-side argument complete: both composite notions defined precisely each in its own terms; independence shown without smuggling in RESTRICTION (circularity guard explicit, grep-audited). Decisive pass_condition is a FRESH-EYES human/verifier review confirming the distinction is earned and non-circular — that review is pending (handed to L5 verifier / human). No collapse found on executor inspection."
      linked_ids: [claim-two-composites, deliv-two-composites, ref-paper5-def1, ref-bgw]
    test-type-consistency:
      status: passed
      summary: "Type/structural-consistency audit performed: every load-bearing object tagged by category (OUS | FRJA | monoidal-composite | conditional-expectation); no sentence equates an OUS-level proposition (exists V_BM) with an FRJA-monoidal-level proposition (h_3(O) composable). Clause (iii) verified verbatim against main.tex lines 351-353 (grep-confirmed). Self-audit tables included in both definition and independence sections."
      linked_ids: [claim-two-composites, deliv-two-composites, ref-paper5-def1]
  references:
    ref-paper5-def1:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Read Paper 5 Def 1 (main.tex line 342) and the composable/non-composable scoping remark (lines 397-401, 165-168) directly from the LIVE paper. Clause (iii) reproduced verbatim. The scoping remark is the textual witness (independence argument step (b)) that the two composite notions are distinct regimes."
    ref-bgw:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Used BGW 2020 to define the Jordan-monoidal composite as a bifunctor on FRJA-Sys and to pin h_3(O) as the unique non-special simple FRJA admitting no well-behaved composite (universe-tensoring). Full independent confirmation of BGW's notion vs rem:converse deferred to plan 60-02 (weakest anchor)."
    ref-hanche-olsen:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Used Hanche-Olsen (universal tensor product; special vs exceptional) to clarify that 'has a minimal internal composite as an OUS self-modeler' (V_BM) and 'admits a universal Jordan tensor product' (BGW) are distinct properties, supporting non-circular separation."
  forbidden_proxies:
    fp-conflate-composites:
      status: rejected
      notes: "Central reward-hacking risk. Actively rejected: the entire Independence argument proves V_BM and the BGW universe-composite are type-distinct objects and that non-composability(h_3(O)) does NOT entail not-exists(V_BM). No sentence treats them as the same fact. Collapse condition (e) is explicitly checked and NOT triggered."
    fp-converse-already-in-paper:
      status: rejected
      notes: "Actively rejected: grep of live complexification.tex finds lem:bottleneck (line 409) but ZERO matches for rem:converse. rem:converse is flagged throughout as prompt-inline authoritative / to-be-produced, never cited as labeled/published. BGW confirmation deferred to plan 60-02."
  uncertainty_markers:
    weakest_anchors:
      - "The composable/non-composable separation rests on Paper 5's own remark + BGW; if BGW's notion of 'composite' and Paper 5's clause-(iii) 'minimal internal composite' turn out to be the SAME construction, the distinction collapses (the disconfirming case). The type-level independence (steps a+b) is robust to this; the existence direction (step c) inherits the rem:converse provenance caveat."
      - "rem:converse is prompt-authoritative but not yet labeled in the live complexification.tex; the V_BM-for-M_n(C)^sa picture used to MOTIVATE (not prove) the distinction inherits that provenance caveat (full BGW confirmation deferred to plan 60-02)."
    unvalidated_assumptions:
      - "Existence direction (c) uses rem:converse as a PRINCIPLE (M_n(C)^sa has its own V_BM with minimal=maximal composite). Confirmed against BGW only in plan 60-02. The type-level independence (a)+(b) does not depend on it."
    competing_explanations: []
    disconfirming_observations:
      - "On close inspection the observer's V_BM and the BGW universe-composite are revealed to be one and the same object/construction -> RESTRICTION circular -> PAUSE (milestone pause condition 1). NOT observed this plan."
      - "The independence argument cannot be made without invoking RESTRICTION itself (latent circularity) -> distinction cannot be earned -> PAUSE. NOT observed this plan."

duration: 5min
completed: 2026-05-23
---

# Phase 60 Plan 01: Two-Composites Distinction Summary

**Proved non-circularly that the observer's clause-(iii) body-model composite V_BM (an order-unit-space object) and h_3(O)'s BGW Jordan-monoidal non-composability (a bifunctor/monoidal-structure property of the universe FRJA) are type-distinct, logically independent objects — so the downstream RESTRICTION claim does not presuppose its own conclusion. The distinction is EARNED from category separation plus Paper 5's own composable/non-composable scoping remark, never from RESTRICTION. No collapse; no PAUSE triggered.**

## Performance

- **Duration:** 5 min
- **Started:** 2026-05-23T21:33:36Z
- **Completed:** 2026-05-23T21:39:08Z
- **Tasks:** 2
- **Files modified:** 4 (all created)

## Key Results

1. **The two composites are objects in different categories.**
   - `V_BM` (clause iii / `sms:minimal`): the observer's **minimal internal composite OUS**, carrying product states, product effects, non-signaling constraints, and a product-form sequential product. **Category: order-unit space.**
   - The **BGW composite** of `h_3(O)`: a **bifunctor** `⊠ : FRJA-Sys × FRJA-Sys -> FRJA-Sys` (tensoring the *whole* universe algebra with an *external* FRJA system); `h_3(O)` is the unique non-special simple FRJA and admits no well-behaved such composite (universe-tensoring). **Category: monoidal-composite / bifunctor.**

2. **Logical independence, non-circular.** `P_BGW` ("h_3(O) is BGW-non-composable") does **NOT** entail `¬P_VBM` ("the observer has no V_BM"). The only type-correct bridge premise that would force the entailment *is* RESTRICTION — which is forbidden as a premise. Independence is established from (a) category separation + (b) Paper 5's own scoping remark, with (c) the existence direction at the level of principle only.

3. **No collapse, no PAUSE.** The honest-negative branch (collapse → DECISIVE NEGATIVE → PAUSE) was wired and checked; it did **not** trigger. The distinction is EARNED.

## Task Commits

1. **Task 1: State both composite notions precisely and independently (DERV-60-01)** — `ee63cdf6` (docs)
2. **Task 2: Prove independence non-circularly + claim.md/STATE.md/attempt-01.md (DERV-60-02, DERV-60-04)** — `b011ebce` (docs)

**Plan metadata:** (this commit)

## Files Created/Modified

- `derivations/p5-basin-restriction/two-composites.md` — Two type-distinct definition blocks (V_BM; BGW composite), Categories ledger, and the Independence argument (category separation + textual witness + principle-level existence + circularity guard + honest-negative branch).
- `derivations/p5-basin-restriction/claim.md` — RESTRICTION restated in derivation notation; allowed inputs; the 3+1 prohibited reward-hacking moves; PAUSE conditions.
- `derivations/p5-basin-restriction/STATE.md` — Derivation-tree state: 4-step attack (60/61/62/63), Phase 60 step 1 IN PROGRESS, steps 2-4 PENDING; verdict UNDECIDED. (This is the workspace deliverable, NOT the project .gpd/STATE.md.)
- `derivations/p5-basin-restriction/attempt-01.md` — Attempt log: inputs used, the category-separation argument, outcome (distinction earned, clean).

## Next Phase Readiness

- **Distinction earned:** RESTRICTION does not collapse into circularity at step 1. The "self-modeling -> QM -> h_3(O)" through-line survives the first load-bearing test.
- **Ready for plan 60-02:** confirm `rem:converse` exactly against BGW (does minimal = maximal composite coincide for `M_n(C)^sa`, so clause (iii) is auto-satisfied for the slice?). This retires the principal provenance caveat.
- **Then Phase 61:** verify the slice `h_3(C_u) ≅ M_3(C)^sa` satisfies clauses (i) [spectral, ≥2 orthogonal projective units] and (iv) [simple] in its own right.
- **The hard part (Phase 62) remains entirely open:** does restricting through the bottleneck `E` preserve what clause (iii) needs on the non-associative `h_3(O)` — in particular for the sequential product `a&b = sqrt(a) b sqrt(a)`, not just the Jordan product?

## Contract Coverage

- **Claim IDs advanced:** `claim-two-composites` -> partial (executor argument complete + self-audited PASS; decisive human_review pending)
- **Deliverable IDs produced:** `deliv-two-composites` -> passed (all 4 files + all must_contain items present at `derivations/p5-basin-restriction/`)
- **Acceptance test IDs run:** `test-type-consistency` -> passed; `test-two-composites` -> partial (fresh-eyes human/verifier review pending)
- **Reference IDs surfaced:** `ref-paper5-def1` -> read+cite; `ref-bgw` -> read+cite; `ref-hanche-olsen` -> read+cite
- **Forbidden proxies rejected:** `fp-conflate-composites` -> rejected; `fp-converse-already-in-paper` -> rejected
- **Decisive comparison verdicts:** none required (pure-proof plan; no numerical/benchmark comparison this phase — SymPy verification of the slice lands in Phase 61)

## Equations Derived

This is a pure-proof / definitional plan; the "equations" are definitional and logical statements rather than computed expressions.

**Statement (60.1) — Clause (iii), verbatim (Paper 5 `sms:minimal`):**

$$
V_{BM}\ \text{is the minimal composite OUS carrying product states, product effects, non-signaling constraints, and product-form sequential product.}
$$

**Statement (60.2) — BGW composite as a bifunctor:**

$$
\boxtimes : \mathbf{FRJA\text{-}Sys} \times \mathbf{FRJA\text{-}Sys} \longrightarrow \mathbf{FRJA\text{-}Sys}, \qquad h_3(\mathbb{O})\ \text{admits no well-behaved}\ \boxtimes\ \text{(non-composability / universe-tensoring).}
$$

**Statement (60.3) — Independence (the result):**

$$
P_{\mathrm{BGW}}\ \big(h_3(\mathbb{O})\ \text{BGW-non-composable}\big) \ \nvdash\ \neg P_{V_{BM}}\ \big(\exists\, V_{BM}\big),
$$

established from category separation + Paper 5's scoping remark, with the existence direction at the level of principle only — **without invoking RESTRICTION, the conditional expectation $E$, or clause-(iii)-satisfaction-on-the-slice.**

## Validations Completed

- **Type/category consistency (dimensional-analysis analog):** every named object tagged OUS | FRJA | monoidal-composite | conditional-expectation; self-audit tables in both the definition and independence sections confirm no inference equates objects of different categories. PASS.
- **Clause (iii) verbatim check:** my reproduction matches `main.tex` lines 351-353 exactly (grep-confirmed); all four carried data + minimality present; not weakened. PASS.
- **Non-circularity grep-audit:** every occurrence of "RESTRICTION", "coherent-embedding", and the conditional expectation "E" in the Independence section is framing prose, the forbidden-list, the named-and-rejected CIRCULAR route (guard d), or the collapse/PAUSE branch (e) — **none is a load-bearing premise.** PASS.
- **Provenance check:** `grep "rem:converse"` on live `complexification.tex` returns **0 matches**; `lem:bottleneck` present at line 409. rem:converse correctly flagged prompt-inline, not published. PASS.
- **Honest-negative branch present:** collapse → DECISIVE NEGATIVE → PAUSE wired in both `two-composites.md` (e) and `attempt-01.md`; checked and NOT triggered. PASS.

## Decisions Made

- **Independence proved via category separation + Paper 5's own scoping remark**, with the existence direction (M_n(C)^sa self-model, slice-inside-h_3(O)) supplied PRINCIPLE-ONLY. Rationale: this is the unique route that does not require RESTRICTION as a premise, so the distinction is earned rather than assumed.
- **rem:converse used only as a principle, never as published provenance.** Rationale: it is genuinely absent from the live paper; treating it as published would fake provenance (fp-converse-already-in-paper). Confirmation against BGW is deferred to plan 60-02.
- **Existence direction deliberately does not assert the slice satisfies clause (iii).** Rationale: that is the coherent-embedding/clause-checking work of Phases 61-62; pre-empting it here would import the conclusion (assert-Peirce-preserves-iii) and re-introduce circularity.

## Deviations from Plan

None — plan executed exactly as written. Both tasks completed in order; all required deliverables and `must_contain` items produced; all `<verify>` checks for both tasks passed.

## Issues Encountered

None. The central risk (the two composites collapsing into one object) was actively checked and did not materialize — the type distinction is genuine (internal OUS composite of the observer's body+model vs external monoidal bifunctor on the whole universe algebra) and is independently witnessed by Paper 5's own regime split.

## Open Questions

- **[plan 60-02]** Does `rem:converse` hold exactly as stated against BGW — minimal = maximal composite coincide for `M_n(C)^sa`, so clause (iii) auto-satisfied for the slice? (Prompt-authoritative; not yet in live paper. Principal provenance caveat carried by this plan.)
- **[Phase 61]** Does `h_3(C_u) ≅ M_3(C)^sa` satisfy clauses (i) [spectral, ≥2 orthogonal projective units] and (iv) [simple] in its own right? (rem:converse targets (ii)-(iii).)
- **[Phase 62, the hard part]** Does restricting through the bottleneck `E` preserve what clause (iii) needs on the actual non-associative `h_3(O)` structure — especially for the sequential product `a&b = sqrt(a) b sqrt(a)`, not just the Jordan product — or is there an obstruction (PAUSE condition 2)?
- **[Phase 63]** VERDICT: clean RESTRICTION theorem (through-line real) or precisely-characterized obstruction (C and O independent posits)?

## Self-Check: PASSED

- All 5 deliverable files exist on disk.
- Both task checkpoints (`ee63cdf6`, `b011ebce`) present in git log.
- Convention consistency: ONE convention block across all derivation files (no drift).
- `gpd validate summary-contract`: valid (no missing fields, no errors).
- Contract coverage: all contract IDs (1 claim, 1 deliverable, 2 acceptance tests, 3 references, 2 forbidden proxies) have explicit `contract_results` entries.

## Validation: PASSED

Domain final verification (mathematical physics — the type-consistency analog of dimensional analysis):
- **Type-distinctness (integer-invariant analog):** every object carries exactly one category tag; the OUS-level `V_BM` and the FRJA-monoidal-level BGW composite are never identified or contraposed. PASS.
- **Non-circularity (anomaly-cancellation / 't Hooft-matching analog):** the independence argument's premises (category separation + Paper 5 scoping remark) are decoupled from the conclusion (RESTRICTION); no premise imports RESTRICTION/E/slice-satisfaction. grep-audited. PASS.
- **Definitional faithfulness:** clause (iii) reproduced verbatim against the live source (lines 351-353). PASS.
- **Honest-negative integrity:** collapse → PAUSE branch present and checked (not triggered). PASS.

---

_Phase: 60-two-composites-distinction_
_Completed: 2026-05-23_
