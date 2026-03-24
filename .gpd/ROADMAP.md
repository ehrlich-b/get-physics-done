# Roadmap: Experiential Measure on Structure Space

## Milestones

- **v1.0 Experiential Measure Formalization** -- Phases 1-3 (completed 2026-03-16)
- **v2.0 QM from Algebraic Genericity** -- Phases 4-7 (completed 2026-03-21)
- **v3.0 GR Extension** -- Phases 8-12 (completed 2026-03-22)
- **v4.0 Spectral Triple from Self-Modeling** -- Phases 13-15 (closed 2026-03-23, medium success)
- **v5.0 Chirality from h_3(O) via Cl(6)** -- Phases 18-21 (completed 2026-03-24)
- **v6.0 Gap C -- Complexification from C*-Measurement Maps** -- Phases 22-25 (active)

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
- [x] Phase 7: D'Ariano Backup (contingency) -- not needed (S4 passed)

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
- [x] Phase 16: Remaining Axioms + Classification -- abandoned
- [x] Phase 17: Paper 7 Assembly -- abandoned (superseded)

See `.gpd/milestones/v4.0-ROADMAP.md` for full details.

</details>

<details>
<summary>v5.0 Chirality from h_3(O) via Cl(6) (Phases 18-21) -- COMPLETED 2026-03-24</summary>

- [x] Phase 18: Complexification from C*-Observer (2/2 plans) -- completed 2026-03-23
- [x] Phase 19: Cl(6) Chirality and SM Embedding (2/2 plans) -- completed 2026-03-23
- [x] Phase 20: Synthesis -- One Choice, Two Consequences (2/2 plans) -- completed 2026-03-23
- [x] Phase 21: Paper 7 Assembly (3/3 plans) -- completed 2026-03-24

See `.gpd/milestones/v5.0-ROADMAP.md` for full details.

</details>

### v6.0 Gap C -- Complexification from C*-Measurement Maps (Phases 22-25)

**Milestone Goal:** Determine whether a C*-algebra observer probing V_{1/2} = O^2 inside h_3(O) necessarily induces complexification V -> V tensor_R C, closing Gap C in Paper 7.

## Contract Overview

| Contract Item | Advanced By Phase(s) | Status |
| --- | --- | --- |
| claim-complexification: C*-observer forces V tensor_R C | Phase 22 | Planned |
| claim-uniqueness: complexification is unique/canonical | Phase 23 | Planned |
| claim-jordan-distinction: Jordan setting forces complexification | Phase 24 | Planned |
| claim-theorem: single theorem closing Gap C | Phase 25 | Planned |
| ref-effros-stormer1979: conditional expectations | Phase 22 | Planned |
| ref-alfsen-shultz2001: Peirce decomposition, state spaces | Phase 22, 23, 24 | Planned |
| ref-baez2002: h_3(O) structure | Phase 22, 24 | Planned |
| ref-upmeier1987: Jordan-C* connections | Phase 22 | Planned |
| ref-hanche-olsen1983: JC-algebra tensor products | Phase 22 | Planned |
| ref-paper5: C*-observer (M_n(C)^sa) | Phase 22, 25 | Planned |
| ref-paper7: chirality chain with Gap C | Phase 25 | Planned |

## Phase Dependencies

| Phase | Depends On | Enables | Critical Path? |
| --- | --- | --- | --- |
| 22 - Measurement Maps | -- | 23, 24, 25 | Yes |
| 23 - Uniqueness | 22 | 25 | Yes |
| 24 - Observable Algebra | 22 | 25 | No (partial overlap with 23) |
| 25 - Formalization | 22, 23, 24 | -- | Yes |

**Critical path:** 22 -> 23 -> 25 (3 phases, minimum duration)
**Parallelizable:** Phase 24 runs concurrently with Phase 23

## Phase Details

### Phase 22: Measurement Maps -- Four Routes to Complexification

**Goal:** Determine whether C*-observer measurement maps on V_{1/2} = O^2 force complexification, via four independent algebraic routes
**Depends on:** Nothing (v6.0 entry point; takes v5.0 Peirce decomposition as input)
**Requirements:** MEAS-01, MEAS-02, MEAS-03, MEAS-04
**Contract Coverage:**
- Advances: claim-complexification
- Deliverables: theorem or counterexample per route (4 deliverables)
- Anchor coverage: ref-effros-stormer1979 (Route 1), ref-alfsen-shultz2001 (Routes 1-2), ref-upmeier1987 (Route 3), ref-hanche-olsen1983 (Route 4), ref-baez2002 (all routes -- h_3(O) structure)
- Forbidden proxies: proving complexification for a different algebra than h_3(O); proving for abstract real spaces without using Peirce/Jordan structure; assuming Spin(10) instead of deriving it from complexification
**Success Criteria** (what must be TRUE):
1. Each of the 4 routes (conditional expectation, state-effect duality, GNS, tensor product) produces either a proof that C*-measurement maps on V_{1/2} factor through V tensor_R C, or an explicit counterexample showing they need not
2. At least one route succeeds (proof of complexification) OR all four produce counterexamples (complexification not forced, triggering failure strategy)
3. For each successful route, the complex structure on V_{1/2} is exhibited explicitly (not just existence)
4. Every proof uses the specific Peirce decomposition h_3(O) = V_1 + V_{1/2} + V_0 under E_{11}, not generic algebra structure
5. All algebraic identities verified against Alfsen-Shultz / Baez reference formulas

**Backtracking trigger:** If all 4 routes produce counterexamples, pivot to failure strategy: characterize minimal additional assumption needed (FORM-02 activated early)

**Plans:** 4 plans (one per route, parallelizable)

Plans:
- [x] 22-01: Route 1 -- Conditional expectations (Effros-Stormer) -- NEGATIVE
- [x] 22-02: Route 2 -- State-effect duality -- NEGATIVE
- [x] 22-03: Route 3 -- GNS construction -- NEGATIVE (3 obstructions)
- [x] 22-04: Route 4 -- Tensor product (Hanche-Olsen) -- WEAK POSITIVE (generic tautology)

### Phase 23: Uniqueness and Spin(10) Compatibility

**Goal:** The complexification from Phase 22 is proved unique and canonical, with Spin(10) extension verified
**Depends on:** Phase 22 (requires at least one successful route)
**Requirements:** UNIQ-01, UNIQ-02, UNIQ-03
**Contract Coverage:**
- Advances: claim-uniqueness
- Deliverables: uniqueness proof, Spin(10) branching verification, Jordan compatibility check
- Anchor coverage: ref-alfsen-shultz2001 (Peirce theory), Boyle 2020 (Spin(10) branching cross-check), v5.0 Phase 18 (branching rule S_{10}^+|_{Spin(9)} = S_9^C)
- Forbidden proxies: uniqueness for wrong module; uniqueness that depends on route choice (must be route-independent)
**Success Criteria** (what must be TRUE):
1. Complexification of V_{1/2} is unique up to canonical isomorphism -- no choices beyond the C*-nature of the observer (Schur's lemma level argument)
2. The Spin(10) action on V_{1/2}^C extends the Spin(9) action on V_{1/2}, with multiplicity-free branching S_{10}^+|_{Spin(9)} = S_9^C confirmed
3. Peirce decomposition of h_3(O)^C gives 27 = 1 + 10 + 16 under Spin(10) subset E_6, with each summand identified as a complexified Peirce subspace
4. If multiple Phase 22 routes succeeded, the resulting complex structures are shown to be the same (route independence)

**Backtracking trigger:** If uniqueness fails (multiple inequivalent complexifications exist), determine whether Spin(10) selects a preferred one; if not, Gap C remains open with the choice as the remaining gap.

**Plans:** 3 plans

Plans:
- [ ] 23-01: Uniqueness proof (Schur's lemma / irreducibility argument)
- [ ] 23-02: Spin(10) extension and branching verification
- [ ] 23-03: Jordan compatibility -- 27 = 1 + 10 + 16 decomposition check

### Phase 24: Observable Algebra -- Why Jordan Forces Complexification

**Goal:** Identify precisely why the Jordan-algebraic setting (Peirce interface, L_{E_{11}} action) forces complexification when generic real spaces probed by C*-systems do not
**Depends on:** Phase 22 (needs at least one successful route to analyze)
**Requirements:** JORD-01, JORD-02
**Contract Coverage:**
- Advances: claim-jordan-distinction
- Deliverables: precise identification of the Jordan-specific mechanism, explicit counterexample for non-Jordan case, V_1 C*-upgrade analysis
- Anchor coverage: ref-baez2002 (h_3(O) structure), ref-alfsen-shultz2001 (Peirce multiplication rules), v5.0 Phase 18 (Peirce decomposition)
- Forbidden proxies: vague "Jordan is special" without precise mechanism; claiming Jordan forces complexification without constructing a non-Jordan counterexample
**Success Criteria** (what must be TRUE):
1. An explicit example of a C*-algebra acting on a real vector space via positive unital maps that does NOT induce complexification (non-Jordan counterexample)
2. The precise algebraic property of the Peirce interface (V_1 . V_{1/2} subset V_{1/2}) that forces complexification is identified and stated as a lemma
3. The V_1 C*-upgrade mechanism is analyzed: if observer forces V_1 from R to C (Peirce 1-eigenspace), whether Peirce rules propagate this to V_{1/2} becoming a C-module
4. The argument distinguishes h_3(O) from cases where complexification is a choice rather than forced

**Backtracking trigger:** If JORD-02 shows Peirce rules do NOT propagate V_1 complexification to V_{1/2}, the "Jordan forces complexification" claim weakens to "Jordan + additional structure forces complexification" -- feed into Phase 25 gap characterization.

**Plans:** 2 plans

Plans:
- [ ] 24-01: Jordan distinction -- mechanism identification and non-Jordan counterexample
- [ ] 24-02: V_1 C*-upgrade through Peirce multiplication rules

### Phase 25: Formalization -- Gap C Closure Theorem

**Goal:** State Gap C closure as a single theorem with complete proof, or precisely characterize the minimal additional assumption needed
**Depends on:** Phase 22 (routes), Phase 23 (uniqueness), Phase 24 (Jordan mechanism)
**Requirements:** FORM-01, FORM-02
**Contract Coverage:**
- Advances: claim-theorem
- Deliverables: formal theorem statement with proof (or precise gap characterization), updated Paper 7 complexification section
- Anchor coverage: ref-paper5 (C*-observer), ref-paper7 (Gap C target, Link 4), all Phase 22-24 results
- Forbidden proxies: theorem with hidden assumptions; proving complexification without addressing the reviewer's sub-gap (a); theorem for a different algebra than h_3(O)
- Stop condition: if Phase 22 produced all counterexamples AND Phase 24 found no Jordan-specific mechanism, FORM-02 becomes the sole deliverable
**Success Criteria** (what must be TRUE):
1. If complexification is forced: a single theorem statement of the form "If V_1 carries a C*-algebra structure (from self-modeling), then V_{1/2} carries a canonical complex structure, Spin(9) extends uniquely to Spin(10), and F_4 upgrades to E_6" -- with complete proof referencing Phase 22-24 results
2. If complexification is NOT forced: precise characterization of the minimal additional assumption, stated as "Gap C reduces to [assumption X]" with X strictly weaker than the current Paper 7 argument
3. All hypotheses of the theorem are stated explicitly (no hidden assumptions beyond Paper 5's C*-observer and h_3(O)'s Peirce decomposition)
4. The theorem (or gap characterization) is directly insertable into Paper 7 Section 3 as an upgrade to the current Link 4 argument
5. Every logical step in the proof is independently verifiable (no "it can be shown" or "straightforward calculation")

**Backtracking trigger:** If synthesis reveals logical gaps between Phase 22-24 results that cannot be bridged, return to the specific phase with the gap.

**Plans:** 2 plans

Plans:
- [ ] 25-01: Theorem statement and proof assembly (or gap characterization)
- [ ] 25-02: Paper 7 section update

## Risk Register

| Phase | Top Risk | Probability | Impact | Mitigation |
| --- | --- | --- | --- | --- |
| 22 | All 4 routes produce counterexamples | LOW | HIGH | Pivot to FORM-02: characterize minimal additional assumption; Paper 7 keeps honest gap |
| 22 | Routes succeed but only for h_3(O), not via general Jordan argument | MEDIUM | LOW | Acceptable -- h_3(O)-specific proof still closes Gap C |
| 23 | Multiple inequivalent complexifications exist | LOW | MEDIUM | Check if Spin(10) selects preferred one; if not, additional input needed |
| 24 | Peirce rules do not propagate V_1 upgrade to V_{1/2} | MEDIUM | MEDIUM | Gap C becomes "C* + [specific Peirce property]" -- still progress over current Paper 7 |
| 25 | Phase 22-24 results don't synthesize into clean theorem | LOW | MEDIUM | State as conjunction of lemmas rather than single theorem; still closes Gap C |

## Progress

**Execution Order:** 22 -> 23 (+ 24 parallel) -> 25

| Phase | Plans Complete | Status | Completed |
| --- | --- | --- | --- |
| 22. Measurement Maps | 4/4 | Complete | 2026-03-24 |
| 23. Uniqueness | 0/3 | Not started | - |
| 24. Observable Algebra | 0/2 | Not started | - |
| 25. Formalization | 0/2 | Not started | - |

