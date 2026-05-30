# Phase 70 (A0) Plan Check — Engine Reconciliation & Signature Bridge

**Checked:** 2026-05-30
**Checker:** gpd-plan-checker (goal-backward, with empirical reproduction against the live engine)
**Plans:** 70-01 (wave 1, 3 tasks), 70-02 (wave 2, 3 tasks)
**Verdict: PASS_WITH_NOTES** — the plans will achieve the Phase 70 goal. All decisive benchmarks were reproduced exactly over Q against the live SSOT engine and match the plans. One minor self-consistency wrinkle in the non-vacuity guard wording (Note A) should be heeded by the executor; it does not block.

> Correction notice: an earlier draft of this file recorded FAIL based on a verification harness that was silently throwing `TypeError` (I passed an octonion list to `oct_real()`, which expects a scalar, so the "empirical" cross-term numbers in that draft were fabricated from crashed runs). Re-running correctly (reading the real part as octonion component `[0]`) reproduces the plans' values exactly. This file supersedes that draft.

---

## What I verified empirically (exact over Q, against `code/ring_lemma_verification.py`)

Scripts run against the live SSOT engine; real parts read as octonion component `[0]`.

### A. The SSOT `det_3` and the F_4 certificate — CONFIRMED
- `det_3(P) == cayley_hamilton_norm(P)` exactly at all three `octonionic_points()`. ✓
- `inner_derivations()` returns exactly **324** nonzero brackets, built in **0.5 s** (LOCK 7b is cheap — far under the ~150 s executor watchdog; no foreground/`python -u` needed for Phase 70). ✓
- Cross-term notation is consistent, NOT the roadmap-line typo. Engine line 335 is literally `cross = oct_mul(oct_mul(x2, x1), x3)` = `2Re((x2 x1) x3)`; the plans use exactly this. The CONVENTIONS.md / state.json label `2Re(x2* x0* x1)` is the SAME det in h3o_tower's conjugated `x0,x1,x2` naming — I confirmed the conjugated form `x2*(x1* x3)` equals the SSOT and the CH norm at the test point. Same convention, two labelings; no contradiction.

### B. Cross-term reconciliation table (Plan 70-01 Task 3 / `test-cross-term-association`) — CONFIRMED CORRECT at `octonionic_points()[1]`

| Ordering | code expr | Re(cross) | N == CH? |
|---|---|---|---|
| SSOT `(x2 x1) x3` | `oct_mul(oct_mul(x2,x1),x3)` | **+4** | **YES** |
| conjugated `x2*(x1* x3)` | `oct_mul(oct_conj(x2),oct_mul(oct_conj(x1),x3))` | **+4** | **YES** (reconciles to SSOT) |
| buggy `(x1 x2) x3` | `oct_mul(oct_mul(x1,x2),x3)` | **-4** | **NO** |

`N_SSOT - N_LR = 16` exactly. Every number the plan hardcodes (+4 / +4 / -4, "off by 16", point `[1]`) is correct. ✓

### C. Hessian benchmark + slice det form (Plan 70-02 Tasks 1-2) — CONFIRMED CORRECT
Following the plan's stated procedure literally (sympy.diff x2 of `-log(det_3)`, restrict to the 4 spacetime sub-slice coords `{beta, gamma, p, q}`, evaluate at I/3):
- `Hess(-log det)|_{I/3} = [[9,0,0,0],[0,9,0,0],[0,0,18,0],[0,0,0,18]] = diag(9,9,18,18)`, **det = 26244**, eigenvalues {9,9,18,18}. ✓ (Matches the plan AND CONVENTIONS.md §1 / state.json `convention_lock`. The 4-var restriction is the right object; including the alpha/trace direction would give the 5-var {9,9,9,18,18} — the plan correctly restricts to the 4 sub-slice dirs, NOT 5.)
- `det_3` restricted to `{x1,x2,x3,x10}` at alpha=1/3 = `beta*gamma/3 - p^2/3 - q^2/3` exactly (diff = 0 over Q). ✓ `test-index-map` is correct as written.

### D. Structure, dependencies, conventions, exact-over-Q — CONFIRMED
- 70-01 `depends_on: []` (wave 1); 70-02 `depends_on: ["70-01"]` (wave 2). Acyclic, no forward refs, waves correct.
- Both plans: 3 well-formed tasks with `<files>/<action>/<verify>/<done>`; full contract blocks (claims → deliverables → acceptance_tests, references with anchors, forbidden_proxies, uncertainty_markers, links). (`gpd verify plan-structure` is not a command in this build — checked by hand.)
- Potential `-log det`, signature mostly-minus (1,3), SSOT = `ring_lemma_verification.det_3`, `octonion_algebra.py` BANNED on the decisive path, `exact_only_guard`, `fp-wrong-cross-term` / `fp-float-decisive` / `fp-contaminated-background` all correctly pinned.
- EXACT-over-Q discipline correct everywhere; float only as labeled non-decisive triage.

---

## Goal-backward coverage (all 5 success criteria + 4 requirements)

| Phase-70 success criterion | Requirement | Covered by | Status |
|---|---|---|---|
| SC1: warm engine ALL_PASS reproduced; det_3 certified via CH + 324/324; three cross-term orderings reconciled on NON-associative e4..e7 data | SETU-01 | 70-01 Tasks 1,2,3 | COVERED (see Note A on the e4..e7 non-vacuity wording) |
| SC2: bridge stated as construction (ii); (i) reported as rejected + why (C*-bottleneck conjecture; Visser chart-dependence) | SETU-02 | 70-02 Task 1 | COVERED |
| SC3: EXACT Minkowski reduction `g(center,M=0)-eta=0` over Q, signature (1,3); diag(9,9,18,18)/det 26244; slice det form reproduced | SETU-02, VALD-02 | 70-02 Tasks 1,2 | COVERED (see Note B: reduction gate is tautological-by-construction; benchmark carries the real content) |
| SC4: h_2(C_u) sub-slice = H^3 = SL(2,C)/SU(2), constant curvature -1 (Totaro) | VALD-03 | 70-02 Task 3 | COVERED (state-and-cite; full computation correctly deferred to Phase 71) |
| SC5: potential FIXED as -log det; spacetime sub-slice index map {17,18,19,26} + signature stated explicitly | (SETU-02) | 70-01 frontmatter + 70-02 Task 1 | COVERED |

No orphan criterion. The mandatory gates (CH + 324/324; three-ordering on non-associative data; diag(9,9,18,18)/26244; exact Minkowski reduction; H^3 = -1 stated) are all present as concrete tasks with exact-over-Q pass conditions.

---

## Notes (heed during execution; none block)

**Note A — the stated non-vacuity guard is itself vacuous-as-worded; fix the predicate (do not weaken the check).**
Plan 70-01 Task 3 step 2 and its disconfirming-observation assert non-vacuity as:
`Re((x1 x2) x3) - Re(x1 (x2 x3)) != 0`.
At `octonionic_points()[1]` this real-part associator is **0** (I reproduced it: `= 0`), so that exact assertion, written literally, would **fail** even though the data is genuinely non-associative. The data really is non-associative — the FULL associator is `[0, 8, 16, 12, 0, -28, -28, -4]` (nonzero in imaginary comps) — and the quantity that actually discriminates SSOT from buggy is the **association/commutator split** `Re((x2 x1) x3) - Re((x1 x2) x3) = 8` (→ +4 vs -4, ×2 in N ⇒ 16). Executor guidance: assert non-vacuity via either (i) the full associator `(x1·x2)·x3 - x1·(x2·x3) != 0` as an octonion (any component), or (ii) the discriminator `Re((x2 x1)x3) != Re((x1 x2)x3)` — NOT the real-part-only triple-product associator, which is 0 here. The plan's headline assertions (+4/+4/-4, off-by-16, SSOT/conj == CH, buggy != CH) are all correct and should stand; only the non-vacuity *predicate* needs this swap. (Do not "fix" it by switching points to make the real-part associator nonzero — at all three octonionic points it is 0; the right fix is the predicate.)

**Note B — `test-minkowski-reduction` is tautological by construction; lean on the Hessian benchmark for the real content.**
The plan defines `h := [restricted cone-Hessian] - [its value at center]`, so `g - eta = h = 0` at the center holds **identically**, regardless of whether the restricted Hessian is the intended object. That means a green `test-minkowski-reduction` alone does NOT certify an uncontaminated background — it only checks `Hess - Hess|center == 0`. The actual anti-contamination content rides on `test-hessian-benchmark` (diag(9,9,18,18)/26244, which I confirmed) and `test-index-map` (slice form `b·g/3 - p²/3 - q²/3`, confirmed). Executor guidance: keep all three; treat the Hessian benchmark + index-map as the load-bearing gates, and state plainly in the SUMMARY that the residual-zero is by-construction so it is not over-claimed as independent evidence. (The plan's own `uncertainty_markers` already flag the by-construction nature — good; just make sure the SUMMARY does not present residual=0 as the decisive uncontaminated-background proof.)

**Note C — informational, no action required for the gate.**
- LOCK 7b is cheap (0.5 s to build 324 brackets); the plan's "tens of seconds" estimate is conservative and the DomainMatrix fallback is unnecessary but harmless. No watchdog risk in Phase 70.
- The stale `.gpd/research/METHODS.md` / `PITFALLS.md` claim that `octonion_algebra.py` is the corrected SSOT is empirically wrong (its det_3 line 2178 uses `(x1 x2) x3`, which fails the CH/inner-derivation certificate). The plans correctly follow the contract/brief, not those files, and surface this in `uncertainty_markers`. Optionally correct those two files later so this does not re-bite a future phase.

---

## Verdict

**PASS_WITH_NOTES.** Strategy, coverage of all 5 success criteria and all 4 requirements (SETU-01, SETU-02, VALD-02, VALD-03), dependency/wave structure, convention-lock alignment (including the `2Re((x2 x1) x3)` ≡ `2Re(x2* x0* x1)` labeling and the BAN on `octonion_algebra.py`), and exact-over-Q discipline are all sound. Every decisive benchmark the plans encode — the CH + 324/324 F_4 certificate, the three-ordering reconciliation (+4/+4/-4, off-by-16 at point `[1]`), the Hessian `diag(9,9,18,18)`/det 26244, and the slice det form `b·g/3 - p²/3 - q²/3` — was reproduced EXACTLY over Q against the live engine and matches. Safe to execute, provided the executor heeds Note A (swap the non-vacuity predicate to the full associator or the association-order discriminator — the real-part-only triple-product associator is 0 at the chosen point) and Note B (the Minkowski-reduction gate is tautological-by-construction; the Hessian benchmark and index-map carry the real anti-contamination content).
