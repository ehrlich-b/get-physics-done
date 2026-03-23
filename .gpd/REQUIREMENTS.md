# Requirements: Chirality from h_3(O) via Cl(6)

**Defined:** 2026-03-23
**Core Research Question:** Does the observer's complexification of h_3(O) automatically produce the correct chiral SM representation via Cl(6)?

## Primary Requirements

### Complexification (Part A)

- [ ] **CMPL-01**: Prove that C*-algebra observer nature forces complexification of Peirce V_1 = O^2 from real Spin(9) spinor S_9 to complex Spin(10) Weyl spinor, using only Paper 5 local tomography result
- [ ] **CMPL-02**: Show complexification at h_3(O) level upgrades F_4 -> E_6 (structure group) and Spin(9) -> Spin(10) (stabilizer), with explicit Peirce decomposition tracking

### Chirality (Part B)

- [ ] **CHIR-01**: Derive Cl(6) subalgebra inside Cl(10) from octonion splitting O = C + C^3, construct the 6 internal gamma matrices explicitly
- [ ] **CHIR-02**: Show Cl(6) volume form omega_6 = gamma_1...gamma_6 defines particle projector P = (1/2)(1 - i*omega_6) selecting 16-dim Weyl representation; verify Pati-Salam Spin(6) x Spin(4) / Z_2 as stabilizer
- [ ] **CHIR-03**: Prove SM gauge group with LEFT (chiral) embedding obtained from Pati-Salam breaking SU(4) -> SU(3) x U(1) via same complex structure; SU(2)_L acts on left-handed fermions only
- [ ] **CHIR-04**: Verify Furey's Witt decomposition result -- creation/annihilation operators a_i = (1/2)(-e_{i+4} + i*e_i) automatically channel SU(2) to single chirality without ad hoc projectors

### Synthesis

- [ ] **SYNT-01**: Unify Parts A and B: single complex structure choice (embedding C in O) simultaneously gives SM gauge group (Gap B step 2) and chirality (Cl(6) volume form)
- [ ] **SYNT-02**: Connect Cl(6)/Pati-Salam route (with chirality) to Todorov-Drenska F_4 intersection (without chirality) -- same group, now with correct chiral representation

### Computational Verification

- [ ] **COMP-01**: Explicit matrix construction of Cl(6) inside Cl(10) and verification of volume form action on 32-dim Dirac spinor of Spin(10)
- [ ] **COMP-02**: Verify SM quantum numbers (Y, I_3, color) emerge correctly from Cl(6) Witt decomposition for all 16 states of one generation

### Paper Assembly

- [ ] **PAPR-01**: Paper 7 "Chirality from h_3(O)" with complete derivation chain from self-modeling -> h_3(O) -> complexification -> Cl(6) -> chirality, honest gap identification, connection to Papers 5-6

## Follow-up Requirements

### Extended Analysis

- **EXTN-01**: Full spectral action computation from h_3(O) spectral triple (coupling constants, Higgs potential)
- **EXTN-02**: Generation structure -- why 3 families from h_3(O) (Jordan algebra rank 3)
- **EXTN-03**: Connection between Paper 6 GR (Jacobson) and spectral action GR from h_3(O)

## Out of Scope

| Topic | Reason |
| ----- | ------ |
| Full spectral action computation | Requires established spectral triple; separate paper |
| Phenomenological predictions (masses, mixing angles) | Requires spectral action; beyond current scope |
| Gap A closure (why h_3(O)) | Assumed closed per prompt; separate derivation |
| Gap B step 1 (rank-1 idempotent choice) | Assumed as input; symmetry breaking mechanism separate |
| Lorentzian signature | Euclidean sufficient for algebraic classification |
| Generations (why 3 families) | Separate question; follow-up requirement |

## Accuracy and Validation Criteria

| Requirement | Accuracy Target | Validation Method |
| ----------- | --------------- | ----------------- |
| CMPL-01 | Exact algebraic proof | Verify Spin(9) -> Spin(10) representation theory |
| CMPL-02 | Exact (F_4 -> E_6 embedding) | Cross-check with Boyle 2020 and Yokota |
| CHIR-01 | Exact Clifford algebra construction | Matrix verification at dim 32 |
| CHIR-02 | Exact projector eigenvalues | Compute omega_6^2 = 1, trace P = 16 |
| CHIR-03 | Exact SM quantum numbers | Compare all 16 states to known SM table |
| CHIR-04 | Exact Witt decomposition | Verify a_i satisfy Clifford relations |
| COMP-01 | Zero tolerance (exact algebra) | All Clifford relations verified computationally |
| COMP-02 | Exact quantum number match | All 16 states identified correctly |

## Contract Coverage

| Requirement | Decisive Output | Anchor / Reference | Prior Inputs | False Progress To Reject |
| ----------- | --------------- | ------------------ | ------------ | ------------------------ |
| CMPL-01 | Proof that C*-nature forces complexification | Boyle 2020 (E_6 from h_3^C(O)) | Paper 5 (C*-algebra, local tomography) | Assuming complexification without deriving from C*-nature |
| CHIR-01 | Explicit Cl(6) construction | Todorov 2022 (arXiv:2206.06912) | Octonion splitting O = C + C^3 | Using Cl(6) without deriving from O splitting |
| CHIR-03 | SM with LEFT embedding | Furey 2018 (arXiv:1806.00612), Baez-Sawin | Cl(6) volume form | Claiming chirality without distinguishing L from diagonal |
| SYNT-01 | One choice -> two consequences | Todorov-Drenska, Furey, Boyle | Parts A and B | Treating gauge group and chirality as independent results |
| PAPR-01 | Paper 7 with complete chain | Papers 5-6, all Part A/B refs | All prior phases | Overclaiming; glossing over gaps |

## Traceability

| Requirement | Phase | Status |
| ----------- | ----- | ------ |
| CMPL-01 | TBD | Pending |
| CMPL-02 | TBD | Pending |
| CHIR-01 | TBD | Pending |
| CHIR-02 | TBD | Pending |
| CHIR-03 | TBD | Pending |
| CHIR-04 | TBD | Pending |
| SYNT-01 | TBD | Pending |
| SYNT-02 | TBD | Pending |
| COMP-01 | TBD | Pending |
| COMP-02 | TBD | Pending |
| PAPR-01 | TBD | Pending |

**Coverage:**

- Primary requirements: 11 total
- Mapped to phases: 0
- Unmapped: 11 (roadmap pending)

---

_Requirements defined: 2026-03-23_
_Last updated: 2026-03-23 after initial definition_
