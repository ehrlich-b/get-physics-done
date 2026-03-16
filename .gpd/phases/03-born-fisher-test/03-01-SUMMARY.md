---
phase: 03-born-fisher-test
plan: 01
depth: full
one-liner: "Static diagonal-state Test A falsifies the half-saturation conjecture: alpha_half(p) varies with p but Born-rule distributions show no special property vs non-Born alternatives"
subsystem: [numerics, validation]
tags: [von-neumann-entropy, quantum-mutual-information, born-rule, experiential-density, density-matrix]

requires:
  - phase: none
    provides: standalone computational test (independent of Phases 1-2)
provides:
  - quantum_info.py reusable quantum information module (von Neumann entropy, partial trace, QMI, experiential density, diagonal state constructor)
  - Test A numerical verdict on static half-saturation conjecture
  - alpha_half(p) curve for d=2 and d=3
  - Born vs non-Born comparison across 4 distribution types
affects: [03-02-PLAN]

methods:
  added: [eigenvalue decomposition for von Neumann entropy, bisection root-finding (numpy only, no scipy)]
  patterns: [diagonal BM state parametrization by (p, alpha), alpha_half extraction via root-finding]

key-files:
  created:
    - simulations/born_fisher/quantum_info.py
    - simulations/born_fisher/test_a_static.py
    - simulations/born_fisher/test_a_results.json
    - figures/test_a_heatmap.pdf
    - figures/test_a_alpha_half.pdf
    - figures/test_a_rho_q.pdf

key-decisions:
  - "Used numpy.linalg.eigh for eigenvalue decomposition (Hermitian-specific, numerically stable)"
  - "Implemented bisect_root manually since scipy is unavailable"
  - "Eigenvalue cutoff eps=1e-15 verified stable across 3 thresholds"

conventions:
  - "entropy base: nats (natural logarithm)"
  - "S_vN(rho) = -Tr(rho ln rho)"
  - "I_vN(B;M) = S_vN(B) + S_vN(M) - S_vN(BM)"
  - "rho_Q = I_vN * (1 - I_vN/S_vN(B))"
  - "density matrices: Tr=1, PSD, Hermitian"

plan_contract_ref: ".gpd/phases/03-born-fisher-test/03-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-born-fisher:
      status: partial
      summary: "Test A (static diagonal states) falsifies the static half-saturation conjecture: alpha_half(p) varies with p but Born-rule p=cos^2(theta) shows no distinguishing property compared to non-Born alternatives. Test B (Lindblad dynamics, Plan 02) remains to test the dynamical version."
      linked_ids: [deliv-qubit-code, deliv-test-a-results, deliv-test-a-figures, test-qubit-sanity, test-qubit-static]
  deliverables:
    deliv-qubit-code:
      status: passed
      path: "simulations/born_fisher/quantum_info.py"
      summary: "Module with 7 functions (von_neumann_entropy, partial_trace, quantum_mutual_information, experiential_density, diagonal_bm_state, bisect_root, validate_density_matrix), all 10 sanity checks passing"
    deliv-test-a-results:
      status: passed
      path: "simulations/born_fisher/test_a_results.json"
      summary: "Full (p, alpha) grid data, alpha_half curve, Born vs non-Born comparison, and FALSIFIES STATIC verdict"
    deliv-test-a-figures:
      status: passed
      path: "figures/test_a_heatmap.pdf"
      summary: "Heatmap of I_vN/S_vN ratio, alpha_half comparison plot, and rho_Q heatmap"
  acceptance_tests:
    test-qubit-sanity:
      status: passed
      summary: "All 10 sanity checks pass: Tr/PSD, Bell state I=2ln2, product I=0, S(I/2)=ln2, S(I/3)=ln3, Araki-Lieb 10/10, symmetry I(p)=I(1-p), cutoff stability, perfect tracking ratio=1, no tracking I=0"
      linked_ids: [deliv-qubit-code]
    test-qubit-static:
      status: passed
      summary: "Clear determination: alpha_half(p) varies with p (spread 0.069 for d=2) and Born-rule p=cos^2(theta) has no special property at half-saturation compared to non-Born alternatives. FALSIFIES STATIC."
      linked_ids: [deliv-qubit-code, deliv-test-a-results]
  references:
    ref-baez-dolan:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited as motivation for 1/|Aut(x)| weighting; referenced in test_a_results.json"
    ref-quantum-draft:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Sections 3, 6, 8 used to define rho_Q, state conjecture, and specify toy model"
  forbidden_proxies:
    fp-code-only-no-verdict:
      status: rejected
      notes: "A clear verdict (FALSIFIES STATIC) is produced and documented in test_a_results.json, not just computation code"
  uncertainty_markers:
    weakest_anchors: ["The diagonal-state test reduces to classical Shannon entropy -- the quantum novelty is in the density matrix formalism, not the computation itself"]
    unvalidated_assumptions: ["The static test may miss dynamical features that Test B (Lindblad) could reveal"]
    competing_explanations: []
    disconfirming_observations: ["alpha_half(p) is not constant -- it varies, but Born is not special among the variation"]

comparison_verdicts:
  - subject_id: claim-born-fisher
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-quantum-draft
    comparison_kind: benchmark
    metric: "alpha_half_born_special_property"
    threshold: "Born alpha_half(theta) is constant or has extremum that non-Born lacks"
    verdict: fail
    recommended_action: "Proceed to Test B (Lindblad dynamics, Plan 03-02) for the dynamical version of the conjecture"
    notes: "Born alpha_half has spread 0.069, indistinguishable in character from non-Born-1 (0.069) and non-Born-2 (0.041). No special property found."

duration: 4min
completed: 2026-03-16
---

# Phase 3 Plan 01: Static Diagonal-State Test A Summary

**Static diagonal-state Test A falsifies the half-saturation conjecture: alpha_half(p) varies with p but Born-rule distributions show no special property vs non-Born alternatives**

## Performance

- **Duration:** 4 min
- **Started:** 2026-03-16T14:29:40Z
- **Completed:** 2026-03-16T14:33:40Z
- **Tasks:** 2
- **Files modified:** 6

## Key Results

- alpha_half(p) varies with p for d=2: range [0.890, 0.959], spread 0.069, symmetric about p=0.5 [CONFIDENCE: HIGH]
- Born-rule alpha_half has spread 0.069 vs non-Born-1 spread 0.069, non-Born-2 spread 0.041, non-Born-3 trivially 0 (uniform). No distinguishing property. [CONFIDENCE: HIGH]
- d=3 qutrit alpha_half also varies (spread 0.023, mean 0.848), qualitatively matching d=2. Not a d=2 artifact. [CONFIDENCE: HIGH]
- rho_Q peaks at S_B/4 within 0.002% confirming parabolic structure [CONFIDENCE: HIGH]
- All 10 sanity checks pass to 1e-12 or better [CONFIDENCE: HIGH]

## Task Commits

1. **Task 1: Quantum info utilities** - `e4f7d36` (calc: implement with 10/10 sanity checks)
2. **Task 2: Test A sweep and verdict** - `a02e219` (sim: full sweep + verdict) + `7d0883a` (fig: 3 PDFs)

## Files Created/Modified

- `simulations/born_fisher/quantum_info.py` - Core quantum info module: 7 functions, handles arbitrary dimension d
- `simulations/born_fisher/test_a_static.py` - Full Test A pipeline: pre-analytical check, grid sweep, root-finding, Born comparison, d=3 check, plotting
- `simulations/born_fisher/test_a_results.json` - Numerical results + verdict
- `figures/test_a_heatmap.pdf` - I_vN/S_vN ratio heatmap over (p, alpha) with I=S/2 contour
- `figures/test_a_alpha_half.pdf` - alpha_half vs theta for Born and 3 non-Born distributions
- `figures/test_a_rho_q.pdf` - Experiential density rho_Q heatmap

## Next Phase Readiness

Test A verdict: FALSIFIES STATIC. The static half-saturation conjecture does not distinguish Born from non-Born distributions. Proceed to Plan 03-02 (Test B: Lindblad dynamics) for the dynamical version of the conjecture. The quantum_info.py module is ready for reuse.

## Contract Coverage

- Claim IDs advanced: claim-born-fisher -> partial (static test complete; dynamical test in Plan 02)
- Deliverable IDs produced: deliv-qubit-code -> passed, deliv-test-a-results -> passed, deliv-test-a-figures -> passed
- Acceptance test IDs run: test-qubit-sanity -> passed (10/10), test-qubit-static -> passed (clear verdict)
- Reference IDs surfaced: ref-baez-dolan -> cited, ref-quantum-draft -> read + cited
- Forbidden proxies rejected: fp-code-only-no-verdict -> rejected (verdict produced)
- Decisive comparison verdicts: claim-born-fisher -> fail (Born not special at half-saturation)

## Equations Derived

No new equations derived. All computations use established formulas:

**Eq. (03.1):** Von Neumann entropy

$$S_{\mathrm{vN}}(\rho) = -\mathrm{Tr}(\rho \ln \rho) = -\sum_i \lambda_i \ln \lambda_i$$

**Eq. (03.2):** Quantum mutual information

$$I_{\mathrm{vN}}(B;M) = S_{\mathrm{vN}}(B) + S_{\mathrm{vN}}(M) - S_{\mathrm{vN}}(BM)$$

**Eq. (03.3):** Experiential density

$$\rho_Q = I_{\mathrm{vN}}(B;M) \cdot \left(1 - \frac{I_{\mathrm{vN}}(B;M)}{S_{\mathrm{vN}}(B)}\right)$$

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
|----------|--------|-------|-------------|--------|-------------|
| alpha_half at p=0.5 (d=2) | alpha_half(0.5) | 0.8900 | +/- 1e-12 | bisection root-finding | p in (0,1) |
| alpha_half spread (d=2) | max-min | 0.0693 | +/- 1e-11 | exhaustive sweep (200 pts) | all p in [0.01, 0.99] |
| alpha_half mean (d=2) | mean | 0.9035 | +/- 1e-4 (spread-limited) | 200-point average | all p in [0.01, 0.99] |
| rho_Q peak at p=0.5 | max(rho_Q) | 0.1733 nats | +/- 1e-6 | direct computation | alpha in [0.51, 0.999] |
| S_B/4 at p=0.5 | ln(2)/4 | 0.1733 nats | exact | analytical | - |

## Approximations Used

| Approximation | Valid When | Error Estimate | Breaks Down At |
|---------------|-----------|----------------|----------------|
| Eigenvalue cutoff eps=1e-15 | Always for double precision | < 3e-14 nats | Never for d<=3 |
| Diagonal state ansatz | Fully decohered regime | Exact within ansatz | Significant coherences present |

## Validations Completed

- S_vN(I/2) = ln(2) verified to machine precision
- S_vN(I/3) = ln(3) verified to 2e-16
- Pure Bell state I_vN = 2*ln(2) verified to machine precision
- Product state I_vN = 0 verified exactly
- Araki-Lieb bound 0 <= I_vN <= 2*min(S_B, S_M) verified for 10 random states and full 40,000-point grid
- Symmetry I(p, alpha) = I(1-p, alpha) verified to 2e-16
- Eigenvalue cutoff stability verified across {1e-15, 1e-14, 1e-13}
- Perfect tracking alpha=1 gives ratio=1.0 exactly
- No tracking alpha=0.5 gives I_vN=0 exactly
- rho_Q parabolic peak at S_B/4 confirmed to 0.002%
- All ratios in [0, 1] for diagonal states (no entanglement regime)
- d=3 results qualitatively match d=2

## Decisions Made

- Implemented manual bisection root-finder since scipy is unavailable. Convergence to 1e-12 in <100 iterations.
- Used nonuniform alpha grid (dense near boundaries 0.51 and 0.999) per experiment design specification.
- For d=3 body probabilities: (p, (1-p)/2, (1-p)/2) parametrization preserving single-parameter sweep.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Code bug] Fixed non_born_3 returning array instead of scalar**

- **Found during:** Task 2, Step 3 (Born vs non-Born comparison)
- **Issue:** `non_born_3(theta)` used `np.ones_like(np.atleast_1d(theta))` which returned an array for scalar theta input, causing `float()` conversion to fail
- **Fix:** Changed to return plain `0.5`
- **Files modified:** simulations/born_fisher/test_a_static.py
- **Verification:** Full pipeline runs without error
- **Committed in:** a02e219 (Task 2 commit)

---

**Total deviations:** 1 auto-fixed (1 code bug)
**Impact on plan:** Trivial fix. No scope change.

## Issues Encountered

None.

## Open Questions

- Does the Lindblad dynamics test (Test B, Plan 02) reveal a dynamical property of Born-rule distributions that the static test misses?
- The diagonal-state test reduces to classical Shannon entropy -- is the quantum extension conjecture fundamentally about the transient decoherence regime rather than the late-time diagonal state?
- The p-dependence of alpha_half is symmetric about p=0.5 for d=2. For d=3 with asymmetric body probs, the symmetry breaks. Does this asymmetry carry physical information?

## Self-Check: PASSED

- [x] simulations/born_fisher/quantum_info.py exists
- [x] simulations/born_fisher/test_a_static.py exists
- [x] simulations/born_fisher/test_a_results.json exists
- [x] figures/test_a_heatmap.pdf exists
- [x] figures/test_a_alpha_half.pdf exists
- [x] figures/test_a_rho_q.pdf exists
- [x] Commit e4f7d36 exists
- [x] Commit a02e219 exists
- [x] Commit 7d0883a exists
- [x] Verdict field in test_a_results.json is non-empty
- [x] Contract results complete: all claim/deliverable/test/reference/proxy IDs accounted for

---

_Phase: 03-born-fisher-test_
_Completed: 2026-03-16_
