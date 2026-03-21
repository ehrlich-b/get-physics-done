# Roadmap: Experiential Measure on Structure Space -- Formalization

## Milestones

- **v1.0 Experiential Measure Formalization** -- Phases 1-3 (completed 2026-03-16)
- **v2.0 QM from Algebraic Genericity** -- Phases 4-7 (active)

## Phases

<details>
<summary>v1.0 Experiential Measure Formalization (Phases 1-3) -- COMPLETED 2026-03-16</summary>

- [x] Phase 1: Theorem A Assembly (2/2 plans) -- completed 2026-03-16
- [x] Phase 2: Lipschitz Stability (2/2 plans) -- completed 2026-03-16
- [x] Phase 3: Born-Fisher Test (2/2 plans) -- completed 2026-03-16

See `.gpd/milestones/v1.0-ROADMAP.md` for full details.

</details>

### Active: v2.0 QM from Algebraic Genericity

**Milestone Goal:** Derive the C*-algebra involution from the sequential product structure of self-modeling systems, closing the last gap in the L4 -> QM chain.

## Contract Overview

| Contract Item | Type | Advanced By Phase(s) | Status |
| ------------- | ---- | -------------------- | ------ |
| claim-sp-axioms (S1-S7 verification) | claim | Phase 4 | Planned |
| claim-local-tomo (B-M -> local tomography) | claim | Phase 5 | Planned |
| claim-paper-5 (Paper 5 assembly) | claim | Phase 6 | Planned |
| ref-vdw2018 (van de Wetering 2018) | anchor | Phase 4, 5 | Planned |
| ref-gudder-greechie (Gudder-Greechie 2002) | anchor | Phase 4 | Planned |
| ref-barnum2023 (Barnum-Ududec-van de Wetering 2023) | anchor | Phase 5 | Planned |
| ref-dariano2006 (D'Ariano 2006) | anchor | Phase 7 (contingency) | Planned |
| ref-barandes (Barandes 2025) | anchor | Phase 6 | Planned |
| ref-motzkin-taussky (Motzkin-Taussky 1955) | anchor | Phase 6 | Planned |
| False progress: sketch without formal verification | forbidden proxy | Phase 4 | Active |
| False progress: Hilbert space circular imports | forbidden proxy | Phase 4 | Active |

## Phase Summary

- [x] **Phase 4: Sequential Product Formalization** -- All S1-S7 proved; EJA classification via vdW Theorem 1 (completed 2026-03-21)
- [ ] **Phase 5: Local Tomography from B-M Compositionality** -- Prove B-M independent accessibility implies local tomography, promoting Jordan -> C*
- [ ] **Phase 6: Paper Assembly** -- Assemble Paper 5 (full chain or conditional, adapting to Phase 4-5 outcomes)
- [ ] **Phase 7: D'Ariano Backup** -- (CONTINGENCY) Construct involution from faithful B-M correlation state if S4 fails

## Phase Details

### Phase 4: Sequential Product Formalization

**Goal:** The self-modeling sequential product is formally defined on a finite-dimensional order unit space, all seven van de Wetering axioms are individually verified or refuted, and the resulting algebraic structure is classified.

**Depends on:** Nothing (entry point for v2.0; builds on v1.0 composite process framework)

**Requirements:** SPFM-01, SPFM-02, SPFM-03, SPFM-04, SPFM-05

**Contract Coverage:**
- Advances: claim-sp-axioms
- Deliverables: Formal definition of the self-modeling sequential product with effect algebra framing resolved; proof/disproof of each axiom S1-S7; non-associativity verification; EJA classification (if S1-S7 hold)
- Anchor coverage: ref-vdw2018 (Theorems 1, 3 -- axiom definitions and EJA result), ref-gudder-greechie (original sequential product formalism)
- Forbidden proxies: Sketch arguing axioms "should hold" without formal proofs; proofs that use Hilbert space structure (circular); checking axioms for quantum sequential products instead of the self-modeling construction; associativity claim without explicit test
- Prior inputs: v1.0 composite process framework, ~/repos/blog/research/quantum-extension/draft.md

**Success Criteria** (what must be TRUE when this phase completes):

1. The self-modeling sequential product is formally written as a bilinear map on the effect space of a finite-dimensional order unit space, using ONLY order unit space primitives and the self-modeling constraint (no Hilbert space imports -- circularity audit passed)
2. The correct effect algebra framing (E(B) vs E(B x M)) is determined and justified, with the rejected framing's failure mode documented
3. Axiom S4 (symmetry of orthogonality) is either proved with a complete formal argument or disproved with an explicit counterexample (a,b such that a.b = 0 but b.a != 0)
4. All remaining axioms S1-S3 and S5-S7 are individually verified with proofs pinned to arXiv:1803.11139 definitions exclusively (not Gudder-Greechie axioms)
5. Non-associativity is confirmed by exhibiting an explicit triple (a,b,c) with (a.b).c != a.(b.c), ruling out the commutativity trap (Westerbaan-Westerbaan-van de Wetering 2020)

**Plans:** 6 plans

Plans:
- [x] 04-01-PLAN.md -- Define compression-based sequential product, resolve E(B) vs E(B x M) framing
- [x] 04-06-PLAN.md -- (GAP CLOSURE) Peirce 1-space feedback extension: corrected product with phi essential
- [x] 04-02-PLAN.md -- Non-associativity confirmed (kill gate passed)
- [x] 04-03-PLAN.md -- S1-S3, S5-S7 all proved
- [x] 04-04-PLAN.md -- S4 proved (phi-independent, facial orthogonality), EJA classification
- [x] 04-05-PLAN.md -- SKIPPED (S4 passed, no failure to characterize)

**Backtracking triggers:**
- If the circularity audit reveals Hilbert space imports in the update map definition -> STOP, redesign the update map from order unit space primitives only
- If non-associativity check fails (product is associative) -> the algebra is commutative (classical), the sequential product route is dead; escalate to user
- If S4 fails -> Phase 4 is still complete (SPFM-05 characterizes the failure); trigger Phase 7 (D'Ariano backup) before Phase 5

**Internal ordering within phase:**
1. SPFM-01 first (formal definition, both framings)
2. SPFM-04 early (non-associativity sanity check -- kills the program if it fails)
3. SPFM-02 next (S1-S3, S5-S7 -- the "free" axioms)
4. SPFM-03 last (S4 -- the hard one, the decisive gate)
5. SPFM-05 only if S4 fails (characterize failure)

---

### Phase 5: Local Tomography from B-M Compositionality

**Goal:** The gap between B-M independent accessibility and local tomography is formally bridged, and the Jordan algebra from Phase 4 is promoted to a C*-algebra via Hanche-Olsen's theorem.

**Depends on:** Phase 4 (EJA structure must be established; S1-S7 must hold)

**Requirements:** LTOM-01, LTOM-02, LTOM-03

**Contract Coverage:**
- Advances: claim-local-tomo
- Deliverables: Formal definition of independent accessibility in the order unit space / GPT framework; proof or disproof that independent accessibility implies local tomography; C*-algebra identification (if local tomography holds)
- Anchor coverage: ref-barnum2023 (compositionality constraints on Jordan algebras), ref-vdw2018 (Theorem 3 -- EJA + local tomography -> C*-algebra), Hanche-Olsen (1985), Barnum-Wilce (arXiv:1202.4513)
- Forbidden proxies: Assuming complex field without proof; conflating independent accessibility with local tomography; hand-waving the Albert algebra exclusion

**Success Criteria** (what must be TRUE when this phase completes):

1. "Independently accessible B and M" is formalized in the GPT / order unit space framework with a precise mathematical definition compatible with Barnum-Wilce
2. Either local tomography is proved from B-M independent accessibility (with the argument explicitly addressing entangled-sector states), or the gap is identified and the minimal additional assumption stated
3. The non-complex EJA types (real M_n(R)_sa, quaternionic M_n(H)_sa, spin factors V_n for n >= 4, Albert algebra M_3(O)_sa) are each explicitly excluded by the compositionality / local tomography constraint
4. If local tomography holds: the C*-algebra structure is identified via Hanche-Olsen, and the involution is exhibited as an explicit operation on the algebra

**Plans:** 2 plans

Plans:
- [ ] 05-01-PLAN.md -- Formalize B-M composite OUS with product-form SP; prove faithful tracking implies local tomography
- [ ] 05-02-PLAN.md -- Exclude non-complex EJA types; C*-algebra promotion via vdW Thm 3 + Barnum-Wilce + Hanche-Olsen; exhibit involution

**Backtracking triggers:**
- If the EJA from Phase 4 is a spin factor or the Albert algebra -> local tomography fails for structural reasons; reclassify Phase 4 result
- If the self-modeling framework does not admit a qubit-like 2-dimensional subsystem -> Barnum-Wilce cannot be applied; need alternative route
- If local tomography fails entirely -> Phase 6 adapts to conditional paper (L4 + C*)

---

### Phase 6: Paper Assembly

**Goal:** Paper 5 is assembled as a complete, self-contained, publication-ready manuscript presenting either the full chain (L4 -> QM with one premise) or the conditional chain (L4 + C* -> QM with two premises).

**Depends on:** Phase 4 (S1-S7 results), Phase 5 (local tomography result or failure characterization)

**Requirements:** PAPR-01

**Contract Coverage:**
- Advances: claim-paper-5
- Deliverables: Paper 5 manuscript (LaTeX, publication-ready)
- Anchor coverage: All v2.0 anchors cited (ref-vdw2018, ref-gudder-greechie, ref-barnum2023, ref-barandes, ref-motzkin-taussky, ref-dariano2006 if backup used); v1.0 papers cited
- Forbidden proxies: Paper that assumes C* without acknowledging it as an additional premise; overclaiming scope (v1.0 lesson); paper without self-contained logical chain

**Success Criteria** (what must be TRUE when this phase completes):

1. The paper presents a complete, self-contained logical chain from premise(s) to QM, with every step either a published theorem (cited) or a result proved in the paper
2. If full chain: L4 is the SOLE premise, and every other structural feature (Jordan algebra, C*-involution, complex field, Born rule) is derived
3. If conditional chain: both L4 and C* are explicitly stated as premises, the sequential product route is discussed as "promising but incomplete at S4/local tomography," and the premise count is compared to competing reconstruction programs
4. The paper honestly states limitations, including finite-dimensionality restriction and any assumptions that were needed beyond L4
5. The manuscript is formatted for the target venue (Foundations of Physics / PRA / NJP) with abstract, introduction, main results, proofs, discussion, and bibliography

**Backtracking triggers:**
- If the logical chain has a gap discovered during writing -> return to Phase 4 or 5 to close it
- If peer review (adversarial AI or human) identifies circularity -> return to Phase 4

---

### Phase 7: D'Ariano Backup (CONTINGENCY)

**Goal:** If S4 fails in Phase 4, the C*-involution is constructed via D'Ariano's faithful-state method, using the B-M correlation state.

**Depends on:** Phase 4 (specifically: S4 must FAIL for this phase to activate)

**Requirements:** DRBK-01

**Contract Coverage:**
- Advances: claim-sp-axioms (partial -- documents S4 failure), provides alternative path for claim-paper-5
- Deliverables: Verification that the B-M correlation state satisfies D'Ariano's Postulate 5 (faithful + symmetric); explicit involution construction if conditions hold
- Anchor coverage: ref-dariano2006 (arXiv:quant-ph/0611094)
- Forbidden proxies: Assuming the correlation state is faithful without checking; postulating composition-preservation without attempting derivation

**Activation condition:** Phase 4 SPFM-03 produces a disproof of S4.

**Success Criteria** (what must be TRUE when this phase completes):

1. The B-M correlation state is explicitly constructed in the order unit space framework
2. Faithfulness of the correlation state is either proved (positive functionals separate points) or disproved (exhibit a nonzero element in the kernel)
3. Symmetry of the correlation state is either proved or disproved
4. If both faithfulness and symmetry hold: the involution is explicitly constructed via D'Ariano's method and verified to satisfy (ab)* = b*a*

**Backtracking triggers:**
- If the correlation state is not faithful -> D'Ariano route fails; Phase 6 ships conditional paper (L4 + C*)
- If composition-preservation cannot be derived and must be postulated -> document as additional premise; Phase 6 adjusts accordingly

**Stop condition:** If S4 fails AND D'Ariano backup also fails, the result is the conditional statement L4 + C* -> QM. This is still publishable and still novel (fewer premises than competitors). Ship Phase 6 with this framing.

## Phase Dependencies

| Phase | Depends On | Enables | Critical Path? |
|-------|-----------|---------|:-:|
| 4 - Sequential Product Formalization | -- | 5, 6, 7 | Yes |
| 5 - Local Tomography | 4 (success) | 6 | Yes |
| 6 - Paper Assembly | 4, 5 (or 7) | -- | Yes |
| 7 - D'Ariano Backup (contingency) | 4 (S4 failure) | 6 | Only if S4 fails |

**Critical path (success case):** 4 -> 5 -> 6 (3 phases)
**Critical path (S4 failure):** 4 -> 7 -> 6 (3 phases)
**No parallelism:** Phases are strictly sequential due to logical dependencies.

## Risk Register

| Phase | Top Risk | Probability | Impact | Mitigation |
|-------|---------|:-:|:-:|-----------|
| 4 | S4 fails for self-modeling sequential product | MEDIUM | HIGH | Phase 7 (D'Ariano backup); conditional paper still publishable |
| 4 | Circularity: update map smuggles in Hilbert space structure | LOW | FATAL | Mandatory circularity audit at every step; only order unit space primitives allowed |
| 4 | Non-associativity check fails (product is associative -> classical) | LOW | FATAL | Check early (SPFM-04 before S4); if fails, entire sequential product route is dead |
| 5 | Local tomography does not follow from independent accessibility alone | MEDIUM | MEDIUM | Identify minimal additional assumption; conditional paper absorbs the gap |
| 5 | Self-modeling framework lacks qubit-like 2-dim subsystem | LOW | HIGH | Would block Barnum-Wilce; need alternative route to complex field |
| 6 | Logical gap discovered during paper assembly | LOW | MEDIUM | Return to Phase 4 or 5 to close it |
| 7 | B-M correlation state not faithful | MEDIUM | HIGH | Route fails; ship conditional paper (L4 + C*) |

## Progress

**Execution Order:** 4 -> 5 -> 6 (happy path) or 4 -> 7 -> 6 (S4 failure path)

| Phase | Plans Complete | Status | Completed |
| ----- | -------------- | ------ | --------- |
| 4. Sequential Product Formalization | 5/6 (1 skipped) | Complete | 2026-03-21 |
| 5. Local Tomography | 0/2 | Planned | -- |
| 6. Paper Assembly | 0/TBD | Not started | -- |
| 7. D'Ariano Backup (contingency) | 0/TBD | Not needed (S4 passed) | -- |
