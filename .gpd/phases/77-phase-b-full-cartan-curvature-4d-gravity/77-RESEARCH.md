# Phase 77: Phase B — Full Cartan Curvature = 4d Gravity — Research

**Researched:** 2026-06-02
**Domain:** Mathematical physics — MacDowell-Mansouri/Cartan gauge gravity; exact-over-Q symbolic differential geometry of a Lorentzian (1,3) slice of the h_3(O) cone; spin connection / Riemann curvature of the soldering-form metric g=e·e
**Confidence:** HIGH on the formulas, the in-repo machinery to reuse, and the fp-relabel discipline; MEDIUM on the genuinely-open outcome (will R[ω]≠0 for M≠0, and is the vacuum Einstein) — those are what the phase exists to MEASURE.

## Summary

Phase 77 is the real gravity gate of v18.0. The cheap gates (Phase 75 coframe-reduction SURVIVES; Phase 76 Berry SOFT-KILL OVERTURNED — Berry curvature is the internal SU(4) sector, NOT gravity) have cleared the runway. The locked object (CONVENTIONS §11) is unambiguous: **gravity = the Lorentz block R[ω] of F=dA+A∧A, which is the Riemann curvature of the soldering-form metric g = e·e**, where e = π_u(dE) is the forced 4d Lorentzian (1,3) coframe from Phase 75. The pre-check (commit f0e544a6) already established g=e·e is the (1,3) η baseline, DIFFERENT from the v17.0 (4,0) cone-Hessian — so this is a genuine new test, not a redundant v17.0 re-kill.

The phase is essentially **standard tetrad gravity executed exact-over-Q on a position-dependent metric g(x) built from the h_3(O) idempotent field E(x)**, with a hard flatness STOP gate up front. The method family (MM/Cartan) is locked by contract; the genuinely-uncertain mechanics are four: (1) how to introduce position-dependence into E(x)→g(x) [the crux], (2) how to extract ω(e) exact over Q, (3) how to assemble A=ω⊕e, compute F, and cross-check R(ω) against an independent Levi-Civita Riemann, and (4) how to test Einstein/matter-sourcing WITHOUT fp-relabel. All four have a concrete in-repo template from the v17.0 harness. The verbatim Wise MM and closed-form Levi-Civita spin-connection formulas the executor needs (executor has no web access) are surfaced below.

**Primary recommendation:** Build g(x)=e·e(x) as the matter-on-flat metric `g = η_bg + h(x;M)` using the EXISTING v17.0 pipeline (`spacetime_curvature_of_g` / `_matterless_reference_hessian` / `offcenter_slice_metric` as the position-dependence template), but **the load-bearing curvature is R[ω] from the closed-form Levi-Civita spin connection ω(e), wedged via F=dA+A∧A — NOT the cone-Hessian Totaro Riemann** (which is the fp-reuse-cone-hessian foil, allowed only as the symmetric/real-part consistency cross-check). Compute R[ω] two ways (closed-form spin connection → second Cartan structure equation, AND the independent `hand_rolled_riemann_of_g`/`totaro_riemann` Levi-Civita Riemann of g) and require exact agreement over Q on ≥5 components. The flatness sub-gate is the first task: build g for one sample M≠0, compute R[ω], STOP if zero.

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| --- | --- | --- | --- | --- |
| **CONVENTIONS.md §11** (Cartan/MM lock) | convention SSOT | Defines gravity = R[ω] = Riemann of g=e·e; Berry≠gravity; A=ω+(1/ℓ)e; F=R[ω]−(Λ/3)e∧e+d_ωe | LOAD as ASSERT_CONVENTION header; cite the locked symbol table | every plan, every driver header, verification |
| **CONVENTIONS.md §6** (Λ=0, flat vacuum) | convention SSOT | M=0 vacuum is flat KKT η (DERIVED, not Λ-negative); "center Einstein-negative Λ<0" is FALSIFIED | Expect flat/pure-Λ at M=0; do NOT reintroduce R×H³ or Λ<0 | B(d) vacuum task, verification |
| **CONVENTIONS.md §1** (K=−1/2 benchmark) | sign benchmark | Pins Riemann/Ricci sign convention (negative & constant; magnitude −1/2 cone-Hessian, −1 round) | Re-run `h3_cone_hessian_benchmark()` to pin signs BEFORE reading any curvature verdict | B(b)/B(c) sign-pinning, verification |
| **code/cartan_phaseB_metric_precheck.py** (commit f0e544a6) | prior artifact | g=e·e=(1,3) η baseline ≠ (4,0) cone-Hessian; frozen index layout V_HALF={11..26}, CU_SURVIVOR=[11,18,19,26], CU4=[1,2,3,10] | REUSE `G_DET2_RAW`, the frozen indices, `to_mink`; build on it (it does NOT build ω/Riemann/Einstein/T) | B(a) coframe task |
| **code/cartan_phaseA_coframe.py** + **derivations/75-coframe-reduction.tex** | prior artifact (SURVIVED) | e=π_u(dE) is the established 4d (1,3) coframe; survivors {11,18,19,26}=C_u²; residual 21=so(3,1)⊕so(6), SO(3,1) FORCED | CITE as the established coframe; B confirms non-degeneracy det(e^a_μ)≠0 | B(a) |
| **code/bulk_geometry_verification.py** (3119 lines) | reuse engine | The v17.0 Totaro + hand-rolled Levi-Civita Riemann harness + matter-on-flat pipeline + K=−1/2 benchmark | REUSE `totaro_riemann`, `hand_rolled_riemann_of_g`, `spacetime_curvature_of_g`, `_matterless_reference_hessian`, `ricci_decomposition_n4`, `eig_signature_count`, `_frame_jacobian_bg_to_mink`, `_eta_minkowski`, `h3_cone_hessian_benchmark` | B(a)-B(d), all curvature work |
| **code/ring_lemma_verification.py** (det SSOT) | reuse engine | Exact-over-Q octonion/Jordan arithmetic (det_3, jordan, Tr); octonion_algebra.py BANNED | ALL octonion arithmetic routes through here; source-guard asserts octonion_algebra absent | every driver |
| **derivations/73-einstein-structure.tex** (Eq. Tpsi, kappas) | method precedent | The EXACT independent-T construction that defeated fp-relabel in v17.0: T[ψ]=∂ψ∂ψ−½η(∂ψ)², ψ=2Re((x2x1)x3), AST-guarded, M=t·M_0 power-counting, single global (κ,Λ) | REPLICATE the independent-T discipline for B(d) matter-sourcing | B(d) Einstein/matter task, verification |
| **Wise, gr-qc/0611154** (verbatim eqs below) | benchmark reference | THE reference: A=ω+(1/ℓ)e; F=(R−(Λ/3)e∧e)+d_ωe; ℓ²=3/Λ; SO(4,1) dS / SO(3,2) AdS | Use the verbatim formulas (executor has NO web) | B(c) assembly |
| **derivations/52-kkt-spacetime.tex** | prior artifact | Minkowski coord map x0=(β+γ)/2, x1=Re(x1)=p, x2=⟨x1,e7⟩=q, x3=(β−γ)/2; det_2=x0²−x1²−x2²−x3²; SO(3,1) boosts B_i=L_{σ_i}, Killing sig (3,3) | Use the coordinate map and (1,3) target | B(a), index bookkeeping |

**Missing or weak anchors:** None blocking. NOTE the index-frame ambiguity: §12.tex (KKT) and the original prompt cite the spacetime sub-slice as engine indices **{17,18,19,26}**, but the LIVE precheck/Phase-75 layout uses **CU4_IDX=[1,2,3,10]** for the V_0 slice coords {β,γ,p,q} and **CU_SURVIVOR=[11,18,19,26]** for the V_{1/2} survivors. The {17,18,19,26} in the prompt conflates the two. **The authoritative live layout is the precheck's: slice coords (the g(x) base) = engine idx [1,2,3,10]; V_{1/2} coframe survivors = [11,18,19,26].** The planner must lock this in the plan header to prevent an index slip.

## Conventions

| Choice | Convention | Source |
| --- | --- | --- |
| Metric signature (slice) | **mostly-minus (+,−,−,−)** timelike-positive Lorentzian (1,3); η=diag(+1,−1,−1,−1) | CONVENTIONS §1, §11 |
| Det / cubic norm SSOT | `ring_lemma_verification.py det_3`, cross-term `2Re(x2* x0* x1)`; octonion_algebra.py BANNED | CONVENTIONS §0 |
| Exactness | EXACT over Q on every decisive verdict; sympy.Matrix.rank/eigenvals/real_roots over QQ, NEVER numpy.linalg | CONVENTIONS §2 |
| Riemann/Ricci sign | NEGATIVE & constant; cone-Hessian K=−1/2, round H³ K=−1 (factor 2). Engine Totaro convention `R_ijkl = −(1/4) g^{pq}(C_jlp C_ikq − C_ilp C_jkq)` | CONVENTIONS §1; `h3_cone_hessian_benchmark()` |
| Cosmological constant | Λ=0 at M=0 (flat KKT η, DERIVED). Λ<0 / R×H³ FALSIFIED — do NOT reintroduce | CONVENTIONS §6 |
| Idempotent / Peirce | E_11=diag(1,0,0); V_1={0}, V_0={1..10}, V_{1/2}={11..26}; u=e_7, C_u=span{1,e_7} | CONVENTIONS §11 |
| Slice coords (g base) | engine idx **[1,2,3,10]** = (β,γ,p,q) = h_2(C_u)≅R^{3,1} | precheck CU4_IDX |
| V_{1/2} coframe survivors | engine idx **[11,18,19,26]** = C_u² (π_u survivors) | precheck CU_SURVIVOR_IDX |

**CRITICAL:** the engine `hand_rolled_riemann_of_g` carries an explicit OVERALL MINUS so its Levi-Civita Riemann matches the Totaro engine's sign convention (pinned to K=−1/2 hyperbolic for the cone-Hessian). Any new spin-connection Riemann must be reconciled to the SAME convention before comparison — verify on the cone-Hessian benchmark first (the uniform −1 global-sign check is already documented in the engine, lines 2299-2310).

## Mathematical Framework

### Key Equations and Starting Points (VERBATIM — executor has no web access)

**(1) Wise MM/Cartan connection and curvature** (gr-qc/0611154, p.3, verbatim):

```
  A = ω + (1/ℓ) e            [ℓ a constant with units of length]

  F = ( R − (Λ/3) e ∧ e ) + d_ω e        [we choose ℓ² = 3/Λ]
        \_____________/       \_____/
         so(3,1) Lorentz       R^{3,1} translation
         block                 block (TORSION)
```
- The so(3,1) (Lorentz) part of F = the curvature R[ω] PLUS a cosmological-constant term `−(Λ/3) e∧e`.
- The R^{3,1} (translation/transvection) part of F = the torsion `d_ω e = de + ω∧e`.
- F[A] vanishes precisely when ω is the torsion-free spin connection for a spacetime locally isometric to de Sitter.
- Gauge group: **SO(4,1) for Λ>0 (dS)**, **SO(3,2) for Λ<0 (AdS)**, Poincaré ISO(3,1) for Λ=0.
- MM action (Phase C, NOT Phase B): `S_MM = (−3/2GΛ) ∫ tr(F̂ ∧ ⋆F̂)`, F̂ = projection into so(3,1), ⋆ = internal Hodge star. **Phase B does NOT use this action** (fp-imported-action) — it computes F=dA+A∧A intrinsically.
- Palatini equivalence (context only): `S_Pal = S_MM − (3/2GΛ) ∫ tr R∧⋆R` (differ by topological term).

**(2) Closed-form torsion-free Levi-Civita spin connection from the tetrad** (verbatim, cross-confirmed Wikipedia + HandWiki):

```
  ω_μ^{ab} =  (1/2) e^{νa}( ∂_μ e_ν^b − ∂_ν e_μ^b )
            − (1/2) e^{νb}( ∂_μ e_ν^a − ∂_ν e_μ^a )
            − (1/2) e^{ρa} e^{σb}( ∂_ρ e_σ^c − ∂_σ e_ρ^c ) e_{μc}
```
Antisymmetric in (a,b) by construction. Uses ONLY the tetrad e^a_μ and its first partials — no Christoffel symbols. This is the cleanest exact-over-Q route for B(b).

**(3) Cartan structure equations** (verbatim):

```
  First (torsion):   Θ^a = d e^a + ω^a_b ∧ e^b           [= 0 for Levi-Civita]
  Second (curvature): R^a_b = d ω^a_b + ω^a_c ∧ ω^c_b = (1/2) R^a_{bcd} e^c ∧ e^d
```

**(4) Curvature-2-form → Riemann tensor index conversion** (standard; the executor's bookkeeping):

```
  R^{ab}_{μν} = ∂_μ ω_ν^{ab} − ∂_ν ω_μ^{ab} + ω_μ^{ac} ω_{νc}^{b} − ω_ν^{ac} ω_{μc}^{b}
  R^ρ_{σμν} = e_a^ρ e^b_σ R^{ab}_{μν}        [frame (ab) → coordinate (ρσ) via tetrad]
  R_{ρσμν}  = g_{ρλ} R^λ_{σμν}                [lower with g = e·e]
```
This is the bridge between the Cartan R(ω)^{ab}_{μν} and the metric Riemann R_{ρσμν} that the cross-check compares.

**(5) Soldering-form metric** (the locked g):

```
  g_{μν} = η_{ab} e^a_μ e^b_ν              [g = e·e, signature (1,3)]
```
where η=diag(+1,−1,−1,−1) and e^a_μ is the tetrad. In the live layout this is `G_DET2_RAW` in raw {β,γ,p,q} coords = `J^T diag(+1,−1,−1,−1) J` (J = `_frame_jacobian_bg_to_mink`).

### Required Techniques

| Technique | What It Does | Where Applied | In-Repo Anchor |
| --- | --- | --- | --- |
| Closed-form Levi-Civita spin connection | ω(e) from tetrad + first partials, no Christoffels | B(b) | formula (2) above; new code |
| Cartan structure equations | F=dA+A∧A as component-matrix curvature | B(c) | formula (3),(4); new code (hand-rolled matrix wedge) |
| Symbolic-then-substitute differentiation | differentiate g(x) symbolically in 4 slice coords, evaluate at rational point (avoids the >200s all-symbolic inverse cliff / watchdog) | B(a)-B(d) | `spacetime_curvature_of_g` lines 2199-2227, `hand_rolled_riemann_of_g` lines 2276-2288 |
| Matter-on-flat metric construction | g=η_bg + [H(bg+M) − H(bg)] so M=0 ⇒ g=η over a neighbourhood (flat baseline) | B(a) position-dependence, B(d) | `_matterless_reference_hessian`, `spacetime_curvature_of_g` |
| Exact signature counting | (1,3) check via real_roots on charpoly over Q (NOT Sylvester — null-aligned frame) | B(a), B(d) | `eig_signature_count` line 2369 |
| Independent stress-energy + power counting | T[M] AST-guarded, M=t·M_0, single global (κ,Λ) | B(d) | derivations/73 Eq.Tpsi; replicate |

### Approximation Schemes

| Approximation | Small Parameter | Regime / Note | Alternatives |
| --- | --- | --- | --- |
| Linear-in-tetrad spin connection | — | ω is exact in e (formula 2 is exact, not perturbative); no approximation | — |
| M = t·M_0 power expansion | t (matter amplitude) | Used ONLY to extract leading M-power of curvature vs T (the fp-relabel order-match test); the curvature itself is computed exactly at finite M | finite-M evaluation (also done; both required) |
| Evaluate at rational slice point | — | Differentiate symbolically, substitute a rational (β,γ,p,q) basepoint BEFORE matrix inverse → exact over Q, fast | fully-symbolic (watchdog blowup — AVOID) |

## Standard Approaches

### Approach 1: Closed-form Levi-Civita spin connection ω(e), then F=dA+A∧A (RECOMMENDED)

**What:** Build the tetrad e^a_μ(x) as a 4×4 matrix field (μ = slice coords [1,2,3,10], a = Minkowski frame), invert it, apply the closed-form spin-connection formula (2), assemble A=ω⊕e, compute F by the component-matrix formula F_{μν}=∂_μA_ν−∂_νA_μ+[A_μ,A_ν], extract the Lorentz block R(ω)^{ab}_{μν}, convert to R^ρ_{σμν} (formula 4), and identify with the Riemann tensor of g=e·e.

**Why standard:** This is textbook tetrad/Palatini gravity. The closed-form ω(e) (formula 2) is preferred over the reductive `f_4/e_6` ambient-Spin(9,1)-projection route because (a) it is purely 4d differential geometry — no need to construct the 45-dim ambient connection and project; (b) it is manifestly exact over Q (rational functions of the tetrad and its partials); (c) it is torsion-free by construction, so the torsion block d_ωe vanishes identically, isolating the Lorentz block cleanly; (d) it is directly cross-checkable against the in-repo Levi-Civita Riemann harness.

**Track record:** The in-repo `hand_rolled_riemann_of_g` (lines 2236-2326) already does the Christoffel→Riemann version of exactly this, validated against Totaro on the cone-Hessian (uniform sign agreement on 9 components). The spin-connection route is the tetrad-formalism sibling.

**Key steps:**
1. Build e^a_μ(x): the tetrad such that g_{μν}=η_{ab}e^a_μe^b_ν = the matter-on-flat g(x). Cleanest: take e = a "square root" of g via the frame map. Since g=J^T η J + h(x) with h the matter perturbation, write e^a_μ = (the constant Phase-75/52-kkt frame map J) at M=0, and for M≠0 build e by Cholesky-like/Gram-Schmidt factorization of g(x) over Q, OR (cleaner) carry e directly as `e = π_u(dE)` evaluated symbolically. **DECISION FOR PLANNER (see Open Q1).**
2. Invert e^a_μ → e_a^μ exact over Q (at a rational basepoint after symbolic differentiation).
3. ω_μ^{ab} via formula (2) — symbolic in e and ∂e, evaluated at the rational point.
4. F_{μν} = ∂_μω_ν − ∂_νω_μ + [ω_μ,ω_ν] (component-matrix; the [·,·] is the A∧A term). For the assembled A=ω⊕e, the Lorentz block is R(ω)+Λe∧e and the translation block is d_ωe.
5. R^ρ_{σμν} = e_a^ρ e^b_σ R(ω)^{ab}_{μν}; lower with g.

**Known difficulties at each step:**
- Step 1: the square-root/factorization of g(x) is non-unique up to local SO(3,1) — but R[ω] is invariant under that frame freedom, so any valid e works; verify by checking g=e·e exactly. Carrying e=π_u(dE) symbolically may be cleaner and ties to the algebraic source (preferred if tractable).
- Step 3: formula (2) has internal-index contractions; index-raising e^{νa} uses the INVERSE tetrad, not g. Bookkeeping must be exact.
- Step 4: `sympy.diffgeom` has NO matrix-valued connection wedge — hand-roll the component-matrix curvature (the commutator IS the A∧A term). Confirmed in METHODS.md.

### Approach 2: Reductive Spin(9,1)→Spin(3,1) ambient projection (CROSS-CHECK / FALLBACK)

**What:** Extract ω as the Lorentz Spin(3,1) sub-block of the ambient Spin(9,1) connection via the reductive split g=h⊕m (f_4/e_6 canonical connection).
**When to switch:** If Approach 1's tetrad factorization proves intractable, OR as an independent cross-check of ω's Lorentz block (the contract names this as the "canonical reductive split" alternative).
**Tradeoffs:** Requires building the 45-dim ambient connection and the non-compact so(3,1)⊂so(9,1) sub-block extraction (the e_{6(-26)} real form) — heavier, and the contract explicitly warns "do NOT use the raw 45-dim Spin(9,1) curvature." Use only the projected 6-dim Lorentz block. Confidence MEDIUM that this agrees cheaply; Approach 1 is cleaner.

**RECOMMENDATION:** Approach 1 (closed-form ω(e)) PRIMARY. The independent Riemann cross-check (test-cartan-curvature) is satisfied by comparing R(ω) [Approach 1, via spin connection] against `hand_rolled_riemann_of_g` / `totaro_riemann` of g [the metric Levi-Civita Riemann] — two genuinely independent computations of the SAME tensor. Approach 2 is an optional third leg, not required.

### Anti-Patterns to Avoid

- **fp-reuse-cone-hessian:** Using the v17.0 cone-Hessian (4,0) Totaro Riemann as the load-bearing gravity tensor. It is the REAL/symmetric sector (different tensor). Allowed ONLY as a soft consistency cross-check (Re(QGT) sanity). The load-bearing R[ω] is the Riemann of the (1,3) g=e·e via the spin connection.
  - _Example:_ calling `cone_hessian_at_center` and feeding it to `totaro_riemann` and calling the result "the gravity curvature" — WRONG. Feed g=e·e (the (1,3) η baseline) to the Levi-Civita Riemann instead.
- **Raw 45-dim Spin(9,1) curvature:** gravity = the 10-dim A=ω⊕e; extract the Spin(3,1) Lorentz 6-dim block, never the raw 45-dim curvature.
- **fp-relabel:** declaring "R(ω) satisfies Einstein" because some 2-form equation holds, WITHOUT an independently-built T[M] matched in magnitude + tensor structure + M-power. The v17.0 Ph73 lesson: G_00≈6151 where T_00=0; κT~10³ off.
- **fp-float-decisive:** any det(e), signature, or curvature verdict resting on numpy.linalg. Use sympy over QQ.
- **fp-imported-action:** positing the MM action `∫ε F∧F` to make Einstein appear — that is Phase C (78), not B. Phase B computes F=dA+A∧A intrinsically.
- **Fully-symbolic matrix inverse:** the >200s watchdog cliff. Differentiate symbolically, substitute rational basepoint, THEN invert (the engine's documented strategy).

## Existing Results to Leverage

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
| --- | --- | --- | --- |
| Coframe is 4d Lorentzian (1,3), SO(3,1) forced | dim π_u(V_{1/2})=4; survivors {11,18,19,26}; residual 21=so(3,1)⊕so(6) | derivations/75; cartan_phaseA_coframe.py | CITE — B confirms only det(e)≠0 non-degeneracy |
| g=e·e is (1,3) η baseline ≠ (4,0) cone-Hessian | `G_DET2_RAW`=[[0,½,0,0],[½,0,0,0],[0,0,−1,0],[0,0,0,−1]], eigenvalues {½,−½,−1,−1} | cartan_phaseB_metric_precheck.py (f0e544a6) | CITE as the base metric; build g(x) on it |
| Minkowski coord map | x0=(β+γ)/2, x1=p, x2=q, x3=(β−γ)/2; det_2=x0²−x1²−x2²−x3² | derivations/52-kkt-spacetime.tex; `_frame_jacobian_bg_to_mink` | the frame map J (det=−1/2) |
| K=−1/2 sign benchmark | cone-Hessian H³ sectional K=−1/2 (constant, negative); round K=−1 | `h3_cone_hessian_benchmark()`; CONVENTIONS §1 | pin Riemann sign BEFORE any verdict |
| Wise MM decomposition | F=(R−(Λ/3)e∧e)+d_ωe; ℓ²=3/Λ | gr-qc/0611154 p.3 | the verdict template for B(c) |
| Closed-form spin connection | formula (2) above | Wikipedia/HandWiki Spin_connection | B(b) primary route |
| Independent-T template | T[ψ]=∂ψ∂ψ−½η(∂ψ)², ψ=2Re((x2x1)x3); AST-guarded; M=t·M_0; single global (κ,Λ) | derivations/73 Eq.Tpsi | B(d) fp-relabel defeat |
| v17.0 NONE does NOT bind | g=e·e is the antisymmetric/Lie sector; v17.0 was the symmetric/real sector | CONVENTIONS §11; SUMMARY.md | B is a genuine new test |

**Key insight:** the entire 4d-differential-geometry toolchain (Christoffel, Levi-Civita Riemann, Ricci decomposition, signature, K-benchmark) is already built, validated, and warm in `bulk_geometry_verification.py`. The ONLY genuinely new code is (i) the tetrad e^a_μ(x) construction and (ii) the closed-form spin connection ω(e) → F=dA+A∧A component-matrix curvature. Everything else is reuse.

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
| --- | --- | --- | --- |
| η_bg in (β,γ,p,q) frame | `_eta_bg_const()` / `J^T diag(+1,−1,−1,−1) J` | bulk_geom line 2430 | the M=0 flat baseline metric |
| matter-on-flat h(x;M) | `H_source(x;bg+M) − H_source(x;bg)`, =0 at M=0 identically | `spacetime_curvature_of_g` | the position-dependent perturbation |
| difference-potential cubic form C | C(M=0)=0 identically ⇒ curvature vanishes at M=0 on the nose | `spacetime_curvature_of_g` step (b) | for the Totaro route only (cone-Hessian cross-check) |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| --- | --- | --- | --- | --- |
| MacDowell-Mansouri gravity & Cartan geometry | D.K. Wise | 2010 (gr-qc/0611154, 2006) | THE reference | F decomposition, A=ω+(1/ℓ)e, ℓ²=3/Λ, SO(4,1)/SO(3,2) |
| Original MM mechanism | MacDowell & Mansouri | 1977 (PRL 38,739) | the source | gravity = broken dS/Lorentz gauge theory |
| Cartan's Generalization (soldering) | Sharpe | 1997 | rigorous soldering-form def | g=e*η, reductive split g=h⊕m |
| KKT spacetime slice | in-repo Phase 52 | — | h_2(C_u)≅R^{3,1} (1,3); boosts B_i=L_{σ_i} Killing sig (3,3) | the (1,3) target, SO(3,1) realization |

## Computational Tools

### Core Tools

| Tool | Module | Purpose | Why Standard |
| --- | --- | --- | --- |
| SymPy 1.14.0 | Matrix, diff, Rational, real_roots, cancel | exact-over-Q symbolic differential geometry | the project SSOT; exact, deterministic |
| `bulk_geometry_verification.py` | totaro_riemann, hand_rolled_riemann_of_g, spacetime_curvature_of_g, _matterless_reference_hessian, ricci_decomposition_n4, eig_signature_count, h3_cone_hessian_benchmark, _frame_jacobian_bg_to_mink, _eta_minkowski, _eta_bg_const | the warm v17.0 curvature + matter-on-flat harness | validated, exact over Q, watchdog-safe |
| `ring_lemma_verification.py` | det_3, jordan, Tr, h3o_from_coords, X_from_symbols, _standard_basis_27 | det SSOT + exact octonion/Jordan arithmetic | certified F_4-invariant; octonion_algebra.py BANNED |
| `embedding_under_E_verification.py` | E() / proj_u_exact | the literal π_u soldering map (e=π_u(dE)) | the Phase-46/75 C_u bottleneck |
| `cartan_phaseB_metric_precheck.py` | G_DET2_RAW, to_mink, frozen indices | the g=e·e base metric + index layout | already done (f0e544a6) |

### Supporting Tools

| Tool | Purpose | When to Use |
| --- | --- | --- |
| sympy `simplify`/`cancel` | per-entry exact simplification (use `cancel` for rational-function speed) | every matrix op |
| AST guard (replicate from 73) | assert no Ric/R/G symbol enters T[M] construction | B(d) T-build |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
| --- | --- | --- |
| Hand-rolled component-matrix F | `sympy.diffgeom` | diffgeom has NO matrix-valued connection wedge — insufficient; hand-roll |
| Closed-form ω(e) [Approach 1] | reductive Spin(9,1) projection [Approach 2] | Approach 2 heavier (45-dim ambient); use as optional cross-check |
| Tetrad factorization of g | carry e=π_u(dE) symbolically | factorization non-unique up to SO(3,1) (R[ω] invariant); π_u(dE) ties to source — planner decides |

### Computational Feasibility

| Computation | Estimated Cost | Bottleneck | Mitigation |
| --- | --- | --- | --- |
| ω(e) + F at one rational basepoint | seconds | symbolic diff of tetrad entries | differentiate symbolically, substitute rational point before inverse |
| Riemann cross-check ≥5 components | seconds-to-minutes | the Levi-Civita Riemann at the point | already watchdog-safe in `hand_rolled_riemann_of_g` |
| Full G[g] over (M,x) family (B(d)) | minutes | per-point matrix inverse + Ricci contraction | the v17.0 Ph73 family (12 valid points) ran fine; reuse the pattern |
| Fully-symbolic g.inv() | >200s (WATCHDOG KILL) | symbolic 4×4 inverse of rational-function entries | NEVER do this — substitute rational point first |

**Installation / Setup:** No new packages. Python 3.14.x / SymPy 1.14.0 already present. NumPy is loaded by the engine ONLY in fenced float-triage helpers (lines 2705, 2737) — keep it OFF the decisive path.

```bash
# No installation needed. Verify the warm engine imports:
python3 -c "import sys; sys.path.insert(0,'code'); import bulk_geometry_verification, ring_lemma_verification; print('OK')"
```

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| --- | --- | --- | --- |
| g = e·e exactly | the tetrad reproduces the locked (1,3) metric | `simplify(η_ab e^a_μ e^b_ν − G_DET2_RAW) == 0` | exact zero over Q |
| det(e^a_μ) ≠ 0 | genuine invertible tetrad (B(a)) | sympy det over Q at sample point(s) | nonzero rational |
| Riemann algebraic symmetries | engine correctness | `riemann_symmetry_ok(R,4)` | True (antisym (ij),(kl); pair sym) |
| **R(ω) == Levi-Civita Riemann of g on ≥5 comps** | THE cross-check (test-cartan-curvature; defeats fp-relabel) | compare R^ρ_{σμν}[ω] vs `hand_rolled_riemann_of_g(g)` after sign-reconcile | exact agreement over Q |
| torsion d_ωe = 0 | ω is the Levi-Civita (torsion-free) connection | `de + ω∧e == 0` (formula 1) | exact zero (by construction of formula 2) |
| sign-pin on cone-Hessian | the spin-connection Riemann is in the K=−1/2 convention | run the new Riemann on the cone-Hessian, compare to `h3_cone_hessian_benchmark` | uniform sign factor (reconcile global minus) |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| --- | --- | --- | --- |
| M=0 vacuum | matter off | g=η flat; R[ω]=0 (flat); Λ=0 | CONVENTIONS §6 (DERIVED flat); precheck |
| H³ sectional curvature | det_2=1 sub-slice | K=−1/2 (cone-Hessian), −1 (round) | `h3_cone_hessian_benchmark` |
| Flatness sub-gate | one sample M≠0 | R[ω]≠0 EXPECTED (else trivial death STOP) | the open question |

### Numerical Validation

| Test | Method | Tolerance | Reference |
| --- | --- | --- | --- |
| all decisive numbers | sympy over QQ | EXACT (zero tolerance) | — |
| signature (1,3) | `eig_signature_count` via real_roots | exact sign of algebraic roots | (1,3,0) |
| det(e), curvature comps | sympy.Matrix.det / Rational entries | exact rationals | — |

### Red Flags During Computation

- **R[ω]=0 for M≠0** at the flatness sub-gate → rigid/integrable soldering, pure-gauge, NO gravity → honest trivial-death STOP (the v18.0 analog of the v17.0 homogeneity dealbreaker).
- **det(e^a_μ)=0** at a generic point → degenerate soldering form, not a genuine tetrad → coframe non-invertibility KILL.
- **R(ω) ≠ Levi-Civita Riemann of g** → an error in ω extraction or index conversion (NOT a physics result) — debug before any verdict.
- **Nonzero torsion d_ωe ≠ 0** with the closed-form ω → an implementation bug (formula 2 is torsion-free by construction).
- **Signature flips to (4,0) Euclidean** at finite M → the matter perturbation left the Lorentzian splice (v17.0 dropped 6/18 such points, did not force them) — drop the point, do not force.
- **κT and G[g] differ by orders of magnitude / support mismatch** → the v17.0 fp-relabel signature; report as NOT Einstein, do not round a near-miss.

## Common Pitfalls

### Pitfall 1: Reusing the cone-Hessian Riemann as load-bearing (fp-reuse-cone-hessian)

**What goes wrong:** computing the Totaro Riemann of `cone_hessian_at_center` (the (4,0) symmetric-sector metric) and calling it "the gravity curvature."
**Why it happens:** the warm `totaro_riemann`/`spacetime_curvature_of_g` pipeline is built around the cone-Hessian; it is the path of least resistance.
**How to avoid:** feed g=e·e (the (1,3) η baseline, `G_DET2_RAW`+matter perturbation) — NOT the cone-Hessian — to the Levi-Civita Riemann. The load-bearing curvature is R[ω] from the spin connection of g=e·e. Use the cone-Hessian ONLY as the soft Re(QGT) consistency cross-check.
**Warning signs:** the metric being differentiated has signature (4,0); the basepoint is the center I/3 with diag(9,9,18,18).
**Recovery:** switch the metric to g=e·e (1,3); re-derive ω(e) from it.

### Pitfall 2: fp-relabel — declaring Einstein without an independent matched T[M]

**What goes wrong:** "R_μν ∝ g_μν holds for some Λ" or "a stress-tensor-shaped object appears" reported as Einstein, without matching an independently-built T[M] in magnitude + tensor structure + M-power.
**Why it happens:** a 2-form curvature always admits SOME decomposition; the temptation is to relabel it.
**How to avoid:** replicate the derivations/73 discipline EXACTLY: build T[ψ]=∂ψ∂ψ−½η(∂ψ)², ψ=2Re((x2x1)x3), AST-guarded (assert NO Ric/R/G symbol in its construction), frozen BEFORE computing G[g]; use M=t·M_0 to extract the leading t-power; require the SAME leading order (T[ψ]~t⁴ matched R~t⁴ in v17.0); fit a SINGLE global (κ,Λ); report the residual honestly.
**Warning signs:** κ fitted per-point; "leading-order Einstein" fallback; rounding a 10³ mismatch.
**Recovery:** report NONE / not-Einstein at true strength (negative-result-is-success).

### Pitfall 3: The index-frame slip ({17,18,19,26} vs [1,2,3,10]/[11,18,19,26])

**What goes wrong:** the prompt/§12.tex cite "spacetime sub-slice indices {17,18,19,26}" but the LIVE layout uses slice coords [1,2,3,10] (the g base) and V_{1/2} survivors [11,18,19,26]. Mixing them corrupts the tetrad.
**Why it happens:** two different index frames (engine-native V_0 slice vs V_{1/2} half-eigenspace), historically conflated.
**How to avoid:** lock the live layout in the plan header: **g(x) base = engine idx [1,2,3,10]=(β,γ,p,q); coframe survivors = [11,18,19,26]**. Use the precheck's frozen constants verbatim.
**Warning signs:** g built on indices {17,18,19,26}; signature comes out wrong.
**Recovery:** re-index to [1,2,3,10] for the base.

### Pitfall 4: Watchdog kill on fully-symbolic matrix inverse

**What goes wrong:** the long-symbolic-run watchdog (~150-600s) kills a fully-symbolic 4×4 `g.inv()` of rational-function entries (the >200s cliff).
**Why it happens:** symbolic inversion of dense rational-function matrices blows up.
**How to avoid:** differentiate g SYMBOLICALLY (cheap per-entry), then SUBSTITUTE a rational (β,γ,p,q) basepoint, THEN invert (rational 4×4 — fast). This is the documented engine strategy (`hand_rolled_riemann_of_g` lines 2276-2288). Run foreground with `python -u`; commit task-by-task; the orchestrator may need to commit+SUMMARY on a stall (see MEMORY feedback_executor_watchdog_stall).
**Warning signs:** a driver hangs >150s with no output.
**Recovery:** kill, switch to substitute-then-invert; work is committed task-by-task.

### Pitfall 5: Sign-convention mismatch between the new spin-connection Riemann and the engine

**What goes wrong:** the bare second-Cartan-structure curvature has the OPPOSITE overall sign to the engine's Totaro convention (which is pinned to K=−1/2). Comparing them naively shows a spurious disagreement.
**Why it happens:** the engine's `hand_rolled_riemann_of_g` carries an explicit overall MINUS (lines 2299-2310) to match Totaro; the new spin-connection Riemann must be reconciled to the same.
**How to avoid:** first validate the new Riemann on the cone-Hessian benchmark; confirm a UNIFORM global sign factor (not a component bug); carry the matching overall sign so the cross-check is in the SAME convention.
**Warning signs:** uniform −1 ratio across all components.
**Recovery:** apply the global sign; re-compare.

## Level of Rigor

**Required for this phase:** controlled exact-over-Q symbolic computation with an independent cross-check (physicist's proof backed by certified computation).

**Justification:** the project's standard; every decisive verdict (det, signature, curvature, Einstein) must be exact over Q with no floating point, and the headline (R(ω)=Riemann of g) must be cross-checked by an independent computation (the contract's ≥5-component requirement).

**What this means concretely:**
- det(e^a_μ), all curvature components, signature: rationals from sympy over QQ, zero tolerance.
- R(ω)^ρ_{σμν} agrees with the independent Levi-Civita Riemann of g on ≥5 components EXACTLY (not "approximately").
- The Einstein/matter-sourcing verdict rests on a SINGLE global (κ,Λ) fit against an AST-guarded independent T[M], with M-power and tensor structure matched — never a per-point fit or a relabel.
- Sign conventions pinned to K=−1/2 BEFORE any verdict is read.
- Negative results (flat R[ω], non-Einstein G[g]) reported at true strength.

## State of the Art

| Old Approach (v17.0) | Current Approach (v18.0) | When Changed | Impact |
| --- | --- | --- | --- |
| cone-Hessian g_X=Hess(−log det), symmetric/real-QGT sector, (4,0) | soldering-form g=e·e, antisymmetric/Lie sector, (1,3) Riemann R[ω] | 2026-06-01/02 | a DIFFERENT tensor; v17.0 NONE does not bind |
| Berry curvature F_B=Im(QGT) tested as gravity | Berry = internal SU(4) gauge sector (NOT gravity); gravity = R[ω] | 2026-06-02 (Phase 76 overturn) | the gravity gate is the LINEAR-in-R EH object ε_abcd R^ab∧e^c∧e^d, not the quadratic F_B∧F_B |

**Superseded approaches to avoid:** the Maxwell-stress/Pontryagin F_B∧F_B discriminant (Phase 76 SOFT-KILL was OVERTURNED — "2-form stress traceless in 4d" is a tautology that also kills real GR). The cone-Hessian-is-the-metric framing (FALSIFIED in Phase 70.1). Λ<0 / R×H³ vacuum (FALSIFIED — the M=0 vacuum is flat).

## Open Questions

1. **How is the tetrad e^a_μ(x) constructed — factorize g(x), or carry e=π_u(dE) symbolically?**
   - What we know: g=e·e is locked; the M=0 e is the constant frame map J; the matter perturbation h(x;M) is built by the v17.0 matter-on-flat pipeline.
   - What's unclear: whether to (A) build e by an over-Q factorization of g(x) (non-unique up to SO(3,1), but R[ω] is frame-invariant), or (B) carry e=π_u(dE) as the literal V_{1/2}-valued soldering form differential, symbolically.
   - Impact: determines the B(a)/B(b) task structure.
   - Recommendation: **Try (B) first (e=π_u(dE) symbolic) — it ties the tetrad to the algebraic source and is the contract's intended construction; fall back to (A) factorization if (B)'s symbolic differentiation is intractable.** Either way, VERIFY g=e·e exactly. The planner should make this an explicit task decision with (A) as the documented fallback.

2. **Will R[ω]≠0 for M≠0 (the flatness sub-gate)?**
   - What we know: the M=0 vacuum is flat (g=η); matter sources the slice geometry (~94% in v17.0 via the cross-term).
   - What's unclear: whether the soldering form e(x) is rigid/integrable (R[ω]=0 even for M≠0, pure-gauge) or genuinely curved.
   - Impact: a hard STOP gate — if R[ω]=0 for M≠0, the route yields no gravity (honest trivial death).
   - Recommendation: make the flatness sub-gate the FIRST task (its own wave-1 gate plan OR the first task of 77-01); build g for ONE sample M≠0, compute R[ω], STOP if zero.

3. **Is the vacuum Einstein and is the matter-sourced Riemann Einstein-structured?**
   - What we know: the v17.0 Ph73 cone-Hessian G[g] was NOT Einstein (S≠0, Weyl≠0, κT~10³ off). This is the DIFFERENT tensor, so the answer is genuinely open.
   - What's unclear: whether R[ω] of g=e·e is Einstein at M=0 (expected flat/Λ=0) and matter-sourced-Einstein at M≠0.
   - Impact: the B(d) verdict; the milestone's headline.
   - Recommendation: MEASURE — report the vacuum level and the matter-sourcing at true strength. The contract's uncertainty markers flag "forced-coframe-but-imported-action partial" as the most-likely real outcome (B yes on curvature, but Einstein structure may need Phase C's action). Do NOT inflate.

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| --- | --- | --- | --- |
| e=π_u(dE) symbolic (Open Q1-B) | symbolic differentiation intractable / watchdog | factorize g(x) over Q (Open Q1-A) | low — R[ω] frame-invariant; just verify g=e·e |
| closed-form ω(e) [Approach 1] | unexpected non-integrability | reductive Spin(9,1)→Spin(3,1) projection [Approach 2] | medium — build 45-dim ambient, project to 6-dim Lorentz block |
| full nonlinear G[g] over (M,x) family | watchdog blowup on too many points | fewer points (≥5 components, ≥3 directions × ≥2 amplitudes); the v17.0 Ph73 used 12 | low — pattern exists |

**Decision criteria:** abandon the flatness sub-gate's "proceed" only if R[ω]=0 exactly over Q for a generic M≠0 sample (then STOP, trivial death). Switch tetrad construction route if symbolic ω(e) does not evaluate within the watchdog window after substitute-then-invert.

## Sources

### Primary (HIGH confidence)
- D.K. Wise, gr-qc/0611154 (CQG 27 (2010) 155010), "MacDowell-Mansouri gravity and Cartan geometry" — read p.3 directly from the locally-saved PDF: A=ω+(1/ℓ)e, F=(R−(Λ/3)e∧e)+d_ωe, ℓ²=3/Λ, S_MM, SO(4,1)/SO(3,2). VERBATIM.
- MacDowell & Mansouri, PRL 38 (1977) 739 — the original broken-gauge mechanism.
- Wikipedia "Spin connection" + HandWiki "Spin connection" (cross-confirmed) — the closed-form torsion-free ω_μ^{ab}(e,∂e) three-term formula; Cartan structure equations. VERBATIM, two independent sources agreeing.
- In-repo: CONVENTIONS.md §1/§6/§11 (locked conventions); derivations/75-coframe-reduction.tex (coframe SURVIVES); derivations/73-einstein-structure.tex (independent-T template); derivations/52-kkt-spacetime.tex (Minkowski map).
- In-repo code (verified by reading): bulk_geometry_verification.py (totaro_riemann L1397, hand_rolled_riemann_of_g L2236, spacetime_curvature_of_g L2153, _matterless_reference_hessian L2097, ricci_decomposition_n4 L2329, eig_signature_count L2369, h3_cone_hessian_benchmark L1512, _frame_jacobian_bg_to_mink L1213); cartan_phaseB_metric_precheck.py (G_DET2_RAW, frozen indices); ring_lemma_verification.py (det SSOT).

### Secondary (MEDIUM confidence)
- .gpd/research/SUMMARY.md, METHODS.md, PITFALLS.md (project-level v18.0 research, 2026-06-01) — the route structure, the hand-rolled-matrix-curvature recommendation, the fp-imported-action central risk.
- Sharpe 1997 (Cartan's Generalization of Klein's Erlangen Program) — soldering form g=e*η, reductive split (cited, not re-read this session).

### Tertiary (LOW confidence)
- None load-bearing.

## Caveats and Alternatives (pre-submission self-critique)

1. **Assumption that might be wrong:** that e=π_u(dE) can be carried symbolically and differentiated within the watchdog window. If E(x) is a complicated idempotent field, the symbolic differentiation of π_u(dE) could blow up. Mitigated by the factorize-g(x) fallback (Open Q1-A) and substitute-then-invert.
2. **Alternative dismissed quickly:** the reductive Spin(9,1)→Spin(3,1) projection (Approach 2). I dismissed it as PRIMARY because the contract warns against the raw 45-dim curvature and because closed-form ω(e) is cleaner and directly cross-checkable. It remains a valid (heavier) cross-check; a Spin(9,1) specialist might prefer it for tying ω to the algebraic source more directly.
3. **Understated limitation:** the "independent" Riemann cross-check (R(ω) vs Levi-Civita Riemann of g) tests that the spin-connection machinery is correct — but BOTH compute the Riemann of the SAME g=e·e, so they are independent METHODS, not independent PHYSICS. The genuine physics gate is B(d) (Einstein/matter-sourcing vs independent T[M]). The cross-check guards implementation, not the verdict.
4. **Simpler method overlooked?** One could skip the explicit A=ω⊕e assembly and just compute the Levi-Civita Riemann of g=e·e directly (via `hand_rolled_riemann_of_g`), since the torsion-free Lorentz block R[ω] IS the metric Riemann. The contract, however, explicitly requires the Cartan assembly F=dA+A∧A with the Lorentz/translation split and the R(ω) identification — so the spin-connection route is required, with the direct metric Riemann as the cross-check. (This is arguably the cleanest framing: the two are designed to agree.)
5. **Would a specialist disagree?** A Cartan-gravity specialist might note that for a torsion-free Levi-Civita ω, the translation block d_ωe vanishes trivially and the Lorentz block is just the metric Riemann minus (Λ/3)e∧e — so "computing F=dA+A∧A" is, modulo the cosmological term, equivalent to computing the metric Riemann. This is correct and is exactly why the cross-check must agree exactly; the milestone's content is whether that Riemann is Einstein-structured and matter-sourced (B(d)), not the assembly mechanics (B(c), which is bookkeeping).

## Metadata

**Confidence breakdown:**
- Mathematical framework: HIGH — Wise MM and closed-form spin-connection formulas read verbatim from primary sources; locked conventions read from CONVENTIONS.md.
- Standard approaches: HIGH — closed-form ω(e) is textbook; the in-repo Levi-Civita harness is validated.
- Computational tools: HIGH — all reuse functions read and confirmed in bulk_geometry_verification.py; watchdog-safe pattern documented.
- Validation strategies: HIGH — cross-check, K=−1/2 benchmark, signature, and the independent-T discipline all have in-repo precedent.
- The OUTCOME (R[ω]≠0? Einstein?): MEDIUM by design — that is what Phase B measures.

**Research date:** 2026-06-02
**Valid until:** stable (physics + conventions locked); re-check if CONVENTIONS §11 or the engine API changes.

## Recommended Plan Structure

Two plans, matching the roadmap sketch, with the flatness sub-gate as the explicit opening hard-STOP.

**Plan 77-01 — Coframe non-degeneracy + spin connection + FLATNESS SUB-GATE (wave 1):**
- **Task 1 (FLATNESS SUB-GATE, the hard STOP):** build g=e·e(x) for ONE sample M≠0 using the matter-on-flat pipeline; build ω(e) (closed-form formula 2) and R[ω] at one rational basepoint; assert R[ω]≠0 exact over Q. If R[ω]=0 → STOP (trivial death, honest negative). **RECOMMENDATION: make this the FIRST TASK of 77-01, not a separate plan** — it reuses 77-01's ω/R[ω] machinery on one sample, so a separate plan would duplicate setup; but it MUST gate everything downstream (a checkpoint/STOP after Task 1). [Rationale: the gate is cheap and shares all machinery with the rest of 77-01; a standalone wave-1 gate plan would force rebuilding e(x)/ω(e) twice. Keep it as 77-01 Task 1 with an explicit STOP checkpoint.]
- **Task 2 (B(a) coframe non-degeneracy):** lock the index layout (slice [1,2,3,10], survivors [11,18,19,26]); construct e^a_μ(x) [primary: e=π_u(dE) symbolic; fallback: factorize g(x)]; verify g=e·e exactly; assert det(e^a_μ)≠0 over Q at sample point(s).
- **Task 3 (B(b) spin connection):** implement the closed-form ω_μ^{ab}(e,∂e) (formula 2); verify torsion d_ωe=0 (formula 1, by construction); sign-pin against the cone-Hessian K=−1/2 benchmark.
- INTERACTIVE: no (computational, gated by the flatness STOP checkpoint).

**Plan 77-02 — F=dA+A∧A, Riemann cross-check, vacuum, matter-sourcing (wave 2, depends_on 77-01):**
- **Task 1 (B(c) assembly + curvature):** assemble A=ω⊕e (iso(3,1)/so(3,2)/so(4,1)); compute F=dA+A∧A as component-matrix curvature; extract Lorentz block R(ω)+Λe∧e and translation block d_ωe; convert R(ω)^{ab}_{μν}→R^ρ_{σμν} (formula 4).
- **Task 2 (B(c) cross-check, defeats fp-relabel-of-mechanics):** compute the independent Levi-Civita Riemann of g via `hand_rolled_riemann_of_g`/`totaro_riemann`; reconcile sign convention; assert R(ω)==metric-Riemann on ≥5 components exactly over Q.
- **Task 3 (B(d) vacuum):** M=0 → confirm flat (R[ω]=0, Λ=0 MEASURED, per corrected §6); pin signs with K=−1/2.
- **Task 4 (B(d) matter-sourcing, the genuine physics gate):** turn on M∈V_{1/2}; compute the matter-sourced Riemann; build the INDEPENDENT T[M] (replicate derivations/73 Eq.Tpsi, AST-guarded, M=t·M_0 power-counting); test G[g]=κT+Λg with a SINGLE global (κ,Λ), matched in magnitude + tensor structure + M-power; Ricci decomposition (S, Weyl) via `ricci_decomposition_n4`; report Einstein-vs-not at true strength.
- INTERACTIVE: yes (Task 4 emits the verdict checkpoint — SURVIVES/greenlight Phase C OR honest-NEGATIVE).
- Optional cross-check leg: Re(QGT)=cone-Hessian soft sanity (NOT load-bearing; fp-reuse-cone-hessian).
