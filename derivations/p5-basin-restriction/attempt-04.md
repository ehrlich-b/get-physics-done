<!-- ASSERT_CONVENTION: metric_signature=riemannian_fisher, fourier_convention=na, natural_units=natural, gauge_choice=na, renormalization_scheme=na -->
<!-- Phase-62 attempt log (DERV-00-01 slice). Plan 62-03. Provenance: LIVE papers only. -->

# Attempt 04 — Coherent embedding under `E`: does `E` transport the sequential product from the non-associative `h_3(O)`?

**Plan:** 62-03 (Phase 62, milestone v15.0) — DERV-00-01 slice (continuing attempt-01, attempt-02, attempt-03)
**Date:** 2026-05-24
**Goal:** Determine, on the **actual non-associative** `h_3(O)`, whether the conditional expectation
`E : h_3(O) -> A = h_3(C_u)` **transports** the self-modeling sequential product
`a & b = sqrt(a) b sqrt(a)` of clause (iii) coherently from the ambient (branch **P** — state and
**prove** the `RESTRICTION` embedding lemma), or **not** (branch **O** — characterize the
ambient-transport obstruction precisely). Per the CORRECTED framing (Bryan 2026-05-24), the verdict
is a **refinement of `RESTRICTION` either way** (coexistence-as-island): `RESTRICTION` needs only
that the observer self-models on the slice (Phase 61) and the slice sits inside `h_3(O)` as
`range E`; ambient `E`-transport is a **stronger, NOT-required** property.

---

## Inputs used

| Input | Source (LIVE / repo) | Used for |
|---|---|---|
| `E` setup + ambient-transport crux framing | `embedding-under-E.md` §1–§3 (62-01, DERV-62-01) | the explicit `E` (entrywise `proj_u`, `u=e_7`); `E` is a Jordan c.e. on the slice but NOT a Jordan morphism on the ambient; the decisive object framed as the AMBIENT residual `R` for generic `X,Y`; slice-internal = trivial control; exact-arithmetic spec; coexistence-as-island governing frame |
| The exact 62-02 AMBIENT-transport computation | `embedding-under-E.md` §4 (62-02, DERV-62-02 + VALD-62-01); `code/embedding_under_E_verification.py`; `tests/test_embedding_under_E.py` | the decisive exact residual `R`, the associator-nonzero precheck, the slice-internal control, the positional-Peirce cross-check, the not-a-Jordan-morphism-on-ambient check, the non-Hermiticity finding |
| `lem:bottleneck` + Effros–Störmer | `~/repos/blog/landing/papers/sm-from-self-modeling/sections/complexification.tex` line 409 (statement), 437 (Effros–Störmer), 481–486 (Peirce (iii)) | `E` as a positive unital idempotent with range a JB-subalgebra (Jordan-product-preserving embedding on the slice); the slice Peirce coordinates `V_1 ~ R`, `V_{1/2} ~ C_u^2`, `V_0 ~ h_2(C_u)` in which the obstruction is localized |
| Hanche-Olsen (universal tensor product; induced-vs-imported) | content as used in Phase 60 (`two-composites.md`, `rem-converse-bgw.md`); executor has no web | frames the verdict: (O) `E` does NOT *induce* the SP datum from `h_3(O)`; ambient transport would have to *import* an external datum not in `range E` — the minimal extra input; and the island carries its own SP intrinsically (Phase 61), so coexistence does not require it |
| Paper 5 clause (iii) (`sms:minimal`), verbatim | `~/repos/blog/landing/papers/qm-from-self-modeling/main.tex` lines 351–353 | the decisive SP datum is the ACTUAL product-form `sqrt(X) Y sqrt(X)` (not the Jordan product, not a surrogate); clause (iii) used verbatim and unchanged |
| `claim.md` (DERV-60-04, updated this plan) | `derivations/p5-basin-restriction/claim.md` | allowed inputs; prohibited reward-hacking moves; the CORRECTED PAUSE condition 2 (ambient-transport obstruction = expected deliverable, not collapse); clause (iii) integrity guard |
| `slice-clause-iii.md` §5/§6 (Phase 61) | `derivations/p5-basin-restriction/slice-clause-iii.md` | the slice satisfies all four Def 1 clauses **intrinsically**; the induced-by-`E` question was deferred to Phase 62; the datum-4 factorization was on the **associative** composite only — so the AMBIENT residual is the decisive object |
| **v11.0 / Phase 42 precedent** (`verify_sequential_product.py`) | GPD prior result | noted **only as historical context** — `sqrt(T_a) T_b sqrt(T_a) = (i/2) T_b` exits `M_16(R)` for anticommuting Cl(9,0) pairs is a **DIFFERENT mechanism** (Clifford non-commuting pairs in a fixed matrix algebra, NOT the `h_3(O) -> h_3(C_u)` projection restriction). **NOT carried as evidence** for (O) |

**Independent re-confirmation this plan (executed):**
- `python code/embedding_under_E_verification.py` → `OVERALL: ALL SELF-CHECKS PASS`; printed
  `DECISIVE VERDICT: O`; `per-pair is_zero_exact = [False, False]`;
  `|R|_F^2 = [38593/72, ...≈155]`; **exit 0**.
- `python tests/test_embedding_under_E.py` → `OVERALL: ALL SELF-CHECKS PASS`;
  `DECISIVE VERDICT (direct residual route): O`; **exit 0**. (Assert-based harness; **NO pytest** —
  `python tests/...py` directly; sympy/numpy only.)
- Both deterministic (no random seeds; hardcoded exact rational/surd entries); re-runs reproduce
  `is_zero_exact = [False, False]` and verdict (O).

---

## Argument / verification made

1. **`E` is a Jordan conditional expectation ON THE SLICE, but NOT a Jordan morphism on the
   ambient.** `E` (entrywise `proj_u`, `u = e_7`) is positive, unital, idempotent, `E|_A = id`
   (verified exactly); the embedding `A hookrightarrow h_3(O)` is Jordan-product-preserving
   (Effros–Störmer / `lem:bottleneck`), so `E(a o b) = (Ea) o (Eb)` for `a,b in A` (a trivial
   Jordan-side control). But on **ambient** elements `E` is **NOT** a Jordan morphism:
   `||E(X o X) - (EX) o (EX)||_F^2 = 3797527/34560000 != 0` (exact). So `E` does not even transport
   the Jordan structure from the ambient — a fortiori the (more rigid CFC triple) sequential
   product need not be transported.

2. **The slice-internal SP is TRIVIAL — recorded as the CONTROL, NOT the decisive test.** The slice
   `A = h_3(C_u) ~ M_3(C)^sa` is a **closed associative** Jordan subalgebra (= range `E`). So for
   `a,b in A`: `sqrt(a) b sqrt(a) in A`, `E(sqrt(a) b sqrt(a)) = sqrt(a) b sqrt(a)` (leakage exactly
   0), and the triple associator is exactly 0. This is just Phase 61's intrinsic triviality
   re-seen; it carries **no** information about ambient transport. Computed and recorded strictly as
   the control (both reward-hack loopholes — passing the trivial residual off as decisive, and the
   unrelated-matrices line-loophole — foreclosed).

3. **The decisive question is AMBIENT TRANSPORT for GENERIC `X,Y`.** Test, exactly,
   `R := E(sqrt(X) Y sqrt(X)) - sqrt(EX)(EY)sqrt(EX)` for generic ambient `X >= 0`,
   `Y = Y^dagger in h_3(O)` (off-diagonal octonion entries with nonzero `(e_1,...,e_6)`-parts).
   `sqrt(X)` is computed **in the ambient** via the exact-square trick `X = C*C` (so `sqrt(X) = C`
   exact; self-check `h3o_matmul(C,C) == X` exact), with `EX = E(C*C)` engineered diagonal to keep
   the **exact** slice root `sqrt(EX)` tractable — while `Y` is rich, so the decisive triple
   genuinely engages non-associativity. The `3x3` octonionic matrix products are computed by
   **independent left/right association** (the triple product is NOT assumed associative).

4. **The exact residual decides P vs O.** `R == 0` exact `=>` (P); `R != 0` exact `=>` (O). Result:
   `R != 0` exactly for **two distinct generic pairs** (`is_zero_exact = [False, False]`):
   `||R||_F^2 = 38593/72` on the clean rational pair (representative entry `R_{11} = -2`, a rational
   with no surd — definitively nonzero, not round-off), and `||R||_F^2 ≈ 155` on the second pair.
   The harness asserts only the **honest consistency** `octmat_is_zero(R) <=> is_zero_exact` (it does
   NOT hardcode P or O).

5. **Independent Peirce cross-check.** The defect `D = R` decomposed into (i) all-entry
   `C_u`-vs-`(e_1,...,e_6)` components and (ii) positional `E_11` Peirce grades `V_1/V_{1/2}/V_0`
   (faithful for the non-Hermitian defect) reaches the **same** verdict (O) as the direct residual
   on **both** pairs; the code RAISES on a split decision (none occurred).

6. **Non-associativity is LOAD-BEARING on the decisive data.** On the **same** decisive triple
   `(sqrt(X), Y, sqrt(X))`, the associator `||(sqrt(X) Y) sqrt(X) - sqrt(X) (Y sqrt(X))||^2 = 524/9
   != 0` (exact). So the test genuinely exercises `(xy)z != x(yz)` (not an accidentally-associative
   corner). Exact arithmetic throughout (zero tolerance; no float64 on the decisive path).

7. **By-product (sharpens O):** the ambient SP `sqrt(X) Y sqrt(X)` is itself **non-Hermitian** in
   `h_3(O)` (the involution identity fails under `(AB)C != A(BC)`) — an additional,
   association-dependent way `E` fails to transport the SP.

---

## Outcome

**Branch (O): AMBIENT-TRANSPORT OBSTRUCTION** (stated exactly as computed; **NOT forced**).

`E` does **NOT** transport the self-modeling sequential product coherently from the non-associative
`h_3(O)`: the ambient-transport residual `R = E(sqrt(X) Y sqrt(X)) - sqrt(EX)(EY)sqrt(EX)` is
**exactly nonzero** for generic ambient `X,Y` (non-associativity load-bearing, associator
`= 524/9`), with the direct-residual and positional-Peirce routes agreeing. The obstruction is
**precisely characterized** (handed to `embedding-under-E.md` §5):

- **The structure `E` cannot transport:** the product-form sequential-product datum from the
  ambient. (`E` is a Jordan c.e. on the slice, not a Jordan/SP morphism on the ambient.)
- **The defect** lives **inside `A`** (lands entirely in the `C_u` directions `e_0, e_7`;
  `C_u`-part`^2 = 38593/72`, `(e_1,...,e_6)`-part`^2 = 0`): the two slice elements
  `E(sqrt(X) Y sqrt(X))` and `sqrt(EX)(EY)sqrt(EX)` **fail to coincide** (not leakage out of `A`).
  Positional `E_11` Peirce grades `||V_1||^2 = 4`, `||V_{1/2}||^2 = 1033/18`, `||V_0||^2 = 3797/8`
  (sum `= 38593/72 = ||R||^2`); defect spread across all three grades, dominantly `V_0`, with a
  nonzero `V_1` scalar component. Mechanism: the ambient triple product populates
  `(e_1,...,e_6)`-content that `E` then projects away. The ambient SP is also non-Hermitian.
- **Minimal extra input** (for the stronger, not-required ambient transport): an external datum on
  `h_3(O)` **not in `range E`** (Hanche-Olsen induced-vs-imported: `E` does not *induce* the SP
  datum; transport would require *importing* it). **NOTE coexistence-as-island does not require
  this at all** — the observer self-models on the slice (Phase 61).

**This (O) REFINES `RESTRICTION` to coexistence-as-island** (the observer is a self-contained C\*
island; the through-line survives — basin `h_3(O)` -> maximal C\* slice `M_3(C)^sa` -> Paper 5
certifies QM; `E` = access/projection map). It is the **EXPECTED, ACCEPTABLE** outcome, **NOT**
"independent posits / two unconnected foundations" and **NOT** a program-collapse PAUSE (corrected
PAUSE condition 2). The **milestone verdict is UNDECIDED** — finalized in Phase 63.

---

## Failure modes / what remains open

- **No PAUSE / no backtracking trigger.** Per the corrected PAUSE condition 2 (`claim.md`), an
  ambient-transport obstruction is the **expected** deliverable. The genuinely-unexpected-pathology
  triggers did **not** fire: the slice-internal control is trivial as expected (leakage 0,
  associator 0), the slice **is** a closed associative subalgebra, and the two-composites
  distinction stands (PAUSE condition 1 untriggered).
- **The exact structure the SP needs that `E` cannot transport (named):** the
  `(e_1,...,e_6)`-content of the ambient `sqrt(X) Y sqrt(X)` that does not survive the projection
  `E`; equivalently, the rule fixing how that killed content feeds back into the `C_u`-image — not
  supplied by `E`. Defect localized in `C_u` / all three `E_11` Peirce grades; ambient SP
  non-Hermitian.
- **Generality caveat:** **one** exact nonzero residual on non-associativity-load-bearing generic
  data SUFFICES to establish (O); we have **two**. The complementary "no generic `X,Y` ever gives
  `R = 0`" is NOT needed for (O) and is NOT claimed. (A hypothetical (P) would have required a
  general symbolic argument, not representatives — but (P) did not occur.)
- **Minimal-extra-input precision caveat:** the precise minimal extra input ambient transport would
  need is the least-certain part — stated as precisely as the evidence allows (external datum not in
  `range E`, via Hanche-Olsen), flagged for Phase 63 / future work; NOT overstated. Coexistence-as-
  island does not require it.
- **Milestone verdict (Phase 63):** finalizes the coexistence-as-island RESTRICTION framing + runs
  the adversarial guard review. Left UNDECIDED here (`fp-overclaim-milestone`).
- **`rem:converse` provenance:** still prompt-inline / not-in-live-paper (FUTR-01), confirmed
  against BGW in Phase 60; not load-bearing for this attempt.

---

## Prohibited reward-hacking moves — explicitly NOT used

- **`fp-assert-preservation`** — REJECTED. The decisive object IS the AMBIENT transport residual
  `R` on the genuinely non-associative `h_3(O)` for **generic** `X,Y` — NOT the trivial
  slice-internal case, and NOT a hand-wave from `E`'s conditional-expectation status. `E` is shown
  NOT a Jordan morphism on the ambient (`||E(XoX)-(EX)o(EX)||^2 = 3797527/34560000 != 0`), so
  transport is genuinely non-trivial. The slice-internal case is computed and recorded strictly as
  the control (leakage 0).
- **`fp-ignore-nonassociativity`** — REJECTED. Non-associativity is load-bearing on the SAME
  decisive `(X,Y)`: associator `= 524/9 != 0` (exact). The decisive `X,Y` are generic ambient (not
  slice-confined). Both loopholes foreclosed (trivial-residual-as-decisive; unrelated-matrices
  line-loophole). `h3o_matmul` computes left/right associations independently.
- **`fp-float-pass`** — REJECTED. The decisive residual uses EXACT SymPy equality only
  (`octmat_is_zero = simplify(...) == 0`); no float64 on the decisive path (no `import numpy`, no
  `.evalf`, no `atol/rtol/1e-`). `R_{11} = -2` is an exact rational — definitively nonzero.
- **`fp-force-positive`** — REJECTED (both directions). Verdict (O) reported honestly as the exact
  computation yields — no cherry-picking `X,Y` to force `R = 0`, no relaxing the exact test (had `R`
  been exactly 0 with both routes agreeing, the verdict would have been (P)). And (O) is **not**
  over-stated as a refutation/collapse — it is framed as the expected coexistence-as-island
  refinement. v11.0 NOT carried as a thumb on the scale (different mechanism).
- **`fp-redefine-iii`** — REJECTED. The decisive test uses the ACTUAL clause-(iii) SP
  `sqrt(X) Y sqrt(X)` (not the Jordan product, not a surrogate). Clause (iii) itself is **unchanged**
  by the coexistence-as-island reframe — only `RESTRICTION`'s embedding clause is weakened (`claim.md`
  Task 1b).
- **`fp-conflate-composites`** — REJECTED. Under coexistence-as-island, `V_BM = A (x) A ~ M_9(C)^sa`
  remains the observer's OWN internal composite, **never** identified with / transported from the
  BGW universe-tensoring `(x)~` of `h_3(O)`. The island has its own composite; the basin fixes the
  TYPE `M_3(C)^sa`, not the composite (Phase 60 distinction preserved).
- **`fp-overclaim-milestone`** — REJECTED. Phase 62 settles the coherent-embedding STEP (ambient
  `E`-transport, refinement either way); the milestone verdict is left UNDECIDED for Phase 63.

---

## Deliverables this attempt

- `embedding-under-E.md` §5 (DERV-62-03) — the verdict (O) read off §4, interpreted as
  coexistence-as-island (committed `461944ba`). [§1–§3 = 62-01; §4 = 62-02.]
- `claim.md` — **UPDATED** (Task 1b): RESTRICTION's embedding clause weakened to
  coexistence-as-island; verdict semantics + PAUSE condition 2 corrected; clause (iii) integrity
  guard + `fp-conflate-composites` preserved unchanged; dated CORRECTED-FRAMING notes, provenance
  preserved (committed `c73ec4db`).
- `attempt-04.md` — this file.
- `STATE.md` — updated (Step 3 / Phase 62 COMPLETE; verdict (O); coexistence-as-island framing;
  Phase 62 detail; [62] RESOLVED; milestone UNDECIDED; corrected PAUSE-2 semantics; guards + pointers).
- `code/embedding_under_E_verification.py` + `tests/test_embedding_under_E.py` (from 62-02,
  VALD-62-01) — re-confirmed this plan (both exit 0, verdict (O)).
- **NOT modified:** `two-composites.md`, `rem-converse-bgw.md` (Phase 60), `slice-clause-iii.md`
  (Phase 61). **NOTE:** `claim.md` **IS** modified this phase (the coexistence-as-island
  correction) — unlike prior phases, where `claim.md` was Phase-60-owned and untouched.
