---
phase: 37-gap-dependency-theorem
plan: 01
depth: full
one-liner: "Gap C tensoriality and Gap D MVEH both DERIVED as theorems from BW + established results, with every assumption enumerated"
subsystem: derivation
tags: [bisognano-wichmann, lovelock, tomita-takesaki, gibbs-variational, entanglement-equilibrium, gap-analysis]

requires:
  - phase: 35-bw-equilibrium
    provides: [K_A = 2pi K_boost (Eq. 35.0a), KMS at beta=2pi (Eq. 35.8), theta=sigma=0 (Eqs. 35.19/35.21), T_U = a/2pi (Eq. 35.3)]
  - phase: 36-assembly-and-gap-scoring
    provides: [Gap scorecards (A NARROWED / B CLOSED-OPEN / C CONDITIONAL / D CONDITIONAL), derivation chain links (a)-(f)]
provides:
  - Gap C closure chain (5 steps, tensoriality DERIVED from BW + Raychaudhuri + Lovelock)
  - Gap D closure chain (5 steps, MVEH mathematical content DERIVED from BW + TT + Gibbs)
  - Complete assumption lists for both chains
  - Sorce two-tier caveat analysis for Gap D
affects: [37-02 dependency theorem assembly, paper7 gap discussion]

methods:
  added: [logical chain construction with hypothesis verification, assumption enumeration with completeness checking]
  patterns: [5-step closure chain with DAG verification, two-tier Sorce analysis]

key-files:
  created:
    - derivations/37-gap-c-closure-chain.md
    - derivations/37-gap-d-closure-chain.md

key-decisions:
  - "Present both Gibbs variational principle (Route A) and relative entropy (Route B) for Gap D Step 4"
  - "Two-tier Sorce assessment rather than dismissing or overclaiming"

patterns-established:
  - "Closure chain format: each step cites theorem, lists ALL hypotheses, verifies coverage by numbered assumptions"
  - "Gap cross-dependency tracking: Gap C requires Gap A (UC9 smooth manifold)"

conventions:
  - "hbar = 1, k_B = 1, a = 1"
  - "metric = (-,+,+,+)"
  - "K_A = -ln(rho_A), positive operator"
  - "beta_mod = 1, beta_phys = 2pi/a"
  - "J > 0 antiferromagnetic"

plan_contract_ref: ".gpd/phases/37-gap-dependency-theorem/37-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-gap-c-chain:
      status: passed
      summary: "Gap C closure chain proved: BW -> K_B local -> entanglement first law -> Raychaudhuri area deficit -> Lovelock uniqueness -> Einstein in d+1=4. Tensoriality DERIVED from BW locality + Raychaudhuri + Lovelock, not assumed. Assumptions: UC5, UC6, UC8, UC9, UC10 + Gap A cross-dependency."
      linked_ids: [deliv-gap-c, test-gap-c-chain-complete, test-gap-c-assumptions, test-gap-c-no-hidden, ref-phase35-bw, ref-jacobson2016, ref-lovelock]
    claim-gap-d-chain:
      status: passed
      summary: "Gap D closure chain proved: BW -> TT KMS -> Gibbs/relative-entropy -> entanglement equilibrium -> MVEH (theorem). Mathematical content of MVEH derived, not postulated. Two-tier Sorce assessment: conformal (strong) vs non-conformal (algebraic). Assumptions: UC5, CS, TL."
      linked_ids: [deliv-gap-d, test-gap-d-chain-complete, test-gap-d-assumptions, test-gap-d-sorce, test-gap-d-no-hidden, ref-phase35-bw, ref-pusz-woronowicz, ref-sorce2024, ref-jacobson2016]
    claim-assumption-enumeration:
      status: passed
      summary: "Every assumption in both chains appears in the numbered assumption lists. Gap C: UC5, UC6, UC8, UC9, UC10. Gap D: UC5, CS, TL. Cross-dependencies stated (UC9 requires Gap A; TL is Gap A territory). No hidden assumptions found."
      linked_ids: [deliv-gap-c, deliv-gap-d, test-gap-c-no-hidden, test-gap-d-no-hidden]
  deliverables:
    deliv-gap-c:
      status: passed
      path: "derivations/37-gap-c-closure-chain.md"
      summary: "Complete Gap C closure chain with 5 steps, theorem citations, hypothesis tables, and assumption list (UC5, UC6, UC8, UC9, UC10)"
      linked_ids: [claim-gap-c-chain, test-gap-c-chain-complete]
    deliv-gap-d:
      status: passed
      path: "derivations/37-gap-d-closure-chain.md"
      summary: "Complete Gap D closure chain with 5 steps, both Gibbs and relative entropy routes, Sorce two-tier analysis, and assumption list (UC5, CS, TL)"
      linked_ids: [claim-gap-d-chain, test-gap-d-chain-complete]
  acceptance_tests:
    test-gap-c-chain-complete:
      status: passed
      summary: "All 5 steps verified present with theorem citations (BW, CHM, BCHM, Jacobson, Lovelock). Chain produces G_ab + Lambda g_ab = 8pi G_N T_ab in d+1=4."
      linked_ids: [claim-gap-c-chain, deliv-gap-c, ref-jacobson2016, ref-lovelock]
    test-gap-c-assumptions:
      status: passed
      summary: "Every step's theorem hypotheses traced to assumption list. Step 1: UC5. Step 2: UC5, UC9. Step 3: none new. Step 4: UC8, UC9, UC10. Step 5: UC6."
      linked_ids: [claim-gap-c-chain, deliv-gap-c]
    test-gap-c-no-hidden:
      status: passed
      summary: "Smoothness for Raychaudhuri traced to UC9 + Gap A dependency. d+1=4 for Lovelock traced to UC6. Area-entropy traced to UC8. Local equilibrium (theta=sigma=0) traced to Killing equation (derived, not assumed). No hidden premises."
      linked_ids: [claim-assumption-enumeration, deliv-gap-c, ref-lovelock, ref-jacobson2016]
    test-gap-d-chain-complete:
      status: passed
      summary: "All 5 steps verified present: BW (Step 1), TT KMS (Step 2), BW+TT combined (Step 3), Gibbs/relative entropy (Step 4, two routes), MVEH identified (Step 5). Both routes produce delta S = 0 at first order."
      linked_ids: [claim-gap-d-chain, deliv-gap-d, ref-pusz-woronowicz, ref-jacobson2016]
    test-gap-d-assumptions:
      status: passed
      summary: "UC5 covers Steps 1-2. CS (cyclic-separating) covers Step 2. TL (type III / thermodynamic limit) covers Step 4. Sorce caveat produces two-tier: conformal (strong) vs algebraic (non-conformal). Type I vs III stated."
      linked_ids: [claim-gap-d-chain, deliv-gap-d, ref-sorce2024]
    test-gap-d-sorce:
      status: passed
      summary: "Sorce caveat addressed: (1) d=1 conformal -- full geometric content, chain fully rigorous; (2) d>=2 non-conformal -- algebraic KMS exact, geometric interpretation approximate (SRF=0.9993); (3) lattice BW SRF provides numerical support; (4) algebraic vs geometric distinction clearly stated."
      linked_ids: [claim-gap-d-chain, deliv-gap-d, ref-sorce2024, ref-phase35-bw]
    test-gap-d-no-hidden:
      status: passed
      summary: "Cyclic-separating vacuum stated as CS assumption. Type III vs I distinction stated with TL assumption. Thermodynamic limit stated. Conformal vs non-conformal stated in Sorce analysis. No prose-only assumptions."
      linked_ids: [claim-assumption-enumeration, deliv-gap-d]
  references:
    ref-phase35-bw:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Phase 35 BW/KMS results cited in both chains: K_A=2pi K_boost (Eq. 35.0a), KMS (Eq. 35.8), theta=sigma=0 (Eqs. 35.19/35.21), T_U (Eq. 35.3), SRF=0.9993"
    ref-jacobson2016:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Jacobson 2016 cited for area deficit formula Eq.(5) in Gap C Step 4, and entanglement equilibrium definition in Gap D Step 5"
    ref-lovelock:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Lovelock 1971/1972 cited in Gap C Step 5 -- uniqueness theorem for d+1=4"
    ref-pusz-woronowicz:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Pusz-Woronowicz 1978 cited in Gap D Step 4 Route A -- KMS <=> passivity <=> Gibbs"
    ref-sorce2024:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Sorce 2024 cited in Gap D Sorce caveat analysis -- geometric modular flow requires conformal symmetry"
    ref-phase36-scorecards:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Phase 36 scorecards read for baseline gap scores. Gap C: CONDITIONAL -> DERIVED. Gap D: CONDITIONAL -> DERIVED (mathematical content)."
  forbidden_proxies:
    fp-mechanism-works:
      status: rejected
      notes: "Every step in Gap C chain cites a specific theorem with verified hypotheses. No vague 'mechanism works' claims."
    fp-hidden-assumptions:
      status: rejected
      notes: "All assumptions enumerated in numbered lists. Gap C: UC5, UC6, UC8, UC9, UC10. Gap D: UC5, CS, TL. Cross-dependencies explicit."
    fp-kms-is-mveh:
      status: rejected
      notes: "Step 4 (Gibbs variational principle / relative entropy) is the explicit bridge between KMS (Step 3) and MVEH (Step 5). No conflation."
    fp-global-maximum:
      status: rejected
      notes: "Document uses 'first-order stationarity at fixed <K_A>' throughout. Forbidden proxy compliance section addresses this explicitly."
  uncertainty_markers:
    weakest_anchors:
      - "Sorce 2024: for non-conformal theories (d>=2), geometric interpretation of modular flow is approximate (SRF=0.9993, not a theorem)"
      - "Type I -> type III transition: Gibbs variational principle is rigorous for type III (continuum) but only formal for type I (finite lattice)"
      - "Gap C depends on Gap A: Raychaudhuri requires smooth manifold (UC9), which is Gap A territory"
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations:
      - "If a chain step required an assumption not statable as a UC property or standard QFT axiom, the closure would be incomplete"

duration: 5min
completed: 2026-03-30
---

# Phase 37 Plan 01: Gap C/D Closure Chains Summary

**Gap C tensoriality and Gap D MVEH both DERIVED as theorems from BW + established results, with every assumption enumerated**

## Performance

- **Duration:** 5 min
- **Started:** 2026-03-30T20:51:59Z
- **Completed:** 2026-03-30T20:57:14Z
- **Tasks:** 2
- **Files modified:** 2

## Key Results

- Gap C (tensoriality): DERIVED from BW locality + Raychaudhuri + Lovelock in 5 steps. Tensoriality is NOT an independent postulate -- the second-derivative restriction comes from Raychaudhuri, the symmetric 2-tensor structure from the entanglement first law at all causal diamonds, and the divergence-free condition from contracted Bianchi. [CONFIDENCE: HIGH]
- Gap D (MVEH): mathematical content DERIVED from BW + Tomita-Takesaki + Gibbs variational principle in 5 steps. MVEH ($\delta S = 0$ at first order at fixed $\langle K_A \rangle$) is a theorem, not a postulate. Physical interpretation remains a structural identification. [CONFIDENCE: HIGH]
- Sorce caveat: two-tier assessment -- conformal ($d = 1$) strong form; non-conformal ($d \geq 2$) algebraic form with SRF = 0.9993 numerical support. [CONFIDENCE: HIGH]
- Assumption lists complete: Gap C uses UC5, UC6, UC8, UC9, UC10 + Gap A cross-dependency. Gap D uses UC5, CS (cyclic-separating), TL (type III / thermodynamic limit). No hidden assumptions. [CONFIDENCE: HIGH]

## Task Commits

1. **Task 1: Gap C closure chain** - `c8426ca` (derive)
2. **Task 2: Gap D closure chain** - `2ec7d68` (derive)

## Files Created/Modified

- `derivations/37-gap-c-closure-chain.md` -- 5-step closure chain BW -> K_B local -> first law -> Raychaudhuri -> Lovelock -> Einstein
- `derivations/37-gap-d-closure-chain.md` -- 5-step closure chain BW -> TT KMS -> Gibbs/relative entropy -> entanglement equilibrium -> MVEH

## Next Phase Readiness

- Gap C and Gap D closure chains ready for Plan 02 (formal dependency theorem assembly)
- Assumption lists (UC5, UC6, UC8, UC9, UC10 for Gap C; UC5, CS, TL for Gap D) ready for the dependency matrix
- Sorce two-tier analysis provides dimension-dependent assessment for theorem statement
- Gap A cross-dependency documented -- Plan 02 must incorporate this into the theorem structure

## Contract Coverage

- Claim IDs advanced: claim-gap-c-chain -> passed, claim-gap-d-chain -> passed, claim-assumption-enumeration -> passed
- Deliverable IDs produced: deliv-gap-c -> derivations/37-gap-c-closure-chain.md, deliv-gap-d -> derivations/37-gap-d-closure-chain.md
- Acceptance test IDs run: test-gap-c-chain-complete -> passed, test-gap-c-assumptions -> passed, test-gap-c-no-hidden -> passed, test-gap-d-chain-complete -> passed, test-gap-d-assumptions -> passed, test-gap-d-sorce -> passed, test-gap-d-no-hidden -> passed
- Reference IDs surfaced: ref-phase35-bw (read, cite), ref-jacobson2016 (read, cite), ref-lovelock (cite), ref-pusz-woronowicz (cite), ref-sorce2024 (cite), ref-phase36-scorecards (read, cite)
- Forbidden proxies rejected: fp-mechanism-works, fp-hidden-assumptions, fp-kms-is-mveh, fp-global-maximum -- all rejected (compliance verified)

## Equations Derived

**Eq. (37.1):** Entanglement first law (cited, exact identity)
$$\delta S_A = \delta \langle K_A \rangle$$

**Eq. (37.4):** Area deficit in Riemann normal coordinates (cited from Jacobson 2016)
$$\delta A = -\frac{\Omega_{d-2} \ell^d}{2(d^2-1)} R_{ik}{}^{ik}$$

**Eq. (37.6):** Einstein equation from Lovelock uniqueness (Gap C conclusion)
$$G_{ab} + \Lambda g_{ab} = 8\pi G_N T_{ab}$$

**Eq. (37.12):** Entanglement equilibrium = MVEH (Gap D conclusion)
$$\delta S = 0 \quad \text{at first order, at fixed } \langle K_A \rangle$$

## Validations Completed

- DAG verification: both chains confirmed acyclic (each step uses only prior outputs)
- Assumption completeness: every theorem hypothesis traced to numbered assumption list
- Convention consistency: metric (-,+,+,+), K_A = -ln(rho_A) positive, beta=2pi, verified throughout
- No circular dependencies between Gap C and Gap D chains
- Forbidden proxy compliance verified for all 4 proxies
- Cross-dependency Gap A <-> Gap C explicitly stated via UC9

## Decisions & Deviations

None -- plan executed as specified.

## Open Questions

- Can the Gauss-Bonnet coefficient be shown to vanish for the SWAP lattice in d+1 > 4, or is UC6 (d+1=4) an irreducible assumption?
- Can the Sorce caveat be weakened by showing approximate geometric modular flow suffices for the Jacobson argument?
- Is the type I -> type III transition (Gap A territory) essential for Gap D, or does the finite-lattice (type I) Gibbs argument suffice?

## Self-Check: PASSED

- [x] derivations/37-gap-c-closure-chain.md exists
- [x] derivations/37-gap-d-closure-chain.md exists
- [x] Commit c8426ca found in git log
- [x] Commit 2ec7d68 found in git log
- [x] Convention consistency: single metric convention (-,+,+,+) throughout both files
- [x] All contract claim IDs have entries
- [x] All deliverable IDs have entries
- [x] All acceptance test IDs have entries
- [x] All reference IDs have entries
- [x] All forbidden proxy IDs have entries

---

_Phase: 37-gap-dependency-theorem, Plan 01_
_Completed: 2026-03-30_
