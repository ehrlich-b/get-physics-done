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

**Current verdict (milestone):** `UNDECIDED` (the verdict is Phase 63). **Step 1 (Phase 60)
COMPLETE:** two-composites distinction EARNED (60-01) and `rem:converse` CONFIRMED-WITH-CAVEAT
against BGW (60-02). No PAUSE triggered. Steps 2–4 (Phases 61–63) pending.

---

## The four-step attack

| Step | Phase | Description | State |
|---|---|---|---|
| **1** | **60** | **Two-composites distinction.** Prove rigorously & non-circularly that the observer's clause-(iii) `V_BM` is a *different object* from `h_3(O)`'s BGW non-composability. | **COMPLETE** (60-01: distinction EARNED; 60-02: `rem:converse` CONFIRMED-WITH-CAVEAT against BGW; existence side stands; no collapse, no PAUSE) |
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

**Plan 60-02 (this plan):** DONE.
- **DERV-60-03:** `rem-converse-bgw.md` — `rem:converse` grounded against BGW 2020.
  **Verdict: CONFIRMED-WITH-CAVEAT.**
  - **CONFIRMED:** faithful self-model of `M_n(C)^sa` (`V_M = V_B = M_n(C)^sa`, `phi = id`,
    internal composite `M_{n^2}(C)^sa`); **clause (iii) satisfied AS WRITTEN** (all four data
    verbatim, minimality in full force) via the **minimal / standard / locally-tomographic
    composite** `M_{n^2}(C)^sa`. Existence side of the two-composites distinction **stands**.
  - **CAVEAT (the correction):** `rem:converse`'s phrasing **"minimal = maximal composites
    COINCIDE for `M_n(C)^sa`" is FALSE as stated.** BGW's **maximal (universal) composite is
    strictly larger**: `C_n ⊠̃ C_m = M_{nm}(C)^sa ⊕ M_{nm}(C)^sa` (two copies — an **extra
    classical bit**), with the standard `M_{nm}(C)^sa` a **direct summand** of it. Clause
    (iii) is auto-satisfied because *minimality selects the standard summand*, **not** because
    the two coincide.
- **Provenance:** `rem:converse` **NOT** in live `complexification.tex` (grep 2026-05-23:
  0 matches; `lem:bottleneck` at line 409). Flagged prompt-inline / not-yet-in-paper;
  FUTR-01 insertion point = after `lem:bottleneck`, with a **wording constraint** (must NOT
  say "coincide"; must state the corrected direct-summand + extra-classical-bit form).
- **Distinction-preservation:** existence result SUPPORTS, does not collapse, 60-01;
  `V_BM` (OUS self-composite, body⊗model) never identified with the BGW `⊠̃` universe-tensoring
  of `h_3(O)`. **PAUSE condition 1 NOT triggered.**
- **Attempt log:** `attempt-02.md`.

### EXACT BGW STATEMENT (the load-bearing citation — carried into Phase 61 baselines)

> **BGW 2020** (Barnum-Graydon-Wilce, *Quantum* **4**, 359; arXiv:1606.09331v3):
> - **Corollary 4.16 + discussion (p.29):** for `A = B = C_n = M_n(C)^sa`, the universal
>   tensor product is `A ⊠̃ B = M_{n^2}(C)_sa ⊕ M_{n^2}(C)_sa`, with *"the usual
>   quantum-mechanical composite `M_{n^2}(C)_sa`"* as a **separate** candidate (a direct
>   summand, by **Theorem 4.15**, p.29).
> - **Table 2 (p.21):** `C_n ⊠̃ C_k = C_{nk} ⊕ C_{nk}`. **Table 1(a) (p.19):**
>   `C^*(C_n) = M_n(C) ⊕ M_n(C)`.
> - **Theorem 4.12 (p.28):** composite of simple nontrivial EJAs is special, UR.
> - **Proposition 4.14 (p.28; intro/abstract calls it "Corollary 4.14"):** no composite
>   with an exceptional factor unless the other is classical — grounds the `h_3(O)`
>   non-composability side.
> - **Proposition 3.10 (p.21) = Hanche-Olsen Thm 5.5:** only complex systems have locally
>   tomographic composites with a qubit. **`A` exceptional iff `C^*(A) = {0}`** (p.18) ⇒
>   `M_n(C)^sa` special admits `⊠̃`; `h_3(O)` does not.
> - "Extra classical bit": abstract (p.1), Example 6.3 (p.35), §6.3 (p.39).

**Numbering caveat for the verifier:** v3/published labels the no-exceptional-composite
result **Proposition 4.14**; the abstract/intro result-map calls it **Corollary 4.14**.
Same content.

---

## Pointers

| File | Contents |
|---|---|
| `two-composites.md` | (A) `V_BM` def, (B) BGW-composite def, Categories ledger, **Independence** argument (DERV-60-01/02) |
| `claim.md` | RESTRICTION in derivation notation; allowed inputs; prohibited moves; PAUSE conditions (DERV-60-04) |
| `rem-converse-bgw.md` | **`rem:converse` grounded against BGW (DERV-60-03):** faithful self-model of `M_n(C)^sa`, clause (iii) via minimal composite, EXACT BGW citation, CONFIRMED-WITH-CAVEAT (minimal ≠ maximal), provenance flag |
| `STATE.md` | this file — derivation-tree state |
| `attempt-01.md` | Phase-60 attempt log (DERV-00-01): two-composites distinction (60-01) |
| `attempt-02.md` | Phase-60 attempt log (DERV-00-01): `rem:converse`-vs-BGW grounding (60-02) |

---

## Open questions (flagged)

- **[60-02] — RESOLVED (CONFIRMED-WITH-CAVEAT).** `rem:converse` does **NOT** hold *verbatim*:
  the minimal and maximal composites of `M_n(C)^sa` do **not** coincide (maximal `= 2×`
  minimal; extra classical bit, BGW Table 2 / Cor. 4.16). But its **load-bearing content
  holds**: the minimal/standard composite `M_{n^2}(C)^sa` exists, is a direct summand of the
  universal one (Thm 4.15), and clause (iii)'s *minimality* selects it — so **clause (iii) is
  auto-satisfied as written** for complex matrix algebras. Existence side of the distinction
  stands. FUTR-01 must insert the *corrected* wording (no "coincide"). See `rem-converse-bgw.md`.
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
- `rem:converse` is prompt-inline, **not** published (grep-verified absent from
  `complexification.tex`); now grounded against BGW (60-02, `rem-converse-bgw.md`) —
  **CONFIRMED-WITH-CAVEAT**: confirm the corrected (minimal ≠ maximal) form, and never cite
  `rem:converse` as already-in-paper (`fp-converse-already-in-paper`). FUTR-01 = insert
  corrected remark after `lem:bottleneck`.
- Do **not** force a positive verdict; a clean obstruction is acceptable.
- LIVE sources only (`~/repos/blog/landing/papers/`).
