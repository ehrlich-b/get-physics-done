# Requirements: GR from det(X) on h_3(O)

**Defined:** 2026-04-11
**Core Research Question:** Does the Peirce complement V_0 = h_2(O), projected via the C*-bottleneck to h_2(C) = R^{3,1}, carry the GST magic supergravity structure with prepotential det(X)?

## Primary Requirements

### Algebraic Foundations

- [ ] **ALGB-01**: Implement and verify projection pi_u: h_2(O) -> h_2(C_u); confirm det on h_2(C_u) has Minkowski signature (1,3)
- [ ] **ALGB-02**: Compute full d_{IJK} polarized cubic form tensor on h_3(O) and decompose into Peirce blocks; confirm exactly two nonzero blocks: (V_1,V_0,V_0) and (V_{1/2},V_{1/2},V_0)
- [ ] **ALGB-03**: Verify stabilizer of u in Spin(9) contains SL(2,C_u) acting as Lorentz group on h_2(C_u); identify full stabilizer Lie algebra
- [ ] **ALGB-04**: Characterize pi_u non-homomorphism failure term pi_u(A circ B) - pi_u(A) circ pi_u(B) and its algebraic structure
- [ ] **ALGB-05**: Compute Peirce product V_{1/2} x V_{1/2} -> V_0 explicitly and determine its image under pi_u

### Uniqueness and Structure Theorems

- [ ] **UNIQ-01**: State and prove "double duty" theorem: det(X) is unique (up to scale) F_4-invariant cubic on h_3(O), forcing rho_J and GST prepotential to share det(X) by algebraic necessity
- [ ] **UNIQ-02**: Decompose the 27 under Peirce + C*-bottleneck: verify 16 -> SM fermions (Paper 7), 10 -> 4 + 6 (spacetime + internal), 1 -> singlet

### Gravitational Connection

- [ ] **GRAV-01**: Identify GST 5d N=2 MESGT field content under Peirce decomposition; match scalars, vectors, and graviton to V_1, V_{1/2}, V_0 sectors
- [ ] **GRAV-02**: Perform 5d -> 4d circle compactification; verify 4d field content (graviton + 28 vectors + 56 scalars on E_7(-25)/(E_6 x U(1)))
- [ ] **GRAV-03**: State precise claim: det(X) determines matter-gravity coupling structure (scalar manifold, prepotential); Paper 6 determines GR itself (Einstein equations via Jacobson)
- [ ] **GRAV-04**: Compute 4d cosmological constant from GST vacuum structure
- [ ] **GRAV-05**: Decompose Chern-Simons cubic coupling C_{IJK} under Peirce; identify physical couplings (fermion-fermion-spacetime, gravitational self-coupling)

### Synthesis

- [ ] **SYNT-01**: Assemble complete picture: Papers 5 (QM) + 6 (GR) + 7 (SM) + this milestone (matter-gravity coupling) giving SM+GR from self-modeling
- [ ] **SYNT-02**: Identify and honestly state all remaining gaps, open questions, and conditional claims

## Follow-up Requirements

### Extended Analysis

- **EXTD-01**: Physical interpretation of pi_u failure term as gauge-gravity coupling
- **EXTD-02**: Connection to Farnsworth's spectral triple framework for gravity sector
- **EXTD-03**: Moduli stabilization on E_6(-26)/F_4 scalar manifold
- **EXTD-04**: Extension to full 10d/11d supergravity context

## Out of Scope

| Topic | Reason |
|-------|--------|
| Full GST Lagrangian numerical evaluation | Only algebraic structure needed; numerical coefficients require spectral action |
| E_7(-25) quaternionic-Kahler geometry | 4d scalar manifold details beyond field content counting |
| Moduli stabilization and vacuum selection | Requires dynamical mechanism beyond algebraic structure |
| Re-deriving Papers 5, 6, 7 results | Already established; used as input |
| Spectral action computation for coupling constants | Beyond scope -- separate milestone |
| N=2 SUSY preservation or breaking | Self-modeling framework is SUSY-agnostic |

## Accuracy and Validation Criteria

| Requirement | Accuracy Target | Validation Method |
|-------------|-----------------|-------------------|
| ALGB-01 | Exact (algebraic) | det signature check; det(E_{11})=0, det(I)=1 benchmarks |
| ALGB-02 | Exact (algebraic) | d_{IJK} symmetry; reassembled tensor reproduces det; d_{0,0,0}=0 |
| ALGB-03 | Exact (algebraic) | Stabilizer Lie algebra dimension and structure; SL(2,C) embedding explicit |
| UNIQ-01 | Exact (proof) | Springer 1962 uniqueness; dim Sym^3(27)^{F_4} = 1 |
| UNIQ-02 | Exact (algebraic) | Quantum numbers match Paper 7 table; dimensions add to 27 |
| GRAV-01 | Exact (field counting) | Match GST 1984 Table 1; 27 vectors, 26+1 scalars |
| GRAV-02 | Exact (field counting) | Match de Wit-Van Proeyen; E_7(-25) coset dimension = 56 |
| GRAV-03 | N/A (precise statement) | No overclaiming vs Paper 6; reviewable by physicist |
| SYNT-01 | N/A (assembly) | All links cited; no circular dependencies |
| SYNT-02 | N/A (completeness) | Every conditional claim flagged; no hidden assumptions |

## Contract Coverage

| Requirement | Decisive Output | Anchor / Reference | Prior Inputs | False Progress To Reject |
|-------------|-----------------|-------------------|--------------|--------------------------|
| ALGB-01 | Explicit pi_u matrix + signature proof | Baez 2002 (h_2(C)=R^{3,1}) | Existing octonion code | Claiming R^{3,1} without pi_u (h_2(O)=R^{9,1}) |
| ALGB-02 | d_{IJK} tensor with Peirce block labels | GST 1984 C_{IJK} | det_h3o implementation | Incomplete block decomposition |
| ALGB-03 | Stabilizer Lie algebra generators | Paper 7 Spin(9) action | Existing Cl(9,0) gamma matrices | Confusing Spin(9) with SO(9) |
| UNIQ-01 | Theorem statement + proof | Springer 1962 | F_4 rep theory | Circular argument using GST to prove GST |
| GRAV-02 | 4d field content table | de Wit-Van Proeyen 1992 | 5d GST content | Wrong E_6 real form |
| GRAV-03 | Precise 2-sentence claim | Papers 5, 6, 7 | All prior milestones | "GR from h_3(O)" without Paper 6 |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| ALGB-01 | Phase 46 | Pending |
| ALGB-02 | Phase 47 | Pending |
| ALGB-03 | Phase 48 | Pending |
| ALGB-04 | Phase 46 | Pending |
| ALGB-05 | Phase 46 | Pending |
| UNIQ-01 | Phase 47 | Pending |
| UNIQ-02 | Phase 47 | Pending |
| GRAV-01 | Phase 49 | Pending |
| GRAV-02 | Phase 49 | Pending |
| GRAV-03 | Phase 49 | Pending |
| GRAV-04 | Phase 49 | Pending |
| GRAV-05 | Phase 49 | Pending |
| SYNT-01 | Phase 50 | Pending |
| SYNT-02 | Phase 50 | Pending |

**Coverage:**

- Primary requirements: 14 total
- Mapped to phases: 14/14
- Unmapped: 0

---

_Requirements defined: 2026-04-11_
_Last updated: 2026-04-11 after roadmap creation (phases 46-50)_
