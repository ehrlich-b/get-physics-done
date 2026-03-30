# Research State

## Project Reference

See: .gpd/PROJECT.md (updated 2026-03-29)

**Core research question:** Can the Standard Model + GR be derived from the requirement that a composite system faithfully models itself?
**Current focus:** v9.0 Continuum Limit from Finite-Dimensional Observer

## Current Position

**Current Phase:** 36
**Current Phase Name:** Assembly and Gap Scoring
**Total Phases:** 36 (31 prior + 5 new in v9.0)
**Current Plan:** 02/02 complete
**Total Plans in Phase:** 2
**Status:** Milestone complete
**Last Activity:** 2026-03-30
**Last Activity Description:** v9.0 milestone completed and archived


## Active Calculations

- ASBL-01: Chain assembly -- COMPLETE (six links (a)-(f), J1-J8 mapped, dimension table, assumption register)
- ASBL-02: Gap scoring -- COMPLETE (A: NARROWED d>=3/CONDITIONAL d=2/OPEN d=1; B: CLOSED d=1 Route A/OPEN d>=2; C: CONDITIONAL; D: CONDITIONAL)

## Intermediate Results

### Phase 36 Results (v9.0)

- **ASBL-01 (Chain assembly)**: Six-link chain (a)-(f) from finite-dim observer to Einstein equations. Every link cites Phase 32-35 equations. No re-derivation. Rigor taxonomy applied: RIGOROUS/CONDITIONAL/PHYSICAL ARGUMENT/ASSUMED. (HIGH)
- **ASBL-01 (J1-J8 mapping)**: All 8 Jacobson 2016 inputs mapped to chain sources with status. J1-J3 from Phase 35, J4 from Phases 32-34, J5 from Paper 6, J6-J7 standard, J8 Route B only. (HIGH)
- **ASBL-01 (Dimension table)**: Chain status dimension-dependent: d=1 FAILS (FISH-03 + trivial Einstein), d=2 CONDITIONAL (log corrections, Neel QMC only), d>=3 CONDITIONAL (strongest case). (HIGH)
- **ASBL-02 (Gap A)**: Continuum Limit -- NARROWED (d>=3), CONDITIONAL (d=2), OPEN (d=1). Key: CORR-03 conditional theorem narrowed from vague gap to 4 explicit hypotheses. (HIGH)
- **ASBL-02 (Gap B)**: Conformal Approx -- CLOSED (d=1 Route A, exact CFT), OPEN (d>=2 Route A), N/A (Route B via Lovelock). Routes A/B complementary. (HIGH)
- **ASBL-02 (Gap C)**: Tensoriality -- CONDITIONAL (Route B only, physically motivated). (MEDIUM-HIGH)
- **ASBL-02 (Gap D)**: MVEH -- CONDITIONAL (structural identification via Connes-Rovelli, Sorce 2024 caveat). (MEDIUM-HIGH)
- **ASBL-02 (Overall verdict)**: v9.0 chain ASSEMBLED and CONDITIONALLY COMPLETE for d>=3. No prior work has comparable chain from finite-dim starting point. (HIGH)

### Phase 35 Results (v9.0)

- **BWEQ-01 (BW prerequisites)**: Wightman axioms W1-W4 satisfied for NL sigma model EFT. W5 (cluster) conditional on mass gap. W6 (constructive) open -- lattice-BW bypasses. OS reflection positivity from DLS 1978. (HIGH)
- **BWEQ-01 (Lattice-BW)**: H_ent^{BW} = (2pi/c_s) sum x_perp h_x, Eq. (35.1). SRF = 0.9993 validates BW locality fingerprint. Type I (lattice) vs type III_1 (continuum) gap honestly stated. (HIGH)
- **BWEQ-02 (KMS)**: KMS at beta=2pi derived (not assumed) from BW modular flow via Tomita-Takesaki. Modular flow sigma_t = boost by 2pi*t. (HIGH)
- **BWEQ-02 (Unruh)**: T_U = a/(2pi) from modular-to-proper time conversion. 2pi traced end-to-end from K_A = 2pi K_boost. (HIGH)
- **BWEQ-02 (Local equilibrium)**: theta = sigma = 0 at bifurcation surface from Killing equation -- exact geometric identity. (HIGH)
- **BWEQ-02 (Jacobson inputs)**: J1 (K_A=2pi K_boost), J2 (theta=sigma=0), J3 (T_U=a/(2pi)) packaged for Phase 36. (MEDIUM-HIGH)

### Phase 34 Results (v9.0)

- **LRNZ-01 (Isotropy)**: Cubic anisotropy alpha_4 = -1/96 at lattice scale, RG irrelevant with exponent rho ~ 2 (Hasenbusch 2021), corrections O(a^2/L^2). Continuous SO(d) restored at long wavelengths. (HIGH)
- **LRNZ-02 (Lorentz)**: Sigma model rescaling tau' = c_s*tau gives O(d+1)-symmetric Eq. (34.16). Wick rotation yields ds^2 = -c_s^2 dt^2 + dx^2 with c_s = 1.659 Ja. DLS 1978 reflection positivity justifies on bipartite lattice. (HIGH)
- **LRNZ-02b (von Ignatowsky)**: All 4 premises (relativity, homogeneity, isotropy, group structure) mapped to emergent theory. Finite c_s selects Lorentz over Galileo. (MEDIUM -- supporting, not primary)
- **LRNZ-03 (Velocity hierarchy)**: v_LR = 12.66 J, c_s = 1.659 J (a=1), v_LR/c_s = 7.63. Four arguments for c_eff = c_s. Hamma et al. 2009 precedent (v_LR/c_photon = 3.84 for toric code). (HIGH)
- **LRNZ-03 (Metric assembly)**: ds^2 = -c_s^2 dt^2 + g_ij dx^i dx^j. Fisher (spatial, Phase 32) + sigma model (temporal). Two-tier causal: LR cone (v_LR, exact) contains Lorentzian cone (c_s, EFT). (MEDIUM -- schematic, not theorem)

### Phase 33 Results (v9.0)

- **CORR-01 (Two-tier decay)**: Gapped tier: Hastings-Koma rigorous exponential. Neel tier (d>=2): m_s > 0 (QMC-established), correlations = m_s^2 + transverse 1/r^{d-1} from Goldstone modes (HIGH/MEDIUM)
- **CORR-02 (Sigma model)**: O(3) NL sigma model Eq. (33.11) with c_s = 1.659 Ja, rho_s = 0.181 J, chi_perp = 0.0657/J, g = 9.18 (d=2). QMC match to 0.3% (HIGH)
- **2D ED (4x4 OBC)**: m_s^2 = 0.233 (strong Neel), Fisher g_plaq = 4.76e-4 via 2x2 plaquette (3.88x > 1D N=16), sublattice TD = 0.114 (HIGH for Neel, MEDIUM for Fisher -- single L=4 point)
- **PBC benchmark**: E0/bond = -0.702, within 3.2% of QMC thermodynamic limit -0.6694 (HIGH)
- **CORR-03 (Fisher smoothness)**: Conditional theorem -- g_F(x) = O(m_s^2) > 0 at interior for d>=2 Neel phase. d>=3: Goldstone integral convergent. d=2: O(ln L) correction. Hypotheses H1-H4 explicit. Three-regime: 1D FAILS / Neel RESCUED / Gapped PASSES (MEDIUM)

### v8.0 Results (archived)

- **ALGV-01**: L_{E_{11}} = (1/2)*I_{16} on V_{1/2} (EXACT, zero error) (HIGH)
- **ALGV-02**: V_0 channel NEGATIVE -- T_b symmetric, J_u antisymmetric (HIGH)
- **T_b Clifford structure**: 9 traceless T_b satisfy {T_a,T_b} = (1/2)*delta_{ab}*I (HIGH)
- **Operator algebra**: 46-dim = 10 (Cl(9) vectors) + 36 (spin(9) from commutators) (HIGH)

## Open Questions

- ~~Does any element of the operator algebra generated by {T_b : b in V_0 = h_2(O)} on V_{1/2} satisfy J^2 = -Id?~~ ANSWERED: NO (structural impossibility -- T_b symmetric, J needs antisymmetric)
- ~~Is the full observable algebra on V_{1/2} (all Peirce multiplication COMPOSITIONS) large enough to contain J_u?~~ ANSWERED: YES trivially (closure = M_16(R) = all 16x16 matrices), but containment is vacuous
- ~~Does V_0 = h_2(O), being a JC-algebra, provide richer structure transmission than V_1 = R?~~ ANSWERED: Yes (10-dim vs 1-dim), but still insufficient for J (wrong symmetry class)
- ~~If algebraic forcing fails, is "no chirality -> no self-modelers" rigorous enough for a theorem?~~ ANSWERED: No -- it's "argued, not proved" (L4 weakest link). Gap C = selection-conditional.
- ~~What is the physical meaning of needing operator compositions (iterated measurements) rather than single Peirce multiplication to reach J_u?~~ ANSWERED: J_u enters at depth 2 (compositions of 3 Peirce operators), but this is vacuous since closure is everything
- NEW: Why does the Peirce-derived spin(9) differ from Krasnov's spin(9)? What is the physical significance of having two distinct spin(9) subalgebras of M_16(R)?
- NEW: Can the choice of u in S^6 be derived from the self-modeling framework, or is it necessarily external input?
- NEW: Is the reduced stabilizer (dim 10 = su(3)+u(1)^2) or Krasnov's (dim 12 = su(3)+su(2)+u(1)) the physically correct one?

## Performance Metrics

| Label | Duration | Tasks | Files |
| ----- | -------- | ----- | ----- |
| 28-01 | ~5min | 2 tasks | 2 files |
| 28-02 | ~8min | 2 tasks | 2 files |
| 29-01 | ~12min | 2 tasks | 2 files |
| 29-02 | ~15min | 2 tasks | 2 files |
| 30-01 | ~12min | 2 tasks | 3 files |
| 30-02 | ~8min | 1 tasks | 1 files |
| 33-01 | ~7min | 2 tasks | 1 files |
| 33-02 | ~8min | 2 tasks | 3 files |
| 33-03 | ~6min | 2 tasks | 1 files |
| 34-01 | ~6min | 2 tasks | 1 files |
| 34-02 | ~3min | 2 tasks | 1 files |
| 35-01 | ~3min | 2 tasks | 1 files |
| 35-02 | ~6min | 2 tasks | 1 files |
| 36-01 | ~7min | 2 tasks | 2 files |
| 36-02 | ~4min | 2 tasks | 1 files |

## Accumulated Context

### Decisions

- [Phase 36, Plan 02]: Gap A NARROWED for d>=3 (CORR-03 conditional theorem H1-H4). Gap B CLOSED only for d=1 Route A (exact CFT). Gaps C,D CONDITIONAL. MVEH = structural identification (never 'derived'). FISH-03 d=1 failure honestly stated. Sorce 2024 caveat cited. Overall: conditionally complete, not proved.
- [Phase 36, Plan 01]: Chain assembled with six links (a)-(f), every result cited by equation number. Rigor taxonomy: RIGOROUS/CONDITIONAL/PHYSICAL ARGUMENT/ASSUMED. Route A and Route B complementary. Chain status dimension-dependent: d>=3 CONDITIONAL, d=2 CONDITIONAL with caveats, d=1 FAILS.
- [Phase 35, Plan 02]: KMS derived (not assumed) from BW + Tomita-Takesaki. theta=sigma=0 exact from Killing equation. T_U=a/(2pi) with 2pi traced end-to-end. Jacobson inputs J1-J3 ready for Phase 36.
- [Phase 35, Plan 01]: BWEQ-01: Lattice-BW route (Giudici et al.) as primary. W6 open (constructive QFT gap). Type I/III gap honestly stated.
- [Phase 34, Plan 02]: c_eff = c_s = 1.659 Ja (four arguments: dispersion, EFT, universality, Hamma). Metric assembly ds^2 = -c_s^2 dt^2 + g_ij dx^i dx^j schematic. v_LR/c_s = 7.63 is 1D-specific.
- [Phase 34, Plan 01]: Isotropy via RG irrelevance (Hasenbusch rho~2), not numerical simulation. Wick rotation justified by DLS 1978 reflection positivity on bipartite lattices. Fisher metric != Lorentzian metric (forbidden proxy respected).
- [Phase 33, Plan 03]: CORR-03 conditional theorem (H1-H4). Sublattice alternation gives g_F ~ O(m_s^2) > 0. d>=3 clean, d=2 logarithmic.
- [Phase 33, Plan 02]: 2D Heisenberg 4x4 OBC: m_s^2=0.233 (Neel), g_plaq=4.76e-4 (3.88x > 1D). Neel rescue supported at L=4.
- [Phase 33, Plan 01]: Two-tier correlation decay (gapped + Neel). O(3) sigma model with c_s=1.659Ja (QMC to 0.3%). S=1/2 d=2 Neel is QMC-established, not rigorous.
- [Phase 30, Plan 01]: Three impossibility theorems proved -- Schur commutant dim=1, J_u grade-3 separation, u in S^6 = Gap B2. 71 tests pass.
- [Phase 30, Plan 02]: Gap C = algebraic impossibility (theorem) + selection-conditional (argued). L4 = weakest link.
- [Phase 29, Plan 02]: REPR-02 verdict -- J_u is distinguished (isolated, grade 2+3) but NOT a 10th Clifford generator. Spin(10) extension fails. Gap C cannot close purely algebraically.
- [Phase 29, Plan 01]: ALGV-03 confirmed -- associative closure = M_16(R) (256-dim). Clifford rescaling: gamma_1 = 4*T_b[1], gamma_k = 2*T_b[k] for k=2..9.
- [Phase 29, Verification]: Krasnov discrepancy resolved -- Peirce spin(9) != Krasnov spin(9) in M_16(R). Both give correct stabilizer dims for their embeddings.
- [Phase 28, Plan 01]: ALGV-01 V_1=R bottleneck numerically confirmed with zero error
- [Phase 28, Plan 02]: ALGV-02 V_0 channel NEGATIVE -- T_b operators symmetric, J_u antisymmetric
- [Phase 0]: Started milestone v9.0: Continuum Limit from Finite-Dimensional Observer — New milestone cycle: close all four Paper 6 gaps via finite-dim observer as UV cutoff

### Active Approximations

None yet.

**Convention Lock:**

- Metric signature: (+,+,...,+) Riemannian Fisher metric
- Fourier convention: N/A (lattice spin chain)
- Natural units: hbar=1, k_B=1, lattice spacing a=1
- Gauge choice: N/A (lattice spin chain)
- Regularization scheme: N/A (lattice spin chain)
- Renormalization scheme: N/A (lattice spin chain)
- Coordinate system: N/A (lattice spin chain)
- Spin basis: standard S^z eigenbasis
- State normalization: density matrices trace 1
- Coupling convention: J > 0 antiferromagnetic
- Index positioning: N/A (lattice spin chain)
- Time ordering: N/A (lattice spin chain)
- Commutation convention: N/A (lattice spin chain)
- Levi-Civita sign: N/A (lattice spin chain)
- Generator normalization: N/A (lattice spin chain)
- Covariant derivative sign: N/A (lattice spin chain)
- Gamma matrix convention: N/A (lattice spin chain)
- Creation/annihilation order: N/A (lattice spin chain)

*Custom conventions:*
- Jordan Product: a o b = (1/2)(ab + ba)
- Peirce Eigenvalues: {0, 1/2, 1}
- Octonion Convention: Fano e_1 e_2 = e_4 (matches Paper 7)
- Complex Structure: u = e_7 by default (any u in S^6 equivalent under G_2)
- Clifford Signature: Cl(9,0) (positive definite, NOT Cl(0,9))
- All Other Convention Fields: see `.gpd/CONVENTIONS.md`

### Propagated Uncertainties

None yet.

### Pending Todos

None yet.

### Blockers/Concerns

- ~~V_0 channel is genuinely unexplored~~ RESOLVED: V_0 channel fully characterized in Phase 28-29
- ~~Observable algebra dimension unknown~~ RESOLVED: closure = M_16(R) = 256-dim (full matrix algebra)
- ~~REPR-02 confirmed Path A (algebraic forcing fails): Phase 30 must formalize impossibility + selection argument~~ RESOLVED: Phase 30 complete -- 3 theorems + selection argument
- Two distinct spin(9) embeddings in M_16(R) -- physical significance unclear, noted in Krasnov discrepancy
- Phase 31 (Integration) must update Paper 7 gap register with Phase 30 results
- Krasnov stabilizer dim discrepancy (10 vs 12) needs interpretation: which spin(9) is physically relevant?

## Session Continuity

**Last session:** 2026-03-29
**Stopped at:** Phase 34 execution complete. All 2 plans passed. Verification pending.
**Resume file:** --
