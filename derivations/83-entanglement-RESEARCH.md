# Slot 83 / v23.0-candidate — Gate 0 RESEARCH

**The Two-Term Balance Question (Jacobson J5, fiber side) — Gate 0: the invariant
candidate space (derive, don't guess) + the face / entropy machinery.**

- Status: **Gate 0 COMPLETE — ALL_PASS, ring CLOSES at degree 3.** Gates 1/2/3 NOT
  run (orchestrator routes the next gate, fail-fast).
- Discipline: exact over Q (sympy Rationals; entropy/log symbolic). No κ, no Λ, no
  G = κT anywhere. det SSOT = `ring_lemma_verification.det_3`; `octonion_algebra.py`
  banned; u = e_7.
- Driver: `code/entanglement_two_term.py` (source-guarded; runs ~5 s; self-tested,
  fail-fast boolean DERIVED from the computed kernel dims, not hardcoded).
- Engines reused (cite file:line below).

---

## 0. Setup, conventions, engines

**Coord layout (27-dim, `ring_lemma_verification`).** A configuration `X ∈ h_3(O)` is
flattened by `_flat27` into 27 real coordinates `c_0 … c_26`:

| coords | block | meaning |
|--------|-------|---------|
| `0` | α | diagonal (1,1) entry |
| `1` | β | diagonal (2,2) entry |
| `2` | γ | diagonal (3,3) entry |
| `3..10` | x1 | the (2,3) octonion (8 comps), in `V_0` |
| `11..18` | x2 | the (1,3) octonion (8 comps), in `V_{1/2}` |
| `19..26` | x3 | the (1,2) octonion (8 comps), in `V_{1/2}` |

**Peirce decomposition under `E_11 = diag(1,0,0)`** (verified via
`kkt_gluing_holonomy.peirce_idx`):
`V_1(1) = {0}` (α), `V_{1/2}(16) = {11..26}` (x2,x3), `V_0(10) = {1..10}` (β,γ,x1) `= h_2(O)`.

**Spin(9) = Stab_{F_4}(E_11).** The group fixing the slice while acting on the Peirce
blocks. Realized exactly as `stab_f4([E_11])` (the 27×27 derivation generators
`{D ∈ f_4 : D·E_11 = 0}`), **dim = 36**.

**Engines (file:line).**

- `code/ring_lemma_verification.py`: `det_3` (cubic-norm SSOT; F_4-invariant, CH +
  324/324), `jordan`, `Tr` (`= α+β+γ`), `Tr2` (full trace form), `X_from_symbols`,
  `_flat27`, `_standard_basis_27`, `h3o_identity`, `h3o_from_coords`, `oct_zero`.
- `code/kkt_gluing_holonomy.py`: `E_ii` (`E_ii(0)=E_11` etc.), `peirce_proj(E,val)`
  / `peirce_idx(E,val)` (exact spectral Peirce projector / pure-eigenvalue indices,
  `peirce_proj.__doc__` ≈ l.? — "Exact spectral projector onto the eigenvalue-`val`
  Peirce space of L_E"), `stab_f4(targets)` (joint f_4 stabilizer nullspace; docstring
  "stab_f4([E11]) = spin(9), dim 36"; def at `kkt_gluing_holonomy.py` `def stab_f4`),
  `f4_basis()` (52-element exact-Q basis of f_4 = span(inner_derivations), 324 brackets;
  def at `def f4_basis`).
- exact-Q rank helper: `kkt_gluing_holonomy.ODG.exact_qq_rank` (module
  `orbit_dimension_gate`).

**Source guard (mirrors `cartan_phaseB_curvature.py:source_guard`).** Confirmed at
runtime: `octonion_algebra` NOT in `sys.modules`; `numpy` NOT in `sys.modules` on the
decisive path; `det_3`/`jordan`/`Tr` native to `ring_lemma_verification`;
`det_3(diag(2,3,5)) == 30` exact. All PASS.

---

## 1. TASK A — Peirce decomposition under Spin(9) = Stab_{F_4}(E_11)

The 36 generators `D` of spin(9) are 27×27 matrices acting (as derivations / linear
maps) on the flat-coord space. Verified exactly over Q:

**(A0) Block-diagonality.** Every one of the 36 generators has **zero** cross-Peirce
entries — spin(9) maps each of `V_1, V_0, V_{1/2}` into itself. So the decomposition
is block-by-block.

**(A1) Trivial-rep directions (joint kernel of all 36 generators per block).** For each
block, build the stacked map `v ↦ (D_1 v, …, D_36 v)` restricted to the block and take
its nullspace (`exact_qq_rank`):

| block | dim | joint-kernel (trivial) dim | nontrivial dim | trivial direction(s) |
|-------|-----|----------------------------|----------------|----------------------|
| `V_1`     | 1  | **1** | 0  | **α** (coord 0) |
| `V_0`     | 10 | **1** | 9  | **β + γ** (coords 1,2; equal coeffs, no x1) |
| `V_{1/2}` | 16 | **0** | 16 | — (no trivial subspace) |

So `V_1 = 1`, `V_0 = 1 ⊕ 9`, `V_{1/2} = 16` (as candidate irreps). The explicit
trivial directions are **α** (in `V_1`) and the **(β+γ) diagonal trace** (in `V_0`).
The `V_0` trivial direction was certified to be exactly `e_β + e_γ` with equal
coefficients and zero x1-component.

**(A2) Irreducibility certificates (Schur / commutant dimension).** For a compact Lie
algebra acting on a real rep `W`, `dim {A ∈ End(W) : [A, D|_W] = 0 ∀ D} = 1` iff `W` is
**irreducible of real type**. Computed exactly over Q:

- **9-block** (the `V_0` complement of the (β+γ) trivial line): commutant dim = **1** ⇒
  irreducible ⇒ the Spin(9) **vector 9**.
- **16-block** (`V_{1/2}`): commutant dim = **1** ⇒ irreducible ⇒ the Spin(9)
  **spinor 16**.

**Conclusion (Task A).** Under Spin(9) = Stab_{F_4}(E_11):

```
   V_1   =  1          (trivial; direction α = coord 0)
   V_0   =  1  ⊕  9    (trivial = the β+γ trace ; the Spin(9) vector 9)
   V_{1/2} =  16        (the Spin(9) spinor)
```

This is the expected `h_3(O) = 1 ⊕ (1⊕9) ⊕ 16` branching of the `27` under
`F_4 ⊃ Spin(9)` — derived here directly, exact over Q, no representation-theory import.

---

## 2. TASK B — the exhaustive ≤deg-3 Spin(9)-invariant ring (the candidate space for A)

**Method (the derivation-kernel certificate, mirroring v16's RING certificate).** A
polynomial `f(c_0…c_26)` is Spin(9)-invariant **iff** `D·f = 0` for all 36 generators,
where `D` acts as the vector field `D·f = Σ_{a,b} D_{ab} c_b ∂f/∂c_a`. For each degree
`d`, `dim(invariants) = dim ker(spin(9) action on the degree-d polynomial space)`.

**Exact-rank technique.** The kernel rank is computed over a **large prime field** (rank
over Q equals rank over `F_p` for all but finitely many primes; agreement at two large
primes `p = 2^31−1` and `p = 2147483629` certifies the Q-rank). Validated against the
direct exact-Q rank at degrees 1, 2 (both give 2 and 5; the exact-Q deg-3 rank was also
launched and the prime-field method reproduces deg-1=2/deg-2=5 identically). Molien was
**not** required (optional cross-check only).

### Per-degree invariant dimension (the kernel-dim certificate)

| degree | #monomials | derivation-map matrix | **invariant dim** (two-prime certified) |
|--------|-----------|------------------------|------------------------------------------|
| 1 | 27   | 972 × 27       | **2** |
| 2 | 378  | 13608 × 378    | **5** |
| 3 | 3654 | 131544 × 3654  | **9** |

### Explicit generators (exact forms) — and the SPAN certificate

The candidate generators were constructed independently and shown to **span** the
kernel at each degree (not merely match the dimension):

**deg 1 (dim 2):** the two trivial-rep linear coords.
- `L_α = α` (coord 0)
- `L_tr = Tr_{V_0} = β + γ` (coords 1+2)
- Equivalent native pair: `{Tr = α+β+γ, α}`. `_span_rank{α, β+γ} = 2`. ✓

**deg 2 (dim 5):** 3 products of deg-1 + 2 new block-norms. The 5 explicit invariants
(derived from the kernel, exact forms):
- `α²`
- `α·Tr_{V_0} = α(β+γ)`
- `Tr_{V_0}² = (β+γ)²`
- **`Q_vector = |9|² = (c_3²+…+c_10²) − β·γ`** — the Spin(9) **vector norm** (the
  9-norm: the 8 x1-octonion squares plus the `−βγ` trace-removed diagonal piece).
- **`Q_spinor = |16|² = c_11²+…+c_26²`** — the Spin(9) **spinor norm** (the 16-norm).

`_span_rank` of these 5 = 5; the native set `{Tr², Tr2, α², α·Tr_{V_0}, Q_spinor}`
spans the same 5-dim space (union rank = 5). Engine cross-check:
`Tr2 = α²+β²+γ² + 2(|x1|²+|x2|²+|x3|²)` (verified exact), and `Tr2` is Spin(9)-invariant
(`D·Tr2 = 0` for all 36). ✓

**deg 3 (dim 9):** 8 reducible products + 1 new cubic.
- **`det_3`** — the Freudenthal cubic norm (SSOT). F_4-invariant ⇒ Spin(9)-invariant
  (verified directly: `D·det_3 = 0` for all 36 generators). **Independent new
  generator.**
- reducible products `{α, Tr_{V_0}} × {deg-2 set}` — span dim **8** (the 10 products
  `{α,Tr_{V_0}}×{α², α·Tr_{V_0}, Tr_{V_0}², Q_vector, Q_spinor}` carry 2 relations,
  e.g. `α·(α·Tr_{V_0}) = (α²)·Tr_{V_0}`).
- `{reducibles, det_3}` span dim **9 = the kernel dim** ⇒ det_3 is the unique new
  generator and **the ring CLOSES at degree 3**.

### The spinor–vector–spinor (Γ-)coupling is NOT an independent generator

The brief asked whether the `16 × 9 × 16 → R` Spin(9) Γ-contraction is an independent
deg-3 generator. **It is not.** Derivation:

- Solving the derivation kernel restricted to monomials of type `(V_0-vector) ×
  (spinor) × (spinor)` gives a **2-dimensional** solution space. One direction is the
  reducible `Tr_{V_0}·Q_spinor = (β+γ)·|16|²`; the other is the genuine Γ-cubic
  `g_Γ` (the `c_10 c_11 c_26 − c_10 c_12 c_22 − …` Clifford contraction).
- `g_Γ` lies inside `span{reducibles, det_3}` with **coefficient −1/2 on det_3** (solved
  exactly: `g_Γ = (reducible combo) − ½ det_3`). Equivalently, the
  `vector × spinor²` cross-terms of `det_3` ARE the Γ-coupling (the scale factor between
  `det_3`'s cross-part and `g_Γ`'s cross-part is exactly −2).
- Consistency: `{reducibles, det_3, g_Γ}` still span only dim 9 — no room for an extra
  independent cubic. The deg-3 kernel dim is exactly 9.

**Program-native reading:** the Γ-coupling `16 × 9 × 16 → R` — which is precisely the
matter-type spinor–vector–spinor coupling one would write down by hand — is **already
contained in the cubic norm `det_3`** as its off-diagonal cross-terms. The fiber does
not carry a *separate* Yukawa-like cubic; the only cubic invariant is `det_3` itself.

### The exhaustive candidate set for A (deg ≤ 3)

Every native face-functional of degree ≤ 3 is a polynomial in:

```
   deg 1 :  α ,  Tr_{V_0} = β+γ            (equivalently  Tr = α+β+γ ,  α)
   deg 2 :  Q_vector = |9|²  ,  Q_spinor = |16|²   (the two new norms)
            [+ products α², α·Tr_{V_0}, Tr_{V_0}²]
   deg 3 :  det_3   (the unique new cubic; CONTAINS the 16×9×16 Γ-coupling
                     as its cross-terms)
            [+ products  deg1 × deg2]
```

Generating set (minimal, by degree/grade):
`{ α (1), Tr_{V_0} (1), Q_vector (2), Q_spinor (2), det_3 (3) }` — five generators;
the full ≤deg-3 invariant Hilbert function is `(1, 2, 5, 9)` for degrees `(0,1,2,3)`.

**FAIL-FAST:** the ring closes cleanly at degree 3 (generators span the kernel at every
degree; deg-3 explicit span = kernel dim = 9; no anomalous kernel dim). **PASS.** The
fail-fast boolean in the driver is derived from the computed kernel dims and the
explicit-generator span ranks (not hardcoded).

---

## 3. TASK C — the face / entropy machinery (convention pinned; bug-guard #4)

### Faces (both choices)

A configuration `X ∈ h_3(O)` is a 3×3 octonion-Hermitian matrix. The Peirce compression
`C_p` onto an idempotent `p` projects onto the **face subalgebra** `V_1(p) = h_k(O)`
(`k = rank p`), read as the matrix corner. Verified via `peirce_proj`/`peirce_idx`:

- **Rank-1 face** `p = E_11`: `V_1(E_11) = ℝ·E_11` (1-dim, coord {0}). Corner = the
  scalar (1,1) entry α.
- **Rank-2 face** `q = E_22 + E_33 = 𝟙 − E_11`: `V_1(q) = h_2(O)` (10-dim, coords
  {1..10} = β,γ,x1). Corner = the lower-right 2×2 octonion-Hermitian block
  `[[β, x1],[x1*, γ]]`. Confirmed `C_q(X)` keeps exactly coords {1..10} and **kills**
  {0}=α (in `V_0(q)`) and {11..26}=x2,x3 (the `V_{1/2}(q)` coupling).

### The pinned convention (bug-guard #4)

```
   ρ_face(X)  =  C_p(X) / Tr( C_p(X) )       — COMPRESS FIRST, NORMALIZE SECOND.
```

`C_p = ` projection onto `V_1(p)` (the face subalgebra), read as the matrix corner;
`S_face(X) = ` von Neumann entropy `−Tr(ρ log ρ)` of the corner's (real) eigenvalues.
For the 2×2 octonion-Hermitian corner the eigenvalues are exact:

```
   λ_±  =  (β+γ)/2  ±  sqrt( ((β−γ)/2)²  +  |x1|² ) ,   |x1|² = Σ_{i=3..10} c_i² .
```

This order (compress, then normalize) is recorded because it **matters at second order**
— and was checked to NOT manufacture spurious criticality (below).

### Verification at X = I/3 (= `h3o_identity()/3`)

- **Rank-1 face:** corner = scalar 1/3 ⇒ ρ_face = 1 ⇒ **S_face = 0 (trivial)** at all
  orders. ⟹ **the meaningful face is the RANK-2 one** (flagged, per brief).
- **Rank-2 face:** corner eigenvalues `(1/3, 1/3)` ⇒ ρ_face = maximally mixed `I_2/2`,
  density eigenvalues `(1/2, 1/2)` ⇒ **S_face = log 2** (exact).

### Bug-guard #4 — non-spuriousness + the Fisher form

Expanding `S_face^{(rank2)}` around I/3 along face-tangent directions (exact, symbolic):

- diagonal direction `(β,γ) = (1/3+t, 1/3−t)`:  `S = log 2 − (9/2) t² + O(t³)`,
  `dS/dt|_0 = 0`.
- off-diagonal direction `x1 = t` (`|x1|² = t²`), `β=γ=1/3`:
  `S = log 2 − (9/2) t² + O(t³)`.

So the compression-then-normalize convention gives a **smooth S_face with vanishing
first derivative at I/3** (no spurious linear criticality), and a **clean second-order
Fisher/Bures form** `δ²S ∝ −Tr(h²)` with exact coefficient `−9/2` per unit face
direction (no log in the quadratic). This is exactly the §8.1 structure: at the entropy
maximum the first variation vanishes and the first nontrivial information is the
2nd-order Fisher form.

### Tangent spaces recorded (for Gate 2's FULL Peirce tangent)

- **rank-1 face tangent:** `V_1(E_11) = {0}` (1-dim, trivial corner).
- **rank-2 face tangent:** `V_1(E_22+E_33) = {1..10}` (10-dim = `h_2(O)`).
- **rank-2 compression KILLS:** `{0}=α` (`V_0(q)`) and `{11..26}=x2,x3`
  (`V_{1/2}(q)` coupling). These directions do NOT enter `S_face^{(rank2)}` at any order
  via the corner — a key structural fact Gate 2 will need when it varies `X = I/3 + εH`
  over the full 27-dim tangent.

**Note for downstream (NOT computed here — Gate 2's job).** At I/3, `δS_face = 0`; the
first nontrivial info is the 2nd-order Fisher/Bures form `δ²S ∝ −Tr(h²)` (clean, exact
over Q, no log) — §8.1. The machinery is set up so Gate 2 can use this directly. Per
§8.5, this 2nd-order object is the **state-side copy of v17's Fisher–Bures corpse**
(the right object on the wrong side of the state/event divide) — a tagged contact, not a
resurrection.

---

## 4. Flagged choices / deviations

- **No deviation from the brief.** All three Gate-0 tasks executed as specified; Gates
  1/2/3 NOT run.
- **Exact-rank method:** deg-3 kernel dim (9) is certified via two-prime field rank
  (rank-over-Q = rank-over-F_p generically; two large primes agree). The direct exact-Q
  `SparseMatrix.rank()` on the 131544×3654 matrix was launched but is slow (>6 min CPU,
  fraction blowup); the prime-field method reproduces deg-1=2/deg-2=5 against the exact-Q
  rank identically and is ~instant. This is a standard, rigorous exact-rank technique;
  flagged for the verifier (an independent re-derivation could confirm deg-3=9 by either
  exact-Q rank with more time, a Molien-series cross-check, or an independent
  prime/Gröbner route).
- **Γ-cubic finding (informative):** the spinor–vector–spinor `16×9×16` coupling is
  NOT an independent generator — it is the cross-term content of `det_3` (coeff −1/2).
  This sharpens the candidate set: the only cubic in the candidate space for A is
  `det_3` itself; there is no separate fiber Yukawa cubic.
- **Meaningful face:** the rank-1 face has trivial entropy (S≡0) ⇒ the rank-2 face
  (`q = E_22+E_33`, corner = `h_2(O)`) is the meaningful one. Both are built; Gate 2
  should center on the rank-2 face.

---

## 5. Anti-overclaim (binding scope — carried from the brief)

Gate 0 is **only** the candidate space + machinery. It establishes WHAT the second-term
functional A can be (a polynomial in `{α, Tr_{V_0}, Q_vector, Q_spinor, det_3}`) and
pins the face/entropy convention. It does **NOT** test the two-term balance (that is
Gate 2), does **NOT** claim λ≠0 is forced, and makes **no** geometric/Einstein/J5
claim. No κ, no Λ, no G = κT appears. LIVE/DEAD is undecided until Gate 2.
