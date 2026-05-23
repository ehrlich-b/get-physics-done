<!-- ASSERT_CONVENTION: metric_signature=riemannian_fisher, fourier_convention=na, natural_units=natural, gauge_choice=na, renormalization_scheme=na -->
<!-- Attempt log (DERV-00-01, Phase 60 slice). Provenance: LIVE papers only. -->

# attempt-01.md — Phase 60 attempt (DERV-00-01 slice)

**Plan:** 60-01 (Phase 60, milestone v15.0)
**Attempt:** 01
**Step attacked:** Step 1 of 4 — the two-composites distinction (does the observer's
clause-(iii) `V_BM` differ, non-circularly, from `h_3(O)`'s BGW non-composability?).

---

## Inputs used

| Input | Use | Provenance |
|---|---|---|
| Paper 5 Def 1 (`def:self-modeling-system`, main.tex line 342) | clause (iii) `sms:minimal` reproduced verbatim; defines `V_BM` (OUS) | LIVE `qm-from-self-modeling/main.tex` |
| Paper 5 composable/non-composable remark (main.tex lines 397–401; parallel 165–168) | **textual witness** that Def 1 scopes to *composable* self-modelers and treats non-composable `h_3(O)` separately | LIVE `qm-from-self-modeling/main.tex` |
| BGW 2020 | defines Jordan-monoidal composite (bifunctor on `FRJA-Sys`); `h_3(O)` = unique non-special simple FRJA, non-composable (universe-tensoring) | `ref-bgw` |
| Hanche-Olsen | universal tensor product; special ⟺ admits well-behaved composite; clarifies "internal composite (OUS)" vs "universal Jordan tensor (BGW)" are distinct properties | `ref-hanche-olsen` |
| `lem:bottleneck` (complexification.tex line 409) | the slice `A ≅ M_3(C)^sa ≅ h_3(C_u) ⊂ h_3(O)` exists; used only at the level of **principle** for the existence direction (item (c)) | LIVE `sm-from-self-modeling/sections/complexification.tex` |

**NOT used (by design — non-circularity):** RESTRICTION; the conditional expectation `E` /
coherent-embedding step; clause-(iii)-satisfaction-on-the-slice. (These are what
RESTRICTION concludes; using them here would be circular.)

**Provenance check performed:** `grep "rem:converse" complexification.tex` ⟹ **0 matches**;
`grep "lem:bottleneck" complexification.tex` ⟹ present (line 409). Therefore `rem:converse`
is treated as **prompt-inline authoritative only**, never as a published/labeled remark.

---

## Argument made

**Category-separation independence.** Recorded the Categories ledger tagging every object
(`V_B, V_M, V_BM` = OUS; `h_3(O), h_3(C_u)` = FRJA; BGW-composite = bifunctor/monoidal; `E`
= conditional expectation, forward-reference only). Then proved

```
  P_BGW ( h_3(O) BGW-non-composable )   does NOT entail   ¬P_VBM ( observer has no V_BM )
```

via:

- **(a) Category separation.** `P_BGW` is a monoidal/bifunctor property of the *whole*
  FRJA `h_3(O)` (tensoring with an *external* FRJA partner); `P_VBM` is an *internal*
  OUS-existence statement for one self-modeling subsystem. Different category ⟹ no
  type-correct inference rule sends `P_BGW` to `¬P_VBM`; the only candidate bridge premise
  *is* RESTRICTION, which is forbidden.
- **(b) Textual witness.** Paper 5 itself scopes Def 1 to *composable* self-modelers and
  treats non-composable `h_3(O)` as a separate companion-paper regime — direct authorial
  support that the two notions concern different objects.
- **(c) Existence direction (principle only).** `M_n(C)^sa` is a composable self-modeler
  with its own internal composite `V_BM` (content `rem:converse` will confirm —
  prompt-authoritative caveat noted), and `M_3(C)^sa ≅ h_3(C_u)` sits **inside** `h_3(O)`
  as the bottleneck slice. So "lives inside a non-composable algebra" ≠ "has no internal
  composite." Stated explicitly as principle/forward-reference; does **not** assert the
  slice satisfies clause (iii) (that is Phase 61/62).
- **(d) Circularity guard.** Named the circular route ("assume RESTRICTION ⟹ conclude the
  distinction") and verified by inspection that RESTRICTION / `E` / slice-clause-(iii) are
  used **nowhere** in (a)–(c).
- **(e) Honest-negative branch.** Wired the collapse condition: if the slice's "internal
  composite" turns out to *be* the BGW universe-composite (no surviving type distinction),
  or the independence cannot be argued without RESTRICTION, ⟹ DECISIVE NEGATIVE ⟹ PAUSE.

---

## Outcome

**DISTINCTION EARNED — no collapse, no PAUSE triggered.**

- The two propositions `P_VBM` (OUS-level, exists `V_BM`) and `P_BGW` (FRJA-monoidal-level,
  `h_3(O)` composable/not) are **type-distinct** and **logically independent**; the
  non-composability of `h_3(O)` does **not** preclude the observer's `V_BM`. RESTRICTION
  therefore does **not** collapse into circularity at this step.
- The argument is **non-circular**: established from category separation (a) + Paper 5's own
  scoping remark (b), with the existence direction (c) supplied only at the level of
  principle. RESTRICTION/embedding/slice-satisfaction appear nowhere as premises.
- Clause (iii) reproduced **verbatim**; **not weakened** (`fp-redefine-iii` guarded at
  source).
- `fp-conflate-composites`: **rejected** (the whole point of the argument).
- `fp-converse-already-in-paper`: **rejected** (`rem:converse` flagged prompt-inline, not in
  live paper; BGW confirmation deferred to 60-02).

**Failure mode:** none this attempt (clean).

**Caveat carried forward:** the existence direction (c) rests on the prompt-authoritative
`rem:converse`, whose exact BGW-grounding ("minimal = maximal composite coincide for
`M_n(C)^sa`") is to be confirmed in plan 60-02. This does **not** weaken the *type-level*
independence, which stands on (a)+(b) alone.

**Next:** plan 60-02 (confirm `rem:converse` against BGW), then Phase 61 (slice satisfies
clauses (i),(iv)).
