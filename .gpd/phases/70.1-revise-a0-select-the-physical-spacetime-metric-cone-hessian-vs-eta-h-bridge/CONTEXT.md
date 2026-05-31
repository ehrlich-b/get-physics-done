# Phase 70.1: Context

## Revision of Phase 70

This phase supersedes **Phase 70 (A0 — Engine Reconciliation & Signature Bridge)**. It does **not** rebuild the engine — it resolves the one load-bearing decision Phase 70 left underdetermined: **which object is the physical spacetime metric?**

### Revision trigger

Phase 70 locked the signature bridge as construction (ii) `g_mu_nu(x) = eta_mu_nu + h_mu_nu(x)` (η from `h_2(C_u)`'s own `det_2`; the cone-Hessian supplies only `h_mu_nu`) and honestly flagged its Minkowski-reduction gate as *tautological-by-construction*. It never confronted the deeper question of whether the cone-Hessian itself, or the `η+h` bridge, is THE gravitational field.

Phase 72's first-result gate (the matter-sourcing KILL test) then computed the M=0 **cone-Hessian** vacuum exactly over Q and found it is the **non-Einstein static product `R_time × H³`**:

- `Hess(−log det_3)|_{I/3}` (4-dim spacetime sub-slice) = `diag(9,9,18,18)`, Ricci endomorphism eigenvalues **`{0,−1,−1,−1}`**, `R = −3` (matches the Phase-71 anchor) — but Einstein in n=4 needs all eigenvalues `= R/4 = −3/4`, so the vacuum is **NOT Einstein**.
- The eigenvalue-0 direction `(1,1,0,0) = β+γ` is the **timelike `x_0`** under `h_2(C_u) ≃ R^{3,1}` (det_2 Minkowski form `βγ/3 − p²/3 − q²/3`; the `βγ/3` block is the hyperbolic 1+1 part, `(1,1)` its timelike eigenvector). So M=0 is `R_time × H³_space` — the flat factor is *time* — with `K(p,q) = −1/2`.

**A GR Λ-vacuum must be Einstein (`Ric ∝ g`).** No baseline subtraction turns a non-Einstein vacuum into an Einstein one, so "which Λ reference?" presupposes a maximally-symmetric vacuum this construction does not produce. **The non-Einstein vacuum IS the result** (negative-result-is-success). The cone-Hessian (thesis metric) and `η+h` bridge therefore disagree about the M=0 geometry → the construction-(ii) bridge is underdetermined (the Riemannian/Lorentzian tension already flagged in `CONVENTIONS.md`).

### What worked in the original phase (inherited unchanged)

- **`code/bulk_geometry_verification.py`** — certified SSOT cubic-norm engine. `det_3` (cross `2Re((x2 x1) x3)`) byte-identical to `ring_lemma_verification.det_3` (sha256 `e43d6a3f…`, LOCK 0); = Cayley-Hamilton norm at 3 octonionic points (LOCK 7a); annihilated by 324/324 inner derivations (LOCK 7b). ALL_PASS, exit 0. **Reuse — do NOT rebuild.**
- **Hessian benchmark:** `Hess(−log det)|_{I/3}|_{x1,x2,x3,x10}` = `diag(9,9,18,18)`, det `26244` (nondegenerate, positive-definite Riemannian bulk).
- **Index map:** `det_3|_{x1,x2,x3,x10}(α=1/3)` = `βγ/3 − p²/3 − q²/3`; spacetime sub-slice `{17,18,19,26} ≡ {x1,x2,x3,x10}` (internal W-sector `{20..25}` excluded).
- **Lorentzian background:** `η = diag(+1,−1,−1,−1)` from `h_2(C_u)`'s own `det_2` (52-kkt); mostly-minus signature (1,3).
- **VALD-03:** det=1 hyperboloid = `H³ = SL(2,C)/SU(2)`; Totaro target `−1`; Phase-71 cone-Hessian-slice value `−1/2` (benign factor-of-2 vs round metric; sign pinned negative).
- **Construction (i) rejection** (Wick-rotate via u=e_7; unproven C\*-bottleneck signature-flip conjecture + Visser arXiv:1702.05572 chart-dependence) — **still stands.** The reopened choice is NOT a return to (i).

### What did not work

Phase 70 made construction (ii) a **fixed modeling choice** rather than a derived/decided result, and deferred "does (ii) preserve the V_1/V_{1/2} matter coupling?" to later phases. Because the cone-Hessian (the route's own thesis object) gives a non-Einstein M=0 vacuum, the choice of physical metric is now load-bearing and can no longer be left implicit: the M=0 geometry differs between the two candidates (cone-Hessian → `R×H³`; `η+h` → flat).

### What to do differently — the one well-posed question

**Decide which object is the physical spacetime metric and restate the route thesis accordingly.** Exactly two admissible outcomes:

1. **Cone-Hessian (the thesis metric).** M=0 vacuum is non-Einstein `R×H³` → the route does NOT yield GR-with-a-Λ-vacuum. The strongest honest claim becomes **linearized matter-response (spin-2) on a FIXED non-Einstein `R×H³` background** — named as such, never relabeled "GR derived." Phase 72 then re-plans as a linearized-perturbation measurement on this fixed background.
2. **`η+h` bridge.** The thesis is wrong as stated → restate it (show why the *bridge metric*, not the cone curvature, is the gravitational field). Flatness at center is GR's correct empty vacuum, but `Λ=0` is *inserted* by center-subtraction, not derived → carry that **circularity tripwire into Phase 73**. Reconciliation (b) becomes the reference.

**Discipline (binding):**
- Exact over Q. No float on any decisive verdict.
- Do **NOT** insert any factor to force `Ric ∝ g` or to force flatness — that corrupts the verdict it feeds.
- `det_3` stays the single source of truth (`code/bulk_geometry_verification.py`; never `octonion_algebra.py`).
- Headline the Ricci spectrum `{0,−1,−1,−1}`.
- **Do NOT** adopt the rejected reconciliation (a) "Einstein on the det₂=1 H³ leaf" — it drops the timelike `x_0` direction and swaps spacetime for a 3-dim spatial slice (`fp-relabel`). Quotienting the dilation/timelike direction is the same move, likewise forbidden.

### Inherited decisions (carry forward, do not re-litigate)

- Potential FIXED as `−log det` (Faraut-Korányi); `g_X = Hess(−log det)` positive-definite (Riemannian) — which is *why* a Riemannian→Lorentzian bridge is needed at all.
- `det_3` cross-term `2Re((x2 x1) x3)` SSOT; buggy `(x1 x2) x3` forbidden (`fp-wrong-cross-term`).
- Engine-native layout; center `I/3` (ρ_J = 0); Minkowski coords `x0=(β+γ)/2, x3=(β−γ)/2`.
- Construction (i) rejected (see above).

### Requirements mapping (inherited from Phase 70)

- **SETU-01** (single certified det_3 engine) — SATISFIED by the inherited engine; not re-opened.
- **SETU-02** (signature bridge stated, reduces to exact Minkowski at M=0/center) — **REOPENED**: the bridge's *physical-metric selection* is the subject of this phase; the Minkowski-reduction mechanics are inherited.
- **VALD-02** (Hessian benchmark diag(9,9,18,18)/det 26244) — SATISFIED; inherited.
- **VALD-03** (H³ = SL(2,C)/SU(2), Totaro curvature) — SATISFIED; inherited.

The decisive new obligation is the **metric-selection verdict** plus the **restated thesis** and the explicit propagation of its consequence (linearized-only on a fixed non-Einstein background, OR `Λ=0`-tripwire) to Phases 72/73.

### Reference

- Superseded phase: `.gpd/phases/70-a0-engine-reconciliation-signature-bridge/`
- Original summaries: `…/70-01-SUMMARY.md` (engine), `…/70-02-SUMMARY.md` (signature bridge)
- Supersession record: `.gpd/phases/70-a0-engine-reconciliation-signature-bridge/SUPERSEDED.md`
- The triggering finding: `derivations/72-matter-sourcing.tex` (§adjudication `sec:adjudication`, §reopened-task `sec:phase70-task`)
- Recovery doc: `.gpd/phases/72-b-matter-sourcing/PHASE-RECOVERY.md`
- Exact reproduction: `.gpd/phases/72-b-matter-sourcing/72-01-baseline-probe.py` (exact over Q, 3.4s, exit 0)
- Convention tension: `.gpd/CONVENTIONS.md` (Riemannian bulk vs Lorentzian slice; "Riemann/Ricci sign — STATE EXPLICITLY at Phase 70")

### Next step

`/gpd:plan-phase 70.1` (fresh context) — break the metric-selection verdict into atomic, exact-over-Q tasks. The engine is warm; this phase is short and decisive (a selection + thesis restatement + consequence propagation), not a rebuild.
