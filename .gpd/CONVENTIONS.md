# Notation and Convention Lock

Single source of truth (human-readable detail) for all conventions in this project.
The canonical machine-readable snapshot is `.gpd/state.json` field `convention_lock`
(checked by `gpd convention check`). If the two ever disagree, **state.json wins** —
flag the inconsistency to the notation-coordinator.

**Last Updated:** v17.0 Phase 70 (A0) — established 2026-05-30
**Status:** ACTIVE (v17.0). Supersedes the v16.0 (RING)-lemma lock.
**Subfield:** Mathematical physics / differential geometry of symmetric cones
(Jordan algebra h_3(O)) with a Lorentzian spacetime slice.

---

## 0. TWO MOST LOAD-BEARING CONVENTIONS (read these first)

1. **Determinant / cubic norm — SINGLE SOURCE OF TRUTH.**
   The Freudenthal cubic norm `det(X)` is computed by **`code/ring_lemma_verification.py`
   `det_3`** and nothing else. It uses cross-terms with order **`2Re(x2* x0* x1)`** and is
   certified `F_4`-invariant via Cayley-Hamilton + 324/324 inner-derivation annihilation.
   **DO NOT import `code/octonion_algebra.py`** — it has the buggy `(x1 x2) x3` association
   order, is float-only, and exhibits a measured **0.67 associator gap** on genuinely
   non-associative (e4..e7) octonion data. Polarization is **LOCKED**: `d(X,X,X) = 6·det(X)`.

2. **Metric signature — mostly-minus on the slice; Riemannian in the bulk.**
   The spacetime slice `h_2(C_u) ~ R^{3,1}` carries the **mostly-minus (−,+,+,+)** Lorentzian
   signature (from the slice's own `det_2`). The ambient `h_3(O)` positive cone is
   **Riemannian / positive-definite** with canonical metric `g_X = Hess(−log det)`.
   **v16.0's Riemannian-Fisher sign convention is RETIRED** (it belonged to the abandoned
   lattice route).

---

## 1. Spacetime / Geometry

| Category | Convention | Test value |
|----------|-----------|------------|
| Metric signature (slice) | **mostly-minus (−,+,+,+)** Lorentzian on `h_2(C_u)` via `det_2` | timelike `p^mu=(E,0)`: `p·p = E^2 − \|p\|^2 > 0`, i.e. `p^2 = m^2` for a massive particle (one `+`, three `−`) |
| Metric signature (bulk) | **Riemannian, positive-definite**; cone metric `g_X = Hess(−log det)` | `g_X` at center `X=I/3` restricted to the 4 slice directions = `diag(9,9,18,18)`, det `26244` (all eigenvalues > 0) |
| Slice Minkowski form | slice `det` at center = `b·g/3 − p^2/3 − q^2/3` | reproduces `eta` up to overall scale (Minkowski quadratic form) |
| Coordinate system | spacetime point `x in V_0`; background `X_bg = I/3 + M`; decisive coords = slice entries `{17,18,19,26}` (b,g,p,q), kept symbolic | dim-4 `h_2(C_u)` slice is the decisive arena |
| Index positioning | lower `mu,nu` on `g_mu_nu`, `h_mu_nu`; raise/lower with the slice metric. Cone indices `p,q` raised with `g^{pq} = P(X)` (quadratic representation) | Faraut-Koranyi: `g^{pq} = P(X)` |
| Riemann/Ricci sign | **STATE EXPLICITLY at Phase 70**; benchmark on `H^3` (constant curvature −1) before any verdict | `H^3 = SL(2,C)/SU(2)` (M=0, det=1 sub-slice): scalar curvature must come out negative, `−d^2/4 = −1` (d=2, rank-1) |

**Signature bridge (construction (ii) — LOCKED).**
`g_mu_nu(x) = eta_mu_nu + h_mu_nu(x)`, where `eta` is taken from `h_2(C_u)`'s **own** `det`
and the `h_3(O)` cone-Hessian supplies **only the perturbation** `h_mu_nu`.
**Enforce `g(center, M=0) = eta` EXACTLY** — never "rotate the answer".
Construction (i) (Wick-rotate via the complex structure `u`) is the **REJECTED** fallback:
it carries an unproven C*-bottleneck signature-flip conjecture, and naive coordinate Wick
rotation on a curved metric manufactures spurious curvature (Visser, arXiv:1702.05572).

---

## 2. Units

| Category | Convention | Test value |
|----------|-----------|------------|
| Natural units | **ħ = c = k_B = 1** | dimensionless geometric quantities |
| Arithmetic | **EXACT rational arithmetic over Q (NOT float)** on all decisive verdicts | slice `Hess` det `= 26244` returned exactly; curvature/rank verdicts as exact rationals |

Dimension map (natural units): `[length] = [time] = [energy]^{-1}`, `[mass] = [energy]`.
The decisive computations are dimensionless differential geometry on the cone, so unit
factors do not enter the verdicts; the binding requirement is **exactness over Q**.

---

## 3. Jordan Algebra h_3(O) (core)

| Category | Convention |
|----------|-----------|
| Jordan product | `X ∘ Y = (1/2)(XY + YX)`; `Tr(X ∘ Y) = Re Tr(XY)` for Hermitian `X,Y`. `XY` = formal 3×3 matrix product with entrywise octonion multiply. |
| Octonion basis | Fano plane, `e1·e2 = e4` (consistent across the whole project). |
| Complex structure | `u = e7`; `C_u = span{1, e7}`. Spacetime sub-slice = `h_2(C_u) ~ R^{3,1}`. |
| Cubic norm / det | Freudenthal `det` **WITH cross-terms**, order **`2Re(x2* x0* x1)`**. SSOT = `code/ring_lemma_verification.py det_3` (F_4-invariant, CH + 324/324). Polarization LOCKED `d(X,X,X) = 6·det(X)`. **NOT** `code/octonion_algebra.py` (buggy order, float, 0.67 gap). |
| Primitive idempotent | `E_11 = diag(1,0,0)`. |
| Center | `I/3` — the `F_4`-symmetric point, `rho_J = 0`. Test: `det(I/3) = 1/27`, `Tr(I/3) = 1`. |
| Peirce decomposition (under `E_11`) | `V_1(1) = R·E_11`, `V_{1/2}(16)`, `V_0(10) = h_2(O)`. Spacetime sub-slice `= h_2(C_u)` (4-dim), indices `{17,18,19,26}`. Matter `M ∈ V_1 + V_{1/2}`. |
| Commutator / anticommutator | `[A,B] = AB − BA`; `{A,B} = AB + BA`. |

---

## 4. Cone Geometry & Curvature

| Category | Convention |
|----------|-----------|
| Potential | **`−log det`** (FIXED at start; **do NOT mix with bare `det`**). |
| Cone metric | `g_X(A,B) = −∂_s ∂_t log det(X + sA + tB)\|_{s=t=0} = Hess(−log det)`. Inverse `g^{pq} = P(X)` (quadratic representation, Faraut-Koranyi). |
| Curvature engine | **Totaro closed form** `R_ijkl = −(1/4) g^{pq}(f_jlp f_ikq − f_ilp f_jkq)`, using **3rd derivatives of det only** (det cubic ⟹ `f_ijkl = 0`). Hand-rolled Christoffel/Riemann (beats `sympy.diffgeom`; ~19s exact on the dim-4 slice). |
| Decisive arena | **dim-4 `h_2(C_u)` slice.** dim-10 `V_0` is **off the critical path** (symbolic inverse times out > 200s; mpmath fallback only). |
| Christoffel | Levi-Civita connection of `g_X`: `Gamma^a_{bc} = (1/2) g^{ad}(∂_b g_dc + ∂_c g_db − ∂_d g_bc)`. |
| Riemann/Ricci sign | **state explicitly and benchmark on `H^3` (constant curvature −1) at Phase 70** before any physics verdict. |

---

## 5. Symmetry Groups

| Category | Convention |
|----------|-----------|
| `F_4` | `F_4 = Aut(h_3(O))`, compact, 52-dim; **fixes `det`** (and Tr, trace form). |
| `E_6` | `E_6 = Stab(det)` — the cone's isometry-relevant group. |
| Residual after fixing the slice | `Stab_{E_6}(E_11)` — parabolic, **Levi ~ Spin(9,1)**. Not cleanly tabulated; likely needs direct kernel computation `{D ∈ e_6 : D·E_11 = 0}` (or `/gpd:research-phase`). |

---

## 6. Matter Coupling, kappa, Lambda

| Category | Convention |
|----------|-----------|
| Matter `M` | `M ∈ V_1 + V_{1/2}`; "off-center-ness" measured by `rho_J(X_bg)`. |
| Coupling | curvature–matter coupling via the cubic-norm **cross-terms** `C_{(V_0)(V_1)(V_{1/2})}` (vs the pure `C_{(V_0)^3}`); the off-switch test replaces `det` by the block-diagonal product to kill the M-sourced curvature. (v16.0 "J>0 antiferromagnetic" lattice coupling is RETIRED.) |
| `kappa`, `Lambda` | `kappa` fitted in **Phase 73** as a **GLOBAL** constant. **`Lambda = 0`** (SUPERSEDED 2026-06-01 by Phases 70.1+72): the M=0 spacetime vacuum is **flat** KKT η, structurally DERIVED (NOT Einstein-negative). The pre-70.1 "center is Einstein with negative Ricci (Cartan), `Lambda < 0`" framing is FALSIFIED — that `{0,−1,−1,−1}`/`R=−3`/`R×H³` geometry is the cone-Hessian **SOURCE** field, not the spacetime metric `g=η+h`. Phase 73 = QUADRATIC-response linearized-Einstein test (use h⁽²⁾, since h⁽¹⁾=0); no Λ tripwire. |

---

## 7. Arithmetic / Engine Discipline

| Category | Convention |
|----------|-----------|
| Field | **EXACT over Q** (or Q-adjoin-surds) on all decisive verdicts. |
| Ranks | via **`sympy.Matrix.rank()`**, **NEVER `numpy.linalg.matrix_rank`**. |
| Warm engine | `code/ring_lemma_verification.py` + `code/embedding_under_E_verification.py`. |
| Banned | `code/octonion_algebra.py` on any decisive path (float-only formula reference at most). |
| Provenance caution | `peirce_coupling.py` / `h3o_tower.py` / `rho_directional_derivatives.py` may be absent or superseded; confirm provenance at Phase 70 — the engine above is the SSOT regardless. |

---

## 8. Cross-Convention Consistency (verified)

These conventions constrain each other; the interactions below were checked at establishment.

| Convention A | Convention B | Required relation | Status |
|--------------|--------------|-------------------|--------|
| Potential `−log det` | Cone metric | `g_X = Hess(−log det)` is positive-definite on the cone (convexity of `−log det`) | OK — `diag(9,9,18,18)` at center, all > 0 |
| `det_3` SSOT (cross-term `2Re(x2* x0* x1)`) | `F_4` fixes `det` | `det` must be `F_4`-invariant | OK — CH + 324/324 certification |
| Polarization `d(X,X,X)=6·det` | Cubic `det` | factor 6 = 3! from full symmetrization of a cubic | OK — consistent with Totaro `f_ijk` (3rd derivs) |
| Curvature engine uses `f_ijkl=0` | `det` cubic | a degree-3 norm has vanishing 4th derivative | OK — Totaro form valid |
| mostly-minus slice (−,+,+,+) | slice `det_2` Minkowski form | one timelike + three spacelike directions | OK — `b·g/3 − p^2/3 − q^2/3` |
| Construction (ii) bridge | `g(center,M=0)=eta` EXACTLY | no spurious constant offset (no fake Lambda / position-dependence) | ENFORCE at Phase 70 (gate) |
| Riemann sign (RESOLVED Phase 71) | `H^3` benchmark | sign pinned NEGATIVE & constant; cone-Hessian-SLICE sectional curvature = **−1/2**, round-metric reinforcement = **−1** (exact factor-of-2: `g_slice|_apex = diag(2,2,2) = 2·g_round`, so `K(2g)=K(g)/2`). Load-bearing fact is the negative constant SIGN, NOT the magnitude; do NOT force −1 | BENCHMARKED Phase 71 (cone-Hessian K=−1/2, round K=−1) |

**Numerical-factor watch list** (convention-determined factors to guard in derivations):
`1/2` (Jordan product), `6` (polarization `d=6·det`), `1/4` (Totaro Riemann prefactor),
`1/3` (center `I/3` entries), sign of scalar curvature (must be negative at the center / on `H^3`).

---

## 9. Reference Convention Maps

| Reference | Used for | Convention note / conversion |
|-----------|----------|-------------------------------|
| Faraut & Koranyi, *Analysis on Symmetric Cones* (1994) | cone metric `g_X = Hess(−log det)`, `g^{pq}=P(X)`, symmetric-space structure | direct adoption; single-state ring is Ch. II–IV (NOT Ch. V) |
| Totaro (2004), Cor 2.3 | curvature closed form `R_ijkl = −(1/4) g^{pq}(...)`; `H^3` constant curvature −1 | adopt Totaro's sign; benchmark on `H^3` to pin our Riemann sign |
| McCrimmon, *A Taste of Jordan Algebras* | Peirce decomposition, cubic norm, `P(X)` | direct adoption |
| Baez, "The Octonions" (2002) | `h_3(O)`, `F_4`, `OP^2 = F_4/Spin(9)` | direct adoption |
| Gunaydin-Sierra-Townsend (1983-84) | the scalar **manifold** `E_{6(−26)}/F_4` only | **DO NOT adopt their Lagrangian / SUSY closure** (the dead circular route) |
| Jacobson (1995) | contrast only | thermodynamic/ensemble route **explicitly rejected** |

---

## 10. Notes & Lineage

- **v17.0 route:** the positive cone of `h_3(O)` is an intrinsically curved Riemannian
  symmetric space; `E_11` picks the spacetime slice `V_0 ⊃ h_2(C_u) ~ R^{3,1}`; an off-center
  state picks a basepoint; gravity is the curvature the slice inherits from the bulk, sourced
  by matter `M ∈ V_1/V_{1/2}` via the cubic-norm cross-terms. **No lattice, no posited
  supergravity Lagrangian, no SUSY, no observers-make-gravity ensemble argument.**
- **Retired from v16.0:** the Riemannian-Fisher metric sign convention, lattice spacing
  `a=1`, the `J>0 antiferromagnetic` coupling, and the various `N/A (pure algebra)` field-theory
  placeholders that no longer describe this milestone. The v16.0 `c = Tr(X∘Y)` coupling
  generator is not load-bearing for v17.0.
- **Independence:** v17.0 is physics-side and INDEPENDENT of the v16.0 (RING) lemma and the
  v15.0 basin-restriction result. Do not entangle.

_All machine-readable fields mirror `.gpd/state.json` `convention_lock`._
