---
phase: 73-c-einstein-structure
plan: 02
depth: complex
one-liner: "DECISIVE can-fail Einstein test (FINAL verdict of v17.0): full nonlinear G_munu[g] over a 12-point (M,x) family (all sig (1,3), Totaro==hand-rolled, G first at O(||M||^4)) is NOT reproduced by kappa T + Lambda g for ANY single global (kappa,Lambda) -- against NEITHER frozen T (T[psi] t^4-matched primary, T_sigma t^2 order-mismatched), at finite-M OR t^4 order; R not prop to g at even one point (best-Lambda residual ~7209/7190), kappa T ~10^3 smaller than G; n=4 decomp R~4008, S!=0 (10/16), Weyl!=0 (72/256). HUMAN-RATIFIED honest level = NONE (curved but not Einstein-structured) -- a decisive full-pass NEGATIVE result on the milestone's strongest claim; route SURVIVED Ph71+72, only G=kappa T+Lambda g fails."

subsystem: [computation, validation, analysis, derivation]
tags: [einstein-equations, einstein-structure, stress-energy-tensor, full-nonlinear-einstein-tensor, ricci-decomposition, weyl-tensor, traceless-ricci, totaro-curvature, lorentzian-signature, octonions, h3o, jordan-algebra, freudenthal-determinant, negative-result, circularity-audit, exact-over-Q, calc-05, milestone-v17-final]

requires:
  - phase: 73-c-einstein-structure (Plan 01)
    provides: "the FROZEN independent RHS -- PRIMARY T[psi] (psi=2Re((x2 x1)x3)) + ALTERNATIVE sigma T[V_{1/2}], each symmetric+EXACTLY conserved+vanishing+V_1-inert+NO Ric/R/G (AST-guarded); kappa_psi=32016781143/5929 (t^4-matched) + kappa_sigma=395268903/129850 (t^2 order-mismatch); the h2_field/box engine routines; the order anchors => full nonlinear G[g] at O(||M||^4) is decisive; the structural order discriminant (T[psi] favored)"
  - phase: 72-b-matter-sourcing (Plan 02)
    provides: "h^(1)=0; a_4=395268903/24010000 (the t^4 R-scale); the decisive M_0; R~a_4||M||^4 with S!=0 & Weyl!=0; the SURVIVES-qualified greenlight; M=0 flat DERIVED"
  - phase: 72-b-matter-sourcing (Plan 01)
    provides: "the validated curvature-of-g engine spacetime_curvature_of_g (B1, indices raised by (eta+h)^{-1}, Totaro==hand-rolled) + ricci_decomposition_n4 + eig_signature_count + det_3 SSOT + eta_bg null-aligned"
  - phase: 70.1-revise-a0
    provides: "g=eta+h is the physical spacetime metric (eta flat KKT DERIVED from det_2); cone-Hessian=matter SOURCE; Lambda=0, NO Lambda tripwire"
provides:
  - "the DECISIVE can-fail Einstein test EXECUTED: full nonlinear G_munu[g]=Ric[g]-(1/2)g R[g] over a 12-point (M,x) family, exact over Q, all sig (1,3); NO single global (kappa,Lambda) reproduces it against EITHER frozen T at finite-M OR t^4 order"
  - "the HUMAN-RATIFIED honest Einstein-structure level for milestone v17.0: NONE (curved but not Einstein-structured)"
  - "the exact-over-Q evidence: best per-point Lambda leaves a residual with 10/16 nonzero entries (largest ~7209 for T[psi], ~7190 for T_sigma); R is NOT proportional to g at even one point; kappa T ~10^3 smaller than G and differently structured; 120-eq global Lambda-solve INCONSISTENT for both candidates"
  - "the n=4 Ricci decomposition at the anchor M_0 (exact reconstruction over Q): R~4007.98, traceless-Ricci S!=0 (10/16 entries), Weyl!=0 (72/256 entries), trace_S=0; consistent across sampled family points"
  - "the COMPLETED circularity audit (VALD-05): C.a/C.b/C.c rows certified + the stale-ROADMAP reconciliation (box-hbar gauge-degenerate; Lambda=0 DERIVED) + the final no-forbidden-import certification"
  - "derivations/73-einstein-structure.tex with the HUMAN-RATIFIED verdict recorded at true strength"
  - "the 73-02 Einstein-test driver (imports the frozen 73-01 RHS, does NOT rebuild)"
affects: [milestone-v17.0-closure, paper6-bulk-geometry]

methods:
  added:
    - "full nonlinear Einstein tensor G_munu = Ric_munu - (1/2) g_munu R (lower index, indices raised by g^{-1}=(eta+h)^{-1}) assembled from the engine spacetime_curvature_of_g over an (M,x) family"
    - "the single-GLOBAL-(kappa,Lambda) can-fail test: with kappa frozen, R_munu = G_munu - kappa T_munu must equal Lambda g_munu for ONE global Lambda over ALL points+components -- tested via (a) per-point trace-forced Lambda + residual, (b) a 120-equation over-determined linsolve over Q; single-point matches REJECTED"
    - "exact-over-Q t^4 leading-order fit via rational polynomial interpolation of G,T,g in the amplitude t (the engine needs rational matter, so the t^4 coefficient is read by interpolating across rational t-samples)"
    - "frozen-RHS import pattern: importing the 73-01 driver module RUNS it once (~77s) and exposes the field-valued T builders + PHASE73_HANDOFF kappa, evaluated at the SAME slice point as G"
  patterns:
    - "T (flat-background, eta_bg-raised) evaluated as a FIELD at the same slice point x where G[g] is computed => the Einstein equation is compared like-for-like, pointwise over the family"
    - "signature gate as a splice boundary: assert eig_signature_count(g)==(1,3,0) at EACH point; full-strength matter that flips to Euclidean is DROPPED (not forced) -- 6 of 18 candidate points dropped honestly"
    - "magnitude+structure mismatch as the honest non-Einstein witness: kappa T ~10^3 smaller than G[g] and a different sparsity pattern => not a near-miss, a decisive non-match"

key-files:
  created:
    - ".gpd/phases/73-c-einstein-structure/73-02-einstein-test.py (the Einstein-test driver: family G[g], the global (kappa,Lambda) fit for both T candidates at finite-M + t^4, the n=4 S/Weyl decomposition + classification)"
    - ".gpd/phases/73-c-einstein-structure/73-02-SUMMARY.md (this file)"
  modified:
    - "derivations/73-einstein-structure.tex (deliv-phaseC: the explicit T, the G vs kappa T + Lambda g comparison with exact residuals, the honest level, the S/Weyl evidence, the HUMAN-RATIFIED verdict at true strength)"
    - ".gpd/phases/73-c-einstein-structure/73-circularity-audit.md (deliv-audit-final: C.a/C.b/C.c rows certified + stale-ROADMAP reconciliation + final VALD-05 certification)"

key-decisions:
  - "HUMAN-RATIFIED VERDICT (B.Ehrlich, 2026-06-01): the honest Einstein-structure level is NONE (curved but not Einstein-structured). NOT self-ratified; the orchestrator independently re-ran the driver and reproduced every decisive number exact over Q. This is the FINAL verdict of milestone v17.0."
  - "TRUE-STRENGTH framing (binding): a DECISIVE, full-pass NEGATIVE result on the milestone's STRONGEST claim (G=kappa T+Lambda g), NOT a method failure and NOT 'the route is dead'. The route SURVIVED Phase-71 (homogeneity) + Phase-72 (matter-sourcing); only the strong-form Einstein-structure claim fails. NOT inflated (no 'leading-order Einstein', no rounding); NOT deflated (Lambda=0 is DERIVED from KKT det_2, NOT an inserted-Lambda circularity)."
  - "kappa FROZEN from 73-01 (NOT re-fit): the test asks whether the SAME frozen kappa works GLOBALLY; only Lambda is fit as a global constant (no consistent Lambda exists). A single-point match (2 constants vs 10 components at one point) is explicitly REJECTED (fp-assume-einstein)."
  - "T[psi] is PRIMARY (t^4-matched to the curvature); T_sigma is the order-mismatched (t^2) alternative carried for completeness. NEITHER matches -- so the order-mismatch was not the only obstruction; the tensor STRUCTURE (S!=0, Weyl!=0) is the genuine obstruction, which no constant kappa or Lambda can repair."

patterns-established:
  - "The decisive Einstein test is the FULL nonlinear G[g] at O(||M||^4), NOT the linearized box-hbar (which is gauge-degenerate: G^(1)[h^(2)]=0, box-hbar^(2) pure gauge)."
  - "A non-Einstein curvature is reported at true strength via the n=4 S/Weyl decomposition + the exact global-fit residual; 'curved but not Einstein-structured' is an ACCEPTABLE full result, not forced into Einstein form and not deflated into a circularity."

conventions:
  - "natural units (hbar=c=k_B=1); EXACT over Q on every decisive quantity (fp-float-decisive rejected; ranks/signatures via sympy real_roots, never numpy)"
  - "spacetime metric g = eta_bg + h(x;M), mostly-minus; eta_bg constant null-aligned [[0,1/2,0,0],[1/2,0,0,0],[0,0,-1,0],[0,0,0,-1]]; G_munu[g]=Ric-(1/2)gR (FULL nonlinear, lower index), indices raised by g^{-1}=(eta+h)^{-1}; T raised by eta_bg (flat background)"
  - "det_3 Freudenthal cross-term 2Re((x2 x1)x3), SSOT = code/bulk_geometry_verification.py (octonion_algebra.py BANNED)"
  - "Lambda = 0 (M=0 vacuum flat-DERIVED from KKT det_2, NO Lambda tripwire); Lambda offered as a free global fit constant (no consistent value exists)"
  - "NOTE: state.json convention_lock.metric_signature reads '(-,+,+,+)' while the plan/handoff write '(+,-,-,-)'; the OPERATIONAL object is the engine eta_bg null-aligned (1,3) slice used for every decisive quantity; the +/- string mismatch is a non-blocking notation aliasing flagged for the notation-coordinator (carried from Phase 71/72/73-01)"

plan_contract_ref: ".gpd/phases/73-c-einstein-structure/73-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-einstein-structure:
      status: passed
      summary: "RESOLVED at true strength: the honest Einstein-structure level is REPORTED and HUMAN-RATIFIED = NONE (curved but not Einstein-structured). No single global (kappa,Lambda) reproduces the full nonlinear G_munu[g(x)] against EITHER independently-frozen T candidate (PRIMARY T[psi] t^4-matched; ALTERNATIVE T_sigma t^2 order-mismatched), at finite M OR at the t^4 leading order, over a 12-point (M,x) family (all sig (1,3)). The claim's pass_condition is met: the level is reported plainly, NOT forced into Einstein form; a per-point or import-dependent 'match' is rejected; the verdict is human-ratified. 'Curved but not Einstein-structured' is the explicitly-acceptable outcome of this claim."
      linked_ids: [obs-einstein-structure, deliv-phaseC, deliv-audit-final, test-einstein-level, ref-prompt, ref-gst, ref-jacobson-contrast, ref-72-handoff, ref-warm-engine]
      evidence:
        - verifier: gpd-executor
          method: "full nonlinear G[g] over a 12-point (M,x) family (all sig (1,3), Totaro==hand-rolled cross-checked, G first at O(||M||^4)); single GLOBAL (kappa,Lambda) fit for both frozen T at finite-M (per-point trace-Lambda + 120-eq over-determined linsolve) and t^4 order; n=4 ricci_decomposition_n4 (S,Weyl) -- all exact over Q; verdict HUMAN-ratified + orchestrator-reproduced"
          confidence: high
          claim_id: claim-einstein-structure
          deliverable_id: deliv-phaseC
          acceptance_test_id: test-einstein-level
          reference_id: ref-warm-engine
          evidence_path: ".gpd/phases/73-c-einstein-structure/73-02-einstein-test.py"
  observables:
    obs-einstein-structure:
      status: passed
      summary: "Einstein-structure level (proof obligation) = NONE. Over the (M,x) family with a single GLOBAL (kappa,Lambda) and kappa frozen from 73-01: G[g] != kappa T + Lambda g for either T, at exact (finite-M) AND leading (t^4) order. The honest level is reported."
      linked_ids: [claim-einstein-structure]
  deliverables:
    deliv-phaseC:
      status: produced
      path: "derivations/73-einstein-structure.tex"
      summary: "Phase C write-up: the explicit candidate T_mu_nu (both, referenced from 73-01, independent of any assumed Einstein form); the order-counting resolution (box-hbar pure gauge => full G[g] at O(||M||^4)); the (M,x)-family G vs kappa T + Lambda g comparison at exact (finite-M) and t^4 order with the EXACT residuals (G[g] O(6000), kappa_psi T[psi] O(4-8), best-Lambda residual ~7209); the honest level NONE; the S/Weyl evidence (R~4008, S!=0 10/16, Weyl!=0 72/256, trace_S=0); the completed circularity audit; the negative-result-is-success framing; the HUMAN-RATIFIED verdict (2026-06-01) at true strength. All four must_contain items present. LaTeX balanced (6 equation/1 align/2 enumerate/3 pmatrix/1 itemize/1 quote, 269/269 braces)."
      linked_ids: [claim-einstein-structure, test-einstein-level]
    deliv-audit-final:
      status: produced
      path: ".gpd/phases/73-c-einstein-structure/73-circularity-audit.md"
      summary: "The COMPLETED per-equation provenance table (VALD-05): the 73-02 rows C.a (G[g] computation), C.b (the global (kappa,Lambda) fit), C.c (the honest-level S/Weyl decomposition) all FILLED and CERTIFIED intrinsic; the stale-ROADMAP reconciliation note added (SC#2 box-hbar gauge-degenerate => full G[g]; Lambda=0 DERIVED from KKT det_2, the inserted-Lambda tripwire does NOT fire); final certification: NO fp-import-supergravity / fp-assume-einstein / fp-ensemble-gravity (+ carried fp-float-decisive / fp-wrong-cross-term) anywhere in either plan. Both must_contain items present; 0 TODO-73-02 placeholders remain."
      linked_ids: [claim-einstein-structure, test-einstein-level]
  acceptance_tests:
    test-einstein-level:
      status: passed
      summary: "PASSED (its pass_condition is to REPORT the honest level, not to find Einstein structure). With T and kappa FROZEN from 73-01, the FULL nonlinear G_munu[g(x)] was computed over a 12-point (M,x) family (3 matter dirs x 3 slice positions x 2 amplitudes; sig (1,3) asserted at each via eig_signature_count, 6 out-of-splice points DROPPED not forced; Totaro-vs-hand-rolled cross-checked on 5 components exact over Q). G = kappa T + Lambda g was tested for a SINGLE global (kappa,Lambda) over the family, exact over Q, at finite M (per-point trace-Lambda + 120-eq over-determined linsolve) AND at the t^4 leading order; ricci_decomposition_n4 gave S,Weyl. RESULT: honest level = NONE ('curved but not Einstein-structured'): no global (kappa,Lambda) reproduces G[g] even at leading order; S!=0 and Weyl!=0 with structure NOT proportional to any independent T. Reported plainly, NOT forced. A per-point / single-point / import-dependent 'match' was REJECTED. The verdict is HUMAN-ratified (not self-ratified)."
      linked_ids: [claim-einstein-structure, deliv-phaseC, deliv-audit-final]
  references:
    ref-prompt:
      status: completed
      completed_actions: [read]
      missing_actions: []
      summary: "paper6-bulk-geometry-prompt.md Phase-C reporting discipline honored: the Einstein test was posed (G=kappa T+Lambda g at exact/linear/none) with T from V_1/V_{1/2}; the binding discipline 'curved but not Einstein-structured is acceptable, do NOT force' is the reported outcome (NONE), neither inflated nor deflated."
    ref-gst:
      status: completed
      completed_actions: [cite, avoid]
      missing_actions: []
      summary: "GST very-special-real geometry (E_{6(-26)}/F_4) cited for the GEOMETRY/ORIENTATION ONLY in the audit + the .tex; its Lagrangian / SUSY-fixed -R/2 coupling is NOT used as an input (fp-import-supergravity rejected). The negative result was reached on intrinsic data alone, so the GST-coincidence trap had no opportunity to manufacture a match."
    ref-jacobson-contrast:
      status: completed
      completed_actions: [cite, avoid]
      missing_actions: []
      summary: "Jacobson 1995 named in the audit + .tex and REJECTED as a method (fp-ensemble-gravity): no delta Q=T dS, no entropy-area, no Unruh-T. G[g], T, kappa come from the algebra's own cubic-norm geometry, one observer, one off-center point."
    ref-72-handoff:
      status: completed
      completed_actions: [read, compare]
      missing_actions: []
      summary: "Phase-72 handoff consumed + cross-checked: a_4=395268903/24010000 used as the R-scale (via kappa); the decisive M_0 anchors the family; G[g] computed on the SAME g (B1) Phase 72 used -- REGRESSION confirmed Rscalar(M_0,center)~4007.98 == Phase-72 R_full exact over Q; h^(1)=0 => leading curvature at O(||M||^4) (G/t^4 stabilizes)."
    ref-warm-engine:
      status: completed
      completed_actions: [use]
      missing_actions: []
      summary: "code/bulk_geometry_verification.py reused (NOT rebuilt, octonion_algebra.py NOT imported): spacetime_curvature_of_g (full Ric[g],R[g] => G[g] at each family point ~3s), ricci_decomposition_n4 (S,Weyl), hand_rolled_riemann_of_g (Levi-Civita cross-check, == Totaro exact over Q), eig_signature_count, det_3 SSOT. Engine ALL_PASS exit 0 (baseline re-confirmed)."
  forbidden_proxies:
    fp-import-supergravity:
      status: rejected
      notes: "NO GST Lagrangian / N=2 SUSY closure / -R/2 fixed by SUSY / Weinberg soft-graviton enters G[g], T, kappa, or the fit. GST cited for geometry/orientation ONLY. The honest level NONE is on intrinsic data alone -- the discipline was to HALT and report non-Einstein if the only route to a match were such an import; no import was needed or used (the option 'halt-circularity' was offered and NOT selected because no import was attempted)."
    fp-assume-einstein:
      status: rejected
      notes: "kappa was FROZEN in 73-01 BEFORE G[g] was computed (DERV-03). The fit solves for a SINGLE GLOBAL Lambda over the WHOLE 12-point family (120-equation over-determined solve) + a per-point Lambda-equality test; a single-point match is explicitly REJECTED in code; no per-point tuning; a near-miss is NOT least-squares-rounded to 'Einstein'. The residual is reported EXACTLY (it is large: ~7209/~7190, R not prop to g at even one point). NO Ric/R/G symbol defined T or kappa (AST-guarded in 73-01)."
    fp-ensemble-gravity:
      status: rejected
      notes: "No observers-make-gravity / Jacobson-style thermodynamic step. No delta Q=T dS, no entropy-area, no Unruh temperature. G[g] is the engine's full nonlinear curvature; T,kappa come from the cubic-norm geometry, one observer, one off-center point M_0."
    fp-float-decisive:
      status: rejected
      notes: "Every decisive quantity is EXACT over Q: the family G_munu[g] (all real rationals), the per-point + global Lambda solve (sympy linsolve over Q), the residual matrices, the n=4 S/Weyl decomposition (reconstruction residual ==0 exact), the signature (1,3) via eig_signature_count (sympy real_roots, never numpy). Floats appear ONLY in human-readable progress prints, never in a verdict."
    fp-wrong-cross-term:
      status: rejected
      notes: "psi and the sigma multiplet use the engine det_3 cross-term 2Re((x2 x1)x3) (Phase-64.1 fix), NOT octonion_algebra.py (BANNED). det_3 SSOT byte-identical to ring_lemma_verification. G[g] uses the validated spacetime_curvature_of_g (Totaro == hand-rolled cross-checked)."
  uncertainty_markers:
    weakest_anchors:
      - "WHICH T candidate carries the bulk G structure (the research Open Q1/Q3, MEDIUM confidence entering 73-02) is now RESOLVED: NEITHER. T[psi] (t^4-matched, primary) and T_sigma (t^2, alternative) both fail the global fit, so the obstruction is the tensor STRUCTURE (S!=0, Weyl!=0), not merely the sigma order-mismatch."
      - "The intrinsic kappa definition (frozen in 73-01, MEDIUM confidence) was TESTED globally and does NOT yield Einstein structure -- consistent with the 'none' level; no re-fit per direction would help, since R is not proportional to g at even one point (a constant kappa/Lambda cannot repair a structural mismatch)."
    unvalidated_assumptions: []
    competing_explanations:
      - "REJECTED: a leading-order ('linear/leading') Einstein structure -- the t^4 fit is equally negative, so there is no weaker-but-positive fallback."
      - "REJECTED: an inserted-Lambda circularity reading of the flat M=0 vacuum -- Lambda=0 is DERIVED from the KKT det_2 (B1 difference potential vanishes identically at M=0); the obstruction is structural, not a constant offset."
    disconfirming_observations:
      - "The SURPRISING POSITIVE that did NOT occur: a single global (kappa,Lambda) reproducing G[g] across the family would have been the surprise; it does not happen, confirming the honest prior (curved but not Einstein-structured, since g carries S!=0 and Weyl!=0 at finite M while the cross-term T is special)."
      - "The fit did NOT 'almost' work and was NOT rounded: kappa T is ~10^3 smaller than G[g] and differently structured; the best-Lambda residual is ~7209 (largest entry), reported exactly."

comparison_verdicts:
  - subject_id: test-einstein-level
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-warm-engine
    comparison_kind: cross_method
    metric: exact_residual_over_Q (G - kappa T - Lambda g; single global (kappa,Lambda), kappa frozen)
    threshold: "zero residual for a single global (kappa,Lambda) over the 12-point family => Einstein (exact); zero at t^4 only => leading; else => NONE (curved but not Einstein-structured)"
    verdict: fail
    recommended_action: "Record the honest level as NONE (curved but not Einstein-structured) -- the decisive can-fail Einstein test FAILED to produce Einstein structure, which is the milestone's honest prior and an ACCEPTABLE full result. Do NOT force Einstein form; do NOT deflate into a circularity. Close milestone v17.0 on this human-ratified NEGATIVE verdict."
    notes: "verdict 'fail' = the Einstein-structure HYPOTHESIS fails (no single global (kappa,Lambda)); the acceptance TEST itself PASSES (its job is to report the honest level, which it did). For BOTH T candidates, at finite M (per-point trace-Lambda residual !=0 at every point; per-point Lambda all unequal; 120-eq over-determined linsolve INCONSISTENT) AND at t^4 (no single global (kappa,Lambda)). R not proportional to g at even one point; best-Lambda residual largest entry ~7209 (T[psi]) / ~7190 (T_sigma); kappa T ~10^3 smaller than G[g]. Exact over Q. Orchestrator independently reproduced."
  - subject_id: claim-einstein-structure
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-72-handoff
    comparison_kind: consistency
    metric: n4_ricci_decomposition_over_Q (S = traceless Ricci, Weyl) + ||M||->0 anchor
    threshold: "S!=0 and/or Weyl!=0 (tracking M, not a coordinate artifact) with structure NOT proportional to any independent T => 'curved but not Einstein-structured'; both T and G[g] -> 0 as ||M||->0 (the can't-fake anchor)"
    verdict: pass
    recommended_action: "Report the honest level NONE with the S/Weyl evidence at true strength; the route SURVIVED Ph71+72 (curved, matter-sourced spacetime), only the strong-form Einstein-structure claim fails."
    notes: "n=4 decomposition exact over Q (reconstruction residual ==0). At anchor M_0: R~4007.98!=0 (== Phase-72 R_full regression), traceless-Ricci S!=0 (10/16 entries), Weyl!=0 (72/256 entries), trace_S=0 (genuinely traceless); consistent across sampled family points. ||M||->0 anchor holds (both T and G[g] -> 0 on the DERIVED-flat eta_bg). This is the honest prior CONFIRMED -- g is genuinely curved (S,Weyl !=0) but that curvature is not Einstein-organized by the cross-term T."

duration: "~58 min total (1 bounded execution segment Tasks 1-3 + Task-4-automated ~37 min to the blocking checkpoint; + the post-ratification continuation ~21 min: .tex verdict at true strength + this SUMMARY)"
completed: 2026-06-01
---

# Phase 73-02 (TEST: the decisive can-fail Einstein test) Summary

**DECISIVE can-fail Einstein test EXECUTED -- the FINAL verdict of milestone v17.0.** With `T_mu_nu` and `kappa` FROZEN from 73-01, the full nonlinear Einstein tensor `G_mu_nu[g] = Ric[g] - (1/2) g R[g]` was computed over a 12-point `(M,x)` family (all sig (1,3), Totaro==hand-rolled cross-checked, first appearing at O(||M||^4)) and tested against `kappa T + Lambda g` for a SINGLE global `(kappa,Lambda)`. **RESULT (exact over Q, HUMAN-RATIFIED 2026-06-01): NONE -- curved but not Einstein-structured.** No single global `(kappa,Lambda)` reproduces `G[g]` against EITHER frozen `T` (PRIMARY `T[psi]` t^4-matched; ALTERNATIVE `T_sigma` t^2 order-mismatched), at finite `M` OR at the t^4 leading order. The curvature is not even proportional to `g` at a single point (best-`Lambda` residual largest entry ~7209/~7190); `kappa T` is three orders of magnitude smaller than `G[g]` and differently structured. The n=4 decomposition gives `R~4008`, traceless-Ricci `S!=0` (10/16), Weyl `!=0` (72/256). This is a **decisive, full-pass NEGATIVE result on the milestone's strongest claim** (negative-result-is-success) -- NOT a method failure and NOT "the route is dead": the route SURVIVED the Phase-71 homogeneity KILL gate and Phase-72 matter-sourcing; only `G=kappa T+Lambda g` fails.

## Performance

- **Duration:** ~58 min total (~37 min Tasks 1-3 + Task-4-automated to the blocking checkpoint; ~21 min post-ratification continuation). Foreground `python3 -u` throughout, watchdog-safe (progress prints between family points; matter/bg rational before `g.inv()`).
- **Completed:** 2026-06-01
- **Tasks:** 4 (Tasks 1-3 + Task-4-automated committed pre-checkpoint; the human-ratified verdict + this SUMMARY committed post-checkpoint)
- **Files:** 1 created (driver), 2 modified (.tex, audit), + this SUMMARY

## Key Results

- **NO single global `(kappa,Lambda)` reproduces `G_mu_nu[g]` [CONFIDENCE: HIGH -- exact over Q, both T candidates, both readings, orchestrator-reproduced].** For BOTH `T[psi]` (PRIMARY, `kappa_psi=32016781143/5929`, t^4-matched) and `T_sigma` (ALTERNATIVE, `kappa_sigma=395268903/129850`, t^2 order-mismatched): at FINITE M the per-point trace-forced `Lambda` leaves `R - Lambda g != 0` at EVERY family point (per-point `Lambda` all unequal), and the 120-equation over-determined global `Lambda`-solve is INCONSISTENT; at the t^4 LEADING order the same test is also negative. The best per-point `Lambda` at `M_0` (~-1062 for `T[psi]`) leaves a residual with 10/16 nonzero entries, largest |entry| ~7209 (`T[psi]`) / ~7190 (`T_sigma`). **R is NOT proportional to `g` at even one point.**
- **`kappa T` is a tiny, differently-shaped fragment of `G[g]` [CONFIDENCE: HIGH -- exact over Q].** At `M_0`, `G[g]` entries are O(6000) (e.g. `G_00~6151`, `G_11~6288`, off-diagonal `G_01~6130`), while `kappa_psi T[psi]` has only THREE nonzero entries of O(4-8) (`(0,1)~4.12`, `(2,2)~8.23`, `(3,3)~-8.23`) -- ~10^3 smaller and a completely different sparsity pattern (`G_00~6151` but `T[psi]_00=0`; `G_33~178` but `kappa T_33~-8.2`). Not a near-miss; a decisive non-match.
- **n=4 Ricci decomposition: `g` is genuinely curved, NOT Einstein [CONFIDENCE: HIGH -- exact reconstruction over Q].** At `M_0`: `R~4007.98 != 0` (== Phase-72 `R_full` regression), traceless-Ricci `S != 0` (10/16 entries), Weyl `!= 0` (72/256 entries), `trace_S = 0` (genuinely traceless); reconstruction `R = Scal+E+Weyl` exact over Q; same structure across sampled family points. The bulk of the curvature (the large `S` and Weyl) is intrinsic geometry NOT tracked by any independent matter tensor.
- **The test LHS is well-posed [CONFIDENCE: HIGH].** 12 valid sig-(1,3) family points (6 of 18 dropped where full-strength matter flips to Euclidean -- honestly dropped, not forced); `G[g] != 0` everywhere; `G` first appears at O(||M||^4) (`G_00(t)/t^4` stabilizes 88->90 as t->0, `G_00/t^3 -> 0`); Totaro == hand-rolled Levi-Civita on 5 Riemann components exact over Q; all entries real rationals (fp-float-decisive avoided).
- **||M||->0 anchor holds (the can't-fake control) [CONFIDENCE: HIGH].** Both `T` (73-01) and `G[g]` -> 0 as the matter switches off, on the DERIVED-flat `eta_bg` (KKT det_2 Minkowski). Flatness is DERIVED (the B1 difference potential vanishes identically at M=0), NOT an inserted Lambda.
- **Circularity audit COMPLETE (VALD-05) [CONFIDENCE: HIGH].** C.a/C.b/C.c rows certified intrinsic; the stale-ROADMAP reconciliation recorded (SC#2 box-hbar gauge-degenerate => full G[g]; Lambda=0 DERIVED from KKT det_2, the inserted-Lambda tripwire does NOT fire); final certification: NO fp-import-supergravity / fp-assume-einstein / fp-ensemble-gravity (+ carried fp-float-decisive / fp-wrong-cross-term) anywhere in either plan.

## Task Commits

Each task was committed atomically:

1. **Task 1: full nonlinear `G_mu_nu[g]` over the (M,x) family** -- `611cfd2b` (compute) [12 sig-(1,3) points, G!=0, O(||M||^4), Totaro==hand-rolled, Rscalar(M_0)~4008 regression]
2. **Task 2: the global (kappa,Lambda) fit -- the can-fail test** -- `3dd328f0` (compute) [NO single global Lambda for either T, finite-M + t^4, exact over Q, single-point matches rejected]
3. **Task 3: honest level via the n=4 S/Weyl decomposition** -- `4abc8338` (compute) [level NONE; S!=0 (10/16), Weyl!=0 (72/256), trace_S=0; reconstruction exact]
4. **Task 4 (automated): circularity audit + write-up** -- `399d6488` (document) [C.a/C.b/C.c certified + stale-ROADMAP reconciliation + 73-einstein-structure.tex], `232f1765` (document) [finalize audit header; 0 TODO placeholders]

**Post-ratification continuation:** the human-ratified verdict at true strength in `73-einstein-structure.tex` + this SUMMARY (committed atomically as the plan-metadata commit below).

## Files Created/Modified

- `.gpd/phases/73-c-einstein-structure/73-02-einstein-test.py` -- the Einstein-test driver (imports the frozen 73-01 RHS; family `G[g]`; the global `(kappa,Lambda)` fit for both `T` at finite-M + t^4; the n=4 `S`/Weyl decomposition + the explicit classification rule). Runs to `EINSTEIN_TEST_OK`, exit 0.
- `derivations/73-einstein-structure.tex` (deliv-phaseC) -- the explicit `T`, the order-counting resolution, the `G` vs `kappa T + Lambda g` comparison with exact residuals, the honest level NONE, the `S`/Weyl evidence, the completed audit, the HUMAN-RATIFIED verdict at true strength.
- `.gpd/phases/73-c-einstein-structure/73-circularity-audit.md` (deliv-audit-final) -- C.a/C.b/C.c rows certified + the stale-ROADMAP reconciliation + the final VALD-05 certification.

## Equations Derived / Reproduced

**Eq. (73-02.1)** -- the test (full nonlinear Einstein tensor vs the frozen RHS):
$$G_{\mu\nu}[g] = \mathrm{Ric}_{\mu\nu}[g] - \tfrac12 g_{\mu\nu}R[g] \stackrel{?}{=} \kappa\,T_{\mu\nu} + \Lambda\,g_{\mu\nu},\qquad \kappa\ \text{FROZEN},\ \Lambda\ \text{one global constant}.$$

**Eq. (73-02.2)** -- the can-fail residual (with `kappa` frozen, the unique trace-forced `Lambda`):
$$R_{\mu\nu}(x) := G_{\mu\nu}(x) - \kappa T_{\mu\nu}(x),\quad \Lambda = \tfrac1n g^{\mu\nu}R_{\mu\nu},\quad \big(R_{\mu\nu} - \Lambda g_{\mu\nu}\big)\big|_{M_0} \neq 0\ \ (\text{largest}\sim7209).$$

**Eq. (73-02.3)** -- the n=4 decomposition (genuinely curved, not Einstein):
$$R_{ijkl} = \mathrm{Scal}_{ijkl} + E_{ijkl} + C^{\mathrm{Weyl}}_{ijkl},\quad S_{ab} = \mathrm{Ric}_{ab} - \tfrac{R}{4}g_{ab} \neq 0,\quad C^{\mathrm{Weyl}} \neq 0,\quad \mathrm{tr}_g S = 0.$$

**Eq. (73-02.4)** -- the magnitude/structure witness at `M_0` (floats; exact over Q in code):
$$G_{\mu\nu}[g]\big|_{M_0}\!\approx\!\begin{pmatrix}6151&6130&1599&0\\6130&6288&1633&0\\1599&1633&974&0\\0&0&0&178\end{pmatrix},\quad \kappa_\psi T^{[\psi]}_{\mu\nu}\big|_{M_0}\!\approx\!\begin{pmatrix}0&4.1&0&0\\4.1&0&0&0\\0&0&8.2&0\\0&0&0&-8.2\end{pmatrix}.$$

## Validations Completed

- **Regression to Phase 72:** `Rscalar(M_0,center) ~ 4007.98` == Phase-72 `R_full` exactly over Q; `G[g] != 0` at `M_0`.
- **Leading order:** `G_00(t)/t^4` stabilizes (88.1 -> 89.7 -> 90.1 as t = 1/10, 1/20, 1/40); `G_00(t)/t^3 -> 0` (8.8 -> 4.5 -> 2.3) -- `G` first appears at O(||M||^4).
- **Engine cross-check:** Totaro `R_ijkl` == hand-rolled Levi-Civita `R_ijkl` on `{(0202),(2323),(0101),(1212),(0303)}` exactly over Q at the anchor.
- **Signature gate:** `eig_signature_count(g) == (1,3,0)` asserted at every family point (sympy `real_roots`, exact); 6 out-of-splice points dropped (not forced).
- **Decomposition reconstruction:** `R = Scal + E + Weyl` exact over Q (`resid_zero=True`) at all 3 sampled points.
- **Exactness/reality:** all family `G`, `g` entries real rationals (no float, no imaginary part).
- **Orchestrator independent re-run:** every decisive number reproduced exact over Q (Rscalar=4008, both fits False, S!=0 10/16, Weyl!=0 72/256, residual ~7209/7190, `EINSTEIN_TEST_OK` exit 0).
- **Engine baseline:** `code/bulk_geometry_verification.py` ALL_PASS, exit 0 (re-confirmed before building).

## Decisions Made

- **HUMAN-RATIFIED verdict NONE (B.Ehrlich, 2026-06-01), not self-ratified** -- presented at the Task-4 blocking checkpoint; the orchestrator independently reproduced every decisive number.
- **True-strength framing (binding):** a decisive full-pass NEGATIVE result on the strongest claim; the route survived Ph71+72, only `G=kappa T+Lambda g` fails. Not inflated (no leading-order Einstein, no rounding), not deflated (Lambda=0 DERIVED, not an inserted-Lambda circularity).
- **kappa frozen, only Lambda fit; single-point matches rejected** -- the test is GLOBAL consistency, exact over Q.
- **Both T candidates tested; neither matches** -- the obstruction is the tensor structure (S!=0, Weyl!=0), not merely the sigma order-mismatch.

## Deviations from Plan

**None - plan executed exactly as written.** The plan's Task 4 was a blocking `checkpoint:decision`; I ran Tasks 1-3 + the automated part of Task 4, PAUSED and returned the verdict package, and (after human ratification) recorded the verdict at true strength + wrote this SUMMARY -- exactly the prescribed interactive flow. No auto-fix deviations (Rules 1-4); no physics redirect/scope change (Rules 5-6).

## Issues Encountered

- **LaTeX toolchain absent (non-blocking).** `pdflatex`/`latexmk` are not installed on this machine, so `derivations/73-einstein-structure.tex` was not compiled to PDF here. It is a `\section` fragment for the project master document (same handling as `72-matter-sourcing.tex`), and its environment/brace balance was verified programmatically (6 equation / 1 align / 2 enumerate / 3 pmatrix / 1 itemize / 1 quote all paired; 269/269 braces; no `$$`; only standard amsmath macros). Master-doc compilation is a researcher/notation-coordinator step.
- **Convention string aliasing (pre-existing, non-blocking).** `state.json convention_lock.metric_signature` reads `(-,+,+,+)` while the plan/handoff write `(+,-,-,-)`; the operational object is the engine `eta_bg` (null-aligned (1,3)) used for every decisive quantity, so no result is affected. Flagged for the notation-coordinator (carried from Phases 71/72/73-01).

## Open Questions

- **Milestone-level (beyond v17.0 scope):** is there a DIFFERENT geometric object (not the cross-term `T`) whose Einstein tensor matches `G[g]`, or is the `h_3(O)` spacetime slice intrinsically non-Einstein? The present result answers the milestone's posed question (the algebra's own cross-term stress content does NOT Einstein-source its curvature) and closes v17.0; a broader "is any matter content Einstein-compatible" question is out of scope.
- **The ~6% V_{1/2} self-norm second channel (Phase-72 caveat):** did not rescue Einstein structure (it is part of the matter content already in `T_sigma`); noted as resolved-by-subsumption.

## Cross-Phase Dependencies

### Results This Phase Provides To Later Phases

| Result | Used By | How |
| --- | --- | --- |
| HUMAN-RATIFIED honest level NONE (curved but not Einstein-structured) | milestone v17.0 closure / paper6 | the FINAL verdict; the strong-form Einstein-structure claim is falsified, the curved-matter-sourced-spacetime content survives |
| derivations/73-einstein-structure.tex (the full Phase-C write-up) | paper6-bulk-geometry | the publishable derivation + verdict |
| 73-circularity-audit.md (complete VALD-05) | paper6 / referee | the per-equation no-forbidden-import certificate |

### Results This Phase Consumed From Earlier Phases

| Result | From Phase | Verified Consistent |
| --- | --- | --- |
| FROZEN T[psi], T_sigma + kappa_psi, kappa_sigma + order anchors | 73-01 | Yes -- imported (not rebuilt); the full-G[g]-at-O(||M||^4) decision honored |
| a_4, M_0, h^(1)=0, R~a_4||M||^4, S!=0/Weyl!=0, M=0 flat DERIVED | 72-02 | Yes -- Rscalar(M_0)~4008 regression; G first at O(||M||^4); S/Weyl confirmed |
| curvature-of-g engine (Totaro==hand-rolled), ricci_decomposition_n4, eig_signature_count, det_3 SSOT, eta_bg | 72-01 | Yes -- reused; ALL_PASS exit 0; cross-check exact over Q |
| g=eta+h physical; M=0 flat DERIVED; cone-Hessian=source; Lambda=0 | 70.1 | Yes -- G on this g; Lambda=0 DERIVED, no tripwire |

### Convention Changes

| Convention | Previous | This Phase | Reason |
| --- | --- | --- | --- |
| None -- all conventions preserved | | | g=eta+h, det_3 SSOT, box from eta_bg^{-1}, Lambda=0 DERIVED, exact over Q -- carried verbatim from 70.1/72/73-01; the metric-signature string aliasing is a pre-existing non-blocking notation item, not a change made here |

## Self-Check: PASSED

- **Files exist:** `73-02-einstein-test.py`, `73-circularity-audit.md` (complete), `derivations/73-einstein-structure.tex` (verdict at true strength), this SUMMARY -- all present.
- **Commits exist:** `611cfd2b` (T1), `3dd328f0` (T2), `4abc8338` (T3), `399d6488` + `232f1765` (T4 automated) -- all FOUND in git log; the .tex+SUMMARY plan commit below.
- **Reproducibility:** the driver re-runs to `EINSTEIN_TEST_OK`, exit 0; the orchestrator independently reproduced every decisive number exact over Q; SymPy 1.14.0; all decisive quantities exact rationals.
- **Convention consistency:** ASSERT_CONVENTION headers in the driver + .tex declare g=eta+h mostly-minus, eta_bg null-aligned, exact over Q, det_3 SSOT, Lambda=0 DERIVED; the metric-signature string aliasing is flagged (non-blocking).
- **Contract coverage:** ALL PLAN contract IDs present -- 1 claim (claim-einstein-structure: passed, level NONE), 1 observable (obs-einstein-structure: passed), 2 deliverables (deliv-phaseC, deliv-audit-final: produced), 1 acceptance test (test-einstein-level: passed -- reports the honest level), 5 references (all completed), 5 forbidden proxies (all rejected: fp-import-supergravity, fp-assume-einstein, fp-ensemble-gravity, fp-float-decisive, fp-wrong-cross-term); 2 comparison_verdicts recorded (the global-fit fail = hypothesis fails; the S/Weyl decomposition pass = honest prior confirmed).
- **Discipline:** the verdict is HUMAN-ratified (not self-ratified), recorded at true strength (not inflated, not deflated); a per-point/single-point/import-dependent match was rejected; all decisive quantities exact over Q.
- **gpd_return envelope:** present below.

```yaml
gpd_return:
  status: completed
  files_written:
    - ".gpd/phases/73-c-einstein-structure/73-02-einstein-test.py"
    - "derivations/73-einstein-structure.tex"
    - ".gpd/phases/73-c-einstein-structure/73-circularity-audit.md"
    - ".gpd/phases/73-c-einstein-structure/73-02-SUMMARY.md"
  issues:
    - "LaTeX toolchain (pdflatex/latexmk) not installed: 73-einstein-structure.tex compilation verified by exact env/brace-balance check (all paired, 269/269 braces, no $$, standard amsmath only); it is a \\section fragment for the master doc (same as 72-matter-sourcing.tex). Master-doc compile is a notation-coordinator/researcher step (non-blocking)."
    - "Pre-existing non-blocking notation aliasing: state.json convention_lock.metric_signature '(-,+,+,+)' vs plan/handoff '(+,-,-,-)'; operationally both denote the engine eta_bg null-aligned (1,3) slice. Flagged for the notation-coordinator (carried from Ph71/72/73-01)."
  next_actions:
    - "Orchestrator: transition Phase 73 to COMPLETE + close milestone v17.0 BY HAND (do NOT run buggy gpd phase complete / gpd state advance). Verdict = NONE (curved but not Einstein-structured), HUMAN-ratified."
    - "Optional gpd-verifier pass on 73-02 (the driver re-runs cheaply; the orchestrator already reproduced the decisive numbers)."
    - "notation-coordinator (non-blocking): reconcile the metric-signature string; the stale ROADMAP Phase-73 SC#2 + Lambda-tripwire wording is now reconciled in 73-circularity-audit.md."
    - "paper6-bulk-geometry: the v17.0 verdict (curved-but-not-Einstein; route survived Ph71+72, strong-Einstein claim falsified) + derivations/73-einstein-structure.tex feed the write-up."
  phase: "73-c-einstein-structure"
  plan: "02"
  tasks_completed: 4
  tasks_total: 4
  duration_seconds: 3480
  verdict: "NONE (curved but not Einstein-structured) -- HUMAN-RATIFIED 2026-06-01; FINAL verdict of milestone v17.0"
  verdict_confidence: high
  self_ratified: false
  conventions_used:
    units: "natural (hbar=c=k_B=1); EXACT over Q on all decisive quantities"
    metric: "mostly-minus; eta_bg constant null-aligned [[0,1/2,0,0],[1/2,0,0,0],[0,0,-1,0],[0,0,0,-1]]; g=eta+h; G=Ric-(1/2)gR raised by g^{-1}; T raised by eta_bg"
    cross_term: "det_3 Freudenthal 2Re((x2 x1)x3), SSOT bulk_geometry_verification.py; octonion_algebra.py BANNED"
    Lambda: "0 (M=0 flat-DERIVED from KKT det_2, NO tripwire); offered as a free global fit constant, no consistent value exists"
  checkpoint_hashes:
    - {hash: "611cfd2b", message: "compute(73-02): full nonlinear G_munu[g] over the (M,x) family exact over Q"}
    - {hash: "3dd328f0", message: "compute(73-02): global (kappa,Lambda) fit -- NO single Lambda, both T candidates, exact over Q"}
    - {hash: "4abc8338", message: "compute(73-02): honest level = NONE (curved but not Einstein) via n=4 S/Weyl decomposition exact over Q"}
    - {hash: "399d6488", message: "document(73-02): complete circularity audit + write 73-einstein-structure.tex (honest level NONE)"}
    - {hash: "232f1765", message: "document(73-02): finalize circularity-audit header (all TODO-73-02 placeholders cleared)"}
  state_updates:
    position: "Phase 73 (C — Einstein Structure), Plan 73-02 COMPLETE; the FINAL plan of milestone v17.0"
    verdict: "HUMAN-RATIFIED honest Einstein-structure level = NONE (curved but not Einstein-structured) -- the decisive can-fail Einstein test FAILED to produce Einstein structure (the milestone's honest prior, an acceptable full result). Route SURVIVED Ph71+72; only G=kappa T+Lambda g fails. Closes milestone v17.0."
    key_result: "Full nonlinear G_munu[g] over a 12-point (M,x) family (all sig (1,3), Totaro==hand-rolled, G first at O(||M||^4)) is NOT reproduced by kappa T + Lambda g for ANY single global (kappa,Lambda), against NEITHER frozen T (T[psi] kappa_psi=32016781143/5929 t^4-matched primary; T_sigma kappa_sigma=395268903/129850 t^2 order-mismatch), at finite-M OR t^4 order. R not proportional to g at even one point; best-Lambda residual largest entry ~7209 (T[psi]) / ~7190 (T_sigma); kappa T ~10^3 smaller than G. n=4 decomp: R~4007.98, S!=0 (10/16), Weyl!=0 (72/256), trace_S=0, reconstruction exact over Q. ||M||->0 anchor holds (T,G->0, flat DERIVED). Circularity audit COMPLETE: no GST/SUSY/-R/2/Weinberg/Jacobson import in either plan; stale-ROADMAP SC#2 (box-hbar gauge-degenerate) + Lambda-tripwire (Lambda=0 DERIVED) reconciled. Verdict orchestrator-reproduced exact over Q."
```

---

_Phase: 73-c-einstein-structure_
_Completed: 2026-06-01_
