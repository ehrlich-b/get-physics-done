# Requirements: Universality Class of Self-Modeler Network and Full Gap Closure

**Defined:** 2026-03-30
**Core Research Question:** Can the Standard Model + GR be derived from the requirement that a composite system faithfully models itself?

## Primary Requirements

Requirements for the main research deliverable. Each maps to roadmap phases.

### Gap Dependency (Formal Logic)

- [ ] **GAPD-01**: Prove gap dependency theorem: universality class properties (UC1)-(UC4) plus enumerated additional assumptions (Wightman axioms, d=3+1, local equilibrium) imply all four Paper 6 gaps close. Explicit mapping from each UC property to each gap's closure conditions. Honest enumeration of ALL hidden assumptions beyond (UC1)-(UC4).
- [ ] **GAPD-02**: Prove Gap C closure chain: BW fires -> K_B is local (modular Hamiltonian = boost generator) -> entanglement first law delta S = delta <K_B> is first order -> Raychaudhuri gives delta A in terms of R_ab (at most 2 derivatives) -> Lovelock uniqueness forces G_ab + Lambda g_ab. Tensoriality DERIVED, not assumed.
- [ ] **GAPD-03**: Prove Gap D closure chain: BW fires -> Tomita-Takesaki KMS at beta=2pi -> vacuum IS thermal equilibrium w.r.t. modular flow -> Gibbs variational principle (thermal eq = max entropy at fixed energy) -> this IS entanglement equilibrium (delta S = 0 for first-order perturbations at fixed <K_B>) -> this IS MVEH. Equivalence proved via Gibbs variational principle.

### Effective Hamiltonian (Algebraic Structure)

- [ ] **HEFF-01**: Compute effective Hamiltonian H_eff for self-modeling subsystems interacting via the Jordan product of h_3(O), using existing T_b operators (16x16 real matrices from v8.0 Phase 28). Explicit matrix elements for nearest-neighbor self-modeler pairs. Determine ferro/antiferro/frustrated character.
- [ ] **HEFF-02**: Identify and prove symmetry group of H_eff. Compute frame stabilizer in F_4 (candidates: Spin(9), Spin(8), G_2). Determine whether H_eff inherits full F_4 symmetry or only a subgroup. Resolve cubic invariant contribution.
- [ ] **HEFF-03**: Derive extended lattice structure from many-body Peirce network (beyond the 3-site K_3 motif). Resolve K_3 non-bipartiteness issue (K_3 has odd 3-cycle). Determine geometry of infinite self-modeler lattice. Check DLS bipartiteness condition on extended lattice.

### SSB and Universality Class

- [ ] **SSBR-01**: Prove spontaneous F_4 breaking in ground state of H_eff on extended lattice in d >= 3 via DLS/FSS/BCS infrared bounds framework (or alternative if lattice non-bipartite). Identify SSB pattern F_4 -> H with proof. Or honest negative result if SSB fails.
- [ ] **SSBR-02**: Count Goldstone modes via Watanabe-Murayama formula applied to F_4 -> H. Determine type (Type I linear vs Type II quadratic dispersion). Compute number = dim(F_4) - dim(H). Verify all modes are gapless.
- [ ] **SSBR-03**: Construct NL sigma model on target space F_4/H. Compute one-loop beta function (Friedan formula via Ricci tensor). Verify asymptotic freedom. Assess RG relevance of cubic invariant det(A). Check homotopy groups for topological terms.
- [ ] **SSBR-04**: Verify all four universality class properties for the self-modeler network: (UC1) gapless excitations from Goldstone modes, (UC2) algebraic correlation decay |C(r)| ~ r^{-(d-1)}, (UC3) isotropy (lattice anisotropy RG-irrelevant), (UC4) OS reflection positivity on the lattice.

### Assembly

- [ ] **ASBL-03**: Apply gap dependency theorem (GAPD-01) to universality class verification (SSBR-04). Update all four gap scores from v9.0 baselines. Produce complete chain document with the self-modeler network (not toy model) at every step.
- [ ] **ASBL-04**: Side-by-side comparison of v10.0 chain (real h_3(O) algebra) vs v9.0 chain (Heisenberg toy model). Document: what was CONDITIONAL is now PROVED; what was toy model is now real algebra; what new assumptions (if any) were introduced.

## Follow-up Requirements

### Extended Analysis

- **EXTD-01**: Compute spectral action for F_4/H sigma model (coupling constants, Higgs mass predictions)
- **EXTD-02**: Investigate d=2 case (Mermin-Wagner restrictions, possible BKT-type transition)
- **EXTD-03**: Numerical ED/DMRG verification of SSB on small F_4-symmetric lattices (N=2-6)
- **EXTD-04**: Classical Monte Carlo on OP^2 for large-lattice sigma model behavior

## Out of Scope

| Topic | Reason |
| ----- | ------ |
| Re-deriving v9.0 results | Cite Phases 32-36; mechanism already established |
| Re-deriving Papers 5, 6, 7 | Cite published results |
| Constructive continuum limit | Effective smoothness suffices (v9.0 established) |
| Spectral action computation | Beyond current milestone; coupling constants deferred |
| Paper writing | Derivation documents only; paper revision deferred |
| d != 3 cases | d=3 selected by rank of h_3(O); d=1,2 are not our universe |
| QMC sign problem investigation | No cluster available; analytical methods primary |

## Accuracy and Validation Criteria

| Requirement | Accuracy Target | Validation Method |
| ----------- | --------------- | ----------------- |
| GAPD-01 | Formal theorem with complete assumption list | Check each gap closure against stated assumptions; verify no circular reasoning |
| GAPD-02 | Rigorous logical chain | Verify each step cites v9.0 equation; check derivative counting |
| GAPD-03 | Rigorous equivalence proof | Verify Gibbs variational -> entanglement equilibrium bijection |
| HEFF-01 | Exact matrix elements | Cross-check against existing T_b operators from v8.0 |
| HEFF-02 | Group-theoretic proof | Verify stabilizer dimension matches; check with representation theory |
| HEFF-03 | Lattice geometry determined | Verify bipartiteness/non-bipartiteness; check DLS conditions explicitly |
| SSBR-01 | Rigorous SSB proof or honest conditional | Verify all DLS/FSS/BCS conditions; cite theorem precisely |
| SSBR-02 | Exact Goldstone count | Cross-check dim(F_4) - dim(H) = dim(F_4/H) |
| SSBR-03 | One-loop beta function computed | Verify against Friedan formula; check Ricci tensor of F_4/H |
| SSBR-04 | All four UC properties verified | Each mapped to specific SSB/sigma model result |
| ASBL-03 | All gaps scored with citations | Each score justified by specific theorem from Phases 37-39 |
| ASBL-04 | Honest comparison | Every CONDITIONAL -> PROVED upgrade has theorem reference |

## Contract Coverage

| Requirement | Decisive Output / Deliverable | Anchor / Benchmark / Reference | Prior Inputs / Baselines | False Progress To Reject |
| ----------- | ----------------------------- | ------------------------------ | ------------------------ | ------------------------ |
| GAPD-01 | Formal theorem statement + proof | v9.0 gap scorecards (Phase 36) | Phase 35 BW/KMS results | Claiming gaps close "because mechanism works" without tracing logical chain |
| HEFF-01 | Explicit H_eff matrix elements | v8.0 T_b operators (Phase 28) | Peirce multiplication rules | Generic "H = J*(Jordan product)" without computing matrix elements |
| HEFF-03 | Lattice geometry diagram + bipartiteness proof | DLS bipartiteness conditions | K_3 Peirce triangle | Assuming bipartiteness without proof |
| SSBR-01 | SSB theorem or negative result | DLS 1978, FSS 1976, KLS 1988 | H_eff from HEFF-01 | Claiming SSB "because ground state chooses frame" without rigorous theorem |
| SSBR-03 | Sigma model Lagrangian + beta function | Friedan 1980, Eichenherr-Forger 1980 | F_4/H from SSBR-01 | Assuming sigma model target without computing from H_eff |
| ASBL-03 | Updated gap scorecard | v9.0 Phase 36 scores | All v10.0 results | Upgrading scores without citing specific theorem |

## Traceability

| Requirement | Phase | Status |
| ----------- | ----- | ------ |
| GAPD-01 | Phase 37: Gap Dependency Theorem | Pending |
| GAPD-02 | Phase 37: Gap Dependency Theorem | Pending |
| GAPD-03 | Phase 37: Gap Dependency Theorem | Pending |
| HEFF-01 | Phase 38: Effective Hamiltonian | Pending |
| HEFF-02 | Phase 38: Effective Hamiltonian | Pending |
| HEFF-03 | Phase 38: Effective Hamiltonian | Pending |
| SSBR-01 | Phase 39: SSB and Universality Class | Pending |
| SSBR-02 | Phase 39: SSB and Universality Class | Pending |
| SSBR-03 | Phase 39: SSB and Universality Class | Pending |
| SSBR-04 | Phase 39: SSB and Universality Class | Pending |
| ASBL-03 | Phase 40: Assembly | Pending |
| ASBL-04 | Phase 40: Assembly | Pending |

**Coverage:**

- Primary requirements: 12 total
- Mapped to phases: 12
- Unmapped: 0

---

_Requirements defined: 2026-03-30_
_Last updated: 2026-03-30 after initial definition_
