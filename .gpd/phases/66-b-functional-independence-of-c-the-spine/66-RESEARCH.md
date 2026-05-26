# Phase 66: (b) Functional Independence of c -- THE SPINE - Research

**Researched:** 2026-05-26
**Domain:** Computational invariant theory of F_4 = Aut(h_3(O)) acting diagonally on 27 (+) 27; exact-over-Q Jacobian-rank / orbit-derivative functional-independence proof
**Confidence:** HIGH (method, machinery inventory, conventions, pitfalls); the OUTCOME is pre-decided by the Phase-65.1 r7==7 preview but must be re-demonstrated by both routes independently in this phase.

## Summary

This phase is the single load-bearing result of milestone v16.0. It demonstrates, by exact computation over Q on the actual non-associative Albert algebra h_3(O), whether the coupling `c = Tr(X o Y)` is functionally (= algebraically, in char 0) independent of the six pointwise generators `{Tr X, Tr X^2, det X, Tr Y, Tr Y^2, det Y}`. The verdict is exactly one of: **rank 7** (c INDEPENDENT, positive pass) or **rank 6** (c DEPENDENT / expressible in the pointwise ring, decisive NEGATIVE, also a full pass). Both branches must be reported honestly; a NEGATIVE must ship the explicit pointwise expression for c.

The phase is a **continuation** of a fully-instrumented, frozen exact-over-Q pipeline (Phases 64/65/65.1). Almost all machinery already exists and is CERTIFIED: the 52-generator f_4 = Der(h_3(O)) basis, the exact width-54 rank `exact_qq_rank`, the 7 base invariants as SymPy expressions on a 54-symbol layout, the ordered 10-candidate Jacobian builder, and `prefix_rank(k, point_pair)` which **already computed r6==6 and r7==7 as a Phase-66 SPINE preview** (Phase 65.1, committed). The genuinely NEW content of this phase is **Route 2**: an infinitesimal orbit-derivative *separating-direction* argument that confirms rank 7 (or its failure) **independently of the Jacobian**, satisfying the reward-hacking guard that demands two agreeing routes.

The two routes are: (Route 1) the exact 7x54 sub-Jacobian rank over Q at >= 3 generic rational points (Derksen-Kemper char-0 criterion: trdeg = generic Jacobian rank); (Route 2) exhibit an f_4 direction xi along the F_4-orbit of X on which every pointwise generator has zero derivative while c has nonzero derivative. Both must agree before any verdict is reported. A critical consistency correction (ITEM 4a) applies: the roadmap's success-criterion-5 language "rank 7 saturates trdeg" is STALE -- Phase 65 computed pair orbit dim = 44 => trdeg = 10, so rank 7 saturates only the `{6 pointwise + c}` SUBSET (a 7x54 matrix has rank <= 7) and is CONSISTENT with (7 <= 10), but does NOT saturate the full transcendence degree.

**Primary recommendation:** REUSE the frozen machinery verbatim (do NOT rebuild the engine). Build the 7x54 sub-Jacobian by slicing `CANDIDATE_GRADS[0:7]`; reuse `exact_qq_rank`, `PAIR_POINTS`, and the genericity gates from `ring_generating_set.py`. Implement Route 2 as a new function reusing the certified f_4 basis (`_select_independent_basis`) and the 54-wide diagonal contraction pattern from `check_f4_invariance`. Pre-register the points and the exact rank test BEFORE evaluating. Adjudicate: report a verdict ONLY if both routes agree.

## User Constraints

No CONTEXT.md exists for this phase (no `/gpd:discuss-phase` was run). The binding constraints come from the ROADMAP success criteria and the project research (`.gpd/research/SUMMARY.md`, `PITFALLS.md`):

- **LOCKED method:** exact SymPy over Q; ranks via `exact_qq_rank` (DomainMatrix-over-QQ) -- NEVER `numpy.linalg.matrix_rank` / float64 on the decisive path. This is the GLOBAL forbidden proxy.
- **LOCKED group/conventions:** F_4 = Aut(h_3(O)) (NOT E_6); `jordan = (1/2)(AB+BA)`; `c = Tr(X o Y)`; `det_3` cross-term `(x2 x1) x3` (Phase-64.1 factor-order fix); `f4 = span{[L_a,L_b]}` dim 52. All frozen in the ASSERT_CONVENTION line.
- **LOCKED dual-route requirement:** BOTH the Jacobian rank AND the infinitesimal orbit-derivative argument are mandatory (reward-hacking guard). No verdict unless they agree.
- **LOCKED honesty discipline:** a rank-6 NEGATIVE is a full pass and must be reported with a constructed explicit P; pre-register the test so a positive cannot be forced over an honest negative.
- **OUT OF SCOPE (deferred to later phases):** ring generation / Hilbert series / Krull-dimension completeness (Phase 68); the (c) degree-2 uniqueness Sym^2 branching (Phase 67); (REDUCIBILITY) dynamical bridge. This phase is the FIELD-level functional-independence of c ONLY.

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| ----------------- | ---- | ------------------- | --------------- | ---------------------- |
| `code/ring_generating_set.py` (Phase 65.1) | Prior artifact (FROZEN) | Holds the ordered 10-candidate list (first 7 = the SPINE set in fixed order), `CANDIDATE_GRADS`, `candidate_jacobian_matrix_at`, `prefix_rank`, `PAIR_POINTS`, and the already-computed r6==6 / r7==7 preview | REUSE verbatim; slice first-7 for Route 1; reuse genericity gates | Plan (Route-1 tasks), Execution, Verification |
| `code/orbit_dimension_gate.py` (Phase 65, CERTIFIED) | Prior artifact (FROZEN) | The 52-gen f_4 basis builder, `exact_qq_rank`, `infinitesimal_action`, `_select_independent_basis`, `PAIR_POINTS`, single-copy GATE (orbit 24/Spin(8)/trdeg 3) reproduced | REUSE the f_4 basis + `exact_qq_rank` + `infinitesimal_action` for Route 2 | Plan (Route-2 tasks), Execution, Verification |
| `code/ring_lemma_verification.py` ("warm exact engine", as module `E`) | Prior artifact (FROZEN) | Octonion + h_3(O) primitives: `jordan`, `Tr`, `Tr2`, `det_3`, `c(X,Y)`, `Xsym/Ysym`, `xs/ys`, `X_from_symbols`, `jordan_L_matrix`, `inner_derivations`, `octonionic_points`, the 7 `inv_*` invariants | REUSE all primitives; build the trace form `Tr(A o B)` from `Tr(jordan(A,B))` | Plan, Execution |
| Derksen-Kemper, *Computational Invariant Theory* (2nd ed., Springer 2015), Jacobian-criterion section | Method (canonical) | Licenses "trdeg = generic Jacobian rank" in char 0 -- THE theorem behind Route 1 | CITE in plan + write-up | Plan, Verification |
| Garibaldi-Guralnick arXiv:2105.09486 (also 2308.08214) Lemma 8.1 | Benchmark (HIGH) | Single-copy F_4-on-26 generic stabilizer Spin(8), orbit 24, trdeg 3 -- already reproduced by the certified gate; grounds the r6==6 cross-check (3 X-block + 3 Y-block) | CITE; r6==6 is the in-phase corroboration | Plan, Verification |
| Springer-Veldkamp, *Octonions, Jordan Algebras and Exceptional Groups* (2000); Springer 1973 | Method/benchmark (HIGH) | F_4 = automorphisms preserving Tr and the cubic norm => the trace form `Tr(X o Y)` is F_4-invariant and non-degenerate on the 26; this is what makes the Route-2 pairing `xi -> Tr((xi.X) o Y)` generically nonzero | CITE in Route-2 formalization | Plan, Execution |
| Schafer, *An Introduction to Nonassociative Algebras* (1966) | Method (HIGH) | `Der(h_3(O)) = f_4`; the inner-derivation formula `D_{a,b} = [L_a, L_b]` -- grounds the f_4 builder | CITE | Plan |
| Phase 65 SUMMARY (pair orbit 44 => trdeg 10) | Prior result (HIGH) | The corrected trdeg target; the basis of the ITEM-4a consistency reframing | READ; use trdeg=10 (NOT 7) in the consistency statement | Plan (consistency task), Verification |
| Phase 65.1 SUMMARY (rank-10 set; r6=6, r7=7 preview) | Prior result (HIGH) | States the SPINE preview already holds AND the ITEM-4a correction verbatim ("rank 7 no longer saturates trdeg; (b) unaffected/strengthened") | READ; re-demonstrate r7==7 here as the phase's own decisive result | Plan, Verification |

**Missing or weak anchors:** None missing. NOTE that the f_4-builder's only *external* literature anchor is the single-copy Spin(8) value (the pair orbit dim 44 is a computed number with no textbook to check against) -- but that anchor is upstream (Phase 65, CERTIFIED) and is NOT re-litigated here; this phase consumes it. The ONE stale anchor is ROADMAP success-criterion-5's "= 54 - orbit_dim = 7 saturates trdeg" wording -- explicitly corrected in ITEM 4a / the Consistency section below.

## Conventions

| Choice | Convention | Alternatives | Source |
| ------ | ---------- | ------------ | ------ |
| Arithmetic field | Exact over Q (SymPy `Rational`) | floats | ASSERT_CONVENTION (all 3 modules) |
| Rank | `exact_qq_rank(A) = DomainMatrix.from_Matrix(A).convert_to(QQ).rank()` | `Matrix.rank()` (correct but unusably slow at width 54); `numpy.linalg.matrix_rank` (FORBIDDEN) | `orbit_dimension_gate.py:154` |
| Group | F_4 = Aut(h_3(O)), 52-dim; fixes Tr, trace form, det | E_6 = Stab(det) -- WRONG group (c is not E_6-invariant) | SUMMARY; Springer-Veldkamp |
| Jordan product | `X o Y = (1/2)(XY + YX)` (`jordan(A,B)`) | — | ASSERT_CONVENTION |
| Coupling | `c = Tr(X o Y) = Tr(jordan(Xsym, Ysym))` (`E.inv_c`); bidegree (1,1); `c(X,X) = Tr X^2` (Lock 2) | `Tr(X)Tr(Y)` is the *reducible* (1,1) product, NOT c | `ring_lemma_verification.py:350` |
| Cubic norm | `det_3`, cross-term `(x2 x1) x3` (x2 BEFORE x1) | the Phase-64 bug `(x1 x2) x3` -- NOT F_4-invariant (killed by only 30/324 inner derivs) | `ring_lemma_verification.py:308`, Phase 64.1 |
| f_4 basis | `span{[L_a,L_b]}`, 52-independent rref subset of the 324 inner derivations | full 324 (same rank, slower) | `orbit_dimension_gate.py:405` |
| Coordinate layout | 54 symbols `xs = x0:27`, `ys = y0:27`; `[alpha,beta,gamma, x1(8), x2(8), x3(8)]` per copy | Peirce-adapted (a deliberate Phase-65 alt; does not affect invariants) | `ring_lemma_verification.py:389` |
| Generic point | integer/rational, all-nonzero, distinct diagonals (distinct spectra), X NOT proportional to Y, X != Y | X=Y, X prop Y, repeated spectra -- DROP the rank (forbidden as independence-test points) | `orbit_dimension_gate.py:581`, PITFALLS P4 |
| Aggregator over points | MAX over >= 3 generic points (rank is lower-semicontinuous: a special point can only UNDER-report) | min, single point | `orbit_dimension_gate.py:379` |

**CRITICAL: All equations and the verdict below use these conventions.** The `det_3` factor order and the `jordan` 1/2 are LOAD-BEARING; a port slip silently corrupts the rank. The project metric is Riemannian Fisher (pure algebra; no field theory / gauge / Fourier -- those convention fields are `na`).

Convention loading: see agent-infrastructure.md Convention Loading Protocol.

## Reusable-Machinery Inventory (NEW vs REUSABLE)

The planner must REUSE, never rebuild. Module aliases as in the existing code: `E = ring_lemma_verification`; the gate functions are imported from `orbit_dimension_gate`; the candidate machinery lives in `ring_generating_set`.

### What is REUSABLE (frozen, certified)

| Piece needed in Phase 66 | Existing function (file:role) | Status |
| ------------------------ | ----------------------------- | ------ |
| (a) The 7x54 sub-Jacobian rows | `ring_generating_set.CANDIDATE_GRADS[0:7]` (the first 7 cached 54-var gradients = 6 pointwise + c, in FIXED order) -- or `prefix_rank(7, pp)` directly | REUSABLE verbatim |
| 7x54 Jacobian matrix at a point | `candidate_jacobian_matrix_at(point_pair)` restricted to first 7 rows; or build via `CANDIDATE_GRADS[:7]` subbed at the point | REUSABLE (slice) |
| (b) The 6x54 pointwise baseline | `prefix_rank(6, point_pair)` (first 6 gradients = the pointwise sextet) | REUSABLE verbatim |
| Exact width-54 rank | `orbit_dimension_gate.exact_qq_rank(A)` (DomainMatrix-over-QQ; the anti-float guard) | REUSABLE verbatim |
| (c) The f_4 basis for Route 2 | `ring_generating_set._f4_basis()` -> `orbit_dimension_gate._select_independent_basis(E.inner_derivations())` (52 indep 27x27 rational matrices) | REUSABLE verbatim |
| (c) Single-copy infinitesimal action xi.v | `orbit_dimension_gate.infinitesimal_action(grad_at, M, v)` = sum_i grad_at[i]*(M.v)[i]; and the raw tangent `M * v` | REUSABLE (also used raw) |
| (d) The trace form Tr(A o B) | `E.Tr(E.jordan(A, B))` (this IS c when A=X, B=Y); `E.inv_c = c(Xsym, Ysym)` | REUSABLE |
| (e) Exact rank (anti-float) | `exact_qq_rank` (above) | REUSABLE |
| Generic pair points | `orbit_dimension_gate.PAIR_POINTS` (4 generic integer pairs: P1xP2, P2xP3, P1xP3, P4xP5; all distinct, non-proportional, distinct diagonals) | REUSABLE verbatim |
| Genericity guard | `orbit_dimension_gate._pair_not_proportional(X,Y)`; `_is_genuinely_octonionic_integer(v27)` | REUSABLE verbatim |
| 7 base invariants / symbols | `E.inv_Tr_X, E.inv_Tr2_X, E.inv_det_X, E.inv_Tr_Y, E.inv_Tr2_Y, E.inv_det_Y, E.inv_c`; `E.xs, E.ys`, `E.Xsym, E.Ysym`; `E.X_from_symbols`, `E._flat27` | REUSABLE verbatim |
| Three-exact-domain cross-check | `orbit_dimension_gate.exact_rank_route_crosscheck(basis, X, Y)` (QQ-frac == QQ-int == ZZ-int) | REUSABLE (apply to the 7x54) |
| r6==6 / r7==7 preview | `ring_generating_set.check_tier_increments` / `prefix_rank` ALREADY computed these | REUSABLE as corroboration |

### What is NEW in Phase 66

| New piece | Why new | Build from |
| --------- | ------- | ---------- |
| **Route 2: orbit-derivative separating-direction test** (PRIMARY new content) | Phase 65.1 only ran the Jacobian route + a single `two_route_precheck` against the orbit-derived trdeg; it never computed, *per generator*, the directional derivative of c vs the pointwise sextet along orbit tangents. THIS is the second independent route. | NEW function reusing the f_4 basis + the 54-wide diagonal-contraction pattern from `check_f4_invariance` (`ring_generating_set.py:236`); see ITEM 1 recipe |
| **The separating-vector `s = (s_1,...,s_52)`** with `s_i = Tr((xi_i . X) o Y)` | Not previously computed | `E.jordan`, `E.Tr`, the f_4 basis acting on X-coords (`M * v_x`), reconstructed via `E.X_from_symbols` |
| **Two-routes-must-agree adjudicator** | `two_route_precheck` is a consistency print, not a verdict gate; Phase 66 needs a function that emits a verdict ONLY when route1_rank and route2 agree (rank 7 <=> separating xi exists; rank 6 <=> no separating xi) | NEW thin wrapper |
| **NEGATIVE-branch constructor** (conditional, almost certainly a no-op) | If rank were 6, solve `c - a*(Tr X)(Tr Y) = 0` over Q (the only matching-bidegree pointwise product) | NEW; linear-algebra-over-Q, see ITEM 4b |
| **The corrected consistency statement** (rank 7 <= trdeg 10) | ROADMAP criterion 5 is stale | NEW prose/assert; see ITEM 4a |
| **7x54 sub-Jacobian rank-stability across >= 3 points as a standalone phase deliverable** | Phase 65.1 computed it as a by-product (`prefix_rank(7,.)`); Phase 66 makes the per-point stability an explicit pre-registered SPINE assertion | REUSE `prefix_rank(7, pp)` for each `pp`, assert SAME at all |

## Route 1 (Jacobian) -- Recipe

**Theorem licensing it (ITEM 2):** Derksen-Kemper char-0 Jacobian criterion -- for polynomials f_1,...,f_m on affine space over a field of characteristic 0, `trdeg_Q Q(f_1,...,f_m) = max rank of the Jacobian [d f_i / d x_j]` over the variety, equivalently the rank at a generic (dense-open) point. Hence the 7x54 Jacobian rank == `trdeg Q(Tr X, Tr X^2, det X, Tr Y, Tr Y^2, det Y, c)`; **rank 7 <=> the 7 are algebraically (hence functionally) independent <=> c is NOT in the algebraic closure of the 6 pointwise**, i.e. `c not-in R_pt`. (Derksen-Kemper, *Computational Invariant Theory*, 2nd ed. 2015; standard, char-0 caveat vacuous.) Note the gate already INVOKES this theorem for the orbit-dimension route (`orbit_dimension_gate.py:343`).

**"Functional independence" = "algebraic independence" here.** In char 0, for polynomial invariants of a reductive group, algebraic independence is the right and exactly-checkable notion; by Schwarz-Luna a smooth invariant is a smooth function of the polynomial generators, so "c is not a polynomial in the six" upgrades to "c is not a smooth function of the six" if needed. This is precisely "the single-frame (third-person) record does not determine Phi": the six pointwise invariants ARE the complete single-copy record of X and of Y separately; c is the cross-frame coupling.

**Steps (REUSE):**

1. Pre-register: fix the points (`PAIR_POINTS`, all generic by `_pair_not_proportional` + distinct diagonals) and the exact rank test (`exact_qq_rank`) BEFORE evaluating. Record `TRDEG_TARGET`-style constants so the verdict cannot be re-rolled.
2. **7x54 sub-Jacobian:** rows = `CANDIDATE_GRADS[0:7]` (6 pointwise + c, fixed order), each a 54-var gradient `[d f / d z for z in xs+ys]`. Substitute the integer point FIRST (per the `_gradients_in_X` swell-control pattern), then `exact_qq_rank`. Equivalent shortcut: `prefix_rank(7, pp)`.
3. **6x54 baseline control:** `prefix_rank(6, pp)` -- MUST be exactly 6 at every generic point (the pointwise sextet is the single-copy 3 X-block + 3 Y-block, trdeg 3+3=6; Garibaldi-Guralnick). If != 6, the engine/builder is broken -- STOP, do not tune.
4. **Rank stability:** compute `prefix_rank(7, pp)` at EACH of >= 3 generic pairs; assert the SAME rank at every point. Take MAX as the generic value (rank lower-semicontinuous; a single unlucky point can only DROP it). The verdict is `MAX = 7` (independent) or `MAX = 6` (dependent).
5. **X=Y degeneracy control:** evaluate `prefix_rank(7, (P, P))` at a diagonal pair -- must give <= 6, confirming X=Y is NOT a valid independence-test point (it collapses c to Tr X^2 in R_pt). This is a *control that should fail to reach 7*, not a counterexample.
6. **Exactness cross-check:** run `exact_rank_route_crosscheck` on the 7x54 at one pair (QQ-frac == QQ-int == ZZ-int) to certify `exact_qq_rank` is genuinely exact at this width, not a float proxy.

**Known difficulties:** det_3 (deg 3) and the 54-var gradients swell if `simplify`d symbolically -- ALWAYS substitute the rational point first (the cached `CANDIDATE_GRADS` are deliberately NOT simplified). The single non-generic-point risk is fully covered by >= 3 points + MAX + the explicit X=Y control.

**Expected result (from the committed Phase-65.1 preview):** `prefix_rank(6,.) == 6`, `prefix_rank(7,.) == 7` -- i.e. **rank 7, c INDEPENDENT (positive)**. Phase 66 re-runs this as its own decisive, pre-registered result (not merely citing the preview).

## Route 2 (Orbit-Derivative) -- Full Formalization + Recipe (ITEM 1, the NEW content)

### The argument (rigorous statement)

Let `O_X = F_4 . X` be the F_4-orbit of X. Its tangent space at X is `T_X O_X = {xi . X : xi in f_4}` (the infinitesimal action; for the 27x27 generator matrix `M_xi`, the tangent is `M_xi . v_x` on coordinates).

- **Pointwise X-invariants are constant on the orbit.** `Tr X, Tr X^2, det X` are F_4-invariant (the certified gate verified `D_M f = 0` for all 324 generators, all three), hence constant on `O_X`, hence their directional derivative along ANY `xi . X` is identically 0.
- **Pointwise Y-invariants have zero derivative trivially** because we move ONLY X (delta Y = 0): `Tr Y, Tr Y^2, det Y` do not depend on X.
- **The derivative of c along `xi . X`** is `D_xi c = Tr((xi . X) o Y)` (linear in the X-argument; Y held fixed). This is exactly the trace-form pairing of the orbit tangent `xi.X` against Y.

**Claim:** for generic rational X, Y there exists `xi in f_4` with `Tr((xi . X) o Y) != 0`.

**Logical bridge (verify AIRTIGHT):** Suppose, for contradiction, `c = P(Tr X, Tr X^2, det X, Tr Y, Tr Y^2, det Y)` for some smooth/polynomial P (i.e. `c in R_pt`). Then along the curve `t -> exp(t xi).X` (fixed Y), every argument of P is constant, so `c` would be constant on `O_X x {Y}`, giving `d/dt|_0 c = 0` for ALL `xi`. But we exhibit a single `xi` with `D_xi c = Tr((xi.X) o Y) != 0`. Contradiction. Therefore `c not-in R_pt` -- c is functionally independent of the six pointwise generators. QED.

**Genericity hypothesis it needs (state explicitly):**
- `dim O_X > 0`, i.e. there exists a NONZERO tangent `xi.X` to test against. The certified single-copy gate gives generic single-copy orbit dim = 24 > 0, so a generic X has a 24-dimensional orbit -- abundant nonzero tangents. (This is what "dim O_X > 0 buys": the orbit is positive-dimensional, so the separating-direction search is over a nontrivial space, not the zero tangent.)
- X, Y JOINTLY generic in the Route-1 sense (all-nonzero, distinct spectra, X not proportional to Y, X != Y). Genericity is what guarantees the pairing does not accidentally vanish: the trace form is **F_4-equivariant and non-degenerate** (F_4 = automorphisms preserving Tr and the norm => preserves the trace form; the 26 is self-dual and the form is non-degenerate on it -- Springer-Veldkamp), so `xi -> Tr((xi.X) o Y)` is a nonzero linear functional on f_4 for generic X, Y; only on a measure-zero locus (e.g. Y orthogonal to the entire orbit-tangent space of X under the trace form) does it vanish identically. The exact computation CONFIRMS non-vanishing at the chosen generic points -- it does not assume it.

**Why the non-degeneracy + equivariance is load-bearing:** if the trace form were degenerate or non-invariant, `xi.X` could be nonzero yet pair to 0 with every Y, and the separating direction would not exist even though the orbit is positive-dimensional. F_4-equivariance is exactly what ties the tangent directions to a nonzero pairing.

### Computational recipe (REUSE the f_4 basis + diagonal-contraction pattern)

For each generic rational pair `(X, Y)` in `PAIR_POINTS`:

1. `v_x = Matrix(E._flat27(X))`, `v_y = Matrix(E._flat27(Y))` (integer 27-vectors).
2. f_4 basis: `f4 = _f4_basis()` (52 independent 27x27 rational matrices; reuse `ring_generating_set._f4_basis`).
3. **Separating vector for c:** for each `xi_i = f4[i]` (i = 0..51), compute the orbit tangent `t_i = M_i . v_x` (a 27-vector, = `xi_i . X` in coords), reconstruct `T_i = E.X_from_symbols(list(t_i))`, and the scalar
   `s_i = Tr( (xi_i . X) o Y ) = E.Tr(E.jordan(T_i, E.X_from_symbols(list(v_y))))` -- exact over Q.
   (Equivalently, since c is bilinear, `s_i = grad_X(c) . (M_i . v_x)` evaluated at the point -- this matches the cached `CANDIDATE_GRADS[6]` X-block contraction and is the cheaper route. Use the gradient form for speed; the explicit `Tr(jordan(.,.))` form is the conceptual check.)
4. **Separating-direction exists** iff the vector `s = (s_0,...,s_51)` is NOT all zero. Assert `any(s_i != 0)`. Record which `xi_i` separates (the first nonzero, for the witness).
5. **Confirm the pointwise generators have zero derivative along that same `xi_i`** (and along ALL `xi_i`, since they are orbit-constant):
   - X-pointwise `{Tr X, Tr X^2, det X}`: `D_{xi_i} f = grad_X(f) . (M_i . v_x)` must be exactly 0 for every i. This re-uses `infinitesimal_action(grad_at, M_i, v_x)` with the cached `CANDIDATE_GRADS[0:3]` X-blocks. (The certified gate already proved this for all 324 generators; re-asserting on the 52-basis at the SPINE points is the in-phase witness.)
   - Y-pointwise `{Tr Y, Tr Y^2, det Y}`: derivative along an X-only direction (delta Y = 0) is 0 by inspection -- their X-block gradient is the zero vector. Assert `CANDIDATE_GRADS[3:6]` X-block == 0.
6. **Verdict from Route 2:** separating xi exists AND all 6 pointwise derivatives vanish => c is functionally independent (the POSITIVE). If NO separating xi exists at any generic point (s identically 0) => Route 2 reports DEPENDENT.

**This route is genuinely independent of the 7x54 Jacobian rank.** Route 1 ranks a 7x54 matrix of full gradients; Route 2 asks a different question -- does the trace-form pairing of orbit tangents against Y ever fire while the pointwise gradients are orbit-flat. They are two faces of the Jacobian-criterion/orbit-geometry duality (`trdeg = 54 - orbit_dim`), which is exactly WHY both are demanded as independent confirmations.

**Reuse map:** f_4 basis <- `_select_independent_basis(E.inner_derivations())`; tangent `M.v` and `infinitesimal_action` <- `orbit_dimension_gate`; trace form <- `E.Tr(E.jordan(.,.))`; the 54-wide gradient split [0:27]/[27:54] and the per-generator loop <- `check_f4_invariance` (`ring_generating_set.py:236`); points <- `PAIR_POINTS`.

## Adjudication: Two-Routes-Must-Agree + NEGATIVE Branch

### The reward-hacking guard (mandatory)

Report a verdict ONLY when the two routes agree:

| Route 1 (7x54 rank, MAX over pts) | Route 2 (separating xi) | Verdict | Action |
| --------------------------------- | ----------------------- | ------- | ------ |
| 7 | exists (s != 0) | **c INDEPENDENT (positive pass)** | report rank 7 + the witness xi + s; assert 6x54 baseline == 6 and X=Y control <= 6 |
| 6 | none (s identically 0 at all generic pts) | **c DEPENDENT (decisive NEGATIVE, full pass)** | construct explicit P (below), report it |
| 7 | none | **NO VERDICT -- contradiction** | STOP; a builder/port bug or a non-generic Route-2 point; do NOT report, do NOT tune |
| 6 | exists | **NO VERDICT -- contradiction** | STOP; investigate (likely a non-generic Route-1 point dropping rank, or a Route-2 false positive) |

The off-diagonal cells are the guard: a single route "passing" is insufficient. (Phase 65.1's `two_route_precheck` checked candidate-Jacobian-trdeg == orbit-derived-trdeg globally; Phase 66 needs this finer per-route agreement specifically for the `{6 pointwise + c}` SPINE question.)

### NEGATIVE-branch construction method (ITEM 4b; almost certainly a no-op)

If (contrary to the r7==7 preview) the verdict is rank 6, success criterion 4 requires an explicit polynomial P with `c = P(Tr X, Tr X^2, det X, Tr Y, Tr Y^2, det Y)`. Bidegree pins P down to ONE candidate:

- c has bidegree (1,1). The pointwise generators have bidegrees `Tr X (1,0), Tr X^2 (2,0), det X (3,0), Tr Y (0,1), Tr Y^2 (0,2), det Y (0,3)`.
- The ONLY product of pointwise generators with matching bidegree (1,1) is `(Tr X)(Tr Y)`. (No other combination sums to (1,1): you need exactly one degree-1-in-X factor (only Tr X) and one degree-1-in-Y factor (only Tr Y).)
- So necessarily `P = a * (Tr X)(Tr Y)` for a single rational constant a.

**Linear-algebra-over-Q method to find a (and verify):**
1. Evaluate `c` and `m := (Tr X)(Tr Y)` at >= 2 generic rational pairs; solve `c - a*m = 0` for a (one rational unknown; over-determined => consistency is the check).
2. **Verify the identity, not just the points:** confirm `simplify(E.inv_c - a*E.inv_Tr_X*E.inv_Tr_Y) == 0` as a symbolic identity over Q (or match gradients: `grad(c) - a*grad(m) == 0` at several points). If it holds identically, `c = a*(Tr X)(Tr Y)` and the NEGATIVE is constructed.
3. If NO rational a makes it vanish identically, then c is NOT expressible in the matching-bidegree pointwise product -- which CONTRADICTS a rank-6 finding (rank 6 would force c in R_pt). That contradiction means a Route-1 non-generic-point artifact; STOP and re-examine, do not report.

This branch is wired but will not fire: `c(X,X) = Tr X^2 != (Tr X)^2` already shows c differs from the product on the diagonal, foreshadowing rank 7.

## Consistency with the Gate -- CORRECTED Framing (ITEM 4a)

**STALE roadmap wording (do NOT copy):** success criterion 5 says "rank 7 saturates the transcendence-degree bound ... `<= 54 - orbit_dim = 7`." This predates the Phase-65 GATE correction. The "7" was the FORBIDDEN naive Spin(8)-triality back-of-envelope (`54 - 47 = 7`), which the gate explicitly rejects.

**What Phase 65 actually computed:** pair orbit dim = **44** (exact QQ rank of the 52x54 infinitesimal-action matrix, triple-confirmed) => `trdeg R[27(+)27]^{F_4} = 54 - 44 = 10`, NOT 7. Phase 65.1 confirmed the 10-candidate set `{6 pointwise, c, Tr(X^2 o Y), Tr(X o Y^2), Tr(X^2 o Y^2)}` has Jacobian rank exactly 10 (two-route agreement).

**CORRECT consistency statement for Phase 66:**
- **rank 7 <= trdeg 10** -- CONSISTENT. c is ONE of the FOUR mixed joint invariants `{c, Tr(X^2 o Y), Tr(X o Y^2), Tr(X^2 o Y^2)}` that bring the count from 6 to 10.
- rank 7 saturates the `{6 pointwise + c}` SUBSET (a 7x54 matrix has rank at most 7) but does **NOT** saturate the full transcendence degree (there are 3 more functionally independent invariants beyond c).
- Per the committed Phase-65.1 SUMMARY (verbatim): "Phase 66: c-independence rank-7 test for {6 pointwise + c} UNCHANGED, but rank 7 no longer saturates trdeg (3 more independent invariants) -- **(b) unaffected/strengthened**."

**Planner directive:** state the consistency as `7 <= 10` (c is a genuinely-new functionally-independent invariant, the FIRST of four mixed ones). Do NOT write "= 7 saturates trdeg." Assert `prefix_rank(7,.) <= ORBIT_DERIVED_TRDEG` (== 10) as the in-phase consistency check.

## Pitfalls / Forbidden Proxies -- Mapped to Concrete Guards

| Pitfall (ROADMAP / PITFALLS.md) | What goes wrong | Concrete guard in this phase |
| ------------------------------- | --------------- | ---------------------------- |
| **P2 assert-without-demonstration** | claiming c independent by appeal to theory without computing on h_3(O) | BOTH routes computed exactly over Q on the actual algebra; adjudicator requires agreement |
| **P3 float rank (GLOBAL forbidden proxy)** | `numpy.linalg.matrix_rank` / SVD tolerance fabricates the 6-vs-7 verdict (rank discontinuous) | `exact_qq_rank` only; `exact_rank_route_crosscheck` (QQ-frac==QQ-int==ZZ-int) certifies exactness; exact-only source guard asserts 0 numpy float-rank calls on the decisive path |
| **P4 non-generic evaluation point** | X=Y, X proportional to Y, repeated spectra DROP the rank | `_pair_not_proportional` + distinct-diagonal gate; >= 3 points + MAX aggregator; X=Y run ONLY as a *control* expected to give <= 6 |
| **P5 forcing a positive over the honest NEGATIVE (fp-force-positive)** | re-rolling points until rank hits 7 | PRE-REGISTER `PAIR_POINTS` + the rank test before evaluating; NEGATIVE branch fully wired with explicit-P constructor; report whatever the pre-registered test yields |
| **fp-rank-before-substitution** | symbolic rank of the 54-var Jacobian stalls (expression swell) | substitute the integer point FIRST, then rank (cached `CANDIDATE_GRADS` deliberately un-simplified) |
| **Route-2 false positive (NEW)** | a single non-generic Route-2 point making s vanish spuriously, or a diagonal-locus cancellation | check the separating vector s at ALL generic `PAIR_POINTS` (not one); confirm pointwise derivatives vanish at the SAME point; cross-check against the independent-pair safety pattern in `check_f4_invariance` |
| **det_3 port slip** | wrong cross-term order `(x1 x2) x3` is NOT F_4-invariant -> corrupts rank silently | conventions inherited from the FROZEN `E.det_3` (Phase-64.1 fix, certified); do NOT re-implement |
| **two-route mismatch ignored** | reporting a verdict when routes disagree | adjudicator emits NO VERDICT + STOP on the off-diagonal cells |

## Validation Strategies

### Internal Consistency Checks

| Check | What it validates | How | Expected |
| ----- | ----------------- | --- | -------- |
| 6x54 baseline | pointwise sextet trdeg = 6 (3 X + 3 Y) | `prefix_rank(6, pp)` at all pairs | exactly 6 (Garibaldi-Guralnick anchor) |
| 7x54 rank stability | generic rank well-defined | `prefix_rank(7, pp)` at >= 3 pairs | SAME at every pair (MAX = the verdict) |
| X=Y control | confirms non-generic point drops rank | `prefix_rank(7, (P,P))` | <= 6 (NOT a valid independence point) |
| Two-route agreement | the reward-hacking guard | Route-1 rank vs Route-2 separating-xi | both say independent (7 / exists) OR both dependent (6 / none) |
| Consistency `7 <= 10` | corrected gate consistency | compare to `ORBIT_DERIVED_TRDEG` | 7 <= 10 (c is 1 of 4 mixed invariants) |
| r6==6, r7==7 corroboration | matches committed Phase-65.1 preview | `check_tier_increments` ladder | (6,7,...) head as before |

### Exactness / Numerical Validation

| Test | Method | Expected |
| ---- | ------ | -------- |
| `exact_qq_rank` is exact at width 54 | `exact_rank_route_crosscheck` on the 7x54 | QQ-frac == QQ-int == ZZ-int (all equal) |
| f_4 basis faithfulness | 52-basis rank == full-324 rank (already certified upstream) | equal |
| Orchestrator-independent re-confirmation | re-run both routes at a FRESH generic pair NOT in `PAIR_POINTS` (distinct diagonals, X!=Y, non-proportional) | rank 7, separating xi exists (mirrors the Phase-65/65.1 hardening) |

### Red Flags During Computation

- `prefix_rank(6,.) != 6` at a generic point -> engine/builder bug; STOP, do not tune (Garibaldi-Guralnick says 6).
- 7x54 rank differs across generic points -> a point is secretly non-generic; check `_pair_not_proportional` and distinct diagonals.
- Route-2 separating vector s identically 0 at a generic point while Route-1 says 7 -> contradiction; likely a Route-2 contraction bug (wrong gradient block, or M acting on the wrong copy). Compare to the `check_f4_invariance` 54-wide split.
- Any nonzero `D_M f` for a pointwise generator along an orbit tangent -> the certified invariance is violated => port/basis bug; STOP.
- A rank-6 result with NO rational a making `c = a (Tr X)(Tr Y)` an identity -> the rank-6 finding is itself spurious (non-generic point); STOP.

## Level of Rigor

**Required:** exact symbolic/numeric proof over Q (the project's standard) -- NOT a controlled approximation, NOT numerical evidence. Every decisive quantity is an exact rational; every rank is `exact_qq_rank`.

**What this means concretely:**
- The verdict (7 or 6) is a definite integer computed exactly over Q at pre-registered generic points; no tolerance, no rounding.
- The orbit-derivative separating vector s is exact over Q; "nonzero" means `s_i != 0` as a rational, not `|s_i| > epsilon`.
- The two-route agreement is a hard gate; no verdict on disagreement.
- The NEGATIVE-branch P (if it fired) must be verified as a SYMBOLIC identity over Q, not merely point-matched.
- This is a "physicist's proof at machine-checked exact-arithmetic rigor" -- the genericity is handled by >= 3 points + MAX + the explicit degeneracy control, which is the field-standard substitute for a symbolic generic-rank argument (the symbolic rank over Q(x,y) stalls at width 54, so point-substitution + lower-semicontinuity is the rigorous route, as certified in the gate).

## Existing Results to Leverage

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
| ------ | ---------- | ------ | ---------- |
| Jacobian criterion (char 0) | trdeg = generic Jacobian rank | Derksen-Kemper 2015 | Route 1 license (rank 7 <=> independent) |
| Single-copy F_4 ring | R[Tr, Tr^2, det], trdeg 3; orbit 24, stab Spin(8) | Garibaldi-Guralnick 2105.09486 Lemma 8.1 (REPRODUCED in the certified gate) | r6==6 = 3 X-block + 3 Y-block cross-check |
| Der(h_3(O)) = f_4, dim 52 | `D_{a,b} = [L_a,L_b]`; span rank 52 (COMPUTED, certified) | Schafer 1966; `orbit_dimension_gate` | the f_4 basis for Route 2 (do NOT rebuild) |
| F_4 preserves Tr, norm, trace form; form non-degenerate on the 26 | — | Springer-Veldkamp 2000; Springer 1973 | grounds Route-2 non-vanishing of the pairing |
| Pair orbit dim = 44 => trdeg 10 | 54 - 44 = 10 (exact QQ rank, triple-confirmed) | Phase 65 SUMMARY | the corrected consistency target (ITEM 4a) |
| 10-set Jacobian rank 10; r6=6, r7=7 preview | exact, MAX over 4 pairs | Phase 65.1 SUMMARY | re-demonstrate r7==7 here as the phase's own result |
| det_3 factor order `(x2 x1) x3` is the F_4-invariant generic norm | annihilated by all 324 inner derivs | Phase 64.1 (certified) | inherited via `E.det_3`; do NOT re-implement |
| `c(X,X) = Tr X^2`, `polarize_d(X,X,X) = 6 det_3` | convention locks | `ring_lemma_verification.main()` | already verified; foreshadows c != (Tr X)^2 |

**Key insight:** the entire decisive computation is laptop-seconds, exact over Q, single-core. No HPC, no GPU, no sign problem. The risk is NOT feasibility -- it is convention/port fidelity and the genericity discipline. Reuse the frozen, certified machinery; the only new code is Route 2 + the adjudicator + the (no-op) NEGATIVE constructor.

## Computational Tools

| Tool | Version/Module | Purpose | Why standard |
| ---- | -------------- | ------- | ------------ |
| SymPy | 1.14 (`Rational`, `diff`, `simplify`, `Matrix`) | exact symbolic invariants, gradients | the warm exact engine; verified present |
| SymPy `DomainMatrix` | `sympy.polys.matrices`, over QQ/ZZ | `exact_qq_rank` -- fast EXACT width-54 rank | ~0.01s vs >5min for `Matrix.rank()`; exact, not float |
| `ring_lemma_verification` (as `E`) | in-repo (FROZEN) | octonion/h_3(O) primitives, 7 invariants, 54 symbols | the certified Phase-64 foundation |
| `orbit_dimension_gate` | in-repo (CERTIFIED) | f_4 basis, `exact_qq_rank`, `infinitesimal_action`, `PAIR_POINTS`, genericity gates | the certified Phase-65 GATE |
| `ring_generating_set` | in-repo (FROZEN) | `CANDIDATE_GRADS`, `prefix_rank`, `candidate_jacobian_matrix_at`, `check_f4_invariance` pattern | the Phase-65.1 candidate machinery |

**Environment:** SymPy 1.14 + NumPy 2.4 only; no Sage/GAP/Singular/Macaulay2/Magma. This phase needs NONE of those (no Molien series here -- that is Phase 68). NumPy must NOT touch the decisive ranks.

**Installation / Setup:** None. All three modules are in `code/`; SymPy is installed. The new harness imports `ring_lemma_verification as E`, the gate functions, and the candidate machinery exactly as `ring_generating_set.py` does.

**Computational feasibility:**

| Computation | Cost | Bottleneck | Mitigation |
| ----------- | ---- | ---------- | ---------- |
| 7x54 rank at one pair | ~0.01s (`exact_qq_rank`) | none | substitute point first |
| Route-2 over 52 generators x several pairs | seconds (52 trace-form scalars + 52 contractions per pair) | `simplify` of the contraction; det_3 gradient | substitute point FIRST; use the gradient-contraction form, not `simplify` of the full expr |
| Both routes over 4 `PAIR_POINTS` + fresh pair | well under a minute total | — | — |

NOTE (watchdog, from project memory): long no-output symbolic runs can trip a 600s stream-watchdog; run foreground with `python -u`; if a background resume stalls, the orchestrator can commit + SUMMARY on stall. Keep per-task output chatty (print per-pair ranks) so progress is visible.

## State of the Art

| Old framing | Current framing | When changed | Impact |
| ----------- | --------------- | ------------ | ------ |
| trdeg = 7 (six pointwise + c saturate) | trdeg = 10 (four mixed joint invariants) | Phase 65 GATE (orbit dim 44 computed) | "rank 7 saturates trdeg" is STALE; correct statement is `7 <= 10`, c is the FIRST of four |
| `octonion_algebra.py` as "warm exact harness" | `embedding_under_E_verification.py` -> `ring_lemma_verification.py` (exact SymPy) | Phase-0/64 | NEVER run decisive ranks on the float64 module |
| det_3 cross `(x1 x2) x3` | `(x2 x1) x3` (F_4-invariant generic norm) | Phase 64.1 | inherited via `E.det_3`; do not revert |

**Superseded approach to avoid:** the Spin(8)-triality back-of-envelope `54 - 47 = 7` (forbidden proxy fp-triality-backofenvelope). The pair orbit dim was COMPUTED (44), not looked up.

## Open Questions

1. **Will Route 2's separating direction agree with Route 1's rank 7?**
   - What we know: the r7==7 Jacobian preview holds (Phase 65.1); the trace form is non-degenerate and F_4-equivariant, so theory predicts a separating xi exists.
   - What's unclear: nothing material -- but Route 2 has never been *computed* per-generator; this phase computes it for the first time.
   - Impact: if they disagree, NO VERDICT (a builder/genericity bug). Recommendation: compute Route 2 at all `PAIR_POINTS` + a fresh pair; on disagreement STOP and diff against `check_f4_invariance`.

2. **Is the rank truly stable across all generic points (no hidden non-generic pair in `PAIR_POINTS`)?**
   - What we know: `PAIR_POINTS` are gated non-proportional with distinct diagonals; Phase 65.1 saw rank 10 (hence r7=7) at all 4.
   - Recommendation: assert SAME `prefix_rank(7,.)` at every pair; MAX is the verdict regardless.

## Alternative Approaches if Primary Fails

| If this fails | Because of | Switch to | Cost |
| ------------- | ---------- | --------- | ---- |
| `exact_qq_rank` doubted at width 54 | exactness concern | `Matrix.rank()` over QQ on the 7x54 (tractable at width 54 with only 7 rows) OR the three-domain cross-check | seconds (7 rows is fine for `Matrix.rank`, unlike the 52-row gate matrix) |
| Route-2 gradient-contraction doubted | possible block/copy error | the explicit `Tr(jordan(xi.X, Y))` trace-form form (slower but conceptually transparent) | seconds |
| A `PAIR_POINTS` pair suspected non-generic | rank anomaly | fresh independent generic integer pair (define inline, gate it) | trivial |
| NEGATIVE fires (rank 6) and `a (Tr X)(Tr Y)` is not an identity | contradiction with rank 6 | STOP -- the rank-6 finding is a non-generic-point artifact; re-examine the point, do not report | — |

**Decision criteria:** abandon the primary path ONLY on a hard contradiction (routes disagree, or a control fails). Never tune a point or redefine an invariant to force a verdict (fp-force-positive). The honest computed verdict -- 7 or 6 -- is the deliverable.

## Caveats and Alternatives (Pre-Submission Self-Critique)

1. **What assumption might be wrong?** That Route 2 is genuinely independent of Route 1. They are linked by the trdeg = 54 - orbit_dim duality. But they are *computationally* independent (different matrices, different question -- full-gradient rank vs trace-form pairing of orbit tangents), which is what the reward-hacking guard requires. The shared dependency is the certified f_4 basis + the engine, which is acceptable (both routes would fail together only on a builder bug, which the upstream GATE certification + the r6==6 control would catch).

2. **What did I dismiss too quickly?** A fully symbolic generic-rank proof over Q(x,y) (no point substitution). Dismissed because the gate documents it stalls at width 54 (expression swell). The >= 3-points + MAX + X=Y-control substitute is the certified field-standard and is rigorous via lower-semicontinuity. For only 7 rows, a symbolic rank MIGHT be tractable -- flagged as a belt-and-suspenders option, not required.

3. **What limitation am I understating?** Genericity is empirical (chosen points), not a proven Zariski-open statement. Mitigated by MAX over several gated-generic points + the explicit degeneracy control, but a pathological common non-generic locus across all chosen points is not formally excluded (only made very unlikely by independent point choices and the fresh-pair re-confirmation).

4. **Simpler method overlooked?** For c specifically, one could note `c(X,X) = Tr X^2` differs from `(Tr X)^2` and argue independence almost by hand -- but the milestone explicitly demands a *demonstrated* computation on the actual algebra (P2 forbids assertion), so the two-route computation is required, not optional.

5. **Would a specialist disagree?** A computational-invariant-theorist would endorse the Jacobian-criterion route as standard and the orbit-derivative as the right geometric dual. The one thing they would insist on -- which this research enforces -- is exact arithmetic for the rank (float rank fabricates the verdict) and honest reporting of a NEGATIVE. No methodological disagreement expected.

## Sources

### Primary (HIGH confidence)

- **Derksen, H.; Kemper, G.** *Computational Invariant Theory*, 2nd ed., Encyclopaedia of Mathematical Sciences 130, Springer (2015). Jacobian criterion (char 0: trdeg = generic Jacobian rank); trdeg = Krull dim for f.g. algebras. -- Route 1 license. [canonical; confirmed standard reference via search]
- **Garibaldi, S.; Guralnick, R.M.** "Generic Stabilizers for Simple Algebraic Groups." arXiv:2105.09486 (Lemma 8.1); corroborated by 2308.08214. -- single-copy F_4-on-26 orbit 24 / Spin(8) / trdeg 3; reproduced by the certified gate; grounds r6==6. [verified, reproduced in-engine]
- **Springer, T.A.** *Jordan Algebras and Algebraic Groups*, Springer (1973); **Springer, T.A.; Veldkamp, F.D.** *Octonions, Jordan Algebras and Exceptional Groups*, Springer (2000). -- F_4 = Aut preserving Tr and the cubic norm; trace form F_4-invariant and non-degenerate. [verified -- grounds Route-2 non-vanishing]
- **Schafer, R.D.** *An Introduction to Nonassociative Algebras* (1966). -- `D_{a,b} = [L_a,L_b]`; Der(h_3(O)) = f_4. [grounds the f_4 builder]

### Secondary (MEDIUM confidence)

- Project research `.gpd/research/SUMMARY.md`, `METHODS.md`, `PITFALLS.md` (2026-05-24) -- the Jacobian recipe, the orbit-derivative sketch, the seven reward-hacking guards, conventions. [internally cross-verified, the binding upstream synthesis]
- In-repo certified artifacts: `code/orbit_dimension_gate.py` (Phase 65, CERTIFIED), `code/ring_generating_set.py` (Phase 65.1), `code/ring_lemma_verification.py` (Phase 64). Phase 65/65.1 SUMMARYs (committed). [the machinery inventory; verified by inspection this session]

### Tertiary (LOW confidence)

- Schwarz, G.W. / Luna, D. -- smooth invariants of a compact group are smooth functions of the polynomial generators (licenses upgrading "not a polynomial" to "not a smooth function"). [used only for the precise phrasing of "functional"]

## Metadata

**Confidence breakdown:**
- Mathematical framework (Jacobian criterion + orbit-derivative bridge): HIGH -- both are standard char-0 tools, the bridge is the textbook trdeg/orbit duality, all anchors verified.
- Reusable-machinery inventory: HIGH -- read every target function this session; NEW-vs-reusable split is precise.
- Route 2 formalization: HIGH on the argument and the genericity hypotheses; the per-generator computation is NEW but reuses certified primitives (the only novelty is the assembly).
- Standard approaches / pitfalls: HIGH -- inherited from the certified pipeline + the project PITFALLS.md; every guard has a runnable test.
- Consistency correction (ITEM 4a): HIGH -- the committed Phase-65.1 SUMMARY states it verbatim.
- Outcome (rank 7 vs 6): the r7==7 preview is HIGH that it is 7, but the phase must RE-DEMONSTRATE both routes; the NEGATIVE branch is fully wired regardless.

**Research date:** 2026-05-26
**Valid until:** stable indefinitely (pure exact-over-Q algebra; only SymPy version could shift, and `exact_qq_rank` is version-robust). The ONE thing that would invalidate the consistency framing is a change to the Phase-65 orbit dim 44 -- which is CERTIFIED and triple-confirmed.
