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
