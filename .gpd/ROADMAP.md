# Roadmap: Experiential Measure on Structure Space

## Milestones

- **v1.0 Experiential Measure Formalization** -- Phases 1-3 (completed 2026-03-16)
- **v2.0 QM from Algebraic Genericity** -- Phases 4-7 (completed 2026-03-21)
- **v3.0 GR Extension** -- Phases 8-12 (completed 2026-03-22)
- **v4.0 Spectral Triple from Self-Modeling** -- Phases 13-15 (closed 2026-03-23, medium success)
- **v5.0 Chirality from h_3(O) via Cl(6)** -- Phases 18-21 (active)

## Phases

<details>
<summary>v1.0 Experiential Measure Formalization (Phases 1-3) -- COMPLETED 2026-03-16</summary>

- [x] Phase 1: Theorem A Assembly (2/2 plans) -- completed 2026-03-16
- [x] Phase 2: Lipschitz Stability (2/2 plans) -- completed 2026-03-16
- [x] Phase 3: Born-Fisher Test (2/2 plans) -- completed 2026-03-16

See `.gpd/milestones/v1.0-ROADMAP.md` for full details.

</details>

<details>
<summary>v2.0 QM from Algebraic Genericity (Phases 4-7) -- COMPLETED 2026-03-21</summary>

- [x] Phase 4: Sequential Product Formalization (5/6 plans, 1 skipped) -- completed 2026-03-21
- [x] Phase 5: Local Tomography from B-M Compositionality (2/2 plans) -- completed 2026-03-21
- [x] Phase 6: Paper Assembly (3/3 plans) -- completed 2026-03-21
- [ ] Phase 7: D'Ariano Backup (contingency) -- not needed (S4 passed)

See `.gpd/milestones/v2.0-ROADMAP.md` for full details.

</details>

<details>
<summary>v3.0 GR Extension (Phases 8-12) -- COMPLETED 2026-03-22</summary>

- [x] Phase 8: Locality Formalization (3/3 plans) -- completed 2026-03-22
- [x] Phase 9: Area-Law Derivation (3/3 plans) -- completed 2026-03-22
- [x] Phase 10: Jacobson Application (3/3 plans) -- completed 2026-03-22
- [x] Phase 11: Numerical Verification (3/3 plans) -- completed 2026-03-22
- [x] Phase 12: Paper Assembly (3/3 plans) -- completed 2026-03-22

See `.gpd/milestones/v3.0-ROADMAP.md` for full details.

</details>

<details>
<summary>v4.0 Spectral Triple from Self-Modeling (Phases 13-15) -- CLOSED 2026-03-23 (medium success)</summary>

- [x] Phase 13: Order Zero + Representation Theory (3/3 plans) -- completed 2026-03-22
- [x] Phase 14: Dirac Operator Construction (2/2 plans) -- completed 2026-03-23
- [x] Phase 15: First-Order Condition + Algebra Identification (2/2 plans) -- completed 2026-03-23
- Phase 16: Remaining Axioms + Classification -- abandoned
- Phase 17: Paper 7 Assembly -- abandoned (superseded)

See `.gpd/milestones/v4.0-ROADMAP.md` for full details.

</details>

### v5.0 Chirality from h_3(O) via Cl(6) (Active)

**Milestone Goal:** Prove that the observer's C*-algebra nature forces complexification of h_3(O), upgrading Spin(9) to Spin(10), and that the octonion splitting O = C + C^3 induces a Cl(6) structure whose volume form selects the chiral (left) SM embedding. One complex structure choice simultaneously gives gauge group and chirality.

**Prior results carried forward:**
- Paper 5: Self-modeling forces M_n(C)^sa, C*-algebra, local tomography
- Paper 6: SWAP Hamiltonian, GR from Jacobson
- v4.0: Spectral triple established but simple M_n(C) cannot give SM (structural obstruction)
- h_3(O) is derived (non-composability argument, Gap A closed)
- F_4 subgroup intersection gives SM gauge group (Todorov-Drenska)

## Contract Overview

| Contract Item | Advanced By Phase(s) | Status |
| ------------- | -------------------- | ------ |
| Complexification proof (C*-nature forces V_1^C) | Phase 18 | Planned |
| F_4 -> E_6, Spin(9) -> Spin(10) upgrade | Phase 18 | Planned |
| Cl(6) construction from O = C + C^3 | Phase 19 | Planned |
| Chiral SM embedding via Pati-Salam breaking | Phase 19 | Planned |
| Furey Witt decomposition verification | Phase 19 | Planned |
| Explicit matrix verification of Cl(6) in Cl(10) | Phase 19 | Planned |
| SM quantum numbers from Cl(6) | Phase 19 | Planned |
| One choice -> gauge group + chirality synthesis | Phase 20 | Planned |
| Todorov-Drenska connection (same group, chiral rep) | Phase 20 | Planned |
| Paper 7 "Chirality from h_3(O)" | Phase 21 | Planned |

## Phase Details

### Phase 18: Complexification from C*-Observer (Part A)

**Goal:** The observer's C*-algebra nature is proved to force complexification of the Peirce V_1 = O^2, upgrading Spin(9) to Spin(10) and F_4 to E_6

**Depends on:** v4.0 results (structural obstruction motivates h_3(O) route); Paper 5 (C*-algebra, local tomography)

**Requirements:** CMPL-01, CMPL-02

**Contract Coverage:**
- Advances: Complexification proof, F_4 -> E_6 upgrade
- Deliverables: Derivation document with proof that C*-observer forces V_1^C; explicit Peirce decomposition tracking through complexification
- Anchor coverage: Paper 5 (C*-algebra, local tomography), Boyle 2020 (h_3^C(O) and E_6), Baez "The Octonions" Sec 4.3
- Forbidden proxies: Assuming complexification without deriving it from C*-nature; claiming Spin(10) without showing the representation-theoretic upgrade from Spin(9)

**Success Criteria** (what must be TRUE):

1. A proof exists that C*-algebra observer nature (complex type from Paper 5 local tomography) forces extension of scalars from R to C when the observer probes V_1 = O^2, turning it into a 16-dim complex space
2. The symmetry upgrade Spin(9) -> Spin(10) is established at the representation level: real spinor S_9 of Spin(9) becomes Weyl spinor of Spin(10) after complexification
3. At the h_3(O) level, F_4 -> E_6 is tracked explicitly through the Peirce decomposition, with the structure-preserving group of h_3^C(O) identified as E_6
4. The 27-dimensional representation decomposes under Spin(10) as 27 -> 1 + 10 + 16, consistent with Boyle 2020

**Plans:** 2 plans

Plans:
- [x] 18-01-PLAN.md -- Peirce decomposition, complexification proof, Spin(9) -> Spin(10)
- [x] 18-02-PLAN.md -- F_4 -> E_6 upgrade, 27 -> 1 + 10 + 16 decomposition, synthesis

**Backtracking trigger:** If complexification requires more structure than just "being a C*-algebra observer" (e.g., needs a specific embedding or additional data beyond the complex structure), document what additional input is needed and assess whether it is derivable from self-modeling.

---

### Phase 19: Cl(6) Chirality and SM Embedding (Part B)

**Goal:** The octonion splitting O = C + C^3 is shown to induce Cl(6) inside Cl(10), whose volume form selects the chiral (left) SM embedding via the Pati-Salam route, with all 16 SM quantum numbers verified computationally

**Depends on:** Phase 18 (complexification to Spin(10) Weyl spinor)

**Requirements:** CHIR-01, CHIR-02, CHIR-03, CHIR-04, COMP-01, COMP-02

**Contract Coverage:**
- Advances: Cl(6) construction, chiral SM embedding, Furey Witt verification, explicit matrix verification, SM quantum numbers
- Deliverables: Explicit Cl(6) gamma matrices inside Cl(10); volume form omega_6 eigenvalue computation; Pati-Salam breaking chain; Witt decomposition creation/annihilation operators; SymPy/NumPy verification code with all 16 states identified
- Anchor coverage: Todorov arXiv:2206.06912 (Cl(6) in Cl(10), omega_6 projector), Furey arXiv:1806.00612 (automatic chirality from Witt decomposition), Baez n-Category Cafe Part 13 (Sawin's theorem, left vs diagonal), Krasnov arXiv:2504.16465 (pure spinors, complex structures on O^2)
- Forbidden proxies: Using Cl(6) without deriving it from O splitting; claiming chirality without distinguishing L from diagonal embedding; matching quantum numbers without explicit matrix verification

**Success Criteria** (what must be TRUE):

1. Six internal gamma matrices gamma_1...gamma_6 are constructed explicitly from the imaginary part of C^3 (orthogonal to u in Im(O)), satisfying Clifford relations {gamma_i, gamma_j} = 2 delta_ij inside Cl(10)
2. The volume form omega_6 = gamma_1...gamma_6 satisfies omega_6^2 = -1, and the projector P = (1/2)(1 - i*omega_6) has trace 16 on the 32-dim Dirac spinor, selecting one Weyl representation of Spin(10)
3. The Pati-Salam group SU(4) x SU(2)_L x SU(2)_R is identified as the stabilizer of omega_6 in Spin(10), and the further breaking SU(4) -> SU(3) x U(1) (from the same complex structure) gives the SM gauge group with LEFT embedding -- SU(2)_L acts on left-handed fermions only
4. Furey's Witt decomposition result is verified: creation/annihilation operators a_i = (1/2)(-e_{i+4} + i*e_i) automatically channel SU(2) to a single chirality without ad hoc projectors
5. All 16 SM quantum numbers (Y, I_3, color) for one generation are reproduced correctly from the Cl(6) Witt decomposition, verified by explicit matrix computation

**Plans:** 2 plans

Plans:
- [x] 19-01-PLAN.md -- Cl(6) from O = C + C^3, volume form, Pati-Salam breaking, Furey Witt decomposition (CHIR-01, CHIR-02, CHIR-03, CHIR-04)
- [x] 19-02-PLAN.md -- Explicit 32x32 matrix verification, all 16 SM quantum numbers (COMP-01, COMP-02)

**Backtracking trigger:** If the Cl(6) volume form does not cleanly select the LEFT embedding (e.g., if additional discrete choices beyond the complex structure are needed to break L/R symmetry), document what extra input is required. Partial success (chirality reduced to a single discrete orientation choice) is still valuable.

---

### Phase 20: Synthesis -- One Choice, Two Consequences

**Goal:** The single complex structure choice (embedding C in O) is proved to simultaneously give the SM gauge group (via F_4 subgroup intersection) and chirality (via Cl(6) volume form), unifying Parts A and B

**Depends on:** Phase 18 (complexification), Phase 19 (Cl(6) chirality)

**Requirements:** SYNT-01, SYNT-02

**Contract Coverage:**
- Advances: One choice -> two consequences synthesis; Todorov-Drenska connection with chiral representation
- Deliverables: Synthesis derivation showing single complex structure choice implies both gauge group and chirality; explicit comparison between Cl(6)/Pati-Salam route (with chirality) and F_4 intersection route (without chirality)
- Anchor coverage: Todorov-Drenska (F_4 intersection), Furey (Witt chirality), Boyle (E_6 complexification)
- Forbidden proxies: Treating gauge group and chirality as independent results; presenting synthesis without tracing both consequences to the same algebraic choice

**Success Criteria** (what must be TRUE):

1. A single algebraic choice (embedding C in O, equivalently choosing a unit imaginary octonion u) is shown to simultaneously: (a) break F_4 to [SU(3) x SU(3)]/Z_3 whose intersection with Spin(9) gives the SM gauge group, and (b) induce Cl(6) inside Cl(10) whose volume form selects the chiral (left) embedding
2. The SM gauge group obtained via the Cl(6)/Pati-Salam route (with chirality) is explicitly identified with the F_4 subgroup intersection of Todorov-Drenska (without chirality) -- same group, now carrying the correct chiral representation
3. The logical chain from self-modeling to chirality is complete: self-modeling -> Jordan algebra (Paper 5) -> h_3(O) (non-composability) -> C*-observer forces complexification (Part A) -> O = C + C^3 gives Cl(6) chirality (Part B) -> SM with left embedding

**Plans:** 2 plans

Plans:
- [x] 20-01-PLAN.md -- Todorov-Drenska F_4 intersection route, two-routes identification, chiral upgrade (SYNT-01, SYNT-02)
- [x] 20-02-PLAN.md -- Complete logical chain from self-modeling to chirality, synthesis theorem, gap register

**Backtracking trigger:** If the two routes (F_4 intersection and Cl(6)/Pati-Salam) give the same group but the identification requires non-trivial conjugation or the chiral representation does not match, document the precise discrepancy.

---

### Phase 21: Paper 7 Assembly

**Goal:** Paper 7 "Chirality from h_3(O)" is assembled with complete derivation chain from self-modeling through chirality, honest gap identification, and connection to Papers 5-6

**Depends on:** Phase 18, Phase 19, Phase 20 (all derivation phases)

**Requirements:** PAPR-01

**Contract Coverage:**
- Advances: Paper 7 deliverable
- Deliverables: Complete manuscript with sections covering: motivation from v4.0 obstruction, complexification argument (Part A), Cl(6) chirality construction (Part B), synthesis, gap identification, connection to Papers 5-6
- Anchor coverage: Papers 5-6 (cited as prior results), all Part A/B references (Todorov, Furey, Boyle, Krasnov, Baez-Sawin), Connes/CCM (spectral triple context)
- Forbidden proxies: Overclaiming (presenting partial results as complete derivation); glossing over gaps; claiming SM derivation without flagging remaining assumptions (Gap B step 1, generation structure)

**Success Criteria** (what must be TRUE):

1. The paper presents the complete chain: self-modeling -> M_n(C)^sa (Paper 5) -> h_3(O) (non-composability) -> complexification (Part A) -> Cl(6) chirality (Part B) -> SM with left embedding, with each link clearly stated as theorem, established result, or gap
2. Gaps are honestly identified: Gap B step 1 (rank-1 idempotent choice / symmetry breaking), generation structure (why 3 families), spectral action computation (deferred)
3. The v4.0 obstruction (simple M_n(C) cannot give SM) is presented as motivation for the h_3(O) route, connecting this paper to the research arc
4. All anchor references are cited and the relationship to Todorov-Drenska, Furey, and Boyle is made explicit

**Plans:** 3 plans

Plans:
- [ ] 21-01-PLAN.md -- Paper skeleton, preamble, bibliography, introduction with chain table
- [ ] 21-02-PLAN.md -- Technical body: Part A (complexification), Part B (chirality), Synthesis
- [ ] 21-03-PLAN.md -- Gap analysis, discussion, final assembly and verification

## Phase Dependencies

| Phase | Depends On | Enables | Critical Path? |
|-------|-----------|---------|:-:|
| 18 - Complexification | v4.0 results, Paper 5 | 19, 20 | Yes |
| 19 - Cl(6) Chirality | 18 | 20 | Yes |
| 20 - Synthesis | 18, 19 | 21 | Yes |
| 21 - Paper Assembly | 18, 19, 20 | -- | Yes |

**Critical path:** 18 -> 19 -> 20 -> 21 (4 phases, strictly sequential)

## Risk Register

| Phase | Top Risk | Probability | Impact | Mitigation |
|-------|---------|:-:|:-:|-----------|
| 18 | Complexification needs more than C*-nature | MEDIUM | HIGH | Document what extra structure is needed; assess if derivable from self-modeling |
| 19 | Cl(6) volume form does not cleanly select LEFT | LOW | HIGH | Partial success: chirality reduced to single discrete choice still publishable |
| 20 | F_4 intersection and Cl(6)/PS routes give same group but non-trivially conjugate | LOW | MEDIUM | Explicit computation resolves; conjugation documented as additional datum |
| 21 | Gaps too large for honest paper | LOW | MEDIUM | Paper honestly scopes as "chirality from h_3(O) conditional on Gap B step 1" |

## Progress

| Phase | Plans Complete | Status | Completed |
| ----- | -------------- | ------ | --------- |
| 18. Complexification (Part A) | 2/2 | Complete | 2026-03-23 |
| 19. Cl(6) Chirality (Part B) | 2/2 | Complete | 2026-03-23 |
| 20. Synthesis | 2/2 | Complete | 2026-03-23 |
| 21. Paper Assembly | 0/TBD | Not started | - |
