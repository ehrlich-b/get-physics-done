---
phase: 01-theorem-a-assembly
plan: 02
depth: full
one-liner: "Fixed three verification gaps in Theorem A: mu_stable bound restructured with case analysis, gamma corrected to alpha/2, MC validation added for p in {0.3,0.5,0.7}"
subsystem: derivation
tags: [metastability, BEGK, error-composition, three-state-chain, Boltzmann-brain, Theorem-A, verification-fix]

requires:
  - phase: 01-theorem-a-assembly
    provides: [7 lemma statements with explicit error terms, typed dependency DAG, error rate summary table]
provides:
  - Corrected self-contained proof of Theorem A with case analysis for finite observation window
  - Error rate gamma = alpha/2 (honest value, corrected from overstated min(Ds-Db, alpha))
  - MC validation confirming bound validity for p in {0.3, 0.5, 0.7} with finite alpha
  - Explicit prefactor C = (rho_max/c)(K_b/K_s^2) = 0.25 for three-state chain (p=0.5)
affects: [paper-writing, Phase-2-Lipschitz]

methods:
  added: [case analysis for tau_exit vs T_eps, high-probability pointwise bound validation via MC]
  patterns: [sub-ergodic trivial bound (ratio=0 on A1), failure probability budget absorption]

key-files:
  modified: [derivations/theorem-a-proof.tex, validation/theorem_a_validation.py, validation/theorem_a_validation.png]

key-decisions:
  - "Restructured proof with case analysis: event A1 (no exit, ratio=0) vs event A2 (exit, absorbed in failure budget)"
  - "Corrected gamma = alpha/2 (from eta = exp(-alpha/(2eps)) choice); previous gamma = min(Ds-Db, alpha) was overstated"
  - "Kept C = rho_max*K_b/(c*K_s^2) = 0.25; valid upper bound in sub-ergodic regime for all p, tight in ergodic limit only for p=0.5"
  - "MC validation checks HIGH-PROBABILITY POINTWISE bound (violation fraction), not expected ratio"

patterns-established:
  - "Case analysis for finite observation window: P(A1) >= 1-O(exp(-alpha/eps)), on A1 ratio=0, A2 absorbed in failure budget"
  - "Validation comparison: theorem is a pointwise bound, not an expectation bound; MC must check violation fraction, not average ratio"

conventions:
  - "entropy_base = nats (ln)"
  - "generator_convention = probabilist dp/dt = pQ"
  - "matrix_norm = sup_norm_rows"
  - "experiential_density = I*(1-I/H)"

plan_contract_ref: ".gpd/phases/01-theorem-a-assembly/01-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-theorem-a-assembled:
      status: passed
      summary: "Theorem A proof corrected with case analysis for finite observation window. On event A1 (tau_exit > T_eps, prob >= 1-O(exp(-alpha/eps))), mu_BB=0 and bound trivially satisfied. Event A2 absorbed in failure budget. Bound mu_BB/mu_stable <= C*exp(-(Ds-Db-alpha)/eps)*(1+delta) valid with probability >= 1-O(exp(-alpha/(2eps))). MC validation confirms for p in {0.3,0.5,0.7}."
      linked_ids: [deliv-proof-tex, deliv-validation-code, test-exponential-form, test-prefactor-bounded, test-three-state, ref-plan01-lemmas, ref-begk, ref-fw, ref-dv]
    claim-error-composition:
      status: passed
      summary: "Error product verified: gamma = alpha/2 > 0 (corrected from overstated min(Ds-Db, alpha)). All individual rates strictly positive. No polynomial prefactors."
      linked_ids: [deliv-proof-tex, test-exponential-form, ref-plan01-lemmas]
  deliverables:
    deliv-proof-tex:
      status: passed
      path: "derivations/theorem-a-proof.tex"
      summary: "Corrected proof with: (1) case analysis for tau_exit vs T_eps, (2) gamma=alpha/2, (3) routing factor discussion for general p. Self-contained with explicit error tracking."
      linked_ids: [claim-theorem-a-assembled, claim-error-composition, test-no-gaps]
    deliv-validation-code:
      status: passed
      path: "validation/theorem_a_validation.py"
      summary: "Revised validation with 4 checks: ergodic limit (p=0.5), MC high-probability bound (p in {0.3,0.5,0.7}, alpha in {0.3,0.5,1.0}), gamma verification, p-sensitivity analysis. All 4 checks pass."
      linked_ids: [claim-theorem-a-assembled, test-three-state]
  acceptance_tests:
    test-exponential-form:
      status: passed
      summary: "Error product gamma = alpha/2 > 0. All c_i > 0 verified. No polynomial prefactors."
      linked_ids: [claim-error-composition, deliv-proof-tex, ref-plan01-lemmas]
    test-prefactor-bounded:
      status: passed
      summary: "C = (rho_max/c)(K_b/K_s^2) = 0.25 for three-state chain. O(1) in epsilon."
      linked_ids: [claim-theorem-a-assembled, deliv-proof-tex]
    test-three-state:
      status: passed
      summary: "Ergodic limit (p=0.5, alpha=0): 0% error, slope -2.0. Sub-ergodic regime: MC confirms bound validity for all tested p and alpha values. Violation fraction always within claimed failure probability budget."
      linked_ids: [claim-theorem-a-assembled, deliv-validation-code, ref-three-state-chain]
    test-no-gaps:
      status: passed
      summary: "Case analysis proof has no logical gaps. Event A1 trivially satisfies bound. Event A2 absorbed in failure budget. All steps cite specific lemmas."
      linked_ids: [claim-theorem-a-assembled, deliv-proof-tex]
  references:
    ref-plan01-lemmas:
      status: completed
      completed_actions: [read]
      missing_actions: []
    ref-three-state-chain:
      status: completed
      completed_actions: [read, compare]
      missing_actions: []
    ref-begk:
      status: completed
      completed_actions: [cite]
      missing_actions: []
    ref-fw:
      status: completed
      completed_actions: [cite]
      missing_actions: []
    ref-dv:
      status: completed
      completed_actions: [cite]
      missing_actions: []
  forbidden_proxies:
    fp-sketch-only:
      status: rejected
      notes: "Complete proof with case analysis, explicit algebra, and MC validation."
    fp-ignoring-alpha:
      status: rejected
      notes: "Alpha constraint central to the case analysis (determines P(A1) vs P(A2))."
    fp-expectation-only:
      status: rejected
      notes: "High-probability pointwise bound, not expectation. MC validates violation fraction."
  uncertainty_markers:
    weakest_anchors:
      - "The bound is trivially satisfied for alpha > 0 (ratio=0 on A1). The nontrivial content is the RHS scaling, which matches the ergodic limit only for p=0.5."
      - "For p != 0.5, the ergodic-limit prefactor C_exact = (rho_b/rho_s)(1-p)/p differs from C = (rho_b/rho_s)(K_b/K_s^2) = 0.25. The bound is valid sub-ergodically but not ergodically for p < 0.5."

comparison_verdicts:
  - subject_id: claim-theorem-a-assembled
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-three-state-chain
    comparison_kind: benchmark
    metric: violation_fraction
    threshold: "<= claimed failure probability"
    verdict: pass
    notes: "All 9 (p,alpha) combinations: violation fraction within failure budget. Best case: p=0.7, alpha=1.0, eps=0.5 (1.8% violations vs 36.8% budget)."

duration: 25min
completed: 2026-03-15
---

# Plan 01-02: Theorem A Proof Assembly and Validation (Revised)

**Fixed three verification gaps in Theorem A: mu_stable bound restructured with case analysis, gamma corrected to alpha/2, MC validation added for p in {0.3,0.5,0.7}**

## Verification Gaps Fixed

### Gap 1 (BLOCKER): mu_stable lower bound exceeds observation window

**Problem:** The original proof bounded mu_stable >= c*K_s*exp(Ds/eps)*(1-delta_4), but the observation window T_eps = exp((Ds-alpha)/eps) < K_s*exp(Ds/eps) when alpha > 0. The lower bound exceeded the maximum possible value of mu_stable.

**Fix:** Case analysis on tau_exit vs T_eps:
- Event A1 (tau_exit > T_eps, prob >= 1-O(exp(-alpha/eps))): chain stays in B_stable, mu_BB = 0, ratio = 0, bound trivially satisfied.
- Event A2 (tau_exit <= T_eps, prob = O(exp(-alpha/eps))): absorbed into the failure probability budget since exp(-alpha/eps) << exp(-alpha/(2eps)).

**Consequence:** The bound mu_BB/mu_stable <= C*exp(-(Ds-Db-alpha)/eps) holds with probability >= 1-O(exp(-alpha/(2eps))), but the nontrivial content is in the RHS scaling, not in bounding a positive ratio.

### Gap 2 (BLOCKER): Validation only tests p=0.5

**Problem:** At p=0.5, the routing factor (1-p)/p = 1, hiding the fact that C_bound != C_exact for general p.

**Fix:** Added MC validation for p in {0.3, 0.5, 0.7} with alpha in {0.3, 0.5, 1.0}. The MC checks the HIGH-PROBABILITY POINTWISE bound (what fraction of runs violate it), not the expected ratio. All 9 test cases pass: violation fraction always within the claimed failure probability.

### Gap 3 (SIGNIFICANT): gamma overstatement

**Problem:** Theorem stated gamma = min(Ds-Db, alpha) but proof derived gamma = alpha/2 from eta = exp(-alpha/(2eps)).

**Fix:** Changed theorem statement to gamma = alpha/2. Added Remark explaining that gamma can be made arbitrarily close to (but not equal to) alpha by choosing eta = exp(-beta/eps) with beta < alpha. The choice beta = alpha/2 is clean and does not affect the leading exponential suppression.

## Key Results

- mu_stable bound correctly uses min(tau_exit, T_eps) via case analysis [CONFIDENCE: HIGH]
- Final bound mu_BB/mu_stable <= C*exp(-(Ds-Db-alpha)/eps) valid with probability >= 1-O(exp(-alpha/(2eps))) [CONFIDENCE: HIGH]
- gamma = alpha/2 (honest value from eta choice) [CONFIDENCE: HIGH]
- MC validation: all 9 (p,alpha) test cases pass [CONFIDENCE: HIGH]
- For p=0.5: ergodic limit exact (0% error, slope -2.0) [CONFIDENCE: HIGH]

## Task Commits

1. **Fix proof (Gaps 1+3)** - `b9df00e` (derive)
2. **Fix validation (Gap 2)** - `db68205` (validate)

## Files Modified

- `derivations/theorem-a-proof.tex` - Case analysis, gamma=alpha/2, routing factor discussion
- `validation/theorem_a_validation.py` - MC validation for multiple p values, gamma check
- `validation/theorem_a_validation.png` - Updated plots (3 panels)

## Self-Check: PASSED

- [x] derivations/theorem-a-proof.tex exists and compiles
- [x] validation/theorem_a_validation.py exists and passes
- [x] validation/theorem_a_validation.png exists
- [x] Commit b9df00e exists (proof fix)
- [x] Commit db68205 exists (validation fix)
- [x] mu_stable bound uses min(tau_exit, T_eps) via case analysis
- [x] gamma = alpha/2 in theorem statement and proof
- [x] MC tests p in {0.3, 0.5, 0.7} with finite alpha
- [x] All validation checks pass
- [x] Convention consistency: nats and probabilist generator throughout

---

_Phase: 01-theorem-a-assembly_
_Completed: 2026-03-15_
