---
phase: 22-measurement-maps-four-routes-to-complexification
plan: 03
depth: full
one-liner: "Route 3 (GNS) obstruction: h_3(O) exceptional status + rank-1 Peirce bottleneck block canonical complexification of V_{1/2} via GNS construction"
subsystem: [formalism, derivation]
tags: [GNS, Jordan-algebra, exceptional, Peirce, complexification, JB-algebra, JC-algebra]

requires:
  - phase: 18
    provides: "Peirce decomposition h_3(O) = V_1(1) + V_{1/2}(16) + V_0(10); V_{1/2} = S_9; C*-observer complexification"
provides:
  - "Route 3 obstruction theorem: GNS cannot canonically induce V_{1/2} tensor_R C"
  - "Three independent obstructions identified: exceptional, parity, bottleneck"
  - "Precise characterization of what additional input would fix Route 3"
affects: [22-04, paper7]

methods:
  added: [JB-algebra GNS construction, Alfsen-Shultz classification, Peirce module analysis]
  patterns: [exceptional obstruction analysis, bottleneck characterization via Peirce rank]

key-files:
  created: [derivations/14-route3-gns-construction.md]

key-decisions:
  - "Route 3 definitively fails: GNS does not provide canonical complexification"
  - "Three independent obstructions identified (exceptional, parity, bottleneck)"
  - "Route 2 (C*-observer extension of scalars) confirmed as the working complexification mechanism"

patterns-established:
  - "Exceptional JB-algebra GNS produces real Hilbert space, not complex"
  - "Rank-1 Peirce bottleneck: V_1 = R transmits only scalar information to V_{1/2}"

conventions:
  - "Jordan product: a * b = (1/2)(ab + ba)"
  - "Peirce decomposition: under E_11"
  - "State normalization: Tr(rho) = 1"

plan_contract_ref: ".gpd/phases/22-measurement-maps-four-routes-to-complexification/22-03-PLAN.md#/contract"
contract_results:
  claims:
    claim-route3-complexification:
      status: passed
      summary: "Established precise obstruction: GNS construction does NOT canonically induce V_{1/2} tensor_R C. Three independent obstructions proven (exceptional, parity, bottleneck). This is the 'counterexample/obstruction' branch of the disjunction."
      linked_ids: [deliv-route3-proof, test-route3-peirce, test-route3-gns-valid, test-route3-decisive]
      evidence:
        - verifier: gpd-executor
          method: analytical derivation
          confidence: high
          claim_id: claim-route3-complexification
          deliverable_id: deliv-route3-proof
          acceptance_test_id: test-route3-decisive
          evidence_path: "derivations/14-route3-gns-construction.md"
  deliverables:
    deliv-route3-proof:
      status: passed
      path: "derivations/14-route3-gns-construction.md"
      summary: "Route 3 obstruction theorem with complete proof: three sub-routes analyzed, three independent obstructions identified, what-would-fix-it analysis included"
      linked_ids: [claim-route3-complexification, test-route3-peirce, test-route3-gns-valid, test-route3-decisive]
  acceptance_tests:
    test-route3-peirce:
      status: passed
      summary: "Peirce spaces with correct dimensions verified: V_1(1) + V_{1/2}(16) + V_0(10) = 27. Used throughout derivation."
      linked_ids: [claim-route3-complexification, deliv-route3-proof]
    test-route3-gns-valid:
      status: passed
      summary: "GNS construction for JB-algebras correctly described per Alfsen-Shultz. Exceptional obstruction explicitly identified: h_3(O) is not a JC-algebra, so GNS produces R^{27} not C^k. Jordan multiplication operators shown to be self-adjoint (eigenvalues real, hence L_a^2 >= 0, cannot give J^2 = -Id)."
      linked_ids: [claim-route3-complexification, deliv-route3-proof]
    test-route3-decisive:
      status: passed
      summary: "Decisive outcome achieved: precise obstruction statement with three independent failure modes (exceptional, parity, bottleneck). Not a theorem but the contractual disjunct 'counterexample/obstruction' established."
      linked_ids: [claim-route3-complexification, deliv-route3-proof]
  references:
    ref-upmeier1987:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Upmeier's JB-algebra representation theory cited for GNS construction context and universal representation"
    ref-alfsen-shultz2001:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Alfsen-Shultz classification theorem (A = A_JC + A_exc) cited as foundation for exceptional obstruction; GNS for JB-algebras (Ch. 11) used throughout"
    ref-baez2002:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Baez 2002 cited for h_3(O) exceptional status and F_4 automorphism group; key 'cannot be represented as operators on Hilbert space' result"
  forbidden_proxies:
    fp-wrong-algebra:
      status: rejected
      notes: "Worked exclusively with h_3(O). The exceptional status of h_3(O) is central to the obstruction argument."
    fp-no-canonical:
      status: rejected
      notes: "The obstruction is precisely about canonicity: GNS fails to provide a state-independent, structure-only complexification. This is what was analyzed."
    fp-assume-spin10:
      status: rejected
      notes: "Did not assume Spin(10). Showed GNS route cannot derive Spin(10) because it cannot produce a complex Hilbert space for V_{1/2}."
  uncertainty_markers:
    weakest_anchors:
      - "The 'bottleneck' argument (V_1 = R, scalar action) is elementary but model-dependent: it relies on using a rank-1 idempotent. A rank-2 idempotent would give a larger V_1."
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations: []

duration: 15min
completed: 2026-03-24
---

# Phase 22, Plan 03: Route 3 GNS Construction Summary

**Route 3 (GNS) obstruction: h_3(O) exceptional status + rank-1 Peirce bottleneck block canonical complexification of V_{1/2} via GNS construction**

## Performance

- **Duration:** 15 min
- **Started:** 2026-03-24T17:26:24Z
- **Completed:** 2026-03-24T17:41:00Z
- **Tasks:** 2
- **Files modified:** 1

## Key Results

- **Route 3 fails:** The GNS construction does NOT canonically induce $V_{1/2} \otimes_\mathbb{R} \mathbb{C}$
- **Three independent obstructions identified:**
  1. Exceptional: $h_3(\mathbb{O})$ is not a JC-algebra; GNS produces $\mathbb{R}^{27}$, not $\mathbb{C}^k$
  2. Parity: $\dim_\mathbb{R}(h_3(\mathbb{O})) = 27$ is odd; $\mathbb{R}^{27}$ admits no complex structure
  3. Bottleneck: $V_1 = \mathbb{R}$ acts on $V_{1/2}$ by scalar multiplication only; observer's complex structure cannot be transmitted through rank-1 Peirce interface
- **Route 2 (C*-observer extension of scalars) confirmed** as the working complexification mechanism

## Task Commits

1. **Task 1: GNS-type representation and V_{1/2} image analysis** - `e63729d` (derive)
2. **Task 2: Determine canonical complexification from GNS** - `817b9a1` (derive)

## Files Created/Modified

- `derivations/14-route3-gns-construction.md` - Route 3 obstruction theorem with complete proof

## Next Phase Readiness

- Route 3 decisively resolved (obstruction). Ready for Route 4 (Cl(6)/complex structure from $u \in S^6$) in Plan 04.
- Strengthens Phase 18 conclusion: complexification comes from C*-nature (Route 2), not representation theory of $h_3(\mathbb{O})$ (Route 3).

## Contract Coverage

- Claim IDs advanced: claim-route3-complexification -> passed (obstruction branch of disjunction)
- Deliverable IDs produced: deliv-route3-proof -> derivations/14-route3-gns-construction.md (passed)
- Acceptance test IDs run: test-route3-peirce (passed), test-route3-gns-valid (passed), test-route3-decisive (passed)
- Reference IDs surfaced: ref-upmeier1987 (read, cite), ref-alfsen-shultz2001 (read, cite), ref-baez2002 (cite)
- Forbidden proxies rejected: fp-wrong-algebra, fp-no-canonical, fp-assume-spin10 (all rejected)

## Equations Derived

**Eq. (22-03.1): Peirce action of V_1 on V_{1/2} (bottleneck)**

$$(\alpha E_{11}) \circ v = \frac{\alpha}{2} v \quad \forall\, \alpha \in \mathbb{R},\, v \in V_{1/2}$$

**Eq. (22-03.2): GNS inner product space for h_3(O)**

$$H_\omega = (h_3(\mathbb{O}),\, \langle a, b \rangle_\omega = \omega(a \circ b)) \cong \mathbb{R}^{27}$$

**Eq. (22-03.3): Self-adjointness obstruction for Jordan multiplication**

$$L_a \text{ self-adjoint} \implies \mathrm{spec}(L_a) \subset \mathbb{R} \implies L_a^2 \geq 0 \implies L_a^2 \neq -\mathrm{Id}$$

## Validations Completed

- Peirce decomposition dimensions: $1 + 16 + 10 = 27$ (consistent with prior Phase 18)
- $\mathbb{R}^{27}$ admits no complex structure (27 is odd; verified via $\det(J)^2 = (-1)^{27} = -1 < 0$)
- Self-adjoint operators have real eigenvalues, hence $L_a^2 \geq 0$ (precludes $J^2 = -\mathrm{Id}$)
- $V_1 = \mathbb{R} \cdot E_{11}$ acts by scalar multiplication $\alpha/2$ on $V_{1/2}$ (direct matrix computation)
- Forbidden proxy checks: all three proxies explicitly rejected with justification
- Cross-check: Route 3 failure consistent with Route 2 success established in Phase 18

## Decisions Made

- Decisive outcome selected: obstruction (not theorem). The three independent failure modes make this unambiguous.
- No approximations used (purely algebraic derivation).

## Deviations from Plan

None - plan executed exactly as written.

## Open Questions

- Could a rank-2 idempotent (e.g., $f = E_{11} + E_{22}$) avoid the bottleneck? This would give $V_1(f) = h_2(\mathbb{O})$ (10-dimensional), a much larger port. But this changes the physical setup (the observer occupies a different Peirce slot).
- Is there a "non-standard" GNS construction for exceptional Jordan algebras that produces a complex Hilbert space? The Alfsen-Shultz classification suggests not, but alternative constructions (e.g., Tits construction, Freudenthal magic square) might relate.

---

_Phase: 22-measurement-maps-four-routes-to-complexification_
_Completed: 2026-03-24_
