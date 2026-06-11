# 88 — GATE-3 VERIFICATION (independent): E3 topology — Morse indices, the Euler closure, the C_u-winding

**Phase 88 / v28.0 (J5-on-the-variety, step 4). Independent verifier. Exact over Q / Q(t).
Three code paths agree (executor 14/14, eigenprojector 9/9, from-scratch `/tmp/v28_indep_check.py`
18/18). The Morse indices below were re-derived from MY OWN Jordan-product Hessian signs — NOT
read from the drivers.**

Setup: diagonal X = diag(x₁>x₂>x₃) (F₄ spectral + covariance, justified in
88-GATE-2-VERIFICATION.md). φ_X(p)=⟨X,p⟩ is Morse off the degenerate strata with critical points
{E₁₁,E₂₂,E₃₃} and critical values {x₁,x₂,x₃}. The gradient field is the spinor moment s_X.

---

## The quantitative anchor: φ''(0) = 8(x_j − x_i), uniform per block. **CONFIRMED (HIGH).**

I built the recorded t-parametrized families myself (`v_i=c, v_j=s e_k`, s=2t/(1+t²)) and
computed φ_X''(0) along each. **Independently confirmed and SHARPENED** — for the diagonal X with
symbolic eigenvalues, every one of the 8 octonion directions in each off-diagonal block gives the
**identical** second derivative (a single value, set size 1):

| block | all 8 e_k directions give φ''(0) | = |
|---|---|---|
| E₁₁→E₂₂ (x₃ entry) | `−8X₁ + 8X₂` | `8(x₂−x₁)` |
| E₁₁→E₃₃ (x₂ entry) | `−8X₁ + 8X₃` | `8(x₃−x₁)` |
| E₂₂→E₃₃ (x₁ entry) | `−8X₂ + 8X₃` | `8(x₃−x₂)` |

So φ''(0) = 8(x_j − x_i) **uniformly across the whole octonion block**. The "8" is the
t-parametrization bookkeeping (NOT geodesic-normalized — guard #3, tracked once here; the v25
λ₁ convention is the reference). This uniformity is the crux of the index count below: each
octonion block is a single Morse "cell" of definite sign sign(x_j−x_i).

## Morse indices from REAL Hessian signs. **CONFIRMED (HIGH).**

Morse index at E_ii (as the descending-direction count of the gradient field s_X) = number of
directions with φ''(0) < 0 = number of blocks toward a SMALLER eigenvalue × (directions/block).
I computed the sign of φ''(0) for every direction at every E_ii from MY Jordan product (NOT an
assertion of 8):

| | toward larger eig | toward smaller eig | **cut** (e₀,e₇: 2 dirs/block) | **OP²** (all 8 dirs/block) |
|---|---|---|---|---|
| E₁₁ (x₁ largest) | — | both blocks (→x₂, →x₃) descend | **4** | **16** |
| E₂₂ | →x₁ (ascend) | →x₃ (descend) | **2** | **8** |
| E₃₃ (x₃ smallest) | both ascend | — | **0** | **0** |

- **Cut Morse indices = (4, 2, 0)** — **PASS** (MY Hessian signs).
- **OP² Morse indices = (16, 8, 0)** — **PASS** (MY Hessian signs over all 8 oct dirs/block).
  The 16 = 2 octonion blocks × 8 real directions each; the per-block uniformity (above) is what
  makes this honest. Each octonion off-diagonal block contributes 8 real tangent directions —
  correct (dim_ℝ O = 8).

## Poincaré–Hopf and the Euler closure. **CONFIRMED (HIGH); genuine-vs-hardwired settled.**

Poincaré–Hopf index of the gradient s_X at an isolated zero = (−1)^{Morse index}. Every Morse
index above is **even**, so the index is **+1 at each of the three zeros**, on both spaces.

> **Σ indices = 1+1+1 = 3 on the cut, and = 3 on OP².**

**Is this genuine or hardwired? — GENUINE.** The chain is:
1. The indices `(4,2,0)`/`(16,8,0)` come from **computed** Hessian-eigenvalue signs (the
   φ''∝(x_j−x_i) structure I re-derived), not from a hardcoded "3".
2. `(−1)^{Morse}` is integer arithmetic on those computed indices → all +1.
3. Their **sum is computed** to be 3.
4. **χ(CP²)=χ(OP²)=3 is a CITED classical fact** (Borel: OP² has b₀=b₈=b₁₆=1, all other Betti
   numbers 0; the torus moment-map picture is Atiyah / Guillemin–Sternberg). The code CITES this
   and CHECKS that the **computed** Σ equals the **cited** χ. It does NOT assert χ then claim it.
   This is the correct classical-vs-program split (guard #4): the Euler closure is a *consistency
   check* (computed gradient index sum == cited topological invariant), and it comes out exactly
   on both spaces. The honest novel content is the winding/weight decomposition below, not χ.

I verified each link independently: my own `(4,2,0)`/`(16,8,0)` → my own `(−1)^Morse=+1` →
my own `Σ=3`. The closure is not an input.

## v25 cross-check (Gate-1 control). **CONFIRMED (HIGH).**

From the four cut-family Hessians at E₁₁:
`Δφ(E₁₁) = ¼[2·8(x₂−x₁) + 2·8(x₃−x₁)] = 4(x₂+x₃−2x₁)` (I got exactly `−8X₁+4X₂+4X₃`), and this
equals `−12(φ−φ̄)(E₁₁) = −12(x₁ − TrX/3)` — **PASS**. Wires v28 to the certified v25 mean-curvature
law (λ₁ = 12 on the 4-frame cut). The ¼ and 8 bookkeeping is consistent with v25 (guard #3).

## The C_u-winding decomposition — THE EXTRACTED NEW NUMBERS (conventions stated).

**Convention.** Each cut tangent C_u-line at E_ii (the (i,j)-block restricted to span{1,e₇}) is
oriented by the C_u complex structure J (e₇-multiplication; the Gate-0 circle, weight −½ on the
tangent). Restricted to a line, s_X is the real-linear map z ↦ (x_j − x_i)·z. A real-scalar
multiple of the identity on a complex line has **degree (C_u-phase winding) +1** on that line's
circle; the **matter-pinned datum is the weight SIGN sign(x_j − x_i)** (which line is
source/sink). Per-zero weight-sign pattern (moment-polytope vertex data, X-determined):

| zero | C_u-lines (→ larger eig is +) | windings | Morse | PH index |
|---|---|---|---|---|
| E₁₁ | (−, −) | (+1, +1) | 4 | +1 |
| E₂₂ | (+, −) | (+1, +1) | 2 | +1 |
| E₃₃ | (+, +) | (+1, +1) | 0 | +1 |

Total S³ degree at each zero = product of line windings = +1 = the Poincaré–Hopf index. All
integers come from exact algebra (`sign(x_j−x_i)`, `(−1)^Morse`) — **no numeric integration**
(guard #2). The weight-sign triple `(−,−)/(+,−)/(+,+)` is the matter-pinned vertex labelling: the
first genuinely new datum the v28 object supplies to the v22-unforced U(1) at the level of the
topological class.

---

## Fence / honesty (E4 reading, fenced)

The v22-unforced gluing U(1) now carries matter-pinned TOPOLOGICAL data: the zeros (WHERE = the
matter eigenframe) and the indices/weights (HOW MUCH), both X-determined. What remains UNFORCED is
the LOCAL FORM of the gluing — the v29 fork, NOT claimed here. The vacuum pins nothing (s≡0):
matter creates the topological skeleton.

- Exactness (guard #2): all verdict-path computations over Q/Q(t); winding integers from exact
  algebra. No float in the verdict path (confirmed by inspection of both drivers).
- Classical-vs-program (guard #4): χ=3 and the Morse/torus-moment-map structure are classical
  (cited Borel; Atiyah/GS); the program content is the identification + the winding decomposition.
- Language fence (guard #6): connection-KINEMATICS on the candidate BASE. NO Einstein, NO Newton
  constant, NO G=κT, NO metric law, NO selection law, NO dark-matter/geodesic/"gravity=connection"
  language (the v18/v20 Cartan/MM corpse stays buried). "matter-pinned" = the topological class.
  Signature OPEN.

**E3: CONFIRMED (HIGH). The Euler closure Σ=3=χ is GENUINE (computed index sum checked against
the cited χ), not hardwired. The (16,8,0) OP² count is correct (8 real directions per octonion
block, per-block-uniform Hessian sign).**
