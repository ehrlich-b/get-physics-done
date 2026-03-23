# Roadmap: Experiential Measure on Structure Space

## Milestones

- **v1.0 Experiential Measure Formalization** -- Phases 1-3 (completed 2026-03-16)
- **v2.0 QM from Algebraic Genericity** -- Phases 4-7 (completed 2026-03-21)
- **v3.0 GR Extension** -- Phases 8-12 (completed 2026-03-22)
- **v4.0 Spectral Triple from Self-Modeling** -- Phases 13-17 (active)

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

### Active: v4.0 Spectral Triple from Self-Modeling

**Milestone Goal:** Determine whether the doubled self-modeling composite (H, J, gamma) satisfies the axioms of a real spectral triple of KO-dimension 6, construct the Dirac operator D, identify the subalgebra A_F forced by the first-order condition, and assemble as Paper 7 with honest gap identification.

## Contract Overview

| Contract Item | Type | Advanced By Phase(s) | Status |
| ------------- | ---- | -------------------- | ------ |
| claim-axioms (spectral triple axioms verified) | claim | Phase 13, Phase 16 | Planned |
| claim-dirac (Dirac operator from self-modeling) | claim | Phase 14 | Planned |
| claim-first-order (subalgebra from first-order condition) | claim | Phase 15 | Planned |
| claim-paper-7 (Paper 7 assembly) | claim | Phase 17 | Planned |
| ref-connes1995 (Connes 1995, J. Math. Phys. 36, 6194) | anchor | Phase 13, Phase 16, Phase 17 | Planned |
| ref-chamseddine-connes2008 (CCM 2008, arXiv:0706.3688) | anchor | Phase 13, Phase 15, Phase 17 | Planned |
| ref-van-suijlekom2024 (van Suijlekom 2024, textbook) | anchor | Phase 13, Phase 14, Phase 16 | Planned |
| ref-paper5 (Paper 5, M_n(C)^sa, J = dagger, SP) | anchor | Phase 13, Phase 14, Phase 17 | Planned |
| ref-paper6 (Paper 6, SWAP, Schur-Weyl) | anchor | Phase 13, Phase 14, Phase 17 | Planned |
| False progress: assuming KO-dim 6 without verifying all sign relations | forbidden proxy | Phase 13 | Active |
| False progress: claiming SM gauge group without checking first-order condition | forbidden proxy | Phase 15 | Active |
| False progress: using ad hoc D without deriving from self-modeling | forbidden proxy | Phase 14 | Active |
| False progress: checking order zero only for specific a,b instead of all | forbidden proxy | Phase 13 | Active |

## Phase Summary

- [x] **Phase 13: Order Zero + Representation Theory** (3/3 plans) -- completed 2026-03-22
- [x] **Phase 14: Dirac Operator Construction** (2/2 plans) -- completed 2026-03-23
- [ ] **Phase 15: First-Order Condition + Algebra Identification** -- Compute [[D,a], Jb*J^{-1}], identify maximal subalgebra A_F, evaluate at n=2,3,4 vs C + H + M_3(C)
- [ ] **Phase 16: Remaining Axioms + Classification** -- Verify Poincare duality, document orientability failure, check CCM classification hypotheses
- [ ] **Phase 17: Paper 7 Assembly** -- Paper 7 "Spectral Triple from Self-Modeling" with complete chain and tiered success statement

## Phase Details

### Phase 13: Order Zero + Representation Theory

**Goal:** The order zero condition [pi(a), Jb*J^{-1}] = 0 is verified for the self-modeling doubled Hilbert space at general n, the bimodule decomposition of H is computed, and the dimension counting 2n^2 vs CCM k^2 is resolved.

**Depends on:** Paper 5 (M_n(C)^sa, J = dagger), Paper 6 (SWAP, doubled space) -- carried forward from v2.0/v3.0

**Requirements:** AXVM-01, AXVM-04, COMP-01

**Contract Coverage:**
- Advances: claim-axioms (order zero -- gatekeeper axiom)
- Deliverables: Proof that [pi(a), pi_o(b)] = 0 for all a, b in M_n(C) at general n; explicit computation of pi_o(b) = Jb*J^{-1}; bimodule decomposition of H into irreducible A-A^o bimodules; Krajewski diagram; resolution of 2n^2 vs k^2 dimension counting
- Anchor coverage: ref-connes1995 (order zero condition definition), ref-van-suijlekom2024 (Ch. 2-4, bimodule decomposition), ref-chamseddine-connes2008 (CCM k^2 counting), ref-paper5 (J = dagger, M_n(C)^sa), ref-paper6 (SWAP, doubled space)
- Forbidden proxies: Checking order zero only for specific a,b instead of all; claiming order zero holds without tracking J's sector-swap through the computation; assuming KO-dim 6 without verifying all sign relations simultaneously
- Stop/rethink condition: If order zero fails for ALL algebra actions (not just the naive one), pivot to find the correct action (do not abandon)

**Success Criteria** (what must be TRUE):

1. pi_o(b) = Jpi(b*)J^{-1} is computed explicitly as a matrix on H = C^{2n^2}, showing how J's sector-swap and SWAP operator transform the algebra action
2. [pi(a), pi_o(b)] = 0 is verified for ALL a, b in M_n(C) at general n (symbolic proof), with SymPy verification at n=2 (8x8 matrices) confirming the general result
3. The bimodule decomposition of H into irreducible A-A^o bimodules is computed, with multiplicities, and the Krajewski diagram is drawn
4. The dimension mismatch 2n^2 vs CCM k^2 per generation is resolved: either (a) explicit mapping showing how 2n^2 decomposes into generation structure, or (b) identification that the self-modeling triple differs from CCM in generation counting, with implications stated
5. If order zero fails for the naive pi(a) = a tensor 1 action, the failure mode is characterized and an alternative algebra action is identified or the obstruction is documented

**Plans:** 3 plans

Plans:
- [x] 13-01-PLAN.md -- Derive pi_o(b) at general n and prove order zero condition algebraically
- [x] 13-02-PLAN.md -- SymPy verification of order zero at n=2,3,4 with full basis test
- [x] 13-03-PLAN.md -- Bimodule decomposition, Krajewski diagram, dimension counting resolution

**Backtracking triggers:**
- If order zero fails for ALL reasonable algebra actions -> STOP per contract. Document what was tried and return to user.
- If pi_o(b) has unexpected form due to J's sector-swap -> re-examine J definition from Paper 5; verify J^2 = +1 still holds with the correct pi_o.

---

### Phase 14: Dirac Operator Construction

**Goal:** The moduli space of Dirac operators satisfying D* = D, D gamma = -gamma D, and JD = DJ is parameterized, and the sequential product asymmetry candidate is tested as a natural D from self-modeling structure.

**Depends on:** Phase 13 (bimodule decomposition constrains allowed D blocks)

**Requirements:** DIRC-01, DIRC-02, DIRC-03, COMP-02 (partial: D verification at n=2,3,4)

**Contract Coverage:**
- Advances: claim-dirac
- Deliverables: Complete parameterization of D moduli space (dimension count); sequential product asymmetry operator L_a - R_a tested against all three constraints; if sequential product candidate works, identification of which parameters it corresponds to; if it fails, identification of the most naturally motivated D from self-modeling structure
- Anchor coverage: ref-van-suijlekom2024 (D parameterization), Barrett 2015 (matrix geometries, general D form for M_n(C)), ref-paper5 (sequential product sp(a,b) = sqrt(a) b sqrt(a))
- Forbidden proxies: Constructing ad hoc D without self-modeling motivation; testing only specific D without parameterizing the full moduli space first (pitfall P4); assuming D exists without verifying the moduli space is non-empty
- User-stated observable: Whether D arises naturally from sequential product asymmetry

**Success Criteria** (what must be TRUE):

1. The D moduli space is fully parameterized: all self-adjoint operators on H = C^{2n^2} satisfying D gamma = -gamma D and JD = DJ are written in terms of free parameters, with the dimension of the moduli space computed at general n and verified at n=2,3,4
2. The moduli space is non-trivial (dimension > 0), confirming that at least one non-zero D exists; if the moduli space is empty or D=0 only, this is documented as a negative result
3. The sequential product asymmetry operator (L_a - R_a or natural contraction) is tested: either (a) it lies in the D moduli space, establishing D from self-modeling, or (b) the specific constraint it violates is identified (JD != DJ or D gamma != -gamma D)
4. If the sequential product candidate fails, the D in the moduli space most naturally motivated from self-modeling structure is identified with explicit rationale
5. SymPy verification at n=2 (8x8), n=3 (18x18), and n=4 (32x32) confirms the moduli space parameterization and tests the sequential product candidate

**Plans:** 2 plans

Plans:
- [x] 14-01-PLAN.md -- Parameterize D moduli space: block decomposition, J constraint, dimension formula, SymPy/NumPy verification at n=1,2,3,4
- [x] 14-02-PLAN.md -- Test sequential product candidates (commutator, SP operator, Barrett form) against moduli space; identify most natural D

**Backtracking triggers:**
- If the D moduli space is empty (no non-trivial D exists) -> reconsider gamma or J definitions; explore alternative SWAP/grading constructions from Paper 6.
- If the sequential product candidate violates JD = DJ -> investigate whether a modified J (still satisfying J^2 = +1, J gamma = -gamma J) admits the sequential product D.

---

### Phase 15: First-Order Condition + Algebra Identification

**Goal:** The maximal subalgebra A_F of M_n(C) satisfying the first-order condition [[D, a], Jb*J^{-1}] = 0 is identified, evaluated at n=2,3,4, and compared to the Standard Model algebra C + H + M_3(C).

**Depends on:** Phase 14 (specific D from moduli space)

**Requirements:** FRST-01, FRST-02, FRST-03, COMP-02 (partial: first-order verification at n=2,3,4)

**Contract Coverage:**
- Advances: claim-first-order
- Deliverables: Maximal subalgebra A_F identified as an abstract algebra with dimension and structure; explicit evaluation at n=2 (dim(A_F), structure), n=3, n=4; comparison to C + H + M_3(C); if A_F differs, characterization of the resulting gauge group
- Anchor coverage: ref-chamseddine-connes2008 (first-order condition -> C + H + M_3(C) in CCM setting), Chamseddine-Connes-van Suijlekom 2013 (Pati-Salam fallback), ref-van-suijlekom2024 (first-order condition as linear algebra)
- Forbidden proxies: Assuming A_F = C + H + M_3(C) without computing the first-order condition; claiming SM gauge group without checking all factors of the algebra; checking first-order condition for only some a,b
- User-stated observable: What algebra A_F the first-order condition forces; for which n (if any) A_F = C + H + M_3(C)

**Success Criteria** (what must be TRUE):

1. [[D, a], Jb*J^{-1}] is computed for general a, b in M_n(C), recast as a linear constraint Mv = 0 on the algebra elements, and the null space (= A_F) is determined
2. A_F is identified as an abstract *-algebra: its dimension, simple summands, and center are computed
3. At n=2, 3, 4: A_F is evaluated explicitly, with dim(A_F) and isomorphism type determined by SymPy null space computation
4. Comparison with C + H + M_3(C) (dim = 14, summands = C + H + M_3(C)) is made; if A_F matches, the gauge group U(1) x SU(2) x SU(3) is confirmed; if A_F differs, the actual gauge group is identified
5. If the first-order condition fails entirely (A_F = C only, or trivial), the Pati-Salam fallback (Chamseddine-Connes-van Suijlekom 2013) is evaluated

**Plans:** TBD

**Backtracking triggers:**
- If A_F is trivial (C only) for all D in the moduli space -> the first-order condition is too restrictive; investigate whether relaxing it (as in CCSV 2013) gives Pati-Salam.
- If A_F depends sensitively on which D is chosen from the moduli space -> document the D-dependence; identify whether self-modeling selects a preferred D.

---

### Phase 16: Remaining Axioms + Classification

**Goal:** All remaining spectral triple axioms are verified or their failure documented, the CCM classification hypotheses are assessed, and a complete axiom checklist is produced.

**Depends on:** Phase 13 (order zero), Phase 14 (D), Phase 15 (A_F)

**Requirements:** AXVM-02, AXVM-03, COMP-02 (partial: remaining axiom checks at n=3,4)

**Contract Coverage:**
- Advances: claim-axioms (completion)
- Deliverables: Orientability check with expected failure documented per Barrett 2007/Stephan 2006; Poincare duality (intersection form) computed; irreducibility, quaternion linearity, unimodularity, massivity conditions assessed; complete axiom checklist with pass/fail status for each
- Anchor coverage: ref-connes1995 (full axiom list), ref-van-suijlekom2024 (Poincare duality, orientability), Barrett 2007 (orientability failure precedent), Cacic 2009 (Poincare duality for finite triples)
- Forbidden proxies: Claiming "spectral triple established" without checking all non-trivial axioms; ignoring CCM classification hypotheses (irreducibility, quaternion linearity, unimodularity) when comparing to SM

**Success Criteria** (what must be TRUE):

1. Orientability (existence of Hochschild cycle c with gamma = pi(c)Jpi(c')J^{-1}) is checked; expected failure documented with precedent citations (Barrett 2007, Stephan 2006) showing this is standard for KO-dim 6 finite triples
2. Poincare duality (non-degeneracy of the intersection form on K-theory) is computed for the candidate spectral triple; pass or fail with explicit calculation
3. CCM classification hypotheses assessed: (a) irreducibility -- does A act irreducibly on each summand? (b) quaternion linearity -- does A contain a quaternion subalgebra acting on the appropriate sector? (c) unimodularity -- does det(u) = 1 for the gauge group? (d) massivity -- is D generically non-degenerate?
4. Complete axiom checklist produced with status for each axiom: order zero (Phase 13), KO-dim 6 signs (verified in preliminary work), Dirac operator (Phase 14), first-order condition (Phase 15), orientability, Poincare duality, CCM hypotheses
5. An honest assessment of which axioms hold, which fail (with severity: fatal vs expected/non-fatal), and what the overall status of the spectral triple is

**Plans:** TBD

**Backtracking triggers:**
- If Poincare duality fails -> investigate whether modification of the construction can restore it; this would be a more serious failure than orientability.
- If CCM hypotheses fail -> the classification theorem does not directly apply; document what weaker classification (if any) does apply.

---

### Phase 17: Paper 7 Assembly

**Goal:** Paper 7 "Spectral Triple from Self-Modeling" is assembled with the complete derivation chain, SymPy verification code, tiered success statement (strong/medium/informative failure), and honest gap identification.

**Depends on:** Phase 13, Phase 14, Phase 15, Phase 16 (all prior v4.0 phases)

**Requirements:** PAPR-01

**Contract Coverage:**
- Advances: claim-paper-7
- Deliverables: Paper 7 manuscript (LaTeX, publication-ready) with: introduction extending Papers 5-6 chain, spectral triple construction, axiom verification, Dirac operator derivation, first-order condition and subalgebra identification, classification assessment, discussion with gap identification, bibliography; SymPy verification code as supplementary material
- Anchor coverage: ref-connes1995 (cited), ref-chamseddine-connes2008 (cited), ref-van-suijlekom2024 (cited), ref-paper5 (cited as input), ref-paper6 (cited as input)
- Forbidden proxies: Overclaiming (SM "derived") when conditions assumed; glossing over axiom failures; pattern matching without algebraic proof
- User-stated deliverable: Paper 7, standalone, with tiered success statement

**Success Criteria** (what must be TRUE):

1. The paper presents the complete chain: self-modeling (Paper 5) -> SWAP structure (Paper 6) -> doubled Hilbert space + J + gamma -> order zero -> Dirac operator -> first-order condition -> A_F, with every step either proved or gap-identified
2. Tiered success statement is explicit: (a) STRONG: A_F = C + H + M_3(C) and all axioms hold (b) MEDIUM: non-trivial A_F with interesting gauge group but not SM (c) INFORMATIVE FAILURE: construction fails at specific axiom, failure mode characterized
3. SymPy verification code for all algebraic identities is included as supplementary material, with instructions for reproduction
4. Every gap and assumption is precisely identified; no hand-waving or elision
5. The paper is formatted for target venue (J. Math. Phys. or Commun. Math. Phys.) with complete bibliography citing all active anchors

**Plans:** TBD

**Backtracking triggers:**
- If assembling the chain reveals a logical gap not caught in Phases 13-16 -> return to the relevant phase.
- If adversarial review identifies circularity or overclaiming -> revise specific sections.

## Phase Dependencies

| Phase | Depends On | Enables | Critical Path? |
|-------|-----------|---------|:-:|
| 13 - Order Zero + Representation Theory | Papers 5-6 (v2.0/v3.0) | 14, 15, 16 | Yes |
| 14 - Dirac Operator Construction | 13 | 15, 16 | Yes |
| 15 - First-Order Condition + Algebra ID | 14 | 16, 17 | Yes |
| 16 - Remaining Axioms + Classification | 13, 14, 15 | 17 | No (parallel with 15 partially) |
| 17 - Paper 7 Assembly | 13, 14, 15, 16 | -- | Yes |

**Critical path:** 13 -> 14 -> 15 -> 17 (4 phases, minimum duration)
**Parallelizable:** Phase 16 (remaining axioms) can begin after Phase 14 completes for orientability/Poincare duality checks; first-order condition assessment requires Phase 15. In practice, Phase 16 is best done after Phase 15 since CCM hypothesis assessment needs A_F.

**Execution order:**

```
Wave 1: Phase 13 (sole entry point -- gatekeeper)
Wave 2: Phase 14 (requires Phase 13 bimodule structure)
Wave 3: Phase 15 (requires Phase 14 D)
Wave 4: Phase 16 (requires Phases 13-15 for complete assessment)
Wave 5: Phase 17 (requires all prior phases)
```

## Risk Register

| Phase | Top Risk | Probability | Impact | Mitigation |
|-------|---------|:-:|:-:|-----------|
| 13 | Order zero condition fails for naive algebra action | MEDIUM | HIGH | Standard tensor product argument suggests it should hold; if fails, search for modified action or subalgebra. Not fatal if alternative action found. |
| 13 | Dimension counting 2n^2 vs k^2 has no solution | MEDIUM | MEDIUM | May indicate self-modeling triple differs from CCM in generation structure. Document and proceed -- first-order condition is the real test. |
| 14 | D moduli space is empty or trivial (D=0 only) | LOW | FATAL | Reconsider gamma or J definitions. Explore alternative grading from Paper 6. |
| 14 | Sequential product asymmetry violates JD = DJ | MEDIUM | HIGH | Fall back to generic D from moduli space. Loss of "derived from self-modeling" narrative but spectral triple may still exist. |
| 15 | First-order condition gives trivial A_F (= C only) | MEDIUM | HIGH | Try all D in moduli space. If all give trivial A_F, relax first-order condition -> Pati-Salam (CCSV 2013). |
| 15 | A_F is non-trivial but not C + H + M_3(C) | MEDIUM | MEDIUM | Still publishable. Characterize actual gauge group. Pati-Salam is a viable outcome. |
| 16 | Poincare duality fails | LOW | MEDIUM | More serious than orientability. Investigate construction modifications. |
| 17 | Results are negative (no spectral triple) | LOW | LOW | Informative failure is still publishable if failure mode is characterized. Paper becomes "obstruction theorem." |

## Progress

**Execution Order:** 13 -> 14 -> 15 -> 16 -> 17

| Phase | Milestone | Plans Complete | Status | Completed |
| ----- | --------- | -------------- | ------ | --------- |
| 13. Order Zero + Representation Theory | v4.0 | 3/3 | Complete | 2026-03-22 |
| 14. Dirac Operator Construction | v4.0 | 2/2 | Complete | 2026-03-23 |
| 15. First-Order Condition + Algebra ID | v4.0 | 0/TBD | Not started | - |
| 16. Remaining Axioms + Classification | v4.0 | 0/TBD | Not started | - |
| 17. Paper 7 Assembly | v4.0 | 0/TBD | Not started | - |
