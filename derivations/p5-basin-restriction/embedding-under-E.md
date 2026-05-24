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
- **§4 is the decisive exact computation (62-02, VALD-62-01) — BELOW; verdict (O), an exact ambient-transport obstruction (the expected outcome, refining `RESTRICTION` to coexistence-as-island).**
- **§5 is the verdict on the obstruction-or-preservation fork (62-03) — BELOW; verdict (O), the ambient-transport obstruction read off §4, interpreted as a REFINEMENT of `RESTRICTION` to coexistence-as-island (not a refutation, not a collapse).**
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

## 3. The crux: does E transport the sequential product coherently from the non-associative ambient?

This is the analytic heart of the setup. 62-02 turns §3's decisive question into an exact
computation; this plan **frames** it and keeps the verdict **open**.

### 3.1 The two products, and E on each

- **Jordan product `a o b = (1/2)(ab + ba)`** — a symmetric **Jordan-algebra binary op**. `E`
  preserves it **ON THE SLICE** (§2.1: `lem:bottleneck` Jordan-product-preserving embedding +
  `E|_A = id`). But `E` is **NOT** a Jordan morphism on **ambient** elements (§2.2):
  `E(X o X) != (EX) o (EX)` in general — to be confirmed in 62-02 (a representative Frobenius
  discrepancy of order `~22` is **expected**, `[UNVERIFIED - forward reference to 62-02]`). So
  **even the Jordan structure is not transported from the ambient by `E`** — a fortiori the
  sequential product need not be.

- **Sequential product `a & b = sqrt(a) b sqrt(a)`** — a **CFC-based, temporally-asymmetric
  TRIPLE product on effects**, **NOT** a Jordan-algebra op. It is clause (iii)'s fourth datum
  (`ref-paper5-def1`, `def:product-sp`; `sms:minimal`, `main.tex` 351–353: *"product-form
  sequential product"*). Here `sqrt(·)` is the **principal** square root via the continuous
  functional calculus (CFC); on a power-associative formally real Jordan algebra, `sqrt(a)` for
  `a >= 0` is a limit of polynomials in `a` (so `sqrt(a)` lies in the associative subalgebra
  `R[a]` generated by `a`), but `sqrt(a) b sqrt(a)` for **generic** `a, b` is a triple product
  that genuinely engages the non-associativity of the ambient.

- **KEY POINT.** The decisive question is whether `E` **TRANSPORTS** the sequential product
  from the ambient:

$$
\boxed{\;
E\big(\sqrt{X}\,Y\,\sqrt{X}\big) \;\overset{?}{=}\; \sqrt{EX}\,(EY)\,\sqrt{EX}
\qquad\text{for GENERIC ambient } X,Y\in h_3(O).
\;}
$$

This is the **morphism-coherence of `E` for the sequential product, on the ambient** — and it
is genuinely non-trivial precisely because (§2.2) `E` is not even a Jordan morphism on the
ambient.

### 3.2 Why the slice-internal version is TRIVIAL — recorded plainly as the CONTROL

> **The slice-internal `sqrt(a) b sqrt(a)` with `a, b in A` is mathematically TRIVIAL and
> carries NO information about ambient transport. It is the documented CONTROL, not the
> decisive test.**

**Statement.** The slice `A = h_3(C_u)` is a **CLOSED, ASSOCIATIVE** Jordan subalgebra of
`h_3(O)` (`= range E`; `A ~ M_3(C)^sa` is the self-adjoint part of the **associative**
`*`-algebra `M_3(C)`). Therefore, for `a, b in A`:

1. `sqrt(a)` (for `a >= 0`, `a in A`) is the `M_3(C)` square root and **lies in `A`** (CFC
   inside the associative subalgebra `R[a] subset A`).
2. `sqrt(a) b sqrt(a) in A` (closed under the associative product), so
   `E(sqrt(a) b sqrt(a)) = sqrt(a) b sqrt(a)` — **leakage EXACTLY 0**.
3. The triple associator `[sqrt(a), b, sqrt(a)] = (sqrt(a) b) sqrt(a) - sqrt(a)(b sqrt(a))` is
   **EXACTLY 0** in `A` (associative).
4. Hence `E(sqrt(a) b sqrt(a)) = sqrt(a) b sqrt(a) = sqrt(Ea)(Eb)sqrt(Ea)` (since `E|_A = id`):
   the sequential-product datum is **induced TRIVIALLY** on the slice; **non-associativity is
   NOT engaged**.

This is just Phase 61's intrinsic result re-seen: the slice carries clause (iii) in its own
right because it is **trivially closed** under `&` (the `M_9(C)^sa` factorization of 61-02 is
the composite-level shadow of this slice-level closure). Quantitatively (carried context from
`code/octonion_algebra.py`-style checks, to be reconfirmed in 62-02): the **slice associator is
`~1e-15`** (machine zero) while the **ambient associator is `~170`** (`O(1)`) on
representative elements — `[UNVERIFIED - forward reference to 62-02]`, flagged to make the
control-vs-decisive distinction quantitatively sharp, not asserted here.

> **REWARD-HACK FORECLOSED (`fp-ignore-nonassociativity`).** Two loopholes are **explicitly
> foreclosed**: (i) passing the **trivial slice-internal** residual off as the decisive
> non-associative result (it is leakage-0 by closure — it can **only** say "0", and that "0"
> means *nothing* about ambient transport); and (ii) the **line-loophole** of running a
> non-associativity exerciser on **UNRELATED** matrices (to "show non-associativity is
> engaged") while the **decisive** test silently stays the trivial slice-internal one. The
> decisive object **must** be the **ambient** transport residual for **generic** `X, Y` (§3.3),
> with non-associativity load-bearing on the **same** `X, Y` whose residual is tested.

### 3.3 The decisive computable question = AMBIENT E-transport (the 62-02 spec)

State the decisive computation precisely (this is the spec 62-02 / VALD-62-01 implements):

- **INPUT.** GENERIC `X, Y in h_3(O)` — **NOT** confined to the slice. `X >= 0` (PSD, so
  `sqrt(X)` exists); `Y = Y^dagger in h_3(O)`. The off-diagonal octonion entries of `X, Y`
  must have nonzero `(e_1,...,e_6)`-components (i.e. they are **not** in `C_u`), so that the
  triple product genuinely leaves the slice.

- **COMPUTE the ambient sequential product.** Form `SP_ambient(X,Y) = sqrt(X) Y sqrt(X)` where
  `sqrt(X)` is computed **in the ambient** `h_3(O)` by the ambient CFC/spectral calculus (`h_3(O)`
  is power-associative, so `sqrt(X) in R[X]` is well-defined as a limit of polynomials in `X,
  I`), and the products use the octonionic `3×3` matrix product (`code/octonion_algebra.py::`
  `_mat_mul_h3o` style, **ported to EXACT arithmetic** — §3.4). Because `X, Y` are generic
  ambient, the triple product genuinely engages `(xy)z != x(yz)`.

- **TEST the AMBIENT TRANSPORT RESIDUAL:**

$$
\boxed{\;
R \;:=\; E\big(\sqrt{X}\,Y\,\sqrt{X}\big) \;-\; \sqrt{EX}\,(EY)\,\sqrt{EX},
\;}
$$

where the RHS computes the sequential product of the **projected** elements `EX, EY` using the
**slice** square root of `EX` (which lies in `A`, so `sqrt(EX) in A`).

  - **EXACT `R = 0`** `=>` `E` **TRANSPORTS** the sequential product coherently — branch **(P)**.
  - **EXACT `R != 0`** `=>` `E` does **NOT** transport it: an **AMBIENT-TRANSPORT OBSTRUCTION**
    — branch **(O)**, the **EXPECTED** outcome.

- **NON-ASSOCIATIVITY MUST BE LOAD-BEARING (mandate for 62-02).** The chosen `X, Y` must
  genuinely exercise `(xy)z != x(yz)`: 62-02 must **verify the associator of the relevant
  ambient triple is NONZERO on the chosen `X, Y`** (so the test is not accidentally
  associative). The associator check and the residual `R` must be on the **same** `X, Y`.

- **INDEPENDENT CROSS-CHECK (mandate for 62-02).** A **second** route to the same verdict: a
  **Peirce / grade-component** argument decomposing both `sqrt(X) Y sqrt(X)` and the projected
  product into `C_u`-vs-`(e_1,...,e_6)` components (equivalently, tracking Peirce grades and
  whether the transport defect populates `ker E`). The two routes (direct residual `R` and the
  grade-component decomposition) **must agree** on the verdict.

### 3.4 EXACT-ARITHMETIC requirement (methodological — carry VERBATIM into 62-02)

- **Exact, not float.** The transport-residual test **MUST** distinguish a genuine obstruction
  from numerical round-off. Use **EXACT arithmetic** (SymPy symbolic / exact rationals/surds),
  **NOT** float64. A nonzero `R` at float64 tolerance is **NOT** evidence; an **EXACT** nonzero
  `R` **IS**.

- **Handling ambient square roots.** Ambient square roots of generic PSD elements may be
  irrational. Handle either via **symbolic `sqrt`**, **or** by the **exact-square trick**:
  choose `X = C^2` (Jordan square / `C o C` with `C` an ambient element of exact entries) so
  that `sqrt(X) = |C|` is exact — **WHILE keeping `X, Y` GENERIC ambient** (off-diagonal entries
  with nonzero `(e_1,...,e_6)`-parts, **NOT** in the slice) so the triple product genuinely
  exercises non-associativity. **Document the construction and CONFIRM it does NOT trivialize
  non-associativity** (verify the associator is nonzero on the chosen `X, Y` — §3.3 mandate).

- **ERROR BUDGET: zero-tolerance decisive test.** `exact R == 0` (e.g. SymPy
  `(R).equals(zeros)` / `simplify(R) == 0`) `=>` coherent transport; `exact R` symbolically
  nonzero `=>` obstruction. **NO float tolerance on the decisive assertion.** (Contrast: the
  Jordan-side control `E(a o b) = (Ea) o (Eb)` for `a,b in A` is exact-0 trivially; the
  ambient-Jordan discrepancy `E(X o X) - (EX) o (EX)` is exact-nonzero — both are sanity
  context, not the decisive SP residual.)

### 3.5 Structural expectation (before computing — stated WITHOUT pre-deciding)

- **`E` is not a Jordan morphism on the ambient (§2.2).** The sequential product is an even
  more rigid (CFC triple) structure than the Jordan product. So it would be **UNSURPRISING** if
  `E` fails to transport it (`R != 0`). This is a **structural observation**, **NOT** a prior
  that forces the verdict. Where a defect would land, structurally: in `ker E` (the
  `(e_1,...,e_6)`-octonion components) — the ambient `sqrt(X) Y sqrt(X)` can populate
  `(e_1,...,e_6)`-components that `E` then projects away, so `E(sqrt(X) Y sqrt(X))` need not
  equal the all-slice `sqrt(EX)(EY)sqrt(EX)`.

- **DROP the v11.0/Phase 42 precedent as a leaning-toward-(O) prior (plan-checker warning).**
  GPD Phase 42 found `sqrt(T_a) T_b sqrt(T_a) = (i/2) T_b` exits `M_16(R)` for anticommuting
  Cl(9,0) pairs. **That is a DIFFERENT mechanism** — Clifford **non-commuting pairs in a fixed
  matrix algebra** `M_16(R)`, **not** the `h_3(O) -> h_3(C_u)` **projection/restriction** at
  issue here. Per the plan-checker, it does **NOT** bear on the ambient `E`-transport verdict;
  it is noted as **historically adjacent only**, **not** as evidence. (Carried context, not a
  premise: `claim.md` allowed-inputs item 7.)

- **HONEST EXPECTATION.** An ambient-transport **obstruction (O) is the EXPECTED, ACCEPTABLE**
  outcome (and would **REFINE** `RESTRICTION` to coexistence-as-island, §3.7) — but **the
  verdict is decided by the exact computation (62-02), not by this expectation.** Do **NOT**
  pre-commit (`fp-force-positive`).

### 3.6 The obstruction-or-preservation fork (stated, kept OPEN; CORRECTED verdict semantics)

| Branch | Condition (62-02) | 62-03 consequence | Status |
|---|---|---|---|
| **(P) COHERENT TRANSPORT** | exact `R = 0` | `E` transports `&` coherently `=>` 62-03 states and proves the **`RESTRICTION` embedding lemma** (touching the actual non-associative structure) | OPEN |
| **(O) AMBIENT-TRANSPORT OBSTRUCTION** | exact `R != 0` | 62-03 characterizes the obstruction precisely (the exact structure `E` cannot transport; where the defect lands — Peirce grade / `e_k`; the minimal extra input) and **REFINES `RESTRICTION` to coexistence-as-island** (§3.7) | OPEN; **EXPECTED**, fully acceptable DELIVERABLE; **NOT** a program-collapse PAUSE |

- This plan does **NOT** decide the fork. **62-02 provides the decisive evidence (the exact
  ambient residual `R` + associator-nonzero check + Peirce cross-check); 62-03 reads the
  verdict.** Handoff wired explicitly: **62-02's exact ambient residual `R` is the decisive
  input to 62-03's verdict.**

- **Corrected semantics (important).** Under the CORRECTED framing (§3.7), an obstruction (O)
  is **NOT** the milestone-collapse outcome (`C` and `O` as "independent posits / two
  unconnected foundations"). It is a **refinement** to coexistence-as-island: the through-line
  survives (§3.7). The original `claim.md` PAUSE-condition-2 framing — "obstruction `=>` `C`
  and `O` independent posits" — is **superseded** by coexistence-as-island for the **embedding
  clause** (Bryan 2026-05-24); a clean (O) is a **valid deliverable**, surfaced for human
  decision, not a fraudulent force-pass and not a collapse.

### 3.7 The CORRECTED RESTRICTION (coexistence-as-island) — the governing frame

- **RESTRICTION needs only COEXISTENCE-AS-ISLAND.** The observer is a **self-certified
  `M_3(C)^sa` system on the slice** `A = h_3(C_u)` (Phase 61: all four Def 1 clauses
  **verbatim**, **intrinsically**), and the slice **sits inside `h_3(O)` as the range of the
  projection `E`**. It does **NOT** need the observer's structure **transported/derived from
  the ambient** via `E` (the prompt's original over-ask).

- **WEAKEN `RESTRICTION`'s EMBEDDING clause.** From

  > *"the observer's `V_BM` is realized **coherently** as a sub-structure of `h_3(O)` **induced
  > by the Peirce/bottleneck restriction `E`**"* (original `claim.md` RESTRICTION)

  to

  > *"the observer **self-models on the slice**, which **sits inside `h_3(O)` as the range of
  > the projection `E`**."* (CORRECTED, Bryan 2026-05-24)

  `E` is the **ACCESS / PROJECTION map**, **NOT** required to be a Jordan morphism on the
  ambient.

- **INTEGRITY — clause (iii) ITSELF is NOT weakened (`fp-redefine-iii`).** Clause (iii) stands
  **verbatim** (all four data — product states, product effects, non-signaling constraints,
  product-form sequential product — plus minimality), established **intrinsically** in Phase 61.
  **Only `RESTRICTION`'s embedding clause** is weakened. Weakening the embedding clause is
  **NOT** the same as weakening clause (iii); do **not** conflate the two.

- **INTEGRITY — `V_BM` not conflated with the ambient (`fp-conflate-composites`).** `V_BM`
  remains the observer's **OWN** internal composite `A (x) A ~ M_9(C)^sa`, **never** identified
  with / transported from the BGW universe-tensoring `(x)~` of `h_3(O)`. Coexistence-as-island
  is **FULLY CONSISTENT** with the Phase 60 two-composites distinction: **the island has its
  own composite; the basin fixes the TYPE `M_3(C)^sa`, not the composite.** (Consistent with
  U-B-M: Peirce `!=` tensor; the basin fixes TYPE.)

- **THE THROUGH-LINE SURVIVES under (O).** Even if `E` does **not** transport the sequential
  product (`R != 0`), the through-line survives as:

  > *`h_3(O)` is the basin whose maximal C* slice is `M_3(C)^sa`, on which Paper 5 certifies
  > the observer's QM; `E` is the access/projection map.*

  An obstruction (O) does **NOT** establish "independent posits / two unconnected
  foundations"; it **REFINES** the claim to a **self-contained C* island**. (P) gives the
  stronger "induced from the ambient" through-line; (O) gives the island through-line. Both are
  coherent; the fork chooses **which** through-line, not **whether** there is one.

### 3.8 Type/category + Peirce self-audit for §3

| Load-bearing object / claim | Subject category | Type-correct? |
|---|---|---|
| sequential product `a & b = sqrt(a) b sqrt(a)` | **CFC triple product on effects** (NOT a Jordan op) | ✓ (never treated as a Jordan-algebra op) |
| decisive object `R = E(sqrt(X) Y sqrt(X)) - sqrt(EX)(EY)sqrt(EX)` | residual in `h_3(O)` for **generic ambient** `X,Y` | ✓ (generic ambient, non-associativity load-bearing) |
| slice-internal `sqrt(a) b sqrt(a)` (`a,b in A`) | **TRIVIAL control** (closed associative subalgebra) | ✓ (leakage 0, associator 0; tagged control, not decisive) |
| `E : h_3(O) -> A` | **access / projection map** (positive unital idempotent) | ✓ (NOT a Jordan morphism on the ambient — §2.2) |
| clause (iii) | OUS composite datum, **verbatim** | ✓ (NOT weakened; only the embedding clause weakened) |
| `V_BM = A (x) A` | observer's OWN OUS self-composite | ✓ (NOT conflated with BGW `(x)~` on `h_3(O)`) |
| obstruction-or-preservation fork | verdict semantics | ✓ (OPEN; (O) EXPECTED + a refinement to island, NOT collapse) |
| v11.0/Phase 42 precedent | historically adjacent (Clifford pairs) | ✓ (DROPPED as a prior — different mechanism) |

**Forbidden proxies — all REJECTED in §3:** `fp-assert-preservation` (decisive object framed
as the **open** ambient transport residual, deferred to 62-02; §3.1, §3.3, §2.3);
`fp-ignore-nonassociativity` (slice-internal triviality recorded as the **control**; decisive
test is ambient with non-associativity load-bearing on the **same** `X,Y`; both loopholes
foreclosed; §3.2, §3.3); `fp-redefine-iii` (clause (iii) verbatim; only the embedding clause
weakened; §3.7); `fp-conflate-composites` (`V_BM = A (x) A` not conflated with the ambient;
§3.7); `fp-force-positive` (fork OPEN; (O) expected but verdict decided by 62-02; v11.0
precedent dropped; §3.5, §3.6).

**[CONFIDENCE: HIGH]** that the crux is **correctly framed** as ambient `E`-transport
(`R = E(sqrt(X) Y sqrt(X)) - sqrt(EX)(EY)sqrt(EX)` for generic `X,Y`, non-associativity
load-bearing), that the **slice-internal triviality** is correctly recorded as the control
(closed associative subalgebra `=>` leakage 0, associator 0), that the **corrected
`RESTRICTION`** (coexistence-as-island) is stated with clause (iii) integrity and the
two-composites distinction preserved, and that the decisive question is **well-posed for exact
computation** in 62-02. **[CONFIDENCE: explicitly UNRESOLVED — the VERDICT]:** whether `R = 0`
(P) or `R != 0` (O) is **NOT** decided here; it is computed in 62-02 and read off in 62-03. The
setup pre-commits to **neither** branch.

---

## 4. The decisive exact computation — AMBIENT E-transport on the non-associative h_3(O) (62-02, VALD-62-01)

This section records the **decisive exact-arithmetic computation** of the §3.3 spec and reads
off the verdict on the obstruction-or-preservation fork (§3.6). It implements §3.3–§3.4 in
**exact SymPy** in `code/embedding_under_E_verification.py` with an **assert-based** harness
`tests/test_embedding_under_E.py` (NO pytest; runnable as `python tests/test_embedding_under_E.py`,
exits 0 on self-check success). **All self-checks PASS; the decisive verdict is (O), an
AMBIENT-TRANSPORT OBSTRUCTION** — the EXPECTED, acceptable outcome that **refines** `RESTRICTION`
to coexistence-as-island (§3.7), handed to 62-03.

### 4.1 The decisive question, recapped

For **GENERIC ambient** `X >= 0` (PSD, so `sqrt(X)` exists in the ambient) and `Y = Y^dagger in
h_3(O)`, with `sqrt(X)` computed **in the non-associative ambient** and the relevant associator
verified **exactly nonzero** (non-associativity load-bearing), is

$$
R \;:=\; E\big(\sqrt{X}\,Y\,\sqrt{X}\big) \;-\; \sqrt{EX}\,(EY)\,\sqrt{EX} \;\overset{?}{=}\; 0
\qquad(\text{exact}),
$$

where `sqrt(EX)` is the **slice** (associative `M_3(C)`) square root of the projected `EX in A`.
`R == 0` (exact) `=>` coherent transport **(P)**; `R != 0` (exact) `=>` ambient-transport
obstruction **(O)**.

### 4.2 What was computed (cite: `code/embedding_under_E_verification.py`, `tests/test_embedding_under_E.py`)

All arithmetic is **exact SymPy** (rationals/surds); the decisive equality test is
`octmat_is_zero(R)` (per-component `simplify(...) == 0`), **never a float tolerance**
(`fp-float-pass` rejected). h_3(O) elements are carried as **full 3×3 octonionic matrices**
(`oct_mul` via the Fano table `e_1 e_2 = e_4`), so the **triple matrix product is NOT assumed
associative**: `(XY)Z` and `X(YZ)` are computed by independent left/right association.

1. **`E` onto `h_3(C_u)` (entrywise `proj_u`, `u = e_7`) — verified EXACTLY:**
   - **unital** `E(I_3) = I_3`; **idempotent** `E(E(X)) = E(X)` (on a generic ambient `X` with
     nonzero `e_1..e_6` content — non-vacuous); `E|_A = id` (on a slice element); **entrywise
     `proj_u`** (off-diagonal `e_1..e_6` zeroed, `e_0, e_7` kept); **positive** on a non-diagonal
     PSD slice effect with **rational spectrum `{1, 3, 5}`** (`E(.)` PSD, exact eigenvalues
     `>= 0`); `dim(range E) = 9`, `dim(ker E) = 18`, `27 = 9 + 18`.
   - **`E` is NOT a Jordan morphism on the ambient** (the §2.2 non-triviality, now CONFIRMED
     exactly): for a generic ambient `X`,
     $$
     \big\|E(X\circ X) - (EX)\circ(EX)\big\|_F^2 \;=\; \tfrac{3797527}{34560000}\;\neq\;0
     \quad(\text{exact}).
     $$
     This is what makes the SP-transport question genuinely non-trivial.

2. **Ambient principal square root `sqrt_ambient(X)` — EXACT:** via the **exact-square trick**
   `X = C*C` with `C` an ambient PSD element of exact entries (confirmed PSD by its reduced
   characteristic-polynomial roots `>= 0`), so `sqrt(X) = C`. Self-check
   `h3o_matmul(sqrt_X, sqrt_X) == X` holds **exactly** in the ambient octonionic product. `X` is
   genuinely ambient (nonzero `e_1..e_6`).

3. **Non-associativity is LOAD-BEARING on the decisive data:** for the **same** decisive triple
   `(sqrt(X), Y, sqrt(X))` whose product is the decisive sequential product, the associator is
   **exactly nonzero**,
   $$
   \big\|(\sqrt{X}\,Y)\,\sqrt{X} - \sqrt{X}\,(Y\,\sqrt{X})\big\|_F^2 \;=\; \tfrac{524}{9}\;\neq\;0
   \quad(\text{exact}),
   $$
   so the test genuinely engages `(xy)z != x(yz)` (NOT an accidentally-associative corner;
   `fp-ignore-nonassociativity` rejected). The decisive `X, Y` are generic ambient, **not**
   slice-confined.

4. **THE DECISIVE AMBIENT-TRANSPORT residual** `R = E(sqrt(X) Y sqrt(X)) - sqrt(EX)(EY)sqrt(EX)`
   computed **exactly** for **two distinct generic `(X, Y)`** (each with the associator-nonzero
   precheck passing):
   - **pair 0:** `R != 0` exactly; `||R||_F^2 = 38593/72` (≈ 536). Representative exactly-nonzero
     entry: `R_{11} = -2` (the `e_0`/real diagonal component) — an `O(1)` rational, no surd, no
     cancellation ambiguity.
   - **pair 1:** `R != 0` exactly; `||R||_F^2 = 127725937/64800 - 13*sqrt(67134)/2 -
     277*sqrt(183513)/900` (≈ 155). Representative exactly-nonzero entry: `R_{11} = 1/6`.
   - In both pairs `is_zero_exact = False`; the harness asserts only the **honest consistency**
     `octmat_is_zero(R) <=> is_zero_exact` (it does **not** hardcode P or O).

5. **Slice-internal TRIVIAL control** (clearly separated, **NOT** the decisive test): for `a, b in
   A` (a PSD slice effect and a slice element with `C_u` off-diagonal content), the ambient-product
   `sqrt(a) b sqrt(a)` has **leakage EXACTLY 0** (`E(sqrt(a) b sqrt(a)) = sqrt(a) b sqrt(a)`, it
   stays in `A`) and triple associator **EXACTLY 0** (`A` is a closed associative subalgebra =
   range `E`). This reconfirms Phase 61's intrinsic triviality and forecloses both reward-hack
   loopholes (the trivial-residual-as-decisive move and the unrelated-matrices line-loophole).

6. **Independent Peirce/grade-component cross-check** (a genuinely **second route**): decomposing
   the defect `D = E(sqrt(X) Y sqrt(X)) - sqrt(EX)(EY)sqrt(EX)` into its `C_u`-vs-`(e_1..e_6)`
   components **and** into Peirce grades `V_1/V_{1/2}/V_0` at `E_11`, the verdict **AGREES** with
   the direct residual on **both** pairs (both routes: defect **nonzero**). The code **RAISES** on a
   split decision; none occurred.

### 4.3 THE VERDICT — (O) AMBIENT-TRANSPORT OBSTRUCTION (stated exactly as computed; NOT forced)

> **`E` does NOT transport the self-modeling sequential product coherently from the
> non-associative ambient `h_3(O)`.** The ambient-transport residual
> `R = E(sqrt(X) Y sqrt(X)) - sqrt(EX)(EY)sqrt(EX)` is **EXACTLY nonzero** for generic ambient
> `X, Y` (non-associativity load-bearing, associator `= 524/9 != 0`), with the direct-residual and
> the independent Peirce/grade routes **agreeing**. **Branch (O).**

**Characterization of the defect (handed to 62-03).** For the first (clean-rational) pair, the
exact residual `R` populates **only the `C_u` directions** (octonion components `e_0` and `e_7`)
of the matrix entries: the all-entry split gives `C_u`-part`^2 = 38593/72` and
`(e_1..e_6)`-part`^2 = 0`, summing to `||R||_F^2 = 38593/72`. So `R` is a genuine **slice element**
(both `E(sqrt(X) Y sqrt(X))` and `sqrt(EX)(EY)sqrt(EX)` lie in `A`, since `E` projects every entry
onto `C_u`), and the obstruction is the **failure of the two slice elements to coincide**, NOT
leakage out of `A`. Across the **positional** Peirce grades at `E_11` (which partition the 9 matrix
entries, so the grade magnitudes sum exactly to `||R||_F^2`):

$$
\|V_1(R)\|^2 = 4,\qquad \|V_{1/2}(R)\|^2 = \tfrac{1033}{18},\qquad \|V_0(R)\|^2 = \tfrac{3797}{8},
\qquad 4 + \tfrac{1033}{18} + \tfrac{3797}{8} = \tfrac{38593}{72},
$$

so the defect is **spread across all three Peirce grades** (dominantly `V_0`, the
`h_2(C_u)`-block, then `V_{1/2}`, then a nonzero `V_1` scalar bottleneck component). Mechanism
(§3.5): the ambient `sqrt(X) Y sqrt(X)` populates `(e_1..e_6)` components that `E` then projects
away; equivalently, `E` applied **after** the ambient triple product retains contributions from
the killed directions that `sqrt(EX)(EY)sqrt(EX)` (built entirely inside `A`) never sees. The
two slice elements therefore differ in their `C_u` components — an `O(1)` defect.

> **Non-Hermiticity finding (sharpens the obstruction).** A by-product of the exact computation:
> the ambient sequential product `sqrt(X) Y sqrt(X)` is itself **NOT Hermitian** in the
> non-associative `h_3(O)` — the would-be involution identity `(\sqrt{X}\,Y\,\sqrt{X})^\dagger =
> \sqrt{X}\,Y\,\sqrt{X}` **fails** because `(AB)C \neq A(BC)`. The natural **left** association
> `(\sqrt{X}\,Y)\,\sqrt{X}` leaves the formally-real Jordan cone. (We use the left association
> throughout; the obstruction holds for it, and would for any fixed association — the SP is
> association-dependent in the ambient.) Consequently the defect `R` is a **non-Hermitian** `3×3`
> octonionic matrix; we therefore characterize it with the **positional** `E_11` Peirce grading and
> an all-entry `C_u`/`(e_1..e_6)` split (faithful for non-Hermitian matrices), **not** a Hermitian-
> coordinate reconstruction. This is an *additional* way `E` fails to transport the SP coherently —
> on top of `R \neq 0`, the ambient SP is not even Hermitian — and it reinforces (O).

**Status of (O): EXPECTED, ACCEPTABLE, a REFINEMENT — not a collapse.** Per §3.6–§3.7, (O)
**refines** `RESTRICTION` to **coexistence-as-island**: the observer self-certifies its
`M_3(C)^sa` QM **on the slice** (Phase 61, all four Def 1 clauses verbatim, intrinsically), and
the slice **sits inside `h_3(O)` as the range of the projection `E`**; `E` is the
**access/projection map**, **not** required to be a Jordan morphism (it is not — §2.2/4.2(1)) nor
an SP-morphism (it is not — this section) on the ambient. The through-line survives as the island
through-line. (O) does **NOT** establish "independent posits / two unconnected foundations" and is
**NOT** a program collapse; it is a clean, valid deliverable, surfaced for the 62-03 read-off and
the Phase 63 milestone verdict. The original `claim.md` PAUSE-condition-2 framing is **superseded**
by coexistence-as-island for the embedding clause (Bryan 2026-05-24).

> **`fp-force-positive` NOT triggered.** The verdict is whatever the exact computation yields. No
> `X, Y` were cherry-picked to force `R = 0`; the exact test was never relaxed; the obstruction is
> reported honestly. The **v11.0/Phase 42** precedent (`sqrt(T_a) T_b sqrt(T_a) = (i/2) T_b` exits
> `M_16(R)`) is **NOT** carried as evidence — it is a **different mechanism** (Clifford
> non-commuting pairs in a fixed matrix algebra, not the `h_3(O) -> h_3(C_u)` projection
> restriction); it is noted only as historical context.

### 4.4 Why the verdict is trustworthy

- **Two independent routes agree.** The direct ambient residual and the Peirce/grade-component
  decomposition reach the **same** verdict (O) on **both** generic pairs; the code raises on a
  split decision and none occurred.
- **EXACT arithmetic, zero tolerance.** `R != 0` means **exactly** nonzero (e.g. `R_{11} = -2`, a
  rational with no surd) — a **genuine** ambient-transport obstruction, **not** float round-off
  (`fp-float-pass` rejected). The exact-square trick `X = C*C` is documented and **confirmed not to
  trivialize non-associativity** (the associator `= 524/9 != 0` on the same `X, Y`).
- **Non-associativity is load-bearing on the decisive data**, and the slice-internal triviality is
  recorded as the **control**, not the decisive test (`fp-ignore-nonassociativity` rejected).
- **The decisive object is the actual self-modeling SP** `sqrt(X) Y sqrt(X)` (not the Jordan
  product or a surrogate; `fp-redefine-iii` rejected); **clause (iii) itself is unchanged** (only
  `RESTRICTION`'s embedding clause is weakened, in §3.7 / 62-03).
- **The computation is on the genuinely non-associative ambient for GENERIC `X, Y`**, not the
  trivial slice (`fp-assert-preservation` rejected).
- **Self-checks pass:** `E` properties (incl. not-a-Jordan-morphism-on-ambient), ambient
  `sqrt^2 == X`, associator nonzero on the decisive data, slice-internal control trivial; the
  harness exits 0.

> **Reproducibility.** SymPy 1.14.0, Python 3.14.2, macOS Darwin 24.6.0. Deterministic (no random
> seeds; all test elements hardcoded with exact rational/surd entries). Re-running the harness
> reproduces `is_zero_exact = [False, False]` and the verdict (O) identically.

### 4.5 Handoff to 62-03

The decisive input to 62-03 is: **branch (O)** — an exact ambient-transport obstruction — with the
**characterized defect** (lands in the `C_u` directions `e_0, e_7`; positional `E_11` Peirce-grade
magnitudes `||V_1||^2 = 4`, `||V_{1/2}||^2 = 1033/18`, `||V_0||^2 = 3797/8`, summing to
`||R||_F^2 = 38593/72`; representative entry `R_{11} = -2`; the ambient SP is non-Hermitian under
non-associativity) on the clean pair. 62-03 reads (O) as a **refinement** of
`RESTRICTION` to coexistence-as-island (§3.7): it states the precise obstruction (the structure
`E` cannot transport — the ambient SP's `(e_1..e_6)` content that does not survive projection), the
**minimal extra input** (the observer does not need transport — it self-models on the slice, which
sits inside `h_3(O)` as `range E`), and carries the verdict to the Phase 63 milestone read-off. The
§5 marker below is updated accordingly.

### 4.6 Type/category + Peirce self-audit for §4

| Load-bearing object / claim | Subject category | Type-correct? |
|---|---|---|
| decisive residual `R = E(sqrt(X) Y sqrt(X)) - sqrt(EX)(EY)sqrt(EX)` | residual in `h_3(O)` for **generic ambient** `X,Y` | ✓ (generic ambient; associator `= 524/9 != 0` load-bearing) |
| ambient sequential product `sqrt(X) Y sqrt(X)` | **CFC triple product on effects** (NOT a Jordan op) | ✓ (triple product, left/right associations computed independently) |
| `sqrt(X)` (ambient) vs `sqrt(EX)` (slice) | ambient principal root vs `M_3(C)` root in `A` | ✓ (exact-square trick ambient; spectral root in associative slice) |
| defect `R` (verdict O) | exactly nonzero; populates `C_u` (`e_0,e_7`); Peirce grades `V_1,V_{1/2},V_0` | ✓ (tagged by grade / `e_k`; characterized, not asserted away) |
| slice-internal `sqrt(a) b sqrt(a)` (`a,b in A`) | **TRIVIAL control** (closed associative subalgebra) | ✓ (leakage 0, associator 0; tagged control, not decisive) |
| `E : h_3(O) -> A` | **access / projection map** (positive unital idempotent) | ✓ (NOT a Jordan morphism on the ambient: `||E(XoX)-(EX)o(EX)||^2 = 3797527/34560000 != 0`) |
| verdict (O) | ambient-transport obstruction | ✓ (EXPECTED; refines `RESTRICTION` to island; NOT forced, NOT a collapse) |
| v11.0/Phase 42 precedent | historically adjacent (Clifford pairs) | ✓ (NOT carried as evidence — different mechanism) |

**Forbidden proxies — all REJECTED in §4:** `fp-assert-preservation` (computed on the genuinely
non-associative ambient for generic `X,Y`, not the trivial slice or a hand-wave);
`fp-ignore-nonassociativity` (associator `= 524/9 != 0` load-bearing on the **same** decisive
`X,Y`; slice-internal recorded as control); `fp-float-pass` (exact SymPy equality on the verdict;
no float64 anywhere on the decisive path); `fp-force-positive` (verdict (O) reported honestly; no
cherry-picking; exact test not relaxed; v11.0 dropped as a prior); `fp-redefine-iii` (actual SP
`sqrt(X) Y sqrt(X)`; clause (iii) unchanged).

**[CONFIDENCE: HIGH]** that the decisive computation is **correct and the verdict is (O)**: all
self-checks pass exactly; the two independent routes (direct residual; Peirce/grade-component)
agree on (O) for two distinct generic pairs; non-associativity is load-bearing (associator
`= 524/9 != 0`) on the same data; the residual is exactly nonzero with `O(1)` rational entries
(e.g. `R_{11} = -2`), excluding float round-off and accidental cancellation; the slice-internal
control is trivial (leakage 0) as expected. **Generality caveat (carry to 62-03):** **one** exact
nonzero residual on non-associativity-load-bearing generic data **suffices** to establish the
obstruction (O) — and we have **two** — so (O) is established rigorously. The complementary
statement "no generic `X,Y` ever gives `R = 0`" is not needed for (O) and is not claimed; the
obstruction is the existence of generic `X,Y` with `R != 0`, which is proven. (A hypothetical (P)
would have required a general argument, not just representatives — but (P) did not occur.)

## 5. The verdict on the fork — (O) AMBIENT-TRANSPORT OBSTRUCTION, refining RESTRICTION to coexistence-as-island (62-03)

This section reads the verdict off §4's exact computation (the obstruction-or-preservation fork of
§3.6) and interprets it. Per the CORRECTED framing (§3.7, Bryan 2026-05-24), the verdict is a
**refinement of `RESTRICTION` either way** (coexistence-as-island); the actual branch, decided by
§4, is **(O)**.

### 5.1 The verdict, read off §4

§4 computed the decisive **ambient-transport residual** of §3.3,

$$
R \;:=\; E\big(\sqrt{X}\,Y\,\sqrt{X}\big) \;-\; \sqrt{EX}\,(EY)\,\sqrt{EX},
$$

**exactly** (SymPy, zero-tolerance) for **two distinct generic ambient** `(X, Y)` (off-diagonal
octonion entries with nonzero `(e_1,...,e_6)`-parts; `sqrt(X)` taken **in the non-associative
ambient** via the exact-square trick `X = C*C`). The result was

$$
\boxed{\;R \;\neq\; 0 \quad(\text{exact}),\qquad \text{is\_zero\_exact} = [\text{False}, \text{False}],\;}
$$

with `||R||_F^2 = 38593/72` on the clean rational pair (representative exactly-nonzero entry
`R_{11} = -2`). Per the §3.6 fork (exact `R != 0` `=>` branch **(O)**), **the computation took
branch (O): the AMBIENT-TRANSPORT OBSTRUCTION.** This §5 verdict is therefore **(O)**, and it
**equals** §4's computed verdict — there is **no §4/§5 divergence** (the verdict follows the exact
computation, as mandated). The verdict is grounded in the **genuinely non-associative** ambient: on
the **same** decisive `(X, Y)` whose residual is `R`, the associator of the triple `(sqrt(X), Y,
sqrt(X))` is `||·||^2 = 524/9 != 0` (exact) — non-associativity is **load-bearing**, not an
accidentally-associative corner. The independent positional-Peirce/grade-component route **agreed**
with the direct residual on both pairs (the harness raises on a split; none occurred).

### 5.2 The governing frame (coexistence-as-island), stated BEFORE the branch

`RESTRICTION` needs **only** that the observer **self-models on the slice** `A = h_3(C_u) ~
M_3(C)^sa` (Phase 61, `slice-clause-iii.md` §5: all four Paper 5 Def 1 clauses verbatim,
**intrinsically**) and that the slice **sits inside `h_3(O)` as the range of the projection `E`**.
Whether `E` **transports** the sequential product from the ambient is a **STRONGER, NOT-REQUIRED**
property; the verdict on it **refines** `RESTRICTION` **either way** (§3.7). `E` is the
**access/projection map**, **not** required to be a Jordan morphism on the ambient (it is not —
§2.2/§4.2(1)) nor an SP-morphism on the ambient (it is not — §4.3). So branch (O) — `E` fails to
transport the SP — does **not** threaten `RESTRICTION`; it **sharpens** it to the island form.

> The branch below is the one §4 supports. The complementary branch (P) — coherent transport, a
> `RESTRICTION` **embedding lemma** — **did NOT obtain** (`R` is exactly nonzero on
> non-associativity-load-bearing generic data), and is **not** asserted. The governing frame (5.2)
> holds regardless of branch.

---

### BRANCH (O): AMBIENT-TRANSPORT OBSTRUCTION — precise characterization + minimal extra input, REFINES RESTRICTION

#### 5.O.1 Characterization of the obstruction (precise; from §4's exact residual)

**(a) The exact structure `E` cannot transport: the product-form sequential-product datum from the
ambient.** `E` is a **Jordan conditional expectation on the slice** (positive, unital, idempotent;
`E|_A = id`; Jordan-product-preserving embedding `A hookrightarrow h_3(O)` — §1.3/§2.1), but it is
**NOT a Jordan morphism on the ambient** (`||E(X o X) - (EX) o (EX)||_F^2 = 3797527/34560000 != 0`,
§4.2(1)). A fortiori it does **NOT transport the sequential product** `a & b = sqrt(a) b sqrt(a)`
(clause (iii)'s fourth datum, the actual product-form SP — `fp-redefine-iii` rejected, §4.4)
coherently from the ambient: for generic ambient `X, Y`,

$$
E\big(\sqrt{X}\,Y\,\sqrt{X}\big) \;\neq\; \sqrt{EX}\,(EY)\,\sqrt{EX}
\qquad(\text{exact},\ R \neq 0).
$$

The two slice elements `E(sqrt(X) Y sqrt(X))` and `sqrt(EX)(EY)sqrt(EX)` **fail to coincide**: the
obstruction is **not** leakage out of `A` (both lie in `A`, since `E` projects every entry onto
`C_u`), but the **failure of the two `A`-elements to agree**.

**(b) WHY (the mechanism): non-associativity, with the defect localized.** The defect is a genuine
**non-associativity effect** (exact, not round-off — `R_{11} = -2` is a rational with no surd). Its
location, from §4's exact residual (clean pair):

- **All-entry `C_u`-vs-`(e_1,...,e_6)` split:** `R` lands **entirely in the `C_u` directions**
  (`e_0, e_7`): `C_u`-part`^2 = 38593/72`, `(e_1,...,e_6)`-part`^2 = 0`. So `R` is a genuine **slice
  element** — the obstruction lives **inside `A`**, as the gap between the two slice elements.
- **Positional `E_11` Peirce grades** (faithful for the non-Hermitian defect; they partition the
  nine matrix entries, so the grade magnitudes sum exactly to `||R||_F^2`):

$$
\|V_1(R)\|^2 = 4,\qquad \|V_{1/2}(R)\|^2 = \tfrac{1033}{18},\qquad \|V_0(R)\|^2 = \tfrac{3797}{8},
\qquad 4 + \tfrac{1033}{18} + \tfrac{3797}{8} = \tfrac{38593}{72}.
$$

  The defect is **spread across all three Peirce grades** — dominantly `V_0` (the
  `h_2(C_u) ~ M_2(C)^sa` block), then `V_{1/2}` (the `C_u^2` interface), with a **nonzero `V_1`
  scalar bottleneck component** `||V_1(R)||^2 = 4`. Mechanism (§3.5/§4.3): the ambient `sqrt(X) Y
  sqrt(X)` populates `(e_1,...,e_6)`-components that `E` then projects away; `E` applied **after**
  the ambient triple product retains contributions from the killed directions that
  `sqrt(EX)(EY)sqrt(EX)` (built entirely inside `A`) never sees, so the two `C_u`-images differ.
- **Sharpening (non-Hermiticity, §4.3).** As an additional, association-dependent failure: the
  ambient SP `sqrt(X) Y sqrt(X)` is itself **NOT Hermitian** in `h_3(O)` (the would-be involution
  identity fails because `(AB)C != A(BC)`). This is a *further* way `E` cannot coherently transport
  the SP, on top of `R != 0`.

**(c) The MINIMAL EXTRA INPUT that ambient transport would require.** Ambient transport (the
**stronger, NOT-required** property) would need the SP's `(e_1,...,e_6)`-content — the part of
`sqrt(X) Y sqrt(X)` that does **not** survive the projection `E` — to be recoverable from the
slice data alone. It is not: `E` discards exactly those directions (`ker E`, real-dim 18), and the
exact residual confirms the discarded content changes the `C_u`-image. In **Hanche-Olsen
induced-vs-imported** terms: `E` does **not INDUCE** the sequential-product datum from `h_3(O)`;
ambient transport would require **IMPORTING** structure — an external datum on `h_3(O)` **not in
the range of `E`** (concretely, a rule fixing how the killed `(e_1,...,e_6)`-content feeds back into
the `C_u`-image; no such rule is supplied by `E`, and §4 shows the naive "project and compute in
`A`" route disagrees with "compute in the ambient and project").

> **NOTE — coexistence-as-island does NOT require this extra input at all.** The observer already
> **self-models on the slice** (Phase 61), which **sits inside `h_3(O)` as `range E``. The minimal
> extra input is **only** what AMBIENT TRANSPORT (the stronger property) would need; the
> island claim needs none of it. (This is the weakest-anchor item, §5.5: stated as precisely as the
> evidence allows, not overstated — `fp-force-positive`/over-claim guard.)

#### 5.O.2 The REFINEMENT (replaces the old PAUSE-2-collapse framing)

The ambient-transport obstruction (O) **REFINES `RESTRICTION` to COEXISTENCE-AS-ISLAND**:

- The observer is a **self-contained C\* island**: it self-certifies its `M_3(C)^sa` QM **on the
  slice** `A = h_3(C_u)` (Phase 61, all four Def 1 clauses verbatim, intrinsically), and the slice
  **sits inside `h_3(O)` as the range of the projection `E`**.
- **The through-line SURVIVES** as the **island through-line**:

  > `h_3(O)` is the **basin** whose **maximal C\* slice** is `M_3(C)^sa`, on which **Paper 5
  > certifies** the observer's QM; `E` is the **access/projection map**.

  `E` is **not** required to be a Jordan morphism (it is not) nor an SP-morphism (it is not) on the
  ambient. The basin **fixes the TYPE** `M_3(C)^sa`; it does **not** transport the observer's
  structure.
- **Consistent with U-B-M:** Peirce `!=` tensor; the basin fixes the TYPE, not the composite. The
  observer's own composite `V_BM = A (x) A ~ M_9(C)^sa` is **never** identified with the BGW
  universe-tensoring `(x)~` of `h_3(O)` (`fp-conflate-composites` preserved — §3.7, §5.4).

This is the **EXPECTED, ACCEPTABLE** outcome and a **valid DELIVERABLE.** It does **NOT** establish
"**independent posits / two unconnected foundations**" and is **NOT** a program-collapse PAUSE. The
original `claim.md` **PAUSE condition 2** framing — "obstruction `=>` `C` and `O` independent
posits, PAUSE" — is **superseded by coexistence-as-island for the embedding clause** (Bryan
2026-05-24); see the `claim.md` update (Task 1b / `deliv-claim-md`). Only a genuinely **unexpected**
pathology (e.g. the slice-internal control failing, or the slice not being a closed associative
subalgebra, or the two-composites distinction collapsing) would be a true PAUSE — and none occurred
(the slice-internal control is trivial as expected, §4.2(5): leakage 0, associator 0).

#### 5.O.3 Program consequence (this branch)

Under (O), the **through-line survives as coexistence-as-island** with a **precisely-located
ambient-transport obstruction** (the SP's `(e_1,...,e_6)`-content that `E` cannot transport; defect
inside `A`, spread across all three `E_11` Peirce grades, `||R||_F^2 = 38593/72`; ambient SP
non-Hermitian). The **MILESTONE-level `RESTRICTION` verdict is FINALIZED in Phase 63** (which reads
this step's outcome + runs the adversarial guard review); it is **NOT** declared here
(`fp-overclaim-milestone` — the milestone verdict stays **UNDECIDED**).

**Respect the asymmetry (project memory: basin-only vs observer+basin).** This (O) concerns **only**
whether the observer's complex structure is **TRANSPORTED by `E` from the non-associative basin** —
the stronger, now-not-required property. It does **NOT** downgrade Paper 7's separate
complexification claim, nor Paper 5's / Phase 61's **intrinsic** result (the slice satisfies clause
(iii) in its own right). The obstruction is characterized at **exactly that join** (ambient
`E`-transport of the SP) and is **not** over-generalized into "independent posits."

> **The verdict is NOT forced (`fp-force-positive`, both directions).** It equals §4's exact
> computation. Coherent transport was **not** manufactured (no `X, Y` cherry-picked to force `R =
> 0`; the exact test was never relaxed — had `R` been exactly 0 with both routes agreeing, the
> verdict would have been (P), a `RESTRICTION` embedding lemma; it was not). And (O) is **not**
> over-stated as a refutation/collapse — it is reported as the expected coexistence-as-island
> refinement. The **v11.0/Phase 42** precedent (`sqrt(T_a) T_b sqrt(T_a) = (i/2) T_b` exits
> `M_16(R)`) is noted **only as historical context** — a **different mechanism** (Clifford
> non-commuting pairs in a fixed matrix algebra, **not** the `h_3(O) -> h_3(C_u)` projection
> restriction at issue) — and is **NOT** carried as evidence for (O).

---

### 5.4 Type/category + Peirce self-audit for §5

| Load-bearing object / claim | Subject category | Type-correct? |
|---|---|---|
| §5 verdict | branch tag **(O)**, `= §4` computed verdict | ✓ (no §4/§5 divergence; reads off the exact residual) |
| obstruction (O) | ambient-transport obstruction localized in `A` (Peirce grades / `C_u`) | ✓ (named: `V_1/V_{1/2}/V_0` grades sum to `||R||^2`; `C_u` directions `e_0,e_7`) |
| sequential product `a & b = sqrt(a) b sqrt(a)` | **CFC triple product on effects** (NOT a Jordan op) | ✓ (the actual SP; clause (iii) datum 4) |
| `E : h_3(O) -> A` | **access/projection map** (positive unital idempotent) | ✓ (NOT a Jordan morphism nor SP-morphism on the ambient) |
| clause (iii) | OUS composite datum, **verbatim** | ✓ (UNCHANGED — only `RESTRICTION`'s embedding clause is weakened, Task 1b) |
| `V_BM = A (x) A ~ M_9(C)^sa` | observer's OWN OUS self-composite | ✓ (NOT conflated with BGW `(x)~` on `h_3(O)`) |
| (O) semantics | refinement to coexistence-as-island | ✓ (EXPECTED + acceptable DELIVERABLE; NOT independent posits, NOT a collapse PAUSE) |
| milestone verdict | `RESTRICTION` milestone | ✓ (UNDECIDED — left to Phase 63) |
| v11.0/Phase 42 precedent | historically adjacent (Clifford pairs) | ✓ (NOT carried as evidence — different mechanism) |

**Forbidden proxies — all REJECTED in §5:** `fp-assert-preservation` (the verdict reads off §4's
**ambient** transport residual on **generic** `X,Y` with the associator `= 524/9 != 0` load-bearing,
**not** the trivial slice-internal control); `fp-ignore-nonassociativity` (non-associativity
load-bearing on the **same** decisive `X,Y`; slice-internal recorded as the control in §4.2(5));
`fp-force-positive` (verdict (O) honest, equals the exact computation; not forced to (P), not
over-stated as a collapse; v11.0 dropped as a prior); `fp-redefine-iii` (the actual product-form SP
`sqrt(X) Y sqrt(X)`; clause (iii) **unchanged** — only `RESTRICTION`'s embedding clause weakened,
Task 1b); `fp-conflate-composites` (`V_BM = A (x) A` not conflated with the ambient);
`fp-overclaim-milestone` (milestone verdict UNDECIDED, Phase 63).

### 5.5 Confidence

**[CONFIDENCE: HIGH]** that the verdict is **(O)** and **matches the exact 62-02 computation**: the
two independent routes (direct exact residual; positional-Peirce/grade-component) **agree** on (O)
for two distinct generic pairs; non-associativity is load-bearing (associator `= 524/9 != 0`) on the
**same** data; the residual is exactly nonzero with `O(1)` rational entries (`R_{11} = -2`),
excluding float round-off and accidental cancellation; the slice-internal control is trivial as
expected (leakage 0, associator 0). **Generality caveat (inherited from §4.6):** **one** exact
nonzero residual on non-associativity-load-bearing generic data **suffices** to establish (O) — and
there are **two** — so the obstruction is established rigorously; the complementary statement "no
generic `X,Y` ever gives `R = 0`" is **not** needed for (O) and is **not** claimed. **Minimal-extra-input
caveat (5.O.1c):** the precise minimal extra input that ambient transport would require is the
least-certain part — stated as precisely as the evidence allows (an external datum on `h_3(O)` not
in `range E`, via Hanche-Olsen induced-vs-imported), and flagged as a Phase-63 / future-work item;
**NOTE coexistence-as-island does not require it at all** (the observer self-models on the slice).
The **milestone verdict** is **UNDECIDED** (Phase 63).

---

_Plan: 62-03 (Phase 62, milestone v15.0) — DERV-62-03. §5 (VERDICT)._
_§0–§3 = 62-01 (SETUP + CRUX FRAMING); §4 = 62-02 (DECISIVE COMPUTATION, verdict (O)); §5 = 62-03 (the verdict read-off + interpretation as coexistence-as-island refinement)._
