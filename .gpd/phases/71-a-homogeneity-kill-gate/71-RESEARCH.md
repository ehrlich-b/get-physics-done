# Phase 71: A — Homogeneity KILL Gate - Research

**Researched:** 2026-05-30
**Domain:** Mathematical physics — Riemannian/Lorentzian differential geometry of the symmetric cone of h_3(O); Hessian-metric curvature of the cubic norm; homogeneity via exact orbit-dimension over Q; second fundamental form of a Peirce sub-slice.
**Confidence:** HIGH on the machinery (curvature engine, orbit-dimension method, totally-geodesic shortcut — all pinned to peer-reviewed sources AND warm in-repo code); the SCIENTIFIC VERDICT (KILL vs SURVIVES) is genuinely uncertain by design and leans GREENLIGHT but is an inference that THIS phase must compute.

## Summary

Phase 71 is the decisive KILL gate of v17.0. Fixing the primitive idempotent E_11 = diag(1,0,0) breaks the cone's structure group E_6 down to Stab_{E_6}(E_11) (a parabolic subgroup, Levi ~ Spin(9,1)). The route to "gravity as inherited slice curvature" is ALIVE iff that residual group does NOT act transitively enough on (basepoint, slice) pairs to make them all isometric — equivalently iff the inherited slice metric g_mu_nu(x) = eta_mu_nu + h_mu_nu(x) on V_0 (with h_2(C_u) ~ R^{3,1} the physical 4-dim sub-slice) has genuinely position-DEPENDENT curvature invariants. The central tension the phase must resolve: the ambient det=1 hypersurface is the Riemannian symmetric space E_{6(-26)}/F_4, which is HOMOGENEOUS with parallel (covariant-constant) curvature — so its curvature invariants are the same number everywhere. The slice can only be inhomogeneous if fixing E_11 and restricting to V_0 genuinely breaks that homogeneity. The precise mechanism is EXTRINSIC: by the Gauss equation, R^slice = (R^ambient restricted to the slice) + (second-fundamental-form II terms); if the slice is totally geodesic (II = 0) it inherits the ambient constant curvature => homogeneous => KILL. So the totally-geodesic question is a cheap, decisive potential KILL, and the literature (Kollross-Rodriguez-Vazquez 2022, Table 7) leans GREENLIGHT because the V_0 = h_2(O)-type slice (SO(9,1)/SO(9)) does NOT appear in the classified maximal totally-geodesic submanifolds of E_{6(-26)}/F_4 — but absence-from-the-maximal-list is an inference that must be confirmed (rule out V_0 sitting inside a larger geodesic submanifold).

The recommended path runs TWO independent cross-checking routes that must AGREE, plus a cheap shortcut. Route 1 (curvature invariants, the primary verdict): build the slice metric off-center, compute the Ricci scalar R(x) and Kretschmann K(x) via Totaro's closed-form Hessian-curvature formula EXACTLY over Q, evaluate them at >= 2 distinct generic rational basepoints, and check whether they differ. Route 2 (stabilizer transitivity, the cross-check): build the e_6 Lie algebra (78-dim = f_4 + L(traceless)), compute dim Stab_{E_6}(E_11) and the dimension of the (basepoint, slice) family modulo that stabilizer as exact ranks over Q — reusing orbit_dimension_gate.py — after FIRST reproducing the single-copy calibration anchor (orbit 24 / Spin(8) stabilizer 28). Shortcut (potential cheap KILL): compute the second fundamental form II of the V_0 slice; II = 0 => totally geodesic => homogeneous => KILL. The decisive arithmetic MUST be exact over Q (float ranks and float curvature fabricate the verdict via catastrophic cancellation). The verdict must be reported without softening either way: a homogeneous result is a clean, valuable KILL and the milestone STOPS.

**Primary recommendation:** Run the curvature-invariant route (Route 1) on the 4-dim h_2(C_u) sub-slice as the decisive arena (the dim-10 V_0 symbolic inverse times out and is OFF the critical path); compute R(x), K(x) via Totaro's formula exact over Q at >= 2 distinct rational basepoints off-center; cross-check the verdict against the exact Stab_{E_6}(E_11)-orbit-vs-basepoint-family dimension count (Route 2, reproducing the orbit-24/Spin(8)-28 anchor first); and use the second-fundamental-form II = 0 test as the cheap independent shortcut. The two routes MUST agree; disagreement between the Riemannian restriction and the Lorentzian bridge localizes a coordinate/Wick artifact and sends you back to Phase 70.

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| ----------------- | ---- | ------------------- | --------------- | ---------------------- |
| **code/bulk_geometry_verification.py** (Phase 70 CERTIFIED SSOT) | warm engine / prior artifact | The det_3 SSOT + `cone_hessian_at_center()` + `slice_det_form()` + the FIXED construction-(ii) bridge. Every curvature is built from this det. | REUSE & EXTEND (do NOT rebuild; do NOT import octonion_algebra) | plan (build metric on top), execution, verification |
| **code/orbit_dimension_gate.py** | warm engine / prior artifact | The exact-over-Q orbit/stabilizer dimension method (`infinitesimal_action`, `single_copy_orbit_rank`, `exact_qq_rank`, `_is_genuinely_octonionic_integer`); reproduces orbit 24 / Spin(8) 28 — the CALIBRATION anchor. | REUSE the pattern for CALC-01; reproduce the single-copy anchor FIRST | plan (Route 2 / CALC-01), execution, verification |
| **ref-totaro** Totaro, "The Curvature of a Hessian Metric," arXiv:math/0401381 | method / benchmark | THE curvature engine: R_ijkl = -(1/4) g^{pq}(f_jlp f_ikq - f_ilp f_jkq), 3rd-derivatives-only; H^3 const curvature -d^2/4 = -1; E_{6(-26)}/F_4 example. | cite + use formula; benchmark Riemann sign on H^3 | plan (Route 1 curvature), execution, verification |
| **ref-faraut-koranyi** Faraut & Koranyi, *Analysis on Symmetric Cones* (OUP 1994) | method | g_X = Hess(-log det); g^{pq} = P(X) (quadratic rep, inverse metric symbolically); cone = E_{6(-26)}/F_4 x R+; det=1 hypersurface is the symmetric space. | cite; use P(X) for the inverse metric if symbolic inverse is needed | plan (metric inverse), execution |
| **ref-kollross-rodriguez-vazquez** arXiv:2202.10775 (Adv. Math. 2023), Table 7 | benchmark / decisive inference | Maximal totally-geodesic submanifolds of E_{6(-26)}/F_4. V_0=h_2(O) slice (SO(9,1)/SO(9)) and H^3 are ABSENT => leans non-geodesic => GREENLIGHT, but an INFERENCE to confirm via the II computation. | cite; use as the totally-geodesic anchor for CALC-02 | plan (CALC-02), execution, verification |
| **ref-mccrimmon** McCrimmon, *A Taste of Jordan Algebras* (2004) | method | Peirce decomposition; P(X) = 2 L(X)^2 - L(X^2) (the quadratic representation = inverse metric). | cite; use P(X) formula | plan (inverse metric), execution |
| **ref-baez-octonions** Baez, "The Octonions," Bull. AMS 39 (2002) | method | F_4 = Aut(h_3(O)); E_6 = Stab(det); SL(2,O) ~ Spin(9,1) (the expected Levi of Stab); OP^2 = F_4/Spin(9). | cite | plan (group theory), execution |
| **ref-52-kkt** derivations/52-kkt-spacetime.tex, 52-observer-uniqueness.tex | prior artifact | h_2(C_u) ~ R^{3,1}, mostly-minus eta from det_2; the index map {17,18,19,26} == engine {x1,x2,x3,x10}; H^3 = SL(2,C)/SU(2) identification. | use the eta + frame map (already in the engine) | plan (slice metric), execution |
| **ref-warm-engine** ring_lemma_verification.py + embedding_under_E_verification.py | prior artifact | Source of the byte-identical det_3 + helpers; `jordan_L_matrix`, `inner_derivations` (f_4), `_standard_basis_27` — the primitives to build e_6. | reuse primitives (already inlined in bulk_geometry_verification.py) | plan (Route 2 e_6 build), execution |
| **ref-h3o-tower** ~/repos/blog/research/qualia-fixed-point/h3o_tower.py | reference only | The corrected cubic-norm triple order; PRESENT at that path (29 KB). Engine det_3 is the SSOT regardless — use only as a cross-reference, not a source of det. | do NOT import; cross-reference only if needed | n/a (engine is SSOT) |

**Missing or weak anchors:**
- **peirce_coupling.py, rho_directional_derivatives.py — ABSENT from code/ (confirmed this session).** The off-center expansion machinery these names imply does NOT exist as a script. **RESOLUTION (decided below, HIGH confidence): the off-center expansion must be NEWLY BUILT in this phase, but it is a TRIVIAL extension** of the existing `cone_hessian_at_center()` — replace the center-substitution `_center_subs()` with a generic-basepoint substitution (or keep the slice coords symbolic). The Phase 70 engine provides the Hessian-AT-the-center only; it does NOT yet provide an off-center expansion, a curvature computation on the cone-Hessian slice, OR a second fundamental form. Those are this phase's new code.
- **e_6 generators (78-dim) are NOT explicitly built anywhere in code/.** The codebase has f_4 (52-dim, `inner_derivations()`) and the multiplication operators (`jordan_L_matrix`), but not the assembled e_6. **RESOLUTION: build e_6 = f_4 (+) L(h_3(O)_traceless) (52 + 26 = 78) using the existing `jordan_L_matrix` + `inner_derivations` primitives** — a clean ~15-line extension. The `E(X)` in embedding_under_E_verification.py is the entrywise C_u PROJECTOR, NOT the group E_6.
- **Exact Stab_{E_6}(E_11) is not cleanly tabulated in the literature** (a parabolic; Levi expected ~ Spin(9,1), dim ~45). **RESOLUTION: compute it directly as the kernel `{D in e_6 : D . E_11 = 0}` over Q** — exactly the orbit_dimension_gate.py pattern (dim Stab = 78 - dim orbit of E_11). Do NOT rely on a looked-up value.

## Conventions

| Choice | Convention | Alternatives | Source |
| ------ | ---------- | ------------ | ------ |
| Cubic norm / det | engine `det_3` (cross-term `2Re(x2* x0* x1)` = `2Re((x2 x1) x3)`); SSOT | buggy `(x1 x2) x3` (FORBIDDEN) | CONVENTIONS.md §0; ring_lemma_verification |
| Potential | `-log det` (FIXED) | bare `det` (do NOT mix) | CONVENTIONS.md §4 |
| Cone metric | `g_X = Hess(-log det)`; inverse `g^{pq} = P(X)` | — | Faraut-Koranyi |
| Signature (slice) | mostly-minus (-,+,+,+) Lorentzian via det_2 | — | CONVENTIONS.md §1 |
| Signature (bulk) | Riemannian, positive-definite | — | CONVENTIONS.md §1 |
| Signature bridge | construction (ii): g = eta + h, eta from det_2, h := Hess - Hess\|center; (i) Wick-via-u REJECTED | construction (i) (rejected) | CONVENTIONS.md §1; Phase 70 |
| Center | I/3 (F_4-symmetric, rho_J = 0); det(I/3)=1/27 | — | CONVENTIONS.md §3 |
| E_11 | diag(1,0,0); Peirce V_1(1) (+) V_{1/2}(16) (+) V_0(10)=h_2(O) | — | CONVENTIONS.md §3 |
| Spacetime sub-slice | engine indices {x1,x2,x3,x10} = {17,18,19,26}; C_u = span{1,e_7} | — | Phase 70 (CONFIRMED) |
| Riemann/Ricci sign | STATE explicitly; benchmark on H^3 (constant curvature -1) BEFORE any verdict | — | CONVENTIONS.md §4; Phase 70 |
| Arithmetic | EXACT over Q (sympy.Rational/Matrix); ranks via `sympy.Matrix.rank()` or DomainMatrix-over-QQ; NEVER numpy float rank | float64 (FORBIDDEN on decisive path) | CONVENTIONS.md §7 |
| Off-center parameter | rho_J(X_bg) (distance from center I/3); NOT the spacetime coordinate x (which is O(1), the WRONG expansion variable) | — | CONVENTIONS.md §6; SUMMARY |

**CRITICAL: All equations and results below use these conventions.** They are LOCKED for v17.0 (state.json `convention_lock`, mirrored in .gpd/CONVENTIONS.md). The Riemann sign must be benchmarked on H^3 = -1 before any KILL/SURVIVES verdict is trusted (Phase 70 reproduced the standard-H^3-metric R=-6, K=-1; the cone-Hessian slice computation that confirms this on the actual metric is THIS phase's first curvature check).

Convention loading: see agent-infrastructure.md Convention Loading Protocol.

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in This Phase |
| -------- | ---------------- | ------ | ------------------ |
| `g_ij(X) = d^2(-log det)/dx_i dx_j` | Cone Hessian metric | Faraut-Koranyi | DERV-01: the slice metric, evaluated off-center |
| `g_munu(x) = eta_munu + h_munu(x)`, `h := Hess\|_slice - Hess\|_center` | Construction-(ii) bridge | Phase 70 (LOCKED) | The object tested for x-dependence |
| `g^{pq} = P(X) = 2 L(X)^2 - L(X^2)` | Quadratic representation = inverse metric | Faraut-Koranyi; McCrimmon | Symbolic metric inverse without finite-differencing (avoids `g.inv()` blowup) |
| `R_ijkl = -(1/4) sum_pq g^{pq}(f_jlp f_ikq - f_ilp f_jkq)` | Totaro Hessian-curvature closed form | Totaro 2004, arXiv:math/0401381 | Route 1: Riemann tensor from 3rd derivatives ONLY (det cubic => f_ijkl = 0) |
| `f_ijk = d^3(-log det)/dx_i dx_j dx_k`; `d(X,X,X) = 6 det` | 3rd-derivative tensor (= `polarize_d`) | Totaro; engine | Inputs to the Totaro formula |
| `R^slice_ijkl = R^ambient_ijkl\|_slice + (II_ik II_jl - II_il II_jk)` | Gauss equation | O'Neill, *Semi-Riemannian Geometry* | CALC-02: II = 0 => R^slice = ambient constant => KILL |
| `II(X,Y) = (nabla_X Y)^perp` | Second fundamental form | O'Neill | CALC-02: the totally-geodesic test |
| dim(orbit of v) = rank of [M . v]_{M in basis} at generic v | Generic orbit dim = rank of infinitesimal action (char 0) | Derksen-Kemper; Garibaldi-Guralnick | Route 2 / CALC-01 |
| dim Stab_{E_6}(E_11) = 78 - dim(orbit of E_11) = dim ker{D -> D . E_11} | Orbit-stabilizer (Lie-algebra level) | standard | CALC-01: the residual symmetry dimension |
| e_6 = f_4 (+) L(h_3(O)_traceless), dim 52 + 26 = 78 | Tits/Koecher construction of e_6 | Baez; standard | Route 2: build the E_6 Lie algebra from existing primitives |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --------- | ------------ | ------------- | ------------------ |
| Off-center Hessian expansion | Evaluate `Hess(-log det)` at a generic basepoint X_bg = I/3 + (perturbation), NOT just the center | DERV-01 (Route 1 metric) | Faraut-Koranyi; this phase's new code |
| Totaro closed-form Riemann | Riemann/Ricci/Kretschmann from 3rd derivatives of the potential | Route 1 curvature | Totaro 2004 |
| Curvature-invariant evaluation | R(x), K(x) as functions of the basepoint; compare across >= 2 basepoints | Route 1 verdict | standard Riemannian geometry |
| Parallel-Riemann check | Test `nabla R = 0` (covariant-constant) — a symmetric space has parallel Riemann | Route 1 (homogeneity diagnostic) | O'Neill; Helgason |
| Exact orbit-dimension over Q | dim Stab / dim orbit-family via rank of infinitesimal-action matrix | Route 2 / CALC-01 | Derksen-Kemper; orbit_dimension_gate.py |
| e_6 Lie algebra construction | Assemble 78-dim e_6 = f_4 (+) L(traceless) | Route 2 | Baez; `jordan_L_matrix` + `inner_derivations` |
| Kernel-over-Q computation | Stab = ker{D -> D . E_11} as an exact nullspace | CALC-01 | standard linear algebra over Q |
| Second-fundamental-form (Gauss) | II of V_0 in the cone; II = 0 <=> totally geodesic | CALC-02 | O'Neill; Gauss-Codazzi |

### Approximation Schemes

| Approximation | Small Parameter | Regime of Validity | Error Estimate | Alternatives if Invalid |
| ------------- | --------------- | ------------------ | -------------- | ----------------------- |
| Expand off-center in rho_J(X_bg) | rho_J (distance from I/3) | near-center; jet TERMINATES (det cubic) | 0 (exact polynomial, no truncation) | full symbolic at a fixed rational basepoint |
| Evaluate invariants at rational basepoints | none (exact points) | always; rank lower-semicontinuous so use >= 2 generic points + MAX | 0 (exact over Q) | fully symbolic x (risks symbolic blow-up) |
| Restrict to 4-dim h_2(C_u) sub-slice | none | the decisive arena; dim-10 V_0 symbolic inverse times out (>200s) | n/a | mpmath dim-10 fallback (guarded; NEVER on the "=0?" verdict) |

**CRITICAL on the expansion variable:** Expand in rho_J(X_bg) (off-center-ness of the BASEPOINT), NOT in the spacetime coordinate x. The spacetime x is O(1) — it is the WRONG expansion variable and expanding in it manufactures spurious "position dependence" (forbidden proxy fp-coordinate-curvature). Distinct basepoints means distinct X_bg = I/3 + (different off-center perturbations), each a valid point of the cone; the verdict is whether the curvature INVARIANTS differ between them.

## Standard Approaches

### Approach 1: Curvature-invariant route (Route 1, RECOMMENDED — the primary verdict)

**What:** Build the inherited slice metric g_munu(x) on the 4-dim h_2(C_u) sub-slice off-center, compute the Ricci scalar R(x) and Kretschmann scalar K(x) via Totaro's closed-form Hessian-curvature formula EXACTLY over Q, evaluate at >= 2 distinct generic rational basepoints, and compare. Invariants differ => SURVIVES; invariants equal => KILL.

**Why standard:** Curvature scalar invariants are coordinate-independent — they are the ONLY honest discriminator between genuine position-dependent curvature and a coordinate artifact (metric components can vary by coordinates even on a homogeneous space). Totaro's formula is the right engine because it needs only 3rd derivatives of the potential (det is cubic => f_ijkl = 0 => the jet terminates), avoiding a `sympy.diffgeom` blowup on the metric.

**Track record:** The Totaro formula is peer-reviewed (Int. J. Math. 15, 2004), confirmed real and on-topic; the in-repo measurement (project COMPUTATIONAL scout) ran a full Christoffel+Riemann with matter rational on the dim-4 slice in ~19s exact over Q. Phase 70 reproduced the H^3 benchmark (R=-6, K=-1) on the standard metric.

**Key steps:**
1. **Benchmark the Riemann sign FIRST.** Compute curvature of the M=0 det=1 sub-slice (H^3 = SL(2,C)/SU(2)) via the cone-Hessian + Totaro; confirm constant sectional curvature -1 (Totaro -d^2/4, d=2). This pins the Riemann/Ricci sign convention BEFORE any verdict. (Phase 70 stated this target; this phase computes it on the actual cone-Hessian slice.)
2. **Build the off-center slice metric** g_munu(x) by extending `cone_hessian_at_center()`: replace `_center_subs()` with a generic-basepoint substitution X_bg = I/3 + (off-center perturbation in V_0 and/or matter directions). Keep the metric exact over Q.
3. **Compute R(x), K(x)** via the Totaro closed form (hand-rolled Christoffel/Riemann loops, ~30 lines; do NOT call `sympy.diffgeom` on the metric). Use `g^{pq} = P(X)` for the inverse to avoid `g.inv()` blowup, OR substitute matter to small rationals BEFORE inverting (the measured mitigation).
4. **Evaluate at >= 2 distinct generic rational basepoints** and compare R, K exactly over Q. Also compute `d_x R` and `d_x K` and test for identical-zero. Optionally check `nabla R = 0` (parallel Riemann — a homogeneous-space diagnostic).
5. **Verdict:** invariants differ across basepoints => position-dependent => SURVIVES; invariants identical => homogeneous => KILL. Report exactly, no softening.

**Known difficulties at each step:**
- Step 2: the off-center substitution must perturb the BASEPOINT (rho_J), not the spacetime coordinate. Mis-choosing the variable is fp-coordinate-curvature.
- Step 3: the symbolic matrix inverse `g.inv()` with matter+coords all symbolic TIMES OUT (>200s, measured). Mitigation: P(X) inverse, or matter-rational-then-invert, keeping only the 4 slice coords symbolic.
- Step 4: a single basepoint CANNOT detect x-dependence — a constant nonzero curvature is still homogeneous (forbidden proxy / Pitfall 11). MUST use >= 2 distinct basepoints.

### Approach 2: Stabilizer-transitivity route (Route 2 / CALC-01, the mandatory cross-check)

**What:** Build e_6 (78-dim), compute dim Stab_{E_6}(E_11) and the dimension of the (basepoint, slice) family modulo that stabilizer as exact ranks over Q (reusing orbit_dimension_gate.py), after reproducing the single-copy anchor (orbit 24 / Spin(8) 28) first. If Stab acts transitively on the basepoint family (orbit dim = family dim) => all basepoints isometric => h x-independent => KILL; if the orbit is a proper subset (orbit dim < family dim) => genuinely inequivalent basepoints => h varies => SURVIVES.

**When to switch:** This is NOT a fallback — it is a MANDATORY second route that must AGREE with Route 1 (the two-route cross-check in success criterion 3). If the two routes disagree, neither verdict is trustworthy; investigate.

**Tradeoffs:** Route 2 is purely group-theoretic / algebraic (no curvature), so it is immune to the Riemann-sign and Wick-artifact hazards of Route 1 — which is exactly why it is the cross-check. It cannot, by itself, give the curvature value (only the homogeneity yes/no).

**Key steps:**
1. **Reproduce the single-copy anchor FIRST** (calibration): run `check_single_copy_orbit_dim` / `check_single_copy_gate` => orbit 24 / Spin(8) stabilizer 28. If this does NOT reproduce, the builder is untrustworthy — re-calibrate before trusting the E_11 count (explicit backtracking trigger).
2. **Build e_6 = f_4 (+) L(h_3(O)_traceless)** (52 + 26 = 78) using `inner_derivations()` (f_4) and `jordan_L_matrix(a, basis)` for traceless a. Verify dim = 78 as an exact span rank over Q.
3. **Compute dim Stab_{E_6}(E_11)** = dim ker{D -> D . E_11} = 78 - rank of [D . E_11]_{D in e_6 basis}, exact over Q. (Expected: parabolic, Levi ~ Spin(9,1).)
4. **Compute the (basepoint, slice)-family dimension and the orbit dimension under Stab_{E_6}(E_11)** via `single_copy_orbit_rank` applied to Stab generators acting on a generic basepoint (use `_is_genuinely_octonionic_integer` to validate the point; MAX over >= 2 points).
5. **Verdict:** orbit dim = family dim => transitive => KILL; orbit dim < family dim => SURVIVES. Cross-check against Route 1.

### Anti-Patterns to Avoid

- **Reading varying metric COMPONENTS as curvature (fp-coordinate-curvature):** metric components vary by coordinate choice even on a homogeneous space. Only curvature-SCALAR INVARIANTS decide.
  - _Example:_ the off-center Hessian components g_munu obviously change as you move the basepoint; that is NOT evidence of inhomogeneity. R(x), K(x) changing is.
- **Float ranks / float curvature (fp-float-decisive):** rank and curvature are derivative-cancellation factories (`R ~ dGamma + GammaGamma`); float tolerance fabricates the verdict.
- **Single-basepoint sampling:** a constant nonzero curvature is still homogeneous. Must use >= 2 distinct basepoints.
- **Relabeling a homogeneous result as "approximately position-dependent" (fp-relabel-homogeneous):** a homogeneous result is a clean valuable KILL. Report it as such and STOP.
- **Over-symmetrizing ("the cone is homogeneous so the slice is too"):** WRONG — fixing E_11 BREAKS transitivity to Stab_{E_6}(E_11). The whole point is that the residual group may NOT be transitive.
- **Gauging away real variation with a group element NOT in Stab_{E_6}(E_11):** only the residual stabilizer's action counts; using a general E_6 element to "show" two basepoints are isometric is a false KILL.
- **Calling `sympy.diffgeom` on the dim-10 metric:** n^4 components x octonionic-rational simplify => blowup. Hand-rolled Totaro on the dim-4 slice is the decisive path.

## Existing Results to Leverage

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
| ------ | ---------- | ------ | ---------- |
| Cone = E_{6(-26)}/F_4 x R+; g_X = Hess(-log det) is the canonical metric | — | Faraut-Koranyi 1994 | The ambient geometry; do not re-derive |
| det=1 hypersurface is a Riemannian SYMMETRIC space (homogeneous, parallel curvature) | — | Faraut-Koranyi; Cartan | This is the SOURCE of the homogeneity tension; cite, do not re-derive |
| Totaro Hessian-curvature closed form | `R_ijkl = -(1/4) g^{pq}(f_jlp f_ikq - f_ilp f_jkq)` | Totaro 2004, eq. (read locally by project scout) | Route 1 curvature engine; USE verbatim |
| H^3 = SL(2,C)/SU(2) constant sectional curvature -1 | `K = -d^2/4 = -1` (d=2) | Totaro Cor. 2.3; ref-52-kkt | Riemann-sign benchmark (Step 1, Route 1) |
| Center I/3 is Einstein with NEGATIVE Ricci | Ricci proportional to g, Lambda < 0 | Cartan; Totaro Example | Sanity check on the center curvature |
| Single-copy F_4 orbit on h_3(O): orbit 24 / Spin(8) stabilizer 28 | dims 24 / 28 / trdeg 3 | orbit_dimension_gate.py (ALL_PASS); Garibaldi-Guralnick arXiv:2308.08214 | CALIBRATION anchor — reproduce FIRST |
| det_3 SSOT, F_4-invariant | cross `2Re((x2 x1) x3)`; CH norm + 324/324 | ring_lemma_verification / bulk_geometry_verification (CERTIFIED) | The det for every Hessian; reuse, do not re-derive |
| Hess(-log det)\|_{I/3} on {x1,x2,x3,x10} = diag(9,9,18,18), det 26244 | exact | Phase 70 (CERTIFIED) | Center metric; off-center expansion starts here |
| Slice det form = beta*gamma/3 - p^2/3 - q^2/3 (Minkowski) | exact | Phase 70 (CERTIFIED) | Index-map anchor; the slice IS {17,18,19,26} |
| Construction-(ii) bridge reduces to EXACT Minkowski at (M=0, center) | residual 0, sig (1,3) | Phase 70 (CERTIFIED) | The FIXED bridge; do not re-derive |
| e_6 = f_4 (+) L(h_3(O)_traceless), dim 78 | 52 + 26 = 78 | Baez; standard Koecher-Tits | Route 2 e_6 build; assemble from primitives |

**Key insight:** The bulk geometry is COMPLETELY pinned by classical theorems — re-deriving the cone metric, the symmetric-space structure, or the Totaro formula wastes context budget and risks introducing errors. The ONLY genuinely novel computation is the INDUCED metric/curvature on the V_0 Peirce sub-slice with E_11 fixed (unaddressed in the literature — see Novelty). Spend effort there, cite everything else.

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
| ------ | ----------------- | ------ | ---------- |
| `cone_hessian_at_center()` | the restricted cone-Hessian at I/3 (the off-center expansion starting point) | engine | extend by changing the substitution |
| `slice_det_form()` | the index-map gate (confirms the 4 slice coords) | engine | exact over Q |
| `infinitesimal_action(grad_at, M, v)`, `single_copy_orbit_rank(derivs, v27)` | the orbit-tangent rank machinery for Route 2 | orbit_dimension_gate.py | reuse verbatim for Stab generators |
| `exact_qq_rank(A)` (DomainMatrix over QQ) | fast exact rank for large matrices (where Matrix.rank stalls) | orbit_dimension_gate.py | use for the 78-dim / large stacks |
| `_is_genuinely_octonionic_integer(v27)` | validates a generic basepoint (>= 2 imaginary comps, distinct diag) | orbit_dimension_gate.py | use for basepoint sampling |
| `jordan_L_matrix(A, basis)`, `inner_derivations()`, `_standard_basis_27()` | primitives to assemble e_6 | engine | f_4 + L(traceless) |
| `P(X) = 2 L(X)^2 - L(X^2)` | inverse metric symbolically (avoids `g.inv()` blowup) | McCrimmon; build from `jordan_L_matrix` | optional mitigation for the inverse |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| ------------ | ------- | ---- | --------- | --------------- |
| The Curvature of a Hessian Metric (arXiv:math/0401381) | Totaro | 2004 | THE curvature engine | R_ijkl closed form; H^3 const curvature; E_{6(-26)}/F_4 example |
| Analysis on Symmetric Cones (OUP) | Faraut, Koranyi | 1994 | the cone metric + inverse | g_X = Hess(-log det); g^{pq}=P(X); symmetric-space structure |
| Totally geodesic submanifolds of exceptional symmetric spaces (arXiv:2202.10775) | Kollross, Rodriguez-Vazquez | 2022/23 | the totally-geodesic anchor (CALC-02) | Table 7 maximal classification for E_{6(-26)}/F_4; V_0 slice ABSENT (leans GREENLIGHT) |
| F_4 generic orbit on 26 (arXiv:2308.08214) | Garibaldi, Guralnick | 2023 | the calibration anchor | orbit 24 / Spin(8) 28 |
| Semi-Riemannian Geometry | O'Neill | 1983 | Gauss equation / II | R^slice = R^ambient + II-terms; totally-geodesic <=> II=0 |
| The Octonions (arXiv:math/0105155) | Baez | 2002 | group facts | E_6 = Stab(det); SL(2,O) ~ Spin(9,1); e_6 dim 78 |
| A Taste of Jordan Algebras | McCrimmon | 2004 | Peirce + P(X) | P(X) = 2L(X)^2 - L(X^2) |

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
| ---- | -------------- | ------- | ------------ |
| SymPy | 1.14.0 (Rational, Matrix, diff, simplify, cancel) | exact-over-Q symbolic algebra, Hessian, curvature, ranks | The project's locked exact engine; rank via `Matrix.rank()` |
| SymPy DomainMatrix | `sympy.polys.matrices`, `convert_to(QQ).rank()` | fast EXACT rank for large/wide matrices (where dense Matrix.rank stalls) | Used in orbit_dimension_gate for the 52x54 pair; needed for the 78-dim e_6 stacks |
| Python | 3.14.2 | runtime | project stack |
| code/bulk_geometry_verification.py | the certified engine | det_3 SSOT, slice metric, bridge; EXTEND for off-center + curvature | Phase 70 CERTIFIED; SSOT |
| code/orbit_dimension_gate.py | the orbit engine | Route 2 / CALC-01 (reuse the rank machinery) | warm, ALL_PASS, reproduces the anchor |

### Supporting Tools

| Tool | Purpose | When to Use |
| ---- | ------- | ----------- |
| NumPy 2.4.2 (eigvalsh) | labeled INFORMATIONAL eigenvalue triage only | NEVER on a decisive verdict; positive-definiteness readout only |
| mpmath 1.3.0 | guarded high-precision fallback | dim-10 V_0 only if ever needed; NEVER on the homogeneity KILL or a "=0?" |
| sympy.diffgeom | one-point cross-check of curvature on the dim-4 slice | reinforcement only (hand-rolled Totaro is decisive; diffgeom Ricci timed out) |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
| ---------- | --------- | -------- |
| `sympy.Matrix.rank()` | `numpy.linalg.matrix_rank` | FORBIDDEN — rank is discontinuous; SVD tolerance fabricates the verdict |
| hand-rolled Totaro curvature | `sympy.diffgeom` Riemann/Ricci | diffgeom is ~5x slower and Ricci timed out; use only as a 1-point cross-check |
| symbolic `g.inv()` | `g^{pq} = P(X)` (quadratic rep) OR matter-rational-then-invert | symbolic inverse with all symbols TIMES OUT (>200s, measured) |
| Sage/GAP/Singular/Magma | — | EXCLUDED; not installed, not needed (everything is over Q in SymPy) |

### Computational Feasibility

| Computation | Estimated Cost | Bottleneck | Mitigation |
| ----------- | -------------- | ---------- | ---------- |
| Off-center Hessian on dim-4 slice (matter rational) | < 1 s | none | trivial |
| Full Christoffel + Riemann on dim-4 slice (matter rational) | ~19 s (measured) | symbolic simplify per entry | matter-rational; `cancel` per entry; print progress |
| Symbolic `g.inv()` with matter+coords ALL symbolic | TIMES OUT >200 s | dense symbolic inverse | DO NOT — use P(X) or substitute matter first |
| dim-10 V_0 symbolic curvature | TIMES OUT | symbolic inverse on 10x10 | OFF the critical path; dim-4 slice is decisive; mpmath fallback only |
| e_6 dim verification (span rank of 78 over Q) | seconds | exact rank | DomainMatrix over QQ |
| Stab_{E_6}(E_11) kernel (78 x 27 over Q) | seconds | exact nullspace | DomainMatrix over QQ |
| Single-copy anchor reproduction | ~20-110 s per point (measured) | exact 52x27 rank | already in the gate; run as-is |
| Second fundamental form II on dim-4 slice | seconds-minutes | symbolic projection | restrict to h_2(C_u); rational basepoint |

**Executor watchdog caveat (from MEMORY):** the gpd-executor stream-watchdog kills long no-output symbolic runs (~150s harness, hard kill 600s); background resume has stalled. **Long curvature runs MUST print progress between heavy steps and run foreground `python -u`; keep each decisive step under ~150s silent compute** (the matter-rational + hand-rolled + `cancel`-per-entry recipe stays well inside this). If a step risks exceeding this, split it or evaluate at a rational basepoint instead of fully symbolic x.

**Installation / Setup:**
```bash
# No new packages needed — the locked stack is already present.
# Verify (do not install silently):
python3 -c "import sympy; print(sympy.__version__)"   # expect 1.14.0
# diffgeom is part of sympy (cross-check only):
python3 -c "from sympy.diffgeom import Manifold; print('ok')"
```

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| ----- | ----------------- | -------------- | --------------- |
| Single-copy anchor reproduction | the orbit/stabilizer builder is correct BEFORE trusting the E_11 count | run `check_single_copy_orbit_dim` | orbit 24 / Spin(8) 28 / trdeg 3 |
| e_6 dimension | the assembled Lie algebra is genuinely E_6 | span rank over Q of f_4 + L(traceless) | 78 |
| Two-route agreement | the verdict is robust | Route 1 (curvature) vs Route 2 (stabilizer) | SAME verdict (both KILL or both SURVIVES) |
| Riemannian-vs-Lorentzian agreement | no Wick/coordinate artifact | x-variation verdict in the Riemannian restriction vs the Lorentzian bridge | SAME; disagreement => return to Phase 70 |
| Center Hessian regression | the off-center code reduces correctly | set basepoint -> I/3 in the new code | diag(9,9,18,18), det 26244 |
| Engine ALL_PASS preserved | no regression in the SSOT | run `python3 code/bulk_geometry_verification.py` | ALL_PASS, exit 0 |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| ----- | ---------------- | ------------ | ------ |
| M=0 det=1 sub-slice = H^3 | matter -> 0, on det=1 | constant sectional curvature -1 (= -d^2/4, d=2) | Totaro Cor. 2.3; ref-52-kkt |
| Center curvature | basepoint -> I/3 | Einstein, NEGATIVE Ricci (Lambda < 0) | Cartan; Totaro |
| Construction-(ii) at (M=0, center) | basepoint = I/3, M=0 | g = eta exactly, residual 0, sig (1,3) | Phase 70 (CERTIFIED) |
| Single-copy F_4 orbit | generic single-copy point | orbit 24 / stabilizer Spin(8) 28 | orbit_dimension_gate.py; Garibaldi-Guralnick |

### Numerical Validation

| Test | Method | Tolerance | Reference Value |
| ---- | ------ | --------- | --------------- |
| H^3 sectional curvature | hand-rolled Totaro on cone-Hessian, exact over Q | EXACT (= 0 residual) | -1 |
| Ricci scalar of H^3 (standard metric reinforcement) | hand-rolled Riemann | EXACT | R = -6, K = -1 |
| Positive-definiteness of bulk Hessian | eigvalsh (INFORMATIONAL only) | float OK (not a verdict) | all eigenvalues > 0 |

### Red Flags During Computation

- **Route 1 and Route 2 disagree** (curvature says SURVIVES but stabilizer is transitive, or vice versa) => neither verdict is trustworthy; localize the error before reporting.
- **Riemannian restriction and Lorentzian bridge give different x-variation verdicts** => a coordinate/Wick artifact; return to Phase 70.
- **Single-copy anchor (orbit 24 / Spin(8) 28) does NOT reproduce** => the orbit/stabilizer builder is broken; re-calibrate before trusting the E_11 count.
- **H^3 benchmark does NOT come out -1** => the Riemann sign convention or the cone-Hessian slice metric is wrong; fix before any verdict.
- **A "position-dependent" result that only appears when expanding in x (not rho_J)** => fp-coordinate-curvature; you expanded in the wrong variable.
- **A curvature invariant with a nonzero imaginary part** => an octonion cross-term association error has corrupted the Hessian (Pitfall 2); check det_3 provenance.
- **det(metric) = 0 at the basepoint** => degenerate (likely on the light cone for the Lorentzian slice); choose a generic timelike/spacelike basepoint.

## Common Pitfalls

### Pitfall 1: The Homogeneity Trap (THE phase, DECISIVE)

**What goes wrong:** Three deadly errors. (a) False KILL by over-symmetrizing: "the cone is a homogeneous symmetric space, so the slice is too" — WRONG, fixing E_11 BREAKS transitivity to Stab_{E_6}(E_11). (b) False KILL by gauging away real variation with a group element NOT in the residual stabilizer. (c) False GREENLIGHT by reading varying metric COMPONENTS (a coordinate artifact) as physical curvature.
**Why it happens:** every Riemannian symmetric space has parallel Riemann (grad R = 0) and constant scalar curvature — so the AMBIENT curvature is the same number everywhere, and it is tempting to conclude the slice is the same.
**How to avoid:** decide via curvature SCALAR INVARIANTS (R(x), K(x), their d_x; check parallel-Riemann) as functions of the BASEPOINT, PLUS the honest dim-Stab-orbit-vs-basepoint-family count — both exact over Q, both at >= 2 distinct basepoints. Never from components, never from one basepoint.
**Warning signs:** a verdict that rests on metric components; a verdict from a single basepoint; using a general E_6 element rather than a Stab_{E_6}(E_11) element.
**Recovery:** recompute the invariants at >= 2 distinct generic basepoints; confirm the stabilizer route agrees.

### Pitfall 2: Octonion cross-term associativity (prerequisite)

**What goes wrong:** `Re((x1 x2) x3) != Re(x1 (x2 x3))` for genuine octonions; a wrong association returns a plausible number and silently corrupts every Hessian and curvature (the error is AMPLIFIED by differentiation).
**Why it happens:** octonion non-associativity; a "verification" on diagonal/quaternionic (e_0..e_3) data is vacuous.
**How to avoid:** single source of truth (engine `det_3`, byte-identical to ring_lemma, CERTIFIED); never import octonion_algebra.py; sample genuinely octonionic basepoints (`_is_genuinely_octonionic_integer`, >= 2 imaginary components).
**Warning signs:** a curvature invariant with a nonzero imaginary part; a verdict that changes if you swap association order.
**Recovery:** rebuild on the SSOT det_3; re-run the engine ALL_PASS.

### Pitfall 3: Coordinate / Wick artifact (load-bearing through C)

**What goes wrong:** mistaking a coordinate artifact for genuine position-dependence; or the Riemannian-restriction and Lorentzian-bridge verdicts disagreeing because of a Wick/coordinate inconsistency.
**Why it happens:** the construction-(ii) bridge maps a Riemannian cone-Hessian to a Lorentzian slice; if curvature is computed inconsistently across the two pictures a spurious difference appears.
**How to avoid:** compute curvature in the FINAL Lorentzian metric (never "rotate the answer"); CROSS-CHECK that the x-variation verdict agrees between the Riemannian restriction and the Lorentzian bridge.
**Warning signs:** the two pictures give different verdicts.
**Recovery:** return to Phase 70 (the disagreement localizes a coordinate/Wick artifact in the bridge).

### Pitfall 4: Slice-vs-bulk / Gauss equation (feeds the verdict)

**What goes wrong:** assuming R^slice = R^bulk|_slice. It does NOT, in general: R^slice = R^ambient|_slice + II-terms (Gauss). If the slice is totally geodesic (II = 0), R^slice = ambient constant => KILL; if II != 0, the slice can be inhomogeneous even though the bulk is homogeneous.
**Why it happens:** the extrinsic curvature (II) is easy to forget.
**How to avoid:** compute II directly (CALC-02); the verdict must rest on INTRINSIC slice invariants, with the II = 0 test as the cheap KILL shortcut.
**Warning signs:** a verdict that assumes the slice inherits the bulk curvature.
**Recovery:** compute the second fundamental form; check against the Kollross-Rodriguez-Vazquez Table 7 inference.

### Pitfall 5: Float catastrophic cancellation (decisive arithmetic)

**What goes wrong:** curvature is `dGamma + GammaGamma` and rank involves derivative cancellations — float tolerance fabricates both.
**Why it happens:** finite-precision cancellation in quantities that should be exact rationals.
**How to avoid:** EXACT over Q on every decisive verdict; `sympy.Matrix.rank()` / DomainMatrix-over-QQ for ranks, never numpy float rank; sympy exact for curvature.
**Warning signs:** a curvature/rank value that depends on a tolerance.
**Recovery:** redo exact over Q.

## Level of Rigor

**Required for this phase:** exact symbolic computation over Q (a "computer-algebra proof" — not a formal pen-and-paper proof, not a numerical estimate).

**Justification:** the verdict is a yes/no on equality of curvature invariants and on rank/transitivity. Both involve cancellations that float cannot be trusted with. The result is decisive (KILLs or greenlights an entire program), so it must be exact and reproduced by two independent routes.

**What this means concretely:**
- All curvature invariants (R, K), all d_x, all ranks computed EXACTLY over Q (sympy.Rational/Matrix, DomainMatrix-over-QQ).
- The verdict rests on >= 2 distinct generic basepoints, never one.
- The two routes (curvature invariants AND stabilizer transitivity) must AGREE; the agreement is part of the pass condition.
- The single-copy calibration anchor (orbit 24 / Spin(8) 28) and the H^3 = -1 benchmark are reproduced FIRST.
- Float appears ONLY as explicitly-labeled non-decisive triage (eigenvalue positivity readouts).
- A homogeneous result is reported as a clean KILL with an explicit "route dead" statement and STOP — no softening, no relabeling.

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| ------------ | ---------------- | ------------ | ------ |
| `sympy.diffgeom` for curvature | hand-rolled Totaro closed form (3rd derivatives only) | this project (measured) | ~5x faster, no Ricci timeout; the decisive engine |
| symbolic `g.inv()` | `g^{pq} = P(X)` (quadratic rep) or matter-rational-then-invert | this project (measured) | avoids the >200s inverse blowup |
| numpy float rank | exact `sympy.Matrix.rank()` / DomainMatrix-over-QQ | project convention | rank is discontinuous; float fabricates the verdict |
| looked-up Stab_{E_6}(E_11) | direct kernel `{D in e_6 : D.E_11 = 0}` over Q | this phase | the exact non-compact stabilizer is not cleanly tabulated |

**Superseded approaches to avoid:**
- octonion_algebra.py det_3: buggy `(x1 x2) x3` order, float-only, 0.67 associator gap; BANNED on the decisive path.
- Riemannian-Fisher metric sign convention (v16.0): RETIRED (belonged to the abandoned lattice route).
- Wick-rotate-via-u (construction (i)): REJECTED (unproven C*-bottleneck conjecture; Visser chart-dependence).

## Open Questions

1. **Is h_munu(x) genuinely x-dependent after fixing E_11? (THE verdict)**
   - What we know: the bulk is homogeneous; the V_0 slice is ABSENT from the Table-7 maximal totally-geodesic list (leans GREENLIGHT/SURVIVES).
   - What's unclear: absence-from-the-maximal-list is an inference; the slice could sit inside a larger geodesic submanifold (F_4(-20)/Spin(9) or Sp(1,3)/...).
   - Impact: this IS the phase verdict.
   - Recommendation: compute it — Route 1 (curvature invariants at >= 2 basepoints) + Route 2 (stabilizer transitivity) + CALC-02 (II = 0?), all exact over Q, all cross-checked.

2. **Is the V_0 slice totally geodesic (II = 0)?**
   - What we know: Table 7 says probably not.
   - What's unclear: must be computed directly, and V_0-not-inside-a-larger-geodesic-submanifold ruled out.
   - Impact: II = 0 => bulk-constant curvature => KILL (a cheap shortcut to the verdict).
   - Recommendation: compute the second fundamental form (CALC-02); if II != 0, that is independent evidence for SURVIVES (via Gauss).

3. **Does the cone-Hessian slice curvature reproduce H^3 = -1?**
   - What we know: Phase 70 reproduced R=-6, K=-1 on the STANDARD H^3 metric; the cone-Hessian slice computation was deferred to this phase.
   - What's unclear: whether the actual cone-Hessian metric on the det=1 sub-slice gives -1.
   - Impact: pins the Riemann sign before any verdict; a failed benchmark invalidates Route 1.
   - Recommendation: compute it FIRST (Step 1 of Route 1).

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| ------------- | ---------- | --------- | ----------------- |
| dim-4 symbolic curvature at symbolic x | symbolic blow-up / watchdog kill | evaluate R, K at >= 2 distinct RATIONAL basepoints (still exact, still decisive) | low — rational evaluation is the recommended default anyway |
| symbolic `g.inv()` | times out >200s | `g^{pq} = P(X)` (quadratic rep) OR matter-rational-then-invert | low — both measured to work |
| dim-10 V_0 exact curvature | symbolic inverse times out | restrict to the dim-4 h_2(C_u) sub-slice (the decisive arena); mpmath fallback ONLY if dim-10 is ever truly needed | low — dim-4 is the decisive arena by design |
| Route 1 curvature is ambiguous | sign/Wick subtlety | lean on Route 2 (stabilizer transitivity — purely algebraic, immune to sign issues) + CALC-02 (II) | low — Route 2 is mandatory anyway |
| Stab_{E_6}(E_11) orbit non-generic | non-generic basepoint underestimates the orbit | sample >= 2 generic integer octonionic points, take MAX (rank lower-semicontinuous) | low — already the gate's pattern |

**Decision criteria:** Default to RATIONAL-basepoint evaluation (not fully symbolic x) from the start — it is exact, decisive, and avoids the blow-up/watchdog risk. Use the dim-4 sub-slice as the decisive arena. If Route 1 and Route 2 disagree, STOP and localize the error rather than reporting a verdict. If the Riemannian and Lorentzian pictures disagree, return to Phase 70.

## Suggested Plan Decomposition (for the planner)

The roadmap suggests 2 plans; the research supports this split, with CALC-02 (II) as a cheap independent shortcut that can live in either plan:

**Plan 71-01 — Route 1 (curvature invariants): the primary KILL verdict [DERV-01, VALD-01]**
- Build the off-center slice metric g_munu(x) on the dim-4 h_2(C_u) sub-slice by extending `cone_hessian_at_center()` (replace `_center_subs()` with a generic-basepoint substitution).
- Benchmark the Riemann sign on H^3 (cone-Hessian slice, M=0, det=1) => constant curvature -1 FIRST.
- Compute R(x), K(x) via hand-rolled Totaro closed form, exact over Q; evaluate at >= 2 distinct generic rational basepoints; compare; check d_x and parallel-Riemann.
- Verdict: invariants differ => SURVIVES; equal => KILL. Report without softening.
- Atomic, verifiable: the verdict is an exact-over-Q equality/inequality of scalars at distinct basepoints.

**Plan 71-02 — Route 2 (stabilizer transitivity) + CALC-02 (totally geodesic): the cross-check [CALC-01, CALC-02, VALD-01]**
- Reproduce the single-copy anchor (orbit 24 / Spin(8) 28) FIRST (calibration).
- Build e_6 = f_4 (+) L(traceless) (78-dim); verify dim 78 over Q.
- Compute dim Stab_{E_6}(E_11) = ker{D -> D.E_11} and the (basepoint, slice)-family dimension modulo it, exact ranks over Q.
- Compute the second fundamental form II of V_0 (II = 0 => totally geodesic => KILL); rule out V_0 inside a larger Table-7 geodesic submanifold.
- Cross-check the stabilizer verdict AND the II verdict against Plan 71-01's curvature verdict (must AGREE).
- Atomic, verifiable: exact-over-Q dimension counts + the agreement check.

**Instrumenting the verdict against the three forbidden proxies (must be designed in):**
- vs **fp-relabel-homogeneous:** the pass condition is a DECISIVE verdict either way; the KILL branch emits an explicit "Phase A homogeneous — route dead. STOP." string and the milestone halts. No "approximately position-dependent" language is permitted.
- vs **fp-coordinate-curvature:** the verdict reads ONLY curvature SCALAR INVARIANTS (R, K), never metric components; the expansion is in rho_J(X_bg), never the spacetime coordinate x. Add an explicit assert that the test quantity is a scalar invariant, not a component.
- vs **fp-float-decisive:** every decisive value is exact over Q (sympy.Rational/Matrix, DomainMatrix-over-QQ); a guard asserts 0 numpy float-rank calls and 0 float curvature on the decisive path; float appears only as labeled triage.

## Sources

### Primary (HIGH confidence)
- **Totaro, B., "The Curvature of a Hessian Metric," Int. J. Math. 15 (2004) 369-391; arXiv:math/0401381** — R_ijkl closed form (3rd derivatives only); H^3 const curvature -d^2/4; E_{6(-26)}/F_4 example. [peer-reviewed, confirmed; formula read locally by project scout]
- **Faraut, J. & Koranyi, A., *Analysis on Symmetric Cones*, OUP 1994** — g_X = Hess(-log det); g^{pq}=P(X); symmetric-space structure of the det=1 hypersurface. [canonical reference, confirmed]
- **Kollross, A. & Rodriguez-Vazquez, A., "Totally geodesic submanifolds in exceptional symmetric spaces," Adv. Math. (2023); arXiv:2202.10775** — Table 7 maximal totally-geodesic classification for E_{6(-26)}/F_4; V_0 slice absent. [peer-reviewed, confirmed; Table 7 read locally by project scout. NOTE: my WebFetch of the abstract page did NOT return the table contents — the Table 7 entries are taken from the project SUMMARY's local read, MEDIUM-HIGH confidence on the inference.]
- **Garibaldi, S. & Guralnick, R., arXiv:2308.08214** — F_4 generic orbit 24 / Spin(8) stabilizer 28 (the calibration anchor). [confirmed; in-repo validated by orbit_dimension_gate.py]
- **In-repo code/bulk_geometry_verification.py (Phase 70 CERTIFIED)** — det_3 SSOT, slice metric, construction-(ii) bridge. [VERIFIED 2026-05-30, ALL_PASS]
- **In-repo code/orbit_dimension_gate.py (CERTIFIED)** — exact orbit/stabilizer rank machinery; reproduces orbit 24 / Spin(8) 28. [ALL_PASS]

### Secondary (MEDIUM confidence)
- **O'Neill, B., *Semi-Riemannian Geometry* (1983)** — Gauss equation, second fundamental form, totally-geodesic <=> II = 0. [standard textbook]
- **McCrimmon, K., *A Taste of Jordan Algebras* (2004)** — Peirce decomposition; P(X) = 2L(X)^2 - L(X^2). [standard]
- **Baez, J., "The Octonions," Bull. AMS 39 (2002); arXiv:math/0105155** — E_6 = Stab(det); SL(2,O) ~ Spin(9,1); e_6 dim 78 = f_4 + L(traceless). [confirmed]
- **Derksen, H. & Kemper, G., *Computational Invariant Theory*** — generic orbit dim = rank of infinitesimal action (char 0). [in-repo validated]
- **ncatlab / cp4space (E_6(-26) = SL(3,O), SL(2,O) ~ Spin(9,1))** — corroborating the expected Levi of Stab. [web search, MEDIUM]

### Tertiary (LOW confidence)
- **ref-h3o-tower** ~/repos/blog/research/qualia-fixed-point/h3o_tower.py — present, but the engine det_3 is the SSOT; cross-reference only.
- **Project SUMMARY.md / METHODS.md / PITFALLS.md / COMPUTATIONAL.md (v17.0)** — the synthesized project research; the source of several measured benchmarks (19s dim-4 curvature, >200s inverse cliff, 0.67 associator gap) that are in-repo measurements, UNVERIFIABLE by web but HIGH given the scout ran them.

## Metadata

**Confidence breakdown:**
- Mathematical framework: **HIGH** — the cone metric, Totaro curvature formula, Gauss equation, and orbit-dimension method are all peer-reviewed and pinned; the Phase-70 engine + benchmarks are CERTIFIED.
- Standard approaches: **HIGH** — both routes (curvature invariants, stabilizer transitivity) are standard and warm in-repo; the two-route cross-check is mandated.
- Computational tools: **HIGH** — the stack is locked and measured; the reuse-vs-build decisions are concrete (off-center expansion and e_6 are trivial extensions of existing primitives; orbit machinery reused verbatim).
- Validation strategies: **HIGH** — the single-copy anchor, the H^3 benchmark, the two-route agreement, and the Riemannian-vs-Lorentzian agreement are all concrete, exact-over-Q checks.
- The SCIENTIFIC VERDICT: **uncertain by design** — leans GREENLIGHT (V_0 absent from Table 7), but this is an inference the phase must compute; a homogeneous KILL is an acceptable, valuable full result.

**Research date:** 2026-05-30
**Valid until:** the physics/math is stable (peer-reviewed theorems); tool versions (SymPy 1.14.0) change faster but the exact-over-Q methods are version-robust.

## Caveats and Alternatives (pre-submission self-critique)

1. **What assumption might be wrong?** That the dim-4 h_2(C_u) sub-slice is sufficient to decide homogeneity of the full V_0. It is the decisive arena by design (the dim-10 inverse times out), and the project SUMMARY endorses it, but a pathological case where the dim-4 sub-slice is homogeneous while the full dim-10 V_0 is not cannot be fully excluded by the dim-4 computation alone. MITIGATION: Route 2 (stabilizer transitivity) operates on the FULL (basepoint, slice) family, not just the dim-4 sub-slice, so the two-route cross-check covers this gap. The planner should ensure Route 2 uses the full V_0 family, not just h_2(C_u).
2. **What alternative did I dismiss too quickly?** Construction (i) (Wick-via-u) — but it was explicitly REJECTED and LOCKED in Phase 70 (CONVENTIONS.md), so re-opening it is out of scope; it remains the documented fallback only if construction (ii) fails the matter-coupling test in Phase B (not this phase).
3. **What limitation am I understating?** The Table-7 inference (V_0 absent => non-geodesic => GREENLIGHT) is exactly that — an inference. My WebFetch of arXiv:2202.10775 returned only the abstract, NOT the table; the Table-7 entries are from the project scout's local read. The CALC-02 direct II computation is what makes this decisive, not the literature inference. I have flagged this as MEDIUM-HIGH, not HIGH, and routed the decisive content to the II computation.
4. **Simpler method overlooked?** The second-fundamental-form II = 0 test is the SIMPLEST potential KILL (if II = 0, you are done — KILL — without computing any curvature invariant). I have surfaced it as the cheap shortcut (CALC-02), but the curvature-invariant route (Route 1) is still needed for the SURVIVES branch (II != 0 is consistent with, but does not by itself prove, position-dependent invariants — though via Gauss it is strong evidence).
5. **Would a specialist disagree?** A symmetric-space geometer might argue that one should compute the curvature of the FULL 10-dim V_0 = h_2(O) slice (SO(9,1)/SO(9)-type) and its II directly, rather than the dim-4 sub-slice, since the homogeneity question is really about the 10-dim slice. This is correct in principle; the dim-4 reduction is a computational tractability choice (the dim-10 symbolic inverse times out). The Route-2 stabilizer count and the II computation (which can be done on the full V_0 algebraically, not just the dim-4 sub-slice) address the full slice, so the verdict is not solely a dim-4 artifact. The planner should make the II / stabilizer computations operate on the full V_0 where feasible, reserving the dim-4 restriction for the (otherwise intractable) symbolic curvature invariants.
