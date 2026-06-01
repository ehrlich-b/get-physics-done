# Computational Approaches: Cartan / MacDowell-Mansouri / Berry-Curvature Gravity on h_3(O)

**Surveyed:** 2026-06-01
**Domain:** Computational differential geometry / exceptional Jordan algebras (h_3(O), F_4, OP^2) / quantum geometry (QGT) — exact symbolic (over Q / Q(i))
**Confidence:** HIGH (the load-bearing engine + curvature harness already exist, run clean, and the four new objects were each prototyped exact-over-Q during this survey)

### Scope Boundary

This file covers computational TOOLS, libraries, representations, algorithms, resource costs, and integration points with the existing engine. Physics methods (what the soldering form / Cartan connection / MM contraction MEAN) belong in METHODS.md; the theory landscape (Borel, Provost-Vallee, MacDowell-Mansouri, Wise) belongs in PRIOR-WORK.md.

---

## Recommended Stack

**Verified environment (this machine, 2026-06-01):** Python `3.14.2`, `sympy 1.14.0`, `numpy 2.4.2`. The executor venv is `sympy`/`numpy` only (no pytest, no SageMath, no GAP) — the existing engines already target this constraint (assert-based harnesses, run as `python3 code/<file>.py`, exit 0 iff ALL_PASS).

**One-line recommendation:** Do NOT introduce any new heavy CAS. Build the entire v18.0 route on the two existing self-contained exact-SymPy modules — `code/ring_lemma_verification.py` (the det SSOT, 960 ln, ALL_PASS confirmed this session) and `code/bulk_geometry_verification.py` (3119 ln; the warm h_3(O) engine + the Totaro/Levi-Civita curvature harness + the F_4/E_6/stabilizer machinery, imports clean with `_ODG` this session) — extended with TWO small hand-rolled layers: (1) a **component-matrix differential-forms layer** for the Lie-algebra-valued Cartan curvature `F=dA+A∧A`, and (2) an **eigenprojector QGT layer** for the Berry curvature `F_B=Im(QGT)`. Both were prototyped exact-over-Q this session (see Validation Strategy). All decisive arithmetic stays exact over Q (Q(i) for the Berry/QGT sector); `sympy.Matrix.rank()` / `sympy.real_roots` only; never numpy/float on a verdict.

**The exactness keystone (empirically confirmed this session):**
- `sympy.diffgeom` (`Differential`, `WedgeProduct`) DOES stay exact over Q for *scalar* rational-coefficient forms (tested: `d((1/2)bg db + (p-3q/7)dg)` returned exact rationals, no `Float` atoms).
- `sympy.diffgeom` does NOT natively represent **matrix-valued / Lie-algebra-valued** connection 1-forms, so the `A∧A` term of the Cartan connection cannot be done in diffgeom directly. The **hand-rolled component-matrix** form `F_{μν} = ∂_μ A_ν − ∂_ν A_μ + [A_μ, A_ν]` (matrix commutator = the wedge of Lie-algebra-valued 1-forms) was tested exact-over-Q this session and is the recommended representation.
- The QGT projector formula `F_{μν} = −i·Tr(P[∂_μP, ∂_νP])` (and `Re Tr(∂_μP ∂_νP)` for the Fubini-Study real part) was tested on a rank-1 rational projector this session: exact over **Q(i)** (Gaussian rationals), no `Float`.

---

## Numerical Algorithms

(All "numerical" here means EXACT symbolic over Q / Q(i) — there is no floating-point step on any decisive path. "Cost per step" is symbolic-simplification cost, the real bottleneck.)

| Algorithm | Problem | Convergence (exactness) | Cost driver | Memory | Key Reference / in-repo |
| --------- | ------- | ----------------------- | ----------- | ------ | ----------------------- |
| Exact RREF / DomainMatrix rank over QQ | orbit/stabilizer dims, coframe image dim, residual-structure-group rank, F_4-invariance (324/324) | exact (rational pivots) | rref of a `729 x k` (e6) or `27 x m` matrix over QQ | low (rational entries) | `_ODG.exact_qq_rank`, `_ODG.span_rank_over_QQ` (orbit_dimension_gate.py L154/L141) |
| `det_3` Freudenthal cubic norm | the SSOT scalar all curvature is built from | exact | non-associative octonion mul (Fano) | low | `ring_lemma_verification.det_3` (L308); copy in bulk_geometry L351 |
| Hessian-metric 3rd-derivative tensor `C_ijk` | the Totaro closed-form Riemann datum (g=Hess(-log det)) | exact | `diff` of `-log(det_3)` 3x over 4 (or 27) symbols | medium (the 27-symbol jet is the heavy build; cache it) | `cubic_form_C` (bulk_geometry L1382) |
| Totaro closed-form Riemann `R_ijkl = -(1/4)g^{pq}(C_jlp C_ikq − C_ilp C_jkq)` | lower-index Riemann of a Hessian metric without 4th derivatives | exact | O(n^4) contraction + one `g.inv()`; `simp=cancel` at a rational point | medium | `totaro_riemann` (L1397); ref-totaro arXiv:math/0401381 |
| Hand-rolled Levi-Civita Riemann (Christoffel route) | INDEPENDENT cross-check of Totaro on ≥5 components | exact | symbolic `g`, diff, then evaluate at rational pt, then 4x4 `inv` | medium | `hand_rolled_riemann_of_g` (L2236) |
| **Hand-rolled matrix-valued curvature `F_{μν}=∂A−∂A+[A,A]`** (NEW) | the Cartan connection field strength F=dA+A∧A | exact | per-component matrix `diff` + matrix commutator | low (the connection matrices are small: 10x10 (A)dS, or the relevant block) | tested this session; matrix commutator = wedge of Lie-valued 1-forms |
| **Eigenprojector QGT** `Q_{μν}=Tr(P ∂_μP ∂_νP)`, Berry `F_B=−i Tr(P[∂_μP,∂_νP])` (NEW) | the Berry curvature = Im(QGT); FS metric = Re(QGT) consistency anchor | exact over **Q(i)** | `diff` of a rank-1 projector P(x) + 2x2/3x3 matrix products | low | tested this session; Avron-Graf-Kohmoto eigenprojector calculus, arXiv:2102.09899 |
| `eig_signature_count` via exact `real_roots` of the charpoly | Lorentzian-signature verdict (1,3) on the coframe Gram | exact | charpoly det + Sturm/Descartes real-root isolation | low | `eig_signature_count` (L2369) |
| `ricci_decomposition_n4` (traceless-Ricci / Weyl / scalar split) | is the curvature Einstein-shaped? (S=0? Weyl=0?) | exact | O(n^4) tensor algebra at n=4 | low | `ricci_decomposition_n4` (L2329) |

### Convergence Properties

There is no iterative convergence — every quantity is computed in closed form and is exact. The only "failure modes" are (a) symbolic blow-up / watchdog stalls (see Resource Estimates) and (b) `sympy.simplify` returning an un-normalized-but-equal expression. Mitigations:
- **Convergence criterion** = the assert passes (e.g. `R[i][j][k][l] + R[j][i][k][l] == 0` antisymmetry, `resid_zero` in the Ricci decomposition, the 324/324 inner-derivation annihilation). These are the `_report(label, ok)` gates the existing harness uses.
- **Use `cancel` not full `simplify`** when entries are rational functions of a rational basepoint (the existing engine does exactly this: `totaro_riemann(..., simp=cancel)`, `h3_cone_hessian_benchmark` uses `cancel`). `simplify` on the symbolic 27-coord Hessian is the watchdog trap.
- **For equality of two symbolic curvatures (Totaro vs Levi-Civita), test `simp(A − B) == 0`**, never `A == B` on un-normalized forms (the existing `riemann_symmetry_ok` and `hand_rolled_riemann_of_g` do this; note the documented uniform `−1` global sign convention between the two routes — carry it).

---

## Software Ecosystem

### Primary Tools

| Tool | Version | Purpose | License | Maturity |
| ---- | ------- | ------- | ------- | -------- |
| Python | 3.14.2 | host | PSF | stable |
| SymPy | 1.14.0 | ALL exact symbolic algebra (Matrix.rank, real_roots, diff, cancel, rref, diffgeom) | BSD | stable |
| NumPy | 2.4.2 | present but **must NOT touch a decisive verdict** (no float ranks/curvature) | BSD | stable |
| `code/ring_lemma_verification.py` | v16.0 SSOT (Phase 64.1; ALL_PASS this session) | det_3 cross-term `2Re((x2 x1)x3)`, Tr/Tr2/c/polarize_d, octonion Fano mul, inner_derivations (324), exact-only guard | in-repo | FROZEN — copy/reuse VERBATIM, do not edit |
| `code/bulk_geometry_verification.py` | v17.0 (3119 ln; imports clean w/ `_ODG` this session) | warm h_3(O) engine (verbatim copy of the SSOT) + Totaro/Levi-Civita curvature harness + F_4/E_6/stabilizer/Peirce machinery + signature bridge | in-repo | warm — REUSE its functions; add v18.0 sections, do not rebuild |
| `code/orbit_dimension_gate.py` | (`_ODG`) | exact-over-QQ rank/orbit/stabilizer helpers (`exact_qq_rank`, `span_rank_over_QQ`) + single/pair-copy calibration anchors | in-repo | warm — REUSE |

### Supporting Tools

| Tool | Version | Purpose | When Needed |
| ---- | ------- | ------- | ----------- |
| `sympy.diffgeom` (`Differential`, `WedgeProduct`, `CoordSystem`) | bundled w/ sympy 1.14 | exact exterior derivative + wedge of SCALAR rational forms | OPTIONAL — only if a scalar-form sanity layer is wanted; the matrix-valued F must be hand-rolled regardless. Recommend hand-rolled components throughout for uniformity. |
| `code/peirce_coupling.py` | in-repo | Peirce decomposition under E_11 (cross-check of `peirce_indices_under_E11`) | Phase 0 / A anchor cross-check |
| `code/embedding_under_E_verification.py` | in-repo (v15.0) | provenance ancestor of the engine; the original exact-SymPy octonion/Jordan source | reference only — already copied into the two primary modules |

### BANNED (auto-fail if used on a decisive path)

| Tool | Why banned |
| ---- | ---------- |
| `code/octonion_algebra.py` | buggy `(x1 x2)x3` cross-term order (annihilated by only 30/324 inner derivations, det off by 16 at the octonionic test point — NOT F_4-invariant), float64 reference spec, 0.67 associator gap. NEVER import on a decisive path. The existing engines assert it is imported 0 times outside the explicit oracle fence (`exact_only_guard`). The v18.0 sections must preserve that guard (extend `exact_only_guard_p70`-style to a `_p74`). |
| numpy float ranks / float curvature / float eigenvalues | `fp-float-decisive` forbidden proxy. Use `sympy.Matrix.rank()` / `_ODG.exact_qq_rank` / `eig_signature_count` (exact `real_roots`) only. |
| SageMath / GAP / Macaulay2 / any external CAS | not in the venv; would break the self-contained `python3 code/<file>.py` discipline and the provenance/verbatim-copy lock. Everything needed is reproducible in pure SymPy (confirmed this session). |

---

## Data Flow

```
det SSOT (ring_lemma_verification.det_3, cross-term 2Re((x2 x1)x3), F_4-invariant)
  -> [Phase 0] tangent identity: L_{E_11} spectrum -> Peirce V_1(1)/V_{1/2}(16)/V_0(10)
                                  E_11 o delta = (1/2) delta for delta in V_{1/2}; T_{E_11}OP^2 = V_{1/2}
                                  calibration: e6=78, orbit(E_11)=17, Stab_{E_6}=61, Stab_{V_0}=45
  -> [Phase A]  idempotent field E(x); soldering form e = dE valued in V_{1/2}(16) (indices 11..26)
                  pi_u (C_u, u=e_7) reduction:  V_{1/2}(16) --pi_u--> 4-dim coframe?   [image dim, EXACT]
                  Gram pairing of the 4-dim coframe -> eig_signature_count -> (1,3)?    [Lorentzian?]
                  residual structure group on the coframe -> exact span rank -> ⊇ SO(3,1)? FORCED?
                  ===KILL GATE=== (not 4d / not Lorentzian / not forced => route DEAD, STOP)
  -> [Phase A.5] eigenprojector QGT of |psi(x)>=rank-1 state at E(x):
                  Re(QGT) -> Fubini-Study  ==consistency==>  reproduce dead Hess(-log det) (cone-Hessian)
                  Im(QGT) = Berry curvature F_B  -> M=0 vacuum level (flat / pure-Lambda?)
                  turn on M in V_{1/2}: is F_B Einstein-shaped or EM-shaped? same-wall vs T[M]?
                  ===SOFT KILL=== (F_B reproduces the cone-Hessian same-wall mismatch => recommend STOP)
  -> [Phase B]  (only if A, A.5 survive)
                  coframe e = pi_u(dE) invertible (det(e^a_mu) != 0)
                  omega = Lorentz Spin(3,1) block of the ambient connection compatible with e
                  A = omega (+) e  (10-dim (A)dS/Poincare);  F = dA + A^A  [hand-rolled matrix forms]
                  Lorentz block of F  ==identify==>  R(omega) (4d Riemann)
                  ==cross-check>= 5 components== Totaro (totaro_riemann) vs Levi-Civita (hand_rolled_riemann_of_g)
                  vacuum M=0: Ric ~ Lambda g? (H^3 K=-1/2 sign benchmark);  then M != 0 sourced Riemann
  -> [Phase C]  is the MM epsilon-contraction (the Einstein term) FORCED by the trace-form/cubic-norm
                  pairing, or POSITED?  (fp-imported-action audit; AST-guard: no MM/EH action import)
```

## Computation Order and Dependencies

| Step | Depends On | Produces | Can Parallelize? |
| ---- | ---------- | -------- | ---------------- |
| 0. Engine recovery + tangent identity + calibration | det SSOT (run `ring_lemma_verification.py`, assert ALL_PASS); `_ODG` anchors | confirmed E_11 Peirce split {1,16,10}; `E_11∘δ=½δ`; `T_{E_11}OP^2=V_{1/2}`; e6=78/orbit=17/Stab=61/45 | within step: anchors independent (yes) |
| A. C_u coframe reduction (THE KILL GATE) | Step 0; the Phase-46 `pi_u` mechanism (reuse from 52-kkt) applied to V_{1/2} | image dim of `pi_u(V_{1/2}(16))` (expect 4); Gram signature (expect (1,3)); residual group rank (⊇ SO(3,1)?) | the 3 clauses (dim / signature / forced) are independent — yes |
| A.5 Berry-curvature same-wall gate | Step 0; eigenprojector QGT layer (NEW) | `F_B=Im(QGT)`; `Re(QGT)`=FS=cone-Hessian anchor; M=0 vacuum level; Einstein- vs EM-shape verdict | Re vs Im parts independent — yes; runs in PARALLEL with A (no dependency) |
| B. Full Cartan curvature F=dA+A∧A | A AND A.5 both SURVIVE; matrix-forms layer (NEW); Totaro+Levi-Civita harness (reuse) | tetrad non-degeneracy; omega; F; Lorentz block = R(omega); ≥5-component Totaro-vs-LeviCivita cross-check; vacuum + sourced Riemann | the ≥5 cross-check components are independent — yes |
| C. Circularity audit | B SURVIVES | forced-vs-posited verdict on the epsilon-contraction; AST guard certifying no MM/EH action import | n/a |

**Critical ordering note (from the milestone spec, binding):** Phase A and A.5 are the CHEAP KILL/SOFT-KILL gates and MUST run before the expensive Phase B connection machinery. A clean KILL (not 4d / not Lorentzian / not forced) or a SOFT KILL (F_B same-wall mismatch) is a full, publishable pass — negative-result-is-success.

## Resource Estimates

| Computation | Time (estimate) | Memory | Notes / hazard |
| ----------- | --------------- | ------ | -------------- |
| Run `ring_lemma_verification.py` (engine recovery) | ~30-90 s (this session: well under the 200 s timeout, exit 0) | < 1 GB | confirmed ALL_PASS this session |
| `peirce_indices_under_E11`, calibration anchors (`stab_E6_E11`, `e6_dimension`) | seconds-to-low-minutes (rref of the 729-flattened e6 stack) | < 1 GB | the `build_e6_basis` rref is the heaviest Phase-0 op; already warm in the engine |
| Phase A: `pi_u(V_{1/2})` image dim + Gram signature + residual rank | seconds (16-dim -> 4-dim linear maps, `exact_qq_rank` + `eig_signature_count`) | low | CHEAP — this is why it is the first gate |
| Phase A.5: eigenprojector QGT (2-3 level model) | seconds-to-minutes (diff of a rank-1 projector + small matrix products); minutes if the projector is the full 27-dim h_3(O) state | low-medium | use `cancel`, not `simplify`; the rational-function denominators grow but stay tractable |
| Phase B: `F=dA+A∧A` (10x10 (A)dS connection) | minutes (per-component matrix diff + commutator over Q) | low | the connection matrices are small; the cost is in `omega` extraction (metric-compatibility solve), not the wedge |
| Phase B: Totaro Riemann at a rational slice point (n=4) | low minutes (`totaro_riemann(..., simp=cancel)`) | medium | reuse the warm `cubic_form_C` cache; the 27-coord symbolic Hessian build is the ONE heavy step — cache it (the engine already does, `_II_DERIV_CACHE`) |
| Phase B: Levi-Civita cross-check (≥5 components) | low minutes (`hand_rolled_riemann_of_g`, evaluate-at-point-then-invert strategy) | medium | the engine's WATCHDOG-SAFE strategy (diff symbolic, THEN substitute rational point, THEN 4x4 inv) is mandatory — a fully-symbolic `g.inv()` blows up |

**WATCHDOG / STALL HAZARD (high — documented project-wide).** Long no-output symbolic runs get killed: the executor stream-watchdog kills ~150 s+ silent runs and the API socket closes ~50-65 min compute-heavy agents (0-token return). MITIGATIONS, all already practised in the engine: (1) run foreground with `python -u` (unbuffered) and emit a `_report(...)` line per check so output never goes silent; (2) the "differentiate-symbolic-then-substitute-rational-point-then-invert" pattern (never a symbolic matrix inverse of the 27-coord or even the 4-coord-symbolic Hessian); (3) `cancel` over `simplify` on rational-function entries; (4) cache the heavy 27-symbol jet once (`_II_DERIV_CACHE` precedent); (5) commit task-by-task so a socket-close loses nothing (recover via `git log`, not re-run). Storage/HPC: none needed — this is a single-core exact-symbolic workload, < 1 GB RAM throughout.

## Integration with Existing Code

This is a CONTINUATION milestone (Phases 74+). The new computations bolt onto the warm v17.0 engine. **Reuse, do not rebuild.**

- **Input format:** h_3(O) elements as the engine's 27-coordinate layout (`X_from_symbols`, `xs = symbols('x0:27')`); octonions as 8-tuples of SymPy rationals (Fano `e1·e2=e4`, conjugate `u=e_7`); idempotent `E_11 = h3o_from_coords(1,0,0, oct_zero(),oct_zero(),oct_zero())`.
- **Output format:** SymPy `Matrix` (rational entries) for metrics/curvature blocks; nested lists `R[i][j][k][l]` for the Riemann tensor (the harness convention); dicts `{label: (value, ok_bool)}` via `_report` for the assert harness.
- **Interface points (specific functions to call / extend):**
  - **det SSOT:** `ring_lemma_verification.det_3` (L308) — the cubic norm; `det_3_block` (bulk_geometry L382) — the **cross-term OFF-switch** (Phase A.5/B off-switch diagnostic, the V_0<->V_{1/2} coupling removed). `inner_derivations()` (324 brackets) — F_4-invariance / Phase-C forced-contraction tests.
  - **Peirce / tangent (Phase 0, A):** `peirce_indices_under_E11()` (L1753; confirmed `{1:1, 1/2:16, 0:10}` this session). **The V_{1/2} soldering sector is engine indices 11..26** (= `V_NORMAL_IDX` minus index 0; V_NORMAL_IDX=L1749 = `[0]+range(11,27)`). The C_u reduction `pi_u` must act on those 16 indices.
  - **Stabilizer / forced-structure-group (Phase 0 calibration, A clause c):** `stab_E6_E11` (L1815), `stab_preserving_V0` (L1844), `v0_orbit_under` (L1891), `build_e6_basis`/`e6_dimension` (L1789/L1802), `_ODG.exact_qq_rank`/`span_rank_over_QQ`. The `orbit_dimension_gate`-style stabilizer counts decide "FORCED vs arbitrary". `second_fundamental_form` (L1951) is the position-dependence anchor reused from the v17.0 LINCHPIN.
  - **Curvature harness (Phase B):** `cubic_form_C` (L1382) -> `totaro_riemann` (L1397) -> `riemann_symmetry_ok` (L1423) / `ricci_scalar` (L1439) / `kretschmann` (L1451) / `sectional_curvature` (L1478); INDEPENDENT cross-check `hand_rolled_riemann_of_g` (L2236, ≥5 components, Levi-Civita); Einstein-shape test `ricci_decomposition_n4` (L2329, S/Weyl split).
  - **Signature bridge (Phase A, B vacuum):** `eig_signature_count` (L2369, exact `real_roots`) for the (1,3) Lorentzian verdict on the coframe Gram and on Ricci eigenvalues; `_eta_minkowski`/`_frame_jacobian_bg_to_mink`/`minkowski_reduction` (L1207/1213/1228) for the h_2(C_u)≅R^{3,1} frame; `h3_cone_hessian_benchmark` (L1512) is the **K=-1/2 sign benchmark** to fix conventions before ANY curvature verdict.
- **NEW code to add (two small layers, ~150-300 ln total, in a fresh `code/cartan_curvature_verification.py` that VERBATIM-copies Sections 1-9 of the SSOT engine, matching the v17.0 copy precedent):**
  1. `pi_u_reduce(V_half_basis)` — the C_u bottleneck on the 16 V_{1/2} indices (mirror the Phase-46 `h_2(O)->h_2(C_u)` mechanism); returns the reduced coframe + image dim.
  2. `cartan_curvature(A_components)` — `F_{μν}=∂_μ A_ν − ∂_ν A_μ + [A_μ, A_ν]` (matrix forms; tested exact-over-Q this session).
  3. `qgt_eigenprojector(P, coords)` — `Q_{μν}=Tr(P ∂_μP ∂_νP)`, `g^{FS}=Re`, `F_B=Im=−i Tr(P[∂_μP,∂_νP])` (tested exact-over-Q(i) this session).
  4. A `_p74`-scoped `exact_only_guard` extending the existing guard (assert 0 `octonion_algebra` imports outside the fence, 0 float-rank calls).

## Validation Strategy

| Result | Validation Method | Benchmark / expected | Source |
| ------ | ----------------- | -------------------- | ------ |
| det SSOT integrity | run `ring_lemma_verification.py`; assert ALL_PASS + 324/324 inner-derivation annihilation + exact-only guard | exit 0, ALL_PASS | confirmed THIS SESSION (exit 0) |
| E_11 Peirce split | `peirce_indices_under_E11()` eigenvalue->count | `{V_1:1, V_{1/2}:16, V_0:10}` | confirmed THIS SESSION |
| sympy.diffgeom exactness (scalar forms) | `Differential`/`WedgeProduct` of rational-coeff forms; check no `Float` atoms | exact rationals, no Float | confirmed THIS SESSION |
| matrix-valued F=dA+A∧A | hand-rolled `∂A−∂A+[A,A]`; antisymmetry `F_{μν}=−F_{νμ}`; no Float | exact, antisymmetric | confirmed THIS SESSION (toy so(2,1)) |
| QGT/Berry curvature | eigenprojector `−i Tr(P[∂P,∂P])`; check `P^2=P`, `Tr P=1`, no Float | exact over Q(i) | confirmed THIS SESSION (rank-1 rational P) |
| Riemann SIGN convention | `h3_cone_hessian_benchmark` sectional curvature on H^3 | constant, NEGATIVE, **K=−1/2** (round-metric cross-check −1, factor 2) | engine docstring L1512; ref-totaro |
| Totaro vs Levi-Civita Riemann | `simp(R_totaro − R_handrolled) == 0` on ≥5 components (carry the documented uniform −1 sign) | exact agreement | `hand_rolled_riemann_of_g` L2236 |
| Lorentzian signature | `eig_signature_count` on the coframe Gram (Phase A) and Ricci eigenvalues | (1,3) i.e. (npos,nneg,nzero)=(1,3,0) | `eig_signature_count` L2369 (exact `real_roots`) |
| Einstein-shape (Phase A.5/B) | `ricci_decomposition_n4`: `resid_zero` True; track `S_zero`/`weyl_zero` vs M | R=Scal+E+Weyl exact; S,Weyl track M iff Einstein-sourced | `ricci_decomposition_n4` L2329 |
| FS = cone-Hessian consistency | `Re(QGT)` reproduces `Hess(-log det)` restricted to the slice | match (the dead v17.0 real part) | Provost-Vallee; v17.0 cone-Hessian |
| Forced vs arbitrary (Phase A c, C) | exact span rank of residual generators; AST guard no MM/EH action import | ⊇ SO(3,1) forced by (E_11,u); no posited action | `_ODG` rank + AST guard (v17.0 circularity-audit precedent) |

---

## Open Questions

| Question | Why Open | Impact on Project | Approaches Being Tried |
| -------- | -------- | ----------------- | ---------------------- |
| Does `pi_u` send V_{1/2}(16) to exactly **4** dims (paralleling V_0->h_2(C_u))? | the C_u bottleneck was derived for V_0=h_2(O)->R^{3,1}; its action on the 16-dim V_{1/2} half-eigenspace is the untested core | THE Phase-A KILL GATE; if not 4 -> route dead | apply the Phase-46 `pi_u` to indices 11..26, `exact_qq_rank` of the image |
| Is the reduced coframe Gram Lorentzian (1,3)? | the V_{1/2} pairing's signature is not a priori the same as V_0's | Phase-A KILL clause (b) | `eig_signature_count` on the Gram, exact `real_roots` |
| Is the 4d reduction FORCED by (E_11,u) alone, or does it need an extra arbitrary choice? | `fp-arbitrary-reduction` forbidden proxy — a hand-smuggled 4d coframe is not a result | Phase-A KILL clause (c) + Phase-C | exact stabilizer/residual-group rank; count the data fixed vs chosen |
| Is the Berry curvature `F_B` exactly over Q or Q(i)? | the QGT imaginary part lands in Gaussian rationals (confirmed this session) | exactness guarantee holds, but verdicts must be stated over Q(i), and `eig_signature_count`/rank must accept Q(i) entries | confirm `sympy.Matrix.rank()` / `real_roots` behave over Q(i) (rank does; real_roots needs the charpoly to have real/rational structure — separate Re/Im if needed) |
| Does `omega` (Lorentz spin connection) have a UNIQUE metric-compatible/torsion-free solution over Q? | the `omega` extraction is a linear solve; over-/under-determined-ness is unknown until tried | Phase B clause (b) feasibility | exact linear solve; check solution-space dim with `_ODG` rank |
| Is the MM epsilon-contraction fixed by the trace-form/cubic-norm? | the whole STRONG-WIN vs fp-imported-action verdict | Phase C | compare the cubic-norm pairing's natural contraction to the MM epsilon; AST-guard against importing the action |

## Anti-Approaches

| Anti-Approach | Why Avoid | What to Do Instead |
| ------------- | --------- | ------------------ |
| `code/octonion_algebra.py` for any octonion mul / det / associator | buggy `(x1 x2)x3` order (30/324 invariance, det off by 16), float64, 0.67 associator gap — BANNED | `ring_lemma_verification` Fano `oct_mul` + `det_3` (SSOT); keep the `exact_only_guard` |
| numpy / float ranks, float eigenvalues, float curvature on a verdict | `fp-float-decisive` forbidden proxy; rank is discontinuous and float-fragile | `sympy.Matrix.rank()`, `_ODG.exact_qq_rank`, `eig_signature_count` (exact `real_roots`) |
| `sympy.diffgeom` for the matrix-valued Cartan curvature `A∧A` | diffgeom has no native Lie-algebra-valued connection wedge; forcing it invites error/blow-up | hand-rolled component matrices `F_{μν}=∂A−∂A+[A,A]` (tested exact this session) |
| Fully-symbolic `g.inv()` of the 27-coord (or even 4-coord-symbolic) Hessian | watchdog/socket-close blow-up (documented) | differentiate symbolic, substitute the rational basepoint, THEN invert the rational 4x4 (engine's WATCHDOG-SAFE pattern) |
| `simplify` on large rational-function curvature entries | slow -> silent -> watchdog kill | `cancel` (the engine default for rational-function-at-a-point) |
| Reusing the v17.0 cone-Hessian Riemann as the load-bearing gravity tensor | it returned NONE; this route is the ANTISYMMETRIC/Berry tensor (a DIFFERENT object) — the FS real part is a CONSISTENCY ANCHOR only | compute `F=dA+A∧A` / `F_B=Im(QGT)`; use `Re(QGT)` only to re-derive the (dead) cone-Hessian as a cross-check |
| Positing an MM/EH action to get the Einstein term | `fp-imported-action` = the GST sin; auto-fail as load-bearing | Phase C audit: is the epsilon-contraction FORCED by the trace-form/cubic-norm? AST-guard against the action import |
| SageMath/GAP/Macaulay2 | not in venv; breaks self-contained reproducibility + provenance lock | everything reproducible in pure SymPy (confirmed this session) |

## Logical Dependencies

```
det SSOT (F_4-invariant, 324/324)          -> EVERYTHING (a wrong cross-term silently corrupts all curvature)
E_11 Peirce split {1,16,10}                -> V_{1/2}(16) = engine indices 11..26 = the soldering sector
pi_u(V_{1/2}) image dim == 4 (Phase A)     -> Lorentzian-(1,3) gate -> forced-SO(3,1) gate (the KILL chain)
A AND A.5 SURVIVE                          -> Phase B is even attempted (else STOP, report KILL/SOFT-KILL)
Riemann SIGN pinned (K=-1/2 benchmark)     -> any Einstein/(A)dS vacuum verdict is readable
Totaro == Levi-Civita on >=5 components    -> the F-Lorentz-block-is-Riemann identification is trusted
epsilon-contraction FORCED by trace-form   -> STRONG WIN; else fp-imported-action (honest partial)
Berry F_B over Q(i) (not Q)                -> state verdicts over Q(i); split Re/Im for real-root signature
```

## Recommended Investigation Scope

Prioritize (cheap-first, matching the milestone's KILL-gate ordering):
1. **Reproduce as validation:** `ring_lemma_verification.py` ALL_PASS (done this session) + the calibration anchors (e6=78, orbit(E_11)=17, Stab=61/45) via `orbit_dimension_gate` BEFORE trusting any new stabilizer count.
2. **Core gate (Phase A):** `pi_u(V_{1/2}(16))` image dim + Gram signature + forced-residual-group — the whole route lives or dies here, and it is cheap (seconds).
3. **Core diagnostic (Phase A.5):** eigenprojector `F_B=Im(QGT)`; `Re(QGT)`=cone-Hessian consistency anchor; Einstein- vs EM-shape same-wall check.
4. **Frontier (Phase B, only if 2+3 survive):** `F=dA+A∧A`, Lorentz block = Riemann, Totaro-vs-Levi-Civita ≥5-component cross-check, vacuum + sourced Riemann.
5. **Frontier (Phase C):** the forced-vs-posited epsilon-contraction audit.

Defer / avoid: any full symbolic 16-dim coframe curvature before Phase A confirms the 4d reduction (wasted compute if A kills); any MM-action contraction before Phase C frames it as the audit target (else it contaminates the result).

## Sources

- SymPy `diffgeom` module docs (v1.14.0) — exterior derivative (`Differential`), `WedgeProduct`, `CoordSystem`, `metric_to_Christoffel_2nd`; confirms scalar-form exactness, no native matrix-valued connection wedge. https://docs.sympy.org/latest/modules/diffgeom.html
- Avron-Graf-Kohmoto eigenprojector calculus for the QGT / Berry curvature — "Berry Curvature and Quantum Metric in N-band systems: an Eigenprojector Approach", arXiv:2102.09899 (Phys. Rev. B 104, 085114) — the projector formulas `g_ij = Re Tr(∂_iP ∂_jP)`, `F_ij = −i Tr(P[∂_iP,∂_jP])` used (exact over Q(i) this session).
- "Gauge-invariant projector calculus for quantum state geometry", arXiv:2412.03637 — gauge-invariant projector QGT (confirms the eigenprojector route avoids state-phase gauge-fixing, the right choice for symbolic exactness).
- Totaro, "The curvature of a Hessian metric", arXiv:math/0401381 — the closed-form `R_ijkl = -(1/4)g^{pq}(C_jlp C_ikq − C_ilp C_jkq)` used by `totaro_riemann` (3rd derivatives only; the jet terminates for the cubic det).
- In-repo (the load-bearing reuse, all confirmed present/runnable this session): `code/ring_lemma_verification.py` (det SSOT, ALL_PASS exit 0), `code/bulk_geometry_verification.py` (Totaro+Levi-Civita harness + F_4/E_6/stabilizer + signature bridge, imports clean), `code/orbit_dimension_gate.py` (`_ODG` exact-QQ rank/orbit machinery).
- Provost & Vallee, Comm. Math. Phys. 76 (1980) 289 — QGT real part = Fubini-Study, imaginary part = Berry curvature (the Re/Im split that makes the cone-Hessian a consistency anchor for this route).
