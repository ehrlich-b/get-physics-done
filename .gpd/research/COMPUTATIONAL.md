# Computational Approaches: Bulk-Geometry Curvature of the h_3(O) Symmetric Cone (v17.0)

**Surveyed:** 2026-05-30
**Domain:** Computational differential geometry on exceptional Jordan-algebra symmetric cones (h_3(O) / Albert algebra); exact symbolic curvature of a 4-dim Lorentzian spacetime slice inherited from g_X = Hess(-log det)
**Confidence:** HIGH on the reuse path and dim-4 tractability (every claim below was run, not assumed); MEDIUM on the dim-10 budget (one cliff measured, not the full curvature)

> **Scope boundary.** This file covers computational TOOLS, the EXACT engine to reuse, symbolic-differential-geometry machinery, the exact-vs-numeric boundary, cost/scaling, and verification hooks. Physics methods (the A0 signature bridge, the homogeneity argument, stress-energy construction) live in METHODS.md; the symmetric-cone/Faraut-Koranyi background lives in PRIOR-WORK.md; convention traps live in PITFALLS.md.

---

## Recommended Stack

**Reuse `code/ring_lemma_verification.py` as the EXACT-over-Q h_3(O) engine; build the slice metric as `g_ij = d_i d_j(-log det_3)` by hand-rolled `sympy.diff`; compute Christoffel/Riemann with a hand-rolled loop (NOT `sympy.diffgeom`); keep matter parameters RATIONAL and slice coordinates symbolic.** This was measured end-to-end: the decisive slice (h_2(C_u), 4 real dim) produces a Minkowski-form det `b*g/3 - p^2/3 - q^2/3`, its `Hess(-log det)` builds in 35 ms, evaluates at the center I/3 to a clean nondegenerate `diag(9,9,18,18)`, and full Christoffel+Riemann with matter turned on (M rational) completes in ~19 s exactly over Q. The whole homogeneity KILL test and the cross-term on/off test are cheap and exact.

The single hard constraint that shapes everything: **SymPy 1.14 + NumPy only. No Sage/GAP/Singular/Macaulay2/Magma.** The warm engine already honors this (assert-based harness, no pytest, sympy/numpy-only venv), so the entire program stays inside the executor sandbox with no new dependencies.

The single load-bearing CORRECTNESS fact: there are **three mutually inconsistent `det` cross-term conventions in this repo**, differing by the octonion associator (measured gap 0.67 on a rational octonionic point). The certified-F_4-invariant exact det is `ring_lemma_verification.det_3`, which uses cross-term order `2*Re((x2 x1) x3)`. The float references (`octonion_algebra.det_3`, `peirce_coupling.H3Matrix.det`) carry the OLD buggy `(x1 x2) x3` order. **Use the engine's `det_3` for all geometry; treat the float dets as wrong on octonionic data.** (Full detail in PITFALLS.md; quantified in "Convention Hazard" below.)

---

## EXISTING ASSETS — confirmed by reading and running (not assumed)

All five named assets were read in full; the exact engine was executed (`ALL_PASS`); det conventions were compared numerically on a genuinely octonionic rational point.

### A1. `code/ring_lemma_verification.py` — THE engine to reuse (PRIMARY)

**Status:** runs clean, `OVERALL: ALL_PASS` (all 5 convention locks + headline `d(X,X,X)==6*det_3` over Q + 324/324 inner-derivation annihilation certifying F_4-invariance). SymPy 1.14.0, Python 3.14.2. Import-safe (`main()` is guarded by `if __name__=="__main__"`), so `from ring_lemma_verification import ...` is clean.

Confirmed public surface (all EXACT over Q; octonion = 8-list of SymPy Rationals; h_3(O) element = 3x3 nested list of octonions):

| Function / object | Signature | What it provides | Use in v17.0 |
|---|---|---|---|
| `oct(comps)`, `oct_zero()`, `oct_real(r)` | list[8] | build exact octonions | slice/matter coordinates |
| `oct_mul`, `oct_add`, `oct_sub`, `oct_scal`, `oct_conj`, `oct_simplify` | octonion arith | Fano `e1 e2 = e4`, NON-associative (`(ab)c != a(bc)` computed independently) | cross-term, associator checks |
| `h3o_from_coords(alpha,beta,gamma,x1,x2,x3)` | -> 3x3 octmat | build h_3(O) element; layout `x1->X[2][1], x2->X[0][2], x3->X[1][0]` | background X_bg, slice point |
| `h3o_identity()` | -> I | identity (center = I/3 via `octmat_scal(Rational(1,3), I)`) | center basepoint |
| `_coord_from_octmat(X)` | -> (a,b,g,x1,x2,x3) | recover coords | round-trip / cross-term reconstruction |
| `jordan(A,B)` | -> 3x3 octmat | **Jordan product (1/2)(AB+BA)**, lands in h_3(O); the 1/2 is load-bearing | X^o2, X^o3, Cayley-Hamilton |
| `h3o_matmul(A,B)` | -> 3x3 octmat | raw octonion matmul (non-associative) | inside jordan; sqrt cross-checks |
| `Tr(X)` | -> scalar | linear trace alpha+beta+gamma, bidegree (1,0) | invariants, CH norm |
| `Tr2(X)` | -> scalar | `Tr(jordan(X,X))`, bidegree (2,0) | CH norm, S(X) |
| **`det_3(X)`** | -> scalar | **the certified cubic norm N(X) = abg - a\|x1\|^2 - b\|x2\|^2 - g\|x3\|^2 + 2*Re((x2 x1) x3)** | **g_X = Hess(-log det_3); THE metric source** |
| `c(X,Y)=Tr(jordan(X,Y))` | -> scalar | coupling, bidegree (1,1) | matter coupling diagnostics |
| `polarize_d(X,Y,Z)` | -> scalar | symmetric trilinear polarization, `d(X,X,X)=6 det_3` | trilinear cross-term extraction |
| `cayley_hamilton_norm(X)` | -> scalar | N(X) from `X^o3 - Tr X^o2 + S X - N I = 0` | INDEPENDENT det verification (Hook V1) |
| `inner_derivations()` | -> [27x27 Matrix] | the 324 nonzero `[L_a,L_b]` spanning f_4 (dim 52) | F_4-invariance certification |
| `X_from_symbols(s)`, `_flat27(X)`, `_standard_basis_27()` | symbolic 27-coord | symbolic h_3(O), flatten/unflatten | symbolic slice metric |

**Cleanest reuse path:** copy `ring_lemma_verification.py` to `code/bulk_geometry_verification.py` (the project's established self-contained-decisive-module pattern — see its own PROVENANCE block, which copied rather than imported the Phase-62 engine), then add only: slice coordinatization, `g_ij = diff(-log(det_3(X(coords))), coords[i], coords[j])`, hand-rolled Christoffel/Riemann, and verification hooks. Do NOT import `octonion_algebra` on the decisive path — the engine's `exact_only_guard()` forbids it and it carries the cross-term bug.

### A2. `code/embedding_under_E_verification.py` — the C_u / Wick-rotation bridge (SECONDARY, for A0(i))

The original VALD-62-01 exact-SymPy engine. Same octonion/Jordan core as A1 (A1's core is ported verbatim from here). Import-safe. **Additionally exposes the h_3(C_u) machinery the A0 signature bridge needs:**

| Function | What it provides | Use in v17.0 |
|---|---|---|
| `proj_u_exact(a, u_index=7)` | project octonion onto C_u = span{1,e7} | restrict slice to h_2(C_u) |
| `E(X)` | conditional expectation h_3(O) -> h_3(C_u) (entrywise proj_u) | the slice projector |
| `cu_to_complex(a)` / `complex_to_cu(z)` | **exact iso C_u ~ C, e7 -> i** | the Wick-rotation hinge (A0(i)) |
| `slice_to_complex(X)` / `complex_to_slice(Mc)` | h_3(C_u) <-> 3x3 SymPy complex matrix | reduce slice det to a complex 3x3 determinant |
| `matrix_sqrt_complex`, `slice_sqrt`, `sqrt_ambient` | exact spectral sqrt (CFC principal branch) | basepoint transport (if needed for B/C) |
| `associator(A,B,C)` | `(AB)C - A(BC)` | confirm non-associativity is live |
| `peirce_V1/Vhalf/V0` (referenced; structure ported from `octonion_algebra`) | Peirce projectors under E_11 | split matter (V_1, V_{1/2}) from slice (V_0) |

This is the asset for **A0 construction (i)** (restrict g_X to V_0 and Wick-rotate via u=e7). For the slice-det route (A0(ii)) the engine in A1 already suffices: the C_u sub-slice det is just the engine's `det_3` evaluated with off-diagonals in comps {0,7}, which we measured to be the Minkowski form.

### A3. `peirce_coupling.py` (NumPy, h_3(K) for K=R,C,H,O) — REUSE FOR PEIRCE GEOMETRY ONLY; det is BUGGY

Float-only. `H3Matrix(K, diag, off)` with `.jordan_product`, `.peirce_decompose(eidx=0)` (returns `(V1, V_half, V0)`), `.trace_inner`, `.norm_sq`. The Peirce decomposition and Jordan product are correct and useful for prototyping the V_0/V_{1/2}/V_1 split. **BUT `.det()` (line 441) uses `K.mul(K.mul(x1, x2), x3)` — the buggy `(x1 x2) x3` order; off by the associator on octonionic data.** Do NOT use `.det()` for geometry. Use it only as a fast NumPy sanity-prototyper for Peirce structure, then re-derive everything exactly in the A1 engine.

### A4. `peirce_coupling_v2.py` (NumPy) — investigation notes, not load-bearing

`from peirce_coupling import *` (inherits the buggy det but only calls `.jordan_product`/`.peirce_decompose`, never `.det`). Establishes a physics fact directly relevant to scoping the cross-term test: **x1 (in V_0) couples to the observer E_11 ONLY through the cubic determinant trilinear, never through bilinear Jordan products** (`V_0 o V_0 -> V_0`, no V_1 leakage). This is exactly the cross-term mechanism Phase B must isolate. Read for intuition; do not import on the decisive path.

### A5. `rho_directional_derivatives.py` (SymPy + NumPy) — REUSE FOR THE OFF-CENTER EXPANSION (B(c))

Symbolic + numeric expansion of `rho_J(X) = det(X)(Tr(X^2) - 1/3)` around diagonal states (incl. I/3). Provides:
- The **exact Hessian-of-det-at-diagonal-state result** (PART 13): off-diagonal Hessian blocks are `d2_i = 4*det - 2*w_i*(sig2 - 1/3)` with `w = (a,b,c)` the eigenvalue opposite slot x_i, in three 8-fold-degenerate blocks. **This is the closed-form second-derivative structure the slice metric inherits at diagonal backgrounds** — a free analytic check on the symbolic Hessian.
- PART 12: the triple product `2*Re(x1 x2 x3)` enters only at THIRD order (`d3/ds dt du = 2*(sig2-1/3)`), confirming it is a vertex, not a propagator.
- **CAUTION:** this file uses the real-only cross term `2*d1*d2*d3` (PART 1, line 31) and labels it `(x1 x2) x3`. On REAL directions all orderings agree, so its results are correct; but the labeling perpetuates the buggy order. Reuse the *formulas and the expansion strategy*, re-derive the octonionic cross-term from the A1 engine.

### Convention Hazard (measured) — the one thing that can silently destroy the result

```
On a genuinely octonionic rational point (all three off-diags with several nonzero imag comps):
  ring_lemma det_3  (== 2*Re((x2 x1) x3))  =  24.97779865462204   <- CERTIFIED F_4-invariant (CH + 324/324 derivations)
  (x1 x2) x3 order  (peirce_coupling, octonion_algebra)            =  24.30616409870177   <- WRONG (old bug)
  associator gap                                                   =   0.6716...           (NONZERO -> order matters)
```
Note `h3o_tower.py` (the prompt's "corrected reference") uses a THIRD spelling `2*Re(conj(x2)(conj(x0) x1))` on a DIFFERENT coordinate labeling (`d/x[0..2]`); it is internally consistent and CH-verified in that file, but it is NOT the same coordinate convention as the engine. **Do not mix labelings.** The engine (A1) is the single source of truth; everything else converts to it or is discarded.

---

## Numerical Algorithms

"Numerical" here means symbolic-algebraic algorithms over Q (the decisive path is exact, not floating-point). mpmath enters only as a guarded fallback (see Exact-vs-Numeric).

| Algorithm | Problem | Convergence | Cost per Step | Memory | Key Reference |
|---|---|---|---|---|---|
| Hessian of -log det_3 (`sympy.diff` x2) | build slice metric g_ij | exact (not iterative) | dim-4: <0.04 s; dim-10: ~0.2 s (55 entries) | small | this survey (measured) |
| Symbolic matrix inverse `Matrix.inv()` | g^{ij} (Christoffel needs it) | exact | dim-4 + matter rational: ~3 s; dim-4 fully-symbolic-in-6-vars: TIMEOUT >200 s; dim-10 symbolic: TIMEOUT >200 s | grows fast | this survey (measured) |
| Hand-rolled Christoffel `Gamma^a_bc` | connection | exact | dim-4 matter-rational: part of the ~19 s total; dim-4 fully-symbolic: TIMEOUT | moderate | MTW / Wald (textbook formula) |
| Hand-rolled Riemann `R^a_bcd` | curvature | exact | dim-4: ~0.15 s once Gamma is in hand | small | MTW / Wald |
| `cancel`/`together` per entry | tame expression swell | n/a | the dominant cost; apply once per tensor entry, never `simplify` in a hot loop | n/a | SymPy docs |
| `sympy.Matrix(...).rank()` over QQ | any rank-bearing check | exact | cheap at these dims | small | engine `RANK_ROUTING_CONVENTION` |

### Convergence / failure properties

- **Not iterative** — everything is exact symbolic algebra, so "convergence" = "does the simplifier terminate before the cliff." The failure mode is **expression swell**, not non-convergence.
- **Known failure mode (measured):** carrying matter parameters AND slice coordinates as free symbols through `Matrix.inv()` blows up (>200 s timeout at dim-4 with 6 symbols; dim-10 symbolic inverse also times out). The metric BUILD and point-EVALUATION are always cheap; the **symbolic inverse is the cliff**.
- **Mitigation that works (measured):** substitute matter (m1, mu, ...) to small RATIONALS *before* inverting; keep only the 4 slice coordinates symbolic. Full Christoffel+Riemann then completes in ~19 s. For the M-dependence of curvature (B(c)), series-expand in a single matter amplitude `t` to low order rather than carrying it symbolically through the inverse.
- Use `cancel(together(expr))` (not `simplify`) on each metric/Christoffel entry; `simplify` is far slower and unnecessary for rational functions.

---

## Software Ecosystem

### Primary Tools

| Tool | Version | Purpose | License | Maturity |
|---|---|---|---|---|
| SymPy | **1.14.0** (current latest stable; confirmed installed + via release tracker) | exact symbolic algebra over Q: octonion/Jordan arithmetic, `det_3`, `diff`, `Matrix.inv`, `Matrix.rank` | BSD | stable |
| NumPy | **2.4.2** (installed; 2.x series) | fast float prototyping of Peirce structure (NON-decisive) | BSD | stable |
| Python | 3.14.2 | interpreter | PSF | stable |

### Supporting Tools

| Tool | Version | Purpose | When Needed |
|---|---|---|---|
| mpmath | 1.3.0 (installed; SymPy dependency) | high-precision (50-100 digit) curvature as a guarded fallback / float-artifact firewall | only where exact times out AND a verdict is still needed; never on the homogeneity KILL test |
| `sympy.diffgeom` | bundled with 1.14 | `metric_to_Christoffel_2nd`, `metric_to_Riemann_components`, `metric_to_Ricci_components` exist and work | OPTIONAL cross-check only — see Anti-Approach below |

### EXPLICITLY EXCLUDED (per milestone constraint)

Sage, GAP, Singular, Macaulay2, Magma. None are available or permitted. The entire program fits in SymPy+NumPy; no Groebner-basis engine is needed for the geometry (the v16.0 milestone established that the project deliberately avoids external CAS).

---

## Anti-Approaches

| Anti-Approach | Why Avoid | What to Do Instead |
|---|---|---|
| Use `octonion_algebra.det_3` or `peirce_coupling.H3Matrix.det` for the metric | BUGGY `(x1 x2) x3` cross-term order; off by the associator (measured 0.67) on octonionic data; would corrupt every curvature downstream | Use `ring_lemma_verification.det_3` (certified F_4-invariant: CH norm + 324/324 inner derivations) |
| `sympy.diffgeom` `metric_to_*` as the PRIMARY curvature path | Finicky (coordinate-function diff fails; `subs` of symbols into coord_functions triggers "more than one coordinate system"; only the base-vector idiom works) AND slower (measured `Christoffel_2nd` 14.2 s vs hand-rolled ~2.9 s; Ricci timed out) | Hand-rolled Christoffel/Riemann loops from the textbook formula on a plain `sympy.Matrix` metric; use diffgeom only as an independent cross-check on ONE point if desired |
| Carry matter params + slice coords all symbolic through `Matrix.inv()` | Expression swell -> >200 s timeout (measured at dim-4/6-symbols and dim-10) | Substitute matter to rationals before inverting; keep 4 slice coords symbolic; series-expand in matter amplitude for M-dependence |
| `numpy.linalg.matrix_rank` / float SVD for any rank or curvature verdict | rank/curvature are discontinuous; a float tolerance fabricates the answer; the engine's `exact_only_guard()` forbids it | `sympy.Matrix(...).rank()` over QQ; exact `cancel(...) == 0` tests for flatness |
| Expect the raw cone Hessian `Hess(-log det)` to be FLAT at M=0 | The cone is an INTRINSICALLY CURVED symmetric space (E_{6(-26)}/F_4 type); measured 60 nonzero Riemann comps at M=0 on the slice | The Minkowski/flat background comes from the A0 signature construction (take eta from h_2(C_u)'s OWN det; let the bulk supply only h_munu), NOT from the bulk Hessian vanishing. See PITFALLS.md. |
| Single-slot matter for the cross-term on/off test | If only one off-diagonal slot is nonzero, `2*Re((x2 x1) x3) = 0` identically (measured), so the cross-term test is vacuous | Populate all three slots so the triple product is genuinely nonzero (x2,x3 carry V_{1/2} matter, x1 carries the V_0 slice direction); confirmed this is what makes the cubic vertex live (peirce_coupling_v2, rho PART 12) |
| Rebuild octonion arithmetic / det / Peirce from scratch | weeks of work, re-introduces the cross-term bug the project already paid to fix in Phase 64.1 | Copy `ring_lemma_verification.py` verbatim (the project's self-contained-decisive-module pattern) and extend |

---

## Logical Dependencies

```
det_3 verified (CH norm == det_3 at octonionic pts; 324/324 inner-derivation annihilation)
   -> ONLY THEN build any metric           (Hook V1; cheap, run FIRST)

g_X = Hess(-log det_3)  requires  det_3 > 0 on the slice
   -> reduce-to-Minkowski at (M=0, center)  (Hook V2): slice det = b*g/3 - p^2/3 - q^2/3 (measured),
      Hess at I/3 = diag(9,9,18,18) nondegenerate

A0 signature bridge (METHODS.md) chooses Lorentzian eta
   -> required BEFORE any curvature claim   (the raw cone Hessian is Riemannian + curved even at M=0)

Christoffel(g)  requires  g^{ij} = g.inv()
   -> matter MUST be rational before inv()  (symbolic-matter inverse times out)

Riemann(g)  requires  Christoffel
   -> Phase A homogeneity test needs only Hess + its x-dependence, NOT Riemann (cheapest gate; do FIRST)

Cross-term ON/OFF (Phase B(b))  requires  all three off-diag slots populated
   -> single-slot matter makes the cubic vertex vanish identically
```

---

## Recommended Investigation Scope

Prioritize (cheapest-and-decisive first, matching the milestone's "Phase A kills or greenlights everything"):

1. **Verify det_3 then reduce-to-Minkowski (Hooks V1, V2).** Reuse `cayley_hamilton_norm` + `inner_derivations` for V1 (already passing in the engine); confirm slice det = Minkowski form and Hess at I/3 = `diag(9,9,18,18)`. **Cost: seconds. Run before anything else.**
2. **Phase A homogeneity KILL test.** Build `Hess(-log det_3)` on the 4 slice coords with matter and ask whether `h_munu(x)` is x-independent. Needs only the Hessian and its dependence on the slice point — NOT the full Riemann. Compare `Stab_{E_6}(E_11)` dimension against the basepoint-family dimension (reuse `orbit_dimension_gate.py` machinery if a rank computation is wanted; route through `sympy.Matrix.rank()`). **Cost: seconds–minutes, exact over Q.**
3. **Phase B Riemann with matter (only if A survives).** Matter rational, slice coords symbolic: full Christoffel+Riemann ~19 s (measured). Cross-term ON/OFF by dropping the `2*Re((x2 x1) x3)` term at the expression level (all three slots populated). **Cost: tens of seconds per configuration.**
4. **Phase B(c) M-dependence.** Series-expand curvature in a single matter amplitude `t` to low order (reuse `rho_directional_derivatives` expansion strategy + its closed-form `d2_i = 4 det - 2 w_i (sig2 - 1/3)` as an analytic check). **Cost: minutes.**

Defer / out of scope for the exact path:
- **Full dim-10 V_0 symbolic curvature:** the symbolic metric INVERSE times out (>200 s, measured). Feasible only point-evaluated or with all matter rational and heavy `cancel`; treat as a high-precision-mpmath fallback if a dim-10 verdict is ever needed. The decisive physics lives on the 4-dim h_2(C_u) slice, so dim-10 is not on the critical path.
- **Dim-26 (det=1 hypersurface) curvature:** not tractable symbolically; not needed (the slice is 4-dim).

---

## Data Flow

```
slice coords (b,g,p,q) [+ matter m1, mu, ...]
 -> h3o_from_coords(...)  using engine layout (x1->[2][1], x2->[0][2], x3->[1][0])
 -> det_3(X)   [CERTIFIED cross-term (x2 x1) x3]                     (Intermediate: cubic norm)
 -> -log(det_3(X))                                                  (potential F)
 -> g_ij = cancel(diff(F, coords[i], coords[j]))                    (4x4 metric, ~0.04 s)
 -> [A0 signature bridge: Lorentzian eta + h_munu]  (METHODS.md)    (signature fix)
 -> [Phase A: is h_munu x-dependent?]  --KILL or GREENLIGHT--
 -> matter -> rationals; g.inv()                                    (g^{ij}, ~3 s)
 -> Gamma^a_bc (hand-rolled)                                        (~few s)
 -> R^a_bcd (hand-rolled)                                           (~0.15 s)
 -> Ricci, Einstein G_munu (contractions)                          (cheap)
 -> [cross-term ON/OFF, M-dependence] -> verdict
```

## Computation Order and Dependencies

| Step | Depends On | Produces | Can Parallelize? |
|---|---|---|---|
| det_3 verification (V1) | engine (already passes) | trust in det | no (gate) |
| slice det + Minkowski check (V2) | det_3 | Minkowski form, diag(9,9,18,18) | no (gate) |
| A0 signature bridge | V2 | Lorentzian eta + h_munu split | no |
| Phase A Hessian x-dependence | det_3, A0 | KILL/GREENLIGHT | matter configs parallel |
| g.inv() (matter rational) | metric | g^{ij} | per-config parallel |
| Christoffel | g^{ij}, metric | Gamma | per-config parallel |
| Riemann/Ricci/Einstein | Christoffel | curvature, G_munu | per-config parallel |
| cross-term ON/OFF | det_3 (with/without cross) | matter-sourcing isolation | parallel |

Parallelism: different matter configurations / the cross-on vs cross-off runs are independent processes — run them as separate `python -u` invocations (the executor's per-process model; see Resource Estimates).

## Resource Estimates

| Computation | Time (measured/estimated) | Memory | Hardware |
|---|---|---|---|
| Engine self-check (`ring_lemma_verification.py`) | ~60-150 s (324-derivation lock dominates) | <1 GB | 1 core |
| Slice det + Hess(-log det), dim-4 | <0.05 s | small | 1 core |
| Eval metric at center I/3 | <0.01 s | small | 1 core |
| dim-4 full Christoffel+Riemann, MATTER RATIONAL | ~19 s | <1 GB | 1 core |
| dim-4 M=0 Christoffel+Riemann (flat-background reference) | ~10 s | <1 GB | 1 core |
| dim-4 fully-symbolic-in-6-vars `g.inv()` | **TIMEOUT >200 s** (avoid) | grows | 1 core |
| dim-10 V_0 Hess build + eval-at-center | ~0.25 s | small | 1 core |
| dim-10 V_0 symbolic `g.inv()` | **TIMEOUT >200 s** (avoid; mpmath fallback) | large | 1 core |
| `sympy.diffgeom` Christoffel_2nd, dim-4 | ~14 s (slower than hand-rolled; cross-check only) | <1 GB | 1 core |

**Executor watchdog caveat (project-specific, from MEMORY).** The `gpd-executor` stream-watchdog kills long no-output symbolic runs (~150 s harness, hard kill at 600 s); background resume has stalled before. Long curvature runs should print progress between heavy steps (after metric build, after inverse, after Christoffel) and run foreground with `python -u`. Keep each decisive step under ~150 s of silent compute — the recipe above (matter rational, hand-rolled, `cancel` per entry) stays well inside this.

## Integration with Existing Code

- **Input format:** h_3(O) elements as the engine's nested-list-of-octonion-8-lists (NOT the `octonion_algebra.H3O` float dataclass, NOT the `peirce_coupling.H3Matrix` float class). Coordinates are exact SymPy `Rational`/`Symbol`.
- **Reuse path:** copy `code/ring_lemma_verification.py` -> `code/bulk_geometry_verification.py`; import nothing from `octonion_algebra` (engine guard forbids it); pull the C_u iso (`cu_to_complex`, `slice_to_complex`, `proj_u_exact`) from `embedding_under_E_verification.py` if A0(i) is chosen.
- **Output format:** assert-based `_report(label, ok)` / `ALL_PASS` / `sys.exit(0/1)` harness (the project standard — no pytest in the executor venv). Curvature verdicts printed as exact rational expressions; flatness as `cancel(R) == 0`.
- **Interface points:** the slice coordinatization and the `g_ij = diff(-log det_3, ...)` builder are the only genuinely new code; Christoffel/Riemann are ~30 lines of textbook loops.

## Validation Strategy (Verification Hooks — concrete, with resource estimates)

| Hook | Result | How to validate | Tolerance | Cost |
|---|---|---|---|---|
| **V1. det multiplicativity + Cayley-Hamilton** (run BEFORE any geometry) | `det_3 == cayley_hamilton_norm` at octonionic pts; annihilated by all 324 inner derivations | reuse engine LOCK 7a/7b (already passing) | exact `==0` over Q | already in engine; ~60-150 s |
| **V2. Reduce-to-Minkowski at (M=0, center)** | slice det = `b*g/3 - p^2/3 - q^2/3` (Minkowski form); `Hess(-log det)` at I/3 = `diag(9,9,18,18)`, nondegenerate (det 26244) | build + subst center; compare to `52-kkt-spacetime` Minkowski quadratic | exact over Q | <0.1 s (measured) |
| **V3. Cross-term ON/OFF** (Phase B(b) isolation) | dropping `2*Re((x2 x1) x3)` from det removes matter-sourced curvature | build det_full and det_nocross; recompute Riemann for each; **populate all 3 slots** or the term is vacuously 0 | exact diff of Riemann components | ~2x the ~19 s curvature run |
| **V4. M=0 curvature baseline** | the slice curvature at M=0 under the A0 construction (NOT the raw cone, which is curved) | recompute Riemann at M=0 after the A0 eta-subtraction; expect flat or pure-Lambda | exact `==0` (flat) or `==const*g` (Lambda) | ~10 s (measured for raw; A0-corrected similar) |
| **V5. F_4-residual symmetry of the metric** | metric/curvature invariant under `Stab_{E_6}(E_11)` action | reuse `orbit_dimension_gate.py` / `inner_derivations`; route ranks through `sympy.Matrix.rank()` | exact | minutes |
| **V6. diffgeom cross-check (optional)** | hand-rolled Riemann == `metric_to_Riemann_components` on one point | run both on a single rational metric | exact match | ~15 s (diffgeom slower) |

---

## Open Questions

| Question | Why Open | Impact on Project | Approaches Being Tried |
|---|---|---|---|
| Which A0 construction reduces exactly to Minkowski at (M=0, center)? | Two candidates (Wick-rotate g_X via u=e7 vs eta from h_2(C_u)'s own det) — both plausible | determines whether curvature is Lorentzian and what "background" means | A0(ii) measured to give Minkowski det directly; A0(i) needs `cu_to_complex`/sqrt machinery (METHODS.md) |
| Is `h_munu(x)` x-dependent after fixing E_11? | the homogeneity KILL/GREENLIGHT fork; not yet computed | DECIDES whether the route is dead | Phase A Hessian-x-dependence + `Stab_{E_6}(E_11)` dimension count (cheap, exact) |
| Does dim-10 V_0 curvature ever need to be computed exactly? | symbolic inverse times out (measured) | only matters if the 4-dim slice is insufficient | deferred; mpmath high-precision fallback available if needed |
| Will `cancel` tame the matter-symbolic Christoffel enough for a low-order series? | swell vs series truncation tradeoff untested | B(c) M-dependence quantification | series-expand in single amplitude `t`; reuse rho-expansion closed forms as a check |

---

## Sources

- `code/ring_lemma_verification.py` (VALD-64-01, this repo) — the EXACT-over-Q h_3(O) engine; `det_3`, `jordan`, `Tr/Tr2/c`, `cayley_hamilton_norm`, `inner_derivations`, `polarize_d`; ran clean (`ALL_PASS`). Cross-term order `(x2 x1) x3` certified F_4-invariant (CH + 324/324 derivations). **Primary reuse target.**
- `code/embedding_under_E_verification.py` (VALD-62-01, this repo) — exact C_u machinery: `proj_u_exact`, `E`, `cu_to_complex`/`slice_to_complex`, `matrix_sqrt_complex`/`slice_sqrt`/`sqrt_ambient`, `associator`. The A0(i) bridge.
- `peirce_coupling.py` / `peirce_coupling_v2.py` (this repo) — correct Peirce decomposition + Jordan product (NumPy); det is BUGGY (`(x1 x2) x3`), use for structure only. v2 establishes x1->E_11 couples only via the cubic vertex.
- `rho_directional_derivatives.py` (this repo) — closed-form off-diagonal Hessian-of-det at diagonal states `d2_i = 4 det - 2 w_i (sig2-1/3)`; triple product is third-order. Real-only cross term (correct on real directions, mislabeled order).
- `~/repos/blog/research/qualia-fixed-point/h3o_tower.py` — float reference det with a THIRD cross-term spelling `2*Re(conj(x2)(conj(x0)x1))` on a different coordinate labeling; CH-verified there but not the engine's convention. Do not mix labelings.
- `code/octonion_algebra.py:2147-2181` (this repo) — float `det_3` with the BUGGY `(x1 x2) x3` order and an (incorrect) "CRITICAL: LEFT-to-right (x1*x2)*x3" comment. Engine's `exact_only_guard()` forbids importing it on the decisive path.
- [SymPy 1.14.0 diffgeom documentation](https://docs.sympy.org/latest/modules/diffgeom.html) — `metric_to_Christoffel_2nd`, `metric_to_Riemann_components`, `metric_to_Ricci_components` exist; finicky and slower than hand-rolled (measured).
- [SymPy releases](https://github.com/sympy/sympy/releases) and [python:sympy versions (Repology)](https://repology.org/project/python:sympy/versions) — confirm 1.14.0 is current latest stable (matches installed).
- Faraut & Koranyi, *Analysis on Symmetric Cones* (OUP 1994) — `g_X = Hess(-log det)` is the canonical cone metric (cited in PRIOR-WORK.md for the geometry; here only as the source of the metric formula being implemented).
- Misner-Thorne-Wheeler / Wald, *General Relativity* — standard Christoffel `Gamma^a_bc = (1/2) g^{ad}(d_b g_dc + d_c g_db - d_d g_bc)` and Riemann `R^a_bcd` formulas used in the hand-rolled loops.
