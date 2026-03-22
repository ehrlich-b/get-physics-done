---
phase: 09-area-law-derivation
plan: 03
depth: full
one-liner: "Synthesized WVCH and channel capacity routes into three-perspective area-law argument resolving 'which state?'; Jacobson bridge established via entanglement first law delta S = delta <K> with MVEH identified as Phase 10 gap"
subsystem: derivation
tags: [area-law, entanglement, synthesis, jacobson, modular-hamiltonian, entanglement-first-law, MVEH, robustness]

requires:
  - phase: 09-area-law-derivation
    plan: 01
    provides: "WVCH thermal MI area law I(A:B) <= 2*beta*|boundary|*|J| (Eq. 09.3), Heisenberg entanglement characterization"
  - phase: 09-area-law-derivation
    plan: 02
    provides: "Channel capacity area law S(A) <= log(n)*|boundary| (Eq. 09-02.1), pure state identity I = 2S"
  - phase: 08-locality-formalization
    provides: "h_xy = JF (SWAP interaction), lattice definition, v_LR = 8eJ/(e-1)"
provides:
  - "Three-perspective 'which state?' resolution: thermal MI (A1), pure S (A2), delta S for any state (A3)"
  - "Entanglement first law: delta S = delta <K_A> (exact identity, Eq. 09-03.3)"
  - "delta S ~ |boundary| for local perturbations (Eq. 09-03.6, physical argument under A3)"
  - "Synthesis Theorem parts (a)-(c): Eqs. 09-03.7a, 09-03.7b, 09-03.7c"
  - "Jacobson bridge: (J1) established, (J2) exact, (J3) MVEH open gap"
  - "Complete assumption register A1-A4 with gap statement"
  - "Dimensionality breakdown: all d, thermal/pure/ground"
  - "Robustness under J, sign, interaction, topology, dimension perturbations"
affects: [10-jacobson, paper-6]

methods:
  added: [entanglement first law, modular Hamiltonian locality argument, Jacobson bridge analysis]
  patterns: [three-perspective redundancy for state-independence, assumption register for gap tracking]

key-files:
  created:
    - derivations/09-area-law-synthesis.md

key-decisions:
  - "Identified delta S (not S itself) as the quantity Jacobson actually needs -- this resolves the MI-vs-S tension between WVCH and channel capacity routes"
  - "Modular Hamiltonian locality (A3) is physically motivated but NOT proven for the self-modeling lattice; flagged as weakest anchor"
  - "MVEH identified as the main Phase 10 gap, distinct from the area-law question"
  - "Sign of J is a physical selection criterion for gravity, not an additional assumption"

patterns-established:
  - "Three-perspective redundancy: A1 fails -> use A2 or A3; A2 fails -> use A1 or A3; A3 fails -> use A1 or A2. Only exotic states break all three."
  - "Jacobson needs delta S, not S -- this is a key insight that decouples the area-law question from the state-selection question"

conventions:
  - "natural units (hbar = c = k_B = 1)"
  - "metric (-,+,+,+)"
  - "entropy: von Neumann S = -Tr(rho ln rho), nats"
  - "I(A:B) = S(A) + S(B) - S(AB)"
  - "H = sum h_xy (no 1/2)"
  - "K_A = -ln(rho_A) (modular Hamiltonian)"
  - "Tr(rho) = 1"

plan_contract_ref: ".gpd/phases/09-area-law-derivation/09-03-PLAN.md#/contract"
contract_results:
  claims:
    claim-area-law-synthesis:
      status: passed
      summary: "Three-part synthesis theorem established: (a) thermal MI area law from WVCH, (b) pure-state S area law from channel capacity, (c) delta S ~ |boundary| from entanglement first law + modular Hamiltonian locality. Jacobson bridge built via delta S route with MVEH identified as Phase 10 gap."
      linked_ids: [deliv-synthesis, test-which-state, test-jacobson-bridge, test-gap-statement, test-robustness, ref-wvch2008-synth, ref-hastings2007-synth, ref-jacobson2016-bridge]
    claim-which-state-resolved:
      status: passed
      summary: "Three complementary perspectives on 'which state?': (a) thermal state at any T>0 for MI area law (A1), (b) any pure state for S area law (A2), (c) entanglement first law delta S = delta <K> for delta S ~ |boundary| scaling (A3). Both signs of J addressed; FM ground state excluded from gravity application due to zero entanglement."
      linked_ids: [deliv-synthesis, test-which-state, test-jacobson-bridge, ref-jacobson2016-bridge]
  deliverables:
    deliv-synthesis:
      status: passed
      path: derivations/09-area-law-synthesis.md
      summary: "Complete synthesis: Parts A-D (which state?, Jacobson bridge, ground-state insufficiency, sign ambiguity) + Parts E-J (assumption register, gap statement, dimensionality, robustness, synthesis theorem, Phase 10 interface). Contains all must_contain items."
      linked_ids: [claim-area-law-synthesis, claim-which-state-resolved]
  acceptance_tests:
    test-which-state:
      status: passed
      summary: "All three perspectives present (Parts A.2-A.3): thermal (Perspective 1, A1), pure (Perspective 2, A2), delta S (Perspective 3, A3). Both signs of J addressed (Part D). FM ground state acknowledged as trivially area-law but useless for gravity. AFM log correction in 1D acknowledged."
      linked_ids: [claim-which-state-resolved, deliv-synthesis]
    test-jacobson-bridge:
      status: passed
      summary: "Part B: (J1) area law delivered via Perspective 3 delta S ~ |boundary| under A3; (J2) entanglement first law stated as exact identity (Eq. 09-03.3) with derivation; (J3) MVEH identified as open gap. Bridge from MI/S area laws to delta S ~ |boundary| is logically complete via entanglement first law."
      linked_ids: [claim-area-law-synthesis, deliv-synthesis, ref-jacobson2016-bridge]
    test-gap-statement:
      status: passed
      summary: "Part F: assumptions A1-A4 listed with status (Physical/Derived/Motivated). Proven vs conditional vs physical vs open classification. Table (F.5) distinguishes rigorous, conditional, physical argument, and open gap. Each assumption has 'what it buys' and 'what fails without it' (Part E). Dimensionality: Part G covers d=1 (rigorous for thermal/pure, log-corrected for AFM ground), d>=2 (rigorous for thermal/pure, conjectured for ground state). Precise enough for referee evaluation."
      linked_ids: [claim-area-law-synthesis, deliv-synthesis, ref-hastings2007-synth]
    test-robustness:
      status: passed
      summary: "Part H: five robustness checks. (1) J perturbations: WVCH linear in |J|, channel capacity J-free. (2) Sign change: |J| dependence. (3) Interaction perturbations: h_xy = JF is unique within self-modeling, but WVCH/channel capacity apply even outside. (4) Topology: bounded-degree graphs OK. (5) Local dimension: channel capacity scales as log(n), WVCH is n-independent. All ROBUST."
      linked_ids: [claim-area-law-synthesis, deliv-synthesis]
  references:
    ref-wvch2008-synth:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "WVCH 2008 PRL 100, 070502 cited as source of part (a) of synthesis theorem. Primary area-law method."
    ref-hastings2007-synth:
      status: completed
      completed_actions: [compare]
      missing_actions: []
      summary: "Hastings 2007 JSTAT P08024 cited as foil -- inapplicable due to gaplessness. Theorem structure used as template for gap statement (proven/conditional/open classification)."
    ref-jacobson2016-bridge:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Jacobson 2016 PRL 116, 201101 cited as target for Phase 10. Three inputs (J1)-(J3) identified; Phase 9 delivers (J1) and (J2), identifies (J3) MVEH as gap."
  forbidden_proxies:
    fp-which-state-unresolved:
      status: rejected
      notes: "Three perspectives on 'which state?' provided (Parts A.2-A.3). No unqualified 'the self-modeling lattice has area-law entanglement' without specifying state and assumption."
    fp-hand-wave-jacobson:
      status: rejected
      notes: "Jacobson bridge goes through entanglement first law delta S = delta <K> (Eq. 09-03.3, derived) + modular Hamiltonian locality (A3, physically motivated with Bisognano-Wichmann evidence). No 'area law implies Jacobson' shortcut."
    fp-overclaim-rigor-higher-d:
      status: rejected
      notes: "Part G dimensionality table explicitly marks d>=2 ground-state results as 'Open conjecture / Not rigorous'. WVCH and channel capacity bounds stated as 'Rigorous given A1/A2' in all d."
  uncertainty_markers:
    weakest_anchors:
      - "A3 (modular Hamiltonian locality): physically motivated by Bisognano-Wichmann (exact for half-space in CFT) and Peschel (free fermions), but NOT proven for the interacting self-modeling lattice with h_xy = JF"
      - "Robustness under interaction perturbations is trivially satisfied because h_xy = JF is the UNIQUE self-modeling interaction -- there is nothing to perturb within the self-modeling family"
    unvalidated_assumptions:
      - "A1 (thermal state): not derived from self-modeling axioms"
      - "A2 (pure global state): not derived from self-modeling axioms"
      - "A3 (modular Hamiltonian locality): not proven for self-modeling lattice"
    competing_explanations: []
    disconfirming_observations:
      - "If the modular Hamiltonian K_A for the self-modeling state is non-local (significant support in the bulk), then delta S does not scale with boundary and the Jacobson bridge (Perspective 3) fails"
      - "If Phase 11 numerics show volume-law scaling for S(A), the channel capacity bound (which is an upper bound) would still hold, but it would indicate the bound is very loose and the physical entanglement structure is not area-law"

comparison_verdicts:
  - subject_id: test-jacobson-bridge
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-jacobson2016-bridge
    comparison_kind: benchmark
    metric: logical_completeness
    threshold: "all three Jacobson inputs (J1)-(J3) addressed"
    verdict: pass
    recommended_action: "Proceed to Phase 10 with MVEH as the primary open question"
    notes: "(J1) established via Perspective 3 under A3. (J2) exact identity. (J3) identified as open gap."
  - subject_id: test-gap-statement
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-hastings2007-synth
    comparison_kind: benchmark
    metric: gap_precision
    threshold: "each assumption independently evaluable by referee"
    verdict: pass
    recommended_action: "None -- gap statement meets precision requirement"
    notes: "Assumption register A1-A4 with explicit status, utility, and failure mode for each"
  - subject_id: test-robustness
    subject_kind: acceptance_test
    subject_role: supporting
    reference_id: ref-wvch2008-synth
    comparison_kind: cross_method
    metric: perturbation_stability
    threshold: "area law persists under all listed perturbation types"
    verdict: pass
    recommended_action: "None -- all 5 robustness checks pass"
    notes: "Uniqueness of h_xy = JF within self-modeling makes interaction robustness trivial"

duration: 8min
completed: 2026-03-22
---

# Plan 09-03: Area-Law Synthesis, Which-State Resolution, and Jacobson Bridge

**Synthesized WVCH and channel capacity routes into three-perspective area-law argument resolving 'which state?'; Jacobson bridge established via entanglement first law delta S = delta <K> with MVEH identified as Phase 10 gap**

## Performance

- **Duration:** ~8 min
- **Started:** 2026-03-22T10:35:59Z
- **Completed:** 2026-03-22T10:44:00Z
- **Tasks:** 2
- **Files modified:** 1

## Key Results

- **"Which state?" resolved via three perspectives:** (1) thermal MI area law under A1, (2) pure-state S area law under A2, (3) delta S ~ |boundary| for any state under A3 -- the three perspectives provide redundancy [CONFIDENCE: HIGH for the framework; MEDIUM for delta S scaling under A3 since modular Hamiltonian locality is not proven for the self-modeling lattice]
- **Entanglement first law:** $\delta S = \delta\langle K_A \rangle$ derived as exact QI identity (Eq. 09-03.3) [CONFIDENCE: HIGH]
- **Jacobson bridge:** (J1) area law delivered, (J2) exact identity, (J3) MVEH identified as main Phase 10 gap [CONFIDENCE: HIGH for the interface specification]
- **Synthesis Theorem:** Parts (a) thermal MI, (b) pure-state S, (c) delta S scaling -- complete area-law characterization from self-modeling locality [CONFIDENCE: HIGH for (a) and (b); MEDIUM for (c)]
- **Gap statement:** Assumption register A1-A4 with proven/conditional/physical/open classification [CONFIDENCE: HIGH]
- **Robustness:** All five perturbation types pass (J, sign, interaction, topology, dimension) [CONFIDENCE: HIGH]

## Task Commits

1. **Task 1: Which-state resolution and Jacobson bridge** - `af6cd56` (derive)
2. **Task 2: Gap statement, robustness, and synthesis theorem** - `52e7faa` (derive)

## Files Created/Modified

- `derivations/09-area-law-synthesis.md` -- Complete synthesis: Parts A-J covering which-state resolution (3 perspectives), Jacobson bridge ((J1)-(J3)), ground-state insufficiency, sign ambiguity, assumption register (A1-A4), gap statement (proven/conditional/physical/open), dimensionality breakdown (all d), robustness (5 checks), synthesis theorem (a)-(c), Phase 10 interface

## Next Phase Readiness

- **Phase 10 (Jacobson):** Receives area-law structure (Synthesis Theorem (a)-(c)), entanglement first law (Eq. 09-03.3), and v_LR from Phase 8. MVEH is the main open question.
- **Phase 11 (Numerics):** Can verify channel capacity bound tightness numerically; can test modular Hamiltonian locality (A3) via entanglement Hamiltonian computation for small systems.
- **Paper 6:** The synthesis theorem provides the main result; the gap statement provides the honest assessment for the paper's limitations section.

## Contract Coverage

- Claim IDs advanced: claim-area-law-synthesis -> passed, claim-which-state-resolved -> passed
- Deliverable IDs produced: deliv-synthesis -> passed (derivations/09-area-law-synthesis.md)
- Acceptance test IDs run: test-which-state -> passed, test-jacobson-bridge -> passed, test-gap-statement -> passed, test-robustness -> passed
- Reference IDs surfaced: ref-wvch2008-synth -> completed (cite), ref-hastings2007-synth -> completed (compare), ref-jacobson2016-bridge -> completed (read, cite)
- Forbidden proxies rejected: fp-which-state-unresolved -> rejected, fp-hand-wave-jacobson -> rejected, fp-overclaim-rigor-higher-d -> rejected
- Decisive comparison verdicts: test-jacobson-bridge -> pass, test-gap-statement -> pass, test-robustness -> pass

## Equations Derived

**Eq. (09-03.1): Thermal MI area law (inherited from Plan 01)**

$$I(A:B) \leq 2\beta \, |\partial(A)| \, |J|$$

**Eq. (09-03.2): Pure-state S area law (inherited from Plan 02)**

$$S(A) \leq \log(n) \cdot |\partial(A)|$$

**Eq. (09-03.3): Entanglement first law (exact identity)**

$$\delta S(A) = \delta\langle K_A \rangle, \quad K_A = -\ln \rho_A$$

**Eq. (09-03.4): Modular Hamiltonian locality (A3)**

$$K_A \approx \sum_{x \in \partial(A)} k_x + \text{exponentially decaying corrections}$$

**Eq. (09-03.6): delta S boundary scaling (physical argument)**

$$\delta S(A) = \delta\langle K_A \rangle \sim O(|\partial(A)|) \quad \text{for local perturbations}$$

**Eqs. (09-03.7a)-(09-03.7c): Synthesis Theorem**

$$(a)\; I(A:B) \leq 2\beta|\partial||J|, \quad (b)\; S(A) \leq \log(n)|\partial|, \quad (c)\; \delta S \sim O(|\partial|)$$

## Validations Completed

- **Entanglement first law derivation:** Full derivation from $S = -\mathrm{Tr}(\rho\ln\rho)$ expansion. Verified at 3 test points: thermal state recovers $\delta S = \beta\delta\langle H\rangle$, product state gives $\delta S = 0$, maximally mixed gives $\delta S = 0$.
- **Sign independence:** All three perspectives depend on $|J|$ or are $J$-free. Verified.
- **Dimensional analysis:** $[\delta S] = [\delta\langle K\rangle] = [\text{dimensionless}]$. All consistent.
- **Forbidden proxy check:** No "locality implies area law" hand-waving (specific theorems cited), no "area law implies Jacobson" shortcut (delta S bridge constructed), no overclaiming rigor in $d \geq 2$ (explicitly marked as "not rigorous" for ground states).
- **Assumption register completeness:** A1-A4 all have status, utility, and failure mode.
- **Robustness:** 5/5 perturbation types pass.
- **Phase 9 success criteria:** 5/5 ROADMAP criteria addressed (Part J.3).

## Decisions Made

- **delta S as the key insight:** Identified that Jacobson needs delta S (change in entropy), not S itself. This resolves the tension between WVCH (which bounds MI, not S) and channel capacity (which bounds S for pure states). The delta S route works for any state.
- **A3 flagged as weakest anchor:** The modular Hamiltonian locality assumption is the least well-supported of A1-A4. It is physically motivated but has no proof for the self-modeling lattice specifically. Honestly flagged.
- **MVEH as Phase 10 gap:** Clearly separated the area-law question (Phase 9, resolved) from the MVEH question (Phase 10, open).

## Deviations from Plan

None -- plan executed exactly as written.

## Issues Encountered

None.

## Open Questions

- **A3 verification:** Can the modular Hamiltonian locality for the self-modeling lattice be verified numerically? For small systems, one could compute $K_A = -\ln\rho_A$ and check whether its matrix elements decay with distance from the boundary.
- **MVEH derivation:** Can MVEH be derived from the self-modeling structure? This is the central question for Phase 10.
- **Continuum limit:** How does the discrete lattice area law $S \leq \log(n)|\partial|$ translate to the continuum $S \propto \mathcal{A}/\ell_P^2$?
- **Tightness of channel capacity bound:** For typical states of the self-modeling Hamiltonian, how close is $S(A)$ to the upper bound $\log(n)|\partial|$?

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
|---|---|---|---|---|---|
| Thermal MI bound per bond | $2\beta|J|$ | $2\beta|J|$ | exact (upper bound) | WVCH 2008 | $\beta > 0$ |
| Pure-state S bound per bond | $\log(n)$ | $\log(n)$ nats | exact (upper bound) | Channel capacity | Pure states |
| LR velocity (1D) | $v_{LR}$ | $12.66J$ | exact (upper bound) | Phase 8 | $J > 0$ |

## Self-Check: PASSED

- [x] derivations/09-area-law-synthesis.md exists
- [x] Checkpoint af6cd56 exists in git log
- [x] Checkpoint 52e7faa exists in git log
- [x] Convention consistency: all files use natural units, entropy in nats, H = sum h_xy, K = -ln(rho)
- [x] Contract: all 2 claim IDs passed, deliv-synthesis produced, all 4 acceptance tests passed, all 3 references surfaced, all 3 forbidden proxies rejected
- [x] Dimensional analysis passes throughout
- [x] All 5 Phase 9 ROADMAP success criteria addressed
- [x] Entanglement first law verified at 3 test points

---

_Phase: 09-area-law-derivation, Plan 03_
_Completed: 2026-03-22_
