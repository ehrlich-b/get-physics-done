---
phase: 01-theorem-a-assembly
verified: 2026-03-15T12:00:00Z
status: passed
score: 9/9 contract targets verified
consistency_score: 10/10 physics checks passed
independently_confirmed: 8/10 checks independently confirmed
confidence: high

re_verification:
  previous_status: gaps_found
  previous_score: 5/9
  gaps_closed:
    - "BLOCKER 1: mu_stable lower bound now uses min(tau_exit, T_eps) with case analysis"
    - "BLOCKER 2: Validation now tests p in {0.3, 0.5, 0.7} with finite alpha via MC"
    - "SIGNIFICANT: gamma value in theorem statement corrected to alpha/2"
  gaps_remaining: []
  regressions: []

comparison_verdicts:
  - subject_kind: acceptance_test
    subject_id: test-three-state
    reference_id: ref-three-state-chain
    comparison_kind: benchmark
    verdict: pass
    metric: relative_error
    threshold: "<= 0.01"
    notes: "Ergodic limit (p=0.5, alpha=0) matches with 0% error; sub-ergodic regime validated via MC for p in {0.3, 0.5, 0.7}"
  - subject_kind: acceptance_test
    subject_id: test-prefactor-bounded
    reference_id: ref-begk
    comparison_kind: consistency
    verdict: pass
    metric: "C independence from epsilon"
    threshold: "C does not depend on epsilon"
    notes: "C = 0.25 is independent of epsilon. For p < 0.5, C is not tight in the ergodic limit, but is a valid upper bound in the sub-ergodic regime (acknowledged in Remark 2)"
  - subject_kind: acceptance_test
    subject_id: test-exponential-form
    reference_id: ref-plan01-lemmas
    comparison_kind: consistency
    verdict: pass
    metric: "error product rate"
    threshold: "gamma > 0"
    notes: "gamma = alpha/2 > 0 for all valid alpha in (0, Ds-Db). Error product preserves exponential form."
---

# Phase 1 Re-Verification: Theorem A Assembly

**Phase goal:** Compose the 7-lemma proof of Boltzmann brain negligibility with explicit error scaling showing mu_BB/mu_stable <= C*exp(-(Delta_s - Delta_b - alpha)/epsilon).

**Re-verified:** 2026-03-15
**Status:** passed
**Confidence:** HIGH
**Mode:** balanced, profile: deep-theory, autonomy: balanced

## Re-Verification Summary

Three gaps were identified in the initial verification. All three have been closed:

1. **BLOCKER 1 (mu_stable lower bound) -- CLOSED.** The proof now uses `mu_stable = integral_0^{min(tau_exit, T_eps)} rho(p_t) dt` (eq mu-stable-def, line 78 of theorem-a-proof.tex). The case analysis in Step 6 splits on A1 = {tau_exit > T_eps} (ratio = 0, trivially bounded) and A2 = {tau_exit <= T_eps} (absorbed into failure probability budget). The old inconsistency where the lower bound exceeded rho_max * T_eps is eliminated. Independently confirmed by numerical check: new lower bound c * T_eps * (1 - O(1/T_eps)) is always <= rho_max * T_eps, while the old bound c * K_s * exp(Ds/eps) exceeded it by factors of 2-17000x.

2. **BLOCKER 2 (validation coverage) -- CLOSED.** The revised validation script tests p in {0.3, 0.5, 0.7} with alpha in {0.3, 0.5, 1.0} via Monte Carlo simulation. All 9 parameter combinations pass. The test now checks the HIGH-PROBABILITY POINTWISE bound (fraction of MC runs where ratio exceeds bound <= claimed failure probability), not the expectation bound. At the previously-failing parameter set (p=0.3, alpha=0.3, eps=0.5), 24.35% of runs violate the bound, well within the 74.08% failure budget.

3. **SIGNIFICANT (gamma value) -- CLOSED.** The theorem statement now reads gamma = alpha/2 (eq delta-def, line 105). The proof's Proposition error-composition (eq gamma-comp, line 603) derives gamma = min(c_2, Ds-alpha, c_5, alpha/2) = alpha/2. Remark 3 (rem:gamma) explains the choice honestly.

## Contract Coverage

| ID | Kind | Status | Confidence | Evidence |
|----|------|--------|------------|----------|
| claim-lemma-statements | claim | VERIFIED | INDEPENDENTLY CONFIRMED | All 7 lemmas have specific theorem citations with explicit error forms |
| claim-dependency-typed | claim | VERIFIED | INDEPENDENTLY CONFIRMED | DAG verified acyclic, all edges typed, type mismatches resolved by BEGK Thm 1.4 |
| claim-theorem-a-assembled | claim | VERIFIED | INDEPENDENTLY CONFIRMED | Case-analysis proof is valid; MC validates across 9 parameter combinations |
| claim-error-composition | claim | VERIFIED | INDEPENDENTLY CONFIRMED | gamma = alpha/2 derived correctly; error product preserves exponential form |
| deliv-lemma-tex | deliverable | VERIFIED | INDEPENDENTLY CONFIRMED | File exists, all 7 lemmas present with citations |
| deliv-proof-tex | deliverable | VERIFIED | INDEPENDENTLY CONFIRMED | File exists, proof complete with case analysis, error composition, and three-state specialization |
| deliv-validation-code | deliverable | VERIFIED | INDEPENDENTLY CONFIRMED | Code runs, tests p in {0.3, 0.5, 0.7} with MC, all 4 checks pass |
| test-three-state | acceptance_test | VERIFIED | INDEPENDENTLY CONFIRMED | MC validates for p=0.3 at (alpha,eps)=(0.3,0.5),(0.5,0.5),(1.0,0.5); ergodic limit exact for p=0.5 |
| test-no-gaps | acceptance_test | VERIFIED | INDEPENDENTLY CONFIRMED | Main argument uses case analysis; no logical gaps remain |

## Required Artifacts

| Artifact | Expected | Status | Details |
|----------|----------|--------|---------|
| derivations/theorem-a-lemmas.tex | 7 lemma statements with error terms | VERIFIED | All 7 present with explicit c_i values and theorem citations |
| derivations/theorem-a-proof.tex | Complete assembled proof | VERIFIED | Proof assembled with case analysis, corrected mu_stable definition, gamma=alpha/2 |
| validation/theorem_a_validation.py | Three-state chain validation | VERIFIED | Tests p in {0.3,0.5,0.7}, alpha in {0.3,0.5,1.0}, MC + ergodic + gamma checks |

## Computational Verification Details

### Spot-Check Results (BLOCKER 1 Fix)

Independent numerical verification that the revised mu_stable lower bound is consistent:

```
eps=0.5, alpha=0.3: T_eps=2.21e+02, E[tau]=4.03e+02
  New lower bound: 1.76e+02 <= 1.77e+02: True
  Old lower bound: 2.58e+02 <= 1.77e+02: False (exceeded by 1.46x)

eps=0.5, alpha=0.5: T_eps=1.48e+02, E[tau]=4.03e+02
  New lower bound: 1.18e+02 <= 1.19e+02: True
  Old lower bound: 2.58e+02 <= 1.19e+02: False (exceeded by 2.17x)

eps=0.1, alpha=1.0: T_eps=4.85e+08, E[tau]=1.07e+13
  New lower bound: 3.88e+08 <= 3.88e+08: True
  Old lower bound: 6.84e+12 <= 3.88e+08: False (exceeded by 17621x)
```

The old bound was violated at all tested parameter combinations. The new bound (using T_min = min(tau_exit, T_eps)) is always consistent.

**Confidence: INDEPENDENTLY CONFIRMED**

### Spot-Check Results (BLOCKER 2 Fix)

Monte Carlo validation at the previously-failing parameter set (p=0.3, alpha=0.3, eps=0.5):

```
MC Results (200000 runs):
  Exit fraction P(A2): 0.3177
  Expected P(A2): 0.5488
  Violation fraction: 0.2435
  Claimed failure prob: 0.7408
  Violation <= claimed: True

  Ratios on A2 (when chain exits):
    Mean:   3.97e-02
    Median: 2.28e-02
    Max:    3.61e+00
    Bound:  8.34e-03
    Fraction of A2 runs violating: 0.7667
```

Key insight: 76.7% of A2 runs (where the chain exits B_stable) violate the bound value. However, A2 itself occurs only 31.8% of the time, so the total violation fraction (24.4%) is within the claimed failure budget (74.1%).

Full MC test matrix from the validation script (all PASS):

```
    p  alpha   eps    Exit%  Exp.Exit%    Viol%  ClaimFail        Bound    OK
  0.3    0.5   0.5  22.3%     36.8%     16.7%     60.7%     1.24e-02  PASS
  0.5    0.5   0.5  16.6%     36.8%     10.4%     60.7%     1.24e-02  PASS
  0.7    0.5   0.5  10.4%     36.8%      5.4%     60.7%     1.24e-02  PASS
  0.3    0.3   0.5  31.5%     54.9%     24.2%     74.1%     8.34e-03  PASS
  0.5    0.3   0.5  23.8%     54.9%     15.3%     74.1%     8.34e-03  PASS
  0.7    0.3   0.5  15.2%     54.9%      7.9%     74.1%     8.34e-03  PASS
  0.3    1.0   0.5   9.0%     13.5%      6.3%     36.8%     3.38e-02  PASS
  0.5    1.0   0.5   6.4%     13.5%      3.7%     36.8%     3.38e-02  PASS
  0.7    1.0   0.5   3.9%     13.5%      1.8%     36.8%     3.38e-02  PASS
```

**Confidence: INDEPENDENTLY CONFIRMED**

### Spot-Check Results (SIGNIFICANT Fix)

gamma value verification:

```
 alpha      c_2   Ds-alpha      c_5  alpha/2      min   = alpha/2?
   0.1      2.0        2.9      2.0     0.05     0.05          Yes
   0.5      2.0        2.5      2.0     0.25     0.25          Yes
   1.0      2.0        2.0      2.0     0.50     0.50          Yes
   1.9      2.0        1.1      2.0     0.95     0.95          Yes
```

gamma = alpha/2 is the bottleneck for all valid alpha in (0, Ds-Db). The theorem statement (eq delta-def) matches.

**Confidence: INDEPENDENTLY CONFIRMED**

### Limiting Cases Re-Derived (Regression Check)

All four previously-passing limits still pass:

**Limit 1: eps -> 0 (exponential decay rate)**
Log(ratio) vs 1/eps has slope -2.000000, expected -(Ds-Db) = -2.0. **PASS** -- INDEPENDENTLY CONFIRMED.

**Limit 2: alpha -> 0 (ergodic recovery for p=0.5)**
Bound/ergodic ratio: alpha=0.01 gives 1.020, alpha=0.001 gives 1.002. Approaches 1 as expected. **PASS** -- INDEPENDENTLY CONFIRMED.

**Limit 3: alpha -> Ds-Db (exponent vanishes)**
Bound at alpha=1.99: 0.245 -> C=0.25. **PASS** -- INDEPENDENTLY CONFIRMED.

**Limit 4: Ds = Db (no metastability)**
Theorem requires Ds > Db. Correctly excluded. **PASS** -- INDEPENDENTLY CONFIRMED.

### Dimensional Analysis Trace (Regression)

| Quantity | Dimensions | Consistent |
|----------|-----------|------------|
| mu_BB/mu_stable | [nats*time] / [nats*time] = dimensionless | Yes |
| C = (rho_max/c) * (K_b/K_s^2) | [nats/nats] * [1/1] = dimensionless | Yes |
| exp(-(Ds-Db-alpha)/eps) | exp(dimensionless) = dimensionless | Yes |
| delta_i = O(exp(-c_i/eps)) | dimensionless | Yes |
| P(A2) = O(exp(-alpha/eps)) | dimensionless probability | Yes |
| P(failure) = O(exp(-alpha/(2eps))) | dimensionless probability | Yes |

**PASS** -- INDEPENDENTLY CONFIRMED.

### Failure Probability Bound Verification

The proof claims P(failure) = O(exp(-alpha/(2eps))). Verified:

| eps | alpha | P(A2) = exp(-alpha/eps) | Claimed = exp(-alpha/(2eps)) | P(A2) <= Claimed |
|-----|-------|------------------------|-----------------------------|--------------------|
| 0.1 | 0.5 | 6.74e-03 | 8.21e-02 | True |
| 0.3 | 0.5 | 1.89e-01 | 4.35e-01 | True |
| 0.5 | 0.5 | 3.68e-01 | 6.07e-01 | True |
| 0.1 | 1.0 | 4.54e-05 | 6.74e-03 | True |
| 0.3 | 1.0 | 3.57e-02 | 1.89e-01 | True |
| 0.5 | 1.0 | 1.35e-01 | 3.68e-01 | True |

Since alpha/eps > alpha/(2eps) for all eps > 0, exp(-alpha/eps) < exp(-alpha/(2eps)) always.

**Confidence: INDEPENDENTLY CONFIRMED**

## Physics Consistency

| # | Check | Status | Confidence | Notes |
|---|-------|--------|------------|-------|
| 5.1 | Dimensional analysis | CONSISTENT | INDEPENDENTLY CONFIRMED | All equations dimensionally consistent |
| 5.2 | Numerical spot-check | VERIFIED | INDEPENDENTLY CONFIRMED | MC validates bound across 9 parameter combinations (3 p-values x 3 alpha values) |
| 5.3 | Limiting cases | VERIFIED | INDEPENDENTLY CONFIRMED | All 4 limits check out; regression confirmed |
| 5.5 | Intermediate spot-check | VERIFIED | INDEPENDENTLY CONFIRMED | mu_stable lower bound now consistent with T_eps truncation |
| 5.6 | Symmetry (DAG acyclicity) | VERIFIED | STRUCTURALLY PRESENT | Graph is acyclic with correct topological order |
| 5.7 | Conservation (probability) | VERIFIED | STRUCTURALLY PRESENT | Union bound correctly accounts for failure probability; P(A2) <= claimed |
| 5.8 | Math consistency | VERIFIED | INDEPENDENTLY CONFIRMED | Case analysis handles both A1 and A2; no double-counting; gamma = alpha/2 consistent throughout |
| 5.10 | Literature agreement | VERIFIED | STRUCTURALLY PRESENT | Citations to BEGK Thm 1.2/1.4, FW Thm 6.3.1, CV Thm 2.1, DV are appropriate |
| 5.11 | Plausibility | VERIFIED | INDEPENDENTLY CONFIRMED | Exponential suppression verified numerically; failure probability monotone decreasing in alpha |
| Gate D | Approximation validity | VERIFIED | STRUCTURALLY PRESENT | Low-noise asymptotics: eps << min(Ds,Db) needed; gamma_D argued O(1) via Cheeger inequality |

## Forbidden Proxy Audit

| Proxy ID | Status | Evidence |
|----------|--------|----------|
| fp-sketch-only | REJECTED | All 7 lemmas cite specific theorem numbers, not just "by BEGK" |
| fp-sketch-repeat | REJECTED | Error terms are explicit with rate constants c_i identified |
| fp-unspecified-c | REJECTED | Each c_i bounded: c_2 >= Ds-Db, c_4 = Ds, c_5 >= Ds-Db, c_6 = alpha |
| fp-ignoring-alpha | REJECTED | Alpha constraint 0 < alpha < Ds-Db appears in theorem statement and proof |
| fp-expectation-only | REJECTED | Case analysis converts to high-probability bound; Step 6 handles the conversion explicitly |

## Comparison Verdict Ledger

| Subject | Comparison | Verdict | Notes |
|---------|-----------|---------|-------|
| test-three-state | three_state_chain.py benchmark | pass | Ergodic limit (p=0.5) exact; MC validates sub-ergodic for all p |
| test-exponential-form | Error product analysis | pass | Product is 1 + O(exp(-gamma/eps)) with gamma = alpha/2 > 0 |
| test-prefactor-bounded | C independence from eps | pass | C = 0.25 is epsilon-independent; acknowledged non-tight for p < 0.5 in ergodic limit |

## Requirements Coverage

| Requirement | Status | Notes |
|-------------|--------|-------|
| DERV-01 | SATISFIED | Proof assembled with case analysis, corrected mu_stable, gamma = alpha/2 |
| DERV-03 | SATISFIED | Error composition preserves exponential form with gamma = alpha/2 > 0 |
| VALD-03 | SATISFIED | Three-state validation passes for p in {0.3, 0.5, 0.7} with MC simulation |

## Anti-Patterns Found

| Category | Location | Description | Physics Impact |
|----------|----------|-------------|----------------|
| INFO | theorem-a-proof.tex | Revision history and routing discussion present (Remark 2) | Positive: transparent about limitations |
| INFO | theorem_a_validation.py | Seeds RNG for reproducibility | None (positive) |
| INFO | theorem-a-lemmas.tex | Lemma 4 still defines mu_stable with integral to tau_exit (not min) | Not a blocker: lemma is valid as standalone; proof redefines for the theorem context |
| INFO | Both .tex files | ASSERT_CONVENTION headers present and match state.json | Convention consistency verified |

## Expert Verification Suggested

| Check | Expected | Domain | Why Expert |
|-------|----------|--------|-----------|
| BEGK Thm 1.4 convergence in distribution vs finite eps | Exponential law is asymptotic; finite eps corrections | Metastability theory | The MC at eps=0.5 shows P(exit) < 1-exp(-s) rather than exactly matching; finite-eps corrections are standard but could be quantified |
| Routing probability q generalization | q enters C for tighter bounds | Harmonic measure theory | The general proof uses q <= 1; sharpening to q = cap(s, B_BB)/cap(s, B_stable^c) is possible but requires BEGK capacity details |
| QSD gamma_D lower bound | gamma_D should be polynomial in chain parameters | Spectral gap theory | Argued via Cheeger inequality but not explicitly computed; should verify for concrete examples |

## Confidence Assessment

**Overall confidence: HIGH**

All three previously-identified gaps have been closed by the revised proof and validation:

1. The mu_stable definition inconsistency is fixed. The proof now uses min(tau_exit, T_eps) and splits on the two cases. On A1 (dominant case, probability ~ 1 - exp(-alpha/eps)), mu_BB = 0 and the bound is trivially satisfied. On A2 (probability ~ exp(-alpha/eps)), the event is within the failure budget. This is verified by MC simulation across 9 parameter combinations.

2. The validation script now tests p in {0.3, 0.5, 0.7} with finite alpha, using Monte Carlo simulation of the actual CTMC dynamics. All tests pass. The test correctly checks the high-probability pointwise bound (violation fraction <= claimed failure probability), not the expectation bound.

3. The gamma value is consistently stated as alpha/2 in both the theorem statement (eq delta-def) and the proof (eq gamma-comp, Proposition error-composition). This is honest: gamma = alpha/2 is the bottleneck rate from the eta = exp(-alpha/(2eps)) choice.

The proof's structure is sound: 7 lemmas precisely stated, dependency graph verified acyclic with all type mismatches resolved, error composition verified, and the case analysis provides a correct high-probability bound. The prefactor C = 0.25 is not tight for p < 0.5 in the ergodic limit, but this is acknowledged in Remark 2 and does not affect the validity of the sub-ergodic theorem.

**Minor note:** Lemma 4 in theorem-a-lemmas.tex still uses the unconditional mu_stable definition (integral to tau_exit). This is valid as a standalone lemma statement, but the proof file correctly redefines mu_stable with the truncation for the theorem context. This is not a gap -- the lemma bounds the measure during a single residence, while the theorem truncates at the observation horizon.
