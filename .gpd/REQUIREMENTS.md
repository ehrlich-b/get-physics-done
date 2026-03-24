# Requirements: Gap C -- Complexification from C*-Measurement Maps

**Defined:** 2026-03-24
**Core Research Question:** Does a C*-algebra observer probing V_{1/2} = O^2 inside h_3(O) necessarily induce complexification V -> V tensor_R C?

## Primary Requirements

### Measurement Map Formalization

- [ ] **MEAS-01**: Formalize C*-observer measurement maps on V_{1/2} via conditional expectations (Effros-Stormer 1979). Determine whether the positive unital projection P: h_3(O) -> A_obs necessarily complexifies V_{1/2}.
- [ ] **MEAS-02**: Formalize via state-effect duality. Determine whether the C-linear extension omega^C of a state omega on M_n(C)^sa, when used to probe V_{1/2}, provides a canonical complexification.
- [ ] **MEAS-03**: Formalize via GNS construction. Determine whether representing V_{1/2} on the complex GNS Hilbert space H_omega canonically induces V tensor_R C.
- [ ] **MEAS-04**: Formalize via tensor product. Determine whether A tensor_R V_{1/2} naturally complexifies to A tensor_C V_{1/2}^C as the correct model of "observer probes V_{1/2}".

### Uniqueness and Canonicity

- [ ] **UNIQ-01**: Prove complexification is unique — no choices beyond the observer's C*-nature (if complexification is forced by any route)
- [ ] **UNIQ-02**: Verify Spin(10) action extends Spin(9) in the specific construction from the successful route (multiplicity-free branching S^+_{10}|_{Spin(9)} = S_9^C)
- [ ] **UNIQ-03**: Verify compatibility with Jordan structure — Peirce decomposition of h_3(O)^C gives 27 = 1 + 10 + 16 under Spin(10) subset E_6

### Observable Algebra / Jordan Distinction

- [ ] **JORD-01**: Identify precisely why the Jordan-algebraic setting (Peirce interface, L_{E_{11}} action) forces complexification, whereas a generic C*-system probing generic real spaces does not
- [ ] **JORD-02**: Investigate V_1 C*-upgrade through Peirce rules — if observer forces V_1 from R to C (1-dim over C = 2-dim over R), determine whether Peirce rules V_1 . V_{1/2} subset V_{1/2} force V_{1/2} to be a C-module

### Formalization

- [ ] **FORM-01**: State Gap C closure as a single theorem: "If V_1 carries a C*-algebra structure (from self-modeling), then V_{1/2} carries a canonical complex structure, Spin(9) extends uniquely to Spin(10), and F_4 upgrades to E_6"
- [ ] **FORM-02**: If full closure fails, characterize the minimal additional assumption needed, with precise statement of what Gap C costs

## Follow-up Requirements

### Extensions

- **EXTD-01**: Determine whether the result is specific to h_3(O) or generalizes to all real Jordan modules probed by C*-systems
- **EXTD-02**: Connect to thermodynamic route to complexification (Paper 8 material — time-orientation -> chiral spinors)
- **EXTD-03**: Full Paper 7 revision incorporating Gap C closure

## Out of Scope

| Topic | Reason |
| ----- | ------ |
| Chirality derivation | Already complete in v5.0 (Cl(6) route) |
| Spectral action computation | Beyond Paper 7 scope |
| Gaps A, B1, B2 | Independent of Gap C; symmetry-breaking inputs |
| Thermodynamic complexification route | Paper 8 material, independent motivation |
| Infinite-dimensional Jordan algebras | Paper 5 restriction to finite dimensions |

## Accuracy and Validation Criteria

| Requirement | Accuracy Target | Validation Method |
| ----------- | --------------- | ----------------- |
| MEAS-01..04 | Exact proof or explicit counterexample | Check all hypotheses against Alfsen-Shultz / Upmeier theory |
| UNIQ-01 | Uniqueness proof (Schur's lemma level) | Verify multiplicity-free condition |
| UNIQ-02 | Exact branching rule match | Cross-check with Boyle 2020, v5.0 Phase 18 |
| UNIQ-03 | Exact dimension count 27 = 1 + 10 + 16 | Cross-check with Baez 2002 |
| JORD-01 | Conceptual argument with precise counterexample for non-Jordan case | Construct explicit C*-on-real-space that does NOT complexify |
| JORD-02 | Exact algebraic proof using Peirce multiplication rules | Verify against Alfsen-Shultz Ch. 8 |
| FORM-01 | Complete formal theorem with all hypotheses stated | Independent verification of each logical step |

## Contract Coverage

| Requirement | Decisive Output / Deliverable | Anchor / Benchmark / Reference | Prior Inputs / Baselines | False Progress To Reject |
| ----------- | ----------------------------- | ------------------------------ | ------------------------ | ------------------------ |
| MEAS-01 | Theorem or counterexample for conditional expectation route | Effros-Stormer 1979 | v5.0 Peirce decomposition | Proving for wrong algebra |
| MEAS-02 | Theorem or counterexample for state-effect route | Alfsen-Shultz 2001 | Paper 5 C*-observer | Generic C-linearity claim |
| MEAS-03 | Theorem or counterexample for GNS route | Upmeier 1987 | Paper 5 GNS | Complexification without canonical structure |
| MEAS-04 | Theorem or counterexample for tensor product route | Hanche-Olsen 1983 | Paper 5 tensor structure | Assuming tensor = complexify |
| UNIQ-01 | Uniqueness proof | Schur's lemma | v5.0 branching rule | Uniqueness for wrong module |
| JORD-01 | Precise identification of Jordan-specific mechanism | Baez 2002, Alfsen-Shultz | v5.0 Phase 18 Peirce | Vague "Jordan is special" |
| FORM-01 | Single theorem statement with proof | All above | All v5.0 inputs | Theorem with hidden assumptions |

## Traceability

| Requirement | Phase | Status |
| ----------- | ----- | ------ |
| MEAS-01 | Phase 22: Measurement Maps | Pending |
| MEAS-02 | Phase 22: Measurement Maps | Pending |
| MEAS-03 | Phase 22: Measurement Maps | Pending |
| MEAS-04 | Phase 22: Measurement Maps | Pending |
| UNIQ-01 | Phase 23: Uniqueness | Pending |
| UNIQ-02 | Phase 23: Uniqueness | Pending |
| UNIQ-03 | Phase 23: Uniqueness | Pending |
| JORD-01 | Phase 24: Observable Algebra | Pending |
| JORD-02 | Phase 24: Observable Algebra | Pending |
| FORM-01 | Phase 25: Formalization | Pending |
| FORM-02 | Phase 25: Formalization | Pending |

**Coverage:**

- Primary requirements: 11 total
- Mapped to phases: 11
- Unmapped: 0

---

_Requirements defined: 2026-03-24_
_Last updated: 2026-03-24 after initial definition_
