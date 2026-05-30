# Requirements: v17.0 — Gravity as Intrinsic Curvature of the h_3(O) Bulk Geometry

**Defined:** 2026-05-30
**Core Research Question:** Can the Standard Model + GR be derived from the requirement that a composite system faithfully models itself? — v17.0 attacks the GR half via a fresh, intrinsic route.
**Milestone question:** With a primitive idempotent E_11 fixed, does the spacetime Peirce slice V_0 (and its h_2(C_u) ~ R^{3,1} sub-slice) inherit a genuinely POSITION-DEPENDENT metric g_mu_nu(x) from the symmetric-cone bulk metric g_X = Hess(-log det X), and is its curvature SOURCED by matter M in V_1+V_{1/2} via the cubic-norm cross-terms — up to Einstein structure G_mu_nu = kappa T_mu_nu + Lambda g_mu_nu? A cheap homogeneity KILL test decides survival first.

**Structure:** gated A0 → A (homogeneity KILL) → B (matter-sourcing) → C (Einstein). Phase A is cheap and decisive; if it shows the slice metric is homogeneous, the route is DEAD and B/C are not executed (a clean valuable KILL). No lattice, no posited Lagrangian, no SUSY, no ensemble argument.

## Primary Requirements

### Setup & Conventions (foundation for all geometry; A0)

- [ ] **SETU-01**: Reconcile the three in-repo cubic-norm cross-term conventions on genuinely NON-associative (e_4..e_7) octonionic data; certify `code/ring_lemma_verification.py` `det_3` as the single source of truth (Cayley-Hamilton + multiplicativity + F_4-invariance); stand up `code/bulk_geometry_verification.py` by copying/extending that engine. Do NOT import `code/octonion_algebra.py` (carries the old `2Re((x1 x2) x3)` bug, float-only; measured 0.67 associator gap).
- [ ] **SETU-02**: State the A0 signature bridge — construction (ii): background Lorentzian eta from h_2(C_u)'s own det + cone-Hessian perturbation h_mu_nu — and verify it reduces to EXACT Minkowski eta_mu_nu (signature (1,3)) at (M=0, center I/3). (Construction (i), Wick-rotate via u=e_7, is the rejected alternative; report which is used and why.)

### Derivations (DERV)

- [ ] **DERV-01**: Build the inherited slice metric g_mu_nu(x) = eta_mu_nu + h_mu_nu(x) on V_0 with E_11 fixed — exact-over-Q expansion of g_X = Hess(-log det) around X = I/3 in the V_0 (and h_2(C_u)) directions; metric inverse via the quadratic representation g^{pq} = P(X) (Faraut-Koranyi).
- [ ] **DERV-02**: Compute the Riemann/Ricci tensor of g_mu_nu(x) via Totaro's Hessian-curvature formula R_ijkl = -(1/4) g^{pq}(f_jlp f_ikq - f_ilp f_jkq) (depends only on third derivatives of det; det is cubic so this is exact and cheap). [Phase B; only if A survives]
- [ ] **DERV-03**: Construct a candidate stress-energy T_mu_nu from the V_1/V_{1/2} cross-term content of M, defined INDEPENDENTLY of any assumed Einstein form (no GST/SUSY/-R/2/Weinberg input). [Phase C; only if B survives]

### Calculations (CALC)

- [ ] **CALC-01**: Compute dim Stab_{E_6}(E_11) and the dimension of the (basepoint, slice) family modulo that stabilizer (reuse `code/orbit_dimension_gate.py`, exact-over-Q ranks); decide whether the residual symmetry acts transitively enough to make all (basepoint, slice) pairs isometric. [Phase A]
- [ ] **CALC-02**: Determine whether the V_0 slice is totally geodesic (second fundamental form II = 0) in the cone — a cheap potential KILL (II=0 ⇒ R^slice = ambient constant curvature ⇒ homogeneous). [Phase A]
- [ ] **CALC-03**: Cross-term on/off test — compute the slice Riemann tensor with the FULL cubic norm vs det replaced by the block-diagonal product det(V_1)*det(V_0), at the same M != 0 (place M so the triple product is non-vacuous). [Phase B]
- [ ] **CALC-04**: Quantify the curvature scale as a function of ||M|| and the off-center parameter rho_J(X_bg) (series-expand in matter amplitude; substitute matter to rationals before any symbolic inverse). [Phase B]
- [ ] **CALC-05**: Compare G_mu_nu[g(x)] against kappa T_mu_nu + Lambda g_mu_nu at exact order and at linear order in M, with kappa and Lambda fit only as GLOBAL constants (not per-point), over an (M, x) family. [Phase C]

### Validations (VALD)

- [ ] **VALD-01**: Phase-A homogeneity verdict from exact-over-Q curvature-SCALAR INVARIANTS evaluated at distinct basepoints (NOT raw metric components, NOT a single basepoint) — cross-checked against the CALC-01 stabilizer-transitivity count. DECISIVE: position-dependent ⇒ SURVIVES; x-independent ⇒ KILL (report without softening).
- [ ] **VALD-02**: Reduce-to-Minkowski — g_mu_nu(center, M=0) = eta_mu_nu exactly, zero residual h_mu_nu (gates SETU-02 / the whole construction).
- [ ] **VALD-03**: h_2(C_u) sub-slice limiting case — the det=1 hyperboloid is H^3 = SL(2,C)/SU(2) with constant negative curvature (independent geometric cross-check of the bulk machinery).
- [ ] **VALD-04**: Center baseline — at M=0 the slice curvature is flat or a pure cosmological constant (the irreducible symmetric space is Einstein with negative Lambda, Cartan); distinguish this pure-Lambda background from genuine M-sourced curvature. [Phase B]
- [ ] **VALD-05**: Circularity audit — a per-equation independence check confirming T_mu_nu (DERV-03), kappa, and the Einstein test (CALC-05) use NO supergravity multiplet data, GST Lagrangian, SUSY closure, or Weinberg soft-graviton input. [Phase C]

## Follow-up Requirements

Deferred; tracked but not in the v17.0 roadmap.

### Extended Analysis

- **EXTD-01**: Full dim-10 V_0 = h_2(O) curvature (the decisive physics is on the 4-dim h_2(C_u) slice; the dim-10 symbolic inverse times out — mpmath high-precision fallback only if needed).
- **EXTD-02**: Solving / interpreting the matter field equations for M (dynamics), beyond treating M as a fixed background source.
- **EXTD-03**: If C succeeds, the precise non-compact stabilizer of a primitive idempotent in E_6(-26) (expected parabolic with Spin(9,1) Levi) and its role in the gravitational interpretation.
- **EXTD-04**: Paper integration / write-up of the result (positive, KILL, or curved-but-not-Einstein).

## Out of Scope

| Topic | Reason |
| ----- | ------ |
| Lattice/Fisher continuum-limit route | ABANDONED (`paper6-continuum-limit-prompt.md`); the lattice is a modeling choice reviewers reject — do not import |
| det/GST/Weinberg N=2 supergravity-Lagrangian route | CIRCULAR (the -R/2 is fixed by the assumed SUSY closure); do not import as load-bearing — GST scalar-manifold geometry citable for GEOMETRY ONLY |
| Observers-make-gravity ensemble / thermodynamic argument | Explicitly rejected (Jacobson 1995 = contrast only); one observer, one off-center point, the algebra's own geometry |
| Quantizing gravity; cosmology | Beyond this milestone's classical-curvature scope |
| Re-deriving the SOLID standard math (cone structure, OP^2 = F_4/Spin(9), h_2(C_u) ~ R^{3,1} Minkowski) | Cite, do not re-derive (Faraut-Koranyi, Baez, Springer) |
| Retroactively retracting the v12.0/v13.0 det/GST gravity result | INDEPENDENT fresh route; the milestone outcome decides which route stands |

## Accuracy and Validation Criteria

| Requirement | Accuracy Target | Validation Method |
| ----------- | --------------- | ----------------- |
| SETU-01 | EXACT (det_3 matches certified engine; associator-sensitive triple correct) | Cayley-Hamilton + multiplicativity on non-associative (e_4..e_7) data; compare 3 conventions |
| SETU-02 / VALD-02 | EXACT Minkowski, zero residual | Symbolic g_mu_nu(center, M=0) == diag Minkowski over Q |
| DERV-01, DERV-02 | EXACT over Q | Hand-rolled Christoffel/Riemann (faster than diffgeom); 4-dim slice ~19s exact |
| CALC-01 | EXACT integer dimensions | exact-over-Q matrix rank (reuse orbit_dimension_gate.py); reproduce single-copy orbit 24/Spin(8) first |
| VALD-01 (KILL gate) | EXACT — curvature invariants equal vs differ across basepoints | exact-over-Q curvature scalars at >=2 basepoints + stabilizer count agree |
| CALC-03, CALC-04 | EXACT over Q (matter rational) | full det vs block-diagonal det; series in ||M|| |
| CALC-05 | EXACT and linear-in-M | global-constant fit over an (M,x) family; reject single-point tuning |
| VALD-03, VALD-04 | Constant curvature (H^3); Einstein/pure-Lambda (center) | known symmetric-space curvature; Cartan |

## Contract Coverage

| Requirement | Decisive Output / Deliverable | Anchor / Benchmark / Reference | False Progress To Reject |
| ----------- | ----------------------------- | ------------------------------ | ------------------------ |
| SETU-01 | certified det_3 engine | ring_lemma_verification.py (CH + 324/324); h3o_tower.py 2Re(x2* x0* x1) | the buggy 2Re((x1 x2) x3) / float det |
| SETU-02, VALD-02 | signature bridge + Minkowski reduction (claim-signature-bridge) | 52-kkt-spacetime (h_2(C_u) Minkowski); test-minkowski-reduction | bridge not reducing to exact Minkowski |
| DERV-01, CALC-01/02, VALD-01 | homogeneity verdict (claim-homogeneity, THE KILL GATE) | Faraut-Koranyi; Kollross-Rodriguez-Vazquez 2022; Totaro; orbit_dimension_gate.py | relabel homogeneous as "approx position-dependent"; coordinate artifact as curvature; float ranks |
| DERV-02, CALC-03/04, VALD-04 | matter-sourcing (claim-matter-sourcing) | Totaro 3rd-deriv formula; test-cross-term-onoff | pure-Lambda (M=0) counted as matter-sourcing |
| DERV-03, CALC-05, VALD-05 | Einstein-structure level (claim-einstein-structure) | GST geometry-only; test-einstein-level | importing GST/SUSY/Weinberg; assuming/tuning Einstein form |

## Traceability

Suggested mapping (roadmapper finalizes; phases continue at 70). The Phase-A KILL gate may terminate the milestone before B/C.

| Requirement | Phase (suggested) | Status |
| ----------- | ----------------- | ------ |
| SETU-01 | Phase 70 (A0: setup + bridge) | Pending |
| SETU-02 | Phase 70 (A0) | Pending |
| VALD-02 | Phase 70 (A0) | Pending |
| VALD-03 | Phase 70 (A0) | Pending |
| DERV-01 | Phase 71 (A: homogeneity) | Pending |
| CALC-01 | Phase 71 (A) | Pending |
| CALC-02 | Phase 71 (A) | Pending |
| VALD-01 | Phase 71 (A — KILL gate) | Pending |
| DERV-02 | Phase 72 (B: matter-sourcing) | Pending |
| CALC-03 | Phase 72 (B) | Pending |
| CALC-04 | Phase 72 (B) | Pending |
| VALD-04 | Phase 72 (B) | Pending |
| DERV-03 | Phase 73 (C: Einstein) | Pending |
| CALC-05 | Phase 73 (C) | Pending |
| VALD-05 | Phase 73 (C) | Pending |

**Coverage:**

- Primary requirements: 15 total (2 SETU, 3 DERV, 5 CALC, 5 VALD)
- Mapped to phases: 15 (suggested)
- Unmapped: 0

---

_Requirements defined: 2026-05-30_
_Last updated: 2026-05-30 after v17.0 initial definition (literature survey complete; roadmap pending)_
