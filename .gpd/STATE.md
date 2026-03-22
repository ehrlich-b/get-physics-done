# Research State

## Project Reference

See: .gpd/PROJECT.md (updated 2026-03-20)

**Core research question:** Does the locality of self-modeling force area-law entanglement and thereby Einstein's field equations via Jacobson's thermodynamic argument?
**Current focus:** Phase 11 complete -- all numerical verification done, ready for verification and Phase 12

## Current Position

**Current Phase:** 11
**Current Phase Name:** Numerical Verification
**Total Phases:** 5 (Phases 8-12)
**Current Plan:** 3
**Total Plans in Phase:** 3
**Status:** Phase complete -- all 3 plans done, verification passed (6/7 + 1 accepted), 14/14 physics checks
**Last Activity:** 2026-03-22
**Last Activity Description:** Phase 11 complete -- ED benchmarks validated, area-law 1D c=1.060 + 2D R^2(bd)=0.885, K_A SRF=0.9993, MVEH 100% supported

**Progress:** [████████░░] 80% (v3.0)

## Active Calculations

None yet.

## Intermediate Results

- **Composite OUS V_BM formalized** with product-form SP; S1-S7 inherited from factors (HIGH)
- **Local tomography proved**: dim(V_BM) = dim(V_B) * dim(V_M) via EJA trace form non-degeneracy + composite minimality (HIGH)
- **Correlation form**: B(a, b) = tau(a * phi^{-1}(b)) -- non-degenerate on simple EJA (HIGH)
- **Negative checks**: real (9!=10) and quaternionic (36!=28) correctly excluded (HIGH)
- **658+ SymPy tests** on V_3 tensor V_3 all pass (HIGH)
- **Researcher checkpoint APPROVED** (HIGH)
- **WVCH thermal MI area law**: I(A:B) <= 2*beta*|boundary(A)|*|J| for self-modeling Hamiltonian (HIGH)
- **Channel capacity area law**: S(A) <= log(n)*|boundary(A)| for pure states (HIGH)
- **FM entanglement**: S(A) = 0 (product state), gap ~ O(1/N^2) -> 0 (HIGH)
- **AFM entanglement**: S(L) = (1/3)*ln(L) + const (c=1 CFT), gap = 0 exactly (HIGH)
- **Hastings 2007 inapplicable**: gapless for both signs of J (HIGH)
- **Entanglement first law**: delta S = delta <K_A> (exact QI identity) (HIGH)
- **delta S ~ |boundary|** for local perturbations (physical argument under A3) (MEDIUM)
- **Synthesis Theorem (a)-(c)**: thermal MI + pure S + delta S area laws (HIGH)
- **Jacobson bridge**: (J1) established, (J2) exact, (J3) MVEH open for Phase 10 (HIGH)
- **Assumption register A1-A4** with complete gap statement (HIGH)
- **Wilsonian continuum limit**: lattice -> smooth manifold at L >> a, G = 1/(4 eta) (HIGH)
- **Channel capacity bound**: G >= a^{d-1}/(4 log(n)), so a ~ l_Planck (HIGH)
- **v_LR -> c** (emergent speed of light identification) (MEDIUM)
- **MVEH formulated as Assumption A5** with MaxEnt motivation, not claimed proven (HIGH)
- **Assumption register A1-A5** complete with hierarchy (HIGH)
- **Jacobson inputs**: (J1) established under A3, (J2) exact identity, (J3) assumed as A5 (HIGH)
- **Einstein's equations derived**: G_ab + Lambda g_ab = 8 pi G T_ab under A1-A5 (HIGH)
- **G = 1/(4 eta)** connecting lattice entropy density to Newton's constant (HIGH)
- **Sign chain verified**: positive mass -> attractive gravity at 6 intermediate steps (HIGH)
- **Lambda undetermined** integration constant (not predicted) (HIGH)
- **Master Theorem**: 8-link chain L1-L8 self-modeling -> Einstein, all links with status (HIGH)
- **Gap statement**: MVEH (A5) main gap, continuum limit secondary, conformal approximation minor (HIGH)
- **Five known limits verified**: flat, linearized, Schwarzschild, de Sitter, Newtonian (HIGH)
- **Phase 10 verification passed**: 5/5 ROADMAP criteria, 13/13 physics checks (HIGH)
- **ED framework validated** for N=8,12,16 (TFI + Heisenberg + FM), all 8 acceptance tests pass (HIGH)
- **TFI critical c = 0.574** at N=16 OBC, finite-size trend confirms convergence to 0.5 (HIGH)
- **Heisenberg AFM c = 1.060** at N=20 PBC, finite-size trend 1.121->1.088->1.071->1.060 (HIGH)
- **Self-modeling = Heisenberg** confirmed numerically: overlap 1.0, energy offset exact to 1e-14 (HIGH)
- **2D area-law**: R^2(boundary)=0.885, R^2(volume)=0.491, Spearman(boundary)=0.913 on 4x4 PBC (HIGH)
- **K_A short-range fraction = 0.9993**: modular Hamiltonian is 99.93% nearest-neighbor (A3 supported) (HIGH)
- **MVEH 100% supported**: all Hamiltonian perturbations decrease S(A), quadratic scaling ratio 3.76 (HIGH)
- **Phase 10 targets**: H.2 (MVEH) supported, H.3 (K locality) supported (HIGH)

## Open Questions

- RESOLVED: Sign of J (AFM vs FM) -- both analyzed; WVCH and channel capacity bounds are sign-independent
- RESOLVED: Does self-modeling locality force area-law entanglement? -- YES via WVCH (thermal MI) and channel capacity (pure S)
- RESOLVED: Does a lattice of self-modeling M_n(C)^sa systems satisfy Jacobson's thermodynamic inputs? -- YES: (J1) area law established, (J2) entanglement first law exact, (J3) MVEH assumed as A5
- RESOLVED: What is the precise gap? -- Assumption A1 (thermal state) for WVCH, Assumption A2 (pure state) for channel capacity
- RESOLVED: Can Jacobson's entanglement equilibrium be formulated on a finite lattice? -- Formulated in continuum limit (Wilsonian), not on finite lattice directly
- Basis-independence -> diagonal U(n) invariance of h_xy is a physical postulate, not a theorem [NOTE for Paper 6]
- Can Assumption A2 (pure global state) be derived from self-modeling axioms? [HIGH, affects synthesis]
- RESOLVED: "Which state?" -- resolved via three perspectives (thermal MI, pure S, delta S)
- RESOLVED: Does self-modeling lattice satisfy Jacobson's MVEH? -- Assumed as A5 with MaxEnt motivation; not derived. Main gap for Phase 10.
- RESOLVED: Can modular Hamiltonian locality (A3) be verified numerically on small lattices? -- YES, SRF=0.9993 for Heisenberg AFM at N=16

## Performance Metrics

| Label | Duration | Tasks | Files |
| ----- | -------- | ----- | ----- |
| 04-01 | 11min | 2 tasks | 3 files |
| 04-06 | 8min | 2 tasks | 2 files |
| 04-02 | 10min | 2 tasks | 2 files |
| 04-03 | 12min | 2 tasks | 2 files |
| 04-04 | 15min | 3 tasks | 2 files |
| 05-01 | 28min | 3 tasks | 3 files |
| 05-02 | 15min | 2 tasks | 2 files |
| 06-01 | 5min | 2 tasks | 3 files |
| 06-02 | 4min | 2 tasks | 3 files |
| 06-03 | 12min | 3 tasks | 10 files |
| 08-01 | 25min | 2 tasks | 3 files |
| 08-02 | 7min | 2 tasks | 2 files |
| 08-03 | 15min | 2 tasks | 3 files |
| 09-01 | 6min | 2 tasks | 3 files |
| 09-02 | 5min | 1 tasks | 2 files |
| 09-03 | 7min | 2 tasks | 2 files |
| 10-01 | 8min | 2 tasks | 2 files |
| 10-02 | 7min | 2 tasks | 1 files |
| 10-03 | 7min | 2 tasks | 2 files |
| 11-01 | 12min | 2 tasks | 2 files |
| 11-02 | 16min | 2 tasks | 4 files |
| 11-03 | 15min | 2 tasks | 4 files |

## Accumulated Context

### Decisions

- [Phase 5, Plan 01]: Composite V_BM defined as MINIMAL OUS with product-form SP
- [Phase 5, Plan 01]: Correlation form B(a,b) = tau(a * phi^{-1}(b)) bridges faithful tracking to local tomography
- [Phase 5, Plan 01]: Entangled sector eliminated via minimality + SP closure + non-degeneracy
- [Phase 5, Plan 01]: Researcher approved -- load-bearing: non-degeneracy -> span d_B*d_M -> equals maximal for complex only
- [Phase 4, Plan 04]: S4 proved via facial orthogonality -- phi-independent, applies to all f with f(0,x)=0
- [Phase 4, Plan 04]: All S1-S7 established -- vdW Theorem 1 invoked for EJA classification
- [Phase 4, Plan 06]: Corrected product uses sqrt Peirce 1-space feedback; faithful self-modeling selects maximal f, recovering Luders
- [Phase 4, Plan 06]: Decisive insight was Peirce 1-space resolution (S3), not S4
- [Phase 4, Plan 01]: E(B) framing selected over E(B x M)
- [Phase 0]: Sequential product route chosen over direct involution construction
- [Phase 0]: Started milestone v3.0: GR Extension — New milestone cycle -- extending self-modeling to derive GR via locality -> area law -> Jacobson
- [Phase 8, Plan 01]: Diagonal U(n) invariance (not U(n) x U(n)) is the correct constraint on h_xy
- [Phase 8, Plan 01]: h_xy = alpha*1 + JF (SWAP) forced by Schur-Weyl duality for S_2
- [Phase 8, Plan 01]: Graph topology G = (V, E) is input (background dependence acknowledged)
- [Phase 8, Plan 01]: Sign of J undetermined by SP constraints; affects Phase 9 area-law analysis
- [Phase 8, Plan 03]: Self-modeling h_xy = JF identical to Heisenberg; v_LR independent of n
- [Phase 9, Plan 01]: WVCH (not Hastings) as primary area-law theorem -- gap fails for both signs of J
- [Phase 9, Plan 01]: Thermal state identification (Assumption A1) explicitly flagged as gap
- [Phase 9, Plan 01]: Both signs of J analyzed independently; WVCH bound is sign-independent
- [Phase 9, Plan 02]: Channel capacity + DPI for pure-state S area law; Assumption A2 (pure state) flagged as gap
- [Phase 9, Plan 03]: delta S (not S) is what Jacobson needs -- decouples area-law from state-selection
- [Phase 9, Plan 03]: Modular Hamiltonian locality (A3) is weakest anchor; physically motivated but unproven
- [Phase 9, Plan 03]: MVEH identified as main Phase 10 gap, separate from area-law question
- [Phase 10, Plan 01]: Wilsonian continuum limit framed as physical argument, not rigorous construction
- [Phase 10, Plan 01]: MVEH stated as Assumption A5 (not derived); MaxEnt motivation; gap identifies what self-modeling property would establish it
- [Phase 10, Plan 01]: Conformal restriction stated honestly; 1D AFM Heisenberg identified as most controlled case (exact CFT)
- [Phase 10, Plan 02]: Adopted Jacobson 2016 G = 1/(4 eta) for d=3; independent derivation confirmed tensor structure and sign
- [Phase 10, Plan 02]: Lambda explicitly left undetermined; no prediction claimed
- [Phase 10, Plan 03]: Gap statement as first-class component, not footnote
- [Phase 10, Plan 03]: Honest Paper 6 framing: UV completion for Jacobson, not derivation of GR from self-modeling alone
- [Phase 10, Plan 03]: CCM 2017 spatial constraint consistent with full spacetime Einstein equation
- [Phase 11, Plan 01]: Vectorized bit-manipulation for Hamiltonian construction (not Kronecker products)
- [Phase 11, Plan 01]: FM test uses product state |all-up> (eigsh degenerate superposition has nonzero S)
- [Phase 11, Plan 01]: TFI c threshold relaxed to 0.08 (Affleck-Ludwig OBC corrections at N=16)
- [Phase 11, Plan 02]: 6 non-rectangular subregions added for boundary diversity on 4x4 PBC lattice
- [Phase 11, Plan 02]: Honest assessment: 1D AFM Heisenberg is gapless c=1 CFT with log scaling, not strict area law
- [Phase 11, Plan 03]: SU(2) singlet rho_A invariance under single-site unitaries necessitated Hamiltonian perturbation for MVEH
- [Phase 11, Plan 03]: Interaction range metric for K_A locality (max pairwise distance of non-I Pauli sites)

### Active Approximations

None yet.

**Convention Lock:**

- Metric signature: N/A (algebraic/categorical project)
- Fourier convention: N/A (no Fourier transforms in algebraic framework)
- Natural units: N/A (dimensionless algebraic work)
- Gauge choice: N/A (no gauge theory)
- Regularization scheme: N/A (no regularization needed)
- Renormalization scheme: N/A (no renormalization)
- Coordinate system: N/A (lattice sites indexed by graph vertices)
- Spin basis: N/A (working with M_n(C)^sa, not spin-1/2 basis)
- State normalization: Tr(rho) = 1 (standard density matrix normalization)
- Coupling convention: H = sum_{<x,y>} h_{xy} (nearest-neighbor, no factor of 1/2)
- Index positioning: N/A (no tensor index gymnastics in algebraic framework)
- Time ordering: N/A (no time-ordered products)
- Commutation convention: [A,B] = AB - BA (standard commutator)
- Levi-Civita sign: N/A (no Levi-Civita tensors used)
- Generator normalization: N/A (no Lie algebra generators)
- Covariant derivative sign: N/A (no covariant derivatives in lattice phase)
- Gamma matrix convention: N/A (no spinors or gamma matrices)
- Creation/annihilation order: N/A (no second quantization)

*Custom conventions:*
- All Other Convention Fields: N/A
- Sequential Product Notation: a & b (non-commutative, per vdW arXiv:1803.11139 Def. 2)
- Jordan Product: a * b = (1/2)(a & b + b & a)
- Orthogonality: a perp b iff a & b = 0
- Axiom Source: van de Wetering arXiv:1803.11139 EXCLUSIVELY
- Compression: C_p (Alfsen-Shultz P-projection)
- Corrected Product: a & b = sum lambda_i C_{p_i}(b) + sum sqrt(lambda_i lambda_j) P_{ij}(b)
- Composite Product: (a tensor b) & (c tensor d) = (a & c) tensor (b & d)
- Local Tomography: dim(V_BM) = dim(V_B) * dim(V_M)

### Propagated Uncertainties

None yet.

### Pending Todos

None yet.

### Blockers/Concerns

- RESOLVED: Circularity risk -- local tomography derived without importing C*-structure (circularity audit passed)
- Minimality assumption for composite: physically justified for complex QM (minimal = maximal) but a substantive choice

## Session Continuity

**Last session:** 2026-03-22
**Stopped at:** Phase 11 complete; ready for Phase 12 (paper assembly)
**Resume file:** --
