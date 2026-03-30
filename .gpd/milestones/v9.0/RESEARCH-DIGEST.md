# Research Digest: v9.0 Continuum Limit from Finite-Dimensional Observer

Generated: 2026-03-30
Milestone: v9.0
Phases: 32-36

## Narrative Arc

The v9.0 milestone tackled the principal open problem of the self-modeling program: can a finite-dimensional observer necessarily see smooth effective geometry? Starting from the quantum Fisher information metric on reduced states of the Heisenberg/SWAP ground state (Phase 32), the investigation established smoothness and positive-definiteness at finite N but discovered that distance recovery fails in 1D (FISH-03). Phase 33 rescued this failure for d>=2 by showing that Neel long-range order, through sublattice alternation, keeps the Fisher metric bounded away from zero -- the CORR-03 conditional theorem with four explicit hypotheses. The NL sigma model effective theory (c_s = 1.659 Ja, QMC to 0.3%) provided the bridge to Phase 34's derivation of emergent Lorentz invariance via isotropy (RG irrelevance) and DLS reflection positivity, resolving the velocity hierarchy (c_eff = c_s, not v_LR). Phase 35 derived local equilibrium from the Bisognano-Wichmann theorem, obtaining KMS at beta=2pi (not assumed), Unruh temperature T_U = a/(2pi), and the Jacobson inputs J1-J3. Phase 36 assembled the complete six-link derivation chain from finite-dimensional observer to Einstein equations and scored each of the four Paper 6 gaps individually, arriving at the milestone verdict: the chain is conditionally complete for d>=3.

## Key Results

| Phase | Result | Equation / Value | Validity Range | Confidence |
| ----- | ------ | ---------------- | -------------- | ---------- |
| 32 | FISH-01: Smoothness of rho_Lambda(x) | Eq. 32.8 (Hastings-Koma) | Gapped, finite N | HIGH |
| 32 | FISH-02: Positive-definiteness of SLD Fisher | derivations/32, Thm 2 | Interior points, OBC | HIGH |
| 32 | FISH-03: Distance recovery fails in 1D | g_bulk ~ N^{-2.75} (Eq. 32.12) | 1D Heisenberg chain | HIGH (negative) |
| 33 | CORR-02: O(3) NL sigma model | c_s = 1.659 Ja (Eq. 33.11/33.14) | d>=2 Neel, S=1/2 | HIGH (QMC 0.3%) |
| 33 | CORR-03: Conditional Fisher smoothness | g_F = O(m_s^2) > 0 (Eq. 33.18/33.19) | d>=2 Neel, H1-H4 | MEDIUM-HIGH |
| 33 | 2D ED: Neel rescue | m_s^2 = 0.233, g_plaq = 4.76e-4 | 4x4 OBC, S=1/2 | MEDIUM |
| 34 | LRNZ-01: Isotropy | alpha_4 RG irrelevant (rho~2) | Lattice -> continuum | HIGH |
| 34 | LRNZ-02: Emergent Lorentz | ds^2 = -c_s^2 dt^2 + g_ij dx^i dx^j (Eq. 34.9/34.16) | Sigma model EFT | MEDIUM-HIGH |
| 34 | Velocity hierarchy | v_LR/c_s = 7.63, c_eff = c_s | 1D; universal ratio expected | HIGH |
| 35 | BWEQ-01: Lattice-BW | H_ent = (2pi/c_s) sum h_x (Eq. 35.1), SRF=0.9993 | Lattice, numerical | MEDIUM-HIGH |
| 35 | BWEQ-02: KMS derived | beta = 2pi from BW + Tomita-Takesaki | Once BW accepted | HIGH |
| 35 | J1-J3 packaged | K_A=2pi K_boost, theta=sigma=0, T_U=a/(2pi) | Eqs. 35.0a, 35.19, 35.3 | HIGH |
| 36 | Gap A score | NARROWED (d>=3) / CONDITIONAL (d=2) / OPEN (d=1) | Dimension-dependent | HIGH |
| 36 | Gap B score | CLOSED (d=1 Route A) / OPEN (d>=2) / N/A (Route B) | Route-dependent | HIGH |
| 36 | Gaps C, D scores | CONDITIONAL | Both routes | MEDIUM-HIGH |
| 36 | Overall verdict | Chain conditionally complete for d>=3 | All 6 links | HIGH |

## Methods Employed

- **Phase 32:** Exact diagonalization of Heisenberg Hamiltonian (OBC), SLD Fisher metric computation via spectral decomposition, Hastings-Koma exponential decay bounds
- **Phase 33:** Two-tier correlation analysis (gapped + Neel), O(3) NL sigma model derivation from coherent state path integral, 2D exact diagonalization (4x4 OBC), conditional theorem construction (H1-H4)
- **Phase 34:** RG irrelevance analysis (Hasenbusch exponents), Wick rotation via DLS reflection positivity, von Ignatowsky's theorem (supporting route), Lieb-Robinson velocity computation
- **Phase 35:** Wightman axiom verification (W1-W6), lattice Bisognano-Wichmann (Giudici et al.), Tomita-Takesaki modular theory, KMS state derivation, Killing equation analysis
- **Phase 36:** Chain assembly with equation-level citation, gap scoring rubric (CLOSED/NARROWED/CONDITIONAL/OPEN), Route A/B comparative analysis

## Convention Evolution

| Phase | Convention | Description | Status |
| ----- | ---------- | ----------- | ------ |
| 32 | metric_signature | (+,...,+) Riemannian for Fisher spatial metric | Active |
| 32 | fisher_metric | SLD, g_F = 4 g_Bures | Active |
| 33 | coupling | J > 0 antiferromagnetic | Active |
| 34 | emergent_speed | c = c_s = 1.659 Ja (NOT v_LR) | Active |
| 34 | spacetime_metric | (-,+,...,+) Lorentzian for emergent spacetime | Active |
| 35 | modular_hamiltonian | K_A = -ln(rho_A), rho_A = e^{-K_A}/Z | Active |
| 35 | kms_temperature | beta = 2pi for Rindler wedge | Active |
| All | natural_units | hbar=1, k_B=1, a=1 | Active |

## Figures and Data Registry

| File | Phase | Description | Paper-ready? |
| ---- | ----- | ----------- | ------------ |
| derivations/32-fisher-geometry-theorems.md | 32 | FISH-01/02/03 theorem statements and proofs | Yes (derivation) |
| derivations/33-correlation-decay-and-sigma-model.md | 33 | CORR-01/02 two-tier decay + sigma model | Yes (derivation) |
| derivations/33-fisher-smoothness-algebraic-decay.md | 33 | CORR-03 conditional theorem | Yes (derivation) |
| derivations/34-emergent-lorentz-invariance.md | 34 | LRNZ-01/02 isotropy + Lorentz | Yes (derivation) |
| derivations/34-velocity-hierarchy-and-causal-structure.md | 34 | Velocity hierarchy + metric assembly | Yes (derivation) |
| derivations/35-bw-axioms-and-lattice-bw.md | 35 | BWEQ-01 Wightman + lattice-BW | Yes (derivation) |
| derivations/35-kms-equilibrium-and-modular-hamiltonian.md | 35 | BWEQ-02 KMS + Unruh + equilibrium | Yes (derivation) |
| derivations/36-derivation-chain.md | 36 | Complete 6-link chain assembly | Yes (main document) |
| derivations/36-gap-scorecards.md | 36 | Four gap scorecards + honest assessment | Yes (assessment) |

## Open Questions

1. Rigorous continuum limit of Fisher geometry for d>=2 (N->infinity)
2. Proof that sigma model is the correct continuum description of SWAP lattice (universality)
3. Rigorous Neel order for S=1/2 d=2 (only QMC evidence exists)
4. Conformal modular Hamiltonian in d>=2 (Route A Gap B)
5. Proof of tensoriality assumption (Route B Gap C)
6. Existence and uniqueness of geometry-defining state (Gap D / MVEH)
7. Resolution of Sorce 2024 caveat for geometric modular flow in d>=2
8. Why does the Peirce-derived spin(9) differ from Krasnov's spin(9)?
9. Can the choice of u in S^6 be derived from self-modeling framework?

## Dependency Graph

    Phase 32 "Fisher Geometry on Reduced States"
      provides: FISH-01 (smoothness), FISH-02 (positive-definiteness), FISH-03 (1D failure)
      requires: --
    -> Phase 33 "Correlation Structure and Effective Theory"
      provides: CORR-01 (two-tier decay), CORR-02 (sigma model), CORR-03 (conditional smoothness)
      requires: FISH-01/02/03
    -> Phase 34 "Emergent Lorentz Invariance"
      provides: LRNZ-01 (isotropy), LRNZ-02 (Lorentz), velocity hierarchy, metric assembly
      requires: CORR-02 (sigma model)
    -> Phase 35 "BW Theorem and Local Equilibrium"
      provides: BWEQ-01 (lattice-BW), BWEQ-02 (KMS, Unruh, equilibrium), J1-J3
      requires: LRNZ-02 (Lorentz invariance, no circularity)
    -> Phase 36 "Assembly and Gap Scoring"
      provides: Complete chain, gap scores, honest assessment
      requires: All prior phases (32-35)

## Mapping to Original Objectives

| Requirement | Status | Fulfilled by | Key Result |
|-------------|--------|-------------|------------|
| claim-fisher (Fisher metric smooth, positive-definite) | Complete | Phase 32 | FISH-01/02 proved at finite N |
| claim-decay (correlation structure characterized) | Complete | Phase 33 | Two-tier decay + sigma model |
| claim-lorentz (emergent Lorentz invariance) | Complete | Phase 34 | LRNZ-01/02 + velocity hierarchy |
| BW + local equilibrium | Complete | Phase 35 | KMS derived, J1-J3 packaged |
| Acceptance signal (complete chain, gaps scored) | Complete | Phase 36 | Chain assembled, 4 gaps scored individually |
| claim-continuum (smooth effective geometry) | Partial | Phases 32-36 | NARROWED for d>=3, not CLOSED -- effective smoothness proved, constructive limit open |
