---
phase: 12-paper-assembly
plan: 02
depth: full
one-liner: "Wrote Sections II-V: self-modeling lattice (H = sum JF forced by Schur-Weyl), unified area-law entanglement (WVCH + channel capacity + first law), MVEH dissolution via Connes-Rovelli thermal time, and Jacobson-derived Einstein equations with G = 1/(4 eta)"
subsystem: paper-writing
tags: [emergent-gravity, entanglement-equilibrium, einstein-equations, self-modeling, area-law, MVEH, thermal-time]

requires:
  - phase: 08-locality-formalization
    provides: Lattice definition, H = sum JF forced by diagonal U(n), LR velocity v_LR = 8eJ/(e-1)
  - phase: 09-area-law-derivation
    provides: WVCH bound, channel capacity bound, entanglement first law, delta S ~ |boundary|
  - phase: 10-jacobson-application
    provides: Wilsonian continuum limit, Jacobson derivation, G = 1/(4 eta), sign chain, gap statement
  - phase: 12-paper-assembly
    plan: 01
    provides: Paper 6 infrastructure, introduction, discussion, bibliography

provides:
  - Section II (lattice.tex): complete self-modeling lattice definition with forced SWAP Hamiltonian and LR bounds
  - Section III (arealaw.tex): unified area-law presentation with three perspectives and entanglement first law
  - Section IV (equilibrium.tex): MVEH dissolution via thermal time hypothesis, Sorce caveat resolution, Wilsonian continuum limit
  - Section V (einstein.tex): Jacobson derivation applied, Einstein equations derived with G = 1/(4 eta), sign chain verified
  - 8 new bibliography entries for references cited in Sections II-V

affects: [12-03]

methods:
  added: [Schur-Weyl duality argument, WVCH thermal MI bound, channel capacity + DPI, Raychaudhuri-based area variation, CHM modular Hamiltonian]
  patterns: [unified area-law presentation (three perspectives), MVEH as definitional rather than assumed, sign chain as explicit verification]

key-files:
  modified:
    - paper6/sections/lattice.tex
    - paper6/sections/arealaw.tex
    - paper6/sections/equilibrium.tex
    - paper6/sections/einstein.tex
    - paper6/refs.bib

key-decisions:
  - "Each area-law bound labeled with its specific assumption (thermal state, pure state, K locality) per plan requirement"
  - "MVEH dissolution uses exact phrasing from phase-12-prompt.md"
  - "Jacobson 2016 G = 1/(4 eta) adopted directly for d=3 rather than re-deriving dimension-dependent coefficient"
  - "Conformal approximation stated as honest caveat with Speranza 2016 reference and Jacobson conjecture noted"

patterns-established:
  - "Three-perspective area-law structure: thermal MI, pure S, perturbative delta S"
  - "Sign chain as numbered verification list in derivation sections"

conventions:
  - "natural units (hbar=c=k_B=1)"
  - "metric = (-,+,+,+)"
  - "entropy = von Neumann, nats: S = -Tr(rho ln rho)"
  - "modular Hamiltonian: K = -ln(rho_A)"
  - "Einstein tensor: G_ab = R_ab - (1/2)Rg_ab"
  - "lattice Hamiltonian: H = sum J F_xy (SWAP)"

plan_contract_ref: ".gpd/phases/12-paper-assembly/12-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-lattice-presentation:
      status: passed
      summary: "Section II presents self-modeling lattice with Paper 5 summary, lattice definition (graph topology as input), H = sum J F_xy forced by diagonal U(n) covariance + Schur-Weyl duality, LR velocity formula v_LR = 8eJ/(e-1), and n-independence."
      linked_ids: [deliv-lattice, test-lattice-completeness, test-hamiltonian-forced, ref-paper5]
    claim-arealaw-presentation:
      status: passed
      summary: "Section III presents three area-law perspectives (WVCH thermal MI, channel capacity pure-state S, perturbative delta S via K locality) with entanglement first law as exact identity and explicit assumption labeling."
      linked_ids: [deliv-arealaw, test-arealaw-unified, test-assumptions-explicit, ref-hastings2007]
    claim-equilibrium-presentation:
      status: passed
      summary: "Section IV presents MVEH as definitional via Connes-Rovelli thermal time hypothesis, addresses Sorce 2024 caveat with SU(n) -> WZW CFT resolution, frames Wilsonian continuum limit with self-modeler perspective."
      linked_ids: [deliv-equilibrium, test-mveh-definitional, test-sorce-addressed, test-continuum-framed, ref-jacobson2016, ref-connesrovelli1994, ref-sorce2024]
    claim-einstein-derivation:
      status: passed
      summary: "Section V derives G_ab + Lambda g_ab = 8 pi G T_ab via Jacobson 2016 applied to self-modeling lattice, with correct attribution, all 5 steps (setup, Raychaudhuri, CHM, equilibrium, extraction), G = 1/(4 eta), and 6-step sign chain."
      linked_ids: [deliv-einstein, test-einstein-derived, test-attribution-correct, test-parameters-identified, ref-jacobson2016, ref-jacobson1995]
  deliverables:
    deliv-lattice:
      status: passed
      path: "paper6/sections/lattice.tex"
      summary: "Section II with Paper 5 summary, lattice definition, SWAP Hamiltonian, Schur-Weyl derivation, LR bounds"
      linked_ids: [claim-lattice-presentation, test-lattice-completeness, test-hamiltonian-forced]
    deliv-arealaw:
      status: passed
      path: "paper6/sections/arealaw.tex"
      summary: "Section III with entanglement first law, WVCH bound, channel capacity bound, perturbative delta S, summary of what is established"
      linked_ids: [claim-arealaw-presentation, test-arealaw-unified, test-assumptions-explicit]
    deliv-equilibrium:
      status: passed
      path: "paper6/sections/equilibrium.tex"
      summary: "Section IV with thermal time hypothesis, MVEH dissolution, Sorce caveat, Wilsonian continuum limit, parameter identifications"
      linked_ids: [claim-equilibrium-presentation, test-mveh-definitional, test-sorce-addressed, test-continuum-framed]
    deliv-einstein:
      status: passed
      path: "paper6/sections/einstein.tex"
      summary: "Section V with entropy decomposition, Raychaudhuri area variation, CHM matter variation, Einstein equation extraction, sign chain, parameter identification"
      linked_ids: [claim-einstein-derivation, test-einstein-derived, test-attribution-correct, test-parameters-identified]
  acceptance_tests:
    test-lattice-completeness:
      status: passed
      summary: "Section II contains all 5 elements: Paper 5 summary (Sec 2.1), lattice definition (Sec 2.2), Hamiltonian forced by U(n) + Schur-Weyl (Sec 2.3), v_LR formula (Sec 2.4), topology-as-input note (Sec 2.2)."
      linked_ids: [claim-lattice-presentation, deliv-lattice]
    test-hamiltonian-forced:
      status: passed
      summary: "Text states h_xy = J F_xy is 'forced' and 'unique diagonal-U(n)-invariant coupling' via Schur-Weyl duality for S_2."
      linked_ids: [claim-lattice-presentation, deliv-lattice]
    test-arealaw-unified:
      status: passed
      summary: "Section III presents all three area-law perspectives (WVCH Sec 3.2.1, channel capacity Sec 3.2.2, perturbative delta S Sec 3.2.3) in a single section with entanglement first law (Sec 3.1)."
      linked_ids: [claim-arealaw-presentation, deliv-arealaw]
    test-assumptions-explicit:
      status: passed
      summary: "Each bound states its assumption inline: 'The state is a Gibbs state' (WVCH), 'The global state is a pure state' (channel capacity), 'modular Hamiltonian locality' (perturbative delta S)."
      linked_ids: [claim-arealaw-presentation, deliv-arealaw]
    test-mveh-definitional:
      status: passed
      summary: "MVEH presented as definitional via Connes-Rovelli in Sec 4.2. Text explicitly states 'MVEH does not appear as a numbered assumption in this paper.' No A5 label anywhere."
      linked_ids: [claim-equilibrium-presentation, deliv-equilibrium]
    test-sorce-addressed:
      status: passed
      summary: "Sorce 2024 caveat addressed in Sec 4.3 with three elements: result stated (geometric modular flow requires conformal symmetry), SU(n) resolution (AFM -> SU(n)_1 WZW CFT), remaining gap noted (sufficient conditions open)."
      linked_ids: [claim-equilibrium-presentation, deliv-equilibrium]
    test-continuum-framed:
      status: passed
      summary: "Continuum limit framed as Wilsonian in Sec 4.4 with self-modeler perspective ('the compressed model M is finite-dimensional; smoothness is... the observer's coarse-grained description') and parameter identifications."
      linked_ids: [claim-equilibrium-presentation, deliv-equilibrium]
    test-einstein-derived:
      status: passed
      summary: "Section V derives G_ab + Lambda g_ab = 8 pi G T_ab through all 5 steps: setup (Sec 5.1), Raychaudhuri (Sec 5.2), CHM (Sec 5.3), equilibrium -> Einstein (Sec 5.4), parameters (Sec 5.5). Final equation is Eq. (18)."
      linked_ids: [claim-einstein-derivation, deliv-einstein]
    test-attribution-correct:
      status: passed
      summary: "Section V opens with 'We now apply the Jacobson (2016) entanglement equilibrium argument to the self-modeling lattice as UV completion' and distinguishes L1-L5 (this work) from L6-L8 (Jacobson applied)."
      linked_ids: [claim-einstein-derivation, deliv-einstein]
    test-parameters-identified:
      status: passed
      summary: "G = 1/(4 eta) stated as Eq. (19). Lambda undetermined (stated twice: Sec 5.4 and 5.5). Channel capacity bound G >= a^{d-1}/(4 log n) stated as Eq. (20)."
      linked_ids: [claim-einstein-derivation, deliv-einstein]
  references:
    ref-paper5:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited in Sec II (Paper 5 summary, locality mapping) and Sec IV (involution dissolution parallel)"
    ref-jacobson2016:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited throughout Secs III-V: Jacobson inputs, entropy decomposition, Raychaudhuri, conformal conjecture, Einstein equation, Lambda undetermined"
    ref-jacobson1995:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited via ref-jacobson2016 context; direct citation in introduction (Plan 01)"
    ref-connesrovelli1994:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited in Sec IV (thermal time hypothesis foundation, MVEH dissolution argument)"
    ref-sorce2024:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited in Sec IV (Sorce caveat on geometric modular flow, SU(n) resolution)"
    ref-hastings2007:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited at end of Sec III: explicitly noted as not directly applicable (system is gapless), cited for historical context"
  forbidden_proxies:
    fp-handwaving-arealaw:
      status: rejected
      notes: "Section III invokes specific theorems (WVCH, channel capacity + DPI, first law + K locality) for each area-law perspective. No hand-waving."
    fp-mveh-assumption:
      status: rejected
      notes: "MVEH does not appear in any numbered assumption list. Sec 4.2 explicitly states it is definitional."
    fp-jacobson-disconnected:
      status: rejected
      notes: "Sec V opens by connecting to the self-modeling lattice as UV completion. The chain L1-L5 (new) vs L6-L8 (Jacobson applied) is stated."
    fp-rigorous-continuum:
      status: rejected
      notes: "Sec 4.4 explicitly frames continuum limit as 'a physical argument, not a rigorous construction' and notes it is a shared open problem."
  uncertainty_markers:
    weakest_anchors:
      - "Sorce caveat: sufficient conditions for geometric modular flow remain open"
      - "Conformal approximation: CHM exact only for CFTs; non-conformal corrections suppressed but not computed"
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations:
      - "If SU(n) Heisenberg IR is not conformal for some n, the Sorce resolution fails"
      - "If non-conformal corrections produce f(R) gravity, the leading-order Einstein claim weakens"

duration: 6min
completed: 2026-03-22
---

# Phase 12, Plan 02: Technical Core Sections (II-V)

**Wrote the four technical core sections of Paper 6: self-modeling lattice (H = sum JF forced by Schur-Weyl), unified area-law entanglement (WVCH + channel capacity + first law), MVEH dissolution via Connes-Rovelli thermal time hypothesis, and Jacobson-derived Einstein equations with G = 1/(4 eta)**

## Performance

- **Duration:** 6 min
- **Started:** 2026-03-22T18:38:36Z
- **Completed:** 2026-03-22T18:44:27Z
- **Tasks:** 2
- **Files modified:** 5

## Key Results

- Section II presents the complete self-modeling lattice with Hamiltonian forced by diagonal U(n) covariance + Schur-Weyl duality: h_xy = J F_xy (SWAP), LR velocity v_LR = 8eJ/(e-1)
- Section III establishes area-law entanglement from three complementary perspectives: thermal MI (WVCH), pure-state S (channel capacity), perturbative delta S (K locality)
- Section IV dissolves MVEH into a definitional identification via the Connes-Rovelli thermal time hypothesis, addresses the Sorce 2024 caveat via SU(n) -> WZW CFT
- Section V derives G_ab + Lambda g_ab = 8 pi G T_ab with G = 1/(4 eta), Lambda undetermined, sign chain verified (6 steps, attractive gravity)

## Task Commits

1. **Task 1: Section II and Section III** - `c378739` (document)
2. **Task 2: Section IV and Section V** - `9f6f976` (document)

## Files Created/Modified

- `paper6/sections/lattice.tex` - Sec II: Paper 5 summary, lattice definition, forced SWAP Hamiltonian, LR bounds
- `paper6/sections/arealaw.tex` - Sec III: entanglement first law, WVCH, channel capacity, perturbative delta S, Jacobson inputs established
- `paper6/sections/equilibrium.tex` - Sec IV: Tomita-Takesaki + thermal time, MVEH dissolution, Sorce caveat, Wilsonian continuum limit
- `paper6/sections/einstein.tex` - Sec V: entropy decomposition, Raychaudhuri, CHM, equilibrium -> Einstein, sign chain, parameters
- `paper6/refs.bib` - 8 new entries: BCHM2013, Holevo1973, BennettWiesner1992, Peschel2003, BratteliRobinson1997, Affleck1986, AffleckHaldane1987, Affleck1988

## Next Phase Readiness

- All four technical core sections complete; Plan 03 can write Sec VI (numerical verification)
- All \ref{eq:*} labels defined: eq:einstein, eq:first-law, eq:hamiltonian, eq:channel-bound, eq:vlr, etc.
- The \ref{eq:einstein} in the discussion section now resolves
- Bibliography has 33 entries (25 original + 8 new)

## Equations Derived

**Eq. (12-02.1):** Forced Hamiltonian

$$H = \sum_{\langle x,y \rangle \in E} J\, F_{xy}$$

**Eq. (12-02.2):** WVCH thermal mutual information area law

$$I(A:B) \leq 2\beta\, |\partial A|\, |J|$$

**Eq. (12-02.3):** Channel capacity area law (pure states)

$$S(A) \leq \log(n) \cdot |\partial A|$$

**Eq. (12-02.4):** Entanglement first law (exact identity)

$$\delta S(A) = \delta\langle K_A \rangle$$

**Eq. (12-02.5):** Einstein field equations

$$G_{ab} + \Lambda\, g_{ab} = 8\pi G\, T_{ab}, \qquad G = 1/(4\eta)$$

## Validations Completed

- MVEH does not appear in any numbered assumption list (grep confirms)
- Each area-law bound explicitly states its assumption (thermal state, pure state, K locality)
- Sign chain verified: 6 steps from positive mass to attractive gravity
- Dimensional consistency: entropy variations dimensionless, area variations have correct length dimensions
- Convention consistency: (-,+,+,+) metric, K = -ln(rho_A), natural units throughout all 4 sections
- Hastings 2007 cited for context only, not as the main route (system is gapless)
- vandeWetering citation key corrected (2018 -> 2019 to match refs.bib)
- All 8 new bib entries have correct metadata

## Decisions Made

- Adopted Jacobson 2016 G = 1/(4 eta) directly for d=3, rather than re-deriving dimension-dependent angular integrals (the tensor structure, sign, and parametric dependence on eta are verified independently)
- Conformal approximation stated as caveat rather than suppressed: Speranza 2016 corrections noted, Jacobson conjecture cited
- Sorce caveat kept to one subsection (Sec 4.3) per plan guidance
- vandeWetering citation key corrected to match existing bib entry

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 4 - Missing Component] Missing bibliography entries**

- **Found during:** Task 2 verification
- **Issue:** 8 citation keys referenced in new sections did not exist in refs.bib
- **Fix:** Added BCHM2013, Holevo1973, BennettWiesner1992, Peschel2003, BratteliRobinson1997, Affleck1986, AffleckHaldane1987, Affleck1988
- **Files modified:** paper6/refs.bib
- **Verification:** All citation keys in Sections II-V have matching bib entries
- **Committed in:** 9f6f976

**2. [Rule 1 - Code Bug] vandeWetering citation key mismatch**

- **Found during:** Task 1 verification
- **Issue:** Cited as vandeWetering2018 but bib entry is vandeWetering2019
- **Fix:** Changed to vandeWetering2019 in lattice.tex
- **Committed in:** 9f6f976

---

**Total deviations:** 2 auto-fixed (1 missing component, 1 key mismatch)
**Impact on plan:** None. Both were corrections for consistency, not scope changes.

## Open Questions

- LaTeX compilation not verified (no pdflatex available on system) -- deferred to environment with compiler
- Equation numbering will be set by LaTeX at compile time; cross-references use \ref labels
- Sec VI (numerical verification) content deferred to Plan 03

## Self-Check: PASSED

- [x] All 5 modified files exist and contain expected content
- [x] Both commits (c378739, 9f6f976) exist in git log
- [x] Convention assertions (ASSERT_CONVENTION) present in all .tex file headers
- [x] Contract coverage complete: all 4 claim IDs, 4 deliverable IDs, 11 acceptance test IDs, 6 reference IDs, 4 forbidden proxy IDs addressed

---

_Phase: 12-paper-assembly, Plan 02_
_Completed: 2026-03-22_
