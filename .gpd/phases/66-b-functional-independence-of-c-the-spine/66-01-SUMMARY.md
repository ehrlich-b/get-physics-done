---
phase: 66-b-functional-independence-of-c-the-spine
plan: 01
depth: complex
one-liner: "THE SPINE: by exact computation over Q on the actual non-associative h_3(O), c = Tr(X o Y) is FUNCTIONALLY INDEPENDENT of the six pointwise generators (rank 7, c INDEPENDENT) -- two independent routes (7x54 Jacobian rank + orbit-derivative separating direction) AGREE on the diagonal cell (7, exists)"
subsystem: [computation, validation]
tags: [invariant-theory, f4, albert-algebra, jacobian-criterion, exact-over-Q, functional-independence, reward-hacking-guarded]

requires:
  - phase: 64-65-65.1
    provides: "FROZEN exact-SymPy engine E (jordan, Tr, det_3, c, 7 invariants, 54-symbol layout); certified f_4 builder (52-dim) + exact_qq_rank + PAIR_POINTS + genericity gates; CANDIDATE_GRADS[0:7] = SPINE rows; ORBIT_DERIVED_TRDEG=10; r6==6/r7==7 preview"
provides:
  - "DEMONSTRATED (not asserted): c = Tr(X o Y) is FIELD-level functionally INDEPENDENT of {Tr X, Tr X^2, det X, Tr Y, Tr Y^2, det Y} on the actual h_3(O), exact over Q"
  - "SPINE_RANK = 7 (7x54 sub-Jacobian, MAX over 5 generic pairs, stable, exact_qq_rank over QQ); RING-02 decisive verdict"
  - "Two-route agreement on diagonal cell (7, exists): Route 1 (Jacobian rank 7) + Route 2 (orbit-derivative separating xi exists) -- reward-hacking guard satisfied"
  - "code/spine_independence.py: pre-registered, foreground-runnable exact-over-Q harness (exit 0, 29 PASS/0 FAIL, deterministic)"
affects: [67, 68, 69, paper-writing, milestone-v16.0-verdict]

methods:
  added: ["orbit-derivative separating-direction test (NEW Route 2): xi -> Tr((xi.X) o Y) over the 52 f_4 generators, computationally independent of the Jacobian rank", "two-route adjudicator (verdict only on diagonal agreement cell; off-diagonal => NO VERDICT + STOP)"]
  patterns: ["pre-registration of points + rank test + verdict map as CODE before any rank (defeats fp-force-positive)", "substitute-first then exact_qq_rank (54-var swell control)", "MAX over >=3 generic pairs + a fresh inline pair (rank lower-semicontinuity)"]

key-files:
  created: [code/spine_independence.py]
  modified: []

key-decisions:
  - "REUSED the FROZEN certified primitives (E.jordan/Tr/det_3, exact_qq_rank, CANDIDATE_GRADS[0:7], _f4_basis) verbatim; NEVER re-implemented det_3/jordan/the f_4 builder (fp-det3-port-slip avoided)"
  - "Pre-registered TEST_PAIRS (4 PAIR_POINTS + 1 fresh inline) + exact rank test + verdict map BEFORE any rank (fp-force-positive defeated)"
  - "Verdict reported ONLY on the diagonal two-route agreement cell; both off-diagonal cells force NO VERDICT + nonzero exit (reward-hacking guard)"
  - "Corrected consistency stated as rank 7 <= trdeg 10 (c is 1 of 4 mixed invariants); stale 'rank 7 = 54-orbit_dim = 7' Spin(8)-triality wording explicitly flagged superseded"

patterns-established:
  - "Pattern: two computationally-independent routes + a diagonal-only adjudicator as the reward-hacking guard for a binary algebraic verdict"
  - "Pattern: the NEGATIVE branch is fully wired and reachable (probe-tested) even when the positive fires -- an honest negative cannot be silently unavailable"

conventions:
  - "Arithmetic: exact over Q (SymPy Rational); ranks via exact_qq_rank = DomainMatrix-over-QQ; NEVER numpy.linalg.matrix_rank / SVD / float .rank()"
  - "F_4 = Aut(h_3(O)) (52-dim, NOT E_6); jordan = (1/2)(AB+BA); c = Tr(X o Y) bidegree (1,1), c(X,X) = Tr X^2; det_3 cross-term (x2 x1) x3 (Phase-64.1 fix)"
  - "Metric: Riemannian Fisher (pure algebra; field-theory / gauge / Fourier convention fields are N/A)"

plan_contract_ref: ".gpd/phases/66-b-functional-independence-of-c-the-spine/66-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-spine-verdict:
      status: passed
      summary: "The 7x54 Jacobian of {Tr X, Tr X^2, det X, Tr Y, Tr Y^2, det Y, c} has exact rank 7 over Q, STABLE across all 5 generic pairs (MAX = 7); the 6x54 pointwise baseline == 6 at every pair, the X=Y control == 6, and the three-exact-domain cross-check agrees at width 54. Verdict: rank 7 => c functionally INDEPENDENT of the six pointwise generators (positive pass)."
      linked_ids: [deliv-spine-harness, deliv-verdict, test-route1-rank, test-baseline-6, test-rank-stability, test-xeqy-control, test-exactness-crosscheck, ref-derksen-kemper, ref-ring-generating-set]
      evidence:
        - verifier: gpd-executor
          method: exact symbolic computation over Q (exact_qq_rank, MAX over 5 generic pairs)
          confidence: high
          claim_id: claim-spine-verdict
          deliverable_id: deliv-spine-harness
          acceptance_test_id: test-route1-rank
          reference_id: ref-derksen-kemper
          evidence_path: "code/spine_independence.py"
    claim-route2-separating:
      status: passed
      summary: "An f_4 direction xi exists along the F_4-orbit of X with nonzero derivative D_xi c = Tr((xi.X) o Y) != 0 (the length-52 separating vector s is NOT all zero; witness xi[0] at all 5 pairs, s[witness] in {-2,-1/2,-1,5/2,-1/2}) while every pointwise generator has zero derivative (X-pointwise by certified F_4-invariance; Y-pointwise since delta Y = 0). The explicit trace-form Tr((xi.X) o Y) equals the gradient-contraction grad_X(c).(M.v_x) for all 52 generators. This confirms c INDEPENDENT by a route computationally independent of the 7x54 rank."
      linked_ids: [deliv-spine-harness, deliv-separating-vector, test-route2-separating, test-pointwise-derivs-zero, ref-springer-veldkamp, ref-orbit-gate]
      evidence:
        - verifier: gpd-executor
          method: exact orbit-derivative pairing over Q (52 f_4 generators, all 5 generic pairs)
          confidence: high
          claim_id: claim-route2-separating
          deliverable_id: deliv-separating-vector
          acceptance_test_id: test-route2-separating
          reference_id: ref-springer-veldkamp
          evidence_path: "code/spine_independence.py"
    claim-two-route-agreement:
      status: passed
      summary: "A verdict was reported ONLY because Route 1 (rank 7) and Route 2 (separating xi exists) AGREE on the diagonal cell (7, exists). The adjudicator was probe-verified to emit NO VERDICT + STOP + nonzero exit on both off-diagonal cells ((7,none),(6,exists)) and the anomaly cell (rank not in {6,7}); the NEGATIVE branch is wired and reachable on the (6,none) cell."
      linked_ids: [deliv-spine-harness, deliv-verdict, test-adjudicator, test-negative-branch-wired, ref-ring-generating-set, ref-orbit-gate]
      evidence:
        - verifier: gpd-executor
          method: pre-registered 2x2 agreement table + off-diagonal/anomaly reachability probes
          confidence: high
          claim_id: claim-two-route-agreement
          deliverable_id: deliv-verdict
          acceptance_test_id: test-adjudicator
          reference_id: ref-ring-generating-set
          evidence_path: "code/spine_independence.py"
    claim-corrected-consistency:
      status: passed
      summary: "Asserted SPINE_RANK 7 <= ORBIT_DERIVED_TRDEG 10 (Phase-65 GATE: 54 - 44). rank 7 saturates the {6 pointwise + c} SUBSET (a 7x54 matrix maxes at 7) but does NOT saturate the full transcendence degree -- c is the FIRST of FOUR mixed joint invariants {c, Tr(X^2 o Y), Tr(X o Y^2), Tr(X^2 o Y^2)}. The stale roadmap criterion-5 wording 'rank 7 saturates trdeg = 54 - orbit_dim = 7' (the forbidden Spin(8)-triality back-of-envelope) is explicitly flagged superseded and NOT used."
      linked_ids: [deliv-spine-harness, deliv-consistency-note, test-consistency-7-le-10, ref-phase65-summary, ref-phase651-summary]
      evidence:
        - verifier: gpd-executor
          method: exact assertion SPINE_RANK <= ORBIT_DERIVED_TRDEG + explicit stale-wording flag
          confidence: high
          claim_id: claim-corrected-consistency
          deliverable_id: deliv-consistency-note
          acceptance_test_id: test-consistency-7-le-10
          reference_id: ref-phase65-summary
          evidence_path: "code/spine_independence.py"
  deliverables:
    deliv-spine-harness:
      status: passed
      path: code/spine_independence.py
      summary: "Pre-registered, foreground-runnable (python -u, chatty) exact-over-Q harness: pre-registration block, Route 1 (7x54 sub-Jacobian rank reusing CANDIDATE_GRADS[0:7]/prefix_rank), Route 2 (52-generator orbit-derivative separating-direction test, NEW), the two-route adjudicator, the NEGATIVE-branch constructor (conditional), and the corrected consistency assert. Runs end-to-end in ~14s foreground, 29 PASS/0 FAIL, exits 0 iff all checks pass AND a verdict on a diagonal cell. Deterministic (two runs identical)."
      linked_ids: [claim-spine-verdict, claim-route2-separating, claim-two-route-agreement, claim-corrected-consistency]
    deliv-verdict:
      status: passed
      path: code/spine_independence.py
      summary: "The decisive SPINE verdict printed by the harness: SPINE_RANK = 7, the 2x2 agreement table with observed cell (7, exists), and the verdict label 'c INDEPENDENT (positive pass)'."
      linked_ids: [claim-spine-verdict, claim-two-route-agreement]
    deliv-separating-vector:
      status: passed
      path: code/spine_independence.py
      summary: "The Route-2 separating vector s = (s_0..s_51) with s_i = Tr((xi_i.X) o Y), the witness index (first separating xi = index 0 at all pairs), reported exact over Q at each generic pair. Sample at P1xP2 (first 8 of 52): [-2, 6, 5/2, -11/2, 4, -3, 1, 2, ...]; #nonzero 49-51 of 52."
      linked_ids: [claim-route2-separating]
    deliv-negative-P:
      status: not_attempted
      path: code/spine_independence.py
      summary: "NOT APPLICABLE on this verdict (rank fired 7 / positive), so no explicit P was produced -- the explicit P = a*(Tr X)(Tr Y) is required ONLY on the rank-6 NEGATIVE branch. The constructor is nonetheless WIRED and reachable (probe-verified on the forced (6,none) path: it correctly finds c/m disagrees across pairs -- -3/10, 3/8, 1/10 -- so no single rational a exists, c is NOT a*(Tr X)(Tr Y), independently corroborating independence). On the positive branch it is a recorded no-op; foreshadowing printed: c(X,X) = Tr X^2 = 62 != (Tr X)^2 = 4 on the diagonal."
      linked_ids: [claim-two-route-agreement]
    deliv-consistency-note:
      status: passed
      path: code/spine_independence.py
      summary: "The corrected consistency statement printed by the harness: rank 7 <= 10 (NOT = 7); c is 1 of 4 mixed joint invariants; the stale roadmap criterion-5 'rank 7 = 54-orbit_dim = 7' (Spin(8)-triality back-of-envelope) explicitly flagged superseded and not used."
      linked_ids: [claim-corrected-consistency]
  acceptance_tests:
    test-route1-rank:
      status: passed
      summary: "Route 1: prefix_rank(7, pp) (7x54 sub-Jacobian, substitute-first then exact_qq_rank) == 7 at every pair; MAX over 5 generic pairs (P1xP2, P2xP3, P1xP3, P4xP5, fresh PFxPF) = SPINE_RANK = 7."
      linked_ids: [claim-spine-verdict, deliv-spine-harness, deliv-verdict, ref-derksen-kemper, ref-ring-generating-set]
    test-baseline-6:
      status: passed
      summary: "6x54 pointwise-sextet baseline prefix_rank(6, pp) == 6 at every generic pair (3 X-block + 3 Y-block, Garibaldi-Guralnick single-copy trdeg 3+3)."
      linked_ids: [claim-spine-verdict, deliv-spine-harness, ref-garibaldi-guralnick]
    test-rank-stability:
      status: passed
      summary: "prefix_rank(7, pp) is the SAME (== 7) at all 5 generic pairs (rank lower-semicontinuous; MAX is the generic value). No instability => no secretly non-generic pair."
      linked_ids: [claim-spine-verdict, deliv-spine-harness]
    test-xeqy-control:
      status: passed
      summary: "X=Y degeneracy control: prefix_rank(7, (P, P)) == 6 <= 6 (X=Y collapses c to Tr X^2 in R_pt). A control EXPECTED to fail to reach 7 -- NOT a counterexample, NOT a test point."
      linked_ids: [claim-spine-verdict, deliv-spine-harness]
    test-exactness-crosscheck:
      status: passed
      summary: "Three-exact-domain cross-check on the 7x54 at P1xP2: QQ-frac == QQ-int == ZZ-int == (7,7,7); the gate f_4-tangent cross-check agrees (44,44,44). Certifies exact_qq_rank is genuinely exact over Q at width 54, not a float proxy."
      linked_ids: [claim-spine-verdict, deliv-spine-harness, ref-orbit-gate]
    test-route2-separating:
      status: passed
      summary: "Route 2: the length-52 separating vector s = (Tr((xi_i.X) o Y))_i is NOT all zero at every generic pair (witness xi[0]; #nonzero 49-51 of 52). A separating direction exists => c varies along the F_4-orbit of X while the pointwise sextet is pinned. Checked at all 5 pairs including the fresh pair."
      linked_ids: [claim-route2-separating, deliv-spine-harness, deliv-separating-vector, ref-springer-veldkamp]
    test-pointwise-derivs-zero:
      status: passed
      summary: "All 6 pointwise directional derivatives == 0 over Q at the same generic points where c separates: X-pointwise {Tr X, Tr X^2, det X} via grad_X(f).(M.v_x) for all 52 generators at all 5 pairs (certified F_4-invariance witnessed); Y-pointwise {Tr Y, Tr Y^2, det Y} by their X-block gradient being the zero vector (delta Y = 0)."
      linked_ids: [claim-route2-separating, deliv-spine-harness, ref-orbit-gate]
    test-adjudicator:
      status: passed
      summary: "The two-route adjudicator reports a verdict ONLY on the diagonal cell (7, exists) => c INDEPENDENT. Probe-verified: both off-diagonal cells ((7,none),(6,exists)) print CONTRADICTION -- STOP and force nonzero (ok=False, verdict=None); the anomaly cell (rank not in {6,7}) STOPs. The 2x2 table is printed with the observed cell highlighted."
      linked_ids: [claim-two-route-agreement, deliv-spine-harness, deliv-verdict]
    test-negative-branch-wired:
      status: passed
      summary: "The NEGATIVE-branch constructor function EXISTS and is reachable on the (6,none) cell (probe-tested with trigger=True: it correctly detects no single rational a -- c/m = -3/10, 3/8, 1/10 disagree across usable pairs -- and STOPs honestly rather than fabricating a P). On the (7,exists) cell it is a recorded no-op with the c(X,X)=Tr X^2 != (Tr X)^2 foreshadowing. The bidegree argument (only (Tr X)(Tr Y) matches (1,1)) is stated in code."
      linked_ids: [claim-two-route-agreement, deliv-spine-harness, deliv-negative-P]
    test-consistency-7-le-10:
      status: passed
      summary: "Asserted SPINE_RANK 7 <= ORBIT_DERIVED_TRDEG 10 (= 54 - 44 from Phase 65). The corrected statement 'rank 7 <= trdeg 10 (c is 1 of 4 mixed invariants, does NOT saturate the full trdeg)' is printed; the stale '= 7 saturates trdeg' wording is explicitly flagged superseded and not used."
      linked_ids: [claim-corrected-consistency, deliv-spine-harness, deliv-consistency-note, ref-phase65-summary, ref-phase651-summary]
  references:
    ref-derksen-kemper:
      status: completed
      completed_actions: [read, use, cite]
      missing_actions: []
      summary: "Char-0 Jacobian criterion (trdeg = generic Jacobian rank) is Route 1's license: rank 7 <=> the 7 algebraically (hence functionally) independent <=> c not in the algebraic closure of R_pt. Cited in the harness docstring."
    ref-springer-veldkamp:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "F_4 = automorphisms preserving Tr and the cubic norm => the trace form Tr(X o Y) is F_4-equivariant and non-degenerate on the 26, exactly what makes xi -> Tr((xi.X) o Y) a nonzero linear functional for generic X,Y (Route 2's separating direction exists). Cited in the Route-2 docstring."
    ref-schafer:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Der(h_3(O)) = f_4; inner-derivation formula D_{a,b} = [L_a, L_b] grounds the f_4 builder reused (via E.inner_derivations / _f4_basis) for Route 2. Cited in the harness docstring."
    ref-garibaldi-guralnick:
      status: completed
      completed_actions: [cite, compare]
      missing_actions: []
      summary: "Single-copy F_4-on-26 orbit 24 / Spin(8) / trdeg 3 (reproduced by the certified gate) grounds the 6x54 baseline == 6 cross-check (3 X-block + 3 Y-block). The baseline == 6 at every pair confirms the comparison."
    ref-ring-generating-set:
      status: completed
      completed_actions: [read, use]
      missing_actions: []
      summary: "Reused VERBATIM: CANDIDATE_GRADS[0:7] (the 7 SPINE rows, fixed order), prefix_rank, candidate_jacobian_matrix_at, _f4_basis, ORBIT_DERIVED_TRDEG==10, NAMES, BIDEGREES. Sliced first-7 for Route 1; the check_f4_invariance 54-wide diagonal-contraction pattern reused for Route 2."
    ref-orbit-gate:
      status: completed
      completed_actions: [read, use]
      missing_actions: []
      summary: "Reused VERBATIM: exact_qq_rank (the anti-float guard), infinitesimal_action, _select_independent_basis, PAIR_POINTS, SINGLE_COPY_POINTS (X=Y control point), _pair_not_proportional, _is_genuinely_octonionic_integer, exact_rank_route_crosscheck (three-exact-domain witness)."
    ref-warm-engine:
      status: completed
      completed_actions: [read, use]
      missing_actions: []
      summary: "Reused VERBATIM: E.jordan, E.Tr, E.det_3 (Phase-64.1 corrected cross-term), E.X_from_symbols, E._flat27, E.inv_c/inv_Tr_X/inv_Tr_Y, E.xs/ys, E.octonionic_points, E.inner_derivations. The trace form Tr(A o B) = E.Tr(E.jordan(A,B)) is c when A=X, B=Y. NEVER touched octonion_algebra.py; NEVER re-froze det_3 (fp-det3-port-slip avoided)."
    ref-phase65-summary:
      status: completed
      completed_actions: [read, use]
      missing_actions: []
      summary: "The corrected trdeg target (10, not the naive Spin(8)-triality 7) is the basis of the consistency reframing rank 7 <= 10. ORBIT_DERIVED_TRDEG = 10 imported and used as the consistency cap."
    ref-phase651-summary:
      status: completed
      completed_actions: [read, compare]
      missing_actions: []
      summary: "States the r7==7 SPINE preview holds + the corrected-consistency wording verbatim. Phase 66 RE-DEMONSTRATES r7==7 here as its own pre-registered decisive result (Route 1 MAX + Route 2), and the r6==6/r7==7 corroboration matches the committed preview."
  forbidden_proxies:
    fp-assert-without-demonstration:
      status: rejected
      notes: "BOTH routes are COMPUTED exactly over Q on the actual h_3(O) (7x54 Jacobian rank + 52-generator orbit-derivative pairing); the adjudicator requires agreement. No appeal to 'it should be' / 'the preview says so'."
    fp-float-rank:
      status: rejected
      notes: "Every decisive rank is exact_qq_rank = DomainMatrix-over-QQ. The exact-only source guard scans this module and asserts 0 numpy float-rank calls and 0 octonion_algebra imports (verified live: regexes match real forbidden tokens). Three-exact-domain cross-check (QQ-frac==QQ-int==ZZ-int) certifies exactness at width 54."
    fp-non-generic-point:
      status: rejected
      notes: "Every TEST pair gated by _pair_not_proportional + distinct diagonals + genuinely octonionic; verdict is MAX over 4 PAIR_POINTS + 1 fresh inline pair. X=Y is run ONLY as a control (== 6 <= 6), never as a test point."
    fp-force-positive:
      status: rejected
      notes: "TEST_PAIRS + exact rank test + verdict map (7->INDEPENDENT, 6->DEPENDENT, else->STOP) are PRE-REGISTERED as CODE before any rank. The NEGATIVE branch is fully wired and reachable. No point/invariant was tuned; the verdict is whatever the pre-registered test yields."
    fp-rank-before-substitution:
      status: rejected
      notes: "The generic integer point is substituted into the cached (un-simplified) CANDIDATE_GRADS FIRST (via prefix_rank / candidate_jacobian_matrix_at), then exact_qq_rank. det_3 (deg 3) / 54-var swell controlled; each rank ~0.01s."
    fp-route2-false-positive:
      status: rejected
      notes: "The separating vector s is checked at ALL 5 generic pairs (not one); the 6 pointwise derivatives are confirmed 0 at the SAME points; the explicit trace-form Tr((xi.X) o Y) is cross-checked == the gradient-contraction grad_X(c).(M.v_x) for all 52 generators at every pair."
    fp-two-route-mismatch-ignored:
      status: rejected
      notes: "The adjudicator emits NO VERDICT + STOP + nonzero exit on both off-diagonal cells (probe-verified). A single route 'passing' is insufficient; the verdict required the diagonal agreement cell (7, exists)."
    fp-det3-port-slip:
      status: rejected
      notes: "det_3 / jordan / the f_4 builder / exact_qq_rank are REUSED from the certified engine (E.det_3 with the Phase-64.1 (x2 x1) x3 fix; orbit_dimension_gate.exact_qq_rank), never re-implemented."
    fp-stale-saturation:
      status: rejected
      notes: "Consistency stated as rank 7 <= 10 (c is 1 of 4 mixed invariants, does NOT saturate). The stale 'rank 7 = 54-orbit_dim = 7' Spin(8)-triality back-of-envelope is explicitly flagged superseded and NOT used."
  uncertainty_markers:
    weakest_anchors:
      - "Genericity is empirical (chosen TEST_PAIRS), not a proven Zariski-open statement; a pathological common non-generic locus across all chosen points is not formally excluded -- only made very unlikely by MAX over 4 gated-generic PAIR_POINTS + the explicit X=Y degeneracy control + a fresh-pair re-confirmation."
      - "Route 2's computational independence from Route 1: they are linked by the trdeg = 54 - orbit_dim duality and share the certified f_4 basis + engine (a builder bug would fail both -- mitigated by the upstream GATE certification and the r6==6 control). They remain computationally distinct questions (full-gradient rank vs trace-form pairing of orbit tangents)."
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations:
      - "prefix_rank(6,.) != 6 at a generic point would mean an engine/builder bug -- did NOT occur (==6 at all 5 pairs)."
      - "prefix_rank(7,.) differing across generic points would mean a secretly non-generic pair -- did NOT occur (==7 at all 5 pairs, stable)."
      - "Route-2 s identically 0 at a generic pair while Route 1 says 7 (off-diagonal) would mean NO VERDICT -- did NOT occur (s nonzero at all 5 pairs, witness xi[0])."
      - "Any nonzero D_M f for a pointwise generator along an orbit tangent would mean a port/basis bug -- did NOT occur (all 6 pointwise derivs == 0)."

comparison_verdicts:
  - subject_id: test-route1-rank
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-derksen-kemper
    comparison_kind: benchmark
    metric: jacobian_rank
    threshold: "rank in {7,6}; MAX over >=3 generic pairs + fresh"
    verdict: pass
    recommended_action: "Report SPINE_RANK = 7 => c INDEPENDENT (Derksen-Kemper char-0 criterion)."
    notes: "The 7x54 sub-Jacobian rank == 7 (exact_qq_rank over QQ), STABLE across all 5 generic pairs (MAX = 7). By the Derksen-Kemper char-0 Jacobian criterion, trdeg = generic rank = 7 => the 7 invariants are algebraically independent => c not in the algebraic closure of R_pt."
  - subject_id: test-exactness-crosscheck
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-orbit-gate
    comparison_kind: cross_method
    metric: exact_rank_three_domains
    threshold: "QQ-frac == QQ-int == ZZ-int"
    verdict: pass
    recommended_action: "Trust SPINE_RANK as exact over Q at width 54 (not a float proxy)."
    notes: "Three independent exact domains on the 7x54 at P1xP2 agree: QQ-frac == QQ-int == ZZ-int == (7,7,7); the gate f_4-tangent cross-check agrees (44,44,44). Certifies exact_qq_rank is genuinely exact over Q at width 54 (fp-float-rank rejected)."
  - subject_id: claim-spine-verdict
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-garibaldi-guralnick
    comparison_kind: baseline
    metric: pointwise_baseline_rank
    threshold: "6x54 baseline == 6 (3 X-block + 3 Y-block)"
    verdict: pass
    recommended_action: "Accept the 6x54 baseline as the certified pointwise-sextet anchor underpinning the SPINE rank."
    notes: "The 6x54 pointwise-sextet baseline == 6 at every generic pair, reproducing the Garibaldi-Guralnick single-copy F_4-on-26 trdeg-3 anchor (3 X-block + 3 Y-block). This grounds that adding c bumps 6 -> 7 (c independent), not a baseline artifact."
  - subject_id: claim-two-route-agreement
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-ring-generating-set
    comparison_kind: cross_method
    metric: agreement_cell
    threshold: "diagonal cell (7,exists) or (6,none)"
    verdict: pass
    recommended_action: "Report the verdict c INDEPENDENT; proceed to Phases 67/68 on the corrected trdeg-10 generating set."
    notes: "Route 1 (7x54 Jacobian rank = 7) and Route 2 (orbit-derivative separating xi exists) AGREE on the diagonal cell (7, exists). Off-diagonal cells were probe-verified to force NO VERDICT + STOP. This is the reward-hacking guard satisfied."
  - subject_id: claim-corrected-consistency
    subject_kind: claim
    subject_role: supporting
    reference_id: ref-phase65-summary
    comparison_kind: baseline
    metric: rank_vs_trdeg
    threshold: "SPINE_RANK <= 10"
    verdict: pass
    recommended_action: "Use rank 7 <= 10 (c is 1 of 4 mixed invariants); never the stale '= 7 saturates trdeg'."
    notes: "SPINE_RANK 7 <= ORBIT_DERIVED_TRDEG 10 (Phase-65 GATE pair orbit dim 44). Consistent; rank 7 saturates only the {6 pointwise + c} subset, not the full transcendence degree."

duration: 13 min
completed: 2026-05-26
---

# Phase 66 Plan 01: (b) Functional Independence of c -- THE SPINE Summary

**THE SPINE: by exact computation over Q on the actual non-associative h_3(O), the coupling c = Tr(X o Y) is FUNCTIONALLY INDEPENDENT of the six pointwise generators {Tr X, Tr X^2, det X, Tr Y, Tr Y^2, det Y} -- SPINE_RANK = 7 (positive pass), confirmed by two computationally-independent routes (7x54 Jacobian rank + orbit-derivative separating direction) agreeing on the diagonal cell (7, exists).**

## Performance

- **Duration:** 13 min
- **Started:** 2026-05-26T22:39:04Z
- **Completed:** 2026-05-26T22:51:51Z
- **Tasks:** 6 (all committed atomically)
- **Files modified:** 1 (code/spine_independence.py created)

## Key Results

- **SPINE VERDICT: c INDEPENDENT (positive pass).** `c = Tr(X o Y)` is FIELD-level functionally (= algebraically, char 0) independent of the pointwise sextet on the actual h_3(O). This is RING-02, the single load-bearing chain-critical result of milestone v16.0: "the complete third-person single-frame record does not determine the coupling Phi."
- **Route 1 (Jacobian):** `SPINE_RANK = 7` = the exact rank over Q (exact_qq_rank, DomainMatrix-over-QQ) of the 7x54 sub-Jacobian of {Tr X, Tr X^2, det X, Tr Y, Tr Y^2, det Y, c}, **STABLE** (== 7) across all 5 generic pairs (MAX). Baseline 6x54 == 6 at every pair; X=Y control == 6; three-exact-domain cross-check (7,7,7) + gate f_4-tangent (44,44,44) at width 54.
- **Route 2 (orbit-derivative, NEW, independent of the rank):** a separating f_4 direction xi EXISTS at every generic pair -- the length-52 vector `s = (Tr((xi_i.X) o Y))_i` is NOT all zero (witness xi[0]; #nonzero 49-51 of 52; s[witness] in {-2, -1/2, -1, 5/2, -1/2}) while all 6 pointwise directional derivatives along orbit tangents are exactly 0. The explicit trace-form == the gradient-contraction for all 52 generators at all 5 pairs.
- **Two-route agreement:** verdict reported ONLY on the diagonal cell **(7, exists)**; both off-diagonal cells and the anomaly cell were probe-verified to force NO VERDICT + STOP + nonzero exit (the reward-hacking guard).
- **Corrected consistency:** `rank 7 <= ORBIT_DERIVED_TRDEG 10` (c is 1 of 4 mixed joint invariants; does NOT saturate the full trdeg). The stale roadmap criterion-5 wording "rank 7 = 54 - orbit_dim = 7" (Spin(8)-triality back-of-envelope) is explicitly flagged superseded and NOT used.
- **Honest-negative discipline:** the NEGATIVE branch (rank 6 => explicit P = a*(Tr X)(Tr Y)) is fully wired and reachable (probe-tested). On the rank-7 positive branch it is a recorded no-op, with the foreshadowing `c(X,X) = Tr X^2 = 62 != (Tr X)^2 = 4` on the diagonal. (The probe of the forced-active path independently corroborates independence: c/m takes three distinct values -3/10, 3/8, 1/10 across generic pairs, so c is NOT a*(Tr X)(Tr Y) for any rational a.)

## SCOPE (read carefully)

**FIELD-level functional independence of c ONLY.** This establishes c is not in the algebraic closure of R_pt (c functionally independent of the six pointwise generators). It is NOT:
- ring generation / Hilbert series / Krull / minimal generators (= Phase 68);
- the degree-2 uniqueness Sym^2 branching (= Phase 67).

## Task Commits

Each task was committed atomically:

1. **Task 1: pre-registration block** - `d43a0409` (compute) -- frozen TEST_PAIRS (4 PAIR_POINTS + 1 fresh inline) + exact rank test + verdict map (7/6/else) + ORBIT_DERIVED_TRDEG==10, BEFORE any rank.
2. **Task 2: Route 1 7x54 sub-Jacobian** - `d12cf8ef` (compute) -- SPINE_RANK=7 stable; baseline 6; X=Y ctrl 6; three-domain exact.
3. **Task 3: Route 2 orbit-derivative** - `968d33e5` (compute) -- ROUTE2_VERDICT=exists; witness xi; 6 pointwise derivs 0; independent of rank.
4. **Task 4: two-route adjudicator + consistency** - `ffbe7e54` (compute) -- verdict only on diagonal; off-diag=>STOP; 7<=10; r6/r7 corroboration.
5. **Task 5: NEGATIVE-branch constructor** - `bba9f86e` (compute) -- wired+reachable; no-op on rank 7 with c(X,X)!=(Tr X)^2 foreshadow; honest STOP if forced.
6. **Task 6: assemble main() + exact-only guard + fresh-pair reconfirm** - `a6cab69b` (compute) -- exit-0-iff-all-pass; 29 PASS/0 FAIL; deterministic.

**Plan metadata:** (this SUMMARY commit)

## Files Created/Modified

- `code/spine_independence.py` (1110 lines) - the pre-registered, foreground-runnable exact-over-Q SPINE harness: Route 1 (7x54 rank), Route 2 (separating direction), the two-route adjudicator, the NEGATIVE constructor, the corrected consistency, the exact-only guard, the fresh-pair re-confirmation. Run: `python -u code/spine_independence.py` (exit 0, ~14s, 29 PASS/0 FAIL).

## Equations / Quantities

**SPINE verdict (Route 1, Derksen-Kemper char-0 Jacobian criterion):**

$$
\operatorname{rank}_{\mathbb{Q}}\left[\frac{\partial f_i}{\partial z_j}\right]_{7\times 54} = 7 \;\Longleftrightarrow\; \{\operatorname{Tr}X,\operatorname{Tr}X^2,\det X,\operatorname{Tr}Y,\operatorname{Tr}Y^2,\det Y, c\}\ \text{algebraically independent} \;\Longleftrightarrow\; c\notin \overline{R_{\mathrm{pt}}}
$$

**Route 2 (orbit-derivative separating direction):** along the F_4-orbit of X (Y fixed),

$$
D_\xi c = \operatorname{Tr}\big((\xi\cdot X)\circ Y\big)\neq 0\ \text{for some}\ \xi\in\mathfrak{f}_4,\qquad D_\xi f = 0\ \forall f\in\{\operatorname{Tr}X,\operatorname{Tr}X^2,\det X,\operatorname{Tr}Y,\operatorname{Tr}Y^2,\det Y\}
$$

so c varies on the orbit while the pointwise sextet is pinned => c functionally independent.

**Corrected consistency:** $\operatorname{SPINE\_RANK} = 7 \le \operatorname{ORBIT\_DERIVED\_TRDEG} = 54 - 44 = 10$ (c is the first of four mixed joint invariants).

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
| --- | --- | --- | --- | --- | --- |
| SPINE Jacobian rank | SPINE_RANK | 7 | exact (integer over Q) | exact_qq_rank, MAX over 5 generic pairs | generic point-pairs |
| Pointwise baseline rank | r6 | 6 | exact (integer over Q) | prefix_rank(6,.), all 5 pairs | generic point-pairs |
| X=Y control rank | -- | 6 | exact (integer over Q) | prefix_rank(7,(P,P)) | diagonal (degenerate) |
| Route-2 separating-vector nonzeros | #nonzero(s) | 49-51 of 52 | exact (rationals over Q) | Tr((xi_i.X) o Y), all 5 pairs | generic point-pairs |
| Orbit-derived trdeg (consistency cap) | trdeg | 10 | exact (Phase-65 CERTIFIED) | 54 - 44 (pair orbit dim) | -- |

All values are EXACT over Q (no tolerance, no rounding); "nonzero" means != 0 as a rational. The only residual uncertainty is the empirical (not Zariski-proven) genericity of the chosen points -- mitigated by MAX over 4 PAIR_POINTS + a fresh pair + the X=Y degeneracy control (see uncertainty_markers).

## Validations Completed

- **6x54 baseline == 6** at all 5 pairs (Garibaldi-Guralnick single-copy 3+3 anchor reproduced).
- **Rank stability:** prefix_rank(7,.) == 7 at all 5 generic pairs (lower-semicontinuity; no secretly non-generic pair).
- **X=Y degeneracy control == 6** (confirms X=Y collapses c to Tr X^2; excluded as a test point).
- **Three-exact-domain cross-check** (QQ-frac==QQ-int==ZZ-int) on the 7x54 at width 54: (7,7,7); gate f_4-tangent (44,44,44) -- exact_qq_rank exact, not a float proxy.
- **Route-2 two forms agree:** explicit Tr((xi.X) o Y) == gradient-contraction grad_X(c).(M.v_x) for all 52 generators at all 5 pairs.
- **6 pointwise derivatives == 0** along all orbit tangents at the same points where c separates.
- **Fresh-pair re-confirmation:** both routes re-confirm (rank 7 + separating xi) at a fresh inline pair NOT in PAIR_POINTS.
- **r6==6 / r7==7 corroboration** matches the committed Phase-65.1 preview.
- **Exact-only source guard** PASS (0 float-rank calls, 0 octonion_algebra imports on the decisive path; guard verified live).
- **Determinism:** two independent runs produce identical decisive lines.

## Decisions Made

- REUSED the FROZEN certified primitives verbatim (E.jordan/Tr/det_3, exact_qq_rank, CANDIDATE_GRADS[0:7], _f4_basis); never re-implemented the engine (fp-det3-port-slip avoided).
- Pre-registered points + rank test + verdict map as CODE before any rank (fp-force-positive defeated).
- Verdict reported ONLY on the diagonal two-route agreement cell (reward-hacking guard).
- Corrected consistency stated as rank 7 <= 10 (not the stale = 7).

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Code Robustness] NEGATIVE constructor pair-scan widened to all TEST_PAIRS**

- **Found during:** Task 5 (NEGATIVE-branch constructor reachability probe)
- **Issue:** The constructor originally scanned only the first 3 TEST_PAIRS for the `a` solve; two of those (P1xP2, P2xP3) have Tr X = 0 or Tr Y = 0 (so m = (Tr X)(Tr Y) = 0, unusable), leaving only 1 usable pair -- below the >= 2 needed for the over-determined consistency check.
- **Fix:** Scan ALL TEST_PAIRS for usable pairs (m != 0). The forced-active probe now collects 3 usable pairs (P1xP3, P4xP5, PFxPF) and correctly reports the a's disagree (-3/10, 3/8, 1/10) => no single rational a => honest STOP (c is NOT a*(Tr X)(Tr Y)).
- **Files modified:** code/spine_independence.py
- **Verification:** Probe with trigger=True collects 3 usable pairs and STOPs honestly; the decisive run (no-op) still exits 0 with 29 PASS/0 FAIL.
- **Committed in:** `bba9f86e` (Task 5 commit)

---

**Total deviations:** 1 auto-fixed (1 code robustness). This is correctness-only (the NEGATIVE branch is a no-op on the actual rank-7 verdict; the fix ensures the branch would behave correctly IF ever forced). No scope creep.

## Issues Encountered

None. All 6 tasks executed exactly as planned; both routes computed cleanly on the first decisive run; the verdict (rank 7, c INDEPENDENT) matches the pre-registered Phase-65.1 r7==7 preview, RE-DEMONSTRATED here by both routes as this phase's own decisive result.

## Open Questions

- None material for the SPINE. The verdict is decisive and reward-hacking-guarded. Downstream: Phase 67 (c the unique degree-2 coupling generator?) and Phase 68 (ring generation / Hilbert series on the corrected trdeg-10 set) build on this FIELD-level independence result.

## Cross-Phase Dependencies

### Results This Phase Provides To Later Phases

| Result | Used By Phase | How |
| --- | --- | --- |
| c functionally INDEPENDENT of R_pt (SPINE_RANK=7) | Phase 67, 68, milestone verdict | The decisive (b) result; grounds "single-frame record does not determine Phi". Phase 67 (degree-2 uniqueness) and Phase 68 (ring generation) build on it. |
| code/spine_independence.py harness | verification, paper-writing | Reproducible exact-over-Q demonstration of the SPINE; the deliverable for RING-02. |

### Results This Phase Consumed From Earlier Phases

| Result | From Phase | Verified Consistent |
| --- | --- | --- |
| FROZEN engine E (jordan, Tr, det_3, c, 7 invariants, 54-symbol layout) | Phase 64/64.1 | Yes -- ASSERT_CONVENTION lines match; det_3 (x2 x1) x3 reused, never re-froze |
| Certified f_4 builder (52-dim) + exact_qq_rank + PAIR_POINTS + genericity gates | Phase 65 | Yes -- baseline==6 (single-copy anchor) + f_4-tangent (44,44,44) cross-check confirm |
| ORBIT_DERIVED_TRDEG = 10; r6==6/r7==7 preview | Phase 65/65.1 | Yes -- consistency 7<=10 asserted; r6==6/r7==7 corroboration matches |

### Convention Changes

| Convention | Previous | This Phase | Reason |
| --- | --- | --- | --- |
| None -- all conventions preserved | | | All inherited verbatim from the frozen engine + certified gate |

## Self-Check: PASSED

- Created files exist on disk: `code/spine_independence.py` (1110 lines), `66-01-SUMMARY.md`.
- All 6 task commits present: d43a0409, d12cf8ef, 968d33e5, ffbe7e54, bba9f86e, a6cab69b.
- Harness reproduces: `python -u code/spine_independence.py` exits 0, prints "SPINE VERDICT: c INDEPENDENT (positive pass)" + "OVERALL: CLEAN PASS".
- Convention consistency: ASSERT_CONVENTION line matches the frozen engine + certified gate (jordan 1/2, det_3 (x2 x1) x3, c=Tr(X o Y), f4 dim 52, exact-over-Q, exact_qq_rank).
- Contract coverage: 4/4 claims, 5/5 deliverables, 10/10 acceptance tests, 9/9 references, 9/9 forbidden proxies, 5 comparison_verdicts -- `gpd validate summary-contract` => VALID.

## Validation: PASSED

- **Exactness:** every decisive rank is exact_qq_rank (DomainMatrix-over-QQ); SPINE_RANK is a definite Python int == 7 in {6,7} (no tolerance, no rounding); three-exact-domain cross-check (7,7,7)+(44,44,44) at width 54.
- **Math-phys domain check:** the decisive invariant (Jacobian rank) is integer-valued and definite; consistency 7 <= 10 (integer bound) holds; the orbit-derivative separating vector entries are exact rationals (nonzero means != 0 as a rational).
- **Reward-hacking guard:** verdict only on the diagonal two-route agreement cell; off-diagonal/anomaly cells probe-verified to force NO VERDICT + nonzero exit.
- **Determinism / reproducibility:** two independent runs produce identical decisive lines (no random seeds; pure exact-over-Q algebra; SymPy 1.14.0, NumPy 2.4.3, Python 3.14.2).

---

_Phase: 66-b-functional-independence-of-c-the-spine_
_Completed: 2026-05-26_
