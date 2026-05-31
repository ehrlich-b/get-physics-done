---
phase: 71-a-homogeneity-kill-gate
plan: 01
depth: full
one-liner: "Route-1 homogeneity KILL gate: the inherited cone-Hessian slice metric on the dim-4 h_2(C_u) sub-slice has GENUINELY POSITION-DEPENDENT curvature invariants -- Ricci R and Kretschmann K DIFFER across 4 distinct generic rational basepoints (distinct rho_J(X_bg)) EXACT over Q -- so Route 1 verdict = SURVIVES (route ALIVE, Phases 72/73 greenlit); H^3 cone-Hessian Riemann-sign benchmark pinned at constant-negative K=-1/2 and center regression diag(9,9,18,18)/26244 both pass FIRST"
subsystem: [derivation, validation, analysis]
tags: [jordan-algebra, h3o, cone-metric, hessian, totaro-curvature, riemann-tensor, ricci-scalar, kretschmann, homogeneity, symmetric-cone, hyperbolic-space, exact-over-Q, kill-gate]

requires:
  - phase: 70-a0-engine-reconciliation-signature-bridge
    provides: "Plan 70-02: certified SSOT det_3 + cone_hessian_at_center()/_center_subs()/_frame_jacobian_bg_to_mink()/_eta_minkowski(); construction-(ii) bridge g=eta+h; Hess(-log det)|_{I/3}=diag(9,9,18,18)/det 26244; index map {17,18,19,26}=={x1,x2,x3,x10}; H^3=SL(2,C)/SU(2) target curvature stated"
  - phase: 52-kkt-spacetime
    provides: "h_2(C_u)~R^{3,1}, mostly-minus eta from det_2; det=1 hyperboloid = H^3 = SL(2,C)/SU(2); Minkowski frame map (beta,gamma,p,q)->(x0,x1,x2,x3)"
provides:
  - "Hand-rolled Totaro Hessian-curvature engine (R_ijkl=-(1/4)g^{pq}(f_jlp f_ikq - f_ilp f_jkq); Ricci scalar; Kretschmann; sectional curvature) with EXPLICIT stated Riemann/Ricci sign convention, exact over Q, on the SSOT det_3"
  - "H^3 cone-Hessian Riemann-sign benchmark: CONSTANT NEGATIVE sectional curvature K=-1/2 on the actual cone-Hessian slice (sign pinned); round-metric reinforcement K=-1 with the exact factor-of-2 (cone-Hessian metric = 2x round at apex)"
  - "Off-center inherited slice metric g_mu_nu(x)=eta+h_mu_nu(x) on the dim-4 h_2(C_u) sub-slice, expansion in rho_J(X_bg) (NOT spacetime x); center regression to diag(9,9,18,18)/26244"
  - "Route-1 KILL-gate verdict: SURVIVES (curvature scalar invariants R,K position-dependent across 4 distinct generic rational basepoints, exact over Q). The Route-1 verdict + its exact R/K evidence for Plan 71-02's mandatory two-route cross-check."
affects: [71-02, 72, 73]

methods:
  added:
    - "Totaro closed-form Hessian curvature (3rd-derivatives-only; det cubic => uses f_ijk, never 4th derivatives, never sympy.diffgeom on the metric)"
    - "off-center cone-Hessian expansion: _offcenter_subs(delta) (generic basepoint X_bg=I/3+delta in non-slice directions; slice coords symbolic) extending _center_subs()"
    - "rho_J(X_bg)^2 = Tr(X^2)-(Tr X)^2/3 as the F_4-invariant off-center-ness (homogeneity comparison variable)"
    - "rational-basepoint curvature evaluation: 4x4 RATIONAL g.inv() after substituting the rational slice point (never all-symbolic g.inv())"
  patterns:
    - "decisive curvature built ONLY on the SSOT det_3 (never octonion_algebra.py); module-local exact-only source guard extended-in-spirit (0 float-rank/float-curvature on the decisive path, asserted)"
    - "Riemann sign pinned on a CONSTANT-curvature benchmark (H^3) BEFORE any KILL/SURVIVES verdict; honest benchmark value (-1/2 literal pullback) NOT fudged to the round -1"

key-files:
  created: [derivations/71-homogeneity-curvature.tex]
  modified: [code/bulk_geometry_verification.py]

key-decisions:
  - "Route-1 verdict = SURVIVES: the inherited slice-metric curvature scalar invariants R(x),K(x) DIFFER across 4 distinct generic rational basepoints (distinct rho_J), exact over Q -> genuinely position-dependent -> fixing E_11 does NOT leave a homogeneous slice -> route ALIVE. Reported WITHOUT softening (the KILL branch's explicit 'Phase A homogeneous -- route dead. STOP.' string is wired and emitted only on the EQUAL-invariants branch, a no-op here)."
  - "H^3 cone-Hessian benchmark resolved at K=-1/2 (NOT -1): the LITERAL cone-Hessian pullback g_ij=Hess(-log det_2) on the {det_2=1} slice is exactly 2x the round hyperbolic metric at the apex (g_slice|_apex=diag(2,2,2)), so by K(c*g)=(1/c)K(g) its constant sectional curvature is -1/2; the round-metric -1 is the centro-affine/Totaro -d^2/4 normalization. Verified TWO independent ways (the Totaro engine AND a direct parametrized pullback). The decisive content -- the Riemann/Ricci SIGN (negative, constant) -- is pinned; we did NOT insert a factor to force -1 (that would corrupt the sign convention the verdict relies on)."
  - "Expansion/comparison variable is rho_J(X_bg) (off-center-ness of the BASEPOINT in the NON-slice V_0-internal/matter directions), NOT the spacetime coordinate x; the decisive across-basepoint comparison holds the spacetime slice point FIXED so only rho_J varies (defeats fp-coordinate-curvature)."

patterns-established:
  - "Pattern 1: curvature gates ADDED to the 70-certified engine; engine stays ALL_PASS exit 0 (29/29 PASS); every decisive verdict exact over Q; deterministic (run1==run2 byte-identical)."
  - "Pattern 2: a benchmark whose literal value differs from a cited target by a metric-normalization factor is reported HONESTLY with the factor explained, not forced to the cited value; the sign (the load-bearing fact) is what the benchmark pins."

conventions:
  - "natural units; decisive arithmetic EXACT over Q (sympy.Rational/Matrix); 0 numpy float-rank / float-curvature on the decisive path"
  - "potential Phi = -log det_3 (SSOT det_3, cross 2Re((x2 x1) x3)); cone metric g_X = Hess(-log det) positive-definite Riemannian; octonion_algebra.py NEVER imported"
  - "Riemann/Ricci sign: R_ijkl = -(1/4) g^{pq}(f_jlp f_ikq - f_ilp f_jkq); Ric_jl = g^{ik}R_ijkl; R = g^{ik}g^{jl}R_ijkl; sectional K(u,v)=R_ijkl u^i v^j u^k v^l/(g(u,u)g(v,v)-g(u,v)^2). Pinned by the H^3 benchmark (constant NEGATIVE)."
  - "signature mostly-minus (-,+,+,+) on h_2(C_u); construction (ii) bridge g=eta+h, h:=Hess-Hess|center"
  - "expansion variable rho_J(X_bg)=sqrt(Tr(X^2)-(Tr X)^2/3) (basepoint off-center-ness), NOT spacetime x"

plan_contract_ref: ".gpd/phases/71-a-homogeneity-kill-gate/71-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-homogeneity:
      status: passed
      summary: "Route 1 (the primary curvature verdict) is DECISIVE: with E_11=diag(1,0,0) fixed, the inherited slice metric g_mu_nu(x)=eta+h_mu_nu(x) on the dim-4 h_2(C_u) sub-slice has GENUINELY POSITION-DEPENDENT curvature -- the scalar invariants R(x) (Ricci) and K(x) (Kretschmann), computed via the hand-rolled Totaro closed form exact over Q, DIFFER across 4 distinct generic rational basepoints (distinct rho_J(X_bg), common spacetime slice point). Verdict = SURVIVES (route ALIVE). Reported without softening; the KILL branch (equal invariants -> explicit STOP string) is wired and a no-op here."
      linked_ids: [deliv-phaseA, deliv-curvature-note, test-homogeneity, test-h3-benchmark, test-center-regression, ref-totaro, ref-faraut-koranyi, ref-mccrimmon, ref-52-kkt, ref-warm-engine]
      evidence:
        - verifier: gpd-executor
          method: "exact-over-Q curvature-scalar-invariant comparison at 4 distinct generic rational basepoints (python3 code/bulk_geometry_verification.py -> ALL_PASS exit 0, 29/29 PASS, deterministic run1==run2): R differs across all basepoints (e.g. R_BP1=-1047519795/310570129, R_BP4=-71861403663/39975603721; R_BP2-R_BP1=12088482848688180288/15576071694189513529 != 0); all invariants real, none degenerate; within-basepoint x-dependence also confirmed"
          confidence: high
          claim_id: claim-homogeneity
          deliverable_id: deliv-curvature-note
          acceptance_test_id: test-homogeneity
          reference_id: ref-totaro
          evidence_path: "code/bulk_geometry_verification.py (Section 12 + main() Phase-71 gates; commits 9740c692, c78f28a1, 99b64455)"
  deliverables:
    deliv-phaseA:
      status: partial
      path: derivations/71-homogeneity-curvature.tex
      summary: "The SHARED Phase 70+71 derivation: this plan ADVANCES the curvature portion -- h_mu_nu(x) computed explicitly on the dim-4 h_2(C_u) sub-slice off-center (expansion in rho_J(X_bg)) and a DECISIVE homogeneous-vs-position-dependent verdict (SURVIVES) via curvature-scalar invariants R(x),K(x) at 4 distinct generic rational basepoints exact over Q. The KILL-branch 'Phase A homogeneous -- route dead. STOP.' is wired (no-op here). status=partial because the stabilizer-dimension, II, and final two-route reconciliation portions of deliv-phaseA are advanced by Plan 71-02 (by design)."
      linked_ids: [claim-homogeneity, test-homogeneity, test-center-regression]
    deliv-curvature-note:
      status: passed
      path: derivations/71-homogeneity-curvature.tex
      summary: "Route-1 write-up: the Totaro engine + stated Riemann/Ricci sign convention; the H^3=-1/2 cone-Hessian Riemann-sign benchmark (with the factor-of-2 to the round -1 explained); the off-center slice-metric construction (rho_J(X_bg) expansion); the >=2-basepoint invariant comparison and the Route-1 SURVIVES verdict (with the KILL-branch STOP string documented). All must_contain tokens present: 'R_ijkl = -(1/4) g^{pq}(f_jlp f_ikq - f_ilp f_jkq)', 'rho_J(X_bg)' (as \\rho_J(X_{\\mathrm{bg}})), 'Route 1 verdict'. LaTeX balanced (braces 268/268, $ even, begin==end); fragment lint only (no pdflatex in env, mirroring 52-kkt/70-signature-bridge)."
      linked_ids: [claim-homogeneity, test-homogeneity, test-h3-benchmark, ref-totaro, ref-faraut-koranyi, ref-mccrimmon, ref-52-kkt]
  acceptance_tests:
    test-homogeneity:
      status: passed
      summary: "DECISIVE Route-1 verdict, exact over Q: the curvature SCALAR INVARIANTS R(x),K(x) of the off-center cone-Hessian slice metric DIFFER across 4 distinct generic rational basepoints (distinct rho_J(X_bg), common spacetime slice point (2/5,3/5,1/10,1/8)) => SURVIVES. R values: BP1 -1047519795/310570129, BP2 -130237700283/50153154601, BP3 -29748150983655/10135417202689, BP4(octonionic) -71861403663/39975603721; all pairwise dR,dK nonzero exact rationals. Instrumented against all three forbidden proxies: SCALAR invariants (not components); rho_J (slice point fixed); exact over Q (0 float-rank/curvature). All real, none degenerate, >=2 distinct rho_J. Verdict handed to Plan 71-02."
      linked_ids: [claim-homogeneity, deliv-phaseA, deliv-curvature-note, ref-totaro, ref-faraut-koranyi]
    test-h3-benchmark:
      status: passed
      summary: "Riemann-sign benchmark on the ACTUAL cone-Hessian H^3={det_2=1} slice, exact over Q: CONSTANT sectional curvature across 3 independent slice-tangent 2-planes, NEGATIVE (hyperbolic) -- Riemann/Ricci SIGN pinned. Honest cone-Hessian value K=-1/2 (the literal Hess(-log det_2) pullback = 2x the round metric at the apex; the round-metric reinforcement gives K=-1, with the exact factor K_round=2*K_coneHessian confirmed). Riemann algebraic symmetries hold; all K real. NOTE: the plan frontmatter stated the target as -1; the genuine cone-Hessian-slice value is -1/2 (a metric-normalization factor of 2, NOT a sign error or engine bug -- verified two independent ways). The SIGN (the load-bearing fact for the verdict) is correctly pinned; no fudge factor inserted."
      linked_ids: [claim-homogeneity, deliv-curvature-note, ref-totaro, ref-52-kkt]
    test-center-regression:
      status: passed
      summary: "The off-center machinery reduces to the Phase-70 certified center metric, exact over Q: cone_hessian_offcenter(X_bg=I/3) == diag(9,9,18,18), det == 26244; h_mu_nu(center) == 4x4 zero (construction-(ii) centered subtraction); rho_J^2(center)==0. Engine python3 code/bulk_geometry_verification.py -> ALL_PASS, exit 0, 29/29 PASS; module-local exact-only source guard PASS (0 octonion_algebra imports, 0 float-rank/curvature calls on the decisive path)."
      linked_ids: [claim-homogeneity, deliv-phaseA, ref-warm-engine]
  references:
    ref-totaro:
      status: completed
      completed_actions: [read, use, cite]
      missing_actions: []
      summary: "Totaro (arXiv:math/0401381) is the curvature ENGINE: the closed form R_ijkl=-(1/4)g^{pq}(f_jlp f_ikq - f_ilp f_jkq) (3rd-derivatives only) was implemented verbatim (totaro_riemann), used for the H^3 benchmark and the Route-1 verdict, and cited in deriv-curvature-note. The -d^2/4=-1 (d=2) value is the round/centro-affine normalization; the literal cone-Hessian pullback gives -1/2 (factor-of-2, documented)."
    ref-faraut-koranyi:
      status: completed
      completed_actions: [cite, use]
      missing_actions: []
      summary: "Faraut-Koranyi Ch. II-IV: cone metric g_X=Hess(-log det) (used as the Hessian metric whose Totaro curvature is computed) and the inverse-metric strategy g^{pq}=P(X) / matter-rational-then-invert (used: the 4x4 rational g.inv() after substituting the rational slice point, never the all-symbolic blowup). Cited in deriv-curvature-note."
    ref-mccrimmon:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "McCrimmon: the quadratic representation P(X)=2L(X)^2-L(X^2) (the inverse-metric primitive) and the Peirce decomposition under E_11 (used to map the V_1/V_{1/2}/V_0 sectors to engine indices). Cited in deriv-curvature-note. (The decisive inverse was the rational 4x4 g.inv() at the slice point, which is equivalent and avoids the symbolic blowup.)"
    ref-52-kkt:
      status: completed
      completed_actions: [read, use, cite]
      missing_actions: []
      summary: "52-kkt: h_2(C_u)~R^{3,1}, mostly-minus eta from det_2, and the det=1 hyperboloid = H^3 = SL(2,C)/SU(2) (the Riemann-sign benchmark target). The Minkowski frame map (beta,gamma,p,q)->(x0,x1,x2,x3) (already in the engine as _frame_jacobian_bg_to_mink) supplies eta in the slice frame for construction (ii). Cited and used in deriv-curvature-note."
    ref-warm-engine:
      status: completed
      completed_actions: [read, use, cite]
      missing_actions: []
      summary: "code/bulk_geometry_verification.py (Phase-70 CERTIFIED SSOT): EXTENDED, not rebuilt. Reused det_3 (SSOT), cone_hessian_at_center/_center_subs (the off-center expansion swaps _center_subs for _offcenter_subs), _frame_jacobian_bg_to_mink/_eta_minkowski (construction-(ii) eta), Tr/Tr2 (rho_J), jordan_L_matrix (available). NEVER imported octonion_algebra.py; engine stays ALL_PASS exit 0; source guard PASS. The center metric diag(9,9,18,18)/26244 is the regression anchor (test-center-regression)."
  forbidden_proxies:
    fp-relabel-homogeneous:
      status: rejected
      notes: "The verdict is DECISIVE and reported without softening: invariants DIFFER across >=2 basepoints => SURVIVES (route alive). No 'approximately position-dependent' language anywhere. The KILL branch is wired to emit the literal 'Phase A homogeneous -- route dead. STOP.' string ONLY on the equal-invariants branch (a no-op here). Had the result been homogeneous it would have been reported as the clean valuable KILL with that explicit STOP string (NEGATIVE-RESULT-IS-SUCCESS)."
    fp-coordinate-curvature:
      status: rejected
      notes: "The decisive comparison reads ONLY the curvature SCALAR INVARIANTS R (Ricci scalar) and K (Kretschmann) -- full 4-index contractions of R_ijkl, NOT metric components. The comparison variable is rho_J(X_bg) (off-center-ness of the BASEPOINT in the non-slice V_0-internal/matter directions), with the spacetime slice point HELD FIXED at (2/5,3/5,1/10,1/8) across all 4 basepoints, so only rho_J varies. The off-center machinery never puts the off-center-ness into the slice coords {beta,gamma,p,q} (the O(1) spacetime x). (Within-basepoint x-dependence is reported separately as a supporting diagnostic, not as the verdict.)"
    fp-float-decisive:
      status: rejected
      notes: "Every decisive value is EXACT over Q (sympy.Rational/Matrix): the Hessian metric, the 3rd-derivative tensor f_ijk, the 4x4 rational inverse, R_ijkl, the Ricci scalar, the Kretschmann scalar, rho_J^2, and every pairwise difference. The module-local exact-only source guard reports 0 octonion_algebra imports and 0 numpy float-rank / float-curvature calls on the decisive path. Float appears ONLY as explicitly-labeled non-decisive triage (the float ~-3.37 readouts printed beside the exact rationals in dev; the engine prints exact rationals)."
  uncertainty_markers:
    weakest_anchors:
      - "The dim-4 h_2(C_u) sub-slice is assumed sufficient to decide homogeneity of the full dim-10 V_0 (the dim-10 symbolic inverse times out). MITIGATED, NOT eliminated, here: Plan 71-02's stabilizer-transitivity route AND the II computation operate on the FULL (basepoint, slice) V_0 family, so the decisive weight on the full-slice question rests on the two-route cross-check. The dim-4 SURVIVES is a strong positive signal (a homogeneous dim-4 sub-slice could in principle coexist with an inhomogeneous full V_0, but NOT the reverse: a position-dependent dim-4 sub-slice already breaks full-V_0 homogeneity)."
      - "The Riemann/Ricci SIGN convention on the cone-Hessian metric -- pinned by the H^3 benchmark (constant NEGATIVE, exact over Q) computed on the SAME engine BEFORE the verdict. If a sign convention were wrong it would flip R->-R uniformly and could NOT manufacture the across-basepoint DIFFERENCES (the SURVIVES signal is the inequality of invariants, which is sign-convention-independent). Plan 71-02 (purely algebraic, sign-immune) is the cross-check."
    unvalidated_assumptions:
      - "Construction (ii) (eta from det_2 + centered cone-Hessian h) is the LOCKED Phase-70 bridge; whether it preserves the V_1/V_{1/2} matter coupling Phase B needs is a Phase-72 question, not decided here. The Route-1 curvature verdict (SURVIVES) is computed on the cone-Hessian slice metric directly and does not depend on that matter-coupling question."
    competing_explanations:
      - "Two distinct off-center basepoints with the same E_11 could in principle be related by a Stab_{E_6}(E_11) element (which would force equal invariants, => KILL). The observed INEQUALITY of invariants rules this out for these basepoints (they are NOT stabilizer-related), which is exactly the SURVIVES signal. Plan 71-02 confirms by computing dim Stab_{E_6}(E_11) and its orbit on the basepoint family directly (the two routes MUST agree)."
    disconfirming_observations:
      - "Did NOT fire: the H^3 cone-Hessian benchmark coming out non-constant or non-negative (it is constant -1/2, negative) -> Riemann sign / slice metric would be wrong."
      - "Did NOT fire: a curvature invariant with a nonzero imaginary part (all R,K real) -> octonion cross-term association error."
      - "Did NOT fire: the off-center code NOT reducing to diag(9,9,18,18)/26244 at the center (it does) -> wrong off-center substitution."
      - "Did NOT fire: a 'position-dependent' result appearing only when expanding in spacetime x (the decisive comparison varies rho_J with x FIXED) -> fp-coordinate-curvature."
      - "Did NOT fire: det(metric)=0 at a basepoint (all detg != 0) -> light-cone degeneracy."

comparison_verdicts:
  - subject_id: test-homogeneity
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-totaro
    comparison_kind: cross_method
    metric: exact_inequality_over_Q
    threshold: "R^(i) != R^(j) and/or K^(i) != K^(j) for some pair of >=2 distinct generic rational basepoints (exact over Q) => SURVIVES; ALL equal => KILL"
    verdict: pass
    recommended_action: "Proceed to Plan 71-02: hand the SURVIVES verdict + the exact R/K evidence to the mandatory stabilizer-transitivity + II two-route cross-check (the two routes MUST agree; Route 1 SURVIVES predicts a NON-transitive Stab_{E_6}(E_11) and II != 0)."
    notes: "4 distinct basepoints (incl. a genuinely octonionic one) give 4 distinct exact-over-Q Ricci scalars; all pairwise differences nonzero rationals. SURVIVES = route alive (NOT the KILL; reported without softening either way)."
  - subject_id: test-h3-benchmark
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-totaro
    comparison_kind: benchmark
    metric: exact_equality_over_Q
    threshold: "cone-Hessian H^3 slice sectional curvature CONSTANT and NEGATIVE over Q (sign pinned); honest value -1/2 = K_round/2 (round-metric -1 = Totaro -d^2/4, d=2)"
    verdict: pass
    recommended_action: "Carry the pinned Riemann/Ricci sign convention (constant-negative on H^3) into Plan 71-02's curvature cross-references; note the cone-Hessian value is -1/2 (factor-of-2 vs the round -1), not a sign error."
    notes: "Plan frontmatter stated target -1; the genuine cone-Hessian-slice value is -1/2 (metric-normalization factor of 2: g_slice|_apex=diag(2,2,2)=2*g_round). Verified two independent ways (Totaro engine + parametrized pullback). DEVIATION recorded (Rule 5, benign mechanism). The SIGN -- the load-bearing fact for the verdict -- is correctly pinned; NOT fudged to -1."
  - subject_id: test-center-regression
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-warm-engine
    comparison_kind: benchmark
    metric: exact_equality_over_Q
    threshold: "cone_hessian_offcenter(I/3) == diag(9,9,18,18), det == 26244; h(center)==0; rho_J^2(center)==0 (exact)"
    verdict: pass
    recommended_action: "No action; the off-center machinery correctly reduces to the Phase-70 certified center metric (the ref-warm-engine benchmark anchor) -> the off-center substitution + construction-(ii) subtraction are correct, so the off-center curvature in test-homogeneity is trustworthy."
    notes: "Decisive regression/benchmark anchor to the Phase-70 certified warm engine (ref-warm-engine): one of the THREE hard gates that must pass BEFORE the Route-1 verdict is trusted (a wrong off-center substitution would invalidate test-homogeneity). Engine ALL_PASS exit 0, 29/29 PASS, deterministic; exact-only source guard PASS (0 octonion_algebra imports, 0 float-rank/curvature)."
  - subject_id: ref-warm-engine
    subject_kind: reference
    subject_role: decisive
    reference_id: ref-warm-engine
    comparison_kind: benchmark
    metric: exact_equality_over_Q
    threshold: "the EXTENDED engine reproduces the Phase-70 certified warm-engine anchors exactly over Q: center metric diag(9,9,18,18)/det 26244 (center regression) AND the full 70-01/70-02 LOCKs (LOCK 0 byte-identity, 7a/7b F_4 certificate, signature-bridge gates)"
    verdict: pass
    recommended_action: "Reuse the EXTENDED certified engine in Plan 71-02 (the Totaro engine, off-center machinery, and rho_J variable are available); no rebuild, no octonion_algebra import."
    notes: "ref-warm-engine (must_surface benchmark) is surfaced decisively: the Phase-71 additions were ADDED on top of the 70-certified engine and the engine still prints ALL_PASS exit 0 (29/29 PASS, deterministic), with LOCK 0 (det_3 byte-identical to ring_lemma_verification), LOCK 7a/7b (F_4 SSOT certificate), and the exact-only source guard (0 octonion_algebra imports, 0 float-rank/curvature on the decisive path) all still passing. The center metric diag(9,9,18,18)/26244 is reproduced exactly (test-center-regression)."

duration: 22min
completed: 2026-05-30
---

# Phase 71 (A) Plan 01: Route-1 Homogeneity KILL Gate Summary

**Route-1 verdict = SURVIVES. With the primitive idempotent E_11 = diag(1,0,0) fixed, the inherited cone-Hessian slice metric g_mu_nu(x) = eta + h_mu_nu(x) on the dim-4 h_2(C_u) sub-slice has GENUINELY POSITION-DEPENDENT curvature: the Ricci scalar R(x) and Kretschmann scalar K(x), computed via a hand-rolled Totaro closed-form engine EXACT over Q, DIFFER across 4 distinct generic rational basepoints (distinct rho_J(X_bg), common spacetime slice point). The two HARD GATES passed FIRST: the H^3 cone-Hessian Riemann-sign benchmark (constant NEGATIVE sectional curvature, exact over Q) pinned the sign convention, and the center regression reproduced the Phase-70 certified diag(9,9,18,18)/det 26244. The route is ALIVE; Phases 72/73 (matter-sourcing, Einstein structure) are greenlit. The verdict is reported without softening; the KILL branch's explicit 'Phase A homogeneous -- route dead. STOP.' string is wired and a no-op here.**

## Performance

- **Duration:** ~22 min (symbolic compute is fast: each curvature invariant at a rational basepoint ~0.5 s; full engine run ~5-8 s; no watchdog risk -- every decisive step ran foreground `python3 -u` well inside ~150 s)
- **Started:** 2026-05-30 (session start)
- **Completed:** 2026-05-30
- **Tasks:** 3 (all build the two deliverables; curvature engine + off-center metric + verdict added to the 70-certified engine)
- **Files modified:** 1 created (`derivations/71-homogeneity-curvature.tex`), 1 extended (`code/bulk_geometry_verification.py`)

## Key Results

- **ROUTE-1 VERDICT = SURVIVES** (the decisive milestone gate). The curvature SCALAR INVARIANTS of the inherited slice metric DIFFER across 4 distinct generic rational basepoints (distinct rho_J(X_bg), common spacetime slice point (2/5, 3/5, 1/10, 1/8)), EXACT over Q:

  | Basepoint | rho_J^2 | R (Ricci scalar) |
  | --- | --- | --- |
  | BP1 (V0-internal {4,5} + V_{1/2} {11}) | 69943/264600 | -1047519795/310570129 |
  | BP2 (V0-internal {4,6} + V_{1/2} {19}) | 239/360 | -130237700283/50153154601 |
  | BP3 (V0-internal {7,8,9} + V_{1/2} {13}) | 168799/352800 | -29748150983655/10135417202689 |
  | BP4 (octonionic {4,5,6} + V_{1/2} {12,20}) | 87881/88200 | -71861403663/39975603721 |

  All pairwise differences are nonzero exact rationals (e.g. R_BP2 - R_BP1 = 12088482848688180288/15576071694189513529 != 0); the Kretschmann K likewise differs across all basepoints. All invariants REAL, none degenerate (det g != 0).
- **H^3 Riemann-sign benchmark (HARD GATE, did FIRST):** the ACTUAL cone-Hessian metric on the {det_2=1} H^3 slice has CONSTANT sectional curvature K = -1/2 across 3 independent slice-tangent 2-planes, NEGATIVE (hyperbolic) -- the Riemann/Ricci SIGN convention is pinned. The round-metric reinforcement gives K = -1 with the exact factor-of-2 (K_round = 2*K_coneHessian; the cone-Hessian pullback is 2x the round metric at the apex). Riemann algebraic symmetries hold; all K real.
- **Center regression (HARD GATE):** cone_hessian_offcenter(X_bg = I/3) == diag(9,9,18,18), det == 26244 (the Phase-70 certified value); h_mu_nu(center) == 0; rho_J^2(center) == 0.
- **Engine status:** `python3 code/bulk_geometry_verification.py` -> ALL_PASS, exit 0, **29/29 PASS**, 0 FAIL, deterministic (run1 == run2 byte-identical). Source guard PASS (0 octonion_algebra imports, 0 numpy float-rank / float-curvature calls on the decisive path); LOCK 0 / 7a / 7b (the F_4 SSOT certificate) still pass.

## Task Commits

Each task was committed atomically:

1. **Task 1: Totaro curvature engine + H^3 Riemann-sign benchmark** - `9740c692` (compute) - `code/bulk_geometry_verification.py` (Section 12: hessian_metric, cubic_form_C, totaro_riemann, ricci_scalar, kretschmann, sectional_curvature, h3_cone_hessian_benchmark) + `derivations/71-homogeneity-curvature.tex` (created: engine + benchmark sections)
2. **Task 2: off-center slice metric + center regression** - `c78f28a1` (compute) - engine `_offcenter_subs`, `cone_hessian_offcenter`, `offcenter_slice_metric`, `rho_J_squared` + the center-regression gate
3. **Task 3: Route-1 KILL verdict (SURVIVES)** - `99b64455` (compute) - engine `route1_curvature_verdict`, `_curvature_invariants_at`, the verdict gate + `.tex` off-center construction + Route-1 verdict sections

**Plan metadata:** this SUMMARY (committed separately).

## Files Created/Modified

- `derivations/71-homogeneity-curvature.tex` (created) - Route-1 write-up: the Totaro engine + stated Riemann/Ricci sign convention (Sec. 1); the H^3 = -1/2 cone-Hessian Riemann-sign benchmark with the factor-of-2 to the round -1 (Sec. 2); the off-center slice-metric construction with the rho_J(X_bg) expansion (Sec. 3); the >=2-basepoint comparison and the Route-1 SURVIVES verdict with the KILL-branch STOP string documented (Sec. 4). Fragment (no \documentclass), like 52-kkt-spacetime.tex; LaTeX balance verified (braces 268/268, $ even, begin==end).
- `code/bulk_geometry_verification.py` (extended) - Section 12 (Phase-71 Totaro curvature engine + H^3 benchmark + Route-1 verdict) ADDED on top of the 70-certified engine; the off-center machinery (_offcenter_subs, cone_hessian_offcenter, offcenter_slice_metric, rho_J_squared) ADDED in the Section-10 geometry region; the Phase-71 gate block ADDED to main(). The 70-certified Sections 1-11 region is otherwise UNCHANGED (LOCK 0 byte-identity, 7a/7b, the source guard all still pass).

## Equations Derived

**Eq. (71.1)** -- Totaro Hessian-curvature closed form (the engine; LOCKED token):

$$
R_{ijkl} = -\tfrac14\, g^{pq}\big(f_{jlp}\,f_{ikq} - f_{ilp}\,f_{jkq}\big),
\qquad f_{ijk} := \partial_i\partial_j\partial_k(-\log\det_3),
$$

with Ricci scalar $R = g^{ik}g^{jl}R_{ijkl}$, Kretschmann $K = R_{ijkl}R^{ijkl}$, and sectional curvature $\mathcal{K}(u,v) = R_{ijkl}u^i v^j u^k v^l / (g(u,u)g(v,v)-g(u,v)^2)$.

**Eq. (71.2)** -- the H^3 cone-Hessian Riemann-sign benchmark (sign pinned; honest value):

$$
\mathcal{K}_{H^3}^{\text{cone-Hessian}} = -\tfrac12 \ \text{(constant, negative, exact over } \mathbb{Q}),
\qquad
\mathcal{K}_{H^3}^{\text{round}} = -1 = 2\,\mathcal{K}_{H^3}^{\text{cone-Hessian}}.
$$

**Eq. (71.3)** -- the off-center inherited slice metric (construction (ii); expansion in rho_J):

$$
g_{\mu\nu}(x) = \eta_{\mu\nu} + h_{\mu\nu}(x), \quad
h_{\mu\nu} := \big[\operatorname{Hess}(-\log\det)|_{V_0}\big]_{X_{\mathrm{bg}}} - \big[\cdots\big]_{(M=0,\,I/3)},
\quad
\rho_J(X_{\mathrm{bg}})^2 = \operatorname{Tr}(X_{\mathrm{bg}}^2) - \tfrac13(\operatorname{Tr} X_{\mathrm{bg}})^2.
$$

**Eq. (71.4)** -- the Route-1 verdict (decisive, exact over Q):

$$
R^{(i)} \neq R^{(j)} \ \text{across 4 distinct generic rational basepoints} \implies \textbf{Route 1 verdict: SURVIVES.}
$$

## Validations Completed

- **H^3 Riemann-sign benchmark (test-h3-benchmark):** cone-Hessian slice sectional curvature CONSTANT (-1/2) across 3 slice-tangent 2-planes, NEGATIVE; Riemann algebraic symmetries hold; all K real. Cross-checked against the round-metric -1 with the exact factor-of-2, AND against an independent parametrized-pullback ground-truth (-1/2) in dev. PASS.
- **Center regression (test-center-regression):** cone_hessian_offcenter(I/3) == diag(9,9,18,18), det 26244; h(center)==0; rho_J^2(center)==0. Exact over Q. PASS.
- **Route-1 verdict (test-homogeneity):** R, K differ across 4 distinct generic rational basepoints, exact over Q; all real; none degenerate; >=2 distinct rho_J; within-basepoint x-dependence also confirmed. Instrumented against all 3 forbidden proxies. PASS (SURVIVES).
- **Octonion-association guard:** BP4 specifically exercises the genuinely-octonionic C_u-orthogonal directions {4,5,6} (where non-associativity bites) and V_{1/2} {12,20}; its R is real and rational -> no cross-term association error. Built on the SSOT det_3.
- **Engine regression:** all 70-01/70-02 LOCKs (0, 1-5, LAYOUT, 7a/7b, exact-only guard, the signature-bridge gates) still PASS; OVERALL ALL_PASS, exit 0, deterministic.
- **Reproducibility:** SymPy 1.14.0, Python 3.14.2, NumPy 2.4.2, macOS Darwin 24.6.0; all test points hardcoded exact rationals, no random seeds; run1 == run2 byte-identical; verdict independently re-derived via the engine API in a fresh process.

## Approximations Used

| Approximation | Valid When | Error Estimate | Breaks Down At |
| --- | --- | --- | --- |
| Restrict the decisive curvature to the dim-4 h_2(C_u) sub-slice | always (the dim-4 slice is the decisive arena by design; dim-10 V_0 symbolic inverse times out >200s and is off the critical path) | 0 (exact over Q on the dim-4 slice) | a pathological case where the dim-4 sub-slice is homogeneous while the full dim-10 V_0 is not -- MITIGATED by Plan 71-02's full-V_0 routes. (Here the dim-4 slice is INHOMOGENEOUS, which already breaks full-V_0 homogeneity, so this mitigation is not even load-bearing for the SURVIVES branch.) |
| Evaluate curvature invariants at distinct generic RATIONAL basepoints (not fully symbolic x) | always exact over Q; the recommended default (avoids symbolic blow-up / the ~150s watchdog) | 0 (exact rational points) | a single basepoint cannot detect rho_J-dependence -- DEFEATED by using 4 distinct generic basepoints with distinct rho_J |

`M=0`/`I/3` and the off-center basepoints are EXACT evaluation points (no perturbative truncation); the off-center expansion in rho_J is via genuine distinct basepoints, not a truncated series.

## Decisions Made

- **Route-1 verdict = SURVIVES, reported without softening.** The curvature scalar invariants differ across 4 distinct generic rational basepoints exact over Q. The KILL branch (equal invariants -> 'Phase A homogeneous -- route dead. STOP.') is fully wired and a no-op here.
- **H^3 cone-Hessian benchmark honest value -1/2 (NOT fudged to -1).** See Deviations. The decisive content -- the negative, constant SIGN -- is pinned.
- **Expansion/comparison variable rho_J(X_bg), slice point held fixed.** Defeats fp-coordinate-curvature.
- **Rational-basepoint evaluation (4x4 rational g.inv() after substituting the slice point).** Avoids the all-symbolic g.inv() >200s blowup; stays well inside the watchdog (~0.5 s/basepoint).
- **EXTEND the certified engine, never import octonion_algebra.py.** Source guard PASS.

## Deviations from Plan

### Auto-fixed / documented

**1. [Rule 5 - Physics benchmark value, benign mechanism] H^3 cone-Hessian benchmark is -1/2, not the plan-stated -1**

- **Found during:** Task 1 (Riemann-sign benchmark, the HARD GATE).
- **Issue:** The plan frontmatter and critical_execution_notes state the H^3 cone-Hessian benchmark target as constant sectional curvature K = -1 ("Totaro -d^2/4, d=2"). The ACTUAL literal cone-Hessian pullback g_ij = Hess(-log det_2) on the {det_2=1} slice gives K = -1/2, NOT -1.
- **Root cause (verified, benign):** the -1 is the curvature of the ROUND hyperbolic metric (the centro-affine / Totaro -d^2/4 normalization, = the Phase-70 reinforcement). The literal cone-Hessian pullback is exactly 2x the round metric at the apex (g_slice|_apex = diag(2,2,2)), so by the scaling law K(c*g) = (1/c)K(g) the cone-Hessian value is -1/2. This is a METRIC-NORMALIZATION factor of 2, NOT a sign error and NOT an engine bug.
- **Verification:** computed TWO independent ways -- (a) the hand-rolled Totaro engine on the cone-Hessian slice (-1/2), and (b) a direct parametrized pullback of the cone-Hessian metric to the {det_2=1} hyperboloid with an intrinsic 3-dim Riemann computation (-1/2), in a dev scratch. Both agree exactly over Q. The round-metric -1 and the exact factor K_round = 2*K_coneHessian are also asserted in the engine.
- **Why not a STOP:** the benchmark's load-bearing PURPOSE (per the plan's own contract) is to PIN THE RIEMANN/RICCI SIGN convention before the verdict. The sign is unambiguously NEGATIVE and the curvature is unambiguously CONSTANT (both exact over Q, two independent methods) -- the sign is correctly pinned. Forcing -1 by inserting a factor would CORRUPT the very sign convention the verdict relies on (fp-float-decisive-adjacent dishonesty). The SURVIVES signal (inequality of invariants across basepoints) is sign-convention-INDEPENDENT, so the factor-of-2 does not affect the verdict at all.
- **Files modified:** code/bulk_geometry_verification.py (Section 12 header + benchmark gate document the factor-of-2), derivations/71-homogeneity-curvature.tex (Sec. 2 explains it).
- **Committed in:** 9740c692 (Task 1 commit).
- **Surfaced for the orchestrator:** YES (this SUMMARY's Key Results, Deviations, and the test-h3-benchmark comparison verdict; the engine output prints it).

---

**Total deviations:** 1 documented (1 benchmark-value/Rule-5, benign verified mechanism).
**Impact on plan:** None on the verdict. The benchmark's purpose (pin the sign) is fully met; the magnitude discrepancy is a metric normalization, verified two independent ways, and the SURVIVES verdict is sign-convention-independent. No scope change.

## Issues Encountered

- **No physics issues.** One tooling note: `pdflatex` is not available in the executor environment, so the `.tex` fragment was validated by structural lint (braces 268/268 balanced, inline `$` even, environments begin==end) rather than compilation -- consistent with how the sibling fragments `derivations/52-kkt-spacetime.tex` and `derivations/70-signature-bridge.tex` are handled (they are `\input`-included by the project master, which compiles elsewhere).

## Open Questions

- Does Plan 71-02's stabilizer-transitivity route (dim Stab_{E_6}(E_11) and its orbit on the basepoint family) AGREE with this Route-1 SURVIVES? (It MUST; a SURVIVES predicts a NON-transitive Stab_{E_6}(E_11).) -- **the mandatory two-route cross-check.**
- Does the second fundamental form II of the V_0 slice come out NON-zero (II != 0), consistent with SURVIVES via the Gauss equation? (Plan 71-02's cheap shortcut.)
- Is the dim-10 V_0 slice (not just the dim-4 h_2(C_u) sub-slice) also inhomogeneous? (Plan 71-02's routes operate on the full V_0 family; here the dim-4 sub-slice inhomogeneity already breaks full-V_0 homogeneity.)
- Is the slice curvature SOURCED by V_1/V_{1/2} matter via the cross-terms, or already present as a pure cosmological constant? (Phase 72.)

## Next Phase Readiness

**Plan 71-02 is ready (and its premise is now set).** The Route-1 verdict (SURVIVES) and its exact-over-Q evidence (the 4-basepoint R/K table, the nonzero pairwise differences) are recorded in the engine main() output and in derivations/71-homogeneity-curvature.tex (Sec. 4), ready to be CONSUMED by Plan 71-02 for the mandatory stabilizer-transitivity + totally-geodesic-II two-route cross-check. The two routes MUST agree: Route 1 SURVIVES predicts (i) a NON-transitive Stab_{E_6}(E_11) (orbit dim < basepoint-family dim) and (ii) a non-vanishing second fundamental form II != 0. The Totaro curvature engine, the off-center machinery, and the rho_J(X_bg) variable are all available in the certified engine for reuse. The Riemann/Ricci sign is pinned (constant-negative on H^3). If Plan 71-02 DISAGREES (finds a transitive stabilizer), neither verdict is trustworthy and the discrepancy must be localized before the milestone proceeds.

## Contract Coverage

- **Claim IDs advanced:** `claim-homogeneity` -> passed (Route-1 SURVIVES, decisive, exact over Q)
- **Deliverable IDs produced:** `deliv-phaseA` -> partial (curvature portion advanced; stabilizer/II/reconciliation portions are Plan 71-02 by design); `deliv-curvature-note` -> derivations/71-homogeneity-curvature.tex (passed, all must_contain tokens present)
- **Acceptance test IDs run:** `test-homogeneity` -> passed (SURVIVES); `test-h3-benchmark` -> passed (sign pinned; honest -1/2 with factor-of-2 to round -1); `test-center-regression` -> passed (diag(9,9,18,18)/26244)
- **Reference IDs surfaced:** `ref-totaro` (read/use/cite); `ref-faraut-koranyi` (cite/use); `ref-mccrimmon` (cite); `ref-52-kkt` (read/use/cite); `ref-warm-engine` (read/use/cite)
- **Forbidden proxies rejected:** `fp-relabel-homogeneous`, `fp-coordinate-curvature`, `fp-float-decisive` -> all rejected
- **Decisive comparison verdicts:** `test-homogeneity` -> pass (decisive; SURVIVES); `test-h3-benchmark` -> pass (decisive; sign pinned, -1/2 honest value); `test-center-regression` -> pass (decisive; regression/benchmark anchor to the Phase-70 warm engine, surfaces ref-warm-engine)

---

## Self-Check: PASSED

- All files exist on disk: `derivations/71-homogeneity-curvature.tex`, `code/bulk_geometry_verification.py`, `.gpd/phases/71-a-homogeneity-kill-gate/71-01-SUMMARY.md`. OK
- All 3 task commits present in `git log`: `9740c692`, `c78f28a1`, `99b64455`. OK
- Key result reproduces: `python3 code/bulk_geometry_verification.py` -> `OVERALL: ALL_PASS`, exit 0, **29/29 PASS, 0 FAIL**, deterministic (run1 == run2 byte-identical). OK
- Verdict independently re-derived via the engine API in a fresh process: SURVIVES, R_BP1=-1047519795/310570129, R_BP4=-71861403663/39975603721, H^3 K=[-1/2,-1/2,-1/2], source guard PASS. OK
- Decisive numbers present in engine output: the 4-basepoint R/K table, the nonzero pairwise differences, 'Route 1 verdict: SURVIVES'. OK
- Convention consistency: one signature (mostly-minus), one potential (-log det), one Riemann sign convention (stated + benchmarked); decisive geometry built on the SSOT det_3 (no octonion_algebra import; guard PASS, 0 float-rank/curvature). OK
- Contract coverage: every claim / deliverable / acceptance-test / reference / forbidden-proxy ID from the PLAN contract appears in contract_results; the 3 decisive/supporting comparison verdicts are recorded. OK

## Validation: PASSED

- Algebraic grading (the "dimensional" check for this pure-geometry phase): det_3 homogeneous degree 3; -log det jet handled (Totaro needs only the 3rd-derivative tensor f_ijk; no 4th derivatives); curvature invariants are pure numbers over Q. OK
- H^3 benchmark exact over Q: cone-Hessian slice K = -1/2 constant negative (sign pinned); round-metric reinforcement K=-1; factor K_round=2*K_coneHessian. OK
- Center regression exact over Q: cone_hessian_offcenter(I/3) == diag(9,9,18,18), det 26244; h(center)==0; rho_J^2(center)==0. OK
- Route-1 verdict exact over Q: R, K differ across 4 distinct generic rational basepoints (all pairwise differences nonzero rationals); all real; none degenerate; SURVIVES. OK
- Forbidden proxies: fp-relabel-homogeneous (decisive verdict, KILL-branch STOP string wired), fp-coordinate-curvature (scalar invariants, rho_J variable, x fixed), fp-float-decisive (exact over Q, 0 float-rank/curvature) -- all rejected. OK

---

_Phase: 71-a-homogeneity-kill-gate_
_Completed: 2026-05-30_
