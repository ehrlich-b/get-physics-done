---
phase: 73-c-einstein-structure
plan: 01
depth: complex
one-liner: "BUILD half of the Phase-C Einstein test (DERV-03): FROZE both independent stress tensors -- PRIMARY single-scalar T[psi] (psi=2Re((x2 x1)x3)) + ALTERNATIVE 16-field sigma T[V_{1/2}] -- each symmetric + EXACTLY conserved (box=0, cross-term linear-in-slice => harmonic) + vanishing as ||M||->0 + V_1-inert + provably NO Ric/R/G (AST-guarded); froze kappa_psi=32016781143/5929 and kappa_sigma=395268903/129850 from intrinsic R/T scales at ONE ref direction; reproduced the order anchors exact over Q (G^(1)[h^(2)]=0, box(hbar^(2))!=0, Lorenz defect!=0) => linear test DEGENERATE, 73-02 uses full nonlinear G[g] at O(||M||^4); added h2_field(x)+box to the engine (ALL_PASS); KEY FINDING: T[psi]~t^4==R-order (structurally matched) but T_sigma~t^2 (ORDER-MISMATCH => disconfirms the sigma candidate)."

subsystem: [computation, derivation, validation]
tags: [linearized-gravity, stress-energy-tensor, einstein-structure, scalar-stress-tensor, sigma-model, octonions, h3o, jordan-algebra, freudenthal-determinant, totaro-curvature, lorentzian-signature, circularity-audit, exact-over-Q, derv-03]

requires:
  - phase: 72-b-matter-sourcing (Plan 02)
    provides: "h^(1)=0 + the h^(2) center matrix + a_4=395268903/24010000 + the decisive M_0 (MATTER_L + BG_HALF, triple -13/63000) + the SURVIVES-qualified greenlight; the box-hbar~kappaT handoff instruction"
  - phase: 72-b-matter-sourcing (Plan 01)
    provides: "validated curvature-of-g engine spacetime_curvature_of_g (B1 difference-of-cone-Hessians, indices raised by g^{-1}=(eta+h)^{-1}, Totaro==hand-rolled) + ricci_decomposition_n4 + flat M=0 baseline + det_3 SSOT + eta_bg null-aligned"
  - phase: 70.1-revise-a0
    provides: "g=eta+h is the physical spacetime metric (eta flat KKT DERIVED from det_2); cone-Hessian=matter SOURCE; Lambda=0, NO Lambda tripwire"
provides:
  - "h2_field(matter_delta, bg_delta) added to the engine -- the LEADING (quadratic) metric response h^(2)(x) as an EXACT rational FIELD over (beta,gamma,p,q); reduces to the Phase-72 handoff h^(2) matrix at the center (REGRESSION)"
  - "box(field) added to the engine -- the flat-background d'Alembertian 4 d_beta d_gamma - d_p^2 - d_q^2, built FROM eta_bg^{-1} (null-aligned, asserted), NOT a hard-coded diag"
  - "the FROZEN PRIMARY single-scalar stress tensor T[psi]: psi(x;M)=2Re((x2 x1)x3) via the det_3 SSOT; T_munu = d_mu psi d_nu psi - (1/2) eta_bg_munu (d psi)^2; symmetric + EXACTLY conserved (box psi=0) + T->0 as ||M||->0 + V_1-inert + NO Ric/R/G"
  - "the FROZEN ALTERNATIVE sigma-model stress tensor T[V_{1/2}]: 16-component multiplet (the octonion components of (x2 x1),(x1 x3)), G_ab=delta; symmetric + conserved + vanishing + V_1-inert + NO Ric/R/G; genuinely distinct tensor structure from T[psi]"
  - "the FROZEN intrinsic couplings kappa_psi=32016781143/5929 and kappa_sigma=395268903/129850 (= a_4 / T-leading-scale at ONE reference direction; NOT -R/2, NOT per-point)"
  - "the reproduced order-counting anchors exact over Q: G^(1)_munu[h^(2)]=0, R^(1)[h^(2)]=0, box(hbar^(2))!=0 ((0,0)=-76221/2450,(3,3)=-38637/1225), Lorenz defect [19143/9800,9747/4900,297/350,0]!=0 -- the linear test is DEGENERATE => 73-02 uses the full nonlinear G[g] at O(||M||^4)"
  - "the KEY STRUCTURAL FINDING for 73-02: T[psi] has tr_eta T ~ t^4 == the curvature order (structurally MATCHED), but T_sigma has tr_eta T ~ t^2 (ORDER MISMATCH) => the single-scalar T[psi] is the structurally-favored Einstein candidate; the sigma order-mismatch is a disconfirming signal"
  - "the circularity-audit scaffold (VALD-05): T3/T4 rows CERTIFIED intrinsic with all 3 forbidden imports rejected; 73-02 G[g] rows = TODO-73-02 placeholders"
affects: [73-02-einstein-structure-test]

methods:
  added:
    - "h2_field(x): t^2-coefficient of the B1 difference-of-cone-Hessians h_sym_t with the slice KEPT symbolic (the Phase-72 field-extraction pattern, NOT substituting the center) => the leading metric response as a field"
    - "box(field): eta_bg^{ab} d_a d_b = 4 d_beta d_gamma - d_p^2 - d_q^2, coefficients read from eta_bg^{-1} (null-aligned), entrywise on a Matrix"
    - "canonical flat-background scalar stress tensor T[psi] on eta_bg from the cross-term scalar psi=2Re((x2 x1)x3) (det_3 SSOT)"
    - "16-component F_4/Spin(9,1)-covariant sigma-model stress tensor T[V_{1/2}] (G_ab=delta, the octonion norm bilinear)"
    - "intrinsic kappa := (t^k leading curvature R-scale a_4) / (t^k leading T-scale tr_eta T) at ONE reference direction, frozen as a global constant"
    - "AST-based circularity guard: walk the T/kappa code's ast.Name/ast.Attribute ids for forbidden curvature/import symbols (sees CODE USE, not comment-mentions of the constraint)"
  patterns:
    - "the cross-term scalar psi (and the sigma channels) are LINEAR in the slice coords => harmonic (box=0) => the scalar/sigma stress tensors are EXACTLY conserved (not merely on-shell) on the flat eta_bg background"
    - "order-matching as a structural Einstein discriminant: a candidate T whose trace shares the curvature's leading t-power (t^4) can be matched by a constant kappa; one that does not (t^2) cannot -- the order-mismatch is a disconfirming signal reported honestly, not forced"

key-files:
  created:
    - ".gpd/phases/73-c-einstein-structure/73-01-build-T-kappa.py (driver: order anchors + both T candidates + both kappa + the frozen PHASE73_HANDOFF for 73-02)"
    - ".gpd/phases/73-c-einstein-structure/73-circularity-audit.md (VALD-05 per-equation provenance scaffold; T3/T4 certified, 73-02 placeholders)"
  modified:
    - "code/bulk_geometry_verification.py (Section 14: h2_field(x), box(), _eta_bg_const(); engine still ALL_PASS exit 0)"

key-decisions:
  - "BUILD half complete (DERV-03): T (both candidates) and kappa (both) are FROZEN from intrinsic V_{1/2} cross-term / cubic-norm data BEFORE any G_munu[g] is computed (73-02 computes G). AST-guarded: NO Ric/R/G symbol is USED in the construction of T or kappa."
  - "DECISIVE CAN-FAIL outcome = the test CAN be posed honestly: BOTH T candidates are symmetric + conserved (EXACTLY, since the cross-term scalar channels are linear-in-slice => harmonic => box=0) + vanishing at the flat ||M||->0 vacuum + provably Einstein/G-free. (Had the only conserved T required a Ric/R/G input, the audit would instead record that no independent T exists -- it did not.)"
  - "KEY STRUCTURAL FINDING (honest, not forced): tr_eta T[psi] ~ t^4 = the SAME leading order as R[g] ~ a_4 t^4 => T[psi] is the structurally-matched Einstein candidate. tr_eta T_sigma ~ t^2 (the sigma fields carry a matter^1 x slice ~ t^1 piece) => an ORDER MISMATCH vs the t^4 curvature => a constant kappa cannot match T_sigma to G; the sigma candidate is disfavored. 73-02 must read this as a disconfirming signal for T_sigma and treat T[psi] as primary."
  - "The order anchors are REPRODUCED (not rediscovered) exact over Q, confirming the FRESH research: G^(1)[h^(2)]=0 (gauge-invariant linear Einstein content vanishes, REQUIRED by R=O(||M||^4)); box(hbar^(2))!=0 is PURE GAUGE (h^(2) not in Lorenz gauge); => the linear box-hbar test is DEGENERATE and the decisive 73-02 test is the FULL nonlinear G_munu[g]=Ric-(1/2)gR at O(||M||^4)."
  - "kappa frozen via the R-scale/T-scale ratio at ONE reference direction (NOT -R/2, NOT per-point): kappa_psi=32016781143/5929, kappa_sigma=395268903/129850 (the latter via T_sigma's OWN t^2 leading scale, carrying the order-mismatch flag). The 73-02 family test asks whether the SAME kappa holds for ALL (M,x)."

patterns-established:
  - "Linear-in-slice cross-term scalars are harmonic => exact conservation of the flat-background stress tensor (no on-shell condition needed; the on-shell box psi=0 holds identically)."
  - "Order-matching (t-power of tr_eta T vs t-power of R) is a structural pre-test of Einstein-compatibility, applied BEFORE the full G[g] fit."
  - "AST-based forbidden-symbol guards (not text grep) correctly distinguish code-USE from comment-MENTION of a constraint being honored."

conventions:
  - "natural units (hbar=c=k_B=1); EXACT over Q on every decisive quantity (fp-float-decisive rejected; ranks/signatures via sympy, never numpy)"
  - "spacetime metric g = eta_bg + h(x;M), mostly-minus; eta_bg = constant null-aligned KKT pullback [[0,1/2,0,0],[1/2,0,0,0],[0,0,-1,0],[0,0,0,-1]] (eta_bg^{-1}=[[0,2,0,0],[2,0,0,0],[0,0,-1,0],[0,0,0,-1]])"
  - "box = eta_bg^{ab} d_a d_b = 4 d_beta d_gamma - d_p^2 - d_q^2 (built from eta_bg^{-1}, NEVER a hard-coded diag); h^(1)=0 so the leading response is h^(2)"
  - "det_3 Freudenthal cross-term 2Re((x2 x1)x3), SSOT = code/bulk_geometry_verification.py (octonion_algebra.py BANNED)"
  - "Lambda = 0 (M=0 vacuum flat-DERIVED from KKT det_2, NO Lambda tripwire); T,kappa raised/lowered with eta_bg (flat background), NOT g"
  - "NOTE: state.json convention_lock records metric_signature as 'mostly-minus (-,+,+,+ ...)'; the plan/72-handoff write '(+,-,-,-)'. The OPERATIONAL object is the engine eta_bg (null-aligned, (1,3) Lorentzian) which both agree on; the +/- string mismatch is a non-blocking notation aliasing flagged for the notation-coordinator (does not affect any decisive quantity, all of which are computed from eta_bg directly)."

plan_contract_ref: ".gpd/phases/73-c-einstein-structure/73-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-einstein-structure:
      status: partial
      summary: "BUILD half complete (this plan establishes the FROZEN independent RHS + the field machinery + the order anchors + the audit scaffold; the honest-LEVEL Einstein verdict is 73-02). The independent T_munu (PRIMARY T[psi] + ALTERNATIVE sigma T[V_{1/2}]) and kappa (kappa_psi, kappa_sigma) are FROZEN from intrinsic V_{1/2} cross-term content, symmetric + EXACTLY conserved + vanishing at flat ||M||->0 + provably Einstein/G-free (AST-guarded), BEFORE any G is computed (DERV-03). The h^(2)(x) field + box are added to the engine. The order anchors are reproduced exact over Q => the linear test is DEGENERATE, fixing the FULL nonlinear G[g] at O(||M||^4) as the decisive 73-02 test. KEY FINDING: T[psi]~t^4 (structurally matched to the curvature) but T_sigma~t^2 (order-mismatch, disfavored)."
      linked_ids: [deliv-T-build, deliv-h2-field, deliv-audit-scaffold, test-T-conserved, test-order-anchors, ref-prompt, ref-gst, ref-jacobson-contrast, ref-72-handoff, ref-warm-engine]
      evidence:
        - verifier: gpd-executor
          method: "engine extension + driver: B1 difference-of-cone-Hessians t^2-field, gauge-general linearized Einstein operator (eta_bg^{-1}-raised), canonical scalar + sigma stress tensors, amplitude-series leading-order, AST circularity guard -- all exact over Q"
          confidence: high
          claim_id: claim-einstein-structure
          deliverable_id: deliv-T-build
          acceptance_test_id: test-T-conserved
          reference_id: ref-warm-engine
          evidence_path: ".gpd/phases/73-c-einstein-structure/73-01-build-T-kappa.py"
  deliverables:
    deliv-T-build:
      status: produced
      path: ".gpd/phases/73-c-einstein-structure/73-01-build-T-kappa.py"
      summary: "The FROZEN independent stress tensors (PRIMARY single-scalar T[psi] + ALTERNATIVE 16-field sigma T[V_{1/2}]), the intrinsic kappa (kappa_psi=32016781143/5929, kappa_sigma=395268903/129850), and the reproduced order-counting anchors -- all exact over Q, all built with NO Ric/R/G input (AST-guarded). must_contain items all present: T[psi]=d psi d psi-(1/2)eta(d psi)^2; sigma-model T[V_{1/2}]; symmetric + d^mu T_munu=0 (EXACT, box psi=0) + T->0 as ||M||->0; kappa a fixed rational from the t^k R/T-scale at ONE reference direction (NOT -R/2, NOT per-point); anchors G^(1)[h^(2)]=0, R^(1)=0, box(hbar^(2))!=0, Lorenz defect!=0. The h^(2)(x) field is emitted via the engine routine (deliv-h2-field)."
      linked_ids: [claim-einstein-structure, test-T-conserved, test-order-anchors]
    deliv-h2-field:
      status: produced
      path: "code/bulk_geometry_verification.py"
      summary: "Engine Section 14: h2_field(matter_delta, bg_delta) returns the h^(2)(x) FIELD (t^2-coeff of the B1 difference-of-cone-Hessians h_sym_t, slice symbolic) -- an EXACT rational function of (beta,gamma,p,q) that reduces to the Phase-72 handoff h^(2) matrix at the center (REGRESSION verified). box(field) = 4 d_beta d_gamma f - d_p^2 f - d_q^2 f built from eta_bg^{-1} (null-aligned, asserted). Engine still ALL_PASS, exit 0. must_contain items both present."
      linked_ids: [claim-einstein-structure, test-order-anchors]
    deliv-audit-scaffold:
      status: produced
      path: ".gpd/phases/73-c-einstein-structure/73-circularity-audit.md"
      summary: "The VALD-05 per-equation provenance table: one row per T3/T4 equation (psi, T[psi], the sigma fields, T_sigma, conservation, the ||M||->0/V_1 controls, the R/T-scales, kappa) -- each CERTIFIED intrinsic (det_3 SSOT + eta_bg + cubic norm) with explicit fp-import-supergravity / fp-assume-einstein / fp-ensemble-gravity PASS. The GST very-special-geometry coincidence trap is explicitly addressed (cite for geometry/orientation ONLY); the Jacobson route is named and rejected. 73-02 G[g] rows are present as TODO-73-02 placeholders. must_contain items both present."
      linked_ids: [claim-einstein-structure, test-T-conserved]
  acceptance_tests:
    test-T-conserved:
      status: passed
      summary: "PASSED for BOTH candidates, exact over Q. (1) T==T.T symmetric (both). (2) d^mu T_munu = 0 with the index raised by eta_bg^{-1}: EXACTLY conserved (not merely on-shell) -- the conservation identity d^mu T_munu = (box psi)(d_nu psi) holds and box psi = 0 because psi (and every sigma channel phi^a) is LINEAR in the slice coords => harmonic. (3) T->0 as ||M||=t->0 (both). NO Ric/R/G symbol appears anywhere in the construction (AST-guarded over the T-functions; forbidden-id uses = {}). V_1-only control: T=0 (V_1 alpha inert). => the Einstein test CAN be posed honestly in 73-02."
      linked_ids: [claim-einstein-structure, deliv-T-build, deliv-audit-scaffold]
    test-order-anchors:
      status: passed
      summary: "PASSED, reproduced exact over Q on the h^(2)(x) field at the center: G^(1)_munu[h^(2)] == zero 4x4 (full gauge-general linearized Einstein tensor), R^(1)[h^(2)] == 0, box(hbar^(2)) != 0 ((0,0)=-76221/2450, (3,3)=-38637/1225), Lorenz defect d^mu hbar^(2)_munu = [19143/9800, 9747/4900, 297/350, 0] != 0. h^(2)(x) at center == the handoff matrix (REGRESSION). DOCUMENTED: box(hbar^(2)) is pure gauge (h^(2) not in Lorenz gauge), the linear test is DEGENERATE => the decisive 73-02 test is the FULL nonlinear G[g] at O(||M||^4)."
      linked_ids: [deliv-h2-field, deliv-T-build]
  references:
    ref-prompt:
      status: completed
      completed_actions: [read]
      missing_actions: []
      summary: "paper6-bulk-geometry-prompt.md Phase-C reporting discipline honored: T from V_1/V_{1/2} built BEFORE the G test; 'curved but not Einstein-structured is acceptable, do NOT force' carried as the 73-02 framing; the honest order-mismatch finding (T_sigma~t^2 disfavored) is reported at true strength."
    ref-gst:
      status: completed
      completed_actions: [cite, avoid]
      missing_actions: []
      summary: "GST very-special-real geometry (E_{6(-26)}/F_4, a_IJ=-(1/3)Hess ln N) cited for the GEOMETRY/ORIENTATION ONLY in the circularity audit; its Lagrangian / SUSY-fixed couplings / -R/2 are NOT used as an input to T or kappa (fp-import-supergravity rejected; the sigma G_ab=delta is the octonion norm, NOT the GST scalar-manifold metric). AST-guarded."
    ref-jacobson-contrast:
      status: completed
      completed_actions: [cite, avoid]
      missing_actions: []
      summary: "Jacobson 1995 named in the audit and REJECTED as a method (fp-ensemble-gravity): no delta Q = T dS, no entropy-area, no Unruh-T. T and kappa come from the algebra's cubic-norm geometry, one observer, one off-center point."
    ref-72-handoff:
      status: completed
      completed_actions: [read, compare]
      missing_actions: []
      summary: "Phase-72 handoff consumed: h^(1)=0, the h^(2) center matrix (REGRESSION anchor for h2_field), a_4=395268903/24010000 (the R-scale for kappa), the decisive M_0, the box-hbar~kappaT instruction (demoted to a documented gauge diagnostic since the linear test is degenerate)."
    ref-warm-engine:
      status: completed
      completed_actions: [read, use]
      missing_actions: []
      summary: "code/bulk_geometry_verification.py EXTENDED in place (Section 14: h2_field, box, _eta_bg_const) reusing cone_hessian_offcenter (B1), _eta_minkowski/_frame_jacobian_bg_to_mink, det_3 SSOT, oct_mul; engine NOT rebuilt; octonion_algebra.py NOT imported; ALL_PASS exit 0 preserved."
  forbidden_proxies:
    fp-import-supergravity:
      status: rejected
      notes: "NO GST Lagrangian / N=2 SUSY closure / -R/2 fixed by SUSY / Weinberg soft-graviton enters T or kappa. GST cited for geometry/orientation ONLY (the slice IS very-special-real geometry -- acknowledged in the audit, not used). The sigma target metric G_ab=delta is the octonion Euclidean norm, NOT a GST coupling. AST-guarded over both the T-functions and the kappa statements (forbidden-id uses = {} / [])."
    fp-assume-einstein:
      status: rejected
      notes: "NO Ric/R/G symbol USED in the construction of T or kappa (AST guard sees CODE USE, not comment-mentions of the constraint). a_4 is a FROZEN rational NUMBER (the t^4 curvature scale at ONE reference direction) -- NOT a live spacetime_curvature_of_g/Ricci call and NOT a per-point tensor fit. kappa is a GLOBAL constant frozen BEFORE G[g] is computed (DERV-03); kappa_psi,kappa_sigma both != -R/2 (=-395268903/48020000). The full G[g] tensor is NOT computed in this plan (it is 73-02's LHS); the only curvature object here is the linearized G^(1)[h^(2)] degeneracy cross-check built from the metric response h^(2), not from any assumed RHS."
    fp-ensemble-gravity:
      status: rejected
      notes: "No observers-make-gravity / Jacobson-style thermodynamic step. No delta Q = T dS, no entropy-area, no Unruh temperature. T and kappa come from the algebra's own cubic-norm geometry (det_3 cross-term 2Re((x2 x1)x3)), one observer, one off-center point M_0."
  uncertainty_markers:
    weakest_anchors:
      - "WHICH T candidate (if either) carries the bulk G structure is the open design choice resolved only in 73-02. This plan FREEZES both at MEDIUM confidence, but ADDS a structural discriminant: T[psi]~t^4 is order-matched to the curvature while T_sigma~t^2 is not, favoring T[psi]. (Open Q1 partially advanced: the sigma candidate is now disfavored on order grounds.)"
      - "kappa's operational definition (a_4 / t^k T-scale at ONE reference direction) is MEDIUM confidence: it is global and non-circular by construction (one frozen number, NOT per-point), but whether the SAME kappa reproduces G[g] for ALL (M,x) is the 73-02 family test (the strong/exact vs leading vs none level)."
    disconfirming_observations:
      - "T_sigma's eta-trace leads at t^2, NOT the t^4 curvature order -- a constant kappa cannot match a t^4 curvature to a t^2 stress trace, so the sigma candidate is structurally disfavored for the Einstein match. Reported honestly (NOT forced); 73-02 should treat T[psi] as primary and read the sigma order-mismatch as disconfirming."
      - "The CAN-FAIL gate did NOT trip: T could be made conserved AND Einstein/G-free, so the Einstein test CAN be posed honestly. (If 73-02 finds no global (kappa,Lambda) reproduces G[g] even at leading order, the honest result is 'curved but not Einstein-structured' -- an ACCEPTABLE outcome, do NOT force Einstein form.)"

comparison_verdicts:
  - subject_id: test-order-anchors
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-72-handoff
    comparison_kind: cross_method
    metric: exact_equality_over_Q
    threshold: "the THIS-research order anchors reproduced exact over Q on the h^(2)(x) field at the center: G^(1)[h^(2)]=0, R^(1)=0, box(hbar^(2))!=0 ((0,0)=-76221/2450), Lorenz defect [19143/9800,9747/4900,297/350,0]!=0; h^(2)(x) center == handoff matrix"
    verdict: pass
    recommended_action: "Use the FULL nonlinear G[g] at O(||M||^4) as the decisive 73-02 Einstein test (the linear box-hbar test is gauge-degenerate); demote box(hbar^(2)) to a documented gauge diagnostic."
    notes: "Every anchor reproduced to the exact rational of the independent FRESH-research computation; h^(2)(x)|center == the Phase-72 handoff matrix (regression). G^(1)[h^(2)]=0 is the order-consistency cross-check (REQUIRED by R=O(||M||^4)). box(hbar^(2))!=0 is pure gauge (h^(2) not in Lorenz gauge). fp-float-decisive avoided."
  - subject_id: test-T-conserved
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-warm-engine
    comparison_kind: consistency
    metric: exact_symmetry_conservation_vanishing_over_Q
    threshold: "BOTH T candidates symmetric + d^mu T_munu=0 (eta_bg-raised) + T->0 as ||M||->0 + NO Ric/R/G; else the Einstein test cannot be posed honestly"
    verdict: pass
    recommended_action: "Pose the 73-02 Einstein test with T[psi] as PRIMARY (order-matched, t^4) and T_sigma as a documented alternative (order-mismatched, t^2, disfavored); kappa frozen as a global constant."
    notes: "Both candidates: symmetric over Q; EXACTLY conserved (box psi = box phi^a = 0, since every cross-term scalar channel is linear-in-slice => harmonic) -- stronger than the merely-on-shell condition the plan allowed; T->0 as t->0; V_1-only control gives T=0. AST guard confirms NO Ric/R/G/Einstein/Riemann/spacetime_curvature/octonion_algebra USED in the construction. The can-fail gate did NOT trip."

duration: "~28 min (1 bounded execution segment: Tasks 1-5; engine baseline + Task1 verify + 3 driver runs + 2 grep-guard->AST fixes + 1 order-mismatch correction + final regression)"
completed: 2026-06-01
---

# Phase 73-01 (BUILD the frozen Einstein-test RHS) Summary

**BUILD half of the Phase-C Einstein-structure test complete (DERV-03 discipline).** The independent stress-energy tensor `T_mu_nu` (PRIMARY single-scalar `T[psi]` + ALTERNATIVE 16-field sigma `T[V_{1/2}]`) and the intrinsic coupling `kappa` (`kappa_psi`, `kappa_sigma`) are FROZEN from the V_{1/2} cross-term content -- each `T` symmetric + EXACTLY conserved + vanishing at the flat `||M||->0` vacuum + provably free of any Einstein/G input -- BEFORE any `G_mu_nu[g]` is computed (that is 73-02). The `h^(2)(x)` field + `box` are added to the engine, the order-counting anchors are reproduced exact over Q (so the linear test is DEGENERATE and the decisive 73-02 test is the full nonlinear `G[g]` at O(||M||^4)), and the circularity-audit scaffold (VALD-05) is stood up. **KEY FINDING:** `T[psi]` has `tr_eta T ~ t^4` == the curvature order (structurally MATCHED), but `T_sigma ~ t^2` (ORDER MISMATCH) -- so the single-scalar `T[psi]` is the structurally-favored Einstein candidate and the sigma order-mismatch is a disconfirming signal, reported honestly.

## Performance

- **Duration:** ~28 min (1 bounded execution segment; foreground `python3 -u` throughout, watchdog-safe -- longest step the h^(2)(x) field + linearized operators at ~85s)
- **Completed:** 2026-06-01
- **Tasks:** 5 (all committed atomically)
- **Files:** 1 engine modified, 2 created (driver + audit)

## Key Results

- **h2_field(x) + box added to the engine [CONFIDENCE: HIGH -- exact over Q + regression].** `h2_field(MATTER_L, BG_HALF)` returns the leading metric response as an EXACT rational field over `(beta,gamma,p,q)` (e.g. `h2[0,0] = (-232 gamma^3 + 308 gamma^2 p - 245 gamma p^2 - 245 gamma q^2)/(29400 det_2(V_0)^2)` -- slice symbols in the `det_2(V_0)^2` denominator, a genuine field). At the center it reduces EXACTLY to the Phase-72 handoff matrix `[[261/1225,0,99/700,0],[0,9/40,99/700,0],[99/700,99/700,4293/9800,0],[0,0,0,4293/9800]]` (REGRESSION). `box = 4 d_beta d_gamma - d_p^2 - d_q^2` built from `eta_bg^{-1}` (asserted null-aligned). Engine still ALL_PASS, exit 0.
- **PRIMARY T[psi] FROZEN [CONFIDENCE: HIGH -- exact over Q].** `psi(x;M_0) = 11p/6300 - 13/63000` (via the engine `det_3` cross-term `2Re((x2 x1)x3)`; center value `-13/63000` == the Phase-72 non-vacuity triple). `T_munu = d_mu psi d_nu psi - (1/2) eta_bg_munu (d psi)^2`. Symmetric; **EXACTLY conserved** (`d^mu T_munu = (box psi)(d_nu psi) = 0` since `box psi = 0`, `psi` linear-in-slice => harmonic); `T->0` as `||M||->0` (`psi(t) = 11p t^2/6300 - 13 t^3/63000`); V_1-only control gives `T=0`. NO Ric/R/G (AST-guarded). `T[psi]` center = `[[0,121/158760000,0,0],[121/158760000,0,0,0],[0,0,121/79380000,0],[0,0,0,-121/79380000]]`.
- **ALTERNATIVE sigma T[V_{1/2}] FROZEN [CONFIDENCE: HIGH -- exact over Q].** 16-component multiplet = the octonion components of `(x2 x1)` and `(x1 x3)`, `G_ab = delta` (the V_{1/2} octonion norm). Symmetric; conserved (all 16 `box phi^a = 0`); `T->0` as `||M||->0`; V_1-inert. NO Ric/R/G. `T_sigma` center = `[[0,53/39200,0,0],[53/39200,0,0,0],[0,0,0,0],[0,0,0,0]]` -- a genuinely DISTINCT tensor structure from `T[psi]` (the (2,2),(3,3) entries vanish, unlike `T[psi]`).
- **kappa FROZEN intrinsically [CONFIDENCE: MEDIUM -- novel definition, global-by-construction].** `kappa := (R-scale a_4) / (t^k T-scale)` at the ONE reference direction `M_0`, held fixed. `kappa_psi = 32016781143/5929` (`= a_4 / (121/39690000)`, T[psi] at t^4); `kappa_sigma = 395268903/129850` (`= a_4 / (53/9800)`, T_sigma at its own t^2). Both exact rationals; both `!= -R/2` (`= -395268903/48020000`); NOT per-point.
- **Order anchors reproduced exact over Q [CONFIDENCE: HIGH -- matches independent research to the exact rational].** `G^(1)_munu[h^(2)] = 0` (zero 4x4), `R^(1)[h^(2)] = 0`, `box(hbar^(2)) != 0` ((0,0)=`-76221/2450`, (3,3)=`-38637/1225`), Lorenz defect `[19143/9800, 9747/4900, 297/350, 0] != 0`. The linear box-hbar test is DEGENERATE (the nonzero `box(hbar^(2))` is pure gauge since `h^(2)` is not in Lorenz gauge; the gauge-invariant `G^(1)[h^(2)] = 0`). **=> the decisive 73-02 test is the FULL nonlinear `G_munu[g] = Ric - (1/2) g R` at O(||M||^4).**
- **KEY STRUCTURAL FINDING (the order discriminant) [CONFIDENCE: HIGH -- exact over Q].** `tr_eta T[psi] = 121 t^4/39690000` (leads at `t^4` == the curvature order `R ~ a_4 t^4`) but `tr_eta T_sigma = 53 t^2/9800` (leads at `t^2`). The sigma fields contain a `matter^1 x slice ~ t^1` piece (=> `d phi ~ t^1`, `(d phi)^2 ~ t^2`), whereas `psi` is `matter^2 x slice ~ t^2` (=> `T[psi] ~ t^4`). **A constant `kappa` can match a `t^4` curvature to a `t^4` stress trace (`T[psi]`) but NOT to a `t^2` one (`T_sigma`)** -- so `T[psi]` is the structurally-matched Einstein candidate and `T_sigma` is disfavored. Reported at true strength, not forced.
- **Circularity-audit scaffold (VALD-05) [CONFIDENCE: HIGH].** T3/T4 rows certified intrinsic (`det_3` SSOT + `eta_bg` + cubic norm); all three forbidden imports rejected (`fp-import-supergravity`, `fp-assume-einstein`, `fp-ensemble-gravity`); GST cited for geometry-only + the subtle very-special-geometry coincidence trap explicitly addressed; Jacobson route named and rejected; 73-02 `G[g]` rows = `TODO-73-02` placeholders.

## Task Commits

1. **Task 1: add h2_field(x) + box to the engine (Section 14)** -- `e3b6a236` (implement) [field reduces to handoff at center; box from eta_bg^{-1}; ALL_PASS exit 0]
2. **Task 2: reproduce + freeze the order-counting anchors** -- `89a76114` (compute) [G^(1)[h^(2)]=0, R^(1)=0, box(hbar^(2))!=0, Lorenz defect!=0; linear test degenerate]
3. **Task 3: build both independent T_munu candidates** -- `fe562f69` (compute) [PRIMARY T[psi] + ALTERNATIVE sigma T[V_{1/2}]; symmetric+conserved+vanishing+V_1-inert; NO Ric/R/G]
4. **Task 4: freeze kappa intrinsically** -- `d76745eb` (compute) [kappa_psi=32016781143/5929, kappa_sigma=395268903/129850; NOT -R/2, NOT per-point; T_sigma order-mismatch flagged]
5. **Task 5: circularity-audit scaffold (VALD-05)** -- `23168138` (document) [T3/T4 certified; 3 forbidden imports rejected; GST geometry-only; 73-02 placeholders]

## Equations Derived / Reproduced

**Eq. (73-01.1)** -- the box operator on the null-aligned constant background:
$$\Box f = \eta_{bg}^{ab}\partial_a\partial_b f = 4\,\partial_\beta\partial_\gamma f - \partial_p^2 f - \partial_q^2 f$$

**Eq. (73-01.2)** -- the PRIMARY cross-term scalar and its stress tensor (flat background `eta_bg`):
$$\psi(x;M) = 2\,\mathrm{Re}\big((x_2 x_1)x_3\big),\qquad T^{[\psi]}_{\mu\nu} = \partial_\mu\psi\,\partial_\nu\psi - \tfrac12\,\eta^{bg}_{\mu\nu}\,\eta_{bg}^{ab}\partial_a\psi\,\partial_b\psi$$
with `psi(x;M_0) = 11p/6300 - 13/63000`, `box psi = 0` (linear-in-slice => harmonic) => `d^mu T_munu = 0` exactly.

**Eq. (73-01.3)** -- the ALTERNATIVE sigma-model stress tensor (`G_ab = delta`, 16 V_{1/2} channels):
$$T^{[\sigma]}_{\mu\nu} = \delta_{ab}\,\partial_\mu\phi^a\partial_\nu\phi^b - \tfrac12\,\eta^{bg}_{\mu\nu}\,\delta_{ab}\,\eta_{bg}^{cd}\partial_c\phi^a\partial_d\phi^b,\qquad \phi^a = \big[(x_2 x_1)_a,\,(x_1 x_3)_a\big]$$

**Eq. (73-01.4)** -- the frozen intrinsic couplings (R-scale / T-scale at the ONE reference direction):
$$\kappa_\psi = \frac{a_4}{[t^4]\,\mathrm{tr}_\eta T^{[\psi]}} = \frac{395268903/24010000}{121/39690000} = \frac{32016781143}{5929},\qquad \kappa_\sigma = \frac{a_4}{[t^2]\,\mathrm{tr}_\eta T^{[\sigma]}} = \frac{395268903}{129850}$$

**Eq. (73-01.5)** -- the reproduced order anchors (the linear test is degenerate):
$$G^{(1)}_{\mu\nu}[h^{(2)}] = 0,\quad R^{(1)}[h^{(2)}] = 0,\quad \Box\bar h^{(2)}_{00} = -\tfrac{76221}{2450}\neq 0,\quad \partial^\mu\bar h^{(2)}_{\mu\nu} = \Big[\tfrac{19143}{9800},\tfrac{9747}{4900},\tfrac{297}{350},0\Big]\neq 0$$

## Validations Completed

- **Engine regression:** `python3 code/bulk_geometry_verification.py` -> ALL_PASS, exit 0, 0 failures (BEFORE and AFTER the Section-14 extension).
- **h^(2)(x) center regression:** `h2_field(MATTER_L, BG_HALF)` at the center == the Phase-72 handoff matrix exactly over Q; symmetric; genuine rational field (slice symbols in the denominator).
- **box spot-checks:** `box(beta gamma)=4`, `box(p^2)=-2`, `box(q^2)=-2`, `box(p q)=0`, `box(const)=0`; entrywise on a Matrix verified.
- **Order anchors:** all four reproduced to the exact rational of the independent FRESH research; all real rationals (no Wick/float contamination).
- **T symmetry/conservation/vanishing:** both candidates symmetric; `d^mu T_munu = 0` exactly (box of every channel = 0); `T(t=0) = 0`; V_1-only control `T = 0`. Conservation identity `d^mu T_munu = (box psi)(d_nu psi)` verified.
- **AST circularity guard:** forbidden-id uses = `{}` over the T-functions and `[]` over the kappa statements (NO Ric/R/G/Einstein/Riemann/spacetime_curvature/GST/SUSY/Weinberg/supergravity/octonion_algebra USED in code).
- **kappa NOT -R/2:** `kappa_psi, kappa_sigma != -a_4/2 = -395268903/48020000`; both fixed rationals (no free symbols).
- **det_3 SSOT:** `psi` via `oct_mul` (Fano `e1 e2 = e4`), NOT `octonion_algebra.py` (BANNED); byte-identical SSOT preserved.

## Decisions Made

- **Both T candidates built and frozen (DERV-03), not just the one that "works":** PRIMARY `T[psi]` and ALTERNATIVE sigma `T[V_{1/2}]`, both BEFORE any G is computed. 73-02 picks/tests; 73-01 freezes.
- **Conservation is EXACT, not merely on-shell:** the plan allowed "document the on-shell condition," but the cross-term scalar channels are linear in the slice coords => harmonic => `box = 0` => `d^mu T_munu = 0` identically. Recorded as the stronger result.
- **kappa via the R-scale/T-scale ratio at ONE reference direction, frozen:** `kappa_psi`, `kappa_sigma` (the sigma via its own t^2 leading scale). The 73-02 family test asks whether the SAME kappa holds for all (M,x).
- **Order-mismatch reported as a structural discriminant (honest, not forced):** `T[psi]~t^4` matched, `T_sigma~t^2` not => `T[psi]` is the structurally-favored Einstein candidate; 73-02 treats it as primary.

## Deviations from Plan

- **[Rule 3 - structural finding]** The plan's Task 4 prescribed `kappa := (t^4 R-scale)/(t^4 T-scale)` for both candidates. The sigma model's eta-trace was found to lead at **t^2**, NOT t^4 (a genuine physics fact: the sigma fields carry a `matter^1 x slice ~ t^1` piece). Handled by defining `kappa_sigma` via T_sigma's OWN leading (t^2) scale and FLAGGING the t^2-vs-t^4 order mismatch as a disconfirming signal for the sigma candidate -- reported honestly, NOT forced into a t^4 form. This sharpens the 73-02 design (T[psi] primary, T_sigma disfavored). PRIMARY T[psi] is t^4 exactly as the plan expected.
- **[Rule 1 - code bug] (x2)** The initial circularity guard used a text regex over the source, which false-positived on the driver's OWN comment/docstring mentions of the constraint ("NO Ric/R/G", "cite GST", "no SUSY/Weinberg"). Fixed by replacing the text grep with an AST-based guard (walks `ast.Name`/`ast.Attribute` ids in the T/kappa code), which inherently sees CODE USE, not comment-mentions. (A tokenize-strip intermediate fix also failed on mid-file fragments -- the TokenError fallback returned the source unmodified; the AST approach is the correct fix.) No physics affected; the guard now correctly reports zero forbidden-symbol uses.

## Issues Encountered

- **Convention string aliasing (non-blocking, flagged for notation-coordinator):** `.gpd/state.json` `convention_lock.metric_signature` reads `"mostly-minus (-,+,+,+ ...)"` while the plan frontmatter and the Phase-72 handoff write `(+,-,-,-)`. The OPERATIONAL object is the engine `eta_bg` (constant null-aligned, signature (1,3)), which both descriptions agree denotes the Lorentzian KKT slice; every decisive quantity here is computed directly from `eta_bg`/`eta_bg^{-1}`, so the `+/-`-string mismatch does not touch any result. Recorded in CONVENTIONS for the pending notation-coordinator follow-up (same one already noted in the Phase-71/72 records).

## Open Questions

- **Which T (if either) carries the bulk G structure** -- now partially advanced: `T[psi]` is order-matched (t^4) to the curvature and `T_sigma` is not (t^2), favoring `T[psi]`. The full answer is the 73-02 `G[g] = kappa T + Lambda g` family fit.
- **Does the frozen `kappa_psi` reproduce `G[g]` for ALL (M,x)** (exact / leading-order / not at all) -- the 73-02 can-fail test. The honest prior (given S!=0, Weyl!=0 at finite M from Phase 72) is "curved but not Einstein-structured"; build 73-02 to report that cleanly, do NOT force.
- **The ~6% V_{1/2} self-norm second channel** (Phase-72 caveat) -- whether it complicates a clean `T` for the full (M,x) family is a 73-02 / general-M question.

## Cross-Phase Dependencies

### Results This Phase Provides To Later Phases

| Result | Used By Phase | How |
| --- | --- | --- |
| FROZEN T[psi] (center matrix + builder) + T_sigma | 73-02 | the independent RHS; 73-02 tests G[g] = kappa T + Lambda g (T[psi] PRIMARY, order-matched) |
| FROZEN kappa_psi=32016781143/5929, kappa_sigma=395268903/129850 | 73-02 | the global coupling constants for the (M,x) family fit (NOT -R/2, NOT per-point) |
| h2_field(x) + box engine routines | 73-02 | the field machinery (h^(2)(x), box) for the gauge diagnostic + any leading-order check |
| order anchors + the "use full nonlinear G[g] at O(||M||^4)" decision | 73-02 | fixes the decisive test (linear box-hbar is gauge-degenerate) |
| order-mismatch finding (T_sigma~t^2 vs R~t^4) | 73-02 | treat T[psi] as primary; read the sigma order-mismatch as disconfirming |
| circularity-audit scaffold (T3/T4 certified) | 73-02 | complete the C.a/C.b/C.c rows after the full G[g] test |

### Results This Phase Consumed From Earlier Phases

| Result | From Phase | Verified Consistent |
| --- | --- | --- |
| h^(1)=0, h^(2) center matrix, a_4=395268903/24010000, decisive M_0 | 72-02 | Yes -- h2_field(center)==handoff; a_4 used as the R-scale |
| validated curvature-of-g engine + B1 difference-of-cone-Hessians + det_3 SSOT + eta_bg | 72-01 | Yes -- extended in place (Section 14); ALL_PASS preserved |
| g=eta+h physical metric; M=0 flat DERIVED; cone-Hessian=source; Lambda=0 | 70.1 | Yes -- T,kappa on the flat eta_bg; NO Lambda tripwire |

### Convention Changes

| Convention | Previous | This Phase | Reason |
| --- | --- | --- | --- |
| None -- all conventions preserved | | | g=eta+h, det_3 SSOT cross-term 2Re((x2 x1)x3), box from eta_bg^{-1}, exact over Q -- carried verbatim from 70.1/72; the metric-signature string aliasing is a pre-existing non-blocking notation item, not a change made here |

## Self-Check: PASSED

- **Files exist:** `code/bulk_geometry_verification.py` (modified, Section 14), `.gpd/phases/73-c-einstein-structure/73-01-build-T-kappa.py` (created), `.gpd/phases/73-c-einstein-structure/73-circularity-audit.md` (created), this SUMMARY -- all present.
- **Commits exist:** `e3b6a236` (T1), `89a76114` (T2), `fe562f69` (T3), `d76745eb` (T4), `23168138` (T5) -- all FOUND in git log.
- **Reproducibility:** the full driver re-runs to `BUILD_T_KAPPA_OK` exit 0; the engine re-runs to ALL_PASS exit 0; SymPy 1.14.0; all decisive quantities exact rationals (re-derived, not transcribed).
- **Convention consistency:** ASSERT_CONVENTION headers in both the engine Section 14 and the driver declare g=eta+h mostly-minus, eta_bg null-aligned, exact over Q, det_3 SSOT, Lambda=0; the metric-signature string aliasing is flagged (non-blocking).
- **Contract coverage:** ALL PLAN contract IDs present in contract_results -- 1 claim (claim-einstein-structure: partial, BUILD half), 3 deliverables (deliv-T-build, deliv-h2-field, deliv-audit-scaffold: produced), 2 acceptance tests (test-T-conserved, test-order-anchors: passed), 5 references (all completed), 3 forbidden proxies (all rejected); 2 decisive comparison_verdicts recorded.
- **Discipline:** the CAN-FAIL gate is reported at true strength (T CAN be posed honestly -> the test proceeds); the order-mismatch finding is reported (not forced); fp-import-supergravity / fp-assume-einstein / fp-ensemble-gravity / fp-float-decisive / fp-wrong-cross-term all rejected; NO Ric/R/G in T or kappa (AST-guarded).
- **gpd_return envelope:** present below.

```yaml
gpd_return:
  status: completed
  files_written:
    - "code/bulk_geometry_verification.py"
    - ".gpd/phases/73-c-einstein-structure/73-01-build-T-kappa.py"
    - ".gpd/phases/73-c-einstein-structure/73-circularity-audit.md"
    - ".gpd/phases/73-c-einstein-structure/73-01-SUMMARY.md"
  issues:
    - "Convention string aliasing (non-blocking): state.json convention_lock.metric_signature says '(-,+,+,+)' while plan/72-handoff say '(+,-,-,-)'; operationally both denote the engine eta_bg null-aligned (1,3) slice used for every decisive quantity. Flagged for the notation-coordinator (pre-existing item)."
    - "[Rule 3] The sigma-model eta-trace leads at t^2 not t^4 (genuine physics): kappa_sigma defined via its OWN t^2 leading scale with the t^2-vs-t^4 order mismatch flagged as disconfirming for the sigma candidate (NOT forced)."
    - "[Rule 1 x2] Circularity guard text-grep false-positived on the driver's own comment/docstring mentions of the constraint; fixed via an AST-based guard (code-use, not comment-mention). No physics affected."
  next_actions:
    - "/gpd:execute-phase 73 (Plan 02): the decisive Einstein-structure test -- compute the FULL nonlinear G_munu[g]=Ric-(1/2)gR at O(||M||^4) over an (M,x) family, fit GLOBAL (kappa,Lambda) against the FROZEN T[psi] (PRIMARY, order-matched) and T_sigma (alternative, order-mismatched/disfavored), report the honest level (exact / leading / 'curved but not Einstein-structured'), human verdict."
    - "73-02 must use kappa_psi=32016781143/5929 (and kappa_sigma=395268903/129850) as FROZEN; Lambda=0 expected (no tripwire); complete the audit C.a/C.b/C.c rows."
    - "notation-coordinator: reconcile the metric-signature string in state.json/CONVENTIONS (non-blocking)."
  phase: "73-c-einstein-structure"
  plan: "01"
  tasks_completed: 5
  tasks_total: 5
  duration_seconds: 1680
  conventions_used:
    units: "natural (hbar=c=k_B=1); EXACT over Q on all decisive quantities"
    metric: "mostly-minus; eta_bg constant null-aligned [[0,1/2,0,0],[1/2,0,0,0],[0,0,-1,0],[0,0,0,-1]]; g=eta+h, M=0 flat DERIVED"
    box: "4 d_beta d_gamma - d_p^2 - d_q^2 (from eta_bg^{-1})"
    cross_term: "det_3 Freudenthal 2Re((x2 x1)x3), SSOT bulk_geometry_verification.py; octonion_algebra.py BANNED"
    Lambda: "0 (M=0 flat-DERIVED, NO tripwire)"
  checkpoint_hashes:
    - hash: "e3b6a236"
      message: "implement(73-01): add h2_field(x) + box to engine (Section 14)"
    - hash: "89a76114"
      message: "compute(73-01): reproduce order-counting anchors exact over Q"
    - hash: "fe562f69"
      message: "compute(73-01): build BOTH independent T_munu candidates exact over Q"
    - hash: "d76745eb"
      message: "compute(73-01): freeze kappa intrinsically exact over Q"
    - hash: "23168138"
      message: "document(73-01): circularity-audit scaffold (VALD-05)"
```

---

_Phase: 73-c-einstein-structure_
_Completed: 2026-06-01_
