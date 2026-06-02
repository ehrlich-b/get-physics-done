---
phase: 76-phase-a-5-berry-curvature-same-wall-gate-soft-kill
plan: 02
depth: complex
one-liner: "VALD-04 DECIDED exactly over Q(i) -- the matter-on Berry curvature F_B is EM-SHAPED (antisymmetric 2-form; F_B^F_B = Pontryagin ~F^2 density; Maxwell stress EXACTLY traceless in 4d, frame-rotation invariant), STRUCTURALLY DISJOINT from the non-traceless independently-frozen T[M] (trace 680, cross-term-sourced); the Lie sector INHERITS the v17.0 symmetric-sector same-wall mismatch => PROPOSED VERDICT SOFT KILL (awaiting Bryan's blocking ratification)"
subsystem: [derivation, validation, analysis, formalism]
tags: [berry-curvature, quantum-geometric-tensor, macdowell-mansouri, maxwell-stress, conformal-tracelessness, soft-kill, octonions, h3O, stress-energy, exact-over-Q, same-wall-gate]

requires:
  - phase: 76-phase-a-5-berry-curvature-same-wall-gate-soft-kill (plan 01)
    provides: "the calibrated QGT recipe (F_B=-2 Im Q, sign/factor pinned by CP^1); the vacuum baseline F_B^vac=-2 omega_K (subtracted to isolate matter F_B); VALD-03 F_B well-defined+nonzero"
  - phase: 75-phase-a-coframe-reduction-dealbreaker-the-kill-gate
    provides: "the FORCED SO(3,1) Lorentz block on the C_u^2 survivors {11,18,19,26}, G=diag(+1,-1,-1,-1); the soldered (1,3) metric is the verdict target (NOT the Euclidean OP^2 foil)"
  - phase: 73-c-einstein-structure (v17.0)
    provides: "the independently-frozen T[M] pipeline (psi=2Re((x2 x1)x3), T[psi]=d psi d psi - 1/2 eta (d psi)^2, kappa first, AST-guarded); the off-switch (inv_det_X_block); ricci_decomposition_n4; the v17.0 NONE same-wall failure pattern (binds Re ONLY)"
provides:
  - "VALD-04 PROPOSED VERDICT = SOFT KILL (awaiting human ratification): the matter Berry curvature F_B is EM-shaped, not Einstein-shaped, exact over Q(i)"
  - "the matter-on idempotent E(x;M) over C_u: rank-1 to all orders in M, C_u-faithful (survivor V_{1/2} matter {11,18,19,26} stays in C_u; transverse e_1..e_6 projected away by pi_u, NOT a rank-changing leak); M->0 recovers the PART-1 vacuum F_B"
  - "matter F_B leading M-power = O(||M||^2) (the v17.0 order of the metric h), confirmed by the exact ratio test ->4=2^2 at two matter directions"
  - "the F_B^F_B Lorentz-block epsilon-contraction (MM-style Pontryagin scalar): matter 46944/571787, full 16384000/571787, vacuum 32 -- gauge-invariant, SO(3,1) frame-rotation invariant"
  - "THE EM SIGNATURE: the Maxwell stress of F_B is EXACTLY traceless in n=4 (trace_G==0 over Q) -- the conformal invariance of any antisymmetric 2-form in 4d (n=3 control != 0); F_B is a field strength, not an Einstein stress"
  - "the independently-frozen T[M] is NON-traceless (trace_eta=680), cross-term-sourced (off-switch R[g] ON=5.13 vs OFF=1144.87), S!=0/Weyl!=0 -- the Einstein-source signature, structurally distinct from F_B"
affects: [77-phase-b (CONJUNCTIVE greenlight blocked by this SOFT KILL), milestone-v18.0 (closes as a publishable negative if ratified)]

methods:
  added:
    - "build_matter_idempotent / task1_matter_idempotent: the matter-on E(x;M) over C_u (Veronese chart with the V_{1/2} matter shifting the centre); rank-1 + C_u-faithful + M->0 + leading-M-power"
    - "berry_F_at_point: watchdog-safe F_B at a rational base point (differentiate P symbolically, EVALUATE derivatives at the point => rational-matrix trace algebra; 5.7s/sample, avoids the >200s all-symbolic cliff)"
    - "FwedgeF_pontryagin: the MM-style F_B^F_B Lorentz-block epsilon-contraction (the gauge-invariant Pontryagin/~F^2 scalar)"
    - "maxwell_stress_of_FB: T[F_B]=F.F-1/4 G F^2 wrt the forced SO(3,1) G; the n=4 traceless EM discriminant"
    - "freeze_T_of_M / _cross_term_psi_field: the independently-frozen T[psi] from the det_3 SSOT cross-term, kappa first, NO reference to F_B"
    - "_rational_so31_rotation: a rational SO(3,1) element (boost cosh=5/4 x rotation cos=3/5) for the frame-rotation gauge test, L^T G L==G exact over Q"
  patterns:
    - "the EM-vs-Einstein discriminant = the Maxwell-stress TRACE: traceless ~F^2 (conformal, 4d) => EM-shaped; non-traceless => Einstein-source. Decided on gauge-invariant scalars, frame-rotation invariant"
    - "C_u-faithfulness via the survivor/transverse split: V_{1/2} matter that survives pi_u sources the Berry response; transverse e_1..e_6 matter is projected away (invisible), NOT a rank-changing leak"

key-files:
  created:
    - ".gpd/phases/76-phase-a-5-berry-curvature-same-wall-gate-soft-kill/76-02-SUMMARY.md (this file)"
  modified:
    - "code/cartan_phaseA5_berry.py (PART 2 appended: matter-on E(x;M); berry_F_at_point; FwedgeF_pontryagin; maxwell_stress_of_FB; the SO(3,1) frame rotation; freeze_T_of_M; task1_matter_idempotent + task2_vald04; 43/43 PASS exit 0)"
    - "derivations/76-berry-same-wall.tex (PART 2 appended: the matter-on construction, the matter F_B M-series, the F_B^F_B Lorentz-block contraction, the independently-frozen T[M], the VALD-04 verdict, the EXPLICIT SOFT KILL line, all 6 forbidden proxies rejected)"

key-decisions:
  - "The EM-vs-Einstein verdict is decided on the Maxwell-stress TRACE (gauge-invariant, frame-rotation invariant): F_B's stress is EXACTLY traceless in n=4 (conformal) => EM-shaped. This is the decisive tensor-structure discriminant, not 'a 2-form appears' (fp-relabel)."
  - "T[M] is built from the det_3 SSOT cross-term psi=2Re((x2 x1)x3) via T[psi]=d psi d psi - 1/2 eta (d psi)^2, kappa frozen first, WITHOUT any reference to F_B (Phase-73 DERV-03 discipline) -- non-circular."
  - "The matter-on E(x;M) over C_u uses the Veronese chart with the C_u-survivor V_{1/2} matter shifting the centre; the transverse e_1..e_6 matter is projected away by pi_u (the C_u-faithfulness resolution, Q6), NOT a rank-changing leak."
  - "Watchdog mitigation: the all-symbolic-in-t berry_F is the >200s cliff; berry_F_at_point (evaluate derivatives at the rational base point) gives 5.7s/sample exact over Q(i). Tasks committed immediately."

patterns-established:
  - "negative-result-is-success at true strength: an EM-shaped F_B is reported FLAT as a SOFT KILL (the Lie sector inherits the symmetric-sector mismatch), NEVER 'approximately Einstein'"
  - "the conformal tracelessness of a 4d field strength as the EM discriminant (independently cross-checked: n=3 control gives trace != 0, so the n=4 zero is genuine conformal symmetry, not a bug)"

conventions:
  - "natural units (hbar=c=k_B=1, dimensionless)"
  - "metric_signature = mostly-minus (+,-,-,-); the FORCED SO(3,1) Lorentz block G=diag(+1,-1,-1,-1) on the C_u^2 survivors {11,18,19,26} (Phase 75)"
  - "complex_structure u = e_7; slice_to_complex maps e_7 -> i (sympy.I) SYMBOLICALLY over Q(i)"
  - "QGT: Q=Tr(P dP dP); g=Re Q (Fubini-Study); F_B=-2 Im Q (Berry). Sign/factor pinned by CP^1 (PART 1)"
  - "T[M] = T[psi], psi=2Re((x2 x1)x3) the det_3 SSOT cross-term (oct_mul SSOT order, NOT Jordan, octonion_algebra.py banned); kappa frozen first; off-switch = inv_det_X_block"
  - "Lambda=0; M=0 vacuum recovered as the pure-Lambda/Kahler F_B^vac=-2 omega_K (no Lambda<0/RxH^3); matter F_B vanishes as M->0"
  - "EXACT over Q(i): the i is sympy.I (symbolic); diff/re/im/ranks/eigenvals via SymPy; NO numpy/float on any decisive path"

plan_contract_ref: ".gpd/phases/76-phase-a-5-berry-curvature-same-wall-gate-soft-kill/76-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-berry-same-wall:
      status: passed
      summary: "VALD-04 DECIDED exactly over Q(i) on gauge-invariant scalars (PROPOSED verdict, awaiting Bryan's blocking ratification at Task 3). The matter-on idempotent E(x;M) over C_u is built + verified a clean rank-1 C_u projector (E^2-E==0, Tr==1, C_u-faithful: survivor V_{1/2} matter stays in C_u, transverse e_1..e_6 projected away by pi_u -- NOT a rank-changing leak), with the M->0 limit recovering the PART-1 vacuum F_B^vac=-2 omega_K exactly and leading matter F_B = O(||M||^2). The matter F_B is EM-SHAPED: an antisymmetric 2-form whose F_B^F_B Lorentz-block epsilon-contraction is the Pontryagin/~F^2 density (matter 46944/571787, gauge-invariant, SO(3,1) frame-rotation invariant) and whose Maxwell stress is EXACTLY TRACELESS in n=4 (trace_G==0, the conformal invariance of a 4d 2-form; n=3 control !=0). The INDEPENDENTLY-FROZEN T[M]=T[psi] (psi=2Re((x2 x1)x3), kappa first, NO reference to F_B) is NON-traceless (trace_eta=680), cross-term-sourced (off-switch R[g] ON=5.13 vs OFF=1144.87), S!=0/Weyl!=0. THE THREE MATCHES: M-power coincides (both O(||M||^2)) BUT tensor structure is a DECISIVE MISMATCH (traceless EM-shaped F_B vs non-traceless Einstein-source T[M]) and support is disjoint => EM-SHAPED => SOFT KILL: the Lie/antisymmetric sector inherits the v17.0 symmetric-sector same-wall mismatch. Reported FLAT (negative-result-is-success). CONJUNCTIVE with Phase 75 (SURVIVES): a SOFT KILL ends milestone v18.0 as a publishable negative; recommend STOP before Phase B (77)."
      linked_ids: [deliv-phaseA5, deliv-phaseA5-code, obs-berry-curvature, test-berry-matter-family, test-berry-shape, ref-provost-vallee, ref-wise, ref-mm-1977, ref-52-kkt, ref-bulk-geometry-prior, ref-peirce-coupling, ref-orbit-gate, ref-faraut-koranyi]
      evidence:
        - verifier: gpd-executor
          method: exact-over-Q(i) SymPy driver (43/43 PASS, exit 0; reproduced); independent cross-check that the n=4 Maxwell-stress tracelessness is conformal symmetry (n=3 control gives trace 2 != 0)
          confidence: high
          claim_id: claim-berry-same-wall
          deliverable_id: deliv-phaseA5-code
          acceptance_test_id: test-berry-shape
          reference_id: ref-wise
          evidence_path: "code/cartan_phaseA5_berry.py"
  observables:
    obs-berry-curvature:
      status: passed
      summary: "F_B = -2 Im Tr(P dP dP) of the matter-on rank-1 C_u idempotent: its matter part is antisymmetric, O(||M||^2), with the F_B^F_B Lorentz-block Pontryagin scalar 46944/571787 (gauge-invariant, frame-rotation invariant) and an EXACTLY TRACELESS Maxwell stress in n=4 (the EM signature). Compared against the independently-frozen T[M] (non-traceless, trace 680) on gauge-invariant scalars -> EM-shaped."
      linked_ids: [claim-berry-same-wall, test-berry-shape]
  deliverables:
    deliv-phaseA5:
      status: passed
      path: derivations/76-berry-same-wall.tex
      summary: "PART 2 appended: (a) the matter-on E(x;M) C_u construction (Prop B.1) + rank-1 + C_u-faithful + M->0 (Lemma B.2); (b) the matter F_B + leading O(||M||^2); (c) the F_B^F_B Lorentz-block epsilon-contraction (MM-style, cite Wise/MM77) + the EXACTLY-traceless Maxwell stress (the EM discriminant, eq B.traceless); (d) the SO(3,1) frame-rotation gauge test; (e) the independently-frozen T[M]=T[psi] (kappa first, off-switch, no F_B); (f) the VALD-04 verdict (Prop B.verdict) + the boxed EXPLICIT SOFT KILL line conjunctive with Phase 75; all 6 forbidden proxies rejected (sec B.fp2). Structural lint PASS; pdflatex unavailable (environment gate, as in 76-01)."
      linked_ids: [claim-berry-same-wall, test-berry-matter-family, test-berry-shape]
    deliv-phaseA5-code:
      status: passed
      path: code/cartan_phaseA5_berry.py
      summary: "PART 2 appended (43/43 PASS, exit 0, exact over Q(i)): build_matter_idempotent + task1_matter_idempotent (rank-1 + C_u-faithful survivor/transverse split + M->0 + leading O(||M||^2) + 2nd-direction cross-check); berry_F_at_point (watchdog-safe, 5.7s/sample); FwedgeF_pontryagin (the F_B^F_B scalar); maxwell_stress_of_FB (traceless EM discriminant); _rational_so31_rotation + frame-rotation invariance test; freeze_T_of_M / _cross_term_psi_field (independently-frozen T[psi], kappa first, no F_B); the inv_det_X_block off-switch; ricci_decomposition_n4; task2_vald04 rendering the SOFT-KILL verdict. Source guard active; sympy only."
      linked_ids: [claim-berry-same-wall, test-berry-matter-family, test-berry-shape]
  acceptance_tests:
    test-berry-matter-family:
      status: passed
      summary: "Q6 / the biggest modeling gap, RESOLVED exactly over Q(i): the matter-on E(x;M) over C_u (X_bg=I/3+M, Veronese chart with the C_u-survivor V_{1/2} matter shifting the centre) is a clean rank-1 C_u projector to ALL orders in M (E^2-E==0, Tr==1, Hermitian at a generic slice pt). C_u-FAITHFUL: the survivor matter {11,18,19,26} stays in C_u (no e_1..e_6 leak); the transverse e_1..e_6 matter {12..17,20..25} is annihilated by pi_u (proj_u(e_k)=0) -- INVISIBLE to the C_u Berry curvature, NOT a rank-changing leak (so NO Approach-2 octonionic cross-check is triggered). The M->0 limit of matter F_B := F_B(M)-F_B^vac VANISHES at t=0 (the PART-1 vacuum is recovered). Leading M-power = O(||M||^2) (ratio matter(t)/matter(t/2)->4=2^2; matter/t->0; matter/t^2->const) at two matter directions. PASS condition met (clean rank-1 C_u projector + M->0 recovery)."
      linked_ids: [claim-berry-same-wall, deliv-phaseA5, deliv-phaseA5-code, ref-peirce-coupling, ref-bulk-geometry-prior]
    test-berry-shape:
      status: passed
      summary: "THE DECISIVE SOFT-KILL CLAUSE (VALD-04), MEASURED not assumed, exact over Q(i). (1) matter F_B M-power = O(||M||^2) (confirmed by the next order). (2) the F_B^F_B Lorentz-block epsilon-contraction onto the FORCED SO(3,1) block = the Pontryagin scalar (matter 46944/571787, full 16384000/571787, vac 32), a gauge-invariant scalar UNCHANGED under a generic SO(3,1) frame rotation (L^T G L==G, I_FF equal before/after). (3) the INDEPENDENTLY-FROZEN T[M]=T[psi] (psi=2Re((x2 x1)x3) det_3 SSOT, kappa first, NO Ric/R/G, built without F_B): trace_eta=680 != 0 (non-traceless); the inv_det_X_block off-switch confirms cross-term-sourcing (R[g] ON=5.13 vs OFF=1144.87); ricci_decomposition_n4 gives S!=0/Weyl!=0. (4) THE THREE MATCHES: M-power coincides; BUT the Maxwell stress of F_B is EXACTLY TRACELESS in n=4 (trace_G==0, conformal; the EM signature) vs T[M] non-traceless (Einstein-source) -- a DECISIVE tensor-structure MISMATCH; support disjoint. PASS condition met: SOFT KILL iff EM-shaped (traceless ~F^2 / support-disjoint) -- it is. Reported FLAT on gauge-invariant scalars. NO assumed Einstein form; NO float."
      linked_ids: [claim-berry-same-wall, deliv-phaseA5, deliv-phaseA5-code, ref-wise, ref-mm-1977, ref-provost-vallee, ref-bulk-geometry-prior, ref-52-kkt, ref-orbit-gate]
  references:
    ref-provost-vallee:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "The QGT split Re=FS / Im=Berry: F_B=Im(QGT) is the object whose matter shape VALD-04 tested. Cited (PART 1 sec 1); the matter F_B is the literal -2 Im Q via the PART-1 helpers."
    ref-wise:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "The MM epsilon-contraction F^F -> EH+Lambda structure: the F_B^F_B Lorentz-block contraction (sec B.FBmatter, eq B.IFF) is the A.5(b) DIAGNOSTIC. Cited for the contraction STRUCTURE only (NOT the Phase-C forced-vs-posited audit)."
    ref-mm-1977:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "The original MM unification (Lorentz connection + coframe into one curvature whose F^F gives EH+Lambda); the structural template for the F_B^F_B contraction. Cited (sec B.FBmatter)."
    ref-52-kkt:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "h_2(C_u)~R^{3,1}, the FORCED SO(3,1) (Phase 75): the soldered (1,3) Lorentz block G=diag(+1,-1,-1,-1) is the verdict target the F_B^F_B contraction lands on + the frame group for the SO(3,1) frame-rotation gauge test. Used (sec B.frame)."
    ref-bulk-geometry-prior:
      status: completed
      completed_actions: [read, use]
      missing_actions: []
      summary: "The INDEPENDENTLY-FROZEN T[M] (spacetime_curvature_of_g + inv_det_X_block off-switch + ricci_decomposition_n4; psi=2Re((x2 x1)x3); the v17.0 cross-term pipeline). Used to build T[M] (sec B.TM); the v17.0 NONE same-wall failure pattern is what VALD-04 confirmed for the Lie sector. Binds ONLY Re (fp-reuse-cone-hessian) -- never the Im verdict."
    ref-peirce-coupling:
      status: completed
      completed_actions: [read, use]
      missing_actions: []
      summary: "slice_to_complex (e_7->i), E, proj_u_exact, h3o_from_coords: used to build the matter-on E(x;M) and to demonstrate C_u-faithfulness (survivor matter stays in C_u; transverse e_1..e_6 annihilated by proj_u). The key tool of the matter construction (sec B.matter-idempotent)."
    ref-orbit-gate:
      status: completed
      completed_actions: [use]
      missing_actions: []
      summary: "Exact-rank-over-QQ helpers were available for the frame test; a self-contained rational SO(3,1) element (_rational_so31_rotation, boost cosh=5/4 x rotation cos=3/5, L^T G L==G exact) was used directly instead (cleaner, exact over Q). Its __main__ (the ~19-min RING gate) was NOT run."
    ref-faraut-koranyi:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "The cone metric g_X=Hess(-log det) underlying the T[M] cubic-norm pipeline (the cross-terms the off-switch toggles). Cited for the T[M] construction; the cone-Hessian itself is the REAL-part object, never load-bearing for the Im verdict (fp-reuse-cone-hessian)."
  forbidden_proxies:
    fp-relabel:
      status: rejected
      notes: "The verdict is the three-way M-power + tensor-structure + support match against the INDEPENDENTLY-FROZEN T[M] (built without F_B, kappa first), NEVER 'a 2-form appears'. A nonzero antisymmetric F_B is a FIELD STRENGTH (EM, source side), not an Einstein structure -- the v17.0 Ph73 lesson. T[M]/kappa do NOT reference F_B (sec B.verdict, B.fp2)."
    fp-reuse-cone-hessian:
      status: rejected
      notes: "The cone-Hessian / Re(QGT) and the symmetric spacetime curvature R[g] (S!=0, Weyl!=0) are used ONLY to BUILD T[M]; never load-bearing for the imaginary-part verdict. The v17.0 NONE binds only Re. The decisive object is Im(QGT)=F_B, a different tensor (sec B.TM, B.fp2)."
    fp-relabel-softkill:
      status: rejected
      notes: "The EM-shaped result is reported FLAT as a SOFT KILL ('the Lie sector inherits the symmetric-sector mismatch'), never 'approximately Einstein'; an Einstein-shaped SURVIVES would not have been deflated (claims at true strength in both directions). The boxed verdict line is flat (sec B.verdict, B.fp2)."
    fp-nonabelian-gauge:
      status: rejected
      notes: "The verdict rests on gauge-invariant scalars (the F_B^F_B Pontryagin scalar, the Maxwell-stress trace) tested + confirmed invariant under a generic SO(3,1) frame rotation (L^T G L==G; I_FF unchanged; trace stays 0) (sec B.frame, B.fp2)."
    fp-float-decisive:
      status: rejected
      notes: "Every decisive number is exact over Q(i) via SymPy: the Maxwell trace is EXACTLY 0, the T[M] trace EXACTLY 680, the Pontryagin scalar an exact rational, the M-power ratios exact rationals -> 4. The i is sympy.I. NO numpy/float on the decisive path (sec B.fp2)."
    fp-octonion-algebra:
      status: rejected
      notes: "octonion_algebra.py ABSENT on the decisive path (runtime source guard PASS); psi uses oct_mul in the det_3 SSOT order (x2 x1)x3; the QGT uses the associative complex matrix product on slice_to_complex(P), NEVER the Jordan product (sec B.fp2)."
  uncertainty_markers:
    weakest_anchors:
      - "VALD-04 (test-berry-shape) was the genuinely-open SOFT-KILL clause (designed to be MEASURED, not assumed). The honest base rate leaned SOFT KILL (the symmetric sector FAILED the analogous v17.0 test) -- and the measurement CONFIRMED it: the matter F_B is EM-shaped (traceless ~F^2, conformal) and structurally disjoint from the non-traceless T[M]. Strengthened by the independent n=3-control cross-check that the n=4 tracelessness is genuine conformal symmetry, not a bug. The verdict is now a CALL for human ratification (Task 3, blocking)."
      - "The matter-on E(x;M) C_u-faithfulness (test-berry-matter-family) is RESOLVED: the survivor/transverse split (survivor V_{1/2} matter sources the C_u Berry response; transverse e_1..e_6 is projected away, not a rank-changing leak) makes the matter family a clean rank-1 C_u projector exactly over Q(i). No Approach-2 octonionic cross-check needed."
      - "The matter direction is a single generic rational C_u-survivor V_{1/2} element (cross-checked at a 2nd direction for M->0 + the O(||M||^2) power). The structural EM signature (traceless Maxwell stress in 4d) is direction-INDEPENDENT (it holds for ANY antisymmetric 2-form in n=4), so the verdict is robust to the direction choice."
    unvalidated_assumptions:
      - "kappa (the overall T[M] scale) is frozen as a single global constant; since the verdict is the TENSOR STRUCTURE mismatch (traceless vs non-traceless) -- a kappa-INDEPENDENT fact -- no kappa fit can rescue an EM-shaped F_B into an Einstein-shaped match. The structural verdict does not depend on the kappa value."
    competing_explanations:
      - "Could the matter F_B be Einstein-shaped under a different matter direction or a different (octonionic Approach-2) QGT? The EM signature (traceless Maxwell stress in n=4) is a structural fact of ANY antisymmetric 2-form, direction- and realization-independent, so no -- the antisymmetric/Lie sector is intrinsically a field-strength sector. This is exactly why the SOFT KILL is robust."
    disconfirming_observations:
      - "Matter F_B traceless (Maxwell trace_G==0) and ~F^2 -> EM-shaped -> SOFT KILL: OBSERVED (the decisive finding)."
      - "Matter-source support disjoint from T[M] (a traceless conformal stress vs a non-traceless gradient stress): OBSERVED."
      - "M-power match (both O(||M||^2)): OBSERVED -- but the tensor-structure mismatch is decisive regardless (a matching power does NOT rescue an EM-shaped tensor)."
      - "The F_B^F_B contraction / verdict scalar changing under an SO(3,1) frame rotation would be a gauge artifact: NOT observed (I_FF and the Maxwell trace are invariant)."
      - "The matter-on E(x;M) NOT a clean rank-1 C_u projector (rank change / verdict-altering e_1..e_6 leak): NOT observed (clean rank-1 to all orders; transverse matter projected away, not a leak)."
      - "T[M] or kappa referencing F_B (circular): NOT the case (T[psi] built from the det_3 cross-term, kappa first, no F_B)."

comparison_verdicts:
  - subject_id: test-berry-shape
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-bulk-geometry-prior
    comparison_kind: cross_method
    metric: "tensor structure (Maxwell-stress trace: traceless EM-shaped vs non-traceless Einstein-source) + M-power + support, on gauge-invariant scalars"
    threshold: "Einstein-shaped (SURVIVES) iff M-power + non-traceless structure + coincident support all match T[M]; EM-shaped (SOFT KILL) iff traceless ~F^2 / structurally disjoint"
    verdict: fail
    recommended_action: "SOFT KILL: recommend STOP before Phase B (77). A.5 is CONJUNCTIVE with Phase 75 (SURVIVES); a SOFT KILL here ends milestone v18.0 as a publishable negative. AWAITING Bryan's blocking ratification (Task 3) before the milestone-gating call is final."
    notes: "matter F_B: antisymmetric 2-form, F_B^F_B Pontryagin 46944/571787 (frame-invariant), Maxwell stress EXACTLY traceless in n=4 (trace_G==0, conformal; n=3 control 2!=0) => EM-shaped. T[M]=T[psi]: non-traceless (trace_eta=680), cross-term-sourced (off-switch R[g] ON 5.13 vs OFF 1144.87), S!=0/Weyl!=0 => Einstein-source. M-power coincides (O(||M||^2)) but tensor structure is a DECISIVE mismatch and support disjoint. The Lie sector inherits the v17.0 symmetric-sector same-wall mismatch. 'fail' = SOFT KILL (the F_B-vs-T[M] match FAILS); reported FLAT, negative-result-is-success."

duration: 78min
completed: 2026-06-02
checkpoint_status: "AWAITING BLOCKING HUMAN RATIFICATION (Task 3, checkpoint:human-verify) -- Bryan ratifies the milestone-gating SOFT-KILL/SURVIVES call. The math is DECIDED (43/43 PASS, exact over Q(i)); this checkpoint ratifies the CALL and its Phase-77 consequence, NOT the arithmetic. NOT self-ratified."
---

# Phase 76 (Plan 02): Berry-Curvature Same-Wall Gate -- PART 2 (the decisive / matter half) Summary

**VALD-04 DECIDED exactly over Q(i): the matter-on canonical Berry curvature F_B is EM-SHAPED -- an antisymmetric 2-form whose F_B^F_B Lorentz-block contraction is the Pontryagin ~F^2 density and whose Maxwell stress is EXACTLY traceless in n=4 (conformal, frame-rotation invariant), STRUCTURALLY DISJOINT from the non-traceless, independently-frozen T[M] (trace 680, cross-term-sourced). The Lie/antisymmetric sector INHERITS the v17.0 symmetric-sector same-wall mismatch => PROPOSED VERDICT: SOFT KILL. Reported FLAT (negative-result-is-success). CONJUNCTIVE with Phase 75 (SURVIVES): a SOFT KILL ends milestone v18.0 as a publishable negative; recommend STOP before Phase B (77). AWAITING Bryan's blocking ratification (Task 3).**

## Performance

- **Duration:** ~78 min
- **Started:** 2026-06-02T14:56:02Z
- **Completed (computation):** 2026-06-02 (awaiting human ratification)
- **Tasks:** 3 (Tasks 1-2 complete + committed; Task 3 = the blocking human-verify checkpoint)
- **Files modified:** 2 (code + derivation; both appended PART 2)

## Key Results

- **Task 1 -- the matter-on E(x;M) over C_u (the biggest modeling gap, Q6, RESOLVED) [CONFIDENCE: HIGH]:** E(x;M)=v v^dag/(v^dag v) with the C_u-survivor V_{1/2} matter shifting the Veronese centre is a clean rank-1 C_u projector to ALL orders in M (E^2-E==0, Tr==1, Hermitian). C_u-FAITHFUL: the survivor matter {11,18,19,26} stays in C_u; the transverse e_1..e_6 matter {12..17,20..25} is annihilated by pi_u (proj_u(e_k)=0) -- INVISIBLE to the C_u Berry curvature, NOT a rank-changing leak. M->0 recovers the PART-1 vacuum F_B^vac=-2 omega_K exactly. Leading matter F_B = O(||M||^2) (ratio ->4=2^2 at two matter directions) -- the v17.0 order of the metric h.
- **Task 2 -- VALD-04, the decisive clause [CONFIDENCE: HIGH]:**
  - matter F_B is ANTISYMMETRIC (a field strength). F_B^F_B Lorentz-block epsilon-contraction (MM-style Pontryagin scalar): matter 46944/571787, full 16384000/571787, vacuum 32 -- gauge-invariant, SO(3,1) frame-rotation invariant.
  - **THE EM SIGNATURE: the Maxwell stress of F_B is EXACTLY traceless in n=4 (G^mu_mu T==0 over Q)** -- the conformal invariance of any antisymmetric 2-form in 4d (n=3 control gives trace 2 != 0, so this is genuine, not a bug). F^2 = 472320/47458321.
  - The INDEPENDENTLY-FROZEN T[M]=T[psi] (psi=2Re((x2 x1)x3), kappa first, NO reference to F_B) is NON-traceless (trace_eta=680), cross-term-sourced (off-switch R[g] ON=5.13 vs OFF=1144.87), S!=0/Weyl!=0 (the Einstein-source signature -- the v17.0 symmetric object that BUILDS T[M], never the Im verdict).
  - THE THREE MATCHES: M-power coincides (both O(||M||^2)); BUT tensor structure is a DECISIVE MISMATCH (traceless EM-shaped F_B vs non-traceless Einstein-source T[M]); support disjoint => EM-SHAPED => SOFT KILL.

## Task Commits

1. **Task 1: matter-on E(x;M) over C_u -- rank-1 + C_u-faithful + M->0 + O(||M||^2)** - `1739bd14` (compute)
2. **Task 2: VALD-04 decisive -- matter F_B EM-shaped vs non-traceless T[M] => SOFT KILL** - `bb757662` (compute)
3. **Task 3 (deriv): PART 2 verdict -- the SOFT KILL line** - `f4e2b075` (derive); research log `7f7c78c4`

_Driver: 43/43 PASS, exit 0, exact over Q(i), reproducible._

## Equations Derived (PART 2)

**Eq. (B.matter-chart)** -- the matter-on idempotent chart (matter shifts the Veronese centre):

z1 = a + i b + mu1 t  (x3 slot),  z2 = c + i d + mu2 t  (x2 slot);  E(x;M) = v v^dag/(v^dag v), v=[1,z1,z2].

**Eq. (B.Mpower)** -- the leading matter Berry curvature: F_B^matter := F_B(M) - F_B^vac = O(||M||^2).

**Eq. (B.IFF)** -- the MM-style F_B^F_B Lorentz-block contraction: I_FF = eps^{mu nu rho sig} F_B[mu,nu] F_B[rho,sig] (Pontryagin scalar).

**Eq. (B.traceless)** -- THE EM SIGNATURE: G^{mu nu} T[F_B]_{mu nu} = 0 (the n=4 conformal tracelessness of the Maxwell stress).

**Eq. (B.TM)** -- the independently-frozen stress: T[M]_{mu nu} = d_mu psi d_nu psi - 1/2 eta_{mu nu} (d psi)^2, psi = 2 Re((x2 x1) x3); tr_eta T[M] = 680 != 0.

## Validations Completed

- Matter-on E(x;M): rank-1 idempotent SYMBOLIC in M (E^2-E==0, Tr==1, Hermitian) at a generic slice point.
- C_u-faithfulness: survivor matter stays in C_u (no leak); transverse e_1..e_6 annihilated by pi_u (the matter family stays a clean rank-1 C_u projector).
- M->0 limit: matter F_B vanishes at t=0; the PART-1 vacuum F_B^vac=-2 omega_K recovered exactly.
- Leading M-power O(||M||^2): exact ratio matter(t)/matter(t/2)->4=2^2; matter/t->0; matter/t^2->const; at two matter directions.
- F_B antisymmetric; F_B^F_B Pontryagin scalar nonzero; gauge-invariant.
- SO(3,1) frame-rotation test: L^T G L==G exact; I_FF unchanged; Maxwell trace stays 0.
- Maxwell stress of F_B EXACTLY traceless in n=4 (trace_G==0 over Q) -- independently cross-checked as conformal symmetry (n=3 control gives trace 2 != 0).
- T[M] non-traceless (trace_eta=680), built WITHOUT reference to F_B; off-switch cross-term-sourcing (R[g] ON=5.13 vs OFF=1144.87); ricci_decomposition_n4 S!=0/Weyl!=0.
- Source guard: octonion_algebra absent on the decisive path; oct_mul SSOT order (x2 x1)x3 in psi; no numpy/float.
- Reproducibility: full driver 43/43 PASS, exit 0.

## Decisions Made

- The EM-vs-Einstein verdict is decided on the Maxwell-stress TRACE (gauge-invariant, frame-rotation invariant): F_B's stress is EXACTLY traceless in n=4 (conformal) => EM-shaped. This is the decisive tensor-structure discriminant, not "a 2-form appears" (fp-relabel).
- T[M] built from the det_3 SSOT cross-term psi via T[psi] (Phase-73 DERV-03 pattern), kappa frozen first, WITHOUT reference to F_B -- non-circular.
- The matter-on E(x;M) uses the Veronese chart with the C_u-survivor V_{1/2} matter shifting the centre; transverse e_1..e_6 matter is projected away by pi_u (the C_u-faithfulness resolution), NOT a rank-changing leak.

## Deviations from Plan

### [Rule 1 - Code bug] missing module-level import (auto-fixed)

`diff` / `LeviCivita` were used in freeze_T_of_M / _levi_civita_4 but not imported at module level (NameError). Auto-fixed (added to the top-of-file sympy import). Verified by re-run (EXIT=0, 43/43 PASS). Correctness-only; no physics change.

### Watchdog mitigation (not a deviation -- a performance fix the plan anticipated)

The all-symbolic-in-t berry_F is the >200s symbolic-inverse cliff the plan warned about. FIX = berry_F_at_point: differentiate the projector symbolically, then EVALUATE the derivatives at the rational base point so the trace algebra is over rational complex 3x3 matrices (5.7s/sample, exact over Q(i)). Sample counts kept tight; tasks committed immediately. The full driver runs in <2 min.

### Environment Gate (not a deviation)

**LaTeX compilation unavailable.** pdflatex/latexmk are not installed (same as 76-01). The PART-2 derivation was validated by a structural lint (env begin/end balance, single document env, brace balance, math-mode parity, no duplicate labels -- PASS; the one `\[`-vs-`\]` flag is a false positive from `\\[2pt]` line-spacing inside a pre-existing PART-1 pmatrix) and committed as source.

## Issues Encountered

None beyond the auto-fixed import (Rule 1) and the watchdog performance fix. The matter-on construction, the EM signature, and the T[M] contrast were all clean and reproducible.

## Open Questions

- (Task 3, blocking) The milestone-gating SOFT-KILL/SURVIVES call awaits Bryan's ratification. The math is DECIDED (43/43 PASS, exact over Q(i)); the checkpoint ratifies the CALL and its Phase-77 consequence.
- (If ratified) Phase 77 (Phase B) greenlight requires BOTH Phase 75 (SURVIVES) AND Phase 76 to SURVIVE (conjunctive). A SOFT KILL here ends milestone v18.0 as a publishable negative -- recommend STOP before Phase B.

## Cross-Phase Dependencies

### Results This Phase Provides To Later Phases

| Result | Used By | How |
| ------ | ------- | --- |
| VALD-04 SOFT KILL (matter F_B EM-shaped) | 77 (Phase B), milestone v18.0 | Conjunctive with Phase 75: a SOFT KILL blocks the Phase-77 greenlight; ends v18.0 as a publishable negative |
| The matter-on E(x;M) C_u construction + the EM signature | (write-up) paper8 / paper6-cartan-tetrad | The Lie-sector Berry curvature is a Maxwell-type field strength, not an Einstein structure |

### Results This Phase Consumed From Earlier Phases

| Result | From | Verified Consistent |
| ------ | ---- | ------------------- |
| Calibrated QGT recipe + vacuum F_B^vac=-2 omega_K | 76-01 | Yes -- M->0 limit recovers it exactly |
| FORCED SO(3,1) block G=diag(+1,-1,-1,-1), survivors {11,18,19,26} | Phase 75 | Yes -- the F_B^F_B contraction target + frame group |
| T[M] pipeline (psi cross-term, off-switch, ricci_decomposition_n4) | v17.0 (Phase 73) | Yes -- engine reproduced; binds only Re (fp-reuse-cone-hessian) |
| det SSOT det_3 / oct_mul SSOT order | v16.0 (ring_lemma) | Yes -- source guard PASS; psi uses (x2 x1)x3 |

### Convention Changes

| Convention | Previous | This Phase | Reason |
| ---------- | -------- | ---------- | ------ |
| None -- all v18.0 conventions preserved | | | The QGT/berry_curvature_FB/u=e_7/metric_signature/SO(3,1) locks were honored exactly |

## Self-Check: PASSED

- Files exist: code/cartan_phaseA5_berry.py, derivations/76-berry-same-wall.tex, 76-02-SUMMARY.md, 76-02-LOG.md (all FOUND).
- Commits exist: 1739bd14 (Task 1), bb757662 (Task 2), f4e2b075 (Task 3 deriv), 7f7c78c4 (log).
- Driver reproducible: 43/43 PASS, exit 0, exact over Q(i).
- Domain final check (math_phys / GR / topological): integer/structural invariants OK (the Pontryagin scalar is an exact rational; the Maxwell-stress tracelessness is exact 0; the SO(3,1) frame rotation preserves G exactly). Gauge-invariance of the verdict scalars verified under a frame rotation.
- Contract coverage: claim-berry-same-wall (passed); obs-berry-curvature (passed); deliv-phaseA5 + deliv-phaseA5-code (passed); test-berry-matter-family + test-berry-shape (passed); all 8 references completed; all 6 forbidden proxies rejected; the decisive comparison_verdict (test-berry-shape: fail = SOFT KILL) recorded.

## Self-Check: contract coverage complete (no contract ID omitted)

NOTE: the only outstanding item is the BLOCKING human ratification (Task 3, checkpoint:human-verify). The computational ledger is COMPLETE and the verdict PROPOSED (SOFT KILL); state advance / milestone consequence are deferred to Bryan's ratification per the plan (NOT self-ratified).

---

_Phase: 76-phase-a-5-berry-curvature-same-wall-gate-soft-kill_
_Completed (computation): 2026-06-02 -- AWAITING blocking human ratification (Task 3)_
