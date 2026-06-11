# 88 — RESEARCH: The Spinor Moment — the Tangent-Valued Matter Field and its Topology

**v28.0 Phase 88 (J5-on-the-variety, step 4). Verification-and-extraction.
Drivers: `code/variety_spinor_moment.py` (executor, 14/14 PASS),
`code/variety_spinor_moment_verify.py` (independent path, 9/9 PASS). Exact over Q/Q(t).
VERDICT: E1 PASS, E2 PASS, E3 PASS (Euler closure Σ=3=χ exact on CP² and OP²), E4 reading.**

This run builds the object both prior Gate-5 ledgers point at — the SPINOR MOMENT, the
tangent-valued matter field — and extracts its exact zero/index/winding topology. Per
v27-LIVE it is the natural next step, NOT forced. **FENCE (standing):** this is NOT the
dead v18/v20 Cartan/MM-connection route (a spacetime connection from FIBER data, closed).
Here the variety is the candidate BASE, and the question is the kinematics of its own
tangent gluing vs matter — no gravity claims, no metric law, no selection law, no
Einstein/Newton/G=κT/dark-matter/geodesic language.

---

## 0. The object

For a state `X` and event `p` (rank-1 idempotent), the spinor moment is the Peirce-1/2
projection
> **`s_X(p) := π_{1/2}^{(p)}(X) ∈ J_{1/2}(p) = T_p(variety)`** (16-dim; cut 4-dim).

It is computed two ways (cross-path): entry-extraction at `E_ii`, and the Jordan
eigenprojector `P_{1/2} = 4L_p(I − L_p)` (`L_p` spectrum `{0,½,1}`), agreeing exactly.

---

## 1. E1 — the identification (the unification)

By the v27 gradient calculus, for a tangent `v ∈ J_{1/2}(p)`, `dφ_X(v) = ⟨X,v⟩ =
⟨π_{1/2}^{(p)}(X), v⟩`, so **`s_X = dφ_X`** — the tangent-valued matter field is the v24
landscape's OWN gradient, not a new construction (verified for symbolic `X` at `E_11` and
via `d/dt φ_X(p(t))|_0 = ⟨s_X, ṗ(0)⟩` along all 16 families, both paths). Its norm is
scalar-local:
> **`‖s_X‖²_tr = TrX² − a² − (TrX − a)² + 2c`**, `a = ⟨X,p⟩`, `c = ⟨X#,p⟩`

(Peirce orthogonality `‖X‖²_tr = ‖π_1‖² + ‖π_{1/2}‖² + ‖π_0‖²`, with `‖π_1‖² = a²`,
`‖π_0‖² = (TrX − a)² − 2c`; for traceless `M` this is the v27 `2(½TrM² − a² + c)` — the
trace-form norm, twice the v27 reduced norm). The DIRECTION is the data the scalars miss
(v24 direction-resolution): two `X` with equal `(a, c, TrX², detX)` at `p` have different
`s_X` direction (e.g. `diag(7,5,3) + F_12(1)` vs `+F_12(e_1)`).

---

## 2. E2 — zeros = the matter eigenframe

`s_X(p) = 0 ⟺ X ∈ J_1(p) ⊕ J_0(p) ⟺ p` is compatible with the spectral frame of `X`
(operator characterization `[X,p] = 0`, verified independently of the projection). For `X`
with DISTINCT spectrum: exactly the three eigenframe idempotents `{p_1, p_2, p_3}` — three
isolated zeros, on the cut (when `X ∈ h_3(C_u)`) and on OP² alike. Verified for diagonal
`X`, a permutation-rotated frame (`g·X`, zero at `g·E_ii` — F₄-covariance EXPLICIT), and an
octonionic/rotated idempotent frame (`s_p(p) = π_{1/2}^{(p)}(p) = 0`). **Degenerate strata
(recorded, EXCLUDED from index claims):** `X = I/3` ⇒ `s ≡ 0` identically (the vacuum
singles out NO events — consistent with v24 homogeneity; a Gate-1 control, not a defect);
a double eigenvalue (`diag(5,5,3)`) gives one isolated zero (`E_33`) plus a positive-
dimensional zero locus (a `CP¹` on the cut / `S⁸`-type on OP²) in the degenerate
eigenspace.

---

## 3. E3 — the topology (the extraction)

Wlog `X = diag(x_1 > x_2 > x_3)` (F₄ spectral + covariance). `φ_X` is Morse off the
degenerate strata with critical points `E_11, E_22, E_33` (critical values `x_1, x_2, x_3`).
The Hessian along the `(i→j)` family direction is `∝ (x_j − x_i)` (anchor: along the
`(1,0)`-family, `φ''(0) = 8(x_2 − x_1)`, the `t`-parametrization NOT geodesic-normalized —
the factor-8 / ¼ bookkeeping tracked once, the v25 `λ₁` convention as reference). Counting
descending directions (`x_j < x_i`):

| | `E_11` (max) | `E_22` (saddle) | `E_33` (min) | Euler |
|---|---|---|---|---|
| **Morse index, cut** | 4 | 2 | 0 | |
| **Morse index, OP²** | 16 | 8 | 0 | |
| **Poincaré–Hopf `(−1)^{ind}`** | +1 | +1 | +1 | **Σ = 3** |

All Morse indices are EVEN, so every Poincaré–Hopf index is `+1`, and
> **Σ indices = 3 = χ(CP²) = χ(OP²)** — the Euler closure comes out EXACTLY on BOTH spaces

(χ(OP²) = 3, `b_0 = b_8 = b_16 = 1`, Borel — recorded math, cited; `χ(CP²) = 3`). The OP²
index `16` is `4 ×` the cut index at `E_11` (the 16-vs-4 tangent), but the indices and Euler
total are IDENTICAL — `χ` is dimension-blind. The v25 cross-check holds exactly:
`Δφ(E_11) = ¼·Σ_cut φ''(0) = 4(x_2 + x_3 − 2x_1) = −12(φ − φ̄)(E_11)` (`λ₁ = 12`).

**The C_u-winding decomposition (the extracted new numbers; conventions stated).** Each cut
tangent `C_u`-line is oriented by the `C_u` complex structure `J` (`e_7`-multiplication);
`s_X` restricted to a line is `z ↦ (x_j − x_i)·z`, a real-scalar map, so the `C_u`-phase
WINDING is `+1` per line, and the total `S³` degree at each zero is the product `= +1 =`
Poincaré–Hopf. The matter-pinned datum is the WEIGHT SIGN `sign(x_j − x_i)` (source/sink
along each line) — the moment-polytope vertex data, X-determined:
> `E_11: (−,−)`,  `E_22: (+,−)`,  `E_33: (+,+)`  (`+` toward the larger eigenvalue).

For diagonal `X` this is literally the torus moment map on CP² (Atiyah /
Guillemin–Sternberg — cited, not claimed); the program-content is that these weights are
the MATTER eigenframe's, X-determined.

---

## 4. Gate 0 — the v22 dictionary (the one open identification)

On the cut, the tangent `J_{1/2}(E_11) ∩ h_3(C_u)` is two `C_u`-lines (the `(0,1)` and
`(0,2)` entries); `e_7`-multiplication is one compact SO(2) — the `C_u` complex structure
`J`. The v22.0 result (slot 82, `kkt_gluing_holonomy.py`): the inter-observer gluing
holonomy is an UNFORCED U(1) — joint pair-stabilizer Spin(8), slice action one compact
SO(2) = the `C_u` phase (`KK._Cu_complex_structure_slice` on the V_0 slice `x1`). The
DICTIONARY: this same circle acts on the spinor-moment tangent. Constructing the torus
generator `D(·) = [δU, ·]`, `δU = diag(0, −e_7/2, e_7/2)` (the f₄ element generating the
slot-82 circle):
> `D` acts on the V_0 slice (`x1`) as **`+1·J_Cu`** (the v22 slice SO(2)) and on the
> `J_{1/2}` tangent (`x2, x3`) as **`−½·J_Cu`** — the SAME circle, NONZERO on the tangent.

So the v22-unforced gluing U(1) **is** the `C_u` phase, and it acts on the variety's own
tangent (the v28 object) by the `C_u` complex structure (tangent weight `−½` vs slice `+1`,
a torus weight ratio, recorded). The dictionary holds; v28's object is the v22-U(1)'s action
on the base tangent. (Verified independently via a diagonal-unitary-conjugation torus
generator.)

---

## 5. E4 — the reading (fenced)

The v22-unforced gluing U(1) now has matter-pinned TOPOLOGICAL data: the zeros (WHERE = the
matter eigenframe), the indices/weights (HOW MUCH), both X-determined. What remains UNFORCED
is the LOCAL FORM of the gluing — whether there is a canonical matter-aligned connection and
what selects it — the v29 fork, NOT claimed here. **The vacuum pins nothing (`s ≡ 0`):
matter is what creates the topological skeleton.** This is connection-KINEMATICS on the
candidate BASE — NOT gravity, NOT a metric law, NOT a selection law; the v18/v20 Cartan/MM
corpse stays buried; "matter-pinned" refers to the topological class only.

**Through-line:** v24 found the field; v25 its closed form + forced operator; v26 its source
+ the MaxEnt theorem; v27 closed it into a local balance law (multiplier = the entropy
response); **v28 gives the field its topological skeleton — zeros at the matter eigenframe,
Euler closure χ = 3, the matter-pinned class for the v22 gluing-U(1).**

---

## 6. Citations

- A. Borel, "Le plan projectif des octaves et les sphères comme espaces homogènes," C. R. Acad. Sci. Paris **230** (1950) — `OP² = F_4/Spin(9)`, cohomology `b_0 = b_8 = b_16 = 1`, `χ(OP²) = 3`; F₄ transitive on rank-1 idempotents.
- M. F. Atiyah, "Convexity and commuting Hamiltonians," Bull. London Math. Soc. **14** (1982); V. Guillemin & S. Sternberg, "Convexity properties of the moment mapping," Invent. Math. **67** (1982) — for diagonal `X`, `φ_X|_cut` is the torus moment map on `CP²`; the fixed-point weights.
- J. Milnor, *Morse Theory*, Annals of Math. Studies 51 (1963) — Morse indices, Poincaré–Hopf `Σ(−1)^{ind} = χ`.
- K. McCrimmon, *A Taste of Jordan Algebras*, Springer (2004); T. A. Springer & F. D. Veldkamp, *Octonions, Jordan Algebras and Exceptional Groups*, Springer (2000) — the Peirce decomposition and projections `P_{1/2} = 4L_p(I−L_p)`.
- (Internal) v22.0 / slot 82 `kkt_gluing_holonomy.py` — the unforced gluing U(1) (Spin(8), the `C_u`-phase SO(2)).
