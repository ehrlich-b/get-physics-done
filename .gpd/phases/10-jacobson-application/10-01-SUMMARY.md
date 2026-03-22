---
phase: 10-jacobson-application
plan: 01
depth: full
one-liner: "Established Wilsonian continuum limit framework mapping lattice area law to G = 1/(4 eta), formulated MVEH as Assumption A5 with MaxEnt motivation and explicit gap, produced Jacobson input status table (J1 established, J2 exact, J3 assumed)"
subsystem: formalism
tags: [jacobson, continuum-limit, wilsonian, MVEH, area-law, newton-constant, entanglement-equilibrium, assumption-register]

requires:
  - phase: 09-area-law-derivation
    plan: 03
    provides: "Area-law synthesis (Eqs. 09-03.1--09-03.7), entanglement first law (Eq. 09-03.3), Jacobson bridge (J1)-(J3), assumption register A1-A4"
  - phase: 08-locality-formalization
    plan: 03
    provides: "v_LR = 8eJ/(e-1) (Eq. 08-03.3), LR bound constants, Paper 5 compatibility"
provides:
  - "Wilsonian continuum limit framework: lattice as UV completion, emergent smooth manifold at L >> a"
  - "Lattice-to-continuum mapping: S = eta * A_phys, eta = eta_lattice / a^{d-1}, G = 1/(4 eta)"
  - "Channel capacity bound on G: G >= a^{d-1} / (4 log(n)), so a ~ l_Planck"
  - "v_LR -> c (emergent speed of light)"
  - "MVEH formulated as Assumption A5 with MaxEnt motivation and gap statement"
  - "Complete assumption register A1-A5"
  - "Jacobson input status table: (J1) established, (J2) exact, (J3) assumed as A5"
  - "CHM formula with conformal restriction and Speranza nonconformal corrections"
  - "UV/matter entropy decomposition S = S_UV + S_mat"
affects: [10-jacobson-application/plan-02, 10-jacobson-application/plan-03, paper-6]

methods:
  added: [Wilsonian continuum limit, Jacobson 2012 G = 1/(4 eta) identification, CHM modular Hamiltonian, Speranza nonconformal corrections]
  patterns: [lattice-to-continuum mapping via dimensional rescaling, assumption register with gap tracking]

key-files:
  created:
    - derivations/10-jacobson-inputs.md
    - .gpd/phases/10-jacobson-application/10-01-SUMMARY.md

key-decisions:
  - "Wilsonian argument framed as physical (not rigorous); no attempt to construct continuum limit"
  - "MVEH stated as Assumption A5, not derived; gap statement identifies what self-modeling property would establish it"
  - "Conformal restriction stated honestly: Jacobson 2016 rigorous for CFT only; nonconformal case conjectured with Speranza corrections"
  - "1D AFM Heisenberg chain identified as the most controlled case (exact CFT)"

patterns-established:
  - "Assumption register A1-A5 is the canonical assumption tracker for the self-modeling -> GR argument"
  - "Jacobson input status table (J1)-(J3) tracks delivered vs assumed ingredients"
  - "Lattice quantities map to continuum via powers of a: area -> a^{d-1}, eta -> 1/a^{d-1}, G -> a^{d-1}"

conventions:
  - "natural units (hbar = c = k_B = 1)"
  - "metric (-,+,+,+)"
  - "entropy: von Neumann S = -Tr(rho ln rho), nats"
  - "K_A = -ln(rho_A) (modular Hamiltonian)"
  - "H = sum h_xy (no 1/2)"
  - "G_ab = R_ab - (1/2) R g_ab (Einstein tensor)"
  - "G = 1/(4 eta) (Jacobson 2012)"

plan_contract_ref: ".gpd/phases/10-jacobson-application/10-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-continuum-framework:
      status: passed
      summary: "Wilsonian continuum limit framework established (Parts A-D): lattice as UV completion, emergent smooth manifold, lattice-to-continuum mapping with eta = eta_lattice/a^{d-1} and G = 1/(4 eta), conformal restriction stated with Speranza corrections. All dimensional checks pass."
      linked_ids: [deliv-jacobson-inputs, test-continuum-dimensional, test-entropy-area-mapping, ref-jacobson2016-inputs, ref-jacobson2012-inputs]
    claim-mveh-status:
      status: passed
      summary: "MVEH formulated as Assumption A5 (not proven/derived). MaxEnt motivation given with three non-rigorous steps identified. Gap statement: what self-modeling property would establish A5? Disconfirmation criteria stated."
      linked_ids: [deliv-jacobson-inputs, test-mveh-not-claimed-proven, test-assumption-register, ref-jacobson2016-inputs]
    claim-input-status:
      status: passed
      summary: "All three Jacobson inputs have explicit status: (J1) established under A3 (Phase 9 Eq. 09-03.6), (J2) exact identity (Phase 9 Eq. 09-03.3), (J3) assumed as A5 (this plan Part E). Jacobson input status table in Part G."
      linked_ids: [deliv-jacobson-inputs, test-three-inputs-explicit, ref-jacobson2016-inputs, ref-phase9-synthesis]
  deliverables:
    deliv-jacobson-inputs:
      status: passed
      path: derivations/10-jacobson-inputs.md
      summary: "Parts A-H: Wilsonian framework, lattice-to-continuum mapping (Eqs. 10-01.1--10-01.9), emergent geometry table, conformal restriction with CHM formula (Eq. 10-01.10), Speranza corrections (Eq. 10-01.12), MVEH as A5 (Eqs. 10-01.14--10-01.18), MaxEnt motivation, gap statement, assumption register A1-A5, Jacobson input status table, Plan 02 input summary"
      linked_ids: [claim-continuum-framework, claim-mveh-status, claim-input-status]
  acceptance_tests:
    test-continuum-dimensional:
      status: passed
      summary: "[eta] = [1/length^{d-1}], [G] = [length^{d-1}], [G * eta] = [dimensionless] = 1/4. All verified in Part B (Eqs. 10-01.3, 10-01.5). Cross-check in self-critique checkpoint."
      linked_ids: [claim-continuum-framework, deliv-jacobson-inputs, ref-jacobson2012-inputs]
    test-entropy-area-mapping:
      status: passed
      summary: "S_lattice = eta_lattice * |bd| maps to S_continuum = eta * A_phys with eta = eta_lattice / a^{d-1} (Eq. 10-01.3). Channel capacity gives eta_lattice <= log(n), so G >= a^{d-1}/(4 log(n)) (Eq. 10-01.6). Mapping is consistent and reproduces expected Planck-scale identification."
      linked_ids: [claim-continuum-framework, deliv-jacobson-inputs, ref-phase9-synthesis]
    test-mveh-not-claimed-proven:
      status: passed
      summary: "MVEH is explicitly called 'Assumption A5' (Part E.3), 'PHYSICAL ARGUMENT, not a proof' (Part E.4), 'ASSUMPTION, not a theorem' (Part E.3). No claim of derivation. Gap statement present (Part E.5)."
      linked_ids: [claim-mveh-status, deliv-jacobson-inputs]
    test-assumption-register:
      status: passed
      summary: "A1-A5 all present in Part F table with 6 columns: ID, Assumption name, Statement, Status, What It Buys, What Fails Without It. Hierarchy and logical dependence diagram included."
      linked_ids: [claim-mveh-status, deliv-jacobson-inputs, ref-phase9-synthesis]
    test-three-inputs-explicit:
      status: passed
      summary: "(J1) status: Established under A3, source: Phase 9 Eq. 09-03.6. (J2) status: Exact identity, source: Phase 9 Eq. 09-03.3. (J3) status: Assumed as A5, source: this plan Part E. All three rows present in Part G table."
      linked_ids: [claim-input-status, deliv-jacobson-inputs, ref-jacobson2016-inputs, ref-phase9-synthesis]
  references:
    ref-jacobson2016-inputs:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Jacobson 2016 PRL 116, 201101 cited as the derivation template throughout. Three inputs (J1)-(J3) from this paper structure the entire plan. MVEH definition and CFT equivalence from this paper."
    ref-jacobson2012-inputs:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Jacobson 2012 IJMPD 21, 1242006 cited for G = 1/(4 eta) identification (Eq. 10-01.5) and UV/IR entropy decomposition (Part E.2)."
    ref-phase9-synthesis:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Phase 9 synthesis (derivations/09-area-law-synthesis.md) cited for (J1) Eq. 09-03.6, (J2) Eq. 09-03.3, assumption register A1-A4 (inherited into A1-A5). Phase 10 interface from Part J used to structure this plan."
  forbidden_proxies:
    fp-mveh-proven:
      status: rejected
      notes: "MVEH explicitly stated as 'Assumption A5' and 'PHYSICAL ARGUMENT, not a proof'. Gap statement identifies what would establish it. Disconfirmation criteria stated."
    fp-lattice-raychaudhuri:
      status: rejected
      notes: "Part C.2 explicitly lists Raychaudhuri equation as a continuum object with no lattice analogue. 'Writing a lattice Raychaudhuri equation would be a category error.' No continuum geometry applied to finite lattice."
    fp-cite-jacobson-no-connect:
      status: rejected
      notes: "Each Jacobson input (J1)-(J3) individually connected to self-modeling lattice results. (J1) via Phase 9 delta S. (J2) via Phase 9 entanglement first law. (J3) via A5 formulation with MaxEnt motivation. Not just cited."
  uncertainty_markers:
    weakest_anchors:
      - "A5 (MVEH): motivated by MaxEnt reasoning but not proven. For CFT, equivalent to Einstein's equation (Jacobson 2016). For non-CFT self-modeling lattice, no derivation exists."
      - "Continuum limit: standard Wilsonian argument but not rigorously constructed. Assumes smooth emergent manifold at long wavelengths."
      - "Conformal restriction: CHM formula exact only for CFT. Nonconformal corrections O((mR)^{2 Delta}) from Speranza 2016; window a << R << 1/m may be empty."
    unvalidated_assumptions:
      - "A5 (MVEH): not derived from self-modeling axioms"
      - "Wilsonian continuum limit: standard physics assumption, not rigorous construction"
      - "Conformal window existence: depends on IR mass scale m vs lattice scale 1/a"
    competing_explanations: []
    disconfirming_observations:
      - "If the self-modeling equilibrium does NOT maximize entanglement among states with same T_ab (A5 fails), Einstein's equations do not follow from this argument"
      - "If the continuum limit produces non-Riemannian geometry, the Raychaudhuri equation and Jacobson derivation do not apply"
      - "If no conformal window exists (m ~ 1/a), the CHM formula is inapplicable and the derivation requires the nonconformal extension (Jacobson Section IV conjecture)"

comparison_verdicts:
  - subject_id: test-continuum-dimensional
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-jacobson2012-inputs
    comparison_kind: benchmark
    metric: dimensional_consistency
    threshold: "[G * eta] = dimensionless = 1/4"
    verdict: pass
    recommended_action: "None -- dimensional analysis is consistent"
    notes: "All dimensional checks pass: [G] = [length^{d-1}], [eta] = [1/length^{d-1}], [G*eta] = 1/4"
  - subject_id: test-entropy-area-mapping
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-phase9-synthesis
    comparison_kind: cross_method
    metric: mapping_consistency
    threshold: "S_lattice = S_continuum under mapping"
    verdict: pass
    recommended_action: "None -- mapping is tautologically consistent"
    notes: "S_lattice = eta_lattice * |bd| = (eta * a^{d-1}) * (A/a^{d-1}) = eta * A = S_continuum"
  - subject_id: test-three-inputs-explicit
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-jacobson2016-inputs
    comparison_kind: benchmark
    metric: logical_completeness
    threshold: "all three Jacobson inputs (J1)-(J3) addressed"
    verdict: pass
    recommended_action: "Proceed to Plan 02 with (J1), (J2) delivered and (J3) assumed as A5"
    notes: "(J1) established under A3, (J2) exact identity, (J3) assumed as A5. Plan 02 derivation is conditional on A5."

duration: 8min
completed: 2026-03-22
---

# Plan 10-01: Wilsonian Continuum Limit and Jacobson Input Preparation

**Established Wilsonian continuum limit framework mapping lattice area law to G = 1/(4 eta), formulated MVEH as Assumption A5 with MaxEnt motivation and explicit gap, produced Jacobson input status table (J1 established, J2 exact, J3 assumed)**

## Performance

- **Duration:** ~8 min
- **Started:** 2026-03-22T12:07:11Z
- **Completed:** 2026-03-22T12:15:00Z
- **Tasks:** 2
- **Files modified:** 1

## Key Results

- **Wilsonian continuum limit:** Lattice as UV completion; smooth manifold emerges at $L \gg a$. Standard Wilsonian argument, not rigorous construction. [CONFIDENCE: MEDIUM -- standard physics but not rigorously proven for the self-modeling lattice]
- **Lattice-to-continuum mapping:** $\eta = \eta_{\text{lattice}}/a^{d-1}$, $G = 1/(4\eta)$ (Jacobson 2012), $a \sim \ell_P \sqrt{\log n}$, $v_{LR} \to c$. All dimensional checks pass. [CONFIDENCE: HIGH for the mapping itself; MEDIUM for the physical identification]
- **MVEH as Assumption A5:** Formulated with MaxEnt motivation; explicitly NOT claimed as proven. Gap statement: what self-modeling property would establish A5? [CONFIDENCE: HIGH for the formulation; the assumption itself is the main open question]
- **Assumption register A1-A5 complete** with status, utility, and failure mode for each [CONFIDENCE: HIGH]
- **Jacobson input status table:** (J1) established under A3, (J2) exact identity, (J3) assumed as A5 [CONFIDENCE: HIGH]
- **Conformal restriction:** CHM formula exact for CFT (1D AFM Heisenberg), approximate in window $a \ll R \ll 1/m$, with Speranza corrections $O((mR)^{2\Delta})$ [CONFIDENCE: HIGH]

## Task Commits

1. **Task 1: Wilsonian framework and lattice-to-continuum mapping** - `56eea50` (derive)
2. **Task 2: MVEH as A5, assumption register, Jacobson input table** - `0533005` (derive)

## Files Created/Modified

- `derivations/10-jacobson-inputs.md` -- Parts A-H: Wilsonian picture, lattice-to-continuum mapping (18 equations), emergent geometry table, conformal restriction with Speranza corrections, MVEH as A5 with MaxEnt motivation and gap statement, assumption register A1-A5, Jacobson input status table, Plan 02 input summary

## Next Phase Readiness

- **Plan 02 (Einstein derivation):** Receives all inputs from Part H: Wilsonian framework, CHM formula, MVEH as A5, UV/matter decomposition, Jacobson input status. Ready to derive Einstein's equations.
- **Plan 03 (Conditionality and scope):** Receives assumption register A1-A5 for conditionality analysis.
- **Paper 6:** The assumption register and gap statement provide the honest limitations section.

## Contract Coverage

- Claim IDs advanced: claim-continuum-framework -> passed, claim-mveh-status -> passed, claim-input-status -> passed
- Deliverable IDs produced: deliv-jacobson-inputs -> passed (derivations/10-jacobson-inputs.md)
- Acceptance test IDs run: test-continuum-dimensional -> passed, test-entropy-area-mapping -> passed, test-mveh-not-claimed-proven -> passed, test-assumption-register -> passed, test-three-inputs-explicit -> passed
- Reference IDs surfaced: ref-jacobson2016-inputs -> completed (read, cite), ref-jacobson2012-inputs -> completed (read, cite), ref-phase9-synthesis -> completed (read, cite)
- Forbidden proxies rejected: fp-mveh-proven -> rejected, fp-lattice-raychaudhuri -> rejected, fp-cite-jacobson-no-connect -> rejected
- Decisive comparison verdicts: test-continuum-dimensional -> pass, test-entropy-area-mapping -> pass, test-three-inputs-explicit -> pass

## Equations Derived

**Eq. (10-01.1): Physical area from lattice boundary**

$$A_{\text{phys}} = |\partial(A)| \cdot a^{d-1}$$

**Eq. (10-01.3): Continuum entropy density**

$$\eta = \frac{\eta_{\text{lattice}}}{a^{d-1}}$$

**Eq. (10-01.5): Newton's constant (Jacobson 2012)**

$$G = \frac{1}{4\eta}$$

**Eq. (10-01.6): Channel capacity bound on G**

$$G \geq \frac{a^{d-1}}{4\log(n)}$$

**Eq. (10-01.10): CHM modular Hamiltonian (CFT)**

$$K_B^{\text{CFT}} = 2\pi \int_B d^{d-1}x \; \frac{R^2 - r^2}{2R} \; T_{00}(x)$$

**Eq. (10-01.15): Entanglement equilibrium (MVEH)**

$$\delta S = 0 \quad \text{for vacuum, at fixed } \langle T_{ab} \rangle$$

**Eq. (10-01.17): UV/matter balance**

$$\delta S_{\text{UV}} + \delta S_{\text{mat}} = 0$$

## Validations Completed

- **Dimensional analysis:** $[G \cdot \eta] = [\text{dimensionless}] = 1/4$. $[G] = [\text{length}]^{d-1}$. $[\eta] = [1/\text{length}]^{d-1}$. $[v_{LR}] = [\text{velocity}]$ when $a$ restored. All consistent.
- **Mapping consistency:** $S_{\text{lattice}} = \eta_{\text{lattice}} \cdot |\partial| = (\eta \cdot a^{d-1}) \cdot (A/a^{d-1}) = \eta \cdot A = S_{\text{continuum}}$. Tautological.
- **Flat space limit:** When $R_{abcd} = 0$ and $T_{ab} = 0$, all perturbations vanish, $\delta S_{\text{UV}} = 0$, $\delta S_{\text{mat}} = 0$. Consistent.
- **Forbidden proxy check:** No "lattice Raychaudhuri", no "MVEH proven", no "Jacobson cited without self-modeling connection".
- **Convention consistency:** $(-,+,+,+)$ metric, natural units, $K = -\ln\rho$, $H = \sum h_{xy}$ throughout.
- **MVEH language check:** "Assumption A5", "PHYSICAL ARGUMENT, not a proof", "ASSUMPTION, not a theorem" -- confirmed not overclaimed.
- **CHM dimensional check:** $[K_B^{\text{CFT}}]$ = dimensionless, verified from $[2\pi] \cdot [\text{length}^{d-1}] \cdot [\text{length}] \cdot [T_{00}]$ with $[T_{00}] = [\text{length}^{-d}]$ in natural units.

## Decisions Made

- **Wilsonian not rigorous:** Framed as physical argument following Wilson's RG philosophy, not a rigorous mathematical construction. This is standard for lattice approaches to gravity.
- **MVEH as A5:** The most significant decision. MVEH could not be derived from self-modeling, so it is honestly stated as an assumption with MaxEnt motivation and explicit gap statement.
- **Conformal restriction:** Stated honestly that Jacobson 2016 is rigorous only for CFT. The 1D AFM case ($SU(2)_1$ WZW) is the most controlled; higher dimensions require the nonconformal extension conjecture.
- **1D AFM as best case:** Identified the Heisenberg AFM chain ($n = 2$, $J > 0$) as the case where the Jacobson derivation is most controlled (exact CFT, exact CHM formula).

## Deviations from Plan

None -- plan executed exactly as written.

## Issues Encountered

None.

## Open Questions

- **Can A5 be derived from self-modeling?** This is the central open question for the project. The gap statement (Part E.5) identifies what would be needed.
- **Does the conformal window exist for d >= 2?** The mass scale $m$ relative to $1/a$ determines whether the CHM formula is approximately valid.
- **Nonconformal extension:** Jacobson's Section IV conjecture that the result extends beyond CFT is physically motivated but unproven.

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
|---|---|---|---|---|---|
| Newton's constant | $G$ | $1/(4\eta)$ | exact (definition) | Jacobson 2012 | $\eta > 0$ |
| Entropy density | $\eta$ | $\eta_{\text{lattice}}/a^{d-1}$ | exact (mapping) | Part B | $a > 0$ |
| Channel capacity bound on $G$ | -- | $a^{d-1}/(4\log n)$ | exact (lower bound) | Phase 9 + Part B | $n \geq 2$ |
| Lattice spacing vs Planck length | $a$ | $\sim \ell_P \sqrt{\log n}$ | order of magnitude | Part B | $n \geq 2$ |

## Approximations Used

| Approximation | Valid When | Error Estimate | Breaks Down At |
|---|---|---|---|
| Continuum limit (Wilsonian) | $L \gg a$ (many lattice sites) | Non-universal lattice corrections $O(a/L)$ | $L \sim a$ (probing UV lattice structure) |
| CHM formula for non-CFT | $a \ll R \ll 1/m$ | $O((mR)^{2\Delta})$ (Speranza 2016) | $R \sim 1/m$ or no mass gap |
| First-order perturbation of vacuum | $\delta g_{ab}, \delta\phi$ small | $O(\delta^2)$ | Curvature $\sim$ Planck scale |

## Self-Check: PASSED

- [x] derivations/10-jacobson-inputs.md exists
- [x] Checkpoint 56eea50 exists in git log
- [x] Checkpoint 0533005 exists in git log
- [x] Convention consistency: all files use natural units, metric (-,+,+,+), K = -ln(rho), H = sum h_xy, G_ab = R_ab - (1/2)Rg_ab
- [x] Contract: all 3 claim IDs passed, deliv-jacobson-inputs produced, all 5 acceptance tests passed, all 3 references surfaced, all 3 forbidden proxies rejected
- [x] Dimensional analysis: [G*eta] = 1/4, [G] = [length^{d-1}], [eta] = [1/length^{d-1}], [K] = dimensionless
- [x] MVEH NOT claimed as proven (language check: "Assumption A5", "not a proof")
- [x] Assumption register A1-A5 complete with all 6 columns
- [x] Jacobson input table (J1)-(J3) with correct statuses
- [x] No forbidden proxies: no lattice Raychaudhuri, no MVEH proven, no Jacobson cited without self-modeling connection
- [x] Gap statement present (Part E.5): what self-modeling property would establish A5?
- [x] Conformal restriction stated honestly (Part D)
- [x] Phase 9 equations cited with numbers (09-03.3, 09-03.6)

---

_Phase: 10-jacobson-application, Plan 01_
_Completed: 2026-03-22_
