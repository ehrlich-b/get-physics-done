---
phase: 23-entropy-increase-under-sequential-products
plan: 01
depth: full
one-liner: "Derived CPTP channel for 2-qubit SWAP dynamics: depolarizing with p=sin^2(Jt), unital when rho_M=I/2, Delta S >= 0 proven analytically and verified numerically over 9900 state-time points"
subsystem: derivation
tags: [entropy, CPTP-channel, SWAP-operator, unitality, depolarizing-channel, Lindblad-H-theorem]

requires:
  - phase: 08-locality-formalization
    provides: "SWAP Hamiltonian h_xy = JF from diagonal U(n) covariance"
  - phase: 04-sequential-product-formalization
    provides: "Luders product a & b = sqrt(a) b sqrt(a)"
provides:
  - "Explicit CPTP channel: E(rho_B) = cos^2(Jt) rho_B + sin^2(Jt) I/2 for rho_M = I/2"
  - "Unitality proven for rho_M = I/2; non-unital for general rho_M"
  - "Delta S >= 0 for all initial states when rho_M = I/2 (Lindblad H-theorem applies)"
  - "General rho_M formula: rho_B(t) = cos^2 rho_B + sin^2 rho_M - i sin*cos [rho_M, rho_B]"
  - "Entropy CAN decrease for non-maximally-mixed rho_M (5508/9900 points negative)"
  - "Non-selective Luders channel (Interpretation A) also unital; reduced to depolarizing with p=1/2"
affects: [23-02, paper8]

methods:
  added: [depolarizing-channel-analysis, partial-trace-index-computation, Pauli-twirl-Kraus-decomposition]
  patterns: [SWAP-evolution-partial-trace, unitality-test-protocol, parametric-entropy-sweep]

key-files:
  created:
    - derivations/23-luders-channel-entropy.md
    - code/luders_entropy.py

key-decisions:
  - "Interpretation B (unitary SWAP evolution + partial trace) is primary for lattice dynamics; Interpretation A (non-selective Luders) is secondary"
  - "rho_M = I/2 used as canonical model state; general rho_M formula derived for completeness"
  - "Both forbidden proxies (fp-assume-unital, fp-dpi-without-unitality) resolved by explicit proof, not assumption"

conventions:
  - "hbar = 1, k_B = 1"
  - "Entropy in nats (natural logarithm)"
  - "Tr(rho) = 1"
  - "S(rho) = -Tr(rho ln rho)"
  - "H = JF (SWAP Hamiltonian, no factor of 1/2)"
  - "a & b = sqrt(a) b sqrt(a) (Luders product)"

plan_contract_ref: ".gpd/phases/23-entropy-increase-under-sequential-products/23-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-entropy-explicit:
      status: passed
      summary: "CPTP channel derived explicitly for both interpretations; unitality proven for rho_M=I/2; entropy change Delta S >= 0 characterized for all 2-qubit initial states"
      linked_ids: [deliv-channel-derivation, deliv-entropy-code]
      evidence:
        - verifier: gpd-executor
          method: analytical derivation + numerical sweep
          confidence: high
          claim_id: claim-entropy-explicit
          deliverable_id: deliv-channel-derivation
          acceptance_test_id: test-cptp
          reference_id: ref-paper5
          evidence_path: "derivations/23-luders-channel-entropy.md"
  deliverables:
    deliv-channel-derivation:
      status: passed
      path: "derivations/23-luders-channel-entropy.md"
      summary: "Complete derivation: Kraus operators, unitality analysis, entropy change formula, general rho_M result, all limiting cases"
      linked_ids: [claim-entropy-explicit, test-cptp, test-unitality, test-entropy-sympy]
    deliv-entropy-code:
      status: passed
      path: "code/luders_entropy.py"
      summary: "617-line verification script: all 13 test categories pass, 9900-point parametric sweep, CPTP/unitality/entropy tests"
      linked_ids: [claim-entropy-explicit, test-cptp, test-unitality, test-entropy-sympy]
  acceptance_tests:
    test-cptp:
      status: passed
      summary: "CPTP verified: sum K_i^dag K_i = I (exact), output PSD with Tr=1 for 20 random states (error < 1e-12)"
      linked_ids: [claim-entropy-explicit, deliv-channel-derivation, deliv-entropy-code]
    test-unitality:
      status: passed
      summary: "E(I/2) = I/2 verified at 10 t-values (error < 5.55e-17); E(I/2) != I/2 confirmed for rho_M = diag(0.9,0.1) with deviation 0.2-0.4"
      linked_ids: [claim-entropy-explicit, deliv-channel-derivation, deliv-entropy-code]
    test-entropy-sympy:
      status: passed
      summary: "Entropy computed for all 5 families: (a) pure |0>, (b) I/2, (c) parametric diag(p,1-p) 99 points, (d) both pure, (e) biased rho_M. All match analytical formula within 1e-10. Delta S >= 0 in 9900-point 2D sweep."
      linked_ids: [claim-entropy-explicit, deliv-channel-derivation, deliv-entropy-code]
  references:
    ref-paper5:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Paper 5 Luders product definition cited in derivation and code"
    ref-paper6:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Paper 6 SWAP Hamiltonian h_xy = JF cited in derivation"
    ref-lindblad1975:
      status: completed
      completed_actions: [read, compare]
      missing_actions: []
      summary: "Lindblad H-theorem applies: unital channel implies S(E(rho)) >= S(rho). Result confirmed numerically."
  forbidden_proxies:
    fp-assume-unital:
      status: rejected
      notes: "Unitality was PROVEN explicitly, not assumed. E(I/2) = cos^2(Jt)(I/2) + sin^2(Jt)(I/2) = I/2."
    fp-dpi-without-unitality:
      status: rejected
      notes: "DPI/Lindblad H-theorem invoked ONLY after proving unitality for rho_M = I/2. For general rho_M, entropy can decrease (5508/9900 points)."
  uncertainty_markers:
    weakest_anchors:
      - "rho_M = I/2 assumption: unitality and entropy increase depend on maximally mixed model. For iterated dynamics, rho_M may not remain I/2."
    unvalidated_assumptions:
      - "Single-step analysis: iterated application may accumulate non-unital corrections if rho_M evolves"
    competing_explanations: []
    disconfirming_observations:
      - "For rho_M != I/2, entropy CAN decrease (confirmed: 5508/9900 points with rho_M = diag(0.9,0.1)). The non-unital concern is real for non-equilibrium model states."

duration: 20min
completed: 2026-03-24
---

# Phase 23, Plan 01: Luders CPTP Channel and Entropy Change Summary

**Derived CPTP channel for 2-qubit SWAP dynamics: depolarizing with p=sin^2(Jt), unital when rho_M=I/2, Delta S >= 0 proven analytically and verified numerically over 9900 state-time points**

## Performance

- **Duration:** 20 min
- **Started:** 2026-03-24T18:54:42Z
- **Completed:** 2026-03-24T19:14:00Z
- **Tasks:** 2
- **Files modified:** 2

## Key Results

- **Channel formula (rho_M = I/2):** E(rho_B) = cos^2(Jt) rho_B + sin^2(Jt) I/2 -- a depolarizing channel with parameter p = sin^2(Jt)
- **Unitality:** PROVEN for rho_M = I/2 (all t); DISPROVEN for rho_M != I/2
- **Entropy change:** Delta S >= 0 for ALL initial states when rho_M = I/2 (Lindblad H-theorem for unital channels)
- **Entropy decrease possible:** For non-maximally-mixed rho_M, 56% of tested state-time points show Delta S < 0
- **General formula:** rho_B(t) = cos^2(Jt) rho_B + sin^2(Jt) rho_M - i sin(Jt)cos(Jt) [rho_M, rho_B]
- **Kraus operators:** K_0 = sqrt(1-3p/4) I, K_i = (sqrt(p)/2) sigma_i (i=1,2,3)

## Task Commits

1. **Task 1: Derive Luders CPTP channel and entropy change** - `a2e147a` (derive)
2. **Task 2: SymPy/NumPy verification and parametric sweep** - `03f6bb8` (compute)

## Files Created/Modified

- `derivations/23-luders-channel-entropy.md` - Full derivation: SWAP operator, unitary evolution, channel construction, unitality proof, entropy change formula, non-selective Luders channel, general rho_M formula
- `code/luders_entropy.py` - 617-line verification: 13 test categories, 9900-point parametric sweep

## Next Phase Readiness

- Channel formula and unitality result ready for Plan 02 (iterated dynamics)
- Key question for Plan 02: does rho_M remain I/2 under iteration? If not, non-unital corrections accumulate and entropy decrease becomes possible
- The Lindblad H-theorem route is confirmed for single-step analysis; iteration requires separate treatment

## Contract Coverage

- Claim IDs advanced: claim-entropy-explicit -> passed
- Deliverable IDs produced: deliv-channel-derivation -> derivations/23-luders-channel-entropy.md, deliv-entropy-code -> code/luders_entropy.py
- Acceptance test IDs run: test-cptp -> passed, test-unitality -> passed, test-entropy-sympy -> passed
- Reference IDs surfaced: ref-paper5 -> cited, ref-paper6 -> cited, ref-lindblad1975 -> read + compared
- Forbidden proxies rejected: fp-assume-unital -> rejected (unitality proven), fp-dpi-without-unitality -> rejected (DPI invoked after proof)

## Equations Derived

**Eq. (23.1) -- Channel for rho_M = I/2:**
$$
E_U(\rho_B) = \cos^2(Jt)\, \rho_B + \sin^2(Jt)\, \frac{I}{2}
$$

**Eq. (23.2) -- General rho_M formula:**
$$
\rho_B(t) = \cos^2(Jt)\, \rho_B + \sin^2(Jt)\, \rho_M - i\sin(Jt)\cos(Jt)\, [\rho_M, \rho_B]
$$

**Eq. (23.3) -- Entropy change:**
$$
\Delta S = h\!\left(\lambda + \sin^2(Jt)\left(\tfrac{1}{2} - \lambda\right)\right) - h(\lambda) \geq 0
$$
where h(x) = -x ln x - (1-x) ln(1-x) is the binary entropy and lambda is the larger eigenvalue of rho_B.

**Eq. (23.4) -- Non-selective Luders reduced channel:**
$$
E_{\text{Luders}}(\rho_B) = \frac{1}{2}\rho_B + \frac{1}{4}I
$$

## Validations Completed

- F^2 = I (exact)
- F eigenvalues {-1, +1, +1, +1}, Tr(F) = 2
- U^dag U = I (error < 2.2e-16 for 10 random t)
- CPTP: Tr(E(rho)) = 1 for 20 random states (error < 1e-12)
- Unitality: E(I/2) = I/2 for 10 t-values (error < 5.6e-17)
- S(I/2) = ln(2) = 0.6931 nats (exact)
- S(|0><0|) = 0 (exact)
- t=0: Delta S = 0 (no evolution)
- Jt=pi/2: rho_B -> I/2 (full SWAP to maximally mixed)
- Kraus operators reproduce channel action (error < 1e-12)
- Analytical formula matches numerical computation (error < 1e-13)
- General rho_M formula matches for 5 model states x 6 times (error < 1.3e-16)
- 9900-point parametric sweep confirms Delta S >= 0

## Decisions & Deviations

None - followed plan as specified. Both interpretations analyzed as requested. Forbidden proxies addressed by explicit proof.

## Open Questions

- Does rho_M remain I/2 under iterated SWAP dynamics? (Critical for Plan 02)
- For iterated dynamics with evolving rho_M, do non-unital corrections accumulate or average out?
- Can the depolarizing channel structure persist beyond n=2 (higher-dimensional systems)?

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
| --- | --- | --- | --- | --- | --- |
| Depolarizing parameter | p | sin^2(Jt) | exact | analytical | all Jt |
| Max entropy gain (pure -> mixed) | Delta S_max | ln(2) = 0.693 nats | exact | analytical | Jt = pi/2, rho_B pure |
| Non-unital fraction (rho_M biased) | - | 5508/9900 = 56% | statistical (grid) | numerical sweep | rho_M = diag(0.9,0.1) |

## Approximations Used

| Approximation | Valid When | Error Estimate | Breaks Down At |
| --- | --- | --- | --- |
| Finite-dim QM (n=2 qubits) | exact for finite-dim | exact | n -> infinity |
| Single-step analysis | one SWAP evolution step | exact for single step | iteration (Plan 02) |
| rho_M = I/2 | model is maximally mixed | exact | rho_M != I/2 (non-unital) |

## Self-Check: PASSED

- [x] derivations/23-luders-channel-entropy.md exists
- [x] code/luders_entropy.py exists
- [x] Commit a2e147a exists
- [x] Commit 03f6bb8 exists
- [x] All numerical values reproduced by code
- [x] Convention consistency: entropy in nats throughout
- [x] Contract coverage complete: all claim/deliverable/test/reference/proxy IDs addressed

---

_Phase: 23-entropy-increase-under-sequential-products_
_Completed: 2026-03-24_
