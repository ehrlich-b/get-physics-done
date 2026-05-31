# Phase 72: B — Matter-Sourcing - Research

**Researched:** 2026-05-30
**Domain:** Computational differential geometry on the h_3(O) (Albert algebra) symmetric cone; exact-over-Q curvature of a dim-4 Lorentzian spacetime slice inherited from g_X = Hess(-log det); matter-sourcing via cubic-norm cross-terms.
**Confidence:** HIGH on method/mechanism/decomposition/isolation (engine measured end-to-end; standard GR decomposition); MEDIUM on the matter-sourcing OUTCOME (novel, undecided — this is the phase's open question); LOW on external literature for matter-sourcing (none found — expected).

## Summary

The computational method is LOCKED and the engine is built (`code/bulk_geometry_verification.py`, 2568 lines, ALL_PASS exit 0). This is NOT a method-selection phase; it is an *isolation* phase. Phase 71 established (VERIFIED, exact over Q) that the matterless V_0 geometry is ALREADY position-dependent: the Ricci scalar R = R(det_2) varies across distinct det_2 leaves with ZERO matter, and is pure-Lambda (Einstein, R(center) = -3) ONLY at the F_4-symmetric center I/3. So the Phase-72 task is delicate: matter is NOT the origin of homogeneity-breaking, and the dominant failure mode is **misattributing the matterless det_2-modulus variation (or the center pure-Lambda) to matter**.

The matter-sourcing question is well-posed and reduces to four exact-over-Q computations on the dim-4 h_2(C_u) sub-slice (engine indices {1,2,3,10} = (beta,gamma,p,q)): (DERV-02) Riemann/Ricci as an explicit function of M via the Totaro closed form; (VALD-04) the GR Ricci-decomposition (Ricci scalar R, traceless Ricci S_munu, Weyl C_munu in n=4) to separate the Einstein/pure-Lambda part from genuine M-structure; (CALC-03) the cross-term ON/OFF test, feeding the SAME M!=0 background through the full cubic norm and through a block-diagonal norm det(V_1)·det(V_0) that zeroes the V_0<->matter cross-terms; (CALC-04) the ||M|| / det_2 scaling law via a series in matter amplitude. Matter enters ONLY through the det cross-term `2*Re((x2*x1)*x3)` — the unique channel coupling V_0 (x1 slot) to V_{1/2} (x2,x3 slots) — so the cross-term off-switch is a clean, decisive control. The isolation protocol holds the V_0 background FIXED (a chosen det_2 leaf, including the center) and defines the matter-sourced curvature as the DIFFERENCE Delta R(M) = R(X_bg + M) - R(X_bg) at fixed V_0-background.

**Primary recommendation:** Extend the existing `_offcenter_subs(delta, ...)` engine API by populating the matter indices (V_1 alpha = {0}; V_{1/2} = {11..26}) in `delta`, keep ONLY the 4 slice coords {beta,gamma,p,q} symbolic, **substitute all matter to small rationals BEFORE any `Matrix.inv()`** (the symbolic-matter inverse is the measured >200s cliff), and run Totaro Riemann (~19s exact). Decide matter-sourcing by the conjunction: (i) cross-term OFF kills Delta R(M); (ii) Delta R(M) -> 0 as ||M|| -> 0; (iii) Delta R(M) carries traceless-Ricci / Weyl structure beyond a pure-Lambda shift — all AT FIXED V_0-background. Anything weaker (e.g. a pure-Lambda Delta R, or a Delta R that survives the off-switch) is the forbidden proxy fp-lambda-as-sourcing and must be reported as "position-dependent but NOT matter-sourced" (NEGATIVE-RESULT-IS-SUCCESS).

## User Constraints

No CONTEXT.md exists for this phase (no `/gpd:discuss-phase` was run). The binding context is the ROADMAP phase spec + the v17.0 project contract (`claim-matter-sourcing`) + the LOCKED v17.0 conventions (`.gpd/CONVENTIONS.md`, 18/18 set) + the VERIFIED Phase-71 findings (`.gpd/phases/71-a-homogeneity-kill-gate/71-VERIFICATION.md`). Treat all of these as locked decisions:

- **Method is LOCKED.** Totaro closed-form curvature on the certified `det_3` SSOT. Do NOT survey alternative formalisms or alternative curvature engines. (Engine = `code/bulk_geometry_verification.py`.)
- **det SSOT is LOCKED.** `det_3` with cross-term `2*Re((x2*x1)*x3)` (Phase-64.1-corrected, F_4-invariant via CH + 324/324). NEVER `code/octonion_algebra.py` (buggy `(x1 x2) x3` order, float-only, 0.67 associator gap).
- **Signature bridge construction (ii) is LOCKED.** g_munu(x) = eta_munu + h_munu(x); eta from h_2(C_u)'s det_2; g(center, M=0) = eta EXACTLY. Construction (i) (Wick via u=e7) is REJECTED.
- **EXACT over Q on all decisive verdicts.** Ranks via `sympy.Matrix.rank()`, never numpy float rank. fp-float-decisive is FORBIDDEN.
- **kappa, Lambda are GLOBAL constants fitted in Phase 73, NOT here.** Phase 72 only needs to SEPARATE the maximally-symmetric (pure-Lambda) piece from M-structure, and confirm Lambda < 0 at the center (Cartan). The numeric value of Lambda is out of scope.
- **Phase-71 reframing (VERIFIED) overrides the pre-71 contract/roadmap wording.** M=0 is NOT flat and NOT a single pure-Lambda constant — the matterless geometry already breaks homogeneity (R = R(det_2)); pure-Lambda holds ONLY at the center. The genuine basepoint modulus is **det_2** (the Stab_{V_0}=Spin(9,1) invariant), not rho_J (they coincide for single-direction perturbations). V_1 (index 0) is INERT to R; V_{1/2} (indices 11..26) is the active matter channel.
- **FORBIDDEN PROXIES (contract):** fp-lambda-as-sourcing (a pure-Lambda M=0 curvature — AND, per Phase 71, the matterless det_2-variation — is NOT matter-sourcing); fp-ensemble-gravity (NO observers-make-gravity / Jacobson thermodynamic argument); fp-float-decisive (cross-term on/off + curvature verdicts EXACT over Q).
- **Backtracking trigger (honest negative):** if M=0 curvature is pure-Lambda and turning on M adds nothing through the cross-terms (cross-term on/off makes no difference at fixed V_0-background), report "position-dependent but pure-Lambda / not matter-sourced" and do NOT proceed to Phase 73.

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| ----------------- | ---- | ------------------- | --------------- | ---------------------- |
| `~/scratch/get-physics-done/paper6-bulk-geometry-prompt.md` (ref-prompt) | authoritative milestone spec | Defines Phase B targets (a)(b)(c): M=0 flat/pure-Lambda; cross-term off-switch removes M-curvature; scale vs \|\|M\|\| and rho_J. The reporting discipline ("do not soften", "curved-but-not-Einstein is acceptable") is binding. | READ IN FULL before planning | plan, execution, verification |
| Faraut & Koranyi, *Analysis on Symmetric Cones* (1994) (ref-faraut-koranyi) | foundational reference | Cone metric g_X = Hess(-log det); inverse g^{pq} = P(X) (quadratic representation); the det=1 hypersurface = symmetric space E_{6(-26)}/F_4. The M=0 center Einstein-negative (Cartan) baseline rests on this. Single-state ring = Ch. II-IV. | CITE for g_X, g^{pq}=P(X), Cartan baseline | plan (mechanism), verification (g^{pq} cross-check) |
| McCrimmon, *A Taste of Jordan Algebras* (2004) (ref-mccrimmon) | reference | Peirce decomposition under E_11, cubic norm, quadratic representation P(X). Grounds the V_1/V_{1/2}/V_0 split and the cross-term coupling structure. | CITE for Peirce + cubic norm structure | plan (mechanism) |
| Totaro, arXiv:math/0401381, Cor 2.3 (ref-totaro) | method reference | The Hessian-curvature closed form R_ijkl = -(1/4) g^{pq}(C_jlp C_ikq - C_ilp C_jkq); rank-1 cone slices have constant sectional curvature -d^2/4. Pins the Riemann sign. | CITE for the curvature engine + sign | plan, execution (engine SSOT) |
| `code/bulk_geometry_verification.py` (warm engine, ALL_PASS) | prior artifact (EXTEND) | The decisive computation surface. `_offcenter_subs`/`cone_hessian_offcenter`/`offcenter_slice_metric`/`cubic_form_C`/`totaro_riemann`/`ricci_scalar`/`second_fundamental_form` are the API Phase 72 EXTENDS (add matter to `delta`; add a block-diagonal-det variant; add a Ricci-decomposition routine). Do NOT rebuild. | EXTEND in place; reuse `det_3` SSOT | execution, verification |
| `.gpd/phases/71-a-homogeneity-kill-gate/71-VERIFICATION.md` | prior artifact (VERIFIED) | Reframes the whole phase: matterless position-dependence is REAL; V_1 inert; V_{1/2} active; det_2 is the genuine modulus; concrete matterless R values to reproduce as a regression anchor. | READ; use values as fixed-V_0-background anchors | plan, execution, verification |
| `~/scratch/get-physics-done/rho_directional_derivatives.py` (ref-peirce-coupling) | reference (real-only) | The off-center / rho_J expansion STRUCTURE for CALC-04 (series in matter amplitude). CAUTION: real-only cross-term `2*d1*d2*d3` — use the expansion strategy ONLY, recompute the octonionic cross-term from the engine `det_3`. | REUSE expansion strategy; NOT its det | execution (CALC-04 scaling) |
| `~/scratch/get-physics-done/peirce_coupling.py` (ref-peirce-coupling) | reference (numpy/float) | Peirce decomposition under E_11 (numpy/float). Establishes that x1 (V_0) couples to E_11 ONLY through the cubic trilinear, never bilinear — exactly the cross-term mechanism. NOT on the decisive path (float). | READ for intuition; do NOT import on decisive path | plan (mechanism) |
| `~/repos/blog/research/qualia-fixed-point/h3o_tower.py` (ref-h3o-tower) | benchmark | Corrected cubic-norm benchmark (cross-term association). Provenance cross-check for `det_3` if needed. | OPTIONAL cross-check of det_3 | verification |

**Missing or weak anchors:**

- **No external literature anchor for the matter-sourcing CLAIM.** A focused literature pass (Totaro, Faraut-Koranyi, "Curvatures of metric Jordan algebras" arXiv:2309.02682) found precedent ONLY for the *matterless* side: every formally real Jordan algebra admits a Jordan-Einstein metric of negative scalar curvature (corroborates the M=0/center Cartan baseline). I found NO precedent for off-diagonal-Peirce / non-idempotent ("matter") content SOURCING or modulating the Hessian curvature on a symmetric cone. This is the novel contribution. Validation must therefore be internal (limiting cases, cross-term off-switch, ||M||->0, exact-over-Q reality), NOT literature-benchmarked. Confidence on the OUTCOME is MEDIUM, not HIGH.
- **STALE-REFERENCE CONFLICT to flag to the planner.** The project-level `.gpd/research/METHODS.md`, `PITFALLS.md`, and `COMPUTATIONAL.md` (written pre-Phase-64.1/70/71) repeatedly name `code/octonion_algebra.py` `det_3` as the SSOT and even instruct "Use `det_3` from the corrected `code/octonion_algebra.py`". This is SUPERSEDED: the v17.0 CONVENTIONS lock and the warm engine make `code/octonion_algebra.py` BANNED (buggy order, float, 0.67 gap) and the SSOT is `code/ring_lemma_verification.py det_3` == `code/bulk_geometry_verification.py det_3` (`2*Re((x2*x1)*x3)`). Where the project research and the convention lock disagree, **the convention lock + warm engine win.** Use the engine's `det_3`.
- **rho_J vs det_2 wording.** The contract/roadmap say "rho_J(X_bg)"; the Phase-71 verifier flagged det_2 (the Stab_{V_0}=Spin(9,1) invariant) as the strictly-correct modulus. They coincide for single-direction perturbations. Phase 72 should report the scaling law against det_2 and NOTE the coincidence; this sharpens, not changes, CALC-04.

## Conventions

| Choice | Convention | Alternatives | Source |
| ------ | ---------- | ------------ | ------ |
| Metric signature (slice) | mostly-minus (-,+,+,+) Lorentzian on h_2(C_u) via det_2 | (+,-,-,-) | CONVENTIONS.md §1 |
| Metric signature (bulk) | Riemannian, positive-definite; g_X = Hess(-log det) | — | Faraut-Koranyi |
| Potential | Phi = -log det (FIXED; do NOT mix with bare det) | — | CONVENTIONS.md §4 |
| det / cubic norm | Freudenthal `det_3`, cross-term `2*Re((x2*x1)*x3)`; SSOT = engine `det_3` | (x1 x2) x3 [BANNED, buggy] | CONVENTIONS.md §0,§3 |
| Riemann (lower idx) | R_ijkl = -(1/4) g^{pq}(C_jlp C_ikq - C_ilp C_jkq), C_ijk = Phi_{,ijk} | — | Totaro Cor 2.3 |
| Ricci tensor | Ric_jl = g^{ik} R_ijkl (contract 1st & 3rd slots) | — | engine §12 header |
| Ricci scalar | R = g^{jl} Ric_jl = g^{ik}g^{jl} R_ijkl | — | engine §12 header |
| Riemann SIGN | NEGATIVE & constant on H^3 / at center (R(center)=-3); cone-Hessian K_sect = -1/2 (round = -1, exact factor 2) | — | Phase 70/71 benchmark |
| Units | natural ħ=c=k_B=1; EXACT over Q on all verdicts | float [FORBIDDEN on verdicts] | CONVENTIONS.md §2 |
| Center | I/3 (F_4-symmetric, rho_J=0); det(I/3)=1/27 | — | CONVENTIONS.md §3 |
| Peirce (under E_11=diag(1,0,0)) | V_1(1)={0} alpha; V_0(10)={1..10}=h_2(O); V_{1/2}(16)={11..26}. Slice h_2(C_u)(4)={1,2,3,10}=(beta,gamma,p,q) | — | engine §11, CONVENTIONS.md §3 |
| Genuine basepoint modulus | **det_2** (Stab_{V_0}=Spin(9,1) invariant); rho_J coincides for single-direction perturbations | rho_J [contract wording] | Phase-71 verifier |

**CRITICAL: All equations below use these conventions.** In particular the Riemann sign is the Totaro/engine convention with R < 0 at the center; the slice is mostly-minus; det_3 uses the corrected cross-term. Converting any external GR formula (e.g. the Ricci decomposition below, taken in a +,+,+,+ Riemannian convention) requires only consistent index raising with THIS slice metric g_munu (the decomposition is signature-agnostic as an algebraic identity in the curvature tensor).

Convention loading: see agent-infrastructure.md Convention Loading Protocol. Run `gpd --raw convention check` to confirm 18/18.

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in This Phase |
| -------- | ---------------- | ------ | ------------------ |
| det_3(X) = abg - a\|x1\|^2 - b\|x2\|^2 - g\|x3\|^2 + 2 Re((x2 x1) x3) | Freudenthal cubic norm | engine `det_3` (l.351) | The ONLY object; matter enters via the cross-term |
| Phi = -log det_3(X_bg + x) | cone potential | Faraut-Koranyi | Hessian metric source |
| g_ij = Phi_{,ij}; g^{pq} = P(X) | cone metric + inverse | Faraut-Koranyi | metric & raised indices |
| C_ijk = Phi_{,ijk} (totally symmetric) | cubic-form tensor | engine `cubic_form_C` (l.1319) | Totaro Riemann datum |
| R_ijkl = -(1/4) g^{pq}(C_jlp C_ikq - C_ilp C_jkq) | Totaro Riemann | engine `totaro_riemann` (l.1334); Totaro Cor 2.3 | DERV-02 Riemann |
| Ric_jl = g^{ik} R_ijkl; R = g^{jl} Ric_jl | Ricci tensor & scalar | engine `ricci_scalar` (l.1376) | DERV-02 / VALD-04 |
| **Matter cross-term** = 2 Re((x2 x1) x3), x1 in V_0, x2,x3 in V_{1/2} | V_0<->matter coupling | engine `det_3` | the SOLE channel for M; the off-switch target |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --------- | ------------ | ------------- | ------------------ |
| Totaro closed-form Hessian curvature (3rd derivs only) | Riemann from C_ijk + one inverse; det cubic => C_ijkl never needed | DERV-02 (R_ijkl) | Totaro arXiv:math/0401381 |
| GR Ricci decomposition (scalar + traceless-Ricci + Weyl), n=4 | Separates pure-Lambda from M-structure | VALD-04 | Wikipedia Ricci decomposition; Besse, *Einstein Manifolds* |
| Polarization of the cubic norm `polarize_d`, d(X,X,X)=6 det_3 | Directional derivatives = polarizations; organizes the M-expansion | CALC-04 | engine `polarize_d` (l.403) |
| Block-diagonal norm construction (zero the cross-term) | Decouples V_0 from matter in det | CALC-03 off-switch | this phase (novel control) |
| Series in matter amplitude t (substitute M = t·M0, expand to low order) | Scaling law Delta R(t) ~ t^k; avoids symbolic-matter inverse | CALC-04 | rho_directional_derivatives.py (strategy only) |
| Fixed-V_0-background difference Delta R(M) = R(X_bg+M) - R(X_bg) | Isolates the M-dependent part from matterless det_2-variation | ISOLATION (all of B) | this phase (Phase-71-mandated) |

### Approximation Schemes

| Approximation | Small Parameter | Regime of Validity | Error Estimate | Alternatives if Invalid |
| ------------- | --------------- | ------------------ | -------------- | ----------------------- |
| Series in matter amplitude t (M = t·M0) | t = \|\|M\|\| | small-matter neighborhood of the fixed V_0-background | EXACT per order (det cubic => finite jet in t; truncation error is the dropped higher orders, themselves exact rationals) | Carry M rational and compute Delta R exactly at several finite M (no truncation) |
| Linear-in-M (leading order of Delta R) | t | leading scaling law | drops O(t^2) | full exact Delta R at finite rational M |

**Note (det cubic => no resummation).** -log det has a finite-order rational Taylor jet around any interior point in the *matter* directions; the expansion TERMINATES. The smallness is \|\|M\|\| and det_2-off-center-ness, NEVER the spacetime coordinate x (which is O(1) and is the wrong expansion variable — Phase-71 lesson).

## Standard Approaches

### Approach 1: Fixed-V_0-background difference + cross-term off-switch (RECOMMENDED, LOCKED)

**What:** Extend the warm engine. Add matter to the off-center `delta` (V_1 alpha={0}, V_{1/2}={11..26}); keep slice coords {beta,gamma,p,q} symbolic; substitute matter to rationals BEFORE inverting; run Totaro Riemann; decompose; compare full-det vs block-diagonal-det at the SAME M; hold V_0-background fixed.

**Why standard:** It is the engine's measured-working path (~19s exact with matter rational, dim-4). It is the only path consistent with the locked conventions and the Phase-71 reframing. The four sub-questions map 1:1 onto contract requirements DERV-02/VALD-04/CALC-03/CALC-04.

**Track record:** The matterless version (Phase 71) ran exactly over Q, ALL_PASS exit 0; matter-on was spot-checked in Phase 71 (V_1 inert, V_{1/2} changes R additively). The block-diagonal-det variant is new but is a one-line change to `det_3` (drop the cross-term).

**Key steps (executable recipe):**

1. **Mechanism + index audit (cheap, do first).** Confirm the Peirce index map (V_1={0}, V_{1/2}={11..26}, V_0={1..10}, slice={1,2,3,10}) and that the cross-term `2*Re((x2*x1)*x3)` is the ONLY det term mixing x1 (V_0) with x2,x3 (V_{1/2}). Re-derive the (V_{1/2},V_{1/2},V_0) polarization block from `polarize_d` on the Peirce basis and confirm it is nonzero on genuinely octonionic M (e_4..e_7 components). [DERV-02 prereq; PITFALLS Pitfall 2.5/2.8]

2. **DERV-02: Riemann/Ricci as explicit function of M.** Build `delta_M` = chosen V_{1/2} (and V_1) matter, slice symbolic. `H_bg = cone_hessian_offcenter(delta_M, slice_symbolic=True)`; **substitute matter to rationals is already done inside delta** (delta values are rational). Then `ginv = H_bg.inv()` (4x4, ~3s with matter rational), `C = cubic_form_C(-log det restricted to slice coords)`, `R = totaro_riemann(ginv, C, 4)`, `Ric`, `Rscalar = ricci_scalar(R, ginv, 4)`. Assert `riemann_symmetry_ok`. ~19s total.

3. **VALD-04: Lambda-vs-matter separation.** At the FIXED V_0-background, compute (a) the M=0 baseline at the center (must be Einstein, R_munu ∝ g_munu, R(center)=-3 < 0 = Cartan/pure-Lambda); (b) for M!=0, the traceless Ricci S_munu = R_munu - (R/4) g_munu and the Weyl C_munu (n=4 formulas below). Genuine M-sourcing requires S_munu != 0 and/or Weyl != 0 tracking M — beyond a pure-Lambda shift R_munu ∝ g_munu.

4. **CALC-03: cross-term ON/OFF.** Define `det_block(X) = det_V0(X) * det_V1(X)` (the block-diagonal norm; see construction below). Recompute Delta R with `Phi_off = -log det_block` at the SAME M!=0. Decisive: Delta R(M)_full != 0 but Delta R(M)_off = 0 (or decisively smaller) => M-curvature is cross-term-sourced. Place M so ALL THREE off-diagonal octonion slots (x1,x2,x3) are populated (else triple product vacuous).

5. **CALC-04: scaling law.** Series Delta R(t) with M = t·M0 (one V_{1/2} direction with octonionic content). Confirm Delta R ∝ \|\|M\|\| (or higher power) and Delta R -> 0 as t -> 0. Report scale vs det_2 (the genuine modulus) at fixed-direction; NOTE rho_J coincidence.

**Known difficulties at each step:**

- Step 2: carrying matter AND slice coords ALL symbolic through `.inv()` => >200s timeout. **Matter must be rational before inv().** (Measured cliff, COMPUTATIONAL.md.)
- Step 4: single-slot matter makes `2*Re((x2 x1) x3) = 0` identically => off-switch test is HOLLOW. Populate all three slots.
- Step 3: the M=0 baseline is pure-Lambda ONLY at the center; at a generic off-center V_0-background it is already non-Einstein (Phase-71). So the Lambda-vs-matter separation must be done as Delta from the SAME fixed V_0-background, not against a global "flat" reference.
- Octonion non-associativity: every Hessian/curvature must be built from the corrected `det_3`; a wrong cross-term silently corrupts everything (PITFALLS Pitfall 2).

### Approach 2: Direct sympy.diffgeom Riemann on the 4-dim slice (FALLBACK / cross-check only)

**What:** Compute a few Riemann components of the dim-4 slice metric directly via hand-rolled Christoffel/Riemann (not the Totaro shortcut), as an INDEPENDENT cross-check of `totaro_riemann`.

**When to switch:** Only to cross-validate a handful of components (the engine already prefers the hand-rolled Christoffel/Riemann path; `sympy.diffgeom` itself blows up). NEVER as the primary on >4 dims.

**Tradeoffs:** Slower, but independent of the Totaro closed-form assumption (a useful guard against an engine bug in `totaro_riemann`). The h3_constant_curvature() H^3 benchmark already exercises this hand-rolled path.

### Anti-Patterns to Avoid

- **Attributing the matterless det_2-variation to matter.** Per Phase 71 the pure geometry already breaks homogeneity. The matter-sourced part is the DIFFERENCE at FIXED V_0-background, not the raw R(X_bg+M). _Example:_ comparing R at two basepoints that differ in BOTH M and det_2 — the det_2 change alone moves R (matterlessly), faking "matter-sourcing." This is fp-lambda-as-sourcing in disguise.
- **Single-slot matter for the cross-term test.** `2*Re((x2 x1) x3) = 0` if any slot is empty => the off-switch changes nothing => hollow test (a vacuous "pass" or "fail"). _Example:_ M with only an x2-component and x3=0 gives identically-zero cross-term; the ON/OFF comparison is then trivially equal and proves nothing.
- **Carrying matter symbolic through the inverse.** >200s timeout; will trip the ~150s executor stream-watchdog. Substitute matter to rationals first.
- **Reading a pure-Lambda Delta R as matter-sourcing.** If Delta R(M) is ∝ g_munu with constant coefficient (Einstein), it is a Lambda shift, not matter structure. Decompose into traceless-Ricci + Weyl and check the off-switch.
- **Using `octonion_algebra.py` det_3 (or the real-only rho-module cross-term) for octonionic M.** Buggy/association-blind => silently wrong coupling. Use the engine `det_3`.

## Existing Results to Leverage

### Established Results (DO NOT RE-DERIVE — cite and use)

| Result | Exact Form | Source | How to Use |
| ------ | ---------- | ------ | ---------- |
| Cone metric = Hessian of -log det | g_X = Hess(-log det), g^{pq} = P(X) | Faraut-Koranyi (ref) | The metric; cite, do not re-derive |
| det=1 hypersurface = E_{6(-26)}/F_4 symmetric space; Cartan => Einstein NEGATIVE | irreducible Riemannian symmetric space, Ricci ∝ g, negative const | Faraut-Koranyi; Cartan; arXiv:2309.02682 (Jordan-Einstein, neg. scalar curv.) | The M=0 center baseline (pure-Lambda, Lambda<0); cite as the limiting case |
| Totaro closed-form Riemann (cubic => f_ijkl=0) | R_ijkl = -(1/4) g^{pq}(C_jlp C_ikq - C_ilp C_jkq) | Totaro Cor 2.3 (ref) | The curvature engine; already coded |
| Corrected cubic-norm cross-term | `2*Re((x2*x1)*x3)`, F_4-invariant (CH + 324/324) | Phase 64.1; engine `det_3` | The SSOT; never re-derive the association |
| Ricci decomposition (n general) | see formulas below | Wikipedia / Besse | Lambda-vs-matter separation; standard, do not re-derive |
| **Phase-71 matterless R values (regression anchors)** | R(center)=-3; R{4:1/5,5:1/7}=-521269105/154700283; R{4:1/3}=-73041507/21967969; R(X)=R(2X) (scale-inv); V_1 inert; one V_{1/2} dR=100305755136000/168193119407041 | 71-VERIFICATION.md | Fixed-V_0-background anchors; reproduce exactly before adding matter |

**Key insight (why re-derivation is wasteful AND dangerous):** the cone metric, the symmetric-space/Cartan baseline, the Totaro formula, and the corrected cross-term are all SOLID standard/certified results — re-deriving them risks re-introducing the very cross-term association bug the project paid to fix in Phase 64.1. The ONLY genuinely novel object is the *matter-sourced* Delta R(M) and its cross-term origin; spend the budget there.

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
| ------ | ----------------- | ------ | ---------- |
| cone_hessian_at_center restricted to slice = diag(9,9,18,18), det 26244 | the M=0, center metric (nondegenerate) | engine `cone_hessian_at_center` (l.976); Phase 70 | center, M=0 |
| Hess(-log det) at diagonal state: off-diag blocks 4·det - 2·w_i·(sig2-1/3) | closed-form 2nd-deriv structure at diagonal backgrounds | rho_directional_derivatives.py PART 13 | diagonal background (incl. I/3); a free analytic check on the symbolic Hessian |
| x1 (V_0) couples to E_11 ONLY through the cubic trilinear, never bilinear | the cross-term IS the only matter channel | peirce_coupling.py (read, not import) | structural fact |
| H^3 cone-Hessian sectional curvature = -1/2 (round = -1, exact factor 2) | Riemann sign benchmark | engine `h3_constant_curvature`/§12; Phase 70/71 | det_2=1 hyperboloid, M=0 |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| ------------ | ------- | ---- | --------- | --------------- |
| The curvature of a Hessian metric (arXiv:math/0401381) | Totaro | 2004 | The exact curvature engine + the -d^2/4 rank-1 slice value | R_ijkl closed form; Cor 2.3; the constant-curvature slice fact |
| Analysis on Symmetric Cones | Faraut & Koranyi | 1994 | g_X=Hess(-log det), g^{pq}=P(X), E_{6(-26)}/F_4 structure | the metric + the Cartan/Einstein baseline |
| Curvatures of metric Jordan algebras (arXiv:2309.02682) | (recent) | 2023 | Confirms every formally real Jordan algebra admits a Jordan-Einstein metric of NEGATIVE scalar curvature | Corroborates the M=0/center Cartan baseline (Lambda<0). NOTE: matterless side only — no matter-sourcing precedent |
| Ricci decomposition / Einstein four-manifolds (Wikipedia; arXiv:1612.00627, 1903.11817) | various | — | Standard n=4 scalar/traceless-Ricci/Weyl decomposition | the exact formulas in VALD-04 |

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
| ---- | -------------- | ------- | ------------ |
| SymPy | 1.14.0 (installed) | exact symbolic algebra over Q: octonion/Jordan arithmetic, det_3, diff, Matrix.inv, Matrix.rank | the project's exact-over-Q engine; FORBIDDEN to use numpy float rank on verdicts |
| `code/bulk_geometry_verification.py` | warm engine (EXTEND) | det_3 SSOT + Totaro curvature + offcenter API + II | the decisive surface; ALL_PASS exit 0 |
| Python 3 (`python3 -u`, foreground) | — | run heavy symbolic with unbuffered progress prints | defeats the ~150s executor stream-watchdog (print between heavy steps) |

### Supporting Tools

| Tool | Purpose | When to Use |
| ---- | ------- | ----------- |
| mpmath | guarded float fallback / triage | ONLY non-decisive triage (e.g. which M to do exactly); NEVER a verdict |
| `rho_directional_derivatives.py` (strategy) | the off-center / amplitude expansion structure | CALC-04 series-in-t; reuse strategy, recompute octonionic cross-term from engine |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
| ---------- | --------- | -------- |
| Totaro closed-form (hand-rolled Christoffel/Riemann) | `sympy.diffgeom` Riemann from metric | diffgeom blows up even at dim-4 with matter; use Totaro. diffgeom-free hand-roll only as a few-component cross-check |
| Faraut-Koranyi g^{pq} = P(X) closed form | numerically invert finite-difference Hessian | float spot-check only; decisive g^{pq} must be exact (Matrix.inv of the rational 4x4) |
| Exact Delta R at finite rational M | series in amplitude t | series is cheaper for the SCALING LAW; finite-M exact is the decisive on/off verdict |

### Computational Feasibility (MEASURED — COMPUTATIONAL.md)

| Computation | Estimated Cost | Bottleneck | Mitigation |
| ----------- | -------------- | ---------- | ---------- |
| Hess(-log det_3) build, dim-4 slice | ~35 ms | — | — |
| Evaluate at center / rational point | fast | — | — |
| `Matrix.inv()` dim-4, MATTER RATIONAL + 4 slice coords symbolic | ~3 s | expression swell | keep matter rational (this is the working regime) |
| `Matrix.inv()` dim-4, matter+coords ALL symbolic (6+ symbols) | **TIMEOUT >200 s** | symbolic inverse cliff | substitute matter to rationals FIRST |
| `Matrix.inv()` dim-10 V_0 symbolic | **TIMEOUT >200 s** | dim-10 off critical path | stay on dim-4 h_2(C_u); dim-10 is mpmath-only triage |
| Full Christoffel + Riemann, dim-4, matter rational | **~19 s total** exact over Q | per-entry simplify | `cancel` per entry, not `simplify` in hot loop; print progress between steps (watchdog) |
| Cross-term ON vs OFF (two runs of the above) | ~40 s total | as above | — |
| Series Delta R(t) to low order | cheap (finite jet) | — | — |

**Installation / Setup:** SymPy 1.14.0 is already installed; no new packages required.
```bash
# nothing to install; if a fresh venv is ever needed:
pip install sympy==1.14.0
```

**Watchdog discipline (MEMORY [[feedback_executor_watchdog_stall_long_symbolic]]):** the gpd-executor stream-watchdog can kill long no-output symbolic runs (~150s harness, 600s hard). Run heavy steps FOREGROUND with `python -u` and print progress between heavy steps (after Hessian build, after inverse, after Riemann, after each decomposition). Background-resume stalls were observed; if a stall happens the orchestrator can commit + write SUMMARY from partial output.

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| ----- | ----------------- | -------------- | --------------- |
| Riemann algebraic symmetries | engine correctness | `riemann_symmetry_ok(R, 4)` | True (antisym i,j; antisym k,l; pair-swap) |
| Engine regression (SSOT) | det_3 + curvature unbroken | `python3 code/bulk_geometry_verification.py` | OVERALL: ALL_PASS, exit 0 |
| g(center, M=0) = eta exactly | construction (ii) clean (no fake Lambda) | `minimal_reduction` residual = 0; H_center restricted = diag(9,9,18,18), det 26244 | exact 4x4 zero; diag matches |
| Phase-71 matterless R reproduced | fixed-V_0-background anchors | recompute R at center (-3) and the 71 basepoints | exact match over Q |
| Cross-term off-switch reduces det to block-diagonal | the off-switch is implemented right | `det_block` = det with `2*Re((x2x1)x3)` term removed; check `det_block` factorizes as det_V0·det_V1 on a test point | exact factorization |
| All three octonion slots populated for cross-term test | non-vacuous triple product | evaluate `2*Re((x2 x1) x3)` at the chosen M | NONZERO (else hollow) |
| Reality + exactness | no Wick/float artifact | R, Ric, Delta R all real rationals over Q | real, exact |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| ----- | ---------------- | ------------ | ------ |
| M -> 0 at the center | ||M||->0, X_bg=I/3 | R -> -3 (Einstein, pure-Lambda, Lambda<0 Cartan); Delta R -> 0 | Phase 70/71; Faraut-Koranyi |
| M -> 0 at fixed off-center V_0-background | ||M||->0, det_2 fixed | R -> the matterless R(det_2) (Phase-71 value); Delta R -> 0 | 71-VERIFICATION.md |
| Cross-terms OFF + M!=0 | block-diagonal det | M-sourced Delta R must VANISH (or change decisively) | ref-prompt Phase B(b); contract test-cross-term-onoff |
| H^3 sub-slice, M=0, det_2=1 | rank-1 complex line | constant sectional curvature -1/2 (cone-Hessian) / -1 (round) | Totaro -d^2/4; engine §12 |
| V_1 (alpha) matter alone | M in V_1 only | R UNCHANGED (V_1 inert) — must be checked/explained | Phase-71 Check A(ii) |

### Numerical Validation

| Test | Method | Tolerance | Reference Value |
| ---- | ------ | --------- | --------------- |
| Delta R(M) reality | exact rational | exact (no tolerance) | imaginary part identically 0 |
| Scaling Delta R(t), M=t·M0 | series in t | exact per order | leading power k>=1; coeff exact rational |
| g^{pq} vs Faraut-Koranyi P(X) | float spot-check of the symbolic inverse | ~1e-10 (triage only) | agreement (decisive g^{pq} is the exact Matrix.inv) |

### Red Flags During Computation

- Delta R(M) has a nonzero imaginary part => a unitarity/reality-violating error (wrong cross-term association or a Wick contamination). Reality must hold exactly over Q.
- `2*Re((x2 x1) x3)` evaluates to 0 at the chosen M => the cross-term test is HOLLOW (single-slot or accidentally-associative M); repopulate all three slots with e_4..e_7 content.
- The cross-term off-switch leaves Delta R UNCHANGED => the curvature is NOT matter-sourced (it is intrinsic/Lambda-like) => honest negative (fp-lambda-as-sourcing avoided).
- `Matrix.inv()` hangs (>60s) => matter is still symbolic; substitute to rationals.
- Delta R(M) is ∝ g_munu with constant coefficient => pure-Lambda shift, NOT matter structure; decompose to confirm S_munu=0, Weyl=0.
- R differs across basepoints that ALSO differ in det_2 => you are seeing the matterless modulus, not matter (fix the V_0-background).

## Common Pitfalls

### Pitfall 1: Lambda (or the matterless det_2-variation) mistaken for matter-sourcing [fp-lambda-as-sourcing]

**What goes wrong:** A nonzero (or position-dependent) Riemann tensor is read as "matter sources curvature," but it is either (a) a maximally-symmetric Lambda piece (R_munu ∝ g_munu, constant R) or (b) per Phase 71, the matterless det_2-modulus variation that exists at M=0.
**Why it happens:** Comparing raw R at backgrounds that differ in det_2 and/or not subtracting the M=0 baseline; conflating "curved" with "matter-sourced."
**How to avoid:** Always work with Delta R(M) = R(X_bg+M) - R(X_bg) at a FIXED V_0-background (fixed det_2 leaf). Decompose into scalar (Lambda) + traceless-Ricci + Weyl. Run the cross-term off-switch. Require Delta R -> 0 as ||M|| -> 0.
**Warning signs:** Delta R ∝ g_munu with constant coefficient; or R varies but det_2 also varied; or Delta R survives the off-switch.
**Recovery:** Re-fix the V_0-background; recompute Delta R; if it is pure-Lambda or off-switch-invariant, report "position-dependent but NOT matter-sourced" (NEGATIVE-RESULT-IS-SUCCESS) and do NOT proceed to Phase 73.

### Pitfall 2: Octonion non-associativity in the cross-term silently corrupts everything [Phase B critical]

**What goes wrong:** Using the wrong cross-term association ((x1 x2) x3, or x1(x2 x3), or the real-only `2 d1 d2 d3`) returns a plausible number, but every Hessian/curvature/coupling built on it is wrong — and the error is amplified by differentiation, not averaged out.
**Why it happens:** Three mutually inconsistent det conventions exist in-repo (measured 0.67 associator gap); stale project-research files even point at the banned `octonion_algebra.py`.
**How to avoid:** Use the engine `det_3` (`2*Re((x2*x1)*x3)`) for ALL geometry. Pre-flight on genuinely non-associative M (e_4..e_7 nonzero): confirm `Re((x2 x1) x3) != Re(x1 (x2 x3))` (nonzero gap) and Cayley-Hamilton holds. Re-derive the (V_{1/2},V_{1/2},V_0) polarization block and confirm it matches.
**Warning signs:** det_3 disagrees with the matrix/Sarrus convention on octonionic data; a "verified" cross-term done only on diagonal/quaternionic (e_0..e_3) inputs (vacuous, associative).
**Recovery:** Recompute det_3 with the corrected association; redo ALL Hessians/curvatures downstream (nothing built on the wrong norm survives).

### Pitfall 3: Hollow cross-term test (vacuous triple product) [CALC-03]

**What goes wrong:** With matter in fewer than all three off-diagonal slots, `2*Re((x2 x1) x3) = 0` identically, so the full-det and block-diagonal-det give the SAME curvature — the ON/OFF test is trivially equal and proves nothing (a false "not sourced" OR a false "sourced", depending on framing).
**Why it happens:** Putting M only in V_{1/2} (x2 or x3) without an x1 (V_0) partner, or only one of x2/x3.
**How to avoid:** Populate x1 (a V_0 slice/internal direction), x2 AND x3 (V_{1/2}) so the triple product is genuinely nonzero. Verify `2*Re((x2 x1) x3) != 0` at the chosen M before running curvature.
**Warning signs:** cross-term evaluates to 0; ON and OFF curvatures identical for trivial reasons.
**Recovery:** Repopulate all three slots with octonionic (e_4..e_7) content; re-run.

### Pitfall 4: Symbolic-matter inverse cliff / watchdog stall [performance]

**What goes wrong:** Carrying matter parameters AND the 4 slice coords as free symbols through `Matrix.inv()` blows up (>200s), tripping the ~150s executor stream-watchdog; the run is killed with no verdict.
**Why it happens:** Expression swell in the symbolic inverse (the dominant cost).
**How to avoid:** Substitute matter to small RATIONALS before inverting; keep ONLY the 4 slice coords symbolic (~3s inverse, ~19s full curvature). For the scaling law, series-expand in a single amplitude t to low order rather than carrying M symbolic. Run foreground `python -u` with progress prints between heavy steps.
**Warning signs:** `.inv()` runs >60s; harness goes quiet.
**Recovery:** Kill, substitute matter to rationals, re-run; if a stall already happened, orchestrator commits + writes SUMMARY from partial output.

### Pitfall 5: Mistaking extrinsic (embedding) curvature for intrinsic gravity [conceptual]

**What goes wrong:** The h_2(C_u) slice is NOT totally geodesic off-center (Phase-71: II != 0). Extrinsic-curvature (II) terms then contribute to R^slice via the Gauss equation; reporting those embedding terms as "matter-sourced gravity" conflates how the slice bends INSIDE h_3(O) with intrinsic spacetime curvature.
**Why it happens:** The Gauss equation R^slice = R^ambient|_slice + (II·II - II·II); II != 0 already at M=0.
**How to avoid:** The DECISIVE quantity is the INTRINSIC curvature of the dim-4 slice metric g_munu(x) (the Totaro R of the induced/inherited metric), and the matter claim is about its M-DEPENDENT part (Delta R(M)) sourced by the cross-terms — not merely that the embedding bends. Keep the comparison intrinsic and M-differenced at fixed background.
**Warning signs:** "position-dependent curvature" that persists at M=0 attributed to matter; II-driven terms quoted as the source.
**Recovery:** Re-express the claim as Delta R(M) intrinsic, cross-term-sourced; the matterless II/position-dependence is the Phase-71 result, not Phase-72's.

## Level of Rigor

**Required for this phase:** EXACT computation over Q (a computer-algebra proof of the specific tensor identities at the chosen backgrounds), at the level of "controlled exact numerical evidence on a decisive sub-slice." NOT a general theorem for all M (that is beyond scope); a decisive exact-over-Q verdict on representative M with the cross-term off-switch and the ||M||->0 limit.

**Justification:** The contract's acceptance tests (test-cross-term-onoff = consistency, test-lambda-vs-matter = limiting_case) and FORBIDDEN PROXIES (fp-float-decisive) demand exactness, not floating-point. The matter-sourcing claim is novel (no literature benchmark), so the rigor must come from internal exact-over-Q checks: the off-switch must EXACTLY kill Delta R, ||M||->0 must EXACTLY recover the matterless geometry, and reality must hold EXACTLY.

**What this means concretely:**
- All curvature verdicts (Delta R, S_munu, Weyl, on/off comparison) computed with `sympy.Rational`, exact over Q. No float on any verdict.
- Ranks/zeros via `sympy.Matrix.rank()` / exact comparison, never numpy.
- The scaling law may be a low-order series in amplitude t, but each coefficient is an exact rational.
- A representative-M result with the off-switch + ||M||->0 limit is sufficient for the SURVIVES/negative verdict; an all-M general proof is NOT required (and is out of scope — Phase C / future).
- Reproduce the Phase-71 matterless anchors exactly before adding matter (regression).

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| ------------ | ---------------- | ------------ | ------ |
| Lattice/Fisher metric (paper6-continuum-limit) | Intrinsic cubic-norm cone-Hessian curvature | v17.0 | No lattice; matter enters via det cross-terms, not a lattice coupling |
| Posited GST/N=2 supergravity Lagrangian with det as prepotential (derivations 47-50,53) | Intrinsic Totaro curvature of g_X=Hess(-log det) | v17.0 | No SUSY, no posited action — circular route abandoned |
| `octonion_algebra.py` det_3 ((x1 x2) x3, float) | `det_3` (`2*Re((x2*x1)*x3)`, exact, F_4-invariant) | Phase 64.1 | The SSOT; stale project-research references to octonion_algebra are SUPERSEDED |
| Construction (i) Wick-rotate via u=e7 | Construction (ii) eta + cone-Hessian perturbation | Phase 70 | Wick rejected (manufactures spurious curvature; unproven C*-bottleneck) |
| rho_J as the basepoint modulus | det_2 (Stab_{V_0}=Spin(9,1) invariant) | Phase 71 | det_2 is the genuine modulus; coincides with rho_J for single-direction perturbations |

**Superseded approaches to avoid:**
- `octonion_algebra.py` det_3: buggy association; the project-research METHODS/PITFALLS/COMPUTATIONAL that point at it are PRE-Phase-64.1 and SUPERSEDED — use the engine `det_3`.
- Jacobson 1995 thermodynamic / observers-make-gravity ensemble: explicitly REJECTED (fp-ensemble-gravity). The curvature must come from the algebra's own cubic-norm geometry, one observer, one off-center point.

## Open Questions

1. **Is V_1 (alpha) inert to curvature only through V_1-self-coupling, or does it source via V_1<->V_{1/2} cross-terms?**
   - What we know: Phase-71 found adding V_1 alone leaves R UNCHANGED; V_{1/2} changes R additively. The det cross-term `2*Re((x2 x1) x3)` involves x1 (V_0), x2,x3 (V_{1/2}) — alpha (V_1, the (0,0) entry) does NOT appear in the octonion cross-term at all (it multiplies |x1|^2 etc. as a diagonal coefficient).
   - What's unclear: whether V_1 can source Delta R indirectly (through its effect on the metric normalization / via mixed V_1-V_{1/2} terms) or is genuinely decoupled from the slice curvature.
   - Impact: determines whether "matter" effectively means V_{1/2} only. Likely the decisive matter channel is V_{1/2}.
   - Recommendation: compute Delta R for (a) V_{1/2} only, (b) V_1 only, (c) V_1+V_{1/2}, at fixed V_0-background; explain the V_1-inertness structurally from the det cross-term (alpha absent from the triple product).

2. **Does the cross-term off-switch cleanly factorize det into det(V_0)·det(V_1), or is there a V_{1/2}-self block to handle?**
   - What we know: the only V_0<->matter mixing term is the octonion triple `2*Re((x2 x1) x3)`. Zeroing it leaves abg - a|x1|^2 - b|x2|^2 - g|x3|^2.
   - What's unclear: the precise block structure of the "block-diagonal" norm — the |x2|^2, |x3|^2 terms (V_{1/2} self-norms) couple to the diagonal a,b,g; the prompt's "det(V_1)·det(V_0)" is schematic.
   - Impact: the exact form of det_block determines what "cross-terms off" means precisely.
   - Recommendation: define det_block operationally as "det_3 with the `2*Re((x2 x1) x3)` term set to 0" (the unique V_0<->V_{1/2} mixing channel), and verify it reduces to det(V_0) when matter (x2,x3,alpha) = 0. Document this as the operational definition; note the prompt's product wording is schematic.

3. **What is the leading power of Delta R(M) in ||M||?**
   - What we know: curvature ~ C·C structure (Totaro), C from 3rd derivatives; the cross-term is quadratic-ish in matter (x2,x3 bilinear with x1).
   - What's unclear: whether the leading Delta R is O(||M||), O(||M||^2), or higher — METHODS Method 4 suggests O(||M||^2) from F_ijk F_ijk, but the cross-term structure may give a linear leading term.
   - Impact: the scaling law (CALC-04) and the linear-vs-exact Einstein test (Phase C).
   - Recommendation: compute the series Delta R(t), M=t·M0, and read the leading power empirically (exact per order); do NOT assume O(||M||^2).

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| ------------- | ---------- | --------- | ----------------- |
| Totaro `totaro_riemann` (suspected engine bug) | wrong sign / symmetry fail | hand-rolled Christoffel/Riemann cross-check (a few components) on the dim-4 slice | low — engine has the hand-rolled path (h3_constant_curvature) |
| Symbolic dim-4 curvature too slow even with matter rational | unexpected swell | series in amplitude t to low order (avoid full inverse), or smaller/sparser rational M | low |
| Exact full-M result intractable | expression swell | representative finite rational M + ||M||->0 series; accept "decisive on representative M" rigor | low (already the planned rigor) |
| Cross-term off-switch ambiguous | block structure unclear | operational det_block = "drop the `2*Re((x2 x1) x3)` term"; verify reduction to det(V_0) at M=0 | low |

**Decision criteria:** If, at a properly fixed V_0-background with all three slots populated, Delta R(M) (i) survives the cross-term off-switch, OR (ii) does not vanish as ||M||->0, OR (iii) is pure-Lambda (S_munu=0, Weyl=0), then matter does NOT source the slice curvature: report "position-dependent but pure-Lambda / not matter-sourced", do NOT proceed to Phase 73 (NEGATIVE-RESULT-IS-SUCCESS). If Delta R(M) vanishes under the off-switch AND vanishes as ||M||->0 AND carries traceless-Ricci/Weyl structure, matter IS cross-term-sourcing the curvature (SURVIVES; Phase 73 greenlit).

## Lambda-vs-Matter Decomposition (n=4) — explicit formulas for VALD-04

The executor computes these EXACT over Q at the fixed V_0-background, with indices raised by the slice metric g_munu (mostly-minus; the decomposition is an algebraic identity in the curvature tensor, signature-agnostic). n = 4.

- **Ricci scalar:** R = g^{munu} R_munu = g^{ik} g^{jl} R_ijkl  (engine `ricci_scalar`).
- **Traceless Ricci:** S_munu = R_munu - (R / n) g_munu = R_munu - (R/4) g_munu.  Einstein space <=> S_munu = 0 (Ricci ∝ metric).
- **Maximally-symmetric reference (pure-Lambda) Riemann:** R^{(Lambda)}_{abcd} = (R / (n(n-1))) (g_ac g_bd - g_ad g_bc) = (R/12)(g_ac g_bd - g_ad g_bc) for n=4. Subtract this to expose non-Lambda structure.
- **Scalar part of Riemann:** S_ijkl = (R/(n(n-1)))(g_il g_jk - g_ik g_jl) = (R/12)(g_il g_jk - g_ik g_jl).
- **Traceless-Ricci part of Riemann:** with Z_jk = S_jk (= R_jk - (R/4)g_jk), E_ijkl = (1/(n-2))(Z_il g_jk - Z_jl g_ik - Z_ik g_jl + Z_jk g_il) = (1/2)(...) for n=4.
- **Weyl tensor (residual):** C_ijkl = R_ijkl - S_ijkl - E_ijkl  (n>=4). Conformally invariant; nonzero Weyl = genuine non-conformally-flat structure.
- **Einstein criterion:** S_munu = 0 everywhere on the neighborhood => pure-Lambda (with Lambda read from R; at the center Lambda<0 = Cartan). **Genuine M-sourcing requires Delta S_munu != 0 and/or Delta C_ijkl != 0 tracking M**, beyond a constant shift of R.

(Source: Wikipedia "Ricci decomposition"; Besse, *Einstein Manifolds*; standard. The criterion "Einstein <=> traceless Ricci = 0" and the maximally-symmetric form R_abcd = (R/(n(n-1)))(g_ac g_bd - g_ad g_bc) are textbook.)

## Cross-term ON/OFF construction — operational recipe for CALC-03

The matter coupling channel is the SINGLE term in `det_3`:
```
cross = oct_mul(oct_mul(x2, x1), x3)   # (x2 x1) x3
det_3(X) = a*b*g - a*|x1|^2 - b*|x2|^2 - g*|x3|^2 + 2*cross[0]
```
with x1 the V_0 octonion (matrix entry X[2][1]), x2,x3 the V_{1/2} octonions (X[0][2], X[1][0]). x1 carries V_0 content (incl. the slice p,q and the internal W-sector); x2,x3 carry the V_{1/2} matter.

- **Cross-terms OFF (block-diagonal norm):** `det_block(X) = a*b*g - a*|x1|^2 - b*|x2|^2 - g*|x3|^2` (the `2*cross[0]` term dropped). This is the unique V_0<->V_{1/2} mixing channel; with it removed, the V_0 sector (a,b,g,x1) and the V_{1/2} matter (x2,x3) no longer couple through the triple product. At M=0 (x2=x3=alpha-matter=0) det_block reduces to det(V_0) = the slice norm (verify exactly). Implement as a one-line variant of `det_3` (a `cross_off=True` flag, or a separate `det_3_block`).
- **Feed the SAME M!=0 through both** `Phi = -log det_3` and `Phi_off = -log det_block`, compute Delta R(M) for each at the SAME fixed V_0-background, and compare. Decisive: Delta R_full != 0, Delta R_off = 0 (or decisively smaller) => cross-term/matter-sourced.
- **Non-vacuity gate (Pitfall 3):** before running, assert `2*cross[0] != 0` at the chosen M — i.e. all three slots x1,x2,x3 populated with octonionic content (include e_4..e_7 components so the test is genuinely non-associative).

Note: the prompt's "det(V_1)·det(V_0)" product is schematic; the operational, unambiguous definition is "det_3 with the `2*Re((x2 x1) x3)` term set to zero" (the only term coupling V_0 to V_{1/2}). Document this and verify the M=0 reduction.

## Isolation Protocol — holding V_0 fixed, varying only M (the subtle part)

Per the Phase-71 reframing, the matterless geometry already varies with det_2; matter must be isolated AT FIXED V_0-background:

1. **Choose a fixed V_0-background.** Either the F_4-symmetric center (X_bg = I/3, det_2 at the center value, the pure-Lambda Cartan baseline R=-3) — cleanest — or a single chosen off-center det_2 leaf (a Phase-71 ROUTE1 basepoint, with its known matterless R). Hold its V_0 content (alpha=beta=gamma diagonal + V_0 octonion x1 internal/slice) FIXED.
2. **Vary ONLY matter M in V_1 (alpha-matter, index 0) ⊕ V_{1/2} (indices 11..26).** In the engine, populate ONLY these indices in `delta`; do NOT change the V_0-internal W-sector {4..9} or the slice background between the M=0 and M!=0 runs.
3. **Define the matter-sourced curvature as the DIFFERENCE** Delta R(M) := R(X_bg + M) - R(X_bg), with X_bg fixed. Likewise Delta S_munu, Delta Weyl. The matterless det_2-variation cancels in the difference (same V_0-background both sides), so Delta R is purely the M-effect.
4. **M-placement (non-vacuous):** ensure all three off-diagonal octonion slots are populated so the cross-term `2*Re((x2 x1) x3)` is genuinely nonzero — x1 from the fixed V_0-background (must be nonzero, OR add a V_0 internal component to the FIXED background so x1!=0), x2,x3 from the V_{1/2} matter, with e_4..e_7 content (genuinely octonionic). [Tension to resolve in planning: if X_bg is the bare center I/3 then x1=0 and the triple product vanishes — so either (a) use a fixed off-center V_0-background with x1!=0, or (b) include a fixed V_0-internal x1 component in the background and vary only x2,x3 matter. Document the choice; verify the cross-term is nonzero.]
5. **Confirm V_1 vs V_{1/2}:** compute Delta R separately for V_1-only and V_{1/2}-only matter to confirm/explain the Phase-71 V_1-inertness (alpha is absent from the octonion triple).

This protocol is what distinguishes Phase 72 from Phase 71: Phase 71 varied the V_0-background (and found matterless variation); Phase 72 FIXES the V_0-background and varies ONLY matter, reading off the M-dependent Delta.

## Caveats and Alternatives (pre-submission self-critique)

1. **Assumption that might be wrong:** that the cross-term `2*Re((x2 x1) x3)` is the ONLY V_0<->matter channel. It is the only OCTONION-mixing term, but the diagonal coefficients (a,b,g multiplying |x1|^2, |x2|^2, |x3|^2) also couple the diagonal V_0/V_1 content to the matter norms. The "block-diagonal" off-switch removes only the triple product; the |x2|^2,|x3|^2 terms remain and still couple x2,x3 to a,b,g. So "cross-terms off" is precise for the V_0<->V_{1/2} TRIPLE coupling but does not fully decouple the matter norms from the diagonal. This is acceptable (the triple product IS the prompt's named channel) but should be stated explicitly — Open Question 2.
2. **Approach I dismissed too quickly:** computing the FULL dim-10 V_0 curvature with matter. Dismissed because the dim-10 symbolic inverse times out (>200s) and Phase-71 established the dim-4 h_2(C_u) sub-slice is the decisive arena. Correct to dismiss for the decisive verdict; a dim-10 mpmath spot-check could be a non-decisive sanity triage only.
3. **Limitation I might be understating:** the rigor is "exact on representative M", not "proved for all M". A matter-sourcing verdict on a few representative M (with off-switch + ||M||->0) is decisive for SURVIVES/negative, but is NOT a general theorem. Phase C (Einstein structure across a neighborhood) is where generality would be tested; Phase 72 deliberately stops short. Stated in Level of Rigor.
4. **Simpler method overlooked?** The series-in-amplitude approach (CALC-04) is actually SIMPLER than full finite-M exact curvature for the scaling law and should be the primary tool there; full finite-M exact is reserved for the decisive on/off verdict. Both are in the engine's wheelhouse.
5. **Would a specialist disagree?** A Jordan-algebra geometer might note that "matter sourcing curvature" is unusual framing — the cone is homogeneous under E_6, so all the curvature is "intrinsic to the algebra," and calling the V_{1/2} contribution "matter" is a physics interpretation, not a math theorem. This is exactly the milestone's point (the interpretation is what's being tested) and is guarded by fp-lambda-as-sourcing and fp-ensemble-gravity. The math verdict (does Delta R(M) vanish under off-switch / as ||M||->0 / carry non-Lambda structure) is interpretation-free and exact — that is what Phase 72 decides.

## Sources

### Primary (HIGH confidence)

- Faraut & Koranyi, *Analysis on Symmetric Cones* (1994), Oxford — cone metric g_X = Hess(-log det), g^{pq} = P(X), E_{6(-26)}/F_4 symmetric-space structure, Cartan/Einstein baseline. [ref-faraut-koranyi]
- Totaro, "The curvature of a Hessian metric", arXiv:math/0401381, Cor 2.3 — R_ijkl closed form; rank-1 slice constant curvature -d^2/4; the engine's curvature method. [ref-totaro]
- McCrimmon, *A Taste of Jordan Algebras* (2004) — Peirce decomposition, cubic norm, P(X). [ref-mccrimmon]
- `~/scratch/get-physics-done/paper6-bulk-geometry-prompt.md` — authoritative milestone spec, Phase B targets + reporting discipline. [ref-prompt]
- `.gpd/phases/71-a-homogeneity-kill-gate/71-VERIFICATION.md` — VERIFIED Phase-71 findings (matterless position-dependence, V_1 inert, V_{1/2} active, det_2 modulus, exact R anchors).
- `code/bulk_geometry_verification.py` — the warm engine (det_3 SSOT, Totaro curvature, offcenter API, II); ALL_PASS exit 0. Read l.342-468 (det_3/Tr/polarize_d), l.976-1210 (center/offcenter metric, construction-(ii) bridge), l.1312-1433 (cubic_form_C/totaro_riemann/ricci_scalar/kretschmann/sectional_curvature), l.1888-1947 (second_fundamental_form).
- `.gpd/CONVENTIONS.md` — v17.0 locked conventions (18/18).
- Wikipedia, "Ricci decomposition" — exact n=4 scalar/traceless-Ricci/Weyl formulas + Einstein/maximally-symmetric criteria (textbook-standard; cross-checked against Einstein-four-manifold literature).

### Secondary (MEDIUM confidence)

- "Curvatures of metric Jordan algebras", arXiv:2309.02682 (2023) — every formally real Jordan algebra admits a Jordan-Einstein metric of NEGATIVE scalar curvature; corroborates the M=0/center Cartan baseline (Lambda<0). PDF could not be parsed in full; relevance from the search abstract. MATTERLESS side only.
- Curvature decompositions on Einstein four-manifolds, arXiv:1903.11817; Bochner formulas for Weyl on 4d Einstein manifolds, arXiv:1612.00627 — corroborate the n=4 decomposition.
- `.gpd/research/METHODS.md`, `PITFALLS.md`, `COMPUTATIONAL.md` — project-level research. USE WITH CAUTION: their det-SSOT references to `octonion_algebra.py` are SUPERSEDED by the v17.0 convention lock (use engine `det_3`). The performance cliffs (>200s symbolic inverse, ~19s matter-rational, vacuous-triple-product) and the Lambda-vs-matter / cross-term-off-switch methodology are accurate and directly used here.

### Tertiary (LOW confidence)

- `~/scratch/get-physics-done/rho_directional_derivatives.py` (real-only cross-term — strategy reuse only), `peirce_coupling.py` (numpy/float — intuition only), `~/repos/blog/research/qualia-fixed-point/h3o_tower.py` (cubic-norm benchmark — optional provenance check). NOT on the decisive path.
- **No external literature found for the matter-sourcing CLAIM** (off-diagonal-Peirce content sourcing Hessian curvature on a symmetric cone). Novel; validation is internal (exact-over-Q + limiting cases + off-switch), not literature-benchmarked.

## Metadata

**Confidence breakdown:**

- Mathematical framework: HIGH — Totaro curvature, Faraut-Koranyi cone metric, Ricci decomposition are all standard/certified; the engine implements them and passes regression.
- Standard approaches: HIGH on the method (engine measured end-to-end), MEDIUM on the matter-sourcing OUTCOME (novel; that's the phase's open question).
- Computational tools: HIGH — SymPy 1.14.0 installed; engine ALL_PASS; all costs MEASURED (COMPUTATIONAL.md), not assumed.
- Validation strategies: HIGH — limiting cases (M->0, center pure-Lambda, H^3), cross-term off-switch, reality/exactness, Phase-71 regression anchors all concrete and exact.
- External literature for matter-sourcing: LOW — none found; expected for this novel construction (Novel Territory — internal validation only).

**Research date:** 2026-05-30
**Valid until:** Physics/math results stable indefinitely (Totaro, Faraut-Koranyi, Ricci decomposition are decades-old textbook). The engine API is the volatile part — re-confirm function signatures if `code/bulk_geometry_verification.py` is refactored. SymPy version (1.14.0) is the fastest-moving dependency.
