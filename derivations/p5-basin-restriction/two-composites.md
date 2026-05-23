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

## Independence (DERV-60-02)

**Goal.** Prove the implication

```
  ( h_3(O) is BGW-non-composable )   does NOT entail   ( the observer's V_BM does not exist )
```

i.e. these are **logically independent** statements about objects in **different
categories**. Equivalently: the non-composability of the universe algebra `h_3(O)` does
*not* preclude the existence of the observer's body-model composite `V_BM`. Establishing
this is exactly what stops the downstream RESTRICTION claim from presupposing its own
conclusion.

> **Non-circularity contract (read before the argument).** The argument below uses
> **only** two ingredients: (i) the *category separation* recorded in the Categories
> ledger above, and (ii) Paper 5's *own scoping remark*. It does **not** use: the
> RESTRICTION claim; the conditional expectation `E`/coherent-embedding step; or
> clause-(iii)-satisfaction-on-the-slice. Those are precisely the things RESTRICTION wants
> to conclude, so using any of them here would be circular. See guard (d).

### (a) The two propositions live in different categories — so neither entails the other a priori

Write the two propositions with their category tags from the ledger:

- **P_BGW** := "`h_3(O)` admits no well-behaved Jordan-monoidal composite `⊠`."
  *Category:* a **bifunctor / monoidal-structure** property of the FRJA `h_3(O)` (a
  statement about tensoring the *whole universe algebra* with *another* FRJA system).

- **P_VBM** := "the observer (a self-modeling system) has a minimal internal composite OUS
  `V_BM`." *Category:* an **OUS-level existence** statement about an *internal* composite
  of the observer's *own* body and model.

These are propositions of **different type**. `P_BGW` quantifies over *external* partners
`J` of `h_3(O)` under a monoidal product on the category `FRJA-Sys`; `P_VBM` asserts the
existence of an *internal* OUS construction for one self-modeling subsystem. By the
type-consistency discipline (the pure-math analog of dimensional analysis), **a statement
about whether `h_3(O)` tensors well with another FRJA carries no a-priori information about
whether some subsystem inside `h_3(O)` has its own minimal internal composite.** The two
live in different categories; there is no type-correct inference rule that takes `P_BGW` to
`¬P_VBM`. (Asserting one would be exactly the conflation error `fp-conflate-composites`:
equating an FRJA-monoidal-level proposition with an OUS-level proposition.)

This already breaks the entailment *formally*: to derive `¬P_VBM` from `P_BGW` one would
need a bridge premise of the form "internal-composite-of-a-subsystem-exists ⟺
whole-algebra-is-monoidally-composable." No such bridge is available — and the obvious
candidate bridge *is* RESTRICTION, which we are forbidden to assume (guard (d)). Hence
`P_BGW ⊬ ¬P_VBM`.

### (b) Textual witness: Paper 5 itself treats the two regimes as distinct

The independence is not merely formal; the authors of Paper 5 already regard the two as
different regimes. From `main.tex` (remark at lines 397–401; parallel statement at lines
165–168), verbatim:

> Definition~\ref{def:self-modeling-system} characterizes *composable* self-modelers —
> subsystems that can participate in composites. The non-composable case
> (`h_3(O)`, which admits no composite at all) is treated in a companion paper.

Read at the level of *type*, this says: the `V_BM` construction (clause iii) is the
defining feature of the **composable** regime; `h_3(O)`-non-composability is the defining
feature of the **separate, non-composable** regime treated elsewhere. Paper 5 thus
*already distinguishes* "has an internal composite `V_BM`" (composable self-modeler) from
"`h_3(O)` admits no composite" (non-composable basin). This is direct authorial support
that `P_VBM` and `P_BGW` concern **different objects** — and it is a *given* of the
existing program, not a consequence of RESTRICTION.

### (c) Existence direction (principle only; full BGW grounding deferred to plan 60-02)

It remains to see that `P_VBM` is *not vacuous* — that "lives inside a non-composable
algebra" and "has no internal composite" really can come apart. At the level of **principle**
(we do **not** here verify the four clauses on the slice — that is plan 60-02 / Phase 61):

1. A complex matrix algebra `M_n(C)^sa` is a perfectly good **composable** self-modeler:
   it has its own minimal internal composite OUS `V_BM` (this is the content that
   `rem:converse` will confirm — take `V_M = V_B = M_n(C)^sa`, `phi = id`, internal
   composite `M_n(C)^sa ⊗ M_n(C)^sa ≅ M_{n^2}(C)^sa`). **Provenance caveat:**
   `rem:converse` is **prompt-inline authoritative only** — it is *not yet* a labeled
   remark in the live `complexification.tex` (grep finds `lem:bottleneck` but no
   `rem:converse`), and its "minimal = maximal composite coincide for `M_n(C)^sa`" content
   is to be confirmed against BGW in plan 60-02. We use it here only as a *principle*, not
   as a published result.

2. `M_3(C)^sa ≅ h_3(C_u)` sits **inside** `h_3(O)` as the C*-bottleneck slice
   (`lem:bottleneck`, complexification.tex line 409: the maximal complex C*-target Jordan
   subalgebra, a single `F_4`-orbit). So here is a concrete situation: a special algebra
   `M_3(C)^sa` that (by item 1, in principle) **has** its own internal composite `V_BM`,
   while **sitting inside** the FRJA `h_3(O)` that (by `P_BGW`) has **no** monoidal
   composite.

Therefore "**lives inside a non-composable algebra**" and "**has no internal composite of
its own**" are **not the same thing**: the bottleneck slice is a witness to a subsystem of
`h_3(O)` that, in principle, carries the internal-composite structure `P_VBM` asks for,
even though the ambient `h_3(O)` is BGW-non-composable. This makes `P_VBM` non-vacuous in
the presence of `P_BGW`, completing the independence: `P_BGW` and `P_VBM` can hold
simultaneously, so `P_BGW ⊬ ¬P_VBM`.

> **Scope discipline (does NOT pre-empt 60-02 / Phase 61).** Item (c) is stated as
> *principle / forward reference*. We do **not** claim here that the slice *satisfies*
> clause (iii) as induced from `h_3(O)` — that is the coherent-embedding question (Phase
> 62) and the clause-checking (Phase 61). We claim only the weaker, type-level fact:
> *inhabiting a non-composable ambient does not, by itself, deprive a subsystem of an
> internal composite.* That weaker fact is all the independence argument needs, and it
> does not touch `E`.

### (d) Circularity guard (explicit)

The circular argument we must avoid is:

> **(CIRCULAR)** Assume RESTRICTION (the slice `A` satisfies clause (iii) coherently
> induced from `h_3(O)` under `E`); conclude that the observer's `V_BM` exists inside
> `h_3(O)`; therefore the two composites are distinct.

This would *assume the conclusion*: RESTRICTION is the very thing the milestone sets out to
prove, and it already presupposes that `V_BM` is realized inside `h_3(O)`. **The argument
in (a)–(c) never uses RESTRICTION.** Explicitly, none of the following appears as a premise
above:

- **RESTRICTION** itself — not used (the independence is from category separation (a) +
  Paper 5's scoping remark (b));
- the **coherent-embedding step** / the conditional expectation `E` — not used (`E` is in
  the ledger only as a forward reference and appears in *no* inference);
- **clause-(iii)-satisfaction-on-the-slice** — not used (item (c) is explicitly
  *principle only* and does **not** assert the slice satisfies clause (iii)).

The independence is established **from category separation + Paper 5's own scoping remark**,
with the existence direction supplied only at the level of principle. The disconfirming
direction (assuming RESTRICTION) is named and *not taken*. Hence the distinction is
**earned, not assumed.**

### (e) Honest-negative branch (the disconfirming condition)

The argument has a built-in failure mode, and it is a **valid, valuable outcome** if it
triggers:

> **(COLLAPSE)** If, on close inspection, the witness (b)+(c) reveals the observer's
> `V_BM` and the BGW *universe*-composite of `h_3(O)` to be the **same construction** —
> i.e. the only sense in which the slice has an "internal composite" turns out to *be* the
> BGW monoidal composite of the whole algebra, with no type distinction surviving — then
> `P_BGW` and `P_VBM` are **not** about different objects after all. In that case the
> independence cannot be earned non-circularly, **RESTRICTION is circular/false**, and this
> plan must **STOP and surface the milestone's first PAUSE condition** (see `claim.md`
> PAUSE conditions). A second collapse trigger: if the independence argument cannot be made
> *without* invoking RESTRICTION/embedding/slice-satisfaction (latent circularity), the
> distinction likewise cannot be earned ⟹ PAUSE.

**Outcome of this attempt:** No collapse was found. The two propositions are type-distinct
(a), the authors already treat them as distinct regimes (b), and the bottleneck slice
witnesses (in principle) a subsystem of a non-composable ambient that nonetheless can carry
its own internal composite (c) — all without invoking RESTRICTION (d). The distinction is
**EARNED**. (Caveat carried forward: the existence direction (c) rests on the
prompt-authoritative `rem:converse`, whose exact BGW-grounding is confirmed in plan 60-02;
this does not weaken the *type-level* independence, which stands on (a)+(b) alone.)

### Independence — type-consistency self-audit

Every load-bearing sentence above, tagged by the category of its subject:

| Load-bearing claim | Subject category | Type-correct? |
|---|---|---|
| `P_BGW` is a monoidal property of `h_3(O)` | bifunctor/monoidal (FRJA) | ✓ |
| `P_VBM` is an OUS existence statement | OUS | ✓ |
| "no type-correct rule sends `P_BGW` -> `¬P_VBM`" | cross-category *non*-inference | ✓ (this is the whole point: the two are never equated) |
| (b) Paper 5 scopes Def 1 to composable self-modelers; `h_3(O)` separate | OUS-regime vs FRJA-regime, *kept distinct* | ✓ |
| (c) `M_n(C)^sa` has its own internal composite (principle) | OUS (special algebra) | ✓ |
| (c) `M_3(C)^sa ≅ h_3(C_u)` ⊂ `h_3(O)` | FRJA subalgebra inclusion | ✓ (inclusion of algebras, not equation of an OUS with a monoidal property) |
| (d) RESTRICTION/`E`/slice-clause-(iii) **not used** | — | ✓ (verified by inspection + grep in claim.md/attempt-01.md) |

**No sentence equates an OUS-level proposition with an FRJA-monoidal-level proposition.**
`P_VBM` (exists `V_BM`) and `P_BGW` (`h_3(O)` composable/not) are never identified and
never contraposed into each other. ✓

