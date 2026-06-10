# Slot 83 / v23.0-candidate — Gate 0 INDEPENDENT VERIFICATION

**The Two-Term Balance Question (Jacobson J5, fiber side) — Gate 0.**
Independent re-derivation of the invariant candidate space + face/entropy machinery.

- **Overall verdict: PASS — all four claims INDEPENDENTLY CONFIRMED. Confidence HIGH.**
- The candidate-A ring `{α, Tr_{V_0}, Q_vector, Q_spinor, det_3}` (Hilbert function
  `1/2/5/9`) and the compress-then-normalize face convention are **INDEPENDENTLY
  CONFIRMED**. No discrepancies. deg-3 = 9 verified by THREE independent witnesses
  (Molien/Weyl character, two independent primes, explicit-generator span). The
  Γ-coupling is NOT independent (coeff −1/2). The face shows NO spurious linear term.
- Discipline: exact over Q (sympy Rationals; entropy/log symbolic). No κ, no Λ, no
  G = κT. `octonion_algebra.py` NOT imported (confirmed at runtime). `det_3` SSOT =
  `ring_lemma_verification.det_3`, `det_3(diag 2,3,5) == 30` exact. Decisive ring-rank
  paths used exact-Q (DomainMatrix/QQ) + integer prime fields; numpy appears ONLY in the
  independent abstract-representation cross-check (which agreed with the exact-Q
  commutant), never on the decisive deg-3 rank.

This is a from-a-different-path verification. I did **not** import or run
`entanglement_two_term.py` as evidence; I read it and the RESEARCH note only to know the
claims, then constructed independent oracles. Where the engine was used (peirce_idx,
stab_f4, det_3), I cross-validated the relevant structural facts by an independent method.

---

## Environment

Python 3.14, sympy 1.14.0, numpy 2.4.2. Code execution available (NOT static mode).

---

## Reference setup (ground-truth indices — confirmed, not the decisive evidence)

```
peirce_idx(E_11, 1)   = [0]            (V_1  = α)
peirce_idx(E_11, 0)   = [1..10]        (V_0  = β,γ,x1 = h_2(O))
peirce_idx(E_11, 1/2) = [11..26]       (V_{1/2} = x2,x3)
stab_f4([E_11]).dim   = 36             (= dim spin(9))
```

Coord layout (engine-native `_flat27`): `0=α, 1=β, 2=γ, 3..10=x1, 11..18=x2, 19..26=x3`.

---

## CLAIM (1) — Spin(9) Peirce decomposition  →  **PASS (INDEPENDENTLY CONFIRMED, HIGH)**

Claim: `V_1 = 1` (α), `V_0 = 1 ⊕ 9` (trivial = β+γ; vector 9), `V_{1/2} = 16` (spinor).

### (1a) Independent abstract B_4 = Spin(9) representation theory (NO engine)

I built the Clifford(9) algebra directly from the **octonion left-multiplication
matrices** `L_{e_i}` (i=1..7, each 8×8 real, verified `L_{e_i}² = −I` and antisymmetric).
From these I built **9 real symmetric 16×16 gamma matrices** on the spinor `R^16 = R^8⊕R^8`:

```
Γ_a = [[0, R_a],[R_aᵀ, 0]]  (a=0..7, R_0=I, R_i=L_{e_i}),   Γ_8 = diag(I_8, −I_8)
```

- Clifford algebra `{Γ_a, Γ_b} = 2 δ_ab I_16`: **verified** for all 9×9 pairs; all gammas
  symmetric.
- `so(9)` generators on the **16**: `Σ_ab = ¼[Γ_a, Γ_b]` (36 of them); on the **9**:
  standard `(M_ab)_cd = δ_ac δ_bd − δ_ad δ_bc`.
- 36 spinor generators: **span rank 36** (= dim so(9)) and **closed under bracket**
  (rank stays 36 after adjoining brackets).

Irreducibility — TWO independent certificates:

| rep | Quadratic Casimir `Σ_{a<b} T·T` | commutant dim (solve `[A,T]=0` via kron) |
|-----|---------------------------------|------------------------------------------|
| **16** (spinor) | scalar `−9·I_16` ✓ | **1** ⇒ irreducible, real type |
| **9** (vector)  | scalar `−8·I_9`  ✓ | **1** ⇒ irreducible, real type |

The Casimir being a scalar (Schur) AND commutant dim = 1 both certify irreducibility; the
specific eigenvalues `−9` (spinor) and `−8` (vector) are the standard B_4 values, pinning
the reps as exactly the **16** and **9** (not some other 16- or 9-dim rep).

### (1b) Independent exact-Q commutant on the ENGINE's Peirce blocks (cross-check)

On the 36 `stab_f4([E_11])` generators, computed **exact over Q** (DomainMatrix/QQ):

- **(A0)** Every generator is block-diagonal on `{V_1, V_0, V_{1/2}}` (zero cross-Peirce
  entries) — read directly off all 36 matrices. ✓
- **(A1)** Joint kernel per block (independent stacked-nullspace):
  `V_1 → 1`, `V_0 → 1`, `V_{1/2} → 0`. The V_0 trivial vector is
  **exactly `[1,1,0,0,0,0,0,0,0,0]`** in coords `(β,γ,x1[0..7])` = `β+γ` (equal coeffs,
  zero x1). ✓
- **(A2)** Commutant dim via independent exact-Q nullspace of `[A,D]=0` (kron method, NOT
  the engine's image-rank route): **16-block → 1**, **9-block (V_0/trivial) → 1**. ⇒ both
  irreducible. ✓

**Both routes agree.** `V_1 = 1`, `V_0 = 1 ⊕ 9`, `V_{1/2} = 16`; trivial directions are
exactly `{α}` and `{β+γ}`; the 9 and 16 are irreducible. **PASS.**

---

## CLAIM (2) — exhaustive ≤deg-3 Spin(9)-invariant ring  →  **PASS (INDEPENDENTLY CONFIRMED, HIGH)**

Claim: minimal generators `{α, Tr_{V_0}=β+γ, Q_vector, Q_spinor, det_3}`; Hilbert
function `(1, 2, 5, 9)` for deg `(0,1,2,3)`; ring closes at deg 3.

### (2a) Hilbert function via MOLIEN / WEYL CHARACTER integration (pure rep theory, NO engine, NO prime field)

Computed `dim Inv(Sym^d W)` for `W = 1 ⊕ 1 ⊕ 9 ⊕ 16` via the B_4 Weyl integration
formula: torus weights of `W` (two `0`-weights, vector `{±e_i, 0}`, spinor
`½(±,±,±,±)`, cleared via `z_i = w_i²`), the 16 B_4 positive roots
`{e_i±e_j, e_i}`, Weyl-measure factor `∏_{α>0}(1−z^α)(1−z^{−α})`, `|W| = 2⁴·4! = 384`,
constant-term (Laurent) extraction per degree:

```
   degree 0 1 2 3  →  invariant dim = 1, 2, 5, 9
```

This is an **independent third route** (the executor used neither Molien nor an exact-Q
deg-3 rank; this needs no engine at all). **It pins deg-3 = 9 from representation theory
alone.**

### (2b) deg-3 = 9 via INDEPENDENT prime fields (distinct from the executor's)

Derivation-kernel rank of the spin(9) action on degree-3 polynomials (matrix
`131544 × 3654`), computed by online Gaussian elimination over **two independent prime
fields** — `p = 1000000007` and `p = 998244353`, **both distinct** from the executor's
`2³¹−1` and `2147483629`:

```
   p = 1000000007 : map rank = 3645  ⇒  deg-3 invariant dim = 3654 − 3645 = 9
   p =  998244353 : map rank = 3645  ⇒  deg-3 invariant dim = 9
```

(Generator entries are rational with denominators in `{1,2,4}`; reduced mod p via modular
inverse — kernel of `D·f=0` is scale-invariant per generator.) **Agrees with Molien.**

### (2c) deg-1 = 2, deg-2 = 5 over EXACT Q (DomainMatrix/QQ)

Derivation-kernel exact-Q rank: deg-1 → **2**, deg-2 → **5**. (deg-3 over exact-Q on the
full 3654-wide matrix is the slow case the executor flagged; I replaced it with Molien +
two independent primes above, which is stronger.)

### (2d) Explicit-generator SPAN certificates (exhibit, don't just dim-match)

Each named generator is killed by all 36 generators (verified) AND the candidate set
**spans** the invariant space at each degree (exact-Q coeff-matrix rank):

| degree | candidates | each invariant? | span rank | target |
|--------|-----------|-----------------|-----------|--------|
| 1 | `α, β+γ` | yes | **2** | 2 ✓ |
| 2 | `α², α(β+γ), (β+γ)², Q_vector, Q_spinor` | yes | **5** | 5 ✓ |
| 3 | 10 reducibles `{α,β+γ}×deg2` | yes | **8** (2 relations) | 8 ✓ |
| 3 | `{reducibles, det_3}` | yes | **9** | 9 = kernel dim ✓ |

with `Q_vector = Σ_{3..10}c² − βγ`, `Q_spinor = Σ_{11..26}c²`, `det_3` =
`ring_lemma_verification.det_3` (verified Spin(9)-invariant: killed by all 36;
`det_3(diag 2,3,5)=30`). The reducibles alone reach only **8**, so `det_3` is genuinely a
new generator and the ring CLOSES at deg 3 (span = kernel dim = 9). **PASS.**

> **Three independent witnesses agree on deg-3 = 9** (Molien/Weyl character; two
> independent primes; explicit span lower-bound = 9). This is the load-bearing,
> executor-flagged number — fully corroborated, no discrepancy.

---

## CLAIM (3) — Γ-coupling (16×9×16) is NOT independent, coeff −1/2  →  **PASS (INDEPENDENTLY CONFIRMED, HIGH)**

### (3a) The (vector × spinor²) invariant solution space is exactly 2-dimensional

Solved the derivation kernel restricted to monomials of type `(V_0-coord) × spinor ×
spinor` (1360 such monomials). Solution space dim = **2**: one direction is the reducible
`Tr_{V_0}·Q_spinor = (β+γ)|16|²` (confirmed in the span, exact-Q); the other is the
genuine Γ-cubic `g_Γ`.

### (3b) g_Γ = (reducible) − ½ det_3

Decomposing `g_Γ` against `{Tr_{V_0}·Q_spinor, det_3-cross}` (exact-Q solve):

```
   g_Γ = −½ (Tr_{V_0}·Q_spinor)  −  ½ det_3      ⇒  coefficient of det_3 = −1/2
```

### (3c) Explicit cross-term scale factor = −2 (independent confirmation of −1/2)

Extracted the genuine spinor(x2)–vector(x1)–spinor(x3) part of `det_3` (its
`2 Re((x2 x1)x3)` cross-term, restricted to one factor in each of x1∈{3..10},
x2∈{11..18}, x3∈{19..26}) and of `g_Γ`:

```
   det_3|_{x2·x1·x3}  +  2 · g_Γ|_{x2·x1·x3}  ≡ 0      ⇒  scale factor = −2
```

i.e. `det_3`'s cross-part is exactly `−2 ×` g_Γ's cross-part, equivalent to the
`−1/2` det_3 coefficient. The `16×9×16` matter-type cubic is **already inside det_3** as
its off-diagonal cross-terms; the fiber carries no separate Yukawa cubic. **PASS.**

---

## CLAIM (4) — ρ_face / entropy machinery  →  **PASS (INDEPENDENTLY CONFIRMED, HIGH)**

Convention: **compress FIRST (project onto V_1(p)), normalize SECOND.**

### (4a) Faces (independent peirce_idx confirmation)

- Rank-1 face `V_1(E_11) = {0} = α`. Corner = scalar.
- Rank-2 face `V_1(E_22+E_33) = {1..10} = h_2(O)`; compression KILLS `{0}=α` (V_0(q)) and
  `{11..26}=x2,x3` (V_{1/2}(q)). ✓

### (4b) Entropy at X = I/3 (independent 2×2 corner build, exact symbolic)

2×2 octonion-Hermitian corner eigenvalues
`λ_± = (β+γ)/2 ± sqrt(((β−γ)/2)² + |x1|²)`; `ρ = corner/Tr(corner)`;
`S = −Σ p log p`.

- **Rank-1 face:** corner = 1/3 ⇒ ρ = 1 ⇒ **S ≡ 0 (trivial)** ⇒ the meaningful face is
  rank-2. ✓
- **Rank-2 face:** corner eigenvalues `(1/3, 1/3)` ⇒ ρ = I₂/2 ⇒ **S = log 2** (exact). ✓

### (4c) Fisher form: S_face = log2 − (9/2)t² + O(t³), NO linear term (≥2 directions)

| face direction | expansion | dS/dt|₀ | t² coeff |
|----------------|-----------|---------|----------|
| diagonal `(β,γ)=(1/3±t)`, x1=0 | `log2 − (9/2)t²` | **0** | **−9/2** ✓ |
| off-diagonal `|x1|²=t²`, β=γ=1/3 | `log2 − (9/2)t²` | **0** | **−9/2** ✓ |

Both trace-preserving face directions give the exact `−9/2` second-order Fisher form with
vanishing first derivative — clean, no log in the quadratic, no spurious linear
criticality.

### (4d) Order check — compress-then-normalize does NOT manufacture spurious linearity

Compared compress-then-normalize vs normalize-then-compress along trace-preserving and
non-trace-preserving directions at I/3. In every case the **compress-then-normalize
linear term = 0**; the `−9/2` (trace-preserving) and `−9/8` (asymmetric) quadratic forms
are robust. The pinned order does not generate a spurious `dS/dt ≠ 0`. **PASS.**

---

## GUARDS (confirmed on the decisive path)

| guard | status |
|-------|--------|
| `octonion_algebra` NOT in sys.modules (banned source) | **PASS** (False at runtime) |
| `det_3` native to `ring_lemma_verification`; `det_3(diag 2,3,5)==30` | **PASS** |
| decisive ring rank = exact-Q (DomainMatrix/QQ) + integer prime fields, NOT numpy.linalg | **PASS** |
| numpy used only for the independent abstract-rep Casimir/commutant cross-check (agreed with exact-Q commutant), never on the decisive deg-3 rank | **PASS** |
| no κ, no Λ, no G=κT, no physical constants; exact over Q; entropy symbolic (log) | **PASS** |

---

## Independent-route summary (how each decisive check differed from the driver)

| claim | executor route | my INDEPENDENT route |
|-------|----------------|----------------------|
| Spin(9) decomp | stab_f4 image-rank + commutant | abstract B_4 Clifford(9) gammas (Casimir + commutant) **and** exact-Q `[A,D]=0` kron-nullspace on engine blocks |
| deg-3 = 9 | two-prime field (`2³¹−1`, `2147483629`) | **Molien/Weyl character** (no engine) + **two independent primes** (`10⁹+7`, `998244353`) + explicit span = 9 |
| Γ-coupling −1/2 | kernel restriction + det_3 decomposition | independent type-restricted kernel (2-dim) + explicit `−2` cross-term scale factor |
| ρ_face | engine face machinery | hand-built 2×2 corner eigenvalues + symbolic series, 2 directions + order comparison |

---

## Discrepancies

**None.** deg-3 = 9 (not ≠ 9). The Γ-coupling is NOT independent (coeff −1/2, as claimed).
The face shows NO spurious linear term. The candidate-A ring and the compress-then-
normalize face convention are **INDEPENDENTLY CONFIRMED**.

## Scope (anti-overclaim)

This verifies ONLY Gate 0: the candidate invariant space + the face/entropy machinery. It
does NOT test the two-term balance (Gate 2), does NOT claim λ≠0 is forced, and makes no
geometric/Einstein/J5 claim. No κ, no Λ, no G=κT appears. LIVE/DEAD is undecided until
Gate 2.

---

**FINAL VERDICT: PASS on all four claims. Confidence HIGH.**
