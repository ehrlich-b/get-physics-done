# Phase 70 (A0) Plan Check — Engine Reconciliation & Signature Bridge

**Checked:** 2026-05-30
**Checker:** gpd-plan-checker (goal-backward, with empirical reproduction against the live engine)
**Plans:** 70-01 (wave 1, 3 tasks), 70-02 (wave 2, 3 tasks)
**Verdict: FAIL** — two independent, reproducible, *load-bearing* benchmark errors are baked into the plans' acceptance criteria. Because this is the foundational gate for all of v17.0, a non-interactive executor will hit assertion failures on the decisive checks, and (worse) a contaminated/incorrect benchmark would silently miscalibrate every downstream curvature. Fix the two benchmarks (and the conjugated-row label), then re-plan.

Important: the underlying SSOT engine (`ring_lemma_verification.py det_3`) is CORRECT and the *strategy* is sound. The failure is entirely in the plans' **hardcoded expected numbers and the chosen test point** — but those are encoded as `assert == +4 / == 16 / == diag(9,9,18,18)` pass conditions, so they are blockers, not cosmetics.

---

## What I verified empirically (exact over Q, against the live engine)

All runs used `code/ring_lemma_verification.py` (the SSOT). Output captured to files to avoid terminal scrambling.

### A. SSOT `det_3` is genuinely correct — PASS
- `det_3(P) == cayley_hamilton_norm(P)` at every `octonionic_points()` entry. ✓
- `inner_derivations()` returns exactly **324** nonzero brackets, built in **3.4 s** (no watchdog risk). ✓
- Association order DOES discriminate the SSOT from the left-right order (see below), so the F_4 story is real.
- **Slice det form CONFIRMED:** `det_3` restricted to the 4 sub-slice coords at alpha=1/3 equals **exactly** `beta*gamma/3 - p^2/3 - q^2/3` (diff = 0 over Q). Plan 70-02 `test-index-map` is correct as written.

### B. BLOCKER 1 — the three-ordering reconciliation table (Plan 70-01 Task 3 / `claim-cross-term-reconciled` / `test-cross-term-association`) has wrong hardcoded values and the wrong test point.

The plan asserts, at `P = octonionic_points()[1]`:
- SSOT `(x2 x1) x3` → `Re(cross) = +4`, det == CH
- conjugated `x2* x1* x3` → `Re(cross) = +4`, det == CH (confirming row)
- buggy `(x1 x2) x3` → `Re(cross) = -4`, det != CH, **`N_SSOT - N_buggy == 16`**

**Empirical truth (exact over Q):**

| Point | SSOT `(x2 x1)x3` | LR `(x1 x2)x3` | conj `x2*(x1*x3)` | SSOT=CH | LR=CH | conj=CH | `N_SSOT - N_LR` | associator Re |
|------|------|------|------|---|---|---|------|------|
| `[0]` | 0 | 0 | 0 | ✓ | ✓ | ✓ | 0 | **0 (vacuous!)** |
| `[1]` | **-1** | **+1** | **-1** | ✓ | ✗ | ✓ | **-2** | 2 |
| `[2]` | **+4** | **-4** | **+4** | ✓ | ✗ | ✓ | **8** | 2 |

Three concrete errors:
1. **Wrong point.** The (+4 / -4) values occur at `octonionic_points()[2]`, NOT `[1]`. At `[1]` the values are (-1 / +1).
2. **Wrong magnitude.** The claimed "off by exactly 16" is false: it is **-2** at `[1]` and **+8** at `[2]`. (The factor-2 from `2*Re(cross)` is already included in N; there is no extra doubling to 16.)
3. **Conjugated row mislabeled / value wrong.** The conjugated form `x2*(x1*x3)` does match CH (good), but its `Re(cross)` tracks the SSOT (**-1** at `[1]`, **+4** at `[2]`) — it is NOT a separate "+4 confirming" datum at `[1]`. The real discriminator at these points is the **association order** (SSOT `(x2 x1)x3` vs LR `(x1 x2)x3`); the conjugated-nested form happens to equal the SSOT.

Consequence: an executor running Task 3 literally (`P = octonionic_points()[1]`; `assert SSOT Re == +4`; `assert buggy Re == -4`; `assert N_SSOT - N_buggy == 16`) gets **three immediate assertion failures**. `test-cross-term-association` (an automated acceptance test) fails. The plan's own disconfirming-observation ("SSOT and buggy give the SAME det → vacuous") would also mis-fire, since at `[1]` SSOT and LR genuinely differ (-1 vs +1) yet none of the hardcoded numbers match.

Maps to: Plan 70-01 Task 3; `claim-cross-term-reconciled`; `acceptance_tests.test-cross-term-association`; frontmatter `conventions.cross_term` narrative + `must_contain: ["...", "324", "reconciliation"]`.

### C. BLOCKER 2 — the Hessian benchmark `diag(9,9,18,18)`, det 26244 (Plan 70-02 Task 2 / `test-hessian-benchmark`) is NOT produced by the plan's stated procedure.

The plan's procedure: "compute the cone metric `Hess(-log det)` at the center I/3 restricted to the 4 spacetime sub-slice coords (sympy.diff x2 of `-log(det_3)`, evaluate at I/3)"; pass condition "`== diag(9,9,18,18)` exactly over Q and `det == 26244`."

**Empirical truth (exact over Q), following that procedure literally:**
- Restricted to `{beta, gamma, p, q}`: `Hess(-log det)|_{I/3} = [[18,9,0,0],[9,18,0,0],[0,0,18,0],[0,0,0,18]]`.
- **det = 78732** (= 9·18·18·27), **eigenvalues {9, 18, 18, 27}** — NOT det 26244, NOT diag(9,9,18,18).
- `78732 / 26244 = exactly 3`. The discrepancy is the radial/trace `-log det` direction: the (beta,gamma) block is `[[18,9],[9,18]]` with eigenvalues {trace-free = 9, radial = 27}. The benchmark `diag(9,9,18,18)` (eigenvalues {9,9,18,18}) would require that block to be `9·I` — i.e. the convex radial direction (eigenvalue 27) removed/normalized away, which the plan does NOT specify.
- I checked all three diagonal-pair restrictions `{alpha,beta,p,q}`, `{alpha,gamma,p,q}`, `{beta,gamma,p,q}`: every one gives det **78732**, eigenvalues **{9,18,18,27}**. None gives 26244.

So the plan's `test-hessian-benchmark` pass condition is unreachable by its own procedure. Either:
- the literal `Hess(-log det)` 4×4 restriction is the intended object → then the benchmark should be **det 78732, eigenvalues {9,18,18,27}** (NOT diag(9,9,18,18)/26244); or
- a trace-removed / det-normalized / induced-on-{det=const} slice metric is intended → then the plan must **specify that projection explicitly** (it currently does not), and re-derive the expected matrix.

This is exactly the kind of silently-wrong background the phase exists to prevent: `diag(9,9,18,18)` is also cited verbatim in CONVENTIONS.md §1 and state.json `convention_lock` as the bulk-metric test value, so if the true object is `{9,18,18,27}`/78732 the *convention lock itself* is mis-stated and must be corrected too.

Maps to: Plan 70-02 Task 2; `claim-signature-bridge`; `acceptance_tests.test-hessian-benchmark`; `deliv-bulk-engine-geom.must_contain: ["diag(9,9,18,18)","26244"]`; CONVENTIONS.md §1 + state.json `convention_lock` bulk-metric test value.

Note: this also undermines `test-minkowski-reduction`. That gate is constructed so `h := [restricted cone-Hessian] - [its value at center]`, which is zero-at-center *by construction* regardless — so the residual=0 check will "pass" trivially even on a wrong restricted Hessian. The real content (that the background is the *correct* Minkowski form, eigenvalues right, signature (1,3)) rides on the Hessian benchmark being correct. With BLOCKER 2 unresolved, a green `test-minkowski-reduction` would be a false pass (it only checks the tautological `Hess - Hess|center == 0`, not that the metric is the intended one).

---

## Things that are FINE (do not re-litigate)

- **Cross-term notation vs the convention lock — NO contradiction.** CONVENTIONS.md / state.json write the SSOT as `2Re(x2* x0* x1)` (conjugated, h3o_tower `x0,x1,x2` naming); the engine + plans write `2Re((x2 x1) x3)` (engine-native `x1,x2,x3`). I verified empirically these compute the **same `det_3`** (both equal the CH norm at every test point: the conjugated-nested `x2*(x1*x3)` equals the SSOT `(x2 x1)x3`). Same convention, two labelings. The task brief's worry that the plan might use the roadmap-line typo `2Re((x2 x1) x3)` is unfounded — that IS the correct SSOT, matching the engine line 320/325.
- **Potential `-log det`, signature mostly-minus (1,3), SSOT = `ring_lemma_verification.det_3`, `octonion_algebra.py` BANNED on the decisive path, `exact_only_guard`** — all correctly pinned in both plans' frontmatter, contracts, and forbidden proxies (`fp-wrong-cross-term`, `fp-float-decisive`, `fp-contaminated-background`). Good.
- **EXACT-over-Q discipline** — every decisive verdict is specified `simplify == 0` / `.rank()` over QQ; float only as labeled non-decisive triage. `fp-float-decisive` correctly surfaced. Good.
- **Dependency / wave sanity** — 70-01 `depends_on: []` (wave 1); 70-02 `depends_on: ["70-01"]` (wave 2). Acyclic, no forward refs, wave numbers correct. `gpd verify plan-structure` reports `valid: true`, 3 well-formed tasks each (files/action/verify/done all present). Good. (The task brief's "6 tasks / 7 tasks" does not match the files — each plan has 3 tasks — but the structure is sound; not an issue.)
- **324/324 LOCK 7b certificate** — the genuinely decisive F_4 test, and it is correctly specified and cheap (3.4 s to build the brackets; full check "tens of seconds", well under the ~150 s watchdog). This is the check that actually proves the engine; it is correct.
- **Watchdog** — all steps run < ~60 s; no foreground `python -u`/progress-print requirement for Phase 70 (info-level only).
- **VALD-03 / H^3** — correctly scoped as state-and-cite (Totaro `-d^2/4 = -1`, d=2), full computation deferred to Phase 71. Fine.
- **Construction (ii) vs (i)** — correctly stated/rejected with reasons (C*-bottleneck conjecture; Visser chart-dependence). Fine.

---

## Minimal concrete fixes (do NOT rewrite the plans here — hand back to planner)

1. **Fix the reconciliation table (Plan 70-01 Task 3, `test-cross-term-association`, `claim-cross-term-reconciled`, frontmatter `conventions.cross_term`).** Either:
   - switch the test point to `octonionic_points()[2]` and assert SSOT `Re=+4`, LR `Re=-4`, `N_SSOT - N_LR = 8` (NOT 16); or
   - keep `[1]` and assert SSOT `Re=-1`, LR `Re=+1`, `N_SSOT - N_LR = -2`.
   In both cases: make the discriminator **association order** (`(x2 x1)x3` vs `(x1 x2)x3`), and label the conjugated `x2*(x1*x3)` as a row that **equals the SSOT** (value = SSOT, not a separate +4). Best practice: assert the *invariant* `det_3 == cayley_hamilton_norm` for SSOT and `!=` for the LR order, rather than hardcoding `Re(cross)` magnitudes that depend on the point. Drop the "off by exactly 16" claim. Confirm associator-Re != 0 on the chosen point (true for `[1]` and `[2]`; **false for `[0]`** — never use `[0]`).

2. **Fix the Hessian benchmark (Plan 70-02 Task 2, `test-hessian-benchmark`, `deliv-bulk-engine-geom.must_contain`, AND CONVENTIONS.md §1 / state.json `convention_lock`).** Decide which object is intended and make the plan + convention lock agree with the engine:
   - if the literal `Hess(-log det)` 4×4 restriction: expected = `[[18,9,0,0],[9,18,0,0],[0,0,18,0],[0,0,0,18]]`, **det 78732, eigenvalues {9,18,18,27}**; or
   - if a trace-removed / det-normalized slice metric (to actually get `diag(9,9,18,18)`/26244): **specify the projection explicitly** in the procedure and re-derive. Until specified, `diag(9,9,18,18)`/26244 is unreachable.
   The `det 78732 = 3 * 26244` factor is the radial (eigenvalue 27 vs 9) direction — name it so the choice is deliberate, not silent.

3. **Harden `test-minkowski-reduction`** so it is not a tautology. The `h := Hess - Hess|center` construction makes residual=0 trivially. Add an independent check that the *background* (eta) is the intended Minkowski form with the correct eigenvalue/signature structure tied to the corrected fix #2, so a wrong restricted Hessian cannot pass.

4. (Info) Optionally have the planner correct the stale `.gpd/research/METHODS.md` / `PITFALLS.md` octonion_algebra-is-SSOT claim, and reconcile the CONVENTIONS.md `2Re(x2* x0* x1)` vs engine `2Re((x2 x1) x3)` labeling with a one-line note that they are the same det in different naming (verified equal over Q) — to stop this from re-biting downstream.

---

## Verdict

**FAIL.** Strategy, dependencies, conventions-lock alignment, exact-over-Q discipline, and the real F_4 certificate (LOCK 7b, 324/324) are all sound. But the two benchmarks that the plans encode as load-bearing pass conditions — the cross-term reconciliation table (+4/-4/off-by-16 at `[1]`) and the Hessian benchmark (`diag(9,9,18,18)`/26244) — are **falsified by the live engine** (true: -1/+1/off-by-2 at `[1]` and +4/-4/off-by-8 at `[2]`; true Hessian det 78732, eigenvalues {9,18,18,27}). On the foundational A0 gate these are exactly the silent-corruption failures the phase exists to catch. Return to planner with fixes 1-3 (4 optional), then re-verify the two corrected benchmarks before execution.
