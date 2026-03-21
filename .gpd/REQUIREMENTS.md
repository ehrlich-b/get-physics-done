# Requirements: QM from Algebraic Genericity

**Defined:** 2026-03-20
**Core Research Question:** Does the sequential product structure of self-modeling systems satisfy van de Wetering's axioms S1-S7, thereby deriving quantum mechanics from a single operational premise?

## Primary Requirements

### Sequential Product Formalization

- [ ] **SPFM-01**: Formally define the self-modeling sequential product on a finite-dimensional order unit space, exploring both effect algebra framings (E(B) and E(B x M)), and determine which framing is correct
- [ ] **SPFM-02**: Verify axioms S1-S3 and S5-S7 for the self-modeling sequential product (per van de Wetering arXiv:1803.11139 exclusively — NOT Gudder-Greechie axioms)
- [ ] **SPFM-03**: Prove or disprove S4 (symmetry of orthogonality) for the self-modeling construction — this is the decisive test
- [ ] **SPFM-04**: Verify non-associativity of the self-modeling sequential product (associativity forces commutativity per Westerbaan-Westerbaan-van de Wetering 2020)
- [ ] **SPFM-05**: If S4 fails, characterize exactly which physical property of the self-model's update map is responsible for the failure

### Local Tomography

- [ ] **LTOM-01**: Formalize "independently accessible B and M" in the order unit space / GPT framework
- [ ] **LTOM-02**: Prove or disprove that B-M independent accessibility implies local tomography on B tensor M
- [ ] **LTOM-03**: If local tomography fails, identify which additional assumption bridges the gap

### Paper Assembly

- [ ] **PAPR-01**: Assemble Paper 5 with the complete chain L4 → sequential product → Jordan algebra → C*-algebra → QM (full version if Phases 1-2 succeed, conditional version L4 + C* if either fails)

### D'Ariano Backup

- [ ] **DRBK-01**: If S4 fails, verify whether the B-M correlation state satisfies D'Ariano's Postulate 5 (symmetric faithful state), enabling explicit involution construction

## Follow-up Requirements

### Extended Analysis

- **EXTD-01**: Verify S1-S7 for infinite-dimensional generalizations (JB-algebra setting)
- **EXTD-02**: Investigate whether non-Markovian self-models change the S4 verdict
- **EXTD-03**: Connect to other QM reconstruction programs (Hardy, Chiribella-D'Ariano-Perinotti) and compare premise counts

## Out of Scope

| Topic | Reason |
| ----- | ------ |
| Standard Model derivation | Level 4+ in the hierarchy, far beyond current scope |
| Self-modeling constants experiment | Level 6, requires experimental apparatus |
| Experiential measure extensions | v1.0 is complete; this milestone is about algebraic structure |
| Infinite-dimensional systems | All proofs restricted to finite dimensions |
| Blog series writeup | Separate project |

## Accuracy and Validation Criteria

| Requirement | Accuracy Target | Validation Method |
| ----------- | --------------- | ----------------- |
| SPFM-01 | Exact formal definition | Audit for Hilbert space imports (circularity check) |
| SPFM-02 | Rigorous proof for each axiom | Line-by-line verification; positive control (Luders product must pass) |
| SPFM-03 | Rigorous proof or explicit counterexample | If proof: check each step for hidden assumptions. If disproof: construct explicit a,b with a.b=0 but b.a!=0 |
| SPFM-04 | Explicit non-associative triple | Construct a,b,c with (a.b).c != a.(b.c) |
| SPFM-05 | Precise identification of failing property | Must point to specific step in S4 proof that breaks |
| LTOM-01 | Exact formal definition | Check compatibility with GPT framework (Barnum-Wilce) |
| LTOM-02 | Rigorous proof or explicit counterexample | Verify against known cases (QM passes, real QM fails) |
| PAPR-01 | Publication-ready manuscript | Self-contained logical chain; peer-review ready |
| DRBK-01 | Rigorous verification | Check faithfulness and symmetry conditions explicitly |

## Contract Coverage

| Requirement | Decisive Output / Deliverable | Anchor / Benchmark / Reference | Prior Inputs / Baselines | False Progress To Reject |
| ----------- | ----------------------------- | ------------------------------ | ------------------------ | ------------------------ |
| SPFM-01 | Formal definition with chosen effect algebra framing | van de Wetering arXiv:1803.11139 definitions | v1.0 composite process framework | Definition that uses Hilbert space primitives (circular) |
| SPFM-02 | Proof of each axiom S1-S3, S5-S7 | Luders product as positive control | — | Proof that works for any sequential product (proves nothing about self-model) |
| SPFM-03 | Proof or disproof of S4 | — (no prior benchmark) | — | Short proof (S4 is hard; short means something is hidden) |
| SPFM-04 | Non-associative triple | Westerbaan et al. (2020) theorem | — | Associativity claim without explicit test |
| LTOM-01 | Formal definition of independent accessibility | Barnum-Wilce GPT framework | — | Conflating accessibility with tomography |
| LTOM-02 | Proof or disproof of local tomography | Hanche-Olsen (1985) | — | Assuming complex field without proof |
| PAPR-01 | Paper 5 manuscript | All v2.0 anchors | v1.0 papers | Paper that assumes C* without acknowledging it as an additional premise |
| DRBK-01 | Faithfulness/symmetry verification | D'Ariano arXiv:quant-ph/0611094 | — | Assuming faithful state without checking |

## Traceability

| Requirement | Phase | Status |
| ----------- | ----- | ------ |
| SPFM-01 | — | Pending |
| SPFM-02 | — | Pending |
| SPFM-03 | — | Pending |
| SPFM-04 | — | Pending |
| SPFM-05 | — | Pending |
| LTOM-01 | — | Pending |
| LTOM-02 | — | Pending |
| LTOM-03 | — | Pending |
| PAPR-01 | — | Pending |
| DRBK-01 | — | Pending |

**Coverage:**

- Primary requirements: 10 total
- Mapped to phases: 0 (pending roadmap)
- Unmapped: 10 (warning — roadmap will resolve)

---

_Requirements defined: 2026-03-20_
_Last updated: 2026-03-20 after initial definition_
