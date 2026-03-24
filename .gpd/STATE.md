# Research State

## Project Reference

See: .gpd/PROJECT.md (updated 2026-03-22)

**Core research question:** Does the observer's complexification of h_3(O) automatically produce the correct chiral SM representation via Cl(6)?
**Current focus:** v5.0 Chirality from h_3(O) via Cl(6) -- Phase 21 complete

## Current Position

**Current Phase:** 21 (complete)
**Current Phase Name:** Paper 7 Assembly
**Total Phases:** 4 (Phases 18-21)
**Current Plan:** 3/3 complete
**Total Plans in Phase:** 3
**Status:** Milestone complete
**Last Activity:** 2026-03-24
**Last Activity Description:** v5.0 milestone completed and archived

**Progress:** [██████████] 100% (v5.0)

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
- **Paper 6 manuscript assembled**: 7 sections, 4 figures, 33 bibliography entries (HIGH)
- **Verification passed**: 14/14 contract targets, 12/12 physics checks, 41/41 consistency checks (HIGH)
- **MVEH definitional throughout**: zero "Assumption A5" instances, 14 "definitional" instances (HIGH)
- **L1-L8 chain complete**: all 8 links present in corresponding sections with Table I in introduction (HIGH)
- **10/10 anchor references cited**: Jacobson 1995/2016, Connes-Rovelli, Sorce, Hastings, VanRaamsdonk, LMVR, Faulkner, CCM, Paper 5 (HIGH)
- **No overclaiming**: zero forbidden phrases, explicit non-claims for G, d=3+1, Lambda (HIGH)

- **pi_o(b) = diag(I_n tensor b^T, I_n tensor b^T)** at general n via J antilinearity (HIGH)
- **[pi(a), pi_o(b)] = 0** for all a, b in M_n(C) at general n -- order zero PASSED (HIGH)
- **Both naive and contragredient actions satisfy order zero** (HIGH)
- **pi_o is *-representation of A^{op}** (HIGH)
- **Even condition [gamma, pi(a)] = 0 FAILS** for all non-scalar a; only C*I survives (HIGH)
- **KO-dim 6 signs verified**: J^2 = +1, J gamma = -gamma J (HIGH)
- **Commutant dimension**: comm(pi(M_n)) = 4n^2 (HIGH)
- **52 pytest tests pass** at n=2,3,4 with zero failures (HIGH)
- **H = 2 x C^{n^2}** as irreducible M_n(C)-M_n(C)^o bimodules (HIGH)
- **Krajewski diagram**: single vertex (n,n), multiplicity 2 (HIGH)
- **Barrett isomorphism**: C^n tensor C^n = M_n(C) via v tensor w -> v w^T (HIGH)
- **Per-sector n^2 = k^2** with k = n; n=4 gives k=4 (SM value), dim(H) = 32 (HIGH)
- **Gamma-refined decomposition**: Sym^2_p(+1) + wedge^2_p(-1) + wedge^2_{ap}(+1) + Sym^2_{ap}(-1) (HIGH)

- **D moduli space dim = n^2(n^2+1)** at general n; closed-form formula (HIGH)
- **Dimension sequence**: n=1:2, n=2:20, n=3:90, n=4:272 (HIGH)
- **Sub-block constraints**: M_{12} = M_{12}^T, M_{21} = M_{21}^T, M_{22} = -M_{11}^T (HIGH)
- **Non-trivial D exists** at all n >= 1 (moduli space is never empty) (HIGH)
- **52 pytest tests pass** verifying all three axioms for every basis element at n=1,2,3,4 (HIGH)
- **n=1 moduli dim = 2** (not 1): J constraint trivially satisfied since J_+ = I at n=1 (HIGH)
- **Commutator [a,-] gets JD = -DJ** (epsilon' = -1 behavior), structural for all real symmetric a (HIGH)
- **SP operator sqrt(a)Xsqrt(a) is SWAP-even**, commutes with gamma (HIGH)
- **Barrett-form D with K real symmetric passes all 3 D axioms** at n=2,3,4 (HIGH)
- **Jordan product connection**: D_1(X) = 2(K*X) = linearized sequential product (HIGH)
- **Barrett subspace dim = n(n+1)/2**: n=2:3, n=3:6, n=4:10 (HIGH)
- **85 pytest tests pass** verifying all candidates at n=2,3,4 (HIGH)

- **[[D_K, L_a], R_b] = 0** for all a, b in M_n(C), all K in M_n(R)^sym -- first-order condition trivially satisfied for Barrett-form D (HIGH)
- **[D_1, L_a] = L_{[K,a]}** -- first commutator is pure left multiplication; commutativity with R_b follows from associativity (HIGH)
- **A_F = M_n(C)** (full algebra) for Barrett-form D -- no restriction from first-order condition (HIGH)
- **Gauge group U(n)** for Barrett D; at n=4: U(4), NOT U(1) x SU(2) x SU(3) (HIGH)
- **General D: A_F = C** (dim 1, gauge U(1)) for non-Barrett D from full moduli space (HIGH)
- **Master formula**: [[M, L_a], R_b](X) = sum_k [A_k, a] X [b, B_k]; Barrett is uniquely "pure-left type" (HIGH)
- **Discontinuous transition**: any non-Barrett perturbation drops A_F from M_n(C) to C (HIGH)
- **No D produces C + H + M_3(C)**: simple M_n(C) algebra cannot give SM -- requires direct sum structure (HIGH)
- **Medium success tier**: valid spectral triple with U(n) gauge group, but SM requires direct sum algebra (HIGH)
- **50 pytest tests pass** verifying first-order condition at n=2,3,4 for Barrett and general D (HIGH)

- **Peirce decomposition h_3(O) = V_1(1) + V_{1/2}(16) + V_0(10)** under E_11, dim check 1+16+10=27 (HIGH)
- **V_{1/2} = O^2 = S_9** (real Spin(9) spinor, dim_R = 16) (HIGH)
- **C*-observer forces V_{1/2}^C = S_{10}^+** (Weyl spinor of Spin(10), dim_C = 16) (MEDIUM)
- **Spin(9) -> Spin(10) upgrade** via branching rule S_{10}^+|_{Spin(9)} = S_9^C (HIGH)
- **Cross-check with Boyle 2020**: consistent identification of V_{1/2} as S_{10}^+ (HIGH)
- **Backtracking trigger NOT fired**: complexification follows from C*-nature alone (HIGH)
- **F_4 -> E_6 upgrade** tracked through Peirce: Aut -> Str_0, dim 52 -> 78 (HIGH)
- **Stab_{E_6}(E_11) = Spin(10) x U(1)**, dim 46, orbit = complexified Cayley plane dim 32 (HIGH)
- **27 -> 1 + 10 + 16** under Spin(10): 1=V_1^C, 10=V_0^C, 16=V_{1/2}^C=S_{10}^+ (HIGH)
- **V_0^C = 10 (vector)** verified via branching 10|_{Spin(9)} = 9+1 (HIGH)
- **Phase 18 verified**: 6/6 contract claims, 12/12 physics checks, consistency 27/27 (HIGH)

- **Cl(6) = Alg(gamma_1,...,gamma_6) subset Cl(10)** from O = C + C^3 splitting with u = e_7 (HIGH)
- **omega_6^2 = -1**, P = (1/2)(1 - i*omega_6), tr(P) = 16 on 32-dim Dirac spinor (HIGH)
- **Stab_{Spin(10)}(omega_6) = SU(4) x SU(2)_L x SU(2)_R / Z_2**, dim 21 = 15 + 6 (HIGH)
- **16 -> (4,2,1) + (4bar,1,2)** LEFT embedding verified (SU(2)_L on left-handed only) (HIGH)
- **Spin(10) -> Pati-Salam -> SU(3)_C x SU(2)_L x U(1)_Y** from single input u in S^6 (HIGH)
- **Furey Witt: 27/27 CAR verified, omega_6 = -i*(-1)^N**, automatic chirality (HIGH)
- **10/10 numerical tests pass** verifying Cl(6) algebra, volume form, stabilizer, Witt CAR (HIGH)
- **29/29 pytest tests pass** verifying explicit 32x32 Cl(10)/Cl(6) construction, Witt CAR, SU(2) algebras, and 16 SM quantum numbers (HIGH)
- **16 SM states matched**: u_L x3, d_L x3, nu_L, e_L, u_R x3, d_R x3, nu_R, e_R in Pati-Salam convention (HIGH)
- **Q distribution {-1:2, -1/3:6, 0:2, +2/3:6}** matches Pati-Salam SM exactly (HIGH)
- **Schwinger boson SU(2)_L x SU(2)_R**: full algebra + L-R commutativity + omega_6 commutativity verified (HIGH)

- **F_4 breaking by u:** [SU(3)_C x SU(3)_J]/Z_3 (dim 16) subset F_4 (HIGH)
- **SM from F_4 intersection:** Spin(9) cap [SU(3)xSU(3)]/Z_3 contains SU(3)_C x SU(2) x U(1) (dim 12) (HIGH)
- **Single-input theorem:** Both F_4 and Cl(6)/PS routes use same u in S^6 and same W = u^perp cap Im(O) (HIGH)
- **Chiral upgrade:** F_4 route = gauge algebra (no chirality); Cl(6) route = same algebra + LEFT embedding (HIGH)
- **Factor matching:** SU(3)_C = Stab_{G_2}(u) in both routes; SU(2) from Spin(4) in both; U(1) unique residual Cartan (HIGH)
- **9-link chain L1-L9** from self-modeling to chiral SM, all with status (HIGH)
- **Synthesis theorem** conditional on gaps A, B1, B2: one choice u gives gauge group + chirality (HIGH)
- **Gap register:** B1 rank-1 idempotent (HIGH), B2 complex structure (HIGH), A non-composability (MEDIUM), Gen generations (LOW), SA spectral action (LOW) (HIGH)
- **v5.0 milestone statement:** C*-observer probing h_3(O), upon choosing u, obtains SM gauge group with LEFT chirality (HIGH)

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
| 12-01 | 5min | 2 tasks | 10 files |
| 12-02 | 6min | 2 tasks | 5 files |
| 12-03 | 6min | 2 tasks | 8 files |
| 13-01 | 7min | 2 tasks | 1 files |
| 13-02 | 8min | 2 tasks | 1 files |
| 13-03 | 10min | 2 tasks | 1 files |
| 14-01 | 10min | 2 tasks | 2 files |
| 14-02 | 15min | 2 tasks | 2 files |
| 15-01 | 4min | 2 tasks | 2 files |
| 15-02 | 8min | 2 tasks | 2 files |

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
- [Phase 12, Plan 01]: MVEH framed as definitional via Connes-Rovelli thermal time hypothesis, not Assumption A5
- [Phase 12, Plan 01]: Derivation chain table (Table I) placed in introduction main text as structural spine
- [Phase 12, Plan 01]: Two gaps: continuum limit (standard, shared) and conformal approximation (minor). MVEH no longer a gap.
- [Phase 12, Plan 02]: Adopted Jacobson 2016 G = 1/(4 eta) in paper; MVEH dissolution uses exact phrasing from researcher lock
- [Phase 12, Plan 02]: Conformal approximation stated as honest caveat with Speranza 2016 reference
- [Phase 12, Plan 03]: All numerical results framed as "consistent with" / "supporting evidence", never "proves"
- [Phase 12, Plan 03]: 2D R^2=0.885 shortfall honestly noted with PBC wrapping explanation
- [Phase 0]: Started milestone v4.0: Spectral Triple from Self-Modeling — New milestone cycle -- spectral triple from self-modeling composite, targeting Standard Model via Connes classification
- [Phase 13, Plan 01]: Naive algebra action pi(a) = diag(a tensor I, a tensor I) used as primary; contragredient also satisfies order zero
- [Phase 13, Plan 01]: pi_o(b) = diag(I_n tensor b^T, I_n tensor b^T) derived via J antilinearity chain
- [Phase 13, Plan 02]: [gamma, pi(a)] = 0 fails for ALL non-scalar a -- only C*I satisfies even condition with SWAP-based chirality
- [Phase 13, Plan 02]: Three resolution paths: (a) different algebra action, (b) different gamma, (c) odd spectral triple
- [Phase 13, Plan 03]: Per-sector n^2 = k^2 is the correct CCM comparison (not naive 2n^2 = k^2); factor of 2 is J-doubling
- [Phase 13, Plan 03]: Barrett spinor space V = C^2; H = V tensor M_n(C) with two sectors
- [Phase 13, Plan 03]: A_F identification deferred to Phase 15; no premature SM claims
- [Phase 14, Plan 01]: D moduli space dim = n^2(n^2+1) at general n; involution constraint M = J_+ M^T J_+
- [Phase 14, Plan 01]: n=1 moduli dim is 2 (not 1): J constraint trivially satisfied since J_+ = I at n=1
- [Phase 14, Plan 01]: Barrett cross-check is partial -- Barrett's D includes first-order condition not yet imposed
- [Phase 14, Plan 01]: Sub-block constraints: M_{12} = M_{12}^T, M_{21} = M_{21}^T, M_{22} = -M_{11}^T
- [Phase 14, Plan 02]: Barrett J constraint requires K^T = K (symmetric), NOT K = scalar
- [Phase 14, Plan 02]: Barrett D_1(X) = KX + XK = 2(K*X) is twice the Jordan product = linearized sequential product
- [Phase 14, Plan 02]: KO-dim 6 epsilon'=+1 selects L_K + R_K (anticommutator) over L_K - R_K (commutator)
- [Phase 14, Plan 02]: Barrett subspace dim = n(n+1)/2 (10 at n=4); expected to match first-order condition subspace
- [Phase 15, Plan 01]: A_F = M_n(C) for Barrett-form D -- first-order condition is automatically satisfied for all a, b
- [Phase 15, Plan 01]: The proof reduces to [L_C, R_b] = 0 (associativity), same identity as order zero
- [Phase 15, Plan 01]: Gauge group U(n) at n=4 gives U(4), not SM -- structural consequence of simple algebra
- [Phase 15, Plan 01]: CCM difference is structural: simple M_n(C) vs direct sum M_2(H) + M_4(C)
- [Phase 15, Plan 02]: A_F = C (dim 1) for generic D from full moduli space; only Barrett D gives A_F = M_n(C)
- [Phase 15, Plan 02]: No intermediate subalgebra exists for simple M_n(C): only C or M_n(C)
- [Phase 15, Plan 02]: Medium success tier: valid spectral triple with U(n) gauge group, but SM requires direct sum algebra
- [Phase 15, Plan 02]: Master formula [[M, L_a], R_b](X) = sum_k [A_k, a] X [b, B_k] -- Barrett is pure-left type
- [Phase 0]: Started milestone v5.0: Chirality from h_3(O) via Cl(6) — New milestone cycle -- h_3(O)/Cl(6) route to chirality replaces spectral triple approach
- [Phase 18, Plan 01]: S_{10}^+ convention following Boyle 2020; chirality deferred to Phase 19
- [Phase 18, Plan 01]: Rank-1 idempotent e = E_11 taken as given input (Gap B step 1)
- [Phase 18, Plan 01]: Backtracking trigger NOT fired -- complexification follows from C*-nature alone
- [Phase 18, Plan 02]: U(1) charges (-4, 2, -1) recorded but physical meaning (B-L) deferred to Phase 19-20
- [Phase 18, Plan 02]: Local-to-global complexification noted as consistent completion, not formally necessary
- [Phase 19, Plan 01]: u = e_7 (Fano) as complex structure; Cl(10) via gamma_k x I + i*omega_6 x tau_a; P selects omega_6 = -i eigenspace (Todorov particle convention)
- [Phase 19, Plan 01]: Witt basis a_j = (1/2)(gamma_{2j-1} + i*gamma_{2j}); Furey octonion-label remapping deferred to Plan 02
- [Phase 19, Plan 01]: omega_6 separates chiralities before Pati-Salam breaking; LEFT not diagonal embedding
- [Phase 19, Plan 02]: Schwinger boson SU(2) from Cl(4) Witt: J3L = (m1+m2-1)/2, J3R = (m1-m2)/2
- [Phase 19, Plan 02]: B-L = 1 - (2/3)N for Pati-Salam assignment (N=1 quarks: +1/3, N=3 leptons: -1)
- [Phase 19, Plan 02]: Pati-Salam left-right symmetric convention: 16 contains L+R particles, same Q operator for both
- [Phase 19, Plan 02]: P selects omega_6 = +i eigenspace = odd N (N=1 quarks + N=3 leptons)
- [Phase 20, Plan 01]: [SU(3)xSU(3)]/Z_3 is maximal-rank subgroup of F_4, per Yokota and Adams
- [Phase 20, Plan 01]: SU(3)_C identified across F_4 and Cl(6)/PS routes via common complex structure J on W
- [Phase 20, Plan 01]: F_4 route provides gauge algebra only; Cl(6) route provides gauge algebra + chirality
- [Phase 20, Plan 01]: U(1) matching via rank counting (rank 4 = rank F_4, minus SU(3) and SU(2) Cartans leaves 1)
- [Phase 20, Plan 02]: Gap B steps 1 and 2 classified as structurally independent (Spin(9) contains G_2 acting transitively on S^6)
- [Phase 20, Plan 02]: Synthesis theorem stated as conditional on 3 gaps (A, B1, B2), not unconditional
- [Phase 20, Plan 02]: Generation structure and spectral action classified as LOW severity for this paper

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

**Last session:** 2026-03-23
**Stopped at:** Phase 18 complete and verified; Phase 19 ready to plan
**Resume file:** --
