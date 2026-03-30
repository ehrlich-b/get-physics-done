---
phase: 35-bw-theorem-and-local-equilibrium
plan: 02
depth: full
one-liner: "KMS property derived from BW modular flow at beta=2pi, Unruh temperature T_U=a/(2pi) obtained, local equilibrium theta=sigma=0 at bifurcation surface from Killing symmetry"
subsystem: [derivation]
tags: [kms, unruh-effect, modular-hamiltonian, bisognano-wichmann, killing-vector, local-equilibrium, rindler, bifurcation-surface, jacobson]

requires:
  - phase: 35-bw-theorem-and-local-equilibrium
    plan: 01
    provides: "BW identification K_A = 2pi K_boost (Eq. 35.0a), lattice-BW form Eq. (35.1), SRF = 0.9993, W1-W4 satisfied"
  - phase: 34-emergent-lorentz-invariance
    plan: 01
    provides: "Emergent Lorentz invariance, Eq. (34.30), DLS reflection positivity"

provides:
  - "BWEQ-02: KMS property derived from BW via Tomita-Takesaki modular flow"
  - "Unruh temperature T_U = a/(2pi) (Eq. 35.3)"
  - "Local equilibrium theta = sigma = 0 at bifurcation surface (Eqs. 35.19, 35.21)"
  - "Three Jacobson inputs (J1: K_A=2pi K_boost, J2: theta=sigma=0, J3: T_U=a/(2pi)) packaged for Phase 36"
  - "Modular flow = Lorentz boost identification (Eq. 35.9)"

affects: [36-jacobson-assembly]

methods:
  added: [tomita-takesaki-modular-theory, kms-derivation, killing-vector-analysis, rindler-observer-construction]
  patterns: [modular-time-to-proper-time-conversion, 2pi-factor-tracing]

key-files:
  created:
    - derivations/35-kms-equilibrium-and-modular-hamiltonian.md

key-decisions:
  - "Cited (not re-derived) Tomita-Takesaki theorem and HHW KMS definition"
  - "theta=sigma=0 derived as exact geometric identity from Killing equation, not approximation"
  - "Lattice KMS property stated as formal (Gibbs state), rigorous only in continuum limit"

patterns-established:
  - "2pi-tracing: the factor 2pi in T_U = a/(2pi) traced end-to-end from K_A = 2pi K_boost through modular-to-proper time conversion"
  - "killing-equilibrium: local equilibrium theta=sigma=0 follows automatically from Killing symmetry, not from additional assumptions"

conventions:
  - "natural_units=natural, hbar=1, k_B=1, a=1"
  - "metric_signature=mostly_minus (-,+,...,+) for emergent Lorentzian spacetime"
  - "modular_hamiltonian=K_A=-ln(rho_A), rho_A=e^{-K_A}/Z"
  - "kms_temperature=beta=2pi for Rindler wedge"
  - "coupling_convention=J>0 AFM"

plan_contract_ref: ".gpd/phases/35-bw-theorem-and-local-equilibrium/35-02-PLAN.md#/contract"

contract_results:
  claims:
    claim-kms-derivation:
      status: passed
      summary: "KMS property DERIVED (not assumed) from BW identification via Tomita-Takesaki modular theory. Logical chain: (1) BW gives K_A = 2pi K_boost (Plan 01), (2) modular automorphism sigma_t = boost by 2pi*t (Eq. 35.9), (3) Tomita-Takesaki: vacuum is KMS at beta_mod=1 for sigma_t (Eq. 35.8), (4) converting modular to proper time: beta_phys = 2pi/a. HHW 1967 cited for KMS definition."
      linked_ids: [deliv-derivation-35-02, test-kms-derived, test-2pi-factor, ref-hhw1967, ref-bw-plan01]
    claim-local-equilibrium:
      status: passed
      summary: "Local equilibrium theta=sigma=0 at bifurcation surface derived from Killing equation. The boost Killing vector xi^mu vanishes at B={x^0=0, x^1=0}. theta=0 from trace of Killing equation (Eq. 35.19). sigma=0 from Killing equation directly (Eq. 35.21). These are exact geometric identities."
      linked_ids: [deliv-derivation-35-02, test-theta-sigma-zero, test-killing-argument, ref-jacobson2016, ref-bw-plan01]
    claim-modular-boost:
      status: passed
      summary: "Modular Hamiltonian K_A identified with 2pi times boost generator K_boost. The 2pi factor traced end-to-end: K_A=2pi K_boost -> sigma_t = boost by 2pi*t -> beta_mod=1 -> beta_phys=2pi/a -> T_U=a/(2pi). Rindler observer trajectory stated explicitly with proper acceleration a. T_U=1/(2pi)~0.159 for a=1. CHM modular Hamiltonian cited as cross-check."
      linked_ids: [deliv-derivation-35-02, test-unruh-temperature, test-jacobson-input, ref-bw-plan01, ref-jacobson2016, ref-chm2011]
  deliverables:
    deliv-derivation-35-02:
      status: passed
      path: "derivations/35-kms-equilibrium-and-modular-hamiltonian.md"
      summary: "Complete derivation document with three parts: (I) KMS from BW via modular flow + Unruh temperature, (II) local equilibrium at bifurcation surface from Killing symmetry, (III) Jacobson input specification J1-J3. Contains ASSERT_CONVENTION line, all required content per contract must_contain list."
      linked_ids: [claim-kms-derivation, claim-local-equilibrium, claim-modular-boost, test-kms-derived, test-2pi-factor, test-theta-sigma-zero, test-killing-argument, test-unruh-temperature, test-jacobson-input]
  acceptance_tests:
    test-kms-derived:
      status: passed
      summary: "All four steps of the KMS derivation chain verified present: (1) BW gives K_A=2pi K_boost from Plan 01, (2) modular automorphism sigma_t = boost by 2pi*t (Eq. 35.9), (3) Tomita-Takesaki KMS at beta_mod=1 cited from Bratteli-Robinson, (4) conversion to beta_phys=2pi/a. KMS is derived from BW, not assumed. No circularity."
      linked_ids: [claim-kms-derivation, deliv-derivation-35-02, ref-hhw1967, ref-bw-plan01]
    test-2pi-factor:
      status: passed
      summary: "The 2pi factor traced through end-to-end table in Step 5: K_A=2pi K_boost -> sigma_t=boost by 2pi*t -> beta_mod=1 -> t=a*tau/(2pi) -> beta_phys=2pi/a -> T_U=a/(2pi). No factor of 2pi dropped or doubled. The 2pi in T_U descends uniquely from K_A=2pi K_boost."
      linked_ids: [claim-kms-derivation, deliv-derivation-35-02]
    test-theta-sigma-zero:
      status: passed
      summary: "theta=0 derived from Killing equation: nabla_(mu xi_nu)=0 -> trace gives nabla_mu xi^mu=0 (Eq. 35.19). sigma=0 derived from Killing equation: nabla_(mu xi_nu)=0 directly (Eq. 35.21). Both derived from xi^mu being a Killing vector, not assumed."
      linked_ids: [claim-local-equilibrium, deliv-derivation-35-02]
    test-killing-argument:
      status: passed
      summary: "Three-step connection verified: (1) BW identifies modular flow with boost (Plan 01), (2) boost is generated by Killing vector field xi^mu (Step 9), (3) bifurcation surface is where xi^mu=0 (Eq. 35.16). Step (1) is the nontrivial content (attributed to BW), steps (2)-(3) are standard GR."
      linked_ids: [claim-local-equilibrium, deliv-derivation-35-02, ref-bw-plan01]
    test-unruh-temperature:
      status: passed
      summary: "T_U=a/(2pi) derived in Step 5 with proper acceleration a defined via Rindler trajectory (Eq. 35.10): x^0=(1/a)sinh(a*tau), x^1=(1/a)cosh(a*tau). Proper acceleration verified: a^mu a_mu = +a^2. For a=1: T_U=1/(2pi) ~ 0.1592. The derivation flows from BW -> KMS -> proper time conversion."
      linked_ids: [claim-modular-boost, deliv-derivation-35-02, ref-hhw1967]
    test-jacobson-input:
      status: passed
      summary: "Three Jacobson inputs explicitly stated as deliverables to Phase 36: (J1) K_A=2pi K_boost (Plan 01 via BW), (J2) theta=sigma=0 at bifurcation (Steps 10-11 via Killing), (J3) T_U=a/(2pi) (Step 5 via KMS). Jacobson 2016 (PRL 116, 201101) cited as downstream consumer."
      linked_ids: [claim-modular-boost, deliv-derivation-35-02, ref-jacobson2016]
  references:
    ref-hhw1967:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "HHW 1967 (CMP 5, 215) cited in Step 3 for the definition of KMS states and the KMS condition (Eq. 35.8). Used as the foundational characterization of thermal equilibrium for identifying the modular flow as thermal."
    ref-bw-plan01:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Plan 01 BW results cited throughout: K_A=2pi K_boost (Eq. 35.0a) in Steps 2, 4, 13 (J1). Lattice-BW Eq. (35.1) in Step 7. SRF=0.9993 in Steps 7, 14. W1-W6 assessment in Step 1."
    ref-jacobson2016:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Jacobson 2016 (PRL 116, 201101; arXiv:1505.04753) cited in Step 13 as the downstream consumer of the three inputs J1-J3. The entanglement equilibrium argument that derives linearized Einstein equation is Phase 36's deliverable."
    ref-chm2011:
      status: completed
      completed_actions: [cite, compare]
      missing_actions: []
      summary: "Casini-Huerta-Myers (JHEP 1105:036, 2011; arXiv:1102.0440) cited in Step 13 (J1) as cross-check: their modular Hamiltonian K_A=2pi int x_perp T_00 for half-space matches the continuum limit of lattice-BW (Plan 01 Eq. 35.4)."
  forbidden_proxies:
    fp-equilibrium-assumed:
      status: rejected
      notes: "KMS property explicitly DERIVED from BW modular flow (Steps 3-4), not assumed. The derivation chain BW -> TT -> KMS is fully stated."
    fp-unruh-without-acceleration:
      status: rejected
      notes: "T_U = a/(2pi) derived with explicit Rindler observer trajectory (Eq. 35.10) and proper acceleration a defined as magnitude of four-acceleration. Not stated without context."
    fp-bw-circularity:
      status: rejected
      notes: "Step 1 explicitly states the logical order: Phase 34 establishes Lorentz -> Plan 01 applies BW using Lorentz -> Plan 02 derives KMS from BW. No circularity."
  uncertainty_markers:
    weakest_anchors:
      - "KMS condition on finite lattice is formal (Gibbs state interpretation), becoming rigorous KMS only in the thermodynamic limit (type III algebras)"
      - "Local equilibrium (theta=sigma=0) is a geometric consequence of Killing symmetry, which is exact in the continuum but approximate on the lattice"
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations:
      - "If the entanglement spectrum of the restricted ground state were NOT thermal (not Boltzmann-distributed), the KMS identification would fail -- SRF=0.9993 provides evidence against this"
      - "If the boost Killing vector did not vanish at the bifurcation surface (geometrically impossible), local equilibrium would fail"

duration: 7min
completed: 2026-03-30
---

# Phase 35, Plan 02: KMS Equilibrium and Modular Hamiltonian Summary

**KMS property derived from BW modular flow at beta=2pi, Unruh temperature T_U=a/(2pi) obtained, local equilibrium theta=sigma=0 at bifurcation surface from Killing symmetry**

## Performance

- **Duration:** 7 min
- **Started:** 2026-03-30T13:27:09Z
- **Completed:** 2026-03-30T13:34:00Z
- **Tasks:** 2
- **Files modified:** 1

## Key Results

- KMS property at beta=2pi DERIVED from BW identification K_A = 2pi K_boost via Tomita-Takesaki modular theory (not assumed) [CONFIDENCE: HIGH]
- Unruh temperature T_U = a/(2pi) derived with 2pi factor traced end-to-end from K_A to T_U; for a=1, T_U = 1/(2pi) ~ 0.1592 [CONFIDENCE: HIGH]
- Local equilibrium theta=sigma=0 at bifurcation surface derived as exact geometric identity from Killing equation [CONFIDENCE: HIGH]
- Three Jacobson inputs (J1: modular Hamiltonian = boost, J2: local equilibrium, J3: Unruh temperature) explicitly packaged for Phase 36 [CONFIDENCE: HIGH for individual results, MEDIUM-HIGH for full chain including lattice-BW]

## Task Commits

1. **Task 1: KMS property from BW and modular Hamiltonian = boost identification** - `ae8df50` (derive)
2. **Task 2: Local equilibrium at bifurcation surface and Jacobson input summary** - `c4909fe` (derive)

## Files Created/Modified

- `derivations/35-kms-equilibrium-and-modular-hamiltonian.md` - Complete derivation: Part I (KMS from BW, Steps 1-7), Part II (local equilibrium, Steps 8-12), Part III (Jacobson inputs, Steps 13-15)

## Next Phase Readiness

Phase 36 (Jacobson's entanglement equilibrium argument) has all three required inputs:
- **(J1)** K_A = 2pi K_boost (Plan 01, Eq. 35.0a)
- **(J2)** theta = sigma = 0 at bifurcation surface (Plan 02, Eqs. 35.19, 35.21)
- **(J3)** T_U = a/(2pi) (Plan 02, Eq. 35.3)

These combine with the entanglement first law delta S_A = delta <K_A> to yield the linearized Einstein equation.

## Contract Coverage

- Claim IDs advanced: claim-kms-derivation -> passed, claim-local-equilibrium -> passed, claim-modular-boost -> passed
- Deliverable IDs produced: deliv-derivation-35-02 -> derivations/35-kms-equilibrium-and-modular-hamiltonian.md (passed)
- Acceptance test IDs run: test-kms-derived -> passed, test-2pi-factor -> passed, test-theta-sigma-zero -> passed, test-killing-argument -> passed, test-unruh-temperature -> passed, test-jacobson-input -> passed
- Reference IDs surfaced: ref-hhw1967 -> cited, ref-bw-plan01 -> cited, ref-jacobson2016 -> cited, ref-chm2011 -> cited+compared
- Forbidden proxies rejected: fp-equilibrium-assumed -> rejected, fp-unruh-without-acceleration -> rejected, fp-bw-circularity -> rejected

## Equations Derived

**Eq. (35.7):** Modular automorphism group

$$
\sigma_t(A) = \Delta^{it} \, A \, \Delta^{-it}
$$

**Eq. (35.8):** KMS condition at beta_mod = 1

$$
F_{A,B}(t) = \omega(A \, \sigma_t(B)), \quad F_{A,B}(t + i) = \omega(\sigma_t(B) \, A)
$$

**Eq. (35.9):** Modular flow = boost

$$
\sigma_t(A) = U(\Lambda(-2\pi t)) \, A \, U(\Lambda(-2\pi t))^{-1}
$$

**Eq. (35.3):** Unruh temperature

$$
T_U = \frac{a}{2\pi}
$$

**Eq. (35.15):** Boost Killing vector

$$
\xi^\mu \partial_\mu = x^1 \, \partial_0 + c_s^2 \, x^0 \, \partial_1
$$

**Eq. (35.19):** Expansion vanishes (from Killing equation)

$$
\theta = \nabla_\mu \xi^\mu = 0
$$

**Eq. (35.21):** Shear vanishes (from Killing equation)

$$
\sigma_{\mu\nu} = 0
$$

## Validations Completed

- 2pi factor traced end-to-end (6-row table): K_A=2pi K_boost -> sigma_t=boost by 2pi*t -> beta_mod=1 -> t=a*tau/(2pi) -> beta_phys=2pi/a -> T_U=a/(2pi). No factor doubled or dropped.
- Rindler observer four-velocity normalization: u^mu u_mu = -1 (timelike, correctly normalized in (-,+,...,+) metric)
- Rindler observer proper acceleration: a^mu a_mu = +a^2 (correct magnitude)
- theta = 0: follows from trace of Killing equation (exact, not approximation)
- sigma = 0: follows from Killing equation directly (exact)
- Lattice cross-check: position-dependent beta_eff(x_perp) = 2pi x_perp / c_s reproduces continuum Rindler temperature profile
- KMS derivation is non-circular: Phase 34 (Lorentz) -> Plan 01 (BW) -> Plan 02 (KMS), no step uses a later result
- Self-critique checkpoints at Steps 4 and 5: sign, factor, convention, dimension checks all passed

## Decisions & Deviations

None -- followed plan as specified.

## Open Questions

- How does the entanglement first law delta S_A = delta <K_A> combine with J1-J3 to yield the linearized Einstein equation? (Phase 36 deliverable)
- What is the precise form of the lattice corrections to local equilibrium (theta, sigma not exactly zero on the lattice)?

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
|----------|--------|-------|-------------|--------|-------------|
| Unruh temperature (a=1) | T_U | 1/(2pi) ~ 0.1592 | exact (analytic) | Derived from BW + TT KMS | All a > 0 |
| Physical inverse temp | beta_phys | 2pi/a | exact (analytic) | Derived from modular-to-proper time | All a > 0 |
| Modular inverse temp | beta_mod | 1 | exact (Tomita-Takesaki) | TT theorem | Modular time parameter |
| SRF | SRF | 0.9993 | numerical (Paper 6) | Paper 6 Phase 11 | L >= 4, Heisenberg AFM |

## Approximations Used

| Approximation | Valid When | Error Estimate | Breaks Down At |
|---------------|-----------|----------------|----------------|
| Lattice-BW ansatz | a/L << 1, Lorentz-invariant low-energy theory | O((a/L)^2) | L ~ a or Lorentz violation |
| Half-space approx | R/L_curv << 1 (flat emergent spacetime) | O(R^2/L_curv^2) | Strong gravitational fields |

---

_Phase: 35-bw-theorem-and-local-equilibrium, Plan: 02_
_Completed: 2026-03-30_
