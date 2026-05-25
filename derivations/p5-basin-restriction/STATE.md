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

**Current verdict (milestone):** **FINALIZED — CHARACTERIZED OBSTRUCTION (coexistence-as-island).**
**Step 1 (Phase 60) COMPLETE:** two-composites distinction EARNED (60-01) and `rem:converse`
CONFIRMED-WITH-CAVEAT against BGW (60-02). **Step 2 (Phase 61) COMPLETE:** the slice `A ≅ M_3(C)^sa`
verified to satisfy all four Paper 5 Def 1 clauses (i)–(iv) **in its own right** — clauses (i)/(iv)
directly, clauses (ii)/(iii) via the corrected (direct-summand) `rem:converse`; clause (iii) AS
STATED via the **minimal** composite `M_9(C)^sa` (dim 81; `minimal ≠ maximal`); 61-02 exact-symbolic
evidence (rank 3, simple, dim 81 vs 162, product-form factorization); induced-by-`E` DEFERRED to
Phase 62. **Step 3 (Phase 62) COMPLETE:** the coherent-embedding step settled on the actual
non-associative `h_3(O)` via the AMBIENT-transport residual `R = E(sqrt(X) Y sqrt(X)) -
sqrt(EX)(EY)sqrt(EX)` for generic `X,Y` — **verdict (O) AMBIENT-TRANSPORT OBSTRUCTION** (exact
`R != 0`, `||R||^2 = 38593/72`; both routes agree; non-associativity load-bearing, associator
`= 524/9`), which **REFINES** `RESTRICTION` to **coexistence-as-island** (NOT independent posits,
NOT a collapse). `claim.md` updated (embedding clause weakened to coexistence-as-island; clause
(iii) unchanged). **No PAUSE** (corrected PAUSE-2: an ambient-transport obstruction is the expected
deliverable). **Step 4 (Phase 63) COMPLETE:** milestone verdict **FINALIZED** as **CHARACTERIZED
OBSTRUCTION** (coexistence-as-island; through-line SURVIVES) in `RESULT.md` — the one-sentence
DERV-00-02 verdict line written. 63-01 assembled the DRAFT; **63-02 ran the fresh-eyes adversarial
guard review BEFORE finalization (ROADMAP Success Criterion 2): all three reward-hacking guards
PASS (clause (iii) not redefined; the two composites not conflated; preservation demonstrated on
generic ambient `X,Y`, associator `524/9` load-bearing) against the real Phase 60/61/62 artifacts;
the decisive harness re-ran exit 0 / verdict (O) / `is_zero_exact=[False,False]`; honest-negative
confirmed; NO backtracking trigger fired** — so the verdict is EARNED. Bryan acknowledged
finalization (option-finalize) at the gated 63-02 backtracking-trigger step.

---

## The four-step attack

| Step | Phase | Description | State |
|---|---|---|---|
| **1** | **60** | **Two-composites distinction.** Prove rigorously & non-circularly that the observer's clause-(iii) `V_BM` is a *different object* from `h_3(O)`'s BGW non-composability. | **COMPLETE** (60-01: distinction EARNED; 60-02: `rem:converse` CONFIRMED-WITH-CAVEAT against BGW; existence side stands; no collapse, no PAUSE) |
| 2 | 61 | **Slice satisfies clause (iii).** Verify `h_3(C_u) ≅ M_3(C)^sa` meets all four Def 1 clauses (i)–(iv) as a self-modeler in its own right (`rem:converse` gets (ii)–(iii); check (i), (iv)). Includes SymPy/matrix verification of the slice. | **COMPLETE** (61-02: VALD-61-01 exact-symbolic evidence — rank 3, simple, dim 81 vs 162, product-form factorization on `M_9(C)^sa` [Phase 60 open item CLOSED]; 61-01: clause-by-clause (i)–(iv) — (i)/(iv) direct + evidence, (ii)/(iii) via corrected `rem:converse`, clause (iii) AS STATED, minimal composite the clause (iii) object, induced-by-`E` DEFERRED to Phase 62, stale "minimal=maximal" text flagged. Honest positive intrinsic verdict; no PAUSE.) |
| 3 | 62 | **Coherent embedding (the hard part).** Show the self-modeling structure on `A` (its `V_BM`, its sequential product `a & b = sqrt(a) b sqrt(a)`) is induced by / consistent with the ambient `h_3(O)` Jordan structure **under `E`** — or exhibit a precise obstruction from the non-associative ambient. | **COMPLETE** — verdict **(O) AMBIENT-TRANSPORT OBSTRUCTION**. The decisive object (CORRECTED 2026-05-24) is **ambient `E`-transport** `E(sqrt(X) Y sqrt(X))` vs `sqrt(EX)(EY)sqrt(EX)` for **generic** `X,Y` (the slice-internal case is the **trivial control** — closed associative subalgebra, leakage 0). 62-02 (VALD-62-01, exact-SymPy, assert-based no-pytest) computed `R != 0` exactly (`is_zero_exact=[False,False]`; `||R||^2 = 38593/72`, `R_{11} = -2`); both routes (direct residual + positional Peirce) agree; non-associativity load-bearing (associator `= 524/9`); ambient SP non-Hermitian. `E` does **NOT** transport the SP. This **REFINES** `RESTRICTION` to **coexistence-as-island** (observer = self-contained C\* island; through-line survives; `E` = access/projection map) — **NOT** independent posits, **NOT** a collapse PAUSE. `claim.md` updated (embedding clause weakened; clause (iii) unchanged). 62-03 §5 reads the verdict; 62-03 interactive checkpoint surfaces it. |
| 4 | 63 | **Verdict.** A clean RESTRICTION theorem, or a precisely-characterized structural obstruction. | **COMPLETE** — milestone verdict **FINALIZED** as **CHARACTERIZED OBSTRUCTION (coexistence-as-island; through-line SURVIVES)**. 63-01 assembled the DRAFT `RESULT.md`; **63-02** ran the fresh-eyes adversarial guard review (3/3 reward-hacking guards PASS against the real Phase 60/61/62 artifacts; harness re-run exit 0 / verdict (O) / `is_zero_exact=[False,False]`; honest-negative confirmed; **no backtracking trigger**) **BEFORE** finalization (ROADMAP SC2), then wrote the one-sentence DERV-00-02 verdict line and removed the DRAFT marker at the human-acknowledged (option-finalize) gate. Verdict EARNED; equals the exact Phase 62 computation (not forced, not over-stated as a collapse). |

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

## Step 2 (Phase 61) detail — current

**Plan 61-02 (wave 1, VALD-61-01):** DONE.
- **VALD-61-01:** `code/slice_clause_iii_verification.py` + `tests/test_slice_clause_iii.py`
  (21 tests) — exact-symbolic SymPy. `M_3(C)^sa` Jordan rank 3 (three orthogonal rank-1 projective
  units `E_11,E_22,E_33 → I_3`, frame-independent); simple (center `= C·I_3`, no nontrivial central
  idempotent); minimal composite `M_9(C)^sa` real-dim **81 = 9·9**, maximal `M_9 ⊕ M_9` real-dim
  **162 ≠ 81** (extra classical bit, BGW); **product-form sequential product factorizes exactly on
  the associative `M_9(C)^sa`** — `√a b √a = (a_B&b_B)⊗(a_M&b_M)` (Phase 60 open item CLOSED, derived
  not assumed). Re-run start of 61-01: ALL CHECKS PASS, exit 0.

**Plan 61-01 (wave 2, depends on 61-02):** DONE.
- **DERV-61-01 (clause i):** `slice-clause-iii.md` — `M_3(C)^sa` finite-dim spectral OUS with three
  (`≥2`) orthogonal nontrivial projective units `→ I_3` (direct + cite 61-02 rank 3).
- **DERV-61-02 (clause iv):** simple, center `= C·I_3`, no nontrivial central idempotent (direct +
  cite 61-02).
- **DERV-61-03 (clauses ii, iii via corrected `rem:converse`):** (ii) `V_B=V_M=M_3(C)^sa`, `φ=id`
  order isomorphism. (iii) AS STATED — minimal composite `M_9(C)^sa` (dim 81) carries all four data
  (product states; product effects [BGW Prop 4.5]; non-signaling; product-form sequential product
  [cite 61-02 factorization]); minimality in full force; **CORRECTED form** — minimal a **direct
  summand** of maximal `M_9⊕M_9` (dim 162, extra classical bit, BGW Thm 4.15/Cor 4.16); `minimal ≠
  maximal`; minimality SELECTS the standard summand. Cite 61-02 `dim 81 vs 162`.
- **Verdict (Phase 61):** all four clauses hold for `A = M_3(C)^sa` **intrinsically** (a self-modeler
  in its own right). Honest positive; no clause redefined; not forced.
- **Phase 62 deferral (explicit):** induced-by-`E` coherence from the non-associative `h_3(O)` is NOT
  claimed; the datum-4 factorization is on the **associative** composite only; no `RESTRICTION`/`E`/
  Peirce-restriction premise used. Phase 62 = NON-ASSOCIATIVITY guard (`E`'s interaction with `&`).
- **Stale-text flag (explicit):** ROADMAP SC3, REQUIREMENTS DERV-61-03, contract
  `deliv-slice-clause-iii.must_contain`, `ref-bgw.why_it_matters`, `user_asserted_anchors` still say
  "minimal=maximal per BGW" — STALE (pre-Phase-60). Corrected direct-summand form used; bidirectional
  guard recorded. Source of truth: `rem-converse-bgw.md`, `60-02-SUMMARY.md`.
- **Attempt log:** `attempt-03.md`.

---

## Step 3 (Phase 62) detail — current

**CORRECTED FRAMING (Bryan 2026-05-24):** coexistence-as-island. The plan-checker found the original
embedding clause over-specified — the slice-internal sequential-product test is **trivial** (the
slice `A = h_3(C_u)` is a closed associative subalgebra = range `E`, leakage 0). The **decisive
object is AMBIENT `E`-transport** `E(sqrt(X) Y sqrt(X))` vs `sqrt(EX)(EY)sqrt(EX)` for **generic**
`X,Y`. An ambient-transport obstruction **REFINES** `RESTRICTION` (it does NOT refute it).

**Plan 62-01 (wave 1, DERV-62-01):** DONE.
- **DERV-62-01:** `embedding-under-E.md` §0–§3 — explicit `E` (entrywise `proj_u`, `u=e_7`; positive
  unital idempotent, `E|_A=id`, range = JB-subalgebra via Effros–Störmer / `lem:bottleneck`);
  precisely what `E` preserves (Jordan product **on the slice** — and **NOT** automatically the
  sequential product; `E` is **not** a Jordan morphism on the ambient); the decisive crux framed as
  the ambient-transport residual `R` for generic `X,Y`; slice-internal = TRIVIAL control;
  exact-arithmetic spec; the CORRECTED RESTRICTION (coexistence-as-island, §3.7). Fork kept OPEN.

**Plan 62-02 (wave 2, DERV-62-02 + VALD-62-01):** DONE.
- **VALD-62-01:** `code/embedding_under_E_verification.py` + `tests/test_embedding_under_E.py` —
  exact-SymPy octonion arithmetic (Fano `e1e2=e4`), non-associative `h3o_matmul` (triple product by
  independent left/right association), `E` onto `h_3(C_u)`, ambient sqrt via exact-square trick
  `X=C*C`, the **DECISIVE ambient-transport residual**, positional-Peirce cross-check,
  non-associativity exerciser, slice-internal control. **Assert-based** `_report/ALL_PASS/sys.exit`
  harness (**NO pytest**; runnable as `python tests/test_embedding_under_E.py`, exits 0).
  Re-confirmed at start of 62-03: both entrypoints `OVERALL: ALL SELF-CHECKS PASS`, verdict (O),
  `is_zero_exact=[False,False]`, exit 0.
- **DERV-62-02:** `embedding-under-E.md` §4 — the decisive exact computation + verdict. **(O)**: the
  ambient residual `R = E(sqrt(X) Y sqrt(X)) - sqrt(EX)(EY)sqrt(EX)` is **exactly nonzero** for two
  generic pairs (`||R||^2 = 38593/72`, `R_{11} = -2`); `E` is NOT a Jordan morphism on the ambient
  (`||E(XoX)-(EX)o(EX)||^2 = 3797527/34560000`); non-associativity load-bearing (associator
  `= 524/9`); defect lands entirely in `C_u` (`e_0,e_7`), positional Peirce grades `4 + 1033/18 +
  3797/8 = 38593/72`; ambient SP non-Hermitian; slice-internal control trivial (leakage 0,
  associator 0).

**Plan 62-03 (wave 3, DERV-62-03):** DONE (this plan; the verdict + interactive checkpoint).
- **DERV-62-03:** `embedding-under-E.md` §5 — reads the verdict **(O)** off §4 (equals §4, no
  divergence); states the coexistence-as-island governing frame; characterizes the obstruction
  precisely (the product-form SP datum `E` cannot transport; defect inside `A`, all three `E_11`
  Peirce grades / `C_u` directions; minimal extra input via Hanche-Olsen induced-vs-imported, which
  coexistence does not require); REFINES `RESTRICTION` to coexistence-as-island (through-line
  survives; `E` = access/projection map; NOT independent posits, NOT a collapse). Milestone verdict
  left to Phase 63. **`claim.md` UPDATED** (embedding clause weakened to coexistence-as-island;
  verdict semantics + PAUSE condition 2 corrected; clause (iii) integrity + `fp-conflate-composites`
  preserved; dated provenance notes). **`attempt-04.md`** appended (DERV-00-01).
- **Interactive checkpoint (62-03 Task 3):** surfaces the verdict (O) for human acknowledgement —
  presented as the **expected** coexistence-as-island refinement, NOT a collapse.

---

## Pointers

| File | Contents |
|---|---|
| `two-composites.md` | (A) `V_BM` def, (B) BGW-composite def, Categories ledger, **Independence** argument (DERV-60-01/02) |
| `claim.md` | RESTRICTION in derivation notation; allowed inputs; prohibited moves; PAUSE conditions (DERV-60-04). **UPDATED 62-03:** embedding clause weakened to coexistence-as-island; verdict semantics + PAUSE condition 2 corrected (ambient-transport obstruction = expected refinement, not collapse); clause (iii) integrity + `fp-conflate-composites` preserved unchanged; dated provenance notes |
| `embedding-under-E.md` | **Phase-62 deliverable (DERV-62-01/02/03):** §0–§3 explicit `E` + crux framing + coexistence-as-island (62-01); §4 the decisive exact ambient-transport computation + verdict **(O)** (62-02); §5 the verdict read-off + characterized obstruction + minimal extra input, REFINING RESTRICTION to coexistence-as-island (62-03) |
| `code/embedding_under_E_verification.py`, `tests/test_embedding_under_E.py` | **VALD-62-01 (62-02):** exact-SymPy, assert-based (NO pytest); the decisive ambient-transport residual `R != 0` (verdict O), two routes agree, non-associativity load-bearing, slice-internal trivial control; `python tests/test_embedding_under_E.py` exits 0 |
| `rem-converse-bgw.md` | **`rem:converse` grounded against BGW (DERV-60-03):** faithful self-model of `M_n(C)^sa`, clause (iii) via minimal composite, EXACT BGW citation, CONFIRMED-WITH-CAVEAT (minimal ≠ maximal), provenance flag |
| `slice-clause-iii.md` | **Phase-61 clause-by-clause deliverable (DERV-61-01/02/03, citing VALD-61-01):** four separate clause blocks (i)–(iv) for `A = M_3(C)^sa` as a self-modeler in its own right; (i)/(iv) direct, (ii)/(iii) via corrected `rem:converse`; clause (iii) AS STATED (minimal composite `M_9(C)^sa`); Phase 62 deferral; stale-text flag; type/category self-audit |
| `STATE.md` | this file — derivation-tree state |
| `attempt-01.md` | Phase-60 attempt log (DERV-00-01): two-composites distinction (60-01) |
| `attempt-02.md` | Phase-60 attempt log (DERV-00-01): `rem:converse`-vs-BGW grounding (60-02) |
| `attempt-03.md` | **Phase-61 attempt log (DERV-00-01):** slice satisfies Def 1 (i)–(iv) in its own right (61-01) |
| `attempt-04.md` | **Phase-62 attempt log (DERV-00-01):** coherent embedding under `E` — ambient-transport decisive, slice-internal trivial control; verdict **(O)** (refines RESTRICTION to coexistence-as-island); no reward-hacking (62-03) |
| `code/slice_clause_iii_verification.py`, `tests/test_slice_clause_iii.py` | **VALD-61-01 (61-02):** exact-symbolic evidence — rank 3, simplicity, dim 81 vs 162, product-form factorization on `M_9(C)^sa` |

---

## Open questions (flagged)

- **[60-02] — RESOLVED (CONFIRMED-WITH-CAVEAT).** `rem:converse` does **NOT** hold *verbatim*:
  the minimal and maximal composites of `M_n(C)^sa` do **not** coincide (maximal `= 2×`
  minimal; extra classical bit, BGW Table 2 / Cor. 4.16). But its **load-bearing content
  holds**: the minimal/standard composite `M_{n^2}(C)^sa` exists, is a direct summand of the
  universal one (Thm 4.15), and clause (iii)'s *minimality* selects it — so **clause (iii) is
  auto-satisfied as written** for complex matrix algebras. Existence side of the distinction
  stands. FUTR-01 must insert the *corrected* wording (no "coincide"). See `rem-converse-bgw.md`.
- **[61] — RESOLVED (POSITIVE, intrinsic).** `h_3(C_u) ≅ M_3(C)^sa` satisfies **all four** Def 1
  clauses as a self-modeler in its own right: (i) finite-dim spectral OUS with three (`≥2`) orthogonal
  nontrivial projective units `→ I_3` and (iv) simple — both verified **directly** + 61-02 evidence;
  (ii) `φ=id` order isomorphism and (iii) minimal composite `M_9(C)^sa` (dim 81) carrying all four
  data AS STATED with minimality in full force — both via the **corrected** `rem:converse`
  (`minimal ≠ maximal`; minimal a direct summand of maximal `M_9⊕M_9`, dim 162). See
  `slice-clause-iii.md`. **Caveat:** this is the *intrinsic* result only; the induced-by-`E` question
  is [62], still open.
- **[62, the hard part] — RESOLVED (O, refinement either way).** Does `E` **transport** the
  sequential product `a & b = sqrt(a) b sqrt(a)` (not just the Jordan product) coherently from the
  actual **non-associative** `h_3(O)`? **Answer: NO** — verdict **(O) AMBIENT-TRANSPORT
  OBSTRUCTION**. The decisive object (CORRECTED 2026-05-24) is **ambient `E`-transport** for
  **generic** `X,Y` (the slice-internal case is the trivial control). 62-02 (VALD-62-01, exact-SymPy)
  found `R = E(sqrt(X) Y sqrt(X)) - sqrt(EX)(EY)sqrt(EX) != 0` exactly (`||R||^2 = 38593/72`,
  `R_{11} = -2`; both routes agree; non-associativity load-bearing, associator `= 524/9`; defect in
  `C_u` / all three `E_11` Peirce grades; ambient SP non-Hermitian). This **REFINES** `RESTRICTION`
  to **coexistence-as-island** (observer = self-contained C\* island; through-line survives; `E` =
  access/projection map) — **NOT** independent posits, **NOT** a collapse. **No PAUSE** (corrected
  PAUSE-2: an ambient-transport obstruction is the expected deliverable, not a backtracking
  trigger). See `embedding-under-E.md` §4/§5, `attempt-04.md`, `claim.md` (updated). The
  *induced-by-`E`* property is the now-not-required stronger property; coexistence-as-island does
  not need it (the slice carries clause (iii) intrinsically, Phase 61).
- **[63] — RESOLVED (milestone verdict FINALIZED).** Reads Step 3's (O) into the milestone framing:
  the milestone verdict is **CHARACTERIZED OBSTRUCTION → coexistence-as-island RESTRICTION** (the
  slice sits inside `h_3(O)` as `range E`; `E` = access/projection map, not a Jordan/SP morphism on
  the ambient; the through-line **SURVIVES** as the island through-line; (O) refines, does NOT
  refute). The fresh-eyes adversarial guard review (63-02) confirmed all three reward-hacking guards
  PASS (harness re-run exit 0 / verdict (O); no backtracking trigger) **before** finalization; the
  one-sentence DERV-00-02 verdict line is written in `RESULT.md` and the DRAFT marker removed.
  **Milestone verdict FINALIZED 2026-05-24** (human-acknowledged option-finalize). See `RESULT.md`
  (DERV-00-02), `embedding-under-E.md` §4/§5.

---

## Guards carried forward

- Clause (iii) is used **verbatim**; never weaken (`fp-redefine-iii`).
- Never conflate `V_BM` with the BGW universe-composite (`fp-conflate-composites`).
- Never assert Peirce-restriction preserves clause (iii) without demonstrating on the actual
  non-associative `h_3(O)` (`assert-Peirce-preserves-iii` / `fp-assert-preservation`). **[Phase 62:
  honored — the decisive test was the AMBIENT residual on generic `X,Y` with non-associativity
  load-bearing (associator `= 524/9`), NOT the trivial slice-internal control;
  `fp-ignore-nonassociativity` rejected; `fp-float-pass` rejected (exact arithmetic).]**
- `rem:converse` is prompt-inline, **not** published (grep-verified absent from
  `complexification.tex`); now grounded against BGW (60-02, `rem-converse-bgw.md`) —
  **CONFIRMED-WITH-CAVEAT**: confirm the corrected (minimal ≠ maximal) form, and never cite
  `rem:converse` as already-in-paper (`fp-converse-already-in-paper`). FUTR-01 = insert
  corrected remark after `lem:bottleneck`.
- Do **not** force a positive verdict; a clean obstruction is acceptable. **[EXTENDED 2026-05-24
  (`fp-force-positive`, both directions):** also do **not** over-state an ambient-transport
  obstruction (O) as a refutation / "independent posits" / collapse — (O) **refines** RESTRICTION to
  coexistence-as-island. The verdict equals the exact 62-02 computation. Phase 62: honored — (O)
  reported as the expected refinement, not forced to (P), not over-stated as a collapse; v11.0
  precedent carried only as historical context.]
- Clause (iii) is **unchanged** by the coexistence-as-island reframe — only `RESTRICTION`'s
  **embedding clause** is weakened (`claim.md`, 62-03); `V_BM = A (x) A` remains the observer's own
  composite (`fp-conflate-composites` preserved). The milestone verdict stays UNDECIDED
  (`fp-overclaim-milestone`; Phase 63).
- LIVE sources only (`~/repos/blog/landing/papers/`).
