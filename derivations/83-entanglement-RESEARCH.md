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

---
---

# Gate 1 (calibration) + Gate 2 (THE TEST) — appended after Gate-0 verifier-hardening

**Status: Gate 1 PASS (the §8.1 tautology, zero evidence). Gate 2 VERDICT = DEAD at
degree ≤ 3.** Gate 3 NOT run (LIVE-only; orchestrator routes). Exact over Q (log
symbolic), source-guarded. Driver: `code/entanglement_two_term.py` (`gate1()`,
`gate2()`; self-tested, verdict ladder non-hardwired).

## 6. GATE 1 — calibration: X = I/3 is the unconstrained fixed-trace maximum of S_face

The pre-registered tautology (carries ZERO evidence; the setup-soundness check). Done by
expanding `S_face^{(rank2)}(I/3 + εH)` to O(ε²) for a **general 27-dim** perturbation `H`,
exact over Q. The eigenvalue degeneracy at I/3 (the rank-2 corner has coincident
eigenvalues 1/3, 1/3) makes the von Neumann entropy non-analytic; this is handled by the
`ε > 0` series (the `√(ε²·…) = ε·√(…)` branch), and the ε² coefficient simplifies to a
**polynomial** Fisher form (the residual `√` pieces cancel — verified).

**Results (exact over Q):**

- `S_face(I/3) = log 2` (rank-2 face; rank-1 face is trivial S ≡ 0).
- **δS_face = 0 in ALL 27 tangent directions at I/3** — the order-ε¹ term is identically
  zero as a polynomial in all `h_0…h_26`. (S_face depends only on the face block
  `{1..10}`; coords `{0}` and `{11..26}` never appear ⇒ δ = 0 there trivially.) This is
  the §8.1 degeneracy: `K = (log 3)·I`, first variations vanish.
- **Face Hessian negative-semidefinite ⇒ I/3 is the MAX.** The order-ε² form is
  `δ²S_face = (9/4)[−(h_β − h_γ)² − 4(h_3²+…+h_10²)]`, with eigenvalues (on the 10-dim
  face block):

  | eigenvalue | multiplicity | direction |
  |------------|--------------|-----------|
  | `0`   | 1 | the scale-invariant face-trace `(β+γ)` |
  | `−9/2`| 1 | the `(β−γ)` traceless-diagonal |
  | `−9`  | 8 | the x1-octonion directions `{3..10}` |

  All ≤ 0 ⇒ I/3 is the unconstrained fixed-trace maximum. The single zero eigenvalue is
  the entropy's scale-invariance (the face-trace direction).

**Gate 1 PASS.** The setup is sound. Per the pre-registration this proves **nothing**
about the route — the one-term extremum IS the tautology this run exists to go beyond.

## 7. GATE 2 — THE TEST: exhaustive forced-λ non-degenerate-competition sweep

**The candidate set.** Every degree-≤3 monomial in the Gate-0 generators
`{α(1), T=β+γ(1), Q_v(2), Q_s(2), det_3(3)}` — **16 monomials** total:

```
  deg 1 (2):  α ; T
  deg 2 (5):  α² ; α·T ; T² ; Q_v ; Q_s
  deg 3 (9):  α³ ; α²·T ; α·T² ; T³ ; Q_v·α ; Q_v·T ; Q_s·α ; Q_s·T ; det_3
```

**The constraint set** (bug-guard #3: `Tr X² = 1/3` is BANNED — it is the faithful
branch; imposing it as a constraint would trivialize the test):
`{ fixed Tr=α+β+γ, fixed Tr_face=β+γ, no constraint, fixed det=det_3 }`. **16 × 4 = 64
cells.**

### The linchpin and the criticality system

Gate 1 established `∇S_face(I/3) = 0` exactly. So the first-order criticality condition

```
   δ(S_face + λA) − μ·δg = 0   at I/3
   ⟺   ∇S_face(I/3) + λ·∇A(I/3) − μ·∇g(I/3) = 0
   ⟺   λ·∇A(I/3) − μ·∇g(I/3) = 0          (27-vector equation; ∇S_face = 0)
```

**`(λ, μ) = (0, 0)` ALWAYS solves this** (I/3 is already critical for S_face alone). So
**λ = 0 is always allowed**, and λ ≠ 0 is **never FORCED**. This was verified
**candidate-by-candidate** (the system was actually solved with `linsolve`, not assumed):

### Candidate gradients at I/3 (exact over Q)

| generator | ∇(·) at I/3 (nonzero coords) | note |
|-----------|------------------------------|------|
| `α` | `e_0` | diagonal |
| `T = β+γ` | `e_1 + e_2` | diagonal |
| `Q_v` | `−⅓(e_1 + e_2)` | ∝ ∇T (x1-quadratic vanishes at origin) |
| `Q_s` | `0` | **gradient vanishes** (purely quadratic in x2,x3) |
| `det_3` | `⅑(e_0 + e_1 + e_2)` | ∝ ∇Tr |
| `Tr` (constraint) | `e_0 + e_1 + e_2` | diagonal |
| `Tr_face` (constraint) | `e_1 + e_2` | diagonal |

**Every candidate gradient at I/3 lies in the 3-dim DIAGONAL subspace `span{e_0,e_1,e_2}`.**

### The 64-cell verdict — three failure modes, all → NOT FORCED

Solving each cell's `λ∇A − μ∇g = 0` (exact `linsolve`):

1. **Tautology** (∇A ≠ 0, no constraint): `λ∇A = 0` forces `λ = 0`. (e.g. `α|none`:
   solset `{(0,)}`.)
2. **λ-glaze** (∇A = 0, i.e. `Q_s` and its multiples `Q_s·α`, `Q_s·T`): λ is **free** ⇒
   DEAD (bug-guard #2: a free λ is DEAD, not LIVE). (solset `{(λ, 0)}`.)
3. **Constraint-absorbed** (∇A ∥ ∇g): the solution `(λ,μ)` is a 1-parameter family
   **including (0,0)** ⇒ λ = 0 allowed. (e.g. `det|fixed_Tr`: solset `{(9μ, μ)}`;
   `Q_v|fixed_Tr_face`: `{(−3μ, μ)}`; `det|fixed_det`: `{(μ, μ)}`.)

In **all 64 cells**, (λ,μ)=(0,0) solves the criticality ⇒ **λ ≠ 0 is NOT forced** in any
cell.

### VERDICT: DEAD at degree ≤ 3

**No candidate × constraint forces a non-degenerate competing λ ≠ 0.** The verdict is
DERIVED (the driver's DEAD/LIVE boolean = `not any_forced`, computed from the 64 solves,
not hardcoded).

### The precise obstruction pattern

```
  ∇S_face(I/3) = 0  (Gate 1, exact)
     ⟹  (λ,μ) = (0,0) solves criticality in EVERY cell
     ⟹  λ = 0 always allowed  ⟹  no forced two-term balance.

  Moreover: every candidate gradient at I/3 lies in span{e_0,e_1,e_2} (diagonal),
  while the S_face Fisher curvature lives on the TRACELESS face block (β−γ and x1).
  ⟹  the A-gradients pull only along diagonal/trace directions; there is no shared
      block on which the A-term and S-term could compete (no Jacobson saddle).
```

The deepest statement: **a forced two-term balance requires `∇S_face ≠ 0`, but I/3 is
the entropy MAXIMUM so `∇S_face = 0` necessarily.** The faithful point being the
vacuum/max (the route's own §4 identification) is *precisely what makes a forced balance
impossible there.* This is the §8.1/§8.2 deflation made exact over Q: the one-term
extremum is a tautology; Einstein lives in the *second* term's variation, and there is
no native second term that the faithful point can be forced to balance against.

### Note on the 2nd-order structure (why DEAD is first-order, not second-order)

Some candidate Hessians DO touch the Fisher block at I/3 (`Q_v`, `Q_v·T`, `Q_v·α` have
positive x1-block curvature; `det_3` has `−2/3` on the β−γ direction). So second-order
*structure* exists on the shared block. But it is **never triggered**: because
`∇S_face = 0`, the functional `S_face + λA` is critical at I/3 with λ = 0, and no
equation forces λ away from 0. The competition would only matter for a *forced* balance,
which never arises. Hence the obstruction is **first-order** (vanishing entropy
gradient), not a second-order misalignment.

## 8. Bug-guards (binding) — status

- **#1 VACUITY (no designed-in trivial pass):** SATISFIED. The forced-λ routine is
  GENERAL and **non-hardwired** — fed a hypothetical off-faithful input (`∇S_face ≠ 0`,
  not ∥ ∇g) it returns `forced = True`; at I/3 (`∇S_face = 0`) it returns `False`. So
  LIVE is detectable in principle, and the DEAD answer is a SUBSTANTIVE fact about I/3,
  not a rigged routine. (Self-test in `gate2()`.) The gate does NOT collapse to the
  first-law δS = δ⟨K⟩ identity — it tests the SECOND term (the λA balance), not the first
  law.
- **#2 λ-glaze:** SATISFIED. A free λ (∇A = 0, the `Q_s` family) is recorded as DEAD, not
  LIVE.
- **#3 constraint-smuggling (`Tr X² = 1/3` BANNED):** SATISFIED. Asserted absent from the
  constraint set.
- **#4 normalization (compress-then-normalize ρ_face):** SATISFIED. The pinned Gate-0
  convention is used throughout; Gate 1 confirmed it does not manufacture spurious
  criticality (δS_face = 0, no spurious linear term).
- **#5 u-alignment:** N/A — no inter-face map is used in Gate 1/2 (all work is at I/3 on a
  single face; no bare transposition / antiholomorphic conjugation enters).

## 9. Anti-overclaim (binding) + §8.5/§8.5a notes

- **DEAD at degree ≤ 3 ≠ absolute DEAD.** Higher degree remains, with a naturalness
  penalty (said once, not inflated). The candidate space was exhaustive **through degree
  3** (the Gate-0 closure); degree ≥ 4 invariants exist but are increasingly unnatural as
  a "geometric/volume" second term.
- **LIVE would have been ≠ Einstein/gravity/J5-won.** This is moot (verdict is DEAD), but
  for the record: the test was the FIBER SHADOW of J5 only; the geometric/base matching
  stays gated on the base/format object.
- **§8.5 contact (noted, not a resurrection):** the I/3 2nd-order object `δ²S_face ∝
  −Tr(h²)` is the SAME Fisher–Bures object v17 built and that died — STATE-side. This run
  confirms it is the right object on the wrong side of the state/event divide; it does not
  resurrect v17.
- **§8.5a (the MODIFIED Jacobson target):** the J5 target is the CGM/Speranza R^(2Δ)
  modified conjecture, not the naive 2015 form. **No contact is forced here** — the DEAD
  verdict is about the *existence of a native second term on the fiber*, which is upstream
  of any R^(2Δ) / relevant-operator question (those live on the un-built emergent QFT, the
  base/format object). The fiber simply carries no forced competing geometric term at the
  faithful point.
- No κ, no Λ, no G = κT anywhere in Gate 1 or Gate 2.

## 10. Flagged choices / deviations (Gate 1/2)

- **No deviation from the brief.** Gate 1 + Gate 2 executed as specified; Gate 3 NOT run
  (DEAD verdict ⇒ LIVE-only Gate 3 is correctly skipped).
- **Degenerate-eigenvalue handling:** the von Neumann entropy is non-analytic at I/3
  (coincident face eigenvalues). Handled rigorously by the `ε > 0` series expansion; the
  ε² Fisher coefficient is a genuine polynomial (residual `√` terms cancel under
  `simplify` — verified). Flagged for the verifier: an independent re-derivation could
  confirm `δS_face = 0` (all 27 dirs) and the Hessian eigenvalues `{0, −9/2, −9×8}` via a
  direct perturbation of the 2×2 corner eigenvalues, or via the relative-entropy /
  Bures-metric route.
- **Verdict is structural and over Q:** the DEAD conclusion rests on the exact fact
  `∇S_face(I/3) = 0` (Gate 1) plus the exact candidate gradients (all diagonal). Both are
  reproducible exactly; no floating point, no approximation.

---

## Milestone verdict (one paragraph, v21/v22 format)

**v23.0 (The Two-Term Balance Question — Jacobson J5, fiber side) — VERDICT: DEAD at degree ≤ 3.** Running the fail-fast gates cheapest-first (executor + independent verifier, different code paths, exact over Q): **Gate 0** DERIVED the exhaustive low-degree candidate space — under Stab_{F_4}(E_11)=Spin(9) the Peirce blocks decompose as V_1=1(α) ⊕ V_0=1(β+γ)⊕9(vector) ⊕ V_{1/2}=16(spinor), and the degree-≤3 invariant ring is generated by {α, Tr_{V_0}=β+γ, Q_vector, Q_spinor, det_3} (Hilbert 1/2/5/9; the spinor–vector–spinor Γ-coupling is NOT independent — it is det_3's cross-term, coefficient −1/2; verifier-confirmed HIGH incl. a from-scratch Spin(9)=B_4 Molien for the deg-3 count). The meaningful face is the rank-2 compression (q=E_22+E_33), whose ρ_face sees only V_0(E_11)=h_2(O); the rank-1 face is trivial (S≡0). **Gate 1** (calibration, the §8.1 tautology, zero evidence) confirmed X=I/3 is the unconstrained fixed-trace maximum of S_face: δS_face=0 in all 27 tangent directions (a polynomial identity), face Hessian eigenvalues {0, −9/2, −9×8} ≤ 0. **Gate 2** (the decisive test) swept all degree-≤3 monomials in the candidate ring × the four native constraints {fixed Tr, fixed Tr_face, no constraint, fixed det} (Tr X²=1/3 BANNED) = 64 exact cells: **no candidate × constraint forces λ≠0.** The mechanism, certified cell-by-cell (not assumed): since ∇S_face(I/3)=0, criticality reduces to λ∇A=μ∇g, and (λ,μ)=(0,0) always solves it ⇒ λ is never forced; every candidate gradient lies in the diagonal span{e_0,e_1,e_2} (∇Q_spinor=0; ∇det_3=⅑∇Tr) while S_face's Fisher curvature lives on the disjoint traceless face block ⇒ no shared block, no Jacobson saddle. **What it establishes:** the fiber-side scope theorem — the second/geometric Jacobson term provably does NOT live on the h_3(O) fiber at low degree (the fiber-side analog of "Molien has no κ-slot"); the entanglement route is fully gated on the base/format object (the un-built emergent QFT). The deepest statement: the faithful point being the entropy maximum (∇S_face=0) is precisely what forbids a forced two-term balance there. **What it leaves open / scope (binding):** DEAD-at-degree-≤3 ≠ absolute DEAD (degree ≥ 4 invariants remain, with a naturalness penalty — stated once); LIVE would have been the FIBER SHADOW of J5 only, never Einstein/gravity/J5-won; the J5 target is the MODIFIED (CGM/Speranza R^(2Δ), §8.5a) Jacobson, and this DEAD sits UPSTREAM of the R^(2Δ) question (it is about whether a native second term exists at all). The I/3 second-order object δ²S_face∝−Tr(h²) is v17's Fisher–Bures corpse on the state side (§8.5, contact not resurrection). **Bug-guards (binding) all held:** the forced-λ routine is NON-HARDWIRED — it returns forced=True for hand-built off-faithful inputs and False at I/3 — so the gate genuinely tests the second term and the DEAD verdict is SUBSTANTIVE, not the designed-in-trivial first-law δS=δ⟨K⟩ vacuity the prompt pre-registered (#1, third instance of that bug class, avoided); the Q_spinor λ-glaze correctly reads DEAD (#2); Tr X²=1/3 banned (#3); compress-then-normalize ρ_face manufactures no spurious criticality (#4); u-alignment N/A single-face/single-point (#5). No κ, no Λ, no G=κT anywhere. All decisive arithmetic exact over Q (entropy/log symbolic); Gate 0/1/2 verifier-hardened HIGH (the decisive Gate 2 independently confirmed through a different code path: closed-form 2×2 corner eigenvalues for the ∇S_face=0 linchpin, independent candidate gradients, an independent non-hardwired forced-λ routine). Deliverables: `code/entanglement_two_term.py`, `derivations/83-entanglement-RESEARCH.md`, `derivations/83-GATE-{0,1,2}-SUMMARY.md`, `derivations/83-GATE-{0,2}-VERIFICATION.md`.
