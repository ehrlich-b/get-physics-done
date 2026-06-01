# Phase 73 — Circularity Audit (VALD-05, per-equation provenance)

**Created:** 2026-06-01 (Plan 73-01; T3/T4 rows certified). **Completed by:** Plan 73-02 (the `G[g]` test rows — marked `TODO-73-02`).

**Purpose.** This is the VALD-05 per-equation provenance table. It certifies that every equation feeding the stress-energy tensor `T_mu_nu`, the coupling `kappa`, and (later, in 73-02) the Einstein test traces to *intrinsic* algebraic data — the engine `det_3` Freudenthal cross-term + `eta_bg` + the cubic norm — with **NO** GST Lagrangian / N=2 SUSY closure / `-R/2` / Weinberg soft-graviton import (`fp-import-supergravity`), **NO** `Ric`/`R`/`G` used to *define* `T` and **NO** per-point `kappa` tuning (`fp-assume-einstein`), and **NO** entropy-area / `δQ = T dS` / Unruh-temperature step (`fp-ensemble-gravity`).

This is the DERV-03 discipline made auditable: `T` and `kappa` are FROZEN from intrinsic cross-term data **before** `G_mu_nu[g]` is ever computed (73-02). Building `T` after seeing `G` would beg the question; this table is the certificate that we did not.

**Conventions (locked, v17.0).** Natural units, EXACT over Q; spacetime metric `g = eta_bg + h(x;M)`, mostly-minus; `eta_bg` = constant null-aligned KKT pullback `[[0,1/2,0,0],[1/2,0,0,0],[0,0,-1,0],[0,0,0,-1]]`; box `= eta_bg^{ab} d_a d_b = 4 d_beta d_gamma - d_p^2 - d_q^2` (built from `eta_bg^{-1}`, never a hard-coded diag); cross-term `2Re((x2 x1)x3)`, SSOT = `code/bulk_geometry_verification.py det_3` (`octonion_algebra.py` BANNED); `Lambda = 0` (M=0 vacuum flat-DERIVED, NO `Lambda` tripwire).

---

## The SUBTLE TRAP (why this audit exists)

The slice geometry **genuinely coincides** with Gunaydin–Sierra–Townsend (GST) very-special-real geometry: both are `Hess(-log N)` of the SAME cubic norm `N = det_3` of the Albert algebra `h_3(O)`, and the scalar manifold is `E_{6(-26)}/F_4` (26-dim). So it is tempting — and easy to do by accident — to read off GST's Einstein equation, its SUSY-fixed couplings, or the `-R/2` coefficient. **That is exactly the circularity the milestone exists to avoid** (`fp-import-supergravity`): the GST couplings are fixed by the *assumed* N=2 SUSY closure (the dead det/GST/Weinberg route's `-R/2` fixed by assumed SUSY).

**Therefore:** GST is cited for the GEOMETRY / ORIENTATION ONLY (acknowledging the slice IS very-special-real geometry). `T`, `kappa`, and the Einstein test are derived from intrinsic algebraic data alone — the engine `det_3` cross-term, `eta_bg`, and the cubic norm. The rows below certify this for each equation.

**The Jacobson route is named and REJECTED** (`fp-ensemble-gravity`, contrast only): Jacobson 1995 (`gr-qc/9504004`) derives `G_mu_nu = 8πG T_mu_nu` from `δQ = T dS` at local Rindler horizons with `S ∝` area (Bekenstein–Hawking) and `T =` Unruh temperature. This milestone uses NONE of it: the curvature and the stress tensor come from the algebra's own cubic-norm geometry, one observer, one off-center point.

---

## Provenance table — T3/T4 equations (Plan 73-01, CERTIFIED)

Legend: **Intrinsic?** = traces only to `det_3` cross-term + `eta_bg` + cubic norm (engine SSOT). **fp-import-supergravity** = no GST Lagrangian / SUSY closure / `-R/2` / Weinberg. **fp-assume-einstein** = no `Ric`/`R`/`G` used to DEFINE the object, no per-point `kappa`. **fp-ensemble-gravity** = no entropy-area / `δQ=TdS` / Unruh-T.

| # | Equation | Inputs | Intrinsic? | fp-import-supergravity | fp-assume-einstein | fp-ensemble-gravity |
|---|----------|--------|:----------:|:----------------------:|:------------------:|:-------------------:|
| **T3.a** | `psi(x;M) := 2Re((x2 x1) x3)` (PRIMARY cross-term scalar) | engine `det_3` cross-term SSOT (`oct_mul`, Fano `e1 e2 = e4`); slice coords `(beta,gamma,p,q)` from `_offcenter_subs`; matter `MATTER_L` in V_{1/2}, partner `BG_HALF` in V_0 | **YES** — the unique V_0↔V_{1/2} channel of the cubic norm | PASS (no GST/SUSY; `octonion_algebra.py` BANNED, `det_3` SSOT byte-identical to `ring_lemma_verification`) | PASS (no `Ric`/`R`/`G`; AST-guarded in `73-01-build-T-kappa.py` §3.3) | PASS (pure algebra; no horizon/entropy) |
| **T3.b** | `T_mu_nu[psi] = d_mu psi d_nu psi - (1/2) eta_bg_mu_nu (d psi)^2`, `(d psi)^2 = eta_bg^{-1}^{ab} d_a psi d_b psi` (PRIMARY) | `psi` (T3.a); `eta_bg`, `eta_bg^{-1}` (constant null-aligned KKT pullback) | **YES** — canonical flat-background scalar stress tensor on `eta_bg` | PASS | PASS (the `-(1/2)eta(dψ)²` is the SCALAR stress-tensor trace term, NOT the gravitational `-R/2`; no `Ric`/`R`/`G`) | PASS |
| **T3.c** | sigma multiplet `phi^a` = the 16 octonion components of `(x2 x1)` and `(x1 x3)` (ALTERNATIVE) | engine `det_3` `oct_mul` products; `_offcenter_subs` slice | **YES** — the natural F_4/Spin(9,1)-covariant V_{1/2} content | PASS | PASS (no `Ric`/`R`/`G`) | PASS |
| **T3.d** | `T_mu_nu[V_{1/2}] = G_ab d_mu phi^a d_nu phi^b - (1/2) eta_bg_mu_nu G_ab eta_bg^{-1}^{cd} d_c phi^a d_d phi^b`, `G_ab = delta_ab` (ALTERNATIVE) | `phi^a` (T3.c); `eta_bg`; target metric `G_ab = delta_ab` = the octonion Euclidean inner product (V_{1/2} norm bilinear) | **YES** — sigma-model stress tensor; `G_ab = delta` is the intrinsic V_{1/2} norm, NOT a GST coupling | PASS (`G_ab = delta` is the octonion norm, NOT the GST scalar-manifold metric `a_IJ = -(1/3)Hess ln N`) | PASS | PASS |
| **T3.e** | conservation: `d^mu T_mu_nu = (box psi)(d_nu psi) = 0` (and `sum_a (box phi^a)(d_nu phi^a) = 0`) | `T` (T3.b/d); `box` from `eta_bg^{-1}`; `box psi = 0`, `box phi^a = 0` (each cross-term scalar is LINEAR in the slice coords ⇒ harmonic) | **YES** — flat-background divergence; conserved EXACTLY (the on-shell `box psi = 0` holds identically because the channels are linear-in-slice ⇒ harmonic) | PASS | PASS (Bianchi-compatibility verified WITHOUT any `Ric`/`R`/`G`; conservation is an intrinsic property of `T`) | PASS |
| **T3.f** | `||M||→0` limit: `T → 0` (both candidates); V_1-only control: `T = 0` (V_1 alpha INERT) | `T(t·M_0)` as `t→0`; pure-alpha matter direction | **YES** | PASS | PASS | PASS |
| **T4.a** | R-SCALE `:= a_4 = 395268903/24010000` (the `t^4` leading coefficient of `R[g(t M_0)]`) | FROZEN Phase-72 rational (a NUMBER, the curvature scale) | **YES** (intrinsic curvature scale of `g`, from Phase 72) | PASS | **PASS — KEY ROW.** `a_4` is a FROZEN rational NUMBER (the `t^4` curvature *scale* at the ONE reference direction `M_0`), NOT a live `Ric`/`R`/`G` symbol call, NOT a per-point tensor fit. Using a single frozen scale to set a dimensionful coupling is scale-setting (like fixing `8πG` once), NOT reverse-engineering the tensor RHS. AST-guarded (no `Ric`/`Rscalar`/`spacetime_curvature_of_g` in the kappa code). | PASS |
| **T4.b** | T-SCALE `:=` `t^4` (PRIMARY) / `t^2` (ALTERNATIVE) leading coefficient of `tr_eta T = eta_bg^{-1}^{mu nu} T_mu_nu` at the center | `T` (T3.b/d); `eta_bg^{-1}` | **YES** — intrinsic stress-tensor scale | PASS | PASS (no `Ric`/`R`/`G`) | PASS |
| **T4.c** | `kappa := (R-SCALE) / (T-SCALE)` at the ONE reference direction `M_0`, then HELD FIXED. `kappa_psi = 32016781143/5929`; `kappa_sigma = 395268903/129850` | T4.a / T4.b | **YES** — ratio of two intrinsic scales | PASS (no GST/SUSY/Weinberg coupling) | **PASS.** `kappa` is ONE rational from ONE reference direction, frozen as a GLOBAL constant; NOT `-R/2` (`= -a_4/2 = -395268903/48020000`, verified distinct from both `kappa`), NOT a per-point fit. The 73-02 family test asks whether this SAME `kappa` works for ALL `(M,x)`; if it must be re-fit per direction, that is the "linear/leading" or "none" level, reported honestly. | PASS |

**HONEST FINDING carried to 73-02 (not forced):** the PRIMARY single-scalar `T[psi]` has `tr_eta T ~ t^4` — the SAME leading order as the curvature `R[g] ~ a_4 t^4` — so it is the **structurally-matched** candidate (a constant `kappa` compares like-for-like). The ALTERNATIVE sigma `T[V_{1/2}]` has `tr_eta T ~ t^2` (an ORDER MISMATCH vs the `t^4` curvature), because the sigma fields contain a `matter^1 × slice` piece (`~t^1`) whereas `psi` is `matter^2 × slice` (`~t^2`). 73-02 must read the sigma order-mismatch as a **disconfirming signal** for the sigma candidate; the structurally-favorable Einstein candidate is `T[psi]`. This is reported at true strength, neither inflated nor suppressed.

**CAN-FAIL outcome of the BUILD half (73-01):** `T` CAN be made symmetric, conserved (exactly, since the cross-term channels are linear-in-slice ⇒ harmonic ⇒ `box = 0`), vanishing at the flat `||M||→0` vacuum, and provably independent of any Einstein/G input (AST-guarded). **Therefore the Einstein test CAN be posed honestly in 73-02.** (Had `T` required a `Ric`/`R`/`G` input to be conserved, or been impossible to make conserved, this audit would instead record that no independent `T` exists and that the Einstein test cannot be posed — the milestone's `fp-assume-einstein` disconfirming observation. It did not.)

---

## Provenance table — 73-02 equations (PLACEHOLDER — `TODO-73-02`)

These rows are to be filled by Plan 73-02 (Task T4), after the FULL nonlinear `G_mu_nu[g]` is computed and the global `(kappa, Lambda)` family fit is run. The frozen `T` and `kappa` above are the INPUTS; `G_mu_nu[g]` is computed AFTER they are frozen (DERV-03).

| # | Equation | Inputs | Intrinsic? | fp-import-supergravity | fp-assume-einstein | fp-ensemble-gravity |
|---|----------|--------|:----------:|:----------------------:|:------------------:|:-------------------:|
| **C.a** | `G_mu_nu[g] = Ric_mu_nu[g] - (1/2) g_mu_nu R[g]` (the test LHS, FULL nonlinear, at O(\|\|M\|\|^4)) | `g = eta_bg + h`; Totaro `R_ijkl` with `C` from the difference potential, indices raised by `g^{-1}=(eta+h)^{-1}`; engine `spacetime_curvature_of_g` | `TODO-73-02` | `TODO-73-02` (cite Totaro Cor 2.3 + the validated engine; the curvature is intrinsic to `g`) | `TODO-73-02` (`G[g]` is the LHS computed AFTER `T`,`kappa` frozen — this is the test TARGET, not an input to `T`) | `TODO-73-02` |
| **C.b** | global `(kappa, Lambda)` fit: solve `G_mu_nu = kappa T_mu_nu + Lambda g_mu_nu` for GLOBAL constants over an `(M,x)` family | `G[g]` (C.a); FROZEN `T` (T3), FROZEN `kappa` (T4.c); `Lambda` fit (expected 0) | `TODO-73-02` | `TODO-73-02` | `TODO-73-02` (GLOBAL constants over the family; per-point tuning REJECTED; `kappa` was frozen in 73-01 BEFORE this fit) | `TODO-73-02` |
| **C.c** | honest-level decomposition (n=4 S / Weyl): exact / linear-in-leading-response / "curved but not Einstein-structured" | `G[g]` decomposition (`ricci_decomposition_n4`); the fit residual | `TODO-73-02` | `TODO-73-02` | `TODO-73-02` ("curved but not Einstein-structured" is an ACCEPTABLE result; do NOT force Einstein form) | `TODO-73-02` |

---

## Forbidden-proxy certification (contract IDs)

| Forbidden proxy (contract ID) | Status (73-01 BUILD half) | Certification |
|-------------------------------|---------------------------|---------------|
| **`fp-import-supergravity`** | **rejected** | No GST Lagrangian, no N=2 SUSY closure, no `-R/2` fixed by SUSY, no Weinberg soft-graviton theorem enters `T` or `kappa`. GST cited for GEOMETRY/ORIENTATION ONLY (the slice IS very-special-real geometry `E_{6(-26)}/F_4`, `a_IJ = -(1/3)Hess ln N` — acknowledged, NOT used as a coupling). The sigma target metric `G_ab = delta` is the octonion norm, NOT the GST scalar-manifold metric. AST-guarded in `73-01-build-T-kappa.py`. |
| **`fp-assume-einstein`** | **rejected** | NO `Ric`/`R`/`G` symbol USED in the construction of `T` or `kappa` (AST-guarded over the T-functions and the kappa statements; comment-mentions of the constraint are not code-uses). `a_4` is a FROZEN rational NUMBER (the curvature scale at ONE reference direction), NOT a live curvature call and NOT a per-point tensor fit. `kappa` is a GLOBAL constant frozen BEFORE `G[g]` is computed (DERV-03); `kappa != -R/2`. |
| **`fp-ensemble-gravity`** | **rejected** | No observers-make-gravity / Jacobson-style thermodynamic step. No `δQ = T dS`, no entropy-area, no Unruh temperature, no ensemble/observer-averaging. `T` and `kappa` come from the algebra's own cubic-norm geometry, one observer, one off-center point `M_0`. Jacobson 1995 named and rejected (contrast only). |
| **`fp-float-decisive`** (carried) | **rejected** | Every decisive quantity in 73-01 is EXACT over Q: `psi = 11p/6300 - 13/63000`, the `T` matrices, `kappa_psi = 32016781143/5929`, `kappa_sigma = 395268903/129850`, the order anchors (`box(hbar^(2))(0,0) = -76221/2450`, Lorenz defect `[19143/9800, 9747/4900, 297/350, 0]`). Ranks/signatures via sympy, never numpy float. |
| **`fp-wrong-cross-term`** (carried) | **rejected** | `psi` uses the engine `det_3` cross-term `2Re((x2 x1)x3)` (the F_4-invariant generic-norm factor order, Phase-64.1 fix), NOT `octonion_algebra.py` (BANNED) and NOT the real-only `2 d1 d2 d3`. `det_3` SSOT is byte-identical to `ring_lemma_verification`. |

---

## Engine / SSOT provenance

- **`det_3` cross-term SSOT** = `code/bulk_geometry_verification.py` (byte-identical to `code/ring_lemma_verification.py`; verified by the engine's `verbatim_copy_integrity` / `exact_only_guard_p70` LOCKs). `octonion_algebra.py` is BANNED on the decisive path.
- **`h2_field(x)` + `box`** added in `code/bulk_geometry_verification.py` Section 14 (Plan 73-01, Task 1); the engine still `ALL_PASS`, exit 0 after the extension.
- **`eta_bg`** = `J^T diag(+1,-1,-1,-1) J` with `J = _frame_jacobian_bg_to_mink` (52-kkt frame); CONSTANT, null-aligned; the box and trace-reverse are built from `eta_bg^{-1}`, never a hard-coded `diag(-1,1,1,1)`.
- All 73-01 computations: `.gpd/phases/73-c-einstein-structure/73-01-build-T-kappa.py` (exact over Q; `BUILD_T_KAPPA_OK`, exit 0).

---

_Phase 73-01 (BUILD): T3/T4 rows CERTIFIED. Phase 73-02 (TEST): completes the C.a/C.b/C.c rows after the full-`G[g]` Einstein test._
