# Roadmap: Experiential Measure on Structure Space

## Milestones

- **v1.0 Experiential Measure Formalization** -- Phases 1-3 (completed 2026-03-16)
- **v2.0 QM from Algebraic Genericity** -- Phases 4-7 (completed 2026-03-21)
- **v3.0 GR Extension** -- Phases 8-12 (active)

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

### Active: v3.0 GR Extension

**Milestone Goal:** Derive Einstein's field equations from the locality of self-modeling, via the chain: local self-modeling lattice -> area-law entanglement -> Jacobson's thermodynamic derivation -> GR. Assemble as standalone Paper 6 with precise gap identification.

## Contract Overview

| Contract Item | Type | Advanced By Phase(s) | Status |
| ------------- | ---- | -------------------- | ------ |
| claim-locality (local self-modeling formalization) | claim | Phase 8 | Planned |
| claim-area-law (area-law entanglement from locality) | claim | Phase 9, Phase 11 | Planned |
| claim-jacobson (Jacobson inputs verified, Einstein derived) | claim | Phase 10 | Planned |
| claim-paper-6 (Paper 6 assembly) | claim | Phase 12 | Planned |
| ref-jacobson2016 (Jacobson 2016, PRL 116, 201101) | anchor | Phase 10, Phase 12 | Planned |
| ref-jacobson1995 (Jacobson 1995, PRL 75, 1260) | anchor | Phase 10, Phase 12 | Planned |
| ref-hastings2007 (Hastings 2007, JSTAT P08024) | anchor | Phase 9, Phase 12 | Planned |
| ref-ccm2017 (Cao-Carroll-Michalakis 2017, PRD 95, 024031) | anchor | Phase 10, Phase 12 | Planned |
| ref-paper5 (Paper 5, v2.0 -- QM from self-modeling) | anchor | Phase 8, Phase 12 | Planned |
| ref-vanraamsdonk2010 (Van Raamsdonk 2010, GRG 42, 2323) | anchor | Phase 12 | Planned |
| ref-lmvr2014 (Lashkari-McDermott-Van Raamsdonk 2014) | anchor | Phase 10, Phase 12 | Planned |
| ref-faulkner2014 (Faulkner et al. 2014) | anchor | Phase 12 | Planned |
| False progress: citing area-law theorems without checking hypotheses | forbidden proxy | Phase 9 | Active |
| False progress: citing Jacobson without connecting to self-modeling | forbidden proxy | Phase 10 | Active |
| False progress: hand-waving locality -> area law without gap identification | forbidden proxy | Phase 9, Phase 12 | Active |

## Phase Summary

- [ ] **Phase 8: Locality Formalization** -- Define self-modeling lattice in Bratteli-Robinson framework; establish Lieb-Robinson bounds and effective causal structure
- [ ] **Phase 9: Area-Law Derivation** -- Prove or strongly argue that local self-modeling interactions produce area-law entanglement; identify which state satisfies area-law conditions
- [ ] **Phase 10: Jacobson Application** -- Verify entanglement equilibrium and derive Einstein's field equations via Jacobson 2016
- [ ] **Phase 11: Numerical Verification** -- Validate area-law scaling on small self-modeling lattices via exact diagonalization
- [ ] **Phase 12: Paper Assembly** -- Assemble Paper 6 "Spacetime from Self-Modeling" with complete chain and precise gap identification

## Phase Details

### Phase 8: Locality Formalization

**Goal:** The self-modeling lattice is precisely defined as a quantum lattice system, with interactions encoding the B-M boundary coupling, and an effective causal structure established via Lieb-Robinson bounds.

**Depends on:** Paper 5 results (M_n(C)^sa, local tomography, composite structure) -- carried forward from v2.0

**Requirements:** LOCL-01, LOCL-02

**Contract Coverage:**
- Advances: claim-locality
- Deliverables: Formal lattice definition (graph, local algebras A_x = M_n(C), interaction Hamiltonian H encoding self-modeling coupling through B-M boundaries); Lieb-Robinson velocity v_LR computed for the specific interaction
- Anchor coverage: ref-paper5 (M_n(C)^sa per site, local tomography, composite OUS), Bratteli-Robinson (1979/1981), Lieb-Robinson (1972), Nachtergaele-Sims (2006/2019)
- Forbidden proxies: Lattice defined without specifying how self-modeling constrains the coupling; citing Lieb-Robinson bounds without computing v_LR for the specific Hamiltonian
- Prior inputs: Paper 5 composite OUS framework, M_n(C)^sa with Luders product

**Success Criteria** (what must be TRUE):

1. The lattice is defined with graph G = (V, E), local algebra A_x = M_n(C) at each site x, and nearest-neighbor interaction Hamiltonian H = sum_{<x,y>} h_{xy} where each h_{xy} encodes the self-modeling coupling through the shared B-M boundary
2. "Self-modeling locality" (model probes body through boundary, not bulk) is formally mapped onto "Hamiltonian locality" (finite-range interactions) with the correspondence made explicit -- specifically, how the B-M boundary interaction constrains the form of h_{xy}
3. Lieb-Robinson velocity v_LR is computed from the interaction Hamiltonian, establishing an effective light cone ||[O_X(t), O_Y]|| <= C exp(-mu(d(X,Y) - v_LR|t|)) with explicit constants C, mu, v_LR
4. All terms in the Hamiltonian have correct energy dimensions, and the lattice structure is consistent with the Bratteli-Robinson quantum lattice framework
5. The mapping is shown to be compatible with Paper 5's local tomography: the composite structure of two neighboring sites in the lattice reproduces the B-M composite OUS from v2.0

**Plans:** 3 plans

Plans:
- [ ] 08-01-PLAN.md -- Lattice definition + locality mapping + Hamiltonian construction from SP constraints
- [ ] 08-02-PLAN.md -- Lieb-Robinson framework instantiation + Heisenberg chain benchmark
- [ ] 08-03-PLAN.md -- LR velocity for self-modeling Hamiltonian + Paper 5 compatibility verification

**Backtracking triggers:**
- If "locality" in the self-modeling sense does not map onto "locality" in the Hamiltonian sense (the two notions are structurally incompatible) -> STOP, return to user for scope decision. This is a stop/rethink condition from the contract.
- If the self-modeling coupling through B-M boundaries does not uniquely determine the interaction Hamiltonian (underdetermined) -> identify the family of compatible Hamiltonians and whether area-law results are robust across the family.

---

### Phase 9: Area-Law Derivation

**Goal:** It is established (by proof or strong argument with precise gap identification) that local self-modeling interactions produce area-law entanglement entropy S(A) ~ |boundary(A)|, and the specific state satisfying the area law is identified.

**Depends on:** Phase 8 (lattice definition, interaction Hamiltonian, locality mapping)

**Requirements:** AREA-01, AREA-02

**Contract Coverage:**
- Advances: claim-area-law
- Deliverables: Proof or strong argument that S(A) ~ |boundary(A)| for the self-modeling lattice state; identification of which state (ground state, fixed point, thermal state) has the area law with justification; precise statement of any gap between self-modeling locality and existing area-law theorems
- Anchor coverage: ref-hastings2007 (area law for 1D gapped Hamiltonians -- template, hypothesis check required), Wolf-Verstraete-Cirac-Hastings 2008 (mutual info bound for thermal states), Brandao-Horodecki (2013/2015, correlation decay in 1D), Anshu-Arad-Gosset (2022, 2D frustration-free)
- Forbidden proxies: Citing area-law theorems without verifying their hypotheses apply to the self-modeling lattice; arguing "locality implies area law" without identifying the precise mathematical connection; assuming "ground state" without defining the Hamiltonian first (Phase 8 must be complete)
- User-stated observable: Whether locality -> area law holds; what exact assumption bridges any gap
- Stop/rethink condition: If no area-law argument (rigorous or strong physical) can be made, STOP

**Success Criteria** (what must be TRUE):

1. The state of the self-modeling lattice that has area-law entanglement is identified -- whether it is the ground state of H (if a spectral gap can be established or assumed), a thermal state (if WVCH route is used), or a pure state with local information flow (if channel capacity route is used) -- with explicit justification for why this state is the physically relevant one
2. Area-law scaling S(A) ~ |boundary(A)| is established for the identified state, with the argument either (a) proving it rigorously by verifying the hypotheses of an existing theorem (Hastings, Brandao-Horodecki, WVCH) apply, or (b) constructing a new information-theoretic argument (channel capacity bound) that S(A) <= c * |boundary(A)| * log(n) where n is local dimension
3. Any gap between the self-modeling setup and the hypotheses of the invoked theorem/argument is precisely stated -- e.g., "this argument requires the state to be the ground state of a gapped Hamiltonian; we have established/assumed that the self-modeling Hamiltonian is gapped because [reason]"
4. The argument addresses spatial dimension: rigorous in 1D, with a physically motivated extension to higher D (or clear statement that higher D remains conjectural)
5. The area-law result is shown to be robust under perturbations of the interaction Hamiltonian within the family of self-modeling-compatible interactions (if the family is non-unique from Phase 8)

**Plans:** TBD

**Backtracking triggers:**
- If the self-modeling fixed point has volume-law entanglement -> the core hypothesis is falsified. Document the result and return to user for scope decision.
- If the channel capacity route requires a pure global state and the self-modeling fixed point is mixed -> fall back to WVCH (thermal) route or Hastings (gapped ground state) route.
- If all area-law routes fail -> STOP. This is a stop/rethink condition from the contract.

---

### Phase 10: Jacobson Application

**Goal:** Jacobson's 2016 entanglement equilibrium condition is verified for the self-modeling lattice, and Einstein's field equations are derived as the leading-order IR effective description of the continuum limit.

**Depends on:** Phase 8 (causal structure), Phase 9 (area-law entanglement)

**Requirements:** JACB-01, JACB-02

**Contract Coverage:**
- Advances: claim-jacobson
- Deliverables: Verification that the self-modeling lattice satisfies Jacobson 2016's maximal vacuum entanglement hypothesis (MVEH): delta S_EE = 0 for small geodesic balls; derivation of G_ab + Lambda g_ab = (8 pi G) T_ab in the continuum limit; identification of G = 1/(4 eta) in terms of self-modeling lattice parameters
- Anchor coverage: ref-jacobson2016 (PREFERRED -- entanglement equilibrium, PRL 116, 201101), ref-jacobson1995 (original thermodynamic derivation), ref-lmvr2014 (entanglement first law), ref-ccm2017 (emergent spatial geometry as consistency check)
- Forbidden proxies: Restating Jacobson's conditions without verifying they hold for self-modeling; citing Jacobson without connecting to the self-modeling lattice; hand-waving the continuum limit without framing it as a Wilsonian effective description
- User-stated deliverable: Full nonlinear Einstein equations G_ab + Lambda g_ab = (8 pi G) T_ab

**Success Criteria** (what must be TRUE):

1. The entanglement first law delta S = delta <K> is verified for the self-modeling lattice state from Phase 9, with K = -ln(rho_A) identified as the modular Hamiltonian of the reduced state
2. Jacobson 2016's MVEH (maximal vacuum entanglement hypothesis) is either (a) verified to hold for the self-modeling area-law state, or (b) identified as an additional assumption with clear statement of what self-modeling property would establish it
3. The continuum limit is framed as a Wilsonian effective description: lattice = UV completion, Einstein's equations = leading-order IR theory at scales >> lattice spacing, with the lattice spacing a as the cutoff
4. Einstein's field equations G_ab + Lambda g_ab = (8 pi G) T_ab are derived in the continuum limit, with G = 1/(4 eta) where eta is the entanglement entropy density, and Lambda appearing as an undetermined integration constant
5. The argument addresses the three historical Jacobson inputs -- (i) area-law entropy (from Phase 9), (ii) local equilibrium / entanglement equilibrium (verified or assumed), (iii) boost generator / modular Hamiltonian (identified) -- with each input's status in the self-modeling framework made explicit

**Plans:** TBD

**Backtracking triggers:**
- If the entanglement first law does not hold for the self-modeling state (e.g., the state is not differentiable under perturbations) -> investigate whether an approximate first law suffices.
- If MVEH cannot be verified or motivated from self-modeling properties -> identify as a gap in Paper 6, not a roadblock. Jacobson's argument still applies conditionally.
- If the continuum limit produces f(R) gravity instead of Einstein's equations -> indicates non-equilibrium effects. Revisit the equilibrium assumption.

---

### Phase 11: Numerical Verification

**Goal:** Area-law scaling and entanglement structure are verified numerically on small self-modeling lattices, benchmarked against known models.

**Depends on:** Phase 8 (interaction Hamiltonian -- needed for self-modeling lattice numerics)
**Partial parallelism:** Benchmark computations on known models (Heisenberg chain, transverse Ising) can begin immediately, without Phase 8. Self-modeling-specific numerics require Phase 8's Hamiltonian.

**Requirements:** NUMR-01

**Contract Coverage:**
- Advances: claim-area-law (numerical support)
- Deliverables: Area-law scaling data with fit statistics (R^2 for area-law vs volume-law fits); benchmark validation on Heisenberg and transverse Ising models; S(A) vs |boundary(A)| and |volume(A)| regression for self-modeling lattice
- Anchor coverage: Known benchmarks (Heisenberg chain, transverse Ising at criticality and away from criticality) as positive and negative controls
- Forbidden proxies: Only checking 1D without attempting 2D (if feasible); reporting scaling without fit statistics; claiming area law without distinguishing from volume law quantitatively

**Success Criteria** (what must be TRUE):

1. Benchmark models reproduce known results: (a) gapped 1D Heisenberg/Ising shows S(A) = O(1) (area law), (b) critical 1D Ising shows S(A) ~ (c/6) ln(L) (log violation), confirming the numerical infrastructure is correct
2. Self-modeling lattice (exact diagonalization, N = 16-20 qubits / 8-10 M_2(C)^sa sites in 1D) shows area-law scaling: R^2 > 0.9 for S(A) vs |boundary(A)| fit, R^2 < 0.5 for S(A) vs |volume(A)| fit
3. If 2D is computationally feasible (4x4 lattice, 16 qubits): area-law scaling verified in 2D with the same fit criteria
4. Entanglement entropy values are converged (insensitive to numerical precision artifacts) and error bars from finite-size effects are estimated

**Plans:** TBD

**Backtracking triggers:**
- If the self-modeling lattice shows volume-law scaling -> contradicts Phase 9 argument. Return to Phase 9 for debugging.
- If benchmark models fail to reproduce known results -> numerical infrastructure error. Debug before proceeding to self-modeling lattice.

---

### Phase 12: Paper Assembly

**Goal:** Paper 6 "Spacetime from Self-Modeling" is assembled as a complete, self-contained manuscript presenting the derivation chain from self-modeling locality to Einstein's field equations, with precise gap identification and honest framing.

**Depends on:** Phase 8 (lattice), Phase 9 (area law), Phase 10 (Jacobson), Phase 11 (numerics)

**Requirements:** PAPR-01

**Contract Coverage:**
- Advances: claim-paper-6
- Deliverables: Paper 6 manuscript (LaTeX, publication-ready) with: introduction motivating the chain, self-modeling lattice definition, area-law argument, Jacobson application, numerical verification, discussion with gap identification, bibliography
- Anchor coverage: All v3.0 anchors cited (ref-jacobson1995, ref-jacobson2016, ref-hastings2007, ref-ccm2017, ref-paper5, ref-vanraamsdonk2010, ref-lmvr2014, ref-faulkner2014); Paper 5 cited as input
- Forbidden proxies: Paper that glosses over gaps instead of identifying them precisely; hand-waving the locality -> area law step; overclaiming scope (lesson from v1.0 peer review)
- User-stated deliverable: Paper 6, standalone, separate from Paper 5

**Success Criteria** (what must be TRUE):

1. The paper presents the complete chain: self-modeling (Paper 5) -> local lattice (Phase 8) -> area-law entanglement (Phase 9) -> entanglement equilibrium (Phase 10) -> Einstein's field equations, with every step either a published result (cited) or a result argued in the paper
2. Every gap in the argument is precisely identified -- e.g., "the area-law step assumes X, which we have established/not established because Y" -- with no hand-waving or elision of assumptions
3. The paper is honest about what is derived vs assumed: self-modeling as sole premise, lattice topology as input, continuum limit as Wilsonian effective description, any additional assumptions for area law or MVEH
4. Numerical results from Phase 11 are presented as supporting evidence with proper error quantification
5. The paper is formatted for the target venue (PRD or Foundations of Physics) with abstract, introduction, main results, discussion, and complete bibliography

**Plans:** TBD

**Backtracking triggers:**
- If assembling the chain reveals a logical gap not caught in Phases 8-10 -> return to the relevant phase.
- If adversarial review (AI or human) identifies circularity or overclaiming -> revise specific sections.

## Phase Dependencies

| Phase | Depends On | Enables | Critical Path? |
|-------|-----------|---------|:-:|
| 8 - Locality Formalization | Paper 5 (v2.0) | 9, 10, 11 | Yes |
| 9 - Area-Law Derivation | 8 | 10, 12 | Yes |
| 10 - Jacobson Application | 8, 9 | 12 | Yes |
| 11 - Numerical Verification | 8 (partial: benchmarks independent) | 12 | No (parallel with 9-10) |
| 12 - Paper Assembly | 8, 9, 10, 11 | -- | Yes |

**Critical path:** 8 -> 9 -> 10 -> 12 (4 phases, minimum duration)
**Parallelizable:** Phase 11 benchmark infrastructure begins immediately; self-modeling numerics run after Phase 8 completes, concurrent with Phases 9-10.

**Execution order:**

```
Wave 1: Phase 8 (sole entry point)
Wave 2: Phase 9 + Phase 11 (benchmarks) -- parallel
Wave 3: Phase 10 + Phase 11 (self-modeling numerics) -- parallel
Wave 4: Phase 12 (requires all prior phases)
```

## Risk Register

| Phase | Top Risk | Probability | Impact | Mitigation |
|-------|---------|:-:|:-:|-----------|
| 8 | Self-modeling locality does not map onto Hamiltonian locality | LOW | FATAL | Contract stop/rethink condition. If the two locality notions are structurally incompatible, the entire v3.0 chain breaks. Return to user. |
| 9 | Self-modeling state has volume-law, not area-law, entanglement | MEDIUM | FATAL | Try multiple routes (channel capacity, WVCH, Hastings). If all fail, the hypothesis is falsified. Document and return. |
| 9 | Channel capacity route requires pure state; self-modeling fixed point is mixed | MEDIUM | HIGH | Fall back to WVCH (thermal) or Hastings (gapped). These routes have additional hypotheses to verify. |
| 10 | No published lattice version of Jacobson exists; adaptation fails | MEDIUM | HIGH | Jacobson 2016 (entanglement equilibrium) is more lattice-compatible than 1995. Entanglement first law is an exact identity on any lattice. Gap is MVEH verification -- identify as explicit assumption if needed. |
| 10 | Continuum limit produces modified gravity (f(R)) instead of GR | LOW | MEDIUM | Indicates non-equilibrium correction. Identify as gap in paper. |
| 11 | Numerics contradict analytical area-law argument | LOW | HIGH | Debug: either numerics or analytics have an error. Systematically check. |
| 12 | Logical gap discovered during paper assembly | LOW | MEDIUM | Return to relevant phase (8, 9, or 10) to close it. |

## Progress

**Execution Order:** 8 -> (9, 11-benchmarks) -> (10, 11-self-modeling) -> 12

| Phase | Milestone | Plans Complete | Status | Completed |
| ----- | --------- | -------------- | ------ | --------- |
| 8. Locality Formalization | v3.0 | 0/3 | Planned | -- |
| 9. Area-Law Derivation | v3.0 | 0/TBD | Not started | -- |
| 10. Jacobson Application | v3.0 | 0/TBD | Not started | -- |
| 11. Numerical Verification | v3.0 | 0/TBD | Not started | -- |
| 12. Paper Assembly | v3.0 | 0/TBD | Not started | -- |
