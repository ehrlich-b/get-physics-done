# Experiential Measure on Structure Space

## What This Is

Deriving the fundamental laws of physics from the algebraic structure of self-modeling composite processes. v1.0 formalized the experiential measure framework. v2.0 derived QM from a single operational premise: self-modeling forces M_n(C)^sa with Luders product and conjugate-transpose involution (Paper 5, three rounds of adversarial review passed). v3.0 extends to gravity: self-modeling is inherently local (the model probes through the B-M boundary), locality forces area-law entanglement, and Jacobson's thermodynamic argument converts area-law entropy to Einstein's field equations. The subfield is mathematical physics / quantum foundations / quantum gravity, with the expected deliverable being Paper 6 deriving GR from self-modeling.

## Core Research Question

Does the locality of self-modeling -- the fact that the model probes the body through the boundary, not telepathically through the bulk -- force area-law entanglement and thereby Einstein's field equations via Jacobson's thermodynamic argument?

## Current Milestone: v3.0 GR Extension

**Goal:** Derive Einstein's field equations from the locality of self-modeling, via the chain: local self-modeling lattice -> area-law entanglement -> Jacobson's thermodynamic derivation -> GR.

**Target results:**

- Formalization of locality of self-modeling for spatially extended systems (lattice of M_n(C)^sa sites)
- Proof or strong argument that local self-modeling implies area-law entanglement entropy
- Verification that Jacobson's inputs (area-law S, Clausius relation, Unruh temperature) are satisfied
- Paper 6 assembling the chain with precise gap identification

## Scoping Contract Summary

### Contract Coverage

- **Locality formalization (claim-locality):** Make precise what "self-modeling is local" means for a lattice of self-modeling systems, each site an M_n(C)^sa from Paper 5
- **Area law (claim-area-law):** Prove or give strong argument that local self-modeling interactions produce area-law entanglement entropy S(A) ~ |boundary(A)|
- **Jacobson application (claim-jacobson):** Verify that the self-modeling composite satisfies Jacobson's three inputs (area-law S, Clausius at Rindler horizons, Unruh temperature)
- **Paper assembly (claim-paper-6):** Paper 6 "Spacetime from Self-Modeling" with complete chain and precise gap identification
- **False progress to reject:** Hand-waving the locality -> area law step without identifying what assumption bridges any gap; citing area-law theorems without checking their hypotheses apply to self-modeling systems

### User Guidance To Preserve

- **User-stated observables:** Whether locality -> area law holds; what exact assumption bridges any gap between self-modeling locality and existing area-law theorems
- **User-stated deliverables:** Paper 6 (standalone, separate from Paper 5)
- **User-stated architecture:** Lattice of self-modeling systems (option b), with note that tensor decomposition of large M_N(C)^sa (option a) is equivalent
- **Must-have references / prior outputs:** Paper 5 results (M_n(C)^sa, local tomography, composite structure), Jacobson (1995), Hastings (2007), Cao-Carroll-Michalakis (2017)
- **Stop / rethink conditions:** If "locality" in the self-modeling sense doesn't map onto "locality" in the lattice Hamiltonian sense; if no area-law argument (rigorous or strong physical) can be made

### Scope Boundaries

**In scope**

- Formalize locality of self-modeling for spatially extended systems
- Derive or argue area-law entanglement from local self-modeling
- Apply Jacobson's thermodynamic argument to get Einstein's equations
- Identify emergent geometry (bonus, if steps 1-3 work)
- Paper 6 assembly

**Out of scope**

- Deriving the specific value of G (Newton's constant)
- Deriving 3+1 dimensions
- Deriving Standard Model gauge groups
- Full quantum gravity theory
- Cosmological constant problem
- Infinite-dimensional systems (Paper 5 restriction carries forward)

### Active Anchor Registry

- **ref-jacobson1995:** Jacobson -- Thermodynamics of Spacetime: The Einstein Equation of State (1995, PRL 75, 1260)
  - Why it matters: The key theorem -- area-law entropy + Clausius relation + Unruh temperature = Einstein's equations
  - Carry forward: planning, execution, verification, writing
  - Required action: read, cite

- **ref-hastings2007:** Hastings -- An area law for one-dimensional quantum systems (2007, JSTAT P08024)
  - Why it matters: Rigorous area law for 1D gapped Hamiltonians; template for higher-D arguments
  - Carry forward: planning, execution, writing
  - Required action: read, cite

- **ref-ccm2017:** Cao, Carroll, Michalakis -- Space from Hilbert space (2017, PRD 95, 024031)
  - Why it matters: Emergent geometry from entanglement in finite Hilbert spaces; closest existing framework to our lattice approach
  - Carry forward: planning, execution, writing
  - Required action: read, cite

- **ref-vanraamsdonk2010:** Van Raamsdonk -- Building up spacetime with quantum entanglement (2010, GRG 42, 2323)
  - Why it matters: Entanglement = geometric connectivity; conceptual foundation for emergent geometry
  - Carry forward: writing
  - Required action: cite

- **ref-lmvr2014:** Lashkari, McDermott, Van Raamsdonk -- Gravitational dynamics from entanglement (2014, JHEP 04, 195)
  - Why it matters: First law of entanglement entropy = linearized Einstein's equations
  - Carry forward: planning, execution, writing
  - Required action: read, cite

- **ref-faulkner2014:** Faulkner et al. -- Gravitation from entanglement in holographic CFTs (2014, JHEP 03, 051)
  - Why it matters: Nonlinear Einstein's equations from entanglement
  - Carry forward: execution, writing
  - Required action: read, cite

- **ref-paper5:** Paper 5 (this project, v2.0) -- QM from self-modeling
  - Why it matters: Provides the M_n(C)^sa algebra, local tomography, and composite structure that are inputs to v3.0
  - Carry forward: planning, execution, verification, writing
  - Required action: cite

### Carry-Forward Inputs

- Paper 5 results: M_n(C)^sa with Luders product, local tomography, composite OUS framework
- paper/sections/*.tex (Paper 5 section files)
- paper/GR_EXTENSION.md (v3.0 research plan)
- v1.0 papers (Theorem A, Lipschitz, Born-Fisher falsification)

### Skeptical Review

- **Weakest anchor:** The locality -> area law step. Self-modeling locality is a statement about B-M boundary interactions; area-law theorems (Hastings) require gapped local Hamiltonians. The bridge between these two notions of locality is the critical gap.
- **Unvalidated assumptions:** That a lattice of self-modeling systems produces a "ground state" or low-energy state to which area-law theorems apply; that the Clausius relation holds at causal horizons in the self-modeling framework
- **Competing explanation:** Area-law entanglement might require additional dynamical assumptions beyond locality (e.g., a spectral gap, specific interaction structure) that self-modeling alone doesn't provide
- **Disconfirming observation:** Self-modeling locality doesn't produce correlation decay; or the resulting entropy scaling is volume-law, not area-law
- **False progress to reject:** Citing area-law theorems without verifying their hypotheses apply; arguing "locality implies area law" without identifying the precise mathematical connection

### Open Contract Questions

- Does self-modeling locality map onto lattice Hamiltonian locality?
- Does the self-modeling fixed point correspond to a gapped ground state?
- Can area-law entanglement be derived purely information-theoretically, bypassing Hamiltonian assumptions?
- Does the Unruh effect hold in the M_n(C)^sa framework (finite dimensions)?

## Research Questions

### Answered

- [x] Can the 7 lemmas in Theorem A's dependency graph be assembled into a self-contained proof with explicit error scaling? -- **YES.** Proof assembled with composite error rate gamma = min(alpha/2, Ds - alpha). Validated on three-state chain across 9 parameter combinations. -- v1.0
- [x] Is the experiential density rho Lipschitz continuous in the transition kernel, and what is the constant L? -- **YES.** L = (C_I + C_H)/gap(P), scaling as ln|Omega|/gap. Verified numerically: 3000 perturbations, zero violations. -- v1.0
- [x] Do Born-rule distributions satisfy I_vN(B;M) = S_vN(B)/2 in a toy qubit composite process? -- **NO. Conjecture FALSIFIED.** rho_Q <= 0 throughout all 1900+ Lindblad trajectories; mu_Q identically zero. -- v1.0
- [x] Does the self-modeling sequential product satisfy van de Wetering's axioms S1-S7? -- **YES.** All seven axioms proved for the corrected product on finite-dim spectral OUS. S4 proved via facial orthogonality (phi-independent). -- v2.0
- [x] Does S4 (symmetry of orthogonality) hold for the self-modeling construction? -- **YES.** Proved via facial orthogonality argument; holds for all mixing functions f with f(0,x)=0. -- v2.0
- [x] Does B-M compositionality (independent accessibility) imply local tomography? -- **YES.** Proved via state separation on minimal composite OUS. dim(V_BM) = dim(V_B) * dim(V_M). -- v2.0
- [x] Which effect algebra framing is correct for the self-modeling sequential product? -- **E(B).** E(B x M) framing fails in three ways; E(B) framing gives correct corrected product formula. -- v2.0

### Active

- [ ] Does self-modeling locality force area-law entanglement entropy?
- [ ] Does a lattice of self-modeling M_n(C)^sa systems satisfy Jacobson's thermodynamic inputs?
- [ ] What is the precise gap (if any) between self-modeling locality and existing area-law theorems?
- [ ] Can Einstein's field equations be derived from self-modeling without additional dynamical assumptions?

### Out of Scope

- Countable/continuous state space generalization -- paper-length work, deferred
- Non-Markovian quantum channels -- could produce rho_Q > 0 regime, untested
- Non-equilibrium extension -- requires different mathematical framework
- Reference measure nu -- shared open problem with Mueller (2020)
- Standard Model derivation -- Level 4+, far beyond current scope
- Self-modeling constants experiment -- Level 6, requires experimental apparatus
- Value of Newton's constant G -- not derivable from this framework
- Number of spacetime dimensions -- not derivable from this framework

## Research Context

### Physical System

A lattice of self-modeling composite processes, each site carrying an M_n(C)^sa algebra (from Paper 5). Nearest-neighbor sites interact through body-model boundaries: site A's model of site B is updated through the shared boundary. Information between distant sites must propagate through intermediaries. The global state of the lattice has entanglement structure determined by these local interactions.

### Theoretical Framework

Quantum foundations / quantum gravity / thermodynamic gravity: algebraic quantum theory (from Paper 5), entanglement entropy and area laws, Jacobson's thermodynamic derivation of Einstein's equations, emergent geometry from entanglement (Van Raamsdonk program). Key tools: Hastings' area law, Rindler horizon thermodynamics, Unruh effect, Fisher information metric.

### Key Parameters and Scales

| Parameter | Symbol | Regime | Notes |
| --------- | ------ | ------ | ----- |
| Local algebra dimension | n | Finite | Each lattice site is M_n(C)^sa |
| Lattice size | N | Large | Number of self-modeling sites |
| Entanglement entropy | S(A) | To be determined | Should scale as |boundary(A)| |
| Spectral gap | Delta | To be determined | Needed for Hastings-type area law |

### Known Results

- v2.0: Self-modeling forces M_n(C)^sa with Luders product and conjugate-transpose involution (Paper 5)
- v2.0: Local tomography for B-M composite; all non-complex EJA types excluded
- Jacobson (1995): Area-law S + Clausius + Unruh = Einstein's equations (published theorem)
- Hastings (2007): Area law for 1D gapped local Hamiltonians (rigorous)
- Cao-Carroll-Michalakis (2017): Emergent geometry from entanglement in finite Hilbert spaces
- Lashkari-McDermott-Van Raamsdonk (2014): First law of entanglement entropy = linearized Einstein

### What Is New

Connecting self-modeling's inherent locality (the model probes through the boundary, not the bulk) to area-law entanglement and thereby to Einstein's equations. No prior work has derived GR from self-modeling. If successful, both QM (Paper 5) and GR (Paper 6) follow from a single operational premise with no additional assumptions.

### Target Venue

Foundations of physics / quantum gravity journal (same tier as Paper 5). Possibly Physical Review D for the gravity content.

### Computational Environment

Local workstation. Primarily conceptual/proof work. Python for any verification calculations.

## Notation and Conventions

See `.gpd/CONVENTIONS.md` for all notation and sign conventions.
See `.gpd/NOTATION_GLOSSARY.md` for symbol definitions.

## Unit System

Natural units (hbar = c = k_B = 1) for the GR/thermodynamic portions. Dimensionless for algebraic portions (Paper 5 framework).

## Requirements

See `.gpd/REQUIREMENTS.md` for the detailed requirements specification.

## Key References

- Jacobson (1995), PRL 75, 1260 -- Einstein equation as equation of state
- Hastings (2007), JSTAT P08024 -- Area law for 1D gapped systems
- Cao, Carroll, Michalakis (2017), PRD 95, 024031 -- Space from Hilbert space
- Van Raamsdonk (2010), GRG 42, 2323 -- Spacetime from entanglement
- Lashkari, McDermott, Van Raamsdonk (2014), JHEP 04, 195 -- Gravitational dynamics from entanglement
- Faulkner et al. (2014), JHEP 03, 051 -- Nonlinear Einstein from entanglement
- Swingle (2012), PRD 86, 065007 -- MERA and AdS/CFT
- Paper 5 (this project, v2.0) -- QM from self-modeling

## Constraints

- **Finite dimensions:** All proofs for finite-dimensional systems only (Paper 5 restriction)
- **Argument quality:** Strong physical argument with precise gap identification; not full theorem, not bare conditional
- **Paper 5 as input:** Takes M_n(C)^sa, local tomography, and composite structure as established results
- **No new QM assumptions:** GR must follow from self-modeling locality alone, not from additional physical postulates

## Key Decisions

| Decision | Rationale | Outcome |
| -------- | --------- | ------- |
| Clean composition over full explicit constants | User prefers self-contained proof with error scaling; constants in appendix | Good -- proof is self-contained |
| Qubit falsification over variational structure | Decisive test first; if it fails, variational work is moot | Good -- conjecture falsified, saved wasted effort |
| Lipschitz over countable extension | Needed for approximate factorization; countable extension is paper-length | Good -- Lipschitz bound proven with explicit constants |
| Deep-theory model profile | Heavy proof work benefits from tier-1 models | Good -- all proofs completed |
| 3 standalone papers over single monograph | Papers written independently for different audiences | Revisit -- peer review suggests Paper 2 may be better as section of Paper 1 |
| Honest framing over cosmological claims | Peer review flagged overclaiming; reframed titles and abstracts | Good -- papers now accurately scope their claims |
| Sequential product route over direct involution construction | van de Wetering axioms give cleaner path; D'Ariano as backup | Good -- S1-S7 all proved, backup not needed |
| Explore both effect algebra framings | Correct framing is a Phase 1 result, not a premise | Good -- E(B) selected, E(B x M) failure documented |
| Lattice architecture for GR extension | Connects directly to Hastings area-law machinery; Cao-Carroll-Michalakis precedent | Pending |
| Strong argument over full theorem | First pass; full theorem too ambitious; bare conditional too weak | Pending |
| Standalone Paper 6 over Paper 5 extension | Clean conceptual separation: Paper 5 = QM, Paper 6 = GR | Pending |

## v1.0 Summary (complete)

All three formal gaps in the experiential measure framework are closed:
1. **Theorem A** assembled from 7 metastability lemmas with explicit error composition
2. **Lipschitz stability** proven with L = (C_I + C_H)/gap(P), verified numerically
3. **Born-Fisher conjecture falsified** -- rho_Q <= 0 for all exchange-plus-dephasing Lindblad dynamics (proved analytically)

Three papers written, peer-reviewed (18-agent 6-pass panel), and revised.

## v2.0 Summary (complete)

QM derived from a single operational premise (faithful self-modeling):
1. **Sequential product formalized** on finite-dim spectral OUS; corrected product with Peirce 1-space feedback
2. **S1-S7 all proved** -- S4 via facial orthogonality (phi-independent); functional form f = sqrt(xy) forced by S5 + S2
3. **Local tomography proved** from faithful tracking via state separation on minimal composite
4. **Type exclusion** -- all non-complex EJA types excluded by dimension counting + Barnum-Wilce
5. **C*-algebra promotion** via vdW Theorem 3; involution = conjugate transpose

Paper 5 assembled, passed three rounds of adversarial review. Chain: L4 -> SP -> EJA -> LT -> type exclusion -> C*-algebra -> M_n(C)^sa.

---

_Last updated: 2026-03-21 after v3.0 milestone initialization_
