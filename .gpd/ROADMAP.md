# Roadmap: Experiential Measure on Structure Space -- Formalization

## Overview

This project closes three formal gaps in the experiential measure framework: assembling Theorem A (Boltzmann brain negligibility) from its seven constituent metastability lemmas into a self-contained proof with explicit error scaling, proving Lipschitz stability of the experiential density rho under kernel perturbations, and testing the Born-Fisher-Experiential conjecture on a toy qubit model. The deliverables are two proofs and one numerical falsification test.

## Contract Overview

| Contract Item | Kind | Advanced By | Status |
| --- | --- | --- | --- |
| claim-theorem-a | claim | Phase 1 | Verified |
| claim-lipschitz | claim | Phase 2 | Planned |
| claim-born-fisher | claim | Phase 3 | Planned |
| deliv-theorem-a-proof | derivation | Phase 1 | Verified |
| deliv-lipschitz-proof | derivation | Phase 2 | Planned |
| deliv-qubit-code | code | Phase 3 | Planned |
| obs-theorem-a | proof obligation | Phase 1 | Verified |
| obs-lipschitz | proof obligation | Phase 2 | Planned |
| obs-qubit-test | scalar | Phase 3 | Planned |
| fp-sketch-only | forbidden proxy | Phase 1 | Rejected |
| fp-numerics-only | forbidden proxy | Phase 2 | Active |

## Phases

**Phase Numbering:**

- Integer phases (1, 2, 3): Planned research work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [x] **Phase 1: Theorem A Assembly** - Compose the 7-lemma proof of Boltzmann brain negligibility with explicit error scaling
- [ ] **Phase 2: Lipschitz Stability** - Prove rho is Lipschitz in the transition kernel and verify numerically
- [ ] **Phase 3: Born-Fisher Test** - Implement qubit model and compute I_vN(B;M)/S_vN(B) for Born vs non-Born distributions

## Phase Details

### Phase 1: Theorem A Assembly

**Goal:** The 7 constituent lemmas (FW basin partition, BEGK residence times, QSD convergence, stable measure lower bound, BB occupation upper bound, DV concentration, ratio assembly) are composed into a single self-contained proof with explicit error scaling showing mu_BB/mu_stable <= C*exp(-(Delta_s - Delta_b - alpha)/epsilon).

**Depends on:** Nothing (first phase)

**Requirements:** DERV-01, DERV-03, VALD-03

**Contract Coverage:**

- Advances: claim-theorem-a, deliv-theorem-a-proof, obs-theorem-a
- Deliverables: Self-contained proof assembling all 7 lemmas with composition chain and exponential bound (deliv-theorem-a-proof)
- Anchor coverage: ref-begk (BEGK residence time bounds, Lemma 2), ref-fw (Freidlin-Wentzell cycle hierarchy, Lemma 1), ref-dv (Donsker-Varadhan concentration, Lemma 6); prior outputs: draft.md Section 8 (7-lemma dependency graph), three_state_chain.py (FW verification)
- Crucial inputs: Theorem A 7-lemma dependency graph from draft Section 8; composite Markov process factorization condition
- Forbidden proxies: fp-sketch-only -- another proof sketch with "the tools exist" language but no assembled composition is NOT acceptable progress
- User-stated observables: Complete logical chain from lemma statements to Theorem A conclusion
- Stop/rethink: If BEGK/DV/QSD error bounds do not compose -- exponential suppression breaks in the full chain

**Success Criteria** (what must be TRUE):

1. Each of the 7 lemmas has a precise statement citing the specific theorem from BEGK, FW, DV, or QSD literature that supplies it
2. The composition chain has no logical gaps: the output of each lemma feeds as input to the next in the dependency graph, with explicit verification that error terms compose
3. The product of individual error bounds preserves the exponential form: mu_BB/mu_stable <= C*exp(-(Delta_s - Delta_b - alpha)/epsilon) with C explicit
4. The assembled proof is consistent with the three-state chain numerical verification (mu_BB/mu_stable matches analytical formula within 1%)
5. No deferred steps remain in the main argument (constants may be deferred to appendix per approved decision)

**Plans:** 2 plans

Plans:

- [x] 01-01-PLAN.md -- State all 7 lemmas with explicit error terms, literature citations, and typed dependency graph
- [x] 01-02-PLAN.md -- Compose error terms through dependency chain, assemble complete proof, validate against three-state chain

### Phase 2: Lipschitz Stability

**Goal:** The experiential density rho(P) = I(B;M) * (1 - I(B;M)/H(B)) is proven Lipschitz continuous under kernel perturbations ||P - P'||_inf, with the Lipschitz constant L characterized as a function of |Omega| and spectral gap, and the bound is verified numerically against toy model perturbations.

**Depends on:** Nothing (independent of Phase 1; different mathematical machinery)

**Requirements:** DERV-02, VALD-01

**Contract Coverage:**

- Advances: claim-lipschitz, deliv-lipschitz-proof, obs-lipschitz
- Deliverables: Proof of Lipschitz stability with explicit L dependence on |Omega| and spectral gap (deliv-lipschitz-proof); must contain perturbation bound, MI continuity argument, explicit L dependence
- Anchor coverage: ref-lmc (LMC statistical complexity -- rho belongs to this family), ref-gell-mann-lloyd (effective complexity -- broader family context); prior outputs: composite_self_model.py (parametric sweep baseline for numerical verification)
- User-stated observables: Lipschitz constant L as function of |Omega| and spectral gap
- Forbidden proxies: fp-numerics-only -- more toy model numerical runs confirming stability intuition without a formal Lipschitz bound is NOT acceptable progress
- Unresolved questions: Exact form of L(|Omega|, spectral_gap) -- to be resolved by this phase

**Success Criteria** (what must be TRUE):

1. The bound |rho(P) - rho(P')| <= L * ||P - P'||_inf is proven with no hand-waving steps
2. L is characterized explicitly: its dependence on |Omega| and the spectral gap of P is written down, not left as "there exists an L"
3. The proof uses perturbation theory for stationary distributions and mutual information continuity -- both steps are rigorous
4. Numerical verification: L_numerical <= L_proven for random kernel perturbations of the 7-chain toy model (100+ perturbations tested)
5. In the limit of large spectral gap (fast mixing), L remains finite and the bound is non-vacuous

**Plans:** 2 plans

Plans:

- [ ] 02-01-PLAN.md -- Derive 3-step Lipschitz bound with explicit L = O(ln(|Omega|)/gap(P)) and verify limiting cases
- [ ] 02-02-PLAN.md -- Numerically verify L_proven against 1000+ random perturbations of toy model, test scaling with gap and |Omega|

### Phase 3: Born-Fisher Test

**Goal:** A toy qubit composite process is implemented, I_vN(B;M) and S_vN(B) are computed for both Born-rule and non-Born distributions, and the ratio I_vN(B;M)/S_vN(B) is evaluated to deliver a clear numerical verdict on whether the Born-Fisher-Experiential conjecture holds.

**Depends on:** Nothing (independent computational work; different from proof phases)

**Requirements:** CALC-01, CALC-02, CALC-03, VALD-02

**Contract Coverage:**

- Advances: claim-born-fisher, deliv-qubit-code, obs-qubit-test
- Deliverables: Python code implementing toy qubit composite process (deliv-qubit-code); must contain qubit density matrix construction, von Neumann entropy computation, Born vs non-Born comparison
- Anchor coverage: ref-baez-dolan (groupoid cardinality motivating 1/|Aut(x)| weighting); prior outputs: quantum-extension/draft.md (quantum extension framework), composite_self_model.py (classical model for cross-check)
- Crucial inputs: Experiential density definition rho(p) = I(B;M) * (1 - I(B;M)/H(B)); product space Omega = B x M with factorization condition
- User-stated observables: I_vN(B;M)/S_vN(B) ratio for Born-rule distributions -- target is 0.5 (or demonstrable failure)
- Stop/rethink: If I_vN(B;M) = S_vN(B)/2 fails for Born-rule distributions -- conjecture is falsified, which is a valid and decisive result
- Unresolved questions: Whether qubit model needs 2x2 or larger Hilbert space to be informative -- to be resolved early in this phase

**Success Criteria** (what must be TRUE):

1. Qubit density matrices are correctly constructed: trace = 1, positive semidefinite, correct dimension
2. Von Neumann entropy S_vN and mutual information I_vN are computed to numerical precision ~1e-12 and cross-checked against analytical formulas where available
3. Born-rule distributions (p_k = |alpha_k|^2) yield a clear numerical answer for I_vN(B;M)/S_vN(B): either equals 0.5 within numerical precision or demonstrably does not
4. Non-Born distributions show a different ratio, establishing that Born rule is special (or showing it is not)
5. In the decoherence limit (t >> tau_D), quantum rho_Q reduces to the classical rho, confirming consistency with the existing classical toy model

**Plans:** TBD

Plans:

- [ ] 03-01: TBD
- [ ] 03-02: TBD

## Phase Dependencies

| Phase | Depends On | Enables | Critical Path? |
| --- | --- | --- | --- |
| 1 - Theorem A Assembly | -- | -- | Yes (independent) |
| 2 - Lipschitz Stability | -- | -- | Yes (independent) |
| 3 - Born-Fisher Test | -- | -- | Yes (independent) |

**Critical path:** All three phases are independent and can execute in any order or in parallel.

**Parallelizable:** Phase 1, Phase 2, and Phase 3 have no inter-dependencies. Phase 1 and Phase 2 are both proof work but use different mathematical tools (metastability composition vs perturbation theory). Phase 3 is computational and uses different artifacts entirely.

## Risk Register

| Phase | Top Risk | Probability | Impact | Mitigation |
| --- | --- | --- | --- | --- |
| 1 | BEGK/DV/QSD error bounds do not compose -- exponential form breaks | MEDIUM | HIGH | Backtrack trigger: if error product grows polynomially rather than exponentially, identify which lemma boundary fails and attempt tighter bound or restructured composition |
| 2 | Lipschitz constant L is vacuously large (bound is technically true but useless) | LOW | MEDIUM | Derive L carefully; if L >> 1 for small |Omega|, check whether tighter MI continuity bounds exist or whether the rho functional form admits a sharper estimate |
| 3 | Qubit model too small to be informative about general conjecture | MEDIUM | MEDIUM | Start with 2x2, check sensitivity to dimension; if ambiguous, extend to 3x3 or 4x4 before concluding |
| 3 | Born-Fisher conjecture falsified | MEDIUM | LOW | This is a valid decisive result per the contract; document cleanly and report |

## Backtracking Triggers

- Phase 1: If the composition chain produces error terms that grow faster than exponentially in 1/epsilon, the proof strategy must be reconsidered. Check whether a different ordering of the lemma composition yields better bounds before abandoning the approach.
- Phase 2: If perturbation theory for stationary distributions yields only L = infinity for some kernel perturbations, restrict the perturbation class (e.g., to those preserving irreducibility with uniform spectral gap bound) and re-derive.
- Phase 3: If Born-rule distributions do NOT satisfy I_vN(B;M) = S_vN(B)/2, this is a stop/rethink condition per the contract. The conjecture is falsified -- document the result and flag for user decision on whether to investigate modified conjectures.

## Progress

**Execution Order:**
Phases execute in numeric order (1, 2, 3) but are all independent.

| Phase | Plans Complete | Status | Completed |
| --- | --- | --- | --- |
| 1. Theorem A Assembly | 2/2 | Complete | 2026-03-16 |
| 2. Lipschitz Stability | 0/TBD | Not started | - |
| 3. Born-Fisher Test | 0/TBD | Not started | - |
