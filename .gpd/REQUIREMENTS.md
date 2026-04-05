# Requirements: Gap C Complexification from Sequential Product

**Defined:** 2026-04-04
**Core Research Question:** Does the C*-observer's sequential product extend Cl(9,0) to Cl(9,C), closing Gap C?

## Primary Requirements

### Sequential Product Complexification

- [ ] **SEQP-01**: Compute sqrt(T_a) for all 9 Cl(9,0) generators (eigenvalues +/-1/2) and verify sqrt(T_a) T_b sqrt(T_a) = (i/2)*T_b for all 72 anticommuting pairs. GO/NO-GO gate.
- [ ] **SEQP-02**: Prove the C*-observer is physically justified in applying the complex functional calculus to indefinite Peirce operators T_a (not effects). Bridge the gap between Gudder-Greechie (effects only) and the observer's actual measurement algebra.
- [ ] **SEQP-03**: Show the C-linear closure of {sqrt(T_a) T_b sqrt(T_a) : a != b} generates M_16(C), and identify this with Cl(9,C) = M_16(C) + M_16(C). Verify the spinor module extends S_9 -> S_{10}^+.

### Gap C Theorem

- [ ] **GAPC-01**: State Gap C closure as a single theorem: C*-observer (Paper 5) -> complex FC on Cl(9,0) generators -> measurement algebra = Cl(9,C) -> spinor module complexifies to S_{10}^+ -> Spin(9) extends to Spin(10) -> F_4 extends to E_6 -> chirality from Cl(6).
- [ ] **GAPC-02**: Verify compatibility with Paper 7's existing 9-link chain (L1-L9). Confirm no regression in existing links. Identify what Gap C closure upgrades in the gap register.

### Contingency

- [ ] **CONT-01**: If SEQP-02 fails (complex FC not physically justified), evaluate Peirce multiplication route and the 4 formal routes (conditional expectations, state-effect, GNS, tensor product) with the new framing from the literature survey.
- [ ] **CONT-02**: If all algebraic routes fail, characterize the precise obstruction, state Gap C status as "algebraic impossibility confirmed; selection argument (Paper 8) is ceiling," and identify weakest sufficient condition for complexification.

## Follow-up Requirements

### Extended Analysis

- **SEQP-04**: Identify the 10th Clifford generator explicitly -- relate the (i/2) factor in the sequential product to gamma_10 in Cl(10,0)
- **GAPC-03**: Connect Gap C closure to Alfsen-Shultz dynamical correspondence (alternative proof route via JB -> C* lifting)
- **PAPR-01**: Integrate Gap C closure into Paper 7 revision (update complexification section, gap register, abstract)

## Out of Scope

| Topic | Reason |
| ----- | ------ |
| Quantum SSB at S_eff=1/2 | Separate conditionality, not related to Gap C |
| Gap A (continuum limit) | Different gap, addressed in v9.0/v10.0 |
| Gap B (symmetry breaking inputs) | Different gap, u in S^6 choice |
| Paper 7 full revision | Deferred until Gap C status is resolved |
| Spectral action computation | Beyond Gap C scope |

## Accuracy and Validation Criteria

| Requirement | Accuracy Target | Validation Method |
| ----------- | --------------- | ----------------- |
| SEQP-01 | Exact (algebraic identity) | SymPy symbolic verification + NumPy numerical check for all 72 pairs |
| SEQP-02 | Rigorous proof | Check premises match Paper 5 Def 2.6; no circular arguments |
| SEQP-03 | Exact (dimension counting) | Verify dim_C(closure) = 256 = dim(M_16(C)); identify Cl(9,C) decomposition |
| GAPC-01 | Complete logical chain | Each step cites specific theorem/equation; no gaps |
| GAPC-02 | Zero regressions | All 9 existing links still valid; gap register updated |
| CONT-01 | Exhaustive | All 4 routes evaluated with new framing |
| CONT-02 | Precise obstruction | Weakest sufficient condition identified |

## Contract Coverage

| Requirement | Decisive Output | Anchor / Reference | Prior Inputs | False Progress To Reject |
| ----------- | --------------- | ------------------ | ------------ | ------------------------ |
| SEQP-01 | Verified identity (i/2)*T_b for 72 pairs | Cl(9,0) generators from v8.0 Phase 29 | T_b matrices from v8.0 | Partial verification (must be ALL pairs) |
| SEQP-02 | Theorem with proof | Paper 5 Def 2.6, Gudder-Greechie 2002 | v8.0 impossibility theorems | Physical hand-waving without theorem |
| SEQP-03 | Dimension = 256 over C | Cl(9,C) = M_16(C) + M_16(C) (Lawson-Michelsohn) | SEQP-01 result | Generating a proper subalgebra of M_16(C) |
| GAPC-01 | Single theorem statement + proof | Paper 7 chain, Paper 5 | SEQP-01-03 | Theorem with unjustified step |
| GAPC-02 | Compatibility verification | Paper 7 L1-L9 | v5.0 Paper 7 | Claiming compatibility without checking each link |

## Traceability

| Requirement | Phase | Status |
| ----------- | ----- | ------ |
| SEQP-01 | Phase 42 | Pending |
| SEQP-02 | Phase 43 | Pending |
| SEQP-03 | Phase 43 | Pending |
| GAPC-01 | Phase 44 | Pending |
| GAPC-02 | Phase 44 | Pending |
| CONT-01 | Phase 45 (conditional) | Pending |
| CONT-02 | Phase 45 (conditional) | Pending |

**Coverage:**

- Primary requirements: 7 total
- Mapped to phases: 7/7
- Unmapped: 0

---

_Requirements defined: 2026-04-04_
_Last updated: 2026-04-04 after roadmap creation (Phases 42-45)_
