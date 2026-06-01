# Research Roadmap: v17.0 — Gravity as Intrinsic Curvature of the h_3(O) Bulk Geometry (Experiential Measure on Structure Space)

## Overview

A fresh, intrinsic route to gravity, replacing two dead routes (the abandoned lattice/Fisher continuum limit and the circular det/GST/Weinberg supergravity Lagrangian). The positive cone of h_3(O) is a Riemannian symmetric space with canonical metric `g_X = Hess(-log det X)` (Faraut-Koranyi); a primitive idempotent E_11 picks the spacetime Peirce slice `V_0 superset h_2(C_u) ~ R^{3,1}`, and an off-center state picks a basepoint. The milestone decides — by a **cheap homogeneity KILL test run FIRST** — whether the slice inherits a genuinely position-dependent metric `g_mu_nu(x)`, and if so whether its curvature is sourced by matter `M in V_1/V_{1/2}` through the cubic-norm cross-terms, up to Einstein structure. NO lattice, NO posited Lagrangian, NO SUSY, NO observers-make-gravity ensemble argument. This is a gated KILL test, not an open-ended exploration: a decisive verdict either way is a full pass.

## Milestones

- **v1.0-v13.0** — Phases 1-53 (archived under `.gpd/milestones/`)
- **v14.0 Paper 5 Revision** — Phases 54-59 (PAUSED 2026-04-17, pending JMP referee report; see `.gpd/V14-CLOSEOUT.md`)
- **v15.0 The P5 <-> Basin Restriction Lemma** — Phases 60-63 (completed 2026-05-24 — CHARACTERIZED OBSTRUCTION / coexistence-as-island)
- **v16.0 The (RING) Lemma** — Phases 64-69 (completed 2026-05-27 — (RING) (a)+(b)+(c) PROVED)
- **Active: v17.0 Gravity as Intrinsic Curvature of the h_3(O) Bulk Geometry** — Phases 70-73 (physics-side; independent of the v16.0 consciousness-side line — do not entangle)

## Contract Overview

The machine-readable project contract lives in `.gpd/state.json` field `project_contract` (schema v1, 4 claims, 6 acceptance tests). The 4 decisive claims map to phases as follows.

| Contract Item | Advanced By Phase(s) | Acceptance Tests | Status |
| ------------- | -------------------- | ---------------- | ------ |
| **claim-signature-bridge** — re-adjudicated at Phase 70.1 to: WHICH object is the physical spacetime metric (cone-Hessian vs η+h) | Phase 70 (A0, superseded) → **Phase 70.1 (RESOLVED)** | test-minkowski-reduction, test-cross-term-association, test-spectrum-einstein, test-selection-decidable | **RESOLVED at Phase 70.1 (2026-05-31, verified 5/5 HIGH): the η+h bridge is the physical spacetime metric; the "cone-Hessian IS the metric" thesis is FALSIFIED (non-Einstein R×H³ {0,−1,−1,−1}). Flat vacuum DERIVED from KKT det₂ (not inserted). Route restated (cone-Hessian = matter source).** |
| **claim-homogeneity** — THE KILL GATE: g_mu_nu(x) genuinely position-dependent (SURVIVES) vs x-independent/homogeneous (DEAD) | Phase 71 (A) | test-homogeneity | **Verified — SURVIVES** (2026-05-30) |
| **claim-matter-sourcing** — slice curvature sourced by M in V_1+V_{1/2} via cubic-norm cross-terms (CONDITIONAL on Phase 71 surviving) | Phase 72 (B) | test-cross-term-onoff, test-lambda-vs-matter | **VERIFIED — SURVIVES (qualified)** (2026-06-01, 9/9 HIGH): matter dominantly (~94%) cross-term-sources the curvature of the flat KKT slice g=η+h (off-switch R≈4008→247, a 16× decisive reduction; passes "vanishes OR changes decisively"); M=0 FLAT structurally DERIVED (C≡0 at M=0); R→0 as ‖M‖⁴; S≠0 & Weyl≠0. Caveats carried to Phase 73: ~6% V_{1/2} self-norm residual (sub-dominant 2nd channel); h⁽¹⁾=0 ⇒ quadratic-response (h⁽²⁾) test. |
| **claim-einstein-structure** — the honest level (exact / linear-in-M / none) at which G_mu_nu = kappa T_mu_nu + Lambda g_mu_nu holds (CONDITIONAL on Phase 72) | Phase 73 (C) | test-einstein-level | Planned (conditional) |

**Anchors carried through the milestone (must surface where applicable):** ref-prompt (`paper6-bulk-geometry-prompt.md`, authoritative spec), ref-faraut-koranyi (cone metric), ref-52-kkt (`52-kkt-spacetime.tex` + `52-observer-uniqueness.tex`, the Minkowski background), ref-h3o-tower (`h3o_tower.py`, corrected cubic norm), ref-baez-octonions, ref-warm-engine (`ring_lemma_verification.py` + `embedding_under_E_verification.py`), ref-peirce-coupling (`peirce_coupling.py` + `rho_directional_derivatives.py`), ref-mccrimmon, ref-vinberg-koszul, ref-gst (geometry only), ref-jacobson-contrast (avoid).

**Forbidden proxies (surfaced per relevant phase, never to be used as load-bearing):** fp-relabel-homogeneous, fp-coordinate-curvature, fp-float-decisive (Phase 71); fp-lambda-as-sourcing, fp-ensemble-gravity (Phase 72); fp-import-supergravity, fp-assume-einstein (Phase 73); fp-wrong-cross-term (Phase 70, propagates to all).

## Gating Structure (binding)

The phases form a **hard-gated chain** with a decisive KILL gate at Phase 71:

```
Phase 70 (A0: signature bridge) → Phase 70.1 (A0′: physical-metric selection) → Phase 71 (A: homogeneity KILL gate)
                                          │
                          ┌───────────────┴───────────────┐
                  HOMOGENEOUS                       POSITION-DEPENDENT
                  → route DEAD,                      → route SURVIVES,
                  STOP (clean valuable KILL,         proceed
                  milestone complete)                     │
                                                          ▼
                                          Phase 72 (B: matter-sourcing)
                                                          │
                                          ┌───────────────┴───────────────┐
                                  NO M-SOURCING                    M-SOURCED
                                  (pure Lambda only)               → proceed
                                  → stop at B                            │
                                                                         ▼
                                                       Phase 73 (C: Einstein structure)
```

**This is the milestone's defining feature.** Phase 71 (the homogeneity test) is CHEAP and DECISIVE and MUST run first (after the A0 foundation). A homogeneous Phase-71 result is a **clean, valuable KILL that terminates the milestone (NEGATIVE-RESULT-IS-SUCCESS)** — report it as such, do not soften it, do not relabel it "approximately position-dependent". Phases 72 and 73 are CONDITIONAL on Phase 71 surviving; "curved but not Einstein-structured" (B yes, C no) is an acceptable honest full-pass outcome.

**Phase 70.1 (inserted 2026-05-31).** Phase 72's first-result gate showed the M=0 **cone-Hessian** vacuum is the non-Einstein static product `R_time × H³` (Ric eig `{0,−1,−1,−1}`) — a GR Λ-vacuum must be Einstein, so this is the genuine VALD-04 finding (negative-result-is-success), not a reference choice. Because the cone-Hessian (route thesis) and the `η+h` bridge disagree about the M=0 geometry, the A0 signature bridge is **underdetermined**. Phase 70.1 re-runs the A0 gate to **select the physical spacetime metric** and restate the thesis before matter-sourcing can resume. Phase 71's SURVIVES verdict (position-dependence of the cone-Hessian slice) is unaffected; only its physical interpretation is re-adjudicated.

## Phases

**Phase Numbering:**
- Integer phases (70, 71, 72, 73): planned research work
- Decimal phases (e.g., 71.1): urgent insertions (marked INSERTED)

- [s] **Phase 70: A0 — Engine Reconciliation & Signature Bridge** — SUPERSEDED by Phase 70.1
  - Reason: construction-(ii) signature bridge **underdetermined** — Phase 72 found the M=0 cone-Hessian vacuum is the non-Einstein static product R_time×H³ (Ric eig {0,−1,−1,−1}); the Riemannian cone-Hessian (route thesis) and the Lorentzian η+h bridge disagree about the M=0 geometry, so the physical-metric selection must be made before any matter verdict. Engine / det_3 / Hessian benchmark / index map / H³ identification all PRESERVED (the engine is faithful, not what broke).
  - Original completion: 2026-05-30
- [x] **Phase 70.1: Revise A0 — select the physical spacetime metric (cone-Hessian vs η+h bridge)** (INSERTED, supersedes Phase 70) — **COMPLETE 2026-05-31 (1/1 plans, verified PASSED 5/5, HIGH; consistency CONSISTENT). VERDICT (human-ratified outcome 2): the physical spacetime metric is the η+h bridge (KKT Minkowski η + matter perturbation h), NOT the cone-Hessian curvature.** The literal "cone-Hessian IS the metric" thesis (option 1) is **FALSIFIED** as a NULL result — its M=0 vacuum is the non-Einstein R_time×H³ ({0,−1,−1,−1}, R=−3, S≠0, reproduced exact-over-Q + independently re-derived via a Levi-Civita path), and a spin-2 field on a fixed non-Einstein background is non-gauge ⇒ not a graviton, not gravity (negative-result-is-success applies to the falsification, NOT to relabeling the wave operator a win). **Human framing corrections (binding):** (1) the flat M=0 vacuum is **DERIVED** from the KKT det₂ Minkowski form (derivation 52: h_2(C_u)~R^{3,1}), **NOT** an inserted Λ=0 — the "circularity tripwire on the vacuum" framing is STRUCK; (2) the route is **RESTATED not abandoned** — the cone-Hessian is the source/information structure (its V_0↔V_{1/2} cross-terms 2Re((x₂x₁)x₃) source h); spacetime is the KKT slice (flat η); (3) Phase 72/73 re-scope is a genuine physics test, NOT a circularity audit. PRIMARY criterion: causal/geodesic match to the slice's own det₂ Minkowski form (η matches; the cone-Hessian makes timelike x₀=β+γ the flat dilation factor of R×H³). det₂/det₃ splice-consistency PASS (h a valid symmetric (0,2) perturbation of η, small matter preserves sig (1,3), perturbative). fp-relabel (H³-leaf/timelike-quotient) rejected; construction (i) Wick-via-u=e₇ stays rejected. SUPERSEDES the falsified "center is Einstein, Λ<0" text (CONVENTIONS.md §6 / ROADMAP VALD-04 criterion #2 — notation-coordinator follow-up, non-blocking). Engine reused, not rebuilt; all decisive arithmetic exact over Q; det₃ SSOT preserved.
- [x] **Phase 71: A — Homogeneity KILL Gate** (completed 2026-05-30 — **SURVIVES**: inherited h_2(C_u) slice metric genuinely position-dependent; routes reconciled, II(h_2(C_u))≠0 off-center) — DECISIVE: is the inherited slice metric genuinely position-dependent (route SURVIVES) or x-independent/homogeneous (route DEAD)?
- [x] **Phase 72: B — Matter-Sourcing (matter-on-flat)** — **COMPLETE 2026-06-01 (2/2 plans; verified PASSED 9/9 HIGH — verifier independently re-derived every decisive number from its own from-scratch Fano-octonion algebra; consistency CONSISTENT). VERDICT: SURVIVES (qualified) — Phase 73 greenlit.** Matter in V_{1/2} **dominantly (~94%)** cross-term-sources the curvature of the flat KKT spacetime slice g=η+h via 2Re((x₂x₁)x₃) (off-switch R_full≈4008→R_off≈247, a 16× decisive reduction); M=0 is FLAT (R=S=Weyl=0, structurally DERIVED — the B1 difference potential vanishes identically at M=0 ⇒ C≡0, flat for ANY g⁻¹; NO Λ); curvature →0 as ‖M‖→0 (R~‖M‖⁴) and carries genuine S≠0 & Weyl≠0 (not a coordinate artifact). **Two honest qualifications:** the cross-term off-switch is a decisive REDUCTION not a total kill (~6% V_{1/2} self-norm residual = a sub-dominant 2nd channel); and **h⁽¹⁾=0 identically ⇒ matter enters at O(‖M‖²) ⇒ Phase 73 is a QUADRATIC-response test using the emitted h⁽²⁾** (the linear-in-M linearized-Einstein test is degenerate). All decisive arithmetic exact over Q; det₃ SSOT; octonion_algebra.py banned. The matter mechanism + ΔR pipeline are PRESERVED. _History: HALTED 2026-05-31 at the 72-01 first-result gate (M=0 cone-Hessian vacuum non-Einstein R_time×H³ {0,-1,-1,-1}) → reopened as Phase 70.1, now resolved. See `.gpd/phases/72-b-matter-sourcing/PHASE-RECOVERY.md`._
- [ ] **Phase 73: C — Einstein Structure (CONDITIONAL on Phase 72)** — **Re-scoped 2026-05-31 by Phase 70.1:** the strong-form test is "does the matter-sourced perturbation h satisfy the LINEARIZED EINSTEIN equation on the KKT-flat η background (□h̄ ~ κT, correct tensor + gauge structure)?" — framed as that derivation step. This test CAN FAIL (if h obeys a non-Einstein PDE, the route's GR claim dies as an honest negative result — that is the real gate, NOT a self-inserted Λ; NO Λ=0 circularity tripwire on the vacuum, since flatness is DERIVED from KKT). Report the honest level (exact / linear-in-M / not-Einstein-structured).

## Phase Details

### Phase 70: A0 — Engine Reconciliation & Signature Bridge

> **⊘ SUPERSEDED by Phase 70.1 (2026-05-31).** The certified engine, `det_3`, Hessian benchmark, index map, and H³ identification below all remain valid and are inherited. What is reopened: the **physical-metric selection** (cone-Hessian vs `η+h`) that this phase left underdetermined by adopting construction (ii) as a modeling choice. See `.gpd/phases/70-a0-engine-reconciliation-signature-bridge/SUPERSEDED.md`.

**Goal:** A single certified cubic-norm engine is established and the Riemannian-cone-Hessian -> Lorentzian-slice signature bridge is fixed and shown to reduce to EXACT Minkowski at (M=0, center). Every downstream curvature is built from det-derivatives, so a wrong det convention or a contaminated background silently corrupts the whole milestone — this is the prerequisite gate.
**Depends on:** Nothing (entry point; reuses warm v16.0 engine)
**Requirements:** SETU-01, SETU-02, VALD-02, VALD-03
**Contract Coverage:**
- Advances: claim-signature-bridge
- Deliverables: deliv-phaseA precursor — `code/bulk_geometry_verification.py` (copy/extend `code/ring_lemma_verification.py`, NOT importing `code/octonion_algebra.py`); a single certified `det_3`; the fixed signature bridge (ii) with eta from h_2(C_u)'s det; the Cayley-Hamilton + multiplicativity cross-term verification
- Anchor coverage: ref-warm-engine (`ring_lemma_verification.py` — reuse, do not rebuild), ref-h3o-tower (`h3o_tower.py` corrected cross-term `2Re(x2* x0* x1)`), ref-52-kkt (`52-kkt-spacetime.tex` — the Minkowski background eta from det_2), ref-faraut-koranyi (`g^{pq} = P(X)`), ref-prompt (authoritative conventions block)
- Forbidden proxies: **fp-wrong-cross-term** (the buggy `2Re(x0(x1 x2))` / `2Re((x1 x2) x3)` association — silently corrupts every downstream curvature; do NOT import `octonion_algebra.py`); fp-float-decisive (cross-term verification exact over Q, not float)
**Success Criteria** (what must be TRUE):

1. The warm engine ALL_PASS is reproduced; `det_3` is certified the single source of truth via Cayley-Hamilton + multiplicativity + F_4-invariance, and the three in-repo cross-term conventions are reconciled on genuinely NON-associative (e_4..e_7) octonionic data (the association-invariance pre-flight is NONZERO — a check on diagonal/quaternionic e_0..e_3 data would be vacuous). [SETU-01]
2. The A0 signature bridge is stated as construction (ii) — background Lorentzian eta from h_2(C_u)'s own det + cone-Hessian perturbation h_mu_nu — with construction (i) (Wick-rotate via u=e_7) reported as the rejected alternative and why (it carries a separate unproven C*-bottleneck signature-flip conjecture; naive coordinate Wick rotation on a curved metric is coordinate-dependent and manufactures spurious curvature, Visser arXiv:1702.05572). [SETU-02]
3. The slice metric reduces to EXACT Minkowski at (M=0, center I/3): `g_mu_nu(center, M=0) = eta_mu_nu` (signature (1,3), mostly-minus) with ZERO residual `h_mu_nu` over Q — the mandatory gate on the whole construction. The measured benchmark `Hess(-log det)` at I/3 = `diag(9,9,18,18)` (nondegenerate, det 26244) and the slice det form `b*g/3 - p^2/3 - q^2/3` are reproduced. [SETU-02, VALD-02]
4. The h_2(C_u) sub-slice limiting case is verified as an independent geometric cross-check of the bulk machinery: the det=1 hyperboloid is `H^3 = SL(2,C)/SU(2)` with constant negative curvature (Totaro Cor. 2.3 gives `-d^2/4 = -1` for d=2, rank-1). [VALD-03]
5. The potential is FIXED as `-log det` (not `det`) at the start and the index/coordinate assignment for the V_0 spacetime sub-slice (`{17,18,19,26}`) and signature convention are stated explicitly (so they are not silently mixed downstream).

**Backtracking trigger:** If the cubic-norm cross-term association fails its Cayley-Hamilton / multiplicativity verification, STOP and fix det before ANY geometry. If construction (ii) does not reduce to EXACT Minkowski at (M=0, center), switch to construction (i) or STOP and re-examine the bridge — do not proceed with a contaminated background (a constant offset masquerades as Lambda or position-dependence).
**Plans:** 2 plans (wave 1: 70-01; wave 2: 70-02)

Plans:

- [ ] 70-01-PLAN.md — Engine reconciliation: copy Sections 1-3 of `ring_lemma_verification.py` verbatim into `code/bulk_geometry_verification.py`; certify `det_3` (cross `2Re((x2 x1) x3)`) via LOCK 7a (Cayley-Hamilton norm) + LOCK 7b (324/324 inner-derivation annihilation); three-ordering reconciliation on non-associative e_4..e_7 data; reproduce ALL_PASS. [SETU-01]
- [ ] 70-02-PLAN.md — Signature bridge (ii): state construction (ii) (eta from h_2(C_u)'s det_2) vs rejected (i); assert sub-slice index map `{17,18,19,26}` == engine-native `{x1,x2,x3,x10}` via slice det form `b*g/3 - p^2/3 - q^2/3`; new gate `Hess(-log det)|_{I/3} = diag(9,9,18,18)`, det 26244; prove exact Minkowski reduction `g(center,M=0) - eta = 0` over Q; state H^3 = SL(2,C)/SU(2) target curvature -1 (Totaro), defer full computation to Phase 71. [SETU-02, VALD-02, VALD-03]

### Phase 70.1: Revise A0 — select the physical spacetime metric (cone-Hessian vs η+h bridge) (INSERTED — supersedes Phase 70)

**Goal:** Resolve the ONE well-posed question Phase 70 left underdetermined — **which object is the physical spacetime metric, the Riemannian cone-Hessian or the Lorentzian construction-(ii) bridge `g = η + h`?** — and restate the route thesis accordingly. This is a decision + thesis-restatement + consequence-propagation phase, NOT an engine rebuild: the Phase-70 SSOT engine, `det_3`, Hessian benchmark, index map, and H³ identification are inherited unchanged. The cone-Hessian (the route's own thesis metric) gives a non-Einstein `R×H³` M=0 vacuum (Ric eig {0,−1,−1,−1}); `η+h` gives a flat one — they disagree, which is exactly the underdetermination to fix.
**Depends on:** Phase 70 (superseded — inherits its certified engine and Lorentzian background)
**Supersedes:** Phase 70
**Requirements:** SETU-02 (REOPENED — physical-metric selection); SETU-01, VALD-02, VALD-03 inherited as SATISFIED
**Contract Coverage:**
- Advances: claim-signature-bridge (re-adjudicated: from "a bridge that reduces to Minkowski" to "WHICH metric is gravity, with the thesis restated")
- Anchor coverage: ref-warm-engine (reuse `code/bulk_geometry_verification.py`, do NOT rebuild), ref-52-kkt (η from `det_2`), ref-faraut-koranyi (`g_X = Hess(−log det)`), ref-totaro (Ricci of the cone-Hessian slice), ref-prompt
- Forbidden proxies: **fp-relabel** (do NOT measure against the det₂=1 H³ leaf — it drops the timelike x_0 and swaps spacetime for a 3-dim spatial slice; quotienting the dilation/timelike dir is the same move); **fp-float-decisive** (selection is exact over Q); **fp-assume-einstein** / inserting any factor to force Ric∝g or flatness
**Success Criteria** (what must be TRUE):

1. The metric-selection verdict is made explicitly and exactly over Q: the cone-Hessian M=0 vacuum's Ricci spectrum `{0,−1,−1,−1}` (R=−3, NOT Einstein; flat dir = timelike x_0; `R_time × H³`, K(p,q)=−1/2) is reproduced from the inherited engine and reported as the headline, NOT papered over with a "which Λ reference" baseline choice.
2. ONE of the two admissible thesis-restatements is adopted and written down:
   - **(cone-Hessian)** route does NOT yield GR-with-Λ-vacuum; strongest honest claim = **linearized spin-2 matter-response on a FIXED non-Einstein `R×H³` background**, named as such; OR
   - **(η+h bridge)** the bridge metric (not the cone curvature) is the gravitational field — restated with justification; `Λ=0` is inserted by center-subtraction → a circularity tripwire explicitly carried into Phase 73.
3. The consequence of the choice is propagated forward: Phase 72 (matter-sourcing) is re-scoped to match the selected metric (linearized perturbation on a fixed background, or `η+h` curvature), and Phase 73's circularity audit inherits the `Λ=0` tripwire if `η+h` is chosen.
4. The rejected reconciliation (a) (Einstein-on-the-H³-leaf) is recorded as rejected (`fp-relabel`), and construction (i) (Wick-rotate via u=e_7) remains rejected (not reopened).
5. All decisive arithmetic is exact over Q; `det_3` stays the single source of truth; no factor is inserted to force `Ric∝g` or flatness.

**Backtracking trigger:** If neither restatement is defensible (e.g. the cone-Hessian background turns out not to admit a consistent linearized spin-2 sector, AND `η+h` cannot be justified as the gravitational field without circularity), report that the route's gravitational interpretation is **not established** and escalate — do NOT force a metric choice to keep the milestone alive.
**Plans:** 1 plan (wave 1: 70.1-01, interactive)

Plans:
- [ ] 70.1-01-PLAN.md — reproduce-and-headline the M=0 cone-Hessian spectrum {0,−1,−1,−1} (R=−3, R_time×H³, NOT Einstein) exact-over-Q from the warm engine; Einstein-condition verdict + signature-independence; linearized-spin-2-on-fixed-non-Einstein-background defensibility + η+h Λ=0-circularity tripwire; interactive thesis-restatement ratification (cone-Hessian / η+h / escalate); consequence propagation to Phases 72/73

### Phase 71: A — Homogeneity KILL Gate

**Goal:** A DECISIVE verdict — either way — on whether the inherited slice metric `h_mu_nu(x)` is genuinely position-dependent (route SURVIVES) or x-independent/homogeneous (route DEAD). Fixing E_11 breaks E_6 -> `Stab_{E_6}(E_11)`; the route is alive iff that residual group does NOT act transitively enough on (basepoint, slice) pairs to make them all isometric. This is the cheapest, most decisive gate, and it KILLs or greenlights everything downstream.
**Depends on:** Phase 70 (certified engine + fixed signature bridge) — Phase 70 superseded by **Phase 70.1**; the engine Phase 71 used is inherited unchanged and the homogeneity **SURVIVES** verdict (cone-Hessian slice genuinely position-dependent) stands. Only the *physical-metric interpretation* of that position-dependence is re-adjudicated at 70.1.
**Requirements:** DERV-01, CALC-01, CALC-02, VALD-01
**Contract Coverage:**
- Advances: claim-homogeneity (THE KILL GATE)
- Deliverables: deliv-phaseA — the inherited slice metric `g_mu_nu(x) = eta_mu_nu + h_mu_nu(x)` built explicitly; the homogeneity verdict (position-dependent vs homogeneous); `dim Stab_{E_6}(E_11)` and the (basepoint, slice) family dimension modulo that stabilizer; if homogeneous, an explicit "route dead" statement and STOP
- Anchor coverage: ref-faraut-koranyi (cone metric, `g^{pq} = P(X)` quadratic representation for the symbolic inverse), ref-warm-engine + `orbit_dimension_gate.py` (exact-over-Q orbit/stabilizer dims), ref-peirce-coupling (`rho_directional_derivatives.py` off-center expansion around I/3), ref-baez-octonions / ref-vinberg-koszul / ref-mccrimmon (symmetric-space + Peirce machinery); the Kollross-Rodriguez-Vazquez 2022 (Adv. Math. 2023; arXiv:2202.10775) Table 7 totally-geodesic classification (V_0 slice `SO(9,1)/SO(9)` absent -> leans GREENLIGHT, but an inference that MUST be computed)
- Forbidden proxies: **fp-relabel-homogeneous** (a homogeneous result is a clean valuable KILL — do NOT relabel it "approximately position-dependent"); **fp-coordinate-curvature** (varying metric COMPONENTS in a bad chart are not curvature — only curvature-scalar invariants decide); **fp-float-decisive** (rank and curvature involve derivative cancellations — float fabricates the verdict; EXACT over Q only)
**Success Criteria** (what must be TRUE):

1. The inherited slice metric `g_mu_nu(x) = eta_mu_nu + h_mu_nu(x)` is built on V_0 with E_11 fixed by an exact-over-Q expansion of `g_X = Hess(-log det)` around X = I/3 in the V_0 (and h_2(C_u)) directions, metric inverse via the quadratic representation `g^{pq} = P(X)`. [DERV-01]
2. **The DECISIVE homogeneity verdict** is computed from exact-over-Q curvature-SCALAR INVARIANTS (Ricci scalar R(x), Kretschmann, and their `d_x`; check parallel-Riemann) evaluated at >= 2 distinct generic basepoints — NOT raw metric components, NOT a single basepoint: position-dependent (invariants differ across basepoints) => SURVIVES; x-independent (invariants equal) => KILL. Reported without softening either way. [VALD-01]
3. `dim Stab_{E_6}(E_11)` and the dimension of the (basepoint, slice) family modulo that stabilizer are computed via exact-over-Q matrix rank of the infinitesimal action (reuse `orbit_dimension_gate.py`), and the single-copy anchor (orbit dim 24 / Spin(8) stabilizer dim 28) is reproduced FIRST as engine calibration. The stabilizer-transitivity count agrees with the curvature-invariant verdict (the two-route cross-check). [CALC-01, VALD-01]
4. The totally-geodesic question is settled as a cheap potential KILL: the V_0 slice's second fundamental form II is computed (II = 0 => `R^slice` = ambient constant curvature => homogeneous => KILL), including ruling out that V_0 sits inside one of the larger geodesic submanifolds of the Table-7 classification (`F_4(-20)/Spin(9)`, `Sp(1,3)/...`). [CALC-02]
5. All decisive arithmetic on the KILL verdict is EXACT over Q (no float ranks, no float curvature); the off-center parameter `rho_J(X_bg)` is distinguished from the spacetime coordinate x (which is O(1), the wrong expansion variable).

**Backtracking trigger:** **KILL CONDITION** — if `h_mu_nu(x)` is x-independent (homogeneous), report "Phase A homogeneous — route dead" and STOP; do NOT proceed to Phase 72/73 and do NOT relabel it. If the single-copy orbit anchor (24 / Spin(8)) is not reproduced, the stabilizer computation is not yet trustworthy — re-calibrate before trusting the E_11-stabilizer count. If the x-variation verdict disagrees between the Riemannian restriction and the Lorentzian bridge, that disagreement localizes a coordinate/Wick artifact — return to Phase 70.
**Plans:** 2 plans (wave 1: 71-01; wave 2: 71-02)

Plans:

- [ ] 71-01-PLAN.md — Route 1 (primary curvature verdict): benchmark H^3=-1 on the cone-Hessian slice FIRST; extend cone_hessian_at_center to an off-center expansion (rho_J(X_bg), not x); compute R(x), K(x) via hand-rolled Totaro closed form exact over Q at >= 2 distinct generic rational basepoints on the dim-4 h_2(C_u) sub-slice; KILL/SURVIVES verdict reported without softening. [DERV-01, VALD-01]
- [ ] 71-02-PLAN.md — Route 2 (mandatory cross-check) + CALC-02 + final reconciliation: reproduce single-copy anchor (24/Spin(8) 28) + build e_6=f_4+L(traceless) (78) FIRST; compute dim Stab_{E_6}(E_11)=ker{D->D.E_11} + the (basepoint,slice)-family dim modulo it exact over Q; compute II of the full V_0 (II=0 => totally geodesic => KILL); emit the FINAL reconciled two-route verdict only if Route 1, Route 2, and II AGREE. [CALC-01, CALC-02, VALD-01]

### Phase 72: B — Matter-Sourcing (CONDITIONAL on Phase 71 surviving)

**Goal:** If Phase 71 greenlights (`h_mu_nu` genuinely varies), establish whether matter `M in V_1/V_{1/2}` SOURCES the slice curvature through the cubic-norm cross-terms — the only channel coupling V_0 to matter — with M=0 giving a flat or pure-cosmological-constant baseline. **This phase runs only if Phase 71 SURVIVES.**
**Depends on:** Phase 71 (the slice metric + a GREENLIGHT homogeneity verdict). **RE-SCOPED MATTER-ON-FLAT 2026-05-31 by Phase 70.1's physical-metric selection (η+h):** the M=0 baseline is flat KKT Minkowski η (R=0, DERIVED from det₂ — NOT inserted, NO Λ tripwire); matter in V_1/V_{1/2} sources h of g=η+h via the det₃ cross-term 2Re((x₂x₁)x₃); the curvature of g is computed with indices raised by g=η+h (NOT the bare cone-Hessian H_bg⁻¹), cross-checked by a hand-rolled Riemann. Matter mechanism + ΔR/decomposition pipeline PRESERVED; the old 72-01/02 plans are SUPERSEDED (archived under `superseded-pre-70.1/`).
**Requirements:** DERV-02, CALC-03, CALC-04, VALD-04
**Contract Coverage:**
- Advances: claim-matter-sourcing
- Deliverables: deliv-phaseB — the Riemann/Ricci tensor of `g_mu_nu(x)` as a function of M; the M=0 baseline (flat or pure-Lambda) established; the cross-term ON/OFF comparison (full det vs block-diagonal `det(V_1)*det(V_0)`); the curvature scale quantified vs `||M||` and `rho_J(X_bg)`
- Anchor coverage: Totaro's Hessian-curvature formula `R_ijkl = -(1/4) g^{pq}(f_jlp f_ikq - f_ilp f_jkq)` (arXiv:math/0401381 — depends ONLY on 3rd derivatives of det; det cubic => `f_ijkl = 0`, so this is exact and cheap, NOT a `sympy.diffgeom` blowup) [ref-mccrimmon / ref-faraut-koranyi machinery], ref-peirce-coupling (`peirce_coupling.py` Peirce decomposition + `rho_directional_derivatives.py` ||M||/rho_J expansion), test-cross-term-onoff
- Forbidden proxies: **fp-lambda-as-sourcing** (a pure cosmological-constant (M=0) curvature is NOT matter-sourcing — only the M-dependent part sourced by the V_0<->V_1/V_{1/2} cross-terms counts); **fp-ensemble-gravity** (no observers-make-gravity ensemble/thermodynamic Jacobson-style argument — the curvature must come from the algebra's own cubic-norm geometry); fp-float-decisive (the cross-term on/off verdict is exact over Q)
**Success Criteria** (what must be TRUE):

1. The Riemann/Ricci tensor of `g_mu_nu(x)` is computed via Totaro's closed form (hand-rolled Christoffel/Riemann, faster than `sympy.diffgeom`; ~19s exact on the dim-4 slice with matter rational), as an explicit function of M. [DERV-02]
2. The M=0 baseline is established as FLAT (R=S=Weyl=0), structurally DERIVED from the KKT det₂ Minkowski η — NOT a pure cosmological constant (the pre-70.1 "center is Einstein with negative Λ (Cartan)" framing is SUPERSEDED: that {0,−1,−1,−1}/R=−3/R×H³ geometry is the cone-Hessian SOURCE field, not the spacetime metric g=η+h). Genuine M-sourcing is distinguished from the flat baseline by the n=4 Ricci scalar / traceless-Ricci / Weyl decomposition (the M≠0 piece carries S≠0 & Weyl≠0; M=0 is flat). [VALD-04 — verified 2026-06-01]
3. **The cross-term ON/OFF test is DECISIVE:** the M-sourced curvature present with the FULL cubic norm VANISHES (or changes decisively) when the V_0<->V_1/V_{1/2} cross-terms are switched off (det replaced by the block-diagonal `det(V_1)*det(V_0)`), at the same M != 0 — establishing the sourcing channel. [CALC-03]
4. M is placed so that all three off-diagonal octonionic slots are populated (else the cubic vertex / triple product is vacuously zero and the test is hollow). [CALC-03]
5. The curvature scale is quantified as a function of `||M||` and the off-center parameter `rho_J(X_bg)` by series-expanding in the matter amplitude (substitute matter to rationals BEFORE any symbolic inverse — the symbolic inverse with matter+coords all symbolic is the >200s cost cliff; keep only the 4 slice coords symbolic); curvature is proportional to `||M||` and vanishes as M -> 0. [CALC-04]

**Backtracking trigger:** If the curvature at M=0 is a pure cosmological constant and turning on M adds nothing through the cross-terms (cross-term on/off makes no difference), then matter does not source the slice curvature — report "position-dependent but pure-Lambda / not matter-sourced" honestly and do NOT proceed to Phase 73 (or proceed only to document the non-Einstein outcome). If a decisive step risks exceeding the ~150s executor silent-compute watchdog, run foreground `python -u` with progress prints between heavy steps.
**Plans:** 2 plans

Plans:

- [x] 72-01-PLAN.md (wave 1, COMPLETE 2026-06-01) — DERV-02 + VALD-04 (matter-on-flat, build-and-confirm): the curvature of the spacetime metric g=η+h(x;M) as an explicit function of M (Totaro C from the cone-Hessian potential, indices raised with g⁻¹=(η+h)⁻¹ — NOT H_bg⁻¹), MANDATORY hand-rolled Riemann cross-check, the FLAT M=0 baseline (R=S=Weyl=0, DERIVED from KKT det₂ — NO Λ, NO R=-3), n=4 Ricci decomposition of the M≠0 curvature, V_1-inertness, and the Phase-71 cone-Hessian SOURCE-engine regression. Engine extension + derivations/72-matter-sourcing.tex SUPERSEDED to matter-on-flat.
- [x] 72-02-PLAN.md (wave 2, depends_on 72-01, COMPLETE 2026-06-01) — CALC-03 + CALC-04 (decisive controls + verdict): the DECISIVE cross-term ON/OFF (full det₃ vs block-diagonal det_block) at the same non-vacuous M≠0 on the curvature of g=η+h, the ||M||→0 flat-η limiting case + scaling vs ||M|| (empirical leading power) and det₂, the emitted linearized-in-M h⁽¹⁾ for the Phase-73 linearized-Einstein test, and the matter-sourcing VERDICT (three-part conjunction). **RESULT (human-ratified): SURVIVES (qualified)** — conjunct (i) off-switch = decisive ~94% reduction (R_full≈4008→R_off≈247, NOT a total kill, ~6% V_{1/2} self-norm residual; passes the contract's "vanishes OR changes decisively" criterion); (ii) ‖M‖→0 recovers flat η (R~‖M‖⁴) clean; (iii) S≠0 & Weyl≠0 clean. h⁽¹⁾=0 ⇒ emitted h⁽²⁾ for a Phase-73 QUADRATIC-response test. interactive (verdict checkpoint:decision, ratified 2026-06-01).

### Phase 73: C — Einstein Structure (CONDITIONAL on Phase 72 showing M-sourcing)

**Goal:** If Phase 72 shows matter sourcing, test the strongest claim — does `G_mu_nu = kappa T_mu_nu + Lambda g_mu_nu` hold for a `T_mu_nu` built independently from the V_1/V_{1/2} cross-term content? — and report the HONEST level (exact / linear-in-M / not at all). **This phase runs only if Phase 72 shows M-sourcing.** "Curved but not Einstein-structured" is an acceptable full-pass outcome and is the honest prior expectation; do NOT force Einstein form.
**Depends on:** Phase 72 (matter-sourced curvature); **if Phase 70.1 selects the η+h bridge, inherit the Λ=0-by-center-subtraction circularity tripwire** (the per-equation circularity audit must flag that flatness/Λ=0 was inserted, not derived).
**Requirements:** DERV-03, CALC-05, VALD-05
**Contract Coverage:**
- Advances: claim-einstein-structure
- Deliverables: deliv-phaseC — the explicit candidate `T_mu_nu` from V_1/V_{1/2} cross-term content (defined BEFORE computing `G_mu_nu`, independent of any assumed Einstein form); the comparison `G_mu_nu` vs `kappa T_mu_nu + Lambda g_mu_nu` at exact and linear-in-M order; the honest level reported (exact / linearized / curved-but-not-Einstein); a per-equation circularity audit
- Anchor coverage: ref-gst (GST `E_{6(-26)}/F_4` scalar-manifold geometry — citable FOR THE GEOMETRY ONLY, never the Lagrangian), ref-jacobson-contrast (Jacobson 1995 — CONTRAST only, the rejected ensemble route), test-einstein-level
- Forbidden proxies: **fp-import-supergravity** (importing supergravity multiplet data / the GST Lagrangian / the assumed N=2 SUSY closure / Weinberg's soft-graviton theorem as a load-bearing INPUT — this is exactly the circularity of the dead det/GST/Weinberg route where -R/2 is fixed by the assumed SUSY closure; the slice geometry genuinely coincides with GST special-real geometry, so this trap is subtle); **fp-assume-einstein** (assuming Einstein form and fitting/tuning kappa, Lambda per-point, or declaring Einstein structure from a single tuned point)
**Success Criteria** (what must be TRUE):

1. A candidate stress-energy `T_mu_nu` is constructed from the V_1/V_{1/2} cross-term content of M, defined INDEPENDENTLY of any assumed Einstein form (NO GST / SUSY / -R/2 / Weinberg input), and `kappa` is defined from intrinsic cross-term data — both BEFORE `G_mu_nu` is computed. [DERV-03]
2. **Re-scoped 2026-06-01 (Phase 72 result):** the test is the LINEARIZED-EINSTEIN can-fail test on the flat KKT η background, at QUADRATIC order in M (since h⁽¹⁾=0, the linear-in-M response is degenerate — use the emitted h⁽²⁾): form the trace-reversed h̄⁽²⁾ and test □h̄⁽²⁾ ~ κT against a T built independently from the V_{1/2} cross-term content, with κ a GLOBAL constant over an (M, x) FAMILY (never a single tuned point). **Λ=0** (the M=0 vacuum is flat-DERIVED from KKT, NOT Einstein-negative — the pre-70.1 "fit Λ nonzero" instruction is SUPERSEDED; no Λ tripwire). A non-Einstein PDE for h⁽²⁾ is an honest negative result, not a failure to force. [CALC-05]
3. The honest level is reported: exact / linear-in-M / none. A no-Einstein-structure result is reported plainly as "curved but not Einstein-structured" — an acceptable full result, not forced into Einstein form. [CALC-05]
4. A per-equation circularity audit confirms `T_mu_nu` (DERV-03), `kappa`, and the Einstein test (CALC-05) use NO supergravity multiplet data, GST Lagrangian, SUSY closure, or Weinberg soft-graviton input as load-bearing. [VALD-05]
5. The same `kappa, Lambda` work across the (M, x) family (a single-point match is rejected as a tuned-point overclaim; linear-in-M agreement is reported as the weaker level it is).

**Backtracking trigger:** If no Einstein structure holds at exact or linear order, that is ACCEPTABLE — report "curved but not Einstein-structured" and do NOT force Einstein form. If the only way to reach `G = kappa T + Lambda g` is to import GST/SUSY/-R/2/Weinberg, STOP — that is the circularity the milestone exists to avoid; report the honest non-Einstein level instead.
**Plans:** TBD

Plans:

- [ ] 73-01: TBD (construct T_mu_nu + kappa from cross-terms, independent of Einstein form; circularity audit)
- [ ] 73-02: TBD (Einstein-structure test over an (M,x) family; honest level verdict)

## Phase Dependencies

| Phase | Depends On | Enables | Critical Path? | Gate |
| ----- | ---------- | ------- | :-: | ---- |
| 70 — A0 Engine & Bridge (SUPERSEDED) | — | 70.1, 71 | Yes | reduce-to-Minkowski gate (superseded by 70.1) |
| **70.1 — Revise A0: metric selection** (COMPLETE) | 70 (superseded; engine inherited) | 72 (re-scope), 73 | Yes | **RESOLVED — η+h selected; cone-Hessian-is-metric FALSIFIED** |
| 71 — A Homogeneity KILL | 70 (engine, via 70.1) | 72 (only if SURVIVES) | Yes | **KILL gate — homogeneous => STOP** |
| 72 — B Matter-Sourcing | 71 (SURVIVES) | 73 (only if M-sourced) | Yes | no-M-sourcing => stop at B |
| 73 — C Einstein Structure | 72 (M-sourced) | — | Yes | curved-but-not-Einstein acceptable |

**Critical path:** 70 → 71 → 72 → 73 (strictly sequential — this is a hard-gated chain, not a parallelizable DAG).
**Parallelizable:** None. Each phase's verdict gates the next; the Phase-71 KILL or Phase-72 no-sourcing result can terminate the milestone as a full pass before later phases execute.

## Risk Register

| Phase | Top Risk | Probability | Impact | Mitigation |
| ----- | -------- | :-: | :-: | ---------- |
| 70 | Wrong cubic-norm cross-term association silently corrupts every downstream curvature | MEDIUM | HIGH | Single source of truth (`ring_lemma_verification.det_3`); Cayley-Hamilton + multiplicativity pre-flight on NON-associative e_4..e_7 data; do NOT import `octonion_algebra.py` |
| 70 | Signature bridge does not reduce to exact Minkowski (contaminated background) | MEDIUM | HIGH | Mandatory `g(center, M=0) = eta` gate; fall back to construction (i) or STOP; never "rotate the answer" |
| 71 | Self-deception at the KILL gate — false KILL (over-symmetrizing) or false GREENLIGHT (reading metric components / coordinate artifact as curvature) | MEDIUM | HIGH | Decide on coordinate-invariant curvature SCALARS as functions of x at >= 2 basepoints PLUS exact stabilizer-orbit count; EXACT over Q; reproduce single-copy anchor first; cross-check Riemannian vs Lorentzian verdict |
| 71 | V_0 slice is totally geodesic (II = 0) => bulk-constant curvature => KILL | MEDIUM | HIGH (decisive) | Compute II directly; rule out V_0 inside larger Table-7 geodesic submanifolds; this IS a legitimate KILL if true (report it) |
| 71 | Exact `Stab_{E_6}(E_11)` (parabolic, Levi ~ Spin(9,1)) not cleanly tabulated | MEDIUM | MEDIUM | Build `{D in e_6 : D*E_11 = 0}` explicitly as a kernel over Q; may need `/gpd:research-phase` |
| 72 | Symbolic matrix inverse with matter+coords symbolic times out (>200s) | HIGH | MEDIUM | Substitute matter to rationals BEFORE inverting; keep only 4 slice coords symbolic; series-expand in single amplitude t; foreground `python -u` with progress prints (watchdog ~150s) |
| 72 | Lambda mistaken for matter-sourcing | MEDIUM | HIGH | Cross-term off-switch (`det -> det(V_1)*det(V_0)`); require curvature -> 0 as M -> 0; decompose Ricci scalar/traceless/Weyl |
| 73 | Circularity — GST/SUSY/-R/2/Weinberg silently re-imports the assumed Einstein structure (the slice geometry coincides with GST special-real geometry) | HIGH | HIGH | Hard input ban declared at Phase 70; cite GST for the manifold ONLY; define T_mu_nu, kappa from cross-terms BEFORE G_mu_nu; per-equation circularity audit (VALD-05) |
| 73 | Tuned-point Einstein overclaim | MEDIUM | MEDIUM | Test over an (M, x) family with GLOBAL constants; report linear-in-M as the weaker level; "curved but not Einstein" is acceptable |

## Backtracking Triggers (summary)

- **Phase 70:** Cross-term association fails Cayley-Hamilton/multiplicativity -> fix det before ANY geometry. Bridge (ii) fails exact-Minkowski reduction -> switch to (i) or STOP.
- **Phase 71 (KILL gate):** `h_mu_nu(x)` x-independent (homogeneous) -> "route dead", STOP, milestone complete as a clean valuable KILL. Single-copy orbit anchor not reproduced -> recalibrate. Riemannian/Lorentzian verdict disagreement -> coordinate artifact, return to Phase 70.
- **Phase 72:** M=0 pure-Lambda with cross-term on/off showing no difference -> not matter-sourced; report honestly, do not force Phase 73.
- **Phase 73:** No Einstein structure at exact/linear order -> report "curved but not Einstein-structured", do NOT force. Reaching Einstein form only via imported GST/SUSY/Weinberg -> STOP (circularity).

## Coverage

- All 15 v17.0 requirements (2 SETU, 3 DERV, 5 CALC, 5 VALD) mapped to exactly one primary phase. No orphans, no duplicates.
- All 4 decisive contract claims surfaced (claim-signature-bridge, claim-homogeneity, claim-matter-sourcing, claim-einstein-structure), each with its acceptance tests.
- All 7 forbidden proxies surfaced in the phase(s) where they bite.
- The user-stated KILL gate (Phase 71 first, decisive, NEGATIVE-RESULT-IS-SUCCESS), the construction-(ii) signature bridge, the exact-over-Q discipline on decisive verdicts, the single-source-of-truth det engine, and all stop/rethink conditions are preserved as success criteria and backtracking triggers.

## Progress

**Execution Order:**
Phases execute in strict numeric order with hard gates: 70 -> 71 -> [KILL?] -> 72 -> [sourced?] -> 73

| Phase | Milestone | Plans Complete | Status | Completed |
| ----- | --------- | -------------- | ------ | --------- |
| 70. A0 — Engine Reconciliation & Signature Bridge | v17.0 | 2/2 | **Superseded by 70.1** (2026-05-31) | 2026-05-30 |
| 70.1 Revise A0 — physical-metric selection (cone-Hessian vs η+h) | v17.0 | 1/1 | **Complete — η+h SELECTED; option-1 cone-Hessian FALSIFIED** (verified 5/5 HIGH) | 2026-05-31 |
| 71. A — Homogeneity KILL Gate | v17.0 | 2/2 | Complete (SURVIVES) | 2026-05-30 |
| 72. B — Matter-Sourcing (matter-on-flat) | v17.0 | 2/2 | **Complete — SURVIVES (qualified)** (verified 9/9 HIGH; consistency CONSISTENT) | 2026-06-01 |
| 73. C — Einstein Structure (conditional) | v17.0 | 0/TBD | Greenlit by 72 — QUADRATIC-response linearized-Einstein test (use h⁽²⁾, h⁽¹⁾=0) | - |

---

_Roadmap created 2026-05-30 for milestone v17.0. Phases 70-73 (physics-side; independent of the v16.0 consciousness-side (RING) line — do not entangle). Machine-readable contract: `.gpd/state.json` field `project_contract`. Authoritative milestone spec: `~/scratch/get-physics-done/paper6-bulk-geometry-prompt.md`._
