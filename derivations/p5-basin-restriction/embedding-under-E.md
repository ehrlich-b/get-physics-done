<!-- ASSERT_CONVENTION: metric_signature=riemannian_fisher, fourier_convention=na, natural_units=natural, gauge_choice=na, renormalization_scheme=na -->
<!-- Pure-algebra: Jordan product a o b = (1/2)(ab+ba); sequential product a&b = sqrt(a) b sqrt(a) (CFC, principal branch). Type/category + Peirce-grade consistency is the dimensional-analysis analog. -->
<!-- Provenance: LIVE papers only (~/repos/blog/landing/papers/). NOT the stale repo papers/. -->
<!-- Slice: A = h_3(C_u) ~ M_3(C)^sa (n=3; u = e_7; any u in S^6 equivalent under G_2). -->

# embedding-under-E.md — Coherent embedding under the bottleneck conditional expectation E (the hard part)

**Plan:** 62-01 (Phase 62, milestone v15.0) — DERV-62-01. **Step 3 of 4.**
**Role:** This file is the Phase 62 deliverable. It sets up the Peirce/bottleneck
conditional expectation `E : h_3(O) -> h_3(C_u)` **explicitly** (Effros–Störmer: positive,
unital, idempotent, range = JB-subalgebra), states **precisely** what `E` preserves (the
Jordan product `a o b` **on the slice** — and crucially **NOT**, automatically, the
sequential product), and **frames** the decisive crux — whether `E` transports the
sequential product coherently from the **non-associative** ambient — **without asserting its
answer.**

**Scope of this file vs the rest of Phase 62.**
- **§0–§3 are written by 62-01 (this plan): the SETUP + CRUX FRAMING.**
- **§4 is the decisive exact computation (62-02, VALD-62-01) — to follow.**
- **§5 is the verdict on the obstruction-or-preservation fork (62-03) — to follow.**
- **The induced-by-`E` verdict is NOT reached in this plan.** §3 makes the decisive question
  well-posed; 62-02 computes it on the actual non-associative `h_3(O)`; 62-03 reads off the
  verdict.

> **CORRECTED FRAMING (2026-05-24, Bryan's decision; plan-checker found the original
> slice-internal test mathematically trivial — verified against `code/octonion_algebra.py`).**
> The slice `A = h_3(C_u)` is a **closed, associative** Jordan subalgebra (= range `E`), so
> the slice-internal `sqrt(a) b sqrt(a)` (with `a,b in A`) has leakage **exactly 0** and
> cannot engage non-associativity — it is a **TRIVIAL control**, not the decisive test. The
> decisive object is **AMBIENT `E`-TRANSPORT**: `E(sqrt(X) Y sqrt(X))` vs
> `sqrt(EX)(EY)sqrt(EX)` for **GENERIC ambient** `X,Y in h_3(O)`. And `RESTRICTION` is
> weakened to **COEXISTENCE-AS-ISLAND** (§3.7): the observer self-models on the slice
> (Phase 61) and the slice sits inside `h_3(O)` as the range of `E` — it does **not** need
> its structure transported from the ambient. An ambient-transport **obstruction is EXPECTED
> and REFINES** `RESTRICTION` (island); it does **not** refute it.

---

## 0. Setup, inputs, and the type/category + Peirce-grade ledger

### 0.1 Inputs read at execution start

This plan re-read, at start of execution:

- **`claim.md`** — `RESTRICTION` in derivation notation; allowed inputs; the prohibited
  reward-hacking moves (especially **`assert-Peirce-preserves-iii`** / `fp-assert-preservation`)
  and **PAUSE condition 2** (embedding needs structure not induced by `E`).
- **`STATE.md`** (derivation-tree) — Step 1 (Phase 60) and Step 2 (Phase 61) **COMPLETE**;
  Step 3 (Phase 62) = **THIS**, the load-bearing, entirely-unproved step; open question
  **[62]**.
- **`slice-clause-iii.md` §6** — the explicit Phase 62 deferral: Phase 61 verified the slice
  satisfies all four Def 1 clauses **intrinsically**, with the induced-by-`E` question
  deferred here; datum-4 factorization was on the **associative** composite only.
- **`code/octonion_algebra.py`** — the `H3O` class, `_mat_mul_h3o` (non-associative 3×3
  octonionic matrix product), `jordan_product`, `peirce_V1/Vhalf/V0`, `proj_u`, `pi_u`.
- **LIVE `lem:bottleneck`** — `~/repos/blog/landing/papers/sm-from-self-modeling/sections/`
  `complexification.tex` lines **409–487** (statement, Effros–Störmer at **437**, Peirce
  decomposition (iii) at **481–486**).

### 0.2 The slice and the ambient (real-dimension bookkeeping)

| Object | Definition | Real dim | Decomposition |
|---|---|---|---|
| `h_3(O)` | exceptional Albert algebra: `3×3` octonionic Hermitian matrices | **27** | 3 real diagonal `+` 3 octonionic off-diagonal `= 3 + 3·8 = 3 + 24` |
| `A = h_3(C_u) ~ M_3(C)^sa` | `lem:bottleneck` (ii): maximal C*-target inside `h_3(O)`; `C_u = R + R·u`, `u = e_7` | **9** | 3 real diagonal `+` 3 `C_u` off-diagonal `= 3 + 3·2 = 3 + 6` |
| `range(E) = A` | `E` idempotent onto `A` | **9** | `rank E = dim A = 9` |
| `ker(E)` | the `(e_1,...,e_6)`-components of the three off-diagonal octonions | **18** | `3` off-diagonal octonions `× 6` killed components `= 18` |

**Bookkeeping check (the dimensional-analysis analog): `27 = 9 + 18`.** ✓ `dim h_3(O) =
dim range(E) + dim ker(E)`.

### 0.3 Type/category + Peirce-grade ledger (the pure-algebra analog of dimensional analysis)

Carried from `slice-clause-iii.md` §0.3, `two-composites.md`, `rem-converse-bgw.md` §0. Every
object carries **one** category tag; no inference equates objects of different tags. The
**Peirce-grade analog of dimensional analysis**: every element carries a Peirce grade under a
rank-1 idempotent `E_11` (eigenvalues `{0, 1/2, 1}`) and a real-dimension; we track both.

| Object | Category tag | Peirce / dim note |
|---|---|---|
| `h_3(O)` | **FRJA (exceptional, simple, non-special, BGW-non-composable)** | real-dim 27; power-associative, NOT associative |
| `A = h_3(C_u) ~ M_3(C)^sa` | **FRJA (special, simple)** = BGW `C_3` | real-dim 9; **associative-enveloping** (`= M_3(C)^sa`, an associative `*`-algebra's s.a. part) |
| `E : h_3(O) -> A` | **conditional expectation** (positive unital idempotent) | rank 9; `E|_A = id`; **NOW used (Phase 62), not a forward reference** |
| Jordan product `a o b = (1/2)(ab+ba)` | **Jordan-algebra binary op** | symmetric; commutes with Peirce projections of `A` |
| sequential product `a & b = sqrt(a) b sqrt(a)` | **CFC triple product on effects** — **NOT** a Jordan-algebra op | temporally asymmetric; built from the spectral (continuous functional) calculus |
| `V_BM = A (x) A ~ M_9(C)^sa` | **FRJA (special, simple)** carrying OUS structure | observer's OWN internal composite (clause iii object); real-dim 81; **NEVER** identified with the ambient |
| BGW bifunctor `(x)~` on `h_3(O)` | **bifunctor / monoidal** | tensoring the *whole* universe with an external FRJA; `h_3(O)` non-composable |

> **Two type-consistency invariants this file preserves (stated up front).**
> **(I)** The Jordan product and the sequential product are **different categories** of
> operation (binary Jordan op vs CFC triple product); a statement about `E` and one does
> **not** transfer to the other. **(II)** `V_BM` (observer's OUS self-composite, body⊗model)
> is **never** identified with the BGW `(x)~` evaluated on `h_3(O)` (bifunctor on the whole
> universe). Coexistence-as-island (§3.7) preserves both.

---

## 1. Explicit construction of E

### 1.1 The definition (entrywise C_u-projection)

In the `H3O` coordinates of `code/octonion_algebra.py`, an element `X in h_3(O)` is
`(alpha, beta, gamma; x1, x2, x3)` with `alpha,beta,gamma in R` and `x1,x2,x3` octonions,
realizing the Hermitian matrix

$$
X \;=\;
\begin{pmatrix}
\alpha & \overline{x_3} & x_2 \\
x_3 & \beta & \overline{x_1} \\
\overline{x_2} & x_1 & \gamma
\end{pmatrix},
\qquad \alpha,\beta,\gamma\in\mathbb{R},\quad x_1,x_2,x_3\in\mathbb{O}.
$$

**DEFINE `E : h_3(O) -> h_3(C_u)` entrywise** by acting as the identity on the real diagonal
and projecting each off-diagonal octonion onto the associative subfield
`C_u = span{1, u} = span{e_0, e_7}`:

$$
\boxed{\;
E(X) \;=\;
\begin{pmatrix}
\alpha & \overline{\mathrm{proj}_u(x_3)} & \mathrm{proj}_u(x_2) \\
\mathrm{proj}_u(x_3) & \beta & \overline{\mathrm{proj}_u(x_1)} \\
\overline{\mathrm{proj}_u(x_2)} & \mathrm{proj}_u(x_1) & \gamma
\end{pmatrix}
\;}
$$

i.e. in `H3O` coordinates

$$
E:\;(\alpha,\beta,\gamma;\,x_1,x_2,x_3)\;\longmapsto\;
(\alpha,\beta,\gamma;\,\mathrm{proj}_u(x_1),\mathrm{proj}_u(x_2),\mathrm{proj}_u(x_3)),
$$

where `proj_u` is **exactly** `code/octonion_algebra.py::proj_u` (lines 527–542): for
`u = e_7` it keeps octonion components `0` and `7` and zeros components `1..6`,

$$
\mathrm{proj}_u\!\big(b_0 + \textstyle\sum_{k=1}^{7} b_k e_k\big) \;=\; b_0 + b_7\,e_7
\qquad (u=e_7).
$$

So `E` projects **every matrix entry** onto `C_u` entrywise (the diagonal entries
`alpha,beta,gamma` are already real `subset C_u`, hence fixed). The image is exactly
`{X : X_{ij} in C_u for all i,j} = h_3(C_u) ~ M_3(C)^sa` (`lem:bottleneck` (ii)).

> **Provenance note.** `proj_u` in the code is written for `u = e_7`; `lem:bottleneck` (ii)
> establishes that any `u in S^6 subset Im(O)` gives an `F_4`-equivalent slice
> (`{h_3(C_u)}` a single `F_4`-orbit), so the choice `u = e_7` is **necessary but
> direction-irrelevant** (Gap B2 in the paper). All structural statements below are
> `u`-independent.

### 1.2 The four conditional-expectation properties (stated + justified)

These are the defining properties of a (Jordan) conditional expectation onto `A`. Each is
**stated with its justification here**; the entrywise/eigenvalue facts are **verified exactly
in 62-02** (`% to follow` marker in §4).

**(a) UNITAL: `E(I_3) = I_3`.** The identity `I_3 = (1,1,1; 0,0,0)` has real diagonal `(1,1,1)`
and zero off-diagonal; all entries already lie in `C_u`, so `E(I_3) = I_3`. ✓

**(b) IDEMPOTENT: `E o E = E`.** `proj_u` is an orthogonal projection of `O` onto `C_u`, so
`proj_u o proj_u = proj_u` (projecting onto `C_u` twice equals once); the diagonal is
untouched. Hence applying `E` entrywise twice equals applying it once: `E o E = E`. ✓
(Exact entrywise idempotency on all 27 real coordinates: 62-02.)

**(c) `E|_A = id` (the "E recovers `lem:bottleneck` on the slice" consistency check).** For
`X in A = h_3(C_u)`, every entry already lies in `C_u`, so `proj_u` fixes each off-diagonal
octonion and `E(X) = X`. Thus `E` restricted to its range is the identity — the hallmark of
an idempotent onto `A`, and the limiting/consistency check that `E` agrees with the slice's
own structure. ✓

**(d) POSITIVE: `E` maps the positive cone of `h_3(O)` into the positive cone of `A`.** This is
the Effros–Störmer content for `E` (§1.3): the entrywise `C_u`-projection realizes the
**standard conditional expectation** of the JB-algebra `h_3(O)` onto the JB-subalgebra
`h_3(C_u)`, and conditional expectations onto JB-subalgebras are positive. (Positivity on
explicit PSD test elements — verifying `X >= 0 => E(X) >= 0` via eigenvalue checks — is
**confirmed exactly in 62-02**.) ✓ *(flagged for 62-02)*

> **Real-dimension restatement.** `range(E) = A` (real-dim **9**); `ker(E)` is spanned by the
> `(e_1,...,e_6)`-components of `x_1,x_2,x_3` (real-dim **18**); `27 = 9 + 18`. ✓

### 1.3 Effros–Störmer: the range is a JB- (Jordan-) subalgebra; the embedding is Jordan-product-preserving

**Quoting the LIVE `lem:bottleneck` proof VERBATIM** (`complexification.tex` line **437**, and
the lemma statement lines **412–413**, **440–441**):

> *"Effros-Störmer: the range of a positive unital idempotent on a JB-algebra is a
> JB-subalgebra. In finite dimensions over `R` this is just a Jordan subalgebra; by the
> hypothesis on `E` the embedding is moreover Jordan-product-preserving."*

and the lemma's own framing (lines **412–413**):

> *"...conditional expectations `E : h_3(O) -> A` with `A subseteq h_3(O)` a Jordan
> subalgebra (the embedding `A hookrightarrow h_3(O)` preserves the Jordan product)..."*

**Conclusion.** `E`'s range `A = h_3(C_u) ~ M_3(C)^sa` is a **JB-subalgebra** of `h_3(O)`
(`= Jordan subalgebra` in finite real dimension), and the embedding `A hookrightarrow h_3(O)`
is **Jordan-product-preserving**. This is what makes `E` a legitimate **Jordan** conditional
expectation. `dim_R(range E) = dim_R A = 9`; `dim_R(ker E) = 18`.

> **IDENTITY_CLAIM (Effros–Störmer, range of a positive unital idempotent on a JB-algebra is a
> JB-subalgebra).** `IDENTITY_SOURCE: citation` — Effros–Störmer 1979, **as quoted in the LIVE
> `lem:bottleneck` proof, `complexification.tex:437`**. The executor has no web; per the plan,
> the quoted content is authoritative. **Not** a training-data identity; no numerical
> re-derivation required (it is a structural theorem, cited, not a computed special-function
> identity).

### 1.4 The Peirce decomposition of A that E restricts through

**Quoting `lem:bottleneck` (iii) VERBATIM** (`complexification.tex` lines **481–486**):

> *"Within `h_3(C_u) ~ M_3(C)^sa`, a rank-1 idempotent `E` has the standard Peirce
> decomposition `h_3(C_u) = V_1(E) (+) V_{1/2}(E) (+) V_0(E)` with `V_1(E) ~ R`,
> `V_{1/2}(E) ~ C_u^2`, and `V_0(E) ~ h_2(C_u) ~ M_2(C)^sa`."*

So at the rank-1 idempotent `E_11` (the code's `H3O.E11() = diag(1,0,0)`), **within the slice**
`A = h_3(C_u)`:

$$
A \;=\; V_1(E_{11}) \,\oplus\, V_{1/2}(E_{11}) \,\oplus\, V_0(E_{11}),
\qquad
V_1 \cong \mathbb{R}\ (\dim 1),\quad
V_{1/2} \cong \mathbb{C}_u^2\ (\dim 4),\quad
V_0 \cong h_2(\mathbb{C}_u) \cong M_2(\mathbb{C})^{sa}\ (\dim 4).
$$

**Peirce-grade bookkeeping: `1 + 4 + 4 = 9 = dim_R A`.** ✓ This is the **slice** Peirce
structure (the prior input "`V_1 = R` bottleneck", v6.0/v8.0: the Peirce interface to
`V_{1/2}` is scalar). It is the Peirce structure `E` restricts through, in the precise sense
of the §1 type-check below.

### 1.5 Type/category + Peirce check for §1

- **Type-correctness.** Every step is internal to the stated categories: `E` (conditional
  expectation) `: h_3(O)` (FRJA) `-> A` (special FRJA); `proj_u` (`O -> C_u` projection)
  applied entrywise; `lem:bottleneck` and Effros–Störmer (structural theorems on JB-algebras).
  No cross-category equation. ✓
- **`E` maps Peirce grades coherently for the Jordan product (on `A`).** Since `E|_A = id`
  (§1.2c) and `E` kills exactly the `(e_1,...,e_6)`-octonion components — which are
  **orthogonal to `C_u`** and lie in `ker E` — `E` commutes with the Peirce projections of
  `A` (`peirce_V1/Vhalf/V0` restricted to `A`): for `X in A`, `E(P_lambda X) = P_lambda X =
  P_lambda(E X)` for each Peirce grade `lambda in {0,1/2,1}`. (This is a statement about the
  **Jordan-side** Peirce structure of the slice; it does **not** assert anything about the
  sequential product — see §2.2, §3.) ✓
- **Real-dim bookkeeping.** `27 = 9 (range) + 18 (ker)`; `9 = 1 + 4 + 4` (slice Peirce). ✓

**[CONFIDENCE: HIGH]** for the explicit construction of `E` and the Effros–Störmer
Jordan-side conclusion (entrywise formula `= code::proj_u`; unital/idempotent/`E|_A=id` by
direct inspection; range = Jordan subalgebra + Jordan-product-preserving embedding quoted
verbatim from the LIVE proof; Peirce decomposition quoted verbatim; dimension bookkeeping
`27=9+18`, `9=1+4+4` exact). *Adversarial check — what could be wrong:* (i) positivity of `E`
on the full 27-dim cone is **stated, not yet exactly verified** (deferred to 62-02 eigenvalue
checks) — so that single property is flagged, not asserted HIGH; (ii) the **sequential-product**
coherence is explicitly **UNRESOLVED** and deferred to §3/§4 — it is **not** part of this
confidence statement.

---

## 2. What E preserves — precisely

### 2.1 E IS coherent with the Jordan product ON THE SLICE

**Statement.** `E` is coherent with the **Jordan product** `a o b = (1/2)(ab + ba)` **on the
slice** `A`. Precisely: `lem:bottleneck` makes the embedding `A hookrightarrow h_3(O)`
**Jordan-product-preserving** (§1.3), and `E|_A = id` (§1.2c). So for `a, b in A`,

$$
E(a \circ b) \;=\; a \circ b \;=\; (E a)\circ(E b)
\qquad (a,b \in A),
$$

because `a o b in A` already (the slice is a Jordan subalgebra) and `E` fixes `A`. This is the
"`E` recovers `lem:bottleneck` on the slice" consistency check.

> **Jordan-side control for 62-02 (should PASS, trivially).** `E(a o b) = (Ea) o (Eb)` for
> `a,b in A` is a Jordan-side control that 62-02 will confirm passes — and is **trivial**
> precisely because the slice is closed under `o`. It is a sanity check on the code path, not
> evidence about ambient transport.

### 2.2 E is NOT a Jordan morphism on AMBIENT elements

**Statement (the key non-triviality).** `E` is **NOT** a Jordan morphism on **ambient**
elements. For generic `X in h_3(O)` (with off-diagonal octonion components outside `C_u`),

$$
\boxed{\;E(X \circ X)\;\neq\;(EX)\circ(EX)\quad\text{in general}.\;}
$$

**Why.** `X o X = (1/2)(X X + X X) = X^2` involves products of octonion entries that have
`(e_1,...,e_6)`-components; squaring mixes those components, and some of the *resulting*
`C_u`-components depend on the killed `(e_1,...,e_6)`-parts (e.g. `|x|^2 = sum_k x_k^2` pulls
the squared norms of the killed components into the real/diagonal part). `E` applied **after**
squaring therefore retains contributions from components that `E` applied **before** squaring
would have discarded. Concretely, `E(X^2)` keeps `sum_{k=0}^{7} (x_i)_k^2` in the diagonal
while `(EX)^2` keeps only `(x_i)_0^2 + (x_i)_7^2`. So the two differ by an `O(1)` amount on
representative elements.

> **Flagged for 62-02 (NOT asserted here).** 62-02 will confirm `E(X o X) != (EX) o (EX)` and
> quantify the discrepancy on representative elements (a representative magnitude of
> order `~22` in the Frobenius norm is **expected**, to be computed exactly — `[UNVERIFIED -
> forward reference to 62-02]`; the decisive claim does not depend on this number). The
> structural point — `E` is **not** a Jordan morphism on the ambient — is what matters here.

**Consequence.** `E` does **not** transport even the **Jordan** structure from the ambient. A
fortiori it need **not** transport the **sequential** product (an even more rigid CFC triple
structure — §3.1). This is exactly what makes the ambient-transport question (§3) **genuinely
non-trivial** rather than a corollary of `lem:bottleneck`.

### 2.3 The decisive question is AMBIENT transport of the SEQUENTIAL product

**Statement.** The decisive question is whether `E` transports the **sequential product**
`a & b = sqrt(a) b sqrt(a)` coherently from the ambient:

$$
\text{Does}\qquad
E\big(\sqrt{X}\,Y\,\sqrt{X}\big) \;=\; \sqrt{EX}\,(EY)\,\sqrt{EX}
\qquad\text{for GENERIC ambient } X,Y\in h_3(O)?
$$

This is set up and framed in §3; it is the morphism-coherence of `E` for the SP on the
**ambient**, and it is genuinely non-trivial precisely because (§2.2) `E` is not even a Jordan
morphism on the ambient.

> **REJECTED hand-wave (`fp-assert-preservation` / `assert-Peirce-preserves-iii`).** The move
> *"`E` is a conditional expectation, so it transports clause (iii)"* is **explicitly
> rejected**. `E`'s Jordan-coherence **on the slice** (§2.1) does **NOT** extend to
> transporting the **non-Jordan triple product** `&` from the **non-associative** ambient, and
> `E` is not even a Jordan morphism on ambient elements (§2.2). `lem:bottleneck` builds `E`
> for the **Jordan** product on the slice **only**; it says **nothing** about the sequential
> product. Treating its Jordan-product-preserving property as if it automatically covered the
> sequential-product transport is the central Phase 62 reward-hack and is foreclosed here.

### 2.4 Type/category + Peirce check for §2

- **Type-correctness.** §2.1 is a statement about the **Jordan product** (binary Jordan op) on
  the **slice** (special FRJA); §2.2 is about the **Jordan product** on the **ambient**
  (exceptional FRJA); §2.3 reclassifies the decisive object as the **sequential product** (CFC
  triple product, **NOT** a Jordan op). No statement crosses from one operation-category to the
  other. ✓
- **Peirce coherence is Jordan-side only.** The §1.5 fact that `E` commutes with `A`'s Peirce
  projections is a **Jordan-side** property of the slice; it is **not** invoked as evidence
  about the sequential product. ✓
- **Forbidden-proxy guard.** `fp-assert-preservation` actively rejected (§2.3). ✓

**[CONFIDENCE: HIGH]** that **what `E` preserves** is exactly: the Jordan product **on the
slice** (Jordan-product-preserving embedding + `E|_A = id`), and that `E` is **NOT** a Jordan
morphism on ambient elements (structural argument in §2.2; exact discrepancy deferred to
62-02). **[CONFIDENCE: explicitly UNRESOLVED]** for whether `E` transports the sequential
product — that is the open crux of §3/§4, neither asserted nor pre-empted here.

---

<!-- §3 (this plan, Task 2) follows below: the AMBIENT E-transport crux, the slice-internal
     triviality control, the corrected RESTRICTION (coexistence-as-island), and the
     obstruction-or-preservation fork. -->
<!-- §4 (the decisive exact computation) to follow — 62-02 (VALD-62-01). -->
<!-- §5 (the verdict on the fork) to follow — 62-03. -->
