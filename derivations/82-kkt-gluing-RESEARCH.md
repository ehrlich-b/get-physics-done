# Derivation 82 — KKT-Slice Gluing Freedom & Three-Point Holonomy — GATE 0

**Milestone:** v22.0-candidate (the η-reading test).
**Scope of this document:** **Gate 0 only** (the identification space + the residual
group R_12). Gates 1/2/3 are **not** run — the orchestrator selects the next gate
from the Gate-0 result (fail-fast discipline).
**Spec:** `paper6-kkt-gluing-holonomy-prompt.md`, section "Gate 0 — the
identification space (pure structure, cheapest)".
**Conventions:** `.gpd/CONVENTIONS.md` (det SSOT, `octonion_algebra.py` BANNED,
`u = e_7`, slice coords `{1,2,3,10}`, mostly-minus `(+,−,−,−)`).
**Arithmetic:** EXACT over **Q** on every decisive number. No `numpy` on the decisive
path; ranks via `sympy.Matrix.rank()` / `DomainMatrix`-over-QQ.
**Numerology guard:** no `κ`, no `Λ`, no physical constants anywhere — this is pure
group theory / structure of `h_3(O)`.

Reproducibility: SymPy 1.14.0, Python 3.14.2, macOS Darwin 24.6.0. Deterministic
(no random seeds; all test elements hardcoded with exact rational entries).
Driver: `PYTHONPATH=code python3 -u code/kkt_gluing_holonomy.py` → exit 0, ALL_PASS.

---

## 1. Setup and exact definitions used (quoting the spec)

The standard frame `E_11 = diag(1,0,0)`, `E_22 = diag(0,1,0)`, `E_33 = diag(0,0,1)`
in `h_3(O)`; `F_4 = Aut(h_3(O))` (compact, dim 52) is transitive on primitive
idempotents with `Stab(E) ≅ Spin(9)`. The decisive arena is the observer's
4-dimensional Minkowski sub-slice `h_2(C_u)(E_11) ⊂ V_0(E_11)`.

Definitions adopted **verbatim** from the spec ("Definitions for this run"):

- **Identification** `E_i → E_j` := `g ∈ F_4` with `g·E_ii = E_jj` (hence `g` maps
  the Peirce decomposition of `E_ii` to that of `E_jj`, and `V_0(E_ii) → V_0(E_jj)`).
- **Slice action** of `g` := the induced map `h_2(C_u)(E_ii) → h_2(C_u')(E_jj)`
  (note: `g` need not respect the complex structures `u, u'` — that is a Gate-1
  condition, not assumed here).
- **Residual group** `R_ij` := the set of slice actions of
  `{g : g·E_ii = E_ii, g·E_jj = E_jj}` — the ambiguity left after both endpoint
  idempotents are fixed. Computed as a group, exactly.

For Gate 0 the load-bearing pair is `(E_11, E_22)`. Because
`E_33 = I − E_11 − E_22`, fixing both `E_11` and `E_22` automatically fixes the
**whole standard frame**, so `R_12` is the slice action of the joint frame
stabilizer.

### Slice coordinates (engine-native, from `CONVENTIONS.md`)

`h_2(C_u)(E_11)` is the 4-dimensional spacetime sub-slice. In the engine-native
27-coordinate layout (`H2CU_SLICE_IDX` in `bulk_geometry_verification.py:1750`):

| engine idx | meaning | Minkowski coord |
|---|---|---|
| 1 | `β` (diagonal slot 1) | enters `x0`, `x3` |
| 2 | `γ` (diagonal slot 2) | enters `x0`, `x3` |
| 3 | `Re(x1)` = `p` | `x1_M` (spatial) |
| 10 | `⟨x1, e_7⟩` = `q` | `x2_M` (spatial) |

Minkowski basis: `x0 = (β+γ)/2`, `x1_M = Re(x1) = p`, `x2_M = ⟨x1,e_7⟩ = q`,
`x3 = (β−γ)/2`; `det_2 = βγ − |x1|²_{C_u} = x0² − x1_M² − x2_M² − x3²`
(mostly-minus, timelike-positive). `u = e_7`, `C_u = span{1, e_7}`.

The remaining `V_0` coordinates `{4,5,6,7,8,9} = ⟨x1, e_1..e_6⟩` are the **internal
W-sector** (`V_0 ⊖ C_u`), killed by the `π_u` projection.

---

## 2. Engine map (file:line for every engine used)

Built on the warm v17–v21 EXACT-over-Q det-SSOT harness — **not** on the BANNED
float64 `code/octonion_algebra.py`, and **not** on Phase 52's KKT code (which was
built on that banned file). A source guard fires before any decisive computation.

| Engine call | File:line | Used for |
|---|---|---|
| `h3o_from_coords`, `X_from_symbols` | `ring_lemma_verification.py:193,400` | build idempotents / generic symbolic `X` |
| `_flat27`, `_standard_basis_27` | `ring_lemma_verification.py:675,682` | 27-vector flatten / standard basis |
| `jordan`, `det_3`, `Tr`, `Tr2` | `ring_lemma_verification.py:260,308,299,339` | det SSOT (cross-term `2Re((x2 x1) x3)`) |
| `jordan_L_matrix`, `inner_derivations` | `ring_lemma_verification.py:692,699` | `f_4 = Der(h_3(O))` (324 brackets) |
| `exact_qq_rank` (DomainMatrix-over-QQ) | `orbit_dimension_gate.py:154` | exact image/kernel dims at width 52 |
| `span_rank_over_QQ` | `orbit_dimension_gate.py:141` | dim `f_4` = 52 confirmation |
| `_select_independent_basis` (rref pivots) | `orbit_dimension_gate.py:405` | a 52-element exact `f_4` basis |
| `stab_E6_E11` (nullspace **PATTERN**) | `bulk_geometry_verification.py:1815` | adapted to `f_4` (NOT `e_6`) for `stab_f4` |
| `proj_u_exact` (`C_u` projection) | `embedding_under_E_verification.py:192` | reference for the `C_u`/`{1,2,3,10}` reduction |

**Source guard** (`kkt_gluing_holonomy.py:source_guard`, mirroring
`cartan_phaseB_curvature.py:120-141`): asserts `octonion_algebra` NOT in
`sys.modules`; `det_3/jordan/Tr` native from `ring_lemma_verification`
(`det_3(diag(2,3,5)) == 30` exact, not float); `numpy` NOT imported on the decisive
path. **All three PASS.**

**`f_4`, not `E_6`.** Identifications are `F_4` automorphisms ("`g ∈ F_4` with
`g·E_11 = E_22`"), so the Lie algebra is `f_4 = span(inner_derivations())`, dim 52.
`stab_E6_E11` is used only as the *nullspace pattern*; it is fed the `f_4` basis,
never `build_e6_basis()`.

---

## 3. Gate-0 results (exact over Q)

### Task 1a — the exact conjugating automorphism P

`P` = conjugation by the `3×3` **real** permutation matrix swapping matrix indices
`0 ↔ 1` (fixing `2`): `(P X)[i][j] = X[σ(i)][σ(j)]` with `σ = (0 1)`. A real
orthogonal conjugation preserves Hermiticity and the Jordan product
(`X∘Y ↦ S^{-1}(X∘Y)S`), hence is an exact element of `F_4 = Aut(h_3(O))`.

This **replaces Phase 52's numeric `P` (max err `1.9e-15`) with an exact-over-Q
element.** Certified (all PASS):

- `P·E_11 = E_22`, `P·E_22 = E_11` (involutive on the pair), `P·E_33 = E_33`.
- `P` preserves the **Jordan product** on all `27×27` standard-basis pairs (the
  genuine automorphism test — product, not just the norm).
- `P` preserves `det_3`, `Tr`, `Tr2` on a **generic symbolic** `X` (`F_4`-invariance).
- `P` is an exact **signed permutation** (entries `{0,±1}`), `P² = I_27`, `det P = 1`.

**Explicit `P`** (coord → sign·image; the diagonal swap `α↔β`, `γ` fixed; the
off-diagonal `x1 ↔ conj(x2)`, `x3 ↔ conj(x3)` — the conjugation flips every
imaginary component's sign, `+` on the real `.0` components):

```
 α      -> +β        x1.0 -> +x2.0      x2.0 -> +x1.0      x3.0 -> +x3.0
 β      -> +α        x1.k -> -x2.k      x2.k -> -x1.k      x3.k -> -x3.k   (k=1..7)
 γ      -> +γ
```

(So `P` swaps the diagonal slots `E_11 ↔ E_22`, fixes `E_33`, and acts on the
off-diagonal octonion slots as `x1 ↔ x̄2`, `x3 ↔ x̄3`.) This is exactly the
signed/conjugated index-permutation the spec anticipated ("the array `(1,0,2)` swaps
diagonal slots `0↔1`, fixes slot `2`; … may require an octonion conjugation on some
entries").

### `f_4` basis

`inner_derivations()` returns **324** nonzero brackets; span rank over QQ = **52**
(`= dim f_4`, COMPUTED not assumed); a 52-generator basis is selected by the rref
pivot set (exact over Q).

### Task 1b — Stab_{f_4}(E_11)

`stab_{f_4}(E_11) = {D ∈ f_4 : D·E_11 = 0}`, the nullspace of the
`27 × 52` matrix `M_{·j} = (basis_j · flat27(E_11))`:

> **dim Stab_{F_4}(E_11) = 36 = dim spin(9)** (image dim 16, `52 − 16 = 36`).

This matches the classical `Stab(E) ≅ Spin(9)`. The identification coset is then
`{g ∈ F_4 : g·E_11 = E_22} = P · Stab_{F_4}(E_11)` — the `P`-translate of the
36-dim stabilizer (a 36-dim coset).

### Task 2a — the residual r_12 (joint frame stabilizer)

`r_12 = {D ∈ f_4 : D·E_11 = 0 AND D·E_22 = 0}`, the nullspace of the **stacked**
`54 × 52` matrix (two 27-row blocks for `E_11` and `E_22`):

> **dim r_12 = 28 = dim spin(8)** (the triality group; image dim 24, `52 − 24 = 28`).

Cross-check (PASS): every `D ∈ r_12` also annihilates `E_33 = I − E_11 − E_22`
(fixes the whole standard frame). `r_12 ≅ so(8)` is the expected triality
stabilizer of the frame inside `F_4` (`Spin(9) ⊃ Spin(8)`).

### Task 2b — the SLICE ACTION of r_12 on h_2(C_u)(E_11)

`r_12` acts on `V_0(E_11) = h_2(O)` (10-dim) **faithfully and without leak**: the
28 generators have a rank-28 action on `V_0`, and **never** map a `V_0` basis
vector outside `V_0` (no cone-normal component) — `V_0` is an invariant subspace
of the frame stabilizer, as required.

The **slice action** is the induced map on the 4d `h_2(C_u)` slice
(coords `{1,2,3,10}`). Reading off the `{1,2,3,10} → {1,2,3,10}` sub-block of each
generator and spanning the resulting `4×4` matrices over Q:

> **slice-action residual = dim 1 = so(2) ≅ u(1)** (the load-bearing Gate-0 number).

Refinements (all exact over Q, all reported by the driver):

- **slice-preserving subalgebra of r_12: dim 16** — the generators that keep the
  slice clean (no leak into the internal W-sector `{4..9}`). Of the 28 `r_12`
  generators, **12 mix** the slice `{1,2,3,10}` with the internal `{4..9}` (they
  rotate the full octonion `x1` across the `C_u`/W boundary); the other 16 act
  cleanly on the slice.
- **slice-image of the preserving subalgebra: dim 1** (same number — the 12 mixers
  contribute nothing extra to the clean slice block).
- **every nonzero slice block is `so(3,1)`-valued** (an infinitesimal Lorentz
  transformation: antisymmetric under `η = diag(+1,−1,−1,−1)`).
- the surviving generator is the **`SO(2)` rotation in the `{p,q}` plane**
  (`p = Re x1`, `q = ⟨x1,e_7⟩`), i.e. the **phase rotation of the complex line
  `C_u = span{1,e_7}`**. Its Minkowski `4×4` block (rows/cols `x0,p,q,x3`) is the
  antisymmetric `{p,q}` generator; its square is `−1` on the `{p,q}` 2-plane and `0`
  elsewhere — a genuine compact rotation generator (`J² = −1`).

**Three independent routes** confirm `slice_dim = 1`: (A) the driver's slice→slice
sub-block span; (B) the `so(3,1)`-projection (antisymmetrize each block under `η`)
spanned; (C) the full `gl(4)` slice image with no Lorentz filter — all give **1**.

---

## 4. Modeling choices flagged (for the independent verifier)

The verifier must be able to re-derive every number from Peirce structure alone.
The following modeling choices were made explicitly:

1. **`P` is the orthogonal-conjugation realization of `(1,0,2)`.** Among the `F_4`
   elements with `P·E_11 = E_22`, the canonical involutive representative is
   conjugation by the real `3×3` swap matrix. This is a *choice of coset
   representative* (any other differs by right-multiplication by `Stab(E_11)`); it
   is the natural exact-over-Q analogue of Phase 52's numeric `P`. The Gate-0
   verdict does **not** depend on this choice (the residual is computed from the
   joint stabilizer, independent of the representative).

2. **"Slice action" = the induced `{1,2,3,10} → {1,2,3,10}` sub-block** (the
   quotient/induced action on the 4d slice). Equivalently, restricting first to the
   slice-preserving subalgebra (dim 16) and reading its action gives the **same**
   dim-1 image. Both readings — (i) "the subalgebra of `r_12` that preserves the
   `C_u` slice and acts on it" and (ii) "the image in the slice's structure group" —
   are reported and **agree at dim 1**. This is the only place with modeling
   content; it is pinned by the explicit constraint system in
   `slice_residual` / the slice-preserving-subalgebra nullspace (re-derivable from
   the Peirce coordinate layout `{1,2,3,10}` + `{4..9}` alone).

3. **The internal complement acts trivially on the slice (EXPECTED, per Phase 48).**
   27 of the 28 `r_12` generators act trivially on the 4d slice; this is the
   `so(6)`/triality complement (the internal `V_0 ⊖ C_u` sector). This is the
   pre-registered "Stab(u) ∩ Spin(9) = so(3) ⊕ so(6)" structure showing up: the
   `so(6)` part is inert on the slice; the slice-acting residual is the compact
   `so(2)` ⊂ the `so(3)` rotation block (see §5).

4. **Minkowski Gram convention.** `η = diag(+1,−1,−1,−1)` in the Minkowski basis
   `(x0, p, q, x3)` via the explicit change-of-basis `B` from engine coords
   `{1,2,3,10}` (`minkowski_form`). The `so(3,1)`-valued test antisymmetrizes under
   this `η`. No physical constant enters; this is purely the `det_2` quadratic form.

---

## 5. Interpretation vs the pre-registered wrinkle (NOT a kill)

The spec's "Expected wrinkle" anticipated a **compact** residual, illustrated by
"e.g. containing the `so(3)` rotation block," and bound the writeup to **not
misreport compactness as a kill**. The computed residual is the compact
**`so(2) ≅ u(1)`** (dim 1), a *sub*algebra of the illustrative `so(3)`. The reason
the full `so(3)` does **not** survive is structural and exact:

- the slice's spatial triple is `{p, q, x3}` with `x3 = (β−γ)/2` built from the
  **diagonal** `(β, γ)`;
- `r_12` **fixes the diagonal idempotents** `E_11, E_22`, so it cannot rotate `x3`
  against `{p, q}`;
- the only spatial rotation it can perform is the `{p, q}` rotation **internal to
  `C_u`** — i.e. the phase of the complex line `e_7`. Hence `so(2)`, not `so(3)`.

This is fully **consistent with the dictionary picture** (compact algebraic freedom;
the boost freedom lives on the metric side and was never inside `Spin(9)` — Phase
48). The residual is non-trivial, so the identification is **not** unique from bare
algebra.

---

## 6. Verdict / routing (deterministic, non-hardwired ladder)

The `verdict()` ladder derives its branch from the **computed** `slice_dim` (not a
literal) and ships self-tests proving each branch fires on synthetic inputs (all
self-tests PASS):

- `slice_dim == 0` → `GATE0-UNIQUE` (unique from bare algebra → skip Gate 1, go to
  Gate 2). **Not** taken.
- `slice_dim > 0` → `RESIDUAL-SURVIVES` (record the 2-point freedom → Gate 1).
  **Taken** (`slice_dim = 1`).
- `n_leak != 0` → `BUILD-ERROR` (slice not invariant; STOP). **Not** taken
  (`n_leak = 0`).

> **VERDICT: `RESIDUAL-SURVIVES`.** The 2-point identification retains a residual
> `so(2) ≅ u(1)` slice freedom (the `C_u` phase rotation). Per the pre-registered
> wrinkle this **compact** residual is **NOT** a kill. **Routing: record the dim-1
> residual and proceed to Gate 1** (the canonicalization sweep — does `u`-alignment /
> `det_2`-isometry / Peirce-block / interface-intertwining cut this `so(2)` to
> triviality?).

**Anti-overclaim (binding):** this is the structure-only identification space. It
proves only that, after fixing both endpoint idempotents, an `so(2)` slice freedom
remains; it does **not** prove independence (that is Gate 2's three-point holonomy),
does **not** produce a metric law / `G = κT` / dynamics, and does **not** touch the
v17–v21 / Sakharov verdicts (the six-kind menu stays exhausted). No `κ`, no `Λ`, no
physical constants entered.

---

## 7. Deviation from the brief (flagged)

The brief pre-registered the residual as "e.g. so(3)" (dim 3) as the illustrative
compact group. The exact computation gives **so(2) = u(1) (dim 1)** instead, for the
structural reason in §5 (`r_12` fixes the diagonal `⟹` cannot rotate `x3`; only the
intra-`C_u` `{p,q}` phase survives). This is a **smaller compact residual**, still
fully consistent with the pre-registered wrinkle (compact, not a kill) and the same
routing verdict (`RESIDUAL-SURVIVES → Gate 1`). It is reported here, not silently
adopted; the load-bearing Gate-0 number is **dim 1**, verified three independent
ways. No deviation in scope, conventions, or the gate boundary (Gates 1/2/3 not run).

---

# GATE 1 — the canonicalization sweep (does anything force uniqueness?)

**Scope of this section:** Gate 1 only (the four program-native compatibility
conditions imposed on the identification `g`, recomputing the surviving slice
residual at each step). **Gate 2 is NOT run** — the orchestrator routes next.
Same guards: source guard (PASS), no `octonion_algebra.py`, no `numpy` on the
decisive path, exact over Q, no `κ`/`Λ`/physical constants.
Driver: `PYTHONPATH=code python3 -u code/kkt_gluing_holonomy.py gate1` → exit 0, ALL_PASS.

## G1.0 Setup — the residual carrier and the Peirce structure

The Gate-0 residual is the slice action of `r_12 = {D ∈ f_4 : D·E_11 = 0, D·E_22 = 0}`
= `so(8)` (dim 28), whose slice action on `h_2(C_u)(E_11)` is `so(2) ≅ u(1)` (dim 1,
the `C_u = span{1,e_7}` phase rotation in the `{p,q}` plane). Each Gate-1 condition
carves a **subalgebra** `R^(i) ⊆ R^(i-1)`; because every condition is **linear** in
`D`, the surviving residual is the span of the `r_12` generators passing the test,
and its slice residual is recomputed by `slice_residual`.

**Peirce structure under the standard frame** (exact eigenspaces of `L_E`):

| | `V_1` (eig 1) | `V_{1/2}` (eig 1/2) | `V_0` (eig 0) |
|---|---|---|---|
| `E_11` | `{0}` = `α` | `{11..26}` = `x2 ⊕ x3` | `{1..10}` = `β,γ,x1` |
| `E_22` | `{1}` = `β` | `{3..10, 19..26}` = `x1 ⊕ x3` | `{0,2,11..18}` |

- **Spacetime slice `{1,2,3,10}` ⊂ V_0(E_11)** (confirmed).
- **SHARED V_{1/2} channel** `= V_{1/2}(E_11) ∩ V_{1/2}(E_22) = {19..26}` = the **`x3`
  octonion slot** (the `(1,0)`/`(0,1)` block that *connects* `E_11` and `E_22`). This
  is the "shared channel each observer assigns sequential-product data to" in
  condition 4.

## G1.1 The four conditions (prompt verbatim) and their exact status

### Condition 1 — u-alignment — **AUTOMATIC** (kept 28/28, slice_dim 1)

`g` maps `u = e_7` of `E_11`'s slice to `u'` of `E_22`'s slice (`g` intertwines
`π_u, π_u'`). At the residual level: `D`'s slice action must **commute with the `C_u`
complex structure `J`** (mult-by-`e_7` on `C_u`, i.e. the `{p,q}` rotation
`p ↦ q, q ↦ −p`). Test: `[D_slice, J_slice] = 0`.

**Result: AUTOMATIC.** All 28 `r_12` generators pass; slice residual stays **1**. The
structural reason (verified exactly): the surviving `so(2)` generator acts as
`e_3 ↦ −e_10`, `e_10 ↦ +e_3` and **touches nothing else** in `V_0` (`β,γ` fixed,
internal-W `{4..9}` untouched) — it **is** the `C_u` phase, a power of `J`, so it
trivially commutes with `J`. (Exactly the prompt's anticipated relation: "the so(2)
IS the `C_u` phase, which commutes with mult-by-`e_7`, so naively `u`-related
conditions may not cut it.")

### Condition 2 — det_2 isometry — **AUTOMATIC** (verified, not assumed)

The slice action preserves the `det_2` Minkowski form. Test: the 4×4 slice block is
`so(3,1)`-valued (`η·A + Aᵀ·η = 0` in Minkowski coords, `η = diag(+1,−1,−1,−1)`).

**Result: AUTOMATIC** (verified per the prompt's "should be automatic from `F_4 ⊂
Aut`; verify, don't assume"). The single nonzero slice block (the `so(2)` rotation)
is `so(3,1)`-valued; slice residual stays **1**.

### Condition 3 — Peirce-block preservation — **AUTOMATIC** (verified)

`g` maps `V_{1/2}(E_11) → V_{1/2}(E_22)` and `V_1 → V_1`. At the residual level:
`D` preserves each Peirce space of `E_11` (`V_1 → V_1`, `V_{1/2} → V_{1/2}`,
`V_0 → V_0`).

**Result: AUTOMATIC** (verified per the prompt's "automatic given `g·E_11 = E_22`;
verify exactly"). All 28 `r_12` generators preserve all three Peirce spaces, because
`D·E_11 = 0 ⟹ [D, L_{E_11}] = 0 ⟹ D` preserves every eigenspace of `L_{E_11}`. Slice
residual stays **1**.

### Condition 4 — interface intertwining — **AUTOMATIC, but NON-VACUOUS** (the only condition with modeling content)

**The exact operator equation (derived from Peirce structure alone):**

> For all `x, y ∈ V_{1/2}(E_11)`:
> `Π_{V_0(E_11)}( (Dx)∘y + x∘(Dy) ) = D( Π_{V_0(E_11)}( x∘y ) )`

i.e. **`D` is an infinitesimal derivation of the Peirce quadratic map**
`Q_11(x,y) = Π_{V_0(E_11)}(x∘y) : V_{1/2}(E_11) × V_{1/2}(E_11) → V_0(E_11)` — the
canonical "sequential-product data each observer assigns to the `V_{1/2}` channel."
The Peirce-0 projector `Π_{V_0(E_11)}` is the exact spectral projector onto the
eigenvalue-0 space of `L_{E_11}` (`peirce_proj`, Lagrange interpolation over Q).

The **cross-frame** form (the full "computed in `E_11`'s frame, pushed through `g`,
equal those in `E_22`'s frame") is
`g(Q_11(x,y)) = Q_22(g(x), g(y))` with `g = P·exp(tD)`. This **splits**:
- the `P`-part: `P` intertwines `Q_11 ↔ Q_22` **exactly** (since `P ∈ Aut(h_3(O))`;
  verified on all 16×16 `V_{1/2}(E_11)` basis pairs over Q);
- the residual-`D` part: the boxed derivation equation above.

**Flagged modeling choices** (the verifier must re-derive from Peirce structure
alone):
1. **`Q = Π_{V_0}(x∘y)`** (the Peirce-0 component of the Jordan product) is taken as
   *the* "sequential-product data." This is the canonical Peirce quadratic map
   `V_{1/2} × V_{1/2} → V_0` (McCrimmon; the Peirce multiplication rules) — **not** a
   hand-picked form. The `V_1`-component `Π_{V_1}(x∘y)` is the complementary
   "norm/length" datum; the `V_0`-component is the genuinely *inter-frame* channel
   (it lands in the shared slice arena), which is why it is the faithfulness-relevant
   one.
2. **Default channel = full `V_{1/2}(E_11) = {11..26}`** (the strongest form). Testing
   only the shared sub-channel `{19..26}` gives the **same** result (any `f_4`
   derivation preserves every Peirce product).
3. **Infinitesimal (Lie-algebra) reading** of "intertwines" — consistent with the
   whole Gate-0/Gate-1 residual-as-subalgebra treatment.

**NON-VACUITY (the condition has teeth — demonstrated, not asserted):**
- `P` (a genuine automorphism) **passes** the cross-frame `Q_11 ↔ Q_22` intertwining
  exactly.
- a **non-derivation** map (`P` plus a spurious `x2(idx11) → x3(idx19)`
  cross-channel `V_{1/2}` coupling) **FAILS** the intertwining.

So the equation is a real constraint that *could* have obstructed.

**Result: AUTOMATIC for the residual.** All 28 `r_12` generators satisfy it (tested
exactly on all 256 `V_{1/2}(E_11)` basis pairs). The **honest reason** the `so(2)`
survives: `r_12 ⊂ Der(h_3(O))` (every element is a global Jordan derivation, so
`D(x∘y) = Dx∘y + x∘Dy` identically), and every `D ∈ r_12` fixes `E_11` (so commutes
with `Π_{V_0(E_11)}`). Hence both sides of the boxed equation are identically
`Π_{V_0(E_11)}(D(x∘y))`. This is **not** a vacuous test (it rejects non-derivations);
it is auto-satisfied *specifically because the residual lives in the frame-fixing
derivation algebra* — which is exactly the program-native statement that the
algebraic freedom respects all Peirce-product data.

## G1.2 The residual chain (exact over Q)

| Step | Condition added | kept gens | slice residual | iso type |
|---|---|---|---|---|
| `R_12` | (start) | 28/28 | **dim 1** | `so(2) ≅ u(1)` |
| `R^(1)` | + u-alignment | 28/28 | **dim 1** | `so(2)` |
| `R^(2)` | + det_2 isometry | 28/28 | **dim 1** | `so(2)` |
| `R^(3)` | + Peirce-block | 28/28 | **dim 1** | `so(2)` |
| `R^(4)` | + interface intertwining | 28/28 | **dim 1** | `so(2)` |

> **Chain: `R_12 ⊇ R^(1) ⊇ R^(2) ⊇ R^(3) ⊇ R^(4)` = `1 ⊇ 1 ⊇ 1 ⊇ 1 ⊇ 1`.**
> Every condition is **AUTOMATIC**; **none** cuts the residual. The cumulative
> residual after all four is `so(2) ≅ u(1)` (dim 1) — the `C_u` phase.

**Independent cross-check (different code path):** building `D(t) = Σ_k t_k·gens_k`
symbolically and imposing conditions 1–2 as **linear equations on the 4×4 slice
block** gives a constraint matrix of **rank 0** (no rows — the `so(2)` block already
commutes with `J` and is already `so(3,1)`-valued); conditions 3–4 add **no rows**
(every generator already passes them). The joint-linear-nullspace surviving slice
residual is **dim 1**, confirming the generator-filtering result.

## G1.3 Verdict / routing (deterministic, non-hardwired ladder)

`gate1_verdict()` derives its branch from the **computed** final cumulative
`slice_dim` (not a literal), with self-tests proving each branch fires (all PASS):

- `final_slice_dim == 0` → `CANONICAL` (a condition forced uniqueness → Gate 2 with
  the canonical `g`'s). **Not** taken.
- `final_slice_dim > 0` → `RESIDUAL-SURVIVES` (freedom survives all four → the 2-point
  independence result → Gate 2 sweeping the residual classes). **Taken**
  (`final_slice_dim = 1`).

> **GATE-1 VERDICT: `RESIDUAL-SURVIVES`.** No program-native compatibility condition
> (u-alignment, det_2 isometry, Peirce-block preservation, interface intertwining)
> cuts the `so(2) ≅ u(1)` `C_u`-phase residual to triviality. This **is** the
> two-point independence result at the canonicalization level: the identification
> `E_11 → E_22` is **NOT canonically unique** — a residual `U(1)` slice freedom
> persists after every faithfulness-proxy condition. **Routing: record the surviving
> `so(2)`; proceed to Gate 2** (three-point holonomy — does the loop
> `g_31 ∘ g_23 ∘ g_12` force the identity, sweep a set, or force a nontrivial `h`?).

**Anti-overclaim (binding):** this proves only that the four conditions do not force
a canonical flat identification at the **two-point** level; it does **NOT** prove
independence around the loop (Gate 2), does **NOT** produce a metric law / `G = κT` /
dynamics, does **NOT** establish the No-Absolute-Objects "bridge" clamp (that remains
an argued, separately-attacked claim — `substrate-dictionary-gravity.md` §9.2), and
does **NOT** touch the exhausted v17–v21 / Sakharov six-kind menu. No `κ`, `Λ`, or
physical constant entered. The compactness of the `so(2)` residual is the
pre-registered Phase-48 fact (boosts are metric-side, never inside `Spin(9)`), not
evidence either way about boosts.

## G1.4 Honest condition tally (per the prompt's request)

| Condition | Status | Cuts the so(2)? | Notes |
|---|---|---|---|
| 1. u-alignment | **AUTOMATIC** | No | the residual IS the `C_u` phase ⟹ commutes with `J` |
| 2. det_2 isometry | **AUTOMATIC** | No | slice block is `so(3,1)`-valued (`F_4 ⊂ Aut`); verified |
| 3. Peirce-block preservation | **AUTOMATIC** | No | `D·E_11 = 0 ⟹` preserves all Peirce spaces; verified |
| 4. interface intertwining | **AUTOMATIC** (non-vacuous) | No | `r_12 ⊂ Der` preserves all Peirce products; teeth demonstrated |

All four automatic; the `so(2)` survives every one. The exact operator equation for
condition 4 is in §G1.1; its non-vacuity (teeth) is demonstrated there.

## G2 — Gate 2: three-point holonomy (THE DECISIVE GATE)

Driver: `PYTHONPATH=code python3 -u code/kkt_gluing_holonomy.py gate2` → **exit 0,
ALL_PASS**. Independent verification: `derivations/82-GATE-2-VERIFICATION.md` (built
from scratch through a DIFFERENT code path — own octonion algebra from the Fano table,
own `f_4`, own nullspaces; **HIGH**, none of the load-bearing checks failed).

Standard frame `E_11, E_22, E_33`; pairwise identifications `g_12, g_23, g_31`; loop
`h = g_31 ∘ g_23 ∘ g_12 ∈ Stab(E_11)`; read its 4d slice action on `h_2(C_u)(E_11)`.

### G2.1 The FIRED bug-guard: the bare transpositions are INADMISSIBLE (the predicted spurious LIVE-B)

The prompt pre-registered LIVE-B as "the most likely executor bug … verify the
identifications were not mis-normalized." A first pass used the bare frame
**transpositions** `τ_ij` (swap `i↔j`) as base identifications and returned **LIVE-B**
(base loop `diag(1,1,−1,−1)`, a spatial π-rotation; the three residual phases co-axial,
unable to cancel it). That pass was **wrong** for a structural reason:

- `τ_01` carries an octonion **conjugation**: it maps `u = e_7 → −e_7` (verified exact:
  `e_7` in the `x1` slot → `−e_7` in the `x2` slot). So `τ` **fails Gate-1 condition 1
  (u-alignment)** and is **NOT an admissible identification**.
- Equivalently `τ_01`'s slice map **anti-intertwines** the `C_u` complex structure
  `J`: `L_τ · J = − J · L_τ` (antiholomorphic), whereas an admissible (u-aligned) map
  must satisfy `L · J = + J · L`.

Because the slice `h_2(C_u)` is **defined** by `u` via `π_u` (Phase 46), u-alignment is
the correct admissibility condition; the transpositions are discarded. **Monotonicity:**
even admitting them would only *enlarge* the holonomy set (the u-aligned loop remains
admissible), so it could never *restore* DEAD. The bug-guard fires; we proceed with the
admissible identifications.

### G2.2 The admissible base: the u-aligned 3-cycle ρ (flat)

`ρ = conj(·, σ)` with `σ = (0→2, 1→0, 2→1)` — the **u-aligned** 3-cycle automorphism
`E_11 → E_22 → E_33 → E_11`. Verified exact over Q: `ρ` is a genuine automorphism, cycles
the frame, **preserves `u = e_7`** (`e_7 → +e_7`; holomorphic, `L_ρ · J = + J · L_ρ`), and
has **order 3** (`ρ³ = I_27`). Its slice maps `L_ρ` carry each leg with no leak and
preserve `det_2`. Taking `g_12 = g_23 = g_31 = ρ`, the **base loop is FLAT**:
`h_slice(ρ³) = I` — the canonical u-aligned gluing has trivial holonomy.

### G2.3 The structural reduction (the load-bearing argument)

> Every residual element fixes **both** endpoint idempotents **and** is an automorphism,
> so it automatically intertwines **all** purely-algebraic data — Gate-1 conditions 1–4
> can **never** eliminate it. Therefore **LIVE-vs-DEAD reduces to one question: does the
> joint endpoint stabilizer act NONTRIVIALLY on the `h_2(C_u)` slice?**

Computed exact over Q: `r_12 = {D ∈ f_4 : D·E_11 = 0 ∧ D·E_22 = 0} = so(8)` (dim 28); its
slice action on `h_2(C_u)(E_11)` is a **genuine nontrivial compact `SO(2)`** (dim 1, the
`C_u` phase `⟨J_rot⟩`). So the reduction answers **nontrivial ⟹ LIVE**.

### G2.4 The decisive computation: h(φ) flat at φ=0, nontrivial otherwise → LIVE-A

With the u-aligned `ρ` base and the residual `C_u` phases `A_i(φ_i)` turned on,
`h(φ) = L_ρ·A_3·L_ρ·A_2·L_ρ·A_1` (4×4, exact over Q, symbolic `(c_i, s_i)`, `c²+s²=1`):

- `h(φ)` genuinely **VARIES** with the phases;
- `h(0) = I` — the pure `ρ`-loop is **FLAT** ⟹ **identity REACHABLE**;
- a single residual phase gives `h ≠ I` ⟹ **nontrivial REACHABLE**;
- `h(φ) ∈ SO(3,1)` (`det_2`-isometry) for **all** `φ`.

> **GATE-2 VERDICT: `LIVE-A` — INDEPENDENCE PROVED.** With admissible (u-aligned)
> identifications the three-point gluing holonomy is an **UNFORCED** choice: flat at the
> canonical `ρ`-base and nontrivial under the residual `C_u` phase. The algebra does
> **NOT** force a canonical flat identification between distinct observers' KKT slices.

### G2.5 The reachable holonomy group (so(3) add-on, non-blocking)

The admissible `ρ`-loop with the joint-stabilizer residual reaches only a **single
`SO(2)`** (the `C_u` plane; the three conjugated phase-generators span rank 1, all
co-axial), **NOT** full `SO(3)`. The freedom is exactly **one internal `u`-phase** = a
spatial `SO(2) ≅ U(1)`.

### G2.6 Anti-overclaim (binding)

This proves **INDEPENDENCE ONLY.** The freedom found is one internal `u`-phase acting as
a spatial `SO(2)/U(1)` — **gauge-flavored** (Berry / MacDowell–Mansouri-shaped, U(1)-shaped,
**NOT metric-shaped**). It is **NOT** "the dictionary's degrees of freedom": a tetrad
needs frame-gluing (boost) freedom, and boosts are never algebra-internal (Phase 48); the
**bridge clamp** (No-Absolute-Objects) is untouched — an argued, separately-attacked claim
(`substrate-dictionary-gravity.md` §9.2). The result produces **no** metric law, `G = κT`,
or dynamics, and does **NOT** reopen the exhausted v17–v21 / Sakharov six-kind menu; the
v12/v13 Einstein result is untouched. No `κ`, `Λ`, or physical constant entered anywhere.

---

## Milestone verdict (one paragraph, v21 format)

**v22.0 (KKT-Slice Gluing Freedom & Three-Point Holonomy) — VERDICT: LIVE-A, INDEPENDENCE
PROVED.** Running the fail-fast gates cheapest-first (executor + independent verifier,
different code paths, exact over Q): **Gate 0** computed the identification space — the
residual after fixing endpoints is the joint frame stabilizer `so(8)` whose slice action on
`h_2(C_u)` is a nontrivial compact `SO(2)` (the `C_u = span{1,e_7}` phase); the exact
conjugating automorphism `P` replaced Phase 52's numeric one. **Gate 1** swept the four
program-native compatibility conditions (u-alignment, det_2 isometry, Peirce-block,
interface intertwining) and found **all four automatic** — none cuts the `SO(2)` (a
structural consequence: the residual is a frame-fixing automorphism, so it intertwines all
algebraic data). **Gate 2** computed the three-point loop holonomy: a first pass on the
**inadmissible** u-flipping transpositions returned the pre-registered spurious **LIVE-B**;
corrected to the **admissible** u-aligned 3-cycle `ρ` (`ρ³ = I`, flat base), the holonomy is
flat at `φ = 0` and nontrivial under the residual `C_u` phase ⟹ **LIVE-A**. **What it
establishes:** the axioms do **not** force a canonical flat gluing between observers' local
KKT slices — the independence half of the implementation-dictionary route, in exact
arithmetic. **What it leaves open:** the freedom is a single gauge-flavored `U(1)` (the `C_u`
phase, `SO(2)` not full `SO(3)`, U(1)-shaped not metric-shaped), so it is **not** a
tetrad/frame-gluing field; and the **No-Absolute-Objects "bridge"** — that the model's law
may contain only forced/certified structure — remains an **argued** clamp (attacked
separately in-repo), not proved here. **No promotion past independence:** no metric law, no
`G = κT`, no dynamics; the v17–v21 six-kind metric-selection menu stays exhausted; the
v12/v13 Einstein result is untouched. All decisive arithmetic exact over Q; Gate 0/1
verifier-hardened HIGH; Gate 2 independently verified HIGH (the spurious LIVE-B caught and
LIVE-A confirmed through a from-scratch code path). Deliverables:
`code/kkt_gluing_holonomy.py`, `derivations/82-kkt-gluing-RESEARCH.md`,
`derivations/82-GATE-{0,1,2}-SUMMARY.md`, `derivations/82-GATE-{0,1,2}-VERIFICATION.md`.
