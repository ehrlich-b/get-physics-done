<!-- ASSERT_CONVENTION: metric_signature=riemannian_fisher, fourier_convention=na, natural_units=natural, gauge_choice=na, renormalization_scheme=na -->
<!-- DERIVATION-TREE STATE for the p5-basin-restriction workspace. -->
<!-- NOTE: This is a PLAN DELIVERABLE, NOT the project .gpd/STATE.md. -->
<!-- Provenance: LIVE papers only (~/repos/blog/landing/papers/). NOT the stale repo papers/. -->

# Derivation-Tree State — p5-basin-restriction

**Milestone:** v15.0 The P5 <-> Basin Restriction Lemma
**Goal (verdict-only):** Prove or DISPROVE **(RESTRICTION)** (see `claim.md`): the
C*-bottleneck slice `A = h_3(C_u) ≅ M_3(C)^sa` satisfies Paper 5 Def 1 clause (iii),
with the observer's `V_BM` realized coherently inside the non-composable `h_3(O)` under the
conditional expectation `E`. Outcome is **a clean RESTRICTION theorem OR a
precisely-characterized obstruction.** A clean obstruction is fully acceptable.

**Current verdict:** `UNDECIDED`.

---

## The four-step attack

| Step | Phase | Description | State |
|---|---|---|---|
| **1** | **60** | **Two-composites distinction.** Prove rigorously & non-circularly that the observer's clause-(iii) `V_BM` is a *different object* from `h_3(O)`'s BGW non-composability. | **IN PROGRESS** (plan 60-01 done: distinction EARNED; plan 60-02 = confirm `rem:converse` against BGW) |
| 2 | 61 | **Slice satisfies clause (iii).** Verify `h_3(C_u) ≅ M_3(C)^sa` meets all four Def 1 clauses (i)–(iv) as a self-modeler in its own right (`rem:converse` gets (ii)–(iii); check (i), (iv)). Includes SymPy/matrix verification of the slice. | PENDING |
| 3 | 62 | **Coherent embedding (the hard part).** Show the self-modeling structure on `A` (its `V_BM`, its sequential product `a & b = sqrt(a) b sqrt(a)`) is induced by / consistent with the ambient `h_3(O)` Jordan structure **under `E`** — or exhibit a precise obstruction from the non-associative ambient. | PENDING (load-bearing, entirely unproved) |
| 4 | 63 | **Verdict.** A clean RESTRICTION theorem, or a precisely-characterized structural obstruction. | PENDING |

---

## Step 1 (Phase 60) detail — current

**Plan 60-01 (this plan):** DONE.
- **DERV-60-01:** `two-composites.md` — two type-distinct definition blocks
  (`V_BM` = OUS internal composite; BGW composite = bifunctor on `FRJA-Sys`, `h_3(O)`
  non-composable). Categories ledger established.
- **DERV-60-02:** `two-composites.md` §Independence — proved
  `P_BGW ⊬ ¬P_VBM` non-circularly via (a) category separation + (b) Paper 5's scoping
  remark + (c) principle-level existence (bottleneck slice witness); (d) circularity guard;
  (e) honest-negative/collapse branch wired. **Distinction EARNED; no collapse.**
- **DERV-60-04:** `claim.md` — RESTRICTION restated in derivation notation; allowed inputs;
  3+1 prohibited reward-hacking moves; PAUSE conditions. **STATE.md** (this file).
- **Attempt log:** `attempt-01.md`.

**Plan 60-02 (next):** confirm `rem:converse` exactly against BGW (does "minimal = maximal
composite coincide for `M_n(C)^sa`" hold, so clause (iii) is auto-satisfied for the slice?),
since `rem:converse` is prompt-authoritative but **not yet** a labeled remark in the live
`complexification.tex`.

---

## Pointers

| File | Contents |
|---|---|
| `two-composites.md` | (A) `V_BM` def, (B) BGW-composite def, Categories ledger, **Independence** argument (DERV-60-01/02) |
| `claim.md` | RESTRICTION in derivation notation; allowed inputs; prohibited moves; PAUSE conditions (DERV-60-04) |
| `STATE.md` | this file — derivation-tree state |
| `attempt-01.md` | Phase-60 attempt log (DERV-00-01 slice): inputs, argument, outcome |

---

## Open questions (flagged)

- **[60-02]** Does `rem:converse` hold exactly as stated against BGW — i.e. do the minimal
  and maximal composites coincide for `M_n(C)^sa`, so that clause (iii) is automatically
  satisfied by the slice? (Prompt-authoritative; not yet in live paper.)
- **[61]** Does `h_3(C_u) ≅ M_3(C)^sa` satisfy clauses (i) [spectral, ≥2 orthogonal
  projective units] and (iv) [simple] in its own right? (`rem:converse` targets (ii)–(iii).)
- **[62, the hard part]** Does restricting through the bottleneck `E` **preserve** what
  clause (iii) needs on the actual **non-associative** `h_3(O)` structure, or is there an
  obstruction? Specifically: is `E`'s interaction with the **sequential product**
  `a & b = sqrt(a) b sqrt(a)` (not just the Jordan product) controlled, or does
  non-associativity leak in? — entirely unproved; an obstruction here ⟹ PAUSE condition 2.
- **[63]** VERDICT: clean RESTRICTION theorem (through-line real) or precisely-characterized
  obstruction (`C` and `O` independent posits)?

---

## Guards carried forward

- Clause (iii) is used **verbatim**; never weaken (`fp-redefine-iii`).
- Never conflate `V_BM` with the BGW universe-composite (`fp-conflate-composites`).
- Never assert Peirce-restriction preserves clause (iii) without demonstrating on the actual
  non-associative `h_3(O)` (`assert-Peirce-preserves-iii`).
- `rem:converse` is prompt-inline, **not** published; confirm against BGW in 60-02
  (`fp-converse-already-in-paper`).
- Do **not** force a positive verdict; a clean obstruction is acceptable.
- LIVE sources only (`~/repos/blog/landing/papers/`).
