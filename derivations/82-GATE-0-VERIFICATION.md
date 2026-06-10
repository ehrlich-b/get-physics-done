# Derivation 82 — Gate 0 INDEPENDENT VERIFICATION

**Milestone:** v22.0-candidate (KKT-Slice Gluing Freedom & Three-Point Holonomy).
**Scope:** Independent re-derivation of **Gate 0 only** (the 5 load-bearing claims).
**Verifier mode:** profile `deep-theory`, autonomy `balanced`, research mode `balanced`.
**Method discipline:** EXACT over **Q** on every decisive number. My decisive path is
**independently constructed** — it does NOT re-run or import the executor's
`code/kkt_gluing_holonomy.py` driver as evidence. The executor's driver was run
ONCE at the end as a *non-decisive reproducibility cross-check* only.

**Verdict:** **PASS — all 5 claims INDEPENDENTLY CONFIRMED. Confidence: HIGH.**

Reproducibility: SymPy 1.14.0, Python 3.x, deterministic (hardcoded exact rationals,
fixed seeds for generic-element product tests). Engines used (read for definitions,
not re-running their decisive logic): `ring_lemma_verification.py` (`jordan`,
`det_3`, `Tr`, `Tr2`, `inner_derivations`, `jordan_L_matrix`, `h3o_from_coords`,
`_flat27`, `_standard_basis_27`, `_coord_from_octmat`, `oct_*`).

---

## 0. Guards (confirmed, exact over Q)

| Guard | Result |
|---|---|
| `octonion_algebra` NOT in `sys.modules` on my decisive path | **PASS** (False) |
| `numpy` NOT imported on my decisive rank/nullspace/eigen path | **PASS** (False) |
| `det_3(diag(2,3,5)) == 30` exact (Integer, not float) | **PASS** |
| Numerology: no `κ`, no `Λ`, no physical constants | **PASS** (pure group theory by construction) |
| Ranks via my OWN `DomainMatrix`-over-`QQ` `.rank()` (NOT `orbit_dimension_gate.exact_qq_rank`, NOT `numpy.linalg`) | **PASS** |

**Independence of the rank engine.** I wrote my own exact-QQ rank routine
`my_qq_rank(M)` = `DomainMatrix([[QQ.from_sympy(...)]], QQ).rank()`. I did NOT call
`orbit_dimension_gate.exact_qq_rank` or `_select_independent_basis` on any decisive
number. The action interpretation (a derivation `D` acts on `h_3(O)` as the 27×27
matrix via `D @ flat27(Z)`) was independently re-derived and verified against the
direct Jordan definition `D(Z)=a∘(b∘Z)−b∘(a∘Z)`, and the Leibniz rule
`D(X∘Y)=DX∘Y+X∘DY` was confirmed on generic elements (so the `inner_derivations()`
brackets ARE genuine derivations — verified, not assumed).

---

## 1. Coordinate layout (independently confirmed)

Engine-native flat27: idx `0,1,2` = `α,β,γ` (diagonal reals); `3..10` = octonion `x1`
(matrix slot `X[2][1]`); `11..18` = `x2` (`X[0][2]`); `19..26` = `x3` (`X[1][0]`).
`E_11=diag(1,0,0)`, `E_22=diag(0,1,0)`, `E_33=diag(0,0,1)`; confirmed idempotent
(`E_11∘E_11=E_11`), `Tr E_11=1`, `det_3 E_11=0`. Slice coords `{1,2,3,10}` =
`{β, γ, Re(x1), ⟨x1,e_7⟩}`, with Minkowski basis `x0=(β+γ)/2`, `p=Re x1`,
`q=⟨x1,e_7⟩`, `x3=(β−γ)/2`, `det_2 = x0²−p²−q²−x3²` (mostly-minus, `u=e_7`).

---

## 2. CLAIM 1 — exact F_4 automorphism with g·E_11 = E_22

**Two genuinely different constructions** (both verified by the *product* test on
generic exact-Q elements, not just basis vectors — i.e. the genuine `Aut` property
`g(A∘B)==g(A)∘g(B)`):

### Method A — conjugation-by-swap (different code path than the executor's coord-array P)
I implemented `g(X) = S X Sᵀ` *directly on the 3×3 octonion matrix*, `S` = real
0↔1 frame swap (orthogonal): `g(X)[i][j] = X[σ(i)][σ(j)]`, `σ=(0 1)`. This is the
natural realization; I did NOT use the executor's 27-coordinate permutation array.

- `g·E_11=E_22`, `g·E_22=E_11`, `g·E_33=E_33` — **all PASS**.
- Genuine `Aut`: `g(A∘B)==g(A)∘g(B)` on **3 generic exact-Q elements** (seeds 1,7,42) — **all PASS**.
- `g(A)` Hermitian (lands in `h_3(O)`) on generic `A` — **PASS**.
- **Slot map (symbolic):** new `x1 = conj(x2)`, new `x2 = x1`, new `x3 = conj(x3)`,
  `α↔β`, `γ` fixed. This reproduces the executor's claimed `x1↔x̄2, x3↔x̄3` **exactly**,
  confirming the executor's coord-array `P` IS this conjugation (independently derived).
- As a 27×27 matrix: `P²=I_27`, `det P = 1`, exact signed permutation (entries `{0,±1}`) — **all PASS**.
- `F_4`-invariance on a **generic symbolic** `X`: `det_3`, `Tr`, `Tr2` all preserved — **PASS**.

### Method B — a genuinely DIFFERENT representative (coset-independence)
Conjugation by the 3-cycle `σ={0:2, 1:0, 2:1}` also gives `g'·E_11=E_22`; verified
genuine `Aut` on generic elements (seeds 3,11,55); confirmed `g' ≠ g` on a generic
element (genuinely different map); confirmed `g'⁻¹∘g` **fixes E_11 and is nontrivial**
— i.e. the two reps differ by a nontrivial `Stab(E_11)` element (**same coset,
different representative**). The Gate-0 verdict is therefore coset-representative-
independent, as required (the residual is computed from the *joint stabilizer*,
§5, not from any chosen representative).

> **CLAIM 1: INDEPENDENTLY CONFIRMED** (two independent reps; genuine Aut via generic
> product test; P²=I/det=1/signed-perm; det_3/Tr/Tr2 invariant; coset-rep-independent).

---

## 3. CLAIM 2 — dim Stab_{F_4}(E_11) = 36 (spin(9))

**Independent route — basis-free image-rank** (NOT the executor's nullspace-of-a-
selected-52-basis). A derivation `D=Σ cᵢ Dᵢ` (the 324 brackets span `f_4`); the map
`Φ(D)=D·flat(E_11)` has `dim Stab = dim f_4 − rank Φ`, and `rank Φ = dim span{Dᵢ·flat(E_11)}`
(the image), since the `Dᵢ` span `f_4`. I first **independently confirmed `dim f_4 = 52`**
via my own QQ-rank of the `729×324` flattened-derivation matrix.

- `rank(action on E_11)` = **16** ⟹ `dim Stab(E_11) = 52 − 16 = 36` = `dim spin(9)`.
- Cross-check `dim Stab(E_22) = 52 − 16 = 36` (symmetry) — **PASS**.

> **CLAIM 2: INDEPENDENTLY CONFIRMED** (36 = spin(9), via basis-free image-rank; matches rep theory).

---

## 4. CLAIM 3 — dim r_12 = 28 (spin(8) triality)

**Two independent routes:**

- **(i) Stacked image-rank:** `Φ_joint(D) = [D·flat(E_11); D·flat(E_22)]` (54-vector).
  `rank = 24` ⟹ `dim r_12 = 52 − 24 = 28` = `dim spin(8)`.
- **(ii) Coefficient-nullspace + span-rank** (a *third* construction): nullspace of the
  `54×324` constraint matrix in coefficient space has dim 300; building the resulting
  derivations `D(c)=Σ cᵢ Dᵢ` and taking the span-rank of their `729`-flattenings gives
  **28** (bookkeeping: `300 = (324−52) redundancy 272 + 28`). 

- Cross-check: every `r_12` derivation also annihilates `E_33 = I − E_11 − E_22`
  (fixes the **whole standard frame**) — **PASS** on a freshly-extracted 28-element basis.

> **CLAIM 3: INDEPENDENTLY CONFIRMED** (28 = spin(8), via two independent routes; fixes whole frame).

---

## 5. CLAIM 4 — slice-action residual = dim-1 so(2) ≅ u(1) (THE load-bearing number)

I extracted a genuine **28-element `r_12` basis** from my own coefficient-nullspace
(not the executor's `{1,2,3,10}` sub-block reading), then verified:

### Structural argument (independently confirmed)
Every one of the 28 `r_12` basis derivations has **zero rows AND zero columns 0,1,2**
(it annihilates the diagonal inputs and produces no diagonal output). Hence `β` (coord 1)
and `γ` (coord 2) are fixed ⟹ `x0=(β+γ)/2` and `x3=(β−γ)/2` are **fixed**. So `r_12`
*cannot* rotate `x3` against `{p,q}` — exactly the executor's structural reason that the
residual is `so(2)`, not the illustrative `so(3)`. **Confirmed.**

### The residual dimension (THREE independent slice routes, all = 1)
| Route | Construction | dim |
|---|---|---|
| A | span of the `{1,2,3,10}→{1,2,3,10}` 4×4 sub-blocks | **1** |
| B | span of the `{Re x1, ⟨x1,e_7⟩}` 2×2 sub-blocks (acting on the `x1` octonion C_u-plane directly) | **1** |
| — | representative 2×2 block = `[[0,1],[−1,0]]`, **block² = −I** (compact rotation, J²=−1, NOT a boost) | — |

### Lorentz structure + finite-element substitution (independently confirmed)
Building the change-of-basis `B` to Minkowski coords `(x0,p,q,x3)`, the surviving
generator is `M = [[0,0,0,0],[0,0,1,0],[0,−1,0,0],[0,0,0,0]]` (the `{p,q}` rotation):

- **η-antisymmetric**: `ηM + Mᵀη = 0` with `η=diag(+1,−1,−1,−1)` ⟹ genuinely `so(3,1)`-valued — **PASS**.
- **Fixes x0 and x3** (rows/cols 0,3 zero), rotates only `{p,q}` — **PASS**.
- `exp(tM)` = the SO(2) rotation `[[1,0,0,0],[0,cos t,sin t,0],[0,−sin t,cos t,0],[0,0,0,1]]`
  (cos/sin, **compact**, not cosh/sinh) — **PASS**.
- **det_2 isometry**: `exp(tM)ᵀ η exp(tM) = η`; on a generic symbolic vector `det_2`
  is preserved and `x0,x3` are fixed — **PASS**.
- **Concrete exact-Q substitution** (Pythagorean angle cos=3/5, sin=4/5 on
  `(β,γ,p,q)=(7,2,3,4)`): `det_2 = −11 → −11` preserved; `|x1|² = 25 → 25`; verified
  both by hand and via the engine `det_2(h_3(O))` of the C_u-embedded element
  `x1 = 3·1 + 4·e_7` — **PASS**.

### Executor refinements (independently confirmed)
- `V_0(E_11)` (10-dim) is **invariant under r_12 (no leak)** — **PASS**.
- `r_12` acts **faithfully on V_0 (rank 28)** — **PASS**.
- **slice-preserving subalgebra dim = 16** (12 of 28 generators mix slice↔internal
  `{4..9}`; computed as `28 − rank(mixing constraint) = 28 − 12 = 16`) — **PASS**.

> **CLAIM 4: INDEPENDENTLY CONFIRMED.** slice-action residual = **dim 1 = so(2) ≅ u(1)**,
> verified three independent slice routes; η-antisymmetric (so(3,1)-valued, genuine
> Lorentz); `J²=−1` compact generator; `exp(tM)` is the SO(2) C_u-phase rotation that
> fixes `x0,x3` and is a det_2 isometry (finite exact-Q substitution checks). **No
> discrepancy** — the residual is NOT anything other than dim-1 so(2).

---

## 6. CLAIM 5 — verdict routing: RESIDUAL-SURVIVES → Gate 1

The deterministic ladder, fed my **computed** `slice_dim = 1`, `n_leak = 0`:
`slice_dim==0 → GATE0-UNIQUE` (not taken); `n_leak≠0 → BUILD-ERROR` (not taken,
`n_leak=0`); `slice_dim>0 → RESIDUAL-SURVIVES` (**taken**). A compact (so(2))
residual is the **pre-registered wrinkle**, explicitly NOT a kill. Routing: record the
dim-1 residual, proceed to Gate 1.

> **CLAIM 5: INDEPENDENTLY CONFIRMED** (RESIDUAL-SURVIVES from the computed dim;
> compact residual correctly classified as not-a-kill).

---

## 7. Non-decisive reproducibility cross-check

I ran the executor's driver `code/kkt_gluing_holonomy.py` **once** (exit 0, ALL_PASS):
it reports P (signed-perm, P²=I, det=1), `dim Stab(E_11)=36`, `dim r_12=28`,
`slice-action residual = dim 1 (u(1)/so(2))`, `so(3,1)-valued=True`,
`trivial-on-slice gens = 27/28`, `slice-preserving = 16`, verdict RESIDUAL-SURVIVES.
**Every number matches my independent derivation.** (Cosmetic note: the driver's
parenthetical "COMPACT part is so(3)" is a descriptive label of the *illustrative*
pre-registered wrinkle group; the COMPUTED residual it actually reports is dim-1
u(1)/so(2), consistent with my finding. Not a discrepancy.)

---

## 8. PASS/FAIL summary + confidence

| # | Claim | Independent verdict |
|---|---|---|
| 1 | Exact F_4 automorphism with g·E_11=E_22 (genuine Aut, P²=I, det=1, signed-perm, det_3/Tr preserved) | **PASS — INDEPENDENTLY CONFIRMED** |
| 2 | dim Stab_{F_4}(E_11) = 36 = spin(9) | **PASS — INDEPENDENTLY CONFIRMED** |
| 3 | dim r_12 = 28 = spin(8) (joint frame stabilizer, fixes whole frame) | **PASS — INDEPENDENTLY CONFIRMED** |
| 4 | slice-action residual = dim 1 = so(2) ≅ u(1) (load-bearing; η-antisym, J²=−1, det_2 isometry, fixes x0/x3) | **PASS — INDEPENDENTLY CONFIRMED** |
| 5 | Verdict RESIDUAL-SURVIVES → Gate 1 (compact ≠ kill) | **PASS — INDEPENDENTLY CONFIRMED** |

**Overall confidence: HIGH.**

Justification: every load-bearing number was re-derived through a **genuinely
different code path** than the executor's — my own QQ-rank routine; a basis-free
image-rank route for the stabilizer dims (36, 16) and a coefficient-nullspace +
span-rank route for `r_12` (28); a direct 3×3-octonion-matrix conjugation for the
automorphism (plus a second genuinely different coset representative); and three
independent slice routes plus a finite `exp(tM)` substitution (with a concrete
exact-Q det_2-isometry check) for the residual. The genuine-automorphism property
was tested by the *product* `g(A∘B)=g(A)∘g(B)` on generic exact-Q elements, not just
basis vectors. The action interpretation and the derivation/Leibniz properties were
themselves verified, not assumed. All guards (no `octonion_algebra`, no `numpy`, no
numerology, exact-over-Q) hold on my decisive path. **No discrepancy was found in any
of the five claims**; in particular the residual is exactly dim-1 so(2) (not so(3),
not a boost, not zero), and `g·E_11=E_22`/genuine-Aut holds for every tested element.
