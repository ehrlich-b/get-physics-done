---
phase: 13-order-zero-representation-theory
plan: 01
depth: full
one-liner: "Derived pi_o(b) = diag(I tensor b^T, I tensor b^T) via J antilinearity and proved order zero condition [pi(a), pi_o(b)] = 0 for all a, b in M_n(C) at general n"
subsystem: derivation
tags: [spectral-triple, order-zero, opposite-algebra, noncommutative-geometry, representation-theory]

requires:
  - phase: "paper7-spectral-triple-prompt"
    provides: "J(psi,chi) = (P conj(chi), P conj(psi)), gamma, KO-dim 6 signs"
provides:
  - "pi_o(b) = diag(I_n tensor b^T, I_n tensor b^T) explicit formula at general n"
  - "Order zero condition [pi(a), pi_o(b)] = 0 proved for all a, b in M_n(C)"
  - "Both naive and contragredient actions satisfy order zero"
  - "pi_o is *-representation of A^{op} verified"
affects: [13-02, 13-03, 14-dirac-operator, 15-first-order-condition]

methods:
  added: [opposite-algebra-computation, antilinear-operator-decomposition, tensor-factor-commutativity]
  patterns: [J-antilinearity-tracking, component-by-component-verification]

key-files:
  created: [derivations/07-order-zero-condition.md]

key-decisions:
  - "Naive algebra action pi(a) = diag(a tensor I, a tensor I) used as primary; contragredient also satisfies order zero"
  - "Both actions work for order zero; distinction deferred to evenness condition in later phase"

patterns-established:
  - "J antilinearity chain: b^dagger entries b_{jk}* -> conj gives b_{jk} -> SWAP gives b^T on second factor"
  - "Block-diagonal structure handles sector-swap: commutator decomposes block-by-block"

conventions:
  - "J = antilinear, J(psi,chi) = (P conj(chi), P conj(psi))"
  - "P = SWAP, P(v tensor w) = w tensor v"
  - "pi_o(b) = J pi(b*) J^{-1} where b* = b^dagger"
  - "[A,B] = AB - BA"

plan_contract_ref: ".gpd/phases/13-order-zero-representation-theory/13-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-pi-o-explicit:
      status: passed
      summary: "pi_o(b) = diag(I_n tensor b^T, I_n tensor b^T) derived component-by-component at general n, showing J's antilinearity converts b^dagger on first factor to b^T on second factor via the chain conj(b_{jk}*) = b_{jk}"
      linked_ids: [deliv-order-zero-derivation, test-pi-o-form, test-pi-o-representation, ref-van-suijlekom2024, ref-paper6]
    claim-order-zero:
      status: passed
      summary: "[pi(a), pi_o(b)] = 0 proved for all a, b in M_n(C) at general n by tensor factor commutativity: pi(a) = a tensor I acts on first factor, pi_o(b) = I tensor b^T acts on second factor, operators on different factors commute"
      linked_ids: [deliv-order-zero-derivation, test-order-zero-general, test-order-zero-basis, ref-connes1995, ref-van-suijlekom2024, ref-paper5, ref-paper6]
  deliverables:
    deliv-order-zero-derivation:
      status: passed
      path: "derivations/07-order-zero-condition.md"
      summary: "Complete derivation with pi_o explicit formula, J antilinearity handling, sector-by-sector analysis, order zero proof, naive vs contragredient analysis, forbidden proxy audit"
      linked_ids: [claim-pi-o-explicit, claim-order-zero, test-pi-o-form, test-pi-o-representation, test-order-zero-general, test-order-zero-basis]
  acceptance_tests:
    test-pi-o-form:
      status: passed
      summary: "pi_o(b) acts as I tensor b^T within each sector, derived by tracking J = antilinear (J_matrix * conj), with J_matrix encoding sector-swap and SWAP. The result confirms the transpose action on the second tensor factor."
      linked_ids: [claim-pi-o-explicit, deliv-order-zero-derivation, ref-paper6]
    test-pi-o-representation:
      status: passed
      summary: "pi_o is a *-representation of A^{op}: pi_o(ba) = pi_o(a)pi_o(b) (opposite multiplication), pi_o(a*) = pi_o(a)^dagger, pi_o(I) = I. All three verified algebraically at general n."
      linked_ids: [claim-pi-o-explicit, deliv-order-zero-derivation]
    test-order-zero-general:
      status: passed
      summary: "[pi(a), pi_o(b)] = 0 for ALL a, b in M_n(C) by the algebraic fact that (a tensor I) and (I tensor b^T) act on different tensor factors of C^n tensor C^n. Both particle and antiparticle sectors checked."
      linked_ids: [claim-order-zero, deliv-order-zero-derivation, ref-connes1995]
    test-order-zero-basis:
      status: passed
      summary: "All n^4 pairs [pi(E_{ij}), pi_o(E_{kl})] = [E_{ij} tensor I, I tensor E_{lk}] = 0 verified. Extension to all a, b by bilinearity."
      linked_ids: [claim-order-zero, deliv-order-zero-derivation]
  references:
    ref-connes1995:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Order zero condition [a, Jb*J^{-1}] = 0 cited as axiom of real spectral triple (Connes 1995)"
    ref-van-suijlekom2024:
      status: completed
      completed_actions: [use, cite]
      missing_actions: []
      summary: "Opposite algebra computation pattern from Ch. 2-4 used as methodological reference for pi_o derivation"
    ref-paper5:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "M_n(C)^sa and J = dagger from Paper 5 cited as source of algebra and involution"
    ref-paper6:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "SWAP operator P, doubled space H, J definition from Paper 6 cited as direct inputs"
  forbidden_proxies:
    fp-specific-ab:
      status: rejected
      notes: "Proof covers ALL a, b via tensor factor argument and bilinearity over matrix units. No specific pairs assumed."
    fp-no-j-tracking:
      status: rejected
      notes: "J's sector-swap explicitly tracked through Steps 4a-4c. Block-diagonal structure handles cross-sector terms."
    fp-linear-j:
      status: rejected
      notes: "Step 5 explicitly tracks antilinearity: conj(b_{jk}*) = b_{jk} produces b^T. Step 10 audits all J applications. WARNING confirms linear J gives wrong result."
  uncertainty_markers:
    weakest_anchors:
      - "Naive vs contragredient action: both satisfy order zero, but the correct choice depends on the evenness condition [gamma, pi(a)] = 0 (Phase 14)"
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations: []

duration: 12min
completed: 2026-03-23
---

# Plan 13-01: Order Zero Condition Summary

**Derived pi_o(b) = diag(I tensor b^T, I tensor b^T) via J antilinearity and proved order zero condition [pi(a), pi_o(b)] = 0 for all a, b in M_n(C) at general n**

## Performance

- **Duration:** 12 min
- **Started:** 2026-03-23T01:50:13Z
- **Completed:** 2026-03-23T02:02:00Z
- **Tasks:** 2
- **Files modified:** 1

## Key Results

- pi_o(b) = diag(I_n tensor b^T, I_n tensor b^T) for all b in M_n(C), derived at general n [CONFIDENCE: HIGH]
- [pi(a), pi_o(b)] = 0 for ALL a, b in M_n(C) at general n, proved by tensor factor commutativity [CONFIDENCE: HIGH]
- Both naive and contragredient algebra actions satisfy order zero [CONFIDENCE: HIGH]
- pi_o is a *-representation of A^{op}: pi_o(ba) = pi_o(a)pi_o(b) [CONFIDENCE: HIGH]

## Task Commits

1. **Task 1: Derive pi_o(b) explicitly at general n** - `8047355` (derive)
2. **Task 2: Prove order zero condition [pi(a), pi_o(b)] = 0** - `091ba33` (derive)

## Files Created/Modified

- `derivations/07-order-zero-condition.md` - Complete derivation of pi_o and order zero proof

## Next Phase Readiness

- Order zero condition PASSED: the gatekeeper axiom is satisfied for M_n(C) at general n
- pi_o(b) = I tensor b^T formula available for Plan 13-02 (SymPy verification) and Plan 13-03 (representation theory)
- Open question: naive vs contragredient action choice deferred to evenness condition analysis

## Contract Coverage

- Claim IDs advanced: claim-pi-o-explicit -> passed, claim-order-zero -> passed
- Deliverable IDs produced: deliv-order-zero-derivation -> derivations/07-order-zero-condition.md (passed)
- Acceptance test IDs run: test-pi-o-form -> passed, test-pi-o-representation -> passed, test-order-zero-general -> passed, test-order-zero-basis -> passed
- Reference IDs surfaced: ref-connes1995 -> cited, ref-van-suijlekom2024 -> used+cited, ref-paper5 -> cited, ref-paper6 -> cited
- Forbidden proxies rejected: fp-specific-ab -> rejected, fp-no-j-tracking -> rejected, fp-linear-j -> rejected

## Equations Derived

**Eq. (13.1) -- Opposite algebra action:**

$$\pi_o(b) = \mathrm{diag}(I_n \otimes b^T, \; I_n \otimes b^T)$$

for all b in M_n(C), where b^T is the matrix transpose.

**Eq. (13.2) -- Order zero condition:**

$$[\pi(a), \pi_o(b)] = [a \otimes I_n, I_n \otimes b^T] = 0 \quad \forall\, a, b \in M_n(\mathbb{C})$$

**Eq. (13.3) -- Key antilinearity identity:**

$$J\, \pi(b^*)\, J^{-1} \text{ acts as } I_n \otimes b^T \quad \text{(not } I_n \otimes \overline{b}\text{)}$$

The conjugation from J's antilinearity converts b^dagger entries to b entries: conj(b_{jk}*) = b_{jk}.

## Validations Completed

- n=1 limiting case: M_1(C) = C, all operators are scalars, commute trivially
- pi_o(I) = I verified
- pi_o *-representation axioms: multiplicativity (A^{op}), *-preserving, identity
- All n^4 matrix unit pairs checked via bilinearity
- Dimensional consistency: pi_o(b) is 2n^2 x 2n^2 for b in M_n(C)
- Antilinearity audit: all J applications use conj, no linear-J violations

## Decisions & Deviations

**Decision:** Used naive algebra action pi(a) = diag(a tensor I, a tensor I) as primary. Both naive and contragredient satisfy order zero, so the distinction is deferred to the evenness condition.

**Deviations:** None -- plan executed exactly as written.

## Open Questions

- Which algebra action (naive or contragredient) satisfies the evenness condition [gamma, pi(a)] = 0? This determines the correct action for the full spectral triple.
- The pi_o formula must be verified computationally at specific n (Plan 13-02, SymPy).

## Self-Check: PASSED

- [x] derivations/07-order-zero-condition.md exists
- [x] Commit 8047355 exists (Task 1)
- [x] Commit 091ba33 exists (Task 2)
- [x] pi_o formula derived and verified
- [x] Order zero proved universally
- [x] All forbidden proxies rejected
- [x] All acceptance tests passed
- [x] All references surfaced

---

_Phase: 13-order-zero-representation-theory_
_Plan: 01_
_Completed: 2026-03-23_
