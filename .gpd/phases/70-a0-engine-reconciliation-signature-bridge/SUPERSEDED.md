# Phase 70: SUPERSEDED

**Superseded by:** Phase 70.1 (Revise A0 — select the physical spacetime metric: cone-Hessian vs η+h bridge)
**Date:** 2026-05-31
**Original completion:** 2026-05-30
**Reason:** The construction-(ii) signature bridge is **underdetermined**. Phase 70 *adopted* `g = η + h` as a modeling choice (with the Minkowski-reduction gate honestly flagged tautological-by-construction) but never confronted *which object is the physical spacetime metric*. Phase 72's first-result gate then found the M=0 **cone-Hessian** vacuum is the non-Einstein static product `R_time × H³` (Ricci endomorphism eigenvalues `{0,−1,−1,−1}`, `R=−3` but NOT Einstein). The Riemannian cone-Hessian (the route thesis "gravity = curvature of the cone-Hessian") and the Lorentzian `η+h` bridge **disagree about the M=0 geometry** — so the bridge is underdetermined and the metric-selection question must be resolved before any matter-sourcing verdict.

## What was learned (still stands — this phase's engine is faithful)

Phase 70 stood up the certified cubic-norm engine and a Lorentzian background, all exact over Q:

- **`code/bulk_geometry_verification.py`** — a self-contained SSOT engine whose `det_3` (cross-term `2Re((x2 x1) x3)`) is **byte-identical** to the v16.0 `ring_lemma_verification.det_3` (sha256 `e43d6a3f…`, LOCK 0), equal to the Cayley-Hamilton generic norm at 3 octonionic points (LOCK 7a), and annihilated by **324/324** inner derivations (LOCK 7b, dim f_4 = 52). `fp-wrong-cross-term` rejected with exact evidence (buggy ordering off-by-16). ALL_PASS, exit 0.
- **Hessian benchmark:** `Hess(−log det)|_{I/3}` restricted to the 4 spacetime sub-slice coords `{x1,x2,x3,x10}` = `diag(9,9,18,18)`, det `26244` (nondegenerate, positive-definite Riemannian).
- **Index map:** `det_3|_{x1,x2,x3,x10}(α=1/3)` = `βγ/3 − p²/3 − q²/3`, asserting the spacetime sub-slice `{17,18,19,26} ≡ {x1,x2,x3,x10}` and excluding the internal W-sector `{20..25}`.
- **VALD-03:** the det=1 hyperboloid in `h_2(C_u)` is `H³ = SL(2,C)/SU(2)` (Totaro target curvature `−1`; cone-Hessian-slice value later benchmarked at `−1/2` in Phase 71 — benign factor-of-2, sign pinned negative).

The engine is **not** what broke: all 4 Phase-71 regression anchors and the Phase-72 baseline probe reproduce exactly over Q. Phase 71's homogeneity verdict (SURVIVES — the cone-Hessian slice metric is genuinely position-dependent) was built on this engine and **continues to hold**.

## What is being changed

The single load-bearing **decision** that Phase 70 left underdetermined:

> *Which object is the physical spacetime metric — the Riemannian cone-Hessian, or the Lorentzian `η+h` bridge?*

Phase 70 locked construction (ii) (`g = η + h`) as THE bridge without resolving that the cone-Hessian (the route's own thesis metric) gives a **non-Einstein** `R×H³` M=0 vacuum while `η+h` (by center-subtraction) gives a flat one. The two metrics genuinely disagree about the empty-vacuum geometry. Phase 70.1 makes this choice explicitly and **restates the route thesis accordingly**:

- **If cone-Hessian (the thesis):** M=0 vacuum is non-Einstein `R×H³` → the route does NOT yield a GR-with-Λ vacuum; the most it can claim is **linearized spin-2 matter-response on a FIXED non-Einstein `R×H³` background** — a strictly weaker result, named as such, never relabeled "GR derived."
- **If `η+h` bridge:** the thesis is wrong as stated and must be restated (why the bridge metric, not the cone curvature, is the gravitational field); `Λ=0` is then *inserted* by center-subtraction → a circularity tripwire to carry into Phase 73.

**Discipline (binding):** exact over Q; do **not** insert any factor to force `Ric ∝ g` or to force flatness (that corrupts the verdict it feeds); `det_3` stays the single source of truth; the headline is `{0,−1,−1,−1}`. A non-Einstein M=0 vacuum **is the negative result** (negative-result-is-success) — it is NOT to be papered over with a "which Λ reference" baseline choice.

## What remains valid (carried forward to Phase 70.1)

- The certified SSOT engine `code/bulk_geometry_verification.py` (det_3, CH-norm + 324/324, Hessian benchmark, index map) — **reused unchanged**.
- `fp-wrong-cross-term` rejection; the V_0↔V_{1/2} cross-term channel `2·Re((x2 x1) x3)`.
- The Lorentzian background `η = diag(+1,−1,−1,−1)` from `h_2(C_u)`'s own `det_2` (52-kkt); the index map `{17,18,19,26}`; the `H³ = SL(2,C)/SU(2)` identification and Totaro target `−1`.
- The rejection of construction (i) (Wick-rotate via u=e_7; unproven C\*-bottleneck signature-flip + Visser chart-dependence) — **stands**; the reopened choice is between the cone-Hessian itself and construction (ii), NOT a return to (i).

## Rejected reconciliations (do NOT reopen as escape hatches)

- **(a) "Einstein on the det₂=1 H³ leaf" — REJECTED (`fp-relabel`).** Drops the flat=timelike `x_0` direction; H³ is the wrong symmetric space and one dimension short (GR's empty hyperbolic-slice vacuum is Milne = flat Minkowski, not H³). Quotienting the dilation/timelike direction is the same move, likewise rejected.
- **(b) "`η+h` is the decisive metric" — CONDITIONAL, not free.** Admissible only if Phase 70.1 explicitly rules `η+h` (not the cone-Hessian) is THE spacetime metric and restates the thesis, carrying the built-in `Λ=0` tripwire to Phase 73.

## Reference

- Original plans/summaries: `.gpd/phases/70-a0-engine-reconciliation-signature-bridge/70-01-*.md`, `70-02-*.md` (UNCHANGED — historical record)
- The finding that triggered the revision: `derivations/72-matter-sourcing.tex` (§adjudication, §phase70-task) and `.gpd/phases/72-b-matter-sourcing/PHASE-RECOVERY.md`
- Reproduction: `.gpd/phases/72-b-matter-sourcing/72-01-baseline-probe.py` (3.4s, exact over Q, exit 0)
- Replacement phase context: `.gpd/phases/70.1-revise-a0-select-the-physical-spacetime-metric-cone-hessian-vs-eta-h-bridge/CONTEXT.md`
