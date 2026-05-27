---
phase: 68-a-generating-set-completeness-certificate
plan: 01
depth: complex
one-liner: "Computed the bigraded Molien series H(s,t) of R[27+27]^{F_4} exactly (no Sage) to total degree <=6 via pure-SymPy Molien-Weyl iterated residue; passed both calibration gates (single-copy 1/((1-s)(1-s^2)(1-s^3)); d_(1,1)=2) and confirmed every bidegree a+b<=4 (incl (2,2)) by an independent exact-over-Q f_4-kernel route -- Krull=10, d_(2,2)=9"

subsystem: [computation, formalism]
tags: [invariant-theory, molien-weyl, hilbert-series, F4, exceptional-group, jordan-algebra, plethystics, exact-arithmetic, two-route]

requires:
  - phase: 65-orbit-dimension-gate
    provides: "Krull dim target 10 (orbit_dim 44 => 54-44=10); inner_derivations() 52-gen f_4 basis; exact_qq_rank"
  - phase: 65.1-corrected-generating-set
    provides: "the 10-candidate trdeg-10 set with bidegrees (6 pointwise + c(1,1) + (2,1)+(1,2)+(2,2)); PAIR_POINTS"
  - phase: 67-c-degree-2-uniqueness
    provides: "bidegree-(1,1) trivial mult = 2 (the d_(1,1) gate G2); Route B Leibniz-lift f_4-kernel engine generalized here"
provides:
  - "Certified bigraded dimension table {d_(a,b): a+b<=6} of R[27+27]^{F_4} as exact non-negative integers"
  - "Two-route (Molien-Weyl + exact-over-Q f_4-kernel) agreement at every bidegree a+b<=4 including (2,2)"
  - "d_(2,2) = 9 (the key Plan 02 diagnostic bidegree for the '(2,2) generator or product?' question)"
  - "Krull dimension read-off = 10 (consistent with Phase 65); H(s,t)=H(t,s) symmetry confirmed"
affects: [68-02, ring-generation, completeness-certificate, minimality]

methods:
  added: ["pure-SymPy Molien-Weyl iterated symbolic residue (z=w^2 doubling, w^0-fiber convolution pruned to numerator support)", "generalized Route-B exact f_4-kernel dim via sparse DomainMatrix-over-QQ rank on the Sym^a(27)(x)Sym^b(27) Lie-derivative operator"]
  patterns: ["calibration-gated normalization (G1 single-copy + G2 (1,1)) BEFORE trusting two-copy coefficients", "two-route exact agreement as the reward-hacking tripwire", "sparse dict-of-dicts QQ rank to scale the exact kernel route to 142,884-dim (2,2)"]

key-files:
  created: ["code/molien_bigraded.py"]
  modified: []

key-decisions:
  - "The 26's 24 nonzero weights are the LONG roots (+/-e_i, (+/-1/2)^4, norm^2=1), NOT the short roots -- pinned by the G1/G2 calibration gates (short roots give d_(1,1)=3 and fail G2; long roots give d_(1,1)=2). This resolves the documented short/long label ambiguity (RESEARCH Caveat 1)."
  - "Single-copy gate target corrected to [1,1,2,3,4,5,7] (the PLAN frontmatter / RESEARCH wrote the s^6 entry as 6; the true value is 7 = #partitions of 6 into parts <=3, verified by sympy.series AND direct partition count). Plan typo, not a normalization issue."
  - "(2,2) exact f_4-kernel computed in full (~36s) via sparse DomainMatrix rank -- the anticipated watchdog fallback to Molien-only was NOT needed; the two-route anchor covers all of a+b<=4."
  - "Molien CT computed by the symbolic iterated residue (w^0-fiber exponent convolution pruned to the numerator support), NOT a numerical torus grid (fp-numerical-grid)."

patterns-established:
  - "Pattern 1: calibration-gate-first Molien-Weyl -- never report a two-copy Hilbert coefficient until the single-copy specialization AND the (1,1) anchor both pass (the normalization has competing literature conventions; the gates are the only thing pinning it)."
  - "Pattern 2: sparse-QQ exact rank for large symmetric-power kernels -- DomainMatrix(dict-of-dicts,(rows,cols),QQ).rank() scales the exact-over-Q f_4-kernel route to 7.34M-row x 142,884-col without dense materialization or any float."

conventions:
  - "jordan(A,B) = (1/2)(AB+BA); c = Tr(X o Y); c(X,X)=Tr(X^2) (NOT (Tr X)^2)"
  - "27 = 1 (+) 26; 27-weight multiset = {0^3} U {24 LONG roots}"
  - "F_4: 48 roots = 24 short (norm^2=2, perms(+/-1,+/-1,0,0)) + 24 long (norm^2=1, +/-e_i and (+/-1/2)^4); |W(F_4)|=1152"
  - "arithmetic exact over Q; ranks via exact DomainMatrix-over-QQ; NEVER float64/numpy rank on the decisive path"
  - "Krull target = 10 (Phase 65); the superseded 7 is FORBIDDEN"
  - "metric = (+,+,...,+) Riemannian Fisher (pure algebra; no field theory/gauge/Fourier)"

plan_contract_ref: ".gpd/phases/68-a-generating-set-completeness-certificate/68-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-molien-series:
      status: passed
      summary: "H(s,t) computed exactly for all a+b<=6 by the pure-SymPy Molien-Weyl iterated symbolic residue (27-weight multiset {0^3} U {24 long roots}, Weyl-measure numerator prod_{48 roots}(1-w^(2a)), 1/|W| with |W|=1152) as a truncated bivariate polynomial of exact non-negative integers; CT_w=1152 reproduced symbolically."
      linked_ids: [deliv-molien-code, deliv-dim-table, test-integer-coeffs, test-weyl-ct, ref-derksen-kemper, ref-hanany, ref-single-copy]
      evidence:
        - verifier: gpd-executor
          method: "symbolic iterated residue + integer-coefficient assertion + Weyl-measure CT cross-check"
          confidence: high
          claim_id: claim-molien-series
          deliverable_id: deliv-molien-code
          acceptance_test_id: test-integer-coeffs
          reference_id: ref-derksen-kemper
          evidence_path: "code/molien_bigraded.py"
    claim-calibration-gates:
      status: passed
      summary: "Both mandatory gates pass BEFORE any two-copy coefficient is trusted: G1 H(s,0)=H(0,t)=[1,1,2,3,4,5,7]=1/((1-s)(1-s^2)(1-s^3)); G2 d_(1,1)=2 (Phase 67). G1 fired as designed and disambiguated the short/long weight label (long roots are the 26's weights)."
      linked_ids: [deliv-molien-code, deliv-dim-table, test-gate-singlecopy, test-gate-11, ref-single-copy, ref-frozen-degree2]
      evidence:
        - verifier: gpd-executor
          method: "t=0/s=0 specialization compared to the single-copy series; d_(1,1) compared to Phase-67 anchor"
          confidence: high
          claim_id: claim-calibration-gates
          deliverable_id: deliv-molien-code
          acceptance_test_id: test-gate-singlecopy
          reference_id: ref-single-copy
          evidence_path: "code/molien_bigraded.py"
    claim-tworoute-agreement:
      status: passed
      summary: "At EVERY feasible low bidegree (1,1),(2,0),(0,2),(2,1),(1,2) AND (2,2), the Molien coefficient equals the EXACT-over-Q f_4-kernel dim = dim Sym^a(27)(x)Sym^b(27) - rank_QQ(stacked Leibniz-lift operators) as identical integers: 2,2,2,4,4,9. The Leibniz-lift correctness guard fired (rho(M) annihilates c for 52/52; wrong M(x)M would give 0/52). (2,2) completed in full -- the watchdog fallback was not needed."
      linked_ids: [deliv-molien-code, deliv-f4kernel-table, test-tworoute, test-f4kernel-exact, ref-frozen-degree2, ref-frozen-orbit]
      evidence:
        - verifier: gpd-executor
          method: "cross-method: independent exact-over-Q f_4-kernel nullspace vs Molien-Weyl residue at 6 bidegrees"
          confidence: high
          claim_id: claim-tworoute-agreement
          deliverable_id: deliv-f4kernel-table
          acceptance_test_id: test-tworoute
          reference_id: ref-frozen-degree2
          evidence_path: "code/molien_bigraded.py"
    claim-krull-symmetry:
      status: passed
      summary: "H(s,t) is consistent with the prior-phase anchors: the Krull dimension is 10 (Phase 65, NOT the superseded 7) -- corroborated by the strictly-increasing, convex total-degree growth T_n=[1,2,6,14,29,56,106] and anchored on the exact Phase-65 orbit computation; and H(s,t)=H(t,s) (d_(a,b)=d_(b,a)) holds for all a+b<=6."
      linked_ids: [deliv-dim-table, deliv-molien-code, test-krull, test-symmetry, ref-frozen-orbit, ref-derksen-kemper]
      evidence:
        - verifier: gpd-executor
          method: "Krull read-off from total-degree growth + Phase-65 anchor; symmetry by coefficient comparison"
          confidence: high
          claim_id: claim-krull-symmetry
          deliverable_id: deliv-dim-table
          acceptance_test_id: test-symmetry
          reference_id: ref-frozen-orbit
          evidence_path: "code/molien_bigraded.py"
  deliverables:
    deliv-molien-code:
      status: passed
      path: code/molien_bigraded.py
      summary: "Pure-SymPy Molien-Weyl iterated-residue computation of H(s,t) to a+b<=6 with the z=w^2 doubling, both calibration gates, the generalized Route-B exact f_4-kernel cross-check at all feasible bidegrees, the Krull-pole-order and symmetry checks, the exact-only source guard, and the ASSERT_CONVENTION line. Exact over Q; no Sage; no float / no numerical grid on the decisive path. CLEAN PASS (exit 0)."
      linked_ids: [claim-molien-series, claim-calibration-gates, claim-tworoute-agreement, claim-krull-symmetry]
    deliv-dim-table:
      status: passed
      path: code/molien_bigraded.py
      summary: "The certified bigraded dimension table {d_(a,b): a+b<=6} emitted as exact integers (printed grid). d_(1,1)=2; single-copy row/col d_(a,0)=d_(0,a)=[1,1,2,3,4,5,7]; d_(2,2)=9. The decisive Plan 02 handoff."
      linked_ids: [claim-molien-series, claim-krull-symmetry]
    deliv-f4kernel-table:
      status: passed
      path: code/molien_bigraded.py
      summary: "Exact-over-Q f_4-kernel dims at the cross-checked bidegrees: (1,1)=2 (reproduces Phase 67's 729-727=2), (2,0)=2, (0,2)=2, (2,1)=4, (1,2)=4, and (2,2)=9 computed in FULL (142884 - 142875 = 9; the recorded Molien-only fallback was NOT needed)."
      linked_ids: [claim-tworoute-agreement]
  acceptance_tests:
    test-integer-coeffs:
      status: passed
      summary: "All d_(a,b), a+b<=6, are non-negative integers (exact SymPy Rational with denominator 1); no non-integer coefficient appeared."
      linked_ids: [claim-molien-series, deliv-molien-code, deliv-dim-table]
    test-weyl-ct:
      status: passed
      summary: "CT_w[prod_{48 roots}(1-w^(2a))] = 1152 = |W(F_4)| recomputed symbolically (165457-term Laurent product), confirming the all-48-roots numerator + 1/|W| normalization structure."
      linked_ids: [claim-molien-series, deliv-molien-code]
    test-gate-singlecopy:
      status: passed
      summary: "H(s,0)=H(0,t)=[1,1,2,3,4,5,7]=1/((1-s)(1-s^2)(1-s^3)) (the s^6 entry is 7, not the plan's 6 -- a plan typo; #partitions of 6 into parts<=3 = 7). Gate fired and pinned the long-root weight set."
      linked_ids: [claim-calibration-gates, deliv-molien-code, deliv-dim-table, ref-single-copy]
    test-gate-11:
      status: passed
      summary: "d_(1,1) read from H(s,t) = 2 = Phase-67 anchor (span{Tr(X)Tr(Y), c})."
      linked_ids: [claim-calibration-gates, deliv-molien-code, deliv-dim-table, ref-frozen-degree2]
    test-f4kernel-exact:
      status: passed
      summary: "Exact f_4-kernel dim computed at every feasible bidegree via exact rank over QQ (sparse DomainMatrix); Leibniz-lift correctness guard fires (rho(M)=M(x)I+I(x)M kills c for 52/52; M(x)M would be 0/52)."
      linked_ids: [claim-tworoute-agreement, deliv-molien-code, deliv-f4kernel-table, ref-frozen-degree2, ref-frozen-orbit]
    test-tworoute:
      status: passed
      summary: "Molien d_(a,b) == f_4-kernel d_(a,b) as IDENTICAL exact integers at all 6 cross-checked bidegrees (1,1)=2,(2,0)=2,(0,2)=2,(2,1)=4,(1,2)=4,(2,2)=9. No disagreement; the reward-hacking tripwire is satisfied."
      linked_ids: [claim-tworoute-agreement, deliv-dim-table, deliv-f4kernel-table]
    test-krull:
      status: passed
      summary: "Krull dimension = 10 (Phase 65; NOT 7). Series growth T_n=[1,2,6,14,29,56,106] is strictly increasing and convex (corroboration); the decisive value is the exact Phase-65 orbit_dim 44 => 54-44=10. (Hybrid check: degree-<=6 truncation cannot uniquely pin the pole order, so Phase 65 is the anchor.)"
      linked_ids: [claim-krull-symmetry, deliv-dim-table, ref-frozen-orbit]
    test-symmetry:
      status: passed
      summary: "d_(a,b) == d_(b,a) for all a+b<=6 (X<->Y diagonal-action symmetry); no asymmetry."
      linked_ids: [claim-krull-symmetry, deliv-dim-table]
  references:
    ref-derksen-kemper:
      status: completed
      completed_actions: [use, cite]
      missing_actions: []
      summary: "Molien-Weyl (Weyl-integration / constant-term) formula used as the integrand form (all-roots numerator, 1/|W| normalization); cited in the module docstring."
    ref-hanany:
      status: completed
      completed_actions: [read, use]
      missing_actions: []
      summary: "The Molien-Weyl + iterated-residue evaluation recipe followed in practice (the w^0-fiber constant-term extraction)."
    ref-single-copy:
      status: completed
      completed_actions: [use, compare, cite]
      missing_actions: []
      summary: "Single-copy series 1/((1-s)(1-s^2)(1-s^3)) used as the G1 calibration gate; H(s,0) compared coefficient-by-coefficient and matched [1,1,2,3,4,5,7]."
    ref-frozen-degree2:
      status: completed
      completed_actions: [use, compare]
      missing_actions: []
      summary: "Phase-67 (1,1)=2 used as the G2 gate; the Route-B Leibniz-lift f_4-kernel machinery generalized to all low bidegrees (the (1,1)=2 reproduced via 729-727=2)."
    ref-frozen-orbit:
      status: completed
      completed_actions: [use, compare]
      missing_actions: []
      summary: "Phase-65 52-generator f_4 basis (inner_derivations + _select_independent_basis) and exact rank reused for the kernel route; Krull target 10 confirmed against the series."
    ref-schwarz:
      status: completed
      completed_actions: [cite, avoid]
      missing_actions: []
      summary: "Schwarz (2-polarization fails generically in char 0) cited as the reason the Hilbert match (this series) -- not polarization -- is the completeness certificate; polarization was NOT assumed to generate (the certificate-assembly is Plan 02)."
    ref-blind:
      status: completed
      completed_actions: [cite, compare]
      missing_actions: []
      summary: "Blind 2011 (E_6 pair ring FREE on 4 dets) cited as the CONTRAST; the F_4 ring is strictly larger (contains c) and NOT free -- H(s,t) was NOT assumed to have a clean free-algebra denominator (the free series is used only as a labelled sanity comparison, not as H_true)."
  forbidden_proxies:
    fp-numerical-grid:
      status: rejected
      notes: "The Molien CT is the symbolic iterated residue (w^0-fiber exponent convolution); 0 numpy/mpmath imports on the decisive path (exact-only source guard asserts it)."
    fp-float-rank:
      status: rejected
      notes: "All kernel ranks via exact DomainMatrix-over-QQ rank; 0 numpy.linalg.matrix_rank / SVD tolerance (source guard asserts 0 float-rank calls)."
    fp-noninteger:
      status: rejected
      notes: "Every d_(a,b) asserted to be an exact non-negative integer (Rational with denominator 1); a non-integer would force a STOP. None occurred."
    fp-krull7:
      status: rejected
      notes: "Krull dimension reported as 10 (Phase 65 orbit_dim 44 => 54-44=10), NOT the superseded Spin(8)-triality 7."
    fp-skip-gate:
      status: rejected
      notes: "Both G1 and G2 are evaluated and must pass BEFORE any two-copy coefficient is trusted; the harness STOPs on a gate failure (G1 fired during development and forced the long-root fix before any two-copy number was reported)."
    fp-e6-free:
      status: rejected
      notes: "H(s,t) was NOT assumed to have a free-algebra product denominator; the free series prod 1/(1-s^a t^b) is printed only as a labelled sanity comparison, explicitly NOT as H_true (the F_4 ring is non-free)."
  uncertainty_markers:
    weakest_anchors:
      - "The exact Molien-Weyl normalization was validated structurally (CT=1152) and PINNED operationally by the G1/G2 gates, not proven a priori -- but both gates PASS and the two-route agreement at 6 bidegrees independently confirms the normalization, so this anchor is now strong."
      - "The (2,2) exact f_4-kernel was the flagged watchdog risk; it COMPLETED in full (~36s via sparse QQ rank), so the (2,2) coefficient now rests on BOTH routes, not Molien-only."
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations:
      - "RESOLVED: t=0 specialization initially gave d_(1,1)=3 and the wrong tensor multiplicities with the SHORT roots as the 26's weights -- the gate fired, the short/long label was corrected to LONG, and G1/G2 then passed. Reported honestly (NEGATIVE-RESULT-IS-SUCCESS at the gate level)."
      - "No two-route disagreement at any bidegree; Krull pole order consistent with 10; H(s,t)=H(t,s). All disconfirming tripwires are clear."

comparison_verdicts:
  - subject_id: claim-tworoute-agreement
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-frozen-degree2
    comparison_kind: cross_method
    metric: exact_integer_equality
    threshold: "identical integers at every feasible bidegree a+b<=4"
    verdict: pass
    recommended_action: "Hand the certified dimension table to Plan 02 for generating-set assembly + minimality certificate."
    notes: "Molien-Weyl vs exact-over-Q f_4-kernel agree as identical integers at (1,1)=2,(2,0)=2,(0,2)=2,(2,1)=4,(1,2)=4,(2,2)=9 (6/6, incl the heavy (2,2))."
  - subject_id: claim-calibration-gates
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-single-copy
    comparison_kind: benchmark
    metric: coefficient_equality
    threshold: "H(s,0)=H(0,t)=[1,1,2,3,4,5,7] through s^6"
    verdict: pass
    recommended_action: "Trust the two-copy coefficients (gate passed); proceed to Plan 02."
    notes: "Single-copy specialization matches 1/((1-s)(1-s^2)(1-s^3)). NB the s^6 entry is 7 (the plan/RESEARCH wrote 6 -- a typo; the true partition count is 7)."
  - subject_id: claim-calibration-gates
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-frozen-degree2
    comparison_kind: cross_method
    metric: exact_integer_equality
    threshold: "d_(1,1) == 2"
    verdict: pass
    recommended_action: "Trust the (1,1) Hilbert coefficient and the normalization."
    notes: "d_(1,1)=2 from Molien matches the Phase-67 exact f_4-kernel anchor (729-727=2)."
  - subject_id: claim-krull-symmetry
    subject_kind: claim
    subject_role: supporting
    reference_id: ref-frozen-orbit
    comparison_kind: prior_work
    metric: krull_dimension
    threshold: "== 10 (NOT 7)"
    verdict: pass
    recommended_action: "Use Krull=10 downstream; the degree-6 truncation corroborates via convex growth, Phase 65 is the decisive anchor."
    notes: "Hybrid: series growth (increasing+convex) is consistent with a high-dim ring; the exact value 10 is the Phase-65 orbit computation."

duration: 53min
completed: 2026-05-27
---

# Phase 68 Plan 01: (a) Generating-Set Completeness Certificate (SERIES half) Summary

**Computed the bigraded Molien series H(s,t) of R[27+27]^{F_4} exactly (no Sage) to total degree <=6 via a pure-SymPy Molien-Weyl iterated residue; passed both calibration gates and confirmed every bidegree a+b<=4 (including the heavy (2,2)) by an independent exact-over-Q f_4-kernel route — yielding the certified dimension table with d_(2,2)=9, Krull=10.**

## Status: COMPLETE — Task 4 human-verify checkpoint APPROVED (2026-05-27)

Tasks 1-3 are COMPLETE, verified, and committed (`5b53520d`). **Task 4 (`checkpoint:human-verify`, `gate="blocking"`) was APPROVED by the human** ("Approve & proceed") after the orchestrator independently re-ran `code/molien_bigraded.py` from a clean invocation and reproduced every decisive number (exit 0: CT=1152, G1=[1,1,2,3,4,5,7], G2 d_(1,1)=2, two-route agreement 6/6 incl (2,2)=9, Krull=10, symmetry). The certified bigraded dimension table is released as the decisive handoff to Plan 02. Post-approval cleanup: the stale ASSERT_CONVENTION / REP-DECOMP comments (which still described the rejected norm^2=2 weight choice) were reconciled to the norm^2=1 weights actually used; the harness re-ran CLEAN PASS (exit 0) after the comment fix.

## Performance

- **Duration:** ~53 min (most of it iterative performance engineering on two long symbolic runs + the gate-fired normalization fix)
- **Started:** 2026-05-27T15:03:12Z
- **Completed (Tasks 1-3):** 2026-05-27T15:56:38Z
- **Tasks:** 3 of 4 (Task 4 = blocking human-verify checkpoint, pending)
- **Files modified:** 1 (`code/molien_bigraded.py`)

## Key Results

- **Certified bigraded dimension table {d_(a,b): a+b<=6}** (exact non-negative integers):

  ```
    a\b |   0   1   2   3   4   5   6
    ------------------------------------
      0 |   1   1   2   3   4   5   7
      1 |   1   2   4   6   9  12   .
      2 |   2   4   9  14  22   .   .
      3 |   3   6  14  24   .   .   .
      4 |   4   9  22   .   .   .   .
      5 |   5  12   .   .   .   .   .
      6 |   7   .   .   .   .   .   .
  ```

- **Weyl-measure structural check:** CT_w[prod_{48 roots}(1-w^(2a))] = **1152 = |W(F_4)|** (recomputed symbolically).
- **G1 single-copy gate:** H(s,0) = H(0,t) = **[1,1,2,3,4,5,7]** = 1/((1-s)(1-s^2)(1-s^3)). PASS.
- **G2 (1,1) gate:** d_(1,1) = **2** (Phase 67 anchor). PASS.
- **Two-route agreement (the reward-hacking tripwire):** Molien == exact-over-Q f_4-kernel as IDENTICAL integers at all 6 feasible bidegrees:

  | bidegree | Molien | exact f_4-kernel | space dim | rank | status |
  |---|---|---|---|---|---|
  | (1,1) | 2 | 2 | 729 | 727 | PASS (reproduces Phase 67) |
  | (2,0) | 2 | 2 | 378 | 376 | PASS |
  | (0,2) | 2 | 2 | 378 | 376 | PASS |
  | (2,1) | 4 | 4 | 10206 | 10202 | PASS |
  | (1,2) | 4 | 4 | 10206 | 10202 | PASS |
  | (2,2) | 9 | 9 | 142884 | 142875 | PASS (computed in FULL; no fallback) |

- **Krull dimension = 10** (Phase 65, NOT the superseded 7); total-degree growth T_n = [1,2,6,14,29,56,106] (strictly increasing, convex).
- **Symmetry:** d_(a,b) = d_(b,a) for all a+b<=6. PASS.
- **d_(2,2) = 9** — the key diagnostic bidegree Plan 02 resolves ("(2,2) generator or product?").

## Task Commits

1. **Tasks 1-3 (engine + gates + two-route + Krull)** — `5b53520d` (compute)
   - Task 1: F_4 root/weight data, symbolic Weyl-measure CT=1152, Molien-Weyl iterated-residue H(s,t) with z=w^2 doubling.
   - Task 2: G1 single-copy gate, G2 (1,1)=2 gate, symmetry check, certified dimension table.
   - Task 3: generalized Route-B exact f_4-kernel cross-check at all feasible bidegrees + Krull read-off.

   _Note: Tasks 1-3 form one cohesive harness (`code/molien_bigraded.py`) that does not function in pieces, so they are committed as one working-state atomic unit per the checkpoint discipline (a non-functional partial commit would violate "each checkpoint = working state")._

**Task 4 (blocking human-verify checkpoint):** pending — no commit; execution returns to the orchestrator for human adjudication.

## Files Created/Modified

- `code/molien_bigraded.py` — the Molien-Weyl iterated-residue engine, both calibration gates, the generalized Route-B exact f_4-kernel cross-check, the Krull-pole-order and symmetry checks, the exact-only source guard. CLEAN PASS (exit 0), ~90s runtime, exact over Q.

## Equations Used

**Eq. (68.1)** — bigraded Molien-Weyl formula (Derksen-Kemper):
$$
H(s,t) = \frac{1}{|W|}\,\mathrm{CT}_w\!\left[\frac{\prod_{\alpha\in 48\text{ roots}}(1-w^{2\alpha})}{D_X(s,w)\,D_Y(t,w)}\right],\quad |W|=1152
$$

**Eq. (68.2)** — one-copy characteristic factor (27 = 1 (+) 26, the 26's nonzero weights = the 24 LONG roots):
$$
D(u,w) = (1-u)^3 \prod_{\mu\in 24\text{ long roots}}\!\left(1-u\,w^{2\mu}\right)
$$

**Eq. (68.3)** — generalized Route-B exact f_4-kernel dimension (the independent cross-check):
$$
d_{a,b} = \dim \mathrm{Sym}^a(27)\otimes\mathrm{Sym}^b(27) - \mathrm{rank}_{\mathbb{Q}}\big(\text{stacked } D_M,\ M\in f_4\big),\quad
D_M f = \sum_i (Mx)_i \partial_{x_i} f + \sum_i (My)_i \partial_{y_i} f
$$

## Validations Completed

- **Weyl-measure CT** = 1152 = |W(F_4)| (symbolic, 165457-term Laurent product).
- **G1** single-copy specialization == 1/((1-s)(1-s^2)(1-s^3)) coefficient-by-coefficient (both t=0 and s=0).
- **G2** d_(1,1) == 2 (Phase 67).
- **Two-route** Molien == exact f_4-kernel at all 6 feasible bidegrees (the (2,2) computed in full).
- **Leibniz-lift correctness guard**: rho(M)=M(x)I+I(x)M annihilates c for 52/52 generators (the wrong M(x)M would be 0/52).
- **Symmetry** d_(a,b) == d_(b,a).
- **Krull** dimension == 10 (Phase 65 anchor + convex series growth).
- **Exact-only source guard**: 0 numpy float-rank, 0 numerical torus grid, 0 octonion_algebra imports on the decisive path.

## Decisions Made

- **The 26's 24 nonzero weights are the LONG roots, not the short roots** (the headline decision; see Deviations). Pinned by the G1/G2 gates.
- **Single-copy gate target = [1,1,2,3,4,5,7]** (corrected the plan's s^6 typo of 6 → 7).
- **(2,2) computed in full** via sparse QQ rank — the anticipated Molien-only fallback was not needed.
- The free-algebra series is used ONLY as a labelled sanity comparison, never as H_true (fp-e6-free).

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Implementation efficiency] Molien convolution + Route-B rank rewritten for tractability**

- **Found during:** Task 1 (Molien integrand) and Task 3 (f_4-kernel).
- **Issue:** (a) The naive full 4-torus product N*invX*invY (7225 x 7225 x 165457 SymPy multiplies) stalled > 240s. (b) The dense 10206x10206 (and 142884x142884) operator blocks in the f_4-kernel route stalled > 580s and were memory-infeasible.
- **Fix:** (a) Bookkept the (s,t)-coefficient of each w-monomial as a plain dict over single-marker degrees and extracted the w^0 constant term by exponent convolution pruned to the numerator support (mathematically identical to the iterated symbolic residue, exact over Q, ~19s). (b) Built the stacked f_4-kernel operator as a SPARSE DomainMatrix-over-QQ (dict-of-dicts) and took its exact rank directly — scaling to the 7.34M-row x 142884-col (2,2) matrix in ~36s.
- **Files modified:** code/molien_bigraded.py
- **Verification:** Both routes still EXACT over Q; the two-route agreement at 6 bidegrees confirms correctness; CT=1152 and all gates pass.
- **Committed in:** 5b53520d

**2. [Rule 4 - Missing/corrected component] Short/long root label for the 26's weights, and the single-copy gate target**

- **Found during:** Task 2 (gate G1/G2 fired).
- **Issue:** Using the SHORT roots (perms(+/-1,+/-1,0,0)) as the 26's nonzero weights (as the PLAN frontmatter / RESEARCH primary phrasing suggested) gave d_(1,1)=3 (a spurious antisymmetric trivial in Lambda^2(27)) and FAILED G2; and the plan's single-copy target [1,1,2,3,4,5,6] had a wrong s^6 entry.
- **Fix:** The 26's 24 nonzero weights are the LONG roots (+/-e_i, (+/-1/2)^4, norm^2=1) — this gives d_(1,1)=2 (Phase 67) and the correct single-copy series. The s^6 single-copy coefficient is 7 (= #partitions of 6 into parts <=3), verified independently by sympy.series AND direct partition count.
- **Files modified:** code/molien_bigraded.py (build_27_weights uses long roots; SINGLE_COPY_TARGET = [1,1,2,3,4,5,7], both documented).
- **Verification:** This is exactly the disambiguation the RESEARCH flagged (Caveat 1: "Sources disagree on the short/long label... the calibration gate is the loud check if the short/long label is swapped"). The Weyl measure N (all 48 roots) is short/long-symmetric (CT=1152 either way); only the CHARACTER weight set is pinned by the gates. NEGATIVE-RESULT-IS-SUCCESS: the gate fired, the normalization was fixed BEFORE any two-copy number was trusted, and the fix is corroborated by the 6-bidegree two-route agreement.
- **Committed in:** 5b53520d

---

**Total deviations:** 2 auto-fixed (1 implementation-efficiency, 1 corrected-component / gate-fired normalization).
**Impact on plan:** No scope change. The efficiency rewrites preserve exact-over-Q rigor and IMPROVED the result (the (2,2) bidegree, expected to fall back to Molien-only, was confirmed by BOTH routes). The short/long correction was the intended function of the calibration gates and is fully consistent with all prior-phase anchors.

## Issues Encountered

- The executor stream-watchdog backgrounded the long symbolic runs (as anticipated by the watchdog guidance). All heavy runs were executed foreground with `python -u` and chunked progress prints, and monitored to completion via output-file polling. No data loss.

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
|---|---|---|---|---|---|
| (1,1) Hilbert coeff | d_(1,1) | 2 | exact (0) | Molien == f_4-kernel (729-727) | exact over Q |
| (2,2) Hilbert coeff | d_(2,2) | 9 | exact (0) | Molien == f_4-kernel (142884-142875) | exact over Q |
| (2,1)/(1,2) coeff | d_(2,1) | 4 | exact (0) | Molien == f_4-kernel (10206-10202) | exact over Q |
| Krull dimension | — | 10 | exact (0) | Phase 65 orbit_dim 44; series-corroborated | exact |
| Weyl group order | \|W\| | 1152 | exact (0) | symbolic CT of the all-roots product | exact |

All quantities are exact integers over Q (no tolerance; the error budget is exact).

## Open Questions (for Plan 02)

- **Is Tr(X^2 o Y^2) at (2,2) a generator or a product?** d_(2,2)=9; Plan 02 compares this against the dimension reachable by products of lower candidates {c^2, c*Tr(X)Tr(Y), Tr(X^2)Tr(Y^2), (2,1)*(0,1), (1,2)*(1,0), ...} and runs the in-span-of-lower-products minimality test.
- **Plethystic log:** Plan 02 reads off (generators - relations) per bidegree from this H(s,t) to separate genuine new generators from syzygies (the F_4 ring is non-free; Blind 2011 E_6 contrast).
- **Higher bidegrees (a+b=5,6):** computed by Molien only (the f_4-kernel route is infeasible there); they probe for surprise generators. The genuinely-new generators live at degree <=4 (single-copy <=3, mixed <=4), so 5,6 are corroboration.

## Next Phase Readiness

The certified bigraded dimension table {d_(a,b): a+b<=6} is the decisive handoff to Plan 02 (generating-set assembly + minimality/completeness certificate). It is calibration-gated, two-route-confirmed (exact over Q) at every bidegree where the genuinely-new generators live, Krull-consistent (10), and symmetric. **Pending: Task 4 human verification before the Plan 02 handoff.**

## Cross-Phase Dependencies

### Results This Phase Provides To Later Phases

| Result | Used By Phase | How |
|---|---|---|
| Certified table {d_(a,b): a+b<=6} | Phase 68 Plan 02 | candidate-product comparison + minimality certificate |
| d_(2,2)=9 | Phase 68 Plan 02 | the "(2,2) generator or product?" decision |
| d_(1,1)=2 reproduced | (cross-check) | confirms Phase 67 at the Hilbert-series level |

### Results This Phase Consumed From Earlier Phases

| Result | From Phase | Verified Consistent |
|---|---|---|
| 52-gen f_4 basis + exact_qq_rank | Phase 65 | Yes — Leibniz guard 52/52; rank reproduces Phase 67 (1,1)=2 |
| Krull target 10 | Phase 65 | Yes — series growth corroborates; pole order != 7 |
| (1,1) trivial mult = 2 | Phase 67 | Yes — d_(1,1)=2 by both routes |
| 10-candidate bidegrees | Phase 65.1 | Yes — the candidate bidegrees (1,1),(2,1),(1,2),(2,2) all appear in the table |

### Convention Changes

| Convention | Previous | This Phase | Reason |
|---|---|---|---|
| 26's nonzero weights | (plan said short roots) | the 24 LONG roots | pinned by G1/G2 gates; resolves the documented short/long ambiguity |
| single-copy s^6 coeff | (plan said 6) | 7 | plan typo; #partitions of 6 into parts <=3 = 7 (verified two ways) |

---

_Phase: 68-a-generating-set-completeness-certificate_
_Completed (Tasks 1-3): 2026-05-27_
