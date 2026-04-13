# Requirements: Paper 6 Closure -- G4 + N=2 from Algebraic Structure

**Defined:** 2026-04-12
**Core Research Question:** Can V_0 = spacetime and N=2 SUSY be DERIVED from h_3(O) algebraic structure, eliminating them as independent inputs to the GR derivation?

## Primary Requirements

### Spacetime Derivation (G4)

- [ ] **SPTM-01**: Verify operational criteria OD1-OD4 for V_0: (OD1) V_1 . V_0 = 0 (Peirce disjointness), (OD2) V_{1/2} . V_{1/2} -> V_0 surjective (accessibility), (OD3) V_0 acts faithfully on V_{1/2} via L_v maps (completeness), (OD4) dim(V_0) = 10 with Peirce completeness 1+16+10=27 (maximality)
- [ ] **SPTM-02**: Compute KKT algebra g(h_2(C_u)) with explicit 15 generators: 4 translations (g_{-1}), 4 special conformal (g_{+1}), 3 rotations + 3 boosts + 1 dilatation (g_0 = Str_0). Verify structure constants match so(4,2).
- [ ] **SPTM-03**: Verify OD5-OD6: classify h_2(C_u) elements by det_2 sign (timelike/null/spacelike), verify forward cone {det_2 > 0, Tr > 0} is convex, verify SL(2,C_u) acts preserving det_2 (Lorentz group identification)
- [ ] **SPTM-04**: Verify OD7 (observer independence): construct second rank-1 idempotent E', verify V_0(E') is F_4-conjugate to V_0(E_{11}), verify det_2 signature and d_{IJK} pattern invariant under observer change
- [ ] **SPTM-05**: State and prove uniqueness theorem: for self-modeling observer at rank-1 idempotent E in h_3(O), pi_u(V_0(E)) = h_2(C_u) is the unique 4d subspace that is (a) disjoint from observer, (b) completely accessible through measurements, (c) Lorentzian, (d) observer-independent up to F_4-conjugacy
- [ ] **SPTM-06**: Identify boost generators explicitly in Str_0(h_2(C_u)) as L_X operators for traceless X in h_2(C_u). Verify [boost, rotation] commutation relations match so(3,1). (Resolves gap G5: compact so(3) -> non-compact so(3,1))

### Lagrangian Uniqueness (N=2 as Consequence)

- [ ] **LAGR-01**: Compute very special real metric a_{IJ} = -(1/2) d_I d_J log det(X)|_{det=1} from Phase 47 d_{IJK} tensor. Verify positive definiteness on the physical constraint surface.
- [ ] **LAGR-02**: Prove two-derivative bosonic Lagrangian uniqueness: enumerate all E_{6(-26)}-invariant two-derivative terms (scalar kinetic, vector kinetic, Chern-Simons, -R/2). Show no other structures exist at this order.
- [ ] **LAGR-03**: Verify all relative coefficients between Lagrangian terms are fixed by the cubic form + E_{6(-26)} covariance alone, with NO N=2 SUSY input. Trace through de Wit-Van Proeyen construction to confirm no SUSY assumption enters.
- [ ] **LAGR-04**: State N=2 as derived property: (1) det(X) -> unique bosonic Lagrangian (LAGR-02/03), (2) GST bijection -> this IS the bosonic sector of N=2 MESGT, (3) therefore N=2 is a property discovered, not assumed. State conclusion precisely.
- [ ] **LAGR-05**: Cross-check: verify uniqueness-derived coefficients match Phase 49 explicit values (Eq. 49.6). Scalar metric, vector metric, and Chern-Simons coefficient must agree exactly.

## Follow-up Requirements

### Future Directions

- **FUTR-01**: Close gap G6 (so(6) -> G_SM) via Todorov-Drenska F_4-Spin(9) intersection mechanism
- **FUTR-02**: Close gap G7 (3 generations) via Boyle triality mechanism
- **FUTR-03**: Investigate Lambda != 0 mechanism beyond ungauged MESGT
- **FUTR-04**: Address fermion sector completion (N=2 gives bosonic sector only)

## Out of Scope

| Topic | Reason |
| ----- | ------ |
| Fermion sector of N=2 MESGT | Bosonic Lagrangian uniqueness suffices for Paper 6; fermions are a separate paper |
| Quantum corrections to MESGT | v13.0 is tree-level algebraic derivation; quantum corrections are phenomenology |
| Fisher-Rao metric on V_0 | Positive semi-definite by construction, CANNOT give Minkowski -- explicitly excluded |
| Gauged MESGT / Lambda != 0 | Ungauged case suffices; gauging is follow-up (FUTR-03) |
| 5d -> 4d dimensional reduction details | Use 4d formulation directly (Phase 49 infrastructure) |
| Spectral action computation | Beyond Paper 6 scope |

## Accuracy and Validation Criteria

| Requirement | Accuracy Target | Validation Method |
| ----------- | --------------- | ----------------- |
| SPTM-01 | Exact (algebraic identity) | Numerical verification of Peirce multiplication rules |
| SPTM-02 | Exact (15 structure constants) | Verify [g_i, g_j] = f_{ij}^k g_k matches so(4,2) Killing form |
| SPTM-03 | Exact (signature classification) | Eigenvalue computation on h_2(C_u) elements |
| SPTM-04 | Exact (F_4 conjugacy) | Explicit second idempotent + Peirce decomposition comparison |
| SPTM-05 | Logical proof | Elimination of all alternative subspaces |
| SPTM-06 | Exact (commutation relations) | Verify so(3,1) algebra from L_X operators |
| LAGR-01 | Exact (from d_{IJK}) | Positive eigenvalues of a_{IJ} at constraint point |
| LAGR-02 | Logical proof | Invariant theory: no additional E_{6(-26)}-invariant structures |
| LAGR-03 | Exact (coefficient comparison) | Trace dWVP derivation step by step for SUSY-free path |
| LAGR-04 | Logical argument | GST theorem citation + logic chain |
| LAGR-05 | Exact match | Numerical comparison with Phase 49 values |

## Contract Coverage

| Requirement | Decisive Output | Anchor / Benchmark | Prior Inputs | False Progress To Reject |
| ----------- | --------------- | ------------------- | ------------ | ------------------------ |
| SPTM-02 | so(4,2) structure constants | Tits 1962, Gunaydin 1993 | Phase 46 pi_u, h_2(C_u) basis | Getting so(3) only (derivations, not full KKT) |
| SPTM-05 | Uniqueness theorem statement | Borel 1950 (F_4 transitivity) | Phase 46-48 results | Claiming uniqueness without eliminating alternatives |
| SPTM-06 | Explicit boost generators | Phase 48 so(3) rotations | Str_0(h_2(C_u)) computation | Citing boosts exist abstractly without constructing them |
| LAGR-02 | Lagrangian uniqueness proof | de Wit-Van Proeyen 1992 | Phase 47 d_{IJK}, Phase 49 Lagrangian | Proving uniqueness WITH N=2 assumed (circular) |
| LAGR-03 | SUSY-free coefficient fixing | Ferrara-Gunaydin 2006 | dWVP construction | Using SUSY to fix relative coefficients then claiming N=2 derived |
| LAGR-04 | GST bijection application | GST 1984, Nucl. Phys. B 242 | LAGR-02/03 results | Stating "N=2 is consequence" without proving Lagrangian uniqueness first |

## Traceability

| Requirement | Phase | Status |
| ----------- | ----- | ------ |
| SPTM-01 | Phase 52: G4 Spacetime Derivation | Pending |
| SPTM-02 | Phase 52: G4 Spacetime Derivation | Pending |
| SPTM-03 | Phase 52: G4 Spacetime Derivation | Pending |
| SPTM-04 | Phase 52: G4 Spacetime Derivation | Pending |
| SPTM-05 | Phase 52: G4 Spacetime Derivation | Pending |
| SPTM-06 | Phase 52: G4 Spacetime Derivation | Pending |
| LAGR-01 | Phase 53: N=2 Lagrangian Uniqueness | Pending |
| LAGR-02 | Phase 53: N=2 Lagrangian Uniqueness | Pending |
| LAGR-03 | Phase 53: N=2 Lagrangian Uniqueness | Pending |
| LAGR-04 | Phase 53: N=2 Lagrangian Uniqueness | Pending |
| LAGR-05 | Phase 53: N=2 Lagrangian Uniqueness | Pending |

**Coverage:**

- Primary requirements: 11 total
- Mapped to phases: 11
- Unmapped: 0

---

_Requirements defined: 2026-04-12_
_Last updated: 2026-04-12 after initial definition_
