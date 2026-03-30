---
phase: 35-bw-theorem-and-local-equilibrium
plan: 01
depth: full
one-liner: "BW prerequisites assessed (W1-W4 satisfied, W5 conditional, W6 open), lattice-BW entanglement Hamiltonian H_ent=(2pi/c_s)*sum x_perp h_x constructed, SRF=0.9993 validated as BW fingerprint"
subsystem: [derivation]
tags: [bisognano-wichmann, wightman-axioms, entanglement-hamiltonian, lattice-bw, modular-hamiltonian, type-III, reflection-positivity, srf]

requires:
  - phase: 34-emergent-lorentz-invariance
    plan: 01
    provides: "Lorentz invariance from sigma model rescaling + Wick rotation, DLS reflection positivity, Eq. (34.16), Eq. (34.30)"
  - phase: 34-emergent-lorentz-invariance
    plan: 02
    provides: "c_s = 1.659 Ja, emergent metric ds^2 = -c_s^2 dt^2 + dx^2"

provides:
  - "BWEQ-01: BW prerequisites assessed -- Wightman axioms W1-W4 satisfied, W5 conditional, W6 open"
  - "Lattice-BW entanglement Hamiltonian Eq. (35.1): H_ent^{BW} = (2pi/c_s) sum x_perp h_x"
  - "SRF = 0.9993 connected to BW locality prediction"
  - "Type I (lattice) vs type III (continuum) gap honestly stated"
  - "Effective inverse temperature beta_eff(x_perp) = 2pi x_perp / c_s (Eq. 35.2)"

affects: [35-plan-02-kms-local-equilibrium, 36-jacobson-assembly]

methods:
  added: [wightman-axiom-assessment, lattice-bw-construction, modular-hamiltonian-analysis]
  patterns: [lattice-fingerprint-of-continuum-result, type-gap-honest-statement]

key-files:
  created:
    - derivations/35-bw-axioms-and-lattice-bw.md

key-decisions:
  - "Used lattice-BW route (Giudici et al.) as primary, continuum BW as theoretical motivation"
  - "W6 (existence of Wightman distributions) stated as open problem, not assumed"
  - "Type I/III gap honestly stated: lattice = type I, continuum = type III, lattice-BW is the bridge"

patterns-established:
  - "lattice-fingerprint: continuum BW result has a lattice analog that becomes exact in the double limit"
  - "honest-type-gap: always state the operator algebra type when discussing modular theory"

conventions:
  - "natural_units=natural, hbar=1, k_B=1, a=1"
  - "metric_signature=mostly_minus (-,+,...,+) for emergent Lorentzian spacetime"
  - "modular_hamiltonian=K_A=-ln(rho_A), rho_A=e^{-K_A}/Z"
  - "kms_temperature=beta=2pi for Rindler wedge"
  - "coupling_convention=J>0 AFM"

plan_contract_ref: ".gpd/phases/35-bw-theorem-and-local-equilibrium/35-01-PLAN.md#/contract"

contract_results:
  claims:
    claim-bw-prerequisites:
      status: passed
      summary: "All six Wightman axioms individually assessed for O(3) NL sigma model: W1-W4 satisfied, W5 conditionally satisfied, W6 not rigorously established (open constructive QFT problem). Lattice-BW route (Giudici et al.) stated as primary mitigation for W6 gap. DLS 1978 reflection positivity cited from Phase 34. Lorentz invariance cited from Phase 34 Eq. (34.30)."
      linked_ids: [deliv-derivation-35-01, test-axiom-checklist, test-rp-citation, ref-bw1975, ref-dls1978, ref-phase34-lorentz]
    claim-lattice-bw:
      status: passed
      summary: "Lattice-BW entanglement Hamiltonian H_ent^{BW} = (2pi/c_s) sum x_perp h_x constructed with correct 2pi factor. SRF = 0.9993 connected as numerical validation of BW locality prediction. Dimensional analysis verified: H_ent is dimensionless."
      linked_ids: [deliv-derivation-35-01, test-srf-connection, test-lattice-bw-formula, ref-giudici2018, ref-srf-paper6]
    claim-type-gap:
      status: passed
      summary: "Type I (lattice, matrix algebra) vs type III_1 (continuum, Haag 1996) gap explicitly stated. No claim that lattice algebra is type III. Lattice-BW is the bridge via continuum limit correspondence with O((a/L)^2) corrections."
      linked_ids: [deliv-derivation-35-01, test-type-gap-stated, ref-giudici2018]
  deliverables:
    deliv-derivation-35-01:
      status: passed
      path: "derivations/35-bw-axioms-and-lattice-bw.md"
      summary: "Complete derivation document with three parts: (I) BW theorem statement + Wightman axiom checklist + OS reflection positivity, (II) lattice-BW construction + dimensional analysis + SRF connection, (III) type I/III gap statement. All required content present per contract must_contain list."
      linked_ids: [claim-bw-prerequisites, claim-lattice-bw, claim-type-gap, test-axiom-checklist, test-rp-citation, test-srf-connection, test-lattice-bw-formula, test-type-gap-stated]
  acceptance_tests:
    test-axiom-checklist:
      status: passed
      summary: "All six Wightman axioms listed with individual status: W1 satisfied (standard QFT), W2 satisfied (Phase 34 Lorentz), W3 satisfied (positive spin-wave energy), W4 satisfied (microcausality from Lorentz action), W5 conditionally satisfied (unique Neel vacuum for d>=2, cyclicity from Reeh-Schlieder), W6 not rigorously established (constructive QFT gap). The lattice-BW bypass is explicitly stated."
      linked_ids: [claim-bw-prerequisites, deliv-derivation-35-01, ref-bw1975]
    test-rp-citation:
      status: passed
      summary: "DLS 1978 reflection positivity cited from Phase 34, Step 11 (not re-derived). Lorentz invariance cited from Phase 34 Eq. (34.30) (not re-derived). Both prior results referenced with equation numbers."
      linked_ids: [claim-bw-prerequisites, deliv-derivation-35-01, ref-dls1978, ref-phase34-lorentz]
    test-srf-connection:
      status: passed
      summary: "SRF = 0.9993 explicitly stated as numerical validation of BW locality. Logical chain written out: BW predicts K_A ~ sum x_perp h_x (local) -> h_x is nearest-neighbor (range 1) -> K_A dominated by range-1 Pauli strings -> SRF close to 1. The 0.07% non-NN weight represents O((a/L)^2) corrections."
      linked_ids: [claim-lattice-bw, deliv-derivation-35-01, ref-srf-paper6, ref-giudici2018]
    test-lattice-bw-formula:
      status: passed
      summary: "Dimensions verified step by step: [H_ent] = [1/c_s]*[x_perp]*[h_x] = [1/J]*[1]*[J] = dimensionless. The 2pi factor is present and traced to K_A = 2pi K_boost (Eq. 35.0a). Python Level 5 numerical verification confirms beta_eff(1) = 2pi/1.659 = 3.787/J."
      linked_ids: [claim-lattice-bw, deliv-derivation-35-01]
    test-type-gap-stated:
      status: passed
      summary: "Three required statements all present: (1) lattice algebras are type I (matrix algebras), stated in Step 11a. (2) BW in the strict sense is a type III result, stated in Step 11b. (3) Lattice-BW bridges the gap via continuum limit correspondence, stated in Step 11c. No claim that the lattice algebra is type III."
      linked_ids: [claim-type-gap, deliv-derivation-35-01]
  references:
    ref-bw1975:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "BW 1975 (JMP 16, 985) and BW 1976 (JMP 17, 303) cited as source of the theorem K_A = 2pi K_boost. Precise hypotheses (Wightman axioms) stated."
    ref-giudici2018:
      status: completed
      completed_actions: [cite, compare]
      missing_actions: []
      summary: "Giudici et al. 2018 (PRB 98, 134403) cited as source and validation of lattice-BW ansatz. Compared with project's SRF = 0.9993 as independent numerical validation."
    ref-dls1978:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Dyson-Lieb-Simon 1978 reflection positivity cited from Phase 34, Step 11. Not re-derived."
    ref-phase34-lorentz:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Phase 34 Lorentz invariance (Eq. 34.30) cited as input. Not re-derived."
    ref-srf-paper6:
      status: completed
      completed_actions: [cite, compare]
      missing_actions: []
      summary: "SRF = 0.9993 from Paper 6 Phase 11 cited and connected to BW locality prediction. Comparison: BW predicts SRF ~ 1, measured 0.9993, consistent."
  forbidden_proxies:
    fp-bw-before-lorentz:
      status: rejected
      notes: "BW theorem cited as applying to the Lorentz-invariant theory. Lorentz invariance established first in Phase 34. No circularity."
    fp-wightman-assumed:
      status: rejected
      notes: "Each Wightman axiom assessed individually in Step 2 table. W6 explicitly stated as not rigorously established. No blanket assumption."
    fp-type-iii-on-lattice:
      status: rejected
      notes: "Step 11 explicitly states lattice algebra is type I (matrix algebra). Type III only in continuum limit. No claim of type III on lattice."
  uncertainty_markers:
    weakest_anchors:
      - "Giudici et al. lattice-BW is numerical evidence, not a rigorous theorem. No proof of convergence to BW form in continuum limit for O(3) NL sigma model."
      - "Wightman axioms for the d >= 2 NL sigma model are not rigorously established (open constructive QFT problem)."
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations:
      - "If SRF were < 0.9, K_A would not be local and the BW approximation would be invalid for this model."
      - "If the lattice-BW entanglement spectrum disagreed qualitatively with exact K_A (wrong level ordering), the ansatz would be inappropriate."

duration: 3min
completed: 2026-03-30
---

# Phase 35, Plan 01: BW Axioms and Lattice-BW Entanglement Hamiltonian

**BW prerequisites assessed (W1-W4 satisfied, W5 conditional, W6 open), lattice-BW entanglement Hamiltonian H_ent=(2pi/c_s) sum x_perp h_x constructed, SRF=0.9993 validated as BW fingerprint**

## Performance

- **Duration:** 3 min
- **Started:** 2026-03-30T13:20:00Z
- **Completed:** 2026-03-30T13:23:13Z
- **Tasks:** 2
- **Files modified:** 1

## Key Results

- **BWEQ-01 (Wightman axioms):** W1-W4 satisfied for O(3) NL sigma model; W5 conditionally satisfied (unique Neel vacuum for d >= 2); W6 not rigorously established (constructive QFT gap). Lattice-BW route bypasses W6 requirement. [CONFIDENCE: HIGH -- individual axiom assessments are standard, the W6 gap is well-known]
- **Lattice-BW formula (Eq. 35.1):** $H_{\text{ent}}^{\text{BW}} = (2\pi/c_s) \sum_{x \in A} x_\perp \, h_x$ with $c_s = 1.659 \, Ja$, dimensionally verified as dimensionless. [CONFIDENCE: HIGH -- standard result from Giudici et al., dimensional analysis verified]
- **SRF validation:** SRF = 0.9993 confirms BW locality prediction -- 99.93% of K_A weight in nearest-neighbor terms. [CONFIDENCE: HIGH -- numerical result from Paper 6]
- **Type I/III gap:** Lattice algebras are type I (matrix algebras); BW applies rigorously only to type III_1 algebras in the continuum; lattice-BW bridges this gap with O((a/L)^2) corrections. [CONFIDENCE: HIGH -- standard operator algebra classification]

## Task Commits

1. **Task 1: BW prerequisites -- Wightman axiom checklist + OS reflection positivity** - `93e0ff2` (derive)
2. **Task 2: Lattice-BW construction + SRF validation + type I/III gap** - `25948ea` (derive)

## Files Created/Modified

- `derivations/35-bw-axioms-and-lattice-bw.md` - Complete derivation: Part I (BW theorem + Wightman axioms + OS-RP), Part II (lattice-BW + dim. analysis + SRF), Part III (type gap)

## Next Phase Readiness

- Lattice-BW entanglement Hamiltonian (Eq. 35.1) ready for Plan 02 (KMS condition and local equilibrium)
- Effective inverse temperature beta_eff(x_perp) = 2pi x_perp / c_s available for Unruh temperature derivation
- SRF validation confirms K_A locality -- supports modular flow interpretation in Plan 02
- Type I/III gap honestly stated -- Plan 02 and Phase 36 can proceed without overclaiming

## Contract Coverage

- claim-bw-prerequisites -> passed (W1-W4 satisfied, W5 conditional, W6 open, lattice-BW bypass)
- claim-lattice-bw -> passed (Eq. 35.1 constructed, SRF = 0.9993 connected, dimensional analysis verified)
- claim-type-gap -> passed (type I lattice, type III continuum, lattice-BW bridge stated)
- deliv-derivation-35-01 -> passed (derivations/35-bw-axioms-and-lattice-bw.md)
- test-axiom-checklist -> passed (all 6 axioms individually assessed)
- test-rp-citation -> passed (DLS 1978 and Phase 34 Lorentz cited, not re-derived)
- test-srf-connection -> passed (logical chain BW -> local K_A -> high SRF written out)
- test-lattice-bw-formula -> passed (dimensional analysis + 2pi factor traced + Python verification)
- test-type-gap-stated -> passed (three required statements all present)
- ref-bw1975 -> completed (cited)
- ref-giudici2018 -> completed (cited, compared with SRF)
- ref-dls1978 -> completed (cited from Phase 34)
- ref-phase34-lorentz -> completed (cited from Phase 34)
- ref-srf-paper6 -> completed (cited, compared)
- fp-bw-before-lorentz -> rejected (Lorentz from Phase 34 first)
- fp-wightman-assumed -> rejected (each axiom individually assessed)
- fp-type-iii-on-lattice -> rejected (lattice stated as type I)

## Equations Derived

**Eq. (35.0a): BW theorem (modular Hamiltonian form)**

$$
K_A = 2\pi K_{\text{boost}}
$$

**Eq. (35.1): Lattice-BW entanglement Hamiltonian**

$$
H_{\text{ent}}^{\text{BW}}(A) = \frac{2\pi}{c_s} \sum_{x \in A} x_\perp \, h_x
$$

**Eq. (35.2): Effective inverse temperature**

$$
\beta_{\text{eff}}(x_\perp) = \frac{2\pi \, x_\perp}{c_s}
$$

**Eq. (35.3): Lattice-BW accuracy**

$$
K_A^{\text{exact}} = H_{\text{ent}}^{\text{BW}} + O\!\left(\frac{a^2}{L^2}\right)
$$

**Eq. (35.4): Continuum limit (CHM modular Hamiltonian)**

$$
H_{\text{ent}}^{\text{BW}} \longrightarrow 2\pi \int_A d^d x \; \frac{x_\perp}{c_s} \, T_{00}(x)
$$

## Validations Completed

- Dimensional analysis: [H_ent^{BW}] = [1/J] * [1] * [J] = dimensionless (verified step by step in Step 7)
- 2pi factor traced from K_A = 2pi K_boost through lattice discretization (Step 8)
- beta_eff(1) = 2pi/1.659 = 3.787/J verified by Python (Level 5)
- SRF = 0.9993 connected to BW locality: 99.93% NN weight consistent with K_A ~ sum x_perp h_x (Step 9)
- Type I/III classification: lattice = type I (matrix algebra), continuum = type III_1 (Step 11)
- No Phase 34 results re-derived: DLS 1978 and Eq. (34.30) cited as inputs
- No circular reasoning: Lorentz (Phase 34) -> BW (Phase 35), not the reverse

## Decisions & Deviations

### Decisions

- Used lattice-BW (Giudici et al.) as primary route, continuum BW as theoretical motivation
- W6 (Wightman distributions) stated as open problem -- no pretense of rigorous resolution
- Both tasks written to same derivation file (plan specifies same output)

### Deviations from Plan

None -- plan executed as specified.

## Approximations Used

| Approximation | Valid When | Error Estimate | Breaks Down At |
|---------------|-----------|----------------|----------------|
| Lattice-BW ansatz | a/L << 1, low-energy Lorentz-invariant | O((a/L)^2) | L ~ a (single-site subsystem) |
| Half-space bipartition (flat cut) | R/L_curv << 1 | O(R^2/L_curv^2) | Curved boundaries |

## Open Questions

- Can the O((a/L)^2) error in Eq. (35.3) be rigorously bounded for the O(3) sigma model?
- Does the lattice-BW ansatz extend to more general (non-planar) entanglement cuts?
- How does the type I -> type III transition manifest quantitatively as system size increases?

## Self-Check: PASSED

- [x] derivations/35-bw-axioms-and-lattice-bw.md exists
- [x] Commit 93e0ff2 exists (Task 1)
- [x] Commit 25948ea exists (Task 2)
- [x] All contract IDs covered (3 claims, 1 deliverable, 5 acceptance tests, 5 references, 3 forbidden proxies)
- [x] No forbidden proxies violated
- [x] Python numerical verification (Level 5) for beta_eff
- [x] Convention assertion line present in derivation file
- [x] All anchor references cited

---

_Phase: 35-bw-theorem-and-local-equilibrium_
_Plan: 01_
_Completed: 2026-03-30_
