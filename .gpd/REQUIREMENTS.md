# Requirements: GR from Self-Modeling

**Defined:** 2026-03-21
**Core Research Question:** Does the locality of self-modeling force area-law entanglement and thereby Einstein's field equations via Jacobson's thermodynamic argument?

## Primary Requirements

### Locality Formalization

- [ ] **LOCL-01**: Define lattice of self-modeling M_n(C)^sa systems with local coupling in Bratteli-Robinson framework, specifying: lattice graph, local algebra A_x = M_n(C) at each site, nearest-neighbor interactions encoding self-modeling coupling through B-M boundaries
- [ ] **LOCL-02**: Establish Lieb-Robinson bounds and effective causal structure from local self-modeling interactions, yielding finite propagation speed v_LR

### Area-Law Derivation

- [ ] **AREA-01**: Prove or strongly argue that local self-modeling interactions produce area-law entanglement entropy S(A) ~ |boundary(A)| for the relevant state, using channel capacity / mutual information route (preferred) or Hastings / Brandao-Horodecki (backup)
- [ ] **AREA-02**: Identify which state of the self-modeling lattice has area-law entanglement -- resolve the "which state?" problem by connecting the self-modeling fixed point to a state satisfying area-law conditions

### Jacobson Application

- [ ] **JACB-01**: Verify that the self-modeling lattice satisfies Jacobson 2016's entanglement equilibrium condition (delta S_EE = 0 for small geodesic balls in the emergent geometry), using the modular Hamiltonian as discrete boost generator
- [ ] **JACB-02**: Derive Einstein's field equations G_ab + Lambda g_ab = (8 pi G) T_ab from self-modeling area-law entropy via Jacobson's 2016 entanglement equilibrium argument, with the continuum limit framed as leading-order IR effective description

### Numerical Verification

- [ ] **NUMR-01**: Verify area-law scaling numerically on small self-modeling lattices (exact diagonalization, N=16-20 qubits / 8-10 M_2(C)^sa sites), distinguishing area vs volume law via linear regression on S(A) vs |boundary(A)| and |volume(A)|

### Paper Assembly

- [ ] **PAPR-01**: Assemble Paper 6 "Spacetime from Self-Modeling" with complete derivation chain (self-modeling locality -> area law -> Jacobson -> Einstein), precise gap identification, and honest framing of assumptions

## Follow-up Requirements

### Extended Analysis

- **LOCL-03**: Derive or justify the lattice topology from self-modeling constraints (address background dependence circularity)
- **AREA-03**: Establish whether the self-modeling fixed point is a pure global state (needed for channel capacity route)
- **JACB-03**: Identify the emergent Newton's constant G = 1/(4 eta) in terms of self-modeling lattice parameters
- **NUMR-02**: Verify entanglement first law delta S = delta <K> on self-modeling lattice
- **NUMR-03**: Construct emergent geometry from mutual information matrix via Cao-Carroll-Michalakis MDS embedding (consistency check)

## Out of Scope

| Topic | Reason |
| ----- | ------ |
| Value of Newton's constant G | Not derivable from this framework without additional input |
| Number of spacetime dimensions | Not derivable; lattice topology is input |
| Standard Model gauge groups | Level 4+ in hierarchy |
| Full quantum gravity theory | Goal is Einstein's equations only, not UV completion |
| Cosmological constant problem | Lambda appears as undetermined constant in Jacobson |
| Rigorous continuum limit | Open problem in quantum gravity; use Wilsonian framing |
| Infinite-dimensional systems | Paper 5 restriction carries forward |

## Accuracy and Validation Criteria

| Requirement | Accuracy Target | Validation Method |
| ----------- | --------------- | ----------------- |
| LOCL-01 | Exact formal definition | Consistency with Bratteli-Robinson framework; Paper 5 algebra per site |
| LOCL-02 | Rigorous bound | Lieb-Robinson velocity computed from interaction Hamiltonian |
| AREA-01 | Strong argument with precise gap identification | Must cite specific theorem or construct specific argument; identify exactly what assumption bridges any gap |
| AREA-02 | Clear identification of state | Must specify which state and why it satisfies area-law conditions |
| JACB-01 | Verification against Jacobson 2016 conditions | Check each condition of arXiv:1505.04753 |
| JACB-02 | Full nonlinear Einstein equations | Must recover G_ab + Lambda g_ab = (8 pi G) T_ab |
| NUMR-01 | Scaling exponent distinguishes area vs volume | R^2 > 0.9 for area-law fit; R^2 < 0.5 for volume-law fit (or vice versa) |
| PAPR-01 | Publication-ready manuscript | Self-contained chain; honest gap framing; all assumptions listed |

## Contract Coverage

| Requirement | Decisive Output / Deliverable | Anchor / Benchmark / Reference | Prior Inputs / Baselines | False Progress To Reject |
| ----------- | ----------------------------- | ------------------------------ | ------------------------ | ------------------------ |
| LOCL-01 | Formal lattice definition with interaction H | Bratteli-Robinson framework | Paper 5 M_n(C)^sa | Lattice defined without specifying how self-modeling constrains coupling |
| LOCL-02 | Lieb-Robinson velocity v_LR | Lieb-Robinson (1972) | -- | Citing LR bounds without computing v_LR for the specific Hamiltonian |
| AREA-01 | Proof/argument that S(A) ~ |boundary(A)| | Hastings (2007), WVCH (2008) | Phase 1 lattice | Citing area-law theorems without checking their hypotheses apply |
| AREA-02 | Identified state with justification | -- (novel) | Phase 1 lattice | Assuming "ground state" without defining the Hamiltonian first |
| JACB-01 | Verification of entanglement equilibrium | Jacobson (2016) arXiv:1505.04753 | Phases 1-2 | Restating Jacobson's conditions without verifying them |
| JACB-02 | Einstein's equations derived | Jacobson (1995, 2016) | Phases 1-3 | Citing Jacobson without connecting to self-modeling |
| NUMR-01 | Area-law scaling data with fit statistics | Known models (Heisenberg, Ising) as benchmark | Phase 1 Hamiltonian | Only checking 1D (must attempt 2D if feasible) |
| PAPR-01 | Paper 6 manuscript | Paper 5 (cited) | All prior phases | Paper that glosses over gaps instead of identifying them precisely |

## Traceability

| Requirement | Phase | Status |
| ----------- | ----- | ------ |
| LOCL-01 | Phase 8 | Pending |
| LOCL-02 | Phase 8 | Pending |
| AREA-01 | Phase 9 | Pending |
| AREA-02 | Phase 9 | Pending |
| JACB-01 | Phase 10 | Pending |
| JACB-02 | Phase 10 | Pending |
| NUMR-01 | Phase 11 | Pending |
| PAPR-01 | Phase 12 | Pending |

**Coverage:**

- Primary requirements: 8 total
- Mapped to phases: 8
- Unmapped: 0

---

_Requirements defined: 2026-03-21_
_Last updated: 2026-03-21 after roadmap creation (Phases 8-12)_
