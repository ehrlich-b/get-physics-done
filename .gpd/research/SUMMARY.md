# Research Summary

**Project:** v12.0 GR from det(X) on h_3(O)
**Domain:** Exceptional Jordan algebra / Magic supergravity / Peirce complement V_0 / Very special geometry
**Researched:** 2026-04-11
**Confidence:** MEDIUM (algebraic ingredients HIGH; novel V_0-to-spacetime chain MEDIUM-LOW; physical interpretation LOW-MEDIUM)

## Unified Notation

| Symbol | Quantity | Units/Dimensions | Convention Notes |
|--------|----------|------------------|------------------|
| h_3(O) | Exceptional (Albert) Jordan algebra | dim 27, dimensionless | 3x3 hermitian octonionic matrices |
| h_2(O) | 2x2 hermitian octonionic matrices = JSpin_9 | dim 10, dimensionless | Isomorphic to V_0 Peirce complement |
| h_2(C) | 2x2 hermitian complex matrices | dim 4, dimensionless | Isomorphic to R^{3,1} Minkowski |
| V_1, V_{1/2}, V_0 | Peirce spaces of h_3(O) at E_{11} | dim 1, 16, 10 | 27 = 1 + 16 + 10 decomposition |
| det_3(X) or N(X) | Cubic norm on h_3(O) | dimensionless | GST writes V(h) |
| det_2(Y) | Quadratic norm on h_2(O) | dimensionless | = beta*gamma - |x_1|^2; gives Minkowski metric |
| pi_u | Projection h_2(O) -> h_2(C_u) | linear map | Keeps C_u = span{1,u} component of off-diagonal octonion |
| u | Observer's complex structure | u in S^6 subset Im(O) | Default: u = e_7 (Fano convention) |
| C_u | Complex subalgebra of O | dim_R 2 | C_u = span_R{1, u} |
| F_4 | Aut(h_3(O)) | dim 52, rank 4 | Preserves Jordan product, Tr, and det |
| E_6(-26) | Str(h_3(O)) | dim 78, rank 6 | Preserves det up to scale; ALWAYS specify real form |
| E_7(-25) | 4d U-duality group | dim 133 | From 5d->4d reduction of octonionic MESGT |
| Spin(9) | Stab_{F_4}(E_{11}) | dim 36 | NOT SO(9) when acting on spinorial V_{1/2} |
| SU(3)_C | Stab_{G_2}(u) | dim 8 | Color group; acts on C^3 subset O, fixes C_u |
| d_{IJK} | Polarized cubic form | symmetric 3-tensor | det_3(X) = (1/6) d_{IJK} X^I X^J X^K |
| X circ Y | Jordan product | (1/2)(XY + YX) | Paper 5-7 convention with 1/2 factor |
| V(h) | GST prepotential | dimensionless | = C_{IJK} h^I h^J h^K = det_3(h) on N=1 surface |

**Metric signature:** (+,-,-,...,-) (mostly minus). det_2 on h_2(O) gives (1,9); det_2 on h_2(C) gives (1,3).

**Unit system:** Natural units (hbar = c = 1) for supergravity; dimensionless for pure algebra.

**Octonion basis:** Fano convention with e_1 e_2 = e_4, complex structure u = e_7.

## Executive Summary

The v12.0 milestone investigates whether the Peirce complement V_0 = h_2(O) of h_3(O), projected to h_2(C) = R^{3,1} by the C*-observer's complex structure u, can deliver 4d Lorentzian spacetime with the Gunaydin-Sierra-Townsend (GST) magic supergravity structure -- where det(X) on h_3(O) serves as the cubic prepotential determining matter-gravity coupling. The algebraic ingredients are individually well-established (HIGH confidence): h_2(O) = R^{9,1} as 10d Minkowski via determinant (Baez 2002), det(X) as the unique F_4-invariant cubic form (Springer 1962), and the GST construction of 5d N=2 MESGT from h_3(O) with prepotential V = det (GST 1983-84). What is genuinely novel and unestablished is the specific chain: C*-bottleneck forces pi_u: h_2(O) -> h_2(C) = R^{3,1}, the projected cubic form determines 4d gravitational couplings, and this reproduces the GST Lagrangian structure without invoking N=2 supersymmetry.

A critical dimension-signature issue must be front and center: h_2(O) with det gives R^{9,1} (10d Minkowski), NOT R^{3,1}. The reduction to 4d spacetime comes entirely from pi_u -- the projection O -> C_u that keeps only the complex component of each octonion. This is the same mechanism that projects V_{1/2} = O^2 to SM fermion representations (Papers 5+7), now applied to the gravitational sector. The 6 discarded dimensions correspond to the C^3 = "color" directions, giving a 10 = 4 + 6 splitting where the internal space is algebraically determined rather than chosen by hand. However, pi_u is NOT a Jordan algebra homomorphism due to octonion non-associativity -- the failure term is physically significant and may encode gauge-gravity coupling.

The recommended approach proceeds in five phases: (1) establish V_0 algebraic structure with pi_u and verify Minkowski signature, (2) decompose the d_{IJK} tensor into Peirce blocks identifying which cubic couplings survive projection, (3) verify equivariance and Lorentz subgroup structure, (4) connect to the GST Lagrangian and 5d->4d reduction, (5) synthesis and paper integration. All computations are exact finite-dimensional algebra (under 5 seconds total), with ~60% of needed infrastructure already implemented. The principal risks are overclaiming (GR itself comes from Paper 6 via Jacobson; h_3(O) determines the matter-gravity COUPLING), circularity in the det "double duty" argument, and the open question of whether the C*-bottleneck mechanism that works for V_{1/2} extends to V_0.

## Key Findings

### Prior Work Landscape

- **h_2(K) = R^{dim(K)+1,1}** as Minkowski spacetime for each division algebra K, with det giving the Minkowski metric (Baez 2002) [HIGH confidence]
- **det(X) on h_3(O) is the unique F_4-invariant cubic form**, up to scale (Springer 1962) [HIGH confidence]
- **GST magic supergravity**: 5d N=2 MESGT with scalar manifold E_6(-26)/F_4, 27 vectors, prepotential V = det(h) (GST 1983-84) [HIGH confidence]
- **5d -> 4d c-map**: Circle reduction gives 4d N=2 MESGT with E_7(-25)/(E_6 x U(1)), prepotential F(X) = det(X)/X^0 (de Wit-Van Proeyen 1992) [HIGH confidence]
- **Farnsworth (2025)**: First spectral triple over h_3(O), giving F_4 x F_4 gauge theory. Does NOT address gravity or det(X). [HIGH confidence for what it covers]
- **The V_0 -> spacetime interpretation is genuinely novel.** No prior work connects det(X) to gravity without N=2 SUSY.

### Recommended Methods

- **Explicit matrix Jordan product**: All h_3(O) and h_2(O) computations via direct octonionic matrix arithmetic
- **Polarization identity for d_{IJK}**: Compute symmetric trilinear form from det evaluations, decompose into Peirce blocks
- **Clifford commutant for stabilizer**: Intersect spin(9) generators with commutant of J_u
- **r-map KK reduction**: Standard 5d -> 4d following Lauria-Van Proeyen (2020) conventions

### Critical Pitfalls

1. **P1 (CRITICAL):** V_0 circ V_0 leaks into V_{1/2} -- use intrinsic h_2(O) product
2. **P2 (CRITICAL):** h_2(O) gives R^{9,1} not R^{3,1} -- pi_u does the reduction
3. **P3 (CRITICAL):** det "double duty" circularity risk -- must go through full GST chain
4. **P5 (CRITICAL):** E_6(-26) is the structure group, not E_6(-78) or E_6(6)
5. **P9 (MODERATE):** GR from Paper 6; h_3(O) determines matter-gravity COUPLING

### Computational Readiness

All computations exact on spaces dim <= 27. Existing codebase covers ~60%. Total runtime under 5 seconds.

## Implications for Roadmap

### Suggested Phase Structure (5 phases)

1. **V_0 Algebraic Foundation and pi_u Projection** -- LOW risk, prerequisite for all
2. **d_{IJK} Tensor and Peirce Block Decomposition** -- LOW risk, depends on Phase 1
3. **Equivariance and Lorentz Subgroup** -- LOW risk, parallel with Phase 2
4. **GST Lagrangian Connection and KK Reduction** -- MEDIUM risk, novel territory
5. **Synthesis and Paper Integration** -- MEDIUM risk, framing claims

## Open Questions

1. **[HIGH PRIORITY]** Does the C*-bottleneck argument extend from V_{1/2} to V_0?
2. **[HIGH PRIORITY]** Does the self-modeling framework produce a cubic density on h_3(O)?
3. **[MEDIUM]** Physical content of the pi_u non-homomorphism failure term?
4. **[MEDIUM]** Stabilizer of u in Spin(9): Spin(7) or Spin(7) x U(1)?
5. **[MEDIUM]** Does V_{1/2} x V_{1/2} -> V_0 after pi_u give the Dirac current?

## Sources

### Primary (HIGH confidence)

- Springer, T.A. and Veldkamp, F.D., *Octonions, Jordan Algebras and Exceptional Groups*, Springer (2000)
- Baez, J.C., "The Octonions," Bull. AMS 39 (2002) 145-205
- Gunaydin, Sierra, Townsend, Phys. Lett. B 133 (1983) 72-76
- Gunaydin, Sierra, Townsend, Nucl. Phys. B 242 (1984) 244-268
- de Wit, Van Proeyen, Commun. Math. Phys. 149 (1992) 307-333
- McCrimmon, K., *A Taste of Jordan Algebras*, Springer (2004)

### Secondary (MEDIUM confidence)

- Lauria, Van Proeyen, arXiv:2004.11433 (2020)
- Farnsworth, arXiv:2503.10744 (2025)
- Farnsworth, arXiv:2506.21496 (2025)
- Boyle, arXiv:2006.16265 (2020)
- Todorov, Drenska, arXiv:1805.06739

---

_Research synthesis completed: 2026-04-11_
_Ready for research plan: yes_
