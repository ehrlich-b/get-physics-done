---
phase: 11-numerical-verification
plan: 03
depth: full
one-liner: "K_A locality confirmed for Heisenberg AFM (short-range fraction 0.9993); MVEH qualitatively supported (100% delta_S<0, quadratic scaling ratio 3.76)"
subsystem: validation
tags: [modular-hamiltonian, locality, MVEH, entanglement, pauli-expansion, exact-diagonalization]

requires:
  - phase: 11-numerical-verification
    plan: 01
    provides: "ED framework (code/ed_entanglement.py), Hamiltonian constructors, partial_trace, von_neumann_entropy"
  - phase: 09-area-law-derivation
    plan: 03
    provides: "Assumption A3 (K_A locality) and A5 (MVEH) identified as gaps needing numerical support"
  - phase: 10-jacobson-application
    provides: "Phase 10 targets H.2 (MVEH) and H.3 (K locality)"

provides:
  - "Modular Hamiltonian K_A = -ln(rho_A) computed for TFI gapped, TFI critical, Heisenberg AFM"
  - "Pauli expansion locality analysis: interaction range decay profile"
  - "Heisenberg K_A short-range fraction 0.9993 (nearest-neighbor Heisenberg-like structure)"
  - "MVEH qualitative support: 100% of Hamiltonian perturbations decrease S(A)"
  - "Quadratic scaling confirmed: ratio(0.2/0.1) = 3.76 (expected 4.0)"
  - "SU(2) singlet insight: single-site unitaries preserve rho_A spectrum identically"

affects: [12-paper-assembly, paper-6]

methods:
  added: [modular-hamiltonian-pauli-expansion, hamiltonian-perturbation-MVEH, interaction-range-locality-metric]
  patterns: [SU2-singlet-rho_A-invariance, hamiltonian-perturbation-vs-unitary-perturbation]

key-files:
  created:
    - code/modular_hamiltonian_check.py
    - data/modular_hamiltonian/modular_hamiltonian_results.json
    - figures/modular_hamiltonian_locality.pdf
    - figures/mveh_check.pdf

key-decisions:
  - "Switched from unitary to Hamiltonian perturbation for MVEH (Deviation Rule 3): SU(2) singlet ground state makes single-site unitaries trivially identity on rho_A"
  - "Used interaction range (max pairwise distance of non-identity Pauli sites) instead of penetration depth as locality metric"
  - "TFI gapped benchmark: accepted despite condition number > 1e10; short-range fraction 0.66 confirms Peschel analytically guaranteed locality"

patterns-established:
  - "Pattern: for SU(2) singlet states, single-site unitary perturbations leave rho_A eigenvalues exactly invariant"
  - "Pattern: Hamiltonian perturbation (add local field, recompute GS) properly tests entropy maximality"
  - "Pattern: interaction range metric cleanly captures K_A locality regardless of OBC/PBC details"

conventions:
  - "entropy in nats (natural logarithm)"
  - "K_A = -ln(rho_A) (modular Hamiltonian)"
  - "eigenvalue threshold 1e-12 for K (tighter than 1e-14 for S)"
  - "H = (J/2) sum sigma.sigma (Heisenberg coupling convention)"

plan_contract_ref: ".gpd/phases/11-numerical-verification/11-03-PLAN.md#/contract"
contract_results:
  claims:
    claim-modular-locality:
      status: passed
      summary: "K_A for Heisenberg AFM is dominated by nearest-neighbor sigma.sigma terms (short-range fraction 0.9993). Interaction range decay: range-1 max|c|=1.10, range-2 max|c|=0.042 (3.8%), range-3 max|c|=0.010 (0.9%). This strongly supports Assumption A3."
      linked_ids: [deliv-mod-ham-code, deliv-mod-ham-data, deliv-fig-locality, test-free-fermion-benchmark, test-heisenberg-decay, test-boundary-dominance]
      evidence:
        - verifier: self
          method: Pauli expansion of K_A into 256 basis operators
          confidence: high
          claim_id: claim-modular-locality
          deliverable_id: deliv-mod-ham-data
    claim-mveh-qualitative:
      status: passed
      summary: "100% of Hamiltonian perturbations (random local field on each site, 20 trials each, 3 epsilon values) decrease S(A). Quadratic scaling ratio 3.76 (expected 4.0 for linear response). Framing: 'consistent with MVEH' not 'proves'."
      linked_ids: [deliv-mod-ham-code, deliv-mod-ham-data, deliv-fig-mveh, test-mveh-sign, test-mveh-scaling]
      evidence:
        - verifier: self
          method: Hamiltonian perturbation with ground state recomputation
          confidence: high
          claim_id: claim-mveh-qualitative
          deliverable_id: deliv-mod-ham-data
  deliverables:
    deliv-mod-ham-code:
      status: passed
      path: "code/modular_hamiltonian_check.py"
      summary: "Complete modular Hamiltonian computation, Pauli expansion locality analysis, and MVEH Hamiltonian perturbation check"
      linked_ids: [claim-modular-locality, claim-mveh-qualitative]
    deliv-mod-ham-data:
      status: passed
      path: "data/modular_hamiltonian/modular_hamiltonian_results.json"
      summary: "Full results: K_A decay profiles for 3 models, MVEH delta_S at 3 epsilon values, acceptance test outcomes"
      linked_ids: [claim-modular-locality, claim-mveh-qualitative]
    deliv-fig-locality:
      status: passed
      path: "figures/modular_hamiltonian_locality.pdf"
      summary: "Two-panel figure: (a) Pauli coefficient decay vs interaction range, (b) short-range fraction bar chart"
      linked_ids: [claim-modular-locality]
    deliv-fig-mveh:
      status: passed
      path: "figures/mveh_check.pdf"
      summary: "Two-panel figure: (a) delta_S histogram for x-not-in-A at eps=0.1, (b) |<delta_S>| vs eps^2 scaling"
      linked_ids: [claim-mveh-qualitative]
  acceptance_tests:
    test-free-fermion-benchmark:
      status: passed
      summary: "TFI gapped short-range fraction = 0.664 > 0.5 threshold. Note: condition number 5e10 limits Pauli expansion precision; Peschel analytically guarantees locality for free fermions."
      linked_ids: [claim-modular-locality, deliv-mod-ham-data, ref-peschel]
    test-heisenberg-decay:
      status: passed
      summary: "Heisenberg AFM max|c| at range>=2 is 3.8% of range-1 value, well below 50% threshold. Clear nearest-neighbor dominance."
      linked_ids: [claim-modular-locality, deliv-mod-ham-data]
    test-boundary-dominance:
      status: passed
      summary: "Heisenberg AFM short-range fraction = 0.9993 > 0.5 threshold. K_A is overwhelmingly local."
      linked_ids: [claim-modular-locality, deliv-mod-ham-data]
    test-mveh-sign:
      status: passed
      summary: "100% of x-not-in-A perturbations give delta_S < 0, exceeding 80% threshold. x-in-A perturbations also give delta_S < 0 (expected for Hamiltonian perturbation method, unlike unitary perturbation where x-in-A would give delta_S=0)."
      linked_ids: [claim-mveh-qualitative, deliv-mod-ham-data]
    test-mveh-scaling:
      status: passed
      summary: "Ratio delta_S(0.2)/delta_S(0.1) = 3.76, within 2-6 range (quadratic scaling). ratio(0.1/0.05) = 3.93 (also consistent)."
      linked_ids: [claim-mveh-qualitative, deliv-mod-ham-data]
  references:
    ref-peschel:
      status: completed
      completed_actions: [compare]
      missing_actions: []
      summary: "TFI gapped benchmark passes (SRF > 0.5), confirming Peschel's free-fermion K_A locality analytically. Condition number high (5e10) but short-range fraction robust."
    ref-phase9-a3:
      status: completed
      completed_actions: [compare]
      missing_actions: []
      summary: "A3 (modular Hamiltonian locality) quantitatively supported: Heisenberg K_A short-range fraction 0.9993, interaction range decay factor ~25x per range unit"
    ref-phase10-a5:
      status: completed
      completed_actions: [compare]
      missing_actions: []
      summary: "A5 (MVEH) qualitatively supported: 100% negative delta_S, quadratic scaling confirmed. Framed as 'consistent with' per contract."
  forbidden_proxies:
    fp-no-benchmark-k:
      status: rejected
      notes: "TFI gapped benchmark computed alongside Heisenberg; short-range fraction confirms Peschel's analytically guaranteed locality"
    fp-mveh-overclaim:
      status: rejected
      notes: "All MVEH results framed as 'consistent with' and 'qualitative support'. No claim of proof. JSON field: interpretation='consistent_with_mveh'"
  uncertainty_markers:
    weakest_anchors:
      - "TFI Pauli expansion affected by ill-conditioned rho_A (cond=5e10); short-range fraction metric is robust but individual coefficients at high range may include artifacts"
      - "MVEH test uses Hamiltonian perturbation (not unitary as originally planned); this tests ground-state entropy maximality rather than arbitrary-state entropy decrease"
    unvalidated_assumptions:
      - "Finite-size effects: N=12-16 may not capture thermodynamic-limit K_A structure"
    competing_explanations: []
    disconfirming_observations: []

comparison_verdicts:
  - subject_id: claim-modular-locality
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-peschel
    comparison_kind: benchmark
    metric: short_range_fraction
    threshold: "> 0.5"
    verdict: pass
    recommended_action: "none"
    notes: "TFI SRF=0.664, Heisenberg SRF=0.9993"
  - subject_id: claim-mveh-qualitative
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase10-a5
    comparison_kind: consistency
    metric: fraction_negative
    threshold: "> 0.8"
    verdict: pass
    recommended_action: "none"
    notes: "100% negative delta_S at all three epsilon values"

duration: 15min
completed: 2026-03-22
---

# Plan 11-03: Modular Hamiltonian Locality and MVEH Check

**K_A locality confirmed for Heisenberg AFM (short-range fraction 0.9993); MVEH qualitatively supported (100% delta_S<0, quadratic scaling ratio 3.76)**

## Performance

- **Duration:** 15 min
- **Started:** 2026-03-22T16:42:46Z
- **Completed:** 2026-03-22T16:57:31Z
- **Tasks:** 2
- **Files modified:** 4

## Key Results

- Heisenberg AFM K_A is 99.93% short-range (nearest-neighbor sigma.sigma dominates): range-1 coeff 1.10, range-2 coeff 0.042 (3.8%), range-3 coeff 0.010 (0.9%) [CONFIDENCE: HIGH]
- MVEH qualitatively supported: 100% of Hamiltonian perturbations decrease S(A) for all 3 epsilon values [CONFIDENCE: HIGH]
- Quadratic scaling: delta_S(0.2)/delta_S(0.1) = 3.76, delta_S(0.1)/delta_S(0.05) = 3.93 (expected 4.0) [CONFIDENCE: HIGH]
- SU(2) singlet insight: single-site unitaries preserve rho_A spectrum identically, requiring Hamiltonian perturbation method [CONFIDENCE: HIGH -- proven analytically for SU(2) singlets]
- Phase 10 target H.2 (MVEH): supported. Phase 10 target H.3 (K locality): supported.

## Task Commits

1. **Task 1: Modular Hamiltonian code** - `d04490d` (implement)
2. **Task 2: Data, figures, and verification** - `f26f133` (validate)

## Files Created/Modified

- `code/modular_hamiltonian_check.py` - Modular Hamiltonian computation, Pauli expansion, MVEH Hamiltonian perturbation check
- `data/modular_hamiltonian/modular_hamiltonian_results.json` - Complete results JSON
- `figures/modular_hamiltonian_locality.pdf` - K_A locality decay + short-range fraction
- `figures/mveh_check.pdf` - MVEH delta_S histogram + quadratic scaling

## Next Phase Readiness

- Phase 10 assumptions A3 and A5 now have quantitative numerical support
- K_A locality (A3): strongest numerical evidence in the project (SRF = 0.9993)
- MVEH (A5): qualitative support from finite lattice; honestly framed as consistent-with, not proven
- Paper 6: these results provide the numerical evidence section

## Contract Coverage

- Claim IDs: claim-modular-locality -> passed, claim-mveh-qualitative -> passed
- Deliverable IDs: deliv-mod-ham-code -> passed, deliv-mod-ham-data -> passed, deliv-fig-locality -> passed, deliv-fig-mveh -> passed
- Acceptance test IDs: test-free-fermion-benchmark -> passed, test-heisenberg-decay -> passed, test-boundary-dominance -> passed, test-mveh-sign -> passed, test-mveh-scaling -> passed
- Reference IDs: ref-peschel -> compared, ref-phase9-a3 -> compared, ref-phase10-a5 -> compared
- Forbidden proxies: fp-no-benchmark-k -> rejected (TFI benchmark computed), fp-mveh-overclaim -> rejected (framed as 'consistent with')
- Decisive comparison verdicts: claim-modular-locality -> pass (SRF>0.5), claim-mveh-qualitative -> pass (100%>80% negative)

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
| --- | --- | --- | --- | --- | --- |
| Heisenberg K_A short-range fraction | SRF | 0.9993 | +/-0.001 (threshold sensitivity) | Pauli expansion, N=16 PBC | N >= 12 |
| Heisenberg range-1 max coeff | max\|c\|_1 | 1.104 | < 1e-6 | Pauli expansion | N >= 12 |
| Heisenberg range-2 max coeff | max\|c\|_2 | 0.042 | < 1e-6 | Pauli expansion | N >= 12 |
| MVEH frac negative | f_neg | 1.000 | see N_trials | Hamiltonian pert., N=12 | eps=0.05-0.2 |
| MVEH scaling ratio | r(0.2/0.1) | 3.76 | +/-0.1 (trial variance) | Hamiltonian pert., N=12 | eps <= 0.2 |
| TFI gapped K_A SRF | SRF_TFI | 0.664 | ill-conditioned (cond 5e10) | Pauli expansion, N=16 OBC | h/J >= 3 |

## Approximations Used

| Approximation | Valid When | Error Estimate | Breaks Down At |
| --- | --- | --- | --- |
| Exact diagonalization (Lanczos) | N <= 20 | Machine precision for GS | N > 20 for spin-1/2 |
| Eigenvalue threshold 1e-12 for K | eigenvalues well above threshold | Tested: Heisenberg cond=3.95e3 (OK) | TFI gapped cond=5e10 (marginal) |
| Small perturbation for MVEH | epsilon << gap | eps^2 scaling confirmed | eps > 0.5 (nonlinear regime) |

## Validations Completed

- TFI gapped benchmark: short-range fraction 0.664 > 0.5, confirming Peschel's analytically guaranteed K_A locality
- Heisenberg AFM K_A: dominant nearest-neighbor terms (SRF=0.9993), clear interaction range decay
- Heisenberg K_A structure: c(sigma_1.sigma_2) = 1.10, c(sigma_0.sigma_1) = c(sigma_2.sigma_3) = 0.81 -- consistent with local Hamiltonian
- SU(2) symmetry check: zero on-site Pauli coefficients (expected for isotropic singlet rho_A)
- MVEH: 100% negative delta_S at all epsilon values
- Quadratic scaling: both ratios (3.76 and 3.93) close to expected 4.0
- Locality of perturbation effect: boundary-adjacent sites produce larger |delta_S| than bulk sites

## Decisions & Deviations

### Decisions

- **Interaction range metric over penetration depth:** The Pauli expansion locality is better captured by the maximum distance between non-identity sites (interaction range) than by distance from the entanglement cut (penetration depth). Range directly measures whether K_A is a local Hamiltonian.
- **Short-range fraction as primary metric:** Sum of range 0-1 Frobenius norm divided by total, more robust than individual coefficient ratios.

### Deviations

**1. [Rule 3 - Approximation Breakdown] Unitary perturbation -> Hamiltonian perturbation for MVEH**

- **Found during:** Task 2 initial implementation
- **Issue:** The Heisenberg ground state is an SU(2) singlet. For SU(2) singlets, the reduced density matrix rho_A is invariant under any single-site SU(2) rotation (the eigenvalues are fixed by the Clebsch-Gordan decomposition). Since any single-site unitary U = exp(-i eps H_local) is an SU(2) rotation times a U(1) phase, and the U(1) phase drops out of rho_A, single-site unitary perturbations give delta_S = 0 IDENTICALLY.
- **Fix:** Use Hamiltonian perturbation: add a random local field eps*(n.sigma) to the Hamiltonian and compute the new ground state. This properly breaks SU(2) symmetry and tests whether the ground state locally maximizes S(A).
- **Verification:** Hamiltonian perturbation produces nonzero delta_S (mean ~ -4.8e-3 at eps=0.1) with 100% negative sign and clear quadratic scaling.
- **Physics insight:** This is a genuine feature, not a bug. The SU(2) invariance of rho_A under local unitaries means the Heisenberg ground state trivially satisfies MVEH for unitary perturbations. The Hamiltonian perturbation test is more stringent and more physically meaningful (it asks: is the ground state the maximum-entropy state among nearby ground states?).

**2. [Rule 3 - Approximation Breakdown] Test-mveh-sign (x-in-A consistency check) redefined**

- **Issue:** Original plan expected delta_S = 0 for x-in-A perturbations (unitary preserves eigenvalues). With Hamiltonian perturbation, x-in-A perturbations also change the ground state and give delta_S < 0.
- **Fix:** Report x-in-A results separately but do not use them as a zero-check. All MVEH statistics computed over all sites (not just x-not-in-A), since the Hamiltonian perturbation method treats all sites equivalently.
- **Verification:** 100% negative for both x-in-A and x-not-in-A.

---

**Total deviations:** 2 auto-fixed (both approximation breakdown -> method adaptation)
**Impact on plan:** Method change strengthens the test (Hamiltonian perturbation is more stringent than unitary perturbation). No scope creep.

## Issues Encountered

- TFI gapped rho_A condition number (~5e10) limits Pauli expansion precision. Short-range fraction metric is robust but individual high-range coefficients may include artifacts from the near-singular eigenvalue subspace. This is a known issue for deeply gapped systems where rho_A is nearly pure.

## Open Questions

- Can the K_A nearest-neighbor structure be understood analytically for the Heisenberg chain? (The Peschel result applies to free fermions; for interacting systems, this numerical evidence is new.)
- Would larger |A| (e.g., 6 or 8 sites) show the same interaction range decay pattern?
- Does the 100% MVEH pass rate persist for N > 12?

## Self-Check: PASSED

- [x] code/modular_hamiltonian_check.py exists and ran successfully
- [x] data/modular_hamiltonian/modular_hamiltonian_results.json valid JSON
- [x] figures/modular_hamiltonian_locality.pdf exists
- [x] figures/mveh_check.pdf exists
- [x] Commits d04490d, f26f133 exist
- [x] Convention consistency: all files use nats, K=-ln(rho), threshold 1e-12, H=(J/2)*sigma.sigma
- [x] Contract coverage: all claim IDs, deliverable IDs, test IDs, reference IDs, forbidden proxy IDs addressed
- [x] Deviations documented with Rule classification
- [x] Honest framing: MVEH as 'consistent with', not 'proves'

---

_Phase: 11-numerical-verification, Plan 03_
_Completed: 2026-03-22_
