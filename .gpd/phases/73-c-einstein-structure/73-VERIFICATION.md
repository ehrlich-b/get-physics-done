---
phase: 73-c-einstein-structure
verified: 2026-06-01T00:00:00Z
status: passed
score: 8/8 contract targets verified
consistency_score: 14/14 applicable physics checks passed
independently_confirmed: 13/14 checks independently confirmed (1 INFO notation flag)
confidence: high
profile: deep-theory
autonomy: balanced
research_mode: balanced
plan_contract_ref:
  - ".gpd/phases/73-c-einstein-structure/73-01-PLAN.md#/contract"
  - ".gpd/phases/73-c-einstein-structure/73-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-einstein-structure:
      status: VERIFIED
      summary: "Honest level = NONE (curved but not Einstein-structured), HUMAN-ratified, reported at true strength. INDEPENDENTLY CONFIRMED by re-running 73-02-einstein-test.py (EINSTEIN_TEST_OK, exit 0): no single global (kappa,Lambda) reproduces the full nonlinear G[g] against EITHER frozen T (T[psi] t^4-matched, T_sigma t^2 order-mismatch), at finite M OR t^4 order, over a 12-point sig-(1,3) family. Einstein form NOT forced; near-miss NOT rounded (kappa*T ~10^3 smaller than G); Lambda=0 DERIVED not inserted."
  deliverables:
    deliv-T-build:
      status: VERIFIED
      summary: "Both T frozen (T[psi]=d psi d psi-(1/2)eta(d psi)^2 via det_3 SSOT; sigma T[V_1/2]); symmetric, EXACTLY conserved (box psi=0, harmonic), T->0 as ||M||->0, V_1-inert, AST-guarded NO Ric/R/G. Re-run reproduced kappa_psi=32016781143/5929, kappa_sigma=395268903/129850, all order anchors exact over Q."
    deliv-h2-field:
      status: VERIFIED
      summary: "h2_field(x)+box added to engine Section 14; engine re-run ALL_PASS exit 0; h^(2)(x)|center == handoff matrix reproduced; box built from eta_bg^{-1}."
    deliv-audit-scaffold:
      status: VERIFIED
      summary: "VALD-05 T3/T4 rows certified intrinsic; GST-coincidence trap addressed; all forbidden imports rejected."
    deliv-phaseC:
      status: VERIFIED
      summary: "derivations/73-einstein-structure.tex complete: explicit T, order-counting resolution, family G[g], decisive fit (both candidates, both readings), n=4 S/Weyl decomp, HUMAN-ratified NONE verdict at true strength, circularity audit. Every decisive number independently reproduced."
    deliv-audit-final:
      status: VERIFIED
      summary: "73-circularity-audit.md C.a/C.b/C.c rows certified; stale-ROADMAP reconciliation present (box-hbar gauge-degenerate; Lambda=0 DERIVED); final no-forbidden-import certification; 0 placeholders."
  acceptance_tests:
    test-T-conserved:
      status: VERIFIED
      summary: "Re-run: both T symmetric + conserved (d^mu T_munu=[0,0,0,0] exact over Q, box psi=0 identically) + vanish as ||M||->0 + V_1-inert; AST guard forbidden-id uses = {} (no Ric/R/G in T construction)."
    test-order-anchors:
      status: VERIFIED
      summary: "Re-run reproduced exact over Q: G^(1)[h^(2)]=0, R^(1)=0, box(hbar^(2))(0,0)=-76221/2450, (3,3)=-38637/1225, Lorenz defect=[19143/9800,9747/4900,297/350,0]; h^(2)(x)|center==handoff. Linear test degenerate => full G[g] at O(||M||^4) decisive."
    test-einstein-level:
      status: VERIFIED
      summary: "Re-run EINSTEIN_TEST_OK exit 0: 12 sig-(1,3) points (6 out-of-splice dropped not forced); Rscalar(M_0)~4008 regression; G~O(M^4) (G/t^4 stabilizes [88.1,89.7,90.1], G/t^3->0); Totaro==hand-rolled (5 components byte-identical over Q); both T finite-M+t^4+120-eq linsolve ALL negative; S!=0 (10/16), Weyl!=0 (72/256), trace_S=0, reconstruction exact. Level NONE reported, single-point match rejected, HUMAN-ratified."
  forbidden_proxies:
    fp-import-supergravity:
      status: REJECTED
      summary: "No GST Lagrangian / SUSY closure / -R/2 / Weinberg in T, kappa, or fit. GST cited geometry-only. Negative result reached on intrinsic data alone (engine ALL_PASS rejects buggy cross-term off-by-16). AST-guarded."
    fp-assume-einstein:
      status: REJECTED
      summary: "AST guard (code-use, not comment-mention) forbidden-id uses = {} for T and kappa. a_4 frozen rational NUMBER not live curvature. kappa frozen in 73-01 before G; kappa != -R/2 (independently confirmed). Single-point match rejected in code; residual reported exact (largest ~7209), not rounded."
    fp-ensemble-gravity:
      status: REJECTED
      summary: "No delta Q=T dS / entropy-area / Unruh-T. Jacobson named and rejected (contrast only)."
    fp-float-decisive:
      status: REJECTED
      summary: "All family G,g entries real rationals over Q (re-run exactness guard passed); fit via sympy linsolve over Q; signatures via eig_signature_count (sympy real_roots). Floats only in progress prints."
    fp-wrong-cross-term:
      status: REJECTED
      summary: "psi/sigma use engine det_3 2Re((x2 x1)x3) SSOT; octonion_algebra.py banned; engine ALL_PASS certifies det_3 byte-identical to ring_lemma_verification and rejects (x1 x2)x3 off-by-16."
  references:
    ref-prompt:
      status: completed
      summary: "Phase-C reporting discipline honored: honest level reported (NONE), not forced, not deflated."
    ref-gst:
      status: completed
      summary: "Cited geometry-only; avoided as a coupling input (fp-import-supergravity rejected)."
    ref-jacobson-contrast:
      status: completed
      summary: "Named and rejected (fp-ensemble-gravity)."
    ref-72-handoff:
      status: completed
      summary: "a_4=395268903/24010000, h^(1)=0, M_0, R_full~4008 consumed and cross-checked; regression Rscalar(M_0,center)~4007.98 independently reproduced over Q."
    ref-warm-engine:
      status: completed
      summary: "Engine reused not rebuilt; ALL_PASS exit 0 re-confirmed; Totaro==hand-rolled cross-check passed."
comparison_verdicts:
  - subject_kind: acceptance_test
    subject_id: test-einstein-level
    reference_id: ref-72-handoff
    comparison_kind: benchmark
    verdict: pass
    metric: "Rscalar(M_0,center) vs Phase-72 R_full"
    threshold: "exact over Q (float ~4007.98)"
    notes: "Independently reproduced: exact rational float 4007.98090373574, matches Phase-72 to <1e-6."
  - subject_kind: acceptance_test
    subject_id: test-einstein-level
    reference_id: ref-warm-engine
    comparison_kind: cross_method
    verdict: pass
    metric: "Totaro closed-form vs hand-rolled Levi-Civita Riemann (5 components)"
    threshold: "exact over Q (byte-identical)"
    notes: "All 5 components R[0202],R[2323],R[0101],R[1212],R[0303] byte-identical exact rationals."
  - subject_kind: claim
    subject_id: claim-einstein-structure
    reference_id: null
    comparison_kind: oracle
    verdict: pass
    metric: "single global (kappa,Lambda) fit residual G - kappa T - Lambda g"
    threshold: "zero residual => Einstein; nonzero => not Einstein"
    notes: "Both T, both readings (finite-M, t^4), 120-eq over-determined linsolve: ALL non-zero/inconsistent. Best-Lambda residual largest |entry| 7209 (T[psi]) / 7190 (T_sigma) at (1,1). Verdict NONE confirmed."
suggested_contract_checks: []
expert_verification: []
---

# Phase 73 (C — Einstein Structure) — Verification Report

**Phase goal:** Test the strongest claim — does `G_mu_nu = kappa T_mu_nu + Lambda g_mu_nu` hold for a `T_mu_nu` built INDEPENDENTLY from the V_1/V_{1/2} cross-term content? — and report the HONEST level (exact / linear-in-M / curved-but-not-Einstein). "Curved but not Einstein-structured" is an acceptable full-pass outcome and the honest prior; Einstein form must NOT be forced.

**Verdict (human-ratified):** NONE (curved but not Einstein-structured). This is the FINAL decisive verdict of milestone v17.0.

**Status:** passed — 8/8 contract targets VERIFIED, all by INDEPENDENT re-execution of the drivers (verifier-reruns-scripts discipline). Confidence: HIGH.

**Verification mode:** Profile=deep-theory, autonomy=balanced, mode=balanced. Initial verification (no prior 73-VERIFICATION.md). Independent context: contract targets keyed to PLAN frontmatter IDs; SUMMARY claims NOT trusted — every decisive number re-derived by re-running the scripts and by independent oracles.

---

## Scripts re-run (the decisive re-checks)

| # | Script | Exit | Decisive numbers REPRODUCED (exact over Q) |
|---|--------|:----:|---------------------------------------------|
| 1 | `code/bulk_geometry_verification.py` | **0** | `OVERALL: ALL_PASS`. det_3 cross-term certified the unique F_4-invariant cubic norm (byte-identical to ring_lemma SSOT; buggy (x1 x2)x3 order **rejected off-by-16** => fp-wrong-cross-term rejected). h2_field/box (Section 14) extensions intact (engine still ALL_PASS after the 73-01 extension). |
| 2 | `73-01-build-T-kappa.py` (run via 73-02 import) | **0** | `BUILD_T_KAPPA_OK`. kappa_psi=**32016781143/5929** (t^4 matched), kappa_sigma=**395268903/129850** (t^2 mismatch). Order anchors: G^(1)[h^(2)]=0, R^(1)=0, box(hbar^(2))(0,0)=**-76221/2450**, (3,3)=**-38637/1225**, Lorenz defect=**[19143/9800, 9747/4900, 297/350, 0]**. psi(x;M_0)=11p/6300-13/63000 (center -13/63000). T[psi] & T_sigma symmetric + conserved (box=0) + T->0 as ||M||->0 + V_1-inert. AST guard forbidden-id uses = **{}** (no Ric/R/G in T) and **[]** (no Ric/R/G/GST/SUSY in kappa). |
| 3 | `73-02-einstein-test.py` | **0** | `EINSTEIN_TEST_OK`. 12 sig-(1,3) points, **6 dropped** out-of-splice (sig (4,0,0)/(3,1,0), not forced). Rscalar(M_0,center) exact rational = float **4007.98** (==Phase-72). G/t^4=[88.14,89.66,90.06] stabilizes; G/t^3->0 => G first at O(||M||^4). Totaro==hand-rolled on 5 components byte-identical over Q. Fit: T[psi] finite-M=**False**, global-solve=**False**, t^4=**False**; T_sigma all **False**. n=4: S!=0 (**10/16**), Weyl!=0 (**72/256**), trace_S=**0**, reconstruction exact. Best-Lambda residual largest |entry|=**7209** (T[psi])/**7190** (T_sigma) at (1,1). LEVEL = **NONE**. |

Both background runs returned **exit code 0**; zero tracebacks/AssertionErrors in either log.

---

## Contract Coverage

| ID | Kind | Status | Confidence | Evidence |
|----|------|--------|------------|----------|
| claim-einstein-structure | claim | VERIFIED | INDEPENDENTLY CONFIRMED | 73-02 EINSTEIN_TEST_OK; level NONE; both T fits negative; S/Weyl != 0; human-ratified |
| deliv-T-build | deliverable | VERIFIED | INDEPENDENTLY CONFIRMED | Both T frozen, conserved, V_1-inert, AST-guarded; kappa reproduced |
| deliv-h2-field | deliverable | VERIFIED | INDEPENDENTLY CONFIRMED | Engine ALL_PASS after Section-14 extension; h^(2)(x)|center==handoff |
| deliv-audit-scaffold | deliverable | VERIFIED | STRUCTURALLY PRESENT | T3/T4 rows certified; GST trap addressed |
| deliv-phaseC | deliverable | VERIFIED | INDEPENDENTLY CONFIRMED | .tex numbers all reproduced; verdict at true strength |
| deliv-audit-final | deliverable | VERIFIED | INDEPENDENTLY CONFIRMED | C.a/C.b/C.c certified; stale-ROADMAP reconciliation present |
| test-T-conserved | acceptance | VERIFIED | INDEPENDENTLY CONFIRMED | d^mu T=0 over Q, box psi=0, AST guard empty |
| test-order-anchors | acceptance | VERIFIED | INDEPENDENTLY CONFIRMED | All 4 anchors reproduced exact over Q |
| test-einstein-level | acceptance | VERIFIED | INDEPENDENTLY CONFIRMED | Full G[g] family fit negative; NONE; single-point match rejected |

---

## Independent Oracles (computed by the verifier, separate from the drivers)

```output
=== ORACLE A: eta_bg signature ===
eta_bg eigenvalues (exact): {-1/2: 1, 1/2: 1, -1: 2}
signature: (+1, -3, 0:0)  => Lorentzian (1,3)? True
eta_bg @ eta_bg^-1 == I? True

=== ORACLE B: a_4, kappa vs -R/2 ===
a_4 = 395268903/24010000 = float 16.4626781757601
-R/2 = -a_4/2 = -395268903/48020000
kappa_psi   = 32016781143/5929    != -R/2? True
kappa_sigma = 395268903/129850    != -R/2? True
implied Tscale_psi   = a4/kappa_psi   = 121/39690000
implied Tscale_sigma = a4/kappa_sigma = 53/9800

=== ORACLE D: Lambda=0 DERIVED -- M=0 => R=S=Weyl=0 (flat, not inserted) ===
M=0: Rscalar = 0  => R==0? True
M=0: S_zero? True  weyl_zero? True  R_zero? True
=> M=0 vacuum is FLAT (R=S=Weyl=0), DERIVED, NOT an inserted Lambda. Tripwire does NOT fire: True
```

- **Oracle A** confirms the metric_signature notation flag is benign: `eta_bg` is genuinely (1,3) Lorentzian regardless of the `(-,+,+,+)`/`(+,-,-,-)` string label, and every decisive quantity is computed from `eta_bg` directly. The claimed inverse is correct.
- **Oracle B** confirms a_4, the kappa ratios, and the NOT-(-R/2) guard independently (kappa_psi structure = 121*kappa/158760000 matches the .tex's (0,1) entry; 158760000 = 4*39690000).
- **Oracle D** independently confirms `Lambda=0` is DERIVED: with matter={} the engine returns R=S=Weyl=0 — flat vacuum from the geometry, NO Lambda subtraction. The deflation guard ("inserted-Lambda circularity") is correctly STRUCK.

---

## Physics Consistency (universal verifier registry)

| # | Check | Status | Confidence | Notes |
|---|-------|--------|------------|-------|
| 5.1 | Dimensional analysis | CONSISTENT | INDEPENDENTLY CONFIRMED | All quantities dimensionless (0,2) tensors / rationals in (beta,gamma,p,q); natural units; exact over Q |
| 5.2 | Numerical spot-check | PASS | INDEPENDENTLY CONFIRMED | kappa, a_4, anchors, residuals reproduced at test values |
| 5.3 | Limiting cases | LIMITS_VERIFIED | INDEPENDENTLY CONFIRMED | ||M||->0: T->0 AND G[g]->0 (M=0 => R=S=Weyl=0, Oracle D); G~O(||M||^4) (G/t^4 stabilizes, G/t^3->0) |
| 5.4 | Independent cross-check | PASS | INDEPENDENTLY CONFIRMED | Totaro vs hand-rolled Levi-Civita byte-identical (5 components); Oracles A/B/D independent of drivers |
| 5.5 | Intermediate spot-check | PASS | INDEPENDENTLY CONFIRMED | Order anchors (h^(2) field, box-hbar, Lorenz defect) reproduced as intermediate regression |
| 5.6 | Symmetry | VERIFIED | INDEPENDENTLY CONFIRMED | T symmetric (T==T.T); eta_bg signature (1,3) preserved; family all sig (1,3) |
| 5.7 | Conservation | VERIFIED | INDEPENDENTLY CONFIRMED | d^mu T_munu = [0,0,0,0] exact over Q for both T (box psi=0, harmonic) |
| 5.8 | Math consistency | CONSISTENT | INDEPENDENTLY CONFIRMED | Index raising via eta_bg^{-1} (T) / g^{-1} (G) correct; n=4 reconstruction R=Scal+E+Weyl exact (resid_zero=True); no sign/factor errors found |
| 5.9 | Numerical convergence | N/A | UNABLE TO VERIFY | Symbolic exact-over-Q, no discretization; amplitude-series leading-order read empirically (G/t^4 stabilizes) |
| 5.10 | Agreement with prior | AGREES | INDEPENDENTLY CONFIRMED | Rscalar(M_0)~4008 == Phase-72 R_full; a_4=395268903/24010000 == handoff; h^(1)=0 consistent |
| 5.11 | Physical plausibility | PLAUSIBLE | INDEPENDENTLY CONFIRMED | trace_S=0 (S genuinely traceless); curved (R!=0,S!=0,Weyl!=0) consistent with Phase-72; out-of-splice points honestly dropped |
| 5.12 | Statistical rigor | N/A | N/A | No stochastic/MC content; exact arithmetic |
| 5.13 | Thermodynamic | N/A | N/A | Not applicable (pure geometry) |
| 5.14 | Spectral/analytic | N/A | N/A | Not applicable |

**GR/Cosmology domain checks:** Einstein tensor G_munu = Ric - (1/2)gR (full nonlinear, lower index) correctly assembled; Bianchi/conservation structure respected on the matter side (d^mu T=0); signature (1,3) asserted at each family point; reconstruction exact over Q. The negative result (G not = kappa T + Lambda g) is the substantive finding, not a computational failure.

**Mandatory gates:** Gate A (cancellation) — exact over Q, no float cancellation. Gate B (analytic-numeric cross-validation) — Totaro vs hand-rolled exact match. Gate C (integration measure) — N/A (no coordinate integrals). Gate D (approximation validity) — amplitude series M=t*M_0 inside the sig-(1,3) splice; controlling check eig_signature_count==(1,3,0) enforced at every point, out-of-splice dropped.

---

## Forbidden Proxy Audit

| Proxy ID | Status | Evidence |
|----------|--------|----------|
| fp-import-supergravity | REJECTED | No GST/SUSY/-R/2/Weinberg in T, kappa, fit. GST geometry-only. Negative result on intrinsic data alone. AST-guarded; engine ALL_PASS. |
| fp-assume-einstein | REJECTED | AST guard empty (code-use). a_4 frozen NUMBER. kappa frozen before G; != -R/2. Single-point match rejected in code; residual exact (~7209), not rounded. |
| fp-ensemble-gravity | REJECTED | No delta Q=T dS / entropy-area / Unruh. Jacobson named+rejected. |
| fp-float-decisive | REJECTED | All decisive G,g entries real rationals over Q; sympy linsolve/real_roots; floats only in prints. |
| fp-wrong-cross-term | REJECTED | det_3 2Re((x2 x1)x3) SSOT; octonion_algebra.py banned; engine rejects (x1 x2)x3 off-by-16. |

---

## True-Strength Assessment (negative-result-is-success)

The verdict NONE (curved but not Einstein-structured) is recorded as a **decisive, full-pass NEGATIVE result on the milestone's strongest claim**, and is correctly framed at true strength in BOTH directions:

- **Not inflated:** No "leading-order Einstein" fallback (the t^4 fit is equally negative for both T); no near-miss rounding (kappa*T is ~10^3 smaller than G[g] and differently structured — confirmed: G_00~6151 but T[psi]_00=0; G_33~178 but kappa T_33~-8.2). The obstruction is the tensor STRUCTURE (S!=0, Weyl!=0), not a constant offset.
- **Not deflated:** Lambda=0 is DERIVED from the KKT det_2 Minkowski form (Oracle D: M=0 => R=S=Weyl=0 from the engine, no subtraction), NOT an inserted-Lambda circularity. The "inserted-Lambda tripwire" correctly does NOT fire. The route SURVIVED Phase-71 (homogeneity) and Phase-72 (matter-sourcing); only G=kappa T+Lambda g fails. The surviving content (curved, matter-sourced spacetime slice) stands.

This matches the binding project guidance (feedback_noneinstein_vacuum_not_reference_choice): name the result at true strength in both directions.

**Human ratification:** The .tex records the verdict as HUMAN-RATIFIED (B. Ehrlich, 2026-06-01) at the Plan-73-02 blocking checkpoint, with the orchestrator independently re-running the driver. This verifier ADDITIONALLY re-ran all scripts and independent oracles and reproduces every decisive number. The verdict is robust and not self-ratified.

---

## Anti-Patterns

Scan of `73-01-build-T-kappa.py`, `73-02-einstein-test.py`, `73-einstein-structure.tex`: **clean.** No TODO/FIXME/PLACEHOLDER (audit confirms 0 placeholders remain), no suppressed warnings, no bare excepts, no numpy ranks on the decisive path. AST-based circularity guards are a positive pattern (distinguish code-use from comment-mention).

---

## Cross-Phase Consistency (vs Phase 72)

- **Notation:** OK on all physics. h^(1)=0, a_4=395268903/24010000, M_0, R_full~4008, S!=0/Weyl!=0 all consumed consistently; regression Rscalar(M_0,center) independently reproduced.
- **Approximations:** amplitude series M=t*M_0 / leading curvature O(||M||^4) consistent with Phase-72 h^(1)=0; validity (sig-(1,3) splice) enforced.
- **Convention (INFO, non-blocking):** `gpd regression-check` flags a `convention_conflict` on metric_signature: state.json convention_lock reads `(-,+,+,+)` while the plan/72-handoff write `(+,-,-,-)`. Oracle A independently confirms the operational eta_bg is genuinely (1,3) Lorentzian regardless of the +/- string, and every decisive quantity is computed from eta_bg directly — so this affects no result. Both SUMMARYs and the audit honestly self-flag it as a notation aliasing for the notation-coordinator (carried from Phase 71/72/73-01). **Recorded as INFO, not a blocker.**
- **Stale-ROADMAP reconciliation:** The audit correctly reconciles two stale pre-70.1 ROADMAP strings — (a) SC#2 "box-hbar^(2) ~ kappa T" (superseded: gauge-degenerate, full G[g] is decisive) and (b) line 116-117 "Lambda=0 inserted by center-subtraction circularity tripwire" (superseded: Lambda=0 DERIVED, tripwire does not fire). Both supersessions trace to the Phase-70.1 human-ratified reframe; the machine-readable convention_lock is clean. Non-blocking.

---

## Confidence Assessment

**HIGH.** Every decisive contract target is INDEPENDENTLY CONFIRMED by re-execution: the engine ALL_PASS (exit 0), the 73-01 BUILD half (BUILD_T_KAPPA_OK), and the decisive 73-02 test (EINSTEIN_TEST_OK, exit 0) all reproduced their headline numbers exactly over Q, and four independent oracles (eta_bg signature, kappa-vs-(-R/2), a_4, Lambda=0-derived) confirm the key intermediates without relying on the drivers. The negative verdict (NONE) is genuine: both stress-tensor candidates fail the single-global-(kappa,Lambda) fit at finite M, at t^4 leading order, and under a 120-equation over-determined solve; the residual is large (~7209) and the curvature carries genuine S!=0 (10/16) and Weyl!=0 (72/256). The circularity audit (VALD-05) is complete and correct — all five forbidden proxies rejected, the GST-coincidence trap addressed, and the Lambda=0-derived / box-hbar-gauge-degenerate reconciliations present and independently verified. The only open item is a benign metric-signature notation string mismatch, already self-flagged as non-blocking for the notation-coordinator and confirmed (Oracle A) to affect no decisive quantity.

**No expert verification required.** The verdict is human-ratified, computationally reproduced, and reported at true strength.

---

## Summary

Phase 73 achieved its GOAL: it posed the strongest can-fail Einstein-structure test honestly (an independent, conserved, G-free T frozen before G was computed) and reported the honest level NONE (curved but not Einstein-structured) at true strength — neither inflated nor deflated. This is the contract's explicitly-acceptable full-pass outcome and the milestone's honest prior. All 8 contract targets VERIFIED, all 5 forbidden proxies REJECTED, exact over Q throughout. **status: passed.** This closes milestone v17.0.
