# Research Summary: Gravity as Intrinsic Curvature of the h_3(O) Bulk Geometry (v17.0)

**Project:** Experiential Measure on Structure Space — Milestone v17.0
**Domain:** Mathematical physics — Riemannian/Lorentzian geometry of the symmetric cone of the exceptional Jordan algebra h_3(O); Hessian-metric curvature of the cubic norm; exact symbolic computation over Q on octonionic data.
**Researched / synthesized:** 2026-05-30
**Confidence:** HIGH on the curvature engine and the homogeneity-test machinery (both pinned to peer-reviewed sources AND a working, certified in-repo implementation); MEDIUM on the Phase-A verdict (leans GREENLIGHT but is an inference that MUST be computed) and on the signature bridge (a modeling choice this milestone must FIX, not discover).

> **Milestone shape (read first).** v17.0 is a **gated KILL test**, not an open-ended exploration. The claim: the positive cone of h_3(O) is an intrinsically-curved Riemannian symmetric space with canonical metric `g_X = Hess(-log det X)`; a primitive idempotent E_11 picks the spacetime slice `V_0 superset h_2(C_u) ~ R^{3,1}`, an off-center state picks a basepoint, and gravity is the curvature the slice inherits from the bulk, sourced by matter `M in V_1/V_{1/2}` via the cubic-norm cross-terms. **NO lattice, NO posited supergravity Lagrangian, NO SUSY, NO observers-make-gravity ensemble argument.** Phase A (homogeneity) is a cheap KILL gate run FIRST: a homogeneous result is a clean, valuable KILL and the project stops. Phases B (matter-sourcing) and C (Einstein structure) run only if A greenlights.

---

## Unified Notation

This table is binding for all downstream phases. All four research files were notation-coherent already (they share the in-repo engine's coordinate layout); the only genuine conflicts are the **three det conventions** (resolved in favor of the engine — see Key Finding M2) and the **two signature constructions** (resolved in favor of (ii) — see Key Finding M3).

| Symbol | Quantity | Convention / value | Notes |
|---|---|---|---|
| `h_3(O)` | Exceptional Jordan (Albert) algebra | 27-dim, 3x3 octonion-Hermitian matrices | The "bulk" carrier space |
| `det(X)`, `N(X)` | Cubic norm (Freudenthal det) | `abg - a||x1||^2 - b||x2||^2 - g||x3||^2 + 2 Re((x2 x1) x3)` | **Cross-term order is load-bearing** (octonion non-associativity). USE the engine's `det_3`. |
| `g_X` | Canonical cone metric | `g_X(A,B) = -d_s d_t log det(X+sA+tB)|_0 = Hess(-log det)` | Faraut-Koranyi characteristic-function metric; positive-definite (Riemannian) on the open cone |
| `g^{pq}` | Inverse metric | `= P(X)` in coordinates (quadratic representation) | Faraut-Koranyi: `g_X(A,B) = (P(X)^{-1}A | B)`; gives `g^{pq}` symbolically without finite-differencing |
| `f_ijk`, `C_ijk` | Third-derivative tensor of the potential | `f_ijk = d^3 f/dx_i dx_j dx_k`; `d(X,X,X) = 6 det` | Implemented as `polarize_d`; **det cubic => f_ijkl = 0** |
| `R_ijkl` | Riemann tensor (Totaro) | `R_ijkl = -(1/4) sum_pq g^{pq}(f_jlp f_ikq - f_ilp f_jkq)` | **Depends ONLY on 3rd derivatives.** Cone-normalized variant carries `-1/(4 d^2 (d-1)^2)`, d=3. |
| `E_11` | Primitive idempotent | `diag(1,0,0)` | Fixing it picks the spacetime slice and BREAKS E_6 -> Stab_{E_6}(E_11) |
| `V_0, V_{1/2}, V_1` | Peirce subspaces under E_11 | `V_0` (slice, dim 10), `V_{1/2}`, `V_1` (matter) | Spacetime sub-slice indices `{17,18,19,26}`; internal V_0 `{20..25}` |
| `h_2(C_u)` | Complex sub-slice | `~ R^{3,1}`, u = e_7, `C_u = span{1,e_7}` | The 4-dim physical spacetime slice; det_2 gives Minkowski form |
| `eta_munu` | Background Minkowski metric | mostly-minus, from det of h_2(C_u) (per `52-kkt-spacetime`) | Construction (ii): eta is the slice's OWN det, NOT from the cone Hessian |
| `h_munu(x)` | Position-dependent perturbation | `g_munu(x) = eta_munu + h_munu(x)`; `h(center, M=0) = 0` | The object Phase A tests for genuine x-dependence |
| `E_{6(-26)}/F_4` | The bulk det=1 symmetric space | noncompact type EIV, dim 26, rank 3, K <= 0 | NOT constant-curvature (rank > 1); Einstein with negative Lambda |
| `||M||`, `rho_J(X_bg)` | Matter amplitude / off-center-ness | The physical small parameters | NOT the spacetime coordinate x (which is O(1)) |
| `kappa, Lambda` | Einstein coupling / cosmological constant | fitted in Phase C; **Lambda != 0** (background is Einstein-negative) | Must be FIXED from intrinsic data BEFORE testing G = kappa T + Lambda g |

**Unit / convention summary:** natural units; exact rational arithmetic over **Q** (NOT float) on the decisive path; metric signature **mostly-minus** (Lorentzian slice) with the Riemann/Ricci sign convention to be stated explicitly and benchmarked on H^3. No renormalization scheme (this is exact differential geometry, not QFT).

---

## Executive Summary

This milestone asks a sharp, falsifiable question: does the spacetime Peirce slice `V_0` of the h_3(O) cone inherit a genuinely **position-dependent** metric from the canonical Hessian metric `g_X = Hess(-log det)`, or is the inherited geometry homogeneous (in which case the route to "gravity from intrinsic curvature" is dead)? The research is unusually well-anchored for a novel claim: the **bulk geometry is completely pinned down by classical theorems** (Faraut-Koranyi: the cone is the symmetric space `E_{6(-26)}/F_4 x R+`; Totaro 2004: its Riemann tensor is an explicit closed form in the *third derivatives of the potential only*), and the homogeneity test reduces to a finite, exact, in-repo orbit-dimension computation. The honest prior expectation is **"curved, possibly not Einstein."**

The recommended path is dictated by four cross-cutting findings that every scout reached independently. (1) **The curvature engine already exists**: Totaro's formula `R_ijkl = -(1/4) g^{pq}(f_jlp f_ikq - f_ilp f_jkq)` needs only `f_ijk` (the polarization of det, which terminates because det is cubic) and one matrix inverse `g^{pq} = P(X)` (the Faraut-Koranyi quadratic representation) — so the curvature of Phases B/C is cheap and exact, *not* a `sympy.diffgeom` blowup. (2) **There is a single source of truth for det**: the certified-over-Q `ring_lemma_verification.det_3` (passes Cayley-Hamilton + 324/324 inner-derivation annihilation, i.e. F_4-invariance). There is a **measured 0.67 associator gap** between this and two other in-repo det spellings (the old buggy `octonion_algebra`/`peirce_coupling` float order, and `h3o_tower.py`'s third spelling on a different coordinate labeling) — all det conventions MUST be reconciled on genuinely non-associative (e_4..e_7) data before any geometry. (3) **The signature bridge should be construction (ii)** — background Lorentzian eta from h_2(C_u)'s own det, with the cone-Hessian supplying only the perturbation `h_munu` — because it is the only construction that reduces to EXACT Minkowski at `(M=0, center)` without smuggling in a second unproven conjecture (the Wick-rotation-via-u signature flip). (4) **Phase A leans GREENLIGHT but must be computed**: the maximal totally-geodesic submanifolds of `E_{6(-26)}/F_4` are completely classified (Kollross-Rodriguez-Vazquez 2022), and the V_0 spacetime slice (`SO(9,1)/SO(9)`) does NOT appear — strong evidence the slice is non-totally-geodesic (nonzero second fundamental form -> position-dependent), but absence-from-the-maximal-list is an *inference*, not a theorem.

The principal risks are all **self-deception at the Phase-A gate**, and the PITFALLS scout maps them precisely: a false KILL (mistaking the *bulk's* homogeneity for a slice property, or gauging away real variation with a group element not in `Stab_{E_6}(E_11)`), a false GREENLIGHT (reading varying metric *components* — or a Wick-rotation artifact, or the background's off-center-ness — as physical curvature), and in Phase C a **circularity trap**: because the slice geometry genuinely coincides with GST special-real geometry, reaching for any GST/SUSY/`-1/2 R`/Weinberg formula silently re-imports the assumed Einstein structure. Mitigations are concrete and non-negotiable: decide KILL/survive on **coordinate-invariant curvature scalars as functions of x** (plus an exact stabilizer-orbit-dimension count), never on metric components or a single basepoint; work **exact over Q** (float curvature is catastrophic-cancellation noise here); enforce a **hard input ban** in Phase C and define `T_munu, kappa` from cross-terms BEFORE computing `G_munu`; and test over an `(M, x)` *family*, never one tuned point. The right first implementation step is mechanical: **copy `ring_lemma_verification.py` to `code/bulk_geometry_verification.py` and extend** (do NOT import `octonion_algebra`).

---

## Key Findings

### Methods (from METHODS.md) — HIGH confidence on the two load-bearing methods

**M1 — Curvature via Totaro's closed form is the decisive engine [HIGH].** For any Hessian metric `g_ij = d^2 f/dx_i dx_j`, the Riemann tensor is `R_ijkl = -(1/4) sum g^{pq}(f_jlp f_ikq - f_ilp f_jkq)` — a closed expression in derivatives of the potential **to order three only** (no Christoffel-of-the-metric recursion, no fourth derivatives). Because det is cubic, `f_ijkl = 0` and the third-derivative tensor is exactly the polarization `polarize_d` (d(X,X,X)=6 det). The inverse metric `g^{pq}` is the Faraut-Koranyi quadratic representation `P(X)`, available symbolically. **This is the single most important recommendation: do NOT call `sympy.diffgeom` on the 10-dim metric** (n^4 components x heavy octonionic-rational simplify -> blowup). Reserve diffgeom for the 4-dim slice as a cross-check only.

**M2 — det engine is the single source of truth; reconcile all conventions first [HIGH].** Use `ring_lemma_verification.det_3` (cross-term `2 Re((x2 x1) x3)`, certified F_4-invariant). Do NOT use `octonion_algebra.py`'s `det_3` (known-buggy `(x1 x2) x3` order; the engine's `exact_only_guard()` forbids importing it). **DECIDE and FIX which potential — `det` vs `-log det` — at the start**; they give metrics differing by the radial (det=const) direction and must not be mixed. The milestone's potential is `-log det`.

**M3 — Signature bridge: use construction (ii) [MEDIUM — a modeling choice to FIX].** Take `eta_munu` from h_2(C_u)'s own det (proven Minkowski in `52-kkt-spacetime`); let the cone-Hessian restricted to V_0 supply only `h_munu(x) := [g_X on V_0, in h_2(C_u) coords] - [its value at (M=0, center)]`. The tested metric is `g_munu(x) = eta_munu + h_munu(x)`, with `h = 0` at the center by construction. Construction (i) (restrict + Wick-rotate via u=e_7) bundles in a *second, separable* conjecture (the C*-bottleneck signature flip) and has no off-the-shelf machinery landing on exact Minkowski. **Mandatory gate: `g(center, M=0) = eta` exactly.**

**M4 — Homogeneity test reuses certified in-repo machinery [HIGH].** Generic orbit dimension = rank, at a generic point, of the infinitesimal-action matrix (Derksen-Kemper char-0; Garibaldi-Guralnick orbit method). `orbit_dimension_gate.py` already implements this exactly over Q and reproduces the single-copy anchor (orbit 24 / Spin(8) stabilizer 28). Phase A is the SAME computation with the e_6 generators that fix E_11. **The verdict logic: if `Stab_{E_6}(E_11)` acts transitively on the basepoint family (rank = dim family) -> every basepoint isometric -> h_munu x-independent -> KILL; if the orbit is a proper subset -> genuinely inequivalent basepoints -> h_munu varies -> proceed to B.**

**M5 — Perturbative organization and the Einstein test [HIGH/MEDIUM].** Expand around the F_4-symmetric center X=I/3 in powers of ||M|| and rho_J; det being cubic, the jet TERMINATES. Gauss-Codazzi separates the slice's *intrinsic* (Gauss) curvature from the *extrinsic* second-fundamental-form term. The Einstein test (Phase C) solves the overdetermined linear system `G_munu = kappa T_munu + Lambda g_munu` for the two scalars exactly / linear-in-M / not at all; "curved but not Einstein" is an accepted, well-defined outcome.

### Prior Work Landscape (from PRIOR-WORK.md) — HIGH on the math, HIGH on the novelty flag

**Must reproduce (validation anchors / benchmarks):**
- **The cone is `E_{6(-26)}/F_4 x R+`** with `g_X = Hess(-log det)` — Faraut-Koranyi 1994, Totaro 2004. The center X=I/3 is an irreducible Riemannian symmetric space -> **Einstein with negative Ricci** (Cartan). [HIGH]
- **h_2(C_u) sub-slice det=1 hyperboloid = `H^3 = SL(2,C)/SU(2) = SO(3,1)/SO(3)`, constant negative curvature `-d^2/4 = -1` (d=2, rank-1)** — Totaro Cor. 2.3 + `52-kkt-spacetime`. The M=0 H^3 limit MUST reproduce this. [HIGH]
- **h_2(O) det=1 = `SO(9,1)/SO(9)`, rank-1, constant negative curvature.** [HIGH]
- **At (M=0, center, h_2(C_u)) the background = exact Minkowski `eta_munu`** — the A0 signature bridge MUST reduce to this. [HIGH]

**Novel contributions (UNADDRESSED in the literature — this is the milestone's claim to originality):**
- **The induced metric/curvature on a Peirce sub-block of a Jordan-algebra cone is computed by no located reference.** Totaro/Faraut-Koranyi treat the *ambient* cone; Kollross-Rodriguez-Vazquez treat only *totally-geodesic* submanifolds. The V_0-slice-curvature question is genuinely new. [HIGH on the novelty]
- **Matter-sourcing via det cross-terms** (V_0 <-> V_1/V_{1/2}) is likewise unaddressed.
- **Prior octonionic-gravity attempts take the rejected action-based route**: Castro (membrane *action* invariant under E_6 cubic form), Singh (h_2(O)=10D-Minkowski, no slice curvature), Dubois-Violette-Todorov (algebraic dictionary, no gravitational curvature). None preempts the intrinsic-cone-curvature claim. [HIGH]

**Phase-A literature anchor [MEDIUM-HIGH inference]:** Kollross-Rodriguez-Vazquez 2022 (Table 7) classify the maximal totally-geodesic submanifolds of `E_{6(-26)}/F_4`: `Sp(1,3)/Sp(1)xSp(3)` (dim 12), `F_4(-20)/Spin(9)` (dim 16, the octonionic hyperbolic plane = idempotent direction), `SL_3(C)/SU_3` (dim 8), `G_2(C)/G_2` (dim 14). **Neither the V_0 slice `SO(9,1)/SO(9)` nor `H^3` appears** -> likely non-totally-geodesic -> nonzero II -> Gauss-Codazzi curvature != ambient -> plausibly position-dependent. **This leans toward "survives," but must be confirmed**, including ruling out that V_0 sits inside one of the larger geodesic submanifolds.

### Computational Approaches (from COMPUTATIONAL.md) — HIGH on reuse and dim-4 tractability

**C1 — Reuse path is mechanical and measured [HIGH].** Copy `ring_lemma_verification.py` -> `code/bulk_geometry_verification.py` (the project's self-contained-decisive-module pattern); add only slice coordinatization, `g_ij = diff(-log(det_3(X)), coords[i], coords[j])`, hand-rolled Christoffel/Riemann loops (~30 lines textbook), and verification hooks. **Confirmed by running:** the h_2(C_u) slice det is `b*g/3 - p^2/3 - q^2/3` (Minkowski form); `Hess(-log det)` at I/3 = `diag(9,9,18,18)` (nondegenerate, det 26244); full Christoffel+Riemann with matter rational completes in **~19 s** exact over Q.

**C2 — The cost cliff is the symbolic matrix inverse [HIGH, measured].** Metric BUILD and point-EVALUATION are always cheap (dim-4 <0.05 s, dim-10 ~0.25 s). The **symbolic inverse `g.inv()` carrying matter+coords as free symbols TIMES OUT >200 s** (both dim-4/6-symbols and dim-10). **Mitigation (works):** substitute matter to small rationals BEFORE inverting; keep only the 4 slice coords symbolic; for M-dependence, series-expand in a single matter amplitude `t`. **Dim-10 V_0 symbolic curvature is off the critical path** — the decisive physics lives on the 4-dim h_2(C_u) slice.

**C3 — Hand-rolled curvature beats `sympy.diffgeom` here [HIGH].** Measured: hand-rolled Christoffel ~2.9 s vs diffgeom 14.2 s; diffgeom Ricci timed out and is finicky (only the base-vector idiom works). Use diffgeom only as a one-point cross-check (Hook V6).

**C4 — Stack is fixed [HIGH].** SymPy 1.14.0 + NumPy 2.4.2 + mpmath 1.3.0, Python 3.14.2. NO Sage/GAP/Singular/Macaulay2/Magma (excluded; not needed). NumPy/float is a FORBIDDEN PROXY on any rank or "=0?" decision; mpmath only as a guarded fallback where exact times out.

**C5 — Executor watchdog caveat [HIGH, from MEMORY].** The `gpd-executor` stream-watchdog kills long no-output symbolic runs (~150 s harness, hard kill 600 s); background resume has stalled. Long curvature runs must print progress between heavy steps and run foreground `python -u`; keep each decisive step under ~150 s silent compute (the matter-rational + hand-rolled + `cancel`-per-entry recipe stays well inside this).

### Critical Pitfalls (from PITFALLS.md) — HIGH on the four headline traps

1. **THE HOMOGENEITY TRAP (Phase A, DECISIVE) [HIGH].** Every Riemannian symmetric space is homogeneous with `grad R = 0` (parallel Riemann) and constant scalar curvature — so the *bulk* curvature is the same number everywhere. Three deadly errors: false KILL by over-symmetrizing ("the cone is homogeneous so the slice is too" — wrong, fixing E_11 BREAKS transitivity to `Stab_{E_6}(E_11)`); false KILL by gauging away real variation with a group element NOT in the residual stabilizer; false GREENLIGHT by reading varying metric *components* as curvature. **Avoid:** decide via curvature SCALARS (Ricci scalar R(x), Kretschmann, `d_x` of each, check parallel-Riemann) as functions of x, PLUS the honest `dim Stab_{E_6}(E_11)`-orbit vs dim-basepoint-family count. Never from components, never from one basepoint.

2. **OCTONION CROSS-TERM ASSOCIATIVITY (Phase A prerequisite, Phase B critical) [HIGH].** `Re((x1 x2) x3) != Re(x1 (x2 x3))` for genuine octonions; a wrong association returns a plausible number and silently corrupts every Hessian and curvature downstream (the error is *amplified* by differentiation, not averaged). **Avoid:** single source of truth (engine `det_3`); run the association-invariance pre-flight on e_4..e_7 data (must be nonzero, else test is vacuously in an associative subalgebra); Cayley-Hamilton check. A "verification" on diagonal/quaternionic (e_0..e_3) data is vacuous.

3. **SIGNATURE / WICK-ROTATION (Phase A sub-task A0, load-bearing through C) [HIGH].** Naive coordinate Wick rotation `t->-it` on a curved/Hessian metric is coordinate-dependent and manufactures spurious curvature (Visser arXiv:1702.05572); mixing constructions (i) and (ii) double-counts the Minkowski background; a bridge that fails to reduce to exact Minkowski at (M=0, center) contaminates h_munu with a constant offset masquerading as Lambda or position-dependence. **Avoid:** pick ONE bridge (recommend (ii)), enforce the `g(center,M=0)=eta` gate exactly, compute curvature in the *final Lorentzian* metric (never "rotate the answer"), and cross-check that the x-variation verdict agrees between the Riemannian restriction and the Lorentzian bridge (disagreement localizes the artifact).

4. **CIRCULARITY / GST-Weinberg SMUGGLING (Phase C fatal, guards from Phase A) [HIGH].** The slice geometry genuinely coincides with GST special-real geometry, so reaching for any GST/supergravity Lagrangian, the `-1/2 R` coefficient, SUSY multiplet data, Weinberg's soft-graviton theorem, or the equivalence principle as a *premise* silently re-imports the assumed Einstein structure. **Avoid:** hard input ban (declare at Phase A); cite GST for the *manifold identification only* (`E_{6(-26)}/F_4`), never the action; define `T_munu` and `kappa` from V_1/V_{1/2} cross-term content BEFORE computing `G_munu`; report the honest level — "curved but not Einstein" is the most likely real outcome and is a legitimate result.

**Supporting pitfalls:** (5) **Slice-vs-bulk / Gauss equation** — `R^slice != R^bulk|_slice`; if the slice is totally geodesic (II=0), `R^slice` = bulk constant -> KILL, and the totally-geodesic question feeds Phase A directly; verdict must rest on *intrinsic* invariants. (6) **Lambda vs matter-sourcing (Phase B)** — a maximally-symmetric nonzero Riemann is just Lambda, not matter; use the cross-term off-switch (`det -> det(V_1)*det(V_0)`) and ||M||->0 vanishing. (7) **Tuned-point Einstein overclaim (Phase C)** — test over an (M,x) family; linear-in-M is weak, report the honest order. (8) **Float catastrophic cancellation** — curvature is `dGamma + GammaGamma`, a cancellation factory; exact-Q only. (11) **Single-point sampling cannot detect x-dependence** — a constant nonzero curvature is still homogeneous.

---

## Critical Claim Verification

Web verification was performed on the roadmap-driving claims. The two load-bearing external references are confirmed real, peer-reviewed, and on-topic. Engine/repo facts were measured directly by the COMPUTATIONAL scout (run, not assumed) and cannot be web-verified; they are flagged as such.

| # | Claim | Source | Verification | Result |
|---|-------|--------|--------------|--------|
| 1 | Totaro's Hessian-curvature formula depends only on 3rd derivatives; octonionic det -> E6/F4 noncompact | METHODS, PRIOR-WORK | web_search "Totaro curvature Hessian metric"; arXiv:math/0401381 confirmed, peer-reviewed (Int. J. Math. 15, 2004); search corroborates link to "metrised Jordan algebras" + homogeneous-form Hessian curvature. PDF binary to WebFetch (both scouts read it locally via pdftotext and quote the IDENTICAL formula) | CONFIRMED (formula corroborated by cross-scout agreement + topic match; exact constant relies on scouts' local read) |
| 2 | Maximal totally-geodesic submanifolds of E_{6(-26)}/F_4 classified; V_0 slice absent -> likely non-geodesic | PRIOR-WORK | web_search; arXiv:2202.10775 (Kollross-Rodriguez-Vazquez) confirmed, Adv. Math. 2023, peer-reviewed; classification + Dynkin-index method confirmed | CONFIRMED (paper + method); the "V_0 absent => non-geodesic" step is an INFERENCE, flagged for Phase A |
| 3 | `g_X = Hess(-log det)` is the canonical metric of the symmetric cone (Faraut-Koranyi) | all four | web_search; Faraut-Koranyi *Analysis on Symmetric Cones* (OUP 1994) confirmed as the canonical reference; specific P(X) metric-inverse identity is standard Jordan theory (also McCrimmon) | CONFIRMED (reference + standard result) |
| 4 | Three in-repo det conventions disagree by a measured associator gap 0.67 on octonionic data; engine `det_3` certified F_4-invariant (CH + 324/324) | COMPUTATIONAL, METHODS, PITFALLS | repo-measured (COMPUTATIONAL scout ran `ring_lemma_verification.py` -> ALL_PASS, compared dets numerically) | UNVERIFIABLE by web — relies on direct in-repo measurement (HIGH given the scout ran it; consistent across 3 files) |
| 5 | Symbolic `g.inv()` with matter+coords symbolic times out >200 s; matter-rational completes in ~19 s | COMPUTATIONAL | repo-measured (run end-to-end this session) | UNVERIFIABLE by web — relies on direct measurement (HIGH; a measured benchmark) |
| 6 | Naive coordinate Wick rotation on curved metrics is ill-defined / manufactures artifacts | PITFALLS, METHODS | Visser arXiv:1702.05572 is a known result; consistent across two scouts | CONFIRMED (well-established) |
| 7 | h_2(C_u) ~ R^{3,1} with Minkowski signature from det_2 (mostly-minus) | all four | in-repo prior result (`52-kkt-spacetime`, `52-observer-uniqueness`); established in v12.0/v13.0 | CONFIRMED (prior project milestone, internally) |

---

## Approximation Landscape

| Method | Valid regime | Breaks down when | Controlled? | Complements |
|---|---|---|---|---|
| **Totaro closed-form R_ijkl** | Any Hessian metric of a cubic norm; exact over Q | n large (dim-10/26) -> symbolic inverse blowup (>200 s) | YES — exact, finite (det cubic => f_ijkl=0) | diffgeom (4-dim cross-check); mpmath (dim-10 fallback) |
| **Orbit-dim via exact rank over Q (Phase A)** | dim Stab and basepoint family; exact | non-generic basepoint underestimates orbit | YES — exact; sample >=2 generic integer points, max rank | totally-geodesic / Gauss check (Pitfall 5) |
| **Signature bridge (ii): eta + cone-Hessian h_munu** | M=0,center -> exact Minkowski by construction | if restricted g_X is conformal to eta with x-INDEPENDENT factor -> trivial (KILL branch) | Partially — a fixed modeling choice, gated | bridge (i) if (ii) fails the coupling-capture test |
| **Perturbative ||M||, rho_J expansion** | small matter / near-center; jet terminates (det cubic) | expanding in spacetime x (wrong variable, O(1)) | YES — finite polynomial, exact | full symbolic at a fixed rational matter point |
| **Gauss-Codazzi II decomposition** | non-degenerate induced metric (away from light cone) | on the light cone (degenerate induced metric) | YES — exact identity | intrinsic invariants (the actual verdict) |
| **mpmath high-precision** | dim-10 verdict if ever needed | NEVER on the homogeneity KILL test or a "=0?" | NO — guarded fallback only | exact-Q (the decisive path) |
| **Float64 finite-difference** | sanity cross-check only | any KILL/survive or rank verdict (cancellation) | NO — FORBIDDEN on decisive path | exact-Q result it cross-checks |

**Coverage gaps:** (a) **Dim-10 full V_0 symbolic curvature** — no exact method (symbolic inverse times out); not on the critical path (4-dim slice is decisive), mpmath fallback if ever needed. (b) **The induced-Peirce-slice-curvature question itself** has NO prior method in the literature — this is the milestone's novel computational contribution, which is why the in-repo engine must be extended rather than a library reused.

---

## Theoretical Connections

| Connection | Type | Status | Roadmap use |
|---|---|---|---|
| Cone Hessian `Hess(-log det)` <-> det=1 symmetric space `E_{6(-26)}/F_4` (warped product over R+) | Structural (Totaro Lemma 2.4 / Loftin) | **Established** | Pass freely between "cone" and "det=1 hyperboloid" pictures; cone curvature <-> hypersurface curvature |
| Hessian-of-cubic geometry <-> "very special real" / GST scalar manifold geometry | Structural identity | **Established** — AND the central circularity hazard | Cite GST for the *manifold* only; the shared geometry is exactly why the `-1/2 R`/SUSY input ban is mandatory (Pitfall 4) |
| det cross-term `2 Re((x2 x1) x3)` <-> third-derivative tensor `f_ijk` <-> curvature `R ~ g^{pq} f f` | Structural | **Established** (Totaro) | The mechanism: matter enters V_0 curvature ONLY through cross-terms; switch-off test (`det->det(V_1)*det(V_0)`) isolates it |
| C_u ~ C (e_7 -> i) <-> Wick rotation hinge | Duality/analogy | **Conjectured** (the C*-bottleneck signature flip, Phase 46) | The reason to AVOID construction (i): this flip is a *separate* unproven claim |
| h_2(O) det <-> 10D Minkowski; h_2(C_u) det <-> R^{3,1} | Duality (det <-> metric) | **Established** (Dubois-Violette-Todorov; v12/v13) | Supplies the background eta for construction (ii) |
| Generic orbit dimension <-> rank of infinitesimal action (char 0) | Structural (Derksen-Kemper) | **Established** + in-repo validated | The Phase-A homogeneity verdict engine (`orbit_dimension_gate.py`) |
| Slice intrinsic curvature <-> bulk curvature + II^II (Gauss equation) | Structural | **Established** (Gauss-Codazzi) | Separates "slice curved" from "slice flat but embedded curvedly"; totally-geodesic => KILL |

**Cross-validation opportunities:** (1) H^3 sub-slice curvature computable BOTH via the general Totaro formula AND via Totaro Thm 3.1 + Clebsch covariant (R^3 closed form) — agreement validates the engine. (2) Center curvature must be Einstein-negative (Cartan) AND match the general formula. (3) Hand-rolled Riemann vs `sympy.diffgeom` on one rational point. (4) The x-variation verdict must agree between the Riemannian restriction and the Lorentzian bridge.

### Cross-Validation Matrix

|  | Totaro closed-form | diffgeom | Exact/analytical limit | In-repo anchor |
|---|:---:|:---:|:---:|:---:|
| **Totaro closed-form R** | — | one rational point (dim-4) | H^3 const `-1`; center Einstein-neg; H^9 | Cayley-Hamilton det LOCK |
| **Orbit-dim (Phase A)** | — | — | — | single-copy orbit 24 / Spin(8) 28 (MUST reproduce first) |
| **Signature bridge (ii)** | — | — | exact Minkowski eta at (M=0,center) | `52-kkt-spacetime` det_2 |
| **Einstein test (C)** | G_munu from Totaro R | — | Lambda negative at leading order | — |

**Reading:** entry (row X, col Y) = regime where X is checked against Y. The orbit-dim Phase-A row has NO analytical cross-check beyond the single-copy anchor -> reproducing `orbit_dimension_gate.py`'s ALL_PASS before trusting the E_11-stabilizer computation is mandatory (highest-risk-no-independent-check item).

---

## Implications for Roadmap

The milestone is pre-structured as a gated A -> B -> C sequence, and the research strongly endorses this ordering: Phase A is cheap, exact, and decisive (it KILLs or greenlights everything downstream), so it MUST come first. The phase suggestions below are inputs for the roadmapper, to be reconciled with REQUIREMENTS.md objectives.

### Suggested Phase Structure

**Phase 70 / A0 — Engine reconciliation + signature bridge (the prerequisite gate).**
- *Rationale (physics):* every downstream curvature is built from det-derivatives, so a wrong det convention or a contaminated background silently corrupts the whole milestone. Three det conventions disagree by a measured 0.67 associator gap; this must be reconciled on e_4..e_7 data first.
- *Delivers:* `code/bulk_geometry_verification.py` (copy of `ring_lemma_verification.py`, extended); a single certified `det_3`; the fixed signature bridge (ii) with eta from det_2.
- *Methods:* M2 (engine det), M3 (bridge ii). *Builds on:* `ring_lemma_verification.py`, `embedding_under_E_verification.py`, `52-kkt-spacetime`.
- *Pitfalls:* 2 (cross-term association), 3 (signature), 12 (index assignment), 13 (sign convention).
- *Success criteria:* engine ALL_PASS reproduced; association pre-flight nonzero on e_4..e_7; **`g(center, M=0) = eta` EXACTLY** (Hook V2: slice det = `b*g/3 - p^2/3 - q^2/3`, Hess at I/3 = `diag(9,9,18,18)`).
- *Risk:* LOW (mechanical reuse, measured). *Needs research:* NO.

**Phase 71 / A — Homogeneity KILL gate (the dealbreaker).**
- *Rationale (physics):* fixing E_11 breaks E_6 -> `Stab_{E_6}(E_11)`; the route is alive iff that residual group does NOT act transitively on (basepoint, slice) pairs. Cheap, exact, decisive.
- *Delivers:* the homogeneity verdict — KILL (homogeneous) or GREENLIGHT (genuinely position-dependent); `dim Stab_{E_6}(E_11)` and the basepoint-family dimension.
- *Methods:* M4 (orbit-dim via exact rank), M1 (Hessian x-dependence), M5/Gauss (totally-geodesic check). *Builds on:* `orbit_dimension_gate.py`; the Kollross-Rodriguez-Vazquez Table 7 anchor.
- *Pitfalls:* **1 (homogeneity trap — the whole phase IS this pitfall)**, 5 (slice-vs-bulk / totally-geodesic), 10 (off-center-ness vs field), 11 (single-point sampling), 8 (float).
- *Success criteria:* curvature invariants computed as functions of x (exact over Q); `d_x` of each tested for identical-zero; stabilizer-orbit dim vs basepoint-family dim reported explicitly; single-copy anchor (orbit 24 / Spin(8)) reproduced first. **A homogeneous result is a clean KILL — report and STOP, do not soften.**
- *Risk:* MEDIUM (verdict leans GREENLIGHT but is an inference; the trap is self-deception). *Needs research:* the exact non-compact `Stab_{E_6}(E_11)` (a parabolic-type subgroup, Levi expected to contain Spin(9,1)) is not cleanly tabulated -> likely needs `/gpd:research-phase` or direct computation.

**Phase 72 / B — Matter-sourcing (only if A greenlights).**
- *Rationale (physics):* if h_munu varies, the next question is whether matter `M in V_1/V_{1/2}` sources it through the cubic-norm cross-terms (the only channel coupling V_0 to matter).
- *Delivers:* Riemann/Ricci of `g_munu(x)`; M=0 => flat/pure-Lambda baseline; the cross-term ON/OFF isolation; curvature scaling with ||M|| and rho_J.
- *Methods:* M1 (Totaro curvature), M5 (||M|| expansion + Gauss), C2 (matter-rational-then-invert). *Builds on:* Phase A's slice metric.
- *Pitfalls:* 6 (Lambda vs matter-sourcing — decompose Ricci scalar/traceless/Weyl), 5 (extrinsic II vs intrinsic), 9 (rho-module real-only misuse), 8 (float).
- *Success criteria:* curvature VANISHES under the cross-term off-switch (`det -> det(V_1)*det(V_0)`); curvature proportional to ||M|| and vanishes as M->0; **all three off-diagonal slots populated** (else the cubic vertex is vacuously zero — Hook V3). Cross-term-on run ~19 s; on/off ~2x.
- *Risk:* MEDIUM. *Needs research:* possibly (T_munu precursor construction from cross-terms).

**Phase 73 / C — Einstein structure (strong form, only if B shows M-sourcing).**
- *Rationale (physics):* the strongest claim — does `G_munu = kappa T_munu + Lambda g_munu` hold for a `T_munu` built from cross-terms?
- *Delivers:* the honest verdict at exact / linear-in-M / no level.
- *Methods:* M5 (Einstein linear test). *Builds on:* Phase B curvature.
- *Pitfalls:* **4 (circularity — fatal; hard input ban)**, 7 (tuned-point / linear-order overclaim).
- *Success criteria:* `T_munu, kappa` DEFINED from cross-term content BEFORE computing `G_munu`; Lambda fitted nonzero (background is Einstein-negative — do NOT set Lambda=0); the SAME kappa, Lambda work across an (M, x) family; no `-1/2 R`/SUSY/GST-action/Weinberg in the derivation chain. "Curved but not Einstein" is an acceptable full result.
- *Risk:* HIGH (circularity is subtle and the answer is hoped-for). *Needs research:* YES — the input audit and the intrinsic-kappa definition are genuinely open.

### Phase Ordering Rationale
- **A0 before A:** a wrong det or contaminated bridge invalidates the homogeneity verdict; reconcile conventions and fix the bridge first.
- **A before B before C:** strict dependency — A's KILL stops everything; B's "no M-sourcing" stops C. This matches the milestone's own gating and the COMPUTATIONAL dependency graph.
- **Cheapest-and-decisive first:** A needs only the Hessian and its x-dependence (NOT the full Riemann), the cheapest gate; full curvature (B) and the Einstein test (C) are progressively more expensive and only run if warranted.

### Phases Requiring Deep Investigation
- **Needs deeper investigation (`/gpd:research-phase` or direct computation):** Phase A (exact `Stab_{E_6}(E_11)` structure; totally-geodesic resolution of the Table 7 inference); Phase C (intrinsic definition of kappa and T_munu without circular inputs).
- **Well-established procedures (straightforward execution):** Phase A0 (mechanical engine reuse, measured); the Totaro-curvature mechanics in B (closed form, in-repo polarization).
- **Genuinely open questions (outcome uncertain):** the Phase-A verdict itself (leans GREENLIGHT, not proven); whether B shows M-sourcing vs pure-Lambda; whether C reaches Einstein vs "curved but not Einstein" (honest prior: the latter).

---

## Confidence Assessment

| Area | Confidence | Notes |
|---|---|---|
| Computational Approaches | **HIGH** | Reuse path + dim-4 tractability MEASURED (run, not assumed); cost cliff (symbolic inverse) measured with a working mitigation; stack fixed and confirmed |
| Prior Work | **HIGH** (math), **MEDIUM-HIGH** (Phase-A inference), **HIGH** (novelty) | Cone/curvature math pinned to Totaro + Faraut-Koranyi (both peer-reviewed, confirmed); Phase-A "non-geodesic" is a Table 7 inference; novelty flag is robust |
| Methods | **HIGH** (curvature + orbit engines), **MEDIUM** (signature bridge) | Both load-bearing methods pinned to a source AND a validated in-repo implementation; the bridge is a modeling choice to FIX, not discover |
| Pitfalls | **HIGH** | The four headline traps each backed by published math + corrected in-repo code; the failure modes are concrete with runnable disconfirming checks |

**Overall confidence: HIGH** on the machinery and the gated structure; the *scientific outcome* is genuinely uncertain by design (this is a KILL test — a decisive verdict either way is a full pass).

### Gaps to Address
- **Phase-A verdict is an inference, not a theorem.** Absence of V_0 from the Table 7 maximal-totally-geodesic list strongly suggests non-geodesic, but a non-maximal slice could be geodesic inside a larger geodesic submanifold (`F_4(-20)/Spin(9)` or `Sp(1,3)/...`). -> Compute the second fundamental form directly in Phase A.
- **Exact `Stab_{E_6}(E_11)` not cleanly tabulated** (a parabolic-type subgroup, Levi containing Spin(9,1)). -> Build `{D in e_6 : D*E_11 = 0}` explicitly as a kernel over Q.
- **Signature bridge is a modeling choice.** Construction (ii) is recommended but if it fails to capture the V_0<->matter coupling, (i) (with its separate C*-bottleneck conjecture) is the fallback. -> Decide at A0 via the reduction gate.
- **No experimental constraint.** This is pure exact differential geometry on an algebraic structure; validation is internal (limiting cases: H^3 const `-1`, center Einstein-negative, exact Minkowski at the center) — there is no laboratory benchmark, so the limiting-case checks carry the full validation burden.
- **Prompt-named files absent from `code/`.** `peirce_coupling.py`/`h3o_tower.py`/`rho_directional_derivatives.py`/`trip_tracking.py` are referenced in the milestone prompt; METHODS found some absent and superseded by `ring_lemma_verification.py` + `embedding_under_E_verification.py`, while COMPUTATIONAL found `peirce_coupling.py`/`rho_directional_derivatives.py` PRESENT (float/real-only, det buggy). -> Roadmapper/executor should confirm file provenance at A0 and not assume prompt filenames verbatim; the engine is the single source of truth regardless.

---

## Open Questions (prioritized)

1. **[HIGH — blocks Phase A] Is h_munu(x) genuinely x-dependent after fixing E_11?** The KILL/GREENLIGHT fork. Settled by curvature-invariant x-dependence + the `Stab_{E_6}(E_11)`-orbit vs basepoint-family dimension count, exact over Q.
2. **[HIGH — blocks Phase A] Is the V_0 slice totally geodesic?** If II=0 -> `R^slice` = bulk constant -> KILL. Table 7 says probably not, but must be computed (and V_0 not-inside the larger geodesic submanifolds ruled out).
3. **[HIGH — Phase A0 decision] Which signature construction reduces exactly to Minkowski at (M=0, center)?** (ii) measured to give the Minkowski det directly; gate decides.
4. **[MEDIUM — blocks Phase B verdict] Is the V_0-block curvature controlled by the MIXED cross-term components `C_{(V_0)(V_1)(V_{1/2})}` vs the pure `C_{(V_0)^3}`?** Determines whether matter genuinely sources via cross-terms (off-switch test).
5. **[MEDIUM — Phase C] Does `G_munu ~ T_munu` for any natural cross-term-built `T_munu`?** Honest prior: "curved, possibly not Einstein."
6. **[LOW] Does dim-10 V_0 curvature ever need exact computation?** Only if the 4-dim slice is insufficient; mpmath fallback exists. Off the critical path.

---

## Sources

### Primary (HIGH — load-bearing, cite directly)
- **Totaro, B., "The Curvature of a Hessian Metric," Int. J. Math. 15 (2004) 369-391; arXiv:math/0401381.** — Explicit Riemann tensor of any Hessian metric in 3rd derivatives only; Lemma 2.4 (cone <-> det=1 hypersurface warped product); Example (octonionic det = `E_{6(-26)}/F_4` noncompact); Thm 3.1 (Clebsch-covariant sectional curvature on R^3). THE curvature engine for B/C. [Confirmed peer-reviewed; both scouts read the PDF locally and quote the identical formula.]
- **Faraut, J. & Koranyi, A., *Analysis on Symmetric Cones*, OUP 1994.** — Symmetric-cone = Jordan-cone-of-squares; `g_X = Hess(-log det)`; `g^{pq} = P(X)`; `Omega = G/K`, h_3(O) => `E_{6(-26)}/F_4`. Authoritative for all "already SOLID" cone facts. [Confirmed canonical reference.]
- **Kollross, A. & Rodriguez-Vazquez, A., "Totally geodesic submanifolds in exceptional symmetric spaces," Adv. Math. (2023); arXiv:2202.10775.** — Table 7: complete maximal-totally-geodesic classification for `E_{6(-26)}/F_4`. DECISIVE anchor for Phase A. [Confirmed peer-reviewed; scout read Table 7 locally.]
- **In-repo engine `code/ring_lemma_verification.py` (VALD-64-01).** — Certified-over-Q `det_3` (cross `2 Re((x2 x1) x3)`, CH norm + 324/324 inner-derivation annihilation = F_4-invariance), `jordan`, `polarize_d`, `cayley_hamilton_norm`, `inner_derivations`. PRIMARY reuse target. [Run this session -> ALL_PASS.]
- **Baez, J., "The Octonions," Bull. AMS 39 (2002) 145-205; arXiv:math/0105155.** — `F_4 = Aut(h_3(O))`, `OP^2 = F_4/Spin(9)`, `E_{6(-26)}` det-preserving, `{det=1} = E_{6(-26)}/F_4`. Q5 group facts.

### Secondary (MEDIUM — corroborating)
- **de Wit, B. & Van Proeyen, A., CMP 149 (1992) 307; arXiv:hep-th/9112027.** — GEOMETRY ONLY: homogeneous cubic norms, curvature-from-`d_ijk`, `J_3^O => E_{6(-26)}/F_4`. (Lagrangian/SUSY content explicitly NOT used.)
- **O'Neill, B., *Semi-Riemannian Geometry* (1983); Shima, *The Geometry of Hessian Structures* (2007); McCrimmon, *A Taste of Jordan Algebras* (2004).** — Gauss-Codazzi; Hessian-manifold theory; Peirce decomposition + `P(X) = 2L(x)^2 - L(x^2)`.
- **Visser, M., arXiv:1702.05572 (Wick-rotation hazards); arXiv:2406.06047 (admissible complex metrics).** — Justify preferring construction (ii); the metric-rotation hazard for (i).
- **Dubois-Violette & Todorov, Nucl. Phys. B 938 (2019); arXiv:1604.01247.** — `h_2(O)=10D Minkowski`, Peirce dictionary (Q4 adjacent, det<->Minkowski).
- **Garibaldi-Guralnick; Derksen-Kemper, *Computational Invariant Theory*.** — generic orbit dim = rank of infinitesimal action (char 0); basis for the Phase-A engine. [In-repo validated.]
- **In-repo `embedding_under_E_verification.py` (C_u machinery), `orbit_dimension_gate.py` (orbit/stabilizer dims); prior `52-kkt-spacetime`, `52-observer-uniqueness` (h_2(C_u) ~ R^{3,1}, mostly-minus).**

### Tertiary (LOW — lineage / explicitly NOT load-bearing)
- **Castro, C. (octonionic gravity/membrane action); Singh, T.P. et al. (octonionic emergent gravity).** — Prior octonionic-gravity attempts, action-based or flat-background; cited as DISTINCT prior attempts, not methods to adopt. [Castro venue/year MEDIUM, paywalled.]
- **DEAD routes (explicitly NOT cited as derivations):** lattice/Fisher continuum limit; the det/GST/Weinberg N=2 supergravity *Lagrangian* (circular — see Pitfall 4); Jacobson 1995 thermodynamic/ensemble route.
- **In-repo `octonion_algebra.py` det_3 / `peirce_coupling.py` / `h3o_tower.py`.** — The BUGGY/inconsistent det conventions; documented as the hazard to reconcile against, NOT to use.

---

_Synthesis completed: 2026-05-30. Overwrote the stale v16.0 SUMMARY.md. Ready for research roadmap (phases 70+)._

```yaml
# --- ROADMAP INPUT (machine-readable, consumed by gpd-roadmapper) ---
synthesis_meta:
  project_title: "Experiential Measure on Structure Space — v17.0: Gravity as Intrinsic Curvature of the h_3(O) Bulk Geometry"
  synthesis_date: "2026-05-30"
  input_files: [METHODS.md, PRIOR-WORK.md, COMPUTATIONAL.md, PITFALLS.md]
  input_quality: {METHODS: good, PRIOR-WORK: good, COMPUTATIONAL: good, PITFALLS: good}

conventions:
  unit_system: "natural"
  metric_signature: "mostly_minus"   # Lorentzian slice via det_2; bulk cone is Riemannian (positive-definite)
  fourier_convention: "N/A"
  coupling_convention: "kappa, Lambda fitted in Phase C; Lambda != 0 (background Einstein-negative); det normalization d(X,X,X)=6*det"
  renormalization_scheme: "N/A"
  det_cross_term: "2*Re((x2 x1) x3)  [engine ring_lemma_verification.det_3 — SINGLE SOURCE OF TRUTH]"
  potential: "-log det  (FIX at start; do not mix with det)"

methods_ranked:
  - name: "Totaro closed-form Hessian curvature R_ijkl = -(1/4) g^{pq}(f_jlp f_ikq - f_ilp f_jkq)"
    regime: "any cubic-norm Hessian metric; exact over Q; decisive on the 4-dim slice"
    confidence: HIGH
    cost: "dim-4 ~19s (matter rational); symbolic inverse cliff >200s if matter+coords all symbolic"
    complements: "sympy.diffgeom (4-dim one-point cross-check); mpmath (dim-10 fallback)"
  - name: "Orbit-dimension via exact rank over QQ (Phase A homogeneity verdict)"
    regime: "dim Stab_{E6}(E_11) and basepoint-family dim; generic-point rank, char 0"
    confidence: HIGH
    cost: "seconds-minutes; reuse orbit_dimension_gate.py"
    complements: "totally-geodesic / Gauss check; Kollross-Rodriguez-Vazquez Table 7"
  - name: "Signature bridge (ii): eta from h_2(C_u) det + cone-Hessian perturbation h_munu"
    regime: "reduces to EXACT Minkowski at (M=0, center) by construction"
    confidence: MEDIUM
    cost: "trivial"
    complements: "bridge (i) Wick-rotate-via-u (fallback; carries a separate C*-bottleneck conjecture)"
  - name: "Perturbative expansion in ||M|| and rho_J around center I/3"
    regime: "small matter / near-center; finite jet (det cubic)"
    confidence: HIGH
    cost: "cheap; series-expand in single matter amplitude t for M-dependence"
    complements: "fixed-rational-matter full symbolic evaluation"
  - name: "Einstein-structure linear test G_munu = kappa T_munu + Lambda g_munu (Phase C)"
    regime: "exact / linear-in-M / none; T_munu from cross-terms, defined BEFORE G_munu"
    confidence: MEDIUM
    cost: "cheap once R_ijkl exists"
    complements: "honest 'curved but not Einstein' outcome"

phase_suggestions:
  - name: "A0 engine reconciliation + signature bridge"
    goal: "Certify a single det_3 and fix the signature bridge (ii) reducing to exact Minkowski at center"
    methods: ["Signature bridge (ii): eta from h_2(C_u) det + cone-Hessian perturbation h_munu"]
    depends_on: []
    needs_research: false
    risk: LOW
    pitfalls: ["pitfall-2-cross-term-association", "pitfall-3-signature-wick", "pitfall-12-index-assignment", "pitfall-13-sign-convention"]
  - name: "A homogeneity KILL gate"
    goal: "Decide homogeneous (route DEAD) vs genuinely position-dependent h_munu(x) after fixing E_11"
    methods: ["Orbit-dimension via exact rank over QQ (Phase A homogeneity verdict)", "Totaro closed-form Hessian curvature R_ijkl = -(1/4) g^{pq}(f_jlp f_ikq - f_ilp f_jkq)"]
    depends_on: ["A0 engine reconciliation + signature bridge"]
    needs_research: true
    risk: MEDIUM
    pitfalls: ["pitfall-1-homogeneity-trap", "pitfall-5-slice-vs-bulk-totally-geodesic", "pitfall-10-offcenter-vs-field", "pitfall-11-single-point-sampling", "pitfall-8-float-cancellation"]
  - name: "B matter-sourcing"
    goal: "Show matter M in V_1/V_{1/2} sources slice curvature via cross-terms (cross-term on/off; ||M|| scaling)"
    methods: ["Totaro closed-form Hessian curvature R_ijkl = -(1/4) g^{pq}(f_jlp f_ikq - f_ilp f_jkq)", "Perturbative expansion in ||M|| and rho_J around center I/3"]
    depends_on: ["A homogeneity KILL gate"]
    needs_research: false
    risk: MEDIUM
    pitfalls: ["pitfall-6-lambda-vs-matter", "pitfall-5-slice-vs-bulk-totally-geodesic", "pitfall-9-rho-real-only-misuse", "pitfall-8-float-cancellation"]
  - name: "C Einstein structure"
    goal: "Test G_munu = kappa T_munu + Lambda g_munu at exact/linear/none; honest curved-but-not-Einstein acceptable"
    methods: ["Einstein-structure linear test G_munu = kappa T_munu + Lambda g_munu (Phase C)"]
    depends_on: ["B matter-sourcing"]
    needs_research: true
    risk: HIGH
    pitfalls: ["pitfall-4-circularity-gst-weinberg", "pitfall-7-tuned-point-overclaim"]

critical_benchmarks:
  - quantity: "Slice (h_2(C_u)) cubic norm at center / Hess(-log det) at I/3"
    value: "det slice = b*g/3 - p^2/3 - q^2/3 (Minkowski form); Hess at I/3 = diag(9,9,18,18), det 26244"
    source: "COMPUTATIONAL.md (measured this session); 52-kkt-spacetime"
    confidence: HIGH
  - quantity: "H^3 = SL(2,C)/SU(2) det=1 sub-slice sectional curvature (M=0 limit)"
    value: "constant negative, -d^2/4 = -1 (d=2, rank-1)"
    source: "Totaro 2004 Cor 2.3; 52-kkt-spacetime"
    confidence: HIGH
  - quantity: "Center X=I/3 Ricci (irreducible symmetric space)"
    value: "Einstein with NEGATIVE Ricci proportional to g (Cartan); Lambda < 0"
    source: "Totaro 2004 Example; Faraut-Koranyi 1994"
    confidence: HIGH
  - quantity: "Single-copy orbit/stabilizer anchor (Phase A engine validation)"
    value: "orbit dim 24 / Spin(8) stabilizer dim 28"
    source: "orbit_dimension_gate.py (in-repo, ALL_PASS); Garibaldi-Guralnick"
    confidence: HIGH
  - quantity: "Background Minkowski at (M=0, center) — signature-bridge gate"
    value: "g_munu = eta_munu EXACTLY, zero residual h_munu"
    source: "METHODS.md M3; PITFALLS.md Pitfall 3"
    confidence: HIGH
  - quantity: "Associator gap between det conventions on octonionic data"
    value: "0.67 (engine det 24.978 vs buggy (x1 x2) x3 order 24.306)"
    source: "COMPUTATIONAL.md (measured on a rational octonionic point)"
    confidence: HIGH

open_questions:
  - question: "Is h_munu(x) genuinely x-dependent after fixing E_11 (KILL vs GREENLIGHT)?"
    priority: HIGH
    blocks_phase: "A homogeneity KILL gate"
  - question: "Is the V_0 slice totally geodesic (II=0 => bulk-constant curvature => KILL)?"
    priority: HIGH
    blocks_phase: "A homogeneity KILL gate"
  - question: "Which signature construction reduces exactly to Minkowski at (M=0, center)?"
    priority: HIGH
    blocks_phase: "A0 engine reconciliation + signature bridge"
  - question: "Is V_0-block curvature controlled by mixed cross-terms C_{(V0)(V1)(V_half)} vs pure C_{(V0)^3}?"
    priority: MEDIUM
    blocks_phase: "B matter-sourcing"
  - question: "Does G_munu proportional to T_munu for any natural cross-term-built T_munu (Einstein vs curved-not-Einstein)?"
    priority: MEDIUM
    blocks_phase: "C Einstein structure"
  - question: "Does dim-10 V_0 curvature ever need exact computation (symbolic inverse times out)?"
    priority: LOW
    blocks_phase: "none"

contradictions_unresolved: []
# All apparent conflicts were resolved in synthesis (documented in prose):
#  - 3 det conventions -> reconciled on the certified engine det_3 (single source of truth)
#  - 2 signature constructions -> resolved to (ii) (only one reducing to exact Minkowski)
#  - Phase-A verdict tension (homogeneity trap) -> resolved by mandating curvature-invariant + stabilizer-count test, not components
#  - prompt-named-files-absent vs present (METHODS vs COMPUTATIONAL) -> flagged as a Phase-A0 provenance check, NOT a physics contradiction; engine is source of truth either way
```
