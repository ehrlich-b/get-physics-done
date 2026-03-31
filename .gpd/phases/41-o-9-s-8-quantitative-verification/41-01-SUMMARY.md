---
phase: 41-o-9-s-8-quantitative-verification
plan: 01
depth: full
one-liner: "Computed all 5 O(9)-specific quantities (c_s, v_LR, ratio, lattice-BW, CORR-03 correlators) replacing Heisenberg carry-forward values in v10.0 chain links (i)-(l)"
subsystem: [derivation, validation]
tags: [sigma-model, spin-wave, lieb-robinson, bisognano-wichmann, fisher-metric, O(9), S^8]

requires:
  - phase: 39-spontaneous-symmetry-breaking-and-universality-class
    provides: [rho_s = J/8, chi_perp = 1/(2Jz), 8 Type-A Goldstones, Lorentz invariance of sigma model]
  - phase: 38-effective-hamiltonian-from-peirce-multiplication
    provides: [2-site spectrum E/J = {-7/4,...,9/4}, ||h_ij|| = 9J/4]
  - phase: 34-emergent-lorentz-invariance
    provides: [velocity hierarchy template, 4 arguments for c_eff = c_s]
  - phase: 33-fisher-metric-and-smoothness
    provides: [CORR-03 conditional theorem, O(3) correlation function]
provides:
  - "c_s(O(9), Z^3) = J*sqrt(3/2) = 1.225 Ja (classical)"
  - "v_LR(O(9), Z^3) = 27eJ = 73.4 J (NS bound)"
  - "v_LR/c_s = 59.9 (two-tier causal hierarchy)"
  - "Lattice-BW universality applies to O(9) (structural, no SRF number)"
  - "CORR-03 applies to O(9): C(r) = 16/(pi*J*r) for d=3"
  - "Emergent metric ds^2 = -(3J^2/2)dt^2 + g_ij dx^i dx^j"
affects: [40-assembly-all-gaps-closed, paper-v10-derivation-chain]

methods:
  added: [NS Lieb-Robinson bound for general lattice, classical O(N) hydrodynamic formula]
  patterns: [O(3) cross-check for all O(N) formulas, forbidden-proxy audit at each section]

key-files:
  created: [derivations/41-o9-quantitative-results.md]

key-decisions:
  - "Used NS bound formula v_LR = 2e*||h_ij||*z consistently for all lattice comparisons"
  - "Classical-only precision stated honestly; no QMC claim for O(9)"
  - "SRF stated as universality argument, not specific number for O(9)"

patterns-established:
  - "O(N) formulas: always cross-check at N=3 against known Heisenberg values"
  - "Forbidden proxy audit after each derivation section"

conventions:
  - "natural_units=natural (hbar=1, k_B=1, a=1)"
  - "metric_signature=mostly_minus (-,+,+,+) for emergent Lorentzian"
  - "coupling_convention=J_gt_0_AFM"
  - "clifford=Cl(9,0)"
  - "sigma_model_field=O9_n_field on S^8"

plan_contract_ref: ".gpd/phases/41-o-9-s-8-quantitative-verification/41-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-cs:
      status: passed
      summary: "Classical spin-wave velocity c_s(O(9), Z^3) = J*sqrt(3/2) = 1.225 Ja derived from hydrodynamic formula with rho_s = J/8 and chi_perp = 1/(12J). O(3) cross-check passes exactly."
      linked_ids: [deliv-quant-results, test-cs-dimensions, test-o3-crosscheck]
    claim-vlr:
      status: passed
      summary: "Lieb-Robinson velocity v_LR(O(9), Z^3) = 27eJ = 73.4 J from NS bound with ||h_ij|| = 9J/4. Factor of 3 over Heisenberg from ||h_ij|| ratio."
      linked_ids: [deliv-quant-results, test-vlr-gt-cs, test-vlr-dimensions]
    claim-hierarchy:
      status: passed
      summary: "v_LR/c_s = 59.9 >> 1. Two-tier causal structure holds with even wider separation than Heisenberg case."
      linked_ids: [deliv-quant-results, test-vlr-gt-cs]
    claim-bw-universality:
      status: passed
      summary: "Lattice-BW ansatz applies to O(9) by universality (Lorentz invariance from Phase 39). SRF not computed numerically; universality predicts SRF ~ 1."
      linked_ids: [deliv-quant-results, test-bw-structural]
    claim-fisher:
      status: passed
      summary: "CORR-03 applies to O(9) with 8 massless modes. C(r) = 16/(pi*J*r) for d=3. All 4 hypotheses verified (H1 conditional on quantum SSB)."
      linked_ids: [deliv-quant-results, test-fisher-h1h4, test-correlation-dimensions]
  deliverables:
    deliv-quant-results:
      status: passed
      path: "derivations/41-o9-quantitative-results.md"
      summary: "Complete derivation document with all 5 O(9)-specific quantities, cross-checks, dimensional analysis, caveats, and summary comparison table."
      linked_ids: [claim-cs, claim-vlr, claim-hierarchy, claim-bw-universality, claim-fisher]
  acceptance_tests:
    test-cs-dimensions:
      status: passed
      summary: "[c_s] = [sqrt(J*J)] = [J] = [velocity at a=1]. Verified."
      linked_ids: [claim-cs, deliv-quant-results]
    test-o3-crosscheck:
      status: passed
      summary: "N=3: c_s(O(3), Z^2) = 2Ja. Matches known classical value exactly. QMC gives 1.659 Ja (17% quantum correction)."
      linked_ids: [claim-cs, deliv-quant-results]
    test-vlr-gt-cs:
      status: passed
      summary: "v_LR = 73.4 J >> c_s = 1.225 J. Ratio = 59.9. Guaranteed by LR theorem."
      linked_ids: [claim-hierarchy, deliv-quant-results]
    test-vlr-dimensions:
      status: passed
      summary: "[v_LR] = [e*J*dimensionless] = [J] = [velocity at a=1]. Same units as c_s."
      linked_ids: [claim-vlr, deliv-quant-results]
    test-bw-structural:
      status: passed
      summary: "O(9) sigma model is Lorentz invariant (Phase 39). Giudici et al. 2018 validated BW for multiple universality classes. Universality argument applies."
      linked_ids: [claim-bw-universality, deliv-quant-results]
    test-fisher-h1h4:
      status: passed
      summary: "H1: LRO for d>=3 (Phase 39 FSS, conditional on quantum SSB). H2: 8 Type-A Goldstones with c_s > 0. H3: generic (full-rank rho). H4: generic (OBC). All satisfied."
      linked_ids: [claim-fisher, deliv-quant-results]
    test-correlation-dimensions:
      status: passed
      summary: "[C(r)] = [1/(rho_s * r^{d-2})] = [1/(J*a)] at a=1, d=3. Dimensionally consistent."
      linked_ids: [claim-fisher, deliv-quant-results]
  references:
    ref-phase39-sigma:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "rho_s = J/8 and sigma model Lorentz invariance used directly in c_s derivation and BW argument."
    ref-phase38-spectrum:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "2-site spectrum and ||h_ij|| = 9J/4 used directly in v_LR computation."
    ref-phase34-velocity:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Velocity hierarchy template and 4 c_eff arguments replicated for O(9)."
    ref-phase33-corr03:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "CORR-03 hypotheses H1-H4 verified for O(9). Correlation function formula applied with N-1=8."
    ref-nachtergaele-sims:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "NS LR bound formula v_LR = 2e*||h||*z applied to O(9) on Z^3."
    ref-giudici2018:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Multi-class BW validation cited as evidence for universality of BW ansatz."
    ref-arxiv-2511:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited as extending BW validity beyond Lorentz-invariant cases."
  forbidden_proxies:
    fp-heisenberg-carryforward:
      status: rejected
      notes: "No Heisenberg values (1.659, 0.181, 0.0657, 12.66) used for O(9). All replaced with O(9)-specific derivations."
    fp-srf-number:
      status: rejected
      notes: "SRF=0.9993 NOT claimed for O(9). Only universality argument stated."
    fp-qmc-precision:
      status: rejected
      notes: "Classical-only precision stated with honest caveat. No QMC claim."
    fp-wrong-n:
      status: rejected
      notes: "N=9 used consistently. Target S^8 from Spin(9)->Spin(8), not N=17 or OP^2."
  uncertainty_markers:
    weakest_anchors:
      - "Classical c_s may overestimate quantum value by ~20% (O(3) analogy)"
      - "No QMC exists for O(9) lattice models"
      - "NS bound is not tight; v_LR overestimates true propagation speed"
    unvalidated_assumptions:
      - "Quantum SSB for O(9) (S_eff=1/2, BCS fails)"
    competing_explanations: []
    disconfirming_observations: []

comparison_verdicts:
  - subject_id: claim-cs
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-phase39-sigma
    comparison_kind: cross_method
    metric: "O(3) cross-check at N=3"
    threshold: "exact match with known classical value"
    verdict: pass
    recommended_action: "none"
    notes: "c_s(O(3), Z^2) = 2Ja from same formula. Matches known classical O(3) spin-wave velocity exactly."
  - subject_id: claim-vlr
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-nachtergaele-sims
    comparison_kind: benchmark
    metric: "v_LR > c_s (theorem guarantee)"
    threshold: "strict inequality"
    verdict: pass
    recommended_action: "none"
    notes: "73.4 J >> 1.225 J. Factor of 3 over Heisenberg consistent with ||h_ij|| ratio."

duration: 5min
completed: 2026-03-30
---

# Phase 41: O(9)/S^8 Quantitative Verification Summary

**Computed all 5 O(9)-specific quantities (c_s, v_LR, ratio, lattice-BW, CORR-03 correlators) replacing Heisenberg carry-forward values in v10.0 chain links (i)-(l)**

## Performance

- **Duration:** ~5 min
- **Started:** 2026-03-31T02:23:16Z
- **Completed:** 2026-03-31T02:27:51Z
- **Tasks:** 2
- **Files modified:** 1

## Key Results

- c_s(O(9), Z^3) = J*sqrt(3/2) = 1.225 Ja (classical; O(3) cross-check passes) [CONFIDENCE: MEDIUM -- classical-only]
- v_LR(O(9), Z^3) = 27eJ = 73.4 J (NS bound; factor of 3 over Heisenberg) [CONFIDENCE: HIGH]
- v_LR/c_s = 59.9 >> 1 (two-tier causal structure holds with wider separation) [CONFIDENCE: HIGH]
- Lattice-BW applies to O(9) by universality; SRF not computed [CONFIDENCE: HIGH -- structural]
- CORR-03 applies to O(9): C(r) = 16/(pi*J*r) for d=3 with 8 Goldstone modes [CONFIDENCE: MEDIUM -- conditional on quantum SSB]

## Task Commits

1. **Task 1: c_s, v_LR, velocity hierarchy** - `67444fc` (derive)
2. **Task 2: lattice-BW, CORR-03, correlation prefactors, emergent metric** - `a39956f` (derive)

## Files Created/Modified

- `derivations/41-o9-quantitative-results.md` - All 5 O(9)-specific quantities with derivations, cross-checks, and comparison table

## Equations Derived

**Eq. (41.1):** rho_s(O(9)) = J/8 = 0.125 J

**Eq. (41.6):** c_s(O(9), Z^3) = J*sqrt(3/2) = 1.225 Ja

**Eq. (41.9):** v_LR(O(9), Z^3) = 27eJ = 73.4 J

**Eq. (41.12):** v_LR/c_s = 59.9

**Eq. (41.17):** H_ent(O(9)) = (2pi/c_s(O(9))) sum x_perp h_x

**Eq. (41.23):** C(r)|_{d=3} = 16/(pi*J*r) for O(9)

**Eq. (41.25):** ds^2 = -(3J^2/2)dt^2 + g_ij dx^i dx^j

## Validations Completed

- O(3) cross-check: setting N=3 in all O(N) formulas recovers known classical Heisenberg values exactly
- Dimensional analysis verified for all 5 quantities + correlator + metric
- v_LR > c_s confirmed (guaranteed by LR theorem)
- Large-N check: c_s decreases with N at fixed lattice (correct)
- No Heisenberg-specific numbers (1.659, 0.181, 0.0657, 12.66, 0.9993) in O(9) results
- All 4 forbidden proxies explicitly rejected with documentation

## Decisions & Deviations

None - followed plan as specified.

## Open Questions

- Quantum corrections to c_s for O(9) remain unknown (no QMC exists). ~20% reduction expected by O(3) analogy.
- SRF for O(9) not computable without numerical simulation (ED/DMRG/QMC).

## Next Phase Readiness

All 5 O(9)-specific values now available for v10.0 derivation chain links (i)-(l). The summary comparison table in the derivation document provides a complete mapping from Heisenberg (v9.0) to O(9) (v10.0) values.

## Contract Coverage

- Claim IDs advanced: claim-cs -> passed, claim-vlr -> passed, claim-hierarchy -> passed, claim-bw-universality -> passed, claim-fisher -> passed
- Deliverable IDs produced: deliv-quant-results -> derivations/41-o9-quantitative-results.md
- Acceptance test IDs run: all 7 tests passed
- Reference IDs surfaced: all 7 references completed
- Forbidden proxies rejected: all 4 rejected
- Decisive comparison verdicts: claim-cs O(3) cross-check pass, claim-vlr benchmark pass

## Self-Check: PASSED

- [x] derivations/41-o9-quantitative-results.md exists and contains all 5 quantities
- [x] Checkpoint 67444fc exists (Task 1)
- [x] Checkpoint a39956f exists (Task 2)
- [x] All forbidden proxies explicitly audited
- [x] Contract IDs: all claims, deliverables, tests, references, proxies have entries

---

_Phase: 41-o-9-s-8-quantitative-verification_
_Completed: 2026-03-30_
