# Research State

## Project Reference

See: .gpd/PROJECT.md (updated 2026-04-11)

**Core research question:** Can the Standard Model + GR be derived from the requirement that a composite system faithfully models itself?
**Current focus:** v12.0 GR from det(X) on h_3(O)

## Current Position

**Current Phase:** 48
**Current Phase Name:** Equivariance and Lorentz Subgroup
**Total Phases:** 50 (v12.0: Phases 46-50)
**Current Plan:** —
**Total Plans in Phase:** —
**Status:** Ready to plan
**Last Activity:** 2026-04-12
**Last Activity Description:** Phase 47 complete, transitioned to Phase 48

**Progress:** [████████████████████████████████████████████] 100%

## Active Calculations

- det_3(X) = alpha*beta*gamma - alpha*|x1|^2 - beta*|x2|^2 - gamma*|x3|^2 + 2*Re((x1*x2)*x3); left-to-right association confirmed
- d_{IJK} tensor: 106 nonzero entries out of 3654 (97% sparse); two Peirce blocks (V_1,V_0,V_0) [10] and (V_{1/2},V_{1/2},V_0) [96]
- det_2 Gram matrix on h_2(C_u) = diag(+1,-1,-1,-1): Minkowski signature (1,3) confirmed
- pi_u idempotent with 4-dim image; benchmark values det_2(E_{22})=0, det_2(I_2)=1, det_2(off-diag e_7)=-1
- Intrinsic h_2(O) Jordan product closes exactly in V_0 (all 55 basis pairs, zero V_{1/2} leakage)
- Delta(A,B) = <wA,wB>_W * I_2 closed form (vanishes on h_2(C_u), nonzero on W)
- Four Minkowski matrices M_mu with M_0=(1/2)I, spatial Cl(3,0): {M_i,M_j}=(1/2)*delta_ij*I_16
- V_{1/2} x V_{1/2} -> V_0 surjective (rank 10), pi_u-projected surjective (rank 4)

## Intermediate Results

- **O(9) quantitative (41-01)**: c_s(O(9),Z^3) = J*sqrt(3/2) = 1.225 Ja (classical), v_LR = 27eJ = 73.4 J, ratio 59.9, BW universality (no SRF number), C(r) = 16/(pi*J*r) d=3. All Heisenberg carry-forward values replaced. Quantum correction ~20% unknown. (MEDIUM-HIGH)
- **Derivation chain update (41-02)**: Links (i)-(l) updated with O(9) numbers. c_s=J*sqrt(3/2), rho_s=J/8, v_LR=27eJ, v_LR/c_s~60. Carry-forward caveat removed. Internal consistency verified. Chain fully self-consistent on O(9)/S^8. (HIGH)

## Open Questions

- NEW: Why does the Peirce-derived spin(9) differ from Krasnov's spin(9)? Physical significance of two distinct spin(9) subalgebras of M_16(R)?
- NEW: Can the choice of u in S^6 be derived from the self-modeling framework, or is it necessarily external input?
- NEW: Is the reduced stabilizer (dim 10 = su(3)+u(1)^2) or Krasnov's (dim 12 = su(3)+su(2)+u(1)) the physically correct one?
- RESOLVED (38-02): Macroscopic lattice = Z^d with h_3(O) per site. K_3 is on-site algebraic structure.
- RESOLVED (39-01): SSB pattern corrected: spontaneous Spin(9)->Spin(8) on S^8 (8 Goldstones), not F_4->Spin(9) on OP^2 (16).
- RESOLVED (38-02): Cubic det(A) is formally RG-relevant (dim 3/2 in d=3) but coefficient = 0 exactly on OP^2.
- RESOLVED (39-02): All 8 Goldstone modes are Type-A (linear omega=c_s|k|). rho_ab = 0 from real Clifford rep.
- RESOLVED (39-02): Ferromagnetic ordering does NOT threaten Lorentz emergence. Real rep forces Type-A.
- Can quantum SSB be proved without BCS? S_eff=1/2 too small for BCS; alternative routes (mean-field heuristic, direct ED scaling) may help.

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
| 37-01 | ~5min | 2 tasks | 2 files |
| 37-02 | ~5min | 2 tasks | 1 files |
| 38-01 | ~10min | 2 tasks | 3 files |
| 38-02 | ~9min | 2 tasks | 3 files |
| 39-01 | ~12min | 2 tasks | 3 files |
| 39-02 | ~5min | 2 tasks | 2 files |
| 39-03 | ~6min | 2 tasks | 2 files |
| 39-04 | ~4min | 2 tasks | 2 files |
| 40-01 | ~9min | 2 tasks | 3 files |
| 40-02 | ~4min | 1 tasks | 2 files |
| 41-01 | ~7min | 2 tasks | 1 files |
| 41-02 | ~6min | 1 tasks | 1 files |
| 43-01 | ~10min | 1 task | 1 file |
| 43-02 | ~4min | 2 tasks | 2 files |
| 44-01 | ~5min | 1 task | 1 file |
| 44-02 | ~7min | 2 tasks | 2 files |
| 46-01 | ~4min | 2 tasks | 1 file |
| 46-02 | ~9min | 2 tasks | 1 file |

## Accumulated Context

### Decisions

- [Phase 47, Plan 02]: F_4 invariance verified under S_3+G_2+Spin(9) (630 tests). Uniqueness via Springer 1962. Double duty non-circular: V_GST = c*det(X). 16 SM fermions match Paper 7. V_0 = 4(Minkowski) + 6(internal).
- [Phase 47, Plan 01]: det_3 with left-to-right Re((x1*x2)*x3); d_{IJK} via inclusion-exclusion polarization yields d(X,X,X)=6*N(X). Two nonzero Peirce blocks: (V_1,V_0,V_0)=det_2 bilinear [10 entries] and (V_{1/2},V_{1/2},V_0) [96 entries]. All forbidden blocks exactly zero. 106/3654 nonzero (97% sparse).
- [Phase 46, Plan 02]: Delta(A,B) = <wA,wB>_W * I_2 where W=span{e_1,...,e_6}. Mechanism: pi_u kills W-components, but W x W Fano cross-terms produce C_u diagonal. V_{1/2} x V_{1/2} -> h_2(C_u) gives spatial Cl(3,0): {M_i,M_j}=(1/2)*delta_ij*I_16. V_1 = identity. Both product maps surjective.
- [Phase 46, Plan 01]: pi_u constructed via proj_u(b) = (b_0, 0,...,0, b_7) for u=e_7. det_2 = beta*gamma - |x1|^2 gives Gram diag(+1,-1,-1,-1). Intrinsic h_2(O) Jordan product closes exactly in V_0 with zero V_{1/2} leakage -- Peirce rule holds for h_3(O), resolving uncertainty marker.
- [Phase 44, Plan 02]: L1-L9 chain verified: L4 UPGRADED (Argued -> Proved given Paper 5), L5/L7/L9 STRENGTHENED (conditionality shifts from L4 to L1), L1/L2/L3/L6/L8 UNCHANGED. Zero regressions. Gap register v11.0 section appended with Paper 7 Gap C = PROVED (given Paper 5), v10.0 Gap C = UNCHANGED at CONDITIONAL-DERIVED.
- [Phase 44, Plan 01]: Pure assembly -- Gap C closure stated as single 7-step theorem. All steps cite Phase 43, Paper 5, Paper 7, or Lawson-Michelsohn. No new mathematics. Observer-induced label; algebraic closure rejected. Phase 30 compatibility explicit. Gap C disambiguated (Paper 7 vs v10.0).
- [Phase 43, Plan 02]: C-linear closure proved by dimension counting. 256 even-grade Cl(9,0) monomials form C-basis of M_16(C). Volume element hat_omega = +I_16 on V_{1/2}. Cl(9,C) identified. Spinor extension S_9 -> S_{10}^+ via Lawson-Michelsohn branching.
- [Phase 43, Plan 01]: Route A (holomorphic FC) used as primary proof. Route B (Alfsen-Shultz) provided as sketch only. Theorem stated for arbitrary n >= 16. All 4 contract claims passed. Effect control correctly predicted as real. Gudder-Greechie domain gap explicitly bridged.
- [Phase 42, Plan 01]: GO verdict confirmed -- sqrt(T_a) T_b sqrt(T_a) = (i/2)*T_b for all 72 anticommuting Cl(9,0) pairs, verified by dual NumPy+SymPy. Sequential product exits M_16(R). Proceed to Phase 43.
- [Phase 41, Plan 02]: Derivation chain carry-forward caveat replaced with historical note. All Heisenberg numbers in links (i)-(l) replaced with O(9) values. Classical c_s caveat added as uncertainty marker. SRF stated as universality argument only. No rigor levels changed.
- [Phase 41, Plan 01]: All 5 O(9)-specific quantities computed. c_s = J*sqrt(3/2) (classical). v_LR = 27eJ (NS). Ratio 59.9. BW by universality (no SRF number). CORR-03 with N-1=8. All Heisenberg carry-forward values replaced. Classical-only precision with honest caveats.
- [Phase 40, Plan 02]: v10.0 vs v9.0 comparison produced. 13 structural differences. 2 gaps UPGRADED (C: CONDITIONAL-DERIVED, D: CONDITIONAL-THEOREM), 7 UNCHANGED, 0 regressions. Quantum SSB = new insight not regression. Status: conditionally complete for d>=3.
- [Phase 40, Plan 01]: v10.0 chain assembled with 12 links (a')-(l). Gap C upgraded CONDITIONAL -> CONDITIONAL-DERIVED (Eq. 37.6). Gap D upgraded CONDITIONAL -> CONDITIONAL-THEOREM (Eq. 37.12). 15 assumptions: 4 verified + 2 derived + 2 prior-verified + 7 assumed = 15. Quantum SSB conditionality documented throughout.
- [Phase 39, Plan 04]: UC1-UC4 all classical-verified, UC1/UC4 quantum-conditional (shared root: S_eff=1/2, Speer). 8/15 gap dependency assumptions resolved. Type-A Goldstone => Lorentz chain consistent.
- [Phase 39, Plan 03]: Sigma model target = S^8 (from Spin(9)->Spin(8) SSB). Ric(S^8) = 7g. Beta = -(d-2)g^2 + (7/2pi)g^4. AF in d=2. No topological terms in d<=7.
- [Phase 39, Plan 02]: rho_ab = 0 exactly (real antisymmetric identity). All 8 Goldstone modes Type-A. Lorentz emergence consistent. Real rep is the mechanism.
- [Phase 39, Plan 01]: SSB pattern corrected from roadmap. Spontaneous Spin(9)->Spin(8) on S^8 (8 Goldstones), not F_4->Spin(9) on OP^2 (16). Classical SSB proved via FSS. Quantum SSB CONDITIONAL (BCS fails at S_eff=1/2).
- [Phase 38, Plan 02]: Frame stabilizer = Spin(9) (not F_4). Cubic det(A) = 0 on OP^2 (geometric, not Z_2). Ferro ground state -> Type I/II Goldstone TBD.
- [Phase 38, Plan 01]: Rescaled T_b to uniform Clifford normalization T_a = (1/2)*gamma_a. 2-site spectrum: 5 levels Lambda^k(V_9). Ground state Lambda^1 (vector rep, dim 9), FERROMAGNETIC.
- [Phase 37, Plan 02]: Gap C upgraded CONDITIONAL -> CONDITIONAL-DERIVED. Gap D upgraded CONDITIONAL -> CONDITIONAL-THEOREM. Dependency matrix 18x6 with no circular dependencies. Phase 39 handoff: UC1-UC4.
- [Phase 37, Plan 01]: Gap C tensoriality DERIVED from BW + Raychaudhuri + Lovelock (5-step chain). Gap D MVEH math content DERIVED from BW + TT + Gibbs (5-step chain). Sorce two-tier analysis.
- [Phase 0]: Started milestone v10.0: Universality Class of Self-Modeler Network and Full Gap Closure
- [Phase 36, Plan 02]: Gap A NARROWED for d>=3. Gap B CLOSED only for d=1 Route A. Gaps C,D CONDITIONAL. Overall: conditionally complete, not proved.
- [Phase 36, Plan 01]: Chain assembled with six links (a)-(f). Rigor taxonomy applied. Chain status dimension-dependent: d>=3 CONDITIONAL, d=1 FAILS.
- [Phase 35, Plan 02]: KMS derived (not assumed) from BW + Tomita-Takesaki. Jacobson inputs J1-J3 ready.
- [Phase 34, Plan 01]: Isotropy via RG irrelevance (Hasenbusch rho~2). Wick rotation justified by DLS reflection positivity.
- [Phase 30, Plan 01]: Three impossibility theorems proved. 71 tests pass.
- [Phase 29, Plan 01]: Associative closure = M_16(R) (256-dim). Clifford rescaling established.
- [Phase 41]: Added Phase 41: O(9)/S^8 Quantitative Verification — Patch phase to recompute model-specific numbers for O(9)/S^8, replacing Heisenberg carry-forward values in links (i)-(l)
- [Phase 0]: Started milestone v11.0: Gap C Complexification from Sequential Product — New milestone cycle -- second attempt at Gap C using sequential product route
- [Phase 0]: Started milestone v12.0: GR from det(X) on h_3(O) — New milestone cycle -- algebraic GR route via GST magic supergravity prepotential on Peirce complement

### Active Approximations

None yet.

**Convention Lock:**

- Metric signature: (+,+,...,+) Riemannian Fisher metric
- Fourier convention: N/A (pure algebra, no field theory)
- Natural units: hbar=1, k_B=1, lattice spacing a=1
- Gauge choice: N/A (pure algebra, no gauge fields)
- Regularization scheme: N/A (pure algebra, no divergences)
- Renormalization scheme: N/A (pure algebra, no renormalization)
- Coordinate system: N/A (pure algebra, no spacetime)
- Spin basis: standard S^z eigenbasis
- State normalization: density matrices trace 1
- Coupling convention: J > 0 antiferromagnetic
- Index positioning: N/A (pure algebra, no tensors)
- Time ordering: N/A (pure algebra, no dynamics)
- Commutation convention: [A,B] = AB - BA; {A,B} = AB + BA
- Levi-Civita sign: N/A (not used in this phase)
- Generator normalization: T_a = (1/2) gamma_a; {T_a, T_b} = (1/2) delta_{ab} I_16
- Covariant derivative sign: N/A (pure algebra, no derivatives)
- Gamma matrix convention: Cl(9,0): gamma_a gamma_b + gamma_b gamma_a = 2 delta_{ab} I_16; T_a = gamma_a/2
- Creation/annihilation order: N/A (pure algebra, no second quantization)

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

- Two distinct spin(9) embeddings in M_16(R) -- physical significance unclear, noted in Krasnov discrepancy
- Krasnov stabilizer dim discrepancy (10 vs 12) needs interpretation: which spin(9) is physically relevant?
- RESOLVED (38-02): K_3 bipartiteness -- K_3 is on-site, physical lattice Z^d is bipartite
- RESOLVED (38-02): Frame stabilizer = Spin(9) (dim 36), confirmed by 3 independent methods
- RESOLVED (39-02): Ferromagnetic Goldstone modes are Type-A (not Type-II). Real Clifford rep forces rho_ab=0.
- Quantum SSB remains CONDITIONAL (S_eff=1/2, BCS fails, Speer blocks quantum RP). Shared root for UC1/UC4 conditionality.

## Session Continuity

**Last session:** 2026-04-11
**Stopped at:** v12.0 roadmap created, Phase 46 ready to plan
**Resume file:** --
