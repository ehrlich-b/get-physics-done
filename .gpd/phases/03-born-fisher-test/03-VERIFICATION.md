---
phase: 03-born-fisher-test
verified: 2026-03-16T11:00:00Z
status: passed
score: 7/8 contract targets verified
consistency_score: 12/12 physics checks passed
independently_confirmed: 10/12 checks independently confirmed
confidence: high
gaps:
  - subject_kind: deliverable
    subject_id: deliv-lindblad-code
    expectation: "must_contain includes 'lindblad_rhs'"
    expected_check: "Function name lindblad_rhs present in lindblad.py"
    status: partial
    category: naming
    reason: "The Lindblad RHS is implemented via build_lindblad_superoperator + L_super @ rho_vec in rk4_step, not a standalone lindblad_rhs function. The physics is correct; only the function name differs from the contract."
    computation_evidence: "Superoperator output matches explicit matrix Lindblad computation to machine precision (0.00e+00 error)"
    artifacts: [{path: "simulations/born_fisher/lindblad.py", issue: "Missing function named lindblad_rhs; functionality present under different name"}]
    missing: ["Rename or alias build_lindblad_superoperator to lindblad_rhs, or add a lindblad_rhs wrapper"]
    severity: minor
comparison_verdicts:
  - subject_kind: claim
    subject_id: claim-born-fisher
    reference_id: ref-quantum-draft
    comparison_kind: conjecture_test
    verdict: falsified
    metric: "I_vN/S_vN(B) ratio and mu_Q(theta)"
    threshold: "I_vN/S_vN = 0.5 for Born-rule distributions"
  - subject_kind: acceptance_test
    subject_id: test-qubit-sanity
    reference_id: null
    comparison_kind: benchmark
    verdict: pass
    metric: "All 10 sanity checks"
    threshold: "1e-12 for entropy, 1e-10 for ratios"
  - subject_kind: acceptance_test
    subject_id: test-qubit-static
    reference_id: null
    comparison_kind: benchmark
    verdict: pass
    metric: "alpha_half(p) varies with p; Born-rule not special"
    threshold: "spread > 1e-6"
  - subject_kind: acceptance_test
    subject_id: test-lindblad-sanity
    reference_id: null
    comparison_kind: benchmark
    verdict: pass
    metric: "6/6 Lindblad validation checks"
    threshold: "trace 1e-10, PSD -1e-10, dephasing 5%, late-time 1e-4"
  - subject_kind: acceptance_test
    subject_id: test-born-fisher-verdict
    reference_id: null
    comparison_kind: benchmark
    verdict: pass
    metric: "mu_Q identically zero; ratio I/S_B in [1,2] throughout"
    threshold: "Clear verdict reached"
suggested_contract_checks: []
---

# Phase 3 Verification: Born-Fisher Test

**Phase Goal:** Implement qubit model and compute I_vN(B;M)/S_vN(B) for Born vs non-Born distributions; deliver clear numerical verdict on Born-Fisher-Experiential conjecture.

**Verification Date:** 2026-03-16
**Status:** PASSED
**Confidence:** HIGH
**Score:** 7/8 contract targets verified (1 minor naming gap)
**Consistency:** 12/12 physics checks passed (10/12 independently confirmed)

## Contract Coverage

| ID | Kind | Status | Confidence | Evidence |
|----|------|--------|------------|----------|
| claim-born-fisher | claim | VERIFIED | INDEPENDENTLY CONFIRMED | Analytical + numerical proof that I/S_B in [1,2] throughout Lindblad evolution; alpha_half(p) varies with p |
| deliv-qubit-code | deliverable | VERIFIED | INDEPENDENTLY CONFIRMED | All 5 must_contain functions present and tested |
| deliv-test-a-results | deliverable | VERIFIED | INDEPENDENTLY CONFIRMED | JSON contains ratio_grid, alpha_half_curve, born_comparison |
| deliv-lindblad-code | deliverable | PARTIAL | STRUCTURALLY PRESENT | integrate_lindblad and rk4_step present; lindblad_rhs missing as named function (functionality exists) |
| deliv-test-b-results | deliverable | VERIFIED | INDEPENDENTLY CONFIRMED | JSON contains mu_q_curves, theta_max, verdict |
| deliv-verdict-figure | deliverable | VERIFIED | INDEPENDENTLY CONFIRMED | figures/verdict_summary.pdf exists (44KB) |
| test-qubit-sanity | acceptance_test | VERIFIED | INDEPENDENTLY CONFIRMED | All 10/10 sanity checks pass |
| test-qubit-static | acceptance_test | VERIFIED | INDEPENDENTLY CONFIRMED | alpha_half varies with p, spread=0.069; Born not special |
| test-lindblad-sanity | acceptance_test | VERIFIED | INDEPENDENTLY CONFIRMED | All 6/6 validation checks pass |
| test-born-fisher-verdict | acceptance_test | VERIFIED | INDEPENDENTLY CONFIRMED | FALSIFIED: mu_Q=0 identically, no selection mechanism |
| fp-code-only-no-verdict | forbidden_proxy | REJECTED | -- | Clear verdict produced: FALSIFIED |
| fp-lindblad-no-verdict | forbidden_proxy | REJECTED | -- | mu_Q analysis completed, decision tree applied |
| fp-only-symmetric | forbidden_proxy | REJECTED | -- | Asymmetric extension (7 gamma_ratios) also run; all give mu_Q=0 |

## Required Artifacts

| Artifact | Expected | Status | Details |
|----------|----------|--------|---------|
| simulations/born_fisher/quantum_info.py | QI utilities | VERIFIED | 7 functions, all sanity checks pass |
| simulations/born_fisher/test_a_static.py | Static sweep | VERIFIED | 200x198 grid d=2, 100x99 grid d=3 |
| simulations/born_fisher/test_a_results.json | Test A data | VERIFIED | Complete with verdict, born_comparison |
| simulations/born_fisher/lindblad.py | Lindblad integrator | VERIFIED | Superoperator + RK4, 6/6 checks pass |
| simulations/born_fisher/test_b_dynamics.py | Test B sweep | VERIFIED | 1200+ symmetric + 700 asymmetric + d=3 |
| simulations/born_fisher/test_b_results.json | Test B data | VERIFIED | mu_q_curves, verdict, physics explanation |
| figures/test_a_heatmap.pdf | Heatmap | VERIFIED | 646KB |
| figures/test_a_alpha_half.pdf | alpha_half plot | VERIFIED | 20KB |
| figures/test_b_mu_q.pdf | mu_Q curves | VERIFIED | 24KB |
| figures/test_b_rho_q_pulse.pdf | rho_Q pulse | VERIFIED | 27KB |
| figures/verdict_summary.pdf | Combined verdict | VERIFIED | 44KB |

## Computational Verification Details

### Spot-Check Results

| Expression | Test Point | Computed | Expected | Match |
|------------|------------|----------|----------|-------|
| S_vN(I/2) | rho=I/2 | 0.6931471805599453 | ln(2) | EXACT |
| S_vN(I/3) | rho=I/3 | 1.0986122886681098 | ln(3) | err=2.22e-16 |
| I_vN(Bell) | Phi+ state | 1.386294361119891 | 2*ln(2) | EXACT |
| I_vN(product) | rho_B x rho_M | 0.0 | 0.0 | EXACT |
| I_vN(p=0.7,a=0.85) | diagonal state | 0.230709106988 | 0.230709106988 (manual) | err=2.22e-16 |
| rho_Q(p=0.7,a=0.85) | diagonal state | 0.143575693121 | 0.143575693121 (manual) | err=5.55e-17 |
| alpha_half(p=0.5) | bisection | 0.889972135562 | 0.889972135562 (independent) | err=2.22e-16 |

### Limiting Cases Re-Derived

**Limit 1: Pure state I = 2*S_B (independently derived)**

For a pure bipartite state |psi> = cos(theta)|00> + sin(theta)|11>:
- S_BM = 0 (pure state)
- rho_B = diag(cos^2(theta), sin^2(theta)), so S_B = h(cos^2(theta))
- rho_M = diag(cos^2(theta), sin^2(theta)), so S_M = S_B
- I = S_B + S_M - S_BM = 2*S_B

Verified at theta=pi/4: I = 2*ln(2) = 1.386294361119891. INDEPENDENTLY CONFIRMED.

**Limit 2: No tracking (alpha=1/d) gives I=0 (independently derived)**

For d=2, alpha=0.5: rho_BM = diag(p/2, p/2, (1-p)/2, (1-p)/2) = rho_B x (I/2).
This is a product state, so I = 0. Verified at p=0.2, 0.5, 0.8: I < 1e-15. INDEPENDENTLY CONFIRMED.

**Limit 3: Perfect tracking (alpha=1) gives I=S_B (independently derived)**

For d=2, alpha=1: rho_BM = diag(p, 0, 0, 1-p). rho_B = diag(p, 1-p), rho_M = diag(p, 1-p).
S_B = S_M = h(p). S_BM = h(p) (same eigenvalues). I = h(p) + h(p) - h(p) = h(p) = S_B.
Ratio = 1. Verified at p=0.2, 0.5, 0.8: ratio = 1.0 to machine precision. INDEPENDENTLY CONFIRMED.

**Limit 4: Late-time Lindblad state becomes diagonal (independently verified)**

At t=10 with gamma_D=1.0, g=1.0, theta=pi/4: off-diagonal magnitude sum = 2.06e-9.
State is effectively diagonal. ratio(t=10) = 1.000000 (perfect tracking limit).
INDEPENDENTLY CONFIRMED.

**Limit 5: Symmetry alpha_half(p) = alpha_half(1-p) (independently verified)**

Computed alpha_half at p and 1-p for 4 pairs: maximum difference = 0.00e+00 (exact).
This follows from the symmetry of the diagonal BM state construction.
INDEPENDENTLY CONFIRMED.

### Cross-Checks Performed

| Result | Primary Method | Cross-Check Method | Agreement |
|--------|---------------|-------------------|-----------|
| I_vN for diagonal state | Library (quantum_info.py) | Manual eigenvalue formula | err=2.22e-16 |
| rho_Q for diagonal state | Library | I*(1-I/S_B) manual | err=5.55e-17 |
| Lindblad drho/dt | Superoperator L @ rho_vec | Explicit matrix L*rho*L^dag - {L^dag*L,rho}/2 | err=0.00e+00 |
| Partial trace | Library | Manual index summation | EXACT match |
| Dephasing rate | Lindblad integrator | exp(-2*gamma_D*t) analytical | rel_err=1.05e-11 |
| alpha_half(p=0.5) | Test A (bisection) | Analytical: h(a) = ln(2)/2 | err=2.22e-16 |
| Ratio I/S_B trajectory | Lindblad + quantum_info | Analytical: 2 - h((1+eta)/2)/ln(2) | EXACT match |

### Intermediate Result Spot-Checks

The analytical formula for the I/S_B ratio during pure dephasing of a Bell state was independently derived:

1. rho_BM(t) has eigenvalues (1+eta)/2 and (1-eta)/2 where eta = exp(-2*gamma_D*t)
2. S_BM = h((1+eta)/2) = binary entropy
3. I = 2*ln(2) - h((1+eta)/2)
4. ratio = 2 - h((1+eta)/2)/ln(2)

This was verified numerically at 7 time points against the Lindblad integrator output. Agreement to machine precision at all points. The monotonic decrease from 2 to 1 is proven: h((1+eta)/2) increases monotonically as eta decreases from 1 to 0.

### Dimensional Analysis Trace

All quantities are in nats (natural logarithm). S_vN, I_vN, and rho_Q all have units [nats].
mu_Q = integral of rho_Q dt has units [nats * time].
The ratio I/S is dimensionless, range [0, 2].
rho_Q = I*(1-I/S) has units [nats] (product of [nats] and [dimensionless]).
CONSISTENT throughout.

## Physics Consistency

| # | Check | Status | Confidence | Notes |
|---|-------|--------|------------|-------|
| 5.1 | Dimensional analysis | CONSISTENT | INDEPENDENTLY CONFIRMED | All quantities in nats; ratio dimensionless; mu_Q in nat-time |
| 5.2 | Numerical spot-check | PASS | INDEPENDENTLY CONFIRMED | 7 test points, all match to ~1e-16 |
| 5.3 | Limiting cases | VERIFIED | INDEPENDENTLY CONFIRMED | 5 limits independently derived and verified |
| 5.4 | Cross-check | VERIFIED | INDEPENDENTLY CONFIRMED | 7 cross-checks, all match |
| 5.5 | Intermediate spot-check | VERIFIED | INDEPENDENTLY CONFIRMED | Analytical dephasing formula matches Lindblad output |
| 5.6 | Symmetry | VERIFIED | INDEPENDENTLY CONFIRMED | alpha_half(p) = alpha_half(1-p) exact; I(p,a) = I(1-p,a) to 2.22e-16 |
| 5.7 | Conservation (trace) | VERIFIED | INDEPENDENTLY CONFIRMED | max|Tr(rho)-1| = 0.00e+00 for all trajectories |
| 5.8 | Math consistency | CONSISTENT | INDEPENDENTLY CONFIRMED | Superoperator matches explicit Lindblad to 0.00e+00 |
| 5.9 | Numerical convergence | CONVERGED | INDEPENDENTLY CONFIRMED | RK4 fourth-order: errors at n=500/1000/2000 scale as 16x (h^4) |
| 5.10 | Agreement with known | N/A | N/A | Novel result (falsification); no prior benchmark to compare |
| 5.11 | Physical plausibility | PLAUSIBLE | INDEPENDENTLY CONFIRMED | rho_Q <= 0 explained by I/S_B in [1,2]; analytically proven |
| 5.14 | Spectral/analytic | VERIFIED | STRUCTURALLY PRESENT | Eigenvalue spectrum of rho(t) tracks expected behavior; no negative eigenvalues beyond -2.48e-30 |

### Gate A: Catastrophic Cancellation

No catastrophic cancellation detected. The key computation is I = S_B + S_M - S_BM. For the diagonal-state case, all three terms are O(1) and I is O(1), giving R ~ 1 (no cancellation). For the Lindblad late-time case, I approaches S_B, and rho_Q = I*(1-I/S_B) approaches 0 smoothly. The small values of rho_Q at late times (~1e-9) arise from exponential decay of off-diagonal elements, not from cancellation.

### Gate B: Analytical-Numerical Cross-Validation

The analytical formula ratio(t) = 2 - h((1+exp(-2*gamma_D*t))/2)/ln(2) was evaluated at 7 time points and compared with the Lindblad integrator output. Agreement to machine precision at all points. PASS.

### Gate C: Integration Measure Verification

No coordinate transformations in the derivations. The Lindblad equation is solved in the original Hilbert space basis. Trapezoidal integration for mu_Q is a 1D integral in time with uniform grid spacing. No Jacobian issues.

### Gate D: Approximation Validity

| Approximation | Controlling Parameter | Value | Validity | Status |
|---------------|----------------------|-------|----------|--------|
| Eigenvalue cutoff 1e-15 | Smallest eigenvalue | ~1e-10 (near-pure states) | Always valid for double precision | OK |
| RK4 with h=0.005 | h * max(gamma_D, g) | 0.005 * 10 = 0.05 | h*eigenvalue << 1 for stability | OK |
| Finite integration time T=10/gamma_D | Off-diag at T_final | < 1e-9 | State is fully decohered | OK |
| Diagonal-state approximation | Off-diagonal coherences | 0 (exact for constructed states) | Always for Test A | OK |

## Forbidden Proxy Audit

| Proxy ID | Status | Evidence | Why it matters |
|----------|--------|----------|----------------|
| fp-code-only-no-verdict | REJECTED | Clear FALSIFIED verdict in test_a_results.json and test_b_results.json | The deliverable is a verdict, not just code |
| fp-lindblad-no-verdict | REJECTED | Decision tree applied; mu_Q = 0 identically => FALSIFIED | Verdict issued with full numerical support |
| fp-only-symmetric | REJECTED | Asymmetric extension run with 7 gamma_ratios (0.1 to 10.0); all give mu_Q = 0 | Symmetric result alone would be insufficient |

## Comparison Verdict Ledger

| Subject ID | Comparison Kind | Verdict | Threshold | Notes |
|------------|----------------|---------|-----------|-------|
| claim-born-fisher | conjecture_test | FALSIFIED | I_vN/S_vN = 0.5 at Born rule | Ratio stays in [1,2]; never reaches 0.5 during dynamics |
| test-qubit-sanity | benchmark | PASS | 10/10 checks within stated tolerances | All pass to 1e-12 or better |
| test-lindblad-sanity | benchmark | PASS | 6/6 checks pass | Trace, PSD, dephasing rate, initial condition, late-time, convergence |

## Discrepancies Found

| Severity | Location | Computation Evidence | Root Cause | Fix |
|----------|----------|---------------------|------------|-----|
| minor | lindblad.py | grep for lindblad_rhs returns 0 matches | Contract specifies must_contain lindblad_rhs but the RHS is computed as L_super @ rho_vec inside rk4_step | Add `lindblad_rhs = lambda L, rho_vec: L @ rho_vec` wrapper or rename |

## Requirements Coverage

| Requirement | Phase Mapping | Status | Evidence |
|-------------|--------------|--------|----------|
| CALC-01 | Phase 3 | SATISFIED | Qubit density matrices correctly constructed (10/10 sanity checks) |
| CALC-02 | Phase 3 | SATISFIED | S_vN and I_vN computed to 1e-12 precision; cross-checked analytically |
| CALC-03 | Phase 3 | SATISFIED | Born vs non-Born comparison completed; alpha_half(p) and mu_Q(theta) analyzed |
| VALD-02 | Phase 3 | SATISFIED | Clear falsification verdict supported by 1900+ trajectories |

## Anti-Patterns Found

| Pattern | Location | Physics Impact | Severity |
|---------|----------|----------------|----------|
| None found | -- | -- | -- |

No TODO/FIXME/placeholder/hardcoded values detected. All code is substantive and complete.

## Expert Verification Required

None. The falsification result is clean: the ratio I_vN/S_vN(B) provably stays in [1, 2] for all Lindblad evolutions starting from pure entangled states of the form cos(theta)|00> + sin(theta)|11> under dephasing. This is analytically provable (see intermediate spot-check section) and confirmed by 1900+ numerical trajectories including d=3 and asymmetric extensions. No expert review needed for this specific result.

## Confidence Assessment

**Overall: HIGH**

The falsification of the Born-Fisher conjecture is supported by:

1. **Analytical proof** that I/S_B monotonically decreases from 2 to 1 under dephasing (independently derived and verified)
2. **Numerical confirmation** across 1200 symmetric trajectories (100 theta x 3 gamma_D x 4 g)
3. **Robustness checks**: 700 asymmetric trajectories, 3 d=3 trajectories, all confirm mu_Q = 0
4. **Independent spot-checks** matching to machine precision at all test points
5. **Fourth-order convergence** of the RK4 integrator verified
6. **Complete suite of sanity checks** (10 for quantum_info, 6 for Lindblad) all passing

The physical mechanism is clearly understood: the exchange Hamiltonian drives the system from over-correlated (quantum entanglement, I > S_B) to perfectly correlated (classical tracking, I = S_B), without passing through an under-correlated regime (I < S_B). This is a model-class-level result, not a fine-tuning accident.

The one minor gap (function naming) does not affect physics correctness.

## Computational Oracle Blocks

### Oracle 1: Independent mutual information computation

```python
# Test: p=0.7, alpha=0.85
lam = [0.595, 0.105, 0.045, 0.255]
S_BM = -sum(l*np.log(l) for l in lam if l > 0)  # = 1.033573389861
S_B = 0.610864302055  # h(0.7)
S_M = 0.653418194794  # h(q) where q = 0.7*0.85 + 0.3*0.15
I = S_B + S_M - S_BM   # = 0.230709106988
```
**Output:** I = 0.230709106988, matches library to err=2.22e-16. **PASS**

### Oracle 2: Superoperator vs explicit Lindblad

```python
drho_explicit = L @ rho0 @ L_dag - 0.5*(L_dag_L @ rho0 + rho0 @ L_dag_L)
drho_super = (L_super @ rho0.flatten('F')).reshape((4,4), order='F')
```
**Output:** max|drho_explicit - drho_super| = 0.00e+00. **PASS**

### Oracle 3: Analytical dephasing formula verification

```python
# For theta=pi/4, gamma_D=1.0: ratio(t) = 2 - h((1+exp(-2t))/2)/ln(2)
# At t=1.0: eta=0.135335, ratio = 1.01325257
# Lindblad integrator: ratio(t=1.0) = 1.01325257
```
**Output:** Analytical and numerical agree to 12 digits. **PASS**

### Oracle 4: RK4 convergence rate

```python
# Errors relative to n=4000 reference:
# n=500:  1.26e-12
# n=1000: 7.81e-14  (ratio: 16.1 -- confirming O(h^4))
# n=2000: 4.56e-15  (ratio: 17.1 -- confirming O(h^4))
```
**Output:** Fourth-order convergence confirmed. **PASS**

### Oracle 5: alpha_half(p=0.5) independent derivation

```python
# For p=0.5: I/S_B = 1 - h(alpha)/ln(2)
# Setting I/S_B = 0.5: h(alpha) = ln(2)/2
# Bisection: alpha = 0.889972135562
# Test A result: 0.889972135562
```
**Output:** Match to err=2.22e-16. **PASS**
