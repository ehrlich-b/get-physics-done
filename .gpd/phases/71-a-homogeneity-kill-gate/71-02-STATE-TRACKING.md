# State Tracking — Phase 71-02

## Conventions in effect (state.json convention_lock SSOT; matches PLAN frontmatter)
- natural units; decisive arithmetic EXACT over Q (sympy.Rational/Matrix, DomainMatrix-over-QQ exact_qq_rank)
- F_4 = inner_derivations() (52); E_6 = Stab(det); e_6 = f_4 + L(h_3(O)_traceless), dim 78 = 52+26
- E_11 = diag(1,0,0); Peirce V_1(eig1)=[0], V_0(eig0)=[1..10], V_{1/2}(eig1/2)=[11..26] (VERIFIED via L_E11 spectrum)
- det_3 = engine SSOT (LOCK 0 byte-identity to ring_lemma_verification.py); cone metric g_X = Hess(-log det)
- Gauss: II=0 <=> totally geodesic <=> R^slice = R^ambient|_slice
- 0 octonion_algebra imports, 0 numpy float-rank on decisive path (exact-only source guard PASS)

## Equations / decisive quantities (all EXACT over Q)
| Quantity | Value | Status |
|---|---|---|
| Peirce split under E_11 | V_1[0](1) + V_0[1..10](10) + V_{1/2}[11..26](16) | VERIFIED (L_E11 diagonal) |
| single-copy F_4 anchor | orbit 24 / Spin(8) 28 / trdeg 3 | REPRODUCED (exact_qq_rank, 3 pts) |
| dim e_6 | 78 = 52 (f_4) + 26 (L traceless) | VERIFIED (span rank over Q) |
| orbit of E_11 under e_6 | 17 = dim affine cone over Cayley plane OP^2 | VERIFIED (2 routes) |
| dim Stab_{E_6}(E_11) = ker{D->D.E_11} | 61 = 78 - 17 | VERIFIED (structural ~45 = Levi only) |
| dim Stab_{V_0} (slice-preserving) | 45 = dim Spin(9,1) | VERIFIED (recovers Levi expectation) |
| V_0 orbit under Stab_{V_0} | 9 < 10 = family dim; trdeg=1 (modulus = det_2) | VERIFIED (MAX over 2 pts) |
| II(V_0) @ I/3 and @ positive V_0-pert | 0 (TOTALLY GEODESIC) | VERIFIED (dim_normal=17, det_3>0) |
| II(h_2(C_u)) @ I/3 | 0 (explains 71-01 H^3 K=-1/2) | VERIFIED |
| II(V_0 + one V_{1/2} matter dir) @ I/3 | != 0 (#nz=17; matter sources curvature) | VERIFIED |

## Verdicts
- Route 2 (stabilizer transitivity on V_0): Stab_{V_0}=Spin(9,1) transitive on det_2-leaves (orbit 9 = leaf dim 9)
- CALC-02 (II of V_0): II=0 => totally geodesic => homogeneous matterless slice => KILL signal
- Route 1 (71-01, consumed): SURVIVES (matter-loaded basepoints)
- FINAL: ROUTES DISAGREE (II=0 KILL-signal vs Route-1 SURVIVES) => NO Phase-71 verdict; localization = matter-vs-geometry split (Phase-72 question); NOT Riemannian-vs-Lorentzian => NOT return-to-Phase-70

## Approximations / limits
- II via the Hessian-metric algebraic shortcut II^n_{bc} = (1/2) f_{abc} n^a (no metric inverse; full V_0)
- II evaluated at POSITIVE-cone basepoints only (det_3>0); pure-V_0 (alpha=0) is cone boundary (g singular), excluded
- V_0 orbit / Stab ranks: MAX over >=2 generic octonionic-integer points (rank lower-semicontinuous)

## Engine status
- code/bulk_geometry_verification.py (Section 13 added): ALL_PASS, exit 0, 41 PASS / 0 FAIL, deterministic (run1==run2)
- exact-only source guard PASS (0 octonion_algebra, 0 float-rank); LOCK 0 / 7a / 7b PASS

## Figures
- None (pure algebra/geometry; results are exact rationals + dimension counts)
