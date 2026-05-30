# Methods Research

**Domain:** Mathematical physics — Riemannian/Lorentzian geometry of the symmetric cone of h_3(O); Hessian-metric curvature of a cubic norm; exact symbolic computation over Q on octonionic data.
**Researched:** 2026-05-30
**Milestone:** v17.0 — gravity as the intrinsic curvature the V_0 = h_2(O) Peirce slice inherits from the h_3(O) cone geometry g_X = Hess(-log det), sourced by matter in V_1+V_{1/2} via cubic-norm cross-terms. (Supersedes the v16.0 RING-lemma METHODS that previously occupied this file.)
**Confidence:** HIGH on the two load-bearing methods (Totaro closed-form curvature of a Hessian metric; orbit-dimension-via-rank), each pinned to a peer-reviewed source AND an in-repo working implementation. MEDIUM only on the signature-bridge construction, which is genuinely a modeling choice this milestone must FIX, not discover.

### Scope Boundary

This file covers analytical and numerical PHYSICS/geometry methods (Hessian-metric curvature, Gauss-Codazzi, orbit dimensions, perturbative expansion, Einstein-structure tests). Software/library version pins live in COMPUTATIONAL.md. The research landscape (what is solid vs conjectural) lives in PRIOR-WORK.md / SUMMARY.md. Convention traps live in PITFALLS.md.

---

## TL;DR for the roadmapper (read this first)

1. **Signature bridge (A0): use construction (ii).** Take eta from h_2(C_u)'s own det (already established in `52-kkt-spacetime`), let the h_3(O) cone-Hessian supply only h_mu_nu. Construction (i) — restrict-then-Wick-rotate g_X via u=e_7 — has no off-the-shelf machinery that lands on EXACT Minkowski at (M=0, center) without an ad-hoc analytic continuation; it bundles in a second conjecture (the C*-bottleneck signature flip). Comparison in Method 1.
2. **Curvature: do NOT call `sympy.diffgeom` on the 10-dim metric.** Use Totaro's closed form `R_ijkl = -(1/4) g^{pq}(f_jlp f_ikq - f_ilp f_jkq)` (Method 3), which needs ONLY third derivatives of the potential and one matrix inverse g^{pq}. This is the single most important recommendation in this file.
3. **Homogeneity test (Phase A, the dealbreaker): reuse the EXACT in-repo machinery.** `orbit_dimension_gate.py` already computes orbit/stabilizer dimensions as the rank over QQ of the infinitesimal-action matrix (it reproduces orbit 24 / Spin(8) at single copy). Phase A is the SAME computation with the e_6/f_4 generators that fix E_11 — Method 5.
4. **Everything stays exact over Q.** Reuse `embedding_under_E_verification.py` (octonion arithmetic, jordan, proj_u, slice_to_complex) and `ring_lemma_verification.py` (det_3, Tr, Tr2, polarize_d, jordan_L_matrix, inner_derivations). Do NOT rebuild octonion arithmetic. Do NOT import `octonion_algebra.py`'s det_3 (known-buggy cross-term — see PITFALLS / Method 3 caution).

---

## Recommended Methods

### Analytical Methods

| Method | Purpose | Why Recommended |
| ------ | ------- | --------------- |
| **Hessian-metric closed-form curvature (Totaro)** | R_ijkl, Ricci, scalar of g_X = Hess(-log det) directly from third derivatives of the potential | The curvature of a Hessian metric depends ONLY on derivatives of the potential to order 3 (not 4). One exact formula, no Christoffel-of-the-metric chain. Decisive for B/C. |
| **Quadratic-representation form of the cone metric (Faraut-Koranyi)** | Closed form g_X(A,B) = (P(X)^{-1} A \| B) in the Jordan product; the metric and its inverse without finite-differencing det | Gives g^{pq} (needed by the Totaro formula) symbolically via P(X), the Jordan product, and the trace form — exact over Q, no numeric Hessian. |
| **Polarization / directional derivatives of the cubic norm** | Taylor/jet of det and of rho_J around the center X=I/3 in V_0 directions; organize h_mu_nu in powers of \|\|M\|\| and rho_J | The full polarization d(X,Y,Z) (with d(X,X,X)=6 det) IS the third-derivative tensor f_ijk the curvature formula needs. Already implemented as `polarize_d`. det is cubic, so the jet TERMINATES. |
| **Orbit-stabilizer / infinitesimal-action rank (Lie-algebra method)** | dim Stab_{E_6}(E_11) and the dimension of the (basepoint, slice) family modulo that stabilizer — the Phase-A homogeneity verdict | Generic orbit dimension = rank of the infinitesimal action at a generic point (Derksen-Kemper, char 0; Garibaldi-Guralnick orbit method). Exact over Q. Already in-repo for the single-copy case. |
| **Gauss-Codazzi (induced-submanifold curvature)** | Curvature of the V_0-restricted metric as a SUBMANIFOLD of the 27-dim cone, separating intrinsic (Gauss) curvature from the second fundamental form (extrinsic embedding) | The honest way to ask "what curvature does the slice INHERIT": Gauss equation gives intrinsic R of the slice from ambient R minus an II∧II term. Distinguishes "slice is curved" from "slice is flat but embedded curvedly." |
| **Einstein-structure linear test** | Test G_mu_nu = kappa T_mu_nu + Lambda g_mu_nu (Phase C) exactly / linearized-in-M / not at all | Compute G_mu_nu = R_mu_nu - (1/2)R g_mu_nu from the slice metric; solve the overdetermined linear system for (kappa, Lambda). Honest "no" (curved-but-not-Einstein) is an acceptable, well-defined outcome. |

### Numerical Methods

| Method | Purpose | When to Use |
| ------ | ------- | ----------- |
| **Exact rational arithmetic (SymPy over QQ)** | The DECISIVE path: octonion arithmetic, det_3, ranks, curvature components | ALWAYS on the decisive path. The program works exact over Q on integer/rational octonionic points; ranks via `sympy.Matrix.rank()` / `DomainMatrix` over QQ. NEVER float64 on a rank or a "= 0?" decision. |
| **High-precision mpmath fallback** | Sanity-check a symbolic result too heavy to fully simplify; spot-check signature/eigenvalues of g at a generic point | Only as a cross-check or to triage which components are nonzero before a full symbolic simplify. Decisions are confirmed exactly over Q. |
| **Random generic-point sampling over Z** | Establish a rank / non-vanishing at a GENERIC point (rank lower-semicontinuous; max over a few integer points = generic rank) | For orbit dimension and "is h_mu_nu non-constant?" — evaluate at >= 2 generic INTEGER octonionic points, take the max rank. Exactly the `octonionic_points()` pattern in `orbit_dimension_gate.py`. |

### Computational Tools

| Tool/library | Version | Purpose | Notes |
| ------------ | ------- | ------- | ----- |
| SymPy | 1.14.0 (confirmed in env) | Exact symbolic algebra, `Matrix.rank()` over QQ, `Poly`, `diff`, `simplify`, `cancel` | `sympy.polys.matrices.DomainMatrix` is the FAST exact-rank path over QQ (used in-repo). |
| NumPy | 2.4.2 (confirmed in env) | Float spot-checks only (signature eigenvalues, triage) | NEVER on a decisive rank or zero-test. `numpy.linalg.matrix_rank` is a FORBIDDEN PROXY on the decisive path (engine convention). |
| `sympy.diffgeom` | ships with SymPy 1.14 | `metric_to_Christoffel_2nd`, `metric_to_Riemann_components` — generic curvature from an explicit metric | Works (verified: 2D sphere -> R_θφθφ = sin²θ in 0.09 s). USE ONLY for the 4-dim slice metric AFTER restriction; prefer the Totaro closed form for the 10-dim ambient (cost note in Method 2). |

---

## Method Details

### Method 1 — Signature bridge (Phase A0): COMPARISON and recommendation

**The decision:** how to get a LORENTZIAN g_mu_nu on h_2(C_u) ~= R^{3,1} from the ambient RIEMANNIAN cone-Hessian g_X = Hess(-log det), which is positive-definite everywhere on the open cone.

| Criterion | (i) restrict g_X, Wick-rotate via u=e_7 | (ii) eta from h_2(C_u) det; cone-Hessian supplies only h_mu_nu |
| --------- | --------------------------------------- | -------------------------------------------------------------- |
| Reduces to EXACT Minkowski at (M=0, center)? | Not automatic — needs a chosen analytic continuation / a J with g(J·,J·)-twist; landing exactly on eta is itself a derivation | YES by construction — eta is h_2(C_u)'s own Minkowski form (proven in `52-kkt-spacetime`) |
| Off-the-shelf machinery | None canonical for "Hessian of a cone -> Lorentzian via an algebra's complex structure." Closest: Wick-rotation-in-the-lapse / admissible-complex-metrics (Visser, arXiv:2406.06047) and almost-(para-)complex compatible metrics g(J·,J·)=±g(·,·) — but these ASSUME you already have the Lorentzian target | Standard background-field split g = eta + h; eta fixed, h = (cone-Hessian restricted to V_0) minus its center value |
| What the cone-Hessian must supply | The WHOLE metric AND the signature flip | ONLY the position-dependent perturbation h_mu_nu — exactly the object Phase A needs |
| Risk | The signature flip via u is the C*-bottleneck mechanism (Phase 46): physically motivated but a SECOND, separable claim that can fail independently | h is positive-definite tangentially and must be mapped onto the eta index pattern by a FIXED explicit linear identification (a frame), not an analytic continuation |

**RECOMMENDATION: construction (ii).** It is the only one that satisfies the milestone's own gate ("reduces to exact Minkowski at (M=0, center)") without smuggling in a second conjecture. Concretely:
- eta_mu_nu := the Minkowski form from det(h_2(C_u)) (from `52-kkt-spacetime`), in the 4 real coordinates of h_2(C_u).
- Restrict the cone-Hessian g_X to the V_0-tangent directions, evaluate at X_bg = I/3 + M and at the spacetime point x, project onto the h_2(C_u) sub-slice (use `slice_to_complex` / `proj_u_exact`), and DEFINE h_mu_nu(x) := [g_X restricted to V_0, in h_2(C_u) coordinates] minus [its value at (M=0, center)].
- The tested metric is g_mu_nu(x) = eta_mu_nu + h_mu_nu(x). At (M=0, center) h=0 by construction; Phase A then asks whether h is genuinely x-dependent.

**Canonical sources:** Faraut & Korányi, *Analysis on Symmetric Cones* (1994), cone-metric chapter (g_X is positive-definite — WHY a bridge is needed). For g(J·,J·)=±g(·,·) language if (i) is revisited: para-Kähler / neutral-signature constructions (arXiv:1301.4638). For the Wick-rotation hazards: Visser, "How to Wick rotate generic curved spacetime" (arXiv:1702.05572); "admissible complex metrics" (arXiv:2406.06047).

**Failure modes for THIS setting:** (a) If the V_0-restricted g_X, in h_2(C_u) coordinates, is conformally proportional to eta with an x-INDEPENDENT factor, h_mu_nu is pure-conformal and the position-dependence is trivial — effectively the KILL branch; check explicitly. (b) The index identification V_0-tangent-direction <-> Minkowski mu,nu must be the SAME linear map at every x (a fixed frame), or spurious x-dependence appears — fix the frame once at the center.

**Cost:** trivial relative to the rest — a few exact restrictions/evaluations on the engine.

---

### Method 2 — Curvature of an induced/restricted metric (Gauss-Codazzi + symbolic Christoffels)

**What:** Given the explicit slice metric g_mu_nu(x), compute Riemann/Ricci/Einstein. Two layers:
- *Intrinsic curvature of the slice metric itself*: Γ^a_bc = (1/2) g^{ad}(∂_b g_dc + ∂_c g_db − ∂_d g_bc), then R^a_bcd from Γ and ∂Γ.
- *Inherited-from-bulk (Gauss equation)*: R^slice(W,X,Y,Z) = R^ambient(W,X,Y,Z) + <II(W,Z),II(X,Y)> − <II(W,Y),II(X,Z)>, where II is the second fundamental form of the V_0 slice inside the 27-dim cone. Separates "slice is intrinsically curved" from "slice is flat but sits in the cone curvedly."

**Mathematical basis:** Gauss-Codazzi for pseudo-Riemannian submanifolds (valid provided the induced metric is NON-DEGENERATE — true away from the light cone). O'Neill, *Semi-Riemannian Geometry* (1983), ch. 4 — the canonical pseudo-Riemannian reference (Totaro cites O'Neill [25] for exactly this).

**Tooling:** `sympy.diffgeom.metric_to_Christoffel_2nd`, `metric_to_Riemann_components` (VERIFIED working: 2D sphere -> R_θφθφ = sin²θ, 0.09 s). Build the metric as `TensorProduct(dx_i, dx_j)` of `base_oneforms()`.

**Cost / scaling (CRITICAL):** `metric_to_Riemann_components` computes n^4 components, each a sum over Christoffels with their derivatives; symbolic cost grows steeply (≈ n^4 × cost-of-simplify, and simplify of rational octonionic expressions is the bottleneck). For the 4-dim slice this is feasible. For the **10-dim V_0 metric it is NOT recommended directly** — 10^4 components and degree-heavy rational simplification can blow up. **Use the Totaro closed form (Method 3) for the ambient/10-dim object; reserve `diffgeom` for the 4-dim slice**, and even there prefer the closed form, using `diffgeom` only as an independent cross-check on a few components.

**Failure modes for THIS setting:** (a) Degeneracy of the induced metric on the light cone — restrict to the timelike/spacelike interior, carry signature explicitly. (b) `simplify` non-termination on octonionic rational entries — use `cancel`/`together` selectively, or evaluate components at a generic integer point to test vanishing (zero is generic). (c) The Gauss route needs the AMBIENT Riemann tensor too; get THAT from Method 3, not from diffgeom on 27 dims (hopeless).

---

### Method 3 — Hessian-metric curvature in closed form (THE primary curvature method)

**What:** For ANY Hessian metric g_ij = ∂²f/∂x_i∂x_j, the curvature is a closed expression in derivatives of f to order THREE only.

**Mathematical basis (Totaro 2004, arXiv:math/0401381, "The curvature of a Hessian metric," formula on p.4 — verified by direct read of the PDF this session):**

- Christoffel of the first kind: Γ_ijk = (1/2) f_ijk,  with f_ijk := ∂³f/∂x_i∂x_j∂x_k.
- Riemann tensor:  **R_ijkl = −(1/4) Σ_{p,q} g^{pq} ( f_jlp f_ikq − f_ilp f_jkq )**.
- Cone-normalized variant for the homogeneous-degree-d norm with g_ij = −(1/d(d−1)) ∂²f/∂x_i∂x_j (Totaro p.5, f = det, d = 3): R_ijkl = −(1/(4 d²(d−1)²)) Σ g^{pq}(f_jlp f_ikq − f_ilp f_jkq).
- Sectional curvature of (∂_1,∂_2): R_1212 / (g_11 g_22 − g_12²).
- Warped-product Lemma 2.1 (Totaro p.5-6): the cone metric is a warped product over the {f=1} hypersurface, so cone curvature determines (and is determined by) the hypersurface (E_{6(-26)}/F_4) curvature — use this to pass between the "cone" and "det=1 hyperboloid" pictures.

**Why this is decisive:** (1) curvature needs only f_ijk = the third derivative of the potential — EXACTLY the polarization tensor `polarize_d` implements (d(X,X,X)=6 det, so the symmetric trilinear form is the third-derivative tensor of det up to a fixed constant). (2) g^{pq} is the inverse Hessian; by Faraut-Korányi g_X(A,B) = (P(X)^{-1}A \| B), so g^{pq} is the quadratic representation P(X) in coordinates — available symbolically. No fourth derivatives, no Christoffel-of-the-metric recursion.

**Two potentials, one caution.** The milestone's potential is phi = −log det (the Faraut-Korányi cone metric). Totaro's degree-d formula uses f = det directly with the −1/(d(d−1)) prefactor; he also notes (p.3) the relation to ∂²(log f)/∂x_i∂x_j. These differ by the rank-one ∂log f ⊗ ∂log f term (the radial / det=const direction). For curvature of the FULL cone metric Hess(−log det), apply the formula to f̃ = −log det directly:  g_ij = −(det_ij/det) + (det_i det_j/det²),  and f̃_ijk = third derivative of (−log det), assembled from det_i, det_ij, det_ijk (all polynomial; det is cubic so det_ijkl ≡ 0). **DECIDE and FIX which potential (det vs −log det) at the start — they give metrics differing by the radial direction; the roadmapper must not mix them.**

**Implementation notes (pseudocode):**

```python
# All exact over Q. Reuse polarize_d, det_3, jordan from ring_lemma_verification.
# 1. Coordinates: the 27 (or restricted-to-V0 10) real components, engine layout.
# 2. det_i, det_ij, det_ijk: directional derivatives of det = polarizations
#    (det_ijk symmetric trilinear = (1/6)*polarize_d basis components; det cubic => det_ijkl = 0).
# 3. g_ij = Hess(-log det) = -(det_ij/det) + det_i det_j/det^2 ; invert -> g^{pq}
#    (cross-check g^{pq} numerically against Faraut-Koranyi P(X)).
# 4. F_ijk = third derivative of (-log det); R_ijkl = -(1/4) sum_{p,q} g^{pq}(F_jlp F_ikq - F_ilp F_jkq).
# 5. Ricci R_ik = sum g^{jl} R_ijkl  (with index placement fixed once); scalar; G = Ric - (1/2)R g.
# 6. Evaluate at X_bg = I/3 + M; expand in ||M|| (Method 4).
```

**Cost/scaling:** dominated by forming g^{pq} (one 10×10 or 27×27 exact inverse) and the n²-fold contraction; for the 10-dim V_0 this is feasible exactly over Q (compare: the single-copy orbit rank of a ~52×27 matrix runs ~20-110 s in-repo). det being cubic (fourth derivatives vanish identically) is a major simplification unique to a cubic norm.

**Validation:** (a) At X = I/3 (center, M=0) the cone is E_{6(-26)}/F_4 × R^+, an irreducible Riemannian symmetric space, hence EINSTEIN of NEGATIVE curvature (Cartan) — computed Ricci at center must be ∝ g with a negative constant. (b) The h_2(C_u) sub-block: Hess(−log det) must reproduce the constant-curvature hyperbolic metric on H^3 = SL(2,C)/SU(2) (per `52-kkt-spacetime`). (c) Diagonal cone diag(a,b,c): −log det = −log(abc) factorizes, giving an explicit flat-in-log-coordinates check.

**Failure modes for THIS setting:** (a) Octonion non-associativity makes det's cross-term association-sensitive — the third-derivative tensor MUST be built from the CORRECTED det (cross = 2Re((x2 x1) x3), Phase-64.1), NOT the buggy `octonion_algebra.py` order. (b) The Faraut-Korányi g = (P(X)^{-1}·\|·) identity is proven for ∂²(−log det); confirm the engine's det normalization matches before trusting g^{pq} = P(X). (c) Constant negative curvature at the center is the BACKGROUND (pure-Lambda); do not mistake it for matter-sourced curvature — the Phase-B claim concerns the M-DEPENDENT part.

---

### Method 4 — Expansion around the center X = I/3 (perturbative organization)

**What:** Taylor/jet of g_X (and rho_J) about the F_4-symmetric point X = I/3 (rho_J = 0), expanding h_mu_nu in powers of \|\|M\|\| (matter in V_1+V_{1/2}) and of the off-center-ness rho_J(X_bg).

**Mathematical basis:** det is cubic, so −log det has a finite-order rational Taylor expansion around any interior point; directional derivatives ARE polarizations of det (the `polarize_d` tensor d(X,Y,Z)). Natural small parameters: \|\|M\|\| and rho_J(X_bg). The directional-derivative primitive lives in `polarize_d`. (NOTE: the prompt names `rho_directional_derivatives.py`, which is NOT present in `code/` as of this survey — see "Engine inventory" caution.)

**Implementation notes:** substitute X = I/3 + s·M + (spacetime displacement), expand det as a polynomial in s, read coefficients = polarizations d(I/3, ·, ·). Because det is cubic the expansion TERMINATES — no resummation issue. Organize: leading h ~ O(\|\|M\|\|) cross-term (V_0–V_1/V_{1/2} coupling), curvature ~ O(\|\|M\|\|²) from the F_ijk F_ijk structure of Method 3.

**Cost:** cheap — finite polynomial expansion, exact over Q.

**Failure modes:** (a) Expanding in the WRONG variable — the physically meaningful smallness is \|\|M\|\| (matter) and rho_J (off-center), NOT the spacetime coordinate x (which can be O(1)). (b) Forgetting that the cross-terms 2Re(...) coupling V_0 to V_1/V_{1/2} are the ONLY channel for M to enter the V_0 metric — Phase B's "switch off cross-terms" control (replace det by the block-diagonal det(V_1)·det(V_0)) requires taking the polarization with the FULL det, then again with the block-diagonal product; the difference is the M-sourced part.

---

### Method 5 — Transitivity / homogeneity test (Phase A, THE dealbreaker)

**What:** Decide whether all (basepoint, slice) pairs are isometric — i.e. whether Stab_{E_6}(E_11) acts transitively enough on basepoints to render h_mu_nu x-independent. Compute (1) dim Stab_{E_6}(E_11) and (2) dim of the basepoint family modulo that stabilizer.

**Mathematical basis (Derksen-Kemper char-0 criterion; Garibaldi-Guralnick/Lawther orbit method):** generic orbit dimension = RANK, at a generic point, of the infinitesimal-action matrix whose rows are (Lie-algebra generator) · (point). dim(orbit) = rank; dim(stabilizer) = dim(algebra) − rank. This is EXACTLY the method implemented and validated in-repo.

**Reuse (decisive):** `code/orbit_dimension_gate.py` already (a) builds f_4 = span{[L_a,L_b]} as 52 explicit 27×27 rational matrices, (b) computes orbit/stabilizer dims as exact ranks over QQ via `span_rank_over_QQ` / `DomainMatrix`, and (c) reproduces the single-copy anchor orbit 24 / Spin(8) stabilizer 28. **Phase A is the same computation** with: (i) e_6 = str(h_3(O)) (dim 78, the cone's isometry algebra) or its relevant subalgebra as generators, (ii) the stabilizer Lie algebra {D in e_6 : D·E_11 = 0} built explicitly as a kernel (exact over Q), (iii) the infinitesimal action on the BASEPOINT family (I/3 + M) rather than on a single state. dim(basepoint family mod stabilizer) = dim(family) − rank(infinitesimal action of Stab_{E_6}(E_11)).

**The verdict logic:**
- Residual stabilizer transitive on the basepoint family (rank = dim family) => every basepoint isometric => h_mu_nu x-independent => **KILL** (route dead, stop — report homogeneous, do NOT soften).
- Orbit a proper subset (rank < dim family) => genuinely inequivalent basepoints => h_mu_nu varies => proceed to B.

**Cost/scaling:** single-copy ranks run ~20-110 s each in-repo; the basepoint version is comparable (a few exact ranks of matrices of size ~dim(algebra) × dim(family)). Cheap and decisive — why the milestone does it FIRST.

**Failure modes for THIS setting:** (a) Using the WRONG algebra — Stab_{E_6}(E_11) is NOT all of f_4; E_11 = diag(1,0,0) is a primitive idempotent and its E_6-stabilizer is a specific parabolic-type subgroup (the Peirce-grading stabilizer). Build {D in e_6 : D·E_11 = 0} explicitly before computing its orbit. (b) Conflating "the CONE is homogeneous" (true — E_6 acts transitively on the open cone) with "the SLICE-with-fixed-E_11 family is homogeneous" (the actual question — only the RESIDUAL stabilizer survives after fixing E_11; fixing E_11 BREAKS transitivity, which is the whole point). (c) Rank at a non-generic basepoint underestimates the orbit — sample >= 2 generic integer points, take the MAX rank (lower-semicontinuity), as the engine already does.

---

### Method 6 — Einstein-structure test (Phase C, strong form)

**What:** Given the explicit slice metric g_mu_nu(x) and a candidate T_mu_nu built from the V_1/V_{1/2} cross-term content of M, test G_mu_nu[g] = kappa T_mu_nu + Lambda g_mu_nu at (a) exact, (b) linear-in-M, or (c) no level.

**Mathematical basis:** G_mu_nu = R_mu_nu − (1/2) R g_mu_nu (from Method 3's R_ijkl, contracted with g^{pq}). The test is a (generically overdetermined) linear system for the two scalars (kappa, Lambda): G_mu_nu − Lambda g_mu_nu must be a constant multiple of T_mu_nu component-by-component. Solve exactly over Q; if no consistent (kappa, Lambda) exists exactly, retry at linear order in \|\|M\|\| (drop O(\|\|M\|\|²) via Method 4).

**Implementation notes:** form the independent component equations G_mu_nu − Lambda g_mu_nu = kappa T_mu_nu; treat (kappa, Lambda) as unknowns; check consistency by exact rank of the augmented linear system. Consistent at exact level = STRONG WIN; consistent only after linearization = WIN (linearized Einstein); inconsistent at both = "curved but not Einstein-structured," explicitly accepted by the milestone.

**Cost:** cheap once R_ijkl exists (a small exact linear solve).

**Failure modes for THIS setting:** (a) The background Lambda is REAL and nonzero (the center is Einstein-with-negative-Lambda, Method 3 validation) — do NOT set Lambda = 0; fit BOTH constants. (b) Choosing T_mu_nu ad hoc to force a fit is the cardinal sin (the milestone's reporting discipline forbids it) — T_mu_nu must be DERIVED from the V_1/V_{1/2} cross-term content independently, then tested, not reverse-engineered from G_mu_nu. (c) An exact fit holding ONLY at the center is not an Einstein STRUCTURE — require it across a neighborhood (generic x), or report it honestly as a center-only coincidence.

---

## Alternatives Considered

| Recommended | Alternative | When to Use Alternative |
| ----------- | ----------- | ----------------------- |
| Totaro closed-form R_ijkl (Method 3) | Full `sympy.diffgeom` Riemann from the metric (Method 2 tooling) | Only on the 4-dim slice as an INDEPENDENT cross-check of a few components; never primary on 10/27 dims (cost blowup). |
| Signature bridge (ii) — eta + cone-Hessian perturbation | Bridge (i) — restrict + Wick-rotate via u=e_7 | Only if (ii) fails the "reduces to exact Minkowski" gate; (i) requires separately establishing the C*-bottleneck signature flip (a second conjecture). |
| Faraut-Koranyi g^{pq} = P(X) closed form | Numerically invert the finite-difference Hessian of −log det | Only as a float spot-check of the symbolic g^{pq}; the decisive g^{pq} must be exact. |
| Orbit dim via exact rank over QQ (Method 5) | Numerical rank (`numpy.linalg.matrix_rank` w/ tolerance) | NEVER on the decisive path — float rank is a FORBIDDEN PROXY; use only to triage which point to do exactly. |
| polarize_d 3rd-deriv tensor of the CORRECTED det | `octonion_algebra.py`'s det_3 | NEVER — its cross-term factor order is known-buggy ((x1 x2) x3 vs (x2 x1) x3); see PITFALLS. |

## What NOT to Use

| Avoid | Why | Use Instead |
| ----- | --- | ----------- |
| `octonion_algebra.py` det_3 on the decisive path | Buggy cross-term association ((x1 x2) x3); the milestone's CAUTION flags it and the engine aliases it as `oa_det_3` (float cross-check only) | The corrected `det_3` / `polarize_d` in `ring_lemma_verification.py` (cross = 2Re((x2 x1) x3)) |
| float64 / numpy rank on any "= 0?" or orbit-dimension decision | Floating point cannot certify exact vanishing of octonionic rational expressions; a spurious near-zero flips a KILL/SURVIVE verdict | Exact rank over QQ (`sympy.Matrix.rank()`, `DomainMatrix`) |
| `sympy.diffgeom` on the 10- or 27-dim metric | n^4 components × heavy octonionic-rational simplify => combinatorial blowup | Totaro closed form (3rd derivatives + one matrix inverse) |
| The lattice/Fisher metric machinery and the posited GST/N=2 supergravity Lagrangian | The two DEAD routes the milestone explicitly rejects (lattice = modeling choice; supergravity = circular) | Intrinsic cubic-norm Hessian curvature only (Methods 1-6) |
| Jacobson 1995 thermodynamic / ensemble "Einstein-equations-as-equation-of-state" | Explicitly rejected ("observers-make-gravity" woo) | One observer, one off-center point, the algebra's own geometry (Methods 3-6) |
| Sage / GAP / Singular / Magma | Not available in the executor venv | SymPy/NumPy exact over Q (everything here is implementable without them) |

## Method Selection by Problem Type

**If the goal is the Phase-A homogeneity verdict (do this FIRST):**
- Use Method 5 (orbit/stabilizer rank over QQ), reusing `orbit_dimension_gate.py` on the E_11-stabilizer acting on basepoints.
- Because it is cheap, exact, decisive, and KILLs or greenlights everything downstream. A homogeneous result stops the project cleanly.

**If A shows genuine x-dependence and the goal is the curvature (Phase B):**
- Use Method 3 (Totaro closed form) for R_ijkl, with Method 4 to organize the M-expansion and the block-diagonal "switch off cross-terms" control.
- Because curvature of a cubic-norm Hessian needs only the finite, polynomial third-derivative tensor; the cross-term-on vs cross-term-off difference isolates the M-sourced curvature.

**If B shows M-sourced curvature and the goal is Einstein structure (Phase C):**
- Use Method 6 (exact/linearized linear test for kappa, Lambda) on G_mu_nu vs a cross-term-derived T_mu_nu.
- Because it gives a definite exact/linear/none verdict and forbids reverse-engineering T to force a fit.

**If a result is too heavy to fully simplify symbolically:**
- Use generic-integer-point evaluation (max over >= 2 points) to settle rank/vanishing, then confirm the decisive instance exactly over Q.
- Because rank and non-vanishing are generic; a single exact confirmation at a generic point certifies the claim.

## Validation Strategy by Method

| Method | Validation Approach | Key Benchmarks |
| ------ | ------------------- | -------------- |
| Method 3 (curvature) | Center must be Einstein with NEGATIVE Ricci ∝ g (irreducible symmetric space, Cartan); h_2(C_u) slice limit must reproduce constant-curvature H^3 = SL(2,C)/SU(2) | E_{6(-26)}/F_4 is Einstein; `52-kkt-spacetime` H^3 limit; diag(a,b,c) factorized −log det |
| Method 5 (orbit) | Reproduce the in-repo single-copy anchor orbit 24 / Spin(8) stabilizer 28 BEFORE trusting the E_11-stabilizer computation | Garibaldi-Guralnick/Lawther single-copy; `orbit_dimension_gate.py` ALL_PASS |
| Method 1 (signature) | At (M=0, center) g_mu_nu must equal eta_mu_nu EXACTLY (Minkowski) | `52-kkt-spacetime` det -> Minkowski quadratic form |
| Method 6 (Einstein) | Lambda must be NEGATIVE and nonzero at leading order (background); fit must hold across a neighborhood, not just the center | Center Einstein constant from Method 3 |
| Engine arithmetic | det_3 LOCKs: d(X,X,X)=6 det_3, det_3(diag(a,b,c))=abc, det_3(I)=1, multiplicativity, Cayley-Hamilton | `ring_lemma_verification.py` LOCK 1-5 (already passing) |

## Engine inventory (what to reuse, what is MISSING)

**Present and reusable (verified by grep this session):**
- `code/embedding_under_E_verification.py`: `oct_mul`, `oct_conj`, `h3o_matmul`, `jordan(A,B)`, `associator`, `proj_u_exact(a, u_index=7)` (the u=e_7 projector — signature-bridge primitive for (i) if revisited), `slice_to_complex`, `cu_to_complex`, `E(X)` (Peirce projector), `h3o_from_coords`, `h3o_identity`.
- `code/ring_lemma_verification.py`: `det_3` (CORRECTED cross-term), `Tr`, `Tr2`, `polarize_d(X,Y,Z)` (symmetric trilinear = third-derivative tensor of det, d(X,X,X)=6 det_3), `jordan`, `jordan_L_matrix(A,basis)` (27×27 L_A), `inner_derivations()` (the 324 brackets spanning f_4), the 27-component coordinate layout.
- `code/orbit_dimension_gate.py`: `span_rank_over_QQ`, `octonionic_points()`, the f_4 builder (52 generators), the orbit-dimension-via-rank GATE (reproduces orbit 24/Spin(8)).

**Named in the prompt but NOT FOUND in `code/` this session (flag for the roadmapper):**
- `peirce_coupling.py`, `h3o_tower.py`, `rho_directional_derivatives.py`, `trip_tracking.py` — referenced in the milestone prompt but absent from `code/`. They are superseded by `embedding_under_E_verification.py` + `ring_lemma_verification.py`, which carry the same octonion arithmetic AND the corrected det. The directional-derivative functionality attributed to `rho_directional_derivatives.py` is available via `polarize_d`. **The roadmapper should confirm file provenance and not assume the prompt's filenames exist verbatim. The stale v16.0 METHODS in this file pointed to `code/octonion_algebra.py` — now the KNOWN-BUGGY reference; do not regress to it.**

## Installation

```bash
# Already satisfied in the executor venv (confirmed this session):
#   sympy 1.14.0, numpy 2.4.2  (sympy.diffgeom imports cleanly)
# No new packages required. NO Sage/GAP/Singular/Magma (not available, not needed).
python3 -c "import sympy, numpy; from sympy.diffgeom import metric_to_Riemann_components; print('ok')"
```

## Sources

- **Totaro, B. (2004), "The curvature of a Hessian metric," arXiv:math/0401381** — THE closed-form curvature of a Hessian metric: Γ_ijk = f_ijk/2, R_ijkl = −(1/4) g^{pq}(f_jlp f_ikq − f_ilp f_jkq); curvature depends only on 3rd derivatives; warped-product Lemma 2.1 relating cone curvature to the {f=1} hypersurface; cites O'Neill [25] for the pseudo-Riemannian machinery. (HIGH — read in full this session.)
- **Faraut, J. & Korányi, A. (1994), *Analysis on Symmetric Cones*, Oxford Math. Monographs (ISBN 9780198534778)** — the cone metric g_X = Hess(−log det), positive-definite; g_X(A,B) = (P(X)^{-1}A \| B); ∇(−log det) = −P(X^{-1}); symmetric-space structure G/K = Str(V)/Aut(V). (HIGH.)
- **O'Neill, B. (1983), *Semi-Riemannian Geometry with Applications to Relativity*, Academic Press** — Gauss-Codazzi for pseudo-Riemannian submanifolds, second fundamental form, induced-metric curvature (Method 2). (HIGH; Totaro's reference [25].)
- **Shima, H. (2007), *The Geometry of Hessian Structures*, World Scientific** — Hessian metrics, dually-flat structures, Hessian sectional curvature; the general theory behind Method 3. (HIGH.)
- **McCrimmon, K. (2004), *A Taste of Jordan Algebras*, Springer** — Peirce decomposition, cubic norm, quadratic representation P(X) = 2L(x)² − L(x²) (needed for the closed-form g^{pq}). (HIGH.)
- **Garibaldi, S. & Guralnick, R. (orbit dimensions of exceptional groups); Derksen, H. & Kemper, G., *Computational Invariant Theory*** — generic orbit dimension = rank of the infinitesimal action at a generic point (char 0), the basis for Method 5. (HIGH; already validated in-repo via `orbit_dimension_gate.py`.)
- SymPy 1.14.0 documentation, `sympy.diffgeom` (`metric_to_Christoffel_2nd`, `metric_to_Riemann_components`) — https://docs.sympy.org/latest/modules/diffgeom.html (HIGH; API verified this session, 2D-sphere benchmark passes).
- Koszul-Vinberg canonical metric = Hess(−log φ), φ the characteristic function; for symmetric cones φ ∝ (det)^{−n/r} so −log φ = (n/r) log det + const (same metric up to scale) — Barbaresco (2019); MDPI Entropy 18(11):383. (MEDIUM; corroborates that −log det is the canonical cone potential.)
- Visser, M. (2017), arXiv:1702.05572; "admissible complex metrics," arXiv:2406.06047 — Wick-rotation hazards, cited only to JUSTIFY preferring construction (ii) over (i). (MEDIUM; contrast/caution, not load-bearing.)
- Contrast only (NOT used): Jacobson (1995), "Thermodynamics of Spacetime," gr-qc/9504004 — the ensemble route explicitly rejected by the milestone.

---

_Methods research for: gravity as intrinsic curvature of the h_3(O) symmetric-cone bulk geometry (Lorentzian V_0 = h_2(O) slice)._
_Researched: 2026-05-30_
