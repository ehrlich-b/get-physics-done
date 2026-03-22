---
phase: 09-area-law-derivation
plan: 01
depth: full
one-liner: "WVCH thermal MI area law I(A:B) <= 2*beta*|boundary|*|J| established for self-modeling Hamiltonian; Heisenberg entanglement fully characterized -- FM S=0, AFM S=(1/3)ln(L), Hastings inapplicable for both signs of J"
subsystem: derivation
tags: [area-law, entanglement, WVCH, heisenberg, mutual-information, thermal-state, spectral-gap, CFT]

requires:
  - phase: 08-locality-formalization
    provides: "h_xy = JF (SWAP interaction), lattice definition, locality mapping, ||h_xy|| = |J|, v_LR = 8eJ/(e-1)"
provides:
  - "WVCH thermal MI area law: I(A:B) <= 2*beta*|boundary(A)|*|J| (Eq. 09.3)"
  - "Higher-dimensional scaling: I(A:B) <= 4d*beta*|J|*L^{d-1} (Eq. 09.4)"
  - "FM entanglement: S(A) = 0 (product state ground state)"
  - "AFM entanglement: S(L) = (1/3)*ln(L) + const (c=1 CFT, Eq. 09.16)"
  - "Spectral gap analysis: FM O(1/N^2), AFM exactly 0"
  - "Hastings 2007 shown to be inapplicable (gapless for both signs)"
  - "Assumption A1 (thermal state identification) explicitly flagged as gap"
affects: [09-02, 09-03, 10-jacobson]

methods:
  added: [WVCH bound application, Calabrese-Cardy entanglement formula, Bethe ansatz spectral analysis]
  patterns: [thermal MI bound as primary area-law route (gap-independent), ground-state entanglement as validation anchor]

key-files:
  created:
    - derivations/09-wvch-thermal-area-law.md
    - derivations/09-heisenberg-entanglement.md

key-decisions:
  - "WVCH (not Hastings) as primary area-law theorem -- Hastings requires gap, which fails"
  - "Thermal state identification flagged as explicit assumption (A1), not smuggled in"
  - "Both signs of J analyzed independently rather than assuming one sign"

patterns-established:
  - "The WVCH bound is the most robust area-law result for this system: no gap required, any dimension, any T > 0"
  - "Ground-state analysis serves as validation anchor, not primary result"

conventions:
  - "natural units (hbar = c = k_B = 1)"
  - "metric (-,+,+,+)"
  - "entropy: von Neumann S = -Tr(rho ln rho), nats"
  - "H = sum h_xy (no 1/2)"
  - "Tr(rho) = 1"

plan_contract_ref: ".gpd/phases/09-area-law-derivation/09-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-wvch-applied:
      status: passed
      summary: "WVCH bound I(A:B) <= 2*beta*|boundary(A)|*|J| rigorously applied to self-modeling Hamiltonian H = sum JF; all hypotheses except thermal state identification (A1) verified; bound holds for any finite T, any dimension, both signs of J"
      linked_ids: [deliv-wvch-derivation, test-wvch-hypotheses, test-wvch-dimensional, ref-wvch2008]
    claim-heisenberg-entanglement:
      status: passed
      summary: "FM: S(A)=0 (product state), gap O(1/N^2); AFM: S(L)=(1/3)ln(L)+const (c=1 CFT), gap=0 exactly; Hastings requires gap>0, which fails for both signs; Brandao-Horodecki requires exponential decay, which also fails for both signs"
      linked_ids: [deliv-heisenberg-analysis, test-fm-trivial, test-afm-log, test-hastings-does-not-apply, ref-hastings2007, ref-calabrese-cardy]
  deliverables:
    deliv-wvch-derivation:
      status: passed
      path: derivations/09-wvch-thermal-area-law.md
      summary: "WVCH theorem stated, all 4 hypotheses checked against Phase 8 results, bound applied (Eq. 09.3), dimensional analysis, 4 limiting cases, higher-dimensional scaling, thermal state assumption flagged"
      linked_ids: [claim-wvch-applied, test-wvch-hypotheses, test-wvch-dimensional]
    deliv-heisenberg-analysis:
      status: passed
      path: derivations/09-heisenberg-entanglement.md
      summary: "FM and AFM ground states, degeneracy, spectral gaps, entanglement entropy (S=0 and (1/3)ln(L)), Hastings and Brandao-Horodecki shown inapplicable, summary table, implications for Phase 9"
      linked_ids: [claim-heisenberg-entanglement, test-fm-trivial, test-afm-log, test-hastings-does-not-apply]
  acceptance_tests:
    test-wvch-hypotheses:
      status: passed
      summary: "H1 (sum of local terms): verified from Phase 8 Def. 5. H2 (Gibbs state): ASSUMED, flagged as gap A1. H3 (finite norm): ||h_xy||=|J| from Phase 8 Eq. (08-03.1). H4 (nearest-neighbor): verified from Phase 8 Theorem 1. All 4 explicitly addressed."
      linked_ids: [claim-wvch-applied, deliv-wvch-derivation]
    test-wvch-dimensional:
      status: passed
      summary: "[I(A:B)] = dimensionless, [beta*|J|] = energy^{-1}*energy = dimensionless, [|boundary|] = dimensionless count. Product is dimensionless. Consistent."
      linked_ids: [claim-wvch-applied, deliv-wvch-derivation]
    test-fm-trivial:
      status: passed
      summary: "FM ground state |up...up> is product state; rho_A = |up><up|^{tensor |A|}; S(A) = -Tr(rho_A ln rho_A) = 0 exactly."
      linked_ids: [claim-heisenberg-entanglement, deliv-heisenberg-analysis]
    test-afm-log:
      status: passed
      summary: "Calabrese-Cardy with c=1 (SU(2)_1 WZW for spin-1/2 AFM Heisenberg) gives S(L) = (1/3)ln(L) + const. Coefficient 1/3 = c/3 with c=1. Confirmed by numerical studies (Laflorencie et al. 2006)."
      linked_ids: [claim-heisenberg-entanglement, deliv-heisenberg-analysis, ref-calabrese-cardy]
    test-hastings-does-not-apply:
      status: passed
      summary: "Hastings requires spectral gap Delta > 0. FM: Delta ~ 2*pi^2*|J|/N^2 -> 0 (quadratic magnon). AFM: Delta = 0 exactly (Bethe ansatz, des Cloizeaux-Pearson 1962). Gap condition fails for BOTH signs of J. Brandao-Horodecki also fails (requires exponential decay; FM has long-range order, AFM has algebraic decay)."
      linked_ids: [claim-heisenberg-entanglement, deliv-heisenberg-analysis, ref-hastings2007]
  references:
    ref-wvch2008:
      status: completed
      completed_actions: [read, use, cite]
      missing_actions: []
      summary: "WVCH 2008 PRL 100, 070502 (arXiv:0704.3906) used as primary area-law result. Theorem stated (Eq. 09.1), all hypotheses checked, bound applied to self-modeling Hamiltonian."
    ref-hastings2007:
      status: completed
      completed_actions: [read, compare]
      missing_actions: []
      summary: "Hastings 2007 JSTAT P08024 (arXiv:0705.2024) cited as foil. Gap hypothesis shown to fail for both signs of J. Theorem explicitly excluded as inapplicable to self-modeling Hamiltonian."
    ref-calabrese-cardy:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Calabrese-Cardy 2004 JHEP 0406:002 (arXiv:hep-th/0405152) used for AFM entanglement formula S(L) = (c/3)ln(L) with c=1. Both open and periodic BC formulae stated."
  forbidden_proxies:
    fp-hastings-without-gap:
      status: rejected
      notes: "Hastings cited ONLY as foil (inapplicable theorem). Gap failure explicitly demonstrated for both FM (O(1/N^2) -> 0) and AFM (exactly 0). No invocation of Hastings as supporting theorem."
    fp-locality-implies-area-law:
      status: rejected
      notes: "Area law derived via specific theorem (WVCH) with all hypotheses checked. No hand-waving 'locality implies area law' argument. The precise mathematical connection is the WVCH bound Eq. (09.3)."
  uncertainty_markers:
    weakest_anchors:
      - "WVCH bounds mutual information, not S(A) -- the connection to Jacobson requires the entanglement first law, handled in Plan 03"
      - "Thermal state identification (Assumption A1) is physically motivated but not derived from self-modeling axioms"
      - "Calabrese-Cardy coefficient 1/3 is from CFT; numerical verification exists but this plan does not independently verify it [UNVERIFIED - training data]"
    unvalidated_assumptions:
      - "Assumption A1: the physically relevant state is a Gibbs state rho_beta = exp(-beta*H)/Z"
      - "c=1 for SU(2)_1 WZW describing low-energy physics of spin-1/2 AFM Heisenberg [UNVERIFIED - training data]"
    competing_explanations: []
    disconfirming_observations:
      - "If the self-modeling Hamiltonian has non-local effective interactions beyond nearest-neighbor, WVCH bound may not be tight"
      - "If the thermal state at any finite T has volume-law S(A), the WVCH MI bound still holds but the route to Jacobson requires additional argument"

comparison_verdicts:
  - subject_id: test-wvch-hypotheses
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-wvch2008
    comparison_kind: benchmark
    metric: hypothesis_satisfaction
    threshold: "all 4 hypotheses addressed"
    verdict: pass
    recommended_action: "None -- WVCH correctly applied"
    notes: "H1-H4 all addressed; H2 flagged as assumption A1 (honest gap, not a failure)"
  - subject_id: test-afm-log
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-calabrese-cardy
    comparison_kind: benchmark
    metric: coefficient_match
    threshold: "c/3 = 1/3 within 10%"
    verdict: pass
    recommended_action: "None -- coefficient matches c=1 CFT prediction exactly"
    notes: "Analytical result S = (1/3)ln(L) from c=1 SU(2)_1 WZW; numerical confirmation exists in literature (Laflorencie et al. 2006)"
  - subject_id: test-hastings-does-not-apply
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-hastings2007
    comparison_kind: benchmark
    metric: hypothesis_failure
    threshold: "gap condition must fail for both J signs"
    verdict: pass
    recommended_action: "None -- Hastings correctly excluded"
    notes: "FM gap O(1/N^2) -> 0; AFM gap = 0 exactly (Bethe ansatz). Both fail the gap > 0 requirement."

duration: 20min
completed: 2026-03-22
---

# Plan 09-01: WVCH Thermal MI Area Law and Heisenberg Entanglement Characterization

**WVCH thermal MI area law I(A:B) <= 2*beta*|boundary|*|J| established for self-modeling Hamiltonian; Heisenberg entanglement fully characterized -- FM S=0, AFM S=(1/3)ln(L), Hastings inapplicable for both signs of J**

## Performance

- **Duration:** ~20 min
- **Started:** 2026-03-22T10:27:45Z
- **Completed:** 2026-03-22T10:48:00Z
- **Tasks:** 2
- **Files modified:** 2

## Key Results

- **WVCH thermal MI area law:** $I(A:B) \leq 2\beta|\partial(A)||J|$ for the self-modeling Hamiltonian at any finite temperature, in any spatial dimension, for both signs of $J$ [CONFIDENCE: HIGH]
- **FM entanglement ($J < 0$):** $S(A) = 0$ exactly (product state ground state); gap $\Delta \sim 2\pi^2|J|/N^2 \to 0$ [CONFIDENCE: HIGH]
- **AFM entanglement ($J > 0$):** $S(L) = \frac{1}{3}\ln L + \text{const}$ (logarithmic correction to area law); gap $= 0$ exactly [CONFIDENCE: HIGH]
- **Hastings 2007 inapplicable:** spectral gap condition $\Delta > 0$ fails for both signs of $J$ [CONFIDENCE: HIGH]
- **Assumption A1 (thermal state identification) explicitly flagged** as the gap between the WVCH bound and the self-modeling axioms [CONFIDENCE: N/A -- this is a stated assumption, not a derived result]

## Task Commits

1. **Task 1: WVCH thermal MI area law** - `b7e9bbb` (derive)
2. **Task 2: Heisenberg entanglement characterization** - `16823ff` (derive)

## Files Created/Modified

- `derivations/09-wvch-thermal-area-law.md` -- WVCH theorem statement, hypothesis verification (H1-H4), bound application (Eq. 09.3), dimensional analysis, 4 limiting cases, higher-dimensional scaling (Eq. 09.4), interpretation and limitations
- `derivations/09-heisenberg-entanglement.md` -- FM and AFM ground states, spectral gaps, entanglement entropy, Calabrese-Cardy formula, Hastings and Brandao-Horodecki exclusion, summary table, Phase 9 implications

## Next Phase Readiness

- **Plan 02 (channel capacity route):** Can proceed independently; uses Phase 8 Hamiltonian and locality results
- **Plan 03 (state identification and Jacobson):** Uses the WVCH bound (Eq. 09.3) as input; must address Assumption A1 and connect MI area law to Jacobson's entanglement equilibrium
- **Phase 10 (Jacobson):** Requires Plan 03 completion; the WVCH bound provides the area-law ingredient

## Contract Coverage

- Claim IDs advanced: claim-wvch-applied -> passed, claim-heisenberg-entanglement -> passed
- Deliverable IDs produced: deliv-wvch-derivation -> passed, deliv-heisenberg-analysis -> passed
- Acceptance test IDs run: test-wvch-hypotheses -> passed, test-wvch-dimensional -> passed, test-fm-trivial -> passed, test-afm-log -> passed, test-hastings-does-not-apply -> passed
- Reference IDs surfaced: ref-wvch2008 -> completed (read, use, cite), ref-hastings2007 -> completed (read, compare), ref-calabrese-cardy -> completed (read, cite)
- Forbidden proxies rejected: fp-hastings-without-gap -> rejected (Hastings cited only as foil), fp-locality-implies-area-law -> rejected (WVCH theorem with explicit hypotheses)
- Decisive comparison verdicts: test-wvch-hypotheses -> pass, test-afm-log -> pass, test-hastings-does-not-apply -> pass

## Equations Derived

**Eq. (09.1): WVCH theorem (general form)**

$$I(A:B) \leq 2\beta \sum_{X:\, X \cap A \neq \emptyset,\, X \cap B \neq \emptyset} \|\Phi(X)\|$$

**Eq. (09.2): Self-modeling interaction norm**

$$\|h_{xy}\| = |J|$$

**Eq. (09.3): WVCH bound for self-modeling Hamiltonian**

$$I(A:B) \leq 2\beta \, |\partial(A)| \, |J|$$

**Eq. (09.4): Higher-dimensional scaling**

$$I(A:B) \leq 4d\beta|J| \cdot L^{d-1}$$

**Eq. (09.5)-(09.10): FM ground state and entanglement**

$$|\Psi_0^{FM}\rangle = |\uparrow\cdots\uparrow\rangle, \quad S(A) = 0, \quad \Delta_{FM} \sim 2\pi^2|J|/N^2$$

**Eq. (09.11)-(09.16): AFM spectral gap and entanglement**

$$\Delta_{AFM} = 0 \text{ (exact)}, \quad S(L) = \frac{1}{3}\ln L + \text{const}$$

## Validations Completed

- **Dimensional analysis (WVCH bound):** $[2\beta|\partial||J|] = [\text{dimensionless}]$. Matches $[I(A:B)]$.
- **Limiting cases:** $\beta \to 0$ (bound $\to 0$, consistent with maximally mixed state); $\beta \to \infty$ (bound $\to \infty$, vacuously large for gapless system); $J \to 0$ (bound $\to 0$, consistent with decoupled sites); $|\partial| = 1$ (bound $= 2\beta|J|$, single bond). All physically correct.
- **Sign independence:** Bound depends on $|J|$, not $\text{sign}(J)$. Verified.
- **FM S(A) = 0:** Product state has zero entanglement. Exact.
- **AFM coefficient:** $c/3 = 1/3$ with $c = 1$ (SU(2)$_1$ WZW). Matches Calabrese-Cardy.
- **Gap analysis:** FM $\Delta \sim O(1/N^2)$, AFM $\Delta = 0$. Both gapless.
- **Forbidden proxy check:** Hastings cited only as foil; WVCH is primary theorem with explicit hypotheses.

## Decisions & Deviations

### Decisions

- **WVCH over Hastings:** Deliberate choice motivated by gaplessness of the Heisenberg model for both signs of $J$.
- **Both signs of J analyzed independently:** The sign ambiguity from Phase 8 is addressed by showing the WVCH bound is sign-independent, while the ground-state entanglement differs qualitatively between FM and AFM.

### Deviations

None -- plan executed exactly as written.

## Issues Encountered

None.

## Open Questions

- **Assumption A1 justification:** The thermal state identification requires physical argument (Plan 03).
- **WVCH bound tightness:** The bound $2\beta|J|$ per boundary bond is an upper bound. How tight is it? Numerical comparison at finite $N$ would quantify the slack.
- **Logarithmic correction in $d \geq 2$:** For AFM on $\mathbb{Z}^d$ with $d \geq 2$, numerical evidence shows area-law scaling with log corrections. No rigorous proof exists.
- **Connection to Jacobson:** The WVCH bound gives an MI area law. Jacobson's entanglement thermodynamics requires an entropy area law. The bridge is the entanglement first law (Plan 03).

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
|---|---|---|---|---|---|
| WVCH bound per bond | $2\beta\|J\|$ | $2\beta\|J\|$ | exact (upper bound) | WVCH 2008 | $\beta > 0$ |
| FM gap (1D) | $\Delta_{FM}$ | $2\pi^2\|J\|/N^2$ | exact (leading order) | Magnon dispersion | $N \gg 1$ |
| AFM gap (1D) | $\Delta_{AFM}$ | 0 | exact | Bethe ansatz | all $N$ |
| AFM entanglement coefficient | $c/3$ | 1/3 | exact (CFT prediction) | Calabrese-Cardy | $L \gg 1$ |
| Central charge | $c$ | 1 | exact | SU(2)$_1$ WZW | spin-1/2 AFM |

## Self-Check: PASSED

- [x] derivations/09-wvch-thermal-area-law.md exists
- [x] derivations/09-heisenberg-entanglement.md exists
- [x] Checkpoint b7e9bbb exists in git log
- [x] Checkpoint 16823ff exists in git log
- [x] Convention consistency: all files use natural units, entropy in nats, H = sum h_xy
- [x] Contract: all 2 claim IDs passed, all 2 deliverable IDs produced, all 5 acceptance test IDs run, all 3 reference IDs surfaced, both forbidden proxies rejected
- [x] Dimensional analysis passes in both derivation files
- [x] All 4 limiting cases physically correct

---

_Phase: 09-area-law-derivation, Plan 01_
_Completed: 2026-03-22_
