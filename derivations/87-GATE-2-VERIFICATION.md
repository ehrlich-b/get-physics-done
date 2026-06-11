# 87 — GATE-2 VERIFICATION (independent): the anchor, the machinery, and THE REDUCTION

**v27.0 Phase 87 — independent verifier (separate code path, importing NEITHER v27
driver for the from-scratch checks). Exact over Q / Q(t). CONFIDENCE: HIGH.**

Scope of this file: D1 (well-posedness / strata bookkeeping), D2 (the multiplier
machinery + the hand anchor), and the **load-bearing reduction**
`λ² = |dG_M|²/|dc_R|²` — the step on which the whole LIVE verdict rests.

Verifier code paths used:
- `variety_equation_of_state.py` (executor): `sharp` = X∘X − Tr(X)X + σ₂I; `pi_half` =
  entry-block extraction. Re-run: **15/15 PASS** (1.8 s).
- `variety_equation_of_state_verify.py` (first independent path): `sharp_grad` (Gram
  dual of ∇N); eigenprojector `P_{1/2}=4L(I−L)`. Re-run: **5/5 PASS**.
- `/tmp/v87_scratch.py`, `/tmp/v87_hard.py`, `/tmp/v87_reduction.py` (this verifier's
  THIRD path): a literal octonionic adjugate `sharp_adj` (no `jordan` calls), three
  independent `π_{1/2}` constructions, and a metric-free reduction audit.
- v26 regression `variety_moment_doublet.py`: **27/27 PASS** (machinery intact).

---

## 0. Machinery regression (Gate 0 of the executor + an independent sharp)

The Freudenthal adjoint `X#` is the single most trap-prone object (octonion
product-order, guard #6). It is now pinned by **THREE** mutually independent
constructions agreeing symbolically over all 27 parameters:

| construction | formula | agrees with `sharp` symbolically? |
|---|---|---|
| `sharp` (executor) | `X∘X − Tr(X)X + σ₂(X)I` (Cayley–Hamilton) | — (reference) |
| `sharp_grad` (verify) | `Gram⁻¹ · (½ ∇N)` (gradient-of-norm) | yes (v27-verify PASS) |
| `sharp_adj` (this path) | literal 3×3 octonionic adjugate, no `jordan` | **yes** (`/tmp/v87_hard.py` STEP A) |

The literal adjugate required the **layout-correct** off-diagonal
`x₁# = conj(x₃·x₂) − α·x₁`, `x₂# = conj(x₁·x₃) − β·x₂`, `x₃# = conj(x₂·x₁) − γ·x₃`
(the reversed product order `conj(qp)`, determined empirically and matched against
`sharp`). My first naive attempt used `conj(x₂·x₃)` and FAILED `(X#)#=N·X` — a live
demonstration that the product-order trap is real, and that the engine's `det_3`/`sharp`
have it **right** (Phase-64.1 `(x₂x₁)x₃` factor order confirmed downstream).

`π_{1/2}` at E₁₁ pinned by THREE independent constructions agreeing symbolically
(`/tmp/v87_scratch.py` STEP 1): (1) entry-block extraction; (2) eigenprojector
`4L(I−L)`; (3) Lagrange projector `L(L−1)/(½−0)(½−1)`. All keep the (0,1)&(0,2)
octonion entries (coords {11..26}) and kill the diagonal + (1,2)-block — i.e.
`J_{1/2}(E₁₁)`, as required.

The two dG paths agree on a battery of families (Gate 0; reproduced from scratch in
`/tmp/v87_scratch.py` STEP 3): `d/dt G_M(p(t))|₀ == ⟨dG_M, ṗ(0)⟩` on families
(1,0),(1,1),(1,3),(1,7),(2,0),(2,5),(2,7) — **all exact over Q(t)**. This is the
second-path confirmation the prompt demands for the formula
`dG_M(p) = π_{1/2}(M# − ½⟨M,p⟩ M)`.

---

## D1 — well-posedness / strata bookkeeping

The parallel locus is non-empty off the trivial strata: the hand anchor (below) is an
explicit existence certificate (E₁₁ is on the locus against the real (1,0)-family for
every t ∉ {0,±1}).

Strata RECORDED and EXCLUDED from fork evidence (verified to be recorded-not-counted):
- `dc_R = 0` (p = R and the polar locus);
- `dG_M = 0` (G-critical points; e.g. diagonal/eigenframe-aligned M). Confirmed:
  `M = diag(2,−1,−1)` gives `dG = 0` (`/tmp/v87_battery.py`), and it is correctly NOT
  fed into the on-locus battery;
- `λ = 0`.

Guard discipline (metric-free, strata-honest, exact-over-Q) is respected: no `|∇·|`
norms enter any verdict (see the reduction note below — the multiplier ratio is
norm-independent), and float values never enter a verdict computation.

---

## D2 — the multiplier machinery (hand anchor, exact over Q(t))

`M₀ = F₁₂(1) + E₁₁ − E₃₃` (diagonal (1,0,−1), x₃ = e₀):

- `M₀# = [[0,1,0],[1,−1,0],[0,0,−1]]` — reproduced independently (executor + the
  literal-adjugate path).
- tuple `(a, c, TrM², detM) = (1, 0, 4, 1)` — confirmed on all three paths.
- `dG(E₁₁) = π(M₀#) − ½·1·π(M₀) = ½·F₁₂(1)`; `dc_R(E₁₁) = cs·F₁₂(1)` for the real
  (1,0)-family idempotent R(t).
- **on-locus check**: `supp(dG₀) = supp(dc_R) = {(0,1,0),(1,0,0)}` (identical 1-dim
  support) ⇒ the two covectors are PARALLEL ⇒ E₁₁ is genuinely on the locus
  (`/tmp/v87_reduction.py` CHECK 4). The negative anchor `M_{e₁}` (x₃=e₁) has
  `supp(dG) = {(0,1,1),(1,0,1)} ≠ supp(dc_R)` ⇒ correctly OFF the locus against the
  real family (CHECK 5), as designed.
- `λ = 1/(2cs) = (1+t²)²/(4t(1−t²))` from the literal component ratio; squared, this
  equals the reduction value `Q_M/|dc_R|²` **exactly over Q(t)** (CHECK 2). Hence
  `4 c_R(1−c_R) λ² = 1`, with `c_R = c(t)²`. λ is rational in t but only algebraic in
  the tuple (λ², not λ, is rational), consistent with the LIVE acceptance of a
  finitely-sheeted algebraic F.

**Tuple-rank (catch #8).** The M-tuple `(a, c, TrM², detM)` Jacobian has generic rank
**4** (`gate2`, reproduced) ⇒ functionally independent ⇒ NO forced relation among the
tuple coordinates ⇒ the tuple is correctly frozen as-is (no restatement needed). The
tuple genuinely MOVES when the geometry differs (`/tmp/v87_final.py` STEP 2: shifting
entry-norms shifts TrM²/detM), so the fork is not vacuous.

---

## THE REDUCTION (the load-bearing step) — VERIFIED SOUND and metric-free

Claim under test: on the locus, `λ² = |dG_M|²/|dc_R|²`, with
`|dc_R|² = |π_{1/2}(R)|² = 2 c_R(1−c_R)` for every rank-1 idempotent R.

**1. The ratio is norm-independent (the metric-free claim, made rigorous).** On the
parallel locus `dG_M = λ·dc_R`, so dG_M and dc_R are *the same vector up to the scalar
λ*. Therefore `|dG_M|² = λ²|dc_R|²` holds in **every** inner product, and
`λ² = |dG_M|²/|dc_R|²` is the same number in every norm. The only content is being ON
the locus (true parallelism, verified by support above). This is stronger than the
prompt's phrasing: the metric-freeness is not a delicate cancellation but a triviality
of comparing a vector to its own multiple. **A factor-of-2 norm convention (see the
note below) therefore cannot affect the verdict, provided the SAME norm is used in
numerator and denominator — which it is (both `normsq` = trace form).**

**2. `|π_{1/2}(R)| ² = 2 c_R(1−c_R)` for a battery of rank-1 idempotents** rebuilt by
this verifier (`/tmp/v87_scratch.py` STEP 2), each separately verified idempotent
(`R∘R=R`, Tr R=1):

| R | c_R | `|π(R)|²` | `2c_R(1−c_R)` | match |
|---|---|---|---|---|
| real (1,0)-family R(t) | (1−t²)²/(1+t²)² | … | … | exact over Q(t) |
| e₇ (1,0)-family R(t) | same | … | … | exact over Q(t) |
| rational (diag 9/25,16/25, off e₀=12/25) | 9/25 | 288/625 | 288/625 | ✓ |
| rational (diag 9/25,16/25, off e₇=12/25) | 9/25 | 288/625 | 288/625 | ✓ |
| rational (diag ½,½, off e₃=½) | ½ | ½ | ½ | ✓ |

So the denominator IS tuple-determined (a function of c_R alone) — exactly as required.

**3. Self-consistency at the anchor** (`/tmp/v87_reduction.py` CHECKs 1–3): `|dc_R|²`
matches `2c_R(1−c_R)` over Q(t); `(component ratio)² == Q_M/|dc_R|²` over Q(t);
`4c_R(1−c_R)λ² = 2Q_M = 1` on the anchor.

**Note — the `|π_{1/2}M|²` label carries a factor-of-2 (immaterial).** The prompt/
executor symbol `|π_{1/2}M|² := ½TrM² − a² + c` equals `|x₂|²+|x₃|²`, which is **half**
the trace-form norm `Tr((πM)∘(πM)) = 2(|x₂|²+|x₃|²)` actually computed by `normsq`
(`/tmp/v87_norm2.py`). This is a naming convention (coordinate sum-of-entry-norms vs
the Jordan trace-form norm), NOT an error: the reduction uses `normsq` consistently top
and bottom, the law `4c_R(1−c_R)λ² = (½TrM²−a²+c)(a²−4c)` is verified as a direct
identity for `2Q_M` (not via the label), and the anchor specialization is correct.
**Recommendation (cosmetic, non-blocking):** state once that `|π_{1/2}M|²` in the
factored prose denotes the half-norm `|x₂|²+|x₃|²`, so a future reader does not conflate
it with `Tr((πM)²)`. The verdict is unaffected.

---

## GATE-2 RESULT: PASS (HIGH confidence)

The anchor reproduces exactly over Q(t) on three independent sharp constructions; the
strata are recorded and excluded; the tuple is functionally independent (rank 4); and
**the load-bearing reduction `λ² = |dG_M|²/|dc_R|²` is sound and genuinely metric-free**
(the ratio is norm-independent on the locus; the denominator is tuple-determined via
`2c_R(1−c_R)`, confirmed on a battery of rebuilt idempotents). No design hole; proceed
to Gate 3.
