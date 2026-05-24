<!-- ASSERT_CONVENTION: metric_signature=riemannian_fisher, fourier_convention=na, natural_units=natural, gauge_choice=na, renormalization_scheme=na -->
<!-- Phase-61 attempt log (DERV-00-01 slice). Plan 61-01. Provenance: LIVE papers only. -->

# Attempt 03 — Slice `A = M_3(C)^sa` satisfies Paper 5 Def 1 (i)–(iv) in its own right

**Plan:** 61-01 (Phase 61, milestone v15.0) — DERV-00-01 slice (continuing attempt-01, attempt-02)
**Date:** 2026-05-24
**Goal:** Verify that the C\*-bottleneck slice `A = h_3(C_u) ≅ M_3(C)^sa` (`lem:bottleneck`, `n=3`)
satisfies **all four** clauses of Paper 5 Def 1 as a self-modeler **IN ITS OWN RIGHT** — clauses
(i)/(iv) directly, clauses (ii)/(iii) via `rem:converse` in its **CORRECTED direct-summand form** —
citing 61-02's exact-symbolic SymPy evidence, with the induced-by-`E` question explicitly **deferred
to Phase 62** and the stale "minimal=maximal" text flagged.

---

## Inputs used

| Input | Source (LIVE / staged) | Used for |
|---|---|---|
| Paper 5 Def 1 clauses (i)–(iv) verbatim | `~/repos/blog/landing/papers/qm-from-self-modeling/main.tex` lines 342–384 | the four clauses, checked AS WRITTEN (re-read this plan: clauses 346–356, `sms:minimal` unpacking 375–384) |
| `lem:bottleneck` | `~/repos/blog/landing/papers/sm-from-self-modeling/sections/complexification.tex` line 409 | supplies the slice `A ≅ M_3(C)^sa` (`n=3`, single `F_4`-orbit) |
| `rem-converse-bgw.md` (corrected grounding) | `derivations/p5-basin-restriction/rem-converse-bgw.md` (Phase 60, DERV-60-03) | clauses (ii)/(iii) supply; CORRECTED direct-summand form (minimal ≠ maximal); BGW exact citations |
| `claim.md` | `derivations/p5-basin-restriction/claim.md` (DERV-60-04) | allowed inputs; prohibited reward-hacking moves; PAUSE conditions; clause (iii) integrity guard |
| `two-composites.md` | `derivations/p5-basin-restriction/two-composites.md` (DERV-60-01/02) | categories ledger; type-distinctness of `V_BM` vs BGW `⊠̃` on `h_3(O)` |
| **BGW 2020** (arXiv:1606.09331v3 = Quantum 4, 359) | via Phase 60 grounding (`rem-converse-bgw.md`) | composite-dimension baseline: minimal `M_{n^2}(C)^sa`, maximal `M_{n^2}(C)^sa ⊕ M_{n^2}(C)^sa`; Thm 4.15 / Cor 4.16 / Table 2 / Prop 4.5 |
| **61-02 SymPy evidence (VALD-61-01)** | `code/slice_clause_iii_verification.py`, `tests/test_slice_clause_iii.py`; `61-02-SUMMARY.md` | exact-symbolic witnesses: rank 3, simplicity, dim 81 vs 162, product-form factorization on `M_9(C)^sa` |

**Independent re-confirmation this plan (executed):**
- `python code/slice_clause_iii_verification.py` → `OVERALL: ALL CHECKS PASS`, **exit 0**.
- `sed -n '340,385p' .../qm-from-self-modeling/main.tex` → Def 1 (i)–(iv) text confirmed verbatim
  (matches the quotes carried in `rem-converse-bgw.md` §1/§3).
- Live paper paths exist (`main.tex`, `complexification.tex`); stale repo `papers/` NOT used.

---

## Argument / verification made

**Structure: four separate, explicit clause blocks (none merged), then assembly + Phase 62 deferral
+ stale-text flag + type/category self-audit.**

1. **Clause (i) `sms:finite` — DIRECT.** `M_3(C)^sa` is a finite-dim (real-dim 9) spectral OUS
   (order unit `I_3`; finite-dim spectral theorem). Jordan rank 3: three mutually orthogonal
   nontrivial rank-1 projective units `E_11,E_22,E_33` with `E_ii²=E_ii`, `E_ii∘E_jj=0` (`i≠j`),
   `Σ=I_3`. **Cite 61-02** `check_rank_three_units`: rank 3, three orthogonal projective units →
   `I_3`, frame-independent (standard + rotated unitary frames), rank caps at 3. `3 ≥ 2` with strict
   margin. ✓

2. **Clause (ii) `sms:faithful` — `rem:converse`.** `V_B = V_M = M_3(C)^sa`, `φ = id`; the identity
   is trivially an order isomorphism (same PSD cone). Paper 5 line 349 verbatim. ✓

3. **Clause (iii) `sms:minimal` — `rem:converse` CORRECTED form, AS STATED.** Clause object =
   **minimal** composite `V_BM = M_3(C)^sa ⊗ M_3(C)^sa ≅ M_9(C)^sa` (real-dim 81). All four data
   checked for `n=3`: (1) product states `ρ_B⊗ρ_M`; (2) product effects `a⊗b` (BGW Prop 4.5; cite
   61-02 `kron` Hermitian lands in `M_9(C)^sa`); (3) non-signaling (standard complex-QM tensor
   product); (4) **product-form sequential product** `√a b √a = (a_B&b_B)⊗(a_M&b_M)` — **cite 61-02
   `check_seqprod_factorization`: exact full-`9×9` matrix proof** (Phase 60 open item CLOSED).
   Minimality in full force: `M_9(C)^sa` simple ⇒ smallest carrying exactly this data. CORRECTED
   `rem:converse`: maximal `C_3 ⊠̃ C_3 = M_9⊕M_9` (real-dim 162) strictly larger (extra classical
   bit, BGW Thm 4.15/Cor 4.16/Table 2); minimal is a **direct summand**; minimality **selects** the
   standard summand. **Cite 61-02 `dim 81 ≠ 162`.** Stated plainly: `minimal ≠ maximal`; clause
   holds because minimality picks the minimal composite, NOT because they coincide. ✓

4. **Clause (iv) `sms:simple` — DIRECT.** `M_3(C)` simple: center `= C·I_3`; only central idempotents
   `0, I_3`; no nontrivial order-unit direct-sum split. **Cite 61-02** `check_simplicity`: commutant
   of matrix units `= C·I_3` (off-diagonals identically 0), `λ²=λ ⇒ λ∈{0,1}`. ✓

5. **Assembly.** All four clauses hold for `A = M_3(C)^sa` intrinsically. Phase 61 intrinsic question
   answered **positively (honestly)**; milestone verdict remains UNDECIDED (Phase 63).

6. **Phase 62 deferral (mandatory).** Whether the structure is **coherently induced by `E`** from the
   non-associative `h_3(O)` is **NOT claimed** — Phase 62's load-bearing question. The datum-4
   factorization is on the **associative** `M_9(C)^sa` only; the non-associative `h_3(O)`
   computation (`E`'s interaction with `&`) is the Phase 62 NON-ASSOCIATIVITY guard, kept separate.
   **No step used `RESTRICTION`/`E`/Peirce-restriction/slice-induction as a premise.**

7. **Stale-text flag (mandatory).** ROADMAP SC3, REQUIREMENTS DERV-61-03, contract
   `deliv-slice-clause-iii.must_contain`, `ref-bgw.why_it_matters`, and `user_asserted_anchors` still
   literally say "minimal = maximal per BGW" — **STALE (pre-Phase-60)**. Corrected direct-summand
   form used; source of truth = `rem-converse-bgw.md` / `60-02-SUMMARY.md`. Bidirectional guard (so
   the verifier does not "correct" the corrected form back to the stale one).

8. **Type/category self-audit.** Every object tagged; "minimal vs maximal" same-category (FRJA),
   answer NOT-equal (`81 ≠ 162`); `V_BM` never conflated with BGW `⊠̃` on `h_3(O)`; `E`
   forward-reference only.

---

## Outcome

**All four clauses of Paper 5 Def 1 hold for `A = h_3(C_u) ≅ M_3(C)^sa` as a self-modeler in its own
right (intrinsically):**

- **(i)** finite-dim spectral OUS, three (`≥2`) orthogonal nontrivial projective units `→ I_3`
  [direct + 61-02 rank 3];
- **(ii)** `φ = id` order isomorphism [`rem:converse`];
- **(iii)** minimal composite `M_9(C)^sa` (dim 81) carries all four data **AS STATED**, minimality in
  full force, minimal a **direct summand** of maximal `M_9⊕M_9` (dim 162, extra classical bit),
  `minimal ≠ maximal` [CORRECTED `rem:converse`; datum-4 factorization cited from 61-02];
- **(iv)** simple, center `= C·I_3`, no nontrivial central idempotent [direct + 61-02].

The induced-by-`E` coherence is **explicitly DEFERRED to Phase 62** (not claimed, not pre-empted).
The stale "minimal=maximal" text is flagged; the corrected form is used. **Honest positive verdict
for the intrinsic question — not forced.**

---

## Failure modes / what remains open

- **No failure / no backtracking trigger.** Every 61-02 check passed: rank `= 3` (not `≠ 3`); three
  rank-1 projections sum to `I_3`; no nontrivial central idempotent; `dim(minimal) = 81 ≠ 162`; the
  product-form sequential product factorizes exactly on `M_9(C)^sa`. The disconfirming conditions
  (clause (i)/(iv) failing, or clause (iii) needing redefinition) were **not** triggered. No PAUSE.
- **Phase 60 open item now CLOSED.** The product-form (datum 4) factorization, *asserted* from the
  Lüders form in 60-02, is now **re-derived by exact `9×9` matrix computation** in 61-02 and cited
  here. This was the least-certain pre-run claim; it is now confirmed.
- **Deferred to Phase 62 (load-bearing, entirely unproved):** does `E : h_3(O) → A` **induce** the
  clause-(iii) structure coherently on the actual **non-associative** `h_3(O)`? Is `E`'s interaction
  with `a & b = √a b √a` (not just the Jordan product) controlled, or does non-associativity leak in?
  An obstruction here ⟹ PAUSE condition 2 (acceptable milestone outcome). Carried context (Phase 42:
  `√(T_a) T_b √(T_a)` exits `M_16(R)`; Phase 46: intrinsic `h_2(O)` closes in `V_0` with zero
  `V_{1/2}` leakage) — flagged for Phase 62, not used as premises here.
- **`rem:converse` provenance:** still prompt-inline / not-in-live-paper (FUTR-01 insertion after
  `lem:bottleneck`, corrected wording, no "coincide"). Confirmed against BGW in Phase 60.

---

## Prohibited reward-hacking moves — explicitly NOT used

- **`fp-redefine-iii`** — REJECTED. Clause (iii) checked AS STATED: all four data present
  (product states, product effects, non-signaling, product-form sequential product), minimality in
  full force (it is the lever that selects `M_9(C)^sa`). No datum dropped or weakened.
- **`fp-conflate-composites`** — REJECTED. Clause (iii) object = **minimal** composite (dim 81);
  maximal (dim 162) flagged as the extra-classical-bit contrast only. `V_BM` (observer's body⊗model
  self-composite) never identified with the BGW `⊠̃` universe-tensoring of `h_3(O)`.
- **`fp-converse-already-in-paper`** — REJECTED. `rem:converse` used as a prompt-inline principle
  confirmed against BGW (Phase 60), never cited as already-published; corrected direct-summand form
  only, never the stale "coincide" wording.
- **`fp-automatic-without-check` / `assert-Peirce-preserves-iii`** — REJECTED. Did NOT say "the slice
  is `M_3(C)^sa` so clause (iii) is automatic": produced explicit projective-unit / simplicity /
  composite-dimension / factorizing-sequential-product evidence (61-02) AND explicitly deferred
  induction-under-`E` to Phase 62. No `RESTRICTION`/`E`/Peirce-restriction premise used.
- **`fp-force-positive`** — REJECTED. The backtracking branch (clause failure / clause (iii) needing
  redefinition) was wired but **not taken**, because the 61-02 evidence genuinely passes. The positive
  verdict is earned, not papered over.

---

## Deliverables this attempt

- `slice-clause-iii.md` (DERV-61-01/02/03, citing VALD-61-01) — created, committed `b4322617`.
- `STATE.md` — updated (Step 2 / Phase 61 COMPLETE; Phase 61 detail subsection; Pointers; [61]
  RESOLVED, [62] PENDING; stale-text correction + guards carried; verdict UNDECIDED; no PAUSE).
- `attempt-03.md` — this file.
- **NOT modified:** `claim.md`, `two-composites.md`, `rem-converse-bgw.md` (owned by Phase 60). ✓
