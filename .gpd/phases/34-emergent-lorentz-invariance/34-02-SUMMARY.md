---
phase: 34-emergent-lorentz-invariance
plan: 02
depth: full
one-liner: "Velocity hierarchy v_LR/c_s=7.63 established, c_eff=c_s justified by four arguments, emergent Lorentzian metric assembled from Fisher (spatial) + sigma model (temporal)"
subsystem: [derivation]
tags: [lieb-robinson, spin-wave-velocity, emergent-lorentz, causal-structure, fisher-metric, sigma-model, velocity-hierarchy]

requires:
  - phase: 33-correlation-structure-and-effective-theory
    plan: 01
    provides: "c_s = 1.659 Ja from NL sigma model (Eq. 33.14); rho_s, chi_perp"
  - phase: 32-fisher-geometry-on-reduced-states
    plan: 02
    provides: "Fisher metric g_ij smooth and positive-definite (FISH-01/02)"

provides:
  - "Velocity hierarchy: v_LR = 12.66 J >> c_s = 1.659 Ja, ratio 7.63"
  - "c_eff identification: c_eff = c_s (four independent arguments)"
  - "Emergent metric: ds^2 = -c_s^2 dt^2 + g_ij dx^i dx^j (Eq. 34.9)"
  - "Two-tier causal structure: LR fundamental (v_LR) containing Lorentzian effective (c_s)"

affects: [35-bisognano-wichmann, 36-jacobson-assembly]

methods:
  added: [velocity-hierarchy-analysis, metric-assembly-from-components]
  patterns: [two-tier-causal-structure, effective-vs-fundamental-speed]

key-files:
  created:
    - derivations/34-velocity-hierarchy-and-causal-structure.md

key-decisions:
  - "c_eff = c_s identified via four independent arguments (dispersion, EFT, universality, Hamma precedent)"
  - "Metric assembly stated as schematic (Fisher + sigma model from different frameworks; physical intuition, not theorem)"
  - "v_LR = 8eJ/(e-1) is 1D value; qualitative hierarchy v_LR >> c_s robust in d>=2 but specific ratio 7.63 is 1D"

patterns-established:
  - "two-tier-causal: separate fundamental (LR, lattice) from effective (Lorentzian, continuum)"
  - "metric-assembly: temporal from sigma model Wick rotation, spatial from Fisher information geometry"

conventions:
  - "natural_units=natural, hbar=1, k_B=1, a=1"
  - "metric_signature=Riemannian_Fisher (spatial); Lorentzian (-,+,...,+) emergent"
  - "coupling_convention=J>0 AFM"
  - "fisher_metric=SLD, g_F=4*g_Bures"
  - "sigma_model_field=O(3) n-field, n^2=1"
  - "velocity_units: v_LR in J, c_s in Ja (both = J when a=1)"

plan_contract_ref: ".gpd/phases/34-emergent-lorentz-invariance/34-02-PLAN.md#/contract"

contract_results:
  claims:
    claim-velocity-hierarchy:
      status: passed
      summary: "v_LR = 12.66 J >> c_s = 1.659 Ja, ratio 7.63. v_LR >= c_s guaranteed by Lieb-Robinson theorem. c_eff = c_s justified by four independent arguments (dispersion, EFT, universality, Hamma precedent). Hamma et al. ratio sqrt(2)*e = 3.84 cited for comparison."
      linked_ids: [deliv-derivation-34-02, test-hierarchy-numerical, test-vlr-bound, test-ceff-identification, ref-nachtergaele-sims2006, ref-paper6-vlr, ref-phase33-cs, ref-hamma2009]
    claim-metric-assembly:
      status: passed
      summary: "Emergent metric ds^2 = -c_s^2 dt^2 + g_ij dx^i dx^j assembled. Temporal from sigma model Wick rotation, spatial from Fisher metric. Lorentzian signature (-,+,...,+) verified from two independent inputs. Two-tier causal structure: effective (c_s, Lorentzian) nested inside fundamental (v_LR, lattice)."
      linked_ids: [deliv-derivation-34-02, test-metric-signature, test-spatial-fisher, test-causal-vlr, ref-nachtergaele-sims2006, ref-phase32-fisher, ref-phase33-cs]
  deliverables:
    deliv-derivation-34-02:
      status: passed
      path: "derivations/34-velocity-hierarchy-and-causal-structure.md"
      summary: "Complete derivation document with Parts I-IV: velocity hierarchy, c_eff identification, metric assembly, two-tier causal structure. All required content present (v_LR/c_s ratio, c_eff=c_s justification, metric equation, causal cones)."
      linked_ids: [claim-velocity-hierarchy, claim-metric-assembly, test-hierarchy-numerical, test-vlr-bound, test-ceff-identification, test-metric-signature, test-spatial-fisher, test-causal-vlr]
  acceptance_tests:
    test-hierarchy-numerical:
      status: passed
      summary: "v_LR/c_s = 12.66/1.659 = 7.63 computed explicitly with correct units. Both values stated. v_LR > c_s confirmed. Python Level 5 verification executed."
      linked_ids: [claim-velocity-hierarchy, deliv-derivation-34-02, ref-paper6-vlr, ref-phase33-cs]
    test-vlr-bound:
      status: passed
      summary: "v_LR >= c_s stated as theorem-level result: v_LR bounds ALL signals including magnon propagation (special case), so inequality follows from definition. Nachtergaele-Sims 2006 cited."
      linked_ids: [claim-velocity-hierarchy, deliv-derivation-34-02, ref-nachtergaele-sims2006]
    test-ceff-identification:
      status: passed
      summary: "Four independent arguments for c_eff = c_s: (a) dispersion relation omega=c_s|k|, (b) EFT -- sigma model manifestly Lorentzian with c_s, (c) universality -- c_s universal, v_LR non-universal, (d) Hamma et al. precedent (toric code). All cited."
      linked_ids: [claim-velocity-hierarchy, deliv-derivation-34-02, ref-hamma2009]
    test-metric-signature:
      status: passed
      summary: "Lorentzian signature (-,+,...,+): temporal -c_s^2 < 0 from Wick rotation of sigma model, spatial g_ij > 0 from Fisher metric positive-definiteness (Phase 32). Two independent inputs confirmed."
      linked_ids: [claim-metric-assembly, deliv-derivation-34-02, ref-phase32-fisher, ref-phase33-cs]
    test-spatial-fisher:
      status: passed
      summary: "Explicitly stated: Fisher metric is spatial (Riemannian), not spacetime (Lorentzian). Fisher metric provides no temporal information. Temporal structure attributed to sigma model Wick rotation."
      linked_ids: [claim-metric-assembly, deliv-derivation-34-02, ref-phase32-fisher]
    test-causal-vlr:
      status: passed
      summary: "Two-tier causal structure described: Tier 1 (fundamental, lattice, v_LR, exact, non-Lorentzian) contains Tier 2 (effective, continuum, c_s, approximate, Lorentzian). Inequality c_s < v_LR means effective cone inside LR cone."
      linked_ids: [claim-metric-assembly, deliv-derivation-34-02, ref-nachtergaele-sims2006]
  references:
    ref-nachtergaele-sims2006:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited as source of rigorous LR bound (Eq. 34.1) and for theorem-level guarantee v_LR >= c_s."
    ref-paper6-vlr:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited for v_LR = 8eJ/(e-1) ~ 12.66 J, SWAP on Z^1."
    ref-phase33-cs:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited for c_s = 1.659 Ja from NL sigma model (Eq. 33.14), QMC verification."
    ref-hamma2009:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited as precedent for v_LR > c_eff on lattices. Specific ratio sqrt(2)*e ~ 3.84 for toric code stated for comparison."
    ref-phase32-fisher:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited for Fisher metric g_ij smooth and positive-definite (spatial part of emergent metric)."
  forbidden_proxies:
    fp-vlr-as-light-speed:
      status: rejected
      notes: "v_LR never appears in ds^2. Only c_s = c_eff appears in the emergent metric. v_LR appears only in causal structure discussion as fundamental (lattice) bound."
    fp-fisher-is-lorentzian:
      status: rejected
      notes: "Fisher metric explicitly stated as Riemannian (spatial only). Temporal structure from sigma model. No claim that Fisher alone gives Lorentzian spacetime."
    fp-conflate-causal-structures:
      status: rejected
      notes: "Two-tier structure explicitly described: effective (c_s, Lorentzian) vs fundamental (v_LR, lattice). Physically distinct. Ratio 7.63 stated."
  uncertainty_markers:
    weakest_anchors:
      - "v_LR = 8eJ/(e-1) is for SWAP on Z^1 (1D); in d>=2 the LR velocity may differ. Qualitative hierarchy v_LR >> c_s is robust but specific ratio 7.63 is 1D."
      - "Metric assembly ds^2 = -c_s^2 dt^2 + g_ij dx^i dx^j is schematic: Fisher g_ij and sigma model time from different frameworks. Precise coupling is physical intuition, not theorem."
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations:
      - "If v_LR < c_s in any dimension, the LR bound is violated and the framework fails"
      - "If Fisher metric has zero eigenvalues in thermodynamic limit (d>=2), spatial part of emergent metric is degenerate"

duration: 3min
completed: 2026-03-30
---

# Phase 34, Plan 02: Velocity Hierarchy and Causal Structure

**Velocity hierarchy v_LR/c_s=7.63 established, c_eff=c_s justified by four arguments, emergent Lorentzian metric assembled from Fisher (spatial) + sigma model (temporal)**

## Performance

- **Duration:** 3 min
- **Started:** 2026-03-30T03:59:30Z
- **Completed:** 2026-03-30T04:02:49Z
- **Tasks:** 2
- **Files modified:** 1

## Key Results

- **Velocity hierarchy:** v_LR = 12.66 J >> c_s = 1.659 J (at a=1), ratio v_LR/c_s = 7.63 [CONFIDENCE: HIGH -- numerical computation verified by Python Level 5]
- **c_eff identification:** c_eff = c_s = 1.659 Ja, justified by four independent arguments (dispersion, EFT, universality, Hamma precedent) [CONFIDENCE: HIGH -- standard condensed matter reasoning]
- **Emergent metric:** ds^2 = -c_s^2 dt^2 + g_ij dx^i dx^j with Lorentzian signature (-,+,...,+) [CONFIDENCE: MEDIUM -- metric assembly is schematic, combining frameworks; individual components are rigorous]
- **Two-tier causal structure:** fundamental LR cone (v_LR, exact, lattice) contains effective Lorentzian cone (c_s, approximate, continuum) [CONFIDENCE: HIGH -- follows directly from v_LR >= c_s theorem]

## Task Commits

1. **Task 1+2: Velocity hierarchy, c_eff identification, metric assembly, causal structure** - `e9efeee` (derive)

## Files Created/Modified

- `derivations/34-velocity-hierarchy-and-causal-structure.md` - Complete derivation: velocity hierarchy, c_eff=c_s arguments, metric assembly, two-tier causal structure

## Next Phase Readiness

- Emergent Lorentzian metric (Eq. 34.9) ready for Phase 35 (Bisognano-Wichmann theorem requires Lorentz invariance)
- Lorentz invariance established via sigma model + Wick rotation (Eq. 34.7)
- c_s = 1.659 Ja available as invariant speed for Phase 35 and Phase 36 (Jacobson assembly)
- Two-tier causal structure provides framework for understanding UV/IR separation in emergent gravity

## Contract Coverage

- claim-velocity-hierarchy -> passed
- claim-metric-assembly -> passed
- deliv-derivation-34-02 -> passed (derivations/34-velocity-hierarchy-and-causal-structure.md)
- test-hierarchy-numerical -> passed (v_LR/c_s = 7.63)
- test-vlr-bound -> passed (theorem-level, Nachtergaele-Sims cited)
- test-ceff-identification -> passed (four arguments + Hamma precedent)
- test-metric-signature -> passed (Lorentzian from two independent inputs)
- test-spatial-fisher -> passed (Fisher spatial only, explicit statement)
- test-causal-vlr -> passed (two-tier structure)
- ref-nachtergaele-sims2006 -> completed (cited)
- ref-paper6-vlr -> completed (cited)
- ref-phase33-cs -> completed (cited)
- ref-hamma2009 -> completed (cited)
- ref-phase32-fisher -> completed (cited)
- fp-vlr-as-light-speed -> rejected
- fp-fisher-is-lorentzian -> rejected
- fp-conflate-causal-structures -> rejected

## Equations Derived

**Eq. (34.1): Lieb-Robinson bound**

$$
\|[O_A(t), O_B(0)]\| \leq C \|O_A\| \|O_B\| \min(|A|,|B|) e^{-\mu(d(A,B) - v_{\text{LR}}|t|)}
$$

**Eq. (34.5): Velocity hierarchy**

$$
v_{\text{LR}} = 12.66\, J, \quad c_s = 1.659\, J, \quad v_{\text{LR}}/c_s = 7.63
$$

**Eq. (34.8): Emergent speed of light identification**

$$
c_{\text{eff}} = c_s = 1.659\, Ja
$$

**Eq. (34.9): Emergent metric assembly**

$$
ds^2 = -c_s^2\, dt^2 + g_{ij}(x)\, dx^i dx^j
$$

**Eq. (34.12): Causal cone nesting**

$$
c_s < v_{\text{LR}} \implies \text{Lorentzian cone} \subset \text{LR cone}
$$

## Validations Completed

- v_LR/c_s = 12.66/1.659 = 7.63 verified by Python (Level 5)
- Dimensional analysis: [v_LR/c_s] = [J/(Ja)] = dimensionless at a=1
- Metric signature: temporal (-c_s^2 < 0) + spatial (g_ij > 0) = Lorentzian (-,+,...,+)
- Dimensional analysis: [ds^2] = [J^2 a^2 / J^2] = [a^2] = [length^2]
- Forbidden proxy check: v_LR never in ds^2, Fisher never called Lorentzian, causal structures not conflated
- Hamma et al. ratio sqrt(2)*e = 3.84 computed for comparison

## Decisions & Deviations

### Decisions

- Both tasks committed as single derivation document (plan specifies same output file)
- Metric assembly stated as schematic with explicit uncertainty marker (Fisher + sigma model from different frameworks)
- v_LR = 8eJ/(e-1) noted as 1D value; qualitative hierarchy v_LR >> c_s is robust but specific ratio is 1D

### Deviations from Plan

None -- plan executed as specified.

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
|----------|--------|-------|-------------|--------|-------------|
| LR velocity | v_LR | 12.66 | exact (analytic) | Paper 6 | SWAP on Z^1 |
| Spin-wave velocity | c_s | 1.65880 | +/- 0.00006 | QMC (Sandvik 2025) | d=2, S=1/2 |
| Velocity ratio | v_LR/c_s | 7.63 | +/- 0.01 | This derivation | a=1 |
| Hamma et al. ratio | v_LR/c_ph | 3.84 | exact (analytic) | Hamma 2009 | Toric code, 2D |

## Approximations Used

| Approximation | Valid When | Error Estimate | Breaks Down At |
|---------------|-----------|----------------|----------------|
| NL sigma model continuum limit | ka << 1 | O((ka)^2) | k ~ pi/a |
| Effective metric assembly | L >> a, L >> xi | schematic | L ~ a or near QCP |

## Open Questions

- What is v_LR for the SWAP Hamiltonian in d >= 2? The qualitative hierarchy v_LR >> c_s is robust but the specific ratio 7.63 is computed for 1D.
- Can the metric assembly Eq. (34.9) be made rigorous (Fisher g_ij and sigma model time from the same framework)?
- How does the two-tier causal structure manifest in the Bisognano-Wichmann analysis (Phase 35)?

## Self-Check: PASSED

- [x] derivations/34-velocity-hierarchy-and-causal-structure.md exists
- [x] Commit e9efeee exists
- [x] v_LR/c_s = 7.63 verified by Python (Level 5)
- [x] All contract IDs covered (2 claims, 1 deliverable, 6 acceptance tests, 5 references, 3 forbidden proxies)
- [x] No forbidden proxies violated
- [x] Dimensional consistency throughout

---

_Phase: 34-emergent-lorentz-invariance_
_Plan: 02_
_Completed: 2026-03-30_
