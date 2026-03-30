---
phase: 39-spontaneous-symmetry-breaking-and-universality-class
plan: 03
depth: full
one-liner: "Constructed O(9) NL sigma model on S^8 = Spin(9)/Spin(8), derived Friedan beta function beta = (7/2pi)g^4, verified asymptotic freedom, proved no topological terms in d<=7"

subsystem: [derivation, formalism]
tags: [sigma-model, asymptotic-freedom, ricci-tensor, homotopy, goldstone-modes, rg-flow, friedan]

requires:
  - phase: 39-spontaneous-symmetry-breaking-and-universality-class
    plan: 01
    provides: "SSB pattern Spin(9)->Spin(8) on S^8, classical SSB proof for d>=3, S_eff=1/2"
provides:
  - "O(9) NL sigma model action on S^8 with spin stiffness rho_s"
  - "Ricci tensor Ric(S^8) = 7g (Einstein manifold, lambda=7)"
  - "Friedan one-loop beta function: mu dg^2/dmu = -(d-2)g^2 + (7/2pi)g^4"
  - "Asymptotic freedom verified for d=2"
  - "Homotopy groups: pi_k(S^8) = 0 for k=1,...,7; no topological terms in d<=7"
  - "Comparison table: S^8 vs OP^2 vs S^2 sigma model properties"
affects: [39-04-uc-verification]

methods:
  added: [friedan-beta-function, symmetric-space-curvature, homotopy-group-analysis]
  patterns: [O(N)-sigma-model-from-SSB-coset, einstein-manifold-ricci-computation]

key-files:
  created:
    - derivations/39-sigma-model.md
  modified: []

key-decisions:
  - "Target space is S^8 (from spontaneous Spin(9)->Spin(8)), not OP^2 (from explicit F_4->Spin(9)). Consistent with Plan 01 correction."
  - "Used constant-curvature formula for Ric(S^8) directly rather than computing from Christoffel symbols. Cross-checked with symmetric space formula."
  - "Stated AF as d=2 concept; for d>=3, the relevant physics is the ordered phase with massless Goldstone modes."

patterns-established:
  - "O(N) sigma model construction from SSB coset: G/H symmetric space -> target, with Friedan beta = -(1/2pi) Ric"
  - "Topological triviality criterion: pi_k(target) = 0 for k <= d implies no topological terms"

conventions:
  - "natural_units: hbar=1, k_B=1, a=1"
  - "metric_signature: (+,...,+) Riemannian on target S^8"
  - "sigma_model_normalization: S = (rho_s/2) int (del n)^2"
  - "coupling: g^2 = T/rho_s"
  - "Riemann tensor sign: R_{ijkl} = K(g_{ik}g_{jl} - g_{il}g_{jk}) with K>0 for positive curvature"

plan_contract_ref: ".gpd/phases/39-spontaneous-symmetry-breaking-and-universality-class/39-03-PLAN.md#/contract"
contract_results:
  claims:
    claim-sigma-model:
      status: passed
      summary: "O(9) NL sigma model on S^8 = Spin(9)/Spin(8) constructed with action S = (rho_s/2) int (del n)^2, coupling g^2 = T/rho_s = 8T/J. Target space correctly derived from SSB coset."
      linked_ids: [deliv-sigma-derivation, test-target-space, test-action-form, ref-plan01-ssb, ref-friedan1985]
      evidence:
        - verifier: self-check
          method: SSB coset construction + dimensional analysis
          confidence: high
          claim_id: claim-sigma-model
          deliverable_id: deliv-sigma-derivation
          acceptance_test_id: test-target-space
    claim-asymptotic-freedom:
      status: passed
      summary: "Friedan one-loop beta function beta^{ij} = -(1/2pi) R^{ij} gives asymptotic freedom. For S^8: Ric = 7g (all eigenvalues positive), so beta < 0 in all directions. Coupling decreases in UV."
      linked_ids: [deliv-sigma-derivation, test-ricci-positive, test-af-check, ref-friedan1985, ref-helgason]
      evidence:
        - verifier: self-check
          method: Explicit Ricci tensor computation from constant-curvature formula + symmetric space cross-check
          confidence: high
          claim_id: claim-asymptotic-freedom
          deliverable_id: deliv-sigma-derivation
          acceptance_test_id: test-ricci-positive
    claim-homotopy:
      status: passed
      summary: "pi_k(S^8) = 0 for k=1,...,7 (connectivity of sphere). pi_8(S^8) = Z (Hurewicz). pi_9(S^8) = Z_2 (Freudenthal). No topological terms (theta, WZW, Skyrmions) in d<=7."
      linked_ids: [deliv-sigma-derivation, test-homotopy-groups, ref-baez2002]
      evidence:
        - verifier: self-check
          method: Algebraic topology (connectivity, Hurewicz theorem, Freudenthal suspension)
          confidence: high
          claim_id: claim-homotopy
          deliverable_id: deliv-sigma-derivation
          acceptance_test_id: test-homotopy-groups
  deliverables:
    deliv-sigma-derivation:
      status: passed
      path: "derivations/39-sigma-model.md"
      summary: "Complete NL sigma model derivation with 8 sections: target space (Sec 1), action (Sec 2), Ricci tensor (Sec 3), beta function (Sec 4), v9.0 connection (Sec 5), homotopy (Sec 6), summary table (Sec 7), homotopy verification (Sec 8)."
      linked_ids: [claim-sigma-model, claim-asymptotic-freedom, claim-homotopy]
  acceptance_tests:
    test-target-space:
      status: passed
      summary: "Target space S^8 = Spin(9)/Spin(8) from SSB pattern in Plan 01. dim(S^8) = 8 = 36 - 28 = dim(Spin(9)) - dim(Spin(8)). Matches SSB coset."
      linked_ids: [claim-sigma-model, deliv-sigma-derivation]
    test-action-form:
      status: passed
      summary: "Action S = (rho_s/2) int (del n)^2 with [rho_s] = [energy * length^{2-d}], [g^2] = [T/rho_s] = [length^{d-2}]. At d=2, g^2 dimensionless. Dimensional analysis consistent."
      linked_ids: [claim-sigma-model, deliv-sigma-derivation]
    test-ricci-positive:
      status: passed
      summary: "Ric(S^8) = 7 g_{ij}. Einstein manifold with positive Einstein constant lambda = 7. All eigenvalues of Ric are 7 > 0. Verified via constant-curvature formula Ric = (n-1)K g = 7*1*g and scalar curvature R = n(n-1) = 56."
      linked_ids: [claim-asymptotic-freedom, deliv-sigma-derivation, ref-helgason]
    test-af-check:
      status: passed
      summary: "From beta^{ij} = -(1/2pi) R^{ij} and R^{ij} = 7 g^{ij} > 0: the metric shrinks under RG in the UV, meaning the coupling decreases. This is asymptotic freedom. Coefficient (N-2)/(2pi) = 7/(2pi) for N=9."
      linked_ids: [claim-asymptotic-freedom, deliv-sigma-derivation, ref-friedan1985]
    test-homotopy-groups:
      status: passed
      summary: "pi_k(S^8) = 0 for k=1,...,7 (sphere is (n-1)-connected). pi_8 = Z (Hurewicz). pi_9 = Z_2 (Freudenthal). pi_15 = Z + Z_120 (octonionic Hopf + stable homotopy) [noted as training data for Z_120 factor]. All physically relevant groups verified."
      linked_ids: [claim-homotopy, deliv-sigma-derivation, ref-baez2002]
  references:
    ref-friedan1985:
      status: completed
      completed_actions: [cite, use]
      missing_actions: []
      summary: "Friedan's beta function beta^{ij} = -(1/2pi) R^{ij} at one loop applied to S^8. Establishes sigma model RG framework."
    ref-helgason:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Curvature of S^8 as symmetric space SO(9)/SO(8). Ric = (n-1)K g formula cited from symmetric space theory."
    ref-baez2002:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "S^8 = Spin(9)/Spin(8) structure, octonionic Hopf fibration S^7 -> S^15 -> S^8, OP^2 comparison."
    ref-plan01-ssb:
      status: completed
      completed_actions: [use]
      missing_actions: []
      summary: "SSB pattern Spin(9)->Spin(8) from Plan 01 used to identify target space S^8."
  forbidden_proxies:
    fp-af-without-ricci:
      status: rejected
      notes: "Ricci tensor computed explicitly from constant-curvature formula R_{ij} = (n-1)K g_{ij} with derivation of the contraction shown. Not assumed."
    fp-assume-op2:
      status: rejected
      notes: "Target space S^8 derived from SSB coset Spin(9)/Spin(8). OP^2 discussed only for comparison."
  uncertainty_markers:
    weakest_anchors:
      - "One-loop beta function; two-loop correction is O(g^6) with coefficient 7/(4pi^2), giving expansion parameter g^2/(2pi) which is small at weak coupling"
      - "pi_15(S^8) = Z + Z_120: the Z_120 factor is from training data (Toda tables); the Z factor is well-established from octonionic Hopf invariant"
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations:
      - "If Ricci tensor had a zero or negative eigenvalue, AF would fail in that direction. Excluded: S^8 has constant positive curvature."

comparison_verdicts:
  - subject_id: test-ricci-positive
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-helgason
    comparison_kind: benchmark
    metric: exact_match
    threshold: "Ric(S^8) = (n-1)g = 7g"
    verdict: pass
    recommended_action: "None -- Ricci tensor matches standard result exactly"
    notes: "Constant-curvature formula gives exact result for round sphere"
  - subject_id: test-af-check
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-friedan1985
    comparison_kind: benchmark
    metric: sign_check
    threshold: "beta coefficient > 0 (AF convention)"
    verdict: pass
    recommended_action: "None -- AF verified with coefficient 7/(2pi) > 0"
    notes: "O(N) sigma model with N=9 has positive one-loop coefficient"

duration: 6min
completed: 2026-03-30
---

# Phase 39, Plan 03: NL Sigma Model on S^8 and Asymptotic Freedom

**Constructed O(9) NL sigma model on S^8 = Spin(9)/Spin(8), derived Friedan beta function beta = (7/2pi)g^4, verified asymptotic freedom, proved no topological terms in d<=7**

## Performance

- **Duration:** 6 min
- **Started:** 2026-03-30T23:30:03Z
- **Completed:** 2026-03-30T23:36:00Z
- **Tasks:** 2
- **Files modified:** 1

## Key Results

- O(9) NL sigma model on S^8: S = (rho_s/2) int (del n)^2 with n in S^8 and g^2 = T/rho_s = 8T/J. [CONFIDENCE: HIGH]
- Ricci tensor: Ric(S^8) = 7 g_{ij} (Einstein manifold, lambda = 7, scalar curvature R = 56). [CONFIDENCE: HIGH]
- Friedan one-loop beta function: mu dg^2/dmu = -(d-2)g^2 + (7/2pi)g^4. Asymptotic freedom in d=2. [CONFIDENCE: HIGH]
- Homotopy: pi_k(S^8) = 0 for k = 1,...,7. No theta term, no WZW term, no Skyrmions for d <= 7. [CONFIDENCE: HIGH]
- O(9) sigma model is topologically simpler than O(3) model (no instantons, no theta, no WZW in any physical dimension). [CONFIDENCE: HIGH]

## Task Commits

1. **Task 1: NL sigma model construction and Friedan beta function** - `562e9bb` (derive)
2. **Task 2: Homotopy groups and topological sectors** - `8d3f3ad` (derive)

## Files Created/Modified

- `derivations/39-sigma-model.md` - Complete NL sigma model: target space, action, Ricci tensor, beta function, asymptotic freedom, homotopy groups, comparison tables

## Next Phase Readiness

- Sigma model action available for UC1-UC4 verification (Plan 04)
- Beta function establishes the RG flow from UV (asymptotically free) to IR (ordered phase with Goldstone modes)
- Topological triviality means no complications from theta terms or WZW for universality class analysis
- Connection to v9.0 O(3) model documented -- same mechanism, larger N
- Sigma model coupling g^2 = 8T/J quantifies perturbative parameter for spin-wave expansion

## Contract Coverage

- claim-sigma-model -> passed (O(9) NL sigma model on S^8 with explicit action)
- claim-asymptotic-freedom -> passed (Ric = 7g > 0, Friedan beta gives AF)
- claim-homotopy -> passed (pi_k = 0 for k <= 7, no topological terms)
- deliv-sigma-derivation -> passed (derivations/39-sigma-model.md)
- test-target-space -> passed (S^8 = Spin(9)/Spin(8), dim 8 = 36 - 28)
- test-action-form -> passed ([g^2] = [length^{d-2}], dimensionless at d=2)
- test-ricci-positive -> passed (Ric = 7g, all eigenvalues = 7 > 0)
- test-af-check -> passed (beta coefficient 7/(2pi) > 0)
- test-homotopy-groups -> passed (pi_1 = ... = pi_7 = 0, pi_8 = Z, pi_9 = Z_2)
- ref-friedan1985 -> completed (cite, use)
- ref-helgason -> completed (cite)
- ref-baez2002 -> completed (cite)
- ref-plan01-ssb -> completed (use)
- fp-af-without-ricci -> rejected (Ricci computed explicitly)
- fp-assume-op2 -> rejected (S^8 derived from SSB coset)
- Decisive comparisons: test-ricci-positive -> pass, test-af-check -> pass

## Equations Derived

**Eq. (39.6): NL sigma model action**

$$
S[\mathbf{n}] = \frac{\rho_s}{2} \int d^d x \, (\partial_\mu \mathbf{n})^2, \quad \mathbf{n} \in S^8
$$

**Eq. (39.7): Ricci tensor of S^8**

$$
\mathrm{Ric}(S^8) = R_{ij} = 7 \, g_{ij}
$$

**Eq. (39.8): Friedan one-loop beta function**

$$
\mu \frac{dg^2}{d\mu} = -(d-2)g^2 + \frac{7}{2\pi}g^4 + O(g^6)
$$

**Eq. (39.9): UV fixed point (d = 2 + epsilon)**

$$
g^2_* = \frac{2\pi\epsilon}{7}
$$

**Eq. (39.10): Homotopy triviality**

$$
\pi_k(S^8) = 0 \text{ for } k = 1, \ldots, 7
$$

## Validations Completed

- dim(S^8) = 8 = dim(Spin(9)) - dim(Spin(8)) = 36 - 28: exact
- Ricci tensor: Ric = (n-1)K g = 7*1*g for S^8 (n=8, K=1): matches constant-curvature formula
- Scalar curvature: R = n(n-1) = 56: matches trace of Ricci
- Beta function coefficient: (N-2)/(2pi) = 7/(2pi) for N=9: standard O(N) result
- Dimensional analysis: [g^2] = [length^{d-2}], dimensionless at d=2: consistent
- Asymptotic freedom: positive one-loop coefficient, coupling decreases in UV: standard convention verified
- Homotopy: pi_k(S^8) = 0 for k < 8 from (n-1)-connectivity of S^n: standard algebraic topology
- No topological terms: pi_2 = pi_3 = 0 implies no theta/WZW in d <= 3: verified
- Cross-check: S^8 and OP^2 homotopy agree for k <= 7 (both 7-connected): consistent

## Decisions Made

- Computed Ric(S^8) via constant-curvature formula rather than full Christoffel symbol computation. The sphere has constant sectional curvature, making this formula exact. Cross-checked with symmetric space formula.
- Stated asymptotic freedom as a d=2 concept. For d >= 3, the physically relevant regime is the ordered phase with massless Goldstone modes. The beta function still governs the UV behavior but the theory is super-renormalizable.
- Included comparison with OP^2 (original roadmap assumption) and S^2 (v9.0 toy model) for completeness and to clarify the simplification from the corrected SSB pattern.

## Deviations from Plan

None -- plan executed as specified.

## Issues Encountered

None.

## Open Questions

- What is the exact value of pi_15(S^8)? The Z factor (octonionic Hopf) is well-established, but the torsion factor (Z_120 from training data) should be verified against Toda's tables if needed.
- How does the two-loop correction modify the UV fixed point at d = 2+epsilon? The one-loop fixed point is g^2_* = 2pi*epsilon/7; the two-loop shift is O(epsilon^2).
- What is the precise spin stiffness rho_s for the quantum model (as opposed to the classical estimate J/8)?

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
|----------|--------|-------|-------------|--------|-------------|
| Ricci tensor | Ric(S^8) | 7 g_{ij} | exact | constant curvature formula | S^8 round metric |
| Einstein constant | lambda | 7 | exact | Ric = lambda g | S^8 |
| Scalar curvature | R | 56 | exact | n(n-1) for S^n | S^8 |
| AF coefficient | (N-2)/(2pi) | 7/(2pi) ~ 1.114 | exact (one-loop) | Friedan 1985 | O(9) model, d=2 |
| UV fixed point (d=2+eps) | g^2_* | 2pi*eps/7 | O(eps^2) | one-loop beta=0 | eps << 1 |
| Spin stiffness (classical) | rho_s | J/8 | O(T/J) corrections | classical O(9) at T=0 | T << J |
| Sigma model coupling | g^2 | 8T/J | exact definition | T/rho_s | classical limit |
| Target space dimension | dim(S^8) | 8 | exact | 36 - 28 | N/A |

## Approximations Used

| Approximation | Valid When | Error Estimate | Breaks Down At |
|---------------|-----------|----------------|----------------|
| One-loop Friedan beta | g^2/(2pi) << 1 | O(g^6/(2pi)^2) ~ 16% of one-loop at g^2 ~ 1 | g^2 ~ 2pi (strong coupling) |
| Classical spin stiffness rho_s = J/8 | T << J (low temperature) | O(T/J) thermal corrections | T ~ J (near T_c) |
| Nearest-neighbor continuum limit | k*a << 1 | O(k^2 a^2) lattice corrections | k ~ pi/a (Brillouin zone edge) |

---

_Phase: 39-spontaneous-symmetry-breaking-and-universality-class, Plan: 03_
_Completed: 2026-03-30_
