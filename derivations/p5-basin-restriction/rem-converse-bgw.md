<!-- ASSERT_CONVENTION: metric_signature=riemannian_fisher, fourier_convention=na, natural_units=natural, gauge_choice=na, renormalization_scheme=na -->
<!-- Pure-algebra / literature-grounding document. No numerics. The "dimensional-analysis" requirement maps to TYPE/CATEGORY consistency + OUS dimension bookkeeping. -->
<!-- Provenance: LIVE papers only (~/repos/blog/landing/papers/). NOT the stale repo papers/. BGW = arXiv:1606.09331v3 = Quantum 4, 359 (2020). -->

# rem:converse, grounded against BGW 2020

**Plan:** 60-02 (Phase 60, milestone v15.0) — DERV-60-03
**Purpose:** Confirm (or correct) Paper 7's `rem:converse` against the **literature**
(Barnum–Graydon–Wilce 2020; Hanche-Olsen), not by re-asserting the prompt. Establish the
**existence** side of the two-composites distinction: every `M_n(C)^sa` admits a faithful
self-model with composite `M_{n^2}(C)^sa`, and clause (iii) (`sms:minimal`) is satisfied
**as written** for complex matrix algebras. Locate the **exact** BGW statement bearing on
"minimal = maximal composite for `M_n(C)^sa`," record its scope, and flag that
`rem:converse` is **not yet** a labeled remark in the live `complexification.tex`.

**Verdict (this file):** `rem:converse` is **CONFIRMED-WITH-CAVEAT**.
- **CONFIRMED:** the existence of a faithful self-model of `M_n(C)^sa` with internal
  composite `M_{n^2}(C)^sa`, and **clause (iii) auto-satisfaction** for complex matrix
  algebras via the **minimal (standard / locally-tomographic) composite**. The existence
  side of the two-composites distinction **stands**.
- **CAVEAT:** `rem:converse`'s specific phrasing **"the minimal and maximal composites
  COINCIDE for `M_n(C)^sa`"** is **NOT** what BGW establishes. BGW show the **maximal
  (universal) composite is STRICTLY LARGER** — it carries an *extra classical bit*:
  `C_n ⊠̃ C_m = M_{nm}(C)^sa ⊕ M_{nm}(C)^sa`, twice the dimension of the minimal composite
  `M_{nm}(C)^sa`. So clause (iii) is satisfied because the **minimal** composite exists and
  is well-behaved (Theorem 4.15 / Corollary 4.16: it is an *ideal / direct summand* of the
  universal one), **not** because minimal and maximal coincide.

This is the honest-negative-aware outcome the milestone licenses: the existence /
clause-(iii) content of `rem:converse` is confirmed against BGW; the "coincide" wording is
the part BGW *complicates*, and it must be qualified with the extra-classical-bit fact.

---

## 0. Notation and category tags (type-consistency ledger)

The pure-math analog of dimensional analysis: **every named object carries one category
tag, and no inference equates objects of different tags.** "minimal = maximal" must be a
comparison of two **BGW-composites** (same category), never an OUS-vs-monoidal equation.

| Object | Category tag | BGW name | What it is |
|---|---|---|---|
| `M_n(C)^sa` | **FRJA (special, simple)** | `C_n` | self-adjoint complex `n×n` matrices; a complex quantum system |
| `V_B, V_M` | **OUS** | — | observer body / model order-unit spaces |
| `V_BM` | **OUS (composite)** | — | observer's *minimal internal* composite OUS (Paper 5 clause iii) |
| **minimal composite** of `M_n(C)^sa`, `M_m(C)^sa` | **FRJA (special, simple)** | standard composite `C_{nm}` (Table 1(c); Ex. 6.3) | `M_{nm}(C)^sa` — the *usual* QM tensor product; locally tomographic |
| **maximal composite** of `M_n(C)^sa`, `M_m(C)^sa` | **FRJA (special, NOT simple)** | universal tensor product `C_n ⊠̃ C_m` (Def. 3.8; Table 2) | `M_{nm}(C)^sa ⊕ M_{nm}(C)^sa` — extra classical bit; NOT locally tomographic |
| BGW composite bifunctor | **bifunctor / monoidal** | `⊠` / `⊠̃` | rule tensoring two FRJA systems |

> **Same-category check for "minimal = maximal."** Both the minimal composite
> (`M_{nm}(C)^sa`) and the maximal composite (`M_{nm}(C)^sa ⊕ M_{nm}(C)^sa`) are
> **FRJA-level composites** of the same pair. Comparing them is a *legitimate
> same-category comparison*. The comparison's **answer is "NOT equal"** (the maximal has
> twice the real dimension). This is type-correct; what fails is the *content* of the
> "coincide" claim, not the type of the claim.

Notation note (BGW): BGW write the composite of `A`, `B` as the juxtaposition `AB`, and the
universal (Hanche-Olsen) tensor product as `A ⊠̃ B` (`A\tilde\otimes B` in their LaTeX).
Their `C_n := M_n(C)_sa`, `R_n := M_n(R)_sa`, `Q_n := M_n(H)_sa`.

---

## 1. Faithful self-model of `M_n(C)^sa` (clause (i)/(ii) ingredients)

**State explicitly** (the self-model `rem:converse` instantiates):

- **`V_M = V_B = M_n(C)^sa`.** Both body and model OUS are the complex quantum system
  `M_n(C)^sa` (a finite-dimensional spectral OUS: the self-adjoint complex `n×n` matrices,
  with `≥ 2` orthogonal nontrivial projections for `n ≥ 2` — satisfying clause (i)
  `sms:finite`).
- **`phi = id : V_B -> V_M`.** The identity map is trivially an **order isomorphism**
  (faithful tracking), so clause (ii) `sms:faithful` holds. (Live Paper 5 clause (ii),
  `qm-from-self-modeling/main.tex` line 349, verbatim: *"`phi: V_B -> V_M` is an order
  isomorphism (faithful tracking)"*.)
- **Internal composite `V_BM`** of body and model: the minimal composite of `M_n(C)^sa`
  with `M_n(C)^sa`, namely the **standard complex-QM tensor product**
  `M_n(C)^sa ⊗ M_n(C)^sa ≅ M_{n^2}(C)^sa`.

**OUS dimension bookkeeping (dimensional-analysis analog).** Local tomography for the
*minimal* composite requires `dim(V_BM) = dim(V_B) · dim(V_M)` at the **state-space /
order-unit** level. For `M_n(C)^sa`: real vector-space dimension is `n^2`. The standard
composite `M_{n^2}(C)^sa` has real dimension `(n^2)^2 = n^4 = n^2 · n^2 = dim(V_B)·dim(V_M)`.
✓ **Consistent** — the minimal composite is exactly the local-tomography-respecting one.
(For `n = 3` — the slice of `lem:bottleneck` — `dim(M_3(C)^sa) = 9`, composite
`dim(M_9(C)^sa) = 81 = 9·9`. ✓)

**Contrast with the maximal composite** (anticipating §2): the universal tensor product
`C_n ⊠̃ C_n = M_{n^2}(C)^sa ⊕ M_{n^2}(C)^sa` has real dimension `2 n^4 ≠ n^4`. So the
maximal composite **violates** the product-dimension bookkeeping — the quantitative
signature of the "extra classical bit," and the reason it is **not** the clause-(iii)
object.

---

## 2. THE EXACT BGW STATEMENT (the load-bearing grounding)

`rem:converse` rests on a claim about how `M_n(C)^sa` composes. The exact BGW results are
the following (quoted verbatim from BGW 2020 = arXiv:1606.09331v3; page numbers are the
published Quantum pagination shown in the PDF).

### 2.1 The universal (maximal) tensor product — Definition 3.8 (p.20)

> **Definition 3.8.** The *universal* tensor product of two EJAs `A` and `B`, denoted
> `A ⊠̃ B`, is the Jordan subalgebra of `C^*(A) ⊗ C^*(B)` (the tensor product of `C^*(A)`
> and `C^*(B)` as finite-dimensional *-algebras) generated by `ψ_A(A) ⊗ ψ_B(B)`.

The universal `C^*`-algebra of `C_n = M_n(C)^sa` is **two copies** of `M_n(C)`
(Table 1(a), p.19, row `C_n`):

> `C^*(C_n) = M_n(C) ⊕ M_n(C)`, with canonical involution `Φ(a,b) = (b^T, a^T)`.

(BGW p.19: *"consider the embedding `M_n(C)_sa -> (M_n(C) ⊕ M_n(C))_sa` given by
`ψ(a) = (a, a^T)` ... Thus, `C^*(C_n) = M_n(C) ⊕ M_n(C)`."* The two summands are the
identity representation and the complex-conjugate / transpose representation. This is
exactly the structural fact the orchestrator flagged as a hypothesis — **CONFIRMED** from
Table 1(a).)

### 2.2 The universal tensor product of two complex systems — Table 2 (p.21)

BGW compute `A ⊠̃ B` for simple universally-reversible EJAs. **Table 2** (p.21), row `C_n`,
column `C_k`:

> `C_n ⊠̃ C_k = C_{nk} ⊕ C_{nk}`.

i.e. `M_n(C)^sa ⊠̃ M_k(C)^sa = M_{nk}(C)^sa ⊕ M_{nk}(C)^sa`. The **universal (maximal)
composite of two complex systems is two copies** of the standard one.

### 2.3 The decisive passage — Theorem 4.15 + Corollary 4.16 and its discussion (p.29)

> **Theorem 4.15.** Let `A` and `B` be simple, special EJAs. Then `AB` is an ideal in
> `A ⊠̃ B`.

> **Corollary 4.16.** Let `AB` be a composite of special EJAs `A` and `B`. Then `AB` is a
> direct summand of `A ⊠̃ B`.

And the discussion immediately following Corollary 4.16 is the **exact grounding** for
`rem:converse` (BGW p.29, verbatim):

> "Combined with Table 2, Theorem 4.15 sharply restricts the possibilities for composites
> of simple EJAs. In particular, it follows that *if `A ⊠̃ B` is itself simple,* then
> `AB ≃ A ⊠̃ B`. In other words, in this case the universal tensor product is the only
> "reasonable" tensor product ... **If `A = B = C_n`, so that
> `A ⊠̃ B = M_{n^2}(C)_sa ⊕ M_{n^2}(C)_sa`, we have another candidate, i.e., the usual
> quantum-mechanical composite `M_{n^2}(C)_sa`.** ... These exhaust the possibilities for
> composites of simple real, complex and quaternionic quantum systems!"

**Reading this at the level of `rem:converse`:**

- For `A = B = M_n(C)^sa`, the **universal/maximal composite** is
  `A ⊠̃ B = M_{n^2}(C)^sa ⊕ M_{n^2}(C)^sa` (two copies).
- The **minimal/standard composite** — *"the usual quantum-mechanical composite"* — is the
  *separate candidate* `M_{n^2}(C)^sa` (one copy), which by Theorem 4.15 / Corollary 4.16
  is an **ideal / direct summand** of the universal one.
- Therefore the **minimal and maximal composites do NOT coincide** for `M_n(C)^sa`: they
  differ by exactly one extra `M_{n^2}(C)^sa` summand (the *extra classical bit*).

### 2.4 The "extra classical bit," stated as such — abstract, footnote 2, and §6 (pp.1–4, 39)

- **Abstract (p.1):** *"This category unifies finite-dimensional real, complex and
  quaternionic mixed-state quantum mechanics, except that the composite of two complex
  quantum systems comes with an extra classical bit."*
- **Footnote 2 (p.4):** points to *"Examples 6.3 and 6.11"* for the corrected
  compact-closure / extra-bit discussion.
- **Example 6.3 (p.35), verbatim:** with standard embeddings,
  `(C_n, M_n(C)) ⊙ (R_k, M_k(C)) = (C_{nk}, M_{nk}(C))` — the **standard composite is the
  simple `M_{nk}(C)`** (the minimal one).
- **§6.3 discussion (p.39), verbatim:** for the universal embedding, *"the tensor product
  is not the usual one: `C_n ⊠̃ C_k = C_{nk} ⊕ C_{nk}`, rather than `C_{nk}`"*, and the
  map on `C^*(C_n) = M_n(C) ⊕ M_n(C)` that *"swaps the two summands ... effects the
  transpose automorphism on `C_n`. This is not permitted in orthodox QM."*

So BGW are explicit and repeated: the **universal (maximal)** composite of two complex
systems carries an **extra classical bit** and is **strictly larger** than the **standard
(minimal)** composite `M_{n^2}(C)^sa`.

### 2.5 Scope and hypotheses of the BGW statement (recorded, not paraphrased loosely)

- Theorem 4.15 and Corollary 4.16 require `A`, `B` **simple, special** EJAs. `M_n(C)^sa` is
  simple and special, so they apply.
- The *standard* composite `M_{n^2}(C)^sa` is the **locally tomographic** one. BGW's general
  notion of composite (Definition 4.1) **does not require tomographic locality** (abstract,
  p.1: *"Our notion of composite requires neither tomographic locality, nor preservation of
  purity under tensor product"*); the universal tensor product `A ⊠̃ B` is, in general,
  **larger** than the vector-space tensor product `A ⊗ B` (p.3) and is **not** in general
  locally tomographic.
- The fact that the **only** EJAs with a *locally tomographic* composite with a qubit are
  the **complex** quantum systems is BGW **Proposition 3.10** (= Hanche-Olsen, [30] Thm 5.5,
  p.21). This is the result that makes the *minimal* (locally tomographic) composite
  single out `M_n(C)^sa` — i.e. it is the engine behind Paper 5's local-tomography selection
  of the complex field, and behind clause (iii) carrying the observer to `M_n(C)^sa`.

> **Numbering caveat (record for the verifier).** The arXiv **v3 / published Quantum**
> text labels the "no composite with an exceptional factor" result as **Proposition 4.14**
> (p.28): *"If `A` contains an exceptional ideal and `B` contains a nontrivial ideal, there
> exists no composite `AB` satisfying the conditions of Definition 1."* The **abstract /
> intro result-map (p.4)** and some secondary sources refer to this as **"Corollary 4.14."**
> Same mathematical content; cite as **"BGW Proposition 4.14 (intro/abstract: Corollary
> 4.14)."** Theorem 4.12 and Theorem 4.15 are labeled identically in body and intro.

### 2.6 Hanche-Olsen corroboration (special ⇒ universal tensor product exists)

The universal tensor product `A ⊠̃ B` (Definition 3.8) is built from the universal
`C^*`-algebras `C^*(A)`, `C^*(B)`. BGW p.18 (citing Hanche-Olsen [30], Theorem 4.1):

> *"It is an important fact that `A` is exceptional iff `C^*(A) = {0}`."*

Hence a simple EJA admits a faithful universal representation (and so the universal tensor
product) **iff it is special**. `M_n(C)^sa` is **special** (it is literally the self-adjoint
part of the complex `*`-algebra `M_n(C)` — BGW p.2, the JvNW classification: special EJAs
are the self-adjoint parts of real/complex/quaternionic matrix algebras and spin factors).
The exceptional `h_3(O)` has `C^*(h_3(O)) = {0}` and admits **no** universal tensor product
— the contrast that grounds the *other* (non-composability) side of the two-composites
distinction (60-01, `two-composites.md` (B)).

**Corroboration summary:** Hanche-Olsen ⇒ `M_n(C)^sa` special ⇒ universal/maximal composite
*exists* (= `M_{n^2}(C)^sa ⊕ M_{n^2}(C)^sa` by Table 2); the standard/minimal composite
`M_{n^2}(C)^sa` *also* exists and is a direct summand of it (Cor. 4.16). Both composites
exist; they **do not coincide**.

---

## 3. Clause (iii) auto-satisfaction — shown AS WRITTEN (not weakened)

Clause (iii) of Paper 5 Def 1, reproduced **verbatim** from the LIVE paper
`qm-from-self-modeling/main.tex` (`sms:minimal`, lines 351–353):

> (iii) `V_{BM}` is the minimal composite OUS carrying product states, product effects,
> non-signaling constraints, and product-form sequential product;

**Claim.** For `A = M_n(C)^sa` (with `V_B = V_M = M_n(C)^sa`, `phi = id`), clause (iii) is
satisfied by the **minimal/standard composite** `V_BM = M_{n^2}(C)^sa`. Each of the four
carried data, **as written**, is checked — none dropped, none relaxed:

1. **product states.** `M_{n^2}(C)^sa = M_n(C)^sa ⊗ M_n(C)^sa` carries product states
   `ρ_B ⊗ ρ_M` (the standard QM tensor product of density matrices). ✓
2. **product effects.** It carries product effects `a ⊗ b`, `a ∈ [0,I]_B`, `b ∈ [0,I]_M`
   (BGW Proposition 4.5, p.24: *"Let `p ∈ A` and `q ∈ B` be projections. Then `p ⊗ q` is a
   projection in `AB`"* — product effects are genuine effects of the composite). ✓
3. **non-signaling constraints.** The standard composite is the non-signaling one (BGW
   Definition 4.1 imposes the no-signaling condition (b); the standard complex-QM tensor
   product satisfies it — testing the body and updating the model act on separate
   tensor factors). ✓
4. **product-form sequential product.** The self-modeling sequential product
   `a & b = sqrt(a) · b · sqrt(a)` acts in product form across the body–model split on
   `M_n(C)^sa ⊗ M_n(C)^sa` (the Lüders form factorizes on product effects; this is the
   ordinary complex-QM sequential/Lüders update, which respects the tensor split). ✓

**Minimality.** `M_{n^2}(C)^sa` is **simple** (no nontrivial direct-sum decomposition), so
it is the *smallest* composite carrying exactly this data — *"the composite has no hidden
structure"* (Paper 5 unpacking of `sms:minimal`, lines 375–384). The **maximal/universal**
composite `M_{n^2}(C)^sa ⊕ M_{n^2}(C)^sa` is **NOT** minimal: it has a nontrivial direct-sum
decomposition (the extra classical bit), i.e. it carries states/effects (the classical bit's
basis states) that the product measurements treat as a *separable extra sector* — precisely
the *"hidden structure"* minimality forbids. Hence the clause-(iii) object is the
**minimal** composite `M_{n^2}(C)^sa`, and minimality **selects it over** the maximal one.

> **Why this is "auto-satisfaction" (the corrected mechanism).** clause (iii) is satisfied
> for `M_n(C)^sa` **not** because "minimal = maximal" (they don't coincide), **but** because
> the minimal composite required by clause (iii) *exists and is the well-behaved, simple,
> locally-tomographic* `M_{n^2}(C)^sa` — which by Theorem 4.15 / Corollary 4.16 sits as an
> **ideal / direct summand** of the universal one. The minimality demand in clause (iii)
> *picks out exactly this summand*. So the **right** statement of `rem:converse` is:
>
> > For complex matrix algebras `M_n(C)^sa`, the **minimal (locally tomographic) composite**
> > `M_{n^2}(C)^sa` exists and is a direct summand of the maximal (universal) composite
> > `M_{n^2}(C)^sa ⊕ M_{n^2}(C)^sa`; clause (iii)'s *minimality* selects the former, so
> > clause (iii) is automatically satisfied — **but minimal and maximal do NOT coincide;
> > the maximal carries an extra classical bit (BGW Table 2, Cor. 4.16, Ex. 6.3/6.11).**

clause (iii) is thereby met **as written** (`fp-redefine-iii` rejected at the source: not
one of the four data was dropped or relaxed, and "minimal" is used in its full force —
indeed it is the very lever that selects `M_{n^2}(C)^sa` over the extra-bit composite).

---

## 4. PROVENANCE FLAG (mandatory)

> ╔══════════════════════════════════════════════════════════════════════════════════╗
> ║ **PROVENANCE FLAG — `rem:converse` is NOT yet in the live paper.**                  ║
> ║                                                                                    ║
> ║ `rem:converse` is **PROMPT-INLINE AUTHORITATIVE** (source:                          ║
> ║ `~/scratch/get-physics-done/p5-basin-restriction-prompt.md`, "Inline definitions"  ║
> ║ → Paper 7 `rem:converse`). It is **NOT** a labeled remark in the LIVE paper         ║
> ║ `~/repos/blog/landing/papers/sm-from-self-modeling/sections/complexification.tex`.  ║
> ║                                                                                    ║
> ║ **Verified by inspection (grep, 2026-05-23):**                                      ║
> ║   • `grep -n "rem:converse" complexification.tex`  →  **0 matches** (exit 1).       ║
> ║   • `lem:bottleneck` IS present — `\label{lem:bottleneck}` at **line 409**.          ║
> ║   • Other labeled remarks present: `rem:basin-scope` (158), `rem:gap-B1` (207),     ║
> ║     `rem:observer-universe` (231), `rem:minkowski` (490), `rem:sel-vs-force` (503),  ║
> ║     `rem:complexification-scope` (1072), and others — but **NO `rem:converse`**.     ║
> ║                                                                                    ║
> ║ **Do NOT cite `rem:converse` as already-published.** The milestone may PRODUCE it   ║
> ║ as a follow-up (**FUTR-01**).                                                        ║
> ║                                                                                    ║
> ║ **Prospective insertion point (for FUTR-01):** immediately AFTER `lem:bottleneck`   ║
> ║ (line 409 + its proof block) in `complexification.tex` — the lemma supplies the     ║
> ║ slice `A = M_3(C)^sa` whose self-model `rem:converse` would instantiate (n = 3).     ║
> ║                                                                                    ║
> ║ **WORDING CONSTRAINT for FUTR-01:** the inserted remark must NOT say "minimal =      ║
> ║ maximal coincide." It must state the **corrected** form (§3 box): the minimal       ║
> ║ (locally tomographic) composite `M_{n^2}(C)^sa` exists as a direct summand of the    ║
> ║ universal composite `M_{n^2}(C)^sa ⊕ M_{n^2}(C)^sa` (BGW Cor. 4.16), and clause      ║
> ║ (iii)'s minimality selects it; the universal/maximal composite carries an extra     ║
> ║ classical bit and is strictly larger.                                               ║
> ╚══════════════════════════════════════════════════════════════════════════════════╝

---

## 5. Distinction-preservation note (the existence result SUPPORTS, does not collapse, 60-01)

This existence result **supports** the two-composites distinction earned in 60-01 and does
**NOT** merge the observer's OUS `V_BM` with the BGW universe-tensoring composite
(`fp-conflate-composites` rejected). Explicitly:

- **`V_BM` (OUS internal composite)** is the observer's minimal composite of its *own* body
  `V_B` and model `V_M` — here `M_n(C)^sa ⊗ M_n(C)^sa ≅ M_{n^2}(C)^sa`. It is an *internal*
  construction for **one** self-modeling subsystem.
- **The BGW composite** is the **bifunctor** `⊠̃` tensoring the *whole* universe algebra
  `h_3(O)` with an **external** FRJA — and BGW's result is that `h_3(O)` admits **no**
  such well-behaved composite (it is exceptional, `C^*(h_3(O)) = {0}`).

These are **different categories** (60-01 `two-composites.md`, Categories ledger). The
existence result of this file confirms: the *special* algebra `M_n(C)^sa` (which sits inside
`h_3(O)` as the bottleneck slice, `lem:bottleneck`) **has** its own internal composite
`V_BM = M_{n^2}(C)^sa`, **even though** the ambient `h_3(O)` is BGW-non-composable. This is
exactly the *witness* that `P_VBM` (the OUS-level existence statement) and `¬P_BGW`-style
non-composability are **independent** — and it does so **without** equating the two notions.

- **No collapse found.** BGW's notion of "composite" is the FRJA-monoidal `⊠̃` /standard `AB`
  on the *whole* algebra; Paper 5's clause-(iii) `V_BM` is an OUS internal composite of the
  observer's body and model. The grounding in §2 keeps them type-distinct: the BGW composite
  of `M_n(C)^sa` with `M_m(C)^sa` is a statement about composing **two complex systems**,
  while `V_BM` is the observer's *self*-composite (body ⊗ model). They are **not** identified
  anywhere in this file. **PAUSE condition 1 NOT triggered.**

> **Honest-negative branch (not taken, but wired).** If the grounding had revealed that the
> only sense in which the slice has an "internal composite" *is* the BGW universe-tensoring
> of the whole `h_3(O)` (no type distinction surviving), that would COLLAPSE the distinction
> and trigger PAUSE condition 1. It did not: the existence direction uses the **standard
> composite of `M_n(C)^sa` with itself** (a special-EJA composite, BGW Ex. 6.3), which is a
> different object from `⊠̃` evaluated on `h_3(O)`.

---

## 6. Type-/structural-consistency self-audit

| Load-bearing claim | Subject category | Type-correct? |
|---|---|---|
| `M_n(C)^sa` special, simple FRJA = BGW `C_n` | FRJA | ✓ |
| minimal composite `M_{n^2}(C)^sa` (standard QM) | FRJA (simple) | ✓ |
| maximal composite `M_{n^2}(C)^sa ⊕ M_{n^2}(C)^sa` (universal) | FRJA (not simple) | ✓ |
| "minimal vs maximal" comparison | FRJA-composite ↔ FRJA-composite (**same category**) | ✓ (answer: **NOT equal**) |
| clause (iii) carried by minimal composite `V_BM` | OUS | ✓ (four data verbatim) |
| `dim(V_BM)=dim(V_B)·dim(V_M)` for minimal (`n^4=n^2·n^2`) | OUS dimension bookkeeping | ✓ |
| maximal fails product-dimension (`2n^4≠n^4`) ⇒ extra bit | OUS bookkeeping | ✓ (consistent w/ BGW) |
| `V_BM` ≠ BGW `⊠̃` on `h_3(O)` | OUS vs bifunctor | ✓ (never equated) |

- **Clause (iii) integrity:** four data (product states, product effects, non-signaling,
  product-form sequential product) + minimality present and verbatim. **Not weakened.** ✓
- **No cross-category equation:** `V_BM` (OUS) is never set equal to a BGW-monoidal property
  of `h_3(O)`. ✓
- **Provenance:** BGW statements quoted verbatim with page + theorem numbers; numbering
  caveat (Prop vs Cor 4.14) recorded; `rem:converse` flagged prompt-inline / not-in-paper,
  grep-verified. ✓
- **Honest grounding:** the "coincide" wording is *corrected*, not rubber-stamped; the
  existence + clause-(iii) content is confirmed. ✓

---

## 7. Citations

- **`ref-bgw`** — Barnum, Graydon, Wilce, "Composites and Categories of Euclidean Jordan
  Algebras," *Quantum* **4**, 359 (2020); arXiv:1606.09331v3.
  - Theorem 4.12 (p.28): composite of simple nontrivial EJAs is special, universally
    reversible.
  - Proposition 4.14 (p.28; intro/abstract: "Corollary 4.14"): no composite with an
    exceptional factor (unless the other factor is classical).
  - Theorem 4.15 (p.29): `AB` is an ideal in `A ⊠̃ B` for simple special `A, B`.
  - **Corollary 4.16 + discussion (p.29): the decisive grounding** — for `A = B = C_n`,
    `A ⊠̃ B = M_{n^2}(C)_sa ⊕ M_{n^2}(C)_sa`, with the usual QM composite `M_{n^2}(C)_sa`
    as a *separate* candidate (a direct summand).
  - Definition 3.8 (p.20): universal tensor product. Table 1(a) (p.19):
    `C^*(C_n) = M_n(C) ⊕ M_n(C)`. Table 2 (p.21): `C_n ⊠̃ C_k = C_{nk} ⊕ C_{nk}`.
  - Proposition 3.10 (p.21) = Hanche-Olsen [30] Thm 5.5: only complex systems have locally
    tomographic composites with a qubit.
  - Abstract (p.1), footnote 2 (p.4), Example 6.3 (p.35), §6.3 discussion (p.39): the
    "extra classical bit."
- **`ref-hanche-olsen`** — Hanche-Olsen, universal tensor product of Jordan algebras
  (BGW [30]). `M_n(C)^sa` special ⇒ admits the universal tensor product; exceptional
  `h_3(O)` has `C^*(h_3(O)) = {0}` (BGW p.18) ⇒ no universal tensor product.
- **`ref-lem-bottleneck`** — `~/repos/blog/landing/papers/sm-from-self-modeling/sections/`
  `complexification.tex`, `lem:bottleneck` (line 409): the slice `A ≅ M_3(C)^sa`; grep
  confirms NO `rem:converse` in this file.
- **`ref-paper5-def1`** — `~/repos/blog/landing/papers/qm-from-self-modeling/main.tex`,
  `def:self-modeling-system` (line 342), clauses (i) `sms:finite` (346), (ii) `sms:faithful`
  (349), (iii) `sms:minimal` (351–353, quoted verbatim), (iv) `sms:simple` (354).

---

## 8. Confidence

**[CONFIDENCE: HIGH]** for the **CONFIRMED-WITH-CAVEAT** verdict.

Three independent checks support it:
1. **Direct quotation** of BGW Corollary 4.16's discussion (p.29) stating, for `A=B=C_n`,
   the universal composite `M_{n^2}(C)_sa ⊕ M_{n^2}(C)_sa` *and* the separate usual QM
   composite `M_{n^2}(C)_sa`.
2. **Independent corroboration** from Table 2 (`C_n ⊠̃ C_k = C_{nk} ⊕ C_{nk}`) and
   Table 1(a) (`C^*(C_n) = M_n(C) ⊕ M_n(C)`) — the maximal composite is two copies.
3. **Dimension bookkeeping** (`dim` minimal `= n^4 = n^2·n^2`; `dim` maximal `= 2n^4`) is
   consistent with the "extra classical bit" and with local tomography holding for the
   minimal composite only.

The **existence** of the faithful self-model with composite `M_{n^2}(C)^sa` and **clause
(iii) satisfaction via the minimal composite** are HIGH confidence. The single correction
(minimal ≠ maximal) is HIGH confidence and *strengthens* — not weakens — the honest verdict,
because BGW state it explicitly and repeatedly. What could still warrant a second look (kept
below HIGH on its own): the precise operational verification that the self-modeling
sequential product `a & b` factorizes on the standard composite is asserted from the Lüders
form (§3 item 4) rather than re-derived here — adequate for a literature-grounding plan, but
Phase 61's matrix verification of the slice should confirm it explicitly.
