# Research State

## Project Reference

See: .gpd/PROJECT.md (updated 2026-05-30)

**Machine-readable scoping contract:** `.gpd/state.json` field `project_contract` (v17.0 — Gravity as Intrinsic Curvature of the h_3(O) Bulk Geometry; schema v1, 4 claims, 6 acceptance tests, 11 references; set 2026-05-30)

**Core research question:** Can the Standard Model + GR be derived from the requirement that a composite system faithfully models itself? — v17.0 attacks the GR half via a fresh, intrinsic route.
**Current focus:** v17.0 Phase 70 (A0 — Engine Reconciliation & Signature Bridge)

## Current Position

**Current Phase:** 70
**Current Phase Name:** A0 — Engine Reconciliation & Signature Bridge
**Total Phases:** 4 (Phases 70-73)
**Current Plan:** 1
**Total Plans in Phase:** TBD
**Status:** Ready to plan
**Last Activity:** 2026-05-30
**Last Activity Description:** v17.0 roadmap CREATED (Phases 70-73; gated A0 → A KILL gate → [STOP if homogeneous] → B → C). 15/15 requirements mapped, 4/4 contract claims surfaced. Phase 70 (A0) ready to plan. Physics-side; independent of the v16.0 consciousness-side (RING) line — do not entangle.

**Progress:** [░░░░░░░░░░] 0%

## Milestone Shape (read first)

v17.0 is a **gated KILL test**, NOT an open-ended exploration. The claim: the positive cone of h_3(O) is an intrinsically-curved Riemannian symmetric space with canonical metric `g_X = Hess(-log det X)`; a primitive idempotent E_11 picks the spacetime slice `V_0 superset h_2(C_u) ~ R^{3,1}`, an off-center state picks a basepoint, and gravity is the curvature the slice inherits from the bulk, sourced by matter `M in V_1/V_{1/2}` via the cubic-norm cross-terms. **NO lattice, NO posited supergravity Lagrangian, NO SUSY, NO observers-make-gravity ensemble argument.** Fresh route replacing the abandoned lattice/Fisher route and the circular det/GST/Weinberg supergravity route.

- **Phase 70 (A0):** certify a single det_3 engine; fix the construction-(ii) signature bridge; reduce to exact Minkowski at (M=0, center).
- **Phase 71 (A — THE KILL GATE, cheap, FIRST):** is `h_mu_nu(x)` genuinely position-dependent (route SURVIVES) or x-independent/homogeneous (route DEAD)? A homogeneous result is a clean valuable KILL — report and STOP (NEGATIVE-RESULT-IS-SUCCESS).
- **Phase 72 (B — CONDITIONAL on A):** does matter `M` source the slice curvature via the cross-terms (cross-term on/off; ||M|| scaling)?
- **Phase 73 (C — CONDITIONAL on B):** at what honest level does `G_mu_nu = kappa T_mu_nu + Lambda g_mu_nu` hold? "Curved but not Einstein" is an acceptable full result.

## Active Calculations

None yet (Phase 70 not started). v17.0 reuses the warm exact-SymPy h_3(O) engine (`code/ring_lemma_verification.py`, `code/embedding_under_E_verification.py`).

[Carried-forward calculations from prior milestones (det_3, d_{IJK}, KKT, MESGT, etc.) preserved in `.gpd/state.json` field `active_calculations` — not active for v17.0.]

## Intermediate Results

No v17.0 results yet. Load-bearing benchmarks the milestone must reproduce (from the literature survey; measured this session):

- Slice (h_2(C_u)) cubic norm at center: slice det = `b*g/3 - p^2/3 - q^2/3` (Minkowski form); `Hess(-log det)` at I/3 = `diag(9,9,18,18)`, det 26244. [HIGH; COMPUTATIONAL.md + 52-kkt-spacetime]
- H^3 = SL(2,C)/SU(2) det=1 sub-slice (M=0 limit): constant negative curvature `-d^2/4 = -1` (d=2, rank-1). [HIGH; Totaro 2004 Cor 2.3]
- Center X=I/3 (irreducible symmetric space): Einstein with NEGATIVE Ricci ∝ g (Cartan); Lambda < 0. [HIGH; Totaro 2004, Faraut-Koranyi 1994]
- Single-copy orbit/stabilizer anchor (Phase-71 engine calibration): orbit dim 24 / Spin(8) stabilizer dim 28. [HIGH; orbit_dimension_gate.py, ALL_PASS]
- Associator gap between det conventions on octonionic data: 0.67 (engine det 24.978 vs buggy (x1 x2) x3 order 24.306) — the conventions to reconcile at A0. [HIGH; COMPUTATIONAL.md, measured]

## Open Questions

v17.0 open questions (from the literature survey; each gates a phase):

1. [HIGH — blocks Phase 71] Is `h_mu_nu(x)` genuinely x-dependent after fixing E_11 (KILL vs GREENLIGHT)? Settled by curvature-invariant x-dependence + the `Stab_{E_6}(E_11)`-orbit vs basepoint-family dimension count, exact over Q.
2. [HIGH — blocks Phase 71] Is the V_0 slice totally geodesic (II = 0 => bulk-constant curvature => KILL)? Kollross-Rodriguez-Vazquez Table 7 says probably not, but must be computed (and V_0 not-inside the larger geodesic submanifolds ruled out).
3. [HIGH — Phase 70 decision] Which signature construction reduces exactly to Minkowski at (M=0, center)? Construction (ii) measured to give the Minkowski det directly; the reduction gate decides.
4. [MEDIUM — blocks Phase 72 verdict] Is the V_0-block curvature controlled by the MIXED cross-terms `C_{(V_0)(V_1)(V_{1/2})}` vs the pure `C_{(V_0)^3}`? Determines whether matter genuinely sources via cross-terms (off-switch test).
5. [MEDIUM — Phase 73] Does `G_mu_nu ∝ T_mu_nu` for any natural cross-term-built `T_mu_nu`? Honest prior: "curved, possibly not Einstein."
6. [LOW] Does dim-10 V_0 curvature ever need exact computation (symbolic inverse times out)? Off the critical path; mpmath fallback exists.

[Resolved prior-milestone open questions preserved in `.gpd/state.json` field `open_questions`.]

## Performance Metrics

| Label | Duration | Tasks | Files |
| ----- | -------- | ----- | ----- |
| -     | -        | -     | -     |

[Per-plan metrics from prior milestones preserved in `.gpd/state.json` field `performance_metrics`.]

## Accumulated Context

### Decisions

Full log: `.gpd/DECISIONS.md`

**Recent high-impact (v17.0 roadmap):**
- [v17.0 roadmap]: Gated A0 → A KILL → B → C chain (Phases 70-73). Phase 71 (homogeneity) is the cheap decisive KILL gate run FIRST (after A0); B/C conditional on A surviving. A homogeneous Phase-71 result is a clean valuable KILL that terminates the milestone (NEGATIVE-RESULT-IS-SUCCESS).
- [v17.0 roadmap]: Signature bridge FIXED as construction (ii) (eta from h_2(C_u) det + cone-Hessian perturbation), reducing to exact Minkowski at center; construction (i) (Wick-rotate via u) is the rejected fallback (carries a separate unproven C*-bottleneck signature-flip conjecture; naive coordinate Wick rotation on a curved metric manufactures spurious curvature, Visser).
- [v17.0 roadmap]: det single source of truth = `code/ring_lemma_verification.py` `det_3` (cross-term `2Re(x2* x0* x1)`, certified F_4-invariant via CH + 324/324); do NOT import `code/octonion_algebra.py` (buggy `(x1 x2) x3` order, float-only, 0.67 associator gap).
- [v17.0 roadmap]: Curvature engine = Totaro's closed form (3rd derivatives of det only; det cubic => f_ijkl=0), hand-rolled Christoffel/Riemann (beats sympy.diffgeom; ~19s exact on dim-4 slice). Decisive physics on the dim-4 h_2(C_u) slice; dim-10 V_0 off the critical path.

### Active Approximations

| Approximation | Validity Range | Controlling Parameter | Current Value | Status |
| ------------- | -------------- | --------------------- | ------------- | ------ |
| Perturbative expansion around center I/3 | small matter / near-center; jet terminates (det cubic) | \|\|M\|\|, rho_J(X_bg) | — (not started) | Planned (Phase 72) |
| Dim-4 h_2(C_u) slice (decisive) vs dim-10 V_0 | symbolic inverse tractable on dim-4 (~19s); dim-10 times out (>200s) | slice dimension | dim-4 | Active (dim-10 = mpmath fallback only, off critical path) |

**Convention Lock (v17.0 — to be formalized in CONVENTIONS.md by gpd-notation-coordinator):**

- Metric signature: mostly-minus (Lorentzian slice via det_2); bulk cone Riemannian (positive-definite). [v16.0's Riemannian-Fisher sign convention is RETIRED — that was the abandoned lattice route.]
- Natural units: ħ = c = k_B = 1; **exact rational arithmetic over Q (NOT float) on all decisive verdicts**
- Jordan product: (1/2)(XY + YX); Tr(X o Y) = Re Tr(XY) for Hermitian X,Y
- Octonion basis: Fano, e1*e2 = e4
- Complex structure: u = e7 (C_u = span{1, e7})
- Cubic norm / det: Freudenthal det WITH cross-terms, order `2Re(x2* x0* x1)` (engine `ring_lemma_verification.det_3`, single source of truth); polarization LOCKED `d(X,X,X) = 6 det`
- Cone metric: `g_X(A,B) = -d_s d_t log det(X+sA+tB)|_0 = Hess(-log det)`; inverse `g^{pq} = P(X)` (quadratic representation, Faraut-Koranyi)
- Potential: `-log det` (FIXED at start; do NOT mix with `det`)
- Primitive idempotent: E_11 = diag(1,0,0); center = I/3 (F_4-symmetric point, rho_J = 0)
- Peirce: V_1(1) = R·E_11, V_{1/2}(16), V_0(10) = h_2(O); spacetime sub-slice = h_2(C_u) (4-dim), indices {17,18,19,26}
- Riemann/Ricci sign convention: state explicitly and benchmark on H^3 (const curvature -1) at Phase 70
- Curvature engine: Totaro `R_ijkl = -(1/4) g^{pq}(f_jlp f_ikq - f_ilp f_jkq)` (3rd derivatives only)
- kappa, Lambda: fitted in Phase 73 as GLOBAL constants; Lambda != 0 (background Einstein-negative)
- Group: F_4 = Aut(h_3(O)) (compact, 52-dim) fixes det; E_6 = Stab(det) (the cone's isometry-relevant group); Stab_{E_6}(E_11) is the residual after fixing the slice (parabolic, Levi ~ Spin(9,1))
- Arithmetic: ranks via `sympy.Matrix.rank()`, NEVER `numpy.linalg.matrix_rank`; warm engine = `ring_lemma_verification.py` + `embedding_under_E_verification.py`
- All other convention fields: see `.gpd/CONVENTIONS.md`

### Propagated Uncertainties

| Quantity | Current Value | Uncertainty | Last Updated (Phase) | Method |
| -------- | ------------- | ----------- | -------------------- | ------ |
| —        | —             | —           | —                    | exact over Q (exact symbolic differential geometry — no statistical error to propagate) |

### Pending Todos

None yet for v17.0.

### Blockers/Concerns

- **[Phase 70 prerequisite] det convention reconciliation.** Three in-repo det conventions disagree by a measured 0.67 associator gap on octonionic data; MUST be reconciled on genuinely NON-associative (e_4..e_7) data before any geometry (a check on e_0..e_3 quaternionic data is vacuous). Single source of truth = `ring_lemma_verification.det_3`; do NOT import `octonion_algebra.py`. [SETU-01]
- **[Phase 70] signature bridge gate.** A bridge that fails to reduce to EXACT Minkowski at (M=0, center) contaminates h_mu_nu with a constant offset masquerading as Lambda or position-dependence. Enforce `g(center, M=0) = eta` exactly; never "rotate the answer".
- **[Phase 71 risk] self-deception at the KILL gate.** The Phase-A verdict leans GREENLIGHT (V_0 slice absent from the Kollross-Rodriguez-Vazquez Table-7 maximal-totally-geodesic list) but is an INFERENCE that MUST be computed. Decide on coordinate-invariant curvature SCALARS as functions of x at >= 2 basepoints PLUS the exact stabilizer-orbit count — NEVER metric components or a single basepoint. The exact `Stab_{E_6}(E_11)` (parabolic, Levi ~ Spin(9,1)) is not cleanly tabulated — likely needs direct kernel computation `{D in e_6 : D*E_11 = 0}` or `/gpd:research-phase`.
- **[Phase 72 cost] symbolic matrix inverse cliff.** Symbolic inverse with matter+coords all symbolic times out (>200s); mitigation (works): substitute matter to rationals before inverting, keep 4 slice coords symbolic, series-expand in a single matter amplitude. Executor stream-watchdog ~150s silent-kill (hard 600s) — run foreground `python -u` with progress prints between heavy steps.
- **[Phase 73 risk] circularity trap.** The slice geometry coincides with GST special-real geometry, so ANY GST/SUSY/-R/2/Weinberg formula silently re-imports the assumed Einstein structure. Hard input ban (declared at Phase 70); cite GST for the MANIFOLD only; define T_mu_nu, kappa from cross-terms BEFORE computing G_mu_nu; per-equation circularity audit (VALD-05).
- **[provenance] prompt-named files.** `peirce_coupling.py` / `h3o_tower.py` / `rho_directional_derivatives.py` may be absent or superseded in `code/`; confirm file provenance at Phase 70 — the engine (`ring_lemma_verification.py` + `embedding_under_E_verification.py`) is the single source of truth regardless.
- **Do NOT entangle with the consciousness-side line.** v17.0 is physics-side and INDEPENDENT of the v16.0 (RING) lemma and the v15.0 basin-restriction result; neither bears on the bulk-geometry claim.
- **Use LIVE sources only** (`~/repos/blog/...`), NOT stale repo `papers/` copies.
- v14.0 PAUSED (pending JMP referee report); resumption triggers and full inventory in `.gpd/V14-CLOSEOUT.md`. Not a v17.0 blocker.

## Session Continuity

**Last session:** 2026-05-30 (v17.0 roadmap creation)
**Stopped at:** v17.0 roadmap created (Phases 70-73, gated A0 → A KILL → B → C). Phase 70 (A0) ready to plan; project_contract (4 claims, 6 acceptance tests, 11 references) preserved in state.json.
**Resume file:** Next action — `/gpd:plan-phase 70` (A0: engine reconciliation + signature bridge). Recommend running `gpd-notation-coordinator` first to refresh `CONVENTIONS.md` for the cone-metric / construction-(ii) signature-bridge / mostly-minus / det-engine notation before planning. v14.0 PAUSED.
