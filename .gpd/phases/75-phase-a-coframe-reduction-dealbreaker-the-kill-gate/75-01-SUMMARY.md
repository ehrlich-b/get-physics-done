---
phase: 75-phase-a-coframe-reduction-dealbreaker-the-kill-gate
plan: 01
depth: full
one-liner: "Phase A KILL gate SURVIVES (human-ratified): with (E_11,u=e_7) fixed, pi_u reduces V_{1/2}(16) to a 4-dim Lorentzian (1,3) coframe carrying SO(3,1) FORCED by (E_11,u) -- all 3 clauses exact over Q (dim 4; soldering target (1,3)+B rank 4; residual 21=so(3,1)[6]+so(6)[15]); greenlight Phase 77 conjunctive with Phase 76"
subsystem: [validation, derivation, formalism]
tags: [octonions, jordan-algebra, peirce-decomposition, cartan-geometry, soldering-form, coframe, spin(9,1), so(3,1), lorentzian-signature, exact-over-Q, kill-gate]

# Dependency graph
requires:
  - phase: 74-engine-recovery
    provides: "T_{E_11}OP^2 = V_{1/2}(E_11) (dim 16, idx 11..26); E_11 o delta=(1/2)delta; calibration anchors 17/61/45; det SSOT re-certified"
  - phase: 52-kkt-spacetime
    provides: "V_0=h_2(O) -> h_2(C_u) ~= R^{3,1}; det_2 (1,3) G=diag(+1,-1,-1,-1); SO(3,1) boosts B_i=L_{sigma_i} sig (3,3); OD3 rank-4-on-pi_u(V_0)"
  - phase: 48
    provides: "Spin(9,1) ⊃ Spin(3,1) x Spin(6) (Lorentz x internal split)"
provides:
  - "CALC-01: dim pi_u(V_{1/2}(16)) over Q == 4, survivors {11,18,19,26}=C_u^2; V_0-limit dim pi_u(V_0)==4"
  - "CALC-02: induced coframe pairing = soldering-form metric (Sharpe g=e^*eta) realized via Peirce bilinear B; signature (1,3) on R^{3,1} target, B rank 4 surjective, n(delta) on forward light cone, image(B)==pi_u(V_0); trace-form foil diag(2,2,2,2)=(4,0) reported NOT-the-verdict"
  - "VALD-02: residual structure group dim 21 = so(3,1)[6] (+) so(6)[15]; the so(3,1) Lorentz block (action on the C_u 4-space) FORCED by (E_11,u), Killing sig (3,3); so(6) internal (trivial on spacetime)"
  - "VERDICT: Phase A SURVIVES (human-ratified) -- greenlight Phase 77 (conjunctive with Phase 76)"
affects: [76-phase-a5-berry-same-wall, 77-phase-b-cartan-curvature, 78-phase-c-circularity-audit]

# Physics tracking
methods:
  added: ["soldering-form-metric (Sharpe g=e^*eta) realized exact-over-Q via the Peirce soldering bilinear B=(delta o delta')|_{V_0} into R^{3,1}", "residual-structure-group as exact nullspace over QQ of {Stab_{V_0} preserving the C_u 4-space}", "Killing-form signature (3,3) test for so(3,1) over QQ"]
  patterns: ["soldering-vs-trace-form design point: read the Lorentzian verdict on the R^{3,1} TARGET, report the Euclidean OP^2 Fubini-Study trace-form as the diagnostic FOIL", "calibration anchors (61/45) reproduced BEFORE any new stabilizer count", "import-only orbit_dimension_gate helpers (never the slow __main__)"]

key-files:
  created: [code/cartan_phaseA_coframe.py, derivations/75-coframe-reduction.tex]
  modified: []

key-decisions:
  - "The induced coframe pairing is the soldering-form metric (candidate b), realized exact over Q via the candidate-(c) Peirce soldering bilinear B; the bare trace form diag(2,2,2,2)=(4,0) is the compact OP^2 Fubini-Study FOIL, NEVER the verdict (the single most important design point; defeats the Euclidean-trap false KILL)"
  - "VALD-02 reports the residual group at dim 21 (not bare 6): 21 = so(3,1)[6] (+) so(6)[15]; the extra so(6) acts TRIVIALLY on the spacetime 4-space (the canonical Phase-48 internal sector), so it is NOT extra Lorentz freedom and NOT an arbitrary frame choice -- SO(3,1) is FORCED"
  - "det_2(delta o delta)==0 identically is the forward LIGHT CONE (x0=(1/2)||delta||^2>=0), NOT a degenerate metric (Pitfall 3 avoided)"
  - "Source guard: the single `import det_3 as oa_det_3` line in ring_lemma is the SANCTIONED in-fence float oracle (Phase-0 DERV-01 semantics) -- never on the decisive path (octonion_algebra absent from sys.modules); distinguished from a genuine offender that would shadow an exact primitive"

patterns-established:
  - "Soldering-form-metric reading: Lorentzian (1,3) is read on the R^{3,1} TARGET (validated det_2), B confirmed rank-4 surjective; the trace-form Euclidean (4,0) is the diagnostic foil"
  - "Both-readings transparency: report the foil ALONGSIDE the verdict so the reader sees 4-dim is genuine (CALC-01) but Lorentzian is a SOLDERED (not intrinsic-to-V_{1/2}) property"

conventions:
  - "natural units (hbar=1, dimensionless)"
  - "metric signature mostly-minus (+,-,-,-): det_2=x0^2-x1^2-x2^2-x3^2, G=diag(+1,-1,-1,-1), signature (1,3); bulk OP^2 trace form Riemannian (4,0)"
  - "Jordan product a o b = (1/2)(ab+ba)"
  - "octonion multiplication Fano e1 e2 = e4; complex structure u = e_7 (C_u=span{1,e_7})"
  - "primitive idempotent E_11 = diag(1,0,0); Peirce eigenvalues {0,1/2,1}"
  - "det SSOT = ring_lemma_verification.py det_3 (cross-term 2Re((x2 x1)x3)); octonion_algebra.py BANNED on the decisive path"
  - "EXACT over Q on every decisive verdict (sympy rank/eigenvals/nullspace over QQ); float = triage only"

# Canonical contract outcome ledger
plan_contract_ref: ".gpd/phases/75-phase-a-coframe-reduction-dealbreaker-the-kill-gate/75-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-coframe-reduction:
      status: passed
      summary: "THE KILL GATE PASSES. With (E_11,u=e_7) fixed, pi_u reduces the 16-dim V_{1/2}(E_11) soldering form e=dE to a 4-dim coframe that is Lorentzian (1,3) and carries a residual structure group containing SO(3,1) FORCED by (E_11,u). Decided by exact image dimension (4), exact Gram-eigenvalue signature on the soldering target ((1,3), B rank 4), and a forced residual-structure-group analysis (21=so(3,1)+so(6), so(3,1) Lorentz block forced). Human-ratified (Bryan, 'approved'); orchestrator re-ran the driver (exit 0, ALL_PASS, 24/24) and reproduced all three clauses exact over Q."
      linked_ids: [deliv-phaseA, test-coframe-dim, test-coframe-signature, test-coframe-forced, ref-52-kkt, ref-52-uniqueness, ref-phase74, ref-sharpe, ref-baez, ref-mccrimmon]
      evidence:
        - verifier: gpd-executor
          method: exact-over-Q linear algebra (sympy rank/eigenvals/nullspace over QQ)
          confidence: high
          claim_id: claim-coframe-reduction
          deliverable_id: deliv-phaseA
          acceptance_test_id: test-coframe-dim
          reference_id: ref-phase74
          evidence_path: "code/cartan_phaseA_coframe.py"
        - verifier: orchestrator
          method: independent driver re-run (exit 0, ALL_PASS, 24/24) + human ratification
          confidence: high
          claim_id: claim-coframe-reduction
          deliverable_id: deliv-phaseA
          acceptance_test_id: test-coframe-forced
          reference_id: ref-52-kkt
          evidence_path: "derivations/75-coframe-reduction.tex"
  deliverables:
    deliv-phaseA:
      status: passed
      path: derivations/75-coframe-reduction.tex
      summary: "Phase A coframe-reduction verdict derivation: exact image dim 4 (C_u reduction explicit, survivors {11,18,19,26}=C_u^2); exact Gram-eigenvalue signature (1,3) on the R^{3,1} soldering target via the Peirce bilinear B (rank 4 surjective, n(delta) on the forward light cone, image(B)==pi_u(V_0)), with the trace-form Euclidean (4,0) foil reported as NOT the verdict; forced residual-structure-group analysis (anchors 61/45; residual 21=so(3,1)[6]+so(6)[15], so(3,1) FORCED); a DECISIVE SURVIVES verdict; every forbidden proxy explicitly rejected. Backed exact-over-Q by code/cartan_phaseA_coframe.py (ALL_PASS, exit 0)."
      linked_ids: [claim-coframe-reduction, test-coframe-dim, test-coframe-signature, test-coframe-forced]
  acceptance_tests:
    test-coframe-dim:
      status: passed
      summary: "dim pi_u(V_{1/2}(16)) over Q == EXACTLY 4 (column rank of the image matrix M over QQ); survivors {11,18,19,26}=C_u^2; zero octonion comps e_1..e_6 leak; V_0-limit dim pi_u(V_0)==4 (the validated 10->4). Decisive integer over Q, no softening, no sub-piece selection. Greenlight clause (a)."
      linked_ids: [claim-coframe-reduction, deliv-phaseA, ref-52-uniqueness, ref-phase74]
    test-coframe-signature:
      status: passed
      summary: "VERDICT pairing = soldering-form metric via the Peirce bilinear B(delta,delta')=(delta o delta')|_{V_0} into R^{3,1}: rank(B)==4 surjective (=OD3 rank-4-on-pi_u(V_0)); det_2 target signature == (1,3) Lorentzian/mostly-minus (raw {beta,gamma,p,q} and orthonormal G=diag(+1,-1,-1,-1) frames agree); n(delta)=B(delta,delta) on the forward light cone (det_2==0 identically, x0=(1/2)||delta||^2>=0); image(B)==pi_u(V_0). FOIL: bare trace Gram == diag(2,2,2,2), signature (4,0) Euclidean = the compact OP^2 Fubini-Study metric, reported transparently and NEVER the verdict. No Wick rotation. Greenlight clause (b)."
      linked_ids: [claim-coframe-reduction, deliv-phaseA, ref-52-kkt, ref-sharpe, ref-baez]
    test-coframe-forced:
      status: passed
      summary: "MEASURED (not assumed): calibration anchors Stab_{E_6}(E_11)=61 (orbit 17) and Stab_{V_0}=45=Spin(9,1) reproduced exactly over Q FIRST. Residual structure group = exact nullspace over QQ of {Stab_{V_0} preserving the C_u 4-space pi_u(V_0)} = dim 21 = so(3,1)[6] (+) so(6)[15] (the block-diagonal Lorentz x internal part of Spin(9,1) ⊃ Spin(3,1) x Spin(6)). The residual action on the C_u 4-space spans dim 6 == so(3,1), kills the det_2 form (A^T g + g A = 0), Killing signature (3,3) (matched to the 52-kkt boosts; the Spin(3,1) 4d vector, not Spin(6) internal). The 4-space is the C_u-projector eigenspace (idempotent, eigenvalues {1:4,0:12}; u-determined). so(6) acts trivially on spacetime (internal sector, not arbitrary frame freedom). SO(3,1) FORCED by (E_11,u) with no extra free parameters. Greenlight clause (c)."
      linked_ids: [claim-coframe-reduction, deliv-phaseA, ref-52-kkt, ref-52-uniqueness]
  references:
    ref-52-kkt:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "The validated V_0 -> h_2(C_u) ~= R^{3,1} precedent: det_2 (1,3) G=diag(+1,-1,-1,-1) is the SOLDERING TARGET the coframe maps onto (CALC-02 verdict read here); SO(3,1) boosts B_i=L_{sigma_i} sig (3,3) matched in VALD-02; the SAME pi_u reused for V_{1/2} (V_0-limit cross-check). Cited in the derivation references."
    ref-52-uniqueness:
      status: completed
      completed_actions: [read, compare, cite]
      missing_actions: []
      summary: "OD3 V_{1/2} x V_{1/2} -> V_0 surjective rank-4-on-pi_u(V_0) IS the soldering bilinear B and the CALC-02 surjectivity check (rank(B)==4 reproduced). Uniqueness Theorem pi_u(V_0)=h_2(C_u) the unique 4-dim JSpin(3) image of pi_u, FORCED by u -- paralleled (not blindly copied) by the VALD-02 measured residual-group rank for V_{1/2}. Cited."
    ref-phase74:
      status: completed
      completed_actions: [read, use]
      missing_actions: []
      summary: "Phase 74 (verified 9/9 HIGH) supplied the warm-engine reuse pattern, the Peirce layout V_{1/2}=idx 11..26 (regression re-checked), the _report harness, the det SSOT source guard, and the calibration anchors 17/61/45 (reproduced in VALD-02). Driver pattern copied; tangent identity not redone."
    ref-sharpe:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Sharpe 1997 soldering-form / Cartan-geometry definition g=e^*eta -- the reason the induced coframe pairing is the soldering-form metric (candidate b), not the bare trace form. Cited as the design-point justification."
    ref-baez:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Baez 2002: OP^2=F_4/Spin(9), T_E OP^2=V_{1/2}; OP^2 a compact Riemannian symmetric space (no invariant Lorentzian form) -- WHY the bare trace form is Euclidean (4,0) and the Lorentzian structure must be SOLDERED. Cited for the foil."
    ref-mccrimmon:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "McCrimmon 2004: Peirce decomposition, E o delta=(1/2)delta, primitive idempotents -- the Peirce identity defining V_{1/2} (verified Phase 74, not re-derived). Cited."
  forbidden_proxies:
    fp-arbitrary-reduction:
      status: rejected
      notes: "The 4 and SO(3,1) are EARNED by exact rank (CALC-01) and the forced residual-group computation (VALD-02): the 4-space is the canonical C_u-projector eigenspace (eigenvalue-1 space, u-determined); NO 4-of-16 direction selection, NO non-canonical projection, NO Wick rotation, NO arbitrary SO(3,1) frame. The so(6) summand acts trivially on spacetime (internal sector), so it is not extra Lorentz freedom from a frame choice."
    fp-relabel-approx-4d:
      status: rejected
      notes: "All three clauses pass at true strength; nothing relabeled 'approximately 4d/Lorentzian/morally Einstein'. The verdict is a clean SURVIVES; a failed clause would have been reported as a flat KILL (negative-result-is-success)."
    fp-float-decisive:
      status: rejected
      notes: "Every decisive number (image dim, Gram signatures, soldering-map rank, residual-group dim, Killing signature) is a rational/integer from sympy.Matrix.rank/.eigenvals/.nullspace over QQ. Float is triage-only. The exact cancellation det_2(delta o delta)==0 is identical, not approximately zero."
    fp-octonion-algebra:
      status: rejected
      notes: "det SSOT = ring_lemma_verification.py det_3; octonion/Jordan primitives from bulk_geometry_verification.py; C_u map from embedding_under_E_verification.py. octonion_algebra.py absent on the decisive path (not in sys.modules after the decisive imports; decisive primitives RL.det_3/Tr/jordan are native exact-over-Q). The single `import det_3 as oa_det_3` line is the sanctioned in-fence float oracle, never shadowing the exact primitive."
  uncertainty_markers:
    weakest_anchors:
      - "VALD-02 forced-vs-arbitrary SO(3,1) (test-coframe-forced) was the genuinely-open clause (MEDIUM a priori). RESOLVED by an exact residual-group rank over QQ (not assumed by analogy): residual 21=so(3,1)[6]+so(6)[15], the so(3,1) Lorentz block FORCED (canonical C_u eigenspace + Killing sig (3,3))."
      - "The judgment that the soldering bilinear B=(delta o delta')|_{V_0} is THE canonical coframe pairing -- defended by OD3 (unique Peirce map to the validated R^{3,1}) and the OP^2-Riemannian-symmetric impossibility of an intrinsic Lorentzian form; BOTH readings (foil + verdict) reported for audit."
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations:
      - "NONE triggered. All disconfirmers were checked and excluded exactly over Q: image dim == 4 (not 6/8/16); B rank == 4 (not <4); target signature == (1,3) (not (2,2)/(4,0)/degenerate); residual has NO extra free parameters tracing to a frame choice (the so(6) is internal, trivial on spacetime); image(B)==pi_u(V_0) (solders to THE spacetime, not a look-alike)."

# Decisive comparison verdicts (internal-anchor comparisons the contract leans on)
comparison_verdicts:
  - subject_id: ref-52-kkt
    subject_kind: reference
    subject_role: decisive
    reference_id: ref-52-kkt
    comparison_kind: benchmark
    metric: exact_signature_and_dim_equality
    threshold: "soldering target det_2 == (1,3) G=diag(+1,-1,-1,-1); V_0-limit pi_u(V_0)==4; boosts sig (3,3) (all exact over Q)"
    verdict: pass
    recommended_action: "Carry the soldering-form (1,3) target metric and the SO(3,1) Lorentz structure into Phase 77."
    notes: "The validated V_0 -> h_2(C_u) ~= R^{3,1} precedent: det_2 (1,3) Eq.46.4 reproduced as the CALC-02 soldering target; same pi_u gives the V_0-limit 10->4; 52-kkt boosts B_i=L_{sigma_i} sig (3,3) matched in VALD-02."
  - subject_id: ref-52-uniqueness
    subject_kind: reference
    subject_role: decisive
    reference_id: ref-52-uniqueness
    comparison_kind: cross_method
    metric: exact_rank_equality
    threshold: "rank(B onto pi_u(V_0)) == 4 (= OD3 rank-4-on-pi_u(V_0)); image(B)==pi_u(V_0) (exact over Q)"
    verdict: pass
    recommended_action: "Treat B as the OD3 soldering map; the coframe solders to THE validated spacetime."
    notes: "OD3 surjective rank-4-on-pi_u(V_0) IS the CALC-02 soldering bilinear B (reproduced); the V_0 Uniqueness Theorem 'forced' result is PARALLELED (not copied) by the measured VALD-02 residual-group rank for V_{1/2}."
  - subject_id: test-coframe-dim
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-52-kkt
    comparison_kind: baseline
    metric: exact_integer_equality
    threshold: "== 4 (exact over Q)"
    verdict: pass
    recommended_action: "Use the 4-dim C_u^2 coframe (survivors {11,18,19,26}) in Phase 77."
    notes: "V_0-limit cross-check: pi_u(V_0)==4 reproduces the validated 52-kkt 10->4 reduction."
  - subject_id: test-coframe-signature
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-52-kkt
    comparison_kind: benchmark
    metric: exact_signature_equality
    threshold: "(1,3) on the R^{3,1} target AND rank(B)==4 (exact over Q)"
    verdict: pass
    recommended_action: "Carry the soldering-form metric (1,3) target into the Phase-77 Cartan curvature; the (4,0) trace-form foil is NOT the spacetime metric."
    notes: "Matches 52-kkt det_2 (1,3) G=diag(+1,-1,-1,-1) Eq.46.4; B==OD3 rank-4-on-pi_u(V_0) (52-uniqueness); image(B)==pi_u(V_0)."
  - subject_id: test-coframe-forced
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-52-uniqueness
    comparison_kind: cross_method
    metric: exact_rank_and_killing_signature
    threshold: "residual contains so(3,1) (dim 6, Killing sig (3,3)) FORCED, no extra frame-choice free params (exact over Q)"
    verdict: pass
    recommended_action: "Treat SO(3,1) as the FORCED Lorentz structure group for the Phase-77 omega connection; the so(6) is the internal sector."
    notes: "Anchors 61/45 reproduced first (Phase 74 VALD-01); residual 21=so(3,1)[6]+so(6)[15]; so(3,1) kills the det_2 form; matched to the 52-kkt boosts ([B_i,B_j]=-eps_ijk J_k, sig (3,3))."

# Metrics
duration: 10min
completed: 2026-06-02
---

# Phase 75: Phase A -- Coframe-Reduction Dealbreaker (THE KILL GATE) Summary

**Phase A KILL gate SURVIVES (human-ratified): with (E_11, u=e_7) fixed, the C_u bottleneck pi_u reduces the 16-dim V_{1/2}(E_11) soldering form e=dE to a 4-dim coframe that is Lorentzian (1,3) and carries a residual structure group containing SO(3,1), FORCED by (E_11,u) -- all three clauses decided EXACTLY over Q. Greenlight Phase 77 (conjunctive with Phase 76 / A.5).**

## Performance

- **Duration:** ~10 min (compute trivial: all matrices small, exact-over-Q runs ~1-2 s each)
- **Started:** 2026-06-02T03:23:05Z
- **Completed:** 2026-06-02T03:33:28Z (+ ratification finalize)
- **Tasks:** 4/4 (CALC-01, CALC-02, VALD-02 computed+committed; Task-4 derivation written+committed; verdict human-ratified)
- **Files modified:** 2 created (driver + derivation)

## Key Results

- **CALC-01 (clause a):** `dim pi_u(V_{1/2}(16)) over Q == 4` EXACTLY, survivors **{11,18,19,26} = C_u^2** = {Re(x2), <x2,e7>, Re(x3), <x3,e7>}; zero octonion comps e1..e6 leak; **V_0-limit `dim pi_u(V_0) == 4`** (reproduces the validated 52-kkt 10->4).
- **CALC-02 (clause b):** induced coframe pairing = the **soldering-form metric** (Sharpe g=e*eta) realized via the Peirce bilinear `B(delta,delta')=(delta o delta')|_{V_0}` into R^{3,1}: **rank(B)==4 surjective**, **det_2 target signature (1,3)** Lorentzian, `n(delta)` on the **forward light cone** (`det_2(delta o delta)==0`, `x0=(1/2)||delta||^2>=0`), `image(B)==pi_u(V_0)`. The bare trace Gram **diag(2,2,2,2)=(4,0)** Euclidean (compact OP^2 Fubini-Study metric) is reported as the **diagnostic FOIL, NEVER the verdict**.
- **VALD-02 (clause c):** anchors **Stab_{E6}(E11)=61, Stab_{V0}=45=Spin(9,1)** reproduced FIRST; residual structure group = exact nullspace over QQ = **dim 21 = so(3,1)[6] (+) so(6)[15]**; the residual action on the C_u 4-space spans **dim 6 == so(3,1)** (kills det_2; **Killing signature (3,3)**); the 4-space is the canonical C_u-projector eigenspace (eigvals {1:4, 0:12}); **so(3,1) FORCED** by (E_11,u). The so(6) acts trivially on spacetime (internal sector).
- **VERDICT: Phase A SURVIVES** (human-ratified by Bryan; orchestrator reproduced exit 0/ALL_PASS/24-of-24 exact over Q). Greenlight Phase 77, conjunctive with Phase 76 (A.5): BOTH must SURVIVE to greenlight Phase B.

## Task Commits

Each task was committed atomically:

1. **Tasks 1-3 (CALC-01 + CALC-02 + VALD-02 driver)** - `95226e5b` (compute) -- the three clauses co-locate in `code/cartan_phaseA_coframe.py` per the plan's `<files>` spec; ALL_PASS, exit 0, 24/24 checks PASS exact over Q.
2. **Task 4 (verdict derivation)** - `12737f81` (derive) -- `derivations/75-coframe-reduction.tex` with all three results + the decisive SURVIVES verdict + every forbidden proxy explicitly rejected.

_The blocking human-verify gate (Task 4) was ratified by Bryan ("approved") after the orchestrator independently re-ran the driver._

## Files Created/Modified

- `code/cartan_phaseA_coframe.py` - The exact-over-Q SymPy driver. Reuses the warm engines (bulk_geometry_verification, embedding_under_E_verification, ring_lemma_verification, orbit_dimension_gate import-only helpers); source guard active; `_report` harness prints each decisive integer/signature + an OVERALL verdict line. Runs `python3 -u`, exit 0 iff SURVIVES.
- `derivations/75-coframe-reduction.tex` - The Phase A verdict derivation (ASSERT_CONVENTION header mirroring 52-kkt; the three clauses; the soldering-vs-trace-form design point with both readings; the forced residual-group analysis; the boxed SURVIVES verdict; the 4 forbidden-proxy rejections).

## Next Phase Readiness

- **Phase 77 (Phase B -- full Cartan curvature)** is greenlit for the coframe side: a 4-dim Lorentzian (1,3) coframe `e=pi_u(dE)` carrying a FORCED SO(3,1) structure group is now established exactly over Q. The omega connection (Lorentz Spin(3,1) block of the ambient Spin(9,1)) and the Cartan/MM connection A=omega(+)e have a well-defined 4d target.
- **CONJUNCTIVE GATE:** Phase 77 greenlight requires BOTH Phase 75 (this, SURVIVES) AND Phase 76 (A.5, Berry same-wall) to SURVIVE. Phase 76 must still be run/checked.
- The soldering-form-metric reading (verdict on the R^{3,1} target; trace-form (4,0) is the foil) is the binding convention for downstream curvature work: the spacetime metric is the soldered (1,3) Lorentzian form, NOT the intrinsic Euclidean OP^2 metric.

## Contract Coverage

- Claim IDs advanced: `claim-coframe-reduction` -> **passed** (all 3 clauses, human-ratified)
- Deliverable IDs produced: `deliv-phaseA` -> **passed** (derivations/75-coframe-reduction.tex)
- Acceptance test IDs run: `test-coframe-dim` -> **passed**; `test-coframe-signature` -> **passed**; `test-coframe-forced` -> **passed**
- Reference IDs surfaced: `ref-52-kkt` (read/compare/cite); `ref-52-uniqueness` (read/compare/cite); `ref-phase74` (read/use); `ref-sharpe` (cite); `ref-baez` (cite); `ref-mccrimmon` (cite) -- all completed
- Forbidden proxies rejected: `fp-arbitrary-reduction`, `fp-relabel-approx-4d`, `fp-float-decisive`, `fp-octonion-algebra` -> all **rejected**
- Decisive comparison verdicts: `test-coframe-dim` -> pass; `test-coframe-signature` -> pass; `test-coframe-forced` -> pass

## Equations Derived

**Eq. (75.1) -- CALC-01 image dimension:**

$$
\dim \pi_u\!\big(V_{1/2}(16)\big) = \mathrm{rank}_{\mathbb{Q}}(M) = 4,
\qquad \mathrm{survivors}=\{11,18,19,26\}=\mathbb{C}_u^{\,2}.
$$

**Eq. (75.2) -- CALC-02 soldering bilinear + target signature:**

$$
B(\delta,\delta') = (\delta\circ\delta')\big|_{V_0} : V_{1/2}\times V_{1/2}\to V_0\cong\mathbb{R}^{3,1},
\quad \mathrm{rank}_{\mathbb{Q}}(B)=4,
\quad \det{}_2 = x_0^2-x_1^2-x_2^2-x_3^2 \Rightarrow (1,3).
$$

**Eq. (75.3) -- null cone (forward light cone, not a degeneracy):**

$$
n(\delta)=B(\delta,\delta),\qquad \det{}_2\big(n(\delta)\big)\equiv 0,\qquad x_0=\tfrac12\|\delta\|^2\ge 0.
$$

**Eq. (75.4) -- the Euclidean trace-form FOIL (NOT the verdict):**

$$
\mathrm{Gram}_{ij}=\mathrm{Tr}(\delta_i\circ\delta_j)=\mathrm{diag}(2,2,2,2),\qquad \text{signature }(4,0)\ \text{[compact OP}^2\text{ Fubini--Study]}.
$$

**Eq. (75.5) -- VALD-02 residual structure group:**

$$
\dim(\text{residual}) = 21 = \underbrace{\mathfrak{so}(3,1)}_{6}\oplus\underbrace{\mathfrak{so}(6)}_{15},
\qquad \mathrm{sig}\,B_{\mathrm{Killing}}(\mathfrak{so}(3,1))=(3,3).
$$

## Validations Completed

- **EXACT over Q** on all decisive numbers (sympy rank/eigenvals/nullspace over QQ; never numpy/float) -- driver reruns deterministically, exit 0, ALL_PASS, 24/24, reproduced 3x (incl. orchestrator-independent).
- **V_0-limit consistency:** the SAME pi_u on V_0 gives dim 4 (52-kkt 10->4); the soldering bilinear B IS the OD3 map (rank-4-on-pi_u(V_0), 52-uniqueness); `image(B)==pi_u(V_0)` (solders to THE spacetime, not a look-alike).
- **Calibration anchors reproduced BEFORE the new count:** Stab_{E6}(E11)=61, Stab_{V0}=45=Spin(9,1) (Phase 74 VALD-01).
- **so(3,1) confirmed three ways:** dim 6 on the C_u 4-space; kills det_2 (A^T g + g A = 0); Killing signature (3,3) (matched to the 52-kkt boosts B_i=L_{sigma_i}, [B_i,B_j]=-eps_ijk J_k).
- **Both readings reported** (foil + verdict) -- the honest framing that defeats fp-relabel: V_{1/2} is NOT intrinsically Lorentzian; the coframe SOLDERS the canonical C_u 4-space onto R^{3,1}.
- **Source guard:** octonion_algebra absent on the decisive path (not in sys.modules; native exact primitives); orbit_dimension_gate __main__ NOT run (import-only helpers).

## Decisions & Deviations

**Decisions (all documented in the derivation):**
- The coframe pairing is the soldering-form metric (candidate b via candidate-c Peirce bilinear); the trace form is the Euclidean foil. (The single most important design point; resolves Q1 of the research.)
- VALD-02 reports the residual at dim 21 (not bare 6): the so(6) is the canonical internal sector (Phase 48), trivial on spacetime, NOT a frame-choice free parameter -- so SO(3,1) is FORCED.

**Deviations from plan:** None - plan executed exactly as written. One internal self-correction during development (not a plan deviation): an initial source-guard implementation flagged the documented `import det_3 as oa_det_3` sanctioned in-fence oracle as an offender; the guard was corrected to Phase-0 DERV-01 runtime semantics (octonion_algebra not in sys.modules + decisive primitives are native exact + only UNSANCTIONED shadowing imports are offenders). The physics results were unaffected (all three clauses passed in the pre-write probes and the final run identically).

## Issues Encountered

- One coordinate-basis subtlety caught by the self-critique checkpoint: the residual Lorentz block initially appeared NOT to satisfy `A^T G + G A = 0` against the orthonormal `G=diag(+1,-1,-1,-1)` -- because the engine's C_u 4-space is the raw {beta,gamma,p,q} basis, NOT the orthonormal Minkowski frame. Using the correct det_2 Gram in {beta,gamma,p,q} (`beta*gamma - p^2 - q^2`, eigenvalues {1/2,-1/2,-1,-1} = (1,3)) confirmed the block is exactly so(3,1). Resolved before the final driver; no impact on the verdict.

## User Setup Required

None - no external configuration required (all engines in-repo; Python 3.14.2 / SymPy 1.14.0).

---

_Phase: 75-phase-a-coframe-reduction-dealbreaker-the-kill-gate_
_Completed: 2026-06-02_
