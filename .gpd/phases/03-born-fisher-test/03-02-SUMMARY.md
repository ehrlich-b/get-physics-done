---
phase: 03-born-fisher-test
plan: 02
depth: full
one-liner: "Lindblad dynamics Test B falsifies the Born-Fisher-Experiential conjecture: rho_Q(t) <= 0 throughout all 1900+ trajectories because I_vN/S_vN(B) stays in [1,2], mu_Q identically zero"
subsystem: [numerics, validation]
tags: [lindblad, von-neumann-entropy, quantum-mutual-information, born-rule, experiential-density, decoherence, density-matrix]

requires:
  - phase: 03-born-fisher-test plan 01
    provides: quantum_info.py module (von Neumann entropy, partial trace, QMI, experiential density), Test A static verdict
provides:
  - Lindblad master equation integrator (hand-written RK4, no scipy)
  - Test B numerical verdict on dynamical Born-Fisher-Experiential conjecture
  - Asymmetric extension (Test B+) results
  - d=3 qutrit spot check
  - Combined Test A + Test B final verdict figure
affects: []

methods:
  added: [Lindblad superoperator construction, RK4 ODE integration for density matrices, vectorization via column-stacking]
  patterns: [build superoperator once then matrix-vector multiply per step, store_every parameter for memory management]

key-files:
  created:
    - simulations/born_fisher/lindblad.py
    - simulations/born_fisher/test_b_dynamics.py
    - simulations/born_fisher/test_b_results.json
    - figures/test_b_mu_q.pdf
    - figures/test_b_rho_q_pulse.pdf
    - figures/verdict_summary.pdf

key-decisions:
  - "Hand-written RK4 integrator since scipy is unavailable; validated to O(h^4) convergence"
  - "Exchange Hamiltonian H = g*(sigma_x x sigma_x + sigma_y x sigma_y) as tracking mechanism"
  - "Asymmetric dephasing uses projective collapse ops |k><k| x I rather than sigma_z"
  - "mu_Q integrates only positive part of rho_Q (negative rho_Q is unphysical)"
  - "Ran asymmetric Test B+ even though symmetric result is trivial (mu_Q=0 everywhere)"

conventions:
  - "entropy base: nats (natural logarithm)"
  - "S_vN(rho) = -Tr(rho ln rho)"
  - "I_vN(B;M) = S_vN(B) + S_vN(M) - S_vN(BM)"
  - "rho_Q = I_vN * (1 - I_vN/S_vN(B))"
  - "vectorization: column-stacking vec(rho) = rho.flatten('F')"
  - "time units: dimensionless (1/gamma_D)"

plan_contract_ref: ".gpd/phases/03-born-fisher-test/03-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-born-fisher:
      status: passed
      summary: "Born-Fisher-Experiential conjecture FALSIFIED in the qubit toy model. Both static (Test A) and dynamical (Test B) tests show no special role for Born-rule distributions. Dynamical test is decisive: rho_Q <= 0 throughout all Lindblad evolution because I_vN/S_vN stays in [1,2], making mu_Q identically zero with no selection mechanism."
      linked_ids: [deliv-lindblad-code, deliv-test-b-results, deliv-verdict-figure, test-lindblad-sanity, test-born-fisher-verdict]
      evidence:
        - verifier: self
          method: "1900+ trajectory sweep (1200 symmetric + 700 asymmetric) + 3 d=3 spot checks"
          confidence: high
          claim_id: claim-born-fisher
          deliverable_id: deliv-test-b-results
          acceptance_test_id: test-born-fisher-verdict
  deliverables:
    deliv-lindblad-code:
      status: passed
      path: "simulations/born_fisher/lindblad.py"
      summary: "Lindblad integrator with build_lindblad_superoperator, rk4_step, integrate_lindblad, build_qubit_system, build_asymmetric_system, initial_entangled_state. All 6 validation checks pass."
      linked_ids: [claim-born-fisher, test-lindblad-sanity]
    deliv-test-b-results:
      status: passed
      path: "simulations/born_fisher/test_b_results.json"
      summary: "Complete results: mu_q_curves for 12 (gamma_D, g) combos, theta_max values, asymmetric extension for 7 gamma_ratios, d=3 spot check, FALSIFIED verdict"
      linked_ids: [claim-born-fisher, test-born-fisher-verdict]
    deliv-verdict-figure:
      status: passed
      path: "figures/verdict_summary.pdf"
      summary: "3-panel figure showing ratio dynamics, mu_Q(theta) curves, and asymmetric results with FALSIFIED verdict annotation"
      linked_ids: [claim-born-fisher]
  acceptance_tests:
    test-lindblad-sanity:
      status: passed
      summary: "All 6 checks pass: (1) Tr(rho)=1 to machine precision, (2) all eigenvalues >= -2e-31, (3) pure dephasing rate matches exp(-2*gamma_D*t) to 5e-11, (4) pure-state I_vN = 2*ln(2) to machine precision, (5) late-time state is diagonal (off-diag sum < 2e-9), (6) mu_Q converges between n=2000 and n=4000"
      linked_ids: [deliv-lindblad-code]
    test-born-fisher-verdict:
      status: passed
      summary: "Clear FALSIFIED verdict. Decision tree: rho_Q never positive in any of 1900+ trajectories -> mu_Q identically zero -> no selection mechanism exists. This holds for symmetric, asymmetric, and d=3 systems."
      linked_ids: [deliv-lindblad-code, deliv-test-b-results, deliv-verdict-figure]
  references:
    ref-baez-dolan:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited in test_b_dynamics.py docstring and test_b_results.json as motivation for groupoid cardinality weighting"
    ref-quantum-draft:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Sections 3, 6, 8 used to define rho_Q, state conjecture, and specify Lindblad toy model. The predicted positive rho_Q pulse did not materialize."
  forbidden_proxies:
    fp-lindblad-no-verdict:
      status: rejected
      notes: "A clear FALSIFIED verdict is produced, not just working code. The verdict is documented in test_b_results.json, the terminal output, and the verdict summary figure."
    fp-only-symmetric:
      status: rejected
      notes: "Asymmetric extension (Test B+) was run with 7 gamma_ratio values. All give mu_Q = 0 identically. The falsification holds for both symmetric and asymmetric dephasing."
  uncertainty_markers:
    weakest_anchors: ["The Lindblad generator is a modeling choice. Different generators (e.g., amplitude damping, non-Markovian) could produce different I/S_B trajectories that might enter the rho_Q > 0 regime."]
    unvalidated_assumptions: []
    competing_explanations: ["The conjecture might apply to a different class of quantum channels where decoherence destroys correlations faster than the tracking interaction rebuilds them, producing I < S_B transiently."]
    disconfirming_observations: ["rho_Q(t) <= 0 for all 1900+ trajectories; I_vN/S_vN(B) monotonically decreases from 2 to 1, never entering the physical rho_Q > 0 domain."]

comparison_verdicts:
  - subject_id: claim-born-fisher
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-quantum-draft
    comparison_kind: benchmark
    metric: "mu_Q_max_over_theta"
    threshold: "mu_Q(theta) has interior maximum selecting Born-rule theta"
    verdict: fail
    recommended_action: "Conjecture falsified for this Lindblad model class. If pursuing further, explore non-Markovian or amplitude-damping channels where I/S_B might transiently dip below 1."
    notes: "mu_Q identically zero because rho_Q <= 0 throughout. No selection mechanism exists in this model."

duration: 8min
completed: 2026-03-16
---

# Phase 3 Plan 02: Lindblad Dynamics Test B Summary

**Lindblad dynamics Test B falsifies the Born-Fisher-Experiential conjecture: rho_Q(t) <= 0 throughout all 1900+ trajectories because I_vN/S_vN(B) stays in [1,2], mu_Q identically zero**

## Performance

- **Duration:** 8 min
- **Started:** 2026-03-16T14:47:38Z
- **Completed:** 2026-03-16T14:56:04Z
- **Tasks:** 2
- **Files modified:** 6

## Key Results

- rho_Q(t) <= 0 throughout the ENTIRE Lindblad evolution for ALL tested parameters (1200 symmetric + 700 asymmetric trajectories + 3 d=3 spot checks) [CONFIDENCE: HIGH]
- I_vN(B;M)/S_vN(B) monotonically decreases from 2 (pure entangled) to 1 (perfect tracking), never dropping below 1 [CONFIDENCE: HIGH]
- mu_Q(theta) = integral of max(rho_Q(t), 0) dt = 0 identically for all theta, gamma_D, g [CONFIDENCE: HIGH]
- Lindblad integrator validates: trace preserved to machine precision, PSD to 2e-31, pure dephasing rate matches theory to 5e-11, convergence verified between n=2000 and n=4000 [CONFIDENCE: HIGH]
- d=3 qutrit spot check confirms: same behavior (ratio in [1,2], rho_Q <= 0), not a d=2 artifact [CONFIDENCE: HIGH]
- **FINAL VERDICT: FALSIFIED** -- Born-rule initial states are not selected by mu_Q because mu_Q is identically zero

## Task Commits

1. **Task 1: Lindblad integrator + validation** - `da813cb` (calc: implement with 6/6 validation checks)
2. **Task 2: Test B sweep + verdict** - `bf42c9b` (sim: 1900 trajectories, FALSIFIED) + `f478e53` (fig: 3 PDFs)

## Files Created/Modified

- `simulations/born_fisher/lindblad.py` - Lindblad master equation integrator: superoperator construction, RK4, system builders for symmetric/asymmetric dephasing
- `simulations/born_fisher/test_b_dynamics.py` - Full Test B pipeline: pilot, symmetric sweep, asymmetric extension, d=3 spot check, decision tree, figures
- `simulations/born_fisher/test_b_results.json` - Complete numerical results + FALSIFIED verdict
- `figures/test_b_rho_q_pulse.pdf` - rho_Q(t) time series showing negative-only evolution
- `figures/test_b_mu_q.pdf` - mu_Q(theta) curves (identically zero for all parameter combos)
- `figures/verdict_summary.pdf` - Combined 3-panel verdict figure

## Next Phase Readiness

Phase 3 complete. Both plans executed:
- Plan 01 (Test A static): FALSIFIES STATIC -- Born-rule distributions have no special property at half-saturation for diagonal states
- Plan 02 (Test B dynamics): FALSIFIED -- mu_Q identically zero, no dynamical selection mechanism exists

The Born-Fisher-Experiential conjecture is falsified for this class of Lindblad models. Phase complete, ready for transition.

## Contract Coverage

- Claim IDs advanced: claim-born-fisher -> passed (decisive FALSIFIED verdict)
- Deliverable IDs produced: deliv-lindblad-code -> passed, deliv-test-b-results -> passed, deliv-verdict-figure -> passed
- Acceptance test IDs run: test-lindblad-sanity -> passed (6/6), test-born-fisher-verdict -> passed (FALSIFIED)
- Reference IDs surfaced: ref-baez-dolan -> cited, ref-quantum-draft -> read + cited
- Forbidden proxies rejected: fp-lindblad-no-verdict -> rejected (verdict produced), fp-only-symmetric -> rejected (asymmetric also run)
- Decisive comparison verdicts: claim-born-fisher -> fail (mu_Q identically zero, no selection)

## Equations Derived

No new equations derived. All computations use established formulas from Plan 01 plus:

**Eq. (03.4):** Lindblad master equation

$$\frac{d\rho}{dt} = -i[H_{\mathrm{int}}, \rho] + \sum_k \left( L_k \rho L_k^\dagger - \frac{1}{2}\{L_k^\dagger L_k, \rho\} \right)$$

**Eq. (03.5):** Superoperator form (column-stacking vectorization)

$$\frac{d}{dt}\mathrm{vec}(\rho) = \mathcal{L} \cdot \mathrm{vec}(\rho)$$

where $\mathcal{L} = -i(I \otimes H - H^T \otimes I) + \sum_k (L_k^* \otimes L_k - \frac{1}{2} I \otimes L_k^\dagger L_k - \frac{1}{2} (L_k^\dagger L_k)^T \otimes I)$

**Eq. (03.6):** Trajectory functional

$$\mu_Q(\theta) = \int_0^{T_{\mathrm{final}}} \max(\rho_Q(t), 0) \, dt$$

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
|----------|--------|-------|-------------|--------|-------------|
| mu_Q for any (theta, gamma_D, g) | mu_Q | 0.0 | +/- 1e-15 nat-time | 1900 trajectories | all tested parameters |
| Min ratio I/S_B (any trajectory) | min(I/S_B) | 1.0000 | +/- 1e-15 | all trajectories | all tested parameters |
| Pure dephasing rate | tau_D | 1/(2*gamma_D) | exact (validated to 5e-11) | analytical + numerical | gamma_D > 0 |
| Trace preservation | Tr(rho)-1 | 0.0 | +/- 1e-16 | all trajectories | all tested parameters |

## Approximations Used

| Approximation | Valid When | Error Estimate | Breaks Down At |
|---------------|-----------|----------------|----------------|
| RK4 fixed-step | dt << 1/max(gamma_D, g) | O(dt^4), verified ~1e-18 | dt comparable to timescales |
| Finite integration time T=10/gamma_D | gamma_D*T >> 1 | exp(-10) ~ 5e-5 | slow decoherence |
| Eigenvalue cutoff eps=1e-15 | double precision | < 3e-14 nats | never for d<=3 |

## Figures Produced

| Figure | File | Description | Key Feature |
|--------|------|-------------|-------------|
| Fig. 03.4 | `figures/test_b_rho_q_pulse.pdf` | rho_Q(t) time series for 5 theta values | rho_Q <= 0 throughout; no positive pulse |
| Fig. 03.5 | `figures/test_b_mu_q.pdf` | mu_Q(theta) for all 12 (gamma_D, g) combos | mu_Q identically zero |
| Fig. 03.6 | `figures/verdict_summary.pdf` | Combined verdict: ratio dynamics + mu_Q + asymmetric | FALSIFIED annotation |

## Decisions Made

- Used exchange Hamiltonian g*(sigma_x x sigma_x + sigma_y x sigma_y) as tracking interaction. This produces perfect tracking (I = S_B) at late times for all g > 0.
- Ran asymmetric Test B+ even though symmetric result was already decisive (mu_Q = 0). Asymmetric also gives mu_Q = 0, confirming the result is not an artifact of the symmetric setup.
- For d=3, used the swap operator (sum |ij><ji|) as generalization of the exchange Hamiltonian, and projective dephasing operators |k><k| x I_3.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Code bug] np.trapz removed in numpy 2.x, replaced with np.trapezoid**

- **Found during:** Task 1, validation check (f)
- **Issue:** `np.trapz` no longer exists in numpy 2.4.2
- **Fix:** Changed to `np.trapezoid`
- **Files modified:** simulations/born_fisher/lindblad.py
- **Verification:** Convergence check passes
- **Committed in:** da813cb

**2. [Rule 4 - Missing component] Late-time consistency check adjusted for strong-coupling regime**

- **Found during:** Task 1, validation check (e)
- **Issue:** With g=1 exchange coupling, late-time ratio = 1.0 (perfect tracking). The discrete alpha grid for matching only reached alpha=0.999, giving 1.1% mismatch.
- **Fix:** Added direct off-diagonal magnitude check as alternative consistency verification
- **Files modified:** simulations/born_fisher/lindblad.py
- **Verification:** Off-diagonal sum < 2e-9, confirming late-time state is diagonal
- **Committed in:** da813cb

---

**Total deviations:** 2 auto-fixed (1 code bug, 1 missing component)
**Impact on plan:** Trivial fixes. No scope change.

## Issues Encountered

None.

## Open Questions

- Would a non-Markovian quantum channel or amplitude damping channel produce I/S_B < 1 transiently, enabling a positive rho_Q pulse? This is the only remaining avenue for the conjecture.
- The exchange Hamiltonian always drives the system to perfect tracking (I = S_B). A weaker or different coupling mechanism might produce undercorrelated transients where the conjecture could still hold.
- Is the conjecture fundamentally about a regime (I < S_B) that is never reached in physically motivated quantum channels, or is this specific to the exchange+dephasing model?

## Self-Check: PASSED

- [x] simulations/born_fisher/lindblad.py exists
- [x] simulations/born_fisher/test_b_dynamics.py exists
- [x] simulations/born_fisher/test_b_results.json exists
- [x] figures/test_b_rho_q_pulse.pdf exists
- [x] figures/test_b_mu_q.pdf exists
- [x] figures/verdict_summary.pdf exists
- [x] Commit da813cb exists
- [x] Commit bf42c9b exists
- [x] Commit f478e53 exists
- [x] FINAL_VERDICT in test_b_results.json is "FALSIFIED"
- [x] Contract results complete: all claim/deliverable/test/reference/proxy IDs accounted for
- [x] Comparison verdicts present for claim-born-fisher

---

_Phase: 03-born-fisher-test_
_Completed: 2026-03-16_
