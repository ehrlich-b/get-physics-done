<!-- ASSERT_CONVENTION: metric_signature=riemannian_fisher, fourier_convention=na, natural_units=natural, gauge_choice=na, renormalization_scheme=na -->
<!-- Pure-algebra / definitional document. No numerics. The "dimensional-analysis" requirement maps to TYPE/CATEGORY consistency: every named object is tagged by category and no inference equates objects of different categories. -->
<!-- Provenance: LIVE papers only (~/repos/blog/landing/papers/). NOT the stale repo papers/. -->

# Two Composites: V_BM vs the BGW Composite of h_3(O)

**Plan:** 60-01 (Phase 60, milestone v15.0) — DERV-60-01
**Purpose:** State, *each entirely in its own terms*, (A) the observer's clause-(iii)
body-model composite `V_BM` and (B) the BGW Jordan-monoidal composite of the universe
algebra `h_3(O)`. These are objects in **different categories**. This file is the
type-consistency ledger that all downstream tasks audit against. Nothing here defines one
notion by reference to the other, and clause (iii) is reproduced verbatim and never
weakened.

---

## Categories table (type-consistency ledger)

Every named object carries exactly one category tag. The pure-math analog of dimensional
analysis is: **no inference may equate, identify, or contrapose objects carrying
different tags.** An OUS-level proposition (e.g. "`V_BM` exists") and an
FRJA-monoidal-level proposition (e.g. "`h_3(O)` is BGW-composable") are *type-distinct*
and may never be set equal.

| Object | Category tag | What it is | Where defined |
|---|---|---|---|
| `V_B` | **OUS** | the observer's *body* order-unit space (a finite-dim spectral OUS) | Paper 5 Def 1, clause (i)/(ii) |
| `V_M` | **OUS** | the observer's *model* order-unit space; `phi: V_B -> V_M` an order isomorphism | Paper 5 Def 1, clause (ii) |
| `V_BM` | **OUS** (composite) | the observer's **minimal internal composite** OUS of body and model (clause iii) | Paper 5 Def 1, clause (iii) / `sms:minimal` |
| `h_3(O)` | **FRJA** | the exceptional, 27-dim, *non-special simple* formally real Jordan algebra (the universe "basin") | BGW 2020; Paper 7 |
| `h_3(C_u)` ≅ `M_3(C)^sa` | **FRJA** (special) / carries OUS structure | the maximal complex C*-target *Jordan subalgebra* inside `h_3(O)` | `lem:bottleneck` (complexification.tex line 409) |
| BGW-composite `(-) ⊠ (-)` | **bifunctor / monoidal-composite** | a *bifunctor* on the category of FRJA-systems (a rule that tensors two FRJA systems into one), subject to the BGW composability axioms | BGW 2020; Hanche-Olsen |
| `E` | **conditional expectation** | a positive unital idempotent `E: h_3(O) -> A` (Effros-Störmer); a *map*, not an algebra or a space | `lem:bottleneck`; **forward reference only** (used in Phase 62, not here) |

**Forward-reference discipline.** `E` appears in this table for completeness of the
ledger, but **no argument in this file uses `E`**. The coherent-embedding question (does
`E` induce clause-(iii) structure on the non-associative ambient?) is Phase 62 and is
deliberately untouched here, so that the Phase 60 distinction is not contaminated by the
embedding step it is supposed to license.

---

## (A) The observer body-model composite `V_BM` — defined in its own terms

**Category: OUS (an order-unit space built from the observer's `V_B` and `V_M`).**

### Clause (iii) verbatim

From the LIVE paper `~/repos/blog/landing/papers/qm-from-self-modeling/main.tex`,
`def:self-modeling-system` (line 342), clause (iii) labelled `sms:minimal` (lines
351–353), reproduced **verbatim**:

> (iii) `V_{BM}` is the minimal composite OUS carrying product states, product effects,
> non-signaling constraints, and product-form sequential product;

This clause carries **four** pieces of data, all of which must be present (the
type-consistency check forbids dropping any of them):

1. **product states** — states of the composite that factorize across body and model;
2. **product effects** — effects (measurements) of the composite that factorize across
   body and model;
3. **non-signaling constraints** — testing the body and updating the model are operations
   on *separate* subsystems (no superluminal/instantaneous influence between the two
   factors);
4. **product-form sequential product** — the self-modeling sequential product
   `a & b = sqrt(a) b sqrt(a)` (Luders / self-modeling form, temporally asymmetric;
   `def:product-sp` in Paper 5) acts in product form across the body-model split.

And the qualifier **minimal**: `V_BM` is the *smallest* composite OUS carrying exactly
this data — "the composite has no hidden structure" (Paper 5, unpacking of `sms:minimal`,
lines 375–384: *"If the body-model composite carried states that product measurements
could not distinguish, those states would be opaque to the self-modeler... Minimality
says: the composite has no such hidden structure."*).

### What `V_BM` is, categorially

`V_BM` is an **order-unit space** — specifically, the minimal composite OUS of the two
OUSs `V_B` and `V_M` that belong to a *single self-modeling observer*. It is an *internal*
construction: the observer's only measurements are product measurements on its own body
and its own model. `V_BM` is the arena in which "the body models itself via the model"
takes place.

### Role of `V_BM` in Paper 5

`V_BM`'s **minimality** is exactly the lever that forces **local tomography**: if the
composite is minimal (no states opaque to product measurements), then the composite state
is determined by the local (product) measurement statistics. Local tomography is the
property that, in Paper 5's exclusion argument
(`thm:local-tomo`, referenced at main.tex line 370), rules out the real and quaternionic
Jordan algebras and singles out the **complex** field. So clause (iii) is the step that
carries the observer to `M_n(C)^sa`.

### Scope of `V_BM` (Paper 5's own words)

Paper 5 explicitly scopes this construction to **composable** self-modelers. From
`main.tex` (the remark at lines 393–402, and the parallel statement at lines 165–168),
reproduced verbatim:

> Definition~\ref{def:self-modeling-system} characterizes *composable* self-modelers —
> subsystems that can participate in composites. The non-composable case
> (`h_3(O)`, which admits no composite at all) is treated in a companion paper.

So `V_BM` is, *by construction*, an object that exists for a **composable** self-modeler.
The paper itself sets the non-composable `h_3(O)` aside as a *different regime*. (This
scoping remark is the textual spine of the Independence argument in Task 2 — it is direct
authorial evidence that the two composite notions are distinct objects, but it is recorded
here only as a *property of `V_BM`'s definition*, not yet wielded as an inference.)

**Citations:** `ref-paper5-def1` (Paper 5 Def 1 + composable/non-composable remark).

---

## (B) The BGW Jordan-monoidal composite of the universe algebra `h_3(O)` — defined in its own terms

**Category: bifunctor / monoidal-composite (a statement about the UNIVERSE algebra
`h_3(O)`, NOT an OUS internal-composite statement).**

### What a BGW Jordan-monoidal composite *is*

Following Barnum–Graydon–Wilce (BGW) 2020 and Hanche-Olsen: a **well-behaved
Jordan-monoidal composite** is a **bifunctor**

```
⊠ : FRJA-Sys × FRJA-Sys  ->  FRJA-Sys
```

on the **category of formally real Jordan algebra systems**, assigning to a pair of FRJA
systems `(J_1, J_2)` a composite FRJA system `J_1 ⊠ J_2` that satisfies the BGW
composability axioms (the monoidal coherence/well-behavedness conditions: existence of
product states and product effects, a *local tomography* condition at the level of the
bifunctor, associativity/unit coherence of `⊠`, and compatibility with the Jordan
structure). The Hanche-Olsen *universal tensor product* of two Jordan algebras is the
canonical candidate for such a `⊠`; the question of whether a *given* Jordan algebra
admits a well-behaved composite is the question of whether the universal tensor product
(or any candidate `⊠`) satisfies the well-behavedness axioms when one of the two arguments
is that algebra.

The defining data here is **a bifunctor on a category of algebras** — i.e. a rule for
**tensoring the universe algebra `h_3(O)` with *another* FRJA system** into a new FRJA
system. The object of concern is the *monoidal structure on `FRJA-Sys`*, evaluated with
`h_3(O)` in one slot.

### The fact: `h_3(O)` is BGW-non-composable

`h_3(O)` is the **unique non-special simple** formally real Jordan algebra (the 27-dim
exceptional / Albert algebra; it is not isomorphic to a Jordan algebra of self-adjoint
operators on any associative \*-algebra). BGW 2020 establishes:

> **`h_3(O)` admits NO well-behaved Jordan-monoidal composite.** There is no bifunctor
> `⊠` (equivalently: the universal Jordan tensor product fails the well-behavedness
> axioms) producing a good composite `h_3(O) ⊠ J` of `h_3(O)` with another FRJA system
> `J`. This is the **universe-tensoring** statement: `h_3(O)`, taken *as a whole*, cannot
> be combined with another system in a tomographically/monoidally well-behaved way.

Equivalently (Hanche-Olsen): a formally real Jordan algebra admits a well-behaved
universal tensor product iff it is **special** (a Jordan algebra of self-adjoint operators
on an associative \*-algebra). `h_3(O)` is the unique simple FRJA that is *not* special,
hence the unique simple FRJA with no well-behaved composite.

### What `h_3(O)`-non-composability is, categorially

It is a **monoidal-structure (bifunctor) statement about the single FRJA `h_3(O)`**: a
statement of the form "the monoidal product `⊠` on `FRJA-Sys` cannot be evaluated
well-behavedly with `h_3(O)` in one slot." It says nothing, *a priori*, about the internal
order-unit-space structure of any *subsystem* sitting inside `h_3(O)`, and in particular
it is **not** an OUS internal-composite statement.

**Citations:** `ref-bgw` (BGW 2020, FRJA composability / universe-tensoring),
`ref-hanche-olsen` (Hanche-Olsen, universal tensor product; special vs exceptional).

---

## Type-consistency self-audit of (A) and (B)

Walking the two definition blocks against the Categories ledger:

| Sentence's subject | Category | OK? |
|---|---|---|
| "`V_BM` is the minimal composite OUS..." | OUS | ✓ uses only OUS-level data (states, effects, non-signaling, sequential product on `V_B`,`V_M`) |
| "`V_BM`'s minimality forces local tomography -> complex field" | OUS -> field selection | ✓ stays at the OUS level; conclusion is about the OUS's underlying field |
| "a BGW composite is a bifunctor `⊠` on `FRJA-Sys`" | bifunctor/monoidal | ✓ uses only category-of-algebras data |
| "`h_3(O)` admits no well-behaved `⊠`" | bifunctor/monoidal property of `h_3(O)` | ✓ a property of the FRJA `h_3(O)` under the monoidal structure |

- **Clause (iii) integrity:** all four carried data (product states, product effects,
  non-signaling, product-form sequential product) + minimality are present and verbatim.
  **Not weakened.**
- **No cross-definition:** block (A) never mentions `⊠`, BGW-composability, or `h_3(O)`
  in defining `V_BM`; block (B) never mentions `V_B`, `V_M`, or `V_BM` in defining the
  BGW composite. **Zero cross-contamination.**
- **(B) is a monoidal/bifunctor property of the universe algebra `h_3(O)`,** not an OUS
  internal-composite claim. ✓
- **Provenance:** all citations point to the LIVE papers / BGW / Hanche-Olsen; `E` is a
  forward reference only and is unused; **no claim that `rem:converse` is a labeled remark
  in the live paper** (it is not — see claim.md provenance guard).

---

<!-- The Independence section is appended below in Task 2 (DERV-60-02). -->
