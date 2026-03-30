# Research State

## Project Reference

See: .gpd/PROJECT.md (updated 2026-03-29)

**Machine-readable scoping contract:** `.gpd/state.json` field `project_contract` (stale v1.0 -- use v9.0 Scoping Contract Summary in PROJECT.md)

**Core research question:** Can the Standard Model + GR be derived from the requirement that a composite system faithfully models itself?
**Current focus:** v9.0 Continuum Limit from Finite-Dimensional Observer

## Current Position

**Current Phase:** 32
**Current Phase Name:** Fisher Geometry on Reduced States
**Total Phases:** 36 (31 prior + 5 new in v9.0)
**Current Plan:** 02/02 complete
**Total Plans in Phase:** 2
**Status:** Phase 32 complete (FISH-01/02 pass, FISH-03 deferred to Phase 33 d>=2)
**Last Activity:** 2026-03-30
**Last Activity Description:** Phase 32 executed. FISH-01 (smoothness) and FISH-02 (positive-definiteness) established. FISH-03 (distance recovery) FAILS in 1D: g_bulk ~ N^{-2.75} -> 0.

**Progress:** [██░░░░░░░░] 20% (v9.0)

## Active Calculations

- Fisher metric g(x) on Heisenberg 1D OBC: g_bulk ~ 0.22 * N^{-2.75} for |Lambda|=2
- Boundary decay: xi_corr matches Hastings-Koma xi_HK = v_LR/gamma within 3%

## Intermediate Results

### Phase 32 Results (v9.0)

- **FISH-01 (Smoothness)**: rho_Lambda(x) smooth from Hastings-Koma exponential clustering; bound exp(-R(x)/xi) where R(x) = min(x, N-x-|Lambda|) (HIGH)
- **FISH-02 (Positive-definiteness)**: g(x) > 0 at all interior points for N=8,12,16,20, |Lambda|=2,3. Z_2 symmetry zero at chain center for even N, |Lambda|=2. Bures fallback for rank-deficient case. (HIGH)
- **FISH-03 (Distance recovery)**: FAILS in 1D. g_bulk ~ 0.22*N^{-2.75} (|Lambda|=2), 7.72*N^{-3.87} (|Lambda|=3). Root cause: 1D Heisenberg is gapless, bulk becomes translation-invariant. (HIGH)
- **SLD-Bures cross-validation**: SLD = 4*Bures to rel_err < 7e-6 in infinitesimal limit (HIGH)
- **TFI benchmark**: Critical enhancement at h/J=1 reproduces Zanardi 2007 (HIGH)
- **PBC sanity**: g = 0 to machine precision on PBC (HIGH)
- **Boundary decay**: xi_corr matches Hastings-Koma xi_HK within 3% at N=20 (HIGH)
- **Three FISH-03 rescue paths**: (1) rescaled metric g*N^alpha, (2) 2D lattice with Neel order, (3) gapped variant (AKLT) (MEDIUM)
- **14 tests passing**, code in code/fisher_metric.py, data in data/fisher/fisher_swap_1d.json

### v8.0 Results (archived)

See MILESTONES.md for v8.0 details. Key results: observable algebra = M_16(R), three impossibility theorems, selection argument, 71 tests.

### Phase 28 Results (v8.0)

- **ALGV-01**: L_{E_{11}} = (1/2)*I_{16} on V_{1/2} (EXACT, zero error) -- numerical confirmation of v6.0 Phase 22 Route 1 (HIGH)
- **ALGV-02**: V_0 channel NEGATIVE -- all 10 T_b are symmetric, J_u is antisymmetric, residual = 4.0 (HIGH)
- **T_b Clifford structure**: 9 traceless T_b satisfy {T_a,T_b} = (1/2)*delta_{ab}*I -- they ARE Cl(9) generators on V_{1/2} (HIGH)
- **Operator algebra**: 46-dim = 10 (Cl(9) vectors) + 36 (spin(9) from commutators) (HIGH)
- **Key insight**: J_u lies in associative closure but NOT in linear span of T_b (HIGH)

### Phase 29 Results

- **ALGV-03**: Associative closure of {T_b} = M_16(R) (256-dim), dimension growth 10->46->130->256 (HIGH)
- **Volume element**: omega = +I_{16} (P_+ factor of Cl(9,0)), all eigenvalues +1 (HIGH)
- **J_u anticommutation**: J_u COMMUTES with gamma_1 (diagonal traceless), mixed with gamma_2..9 -- NOT a 10th Clifford generator (HIGH)
- **J_u grade decomposition**: grade 2+3 mixed (4 grade-2 + 4 grade-3 terms), coefficients {0.25, 0.75} from Fano plane (HIGH)
- **J_u depth**: enters at depth 2 (requires 3+ Peirce operator compositions) (HIGH)
- **J_u uniqueness**: isolated in 8-monomial subspace (tangent dim=0, Jacobian rank=8) (HIGH)
- **Stabilizer**: dim(Stab_{spin(9)}(J_u)) = 10 = su(3) + u(1)^2 for PEIRCE-derived spin(9) (HIGH)
- **Krasnov resolution**: Peirce spin(9) != Krasnov spin(9) in M_16(R); combined rank 51 (not 36). Krasnov's spin(9) gives stab dim=12. Both correct for their embeddings (HIGH)
- **Spin(10) extension**: FAILS -- span{spin(9), gamma_i J_u} = 45-dim but NOT a Lie algebra; closure = sl(16,R) (255-dim) (HIGH)
- **REPR-02 verdict**: J_u is algebraically distinguished but containment in M_16(R) is vacuous; Gap C cannot close purely algebraically (HIGH)

### Phase 30 Results

- **Theorem 1 (No equivariant J)**: End_{Spin(9)}(S_9) = R (commutant dim=1 by SVD). No Spin(9)-equivariant J with J^2=-Id exists. Schur's lemma + Bott periodicity (9 mod 8 = 1 = real type). (HIGH)
- **Theorem 2 (J_u not in spin(9))**: J_u grade-3 norm = 0.866, spin(9) is grade-2 only. Projection residual = 0.866. (HIGH)
- **Theorem 2 distinguishing**: All 36 grade-2 complex structures (gamma_{ij}) have stabilizer dim=22, not 10. J_u's su(3)+u(1)^2 structure is unique to grade 2+3 elements. (HIGH)
- **Theorem 3 (Weakest condition)**: Minimal input = u in S^6 = Gap B2. Given u, J_u uniquely determined (Jacobian rank 8). Stabilizer dim=10. (HIGH)
- **Selection chain**: L1-L5 independently justified, no circular Gap C reference. L4 ("no chirality -> no self-modelers") = weakest link, flagged as "argued, not proved". (HIGH for structure, MEDIUM for L4)
- **Gap C honest status**: Algebraic impossibility (theorem) + selection-conditional (argued). NOT "closed" or "proved". (HIGH)
- **Test suite**: 17 new tests + 54 Phase 29 regression = 71 total, all passing. (HIGH)

### v8.0 Carry-Forward (from v5.0, v6.0, v7.0)

- **Peirce decomposition**: h_3(O) = V_1(1) + V_{1/2}(16) + V_0(10) under E_11 (HIGH)
- **V_{1/2} = O^2 = S_9** (real Spin(9) spinor, dim_R = 16) (HIGH)
- **V_1 = R*E_11** is 1-dimensional -- ALL 4 v6.0 Peirce-mediated routes failed at this bottleneck (HIGH)
- **S_9 is REAL type** (Frobenius-Schur = +1, End_{Spin(9)}(S_9) = R) (HIGH)
- **G_SM = Stab_{Spin(9)}(J_u)** where J_u is left-mult by u on O^2 (Krasnov 2019) (HIGH)
- **Extension of scalars** V_{1/2}^C = S_{10}^+ valid but generic (not h_3(O)-specific) (HIGH)
- **v7.0 selection**: non-complexified blocks have rho = 0 for SM-like observers (MEDIUM)
- **V_0 = h_2(O)** channel UNEXPLORED in v6.0 -- this is the novel v8.0 algebraic route (HIGH)

### Prior Milestones (condensed)

- Paper 5: M_n(C)^sa from self-modeling via S1-S7 + local tomography + type exclusion (HIGH)
- Paper 6: Einstein equations from self-modeling lattice via Jacobson + area law (HIGH)
- Paper 7: 9-link chain L1-L9 from self-modeling to chiral SM, conditional on gaps A, B1, B2, C (HIGH)
- v4.0: Simple M_n(C) cannot produce SM gauge group -- structural obstruction (HIGH)

## Open Questions

- **RESOLVED (NO):** Does the Fisher information metric on SWAP ground state reduced states recover lattice distance at leading order? -> g_bulk -> 0 as N -> inf in 1D.
- Can d_Fisher/d_lattice be rescued by rescaling (g*N^alpha), 2D lattice (Neel order), or gapped variant (AKLT)?
- Does the 2D Heisenberg AFM Fisher metric give non-vanishing g_bulk due to Neel long-range order?
- Does the Heisenberg AFM (n=2) on d>=2 lattice have a rigorous spectral gap proof?
- Does isotropy + LR finite speed + Fisher smoothness uniquely determine Lorentz invariance?
- Does the effective theory from Fisher geometry satisfy Wightman axioms sufficient for BW?
- Is the Fisher metric Riemannian or can it give Lorentzian signature?
- Carry-forward from v8.0: two distinct spin(9) embeddings in M_16(R), physical significance unclear

## Performance Metrics

| Label | Duration | Tasks | Files |
| ----- | -------- | ----- | ----- |
| 28-01 | ~5min | 2 | 2 |
| 28-02 | ~8min | 2 | 2 |
| 29-01 | ~12min | 2 | 2 |
| 29-02 | ~15min | 2 | 2 |
| 30-01 | ~12min | 2 | 3 |
| 30-02 | ~8min | 1 | 1 |

## Accumulated Context

### Decisions

Full log: `.gpd/DECISIONS.md`

**Recent high-impact:**
- [Phase 32, Plan 01]: FISH-02 passed (g>0 at all interior points). FISH-03 FAILS: d_Fisher/d_lattice -> 0 as N -> inf. g_bulk ~ N^{-2.75}. 1D Heisenberg bulk is translation-invariant.
- [Phase 32, Plan 02]: Three FISH theorems proved. Smoothness from Hastings-Koma (corrected bound). PD from SLD structure. Distance recovery fails honestly. Three rescue paths identified.
- [Phase 30, Plan 01]: Three impossibility theorems proved -- Schur commutant dim=1, J_u grade-3 separation, u in S^6 = Gap B2. 71 tests pass.
- [Phase 30, Plan 02]: Gap C = algebraic impossibility (theorem) + selection-conditional (argued). L4 = weakest link.
- [Phase 29, Plan 02]: REPR-02 verdict -- J_u is distinguished (isolated, grade 2+3) but NOT a 10th Clifford generator. Spin(10) extension fails. Gap C cannot close purely algebraically.
- [Phase 29, Plan 01]: ALGV-03 confirmed -- associative closure = M_16(R) (256-dim). Clifford rescaling: gamma_1 = 4*T_b[1], gamma_k = 2*T_b[k] for k=2..9.
- [Phase 29, Verification]: Krasnov discrepancy resolved -- Peirce spin(9) != Krasnov spin(9) in M_16(R). Both give correct stabilizer dims for their embeddings.
- [Phase 28, Plan 01]: ALGV-01 V_1=R bottleneck numerically confirmed with zero error
- [Phase 28, Plan 02]: ALGV-02 V_0 channel NEGATIVE -- T_b operators symmetric, J_u antisymmetric
- [Phase 0]: Started milestone v9.0: Continuum Limit from Finite-Dimensional Observer — New milestone cycle: close all four Paper 6 gaps via finite-dim observer as UV cutoff

### Active Approximations

None (algebraic, exact computation).

**Convention Lock:**

- Jordan product: a o b = (1/2)(ab + ba)
- Peirce eigenvalues: {0, 1/2, 1}
- Octonion convention: Fano e_1 e_2 = e_4 (matches Paper 7)
- Complex structure: u = e_7 by default (any u in S^6 equivalent under G_2)
- Clifford signature: Cl(9,0) (positive definite, NOT Cl(0,9))
- All other convention fields: see `.gpd/CONVENTIONS.md`

### Propagated Uncertainties

None (algebraic, exact).

### Pending Todos

None yet.

### Blockers/Concerns

- **FISH-03 failure in 1D**: g_bulk -> 0 as N -> inf. Distance recovery requires 2D (Neel order) or gapped system or rescaled metric. This impacts Phases 34 (emergent Lorentz) and 36 (assembly).
- Fisher metric signature: Riemannian (positive-definite) not Lorentzian -- need causal structure from LR bounds separately
- Exponential decay for general n: may not have rigorous proof; n=2 is the rigorous target
- BW theorem requires Wightman axioms in the effective theory -- need to check these hold

## Session Continuity

**Last session:** 2026-03-30
**Stopped at:** Phase 32 execution complete. FISH-01/02 pass, FISH-03 fails. Awaiting verification.
**Resume file:** --
