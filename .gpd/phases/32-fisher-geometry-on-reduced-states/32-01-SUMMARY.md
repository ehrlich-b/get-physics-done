---
phase: 32-fisher-geometry-on-reduced-states
plan: 01
depth: full
one-liner: "SLD Fisher metric on Heisenberg OBC ground state is positive-definite at all interior points but distance ratio d_Fisher/d_lattice -> 0 as N -> infinity"
subsystem: [numerics, computation]
tags: [fisher-metric, quantum-information, heisenberg-chain, exact-diagonalization, SLD, bures]

requires:
  - phase: 11-numerical-verification
    provides: ED infrastructure (ed_entanglement.py), Hamiltonian constructors, partial_trace

provides:
  - QFIM computation module (code/fisher_metric.py) with SLD eigendecomposition, Bures cross-check, geodesic distance
  - Test suite (tests/test_fisher_metric.py) with 14 tests: TFI benchmark, SLD-Bures, PBC zero, positivity, trace
  - Numerical Fisher metric data for SWAP/Heisenberg 1D OBC at N=8,12,16,20 with |Lambda|=2,3
  - Finite-size scaling: g_bulk ~ N^{-2.75} for |Lambda|=2, N^{-3.87} for |Lambda|=3
  - Key negative result: d_Fisher/d_lattice -> 0 as N -> infinity (boundary-dominated metric)

affects: [32-02, 33-correlation-structure, 34-emergent-lorentz]

methods:
  added: [SLD-QFIM-eigendecomposition, Bures-fidelity-metric, central-finite-difference]
  patterns: [reduced-state-sweep, SLD-Bures-cross-validation, PBC-zero-sanity-check]

key-files:
  created:
    - code/fisher_metric.py
    - tests/test_fisher_metric.py
    - data/fisher/fisher_swap_1d.json

key-decisions:
  - "Bures cross-check uses central difference (rho_{x-1}, rho_{x+1}) to match SLD parameterization"
  - "SLD=4*Bures identity tested in infinitesimal limit (dh=0.001) for rigorous validation; lattice has O(a^2) corrections"
  - "TFI benchmark uses bulk points (center of chain) to avoid boundary-dominated averages"

patterns-established:
  - "compute_fisher_pipeline: full pipeline from Hamiltonian to metric profile"
  - "SLD-Bures infinitesimal cross-check as gold-standard algorithm validation"
  - "PBC zero check as translation-invariance sanity test"

conventions:
  - "units=natural, hbar=1, k_B=1"
  - "lattice_spacing=1"
  - "fisher_metric=SLD"
  - "normalization=g_F_equals_4_times_g_Bures (infinitesimal limit)"
  - "eigenvalue_threshold=1e-14"
  - "boundary=OBC for physics, PBC for sanity check only"
  - "coupling=J>0 antiferromagnetic"
  - "finite_difference=central, dx=(rho_{x+1}-rho_{x-1})/2"

plan_contract_ref: ".gpd/phases/32-fisher-geometry-on-reduced-states/32-01-PLAN.md#/contract"

contract_results:
  claims:
    claim-fisher-numerical:
      status: partial
      summary: "SLD Fisher metric g(x) is positive-definite at all interior points for N=8-20 OBC. However, d_Fisher/d_lattice does NOT converge to a positive constant; it decays as N^{-1.37} for |Lambda|=2. Distance recovery fails in original form."
      linked_ids: [deliv-fisher-code, deliv-fisher-data, test-sld-bures, test-pbc-zero, test-positive-definite, test-distance-ratio, test-tfi-benchmark, ref-braunstein-caves1994, ref-zanardi2007]
    claim-fisher:
      status: partial
      summary: "Reduced states rho_Lambda(x) form a family with positive-definite Fisher metric at finite N, but the metric does not recover lattice distance in the thermodynamic limit. Positive-definiteness established numerically; smoothness confirmed by non-zero g at all interior points."
      linked_ids: [deliv-fisher-code, deliv-fisher-data, test-positive-definite, ref-braunstein-caves1994, ref-paper5, ref-paper6]
  deliverables:
    deliv-fisher-code:
      status: passed
      path: "code/fisher_metric.py"
      summary: "QFIM module with compute_qfim (SLD), compute_bures_metric, fisher_geodesic_distance, compute_distance_ratios, compute_fisher_pipeline. All required functions present."
      linked_ids: [claim-fisher-numerical, claim-fisher, test-sld-bures, test-tfi-benchmark]
    deliv-fisher-tests:
      status: passed
      path: "tests/test_fisher_metric.py"
      summary: "14 tests covering TFI benchmark, SLD-Bures (infinitesimal + lattice), PBC zero, positivity, trace preservation, geodesic distance. All pass."
      linked_ids: [claim-fisher-numerical, test-sld-bures, test-pbc-zero, test-tfi-benchmark]
    deliv-fisher-data:
      status: passed
      path: "data/fisher/fisher_swap_1d.json"
      summary: "Full Fisher metric data for N=8,12,16,20 with |Lambda|=2,3. Includes g profiles, eigenvalue data, distance ratios, finite-size scaling, power-law fits, physics analysis."
      linked_ids: [claim-fisher-numerical, test-positive-definite, test-distance-ratio]
  acceptance_tests:
    test-sld-bures:
      status: passed
      summary: "SLD = 4*Bures verified to rel_err < 1e-4 in infinitesimal limit (dh=0.001). On discrete lattice (a=1), O(a^2) corrections give factor-of-2 disagreement near boundaries but same-order-of-magnitude consistency throughout."
      linked_ids: [claim-fisher-numerical, deliv-fisher-code, ref-braunstein-caves1994, ref-safranek2017]
    test-pbc-zero:
      status: passed
      summary: "max|g| < 1e-12 on PBC for N=8,12. Translation invariance verified."
      linked_ids: [claim-fisher-numerical, deliv-fisher-code]
    test-positive-definite:
      status: passed
      summary: "g(x) > 0 at all interior points for all N=8,12,16,20 and |Lambda|=2,3. Exception: reflection-symmetry zero at chain center for |Lambda|=2 (d_x rho = 0 by mirror symmetry)."
      linked_ids: [claim-fisher-numerical, deliv-fisher-data]
    test-distance-ratio:
      status: failed
      summary: "d_Fisher/d_lattice does NOT converge to a positive constant. Ratio decays as N^{-1.37} for |Lambda|=2, N^{-1.94} for |Lambda|=3. Bulk Fisher metric vanishes as N -> infinity because the 1D Heisenberg ground state becomes translation-invariant in the thermodynamic limit."
      linked_ids: [claim-fisher-numerical, deliv-fisher-data]
    test-tfi-benchmark:
      status: passed
      summary: "Bulk Fisher metric at h/J=1.0 exceeds h/J=0.5 and h/J=1.5 for both |Lambda|=2,3 at N=12. Critical enhancement at quantum phase transition confirmed (Zanardi 2007)."
      linked_ids: [claim-fisher-numerical, deliv-fisher-tests, ref-zanardi2007]
  references:
    ref-braunstein-caves1994:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "SLD Fisher metric definition and g_F = 4*g_Bures identity used throughout. Verified numerically in infinitesimal limit."
    ref-zanardi2007:
      status: completed
      completed_actions: [compare]
      missing_actions: []
      summary: "Fisher metric critical enhancement at TFI QPT (h/J=1) reproduced as benchmark. Bulk metric at criticality exceeds off-critical values."
    ref-safranek2017:
      status: completed
      completed_actions: [cite]
      missing_actions: [read]
      summary: "Rank-deficient handling implemented via eigenvalue threshold. Bures metric used as continuous extension at rank changes."
    ref-paper5:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "M_n(C)^sa finite-dimensional observer constrains subsystem dimension. Used |Lambda|=2,3 as finite subsystem sizes."
    ref-paper6:
      status: completed
      completed_actions: [cite]
      missing_actions: [read]
      summary: "SWAP lattice definition and OBC requirement. Used Heisenberg OBC (same ground state as SWAP) from existing ED infrastructure."
  forbidden_proxies:
    fp-product-states:
      status: rejected
      notes: "All computations use the entangled Heisenberg ground state (Bethe ansatz singlet), not product states."
    fp-trivial-metric:
      status: rejected
      notes: "Metric shows strong position dependence: boundary peaks, sublattice alternation for |Lambda|=2, power-law decay into bulk. Not a trivial scalar multiple of delta_ij."
    fp-nearest-only:
      status: rejected
      notes: "Distance ratios computed for ALL bulk pairs at all separations, not just nearest-neighbor."
    fp-pbc-physics:
      status: rejected
      notes: "PBC used only as sanity check (g=0 verified). All physics results use OBC."
  uncertainty_markers:
    weakest_anchors:
      - "Full-rank assumption verified numerically but not proved analytically"
      - "Finite-size scaling fit (4 points) -- power law exponent has ~10% uncertainty"
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations:
      - "Distance ratio -> 0 as N -> inf: metric does not recover lattice distance in thermodynamic limit"

comparison_verdicts:
  - subject_id: test-sld-bures
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-braunstein-caves1994
    comparison_kind: cross_method
    metric: relative_error
    threshold: "<= 1e-4 (infinitesimal limit)"
    verdict: pass
    recommended_action: "None -- identity verified"
    notes: "Infinitesimal test (dh=0.001) gives rel_err=6.8e-6. Lattice (a=1) has O(a^2) corrections."
  - subject_id: test-tfi-benchmark
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-zanardi2007
    comparison_kind: benchmark
    metric: ordering
    threshold: "g(h=1) > g(h=0.5) and g(h=1) > g(h=1.5)"
    verdict: pass
    recommended_action: "None -- benchmark reproduced"
  - subject_id: test-distance-ratio
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-paper6
    comparison_kind: convergence
    metric: "std(ratio)/mean(ratio)"
    threshold: "< 0.1 for N >= 16"
    verdict: fail
    recommended_action: "Ratio -> 0. Consider rescaled metric, different parameterization, or 2D lattice."
    notes: "1D Heisenberg OBC: bulk becomes translation-invariant as N -> inf, so spatial Fisher metric vanishes. This is a genuine physics result, not an algorithm bug."

duration: 12min
completed: 2026-03-30
---

# Phase 32, Plan 01: QFIM Implementation and SWAP Lattice Fisher Metric

**SLD Fisher metric on Heisenberg OBC ground state is positive-definite at all interior points but distance ratio d_Fisher/d_lattice -> 0 as N -> infinity**

## Performance

- **Duration:** 12 min
- **Started:** 2026-03-30T01:51:38Z
- **Completed:** 2026-03-30T02:03:00Z
- **Tasks:** 2
- **Files modified:** 3

## Key Results

- Fisher metric g(x) > 0 at ALL interior lattice points for N=8,12,16,20 with |Lambda|=2,3 [CONFIDENCE: HIGH]
- SLD = 4*Bures identity verified to rel_err < 7e-6 in infinitesimal limit [CONFIDENCE: HIGH]
- PBC Fisher metric = 0 to machine precision (translation invariance) [CONFIDENCE: HIGH]
- TFI critical enhancement reproduced: g_bulk(h=1) >> g_bulk(h=0.5) and g_bulk(h=1.5) [CONFIDENCE: HIGH]
- **Key negative result:** d_Fisher/d_lattice -> 0 as N -> infinity. g_bulk ~ N^{-2.75} for |Lambda|=2, N^{-3.87} for |Lambda|=3 [CONFIDENCE: MEDIUM -- 4-point power-law fit]
- Reflection symmetry zero: g(x_center) = 0 exactly for |Lambda|=2, even N (mirror plane) [CONFIDENCE: HIGH]
- Strong sublattice alternation for |Lambda|=2 (even/odd ratio ~0.3-0.5); none for |Lambda|=3 [CONFIDENCE: HIGH]

## Task Commits

1. **Task 1: Implement QFIM module and validate on TFI benchmark** - `c41a23e` (implement)
2. **Task 2: Compute Fisher metric on SWAP lattice and analyze distance recovery** - `5e3d0b4` (compute)

## Files Created/Modified

- `code/fisher_metric.py` - QFIM module: SLD eigendecomposition, Bures cross-check, geodesic distance, distance ratios
- `tests/test_fisher_metric.py` - 14 tests: TFI benchmark, SLD-Bures (infinitesimal + lattice), PBC zero, positivity, trace, distance
- `data/fisher/fisher_swap_1d.json` - Full numerical data for N=8,12,16,20 with analysis

## Next Phase Readiness

- Fisher metric module ready for Plan 02 analytical work
- Positive-definiteness (FISH-02) established -- available for downstream phases
- Distance recovery (FISH-03) FAILS in original form -- Plan 02 needs to address this
- Data stored for Phase 33 (correlation structure) analysis
- Options for salvaging distance recovery: (1) N-dependent rescaling, (2) different parameterization, (3) 2D lattice where bulk structure persists

## Contract Coverage

- claim-fisher-numerical -> partial (positive-definite YES, distance recovery NO)
- claim-fisher -> partial (positive-definite YES, smooth manifold YES, distance recovery NO)
- deliv-fisher-code -> passed
- deliv-fisher-tests -> passed
- deliv-fisher-data -> passed
- test-sld-bures -> passed
- test-pbc-zero -> passed
- test-positive-definite -> passed
- test-distance-ratio -> FAILED (ratio -> 0, not -> const > 0)
- test-tfi-benchmark -> passed
- ref-braunstein-caves1994 -> completed (cited)
- ref-zanardi2007 -> completed (compared)
- ref-safranek2017 -> completed (cited, method used)
- ref-paper5 -> completed (cited)
- ref-paper6 -> completed (cited)
- fp-product-states -> rejected
- fp-trivial-metric -> rejected
- fp-nearest-only -> rejected
- fp-pbc-physics -> rejected

## Equations Derived

**Eq. (32.1): SLD Fisher metric (1D, central difference)**

$$
g(x) = \sum_{m,n:\, p_m + p_n > \epsilon} \frac{2\,|\langle m|\partial_x \rho|n\rangle|^2}{p_m + p_n}, \quad \partial_x \rho \approx \frac{\rho_{x+1} - \rho_{x-1}}{2}
$$

**Eq. (32.2): Fisher geodesic distance**

$$
d_\mathrm{Fisher}(x_1, x_2) = \sum_{x=x_1}^{x_2-1} \sqrt{g(x)} \cdot a, \quad a = 1
$$

**Eq. (32.3): Bulk Fisher metric scaling**

$$
g_\mathrm{bulk}(N) \sim A \cdot N^{-\alpha}, \quad \alpha \approx \begin{cases} 2.75 & |\Lambda|=2 \\ 3.87 & |\Lambda|=3 \end{cases}
$$

## Validations Completed

- SLD = 4*Bures in infinitesimal limit (dh=0.001): rel_err = 6.8e-6
- PBC Fisher metric = 0 to machine precision (N=8, 12)
- TFI critical enhancement at h/J=1 (Zanardi 2007 benchmark)
- Tr(rho_x) = 1 to 1e-14 at all positions
- All eigenvalues of rho_x >= 0 at all positions
- Reflection symmetry of g(x) profile (g(x) = g(N-|Lambda|-x) for all N)
- 14 pytest tests all passing

## Decisions & Deviations

### Decisions

- **Bures central-difference matching:** Bures metric computed using F(rho_{x-1}, rho_{x+1}) with parameter separation 2a, matching the SLD central-difference convention. This gives g_Bures = ds^2_B / (2a)^2 and the identity g_SLD = 4*g_Bures in the infinitesimal limit.
- **TFI benchmark uses bulk points:** Mean over full chain is boundary-dominated for small N. Using central 3 points isolates the bulk critical enhancement signal.
- **SLD-Bures lattice tolerance relaxed:** Identity has O(a^2) corrections on discrete lattice (a=1). Infinitesimal test (dh=0.001) is the rigorous cross-validation; lattice test checks same order of magnitude.

### Auto-fixed Issues

**1. [Rule 1 - Code] Fixed Bures metric parameterization mismatch**

- **Found during:** Task 1 (SLD-Bures cross-validation)
- **Issue:** Initial Bures computation used forward difference (rho_x, rho_{x+1}) while SLD uses central difference (rho_{x-1}, rho_{x+1}). Parameterization mismatch gave large disagreement.
- **Fix:** Changed Bures to use F(rho_{x-1}, rho_{x+1}) with parameter separation 2a to match SLD central difference.
- **Files modified:** code/fisher_metric.py
- **Verification:** Infinitesimal test now passes with rel_err < 1e-4
- **Committed in:** c41a23e

**Total deviations:** 1 auto-fixed (Rule 1, code bug)
**Impact on plan:** Necessary correctness fix. No scope change.

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
|----------|--------|-------|-------------|--------|-------------|
| Bulk Fisher metric (|Lambda|=2) | g_bulk | 5.64e-5 (N=20) | power-law fit error ~10% | SLD eigendecomposition | N=8-20 |
| Bulk Fisher metric (|Lambda|=3) | g_bulk | 7.46e-5 (N=20) | power-law fit error ~10% | SLD eigendecomposition | N=8-20 |
| Scaling exponent (|Lambda|=2) | alpha | 2.75 | ~0.3 (4-point fit) | log-log linear fit | N=8-20 |
| Scaling exponent (|Lambda|=3) | alpha | 3.87 | ~0.4 (4-point fit) | log-log linear fit | N=8-20 |
| Sublattice ratio (|Lambda|=2, N=20) | g_even/g_odd | 0.47 | exact (numerical) | direct computation | N=8-20 |
| Distance ratio (|Lambda|=3, N=20) | d_F/d_latt | 0.0065 | cv=0.35 | geodesic sum | N=20 bulk |

## Approximations Used

| Approximation | Valid When | Error Estimate | Breaks Down At |
|---------------|-----------|----------------|----------------|
| Central finite difference | Lattice parameterization | Exact on discrete lattice | N/A |
| Eigenvalue threshold 1e-14 | Full-rank rho | 0 (all rho full-rank in bulk) | Near rank deficiency |
| Power-law scaling fit | N=8-20 | R^2 > 0.98 | N < 8 or N >> 100 (unknown) |

## Open Questions

- Can d_Fisher/d_lattice be rescued by N-dependent rescaling (e.g., N^{alpha/2} * g)?
- Does the 2D Heisenberg lattice give a non-vanishing bulk Fisher metric? (2D has true long-range Neel order at T=0)
- Is the correct distance measure not d_Fisher but rather d_Fisher / d_Fisher(boundary), normalizing to the boundary scale?
- Should the parameterization use a continuous interpolation parameter instead of discrete lattice position?
- What is the role of the sublattice alternation for |Lambda|=2 -- is it related to the Neel order parameter?

## Issues Encountered

None beyond the Bures parameterization mismatch (auto-fixed, see Deviations).

## User Setup Required

None - no external configuration required.

---

_Phase: 32-fisher-geometry-on-reduced-states_
_Plan: 01_
_Completed: 2026-03-30_
